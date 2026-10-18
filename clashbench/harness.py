#!/usr/bin/env python
"""ClashBench harness: diagnosis, meta-skill compilation, clash curriculum, reflective refinement, evaluation.

Stages (run in this order for a full pipeline):
  export      write every skill as SKILL.md under skills/<job>/ (input for external compilers)
  diag        no skill, each skill alone, both skills in both orders, skill + unrelated skill
  compile     build merged meta-skills with the local model (free merge, structured, oracle-relations)
  curriculum  propose clash-provoking requests and score them without training
  refine      GEPA-style reflective refinement of a meta-skill on curriculum requests
  treat       evaluate precedence baselines and every meta-skill variant on the held-out requests

All generations are cached on disk, so an interrupted stage resumes where it stopped.
"""
import argparse
import hashlib
import json
import os
import random
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
if os.path.isdir("/scratch2/prazmara/hf_cache"):  # the authors' cluster; elsewhere the normal Hugging Face defaults apply
    os.environ.setdefault("HF_HOME", "/scratch2/prazmara/hf_cache")
    os.environ.setdefault("HF_HUB_OFFLINE", "1")

from spec import norm, render_skill, rule_order, score, target_set  # noqa: E402
import jobs_core  # noqa: E402

JOBS = list(jobs_core.JOBS)
try:
    import jobs_extra  # noqa: E402
    JOBS += list(jobs_extra.JOBS)
except ImportError:
    pass
JOBMAP = {j.id: j for j in JOBS}
MODELS = {"qwen4b": "Qwen/Qwen3-4B-Instruct-2507", "llama8b": "meta-llama/Llama-3.1-8B-Instruct",
          "qwen7b": "Qwen/Qwen2.5-7B-Instruct", "qwen14b": "Qwen/Qwen2.5-14B-Instruct", "qwen32b": "Qwen/Qwen2.5-32B-Instruct",
          "mistral7b": "mistralai/Mistral-7B-Instruct-v0.3", "gemma9b": "google/gemma-2-9b-it", "phi4": "microsoft/phi-4"}
T0 = time.time()


def log(*a):
    print(f"[{time.time() - T0:7.0f}s]", *a, flush=True)


# ----------------------------------------------------------------------------- model wrapper
class LM:
    def __init__(self, tag, tok_budget=22000):
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer
        self.torch, self.tag, self.mid = torch, tag, MODELS[tag]
        self.tok = AutoTokenizer.from_pretrained(self.mid)
        self.tok.padding_side = "left"
        if self.tok.pad_token is None:
            v = self.tok.get_vocab()
            self.tok.pad_token = "<|finetune_right_pad_id|>" if "<|finetune_right_pad_id|>" in v else self.tok.eos_token
        self.model = AutoModelForCausalLM.from_pretrained(self.mid, torch_dtype=torch.float16).cuda().eval()
        os.makedirs(f"{ROOT}/runs/{tag}", exist_ok=True)
        self.cache_path = f"{ROOT}/runs/{tag}/cache.jsonl"
        self.cache = {}
        if os.path.exists(self.cache_path):
            for line in open(self.cache_path):
                try:
                    d = json.loads(line)
                    self.cache[d["k"]] = d["o"]
                except Exception:
                    pass
        self.fh = open(self.cache_path, "a")
        self.tok_budget, self.n_gen, self.n_hit = tok_budget, 0, 0
        log(f"loaded {self.mid}; cache entries {len(self.cache)}; gpu mem {torch.cuda.memory_allocated() / 1e9:.1f} GB")

    def _key(self, msgs, max_new, temp, seed):
        return hashlib.sha1(json.dumps([self.mid, msgs, max_new, temp, seed], sort_keys=True).encode()).hexdigest()

    def chat(self, batch_msgs, max_new=320, temp=0.0, seed=0, desc=""):
        keys = [self._key(m, max_new, temp, seed) for m in batch_msgs]
        todo = {}
        for k, m in zip(keys, batch_msgs):
            if k in self.cache:
                self.n_hit += 1
            elif k not in todo:
                todo[k] = m
        if todo:
            items = list(todo.items())
            texts = [self._render(m) for _, m in items]
            lens = [len(self.tok(t, add_special_tokens=False).input_ids) for t in texts]
            order = sorted(range(len(items)), key=lambda i: -lens[i])
            i, t0 = 0, time.time()
            while i < len(order):
                per = lens[order[i]] + max_new
                bs = max(1, min(48, self.tok_budget // per))
                idx = order[i:i + bs]
                try:
                    outs = self._gen([texts[j] for j in idx], max_new, temp, seed * 100003 + i)
                except self.torch.cuda.OutOfMemoryError:
                    self.torch.cuda.empty_cache()
                    self.tok_budget = max(3000, int(self.tok_budget * 0.6))
                    log(f"OOM, token budget now {self.tok_budget}")
                    time.sleep(5)
                    continue
                for j, o in zip(idx, outs):
                    self.cache[items[j][0]] = o
                    self.fh.write(json.dumps({"k": items[j][0], "o": o}) + "\n")
                self.fh.flush()
                i += len(idx)
                self.n_gen += len(idx)
                if (i // max(1, bs)) % 4 == 0 or i >= len(order):
                    log(f"  {desc} {i}/{len(order)} generated ({(time.time() - t0) / max(i, 1):.2f} s/item, bs {bs})")
        return [self.cache[k] for k in keys]

    def _render(self, m):
        try:
            return self.tok.apply_chat_template(m, tokenize=False, add_generation_prompt=True)
        except Exception:  # chat templates without a system role (for example Gemma): fold it into the user turn
            if m and m[0]["role"] == "system":
                m2 = [{"role": "user", "content": m[0]["content"] + "\n\n" + m[1]["content"]}] + list(m[2:])
                return self.tok.apply_chat_template(m2, tokenize=False, add_generation_prompt=True)
            raise

    def _gen(self, texts, max_new, temp, seed):
        torch = self.torch
        enc = self.tok(texts, return_tensors="pt", padding=True, add_special_tokens=False).to("cuda")
        kw = dict(max_new_tokens=max_new, pad_token_id=self.tok.pad_token_id)
        if temp > 0:
            torch.manual_seed(seed)
            kw.update(do_sample=True, temperature=temp, top_p=0.95, top_k=None)
        else:
            kw.update(do_sample=False, temperature=None, top_p=None, top_k=None)
        with torch.no_grad():
            g = self.model.generate(**enc, **kw)
        return self.tok.batch_decode(g[:, enc.input_ids.shape[1]:], skip_special_tokens=True)


class APILM:
    """Same interface as LM, backed by any OpenAI-compatible chat completions endpoint.

    The key is read from an environment variable and never written to disk. Outputs are cached like local ones.
    """

    def __init__(self, tag, model, base, key_env, workers=8):
        self.tag, self.mid, self.base, self.workers = tag, model, base.rstrip("/"), workers
        self.key = os.environ.get(key_env, "")
        if not self.key:
            sys.exit(f"environment variable {key_env} is not set")
        os.makedirs(f"{ROOT}/runs/{tag}", exist_ok=True)
        self.cache_path = f"{ROOT}/runs/{tag}/cache.jsonl"
        self.cache = {}
        if os.path.exists(self.cache_path):
            for line in open(self.cache_path):
                try:
                    d = json.loads(line)
                    self.cache[d["k"]] = d["o"]
                except Exception:
                    pass
        self.fh = open(self.cache_path, "a")
        self.n_gen, self.n_hit, self.tok_field, self.send_temp = 0, 0, "max_tokens", True
        self.usage = dict(prompt_tokens=0, completion_tokens=0)
        log(f"API model {model} at {self.base}; cache entries {len(self.cache)}")

    def _key(self, msgs, max_new, temp, seed):
        return hashlib.sha1(json.dumps([self.mid, msgs, max_new, temp, seed], sort_keys=True).encode()).hexdigest()

    def _one(self, msgs, max_new, temp):
        import urllib.error
        import urllib.request
        for attempt in range(8):
            body = {"model": self.mid, "messages": msgs, self.tok_field: max_new}
            if self.send_temp:
                body["temperature"] = temp
            req = urllib.request.Request(self.base + "/chat/completions", data=json.dumps(body).encode(),
                                         headers={"Content-Type": "application/json", "Authorization": "Bearer " + self.key})
            try:
                with urllib.request.urlopen(req, timeout=180) as r:
                    d = json.loads(r.read())
                u = d.get("usage") or {}
                self.usage["prompt_tokens"] += u.get("prompt_tokens", 0)
                self.usage["completion_tokens"] += u.get("completion_tokens", 0)
                return d["choices"][0]["message"].get("content") or ""
            except urllib.error.HTTPError as e:
                msg = e.read().decode("utf-8", "replace")[:400]
                if e.code == 400 and "max_completion_tokens" in msg and self.tok_field == "max_tokens":
                    self.tok_field = "max_completion_tokens"
                    continue
                if e.code == 400 and "temperature" in msg and self.send_temp:
                    self.send_temp = False
                    continue
                if e.code in (401, 403, 404):
                    sys.exit(f"API error {e.code}: {msg}")
                log(f"  API {e.code}, retry {attempt}: {msg[:120]}")
            except Exception as e:  # timeouts, connection resets
                log(f"  API exception, retry {attempt}: {str(e)[:120]}")
            time.sleep(min(60, 2 ** attempt))
        return ""

    def chat(self, batch_msgs, max_new=320, temp=0.0, seed=0, desc=""):
        from concurrent.futures import ThreadPoolExecutor
        keys = [self._key(m, max_new, temp, seed) for m in batch_msgs]
        todo = {}
        for k, m in zip(keys, batch_msgs):
            if k in self.cache:
                self.n_hit += 1
            elif k not in todo:
                todo[k] = m
        if todo:
            items = list(todo.items())
            t0 = time.time()
            with ThreadPoolExecutor(self.workers) as ex:
                for n, (k, o) in enumerate(zip([k for k, _ in items], ex.map(lambda km: self._one(km[1], max_new, temp), items))):
                    if o:
                        self.cache[k] = o
                        self.fh.write(json.dumps({"k": k, "o": o}) + "\n")
                        self.fh.flush()
                    else:
                        self.cache.setdefault(k, "")
                    self.n_gen += 1
                    if (n + 1) % 50 == 0 or n + 1 == len(items):
                        log(f"  {desc} {n + 1}/{len(items)} ({(time.time() - t0) / (n + 1):.2f} s/item) tokens so far {self.usage}")
        return [self.cache[k] for k in keys]


# ----------------------------------------------------------------------------- prompts
SYS_BASE = "You are an assistant working in a software team's workspace."


def sys_prompt(skill_texts, precedence=None):
    if not skill_texts:
        return SYS_BASE
    s = (SYS_BASE + " The skills below are installed and loaded for this session. "
         "Follow every rule of every loaded skill that applies to the request.\n\n")
    s += "\n\n".join(f"<skill>\n{t}\n</skill>" for t in skill_texts)
    if precedence:
        s += (f"\n\nIf two loaded skills give conflicting instructions, the skill `{precedence}` takes precedence. "
              "Otherwise follow all rules of all loaded skills.")
    return s


def user_prompt(job, request):
    return f"{request}\n\nReply with the {job.artifact} only, with no commentary before or after it."


def skill_text(job, letter, with_example=True, drop=()):
    return render_skill(job.skills[letter], job, with_example=with_example, drop=drop)


def union_skill(job, P, precedence=False):
    """Code-only merge: every rule of both skills in one file, no examples, nothing resolved."""
    Q = "B" if P == "A" else "A"
    sp, sq = job.skills[P], job.skills[Q]
    t = ["---", f"name: {sp.name}+{sq.name}",
         f"description: Combined rules of `{sp.name}` and `{sq.name}`. Use for any {job.artifact}.", "---", "",
         f"# Combined skill: {sp.name} + {sq.name}", "", "Follow every rule below.", "",
         f"## Rules from `{sp.name}`", ""] + [f"- {r.text}" for r in rule_order(sp, job)]
    t += ["", f"## Rules from `{sq.name}`", ""] + [f"- {r.text}" for r in rule_order(sq, job)]
    if precedence:
        t += ["", f"If two rules cannot both hold, the rule from `{sp.name}` wins."]
    return "\n".join(t)


def final_part(text):
    """For the checklist condition: keep what follows the last FINAL: marker."""
    i = text.rfind("FINAL:")
    return text[i + 6:].strip() if i >= 0 else text


def unrelated(job):
    i = JOBS.index(job)
    return JOBS[(i + len(JOBS) // 2) % len(JOBS)]


def run(lm, specs, out_path=None, temp=0.0, seed=0, desc=""):
    """specs: dicts with job, request, system and any metadata. Returns records with output and scores."""
    msgs = [[{"role": "system", "content": s["system"]},
             {"role": "user", "content": s.get("user") or user_prompt(JOBMAP[s["job"]], s["request"])}] for s in specs]
    outs = [None] * len(specs)
    by = {}
    for i, s in enumerate(specs):
        by.setdefault(JOBMAP[s["job"]].max_new_tokens + s.get("extra_tokens", 0), []).append(i)
    for mn, idxs in sorted(by.items()):
        o = lm.chat([msgs[i] for i in idxs], max_new=mn, temp=temp, seed=seed, desc=f"{desc}[{mn}]")
        for i, x in zip(idxs, o):
            outs[i] = x
    recs = []
    for s, o in zip(specs, outs):
        r = {k: v for k, v in s.items() if k not in ("system", "user", "extra_tokens", "post")}
        if s.get("post") == "final":
            r["full_output"], o = o, final_part(o)
        r["output"], r["scores"] = o, score(JOBMAP[s["job"]], o)
        recs.append(r)
    if out_path:
        with open(out_path, "w") as f:
            for r in recs:
                f.write(json.dumps(r) + "\n")
        log(f"wrote {len(recs)} records to {out_path}")
    return recs


def frac_target(job, primary, scores):
    t = target_set(job, primary)
    return sum(scores[f"{l}.{k}"] for l, k, _ in t) / len(t)


# ----------------------------------------------------------------------------- stage: export / diag
def stage_export(args):
    for job in JOBS:
        d = f"{ROOT}/skills/{job.id}"
        os.makedirs(d, exist_ok=True)
        for L in "AB":
            open(f"{d}/{L}.md", "w").write(skill_text(job, L) + "\n")
        json.dump({"artifact": job.artifact, "example_request": job.example_request,
                   "A": job.skills["A"].name, "B": job.skills["B"].name}, open(f"{d}/job.json", "w"), indent=1)
    log(f"exported {len(JOBS)} jobs to {ROOT}/skills")


def stage_diag(lm, args):
    specs = []
    for job in args.jobs:
        A, B = skill_text(job, "A"), skill_text(job, "B")
        C = skill_text(unrelated(job), "A")
        conds = {"none": [], "A": [A], "B": [B], "AB": [A, B], "BA": [B, A], "AC": [A, C], "CA": [C, A],
                 "BC": [B, C], "CB": [C, B]}
        for ti, req in enumerate(job.tasks[:args.limit_tasks]):
            for c, sk in conds.items():
                specs.append(dict(job=job.id, task=ti, request=req, cond=c, system=sys_prompt(sk)))
    run(lm, specs, f"{ROOT}/runs/{lm.tag}/diag.jsonl", desc="diag")


# ----------------------------------------------------------------------------- stage: compile
def parse_json_array(text):
    i, j = text.find("["), text.rfind("]")
    if i < 0 or j <= i:
        return None
    try:
        v = json.loads(text[i:j + 1])
        return v if isinstance(v, list) else None
    except Exception:
        return None


def ws(s):
    return re.sub(r"\s+", " ", s).strip()


def extract_rules(lm, texts):
    """LLM lists the atomic rules of each skill, word for word. Non-verbatim items are dropped."""
    msgs = [[{"role": "system", "content": "You analyze instruction files for AI assistants."},
             {"role": "user", "content": "Below is an agent skill (SKILL.md). List every rule it imposes on the output. "
              "Copy each rule word for word from the skill, one rule per item, without the leading dash. "
              "Do not include the example or the description. Return a JSON array of strings and nothing else.\n\n"
              f"<skill>\n{t}\n</skill>"}] for t in texts]
    outs = lm.chat(msgs, max_new=700, desc="extract")
    res = []
    for t, o in zip(texts, outs):
        arr = parse_json_array(o) or []
        body = ws(t)
        ok = []
        for x in arr:
            if isinstance(x, str):
                x = ws(x.lstrip("- "))
                if len(x) > 8 and x in body and x not in ok:
                    ok.append(x)
        path = "llm"
        if len(ok) < 3:  # structural fallback: bullet lines of the Rules section
            m = re.search(r"## Rules\s*\n(.*?)(\n## |\Z)", t, re.S)
            ok = [ws(l[2:]) for l in (m.group(1).split("\n") if m else []) if l.startswith("- ")]
            path = "fallback"
        res.append(dict(rules=ok, path=path, raw=o))
    return res


REL_PROMPT = (
    "Two skills will be loaded together for the same task. Skill A is `{an}` and skill B is `{bn}`.\n\n"
    "Rules of skill A:\n{ra}\n\nRules of skill B:\n{rb}\n\n"
    "Compare every rule of A with every rule of B and report only the pairs that interact:\n"
    '- "duplicate": both rules ask for the same thing.\n'
    '- "contradictory": no single output can satisfy both rules.\n'
    '- "entangled": both rules can be satisfied together, but only if the output is arranged in a specific way '
    "(an ordering, a placement, or fitting inside a limit). Following one rule in the obvious way would break the other.\n"
    "Do not list pairs of rules that are simply independent.\n"
    'Return a JSON array of objects like {{"a": "A3", "b": "B1", "relation": "contradictory", "reason": "..."}} and nothing else.')


def detect_relations(lm, pairs):
    """pairs: list of (job, rulesA, rulesB). One call per job."""
    msgs = []
    for job, ra, rb in pairs:
        msgs.append([{"role": "system", "content": "You analyze instruction files for AI assistants."},
                     {"role": "user", "content": REL_PROMPT.format(
                         an=job.skills["A"].name, bn=job.skills["B"].name,
                         ra="\n".join(f"A{i + 1}. {r}" for i, r in enumerate(ra)),
                         rb="\n".join(f"B{i + 1}. {r}" for i, r in enumerate(rb)))}])
    outs = lm.chat(msgs, max_new=900, desc="relate")
    res = []
    for (job, ra, rb), o in zip(pairs, outs):
        rel = []
        for x in parse_json_array(o) or []:
            try:
                a, b = int(str(x["a"]).strip().lstrip("Aa")) - 1, int(str(x["b"]).strip().lstrip("Bb")) - 1
                r = str(x["relation"]).strip().lower()
                if 0 <= a < len(ra) and 0 <= b < len(rb) and r in ("duplicate", "contradictory", "entangled"):
                    rel.append(dict(a=a, b=b, relation=r, reason=str(x.get("reason", ""))[:300]))
            except Exception:
                continue
        res.append(dict(relations=rel, raw=o))
    return res


def combine_rules(lm, items):
    """items: list of (rule_p, name_p, rule_q, name_q). Returns one combined rule per item."""
    msgs = [[{"role": "system", "content": "You write precise instructions for AI assistants."},
             {"role": "user", "content": f"Rule from skill `{np_}`: {rp}\nRule from skill `{nq}`: {rq}\n\n"
              "Both rules must hold for the same output. They can both be satisfied if the output is arranged carefully. "
              "Write one combined rule, at most two sentences, that tells the writer exactly how to satisfy both at once. "
              "Keep every literal marker, label and format from both rules. Return only the combined rule."}]
            for rp, np_, rq, nq in items]
    return [ws(norm(o)) for o in lm.chat(msgs, max_new=160, desc="combine")]


def assemble(job, P, kept_p, kept_q, reconciled, example=None):
    Q = "B" if P == "A" else "A"
    sp, sq = job.skills[P], job.skills[Q]
    t = ["---", f"name: {sp.name}+{sq.name}",
         f"description: Merged skill that replaces `{sp.name}` and `{sq.name}`. Use for any {job.artifact}.", "---", "",
         f"# Merged skill: {sp.name} + {sq.name}", "",
         f"This skill replaces `{sp.name}` and `{sq.name}`. It keeps every rule of both skills that can hold at the "
         "same time. Follow every rule below.", "",
         f"## Rules kept unchanged from `{sp.name}`", ""] + [f"- {r}" for r in kept_p]
    t += ["", f"## Rules kept unchanged from `{sq.name}`", ""] + [f"- {r}" for r in kept_q]
    if reconciled:
        t += ["", "## Reconciled rules (each one satisfies a rule of both skills at once)", ""] + [f"- {r}" for r in reconciled]
    if example:
        t += ["", "## Example", "", f"Request: {job.example_request}", "", "Output:", ""]
        t += [example] if "```" in example else ["```", example, "```"]
    return "\n".join(t)


def write_examples(lm, items):
    """items: list of (job, meta_text_without_example). The model writes one example output per meta-skill."""
    specs = [dict(job=j.id, request=j.example_request, system=sys_prompt([t])) for j, t in items]
    recs = run(lm, specs, desc="example")
    out = []
    for (j, _), r in zip(items, recs):
        o = r["output"].strip()
        out.append(o if j.id == "python" else norm(o))
    return out


def save_meta(variant, job, P, text, report):
    d = f"{ROOT}/meta/{variant}"
    os.makedirs(d, exist_ok=True)
    open(f"{d}/{job.id}_{P}.md", "w").write(text + "\n")
    json.dump(report, open(f"{d}/{job.id}_{P}.json", "w"), indent=1)


def load_meta(variant, job, P):
    p = f"{ROOT}/meta/{variant}/{job.id}_{P}.md"
    return open(p).read().strip() if os.path.exists(p) else None


def stage_compile(lm, args):
    tag = lm.tag
    jobs = args.jobs
    # ---- baseline: unstructured merge by the same model
    msgs, units = [], []
    for job in jobs:
        for P in "AB":
            Q = "B" if P == "A" else "A"
            msgs.append([{"role": "system", "content": "You write instruction files for AI assistants."},
                         {"role": "user", "content":
                          "Two agent skills will be installed together. Merge them into ONE skill file that replaces both. "
                          "Keep every rule of both skills. Where two rules cannot both hold, the rule from "
                          f"`{job.skills[P].name}` wins. Write a complete SKILL.md with frontmatter, a rules section and one example. "
                          "Return only the merged skill file.\n\n"
                          f"<skill>\n{skill_text(job, P)}\n</skill>\n\n<skill>\n{skill_text(job, Q)}\n</skill>"}])
            units.append((job, P))
    for (job, P), o in zip(units, lm.chat(msgs, max_new=1100, desc="freemerge")):
        save_meta(f"freemerge_{tag}", job, P, norm(o), dict(method="freemerge", compiler=lm.mid))

    # ---- structured compile: extract -> relate -> resolve -> assemble
    ext = extract_rules(lm, [skill_text(j, L) for j in jobs for L in "AB"])
    ext = {(j.id, L): e for (j, L), e in zip([(j, L) for j in jobs for L in "AB"], ext)}
    rel = detect_relations(lm, [(j, ext[(j.id, "A")]["rules"], ext[(j.id, "B")]["rules"]) for j in jobs])
    rel = {j.id: r for j, r in zip(jobs, rel)}

    plans = []  # one per (job, P, mode)
    for job in jobs:
        for mode in ("llm", "oracle"):
            if mode == "llm":
                rules = {L: ext[(job.id, L)]["rules"] for L in "AB"}
                rels = rel[job.id]["relations"]
            else:  # ground-truth rules and relations: isolates detection errors
                rules = {L: [r.text for r in job.skills[L].reqs] for L in "AB"}
                keys = [r.key for r in job.skills["A"].reqs]
                rels = [dict(a=keys.index(k), b=[r.key for r in job.skills["B"].reqs].index(k),
                             relation={"con": "contradictory", "sh": "duplicate", "ent": "entangled"}[k])
                        for k in ("con", "sh", "ent")]
            for P in "AB":
                Q = "B" if P == "A" else "A"
                pi, qi = ("a", "b") if P == "A" else ("b", "a")
                drop_q, ent_pairs, used_p, used_q = set(), [], set(), set()
                for r in rels:  # precedence and duplicates first: the non-primary copy is dropped
                    if r["relation"] in ("contradictory", "duplicate"):
                        drop_q.add(r[qi])
                for r in rels:
                    if r["relation"] == "entangled" and r[qi] not in drop_q and r[pi] not in used_p and r[qi] not in used_q:
                        ent_pairs.append((r[pi], r[qi]))
                        used_p.add(r[pi])
                        used_q.add(r[qi])
                plans.append(dict(job=job, P=P, Q=Q, mode=mode, rules=rules, rels=rels, drop_q=sorted(drop_q), ent=ent_pairs))
    items = []
    for p in plans:
        for a, b in p["ent"]:
            items.append((p["rules"][p["P"]][a], p["job"].skills[p["P"]].name, p["rules"][p["Q"]][b], p["job"].skills[p["Q"]].name))
    combined = combine_rules(lm, items) if items else []
    ci = 0
    for p in plans:
        rec = []
        for _ in p["ent"]:
            rec.append(combined[ci])
            ci += 1
        ep, eq = {a for a, _ in p["ent"]}, {b for _, b in p["ent"]}
        p["kept_p"] = [r for i, r in enumerate(p["rules"][p["P"]]) if i not in ep]
        p["kept_q"] = [r for i, r in enumerate(p["rules"][p["Q"]]) if i not in eq and i not in p["drop_q"]]
        p["reconciled"] = rec
        p["noex"] = assemble(p["job"], p["P"], p["kept_p"], p["kept_q"], rec)
    exs = write_examples(lm, [(p["job"], p["noex"]) for p in plans])
    for p, ex in zip(plans, exs):
        job, P = p["job"], p["P"]
        rep = dict(method="structured", mode=p["mode"], compiler=lm.mid, primary=P,
                   rules={L: p["rules"][L] for L in "AB"}, relations=p["rels"], dropped_from_secondary=p["drop_q"],
                   entangled_pairs=p["ent"], reconciled=p["reconciled"],
                   extract_path={L: ext[(job.id, L)]["path"] for L in "AB"} if p["mode"] == "llm" else None)
        suffix = "" if p["mode"] == "llm" else "oracle_"
        save_meta(f"truce_{suffix}noex_{tag}", job, P, p["noex"], rep)
        save_meta(f"truce_{suffix}{tag}", job, P, assemble(job, P, p["kept_p"], p["kept_q"], p["reconciled"], ex), rep)
    json.dump({j.id: dict(extract={L: ext[(j.id, L)] for L in "AB"}, relate=rel[j.id]) for j in jobs},
              open(f"{ROOT}/runs/{tag}/compile_trace.json", "w"), indent=1)
    log("compile done")


# ----------------------------------------------------------------------------- stage: curriculum
def jaccard(a, b):
    a, b = set(re.findall(r"\w+", a.lower())), set(re.findall(r"\w+", b.lower()))
    return len(a & b) / max(1, len(a | b))


def stage_curriculum(lm, args):
    jobs, n, keep = args.jobs, args.n_cand, args.n_keep
    cands = {j.id: [] for j in jobs}
    for attempt in range(3):
        need = [j for j in jobs if len(cands[j.id]) < n]
        if not need:
            break
        msgs = [[{"role": "system", "content": "You write realistic work requests used to test an AI assistant."},
                 {"role": "user", "content":
                  f"Two skills are installed for writing a {j.artifact}.\n\n<skill>\n{skill_text(j, 'A')}\n</skill>\n\n"
                  f"<skill>\n{skill_text(j, 'B')}\n</skill>\n\n"
                  f"Write {n} new and varied requests that a user could send and to which BOTH skills apply. "
                  f"Each request must be self-contained and must mention {j.facts_hint}. "
                  f"Follow the style of this example request but change the content: \"{j.example_request}\"\n"
                  "Prefer requests for which following both skills at once is difficult. "
                  "Do not mention the skills or their rules in a request. "
                  f"Return a JSON array of {n} strings and nothing else."}] for j in need]
        outs = lm.chat(msgs, max_new=1500, temp=0.8, seed=11 + attempt, desc="propose")
        for j, o in zip(need, outs):
            for x in parse_json_array(o) or []:
                if isinstance(x, str) and 40 <= len(x) <= 700:
                    x = ws(x)
                    if all(jaccard(x, t) < 0.8 for t in list(j.tasks) + [j.example_request] + cands[j.id]):
                        cands[j.id].append(x)
    for j in jobs:
        cands[j.id] = cands[j.id][:n]
        log(f"  {j.id}: {len(cands[j.id])} candidate requests")
    # score: requirement-level instability across load orders and samples (inference only)
    specs = []
    for j in jobs:
        A, B = skill_text(j, "A"), skill_text(j, "B")
        for ci, req in enumerate(cands[j.id]):
            for o, sk in (("AB", [A, B]), ("BA", [B, A])):
                for s in (1, 2):
                    specs.append(dict(job=j.id, cand=ci, request=req, order=o, sample=s, system=sys_prompt(sk)))
    recs = []
    for s in (1, 2):
        sub = [x for x in specs if x["sample"] == s]
        recs += run(lm, sub, temp=0.7, seed=s, desc=f"curr-score s{s}")
    out = {}
    for j in jobs:
        info = []
        for ci, req in enumerate(cands[j.id]):
            rs = [r["scores"] for r in recs if r["job"] == j.id and r["cand"] == ci]
            keys = list(rs[0].keys())
            p = {k: sum(r[k] for r in rs) / len(rs) for k in keys}
            U = sum(1 - 2 * abs(p[k] - 0.5) for k in keys) / len(keys)
            nc = [k for k in keys if not k.endswith(".con")]
            clash = 1 - sum(p[k] for k in nc) / len(nc)
            info.append(dict(request=req, U=U, clash=clash, S=U + 0.5 * clash))
        chosen, pool = [], list(range(len(info)))
        while pool and len(chosen) < keep:  # greedy selection with a repetition penalty
            best = max(pool, key=lambda i: info[i]["S"] - 0.5 * max([jaccard(info[i]["request"], info[c]["request"]) for c in chosen] or [0]))
            chosen.append(best)
            pool.remove(best)
        out[j.id] = dict(candidates=info, frontier=[info[i]["request"] for i in chosen],
                         random=[x["request"] for x in info[:keep]])
    json.dump(out, open(f"{ROOT}/runs/{lm.tag}/curriculum.json", "w"), indent=1)
    log("curriculum done")


# ----------------------------------------------------------------------------- stage: refine (GEPA-style)
REFLECT = (
    "The skill file below merges two skills. An assistant followed it on some requests but broke rules that must hold.\n\n"
    "<skill>\n{skill}\n</skill>\n\n{feedback}\n\n"
    "Revise the skill file so that an assistant following it satisfies every rule, including the broken ones.\n"
    "- Keep all existing rules. If one of them makes a broken rule hard to satisfy, state precisely how to satisfy both.\n"
    "- If a broken rule is missing from the file, add it.\n"
    "- Fix or replace the example if it breaks a rule. The example must follow every rule.\n"
    "- Do not add requirements that are neither in the file nor in the broken rules.\n"
    "Return only the complete revised skill file.")


def stage_refine(lm, args):
    cur = json.load(open(f"{ROOT}/runs/{lm.tag}/curriculum.json"))
    rng = random.Random(args.seed)
    units = []
    for job in args.jobs:
        for P in "AB":
            seed_text = load_meta(args.src, job, P)
            tasks = cur[job.id][args.curriculum]
            if seed_text is None or len(tasks) < 6:
                log(f"skip {job.id} {P}: missing seed or too few curriculum requests ({len(tasks)})")
                continue
            fb, par = tasks[0::2], tasks[1::2]
            units.append(dict(job=job, P=P, cands=[seed_text], fb=fb, par=par, hist=[], rollouts=0))

    def rollout(pairs, desc):  # pairs: (unit, text, request) -> fraction of target set satisfied, scores
        recs = run(lm, [dict(job=u["job"].id, request=req, system=sys_prompt([t])) for u, t, req in pairs], desc=desc)
        for u, _, _ in pairs:
            u["rollouts"] += 1
        return [(frac_target(u["job"], u["P"], r["scores"]), r) for (u, _, _), r in zip(pairs, recs)]

    res = rollout([(u, u["cands"][0], req) for u in units for req in u["par"]], "refine-seed-pareto")
    k = 0
    for u in units:
        u["par_scores"] = [[x[0] for x in res[k:k + len(u["par"])]]]
        k += len(u["par"])

    for it in range(args.iters):
        sel = []
        for u in units:  # Pareto-based parent selection
            nt = len(u["par"])
            best = [max(c[t] for c in u["par_scores"]) for t in range(nt)]
            w = [sum(c[t] >= best[t] - 1e-9 for t in range(nt)) for c in u["par_scores"]]
            parent = rng.choices(range(len(u["cands"])), weights=w)[0]
            mb = rng.sample(u["fb"], min(args.minibatch, len(u["fb"])))
            sel.append((u, parent, mb))
        before = rollout([(u, u["cands"][p], req) for u, p, mb in sel for req in mb], f"refine-it{it}-parent")
        k, msgs, act = 0, [], []
        for u, p, mb in sel:
            rs = before[k:k + len(mb)]
            k += len(mb)
            job, P = u["job"], u["P"]
            blocks = []
            for req, (f, r) in zip(mb, rs):
                broken = [(l, kk) for l, kk, _ in target_set(job, P) if not r["scores"][f"{l}.{kk}"]]
                if broken:
                    blocks.append(f"Request: {req}\nAssistant output:\n{r['output'][:1200]}\nRules that this output broke:\n" +
                                  "\n".join(f"- \"{job.skills[l].req(kk).text}\" (from `{job.skills[l].name}`)" for l, kk in broken))
            if not blocks:
                u["hist"].append(dict(it=it, parent=p, note="minibatch perfect"))
                continue
            msgs.append([{"role": "system", "content": "You improve instruction files for AI assistants."},
                         {"role": "user", "content": REFLECT.format(skill=u["cands"][p], feedback="\n\n".join(blocks))}])
            act.append((u, p, mb, sum(f for f, _ in rs)))
        if not msgs:
            continue
        kids = [norm(o) for o in lm.chat(msgs, max_new=1200, temp=0.7, seed=1000 + it, desc=f"reflect-it{it}")]
        after = rollout([(u, kid, req) for (u, p, mb, _), kid in zip(act, kids) for req in mb], f"refine-it{it}-child")
        k, acc = 0, []
        for (u, p, mb, sb), kid in zip(act, kids):
            sa = sum(f for f, _ in after[k:k + len(mb)])
            k += len(mb)
            ok = sa > sb + 1e-9 and len(kid) > 200
            u["hist"].append(dict(it=it, parent=p, before=sb, after=sa, accepted=ok))
            if ok:
                acc.append((u, kid))
        if acc:
            res = rollout([(u, kid, req) for u, kid in acc for req in u["par"]], f"refine-it{it}-pareto")
            k = 0
            for u, kid in acc:
                u["cands"].append(kid)
                u["par_scores"].append([x[0] for x in res[k:k + len(u["par"])]])
                k += len(u["par"])
        log(f"refine iter {it}: {len(act)} reflections, {len(acc)} accepted")

    for u in units:
        means = [sum(c) / len(c) for c in u["par_scores"]]
        bi = max(range(len(means)), key=lambda i: (means[i], -i))
        save_meta(args.dst, u["job"], u["P"], u["cands"][bi],
                  dict(method="refined", src=args.src, curriculum=args.curriculum, executor=lm.mid, chosen=bi,
                       n_candidates=len(u["cands"]), pareto_means=means, history=u["hist"], rollouts=u["rollouts"]))
    log(f"refine done: {sum(len(u['cands']) > 1 for u in units)}/{len(units)} units improved on the minibatch at least once")


# ----------------------------------------------------------------------------- stage: treat
def stage_treat(lm, args):
    specs = []
    for job in args.jobs:
        for P in "AB":
            Q = "B" if P == "A" else "A"
            tp, tq = skill_text(job, P), skill_text(job, Q)
            conds = {"prec_PQ": sys_prompt([tp, tq], job.skills[P].name), "prec_QP": sys_prompt([tq, tp], job.skills[P].name)}
            if not args.no_builtin:
                strong = (f"\n\nThe loaded skills are complementary, not alternatives. Apply every rule of BOTH skills in the same "
                          f"output. Only where two rules cannot both hold does the rule from `{job.skills[P].name}` win.")
                conds["strong_PQ"] = sys_prompt([tp, tq]) + strong
                conds["strong_QP"] = sys_prompt([tq, tp]) + strong
                conds["union_noex"] = sys_prompt([union_skill(job, P)])
                conds["union_prec"] = sys_prompt([union_skill(job, P, True)])
            for v in args.variants:
                m = load_meta(v, job, P)
                if m is not None:
                    conds[v] = sys_prompt([m])
            for ti, req in enumerate(job.tasks[:args.limit_tasks]):
                for c, s in conds.items():
                    specs.append(dict(job=job.id, task=ti, request=req, cond=c, primary=P, system=s))
                if not args.no_builtin:
                    specs.append(dict(job=job.id, task=ti, request=req, cond="checklist_PQ", primary=P, post="final", extra_tokens=450,
                                      system=sys_prompt([tp, tq], job.skills[P].name),
                                      user=f"{req}\n\nFirst write a short numbered checklist of every rule from the loaded skills that "
                                           "applies to this request and how you will satisfy it. Then write a line containing only "
                                           f"FINAL: and after it the {job.artifact} only."))
    recs = run(lm, specs, None, desc="treat")
    if not args.no_builtin:  # two-pass treatment: write with the primary skill, then revise with the secondary skill
        drafts = run(lm, [dict(job=j.id, task=ti, request=req, primary=P, system=sys_prompt([skill_text(j, P)]))
                          for j in args.jobs for P in "AB" for ti, req in enumerate(j.tasks[:args.limit_tasks])], desc="seq-draft")
        rev = []
        for d in drafts:
            j = JOBMAP[d["job"]]
            Q = "B" if d["primary"] == "A" else "A"
            rev.append(dict(job=d["job"], task=d["task"], request=d["request"], cond="seqrev", primary=d["primary"],
                            system=sys_prompt([skill_text(j, Q)]),
                            user=f"{d['request']}\n\nA colleague already wrote this draft:\n\n{d['output']}\n\n"
                                 "Revise the draft so that it also satisfies the rules of the loaded skill. Keep everything else in the "
                                 "draft unchanged. If a rule cannot hold without undoing something the draft does on purpose, keep the "
                                 f"draft's version. Reply with the revised {j.artifact} only, with no commentary before or after it."))
        recs += run(lm, rev, None, desc="seq-revise")
    path = f"{ROOT}/runs/{lm.tag}/treat{args.suffix}.jsonl"
    with open(path, "w") as f:
        for r in recs:
            f.write(json.dumps(r) + "\n")
    log(f"wrote {len(recs)} records to {path}")


# ----------------------------------------------------------------------------- stage: variance (is the winner stable?)
def stage_variance(lm, args):
    """Both skills loaded, sampled at temperature 0.7 with three seeds: does the same request get the same winner?"""
    specs = []
    for job in args.jobs:
        A, B = skill_text(job, "A"), skill_text(job, "B")
        for ti, req in enumerate(job.tasks[:args.limit_tasks]):
            for c, sk in (("AB", [A, B]), ("BA", [B, A])):
                specs.append(dict(job=job.id, task=ti, request=req, cond=c, system=sys_prompt(sk)))
    recs = []
    for seed in (1, 2, 3):
        rs = run(lm, specs, None, temp=0.7, seed=seed, desc=f"variance-s{seed}")
        for r in rs:
            r["seed"] = seed
        recs += rs
    path = f"{ROOT}/runs/{lm.tag}/variance.jsonl"
    with open(path, "w") as f:
        for r in recs:
            f.write(json.dumps(r) + "\n")
    log(f"wrote {len(recs)} records to {path}")


# ----------------------------------------------------------------------------- stage: ablate (what triggers the takeover?)
def stage_ablate(lm, args):
    """Both skills loaded, with parts removed: examples, then the contradictory rule, then also the entangled rule."""
    variants = {"noex": (), "nocon": ("con",), "compat": ("con", "ent")}
    specs = []
    for job in args.jobs:
        for v, drop in variants.items():
            A, B = skill_text(job, "A", False, drop), skill_text(job, "B", False, drop)
            for ti, req in enumerate(job.tasks[:args.limit_tasks]):
                for c, sk in ((f"{v}_A", [A]), (f"{v}_B", [B]), (f"{v}_AB", [A, B]), (f"{v}_BA", [B, A])):
                    specs.append(dict(job=job.id, task=ti, request=req, cond=c, system=sys_prompt(sk)))
    run(lm, specs, f"{ROOT}/runs/{lm.tag}/ablate.jsonl", desc="ablate")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="qwen4b")
    ap.add_argument("--stage", required=True)
    ap.add_argument("--jobs", default="")
    ap.add_argument("--limit-tasks", type=int, default=99)
    ap.add_argument("--variants", default="")
    ap.add_argument("--suffix", default="")
    ap.add_argument("--src", default="")
    ap.add_argument("--dst", default="")
    ap.add_argument("--curriculum", default="frontier")
    ap.add_argument("--iters", type=int, default=6)
    ap.add_argument("--minibatch", type=int, default=3)
    ap.add_argument("--n-cand", type=int, default=16)
    ap.add_argument("--n-keep", type=int, default=12)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--tok-budget", type=int, default=22000)
    ap.add_argument("--hf-model", default="", help="any Hugging Face chat model id; --model is then only a tag for the runs folder")
    ap.add_argument("--no-builtin", action="store_true", help="treat stage: skip the prompt-level and code-only treatments")
    ap.add_argument("--api-model", default="", help="model name at an OpenAI-compatible endpoint; --model is then only a tag for the runs folder")
    ap.add_argument("--api-base", default="https://api.openai.com/v1")
    ap.add_argument("--api-key-env", default="OPENAI_API_KEY")
    ap.add_argument("--api-workers", type=int, default=8)
    args = ap.parse_args()
    args.jobs = [JOBMAP[x] for x in args.jobs.split(",") if x] or JOBS
    args.variants = [v for v in args.variants.split(",") if v]
    if args.stage == "export":
        return stage_export(args)
    if args.api_model:
        lm = APILM(args.model, args.api_model, args.api_base, args.api_key_env, args.api_workers)
    else:
        if args.hf_model:
            MODELS[args.model] = args.hf_model
        lm = LM(args.model, args.tok_budget)
    for st in args.stage.split(","):
        log(f"=== stage {st} ({len(args.jobs)} jobs)")
        {"diag": stage_diag, "ablate": stage_ablate, "variance": stage_variance, "compile": stage_compile, "curriculum": stage_curriculum,
         "refine": stage_refine, "treat": stage_treat}[st](lm, args)
        log(f"=== stage {st} finished; generated {lm.n_gen}, cache hits {lm.n_hit}")


if __name__ == "__main__":
    main()

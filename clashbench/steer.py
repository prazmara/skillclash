#!/usr/bin/env python
"""Activation probe and activation steering for the takeover. Weights stay frozen; inference only.

Usage: python steer.py --model qwen4b --stage acts,probe,sweep,test,report

Stages:
  acts    one forward pass per prompt; saves residual-stream vectors to runs/<tag>/steer_acts.npz
  probe   can a linear readout at the last prompt token (before any output) predict which co-loaded skill wins?
  sweep   steering on the development requests (tasks 0-3) over layers and strengths
  test    the settings selected on the development requests, run on the held-out requests (tasks 4-7)
  report  tables with 95% bootstrap intervals over jobs; writes runs/<tag>/steer_summary.json

Steering adds one fixed vector to the output of one transformer block at every position while the model reads the
prompt and writes. Three directions, all scaled to c times the mean residual norm of that block:
  skill   for this job: mean activation while writing with the target skill alone minus the same for the other skill
          (computed on requests that are not the ones being evaluated)
  order   one direction for all jobs: co-loaded prompts where the first-listed skill won minus prompts where the
          second-listed skill won, at the last prompt token, from the other 15 jobs only
  rand    a random direction of the same length (control)
The target of the push is the skill that lost at baseline, so this is an analysis tool, not a deployable treatment.
Benchmark, prompts and checkers are imported from harness.py and spec.py unchanged.
"""
import argparse
import collections
import json
import os
import sys
import zlib

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from harness import JOBS, JOBMAP, MODELS, frac_target, log, skill_text, sys_prompt, user_prompt  # noqa: E402
from spec import score  # noqa: E402

DEV, TEST = (0, 1, 2, 3), (4, 5, 6, 7)
RNG = np.random.default_rng(0)


def load(p):
    return [json.loads(l) for l in open(p)] if os.path.exists(p) else []


def ex(s, L):
    return sum(s[f"{L}.e{i}"] for i in (1, 2, 3)) / 3


def winner(s):
    a, b = ex(s, "A"), ex(s, "B")
    return "A" if a >= 0.99 and b <= 0.01 else "B" if b >= 0.99 and a <= 0.01 else "mixed"


def msgs(job, skills, req):
    return [{"role": "system", "content": sys_prompt(skills)}, {"role": "user", "content": user_prompt(job, req)}]


def co_skills(job, cond):
    return [skill_text(job, cond[0]), skill_text(job, cond[1])]


def unit(v):
    return v / (np.linalg.norm(v) + 1e-8)


def boot(v):
    v = np.array([x for x in v if x is not None], float)
    if len(v) == 0:
        return dict(mean=None, lo=None, hi=None, n=0)
    m = v[RNG.integers(0, len(v), (10000, len(v)))].mean(1)
    return dict(mean=float(v.mean()), lo=float(np.percentile(m, 2.5)), hi=float(np.percentile(m, 97.5)), n=int(len(v)))


def fmt(b, scale=100):
    return "n/a" if b["mean"] is None else f"{scale * b['mean']:5.1f} [{scale * b['lo']:5.1f}, {scale * b['hi']:5.1f}]"


# ----------------------------------------------------------------------------- model
class M:
    def __init__(self, tag):
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer
        self.torch, self.mid = torch, MODELS[tag]
        self.tok = AutoTokenizer.from_pretrained(self.mid)
        self.tok.padding_side = "left"
        if self.tok.pad_token is None:
            v = self.tok.get_vocab()
            self.tok.pad_token = "<|finetune_right_pad_id|>" if "<|finetune_right_pad_id|>" in v else self.tok.eos_token
        self.model = AutoModelForCausalLM.from_pretrained(self.mid, torch_dtype=torch.float16).cuda().eval()
        self.layers = self.model.model.layers
        self.cur = None  # steering tensor [batch, 1, dim] for the hooked block, or None
        log(f"loaded {self.mid}; {len(self.layers)} blocks; gpu mem {torch.cuda.memory_allocated() / 1e9:.1f} GB")

    def render(self, m):
        return self.tok.apply_chat_template(m, tokenize=False, add_generation_prompt=True)

    def ids(self, text):
        return self.tok(text, add_special_tokens=False).input_ids

    def hidden(self, ids):
        """All block outputs for one sequence: array [blocks + 1, tokens, dim] on the GPU."""
        torch = self.torch
        with torch.no_grad():
            out = self.model(input_ids=torch.tensor([ids], device="cuda"), output_hidden_states=True)
        return torch.stack(out.hidden_states)[:, 0].float()

    def _hook(self, mod, inp, out):
        if self.cur is None:
            return None
        if isinstance(out, tuple):
            return (out[0] + self.cur,) + tuple(out[1:])
        return out + self.cur

    def generate(self, items, layer=None, budget=14000, desc=""):
        """items: dicts with text, max_new and (when layer is given) vec. Greedy decoding, as in the main runs."""
        torch = self.torch
        outs = [None] * len(items)
        lens = [len(self.ids(x["text"])) for x in items]
        by = collections.defaultdict(list)
        for i, x in enumerate(items):
            by[x["max_new"]].append(i)
        h = self.layers[layer].register_forward_hook(self._hook) if layer is not None else None
        done = 0
        try:
            for mn, idxs in sorted(by.items()):
                idxs = sorted(idxs, key=lambda i: -lens[i])
                i = 0
                while i < len(idxs):
                    bs = max(1, min(32, budget // (lens[idxs[i]] + mn)))
                    idx = idxs[i:i + bs]
                    enc = self.tok([items[j]["text"] for j in idx], return_tensors="pt", padding=True, add_special_tokens=False).to("cuda")
                    if layer is not None:
                        self.cur = torch.tensor(np.stack([items[j]["vec"] for j in idx]), device="cuda", dtype=torch.float16)[:, None, :]
                    try:
                        with torch.no_grad():
                            g = self.model.generate(**enc, max_new_tokens=mn, pad_token_id=self.tok.pad_token_id,
                                                    do_sample=False, temperature=None, top_p=None, top_k=None)
                    except torch.cuda.OutOfMemoryError:
                        torch.cuda.empty_cache()
                        budget = max(3000, int(budget * 0.6))
                        log(f"OOM, token budget now {budget}")
                        continue
                    finally:
                        self.cur = None
                    for j, o in zip(idx, self.tok.batch_decode(g[:, enc.input_ids.shape[1]:], skip_special_tokens=True)):
                        outs[j] = o
                    i += len(idx)
                    done += len(idx)
            log(f"  {desc}: {done} generated")
        finally:
            if h is not None:
                h.remove()
        return outs


# ----------------------------------------------------------------------------- stage: acts
def stage_acts(m, tag):
    diag = {(r["job"], r["task"], r["cond"]): r for r in load(f"{ROOT}/runs/{tag}/diag.jsonl")}
    co_last, co_meta, al_last, al_gen, al_norm, al_meta = [], [], [], [], [], []
    for job in JOBS:
        ntok = {L: len(m.ids(skill_text(job, L))) for L in "AB"}
        for ti, req in enumerate(job.tasks):
            for cond in ("AB", "BA"):
                p = m.ids(m.render(msgs(job, co_skills(job, cond), req)))
                co_last.append(m.hidden(p)[:, -1].cpu().numpy().astype(np.float16))
                w = winner(diag[(job.id, ti, cond)]["scores"])
                co_meta.append(dict(job=job.id, task=ti, cond=cond, winner=w,
                                    first_wins=None if w == "mixed" else int(w == cond[0]),
                                    tok_first=ntok[cond[0]], tok_second=ntok[cond[1]], tok_request=len(m.ids(req)), tok_prompt=len(p)))
            for L in "AB":
                p = m.ids(m.render(msgs(job, [skill_text(job, L)], req)))
                o = m.ids(diag[(job.id, ti, L)]["output"])[:job.max_new_tokens]
                hs = m.hidden(p + o)
                span = hs[:, len(p) - 1:len(p) + max(len(o), 1) - 1]  # positions from which the output tokens are predicted
                al_last.append(hs[:, len(p) - 1].cpu().numpy().astype(np.float16))
                al_gen.append(span.mean(1).cpu().numpy().astype(np.float16))
                al_norm.append(span.norm(dim=-1).mean(1).cpu().numpy().astype(np.float32))
                al_meta.append(dict(job=job.id, task=ti, skill=L, tok_out=len(o)))
        log(f"  acts {job.id} done")
    np.savez(f"{ROOT}/runs/{tag}/steer_acts.npz", co_last=np.stack(co_last), al_last=np.stack(al_last), al_gen=np.stack(al_gen),
             al_norm=np.stack(al_norm), co_meta=json.dumps(co_meta), al_meta=json.dumps(al_meta))
    log(f"wrote steer_acts.npz: {len(co_meta)} co-loaded prompts, {len(al_meta)} single-skill runs")


def load_acts(tag):
    z = np.load(f"{ROOT}/runs/{tag}/steer_acts.npz")
    A = dict(co_last=z["co_last"].astype(np.float32), al_gen=z["al_gen"].astype(np.float32), al_norm=z["al_norm"],
             co_meta=json.loads(str(z["co_meta"])), al_meta=json.loads(str(z["al_meta"])))
    A["al_ix"] = {(r["job"], r["task"], r["skill"]): i for i, r in enumerate(A["al_meta"])}
    return A


# ----------------------------------------------------------------------------- stage: probe
def ridge_scores(Xtr, ytr, Xte, lam):
    """Ridge regression to +1 / -1 labels on standardized features (dual form); returns test scores, class 1 if > 0."""
    mu, sd = Xtr.mean(0), Xtr.std(0) + 1e-6
    Xtr, Xte = (Xtr - mu) / sd, (Xte - mu) / sd
    t = 2.0 * ytr - 1.0
    a = np.linalg.solve(Xtr @ Xtr.T + lam * np.eye(len(Xtr)), t - t.mean())
    return Xte @ (Xtr.T @ a) + t.mean()


def auc(scores, y):
    y = np.asarray(y)
    if y.min() == y.max():
        return None
    r = np.argsort(np.argsort(scores)) + 1.0
    n1, n0 = y.sum(), len(y) - y.sum()
    return float((r[y == 1].sum() - n1 * (n1 + 1) / 2) / (n1 * n0))


def stage_probe(tag):
    A = load_acts(tag)
    meta = A["co_meta"]
    keep = [i for i, r in enumerate(meta) if r["first_wins"] is not None]
    y = np.array([meta[i]["first_wins"] for i in keep], float)
    jobs = np.array([meta[i]["job"] for i in keep])
    tasks = np.array([meta[i]["task"] for i in keep])
    conds = np.array([meta[i]["cond"] for i in keep])
    text = np.array([[meta[i]["tok_first"], meta[i]["tok_second"], meta[i]["tok_first"] - meta[i]["tok_second"], meta[i]["tok_request"]]
                     for i in keep], float)
    nl = A["co_last"].shape[1]
    out = dict(model=tag, n_prompts=len(meta), n_labeled=len(keep), first_listed_wins=float(y.mean()), splits={})
    for split, groups in (("new_skill_pair", jobs), ("new_request", tasks)):
        folds = [(np.where(groups != g)[0], np.where(groups == g)[0]) for g in sorted(set(groups))]
        base = np.zeros(len(y))  # baseline prediction per row
        for tr, te in folds:
            if split == "new_skill_pair":   # nothing about a new pair is known: predict the more frequent position
                base[te] = float(y[tr].mean() >= 0.5)
            else:                           # same pair and load order seen on other requests: predict its usual winner
                for i in te:
                    same = [k for k in tr if jobs[k] == jobs[i] and conds[k] == conds[i]]
                    base[i] = float(np.mean(y[same]) >= 0.5) if same else float(y[tr].mean() >= 0.5)
        tx = np.zeros(len(y))
        for tr, te in folds:
            tx[te] = ridge_scores(text[tr], y[tr], text[te], 1.0)
        per_layer = []
        for hl in range(nl):
            X = A["co_last"][keep][:, hl]
            sc = np.zeros(len(y))
            for tr, te in folds:
                sc[te] = ridge_scores(X[tr], y[tr], X[te], float(X.shape[1]))
            per_layer.append(dict(layer=hl, acc=float(((sc > 0) == y).mean()), auc=auc(sc, y), _pred=(sc > 0).astype(float)))
        best = max(per_layer, key=lambda d: d["acc"])
        mid = per_layer[nl // 2]
        # nested: the block is chosen inside each training fold (same kind of split again), so this estimate is not optimistic
        Xall = A["co_last"][keep]
        nested, picked = np.zeros(len(y)), []
        for tr, te in folds:
            g_in = groups[tr]
            inner = [(np.where(g_in != g)[0], np.where(g_in == g)[0]) for g in sorted(set(g_in))]
            accs = []
            for hl in range(nl):
                Xl, sc = np.ascontiguousarray(Xall[tr, hl]), np.zeros(len(tr))
                for a_, b_ in inner:
                    sc[b_] = ridge_scores(Xl[a_], y[tr][a_], Xl[b_], float(Xall.shape[2]))
                accs.append(float(((sc > 0) == y[tr]).mean()))
            hl = int(np.argmax(accs))
            picked.append(hl)
            nested[te] = ridge_scores(Xall[tr, hl], y[tr], Xall[te, hl], float(Xall.shape[2])) > 0

        def by_job(pred):
            return {j: float((pred[jobs == j] == y[jobs == j]).mean()) for j in sorted(set(jobs))}
        bj = by_job(base)
        res = dict(n_folds=len(folds), baseline_acc=float((base == y).mean()), text_features_acc=float(((tx > 0) == y).mean()),
                   text_features_auc=auc(tx, y), per_layer=[{k: v for k, v in d.items() if k != "_pred"} for d in per_layer])
        for name, d in (("best_layer", best), ("middle_layer", mid)):
            pj = by_job(d["_pred"])
            res[name] = dict(layer=d["layer"], acc=d["acc"], auc=d["auc"], acc_minus_baseline=boot([pj[j] - bj[j] for j in pj]))
        pj = by_job(nested)
        res["nested"] = dict(acc=float((nested == y).mean()), layers_picked=picked, acc_minus_baseline=boot([pj[j] - bj[j] for j in pj]))
        out["splits"][split] = res
        print(f"\n=== PROBE, held out: {split} ({len(keep)} prompts with a winner; first-listed skill wins {100 * y.mean():.1f}%)")
        print(f"  baseline accuracy {100 * res['baseline_acc']:.1f}   text-feature accuracy {100 * res['text_features_acc']:.1f}")
        for name in ("middle_layer", "best_layer"):
            r = res[name]
            print(f"  {name:13s} (block output {r['layer']:2d}): accuracy {100 * r['acc']:.1f}, AUC {r['auc']:.2f}, "
                  f"accuracy minus baseline per job {fmt(r['acc_minus_baseline'])}")
        print(f"  block chosen inside each training fold: accuracy {100 * res['nested']['acc']:.1f}, accuracy minus baseline per job "
              f"{fmt(res['nested']['acc_minus_baseline'])}; blocks picked {sorted(set(picked))}")
    json.dump(out, open(f"{ROOT}/runs/{tag}/steer_probe.json", "w"), indent=1)
    print(f"\nwrote runs/{tag}/steer_probe.json (the best layer is picked after the fact, so its accuracy is optimistic)")


# ----------------------------------------------------------------------------- stage: sweep / test
class Dirs:
    def __init__(self, A):
        self.A, self.cache = A, {}

    def scale(self, layer):
        return float(self.A["al_norm"][:, layer + 1].mean())

    def vec(self, kind, job, cond, target, layer, c, fit_tasks):
        A, hl = self.A, layer + 1
        if kind == "skill":
            key = (kind, job, target, layer, fit_tasks)
            if key not in self.cache:
                other = "B" if target == "A" else "A"
                self.cache[key] = unit(np.mean([A["al_gen"][A["al_ix"][(job, t, target)], hl] - A["al_gen"][A["al_ix"][(job, t, other)], hl]
                                                for t in fit_tasks], 0))
            d = self.cache[key]
        elif kind == "order":
            key = (kind, job, layer)
            if key not in self.cache:
                r1 = [i for i, r in enumerate(A["co_meta"]) if r["job"] != job and r["first_wins"] == 1]
                r0 = [i for i, r in enumerate(A["co_meta"]) if r["job"] != job and r["first_wins"] == 0]
                self.cache[key] = unit(A["co_last"][r1][:, hl].mean(0) - A["co_last"][r0][:, hl].mean(0))
            d = self.cache[key] * (1.0 if target == cond[0] else -1.0)
        else:
            d = unit(np.random.default_rng(zlib.crc32(f"{job}/{cond}/{layer}".encode())).standard_normal(A["co_last"].shape[2]))
        return (c * self.scale(layer) * d).astype(np.float32)


class Runs:
    """Generations keyed by (setting, job, task, cond); appended to runs/<tag>/steer_gen.jsonl so a restart resumes."""

    def __init__(self, tag):
        self.path = f"{ROOT}/runs/{tag}/steer_gen.jsonl"
        self.recs = {(r["setting"], r["job"], r["task"], r["cond"]): r for r in load(self.path)}
        self.fh = open(self.path, "a")

    def add(self, r):
        self.recs[(r["setting"], r["job"], r["task"], r["cond"])] = r
        self.fh.write(json.dumps(r) + "\n")
        self.fh.flush()

    def setting(self, name):
        return [r for k, r in self.recs.items() if k[0] == name]


def run_setting(m, runs, dirs, jobs, name, kind, layer, c, tasks, fit_tasks, budget):
    todo, items = [], []
    for job in jobs:
        for ti in tasks:
            for cond in ("AB", "BA"):
                if (name, job.id, ti, cond) in runs.recs:
                    continue
                tgt = None
                if kind != "base":
                    b = runs.recs[("base", job.id, ti, cond)]["scores"]
                    a_, b_ = ex(b, "A"), ex(b, "B")
                    tgt = "A" if a_ < b_ else "B" if b_ < a_ else cond[1]  # push toward the skill that lost; ties: the second-listed
                it = dict(text=m.render(msgs(job, co_skills(job, cond), job.tasks[ti])), max_new=job.max_new_tokens)
                if kind != "base":
                    it["vec"] = dirs.vec(kind, job.id, cond, tgt, layer, c, fit_tasks)
                items.append(it)
                todo.append(dict(setting=name, kind=kind, layer=layer, c=c, job=job.id, task=ti, cond=cond, target=tgt))
    if not items:
        return
    outs = m.generate(items, layer=None if kind == "base" else layer, budget=budget, desc=name)
    for r, o in zip(todo, outs):
        r["output"], r["scores"] = o, score(JOBMAP[r["job"]], o)
        runs.add(r)


def sname(kind, layer, c, split):
    return f"{kind}_L{layer}_c{c:g}_{split}"


def outcome(r, base):
    """Categories relative to the baseline loser T (the push target) and the baseline winner O."""
    T = r.get("target") or base.get("_target")
    O = "B" if T == "A" else "A"
    t, o = ex(r["scores"], T), ex(r["scores"], O)
    cat = "both" if t >= 0.99 and o >= 0.99 else "flip" if t >= 0.99 and o <= 0.01 else "stay" if o >= 0.99 and t <= 0.01 else \
        "neither" if t <= 0.01 and o <= 0.01 else "partial"
    j = JOBMAP[r["job"]]
    return dict(cat=cat, target=t, other=o, both_score=(t + o) / 2, mss=(frac_target(j, "A", r["scores"]) + frac_target(j, "B", r["scores"])) / 2,
                chars=len(r["output"]))


def summarize(recs, base_by, only_takeover=False):
    per = collections.defaultdict(lambda: collections.defaultdict(list))
    for r in recs:
        b = base_by[(r["job"], r["task"], r["cond"])]
        if only_takeover and winner(b["scores"]) == "mixed":
            continue
        o = outcome(r, b)
        for c in ("both", "flip", "stay", "partial", "neither"):
            per[c][r["job"]].append(float(o["cat"] == c))
        for k in ("target", "other", "both_score", "mss", "chars"):
            per[k][r["job"]].append(o[k])
    stats = {k: boot([float(np.mean(v)) for v in d.values()]) for k, d in per.items()}
    stats["n_outputs"] = sum(len(v) for v in per["chars"].values())
    return stats, {k: {j: float(np.mean(v)) for j, v in d.items()} for k, d in per.items()}


def base_index(runs):
    by = {}
    for r in runs.setting("base"):
        a_, b_ = ex(r["scores"], "A"), ex(r["scores"], "B")
        r["_target"] = "A" if a_ < b_ else "B" if b_ < a_ else r["cond"][1]
        by[(r["job"], r["task"], r["cond"])] = r
    return by


def pick(runs, base_by, kinds, layers, cs, crit):
    best = {}
    for kind in kinds:
        cands = []
        for layer in layers:
            for c in cs:
                recs = runs.setting(sname(kind, layer, c, "dev"))
                if recs:
                    s, _ = summarize(recs, base_by)
                    cands.append((s[crit]["mean"], -c, layer, c))
        if cands:
            _, _, layer, c = max(cands)
            best[kind] = (layer, c)
    return best


def stage_sweep(m, tag, args):
    runs, dirs = Runs(tag), Dirs(load_acts(tag))
    run_setting(m, runs, dirs, args.jobs, "base", "base", None, 0, DEV + TEST, None, args.budget)
    for kind in args.kinds:
        for layer in args.layers:
            for c in args.cs:
                run_setting(m, runs, dirs, args.jobs, sname(kind, layer, c, "dev"), kind, layer, c, DEV, TEST, args.budget)


def stage_test(m, tag, args):
    runs, dirs = Runs(tag), Dirs(load_acts(tag))
    base_by = base_index(runs)
    chosen = {}
    for crit in ("both_score", "flip"):
        for kind, (layer, c) in pick(runs, base_by, args.kinds, args.layers, args.cs, crit).items():
            chosen[f"{kind}/{crit}"] = (kind, layer, c)
    for key, (kind, layer, c) in list(chosen.items()):  # random-direction control at the same block and strength
        chosen[f"rand@{key}"] = ("rand", layer, c)
    for key, (kind, layer, c) in chosen.items():
        log(f"test setting {key}: block {layer}, c {c}")
        run_setting(m, runs, dirs, args.jobs, sname(kind, layer, c, "test"), kind, layer, c, TEST, DEV, args.budget)
    json.dump({k: dict(kind=v[0], layer=v[1], c=v[2]) for k, v in chosen.items()}, open(f"{ROOT}/runs/{tag}/steer_chosen.json", "w"), indent=1)


def stage_report(tag, args):
    runs = Runs(tag)
    base_by = base_index(runs)
    cols = ["both", "flip", "stay", "partial", "neither", "target", "other", "both_score", "mss"]
    out = dict(model=tag, dev={}, test={})

    def show(title, rows):
        print(f"\n=== {title}")
        print(f"{'setting':26s} {'n':>4s} " + " ".join(f"{c:>20s}" for c in cols) + f" {'chars':>6s}")
        for name, n, s in rows:
            if not n:
                continue
            print(f"{name:26s} {n:4d} " + " ".join(f"{fmt(s[c]):>20s}" for c in cols) + f" {s['chars']['mean']:6.0f}")

    for split, tasks in (("dev", DEV), ("test", TEST)):
        names = sorted({k[0] for k in runs.recs if k[0].endswith("_" + split)})
        b = [r for r in runs.setting("base") if r["task"] in tasks]
        for sub, only in (("all prompts", False), ("prompts with a takeover at baseline", True)):
            rows = []
            sb, pb = summarize(b, base_by, only)
            rows.append(("no steering", sb["n_outputs"], sb))
            for name in names:
                recs = runs.setting(name)
                s, pj = summarize(recs, base_by, only)
                s["delta_both_score"] = boot([pj["both_score"][j] - pb["both_score"][j] for j in pj["both_score"] if j in pb["both_score"]])
                s["delta_mss"] = boot([pj["mss"][j] - pb["mss"][j] for j in pj["mss"] if j in pb["mss"]])
                rows.append((name, s["n_outputs"], s))
                out[split].setdefault(sub, {})[name] = dict(s, n=s["n_outputs"], kind=recs[0]["kind"], layer=recs[0]["layer"], c=recs[0]["c"])
            out[split].setdefault(sub, {})["no steering"] = dict(sb, n=sb["n_outputs"])
            show(f"STEERING, {split} requests, {sub} (% of outputs or % of exclusive rules, mean over jobs [95% CI])", rows)
            if split == "test":
                for name, n, s in rows[1:]:
                    print(f"  {name:26s} change vs no steering: both_score {fmt(s['delta_both_score'])}  MSS {fmt(s['delta_mss'])}")
    if os.path.exists(f"{ROOT}/runs/{tag}/steer_chosen.json"):
        out["chosen"] = json.load(open(f"{ROOT}/runs/{tag}/steer_chosen.json"))
    json.dump(out, open(f"{ROOT}/runs/{tag}/steer_summary.json", "w"), indent=1)
    print(f"\nwrote runs/{tag}/steer_summary.json")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="qwen4b")
    ap.add_argument("--stage", required=True)
    ap.add_argument("--jobs", default="")
    ap.add_argument("--layers", default="")
    ap.add_argument("--cs", default="0.1,0.2,0.4,0.8")
    ap.add_argument("--kinds", default="skill,order")
    ap.add_argument("--budget", type=int, default=14000)
    args = ap.parse_args()
    args.jobs = [JOBMAP[x] for x in args.jobs.split(",") if x] or JOBS
    args.cs = [float(x) for x in args.cs.split(",")]
    args.kinds = args.kinds.split(",")
    stages = args.stage.split(",")
    m = M(args.model) if set(stages) & {"acts", "sweep", "test"} else None
    if m is not None and not args.layers:
        n = len(m.layers)
        args.layers = [n // 4, n // 2, 3 * n // 4]
    elif args.layers:
        args.layers = [int(x) for x in args.layers.split(",")]
    for st in stages:
        log(f"=== stage {st}")
        if st == "acts":
            stage_acts(m, args.model)
        elif st == "probe":
            stage_probe(args.model)
        elif st == "sweep":
            stage_sweep(m, args.model, args)
        elif st == "test":
            stage_test(m, args.model, args)
        elif st == "report":
            stage_report(args.model, args)
    log("done")


if __name__ == "__main__":
    main()

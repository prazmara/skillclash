#!/usr/bin/env python
"""Why does the step-by-step (structured) merge lose rules? Usage: python merge_errors.py

For every structured merged file (meta/truce_<compiler>/<job>_<P>.json) we recompute, from the relations the compiler
reported, what happened to each rule of the maximum satisfiable set: kept word for word, combined with a partner,
dropped, or lost at extraction. We compare that with what should have happened under the planted relations, and then
read how often the executor follows the rules of each kind (from runs/<executor>/treat*.jsonl).
Writes runs/merge_errors.json and prints tables. Reads only; changes no run data.
"""
import collections
import glob
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from spec import target_set  # noqa: E402
import jobs_core  # noqa: E402
import jobs_extra  # noqa: E402

JOBS = list(jobs_core.JOBS) + list(jobs_extra.JOBS)
COMPILERS = ["qwen4b", "qwen7b", "mistral7b", "llama8b", "phi4mini", "qwen235b", "gpt41", "agent"]
EXECUTORS = ["qwen4b", "qwen7b", "mistral7b", "llama8b", "phi4mini", "qwen235b", "gpt41"]


def ws(s):
    return " ".join(s.split())


def plan(job, P, rep):
    """Fate of every planted rule in the structured file for primary P, following stage_compile."""
    Q = "B" if P == "A" else "A"
    rules, rels = rep["rules"], rep["relations"]
    idx = {L: {ws(t): i for i, t in enumerate(rules[L])} for L in "AB"}
    pi, qi = ("a", "b") if P == "A" else ("b", "a")
    drop_q, used_p, used_q, ent = set(), set(), set(), []
    for r in rels:
        if r["relation"] in ("contradictory", "duplicate"):
            drop_q.add(r[qi])
    for r in rels:
        if r["relation"] == "entangled" and r[qi] not in drop_q and r[pi] not in used_p and r[qi] not in used_q:
            ent.append((r[pi], r[qi]))
            used_p.add(r[pi])
            used_q.add(r[qi])
    partner = {("P", a): b for a, b in ent}
    partner.update({("Q", b): a for a, b in ent})
    fate = {}
    for L, side in ((P, "P"), (Q, "Q")):
        for req in job.skills[L].reqs:
            i = idx[L].get(ws(req.text))
            if i is None:
                f = "not extracted"
            elif side == "Q" and i in drop_q:
                f = "dropped"
            elif (side, i) in partner:
                f = "combined"
            else:
                f = "kept"
            fate[(L, req.key)] = (f, i, partner.get((side, i)))
    # is the combined rule the planted entangled pair?
    pe, qe = fate[(P, "ent")], fate[(Q, "ent")]
    right_pair = pe[0] == "combined" and qe[0] == "combined" and pe[2] == qe[1]
    return fate, right_pair


def expected(side, rel):
    if rel == "ent":
        return "combined"
    if side == "Q" and rel in ("con", "sh"):
        return "dropped"
    return "kept"


def boot(v):
    v = np.array(v, float)
    m = v[np.random.default_rng(0).integers(0, len(v), (10000, len(v)))].mean(1)
    return [float(v.mean()), float(np.percentile(m, 2.5)), float(np.percentile(m, 97.5))]


out = {}
for comp in COMPILERS:
    files = {}
    for j in JOBS:
        for P in "AB":
            p = f"{ROOT}/meta/truce_{comp}/{j.id}_{P}.json"
            if os.path.exists(p):
                rep = json.load(open(p))
                if "relations" in rep and "rules" in rep:
                    files[(j.id, P)] = plan(j, P, rep)
    if not files:
        continue
    # ---- what the compiler did to the rules (counts over job x primary)
    cnt = collections.Counter()
    for (jid, P), (fate, right_pair) in files.items():
        j = next(x for x in JOBS if x.id == jid)
        Q = "B" if P == "A" else "A"
        for L, side in ((P, "P"), (Q, "Q")):
            for req in j.skills[L].reqs:
                f = fate[(L, req.key)][0]
                e = expected(side, req.rel)
                if side == "Q" and req.rel == "con":
                    cnt["losing contradictory rule: " + ("removed (right)" if f == "dropped" else f"left in the file ({f})")] += 1
                    continue
                if side == "Q" and req.rel == "sh":
                    continue
                kind = "entangled pair rule" if req.rel == "ent" else "rule that touches nothing" if req.rel == "excl" else "primary's contradictory or shared rule"
                if f == e and (req.rel != "ent" or right_pair):
                    cnt[kind + ": handled right"] += 1
                elif req.rel == "ent" and f == "combined":
                    cnt[kind + ": combined with the wrong partner"] += 1
                else:
                    cnt[kind + f": {f} (should be {e})"] += 1
    res = dict(files=len(files), counts=dict(sorted(cnt.items())), executors={})
    print(f"\n=== compiler {comp}: {len(files)} structured files (16 jobs x 2 primaries)")
    for k, v in sorted(cnt.items()):
        print(f"  {v:4d}  {k}")
    # ---- how the executor follows the rules, by what the compiler did
    for ex in EXECUTORS:
        recs = []
        for p in sorted(glob.glob(f"{ROOT}/runs/{ex}/treat*.jsonl")):
            if p.endswith("treat_v1.jsonl"):
                continue
            recs += [json.loads(l) for l in open(p)]
        st = {r_["cond"]: None for r_ in recs}
        if f"truce_{comp}" not in st:
            continue
        by = collections.defaultdict(lambda: collections.defaultdict(list))   # group -> job -> values
        loss = collections.defaultdict(lambda: collections.defaultdict(float))
        tot = collections.defaultdict(int)
        seen = set()
        for r in recs:
            if r["cond"] != f"truce_{comp}" or (r["job"], r["primary"]) not in files:
                continue
            k = (r["job"], r["primary"], r["task"])
            if k in seen:
                continue
            seen.add(k)
            j = next(x for x in JOBS if x.id == r["job"])
            P = r["primary"]
            Q = "B" if P == "A" else "A"
            fate, right_pair = files[(r["job"], P)]
            tot[r["job"]] += 1
            for l, key, cat in target_set(j, P):
                side = "P" if l == P else "Q"
                rel = j.skills[l].req(key).rel
                f = fate[(l, key)][0]
                ok = f == expected(side, rel) and (rel != "ent" or right_pair)
                g = "handled right" if ok else ("wrongly dropped or not extracted" if f in ("dropped", "not extracted") else
                                                "wrongly combined" if f == "combined" else "entangled rule left unreconciled")
                v = float(r["scores"][f"{l}.{key}"])
                by[g][r["job"]].append(v)
                loss[g][r["job"]] += (1 - v) / 10.0
        groups = {}
        for g, d in by.items():
            vals = [x for v in d.values() for x in v]
            groups[g] = dict(rule_slots=len(vals), followed=float(np.mean(vals)),
                             points_lost=float(np.mean([loss[g].get(jid, 0.0) / tot[jid] for jid in tot])) * 100)
        res["executors"][ex] = groups
        print(f"  executor {ex}: " + "; ".join(f"{g}: {100 * v['followed']:.0f}% followed in {v['rule_slots']} slots, costs {v['points_lost']:.1f} points"
                                               for g, v in sorted(groups.items())))
    out[comp] = res
json.dump(out, open(f"{ROOT}/runs/merge_errors.json", "w"), indent=1)
print("\nwrote runs/merge_errors.json")


# ---------------------------------------------------------------- file level: clean files against files with a detection error
def example_of(text):
    """The example output inside a merged skill file (best effort)."""
    i = text.rfind("Output:")
    body = text[i + 7:] if i >= 0 else text[text.rfind("## Example"):] if "## Example" in text else ""
    if "```" in body:
        parts = body.split("```")
        if len(parts) >= 3:
            inner = parts[1]
            return inner.split("\n", 1)[1] if "\n" in inner and not inner.startswith("\n") and len(inner.split("\n", 1)[0]) < 15 else inner
    return body


from spec import score  # noqa: E402

print("\n=== FILE LEVEL: structured files with every rule handled right ('clean') against files with at least one error")
out2 = {}
for comp in COMPILERS:
    clean = {}
    for j in JOBS:
        for P in "AB":
            p = f"{ROOT}/meta/truce_{comp}/{j.id}_{P}.json"
            if not os.path.exists(p):
                continue
            rep = json.load(open(p))
            if "relations" not in rep:
                continue
            fate, right_pair = plan(j, P, rep)
            Q = "B" if P == "A" else "A"
            ok = right_pair and fate[(Q, "con")][0] == "dropped"
            for L, side in ((P, "P"), (Q, "Q")):
                for req in j.skills[L].reqs:
                    if side == "Q" and req.rel in ("con", "sh"):
                        continue
                    ok = ok and fate[(L, req.key)][0] == expected(side, req.rel)
            clean[(j.id, P)] = ok
    if not clean:
        continue
    # examples inside the files
    exs = {}
    for v in (f"truce_{comp}", f"freemerge_{comp}"):
        good = n = 0
        for j in JOBS:
            for P in "AB":
                p = f"{ROOT}/meta/{v}/{j.id}_{P}.md"
                if os.path.exists(p):
                    s = score(j, example_of(open(p).read()))
                    n += 1
                    good += all(s[f"{l}.{k}"] for l, k, _ in target_set(j, P))
        if n:
            exs[v] = f"{good}/{n}"
    res = dict(clean_files=sum(clean.values()), files=len(clean), examples_meeting_every_achievable_rule=exs, executors={})
    print(f"\ncompiler {comp}: {sum(clean.values())} of {len(clean)} structured files are clean; example in the file meets every achievable rule: {exs}")
    for ex in EXECUTORS:
        cell = collections.defaultdict(dict)   # cond -> (job, P) -> mean fidelity
        for p in sorted(glob.glob(f"{ROOT}/runs/{ex}/treat*.jsonl")):
            if p.endswith("treat_v1.jsonl"):
                continue
            tmp = collections.defaultdict(lambda: collections.defaultdict(dict))
            for l in open(p):
                r = json.loads(l)
                if r["cond"] in (f"truce_{comp}", f"freemerge_{comp}", f"truce_noex_{comp}", f"truce_oracle_{comp}"):
                    j = next(x for x in JOBS if x.id == r["job"])
                    t = target_set(j, r["primary"])
                    tmp[r["cond"]][(r["job"], r["primary"])][r["task"]] = np.mean([r["scores"][f"{a}.{b}"] for a, b, _ in t])
            for c, d in tmp.items():
                for k, v in d.items():
                    cell[c][k] = float(np.mean(list(v.values())))
        if f"truce_{comp}" not in cell or f"freemerge_{comp}" not in cell:
            continue
        row = {}
        for name, sel in (("clean", True), ("with an error", False)):
            ks = [k for k in clean if clean[k] == sel and k in cell[f"truce_{comp}"] and k in cell[f"freemerge_{comp}"]]
            if ks:
                row[name] = dict(files=len(ks), structured=float(np.mean([cell[f"truce_{comp}"][k] for k in ks])),
                                 free_form=float(np.mean([cell[f"freemerge_{comp}"][k] for k in ks])),
                                 structured_no_example=float(np.mean([cell[f"truce_noex_{comp}"][k] for k in ks])) if f"truce_noex_{comp}" in cell else None,
                                 structured_true_relations=float(np.mean([cell[f"truce_oracle_{comp}"][k] for k in ks])) if f"truce_oracle_{comp}" in cell else None)
        res["executors"][ex] = row
        for name, v in row.items():
            print(f"  executor {ex}, {v['files']} files {name}: structured {100 * v['structured']:.1f}, free-form {100 * v['free_form']:.1f}"
                  + (f", structured without example {100 * v['structured_no_example']:.1f}" if v["structured_no_example"] is not None else "")
                  + (f", structured with true relations {100 * v['structured_true_relations']:.1f}" if v["structured_true_relations"] is not None else ""))
    out2[comp] = res
out["file_level"] = out2
json.dump(out, open(f"{ROOT}/runs/merge_errors.json", "w"), indent=1)

#!/usr/bin/env python
"""Secondary analysis of the public run logs of "One Skill Too Many" (arXiv 2610.11647).

Data: https://github.com/ltroin/conflict (data/runs.jsonl, data/cases.jsonl), cloned to external/conflict_repo/repo.
Question: when the agent actually uses BOTH co-installed skills in a run, what happens to the installed
skill's core functions, compared with the paired run that had only the installed skill?

We take the first completed replicate of every (case, configuration, model). We keep pairs whose only-A run
used A, split A+B runs by which skills they used, and report the paired change in the share of applicable core
functions fulfilled, separately for functions exclusive to A and shared with B. Differences are averaged within
case and bootstrapped over cases (95% percentile interval, 10,000 resamples, seed 0).
This is observational: which skills a run uses is not randomized.
"""
import collections
import json
import os

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = f"{ROOT}/external/conflict_repo/repo/data"
rows = [json.loads(l) for l in open(f"{D}/runs.jsonl")]
cases = {json.loads(l)["case_id"]: json.loads(l) for l in open(f"{D}/cases.jsonl")}
best = {}
for r in sorted(rows, key=lambda r: r["replicate"]):
    best.setdefault((r["case_id"], r["configuration"], r["model"]), r)


def rate(r, excl):
    cf = {str(f["rank"]): f for f in cases[r["case_id"]]["core_functions"]}
    v = [x for k, x in r["all_items"].items() if x is not None and (excl is None or cf.get(k, {}).get("exclusive") == excl)]
    return float(np.mean(v)) if v else None


def boot(d):
    d = np.array(d, float)
    rng = np.random.default_rng(0)
    m = d[rng.integers(0, len(d), (10000, len(d)))].mean(1)
    return dict(mean=float(d.mean()), lo=float(np.percentile(m, 2.5)), hi=float(np.percentile(m, 97.5)), pairs=int(len(d)))


USE = {"both skills used": lambda r: r["used_A"] and r["used_B"], "only A used": lambda r: r["used_A"] and not r["used_B"],
       "only B used": lambda r: r["used_B"] and not r["used_A"], "neither used": lambda r: not r["used_A"] and not r["used_B"]}
out = {}
for cfg_name, cfgs in (("A+B", ["both"]), ("A+B and swapped", ["both", "both_swapped"])):
    out[cfg_name] = {}
    for use, cond in USE.items():
        for excl, en in ((True, "exclusive"), (False, "shared"), (None, "all")):
            byc, comp, n = collections.defaultdict(list), [], 0
            for (c, cfg, m), r in best.items():
                if cfg not in cfgs or not cond(r):
                    continue
                a = best.get((c, "A_only", m))
                if a is None or not a["used_A"]:
                    continue
                x, y = rate(r, excl), rate(a, excl)
                if x is None or y is None:
                    continue
                byc[c].append(100 * (x - y))
                n += 1
                if r["completion"] is not None and a["completion"] is not None:
                    comp.append(100 * (r["completion"] - a["completion"]))
            if len(byc) > 5:
                b = boot([np.mean(v) for v in byc.values()])
                b.update(runs=n, completion_delta=float(np.mean(comp)) if comp else None)
                out[cfg_name][f"{use} / {en}"] = b
                print(f"{cfg_name:16s} {use:17s} {en:9s} {b['mean']:+6.1f} pp [{b['lo']:+.1f}, {b['hi']:+.1f}]  pairs={b['pairs']} runs={n} completion {b['completion_delta']:+.1f}")
out["use_pattern_in_A+B"] = {}
for m in ("haiku", "sonnet", "opus"):
    rs = [r for (c, cfg, mm), r in best.items() if cfg == "both" and mm == m]
    out["use_pattern_in_A+B"][m] = {k: float(np.mean([bool(f(r)) for r in rs])) for k, f in USE.items()} | {"runs": len(rs)}
    print(m, {k: round(100 * v, 1) if k != "runs" else v for k, v in out["use_pattern_in_A+B"][m].items()})
os.makedirs(f"{ROOT}/runs", exist_ok=True)
json.dump(out, open(f"{ROOT}/runs/reanalysis_ostm.json", "w"), indent=1)
print("wrote runs/reanalysis_ostm.json")

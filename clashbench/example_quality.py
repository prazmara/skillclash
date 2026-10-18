#!/usr/bin/env python
"""Does the worked example of a merged file help in proportion to how correct it is? Usage: python example_quality.py

For every merger M and every (job, primary) cell, the example of M's step-by-step file (meta/truce_<M>) is scored on the
achievable rules with the benchmark's own checker. Its effect is read from the variant that adds only that example to the
rule union with a priority line (meta/unionwex_<M>, meta/unionagentex for Claude Opus 5.5): achievable rules followed with
the example minus without it (union_prec), per cell, for each reader model that ran the variants.
Writes runs/example_quality.json and prints a summary. Nothing here calls a model.
"""
import collections
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from spec import score, target_set  # noqa: E402
import jobs_core  # noqa: E402
import jobs_extra  # noqa: E402

JOBS = list(jobs_core.JOBS) + list(jobs_extra.JOBS)
MERGERS = {"mistral7b": "unionwex_mistral7b", "qwen7b": "unionwex_qwen7b", "llama8b": "unionwex_llama8b", "qwen4b": "unionwex_qwen4b",
           "qwen235b": "unionwex_qwen235b", "gpt41": "unionwex_gpt41", "agent": "unionagentex"}
READERS = ["qwen4b", "qwen7b", "llama8b"]


def example_of(text):
    """The example output inside a merged skill file (same rule as merge_errors.py)."""
    i = text.rfind("Output:")
    body = text[i + 7:] if i >= 0 else text[text.rfind("## Example"):] if "## Example" in text else ""
    if "```" in body:
        parts = body.split("```")
        if len(parts) >= 3:
            inner = parts[1]
            return inner.split("\n", 1)[1] if "\n" in inner and not inner.startswith("\n") and len(inner.split("\n", 1)[0]) < 15 else inner
    return body


def boot(v):
    v = np.array(v, float)
    if len(v) == 0:
        return dict(mean=None, lo=None, hi=None, n=0)
    m = v[np.random.default_rng(0).integers(0, len(v), (10000, len(v)))].mean(1)
    return dict(mean=float(v.mean()), lo=float(np.percentile(m, 2.5)), hi=float(np.percentile(m, 97.5)), n=int(len(v)))


def cell_mss(tag, cond):
    """(job, P) -> mean share of the achievable rules followed, from runs/<tag>/treat*.jsonl."""
    out = collections.defaultdict(list)
    for fn in sorted(os.listdir(f"{ROOT}/runs/{tag}")):
        if not (fn.startswith("treat") and fn.endswith(".jsonl")) or fn == "treat_v1.jsonl":
            continue
        for line in open(f"{ROOT}/runs/{tag}/{fn}"):
            r = json.loads(line)
            if r["cond"] != cond:
                continue
            j = next(x for x in JOBS if x.id == r["job"])
            tgt = target_set(j, r["primary"])
            out[(r["job"], r["primary"])].append(np.mean([r["scores"][f"{l}.{k}"] for l, k, _ in tgt]))
    return {k: float(np.mean(v)) for k, v in out.items()}


ex = {}   # (merger, job, P) -> (share of achievable rules the example meets, meets all)
for M in MERGERS:
    src = "truce_agent" if M == "agent" else f"truce_{M}"
    for j in JOBS:
        for P in "AB":
            p = f"{ROOT}/meta/{src}/{j.id}_{P}.md"
            if os.path.exists(p):
                s = score(j, example_of(open(p).read()))
                tgt = target_set(j, P)
                ex[(M, j.id, P)] = (float(np.mean([s[f"{l}.{k}"] for l, k, _ in tgt])), bool(all(s[f"{l}.{k}"] for l, k, _ in tgt)))

res = dict(mergers={}, pooled={})
for R in READERS:
    if not os.path.exists(f"{ROOT}/runs/{R}"):
        continue
    base = cell_mss(R, "union_prec")
    rows, per_merger = [], {}
    for M, cond in MERGERS.items():
        withex = cell_mss(R, cond)
        cells = [(k, withex[k] - base[k]) for k in withex if k in base and (M, *k) in ex]
        if not cells:
            continue
        by_job = collections.defaultdict(list)
        for (jid, P), d in cells:
            by_job[jid].append(d)
            rows.append(dict(merger=M, job=jid, primary=P, gain=d, example_share=ex[(M, jid, P)][0], example_correct=ex[(M, jid, P)][1]))
        per_merger[M] = dict(gain=boot([np.mean(v) for v in by_job.values()]),
                             correct_examples=sum(ex[(M, *k)][1] for k, _ in cells), files=len(cells))
    if not rows:
        continue
    res["mergers"][R] = per_merger
    g_ok = [r["gain"] for r in rows if r["example_correct"]]
    g_bad = [r["gain"] for r in rows if not r["example_correct"]]
    xs, ys = np.array([r["example_share"] for r in rows]), np.array([r["gain"] for r in rows])
    res["pooled"][R] = dict(correct=boot(g_ok), not_correct=boot(g_bad), n_correct=len(g_ok), n_not_correct=len(g_bad),
                            corr_example_share_gain=float(np.corrcoef(xs, ys)[0, 1]) if len(rows) > 2 else None)
    print(f"\n=== reader {R}: achievable rules followed, rule union + merger's example minus rule union (points, 95% CI over jobs)")
    for M, v in per_merger.items():
        g = v["gain"]
        print(f"  {M:10s} correct examples {v['correct_examples']:2d}/{v['files']}   gain {100 * g['mean']:+6.1f} [{100 * g['lo']:+.1f}, {100 * g['hi']:+.1f}]")
    pr = res["pooled"][R]
    print(f"  pooled over files: correct example {100 * pr['correct']['mean']:+.1f} [{100 * pr['correct']['lo']:+.1f}, {100 * pr['correct']['hi']:+.1f}] (n={pr['n_correct']}), "
          f"not correct {100 * pr['not_correct']['mean']:+.1f} [{100 * pr['not_correct']['lo']:+.1f}, {100 * pr['not_correct']['hi']:+.1f}] (n={pr['n_not_correct']}); "
          f"correlation of example share with gain {pr['corr_example_share_gain']:+.2f}")
json.dump(res, open(f"{ROOT}/runs/example_quality.json", "w"), indent=1)
print("\nwrote runs/example_quality.json")

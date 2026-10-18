#!/usr/bin/env python
"""Run only meta-skill variants, with the treat stage's prompts, and nothing else.

Usage: python treat_variants.py --model qwen7b --suffix _abl2 --variants a,b,c [--hf-model ...] [--tok-budget N]
Same specs as harness.stage_treat for --variants, but without the two priority-instruction conditions that the treat stage
always adds. Use it for a model whose earlier runs were made elsewhere, so those conditions are not regenerated and do not
replace the delivered records. Writes runs/<tag>/treat<suffix>.jsonl.
"""
import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import harness as H  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--hf-model", default="")
    ap.add_argument("--suffix", required=True)
    ap.add_argument("--variants", required=True)
    ap.add_argument("--tok-budget", type=int, default=22000)
    ap.add_argument("--limit-tasks", type=int, default=99)
    a = ap.parse_args()
    if a.hf_model:
        H.MODELS[a.model] = a.hf_model
    lm = H.LM(a.model, a.tok_budget)
    specs = []
    for job in H.JOBS:
        for P in "AB":
            for v in [x for x in a.variants.split(",") if x]:
                m = H.load_meta(v, job, P)
                if m is None:
                    continue
                for ti, req in enumerate(job.tasks[:a.limit_tasks]):
                    specs.append(dict(job=job.id, task=ti, request=req, cond=v, primary=P, system=H.sys_prompt([m])))
    recs = H.run(lm, specs, None, desc="treat")
    path = f"{H.ROOT}/runs/{a.model}/treat{a.suffix}.jsonl"
    with open(path, "w") as f:
        for r in recs:
            f.write(json.dumps(r) + "\n")
    H.log(f"wrote {len(recs)} records to {path}")
    H.log(f"=== variants finished; generated {lm.n_gen}, cache hits {lm.n_hit}")


if __name__ == "__main__":
    main()

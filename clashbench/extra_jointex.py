#!/usr/bin/env python
"""Ablation: two separate skill files, each ending with an example that follows BOTH skills.

Usage: python extra_jointex.py --model qwen4b [--hf-model ...] [--tok-budget N]
Each skill file keeps its own rules (harness.skill_text without its example) and ends with the example section of Claude
Opus 5.5's merged file for that primary skill (meta/truce_agent). Both load orders. Prompts and checkers are unchanged.
Conditions jointex_PQ / jointex_QP (primary listed first / second), written as treatment records to
runs/<tag>/treat_jointex.jsonl, so analyze.py scores them on the achievable rules of the primary.
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
    ap.add_argument("--tok-budget", type=int, default=22000)
    ap.add_argument("--limit-tasks", type=int, default=99)
    a = ap.parse_args()
    if a.hf_model:
        H.MODELS[a.model] = a.hf_model
    lm = H.LM(a.model, a.tok_budget)
    specs = []
    for job in H.JOBS:
        for P in "AB":
            Q = "B" if P == "A" else "A"
            m = H.load_meta("truce_agent", job, P)
            i = m.find("\n## Example") if m else -1
            if i < 0:
                continue
            ex = m[i:].rstrip()
            fp, fq = H.skill_text(job, P, False) + "\n" + ex, H.skill_text(job, Q, False) + "\n" + ex
            for ti, req in enumerate(job.tasks[:a.limit_tasks]):
                for c, texts in (("jointex_PQ", [fp, fq]), ("jointex_QP", [fq, fp])):
                    specs.append(dict(job=job.id, task=ti, request=req, cond=c, primary=P, system=H.sys_prompt(texts)))
    recs = H.run(lm, specs, None, desc="jointex")
    path = f"{H.ROOT}/runs/{a.model}/treat_jointex.jsonl"
    with open(path, "w") as f:
        for r in recs:
            f.write(json.dumps(r) + "\n")
    H.log(f"wrote {len(recs)} records to {path}")
    H.log(f"=== joint-example ablation finished; generated {lm.n_gen}, cache hits {lm.n_hit}")


if __name__ == "__main__":
    main()

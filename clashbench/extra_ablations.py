#!/usr/bin/env python
"""Extra ablation: two skill files where only ONE skill keeps its worked example.

Usage: python extra_ablations.py --model qwen4b [--hf-model ...] [--tok-budget N]
Conditions (both load orders): exA_AB, exA_BA (only skill A has its example), exB_AB, exB_BA (only skill B has it).
Prompts, skill texts and checkers come unchanged from harness.py and spec.py; only which skill shows its example
differs. Writes runs/<tag>/ablate_oneex.jsonl, using and extending runs/<tag>/cache.jsonl like every other stage.
"""
import argparse
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
        sk = {(L, ex): H.skill_text(job, L, ex) for L in "AB" for ex in (True, False)}
        for ti, req in enumerate(job.tasks[:a.limit_tasks]):
            for has in "AB":
                for order in ("AB", "BA"):
                    texts = [sk[(L, L == has)] for L in order]
                    specs.append(dict(job=job.id, task=ti, request=req, cond=f"ex{has}_{order}", system=H.sys_prompt(texts)))
    H.run(lm, specs, f"{H.ROOT}/runs/{a.model}/ablate_oneex.jsonl", desc="oneex")
    H.log(f"=== one-example ablation finished; generated {lm.n_gen}, cache hits {lm.n_hit}")


if __name__ == "__main__":
    main()

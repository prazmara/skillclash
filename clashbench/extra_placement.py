#!/usr/bin/env python
"""Robustness check: the skill files in the user turn instead of the system prompt.

Usage: python extra_placement.py --model qwen4b [--hf-model ...] [--tok-budget N]
The system prompt is only the base sentence (harness.SYS_BASE). The user turn holds the same loading sentence and the same
<skill> blocks that harness.sys_prompt puts in the system prompt, followed by the usual request (harness.user_prompt).
Conditions: user_A, user_B (one skill), user_AB, user_BA (both, two load orders). Writes runs/<tag>/ablate_placement.jsonl.
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
        sk = {L: H.skill_text(job, L) for L in "AB"}
        for ti, req in enumerate(job.tasks[:a.limit_tasks]):
            for c in ("A", "B", "AB", "BA"):
                skills = H.sys_prompt([sk[L] for L in c])[len(H.SYS_BASE) + 1:]   # loading sentence and <skill> blocks
                specs.append(dict(job=job.id, task=ti, request=req, cond=f"user_{c}", system=H.SYS_BASE,
                                  user=skills + "\n\n" + H.user_prompt(job, req)))
    H.run(lm, specs, f"{H.ROOT}/runs/{a.model}/ablate_placement.jsonl", desc="placement")
    H.log(f"=== placement check finished; generated {lm.n_gen}, cache hits {lm.n_hit}")


if __name__ == "__main__":
    main()

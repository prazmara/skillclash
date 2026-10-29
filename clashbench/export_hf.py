#!/usr/bin/env python
"""Write the Hugging Face dataset files (hf/data/*.parquet) from the benchmark, meta/ and runs/.

Usage: python export_hf.py          (needs pyarrow; the dataset card is hf/README.md)
Upload: hf upload prazmara/skillclash ../hf . --repo-type dataset

Tables (one config each on the Hub):
  jobs           16 jobs: both SKILL.md files and the two reference outputs (one per skill that wins the contradiction)
  rules          192 rules: relation to the other skill, position in the file, whether it is achievable when A or B wins
  requests       128 held-out requests with the user prompt and the system prompts for A, B, AB and BA
  merged_skills  the files in meta/ (variant, job, primary skill, text, and the variant's json info)
  outputs        every scored output in runs/<model>/*.jsonl; scores are the checker results of spec.score
The checkers are code, so scoring a new output needs spec.score from this repository.
"""
import glob
import json
import os
import sys

import pyarrow as pa
import pyarrow.parquet as pq

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from harness import JOBMAP, JOBS, ROOT, skill_text, sys_prompt, user_prompt  # noqa: E402
from spec import rule_order, target_set  # noqa: E402

OUT = f"{ROOT}/hf/data"
NAMES = {"qwen4b": "Qwen/Qwen3-4B-Instruct-2507", "qwen7b": "Qwen/Qwen2.5-7B-Instruct",
         "mistral7b": "mistralai/Mistral-7B-Instruct-v0.3", "llama8b": "meta-llama/Llama-3.1-8B-Instruct",
         "phi4mini": "microsoft/Phi-4-mini-instruct", "qwen235b": "qwen/qwen3-235b-a22b-2507", "gpt41": "openai/gpt-4.1"}
KEYS = [f"{L}.{k}" for L in "AB" for k in ("con", "e1", "e2", "e3", "sh", "ent")]


def write(name, rows, schema=None):
    pq.write_table(pa.Table.from_pylist(rows, schema=schema), f"{OUT}/{name}.parquet", compression="zstd")
    print(f"{name}: {len(rows)} rows")


def main():
    os.makedirs(OUT, exist_ok=True)
    write("jobs", [dict(job_id=j.id, artifact=j.artifact, example_request=j.example_request,
                        skill_a_name=j.skills["A"].name, skill_b_name=j.skills["B"].name,
                        skill_a=skill_text(j, "A"), skill_b=skill_text(j, "B"),
                        reference_output_a_wins=j.witness["A"], reference_output_b_wins=j.witness["B"]) for j in JOBS])

    rules = []
    for j in JOBS:
        win = {P: {(L, k) for L, k, _ in target_set(j, P)} for P in "AB"}
        for L in "AB":
            s = j.skills[L]
            pos = {r.key: i + 1 for i, r in enumerate(rule_order(s, j))}
            rules += [dict(job_id=j.id, skill=L, skill_name=s.name, rule_key=r.key, relation=r.rel, text=r.text,
                           position=pos[r.key], achievable_if_a_wins=(L, r.key) in win["A"],
                           achievable_if_b_wins=(L, r.key) in win["B"]) for r in s.reqs]
    write("rules", rules)

    reqs = []
    for j in JOBS:
        A, B = skill_text(j, "A"), skill_text(j, "B")
        reqs += [dict(job_id=j.id, task=t, request=q, user_prompt=user_prompt(j, q), system_a=sys_prompt([A]),
                      system_b=sys_prompt([B]), system_ab=sys_prompt([A, B]), system_ba=sys_prompt([B, A]))
                 for t, q in enumerate(j.tasks)]
    write("requests", reqs)

    merged = []
    for d in sorted(glob.glob(f"{ROOT}/meta/*/")):
        v = os.path.basename(d.rstrip("/"))
        if v.startswith("_"):  # superseded drafts
            continue
        for f in sorted(glob.glob(f"{d}*.md")):
            job, P = os.path.basename(f)[:-3].rsplit("_", 1)
            info = f[:-3] + ".json"
            merged.append(dict(variant=v, job_id=job, primary=P, text=open(f).read(),
                               info=open(info).read() if os.path.exists(info) else None))
    write("merged_skills", merged)

    schema = pa.schema([("model", pa.string()), ("model_id", pa.string()), ("source", pa.string()), ("job_id", pa.string()),
                        ("task", pa.int64()), ("cond", pa.string()), ("primary", pa.string()), ("request", pa.string()),
                        ("output", pa.string()), ("scores", pa.struct([(k, pa.bool_()) for k in KEYS])), ("extra", pa.string())])
    outs = []
    for f in sorted(glob.glob(f"{ROOT}/runs/*/*.jsonl")):
        tag, src = f.split("/")[-2], os.path.basename(f)[:-6]
        for line in open(f):
            r = json.loads(line)
            q = JOBMAP[r["job"]].tasks[r["task"]]
            assert r.get("request", q) == q, (f, r["job"], r["task"])
            rest = {k: v for k, v in r.items() if k not in ("job", "task", "cond", "primary", "request", "output", "scores")}
            outs.append(dict(model=tag, model_id=NAMES[tag], source=src, job_id=r["job"], task=r["task"], cond=r["cond"],
                             primary=r.get("primary"), request=q, output=r["output"], scores=r["scores"],
                             extra=json.dumps(rest) if rest else None))
    write("outputs", outs, schema)


if __name__ == "__main__":
    main()

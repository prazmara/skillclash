---
license: cc-by-4.0
language:
- en
pretty_name: SkillClash
size_categories:
- 10K<n<100K
task_categories:
- text-generation
tags:
- agent-skills
- instruction-following
- llm-agents
- benchmark
configs:
- config_name: requests
  default: true
  data_files:
  - split: test
    path: data/requests.parquet
- config_name: jobs
  data_files:
  - split: test
    path: data/jobs.parquet
- config_name: rules
  data_files:
  - split: test
    path: data/rules.parquet
- config_name: merged_skills
  data_files:
  - split: test
    path: data/merged_skills.parquet
- config_name: outputs
  data_files:
  - split: test
    path: data/outputs.parquet
---

# SkillClash

Benchmark and results for the paper [One Skill Takes Over: Clashing Agent Skills and a One-File Fix](https://arxiv.org/abs/2610.25064).
Code: [github.com/prazmara/skillclash](https://github.com/prazmara/skillclash).

SkillClash has 16 jobs (commit message, SQL query, changelog entry, ...). Each job has two Agent Skills (SKILL.md files) for
the same job, with six rules each, and code checks every rule. When both skills are loaded, most outputs follow one skill
completely and drop the other ("takeover"). The paper measures this on seven models and tests fixes, among them merged skill files.

## Tables

| Config | Rows | One row is |
|---|---|---|
| `requests` | 128 | a held-out request (8 per job), with the user prompt and the system prompts that load skill A, B, A then B, or B then A |
| `jobs` | 16 | a job: both SKILL.md files and two reference outputs, one for each skill winning the contradiction |
| `rules` | 192 | a rule: its relation to the other skill, its position in the file, and whether it is achievable when A or B wins |
| `merged_skills` | 1,632 | a merged or code-made skill file from `meta/` of the repository (51 variants x 16 jobs x 2 primary skills) |
| `outputs` | 91,648 | a scored model output from the paper's runs (7 models, every condition) |

```python
from datasets import load_dataset

requests = load_dataset("prazmara/skillclash", "requests", split="test")
outputs = load_dataset("prazmara/skillclash", "outputs", split="test")
```

## Scoring a new model

The rule checkers are code, so scoring needs the repository. Send `system_ab` (and `system_ba`) as the system message and
`user_prompt` as the user message, then score the reply:

```python
# git clone https://github.com/prazmara/skillclash && cd skillclash/clashbench
from harness import JOBMAP
from spec import score

scores = score(JOBMAP[row["job_id"]], reply)   # {"A.con": True, "A.e1": False, ...}
```

`bash run_model.sh <tag> --hf-model <id>` (or `--api-model`) in `clashbench/` runs every condition of the paper and
`python analyze.py <tag>` makes the tables.

## Fields

Rule keys (`rules.rule_key`, and `A.<key>` / `B.<key>` in `outputs.scores`): `con` is the rule that contradicts the other
skill, `e1` to `e3` are asked for by this skill only, `sh` is asked for by both skills, `ent` is entangled with a rule of the
other skill (both can hold, but only if combined in one specific way). `relation` is `con`, `excl`, `sh` or `ent`.
When skill P wins the contradiction, ten rules are achievable: all six of P and the four exclusive and entangled rules of
the other skill (`achievable_if_a_wins`, `achievable_if_b_wins`). The paper reports the share of these that an output follows.

`outputs` columns:

- `model`, `model_id`: the model that wrote the output (Hugging Face ID, or OpenRouter ID for Qwen3-235B and GPT-4.1).
- `source`: the run file in `runs/<model>/` (`diag`, `ablate`, `treat`, `variance`, `steer_gen`, ...).
- `cond`: the condition. In `diag`: `none`, `A`, `B`, `AB`, `BA` (both skills, in that order), `AC`, `CA`, `BC`, `CB`
  (with an unrelated skill C). In the `treat*` files, `primary` is the skill P that should win the contradiction, Q is the
  other one, and `cond` is `prec_PQ`/`prec_QP` (priority instruction), `strong_PQ`/`strong_QP` ("apply both" instruction),
  `union_noex`/`union_prec` (rule union written by code, without/with a priority line), `checklist_PQ`, `seqrev`
  (write with P, then revise with Q), `jointex_PQ`/`jointex_QP` (two skill files that each end with an example that follows
  both skills), or the name of a `merged_skills` variant. `ablate` holds the files without examples (`noex_*`), without the
  contradiction (`nocon_*`) and fully compatible (`compat_*`); `ablate_oneex` has only one skill with its example
  (`exA_*`, `exB_*`); `ablate_placement` has the skills in the user turn.
- `scores`: the checker result for all twelve rules of both skills.
- `extra`: JSON with fields that only some files have (`seed` for sampled runs, steering settings, `full_output` of the checklist condition).

Main `merged_skills` variants: `truce_agent` is the merged file written by Claude Opus 5.5 ("Claude's merged file" in the
paper); `freemerge_<model>` is the model's plain merge; `truce_<model>` its step-by-step merge (rule pairs labeled first);
`truce_oracle_<model>` the step-by-step merge given the true labels; `*_noex` the same without the worked example;
`unionfile` the rule union with a priority line; `unionex`, `unionagentex`, `unionwex_<model>` the rule union plus both
original examples, plus the example of Claude's file, or plus the example of that model's merged file; `onefile_full` both
full skill files in one file; `*_ref_*` files after the feedback loop. `info` holds each file's settings.

## Notes

- The skills were written for the benchmark, with planted relations between their rules; they are not collected from public skill libraries.
- Decoding is greedy (temperature 0 for the API models), except in `variance` (temperature 0.7, three seeds).
- The human check of the rule relations is described in the paper; its answer key is not released.

## License and citation

Data: CC BY 4.0. Code (GitHub): MIT.

```bibtex
@article{razmara2026skillclash,
  title   = {One Skill Takes Over: Clashing Agent Skills and a One-File Fix},
  author  = {Razmara, Parsa and Azizi, Seyedarmin and Aryashad, Ardalan},
  journal = {arXiv preprint arXiv:2610.25064},
  year    = {2026}
}
```

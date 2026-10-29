# SkillClash: clashing Agent Skills and a one-file fix

Code, benchmark, and results for the paper *One Skill Takes Over: Clashing Agent Skills and a One-File Fix*.

[Paper (arXiv:2610.25064)](https://arxiv.org/abs/2610.25064) · [Dataset on Hugging Face](https://huggingface.co/datasets/prazmara/skillclash)

When two Agent Skills for the same job are loaded together, the model follows one of them completely and drops the other,
including rules that conflict with nothing ("takeover"). The worked examples inside the skills drive it. One merged skill
file that ends with an example that follows both skills fixes it.

## Results

Last five columns: share of the achievable rules followed (%). Every number is computed by clashbench/analyze.py from the files in runs/. The paper gives intervals and all ablations.

| Model | Rules followed, skill alone (%) | ... with a same-job skill (%) | Takeover (% of outputs) | Priority instruction | "Apply both" instruction | Rule union (code) | Model's own merge | Claude's merged file |
|---|---|---|---|---|---|---|---|---|
| Qwen3-4B-Instruct-2507 | 97 | 61 | 78 | 62 | 69 | 79 | 79 | 98 |
| Qwen2.5-7B-Instruct | 97 | 61 | 69 | 65 | 73 | 73 | 75 | 97 |
| Mistral-7B-Instruct-v0.3 | 93 | 62 | 45 | 65 | 78 | 75 | 80 | 97 |
| Llama-3.1-8B-Instruct | 98 | 61 | 66 | 62 | 72 | 79 | 87 | 99 |
| Phi-4-mini-instruct | 96 | 62 | 49 | 64 | 69 | 66 | 71 | 96 |
| Qwen3-235B-A22B-2507 | 99 | 62 | 73 | 71 | 88 | 86 | 94 | 99 |
| GPT-4.1 | 99 | 61 | 77 | 63 | 89 | 90 | 95 | 99 |

## Layout

| Path | What it is |
|---|---|
| `clashbench/spec.py`, `jobs_core.py`, `jobs_extra.py` | The benchmark: 16 jobs, two skills per job, six code-checked rules per skill |
| `clashbench/harness.py` | Runs a model on every condition (local Hugging Face model or OpenAI-compatible API) |
| `clashbench/run_model.sh` | One command for the full pipeline of one model |
| `clashbench/extra_*.py`, `treat_variants.py`, `make_variants.py` | Ablations: one example only, skills in the user turn, an example that follows both skills, file versus examples |
| `clashbench/steer.py` | Linear probe and activation steering |
| `clashbench/analyze.py`, `merge_errors.py`, `example_quality.py` | Analysis |
| `skills/<job>/A.md`, `B.md` | The 32 skills as SKILL.md files |
| `meta/<variant>/<job>_<P>.md` | Merged skills and code-made variants; `P` is the skill that wins a true contradiction |
| `runs/<model>/` | Outputs and scores for every condition (`*.jsonl`), `analysis.json`, `tables.txt` |
| `human_validation/` | The rule-pair sheet and a blank form for the human check (answer key not included) |
| `clashbench/export_hf.py`, `hf/` | Builds the Hugging Face dataset (`hf/data/*.parquet`) from the files above; `hf/README.md` is its dataset card |

## Hugging Face dataset

The benchmark, the merged skills and all scored outputs are also on the Hub as five tables
(`requests`, `jobs`, `rules`, `merged_skills`, `outputs`):

```python
from datasets import load_dataset
requests = load_dataset("prazmara/skillclash", "requests", split="test")
```

Scoring a new output still needs `spec.score` from this repository (the checkers are code); see the dataset card.

## Reproduce

```bash
pip install numpy torch transformers accelerate
cd clashbench
python selftest.py                                   # 16 jobs, 0 failures
bash run_model.sh qwen4b --hf-model Qwen/Qwen3-4B-Instruct-2507
# API model: the key is read from the environment variable you name and is never written to disk
bash run_model.sh mytag --api-model <model> --api-base <url ending in /v1> --api-key-env MY_API_KEY
python analyze.py qwen4b
# ablations of the paper (each writes new files into runs/<tag>/)
python make_variants.py
python extra_ablations.py --model qwen4b; python extra_placement.py --model qwen4b; python extra_jointex.py --model qwen4b
python treat_variants.py --model qwen4b --suffix _abl2 --variants onefile_full,unionex,truceagent_noex,unionagentex
python steer.py --model qwen4b --stage acts,probe,sweep,test,report
```

Every model call is cached in `runs/<tag>/cache.jsonl` (not included here because of its size), so reruns are free.
Decoding is greedy; results on other GPUs can differ in a few outputs.

## Models and runs

Open models were run in half precision on single A100 GPUs (Qwen2.5-7B and Mistral-7B on a cloud GPU with pinned
revisions). Qwen3-235B and GPT-4.1 were called through OpenRouter at temperature 0; GPT-4.1 ran four of the eight
requests per job. Runs made by co-authors were replayed with this code and gave identical scores.

## Not included

Model caches and activation files (about 0.5 GB), logs, the human-check answer key, and working notes.

## License

Code: MIT (`LICENSE`). Data (`skills/`, `meta/`, `runs/`, `human_validation/`, the Hugging Face dataset): CC BY 4.0 (`LICENSE-DATA`).

## Citation

```bibtex
@article{razmara2026skillclash,
  title   = {One Skill Takes Over: Clashing Agent Skills and a One-File Fix},
  author  = {Razmara, Parsa and Azizi, Seyedarmin and Aryashad, Ardalan},
  journal = {arXiv preprint arXiv:2610.25064},
  year    = {2026}
}
```

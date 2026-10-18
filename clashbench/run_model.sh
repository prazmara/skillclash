#!/bin/bash
# Full ClashBench run for ONE model as the agent (executor), plus that model as merge compiler.
#
# Local GPU model:  bash run_model.sh <tag> --hf-model <Hugging Face chat model id>
#   example:        bash run_model.sh qwen7b --hf-model Qwen/Qwen2.5-7B-Instruct
# API model:        bash run_model.sh <tag> --api-model <name> --api-base <url> --api-key-env MY_API_KEY
#   example:        bash run_model.sh mymodel --api-model provider/model --api-base https://openrouter.ai/api/v1 --api-key-env MY_API_KEY
#
# Environment switches:
#   PY=python3.11        python to use (default: python)
#   LIMIT=4              use only the first 4 of the 8 requests per job (halves the cost; say so when you report)
#   STAGES="diag treat"  run only some of: diag ablate treat compile own analyze (default: all, in that order)
# Everything is cached in runs/<tag>/cache.jsonl, so an interrupted run continues where it stopped.
set -u
cd "$(dirname "$0")" || exit 1
TAG=$1; shift
PY=${PY:-python}
STAGES=${STAGES:-"diag ablate treat compile own analyze"}
LIM=""; [ -n "${LIMIT:-}" ] && LIM="--limit-tasks $LIMIT"
mkdir -p ../logs
V=freemerge_qwen4b,truce_qwen4b,truce_noex_qwen4b,truce_oracle_qwen4b,truce_oracle_noex_qwen4b,truce_agent,freemerge_agent,truce_ref_frontier_qwen4b
run() { echo "=== $(date '+%F %T') $*" | tee -a ../logs/$TAG.log; $PY harness.py --model "$TAG" "$@" 2>&1 | grep -v -i "warn" | tee -a ../logs/$TAG.log; }
for st in $STAGES; do
  case $st in
    diag)    run --stage diag $LIM "$@" ;;                       # no skill, each skill alone, both orders, plus unrelated skill
    ablate)  run --stage ablate,variance $LIM "$@" ;;            # what triggers the takeover; sampling variance
    treat)   run --stage treat --variants $V $LIM "$@" ;;        # baselines and all merged skills shipped in meta/
    compile) run --stage compile "$@" ;;                         # this model writes its own merged skills into meta/*_<tag>/
    own)     run --stage treat --no-builtin --suffix _own --variants freemerge_$TAG,truce_$TAG,truce_noex_$TAG $LIM "$@" ;;
    analyze) $PY analyze.py "$TAG" 2>&1 | tee ../runs/$TAG/tables.txt ;;
  esac
done
echo "Done. Send back: runs/$TAG/ (without cache.jsonl if it is large) and meta/*_$TAG/"

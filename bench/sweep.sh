#!/usr/bin/env bash
# Run inside the vllm container (has vllm bench serve): docker compose exec vllm-proposer bash /workspace/bench/sweep.sh
set -euo pipefail
# MODEL must be the --served-model-name the server was started with
# (proposer/judge), not the underlying HF repo id — the server 404s on any
# other name. TOKENIZER must be the real HF repo id — the client loads the
# tokenizer straight from the hub/cache under that name, unrelated to what
# the server calls the model.
MODEL=${MODEL:-proposer}
TOKENIZER=${TOKENIZER:-openai/gpt-oss-120b}
BASE=${BASE:-http://localhost:8000}
# --dataset-name random + --ignore-eos crashes generation partway through
# for gpt-oss-120b: random-token-ID prompts decode to genuine multilingual
# noise, the model tries to give a short "I don't understand" reply and
# hit its natural stop point, and ignore_eos forcing it past that point
# produces a token sequence the harmony-format reasoning parser can't
# parse — the server 500s mid-stream with "Unexpected token N while
# expecting start token N". The client sees the stream end and silently
# records whatever partial content arrived as "completed", with no error
# surfaced — a 1024-token target can come back as ~40-90 actual tokens and
# LOOK like a normal successful run. Use the sonnet dataset (real English
# text) instead; it doesn't trigger the model's short-refusal path.
DATASET_PATH=${DATASET_PATH:-/opt/vllm/vllm-src/benchmarks/sonnet.txt}
IN=${IN:-4096}; OUT=${OUT:-1024}
DIR="/workspace/bench/results/$(date +%Y%m%d-%H%M)-in${IN}-out${OUT}"
mkdir -p "$DIR"

nvidia-smi --query-gpu=timestamp,power.draw,temperature.gpu,clocks.sm \
  --format=csv -l 5 > "$DIR/thermal.csv" &
SMI=$!
trap 'kill $SMI' EXIT

for C in 1 4 8 16 32 64 128 256; do
  N=$(( C * 4 )); (( N < 64 )) && N=64
  echo "=== concurrency=$C prompts=$N ==="
  vllm bench serve \
    --backend openai-chat --base-url "$BASE" \
    --endpoint /v1/chat/completions --model "$MODEL" --tokenizer "$TOKENIZER" \
    --dataset-name sonnet --dataset-path "$DATASET_PATH" \
    --sonnet-input-len "$IN" --sonnet-output-len "$OUT" --sonnet-prefix-len 200 \
    --ignore-eos \
    --num-prompts "$N" --max-concurrency "$C" --request-rate inf \
    --percentile-metrics ttft,tpot,itl,e2el \
    --save-result --result-dir "$DIR" --result-filename "c${C}.json"
  sleep 30
done

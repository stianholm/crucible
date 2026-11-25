#!/usr/bin/env bash
# PHASE-5.md task 5.2: the nightly window. Stop the proposer, train one adapter
# from the stock base, restart the proposer, load the adapter beside the stock
# model. Sequential and paranoid about memory, as the task asks.
#
# Usage: ops/nightly.sh [deadline]   deadline as HH:MM today/tomorrow, default 06:00
#
# Departures from the task's sketch, each forced by this machine:
# - Memory is read from /proc/meminfo, not nvidia-smi: on the GB10's unified
#   pool nvidia-smi reports memory.used as N/A, so the sketch's loop never ends.
#   And it is MemFree, after evicting the weights' page cache, not
#   MemAvailable: CUDA counts only free pages (ops/evict_cache.py).
# - Training runs in the pinned image (train/Dockerfile), not a host Python.
# - No signed review for the current selection means no training tonight
#   (task 5.1), and an adapter the deadline cut short is never loaded.
# - The judge stops too. gpt-oss-120b's QLoRA load does not fit beside it
#   (93 GB free was killed, 113 GB trained), and a judge restart costs no more
#   comparability than concurrent batching already does (TODO.md decision 71).
set -euo pipefail
cd "$(dirname "$0")/.."
set -a; . ./.env; set +a

STAMP=$(date +%Y%m%d)
DEADLINE=$(date -d "${1:-06:00}" +%s); [ "$DEADLINE" -gt "$(date +%s)" ] || DEADLINE=$((DEADLINE + 86400))
DEADLINE_ISO=$(date -d "@$DEADLINE" +%Y-%m-%dT%H:%M)
# Training has to stop with enough time left to restart serving (~7 min of
# weight load, AGENTS.md / compose.yaml) inside the window.
TRAIN_DEADLINE_ISO=$(date -d "@$((DEADLINE - 1200))" +%Y-%m-%dT%H:%M)
LOG=logs/nightly-$STAMP.log; mkdir -p logs adapters data/train
exec > >(tee -a "$LOG") 2>&1
log() { echo "[$(date +%H:%M:%S)] $*"; }
free_gb() { awk '/MemFree/ {print int($2/1048576)}' /proc/meminfo; }
PY=".venv/bin/python"

# The training set first, while the proposer still serves: it needs no GPU,
# and a missing review should cost nothing.
SELECTION=$(PYTHONPATH=. $PY -c 'from train.harvest import select; print(select()["selection"])')
REVIEW=train/reviews/$SELECTION.yaml
DATA=data/train/$STAMP.jsonl
# The signature is checked on its own, so that "not signed" (no training
# tonight, by design) cannot mask a real emit failure. Until 2026-10-17 any
# emit error was reported as a missing signature, and hid a path bug.
if ! [ -f "$REVIEW" ] || ! $PY -c "import yaml,sys; r=yaml.safe_load(open('$REVIEW')); sys.exit(0 if str(r.get('reviewer') or '').strip() else 1)"; then
  log "no signed review for selection $SELECTION: no training tonight"
  exit 0
fi
# A selection trains once. Scheduled nightly (PHASE-6.md), the same signed
# review would otherwise retrain the same adapter every night.
if grep -lq "\"selection\": \"$SELECTION\"" adapters/*/train_meta.json 2>/dev/null; then
  log "selection $SELECTION already trained ($(grep -l "\"selection\": \"$SELECTION\"" adapters/*/train_meta.json | head -1)): no training tonight"
  exit 0
fi
PYTHONPATH=. $PY -m train.harvest emit --review "$REVIEW" --out "$DATA" || { log "EMIT FAILED for a signed review: see above"; exit 1; }

restore() {
  log "starting proposer, then judge (compose order)"
  # Training just read ~62 GB of weights into the page cache, which CUDA
  # does not count as free. Both KV sizes are pinned in compose.yaml, so with
  # the cache gone each server starts the same way every time.
  python3 ops/evict_cache.py
  docker compose up -d vllm-proposer
  wait_healthy 8000 120 || { log "PROPOSER NOT HEALTHY after 20 min"; return 1; }
  docker compose up -d vllm-judge
  wait_healthy 8001 60 || { log "JUDGE NOT HEALTHY after 10 min"; return 1; }
  # docs/change-procedures.md section 5: every score records which judge lifetime
  # it came from.
  log "judge started $(docker inspect -f '{{.State.StartedAt}}' crucible-vllm-judge-1)"
}
wait_healthy() {
  for _ in $(seq 1 "$2"); do curl -sf -m5 "localhost:$1/v1/models" >/dev/null && return 0; sleep 10; done
  return 1
}
trap restore EXIT

docker compose stop vllm-judge vllm-proposer
# Stopping is not releasing (task 5.2), and released is not free while the
# page cache holds the weights the proposer just served from.
python3 ops/evict_cache.py
# 113 GB free trained; 93 GB was killed at load. 105 is the floor.
for _ in $(seq 1 120); do [ "$(free_gb)" -ge 105 ] && break; sleep 5; done
[ "$(free_gb)" -ge 105 ] || { log "only $(free_gb) GB free after stop: not training"; exit 1; }
log "free: $(free_gb) GB"

set +e
docker run --rm --name crucible-train --gpus all --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 \
  -v "$PWD":/work -v "$HOME/.cache/huggingface":/root/.cache/huggingface -e HF_TOKEN -e HF_HUB_OFFLINE=1 \
  crucible-train:26.08 python -m train.distil --data "$DATA" --out "adapters/$STAMP" --deadline "$TRAIN_DEADLINE_ISO"
TRAIN_EXIT=$?
# The container trains as root, so the adapter directory is root's; hand it to
# the operator so later steps (the capability gate's verdict) can write into it.
docker run --rm --entrypoint chown -v "$PWD/adapters":/a crucible-train:26.08 -R "$(id -u):$(id -g)" "/a/$STAMP"
set -e
log "training exit $TRAIN_EXIT"

trap - EXIT
restore

if [ "$TRAIN_EXIT" -ne 0 ] || ! grep -q '"complete": true' "adapters/$STAMP/train_meta.json" 2>/dev/null; then
  log "adapter $STAMP incomplete or failed: not loaded"
  exit 0
fi
# Under the stable name "distilled", which LiteLLM routes as
# proposer-distilled (litellm.config.yaml). The proposer was just restarted,
# so nothing is loaded under that name yet. Which adapter answers is the
# `root` of vLLM's /v1/models entry.
curl -sf -X POST localhost:8000/v1/load_lora_adapter -H 'content-type: application/json' \
  -d "{\"lora_name\":\"distilled\",\"lora_path\":\"/adapters/$STAMP\"}"
log "loaded adapters/$STAMP as distilled"

# Forgetting check (PHASE-5.md task 5.5): 5 passes of the fixed capability
# suite on the adapter, against the stored 20-pass stock reference. Recorded
# beside the adapter for the promotion gate (task 5.6); it does not block the
# A/B, since a rejected adapter can still be measured, just not promoted.
set +e
PYTHONPATH=. $PY -m harness.capability gate 5 > "adapters/$STAMP/capability.json"
GATE=$?
set -e
log "capability gate: $([ $GATE -eq 0 ] && echo passed || echo REJECTED) (adapters/$STAMP/capability.json)"

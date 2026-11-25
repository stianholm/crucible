#!/usr/bin/env bash
# PHASE-5.md's first round, end to end, started ahead of time so it begins the
# moment its two preconditions hold:
#   1. the 20-pass stock capability reference exists (task 5.5), and
#   2. the operator has signed the harvest review (task 5.1).
# It never signs anything; it only waits for the signature.
#
# Then: ops/nightly.sh (emit, train, restart, load adapter, capability gate),
# then 10 paired A/B generations at 16 pairs each (TODO.md decision 75) on an
# empty archive, parked afterwards as capability_case_ab1.
#
# Usage: ops/round1.sh <review.yaml>
set -euo pipefail
cd "$(dirname "$0")/.."
set -a; . ./.env; set +a
REVIEW=${1:?review file}
LOG=logs/round1.log; mkdir -p logs
exec > >(tee -a "$LOG") 2>&1
log() { echo "[$(date '+%F %T')] $*"; }
PY=".venv/bin/python"

log "waiting for bench/capability_reference.json and a signed $REVIEW"
until [ -f bench/capability_reference.json ] && \
      $PY -c "import yaml,sys; r=yaml.safe_load(open('$REVIEW')); sys.exit(0 if str(r.get('reviewer') or '').strip() else 1)"; do
  sleep 60
done
log "preconditions met; starting the nightly round"

STAMP=$(date +%Y%m%d)  # what ops/nightly.sh names tonight's adapter, taken just before it starts
ops/nightly.sh 06:00
grep -q '"complete": true' "adapters/$STAMP/train_meta.json" || { log "adapter incomplete: no A/B"; exit 1; }

COUNT=$(docker exec crucible-postgres-1 psql -U postgres -d crucible -tAc \
  "select count(*) from elite where solution_id='capability_case'")
[ "$COUNT" -eq 0 ] || { log "live archive not empty ($COUNT elites): refusing to start the A/B"; exit 1; }

log "A/B: 10 paired generations, 16 pairs each"
PYTHONPATH=. $PY - <<'EOF'
from harness.run_population import run_population
from solutions.capability_case.adapter import TASK_DESCRIPTION as DESC
print(run_population("capability_case", DESC, max_generations=10, max_tokens=8_000_000,
                     candidates_per_island=4, patience=10, max_wall_s=12 * 3600,
                     proposer_models=("proposer", "proposer-distilled")))
EOF

docker exec crucible-postgres-1 psql -U postgres -d crucible -c \
  "update elite set solution_id='capability_case_ab1' where solution_id='capability_case'"
for f in solutions/capability_case/results/GENERATION-[0-9][0-9][0-9].md; do
  mv "$f" "${f%.md}-ab1.md"
done
log "round 1 done; reports suffixed -ab1, archive parked as capability_case_ab1"

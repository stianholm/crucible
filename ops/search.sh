#!/usr/bin/env bash
# A stock-proposer population search from an empty archive, parked afterwards
# under a tag so the next run starts clean.
#
# Usage: ops/search.sh <tag> [generations] [solution_id] [git-rev]
#   solution defaults to capability_case; git-rev seeds the search from the
#   solution's candidate file at that revision instead of the incumbent.
#   reports become results/GENERATION-00N-<tag>.md, the archive <solution_id>_<tag>.
#   The task description is the solution's own (harness.onboarding.task_description).
set -euo pipefail
cd "$(dirname "$0")/.."
set -a; . ./.env; set +a
TAG=${1:?tag}; GENS=${2:-10}; SOL=${3:-capability_case}; SEEDREV=${4:-}
LOG=logs/search-$SOL-$TAG.log; mkdir -p logs
# The process group, for ops/stop.sh. The Python child's command line is
# ".venv/bin/python -" (code on stdin), so matching on its content cannot find
# it; on 2026-10-19 that left an "aborted" run going all night, sharing the
# live archive with its replacement (TODO.md decision 83).
echo "$(ps -o pgid= $$ | tr -d ' ')" > "logs/search-$SOL-$TAG.pgid"
exec > >(tee -a "$LOG") 2>&1
log() { echo "[$(date '+%F %T')] $*"; }

[ -f state/HALT ] && { log "halted: $(cat state/HALT); lift with ops/kill.py --clear"; exit 1; }
COUNT=$(docker exec crucible-postgres-1 psql -U postgres -d crucible -tAc \
  "select count(*) from elite where solution_id='$SOL'")
[ "$COUNT" -eq 0 ] || { log "live archive not empty ($COUNT elites): refusing to start"; exit 1; }
ls solutions/$SOL/results/GENERATION-[0-9][0-9][0-9].md >/dev/null 2>&1 && { log "unparked reports present: refusing to start"; exit 1; }

log "search $SOL $TAG: $GENS generations, 32 candidates each, stock proposer, lessons off"
PYTHONPATH=. GENS=$GENS SOL=$SOL SEEDREV=$SEEDREV .venv/bin/python - <<'EOF'
import os, subprocess
from harness.run_population import run_population
sol = os.environ["SOL"]
seed = None
if os.environ["SEEDREV"]:
    from pathlib import Path
    cand = next(Path(f"solutions/{sol}/candidate").iterdir()).name
    text = subprocess.run(["git", "show", f"{os.environ['SEEDREV']}:solutions/{sol}/candidate/{cand}"],
                          capture_output=True, text=True, check=True).stdout
    seed = text.split("EVOLVE-BLOCK-START")[1].split("EVOLVE-BLOCK-END")[0].strip("\n")
    print(f"seeded from {cand} at {os.environ['SEEDREV']}", flush=True)
if sol == "capability_case":  # its description lives in its adapter (decision 78)
    from solutions.capability_case.adapter import TASK_DESCRIPTION as desc
else:
    desc = None  # question one plus the standard (decision 80)
print(run_population(sol, desc, max_generations=int(os.environ["GENS"]),
                     max_tokens=20_000_000, max_wall_s=20 * 3600, patience=10,
                     candidates_per_island=8, seed_block=seed))
EOF

docker exec crucible-postgres-1 psql -U postgres -d crucible -c \
  "update elite set solution_id='${SOL}_$TAG' where solution_id='$SOL'"
for f in solutions/$SOL/results/GENERATION-[0-9][0-9][0-9].md; do mv "$f" "${f%.md}-$TAG.md"; done
log "search $SOL $TAG done; parked as ${SOL}_$TAG"

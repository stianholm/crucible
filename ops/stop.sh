#!/usr/bin/env bash
# Stop a run started by ops/search.sh, including its Python child, by killing
# the whole process group it recorded. Launch runs with setsid so each has its
# own group. Usage: ops/stop.sh <solution_id> <tag>
set -euo pipefail
cd "$(dirname "$0")/.."
F="logs/search-$1-$2.pgid"
PGID=$(cat "$F")
kill -TERM -- "-$PGID" 2>/dev/null && echo "stopped process group $PGID" || echo "process group $PGID not running"
sleep 2
if pgrep -g "$PGID" >/dev/null; then kill -KILL -- "-$PGID"; echo "killed stragglers in $PGID"; fi

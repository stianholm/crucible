#!/usr/bin/env bash
# PHASE-6.md's 23:00 retention sweep, run by crucible-retention.timer.
set -euo pipefail
cd "$(dirname "$0")/.."
set -a; . ./.env; set +a
mkdir -p logs
echo "[$(date '+%F %T')] retention sweep" >>logs/retention.log
PYTHONPATH=. .venv/bin/python -m harness.retention sweep >>logs/retention.log 2>&1

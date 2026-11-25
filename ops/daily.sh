#!/usr/bin/env bash
# The daily generation window (PHASE-6.md), run by crucible-day.timer at 06:30.
# Segments run until the deadline; harness/scheduler.py decides what runs.
# Usage: ops/daily.sh [HH:MM deadline, default 23:00]
set -euo pipefail
cd "$(dirname "$0")/.."
set -a; . ./.env; set +a
mkdir -p logs
exec >>"logs/day-$(date +%Y%m%d).log" 2>&1
echo "[$(date '+%F %T')] day window opens, deadline ${1:-23:00}"
PYTHONPATH=. .venv/bin/python -m harness.scheduler day --until "${1:-23:00}"
echo "[$(date '+%F %T')] day window closes"

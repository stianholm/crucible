#!/usr/bin/env bash
# Write the morning report (PHASE-6.md), run by crucible-morning.timer at 08:00.
set -euo pipefail
cd "$(dirname "$0")/.."
set -a; . ./.env; set +a
mkdir -p logs
PYTHONPATH=. .venv/bin/python -m harness.morning write >>logs/morning.log 2>&1

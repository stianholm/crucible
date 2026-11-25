#!/usr/bin/env bash
# PHASE-6.md's immediate alert tier, run by crucible-alerts.timer every 5 minutes.
set -euo pipefail
cd "$(dirname "$0")/.."
set -a; . ./.env; set +a
mkdir -p logs
PYTHONPATH=. .venv/bin/python -m harness.alerts check >>logs/alerts-check.log 2>&1

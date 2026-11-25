#!/usr/bin/env bash
# docs/backup.md: take a backup, or verify one by restoring it into a scratch
# database. Run from a terminal to include .env, encrypted (gpg asks for a
# passphrase).
#   ops/backup.sh [DEST]          default ~/crucible-backups, or $CRUCIBLE_BACKUP_DIR
#   ops/backup.sh verify DIR
set -euo pipefail
cd "$(dirname "$0")/.."
if [ "${1:-}" = verify ]; then shift; exec ops/crucible backup verify "$@"; fi
exec ops/crucible backup take "$@"

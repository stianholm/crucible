# Backup and recovery

**Status on 2026-11-05: built, verified, and copied off the machine.**
`ops/backup.sh` took the first backup (290 MB, 42 s) and a restore into a
scratch database matched its manifest exactly (decision 103). The backup with
`env.gpg` went to a release on a private GitHub repository, and a copy
downloaded back from GitHub passed the same check (decision 104).

Moved from `BACKUP.md`. That document's draft script used names that never
existed (`harness` for the database, `harness-artifacts` for the bucket); the
table below uses the real ones.

---

## What is backed up

Everything expensive is small, and everything large is cheap.

| Asset | Where | Backed up |
|---|---|---|
| Archive and event log | Postgres database `crucible` in container `crucible-postgres-1` | **Always**: `pg_dump -Fc`, 34 MB on 2026-11-05 |
| Task sets, including sealed held-out | `solutions/*/data/` | **Always**, copied with a sha256 per file; also in git |
| Candidate text | MinIO bucket `candidates` | **Always**: 8,782 objects, 44 MB on 2026-11-05 |
| LoRA adapters | `adapters/` | **Always**, with a sha256 per file (about 200 MB) |
| `.env` (secrets) | Repository root, not in git | **Only from a terminal**, encrypted with gpg (AES256, a passphrase you choose) |
| Signed harvest reviews, solution baselines, `CAPACITY.yaml`, code | Git | Git remote |
| Langfuse traces | ClickHouse, MinIO `langfuse` | Skipped: proposer contexts are already in `iteration.proposal` |
| Model weights, images | Hugging Face cache, Docker | Skipped: re-downloadable by digest |

**"In git" only counts once pushed.** Push to your remote after each working
session.

## Taking a backup

```bash
ops/backup.sh                    # to ~/crucible-backups/crucible-<stamp>/
ops/backup.sh /media/usb/backups # anywhere else
ops/backup.sh verify ~/crucible-backups/crucible-<stamp>   # the restore check
```

Run it from a terminal to include `.env`: gpg asks for a passphrase twice.
Keep the passphrase somewhere other than this machine. Unattended, `.env` is
skipped and the manifest says so. Every secret in it can be set fresh on a
rebuilt machine, but the Langfuse keys and the ntfy topic are easier restored
than re-issued.

The script (`harness/backup.py`):

1. Counts the rows of `iteration`, `elite`, `event` and `lesson` in a
   repeatable-read transaction and exports its snapshot.
2. Runs `pg_dump -Fc --snapshot=<it>` in the database container, so the dump
   holds exactly the counted rows, even while timer jobs write events.
3. Mirrors the `candidates` bucket, and copies `adapters/` and every
   `solutions/*/data/`.
4. Encrypts `.env` if a terminal is attached.
5. Writes `manifest.json`: time, git sha and whether the tree was dirty,
   container digest, row counts, the dump's sha256 and size, the candidate
   count, and a sha256 for every copied file.
6. Writes into `crucible-<stamp>.partial` and renames it only when complete,
   then records a `backup` event.

The manifest is what makes it a backup rather than a copy: a restore is
verified by comparing against it, not hoped at.

## Off the machine

A backup on the same NVMe dies with it, so each one goes to a **GitHub
release** on a private repository (decision 104). A release stores files
beside the repository, not in its history, so clones do not grow. One asset
may be up to 2 GB; a backup packs to about 160 MB. **Never attach a backup to
a public repository's release:** it holds the full database and `env.gpg`.
Use a separate private repository, or run the `gh` commands below with
`--repo <owner>/<private-repo>`.

```bash
cd ~/crucible-backups
tar -cf - crucible-<stamp> | zstd -T0 -19 -o crucible-<stamp>.tar.zst
gh release create backup-<date> crucible-<stamp>.tar.zst --title "Backup <date>" --notes "..."
```

Then download it back and check it, which proves the GitHub copy restores:

```bash
gh release download backup-<date> --dir /tmp/check
zstd -d < /tmp/check/crucible-<stamp>.tar.zst | tar -x -C /tmp/check
ops/backup.sh verify /tmp/check/crucible-<stamp>
```

`env.gpg` goes with it, encrypted; its passphrase never does.

## Cadence

| When | Why |
|---|---|
| Before any fitness, eval set, model, container or system update | The old scores become unreproducible afterwards |
| Monthly in steady state | Generations are incremental |

The morning report's `backup` signal fails when no backup is younger than 35
days (decision 103). Backups are never deleted automatically; each is about
300 MB.

## Restore

`ops/backup.sh verify DIR` restores the dump into a scratch database
(`crucible_restore_check`), counts the four tables, drops it, and compares the
counts, the dump's checksum, the candidate count and every file's checksum
against the manifest. It records a `restore_check` event either way. Run it
quarterly, and on any copy you move off the machine.

A real restore, onto a rebuilt machine:

1. Bring up the stack (`docker compose up -d postgres minio`).
2. `docker exec -i crucible-postgres-1 pg_restore -U postgres --no-owner -C -d postgres < crucible.dump`
   (`-C` creates the `crucible` database).
3. Upload `candidates/` back into the bucket, for example with the AWS CLI or
   `mc mirror` against `localhost:9002`.
4. Copy `adapters/` and `data/<solution>/` back to `adapters/` and
   `solutions/<solution>/data/`.
5. `gpg -d env.gpg > .env`.
6. Compare row counts against the manifest.

What a restore never recovers: Langfuse traces, non-elite candidate text older
than 30 days, and anything since the last backup.

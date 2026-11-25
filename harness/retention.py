"""The 23:00 retention sweep. See PHASE-6.md, "Steady-state housekeeping".

    crucible retention sweep [--dry-run]

| Data | Retention | Here |
|---|---|---|
| `iteration` rows, adapters, benchmark JSON | Forever | Not touched |
| Candidate artifacts in MinIO | Elites forever, the rest 30 days | "Kept" is wider than the elite table: anything ever claimed, any elite, any candidate an event names |
| Langfuse traces | 90 days | ClickHouse rows and the raw events Langfuse keeps in MinIO |
| ClickHouse's own system logs | 7 days | Not in PHASE-6.md's table: found 2026-10-25 holding 9 GB, against 180 MB of actual traces |
| Container images | Pinned plus one previous | Reported, not removed: an unattended sweep that deletes an image can delete the rollback target |

Measured 2026-10-25 before the first sweep: candidates 61 MB, Langfuse
events 4.3 GB, Langfuse tables 0.2 GB, ClickHouse system logs 9.1 GB.
"""

from __future__ import annotations

import argparse
import datetime
import os
import subprocess
from pathlib import Path

from harness import events

REPO_ROOT = Path(__file__).resolve().parent.parent
CANDIDATE_DAYS = 30
TRACE_DAYS = 90
SYSTEM_LOG_DAYS = 7
LANGFUSE_BUCKET, LANGFUSE_EVENTS = "langfuse", "events/"
LANGFUSE_TABLES = {"traces": "timestamp", "observations": "start_time", "scores": "timestamp",
                   "blob_storage_file_log": "created_at"}
SYSTEM_LOGS = ("asynchronous_insert_log", "asynchronous_metric_log", "background_schedule_pool_log", "error_log",
               "metric_log", "opentelemetry_span_log", "part_log", "processors_profile_log", "query_log",
               "text_log", "trace_log")
# Images in use by something other than a running container.
PINNED_IMAGES = ("crucible-train:26.08", "nvcr.io/nvidia/pytorch:26.08-py3", "harness/runner:1", "python:3.12-slim")


def clickhouse(q: str) -> str:
    return subprocess.run(["docker", "exec", "crucible-clickhouse-1", "clickhouse-client",
                           "--password", os.environ["CLICKHOUSE_PASSWORD"], "-q", q],
                          capture_output=True, text=True, check=True).stdout.strip()


def _expire_objects(bucket: str, prefix: str, days: int, keep: set[str], dry_run: bool) -> tuple[int, int]:
    from harness.storage import s3_client

    s3 = s3_client()
    cutoff = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=days)
    doomed, size = [], 0
    for page in s3.get_paginator("list_objects_v2").paginate(Bucket=bucket, Prefix=prefix):
        for o in page.get("Contents", []):
            if o["LastModified"] < cutoff and o["Key"] not in keep:
                doomed.append(o["Key"])
                size += o["Size"]
    if not dry_run:
        for i in range(0, len(doomed), 1000):
            s3.delete_objects(Bucket=bucket, Delete={"Objects": [{"Key": k} for k in doomed[i:i + 1000]], "Quiet": True})
    return len(doomed), size


def kept_candidates(conn) -> set[str]:
    rows = conn.execute(
        """select i.candidate_sha from elite e join iteration i on i.id = e.iteration_id
           union select candidate_sha from iteration where accepted
           union select detail->>'candidate_sha' from event where detail ? 'candidate_sha'"""
    ).fetchall()
    return {f"{r[0]}.py" for r in rows if r[0]}


def _langfuse_rows(dry_run: bool) -> dict[str, int]:
    out = {}
    for table, col in LANGFUSE_TABLES.items():
        where = f"{col} < now() - INTERVAL {TRACE_DAYS} DAY"
        n = int(clickhouse(f"select count() from default.{table} where {where}"))
        if n and not dry_run:
            clickhouse(f"DELETE FROM default.{table} WHERE {where}")
        out[table] = n
    return out


def _system_log_ttl(dry_run: bool) -> list[str]:
    """Idempotent: ClickHouse recreates a system log table when its version
    changes, dropping any TTL, so every sweep checks and sets it again."""
    present = set(clickhouse("select name from system.tables where database = 'system'").split())
    changed = []
    for t in SYSTEM_LOGS:
        if t not in present:
            continue
        ddl = clickhouse(f"select create_table_query from system.tables where database = 'system' and name = '{t}'")
        if f"toIntervalDay({SYSTEM_LOG_DAYS})" not in ddl:
            changed.append(t)
            if not dry_run:
                # Most date their rows event_date; opentelemetry_span_log uses finish_date.
                col = clickhouse(f"select name from system.columns where database = 'system' and table = '{t}' "
                                 "and name in ('event_date', 'finish_date') order by name limit 1")
                clickhouse(f"ALTER TABLE system.{t} MODIFY TTL {col} + INTERVAL {SYSTEM_LOG_DAYS} DAY")
    return changed


def _unreferenced_images() -> list[str]:
    used = set(subprocess.run(["docker", "ps", "-a", "--format", "{{.Image}}"],
                              capture_output=True, text=True).stdout.split())
    used_ids = {subprocess.run(["docker", "image", "inspect", "-f", "{{.Id}}", u], capture_output=True,
                               text=True).stdout.strip() for u in used | set(PINNED_IMAGES)}
    out = []
    for line in subprocess.run(["docker", "images", "--format", "{{.Repository}}:{{.Tag}} {{.ID}} {{.Size}}"],
                               capture_output=True, text=True).stdout.splitlines():
        name, short_id, size = line.split()
        if not any(i.startswith(f"sha256:{short_id}") for i in used_ids):
            out.append(f"{name} ({size})")
    return out


def sweep(conn, dry_run: bool = False) -> dict:
    n_cand, b_cand = _expire_objects("candidates", "", CANDIDATE_DAYS, kept_candidates(conn), dry_run)
    n_evt, b_evt = _expire_objects(LANGFUSE_BUCKET, LANGFUSE_EVENTS, TRACE_DAYS, set(), dry_run)
    result = {
        "dry_run": dry_run,
        "candidates_expired": n_cand, "candidate_mb": round(b_cand / 1e6, 1),
        "langfuse_events_expired": n_evt, "langfuse_event_mb": round(b_evt / 1e6, 1),
        "langfuse_rows_expired": _langfuse_rows(dry_run),
        "system_log_ttl_set": _system_log_ttl(dry_run),
        "images_unreferenced": _unreferenced_images(),
    }
    if not dry_run:
        events.record(conn, "retention", None, **result)
    return result


def main() -> int:
    from harness.persistence import connect

    ap = argparse.ArgumentParser(description="PHASE-6.md's retention sweep")
    ap.add_argument("cmd", choices=["sweep"])
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    with connect() as conn:
        for k, v in sweep(conn, a.dry_run).items():
            print(f"{k}: {v}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

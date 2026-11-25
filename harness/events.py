"""The event log behind the morning report. See PHASE-6.md.

One row per thing that happened and that a person may need to know about.
The report reads these instead of parsing generation reports, so anything
not recorded here is invisible to it by construction.
"""

from __future__ import annotations

import datetime

from psycopg.types.json import Jsonb

from harness.persistence import ensure_schema


# clock_timestamp(), not now(): now() is the transaction's start, and a caller
# that read before a 40-minute held-out check stamped its result 40 minutes
# early (found 2026-10-24, the first scheduled segment).
def record(conn, kind: str, solution_id: str | None = None, needs_ack: bool = False,
           at: datetime.datetime | None = None, **detail) -> int:
    ensure_schema(conn)
    row = conn.execute(
        "insert into event (at, kind, solution_id, detail, needs_ack) "
        "values (coalesce(%s, clock_timestamp()), %s, %s, %s, %s) returning id",
        (at, kind, solution_id, Jsonb(detail), needs_ack),
    ).fetchone()
    conn.commit()
    return row[0]


def since(conn, hours: float, kinds: tuple[str, ...] | None = None) -> list[dict]:
    ensure_schema(conn)
    q = "select id, at, kind, solution_id, detail, needs_ack, acked_at from event where at > now() - make_interval(secs => %s)"
    args: list = [hours * 3600]
    if kinds:
        q += " and kind = any(%s)"
        args.append(list(kinds))
    cols = ("id", "at", "kind", "solution_id", "detail", "needs_ack", "acked_at")
    return [dict(zip(cols, r)) for r in conn.execute(q + " order by at", args).fetchall()]


def latest(conn, kind: str, solution_id: str | None = None, n: int = 1) -> list[dict]:
    ensure_schema(conn)
    q = "select id, at, kind, solution_id, detail from event where kind = %s"
    args: list = [kind]
    if solution_id is not None:
        q += " and solution_id = %s"
        args.append(solution_id)
    rows = conn.execute(q + " order by at desc, id desc limit %s", args + [n]).fetchall()
    return [dict(zip(("id", "at", "kind", "solution_id", "detail"), r)) for r in rows]


def pending(conn) -> list[dict]:
    ensure_schema(conn)
    rows = conn.execute(
        "select id, at, kind, solution_id, detail from event where needs_ack and acked_at is null order by at"
    ).fetchall()
    return [dict(zip(("id", "at", "kind", "solution_id", "detail"), r)) for r in rows]


def ack(conn, event_id: int) -> bool:
    ensure_schema(conn)
    n = conn.execute("update event set acked_at = now() where id = %s and needs_ack and acked_at is null",
                     (event_id,)).rowcount
    conn.commit()
    return n == 1

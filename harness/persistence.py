"""Iteration persistence. See PHASE-2.md task 2.5.

Every iteration is written down, including the ones that never reached the
sandbox. The table is designed as the Phase 3 archive with columns
missing, so Phase 3 adds nullable columns rather than migrating data —
`descriptors`, `island_id` and `generation` all land here nullable, ready
for Phase 3 to populate.
"""

from __future__ import annotations

import json
import os
import uuid
from typing import Any

import psycopg

DDL = """
create table if not exists iteration (
  id            bigserial primary key,
  solution_id   text        not null,
  run_id        uuid        not null,
  n             int         not null,
  parent_sha    text,
  candidate_sha text,
  artifact_uri  text,
  status        text        not null,    -- parse_failed | inadmissible | scored
  valid         boolean,
  quality       real,
  cost_tokens   int,
  latency_s     real,
  scalar        real,
  accepted      boolean     not null default false,
  reason        text,
  detail        jsonb,
  prompt_tokens int,
  wall_s        real,
  descriptors   int[],      -- Phase 3, nullable until then
  island_id     int,        -- Phase 3, nullable until then
  generation    int,        -- Phase 3, nullable until then
  root_sha      text,       -- Phase 3, lineage ancestor (PHASE-3.md task 3.2)
  created_at    timestamptz not null default now()
);
create index if not exists iteration_run_idx on iteration (solution_id, run_id, n);

-- root_sha and the elite table below were both added to the live database
-- by hand, per PHASE-3.md task 3.2's own migration note, and never folded
-- back into this DDL — meaning a fresh database (a new dev environment,
-- CI, or a from-code restore) would be missing both and crash on the
-- first scored candidate. Found by the session-review workflow,
-- 2026-09-22; this file is now the single source of truth for both.
create table if not exists elite (
  solution_id  text        not null,
  island_id    int         not null,
  cell         int[]       not null,
  iteration_id bigint      not null references iteration(id),
  scalar       real        not null,
  updated_at   timestamptz not null default now(),
  primary key (solution_id, island_id, cell)
);

-- Phase 4 task 4.2, the lesson store. PHASE-4.md's own schema uses
-- pgvector's `vector(1024)` for real semantic embeddings - not available
-- here on two counts, found 2026-09-27 building task 4.1: the pgvector
-- extension was never installed (Phase 0 deployed plain postgres:17), and
-- the embedding model itself can't run alongside proposer+judge's 83%
-- memory reservation regardless (docs/platform.md). `vector` here is a TF-IDF
-- vector (harness/taxonomy.py's vectorizer, same one the failure taxonomy
-- uses), a real[] array rather than pgvector's type - no ivfflat index,
-- since brute-force cosine similarity over what will be at most hundreds
-- of lessons is trivially fast and pgvector isn't installed to index it
-- anyway.
create table if not exists lesson (
  id          bigserial primary key,
  solution_id text        not null,
  failure_id  text        not null,          -- taxonomy category id, e.g. F00
  text        text        not null,
  support     int         not null,          -- distinct failures it derives from
  followed    int         not null default 0,
  followed_ok int         not null default 0,
  vector      real[]      not null,
  created_gen int         not null,
  retired_gen int,
  created_at  timestamptz not null default now()
);
create index if not exists lesson_active_idx on lesson (solution_id) where retired_gen is null;

-- retired_reason added after the table above was first created and used
-- for real (2026-09-27) - an ALTER here, not folded into the CREATE TABLE,
-- so ensure_schema() fixes an already-existing lesson table the same way
-- it creates a fresh one. root_sha/elite already taught this lesson once
-- (see the comment above the elite table); applying it this time instead
-- of repeating the mistake.
alter table lesson add column if not exists retired_reason text;  -- set only by retire_manually(); NULL for automatic falsification retirement

-- Task 4.3's falsification loop, added 2026-09-28, same ALTER-not-CREATE
-- reasoning as retired_reason above (the iteration table is years of rows
-- older than this column).
--
-- failure_id is the task 4.1 taxonomy category a scored candidate's own
-- failure evidence was assigned to, NULL when it had no failures or when
-- the evidence matched no centroid (harness/taxonomy.py's novelty
-- threshold). PHASE-4.md task 4.6's repeat-failure-rate SQL already reads
-- this column; it simply never existed.
--
-- lessons_injected records which lessons reached this candidate's proposal
-- prompt. The lesson table's followed/followed_ok counters are what
-- retirement reads, but counters alone cannot answer "which lesson reached
-- which candidate" after the fact - a real limitation hit analysing the
-- 2026-09-28 verification run, where lessons were provably injected and
-- nothing recorded where.
alter table iteration add column if not exists failure_id text;
alter table iteration add column if not exists lessons_injected integer[];

-- failure_ids holds *every* taxonomy category this candidate's evidence fell
-- into; failure_id above keeps the dominant one, because PHASE-4.md task
-- 4.6's repeat-failure SQL reads a single value per row.
--
-- Added 2026-09-29 to make the falsification measurement symmetric. A treated
-- candidate was being scored against its full category set while the control
-- group could only be read from failure_id, the dominant one, so the same
-- recurrence counted as a failure for a lesson that received it and an
-- avoidance for a control candidate whose dominant category differed - which
-- biased every lesson toward retirement. Both sides were temporarily compared
-- on the dominant category instead, which is symmetric but discards the
-- secondary categories; this column lets both sides use the full set.
alter table iteration add column if not exists failure_ids text[];

-- proposal: the proposer's messages, response and reasoning for this row.
-- PHASE-5.md task 5.1 trains on context-to-proposal pairs. Until 2026-10-16
-- the only copy was Langfuse, which docs/backup.md does not back up; Postgres is.
alter table iteration add column if not exists proposal jsonb;

-- PHASE-5.md task 5.4's paired A/B. proposer_model is the LiteLLM role that
-- produced the row, with the adapter directory appended for the distilled
-- arm ("proposer-distilled@/adapters/20261018"), so a row says exactly which
-- weights proposed it. pair_id ties the two proposals made from one parent
-- in one generation; NULL outside an A/B.
alter table iteration add column if not exists proposer_model text;
alter table iteration add column if not exists pair_id integer;

-- class_skew: the fraction of its category's failure evidence that falls in
-- that category's dominant task class, so 1.0 means the failure only ever
-- occurs on one class of task and 0.5 means it occurs equally on both.
--
-- Added 2026-10-07 because the standing tier was promoting class-conditional
-- advice and injecting it universally. The tier takes the HIGHEST-SUPPORT
-- lessons, support follows the most common failure category, and on
-- capability_case 8 of 12 categories are more than 90% one-class - which is
-- structural, since the mechanical floor determines a task's class and a
-- candidate that over-rejects can only fail on floor-passing items. So the
-- tier reliably promoted a lesson that is right for one class and inverted for
-- the other: "When floor passes, prefer accept over reject" went into
-- must-reject prompts too, twice, derived independently both times.
alter table lesson add column if not exists class_skew real;

-- PHASE-6.md: everything the morning report says happened, as rows rather
-- than prose in generation reports. Held-out results (stamped with the eval
-- set's version), gate decisions, ladder steps, alerts, reports written and
-- reports read. needs_ack rows stay in "Wants from you" until acknowledged.
create table if not exists event (
    id          bigserial primary key,
    at          timestamptz not null default now(),
    kind        text not null,
    solution_id text,
    detail      jsonb not null default '{}',
    needs_ack   boolean not null default false,
    acked_at    timestamptz
);
create index if not exists event_kind_at on event (kind, at);
"""


def connect() -> psycopg.Connection:
    return psycopg.connect(
        host=os.environ.get("PGHOST", "localhost"),
        port=int(os.environ.get("PGPORT", "5432")),
        user=os.environ.get("PGUSER", "postgres"),
        password=os.environ["POSTGRES_PASSWORD"],
        dbname=os.environ.get("PGDATABASE", "crucible"),
    )


def ensure_schema(conn: psycopg.Connection, force: bool = False) -> None:
    """Idempotent per connection, not merely per statement.

    The DDL above is all `if not exists`, so running it repeatedly was
    harmless in its effect and expensive in its locking: `alter table
    iteration add column ...` takes an ACCESS EXCLUSIVE lock even when the
    column is already there, and a *waiting* exclusive lock queues every
    reader behind it. harness/lessons.py's record_usage() is called up to
    four times per candidate, so a 32-candidate generation ran this whole
    script 128 times inside one long transaction.

    Found 2026-09-29 the direct way: a read-only metrics query issued from a
    second process during a live ten-generation run blocked for 153 seconds
    on `Lock/relation` behind the run's open transaction, and had to be
    cancelled before the run's own next statement queued behind it.

    Tracked on the connection object rather than by id(), which is reusable
    after garbage collection. `force=True` re-runs it, for a caller that has
    genuinely changed the schema."""
    if not force and getattr(conn, "_crucible_schema_ready", False):
        return
    # End the caller's transaction first, so this connection holds no table
    # lock while it queues. The advisory lock alone was not enough: retention
    # and the morning report read `iteration` before recording an event, so
    # they waited for the advisory lock while holding the read lock the
    # holder's DDL needed. Same deadlock, two nights running (2026-10-26/27).
    conn.commit()
    with conn.cursor() as cur:
        # One process at a time. The 23:00 retention sweep and the alert
        # check both ran this script within 8 s of each other on 2026-10-25,
        # each holding a lock the other's DDL needed, and Postgres killed the
        # sweep as a deadlock. The advisory lock is released at commit.
        cur.execute("select pg_advisory_xact_lock(hashtext('crucible.ensure_schema'))")
        cur.execute(DDL)
    try:
        conn._crucible_schema_ready = True
    except AttributeError:  # a connection type that rejects attributes
        pass
    conn.commit()


class IterationWriter:
    """One instance per run. `record()` matches the shape hill_climb()
    needs — status plus whatever fitness/accept fields are available for
    that status."""

    def __init__(self, conn: psycopg.Connection, solution_id: str, run_id: uuid.UUID | None = None):
        self.conn = conn
        self.solution_id = solution_id
        self.run_id = run_id or uuid.uuid4()
        ensure_schema(conn)

    def record(
        self,
        n: int,
        status: str,
        *,
        parent_sha: str | None = None,
        candidate_sha: str | None = None,
        candidate_block: str | None = None,  # if given with candidate_sha, persisted to storage (see harness.storage)
        fitness: Any | None = None,  # harness.fitness.Fitness
        accepted: bool = False,
        reason: str | None = None,
        prompt_tokens: int | None = None,
        wall_s: float | None = None,
        cost_tokens_override: int | None = None,
    ) -> None:
        """cost_tokens_override exists because a multi-task evaluation has two
        different right answers for cost. Fitness.cost_tokens is the per-task
        mean, which is what Fitness.scalar has to penalise against its
        4,000-token anchor to stay comparable with hill-climb. This column is
        what run_population sums for the token budget, so it has to be the
        real total across every task. Storing the mean here would undercount
        a generation's spend by a factor of k, the same class of mistake as
        decision 30's token undercount."""
        quality = cost_tokens = latency_s = scalar = valid = detail = None
        if fitness is not None:
            valid = fitness.valid
            quality = fitness.quality
            cost_tokens = fitness.cost_tokens if cost_tokens_override is None else cost_tokens_override
            latency_s = fitness.latency_s
            scalar = fitness.scalar
            detail = json.dumps(fitness.detail)

        artifact_uri = None
        if candidate_sha is not None and candidate_block is not None:
            from harness.storage import put_candidate

            artifact_uri = put_candidate(candidate_sha, candidate_block)

        with self.conn.cursor() as cur:
            cur.execute(
                """
                insert into iteration
                  (solution_id, run_id, n, parent_sha, candidate_sha, artifact_uri, status,
                   valid, quality, cost_tokens, latency_s, scalar,
                   accepted, reason, detail, prompt_tokens, wall_s)
                values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    self.solution_id,
                    self.run_id,
                    n,
                    parent_sha,
                    candidate_sha,
                    artifact_uri,
                    status,
                    valid,
                    quality,
                    cost_tokens,
                    latency_s,
                    scalar,
                    accepted,
                    reason,
                    detail,
                    prompt_tokens,
                    wall_s,
                ),
            )
        self.conn.commit()

    def fetch_run(self) -> list[dict]:
        with self.conn.cursor() as cur:
            cur.execute(
                "select * from iteration where solution_id = %s and run_id = %s order by n",
                (self.solution_id, self.run_id),
            )
            cols = [d.name for d in cur.description]
            return [dict(zip(cols, row)) for row in cur.fetchall()]

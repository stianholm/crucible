"""PHASE-5.md task 5.1: turn the archive into a training set.

Each example is a context-to-proposal pair lifted from a real generation: the
exact messages the proposer was sent, and the response it gave, for a proposal
whose candidate claimed an archive cell. Rejection-sampling fine-tuning, so the
value is in which proposals are let through.

Two commands, with a human between them:

    python -m train.harvest review --sheet REVIEW.md
    python -m train.harvest emit --review train/reviews/<selection>.yaml --out data/train/<stamp>.jsonl

`review` runs every automatic filter and writes a sheet listing each surviving
candidate in full, plus a review file skeleton named after the selection's
hash. A person reads the sheet and records exclusions in that file. `emit`
refuses to write a training set unless a review file exists for exactly the
current selection, signed by a reviewer. The exclusion judgement itself is
never automated (task 5.1: "The human review step is not optional and does not
get automated").

Sources, where each field comes from, and why:
- **Which runs:** `train/harvest.yaml`, one fitness regime only.
- **Which proposals claimed a cell:** `iteration.accepted` from 2026-10-16,
  and the generation reports' "newly claimed elites" sections before that,
  each checked against the report's own claim count. `elite` cannot answer
  it: it keeps each cell's final occupant, not everything that ever claimed.
- **The proposer's context and response:** `iteration.proposal`, written by
  the harness from 2026-10-16. Older rows fall back to Langfuse, which LiteLLM
  writes every call to, joined by the sha of the candidate parsed from the
  response, which is how the candidate sha was computed in the first place.
  `backfill` copies those traces into `iteration.proposal`, because docs/backup.md
  backs up Postgres and not Langfuse.
"""

from __future__ import annotations

import argparse
import glob
import hashlib
import json
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import timedelta, timezone
from pathlib import Path

import yaml
from psycopg.types.json import Jsonb
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from harness.generation import sha
from harness.persistence import connect, ensure_schema
from harness.proposal import parse_candidate

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCES = REPO_ROOT / "train" / "harvest.yaml"
REVIEWS = REPO_ROOT / "train" / "reviews"

# Two candidates at or above this TF-IDF cosine similarity are one proposal
# for training purposes, and only the higher-scoring is kept. Task 5.1 asks for
# embedding distance; no embedding model fits beside proposer and judge on this
# machine (TODO.md decision 34), and TF-IDF is what the failure taxonomy
# already uses for the same job.
DEDUP_COSINE = 0.90

# At most this many examples per parent failure category. Task 5.1: "Sample
# across Phase 4's failure taxonomy, not by frequency."
PER_CATEGORY_CAP = 40

# A claim is only a training signal if the candidate was good, not merely
# first into an empty cell. Without a floor, 45 of the first selection's 239
# scored below 0.50 (lowest 0.25) against a median of 0.63, admitted because
# generation 0 and new descriptor regions let almost anything claim. Decided at
# the first human review, 2026-10-17 (TODO.md decision 74). Applied before
# dedup, so dedup chooses among candidates that pass.
MIN_SCALAR = 0.50

# Magnitude weight: 1 + (rotation improvement over the parent, clipped to
# [0, WEIGHT_CAP_DELTA]) / WEIGHT_CAP_DELTA, so weights run from 1 to 2 and one
# enormous win cannot dominate. The improvement is measured against a parent
# scored in an earlier generation on a different nine-task sample, so it is a
# noisy quantity; the cap and the floor of 1 keep that noise from mattering
# much.
WEIGHT_CAP_DELTA = 0.2

# Proposer calls start before a run's first iteration row is written, since
# rows are recorded after generation 0's proposals return.
TRACE_LEAD = timedelta(hours=2)

CLAIM_HEADER = re.compile(r"^### Island (\d+), cell \(([\d, ]+)\), scalar ([\d.]+)$")
CLAIM_LINE = re.compile(r"^parent `([0-9a-f]+)` -> candidate `([0-9a-f]+)`$")
CLAIM_COUNT = re.compile(r"^- Cells newly claimed this generation: (\d+)$")


def load_sources(path: Path = SOURCES) -> list[dict]:
    return yaml.safe_load(path.read_text())["sources"]


def claims_from_reports(pattern: str) -> list[str]:
    """Candidate shas listed as newly claimed, across one run's reports.

    Each report's listing is checked against its own count line, so a report
    format change fails loudly instead of silently dropping claims."""
    shas = []
    files = sorted(glob.glob(str(REPO_ROOT / pattern)))
    if not files:
        raise SystemExit(f"no reports match {pattern}")
    for f in files:
        lines = Path(f).read_text().splitlines()
        expected = next(int(m.group(1)) for l in lines if (m := CLAIM_COUNT.match(l)))
        found = [m.group(2) for l in lines if (m := CLAIM_LINE.match(l))]
        if len(found) != expected:
            raise SystemExit(f"{f}: lists {len(found)} claims, count line says {expected}")
        shas += found
    return shas


def claims_from_db(conn, run_id: str) -> list[str]:
    return [r[0] for r in conn.execute(
        "select candidate_sha from iteration where run_id = %s and accepted order by id", (run_id,))]


def iteration_rows(conn, run_id: str) -> dict[str, dict]:
    """Scored rows of one run, keyed by candidate sha (first occurrence)."""
    rows = {}
    for r in conn.execute(
        """select id, candidate_sha, parent_sha, generation, island_id, scalar, quality,
                  failure_id, lessons_injected, created_at, proposal
           from iteration where run_id = %s and status = 'scored' order by id""",
        (run_id,),
    ):
        d = dict(zip(["id", "candidate_sha", "parent_sha", "generation", "island_id", "scalar",
                      "quality", "failure_id", "lessons_injected", "created_at", "proposal"], r))
        # UTC and naive, to compare with Langfuse's start_time, which is UTC;
        # psycopg returns the session's zone, which on this box is local time.
        d["created_at"] = d["created_at"].astimezone(timezone.utc).replace(tzinfo=None)
        rows.setdefault(d["candidate_sha"], d)
    return rows


def proposer_traces(t0, t1) -> dict[str, list[dict]]:
    """Proposer calls in [t0, t1] from Langfuse, keyed by parsed-candidate sha."""
    q = (
        "select id, toString(start_time) as start_time, input, output from observations "
        f"where start_time >= '{t0:%Y-%m-%d %H:%M:%S}' and start_time <= '{t1:%Y-%m-%d %H:%M:%S}' "
        "and position(input, '## What this component must do') > 0 "
        "order by start_time, id format JSONEachRow"
    )
    out = subprocess.run(
        ["docker", "exec", "crucible-clickhouse-1", "clickhouse-client",
         "--password", os.environ["CLICKHOUSE_PASSWORD"], "-q", q],
        capture_output=True, text=True, check=True,
    ).stdout
    traces = defaultdict(list)
    for line in out.splitlines():
        o = json.loads(line)
        try:
            msg = json.loads(o["output"])
        except json.JSONDecodeError:
            continue  # a failed call: the output is an error string
        content = (msg or {}).get("content") if isinstance(msg, dict) else None
        cand = parse_candidate(content) if content else None
        if cand is None:
            continue
        traces[sha(cand)].append({
            "trace_id": o["id"],
            "start_time": o["start_time"],
            "messages": json.loads(o["input"])["messages"],
            "content": content,
            "reasoning": msg.get("reasoning_content") or "",
            "candidate": cand,
        })
    return traces


def _traces_for(rows: dict[str, dict]) -> dict[str, list[dict]]:
    times = [r["created_at"] for r in rows.values()]
    return proposer_traces(min(times) - TRACE_LEAD, max(times))


def _trace_for(traces: dict[str, list[dict]], row: dict) -> dict | None:
    """The call nearest before the row was written: the one that produced it."""
    stamp = f"{row['created_at']:%Y-%m-%d %H:%M:%S.%f}"
    hits = [t for t in traces.get(row["candidate_sha"], []) if t["start_time"] <= stamp]
    return hits[-1] if hits else None


def _from_proposal(p: dict) -> dict:
    return {"trace_id": p.get("trace_id"), "messages": p["messages"], "content": p["content"],
            "reasoning": p.get("reasoning", ""), "candidate": parse_candidate(p["content"])}


def backfill(conn, sources: list[dict]) -> Counter:
    """Copy Langfuse proposer traces into iteration.proposal for every scored
    row of the listed runs that lacks one. Idempotent."""
    counts = Counter()
    for src in sources:
        rows = iteration_rows(conn, src["run_id"])
        missing = [r for r in rows.values() if not r["proposal"]]
        if not missing:
            continue
        traces = _traces_for(rows)
        for row in missing:
            t = _trace_for(traces, row)
            if t is None:
                counts["no trace"] += 1
                continue
            conn.execute("update iteration set proposal = %s where id = %s", (Jsonb({
                "messages": t["messages"], "content": t["content"], "reasoning": t["reasoning"],
                "trace_id": t["trace_id"], "backfilled_from": "langfuse",
            }), row["id"]))
            counts["backfilled"] += 1
        conn.commit()
    return counts


def collect(conn, sources: list[dict]) -> tuple[list[dict], Counter]:
    """Every claimed proposal joined to its context, before dedup and balance."""
    counts = Counter()
    examples = []
    for src in sources:
        rows = iteration_rows(conn, src["run_id"])
        claimed = claims_from_reports(src["reports"]) if src.get("reports") else claims_from_db(conn, src["run_id"])
        counts["claims"] += len(claimed)
        traces = None
        for cand_sha in dict.fromkeys(claimed):  # a cell re-claimed by the same text is one example
            row = rows.get(cand_sha)
            if row is None:
                counts["dropped: claim with no scored row"] += 1
                continue
            if row["proposal"]:
                counts["context from postgres"] += 1
                trace = _from_proposal(row["proposal"])
            else:
                traces = traces if traces is not None else _traces_for(rows)
                trace = _trace_for(traces, row)
                if trace is None:
                    counts["dropped: no proposer trace"] += 1
                    continue
                counts["context from langfuse"] += 1
            parent = rows.get(row["parent_sha"])
            delta = None if parent is None else row["scalar"] - parent["scalar"]
            examples.append({
                "candidate_sha": cand_sha,
                "source": src["label"],
                "solution_id": src["solution_id"],
                "run_id": src["run_id"],
                "iteration_id": row["id"],
                "generation": row["generation"],
                "parent_sha": row["parent_sha"],
                "category": (parent or {}).get("failure_id") or ("seed" if parent is None else "none"),
                "scalar": row["scalar"],
                "parent_scalar": None if parent is None else parent["scalar"],
                "delta": delta,
                "weight": 1 + min(max(delta or 0.0, 0.0), WEIGHT_CAP_DELTA) / WEIGHT_CAP_DELTA,
                "lessons_injected": row["lessons_injected"] or [],
                "trace_id": trace["trace_id"],
                "messages": trace["messages"],
                "response": {"content": trace["content"], "reasoning": trace["reasoning"]},
                "candidate": trace["candidate"],
            })
    counts["joined"] = len(examples)
    return examples, counts


def dedup(examples: list[dict]) -> tuple[list[dict], list[tuple[str, str, float]]]:
    """Greedy, highest scalar first: keep a candidate unless it is a near copy
    of one already kept. Returns the kept examples and (dropped, kept_instead, cos)."""
    order = sorted(examples, key=lambda e: (-e["scalar"], e["iteration_id"]))
    if len(order) < 2:
        return order, []
    sims = cosine_similarity(TfidfVectorizer().fit_transform([e["candidate"] for e in order]))
    kept, dropped = [], []
    for i, e in enumerate(order):
        near = next(((j, sims[i, j]) for j in kept if sims[i, j] >= DEDUP_COSINE), None)
        if near:
            dropped.append((e["candidate_sha"], order[near[0]]["candidate_sha"], round(float(near[1]), 3)))
        else:
            kept.append(i)
    return [order[i] for i in kept], dropped


def balance(examples: list[dict]) -> tuple[list[dict], Counter]:
    """Cap each parent failure category, keeping its highest-scoring examples."""
    by_cat = defaultdict(list)
    for e in sorted(examples, key=lambda e: (-e["scalar"], e["iteration_id"])):
        by_cat[e["category"]].append(e)
    kept, cut = [], Counter()
    for cat, es in by_cat.items():
        kept += es[:PER_CATEGORY_CAP]
        if len(es) > PER_CATEGORY_CAP:
            cut[cat] = len(es) - PER_CATEGORY_CAP
    return sorted(kept, key=lambda e: (e["source"], e["iteration_id"])), cut


def select(conn=None) -> dict:
    """All automatic filters, deterministically. The selection hash names it."""
    own = conn is None
    conn = conn or connect()
    try:
        sources = load_sources()
        examples, counts = collect(conn, sources)
    finally:
        if own:
            conn.close()
    examples = [e for e in examples if e["scalar"] >= MIN_SCALAR]
    counts["after scalar floor"] = len(examples)
    deduped, dups = dedup(examples)
    counts["after dedup"] = len(deduped)
    balanced, cut = balance(deduped)
    counts["after category balance"] = len(balanced)
    digest = hashlib.sha256("\n".join(e["candidate_sha"] for e in balanced).encode()).hexdigest()[:16]
    return {
        "selection": digest,
        "examples": balanced,
        "counts": dict(counts),
        "dedup_dropped": dups,
        "category_cut": dict(cut),
        "categories": dict(Counter(e["category"] for e in balanced)),
        "params": {"MIN_SCALAR": MIN_SCALAR, "DEDUP_COSINE": DEDUP_COSINE, "PER_CATEGORY_CAP": PER_CATEGORY_CAP,
                   "WEIGHT_CAP_DELTA": WEIGHT_CAP_DELTA},
        "sources": [s["label"] for s in sources],
    }


def write_review(sel: dict, sheet: Path) -> Path:
    """The sheet a person reads, and the file they record exclusions in."""
    lines = [
        f"# Harvest review, selection `{sel['selection']}`", "",
        "Read every candidate below. Exclude any that won by exploiting the fitness",
        "function rather than by doing the task better: instructions that game the",
        "judge, dictate the output so a check passes vacuously, or encode the rotation",
        "set's quirks rather than the rule. PHASE-5.md task 5.1 explains why this",
        "matters more here than anywhere else in the project.", "",
        "| Stage | Count |", "|---|---|",
        *[f"| {k} | {v} |" for k, v in sel["counts"].items()], "",
        "| Parent failure category | Examples |", "|---|---|",
        *[f"| {k} | {v} |" for k, v in sorted(sel["categories"].items(), key=lambda kv: -kv[1])], "",
    ]
    for i, e in enumerate(sel["examples"], 1):
        delta = "n/a (seed parent)" if e["delta"] is None else f"{e['delta']:+.4f}"
        lines += [
            f"## {i}. `{e['candidate_sha']}`, {e['source']} generation {e['generation']}", "",
            f"- Rotation scalar {e['scalar']:.4f}, over parent {delta}, weight {e['weight']:.2f}",
            f"- Parent `{e['parent_sha']}`, category `{e['category']}`, lessons {e['lessons_injected'] or 'none'}",
            "", "```", e["candidate"], "```", "",
        ]
    sheet.write_text("\n".join(lines))

    REVIEWS.mkdir(parents=True, exist_ok=True)
    review = REVIEWS / f"{sel['selection']}.yaml"
    if not review.exists():
        review.write_text(
            f"# Review of harvest selection {sel['selection']} ({len(sel['examples'])} candidates).\n"
            f"# Sheet: {sheet}\n"
            "# Fill in reviewer and date, and list every exclusion with its reason.\n"
            "# emit refuses this file while reviewer is empty.\n"
            f"selection: {sel['selection']}\n"
            "reviewer: \"\"\n"
            "date: \"\"\n"
            "excluded: {}\n"
            "#  <candidate_sha>: <why it exploits the fitness function>\n"
        )
    return review


def emit(sel: dict, review_path: Path, out: Path) -> dict:
    review = yaml.safe_load(review_path.read_text())
    if review.get("selection") != sel["selection"]:
        raise SystemExit(f"{review_path} reviews selection {review.get('selection')}, "
                         f"but the archive now selects {sel['selection']}. Run `review` again.")
    if not str(review.get("reviewer") or "").strip():
        raise SystemExit(f"{review_path} has no reviewer: the human review step has not happened.")
    excluded = review.get("excluded") or {}
    unknown = set(excluded) - {e["candidate_sha"] for e in sel["examples"]}
    if unknown:
        raise SystemExit(f"{review_path} excludes candidates not in the selection: {sorted(unknown)}")

    kept = [e for e in sel["examples"] if e["candidate_sha"] not in excluded]
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w") as f:
        for e in kept:
            f.write(json.dumps({
                # The proposer's own messages, then its response. `thinking` is
                # gpt-oss's analysis channel, kept so task 5.3 can decide whether
                # to train on it rather than having it lost here.
                "messages": e["messages"] + [{"role": "assistant", "content": e["response"]["content"],
                                              "thinking": e["response"]["reasoning"]}],
                "weight": e["weight"],
                "meta": {k: e[k] for k in ("candidate_sha", "source", "solution_id", "run_id", "iteration_id",
                                           "generation", "parent_sha", "category", "scalar", "parent_scalar",
                                           "delta", "lessons_injected", "trace_id")},
            }, default=str) + "\n")
    manifest = {
        "selection": sel["selection"], "review": str(review_path.resolve().relative_to(REPO_ROOT)) if review_path.resolve().is_relative_to(REPO_ROOT) else str(review_path),
        "reviewer": review["reviewer"], "excluded": excluded, "examples": len(kept),
        "counts": sel["counts"] | {"after human review": len(kept)}, "categories": sel["categories"],
        "category_cut": sel["category_cut"], "dedup_dropped": sel["dedup_dropped"],
        "params": sel["params"], "sources": sel["sources"],
    }
    out.with_suffix(".manifest.json").write_text(json.dumps(manifest, indent=1))
    return manifest


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m train.harvest")
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("review", help="run the automatic filters and write the review sheet")
    r.add_argument("--sheet", type=Path, default=Path("REVIEW.md"))
    e = sub.add_parser("emit", help="write the training set, given a completed review")
    e.add_argument("--review", type=Path, required=True)
    e.add_argument("--out", type=Path, required=True)
    sub.add_parser("backfill", help="copy Langfuse proposer traces into iteration.proposal")
    args = ap.parse_args(argv)

    if args.cmd == "backfill":
        with connect() as conn:
            ensure_schema(conn)  # adds iteration.proposal on a database that predates it
            print(dict(backfill(conn, load_sources())))
        return 0

    sel = select()
    if args.cmd == "review":
        review = write_review(sel, args.sheet)
        print(json.dumps(sel["counts"], indent=1))
        print(f"selection {sel['selection']}: {len(sel['examples'])} candidates")
        print(f"sheet {args.sheet}, review file {review}")
    else:
        m = emit(sel, args.review, args.out)
        print(json.dumps(m["counts"], indent=1))
        print(f"wrote {m['examples']} examples to {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

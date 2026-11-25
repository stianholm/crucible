"""The morning report. See PHASE-6.md, "The morning report".

Two rules shape it. It leads with what would make you stop the system, before
anything reassuring. And it stays readable in five minutes. The verdict line
is HEALTHY, DEGRADED with the failing signals named, or HALTED with the reason.

Two things keep it from becoming wallpaper. An unread report is itself a
would-stop signal the next morning: reading is recorded (`read`), so a
fortnight of unread reports cannot pass as oversight. And the weekly elite read,
the one check PHASE-6.md says can never be automated, appears under "Wants from
you" whenever it is due.

    crucible morning write            write today's report
    crucible morning read             mark the latest report read
    crucible morning elite-read NOTE  record the weekly elite read
    crucible morning ack ID           acknowledge an event

collect() reads the system; render() is a pure function of what it returns.
"""

from __future__ import annotations

import argparse
import datetime
import json
import random
import shutil
import statistics
import urllib.request
from dataclasses import dataclass
from pathlib import Path

import yaml

from harness import events, ladder
from harness.halt import halted

REPO_ROOT = Path(__file__).resolve().parent.parent
REPORT_DIR = REPO_ROOT / "reports" / "morning"
SCHEDULE = REPO_ROOT / "schedule.yaml"
# Thresholds. Each is a would-stop line; changing one is a gate change, so
# record it in docs/decisions.md with a date and a reason (PHASE-6.md, "The gate loosens").
HELD_OUT_DROP = 0.03     # the capability gate's grey zone (decision 77)
PLATEAU_GENS = 12        # PHASE-6.md's opening value
FAIL_RATE = 0.10
DISK_PCT = 85            # also the immediate-alert line
CAPABILITY_REGRESSION = 0.05
DIVERSITY_DROP = 0.10    # week on week
DIVERSITY_SAMPLE = 300   # proposals per solution per week, for a bounded pairwise cost
BACKUP_DAYS = 35         # docs/backup.md: monthly, with a few days' slack (decision 103)


@dataclass
class Signal:
    name: str
    value: str
    ok: bool


# ---------------------------------------------------------------- rendering

def verdict(halt: str | None, signals: list[Signal]) -> tuple[str, str]:
    if halt:
        return "HALTED", halt
    bad = [s.name for s in signals if not s.ok]
    return ("DEGRADED", ", ".join(bad)) if bad else ("HEALTHY", "")


def render(f: dict) -> str:
    word, reason = verdict(f["halt"], f["signals"])
    head = f"**{word}**" + (f": {reason}" if reason else "")
    out = [f"# Harness, {f['date']}", "",
           f"{head} · {f['generations']} generation{'' if f['generations'] == 1 else 's'} · {len(f['pending'])} pending acknowledgements", "",
           "## Would-stop signals", "", "| Signal | | |", "|---|---|---|"]
    out += [f"| {s.name} | {s.value} | {'ok' if s.ok else '**CHECK**'} |" for s in f["signals"]]
    out += ["", "## What changed", ""]
    out += [f"- {c}" for c in f["changed"]] or ["- nothing"]
    out += ["", "## Numbers", "", "| | |", "|---|---|"]
    out += [f"| {k} | {v} |" for k, v in f["numbers"]]
    out += ["", "## Solutions", "", "| Solution | State | Held-out | Eval set |", "|---|---|---|---|"]
    out += [f"| {s['solution_id']} | {s['state']} | {s['held_out']} | {s['eval_version']} |" for s in f["solutions"]]
    out += ["", "## Wants from you", ""]
    out += [f"- {w}" for w in f["wants"]] or ["- nothing"]
    out += ["", "Read it? `crucible morning read`. An unread report is tomorrow's first warning.", ""]
    return "\n".join(out)


# ---------------------------------------------------------------- collection

def _healthy(port: int) -> bool:
    try:
        with urllib.request.urlopen(f"http://localhost:{port}/v1/models", timeout=5):
            return True
    except OSError:
        return False


def _fmt_tokens(n: float) -> str:
    return f"{n / 1e6:.1f}M" if n >= 1e5 else f"{n:,.0f}"


def _attention(conn) -> Signal:
    prev = events.latest(conn, "report")
    if not prev:
        return Signal("attention", "first report", True)
    read = events.latest(conn, "report_read")
    ok = bool(read) and read[0]["at"] >= prev[0]["at"]
    return Signal("attention", "last report read" if ok else f"last report ({prev[0]['at']:%a %d %b}) NOT read", ok)


def _held_out(conn, sol: str) -> tuple[Signal | None, str, str]:
    """Latest held-out against the best earlier one on the same eval set."""
    rows = events.latest(conn, "held_out", sol, n=200)
    if not rows:
        return None, "not recorded", "-"
    last = rows[0]["detail"]
    q, v = last["quality"], last["eval_version"]
    same = [r["detail"]["quality"] for r in rows[1:] if r["detail"]["eval_version"] == v]
    if rows[1:] and not same:
        return Signal(f"held-out {sol}", f"{q:.3f}; eval set changed, not compared", True), f"{q:.3f}", v
    if not same:
        return Signal(f"held-out {sol}", f"{q:.3f}, first on this eval set", True), f"{q:.3f}", v
    best = max(same)
    return Signal(f"held-out {sol}", f"{q:.3f}, best {best:.3f}", q >= best - HELD_OUT_DROP), f"{q:.3f}", v


def activity(gens: int, idle_at: datetime.datetime | None, all_dormant: bool) -> Signal:
    """A day the scheduler checked and correctly ran nothing, every solution
    dormant, is a scheduled day (decision 100). It counts only with the
    scheduler's own idle record, so a day timer that never fired still fails."""
    if gens:
        return Signal("activity", f"{gens} generation{'' if gens == 1 else 's'} in 24 h", True)
    if idle_at and all_dormant:
        return Signal("activity", f"idle by design: every solution dormant (checked {idle_at.astimezone():%H:%M})", True)
    return Signal("activity", "idle: no generations and no scheduler check in 24 h"
                  if not idle_at else "idle: no generations, but a solution has headroom", False)


def backup(last: datetime.datetime | None, now: datetime.datetime) -> Signal:
    """docs/backup.md: days since the last backup is a would-stop signal."""
    if not last:
        return Signal("backup", "no backup taken (`ops/backup.sh`)", False)
    days = (now - last).days
    return Signal("backup", f"last {last.astimezone():%d %b}, {days} day{'' if days == 1 else 's'} ago",
                  days <= BACKUP_DAYS)


def _plateau(c) -> Signal:
    """PHASE-6.md: the ladder reaching step 3 is a morning-report item."""
    st = c.state
    where = f"step {st.step} ({ladder.STEPS[st.step]})" if st.step else "climbing"
    return Signal(f"plateau {c.solution_id}", f"{where}, {st.since} generations without a held-out gain", st.step < 3)


def _diversity(conn, sol: str) -> Signal | None:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_distances

    rows = conn.execute(
        """select created_at > now() - interval '7 days', proposal->>'content' from iteration
           where solution_id = %s and created_at > now() - interval '14 days'
             and proposal->>'content' is not null and coalesce(proposer_model, 'proposer') = 'proposer'""",
        (sol,),
    ).fetchall()
    weeks = {True: [t for w, t in rows if w], False: [t for w, t in rows if not w]}
    if min(len(weeks[True]), len(weeks[False])) < 8:
        return None
    rng = random.Random(0)
    d = {}
    for w, texts in weeks.items():
        texts = rng.sample(texts, min(DIVERSITY_SAMPLE, len(texts)))
        m = cosine_distances(TfidfVectorizer().fit_transform(texts))
        n = m.shape[0]
        d[w] = float(m.sum() / (n * (n - 1)))
    change = d[True] / d[False] - 1
    return Signal(f"diversity {sol}", f"{change:+.0%} week on week", change >= -DIVERSITY_DROP)


def _capability_signal(adapter: Path) -> Signal:
    c = json.loads((adapter / "capability.json").read_text())
    reg = c["regression"]
    return Signal("capability", f"{-reg:+.1%} against stock (adapter {adapter.name})",
                  c["passes"] and reg <= CAPABILITY_REGRESSION)


JOBS = ("crucible-day", "crucible-nightly", "crucible-retention", "crucible-alerts", "crucible-morning")


def failed_jobs(results: dict[str, str]) -> list[str]:
    """Pure: units whose last run did not succeed. systemd reports Result
    'success' after a clean run and keeps a failure's result until the next
    run, so a job that failed overnight is still visible at 08:00."""
    return [unit for unit, result in results.items() if result not in ("success", "")]


def _jobs() -> Signal:
    """Added 2026-10-26: the 23:00 retention sweep failed the night before
    (a schema deadlock) and nothing said so."""
    import subprocess

    results = {}
    for unit in JOBS:
        out = subprocess.run(["systemctl", "--user", "show", f"{unit}.service", "-p", "Result", "--value"],
                             capture_output=True, text=True)
        results[unit] = out.stdout.strip() if out.returncode == 0 else "unknown"
    bad = failed_jobs(results)
    return Signal("jobs", f"last run failed: {', '.join(bad)}" if bad else f"all {len(JOBS)} timer jobs succeeded",
                  not bad)


def _gate(conn) -> Signal:
    rows = events.latest(conn, "gate", n=7)
    if not rows:
        return Signal("gate", "no gate decisions yet", True)
    rejected = [r["detail"].get("decision") == "rejected" for r in rows]
    three = len(rejected) >= 3 and all(rejected[:3])
    return Signal("gate", f"{sum(rejected)} rejection{'' if sum(rejected) == 1 else 's'} in the last {len(rows)}"
                  + ("; last three all rejected" if three else ""), not three)


def _disk(conn) -> tuple[Signal, float]:
    u = shutil.disk_usage("/")
    pct = 100 * u.used / u.total
    old = conn.execute(
        "select detail->>'pct' from event where kind = 'disk' and at > now() - interval '7 days' order by at limit 1"
    ).fetchone()
    trend = f", {round(pct - float(old[0]), 1) + 0.0:+.1f} pts over 7 days" if old else ", no 7-day history yet"
    return Signal("disk", f"{pct:.0f}% used{trend}", pct < DISK_PCT), pct


def _generation_walls(conn, days_from: int, days_to: int) -> list[float]:
    """Seconds between consecutive generations of the same run. A generation
    writes its rows in one burst at its end, so the gap between bursts is the
    generation's wall clock (the first generation of a run has no gap)."""
    rows = conn.execute(
        """select run_id, generation, max(created_at) from iteration
           where created_at > now() - make_interval(days => %s) and created_at <= now() - make_interval(days => %s)
             and generation is not null
           group by 1, 2 order by 1, 2""",
        (days_from, days_to),
    ).fetchall()
    walls = []
    for (r1, g1, t1), (r2, g2, t2) in zip(rows, rows[1:]):
        if r1 == r2 and g2 == g1 + 1:
            walls.append((t2 - t1).total_seconds())
    return walls


def _describe(e: dict) -> str:
    """One short clause per event, for "What changed"."""
    d, k = e["detail"], e["kind"]
    if k == "held_out":
        return f"{d['quality']:.3f} held-out, candidate {d['candidate_sha'][:8]}"
    if k == "ladder":
        return f"step {d['step']}, {d['action']}" + (f" ({d['reason']})" if d.get("reason") else "")
    if k == "segment":
        return f"{d['generations']} generations at temperature {d['temperature']}, {' and '.join(d['proposer_models'])}"
    if k == "gate":
        return f"adapter {d.get('adapter')} {d.get('decision')}" + (f", failed {', '.join(d['failed'])}" if d.get("failed") else "")
    return ", ".join(f"{key} {v}" for key, v in d.items() if key not in ("eval_version", "backfilled"))


def collect(conn, today: datetime.date | None = None) -> dict:
    today = today or datetime.date.today()
    halt = halted()
    cap = (yaml.safe_load(SCHEDULE.read_text()) or {}).get("daily_token_cap") if SCHEDULE.exists() else None

    tokens, gens, rows, failed = conn.execute(
        """select coalesce(sum(coalesce(prompt_tokens, 0) + coalesce(cost_tokens, 0)), 0),
                  count(distinct (run_id, generation)), count(*), count(*) filter (where status <> 'scored')
           from iteration where created_at > now() - interval '24 hours'"""
    ).fetchone()
    active = [r[0] for r in conn.execute(
        "select distinct solution_id from iteration where created_at > now() - interval '24 hours' order by 1"
    ).fetchall()]
    from harness.scheduler import contenders

    roster = contenders(conn)

    proposer, judge = _healthy(8000), _healthy(8001)
    signals = [
        _attention(conn),
        _jobs(),
        Signal("models", f"proposer {'up' if proposer else 'DOWN'}, judge {'up' if judge else 'DOWN'}", proposer and judge),
        activity(gens, (idle[-1]["at"] if (idle := events.since(conn, 24, ("idle",))) else None),
                 bool(roster) and all(c.state.dormant for c in roster)),
        Signal("budget", f"{tokens / cap:.0%} of the daily token cap ({_fmt_tokens(tokens)} of {_fmt_tokens(cap)})"
               if cap else "no daily token cap set in schedule.yaml", bool(cap) and tokens < cap),
        Signal("failures", f"{failed} of {rows} rows not scored ({failed / rows:.1%})" if rows else "no rows in 24 h",
               not rows or failed / rows <= FAIL_RATE),
    ]
    signals += [_plateau(c) for c in roster if not c.state.dormant]
    solutions = []
    for c in roster:
        sig, q, v = _held_out(conn, c.solution_id)
        if sig:
            signals.append(sig)
        st = c.state
        state = "dormant" if st.dormant else (f"ladder step {st.step}" if st.step else "climbing")
        solutions.append({"solution_id": c.solution_id, "state": state, "held_out": q, "eval_version": st.eval_version})
    signals.append(_gate(conn))
    adapters = sorted(p for p in (REPO_ROOT / "adapters").glob("[0-9]" * 8) if (p / "capability.json").exists())
    signals.append(_capability_signal(adapters[-1]) if adapters else Signal("capability", "no adapter yet", True))
    disk, pct = _disk(conn)
    signals.append(disk)
    last = events.latest(conn, "backup")
    signals.append(backup(last[0]["at"] if last else None, datetime.datetime.now(datetime.timezone.utc)))
    signals += [s for s in (_diversity(conn, sol) for sol in active) if s]

    changed = []
    for e in events.since(conn, 24):
        if e["kind"] in ("report", "report_read", "disk"):
            continue
        changed.append(f"{e['at'].astimezone():%H:%M} {e['kind']} {e['solution_id'] or ''}: {_describe(e)}"
                       .replace("  ", " "))
    for sol, n in conn.execute(
        "select solution_id, count(*) from elite where updated_at > now() - interval '24 hours' group by 1 order by 1"
    ).fetchall():
        changed.append(f"{n} new elites in {sol}")

    walls, last_week = _generation_walls(conn, 1, 0), _generation_walls(conn, 8, 1)
    wall = (f"{statistics.median(walls) / 60:.0f} min median"
            + (f", last week {statistics.median(last_week) / 60:.0f} min" if last_week else "")) if walls else "n/a"
    numbers = [("tokens, 24 h", _fmt_tokens(tokens)), ("generations, 24 h", str(gens)),
               ("generation wall clock", wall), ("active solutions", ", ".join(active) or "none")]

    wants = []
    if halt:
        wants.append(f"Halted: {halt}. Lift with `ops/kill.py --clear` once understood.")
    for e in events.pending(conn):
        wants.append(f"Acknowledge event {e['id']} ({e['kind']} {e['solution_id'] or ''}): "
                     f"`crucible morning ack {e['id']}`")
    for r in sorted((REPO_ROOT / "train" / "reviews").glob("*.yaml")):
        if not str((yaml.safe_load(r.read_text()) or {}).get("reviewer") or "").strip():
            wants.append(f"Sign or discard the harvest review `{r.relative_to(REPO_ROOT)}`.")
    if roster and all(c.state.dormant for c in roster):
        wants.append("Every solution is dormant: onboard one with headroom, or rotate an eval set.")
    er = events.latest(conn, "elite_read")
    if not er or er[0]["at"] < datetime.datetime.now(er[0]["at"].tzinfo) - datetime.timedelta(days=7):
        last = f"{er[0]['at']:%d %b}" if er else "never"
        wants.append(f"Weekly elite read is due (last: {last}). Record it with "
                     "`crucible morning elite-read \"what you found\"`.")

    return {"date": today.isoformat(), "halt": halt, "signals": signals, "changed": changed,
            "numbers": numbers, "solutions": solutions, "wants": wants, "generations": gens,
            "pending": events.pending(conn), "disk_pct": pct}


def write(conn, today: datetime.date | None = None) -> Path:
    f = collect(conn, today)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    path = REPORT_DIR / f"{f['date']}.md"
    path.write_text(render(f))
    word, reason = verdict(f["halt"], f["signals"])
    events.record(conn, "disk", pct=round(f["disk_pct"], 2))
    events.record(conn, "report", path=str(path.relative_to(REPO_ROOT)), verdict=word, reason=reason)
    return path


def main() -> int:
    from harness.persistence import connect

    ap = argparse.ArgumentParser(description="PHASE-6.md's morning report")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("write")
    sub.add_parser("read")
    p = sub.add_parser("elite-read")
    p.add_argument("note")
    p = sub.add_parser("ack")
    p.add_argument("id", type=int)
    a = ap.parse_args()
    with connect() as conn:
        if a.cmd == "write":
            print(write(conn))
        elif a.cmd == "read":
            last = events.latest(conn, "report")
            if not last:
                print("no report to mark read")
                return 1
            events.record(conn, "report_read", path=last[0]["detail"]["path"])
            print(f"marked read: {last[0]['detail']['path']}")
        elif a.cmd == "elite-read":
            events.record(conn, "elite_read", note=a.note)
            print("weekly elite read recorded")
        else:
            print("acknowledged" if events.ack(conn, a.id) else f"no pending event {a.id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

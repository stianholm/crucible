"""The morning report's verdict, ordering and comparison rules (PHASE-6.md)."""

import datetime as dt

from harness import morning
from harness.morning import Signal, render, verdict


def facts(**over):
    f = {"date": "2026-10-24", "halt": None, "generations": 12, "pending": [], "changed": [],
         "numbers": [("tokens, 24 h", "1.0M")], "wants": [],
         "solutions": [{"solution_id": "s", "state": "active", "held_out": "0.900", "eval_version": "abc"}],
         "signals": [Signal("attention", "last report read", True), Signal("disk", "40% used", True)]}
    f.update(over)
    return f


def test_verdict_is_one_of_three_words():
    ok = [Signal("a", "", True)]
    assert verdict(None, ok) == ("HEALTHY", "")
    assert verdict(None, ok + [Signal("disk", "", False), Signal("gate", "", False)]) == ("DEGRADED", "disk, gate")
    assert verdict("plateau step 4", ok + [Signal("disk", "", False)]) == ("HALTED", "plateau step 4")


def test_leads_with_would_stop_signals_and_names_the_reason():
    out = render(facts(signals=[Signal("attention", "last report (Fri 23 Oct) NOT read", False)]))
    lines = out.splitlines()
    assert lines[2].startswith("**DEGRADED**: attention")
    assert out.index("## Would-stop signals") < out.index("## What changed") < out.index("## Numbers")
    assert "**CHECK**" in out


def test_empty_sections_say_nothing_rather_than_vanish():
    out = render(facts())
    assert out.count("- nothing") == 2  # what changed, wants from you


def test_stays_short():
    # PHASE-6.md: readable in five minutes. A day with a full roster and
    # plenty happening must still fit on a screen or two.
    f = facts(signals=[Signal(f"s{i}", "x", True) for i in range(14)],
              changed=[f"event {i}" for i in range(10)], wants=["a", "b", "c"])
    assert len(render(f).splitlines()) < 70


def _rows(*pairs):
    return [{"detail": {"quality": q, "eval_version": v}, "at": dt.datetime(2026, 10, 24)} for q, v in pairs]


def test_held_out_compares_only_within_an_eval_set(monkeypatch):
    def run(rows):
        monkeypatch.setattr(morning.events, "latest", lambda *a, **k: rows)
        return morning._held_out(None, "s")

    sig, q, v = run(_rows((0.90, "v1"), (0.95, "v1")))
    assert not sig.ok and "best 0.950" in sig.value          # a real drop, same set
    sig, *_ = run(_rows((0.93, "v1"), (0.95, "v1")))
    assert sig.ok                                             # inside the grey zone
    sig, *_ = run(_rows((0.60, "v2"), (0.95, "v1")))
    assert sig.ok and "eval set changed, not compared" in sig.value
    sig, q, v = run([])
    assert sig is None and q == "not recorded"


def test_failed_jobs_are_named():
    assert morning.failed_jobs({"crucible-day": "success", "crucible-retention": "exit-code"}) == ["crucible-retention"]
    assert morning.failed_jobs({"crucible-day": "success", "crucible-alerts": "success"}) == []


def test_idle_counts_only_when_the_scheduler_checked_and_everything_is_dormant():
    # Decision 100: a correctly idle day is a scheduled day; a missing day is not.
    at = dt.datetime(2026, 10, 29, 6, 30, tzinfo=dt.timezone.utc)
    assert morning.activity(34, None, False).ok
    assert morning.activity(0, at, True).ok
    assert not morning.activity(0, None, True).ok    # the day timer never fired
    assert not morning.activity(0, at, False).ok     # something had headroom and did not run


def test_backup_signal_fails_when_never_taken_or_older_than_a_month():
    now = dt.datetime(2026, 11, 5, 12, tzinfo=dt.timezone.utc)
    assert not morning.backup(None, now).ok
    assert morning.backup(now - dt.timedelta(days=35), now).ok
    assert not morning.backup(now - dt.timedelta(days=36), now).ok

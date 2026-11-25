"""PHASE-6.md's immediate alert tier: what fires, what is suppressed, what clears."""

import datetime as dt

from harness.alerts import Observation, State, evaluate

T0 = dt.datetime(2026, 10, 25, 12, 0, tzinfo=dt.timezone.utc)


def obs(minutes=0, proposer=True, window=False, disk=40.0, sandboxes=(), capability=None):
    return Observation(T0 + dt.timedelta(minutes=minutes), {"proposer": proposer, "judge": True}, window,
                       disk, list(sandboxes), capability)


def test_model_down_fires_only_after_fifteen_minutes():
    st = State()
    assert evaluate(obs(0, proposer=False), st)[0] == {}
    assert evaluate(obs(14, proposer=False), st)[0] == {}
    cond, _ = evaluate(obs(15, proposer=False), st)
    assert "models:proposer" in cond and f"since {T0.astimezone():%H:%M}" in cond["models:proposer"]


def test_a_recovery_resets_the_clock():
    st = State()
    evaluate(obs(0, proposer=False), st)
    evaluate(obs(10), st)
    assert evaluate(obs(20, proposer=False), st)[0] == {}


def test_nightly_window_suppresses_model_down():
    st = State()
    for m in (0, 30, 300):
        assert evaluate(obs(m, proposer=False, window=True), st)[0] == {}


def test_disk_leak_capability():
    cond, _ = evaluate(obs(disk=86, sandboxes=[("crucible-sbx-a", 3600), ("crucible-sbx-b", 30)],
                           capability=("20261101", 0.06)), State())
    assert set(cond) == {"disk", "leak", "capability:20261101"}
    assert "1 sandbox" in cond["leak"]
    cond, _ = evaluate(obs(disk=85, capability=("20261017", -0.022)), State())
    assert cond == {}


def test_active_alerts_clear_when_the_condition_goes():
    st = State(active={"disk": 7, "leak": 8})
    cond, cleared = evaluate(obs(disk=90), st)
    assert "disk" in cond and cleared == ["leak"]

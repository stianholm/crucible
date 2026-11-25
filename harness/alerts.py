"""Immediate alerts. See PHASE-6.md, "Alerting".

Two tiers only. This module is the immediate tier; everything else belongs in
the morning report. Run every five minutes by crucible-alerts.timer:

    crucible alerts check    evaluate, fire new alerts, clear resolved ones
    crucible alerts test     send a test alert through every channel

| Signal | Fires when |
|---|---|
| models | proposer or judge unreachable for 15 minutes, outside a nightly window |
| disk | above 85% |
| leak | a sandbox container older than LEAK_AGE_S |
| capability | the newest adapter regresses more than 5% against stock |
| budget | relayed from the scheduler: the daily cap spent before 18:00 |

An alert fires once per incident, is recorded as an event needing
acknowledgement (so the morning report lists it until acknowledged), and
clears with a one-line "resolved" message when the condition goes away.

Channels: always the event and logs/alerts.log; a desktop notification when a
session bus exists; and a push to NTFY_URL (an ntfy topic URL in .env) only if
the operator has set one. Sending outside the box is the operator's choice.

Resist adding a tier (PHASE-6.md). A new signal goes in this table or in the
morning report, nowhere else.
"""

from __future__ import annotations

import argparse
import datetime
import importlib.util
import json
import os
import shutil
import subprocess
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path

from harness import events

REPO_ROOT = Path(__file__).resolve().parent.parent
STATE = REPO_ROOT / "state" / "alerts.json"
LOG = REPO_ROOT / "logs" / "alerts.log"
MODEL_DOWN_S = 15 * 60
DISK_PCT = 85
LEAK_AGE_S = 15 * 60      # sandbox runs are bounded far below this (harness/sandbox.py)
CAPABILITY_REGRESSION = 0.05
PORTS = {"proposer": 8000, "judge": 8001}


@dataclass
class Observation:
    now: datetime.datetime
    models: dict[str, bool]
    window: bool                       # a nightly window stops the models on purpose
    disk_pct: float
    sandboxes: list[tuple[str, float]]  # (name, age in seconds)
    capability: tuple[str, float] | None  # (adapter, regression)


@dataclass
class State:
    down_since: dict[str, str] = field(default_factory=dict)
    active: dict[str, int] = field(default_factory=dict)   # key -> alert event id


def evaluate(obs: Observation, st: State) -> tuple[dict[str, str], list[str]]:
    """Pure apart from updating st.down_since. Returns (conditions now true,
    keyed and described; keys of active alerts that have cleared)."""
    cond: dict[str, str] = {}
    for name, up in obs.models.items():
        if up or obs.window:
            st.down_since.pop(name, None)
            continue
        since = datetime.datetime.fromisoformat(st.down_since.setdefault(name, obs.now.isoformat()))
        if (obs.now - since).total_seconds() >= MODEL_DOWN_S:
            cond[f"models:{name}"] = f"{name} unreachable since {since.astimezone():%H:%M}"  # local time, not UTC
    if obs.disk_pct > DISK_PCT:
        cond["disk"] = f"disk {obs.disk_pct:.0f}% used (limit {DISK_PCT}%)"
    leaks = [n for n, age in obs.sandboxes if age > LEAK_AGE_S]
    if leaks:
        cond["leak"] = f"{len(leaks)} sandbox container(s) older than {LEAK_AGE_S // 60} min: {', '.join(leaks[:3])}"
    if obs.capability and obs.capability[1] > CAPABILITY_REGRESSION:
        a, r = obs.capability
        cond[f"capability:{a}"] = f"adapter {a} regresses {r:.1%} against stock (limit {CAPABILITY_REGRESSION:.0%})"
    cleared = [k for k in st.active if k not in cond]
    return cond, cleared


# ---------------------------------------------------------------- observing

def _healthy(port: int) -> bool:
    try:
        with urllib.request.urlopen(f"http://localhost:{port}/v1/models", timeout=5):
            return True
    except OSError:
        return False


def _in_window() -> bool:
    """A nightly window is running: ops/nightly.sh or the training container."""
    spec = importlib.util.spec_from_file_location("kill", REPO_ROOT / "ops" / "kill.py")
    kill = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(kill)
    if any(w in what for what in kill.find_runs().values() for w in kill.WINDOW_SCRIPTS):
        return True
    out = subprocess.run(["docker", "ps", "-q", "-f", f"name=^{kill.TRAIN_CONTAINER}$"], capture_output=True, text=True)
    return bool(out.stdout.strip())


def _sandboxes(now: datetime.datetime) -> list[tuple[str, float]]:
    out = subprocess.run(["docker", "ps", "-a", "--filter", "name=^crucible-sbx-", "--format", "{{.Names}}"],
                         capture_output=True, text=True).stdout.split()
    ages = []
    for name in out:
        created = subprocess.run(["docker", "inspect", "-f", "{{.Created}}", name],
                                 capture_output=True, text=True).stdout.strip()
        if created:
            t = datetime.datetime.fromisoformat(created[:26].rstrip("Z") + "+00:00")
            ages.append((name, (now - t).total_seconds()))
    return ages


def _capability() -> tuple[str, float] | None:
    adapters = sorted(p for p in (REPO_ROOT / "adapters").glob("[0-9]" * 8) if (p / "capability.json").exists())
    if not adapters:
        return None
    return adapters[-1].name, json.loads((adapters[-1] / "capability.json").read_text())["regression"]


def observe() -> Observation:
    now = datetime.datetime.now(datetime.timezone.utc)
    u = shutil.disk_usage("/")
    return Observation(now, {n: _healthy(p) for n, p in PORTS.items()}, _in_window(),
                       100 * u.used / u.total, _sandboxes(now), _capability())


# ---------------------------------------------------------------- delivering

def deliver(title: str, message: str) -> list[str]:
    """Every configured channel; returns the ones that worked."""
    sent = []
    LOG.parent.mkdir(exist_ok=True)
    with LOG.open("a") as f:
        f.write(f"{datetime.datetime.now():%F %T} {title}: {message}\n")
    sent.append("log")
    if os.environ.get("DBUS_SESSION_BUS_ADDRESS") or Path(f"/run/user/{os.getuid()}/bus").exists():
        env = {**os.environ, "DBUS_SESSION_BUS_ADDRESS": os.environ.get(
            "DBUS_SESSION_BUS_ADDRESS", f"unix:path=/run/user/{os.getuid()}/bus")}
        if subprocess.run(["notify-send", "-u", "critical", f"crucible: {title}", message],
                          env=env, capture_output=True).returncode == 0:
            sent.append("desktop")
    if url := os.environ.get("NTFY_URL"):
        req = urllib.request.Request(url, data=message.encode(), method="POST",
                                     headers={"Title": f"crucible: {title}", "Priority": "high"})
        try:
            urllib.request.urlopen(req, timeout=15).read()
            sent.append("ntfy")
        except OSError as e:
            with LOG.open("a") as f:
                f.write(f"{datetime.datetime.now():%F %T} ntfy delivery failed: {e}\n")
    return sent


def _load() -> State:
    try:
        return State(**json.loads(STATE.read_text()))
    except (FileNotFoundError, json.JSONDecodeError, TypeError):
        return State()


def _save(st: State) -> None:
    STATE.parent.mkdir(exist_ok=True)
    STATE.write_text(json.dumps(st.__dict__, indent=1))


def check(conn) -> None:
    st = _load()
    cond, cleared = evaluate(observe(), st)
    for key, msg in cond.items():
        if key in st.active:
            continue
        sent = deliver("ALERT", msg)
        st.active[key] = events.record(conn, "alert", None, needs_ack=True, signal=key, message=msg,
                                       immediate=True, delivered=sent)
        print(f"fired {key}: {msg} via {', '.join(sent)}")
    for key in cleared:
        deliver("resolved", f"{key} cleared")
        events.record(conn, "alert_cleared", None, signal=key, alert_event=st.active.pop(key))
        print(f"cleared {key}")
    # Immediate alerts other components recorded (the scheduler's budget
    # alert), delivered once.
    for e in events.since(conn, 48, ("alert",)):
        d = e["detail"]
        if d.get("immediate") and "delivered" not in d:
            sent = deliver("ALERT", d.get("message") or d.get("signal", "alert"))
            conn.execute("update event set detail = detail || %s::jsonb where id = %s",
                         (json.dumps({"delivered": sent}), e["id"]))
            conn.commit()
            print(f"relayed event {e['id']} via {', '.join(sent)}")
    _save(st)


def main() -> int:
    from harness.persistence import connect

    ap = argparse.ArgumentParser(description="PHASE-6.md's immediate alert tier")
    ap.add_argument("cmd", choices=["check", "test"])
    a = ap.parse_args()
    if a.cmd == "test":
        print("sent via", ", ".join(deliver("test", "crucible alert channel test; nothing is wrong")))
        return 0
    with connect() as conn:
        check(conn)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""The kill switch. See PHASE-6.md, "The kill switch".

One command. Stops generations, leaves the archive intact, leaves the deployed
solution at its last promoted state, and leaves the models serving.

    ops/kill.py "reason"     halt: set state/HALT, then stop everything running
    ops/kill.py --status     say whether the harness is halted, and why
    ops/kill.py --clear      lift the halt (a human decision, never automatic)

Standard library only, run with the system python3, so it works when the venv
or the database is the thing that broke.

Why each step is safe:
- **Archive.** Every elite insert and iteration row commits on its own
  (harness/generation.py), and Postgres rolls back an open transaction when
  its client dies, so a killed run leaves at worst a partial generation, never
  a half-written row. The elite counts printed before and after are the check.
- **Deployed solution.** No run writes solutions/*/candidate/; promotion is
  manual (PHASE-6.md, "What stays manual"). The git state printed at the end
  is the check.
- **Models.** Left alone unless the halt interrupted a nightly window, which
  stops both. Only then are they restarted, in the nightly's own order.
"""

from __future__ import annotations

import argparse
import datetime
import getpass
import os
import signal
import subprocess
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
HALT = REPO / "state" / "HALT"
# Every long-running entry point. A new one belongs here, or the switch misses it.
RUN_SCRIPTS = ("ops/search.sh", "ops/nightly.sh", "ops/round1.sh", "ops/daily.sh")
WINDOW_SCRIPTS = ("ops/nightly.sh", "ops/round1.sh")
TRAIN_CONTAINER = "crucible-train"
SANDBOX_PREFIX = "crucible-sbx-"


def is_run(argv: list[str], cwd: str) -> str | None:
    """Which crucible run this process is, or None. Matches on the program
    and script paths resolved against the process's cwd, never on free text:
    a shell whose command line merely mentions ops/search.sh must not match,
    the mistake `pkill -f` made several times (TODO.md decision 83)."""
    if not argv:
        return None
    paths = [os.path.normpath(os.path.join(cwd, a)) for a in argv[:2]]
    if paths[0] == str(REPO / ".venv" / "bin" / "python") or paths[0] == str(REPO / ".venv" / "bin" / "python3"):
        return "python"
    # The script is the program, or the argument a shell is running; `grep
    # ops/search.sh logs/x` names it too and is not a run.
    shell = os.path.basename(argv[0]) in ("bash", "sh")
    for script in RUN_SCRIPTS:
        if paths[0] == str(REPO / script) or (shell and paths[1:] == [str(REPO / script)]):
            return script
    return None


def find_runs() -> dict[int, set[str]]:
    """Process groups holding a crucible run, mapped to what they hold."""
    own = os.getpgrp()
    groups: dict[int, set[str]] = {}
    for d in Path("/proc").iterdir():
        if not d.name.isdigit():
            continue
        try:
            argv = (d / "cmdline").read_bytes().decode(errors="replace").split("\0")[:-1]
            cwd = os.readlink(d / "cwd")
            pgid = os.getpgid(int(d.name))
        except (OSError, ProcessLookupError):
            continue
        what = is_run(argv, cwd)
        if what and pgid != own:
            groups.setdefault(pgid, set()).add(what)
    return groups


def sh(*cmd: str) -> str:
    r = subprocess.run(cmd, capture_output=True, text=True)
    return r.stdout.strip()


def archive_fingerprint() -> str:
    """Elite count and a hash of every parked archive. Live archives (named
    after a directory in solutions/) are left out: a run halted mid-generation
    may legitimately leave its own archive short, and the hash is what shows
    nothing else moved."""
    live = ",".join(f"'{d.name}'" for d in (REPO / "solutions").iterdir() if d.is_dir())
    q = ("select count(*) || ' elites, ' || coalesce(md5(string_agg(solution_id || island_id || cell::text "
         "|| iteration_id || scalar, ',' order by solution_id, island_id, cell)), '-') "
         f"from elite where solution_id not in ({live})")
    return sh("docker", "exec", "crucible-postgres-1", "psql", "-U", "postgres", "-d", "crucible", "-tAc", q) or "unavailable"


def running_requests() -> int:
    n = 0
    for port in (8000, 8001):
        out = sh("curl", "-s", "-m5", f"localhost:{port}/metrics")
        n += sum(int(float(l.split()[-1])) for l in out.splitlines() if l.startswith("vllm:num_requests_running"))
    return n


def healthy(port: int) -> bool:
    return subprocess.run(["curl", "-sf", "-m5", f"localhost:{port}/v1/models"], capture_output=True).returncode == 0


def restore_models() -> None:
    """The nightly's restore(), for a window the halt interrupted."""
    for service, port, tries in (("vllm-proposer", 8000, 120), ("vllm-judge", 8001, 60)):
        if healthy(port):
            print(f"  {service} already serving")
            continue
        subprocess.run([sys.executable, str(REPO / "ops" / "evict_cache.py")], cwd=REPO)
        subprocess.run(["docker", "compose", "up", "-d", service], cwd=REPO, check=True)
        for _ in range(tries):
            if healthy(port):
                print(f"  {service} serving")
                break
            time.sleep(10)
        else:
            print(f"  {service} NOT HEALTHY after {tries * 10 // 60} min: fix by hand")


def halt(reason: str) -> int:
    HALT.parent.mkdir(exist_ok=True)
    stamp = datetime.datetime.now().isoformat(timespec="seconds")
    HALT.write_text(f"{stamp} {reason} (by {getpass.getuser()})\n")
    print(f"halt set: {HALT.read_text().strip()}")
    before = archive_fingerprint()

    groups = find_runs()
    for pgid, what in groups.items():
        print(f"stopping process group {pgid}: {', '.join(sorted(what))}")
        try:
            os.killpg(pgid, signal.SIGTERM)
        except ProcessLookupError:
            pass
    deadline = time.time() + 15
    while time.time() < deadline and any(_alive(g) for g in groups):
        time.sleep(1)
    for pgid in groups:
        if _alive(pgid):
            os.killpg(pgid, signal.SIGKILL)
            print(f"killed stragglers in {pgid}")
    if not groups:
        print("no crucible run was running")

    # A dead client does not cancel its requests: LiteLLM keeps the upstream
    # connections and vLLM decodes on for minutes. Restarting LiteLLM drops
    # them (measured 2026-10-24: 16 orphans, 0 three seconds after an 11 s
    # restart) and leaves both models loaded.
    if groups and (n := running_requests()):
        subprocess.run(["docker", "compose", "restart", "litellm"], cwd=REPO, capture_output=True)
        # Restarted is not ready: LiteLLM answers about 6 s later. A run
        # relaunched 13 s after an early version of this switch lost all 32
        # proposals of its first generation to connection errors (2026-10-25).
        for _ in range(60):
            if subprocess.run(["curl", "-sf", "-m3", "localhost:4000/health/liveliness"],
                              capture_output=True).returncode == 0:
                break
            time.sleep(2)
        else:
            print("  LiteLLM NOT answering after 2 min: fix by hand")
        print(f"restarted LiteLLM to cancel {n} orphaned requests; now {running_requests()} running")

    window = any(w in what for what in groups.values() for w in WINDOW_SCRIPTS)
    if sh("docker", "ps", "-q", "-f", f"name=^{TRAIN_CONTAINER}$"):
        subprocess.run(["docker", "stop", TRAIN_CONTAINER], capture_output=True)
        print("stopped the training container")
        window = True
    sandboxes = sh("docker", "ps", "-aq", "-f", f"name=^{SANDBOX_PREFIX}").split()
    if sandboxes:
        subprocess.run(["docker", "rm", "-f", *sandboxes], capture_output=True)
        print(f"removed {len(sandboxes)} sandbox containers")

    if window:
        print("a nightly window was interrupted: restoring the models")
        restore_models()
    for name, port in (("proposer", 8000), ("judge", 8001)):
        print(f"  {name}: {'serving' if healthy(port) else 'not serving'}")

    after = archive_fingerprint()
    print(f"parked archives: before {before}\n                 after  {after}"
          + ("" if before == after else "\n  CHANGED: investigate before lifting the halt"))
    changed = sh("git", "-C", str(REPO), "status", "--porcelain", "--", "solutions/*/candidate")
    print("deployed candidates: " + ("UNCOMMITTED CHANGES\n" + changed if changed else "unchanged from git"))
    print("halted. Lift with: ops/kill.py --clear")
    return 0


def _alive(pgid: int) -> bool:
    try:
        os.killpg(pgid, 0)
        return True
    except ProcessLookupError:
        return False


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("reason", nargs="?", help="why, recorded in state/HALT")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--status", action="store_true")
    g.add_argument("--clear", action="store_true")
    a = ap.parse_args()
    if a.status or a.clear:
        reason = HALT.read_text().strip() if HALT.exists() else None
        if a.clear and reason:
            HALT.unlink()
            print(f"halt lifted (was: {reason})")
        else:
            print(f"halted: {reason}" if reason else "not halted")
        return 0
    if not a.reason:
        ap.error("give a reason; it is what the morning report will show")
    return halt(a.reason)


if __name__ == "__main__":
    sys.exit(main())

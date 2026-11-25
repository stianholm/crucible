"""The single sandbox slot. See PHASE-2.md task 2.3.

Rootless, no network, read-only root, capped everything — except this uses
docker, not podman as PHASE-2.md specifies. podman isn't installed on this
machine and rootless mode needs sudo-gated subuid/subgid configuration;
docker was already working from Phase 0. Every other isolation property
(--network none, --read-only, memory/pids caps, --cap-drop ALL,
--security-opt no-new-privileges) is identical either way. The one real
gap: docker's daemon runs as root, so a container escape is more
consequential than it would be under rootless podman. Documented deviation,
not an oversight — see TODO.md. Swap the `docker` calls below for `podman`
if that gap ever needs closing; the flags themselves barely change.

The wall clock is enforced twice, per the spec's own reasoning: once inside
the container via coreutils `timeout` (so a runaway candidate process is
killed from the inside), and once in this parent process (so a container
that fails to even start — image pull hang, daemon hiccup — still gets
killed, since it would never reach its own internal timeout).
"""

from __future__ import annotations

import subprocess
import time
import uuid
from pathlib import Path

from harness.types import Run

RUNNER_IMAGE = "harness/runner:1"
PARENT_TIMEOUT_SLACK_S = 10.0  # headroom over the in-container timeout before the parent also kills it


def run_in_sandbox(
    cand_dir: Path,
    task_input: str,
    timeout: float,
    memory_mb: int = 256,
    pids_limit: int = 64,
    cpus: float = 1.0,
) -> Run:
    name = f"crucible-sbx-{uuid.uuid4().hex[:12]}"
    cmd = [
        "docker",
        "run",
        "--rm",
        "--name",
        name,
        "--network",
        "none",
        "--read-only",
        "--tmpfs",
        "/tmp:rw,size=64m",
        "--memory",
        f"{memory_mb}m",
        "--memory-swap",
        f"{memory_mb}m",
        "--pids-limit",
        str(pids_limit),
        "--cpus",
        str(cpus),
        "--cap-drop",
        "ALL",
        "--security-opt",
        "no-new-privileges",
        "-v",
        f"{cand_dir}:/candidate:ro",
        "--entrypoint",
        "timeout",
        RUNNER_IMAGE,
        f"{timeout}s",
        "python",
        "/run_candidate.py",
        task_input,
    ]

    t0 = time.perf_counter()
    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout + PARENT_TIMEOUT_SLACK_S,
        )
    except subprocess.TimeoutExpired:
        # backstop: the container never respected its own in-container
        # timeout (e.g. it never started at all). Kill it directly —
        # killing the docker-run client process does not stop the
        # container by itself.
        subprocess.run(["docker", "kill", name], capture_output=True, timeout=10)
        return Run(
            output=None,
            tokens=0,
            tool_calls=0,
            wall_time_s=time.perf_counter() - t0,
            raw={"error": "timeout (parent-enforced backstop)"},
        )

    wall = time.perf_counter() - t0
    if proc.returncode == 124:
        return Run(output=None, tokens=0, tool_calls=0, wall_time_s=wall, raw={"error": "timeout (in-container)"})
    if proc.returncode != 0:
        return Run(
            output=None,
            tokens=0,
            tool_calls=0,
            wall_time_s=wall,
            raw={"stderr": proc.stderr[-2000:], "returncode": proc.returncode},
        )
    return Run(output=proc.stdout.strip(), tokens=0, tool_calls=0, wall_time_s=wall, raw={})

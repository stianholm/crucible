# Security, as built

**Posture:** isolated lab machine, non-sensitive data, single operator
(decision 4). Moved from `THREAT-MODEL.md` and corrected to what was built.

---

## What this defends against

There is no meaningful external adversary on an isolated box with one user.
The real risk is different in kind: this system generates code and runs it,
unattended, thousands of times a week. Nothing is attacking it. Its own
search explores a space that includes destructive behaviour, without intent
and faster than any review. So the model is **containment of the system's own
output**.

## Assets

| Asset | Cost if lost |
|---|---|
| Postgres (`iteration`, `elite`, `lesson`, `event`) | Weeks of GPU time; the project's memory |
| Task sets and sealed held-out splits | Every historical measurement becomes unreproducible |
| LoRA adapters | One nightly window each |
| `CAPACITY.yaml`, `BASELINE.yaml` files | The basis of every sizing decision |
| Model weights | Download time only |

The expensive assets are small and the large ones are cheap, which keeps
[backup.md](backup.md) simple.

## Trust boundary

```
  trusted                          untrusted
┌──────────────────────────┐   ┌───────────────────────────┐
│ harness code             │   │ candidate artifacts       │
│ fitness.py, scorer       │──▶│ written by the proposer   │
│ archive, task sets       │   │ executed in the sandbox   │
│ checks/, adapters        │◀──│ returns only its output   │
└──────────────────────────┘   └───────────────────────────┘
```

**The candidate never reaches the evaluator**: not by import, path or
network. Its output is scored outside the sandbox by code it cannot see.

## Controls as built

| Risk | Control | Where |
|---|---|---|
| Generated code damages the host | Read-only root, 64 MB tmpfs, only the candidate directory mounted, read-only | `harness/sandbox.py` |
| Generated code reaches the network | `--network none`, always | `harness/sandbox.py` |
| Runaway resources | Memory and pids caps, one CPU, wall-clock kill in the container and again by the parent | `harness/sandbox.py` |
| Escalation | Docker (not rootless Podman, decision 14), `--cap-drop ALL`, `no-new-privileges`, non-root user in the image | `sandbox/Dockerfile` |
| Candidate scores itself | Forbidden imports in the validation ladder; scorer and checks outside the mount | `harness/validate.py` |
| Generated instructions steer the judge | The judge sees an adapter-controlled view of the output | `judge_view` in `harness/scorer.py` |
| Container leak | Immediate alert on any sandbox older than 15 minutes; the kill switch removes them | `harness/alerts.py`, `ops/kill.py` |
| Disk exhaustion | Retention sweep; alert at 85% | `harness/retention.py`, `harness/alerts.py` |
| Archive loss | `ops/backup.sh`, verified by a scratch restore; on the same disk until copied off | [backup.md](backup.md) |

The abuse suite (`tests/test_sandbox_abuse.py`: a hang, an allocation bomb, a
fork bomb) is the enforcement test. Run it after any container or Docker
change. Network and filesystem isolation are set by flags and not tested by
the suite.

Docker's daemon runs as root, so a container escape is more serious than it
would be under rootless Podman. Accepted for this posture.

## Supply chain

- **Images** are pinned by digest (`.container-digest`,
  `train/.container-digest`).
- **Python packages** for training are locked (`train/requirements.lock`).
- **The sandbox image** is built locally and kept minimal: an interpreter and
  nothing else.
- **Model weights** are trusted as published.

## Accepted risks

- No egress filtering outside the sandbox; the host reaches Hugging Face and
  NGC.
- No authentication on internal services; all bind `127.0.0.1`.
- No tamper-proof audit log; the archive is the record.
- **Alerts leave the box** through ntfy.sh since 2026-10-25 (`NTFY_URL`). The
  unguessable topic name is the only protection. Messages carry signal names
  and times, never data.
- **Security updates are applied by hand,** through the change procedure and
  after a fresh backup, because they risk stopping vLLM mid-run (decision 99).
  The batch deferred through Phase 6 was installed on 2026-11-05, and the sandbox
  abuse suite passed afterwards (decision 105).

## What would change this model

Revisit everything if any of these become true: the data becomes sensitive;
the box joins a shared or corporate network; a second person gets access; an
improved solution's output is used in production; or a solution needs network
access inside the sandbox, which needs an allowlist proxy, not a relaxed
flag.

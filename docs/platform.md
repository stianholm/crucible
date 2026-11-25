# Platform

The machine, the measured capacity, and the traps that are expensive to
rediscover. This replaces `MEMORY.md`, the planning-era memory accounting,
which is not included in this repository.

---

## Hardware

| | |
|---|---|
| Machine | HP ZGX Nano G1n AI Station |
| Processor | NVIDIA GB10, 20 Arm cores |
| Memory | 128 GB unified LPDDR5X, 121.6 GiB usable |
| Bandwidth | 273 GB/s |
| Compute | sm_121 |
| OS | NVIDIA DGX OS, aarch64 |
| Disk | 3.6 TB NVMe, one filesystem |

## Containers

| Image | Pinned | Why pinned |
|---|---|---|
| `nvcr.io/nvidia/vllm:26.08-py3` | By digest, `.container-digest` | vLLM does not officially target sm_121; support arrives through NVIDIA's builds. Never float the tag or chase upstream main |
| `crucible-train:26.08` | Built from NVIDIA PyTorch 26.08 by digest (`train/.container-digest`) | The build asserts an NVIDIA torch |
| `harness/runner:1` | Built from `sandbox/Dockerfile` | Executes generated code; minimal on purpose |

---

## System updates

Nothing installs updates automatically: `unattended-upgrades` is absent and
the apt periodic settings are 0 (checked 2026-10-27). The DGX Dashboard
(`localhost:11000`, the machine's own login) installs only when someone clicks
Update. Treat a kernel, NVIDIA driver, container toolkit or Docker update as a
platform change: [change-procedures.md](change-procedures.md), then a reboot
check (decision 99).

| Installed 2026-11-05 (decision 105) | Version |
|---|---|
| Kernel | 7.0.0-1024-nvidia |
| NVIDIA driver | 580.178.04 |
| NVIDIA Container Toolkit | 1.20.1 |
| Docker | 29.6.2 |

## Capacity (`CAPACITY.yaml`)

Re-measured 2026-11-05 at the live KV pins (decision 105). Machine-and-model
level. Per-solution generation sizing lives in each solution's `BASELINE.yaml`;
do not merge the two.

| Profile | Knee | Saturation | Aggregate at knee | Per sequence at knee |
|---|---:|---:|---:|---:|
| Propose (4096 in, 1024 out) | 16 | 16 | 142.9 tok/s | 9.23 tok/s |
| Judge (2048 in, 128 out) | 16 | 32 | 199.1 tok/s | 13.96 tok/s |

- **The propose profile is a worst case.** The proposer's 92,991-token cache
  holds about 18 requests of 5,120 tokens.
- **Real generations are unaffected.** They ran 32 requests at a median
  221 tok/s and 31% KV use, 2026-10-17 to 10-26.
- **The limit for a new solution:** requests averaging above about 2,900 tokens
  would queue at 32. Check this at onboarding.
- **September's higher ceiling is not available.** Its 201 tok/s at 64 used a
  233,350-token cache, at utilisation 0.80 with the stack stopped.

Sustained derate over 30 minutes: 0.98, measured in September at concurrency 32
with the larger cache.

## Memory

| Component | Resident |
|---|---:|
| gpt-oss-120b weights, MXFP4 | 82.8 GiB |
| Proposer total at 0.74 utilisation | about 85.5 GiB |
| Judge total at 0.09 utilisation | about 14.5 GiB |
| Observability stack | about 4.4 GiB |
| OS, desktop, Docker | about 10.6 GiB |

After the 2026-11-05 updates and about 6.5 hours of sweeps, `MemAvailable` read 4.9 GiB and
`MemFree` 1.7 GiB, in line with the roughly 5 GiB `CAPACITY.yaml` records.

Proposer and judge reserve 83% of the pool between them. **No third CUDA
process can initialise beside them**, however small: an embedding model
failed with out-of-memory at device init, twice (decision 34). Training needs
both stopped.

---

## Traps

- **Page cache is not free memory to CUDA.** After reading weights, tens of
  GB the kernel calls available cannot be allocated. Run
  `python3 ops/evict_cache.py` and check `MemFree`, not `MemAvailable`, before
  any large GPU allocation.
- **`nvidia-smi` reports memory as N/A** on this unified pool. Use
  `/proc/meminfo`, and `nvidia-smi --query-compute-apps` for per-process use.
  `docker stats` underreports vLLM by tens of GB.
- **KV cache sizing is not deterministic** unless pinned. The same 0.74
  produced 0.06, 0.77 and 18.05 GiB in one evening. Both engines pin
  `--kv-cache-memory-bytes`; do not remove the pins without re-measuring.
- **The two engines can fail to cold-start together** (decision 11). Start
  the proposer, wait for it to be healthy, then the judge (compose order and
  `ops/nightly.sh` do this). Docker ignores that order at boot; a reboot test
  started both together without trouble (decision 99), and if it ever fails
  the 15-minute alert says so.
- **`--gpu-memory-utilization` is a lifetime reservation** of the shared pool,
  not a ceiling.
- **Client timeouts must exceed 15 minutes.** At high concurrency a sequence
  decodes at a few tokens per second.
- **The judge is not deterministic under concurrent load.** About 25% of
  verdicts flip when the same requests are batched differently. Batch-invariant
  mode fixes the judge but cannot run on the MXFP4 worker (decisions 71, 72).
- **A dead client does not cancel its requests.** LiteLLM keeps decoding
  them. Restarting LiteLLM drops them in about 11 s; it answers about 6 s
  after that (decisions 89, 94).
- **Postgres `now()` is the transaction start.** Event timestamps use
  `clock_timestamp()` (decision 91).
- **Nemotron NVFP4 is capped at `--max-num-seqs 4`** on this platform, which
  rules it out for population search.
- **Two jobs setting up the schema at once deadlocked** while one held a
  read lock (23:00 retention against the alert check, two nights running).
  `ensure_schema()` now commits first and takes an advisory lock (decisions
  96, 98).
- **The clocks change.** On 2026-10-25 the zone went from CEST (+02) to CET
  (+01), and a query written with `+02` silently selected the wrong hour.
  Compare timestamps with the zone name or in UTC.
- **Plain `python` does not exist** on this machine. Use `crucible <module>`
  (`ops/crucible`), or `.venv/bin/python` from the repository root.
- **`pkill -f` matches its own shell.** Stop runs by process group
  (`ops/stop.sh`, `ops/kill.py`), never by command-line text (decision 83).

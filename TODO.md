# Roadmap

**Updated 2026-11-25.** What is left, and what would come next. The system as
built is documented in [docs/](docs/README.md); every decision so far is in
[docs/decisions.md](docs/decisions.md).

**State:** Phases 0 to 6 complete. Phase 6's handover closed on 2026-11-05
after nine scheduled days (decision 102). Every solution is dormant, so the
scheduler idles by design until one gets new headroom (decision 100). This is
a finished case study, published as-is.

---

## Phase 6 handover checklist, as closed

| Item | Result |
|---|---|
| Consecutive scheduled days, no manual intervention | 9, 2026-10-28 to 2026-11-05 (decisions 100 to 102) |
| Morning reports delivered and read | 9 of 9 |
| Plateau escalation handled by the ladder | All four steps, 2026-10-26 and 28 |
| A real alert caught a real problem | 2026-10-27, the report's `jobs` signal named a deadlock (decision 98) |
| Retention enforced, disk flat over a week | 10%, +0.0 points over 7 days |
| Chaos test against the live system | 2026-10-25 (decision 95) |
| Elite read | Once, 2026-11-02 |
| Kill switch tested, archive intact | Seven live uses |

Not shown: the phone tier never fired on a real problem, and the box idled
after day 1, so slow drift under load is unmeasured (decision 102).

---

## Done after the handover

- **Backup built and verified** (decision 103), and copied off the machine
  (decision 104).
- **Deferred system updates applied** with a reboot check, the abuse suite, a
  capacity sweep and one real `fixture` generation (decision 105).

## Open

- **Give the scheduler work.** Every solution is dormant. New headroom means a
  new eval set, a fitness change (both manual), or a new solution onboarded.
- **Test the distillation thesis.** It is untested, not refuted: the only
  adapter was trained before the solutions saturated
  ([docs/distillation.md](docs/distillation.md)). `ot_change_scheduler` is the
  first solution with a deep enough gradient to test it.
- **Measure slow drift under load.** Weeks of real generations, not an idle
  box: wall clock, thermals, leaks.
- **Free memory for the proposer's KV cache.** Moving the observability stack
  and the desktop session off the box could roughly double it. Not measured;
  re-measure through [docs/change-procedures.md](docs/change-procedures.md).
- **Promote `ot_change_scheduler`'s winner** when the evidence is good enough.
  The 2026-11-02 elite read found nothing worth promoting. If one is promoted
  later, prefer `b246cae8`, which also avoids a possible defect in the
  incumbent (its swap step removes a scheduled change without checking what
  depends on it; not yet measured).
- **The weekly checks** (rotate the visible rotation slice, re-check the
  taxonomy, check the reseed rule) are not built. Build them when a solution
  is running again.

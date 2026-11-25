"""The retention sweep's policy constants match PHASE-6.md's table."""

from harness import retention


def test_policy_matches_phase_6():
    assert retention.CANDIDATE_DAYS == 30
    assert retention.TRACE_DAYS == 90
    assert retention.SYSTEM_LOG_DAYS == 7
    # Langfuse's three trace tables are all covered, each by its own time column.
    assert {"traces", "observations", "scores"} <= set(retention.LANGFUSE_TABLES)

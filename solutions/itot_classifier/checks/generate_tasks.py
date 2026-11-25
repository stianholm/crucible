"""Builds the itot_classifier task set from reference.py and writes it
split three ways. See PHASE-1.md task 1.2. `expected` is always computed
by calling the reference classifier, never typed by hand — the only thing
that needs hand-checking is whether each scenario's *input* fields
faithfully represent the situation its comment describes, against the
paper's own text.

Usage: python -m solutions.itot_classifier.checks.generate_tasks
"""

from __future__ import annotations

import dataclasses
import json
from pathlib import Path

from harness.split import split_of
from solutions.itot_classifier.checks.reference import IntegrationProposal, classify

SOL_DIR = Path(__file__).resolve().parent.parent

# Each entry: (proposal_id, IntegrationProposal). expected is computed via
# classify(), never hand-typed. Comments trace each scenario back to a
# specific paper passage so the "hand-check" step is checkable, not just
# asserted.
SCENARIOS: list[tuple[str, IntegrationProposal]] = [
    # --- pure telemetry reads (Sec 5 §3, Gateway 1 in Sec 5) ---
    ("telemetry-01", IntegrationProposal("telemetry-01", "Historian time-series read for a dashboard", False, False, "live_process", True)),
    ("telemetry-02", IntegrationProposal("telemetry-02", "Current process values for a shift summary", False, False, "live_process", True)),
    ("telemetry-03", IntegrationProposal("telemetry-03", "Alarm and event stream join for operator briefing", False, False, "live_process", True)),
    ("telemetry-04", IntegrationProposal("telemetry-04", "Equipment health indicators, not yet in operations' approved source list", False, False, "live_process", False)),
    ("telemetry-05", IntegrationProposal("telemetry-05", "Predictive maintenance recommendation input data", False, False, "live_process", True)),
    ("telemetry-06", IntegrationProposal("telemetry-06", "Reading SIS *state visibility* via a monitoring system, not the SIS itself (Sec 6 narrow exception)", False, False, "live_process", True)),

    # --- pure engineering data reads (Gateway 2 in Sec 5) ---
    ("engineering-01", IntegrationProposal("engineering-01", "P&ID drawings for an engineer's retrieval query", False, False, "engineering", True)),
    ("engineering-02", IntegrationProposal("engineering-02", "Asset register lookup for incident history search", False, False, "engineering", True)),
    ("engineering-03", IntegrationProposal("engineering-03", "Equipment specifications, not yet in the approved engineering-data scope", False, False, "engineering", False)),
    ("engineering-04", IntegrationProposal("engineering-04", "Maintenance history records for a reliability analysis", False, False, "engineering", True)),
    ("engineering-05", IntegrationProposal("engineering-05", "Control system configuration, read-only, for design review support", False, False, "engineering", True)),

    # --- operational change (Gateway 3), various approval states ---
    ("opchange-01", IntegrationProposal("opchange-01", "Sec 6 worked example: refinery setpoint adjustment, on the allow-list, in a maintenance window, human-approved", False, True, "live_process", True)),
    ("opchange-02", IntegrationProposal("opchange-02", "Setpoint adjustment requested, but not yet on operations' allow-list", False, True, "live_process", False)),
    ("opchange-03", IntegrationProposal("opchange-03", "Nuisance-alarm parameterised acknowledgement, narrow pre-approved class (Sec 7)", False, True, "live_process", True, pre_approved_narrow_class=True)),
    ("opchange-04", IntegrationProposal("opchange-04", "Maintenance-window test sequence during planned shutdown (Sec 7)", False, True, "live_process", True)),
    ("opchange-05", IntegrationProposal("opchange-05", "Closed-loop process optimisation adjustment, well-instrumented unit, pre-approved narrow class (Sec 7)", False, True, "live_process", True, pre_approved_narrow_class=True)),
    ("opchange-06", IntegrationProposal("opchange-06", "Configuration change request outside any approved allow-list", False, True, "engineering", False)),

    # --- the safety wall (Sec 6): touches_sis always wins, regardless of other fields ---
    ("safety-01", IntegrationProposal("safety-01", "Agent proposes to acknowledge an SIS alarm directly", True, True, "live_process", False)),
    ("safety-02", IntegrationProposal("safety-02", "Agent wants read access framed as 'just visibility' but touches the SIS itself", True, False, "live_process", True)),
    ("safety-03", IntegrationProposal("safety-03", "Proposed future enhancement: agent tunes SIS proof-test intervals", True, True, "engineering", True)),
    ("safety-04", IntegrationProposal("safety-04", "SIS interaction proposed even with full approval and allow-listing in place", True, True, "live_process", True)),

    # --- anti-pattern: "we will connect the agent directly, just for the pilot" ---
    ("antipattern-pilot-01", IntegrationProposal("antipattern-pilot-01", "Pilot wires the agent straight into the historian, no gateway at all", False, False, "live_process", True, is_pilot=True, pilot_uses_full_gateway=False)),
    ("antipattern-pilot-02", IntegrationProposal("antipattern-pilot-02", "Pilot, but runs through a minimal real gateway (identity, allow-list, logging) — the paper's own alternative", False, False, "live_process", True, is_pilot=True, pilot_uses_full_gateway=True)),
    ("antipattern-pilot-03", IntegrationProposal("antipattern-pilot-03", "Operational-change pilot skipping the gateway to move fast", False, True, "live_process", True, is_pilot=True, pilot_uses_full_gateway=False)),

    # --- anti-pattern: "it is just an API" ---
    ("antipattern-api-01", IntegrationProposal("antipattern-api-01", "Proposal treats the OT historian as a generic REST endpoint, no gateway framing", False, False, "live_process", True, treats_ot_as_plain_api=True)),
    ("antipattern-api-02", IntegrationProposal("antipattern-api-02", "Operational-change request designed as a plain API call, difference collapsed into the API contract", False, True, "live_process", True, treats_ot_as_plain_api=True)),

    # --- anti-pattern: "same identity on both sides, it is simpler" ---
    ("antipattern-identity-01", IntegrationProposal("antipattern-identity-01", "Single IT-side identity proposed to also authenticate on the OT side", False, False, "engineering", True, shares_identity_across_boundary=True)),
    ("antipattern-identity-02", IntegrationProposal("antipattern-identity-02", "Operational-change proposal reuses the agent's IT identity as its OT-side credential", False, True, "live_process", True, shares_identity_across_boundary=True)),

    # --- anti-pattern: "the gateway is plumbing; ops can build it" ---
    ("antipattern-plumbing-01", IntegrationProposal("antipattern-plumbing-01", "Gateway spec handed to operations, never reaches the architecture review", False, True, "live_process", True, gateway_spec_reviewed_by_architect=False)),
    ("antipattern-plumbing-02", IntegrationProposal("antipattern-plumbing-02", "Telemetry gateway treated as generic integration infrastructure, unreviewed", False, False, "live_process", True, gateway_spec_reviewed_by_architect=False)),

    # --- anti-pattern: "the agent will know when to stop" ---
    ("antipattern-selfrestraint-01", IntegrationProposal("antipattern-selfrestraint-01", "Allow-list removed on the strength of the agent's training and evaluation results alone", False, True, "live_process", True, relies_on_agent_self_restraint_only=True)),
    ("antipattern-selfrestraint-02", IntegrationProposal("antipattern-selfrestraint-02", "Team argues the agent is reliable enough that the allow-list is redundant", False, True, "engineering", True, relies_on_agent_self_restraint_only=True)),

    # --- anti-pattern: "eval runs nightly" (only bites on operational-change) ---
    ("antipattern-nightlyeval-01", IntegrationProposal("antipattern-nightlyeval-01", "Operational-change action evaluated only in a nightly batch, not pre-action", False, True, "live_process", True, evaluation_only_nightly_batch=True)),
    ("antipattern-nightlyeval-02", IntegrationProposal("antipattern-nightlyeval-02", "Telemetry read, nightly-batch evaluated — anti-pattern does not apply outside operational-change", False, False, "live_process", True, evaluation_only_nightly_batch=True)),

    # --- anti-pattern: "we will govern it later" ---
    ("antipattern-governlater-01", IntegrationProposal("antipattern-governlater-01", "Architecture and gateway built, governance for allow-list changes deferred to a later phase", False, True, "live_process", True, governance_defined_upfront=False)),
    ("antipattern-governlater-02", IntegrationProposal("antipattern-governlater-02", "Telemetry gateway deployed without a defined review cadence for source additions", False, False, "live_process", True, governance_defined_upfront=False)),

    # --- additional coverage: not-approved variants, pre-approved-narrow-class
    # combinations, and anti-patterns on the engineering-data path (most
    # anti-pattern scenarios above use live_process; a real classifier
    # should not silently assume anti-pattern detection is data-type-specific) ---
    ("telemetry-07", IntegrationProposal("telemetry-07", "Alarm stream, requested for a use case operations has not yet reviewed", False, False, "live_process", False)),
    ("engineering-06", IntegrationProposal("engineering-06", "Certification records lookup, within the already-approved engineering scope", False, False, "engineering", True)),
    ("engineering-07", IntegrationProposal("engineering-07", "Maintenance history, outside the approved engineering-data source list", False, False, "engineering", False)),
    ("opchange-07", IntegrationProposal("opchange-07", "Pre-approved narrow class requested, but the specific action is not yet on the allow-list", False, True, "live_process", False, pre_approved_narrow_class=True)),
    ("opchange-08", IntegrationProposal("opchange-08", "Engineering-scope write (e.g. asset-register correction), approved, full gateway", False, True, "engineering", True)),
    ("safety-05", IntegrationProposal("safety-05", "Read-only SIS state query proposed directly against the SIS (not a monitoring system) — still rejected", True, False, "live_process", True)),
    ("safety-06", IntegrationProposal("safety-06", "SIS-touching pilot, fully approved elsewhere — rejection is unconditional", True, True, "live_process", True, is_pilot=True, pilot_uses_full_gateway=True)),
    ("antipattern-api-03", IntegrationProposal("antipattern-api-03", "Engineering-data read designed as a plain API call to the config store", False, False, "engineering", True, treats_ot_as_plain_api=True)),
    ("antipattern-identity-03", IntegrationProposal("antipattern-identity-03", "Telemetry read reusing the same identity across the boundary", False, False, "live_process", True, shares_identity_across_boundary=True)),
    ("antipattern-plumbing-03", IntegrationProposal("antipattern-plumbing-03", "Engineering-data gateway spec never reaches architecture review", False, False, "engineering", True, gateway_spec_reviewed_by_architect=False)),
    ("antipattern-selfrestraint-03", IntegrationProposal("antipattern-selfrestraint-03", "Pre-approved narrow class, but allow-list dropped in favour of trusting agent judgement", False, True, "live_process", True, pre_approved_narrow_class=True, relies_on_agent_self_restraint_only=True)),
    ("antipattern-governlater-03", IntegrationProposal("antipattern-governlater-03", "Engineering-data gateway live, governance for scope changes deferred", False, False, "engineering", True, governance_defined_upfront=False)),

    # --- combinations: multiple anti-patterns on one proposal ---
    ("combo-01", IntegrationProposal("combo-01", "Pilot wired direct, treated as a plain API, governance deferred — three anti-patterns at once", False, True, "live_process", True, is_pilot=True, pilot_uses_full_gateway=False, treats_ot_as_plain_api=True, governance_defined_upfront=False)),
    ("combo-02", IntegrationProposal("combo-02", "Shared identity plus unreviewed gateway spec on an engineering-data read", False, False, "engineering", True, shares_identity_across_boundary=True, gateway_spec_reviewed_by_architect=False)),
    ("combo-04", IntegrationProposal("combo-04", "Not-approved operational change that also relies on agent self-restraint instead of an allow-list", False, True, "live_process", False, relies_on_agent_self_restraint_only=True)),
    ("combo-05", IntegrationProposal("combo-05", "Pre-approved narrow class, nightly-eval-only, governance deferred — three issues on one operational-change proposal", False, True, "live_process", True, pre_approved_narrow_class=True, evaluation_only_nightly_batch=True, governance_defined_upfront=False)),
    ("combo-03", IntegrationProposal("combo-03", "SIS-touching proposal that also relies on agent self-restraint — rejection wins regardless", True, True, "live_process", True, relies_on_agent_self_restraint_only=True)),

    # --- clean scenarios: no anti-patterns, testing the classifier doesn't over-flag ---
    ("clean-01", IntegrationProposal("clean-01", "Well-scoped telemetry read, fully compliant, nothing to flag", False, False, "live_process", True)),
    ("clean-02", IntegrationProposal("clean-02", "Well-scoped engineering-data read, fully compliant", False, False, "engineering", True)),
    ("clean-03", IntegrationProposal("clean-03", "Well-scoped operational-change request, full gateway, human-approved, governed from the start", False, True, "live_process", True)),
    ("clean-04", IntegrationProposal("clean-04", "Pre-approved narrow-class operational change, fully compliant otherwise", False, True, "live_process", True, pre_approved_narrow_class=True)),
]


def build_tasks() -> list[dict]:
    tasks = []
    seen_ids = set()
    for task_id, proposal in SCENARIOS:
        if task_id in seen_ids:
            raise ValueError(f"duplicate task_id: {task_id}")
        seen_ids.add(task_id)
        expected = dataclasses.asdict(classify(proposal))
        tasks.append(
            {
                "task_id": task_id,
                "input": json.dumps(dataclasses.asdict(proposal)),
                "expected": expected,
            }
        )
    return tasks


def main() -> None:
    tasks = build_tasks()

    buckets: dict[str, list[dict]] = {"dev": [], "rotation": [], "held_out": []}
    for t in tasks:
        buckets[split_of(t["task_id"])].append(t)

    for name, items in buckets.items():
        out_dir = SOL_DIR / "data" / name
        out_dir.mkdir(parents=True, exist_ok=True)
        for existing in out_dir.glob("*.json"):
            existing.unlink()
        for item in items:
            (out_dir / f"{item['task_id']}.json").write_text(json.dumps(item, indent=2) + "\n")
        print(f"{name}: {len(items)} tasks")

    if not buckets["held_out"]:
        raise SystemExit("held_out split is empty — task set is too small for a safe split")


if __name__ == "__main__":
    main()

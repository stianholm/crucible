"""itot_classifier candidate. FROZEN signature: `solve(task_input: str, ctx) -> str`.

task_input is a JSON string encoding an IntegrationProposal's fields (see
solutions/itot_classifier/checks/reference.py for the field list). solve()
must classify it and return `json.dumps(result)` with at least a "gateway"
key.

Everything between the EVOLVE-BLOCK markers is the proposer's to rewrite.
This version is the hill-climb winner from the run recorded in RUN.md
(candidate 6f744ecb3b388109, parent cac1371ba01dbaff — the original
deliberately-imperfect incumbent, preserved in git history) — verified
1.0 quality on both rotation and held-out (see BASELINE.yaml). Promoted
to incumbent because, unlike the fixture, this solution isn't a permanent
regression scaffold: the whole point was a working classifier. Current
headroom is exhausted; further improvement here needs an expanded task
set (new anti-patterns, ambiguous edge cases), not a bug fix.
"""

from __future__ import annotations

import json


def solve(task_input: str, ctx=None) -> str:
    proposal = json.loads(task_input)
    result = _classify(proposal)
    return json.dumps(result)


def _classify(p: dict) -> dict:
    # EVOLVE-BLOCK-START
    # Extract fields with defaults and ensure booleans where appropriate
    touches_sis = bool(p.get("touches_sis", False))
    needs_write = bool(p.get("needs_write", False))
    within_approved_scope = bool(p.get("within_approved_scope", False))
    data_type = p.get("data_type", "engineering")
    is_pilot = bool(p.get("is_pilot", False))
    pilot_uses_full_gateway = bool(p.get("pilot_uses_full_gateway", True))
    treats_ot_as_plain_api = bool(p.get("treats_ot_as_plain_api", False))
    shares_identity_across_boundary = bool(p.get("shares_identity_across_boundary", False))
    gateway_spec_reviewed_by_architect = bool(p.get("gateway_spec_reviewed_by_architect", True))
    relies_on_agent_self_restraint_only = bool(p.get("relies_on_agent_self_restraint_only", False))
    evaluation_only_nightly_batch = bool(p.get("evaluation_only_nightly_batch", False))
    governance_defined_upfront = bool(p.get("governance_defined_upfront", True))

    # Anti‑pattern detection (order does not matter)
    anti_patterns = [
        name
        for condition, name in [
            (is_pilot and not pilot_uses_full_gateway, "pilot_direct_connect"),
            (treats_ot_as_plain_api, "just_an_api"),
            (shares_identity_across_boundary, "shared_identity"),
            (not gateway_spec_reviewed_by_architect, "gateway_is_plumbing"),
            (relies_on_agent_self_restraint_only, "agent_will_know_when_to_stop"),
            (needs_write and evaluation_only_nightly_batch, "eval_runs_nightly"),
            (not governance_defined_upfront, "we_will_govern_it_later"),
        ]
        if condition
    ]

    # Routing logic – SIS check has absolute priority
    if touches_sis:
        gateway = "safety_wall"
        approved = False
    elif needs_write:
        gateway = "operational_change"
        approved = within_approved_scope
    else:
        gateway = "telemetry" if data_type == "live_process" else "engineering_data"
        approved = within_approved_scope

    return {
        "gateway": gateway,
        "approved": approved,
        "anti_patterns_detected": anti_patterns,
    }
    # EVOLVE-BLOCK-END

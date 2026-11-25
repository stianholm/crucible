"""Ground-truth classifier for the IT/OT gateway decision procedure. See
Stian Holm, "The IT/OT Boundary as Architecture: A Pattern Language for
Agentic AI" (SSRN 6866600), Section 5 (decision criteria) and Section 9
(anti-patterns).

Used only to compute the `expected` field for the task set. Never shipped
to the proposer and never imported by candidate.py — the candidate must
reconstruct this decision procedure independently. See PHASE-1.md task
1.1's note on the evaluator never being reachable from the candidate.

Every branch below cites the paper passage it encodes, so ground truth
here is checkable against the source rather than trusted on my reading
alone.
"""

from __future__ import annotations

from dataclasses import dataclass, field

GATEWAY_TELEMETRY = "telemetry"
GATEWAY_ENGINEERING = "engineering_data"
GATEWAY_OPERATIONAL = "operational_change"
GATEWAY_SAFETY_WALL = "safety_wall"

ANTI_PATTERN_PILOT_DIRECT_CONNECT = "pilot_direct_connect"
ANTI_PATTERN_JUST_AN_API = "just_an_api"
ANTI_PATTERN_SHARED_IDENTITY = "shared_identity"
ANTI_PATTERN_GATEWAY_IS_PLUMBING = "gateway_is_plumbing"
ANTI_PATTERN_AGENT_SELF_RESTRAINT = "agent_will_know_when_to_stop"
ANTI_PATTERN_NIGHTLY_EVAL_ONLY = "eval_runs_nightly"
ANTI_PATTERN_GOVERN_LATER = "we_will_govern_it_later"


@dataclass
class IntegrationProposal:
    proposal_id: str
    description: str  # human-readable only; classification never reads this field
    touches_sis: bool  # "does the integration affect SIS, directly or indirectly" (Sec 5, step 1)
    needs_write: bool  # "does it need any write to the OT side" (Sec 5, step 2)
    data_type: str  # "live_process" | "engineering" (Sec 5, step 3)
    within_approved_scope: bool  # "is the access within scope operations has approved" (Sec 5, step 4)
    pre_approved_narrow_class: bool = False  # Sec 7's narrow closed-loop exception: gateway may act without per-action approval
    # anti-pattern indicator fields, Section 9
    is_pilot: bool = False
    pilot_uses_full_gateway: bool = True
    treats_ot_as_plain_api: bool = False
    shares_identity_across_boundary: bool = False
    gateway_spec_reviewed_by_architect: bool = True
    relies_on_agent_self_restraint_only: bool = False
    evaluation_only_nightly_batch: bool = False
    governance_defined_upfront: bool = True


@dataclass
class Classification:
    gateway: str
    approved: bool
    required_controls: list[str] = field(default_factory=list)
    anti_patterns_detected: list[str] = field(default_factory=list)
    reasoning: str = ""


def _controls_for(gateway: str, human_approval_required: bool) -> list[str]:
    # Section 4, "Four kinds of control" — identity translation, action
    # allow-list, time-window constraints, human approval — applied per
    # gateway class per Section 5's typology.
    if gateway == GATEWAY_TELEMETRY:
        return ["identity_translation_readonly", "source_scope_review", "audit_every_read", "volume_anomaly_alerting"]
    if gateway == GATEWAY_ENGINEERING:
        return ["identity_translation_readonly", "source_scope_review", "audit_every_read"]
    if gateway == GATEWAY_OPERATIONAL:
        controls = ["identity_translation_writescoped", "action_allowlist", "time_window_constraints", "signed_chain_audit"]
        if human_approval_required:
            controls.append("human_approval")
        return controls
    return []


def classify(p: IntegrationProposal) -> Classification:
    anti_patterns: list[str] = []

    # Section 9 anti-patterns — independent of gateway routing, checked
    # against the proposal's own properties regardless of outcome.
    if p.is_pilot and not p.pilot_uses_full_gateway:
        anti_patterns.append(ANTI_PATTERN_PILOT_DIRECT_CONNECT)
    if p.treats_ot_as_plain_api:
        anti_patterns.append(ANTI_PATTERN_JUST_AN_API)
    if p.shares_identity_across_boundary:
        anti_patterns.append(ANTI_PATTERN_SHARED_IDENTITY)
    if not p.gateway_spec_reviewed_by_architect:
        anti_patterns.append(ANTI_PATTERN_GATEWAY_IS_PLUMBING)
    if p.relies_on_agent_self_restraint_only:
        anti_patterns.append(ANTI_PATTERN_AGENT_SELF_RESTRAINT)
    if not p.governance_defined_upfront:
        anti_patterns.append(ANTI_PATTERN_GOVERN_LATER)

    # Section 5, step 1: "does the integration affect SIS, directly or
    # indirectly? If yes, the answer is no. Not now, not as a future
    # enhancement." Full stop — no other field changes this outcome.
    # Section 6, "The safety boundary: not a gateway" — "Agents do not
    # interact with SIS. Full stop."
    if p.touches_sis:
        return Classification(
            gateway=GATEWAY_SAFETY_WALL,
            approved=False,
            required_controls=[],
            anti_patterns_detected=anti_patterns,
            reasoning="Touches SIS, directly or indirectly. The safety boundary is a wall, not a gateway — reformulate "
            "so it does not involve SIS, or reject it.",
        )

    # Section 5, step 2: "does it need any write to the OT side? If yes,
    # route it through the operational change gateway."
    if p.needs_write:
        gateway = GATEWAY_OPERATIONAL
        # Section 7's narrow exception, Section 4's "human-in-the-loop
        # default": approval is required for every action unless the
        # operations team has explicitly pre-approved a narrow class
        # within a gateway-eligible, time-windowed context.
        human_approval_required = not p.pre_approved_narrow_class

        # Section 9, "Eval runs nightly": for operational-change actions
        # specifically, evaluating only in a nightly batch (rather than
        # pre-action, against current state) is the anti-pattern — the
        # gap between the nightly eval and the action is where the cost
        # builds up.
        if p.evaluation_only_nightly_batch:
            anti_patterns.append(ANTI_PATTERN_NIGHTLY_EVAL_ONLY)

        return Classification(
            gateway=gateway,
            approved=p.within_approved_scope,
            required_controls=_controls_for(gateway, human_approval_required),
            anti_patterns_detected=anti_patterns,
            reasoning="Needs a write to the OT side — routes through the operational change gateway, narrow by design."
            + ("" if p.within_approved_scope else " Not approved until the gateway's allow-list is widened."),
        )

    # Section 5, step 3: read-only traffic splits by data type — live
    # process data through telemetry, engineering/configuration data
    # through the engineering data gateway.
    if p.data_type == "live_process":
        gateway = GATEWAY_TELEMETRY
    elif p.data_type == "engineering":
        gateway = GATEWAY_ENGINEERING
    else:
        raise ValueError(f"unrecognised data_type: {p.data_type!r}")

    return Classification(
        gateway=gateway,
        approved=p.within_approved_scope,
        required_controls=_controls_for(gateway, human_approval_required=False),
        anti_patterns_detected=anti_patterns,
        reasoning=f"Read-only {p.data_type.replace('_', ' ')} data — routes through the {gateway.replace('_', ' ')} gateway."
        + ("" if p.within_approved_scope else " Not approved until the gateway's scope is widened."),
    )

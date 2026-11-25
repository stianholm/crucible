# Generation 0 — itot_classifier

## Throughput

- Peak queue depth: 32
- Sustained (median) queue depth: 32.0
- Prefix cache hit rate: 87.4%

## Archive

- Island 0: coverage 2.8%, QD score 0.999, unique ancestors 1
- Island 1: coverage 2.8%, QD score 0.999, unique ancestors 1
- Island 2: coverage 2.8%, QD score 0.999, unique ancestors 1
- Island 3: coverage 2.8%, QD score 0.999, unique ancestors 1
- Cells newly claimed this generation: 11

## Quality

- Best scalar this generation: 0.9991
- Median scalar of newly-claimed: 0.9990

## Cost

- Budget: {'generation': 0, 'max_generations': 20, 'tokens_used_total': 70326, 'max_tokens': 58145, 'elapsed_s_total': 138.3, 'generation_wall_s': 138.3}
- Candidates proposed: 32
- Parsed: 32 (100.0%)
- Admissible: 32 (100.0%)
- Scored: 32

## Content — newly claimed elites

### Island 0, cell (5, 5), scalar 0.9985

parent `cac1371ba01dbaff` -> candidate `bb21c4a2b5c80624`

```diff
--- parent cac1371ba01dbaff
+++ candidate bb21c4a2b5c80624
@@ -0,0 +1,37 @@
+    # Determine anti-patterns
+    anti_patterns = []
+    if p.get("is_pilot") and not p.get("pilot_uses_full_gateway", True):
+        anti_patterns.append("pilot_direct_connect")
+    if p.get("treats_ot_as_plain_api"):
+        anti_patterns.append("just_an_api")
+    if p.get("shares_identity_across_boundary"):
+        anti_patterns.append("shared_identity")
+    if not p.get("gateway_spec_reviewed_by_architect", True):
+        anti_patterns.append("gateway_is_plumbing")
+    if p.get("relies_on_agent_self_restraint_only"):
+        anti_patterns.append("agent_will_know_when_to_stop")
+    if p.get("needs_write") and p.get("evaluation_only_nightly_batch"):
+        anti_patterns.append("eval_runs_nightly")
+    if not p.get("governance_defined_upfront", True):
+        anti_patterns.append("we_will_govern_it_later")
+
+    # Routing logic (SIS check has highest priority)
+    if p.get("touches_sis"):
+        gateway = "safety_wall"
+        approved = False
+    elif p.get("needs_write"):
+        gateway = "operational_change"
+        approved = bool(p.get("within_approved_scope"))
+    else:
+        data_type = p.get("data_type")
+        if data_type == "live_process":
+            gateway = "telemetry"
+        else:
+            gateway = "engineering_data"
+        approved = bool(p.get("within_approved_scope"))
+
+    return {
+        "gateway": gateway,
+        "approved": approved,
+        "anti_patterns_detected": anti_patterns,
+    }
```

### Island 1, cell (5, 5), scalar 0.9991

parent `cac1371ba01dbaff` -> candidate `7202c4fb11581b01`

```diff
--- parent cac1371ba01dbaff
+++ candidate 7202c4fb11581b01
@@ -0,0 +1,37 @@
+    # Determine anti-patterns (order does not matter)
+    anti_patterns = []
+    if p.get("is_pilot") and not p.get("pilot_uses_full_gateway", True):
+        anti_patterns.append("pilot_direct_connect")
+    if p.get("treats_ot_as_plain_api"):
+        anti_patterns.append("just_an_api")
+    if p.get("shares_identity_across_boundary"):
+        anti_patterns.append("shared_identity")
+    if not p.get("gateway_spec_reviewed_by_architect", True):
+        anti_patterns.append("gateway_is_plumbing")
+    if p.get("relies_on_agent_self_restraint_only"):
+        anti_patterns.append("agent_will_know_when_to_stop")
+    if p.get("needs_write") and p.get("evaluation_only_nightly_batch"):
+        anti_patterns.append("eval_runs_nightly")
+    if not p.get("governance_defined_upfront", True):
+        anti_patterns.append("we_will_govern_it_later")
+
+    # Routing logic – SIS check has highest priority
+    if p.get("touches_sis"):
+        gateway = "safety_wall"
+        approved = False
+    elif p.get("needs_write"):
+        gateway = "operational_change"
+        approved = bool(p.get("within_approved_scope"))
+    else:
+        data_type = p.get("data_type")
+        if data_type == "live_process":
+            gateway = "telemetry"
+        else:
+            gateway = "engineering_data"
+        approved = bool(p.get("within_approved_scope"))
+
+    return {
+        "gateway": gateway,
+        "approved": approved,
+        "anti_patterns_detected": anti_patterns,
+    }
```

### Island 2, cell (5, 5), scalar 0.9989

parent `cac1371ba01dbaff` -> candidate `53450776bc17c48d`

```diff
--- parent cac1371ba01dbaff
+++ candidate 53450776bc17c48d
@@ -0,0 +1,36 @@
+    # Detect anti-patterns (independent of routing)
+    anti_patterns = []
+    if p.get("is_pilot", False) and not p.get("pilot_uses_full_gateway", True):
+        anti_patterns.append("pilot_direct_connect")
+    if p.get("treats_ot_as_plain_api", False):
+        anti_patterns.append("just_an_api")
+    if p.get("shares_identity_across_boundary", False):
+        anti_patterns.append("shared_identity")
+    if not p.get("gateway_spec_reviewed_by_architect", True):
+        anti_patterns.append("gateway_is_plumbing")
+    if p.get("relies_on_agent_self_restraint_only", False):
+        anti_patterns.append("agent_will_know_when_to_stop")
+    if p.get("needs_write", False) and p.get("evaluation_only_nightly_batch", False):
+        anti_patterns.append("eval_runs_nightly")
+    if not p.get("governance_defined_upfront", True):
+        anti_patterns.append("we_will_govern_it_later")
+
+    # Routing logic – strict priority, SIS check first
+    if p.get("touches_sis", False):
+        gateway = "safety_wall"
+        approved = False
+    elif p.get("needs_write", False):
+        gateway = "operational_change"
+        approved = bool(p.get("within_approved_scope", False))
+    else:
+        if p.get("data_type") == "live_process":
+            gateway = "telemetry"
+        else:
+            gateway = "engineering_data"
+        approved = bool(p.get("within_approved_scope", False))
+
+    return {
+        "gateway": gateway,
+        "approved": approved,
+        "anti_patterns_detected": anti_patterns,
+    }
```

### Island 2, cell (5, 5), scalar 0.9990

parent `cac1371ba01dbaff` -> candidate `ccd313bec134f1db`

```diff
--- parent cac1371ba01dbaff
+++ candidate ccd313bec134f1db
@@ -0,0 +1,37 @@
+    # Determine anti-patterns (independent of routing)
+    anti_patterns = []
+    if p.get("is_pilot", False) and not p.get("pilot_uses_full_gateway", False):
+        anti_patterns.append("pilot_direct_connect")
+    if p.get("treats_ot_as_plain_api", False):
+        anti_patterns.append("just_an_api")
+    if p.get("shares_identity_across_boundary", False):
+        anti_patterns.append("shared_identity")
+    if not p.get("gateway_spec_reviewed_by_architect", True):
+        anti_patterns.append("gateway_is_plumbing")
+    if p.get("relies_on_agent_self_restraint_only", False):
+        anti_patterns.append("agent_will_know_when_to_stop")
+    if p.get("needs_write", False) and p.get("evaluation_only_nightly_batch", False):
+        anti_patterns.append("eval_runs_nightly")
+    if not p.get("governance_defined_upfront", True):
+        anti_patterns.append("we_will_govern_it_later")
+
+    # Routing logic (SIS check has highest priority)
+    if p.get("touches_sis", False):
+        gateway = "safety_wall"
+        approved = False
+    elif p.get("needs_write", False):
+        gateway = "operational_change"
+        approved = bool(p.get("within_approved_scope", False))
+    else:
+        data_type = p.get("data_type")
+        if data_type == "live_process":
+            gateway = "telemetry"
+        else:
+            gateway = "engineering_data"
+        approved = bool(p.get("within_approved_scope", False))
+
+    return {
+        "gateway": gateway,
+        "approved": approved,
+        "anti_patterns_detected": anti_patterns,
+    }
```

### Island 2, cell (5, 5), scalar 0.9991

parent `cac1371ba01dbaff` -> candidate `0e061eed1e23f114`

```diff
--- parent cac1371ba01dbaff
+++ candidate 0e061eed1e23f114
@@ -0,0 +1,37 @@
+    # Detect anti-patterns (independent of routing)
+    anti_patterns = []
+    if p.get("is_pilot") and not p.get("pilot_uses_full_gateway", True):
+        anti_patterns.append("pilot_direct_connect")
+    if p.get("treats_ot_as_plain_api"):
+        anti_patterns.append("just_an_api")
+    if p.get("shares_identity_across_boundary"):
+        anti_patterns.append("shared_identity")
+    if not p.get("gateway_spec_reviewed_by_architect", True):
+        anti_patterns.append("gateway_is_plumbing")
+    if p.get("relies_on_agent_self_restraint_only"):
+        anti_patterns.append("agent_will_know_when_to_stop")
+    if p.get("needs_write") and p.get("evaluation_only_nightly_batch"):
+        anti_patterns.append("eval_runs_nightly")
+    if not p.get("governance_defined_upfront", True):
+        anti_patterns.append("we_will_govern_it_later")
+
+    # Routing and approval logic (strict priority)
+    if p.get("touches_sis"):
+        gateway = "safety_wall"
+        approved = False
+    elif p.get("needs_write"):
+        gateway = "operational_change"
+        approved = bool(p.get("within_approved_scope"))
+    else:
+        data_type = p.get("data_type")
+        if data_type == "live_process":
+            gateway = "telemetry"
+        else:
+            gateway = "engineering_data"
+        approved = bool(p.get("within_approved_scope"))
+
+    return {
+        "gateway": gateway,
+        "approved": approved,
+        "anti_patterns_detected": anti_patterns,
+    }
```

### Island 3, cell (5, 5), scalar 0.9988

parent `cac1371ba01dbaff` -> candidate `bb21c4a2b5c80624`

```diff
--- parent cac1371ba01dbaff
+++ candidate bb21c4a2b5c80624
@@ -0,0 +1,37 @@
+    # Determine anti-patterns
+    anti_patterns = []
+    if p.get("is_pilot") and not p.get("pilot_uses_full_gateway", True):
+        anti_patterns.append("pilot_direct_connect")
+    if p.get("treats_ot_as_plain_api"):
+        anti_patterns.append("just_an_api")
+    if p.get("shares_identity_across_boundary"):
+        anti_patterns.append("shared_identity")
+    if not p.get("gateway_spec_reviewed_by_architect", True):
+        anti_patterns.append("gateway_is_plumbing")
+    if p.get("relies_on_agent_self_restraint_only"):
+        anti_patterns.append("agent_will_know_when_to_stop")
+    if p.get("needs_write") and p.get("evaluation_only_nightly_batch"):
+        anti_patterns.append("eval_runs_nightly")
+    if not p.get("governance_defined_upfront", True):
+        anti_patterns.append("we_will_govern_it_later")
+
+    # Routing logic (SIS check has highest priority)
+    if p.get("touches_sis"):
+        gateway = "safety_wall"
+        approved = False
+    elif p.get("needs_write"):
+        gateway = "operational_change"
+        approved = bool(p.get("within_approved_scope"))
+    else:
+        data_type = p.get("data_type")
+        if data_type == "live_process":
+            gateway = "telemetry"
+        else:
+            gateway = "engineering_data"
+        approved = bool(p.get("within_approved_scope"))
+
+    return {
+        "gateway": gateway,
+        "approved": approved,
+        "anti_patterns_detected": anti_patterns,
+    }
```

### Island 3, cell (5, 5), scalar 0.9989

parent `cac1371ba01dbaff` -> candidate `09c66aefe77e8568`

```diff
--- parent cac1371ba01dbaff
+++ candidate 09c66aefe77e8568
@@ -0,0 +1,38 @@
+    # Determine anti-patterns
+    anti_patterns = []
+
+    if p.get("is_pilot", False) and not p.get("pilot_uses_full_gateway", True):
+        anti_patterns.append("pilot_direct_connect")
+    if p.get("treats_ot_as_plain_api", False):
+        anti_patterns.append("just_an_api")
+    if p.get("shares_identity_across_boundary", False):
+        anti_patterns.append("shared_identity")
+    if not p.get("gateway_spec_reviewed_by_architect", True):
+        anti_patterns.append("gateway_is_plumbing")
+    if p.get("relies_on_agent_self_restraint_only", False):
+        anti_patterns.append("agent_will_know_when_to_stop")
+    if p.get("needs_write", False) and p.get("evaluation_only_nightly_batch", False):
+        anti_patterns.append("eval_runs_nightly")
+    if not p.get("governance_defined_upfront", True):
+        anti_patterns.append("we_will_govern_it_later")
+
+    # Gateway routing (SIS check first)
+    if p.get("touches_sis", False):
+        gateway = "safety_wall"
+        approved = False
+    elif p.get("needs_write", False):
+        gateway = "operational_change"
+        approved = bool(p.get("within_approved_scope", False))
+    else:
+        data_type = p.get("data_type")
+        if data_type == "live_process":
+            gateway = "telemetry"
+        else:
+            gateway = "engineering_data"
+        approved = bool(p.get("within_approved_scope", False))
+
+    return {
+        "gateway": gateway,
+        "approved": approved,
+        "anti_patterns_detected": anti_patterns,
+    }
```

### Island 3, cell (5, 5), scalar 0.9989

parent `cac1371ba01dbaff` -> candidate `41b14a22c32bfa6b`

```diff
--- parent cac1371ba01dbaff
+++ candidate 41b14a22c32bfa6b
@@ -0,0 +1,37 @@
+    # Detect anti-patterns (independent of routing)
+    anti_patterns = []
+    if p.get("is_pilot") and not p.get("pilot_uses_full_gateway", True):
+        anti_patterns.append("pilot_direct_connect")
+    if p.get("treats_ot_as_plain_api"):
+        anti_patterns.append("just_an_api")
+    if p.get("shares_identity_across_boundary"):
+        anti_patterns.append("shared_identity")
+    if not p.get("gateway_spec_reviewed_by_architect", True):
+        anti_patterns.append("gateway_is_plumbing")
+    if p.get("relies_on_agent_self_restraint_only"):
+        anti_patterns.append("agent_will_know_when_to_stop")
+    if p.get("needs_write") and p.get("evaluation_only_nightly_batch"):
+        anti_patterns.append("eval_runs_nightly")
+    if not p.get("governance_defined_upfront", True):
+        anti_patterns.append("we_will_govern_it_later")
+
+    # Routing logic (SIS check first, then write, else read)
+    if p.get("touches_sis"):
+        gateway = "safety_wall"
+        approved = False
+    elif p.get("needs_write"):
+        gateway = "operational_change"
+        approved = bool(p.get("within_approved_scope"))
+    else:
+        data_type = p.get("data_type")
+        if data_type == "live_process":
+            gateway = "telemetry"
+        else:
+            gateway = "engineering_data"
+        approved = bool(p.get("within_approved_scope"))
+
+    return {
+        "gateway": gateway,
+        "approved": approved,
+        "anti_patterns_detected": anti_patterns,
+    }
```

### Island 3, cell (5, 5), scalar 0.9990

parent `cac1371ba01dbaff` -> candidate `48ca6ffd679e55de`

```diff
--- parent cac1371ba01dbaff
+++ candidate 48ca6ffd679e55de
@@ -0,0 +1,37 @@
+    # Compute anti-patterns
+    anti_patterns = []
+    if p.get("is_pilot") and not p.get("pilot_uses_full_gateway", True):
+        anti_patterns.append("pilot_direct_connect")
+    if p.get("treats_ot_as_plain_api"):
+        anti_patterns.append("just_an_api")
+    if p.get("shares_identity_across_boundary"):
+        anti_patterns.append("shared_identity")
+    if not p.get("gateway_spec_reviewed_by_architect", True):
+        anti_patterns.append("gateway_is_plumbing")
+    if p.get("relies_on_agent_self_restraint_only"):
+        anti_patterns.append("agent_will_know_when_to_stop")
+    if p.get("needs_write") and p.get("evaluation_only_nightly_batch"):
+        anti_patterns.append("eval_runs_nightly")
+    if not p.get("governance_defined_upfront", True):
+        anti_patterns.append("we_will_govern_it_later")
+
+    # Routing and approval logic (SIS check has highest priority)
+    if p.get("touches_sis"):
+        gateway = "safety_wall"
+        approved = False
+    elif p.get("needs_write"):
+        gateway = "operational_change"
+        approved = bool(p.get("within_approved_scope"))
+    else:
+        data_type = p.get("data_type")
+        if data_type == "live_process":
+            gateway = "telemetry"
+        else:
+            gateway = "engineering_data"
+        approved = bool(p.get("within_approved_scope"))
+
+    return {
+        "gateway": gateway,
+        "approved": approved,
+        "anti_patterns_detected": anti_patterns,
+    }
```

### Island 3, cell (5, 5), scalar 0.9991

parent `cac1371ba01dbaff` -> candidate `4dabb90d417f6c4a`

```diff
--- parent cac1371ba01dbaff
+++ candidate 4dabb90d417f6c4a
@@ -0,0 +1,37 @@
+    # Determine anti-patterns (independent of routing)
+    anti_patterns = []
+    if p.get("is_pilot") and not p.get("pilot_uses_full_gateway", True):
+        anti_patterns.append("pilot_direct_connect")
+    if p.get("treats_ot_as_plain_api"):
+        anti_patterns.append("just_an_api")
+    if p.get("shares_identity_across_boundary"):
+        anti_patterns.append("shared_identity")
+    if not p.get("gateway_spec_reviewed_by_architect", True):
+        anti_patterns.append("gateway_is_plumbing")
+    if p.get("relies_on_agent_self_restraint_only"):
+        anti_patterns.append("agent_will_know_when_to_stop")
+    if p.get("needs_write") and p.get("evaluation_only_nightly_batch"):
+        anti_patterns.append("eval_runs_nightly")
+    if not p.get("governance_defined_upfront", True):
+        anti_patterns.append("we_will_govern_it_later")
+
+    # Gateway routing (strict priority, SIS check first)
+    if p.get("touches_sis"):
+        gateway = "safety_wall"
+        approved = False
+    elif p.get("needs_write"):
+        gateway = "operational_change"
+        approved = bool(p.get("within_approved_scope"))
+    else:
+        data_type = p.get("data_type")
+        if data_type == "live_process":
+            gateway = "telemetry"
+        else:
+            gateway = "engineering_data"
+        approved = bool(p.get("within_approved_scope"))
+
+    return {
+        "gateway": gateway,
+        "approved": approved,
+        "anti_patterns_detected": anti_patterns,
+    }
```

### Island 3, cell (5, 5), scalar 0.9991

parent `cac1371ba01dbaff` -> candidate `18fb784c9c32fcac`

```diff
--- parent cac1371ba01dbaff
+++ candidate 18fb784c9c32fcac
@@ -0,0 +1,36 @@
+    # Detect anti‑patterns (independent of routing)
+    anti_patterns = []
+    if p.get("is_pilot") and not p.get("pilot_uses_full_gateway", False):
+        anti_patterns.append("pilot_direct_connect")
+    if p.get("treats_ot_as_plain_api"):
+        anti_patterns.append("just_an_api")
+    if p.get("shares_identity_across_boundary"):
+        anti_patterns.append("shared_identity")
+    if not p.get("gateway_spec_reviewed_by_architect", True):
+        anti_patterns.append("gateway_is_plumbing")
+    if p.get("relies_on_agent_self_restraint_only"):
+        anti_patterns.append("agent_will_know_when_to_stop")
+    if p.get("needs_write") and p.get("evaluation_only_nightly_batch"):
+        anti_patterns.append("eval_runs_nightly")
+    if not p.get("governance_defined_upfront", True):
+        anti_patterns.append("we_will_govern_it_later")
+
+    # Gateway routing (SIS check has highest priority)
+    if p.get("touches_sis"):
+        gateway = "safety_wall"
+        approved = False
+    elif p.get("needs_write"):
+        gateway = "operational_change"
+        approved = bool(p.get("within_approved_scope"))
+    else:
+        if p.get("data_type") == "live_process":
+            gateway = "telemetry"
+        else:
+            gateway = "engineering_data"
+        approved = bool(p.get("within_approved_scope"))
+
+    return {
+        "gateway": gateway,
+        "approved": approved,
+        "anti_patterns_detected": anti_patterns,
+    }
```


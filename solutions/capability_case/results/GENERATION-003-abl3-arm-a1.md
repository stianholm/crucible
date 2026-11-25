# Generation 3 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31
- Prefix cache hit rate: 70.0%
- Aggregate throughput: 92.1 tok/s (204596 completion tokens / 2220.8s)

## Archive

- Island 0: coverage 27.8%, QD score 5.932, unique ancestors 5
- Island 1: coverage 13.9%, QD score 2.882, unique ancestors 3
- Island 2: coverage 22.2%, QD score 3.463, unique ancestors 3
- Island 3: coverage 22.2%, QD score 5.306, unique ancestors 5
- Cells newly claimed this generation: 4

## Quality

- Best scalar this generation: 0.7558
- Median scalar of newly-claimed: 0.5737

## Cost

- Budget: {'generation': 3, 'max_generations': 30, 'tokens_used_total': 2460897, 'max_tokens': 3000000, 'elapsed_s_total': 9523.2, 'generation_wall_s': 2220.8}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 0, cell (1, 5), scalar 0.5947

parent `8911d13f4535b97a` -> candidate `aa4f3d7b3051d183`

```diff
--- parent 8911d13f4535b97a
+++ candidate aa4f3d7b3051d183
@@ -1,21 +1,32 @@
-You are evaluating a capability case that proposes to relax the per‑action human‑approval step for an industrial operational‑change action. Your task is to judge the case as **sound**, **needs‑more‑evidence**, or **rejected** according to Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are reviewing a proposal that seeks to remove the per‑action human‑approval requirement for an industrial operational‑change gateway. Decide whether the case is **sound**, **needs‑more‑evidence**, or **rejected** by applying the criteria below, which are drawn from Section 8 (Strategy C) and the anti‑patterns in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Evaluation criteria**
+### Review checklist
 
-1. **Real‑world testing** – Has the team performed functional, integration, and failure‑injection testing that reflects the operational environment?
-2. **Risk & failure analysis** – Are potential failure modes identified, and are mitigations or fallback controls described?
-3. **Auditability & traceability** – Is there a verifiable log or record that can reconstruct the agent’s decision‑making after the fact?
-4. **Human‑parity comparison** – Does the submission include quantitative or qualitative comparison of the agent’s decisions against human operators, showing equal or better safety/performance?
-5. **Compliance & safety safeguards** – Are regulatory constraints respected and are safety‑critical safeguards (e.g., emergency stop, manual override) retained?
+| Criterion | What to look for |
+|-----------|------------------|
+| **1. Real‑world validation** | End‑to‑end functional, integration, and failure‑injection tests performed in a production‑like environment; documented results covering normal and edge cases. |
+| **2. Risk & failure‑mode analysis** | Systematic identification of failure modes (e.g., FMEA, hazard analysis) together with concrete mitigation or fallback controls. |
+| **3. Auditability & traceability** | Immutable logs that capture each autonomous decision, its inputs, and outcomes, allowing post‑hoc reconstruction. |
+| **4. Human‑parity evidence** | Quantitative or qualitative comparison showing the automated decision is at least as safe/effective as a human operator (metrics such as accuracy, false‑positive/negative rates). |
+| **5. Anti‑pattern compliance** | Absence of the following disqualifiers (any one present forces **rejected**): <br>• Black‑box decisions without explainability.<br>• Removal of approval for actions that can cause irreversible physical impact without a safe‑state or manual override.<br>• No explicit rollback or emergency‑stop procedure.<br>• Single point of automation failure with no redundant human or system fallback.<br>• Lack of segregation of duties (design and operation by the same team). |
 
-**Decision rules**
+### Decision rules
 
-- **Sound** – All five criteria are addressed satisfactorily; evidence is robust, and no serious red‑flags are present.
-- **Needs‑more‑evidence** – One or more criteria are only partially addressed or missing, but no catastrophic issue is identified.
-- **Rejected** – Any criterion reveals a fundamental flaw (e.g., no audit trail, unmitigated safety hazard, violation of anti‑patterns) that makes the proposal unsafe or non‑compliant.
+1. **Rejected** – If any anti‑pattern in Criterion 5 is found, or if a criterion reveals a fundamental safety or compliance breach (e.g., no audit trail, unmitigated hazard).  
+2. **Sound** – All five criteria are fully satisfied with robust evidence and no red‑flags.  
+3. **Needs‑more‑evidence** – One or more of Criteria 1‑4 are only partially addressed or missing, but no anti‑pattern is present.
 
-**Output**
+### Output format
 
-Provide the verdict label (**sound**, **needs‑more‑evidence**, or **rejected**) followed by a brief explanation that cites the specific criteria that led to your decision.
+- Write the verdict word (`sound`, `needs-more-evidence`, or `rejected`) on the first line.  
+- On the next line, give a concise justification that cites the specific criterion(ia) that drove your decision.  
+- Do not add any extra headings, bullet lists, or formatting.
 
-Respond with your verdict and your reasoning.+**Example**
+
+```
+needs-more-evidence
+Partial testing (Criterion 1) and no documented rollback procedure (Criterion 5) but no outright anti‑pattern detected.
+```
+
+Proceed with the evaluation and produce your verdict followed by the brief rationale.
```

### Island 0, cell (0, 3), scalar 0.5294

parent `668a21f6566788cf` -> candidate `2018c3af5f3fc2b3`

```diff
--- parent 668a21f6566788cf
+++ candidate 2018c3af5f3fc2b3
@@ -1,20 +1,20 @@
-You are evaluating a capability case that proposes to eliminate the per‑action human‑approval step for an industrial operational‑change gateway. Using the information supplied in the case, apply the following criteria (derived from Section 8 – Strategy C and the anti‑patterns of Section 9) and produce a single verdict.
+You are to judge a capability case that proposes removing the per‑action human‑approval step for an industrial operational‑change gateway. Using the case details, assess it against the five criteria below and output a single verdict.
 
 **Criteria**
-1. **Real‑world testing** – functional, integration, and failure‑injection tests that reflect production conditions.  
-2. **Risk & mitigation** – identified failure modes, their likelihood/severity, and concrete mitigations or fallback controls.  
-3. **Auditability** – immutable logging or equivalent that enables full post‑action reconstruction.  
-4. **Human‑parity evidence** – quantitative or qualitative proof that the automated decision is at least as safe/reliable as a qualified human.  
-5. **Anti‑pattern check** – confirm that none of the Section 9 anti‑patterns (e.g., uncontrolled single point of automation, missing safe‑stop, unbounded scope, unchecked escalation, lack of rollback) are present.
+1. **Real‑world testing** – functional, integration and fault‑injection tests that mimic production use.  
+2. **Risk & mitigation** – clear enumeration of failure modes, their likelihood/severity, and concrete mitigations or fallback controls.  
+3. **Auditability** – immutable logging or equivalent that enables full reconstruction of each automated decision.  
+4. **Human‑parity evidence** – quantitative or qualitative proof that the automation is at least as safe/reliable as a qualified human operator.  
+5. **Anti‑pattern absence** – confirm none of the Section 9 anti‑patterns (e.g., uncontrolled single point of automation, missing safe‑stop, unchecked escalation, unbounded scope, lack of rollback) are present.
 
-**Decision hierarchy**
-- If any anti‑pattern (criterion 5) is detected → **rejected**.  
-- Else if criteria 1‑4 are all fully satisfied with strong evidence → **sound**.  
+**Decision rules**
+- If any anti‑pattern is found (criterion 5) → **rejected**.  
+- Else if criteria 1‑4 are each fully satisfied with strong evidence → **sound**.  
 - Otherwise → **needs‑more‑evidence**.
 
-**Output format (exactly two lines, no extra text)**
+**Output (exactly two lines, no extra text)**
 ```
 Verdict: <sound|needs-more-evidence|rejected>
-Reasoning: <brief explanation citing the criteria numbers or names that determined the verdict>
+Reasoning: <brief explanation that cites the relevant criterion numbers or names that led to the verdict>
 ```
-Reference the relevant criteria in your reasoning (e.g., “Missing auditability (3)”, “Partial testing (1)”, “Anti‑pattern detected (5)”). Do not add any other content. +Reference the criteria in the reasoning (e.g., “Missing auditability (3)”, “Anti‑pattern detected (5)”, “Partial testing (1)”).
```

### Island 0, cell (0, 4), scalar 0.5527

parent `668a21f6566788cf` -> candidate `408da3ba8bc70f49`

```diff
--- parent 668a21f6566788cf
+++ candidate 408da3ba8bc70f49
@@ -1,20 +1,20 @@
-You are evaluating a capability case that proposes to eliminate the per‑action human‑approval step for an industrial operational‑change gateway. Using the information supplied in the case, apply the following criteria (derived from Section 8 – Strategy C and the anti‑patterns of Section 9) and produce a single verdict.
+You are reviewing a proposal that seeks to drop the per‑action human‑approval requirement for an industrial operational‑change gateway. Examine the case file and decide whether the proposal is **sound**, **needs‑more‑evidence**, or **rejected** by applying the five mandatory checks below (taken from Section 8 – Strategy C and the anti‑pattern list in Section 9).
 
-**Criteria**
-1. **Real‑world testing** – functional, integration, and failure‑injection tests that reflect production conditions.  
-2. **Risk & mitigation** – identified failure modes, their likelihood/severity, and concrete mitigations or fallback controls.  
-3. **Auditability** – immutable logging or equivalent that enables full post‑action reconstruction.  
-4. **Human‑parity evidence** – quantitative or qualitative proof that the automated decision is at least as safe/reliable as a qualified human.  
-5. **Anti‑pattern check** – confirm that none of the Section 9 anti‑patterns (e.g., uncontrolled single point of automation, missing safe‑stop, unbounded scope, unchecked escalation, lack of rollback) are present.
+**Mandatory checks**
+1. **Real‑world testing** – evidence of functional, integration and failure‑injection tests that emulate production conditions, including edge cases.  
+2. **Risk analysis & mitigation** – clear identification of failure modes, their likelihood/severity, and concrete mitigations or fallback controls.  
+3. **Audit trail** – immutable logging or equivalent that permits full reconstruction of each automated decision.  
+4. **Human‑parity evidence** – quantitative or qualitative proof that the automation matches or exceeds the safety/reliability of a qualified human operator.  
+5. **Anti‑pattern compliance** – confirmation that none of the Section 9 anti‑patterns (e.g., uncontrolled single point of automation, missing safe‑stop, unbounded scope, unchecked escalation, absence of rollback) are present.
 
-**Decision hierarchy**
-- If any anti‑pattern (criterion 5) is detected → **rejected**.  
-- Else if criteria 1‑4 are all fully satisfied with strong evidence → **sound**.  
+**Decision rules**
+- If any violation of check 5 is found → **rejected**.  
+- Else, if checks 1‑4 are each satisfied with strong, documented evidence → **sound**.  
 - Otherwise → **needs‑more‑evidence**.
 
-**Output format (exactly two lines, no extra text)**
+**Required output (exactly two lines, no additional text)**
 ```
 Verdict: <sound|needs-more-evidence|rejected>
-Reasoning: <brief explanation citing the criteria numbers or names that determined the verdict>
+Reasoning: <brief justification citing the relevant check numbers or names that led to the verdict>
 ```
-Reference the relevant criteria in your reasoning (e.g., “Missing auditability (3)”, “Partial testing (1)”, “Anti‑pattern detected (5)”). Do not add any other content. +Reference the specific checks in your reasoning (e.g., “Missing audit trail (3)”, “Partial testing (1)”, “Anti‑pattern detected (5)”). 
```

### Island 3, cell (1, 4), scalar 0.7558

parent `5c5c1c28d69630da` -> candidate `44f2ab0e448db868`

```diff
--- parent 5c5c1c28d69630da
+++ candidate 44f2ab0e448db868
@@ -1,20 +1,18 @@
-You act as an independent reviewer for a capability case that seeks to waive the per‑action human‑approval gate on an industrial operational‑change action. Examine the supplied evidence and then produce **exactly two lines**:
+You are an independent reviewer evaluating a capability case that requests removal of the per‑action human‑approval gate for an industrial operational‑change action. Using the checklist below, decide and output exactly two lines:
 
-1. **Verdict line** – write one of the three tokens **sound**, **needs-more-evidence**, or **rejected** (lower‑case, no extra text).  
-2. **Rationale line** – a concise (1‑3 sentence) explanation that cites the specific checklist items that led to your decision.
+Line 1: one of the tokens sound, needs-more-evidence, rejected — nothing else.  
+Line 2: a brief (1‑2 sentence) justification that references the specific checklist items (by name) that support your decision.
 
-Use the following checklist, derived from Section 8 (Strategy C) and the anti‑pattern list in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper:
+Checklist (all must be considered):
+- Testing: end‑to‑end, production‑like trials with documented scope, repeatability and results.  
+- Failure analysis: identified realistic failure modes and defined fail‑safe or rollback mitigation.  
+- Auditability: immutable log/trace that can reconstruct the automated decision and context.  
+- Human benchmark: comparison with qualified human decisions showing equal or better safety/quality.  
+- Anti‑pattern check: none of the Section 9 anti‑patterns (no fallback, opaque logic, single‑point delegation, unchecked authority escalation, etc.) are present.
 
-* **Testing** – Has the team run end‑to‑end, production‑like trials with documented scope, repeatability, and results?  
-* **Failure analysis** – Are realistic failure modes (sensor loss, network split, unexpected agent behavior, etc.) identified and mitigated with fail‑safe or rollback procedures?  
-* **Auditability** – Is there an immutable log or trace that can reconstruct the automated decision and its context?  
-* **Human benchmark** – Does the case compare the automated outcomes to a qualified human operator’s decisions, showing equal or better safety/quality?  
-* **Anti‑pattern check** – Verify that none of the Section 9 anti‑patterns (e.g., no fallback, opaque logic, single‑point delegation, unchecked authority escalation) appear.
+Decision criteria:
+- sound: every checklist item is satisfactorily met and no anti‑pattern is found.  
+- needs-more-evidence: at least one item is addressed but lacks sufficient detail, data or justification; no fatal flaw detected.  
+- rejected: a critical item is missing or an anti‑pattern is evident, making the proposal unsafe or non‑compliant.
 
-**Decision rules**
-
-* **sound** – every checklist item is satisfied at a level that convincingly demonstrates the capability can replace human approval, and no anti‑patterns are present.  
-* **needs-more-evidence** – one or more items are addressed but lack depth, data, or clear justification; no fatal flaw is found.  
-* **rejected** – a critical item is missing or an anti‑pattern is evident, making the proposal unsafe or non‑compliant.
-
-Follow the two‑line output format exactly; do not add headings, markup, or extra text.+Produce only the two lines as described; do not add headings, bullet symbols, or any other text.
```


## Lesson retirement (dry run)

- Lesson 15: **RETIRED** — precision 0.115 vs base 0.482, 9.7 sigma below
- Lesson 17: **kept** — precision 0.986 >= base 0.694
- Lesson 19: **kept** — precision 0.983 >= base 0.881
- Lesson 11: **kept** — precision 0.750 vs base 0.918, only 0.8 sigma below

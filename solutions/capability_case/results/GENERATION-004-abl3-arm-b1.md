# Generation 4 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 28.0
- Prefix cache hit rate: 69.7%
- Aggregate throughput: 68.8 tok/s (223824 completion tokens / 3253.5s)

## Archive

- Island 0: coverage 27.8%, QD score 5.091, unique ancestors 2
- Island 1: coverage 5.6%, QD score 1.490, unique ancestors 1
- Island 2: coverage 19.4%, QD score 5.025, unique ancestors 2
- Island 3: coverage 22.2%, QD score 3.680, unique ancestors 4
- Cells newly claimed this generation: 5

## Quality

- Best scalar this generation: 0.6290
- Median scalar of newly-claimed: 0.5283

## Cost

- Budget: {'generation': 4, 'max_generations': 30, 'tokens_used_total': 3354251, 'max_tokens': 3000000, 'elapsed_s_total': 12179.0, 'generation_wall_s': 3253.5}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 0, cell (1, 2), scalar 0.3715

parent `762bd0df24e8f1dd` -> candidate `8887f2aa48c61218`

```diff
--- parent 762bd0df24e8f1dd
+++ candidate 8887f2aa48c61218
@@ -1,36 +1,36 @@
-You are reviewing a capability case that seeks to relax per‑action human approval for an industrial operational‑change gateway action. Your assessment must be consistent with **Section 8 (Strategy C, capability‑based opening)** and must not exhibit any anti‑patterns from **Section 9** of the ITOT‑boundary‑as‑architecture whitepaper.
+You are evaluating a capability case that proposes to remove per‑action human approval for an industrial operational‑change gateway action. Your judgment must follow **Section 8 (Strategy C, capability‑based opening)** and must not contain any of the anti‑patterns listed in **Section 9** of the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Allowed verdicts (pick exactly one word):**
+**Possible verdicts (choose exactly one word):**
 - **sound**
 - **needs‑more‑evidence**
 - **rejected**
 
-**Evidence checklist (each item must be addressed in the submission):**
-1. **Real‑world testing** – Controlled field trials or high‑fidelity simulations that reflect production conditions. State scope, duration, and quantitative outcomes.  
-2. **Failure‑mode & risk analysis** – “What‑if” analysis covering plausible faults, worst‑case impacts, likelihood estimates, and mitigations or fallback strategies.  
-3. **Auditability & traceability** – Tamper‑evident logs, decision provenance, timestamps, and real‑time monitoring enabling forensic review.  
-4. **Human‑baseline comparison** – Direct quantitative comparison of the automated decisions with those of qualified humans (e.g., accuracy, false‑positive/negative rates).  
-5. **Governance definition** – Clear description of who governs the relaxation, how periodic reviews and stakeholder sign‑offs are performed, and how deviations are handled.
+**Evidence dimensions (all must be addressed):**
+1. **Real‑world testing** – controlled field trial or high‑fidelity simulation; include scope, duration, and quantitative results.  
+2. **Failure‑mode & risk analysis** – list plausible faults, estimate likelihood, describe worst‑case impact, and provide concrete mitigation or rollback steps.  
+3. **Auditability & traceability** – immutable logs, decision provenance, timestamps, and a mechanism for forensic review.  
+4. **Human‑baseline comparison** – quantitative comparison (accuracy, false‑positive/negative rates, etc.) between the automated decision and a qualified human.  
+5. **Governance definition** – who governs the relaxation, review cadence, stakeholder sign‑offs, and an explicit human‑override path for emergent situations.
 
-**Anti‑pattern check (Section 9)** – The submission must **not** contain any of the following without full remediation:
-- Black‑box control with no observable rationale  
-- Missing rollback or safe‑stop mechanism  
-- Unbounded scope affecting out‑of‑boundary systems  
-- Absence of explicit safety constraints for safety‑critical assets  
-- No explicit human‑override path in emergent situations  
-- Lack of defined governance (or “we will govern it later”)  
+**Anti‑patterns (any occurrence forces **rejected**):**
+- Black‑box control with no observable rationale.  
+- No rollback, safe‑stop, or emergency‑override mechanism.  
+- Unbounded scope that can affect out‑of‑boundary systems.  
+- Missing explicit safety constraints for safety‑critical assets.  
+- Absence of a manual‑override path in emergent situations.  
+- Governance deferred (“we will govern it later”) or otherwise undefined.
 
-**Decision hierarchy**
+**Decision procedure**
+1. **Anti‑pattern check** – if any anti‑pattern is present → **rejected** (stop).  
+2. **Presence check** – if any of items 1‑5 is completely absent → **rejected**.  
+3. **Sufficiency check** – if all items are present but one or more lack required detail (e.g., no quantitative results, missing likelihood estimate, incomplete audit data) → **needs‑more‑evidence**.  
+4. If all items are fully satisfied and no anti‑patterns were found → **sound**.
 
-1. **Reject** if **any** anti‑pattern is present *or* if **any** checklist item (1‑5) is **completely absent** (no evidence at all).  
-2. **Needs‑more‑evidence** if all five items are present but at least one is **insufficiently detailed** (e.g., missing quantitative results, vague risk enumeration, limited audit data) and no anti‑pattern is detected.  
-3. **Sound** if items 1‑5 are **fully satisfied** (complete, robust, and documented) and no anti‑pattern applies.
-
-**Output format (must be followed exactly)**
+**Output format (exactly two lines)**  
 
 ```
 <verdict>
-<concise reasoning paragraph that cites the specific checklist items influencing the decision>
+<single concise paragraph citing the checklist items that determined the verdict>
 ```
 
-The paragraph should reference the relevant items, e.g., “Item 2 lacks a likelihood estimate” or “No anti‑pattern from the Section 9 list was found”. Apply the checklist rigorously and return only the two‑line response.+The paragraph must reference the relevant item numbers (e.g., “Item 2 lacks a likelihood estimate” or “No anti‑pattern from Section 9 was found”). Return only the two‑line response.  
```

### Island 2, cell (1, 3), scalar 0.5438

parent `342d1ee7e447ba85` -> candidate `e35e77ae5480eba1`

```diff
--- parent 342d1ee7e447ba85
+++ candidate e35e77ae5480eba1
@@ -1,21 +1,19 @@
-You are an auditor evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action.
+You are an auditor assessing a proposal that seeks to remove per‑action human approval for an industrial operational‑change gateway.
 
-**Checklist (derived from Sections 8 & 9 of the ITOT‑boundary‑as‑architecture whitepaper)**  
+**Evaluation criteria (derived from Sections 8 & 9 of the IT‑OT boundary whitepaper)**  
 
-1. **Empirical validation** – concrete test or simulation results (including edge‑case and failure‑mode scenarios).  
-2. **Risk analysis** – documented failure‑mode analysis covering safety, security and operational impact, with mitigation for each risk.  
-3. **Auditability** – immutable audit trail or provenance data that can be inspected after every automated decision.  
-4. **Human‑baseline comparison** – quantitative or qualitative evidence that the autonomous decision matches or exceeds a qualified human operator.  
-5. **Anti‑pattern compliance** – the proposal must contain **none** of the disallowed patterns listed in Section 9 (e.g., black‑box control without fallback, unbounded autonomy, implicit revocation, “govern later”, etc.).
+1. **Empirical evidence** – documented test, pilot or simulation results, including normal operation, edge cases and failure‑mode behavior.  
+2. **Risk analysis** – a complete failure‑mode study that identifies safety, security and operational impacts and lists concrete mitigations.  
+3. **Auditability** – an immutable log or provenance mechanism that can be inspected after each automated decision.  
+4. **Human‑baseline** – quantitative or qualitative proof that the automated decision is at least as good as a qualified human operator.  
+5. **Anti‑pattern check** – the submission must contain **no** prohibited patterns from Section 9 (e.g., black‑box control without fallback, unlimited autonomy, implicit revocation, “govern‑later”, etc.).
 
-**Decision hierarchy**
+**Decision rules**
 
-1. **Reject** immediately if any anti‑pattern from #5 is present **or** if any of the mandatory evidence items #1‑#4 are completely absent (no test results, no failure‑mode analysis, no audit trail, no baseline comparison).  
-2. If no anti‑pattern and all four evidence items are present but one or more are only partially addressed or lack sufficient detail, classify as **needs‑more‑evidence**.  
-3. If all five checklist items are satisfactorily addressed, classify as **sound**.
+- **Reject** if any anti‑pattern (criterion 5) is found **or** if any of criteria 1‑4 are entirely missing.  
+- **Needs‑more‑evidence** if all criteria are present but one or more of 1‑4 are only partially satisfied or lack required detail.  
+- **Sound** only when every criterion (1‑5) is fully satisfied.
 
-**Output format**
+**Output requirement**
 
-Produce a single line containing the verdict (`sound`, `needs-more-evidence`, or `rejected`) followed by a brief justification (1‑2 sentences) that cites the most relevant checklist item(s).
-
-Do not add any other text or formatting. +Write a single line that starts with the verdict (`sound`, `needs-more-evidence`, or `rejected`) followed by a brief justification (1‑2 sentences) that references the most relevant criterion(ia). Do not include any other text or formatting. 
```

### Island 2, cell (1, 3), scalar 0.6290

parent `342d1ee7e447ba85` -> candidate `25edd46b76506422`

```diff
--- parent 342d1ee7e447ba85
+++ candidate 25edd46b76506422
@@ -1,21 +1,19 @@
-You are an auditor evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action.
+You act as an auditor for a capability case that seeks to waive per‑action human approval on an industrial operational‑change gateway.
 
-**Checklist (derived from Sections 8 & 9 of the ITOT‑boundary‑as‑architecture whitepaper)**  
+**Evaluation criteria (Sections 8 & 9 of the IT/OT‑boundary‑as‑architecture whitepaper)**  
 
-1. **Empirical validation** – concrete test or simulation results (including edge‑case and failure‑mode scenarios).  
-2. **Risk analysis** – documented failure‑mode analysis covering safety, security and operational impact, with mitigation for each risk.  
-3. **Auditability** – immutable audit trail or provenance data that can be inspected after every automated decision.  
-4. **Human‑baseline comparison** – quantitative or qualitative evidence that the autonomous decision matches or exceeds a qualified human operator.  
-5. **Anti‑pattern compliance** – the proposal must contain **none** of the disallowed patterns listed in Section 9 (e.g., black‑box control without fallback, unbounded autonomy, implicit revocation, “govern later”, etc.).
+1. **Empirical data** – documented test, pilot or simulation results, covering normal operation, edge cases and failure‑mode behavior.  
+2. **Failure‑mode risk study** – analysis of safety, security and operational impacts together with concrete mitigation measures.  
+3. **Traceability** – an immutable audit log or provenance record that can be inspected after each automated decision.  
+4. **Human benchmark** – quantitative or qualitative evidence that the automated action meets or exceeds the performance of a qualified human operator.  
+5. **Anti‑pattern screening** – the proposal must contain **none** of the prohibited patterns listed in Section 9 (e.g., black‑box control without fallback, unlimited autonomy, implicit revocation, “govern‑later”, etc.).
 
-**Decision hierarchy**
+**Decision logic**  
 
-1. **Reject** immediately if any anti‑pattern from #5 is present **or** if any of the mandatory evidence items #1‑#4 are completely absent (no test results, no failure‑mode analysis, no audit trail, no baseline comparison).  
-2. If no anti‑pattern and all four evidence items are present but one or more are only partially addressed or lack sufficient detail, classify as **needs‑more‑evidence**.  
-3. If all five checklist items are satisfactorily addressed, classify as **sound**.
+- **Reject** if any anti‑pattern (criterion 5) is present **or** if any of criteria 1‑4 are completely missing.  
+- **Needs‑more‑evidence** if no anti‑pattern exists, all four evidence criteria are provided, but at least one is only partially addressed or lacks required detail.  
+- **Sound** only when every criterion 1‑5 is fully satisfied.
 
-**Output format**
+**Output requirement**  
 
-Produce a single line containing the verdict (`sound`, `needs-more-evidence`, or `rejected`) followed by a brief justification (1‑2 sentences) that cites the most relevant checklist item(s).
-
-Do not add any other text or formatting. +Produce a single line containing the verdict (`sound`, `needs-more-evidence`, or `rejected`) followed by a brief justification (1–2 sentences) that references the most relevant criterion/criteria. No other text or formatting may be added.  
```

### Island 2, cell (0, 1), scalar 0.5283

parent `342d1ee7e447ba85` -> candidate `c2426167f93e2943`

```diff
--- parent 342d1ee7e447ba85
+++ candidate c2426167f93e2943
@@ -1,21 +1,16 @@
-You are an auditor evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action.
+You are an auditor reviewing a request to waive per‑action human approval for an industrial operational‑change gateway.
 
-**Checklist (derived from Sections 8 & 9 of the ITOT‑boundary‑as‑architecture whitepaper)**  
+**Evaluation checklist (based on Sections 8 & 9 of the IT/OT‑boundary‑as‑architecture whitepaper)**  
+1. **Empirical evidence** – Includes test, simulation, or pilot results that cover normal operation, edge cases, and failure modes.  
+2. **Risk assessment** – Provides a documented failure‑mode analysis with safety, security, and operational impacts plus mitigation actions.  
+3. **Auditability** – Supplies immutable logs or provenance data allowing reconstruction of every automated decision.  
+4. **Human‑baseline comparison** – Shows, quantitatively or qualitatively, that the automated action meets or exceeds the performance of a qualified human operator.  
+5. **Anti‑pattern check** – Confirms that none of the prohibited patterns from Section 9 appear (e.g., opaque control without fallback, unbounded autonomy, implicit revocation, “govern‑later”, etc.).
 
-1. **Empirical validation** – concrete test or simulation results (including edge‑case and failure‑mode scenarios).  
-2. **Risk analysis** – documented failure‑mode analysis covering safety, security and operational impact, with mitigation for each risk.  
-3. **Auditability** – immutable audit trail or provenance data that can be inspected after every automated decision.  
-4. **Human‑baseline comparison** – quantitative or qualitative evidence that the autonomous decision matches or exceeds a qualified human operator.  
-5. **Anti‑pattern compliance** – the proposal must contain **none** of the disallowed patterns listed in Section 9 (e.g., black‑box control without fallback, unbounded autonomy, implicit revocation, “govern later”, etc.).
+**Decision rules**  
+- **Reject** if any anti‑pattern (item 5) is found **or** if any of items 1‑4 are completely missing.  
+- **Needs‑more‑evidence** if all items are present but one or more of items 1‑4 are only partially satisfied or lack sufficient detail.  
+- **Sound** only when every checklist item is fully addressed and no anti‑patterns exist.
 
-**Decision hierarchy**
-
-1. **Reject** immediately if any anti‑pattern from #5 is present **or** if any of the mandatory evidence items #1‑#4 are completely absent (no test results, no failure‑mode analysis, no audit trail, no baseline comparison).  
-2. If no anti‑pattern and all four evidence items are present but one or more are only partially addressed or lack sufficient detail, classify as **needs‑more‑evidence**.  
-3. If all five checklist items are satisfactorily addressed, classify as **sound**.
-
-**Output format**
-
-Produce a single line containing the verdict (`sound`, `needs-more-evidence`, or `rejected`) followed by a brief justification (1‑2 sentences) that cites the most relevant checklist item(s).
-
-Do not add any other text or formatting. +**Output requirement**  
+Return a single line: first the verdict (`sound`, `needs-more-evidence`, or `rejected`), then a brief justification (1‑2 sentences) that cites the relevant checklist number(s). Do not add any other text or formatting.
```

### Island 3, cell (1, 4), scalar 0.4797

parent `f296d8d3e9bf630c` -> candidate `b8e03e9eae3b204f`

```diff
--- parent f296d8d3e9bf630c
+++ candidate b8e03e9eae3b204f
@@ -1,26 +1,27 @@
-You are reviewing a capability case that seeks to waive the per‑action human‑approval step for an operational‑change gateway action in an industrial environment.
+You are reviewing a capability case that proposes waiving the per‑action human‑approval step for an operational‑change gateway action in an industrial environment.
 
-**Goal**: After reading the submission, output a single verdict—**sound**, **needs‑more‑evidence**, or **rejected**—and a concise justification.
+**Goal** – After reading the submission, produce a two‑line answer:
 
-**Checklist (derived from Section 8 “Strategy C, capability‑based opening” and Section 9 anti‑patterns)**  
-
-1. **Real‑world testing** – Evidence of end‑to‑end, representative tests (including failure‑injection or edge‑case scenarios) and documented results.  
-2. **Risk & failure‑mode analysis** – A systematic hazard/failure‑modes assessment with clear mitigation or rollback strategies.  
-3. **Auditability & traceability** – Tamper‑evident logging, provenance data, and a replayable audit trail for post‑action review.  
-4. **Human‑benchmark comparison** – Quantitative comparison of the automated decisions against expert human decisions (e.g., accuracy, false‑positive/negative rates).  
-5. **Anti‑pattern compliance** – Confirmation that none of the prohibited patterns from Section 9 appear (e.g., unbounded autonomy, opaque reasoning, missing fail‑safe, no monitoring/override). Any violation **automatically triggers a “rejected” verdict**.  
-6. **Governance & rollback** – Defined automated rollback or human‑override path, continuous monitoring, and a clear remediation plan.
-
-**Decision hierarchy**  
-
-- **sound** – All six items are *fully* satisfied with concrete evidence and the evidence meets a reasonable confidence threshold.  
-- **rejected** – Any checklist item is *completely missing* or fails to meet the minimum requirement **or** any anti‑pattern from item 5 is present.  
-- **needs‑more‑evidence** – All items are present, but one or more are only partially addressed (e.g., testing is described but lacks representative coverage, risk analysis is superficial, audit logs are mentioned but not proven tamper‑proof, etc.). The submission shows promise but does not yet provide sufficient confidence for approval.
-
-**Output format (must match the surrounding template exactly)**  
 ```
 Verdict: <sound|needs-more-evidence|rejected>
 Reasoning: <concise explanation that cites the relevant checklist items>
 ```
 
-In your reasoning, explicitly mention which checklist items support the chosen verdict and which (if any) are lacking or problematic. Use clear, professional language and keep the explanation brief. +**Checklist** (derived from Section 8 “Strategy C, capability‑based opening” and Section 9 anti‑patterns)
+
+| # | Requirement | Critical? | What counts as “Met” |
+|---|-------------|-----------|----------------------|
+| 1 | **Real‑world testing** – end‑to‑end, production‑like runs including edge‑cases and failure‑injection, with documented results. | Yes | Concrete test reports covering representative scenarios. |
+| 2 | **Risk & failure‑mode analysis** – systematic hazard/FMEA with clear mitigation, rollback or safe‑state strategies. | Yes | A complete analysis that identifies risks and defines validated mitigations. |
+| 3 | **Auditability & traceability** – tamper‑evident logging, provenance data, and a replayable audit trail for post‑action review. | Yes | Evidence that logs cannot be altered and can be audited. |
+| 4 | **Human‑benchmark comparison** – quantitative comparison of the automated decisions against expert human decisions (accuracy, false‑positive/negative rates, etc.). | Yes | Results showing the automated performance meets or exceeds the agreed threshold. |
+| 5 | **Governance & rollback** – defined automated rollback or human‑override path, continuous monitoring, and a remediation plan. | No | Any workable rollback/override and monitoring scheme. |
+| 6 | **Anti‑pattern compliance** – confirmation that none of the Section 9 anti‑patterns appear (e.g., unbounded autonomy, opaque reasoning, missing fail‑safe, “governance later”). | No | Explicit statement that each anti‑pattern is absent or fully mitigated. **If any anti‑pattern is present without mitigation, verdict is automatically “rejected”.** |
+
+**Decision rules**
+
+* **Rejected** – Any **critical** item (1‑4) is **missing** or **not met**, **or** any anti‑pattern (item 6) is present without mitigation.
+* **Needs‑more‑evidence** – All critical items are present but at least one is only **partially met** (e.g., testing lacks edge‑cases, risk analysis is superficial, audit logs are mentioned but not proven tamper‑evident, benchmark data is incomplete). Non‑critical items (5‑6) may also be partially met, provided no anti‑pattern is unmitigated.
+* **Sound** – Every checklist item (1‑6) is **fully met** with concrete, verifiable evidence and no anti‑pattern violations.
+
+When writing the reasoning, explicitly reference the checklist numbers that support your verdict (e.g., “Item 2 missing risk analysis – reject” or “Item 5 partially defined – needs‑more‑evidence”). Keep the explanation brief and professional.
```


## Lesson retirement (dry run)

- Lesson 15: **RETIRED** — precision 0.120 vs base 0.482, 9.7 sigma below
- Lesson 19: **kept** — precision 0.986 >= base 0.881
- Lesson 17: **kept** — precision 0.986 >= base 0.694
- Lesson 11: **kept** — precision 0.750 vs base 0.927, only 0.8 sigma below

## Held-out check (best-ever candidate)

- Candidate: `342d1ee7e447ba85` (rotation scalar 0.8587)
- Held-out quality: 0.9568 (passes: 0.9666, 0.9470)
- Held-out scalar: 0.8375 (passes: 0.8453, 0.8296)
- All held-out tasks valid: True

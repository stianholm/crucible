# Generation 2 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 30.5
- Prefix cache hit rate: 69.9%
- Aggregate throughput: 99.4 tok/s (233230 completion tokens / 2347.4s)

## Archive

- Island 0: coverage 25.0%, QD score 4.350, unique ancestors 3
- Island 1: coverage 5.6%, QD score 1.433, unique ancestors 2
- Island 2: coverage 13.9%, QD score 3.865, unique ancestors 2
- Island 3: coverage 22.2%, QD score 3.296, unique ancestors 4
- Cells newly claimed this generation: 11

## Quality

- Best scalar this generation: 0.8556
- Median scalar of newly-claimed: 0.6073

## Cost

- Budget: {'generation': 2, 'max_generations': 30, 'tokens_used_total': 1987241, 'max_tokens': 3000000, 'elapsed_s_total': 6490.8, 'generation_wall_s': 2347.4}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 0, cell (1, 4), scalar 0.3667

parent `ebf462e4e1c5e1e0` -> candidate `762bd0df24e8f1dd`

```diff
--- parent ebf462e4e1c5e1e0
+++ candidate 762bd0df24e8f1dd
@@ -1,28 +1,30 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Your judgment must follow **Section 8 (Strategy C, capability‑based opening)** and the anti‑patterns listed in **Section 9** of the ITOT‑boundary‑as‑architecture whitepaper.
+You are reviewing a capability case that seeks to relax per‑action human approval for an industrial operational‑change gateway action. Your assessment must be consistent with **Section 8 (Strategy C, capability‑based opening)** and must not exhibit any anti‑patterns from **Section 9** of the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Allowed verdicts (use exactly one word):**
+**Allowed verdicts (pick exactly one word):**
 - **sound**
 - **needs‑more‑evidence**
 - **rejected**
 
-**Checklist**
+**Evidence checklist (each item must be addressed in the submission):**
+1. **Real‑world testing** – Controlled field trials or high‑fidelity simulations that reflect production conditions. State scope, duration, and quantitative outcomes.  
+2. **Failure‑mode & risk analysis** – “What‑if” analysis covering plausible faults, worst‑case impacts, likelihood estimates, and mitigations or fallback strategies.  
+3. **Auditability & traceability** – Tamper‑evident logs, decision provenance, timestamps, and real‑time monitoring enabling forensic review.  
+4. **Human‑baseline comparison** – Direct quantitative comparison of the automated decisions with those of qualified humans (e.g., accuracy, false‑positive/negative rates).  
+5. **Governance definition** – Clear description of who governs the relaxation, how periodic reviews and stakeholder sign‑offs are performed, and how deviations are handled.
 
-1. **Real‑world testing** – Controlled field trials or simulations that mirror the production environment. Provide scope, duration, and results.
-2. **Failure‑mode & risk analysis** – Documented “what‑if” analysis covering plausible faults, worst‑case impacts, likelihood, and mitigation.
-3. **Auditability & traceability** – Immutable logs, provenance data, or equivalent that enable post‑action forensic review.
-4. **Human‑baseline comparison** – Quantitative or qualitative benchmarking of the agent’s decisions against those of a qualified human (e.g., accuracy, false‑positive/negative rates).
-5. **Anti‑pattern compliance (Section 9)** – Ensure none of the following appear (or are fully mitigated):
-   - Black‑box control with no observable rationale  
-   - Missing rollback or safe‑stop mechanism  
-   - Unbounded scope affecting out‑of‑boundary systems  
-   - Absence of explicit safety constraints for safety‑critical assets  
-   - No explicit human‑override path in emergent situations  
+**Anti‑pattern check (Section 9)** – The submission must **not** contain any of the following without full remediation:
+- Black‑box control with no observable rationale  
+- Missing rollback or safe‑stop mechanism  
+- Unbounded scope affecting out‑of‑boundary systems  
+- Absence of explicit safety constraints for safety‑critical assets  
+- No explicit human‑override path in emergent situations  
+- Lack of defined governance (or “we will govern it later”)  
 
 **Decision hierarchy**
 
-1. **Reject immediately** if any anti‑pattern from item 5 is present, *or* if any of items 1‑4 is **completely absent** (i.e., no evidence at all for that dimension).  
-2. If all four evidence items are present but at least one is **insufficiently detailed** (e.g., missing quantitative results, incomplete risk enumeration, limited audit data), and no anti‑pattern is found, verdict = **needs‑more‑evidence**.  
-3. If items 1‑4 are **fully satisfied** (complete, robust, and documented) and no anti‑pattern applies, verdict = **sound**.
+1. **Reject** if **any** anti‑pattern is present *or* if **any** checklist item (1‑5) is **completely absent** (no evidence at all).  
+2. **Needs‑more‑evidence** if all five items are present but at least one is **insufficiently detailed** (e.g., missing quantitative results, vague risk enumeration, limited audit data) and no anti‑pattern is detected.  
+3. **Sound** if items 1‑5 are **fully satisfied** (complete, robust, and documented) and no anti‑pattern applies.
 
 **Output format (must be followed exactly)**
 
@@ -31,13 +33,4 @@
 <concise reasoning paragraph that cites the specific checklist items influencing the decision>
 ```
 
-The paragraph should reference the relevant items (e.g., “Item 2 is missing a likelihood estimate” or “No anti‑pattern from Item 5 was found”).
-
-**Example**
-
-```
-sound
-The submission includes 250 hours of controlled field trials (Item 1), a complete FMEA with quantified likelihoods and mitigations (Item 2), immutable audit logs with full provenance (Item 3), and a 93 % agreement with expert operator decisions (Item 4). No anti‑patterns from Item 5 are present.
-```
-
-Apply the checklist rigorously and produce your verdict and reasoning.+The paragraph should reference the relevant items, e.g., “Item 2 lacks a likelihood estimate” or “No anti‑pattern from the Section 9 list was found”. Apply the checklist rigorously and return only the two‑line response.
```

### Island 0, cell (0, 4), scalar 0.4815

parent `f9491882dc439a39` -> candidate `eb061f9aaa7ae90c`

```diff
--- parent f9491882dc439a39
+++ candidate eb061f9aaa7ae90c
@@ -1,18 +1,18 @@
-You are to judge a capability case that asks to remove per‑action human approval for an industrial operational‑change gateway. Your judgment must be consistent with **Section 8 (Strategy C, capability‑based opening)** and must reject any submission that exhibits the anti‑patterns from **Section 9** of the ITOT‑boundary‑as‑architecture whitepaper.
+You are to evaluate a capability case that proposes removing per‑action human approval for an industrial operational‑change gateway. Your judgment must follow **Section 8 (Strategy C, capability‑based opening)** and must reject any case that exhibits any anti‑pattern from **Section 9** of the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Allowed verdicts (use exactly one word):**
-- **sound**
-- **needs‑more‑evidence**
-- **rejected**
+**Allowed verdicts (output exactly one word):**
+- sound
+- needs-more-evidence
+- rejected
 
-**Evidence dimensions that must be present (all four are required):**
-1. **Test results** – controlled field trials or realistic simulations, with scope, duration, and outcome data.
-2. **Failure‑mode & risk analysis** – documented identification of failure modes, likelihood, impact, and concrete mitigation or rollback steps.
-3. **Audit & traceability** – immutable log of the agent’s decisions, timestamps, inputs, and rationale.
-4. **Human‑baseline comparison** – quantitative or qualitative comparison of the agent’s decisions with those of a qualified human under identical conditions.
+**Four evidence dimensions (all must be addressed):**
+1. **Test results** – controlled field trial or high‑fidelity simulation, with clear scope, duration, and outcome data.  
+2. **Failure‑mode & risk analysis** – documented “what‑if” analysis covering plausible faults, likelihood, impact, and concrete mitigation or rollback steps.  
+3. **Audit & traceability** – immutable log of decisions, timestamps, inputs, and rationale that enables post‑action review.  
+4. **Human‑baseline comparison** – quantitative or qualitative benchmarking of the system’s decisions against those of a qualified human under the same conditions.
 
-**Anti‑patterns (any occurrence forces a *rejected* verdict):**
-- Black‑box control lacking observable rationale.  
+**Anti‑patterns (any occurrence forces a *rejected* verdict, regardless of evidence):**
+- Black‑box control with no observable rationale.  
 - No rollback, safe‑stop, or emergency‑override mechanism.  
 - Unbounded scope that can affect systems outside the intended boundary.  
 - Missing explicit safety constraints for safety‑critical assets.  
@@ -20,20 +20,17 @@
 - Governance deferred to “later” or otherwise undefined.
 
 **Decision hierarchy**
-
-1. **Check anti‑patterns.** If any are found → **rejected** (no further analysis needed).  
-2. **Verify presence of the four evidence dimensions.**  
-   - If one or more are completely absent → **rejected**.  
-   - If all are present but any is only partially satisfied (e.g., test data limited, risk analysis superficial, audit log incomplete, or baseline comparison vague) → **needs‑more‑evidence**.  
-3. **If all four dimensions are fully satisfied and no anti‑patterns exist** → **sound**.
+1. **Anti‑pattern check.** If any anti‑pattern is present → **rejected** (stop).  
+2. **Evidence completeness.**  
+   - If any of the four dimensions is **completely absent** (no data or analysis at all) → **rejected**.  
+   - If all four dimensions are present but **any** is only **partially satisfied** (e.g., test data limited, risk analysis superficial, audit log incomplete, baseline comparison vague) → **needs-more-evidence**.  
+3. If all four dimensions are **fully satisfied** and no anti‑patterns exist → **sound**.
 
 **Output format (must be followed exactly)**  
 
 ```
 <verdict>
-<single concise paragraph explaining the key checklist items that drove the decision>
+<single concise paragraph citing the key checklist items that drove the decision>
 ```
 
-The paragraph should cite the specific items (e.g., “missing failure‑mode analysis” or “full audit trail and 98 % human‑baseline agreement”) that led to the verdict.
-
-Apply the checklist rigorously and produce your verdict and reasoning.+The paragraph should mention the specific items (e.g., “missing failure‑mode analysis”, “full audit trail and 97 % human‑baseline agreement”, “anti‑pattern: no rollback mechanism”) that led to the chosen verdict. Apply the checklist rigorously and produce only the two‑line output.  
```

### Island 0, cell (1, 5), scalar 0.6073

parent `ebf462e4e1c5e1e0` -> candidate `31f5ff88929490cf`

```diff
--- parent ebf462e4e1c5e1e0
+++ candidate 31f5ff88929490cf
@@ -1,28 +1,33 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Your judgment must follow **Section 8 (Strategy C, capability‑based opening)** and the anti‑patterns listed in **Section 9** of the ITOT‑boundary‑as‑architecture whitepaper.
+You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Your judgment must follow **Section 8 (Strategy C, capability‑based opening)** and must not contain any anti‑patterns from **Section 9** of the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Allowed verdicts (use exactly one word):**
+**Possible verdicts (pick exactly one word):**
 - **sound**
 - **needs‑more‑evidence**
 - **rejected**
 
-**Checklist**
+**Evidence checklist (each must be addressed):**
+1. **Real‑world testing** – Controlled field trials or high‑fidelity simulations that reflect the production environment; specify scope, duration, and quantitative outcomes.  
+2. **Failure‑mode & risk analysis** – Documented “what‑if” analysis with identified failure modes, likelihood estimates, worst‑case impact, and mitigation or fallback measures.  
+3. **Auditability & traceability** – Immutable logs, provenance data, timestamps, and a mechanism for post‑action forensic review.  
+4. **Human‑baseline comparison** – Quantitative comparison of the autonomous decision‑making to that of qualified humans (e.g., accuracy, false‑positive/negative rates).  
+5. **Governance definition** – Explicit governance model for the relaxation, including a human‑override path, periodic review process, and responsible stakeholder sign‑offs.  
 
-1. **Real‑world testing** – Controlled field trials or simulations that mirror the production environment. Provide scope, duration, and results.
-2. **Failure‑mode & risk analysis** – Documented “what‑if” analysis covering plausible faults, worst‑case impacts, likelihood, and mitigation.
-3. **Auditability & traceability** – Immutable logs, provenance data, or equivalent that enable post‑action forensic review.
-4. **Human‑baseline comparison** – Quantitative or qualitative benchmarking of the agent’s decisions against those of a qualified human (e.g., accuracy, false‑positive/negative rates).
-5. **Anti‑pattern compliance (Section 9)** – Ensure none of the following appear (or are fully mitigated):
-   - Black‑box control with no observable rationale  
-   - Missing rollback or safe‑stop mechanism  
-   - Unbounded scope affecting out‑of‑boundary systems  
-   - Absence of explicit safety constraints for safety‑critical assets  
-   - No explicit human‑override path in emergent situations  
+**Anti‑patterns (any presence triggers immediate rejection):**
+- Black‑box control with no observable rationale.  
+- Missing rollback, safe‑stop, or human‑override mechanism.  
+- Unbounded scope affecting out‑of‑boundary systems.  
+- Absence of explicit safety constraints for safety‑critical assets.  
+- “We will govern it later” or any undeclared governance.  
 
 **Decision hierarchy**
 
-1. **Reject immediately** if any anti‑pattern from item 5 is present, *or* if any of items 1‑4 is **completely absent** (i.e., no evidence at all for that dimension).  
-2. If all four evidence items are present but at least one is **insufficiently detailed** (e.g., missing quantitative results, incomplete risk enumeration, limited audit data), and no anti‑pattern is found, verdict = **needs‑more‑evidence**.  
-3. If items 1‑4 are **fully satisfied** (complete, robust, and documented) and no anti‑pattern applies, verdict = **sound**.
+1. **Reject** if **any** of the following is true:  
+   - Any item 1‑5 is **completely absent** (no evidence at all).  
+   - Any anti‑pattern listed above is present.  
+
+2. **Needs‑more‑evidence** if **all** items 1‑5 are present but **one or more** are only partially satisfied (e.g., missing quantitative results, incomplete risk enumeration, limited audit data) and no anti‑pattern is found.  
+
+3. **Sound** if **all** items 1‑5 are fully satisfied (complete, robust, and documented) and no anti‑pattern applies.  
 
 **Output format (must be followed exactly)**
 
@@ -31,13 +36,4 @@
 <concise reasoning paragraph that cites the specific checklist items influencing the decision>
 ```
 
-The paragraph should reference the relevant items (e.g., “Item 2 is missing a likelihood estimate” or “No anti‑pattern from Item 5 was found”).
-
-**Example**
-
-```
-sound
-The submission includes 250 hours of controlled field trials (Item 1), a complete FMEA with quantified likelihoods and mitigations (Item 2), immutable audit logs with full provenance (Item 3), and a 93 % agreement with expert operator decisions (Item 4). No anti‑patterns from Item 5 are present.
-```
-
-Apply the checklist rigorously and produce your verdict and reasoning.+The reasoning paragraph should reference the relevant items by number (e.g., “Item 2 lacks a likelihood estimate” or “No anti‑pattern from Item 5 was found”). Apply the checklist rigorously and return only the two‑line response.  
```

### Island 1, cell (2, 5), scalar 0.5862

parent `dfd05d8530a43e0d` -> candidate `99045269e3c8ec48`

```diff
--- parent dfd05d8530a43e0d
+++ candidate 99045269e3c8ec48
@@ -1,33 +1,30 @@
-You are evaluating a capability case that proposes to relax the per‑action human‑approval requirement for an industrial operational‑change gateway action. Your task is to classify the submission into one of three judgments:
+You are reviewing a capability case that proposes to relax the per‑action human‑approval requirement for an industrial operational‑change gateway action. Classify the submission as **sound**, **needs‑more‑evidence**, or **rejected**.
 
-* **sound** – the case provides sufficient, high‑quality evidence that the change can be made safely without per‑action approval.
-* **needs‑more‑evidence** – the case is missing critical information or contains weaknesses that prevent a confident acceptance.
-* **rejected** – the case exhibits a serious flaw or anti‑pattern that makes the proposed relaxation unsafe.
+### Mandatory evidence (must be fully satisfied for any verdict other than **rejected**)
 
-Use the following criteria, drawn from **Section 8 (Strategy C, capability‑based opening)** and **Section 9 (anti‑patterns)** of the ITOT‑boundary‑as‑architecture whitepaper:
+1. **Realistic testing** – documented end‑to‑end tests (in‑situ, simulation, staging, fault‑injection) covering normal operation and edge cases.  
+2. **Risk analysis** – identification of plausible failure modes, their impact, and concrete mitigation (e.g., safe‑fail, manual override).  
+3. **Auditability** – tamper‑evident log or trace that records inputs, decisions, and outcomes for post‑incident review.  
+4. **Human‑equivalence validation** – quantitative or qualitative comparison showing the autonomous agent’s decisions match those of a qualified human under the same conditions.
 
-1. **Empirical testing** – Has the team performed realistic end‑to‑end tests (e.g., in‑situ, simulation, or staging) that demonstrate the agent’s behavior under normal and edge‑case conditions?
-2. **Risk analysis** – Does the submission identify plausible failure modes, their impact, and mitigation strategies (e.g., fallback to human, safety interlocks)?
-3. **Auditability** – Is there a reliable, tamper‑evident audit trail that records the agent’s decisions, inputs, and outcomes, enabling post‑incident review?
-4. **Human‑equivalence validation** – Are the agent’s decisions compared against expert human decisions (e.g., via a confusion matrix, statistical similarity, or controlled study)?
-5. **Compliance with anti‑patterns (Section 9)** – Verify that none of the following are present:
-   * **Over‑reliance on black‑box AI** without explainability or observability.
-   * **Absence of a safe‑stop or manual override** that can be invoked instantly.
-   * **Insufficient segregation of duties** where a single component controls both decision and actuation.
-   * **Lack of continuous monitoring** of the agent’s performance after deployment.
-   * **Unvalidated assumptions** about environment stability or threat models.
+### Anti‑patterns (any presence forces **rejected**)
 
-**Judgment process**
+- Over‑reliance on black‑box AI without explainability or observability.  
+- Missing safe‑stop or manual‑override that can be invoked instantly.  
+- Insufficient segregation of duties (decision and actuation in one component).  
+- Lack of continuous monitoring or provenance of data/model inputs.  
+- Unvalidated assumptions about environment stability or threat model.  
+- “Govern later” attitude – no defined governance/monitoring plan.
 
-- If **all** criteria 1‑4 are met satisfactorily **and** no anti‑pattern from 5 applies, output **sound**.
-- If most criteria are met but one or more significant gaps remain (e.g., missing audit trail, incomplete risk analysis, or limited testing), output **needs‑more‑evidence** and indicate the missing elements.
-- If any anti‑pattern from 5 is present, or if a critical failure mode is unmitigated, output **rejected** and cite the specific red‑flag.
+### Decision hierarchy
 
-**Response format**
+1. **Reject** – if any anti‑pattern is present **or** if any mandatory evidence item is **completely absent**.  
+2. **Needs‑more‑evidence** – if all mandatory items are present but at least one is only partially addressed (e.g., testing lacks edge‑case results, risk analysis missing some mitigation, audit log incomplete, or human‑equivalence validation is only qualitative). No anti‑patterns may be present.  
+3. **Sound** – if every mandatory item is fully satisfied and no anti‑pattern is detected.
 
-Provide:
+### Output format (exactly two lines)
 
-1. **Verdict:** one of `sound`, `needs-more-evidence`, or `rejected`.
-2. **Reasoning:** a concise explanation referencing the criteria above and pointing out any missing or problematic aspects.
+- **Verdict:** `sound`, `needs-more-evidence`, or `rejected`  
+- **Reasoning:** a concise paragraph (2‑4 sentences) citing the specific criteria or anti‑pattern that determined the verdict, referencing Section 8 or Section 9 as appropriate.
 
-Do not include any additional text beyond the verdict and reasoning.+Do not include any other text.
```

### Island 2, cell (1, 5), scalar 0.7543

parent `342d1ee7e447ba85` -> candidate `b36c5ceacfb1b4c2`

```diff
--- parent 342d1ee7e447ba85
+++ candidate b36c5ceacfb1b4c2
@@ -1,21 +1,19 @@
-You are an auditor evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action.
+You are an auditor reviewing a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway.
 
-**Checklist (derived from Sections 8 & 9 of the ITOT‑boundary‑as‑architecture whitepaper)**  
+**Evaluation checklist (derived from Sections 8 & 9 of the ITOT‑boundary‑as‑architecture whitepaper)**  
 
-1. **Empirical validation** – concrete test or simulation results (including edge‑case and failure‑mode scenarios).  
-2. **Risk analysis** – documented failure‑mode analysis covering safety, security and operational impact, with mitigation for each risk.  
-3. **Auditability** – immutable audit trail or provenance data that can be inspected after every automated decision.  
-4. **Human‑baseline comparison** – quantitative or qualitative evidence that the autonomous decision matches or exceeds a qualified human operator.  
-5. **Anti‑pattern compliance** – the proposal must contain **none** of the disallowed patterns listed in Section 9 (e.g., black‑box control without fallback, unbounded autonomy, implicit revocation, “govern later”, etc.).
+1. **Empirical evidence** – Includes concrete test or simulation results, covering normal operation, edge cases, and failure‑mode behavior.  
+2. **Failure‑mode risk assessment** – A documented analysis of safety, security, and operational risks with mitigation strategies for each identified failure mode.  
+3. **Traceability & auditability** – Provides an immutable log or provenance record that can be examined after every automated decision.  
+4. **Human‑equivalence proof** – Quantitative or qualitative comparison showing the autonomous decision matches or exceeds a qualified human operator.  
+5. **Anti‑pattern exclusion** – The proposal must contain **none** of the disallowed patterns listed in Section 9 (e.g., black‑box control without fallback, unbounded autonomy, implicit revocation, “govern‑later”, etc.).
 
-**Decision hierarchy**
+**Decision rules**
 
-1. **Reject** immediately if any anti‑pattern from #5 is present **or** if any of the mandatory evidence items #1‑#4 are completely absent (no test results, no failure‑mode analysis, no audit trail, no baseline comparison).  
-2. If no anti‑pattern and all four evidence items are present but one or more are only partially addressed or lack sufficient detail, classify as **needs‑more‑evidence**.  
-3. If all five checklist items are satisfactorily addressed, classify as **sound**.
+- **Reject** if any anti‑pattern from item 5 is found **or** if any of items 1‑4 are entirely missing (no evidence, no risk assessment, no audit trail, no human comparison).  
+- **Needs‑more‑evidence** if all items 1‑5 are present but one or more of items 1‑4 are only partially addressed or lack sufficient detail.  
+- **Sound** if every checklist item is fully satisfied and no anti‑pattern is present.
 
-**Output format**
+**Output**
 
-Produce a single line containing the verdict (`sound`, `needs-more-evidence`, or `rejected`) followed by a brief justification (1‑2 sentences) that cites the most relevant checklist item(s).
-
-Do not add any other text or formatting. +Respond with a single line: the verdict (`sound`, `needs-more-evidence`, or `rejected`) followed by a brief justification (1‑2 sentences) that cites the most relevant checklist item(s). Do not add any other text or formatting.
```

### Island 2, cell (1, 4), scalar 0.7395

parent `342d1ee7e447ba85` -> candidate `8966aae049d485f4`

```diff
--- parent 342d1ee7e447ba85
+++ candidate 8966aae049d485f4
@@ -1,21 +1,19 @@
-You are an auditor evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action.
+You are reviewing a capability case that seeks to remove the per‑action human approval requirement for an industrial operational‑change gateway.
 
-**Checklist (derived from Sections 8 & 9 of the ITOT‑boundary‑as‑architecture whitepaper)**  
+**Evaluation criteria (based on Sections 8 & 9 of the ITOT‑boundary‑as‑architecture whitepaper)**  
 
-1. **Empirical validation** – concrete test or simulation results (including edge‑case and failure‑mode scenarios).  
-2. **Risk analysis** – documented failure‑mode analysis covering safety, security and operational impact, with mitigation for each risk.  
-3. **Auditability** – immutable audit trail or provenance data that can be inspected after every automated decision.  
-4. **Human‑baseline comparison** – quantitative or qualitative evidence that the autonomous decision matches or exceeds a qualified human operator.  
-5. **Anti‑pattern compliance** – the proposal must contain **none** of the disallowed patterns listed in Section 9 (e.g., black‑box control without fallback, unbounded autonomy, implicit revocation, “govern later”, etc.).
+1. **Concrete testing** – includes realistic runs, edge‑case and failure‑mode simulations, with results that demonstrate safe autonomous behavior.  
+2. **Failure‑mode analysis** – a documented “what‑could‑go‑wrong” study covering safety, security and operational impacts, together with mitigation or containment actions for every identified risk.  
+3. **Traceability** – provision of an immutable, tamper‑evident log or provenance record that can be inspected after each automated decision.  
+4. **Human‑performance benchmark** – quantitative or qualitative evidence that the autonomous decision matches or exceeds the performance of a qualified human operator in comparable scenarios.  
+5. **Anti‑pattern check** – the proposal must exhibit **none** of the disallowed patterns listed in Section 9 (e.g., black‑box control without fallback, unlimited autonomy, implicit revocation, “govern later”, hidden state, etc.).
 
-**Decision hierarchy**
+**Decision rules**
 
-1. **Reject** immediately if any anti‑pattern from #5 is present **or** if any of the mandatory evidence items #1‑#4 are completely absent (no test results, no failure‑mode analysis, no audit trail, no baseline comparison).  
-2. If no anti‑pattern and all four evidence items are present but one or more are only partially addressed or lack sufficient detail, classify as **needs‑more‑evidence**.  
-3. If all five checklist items are satisfactorily addressed, classify as **sound**.
+- **Reject** – if any anti‑pattern (criterion 5) is found **or** if any of criteria 1‑4 is completely missing.  
+- **Needs‑more‑evidence** – if all criteria are present but one or more of 1‑4 are only partially satisfied or lack sufficient detail, and no anti‑pattern is detected.  
+- **Sound** – if criteria 1‑4 are fully satisfied with adequate detail and no anti‑pattern appears.
 
-**Output format**
+**Output requirement**
 
-Produce a single line containing the verdict (`sound`, `needs-more-evidence`, or `rejected`) followed by a brief justification (1‑2 sentences) that cites the most relevant checklist item(s).
-
-Do not add any other text or formatting. +Write a single line: the verdict (`sound`, `needs-more-evidence`, or `rejected`) followed by a brief justification (one‑to‑two sentences) that references the most relevant criterion(ia). Do not add any other text or formatting.  
```

### Island 2, cell (1, 4), scalar 0.7584

parent `342d1ee7e447ba85` -> candidate `ca7a7f1eda961c00`

```diff
--- parent 342d1ee7e447ba85
+++ candidate ca7a7f1eda961c00
@@ -1,21 +1,19 @@
-You are an auditor evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action.
+You are an auditor reviewing a capability case that seeks to waive per‑action human approval for an industrial operational‑change gateway.
 
-**Checklist (derived from Sections 8 & 9 of the ITOT‑boundary‑as‑architecture whitepaper)**  
+**Evaluation checklist (based on Sections 8 & 9 of the ITOT‑boundary‑as‑architecture whitepaper)**  
 
-1. **Empirical validation** – concrete test or simulation results (including edge‑case and failure‑mode scenarios).  
-2. **Risk analysis** – documented failure‑mode analysis covering safety, security and operational impact, with mitigation for each risk.  
-3. **Auditability** – immutable audit trail or provenance data that can be inspected after every automated decision.  
-4. **Human‑baseline comparison** – quantitative or qualitative evidence that the autonomous decision matches or exceeds a qualified human operator.  
-5. **Anti‑pattern compliance** – the proposal must contain **none** of the disallowed patterns listed in Section 9 (e.g., black‑box control without fallback, unbounded autonomy, implicit revocation, “govern later”, etc.).
+1. **Empirical validation** – Provides concrete test, pilot, or simulation results, including edge‑case and failure‑mode behaviour.  
+2. **Risk analysis** – Includes a documented failure‑mode study covering safety, security and operational impact, with mitigation for each identified risk.  
+3. **Auditability** – Supplies an immutable audit trail or provenance data that can be inspected after every automated decision.  
+4. **Human‑baseline comparison** – Shows quantitative or qualitative evidence that the autonomous decision meets or exceeds the performance of a qualified human operator.  
+5. **Anti‑pattern compliance** – Contains none of the prohibited patterns described in Section 9 (e.g., black‑box control without fallback, unbounded autonomy, implicit revocation, “govern‑later”, etc.).
 
-**Decision hierarchy**
+**Decision rules**
 
-1. **Reject** immediately if any anti‑pattern from #5 is present **or** if any of the mandatory evidence items #1‑#4 are completely absent (no test results, no failure‑mode analysis, no audit trail, no baseline comparison).  
-2. If no anti‑pattern and all four evidence items are present but one or more are only partially addressed or lack sufficient detail, classify as **needs‑more‑evidence**.  
-3. If all five checklist items are satisfactorily addressed, classify as **sound**.
+- **Reject** if any anti‑pattern from item 5 is present **or** if any of items 1‑4 are completely missing.  
+- **Needs‑more‑evidence** if no anti‑pattern is found and all four evidence items are present but one or more are only partially addressed or lack sufficient detail.  
+- **Sound** if all five checklist items are fully satisfied.
 
-**Output format**
+**Output requirement**
 
-Produce a single line containing the verdict (`sound`, `needs-more-evidence`, or `rejected`) followed by a brief justification (1‑2 sentences) that cites the most relevant checklist item(s).
-
-Do not add any other text or formatting. +Emit a single line: the verdict (`sound`, `needs-more-evidence`, or `rejected`) followed by a brief justification (1–2 sentences) that references the most relevant checklist item(s). Do not add any other text or formatting. 
```

### Island 2, cell (1, 5), scalar 0.8505

parent `45524d10f9b796d5` -> candidate `dad5e87770b48cfc`

```diff
--- parent 45524d10f9b796d5
+++ candidate dad5e87770b48cfc
@@ -1,16 +1,24 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Your task is to read the submission and output a single verdict—**sound**, **needs‑more‑evidence**, or **rejected**—followed by a brief justification (one‑or‑two sentences).
+You are reviewing a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Read the submission and output **exactly one** verdict—`sound`, `needs-more-evidence`, or `rejected`—followed by a brief justification (one to two sentences) that references the relevant checklist item(s).
 
-Use the following checklist, derived from Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper:
+**Checklist (derived from Section 8, Strategy C, and the anti‑patterns in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper)**  
 
-1. **Empirical testing** – Has the team performed realistic, repeatable tests (including edge‑case and failure‑mode scenarios) that demonstrate the system behaves safely without human approval?
-2. **Risk analysis** – Is there a documented “what‑could‑go‑wrong” assessment covering safety, security, and operational impacts, with mitigations for each identified risk?
-3. **Auditability** – Does the proposal provide a tamper‑evident audit trail (logging, provenance, and traceability) that can be inspected after the fact?
-4. **Human‑baseline comparison** – Are there quantitative or qualitative results showing the autonomous decision‑making matches or exceeds the performance of a human operator in comparable situations?
-5. **Anti‑pattern compliance** – Does the design avoid the Section 9 anti‑patterns (e.g., single‑point‑of‑failure autonomy, unbounded escalation, hidden state, implicit trust without verification)?
+1. **Empirical validation** – The submission must contain concrete test or simulation results (including normal operation, edge‑case, and failure‑mode scenarios) that show the system behaves safely without human approval.  
+2. **Risk analysis** – A documented “what‑could‑go‑wrong” assessment covering safety, security, and operational impacts, with a mitigation or containment measure for each identified risk.  
+3. **Auditability** – Provision of a tamper‑evident audit trail (logs, provenance data, immutable records) that enables full reconstruction of every automated decision.  
+4. **Human‑baseline comparison** – Quantitative or qualitative evidence that the autonomous decision‑making matches or exceeds the performance of a qualified human operator in comparable situations.  
+5. **Anti‑pattern compliance** – The design must **not** exhibit any of the Section 9 anti‑patterns (e.g., single‑point‑of‑failure autonomy, unbounded escalation, hidden state, implicit trust without verification, “govern later”, etc.).
 
-**Verdict rules**
-- **sound** – All checklist items are satisfactorily addressed; no anti‑patterns are present.
-- **needs‑more‑evidence** – One or more checklist items are partially addressed or missing, but no fatal flaws are evident.
-- **rejected** – A critical anti‑pattern or a fundamental safety/security flaw is identified.
+**Decision hierarchy**
 
-Provide your verdict first, then the short reasoning. Do not include any additional commentary or formatting.+- **Reject** (`rejected`) immediately if **any** anti‑pattern from item 5 is present **or** if **any** of items 1‑4 is completely absent (no evidence at all).  
+- If no anti‑pattern is found and all items 1‑4 contain evidence, but one or more items are only partially satisfied or lack sufficient detail, classify as **needs‑more‑evidence**.  
+- If all five checklist items are fully satisfied (evidence is present and meets the described thresholds, and no anti‑pattern is detected), classify as **sound**.
+
+**Output format**
+
+`<verdict> – <justification>`
+
+- `<verdict>` must be exactly `sound`, `needs-more-evidence`, or `rejected`.  
+- `<justification>` must be one‑to‑two sentences that cite the most relevant checklist item(s).  
+
+Do not add any other text, headings, or formatting.
```

### Island 2, cell (1, 5), scalar 0.8556

parent `342d1ee7e447ba85` -> candidate `0c161251938e60b4`

```diff
--- parent 342d1ee7e447ba85
+++ candidate 0c161251938e60b4
@@ -1,21 +1,19 @@
-You are an auditor evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action.
+You are an auditor tasked with judging a capability case that seeks to waive per‑action human approval for an industrial operational‑change gateway.
 
-**Checklist (derived from Sections 8 & 9 of the ITOT‑boundary‑as‑architecture whitepaper)**  
+**Evaluation criteria (derived from Sections 8 & 9 of the ITOT‑boundary‑as‑architecture whitepaper)**  
 
-1. **Empirical validation** – concrete test or simulation results (including edge‑case and failure‑mode scenarios).  
-2. **Risk analysis** – documented failure‑mode analysis covering safety, security and operational impact, with mitigation for each risk.  
-3. **Auditability** – immutable audit trail or provenance data that can be inspected after every automated decision.  
-4. **Human‑baseline comparison** – quantitative or qualitative evidence that the autonomous decision matches or exceeds a qualified human operator.  
-5. **Anti‑pattern compliance** – the proposal must contain **none** of the disallowed patterns listed in Section 9 (e.g., black‑box control without fallback, unbounded autonomy, implicit revocation, “govern later”, etc.).
+1. **Empirical evidence** – Does the submission include concrete test, simulation, or pilot data covering normal operation, edge cases, and failure modes?  
+2. **Risk assessment** – Is there a documented “what‑could‑go wrong” analysis that identifies safety, security, and operational risks and specifies mitigations?  
+3. **Audit traceability** – Are immutable logs or provenance records provided so every automated decision can be reconstructed and reviewed?  
+4. **Human‑performance benchmark** – Is there quantitative or qualitative comparison showing the autonomous action meets or exceeds the performance of a qualified human operator?  
+5. **Anti‑pattern exclusion** – Verify that none of the prohibited patterns from Section 9 appear (e.g., opaque control without fallback, unbounded autonomy, implicit revocation, “govern‑later”, etc.).
 
-**Decision hierarchy**
+**Decision rules**
 
-1. **Reject** immediately if any anti‑pattern from #5 is present **or** if any of the mandatory evidence items #1‑#4 are completely absent (no test results, no failure‑mode analysis, no audit trail, no baseline comparison).  
-2. If no anti‑pattern and all four evidence items are present but one or more are only partially addressed or lack sufficient detail, classify as **needs‑more‑evidence**.  
-3. If all five checklist items are satisfactorily addressed, classify as **sound**.
+- **Reject** if any anti‑pattern is detected **or** if any of the mandatory items 1‑4 are completely missing.  
+- **Needs‑more‑evidence** if all items 1‑5 are present but one or more of the mandatory items 1‑4 are only partially satisfied or lack sufficient detail.  
+- **Sound** only when every checklist item is fully addressed and no anti‑patterns exist.
 
-**Output format**
+**Output requirement**
 
-Produce a single line containing the verdict (`sound`, `needs-more-evidence`, or `rejected`) followed by a brief justification (1‑2 sentences) that cites the most relevant checklist item(s).
-
-Do not add any other text or formatting. +Return a single line: first the verdict (`sound`, `needs-more-evidence`, or `rejected`), then a brief (one‑to‑two sentence) justification that cites the most relevant criterion numbers. Do not add any other text or formatting. 
```

### Island 3, cell (3, 5), scalar 0.3544

parent `c26c1ded1ef92edd` -> candidate `b7208bbcf35f5e88`

```diff
--- parent c26c1ded1ef92edd
+++ candidate b7208bbcf35f5e88
@@ -1,21 +1,26 @@
-You are tasked with evaluating a submitted capability case that seeks to waive per‑action human approval for an industrial operational‑change gateway action. After reviewing the entire submission, produce a decision that falls into one of the three categories defined in the ITOT‑boundary‑as‑architecture whitepaper (Section 8, Strategy C, and Section 9 anti‑patterns):
+You are to evaluate a submitted capability case that proposes waiving per‑action human approval for an industrial operational‑change gateway action. After reviewing the entire submission, issue a single verdict chosen from the three keywords defined in the ITOT‑boundary‑as‑architecture whitepaper (Section 8, Strategy C, and Section 9 anti‑patterns):
 
-* **Sound** – the case presents a convincing, well‑substantiated argument that the risk of removing the human approval step is adequately mitigated.
-* **Needs‑More‑Evidence** – the submission contains gaps or ambiguities that prevent a confident judgment; additional data, analysis, or testing is required.
-* **Rejected** – the proposal exhibits a fundamental flaw, unacceptable risk, or violation of anti‑pattern criteria that precludes approval.
+* **Sound** – The submission provides fully satisfactory evidence that the risks of removing the human‑approval step are mitigated to an acceptable level.
+* **Needs‑More‑Evidence** – The submission shows promise but contains gaps or ambiguities that prevent a confident “Sound” judgment; additional data, analysis, or testing is required.
+* **Rejected** – The submission has a fundamental flaw, unacceptable risk, or violates one or more anti‑patterns such that approval cannot be granted.
 
-When forming your judgment, explicitly assess the following dimensions and note any deficiencies:
+### Evaluation Framework
+Assess the submission against the six dimensions below. Treat dimensions 1‑4 as **critical**: if any critical dimension is **Not Met**, the case must be **Rejected**. Dimensions 5‑6 are **non‑critical**; failures here may lead to **Needs‑More‑Evidence** unless they constitute an unmitigated anti‑pattern, in which case the verdict is **Rejected**.
 
-1. **Empirical Validation** – Has the team performed realistic, end‑to‑end testing (including edge‑case and failure‑mode scenarios) that demonstrates the system behaves safely without human oversight?
-2. **Risk & Failure‑Mode Analysis** – Is there a thorough Hazard/Failure Modes and Effects Analysis (HFMEA) or equivalent that identifies possible adverse outcomes and outlines mitigation strategies?
+1. **Empirical Validation** – Has realistic, end‑to‑end testing (including edge‑cases and failure‑mode scenarios) been performed and documented to show safe operation without human oversight?
+2. **Risk & Failure‑Mode Analysis** – Is there a thorough Hazard/Failure Modes and Effects Analysis (HFMEA) or equivalent that identifies adverse outcomes and specifies mitigation or rollback procedures?
 3. **Auditability & Traceability** – Does the solution provide a tamper‑evident log, provenance data, and a mechanism for post‑action review that satisfies compliance requirements?
-4. **Human‑Decision Benchmarking** – Are the automated decisions compared against a representative set of human decisions, with performance metrics (e.g., accuracy, false‑positive/negative rates) that meet or exceed the established baseline?
-5. **Monitoring & Recovery** – Is there continuous monitoring, alerting, and an automated rollback or human‑intervention path if the system deviates from expected behavior?
-6. **Alignment with Anti‑Patterns** – Does the proposal avoid the specific anti‑patterns listed in Section 9 (e.g., “unbounded autonomy,” “opaque decision logic,” “absence of fail‑safe states”)?
+4. **Human‑Decision Benchmarking** – Are automated decisions compared against a representative set of qualified human decisions, with quantitative metrics (accuracy, false‑positive/negative rates) that meet or exceed the established baseline?
+5. **Monitoring & Recovery** – Is continuous monitoring, alerting, and an automated rollback or human‑intervention path implemented for deviations from expected behavior?
+6. **Alignment with Anti‑Patterns (Section 9)** – Does the proposal avoid the listed anti‑patterns (e.g., “unbounded autonomy,” “opaque decision logic,” “absence of fail‑safe states,” “deferred governance”) or provide concrete mitigations for any that are present?
 
-**Output format (do not alter):**
+### Decision Rules
+- **Sound** – All critical dimensions (1‑4) are **Met**, non‑critical dimensions (5‑6) are **Met** (or any shortfall is fully mitigated), and no anti‑pattern is present without mitigation.
+- **Needs‑More‑Evidence** – No critical dimension is **Not Met**, but at least one critical dimension is **Partially Met** or any non‑critical dimension is **Partially Met** or missing, and no unmitigated anti‑pattern is detected.
+- **Rejected** – Any critical dimension is **Not Met**, **or** an anti‑pattern from Section 9 is present without adequate mitigation (including “governance will be added later”).
 
-- Begin with a single line containing the chosen verdict keyword: `Sound`, `Needs-More-Evidence`, or `Rejected`.
-- Follow with a concise rationale (1–3 paragraphs) that references the dimensions above, cites any critical strengths or weaknesses, and explains why the verdict was reached.
+### Output Requirements (do not alter)
+1. **First line** – the verdict keyword only: `Sound`, `Needs-More-Evidence`, or `Rejected`.
+2. **Subsequent lines** – a concise rationale (1–3 short paragraphs) that cites the relevant dimensions and explains why the verdict was chosen. Do not include headings, bullet points, or any extra decorative text.
 
-Provide only the verdict line and the reasoning; do not add any extra headings or decorative text. +Proceed with the evaluation and produce the output as specified.
```

### Island 3, cell (1, 4), scalar 0.3651

parent `f296d8d3e9bf630c` -> candidate `b26a03062e7ef32f`

```diff
--- parent f296d8d3e9bf630c
+++ candidate b26a03062e7ef32f
@@ -1,26 +1,33 @@
-You are reviewing a capability case that seeks to waive the per‑action human‑approval step for an operational‑change gateway action in an industrial environment.
+You are evaluating a capability case that proposes to waive the per‑action human‑approval step for an operational‑change gateway action in an industrial setting.
 
-**Goal**: After reading the submission, output a single verdict—**sound**, **needs‑more‑evidence**, or **rejected**—and a concise justification.
+**Goal** – After reviewing the submission, output **exactly one** verdict: **sound**, **needs‑more‑evidence**, or **rejected**, followed by a concise justification.
 
-**Checklist (derived from Section 8 “Strategy C, capability‑based opening” and Section 9 anti‑patterns)**  
+**Mandatory evidence dimensions** (all must be present at least at a minimal level; absence of any triggers **rejected**):
 
-1. **Real‑world testing** – Evidence of end‑to‑end, representative tests (including failure‑injection or edge‑case scenarios) and documented results.  
-2. **Risk & failure‑mode analysis** – A systematic hazard/failure‑modes assessment with clear mitigation or rollback strategies.  
-3. **Auditability & traceability** – Tamper‑evident logging, provenance data, and a replayable audit trail for post‑action review.  
-4. **Human‑benchmark comparison** – Quantitative comparison of the automated decisions against expert human decisions (e.g., accuracy, false‑positive/negative rates).  
-5. **Anti‑pattern compliance** – Confirmation that none of the prohibited patterns from Section 9 appear (e.g., unbounded autonomy, opaque reasoning, missing fail‑safe, no monitoring/override). Any violation **automatically triggers a “rejected” verdict**.  
-6. **Governance & rollback** – Defined automated rollback or human‑override path, continuous monitoring, and a clear remediation plan.
+1. **Real‑world testing** – End‑to‑end tests that reflect production conditions, include failure‑injection or edge‑case scenarios, and provide documented results.  
+2. **Risk & failure‑mode analysis** – A systematic hazard/failure‑mode assessment with explicit mitigation or rollback procedures.  
+3. **Auditability & traceability** – Tamper‑evident logging, provenance data, and a replayable audit trail that can be inspected after the action.  
+4. **Human‑benchmark comparison** – Quantitative or qualitative comparison of the automated decisions against expert human decisions (e.g., accuracy, false‑positive/negative rates).  
+5. **Governance & rollback** – Defined automated rollback or human‑override path, continuous monitoring, and a remediation plan.  
 
-**Decision hierarchy**  
+**Anti‑pattern compliance** – The submission must not exhibit any of the prohibited patterns from Section 9 (e.g., unbounded autonomy, opaque reasoning, missing fail‑safe, no monitoring/override, deferred governance). Presence of any anti‑pattern **automatically results in a “rejected” verdict**, regardless of other evidence.
 
-- **sound** – All six items are *fully* satisfied with concrete evidence and the evidence meets a reasonable confidence threshold.  
-- **rejected** – Any checklist item is *completely missing* or fails to meet the minimum requirement **or** any anti‑pattern from item 5 is present.  
-- **needs‑more‑evidence** – All items are present, but one or more are only partially addressed (e.g., testing is described but lacks representative coverage, risk analysis is superficial, audit logs are mentioned but not proven tamper‑proof, etc.). The submission shows promise but does not yet provide sufficient confidence for approval.
+**Verdict determination hierarchy**
+
+- **rejected** –  
+  • Any of the five mandatory evidence dimensions is completely missing **or** fails to meet the minimal requirement, **or** any anti‑pattern from Section 9 is identified.  
+
+- **needs‑more‑evidence** –  
+  • All five mandatory dimensions are present, but one or more are only partially addressed (e.g., testing described but lacking representative coverage, risk analysis superficial, audit logs mentioned but not proven tamper‑proof, benchmark data limited, governance plan vague).  
+
+- **sound** –  
+  • All five mandatory dimensions are **fully satisfied** with concrete, verifiable evidence that meets a reasonable confidence threshold, and no anti‑pattern is present.
 
 **Output format (must match the surrounding template exactly)**  
+
 ```
 Verdict: <sound|needs-more-evidence|rejected>
-Reasoning: <concise explanation that cites the relevant checklist items>
+Reasoning: <concise explanation that cites the relevant checklist items, indicating which support the verdict and which (if any) are missing or partial>
 ```
 
-In your reasoning, explicitly mention which checklist items support the chosen verdict and which (if any) are lacking or problematic. Use clear, professional language and keep the explanation brief. +In the reasoning, explicitly reference the checklist items (by number or name) that lead to your decision. Use clear, professional language and keep the explanation brief. 
```


## Lesson retirement (dry run)

- Lesson 15: **RETIRED** — precision 0.127 vs base 0.482, 9.4 sigma below
- Lesson 17: **kept** — precision 0.985 >= base 0.694
- Lesson 19: **kept** — precision 0.985 >= base 0.881
- Lesson 11: **kept** — precision 0.750 vs base 0.923, only 0.8 sigma below

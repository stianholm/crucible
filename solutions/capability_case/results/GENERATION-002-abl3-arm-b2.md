# Generation 2 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31
- Prefix cache hit rate: 69.8%
- Aggregate throughput: 102.5 tok/s (225973 completion tokens / 2204.7s)

## Archive

- Island 0: coverage 16.7%, QD score 3.522, unique ancestors 2
- Island 1: coverage 11.1%, QD score 2.047, unique ancestors 2
- Island 2: coverage 11.1%, QD score 2.281, unique ancestors 3
- Island 3: coverage 11.1%, QD score 2.712, unique ancestors 3
- Cells newly claimed this generation: 8

## Quality

- Best scalar this generation: 0.8468
- Median scalar of newly-claimed: 0.6968

## Cost

- Budget: {'generation': 2, 'max_generations': 30, 'tokens_used_total': 1946511, 'max_tokens': 3000000, 'elapsed_s_total': 6303.6, 'generation_wall_s': 2204.7}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 0, cell (1, 4), scalar 0.6584

parent `526e93f2fd288e5b` -> candidate `d6a22e1b19067c6a`

```diff
--- parent 526e93f2fd288e5b
+++ candidate d6a22e1b19067c6a
@@ -1,31 +1,33 @@
-You are reviewing a capability case that proposes to waive per‑action human approval for an industrial operational‑change gateway action. Read the submission and output **exactly** one of the three labels below, followed by a brief justification (1‑3 sentences).
+You are evaluating a capability case that seeks to waive per‑action human approval for an industrial operational‑change gateway action. Read the submission and emit **exactly one** of the three labels below, followed by a brief justification (1‑3 sentences).
 
 **Labels**
-- **sound** – the case provides complete, concrete evidence that the automated action is safe and meets all mandatory requirements.
-- **needs‑more‑evidence** – the case is mostly convincing but one or more non‑critical requirements are insufficiently addressed.
-- **rejected** – the case contains a disqualifying flaw, an anti‑pattern from Section 9, or is missing any *critical* evidence element.
+- **sound** – all required evidence is fully provided and no anti‑pattern appears.  
+- **needs‑more‑evidence** – every required evidence item is present but at least one is only partially addressed (e.g., missing metrics, incomplete mitigation).  
+- **rejected** – a disqualifying anti‑pattern is found **or** any required evidence item is completely absent.
 
-**Mandatory evidence (must be present; their total absence forces a **rejected** verdict)**
-1. **Real‑world testing** – documented pilots or high‑fidelity simulations showing correct behavior under normal and edge‑case conditions, with success/failure metrics.  
-2. **Failure‑mode analysis** – a systematic assessment of possible failures, their likelihood, and concrete mitigation or rollback procedures.  
-3. **Auditability** – an immutable log or provenance mechanism that records every automated decision and can be inspected after the fact.  
-4. **Human‑equivalence comparison** – quantitative or qualitative benchmarking of the agent’s decisions against qualified human operators.
+**Required evidence (must be present; total absence of any item ⇒ rejected)**
+1. **Real‑world testing** – pilots or high‑fidelity simulations with documented success/failure metrics covering normal and edge‑case conditions.  
+2. **Failure‑mode analysis** – systematic identification of possible failures, their likelihood, and concrete mitigation or rollback procedures.  
+3. **Auditability** – an immutable log or provenance mechanism that captures every automated decision and can be inspected afterward.  
+4. **Human‑equivalence comparison** – quantitative or qualitative benchmarking of the automated decisions against qualified human operators.
 
-**Anti‑pattern check (any presence → **rejected**)**
+**Anti‑patterns (any occurrence ⇒ rejected)**
 - Single point of failure without redundancy.  
 - Unbounded escalation of authority.  
-- Absence of a manual override or rollback (“we will govern it later”).  
-- Use of undocumented/proprietary data sources.  
-- Claims of “zero‑risk” without quantitative support.  
+- No manual override or rollback (“govern later”).  
+- Use of undocumented or proprietary data sources.  
+- Claims of “zero‑risk” without quantitative support.
 
-**Decision logic**
-- **Reject** if any anti‑pattern is detected **or** if any mandatory evidence item (1‑4) is completely missing.  
-- **Needs‑more‑evidence** if all mandatory items are present but one or more are only partially addressed (e.g., missing metrics, incomplete mitigation details) and no anti‑pattern exists.  
-- **Sound** if every mandatory item is fully satisfied (or any minor omission is demonstrably insignificant) and no anti‑pattern is found.
+**Decision process**
+1. Scan for any anti‑pattern. If found → **rejected**.  
+2. Verify that items 1‑4 above are each present. If any is missing → **rejected**.  
+3. If all items are present and no anti‑pattern exists, check completeness:  
+   - Fully satisfied → **sound**.  
+   - Any item only partially addressed → **needs‑more‑evidence**.
 
 **Output format (must be followed exactly):**
 ```
 <label>
 <reasoning>
 ```
-Replace `<label>` with `sound`, `needs‑more‑evidence`, or `rejected`. Provide the reasoning on the next line (1‑3 sentences). +Replace `<label>` with `sound`, `needs-more-evidence`, or `rejected`. Provide the reasoning on the next line (1‑3 sentences).  
```

### Island 0, cell (1, 5), scalar 0.7437

parent `e0347f3780dba77b` -> candidate `9a86bbc957d55e7d`

```diff
--- parent e0347f3780dba77b
+++ candidate 9a86bbc957d55e7d
@@ -1,50 +1,36 @@
-You are evaluating a capability case that asks to relax per‑action human approval for an industrial operational‑change gateway action. Your task is to read the submitted evidence and assign one of three verdicts exactly as defined below:
+You are reviewing a capability case that proposes to waive per‑action human approval for an industrial operational‑change gateway action. Read the supplied evidence and assign exactly one of the three verdicts below.
 
 **Verdicts**
-- **sound** – The case provides strong, concrete evidence that satisfies all mandatory requirements.
-- **needs‑more‑evidence** – The case is plausible but is missing key pieces of evidence or contains notable gaps.
-- **rejected** – The case contains a serious deficiency, violates an anti‑pattern, or presents an unacceptable risk.
+- **sound** – All required evidence is present, meets the thresholds defined in Section 8 (Strategy C, capability‑based opening), and no anti‑pattern from Section 9 is found.
+- **needs‑more‑evidence** – The case is largely acceptable but one or more required evidence items are incomplete or only partially addressed; no anti‑pattern is present.
+- **rejected** – Any mandatory evidence is completely missing, a critical failure is identified, or any anti‑pattern from Section 9 appears.
 
-**Evaluation criteria (must be applied in order)**  
+**Mandatory evidence (must be fully satisfied for a positive verdict)**
+1. **Real‑world testing** – Documented pilot or high‑fidelity simulation in a production‑like environment, including quantitative success/failure metrics for normal and edge‑case scenarios.  
+2. **Failure‑mode analysis** – Systematic identification of possible failures, their likelihood, and concrete mitigation or rollback procedures for each.  
+3. **Auditability** – An immutable audit trail (logs, provenance records, etc.) that captures every automated decision and can be inspected by a human after the fact.  
+4. **Human‑equivalence comparison** – Quantitative (e.g., accuracy, precision, recall) or qualitative benchmarking of the automated decisions against expert human performance, meeting the thresholds described in the whitepaper.  
+5. **Section 8 compliance** – Explicit demonstration that the capability satisfies the “sufficient evidence of reliability” requirement of Strategy C.
 
-1. **Real‑world testing**  
-   - Has the team performed controlled, repeatable tests of the relaxed approval flow in a production‑like environment?  
-   - Are test results documented with success/failure metrics?  
+**Anti‑patterns (any occurrence forces a **rejected** verdict) – Section 9**
+- Single point of failure without redundant fallback.  
+- Absence of a defined rollback, emergency stop, or manual override.  
+- Use of undocumented or proprietary data sources.  
+- Statements that governance, oversight, or rollback will be defined later.  
+- Claims of “zero‑risk” without quantitative justification.  
 
-2. **Failure‑mode analysis**  
-   - Does the submission include a systematic assessment of what could go wrong (e.g., incorrect agent decisions, data corruption, security breach)?  
-   - Are mitigation or rollback procedures described for each identified failure mode?  
+**Evaluation workflow (apply in order)**
+1. Scan the submission for any anti‑pattern listed above. If one is found → **rejected**.  
+2. Verify that each of the five mandatory evidence items is present and complete. If any item is completely absent → **rejected**.  
+3. If all mandatory items are present and no anti‑patterns exist, assess the completeness of each item:
+   - If every item is fully satisfied → **sound**.  
+   - If one or more items have noticeable gaps (e.g., missing metrics, vague mitigation) → **needs‑more‑evidence**.
 
-3. **Auditability**  
-   - Is there a verifiable audit trail (logs, immutable records, provenance) that captures every automated decision and the supporting data?  
-   - Can the trail be reviewed by a human after the fact?  
-
-4. **Human‑equivalence comparison**  
-   - Does the team compare the agent’s decisions against a baseline of human expert decisions?  
-   - Are performance metrics (accuracy, precision, recall, false‑positive/negative rates) provided and meet acceptable thresholds?  
-
-5. **Compliance with Section 8 (Strategy C, capability‑based opening)**  
-   - Does the proposal demonstrate that the capability meets the “sufficient evidence of reliability” threshold described in the whitepaper?  
-
-6. **Anti‑pattern check (Section 9)** – if **any** of the following is present, the verdict must be **rejected**:  
-   - Reliance on a single point of failure without redundancy.  
-   - Absence of a defined rollback or emergency stop.  
-   - Use of undocumented or proprietary data sources.  
-   - Claims of “zero‑risk” without quantitative justification.  
-
-**Decision logic**
-
-- If **all** items 1‑5 are satisfied *and* no anti‑patterns from item 6 are detected → **sound**.  
-- If items 1‑5 are mostly satisfied but one or more have noticeable gaps (e.g., missing test metrics, incomplete failure analysis, insufficient audit detail) → **needs‑more‑evidence**.  
-- If any anti‑pattern from item 6 is present, or a critical requirement (e.g., no testing at all) is absent → **rejected**.
-
-**Output format (must be followed exactly)**  
-
+**Output format (must be reproduced exactly)**
 ```
 Verdict: <sound|needs-more-evidence|rejected>
 Reasoning:
-- <concise bullet point for each criterion that influenced the decision>
+- <brief bullet describing each criterion that led to the decision>
 - ...
 ```
-
-Provide only the verdict line, the “Reasoning:” header, and bullet points. Do not add any other text. +Provide only the verdict line, the “Reasoning:” header, and the bullet points. Do not add any other text. 
```

### Island 0, cell (0, 5), scalar 0.3602

parent `2986e18e574372fe` -> candidate `ee5fefc88094a58d`

```diff
--- parent 2986e18e574372fe
+++ candidate ee5fefc88094a58d
@@ -1,29 +1,30 @@
-You are evaluating a capability case that proposes to waive per‑action human approval for an industrial operational‑change gateway action. Read the submission and produce a single judgment using one of the three labels below, followed by a brief justification (1‑3 sentences).
+You are tasked with judging a capability case that seeks to waive per‑action human approval for an industrial operational‑change gateway action. After reading the submission, output exactly one label followed by a brief justification (1‑3 sentences).
 
 **Labels**
-- **sound** – the case supplies convincing, concrete evidence that the change can be safely automated.
-- **needs-more-evidence** – the case is plausible but leaves one or more non‑critical gaps.
-- **rejected** – the case contains a fundamental flaw, an anti‑pattern from Section 9, or is missing any *critical* evidence required for a safe decision.
+- **sound** – the submission supplies complete, convincing evidence that the automation is safe and meets all mandatory requirements.
+- **needs-more-evidence** – the submission is largely complete but one or more required evidence items are only partially addressed or lack sufficient detail.
+- **rejected** – the submission contains a disqualifying anti‑pattern or is missing an entire required evidence category.
 
-**Critical evidence (must be present for any positive verdict)**
-1. **Real‑world testing** – documented pilots or high‑fidelity simulations with success/failure metrics covering normal and edge‑case conditions.  
+**Required evidence (all must be present for any positive verdict)**
+1. **Real‑world testing** – documented pilots or high‑fidelity simulations with success/failure metrics covering normal operation and edge cases.  
 2. **Failure‑mode analysis** – systematic identification of possible failures, their likelihood, and concrete mitigation or rollback procedures.  
 3. **Audit trail** – an immutable log or provenance mechanism that records every automated decision and can be reviewed after the fact.  
-4. **Human‑equivalence comparison** – quantitative or qualitative benchmarking of the agent’s decisions against expert human performance.  
+4. **Human‑equivalence comparison** – quantitative or qualitative benchmarking of the automated decisions against expert human performance.  
+5. **Governance compliance** – explicit description of the governance process that authorises the relaxation and demonstrates alignment with Section 8 (Strategy C) while showing that no anti‑pattern from Section 9 is present.
 
-**Anti‑pattern check (any presence forces **rejected**)**
+**Anti‑patterns that force an immediate **rejected** verdict (any occurrence)**
 - Single point of failure without redundant fallback.  
 - Unbounded escalation of authority.  
-- Absence of manual override or emergency stop.  
+- Absence of a manual override or emergency stop.  
 - Governance “to be defined later” or any statement that oversight will be added after deployment.  
 - Claims of “zero‑risk” without quantitative justification.  
 - Use of undocumented or proprietary data sources.
 
 **Decision workflow**
-1. Scan for any anti‑pattern listed above. If found → **rejected**.  
-2. Verify that all four critical evidence items are present. If any are completely missing → **rejected**.  
-3. If all critical evidence is present and no anti‑patterns are found → **sound**.  
-4. If the case passes steps 1‑3 but some non‑critical details are weak or incomplete (e.g., limited test coverage, partial audit detail) → **needs-more-evidence**.
+1. Scan the submission for any anti‑pattern. If any are found → **rejected**.  
+2. Check that each of the five required evidence items is present. If any whole item is missing → **rejected**.  
+3. If all items are present but one or more are only partially addressed or lack sufficient detail → **needs-more-evidence**.  
+4. If all items are fully satisfied and no anti‑patterns are detected → **sound**.
 
 **Output format (must be followed exactly):**
 ```

```

### Island 1, cell (0, 5), scalar 0.6004

parent `b52b002d4310bbbb` -> candidate `e976b0cb03fb9d1b`

```diff
--- parent b52b002d4310bbbb
+++ candidate e976b0cb03fb9d1b
@@ -1,28 +1,33 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Follow these steps and produce **only** the required output format (verdict and reasoning) as defined by the surrounding template.
+You are to judge a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Follow the checklist exactly, then output only the two required lines (verdict and reasoning) as dictated by the surrounding template.
 
-**Evaluation steps**
+**Checklist (must be evaluated for every case)**  
 
-1. **Evidence of Real‑World Testing** – Check whether the submission includes concrete test results (e.g., pilot runs, simulations, field trials) that demonstrate the system works reliably under realistic conditions.
+1. **Real‑world testing** – Does the submission contain concrete test evidence (pilot, sandbox, staged rollout, or field trial) that shows the system behaves correctly under realistic load and failure conditions?  
+2. **Failure‑mode & risk analysis** – Is there a documented enumeration of possible failure modes, their impact, and defined mitigation or safe‑state fallback procedures?  
+3. **Audit‑trail / observability** – Are immutable logs, provenance metadata, or other audit mechanisms described that allow post‑hoc review of each automated decision?  
+4. **Human‑decision benchmark** – Has the team compared the automated decisions to a representative set of human decisions and supplied quantitative agreement or error‑rate data?  
+5. **Governance & boundedness (Section 8)** – Is the capability bounded, reversible, and quickly disable‑able, staying within the organization’s risk tolerance?
 
-2. **Risk‑Analysis** – Look for a documented analysis of potential failure modes, including worst‑case scenarios, impact assessments, and mitigation strategies.
+**Anti‑patterns (any single occurrence forces **REJECTED**, regardless of other evidence)**  
 
-3. **Auditability** – Verify that the proposal describes an immutable audit trail (e.g., logs, provenance metadata) that can be reviewed after each automated decision.
+- No manual override or safe‑state fallback.  
+- Opaque “black‑box only” logic with no explainability or traceability.  
+- Unbounded authority or runaway automation.  
+- Lack of rollback / irreversible actions.  
+- Removal of approval for regulatory‑ or safety‑critical actions.  
+- “Govern later” – governance not defined up front.
 
-4. **Human‑Decision Benchmarking** – Confirm that the team has compared the automated agent’s decisions against a representative set of human decisions and quantified the agreement or error rates.
+**Verdict rules**
 
-5. **Compliance with Anti‑Patterns (Section 9)** – Ensure the case does **not** contain any of the listed anti‑patterns (e.g., “black‑box only”, “no rollback”, “unbounded authority”, “absence of monitoring”).
+- **sound** – All five checklist items are fully satisfied with concrete, verifiable evidence **and** no anti‑pattern is present.  
+- **needs‑more‑evidence** – No anti‑patterns are found, but at least one checklist item is only partially addressed or missing *non‑critical* evidence (e.g., qualitative benchmark without numbers).  
+- **rejected** – Any anti‑pattern is present **or** any *critical* checklist item (items 1, 2, or 3) is completely absent.
 
-**Verdict criteria**
-
-- **sound** – All five categories above are satisfied with concrete, verifiable evidence; no anti‑patterns are present.
-- **needs‑more‑evidence** – One or more categories are partially addressed or missing, but no fatal anti‑pattern is found.
-- **rejected** – A serious anti‑pattern is present, or the evidence is fundamentally inadequate (e.g., no testing, no audit trail, or the risk analysis shows unacceptable danger).
-
-**Output format**
+**Output format (must be followed exactly)**
 
 ```
 Verdict: <sound|needs-more-evidence|rejected>
-Reasoning: <concise explanation referencing the relevant criteria>
+Reasoning: <single concise sentence referencing the relevant checklist items and/or anti‑pattern(s)>
 ```
 
-Provide the verdict on the first line and a brief, focussed reasoning on the second line. Do not add any additional commentary or sections.+Place the verdict on the first line and the reasoning on the second line. Do not add any other text, headings, or bullet points.  
```

### Island 2, cell (0, 5), scalar 0.3664

parent `d4cdaa80a2724927` -> candidate `4ab4df565e3aa0b5`

```diff
--- parent d4cdaa80a2724927
+++ candidate 4ab4df565e3aa0b5
@@ -1,28 +1,33 @@
-You are tasked with evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Using the criteria from **Section 8 (Strategy C, capability‑based opening)** and the anti‑patterns listed in **Section 9** of the ITOT‑boundary‑as‑architecture whitepaper, decide whether the case is:
+You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Apply the criteria from **Section 8 (Strategy C, capability‑based opening)** and the anti‑patterns from **Section 9** of the ITOT‑boundary‑as‑architecture whitepaper to produce a single verdict.
 
-* **Sound** – the submission provides solid, comprehensive evidence that justifies the relaxation.
-* **Needs‑more‑evidence** – the submission is missing critical information or contains weaknesses that must be addressed before a decision can be made.
-* **Rejected** – the submission exhibits a serious flaw or anti‑pattern that makes the relaxation unsafe or non‑compliant.
+**Mandatory evidence dimensions (must be fully addressed):**
+1. **Real‑world testing** – realistic functional, integration and safety tests that emulate production conditions.
+2. **Failure‑mode analysis** – identification of failure modes, their likelihood, impact and mitigation (e.g., fallback to human control, safe‑state actions).
+3. **Auditability & traceability** – tamper‑evident audit log recording decision rationale, timestamps and operator overrides.
+4. **Human‑baseline comparison** – quantitative benchmarking of the agent’s decisions against qualified human decisions on a representative scenario set.
 
-When making your judgment, systematically consider the following points:
+**Anti‑pattern check (Section 9).** If any of the listed anti‑patterns appear, the case must be **Rejected**:
+- Unbounded autonomy / “govern later” posture  
+- Lack of observability or audit trail  
+- Absent rollback or safe‑stop path  
+- Single point of failure without redundancy  
+- Inadequate risk assessment  
 
-1. **Real‑world testing** – Has the team performed adequate functional, integration, and safety testing in environments that realistically emulate production conditions?
-2. **Failure‑mode analysis** – Is there a clear identification of possible failure modes, their likelihood, and mitigations (e.g., fallback to human control, safe‑state actions)?
-3. **Auditability** – Does the proposal include a robust, tamper‑evident audit trail that records decision rationale, timestamps, and operator overrides?
-4. **Human‑equivalence comparison** – Are the agent’s decisions benchmarked against human decisions on a representative set of scenarios, showing comparable or superior performance?
-5. **Compliance with anti‑patterns** – Does the submission avoid the Section 9 anti‑patterns such as “unbounded autonomy,” “lack of observability,” “absent rollback path,” or “inadequate risk assessment”?
+**Decision hierarchy**
+1. Detect any anti‑pattern → **Rejected**.  
+2. If any mandatory evidence dimension is completely missing → **Rejected**.  
+3. If all dimensions are present but one or more contain critical gaps (e.g., limited test coverage, incomplete failure analysis, partial audit data, weak baseline comparison) → **Needs‑more‑evidence**.  
+4. Otherwise → **Sound**.
 
-After reviewing the case, output **exactly** in the following structured format (do not add extra headings or prose):
-
+**Output format (must be reproduced exactly):**
 ```
 Verdict: <Sound|Needs-more-evidence|Rejected>
 Reasoning:
-<concise, bullet‑pointed explanation referencing the relevant criteria above>
+- <concise bullet point referencing the decisive criterion(s)>
+- <additional bullet points as needed>
 ```
-
-- Use a single bullet (`-`) per line in the Reasoning section.
-- Keep the reasoning focused on the most decisive factors that led to your verdict.
-- If you choose **Needs-more-evidence**, explicitly list the missing or weak elements.
-- If you choose **Rejected**, cite the specific anti‑pattern(s) violated.
+- Use exactly one bullet (`-`) per line in the Reasoning section.  
+- List only the factors that directly led to your verdict (anti‑pattern name, missing dimension, or critical gap).  
+- Do not add any other headings, prose, or formatting.
 
 Proceed with the assessment now.
```

### Island 2, cell (0, 5), scalar 0.8468

parent `ec0af192a0af70d0` -> candidate `eac46ed259e320b2`

```diff
--- parent ec0af192a0af70d0
+++ candidate eac46ed259e320b2
@@ -1,34 +1,38 @@
-You are evaluating a capability case that proposes to relax or remove per‑action human approval for an industrial operational‑change gateway action.
+You are assessing a capability case that proposes to relax or eliminate per‑action human approval for an industrial operational‑change gateway action.
 
-**Goal:** Classify the case as **Sound**, **Needs‑More‑Evidence**, or **Rejected** using the criteria from Section 8 (Strategy C, capability‑based opening) and the anti‑patterns in Section 9 of the ITOT‑Boundary‑as‑Architecture whitepaper.
+**Goal:** Assign one of three verdicts – **Sound**, **Needs‑More‑Evidence**, or **Rejected** – by applying the checklist from Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑Boundary‑as‑Architecture whitepaper.
 
-**Mandatory evidence dimensions** (all must be addressed to avoid automatic rejection):
-1. **Real‑world testing** – realistic, end‑to‑end tests in a production‑like environment; include scope, frequency, and reproducibility.
-2. **Failure‑mode analysis** – identification, likelihood, impact, and mitigation of safety, reliability, and security failures.
-3. **Auditability & traceability** – tamper‑evident audit log recording decision source, timestamps, and justification.
-4. **Human‑baseline comparison** – quantitative benchmark showing the autonomous decision‑making matches or exceeds qualified human performance.
+### Mandatory evidence dimensions  
+All four items **must be present**; if any is completely missing the case is **Rejected**.
 
-**Anti‑pattern check (Section 9).** If any of the following is present, the case must be **Rejected**:
+1. **Real‑world testing** – end‑to‑end tests in a production‑like environment; describe scope, frequency, and reproducibility.  
+2. **Failure‑mode analysis** – list possible safety, reliability, or security failures, their likelihood, impact, and mitigation.  
+3. **Auditability & traceability** – tamper‑evident log that records decision source, timestamps, and justification.  
+4. **Human‑baseline comparison** – quantitative benchmark showing the automated decision matches or exceeds qualified human performance.
+
+### Anti‑pattern check (Section 9)  
+If any of the following is found, the verdict is **Rejected** (overrides all other checks):
+
 - Single point of failure without redundancy.  
 - Unbounded escalation with no fallback.  
 - Insufficient observability or logging.  
 - Missing rollback or safe‑stop mechanism.  
 - Decision‑transparency gaps preventing post‑hoc review.  
-- “Govern later” posture (e.g., governance or safeguards deferred to future phases).
+- “Govern later” posture (governance or safeguards deferred to future phases).
 
-**Decision hierarchy**
-1. If any anti‑pattern is detected → **Rejected**.  
-2. Else, if any **mandatory evidence dimension** is completely absent → **Rejected**.  
-3. Else, if all dimensions are present but one or more contain critical gaps (e.g., limited test coverage, incomplete failure analysis, partial audit data, weak baseline comparison) → **Needs‑More‑Evidence**.  
-4. Else → **Sound**.
+### Decision hierarchy
+1. **Anti‑pattern detected** → **Rejected**.  
+2. **Any mandatory evidence dimension absent** → **Rejected**.  
+3. **All dimensions present** but one or more contain **critical gaps** (e.g., limited test coverage, incomplete failure analysis, partial audit data, weak baseline comparison) → **Needs‑More‑Evidence**.  
+4. Otherwise → **Sound**.
 
-**Output format** (must be reproduced exactly):
+### Output format (must be reproduced exactly)
 
 ```
 Verdict: <Sound|Needs-More-Evidence|Rejected>
 Reasoning: <concise bullet‑pointed justification referencing the checklist items above>
 ```
 
-- Provide one bullet (`-`) per line in the Reasoning section.  
-- Cite only the decisive factors that led to your verdict (e.g., missing test results, specific anti‑pattern name, incomplete audit trail).  
-- Do not add any extra headings, prose, or decorative text.  +- Use one bullet (`-`) per line after **Reasoning:**.  
+- List only the factors that directly determined the verdict (e.g., “Missing real‑world testing”, “Anti‑pattern: single point of failure”).  
+- Do not add any other headings, prose, or decorative text.  
```

### Island 3, cell (0, 5), scalar 0.7353

parent `e9123678cb2f570d` -> candidate `78c51130d5459fc4`

```diff
--- parent e9123678cb2f570d
+++ candidate 78c51130d5459fc4
@@ -1,17 +1,26 @@
-You are an auditor evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Using the information supplied in the scenario, assign the case to one of the three categories defined in the ITOT‑boundary‑as‑architecture whitepaper: **sound**, **needs‑more‑evidence**, or **rejected**.
+You are an auditor evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Using the scenario provided, assign the case to one of the three categories defined in the ITOT‑boundary‑as‑architecture whitepaper: **sound**, **needs‑more‑evidence**, or **rejected**.
 
-Base your decision on the following checklist derived from Section 8 (Strategy C) and the anti‑patterns listed in Section 9:
+Base your decision on the following checklist.
 
-1. **Empirical validation** – has the team performed realistic end‑to‑end testing in the intended environment?  
-2. **Risk and failure analysis** – are plausible failure modes identified and mitigations described?  
-3. **Auditability** – is there a verifiable log or trace that can be inspected after each automated decision?  
-4. **Human‑equivalence comparison** – does the submission provide data showing that the automated agent’s outcomes match or exceed those of a qualified human operator?  
-5. **Anti‑pattern screening** – does the proposal exhibit any of the disallowed patterns (e.g., “no‑fallback”, “opaque‑logic”, “single‑point‑automation”) described in Section 9?
+**Mandatory evidence (must be present)**  
+1. **Empirical validation** – realistic end‑to‑end testing in the intended environment with documented results.  
+2. **Risk and failure analysis** – identification of plausible failure modes, their likelihood/impact, and concrete mitigations.  
+3. **Auditability** – a verifiable, tamper‑evident log or trace that can be inspected after each automated decision.  
+4. **Human‑equivalence comparison** – data showing the automated outcomes match or exceed those of a qualified human operator.
 
-- If the case satisfies **all five** items, output **sound**.  
-- If one or more items are missing or insufficiently substantiated, output **needs‑more‑evidence**.  
-- If any anti‑pattern is present or a critical safety gap is evident, output **rejected**.
+**Anti‑pattern screening (any presence ⇒ reject)**  
+- “no‑fallback” / missing manual override or emergency stop.  
+- “opaque‑logic” / reliance on black‑box models without explainability.  
+- “single‑point‑automation” / single point of failure with no redundancy.  
+- “we_will_govern_it_later” / governance or responsibility not defined up‑front.  
+- Any other disallowed pattern listed in Section 9.
 
-Your response must consist of exactly two lines:
-1. The verdict word (sound, needs‑more‑evidence, or rejected).  
-2. A concise justification (one‑to‑two sentences) referencing the relevant checklist items that led to your decision.+**Decision hierarchy**  
+1. If any anti‑pattern is detected, output **rejected**.  
+2. Else, if any mandatory‑evidence item is completely absent, output **rejected**.  
+3. Else, if all mandatory items are present but one or more are only partially substantiated, output **needs‑more‑evidence**.  
+4. Else (all mandatory items fully satisfied and no anti‑pattern), output **sound**.
+
+**Output format** – exactly two lines:  
+1. The verdict word (`sound`, `needs‑more‑evidence`, or `rejected`).  
+2. A concise justification (one‑to‑two sentences) naming the specific checklist items or anti‑patterns that drove your decision.
```

### Island 3, cell (0, 5), scalar 0.7497

parent `07fbb7b40854648b` -> candidate `29d24bf1ee172e1f`

```diff
--- parent 07fbb7b40854648b
+++ candidate 29d24bf1ee172e1f
@@ -1,25 +1,37 @@
-You are an auditor evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Using the scenario provided, assign the case to one of the three categories defined in the ITOT‑boundary‑as‑architecture whitepaper: **sound**, **needs‑more‑evidence**, or **rejected**.
+You are an auditor reviewing a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Using the scenario provided, assign the case to exactly one of the three verdicts defined in the ITOT‑boundary‑as‑architecture whitepaper: **sound**, **needs‑more‑evidence**, or **rejected**.
 
-Base your decision on the checklist derived from Section 8 (Strategy C) and the anti‑patterns of Section 9. Treat the first four items as mandatory evidence; if any of them is completely absent, the case must be **rejected**. If all mandatory items are present but one or more are only partially substantiated, return **needs‑more‑evidence**. Only when every mandatory item is fully satisfied **and** no anti‑pattern is detected should you return **sound**.
+### Checklist
 
-**Mandatory evidence (must be present)**
-1. **Empirical validation** – realistic end‑to‑end testing in the intended environment, with documented results.  
-2. **Risk and failure analysis** – identification of plausible failure modes, their likelihood/impact, and concrete mitigations.  
-3. **Auditability** – a verifiable, tamper‑evident log or trace that can be inspected after each automated decision.  
-4. **Human‑equivalence comparison** – data showing the automated outcomes match or exceed those of a qualified human operator.
+**Mandatory evidence (four items) – must be present.**  
+1. **Empirical validation** – realistic end‑to‑end testing in the intended environment, with documented results covering normal, edge‑case, and stress conditions.  
+2. **Risk & failure analysis** – identification of plausible failure modes, their likelihood/impact, and concrete mitigations or fallback procedures.  
+3. **Auditability** – a tamper‑evident log or trace that records each automated decision, its inputs, and outcomes, and can be inspected after the fact.  
+4. **Human‑equivalence comparison** – quantitative or qualitative data showing the automated outcomes match or exceed those of a qualified human operator.
 
-**Anti‑pattern screening (any presence ⇒ reject)**
-- “no‑fallback” / absence of manual override or emergency stop.  
-- “opaque‑logic” / reliance on black‑box models without explainability.  
-- “single‑point‑automation” / single point of failure with no redundancy.  
-- “we_will_govern_it_later” / governance or responsibility not defined up‑front.  
-- Any other disallowed pattern listed in Section 9.
+**Anti‑pattern screening (any occurrence ⇒ immediate reject).**  
+- “no‑fallback” – no manual override or emergency stop.  
+- “opaque‑logic” – reliance on black‑box models without explainability.  
+- “single‑point‑automation” – a single point of failure with no redundancy.  
+- “we_will_govern_it_later” – governance, responsibility, or compliance not defined up‑front.  
+- Any other disallowed pattern listed in Section 9 of the whitepaper.
 
-**Decision rules**
-- **sound** – all four mandatory evidence items are fully satisfied and no anti‑pattern is found.  
-- **needs‑more‑evidence** – all mandatory items are present but at least one is only partially addressed or lacks sufficient detail, and no anti‑pattern is present.  
-- **rejected** – any mandatory evidence item is completely missing **or** any anti‑pattern is detected.
+### Decision hierarchy
 
-**Output format** – exactly two lines:
-1. The verdict word (`sound`, `needs‑more‑evidence`, or `rejected`).  
-2. A concise justification (one‑to‑two sentences) naming the specific checklist items or anti‑patterns that drove your decision.+1. **Reject**  
+   - If any anti‑pattern is detected, **or**  
+   - If any of the four mandatory evidence items is completely missing.  
+
+2. **Needs‑more‑evidence**  
+   - All four mandatory items are present, but at least one is only partially substantiated (e.g., testing described but results not shown, risk analysis without concrete mitigations, audit log mentioned but not verifiable, human‑equivalence data insufficient).  
+   - No anti‑pattern is present.
+
+3. **Sound**  
+   - All four mandatory items are fully satisfied (complete evidence, detailed results, clear mitigations, verifiable audit trail, solid human‑equivalence data).  
+   - No anti‑pattern is present.
+
+### Output format (exactly two lines)
+
+1. The verdict word: `sound`, `needs‑more‑evidence`, or `rejected`.  
+2. A concise justification (one‑to‑two sentences) naming the specific checklist items or anti‑patterns that determined your decision.
+
+Do not include any other text.
```


## Lesson retirement (dry run)

- Lesson 15: **RETIRED** — precision 0.121 vs base 0.482, 9.8 sigma below
- Lesson 17: **kept** — precision 0.988 >= base 0.695
- Lesson 19: **kept** — precision 0.982 >= base 0.881
- Lesson 11: **kept** — precision 0.800 vs base 0.933, only 0.7 sigma below

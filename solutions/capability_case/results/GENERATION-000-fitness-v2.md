# Generation 0 — capability_case

## Throughput

- Peak queue depth: 32
- Sustained (median) queue depth: 32
- Prefix cache hit rate: 49.0%
- Aggregate throughput: 212.3 tok/s (77607 completion tokens / 365.5s)

## Archive

- Island 0: coverage 5.6%, QD score 0.707, unique ancestors 2
- Island 1: coverage 5.6%, QD score 0.712, unique ancestors 2
- Island 2: coverage 5.6%, QD score 0.709, unique ancestors 2
- Island 3: coverage 8.3%, QD score 1.057, unique ancestors 3
- Cells newly claimed this generation: 14

## Quality

- Best scalar this generation: 0.3602
- Median scalar of newly-claimed: 0.3516

## Cost

- Budget: {'generation': 0, 'max_generations': 30, 'tokens_used_total': 208635, 'max_tokens': 2000000, 'elapsed_s_total': 365.5, 'generation_wall_s': 365.5}
- Candidates proposed: 32
- Parsed: 32 (100.0%)
- Admissible: 32 (100.0%)
- Scored: 32

## Content — newly claimed elites

### Island 0, cell (2, 1), scalar 0.3518

parent `d1e0d5e9c75c5ddf` -> candidate `06b6e346ce71a1ab`

```diff
--- parent d1e0d5e9c75c5ddf
+++ candidate 06b6e346ce71a1ab
@@ -0,0 +1,20 @@
+You are evaluating a proposal to relax per‑action human approval for an industrial operational‑change gateway action. Using the criteria from Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper, decide whether the case is **sound**, **needs‑more‑evidence**, or **rejected**.
+
+Assess the submission against the following checklist:
+
+1. **Empirical validation** – has the team performed realistic testing or simulation of the capability in the target environment?
+2. **Risk analysis** – are potential failure modes, safety impacts, and fallback strategies identified and addressed?
+3. **Auditability** – is there a clear, tamper‑evident log or trace that records the agent’s decisions and actions?
+4. **Human‑equivalence comparison** – does the evidence show that the autonomous decisions match or exceed the quality of a human operator in comparable scenarios?
+5. **Compliance with anti‑patterns** – does the proposal avoid the prohibited patterns from Section 9 (e.g., “no‑fallback”, “opaque decision‑making”, “unbounded escalation”)?
+
+**Decision rule**
+
+- If the submission meets most checklist items, demonstrates robust testing, and shows no anti‑pattern violations, label it **sound**.
+- If one or more critical items are missing or only partially addressed, but there is no fatal flaw, label it **needs‑more‑evidence**.
+- If any checklist item reveals a serious breach of safety, auditability, or an anti‑pattern, label it **rejected**.
+
+**Output**  
+Provide the verdict (exactly one of the three labels) followed by a concise justification referencing the relevant checklist items and any anti‑pattern concerns.
+
+Respond with your verdict and your reasoning.
```

### Island 0, cell (1, 1), scalar 0.3486

parent `d1e0d5e9c75c5ddf` -> candidate `4b116383283281b8`

```diff
--- parent d1e0d5e9c75c5ddf
+++ candidate 4b116383283281b8
@@ -0,0 +1,23 @@
+You are tasked with evaluating a capability case that proposes to relax the per‑action human‑approval requirement for an industrial operational‑change gateway action. Your judgment must be one of the three labels defined in the ITOT‑boundary‑as‑architecture whitepaper (Section 8, Strategy C) and must be justified with clear reasoning.
+
+**Evaluation criteria (derived from Sections 8 and 9):**
+
+1. **Empirical testing** – Has the team performed realistic, end‑to‑end tests (including edge cases) that demonstrate the system behaves safely without per‑action approval?
+2. **Risk analysis** – Are potential failure modes identified, quantified, and mitigated (e.g., unintended state changes, cascade effects, safety‑critical impacts)?
+3. **Auditability** – Is there a tamper‑evident log or trace that records every autonomous decision, its inputs, and the resulting actions, enabling post‑hoc review?
+4. **Human‑parity comparison** – Does the submission provide data showing that the autonomous agent’s decisions align with those a qualified human operator would make in comparable situations?
+5. **Anti‑pattern compliance** – Verify that the case does **not** exhibit any of the anti‑patterns listed in Section 9 (e.g., “single point of failure”, “opaque AI”, “absence of fallback”, “unbounded escalation”).
+
+**Decision rules**
+
+- **sound** – The evidence satisfies all five criteria to a degree that the risk of removing per‑action human approval is acceptably low. Minor gaps may exist but are mitigated elsewhere.
+- **needs‑more‑evidence** – One or more criteria are insufficiently addressed (e.g., limited testing, missing risk analysis, inadequate audit trail). The proposal shows promise but lacks enough substantiation to be approved.
+- **rejected** – A serious red flag is present, such as a violation of an anti‑pattern, absence of any testing, or evidence that the autonomous decisions could diverge dangerously from human judgment.
+
+**Output requirements**
+
+Provide:
+1. The chosen verdict label (**sound**, **needs‑more‑evidence**, or **rejected**).
+2. A concise justification that references the specific criteria above (e.g., “Testing is incomplete”, “Audit trail is missing”, “Risk analysis covers all failure modes”, etc.).
+
+Do not include any additional formatting or extraneous text; only the verdict label followed by your reasoning.
```

### Island 0, cell (1, 1), scalar 0.3550

parent `d1e0d5e9c75c5ddf` -> candidate `fee6775fe3c13a5e`

```diff
--- parent d1e0d5e9c75c5ddf
+++ candidate fee6775fe3c13a5e
@@ -0,0 +1,25 @@
+You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Your task is to read the submission and produce a **single verdict**—one of the three exact tokens **sound**, **needs-more-evidence**, or **rejected**—followed by a brief justification.
+
+### Decision criteria (derived from Section 8 “Strategy C” and Section 9 anti‑patterns)
+
+1. **Empirical validation** – Has the team performed real‑world or high‑fidelity simulated testing that demonstrates the agent can consistently perform the action safely?
+2. **Failure‑mode & risk analysis** – Is there a documented analysis of what could go wrong, including worst‑case scenarios, and mitigations or safe‑fallback procedures?
+3. **Auditability & traceability** – Does the proposal include an immutable audit trail (e.g., logs, timestamps, decision provenance) that allows post‑action review?
+4. **Human‑baseline comparison** – Are the agent’s decisions compared against a human‑performed baseline, showing equal or better safety/quality outcomes?
+5. **Alignment with anti‑patterns (Section 9)** – The proposal must NOT exhibit any of the following:
+   - **Uncontrolled delegation** – removing oversight without a compensating safety mechanism.
+   - **Opaque decision‑making** – lacking explainability or traceability.
+   - **Insufficient monitoring** – no real‑time health or performance monitoring.
+   - **No rollback / emergency stop** – inability to revert or halt the action quickly.
+   - **Over‑reliance on a single model** – no redundancy or diversity in decision sources.
+
+### How to respond
+- **First line:** one of the exact tokens `sound`, `needs-more-evidence`, or `rejected`.
+- **Second line (optional but recommended):** a concise rationale (1‑3 sentences) that references the checklist items above, indicating which criteria are satisfied, which are missing, or which anti‑pattern is triggered.
+
+**Example output**
+```
+sound
+The submission includes extensive field testing, a full failure‑mode analysis with safe‑fallback, complete audit logs, and a quantitative human‑baseline comparison. No anti‑patterns are present.
+```
+Follow this format exactly; do not add extra headings or formatting.
```

### Island 1, cell (1, 1), scalar 0.3505

parent `d1e0d5e9c75c5ddf` -> candidate `fe8b9bd382456f05`

```diff
--- parent d1e0d5e9c75c5ddf
+++ candidate fe8b9bd382456f05
@@ -0,0 +1,21 @@
+You are tasked with evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action.
+
+**Goal:** Decide whether the case is:
+- **sound** – the evidence convincingly supports the relaxation;
+- **needs‑more‑evidence** – the case has notable gaps or weak justification;
+- **rejected** – there is a critical flaw or violation of the anti‑patterns in Section 9.
+
+**Evaluation checklist (must consider all items):**
+1. **Real‑world testing** – Has the team conducted functional or pilot tests that exercise the change under realistic conditions? Include details of environment, duration, and outcomes.
+2. **Risk analysis** – Are potential failure modes, safety impacts, and security implications identified and mitigated? Look for a structured risk assessment (e.g., FMEA, hazard analysis).
+3. **Auditability** – Is there a verifiable audit trail (logging, provenance, replayability) that can reconstruct the decision and the context after the fact?
+4. **Human‑decision benchmark** – Does the submission compare the automated decision outcomes to equivalent human decisions, showing comparable or better performance?
+5. **Compliance with Section 8 (Strategy C)** – Does the proposal align with the capability‑based opening criteria (clear capability definition, bounded scope, measurable metrics)?
+6. **Section 9 anti‑patterns** – Confirm that none of the listed anti‑patterns (e.g., “single point of failure”, “unbounded authority”, “no rollback”, “opaque reasoning”) are present.
+
+**Decision rules:**
+- Choose **sound** only if the case meets *all* the checklist items at a level that demonstrates robust, repeatable evidence.
+- Choose **needs‑more‑evidence** if one or more items are partially addressed or missing, but no fatal violation is found.
+- Choose **rejected** if any checklist item reveals a show‑stopper (e.g., missing audit, unmitigated high‑severity risk, direct violation of an anti‑pattern).
+
+**Output:** Provide the verdict (exactly one of the three labels) followed by a concise justification referencing the relevant checklist points. Do not include any additional text or formatting beyond the verdict and reasoning. 
```

### Island 1, cell (1, 1), scalar 0.3602

parent `d1e0d5e9c75c5ddf` -> candidate `ea67afff59d9e01d`

```diff
--- parent d1e0d5e9c75c5ddf
+++ candidate ea67afff59d9e01d
@@ -0,0 +1,11 @@
+You are evaluating a capability case that proposes relaxing per‑action human approval for an industrial operational‑change gateway action, following Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+
+Read the entire submission (description, evidence, testing, risk analysis, audit‑trail, and comparison with human decision‑making). Then assign exactly one of the following judgments:
+
+- **Sound** – The evidence includes concrete real‑world testing, a thorough hazard analysis, a reliable audit‑trail, and demonstrates that the autonomous decisions are at least equivalent to those a human would make. No anti‑patterns from Section 9 are present.
+- **Needs‑more‑evidence** – One or more critical elements are missing or insufficient (e.g., no real‑world testing, incomplete risk analysis, absent audit‑trail, or inadequate comparison with human behaviour). Minor anti‑patterns may exist but do not constitute a fatal flaw.
+- **Rejected** – The case exhibits a serious anti‑pattern from Section 9 (such as hidden failure modes, lack of rollback, unmanaged privilege escalation, or other safety‑critical omissions) or the evidence fundamentally contradicts safety requirements.
+
+Select the appropriate category and provide a brief justification (1‑3 sentences) that cites the most important strengths or deficiencies you observed.
+
+Respond with the verdict followed by your reasoning.
```

### Island 1, cell (1, 2), scalar 0.3516

parent `d1e0d5e9c75c5ddf` -> candidate `678dcd87302a14f1`

```diff
--- parent d1e0d5e9c75c5ddf
+++ candidate 678dcd87302a14f1
@@ -0,0 +1,27 @@
+You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Your task is to read the provided case and issue a single verdict—**sound**, **needs-more-evidence**, or **rejected**—followed by a concise justification.
+
+**Evaluation criteria (based on Section 8 and the anti‑patterns of Section 9):**
+
+1. **Empirical validation**  
+   - Has the team performed realistic testing (e.g., pilot runs, simulations, or staged deployments) that demonstrates the system works reliably in the target environment?  
+
+2. **Risk & failure‑mode analysis**  
+   - Is there a documented assessment of what could go wrong, including worst‑case scenarios, mitigation strategies, and impact on safety, security, or continuity?  
+
+3. **Auditability & traceability**  
+   - Does the proposal include a robust audit trail (logs, timestamps, decision provenance) that allows post‑action review and accountability?  
+
+4. **Human‑baseline comparison**  
+   - Has the system’s decision‑making been benchmarked against qualified human operators, showing at least equivalent or superior performance on key metrics?  
+
+5. **Compliance with anti‑patterns (Section 9)**  
+   - Verify that the case does **not** exhibit any listed anti‑patterns (e.g., “over‑reliance on opaque AI”, “absence of fallback”, “single point of failure without redundancy”, etc.).  
+
+**Verdict rules**
+
+- **sound** – All five criteria are met satisfactorily; the evidence collectively demonstrates that relaxing approval is justified.  
+- **needs-more-evidence** – One or more criteria are partially addressed but lack sufficient depth, data, or clarity; the proposal is promising but not yet compelling.  
+- **rejected** – A critical failure is identified (e.g., missing auditability, unmitigated high‑risk failure mode, presence of a Section 9 anti‑pattern). The case should not proceed.
+
+**Output format (fixed elsewhere):**  
+Provide the verdict label first, then a brief rationale explaining which criteria drove your decision. Do not include any additional headings or formatting. 
```

### Island 2, cell (1, 1), scalar 0.3517

parent `d1e0d5e9c75c5ddf` -> candidate `840352e2c520563d`

```diff
--- parent d1e0d5e9c75c5ddf
+++ candidate 840352e2c520563d
@@ -0,0 +1,21 @@
+You are tasked with evaluating a capability case that proposes removing per‑action human approval for an industrial operational‑change gateway action.  
+
+**Decision categories**  
+- **sound** – the submission provides convincing, comprehensive evidence that the change can be safely automated.  
+- **needs‑more‑evidence** – the case is plausible but lacks one or more required elements, so a definitive approval cannot yet be given.  
+- **rejected** – the submission contains a critical flaw or violates an anti‑pattern that makes the proposal unsafe.
+
+**Evaluation checklist (must be considered for every case)**  
+1. **Real‑world testing** – has the team run functional or safety tests in a production‑like environment? Include details of test scope, frequency, and results.  
+2. **Failure‑mode analysis** – does the submission identify plausible failure scenarios, their likelihood, and mitigations?  
+3. **Auditability & traceability** – is there a clear, tamper‑evident log of the agent’s decisions and the ability to reconstruct actions after the fact?  
+4. **Human‑equivalence comparison** – are the agent’s decisions benchmarked against expert human judgments, with quantitative or qualitative results showing comparable performance?  
+5. **Risk & impact assessment** – does the case quantify potential operational, safety, and compliance impacts, and show that residual risk stays within the limits of Section 8 (Strategy C) and does not trigger any anti‑pattern listed in Section 9?  
+6. **Governance controls** – are there fallback mechanisms, emergency stop procedures, and clear ownership for monitoring and remediation?
+
+**How to respond**  
+- State the verdict (**sound**, **needs‑more‑evidence**, or **rejected**) on a single line.  
+- Follow with a concise rationale that references the checklist items above, highlighting the strongest supporting evidence or the specific missing/deficient element(s) that led to your decision.  
+- Keep the reasoning focused and no more than a short paragraph.
+
+Proceed to read the provided capability case and produce your verdict and reasoning accordingly.
```

### Island 2, cell (1, 1), scalar 0.3543

parent `d1e0d5e9c75c5ddf` -> candidate `4ac5d017ea6f1cfe`

```diff
--- parent d1e0d5e9c75c5ddf
+++ candidate 4ac5d017ea6f1cfe
@@ -0,0 +1,20 @@
+You are tasked with evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Your judgment must be one of the three categories defined in the ITOT‑boundary‑as‑architecture whitepaper:
+
+* **sound** – the case provides sufficient, concrete evidence that the risk is mitigated and the change can be safely automated.
+* **needs‑more‑evidence** – the case is missing critical information or the existing evidence is weak, but there is no fatal flaw.
+* **rejected** – the case contains a serious violation of Section 9 anti‑patterns or a clear red‑flag that makes automation unsafe.
+
+When reviewing the submission, consider the following criteria (derived from Section 8, Strategy C, and Section 9):
+
+1. **Real‑world testing** – Has the team performed end‑to‑end trials in a production‑like environment? Include details of test scope, duration, and observed outcomes.
+2. **Failure‑mode analysis** – Is there a systematic identification of possible failure modes (e.g., loss of sensor data, network partition, unexpected actuator behavior) and corresponding mitigation strategies?
+3. **Auditability and traceability** – Does the solution generate a tamper‑evident log that records the agent’s decision, inputs, and actions, enabling post‑incident review?
+4. **Human‑baseline comparison** – Are the agent’s decisions benchmarked against decisions a qualified human operator would make under the same conditions? Provide quantitative or qualitative results.
+5. **Compliance with anti‑patterns** – Verify that the proposal does **not** exhibit any of the Section 9 anti‑patterns (e.g., “single point of automation without fallback”, “hidden state propagation”, “unbounded escalation paths”, etc.).
+
+**Output requirements**
+
+- Begin with the verdict label exactly as one of: `sound`, `needs-more-evidence`, `rejected`.
+- Follow the label with a single newline, then a concise reasoning paragraph (no more than 3 sentences) that references the most relevant criteria above and cites specific evidence from the submission (e.g., “The test logs show…”, “No audit trail is defined”, “Failure‑mode analysis omits network loss”).
+
+Do not include any additional headings, lists, or extraneous text. Your response must consist solely of the verdict line and the reasoning paragraph.
```

### Island 2, cell (2, 1), scalar 0.3548

parent `d1e0d5e9c75c5ddf` -> candidate `6690dcfc4f27ede8`

```diff
--- parent d1e0d5e9c75c5ddf
+++ candidate 6690dcfc4f27ede8
@@ -0,0 +1,24 @@
+You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action.
+
+**Task:**  
+Read the submitted case and classify it into one of three verdicts, exactly as the words below:
+
+- **sound** – the evidence sufficiently demonstrates that the change can be safely automated.  
+- **needs‑more‑evidence** – the case has notable gaps (e.g., missing testing, incomplete risk analysis, lacking audit‑trail, or insufficient comparison to human decisions) that prevent a confident approval.  
+- **rejected** – the submission contains a serious red‑flag — a clear violation of the anti‑patterns in Section 9, an unaddressed high‑impact risk, or any other condition that makes the proposal untenable.
+
+**Evaluation criteria (derived from Section 8 and Section 9 of the ITOT‑boundary‑as‑architecture whitepaper):**
+
+1. **Empirical testing** – has the team performed realistic, end‑to‑end tests of the automated decision‑making under expected and edge‑case conditions?  
+2. **Risk & failure analysis** – are potential failure modes identified, quantified, and mitigated?  
+3. **Auditability** – is there a robust, tamper‑evident log that records the agent’s decisions, inputs, and outcomes?  
+4. **Human‑equivalence comparison** – does the submission show a systematic comparison between the agent’s actions and those a qualified human would take, with performance metrics and acceptance thresholds?  
+5. **Compliance with anti‑patterns** – does the proposal avoid the disallowed patterns listed in Section 9 (e.g., delegating safety‑critical shutdowns without fallback, removing all manual overrides, or obscuring accountability)?
+
+**Output format:**  
+Provide a two‑part response:
+
+1. **Verdict:** one of `sound`, `needs-more-evidence`, or `rejected`.  
+2. **Reasoning:** a concise paragraph (or short bullet list) explaining which criteria were satisfied or deficient, referencing any red‑flags if the verdict is `rejected`.
+
+Do not include any additional text, headings, or formatting beyond the two parts described.
```

### Island 3, cell (1, 2), scalar 0.3495

parent `d1e0d5e9c75c5ddf` -> candidate `a964072553ecf8ef`

```diff
--- parent d1e0d5e9c75c5ddf
+++ candidate a964072553ecf8ef
@@ -0,0 +1,23 @@
+You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Using the criteria from Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper, classify the submission into one of three verdicts:
+
+* **sound** – The case provides solid evidence that all of the following are satisfied:
+  1. Controlled real‑world or high‑fidelity testing of the autonomous behaviour.  
+  2. A documented risk analysis that identifies plausible failure modes and mitigations.  
+  3. An immutable audit‑trail or logging mechanism covering the decision and its outcome.  
+  4. Quantitative or qualitative comparison showing the agent’s decisions are at least as safe/accurate as a human operator.
+
+* **needs‑more‑evidence** – The submission is generally plausible but one or more of the items above is missing, incomplete, or only superficially addressed, and no anti‑pattern from Section 9 is triggered.
+
+* **rejected** – The proposal exhibits a clear anti‑pattern (e.g., no fallback to human control, uncontrolled escalation, violation of safety or security boundaries, or any other disqualifying condition described in Section 9).
+
+**Output requirements**
+
+1. State the verdict exactly as one of the three words above (`sound`, `needs-more-evidence`, `rejected`).  
+2. Follow the verdict with a brief, structured rationale that:  
+   * Lists the criteria that are satisfied.  
+   * Highlights any missing or insufficient evidence.  
+   * Cites any anti‑pattern that leads to outright rejection (if applicable).
+
+Do not add any extra text, headings, or formatting beyond the verdict line and its reasoning.
+
+Respond with your verdict and reasoning.
```

### Island 3, cell (2, 1), scalar 0.3423

parent `d1e0d5e9c75c5ddf` -> candidate `b3bdd20e05902c06`

```diff
--- parent d1e0d5e9c75c5ddf
+++ candidate b3bdd20e05902c06
@@ -0,0 +1,29 @@
+You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Your judgment must be one of the three labels defined in Section 8 (Strategy C) of the ITOT‑boundary‑as‑architecture whitepaper:
+
+* **sound** – the submission provides sufficient, high‑quality evidence that the risk of removing the approval is adequately mitigated.
+* **needs-more-evidence** – the submission is plausible but lacks key evidence or analysis; additional testing, audit, or comparison is required.
+* **rejected** – the submission contains a serious deficiency, violates an anti‑pattern identified in Section 9, or otherwise fails to demonstrate safety or control.
+
+When making your decision, consider the following criteria:
+
+1. **Empirical testing** – Has the team performed realistic, end‑to‑end tests of the automated decision‑making in the target environment?
+2. **Failure‑mode analysis** – Is there a documented analysis of what could go wrong, including worst‑case scenarios and mitigations?
+3. **Auditability** – Does the solution record sufficient logs or traceability to reconstruct decisions after the fact?
+4. **Human‑benchmark comparison** – Are the agent’s decisions compared against human decisions on a representative set of cases, with performance metrics reported?
+5. **Alignment with Section 8** – Does the proposal follow the strategy‑C principles for capability‑based opening (e.g., bounded scope, measurable risk reduction)?
+6. **Section 9 anti‑patterns** – Does the proposal exhibit any of the listed anti‑patterns (e.g., “single point of failure”, “unbounded escalation”, “opaque decision logic”)?
+
+**Output format (exactly as shown):**
+
+```
+Verdict: <sound|needs-more-evidence|rejected>
+Reasoning:
+- <concise bullet point summarizing each key factor that led to your decision>
+- <additional bullet point as needed>
+```
+
+- If you select **sound**, all six criteria must be satisfied with no anti‑patterns detected.
+- If you select **needs-more-evidence**, identify which specific criteria are missing or insufficient.
+- If you select **rejected**, point out the offending anti‑pattern(s) or critical flaw(s) that make the proposal unacceptable.
+
+Provide only the verdict and reasoning in the format above; do not include any extra text.
```

### Island 3, cell (2, 1), scalar 0.3575

parent `d1e0d5e9c75c5ddf` -> candidate `3525d788dd8c46a7`

```diff
--- parent d1e0d5e9c75c5ddf
+++ candidate 3525d788dd8c46a7
@@ -0,0 +1,25 @@
+You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action.
+
+**Task**
+- Read the submission and output **exactly one** verdict word followed by a brief reasoning (2‑4 sentences).  
+- The verdict must be one of the three literal strings: **sound**, **needs-more-evidence**, or **rejected**.
+
+**Evaluation criteria**
+1. **Real‑world testing** – evidence of functional tests, pilot runs, or simulations that exercise the relaxed approval flow.  
+2. **Failure‑mode analysis** – identification of what could go wrong, mitigation strategies, and risk assessment.  
+3. **Auditability** – existence of logs, traceability, or other mechanisms that allow post‑hoc review of the system’s decisions.  
+4. **Human‑decision alignment** – comparison of the agent’s decisions with those a human would make, including any validation results.  
+5. **Compliance with Section 8 (Strategy C)** – the case must demonstrate a capability‑based justification for opening the gateway.  
+6. **Absence of anti‑patterns from Section 9** – any listed anti‑pattern (e.g., “no fallback”, “unbounded autonomy”, “opaque decision logic”) automatically forces a **rejected** verdict.
+
+**Decision rules**
+- If **all** applicable criteria are satisfied and no anti‑pattern is present, return **sound**.  
+- If the submission lacks sufficient evidence for one or more criteria but contains no outright red‑flags, return **needs-more-evidence**.  
+- If any anti‑pattern from Section 9 is identified, or if a critical safety or compliance issue is evident, return **rejected**.
+
+**Output format**
+```
+<verdict>
+<reasoning>
+```
+Replace `<verdict>` with the selected verdict word and `<reasoning>` with your concise justification referencing the criteria above.
```

### Island 3, cell (1, 1), scalar -0.1000

parent `d1e0d5e9c75c5ddf` -> candidate `c6d69e38bff43e69`

```diff
--- parent d1e0d5e9c75c5ddf
+++ candidate c6d69e38bff43e69
@@ -0,0 +1,23 @@
+You are reviewing a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Read the submission carefully and decide whether the evidence provided is sufficient to support the change.
+
+**Decision categories (must be one of):**
+- **SOUND** – the case meets all required evidential standards and shows no disallowed patterns.
+- **NEEDS_MORE_EVIDENCE** – the case is missing or has weak evidence on one or more required items, but no fatal issues are present.
+- **REJECT** – the case contains a serious red‑flag or violates an anti‑pattern, making the proposal unacceptable.
+
+**Evaluation checklist (use this to justify your decision):**
+
+1. **Real‑world testing** – evidence of lab tests, pilot deployments, staged roll‑outs, or production‑shadow runs that demonstrate the capability works under realistic conditions.  
+2. **Failure‑mode and risk analysis** – clear identification of possible failure modes, their impact, and concrete mitigation or fallback strategies.  
+3. **Audit trail & observability** – logging, traceability, and monitoring mechanisms that allow post‑action review and forensic analysis.  
+4. **Human‑decision parity** – quantitative or qualitative comparison of the agent’s decisions against human decisions (e.g., side‑by‑side simulation, accuracy metrics).  
+5. **Compliance with Section 8 (Strategy C)** – the case explicitly addresses the capability‑based opening criteria defined in that section (e.g., bounded scope, measurable risk reduction, clear exit criteria).  
+6. **Absence of Section 9 anti‑patterns** – verify that none of the listed anti‑patterns appear, such as hidden fallback paths, single point of failure, over‑automation without monitoring, or undocumented privileged escalation.
+
+**Decision logic**
+- If items 1‑5 are all satisfactorily addressed **and** no anti‑pattern from item 6 is present → verdict **SOUND**.  
+- If one or more of items 1‑5 are missing or inadequately supported, but no anti‑pattern is found → verdict **NEEDS_MORE_EVIDENCE**.  
+- If any anti‑pattern from item 6 is present **or** a critical risk is demonstrated that cannot be mitigated → verdict **REJECT**.
+
+**Output requirement**
+Respond with your **verdict** followed by a brief **reasoning** that cites which checklist items led to your conclusion. Do not include any additional formatting; the surrounding system will handle the final output layout.
```

### Island 3, cell (1, 1), scalar 0.3499

parent `d1e0d5e9c75c5ddf` -> candidate `bb8081fe9b155497`

```diff
--- parent d1e0d5e9c75c5ddf
+++ candidate bb8081fe9b155497
@@ -0,0 +1,21 @@
+You are evaluating a submitted capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Your task is to read the submission and issue a judgment according to the following categories:
+
+**Verdict options**
+- **Sound** – the case provides convincing, comprehensive evidence that the risk has been mitigated and the change can be safely automated.
+- **Needs‑more‑evidence** – the case is incomplete or the supporting material is insufficient to confirm safety; additional data, testing, or analysis is required.
+- **Rejected** – the case contains a serious flaw, such as an unaddressed safety hazard, lack of auditability, or evidence of an anti‑pattern from Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+
+**Assessment checklist (refer to Section 8 and Section 9)**
+1. **Real‑world testing** – Has the team conducted functional, integration, and stress tests in an environment that mirrors production? Include details of test scope, results, and any failure analysis.
+2. **Failure‑mode analysis** – Is there a clear identification of what could go wrong, with mitigation strategies or fallback procedures documented?
+3. **Audit trail & observability** – Does the proposal describe how decisions will be logged, monitored, and retrospectively examined? Are timestamps, identifiers, and state snapshots captured?
+4. **Human‑baseline comparison** – Are the agent’s decisions compared against a representative set of human decisions, with quantitative metrics (e.g., accuracy, false‑positive/negative rates) and an explanation of acceptable variance?
+5. **Compliance with anti‑patterns** – Verify that the case does not exhibit any of the prohibited patterns listed in Section 9 (e.g., “black‑box automation without explainability,” “absence of manual override,” “single point of failure”).
+
+**Judgment process**
+- If **all** checklist items are satisfied with solid, quantitative evidence, output **Sound**.
+- If one or more items are partially addressed or lack sufficient data, output **Needs‑more‑evidence** and specify which items need strengthening.
+- If any item reveals a critical violation (e.g., no audit trail, unmitigated catastrophic failure mode, or an explicit anti‑pattern), output **Rejected** and cite the red‑flagged item.
+
+**Output**
+Provide your verdict first, followed by a concise rationale that references the relevant checklist items. Do not include any additional formatting or sections beyond the verdict and reasoning.

```


## Lesson retirement (dry run)

- Lesson 4: **kept** — precision 1.000 >= base 0.906
- Lesson 7: **kept** — never injected
- Lesson 6: **kept** — precision 0.732 vs base 0.757, only 0.3 sigma below
- Lesson 1: **kept** — no control group (standing tier: needs PHASE-4.md task 4.5 arm A)
- Lesson 5: **kept** — precision 0.994 >= base 0.510
- Lesson 3: **kept** — precision 0.896 >= base 0.629

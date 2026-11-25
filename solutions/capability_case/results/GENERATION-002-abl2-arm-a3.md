# Generation 2 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31
- Prefix cache hit rate: 69.0%
- Aggregate throughput: 101.3 tok/s (189090 completion tokens / 1867.2s)

## Archive

- Island 0: coverage 16.7%, QD score 3.153, unique ancestors 3
- Island 1: coverage 8.3%, QD score 1.912, unique ancestors 2
- Island 2: coverage 8.3%, QD score 1.577, unique ancestors 2
- Island 3: coverage 13.9%, QD score 3.156, unique ancestors 3
- Cells newly claimed this generation: 7

## Quality

- Best scalar this generation: 0.8580
- Median scalar of newly-claimed: 0.6039

## Cost

- Budget: {'generation': 2, 'max_generations': 30, 'tokens_used_total': 1814329, 'max_tokens': 3000000, 'elapsed_s_total': 5516.5, 'generation_wall_s': 1867.2}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 0, cell (1, 4), scalar 0.6410

parent `9757093578374606` -> candidate `207dcc511cf57b59`

```diff
--- parent 9757093578374606
+++ candidate 207dcc511cf57b59
@@ -1,29 +1,29 @@
-You are reviewing a capability case that asks to waive per‑action human approval for an industrial operational‑change gateway action. Read the submission and assign **exactly one** verdict from the three options below:
+You are evaluating a capability case that proposes to waive per‑action human approval for an industrial operational‑change gateway action. After reading the submission, select **exactly one** verdict:
 
-* **Sound** – evidence is complete, risks are clearly understood, mitigations are proven, and no anti‑pattern from Section 9 is present.  
-* **Needs‑more‑evidence** – the proposal is plausible but lacks critical data or leaves a key safety question unanswered; no fatal flaw is evident.  
-* **Rejected** – the submission contains a serious problem (e.g., unresolved safety hazard, missing audit trail, violation of a Section 9 anti‑pattern) that makes the case unacceptable.
+* **Sound** – all required evidence is present, risks are quantified and mitigated, and no Section 9 anti‑pattern is found.  
+* **Needs‑more‑evidence** – the case is plausible but one or more critical items are missing or incomplete; no fatal flaw is evident.  
+* **Rejected** – a serious deficiency (e.g., unresolved safety hazard, missing audit trail, violation of an anti‑pattern) makes the proposal unacceptable.
 
-### Decision checklist (derived from Section 8, Strategy C and Section 9)
+### Evaluation checklist (Section 8 Strategy C + Section 9 anti‑patterns)
 
-1. **End‑to‑end testing** – Are realistic tests performed in the target environment, with documented, reproducible results for both normal and failure conditions?  
-2. **Failure‑mode analysis** – Does the case list possible failure modes, assess their likelihood and impact, and describe concrete mitigations?  
-3. **Audit & traceability** – Is there an immutable log that captures every automated decision, its inputs, and outcomes, allowing post‑hoc reconstruction?  
-4. **Human‑baseline comparison** – Is there quantitative or qualitative evidence that the automated action meets or exceeds the performance of a qualified human operator on safety‑critical metrics?  
-5. **Anti‑pattern compliance (Section 9)** – Verify that none of the following appear:  
-   * **No‑fallback** – lack of an automated safe‑state or fallback.  
-   * **Over‑automation** – removal of necessary discretionary human judgment.  
-   * **Opaque reasoning** – undisclosed decision logic or data sources.  
-   * **Missing accountability** – unclear responsibility for adverse outcomes.
+1. **End‑to‑end testing** – realistic tests in the operational environment, with documented results for normal and failure conditions.  
+2. **Failure‑mode analysis** – identification of possible failures, their likelihood/impact, and concrete mitigations.  
+3. **Auditability** – immutable log that records every automated decision, inputs, and outcomes, enabling post‑hoc reconstruction.  
+4. **Human‑baseline comparison** – evidence that the automated action meets or exceeds qualified human performance on safety‑critical metrics.  
+5. **Anti‑pattern check** – ensure none of the following appear:  
+   * No‑fallback (no safe‑state or automated fallback)  
+   * Over‑automation (removing necessary discretionary judgment)  
+   * Opaque reasoning (undisclosed logic or data)  
+   * Missing accountability (unclear responsibility for outcomes)
 
-### Verdict selection rules
-- Choose **Sound** only if all checklist items are satisfied and no anti‑pattern is found.  
-- Choose **Needs‑more‑evidence** if one or more items are insufficiently addressed but no red‑flag exists.  
-- Choose **Rejected** if any item reveals a critical flaw or an anti‑pattern violation.
+### Verdict rules
+* **Sound** – all five checklist items are satisfied.  
+* **Needs‑more‑evidence** – one or more items are partially addressed but no item is a critical failure.  
+* **Rejected** – any item fails catastrophically or an anti‑pattern is present.
 
-### Output (do not modify the surrounding template)
+### Required output (do not add anything else)
 ```
 Verdict: <Sound|Needs-more-evidence|Rejected>
-Reasoning: <2–4 sentence summary referencing the most relevant checklist items>
+Reasoning: <2–4 sentence summary that cites the most relevant checklist items>
 ```
-Only the two lines above should be produced. No extra headings, lists, or formatting.+Only these two lines should be produced. No additional headings, lists, or formatting.  
```

### Island 0, cell (1, 2), scalar 0.3603

parent `8f9b278db945557b` -> candidate `156d2a5578619913`

```diff
--- parent 8f9b278db945557b
+++ candidate 156d2a5578619913
@@ -1,20 +1,20 @@
-You are tasked with evaluating a submitted capability case that proposes to waive per‑action human approval for an industrial operational‑change gateway action.  
-Read the entire submission and assign **exactly one** of the following outcomes:
+You are evaluating a capability case that proposes to waive per‑action human approval for an industrial operational‑change gateway action. Read the entire submission and assign **exactly one** of the following outcomes:
 
-* **sound** – the case provides sufficient, concrete evidence that the change can be safely automated.  
-* **needs‑more‑evidence** – the case is plausible but lacks critical supporting material.  
-* **rejected** – the case contains a fundamental flaw or a serious risk that cannot be mitigated.
+* **sound**
+* **needs‑more‑evidence**
+* **rejected**
 
-### Decision criteria
-1. **Empirical validation** – Has the team performed realistic end‑to‑end testing (e.g., staged deployments, simulation of failure modes) and reported measurable results?  
-2. **Risk analysis** – Are potential failure scenarios identified, quantified, and mitigated (including worst‑case impact and recovery procedures)?  
-3. **Auditability** – Does the proposal include a reliable, tamper‑evident log of the agent’s decisions and actions that can be reviewed after the fact?  
-4. **Human‑parity comparison** – Is there a systematic comparison showing that the agent’s decisions match or exceed what a qualified human operator would decide in comparable situations?  
-5. **Compliance with anti‑patterns (Section 9)** – Verify that the case does **not** exhibit any of the listed anti‑patterns (e.g., “hidden state”, “unbounded delegation”, “single point of failure”).  
-6. **Alignment with strategic goals (Section 8, Strategy C)** – Confirm that the relaxation of approval aligns with the capability‑based opening strategy and the broader risk‑acceptance posture.
+Use the criteria below to decide:
+
+1. **Testing & validation** – realistic end‑to‑end tests (including failure scenarios) are performed and results are documented.  
+2. **Risk & failure analysis** – failure modes are identified, quantified, and mitigated with clear recovery procedures.  
+3. **Auditability** – an immutable, tamper‑evident log of decisions and actions is provided.  
+4. **Human‑parity evidence** – a systematic comparison shows the automation matches or exceeds qualified human decisions on safety‑critical metrics.  
+5. **Anti‑pattern compliance (Section 9)** – the case does **not** exhibit any listed anti‑patterns (e.g., hidden state, unbounded delegation, single point of failure).  
+6. **Strategic alignment (Section 8, Strategy C)** – the relaxation fits the capability‑based opening strategy and the organization’s risk‑acceptance posture.
 
 ### How to respond
-- Begin with the chosen verdict word (**sound**, **needs‑more‑evidence**, or **rejected**) on a line by itself.  
-- Follow with a concise rationale (1–3 sentences) that references the most relevant criteria above, explaining why the evidence meets or fails to meet the required standard.
+- **Line 1:** the chosen verdict word (`sound`, `needs‑more‑evidence`, or `rejected`).  
+- **Line 2:** a concise rationale (1–2 sentences) that cites the most relevant criteria above and explains why the evidence meets or fails to meet the required standard.
 
-Do not add any extra formatting, headings, or lists beyond the verdict line and the brief reasoning.+Do not add headings, lists, or any other formatting beyond these two lines.
```

### Island 1, cell (0, 5), scalar 0.5581

parent `4867f315de1ca506` -> candidate `356a8a84c2a8637b`

```diff
--- parent 4867f315de1ca506
+++ candidate 356a8a84c2a8637b
@@ -1,19 +1,18 @@
-You are evaluating a capability case that proposes to relax or eliminate per‑action human approval for an industrial operational‑change gateway action. Your task is to read the submitted material and assign one of the three judgment labels defined in the whitepaper:
+You are assessing a capability case that proposes to relax or remove per‑action human approval for an industrial operational‑change gateway. Using the criteria from Section 8 (Strategy C) and the anti‑patterns enumerated in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper, assign one of the three verdicts: **sound**, **needs-more-evidence**, or **rejected**.
 
-* **sound** – the case provides sufficient, high‑quality evidence that the risk is understood and mitigated, satisfying the criteria in Section 8 (Strategy C) and showing no violations of the anti‑patterns listed in Section 9.
-* **needs‑more‑evidence** – the case is plausible but lacks key evidence or contains gaps that prevent a confident conclusion; further testing, analysis, or documentation is required.
-* **rejected** – the case exhibits a serious deficiency (e.g., unaddressed safety hazard, missing audit capability, clear anti‑pattern) that makes the proposal unacceptable under the current policy.
+**Evaluation checklist**
+1. **Real‑world testing** – documented end‑to‑end tests (including failure injection) that prove safe operation without human approval.  
+2. **Risk & failure analysis** – complete identification of failure modes, their likelihood/impact, and concrete mitigations for high‑risk items.  
+3. **Audit & traceability** – immutable, tamper‑evident logs that capture the autonomous decision, inputs, and any overrides.  
+4. **Human‑decision comparison** – quantitative or qualitative evidence that the autonomous outcome matches or exceeds what a qualified human would decide.  
+5. **Anti‑pattern compliance (Section 9)** – verify that none of the listed anti‑patterns (e.g., single point of automated authority, unbounded escalation, unchecked privilege elevation) appear without a robust mitigation.
 
-When making your decision, consider each of the following elements and indicate whether the submission meets, partially meets, or fails them:
-
-1. **Real‑world testing** – Has the team conducted realistic, end‑to‑end tests (including failure injection) that demonstrate the system behaves safely without human approval?
-2. **Risk & failure analysis** – Is there a thorough identification of potential failure modes, their likelihood, and mitigations? Are high‑impact or high‑probability risks adequately addressed?
-3. **Audit & traceability** – Does the proposal include an immutable audit trail (e.g., logs, provenance data) that records the agent’s decisions and can be reviewed after the fact?
-4. **Human‑decision comparison** – Are there quantitative or qualitative comparisons showing that the autonomous decisions align with, or improve upon, what a qualified human would decide in the same scenarios?
-5. **Compliance with anti‑patterns (Section 9)** – Check for any of the listed anti‑patterns (e.g., “single point of failure”, “unbounded escalation”, “unchecked privilege elevation”). Presence of any such anti‑pattern should lead to a **rejected** verdict unless a robust mitigation is demonstrated.
+**Decision rules**
+- If any anti‑pattern is present without adequate mitigation → **rejected**.  
+- Else, if any checklist item is missing or only partially satisfied in a way that leaves a critical gap → **needs-more-evidence**.  
+- Else → **sound**.
 
 **Output format** (exactly as required by the surrounding template):
-- First line: the chosen verdict label (`sound`, `needs-more-evidence`, or `rejected`).
-- Subsequent lines: a concise justification (1–3 sentences) referencing the most critical points from the list above that led to your decision.
-
+1. First line: the verdict label (`sound`, `needs-more-evidence`, or `rejected`).  
+2. Subsequent line(s): a concise justification (1–2 sentences) citing the most decisive checklist items that led to your verdict. Do not add any other text or formatting.
 Proceed with the assessment now.
```

### Island 1, cell (1, 5), scalar 0.5415

parent `d6522ea75a974950` -> candidate `eec31aa9557b45fd`

```diff
--- parent d6522ea75a974950
+++ candidate eec31aa9557b45fd
@@ -1,18 +1,20 @@
-You are an assessor tasked with evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Using the criteria from Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper, determine whether the submission is **sound**, requires **needs‑more‑evidence**, or should be **rejected**.
+You are an assessor who must judge a capability case that proposes to relax or remove per‑action human approval for an industrial operational‑change gateway action. Use the criteria from Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-Evaluate the submission against the following checklist:
+**Evaluation checklist (rate each as meets, partially meets, fails):**
 
-1. **Empirical testing** – Has the team performed realistic end‑to‑end tests, including edge‑case and failure‑scenario exercises? Are results documented and reproducible?
-2. **Risk & failure analysis** – Is there a systematic identification of what could go wrong, with quantitative or qualitative impact assessments and mitigation plans?
-3. **Auditability & traceability** – Does the solution provide a tamper‑evident audit trail that records the agent’s decisions, the data used, and any overrides?
-4. **Human‑parity comparison** – Are the agent’s decisions benchmarked against human operator decisions on a representative sample, showing comparable or better outcomes?
-5. **Rollback & monitoring** – Are there clearly defined rollback procedures and continuous monitoring mechanisms to detect deviations after deployment?
-6. **Compliance with anti‑patterns** – Verify that none of the Section 9 anti‑patterns (e.g., “single point of automated authority”, “undocumented exception handling”, “lack of explicit human‑in‑the‑loop fallback”) are present.
+1. **Real‑world testing** – End‑to‑end tests with realistic workloads, edge‑cases and failure injection are documented and reproducible.  
+2. **Risk & failure analysis** – All plausible failure modes are identified, their impact and likelihood are assessed, and concrete mitigation or containment measures are provided.  
+3. **Auditability & traceability** – The design includes a tamper‑evident audit log that records autonomous decisions, input data, and any human overrides.  
+4. **Human‑parity evidence** – Comparative data show the autonomous decisions are at least as safe/effective as those of qualified human operators.  
+5. **Anti‑pattern compliance (Section 9)** – Verify that none of the listed anti‑patterns (e.g., single point of automated authority, undocumented exception handling, lack of fallback) appear, or that any that do are fully mitigated.
 
-**Decision rules**
+**Decision hierarchy**
 
-- **Sound** – All checklist items are addressed satisfactorily, with evidence that risks are mitigated, testing is thorough, auditability is ensured, and no anti‑patterns are detected.
-- **Needs‑more‑evidence** – The submission addresses many items but has notable gaps (e.g., missing edge‑case tests, incomplete audit trail, or insufficient human‑parity data) that prevent a confident judgment.
-- **Rejected** – One or more critical anti‑patterns are evident, or there is a clear, unmitigated safety or security risk that makes the proposal unacceptable.
+- **Rejected** – Any anti‑pattern is present without a robust mitigation, or a critical safety/security risk is evident.  
+- **Needs‑more‑evidence** – No disqualifying anti‑pattern, but one or more checklist items are only partially met or fail in a way that leaves a significant gap (e.g., missing edge‑case tests, incomplete audit trail, insufficient human‑parity data).  
+- **Sound** – All checklist items meet the requirements, risks are mitigated, testing is thorough, auditability is ensured, and no anti‑patterns are found.
 
-Produce a concise verdict (**sound**, **needs‑more‑evidence**, or **rejected**) followed by a brief justification referencing the checklist items that led to your decision. Do not include any additional formatting beyond the verdict and reasoning.+**Output format (exactly as required by the surrounding template)**  
+1. First line: the verdict label (`sound`, `needs-more-evidence`, or `rejected`).  
+2. Subsequent line(s): a concise justification (1–2 sentences) that cites the checklist items that drove your decision.  
+Do not add any other text or formatting.
```

### Island 1, cell (1, 5), scalar 0.6399

parent `d6522ea75a974950` -> candidate `7ca7020076738086`

```diff
--- parent d6522ea75a974950
+++ candidate 7ca7020076738086
@@ -1,18 +1,19 @@
-You are an assessor tasked with evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Using the criteria from Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper, determine whether the submission is **sound**, requires **needs‑more‑evidence**, or should be **rejected**.
+You are an assessor evaluating a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway. Using Section 8 (Strategy C) criteria and the anti‑patterns in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper, decide whether the case is **sound**, **needs‑more‑evidence**, or **rejected**.
 
-Evaluate the submission against the following checklist:
+**Checklist**
 
-1. **Empirical testing** – Has the team performed realistic end‑to‑end tests, including edge‑case and failure‑scenario exercises? Are results documented and reproducible?
-2. **Risk & failure analysis** – Is there a systematic identification of what could go wrong, with quantitative or qualitative impact assessments and mitigation plans?
-3. **Auditability & traceability** – Does the solution provide a tamper‑evident audit trail that records the agent’s decisions, the data used, and any overrides?
-4. **Human‑parity comparison** – Are the agent’s decisions benchmarked against human operator decisions on a representative sample, showing comparable or better outcomes?
-5. **Rollback & monitoring** – Are there clearly defined rollback procedures and continuous monitoring mechanisms to detect deviations after deployment?
-6. **Compliance with anti‑patterns** – Verify that none of the Section 9 anti‑patterns (e.g., “single point of automated authority”, “undocumented exception handling”, “lack of explicit human‑in‑the‑loop fallback”) are present.
+1. **Real‑world testing** – documented end‑to‑end tests, including edge‑cases and failure injection, with reproducible results.  
+2. **Risk & failure analysis** – systematic identification of failure modes, impact assessment, and mitigation strategy.  
+3. **Audit & traceability** – tamper‑evident logs that capture autonomous decisions, inputs, and any overrides.  
+4. **Human‑parity evidence** – quantitative/qualitative comparison showing the autonomous system matches or exceeds qualified human decisions.  
+5. **Anti‑pattern compliance** – no occurrence of Section 9 anti‑patterns (e.g., single automated authority, undocumented exception handling, lack of fallback) unless fully mitigated.
 
-**Decision rules**
+**Decision hierarchy**
 
-- **Sound** – All checklist items are addressed satisfactorily, with evidence that risks are mitigated, testing is thorough, auditability is ensured, and no anti‑patterns are detected.
-- **Needs‑more‑evidence** – The submission addresses many items but has notable gaps (e.g., missing edge‑case tests, incomplete audit trail, or insufficient human‑parity data) that prevent a confident judgment.
-- **Rejected** – One or more critical anti‑patterns are evident, or there is a clear, unmitigated safety or security risk that makes the proposal unacceptable.
+- **Reject** if any checklist item reveals an unmitigated anti‑pattern or a critical safety/security risk.  
+- **Needs‑more‑evidence** if all items are present but one or more have gaps (e.g., missing edge‑case tests, incomplete audit trail, insufficient human‑parity data) that prevent confidence.  
+- **Sound** only when every checklist item is fully satisfied with clear, verifiable evidence and no anti‑patterns are present.
 
-Produce a concise verdict (**sound**, **needs‑more‑evidence**, or **rejected**) followed by a brief justification referencing the checklist items that led to your decision. Do not include any additional formatting beyond the verdict and reasoning.+**Output required** (exactly as the surrounding template expects):
+1. First line: the verdict label – `sound`, `needs-more-evidence`, or `rejected`.  
+2. Subsequent line(s): a brief justification (1–2 sentences) citing the checklist items that drove the decision. Do not add any other text or formatting.
```

### Island 2, cell (0, 5), scalar 0.6039

parent `850d3560a291f194` -> candidate `1fae6bed4a0d1630`

```diff
--- parent 850d3560a291f194
+++ candidate 1fae6bed4a0d1630
@@ -1,29 +1,35 @@
-You are reviewing a Capability Case that seeks to remove per‑action human approval for an industrial operational‑change gateway. Using the definitions in **Section 8 (Strategy C – capability‑based opening)** and the anti‑patterns from **Section 9** of the ITOT‑Boundary‑as‑Architecture whitepaper, assign one of the three verdicts: **sound**, **needs‑more‑evidence**, or **rejected**.
+You are evaluating a Capability Case that proposes removing per‑action human approval for an industrial operational‑change gateway. Using **Section 8 (Strategy C – capability‑based opening)** and the anti‑patterns listed in **Section 9** of the ITOT‑Boundary‑as‑Architecture whitepaper, decide on a single verdict: **sound**, **needs‑more‑evidence**, or **rejected**.
 
-### Evaluation checklist
+### Decision steps
 
-| Requirement | What to look for | Verdict impact |
-|-------------|------------------|----------------|
-| **Real‑world testing** | Controlled field, pilot, or sandbox trials that include failure injection and recovery validation. | Missing → **needs‑more‑evidence** (unless a critical anti‑pattern is present). |
-| **Risk & failure‑mode analysis** | Comprehensive threat model / failure‑mode analysis covering misuse, loss of control, cascade effects, with mitigation plans. | Missing → **needs‑more‑evidence**. |
-| **Auditability & rollback** | Immutable logs, decision traceability, and a documented manual‑override or rollback mechanism. | Missing → **needs‑more‑evidence**. |
-| **Human‑equivalence validation** | Quantitative comparison of automated decisions to a representative human operator set (e.g., accuracy, false‑positive/negative rates, latency) showing equal or better safety/quality. | Missing → **needs‑more‑evidence**. |
-| **Anti‑pattern compliance (Section 9)** | No presence of any critical anti‑patterns: <br>• Black‑box decision making with no observability<br>• No manual override / emergency stop<br>• Unbounded autonomy beyond the defined envelope<br>• Single point of failure without redundancy<br>• Conflict with regulatory or safety standards | **Any** critical anti‑pattern → **rejected**, regardless of other evidence. |
+1. **Check for critical anti‑patterns (Section 9).**  
+   - Black‑box decision making with no observability  
+   - No manual‑override / emergency stop  
+   - Unbounded autonomy beyond the defined envelope  
+   - Single point of failure without redundancy  
+   - Conflict with regulatory or safety standards  
 
-- **Sound**: All four evidence categories are satisfied **and** no critical anti‑patterns are found.  
-- **Needs‑more‑evidence**: One or more evidence categories are missing *or* only minor, non‑critical anti‑pattern signals appear (e.g., vague fallback description).  
-- **Rejected**: At least one critical anti‑pattern from Section 9 is present.
+   **If any of these appear → verdict = `rejected`.** No further evidence matters.
 
-### Output format (do not modify)
+2. **Assess the four evidence categories.**  
+   - **Real‑world testing** – controlled field, pilot, sandbox, or shadow deployment *with* failure injection.  
+   - **Risk & failure‑mode analysis** – complete threat model, misuse scenarios, cascade effects, and mitigation plans.  
+   - **Auditability & rollback** – immutable logs, decision traceability, and a documented manual‑override or rollback path.  
+   - **Human‑equivalence validation** – quantitative comparison to a representative human operator set (accuracy, false‑positive/negative rates, latency) showing equal or better safety/quality.
 
-1. A line beginning with **Verdict:** followed by `sound`, `needs-more-evidence`, or `rejected`.  
-2. One or two short sentences giving the rationale, explicitly citing which checklist items led to the decision.
+   **If all four are present → verdict = `sound`.**  
+   **If one or more are missing (but no critical anti‑pattern) → verdict = `needs-more-evidence`.**
+
+### Output requirements (do not change)
+
+1. A line beginning with **Verdict:** followed by exactly one of `sound`, `needs-more-evidence`, or `rejected`.  
+2. One or two short sentences explaining the decision, explicitly referencing the checklist items that drove the verdict.
 
 **Example**
 
 ```
-Verdict: sound
-The case includes controlled field trials with failure injection, a full threat model, immutable audit logs with a manual override, and quantitative parity with human operators, and it contains no Section 9 anti‑patterns.
+Verdict: needs-more-evidence
+Missing real‑world field trials with failure injection; no critical anti‑patterns detected.
 ```
 
-Apply the checklist to the provided capability case and produce your verdict and reasoning.+Apply the steps above to the supplied capability case and produce the verdict and reasoning exactly as specified.
```

### Island 3, cell (0, 4), scalar 0.8580

parent `0844a88a49262eb1` -> candidate `aefd66e20f4bc98d`

```diff
--- parent 0844a88a49262eb1
+++ candidate aefd66e20f4bc98d
@@ -1,21 +1,19 @@
-You are to judge a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway. Base your assessment on **Section 8 (Strategy C – capability‑based opening)** and the **anti‑patterns in Section 9** of the ITOT‑boundary‑as‑architecture whitepaper.
+You are to evaluate a capability case that proposes eliminating per‑action human approval for an industrial operational‑change gateway. Base your judgment on **Section 8 (Strategy C – capability‑based opening)** and the **anti‑patterns listed in Section 9** of the ITOT‑boundary‑as‑architecture whitepaper.
 
-### Evaluation criteria
-| # | Criterion (what to look for) |
-|---|------------------------------|
-| 1 | **Real‑world testing** – end‑to‑end, high‑fidelity tests covering normal operation and edge cases. |
-| 2 | **Failure‑mode analysis** – documented risks, impact estimates, and concrete mitigation or rollback steps. |
-| 3 | **Audit & traceability** – immutable logs, provenance data, and post‑action explainability. |
-| 4 | **Human‑parity evidence** – quantitative/qualitative comparison showing the automation meets or exceeds qualified human decisions. |
-| 5 | **Anti‑pattern check** – confirm **none** of the Section 9 anti‑patterns (e.g., single‑point automation, no manual override, missing monitoring, unbounded escalation, black‑box behavior). |
+Checklist
+1. Real‑world testing – end‑to‑end, high‑fidelity runs covering normal operation and edge cases.  
+2. Failure‑mode analysis – identified risks, impact estimates, and concrete mitigation or rollback steps.  
+3. Audit & traceability – immutable logs, provenance data, and post‑action explainability.  
+4. Human‑parity evidence – quantitative/qualitative comparison showing the automation meets or exceeds qualified human decisions.  
+5. Anti‑pattern compliance – confirm none of the Section 9 anti‑patterns (e.g., single‑point automation, missing manual override, absent monitoring, unbounded escalation, black‑box behavior) are present.
 
-### Decision logic
-1. **Reject** – If any anti‑pattern (criterion 5) is present **or** there is a total lack of testing, risk analysis, or audit capability.  
-2. **Needs‑more‑evidence** – If all anti‑patterns are absent but one or more of criteria 1‑4 are missing, insufficient, or only partially addressed.  
-3. **Sound** – If every criterion 1‑4 is fully satisfied with concrete evidence and no anti‑pattern is detected.
+Decision
+- **reject** – any anti‑pattern is found **or** testing, risk analysis, or audit capability is completely absent.  
+- **needs‑more‑evidence** – all anti‑patterns are absent but one or more of items 1‑4 are missing, insufficient, or only partially addressed.  
+- **sound** – items 1‑4 are fully satisfied with concrete evidence and no anti‑pattern is detected.
 
-### Output requirements
-1. **First line:** the verdict word exactly as one of `sound`, `needs-more-evidence`, or `rejected`.  
-2. **Second line (and any following lines):** a brief justification (one‑sentence preferred) that cites the relevant criterion numbers (e.g., “Missing end‑to‑end testing (1)” or “Anti‑pattern ‘no manual override’ detected (5)”).  
+Output
+1. First line: exactly `sound`, `needs-more-evidence`, or `rejected`.  
+2. Subsequent line(s): a brief justification (one sentence preferred) that cites the relevant checklist numbers, e.g., “Missing end‑to‑end testing (1)” or “Anti‑pattern ‘no manual override’ detected (5)”.
 
-Do not add headings, tables, or extra structure beyond the two‑line format required by the surrounding template. Follow the wording exactly. +Do not add headings, tables, or any extra structure beyond the two‑line format required by the surrounding template.
```


## Lesson retirement (dry run)

- Lesson 15: **RETIRED** — precision 0.094 vs base 0.482, 10.0 sigma below
- Lesson 17: **kept** — precision 0.983 >= base 0.694
- Lesson 19: **kept** — precision 0.983 >= base 0.881
- Lesson 11: **kept** — precision 0.750 vs base 0.933, only 0.8 sigma below

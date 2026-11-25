# Generation 1 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31.0
- Prefix cache hit rate: 69.0%
- Aggregate throughput: 133.2 tok/s (203642 completion tokens / 1528.4s)

## Archive

- Island 0: coverage 11.1%, QD score 2.151, unique ancestors 3
- Island 1: coverage 8.3%, QD score 1.764, unique ancestors 2
- Island 2: coverage 8.3%, QD score 1.422, unique ancestors 2
- Island 3: coverage 11.1%, QD score 2.298, unique ancestors 3
- Cells newly claimed this generation: 8

## Quality

- Best scalar this generation: 0.7268
- Median scalar of newly-claimed: 0.5382

## Cost

- Budget: {'generation': 1, 'max_generations': 30, 'tokens_used_total': 1208471, 'max_tokens': 3000000, 'elapsed_s_total': 3649.1, 'generation_wall_s': 1528.4}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 0, cell (1, 5), scalar 0.5541

parent `42d3e5d7f65e8488` -> candidate `6f90b7eafeb86540`

```diff
--- parent 42d3e5d7f65e8488
+++ candidate 6f90b7eafeb86540
@@ -1,37 +1,29 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Your task is to read the submitted evidence and assign one of three verdicts:
+You are to judge a capability case that seeks to drop per‑action human approval for an industrial operational‑change gateway. Read the evidence and output **exactly** one of the three verdicts below, followed by a short justification (2‑4 sentences) that cites the most relevant criteria.
 
-* **Sound** – the case provides strong, comprehensive evidence that the risk is well understood, mitigation measures are in place, and the automation can reliably replace human approval.
-* **Needs‑more‑evidence** – the case is missing key information or contains only partial testing; the risk assessment is incomplete, but no fatal flaw is apparent.
-* **Rejected** – the case contains a serious red flag (e.g., unaddressed safety hazard, lack of auditability, violation of an anti‑pattern from Section 9) that makes the proposal unacceptable.
+**Possible verdicts**
+- **Sound** – the submission shows thorough, convincing evidence that the risk is quantified, mitigations exist, and automation can safely replace the human step.
+- **Needs‑more‑evidence** – the case is plausible but lacks critical data or analysis; no fatal flaw is evident.
+- **Rejected** – a serious problem is present (e.g., safety hazard, missing audit trail, violation of a Section 9 anti‑pattern) that makes the proposal unacceptable.
 
-When making your decision, follow these criteria derived from Section 8 (Strategy C) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper:
+**Evaluation checklist (derived from Section 8, Strategy C and Section 9 anti‑patterns)**
+1. **Real‑world testing** – end‑to‑end trials in the target environment, documented results for normal and failure conditions.
+2. **Failure‑mode analysis** – systematic identification of failure modes, with likelihood, impact, and mitigation for each.
+3. **Audit & traceability** – immutable logs that capture decisions, inputs, and outcomes, allowing post‑hoc reconstruction.
+4. **Human‑baseline comparison** – quantitative or qualitative evidence that the automated action meets or exceeds expert human performance on safety‑critical metrics.
+5. **Anti‑pattern compliance** – confirms none of the following are present:
+   - No‑fallback / safe‑state,
+   - Over‑automation removing required discretionary judgment,
+   - Opaque reasoning or hidden data sources,
+   - Unassigned accountability for adverse outcomes.
 
-1. **Testing & Validation**  
-   - Has the team performed realistic, end‑to‑end testing of the automation in the target environment?  
-   - Are test results documented, reproducible, and cover both nominal and failure scenarios?
+**Decision rule**
+- Choose **Sound** only if all checklist items are satisfied and no anti‑patterns appear.
+- Choose **Needs‑more‑evidence** if the submission is generally solid but one or more items are insufficiently addressed, without a show‑stopper.
+- Choose **Rejected** if any anti‑pattern or critical safety issue is found.
 
-2. **Risk & Failure Analysis**  
-   - Is there a systematic identification of possible failure modes?  
-   - Are consequences, likelihood, and mitigations for each failure mode described?
-
-3. **Auditability & Traceability**  
-   - Does the proposal include an immutable audit trail that records the agent’s decisions, inputs, and outcomes?  
-   - Can a reviewer reconstruct the decision path after the fact?
-
-4. **Human Decision Comparison**  
-   - Is there a quantitative or qualitative comparison between the agent’s actions and expert human decisions?  
-   - Does the evidence show equal or better performance on safety‑critical metrics?
-
-5. **Anti‑Pattern Checks (Section 9)**  
-   - **No‑fallback**: Is there a clear, automated fallback or safe‑state if the agent fails?  
-   - **Over‑automation**: Does the proposal avoid removing human judgment from contexts that require discretionary assessment?  
-   - **Opaque reasoning**: Are the agent’s decision logic and data sources transparent and explainable?  
-   - **Missing accountability**: Is responsibility for adverse outcomes clearly assigned?
-
-Assign the verdict that best matches the overall strength of the evidence. After the verdict, provide a concise rationale (2–4 sentences) that references the most salient points from the criteria above.
-
-**Output format (do not alter the surrounding template):**  
+**Output format (do not modify):**
 ```
 Verdict: <Sound|Needs-more-evidence|Rejected>
 Reasoning: <brief explanation>
-```+```
+The reasoning must reference the checklist items that drove your decision.
```

### Island 0, cell (1, 5), scalar 0.5554

parent `42d3e5d7f65e8488` -> candidate `90e3dfa266a11146`

```diff
--- parent 42d3e5d7f65e8488
+++ candidate 90e3dfa266a11146
@@ -1,37 +1,28 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Your task is to read the submitted evidence and assign one of three verdicts:
+You are reviewing a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway. Read the entire submission and choose **exactly one** verdict:
 
-* **Sound** – the case provides strong, comprehensive evidence that the risk is well understood, mitigation measures are in place, and the automation can reliably replace human approval.
-* **Needs‑more‑evidence** – the case is missing key information or contains only partial testing; the risk assessment is incomplete, but no fatal flaw is apparent.
-* **Rejected** – the case contains a serious red flag (e.g., unaddressed safety hazard, lack of auditability, violation of an anti‑pattern from Section 9) that makes the proposal unacceptable.
+* **Sound** – the evidence convincingly shows that the automation can safely replace the human gate‑keeper.
+* **Needs‑more‑evidence** – the case is plausible but missing critical data or analysis; no fatal flaw is evident.
+* **Rejected** – a serious problem is present (e.g., safety hazard, missing auditability, violation of a Section 9 anti‑pattern) that makes the proposal unacceptable.
 
-When making your decision, follow these criteria derived from Section 8 (Strategy C) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper:
+**Evaluation checklist**
 
-1. **Testing & Validation**  
-   - Has the team performed realistic, end‑to‑end testing of the automation in the target environment?  
-   - Are test results documented, reproducible, and cover both nominal and failure scenarios?
+1. **Real‑world testing** – Are end‑to‑end trials performed in the target environment, with documented results for normal and failure conditions?
+2. **Failure‑mode analysis** – Does the submission list possible failures, their likelihood, impact, and concrete mitigations?
+3. **Audit trail** – Is there an immutable log that records decision inputs, logic, and outcomes, allowing post‑hoc reconstruction?
+4. **Human‑baseline comparison** – Is there quantitative or qualitative evidence that the automated decisions match or exceed expert human performance on safety‑critical metrics?
+5. **Section 9 anti‑patterns** – Verify that none of the following are present:
+   - No‑fallback / missing safe‑state
+   - Over‑automation where discretionary judgment is required
+   - Opaque or undocumented reasoning
+   - Unassigned accountability
 
-2. **Risk & Failure Analysis**  
-   - Is there a systematic identification of possible failure modes?  
-   - Are consequences, likelihood, and mitigations for each failure mode described?
+**Decision rule**
+- If all checklist items are satisfied and no anti‑pattern appears → **Sound**.  
+- If most items are addressed but one or more are incomplete, without a red‑flag → **Needs‑more‑evidence**.  
+- If any anti‑pattern or critical safety issue is found → **Rejected**.
 
-3. **Auditability & Traceability**  
-   - Does the proposal include an immutable audit trail that records the agent’s decisions, inputs, and outcomes?  
-   - Can a reviewer reconstruct the decision path after the fact?
-
-4. **Human Decision Comparison**  
-   - Is there a quantitative or qualitative comparison between the agent’s actions and expert human decisions?  
-   - Does the evidence show equal or better performance on safety‑critical metrics?
-
-5. **Anti‑Pattern Checks (Section 9)**  
-   - **No‑fallback**: Is there a clear, automated fallback or safe‑state if the agent fails?  
-   - **Over‑automation**: Does the proposal avoid removing human judgment from contexts that require discretionary assessment?  
-   - **Opaque reasoning**: Are the agent’s decision logic and data sources transparent and explainable?  
-   - **Missing accountability**: Is responsibility for adverse outcomes clearly assigned?
-
-Assign the verdict that best matches the overall strength of the evidence. After the verdict, provide a concise rationale (2–4 sentences) that references the most salient points from the criteria above.
-
-**Output format (do not alter the surrounding template):**  
+**Output (do not modify the surrounding template)**
 ```
 Verdict: <Sound|Needs-more-evidence|Rejected>
-Reasoning: <brief explanation>
+Reasoning: <brief explanation referencing the most relevant checklist points>
 ```
```

### Island 0, cell (1, 5), scalar 0.6529

parent `42d3e5d7f65e8488` -> candidate `9757093578374606`

```diff
--- parent 42d3e5d7f65e8488
+++ candidate 9757093578374606
@@ -1,37 +1,29 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Your task is to read the submitted evidence and assign one of three verdicts:
+You are reviewing a capability case that asks to waive per‑action human approval for an industrial operational‑change gateway action. Read the submission and assign **exactly one** verdict from the three options below:
 
-* **Sound** – the case provides strong, comprehensive evidence that the risk is well understood, mitigation measures are in place, and the automation can reliably replace human approval.
-* **Needs‑more‑evidence** – the case is missing key information or contains only partial testing; the risk assessment is incomplete, but no fatal flaw is apparent.
-* **Rejected** – the case contains a serious red flag (e.g., unaddressed safety hazard, lack of auditability, violation of an anti‑pattern from Section 9) that makes the proposal unacceptable.
+* **Sound** – evidence is complete, risks are clearly understood, mitigations are proven, and no anti‑pattern from Section 9 is present.  
+* **Needs‑more‑evidence** – the proposal is plausible but lacks critical data or leaves a key safety question unanswered; no fatal flaw is evident.  
+* **Rejected** – the submission contains a serious problem (e.g., unresolved safety hazard, missing audit trail, violation of a Section 9 anti‑pattern) that makes the case unacceptable.
 
-When making your decision, follow these criteria derived from Section 8 (Strategy C) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper:
+### Decision checklist (derived from Section 8, Strategy C and Section 9)
 
-1. **Testing & Validation**  
-   - Has the team performed realistic, end‑to‑end testing of the automation in the target environment?  
-   - Are test results documented, reproducible, and cover both nominal and failure scenarios?
+1. **End‑to‑end testing** – Are realistic tests performed in the target environment, with documented, reproducible results for both normal and failure conditions?  
+2. **Failure‑mode analysis** – Does the case list possible failure modes, assess their likelihood and impact, and describe concrete mitigations?  
+3. **Audit & traceability** – Is there an immutable log that captures every automated decision, its inputs, and outcomes, allowing post‑hoc reconstruction?  
+4. **Human‑baseline comparison** – Is there quantitative or qualitative evidence that the automated action meets or exceeds the performance of a qualified human operator on safety‑critical metrics?  
+5. **Anti‑pattern compliance (Section 9)** – Verify that none of the following appear:  
+   * **No‑fallback** – lack of an automated safe‑state or fallback.  
+   * **Over‑automation** – removal of necessary discretionary human judgment.  
+   * **Opaque reasoning** – undisclosed decision logic or data sources.  
+   * **Missing accountability** – unclear responsibility for adverse outcomes.
 
-2. **Risk & Failure Analysis**  
-   - Is there a systematic identification of possible failure modes?  
-   - Are consequences, likelihood, and mitigations for each failure mode described?
+### Verdict selection rules
+- Choose **Sound** only if all checklist items are satisfied and no anti‑pattern is found.  
+- Choose **Needs‑more‑evidence** if one or more items are insufficiently addressed but no red‑flag exists.  
+- Choose **Rejected** if any item reveals a critical flaw or an anti‑pattern violation.
 
-3. **Auditability & Traceability**  
-   - Does the proposal include an immutable audit trail that records the agent’s decisions, inputs, and outcomes?  
-   - Can a reviewer reconstruct the decision path after the fact?
-
-4. **Human Decision Comparison**  
-   - Is there a quantitative or qualitative comparison between the agent’s actions and expert human decisions?  
-   - Does the evidence show equal or better performance on safety‑critical metrics?
-
-5. **Anti‑Pattern Checks (Section 9)**  
-   - **No‑fallback**: Is there a clear, automated fallback or safe‑state if the agent fails?  
-   - **Over‑automation**: Does the proposal avoid removing human judgment from contexts that require discretionary assessment?  
-   - **Opaque reasoning**: Are the agent’s decision logic and data sources transparent and explainable?  
-   - **Missing accountability**: Is responsibility for adverse outcomes clearly assigned?
-
-Assign the verdict that best matches the overall strength of the evidence. After the verdict, provide a concise rationale (2–4 sentences) that references the most salient points from the criteria above.
-
-**Output format (do not alter the surrounding template):**  
+### Output (do not modify the surrounding template)
 ```
 Verdict: <Sound|Needs-more-evidence|Rejected>
-Reasoning: <brief explanation>
-```+Reasoning: <2–4 sentence summary referencing the most relevant checklist items>
+```
+Only the two lines above should be produced. No extra headings, lists, or formatting.
```

### Island 1, cell (0, 5), scalar 0.5109

parent `4867f315de1ca506` -> candidate `7df1e9e36335dd4b`

```diff
--- parent 4867f315de1ca506
+++ candidate 7df1e9e36335dd4b
@@ -1,19 +1,25 @@
-You are evaluating a capability case that proposes to relax or eliminate per‑action human approval for an industrial operational‑change gateway action. Your task is to read the submitted material and assign one of the three judgment labels defined in the whitepaper:
+You are to evaluate a capability case that proposes to relax or eliminate per‑action human approval for an industrial operational‑change gateway action. Using the criteria from Section 8 (Strategy C) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper, decide on one of the three verdicts:
 
-* **sound** – the case provides sufficient, high‑quality evidence that the risk is understood and mitigated, satisfying the criteria in Section 8 (Strategy C) and showing no violations of the anti‑patterns listed in Section 9.
-* **needs‑more‑evidence** – the case is plausible but lacks key evidence or contains gaps that prevent a confident conclusion; further testing, analysis, or documentation is required.
-* **rejected** – the case exhibits a serious deficiency (e.g., unaddressed safety hazard, missing audit capability, clear anti‑pattern) that makes the proposal unacceptable under the current policy.
+* **sound** – The submission provides complete, high‑quality evidence that all risks are understood and mitigated, includes thorough real‑world testing, an immutable audit trail, and shows no anti‑patterns (or mitigates them convincingly).
+* **needs‑more‑evidence** – The case is plausible but at least one of the required elements is missing or insufficient; no disqualifying anti‑pattern is present.
+* **rejected** – Any anti‑pattern from Section 9 appears without a robust mitigation, or a serious safety/security deficiency is evident, regardless of other evidence.
 
-When making your decision, consider each of the following elements and indicate whether the submission meets, partially meets, or fails them:
+Assess the submission against the following checklist (record “meets”, “partially meets”, or “fails” for each, but you need not list them in the output):
 
-1. **Real‑world testing** – Has the team conducted realistic, end‑to‑end tests (including failure injection) that demonstrate the system behaves safely without human approval?
-2. **Risk & failure analysis** – Is there a thorough identification of potential failure modes, their likelihood, and mitigations? Are high‑impact or high‑probability risks adequately addressed?
-3. **Audit & traceability** – Does the proposal include an immutable audit trail (e.g., logs, provenance data) that records the agent’s decisions and can be reviewed after the fact?
-4. **Human‑decision comparison** – Are there quantitative or qualitative comparisons showing that the autonomous decisions align with, or improve upon, what a qualified human would decide in the same scenarios?
-5. **Compliance with anti‑patterns (Section 9)** – Check for any of the listed anti‑patterns (e.g., “single point of failure”, “unbounded escalation”, “unchecked privilege elevation”). Presence of any such anti‑pattern should lead to a **rejected** verdict unless a robust mitigation is demonstrated.
+1. **Real‑world testing** – End‑to‑end tests with realistic workloads and failure injection are documented and reproducible.  
+2. **Risk & failure analysis** – All plausible failure modes are identified, their likelihood and impact are evaluated, and mitigations are described.  
+3. **Audit & traceability** – An immutable, tamper‑evident audit trail records the autonomous decisions, inputs, and any overrides.  
+4. **Human‑decision comparison** – Quantitative or qualitative evidence shows the autonomous decisions are at least as safe/effective as those of a qualified human operator.  
+5. **Anti‑pattern compliance (Section 9)** – Verify that none of the listed anti‑patterns (e.g., single point of automated authority, unbounded escalation, unchecked privilege elevation, lack of fallback) are present, or that any that appear are mitigated with explicit controls.
+
+**Decision rules**
+
+* If any anti‑pattern fails the mitigation check → **rejected**.  
+* Else if any checklist item **fails** or is only **partially met** in a way that leaves a critical gap → **needs‑more‑evidence**.  
+* Else → **sound**.
 
 **Output format** (exactly as required by the surrounding template):
-- First line: the chosen verdict label (`sound`, `needs-more-evidence`, or `rejected`).
-- Subsequent lines: a concise justification (1–3 sentences) referencing the most critical points from the list above that led to your decision.
+1. First line: the verdict label (`sound`, `needs-more-evidence`, or `rejected`).  
+2. Subsequent line(s): a concise justification (1–2 sentences) that references the most decisive checklist items influencing your verdict.
 
-Proceed with the assessment now.+Do not add any other text or formatting.
```

### Island 2, cell (1, 5), scalar 0.5144

parent `a7258b3565b39816` -> candidate `f9ff3498f559abbb`

```diff
--- parent a7258b3565b39816
+++ candidate f9ff3498f559abbb
@@ -1,38 +1,24 @@
-You are evaluating a Capability Case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Your task is to classify the case as **sound**, **needs‑more‑evidence**, or **rejected** according to the criteria in **Section 8 (Strategy C – capability‑based opening)** and the anti‑patterns listed in **Section 9** of the ITOT‑Boundary‑as‑Architecture whitepaper.
+You are reviewing a Capability Case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Classify the case as **sound**, **needs‑more‑evidence**, or **rejected** based on the criteria below.
 
-**Decision criteria**
+**Required evidence for a *sound* verdict (all must be present):**
+1. **Real‑world testing** – controlled field, sandbox, or pilot trials that include failure injection and recovery.
+2. **Risk & failure‑mode analysis** – a complete threat‑model covering misuse, loss of control, cascade effects, and mitigation plans.
+3. **Auditability** – immutable logs, traceability of each automated decision, and a defined rollback/manual‑override procedure.
+4. **Human‑benchmark comparison** – quantitative results showing the automated system matches or exceeds representative human operators on safety/quality metrics.
+5. **No critical anti‑patterns** – the case must not exhibit any of the Section 9 red‑flags listed below.
 
-1. **Sound** – The submission satisfies all of the following:
-   - **Real‑world testing**: Demonstrates controlled field or sandbox trials that include failure injection and recovery.
-   - **Risk analysis**: Provides a thorough Threat‑Model/Failure‑Mode analysis covering misuse, loss of control, and cascade effects.
-   - **Auditability**: Supplies immutable logs, traceability of agent decisions, and a clear rollback or manual‑override mechanism.
-   - **Human‑equivalence validation**: Compares automated decisions against a representative human operator set and shows equal or better safety/quality outcomes.
-   - **No Section 9 anti‑patterns**: Absence of “black‑box only”, “no fallback”, “unbounded autonomy”, or “single point of failure” issues.
+***Needs‑more‑evidence* verdict** – the submission lacks one or more of the items above but does **not** contain a critical anti‑pattern. Typical gaps include limited testing, incomplete risk analysis, missing audit trail, or absent human‑benchmark data.
 
-2. **Needs‑more‑evidence** – The case is missing one or more of the items above but does not contain a critical anti‑pattern. Typical gaps:
-   - Limited or no testing, or testing only in simulation.
-   - Incomplete risk assessment or missing mitigation strategies.
-   - Partial audit trail or unclear log retention.
-   - No quantitative comparison to human performance.
-   - Minor anti‑pattern signals that could be remedied (e.g., unclear fallback procedure).
+***Rejected* verdict** – the submission contains any **critical anti‑pattern** (or regulatory conflict) from Section 9, such as:
+- Black‑box decision making with no observability.
+- No manual override or emergency stop.
+- Unbounded autonomy beyond the defined operational envelope.
+- Single point of failure without redundancy.
+- Any other listed anti‑pattern that compromises safety, security, or compliance.
 
-3. **Rejected** – The submission exhibits any **critical anti‑pattern** from Section 9, such as:
-   - **Black‑box decision making** with no observability.
-   - **No manual override** or emergency stop.
-   - **Unbounded autonomy** beyond the defined operational envelope.
-   - **Single point of failure** without redundancy.
-   - Evidence of **conflict with regulatory or safety standards**.
-
-**Output format**
-
-- State the verdict clearly on a line beginning with **Verdict:** followed by one of `sound`, `needs-more-evidence`, or `rejected`.
-- On subsequent lines, provide a concise rationale (1‑3 sentences) that references the specific criteria or anti‑patterns that led to your decision.
-
-Example:
-
+**Output format (do not modify):**
 ```
-Verdict: sound
-The submission includes full field trials with failure injection, a documented threat model, immutable audit logs, and quantitative parity with human operators, and it contains no Section 9 anti‑patterns.
+Verdict: <sound|needs-more-evidence|rejected>
+Reasoning: <1‑3 sentences citing the specific criteria or anti‑pattern that led to your decision>
 ```
-
-Proceed to read the provided capability case and apply the checklist above to produce your verdict and reasoning.+Provide the verdict on the first line exactly as shown, followed by a concise reasoning line. Apply the checklist rigorously to the supplied capability case. 
```

### Island 2, cell (0, 5), scalar 0.4483

parent `a7258b3565b39816` -> candidate `4a4fc1d90d0ac1a7`

```diff
--- parent a7258b3565b39816
+++ candidate 4a4fc1d90d0ac1a7
@@ -1,38 +1,29 @@
-You are evaluating a Capability Case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Your task is to classify the case as **sound**, **needs‑more‑evidence**, or **rejected** according to the criteria in **Section 8 (Strategy C – capability‑based opening)** and the anti‑patterns listed in **Section 9** of the ITOT‑Boundary‑as‑Architecture whitepaper.
+You are to assess a Capability Case that seeks to remove per‑action human approval for an industrial operational‑change gateway. Choose a single verdict – **sound**, **needs‑more‑evidence**, or **rejected** – by applying the criteria from **Section 8 (Strategy C – capability‑based opening)** and the anti‑patterns listed in **Section 9** of the ITOT‑Boundary‑as‑Architecture whitepaper.
 
-**Decision criteria**
+### Decision checklist
 
-1. **Sound** – The submission satisfies all of the following:
-   - **Real‑world testing**: Demonstrates controlled field or sandbox trials that include failure injection and recovery.
-   - **Risk analysis**: Provides a thorough Threat‑Model/Failure‑Mode analysis covering misuse, loss of control, and cascade effects.
-   - **Auditability**: Supplies immutable logs, traceability of agent decisions, and a clear rollback or manual‑override mechanism.
-   - **Human‑equivalence validation**: Compares automated decisions against a representative human operator set and shows equal or better safety/quality outcomes.
-   - **No Section 9 anti‑patterns**: Absence of “black‑box only”, “no fallback”, “unbounded autonomy”, or “single point of failure” issues.
+| # | Requirement | Must‑have for **sound** | Acceptable gap for **needs‑more‑evidence** | Disqualifies (→ **rejected**) |
+|---|-------------|--------------------------|--------------------------------------------|--------------------------------|
+| 1 | **Real‑world testing** – controlled field, sandbox, or pilot trials with failure injection | Full trials covering normal and edge cases | Only simulation or limited lab tests | – |
+| 2 | **Risk & failure‑mode analysis** – threat model, misuse, cascade effects, mitigation plans | Comprehensive analysis with mitigations | Partial or missing mitigation details | – |
+| 3 | **Auditability** – immutable logs, decision traceability, rollback or manual‑override path | Complete end‑to‑end logging and verified override | Logs exist but are incomplete or rollback unclear | – |
+| 4 | **Human‑benchmark validation** – quantitative comparison to a representative human operator set | Demonstrated equal or better safety/quality metrics | No quantitative comparison or only qualitative claim | – |
+| 5 | **Anti‑pattern compliance (Section 9)** – no occurrence of black‑box only, no fallback, unbounded autonomy, single point of failure, regulatory conflict, etc. | **None** detected | Minor, non‑critical wording issues | Any **critical** anti‑pattern present |
 
-2. **Needs‑more‑evidence** – The case is missing one or more of the items above but does not contain a critical anti‑pattern. Typical gaps:
-   - Limited or no testing, or testing only in simulation.
-   - Incomplete risk assessment or missing mitigation strategies.
-   - Partial audit trail or unclear log retention.
-   - No quantitative comparison to human performance.
-   - Minor anti‑pattern signals that could be remedied (e.g., unclear fallback procedure).
+- **Sound**: All rows satisfied (no “✓” missing, no red‑flag anti‑pattern).  
+- **Needs‑more‑evidence**: One or more rows missing or incomplete **and** no critical anti‑pattern is found.  
+- **Rejected**: Any critical anti‑pattern from row 5 is present, regardless of other items.
 
-3. **Rejected** – The submission exhibits any **critical anti‑pattern** from Section 9, such as:
-   - **Black‑box decision making** with no observability.
-   - **No manual override** or emergency stop.
-   - **Unbounded autonomy** beyond the defined operational envelope.
-   - **Single point of failure** without redundancy.
-   - Evidence of **conflict with regulatory or safety standards**.
+### Output specification (exactly as required)
 
-**Output format**
+1. **Verdict:** `<verdict>` – one word from the set `sound`, `needs-more-evidence`, `rejected`.  
+2. **Reasoning:** 1‑3 sentences that cite the specific checklist items that drove the verdict (e.g., “Missing field trials” or “Contains unbounded autonomy”).
 
-- State the verdict clearly on a line beginning with **Verdict:** followed by one of `sound`, `needs-more-evidence`, or `rejected`.
-- On subsequent lines, provide a concise rationale (1‑3 sentences) that references the specific criteria or anti‑patterns that led to your decision.
-
-Example:
+**Example**
 
 ```
-Verdict: sound
-The submission includes full field trials with failure injection, a documented threat model, immutable audit logs, and quantitative parity with human operators, and it contains no Section 9 anti‑patterns.
+Verdict: needs-more-evidence
+Reasoning: The case provides audit logs and a threat model but lacks real‑world testing with failure injection; no critical anti‑patterns were found.
 ```
 
-Proceed to read the provided capability case and apply the checklist above to produce your verdict and reasoning.+Read the supplied capability case, run through the checklist, and output the verdict and reasoning exactly as described.
```

### Island 2, cell (1, 5), scalar 0.5223

parent `a7258b3565b39816` -> candidate `850d3560a291f194`

```diff
--- parent a7258b3565b39816
+++ candidate 850d3560a291f194
@@ -1,38 +1,29 @@
-You are evaluating a Capability Case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Your task is to classify the case as **sound**, **needs‑more‑evidence**, or **rejected** according to the criteria in **Section 8 (Strategy C – capability‑based opening)** and the anti‑patterns listed in **Section 9** of the ITOT‑Boundary‑as‑Architecture whitepaper.
+You are reviewing a Capability Case that seeks to remove per‑action human approval for an industrial operational‑change gateway. Using the definitions in **Section 8 (Strategy C – capability‑based opening)** and the anti‑patterns from **Section 9** of the ITOT‑Boundary‑as‑Architecture whitepaper, assign one of the three verdicts: **sound**, **needs‑more‑evidence**, or **rejected**.
 
-**Decision criteria**
+### Evaluation checklist
 
-1. **Sound** – The submission satisfies all of the following:
-   - **Real‑world testing**: Demonstrates controlled field or sandbox trials that include failure injection and recovery.
-   - **Risk analysis**: Provides a thorough Threat‑Model/Failure‑Mode analysis covering misuse, loss of control, and cascade effects.
-   - **Auditability**: Supplies immutable logs, traceability of agent decisions, and a clear rollback or manual‑override mechanism.
-   - **Human‑equivalence validation**: Compares automated decisions against a representative human operator set and shows equal or better safety/quality outcomes.
-   - **No Section 9 anti‑patterns**: Absence of “black‑box only”, “no fallback”, “unbounded autonomy”, or “single point of failure” issues.
+| Requirement | What to look for | Verdict impact |
+|-------------|------------------|----------------|
+| **Real‑world testing** | Controlled field, pilot, or sandbox trials that include failure injection and recovery validation. | Missing → **needs‑more‑evidence** (unless a critical anti‑pattern is present). |
+| **Risk & failure‑mode analysis** | Comprehensive threat model / failure‑mode analysis covering misuse, loss of control, cascade effects, with mitigation plans. | Missing → **needs‑more‑evidence**. |
+| **Auditability & rollback** | Immutable logs, decision traceability, and a documented manual‑override or rollback mechanism. | Missing → **needs‑more‑evidence**. |
+| **Human‑equivalence validation** | Quantitative comparison of automated decisions to a representative human operator set (e.g., accuracy, false‑positive/negative rates, latency) showing equal or better safety/quality. | Missing → **needs‑more‑evidence**. |
+| **Anti‑pattern compliance (Section 9)** | No presence of any critical anti‑patterns: <br>• Black‑box decision making with no observability<br>• No manual override / emergency stop<br>• Unbounded autonomy beyond the defined envelope<br>• Single point of failure without redundancy<br>• Conflict with regulatory or safety standards | **Any** critical anti‑pattern → **rejected**, regardless of other evidence. |
 
-2. **Needs‑more‑evidence** – The case is missing one or more of the items above but does not contain a critical anti‑pattern. Typical gaps:
-   - Limited or no testing, or testing only in simulation.
-   - Incomplete risk assessment or missing mitigation strategies.
-   - Partial audit trail or unclear log retention.
-   - No quantitative comparison to human performance.
-   - Minor anti‑pattern signals that could be remedied (e.g., unclear fallback procedure).
+- **Sound**: All four evidence categories are satisfied **and** no critical anti‑patterns are found.  
+- **Needs‑more‑evidence**: One or more evidence categories are missing *or* only minor, non‑critical anti‑pattern signals appear (e.g., vague fallback description).  
+- **Rejected**: At least one critical anti‑pattern from Section 9 is present.
 
-3. **Rejected** – The submission exhibits any **critical anti‑pattern** from Section 9, such as:
-   - **Black‑box decision making** with no observability.
-   - **No manual override** or emergency stop.
-   - **Unbounded autonomy** beyond the defined operational envelope.
-   - **Single point of failure** without redundancy.
-   - Evidence of **conflict with regulatory or safety standards**.
+### Output format (do not modify)
 
-**Output format**
+1. A line beginning with **Verdict:** followed by `sound`, `needs-more-evidence`, or `rejected`.  
+2. One or two short sentences giving the rationale, explicitly citing which checklist items led to the decision.
 
-- State the verdict clearly on a line beginning with **Verdict:** followed by one of `sound`, `needs-more-evidence`, or `rejected`.
-- On subsequent lines, provide a concise rationale (1‑3 sentences) that references the specific criteria or anti‑patterns that led to your decision.
-
-Example:
+**Example**
 
 ```
 Verdict: sound
-The submission includes full field trials with failure injection, a documented threat model, immutable audit logs, and quantitative parity with human operators, and it contains no Section 9 anti‑patterns.
+The case includes controlled field trials with failure injection, a full threat model, immutable audit logs with a manual override, and quantitative parity with human operators, and it contains no Section 9 anti‑patterns.
 ```
 
-Proceed to read the provided capability case and apply the checklist above to produce your verdict and reasoning.+Apply the checklist to the provided capability case and produce your verdict and reasoning.
```

### Island 3, cell (0, 5), scalar 0.7268

parent `519963da19cb60df` -> candidate `0844a88a49262eb1`

```diff
--- parent 519963da19cb60df
+++ candidate 0844a88a49262eb1
@@ -1,16 +1,21 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Using the criteria from Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper, decide whether the case should be judged **sound**, **needs‑more‑evidence**, or **rejected**.
+You are to judge a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway. Base your assessment on **Section 8 (Strategy C – capability‑based opening)** and the **anti‑patterns in Section 9** of the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Evaluation checklist**
-1. **Empirical testing** – Has the team performed realistic, end‑to‑end tests of the automated decision‑making? Include test scope, environment fidelity, and coverage of edge cases.
-2. **Failure‑mode analysis** – Is there a documented assessment of what could go wrong (risk analysis, mitigation strategies, fallback paths)?
-3. **Auditability & traceability** – Does the proposal provide an immutable audit trail (logs, provenance, explainability) that can be reviewed after each automated action?
-4. **Human‑equivalence comparison** – Are the agent’s decisions benchmarked against human decisions (e.g., accuracy, false‑positive/negative rates) and shown to meet or exceed required performance?
-5. **Anti‑pattern compliance** – Verify that none of the Section 9 anti‑patterns are present (e.g., “over‑reliance on single‑point automation”, “absence of manual override”, “insufficient monitoring”, “unbounded escalation”, etc.). If any anti‑pattern applies, treat it as a red flag.
+### Evaluation criteria
+| # | Criterion (what to look for) |
+|---|------------------------------|
+| 1 | **Real‑world testing** – end‑to‑end, high‑fidelity tests covering normal operation and edge cases. |
+| 2 | **Failure‑mode analysis** – documented risks, impact estimates, and concrete mitigation or rollback steps. |
+| 3 | **Audit & traceability** – immutable logs, provenance data, and post‑action explainability. |
+| 4 | **Human‑parity evidence** – quantitative/qualitative comparison showing the automation meets or exceeds qualified human decisions. |
+| 5 | **Anti‑pattern check** – confirm **none** of the Section 9 anti‑patterns (e.g., single‑point automation, no manual override, missing monitoring, unbounded escalation, black‑box behavior). |
 
-**Decision rules**
-- **sound** – All checklist items are satisfied, evidence is concrete and comprehensive, and no anti‑patterns are detected.
-- **needs‑more‑evidence** – Most items are addressed but one or more critical pieces (e.g., testing depth, risk analysis, audit trail) are missing or insufficient.
-- **rejected** – A serious red flag is present (e.g., a Section 9 anti‑pattern, lack of any testing, no audit capability, or evidence of unsafe failure handling).
+### Decision logic
+1. **Reject** – If any anti‑pattern (criterion 5) is present **or** there is a total lack of testing, risk analysis, or audit capability.  
+2. **Needs‑more‑evidence** – If all anti‑patterns are absent but one or more of criteria 1‑4 are missing, insufficient, or only partially addressed.  
+3. **Sound** – If every criterion 1‑4 is fully satisfied with concrete evidence and no anti‑pattern is detected.
 
-**Output**
-Provide **exactly** the verdict label (`sound`, `needs-more-evidence`, or `rejected`) followed by a concise rationale that references the checklist items above. Follow the surrounding template’s output format; do not add extra headings or structures.+### Output requirements
+1. **First line:** the verdict word exactly as one of `sound`, `needs-more-evidence`, or `rejected`.  
+2. **Second line (and any following lines):** a brief justification (one‑sentence preferred) that cites the relevant criterion numbers (e.g., “Missing end‑to‑end testing (1)” or “Anti‑pattern ‘no manual override’ detected (5)”).  
+
+Do not add headings, tables, or extra structure beyond the two‑line format required by the surrounding template. Follow the wording exactly. 
```


## Lesson retirement (dry run)

- Lesson 15: **RETIRED** — precision 0.094 vs base 0.482, 10.0 sigma below
- Lesson 17: **kept** — precision 0.983 >= base 0.694
- Lesson 19: **kept** — precision 0.983 >= base 0.881
- Lesson 11: **kept** — precision 0.750 vs base 0.933, only 0.8 sigma below

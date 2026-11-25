# Generation 4 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31.0
- Prefix cache hit rate: 69.8%
- Aggregate throughput: 92.3 tok/s (219335 completion tokens / 2376.2s)

## Archive

- Island 0: coverage 27.8%, QD score 5.933, unique ancestors 5
- Island 1: coverage 13.9%, QD score 3.021, unique ancestors 3
- Island 2: coverage 25.0%, QD score 3.786, unique ancestors 3
- Island 3: coverage 22.2%, QD score 5.557, unique ancestors 4
- Cells newly claimed this generation: 6

## Quality

- Best scalar this generation: 0.7554
- Median scalar of newly-claimed: 0.5815

## Cost

- Budget: {'generation': 4, 'max_generations': 30, 'tokens_used_total': 3095075, 'max_tokens': 3000000, 'elapsed_s_total': 11899.6, 'generation_wall_s': 2376.2}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 0, cell (0, 4), scalar 0.5536

parent `8911d13f4535b97a` -> candidate `ef41f0b2c2315c8d`

```diff
--- parent 8911d13f4535b97a
+++ candidate ef41f0b2c2315c8d
@@ -1,21 +1,21 @@
-You are evaluating a capability case that proposes to relax the per‑action human‑approval step for an industrial operational‑change action. Your task is to judge the case as **sound**, **needs‑more‑evidence**, or **rejected** according to Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are reviewing a capability case that seeks to remove or relax the per‑action human‑approval requirement for an industrial operational‑change gateway. Base your judgment on Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
 **Evaluation criteria**
 
-1. **Real‑world testing** – Has the team performed functional, integration, and failure‑injection testing that reflects the operational environment?
-2. **Risk & failure analysis** – Are potential failure modes identified, and are mitigations or fallback controls described?
-3. **Auditability & traceability** – Is there a verifiable log or record that can reconstruct the agent’s decision‑making after the fact?
-4. **Human‑parity comparison** – Does the submission include quantitative or qualitative comparison of the agent’s decisions against human operators, showing equal or better safety/performance?
-5. **Compliance & safety safeguards** – Are regulatory constraints respected and are safety‑critical safeguards (e.g., emergency stop, manual override) retained?
+1. **Real‑world testing** – Does the submission include functional, integration and failure‑injection tests that mimic production conditions?  
+2. **Risk & mitigation analysis** – Are failure modes identified, their likelihood/severity quantified, and concrete mitigations or fallback controls described?  
+3. **Auditability & traceability** – Is there an immutable log or equivalent that allows full reconstruction of the automated decision after the fact?  
+4. **Human‑parity evidence** – Is there quantitative or qualitative evidence that the automated decision is at least as safe and reliable as a qualified human operator?  
+5. **Anti‑pattern compliance** – Does the proposal avoid all anti‑patterns from Section 9 (e.g., single point of failure, unchecked escalation, opaque logic, unbounded scope, missing safe‑stop)?
 
-**Decision rules**
+**Decision hierarchy**
 
-- **Sound** – All five criteria are addressed satisfactorily; evidence is robust, and no serious red‑flags are present.
-- **Needs‑more‑evidence** – One or more criteria are only partially addressed or missing, but no catastrophic issue is identified.
-- **Rejected** – Any criterion reveals a fundamental flaw (e.g., no audit trail, unmitigated safety hazard, violation of anti‑patterns) that makes the proposal unsafe or non‑compliant.
+- **Rejected** – If any anti‑pattern is present (criterion 5) or a fundamental flaw makes the proposal unsafe or non‑compliant.  
+- **Sound** – If criteria 1‑4 are all fully satisfied with robust evidence and no serious issues are found.  
+- **Needs‑more‑evidence** – If one or more of criteria 1‑4 are only partially addressed or missing, but no outright anti‑pattern is detected.
 
-**Output**
+**Output format (exactly two lines)**  
+1. First line: the verdict label – `sound`, `needs-more-evidence`, or `rejected`.  
+2. Second line: a concise justification (1‑2 sentences) that cites the relevant criterion numbers or names that led to your decision.
 
-Provide the verdict label (**sound**, **needs‑more‑evidence**, or **rejected**) followed by a brief explanation that cites the specific criteria that led to your decision.
-
-Respond with your verdict and your reasoning.+Produce only these two lines, nothing else.
```

### Island 1, cell (2, 5), scalar 0.6094

parent `3bd0fcc21178bc2c` -> candidate `fa861a51f6835ab2`

```diff
--- parent 3bd0fcc21178bc2c
+++ candidate fa861a51f6835ab2
@@ -1,25 +1,25 @@
-You are reviewing a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Your task is to read the provided submission and judge it according to the criteria in Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are evaluating a capability case that proposes to remove per‑action human approval for an industrial operational‑change gateway action. Use the criteria from Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Evaluation checklist**
+**Checklist**
 
-1. **Real‑world testing** – Has the team performed realistic lab, test‑bed, or field trials that demonstrate the capability works under expected conditions?
-2. **Failure‑mode analysis** – Is there a documented analysis of what could go wrong (e.g., edge cases, sensor failures, adversarial inputs) and mitigations for each?
-3. **Audit trail / traceability** – Does the solution produce a reliable, tamper‑evident log of decisions and actions that can be reviewed later?
-4. **Human‑equivalence comparison** – Has the agent’s decision‑making been benchmarked against qualified human operators, showing comparable or better performance?
-5. **Absence of anti‑patterns** – Verify that none of the Section 9 anti‑patterns (e.g., “single point of automated decision without fallback”, “unchecked escalation”, “opaque AI without explainability”) are present.
+1. **Real‑world testing** – Evidence of lab, test‑bed, or field trials showing the capability works under realistic conditions.  
+2. **Failure‑mode analysis** – Documented identification of possible failure modes (e.g., sensor loss, edge cases, adversarial input) with mitigation or containment strategies.  
+3. **Audit‑trail / traceability** – The solution creates a tamper‑evident log of decisions, actions, and system state that can be reviewed after the fact.  
+4. **Human‑equivalence benchmark** – Quantitative or qualitative comparison showing the autonomous decision‑making matches or exceeds qualified human operators.  
+5. **Anti‑pattern scan** – Confirm that none of the Section 9 anti‑patterns are present (e.g., single‑point automated decision without fallback, unchecked escalation, opaque AI without explainability, irreversible actions).
 
-**Verdict rules**
+**Verdict determination**
 
-- **sound** – All essential checklist items (1‑4) are convincingly satisfied **and** no anti‑pattern from (5) is detected.
-- **needs-more-evidence** – One or more essential items are missing, weak, or only partially addressed, but no fatal anti‑pattern is found.
-- **rejected** – Any anti‑pattern from (5) is present **or** the evidence shows a high‑risk gap that makes the proposal unsafe.
+- **sound** – Items 1‑4 are fully satisfied **and** no anti‑pattern from item 5 is found.  
+- **needs-more-evidence** – One or more of items 1‑4 are missing, weak, or only partially addressed, **and** no anti‑pattern is detected.  
+- **rejected** – Any anti‑pattern from item 5 is present **or** a critical safety gap (e.g., missing mitigation for a high‑impact failure mode) makes the proposal unsafe.
 
-**Output format (must be followed exactly)**
+**Output format (must be reproduced exactly)**
 
 ```
 Verdict: <sound|needs-more-evidence|rejected>
 Reasoning:
-<your concise explanation, referencing which checklist items were met, missing, or violated>
+<concise explanation that cites which checklist items are met, missing, or violated>
 ```
 
-Do not include any additional commentary, headings, or formatting beyond what is shown above.+Provide only the two sections above; do not add any other text, headings, or formatting.
```

### Island 1, cell (0, 5), scalar 0.6497

parent `3bd0fcc21178bc2c` -> candidate `24023dc87656d67d`

```diff
--- parent 3bd0fcc21178bc2c
+++ candidate 24023dc87656d67d
@@ -1,25 +1,20 @@
-You are reviewing a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Your task is to read the provided submission and judge it according to the criteria in Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are evaluating a capability case that seeks to relax per‑action human approval for an industrial operational‑change gateway action. Use the criteria from Section 8 (Strategy C, capability‑based opening) and verify that none of the anti‑patterns from Section 9 appear.
 
-**Evaluation checklist**
+**Checklist (must be addressed by the submission)**  
+1. **Testing** – realistic lab, test‑bed, or field trials showing the capability works under expected conditions.  
+2. **Failure analysis** – documented identification of possible failure modes (edge cases, sensor loss, adversarial input, etc.) with mitigations.  
+3. **Audit trail** – tamper‑evident logs that record decisions, actions, and system state for later review.  
+4. **Human‑equivalence** – evidence that the automated decision‑making matches or exceeds qualified human operators.  
+5. **Anti‑pattern scan** – confirmation that no Section 9 anti‑patterns (e.g., single‑point automated decision without fallback, unchecked escalation, opaque AI, no rollback/override) are present.
 
-1. **Real‑world testing** – Has the team performed realistic lab, test‑bed, or field trials that demonstrate the capability works under expected conditions?
-2. **Failure‑mode analysis** – Is there a documented analysis of what could go wrong (e.g., edge cases, sensor failures, adversarial inputs) and mitigations for each?
-3. **Audit trail / traceability** – Does the solution produce a reliable, tamper‑evident log of decisions and actions that can be reviewed later?
-4. **Human‑equivalence comparison** – Has the agent’s decision‑making been benchmarked against qualified human operators, showing comparable or better performance?
-5. **Absence of anti‑patterns** – Verify that none of the Section 9 anti‑patterns (e.g., “single point of automated decision without fallback”, “unchecked escalation”, “opaque AI without explainability”) are present.
+**Verdict determination (apply in order)**  
+- **rejected** – any anti‑pattern from item 5 is found **or** a critical safety gap is evident.  
+- **sound** – items 1‑4 are all fully satisfied **and** no anti‑pattern is detected.  
+- **needs-more-evidence** – otherwise (one or more of items 1‑4 missing, weak, or only partially addressed, with no anti‑pattern).
 
-**Verdict rules**
-
-- **sound** – All essential checklist items (1‑4) are convincingly satisfied **and** no anti‑pattern from (5) is detected.
-- **needs-more-evidence** – One or more essential items are missing, weak, or only partially addressed, but no fatal anti‑pattern is found.
-- **rejected** – Any anti‑pattern from (5) is present **or** the evidence shows a high‑risk gap that makes the proposal unsafe.
-
-**Output format (must be followed exactly)**
-
+**Output (exactly two lines, no extra text or formatting)**  
 ```
 Verdict: <sound|needs-more-evidence|rejected>
-Reasoning:
-<your concise explanation, referencing which checklist items were met, missing, or violated>
+Reasoning: <brief explanation citing which checklist items are met, missing, or violated>
 ```
-
-Do not include any additional commentary, headings, or formatting beyond what is shown above.+The reasoning should reference the numbered checklist items (e.g., “Missing testing (1) and incomplete failure analysis (2)”). Do not add headings, bullet points, or additional lines.
```

### Island 2, cell (0, 4), scalar 0.2448

parent `d9adee957e5d0bc1` -> candidate `7fa1a4bfb6c07da9`

```diff
--- parent d9adee957e5d0bc1
+++ candidate 7fa1a4bfb6c07da9
@@ -1,26 +1,35 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action.  
-Your task is to read the submitted material and assign **one** of the three verdicts defined in the whitepaper (Section 8, Strategy C):
+You are reviewing a capability case that proposes to remove per‑action human approval for an operational‑change gateway action. Based **only** on the supplied submission, assign **one** of the three verdicts defined in the whitepaper (Section 8, Strategy C):
 
-* **sound** – the case provides sufficient, concrete evidence that the change is safe and complies with the anti‑patterns of Section 9.  
-* **needs‑more‑evidence** – the case is plausibly beneficial but lacks key information or testing to satisfy the safety criteria.  
-* **rejected** – the case contains a serious flaw (e.g., missing audit‑trail, unaddressed failure mode, or direct conflict with an anti‑pattern) that makes the proposal unsafe.
+* **sound** – all safety evidence required by Section 8 is present and no anti‑pattern from Section 9 appears.  
+* **needs‑more‑evidence** – the case is promising but one or more required items are insufficient or missing, yet no critical anti‑pattern is found.  
+* **rejected** – the submission exhibits a disqualifying anti‑pattern or a critical safety flaw.
 
-When making your decision, consider the following checklist (all items are required for a **sound** verdict; missing or weak items push the verdict to **needs‑more‑evidence**, and any critical failure results in **rejected**):
+**Decision checklist**
 
-1. **Real‑world testing** – evidence of controlled experiments, pilot runs, or simulations that demonstrate the system behaves correctly under realistic conditions.  
-2. **Failure analysis** – identification of plausible failure modes, their impact, and mitigations or fallback procedures.  
-3. **Audit trail & observability** – clear description of logging, monitoring, and post‑hoc review mechanisms that enable reconstruction of decisions.  
-4. **Human‑decision comparison** – quantitative or qualitative comparison showing the automated decision aligns with, or improves upon, a human operator’s judgment.  
-5. **Compliance with anti‑patterns (Section 9)** – explicit confirmation that none of the listed anti‑patterns (e.g., “single point of failure”, “opaque decision logic”, “unbounded delegation”) are present.
+1. **Anti‑pattern scan (Section 9)** – reject immediately if any of the following is present:
+   - Unbounded automation with no safe‑stop/fallback.  
+   - Absence of human‑in‑the‑loop for high‑impact actions.  
+   - Opaque, non‑explainable decision logic.  
+   - Missing audit‑trail, monitoring, or drift‑detection.  
+   - Direct conflict with safety, security, or regulatory policies.
 
-**Output format** (do not add any extra text):  
+2. **Evidence requirements (Section 8, Strategy C)** – all must be satisfied for a **sound** verdict:
+   - **Real‑world testing** – controlled experiments, pilot runs, or realistic simulations showing correct behavior.  
+   - **Failure‑mode analysis** – identified failure modes, impact assessment, and mitigations or fallback procedures.  
+   - **Audit trail & observability** – logging/telemetry that enables post‑hoc reconstruction of decisions.  
+   - **Human‑decision comparison** – quantitative or qualitative evidence that the automated decision matches or exceeds expert human judgment.  
+   - **Anti‑pattern compliance** – explicit statement that none of the Section 9 anti‑patterns apply.
+
+**Verdict rule**
+- If any anti‑pattern is detected → **rejected**.  
+- Else if the five evidence items are all met (or any minor gap is fully mitigated) → **sound**.  
+- Otherwise → **needs‑more‑evidence**.
+
+**Output format** (no additional text, exactly two lines):
 
 ```
 Verdict: <sound|needs-more-evidence|rejected>
-Reasoning: <concise explanation referencing the checklist items above and citing specific evidence or missing evidence from the submission>
+Reasoning: <brief justification referencing the checklist items and specific evidence or gaps>
 ```
 
-- Begin with the word “Verdict:” followed by the chosen label.  
-- On the next line start with “Reasoning:” and provide a brief, bullet‑style or sentence‑style justification, pointing to the relevant sections of the submission.
-
-Make your judgement based solely on the information provided; do not assume any unstated facts.+Begin the first line with “Verdict:” and the second with “Reasoning:”. Keep the reasoning to 1‑3 sentences, citing which checklist items influenced your decision.
```

### Island 2, cell (0, 5), scalar 0.5529

parent `d9adee957e5d0bc1` -> candidate `6e8cb17719e84cfc`

```diff
--- parent d9adee957e5d0bc1
+++ candidate 6e8cb17719e84cfc
@@ -1,26 +1,33 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action.  
-Your task is to read the submitted material and assign **one** of the three verdicts defined in the whitepaper (Section 8, Strategy C):
+You are assessing a capability case that seeks to remove the per‑action human‑approval step for an operational‑change gateway action.
 
-* **sound** – the case provides sufficient, concrete evidence that the change is safe and complies with the anti‑patterns of Section 9.  
-* **needs‑more‑evidence** – the case is plausibly beneficial but lacks key information or testing to satisfy the safety criteria.  
-* **rejected** – the case contains a serious flaw (e.g., missing audit‑trail, unaddressed failure mode, or direct conflict with an anti‑pattern) that makes the proposal unsafe.
+Read the submission and assign **exactly one** verdict from the whitepaper (Section 8, Strategy C):
 
-When making your decision, consider the following checklist (all items are required for a **sound** verdict; missing or weak items push the verdict to **needs‑more‑evidence**, and any critical failure results in **rejected**):
+* **sound** – all safety‑related requirements are fully satisfied.  
+* **needs‑more‑evidence** – the proposal is plausible but one or more required elements are missing or only partially addressed.  
+* **rejected** – a critical flaw or an anti‑pattern (Section 9) is present, making the proposal unsafe.
 
-1. **Real‑world testing** – evidence of controlled experiments, pilot runs, or simulations that demonstrate the system behaves correctly under realistic conditions.  
-2. **Failure analysis** – identification of plausible failure modes, their impact, and mitigations or fallback procedures.  
-3. **Audit trail & observability** – clear description of logging, monitoring, and post‑hoc review mechanisms that enable reconstruction of decisions.  
-4. **Human‑decision comparison** – quantitative or qualitative comparison showing the automated decision aligns with, or improves upon, a human operator’s judgment.  
-5. **Compliance with anti‑patterns (Section 9)** – explicit confirmation that none of the listed anti‑patterns (e.g., “single point of failure”, “opaque decision logic”, “unbounded delegation”) are present.
+**Required checklist** (all must be present for a **sound** verdict; any missing/weak item ⇒ **needs‑more‑evidence**; any critical failure ⇒ **rejected**):
 
-**Output format** (do not add any extra text):  
+1. **Real‑world validation** – controlled experiments, pilot runs, or realistic simulations proving correct behavior.  
+2. **Failure‑mode analysis** – identified failure modes, impact assessment, and concrete mitigations or safe‑stop procedures.  
+3. **Audit‑trail & observability** – logging, monitoring, and post‑hoc review mechanisms that allow full reconstruction of decisions.  
+4. **Human‑decision comparison** – quantitative or qualitative evidence that the automated decision matches or exceeds expert human judgment.  
+5. **Anti‑pattern compliance (Section 9)** – explicit confirmation that none of the disqualifying patterns (e.g., single point of failure, opaque decision logic, unbounded delegation, lack of fallback) exist.
+
+**Decision rule**
+
+- If items 1‑5 are all satisfied (or any minor gaps are clearly mitigated), output **sound**.  
+- If any item is missing or only partially satisfied and no anti‑pattern is found, output **needs‑more‑evidence**.  
+- If an anti‑pattern is present or a critical safety failure is unaddressed, output **rejected**.
+
+**Output format** (no extra text, no headings, no markup):
 
 ```
 Verdict: <sound|needs-more-evidence|rejected>
-Reasoning: <concise explanation referencing the checklist items above and citing specific evidence or missing evidence from the submission>
+Reasoning: <brief justification citing the checklist items and specific evidence or gaps from the submission>
 ```
 
-- Begin with the word “Verdict:” followed by the chosen label.  
-- On the next line start with “Reasoning:” and provide a brief, bullet‑style or sentence‑style justification, pointing to the relevant sections of the submission.
+- The first line must start with “Verdict:” followed by the exact label.  
+- The second line must start with “Reasoning:” and contain a concise explanation (one‑sentence or short bullet style) that references the relevant checklist points.
 
-Make your judgement based solely on the information provided; do not assume any unstated facts.+Make your judgment solely on the information provided; do not assume any unstated facts.
```

### Island 3, cell (1, 5), scalar 0.7554

parent `5c5c1c28d69630da` -> candidate `9d053e8f9a0afa4a`

```diff
--- parent 5c5c1c28d69630da
+++ candidate 9d053e8f9a0afa4a
@@ -1,20 +1,20 @@
-You act as an independent reviewer for a capability case that seeks to waive the per‑action human‑approval gate on an industrial operational‑change action. Examine the supplied evidence and then produce **exactly two lines**:
+You are an independent assessor for a capability case that proposes to waive the per‑action human‑approval gate on an industrial operational‑change action. Review the provided evidence and then output **exactly two lines**:
 
-1. **Verdict line** – write one of the three tokens **sound**, **needs-more-evidence**, or **rejected** (lower‑case, no extra text).  
-2. **Rationale line** – a concise (1‑3 sentence) explanation that cites the specific checklist items that led to your decision.
+1. **Verdict line** – write only one of the three tokens `sound`, `needs-more-evidence`, or `rejected` (lower‑case, no surrounding text).  
+2. **Rationale line** – a brief explanation (1‑3 sentences) that references the specific checklist items influencing your decision.
 
-Use the following checklist, derived from Section 8 (Strategy C) and the anti‑pattern list in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper:
+**Checklist (derived from Section 8 and Section 9 of the ITOT‑boundary‑as‑architecture whitepaper)**  
 
-* **Testing** – Has the team run end‑to‑end, production‑like trials with documented scope, repeatability, and results?  
-* **Failure analysis** – Are realistic failure modes (sensor loss, network split, unexpected agent behavior, etc.) identified and mitigated with fail‑safe or rollback procedures?  
-* **Auditability** – Is there an immutable log or trace that can reconstruct the automated decision and its context?  
-* **Human benchmark** – Does the case compare the automated outcomes to a qualified human operator’s decisions, showing equal or better safety/quality?  
-* **Anti‑pattern check** – Verify that none of the Section 9 anti‑patterns (e.g., no fallback, opaque logic, single‑point delegation, unchecked authority escalation) appear.
+- **Testing** – documented end‑to‑end, production‑like trials with clear scope, repeatability and results.  
+- **Failure analysis** – realistic failure modes identified (e.g., sensor loss, network partition, agent mis‑behaviour) and mitigated through fail‑safe or rollback procedures.  
+- **Auditability** – immutable logging or tracing that can reconstruct the automated decision and its context.  
+- **Human benchmark** – comparison showing the automated outcome is at least as safe/accurate as a qualified human operator.  
+- **Anti‑pattern check** – confirmation that none of the Section 9 anti‑patterns (no fallback, opaque logic, single‑point delegation, unchecked authority escalation, etc.) are present.
 
-**Decision rules**
+**Decision criteria**
 
-* **sound** – every checklist item is satisfied at a level that convincingly demonstrates the capability can replace human approval, and no anti‑patterns are present.  
-* **needs-more-evidence** – one or more items are addressed but lack depth, data, or clear justification; no fatal flaw is found.  
-* **rejected** – a critical item is missing or an anti‑pattern is evident, making the proposal unsafe or non‑compliant.
+- **sound** – every checklist item is satisfied to a convincing level and no anti‑pattern is found.  
+- **needs-more-evidence** – one or more items are addressed but lack sufficient depth, data, or justification; no fatal flaw is detected.  
+- **rejected** – a critical item is missing or an anti‑pattern is evident, making the proposal unsafe or non‑compliant.
 
-Follow the two‑line output format exactly; do not add headings, markup, or extra text.+Produce the two‑line output exactly as described; do not add headings, markup, or any extra text.
```


## Lesson retirement (dry run)

- Lesson 15: **RETIRED** — precision 0.115 vs base 0.482, 9.7 sigma below
- Lesson 17: **kept** — precision 0.986 >= base 0.694
- Lesson 19: **kept** — precision 0.983 >= base 0.881
- Lesson 11: **kept** — precision 0.750 vs base 0.918, only 0.8 sigma below

## Held-out check (best-ever candidate)

- Candidate: `3964302502b3b1ed` (rotation scalar 0.8606)
- Held-out quality: 0.6619 (passes: 0.6011, 0.7227)
- Held-out scalar: 0.5661 (passes: 0.5010, 0.6313)
- All held-out tasks valid: True

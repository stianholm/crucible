# Generation 5 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31.0
- Prefix cache hit rate: 43.0%
- Aggregate throughput: 82.3 tok/s (102896 completion tokens / 1250.7s)

## Archive

- Island 0: coverage 11.1%, QD score 2.302, unique ancestors 3
- Island 1: coverage 11.1%, QD score 2.982, unique ancestors 2
- Island 2: coverage 11.1%, QD score 1.690, unique ancestors 3
- Island 3: coverage 5.6%, QD score 1.552, unique ancestors 1
- Cells newly claimed this generation: 7

## Quality

- Best scalar this generation: 0.8319
- Median scalar of newly-claimed: 0.8257

## Cost

- Budget: {'generation': 5, 'max_generations': 30, 'tokens_used_total': 1507149, 'max_tokens': 2000000, 'elapsed_s_total': 4250.8, 'generation_wall_s': 1250.7}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 0, cell (0, 1), scalar 0.8259

parent `dfc3faf9a8c65595` -> candidate `5ead53ed4ecb7e6b`

```diff
--- parent dfc3faf9a8c65595
+++ candidate 5ead53ed4ecb7e6b
@@ -1,17 +1,17 @@
-You are evaluating a capability case that proposes removing per‑action human approval for an industrial operational‑change gateway action. Judge the case according to Section 8 (Strategy C, capability‑based opening) and verify that none of the anti‑patterns from Section 9 of the ITOT‑boundary‑as‑architecture whitepaper appear.
+You are reviewing a capability case that seeks to drop per‑action human approval for an industrial operational‑change gateway. Determine the verdict—**sound**, **needs‑more‑evidence**, or **rejected**—by checking the submission against the five evidence requirements from Section 8 (Strategy C) and confirming that none of the Section 9 anti‑patterns appear.
 
-**Evaluation criteria**
-1. **Real‑world testing** – documented pilots or production‑like trials that demonstrate reliable operation.  
-2. **Risk analysis** – identified failure modes, impact assessments, and concrete mitigations (e.g., safe‑state fallback, human override).  
-3. **Auditability** – immutable logs or traces that record inputs, decisions, and outcomes for post‑incident review.  
+**Evidence requirements**
+1. **Real‑world testing** – pilot or production‑like trials that prove reliable operation.  
+2. **Risk analysis** – clear identification of failure modes, impact assessment, and concrete mitigations (e.g., safe‑state fallback, human‑override).  
+3. **Auditability** – immutable logs or traces capturing inputs, decisions, and outcomes for post‑incident review.  
 4. **Human‑parity evidence** – quantitative or qualitative comparison showing the system’s decisions match those of a qualified human.  
-5. **Anti‑pattern check** – no occurrence of any Section 9 anti‑patterns (e.g., uncontrolled autonomy, single‑point automation failure, opaque reasoning, missing fallback).
+5. **Anti‑pattern compliance** – absence of any Section 9 anti‑patterns such as uncontrolled autonomy, single‑point automation failure, opaque reasoning, or missing fallback.
 
-**Decision rules**
-- **sound** – all five criteria are fully satisfied and no anti‑pattern is found.  
-- **needs‑more‑evidence** – one or more criteria are only partially addressed or missing, but no anti‑pattern is present.  
-- **rejected** – any criterion is fundamentally absent **or** any anti‑pattern is identified.
+**Verdict rules**
+- **sound** – all five requirements are fully satisfied and no anti‑pattern is found.  
+- **needs‑more‑evidence** – one or more requirements are only partially addressed or missing, but no anti‑pattern is present.  
+- **rejected** – any requirement is fundamentally absent **or** any anti‑pattern is identified.
 
 **Output**
-1. On the first line write the verdict label exactly as `sound`, `needs-more-evidence`, or `rejected`.  
-2. On the following line(s) give a concise rationale (2‑4 sentences) that cites the most relevant criterion or anti‑pattern influencing your decision. Do not include any other text, headings, or formatting.+1. Write the verdict label (`sound`, `needs‑more‑evidence`, or `rejected`) on the first line.  
+2. On the next line(s) give a concise rationale (2‑4 sentences) that cites the most relevant requirement(s) or anti‑pattern(s) influencing your decision. Do not add any other text, headings, or formatting.
```

### Island 1, cell (1, 1), scalar 0.8257

parent `2071b631e0cadc12` -> candidate `83860a1e19033747`

```diff
--- parent 2071b631e0cadc12
+++ candidate 83860a1e19033747
@@ -1,21 +1,19 @@
-You are an auditor evaluating a proposal to remove per‑action human approval for an industrial operational‑change gateway. Your decision must be one of **sound**, **needs‑more‑evidence**, or **rejected** according to Section 8 (Strategy C) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are an auditor deciding whether a proposal to drop per‑action human approval for an industrial operational‑change gateway meets the standards of Section 8 (Strategy C) and avoids the anti‑patterns of Section 9 in the ITOT‑boundary‑as‑architecture whitepaper. Choose exactly one verdict: **sound**, **needs‑more‑evidence**, or **rejected**.
 
-**Mandatory evidence categories**
-
-1. **Real‑world validation** – staged runs, simulations, or pilots that demonstrate safe automated execution.  
+**Evidence requirements (must all be satisfied for a “sound” verdict)**  
+1. **Real‑world validation** – staged runs, simulations, or pilots that prove safe automated execution.  
 2. **Failure‑mode analysis** – identified failure modes, worst‑case impact, and concrete mitigation or rollback plans.  
 3. **Auditability** – immutable logs, provenance data, or other traceability mechanisms for post‑action review.  
-4. **Human‑parity** – quantitative or qualitative comparison of the automated decisions against expert human decisions on a representative set.  
+4. **Human‑parity evidence** – quantitative or qualitative comparison of the automated decisions against expert human decisions on a representative set.  
 5. **Anti‑pattern check** – confirmation that none of the Section 9 anti‑patterns (e.g., single point of failure, unchecked escalation, opaque logic, missing fallback) are present.
 
-**Decision rules**
-
-- **rejected** – any anti‑pattern is detected, or the submission shows a clear safety/security breach.  
-- **needs‑more‑evidence** – one or more of the five mandatory categories are missing or only partially addressed, with no anti‑pattern present.  
-- **sound** – all five categories are fully satisfied and no anti‑pattern is found.
+**Decision logic**  
+- **rejected** – any anti‑pattern is found, or any requirement reveals a clear safety or security breach.  
+- **needs‑more‑evidence** – one or more of the five requirements are missing or only partially addressed, with no anti‑pattern detected.  
+- **sound** – all five requirements are fully satisfied and no anti‑pattern is present.
 
 **Output (exactly two lines)**  
 1. The verdict word: `sound`, `needs-more-evidence`, or `rejected`.  
-2. A brief justification (1‑3 sentences) that cites the specific category(ies) or anti‑pattern(s) that drove your decision.  
+2. A brief justification (1‑3 sentences) that cites the specific requirement(s) or anti‑pattern(s) that led to your decision.  
 
-Do not include any other text, headings, or formatting.+Do not add any other text, headings, or formatting.
```

### Island 1, cell (0, 1), scalar 0.8216

parent `2071b631e0cadc12` -> candidate `39f3eba98e28e43f`

```diff
--- parent 2071b631e0cadc12
+++ candidate 39f3eba98e28e43f
@@ -1,21 +1,19 @@
-You are an auditor evaluating a proposal to remove per‑action human approval for an industrial operational‑change gateway. Your decision must be one of **sound**, **needs‑more‑evidence**, or **rejected** according to Section 8 (Strategy C) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are auditing a request to drop per‑action human approval for an industrial operational‑change gateway. Choose one verdict—**sound**, **needs‑more‑evidence**, or **rejected**—based on Section 8 (Strategy C) and the anti‑patterns in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Mandatory evidence categories**
+**Evidence required (all must be fully satisfied for a “sound” verdict)**  
+1. **Real‑world validation** – staged runs, simulations, or pilots proving safe automated operation.  
+2. **Failure‑mode analysis** – list of possible faults, worst‑case impact, and concrete mitigation/rollback steps.  
+3. **Auditability** – immutable logs, provenance, or other traceability that enables post‑action review.  
+4. **Human‑parity evidence** – quantitative or qualitative comparison showing the automation matches expert human decisions on a representative dataset.  
+5. **Anti‑pattern check** – confirmation that none of the Section 9 anti‑patterns (e.g., single point of failure, unchecked escalation, opaque logic, missing fallback) appear.
 
-1. **Real‑world validation** – staged runs, simulations, or pilots that demonstrate safe automated execution.  
-2. **Failure‑mode analysis** – identified failure modes, worst‑case impact, and concrete mitigation or rollback plans.  
-3. **Auditability** – immutable logs, provenance data, or other traceability mechanisms for post‑action review.  
-4. **Human‑parity** – quantitative or qualitative comparison of the automated decisions against expert human decisions on a representative set.  
-5. **Anti‑pattern check** – confirmation that none of the Section 9 anti‑patterns (e.g., single point of failure, unchecked escalation, opaque logic, missing fallback) are present.
+**Decision logic**  
+- **rejected** – any anti‑pattern is found, or any evidence reveals a clear safety or security breach.  
+- **needs‑more‑evidence** – one or more of the five evidence items are missing or only partially addressed, with no anti‑pattern detected.  
+- **sound** – every evidence item is completely satisfied and no anti‑pattern exists.
 
-**Decision rules**
+**Output (exactly two lines, no extra text)**  
+1. The verdict word: `sound`, `needs-more-evidence`, or `rejected`.  
+2. A concise justification (1‑3 sentences) that cites the specific evidence item(s) or anti‑pattern(s) that led to your decision.  
 
-- **rejected** – any anti‑pattern is detected, or the submission shows a clear safety/security breach.  
-- **needs‑more‑evidence** – one or more of the five mandatory categories are missing or only partially addressed, with no anti‑pattern present.  
-- **sound** – all five categories are fully satisfied and no anti‑pattern is found.
-
-**Output (exactly two lines)**  
-1. The verdict word: `sound`, `needs-more-evidence`, or `rejected`.  
-2. A brief justification (1‑3 sentences) that cites the specific category(ies) or anti‑pattern(s) that drove your decision.  
-
-Do not include any other text, headings, or formatting.+Do not add headings, bullet points, or any other formatting beyond the two required lines.
```

### Island 1, cell (1, 2), scalar 0.8256

parent `2071b631e0cadc12` -> candidate `ec0ebcab1ed5e5af`

```diff
--- parent 2071b631e0cadc12
+++ candidate ec0ebcab1ed5e5af
@@ -1,21 +1,19 @@
-You are an auditor evaluating a proposal to remove per‑action human approval for an industrial operational‑change gateway. Your decision must be one of **sound**, **needs‑more‑evidence**, or **rejected** according to Section 8 (Strategy C) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are reviewing a request to eliminate per‑action human approval for an industrial operational‑change gateway. Evaluate the submission against the five evidence areas required by Section 8 (Strategy C) and verify that none of the Section 9 anti‑patterns are present.
 
-**Mandatory evidence categories**
+**Evidence areas (must be satisfied)**  
+1. **Real‑world validation** – staged runs, simulations, or pilot deployments that show the automation can operate safely.  
+2. **Failure‑mode analysis** – identification of possible faults, worst‑case consequences, and concrete mitigation or rollback procedures.  
+3. **Auditability** – immutable logging, provenance records, or other traceability that enables post‑action review.  
+4. **Human‑parity proof** – quantitative or qualitative comparison demonstrating the automated decision matches expert human decisions on a representative sample.  
+5. **Anti‑pattern clearance** – confirmation that no Section 9 anti‑patterns (e.g., single point of failure, unchecked escalation, opaque logic, missing fallback) exist.
 
-1. **Real‑world validation** – staged runs, simulations, or pilots that demonstrate safe automated execution.  
-2. **Failure‑mode analysis** – identified failure modes, worst‑case impact, and concrete mitigation or rollback plans.  
-3. **Auditability** – immutable logs, provenance data, or other traceability mechanisms for post‑action review.  
-4. **Human‑parity** – quantitative or qualitative comparison of the automated decisions against expert human decisions on a representative set.  
-5. **Anti‑pattern check** – confirmation that none of the Section 9 anti‑patterns (e.g., single point of failure, unchecked escalation, opaque logic, missing fallback) are present.
-
-**Decision rules**
-
-- **rejected** – any anti‑pattern is detected, or the submission shows a clear safety/security breach.  
-- **needs‑more‑evidence** – one or more of the five mandatory categories are missing or only partially addressed, with no anti‑pattern present.  
-- **sound** – all five categories are fully satisfied and no anti‑pattern is found.
+**Decision rules**  
+- **rejected** – any anti‑pattern is found or a clear safety/security breach is evident.  
+- **needs‑more‑evidence** – one or more of the five evidence areas are missing or only partially addressed, with no anti‑pattern detected.  
+- **sound** – all five evidence areas are fully satisfied and no anti‑pattern is present.
 
 **Output (exactly two lines)**  
-1. The verdict word: `sound`, `needs-more-evidence`, or `rejected`.  
-2. A brief justification (1‑3 sentences) that cites the specific category(ies) or anti‑pattern(s) that drove your decision.  
+1. One word: `sound`, `needs-more-evidence`, or `rejected`.  
+2. A concise justification (1‑3 sentences) that cites the specific evidence area(s) or anti‑pattern(s) influencing the verdict.
 
-Do not include any other text, headings, or formatting.+Do not add any other text, headings, or formatting.
```

### Island 1, cell (1, 1), scalar 0.8295

parent `2071b631e0cadc12` -> candidate `0a1cba46dc06071a`

```diff
--- parent 2071b631e0cadc12
+++ candidate 0a1cba46dc06071a
@@ -1,21 +1,21 @@
-You are an auditor evaluating a proposal to remove per‑action human approval for an industrial operational‑change gateway. Your decision must be one of **sound**, **needs‑more‑evidence**, or **rejected** according to Section 8 (Strategy C) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You act as an auditor who must decide whether a proposal to drop per‑action human approval for an industrial operational‑change gateway is **sound**, **needs‑more‑evidence**, or **rejected**. Your judgment follows Section 8 (Strategy C) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Mandatory evidence categories**
+**Required evidence**
 
-1. **Real‑world validation** – staged runs, simulations, or pilots that demonstrate safe automated execution.  
-2. **Failure‑mode analysis** – identified failure modes, worst‑case impact, and concrete mitigation or rollback plans.  
-3. **Auditability** – immutable logs, provenance data, or other traceability mechanisms for post‑action review.  
-4. **Human‑parity** – quantitative or qualitative comparison of the automated decisions against expert human decisions on a representative set.  
-5. **Anti‑pattern check** – confirmation that none of the Section 9 anti‑patterns (e.g., single point of failure, unchecked escalation, opaque logic, missing fallback) are present.
+1. **Real‑world validation** – staged runs, simulations, or pilot studies that prove the automated action can be performed safely.  
+2. **Failure‑mode analysis** – a catalog of possible faults, the worst‑case consequence of each, and concrete mitigation or rollback procedures.  
+3. **Auditability** – immutable logging, provenance records, or other mechanisms that enable post‑action review.  
+4. **Human‑parity proof** – quantitative or qualitative comparison showing the automated decisions match expert human decisions on a representative data set.  
+5. **Anti‑pattern compliance** – explicit confirmation that none of the Section 9 anti‑patterns (single point of failure, unchecked escalation, opaque logic, missing fallback, etc.) exist.
 
-**Decision rules**
+**Decision hierarchy**
 
-- **rejected** – any anti‑pattern is detected, or the submission shows a clear safety/security breach.  
-- **needs‑more‑evidence** – one or more of the five mandatory categories are missing or only partially addressed, with no anti‑pattern present.  
-- **sound** – all five categories are fully satisfied and no anti‑pattern is found.
+- **rejected** – any anti‑pattern is identified or the submission contains an evident safety/security breach.  
+- **needs‑more‑evidence** – one or more of the five required items are absent or only partially satisfied, provided no anti‑pattern is found.  
+- **sound** – every required item is fully addressed and no anti‑pattern is present.
 
 **Output (exactly two lines)**  
 1. The verdict word: `sound`, `needs-more-evidence`, or `rejected`.  
-2. A brief justification (1‑3 sentences) that cites the specific category(ies) or anti‑pattern(s) that drove your decision.  
+2. A short justification (1‑3 sentences) that cites the specific evidence category(ies) or anti‑pattern(s) that determined your verdict.  
 
-Do not include any other text, headings, or formatting.+Do not add any other text, headings, or formatting.
```

### Island 3, cell (1, 2), scalar 0.7204

parent `6839ecc94619959f` -> candidate `2e457c3168a3a99e`

```diff
--- parent 6839ecc94619959f
+++ candidate 2e457c3168a3a99e
@@ -1,29 +1,22 @@
-You are evaluating a proposal that asks to drop the per‑action human‑approval requirement for an industrial operational‑change gateway.
+You are reviewing a proposal that seeks to remove the per‑action human‑approval requirement for an industrial operational‑change gateway.
 
-**Assessment dimensions (Section 8 – Strategy C & Section 9 – anti‑patterns):**
+**Evaluation criteria (Section 8 – Strategy C & Section 9 – anti‑patterns)**  
 
-1. **Validated performance** – realistic testing (sandbox, pilot, or production‑mirrored) that demonstrates reliable autonomous decisions.  
-2. **Risk & mitigation** – a documented analysis of failure modes together with concrete safeguards for safety, security and compliance.  
-3. **Traceability** – logs or other artefacts that let an auditor reconstruct every autonomous decision, its inputs and its outcome.  
-4. **Human‑level equivalence** – quantitative or qualitative comparison showing the system’s decisions meet or exceed those of qualified humans in the same scenarios.  
-5. **No disallowed anti‑patterns** – the proposal must not contain any pattern prohibited in Section 9 (e.g., eliminating fallback, removing traceability, exposing safety‑critical assets to unchecked autonomy).
+1. **Validated performance** – Evidence from sandbox, pilot, or production‑mirrored testing showing reliable autonomous decisions.  
+2. **Risk analysis & mitigation** – Documented failure‑mode analysis with concrete safeguards for safety, security and compliance.  
+3. **Traceability** – Logs or other artefacts that allow reconstruction of every autonomous decision, its inputs and outcome.  
+4. **Human‑level equivalence** – Quantitative or qualitative comparison demonstrating decisions meet or exceed those of qualified humans.  
+5. **Absence of prohibited anti‑patterns** – No use of any pattern listed in Section 9 (e.g., eliminating fallback, removing traceability, exposing safety‑critical assets to unchecked autonomy).
 
 **Decision rules**
 
-- **sound** – all five dimensions are fully satisfied and no anti‑pattern is present.  
-- **needs‑more‑evidence** – one or more dimensions are missing or only partially addressed, but no critical anti‑pattern appears.  
-- **rejected** – a listed anti‑pattern is evident **or** the evidence shows a clear safety, security, or compliance risk.
+- **sound** – All five criteria are fully satisfied and no anti‑pattern is present.  
+- **needs‑more‑evidence** – One or more criteria are missing or only partially addressed, but no anti‑pattern is found.  
+- **rejected** – Any prohibited anti‑pattern is evident **or** the submission shows an unavoidable safety, security, or compliance risk.
 
 **Output format**
 
 - **Line 1:** exactly `sound`, `needs‑more‑evidence`, or `rejected`.  
-- **Line 2 onward:** a brief rationale (1‑3 short sentences) that cites the relevant dimension(s). Do not add headings, bullet points, or extra text.
-
-*Example*
-
-```
-sound
-The case provides a full‑scale pilot with 96 % agreement to human operators, complete audit logs, and explicitly avoids every anti‑pattern.
-```
+- **Line 2 onward:** a brief rationale (1‑3 short sentences) that cites the specific criterion(ia) that determined the verdict. Do not include headings, bullet points, or any extra text.
 
 Read the submission, apply the rubric, and produce the verdict followed by the concise justification.
```

### Island 3, cell (1, 1), scalar 0.8319

parent `6839ecc94619959f` -> candidate `910e3e2dd8f08fc4`

```diff
--- parent 6839ecc94619959f
+++ candidate 910e3e2dd8f08fc4
@@ -1,29 +1,29 @@
-You are evaluating a proposal that asks to drop the per‑action human‑approval requirement for an industrial operational‑change gateway.
+You are reviewing a proposal that seeks to remove the per‑action human‑approval requirement for an industrial operational‑change gateway.
 
-**Assessment dimensions (Section 8 – Strategy C & Section 9 – anti‑patterns):**
+**Evaluation criteria (based on Section 8 – Strategy C and Section 9 – anti‑patterns)**
 
-1. **Validated performance** – realistic testing (sandbox, pilot, or production‑mirrored) that demonstrates reliable autonomous decisions.  
-2. **Risk & mitigation** – a documented analysis of failure modes together with concrete safeguards for safety, security and compliance.  
-3. **Traceability** – logs or other artefacts that let an auditor reconstruct every autonomous decision, its inputs and its outcome.  
-4. **Human‑level equivalence** – quantitative or qualitative comparison showing the system’s decisions meet or exceed those of qualified humans in the same scenarios.  
-5. **No disallowed anti‑patterns** – the proposal must not contain any pattern prohibited in Section 9 (e.g., eliminating fallback, removing traceability, exposing safety‑critical assets to unchecked autonomy).
+1. **Validated performance** – evidence from sandbox, pilot, or production‑mirrored testing showing the system makes reliable autonomous decisions.  
+2. **Risk analysis & mitigation** – a documented list of plausible failure modes together with concrete safeguards for safety, security and compliance.  
+3. **Traceability / auditability** – logs or other artefacts that enable reconstruction of every autonomous decision, its inputs and its outcome.  
+4. **Human‑level equivalence** – quantitative or qualitative comparison demonstrating that the system’s decisions meet or exceed those of qualified humans in the same scenarios.  
+5. **Absence of disallowed anti‑patterns** – the proposal must not contain any pattern prohibited in Section 9 (e.g., removing fallback to humans, eliminating traceability, granting unchecked autonomy to safety‑critical functions, etc.).
 
 **Decision rules**
 
-- **sound** – all five dimensions are fully satisfied and no anti‑pattern is present.  
-- **needs‑more‑evidence** – one or more dimensions are missing or only partially addressed, but no critical anti‑pattern appears.  
-- **rejected** – a listed anti‑pattern is evident **or** the evidence shows a clear safety, security, or compliance risk.
+- **sound** – all five criteria are fully satisfied and no anti‑pattern is present.  
+- **needs‑more‑evidence** – one or more criteria are missing or only partially addressed, and no anti‑pattern is detected.  
+- **rejected** – any listed anti‑pattern is present **or** the evidence reveals an unmitigated safety, security, or compliance risk.
 
-**Output format**
+**Required output**
 
-- **Line 1:** exactly `sound`, `needs‑more‑evidence`, or `rejected`.  
-- **Line 2 onward:** a brief rationale (1‑3 short sentences) that cites the relevant dimension(s). Do not add headings, bullet points, or extra text.
+- **Line 1:** exactly `sound`, `needs‑more‑evidence`, or `rejected` (no extra spaces or punctuation).  
+- **Line 2 onward:** a brief justification (1‑3 short sentences) that directly references the relevant criterion(ia). Do **not** use headings, bullet points, or any additional text.
 
 *Example*
 
 ```
 sound
-The case provides a full‑scale pilot with 96 % agreement to human operators, complete audit logs, and explicitly avoids every anti‑pattern.
+The case includes a full‑scale pilot with 96 % agreement to human operators, complete audit logs, and avoids every prohibited anti‑pattern.
 ```
 
-Read the submission, apply the rubric, and produce the verdict followed by the concise justification.+Read the submission, apply the criteria, and produce the verdict followed by the concise justification.
```

## Migration

- island 0 -> island 1: cell (0, 1), scalar 0.8259, claimed=True
- island 1 -> island 2: cell (1, 1), scalar 0.8295, claimed=True
- island 2 -> island 3: cell (1, 1), scalar 0.5116, claimed=False
- island 3 -> island 0: cell (1, 1), scalar 0.8319, claimed=True

## Lesson retirement (dry run)

- Lesson 4: **kept** — no control group (standing tier: needs PHASE-4.md task 4.5 arm A)
- Lesson 3: **kept** — no control group (standing tier: needs PHASE-4.md task 4.5 arm A)
- Lesson 5: **kept** — no control group (standing tier: needs PHASE-4.md task 4.5 arm A)
- Lesson 6: **kept** — no control group (standing tier: needs PHASE-4.md task 4.5 arm A)
- Lesson 7: **kept** — no control group (standing tier: needs PHASE-4.md task 4.5 arm A)
- Lesson 1: **kept** — no control group (standing tier: needs PHASE-4.md task 4.5 arm A)

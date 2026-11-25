# Generation 4 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31
- Prefix cache hit rate: 42.6%
- Aggregate throughput: 242.5 tok/s (83284 completion tokens / 343.4s)

## Archive

- Island 0: coverage 11.1%, QD score 1.671, unique ancestors 2
- Island 1: coverage 11.1%, QD score 2.029, unique ancestors 1
- Island 2: coverage 11.1%, QD score 1.372, unique ancestors 2
- Island 3: coverage 5.6%, QD score 0.700, unique ancestors 2
- Cells newly claimed this generation: 5

## Quality

- Best scalar this generation: 0.5137
- Median scalar of newly-claimed: 0.5112

## Cost

- Budget: {'generation': 4, 'max_generations': 30, 'tokens_used_total': 1202063, 'max_tokens': 2000000, 'elapsed_s_total': 3000.1, 'generation_wall_s': 343.4}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 0, cell (0, 1), scalar 0.5137

parent `84aba896d7ccb0c1` -> candidate `340d328097bbfbfa`

```diff
--- parent 84aba896d7ccb0c1
+++ candidate 340d328097bbfbfa
@@ -1,18 +1,18 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Your task is to decide whether the proposal should be judged **sound**, **needs‑more‑evidence**, or **rejected**, according to Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are assessing a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway action. Judge the case using Section 8 (Strategy C, capability‑based opening) and the anti‑patterns defined in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-Assess the submission against the following evidence criteria:
+**Evidence checklist**
+1. **Real‑world testing** – documented pilots or production‑like trials that prove the capability works reliably.
+2. **Risk analysis** – clear identification of failure modes, their impact, and mitigation (e.g., safe‑state fallback, human override).
+3. **Auditability** – immutable logs or traces of inputs, decisions, and outcomes suitable for post‑incident review.
+4. **Human‑parity evidence** – quantitative or qualitative comparison showing the system matches a qualified human’s decisions.
+5. **Anti‑pattern compliance** – none of the Section 9 anti‑patterns (e.g., trust‑by‑obscurity, single‑point automation failure, unbounded escalation) are present.
 
-1. **Real‑world testing** – Has the team performed controlled experiments or pilot runs that demonstrate the capability works reliably under realistic conditions?
-2. **Risk analysis** – Does the case identify plausible failure modes, their impact, and mitigation strategies (e.g., fallback to human control, safe‑state triggers)?
-3. **Auditability** – Is there a verifiable log or trace that records the agent’s decisions, inputs, and outcomes, enabling post‑incident review?
-4. **Human‑parity comparison** – Does the submission provide quantitative or qualitative comparison of the agent’s decisions against those a qualified human would make?
-5. **Compliance with anti‑patterns** – Verify that none of the Section 9 anti‑patterns are present (e.g., “trust‑by‑obscurity”, “single‑point‑automation failure”, “unbounded escalation”).
+**Decision criteria**
+- **sound** – all five checklist items are fully satisfied and no anti‑pattern is found.
+- **needs‑more‑evidence** – one or more items are partially addressed or missing, but no anti‑pattern appears.
+- **rejected** – any checklist item is fundamentally unsatisfied **or** any anti‑pattern is detected.
 
-**Decision rules**
-
-- **Sound** – All five criteria are satisfied to a degree that the evidence collectively demonstrates the capability can safely replace per‑action human approval.
-- **Needs‑more‑evidence** – One or more criteria are partially addressed or missing, but no critical red‑flag anti‑pattern is present.
-- **Rejected** – Any criterion is fundamentally unsatisfied **or** a Section 9 anti‑pattern is evident, indicating a serious safety or governance risk.
-
-**Output**  
-Return a single line with the verdict (`sound`, `needs‑more‑evidence`, or `rejected`) followed by a concise rationale (one‑ or two‑sentence explanation) that references the most relevant criteria or anti‑pattern(s). Do not include any additional text or headings. +**Output**
+1. First line: the verdict label exactly as `sound`, `needs-more-evidence`, or `rejected`.  
+2. Subsequent line(s): a brief rationale (1‑2 sentences) citing the most decisive checklist item(s) or anti‑pattern(s).  
+Do not add any other text, headings, or formatting. 
```

### Island 1, cell (0, 1), scalar 0.5063

parent `4d953d9eeca44c0a` -> candidate `5bd03c4b534f91e4`

```diff
--- parent 4d953d9eeca44c0a
+++ candidate 5bd03c4b534f91e4
@@ -1,22 +1,22 @@
-You are reviewing a capability case that seeks to eliminate per‑action human approval for an industrial operational‑change gateway. Your judgment must be **sound**, **needs‑more‑evidence**, or **rejected** in line with Section 8 (Strategy C) and the anti‑patterns of Section 9 in the ITOT‑boundary‑as‑architecture whitepaper.
+You act as an auditor for a capability case that proposes removing per‑action human approval from an industrial operational‑change gateway. Your task is to decide whether the case is **sound**, **needs‑more‑evidence**, or **rejected** according to Section 8 (Strategy C) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Evaluation checklist**
+**Evaluation criteria (must be assessed individually)**  
 
-1. **Real‑world validation** – Does the submission include staged runs, simulations, or pilots that prove the automated agent can safely perform the action?  
-2. **Failure‑mode analysis** – Is there a documented assessment of possible failures, worst‑case impacts, and mitigation or rollback plans?  
-3. **Audit trail** – Are immutable logs, provenance data, or other traceability mechanisms provided for post‑hoc review?  
-4. **Human‑parity evidence** – Are the agent’s decisions compared to expert human decisions on a representative set, with quantitative or qualitative results?  
-5. **Anti‑pattern compliance** – Verify that none of the Section 9 anti‑patterns (e.g., single point of failure, unchecked escalation, opaque logic, missing fallback) appear.
+1. **Real‑world validation** – presence of staged runs, simulations, or pilot deployments that demonstrate safe automated execution.  
+2. **Failure‑mode analysis** – documented identification of possible faults, worst‑case impact, and concrete mitigation or rollback procedures.  
+3. **Auditability** – provision of immutable logs, provenance data, or other traceability mechanisms for post‑action review.  
+4. **Human‑parity evidence** – quantitative or qualitative comparison of the automated decisions with expert human decisions on a representative dataset.  
+5. **Anti‑pattern check** – confirmation that none of the Section 9 anti‑patterns (e.g., single point of failure, unchecked escalation, opaque logic, missing fallback) are present.
 
-**Decision hierarchy**
+**Decision rules**
 
-- **Rejected** – Any anti‑pattern from Section 9 is present, or the evidence shows a clear safety or security breach.  
-- **Needs‑more‑evidence** – One or more checklist items are missing or only partially addressed, but no anti‑pattern is detected.  
-- **Sound** – All five checklist items are fully satisfied and no anti‑pattern is found.
+- **rejected** – any anti‑pattern is detected, or the submission contains an explicit safety or security violation.  
+- **needs‑more‑evidence** – one or more of the first four criteria are missing, incomplete, or only partially satisfied, and no anti‑pattern is found.  
+- **sound** – all five criteria are fully satisfied and no anti‑pattern appears.
 
-**Output format**
+**Output (exactly two lines, no extra text or formatting)**  
 
-1. **Verdict** – a single word: `sound`, `needs-more-evidence`, or `rejected`.  
-2. **Reasoning** – one to three concise sentences that reference the checklist items (or anti‑patterns) that led to your verdict.
+1. The verdict word: `sound`, `needs-more-evidence`, or `rejected`.  
+2. A brief justification (1‑3 sentences) that cites the specific criteria or anti‑patterns influencing your decision.
 
-Do not add any other text or formatting.+Do not add any headings, bullet points, or other content.
```

### Island 1, cell (1, 2), scalar 0.5063

parent `4d953d9eeca44c0a` -> candidate `2bc8cc585a45e1f2`

```diff
--- parent 4d953d9eeca44c0a
+++ candidate 2bc8cc585a45e1f2
@@ -1,22 +1,19 @@
-You are reviewing a capability case that seeks to eliminate per‑action human approval for an industrial operational‑change gateway. Your judgment must be **sound**, **needs‑more‑evidence**, or **rejected** in line with Section 8 (Strategy C) and the anti‑patterns of Section 9 in the ITOT‑boundary‑as‑architecture whitepaper.
+You are assessing a capability case that proposes removing per‑action human approval for an industrial operational‑change gateway. Produce a verdict of **sound**, **needs‑more‑evidence**, or **rejected** according to Section 8 (Strategy C) and the anti‑patterns defined in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Evaluation checklist**
+**Checklist (must be considered in order)**  
+1. **Real‑world validation** – staged runs, simulations, or pilots that demonstrate safe automated execution.  
+2. **Failure‑mode analysis** – documented possible faults, worst‑case impact, and mitigation/rollback plans.  
+3. **Auditability** – immutable logs, provenance data, or other traceability mechanisms for post‑action review.  
+4. **Human‑parity evidence** – quantitative or qualitative comparison of automated decisions with expert human decisions on a representative set.  
+5. **Anti‑pattern check** – verify none of the Section 9 anti‑patterns (e.g., single point of failure, unchecked escalation, opaque logic, missing fallback) are present.
 
-1. **Real‑world validation** – Does the submission include staged runs, simulations, or pilots that prove the automated agent can safely perform the action?  
-2. **Failure‑mode analysis** – Is there a documented assessment of possible failures, worst‑case impacts, and mitigation or rollback plans?  
-3. **Audit trail** – Are immutable logs, provenance data, or other traceability mechanisms provided for post‑hoc review?  
-4. **Human‑parity evidence** – Are the agent’s decisions compared to expert human decisions on a representative set, with quantitative or qualitative results?  
-5. **Anti‑pattern compliance** – Verify that none of the Section 9 anti‑patterns (e.g., single point of failure, unchecked escalation, opaque logic, missing fallback) appear.
+**Decision rules**  
+- **rejected** – any anti‑pattern is detected **or** any checklist item reveals a clear safety or security breach.  
+- **needs‑more‑evidence** – one or more checklist items are missing or only partially satisfied, with no anti‑pattern found.  
+- **sound** – all five checklist items are fully satisfied and no anti‑pattern is present.
 
-**Decision hierarchy**
+**Output (exactly two lines)**  
+1. The verdict word: `sound`, `needs-more-evidence`, or `rejected`.  
+2. A brief justification (1‑3 sentences) that cites the specific checklist numbers or anti‑patterns that drove your decision.
 
-- **Rejected** – Any anti‑pattern from Section 9 is present, or the evidence shows a clear safety or security breach.  
-- **Needs‑more‑evidence** – One or more checklist items are missing or only partially addressed, but no anti‑pattern is detected.  
-- **Sound** – All five checklist items are fully satisfied and no anti‑pattern is found.
-
-**Output format**
-
-1. **Verdict** – a single word: `sound`, `needs-more-evidence`, or `rejected`.  
-2. **Reasoning** – one to three concise sentences that reference the checklist items (or anti‑patterns) that led to your verdict.
-
-Do not add any other text or formatting.+Do not include any other text, headings, or formatting.
```

### Island 1, cell (0, 1), scalar 0.5125

parent `4d953d9eeca44c0a` -> candidate `2071b631e0cadc12`

```diff
--- parent 4d953d9eeca44c0a
+++ candidate 2071b631e0cadc12
@@ -1,22 +1,21 @@
-You are reviewing a capability case that seeks to eliminate per‑action human approval for an industrial operational‑change gateway. Your judgment must be **sound**, **needs‑more‑evidence**, or **rejected** in line with Section 8 (Strategy C) and the anti‑patterns of Section 9 in the ITOT‑boundary‑as‑architecture whitepaper.
+You are an auditor evaluating a proposal to remove per‑action human approval for an industrial operational‑change gateway. Your decision must be one of **sound**, **needs‑more‑evidence**, or **rejected** according to Section 8 (Strategy C) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Evaluation checklist**
+**Mandatory evidence categories**
 
-1. **Real‑world validation** – Does the submission include staged runs, simulations, or pilots that prove the automated agent can safely perform the action?  
-2. **Failure‑mode analysis** – Is there a documented assessment of possible failures, worst‑case impacts, and mitigation or rollback plans?  
-3. **Audit trail** – Are immutable logs, provenance data, or other traceability mechanisms provided for post‑hoc review?  
-4. **Human‑parity evidence** – Are the agent’s decisions compared to expert human decisions on a representative set, with quantitative or qualitative results?  
-5. **Anti‑pattern compliance** – Verify that none of the Section 9 anti‑patterns (e.g., single point of failure, unchecked escalation, opaque logic, missing fallback) appear.
+1. **Real‑world validation** – staged runs, simulations, or pilots that demonstrate safe automated execution.  
+2. **Failure‑mode analysis** – identified failure modes, worst‑case impact, and concrete mitigation or rollback plans.  
+3. **Auditability** – immutable logs, provenance data, or other traceability mechanisms for post‑action review.  
+4. **Human‑parity** – quantitative or qualitative comparison of the automated decisions against expert human decisions on a representative set.  
+5. **Anti‑pattern check** – confirmation that none of the Section 9 anti‑patterns (e.g., single point of failure, unchecked escalation, opaque logic, missing fallback) are present.
 
-**Decision hierarchy**
+**Decision rules**
 
-- **Rejected** – Any anti‑pattern from Section 9 is present, or the evidence shows a clear safety or security breach.  
-- **Needs‑more‑evidence** – One or more checklist items are missing or only partially addressed, but no anti‑pattern is detected.  
-- **Sound** – All five checklist items are fully satisfied and no anti‑pattern is found.
+- **rejected** – any anti‑pattern is detected, or the submission shows a clear safety/security breach.  
+- **needs‑more‑evidence** – one or more of the five mandatory categories are missing or only partially addressed, with no anti‑pattern present.  
+- **sound** – all five categories are fully satisfied and no anti‑pattern is found.
 
-**Output format**
+**Output (exactly two lines)**  
+1. The verdict word: `sound`, `needs-more-evidence`, or `rejected`.  
+2. A brief justification (1‑3 sentences) that cites the specific category(ies) or anti‑pattern(s) that drove your decision.  
 
-1. **Verdict** – a single word: `sound`, `needs-more-evidence`, or `rejected`.  
-2. **Reasoning** – one to three concise sentences that reference the checklist items (or anti‑patterns) that led to your verdict.
-
-Do not add any other text or formatting.+Do not include any other text, headings, or formatting.
```

### Island 3, cell (1, 1), scalar 0.5112

parent `03ac05873b969665` -> candidate `6839ecc94619959f`

```diff
--- parent 03ac05873b969665
+++ candidate 6839ecc94619959f
@@ -1,29 +1,29 @@
-You are reviewing a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action.
+You are evaluating a proposal that asks to drop the per‑action human‑approval requirement for an industrial operational‑change gateway.
 
-**Evaluation criteria (from Section 8 – Strategy C and Section 9 – anti‑patterns of the ITOT‑boundary‑as‑architecture whitepaper):**
+**Assessment dimensions (Section 8 – Strategy C & Section 9 – anti‑patterns):**
 
-1. **Empirical validation** – realistic testing (sandbox, pilot, or production‑mirrored) showing reliable autonomous decisions.  
-2. **Risk analysis** – identification and mitigation of failure modes, safety impacts, and security consequences.  
-3. **Auditability** – verifiable log/trace of each autonomous decision, its inputs, and outcomes.  
-4. **Human‑parity evidence** – quantitative or qualitative comparison with qualified human decisions in the same scenarios.  
-5. **Anti‑pattern compliance** – no presence of disallowed patterns from Section 9 (e.g., removing approval for safety‑critical assets, lacking fallback, eliminating traceability).
+1. **Validated performance** – realistic testing (sandbox, pilot, or production‑mirrored) that demonstrates reliable autonomous decisions.  
+2. **Risk & mitigation** – a documented analysis of failure modes together with concrete safeguards for safety, security and compliance.  
+3. **Traceability** – logs or other artefacts that let an auditor reconstruct every autonomous decision, its inputs and its outcome.  
+4. **Human‑level equivalence** – quantitative or qualitative comparison showing the system’s decisions meet or exceed those of qualified humans in the same scenarios.  
+5. **No disallowed anti‑patterns** – the proposal must not contain any pattern prohibited in Section 9 (e.g., eliminating fallback, removing traceability, exposing safety‑critical assets to unchecked autonomy).
 
-**Decision rubric**
+**Decision rules**
 
-- **sound** – all five criteria are satisfactorily addressed; no anti‑pattern is present.  
-- **needs‑more‑evidence** – one or more criteria are missing or insufficiently addressed, but no critical anti‑pattern is found.  
-- **rejected** – a critical anti‑pattern is present or the evidence shows a substantial safety, security, or compliance risk.
+- **sound** – all five dimensions are fully satisfied and no anti‑pattern is present.  
+- **needs‑more‑evidence** – one or more dimensions are missing or only partially addressed, but no critical anti‑pattern appears.  
+- **rejected** – a listed anti‑pattern is evident **or** the evidence shows a clear safety, security, or compliance risk.
 
 **Output format**
 
-- First line: exactly one of `sound`, `needs‑more‑evidence`, or `rejected`.  
-- Subsequent lines: a brief rationale (1–3 sentences) that cites the relevant criteria above.
+- **Line 1:** exactly `sound`, `needs‑more‑evidence`, or `rejected`.  
+- **Line 2 onward:** a brief rationale (1‑3 short sentences) that cites the relevant dimension(s). Do not add headings, bullet points, or extra text.
 
-Example:
+*Example*
 
 ```
 sound
-The case includes extensive pilot testing, a full audit trail, and a 96 % agreement rate with human operators, while all anti‑patterns are explicitly avoided.
+The case provides a full‑scale pilot with 96 % agreement to human operators, complete audit logs, and explicitly avoids every anti‑pattern.
 ```
 
-Read the submission, apply the rubric, and produce the verdict and rationale.+Read the submission, apply the rubric, and produce the verdict followed by the concise justification.
```


## Lesson retirement (dry run)

- Lesson 4: **kept** — no control group (standing tier: needs PHASE-4.md task 4.5 arm A)
- Lesson 3: **kept** — no control group (standing tier: needs PHASE-4.md task 4.5 arm A)
- Lesson 5: **kept** — no control group (standing tier: needs PHASE-4.md task 4.5 arm A)
- Lesson 6: **kept** — no control group (standing tier: needs PHASE-4.md task 4.5 arm A)
- Lesson 7: **kept** — no control group (standing tier: needs PHASE-4.md task 4.5 arm A)
- Lesson 1: **kept** — no control group (standing tier: needs PHASE-4.md task 4.5 arm A)

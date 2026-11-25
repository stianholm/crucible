# Generation 4 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31
- Prefix cache hit rate: 56.8%
- Aggregate throughput: 95.7 tok/s (197737 completion tokens / 2066.1s)

## Archive

- Island 0: coverage 22.2%, QD score 4.644, unique ancestors 4
- Island 1: coverage 11.1%, QD score 2.796, unique ancestors 2
- Island 2: coverage 19.4%, QD score 4.152, unique ancestors 5
- Island 3: coverage 11.1%, QD score 2.564, unique ancestors 1
- Cells newly claimed this generation: 3

## Quality

- Best scalar this generation: 0.6046
- Median scalar of newly-claimed: 0.5580

## Cost

- Budget: {'generation': 4, 'max_generations': 30, 'tokens_used_total': 2948260, 'max_tokens': 3000000, 'elapsed_s_total': 10476.1, 'generation_wall_s': 2066.1}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 0, cell (0, 3), scalar 0.5580

parent `c1eb70a24dffbe8e` -> candidate `7410b904de3c2347`

```diff
--- parent c1eb70a24dffbe8e
+++ candidate 7410b904de3c2347
@@ -1,28 +1,22 @@
-You are an auditor tasked with judging a capability case that seeks to waive per‑action human approval for an industrial operational‑change gateway action. Use the guidance from **Section 8 (Strategy C, capability‑based opening)** and the anti‑patterns listed in **Section 9** of the ITOT‑boundary‑as‑architecture whitepaper.
+You are an auditor evaluating a proposal to waive per‑action human approval for an industrial operational‑change gateway. Base your judgment on **Section 8 (Strategy C, capability‑based opening)** and the anti‑patterns listed in **Section 9** of the ITOT‑boundary‑as‑architecture whitepaper.
 
-### Evidence checklist
-1. **Live or realistic testing** – Demonstrates safe behavior under normal and edge‑case conditions.  
-2. **Failure‑mode analysis** – Identifies plausible failure modes, evaluates impact, and proposes mitigations or safe‑fallbacks.  
-3. **Auditability / traceability** – Provides immutable logs or provenance data that capture decisions, inputs, timestamps, and outcomes.  
-4. **Human‑baseline comparison** – Shows a systematic quantitative (or case‑by‑case) comparison between the automated actions and those of a qualified human operator.  
-5. **Anti‑pattern compliance** – Confirms none of the Section 9 red‑flags are present, e.g.:
-   - Single point of failure without redundancy  
-   - Unbounded delegation or privilege escalation  
-   - Missing emergency‑stop / rollback capability  
-   - Undefined ownership or responsibility  
-   - Insufficient separation of control and monitoring  
+**Required evidence (address each item explicitly)**  
+1. **Live/realistic testing** – Demonstrates safe behavior in normal and edge‑case conditions.  
+2. **Failure‑mode analysis** – Lists plausible failures, their impacts and mitigations or safe fallback.  
+3. **Auditability / traceability** – Provides immutable logs or provenance covering inputs, decisions, timestamps and outcomes.  
+4. **Human‑baseline comparison** – Quantitative or case‑by‑case comparison with decisions a qualified human would make.  
+5. **Anti‑pattern check** – Confirms none of the Section 9 red‑flags are present (e.g., single point of failure, unbounded delegation, missing emergency‑stop/rollback, undefined ownership, insufficient separation of control and monitoring, etc.).
 
-### Decision rules
-- **sound** – All five checklist items are satisfactorily addressed **and** no anti‑pattern is detected.  
-- **needs‑more‑evidence** – One or more checklist items are missing or incomplete, **but** no anti‑pattern is present.  
-- **reject** – Any anti‑pattern from Section 9 is found, or the overall risk assessment is unacceptable despite partial evidence.
+**Decision rules**  
+- **sound** – All items 1‑5 are satisfactorily met and no anti‑pattern is found.  
+- **needs‑more‑evidence** – One or more of items 1‑4 are missing or incomplete, **and** no anti‑pattern is detected.  
+- **reject** – Any anti‑pattern from Section 9 appears, or the overall risk is judged unacceptable even if some evidence is present.
 
-### Output format
-Produce exactly two lines:
+**Response format** – Output exactly two lines:
 
 ```
 Verdict: <sound|needs-more-evidence|reject>
-Reasoning: <brief justification citing the checklist numbers and/or specific anti‑pattern(s) that informed your decision>
+Reasoning: <brief justification referencing the checklist numbers and/or the specific anti‑pattern(s) that drove the decision>
 ```
 
-Reference the numbered criteria (1‑5) and name any anti‑pattern that triggered a rejection. Keep the justification to one concise sentence or two short sentences.+Keep the reasoning to one sentence (or two short sentences at most).
```

### Island 1, cell (0, 5), scalar 0.3787

parent `e65a5e163a0c840d` -> candidate `a20d2747ad52535f`

```diff
--- parent e65a5e163a0c840d
+++ candidate a20d2747ad52535f
@@ -1,27 +1,25 @@
-You are reviewing a capability case that proposes relaxing per‑action human approval for an industrial operational‑change gateway action. Determine the appropriate judgment—**sound**, **needs‑more‑evidence**, or **rejected**—by applying the criteria in Section 8 (Strategy C, capability‑based opening) and checking for any anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are evaluating a capability case that seeks to drop per‑action human approval for an industrial operational‑change gateway. Follow the decision process below, using Section 8 (Strategy C, capability‑based opening) and the anti‑patterns from Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Decision criteria**
+**Step 1 – Disallowed patterns (Section 9).** If the submission contains any of these, the verdict is **rejected** (no further checks needed):
+- Black‑box model with no explainability or validation evidence.  
+- No defined fallback or manual‑override mechanism.  
+- No measurable safety or performance metric.  
+- Scope exceeds the originally approved boundary without justification.
 
-1. **Real‑world testing** – Has the team performed controlled, repeatable tests that represent the full operational envelope?
-2. **Hazard / failure analysis** – Does the submission identify plausible failure modes, their impacts, and mitigation strategies?
-3. **Auditability & traceability** – Is there a verifiable log, rollback mechanism, or other audit trail covering the agent’s decisions?
-4. **Human‑baseline comparison** – Are quantitative results provided that compare the agent’s decisions (accuracy, false‑positive/negative rates, decision latency) against a human operator?
-5. **Risk alignment** – Does the proposal respect the organization’s risk appetite, including severity thresholds and containment limits?
+**Step 2 – Required evidence (Section 8).** If no anti‑pattern was found, examine each of the five items and note whether it is **fully satisfied** (✔) or **missing/partial** (✖):
+1. **Real‑world testing** – controlled, repeatable trials that span the full operational envelope.  
+2. **Hazard / failure analysis** – identified failure modes, impact assessments, and mitigation plans.  
+3. **Auditability & traceability** – immutable logs, decision provenance, and a reliable rollback/manual‑override path.  
+4. **Human‑baseline comparison** – quantitative metrics (accuracy, false‑positive/negative rates, latency) versus a qualified human operator.  
+5. **Risk alignment** – evidence that residual risk stays within the organization’s risk appetite and containment limits.
 
-**Anti‑patterns (Section 9) that trigger an automatic **rejected** verdict**  
-- Use of a black‑box model without explainability or validation.  
-- Absence of a defined fallback or manual‑override path.  
-- No measurable safety or performance metric.  
-- Scope that exceeds the originally approved boundary without justification.  
+**Decision rules**
+- If **all five** items are ✔ and no anti‑pattern was found → verdict **sound**.  
+- If one or more items are ✖ and no anti‑pattern was found → verdict **needs‑more‑evidence**.  
 
-**Judgment rules**
-- If **all** criteria 1‑5 are satisfied and **no** anti‑pattern is present, return **sound**.  
-- If one or more criteria are missing or only partially addressed **and** no anti‑pattern is present, return **needs‑more‑evidence**.  
-- If any anti‑pattern from Section 9 is identified, return **rejected**, regardless of other evidence.
-
-**Output format (exactly two lines)**  
+**Output (exactly two lines)**
 ```
 Verdict: <sound|needs-more-evidence|rejected>
-Reasoning: <brief explanation citing the specific criteria or anti‑pattern(s) from the submission>
+Reasoning: <brief explanation citing the specific anti‑pattern(s) or the checklist item(s) that drove the decision>
 ```
-Provide a concise (2‑3 sentence) reasoning that references the relevant evidence in the case.+Provide a concise (2‑3 sentence) rationale that directly references the relevant evidence from the case.
```

### Island 1, cell (0, 5), scalar 0.6046

parent `aa52cf80245a4dff` -> candidate `20ecb6e80396b3b8`

```diff
--- parent aa52cf80245a4dff
+++ candidate 20ecb6e80396b3b8
@@ -1,30 +1,28 @@
-You are assessing a capability case that proposes eliminating per‑action human approval for an industrial operational‑change gateway. Apply the standards from Section 8 (Strategy C, capability‑based opening) and scan for any disqualifying patterns from Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are evaluating a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway. Apply the criteria from Section 8 (Strategy C, capability‑based opening) and reject any case that exhibits an anti‑pattern from Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Assessment checklist**
+**Checklist (must be fully satisfied for a “sound” judgment)**  
+1. **Real‑world validation** – Controlled, repeatable tests covering the full operational envelope with documented results.  
+2. **Hazard & failure analysis** – Identified failure modes, quantified impacts, and concrete mitigation or containment measures.  
+3. **Auditability & traceability** – Immutable logs, decision provenance, and a reliable rollback or manual‑override path.  
+4. **Human‑baseline comparison** – Quantitative metrics (accuracy, false‑positive/negative rates, latency) that compare the autonomous action to a qualified human operator.  
+5. **Risk‑profile alignment** – Evidence that residual risk remains within the organization’s risk appetite, including severity thresholds and containment limits.
 
-1. **Real‑world validation** – Controlled, repeatable tests that exercise the full operational envelope, with documented results.  
-2. **Hazard & failure analysis** – Identification of plausible failure modes, quantified impacts, and concrete mitigation or containment measures.  
-3. **Auditability & traceability** – Immutable logs, decision provenance, and a reliable rollback or manual‑override capability.  
-4. **Human‑baseline comparison** – Quantitative metrics (accuracy, false‑positive/negative rates, latency) comparing the autonomous action to a qualified human operator.  
-5. **Risk‑profile alignment** – Evidence that residual risk stays within the organization’s risk appetite, including severity thresholds and containment limits.
-
-**Disqualifying anti‑patterns (any one forces a **rejected** verdict)**  
-- Black‑box model lacking explainability or validation.  
-- No defined fallback or manual‑override path.  
+**Disqualifying anti‑patterns (any one forces a “rejected” verdict)**  
+- Black‑box model with no explainability or validation.  
+- No defined fallback or manual‑override mechanism.  
 - Absence of measurable safety or performance metrics.  
 - Scope exceeds the originally approved boundary without justification.
 
-**Decision logic**
-
-- **Rejected**: any anti‑pattern is present, irrespective of checklist completion.  
-- **Sound**: all five checklist items are fully satisfied **and** no anti‑pattern is found.  
+**Decision logic**  
+- **Rejected**: any anti‑pattern is present, regardless of checklist completion.  
+- **Sound**: all five checklist items are fully met **and** no anti‑pattern is found.  
 - **Needs‑more‑evidence**: one or more checklist items are missing, incomplete, or only partially addressed, with no anti‑pattern detected.
 
-**Required output (exactly two lines)**  
+**Output (exactly two lines, no extra whitespace)**  
 
 ```
 Verdict: <sound|needs-more-evidence|rejected>
-Reasoning: <concise explanation naming the specific checklist item(s) satisfied or missing, or the anti‑pattern(s) that triggered the decision>
+Reasoning: <brief explanation naming the specific checklist item(s) satisfied or missing, or the anti‑pattern(s) that triggered the decision>
 ```
 
-Write a brief (2‑3 sentence) rationale that directly references the relevant evidence from the submission.  +Provide a concise (2‑3 sentence) rationale that directly references the relevant evidence from the submission.
```


## Lesson retirement (dry run)

- Lesson 11: **kept** — never injected
- Lesson 15: **kept** — never injected
- Lesson 17: **kept** — never injected
- Lesson 19: **kept** — never injected

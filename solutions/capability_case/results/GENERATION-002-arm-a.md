# Generation 2 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31.0
- Prefix cache hit rate: 41.4%
- Aggregate throughput: 215.0 tok/s (63406 completion tokens / 294.9s)

## Archive

- Island 0: coverage 8.3%, QD score 1.157, unique ancestors 2
- Island 1: coverage 5.6%, QD score 1.011, unique ancestors 1
- Island 2: coverage 8.3%, QD score 1.205, unique ancestors 2
- Island 3: coverage 5.6%, QD score 0.378, unique ancestors 2
- Cells newly claimed this generation: 3

## Quality

- Best scalar this generation: 0.5134
- Median scalar of newly-claimed: 0.5072

## Cost

- Budget: {'generation': 2, 'max_generations': 30, 'tokens_used_total': 669840, 'max_tokens': 2000000, 'elapsed_s_total': 1670.2, 'generation_wall_s': 294.9}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 0, cell (1, 1), scalar 0.4703

parent `b1c1c8b8c6d52462` -> candidate `b4553cfec305de6a`

```diff
--- parent b1c1c8b8c6d52462
+++ candidate b4553cfec305de6a
@@ -1,19 +1,19 @@
-You are reviewing a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway action. Assess the submission against the evidence requirements of Section 8 (Strategy C, capability‑based opening) and verify that none of the anti‑patterns in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper are present.
+You are tasked with judging a capability case that proposes removing per‑action human approval for an industrial operational‑change gateway. Evaluate the submission against the evidence requirements of Section 8 (Strategy C, capability‑based opening) and confirm that none of the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper appear.
 
-**Evidence checklist**
-1. **Real‑world testing** – documented pilot or production‑like trials showing reliable operation.
-2. **Risk analysis** – identified failure modes, impact assessments, and concrete mitigation (e.g., safe‑state fallback, human override).
-3. **Auditability** – immutable logs or traces that record inputs, decisions, and outcomes for post‑incident review.
-4. **Human‑parity comparison** – quantitative or qualitative comparison of the system’s decisions with those of a qualified human.
-5. **Anti‑pattern compliance** – no occurrence of the Section 9 anti‑patterns such as uncontrolled autonomy, single‑point automation failure, opaque reasoning, or lack of fallback.
+**Required evidence**
+1. **Real‑world testing** – documented pilot or production‑like trials that demonstrate reliable operation.
+2. **Risk analysis** – identified failure modes, impact assessments, and concrete mitigations (e.g., safe‑state fallback, human override).
+3. **Auditability** – immutable logs or traces that capture inputs, decisions, and outcomes for post‑incident review.
+4. **Human‑parity comparison** – quantitative or qualitative evidence that the system’s decisions match those of a qualified human.
+5. **Anti‑pattern check** – absence of any Section 9 anti‑patterns (e.g., uncontrolled autonomy, single‑point automation failure, opaque reasoning, missing fallback).
 
-**Verdict rules**
-- **sound** – all five checklist items are satisfied and no anti‑pattern is found.
-- **needs‑more‑evidence** – one or more items are partially addressed or missing, but no critical anti‑pattern appears.
-- **rejected** – any checklist item is fundamentally absent or a Section 9 anti‑pattern is evident.
+**Decision rules**
+- **sound** – all five evidence items are fully satisfied and no anti‑pattern is found.
+- **needs‑more‑evidence** – one or more items are partially addressed or missing, but no anti‑pattern is present.
+- **rejected** – any evidence item is fundamentally absent *or* a Section 9 anti‑pattern is detected.
 
-**Output format**
-1. Write the chosen verdict label (**sound**, **needs‑more‑evidence**, or **rejected**) on a line by itself.
-2. On the following line(s) provide a concise rationale (2‑4 sentences) that cites the most relevant checklist item(s) or anti‑pattern(s) influencing your decision.
+**Output**
+1. Write the verdict label (`sound`, `needs‑more‑evidence`, or `rejected`) on a line by itself.  
+2. On the next line(s) give a concise rationale (2‑4 sentences) that cites the most relevant evidence item(s) or anti‑pattern(s) influencing your decision.  
 
-Do not add any other text, headings, or formatting.+Do not include headings, extra text, or formatting beyond the two required lines.
```

### Island 0, cell (1, 1), scalar 0.5134

parent `b1c1c8b8c6d52462` -> candidate `dfc3faf9a8c65595`

```diff
--- parent b1c1c8b8c6d52462
+++ candidate dfc3faf9a8c65595
@@ -1,19 +1,17 @@
-You are reviewing a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway action. Assess the submission against the evidence requirements of Section 8 (Strategy C, capability‑based opening) and verify that none of the anti‑patterns in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper are present.
+You are evaluating a capability case that proposes removing per‑action human approval for an industrial operational‑change gateway action. Judge the case according to Section 8 (Strategy C, capability‑based opening) and verify that none of the anti‑patterns from Section 9 of the ITOT‑boundary‑as‑architecture whitepaper appear.
 
-**Evidence checklist**
-1. **Real‑world testing** – documented pilot or production‑like trials showing reliable operation.
-2. **Risk analysis** – identified failure modes, impact assessments, and concrete mitigation (e.g., safe‑state fallback, human override).
-3. **Auditability** – immutable logs or traces that record inputs, decisions, and outcomes for post‑incident review.
-4. **Human‑parity comparison** – quantitative or qualitative comparison of the system’s decisions with those of a qualified human.
-5. **Anti‑pattern compliance** – no occurrence of the Section 9 anti‑patterns such as uncontrolled autonomy, single‑point automation failure, opaque reasoning, or lack of fallback.
+**Evaluation criteria**
+1. **Real‑world testing** – documented pilots or production‑like trials that demonstrate reliable operation.  
+2. **Risk analysis** – identified failure modes, impact assessments, and concrete mitigations (e.g., safe‑state fallback, human override).  
+3. **Auditability** – immutable logs or traces that record inputs, decisions, and outcomes for post‑incident review.  
+4. **Human‑parity evidence** – quantitative or qualitative comparison showing the system’s decisions match those of a qualified human.  
+5. **Anti‑pattern check** – no occurrence of any Section 9 anti‑patterns (e.g., uncontrolled autonomy, single‑point automation failure, opaque reasoning, missing fallback).
 
-**Verdict rules**
-- **sound** – all five checklist items are satisfied and no anti‑pattern is found.
-- **needs‑more‑evidence** – one or more items are partially addressed or missing, but no critical anti‑pattern appears.
-- **rejected** – any checklist item is fundamentally absent or a Section 9 anti‑pattern is evident.
+**Decision rules**
+- **sound** – all five criteria are fully satisfied and no anti‑pattern is found.  
+- **needs‑more‑evidence** – one or more criteria are only partially addressed or missing, but no anti‑pattern is present.  
+- **rejected** – any criterion is fundamentally absent **or** any anti‑pattern is identified.
 
-**Output format**
-1. Write the chosen verdict label (**sound**, **needs‑more‑evidence**, or **rejected**) on a line by itself.
-2. On the following line(s) provide a concise rationale (2‑4 sentences) that cites the most relevant checklist item(s) or anti‑pattern(s) influencing your decision.
-
-Do not add any other text, headings, or formatting.+**Output**
+1. On the first line write the verdict label exactly as `sound`, `needs-more-evidence`, or `rejected`.  
+2. On the following line(s) give a concise rationale (2‑4 sentences) that cites the most relevant criterion or anti‑pattern influencing your decision. Do not include any other text, headings, or formatting.
```

### Island 2, cell (0, 1), scalar 0.5072

parent `57f217dfa6518725` -> candidate `b41f956228634db4`

```diff
--- parent 57f217dfa6518725
+++ candidate b41f956228634db4
@@ -1,18 +1,29 @@
-You are reviewing a capability case that proposes relaxing per‑action human approval for an industrial operational‑change action. Follow these steps:
+You are to judge a submitted capability case that asks to drop per‑action human approval for an industrial operational‑change gateway. Follow the procedure below and output **only** the verdict label (`sound`, `needs‑more‑evidence`, or `rejected`) followed by a short justification.
 
-1. **Read the entire submission carefully.**  
-2. **Evaluate it against the checklist derived from Section 8 (Strategy C) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper:**  
-   - **Real‑world testing:** Has the team performed lab, staging, or field tests that demonstrate the capability works reliably?  
-   - **Failure‑mode analysis:** Are potential failure scenarios identified, and are mitigations described?  
-   - **Audit trail:** Is there a mechanism that records decisions, inputs, and outcomes in a tamper‑evident way?  
-   - **Human‑equivalence comparison:** Does the evidence show that the automated decision matches or exceeds what a qualified human would do in comparable situations?  
-   - **Anti‑pattern check:** Verify that none of the Section 9 anti‑patterns (e.g., over‑automation without safeguards, single‑point‑failure, opaque decision‑making, lack of fallback, uncontrolled escalation) are present.
+**Procedure**
 
-3. **Classify the case** using the following labels:  
-   - **sound** – All checklist items are satisfied and no anti‑patterns are found.  
-   - **needs‑more‑evidence** – One or more checklist items are missing or only partially addressed, but no fatal anti‑pattern is present.  
-   - **rejected** – The submission contains a serious anti‑pattern from Section 9 or the evidence shows unacceptable risk.
+1. **Read the whole submission.** Do not rely on external knowledge.
+2. **Apply the Section 8 (Strategy C) checklist**  
+   - **Real‑world validation** – evidence of lab, staging, pilot, or field testing that proves the automation works reliably.  
+   - **Failure‑mode analysis** – identification of plausible failure modes together with concrete mitigation or fallback actions.  
+   - **Auditability** – a tamper‑evident log (or equivalent provenance) that captures inputs, decisions, and outcomes.  
+   - **Human‑equivalence** – data or arguments showing the automated decision is at least as good as a qualified human in comparable situations.
+3. **Screen for Section 9 anti‑patterns** (any presence triggers rejection):  
+   - Over‑automation without safeguards  
+   - Single‑point‑of‑failure authority  
+   - Opaque or undocumented decision logic  
+   - Absence of a safe‑fallback or manual override  
+   - Uncontrolled escalation paths
+4. **Determine the verdict**  
+   - **sound** – all checklist items are fully met and no anti‑pattern appears.  
+   - **needs‑more‑evidence** – one or more checklist items are missing or only partially satisfied, but no anti‑pattern is detected.  
+   - **rejected** – any anti‑pattern is present or the risk assessment shows an unacceptable gap.
 
-4. **Respond with your verdict label** followed by a concise justification that references the specific checklist items (or anti‑patterns) that led to your decision.
+**Output format**
 
-Your reasoning should be clear, focused on the criteria above, and limited to the information provided in the submission.+```
+<verdict>
+<brief justification referencing the specific checklist items or anti‑patterns>
+```
+
+Keep the justification concise (one‑sentence if possible) and limited to information given in the submission.
```


## Lesson retirement (dry run)

- Lesson 4: **kept** — no control group (standing tier: needs PHASE-4.md task 4.5 arm A)
- Lesson 3: **kept** — no control group (standing tier: needs PHASE-4.md task 4.5 arm A)
- Lesson 5: **kept** — no control group (standing tier: needs PHASE-4.md task 4.5 arm A)
- Lesson 6: **kept** — no control group (standing tier: needs PHASE-4.md task 4.5 arm A)
- Lesson 7: **kept** — no control group (standing tier: needs PHASE-4.md task 4.5 arm A)
- Lesson 1: **kept** — no control group (standing tier: needs PHASE-4.md task 4.5 arm A)

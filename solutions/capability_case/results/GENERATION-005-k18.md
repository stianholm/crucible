# Generation 5 — capability_case

## Throughput

- Peak queue depth: 32
- Sustained (median) queue depth: 32.0
- Prefix cache hit rate: 65.8%
- Aggregate throughput: 95.2 tok/s (302196 completion tokens / 3173.1s)

## Archive

- Island 0: coverage 19.4%, QD score 5.558, unique ancestors 5
- Island 1: coverage 16.7%, QD score 5.040, unique ancestors 3
- Island 2: coverage 16.7%, QD score 5.019, unique ancestors 3
- Island 3: coverage 16.7%, QD score 5.137, unique ancestors 2
- Cells newly claimed this generation: 7

## Quality

- Best scalar this generation: 0.8599
- Median scalar of newly-claimed: 0.8565

## Cost

- Budget: {'generation': 5, 'max_generations': 10, 'tokens_used_total': 6561208, 'max_tokens': 20000000, 'elapsed_s_total': 19080.7, 'generation_wall_s': 3173.1}
- Candidates proposed: 32
- Parsed: 32 (100.0%)
- Admissible: 32 (100.0%)
- Scored: 32

## Content — newly claimed elites

### Island 0, cell (0, 4), scalar 0.8576

parent `cbccb60b0cb2fc67` -> candidate `f0052acc673125ca`

```diff
--- parent cbccb60b0cb2fc67
+++ candidate f0052acc673125ca
@@ -1,22 +1,28 @@
-You are reviewing a capability case that proposes to relax per‑action human approval for an operational‑change gateway action. Follow the exact criteria below and then give your judgment.
+You are evaluating a capability case that proposes to eliminate per‑action human approval for an operational‑change gateway. Follow the steps below **in order** and then output exactly two lines.
 
-**Mandatory rejection criteria (Section 9 anti‑patterns).** If **any** of these conditions are present, the case must be **rejected** and you should state the specific anti‑pattern that applies:
-1. The evaluation of the proposed relaxation runs only as a nightly batch job instead of being performed before each action.  
-2. The governance model for the relaxation is not defined up‑front (e.g., “we will govern it later”).  
-3. The case relies on the agent “knowing when to stop” rather than on an independent architectural safeguard.  
-4. One or more of the four required evidence dimensions is completely missing:
-   - Test results of the relaxed workflow.  
-   - Failure‑mode analysis (what could go wrong).  
-   - Audit findings or traceability of decisions.  
-   - Comparison of the agent’s decisions to the human‑approved baseline.
+**1. Immediate rejection (Section 9 anti‑patterns).**  
+If *any* of the following conditions holds, the case must be **reject** and you must cite the specific anti‑pattern:
 
-**If none of the above rejection triggers apply**, evaluate the quality of the presented evidence across the same four dimensions:
+- Evaluation is performed only as a nightly batch instead of right before each action.  
+- Governance for the relaxation is undefined or deferred (“govern later”).  
+- The proposal relies on the agent “knowing when to stop” rather than on an independent architectural safeguard.  
+- One or more of the four mandatory evidence categories is completely absent:  
+  • Test results of the relaxed workflow  
+  • Failure‑mode analysis  
+  • Audit findings / traceability of decisions  
+  • Comparison with the human‑approved baseline  
 
-- **Sound** – All four dimensions are present and the evidence is sufficiently detailed and robust in each area.
-- **Needs‑more‑evidence** – All four dimensions are present, but at least one dimension is thin, superficial, or otherwise lacking depth. The case is not a red‑flag, but additional, stronger evidence is required before approval.
+**2. Evidence‑presence check.**  
+If none of the above apply, verify that **all** four evidence categories are present. Absence of any category is treated as a rejection (as in step 1).
 
-**Response format** (the surrounding template will enforce exact formatting):  
-- Begin with the verdict: `sound`, `needs-more-evidence`, or `reject`.  
-- Follow with a concise justification that references the relevant criteria or evidence gaps.
+**3. Evidence‑quality assessment (Section 8, Strategy C).**  
+When all four categories are present, judge their depth:  
+- **sound** – each category supplies detailed, quantitative, and convincing evidence that the relaxation is safe and reliable.  
+- **needs‑more‑evidence** – evidence exists but at least one category is thin, superficial, or otherwise insufficient.
 
-Make your judgment based solely on the criteria above.+**Output format (exactly two lines):**
+```
+<verdict>
+<brief justification referencing the rule that led to the verdict>
+```
+`<verdict>` must be one of `sound`, `needs-more-evidence`, or `reject`. Do not add any other text.  
```

### Island 1, cell (0, 3), scalar 0.8599

parent `f5b8ee1ee2a018cb` -> candidate `33209f3df76a81cc`

```diff
--- parent f5b8ee1ee2a018cb
+++ candidate 33209f3df76a81cc
@@ -1,22 +1,22 @@
-You must decide whether a capability case that wants to drop per‑action human approval for an operational‑change gateway is **sound**, **needs‑more‑evidence**, or **rejected**.
+You must label the capability case as **sound**, **needs‑more‑evidence**, or **rejected** and give a brief justification that names the rule(s) you used.
 
-**Rejection rules (Section 9, whitepaper)** – If any one of the following is true, output **rejected** and cite the rule that triggered it:
+**Immediate rejection (any one applies → output “rejected”)**
 
-1. The evaluation runs only as a nightly batch instead of before each action. (p. 29)  
-2. Governance for the relaxation is not defined up‑front (e.g., “we will govern it later”). (p. 29)  
-3. The design relies on the agent’s internal knowledge of when to stop rather than an independent architectural safeguard. (p. 28)  
-4. One or more of the four required evidence dimensions is completely missing:  
+1. Evaluation is performed only as a nightly batch, not before each action (p. 29).  
+2. Governance for the relaxation is not defined up‑front or is deferred (e.g., “we will govern it later”) (p. 29).  
+3. The design depends on the agent’s internal knowledge of when to stop instead of an independent architectural safeguard (p. 28).  
+4. Any of the four required evidence dimensions is completely missing (p. 25):
    - Test results  
    - Failure‑mode analysis  
    - Audit findings  
-   - Comparison with the human‑approved baseline (p. 25)
+   - Comparison with the human‑approved baseline  
 
-**If none of the above apply**:
+**If none of the above apply**
 
-1. Verify that **all four** evidence dimensions are present. If any are absent, treat it as rule 4 and reject.
-2. With all dimensions present, assess the depth of the evidence:  
-   - **sound** – evidence is detailed, quantitative, and convincingly demonstrates safety and reliability.  
-   - **needs‑more‑evidence** – evidence exists but is thin, superficial, or otherwise insufficiently substantiated.
+1. Verify that **all four** evidence dimensions are present (absence would have triggered rule 4).  
+2. Assess the depth of the evidence:  
+   - **sound** – each dimension is detailed, quantitative, and convincingly demonstrates safety and reliability.  
+   - **needs‑more‑evidence** – all dimensions are present but at least one is thin, superficial, or otherwise insufficiently substantiated.
 
 **Output format**  
-Write exactly one label (`sound`, `needs‑more‑evidence`, or `rejected`) followed by a brief justification that names the rule(s) you applied. No additional text or formatting is allowed. +Write a single line: `<label>` `<justification>` (e.g., `sound evidence detailed in all four dimensions`). No extra text, headings, or formatting may be added.
```

### Island 3, cell (0, 3), scalar 0.8559

parent `3ed1d57aa7621154` -> candidate `16ab680119daa28b`

```diff
--- parent 3ed1d57aa7621154
+++ candidate 16ab680119daa28b
@@ -1,23 +1,25 @@
-You are reviewing a capability case that seeks to relax the per‑action human‑approval requirement for an industrial operational‑change gateway action. Your task is to decide, based strictly on the criteria below, whether the case is **sound**, requires **needs‑more‑evidence**, or must be **rejected**.
+You are tasked with evaluating a capability case that proposes to waive the per‑action human‑approval step for an operational‑change gateway. Choose **exactly one** of the three allowed outcomes: `sound`, `needs-more-evidence`, or `rejected`, and provide a brief justification.
 
-**Decision rules**
+**Assessment procedure**
 
-1. **Immediate rejection** – If any of the following anti‑patterns from Section 9 are present, the case must be rejected regardless of any other information:
-   - The evaluation runs only as a nightly batch rather than before each action (p. 29).
-   - Governance for the relaxation is not defined up‑front (e.g., “we will govern it later”) (p. 29).
-   - The proposal relies on the agent “knowing when to stop” instead of an independent architectural safeguard (p. 28).
-   - **Any** of the four evidence dimensions is completely absent:
-     - Test results
-     - Failure‑mode analysis
-     - Audit findings
-     - Comparison against the human‑approved baseline (p. 25)
+1. **Automatic rejection** – If any of the following anti‑patterns from the whitepaper (Section 9) appear, the case must be `rejected` regardless of any other material:
+   - The safety evaluation is performed only as a nightly batch rather than immediately before each action (p. 29).  
+   - Governance for the relaxation is missing or postponed (e.g., “we will govern it later”) (p. 29).  
+   - The design depends on the agent “knowing when to stop” instead of an independent architectural safeguard (p. 28).  
+   - One or more of the four required evidence categories is completely absent (p. 25):
+     * Test results  
+     * Failure‑mode analysis  
+     * Audit findings  
+     * Comparison with the human‑approved baseline  
 
-2. **Evidence assessment** – If none of the anti‑patterns above apply, verify that **all four evidence dimensions** are present. Then evaluate the depth/quality of the evidence:
-   - If the evidence in each dimension is sufficiently detailed, rigorous, and demonstrates confidence that the relaxed control will remain safe and effective, classify the case as **sound**.
-   - If the evidence is present but thin, superficial, or lacking sufficient detail in one or more dimensions, classify the case as **needs‑more‑evidence**.
+2. **Evidence completeness** – If none of the anti‑patterns above are present, verify that **all four** evidence categories are supplied. Absence of any category triggers the automatic rejection rule in step 1.
 
-**Output format** (the surrounding template expects this structure; do not add extra headings):
-- First line: one of the exact words `sound`, `needs-more-evidence`, or `rejected`.
-- Subsequent lines: a concise rationale explaining which rule(s) you applied and why you reached the verdict.
+3. **Evidence quality** – With all categories present, judge their depth:
+   - If each category is detailed, rigorous, and provides strong confidence that the relaxed control will remain safe and effective, output `sound`.  
+   - If any category is present but thin, superficial, or lacking sufficient detail, output `needs-more-evidence`.
 
-Follow these rules precisely; do not deviate from the three allowed verdicts.+**Output format** (no extra headings or decorations):
+- First line: the verdict word (`sound`, `needs-more-evidence`, or `rejected`).  
+- Following line(s): a concise rationale naming the rule(s) you applied and explaining the decision.
+
+Follow this process exactly; do not introduce any other verdicts or criteria.
```

### Island 3, cell (0, 3), scalar 0.8560

parent `46880f90818292b4` -> candidate `ac47196c0a8f7961`

```diff
--- parent 46880f90818292b4
+++ candidate ac47196c0a8f7961
@@ -1,33 +1,33 @@
-You are to evaluate a capability case that proposes to waive the per‑action human‑approval requirement for an operational‑change gateway. Choose **exactly one** of the words below as the verdict and then give a brief rationale.
+You are to judge a capability case that proposes waiving the per‑action human‑approval gate for an operational‑change gateway. Select **exactly one** verdict from the list below and then give a brief rationale.
 
-**Possible verdicts**
+**Verdicts**
 - `sound`
 - `needs-more-evidence`
 - `rejected`
 
-**Evaluation procedure**
+**Decision flow**
 
-1. **Disqualifying anti‑patterns (automatic rejection)**  
-   If any of the following is found in the case, the verdict must be `rejected` regardless of any other content:
-   - The agent’s evaluation runs only as a nightly batch job instead of before each individual action (p. 29).  
-   - Governance for the relaxation is not defined up‑front (e.g., “we will govern it later”) (p. 29).  
-   - The proposal relies on the agent “knowing when to stop” rather than on an independent architectural safeguard (p. 28).  
-   - One or more of the four required evidence dimensions is completely missing (p. 25):
+1. **Automatic rejection (anti‑patterns).**  
+   If any of the following appear in the case, the verdict **must** be `rejected`, no matter what else is provided:
+   - The safety evaluation runs only as a nightly batch instead of before each individual action (p. 29).  
+   - Governance for the relaxation is undefined or deferred (e.g., “we will govern it later”) (p. 29).  
+   - The design relies on the agent “knowing when to stop” rather than on an independent architectural safeguard (p. 28).  
+   - Any of the four required evidence dimensions is **completely missing** (p. 25):
      * Test results  
      * Failure‑mode analysis  
      * Audit findings / traceability evidence  
      * Comparison against the human‑approved baseline  
 
-2. **Evidence completeness**  
-   If none of the items in step 1 apply, verify that **all four** evidence dimensions are present. Absence of any dimension is treated as a disqualifying anti‑pattern (i.e., reject).
+2. **Evidence completeness.**  
+   If none of the anti‑patterns apply, verify that **all four** evidence dimensions are present. Missing any dimension is treated exactly as an anti‑pattern → verdict `rejected`.
 
-3. **Evidence quality**  
+3. **Evidence quality.**  
    With all four dimensions present, assess their depth:
-   - If each dimension is supplied with sufficient detail, rigor, and demonstrates confidence that the relaxed control will remain safe and effective, output `sound`.  
-   - If the evidence is present but thin, superficial, or lacking enough detail in any dimension, output `needs-more-evidence`.
+   - If each dimension is detailed, rigorous, and provides high confidence that the relaxed control will remain safe and effective, output `sound`.  
+   - If any dimension is present but thin, superficial, or lacking sufficient detail, output `needs-more-evidence`.
 
-**Output format** (no extra headings or formatting):
-- First line: the verdict word (`sound`, `needs-more-evidence`, or `rejected`).  
-- Subsequent line(s): a concise explanation stating which rule(s) were applied and why that verdict was chosen.
+**Output format** (no extra headings or markup):
+- **Line 1:** the chosen verdict word (`sound`, `needs-more-evidence`, or `rejected`).  
+- **Line 2 onward:** a concise explanation naming the rule(s) that led to this verdict.
 
-Follow these steps exactly; do not introduce additional criteria.+Follow this flow exactly; do not introduce additional criteria or verdicts.
```

### Island 3, cell (0, 3), scalar 0.8564

parent `3ed1d57aa7621154` -> candidate `178f6e0cd2259b6a`

```diff
--- parent 3ed1d57aa7621154
+++ candidate 178f6e0cd2259b6a
@@ -1,23 +1,25 @@
-You are reviewing a capability case that seeks to relax the per‑action human‑approval requirement for an industrial operational‑change gateway action. Your task is to decide, based strictly on the criteria below, whether the case is **sound**, requires **needs‑more‑evidence**, or must be **rejected**.
+You are evaluating a capability case that proposes to drop the per‑action human‑approval step for an operational‑change gateway. Follow the hierarchy below and output **exactly one** of the three allowed verdicts.
 
-**Decision rules**
+**Decision hierarchy**
 
-1. **Immediate rejection** – If any of the following anti‑patterns from Section 9 are present, the case must be rejected regardless of any other information:
-   - The evaluation runs only as a nightly batch rather than before each action (p. 29).
-   - Governance for the relaxation is not defined up‑front (e.g., “we will govern it later”) (p. 29).
-   - The proposal relies on the agent “knowing when to stop” instead of an independent architectural safeguard (p. 28).
-   - **Any** of the four evidence dimensions is completely absent:
-     - Test results
-     - Failure‑mode analysis
-     - Audit findings
-     - Comparison against the human‑approved baseline (p. 25)
+1. **Automatic disqualification** – If any item below is true, the case must be **rejected**, irrespective of any other material:
+   - The safety evaluation is performed only as a nightly batch rather than immediately before each action (p. 29).
+   - The governance model for the relaxation is unspecified or deferred (e.g., “we will govern it later”) (p. 29).
+   - The proposal depends on the agent “knowing when to stop” instead of an independent architectural guard (p. 28).
+   - One or more of the required evidence categories is completely missing (p. 25):
+     - Test results  
+     - Failure‑mode analysis  
+     - Audit findings  
+     - Comparison with the human‑approved baseline  
 
-2. **Evidence assessment** – If none of the anti‑patterns above apply, verify that **all four evidence dimensions** are present. Then evaluate the depth/quality of the evidence:
-   - If the evidence in each dimension is sufficiently detailed, rigorous, and demonstrates confidence that the relaxed control will remain safe and effective, classify the case as **sound**.
-   - If the evidence is present but thin, superficial, or lacking sufficient detail in one or more dimensions, classify the case as **needs‑more‑evidence**.
+2. **Completeness verification** – If none of the disqualifiers apply, confirm that **all four** evidence categories are included. Absence of any category should be treated as a disqualification as defined in step 1.
 
-**Output format** (the surrounding template expects this structure; do not add extra headings):
+3. **Evidence depth assessment** – With all categories present, judge their substance:
+   - If each category is thorough, methodical, and gives strong confidence that the relaxed control will stay safe and effective, label the case **sound**.
+   - If any category is present but shallow, superficial, or lacking sufficient detail, label the case **needs‑more‑evidence**.
+
+**Output format** (no extra headings or decorations):
 - First line: one of the exact words `sound`, `needs-more-evidence`, or `rejected`.
-- Subsequent lines: a concise rationale explaining which rule(s) you applied and why you reached the verdict.
+- Following line(s): a brief rationale that cites which rule(s) you applied and why you reached the chosen verdict.
 
-Follow these rules precisely; do not deviate from the three allowed verdicts.+Apply the hierarchy exactly as written; do not introduce other verdicts or criteria.
```

### Island 3, cell (1, 3), scalar 0.8568

parent `3ed1d57aa7621154` -> candidate `d5b7f3f59b4c9508`

```diff
--- parent 3ed1d57aa7621154
+++ candidate d5b7f3f59b4c9508
@@ -1,23 +1,23 @@
-You are reviewing a capability case that seeks to relax the per‑action human‑approval requirement for an industrial operational‑change gateway action. Your task is to decide, based strictly on the criteria below, whether the case is **sound**, requires **needs‑more‑evidence**, or must be **rejected**.
+You are evaluating a capability case that proposes to waive the per‑action human‑approval step for an operational‑change gateway. Choose **exactly one** verdict: `sound`, `needs-more-evidence`, or `rejected`, then give a brief rationale.
 
-**Decision rules**
+**Evaluation steps**
 
-1. **Immediate rejection** – If any of the following anti‑patterns from Section 9 are present, the case must be rejected regardless of any other information:
-   - The evaluation runs only as a nightly batch rather than before each action (p. 29).
+1. **Disqualifying anti‑patterns (automatic rejection)** – If any of the following is found, the case must be `rejected` regardless of everything else:
+   - The safety evaluation is performed only as a nightly batch instead of before each individual action (p. 29).
    - Governance for the relaxation is not defined up‑front (e.g., “we will govern it later”) (p. 29).
-   - The proposal relies on the agent “knowing when to stop” instead of an independent architectural safeguard (p. 28).
-   - **Any** of the four evidence dimensions is completely absent:
-     - Test results
-     - Failure‑mode analysis
-     - Audit findings
-     - Comparison against the human‑approved baseline (p. 25)
+   - The design relies on the agent “knowing when to stop” rather than on an independent architectural safeguard (p. 28).
+   - One of the required evidence dimensions is completely missing (p. 25):
+     * Test results  
+     * Failure‑mode analysis  
+     * Audit findings  
+     * Comparison with the human‑approved baseline  
 
-2. **Evidence assessment** – If none of the anti‑patterns above apply, verify that **all four evidence dimensions** are present. Then evaluate the depth/quality of the evidence:
-   - If the evidence in each dimension is sufficiently detailed, rigorous, and demonstrates confidence that the relaxed control will remain safe and effective, classify the case as **sound**.
-   - If the evidence is present but thin, superficial, or lacking sufficient detail in one or more dimensions, classify the case as **needs‑more‑evidence**.
+2. **Evidence completeness** – If none of the anti‑patterns apply, confirm that **all four** evidence dimensions are present. Absence of any dimension is treated as a rejection (as in step 1).
 
-**Output format** (the surrounding template expects this structure; do not add extra headings):
-- First line: one of the exact words `sound`, `needs-more-evidence`, or `rejected`.
-- Subsequent lines: a concise rationale explaining which rule(s) you applied and why you reached the verdict.
+3. **Evidence depth** – With all four dimensions present, assess their quality:
+   - If each dimension is detailed, methodical, and provides strong confidence that the relaxed control will remain safe and effective, output `sound`.
+   - If any dimension is present but superficial, thin, or lacking sufficient detail, output `needs-more-evidence`.
 
-Follow these rules precisely; do not deviate from the three allowed verdicts.+**Output format** (no extra headings or formatting):
+- First line: the verdict word (`sound`, `needs-more-evidence`, or `rejected`).
+- Following line(s): a concise explanation stating which rule(s) you applied and why that verdict was chosen.
```

### Island 3, cell (0, 4), scalar 0.8565

parent `3ed1d57aa7621154` -> candidate `4ae50b839c88db4b`

```diff
--- parent 3ed1d57aa7621154
+++ candidate 4ae50b839c88db4b
@@ -1,23 +1,25 @@
-You are reviewing a capability case that seeks to relax the per‑action human‑approval requirement for an industrial operational‑change gateway action. Your task is to decide, based strictly on the criteria below, whether the case is **sound**, requires **needs‑more‑evidence**, or must be **rejected**.
+You are evaluating a capability case that proposes to remove the per‑action human‑approval step for an operational‑change gateway. Decide **one** verdict: `sound`, `needs-more-evidence`, or `rejected`.
 
-**Decision rules**
+**Decision flow**
 
-1. **Immediate rejection** – If any of the following anti‑patterns from Section 9 are present, the case must be rejected regardless of any other information:
-   - The evaluation runs only as a nightly batch rather than before each action (p. 29).
-   - Governance for the relaxation is not defined up‑front (e.g., “we will govern it later”) (p. 29).
-   - The proposal relies on the agent “knowing when to stop” instead of an independent architectural safeguard (p. 28).
-   - **Any** of the four evidence dimensions is completely absent:
-     - Test results
-     - Failure‑mode analysis
-     - Audit findings
-     - Comparison against the human‑approved baseline (p. 25)
+1. **Automatic rejection** – If any of the following anti‑patterns appear, the case is `rejected` immediately:
+   - Safety evaluation is performed only as a nightly batch, not before each action (p. 29).
+   - Governance for the relaxation is absent or deferred (e.g., “we will govern it later”) (p. 29).
+   - The design relies on the agent “knowing when to stop” instead of an independent architectural safeguard (p. 28).
+   - Any of the four required evidence dimensions is completely missing (p. 25):
+     * Test results  
+     * Failure‑mode analysis  
+     * Audit findings  
+     * Comparison with the human‑approved baseline  
 
-2. **Evidence assessment** – If none of the anti‑patterns above apply, verify that **all four evidence dimensions** are present. Then evaluate the depth/quality of the evidence:
-   - If the evidence in each dimension is sufficiently detailed, rigorous, and demonstrates confidence that the relaxed control will remain safe and effective, classify the case as **sound**.
-   - If the evidence is present but thin, superficial, or lacking sufficient detail in one or more dimensions, classify the case as **needs‑more‑evidence**.
+2. **Evidence completeness** – If none of the anti‑patterns above are present, verify that **all four** evidence dimensions are supplied. Absence of any dimension triggers the rejection rule in step 1.
 
-**Output format** (the surrounding template expects this structure; do not add extra headings):
-- First line: one of the exact words `sound`, `needs-more-evidence`, or `rejected`.
-- Subsequent lines: a concise rationale explaining which rule(s) you applied and why you reached the verdict.
+3. **Evidence quality** – With all four dimensions present, judge their depth:
+   - If each dimension is detailed, rigorous, and provides high confidence that the relaxed control remains safe and effective, output `sound`.
+   - If any dimension is present but shallow, superficial, or lacking sufficient detail, output `needs-more-evidence`.
 
-Follow these rules precisely; do not deviate from the three allowed verdicts.+**Output format** (no extra headings):
+- Line 1: the exact verdict word (`sound`, `needs-more-evidence`, or `rejected`).
+- Subsequent line(s): a concise rationale naming the rule(s) applied and why the verdict was chosen.
+
+Follow this hierarchy exactly; do not use any other verdict or criteria.
```

## Migration

- island 0 -> island 1: cell (0, 2), scalar 0.8609, claimed=True
- island 1 -> island 2: cell (0, 3), scalar 0.8599, claimed=True
- island 2 -> island 3: cell (0, 3), scalar 0.8590, claimed=True
- island 3 -> island 0: cell (1, 3), scalar 0.8568, claimed=True

## Lesson retirement (dry run)

- Lesson 15: **RETIRED** — precision 0.155 vs base 0.482, 8.9 sigma below
- Lesson 19: **kept** — precision 0.978 >= base 0.881
- Lesson 17: **kept** — precision 0.989 >= base 0.698
- Lesson 11: **kept** — precision 0.857 vs base 0.944, only 0.7 sigma below

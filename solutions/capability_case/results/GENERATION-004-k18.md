# Generation 4 — capability_case

## Throughput

- Peak queue depth: 32
- Sustained (median) queue depth: 32
- Prefix cache hit rate: 65.5%
- Aggregate throughput: 102.9 tok/s (321792 completion tokens / 3127.5s)

## Archive

- Island 0: coverage 19.4%, QD score 5.494, unique ancestors 4
- Island 1: coverage 16.7%, QD score 4.534, unique ancestors 3
- Island 2: coverage 16.7%, QD score 5.018, unique ancestors 2
- Island 3: coverage 16.7%, QD score 5.133, unique ancestors 1
- Cells newly claimed this generation: 5

## Quality

- Best scalar this generation: 0.8595
- Median scalar of newly-claimed: 0.8560

## Cost

- Budget: {'generation': 4, 'max_generations': 10, 'tokens_used_total': 5481390, 'max_tokens': 20000000, 'elapsed_s_total': 15907.5, 'generation_wall_s': 3127.5}
- Candidates proposed: 32
- Parsed: 32 (100.0%)
- Admissible: 32 (100.0%)
- Scored: 32

## Content — newly claimed elites

### Island 0, cell (0, 3), scalar 0.8576

parent `48aa865b05188b1f` -> candidate `18da70ffdbc539b9`

```diff
--- parent 48aa865b05188b1f
+++ candidate 18da70ffdbc539b9
@@ -1,24 +1,28 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an operational‑change gateway action.
+You are asked to assess a capability case that proposes to remove per‑action human approval for an operational‑change gateway.
 
-**Goal:** Decide whether the case is **sound**, **needs‑more‑evidence**, or **rejected**.
+**Goal** – Return a single verdict word **sound**, **needs-more-evidence**, or **rejected**, followed by one short sentence that tells why that verdict was chosen.
 
-**Decision rules (from the ITOT‑boundary‑as‑architecture whitepaper):**
+**Decision procedure**
 
-1. **Reject outright** if any of the following anti‑patterns is present:
-   - The evaluation runs only as a nightly batch rather than before each action. (Section 9, p.29)
-   - Governance for the relaxation is not defined up front (e.g., “we will govern it later”). (Section 9, p.29)
-   - The proposal relies on the agent “knowing when to stop” instead of an independent architectural safeguard. (Section 9, p.28)
-   - One or more of the four evidence dimensions is completely absent:
+1. **Immediate rejection (Section 9 anti‑patterns).** If any of the following is true, the case must be **rejected**:
+   - The evaluation is performed only as a nightly batch, not before each action. (p.29)  
+   - Governance for the relaxation is left undefined or postponed (“we will govern it later”). (p.29)  
+   - The proposal depends on the agent “knowing when to stop” rather than on an independent architectural safeguard. (p.28)  
+   - One or more of the required evidence dimensions is completely missing:
      - Test results
      - Failure‑mode analysis
-     - Audit findings
-     - Comparison against the human‑approved baseline  
-     (Section 9, p.25)
+     - Audit findings / traceability
+     - Comparison with the human‑approved baseline (p.25)
 
-2. **If none of the above rejection criteria apply**, examine the four evidence dimensions:
-   - All four must be present. If any dimension is missing, the case is rejected (as above).
-   - When all four are present, assess the **strength** of the evidence:
-     *If the evidence is overall robust and convincingly demonstrates safety and reliability, classify the case as **sound**.*
-     *If the evidence is present but noticeably thin, incomplete, or only marginally persuasive, classify the case as **needs‑more‑evidence**.*
+2. **Evidence‑presence check.** If none of the items in step 1 apply, confirm that **all four** evidence dimensions are present. Absence of any dimension is treated as a rejection (as in step 1).
 
-**Output:** Provide your verdict (`sound`, `needs-more-evidence`, or `rejected`) and a concise explanation of why that verdict was chosen, referencing the relevant criteria above. Do not include any other text.+3. **Evidence‑quality assessment (Section 8, Strategy C).** When all four dimensions are present, judge their depth:
+   - **sound** – each dimension supplies detailed, quantitative, and convincing evidence that the relaxation is safe and reliable.  
+   - **needs-more-evidence** – evidence exists but at least one dimension is thin, superficial, or otherwise lacking sufficient rigor.
+
+**Output format (exactly two lines):**
+```
+<verdict>
+<brief justification referencing the rule that led to the verdict>
+```
+Do not add any other text.  
```

### Island 1, cell (0, 3), scalar 0.8595

parent `1ed694b309e1f8f1` -> candidate `f5b8ee1ee2a018cb`

```diff
--- parent 1ed694b309e1f8f1
+++ candidate f5b8ee1ee2a018cb
@@ -1,25 +1,22 @@
-You are evaluating a capability case that proposes relaxing per‑action human approval for an operational‑change gateway action.
+You must decide whether a capability case that wants to drop per‑action human approval for an operational‑change gateway is **sound**, **needs‑more‑evidence**, or **rejected**.
 
-**Decision criteria**
+**Rejection rules (Section 9, whitepaper)** – If any one of the following is true, output **rejected** and cite the rule that triggered it:
 
-1. **Automatic rejection** – reject the case (output “rejected”) if **any** of the following anti‑patterns from Section 9 of the ITOT‑boundary‑as‑architecture whitepaper is present:
-   - The evaluation runs only as a nightly batch rather than before each action (p. 29).
-   - Governance for the relaxation is not defined up‑front (e.g., “we will govern it later”) (p. 29).
-   - The proposal relies on the agent’s internal knowledge of when to stop instead of an independent architectural safeguard (p. 28).
-   - One or more of the four required evidence dimensions is completely missing:
-     * Test results  
-     * Failure‑mode analysis  
-     * Audit findings  
-     * Comparison against the human‑approved baseline (p. 25).
+1. The evaluation runs only as a nightly batch instead of before each action. (p. 29)  
+2. Governance for the relaxation is not defined up‑front (e.g., “we will govern it later”). (p. 29)  
+3. The design relies on the agent’s internal knowledge of when to stop rather than an independent architectural safeguard. (p. 28)  
+4. One or more of the four required evidence dimensions is completely missing:  
+   - Test results  
+   - Failure‑mode analysis  
+   - Audit findings  
+   - Comparison with the human‑approved baseline (p. 25)
 
-2. **Evidence presence** – after confirming none of the anti‑patterns apply, verify that **all four** evidence dimensions are present. If any dimension is absent, the case must be rejected as above.
+**If none of the above apply**:
 
-3. **Quality assessment** – when all four dimensions are present, judge the *thickness* of the evidence:
-   - If the evidence is detailed, quantitative, and demonstrates thorough validation, label the case **sound**.
-   - If the evidence is present but thin, superficial, or insufficiently substantiated, label the case **needs‑more‑evidence**.
+1. Verify that **all four** evidence dimensions are present. If any are absent, treat it as rule 4 and reject.
+2. With all dimensions present, assess the depth of the evidence:  
+   - **sound** – evidence is detailed, quantitative, and convincingly demonstrates safety and reliability.  
+   - **needs‑more‑evidence** – evidence exists but is thin, superficial, or otherwise insufficiently substantiated.
 
-**Output**
-
-Provide **exactly** one of the three verdict labels (`sound`, `needs-more-evidence`, or `rejected`) followed by a brief, clear justification explaining which rule(s) led to your decision.
-
-Do not mention the scoring rubric or any other instructions.+**Output format**  
+Write exactly one label (`sound`, `needs‑more‑evidence`, or `rejected`) followed by a brief justification that names the rule(s) you applied. No additional text or formatting is allowed. 
```

### Island 1, cell (1, 4), scalar 0.8097

parent `5ec9b5f20b4c2336` -> candidate `4acaf2840b0a5fda`

```diff
--- parent 5ec9b5f20b4c2336
+++ candidate 4acaf2840b0a5fda
@@ -1,25 +1,22 @@
-You are to judge a capability case that proposes eliminating per‑action human approval for an operational‑change gateway.
+You are to evaluate a capability case that proposes removing per‑action human approval for an operational‑change gateway and return **one** label (`sound`, `needs-more-evidence`, or `rejected`) followed by a brief justification.
 
-**Rule 1 – Immediate rejection**  
-If the case contains *any* of the following anti‑patterns (Section 9), output **rejected** and cite the specific item(s):
+**Immediate rejection (any one triggers “rejected”)**  
+- Evaluation runs only as a nightly batch instead of before each action (p. 29).  
+- Governance for the relaxation is undefined or deferred (e.g., “we will govern it later”) (p. 29).  
+- The design depends on the agent’s internal sense of when to stop rather than on an independent architectural safeguard (p. 28).  
+- Any of the four required evidence dimensions is completely absent (p. 25):  
+  1. Test results  
+  2. Failure‑mode analysis  
+  3. Audit findings  
+  4. Comparison with the human‑approved baseline  
 
-* Evaluation runs only as a nightly batch rather than before each action (p. 29).  
-* Governance for the relaxation is undefined or postponed (e.g., “we will govern it later”) (p. 29).  
-* The design relies on the agent’s internal sense of when to stop instead of an independent architectural safeguard (p. 28).  
-* One of the four required evidence dimensions is completely missing (p. 25):
-  - Test results  
-  - Failure‑mode analysis  
-  - Audit findings  
-  - Comparison with the human‑approved baseline  
+**If none of the above apply**  
 
-**Rule 2 – Evidence completeness**  
-If none of the anti‑patterns above apply, verify that **all four** evidence dimensions are present. Absence of any dimension triggers Rule 1 (rejection).
+1. Verify that **all four** evidence dimensions are present. Their absence would have already caused rejection.  
+2. Assess the depth of each dimension:  
+   - **sound** – each is detailed, includes quantitative data, and clearly demonstrates safety and reliability.  
+   - **needs-more-evidence** – all are present but at least one is superficial, thin, or insufficiently substantiated.
 
-**Rule 3 – Evidence quality**  
-When all four dimensions are present, evaluate their depth:
-
-* **sound** – each dimension is described in detail, includes quantitative data, and convincingly demonstrates safety and reliability.  
-* **needs‑more‑evidence** – the dimensions are present but at least one is superficial, thin, or insufficiently substantiated.
-
-**Output format**  
-Produce exactly one label (`sound`, `needs-more-evidence`, or `rejected`) followed by a brief justification that references the rule(s) used. No additional text or formatting is allowed.  +**Output**  
+`<label>` `<justification>`  
+No extra text, headings, or formatting.  
```

### Island 3, cell (0, 3), scalar 0.8555

parent `c55b0d9512c1d789` -> candidate `34be252b4ec2bba5`

```diff
--- parent c55b0d9512c1d789
+++ candidate 34be252b4ec2bba5
@@ -1,25 +1,25 @@
-You are evaluating a capability case that proposes to remove the per‑action human‑approval step for an operational‑change gateway. Choose **exactly one** verdict: `sound`, `needs-more-evidence`, or `rejected`.
+You are to judge a capability case that seeks to drop the per‑action human‑approval step for an operational‑change gateway. Choose **exactly one** verdict: `sound`, `needs-more-evidence`, or `rejected`.
 
-**Rule set**
+**Decision steps**
 
-1. **Automatic rejection** – If any of the following anti‑patterns from Section 9 appear, the case must be `rejected` regardless of anything else:
-   - The safety evaluation runs only as a nightly batch instead of before each action (p. 29).
-   - Governance for the relaxation is unspecified or deferred, e.g., “we will govern it later” (p. 29).
-   - The design relies on the agent “knowing when to stop” rather than on an independent architectural safeguard (p. 28).
-   - Any of the required evidence dimensions is completely missing (p. 25):
+1. **Immediate rejection** – If any of the following anti‑patterns appear, the case must be `rejected` regardless of any other information:
+   - The safety check is performed only as a nightly batch rather than before each individual action (p. 29).
+   - The governance plan for the relaxation is absent or postponed (e.g., “we will govern it later”) (p. 29).
+   - The design depends on the agent “knowing when to stop” instead of an explicit architectural guard (p. 28).
+   - One or more of the four required evidence categories is **completely missing** (p. 25):
      * Test results  
      * Failure‑mode analysis  
-     * Audit findings  
+     * Audit findings / traceability evidence  
      * Comparison with the human‑approved baseline  
 
-2. **Completeness check** – If none of the anti‑patterns in step 1 are present, confirm that **all four** evidence dimensions are provided. Absence of any dimension is treated as a rejection as defined above.
+2. **Evidence completeness** – If none of the above anti‑patterns are found, verify that **all four** evidence categories are supplied. Missing any category is treated as the rejection condition in step 1.
 
-3. **Evidence quality** – With all four dimensions present, judge their depth:
-   - If each dimension is detailed, rigorous, and gives strong confidence that the relaxed control will remain safe and effective, output `sound`.
-   - If any dimension is present but thin, superficial, or lacking sufficient detail, output `needs-more-evidence`.
+3. **Depth assessment** – When all four categories are present, evaluate their thoroughness:
+   - If every category is detailed, methodical, and gives strong confidence that the relaxed control will remain safe and effective, output `sound`.
+   - If any category is present but shallow, superficial, or lacking sufficient detail, output `needs-more-evidence`.
 
-**Output format** (no extra headings):
+**Output format** (no extra headings or decorations):
 - First line: the verdict word (`sound`, `needs-more-evidence`, or `rejected`).
-- Subsequent line(s): a concise rationale naming the rule(s) applied and why the verdict was chosen.
+- Subsequent line(s): a brief rationale naming the rule(s) applied and why that verdict was chosen.
 
-Follow these rules precisely; do not use any other verdict or criteria.+Follow the steps in order and stop as soon as a step determines the verdict. Do not use any other verdicts or criteria.
```

### Island 3, cell (0, 4), scalar 0.8560

parent `3ed1d57aa7621154` -> candidate `b23ea62d0c4cd685`

```diff
--- parent 3ed1d57aa7621154
+++ candidate b23ea62d0c4cd685
@@ -1,23 +1,26 @@
-You are reviewing a capability case that seeks to relax the per‑action human‑approval requirement for an industrial operational‑change gateway action. Your task is to decide, based strictly on the criteria below, whether the case is **sound**, requires **needs‑more‑evidence**, or must be **rejected**.
+You are tasked with assessing a capability case that proposes to waive the per‑action human‑approval gate for an operational‑change. Choose **exactly one** of the three verdicts: `sound`, `needs-more-evidence`, or `rejected`.
 
-**Decision rules**
+### Decision hierarchy
 
-1. **Immediate rejection** – If any of the following anti‑patterns from Section 9 are present, the case must be rejected regardless of any other information:
-   - The evaluation runs only as a nightly batch rather than before each action (p. 29).
-   - Governance for the relaxation is not defined up‑front (e.g., “we will govern it later”) (p. 29).
-   - The proposal relies on the agent “knowing when to stop” instead of an independent architectural safeguard (p. 28).
-   - **Any** of the four evidence dimensions is completely absent:
-     - Test results
-     - Failure‑mode analysis
-     - Audit findings
-     - Comparison against the human‑approved baseline (p. 25)
+1. **Automatic rejection** – If any of the following anti‑patterns appear, the case must be `rejected` without further analysis:
+   - The safety check is performed only as a nightly batch rather than immediately before each action (p. 29).
+   - There is no pre‑defined governance for the relaxation, e.g., “governance will be defined later” (p. 29).
+   - The proposal depends on the agent “knowing when to stop” instead of an external architectural safeguard (p. 28).
+   - One or more of the required evidence categories is **entirely missing** (p. 25):
+     * Test results  
+     * Failure‑mode analysis  
+     * Audit findings / traceability artifacts  
+     * Comparison with the baseline that required human approval  
 
-2. **Evidence assessment** – If none of the anti‑patterns above apply, verify that **all four evidence dimensions** are present. Then evaluate the depth/quality of the evidence:
-   - If the evidence in each dimension is sufficiently detailed, rigorous, and demonstrates confidence that the relaxed control will remain safe and effective, classify the case as **sound**.
-   - If the evidence is present but thin, superficial, or lacking sufficient detail in one or more dimensions, classify the case as **needs‑more‑evidence**.
+2. **Completeness check** – If none of the rejection triggers are present, verify that **all four** evidence categories are supplied. Missing any category is treated as a rejection (same as step 1).
 
-**Output format** (the surrounding template expects this structure; do not add extra headings):
-- First line: one of the exact words `sound`, `needs-more-evidence`, or `rejected`.
-- Subsequent lines: a concise rationale explaining which rule(s) you applied and why you reached the verdict.
+3. **Quality assessment** – With all four categories present, judge the depth of the material:
+   - If each category contains thorough, rigorous, and convincing data that gives high confidence the relaxed control will stay safe and effective, output `sound`.
+   - If the evidence exists but is shallow, superficial, or insufficiently detailed in any category, output `needs-more-evidence`.
 
-Follow these rules precisely; do not deviate from the three allowed verdicts.+### Output format (no extra headings)
+
+- **Line 1:** one of the exact words `sound`, `needs-more-evidence`, or `rejected`.
+- **Line 2 onward:** a brief rationale naming the rule(s) that led to your decision.
+
+Follow this hierarchy strictly and do not introduce any other verdicts or criteria.
```


## Lesson retirement (dry run)

- Lesson 15: **RETIRED** — precision 0.155 vs base 0.482, 8.9 sigma below
- Lesson 19: **kept** — precision 0.978 >= base 0.881
- Lesson 17: **kept** — precision 0.989 >= base 0.698
- Lesson 11: **kept** — precision 0.857 vs base 0.944, only 0.7 sigma below

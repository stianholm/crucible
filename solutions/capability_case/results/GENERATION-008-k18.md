# Generation 8 — capability_case

## Throughput

- Peak queue depth: 32
- Sustained (median) queue depth: 32
- Prefix cache hit rate: 66.4%
- Aggregate throughput: 83.8 tok/s (301581 completion tokens / 3600.4s)

## Archive

- Island 0: coverage 19.4%, QD score 5.568, unique ancestors 5
- Island 1: coverage 16.7%, QD score 5.041, unique ancestors 3
- Island 2: coverage 16.7%, QD score 5.022, unique ancestors 2
- Island 3: coverage 19.4%, QD score 5.944, unique ancestors 2
- Cells newly claimed this generation: 2

## Quality

- Best scalar this generation: 0.8621
- Median scalar of newly-claimed: 0.8338

## Cost

- Budget: {'generation': 8, 'max_generations': 10, 'tokens_used_total': 9782904, 'max_tokens': 20000000, 'elapsed_s_total': 29505.9, 'generation_wall_s': 3600.4}
- Candidates proposed: 32
- Parsed: 32 (100.0%)
- Admissible: 32 (100.0%)
- Scored: 32

## Content — newly claimed elites

### Island 1, cell (0, 2), scalar 0.8621

parent `4acaf2840b0a5fda` -> candidate `5be764760b4eb817`

```diff
--- parent 4acaf2840b0a5fda
+++ candidate 5be764760b4eb817
@@ -1,22 +1,23 @@
-You are to evaluate a capability case that proposes removing per‑action human approval for an operational‑change gateway and return **one** label (`sound`, `needs-more-evidence`, or `rejected`) followed by a brief justification.
+Your task is to read a capability case that proposes removing per‑action human approval for an operational‑change gateway and then output **exactly one** label – `sound`, `needs-more-evidence`, or `rejected` – followed by a short justification (one sentence is enough). Do not add any headings, extra punctuation, or formatting.
 
-**Immediate rejection (any one triggers “rejected”)**  
-- Evaluation runs only as a nightly batch instead of before each action (p. 29).  
-- Governance for the relaxation is undefined or deferred (e.g., “we will govern it later”) (p. 29).  
-- The design depends on the agent’s internal sense of when to stop rather than on an independent architectural safeguard (p. 28).  
-- Any of the four required evidence dimensions is completely absent (p. 25):  
+**Immediate rejection (“rejected”)** – if *any* of the following is found, choose `rejected` and name the offending anti‑pattern:
+
+- Evaluation is performed only as a nightly batch rather than right before each action. (Sec 9, p.29)  
+- Governance for the relaxation is absent or postponed (“we will govern it later”). (Sec 9, p.29)  
+- The design relies on the agent’s internal sense of when to stop instead of an independent architectural safeguard. (Sec 9, p.28)  
+- One of the four required evidence dimensions is completely missing (Sec 9, p.25):  
   1. Test results  
   2. Failure‑mode analysis  
   3. Audit findings  
   4. Comparison with the human‑approved baseline  
 
-**If none of the above apply**  
+**If none of the above apply**:
 
-1. Verify that **all four** evidence dimensions are present. Their absence would have already caused rejection.  
-2. Assess the depth of each dimension:  
-   - **sound** – each is detailed, includes quantitative data, and clearly demonstrates safety and reliability.  
-   - **needs-more-evidence** – all are present but at least one is superficial, thin, or insufficiently substantiated.
+1. Confirm that all four evidence dimensions are present (their absence would already trigger rejection).  
+2. Judge the thoroughness of the evidence:  
+   - `sound` – every dimension is detailed, includes quantitative data, and convincingly shows safety and reliability.  
+   - `needs-more-evidence` – all dimensions exist but at least one is shallow, vague, or insufficiently substantiated.
 
-**Output**  
+**Output format**  
 `<label>` `<justification>`  
-No extra text, headings, or formatting.  +(no extra text).  
```

### Island 3, cell (0, 2), scalar 0.8054

parent `46880f90818292b4` -> candidate `2a50b3baf6cc9e9d`

```diff
--- parent 46880f90818292b4
+++ candidate 2a50b3baf6cc9e9d
@@ -1,33 +1,25 @@
-You are to evaluate a capability case that proposes to waive the per‑action human‑approval requirement for an operational‑change gateway. Choose **exactly one** of the words below as the verdict and then give a brief rationale.
+You must decide whether a capability case that seeks to waive the per‑action human‑approval step for an operational‑change gateway is **sound**, **needs-more-evidence**, or **rejected**. Output exactly one of those words on the first line, followed by a brief justification.
 
-**Possible verdicts**
-- `sound`
-- `needs-more-evidence`
-- `rejected`
+**Decision rules**
 
-**Evaluation procedure**
-
-1. **Disqualifying anti‑patterns (automatic rejection)**  
-   If any of the following is found in the case, the verdict must be `rejected` regardless of any other content:
-   - The agent’s evaluation runs only as a nightly batch job instead of before each individual action (p. 29).  
-   - Governance for the relaxation is not defined up‑front (e.g., “we will govern it later”) (p. 29).  
-   - The proposal relies on the agent “knowing when to stop” rather than on an independent architectural safeguard (p. 28).  
-   - One or more of the four required evidence dimensions is completely missing (p. 25):
+1. **Automatic rejection (anti‑patterns)** – If any of the following appear in the case, the verdict is **rejected**, regardless of any other information:
+   - The safety evaluation is performed only as a nightly batch rather than immediately before each action (Section 9, p. 29).  
+   - Governance for the relaxation is left undefined or deferred (e.g., “we will govern it later”) (Section 9, p. 29).  
+   - The design depends on the agent “knowing when to stop” instead of an independent architectural safeguard (Section 9, p. 28).  
+   - One or more of the required evidence dimensions is completely missing (Section 9, p. 25):
      * Test results  
      * Failure‑mode analysis  
-     * Audit findings / traceability evidence  
-     * Comparison against the human‑approved baseline  
+     * Audit / traceability evidence  
+     * Comparison with the human‑approved baseline  
 
-2. **Evidence completeness**  
-   If none of the items in step 1 apply, verify that **all four** evidence dimensions are present. Absence of any dimension is treated as a disqualifying anti‑pattern (i.e., reject).
+2. **Evidence completeness** – If none of the anti‑patterns above are present, verify that **all four** evidence dimensions are supplied. Absence of any dimension is treated as an anti‑pattern and leads to **rejected**.
 
-3. **Evidence quality**  
-   With all four dimensions present, assess their depth:
-   - If each dimension is supplied with sufficient detail, rigor, and demonstrates confidence that the relaxed control will remain safe and effective, output `sound`.  
-   - If the evidence is present but thin, superficial, or lacking enough detail in any dimension, output `needs-more-evidence`.
+3. **Evidence quality** – When all four dimensions are present, judge their depth:
+   - If each dimension is described with sufficient detail, rigor, and provides strong confidence that the relaxed control will remain safe and effective, output **sound**.  
+   - If any dimension is present but superficial, thin, or lacking necessary detail, output **needs-more-evidence**.
 
 **Output format** (no extra headings or formatting):
-- First line: the verdict word (`sound`, `needs-more-evidence`, or `rejected`).  
-- Subsequent line(s): a concise explanation stating which rule(s) were applied and why that verdict was chosen.
+1. First line: one word – `sound`, `needs-more-evidence`, or `rejected`.  
+2. Following line(s): a concise explanation naming the rule(s) applied and the reason for the chosen verdict.
 
-Follow these steps exactly; do not introduce additional criteria.+Apply the rules exactly as written; do not add other criteria or verdicts.
```


## Lesson retirement (dry run)

- Lesson 15: **RETIRED** — precision 0.155 vs base 0.482, 8.9 sigma below
- Lesson 19: **kept** — precision 0.978 >= base 0.881
- Lesson 17: **kept** — precision 0.989 >= base 0.698
- Lesson 11: **kept** — precision 0.857 vs base 0.944, only 0.7 sigma below

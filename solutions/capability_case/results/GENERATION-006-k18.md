# Generation 6 — capability_case

## Throughput

- Peak queue depth: 32
- Sustained (median) queue depth: 32.0
- Prefix cache hit rate: 66.0%
- Aggregate throughput: 91.7 tok/s (309987 completion tokens / 3379.1s)

## Archive

- Island 0: coverage 19.4%, QD score 5.567, unique ancestors 5
- Island 1: coverage 16.7%, QD score 5.040, unique ancestors 3
- Island 2: coverage 16.7%, QD score 5.021, unique ancestors 2
- Island 3: coverage 16.7%, QD score 5.137, unique ancestors 2
- Cells newly claimed this generation: 3

## Quality

- Best scalar this generation: 0.8585
- Median scalar of newly-claimed: 0.8554

## Cost

- Budget: {'generation': 6, 'max_generations': 10, 'tokens_used_total': 7650973, 'max_tokens': 20000000, 'elapsed_s_total': 22460.1, 'generation_wall_s': 3379.1}
- Candidates proposed: 32
- Parsed: 32 (100.0%)
- Admissible: 32 (100.0%)
- Scored: 32

## Content — newly claimed elites

### Island 0, cell (0, 5), scalar 0.8554

parent `18da70ffdbc539b9` -> candidate `e3d211725ba40d4c`

```diff
--- parent 18da70ffdbc539b9
+++ candidate e3d211725ba40d4c
@@ -1,28 +1,25 @@
-You are asked to assess a capability case that proposes to remove per‑action human approval for an operational‑change gateway.
+You are to judge a capability case that proposes removing per‑action human approval for an operational‑change gateway.
 
-**Goal** – Return a single verdict word **sound**, **needs-more-evidence**, or **rejected**, followed by one short sentence that tells why that verdict was chosen.
+**Output:** exactly two lines  
+1️⃣ verdict – one word: `sound`, `needs-more-evidence`, or `rejected`  
+2️⃣ brief justification – cite the rule that determined the verdict
 
-**Decision procedure**
+**Decision rules**
 
-1. **Immediate rejection (Section 9 anti‑patterns).** If any of the following is true, the case must be **rejected**:
-   - The evaluation is performed only as a nightly batch, not before each action. (p.29)  
-   - Governance for the relaxation is left undefined or postponed (“we will govern it later”). (p.29)  
-   - The proposal depends on the agent “knowing when to stop” rather than on an independent architectural safeguard. (p.28)  
-   - One or more of the required evidence dimensions is completely missing:
-     - Test results
-     - Failure‑mode analysis
-     - Audit findings / traceability
-     - Comparison with the human‑approved baseline (p.25)
+1. **Automatic rejection (Section 9 anti‑patterns).** If *any* of the following is true, output `rejected` and name the violated anti‑pattern:  
+   - Evaluation runs only as a nightly batch, not before each action (p. 29).  
+   - Governance for the relaxation is undefined or postponed (“we will govern it later”) (p. 29).  
+   - The design relies on the agent “knowing when to stop” instead of an independent architectural safeguard (p. 28).  
+   - One of the required evidence dimensions is completely missing (p. 25):  
+     • Test results  
+     • Failure‑mode analysis  
+     • Audit findings / traceability  
+     • Comparison with the human‑approved baseline  
 
-2. **Evidence‑presence check.** If none of the items in step 1 apply, confirm that **all four** evidence dimensions are present. Absence of any dimension is treated as a rejection (as in step 1).
+2. **Evidence completeness.** If no anti‑pattern applies, verify that **all four** evidence dimensions are present. If any is absent, treat it as the same rejection case as in rule 1.
 
-3. **Evidence‑quality assessment (Section 8, Strategy C).** When all four dimensions are present, judge their depth:
-   - **sound** – each dimension supplies detailed, quantitative, and convincing evidence that the relaxation is safe and reliable.  
-   - **needs-more-evidence** – evidence exists but at least one dimension is thin, superficial, or otherwise lacking sufficient rigor.
+3. **Evidence quality (Section 8, Strategy C).** When all four dimensions are present, assess their depth:  
+   - `sound` – every dimension provides detailed, quantitative, and convincing evidence that the relaxation is safe.  
+   - `needs-more-evidence` – evidence exists for all dimensions but at least one is thin, superficial, or lacking sufficient rigor.
 
-**Output format (exactly two lines):**
-```
-<verdict>
-<brief justification referencing the rule that led to the verdict>
-```
-Do not add any other text.  +Follow the rules in order; the first applicable rule determines the verdict. Do not add any other text.  
```

### Island 2, cell (0, 5), scalar 0.8552

parent `33209f3df76a81cc` -> candidate `738c94f800f5d0fd`

```diff
--- parent 33209f3df76a81cc
+++ candidate 738c94f800f5d0fd
@@ -1,22 +1,33 @@
-You must label the capability case as **sound**, **needs‑more‑evidence**, or **rejected** and give a brief justification that names the rule(s) you used.
+Your job is to assign one of three verdicts—**sound**, **needs‑more‑evidence**, or **rejected**—to the capability case and to supply a short reason that cites the rule(s) you applied.
 
-**Immediate rejection (any one applies → output “rejected”)**
+**Step 1 – Automatic disqualification (any one triggers “rejected”)**
 
-1. Evaluation is performed only as a nightly batch, not before each action (p. 29).  
-2. Governance for the relaxation is not defined up‑front or is deferred (e.g., “we will govern it later”) (p. 29).  
-3. The design depends on the agent’s internal knowledge of when to stop instead of an independent architectural safeguard (p. 28).  
-4. Any of the four required evidence dimensions is completely missing (p. 25):
-   - Test results  
-   - Failure‑mode analysis  
-   - Audit findings  
-   - Comparison with the human‑approved baseline  
+- The safety check is executed only as a nightly batch rather than immediately before each action (see § 8, p. 29).  
+- Governance for the waiver is absent or postponed (“we will define it later”) (§ 8, p. 29).  
+- The design relies on the agent’s internal decision‑making (“knows when to stop”) instead of an external architectural guard (§ 8, p. 28).  
+- One of the four mandatory evidence categories is completely missing (§ 9, p. 25):  
+  1. Test results  
+  2. Failure‑mode analysis  
+  3. Audit findings / traceability  
+  4. Comparison with the human‑approved baseline  
 
-**If none of the above apply**
+If any of these conditions holds, output:  
+`rejected <mention the specific anti‑pattern>`  
 
-1. Verify that **all four** evidence dimensions are present (absence would have triggered rule 4).  
-2. Assess the depth of the evidence:  
-   - **sound** – each dimension is detailed, quantitative, and convincingly demonstrates safety and reliability.  
-   - **needs‑more‑evidence** – all dimensions are present but at least one is thin, superficial, or otherwise insufficiently substantiated.
+**Step 2 – Evidence depth (run only when Step 1 did not reject)**  
 
-**Output format**  
-Write a single line: `<label>` `<justification>` (e.g., `sound evidence detailed in all four dimensions`). No extra text, headings, or formatting may be added.+All four evidence categories must be present (their absence would have caused rejection). Judge each:
+
+- **Substantive** – provides detailed data, quantitative metrics, or thorough analysis.  
+- **Thin** – only high‑level, cursory, or incomplete information.
+
+- If every category is **substantive**, the verdict is **sound**.  
+- If all are present but at least one is **thin**, the verdict is **needs‑more‑evidence**.
+
+**Step 3 – Output**  
+
+Write exactly one line:  
+
+`<verdict> <concise justification referencing the rule(s) used>`  
+
+Do not add headings, extra lines, or any other formatting.  
```

### Island 2, cell (0, 4), scalar 0.8585

parent `33209f3df76a81cc` -> candidate `17ddc08ff9d90218`

```diff
--- parent 33209f3df76a81cc
+++ candidate 17ddc08ff9d90218
@@ -1,22 +1,24 @@
-You must label the capability case as **sound**, **needs‑more‑evidence**, or **rejected** and give a brief justification that names the rule(s) you used.
+Your task is to assign one of three verdicts—**sound**, **needs‑more‑evidence**, or **rejected**—to the capability case and supply a concise reason that cites the rule(s) applied.
 
-**Immediate rejection (any one applies → output “rejected”)**
+**Step 1 – Immediate rejection (any condition true → verdict = rejected)**  
+Reject if the case exhibits any of the following anti‑patterns (Section 9):
 
-1. Evaluation is performed only as a nightly batch, not before each action (p. 29).  
-2. Governance for the relaxation is not defined up‑front or is deferred (e.g., “we will govern it later”) (p. 29).  
-3. The design depends on the agent’s internal knowledge of when to stop instead of an independent architectural safeguard (p. 28).  
-4. Any of the four required evidence dimensions is completely missing (p. 25):
+1. Safety evaluation is scheduled only as a nightly batch rather than run **before each individual action** (p. 29).  
+2. Governance for the relaxation is left undefined or postponed (e.g., “govern later”) (p. 29).  
+3. The solution relies on the agent’s internal “knowledge of when to stop” instead of an **independent architectural safeguard** (p. 28).  
+4. One of the four required evidence dimensions is **completely missing** (p. 25):  
    - Test results  
    - Failure‑mode analysis  
-   - Audit findings  
+   - Audit findings / traceability  
    - Comparison with the human‑approved baseline  
 
-**If none of the above apply**
+If any of the above is present, output **rejected** and mention the specific anti‑pattern.
 
-1. Verify that **all four** evidence dimensions are present (absence would have triggered rule 4).  
-2. Assess the depth of the evidence:  
-   - **sound** – each dimension is detailed, quantitative, and convincingly demonstrates safety and reliability.  
-   - **needs‑more‑evidence** – all dimensions are present but at least one is thin, superficial, or otherwise insufficiently substantiated.
+**Step 2 – Evidence assessment (run only if no anti‑pattern matched)**  
+All four evidence dimensions must be present (absence would have triggered Step 1). Evaluate their depth:
 
-**Output format**  
-Write a single line: `<label>` `<justification>` (e.g., `sound evidence detailed in all four dimensions`). No extra text, headings, or formatting may be added.+* **sound** – every dimension provides detailed, quantitative information that convincingly demonstrates safety and reliability.  
+* **needs‑more‑evidence** – all dimensions are present but at least one is shallow, high‑level, or otherwise insufficiently substantiated.
+
+**Output requirement**  
+Produce exactly one line containing the verdict label, a single space, then your brief justification (e.g., `sound all four dimensions detailed`). No headings, line breaks, or extra text are allowed.
```


## Lesson retirement (dry run)

- Lesson 15: **RETIRED** — precision 0.155 vs base 0.482, 8.9 sigma below
- Lesson 19: **kept** — precision 0.978 >= base 0.881
- Lesson 17: **kept** — precision 0.989 >= base 0.698
- Lesson 11: **kept** — precision 0.857 vs base 0.944, only 0.7 sigma below

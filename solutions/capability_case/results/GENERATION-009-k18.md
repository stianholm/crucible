# Generation 9 — capability_case

## Throughput

- Peak queue depth: 32
- Sustained (median) queue depth: 32
- Prefix cache hit rate: 66.5%
- Aggregate throughput: 103.4 tok/s (301136 completion tokens / 2912.4s)

## Archive

- Island 0: coverage 19.4%, QD score 5.568, unique ancestors 5
- Island 1: coverage 16.7%, QD score 5.041, unique ancestors 3
- Island 2: coverage 16.7%, QD score 5.022, unique ancestors 2
- Island 3: coverage 19.4%, QD score 5.944, unique ancestors 2
- Cells newly claimed this generation: 1

## Quality

- Best scalar this generation: 0.8590
- Median scalar of newly-claimed: 0.8590

## Cost

- Budget: {'generation': 9, 'max_generations': 10, 'tokens_used_total': 10847711, 'max_tokens': 20000000, 'elapsed_s_total': 32418.4, 'generation_wall_s': 2912.4}
- Candidates proposed: 32
- Parsed: 32 (100.0%)
- Admissible: 32 (100.0%)
- Scored: 32

## Content — newly claimed elites

### Island 2, cell (0, 4), scalar 0.8590

parent `33209f3df76a81cc` -> candidate `31d22220de9cae13`

```diff
--- parent 33209f3df76a81cc
+++ candidate 31d22220de9cae13
@@ -1,22 +1,20 @@
-You must label the capability case as **sound**, **needs‑more‑evidence**, or **rejected** and give a brief justification that names the rule(s) you used.
+Your task is to assign one of three labels—**sound**, **needs‑more‑evidence**, or **rejected**—to the capability case and to supply a concise reason that cites the rule(s) you applied.
 
-**Immediate rejection (any one applies → output “rejected”)**
-
-1. Evaluation is performed only as a nightly batch, not before each action (p. 29).  
-2. Governance for the relaxation is not defined up‑front or is deferred (e.g., “we will govern it later”) (p. 29).  
-3. The design depends on the agent’s internal knowledge of when to stop instead of an independent architectural safeguard (p. 28).  
-4. Any of the four required evidence dimensions is completely missing (p. 25):
+**Reject outright if any of the following applies (label = rejected):**
+1. Safety evaluation runs only as a nightly batch instead of before each individual action (p. 29).  
+2. Governance for the relaxation is not defined up‑front, e.g., “we will govern it later” (p. 29).  
+3. The proposal depends on the agent’s internal knowledge of when to stop rather than on an independent architectural safeguard (p. 28).  
+4. One of the four required evidence dimensions is completely missing (p. 25):
    - Test results  
    - Failure‑mode analysis  
    - Audit findings  
    - Comparison with the human‑approved baseline  
 
-**If none of the above apply**
+**If none of the above triggers rejection:**
+1. Confirm that all four evidence dimensions are present (otherwise rule 4 would have caused rejection).  
+2. Judge the quality of the evidence:  
+   - **sound** – each dimension is presented with detailed, quantitative, and convincing information.  
+   - **needs‑more‑evidence** – all dimensions are present but at least one is superficial, sparse, or otherwise insufficiently substantiated.
 
-1. Verify that **all four** evidence dimensions are present (absence would have triggered rule 4).  
-2. Assess the depth of the evidence:  
-   - **sound** – each dimension is detailed, quantitative, and convincingly demonstrates safety and reliability.  
-   - **needs‑more‑evidence** – all dimensions are present but at least one is thin, superficial, or otherwise insufficiently substantiated.
-
-**Output format**  
-Write a single line: `<label>` `<justification>` (e.g., `sound evidence detailed in all four dimensions`). No extra text, headings, or formatting may be added.+**Output requirement**  
+Produce a single line: `<label>` `<justification>` (for example, `sound evidence thorough across all four dimensions`). No extra headings, lines, or formatting are allowed.
```


## Lesson retirement (dry run)

- Lesson 15: **RETIRED** — precision 0.155 vs base 0.482, 8.9 sigma below
- Lesson 19: **kept** — precision 0.978 >= base 0.881
- Lesson 17: **kept** — precision 0.989 >= base 0.698
- Lesson 11: **kept** — precision 0.857 vs base 0.944, only 0.7 sigma below

## Held-out check (best-ever candidate)

- Candidate: `5be764760b4eb817` (rotation scalar 0.8621)
- Held-out quality: 0.9724 (passes: 0.9783, 0.9666)
- Held-out scalar: 0.8541 (passes: 0.8557, 0.8526)
- All held-out tasks valid: True

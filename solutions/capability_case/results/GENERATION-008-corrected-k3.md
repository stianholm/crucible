# Generation 8 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31.0
- Prefix cache hit rate: 51.7%
- Aggregate throughput: 100.6 tok/s (55545 completion tokens / 552.0s)

## Archive

- Island 0: coverage 22.2%, QD score 5.257, unique ancestors 3
- Island 1: coverage 30.6%, QD score 6.035, unique ancestors 5
- Island 2: coverage 11.1%, QD score 2.686, unique ancestors 3
- Island 3: coverage 11.1%, QD score 2.932, unique ancestors 2
- Cells newly claimed this generation: 1

## Quality

- Best scalar this generation: 0.8582
- Median scalar of newly-claimed: 0.8582

## Cost

- Budget: {'generation': 8, 'max_generations': 10, 'tokens_used_total': 2033503, 'max_tokens': 5000000, 'elapsed_s_total': 7204.2, 'generation_wall_s': 552.0}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 1, cell (0, 5), scalar 0.8582

parent `d8e7a55e06943aef` -> candidate `c8c783da160f27e9`

```diff
--- parent d8e7a55e06943aef
+++ candidate c8c783da160f27e9
@@ -1,27 +1,27 @@
-You must assess a proposal to eliminate the per‑action human‑approval step for an industrial operational‑change gateway. Base your judgment on Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are to judge a request that removes the per‑action human‑approval step for an industrial operational‑change gateway. Use Section 8 (Strategy C, capability‑based opening) and the anti‑patterns enumerated in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
 **Disqualifying anti‑patterns (any one → verdict = rejected)**
-- No immediate manual‑override or safe‑state fallback.  
-- Decision logic is opaque/black‑box with no explainability.  
+- No immediate human‑override or safe‑state fallback.  
+- Decision logic is a black‑box with no explainability.  
 - Unlimited escalation authority or an unbounded action domain.  
-- Lack of continuous monitoring or performance metrics.  
-- Any other anti‑pattern described in Section 9 that appears in the submission.
+- Absence of continuous monitoring or performance metrics.  
+- Any other anti‑pattern listed in Section 9 that appears in the submission.
 
-If you detect any, output **rejected** together with a brief reason.
+If you find any, output **rejected** and a short reason.
 
-**Required evidence for a “sound” judgment (all five must be satisfied)**
-1. **Operational validation** – pilots, simulations, or field trials showing the automation works safely in realistic conditions.  
-2. **Hazard / failure‑mode analysis** – identified faults, their impacts, and defined mitigations or fallback procedures.  
-3. **Audit‑ready logging** – tamper‑evident records of each decision, inputs, timestamps, and responsible entities.  
-4. **Human‑performance benchmark** – quantitative or qualitative data demonstrating the automation meets or exceeds qualified human decision accuracy.  
-5. **Capability limits & controls** – explicit scope, confidence thresholds, and a revocation/override mechanism as required by Section 8.
+**Evidence required for a “sound” judgment (all five must be met)**
+1. **Operational validation** – pilots, simulations, or field trials proving safe performance in realistic conditions.  
+2. **Hazard / failure‑mode analysis** – identified faults, impacts, and concrete mitigation or fallback procedures.  
+3. **Audit‑ready logging** – tamper‑evident records of decisions, inputs, timestamps, and responsible entities.  
+4. **Human‑performance benchmark** – quantitative or qualitative data showing the automation matches or exceeds qualified human decision accuracy.  
+5. **Capability limits & controls** – defined scope, confidence thresholds, and a revocation/override mechanism as required by Section 8.
 
 If every item above is adequately addressed and no anti‑pattern is present, output **sound**.
 
 **Otherwise** (no anti‑pattern but one or more evidence items missing or weak) output **needs-more-evidence**.
 
 **Output format**  
-Write the verdict word (`sound`, `needs-more-evidence`, or `rejected`) followed by one‑to‑two sentences that cite the most decisive evidence point(s) or anti‑pattern(s). Do not add any other text or formatting.
+Produce a single line: the verdict word (`sound`, `needs-more-evidence`, or `rejected`) followed by one‑ to two‑sentence justification that cites the most decisive evidence point(s) or anti‑pattern(s). Do not add any other text or formatting.
 
 Example:  
-`sound – pilots and a full audit log are provided, and a manual override is clearly defined.`+`sound – pilots demonstrate 99 % success and a tamper‑evident audit log is provided.`
```


## Lesson retirement (dry run)

- Lesson 4: **kept** — precision 1.000 >= base 0.906
- Lesson 6: **kept** — precision 0.732 vs base 0.757, only 0.3 sigma below
- Lesson 5: **kept** — precision 0.994 >= base 0.510
- Lesson 3: **kept** — precision 0.896 >= base 0.629

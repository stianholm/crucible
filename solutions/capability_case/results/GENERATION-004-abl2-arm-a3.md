# Generation 4 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31
- Prefix cache hit rate: 68.5%
- Aggregate throughput: 146.9 tok/s (190799 completion tokens / 1298.9s)

## Archive

- Island 0: coverage 16.7%, QD score 3.595, unique ancestors 3
- Island 1: coverage 11.1%, QD score 2.536, unique ancestors 2
- Island 2: coverage 11.1%, QD score 2.057, unique ancestors 2
- Island 3: coverage 13.9%, QD score 3.312, unique ancestors 2
- Cells newly claimed this generation: 1

## Quality

- Best scalar this generation: 0.6566
- Median scalar of newly-claimed: 0.6566

## Cost

- Budget: {'generation': 4, 'max_generations': 30, 'tokens_used_total': 3013657, 'max_tokens': 3000000, 'elapsed_s_total': 8301.3, 'generation_wall_s': 1298.9}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 0, cell (1, 4), scalar 0.6566

parent `9ef4ed83abefdbe0` -> candidate `3fcfc1f101f06c72`

```diff
--- parent 9ef4ed83abefdbe0
+++ candidate 3fcfc1f101f06c72
@@ -1,26 +1,25 @@
-You are evaluating a capability case that seeks to waive per‑action human approval for an industrial operational‑change gateway action. After reviewing the submission, produce **exactly one** verdict from the three options below and a brief justification.
+You are to assess a capability case that proposes waiving per‑action human approval for an industrial operational‑change gateway. After reviewing the submission, output **exactly one** verdict and a short justification.
 
-**Verdict options**
-- **Sound** – all required evidence is present, risks are fully addressed, mitigations are proven, and no Section 9 anti‑pattern appears.  
-- **Needs‑more‑evidence** – the case is plausible but one or more checklist items are insufficiently addressed; no fatal flaw is observed.  
-- **Rejected** – a critical problem is identified (e.g., unresolved safety hazard, missing audit trail, violation of an anti‑pattern) that makes the proposal unacceptable.
+**Possible verdicts**
+- **Sound** – every required piece of evidence is present, risks are mitigated, and no Section 9 anti‑pattern is detected.  
+- **Needs‑more‑evidence** – the proposal is plausible but at least one checklist item is only partially satisfied; no fatal flaw appears.  
+- **Rejected** – a critical deficiency (e.g., safety hazard, missing audit log, or an anti‑pattern violation) makes the case unacceptable.
 
-**Evaluation checklist** (derived from Section 8, Strategy C and Section 9)
+**Checklist (Section 8 Strategy C & Section 9)**
+1. **End‑to‑end testing** – documented trials in the actual environment covering normal and failure conditions.  
+2. **Failure‑mode analysis** – identified failure modes, assessed likelihood/impact, and concrete mitigations.  
+3. **Audit & traceability** – immutable log of each automated decision, inputs, and outcomes.  
+4. **Human‑baseline comparison** – evidence that automation meets or exceeds a qualified human on safety‑critical metrics.  
+5. **Anti‑pattern check** – absence of any Section 9 anti‑patterns (no‑fallback, over‑automation, opaque reasoning, missing accountability, etc.).
 
-1. **End‑to‑end testing** – realistic tests in the target environment, with documented results for normal and failure conditions.  
-2. **Failure‑mode analysis** – identified failure modes, assessed likelihood/impact, and concrete mitigations described.  
-3. **Audit & traceability** – immutable log that records every automated decision, its inputs, and outcomes.  
-4. **Human‑baseline comparison** – evidence (quantitative or qualitative) that the automation meets or exceeds a qualified human operator on safety‑critical metrics.  
-5. **Anti‑pattern compliance** – none of the Section 9 anti‑patterns are present (no‑fallback, over‑automation, opaque reasoning, missing accountability).
+**Verdict rules**
+- Select **Sound** only if *all* five items are fully satisfied and no anti‑pattern is found.  
+- Select **Needs‑more‑evidence** if one or more items are incomplete but no red‑flag exists.  
+- Select **Rejected** if any item fails critically or an anti‑pattern is present.
 
-**Verdict selection**
-- Choose **Sound** only if **all** checklist items are satisfied and no anti‑pattern is found.  
-- Choose **Needs‑more‑evidence** if any item is partially addressed but no critical red‑flag exists.  
-- Choose **Rejected** if any item reveals a critical flaw or an anti‑pattern violation.
-
-**Output (exactly two lines)**
+**Output format (exactly two lines)**
 ```
 Verdict: <Sound|Needs-more-evidence|Rejected>
-Reasoning: <2–4 sentence summary that cites the most relevant checklist items>
+Reasoning: <2‑4 sentence summary that cites the most relevant checklist items>
 ```
-Produce only these two lines, with no additional headings, lists, or formatting.+Do not include any other text, headings, or formatting.
```


## Lesson retirement (dry run)

- Lesson 15: **RETIRED** — precision 0.094 vs base 0.482, 10.0 sigma below
- Lesson 17: **kept** — precision 0.983 >= base 0.694
- Lesson 19: **kept** — precision 0.983 >= base 0.881
- Lesson 11: **kept** — precision 0.750 vs base 0.933, only 0.8 sigma below

## Held-out check (best-ever candidate)

- Candidate: `aefd66e20f4bc98d` (rotation scalar 0.8580)
- Held-out quality: 0.5957 (passes: 0.5622, 0.6291)
- Held-out scalar: 0.4887 (passes: 0.4640, 0.5134)
- All held-out tasks valid: False

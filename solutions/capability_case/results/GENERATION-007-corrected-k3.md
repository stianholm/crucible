# Generation 7 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31.0
- Prefix cache hit rate: 51.8%
- Aggregate throughput: 114.2 tok/s (66680 completion tokens / 584.0s)

## Archive

- Island 0: coverage 22.2%, QD score 5.257, unique ancestors 3
- Island 1: coverage 30.6%, QD score 5.971, unique ancestors 5
- Island 2: coverage 11.1%, QD score 2.686, unique ancestors 3
- Island 3: coverage 11.1%, QD score 2.932, unique ancestors 2
- Cells newly claimed this generation: 1

## Quality

- Best scalar this generation: 0.6074
- Median scalar of newly-claimed: 0.6074

## Cost

- Budget: {'generation': 7, 'max_generations': 10, 'tokens_used_total': 1812705, 'max_tokens': 5000000, 'elapsed_s_total': 6652.0, 'generation_wall_s': 584.0}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 0, cell (0, 3), scalar 0.6074

parent `f701fdc18e6e16db` -> candidate `019f9ddcf6ae5593`

```diff
--- parent f701fdc18e6e16db
+++ candidate 019f9ddcf6ae5593
@@ -1,21 +1,32 @@
-You are evaluating a capability case that proposes to drop per‑action human approval for an industrial operational‑change gateway. Apply the criteria from **Section 8 (Strategy C – capability‑based opening)** and verify that none of the **Section 9 anti‑patterns** are present.
+You are reviewing a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway. Base your assessment on **Section 8 (Strategy C – capability‑based opening)** and verify that none of the **Section 9 anti‑patterns** appear.
 
-**Checklist (all must be satisfied for a “sound” judgment)**  
-1. **Real‑world validation** – functional tests or pilots covering normal operation, edge cases and failure modes, with quantitative results.  
-2. **Failure‑mode & mitigation** – documented possible failures, mitigation measures and a concrete fallback/escalation plan.  
-3. **Auditability** – immutable logs that record every automated decision with timestamps and provenance, accessible for review.  
-4. **Human‑equivalence** – quantitative or qualitative comparison of the automation’s decisions to expert‑human decisions.  
-5. **Section 8 compliance** – explicit reference to the capability‑based opening requirements (risk thresholds, fallback, etc.).  
-6. **No Section 9 anti‑patterns** – confirmation that the design avoids every listed anti‑pattern (e.g., unbounded authority, no fallback, opaque logic, missing safety interlocks).
+### Evidence checklist (all must be met for a “sound” result)
 
-**Decision rules**  
-- **rejected** – any anti‑pattern is found or any of items 1‑3 are completely missing.  
-- **sound** – items 1‑6 are fully satisfied and no anti‑pattern is present.  
-- **needs‑more‑evidence** – passes the reject test but one or more items are only partially addressed.
+1. **Real‑world validation** – documented pilots or field tests exercising normal, edge‑case and failure scenarios, with quantitative outcomes.  
+2. **Failure‑mode analysis & mitigation** – a list of plausible failure modes, associated risk metrics, and concrete fallback or escalation procedures.  
+3. **Audit trail** – immutable, timestamped logs that capture every automated decision, its inputs, and provenance, and that can be inspected later.  
+4. **Human‑equivalence** – a comparison (quantitative or qualitative) showing that the automation’s decisions are at least as reliable as those of a qualified human operator.  
+5. **Section 8 compliance reference** – explicit statement that the proposal satisfies the capability‑based opening requirements (risk thresholds, fallback, etc.).  
 
-**Output (exactly two lines)**  
+### Anti‑pattern screening (any occurrence forces a **rejected** verdict)
+
+- Unbounded authority or missing escalation limits  
+- Absence of a safe‑state/rollback mechanism  
+- Opaque or “black‑box” decision logic without explainability  
+- Missing safety interlocks or revocation capability  
+- Lack of independent verification or validation  
+
+### Verdict rules  
+
+- **rejected** – if any anti‑pattern is detected **or** any of items 1‑3 are completely absent.  
+- **needs‑more‑evidence** – if no anti‑pattern is found but one or more checklist items are only partially satisfied.  
+- **sound** – if all checklist items 1‑5 are fully satisfied and no anti‑pattern is present.
+
+### Required output (exactly two lines)
+
 ```
 Verdict: <sound|needs-more-evidence|rejected>
-Reasoning: <brief reference to the checklist items supporting your decision>
+Reasoning: <concise reference to the checklist items or anti‑patterns that justify the decision>
 ``` 
-Do not add any other text.+
+Produce only these two lines, no additional text.
```


## Lesson retirement (dry run)

- Lesson 4: **kept** — precision 1.000 >= base 0.906
- Lesson 6: **kept** — precision 0.732 vs base 0.757, only 0.3 sigma below
- Lesson 5: **kept** — precision 0.994 >= base 0.510
- Lesson 3: **kept** — precision 0.896 >= base 0.629

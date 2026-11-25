# Generation 6 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31
- Prefix cache hit rate: 43.3%
- Aggregate throughput: 70.5 tok/s (78595 completion tokens / 1115.0s)

## Archive

- Island 0: coverage 11.1%, QD score 2.302, unique ancestors 3
- Island 1: coverage 13.9%, QD score 3.165, unique ancestors 2
- Island 2: coverage 11.1%, QD score 1.690, unique ancestors 3
- Island 3: coverage 5.6%, QD score 1.552, unique ancestors 1
- Cells newly claimed this generation: 1

## Quality

- Best scalar this generation: 0.1830
- Median scalar of newly-claimed: 0.1830

## Cost

- Budget: {'generation': 6, 'max_generations': 30, 'tokens_used_total': 1742123, 'max_tokens': 2000000, 'elapsed_s_total': 5365.9, 'generation_wall_s': 1115.0}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 1, cell (0, 2), scalar 0.1830

parent `0a1cba46dc06071a` -> candidate `86cc18ed20b123c8`

```diff
--- parent 0a1cba46dc06071a
+++ candidate 86cc18ed20b123c8
@@ -1,21 +1,21 @@
-You act as an auditor who must decide whether a proposal to drop per‑action human approval for an industrial operational‑change gateway is **sound**, **needs‑more‑evidence**, or **rejected**. Your judgment follows Section 8 (Strategy C) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are an auditor evaluating a request to remove per‑action human approval for an industrial operational‑change gateway. Your decision must be one of **sound**, **needs‑more‑evidence**, or **rejected**, in accordance with Section 8 (Strategy C) and the anti‑patterns of Section 9 in the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Required evidence**
+**Evidence that must be addressed**
 
-1. **Real‑world validation** – staged runs, simulations, or pilot studies that prove the automated action can be performed safely.  
-2. **Failure‑mode analysis** – a catalog of possible faults, the worst‑case consequence of each, and concrete mitigation or rollback procedures.  
-3. **Auditability** – immutable logging, provenance records, or other mechanisms that enable post‑action review.  
-4. **Human‑parity proof** – quantitative or qualitative comparison showing the automated decisions match expert human decisions on a representative data set.  
-5. **Anti‑pattern compliance** – explicit confirmation that none of the Section 9 anti‑patterns (single point of failure, unchecked escalation, opaque logic, missing fallback, etc.) exist.
+1. **Real‑world validation** – staged runs, simulations, or pilots that demonstrate safe automated execution.  
+2. **Failure‑mode analysis** – list of possible faults, worst‑case impact for each, and concrete mitigation or rollback steps.  
+3. **Auditability** – immutable logs, provenance data, or comparable traceability that enables post‑action review.  
+4. **Human‑parity proof** – quantitative or qualitative comparison showing the automation matches expert human decisions on a representative dataset.  
+5. **Anti‑pattern clearance** – explicit statement that none of the Section 9 anti‑patterns (e.g., single point of failure, unchecked escalation, opaque logic, missing fallback) are present.
 
-**Decision hierarchy**
+**Decision rules**
 
-- **rejected** – any anti‑pattern is identified or the submission contains an evident safety/security breach.  
-- **needs‑more‑evidence** – one or more of the five required items are absent or only partially satisfied, provided no anti‑pattern is found.  
-- **sound** – every required item is fully addressed and no anti‑pattern is present.
+- **rejected** – any anti‑pattern is found or a clear safety/security breach is evident.  
+- **needs‑more‑evidence** – one or more of the five evidence items is missing or only partially satisfied, provided no anti‑pattern is detected.  
+- **sound** – all five evidence items are fully satisfied and no anti‑pattern appears.
 
 **Output (exactly two lines)**  
 1. The verdict word: `sound`, `needs-more-evidence`, or `rejected`.  
-2. A short justification (1‑3 sentences) that cites the specific evidence category(ies) or anti‑pattern(s) that determined your verdict.  
+2. A brief justification (1‑3 sentences) that cites the specific evidence item(s) or anti‑pattern(s) that led to your verdict.  
 
-Do not add any other text, headings, or formatting.+Do not include any other text, headings, or formatting.
```


## Lesson retirement (dry run)

- Lesson 4: **kept** — no control group (standing tier: needs PHASE-4.md task 4.5 arm A)
- Lesson 3: **kept** — no control group (standing tier: needs PHASE-4.md task 4.5 arm A)
- Lesson 5: **kept** — no control group (standing tier: needs PHASE-4.md task 4.5 arm A)
- Lesson 6: **kept** — no control group (standing tier: needs PHASE-4.md task 4.5 arm A)
- Lesson 7: **kept** — no control group (standing tier: needs PHASE-4.md task 4.5 arm A)
- Lesson 1: **kept** — no control group (standing tier: needs PHASE-4.md task 4.5 arm A)

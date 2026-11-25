# Generation 5 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31.0
- Prefix cache hit rate: 48.9%
- Aggregate throughput: 63.1 tok/s (75089 completion tokens / 1189.6s)

## Archive

- Island 0: coverage 13.9%, QD score 2.808, unique ancestors 1
- Island 1: coverage 19.4%, QD score 3.462, unique ancestors 3
- Island 2: coverage 19.4%, QD score 2.920, unique ancestors 1
- Island 3: coverage 16.7%, QD score 3.116, unique ancestors 3
- Cells newly claimed this generation: 2

## Quality

- Best scalar this generation: 0.5149
- Median scalar of newly-claimed: 0.4946

## Cost

- Budget: {'generation': 5, 'max_generations': 30, 'tokens_used_total': 1678630, 'max_tokens': 2000000, 'elapsed_s_total': 6256.6, 'generation_wall_s': 1189.6}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 0, cell (1, 1), scalar 0.5149

parent `e2d26733e64ff96c` -> candidate `7492a142ce513467`

```diff
--- parent e2d26733e64ff96c
+++ candidate 7492a142ce513467
@@ -1,19 +1,19 @@
-You are to evaluate a proposal that aims to eliminate per‑action human approval for an industrial operational‑change gateway. Examine the provided material and issue **one** verdict—**sound**, **needs‑more‑evidence**, or **rejected**—followed by a brief justification (1‑3 sentences).
+You are to judge a proposal that seeks to remove per‑action human approval from an industrial operational‑change gateway. After reviewing the supplied documentation, output **exactly one** verdict—**sound**, **needs‑more‑evidence**, or **rejected**—followed by a brief justification (1‑3 sentences) that references the numbered checklist items.
 
-**Evaluation checklist (Section 8, Strategy C & Section 9 anti‑patterns)**  
-1. **Real‑world testing** – Evidence of end‑to‑end trials or production‑scale simulations.  
-2. **Failure‑mode / risk analysis** – Documented failure modes, likelihoods, and mitigations.  
-3. **Immutable audit trail** – Tamper‑evident logs or provenance for every automated decision.  
-4. **Human‑parity evidence** – Data showing the automation meets or exceeds a qualified human’s decisions.  
-5. **Anti‑pattern screening** – No presence of prohibited patterns (e.g., single point of failure, opaque black‑box logic, lack of rollback, unbounded escalation).
+**Checklist (derived from Section 8 Strategy C and Section 9 anti‑patterns)**  
+1. **Real‑world validation** – presence of end‑to‑end trials or production‑scale simulations.  
+2. **Failure‑mode & risk analysis** – documented failure scenarios, their likelihood, and mitigation measures.  
+3. **Immutable auditability** – tamper‑evident logs or provenance for every automated decision.  
+4. **Human‑parity evidence** – data showing the automation meets or exceeds the performance of a qualified human operator.  
+5. **Anti‑pattern exclusion** – no prohibited patterns such as single points of failure, opaque black‑box logic, missing rollback, or unbounded escalation.
 
-**Verdict criteria**  
-- **sound** – All five items are fully satisfied and no anti‑pattern is found.  
-- **needs‑more‑evidence** – Most items are met, but at least one critical element (testing, auditability, or risk analysis) is missing or insufficient.  
-- **rejected** – Any anti‑pattern is detected, or a fundamental flaw (no testing, no audit trail, clear safety violation) exists.
+**Decision rules**  
+- **sound** – all five items are fully satisfied and no anti‑pattern is present.  
+- **needs‑more‑evidence** – most items are met, but at least one critical element (validation, risk analysis, auditability, or parity) is missing or inadequate.  
+- **rejected** – any anti‑pattern is detected, or a fundamental flaw (e.g., no testing, no audit trail, obvious safety violation) exists.
 
 **Output format**  
-1. First line: exactly one of the three verdict words.  
-2. Subsequent line(s): concise justification that cites the relevant checklist numbers (e.g., “Missing #2 risk analysis” or “All criteria #1‑5 satisfied”).
+1. First line: the verdict word exactly as listed.  
+2. Subsequent line(s): a concise justification that cites the relevant checklist numbers (e.g., “Missing #2 risk analysis” or “All criteria #1‑5 satisfied”).
 
-Begin your assessment now.+Proceed with the assessment now.
```

### Island 0, cell (0, 2), scalar 0.4743

parent `4c7c5a49132aba89` -> candidate `f624493ab82de941`

```diff
--- parent 4c7c5a49132aba89
+++ candidate f624493ab82de941
@@ -1,22 +1,22 @@
-You are tasked with judging a proposal that seeks to remove per‑action human approval for an industrial operational‑change gateway. Read the provided material and output a single verdict—**sound**, **needs‑more‑evidence**, or **rejected**—followed by a brief justification (1‑3 sentences).
+You will evaluate a proposal that wants to drop per‑action human approval for an industrial operational‑change gateway. After reviewing the supplied documentation, output **exactly one** of the three verdict words—**sound**, **needs‑more‑evidence**, or **rejected**—followed by a short justification (1‑3 sentences) that cites the numbered criteria.
 
-**Assessment checklist (derived from Section 8, Strategy C and Section 9 anti‑patterns)**  
+**Evaluation checklist (Section 8, Strategy C + Section 9 anti‑patterns)**  
 
-1. **Real‑world testing** – Does the team show end‑to‑end trials or production‑scale simulations?  
-2. **Failure‑mode analysis** – Is there a documented list of possible failures, their likelihood, and mitigation strategies?  
+1. **Real‑world validation** – Does the team provide end‑to‑end trials or production‑scale simulations?  
+2. **Failure‑mode & risk analysis** – Is there a documented list of failure modes, their likelihood, and mitigation measures?  
 3. **Immutable audit trail** – Are all automated decisions recorded in tamper‑evident logs or provenance metadata?  
-4. **Human‑parity evidence** – Are results provided that demonstrate the automation matches or exceeds a qualified human operator’s decisions?  
-5. **Anti‑pattern screening** – Confirm the proposal contains none of the prohibited patterns (e.g., single point of failure, opaque black‑box logic, lack of rollback, unbounded escalation).
+4. **Human‑parity evidence** – Are results shown that the automation performs at least as well as a qualified human operator?  
+5. **Anti‑pattern screening** – Verify that none of the prohibited patterns appear (e.g., single point of failure, opaque black‑box logic, missing rollback, unbounded escalation).
 
 **Verdict rules**
 
-- **sound** – Every checklist item is satisfactorily addressed and no anti‑pattern is present.  
-- **needs‑more‑evidence** – The majority of items are met, but at least one critical element (testing depth, auditability, or risk analysis) is missing or insufficient.  
-- **rejected** – Any anti‑pattern is detected, or a fundamental flaw (no testing, no audit, clear safety violation) makes the proposal unacceptable.
+- **sound** – All five items are satisfactorily addressed and no anti‑pattern is found.  
+- **needs‑more‑evidence** – Most items are met, but at least one critical element (validation, risk analysis, auditability, or parity) is missing or insufficient.  
+- **rejected** – Any anti‑pattern is present, or a fundamental flaw (no testing, no audit trail, clear safety violation) exists, irrespective of the other items.
 
 **Output format**
 
-1. First line: exactly one of the three verdict words.  
-2. Subsequent line(s): a concise justification that cites the relevant checklist numbers (e.g., “Missing #2 risk analysis” or “All criteria #1‑5 satisfied”).
+1. **First line:** the verdict word exactly as listed.  
+2. **Next line(s):** a concise justification that references the relevant checklist numbers (e.g., “Missing #2 risk analysis” or “All criteria #1‑5 satisfied”).
 
-Begin your evaluation now.+Begin your assessment now.
```

## Migration

- island 0 -> island 1: cell (0, 0), scalar 0.8358, claimed=True
- island 1 -> island 2: cell (0, 1), scalar 0.8296, claimed=False
- island 2 -> island 3: cell (0, 1), scalar 0.8303, claimed=True
- island 3 -> island 0: cell (0, 1), scalar 0.8275, claimed=False

## Lesson retirement (dry run)

- Lesson 4: **kept** — precision 1.000 >= base 0.906
- Lesson 7: **kept** — never injected
- Lesson 6: **kept** — precision 0.732 vs base 0.757, only 0.3 sigma below
- Lesson 1: **kept** — no control group (standing tier: needs PHASE-4.md task 4.5 arm A)
- Lesson 5: **kept** — precision 0.994 >= base 0.510
- Lesson 3: **kept** — precision 0.896 >= base 0.629

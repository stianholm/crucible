# Generation 4 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31.0
- Prefix cache hit rate: 50.3%
- Aggregate throughput: 68.1 tok/s (69684 completion tokens / 1023.3s)

## Archive

- Island 0: coverage 8.3%, QD score 1.063, unique ancestors 2
- Island 1: coverage 11.1%, QD score 1.614, unique ancestors 2
- Island 2: coverage 8.3%, QD score 1.069, unique ancestors 1
- Island 3: coverage 8.3%, QD score 1.573, unique ancestors 1
- Cells newly claimed this generation: 2

## Quality

- Best scalar this generation: 0.3514
- Median scalar of newly-claimed: 0.3240

## Cost

- Budget: {'generation': 4, 'max_generations': 30, 'tokens_used_total': 1128665, 'max_tokens': 2000000, 'elapsed_s_total': 4313.5, 'generation_wall_s': 1023.3}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 0, cell (1, 2), scalar 0.3514

parent `06b6e346ce71a1ab` -> candidate `b0a32453d13b4091`

```diff
--- parent 06b6e346ce71a1ab
+++ candidate b0a32453d13b4091
@@ -1,20 +1,22 @@
-You are evaluating a proposal to relax per‑action human approval for an industrial operational‑change gateway action. Using the criteria from Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper, decide whether the case is **sound**, **needs‑more‑evidence**, or **rejected**.
+You are reviewing a request to waive per‑action human approval for an industrial operational‑change gateway. Apply the criteria from Section 8 (Strategy C, capability‑based opening) and ensure the proposal does **not** exhibit any anti‑patterns from Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-Assess the submission against the following checklist:
+**Checklist**
 
-1. **Empirical validation** – has the team performed realistic testing or simulation of the capability in the target environment?
-2. **Risk analysis** – are potential failure modes, safety impacts, and fallback strategies identified and addressed?
-3. **Auditability** – is there a clear, tamper‑evident log or trace that records the agent’s decisions and actions?
-4. **Human‑equivalence comparison** – does the evidence show that the autonomous decisions match or exceed the quality of a human operator in comparable scenarios?
-5. **Compliance with anti‑patterns** – does the proposal avoid the prohibited patterns from Section 9 (e.g., “no‑fallback”, “opaque decision‑making”, “unbounded escalation”)?
+1. **Empirical validation** – realistic testing or high‑fidelity simulation in the target environment is provided.
+2. **Risk analysis** – failure modes, safety impact, and fallback/rollback procedures are identified and mitigated.
+3. **Auditability** – an immutable, tamper‑evident log or trace of decisions and actions exists.
+4. **Human‑equivalence** – evidence shows autonomous performance meets or exceeds a human operator’s safety/quality in comparable scenarios.
+5. **Anti‑pattern compliance** – the proposal avoids all prohibited patterns from Section 9 (e.g., no‑fallback, opaque decision‑making, unbounded escalation, uncontrolled delegation, insufficient monitoring, single‑model reliance).
 
 **Decision rule**
 
-- If the submission meets most checklist items, demonstrates robust testing, and shows no anti‑pattern violations, label it **sound**.
-- If one or more critical items are missing or only partially addressed, but there is no fatal flaw, label it **needs‑more‑evidence**.
-- If any checklist item reveals a serious breach of safety, auditability, or an anti‑pattern, label it **rejected**.
+- **sound** – all checklist items are fully satisfied and no anti‑patterns are present.
+- **needs-more-evidence** – one or more items are missing or only partially addressed, but no fatal safety or anti‑pattern violation is found.
+- **rejected** – any item reveals a serious breach of safety, auditability, or a Section 9 anti‑pattern.
 
-**Output**  
-Provide the verdict (exactly one of the three labels) followed by a concise justification referencing the relevant checklist items and any anti‑pattern concerns.
+**Output format**
 
-Respond with your verdict and your reasoning.+1. First line: exactly one token – `sound`, `needs-more-evidence`, or `rejected`.
+2. Second line (optional but recommended): a brief justification (1‑3 sentences) citing the relevant checklist items and any anti‑pattern concerns.
+
+Produce only these two lines, with no additional headings or formatting.
```

### Island 1, cell (0, 2), scalar 0.2965

parent `678dcd87302a14f1` -> candidate `5b026214c3565f48`

```diff
--- parent 678dcd87302a14f1
+++ candidate 5b026214c3565f48
@@ -1,27 +1,20 @@
-You are evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Your task is to read the provided case and issue a single verdict—**sound**, **needs-more-evidence**, or **rejected**—followed by a concise justification.
+You are assessing a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway action. Read the entire submission (description, evidence, testing, risk analysis, audit‑trail, human‑baseline comparison) and produce **exactly two lines**:
 
-**Evaluation criteria (based on Section 8 and the anti‑patterns of Section 9):**
+1. **Verdict** – one of the three labels **sound**, **needs-more-evidence**, or **rejected** (lower‑case, no extra characters).  
+2. **Justification** – a brief explanation (no more than two sentences) stating the decisive factor(s) that led to your verdict.
 
-1. **Empirical validation**  
-   - Has the team performed realistic testing (e.g., pilot runs, simulations, or staged deployments) that demonstrates the system works reliably in the target environment?  
+**Evaluation checklist (all must be satisfied for a “sound” verdict):**
 
-2. **Risk & failure‑mode analysis**  
-   - Is there a documented assessment of what could go wrong, including worst‑case scenarios, mitigation strategies, and impact on safety, security, or continuity?  
-
-3. **Auditability & traceability**  
-   - Does the proposal include a robust audit trail (logs, timestamps, decision provenance) that allows post‑action review and accountability?  
-
-4. **Human‑baseline comparison**  
-   - Has the system’s decision‑making been benchmarked against qualified human operators, showing at least equivalent or superior performance on key metrics?  
-
-5. **Compliance with anti‑patterns (Section 9)**  
-   - Verify that the case does **not** exhibit any listed anti‑patterns (e.g., “over‑reliance on opaque AI”, “absence of fallback”, “single point of failure without redundancy”, etc.).  
+- **Empirical validation** – realistic testing (pilot, simulation, staged deployment) showing reliable operation in the target environment.  
+- **Risk & failure‑mode analysis** – documented hazards, worst‑case scenarios, mitigation strategies, and impact assessment for safety, security, and continuity.  
+- **Auditability & traceability** – complete audit trail (logs, timestamps, decision provenance) enabling post‑action review and accountability.  
+- **Human‑baseline comparison** – performance benchmarked against qualified human operators, demonstrating at least equivalent outcomes on key metrics.  
+- **Anti‑pattern compliance (Section 9)** – absence of any listed anti‑patterns (e.g., opaque AI reliance, no fallback, single point of failure, unmanaged privilege escalation).
 
 **Verdict rules**
 
-- **sound** – All five criteria are met satisfactorily; the evidence collectively demonstrates that relaxing approval is justified.  
-- **needs-more-evidence** – One or more criteria are partially addressed but lack sufficient depth, data, or clarity; the proposal is promising but not yet compelling.  
-- **rejected** – A critical failure is identified (e.g., missing auditability, unmitigated high‑risk failure mode, presence of a Section 9 anti‑pattern). The case should not proceed.
+- **sound** – every checklist item is fully addressed and no anti‑pattern is present.  
+- **needs-more-evidence** – one or more items are addressed only partially or lack sufficient detail, but no fatal anti‑pattern is found.  
+- **rejected** – a critical failure is identified (e.g., missing auditability, unmitigated high‑risk failure mode, or presence of a Section 9 anti‑pattern).
 
-**Output format (fixed elsewhere):**  
-Provide the verdict label first, then a brief rationale explaining which criteria drove your decision. Do not include any additional headings or formatting. +Follow the two‑line output format precisely; do not add headings, bullet points, or any other text. 
```


## Lesson retirement (dry run)

- Lesson 4: **kept** — precision 1.000 >= base 0.906
- Lesson 7: **kept** — never injected
- Lesson 6: **kept** — precision 0.732 vs base 0.757, only 0.3 sigma below
- Lesson 1: **kept** — no control group (standing tier: needs PHASE-4.md task 4.5 arm A)
- Lesson 5: **kept** — precision 0.994 >= base 0.510
- Lesson 3: **kept** — precision 0.896 >= base 0.629

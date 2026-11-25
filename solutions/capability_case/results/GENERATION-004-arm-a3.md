# Generation 4 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31.0
- Prefix cache hit rate: 48.8%
- Aggregate throughput: 68.8 tok/s (102538 completion tokens / 1489.3s)

## Archive

- Island 0: coverage 13.9%, QD score 2.525, unique ancestors 1
- Island 1: coverage 16.7%, QD score 2.626, unique ancestors 2
- Island 2: coverage 19.4%, QD score 2.920, unique ancestors 1
- Island 3: coverage 16.7%, QD score 3.114, unique ancestors 2
- Cells newly claimed this generation: 9

## Quality

- Best scalar this generation: 0.5102
- Median scalar of newly-claimed: 0.1212

## Cost

- Budget: {'generation': 4, 'max_generations': 30, 'tokens_used_total': 1408335, 'max_tokens': 2000000, 'elapsed_s_total': 5066.8, 'generation_wall_s': 1489.3}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 0, cell (1, 2), scalar 0.1212

parent `4c7c5a49132aba89` -> candidate `b680392e5baa5c75`

```diff
--- parent 4c7c5a49132aba89
+++ candidate b680392e5baa5c75
@@ -1,22 +1,24 @@
-You are tasked with judging a proposal that seeks to remove per‑action human approval for an industrial operational‑change gateway. Read the provided material and output a single verdict—**sound**, **needs‑more‑evidence**, or **rejected**—followed by a brief justification (1‑3 sentences).
+You are acting as a compliance evaluator for a request to drop per‑action human approval on an industrial operational‑change gateway. Examine the supplied evidence and issue **one** of the three decisions: **sound**, **needs‑more‑evidence**, or **rejected**. Follow the checklist below, then give a brief (1‑3 sentence) rationale that points to the specific checklist items that drove your choice.
 
-**Assessment checklist (derived from Section 8, Strategy C and Section 9 anti‑patterns)**  
+**Checklist (Section 8 – Strategy C & Section 9 anti‑patterns)**  
 
-1. **Real‑world testing** – Does the team show end‑to‑end trials or production‑scale simulations?  
-2. **Failure‑mode analysis** – Is there a documented list of possible failures, their likelihood, and mitigation strategies?  
-3. **Immutable audit trail** – Are all automated decisions recorded in tamper‑evident logs or provenance metadata?  
-4. **Human‑parity evidence** – Are results provided that demonstrate the automation matches or exceeds a qualified human operator’s decisions?  
-5. **Anti‑pattern screening** – Confirm the proposal contains none of the prohibited patterns (e.g., single point of failure, opaque black‑box logic, lack of rollback, unbounded escalation).
+| ID | Requirement |
+|----|--------------|
+| **C1** | **Real‑world validation** – evidence of end‑to‑end trials or production‑scale simulations. |
+| **C2** | **Failure‑mode & risk analysis** – documented failure scenarios, likelihoods, and mitigation plans. |
+| **C3** | **Immutable audit trail** – tamper‑evident logs or provenance data for every automated decision. |
+| **C4** | **Human‑parity proof** – quantitative/qualitative results showing the automation meets or exceeds a qualified human’s decisions. |
+| **C5** | **Anti‑pattern screening** – confirm the design avoids all prohibited patterns (e.g., single point of failure, opaque black‑box, lack of rollback, unbounded escalation). |
 
-**Verdict rules**
+**Decision matrix**
 
-- **sound** – Every checklist item is satisfactorily addressed and no anti‑pattern is present.  
-- **needs‑more‑evidence** – The majority of items are met, but at least one critical element (testing depth, auditability, or risk analysis) is missing or insufficient.  
-- **rejected** – Any anti‑pattern is detected, or a fundamental flaw (no testing, no audit, clear safety violation) makes the proposal unacceptable.
+* **sound** – All five items C1‑C5 are fully satisfied and no anti‑pattern is found.  
+* **needs‑more‑evidence** – Most items are addressed, but at least one critical element (C1, C2, C3, or C4) is missing, incomplete, or weak.  
+* **rejected** – Any anti‑pattern is present (C5) or a fundamental flaw (e.g., no testing, no audit, clear safety violation) makes the proposal unacceptable.
 
 **Output format**
 
-1. First line: exactly one of the three verdict words.  
-2. Subsequent line(s): a concise justification that cites the relevant checklist numbers (e.g., “Missing #2 risk analysis” or “All criteria #1‑5 satisfied”).
+1. First line: exactly the chosen verdict word (`sound`, `needs-more-evidence`, or `rejected`).  
+2. Following line(s): a concise justification that cites the relevant checklist IDs (e.g., “Missing C2 risk analysis” or “All criteria C1‑C5 satisfied”).
 
-Begin your evaluation now.+Proceed with the evaluation now.
```

### Island 0, cell (1, 2), scalar 0.1502

parent `4c7c5a49132aba89` -> candidate `e2d26733e64ff96c`

```diff
--- parent 4c7c5a49132aba89
+++ candidate e2d26733e64ff96c
@@ -1,22 +1,19 @@
-You are tasked with judging a proposal that seeks to remove per‑action human approval for an industrial operational‑change gateway. Read the provided material and output a single verdict—**sound**, **needs‑more‑evidence**, or **rejected**—followed by a brief justification (1‑3 sentences).
+You are to evaluate a proposal that aims to eliminate per‑action human approval for an industrial operational‑change gateway. Examine the provided material and issue **one** verdict—**sound**, **needs‑more‑evidence**, or **rejected**—followed by a brief justification (1‑3 sentences).
 
-**Assessment checklist (derived from Section 8, Strategy C and Section 9 anti‑patterns)**  
+**Evaluation checklist (Section 8, Strategy C & Section 9 anti‑patterns)**  
+1. **Real‑world testing** – Evidence of end‑to‑end trials or production‑scale simulations.  
+2. **Failure‑mode / risk analysis** – Documented failure modes, likelihoods, and mitigations.  
+3. **Immutable audit trail** – Tamper‑evident logs or provenance for every automated decision.  
+4. **Human‑parity evidence** – Data showing the automation meets or exceeds a qualified human’s decisions.  
+5. **Anti‑pattern screening** – No presence of prohibited patterns (e.g., single point of failure, opaque black‑box logic, lack of rollback, unbounded escalation).
 
-1. **Real‑world testing** – Does the team show end‑to‑end trials or production‑scale simulations?  
-2. **Failure‑mode analysis** – Is there a documented list of possible failures, their likelihood, and mitigation strategies?  
-3. **Immutable audit trail** – Are all automated decisions recorded in tamper‑evident logs or provenance metadata?  
-4. **Human‑parity evidence** – Are results provided that demonstrate the automation matches or exceeds a qualified human operator’s decisions?  
-5. **Anti‑pattern screening** – Confirm the proposal contains none of the prohibited patterns (e.g., single point of failure, opaque black‑box logic, lack of rollback, unbounded escalation).
+**Verdict criteria**  
+- **sound** – All five items are fully satisfied and no anti‑pattern is found.  
+- **needs‑more‑evidence** – Most items are met, but at least one critical element (testing, auditability, or risk analysis) is missing or insufficient.  
+- **rejected** – Any anti‑pattern is detected, or a fundamental flaw (no testing, no audit trail, clear safety violation) exists.
 
-**Verdict rules**
+**Output format**  
+1. First line: exactly one of the three verdict words.  
+2. Subsequent line(s): concise justification that cites the relevant checklist numbers (e.g., “Missing #2 risk analysis” or “All criteria #1‑5 satisfied”).
 
-- **sound** – Every checklist item is satisfactorily addressed and no anti‑pattern is present.  
-- **needs‑more‑evidence** – The majority of items are met, but at least one critical element (testing depth, auditability, or risk analysis) is missing or insufficient.  
-- **rejected** – Any anti‑pattern is detected, or a fundamental flaw (no testing, no audit, clear safety violation) makes the proposal unacceptable.
-
-**Output format**
-
-1. First line: exactly one of the three verdict words.  
-2. Subsequent line(s): a concise justification that cites the relevant checklist numbers (e.g., “Missing #2 risk analysis” or “All criteria #1‑5 satisfied”).
-
-Begin your evaluation now.+Begin your assessment now.
```

### Island 0, cell (0, 2), scalar 0.1913

parent `4c7c5a49132aba89` -> candidate `9f4f557ed1e2864c`

```diff
--- parent 4c7c5a49132aba89
+++ candidate 9f4f557ed1e2864c
@@ -1,22 +1,22 @@
-You are tasked with judging a proposal that seeks to remove per‑action human approval for an industrial operational‑change gateway. Read the provided material and output a single verdict—**sound**, **needs‑more‑evidence**, or **rejected**—followed by a brief justification (1‑3 sentences).
+You are evaluating a proposal that aims to eliminate per‑action human approval for an industrial operational‑change gateway. After reviewing the supplied documentation, issue **exactly one** of the three verdicts: **sound**, **needs‑more‑evidence**, or **rejected**, then supply a brief justification (1‑3 sentences) that cites the relevant assessment points.
 
-**Assessment checklist (derived from Section 8, Strategy C and Section 9 anti‑patterns)**  
+**Evaluation criteria (Section 8, Strategy C + Section 9 anti‑patterns)**  
 
-1. **Real‑world testing** – Does the team show end‑to‑end trials or production‑scale simulations?  
-2. **Failure‑mode analysis** – Is there a documented list of possible failures, their likelihood, and mitigation strategies?  
-3. **Immutable audit trail** – Are all automated decisions recorded in tamper‑evident logs or provenance metadata?  
-4. **Human‑parity evidence** – Are results provided that demonstrate the automation matches or exceeds a qualified human operator’s decisions?  
-5. **Anti‑pattern screening** – Confirm the proposal contains none of the prohibited patterns (e.g., single point of failure, opaque black‑box logic, lack of rollback, unbounded escalation).
+1. **Real‑world validation** – Evidence of end‑to‑end trials or production‑scale simulations.  
+2. **Failure‑mode & risk analysis** – Documented failure scenarios, likelihood estimates, and mitigation plans.  
+3. **Immutable auditability** – Tamper‑evident logs or provenance data for every automated decision.  
+4. **Human‑parity evidence** – Quantitative or qualitative proof that the automation meets or exceeds qualified human performance.  
+5. **Anti‑pattern screening** – Absence of prohibited patterns such as single points of failure, opaque black‑box logic, missing rollback, or unbounded escalation.
 
-**Verdict rules**
+**Verdict determination**
 
-- **sound** – Every checklist item is satisfactorily addressed and no anti‑pattern is present.  
-- **needs‑more‑evidence** – The majority of items are met, but at least one critical element (testing depth, auditability, or risk analysis) is missing or insufficient.  
-- **rejected** – Any anti‑pattern is detected, or a fundamental flaw (no testing, no audit, clear safety violation) makes the proposal unacceptable.
+- **sound** – All five criteria are fully satisfied and no anti‑pattern is detected.  
+- **needs‑more‑evidence** – Most criteria are met, but at least one critical element (validation, risk analysis, auditability, or parity) is missing or inadequately described.  
+- **rejected** – Any anti‑pattern is present, or a fundamental flaw (e.g., no testing, no audit trail, clear safety violation) makes the proposal unacceptable.
 
 **Output format**
 
-1. First line: exactly one of the three verdict words.  
-2. Subsequent line(s): a concise justification that cites the relevant checklist numbers (e.g., “Missing #2 risk analysis” or “All criteria #1‑5 satisfied”).
+1. **First line:** the verdict word exactly as listed.  
+2. **Subsequent line(s):** a concise justification referencing the checklist numbers (e.g., “Missing #2 risk analysis” or “All criteria #1‑5 satisfied”).
 
-Begin your evaluation now.+Proceed with the assessment now.
```

### Island 1, cell (0, 3), scalar 0.0860

parent `6c5ea1c30111c0fb` -> candidate `7a1ebf820e28d74a`

```diff
--- parent 6c5ea1c30111c0fb
+++ candidate 7a1ebf820e28d74a
@@ -1,24 +1,25 @@
-You are tasked with judging a capability case that proposes to remove per‑action human approval for an industrial operational‑change gateway. After reviewing the submission, output **exactly one** of the three labels **sound**, **needs‑more‑evidence**, or **rejected**, followed by a short justification.
+You are to assess a capability case that proposes removing per‑action human approval for an industrial operational‑change gateway. After reading the submission, output **exactly one** verdict label—`sound`, `needs‑more‑evidence`, or `rejected`—followed by a single‑sentence justification.
 
-### Evaluation checklist
-1. **Real‑world testing** – Does the case include repeatable in‑situ trials, high‑fidelity simulation, or a staged rollout that proves safe operation?
-2. **Failure‑mode analysis** – Is there a documented list of possible failures, their probabilities, and concrete mitigation or containment steps?
-3. **Auditability** – Is an immutable log of inputs, decisions, and outcomes provided for post‑event review?
+#### Checklist (all must be considered)
+
+1. **Real‑world testing** – Does the case provide repeatable in‑situ trials, high‑fidelity simulation, or a staged rollout that demonstrates safe operation?
+2. **Failure‑mode analysis** – Is there a catalog of possible failures, their estimated probabilities, and concrete mitigation/containment steps?
+3. **Auditability** – Is an immutable log of inputs, decisions, and outcomes supplied for post‑event review?
 4. **Human‑parity evidence** – Is there quantitative or qualitative data showing the system’s decisions match those of a qualified human in the same scenario?
-5. **Section 9 anti‑patterns** – Are any of the prohibited patterns (e.g., no fallback, unbounded escalation, opaque decision logic, missing manual override, etc.) present?
+5. **Section 9 anti‑patterns** – Are any prohibited patterns present (e.g., no fallback, unbounded escalation, opaque decision logic, missing manual override, etc.)?
 
-### Verdict rules
-- **rejected** – If any anti‑pattern from item 5 is found, or the overall safety risk is unacceptable. This overrides all other items.
-- **sound** – Items 1‑4 are each fully satisfied **and** no anti‑patterns are detected.
+#### Verdict hierarchy
+- **rejected** – Any anti‑pattern from item 5 is detected **or** the overall safety risk is judged unacceptable. This overrides all other items.
+- **sound** – Items 1‑4 are each fully satisfied **and** no anti‑patterns are found.
 - **needs‑more‑evidence** – No anti‑patterns appear, but at least one of items 1‑4 is missing, incomplete, or insufficiently justified.
 
-### Output format
+#### Output template
 ```
 <verdict label>
-Justification: <brief reason referencing the relevant checklist items>
+Justification: <brief reason referencing checklist numbers or specific anti‑patterns>
 ```
 *Example*  
 `sound`  
 `Justification: items 1‑4 all met; no anti‑patterns detected.`
 
-Provide the verdict on the first line and a concise, one‑sentence justification on the second line, directly citing the checklist numbers or specific anti‑patterns as appropriate.+Provide the verdict on the first line and a concise, one‑sentence justification on the second line, citing the relevant checklist items or anti‑patterns.
```

### Island 1, cell (0, 4), scalar 0.5102

parent `d127c05bcd01ec7b` -> candidate `98af764911b8df0d`

```diff
--- parent d127c05bcd01ec7b
+++ candidate 98af764911b8df0d
@@ -1,18 +1,25 @@
-You are assessing a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway. Use the **Section 8 (Strategy C) criteria** and the **Section 9 anti‑patterns** from the IT/OT‑boundary‑as‑architecture whitepaper to reach a verdict.
+You are evaluating a proposal that wants to eliminate per‑action human approval for an industrial operational‑change gateway. Apply the **Section 8 (Strategy C)** requirements and screen for any **Section 9 anti‑patterns** described in the IT/OT‑boundary‑as‑architecture whitepaper.
 
-**Assessment criteria**
-1. **Representative testing** – Does the submission include realistic pilots or simulations that prove the system works safely in the intended environment?  
-2. **Failure‑mode analysis** – Are possible adverse outcomes identified, their likelihood quantified, and mitigation measures described?  
-3. **Auditability** – Is there a tamper‑evident log that records inputs, decisions, and outcomes for later review?  
-4. **Human‑parity evidence** – Is there data showing the system’s decisions match those a qualified human would make under the same conditions?  
-5. **Section 9 anti‑patterns** – Does the design contain any red‑flags such as “no fallback”, “unbounded escalation”, “opaque decision logic”, “missing manual override”, or similar?  
+**Section 8 requirements**
+1. **Real‑world evidence** – Does the submission contain pilots, staged roll‑outs, or high‑fidelity simulations that demonstrate safe operation in the target environment?  
+2. **Failure‑mode treatment** – Are failure scenarios listed, their probabilities quantified, and concrete mitigation or containment steps defined?  
+3. **Audit trail** – Is there an immutable, tamper‑evident log of inputs, decisions, and outcomes that can be reviewed after the fact?  
+4. **Human‑parity proof** – Is there data (quantitative or qualitative) showing the system’s decisions match those a qualified human would make under identical conditions?
 
-**Verdict logic**
-- **REJECTED** – If any anti‑pattern from criterion 5 is present, or if a fundamental safety risk is evident, the case is rejected outright (this overrides all other criteria).  
-- **SOUND** – All of criteria 1‑4 are fully satisfied **and** no anti‑patterns are detected.  
-- **NEEDS‑MORE‑EVIDENCE** – No anti‑patterns are found, but at least one of criteria 1‑4 is missing, incomplete, or insufficiently justified.
+**Section 9 anti‑patterns (must be absent)**
+- No fallback or safe‑state mechanism  
+- Unbounded escalation or uncontrolled propagation  
+- Opaque or undocumented decision logic  
+- Missing manual override capability  
+- Any other pattern identified in the whitepaper as a safety‑critical flaw
+
+**Decision rules**
+- **REJECTED** – If any anti‑pattern is present, or a clear, unacceptable safety risk is evident. This overrides all other considerations.  
+- **SOUND** – All four Section 8 requirements are fully satisfied **and** no anti‑patterns are detected.  
+- **NEEDS‑MORE‑EVIDENCE** – No anti‑patterns are found, but at least one of the Section 8 requirements is missing, incomplete, or insufficiently substantiated.
 
 **Output format**
-Write the chosen label (**SOUND**, **NEEDS‑MORE‑EVIDENCE**, or **REJECTED**) on the first line, followed by a concise justification (1‑2 sentences) that cites the relevant criteria numbers or specific anti‑patterns.
+1. First line: the chosen label exactly as **SOUND**, **NEEDS‑MORE‑EVIDENCE**, or **REJECTED**.  
+2. Second line: a brief (one‑sentence) justification that references the relevant requirement numbers (1‑4) or names the specific anti‑pattern(s) that led to the decision.
 
-Proceed with your evaluation.+Proceed with the assessment.
```

### Island 2, cell (0, 5), scalar 0.0923

parent `bb577be66eaeec92` -> candidate `a5ab3a3f867d8c61`

```diff
--- parent bb577be66eaeec92
+++ candidate a5ab3a3f867d8c61
@@ -1,26 +1,21 @@
-You are to judge a capability case that proposes removing per‑action human approval for an industrial operational‑change gateway.
+You are to evaluate a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway.
 
-**Goal**  
-Examine the supplied evidence and produce **exactly two lines**:
+**Output requirement** – Produce **exactly two lines**, nothing else (no markdown, no extra blanks):
 
 1. `Verdict: <sound|needs-more-evidence|rejected>`
-2. `Reason: <brief justification that cites at least one checklist item>`
+2. `Reason: <concise justification that cites at least one checklist item by number or short name>`
 
-No other text, blanks, or punctuation may appear.
-
-**Verdict meanings**
-- **sound** – evidence shows the risk is fully understood, mitigated, and on par with qualified human decisions.
-- **needs-more-evidence** – one or more required elements are missing or insufficient.
-- **rejected** – a critical flaw (e.g., an anti‑pattern, lack of auditability, or an unacceptable failure mode) makes the relaxation unsafe.
+**Decision rules**
+1. If any Section 9 anti‑pattern appears, the verdict is **rejected**.
+2. Otherwise, if **all** six checklist items are satisfied, the verdict is **sound**.
+3. If the proposal fails to meet every checklist item but has no anti‑pattern, the verdict is **needs-more-evidence**.
 
 **Checklist (must be considered)**
-1. **Real‑world testing** – functional, integration, and stress tests that reflect production use.
-2. **Failure‑mode analysis** – identification of plausible errors with defined mitigations or fall‑backs.
-3. **Auditability** – tamper‑evident logs or traces that can be inspected post‑hoc.
-4. **Human‑parity comparison** – quantitative or qualitative evidence that the system matches qualified human performance.
+1. **Real‑world testing** – functional, integration, and stress tests that mirror production.
+2. **Failure‑mode analysis** – identified error scenarios with mitigations or fall‑backs.
+3. **Auditability** – tamper‑evident logs or traces that can be inspected after the fact.
+4. **Human‑parity comparison** – evidence the system matches qualified human performance.
 5. **Anti‑pattern compliance** – absence of any Section 9 anti‑patterns (e.g., “no‑fallback”, “unbounded autonomy”, “opaque decision logic”).
 6. **Risk‑level alignment** – the relaxation does not raise the risk tier beyond what Section 8 allows for Strategy C.
 
-When forming your decision, reference the relevant checklist items (by number or short phrase) in the Reason line.
-
-Proceed with the assessment now.+When writing the Reason line, refer to the relevant checklist item(s) (e.g., “item 3”, “auditability”, “risk‑level alignment”). Proceed with the assessment now.
```

### Island 2, cell (1, 2), scalar 0.1172

parent `bb577be66eaeec92` -> candidate `f5dbf2ba664925ea`

```diff
--- parent bb577be66eaeec92
+++ candidate f5dbf2ba664925ea
@@ -1,26 +1,28 @@
-You are to judge a capability case that proposes removing per‑action human approval for an industrial operational‑change gateway.
+You will evaluate a capability case that seeks to eliminate per‑action human approval for an industrial operational‑change gateway.
 
-**Goal**  
-Examine the supplied evidence and produce **exactly two lines**:
+**Output requirement** – Produce **exactly two lines**, nothing else (no markdown, no extra spaces):
 
 1. `Verdict: <sound|needs-more-evidence|rejected>`
-2. `Reason: <brief justification that cites at least one checklist item>`
+2. `Reason: <concise justification that cites at least one checklist item>`  
 
-No other text, blanks, or punctuation may appear.
+The Reason line must be a single sentence (≤ 200 characters) and reference checklist items by number (e.g., “item 3”) or by their short title.
 
-**Verdict meanings**
-- **sound** – evidence shows the risk is fully understood, mitigated, and on par with qualified human decisions.
-- **needs-more-evidence** – one or more required elements are missing or insufficient.
-- **rejected** – a critical flaw (e.g., an anti‑pattern, lack of auditability, or an unacceptable failure mode) makes the relaxation unsafe.
+**Verdict definitions**  
+- **sound** – the evidence demonstrates full understanding of risk, appropriate mitigation, and parity with qualified human decisions.  
+- **needs-more-evidence** – one or more required elements are absent or insufficient, but no fatal flaw is found.  
+- **rejected** – a critical problem exists (e.g., a Section 9 anti‑pattern, missing audit trail, or an unacceptable failure mode) that makes the relaxation unsafe.
 
-**Checklist (must be considered)**
-1. **Real‑world testing** – functional, integration, and stress tests that reflect production use.
-2. **Failure‑mode analysis** – identification of plausible errors with defined mitigations or fall‑backs.
-3. **Auditability** – tamper‑evident logs or traces that can be inspected post‑hoc.
-4. **Human‑parity comparison** – quantitative or qualitative evidence that the system matches qualified human performance.
-5. **Anti‑pattern compliance** – absence of any Section 9 anti‑patterns (e.g., “no‑fallback”, “unbounded autonomy”, “opaque decision logic”).
-6. **Risk‑level alignment** – the relaxation does not raise the risk tier beyond what Section 8 allows for Strategy C.
+**Checklist (must be considered)**  
+1. **Real‑world testing** – functional, integration, and stress tests that reflect production use.  
+2. **Failure‑mode analysis** – identified error scenarios with defined mitigations or fall‑backs.  
+3. **Auditability** – tamper‑evident logs or traces that can be inspected after the fact.  
+4. **Human‑parity comparison** – quantitative or qualitative proof that the system matches qualified human performance.  
+5. **Anti‑pattern compliance** – absence of any Section 9 anti‑patterns (e.g., “no‑fallback”, “unbounded autonomy”, “opaque decision logic”).  
+6. **Risk‑level alignment** – the relaxation does not raise the risk tier beyond what Section 8 permits for Strategy C.
 
-When forming your decision, reference the relevant checklist items (by number or short phrase) in the Reason line.
+**Decision flow**  
+- If any anti‑pattern (item 5) is present, output **rejected**.  
+- Else if all six items are adequately addressed, output **sound**.  
+- Otherwise output **needs-more-evidence**.
 
-Proceed with the assessment now.+Assess the supplied evidence now and emit the two‑line verdict.
```

### Island 2, cell (0, 4), scalar 0.0536

parent `bb577be66eaeec92` -> candidate `bcba5c01696b3162`

```diff
--- parent bb577be66eaeec92
+++ candidate bcba5c01696b3162
@@ -1,26 +1,31 @@
-You are to judge a capability case that proposes removing per‑action human approval for an industrial operational‑change gateway.
+You are to evaluate a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway.
 
-**Goal**  
-Examine the supplied evidence and produce **exactly two lines**:
+**Task**  
+Read the provided evidence and output **exactly two lines**, nothing else:
 
-1. `Verdict: <sound|needs-more-evidence|rejected>`
-2. `Reason: <brief justification that cites at least one checklist item>`
+```
+Verdict: <sound|needs-more-evidence|rejected>
+Reason: <brief justification that references at least one checklist item>
+```
 
-No other text, blanks, or punctuation may appear.
+**Verdict definitions**
+- **sound** – the case demonstrates full understanding of risk, effective mitigation, and performance comparable to qualified humans.
+- **needs-more-evidence** – one or more required elements are missing or insufficient.
+- **rejected** – a show‑stopper such as an anti‑pattern, lack of auditability, or an unacceptable failure mode is present.
 
-**Verdict meanings**
-- **sound** – evidence shows the risk is fully understood, mitigated, and on par with qualified human decisions.
-- **needs-more-evidence** – one or more required elements are missing or insufficient.
-- **rejected** – a critical flaw (e.g., an anti‑pattern, lack of auditability, or an unacceptable failure mode) makes the relaxation unsafe.
+**Decision hierarchy**
+1. If any **Section 9 anti‑pattern** is detected, the verdict is **rejected**.
+2. Otherwise, if **all six checklist items** are satisfactorily addressed, the verdict is **sound**.
+3. In all other situations, the verdict is **needs-more-evidence**.
 
 **Checklist (must be considered)**
-1. **Real‑world testing** – functional, integration, and stress tests that reflect production use.
-2. **Failure‑mode analysis** – identification of plausible errors with defined mitigations or fall‑backs.
-3. **Auditability** – tamper‑evident logs or traces that can be inspected post‑hoc.
-4. **Human‑parity comparison** – quantitative or qualitative evidence that the system matches qualified human performance.
-5. **Anti‑pattern compliance** – absence of any Section 9 anti‑patterns (e.g., “no‑fallback”, “unbounded autonomy”, “opaque decision logic”).
-6. **Risk‑level alignment** – the relaxation does not raise the risk tier beyond what Section 8 allows for Strategy C.
+1. **Real‑world testing** – functional, integration, and stress tests that mirror production use.  
+2. **Failure‑mode analysis** – identification of plausible errors together with mitigations or fallback procedures.  
+3. **Auditability** – tamper‑evident logs or traces that can be reviewed after the fact.  
+4. **Human‑parity comparison** – quantitative or qualitative evidence that the system matches qualified human performance.  
+5. **Anti‑pattern compliance** – confirmation that no Section 9 anti‑patterns (e.g., “no‑fallback”, “unbounded autonomy”, “opaque decision logic”) are present.  
+6. **Risk‑level alignment** – the relaxation does not elevate the risk tier beyond what Section 8 permits for Strategy C.
 
-When forming your decision, reference the relevant checklist items (by number or short phrase) in the Reason line.
+When writing the **Reason** line, name the checklist item(s) that drove your decision (e.g., “fails item 3: auditability missing” or “satisfies items 1‑4”).  
 
 Proceed with the assessment now.
```

### Island 3, cell (0, 4), scalar 0.1751

parent `d8a41b7a5f720727` -> candidate `e6b7bc97761c430c`

```diff
--- parent d8a41b7a5f720727
+++ candidate e6b7bc97761c430c
@@ -1,22 +1,22 @@
-You are reviewing a capability case that seeks to waive the per‑action human‑approval requirement for an industrial operational‑change gateway action. Judge the case according to the criteria in **Section 8 (Strategy C, capability‑based opening)** and verify that none of the **Section 9 anti‑patterns** are present.
+You are evaluating a capability case that proposes to waive the per‑action human‑approval step for an industrial operational‑change gateway. Your judgment must conform to **Section 8 (Strategy C – capability‑based opening)** and ensure that **none of the Section 9 anti‑patterns** are present.
 
-**Evidence categories to verify**
+**Evidence items to check**
 
-1. **Empirical validation** – realistic end‑to‑end or pilot testing (including edge cases) in the intended environment.  
-2. **Failure‑mode & risk analysis** – documented possible failures, worst‑case impacts, and mitigation or fallback procedures.  
-3. **Auditability & traceability** – tamper‑evident logs or traces that capture decisions, actions, and context for post‑event review.  
-4. **Human‑equivalence comparison** – quantitative or qualitative evidence that the automated decisions match or exceed those of a qualified human operator.  
-5. **Residual risk assessment** – clear articulation of remaining risk, its safety/security/continuity impact, and justification that the risk level is acceptable under policy.  
-6. **Anti‑pattern compliance** – confirmation that no Section 9 anti‑patterns (e.g., black‑box automation without observability, single point of failure, lack of manual override) appear.
+1. **Empirical validation** – end‑to‑end or pilot testing in the actual environment, including normal and edge‑case scenarios.  
+2. **Failure‑mode & risk analysis** – documented possible failures, worst‑case impacts, and concrete mitigation or fallback measures.  
+3. **Auditability & traceability** – tamper‑evident logs or traces that capture every automated decision, its context, and rationale for post‑event review.  
+4. **Human‑equivalence** – quantitative or qualitative proof that the automation matches or exceeds the performance of a qualified human operator.  
+5. **Residual risk assessment** – clear description of remaining risk, its safety/security/continuity impact, and justification that the risk is acceptable under policy.  
+6. **Anti‑pattern compliance** – explicit confirmation that no Section 9 anti‑patterns (e.g., black‑box automation, single point of failure, lack of manual override) are present.
 
-**Decision rules**
+**Decision rubric**
 
-- **sound** – all six categories are substantively satisfied, no anti‑pattern is detected, and residual risk is demonstrably acceptable.  
-- **needs-more-evidence** – one or more critical categories are missing, incomplete, or weak, but no fatal anti‑pattern or unmitigated high‑impact risk is present.  
-- **rejected** – any category contains a serious deficiency (e.g., no testing, no audit trail, unmitigated high‑impact risk) or any Section 9 anti‑pattern is identified.
+- **sound** – all six items are substantively satisfied, no anti‑pattern is found, and the residual risk is demonstrably acceptable.  
+- **needs‑more‑evidence** – one or more items are missing, incomplete, or weak, but there is no fatal anti‑pattern or unmitigated high‑impact risk.  
+- **rejected** – any item contains a critical deficiency (e.g., no testing, no audit trail, unmitigated high‑impact risk) or any Section 9 anti‑pattern is identified.
 
-**Response format**
+**Output requirement**
 
-Output **exactly one** of the labels **sound**, **needs-more-evidence**, or **rejected**, followed by a brief (one‑sentence) justification that cites the relevant evidence categories and notes any anti‑pattern concerns.
+Print **exactly one** of the labels `sound`, `needs-more-evidence`, or `rejected`, followed by a single‑sentence justification that cites the relevant evidence items (and any anti‑pattern, if applicable).
 
 Proceed with the assessment now.
```


## Lesson retirement (dry run)

- Lesson 4: **kept** — precision 1.000 >= base 0.906
- Lesson 7: **kept** — never injected
- Lesson 6: **kept** — precision 0.732 vs base 0.757, only 0.3 sigma below
- Lesson 1: **kept** — no control group (standing tier: needs PHASE-4.md task 4.5 arm A)
- Lesson 5: **kept** — precision 0.994 >= base 0.510
- Lesson 3: **kept** — precision 0.896 >= base 0.629

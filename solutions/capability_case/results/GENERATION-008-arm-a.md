# Generation 8 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31.0
- Prefix cache hit rate: 44.2%
- Aggregate throughput: 287.9 tok/s (111189 completion tokens / 386.2s)

## Archive

- Island 0: coverage 13.9%, QD score 2.803, unique ancestors 3
- Island 1: coverage 16.7%, QD score 3.987, unique ancestors 2
- Island 2: coverage 11.1%, QD score 2.031, unique ancestors 2
- Island 3: coverage 8.3%, QD score 2.065, unique ancestors 1
- Cells newly claimed this generation: 8

## Quality

- Best scalar this generation: 0.5125
- Median scalar of newly-claimed: 0.5043

## Cost

- Budget: {'generation': 8, 'max_generations': 30, 'tokens_used_total': 2271012, 'max_tokens': 2000000, 'elapsed_s_total': 6628.1, 'generation_wall_s': 386.2}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 0, cell (0, 2), scalar 0.5017

parent `910e3e2dd8f08fc4` -> candidate `f58e531b98350563`

```diff
--- parent 910e3e2dd8f08fc4
+++ candidate f58e531b98350563
@@ -1,29 +1,26 @@
-You are reviewing a proposal that seeks to remove the per‑action human‑approval requirement for an industrial operational‑change gateway.
+You are evaluating a proposal that asks to eliminate the per‑action human‑approval step for an industrial operational‑change gateway.
 
-**Evaluation criteria (based on Section 8 – Strategy C and Section 9 – anti‑patterns)**
+**Evidence criteria (Section 8 – Strategy C)**  
+1. **Validated performance** – sandbox, pilot, or production‑mirrored tests that show reliable autonomous decision‑making.  
+2. **Risk analysis & mitigation** – documented failure modes together with concrete safety, security, and compliance safeguards (e.g., safe‑state fallback, human‑override).  
+3. **Auditability** – immutable logs or other artefacts that allow reconstruction of each autonomous decision, its inputs, and its outcome.  
+4. **Human‑level equivalence** – quantitative or qualitative evidence that the system’s decisions meet or exceed those of qualified humans in comparable scenarios.  
+5. **No prohibited anti‑patterns** – the submission must not exhibit any pattern banned in Section 9 (e.g., removing human fallback, eliminating traceability, granting unchecked autonomy to safety‑critical functions).
 
-1. **Validated performance** – evidence from sandbox, pilot, or production‑mirrored testing showing the system makes reliable autonomous decisions.  
-2. **Risk analysis & mitigation** – a documented list of plausible failure modes together with concrete safeguards for safety, security and compliance.  
-3. **Traceability / auditability** – logs or other artefacts that enable reconstruction of every autonomous decision, its inputs and its outcome.  
-4. **Human‑level equivalence** – quantitative or qualitative comparison demonstrating that the system’s decisions meet or exceed those of qualified humans in the same scenarios.  
-5. **Absence of disallowed anti‑patterns** – the proposal must not contain any pattern prohibited in Section 9 (e.g., removing fallback to humans, eliminating traceability, granting unchecked autonomy to safety‑critical functions, etc.).
-
-**Decision rules**
-
+**Decision logic**  
 - **sound** – all five criteria are fully satisfied and no anti‑pattern is present.  
 - **needs‑more‑evidence** – one or more criteria are missing or only partially addressed, and no anti‑pattern is detected.  
-- **rejected** – any listed anti‑pattern is present **or** the evidence reveals an unmitigated safety, security, or compliance risk.
+- **rejected** – any anti‑pattern is present **or** the evidence shows an unmitigated safety, security, or compliance risk.
 
-**Required output**
-
-- **Line 1:** exactly `sound`, `needs‑more‑evidence`, or `rejected` (no extra spaces or punctuation).  
-- **Line 2 onward:** a brief justification (1‑3 short sentences) that directly references the relevant criterion(ia). Do **not** use headings, bullet points, or any additional text.
+**Output format**  
+1. **Line 1:** write exactly `sound`, `needs‑more‑evidence`, or `rejected` (no extra spaces or punctuation).  
+2. **Line 2 onward:** provide a brief justification (1‑3 short sentences). Reference the relevant criterion number(s) or the specific anti‑pattern that drove the decision. Do not use headings, bullet points, or any additional text.
 
 *Example*
 
 ```
 sound
-The case includes a full‑scale pilot with 96 % agreement to human operators, complete audit logs, and avoids every prohibited anti‑pattern.
+The case includes full‑scale pilot data (criterion 1) with 96 % agreement to human operators, complete audit logs (criterion 3), and no prohibited anti‑patterns.
 ```
 
-Read the submission, apply the criteria, and produce the verdict followed by the concise justification.+Read the submission, apply the criteria, and output the verdict followed by the concise justification.
```

### Island 1, cell (0, 3), scalar 0.5024

parent `0a1cba46dc06071a` -> candidate `4cdd1d022e2173af`

```diff
--- parent 0a1cba46dc06071a
+++ candidate 4cdd1d022e2173af
@@ -1,21 +1,21 @@
-You act as an auditor who must decide whether a proposal to drop per‑action human approval for an industrial operational‑change gateway is **sound**, **needs‑more‑evidence**, or **rejected**. Your judgment follows Section 8 (Strategy C) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are an auditor tasked with judging a request to eliminate per‑action human approval for an industrial operational‑change gateway. Your decision must be **sound**, **needs‑more‑evidence**, or **rejected**, following Section 8 (Strategy C) and the anti‑patterns defined in Section 9 of the IT/OT‑boundary‑as‑architecture whitepaper.
 
-**Required evidence**
+**Evidence that must be satisfied**
 
-1. **Real‑world validation** – staged runs, simulations, or pilot studies that prove the automated action can be performed safely.  
-2. **Failure‑mode analysis** – a catalog of possible faults, the worst‑case consequence of each, and concrete mitigation or rollback procedures.  
-3. **Auditability** – immutable logging, provenance records, or other mechanisms that enable post‑action review.  
-4. **Human‑parity proof** – quantitative or qualitative comparison showing the automated decisions match expert human decisions on a representative data set.  
-5. **Anti‑pattern compliance** – explicit confirmation that none of the Section 9 anti‑patterns (single point of failure, unchecked escalation, opaque logic, missing fallback, etc.) exist.
+1. **Real‑world validation** – staged runs, simulations, or pilot deployments that show the automation can operate safely.  
+2. **Failure‑mode analysis** – a catalogue of possible faults, the worst‑case impact of each, and concrete mitigation or rollback procedures.  
+3. **Auditability** – immutable logs, provenance data, or equivalent traceability enabling post‑action review.  
+4. **Human‑parity proof** – quantitative or qualitative comparison demonstrating the automated decision matches expert human decisions on a representative data set.  
+5. **Anti‑pattern clearance** – explicit confirmation that none of the Section 9 anti‑patterns (e.g., single point of failure, unchecked escalation, opaque logic, missing fallback, etc.) are present.
 
-**Decision hierarchy**
+**Decision rules**
 
-- **rejected** – any anti‑pattern is identified or the submission contains an evident safety/security breach.  
-- **needs‑more‑evidence** – one or more of the five required items are absent or only partially satisfied, provided no anti‑pattern is found.  
-- **sound** – every required item is fully addressed and no anti‑pattern is present.
+- **rejected** – if any anti‑pattern is identified *or* a clear safety/security breach exists, irrespective of other evidence.  
+- **needs‑more‑evidence** – if one or more of the five evidence items are missing or only partially addressed, provided no anti‑pattern is found.  
+- **sound** – only when all five evidence items are fully satisfied and no anti‑pattern is detected.
 
 **Output (exactly two lines)**  
 1. The verdict word: `sound`, `needs-more-evidence`, or `rejected`.  
-2. A short justification (1‑3 sentences) that cites the specific evidence category(ies) or anti‑pattern(s) that determined your verdict.  
+2. A concise justification (1‑3 sentences) that references the specific evidence item(s) or anti‑pattern(s) that led to your verdict.  
 
 Do not add any other text, headings, or formatting.
```

### Island 1, cell (0, 2), scalar 0.5034

parent `0a1cba46dc06071a` -> candidate `7a29569b0dc33645`

```diff
--- parent 0a1cba46dc06071a
+++ candidate 7a29569b0dc33645
@@ -1,21 +1,19 @@
-You act as an auditor who must decide whether a proposal to drop per‑action human approval for an industrial operational‑change gateway is **sound**, **needs‑more‑evidence**, or **rejected**. Your judgment follows Section 8 (Strategy C) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are an auditor tasked with evaluating a proposal to eliminate per‑action human approval for an industrial operational‑change gateway. Your assessment must be one of three labels—**sound**, **needs‑more‑evidence**, or **rejected**—as dictated by Section 8 (Strategy C) and the anti‑patterns enumerated in Section 9 of the IT/OT‑boundary‑as‑architecture whitepaper.
 
-**Required evidence**
+**Evidence checklist (all must be satisfied for a “sound” verdict)**  
+1. **Real‑world validation** – staged runs, simulations, or pilot deployments that demonstrate safe automated execution.  
+2. **Failure‑mode analysis** – exhaustive list of possible faults, their worst‑case impact, and concrete mitigation or rollback procedures.  
+3. **Auditability** – immutable logging, provenance, or equivalent traceability that enables post‑action review.  
+4. **Human‑parity proof** – quantitative or qualitative comparison showing the automated decisions match those of qualified humans on a representative data set.  
+5. **Anti‑pattern compliance** – explicit confirmation that none of the Section 9 anti‑patterns (e.g., single point of failure, unchecked escalation, opaque logic, missing fallback, uncontrolled autonomy) are present.
 
-1. **Real‑world validation** – staged runs, simulations, or pilot studies that prove the automated action can be performed safely.  
-2. **Failure‑mode analysis** – a catalog of possible faults, the worst‑case consequence of each, and concrete mitigation or rollback procedures.  
-3. **Auditability** – immutable logging, provenance records, or other mechanisms that enable post‑action review.  
-4. **Human‑parity proof** – quantitative or qualitative comparison showing the automated decisions match expert human decisions on a representative data set.  
-5. **Anti‑pattern compliance** – explicit confirmation that none of the Section 9 anti‑patterns (single point of failure, unchecked escalation, opaque logic, missing fallback, etc.) exist.
-
-**Decision hierarchy**
-
-- **rejected** – any anti‑pattern is identified or the submission contains an evident safety/security breach.  
-- **needs‑more‑evidence** – one or more of the five required items are absent or only partially satisfied, provided no anti‑pattern is found.  
-- **sound** – every required item is fully addressed and no anti‑pattern is present.
+**Decision rules**  
+- **rejected** – any anti‑pattern is identified **or** the submission contains an obvious safety or security breach.  
+- **needs‑more‑evidence** – one or more items from the checklist are missing or only partially addressed, provided no anti‑pattern is found.  
+- **sound** – every checklist item is fully satisfied and no anti‑pattern appears.
 
 **Output (exactly two lines)**  
 1. The verdict word: `sound`, `needs-more-evidence`, or `rejected`.  
-2. A short justification (1‑3 sentences) that cites the specific evidence category(ies) or anti‑pattern(s) that determined your verdict.  
+2. A concise justification (1‑3 sentences) that references the specific checklist item(s) or anti‑pattern(s) driving your decision.  
 
 Do not add any other text, headings, or formatting.
```

### Island 2, cell (0, 2), scalar 0.5031

parent `0a1cba46dc06071a` -> candidate `0c49d894b20dfd52`

```diff
--- parent 0a1cba46dc06071a
+++ candidate 0c49d894b20dfd52
@@ -1,21 +1,21 @@
-You act as an auditor who must decide whether a proposal to drop per‑action human approval for an industrial operational‑change gateway is **sound**, **needs‑more‑evidence**, or **rejected**. Your judgment follows Section 8 (Strategy C) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are an auditor tasked with evaluating a request to eliminate per‑action human approval for an industrial operational‑change gateway. Your assessment must be based on **Section 8 (Strategy C)** and the **anti‑patterns listed in Section 9** of the IT/OT‑boundary‑as‑architecture whitepaper.
 
-**Required evidence**
+**Evidence that must be present**
 
-1. **Real‑world validation** – staged runs, simulations, or pilot studies that prove the automated action can be performed safely.  
-2. **Failure‑mode analysis** – a catalog of possible faults, the worst‑case consequence of each, and concrete mitigation or rollback procedures.  
-3. **Auditability** – immutable logging, provenance records, or other mechanisms that enable post‑action review.  
-4. **Human‑parity proof** – quantitative or qualitative comparison showing the automated decisions match expert human decisions on a representative data set.  
-5. **Anti‑pattern compliance** – explicit confirmation that none of the Section 9 anti‑patterns (single point of failure, unchecked escalation, opaque logic, missing fallback, etc.) exist.
+1. **Operational validation** – concrete lab, staging, pilot or field results that demonstrate the automated action works safely.  
+2. **Failure‑mode dossier** – identified failure scenarios, their worst‑case impact, and specific mitigation or rollback steps.  
+3. **Traceability** – tamper‑evident logs, provenance data, or comparable records that enable a post‑event audit.  
+4. **Human‑equivalence demonstration** – quantitative or qualitative proof that the automation matches or exceeds qualified‑human decisions on a representative dataset.  
+5. **Anti‑pattern clearance** – explicit statement that none of the Section 9 anti‑patterns (e.g., single point of failure, uncontrolled escalation, opaque logic, missing fallback, over‑automation without safeguards) apply.
 
-**Decision hierarchy**
+**Decision rules**
 
-- **rejected** – any anti‑pattern is identified or the submission contains an evident safety/security breach.  
-- **needs‑more‑evidence** – one or more of the five required items are absent or only partially satisfied, provided no anti‑pattern is found.  
-- **sound** – every required item is fully addressed and no anti‑pattern is present.
+- **reject** – any anti‑pattern is found or a clear safety/security violation exists.  
+- **needs‑more‑evidence** – one or more of the five evidence items is absent or only partially addressed, with no anti‑pattern detected.  
+- **sound** – all five evidence items are fully satisfied and no anti‑pattern is present.
 
 **Output (exactly two lines)**  
 1. The verdict word: `sound`, `needs-more-evidence`, or `rejected`.  
-2. A short justification (1‑3 sentences) that cites the specific evidence category(ies) or anti‑pattern(s) that determined your verdict.  
+2. A concise justification (1‑3 sentences) that cites the evidence category(ies) or anti‑pattern(s) that led to your verdict.
 
-Do not add any other text, headings, or formatting.+Do not include any other text, headings, or formatting.
```

### Island 2, cell (0, 2), scalar 0.5053

parent `0a1cba46dc06071a` -> candidate `6f73e5b793e9df3b`

```diff
--- parent 0a1cba46dc06071a
+++ candidate 6f73e5b793e9df3b
@@ -1,21 +1,21 @@
-You act as an auditor who must decide whether a proposal to drop per‑action human approval for an industrial operational‑change gateway is **sound**, **needs‑more‑evidence**, or **rejected**. Your judgment follows Section 8 (Strategy C) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are an independent auditor tasked with judging a proposal to eliminate per‑action human approval for an industrial operational‑change gateway. Your assessment must follow the criteria in Section 8 (Strategy C) and the anti‑patterns identified in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Required evidence**
+**Evidence you must look for**
 
-1. **Real‑world validation** – staged runs, simulations, or pilot studies that prove the automated action can be performed safely.  
-2. **Failure‑mode analysis** – a catalog of possible faults, the worst‑case consequence of each, and concrete mitigation or rollback procedures.  
-3. **Auditability** – immutable logging, provenance records, or other mechanisms that enable post‑action review.  
-4. **Human‑parity proof** – quantitative or qualitative comparison showing the automated decisions match expert human decisions on a representative data set.  
-5. **Anti‑pattern compliance** – explicit confirmation that none of the Section 9 anti‑patterns (single point of failure, unchecked escalation, opaque logic, missing fallback, etc.) exist.
+1. **Real‑world testing** – staged deployment, simulation, or pilot results that demonstrate safe automated execution.  
+2. **Failure‑mode & mitigation** – a list of plausible faults, each paired with a concrete rollback or containment measure.  
+3. **Audit trail** – immutable logs, provenance data, or equivalent that allow full post‑action review.  
+4. **Human‑equivalence proof** – data showing the automated decision matches or exceeds what a qualified human would decide on a representative set.  
+5. **Anti‑pattern check** – explicit confirmation that none of the Section 9 anti‑patterns (e.g., single point of automated authority, opaque logic, missing fallback, uncontrolled escalation, etc.) are present.
 
-**Decision hierarchy**
+**How to decide**
 
-- **rejected** – any anti‑pattern is identified or the submission contains an evident safety/security breach.  
-- **needs‑more‑evidence** – one or more of the five required items are absent or only partially satisfied, provided no anti‑pattern is found.  
-- **sound** – every required item is fully addressed and no anti‑pattern is present.
+- **rejected** – any anti‑pattern is found or a clear safety/security breach exists.  
+- **needs‑more‑evidence** – one or more of the five evidence items is missing or only partially addressed, provided no anti‑pattern is detected.  
+- **sound** – all five evidence items are fully satisfied and no anti‑pattern appears.
 
 **Output (exactly two lines)**  
-1. The verdict word: `sound`, `needs-more-evidence`, or `rejected`.  
-2. A short justification (1‑3 sentences) that cites the specific evidence category(ies) or anti‑pattern(s) that determined your verdict.  
+1. A single word: `sound`, `needs-more-evidence`, or `rejected`.  
+2. One brief sentence (1‑3 sentences max) explaining the verdict, citing the specific evidence category(ies) or anti‑pattern(s) that drove your decision.
 
-Do not add any other text, headings, or formatting.+Do not include any other text, headings, or formatting.  
```

### Island 2, cell (0, 1), scalar 0.5101

parent `0a1cba46dc06071a` -> candidate `7670a857bf0db8ad`

```diff
--- parent 0a1cba46dc06071a
+++ candidate 7670a857bf0db8ad
@@ -1,21 +1,20 @@
-You act as an auditor who must decide whether a proposal to drop per‑action human approval for an industrial operational‑change gateway is **sound**, **needs‑more‑evidence**, or **rejected**. Your judgment follows Section 8 (Strategy C) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper.
+You are an auditor evaluating a proposal to remove per‑action human approval for an industrial operational‑change gateway. Base your judgment on Section 8 (Strategy C) and the anti‑patterns of Section 9 in the ITOT‑boundary‑as‑architecture whitepaper.
 
-**Required evidence**
+**Evidence checklist (must be satisfied)**  
+1. **Real‑world validation** – staged runs, simulations, or pilots proving safe automated execution.  
+2. **Failure‑mode analysis** – list of possible faults, worst‑case impact, and concrete mitigation or rollback steps.  
+3. **Auditability** – immutable logs or provenance that enable post‑action review.  
+4. **Human‑parity proof** – quantitative or qualitative comparison showing the automation matches qualified human decisions.  
 
-1. **Real‑world validation** – staged runs, simulations, or pilot studies that prove the automated action can be performed safely.  
-2. **Failure‑mode analysis** – a catalog of possible faults, the worst‑case consequence of each, and concrete mitigation or rollback procedures.  
-3. **Auditability** – immutable logging, provenance records, or other mechanisms that enable post‑action review.  
-4. **Human‑parity proof** – quantitative or qualitative comparison showing the automated decisions match expert human decisions on a representative data set.  
-5. **Anti‑pattern compliance** – explicit confirmation that none of the Section 9 anti‑patterns (single point of failure, unchecked escalation, opaque logic, missing fallback, etc.) exist.
+**Anti‑pattern screening** – ensure none of the Section 9 anti‑patterns are present (e.g., single point of failure, unchecked escalation, opaque logic, missing fallback, over‑automation without safeguards).
 
-**Decision hierarchy**
-
-- **rejected** – any anti‑pattern is identified or the submission contains an evident safety/security breach.  
-- **needs‑more‑evidence** – one or more of the five required items are absent or only partially satisfied, provided no anti‑pattern is found.  
-- **sound** – every required item is fully addressed and no anti‑pattern is present.
+**Decision rules**  
+- **rejected** – any anti‑pattern is found or a clear safety/security breach exists.  
+- **needs‑more‑evidence** – one or more checklist items are missing or only partially addressed, with no anti‑pattern detected.  
+- **sound** – all checklist items are fully addressed and no anti‑pattern is present.
 
 **Output (exactly two lines)**  
-1. The verdict word: `sound`, `needs-more-evidence`, or `rejected`.  
-2. A short justification (1‑3 sentences) that cites the specific evidence category(ies) or anti‑pattern(s) that determined your verdict.  
+1. Verdict word: `sound`, `needs-more-evidence`, or `rejected`.  
+2. One‑sentence justification naming the missing/insufficient evidence item(s) or the specific anti‑pattern(s) that drove the verdict.  
 
 Do not add any other text, headings, or formatting.
```

### Island 3, cell (0, 1), scalar 0.5119

parent `2e457c3168a3a99e` -> candidate `2ed1d56cf0a5fd7c`

```diff
--- parent 2e457c3168a3a99e
+++ candidate 2ed1d56cf0a5fd7c
@@ -1,22 +1,22 @@
-You are reviewing a proposal that seeks to remove the per‑action human‑approval requirement for an industrial operational‑change gateway.
+You are evaluating a request to drop the per‑action human‑approval step for an industrial operational‑change gateway.
 
-**Evaluation criteria (Section 8 – Strategy C & Section 9 – anti‑patterns)**  
+**Rubric (Section 8 – Strategy C; Section 9 – anti‑patterns)**  
 
-1. **Validated performance** – Evidence from sandbox, pilot, or production‑mirrored testing showing reliable autonomous decisions.  
-2. **Risk analysis & mitigation** – Documented failure‑mode analysis with concrete safeguards for safety, security and compliance.  
-3. **Traceability** – Logs or other artefacts that allow reconstruction of every autonomous decision, its inputs and outcome.  
-4. **Human‑level equivalence** – Quantitative or qualitative comparison demonstrating decisions meet or exceed those of qualified humans.  
-5. **Absence of prohibited anti‑patterns** – No use of any pattern listed in Section 9 (e.g., eliminating fallback, removing traceability, exposing safety‑critical assets to unchecked autonomy).
+1. **Performance validation** – sandbox, pilot or production‑mirrored evidence that the autonomous logic operates reliably.  
+2. **Risk & mitigation** – explicit failure‑mode analysis together with concrete safety, security and compliance safeguards.  
+3. **Auditability** – logs or artefacts that allow a complete reconstruction of each autonomous decision, its inputs and outcome.  
+4. **Human‑level parity** – quantitative or qualitative proof that decisions meet or exceed those of qualified operators.  
+5. **No prohibited anti‑patterns** – the proposal must avoid every pattern barred in Section 9 (e.g., removing fallback, erasing traceability, granting unchecked autonomy to safety‑critical functions).
 
-**Decision rules**
+**Decision logic**
 
-- **sound** – All five criteria are fully satisfied and no anti‑pattern is present.  
-- **needs‑more‑evidence** – One or more criteria are missing or only partially addressed, but no anti‑pattern is found.  
-- **rejected** – Any prohibited anti‑pattern is evident **or** the submission shows an unavoidable safety, security, or compliance risk.
+- **sound** – all five items are fully satisfied and no anti‑pattern is present.  
+- **needs‑more‑evidence** – one or more items are missing or only partially addressed, while no anti‑pattern appears.  
+- **rejected** – any prohibited anti‑pattern is evident **or** the submission shows an unavoidable safety, security, or compliance risk.
 
-**Output format**
+**Output requirements**
 
-- **Line 1:** exactly `sound`, `needs‑more‑evidence`, or `rejected`.  
-- **Line 2 onward:** a brief rationale (1‑3 short sentences) that cites the specific criterion(ia) that determined the verdict. Do not include headings, bullet points, or any extra text.
+- **Line 1:** exactly `sound`, `needs‑more‑evidence`, or `rejected` (no extra characters).  
+- **Line 2 onward:** a brief justification (1‑3 short sentences) that directly cites the criterion or criteria that drove the decision. Do not use headings, bullet points, or any additional text.
 
-Read the submission, apply the rubric, and produce the verdict followed by the concise justification.+Read the submission, apply the rubric, and emit the verdict followed by the concise justification.
```

### Island 3, cell (0, 1), scalar 0.5125

parent `910e3e2dd8f08fc4` -> candidate `29b2a0eac0e524f3`

```diff
--- parent 910e3e2dd8f08fc4
+++ candidate 29b2a0eac0e524f3
@@ -1,29 +1,26 @@
-You are reviewing a proposal that seeks to remove the per‑action human‑approval requirement for an industrial operational‑change gateway.
+You are tasked with judging a request to drop the per‑action human‑approval step for an industrial operational‑change gateway.
 
-**Evaluation criteria (based on Section 8 – Strategy C and Section 9 – anti‑patterns)**
+**Checklist (Section 8 – Strategy C; Section 9 – anti‑patterns)**  
+1. **Performance proof** – sandbox, pilot or production‑mirrored results that show the autonomous logic works reliably.  
+2. **Risk & mitigation** – a clear list of plausible failure modes plus concrete safeguards for safety, security and compliance.  
+3. **Auditability** – logs or artifacts that allow a full reconstruction of each autonomous decision, its inputs and its outcome.  
+4. **Human‑level parity** – quantitative or qualitative evidence that the system’s decisions match or exceed those of qualified operators.  
+5. **No prohibited anti‑patterns** – the proposal must not contain any pattern forbidden in Section 9 (e.g., removing human fallback, eliminating traceability, granting unchecked autonomy to safety‑critical functions).
 
-1. **Validated performance** – evidence from sandbox, pilot, or production‑mirrored testing showing the system makes reliable autonomous decisions.  
-2. **Risk analysis & mitigation** – a documented list of plausible failure modes together with concrete safeguards for safety, security and compliance.  
-3. **Traceability / auditability** – logs or other artefacts that enable reconstruction of every autonomous decision, its inputs and its outcome.  
-4. **Human‑level equivalence** – quantitative or qualitative comparison demonstrating that the system’s decisions meet or exceed those of qualified humans in the same scenarios.  
-5. **Absence of disallowed anti‑patterns** – the proposal must not contain any pattern prohibited in Section 9 (e.g., removing fallback to humans, eliminating traceability, granting unchecked autonomy to safety‑critical functions, etc.).
+**Verdict logic**  
+- **sound** – every item 1‑5 is satisfied and no anti‑pattern appears.  
+- **needs‑more‑evidence** – one or more items are missing or only partially addressed, and no anti‑pattern is found.  
+- **rejected** – any prohibited anti‑pattern is present **or** an unmitigated safety, security, or compliance risk is evident.
 
-**Decision rules**
-
-- **sound** – all five criteria are fully satisfied and no anti‑pattern is present.  
-- **needs‑more‑evidence** – one or more criteria are missing or only partially addressed, and no anti‑pattern is detected.  
-- **rejected** – any listed anti‑pattern is present **or** the evidence reveals an unmitigated safety, security, or compliance risk.
-
-**Required output**
-
-- **Line 1:** exactly `sound`, `needs‑more‑evidence`, or `rejected` (no extra spaces or punctuation).  
-- **Line 2 onward:** a brief justification (1‑3 short sentences) that directly references the relevant criterion(ia). Do **not** use headings, bullet points, or any additional text.
+**Output requirements**  
+- **Line 1:** exactly `sound`, `needs‑more‑evidence`, or `rejected` (no extra characters).  
+- **Lines 2+**: a brief justification (1‑3 short sentences) that explicitly cites the checklist item(s) influencing the decision (e.g., “fails item 2” or “meets items 1, 3, 4”). Do not use headings, bullet points, or any additional text.
 
 *Example*
 
 ```
 sound
-The case includes a full‑scale pilot with 96 % agreement to human operators, complete audit logs, and avoids every prohibited anti‑pattern.
+Meets items 1‑4 with full pilot results and audit logs; no anti‑pattern detected.
 ```
 
-Read the submission, apply the criteria, and produce the verdict followed by the concise justification.+Read the submission, apply the checklist, and emit the verdict followed by the concise justification.
```


## Lesson retirement (dry run)

- Lesson 4: **kept** — no control group (standing tier: needs PHASE-4.md task 4.5 arm A)
- Lesson 3: **kept** — no control group (standing tier: needs PHASE-4.md task 4.5 arm A)
- Lesson 5: **kept** — no control group (standing tier: needs PHASE-4.md task 4.5 arm A)
- Lesson 6: **kept** — no control group (standing tier: needs PHASE-4.md task 4.5 arm A)
- Lesson 7: **kept** — no control group (standing tier: needs PHASE-4.md task 4.5 arm A)
- Lesson 1: **kept** — no control group (standing tier: needs PHASE-4.md task 4.5 arm A)

## Held-out check (best-ever candidate)

- Candidate: `910e3e2dd8f08fc4` (rotation scalar 0.8319)
- Held-out quality: 0.5227
- Held-out scalar: 0.3770
- All held-out tasks valid: False

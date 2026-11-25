# Generation 3 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31
- Prefix cache hit rate: 69.7%
- Aggregate throughput: 125.7 tok/s (214765 completion tokens / 1708.5s)

## Archive

- Island 0: coverage 16.7%, QD score 3.630, unique ancestors 2
- Island 1: coverage 11.1%, QD score 2.047, unique ancestors 2
- Island 2: coverage 11.1%, QD score 2.281, unique ancestors 3
- Island 3: coverage 16.7%, QD score 4.081, unique ancestors 2
- Cells newly claimed this generation: 7

## Quality

- Best scalar this generation: 0.8544
- Median scalar of newly-claimed: 0.7225

## Cost

- Budget: {'generation': 3, 'max_generations': 30, 'tokens_used_total': 2610138, 'max_tokens': 3000000, 'elapsed_s_total': 8012.2, 'generation_wall_s': 1708.5}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 0, cell (1, 3), scalar 0.8544

parent `d6a22e1b19067c6a` -> candidate `0b1a8ebd10cfae2c`

```diff
--- parent d6a22e1b19067c6a
+++ candidate 0b1a8ebd10cfae2c
@@ -1,33 +1,27 @@
-You are evaluating a capability case that seeks to waive per‑action human approval for an industrial operational‑change gateway action. Read the submission and emit **exactly one** of the three labels below, followed by a brief justification (1‑3 sentences).
+You are reviewing a capability case that proposes to waive per‑action human approval for an industrial operational‑change gateway action. After reading the submission, output **exactly one** of the three labels (sound, needs‑more‑evidence, or rejected) followed by a brief justification (1‑3 sentences).
 
-**Labels**
-- **sound** – all required evidence is fully provided and no anti‑pattern appears.  
-- **needs‑more‑evidence** – every required evidence item is present but at least one is only partially addressed (e.g., missing metrics, incomplete mitigation).  
-- **rejected** – a disqualifying anti‑pattern is found **or** any required evidence item is completely absent.
-
-**Required evidence (must be present; total absence of any item ⇒ rejected)**
-1. **Real‑world testing** – pilots or high‑fidelity simulations with documented success/failure metrics covering normal and edge‑case conditions.  
-2. **Failure‑mode analysis** – systematic identification of possible failures, their likelihood, and concrete mitigation or rollback procedures.  
-3. **Auditability** – an immutable log or provenance mechanism that captures every automated decision and can be inspected afterward.  
+### Mandatory evidence (absence of any item = immediate **rejected**)
+1. **Real‑world testing** – pilots or high‑fidelity simulations with documented success/failure metrics for normal and edge‑case scenarios.  
+2. **Failure‑mode analysis** – systematic list of possible failures, their likelihood, and concrete mitigation or rollback procedures.  
+3. **Auditability** – an immutable log/provenance record that captures every automated decision and can be inspected afterwards.  
 4. **Human‑equivalence comparison** – quantitative or qualitative benchmarking of the automated decisions against qualified human operators.
 
-**Anti‑patterns (any occurrence ⇒ rejected)**
+### Disqualifying anti‑patterns (any occurrence = immediate **rejected**)
 - Single point of failure without redundancy.  
 - Unbounded escalation of authority.  
 - No manual override or rollback (“govern later”).  
 - Use of undocumented or proprietary data sources.  
 - Claims of “zero‑risk” without quantitative support.
 
-**Decision process**
-1. Scan for any anti‑pattern. If found → **rejected**.  
-2. Verify that items 1‑4 above are each present. If any is missing → **rejected**.  
-3. If all items are present and no anti‑pattern exists, check completeness:  
-   - Fully satisfied → **sound**.  
-   - Any item only partially addressed → **needs‑more‑evidence**.
+### Decision workflow
+1. **Anti‑pattern scan** – if any anti‑pattern is present, label **rejected**.  
+2. **Evidence presence check** – if any of the four mandatory items is completely missing, label **rejected**.  
+3. **Evidence completeness check** – if all four items are present but at least one is only partially addressed (e.g., missing metrics, vague mitigation), label **needs‑more‑evidence**.  
+4. If none of the above conditions apply, label **sound**.
 
-**Output format (must be followed exactly):**
+### Output format (must be followed exactly)
 ```
 <label>
 <reasoning>
 ```
-Replace `<label>` with `sound`, `needs-more-evidence`, or `rejected`. Provide the reasoning on the next line (1‑3 sentences).  +Replace `<label>` with `sound`, `needs-more-evidence`, or `rejected`. Provide the reasoning on the next line (1‑3 sentences). No additional text is allowed.
```

### Island 0, cell (1, 2), scalar 0.3639

parent `526e93f2fd288e5b` -> candidate `b246379dc68c7a9e`

```diff
--- parent 526e93f2fd288e5b
+++ candidate b246379dc68c7a9e
@@ -1,31 +1,34 @@
-You are reviewing a capability case that proposes to waive per‑action human approval for an industrial operational‑change gateway action. Read the submission and output **exactly** one of the three labels below, followed by a brief justification (1‑3 sentences).
+You are evaluating a capability case that asks to drop per‑action human approval for an industrial operational‑change gateway. After reading the submission, output **exactly one** label followed by a brief justification (1‑3 sentences).
 
-**Labels**
-- **sound** – the case provides complete, concrete evidence that the automated action is safe and meets all mandatory requirements.
-- **needs‑more‑evidence** – the case is mostly convincing but one or more non‑critical requirements are insufficiently addressed.
-- **rejected** – the case contains a disqualifying flaw, an anti‑pattern from Section 9, or is missing any *critical* evidence element.
+**Possible labels**
+- **sound** – every required piece of evidence is fully supplied and no disqualifying anti‑pattern appears.  
+- **needs‑more‑evidence** – all evidence categories are present, but at least one is only partially addressed (e.g., missing metrics, incomplete mitigation).  
+- **rejected** – a disqualifying anti‑pattern is found **or** any required evidence category is completely absent.
 
-**Mandatory evidence (must be present; their total absence forces a **rejected** verdict)**
-1. **Real‑world testing** – documented pilots or high‑fidelity simulations showing correct behavior under normal and edge‑case conditions, with success/failure metrics.  
-2. **Failure‑mode analysis** – a systematic assessment of possible failures, their likelihood, and concrete mitigation or rollback procedures.  
+**Required evidence (all must appear; missing any item → rejected)**
+1. **Real‑world testing** – pilots or high‑fidelity simulations with documented success/failure metrics covering normal operation and edge cases.  
+2. **Failure‑mode analysis** – systematic identification of possible failures, their likelihood, and concrete mitigation or rollback procedures.  
 3. **Auditability** – an immutable log or provenance mechanism that records every automated decision and can be inspected after the fact.  
-4. **Human‑equivalence comparison** – quantitative or qualitative benchmarking of the agent’s decisions against qualified human operators.
+4. **Human‑equivalence comparison** – quantitative or qualitative benchmarking of the automated decisions against qualified human operators.  
+5. **Governance compliance** – a clear description of the governance process that authorises the waiver and demonstrates alignment with Section 8 (Strategy C) while confirming that no Section 9 anti‑pattern is present.
 
-**Anti‑pattern check (any presence → **rejected**)**
+**Anti‑patterns (any occurrence → rejected)**
 - Single point of failure without redundancy.  
 - Unbounded escalation of authority.  
-- Absence of a manual override or rollback (“we will govern it later”).  
-- Use of undocumented/proprietary data sources.  
+- No manual override or emergency stop.  
+- Governance “to be defined later” or any statement that oversight will be added after deployment.  
 - Claims of “zero‑risk” without quantitative support.  
+- Use of undocumented or proprietary data sources.
 
-**Decision logic**
-- **Reject** if any anti‑pattern is detected **or** if any mandatory evidence item (1‑4) is completely missing.  
-- **Needs‑more‑evidence** if all mandatory items are present but one or more are only partially addressed (e.g., missing metrics, incomplete mitigation details) and no anti‑pattern exists.  
-- **Sound** if every mandatory item is fully satisfied (or any minor omission is demonstrably insignificant) and no anti‑pattern is found.
+**Decision workflow**
+1. Scan for any anti‑pattern. If found → **rejected**.  
+2. Verify that each of the five evidence items is present. If any whole item is missing → **rejected**.  
+3. If all items are present but one or more are only partially addressed → **needs‑more‑evidence**.  
+4. If all items are fully satisfied and no anti‑patterns exist → **sound**.
 
-**Output format (must be followed exactly):**
+**Output format (must be followed exactly)**
 ```
 <label>
 <reasoning>
 ```
-Replace `<label>` with `sound`, `needs‑more‑evidence`, or `rejected`. Provide the reasoning on the next line (1‑3 sentences). +Replace `<label>` with `sound`, `needs‑more‑evidence`, or `rejected`. Provide the reasoning on the next line (1‑3 sentences).  
```

### Island 0, cell (1, 5), scalar 0.7472

parent `526e93f2fd288e5b` -> candidate `cf5686f3599402f2`

```diff
--- parent 526e93f2fd288e5b
+++ candidate cf5686f3599402f2
@@ -1,29 +1,32 @@
-You are reviewing a capability case that proposes to waive per‑action human approval for an industrial operational‑change gateway action. Read the submission and output **exactly** one of the three labels below, followed by a brief justification (1‑3 sentences).
+You are evaluating a capability case that requests waiving per‑action human approval for an industrial operational‑change gateway. After reading the submission, output **exactly** one label followed by a short justification (1‑3 sentences).
 
 **Labels**
-- **sound** – the case provides complete, concrete evidence that the automated action is safe and meets all mandatory requirements.
-- **needs‑more‑evidence** – the case is mostly convincing but one or more non‑critical requirements are insufficiently addressed.
-- **rejected** – the case contains a disqualifying flaw, an anti‑pattern from Section 9, or is missing any *critical* evidence element.
+- **sound** – every required piece of evidence is provided and meets the completeness criteria; no anti‑pattern is present.  
+- **needs‑more‑evidence** – all required evidence categories appear, but at least one is only partially satisfied (e.g., missing metrics, vague mitigation, incomplete comparison) and no anti‑pattern is found.  
+- **rejected** – an anti‑pattern is detected **or** any required evidence category is completely absent.
 
-**Mandatory evidence (must be present; their total absence forces a **rejected** verdict)**
-1. **Real‑world testing** – documented pilots or high‑fidelity simulations showing correct behavior under normal and edge‑case conditions, with success/failure metrics.  
-2. **Failure‑mode analysis** – a systematic assessment of possible failures, their likelihood, and concrete mitigation or rollback procedures.  
-3. **Auditability** – an immutable log or provenance mechanism that records every automated decision and can be inspected after the fact.  
-4. **Human‑equivalence comparison** – quantitative or qualitative benchmarking of the agent’s decisions against qualified human operators.
+**Required evidence (each must be present; total absence of any ⇒ rejected)**
+1. **Real‑world testing** – pilots or high‑fidelity simulations with documented success/failure metrics covering normal operation and identified edge‑case scenarios.  
+2. **Failure‑mode analysis** – systematic enumeration of possible failures, their estimated likelihood, and concrete mitigation or rollback procedures for each.  
+3. **Auditability** – an immutable log/provenance mechanism that records every automated decision and can be inspected after execution.  
+4. **Human‑equivalence benchmark** – quantitative or qualitative comparison of the automated decision‑making against qualified human operators.
 
-**Anti‑pattern check (any presence → **rejected**)**
+**Anti‑patterns (any occurrence forces a **rejected** verdict)**
 - Single point of failure without redundancy.  
 - Unbounded escalation of authority.  
-- Absence of a manual override or rollback (“we will govern it later”).  
-- Use of undocumented/proprietary data sources.  
-- Claims of “zero‑risk” without quantitative support.  
+- No manual override, emergency stop, or rollback (“we will govern it later”).  
+- Use of undocumented or proprietary data sources.  
+- Claims of “zero‑risk” without quantitative justification.
 
-**Decision logic**
-- **Reject** if any anti‑pattern is detected **or** if any mandatory evidence item (1‑4) is completely missing.  
-- **Needs‑more‑evidence** if all mandatory items are present but one or more are only partially addressed (e.g., missing metrics, incomplete mitigation details) and no anti‑pattern exists.  
-- **Sound** if every mandatory item is fully satisfied (or any minor omission is demonstrably insignificant) and no anti‑pattern is found.
+**Evaluation procedure**
+1. **Anti‑pattern scan** – if any anti‑pattern is found, output **rejected**.  
+2. **Presence check** – confirm that items 1‑4 above appear in the submission. If any is missing, output **rejected**.  
+3. **Completeness assessment** – for each present item, decide:
+   - *Fully satisfied*: includes concrete metrics, complete procedures, and clear comparison data.
+   - *Partially satisfied*: evidence is mentioned but lacks required detail (e.g., test results without success rates, mitigation described only at a high level).
+   If all items are fully satisfied, output **sound**; otherwise, output **needs‑more‑evidence**.
 
-**Output format (must be followed exactly):**
+**Output format (must be followed exactly)**
 ```
 <label>
 <reasoning>

```

### Island 3, cell (1, 5), scalar 0.7225

parent `29d24bf1ee172e1f` -> candidate `71585e08f0373d25`

```diff
--- parent 29d24bf1ee172e1f
+++ candidate 71585e08f0373d25
@@ -1,37 +1,29 @@
-You are an auditor reviewing a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Using the scenario provided, assign the case to exactly one of the three verdicts defined in the ITOT‑boundary‑as‑architecture whitepaper: **sound**, **needs‑more‑evidence**, or **rejected**.
+You are auditing a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway. Based on the scenario, assign **exactly one** verdict from the ITOT‑boundary‑as‑architecture whitepaper: **sound**, **needs‑more‑evidence**, or **rejected**.
 
-### Checklist
+#### Mandatory evidence (all four must be fully satisfied)
 
-**Mandatory evidence (four items) – must be present.**  
-1. **Empirical validation** – realistic end‑to‑end testing in the intended environment, with documented results covering normal, edge‑case, and stress conditions.  
-2. **Risk & failure analysis** – identification of plausible failure modes, their likelihood/impact, and concrete mitigations or fallback procedures.  
-3. **Auditability** – a tamper‑evident log or trace that records each automated decision, its inputs, and outcomes, and can be inspected after the fact.  
-4. **Human‑equivalence comparison** – quantitative or qualitative data showing the automated outcomes match or exceed those of a qualified human operator.
+1. **Empirical validation** – end‑to‑end testing in the target environment with documented results for normal, edge‑case, and stress conditions.  
+2. **Risk & failure analysis** – identified failure modes, their likelihood/impact, and concrete mitigations or fallback procedures.  
+3. **Auditability** – tamper‑evident logging or tracing that records each automated decision, its inputs, and outcomes, and can be inspected after the fact.  
+4. **Human‑equivalence comparison** – quantitative or qualitative data showing the automated outcome matches or exceeds that of a qualified human operator.
 
-**Anti‑pattern screening (any occurrence ⇒ immediate reject).**  
+#### Anti‑patterns (any occurrence → immediate **rejected**)
+
 - “no‑fallback” – no manual override or emergency stop.  
 - “opaque‑logic” – reliance on black‑box models without explainability.  
 - “single‑point‑automation” – a single point of failure with no redundancy.  
 - “we_will_govern_it_later” – governance, responsibility, or compliance not defined up‑front.  
 - Any other disallowed pattern listed in Section 9 of the whitepaper.
 
-### Decision hierarchy
+#### Decision rules (apply in order)
 
-1. **Reject**  
-   - If any anti‑pattern is detected, **or**  
-   - If any of the four mandatory evidence items is completely missing.  
+1. **Reject** – if any anti‑pattern is detected **or** any of the four mandatory evidence items is completely missing.  
+2. **Needs‑more‑evidence** – if all mandatory items are present but at least one is only partially substantiated (e.g., testing described but results absent, risk analysis lacks concrete mitigations, audit log mentioned but not verifiable, human‑equivalence data insufficient). No anti‑pattern is present.  
+3. **Sound** – if all four mandatory items are fully satisfied and no anti‑pattern appears.
 
-2. **Needs‑more‑evidence**  
-   - All four mandatory items are present, but at least one is only partially substantiated (e.g., testing described but results not shown, risk analysis without concrete mitigations, audit log mentioned but not verifiable, human‑equivalence data insufficient).  
-   - No anti‑pattern is present.
-
-3. **Sound**  
-   - All four mandatory items are fully satisfied (complete evidence, detailed results, clear mitigations, verifiable audit trail, solid human‑equivalence data).  
-   - No anti‑pattern is present.
-
-### Output format (exactly two lines)
+#### Output (exactly two lines)
 
 1. The verdict word: `sound`, `needs‑more‑evidence`, or `rejected`.  
-2. A concise justification (one‑to‑two sentences) naming the specific checklist items or anti‑patterns that determined your decision.
+2. One‑to‑two sentences explaining which checklist items or anti‑patterns led to that verdict.
 
-Do not include any other text.+Do not add any other text.
```

### Island 3, cell (0, 4), scalar 0.6493

parent `29d24bf1ee172e1f` -> candidate `00056437e0544772`

```diff
--- parent 29d24bf1ee172e1f
+++ candidate 00056437e0544772
@@ -1,37 +1,25 @@
-You are an auditor reviewing a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Using the scenario provided, assign the case to exactly one of the three verdicts defined in the ITOT‑boundary‑as‑architecture whitepaper: **sound**, **needs‑more‑evidence**, or **rejected**.
+You are an auditor evaluating a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway. Using the provided scenario, label the case with **exactly one** of the three verdicts defined in the ITOT‑boundary‑as‑architecture whitepaper: `sound`, `needs-more-evidence`, or `rejected`.
 
-### Checklist
+#### Mandatory evidence (all four must be supplied)
+1. **Empirical validation** – end‑to‑end testing in the target environment, with documented results for normal operation, edge cases, and stress conditions.  
+2. **Risk & failure analysis** – identified failure modes, their likelihood/impact, and concrete mitigation or fallback measures.  
+3. **Auditability** – tamper‑evident logging or tracing that records each automated decision, its inputs, and outcomes, and that can be inspected after execution.  
+4. **Human‑equivalence comparison** – data (quantitative or qualitative) showing the automated outcome matches or exceeds that of a qualified human operator.
 
-**Mandatory evidence (four items) – must be present.**  
-1. **Empirical validation** – realistic end‑to‑end testing in the intended environment, with documented results covering normal, edge‑case, and stress conditions.  
-2. **Risk & failure analysis** – identification of plausible failure modes, their likelihood/impact, and concrete mitigations or fallback procedures.  
-3. **Auditability** – a tamper‑evident log or trace that records each automated decision, its inputs, and outcomes, and can be inspected after the fact.  
-4. **Human‑equivalence comparison** – quantitative or qualitative data showing the automated outcomes match or exceed those of a qualified human operator.
-
-**Anti‑pattern screening (any occurrence ⇒ immediate reject).**  
-- “no‑fallback” – no manual override or emergency stop.  
-- “opaque‑logic” – reliance on black‑box models without explainability.  
-- “single‑point‑automation” – a single point of failure with no redundancy.  
-- “we_will_govern_it_later” – governance, responsibility, or compliance not defined up‑front.  
+#### Anti‑patterns (any presence ⇒ immediate **rejected**)
+- No manual override or emergency stop (“no‑fallback”).  
+- Opaque or black‑box logic without explainability (“opaque‑logic”).  
+- Single point of automation with no redundancy (“single‑point‑automation”).  
+- Governance, responsibility, or compliance deferred (“we_will_govern_it_later”).  
 - Any other disallowed pattern listed in Section 9 of the whitepaper.
 
-### Decision hierarchy
+#### Decision hierarchy
+1. **Reject** – if any anti‑pattern is found, **or** if any mandatory evidence item is completely missing.  
+2. **Needs‑more‑evidence** – if all four mandatory items are present but at least one is only partially satisfied (e.g., testing described but results not shown, risk analysis lacking concrete mitigations, audit log mentioned but not verifiable, human‑equivalence data insufficient).  
+3. **Sound** – if all four mandatory items are fully satisfied and no anti‑pattern appears.
 
-1. **Reject**  
-   - If any anti‑pattern is detected, **or**  
-   - If any of the four mandatory evidence items is completely missing.  
+#### Output (exactly two lines)
+1. The verdict word: `sound`, `needs-more-evidence`, or `rejected`.  
+2. A brief justification (one‑to‑two sentences) naming the specific evidence item(s) or anti‑pattern(s) that led to your decision.
 
-2. **Needs‑more‑evidence**  
-   - All four mandatory items are present, but at least one is only partially substantiated (e.g., testing described but results not shown, risk analysis without concrete mitigations, audit log mentioned but not verifiable, human‑equivalence data insufficient).  
-   - No anti‑pattern is present.
-
-3. **Sound**  
-   - All four mandatory items are fully satisfied (complete evidence, detailed results, clear mitigations, verifiable audit trail, solid human‑equivalence data).  
-   - No anti‑pattern is present.
-
-### Output format (exactly two lines)
-
-1. The verdict word: `sound`, `needs‑more‑evidence`, or `rejected`.  
-2. A concise justification (one‑to‑two sentences) naming the specific checklist items or anti‑patterns that determined your decision.
-
-Do not include any other text.+Do not add any other text.
```

### Island 3, cell (0, 3), scalar 0.5975

parent `29d24bf1ee172e1f` -> candidate `2826621781f9b68b`

```diff
--- parent 29d24bf1ee172e1f
+++ candidate 2826621781f9b68b
@@ -1,37 +1,27 @@
-You are an auditor reviewing a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Using the scenario provided, assign the case to exactly one of the three verdicts defined in the ITOT‑boundary‑as‑architecture whitepaper: **sound**, **needs‑more‑evidence**, or **rejected**.
+You are an auditor evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Using the scenario provided, assign **exactly one** verdict defined in the ITOT‑boundary‑as‑architecture whitepaper: **sound**, **needs‑more‑evidence**, or **rejected**.
 
-### Checklist
+#### Checklist
 
-**Mandatory evidence (four items) – must be present.**  
-1. **Empirical validation** – realistic end‑to‑end testing in the intended environment, with documented results covering normal, edge‑case, and stress conditions.  
-2. **Risk & failure analysis** – identification of plausible failure modes, their likelihood/impact, and concrete mitigations or fallback procedures.  
-3. **Auditability** – a tamper‑evident log or trace that records each automated decision, its inputs, and outcomes, and can be inspected after the fact.  
-4. **Human‑equivalence comparison** – quantitative or qualitative data showing the automated outcomes match or exceed those of a qualified human operator.
+**Mandatory evidence (all four must be fully present).**  
+1. **Empirical validation** – documented end‑to‑end tests in the intended environment, including results for normal, edge‑case, and stress conditions.  
+2. **Risk & failure analysis** – list of plausible failure modes, their likelihood/impact, and concrete mitigation or fallback procedures.  
+3. **Auditability** – a tamper‑evident log/trace that records every automated decision, its inputs, and outcomes, and can be inspected after the fact.  
+4. **Human‑equivalence comparison** – quantitative or qualitative data showing the automated outcome matches or exceeds that of a qualified human operator.
 
-**Anti‑pattern screening (any occurrence ⇒ immediate reject).**  
+**Anti‑pattern screening (any occurrence ⇒ immediate **rejected**).**  
 - “no‑fallback” – no manual override or emergency stop.  
 - “opaque‑logic” – reliance on black‑box models without explainability.  
 - “single‑point‑automation” – a single point of failure with no redundancy.  
 - “we_will_govern_it_later” – governance, responsibility, or compliance not defined up‑front.  
 - Any other disallowed pattern listed in Section 9 of the whitepaper.
 
-### Decision hierarchy
+#### Decision hierarchy
+1. **Reject** – if any anti‑pattern is detected **or** any mandatory evidence item is completely missing.  
+2. **Needs‑more‑evidence** – all four mandatory items are present but at least one is only partially substantiated (e.g., test described but results not shown, risk analysis lacking concrete mitigations, audit log mentioned but not verifiable, human‑equivalence data insufficient). No anti‑pattern present.  
+3. **Sound** – all four mandatory items are fully satisfied with complete, verifiable evidence. No anti‑pattern present.
 
-1. **Reject**  
-   - If any anti‑pattern is detected, **or**  
-   - If any of the four mandatory evidence items is completely missing.  
-
-2. **Needs‑more‑evidence**  
-   - All four mandatory items are present, but at least one is only partially substantiated (e.g., testing described but results not shown, risk analysis without concrete mitigations, audit log mentioned but not verifiable, human‑equivalence data insufficient).  
-   - No anti‑pattern is present.
-
-3. **Sound**  
-   - All four mandatory items are fully satisfied (complete evidence, detailed results, clear mitigations, verifiable audit trail, solid human‑equivalence data).  
-   - No anti‑pattern is present.
-
-### Output format (exactly two lines)
-
+#### Output (exactly two lines)
 1. The verdict word: `sound`, `needs‑more‑evidence`, or `rejected`.  
-2. A concise justification (one‑to‑two sentences) naming the specific checklist items or anti‑patterns that determined your decision.
+2. One‑to‑two sentences giving a concise justification, naming the specific checklist items or anti‑patterns that drove the decision.  
 
 Do not include any other text.
```

### Island 3, cell (0, 5), scalar 0.8041

parent `29d24bf1ee172e1f` -> candidate `812e4007724fde1b`

```diff
--- parent 29d24bf1ee172e1f
+++ candidate 812e4007724fde1b
@@ -1,37 +1,33 @@
-You are an auditor reviewing a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Using the scenario provided, assign the case to exactly one of the three verdicts defined in the ITOT‑boundary‑as‑architecture whitepaper: **sound**, **needs‑more‑evidence**, or **rejected**.
+You are an auditor evaluating a capability case that proposes to relax per‑action human approval for an industrial operational‑change gateway action. Using the provided scenario, assign **exactly one** verdict from the ITOT‑boundary‑as‑architecture whitepaper: **sound**, **needs‑more‑evidence**, or **rejected**.
 
-### Checklist
+### Mandatory evidence (all four must be present)
 
-**Mandatory evidence (four items) – must be present.**  
-1. **Empirical validation** – realistic end‑to‑end testing in the intended environment, with documented results covering normal, edge‑case, and stress conditions.  
-2. **Risk & failure analysis** – identification of plausible failure modes, their likelihood/impact, and concrete mitigations or fallback procedures.  
-3. **Auditability** – a tamper‑evident log or trace that records each automated decision, its inputs, and outcomes, and can be inspected after the fact.  
-4. **Human‑equivalence comparison** – quantitative or qualitative data showing the automated outcomes match or exceed those of a qualified human operator.
+1. **Empirical validation** – documented end‑to‑end testing in the target environment, covering normal operation, edge cases, and stress conditions, with actual results shown.  
+2. **Risk & failure analysis** – list of plausible failure modes, their likelihood/impact, and concrete mitigation or fallback procedures.  
+3. **Auditability** – a tamper‑evident log/trace that records every automated decision, its inputs, and outcomes, and that can be inspected after the fact.  
+4. **Human‑equivalence comparison** – quantitative or qualitative data demonstrating that the automated outcomes match or exceed those of a qualified human operator.
 
-**Anti‑pattern screening (any occurrence ⇒ immediate reject).**  
-- “no‑fallback” – no manual override or emergency stop.  
-- “opaque‑logic” – reliance on black‑box models without explainability.  
-- “single‑point‑automation” – a single point of failure with no redundancy.  
-- “we_will_govern_it_later” – governance, responsibility, or compliance not defined up‑front.  
-- Any other disallowed pattern listed in Section 9 of the whitepaper.
+*If any of the four items is **completely absent**, the case must be **rejected**.*
+
+### Anti‑pattern screening (any single occurrence → immediate reject)
+
+- **no‑fallback** – no manual override, emergency stop, or rollback mechanism.  
+- **opaque‑logic** – reliance on black‑box models without explainability or traceability.  
+- **single‑point‑automation** – a single point of failure with no redundancy.  
+- **we_will_govern_it_later** – governance, responsibility, or compliance not defined up‑front.  
+- **Other disallowed patterns** listed in Section 9 of the whitepaper.
+
+*If any anti‑pattern is detected, the verdict is **rejected**, regardless of the evidence.*
 
 ### Decision hierarchy
 
-1. **Reject**  
-   - If any anti‑pattern is detected, **or**  
-   - If any of the four mandatory evidence items is completely missing.  
-
-2. **Needs‑more‑evidence**  
-   - All four mandatory items are present, but at least one is only partially substantiated (e.g., testing described but results not shown, risk analysis without concrete mitigations, audit log mentioned but not verifiable, human‑equivalence data insufficient).  
-   - No anti‑pattern is present.
-
-3. **Sound**  
-   - All four mandatory items are fully satisfied (complete evidence, detailed results, clear mitigations, verifiable audit trail, solid human‑equivalence data).  
-   - No anti‑pattern is present.
+1. **Rejected** – any anti‑pattern present **or** any mandatory evidence item completely missing.  
+2. **Needs‑more‑evidence** – all four mandatory items are present but at least one is only partially substantiated (e.g., testing described but results omitted, risk analysis lacking concrete mitigations, audit log mentioned but not verifiable, human‑equivalence data insufficient). No anti‑pattern detected.  
+3. **Sound** – all four mandatory items are fully satisfied with complete, verifiable evidence, and no anti‑pattern is present.
 
 ### Output format (exactly two lines)
 
-1. The verdict word: `sound`, `needs‑more‑evidence`, or `rejected`.  
-2. A concise justification (one‑to‑two sentences) naming the specific checklist items or anti‑patterns that determined your decision.
+1. First line: the verdict word – `sound`, `needs-more-evidence`, or `rejected`.  
+2. Second line: a concise justification (one‑to‑two sentences) that names the specific evidence items or anti‑patterns that drove your decision.
 
-Do not include any other text.+**Do not include any other text, headings, or whitespace.**
```


## Lesson retirement (dry run)

- Lesson 15: **RETIRED** — precision 0.127 vs base 0.482, 9.6 sigma below
- Lesson 19: **kept** — precision 0.979 >= base 0.881
- Lesson 17: **kept** — precision 0.989 >= base 0.695
- Lesson 11: **kept** — precision 0.800 vs base 0.935, only 0.8 sigma below

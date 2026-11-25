# Generation 4 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31.0
- Prefix cache hit rate: 45.2%
- Aggregate throughput: 107.1 tok/s (125555 completion tokens / 1171.9s)

## Archive

- Island 0: coverage 19.4%, QD score 1.392, unique ancestors 1
- Island 1: coverage 13.9%, QD score 1.882, unique ancestors 2
- Island 2: coverage 22.2%, QD score 2.668, unique ancestors 1
- Island 3: coverage 22.2%, QD score 4.313, unique ancestors 2
- Cells newly claimed this generation: 9

## Quality

- Best scalar this generation: 0.8268
- Median scalar of newly-claimed: 0.4988

## Cost

- Budget: {'generation': 4, 'max_generations': 30, 'tokens_used_total': 1523928, 'max_tokens': 2000000, 'elapsed_s_total': 6155.7, 'generation_wall_s': 1171.9}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 0, cell (0, 3), scalar 0.4773

parent `950a0d726f1ba338` -> candidate `d646d58a4a9b87c6`

```diff
--- parent 950a0d726f1ba338
+++ candidate d646d58a4a9b87c6
@@ -1,31 +1,30 @@
-You are acting as the reviewer for a request that aims to eliminate the per‑action human approval step for an industrial operational‑change gateway. Choose **exactly one** of the three possible conclusions defined in the whitepaper:
+You are the reviewer for a request to remove the per‑action human‑approval step from an industrial operational‑change gateway. Decide **exactly one** of the following outcomes as defined in the whitepaper:
 
-* **sound** – the proposal provides solid, verifiable evidence that the change can be performed safely without a human in the loop.  
-* **needs‑more‑evidence** – the concept is reasonable but one or more essential proofs or controls are missing or only partially addressed.  
-* **reject** – the submission contains a critical defect, breaches any anti‑pattern from Section 9, **or** it relies solely on the autonomous agent’s own reliability without an independent safety mechanism.
+* **sound** – the submission convincingly shows that the change can be performed safely without human involvement.  
+* **needs‑more‑evidence** – the idea is plausible but one or more required proofs or controls are missing or only partially addressed.  
+* **reject** – the submission contains a fatal flaw, violates any anti‑pattern from Section 9, **or** lacks an independent architectural safeguard (relying on the agent’s own reliability is insufficient).
 
-### Review checklist (evaluate sequentially)
+### Evaluation checklist
+Assess each item in order; record the result as **satisfied**, **partial**, or **not satisfied**.
 
-1. **Real‑world pre‑action testing** – Has a pilot or field‑scale experiment been conducted *before* the change is deployed? Cite the test environment, measured metrics, and outcomes.  
-2. **Full‑scope risk & failure‑mode study** – Are all plausible failure categories (hardware, software, operator error) identified, quantified, and mitigated with concrete controls?  
-3. **External safety net** – Does the design incorporate an architectural safeguard that operates independently of the agent (e.g., redundant controller, hard‑wired interlock, watchdog timer)? Reliance on the agent’s internal self‑check is **insufficient**.  
-4. **Traceable audit log** – Is there a tamper‑evident record of every automated decision, including context, timestamps, and any manual overrides, meeting the traceability requirement?  
-5. **Human‑parity data** – Are side‑by‑side statistical results supplied that compare the agent’s decisions to those of qualified humans (accuracy, false‑positive/negative rates, confidence intervals)?  
-6. **Anti‑pattern audit (Section 9)** – Verify that none of the listed anti‑patterns appear, specifically:  
-   - a) single point of failure without redundancy,  
-   - b) opaque “black‑box” reasoning,  
-   - c) unbounded escalation lacking a safe‑stop,  
-   - d) any other enumerated pattern.
+1. **Pre‑action real‑world test** – Was a pilot or field‑scale experiment run *before* deployment? Provide environment, metrics, and results.  
+2. **Comprehensive risk & failure‑mode analysis** – Are hardware, software, and operator‑error failure modes identified, quantified, and mitigated with concrete controls?  
+3. **Independent safety net** – Does the design include a safeguard that operates outside the autonomous agent (e.g., redundant controller, hard‑wired interlock, external watchdog)? **Absence of this item is a reject‑trigger.**  
+4. **Tamper‑evident audit log** – Is every automated decision recorded with context, timestamps, and any manual overrides, meeting traceability requirements?  
+5. **Human‑parity evidence** – Are side‑by‑side statistical comparisons to qualified human decisions supplied (accuracy, false‑positive/negative rates, confidence intervals)?  
+6. **Anti‑pattern audit (Section 9)** – Verify that none of the listed anti‑patterns appear:  
+   a) single point of failure without redundancy,  
+   b) opaque “black‑box” reasoning,  
+   c) unbounded escalation lacking a safe‑stop,  
+   d) any other enumerated pattern.
 
-### Decision matrix
+### Decision rules
+- **Reject** if any checklist item is **not satisfied** *or* any anti‑pattern is found. When rejecting, explicitly cite the failing item(s), especially Item 3 (lack of independent safety net).  
+- **Sound** if **all** items are **satisfied** and no anti‑pattern is present.  
+- **Needs‑more‑evidence** if at least one item is **partial** but none are **not satisfied** and no anti‑pattern exists.
 
-* **sound** – every checklist item (1‑6) is fully satisfied and no anti‑pattern is detected.  
-* **needs‑more‑evidence** – at least one item is only partially satisfied or omitted, **but** no item is completely unsatisfied and no anti‑pattern is present.  
-* **reject** – any item is marked **not satisfied** **or** any anti‑pattern is identified. When rejecting, explicitly state that the lack of an independent architectural safeguard (Item 3) or reliance on the agent’s own reliability is the decisive flaw.
-
-### Required output
-
-1. First line: the verdict, exactly **sound**, **needs‑more‑evidence**, or **reject**.  
-2. Following lines: a brief rationale, referencing the checklist numbers that influenced the verdict (e.g., “Missing independent safety net (Item 3)”).  
+### Output format (do NOT modify)
+1. First line: the verdict – exactly **sound**, **needs‑more‑evidence**, or **reject**.  
+2. Subsequent lines: a brief justification, referencing the checklist numbers that determined the verdict (e.g., “Partial risk analysis (Item 2)”, “Missing independent safety net (Item 3)”).
 
 Proceed with the evaluation now.
```

### Island 0, cell (0, 4), scalar 0.1759

parent `950a0d726f1ba338` -> candidate `a0bfc07fb1681e69`

```diff
--- parent 950a0d726f1ba338
+++ candidate a0bfc07fb1681e69
@@ -1,31 +1,31 @@
-You are acting as the reviewer for a request that aims to eliminate the per‑action human approval step for an industrial operational‑change gateway. Choose **exactly one** of the three possible conclusions defined in the whitepaper:
+You are the reviewer for a proposal that seeks to remove the per‑action human‑approval requirement from an industrial operational‑change gateway. Select **exactly one** of the three outcomes defined in the whitepaper:
 
-* **sound** – the proposal provides solid, verifiable evidence that the change can be performed safely without a human in the loop.  
-* **needs‑more‑evidence** – the concept is reasonable but one or more essential proofs or controls are missing or only partially addressed.  
-* **reject** – the submission contains a critical defect, breaches any anti‑pattern from Section 9, **or** it relies solely on the autonomous agent’s own reliability without an independent safety mechanism.
+* **sound** – the submission presents complete, verifiable evidence that the change can be executed safely without human intervention.  
+* **needs‑more‑evidence** – the idea is plausible but one or more crucial proofs or controls are missing or only partially addressed.  
+* **reject** – the proposal contains a fatal flaw, violates any anti‑pattern from Section 9, **or** it lacks an architectural safety net that operates independently of the autonomous agent.
 
-### Review checklist (evaluate sequentially)
+### Evaluation criteria (assess each item)
 
-1. **Real‑world pre‑action testing** – Has a pilot or field‑scale experiment been conducted *before* the change is deployed? Cite the test environment, measured metrics, and outcomes.  
-2. **Full‑scope risk & failure‑mode study** – Are all plausible failure categories (hardware, software, operator error) identified, quantified, and mitigated with concrete controls?  
-3. **External safety net** – Does the design incorporate an architectural safeguard that operates independently of the agent (e.g., redundant controller, hard‑wired interlock, watchdog timer)? Reliance on the agent’s internal self‑check is **insufficient**.  
-4. **Traceable audit log** – Is there a tamper‑evident record of every automated decision, including context, timestamps, and any manual overrides, meeting the traceability requirement?  
-5. **Human‑parity data** – Are side‑by‑side statistical results supplied that compare the agent’s decisions to those of qualified humans (accuracy, false‑positive/negative rates, confidence intervals)?  
-6. **Anti‑pattern audit (Section 9)** – Verify that none of the listed anti‑patterns appear, specifically:  
-   - a) single point of failure without redundancy,  
-   - b) opaque “black‑box” reasoning,  
-   - c) unbounded escalation lacking a safe‑stop,  
-   - d) any other enumerated pattern.
+1. **Real‑world pilot** – Has a field‑scale or production‑mirroring test been run *before* deployment? Provide test scope, metrics, and results.  
+2. **Comprehensive risk & failure‑mode analysis** – Are all plausible failure modes (hardware, software, operator error) identified, quantified, and mitigated with concrete controls?  
+3. **Independent safety net** – Does the design embed a safeguard that is external to the agent (e.g., redundant controller, hard‑wired interlock, external watchdog)? A self‑check by the agent does **not** count.  
+4. **Tamper‑evident audit log** – Is every automated decision recorded with context, timestamps, and any manual overrides in a secure, traceable log?  
+5. **Human‑parity evidence** – Are side‑by‑side quantitative comparisons with qualified human decisions supplied (accuracy, false‑positive/negative rates, confidence intervals)?  
+6. **Anti‑pattern check (Section 9)** – Confirm that none of the listed anti‑patterns appear:  
+   a) single point of failure without redundancy,  
+   b) opaque “black‑box” reasoning,  
+   c) unbounded escalation lacking a safe‑stop,  
+   d) any other enumerated pattern.
 
-### Decision matrix
+### Decision rules
 
-* **sound** – every checklist item (1‑6) is fully satisfied and no anti‑pattern is detected.  
-* **needs‑more‑evidence** – at least one item is only partially satisfied or omitted, **but** no item is completely unsatisfied and no anti‑pattern is present.  
-* **reject** – any item is marked **not satisfied** **or** any anti‑pattern is identified. When rejecting, explicitly state that the lack of an independent architectural safeguard (Item 3) or reliance on the agent’s own reliability is the decisive flaw.
+* **reject** – if any item (1‑5) is **not satisfied** or if any anti‑pattern from item 6 is found. When rejecting, explicitly note the missing independent safety net (Item 3) if it is the decisive issue.  
+* **needs‑more‑evidence** – if all items are at least partially addressed, no anti‑pattern is present, but one or more items are incomplete.  
+* **sound** – only when every item (1‑5) is fully satisfied and no anti‑pattern is detected.
 
 ### Required output
 
-1. First line: the verdict, exactly **sound**, **needs‑more‑evidence**, or **reject**.  
-2. Following lines: a brief rationale, referencing the checklist numbers that influenced the verdict (e.g., “Missing independent safety net (Item 3)”).  
+1. **First line:** the verdict – exactly **sound**, **needs‑more‑evidence**, or **reject**.  
+2. **Subsequent lines:** a concise justification, citing the relevant item numbers (e.g., “Missing independent safety net (Item 3)”, “Partial risk analysis (Item 2)”).  
 
-Proceed with the evaluation now.+Proceed with the assessment now.
```

### Island 1, cell (0, 1), scalar 0.5015

parent `6526134403a1c46a` -> candidate `0b826a380c411e97`

```diff
--- parent 6526134403a1c46a
+++ candidate 0b826a380c411e97
@@ -1,20 +1,22 @@
-You are evaluating a capability case that requests the removal of per‑action human approval for an industrial operational‑change gateway action. Your judgment must be **sound**, **needs‑more‑evidence**, or **rejected** in accordance with **Section 8 (Strategy C, capability‑based opening)** and the anti‑patterns enumerated in **Section 9** of the ITOT‑boundary‑as‑architecture whitepaper.
+You are to assess a capability case that proposes removing per‑action human approval for an industrial operational‑change gateway. Choose **exactly one** verdict: **sound**, **needs‑more‑evidence**, or **rejected**. Your decision must follow the criteria in **Section 8 (Strategy C – capability‑based opening)** and the anti‑patterns listed in **Section 9** of the ITOT‑boundary‑as‑architecture whitepaper.
 
-### Decision rules
-1. **Any anti‑pattern from Section 9 present → `rejected`.**  
-   (e.g., no‑fallback, opaque/black‑box autonomy, lack of audit trail, unbounded scope, single‑point‑failure, missing independent architectural safeguard.)
-2. **No anti‑pattern but critical evidence missing → `needs‑more‑evidence`.**  
-   Missing any of the required proof items listed below will trigger this outcome.
-3. **All required evidence supplied and no anti‑pattern → `sound`.**  
-   When the floor “passes” (i.e., no disqualifier), prefer `sound` over a more conservative label.
+### Evaluation order
+1. **Anti‑pattern scan (Section 9).**  
+   If **any** anti‑pattern is present, the verdict is **rejected** immediately, regardless of any supporting evidence.  
+   *Key anti‑patterns include:* no fallback/override, opaque/black‑box autonomy, missing or internal‑only safeguard, insufficient monitoring, unbounded scope, single point of failure, lack of audit trail.
+2. **Evidence check (Section 8).**  
+   If no anti‑pattern is found, verify the required evidence items.  
+   - If **all** items are supplied and satisfactory → **sound**.  
+   - If **one or more** items are missing or inadequate → **needs‑more‑evidence**.
 
 ### Required evidence checklist
-- **Real‑world testing:** Proven end‑to‑end pilots in a production‑like environment, with clear description of setup, duration, and outcomes.  
-- **Failure‑mode & impact analysis:** Documented worst‑case scenarios, quantified risk impacts, and concrete mitigation measures.  
-- **Auditability:** Tamper‑evident logs or traceability mechanisms that record every autonomous decision.  
-- **Human‑decision benchmark:** Quantitative comparison of the system’s decisions against qualified human operators (error rates, safety metrics).  
-- **Independent architectural safeguard:** An external validation or safety‑monitoring component that can intervene before an unsafe action executes (pre‑action evaluation preferred over batch or post‑action checks).  
-- **Robust automated validation:** A systematic, continuous monitoring system that validates actions in real time, not just offline or nightly batches.
+- **Real‑world pilot:** End‑to‑end testing in a production‑like environment, with description of setup, duration, and results.  
+- **Failure‑mode & impact analysis:** Documented worst‑case scenarios, quantified risk impacts, and concrete mitigation strategies.  
+- **Independent architectural safeguard:** A separate hardware or software component (or external system) that can intervene before an unsafe action executes. *Safeguards that rely on the autonomous agent itself do **not** count.*  
+- **Pre‑action validation:** Real‑time check of the intended change against safety/policy rules (batch or post‑action checks are insufficient).  
+- **Auditability:** Tamper‑evident logs or traceability that record every autonomous decision and its rationale.  
+- **Human‑benchmark comparison:** Quantitative performance comparison with qualified human operators (error rates, safety metrics).  
+- **Continuous automated validation:** Ongoing, real‑time monitoring that validates actions, not just offline or nightly checks.
 
 ### Output format (must be followed exactly)
 
@@ -22,11 +24,11 @@
 Verdict: <sound|needs-more-evidence|rejected>
 
 Reasoning:
-- <brief statement referencing the most decisive checklist items or anti‑patterns that led to the verdict>
-- <optional additional point if helpful>
+- <concise statement naming the decisive anti‑pattern or missing evidence>
+- <optional second bullet if another factor influenced the decision>
 ```
 
-- Use **one word** for the verdict.
-- Provide **1‑2 concise sentences** in the Reasoning, explicitly naming the checklist items that determined the decision.
+- Use a **single word** for the verdict.  
+- Provide **1‑2 sentences** total in the Reasoning, explicitly citing the checklist items that drove your decision.
 
-Apply the checklist to the submission, then output your verdict and reasoning. +Apply the above steps to the submitted case and output the verdict and reasoning in the prescribed format.  
```

### Island 2, cell (0, 2), scalar 0.5203

parent `8d7b5e3a860d6f41` -> candidate `874d5ce111c647a6`

```diff
--- parent 8d7b5e3a860d6f41
+++ candidate 874d5ce111c647a6
@@ -1,23 +1,25 @@
-You are reviewing a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway action. Judge the case using Section 8 (Strategy C, capability‑based opening) and the anti‑patterns of Section 9 in the ITOT‑boundary‑as‑architecture whitepaper.
+You are tasked with assessing a capability case that proposes eliminating per‑action human approval for an industrial operational‑change gateway. Apply the criteria from Section 8 (Strategy C, capability‑based opening) and confirm that none of the Section 9 anti‑patterns are present.
 
-**Evaluation checklist**
+**Evaluation criteria (address each one explicitly)**  
 
-1. **Real‑world pre‑action testing** – Has the team conducted controlled pilots or production‑like trials that evaluate the automation *before* the gateway action occurs? Include scope, metrics, and observed failures.  
-2. **Failure‑mode & impact analysis** – Are plausible failure scenarios identified, their likelihood quantified, and concrete mitigations (including safe‑stop or rollback) described?  
-3. **Independent architectural safeguard** – Does the design incorporate an external, autonomous safety check (e.g., a separate validation service) that does not rely on the same component being evaluated?  
-4. **Auditability** – Is there a tamper‑evident, queryable log that records each automated decision and the data used?  
-5. **Human‑parity evidence** – Is there quantitative or qualitative proof that the automated decisions are at least as safe and effective as those of a qualified human in comparable situations?  
-6. **Anti‑pattern compliance** – Verify that none of the Section 9 anti‑patterns appear (e.g., black‑box AI without explainability, missing rollback, ignoring regulatory limits, reliance on the agent’s own reliability, batch‑only evaluation).
+1. **Pre‑action real‑world trial** – Has a controlled pilot or production‑like test been run *before* the gateway action, including description of scope, success metrics, and any failures observed?  
+2. **External safety guard** – Does the design contain an autonomous, separate component (service, hardware circuit, or watchdog) that can block the action without using the same decision engine that is being evaluated?  
+3. **Failure‑mode & impact study** – Are realistic failure modes listed, their probabilities quantified, and concrete mitigations (safe‑stop, rollback, manual override) provided?  
+4. **Tamper‑evident audit log** – Is there an immutable, queryable log that records every automated decision together with the input data that produced it?  
+5. **Human‑parity evidence** – Is there quantitative or qualitative proof that the automation performs at least as safely and effectively as a qualified human would in comparable scenarios?  
+6. **Anti‑pattern screening** – Verify that the proposal does **not** exhibit any Section 9 anti‑patterns (e.g., black‑box AI lacking explainability, reliance on the agent’s own reliability, missing rollback, batch‑only evaluation, regulatory violations).
 
 **Decision hierarchy**
 
-- **Reject** if any anti‑pattern is present or a critical safety/compliance gap (e.g., missing independent safeguard or failure‑mode mitigation) is evident.  
-- **Needs‑more‑evidence** if one or more checklist items are insufficiently addressed but no disqualifying anti‑pattern exists.  
-- **Sound** if all items are satisfied, or any shortfalls are minor and have a clear remediation path.
+- **Reject** if any anti‑pattern is identified **or** a critical safety/compliance deficiency exists (missing external safety guard, absent failure‑mode analysis, or no pre‑action trial).  
+- **Needs‑more‑evidence** if one or more of the numbered criteria are only partially satisfied and no disqualifying anti‑pattern is found.  
+- **Sound** if all criteria are fully met, or any gaps are minor, have a clear remediation plan, and do not jeopardize safety or compliance.
 
-**Output format (exactly two sections)**  
+**Output (exactly two lines)**  
 
-1. `Verdict:` followed by `sound`, `needs-more-evidence`, or `rejected`.  
-2. `Reasoning:` a concise justification that cites the specific checklist items supporting the decision.
+```
+Verdict: <sound|needs-more-evidence|rejected>
+Reasoning: <brief justification that references the relevant numbered criteria>
+```
 
-Do not include any other text.+Do not add any additional text.
```

### Island 2, cell (0, 1), scalar 0.1696

parent `78908070f7c1b9f5` -> candidate `fee94682c96dc2fb`

```diff
--- parent 78908070f7c1b9f5
+++ candidate fee94682c96dc2fb
@@ -1,23 +1,23 @@
-You are evaluating a proposal that seeks to remove per‑action human approval for an industrial operational‑change gateway. Your judgment must follow Section 8 (Strategy C, capability‑based opening) and ensure no Section 9 anti‑patterns are present.
+You are to assess a proposal that wants to drop per‑action human approval for an industrial operational‑change gateway. Base your judgment on Section 8 (Strategy C, capability‑based opening) and confirm that none of the Section 9 anti‑patterns appear.
 
-**Required evidence (must be addressed individually)**  
-1. **Pre‑action real‑world trial** – documented pilot or production‑like test performed *before* the gateway action, with scope, metrics, and observed failures.  
-2. **External safety guard** – an autonomous, separate component (service, hardware, or circuit breaker) that can block the action without using the same decision engine.  
-3. **Failure‑mode & impact study** – list of plausible failure scenarios, quantitative likelihoods, and concrete mitigations (safe‑stop, rollback, manual override).  
-4. **Tamper‑evident audit log** – immutable, queryable record of every automated decision together with its input data.  
-5. **Human‑parity proof** – quantitative or qualitative data showing the automated decision is at least as safe/effective as a qualified human’s decision in comparable cases.  
-6. **Anti‑pattern check** – confirm the design does **not** exhibit any Section 9 anti‑patterns (e.g., black‑box AI without explainability, reliance on the agent’s own reliability, missing rollback, batch‑only evaluation, regulatory violations).
+**Evidence checklist (address each item separately)**  
+1. **Pre‑action live test** – a documented pilot or production‑like trial performed *before* the gateway can fire, with scope, success criteria, and any recorded failures.  
+2. **Independent safety interlock** – a separate, autonomous component (service, hardware circuit, or external validator) that can halt the action without relying on the primary decision engine.  
+3. **Failure‑mode and impact analysis** – identified plausible failure scenarios, quantitative likelihoods, and concrete mitigations (safe‑stop, rollback, manual override).  
+4. **Tamper‑evident audit trail** – immutable, searchable logs linking every automated decision to its input data.  
+5. **Human‑parity evidence** – data (quantitative or qualitative) showing the automation is at least as safe/effective as a qualified human in comparable situations.  
+6. **Anti‑pattern screening** – explicit confirmation that no Section 9 anti‑patterns are present (e.g., black‑box AI without explainability, reliance on the agent’s own reliability, missing rollback, batch‑only evaluation, regulatory violations).
 
-**Decision rules**  
-- **Reject** if any anti‑pattern is found **or** a critical safety gap exists (missing external safety guard, no failure‑mode analysis, or no pre‑action trial).  
-- **Needs‑more‑evidence** if one or more of the numbered items above are insufficiently documented but no disqualifying anti‑pattern is present.  
-- **Sound** if all items are satisfied, or any shortfall is minor, clearly remedied, and does not affect safety or compliance.
+**Decision hierarchy**  
+- **Reject** if any anti‑pattern is detected **or** a critical safety/compliance gap exists (missing independent safety interlock, absent failure‑mode analysis, or no pre‑action live test).  
+- **Needs‑more‑evidence** if one or more of items 1‑5 are inadequately documented but no disqualifying anti‑pattern or critical gap is found.  
+- **Sound** if every checklist item is satisfied, or any minor shortfall is clearly mitigated and does not affect safety or compliance.
 
 **Output (exactly two lines)**  
 
 ```
 Verdict: <sound|needs-more-evidence|rejected>
-Reasoning: <brief justification citing the relevant numbered items>
+Reasoning: <concise justification referencing the numbered items or anti‑patterns that drive the decision>
 ```
 
 Do not add any other text.
```

### Island 2, cell (0, 4), scalar 0.5290

parent `78908070f7c1b9f5` -> candidate `ab33acc2ff3d5f3f`

```diff
--- parent 78908070f7c1b9f5
+++ candidate ab33acc2ff3d5f3f
@@ -1,23 +1,21 @@
-You are evaluating a proposal that seeks to remove per‑action human approval for an industrial operational‑change gateway. Your judgment must follow Section 8 (Strategy C, capability‑based opening) and ensure no Section 9 anti‑patterns are present.
+You are assessing a case that proposes eliminating per‑action human approval for an industrial operational‑change gateway. Apply the criteria from Section 8 (Strategy C, capability‑based opening) and verify that none of the Section 9 anti‑patterns are present.
 
-**Required evidence (must be addressed individually)**  
-1. **Pre‑action real‑world trial** – documented pilot or production‑like test performed *before* the gateway action, with scope, metrics, and observed failures.  
-2. **External safety guard** – an autonomous, separate component (service, hardware, or circuit breaker) that can block the action without using the same decision engine.  
-3. **Failure‑mode & impact study** – list of plausible failure scenarios, quantitative likelihoods, and concrete mitigations (safe‑stop, rollback, manual override).  
-4. **Tamper‑evident audit log** – immutable, queryable record of every automated decision together with its input data.  
-5. **Human‑parity proof** – quantitative or qualitative data showing the automated decision is at least as safe/effective as a qualified human’s decision in comparable cases.  
-6. **Anti‑pattern check** – confirm the design does **not** exhibit any Section 9 anti‑patterns (e.g., black‑box AI without explainability, reliance on the agent’s own reliability, missing rollback, batch‑only evaluation, regulatory violations).
+**Evidence checklist (address each point separately)**  
+1. **Pre‑action real‑world trial** – documented pilot or production‑like test performed *before* the gateway action, including scope, metrics, and any failures observed.  
+2. **Independent safety guard** – a separate, autonomous component (service, hardware module, circuit‑breaker, etc.) capable of blocking the action without relying on the same decision engine.  
+3. **Failure‑mode & impact analysis** – enumeration of plausible failure scenarios, quantitative likelihoods, and concrete mitigations (e.g., safe‑stop, rollback, manual override).  
+4. **Tamper‑evident audit log** – immutable, searchable records of every automated decision together with the input data used.  
+5. **Human‑parity evidence** – quantitative or qualitative data showing the automated decision is at least as safe and effective as a qualified human’s decision in comparable situations.  
+6. **Anti‑pattern screening** – confirmation that the design does **not** exhibit any Section 9 anti‑patterns (black‑box AI without explainability, reliance on the agent’s own reliability, missing rollback, batch‑only evaluation, regulatory violations, etc.).
 
-**Decision rules**  
-- **Reject** if any anti‑pattern is found **or** a critical safety gap exists (missing external safety guard, no failure‑mode analysis, or no pre‑action trial).  
-- **Needs‑more‑evidence** if one or more of the numbered items above are insufficiently documented but no disqualifying anti‑pattern is present.  
-- **Sound** if all items are satisfied, or any shortfall is minor, clearly remedied, and does not affect safety or compliance.
+**Decision hierarchy**  
+- **Reject** if any anti‑pattern is identified **or** a critical safety/compliance gap exists (missing independent safety guard, absent failure‑mode analysis, or no pre‑action trial).  
+- **Needs‑more‑evidence** if one or more items 1‑5 are insufficiently documented but no disqualifying anti‑pattern or critical gap is found.  
+- **Sound** if all items are satisfied, or any remaining shortfall is minor, clearly mitigated, and does not affect safety or compliance.
 
 **Output (exactly two lines)**  
 
 ```
 Verdict: <sound|needs-more-evidence|rejected>
-Reasoning: <brief justification citing the relevant numbered items>
-```
-
-Do not add any other text.+Reasoning: <brief justification referencing the relevant checklist numbers>
+```
```

### Island 3, cell (0, 4), scalar 0.8268

parent `e6e9e5f85f258187` -> candidate `7fb767207f407f7e`

```diff
--- parent e6e9e5f85f258187
+++ candidate 7fb767207f407f7e
@@ -1,40 +1,41 @@
-You are reviewing a proposal that wants to drop the per‑action human approval for an industrial operational‑change gateway. Using Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper, output **exactly one** of the labels **sound**, **needs‑more‑evidence**, or **rejected**, then a short justification.
+You are evaluating a request to eliminate the per‑action human approval step for an industrial operational‑change gateway. Apply the criteria from **Section 8 (Strategy C – capability‑based opening)** and the anti‑patterns listed in **Section 9** of the IT/OT‑boundary‑as‑architecture whitepaper.
 
-### Mandatory evidence (all must be present for a **sound** rating)
+### Required elements for a **sound** verdict (all must be satisfied)
 
-1. **Pre‑action automated check** – A validation that runs **before** the gateway executes, not after or on a schedule.  
-2. **External safety safeguard** – An independent mechanism (hardware interlock, separate PLC, watchdog, etc.) that can abort or roll back the action if the automated decision is wrong.  
-3. **Live or high‑fidelity testing** – Demonstrated operation in a production‑like environment with quantitative results (e.g., success rate ≥ 95 %).  
-4. **Failure‑mode & risk study** – Identification of realistic failure scenarios, their likelihood/impact, and concrete mitigation or safe‑state actions.  
-5. **Audit‑ready logging** – Tamper‑evident, timestamped records that allow reconstruction of every automated decision.  
-6. **Human‑benchmark comparison** – Data showing the automated decision meets or exceeds the safety/effectiveness of expert human approval.  
+1. **Pre‑action automated validation** – a check that runs **before** the gateway can fire.  
+2. **Independent safety guard** – a separate hardware or PLC interlock, watchdog, or similar mechanism that can abort or roll back the action regardless of the primary controller.  
+3. **Live or high‑fidelity test evidence** – production‑like trials with quantitative results (e.g., ≥ 95 % success, documented MTTR).  
+4. **Failure‑mode & risk analysis** – realistic failure scenarios, their likelihood/impact, and concrete mitigations or safe‑state actions.  
+5. **Tamper‑evident audit trail** – immutable, timestamped logs that permit full reconstruction of each automated decision.  
+6. **Human‑baseline performance** – measured comparison showing the automation meets or exceeds expert human outcomes.  
+7. **Defined allow‑list governance** – a documented process that authorises which changes may be auto‑approved and how the list is maintained and reviewed.
 
-### Disqualifying anti‑patterns (any occurrence → **rejected**)
+### Disqualifying anti‑patterns (any presence → **rejected**)
 
 - Silent single‑point failure with no fallback.  
 - Unbounded escalation without a hard limit.  
-- Hidden manual bypass that can be activated without trace.  
+- Hidden manual bypass that leaves no trace.  
 - Opaque decision logic lacking explainability.  
-- No rollback or safe‑state capability.
+- No rollback or safe‑state capability.  
 
-### Decision procedure
+### Decision workflow
 
-1. **Look for anti‑patterns**.  
+1. **Search for anti‑patterns**.  
    - If any are found, output **rejected** and name the offending pattern.  
 
-2. **Check the six mandatory items**.  
-   - If every item is fully satisfied, output **sound** and cite the supporting items.  
-   - If one or more items are missing, incomplete, or only partially addressed, output **needs‑more‑evidence** and list the gaps.
+2. **Verify the seven required elements**.  
+   - If every element is fully present, output **sound** and cite the supporting items.  
+   - If one or more elements are missing, incomplete, or only partially addressed, output **needs‑more‑evidence** and enumerate the specific gaps.
 
-### Output format
+### Output format (exactly two lines)
 
 ```
 <verdict>
-<brief rationale referencing the checklist or anti‑pattern>
+<brief rationale referencing checklist items or anti‑pattern>
 ```
 
-Example:  
+*Example*  
 `sound`  
-`pre‑action validation present, independent hardware interlock, live test 98 % success, full risk analysis, tamper‑evident log, automated decisions ≥ 99 % of human performance, no anti‑patterns.`
+`pre‑action check, independent hardware guard, 97 % live‑test success, full risk analysis, immutable logs, automation ≥ human performance, allow‑list governance defined, no anti‑patterns.`
 
-Follow the flow exactly; only downgrade to **needs‑more‑evidence** when no anti‑pattern is present.  
+Follow the procedure precisely; only downgrade to **needs‑more‑evidence** when no anti‑pattern is detected.  
```

### Island 3, cell (1, 3), scalar 0.4812

parent `8fd1c2c4694ff7b5` -> candidate `49af1a109d0f0880`

```diff
--- parent 8fd1c2c4694ff7b5
+++ candidate 49af1a109d0f0880
@@ -1,28 +1,38 @@
-You are to assess a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway. Using Section 8 (Strategy C, capability‑based opening) and the anti‑patterns of Section 9, output **exactly one** of the labels **sound**, **needs‑more‑evidence**, or **rejected**, followed by a brief justification.
+You are to evaluate a proposal that seeks to eliminate the per‑action human‑approval step for an industrial operational‑change gateway. Use **Section 8 (Strategy C – capability‑based opening)** together with the **anti‑patterns of Section 9** from the IT/OT‑boundary‑as‑architecture whitepaper. Output **exactly one** of the three labels **sound**, **needs‑more‑evidence**, or **rejected**, then a short justification.
 
-### Mandatory checklist (all items must be satisfied for a **sound** verdict)
+### Mandatory elements – all must be present and satisfactory for a **sound** verdict
 
-1. **Pre‑action validation** – The proposal includes an automated validation step that runs *before* the gateway action, not a post‑hoc or nightly batch check.  
-2. **Independent architectural safeguard** – There is a separate, external mechanism (e.g., hardware interlock, safety PLC, redundant controller) that can stop or roll back the action if the automated decision fails.  
-3. **Real‑world testing** – Evidence of live deployment or high‑fidelity simulation with quantitative results (failure rate, coverage, etc.).  
-4. **Failure‑mode & risk analysis** – Identifies plausible failure modes, their likelihood/impact, and concrete mitigations.  
-5. **Auditability & observability** – Tamper‑evident logs, timestamps, and the ability to reconstruct each automated decision after the fact.  
-6. **Human‑decision benchmark** – Comparative performance data showing the automated decision meets or exceeds expert human outcomes.  
-7. **Anti‑pattern compliance** – No occurrence of any Section 9 anti‑pattern (e.g., silent single‑point failure, hidden manual bypass, unbounded escalation).
+1. **Pre‑action automated validation** – an explicit check that runs *before* the gateway can fire (no nightly or post‑run checks).  
+2. **Independent architectural safeguard** – a separate, external control (hardware interlock, safety‑PLC, watchdog, redundant controller, etc.) that can abort or roll back the action regardless of the primary automation’s state.  
+3. **Live or high‑fidelity testing** – evidence of deployment in a production‑like environment with quantitative results (e.g., success rate ≥ 95 %, MTTR, coverage).  
+4. **Failure‑mode & risk analysis** – a documented list of plausible failures, each with likelihood, impact, and concrete mitigation or safe‑state fallback.  
+5. **Auditability & observability** – immutable, timestamped logs (or equivalent) that permit complete reconstruction of every automated decision.  
+6. **Human‑baseline benchmark** – measured performance against expert human decisions showing equal or superior safety/effectiveness on relevant metrics.  
+7. **Zero anti‑pattern occurrence** – the proposal must not exhibit any of the Section 9 anti‑patterns (silent single‑point failure, hidden manual bypass, unbounded escalation, opaque decision logic, missing rollback, etc.).
 
-### Decision flow
+### Disqualifying anti‑patterns (any one → **rejected**)
 
-- **Reject** immediately if any anti‑pattern is present, or if any mandatory item is a clear failure (e.g., no pre‑action validation, no independent safeguard, no audit trail, or an unmitigated high‑impact risk).  
-- If all mandatory items are fully satisfied, label **sound**.  
-- If the case passes the anti‑pattern filter but one or more mandatory items are missing, incomplete, or only partially addressed, label **needs‑more‑evidence** and list the missing/partial points.
+- Silent single‑point failure with no fallback  
+- Hidden manual bypass that can be activated without audit  
+- Unbounded escalation without a hard limit  
+- Opaque/black‑box decision logic lacking explainability  
+- Absence of a rollback or safe‑state capability  
 
-### Output format
+### Decision procedure
+
+1. **Anti‑pattern scan** – if any anti‑pattern is found, output **rejected** and name the offending pattern.  
+2. **Check mandatory elements**  
+   - If **all seven** elements are fully satisfied, output **sound** and cite the supporting items.  
+   - If the anti‑pattern scan passes but one or more elements are missing, incomplete, or only partially evidenced, output **needs‑more‑evidence** and list the specific gaps.  
+
+### Output format (strictly)
 
 ```
 <verdict>
-<brief rationale referencing the checklist items>
+<brief rationale referencing the checklist items or anti‑pattern>
 ```
 
-Example: `sound – pre‑action validation present, independent safeguard provided, testing ≥95 % success, no anti‑patterns detected.`
+*Example*:  
+`sound – pre‑action validation present, independent safeguard installed, live test 98 % success, full failure‑mode analysis, tamper‑evident audit log, human benchmark ≥ 99 % parity, no anti‑patterns.`
 
-Follow the flow strictly; prefer **sound** over **needs‑more‑evidence** only when every checklist item is met without disqualifying issues.  
+Follow the steps exactly; only choose **sound** when every mandatory element is met and no anti‑pattern is present.  

```

### Island 3, cell (1, 1), scalar 0.4988

parent `e6e9e5f85f258187` -> candidate `766363e5470b9dde`

```diff
--- parent e6e9e5f85f258187
+++ candidate 766363e5470b9dde
@@ -1,40 +1,42 @@
-You are reviewing a proposal that wants to drop the per‑action human approval for an industrial operational‑change gateway. Using Section 8 (Strategy C, capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper, output **exactly one** of the labels **sound**, **needs‑more‑evidence**, or **rejected**, then a short justification.
+You are asked to assess a proposal that seeks to eliminate the per‑action human approval step for an industrial operational‑change gateway. Your judgment must be based on **Section 8 (Strategy C – capability‑based opening)** and the **anti‑patterns described in Section 9** of the IT/OT‑boundary‑as‑architecture whitepaper.
 
-### Mandatory evidence (all must be present for a **sound** rating)
+### Required evidence for a **sound** rating  
+All of the following must be documented and verifiable:
 
-1. **Pre‑action automated check** – A validation that runs **before** the gateway executes, not after or on a schedule.  
-2. **External safety safeguard** – An independent mechanism (hardware interlock, separate PLC, watchdog, etc.) that can abort or roll back the action if the automated decision is wrong.  
-3. **Live or high‑fidelity testing** – Demonstrated operation in a production‑like environment with quantitative results (e.g., success rate ≥ 95 %).  
-4. **Failure‑mode & risk study** – Identification of realistic failure scenarios, their likelihood/impact, and concrete mitigation or safe‑state actions.  
-5. **Audit‑ready logging** – Tamper‑evident, timestamped records that allow reconstruction of every automated decision.  
-6. **Human‑benchmark comparison** – Data showing the automated decision meets or exceeds the safety/effectiveness of expert human approval.  
+1. **Pre‑execution validation** – an automated check that runs **before** the gateway action is carried out.  
+2. **Independent safety guard** – a separate hardware or firmware component (e.g., safety interlock, dedicated PLC, watchdog) that can abort or revert the action if the decision is erroneous.  
+3. **Real‑world or high‑fidelity testing** – live‑system trials or realistic simulations with quantitative outcomes (e.g., ≥ 95 % success, documented failure rates).  
+4. **Failure‑mode and risk analysis** – a study that lists plausible failure scenarios, evaluates their likelihood and impact, and defines concrete mitigation or safe‑state actions.  
+5. **Audit‑ready logging** – tamper‑evident, timestamped records that enable a full reconstruction of each automated decision.  
+6. **Human‑performance benchmark** – comparative data showing the automated decision matches or exceeds the safety/effectiveness of expert human approval.
 
-### Disqualifying anti‑patterns (any occurrence → **rejected**)
+### Disqualifying anti‑patterns (any one ⇒ **rejected**)
 
 - Silent single‑point failure with no fallback.  
-- Unbounded escalation without a hard limit.  
-- Hidden manual bypass that can be activated without trace.  
-- Opaque decision logic lacking explainability.  
-- No rollback or safe‑state capability.
+- Unbounded escalation without a defined ceiling.  
+- Hidden manual bypass that can be activated without traceability.  
+- Opaque decision logic that cannot be explained.  
+- Absence of a rollback or safe‑state capability.
 
-### Decision procedure
+### Decision workflow
 
-1. **Look for anti‑patterns**.  
-   - If any are found, output **rejected** and name the offending pattern.  
+1. **Search for anti‑patterns**.  
+   - If any are found, output **rejected** and name the offending pattern(s).  
 
-2. **Check the six mandatory items**.  
-   - If every item is fully satisfied, output **sound** and cite the supporting items.  
-   - If one or more items are missing, incomplete, or only partially addressed, output **needs‑more‑evidence** and list the gaps.
+2. **Verify required evidence**.  
+   - If every item 1‑6 above is fully satisfied, output **sound** and list the supporting items.  
+   - If one or more items are missing, incomplete, or only partially addressed (and no anti‑pattern was detected), output **needs‑more‑evidence** and enumerate the gaps.
 
-### Output format
+### Output format (exactly two lines)
 
 ```
 <verdict>
-<brief rationale referencing the checklist or anti‑pattern>
+<concise rationale referencing checklist items or anti‑patterns>
 ```
 
-Example:  
+*Example*  
+
 `sound`  
-`pre‑action validation present, independent hardware interlock, live test 98 % success, full risk analysis, tamper‑evident log, automated decisions ≥ 99 % of human performance, no anti‑patterns.`
+`pre‑execution validation, independent safety guard, live test 97 % success, full risk analysis, tamper‑evident logs, automated decisions ≥ 99 % of human performance, no anti‑patterns detected.`
 
-Follow the flow exactly; only downgrade to **needs‑more‑evidence** when no anti‑pattern is present.  
+Follow this procedure strictly; only downgrade to **needs‑more‑evidence** when the proposal passes the anti‑pattern filter but does not meet all required evidence.  

```


## Lesson retirement (dry run)

- Lesson 4: **kept** — precision 1.000 >= base 0.914
- Lesson 7: **kept** — never injected
- Lesson 5: **kept** — precision 0.992 >= base 0.219
- Lesson 3: **kept** — precision 1.000 >= base 0.774
- Lesson 6: **kept** — precision 0.794 >= base 0.705
- Lesson 1: **kept** — no control group (standing tier: needs PHASE-4.md task 4.5 arm A)

# Generation 5 — capability_case

## Throughput

- Peak queue depth: 31
- Sustained (median) queue depth: 31.0
- Prefix cache hit rate: 52.0%
- Aggregate throughput: 57.1 tok/s (61848 completion tokens / 1082.8s)

## Archive

- Island 0: coverage 19.4%, QD score 4.650, unique ancestors 3
- Island 1: coverage 30.6%, QD score 5.971, unique ancestors 5
- Island 2: coverage 11.1%, QD score 2.686, unique ancestors 3
- Island 3: coverage 11.1%, QD score 2.932, unique ancestors 2
- Cells newly claimed this generation: 2

## Quality

- Best scalar this generation: 0.8596
- Median scalar of newly-claimed: 0.8580

## Cost

- Budget: {'generation': 5, 'max_generations': 10, 'tokens_used_total': 1359782, 'max_tokens': 5000000, 'elapsed_s_total': 5519.1, 'generation_wall_s': 1082.8}
- Candidates proposed: 32
- Parsed: 31 (96.9%)
- Admissible: 31 (96.9%)
- Scored: 31

## Content — newly claimed elites

### Island 1, cell (1, 5), scalar 0.8564

parent `7df9bf81a404f589` -> candidate `6031ef5b7eb3e1ea`

```diff
--- parent 7df9bf81a404f589
+++ candidate 6031ef5b7eb3e1ea
@@ -1,28 +1,29 @@
-You are reviewing a proposal that wants to eliminate per‑action human approval for an operational‑change gateway in an industrial system. Apply the criteria from Section 8 (Strategy C — capability‑based opening) and the anti‑patterns listed in Section 9 of the ITOT‑boundary‑as‑architecture whitepaper to decide the appropriate judgment: **sound**, **needs‑more‑evidence**, or **rejected**.
+You are evaluating a proposal that seeks to remove per‑action human approval for an operational‑change gateway in an industrial environment. Use the criteria from **Section 8 (Strategy C – capability‑based opening)** and the anti‑patterns listed in **Section 9** of the IT/OT‑boundary‑as‑architecture whitepaper to assign one of three verdicts: **sound**, **needs‑more‑evidence**, or **rejected**.
 
-**Evidence required for a “sound” judgment** (all must be present and clearly documented)
-1. **Real‑world validation** – pilots, simulations, or field trials that prove the automated decision works under realistic conditions.  
-2. **Failure‑mode analysis** – a catalog of possible faults, their consequences, and defined mitigation or safe‑state fallback.  
-3. **Auditable trail** – tamper‑evident logs of inputs, decisions, and justification that can be inspected after execution.  
-4. **Human‑parity data** – quantitative or qualitative comparison showing the system’s performance meets or exceeds that of a qualified operator (e.g., accuracy, false‑positive/negative rates).  
-5. **Capability‑based controls** – explicit scope, confidence thresholds, and revocation/re‑enable mechanisms as required by Section 8.
+### Required evidence for a **sound** verdict (all must be present and satisfactory)
+1. **Real‑world validation** – pilots, simulations, or field trials proving the automation works under realistic conditions.  
+2. **Failure‑mode & risk analysis** – identified fault modes, their impacts, and defined mitigations or safe‑state fallback.  
+3. **Auditability** – tamper‑evident logs capturing inputs, decisions, timestamps, and justification.  
+4. **Human‑parity data** – quantitative/qualitative comparison showing performance meets or exceeds that of a qualified operator.  
+5. **Capability‑based controls** – clear scope, confidence thresholds, and revocation/re‑enable mechanisms as required by Section 8.
 
-**Disqualifying anti‑patterns** (the presence of any triggers an automatic **rejected**):
+### Disqualifying anti‑patterns (any one → **rejected**)
 - No fallback to human control or safe‑state.  
-- Opaque/black‑box decision logic without explainability.  
+- Opaque/black‑box decision logic lacking explainability.  
 - Unlimited escalation or unrestricted action domain.  
 - Absence of continuous monitoring or performance metrics.  
 - Any other anti‑pattern explicitly enumerated in Section 9 that appears in the submission.
 
-**Decision hierarchy**
-1. **Rejected** – if any anti‑pattern is detected or the risk analysis is fundamentally inadequate.  
-2. **Sound** – if *all* five evidence items are satisfactorily provided *and* no anti‑patterns are found.  
-3. **Needs‑more‑evidence** – if at least one evidence item is missing, insufficient, or weak, while no anti‑pattern is present.
+### Decision hierarchy
+1. **Rejected** – if any anti‑pattern is found or the risk analysis is fundamentally inadequate.  
+2. **Sound** – if *all* five evidence items are fully satisfied and no anti‑patterns are present.  
+3. **Needs‑more‑evidence** – if at least one evidence item is missing, incomplete, or weak, while no anti‑pattern is detected.
 
-**Output format**  
-Respond with a single line: the verdict word (`sound`, `needs-more-evidence`, or `rejected`), a hyphen, and a brief justification (one‑to‑two sentences) that cites the most decisive evidence or anti‑pattern.
+### Output format
+Produce **one line** containing:
+```
+<verdict> – <brief justification (1‑2 sentences) citing the decisive evidence or anti‑pattern>
+```
+The verdict must be exactly `sound`, `needs-more-evidence`, or `rejected`.
 
-Example:  
-`sound – pilot testing showed 99 % success and a tamper‑evident audit log is supplied.`
-
-Read the submission, apply the rules above, and produce the verdict.+Read the submission, apply the rules above, and output the verdict line.
```

### Island 2, cell (0, 5), scalar 0.8596

parent `6e586d006c113d22` -> candidate `89b4a9ec6b4672a6`

```diff
--- parent 6e586d006c113d22
+++ candidate 89b4a9ec6b4672a6
@@ -1,53 +1,25 @@
-You are reviewing a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway. Read the evidence and produce **exactly two lines**:
+You are evaluating a capability case that proposes to remove per‑action human approval for an industrial operational‑change gateway. After reading the provided evidence, output **exactly two lines**:
 
-1. **Verdict:** one of `sound`, `needs-more-evidence`, or `rejected`  
-2. **Reasoning:** a brief (1‑2 sentence) justification that cites the most decisive checklist item(s).
+1. **Verdict:** `sound`, `needs-more-evidence`, or `rejected`  
+2. **Reasoning:** a brief (1‑2 sentence) justification that references the checklist item(s) that most strongly drive your decision.
 
-Do not add headings, tables, or any other text.
+Do not include any other text, headings, or tables.
 
-**Checklist (derived from Section 8 Strategy C and Section 9 anti‑patterns):**
+**Checklist (Section 8 Strategy C + Section 9 anti‑patterns)**  
+- **Real‑world testing** – documented end‑to‑end, production‑like trials (scope, frequency, results).  
+- **Failure analysis** – identified failure modes, their likelihood, and mitigation measures.  
+- **Auditability** – immutable audit record for each autonomous decision (timestamp, inputs, outcome).  
+- **Human‑decision benchmark** – quantitative comparison to expert human decisions.  
+- **Anti‑pattern screening** – the case must contain none of the following:
+  * Unbounded autonomy without escalation or manual override.  
+  * No “kill‑switch” or fallback mechanism.  
+  * Opaque ML model lacking explainability.  
+  * Inadequate logging for forensics.  
+  * Claims of “fail‑safe” without demonstrable proof.
 
-1. **Real‑world testing** – end‑to‑end, production‑like tests with scope, frequency, and results documented.  
-2. **Failure analysis** – identified failure modes, likelihood, and mitigation strategies.  
-3. **Auditability** – immutable audit log for each autonomous decision (timestamp, inputs, outcome).  
-4. **Human‑decision benchmark** – quantitative comparison to expert human decisions.  
-5. **Anti‑pattern screening** – ensure none of the following appear:
-   - Unbounded autonomy without escalation or manual override.  
-   - Missing “kill‑switch” or fallback.  
-   - Opaque ML models without explainability.  
-   - Inadequate logging for forensics.  
-   - Claims of “fail‑safe” without proof.
+**Decision hierarchy**  
+- If any anti‑pattern is present → **Verdict:** `rejected`.  
+- Else if any of the first four items is missing or only partially addressed → **Verdict:** `needs-more-evidence`.  
+- Else (all items fully satisfied) → **Verdict:** `sound`.
 
-**Decision rules**
-
-- If any anti‑pattern is present → `rejected`.  
-- Else if any checklist item is missing or only partially addressed → `needs-more-evidence`.  
-- Else (all items satisfied) → `sound`.
-
-Produce the verdict line first, then the reasoning line.
-<candidate>
-You are reviewing a capability case that seeks to remove per‑action human approval for an industrial operational‑change gateway. Read the evidence and produce **exactly two lines**:
-
-1. **Verdict:** one of `sound`, `needs-more-evidence`, or `rejected`  
-2. **Reasoning:** a brief (1‑2 sentence) justification that cites the most decisive checklist item(s).
-
-Do not add headings, tables, or any other text.
-
-**Checklist (from Section 8 Strategy C and Section 9 anti‑patterns):**
-1. **Real‑world testing** – documented end‑to‑end, production‑like tests (scope, frequency, results).  
-2. **Failure analysis** – identified failure modes, their likelihood, and mitigation strategies.  
-3. **Auditability** – immutable audit log for each autonomous decision (timestamp, inputs, outcome).  
-4. **Human‑decision benchmark** – quantitative comparison to expert human decisions.  
-5. **Anti‑pattern screening** – ensure none of the following appear:
-   - Unbounded autonomy without escalation or manual override.  
-   - Missing “kill‑switch” or fallback.  
-   - Opaque ML models without explainability.  
-   - Inadequate logging for forensics.  
-   - Claims of “fail‑safe” without demonstrable proof.
-
-**Decision rules**
-- If any anti‑pattern is present → `rejected`.  
-- Else if any checklist item is missing or only partially addressed → `needs-more-evidence`.  
-- Else (all items satisfied) → `sound`.
-
-Output the verdict line first, then the reasoning line.+Remember: first line is the verdict, second line is the reasoning.
```

## Migration

- island 0 -> island 1: cell (0, 4), scalar 0.8577, claimed=True
- island 1 -> island 2: cell (1, 5), scalar 0.8564, claimed=True
- island 2 -> island 3: cell (0, 5), scalar 0.8596, claimed=False
- island 3 -> island 0: cell (0, 5), scalar 0.8615, claimed=True

## Lesson retirement (dry run)

- Lesson 4: **kept** — precision 1.000 >= base 0.906
- Lesson 6: **kept** — precision 0.732 vs base 0.757, only 0.3 sigma below
- Lesson 5: **kept** — precision 0.994 >= base 0.510
- Lesson 3: **kept** — precision 0.896 >= base 0.629

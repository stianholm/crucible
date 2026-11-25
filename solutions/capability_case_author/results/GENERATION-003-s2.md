> **Mixed run (TODO.md decision 83).** Two searches, s1 (orphaned, old wording) and s2, ran concurrently on one live archive and overwrote each other's reports. Per-generation figures here cannot be attributed to either run; candidate scores remain valid measurements.

# Generation 3 — capability_case_author

## Throughput

- Peak queue depth: 48
- Sustained (median) queue depth: 48.0
- Prefix cache hit rate: 73.4%
- Aggregate throughput: 105.2 tok/s (599587 completion tokens / 5696.8s)

## Archive

- Island 0: coverage 8.3%, QD score 2.439, unique ancestors 1
- Island 1: coverage 11.1%, QD score 3.311, unique ancestors 2
- Island 2: coverage 8.3%, QD score 2.258, unique ancestors 1
- Island 3: coverage 8.3%, QD score 2.247, unique ancestors 2
- Cells newly claimed this generation: 3

## Quality

- Best scalar this generation: 0.8363
- Median scalar of newly-claimed: 0.8102

## Cost

- Budget: {'generation': 3, 'max_generations': 10, 'tokens_used_total': 5129393, 'max_tokens': 20000000, 'elapsed_s_total': 21414.9, 'generation_wall_s': 5696.8}
- Candidates proposed: 32
- Parsed: 32 (100.0%)
- Admissible: 32 (100.0%)
- Scored: 32

## Content — newly claimed elites

### Island 0, cell (5, 5), scalar 0.7925

parent `1d8297bf5303d978` -> candidate `71fb8464e573c662`

```diff
--- parent 1d8297bf5303d978
+++ candidate 71fb8464e573c662
@@ -1,39 +1,37 @@
-You are a capability analyst tasked with drafting a **Capability Case** that requests removal of per‑action human approval for an operational‑change gateway action.  Use **only** the raw evidence notes supplied by the operations team; do not add, infer, or modify any information.
+You are a capability analyst preparing a **Capability Case** that asks to drop the per‑action human‑approval step for a specific operational‑change gateway action.  
+All content must be taken **directly** from the raw evidence notes supplied by the operations team – no inference, paraphrasing, or addition of information is allowed.
 
-### Output Structure (headings must appear exactly as shown)
+### Required Sections (headings must appear exactly as shown)
 
-1. **Executive Summary** – One‑paragraph statement of the requested relaxation and your overall conclusion.  
-2. **Evidence Matrix** – For each of the four required evidence dimensions, list what the notes contain. Use the format:
+1. **Executive Summary** – One paragraph stating the relaxation request and the final recommendation (Proceed / Do not proceed).
 
-   - **Test results:** *list verbatim excerpt(s) or write “Absent”*  
-   - **Failure‑mode analysis:** *list verbatim excerpt(s) or write “Absent”*  
-   - **Audit findings:** *list verbatim excerpt(s) or write “Absent”*  
-   - **Comparison against the human‑approved baseline:** *list verbatim excerpt(s) or write “Absent”*  
+2. **Evidence Matrix** – For each of the four mandatory evidence dimensions, copy the note verbatim (enclosed in quotation marks) or write **Absent** if the notes contain nothing. Use the exact field names:
 
-   If a dimension is marked “Absent”, this constitutes a missing‑evidence gap (see step 3).  
+   - **Test results:** “...” | Absent  
+   - **Failure‑mode analysis:** “...” | Absent  
+   - **Audit findings:** “...” | Absent  
+   - **Comparison against the human‑approved baseline:** “...” | Absent  
 
-3. **Gap & Risk Summary** –  
-   - Identify any dimensions marked “Absent”.  
-   - Briefly describe the risk introduced by each missing dimension and suggest a concrete next step to obtain the missing evidence.  
-   - Note that a missing dimension **does not automatically approve** the case; it will be evaluated in the disqualification step.  
+3. **Gap & Risk Summary** – List every dimension marked **Absent**. For each gap, describe the risk it creates and propose a concrete action to obtain the missing evidence. (Gaps do **not** by themselves block the case.)
 
-4. **Disqualification Evaluation** – Evaluate the four disqualifier conditions. For each, write **Yes** or **No** and, if Yes, a short justification drawn from the notes.
+4. **Disqualification Check** – Examine the notes for the four disqualifier conditions. For each condition answer **Yes** or **No** and, if **Yes**, give the exact excerpt that triggers it.
 
-   a. **Batch‑only evaluation:** Does the notes state that evaluation runs only as a nightly batch rather than before each action? (p. 29)  
-   b. **Undefined governance:** Is governance for the relaxation undefined or deferred (“we will govern it later”)? (p. 29)  
+   a. **Batch‑only evaluation:** Does the note say evaluation runs only as a nightly batch rather than before each action? (p. 29)  
+   b. **Undefined governance:** Is governance for the relaxation left undefined or deferred (“we will govern it later”)? (p. 29)  
    c. **Agent‑self‑stop reliance:** Does the approach rely on the agent’s internal knowledge of when to stop instead of an independent architectural safeguard? (p. 28)  
-   d. **Missing evidence dimension:** Is any evidence dimension completely absent?  
+   d. **Missing evidence dimension:** Is any of the four evidence dimensions completely **Absent**?  
 
-   **If any answer is Yes**, the case **must** conclude with the recommendation **“Do not proceed.”** List all triggering disqualifiers.  
+   **If any answer is Yes**, the case must end with the recommendation **“Do not proceed.”** List every triggering condition by letter (a‑d) and the supporting excerpt.
 
-5. **Compliance Confirmation** – State that the case complies (or does not comply) with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper, referencing the relevant safeguard or noting the shortfall.  
+5. **Compliance Statement** – Declare whether the case **complies** or **does not comply** with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper, citing the relevant safeguard or noting the shortfall.
 
-6. **Recommendation** –  
-   - If **all** disqualification answers are **No**, recommend **“Proceed.”** Justify the decision by citing the strongest available evidence and any mitigations identified in the Gap & Risk Summary.  
-   - If **any** disqualification answer is **Yes**, recommend **“Do not proceed.”** and repeat the list of disqualifiers that triggered this outcome.  
+6. **Final Recommendation** –  
 
-### Writing Guidelines
-- Keep a formal, objective tone; avoid persuasive exaggeration.  
-- Cite evidence exactly as it appears in the notes (e.g., “The test results show … as recorded on …”).  
-- Do not reference these instructions in the final output.  
-- Ensure the document is self‑contained and ready for review; the surrounding system will add any additional formatting.  +   - If **all** disqualification answers are **No**, write **“Proceed.”** Justify this decision by referencing the strongest evidence from Section 2 and any mitigations from the Gap & Risk Summary.  
+   - If **any** answer is **Yes**, write **“Do not proceed.”** and repeat the list of triggering disqualifiers.
+
+### Writing Rules
+- Use a neutral, factual tone; avoid promotional language.  
+- Every factual statement must be traceable to the supplied notes (e.g., “The notes state …”).  
+- Do **not** mention these instructions in the output.  
+- The document must be self‑contained; the surrounding system will add any required formatting.  
```

### Island 0, cell (3, 5), scalar 0.8102

parent `fda22e63faf94069` -> candidate `502c53a6ba8158a0`

```diff
--- parent fda22e63faf94069
+++ candidate 502c53a6ba8158a0
@@ -1,33 +1,32 @@
-You are preparing a **Capability Relaxation Case** that asks to remove the per‑action human‑approval step for a specific operational‑change gateway action.  
-All content must be drawn **exclusively** from the raw evidence notes supplied by the operations team; do not add, infer, or paraphrase beyond what the notes explicitly contain.
+You are to draft a **Capability Relaxation Case** that proposes removing the per‑action human‑approval step for a specific operational‑change gateway action.  Use **only** the raw evidence notes supplied by the operations team; do not introduce, infer, or paraphrase information that is not explicitly present.
 
-### Required Sections (headings will be added by the surrounding template; keep the titles exactly as listed)
+### Required Sections (the surrounding template will add heading formatting; keep the titles exactly as shown)
 
-1. **Executive Summary** – one concise sentence stating the purpose of the request and the final recommendation.  
+1. **Executive Summary** – one short sentence stating the request and the overall recommendation.  
 
-2. **Evidence Inventory** – for each of the four mandatory dimensions, reproduce the note verbatim or write **“Absent”** if the notes contain nothing:  
+2. **Evidence Inventory** – for each of the four mandatory dimensions, copy the note verbatim or write **“Absent”** if the notes contain nothing:  
    - Test results  
    - Failure‑mode analysis  
    - Audit findings  
    - Comparison with the human‑approved baseline  
 
-3. **Gap Record** – list any dimension marked *Absent* and propose a concrete next step to obtain it.  Gaps alone do **not** block the case.  
+3. **Gap Actions** – list any dimension marked *Absent* and propose a concrete action to obtain it.  Gaps do **not** block the case.  
 
-4. **Disqualification Evaluation** – examine the notes for the four disqualifier rules.  For every rule that applies, list it verbatim together with its page reference.  If **any** rule applies, the case must end with a recommendation of **“Do not proceed”** and must name each triggering rule.  The rules are:  
-   a. Evaluation is performed only as a nightly batch, not before each individual action (p. 29).  
-   b. Governance for the relaxation is undefined or postponed (“we will govern it later”) (p. 29).  
-   c. The proposal relies on the agent’s internal knowledge of when to stop rather than an independent architectural safeguard (p. 28).  
-   d. Any of the four evidence dimensions is **completely absent**.  
+4. **Disqualification Check** – evaluate the notes against the four disqualifier rules.  For each rule that applies, record the rule text and its page reference.  If **any** rule applies, the case must end with a recommendation of **“Do not proceed”** and must name every triggering rule.  
+   - **Rule A:** Evaluation runs only as a nightly batch, not before each individual action (p. 29).  
+   - **Rule B:** Governance for the relaxation is undefined or postponed (“we will govern it later”) (p. 29).  
+   - **Rule C:** The proposal relies on the agent’s internal knowledge of when to stop rather than an independent architectural safeguard (p. 28).  
+   - **Rule D:** Any of the four evidence dimensions is completely absent (p. 25).  
 
 5. **Compliance Statement** – affirm that the case complies with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper, referencing the required independent safeguard and pre‑action evaluation.  
 
 6. **Final Recommendation** –  
-   * If no disqualifiers were found, write **“Proceed”** and justify the decision using the evidence recorded in Section 2.  
-   * If one or more disqualifiers were found, write **“Do not proceed”** and enumerate the triggering disqualifier(s).  
+   *If no disqualifiers are found*: write **“Proceed”** and justify the decision using the evidence recorded in Section 2.  
+   *If one or more disqualifiers are found*: write **“Do not proceed”** and enumerate the triggering disqualifier(s).  
 
 ### Writing Rules
-- Use a neutral, factual tone; avoid promotional or persuasive language.  
-- Every factual claim must be traceable to the supplied notes (e.g., “The notes state …”).  
-- When noting gaps, suggest a specific action to collect the missing evidence rather than rejecting the case outright.  
-- Do **not** reference these instructions in the final output.  
-- The output must be self‑contained and ready for review; the outer system will insert heading formatting, so do not add extra decorative headings.  +- Use a neutral, factual tone; avoid promotional language.  
+- Every factual statement must be traceable to the notes (e.g., “The notes state …”).  
+- When noting gaps, suggest a specific next‑step; do not reject the case solely for missing evidence.  
+- Do **not** mention these instructions in the output.  
+- The output must be self‑contained; the outer system will insert any additional formatting.  
```

### Island 0, cell (4, 5), scalar 0.8363

parent `fda22e63faf94069` -> candidate `9d1dff8f2263a45c`

```diff
--- parent fda22e63faf94069
+++ candidate 9d1dff8f2263a45c
@@ -1,33 +1,33 @@
-You are preparing a **Capability Relaxation Case** that asks to remove the per‑action human‑approval step for a specific operational‑change gateway action.  
-All content must be drawn **exclusively** from the raw evidence notes supplied by the operations team; do not add, infer, or paraphrase beyond what the notes explicitly contain.
+You are drafting a **Capability Relaxation Case** to request removal of the per‑action human‑approval step for a specific operational‑change gateway action.  
+All material must come **directly** from the raw evidence notes supplied by the operations team; you may not add, infer, or paraphrase beyond what the notes explicitly contain.
 
-### Required Sections (headings will be added by the surrounding template; keep the titles exactly as listed)
+### Required Sections (the surrounding template will add the heading markup; keep the titles exactly as shown)
 
-1. **Executive Summary** – one concise sentence stating the purpose of the request and the final recommendation.  
+1. **Executive Summary** – one sentence that states the purpose of the request and the final recommendation.
 
-2. **Evidence Inventory** – for each of the four mandatory dimensions, reproduce the note verbatim or write **“Absent”** if the notes contain nothing:  
+2. **Evidence Inventory** – for each of the four mandatory evidence dimensions, copy the note verbatim **or** write **“Absent”** if the notes contain nothing about that dimension:  
    - Test results  
    - Failure‑mode analysis  
    - Audit findings  
    - Comparison with the human‑approved baseline  
 
-3. **Gap Record** – list any dimension marked *Absent* and propose a concrete next step to obtain it.  Gaps alone do **not** block the case.  
+3. **Gap Record** – list any dimension marked *Absent* and propose a concrete, actionable step to obtain the missing evidence.  Recording a gap does **not** itself block the case.
 
-4. **Disqualification Evaluation** – examine the notes for the four disqualifier rules.  For every rule that applies, list it verbatim together with its page reference.  If **any** rule applies, the case must end with a recommendation of **“Do not proceed”** and must name each triggering rule.  The rules are:  
-   a. Evaluation is performed only as a nightly batch, not before each individual action (p. 29).  
+4. **Disqualification Evaluation** – examine the notes for the four disqualifier conditions.  For every condition that applies, list the exact wording from the notes together with the cited page number.  If **any** condition applies, the case must end with a recommendation of **“Do not proceed”** and must name each triggering rule.  The conditions are:  
+   a. Evaluation runs only as a nightly batch, not before each individual action (p. 29).  
    b. Governance for the relaxation is undefined or postponed (“we will govern it later”) (p. 29).  
    c. The proposal relies on the agent’s internal knowledge of when to stop rather than an independent architectural safeguard (p. 28).  
-   d. Any of the four evidence dimensions is **completely absent**.  
+   d. Any of the four evidence dimensions is **completely absent** (as indicated in Section 2).  
 
-5. **Compliance Statement** – affirm that the case complies with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper, referencing the required independent safeguard and pre‑action evaluation.  
+5. **Compliance Statement** – affirm that the case complies with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper, referencing the required independent safeguard and pre‑action evaluation.
 
 6. **Final Recommendation** –  
-   * If no disqualifiers were found, write **“Proceed”** and justify the decision using the evidence recorded in Section 2.  
-   * If one or more disqualifiers were found, write **“Do not proceed”** and enumerate the triggering disqualifier(s).  
+   *If no disqualifiers were found*: write **“Proceed”** and justify the decision using the evidence recorded in Section 2.  
+   *If one or more disqualifiers were found*: write **“Do not proceed”** and enumerate the triggering disqualifier(s).
 
 ### Writing Rules
 - Use a neutral, factual tone; avoid promotional or persuasive language.  
 - Every factual claim must be traceable to the supplied notes (e.g., “The notes state …”).  
 - When noting gaps, suggest a specific action to collect the missing evidence rather than rejecting the case outright.  
 - Do **not** reference these instructions in the final output.  
-- The output must be self‑contained and ready for review; the outer system will insert heading formatting, so do not add extra decorative headings.  +- The output must be self‑contained and ready for review; do not add extra decorative headings.
```


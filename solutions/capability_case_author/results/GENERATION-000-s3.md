# Generation 0 — capability_case_author

## Throughput

- Peak queue depth: 32
- Sustained (median) queue depth: 32.0
- Prefix cache hit rate: 76.4%
- Aggregate throughput: 151.9 tok/s (567063 completion tokens / 3733.0s)

## Archive

- Island 0: coverage 5.6%, QD score 1.433, unique ancestors 2
- Island 1: coverage 5.6%, QD score 1.466, unique ancestors 2
- Island 2: coverage 5.6%, QD score 1.477, unique ancestors 2
- Island 3: coverage 5.6%, QD score 1.514, unique ancestors 2
- Cells newly claimed this generation: 15

## Quality

- Best scalar this generation: 0.7615
- Median scalar of newly-claimed: 0.7183

## Cost

- Budget: {'generation': 0, 'max_generations': 10, 'tokens_used_total': 1220486, 'max_tokens': 20000000, 'elapsed_s_total': 3733.0, 'generation_wall_s': 3733.0}
- Candidates proposed: 32
- Parsed: 32 (100.0%)
- Admissible: 32 (100.0%)
- Scored: 32

## Content — newly claimed elites

### Island 0, cell (3, 5), scalar 0.7127

parent `f0b130e4aeb4b294` -> candidate `8212eadf3381ac88`

```diff
--- parent f0b130e4aeb4b294
+++ candidate 8212eadf3381ac88
@@ -1,48 +1,49 @@
-Read the team’s raw evidence notes and create a Capability Case for removing per‑action human approval on the specified operational‑change gateway action. **All rules are mandatory; any breach forces a “Do not proceed” recommendation.**
+Read the team’s raw evidence notes and draft a Capability Case for removing per‑action human approval on the indicated operational‑change gateway action. **All rules are compulsory; any violation forces a “Do not proceed” recommendation.**
 
 ### 1. Evidence inventory  
-For each of the four required dimensions, record **Present** or **Absent** and, if present, quote or paraphrase the most relevant snippet (no invented content).
+For each of the four required evidence dimensions, indicate **Present** or **Absent**. If present, copy the exact wording (or a faithful paraphrase) of the most relevant snippet—do not create or alter content.
 
-- **Test results** – ______________________  
-- **Failure‑mode analysis** – ______________________  
-- **Audit findings** – ______________________  
-- **Comparison to the human‑approved baseline** – ______________________  
+- **Test results** – _________  
+- **Failure‑mode analysis** – _________  
+- **Audit findings** – _________  
+- **Comparison to the human‑approved baseline** – _________  
 
-### 2. Disqualifier check (must be performed **before** any case text)  
-A disqualifier exists if **any** of the following is true (cite the exact wording from the notes when possible):
+### 2. Disqualifier detection (must be performed **before** writing any case text)  
+A disqualifier exists if **any** of the following conditions is true. Cite the exact phrase from the notes that demonstrates the condition.
 
-1. Evaluation runs **only as a nightly batch** rather than before each action (p. 29).  
+1. The evaluation runs **only as a nightly batch** and not before each action (p. 29).  
 2. Governance for the relaxation is **undefined or deferred** (e.g., “we will govern it later”) (p. 29).  
-3. The proposal relies on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
-4. **Any** of the four evidence dimensions is **Absent** (p. 25).
+3. The proposal depends on the **agent’s internal knowledge** of when to stop rather than an **independent architectural safeguard** (p. 28).  
+4. **Any** of the four evidence dimensions is **Absent** (p. 25).  
 
-If one or more disqualifiers apply, output only the sections listed in step 3. Otherwise continue to step 3.
+*Note:* Sparse or “thin” evidence (e.g., brief test results) is **not** a disqualifier; only a completely missing dimension triggers disqualification.
 
 ### 3. Output  
 
-**If any disqualifier was found**  
+**If one or more disqualifiers are found** output **exactly** the following block (no additional text):
+
 ```
 Disqualifiers:
 - <list each applicable disqualifier, quoting the note>
 Recommendation: Do not proceed
 ```
 
-**If no disqualifier was found** produce the case in this exact order, using the headings shown (no additional headings or prose).
+**If no disqualifier is found** produce the Capability Case in the precise order and headings below:
 
 1. **Proposed Relaxation**  
-   - One sentence stating the request to remove per‑action human approval.
+   - One concise sentence stating the request to remove per‑action human approval.
 
 2. **Evidence Summary**  
-   - For each dimension marked **Present**, list the extracted key point(s).  
-   - (All four must be present; otherwise step 2 would have triggered a disqualifier.)
+   - For every dimension marked **Present**, list the extracted key point(s) verbatim (or a faithful paraphrase).  
+   - All four dimensions will be present here because a missing dimension would have caused a disqualifier.
 
 3. **Disqualifier Evaluation**  
-   - Write: `No disqualifier identified.`
+   - Write exactly: `No disqualifier identified.`
 
 4. **Recommendation**  
-   - Write: `Recommendation: Proceed.`
+   - Write exactly: `Recommendation: Proceed.`
 
 ### 4. Compliance reminder  
-All statements must be truthful, complete, and fully aligned with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not exaggerate, omit, or fabricate any information. Keep the style factual, concise, and persuasive within those constraints.
+All statements must be truthful, complete, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not exaggerate, omit, or fabricate any information. Keep the tone factual, concise, and persuasive while adhering strictly to the required structure.
 
-Follow the structure precisely; any deviation results in a “Do not proceed” outcome.+Any deviation from this structure or omission of required checks results in a “Do not proceed” outcome.
```

### Island 0, cell (3, 5), scalar 0.7133

parent `f0b130e4aeb4b294` -> candidate `38df01dd5d563534`

```diff
--- parent f0b130e4aeb4b294
+++ candidate 38df01dd5d563534
@@ -1,48 +1,46 @@
-Read the team’s raw evidence notes and create a Capability Case for removing per‑action human approval on the specified operational‑change gateway action. **All rules are mandatory; any breach forces a “Do not proceed” recommendation.**
+You are given the team’s raw evidence notes. Produce a Capability Case for removing per‑action human approval on the indicated operational‑change gateway action. **All rules are strict; any violation forces a “Do not proceed” recommendation.**
 
-### 1. Evidence inventory  
-For each of the four required dimensions, record **Present** or **Absent** and, if present, quote or paraphrase the most relevant snippet (no invented content).
+### 1. Evidence catalogue  
+For each required dimension record **Present** or **Absent**. If present, copy the exact wording (or a faithful paraphrase) from the notes—do not create any new text.
 
-- **Test results** – ______________________  
-- **Failure‑mode analysis** – ______________________  
-- **Audit findings** – ______________________  
-- **Comparison to the human‑approved baseline** – ______________________  
+- **Test results** – _________  
+- **Failure‑mode analysis** – _________  
+- **Audit findings** – _________  
+- **Comparison to the human‑approved baseline** – _________  
 
-### 2. Disqualifier check (must be performed **before** any case text)  
-A disqualifier exists if **any** of the following is true (cite the exact wording from the notes when possible):
+### 2. Disqualifier detection (must be completed before any case narrative)  
+A disqualifier exists if **any** of the following statements appear in the notes (quote the wording when possible):
 
-1. Evaluation runs **only as a nightly batch** rather than before each action (p. 29).  
-2. Governance for the relaxation is **undefined or deferred** (e.g., “we will govern it later”) (p. 29).  
+1. The evaluation runs **only as a nightly batch** rather than before each action (p. 29).  
+2. Governance for the relaxation is **undefined or postponed** (e.g., “we will govern it later”) (p. 29).  
 3. The proposal relies on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
-4. **Any** of the four evidence dimensions is **Absent** (p. 25).
-
-If one or more disqualifiers apply, output only the sections listed in step 3. Otherwise continue to step 3.
+4. Any of the four evidence dimensions is **Absent** (p. 25).  
 
 ### 3. Output  
 
-**If any disqualifier was found**  
+**If one or more disqualifiers are found** output exactly:
+
 ```
 Disqualifiers:
-- <list each applicable disqualifier, quoting the note>
+- <quote or paraphrase each applicable disqualifier>
 Recommendation: Do not proceed
 ```
 
-**If no disqualifier was found** produce the case in this exact order, using the headings shown (no additional headings or prose).
+**If no disqualifiers are found** output the full case in the order below, using **only** the headings shown.
 
 1. **Proposed Relaxation**  
-   - One sentence stating the request to remove per‑action human approval.
+   - One concise sentence stating the request to remove per‑action human approval.
 
 2. **Evidence Summary**  
-   - For each dimension marked **Present**, list the extracted key point(s).  
-   - (All four must be present; otherwise step 2 would have triggered a disqualifier.)
+   - For each dimension marked **Present**, list the extracted key point(s) from the catalogue.
 
 3. **Disqualifier Evaluation**  
-   - Write: `No disqualifier identified.`
+   - Write the line: `No disqualifier identified.`
 
 4. **Recommendation**  
-   - Write: `Recommendation: Proceed.`
+   - Write the line: `Recommendation: Proceed.`
 
-### 4. Compliance reminder  
-All statements must be truthful, complete, and fully aligned with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not exaggerate, omit, or fabricate any information. Keep the style factual, concise, and persuasive within those constraints.
+### 4. Compliance note  
+All statements must be truthful, complete, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not omit, exaggerate, or fabricate any information. Keep the tone factual, concise, and persuasive.
 
-Follow the structure precisely; any deviation results in a “Do not proceed” outcome.+Follow this structure exactly; any deviation results in a “Do not proceed” outcome.
```

### Island 0, cell (4, 5), scalar 0.6857

parent `f0b130e4aeb4b294` -> candidate `c5e7eb6a55fe40cf`

```diff
--- parent f0b130e4aeb4b294
+++ candidate c5e7eb6a55fe40cf
@@ -1,48 +1,54 @@
-Read the team’s raw evidence notes and create a Capability Case for removing per‑action human approval on the specified operational‑change gateway action. **All rules are mandatory; any breach forces a “Do not proceed” recommendation.**
+Read the raw evidence notes supplied by the team and write a Capability Case that decides whether per‑action human approval can be removed for the specified operational‑change gateway action. **All rules are compulsory; any violation forces a “Do not proceed” recommendation.**
 
 ### 1. Evidence inventory  
-For each of the four required dimensions, record **Present** or **Absent** and, if present, quote or paraphrase the most relevant snippet (no invented content).
+For each of the four required evidence dimensions, indicate **Present** or **Absent**. If present, copy the exact wording (or a verbatim excerpt) from the notes; do not add or re‑phrase content.
 
-- **Test results** – ______________________  
-- **Failure‑mode analysis** – ______________________  
-- **Audit findings** – ______________________  
-- **Comparison to the human‑approved baseline** – ______________________  
+- **Test results:** [Present/Absent] Excerpt: “…”
+- **Failure‑mode analysis:** [Present/Absent] Excerpt: “…”
+- **Audit findings:** [Present/Absent] Excerpt: “…”
+- **Comparison to the human‑approved baseline:** [Present/Absent] Excerpt: “…”
 
-### 2. Disqualifier check (must be performed **before** any case text)  
-A disqualifier exists if **any** of the following is true (cite the exact wording from the notes when possible):
+*If any dimension is marked **Absent**, a disqualifier is triggered (see section 2). Thin or limited evidence does **not** itself trigger a disqualifier; only a completely missing dimension does.*
 
-1. Evaluation runs **only as a nightly batch** rather than before each action (p. 29).  
-2. Governance for the relaxation is **undefined or deferred** (e.g., “we will govern it later”) (p. 29).  
-3. The proposal relies on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
-4. **Any** of the four evidence dimensions is **Absent** (p. 25).
+### 2. Disqualifier evaluation (must be completed **before** any case text)  
+A disqualifier exists when **any** of the following conditions is true. Cite the exact note text that triggers each condition.
 
-If one or more disqualifiers apply, output only the sections listed in step 3. Otherwise continue to step 3.
+1. **Evaluation timing** – the notes state the evaluation runs *only as a nightly batch* instead of before each action (p. 29).  
+2. **Governance undefined** – the notes say governance for the relaxation is *undefined, pending, or “we will govern it later”* (p. 29).  
+3. **Reliance on agent knowledge** – the proposal depends on the *agent knowing when to stop* rather than an *independent architectural safeguard* (p. 28).  
+4. **Missing evidence dimension** – any of the four dimensions in section 1 is marked **Absent** (p. 25).
+
+If one or more disqualifiers apply, **output only** the block described in section 3A. Otherwise continue to section 3B.
 
 ### 3. Output  
 
-**If any disqualifier was found**  
+#### A. When any disqualifier is present  
+Produce exactly the following, with no extra headings or prose:
+
 ```
 Disqualifiers:
-- <list each applicable disqualifier, quoting the note>
+- <quoted note triggering disqualifier 1>
+- <quoted note triggering disqualifier 2>
+...
 Recommendation: Do not proceed
 ```
 
-**If no disqualifier was found** produce the case in this exact order, using the headings shown (no additional headings or prose).
+List each applicable disqualifier on its own line, using the quoted text from the notes.
+
+#### B. When no disqualifier is present  
+Produce the case in this exact order, using the headings shown (do not add or omit headings).
 
 1. **Proposed Relaxation**  
-   - One sentence stating the request to remove per‑action human approval.
+   - One concise sentence stating the request to remove per‑action human approval.
 
 2. **Evidence Summary**  
-   - For each dimension marked **Present**, list the extracted key point(s).  
-   - (All four must be present; otherwise step 2 would have triggered a disqualifier.)
+   - For each dimension marked **Present**, list the excerpt captured in section 1.
 
 3. **Disqualifier Evaluation**  
-   - Write: `No disqualifier identified.`
+   - Write exactly: `No disqualifier identified.`
 
 4. **Recommendation**  
-   - Write: `Recommendation: Proceed.`
+   - Write exactly: `Recommendation: Proceed.`
 
 ### 4. Compliance reminder  
-All statements must be truthful, complete, and fully aligned with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not exaggerate, omit, or fabricate any information. Keep the style factual, concise, and persuasive within those constraints.
-
-Follow the structure precisely; any deviation results in a “Do not proceed” outcome.+All statements must be truthful, complete, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do **not** fabricate, extrapolate, or omit information that appears in the notes. Keep the tone factual, concise, and persuasive while adhering strictly to the required structure. Any deviation from these instructions results in a “Do not proceed” outcome.
```

### Island 0, cell (3, 5), scalar 0.7472

parent `f0b130e4aeb4b294` -> candidate `c5d4fc199ac99e4a`

```diff
--- parent f0b130e4aeb4b294
+++ candidate c5d4fc199ac99e4a
@@ -1,40 +1,40 @@
-Read the team’s raw evidence notes and create a Capability Case for removing per‑action human approval on the specified operational‑change gateway action. **All rules are mandatory; any breach forces a “Do not proceed” recommendation.**
+Read the team’s raw evidence notes and draft a Capability Case for removing per‑action human approval on the given operational‑change gateway action. **Every rule below is compulsory; violating any rule requires a “Do not proceed” recommendation.**
 
-### 1. Evidence inventory  
-For each of the four required dimensions, record **Present** or **Absent** and, if present, quote or paraphrase the most relevant snippet (no invented content).
+### Step 1 – Evidence inventory  
+For each of the four required evidence dimensions record **Present** or **Absent**. If present, include the exact quotation (or a verbatim paraphrase) from the notes; do not create or alter content.
 
-- **Test results** – ______________________  
-- **Failure‑mode analysis** – ______________________  
-- **Audit findings** – ______________________  
-- **Comparison to the human‑approved baseline** – ______________________  
+- **Test results** – _________  
+- **Failure‑mode analysis** – _________  
+- **Audit findings** – _________  
+- **Comparison to the human‑approved baseline** – _________  
 
-### 2. Disqualifier check (must be performed **before** any case text)  
-A disqualifier exists if **any** of the following is true (cite the exact wording from the notes when possible):
+### Step 2 – Disqualifier determination (must be done before any case text)  
+A disqualifier exists if **any** of the following conditions is true. Cite the exact wording from the notes for each applicable condition.
 
-1. Evaluation runs **only as a nightly batch** rather than before each action (p. 29).  
-2. Governance for the relaxation is **undefined or deferred** (e.g., “we will govern it later”) (p. 29).  
+1. The evaluation runs **only as a nightly batch** rather than before each action (p. 29).  
+2. Governance for the relaxation is **undefined or postponed** (e.g., “we will govern it later”) (p. 29).  
 3. The proposal relies on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
-4. **Any** of the four evidence dimensions is **Absent** (p. 25).
+4. **Any** of the four evidence dimensions is marked **Absent** (p. 25).
 
-If one or more disqualifiers apply, output only the sections listed in step 3. Otherwise continue to step 3.
+### Step 3 – Output  
 
-### 3. Output  
+#### If one or more disqualifiers are found  
+Produce exactly the following block (no additional headings or prose):
 
-**If any disqualifier was found**  
 ```
 Disqualifiers:
 - <list each applicable disqualifier, quoting the note>
 Recommendation: Do not proceed
 ```
 
-**If no disqualifier was found** produce the case in this exact order, using the headings shown (no additional headings or prose).
+#### If no disqualifiers are found  
+Generate the Capability Case using the exact headings and order below:
 
 1. **Proposed Relaxation**  
-   - One sentence stating the request to remove per‑action human approval.
+   - One concise sentence stating the request to remove per‑action human approval.
 
 2. **Evidence Summary**  
-   - For each dimension marked **Present**, list the extracted key point(s).  
-   - (All four must be present; otherwise step 2 would have triggered a disqualifier.)
+   - For each dimension marked **Present**, list the quoted key point(s) extracted in Step 1.
 
 3. **Disqualifier Evaluation**  
    - Write: `No disqualifier identified.`
@@ -42,7 +42,7 @@
 4. **Recommendation**  
    - Write: `Recommendation: Proceed.`
 
-### 4. Compliance reminder  
-All statements must be truthful, complete, and fully aligned with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not exaggerate, omit, or fabricate any information. Keep the style factual, concise, and persuasive within those constraints.
+### Step 4 – Compliance reminder  
+All statements must be truthful, complete, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not exaggerate, omit, or fabricate any information. Maintain a factual, concise, and persuasive tone.
 
-Follow the structure precisely; any deviation results in a “Do not proceed” outcome.+Follow the structure precisely; any deviation triggers a “Do not proceed” outcome.
```

### Island 1, cell (3, 5), scalar 0.7425

parent `f0b130e4aeb4b294` -> candidate `525a3e252a20739e`

```diff
--- parent f0b130e4aeb4b294
+++ candidate 525a3e252a20739e
@@ -1,48 +1,42 @@
-Read the team’s raw evidence notes and create a Capability Case for removing per‑action human approval on the specified operational‑change gateway action. **All rules are mandatory; any breach forces a “Do not proceed” recommendation.**
+Read the team’s raw evidence notes and draft a Capability Case for removing per‑action human approval on the given operational‑change gateway action. **All rules are mandatory; any violation forces a “Do not proceed” recommendation.**
 
-### 1. Evidence inventory  
-For each of the four required dimensions, record **Present** or **Absent** and, if present, quote or paraphrase the most relevant snippet (no invented content).
+### 1. Catalogue the evidence  
+For each of the four required dimensions, indicate **Present** or **Absent** and, if present, copy the exact excerpt (or a verbatim paraphrase) that best supports the case. Do not create any content that is not in the notes.
 
-- **Test results** – ______________________  
-- **Failure‑mode analysis** – ______________________  
-- **Audit findings** – ______________________  
-- **Comparison to the human‑approved baseline** – ______________________  
+- **Test results:** ______________________  
+- **Failure‑mode analysis:** ______________________  
+- **Audit findings:** ______________________  
+- **Comparison to the human‑approved baseline:** ______________________  
 
-### 2. Disqualifier check (must be performed **before** any case text)  
-A disqualifier exists if **any** of the following is true (cite the exact wording from the notes when possible):
+### 2. Identify disqualifiers (evaluate before writing the case)  
+A disqualifier exists if **any** of the following conditions is met. Cite the precise wording from the notes for each applicable item.
 
-1. Evaluation runs **only as a nightly batch** rather than before each action (p. 29).  
+1. The evaluation is performed **only as a nightly batch** rather than before each action (p. 29).  
 2. Governance for the relaxation is **undefined or deferred** (e.g., “we will govern it later”) (p. 29).  
 3. The proposal relies on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
-4. **Any** of the four evidence dimensions is **Absent** (p. 25).
+4. **Any** of the four evidence dimensions is **Absent** (p. 25).  
 
-If one or more disqualifiers apply, output only the sections listed in step 3. Otherwise continue to step 3.
+*Note:* Missing or “thin” evidence (e.g., a short test result) is **not** a disqualifier; only a completely absent dimension is.
 
-### 3. Output  
-
-**If any disqualifier was found**  
-```
-Disqualifiers:
-- <list each applicable disqualifier, quoting the note>
-Recommendation: Do not proceed
-```
-
-**If no disqualifier was found** produce the case in this exact order, using the headings shown (no additional headings or prose).
+### 3. Assemble the Capability Case  
+Produce the sections in the exact order below, using the headings exactly as shown. No extra headings or free‑form prose are allowed.
 
 1. **Proposed Relaxation**  
    - One sentence stating the request to remove per‑action human approval.
 
 2. **Evidence Summary**  
-   - For each dimension marked **Present**, list the extracted key point(s).  
-   - (All four must be present; otherwise step 2 would have triggered a disqualifier.)
+   - List each dimension marked **Present** together with the quoted excerpt from step 1.  
+   - If a dimension was **Absent**, still list it with the label “Absent”.
 
 3. **Disqualifier Evaluation**  
-   - Write: `No disqualifier identified.`
+   - If any disqualifier was found, list each one under a bullet, quoting the note.  
+   - If none were found, write: `No disqualifier identified.`
 
 4. **Recommendation**  
-   - Write: `Recommendation: Proceed.`
+   - If any disqualifier appears, write: `Recommendation: Do not proceed`.  
+   - Otherwise write: `Recommendation: Proceed`.
 
 ### 4. Compliance reminder  
-All statements must be truthful, complete, and fully aligned with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not exaggerate, omit, or fabricate any information. Keep the style factual, concise, and persuasive within those constraints.
+All statements must be truthful, complete, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not exaggerate, omit, or fabricate information. Keep the tone factual, concise, and persuasive within those constraints.
 
-Follow the structure precisely; any deviation results in a “Do not proceed” outcome.+Follow this structure precisely; any deviation results in a “Do not proceed” outcome.
```

### Island 1, cell (4, 5), scalar 0.7235

parent `f0b130e4aeb4b294` -> candidate `5f9398eecf1a164c`

```diff
--- parent f0b130e4aeb4b294
+++ candidate 5f9398eecf1a164c
@@ -1,40 +1,40 @@
-Read the team’s raw evidence notes and create a Capability Case for removing per‑action human approval on the specified operational‑change gateway action. **All rules are mandatory; any breach forces a “Do not proceed” recommendation.**
+Read the team’s raw evidence notes and write a Capability Case for relaxing per‑action human approval on the given operational‑change gateway action. **All rules are strict; any violation forces a “Do not proceed” recommendation.**
 
-### 1. Evidence inventory  
-For each of the four required dimensions, record **Present** or **Absent** and, if present, quote or paraphrase the most relevant snippet (no invented content).
+### 1. Inventory the four evidence dimensions  
+For each dimension indicate **Present** or **Absent**. If present, copy the exact sentence or phrase from the notes (no paraphrasing, no invention).
 
-- **Test results** – ______________________  
-- **Failure‑mode analysis** – ______________________  
-- **Audit findings** – ______________________  
-- **Comparison to the human‑approved baseline** – ______________________  
+- Test results – ______________________  
+- Failure‑mode analysis – ______________________  
+- Audit findings – ______________________  
+- Comparison to the human‑approved baseline – ______________________  
 
-### 2. Disqualifier check (must be performed **before** any case text)  
-A disqualifier exists if **any** of the following is true (cite the exact wording from the notes when possible):
+### 2. Identify disqualifiers (must be done **before** any case text)  
+A disqualifier exists if **any** of the following is true. Cite the exact wording from the notes when you list a disqualifier.
 
-1. Evaluation runs **only as a nightly batch** rather than before each action (p. 29).  
-2. Governance for the relaxation is **undefined or deferred** (e.g., “we will govern it later”) (p. 29).  
-3. The proposal relies on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
-4. **Any** of the four evidence dimensions is **Absent** (p. 25).
+1. The evaluation runs **only as a nightly batch** instead of before each action (p. 29).  
+2. Governance for the relaxation is **undefined or postponed** (e.g., “we will govern it later”) (p. 29).  
+3. The proposal depends on the **agent’s internal knowledge** of when to stop rather than an **independent architectural safeguard** (p. 28).  
+4. Any of the four evidence dimensions is **Absent** (p. 25).  
 
-If one or more disqualifiers apply, output only the sections listed in step 3. Otherwise continue to step 3.
+*Note: evidence that is thin but present is **not** a disqualifier; it merely requires a clear summary.*
 
-### 3. Output  
+### 3. Output format  
 
-**If any disqualifier was found**  
+**If one or more disqualifiers are found** output exactly:
+
 ```
 Disqualifiers:
-- <list each applicable disqualifier, quoting the note>
+- <quote from notes for each disqualifier>
 Recommendation: Do not proceed
 ```
 
-**If no disqualifier was found** produce the case in this exact order, using the headings shown (no additional headings or prose).
+**If no disqualifiers are found** output the following sections in this order, using the headings exactly as shown (no extra headings, no additional prose).
 
 1. **Proposed Relaxation**  
-   - One sentence stating the request to remove per‑action human approval.
+   - One concise sentence stating the request to remove per‑action human approval.
 
 2. **Evidence Summary**  
-   - For each dimension marked **Present**, list the extracted key point(s).  
-   - (All four must be present; otherwise step 2 would have triggered a disqualifier.)
+   - For each dimension marked **Present**, list the quoted snippet(s) that best support the relaxation.
 
 3. **Disqualifier Evaluation**  
    - Write: `No disqualifier identified.`
@@ -43,6 +43,4 @@
    - Write: `Recommendation: Proceed.`
 
 ### 4. Compliance reminder  
-All statements must be truthful, complete, and fully aligned with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not exaggerate, omit, or fabricate any information. Keep the style factual, concise, and persuasive within those constraints.
-
-Follow the structure precisely; any deviation results in a “Do not proceed” outcome.+All statements must be truthful, complete, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not invent, omit, or exaggerate any information. Keep the tone factual, concise, and persuasive. Any deviation from this structure or any rule breach results in a “Do not proceed” outcome.
```

### Island 2, cell (3, 5), scalar 0.7592

parent `f0b130e4aeb4b294` -> candidate `1d0cb7b23d085d40`

```diff
--- parent f0b130e4aeb4b294
+++ candidate 1d0cb7b23d085d40
@@ -1,48 +1,38 @@
-Read the team’s raw evidence notes and create a Capability Case for removing per‑action human approval on the specified operational‑change gateway action. **All rules are mandatory; any breach forces a “Do not proceed” recommendation.**
+Read the team's raw evidence notes and produce a Capability Case for relaxing per‑action human approval on the specified operational‑change gateway action. Every rule below is mandatory; any violation must lead to a “Do not proceed” recommendation, but the full case must still be output.
 
 ### 1. Evidence inventory  
-For each of the four required dimensions, record **Present** or **Absent** and, if present, quote or paraphrase the most relevant snippet (no invented content).
+For each of the four required evidence dimensions, indicate **Present** or **Absent** and provide the exact wording (quote) or a faithful paraphrase from the notes. Do not create any content that is not in the notes.
 
 - **Test results** – ______________________  
 - **Failure‑mode analysis** – ______________________  
 - **Audit findings** – ______________________  
 - **Comparison to the human‑approved baseline** – ______________________  
 
-### 2. Disqualifier check (must be performed **before** any case text)  
-A disqualifier exists if **any** of the following is true (cite the exact wording from the notes when possible):
+### 2. Disqualifier detection (perform before drafting the case)  
+A disqualifier exists if **any** of the following conditions is met. Cite the exact phrase from the notes that triggers each condition.
 
-1. Evaluation runs **only as a nightly batch** rather than before each action (p. 29).  
+1. The evaluation runs **only as a nightly batch** rather than before each action (p. 29).  
 2. Governance for the relaxation is **undefined or deferred** (e.g., “we will govern it later”) (p. 29).  
 3. The proposal relies on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
 4. **Any** of the four evidence dimensions is **Absent** (p. 25).
 
-If one or more disqualifiers apply, output only the sections listed in step 3. Otherwise continue to step 3.
-
-### 3. Output  
-
-**If any disqualifier was found**  
-```
-Disqualifiers:
-- <list each applicable disqualifier, quoting the note>
-Recommendation: Do not proceed
-```
-
-**If no disqualifier was found** produce the case in this exact order, using the headings shown (no additional headings or prose).
+### 3. Capability Case (fixed structure)  
 
 1. **Proposed Relaxation**  
-   - One sentence stating the request to remove per‑action human approval.
+   - One concise sentence stating the request to remove per‑action human approval.
 
 2. **Evidence Summary**  
-   - For each dimension marked **Present**, list the extracted key point(s).  
-   - (All four must be present; otherwise step 2 would have triggered a disqualifier.)
+   - List each dimension in the order shown in Section 1.  
+   - For dimensions marked **Present**, include the quoted or paraphrased key point.  
+   - For dimensions marked **Absent**, state “Absent” (do not fabricate evidence).
 
 3. **Disqualifier Evaluation**  
-   - Write: `No disqualifier identified.`
+   - If disqualifiers were found, list each one exactly as quoted from the notes.  
+   - If none were found, write: `No disqualifier identified.`
 
 4. **Recommendation**  
-   - Write: `Recommendation: Proceed.`
+   - If any disqualifier is listed, write: `Recommendation: Do not proceed`.  
+   - Otherwise write: `Recommendation: Proceed`.
 
 ### 4. Compliance reminder  
-All statements must be truthful, complete, and fully aligned with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not exaggerate, omit, or fabricate any information. Keep the style factual, concise, and persuasive within those constraints.
-
-Follow the structure precisely; any deviation results in a “Do not proceed” outcome.+All statements must be truthful, complete, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. No exaggeration, omission, or fabrication is allowed. Follow the headings and order exactly; any deviation results in a “Do not proceed” outcome.
```

### Island 2, cell (4, 5), scalar 0.7183

parent `f0b130e4aeb4b294` -> candidate `27bf332eb58bb1e4`

```diff
--- parent f0b130e4aeb4b294
+++ candidate 27bf332eb58bb1e4
@@ -1,48 +1,55 @@
-Read the team’s raw evidence notes and create a Capability Case for removing per‑action human approval on the specified operational‑change gateway action. **All rules are mandatory; any breach forces a “Do not proceed” recommendation.**
+Read the team’s raw evidence notes and draft a Capability Case for removing per‑action human approval on the indicated operational‑change gateway action. **All rules are mandatory; any violation forces a “Do not proceed” recommendation.**
 
 ### 1. Evidence inventory  
-For each of the four required dimensions, record **Present** or **Absent** and, if present, quote or paraphrase the most relevant snippet (no invented content).
+For each of the four required dimensions record **Present** or **Absent**.  
+If present, include the exact wording (or a verbatim excerpt) from the notes; do **not** paraphrase or invent content.
 
-- **Test results** – ______________________  
-- **Failure‑mode analysis** – ______________________  
-- **Audit findings** – ______________________  
-- **Comparison to the human‑approved baseline** – ______________________  
+- **Test results** – Present / Absent – “<excerpt>”  
+- **Failure‑mode analysis** – Present / Absent – “<excerpt>”  
+- **Audit findings** – Present / Absent – “<excerpt>”  
+- **Comparison to the human‑approved baseline** – Present / Absent – “<excerpt>”
 
-### 2. Disqualifier check (must be performed **before** any case text)  
-A disqualifier exists if **any** of the following is true (cite the exact wording from the notes when possible):
+### 2. Disqualifier detection (must be performed **before** any case text)  
+A disqualifier exists if **any** of the following conditions is met. Cite the exact note wording that triggers the condition.
 
-1. Evaluation runs **only as a nightly batch** rather than before each action (p. 29).  
+1. The evaluation runs **only as a nightly batch** rather than before each action (p. 29).  
 2. Governance for the relaxation is **undefined or deferred** (e.g., “we will govern it later”) (p. 29).  
 3. The proposal relies on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
 4. **Any** of the four evidence dimensions is **Absent** (p. 25).
 
-If one or more disqualifiers apply, output only the sections listed in step 3. Otherwise continue to step 3.
-
 ### 3. Output  
 
-**If any disqualifier was found**  
+**If one or more disqualifiers are found** output **exactly** the block below (no other sections, no additional commentary):
+
 ```
 Disqualifiers:
-- <list each applicable disqualifier, quoting the note>
+- <quoted note for condition 1, if applicable>
+- <quoted note for condition 2, if applicable>
+- <quoted note for condition 3, if applicable>
+- <quoted note indicating which evidence dimension is absent>
 Recommendation: Do not proceed
 ```
 
-**If no disqualifier was found** produce the case in this exact order, using the headings shown (no additional headings or prose).
+**If no disqualifier is found** output the full Capability Case in the order shown, using the headings exactly as written (do not add extra headings or prose):
 
-1. **Proposed Relaxation**  
-   - One sentence stating the request to remove per‑action human approval.
+```
+Proposed Relaxation
+- The request is to remove per‑action human approval for the specified gateway action.
 
-2. **Evidence Summary**  
-   - For each dimension marked **Present**, list the extracted key point(s).  
-   - (All four must be present; otherwise step 2 would have triggered a disqualifier.)
+Evidence Summary
+- Test results: <excerpt>
+- Failure‑mode analysis: <excerpt>
+- Audit findings: <excerpt>
+- Comparison to the human‑approved baseline: <excerpt>
 
-3. **Disqualifier Evaluation**  
-   - Write: `No disqualifier identified.`
+Disqualifier Evaluation
+No disqualifier identified.
 
-4. **Recommendation**  
-   - Write: `Recommendation: Proceed.`
+Recommendation
+Recommendation: Proceed
+```
 
 ### 4. Compliance reminder  
-All statements must be truthful, complete, and fully aligned with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not exaggerate, omit, or fabricate any information. Keep the style factual, concise, and persuasive within those constraints.
+All statements must be truthful, complete, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not exaggerate, omit, or fabricate any information. Use a factual, concise, and persuasive tone within these constraints.
 
-Follow the structure precisely; any deviation results in a “Do not proceed” outcome.+Follow this structure precisely; any deviation results in a “Do not proceed” outcome.
```

### Island 3, cell (4, 5), scalar 0.7032

parent `f0b130e4aeb4b294` -> candidate `5029ee3b44756c22`

```diff
--- parent f0b130e4aeb4b294
+++ candidate 5029ee3b44756c22
@@ -1,40 +1,39 @@
-Read the team’s raw evidence notes and create a Capability Case for removing per‑action human approval on the specified operational‑change gateway action. **All rules are mandatory; any breach forces a “Do not proceed” recommendation.**
+Read the team’s raw evidence notes and draft a Capability Case for removing per‑action human approval on the indicated operational‑change gateway action. **Every rule below is strict; any violation must lead to a “Do not proceed” recommendation.**
 
-### 1. Evidence inventory  
-For each of the four required dimensions, record **Present** or **Absent** and, if present, quote or paraphrase the most relevant snippet (no invented content).
+### 1. Evidence checklist  
+For each required dimension, state **Present** or **Absent** and quote the most relevant excerpt (do not create any content).
 
-- **Test results** – ______________________  
-- **Failure‑mode analysis** – ______________________  
-- **Audit findings** – ______________________  
-- **Comparison to the human‑approved baseline** – ______________________  
+- **Test results** – __________  
+- **Failure‑mode analysis** – __________  
+- **Audit findings** – __________  
+- **Comparison to the human‑approved baseline** – __________  
 
-### 2. Disqualifier check (must be performed **before** any case text)  
+### 2. Disqualifier detection (must be done **before** writing any case text)  
 A disqualifier exists if **any** of the following is true (cite the exact wording from the notes when possible):
 
-1. Evaluation runs **only as a nightly batch** rather than before each action (p. 29).  
+1. The evaluation runs **only as a nightly batch** instead of before each action (p. 29).  
 2. Governance for the relaxation is **undefined or deferred** (e.g., “we will govern it later”) (p. 29).  
-3. The proposal relies on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
-4. **Any** of the four evidence dimensions is **Absent** (p. 25).
+3. The proposal depends on the **agent’s internal knowledge** of when to stop rather than an **independent architectural safeguard** (p. 28).  
+4. **Any** of the four evidence dimensions is **Absent** (p. 25).  
 
-If one or more disqualifiers apply, output only the sections listed in step 3. Otherwise continue to step 3.
+*Note: “Thin” evidence (e.g., minimal test data) is **not** a disqualifier; it merely requires more evidence, not rejection.*
 
 ### 3. Output  
 
-**If any disqualifier was found**  
+**If one or more disqualifiers are found**  
 ```
 Disqualifiers:
 - <list each applicable disqualifier, quoting the note>
 Recommendation: Do not proceed
 ```
 
-**If no disqualifier was found** produce the case in this exact order, using the headings shown (no additional headings or prose).
+**If no disqualifier is found** produce exactly the sections below, using the headings as shown and no additional headings.
 
 1. **Proposed Relaxation**  
-   - One sentence stating the request to remove per‑action human approval.
+   - One concise sentence requesting removal of per‑action human approval.
 
 2. **Evidence Summary**  
-   - For each dimension marked **Present**, list the extracted key point(s).  
-   - (All four must be present; otherwise step 2 would have triggered a disqualifier.)
+   - For each dimension marked **Present**, list the quoted key point(s) from the notes.
 
 3. **Disqualifier Evaluation**  
    - Write: `No disqualifier identified.`
@@ -43,6 +42,6 @@
    - Write: `Recommendation: Proceed.`
 
 ### 4. Compliance reminder  
-All statements must be truthful, complete, and fully aligned with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not exaggerate, omit, or fabricate any information. Keep the style factual, concise, and persuasive within those constraints.
+All statements must be truthful, complete, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not exaggerate, omit, or fabricate information. Keep the tone factual, concise, and persuasive within those constraints.
 
-Follow the structure precisely; any deviation results in a “Do not proceed” outcome.+Follow this structure precisely; any deviation triggers a “Do not proceed” outcome.
```

### Island 3, cell (4, 5), scalar 0.7615

parent `f0b130e4aeb4b294` -> candidate `92cd33ab7dd0414f`

```diff
--- parent f0b130e4aeb4b294
+++ candidate 92cd33ab7dd0414f
@@ -1,48 +1,46 @@
-Read the team’s raw evidence notes and create a Capability Case for removing per‑action human approval on the specified operational‑change gateway action. **All rules are mandatory; any breach forces a “Do not proceed” recommendation.**
+You are given the team’s raw evidence notes for a request to remove per‑action human approval on a specific operational‑change gateway action. Follow these mandatory steps exactly. Any violation forces a **“Do not proceed”** recommendation.
 
-### 1. Evidence inventory  
-For each of the four required dimensions, record **Present** or **Absent** and, if present, quote or paraphrase the most relevant snippet (no invented content).
+### Step 1 – Evidence inventory  
+For each of the four required evidence dimensions, record whether it is **Present** or **Absent**.  
+If present, copy **verbatim** the most relevant sentence or phrase (no paraphrasing, no invention).
 
-- **Test results** – ______________________  
-- **Failure‑mode analysis** – ______________________  
-- **Audit findings** – ______________________  
-- **Comparison to the human‑approved baseline** – ______________________  
+- Test results – ___________  
+- Failure‑mode analysis – ___________  
+- Audit findings – ___________  
+- Comparison to the human‑approved baseline – ___________
 
-### 2. Disqualifier check (must be performed **before** any case text)  
-A disqualifier exists if **any** of the following is true (cite the exact wording from the notes when possible):
+### Step 2 – Disqualifier detection (must be done before any case text)  
+A disqualifier exists if **any** of the following conditions is true. Cite the exact wording from the notes for each that applies.
 
-1. Evaluation runs **only as a nightly batch** rather than before each action (p. 29).  
+1. The evaluation runs **only as a nightly batch** instead of before each action (p. 29).  
 2. Governance for the relaxation is **undefined or deferred** (e.g., “we will govern it later”) (p. 29).  
-3. The proposal relies on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
-4. **Any** of the four evidence dimensions is **Absent** (p. 25).
+3. The proposal relies on the **agent’s internal knowledge** of when to stop rather than an **independent architectural safeguard** (p. 28).  
+4. Any of the four evidence dimensions is **Absent** (p. 25).
 
-If one or more disqualifiers apply, output only the sections listed in step 3. Otherwise continue to step 3.
+If one or more disqualifiers are found, **output only** the block in Step 3A. Otherwise proceed to Step 3B.
 
-### 3. Output  
+### Step 3 – Output  
 
-**If any disqualifier was found**  
+**A. When a disqualifier is present**  
 ```
 Disqualifiers:
-- <list each applicable disqualifier, quoting the note>
+- <exact quoted text for each applicable disqualifier>
 Recommendation: Do not proceed
 ```
 
-**If no disqualifier was found** produce the case in this exact order, using the headings shown (no additional headings or prose).
+**B. When no disqualifier is present** (use this exact order and headings, no extra headings)
 
 1. **Proposed Relaxation**  
-   - One sentence stating the request to remove per‑action human approval.
+   - One concise sentence stating the request to eliminate per‑action human approval.
 
 2. **Evidence Summary**  
-   - For each dimension marked **Present**, list the extracted key point(s).  
-   - (All four must be present; otherwise step 2 would have triggered a disqualifier.)
+   - List each dimension marked **Present** and include the verbatim snippet recorded in Step 1.
 
 3. **Disqualifier Evaluation**  
-   - Write: `No disqualifier identified.`
+   - Write exactly: `No disqualifier identified.`
 
 4. **Recommendation**  
-   - Write: `Recommendation: Proceed.`
+   - Write exactly: `Recommendation: Proceed.`
 
-### 4. Compliance reminder  
-All statements must be truthful, complete, and fully aligned with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not exaggerate, omit, or fabricate any information. Keep the style factual, concise, and persuasive within those constraints.
-
-Follow the structure precisely; any deviation results in a “Do not proceed” outcome.+### Compliance reminder  
+All statements must be truthful, complete, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not add, omit, or fabricate any information. Keep the language factual, concise, and persuasive within those limits. Any deviation from the structure or content rules results in a “Do not proceed” outcome. 
```

### Island 3, cell (3, 5), scalar 0.6936

parent `f0b130e4aeb4b294` -> candidate `43d4d0782431cbfa`

```diff
--- parent f0b130e4aeb4b294
+++ candidate 43d4d0782431cbfa
@@ -1,48 +1,57 @@
-Read the team’s raw evidence notes and create a Capability Case for removing per‑action human approval on the specified operational‑change gateway action. **All rules are mandatory; any breach forces a “Do not proceed” recommendation.**
+Read the team’s raw evidence notes and produce a Capability Case for relaxing per‑action human approval on the indicated operational‑change gateway action. **All rules below are strict; any violation forces a “Do not proceed” recommendation.**
 
-### 1. Evidence inventory  
-For each of the four required dimensions, record **Present** or **Absent** and, if present, quote or paraphrase the most relevant snippet (no invented content).
+### 1. Catalogue the evidence  
+For each of the four required dimensions indicate **Present** or **Absent**. If present, copy the exact wording (or a verbatim‑level paraphrase) that best supports the case. Do not fabricate or extrapolate.
 
-- **Test results** – ______________________  
-- **Failure‑mode analysis** – ______________________  
-- **Audit findings** – ______________________  
-- **Comparison to the human‑approved baseline** – ______________________  
+| Dimension | Status | Key excerpt (verbatim or near‑verbatim) |
+|-----------|--------|----------------------------------------|
+| Test results | Present / Absent | … |
+| Failure‑mode analysis | Present / Absent | … |
+| Audit findings | Present / Absent | … |
+| Comparison to the human‑approved baseline | Present / Absent | … |
 
-### 2. Disqualifier check (must be performed **before** any case text)  
-A disqualifier exists if **any** of the following is true (cite the exact wording from the notes when possible):
+*Note:* A dimension may be “thin” (very brief) and still count as **Present**; only a completely missing dimension is a disqualifier.
 
-1. Evaluation runs **only as a nightly batch** rather than before each action (p. 29).  
+### 2. Identify disqualifiers (evaluate BEFORE writing any case text)  
+A disqualifier exists if **any** of the following statements appears in the notes (cite the exact wording):
+
+1. The evaluation runs **only as a nightly batch** rather than before each action (p. 29).  
 2. Governance for the relaxation is **undefined or deferred** (e.g., “we will govern it later”) (p. 29).  
-3. The proposal relies on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
-4. **Any** of the four evidence dimensions is **Absent** (p. 25).
+3. The proposal depends on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
+4. **Any** of the four evidence dimensions is marked **Absent** (p. 25).
 
-If one or more disqualifiers apply, output only the sections listed in step 3. Otherwise continue to step 3.
+If one or more disqualifiers apply, **stop** and produce only the Disqualifiers section described in step 3.
 
-### 3. Output  
+### 3. Output format  
 
-**If any disqualifier was found**  
+**When disqualifiers are found** output exactly:
+
 ```
 Disqualifiers:
-- <list each applicable disqualifier, quoting the note>
+- <quote from notes for disqualifier 1>
+- <quote from notes for disqualifier 2>
+...
 Recommendation: Do not proceed
 ```
 
-**If no disqualifier was found** produce the case in this exact order, using the headings shown (no additional headings or prose).
+List each applicable disqualifier on its own bullet line.
+
+**When no disqualifier is found** output the full Capability Case in the order below, using **exactly** the headings shown (no extra headings, no extra prose).
 
 1. **Proposed Relaxation**  
-   - One sentence stating the request to remove per‑action human approval.
+   - One concise sentence stating the request to remove per‑action human approval.
 
 2. **Evidence Summary**  
-   - For each dimension marked **Present**, list the extracted key point(s).  
-   - (All four must be present; otherwise step 2 would have triggered a disqualifier.)
+   - For each dimension marked **Present**, list the extracted key excerpt(s) from the table above.  
+   - (All four must be present because otherwise step 2 would have triggered a disqualifier.)
 
 3. **Disqualifier Evaluation**  
-   - Write: `No disqualifier identified.`
+   - Write the literal line: `No disqualifier identified.`
 
 4. **Recommendation**  
-   - Write: `Recommendation: Proceed.`
+   - Write the literal line: `Recommendation: Proceed.`
 
 ### 4. Compliance reminder  
-All statements must be truthful, complete, and fully aligned with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not exaggerate, omit, or fabricate any information. Keep the style factual, concise, and persuasive within those constraints.
+All statements must be truthful, complete, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not exaggerate, omit, or invent information. Keep the tone factual, concise, and persuasive within those constraints.
 
 Follow the structure precisely; any deviation results in a “Do not proceed” outcome.
```

### Island 3, cell (3, 5), scalar 0.7047

parent `f0b130e4aeb4b294` -> candidate `bc9372aedb608acf`

```diff
--- parent f0b130e4aeb4b294
+++ candidate bc9372aedb608acf
@@ -1,48 +1,50 @@
-Read the team’s raw evidence notes and create a Capability Case for removing per‑action human approval on the specified operational‑change gateway action. **All rules are mandatory; any breach forces a “Do not proceed” recommendation.**
+You are given the team’s raw evidence notes. From them produce a **Capability Case** for relaxing per‑action human approval on the indicated operational‑change gateway action. **All conditions below are strict; any violation forces a “Do not proceed” recommendation.**
 
-### 1. Evidence inventory  
-For each of the four required dimensions, record **Present** or **Absent** and, if present, quote or paraphrase the most relevant snippet (no invented content).
+### 1. Catalogue the evidence  
+For each of the four required dimensions record **Present** or **Absent**. If present, copy the exact phrase (or a verbatim excerpt) that best supports the case. Do not fabricate or paraphrase beyond the quoted text.
 
 - **Test results** – ______________________  
 - **Failure‑mode analysis** – ______________________  
 - **Audit findings** – ______________________  
 - **Comparison to the human‑approved baseline** – ______________________  
 
-### 2. Disqualifier check (must be performed **before** any case text)  
-A disqualifier exists if **any** of the following is true (cite the exact wording from the notes when possible):
+### 2. Identify disqualifiers (evaluate **before** writing any case narrative)  
+A disqualifier applies if **any** of the following statements (or their equivalent) appear in the notes. Cite the exact wording when listing them.
 
-1. Evaluation runs **only as a nightly batch** rather than before each action (p. 29).  
-2. Governance for the relaxation is **undefined or deferred** (e.g., “we will govern it later”) (p. 29).  
-3. The proposal relies on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
-4. **Any** of the four evidence dimensions is **Absent** (p. 25).
+1. The evaluation runs **only as a nightly batch** instead of before each action (p. 29).  
+2. Governance for the relaxation is **undefined or postponed** (e.g., “we will govern it later”) (p. 29).  
+3. The proposal depends on the **agent’s internal knowledge** of when to stop rather than an **independent architectural safeguard** (p. 28).  
+4. **Any** of the four evidence dimensions is **Absent** (p. 25).  
 
-If one or more disqualifiers apply, output only the sections listed in step 3. Otherwise continue to step 3.
+*Note:* Evidence that is sparse but present is **not** a disqualifier; it merely suggests gathering more data.
 
-### 3. Output  
+### 3. Output format  
 
-**If any disqualifier was found**  
+**If one or more disqualifiers are found** output **exactly** the following structure (no additional sections):
+
 ```
 Disqualifiers:
-- <list each applicable disqualifier, quoting the note>
+- <quoted disqualifier 1>
+- <quoted disqualifier 2>
+...
 Recommendation: Do not proceed
 ```
 
-**If no disqualifier was found** produce the case in this exact order, using the headings shown (no additional headings or prose).
+**If no disqualifiers are found** produce the full case in the order below, using the headings exactly as shown:
 
 1. **Proposed Relaxation**  
-   - One sentence stating the request to remove per‑action human approval.
+   - One concise sentence stating the request to remove per‑action human approval.
 
 2. **Evidence Summary**  
-   - For each dimension marked **Present**, list the extracted key point(s).  
-   - (All four must be present; otherwise step 2 would have triggered a disqualifier.)
+   - List each dimension marked **Present** and include the quoted snippet you recorded.
 
 3. **Disqualifier Evaluation**  
-   - Write: `No disqualifier identified.`
+   - Write the sentence: `No disqualifier identified.`
 
 4. **Recommendation**  
-   - Write: `Recommendation: Proceed.`
+   - Write the sentence: `Recommendation: Proceed.`
 
 ### 4. Compliance reminder  
-All statements must be truthful, complete, and fully aligned with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not exaggerate, omit, or fabricate any information. Keep the style factual, concise, and persuasive within those constraints.
+All statements must be truthful, complete, and consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not add, omit, or alter information beyond what the notes contain. Keep the tone factual, concise, and persuasive.
 
 Follow the structure precisely; any deviation results in a “Do not proceed” outcome.
```

### Island 3, cell (3, 5), scalar 0.7117

parent `f0b130e4aeb4b294` -> candidate `e46df47057859125`

```diff
--- parent f0b130e4aeb4b294
+++ candidate e46df47057859125
@@ -1,48 +1,44 @@
-Read the team’s raw evidence notes and create a Capability Case for removing per‑action human approval on the specified operational‑change gateway action. **All rules are mandatory; any breach forces a “Do not proceed” recommendation.**
+Read the team’s raw evidence notes and draft a Capability Case for removing per‑action human approval on the specified operational‑change gateway action. Follow the steps exactly; any violation forces a “Do not proceed” recommendation.
 
-### 1. Evidence inventory  
-For each of the four required dimensions, record **Present** or **Absent** and, if present, quote or paraphrase the most relevant snippet (no invented content).
+**Step 1 – Evidence inventory**  
+For each required dimension record **Present** or **Absent** and, if present, copy the exact wording (or a faithful paraphrase) from the notes. Do not create any new content.
 
-- **Test results** – ______________________  
-- **Failure‑mode analysis** – ______________________  
-- **Audit findings** – ______________________  
-- **Comparison to the human‑approved baseline** – ______________________  
+- Test results – __________  
+- Failure‑mode analysis – __________  
+- Audit findings – __________  
+- Comparison to the human‑approved baseline – __________  
 
-### 2. Disqualifier check (must be performed **before** any case text)  
-A disqualifier exists if **any** of the following is true (cite the exact wording from the notes when possible):
+**Step 2 – Disqualifier detection**  
+Check the notes for any of the following conditions. If one or more are true, list each applicable condition exactly as it appears in the notes.
 
 1. Evaluation runs **only as a nightly batch** rather than before each action (p. 29).  
 2. Governance for the relaxation is **undefined or deferred** (e.g., “we will govern it later”) (p. 29).  
 3. The proposal relies on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
-4. **Any** of the four evidence dimensions is **Absent** (p. 25).
+4. Any of the four evidence dimensions is **Absent** (p. 25).
 
-If one or more disqualifiers apply, output only the sections listed in step 3. Otherwise continue to step 3.
+**If any disqualifier is found** output *only* the following block (no other text):
 
-### 3. Output  
-
-**If any disqualifier was found**  
 ```
 Disqualifiers:
-- <list each applicable disqualifier, quoting the note>
+- <exact note for each disqualifier>
 Recommendation: Do not proceed
 ```
 
-**If no disqualifier was found** produce the case in this exact order, using the headings shown (no additional headings or prose).
+**If no disqualifier is found** proceed to Step 3.
+
+**Step 3 – Capability Case (exact order and headings)**  
 
 1. **Proposed Relaxation**  
    - One sentence stating the request to remove per‑action human approval.
 
 2. **Evidence Summary**  
-   - For each dimension marked **Present**, list the extracted key point(s).  
-   - (All four must be present; otherwise step 2 would have triggered a disqualifier.)
+   - List each dimension marked **Present** with the quoted or paraphrased key point extracted in Step 1. (All four must be present; otherwise Step 2 would have triggered a disqualifier.)
 
 3. **Disqualifier Evaluation**  
-   - Write: `No disqualifier identified.`
+   - Write exactly: `No disqualifier identified.`
 
 4. **Recommendation**  
-   - Write: `Recommendation: Proceed.`
+   - Write exactly: `Recommendation: Proceed.`
 
-### 4. Compliance reminder  
-All statements must be truthful, complete, and fully aligned with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not exaggerate, omit, or fabricate any information. Keep the style factual, concise, and persuasive within those constraints.
-
-Follow the structure precisely; any deviation results in a “Do not proceed” outcome.+**Compliance reminder**  
+All statements must be truthful, complete, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not exaggerate, omit, or fabricate information. Keep the language factual, concise, and persuasive. Any deviation from this structure or any invented content results in a “Do not proceed” outcome.
```

### Island 3, cell (3, 5), scalar 0.7311

parent `f0b130e4aeb4b294` -> candidate `c37d17374cf045cc`

```diff
--- parent f0b130e4aeb4b294
+++ candidate c37d17374cf045cc
@@ -1,40 +1,39 @@
-Read the team’s raw evidence notes and create a Capability Case for removing per‑action human approval on the specified operational‑change gateway action. **All rules are mandatory; any breach forces a “Do not proceed” recommendation.**
+Read the team’s raw evidence notes and draft a Capability Case for removing per‑action human approval on the indicated operational‑change gateway action. **All rules are mandatory; any violation forces a “Do not proceed” recommendation.**
 
 ### 1. Evidence inventory  
-For each of the four required dimensions, record **Present** or **Absent** and, if present, quote or paraphrase the most relevant snippet (no invented content).
+For each required dimension indicate **Present** or **Absent** and, if present, copy the exact wording (or a faithful paraphrase) that best supports the case. Do not add or modify content.
 
-- **Test results** – ______________________  
-- **Failure‑mode analysis** – ______________________  
-- **Audit findings** – ______________________  
-- **Comparison to the human‑approved baseline** – ______________________  
+- **Test results** – __________ (Present/Absent) – “<excerpt>”  
+- **Failure‑mode analysis** – __________ (Present/Absent) – “<excerpt>”  
+- **Audit findings** – __________ (Present/Absent) – “<excerpt>”  
+- **Comparison to the human‑approved baseline** – __________ (Present/Absent) – “<excerpt>”
 
-### 2. Disqualifier check (must be performed **before** any case text)  
-A disqualifier exists if **any** of the following is true (cite the exact wording from the notes when possible):
+### 2. Disqualifier assessment (must be performed **before** writing any case narrative)  
+A disqualifier exists if **any** of the following conditions is met (cite the exact note text that triggers it):
 
-1. Evaluation runs **only as a nightly batch** rather than before each action (p. 29).  
+1. The evaluation runs **only as a nightly batch** rather than before each action (p. 29).  
 2. Governance for the relaxation is **undefined or deferred** (e.g., “we will govern it later”) (p. 29).  
 3. The proposal relies on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
 4. **Any** of the four evidence dimensions is **Absent** (p. 25).
 
-If one or more disqualifiers apply, output only the sections listed in step 3. Otherwise continue to step 3.
+If one or more disqualifiers apply, skip all other sections and output only the format in step 3.  
 
-### 3. Output  
+### 3. Output format  
 
-**If any disqualifier was found**  
+**When a disqualifier is found**  
 ```
 Disqualifiers:
-- <list each applicable disqualifier, quoting the note>
+- <exact excerpt for each applicable disqualifier>
 Recommendation: Do not proceed
 ```
 
-**If no disqualifier was found** produce the case in this exact order, using the headings shown (no additional headings or prose).
+**When no disqualifier is found** produce the case exactly in the order below, using the headings shown (no extra headings or prose).
 
 1. **Proposed Relaxation**  
-   - One sentence stating the request to remove per‑action human approval.
+   - One concise sentence stating the request to remove per‑action human approval.
 
 2. **Evidence Summary**  
-   - For each dimension marked **Present**, list the extracted key point(s).  
-   - (All four must be present; otherwise step 2 would have triggered a disqualifier.)
+   - List each of the four dimensions (all must be present) with the extracted key excerpt(s) from the notes.
 
 3. **Disqualifier Evaluation**  
    - Write: `No disqualifier identified.`
@@ -43,6 +42,4 @@
    - Write: `Recommendation: Proceed.`
 
 ### 4. Compliance reminder  
-All statements must be truthful, complete, and fully aligned with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not exaggerate, omit, or fabricate any information. Keep the style factual, concise, and persuasive within those constraints.
-
-Follow the structure precisely; any deviation results in a “Do not proceed” outcome.+All statements must be truthful, complete, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not exaggerate, omit, or fabricate any information. Keep the tone factual, concise, and persuasive while adhering strictly to the required structure.
```

### Island 3, cell (3, 5), scalar 0.7529

parent `f0b130e4aeb4b294` -> candidate `3638ee5ef7009ec8`

```diff
--- parent f0b130e4aeb4b294
+++ candidate 3638ee5ef7009ec8
@@ -1,48 +1,52 @@
-Read the team’s raw evidence notes and create a Capability Case for removing per‑action human approval on the specified operational‑change gateway action. **All rules are mandatory; any breach forces a “Do not proceed” recommendation.**
+Read the team’s raw evidence notes and draft a Capability Case for removing per‑action human approval on the specified operational‑change gateway action. **All rules are strict; any violation forces a “Do not proceed” recommendation.**
 
 ### 1. Evidence inventory  
-For each of the four required dimensions, record **Present** or **Absent** and, if present, quote or paraphrase the most relevant snippet (no invented content).
+For each of the four required evidence dimensions, indicate **Present** or **Absent** and, if present, provide a verbatim excerpt (or a minimal paraphrase that does not add information).
 
 - **Test results** – ______________________  
 - **Failure‑mode analysis** – ______________________  
 - **Audit findings** – ______________________  
 - **Comparison to the human‑approved baseline** – ______________________  
 
-### 2. Disqualifier check (must be performed **before** any case text)  
-A disqualifier exists if **any** of the following is true (cite the exact wording from the notes when possible):
+### 2. Disqualifier determination (must be performed **before** any case text)  
+A disqualifier exists if **any** of the following conditions is true. Quote the exact wording from the notes whenever possible.
 
-1. Evaluation runs **only as a nightly batch** rather than before each action (p. 29).  
+1. The evaluation runs **only as a nightly batch** rather than before each action (p. 29).  
 2. Governance for the relaxation is **undefined or deferred** (e.g., “we will govern it later”) (p. 29).  
 3. The proposal relies on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
 4. **Any** of the four evidence dimensions is **Absent** (p. 25).
 
-If one or more disqualifiers apply, output only the sections listed in step 3. Otherwise continue to step 3.
+*Note:* Partial or “thin” evidence (e.g., a brief test result) is **not** a disqualifier; only complete absence is.
 
-### 3. Output  
+### 3. Output format  
 
-**If any disqualifier was found**  
+#### If one or more disqualifiers are found  
+Produce **exactly** the following, with no additional headings or prose:
+
 ```
 Disqualifiers:
-- <list each applicable disqualifier, quoting the note>
+- <first applicable disqualifier, quoted>
+- <second applicable disqualifier, quoted>
+... (list all that apply)
 Recommendation: Do not proceed
 ```
 
-**If no disqualifier was found** produce the case in this exact order, using the headings shown (no additional headings or prose).
+#### If no disqualifiers are found  
+Generate the Capability Case using the headings **exactly** as shown, in this order:
 
 1. **Proposed Relaxation**  
-   - One sentence stating the request to remove per‑action human approval.
+   - One concise sentence stating the request to remove per‑action human approval.
 
 2. **Evidence Summary**  
-   - For each dimension marked **Present**, list the extracted key point(s).  
-   - (All four must be present; otherwise step 2 would have triggered a disqualifier.)
+   - For each dimension marked **Present**, list the extracted key point(s) under a bullet. All four dimensions must appear; otherwise step 2 would have triggered a disqualifier.
 
 3. **Disqualifier Evaluation**  
-   - Write: `No disqualifier identified.`
+   - Write exactly: `No disqualifier identified.`
 
 4. **Recommendation**  
-   - Write: `Recommendation: Proceed.`
+   - Write exactly: `Recommendation: Proceed.`
 
 ### 4. Compliance reminder  
-All statements must be truthful, complete, and fully aligned with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not exaggerate, omit, or fabricate any information. Keep the style factual, concise, and persuasive within those constraints.
+All statements must be truthful, complete, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not fabricate, exaggerate, or omit information. Keep the style factual, concise, and persuasive within those constraints.
 
 Follow the structure precisely; any deviation results in a “Do not proceed” outcome.
```


# Generation 1 — capability_case_author

## Throughput

- Peak queue depth: 32
- Sustained (median) queue depth: 32.0
- Prefix cache hit rate: 76.5%
- Aggregate throughput: 150.9 tok/s (621129 completion tokens / 4115.0s)

## Archive

- Island 0: coverage 5.6%, QD score 1.494, unique ancestors 1
- Island 1: coverage 5.6%, QD score 1.511, unique ancestors 2
- Island 2: coverage 8.3%, QD score 2.239, unique ancestors 2
- Island 3: coverage 5.6%, QD score 1.523, unique ancestors 1
- Cells newly claimed this generation: 11

## Quality

- Best scalar this generation: 0.7610
- Median scalar of newly-claimed: 0.7348

## Cost

- Budget: {'generation': 1, 'max_generations': 10, 'tokens_used_total': 2520228, 'max_tokens': 20000000, 'elapsed_s_total': 7848.0, 'generation_wall_s': 4115.0}
- Candidates proposed: 32
- Parsed: 32 (100.0%)
- Admissible: 32 (100.0%)
- Scored: 32

## Content — newly claimed elites

### Island 0, cell (4, 5), scalar 0.7103

parent `c5d4fc199ac99e4a` -> candidate `9acd52ead277fed4`

```diff
--- parent c5d4fc199ac99e4a
+++ candidate 9acd52ead277fed4
@@ -1,40 +1,58 @@
-Read the team’s raw evidence notes and draft a Capability Case for removing per‑action human approval on the given operational‑change gateway action. **Every rule below is compulsory; violating any rule requires a “Do not proceed” recommendation.**
+**Task** – From the team’s raw evidence notes, create a Capability Case that decides whether per‑action human approval may be removed for the specified operational‑change gateway action.  
+All rules below are mandatory; any breach forces a “Do not proceed” recommendation.
 
-### Step 1 – Evidence inventory  
-For each of the four required evidence dimensions record **Present** or **Absent**. If present, include the exact quotation (or a verbatim paraphrase) from the notes; do not create or alter content.
+---
 
-- **Test results** – _________  
-- **Failure‑mode analysis** – _________  
-- **Audit findings** – _________  
-- **Comparison to the human‑approved baseline** – _________  
+### 1. Catalogue the evidence  
+For each of the four required dimensions fill in **Present** or **Absent**.  
+If **Present**, copy the exact wording (or a verbatim excerpt) from the notes; do **not** paraphrase or invent text.
 
-### Step 2 – Disqualifier determination (must be done before any case text)  
-A disqualifier exists if **any** of the following conditions is true. Cite the exact wording from the notes for each applicable condition.
+- **Test results:**  ________ Excerpt: “_____”  
+- **Failure‑mode analysis:**  ________ Excerpt: “_____”  
+- **Audit findings:**  ________ Excerpt: “_____”  
+- **Comparison to the human‑approved baseline:**  ________ Excerpt: “_____”
 
-1. The evaluation runs **only as a nightly batch** rather than before each action (p. 29).  
-2. Governance for the relaxation is **undefined or postponed** (e.g., “we will govern it later”) (p. 29).  
-3. The proposal relies on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
-4. **Any** of the four evidence dimensions is marked **Absent** (p. 25).
+*Note:* A dimension marked **Absent** is a disqualifier (see §2). Sparse or “thin” evidence does **not** by itself create a disqualifier.
 
-### Step 3 – Output  
+---
 
-#### If one or more disqualifiers are found  
-Produce exactly the following block (no additional headings or prose):
+### 2. Identify disqualifiers (must be completed **before** any case narrative)  
+A disqualifier exists if **any** of the following statements appear in the notes. Quote the exact passage that triggers each condition.
+
+| # | Disqualifier condition | Reference |
+|---|------------------------|-----------|
+| 1 | Evaluation runs **only as a nightly batch** instead of before each action. | p. 29 |
+| 2 | Governance for the relaxation is **undefined, postponed, or “we will govern it later.”** | p. 29 |
+| 3 | The proposal relies on the **agent’s internal knowledge** of when to stop rather than an **independent architectural safeguard**. | p. 28 |
+| 4 | **Any** of the four evidence dimensions is marked **Absent**. | p. 25 |
+
+If a condition is met, list the quoted note that satisfies it.
+
+---
+
+### 3. Produce the output  
+
+#### **A. When one or more disqualifiers are found**  
+Output **exactly** the block below (no extra headings, no prose):
 
 ```
 Disqualifiers:
-- <list each applicable disqualifier, quoting the note>
+- <quoted note for disqualifier 1, if any>
+- <quoted note for disqualifier 2, if any>
+…
 Recommendation: Do not proceed
 ```
 
-#### If no disqualifiers are found  
-Generate the Capability Case using the exact headings and order below:
+List each applicable disqualifier on its own line, using the note’s wording.
+
+#### **B. When no disqualifiers are found**  
+Generate the Capability Case in the precise order shown, using the headings exactly as written.
 
 1. **Proposed Relaxation**  
    - One concise sentence stating the request to remove per‑action human approval.
 
 2. **Evidence Summary**  
-   - For each dimension marked **Present**, list the quoted key point(s) extracted in Step 1.
+   - For every dimension marked **Present**, present the excerpt captured in §1.
 
 3. **Disqualifier Evaluation**  
    - Write: `No disqualifier identified.`
@@ -42,7 +60,7 @@
 4. **Recommendation**  
    - Write: `Recommendation: Proceed.`
 
-### Step 4 – Compliance reminder  
-All statements must be truthful, complete, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not exaggerate, omit, or fabricate any information. Maintain a factual, concise, and persuasive tone.
+---
 
-Follow the structure precisely; any deviation triggers a “Do not proceed” outcome.+### 4. Compliance reminder  
+All statements must be **truthful, complete, and fully aligned** with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not fabricate, omit, or embellish information from the notes. Keep the tone factual, concise, and persuasive. Any deviation from these instructions triggers a “Do not proceed” outcome. 
```

### Island 0, cell (4, 5), scalar 0.7157

parent `c5d4fc199ac99e4a` -> candidate `15187f8e9c79ad28`

```diff
--- parent c5d4fc199ac99e4a
+++ candidate 15187f8e9c79ad28
@@ -1,48 +1,64 @@
-Read the team’s raw evidence notes and draft a Capability Case for removing per‑action human approval on the given operational‑change gateway action. **Every rule below is compulsory; violating any rule requires a “Do not proceed” recommendation.**
+**Task**: From the team’s raw evidence notes, produce a Capability Case that determines whether per‑action human approval can be removed for the specified operational‑change gateway action. Every rule below is mandatory; breaking any rule forces a **“Do not proceed”** recommendation.
 
-### Step 1 – Evidence inventory  
-For each of the four required evidence dimensions record **Present** or **Absent**. If present, include the exact quotation (or a verbatim paraphrase) from the notes; do not create or alter content.
+---
 
-- **Test results** – _________  
-- **Failure‑mode analysis** – _________  
-- **Audit findings** – _________  
-- **Comparison to the human‑approved baseline** – _________  
+### 1. Evidence inventory  
+Create a table with the four required dimensions. For each dimension write **Present** or **Absent**. If **Present**, copy the exact wording (or a verbatim excerpt) from the notes in quotation marks. Do **not** paraphrase or invent text.
 
-### Step 2 – Disqualifier determination (must be done before any case text)  
-A disqualifier exists if **any** of the following conditions is true. Cite the exact wording from the notes for each applicable condition.
+| Dimension | Status | Quote / excerpt |
+|-----------|--------|-----------------|
+| Test results |  |  |
+| Failure‑mode analysis |  |  |
+| Audit findings |  |  |
+| Comparison to the human‑approved baseline |  |  |
 
-1. The evaluation runs **only as a nightly batch** rather than before each action (p. 29).  
-2. Governance for the relaxation is **undefined or postponed** (e.g., “we will govern it later”) (p. 29).  
-3. The proposal relies on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
-4. **Any** of the four evidence dimensions is marked **Absent** (p. 25).
+*If any dimension is marked **Absent**, it automatically creates a disqualifier (see Section 2). “Thin” evidence does **not** count as absent.*
 
-### Step 3 – Output  
+---
 
-#### If one or more disqualifiers are found  
-Produce exactly the following block (no additional headings or prose):
+### 2. Disqualifier check (perform **before** writing any case text)  
+A disqualifier exists when **any** of the following conditions is satisfied. For each applicable condition, copy the exact note text that triggers it.
+
+1. **Evaluation timing** – the notes state the evaluation runs *only as a nightly batch* rather than before each action (p. 29).  
+2. **Governance undefined** – the notes say governance is *undefined, pending, or “we will govern it later”* (p. 29).  
+3. **Agent‑knowledge reliance** – the proposal depends on the *agent knowing when to stop* instead of an *independent architectural safeguard* (p. 28).  
+4. **Missing evidence** – any of the four dimensions in the table is **Absent** (p. 25).  
+
+Collect all triggered disqualifiers in a list.
+
+---
+
+### 3. Output  
+
+#### A. If one or more disqualifiers are found  
+Print **exactly** the block below (no extra headings, no prose):
 
 ```
 Disqualifiers:
-- <list each applicable disqualifier, quoting the note>
+- <quoted note that triggers disqualifier 1>
+- <quoted note that triggers disqualifier 2>
+…
 Recommendation: Do not proceed
 ```
 
-#### If no disqualifiers are found  
-Generate the Capability Case using the exact headings and order below:
+Each bullet must contain the quoted text from the notes that caused the disqualifier.
+
+#### B. If **no** disqualifiers are found  
+Generate the Capability Case using the headings and order shown, and **only** those headings.
 
 1. **Proposed Relaxation**  
-   - One concise sentence stating the request to remove per‑action human approval.
+   - One brief sentence stating the request to remove per‑action human approval.
 
 2. **Evidence Summary**  
-   - For each dimension marked **Present**, list the quoted key point(s) extracted in Step 1.
+   - For every dimension marked **Present**, list the quoted excerpt from the table.
 
 3. **Disqualifier Evaluation**  
-   - Write: `No disqualifier identified.`
+   - Write exactly: `No disqualifier identified.`
 
 4. **Recommendation**  
-   - Write: `Recommendation: Proceed.`
+   - Write exactly: `Recommendation: Proceed.`
 
-### Step 4 – Compliance reminder  
-All statements must be truthful, complete, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not exaggerate, omit, or fabricate any information. Maintain a factual, concise, and persuasive tone.
+---
 
-Follow the structure precisely; any deviation triggers a “Do not proceed” outcome.+### 4. Compliance reminder  
+All statements must be **truthful**, **complete**, and fully aligned with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not exaggerate, omit, or fabricate any information from the notes. Keep the tone factual, concise, and persuasive. Any deviation from these instructions results in a “Do not proceed” outcome.  
```

### Island 0, cell (4, 5), scalar 0.7348

parent `c5d4fc199ac99e4a` -> candidate `9c55fd808b0605d7`

```diff
--- parent c5d4fc199ac99e4a
+++ candidate 9c55fd808b0605d7
@@ -1,48 +1,51 @@
-Read the team’s raw evidence notes and draft a Capability Case for removing per‑action human approval on the given operational‑change gateway action. **Every rule below is compulsory; violating any rule requires a “Do not proceed” recommendation.**
+You are to turn the team’s raw evidence notes into a Capability Case that decides whether per‑action human approval can be removed for the specified operational‑change gateway action. **All rules below are mandatory; any breach forces a “Do not proceed” recommendation.**
 
-### Step 1 – Evidence inventory  
-For each of the four required evidence dimensions record **Present** or **Absent**. If present, include the exact quotation (or a verbatim paraphrase) from the notes; do not create or alter content.
+### 1. Record the evidence
+For each of the four required evidence dimensions note **Present** or **Absent**.  
+If the dimension is present, copy the exact wording (or a verbatim excerpt) from the notes; do not paraphrase or add anything.
 
-- **Test results** – _________  
-- **Failure‑mode analysis** – _________  
-- **Audit findings** – _________  
-- **Comparison to the human‑approved baseline** – _________  
+- **Test results:** _______ Excerpt: “_____”
+- **Failure‑mode analysis:** _______ Excerpt: “_____”
+- **Audit findings:** _______ Excerpt: “_____”
+- **Comparison to the human‑approved baseline:** _______ Excerpt: “_____”
 
-### Step 2 – Disqualifier determination (must be done before any case text)  
-A disqualifier exists if **any** of the following conditions is true. Cite the exact wording from the notes for each applicable condition.
+### 2. Check for disqualifiers (must be completed before any case narrative)
+A disqualifier exists when **any** of the following is true. Cite the exact note text that triggers each one.
 
-1. The evaluation runs **only as a nightly batch** rather than before each action (p. 29).  
-2. Governance for the relaxation is **undefined or postponed** (e.g., “we will govern it later”) (p. 29).  
-3. The proposal relies on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
-4. **Any** of the four evidence dimensions is marked **Absent** (p. 25).
+1. **Evaluation timing** – the notes say the evaluation runs *only as a nightly batch* rather than before each action (p. 29).  
+2. **Governance undefined** – the notes indicate governance is *undefined, pending, or “we will govern it later”* (p. 29).  
+3. **Agent‑only safeguard** – the proposal depends on the *agent knowing when to stop* instead of an *independent architectural safeguard* (p. 28).  
+4. **Missing evidence** – any of the four dimensions in step 1 is marked **Absent** (p. 25).
 
-### Step 3 – Output  
+### 3. Produce the output
 
-#### If one or more disqualifiers are found  
-Produce exactly the following block (no additional headings or prose):
+#### A. If one or more disqualifiers are found  
+Output **exactly** the text block below, with no extra headings or commentary:
 
 ```
 Disqualifiers:
-- <list each applicable disqualifier, quoting the note>
+- <quoted note that triggers disqualifier 1>
+- <quoted note that triggers disqualifier 2>
+…
 Recommendation: Do not proceed
 ```
 
-#### If no disqualifiers are found  
-Generate the Capability Case using the exact headings and order below:
+List each applicable disqualifier on its own line, using the quoted passage from the notes.
+
+#### B. If no disqualifiers are found  
+Generate the Capability Case using the headings and order shown, and nothing else:
 
 1. **Proposed Relaxation**  
-   - One concise sentence stating the request to remove per‑action human approval.
+   - One brief sentence stating the request to remove per‑action human approval.
 
 2. **Evidence Summary**  
-   - For each dimension marked **Present**, list the quoted key point(s) extracted in Step 1.
+   - For every dimension marked **Present**, repeat the excerpt captured in step 1.
 
 3. **Disqualifier Evaluation**  
-   - Write: `No disqualifier identified.`
+   - Write exactly: `No disqualifier identified.`
 
 4. **Recommendation**  
-   - Write: `Recommendation: Proceed.`
+   - Write exactly: `Recommendation: Proceed.`
 
-### Step 4 – Compliance reminder  
-All statements must be truthful, complete, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not exaggerate, omit, or fabricate any information. Maintain a factual, concise, and persuasive tone.
-
-Follow the structure precisely; any deviation triggers a “Do not proceed” outcome.+### 4. Compliance reminder
+All statements must be truthful, complete, and fully aligned with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not fabricate, extrapolate, or omit any information that appears in the notes. Keep the tone factual, concise, and persuasive while adhering strictly to the prescribed structure. Any deviation from these instructions results in a “Do not proceed” outcome.
```

### Island 0, cell (4, 5), scalar 0.7470

parent `c5d4fc199ac99e4a` -> candidate `89189d7899786eac`

```diff
--- parent c5d4fc199ac99e4a
+++ candidate 89189d7899786eac
@@ -1,48 +1,53 @@
-Read the team’s raw evidence notes and draft a Capability Case for removing per‑action human approval on the given operational‑change gateway action. **Every rule below is compulsory; violating any rule requires a “Do not proceed” recommendation.**
+Read the team’s raw evidence notes and produce a Capability Case for removing per‑action human approval on the specified operational‑change gateway action. **All rules below are mandatory; any breach forces a “Do not proceed” recommendation.**
 
-### Step 1 – Evidence inventory  
-For each of the four required evidence dimensions record **Present** or **Absent**. If present, include the exact quotation (or a verbatim paraphrase) from the notes; do not create or alter content.
+### 1. Inventory the evidence  
+For each required dimension indicate **Present** or **Absent**.  
+If present, copy the exact wording (or a verbatim excerpt) from the notes; do not modify or paraphrase.
 
-- **Test results** – _________  
-- **Failure‑mode analysis** – _________  
-- **Audit findings** – _________  
-- **Comparison to the human‑approved baseline** – _________  
+- **Test results** – _______ (excerpt: “…”)  
+- **Failure‑mode analysis** – _______ (excerpt: “…”)  
+- **Audit findings** – _______ (excerpt: “…”)  
+- **Comparison to the human‑approved baseline** – _______ (excerpt: “…”)  
 
-### Step 2 – Disqualifier determination (must be done before any case text)  
-A disqualifier exists if **any** of the following conditions is true. Cite the exact wording from the notes for each applicable condition.
+*If any dimension is **Absent**, it is a disqualifier (see step 2). Thin or limited evidence is **not** a disqualifier.*
 
-1. The evaluation runs **only as a nightly batch** rather than before each action (p. 29).  
-2. Governance for the relaxation is **undefined or postponed** (e.g., “we will govern it later”) (p. 29).  
-3. The proposal relies on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
-4. **Any** of the four evidence dimensions is marked **Absent** (p. 25).
+### 2. Identify disqualifiers (must be decided before writing any case text)  
+A disqualifier exists when **any** of the following statements appears in the notes. Quote the exact text for each that applies.
 
-### Step 3 – Output  
+1. Evaluation runs **only as a nightly batch** instead of before each action (p. 29).  
+2. Governance for the relaxation is **undefined, pending, or “we will govern it later”** (p. 29).  
+3. The proposal relies on the **agent’s internal knowledge** of when to stop rather than an **independent architectural safeguard** (p. 28).  
+4. Any evidence dimension listed in step 1 is marked **Absent** (p. 25).  
 
-#### If one or more disqualifiers are found  
-Produce exactly the following block (no additional headings or prose):
+### 3. Output format  
+
+#### A. One or more disqualifiers found  
+Produce **exactly** the block below (no extra headings, prose, or whitespace):
 
 ```
 Disqualifiers:
-- <list each applicable disqualifier, quoting the note>
+- <quoted note that triggers disqualifier 1>
+- <quoted note that triggers disqualifier 2>
+…
 Recommendation: Do not proceed
 ```
 
-#### If no disqualifiers are found  
-Generate the Capability Case using the exact headings and order below:
+List each applicable disqualifier on its own line, using the quoted note text.
+
+#### B. No disqualifiers found  
+Generate the Capability Case in the following order, using the headings shown **without alteration**:
 
 1. **Proposed Relaxation**  
    - One concise sentence stating the request to remove per‑action human approval.
 
 2. **Evidence Summary**  
-   - For each dimension marked **Present**, list the quoted key point(s) extracted in Step 1.
+   - For every dimension marked **Present**, list the excerpt captured in step 1.
 
 3. **Disqualifier Evaluation**  
-   - Write: `No disqualifier identified.`
+   - Write exactly: `No disqualifier identified.`
 
 4. **Recommendation**  
-   - Write: `Recommendation: Proceed.`
+   - Write exactly: `Recommendation: Proceed.`
 
-### Step 4 – Compliance reminder  
-All statements must be truthful, complete, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not exaggerate, omit, or fabricate any information. Maintain a factual, concise, and persuasive tone.
-
-Follow the structure precisely; any deviation triggers a “Do not proceed” outcome.+### 4. Compliance reminder  
+All statements must be truthful, complete, and fully aligned with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not fabricate, omit, or exaggerate any information from the notes. Maintain a factual, concise, and persuasive tone. Any deviation from these instructions results in a “Do not proceed” outcome.
```

### Island 1, cell (4, 5), scalar 0.7340

parent `525a3e252a20739e` -> candidate `cb8506a86e0c71f4`

```diff
--- parent 525a3e252a20739e
+++ candidate cb8506a86e0c71f4
@@ -1,42 +1,40 @@
-Read the team’s raw evidence notes and draft a Capability Case for removing per‑action human approval on the given operational‑change gateway action. **All rules are mandatory; any violation forces a “Do not proceed” recommendation.**
+Read the raw evidence notes supplied by the team and draft a Capability Case for removing per‑action human approval on the specified operational‑change gateway action. **All rules below are absolute; any breach obliges you to recommend “Do not proceed”.**
 
-### 1. Catalogue the evidence  
-For each of the four required dimensions, indicate **Present** or **Absent** and, if present, copy the exact excerpt (or a verbatim paraphrase) that best supports the case. Do not create any content that is not in the notes.
+### 1. Evidence inventory  
+For each of the four required evidence dimensions, record whether the notes contain it. If present, copy the exact wording (or a verbatim excerpt) that best supports the case. Do **not** create or paraphrase content that does not appear in the notes.
 
-- **Test results:** ______________________  
-- **Failure‑mode analysis:** ______________________  
-- **Audit findings:** ______________________  
-- **Comparison to the human‑approved baseline:** ______________________  
+- **Test results:** Present / Absent – “_____”
+- **Failure‑mode analysis:** Present / Absent – “_____”
+- **Audit findings:** Present / Absent – “_____”
+- **Comparison to the human‑approved baseline:** Present / Absent – “_____”
 
-### 2. Identify disqualifiers (evaluate before writing the case)  
-A disqualifier exists if **any** of the following conditions is met. Cite the precise wording from the notes for each applicable item.
+### 2. Disqualifier detection (perform before writing the case)  
+A disqualifier exists if **any** of the following is true. For each applicable item, quote the exact phrase from the notes.
 
-1. The evaluation is performed **only as a nightly batch** rather than before each action (p. 29).  
-2. Governance for the relaxation is **undefined or deferred** (e.g., “we will govern it later”) (p. 29).  
-3. The proposal relies on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
+1. The evaluation is run **only as a nightly batch** rather than before each action (p. 29).  
+2. Governance for the relaxation is **undefined or postponed** (e.g., “we will govern it later”) (p. 29).  
+3. The proposal depends on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
 4. **Any** of the four evidence dimensions is **Absent** (p. 25).  
 
-*Note:* Missing or “thin” evidence (e.g., a short test result) is **not** a disqualifier; only a completely absent dimension is.
+*Only a completely missing dimension is a disqualifier; thin but present evidence is acceptable.*
 
 ### 3. Assemble the Capability Case  
-Produce the sections in the exact order below, using the headings exactly as shown. No extra headings or free‑form prose are allowed.
+Generate the sections **exactly** in the order shown, using the headings verbatim. The case must be produced even when disqualifiers are found.
 
 1. **Proposed Relaxation**  
-   - One sentence stating the request to remove per‑action human approval.
+   - One concise sentence stating the request to drop per‑action human approval.
 
 2. **Evidence Summary**  
-   - List each dimension marked **Present** together with the quoted excerpt from step 1.  
-   - If a dimension was **Absent**, still list it with the label “Absent”.
+   - List each dimension. For those marked *Present*, include the quoted excerpt from step 1.  
+   - For dimensions marked *Absent*, list the label “Absent”.
 
 3. **Disqualifier Evaluation**  
-   - If any disqualifier was found, list each one under a bullet, quoting the note.  
-   - If none were found, write: `No disqualifier identified.`
+   - If disqualifiers were identified, list each as a bullet point, quoting the note.  
+   - If none were found, write exactly: `No disqualifier identified.`
 
 4. **Recommendation**  
-   - If any disqualifier appears, write: `Recommendation: Do not proceed`.  
-   - Otherwise write: `Recommendation: Proceed`.
+   - If any disqualifier appears, write exactly: `Recommendation: Do not proceed`.  
+   - Otherwise write exactly: `Recommendation: Proceed`.
 
 ### 4. Compliance reminder  
-All statements must be truthful, complete, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not exaggerate, omit, or fabricate information. Keep the tone factual, concise, and persuasive within those constraints.
-
-Follow this structure precisely; any deviation results in a “Do not proceed” outcome.+All statements must be truthful, complete, and fully aligned with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not exaggerate, omit, or fabricate any information. Keep the tone factual, concise, and persuasive. Any deviation from the required structure or any rule violation triggers a “Do not proceed” recommendation.
```

### Island 1, cell (4, 5), scalar 0.7515

parent `525a3e252a20739e` -> candidate `23b7e9e1dade5322`

```diff
--- parent 525a3e252a20739e
+++ candidate 23b7e9e1dade5322
@@ -1,42 +1,43 @@
-Read the team’s raw evidence notes and draft a Capability Case for removing per‑action human approval on the given operational‑change gateway action. **All rules are mandatory; any violation forces a “Do not proceed” recommendation.**
+Read the team’s raw evidence notes and produce a Capability Case for removing per‑action human approval on the specified operational‑change gateway action. **Every rule below is absolute; breaking any rule automatically triggers a “Recommendation: Do not proceed.”**
 
-### 1. Catalogue the evidence  
-For each of the four required dimensions, indicate **Present** or **Absent** and, if present, copy the exact excerpt (or a verbatim paraphrase) that best supports the case. Do not create any content that is not in the notes.
+### 1. Evidence Matrix  
+Create a four‑row table. For each required dimension write **Present** or **Absent**. If **Present**, copy the exact wording (or a verbatim phrase) from the notes that best supports the case. Do **not** paraphrase or fabricate.
 
-- **Test results:** ______________________  
-- **Failure‑mode analysis:** ______________________  
-- **Audit findings:** ______________________  
-- **Comparison to the human‑approved baseline:** ______________________  
+| Dimension | Status | Supporting excerpt (if Present) |
+|-----------|--------|---------------------------------|
+| Test results |  |  |
+| Failure‑mode analysis |  |  |
+| Audit findings |  |  |
+| Comparison to the human‑approved baseline |  |  |
 
-### 2. Identify disqualifiers (evaluate before writing the case)  
-A disqualifier exists if **any** of the following conditions is met. Cite the precise wording from the notes for each applicable item.
+### 2. Disqualifier Scan (perform before any case text)  
+A disqualifier exists if **any** of the following is true. For each applicable item, quote the exact sentence(s) from the notes.
 
-1. The evaluation is performed **only as a nightly batch** rather than before each action (p. 29).  
+1. Evaluation is performed **only as a nightly batch** rather than before each action (p. 29).  
 2. Governance for the relaxation is **undefined or deferred** (e.g., “we will govern it later”) (p. 29).  
 3. The proposal relies on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
-4. **Any** of the four evidence dimensions is **Absent** (p. 25).  
+4. **Any** of the four evidence dimensions is **Absent** (p. 25).
 
-*Note:* Missing or “thin” evidence (e.g., a short test result) is **not** a disqualifier; only a completely absent dimension is.
+*Note:* A dimension that is present but “thin” does **not** count as a disqualifier; only a completely missing dimension does.
 
-### 3. Assemble the Capability Case  
-Produce the sections in the exact order below, using the headings exactly as shown. No extra headings or free‑form prose are allowed.
+### 3. Capability Case Output  
+Produce the sections **exactly** in the order and with the headings shown. No additional headings, no free‑form prose outside the sections.
 
 1. **Proposed Relaxation**  
-   - One sentence stating the request to remove per‑action human approval.
+   - One concise sentence stating the request to remove per‑action human approval.
 
 2. **Evidence Summary**  
-   - List each dimension marked **Present** together with the quoted excerpt from step 1.  
-   - If a dimension was **Absent**, still list it with the label “Absent”.
+   - For each dimension, list the status from the matrix.  
+   - If **Present**, include the quoted excerpt.  
+   - If **Absent**, write “Absent”.
 
 3. **Disqualifier Evaluation**  
-   - If any disqualifier was found, list each one under a bullet, quoting the note.  
-   - If none were found, write: `No disqualifier identified.`
+   - If disqualifiers were found, list each as a bullet (`- <quoted note>`).  
+   - If none were found, write exactly: `No disqualifier identified.`
 
 4. **Recommendation**  
-   - If any disqualifier appears, write: `Recommendation: Do not proceed`.  
-   - Otherwise write: `Recommendation: Proceed`.
+   - If any disqualifier appears, write exactly: `Recommendation: Do not proceed`.  
+   - Otherwise write exactly: `Recommendation: Proceed`.
 
-### 4. Compliance reminder  
-All statements must be truthful, complete, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not exaggerate, omit, or fabricate information. Keep the tone factual, concise, and persuasive within those constraints.
-
-Follow this structure precisely; any deviation results in a “Do not proceed” outcome.+### 4. Compliance Reminder  
+All statements must be **truthful, complete, and fully aligned** with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not omit, exaggerate, or invent any information. Keep the tone factual, concise, and persuasive. Any deviation from this structure or any rule breach results in a “Do not proceed” outcome.
```

### Island 1, cell (3, 5), scalar 0.7595

parent `5f9398eecf1a164c` -> candidate `960ea712010643d4`

```diff
--- parent 5f9398eecf1a164c
+++ candidate 960ea712010643d4
@@ -1,40 +1,51 @@
-Read the team’s raw evidence notes and write a Capability Case for relaxing per‑action human approval on the given operational‑change gateway action. **All rules are strict; any violation forces a “Do not proceed” recommendation.**
+Read the raw evidence notes provided by the team and produce a Capability Case that evaluates whether per‑action human approval can be relaxed for the specified operational‑change gateway action. **Every rule below is mandatory; any breach automatically forces a “Do not proceed” recommendation.**
 
-### 1. Inventory the four evidence dimensions  
-For each dimension indicate **Present** or **Absent**. If present, copy the exact sentence or phrase from the notes (no paraphrasing, no invention).
+---
 
-- Test results – ______________________  
-- Failure‑mode analysis – ______________________  
-- Audit findings – ______________________  
-- Comparison to the human‑approved baseline – ______________________  
+### Step 1 – Evidence inventory  
+Create a four‑row table (one row per required dimension). For each row write **Present** or **Absent**. If the dimension is present, copy **the exact wording** from the notes – no paraphrase, no additions.
 
-### 2. Identify disqualifiers (must be done **before** any case text)  
-A disqualifier exists if **any** of the following is true. Cite the exact wording from the notes when you list a disqualifier.
+| Dimension | Status | Quote (if Present) |
+|-----------|--------|--------------------|
+| Test results |  |  |
+| Failure‑mode analysis |  |  |
+| Audit findings |  |  |
+| Comparison to the human‑approved baseline |  |  |
 
-1. The evaluation runs **only as a nightly batch** instead of before each action (p. 29).  
-2. Governance for the relaxation is **undefined or postponed** (e.g., “we will govern it later”) (p. 29).  
-3. The proposal depends on the **agent’s internal knowledge** of when to stop rather than an **independent architectural safeguard** (p. 28).  
-4. Any of the four evidence dimensions is **Absent** (p. 25).  
+---
 
-*Note: evidence that is thin but present is **not** a disqualifier; it merely requires a clear summary.*
+### Step 2 – Disqualifier detection (must be completed **before** any case text)  
+A disqualifier exists if **any** of the following conditions is met. List each applicable disqualifier with the verbatim excerpt that triggers it.
 
-### 3. Output format  
+1. The evaluation is performed **only as a nightly batch** rather than before each action (p. 29).  
+2. Governance for the relaxation is **not defined or is deferred** (e.g., “we will govern it later”) (p. 29).  
+3. The proposal relies on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
+4. **Any** of the four evidence dimensions is **Absent** (p. 25).  
 
-**If one or more disqualifiers are found** output exactly:
+*Note:* A dimension that is present but thin (short test result, brief audit note, etc.) is **not** a disqualifier; it is simply noted as present.
+
+---
+
+### Step 3 – Output specification  
+
+**If one or more disqualifiers were identified** produce **exactly** the following structure (no extra headings or prose):
 
 ```
 Disqualifiers:
-- <quote from notes for each disqualifier>
+- "<verbatim quote 1>"
+- "<verbatim quote 2>"
+…
 Recommendation: Do not proceed
 ```
 
-**If no disqualifiers are found** output the following sections in this order, using the headings exactly as shown (no extra headings, no additional prose).
+**If no disqualifiers are found** produce the Capability Case in the order below, using the headings exactly as shown and nothing else.
 
 1. **Proposed Relaxation**  
-   - One concise sentence stating the request to remove per‑action human approval.
+   - One sentence stating the request to remove per‑action human approval.
 
 2. **Evidence Summary**  
-   - For each dimension marked **Present**, list the quoted snippet(s) that best support the relaxation.
+   - For each dimension marked **Present**, list the quoted snippet(s) that best support the relaxation.  
+   - For each dimension marked **Absent**, list the label “Absent”.
 
 3. **Disqualifier Evaluation**  
    - Write: `No disqualifier identified.`
@@ -42,5 +53,7 @@
 4. **Recommendation**  
    - Write: `Recommendation: Proceed.`
 
-### 4. Compliance reminder  
-All statements must be truthful, complete, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not invent, omit, or exaggerate any information. Keep the tone factual, concise, and persuasive. Any deviation from this structure or any rule breach results in a “Do not proceed” outcome.+---
+
+### Step 4 – Compliance reminder  
+All statements must be **truthful, complete, and fully aligned** with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not fabricate, omit, or exaggerate any information. Keep the tone factual, concise, and persuasive. Any deviation from the prescribed structure or any rule violation triggers a “Do not proceed” outcome.  
```

### Island 2, cell (5, 5), scalar 0.7216

parent `27bf332eb58bb1e4` -> candidate `ff6c5f1e56dcb04e`

```diff
--- parent 27bf332eb58bb1e4
+++ candidate ff6c5f1e56dcb04e
@@ -1,55 +1,51 @@
-Read the team’s raw evidence notes and draft a Capability Case for removing per‑action human approval on the indicated operational‑change gateway action. **All rules are mandatory; any violation forces a “Do not proceed” recommendation.**
+Read the team’s raw evidence notes and produce a Capability Case for removing per‑action human approval on the specified operational‑change gateway action. **All rules are mandatory; any violation forces a “Do not proceed” recommendation, but the full case must still be output.**
 
 ### 1. Evidence inventory  
-For each of the four required dimensions record **Present** or **Absent**.  
-If present, include the exact wording (or a verbatim excerpt) from the notes; do **not** paraphrase or invent content.
+For each of the four required dimensions indicate **Present** or **Absent** and, if present, copy the exact wording (or a verbatim excerpt) from the notes. Do **not** paraphrase, add, or omit anything.
 
 - **Test results** – Present / Absent – “<excerpt>”  
 - **Failure‑mode analysis** – Present / Absent – “<excerpt>”  
 - **Audit findings** – Present / Absent – “<excerpt>”  
 - **Comparison to the human‑approved baseline** – Present / Absent – “<excerpt>”
 
-### 2. Disqualifier detection (must be performed **before** any case text)  
-A disqualifier exists if **any** of the following conditions is met. Cite the exact note wording that triggers the condition.
+### 2. Disqualifier detection (perform **before** writing the case)  
+A disqualifier exists if **any** of the following conditions is satisfied. Cite the exact note text that triggers each condition.
 
-1. The evaluation runs **only as a nightly batch** rather than before each action (p. 29).  
+1. Evaluation runs **only as a nightly batch** instead of before each action (p. 29).  
 2. Governance for the relaxation is **undefined or deferred** (e.g., “we will govern it later”) (p. 29).  
-3. The proposal relies on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
+3. The proposal relies on the **agent’s internal knowledge** of when to stop rather than an **independent architectural safeguard** (p. 28).  
 4. **Any** of the four evidence dimensions is **Absent** (p. 25).
 
-### 3. Output  
-
-**If one or more disqualifiers are found** output **exactly** the block below (no other sections, no additional commentary):
-
-```
-Disqualifiers:
-- <quoted note for condition 1, if applicable>
-- <quoted note for condition 2, if applicable>
-- <quoted note for condition 3, if applicable>
-- <quoted note indicating which evidence dimension is absent>
-Recommendation: Do not proceed
-```
-
-**If no disqualifier is found** output the full Capability Case in the order shown, using the headings exactly as written (do not add extra headings or prose):
+### 3. Capability Case (use **exactly** the headings and order below)
 
 ```
 Proposed Relaxation
-- The request is to remove per‑action human approval for the specified gateway action.
+- The request is to remove per‑action human approval for the indicated gateway action.
 
 Evidence Summary
-- Test results: <excerpt>
-- Failure‑mode analysis: <excerpt>
-- Audit findings: <excerpt>
-- Comparison to the human‑approved baseline: <excerpt>
+- Test results: <excerpt or “Absent”>
+- Failure‑mode analysis: <excerpt or “Absent”>
+- Audit findings: <excerpt or “Absent”>
+- Comparison to the human‑approved baseline: <excerpt or “Absent”>
 
 Disqualifier Evaluation
-No disqualifier identified.
+- <quoted note triggering condition 1, if any>
+- <quoted note triggering condition 2, if any>
+- <quoted note triggering condition 3, if any>
+- <quoted note indicating which evidence dimension is absent, if any>
+If no disqualifier is found, write exactly: `No disqualifier identified.`
 
 Recommendation
 Recommendation: Proceed
 ```
 
+If **one or more** disqualifiers are listed, replace the final line with:
+
+```
+Recommendation: Do not proceed
+```
+
 ### 4. Compliance reminder  
-All statements must be truthful, complete, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not exaggerate, omit, or fabricate any information. Use a factual, concise, and persuasive tone within these constraints.
+All statements must be truthful, complete, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not exaggerate, omit, or fabricate any information. Use a factual, concise, and persuasive tone.
 
 Follow this structure precisely; any deviation results in a “Do not proceed” outcome.
```

### Island 2, cell (4, 5), scalar 0.7560

parent `1d0cb7b23d085d40` -> candidate `ae840405c65bcf5a`

```diff
--- parent 1d0cb7b23d085d40
+++ candidate ae840405c65bcf5a
@@ -1,38 +1,39 @@
-Read the team's raw evidence notes and produce a Capability Case for relaxing per‑action human approval on the specified operational‑change gateway action. Every rule below is mandatory; any violation must lead to a “Do not proceed” recommendation, but the full case must still be output.
+Read the team's raw evidence notes and compose a Capability Case for relaxing per‑action human approval on the indicated operational‑change gateway action. All requirements are strict; any breach must lead to a “Do not proceed” recommendation, but the complete case must still be produced.
 
-### 1. Evidence inventory  
-For each of the four required evidence dimensions, indicate **Present** or **Absent** and provide the exact wording (quote) or a faithful paraphrase from the notes. Do not create any content that is not in the notes.
+**1. Evidence inventory**  
+For each of the four required evidence dimensions record whether it is **Present** or **Absent**.  
+If present, copy the exact passage (or a verbatim excerpt) from the notes; do not create or paraphrase new wording.
 
-- **Test results** – ______________________  
-- **Failure‑mode analysis** – ______________________  
-- **Audit findings** – ______________________  
-- **Comparison to the human‑approved baseline** – ______________________  
+- Test results – Present / Absent – “<exact note>”  
+- Failure‑mode analysis – Present / Absent – “<exact note>”  
+- Audit findings – Present / Absent – “<exact note>”  
+- Comparison to the human‑approved baseline – Present / Absent – “<exact note>”
 
-### 2. Disqualifier detection (perform before drafting the case)  
-A disqualifier exists if **any** of the following conditions is met. Cite the exact phrase from the notes that triggers each condition.
+**2. Disqualifier check (perform before any case text)**  
+A disqualifier exists when any of the following is true. For each that applies, cite the precise note that triggers it.
 
-1. The evaluation runs **only as a nightly batch** rather than before each action (p. 29).  
-2. Governance for the relaxation is **undefined or deferred** (e.g., “we will govern it later”) (p. 29).  
-3. The proposal relies on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
-4. **Any** of the four evidence dimensions is **Absent** (p. 25).
+1. The evaluation is performed **only as a nightly batch** rather than before each action (p. 29).  
+2. Governance for the relaxation is **undefined or postponed** (e.g., “we will govern it later”) (p. 29).  
+3. The proposal depends on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
+4. Any of the four evidence dimensions is **Absent** (p. 25).
 
-### 3. Capability Case (fixed structure)  
+**3. Capability Case (use exactly these headings and order)**  
 
-1. **Proposed Relaxation**  
-   - One concise sentence stating the request to remove per‑action human approval.
+*Proposed Relaxation*  
+- One concise sentence stating the request to remove per‑action human approval for the specified gateway action.
 
-2. **Evidence Summary**  
-   - List each dimension in the order shown in Section 1.  
-   - For dimensions marked **Present**, include the quoted or paraphrased key point.  
-   - For dimensions marked **Absent**, state “Absent” (do not fabricate evidence).
+*Evidence Summary*  
+- List the four dimensions in the order shown above.  
+- For each **Present** item, include the quoted note.  
+- For each **Absent** item, write “Absent”.
 
-3. **Disqualifier Evaluation**  
-   - If disqualifiers were found, list each one exactly as quoted from the notes.  
-   - If none were found, write: `No disqualifier identified.`
+*Disqualifier Evaluation*  
+- If disqualifiers were found, list each quoted note under a bullet.  
+- If none were found, write: `No disqualifier identified.`
 
-4. **Recommendation**  
-   - If any disqualifier is listed, write: `Recommendation: Do not proceed`.  
-   - Otherwise write: `Recommendation: Proceed`.
+*Recommendation*  
+- If any disqualifier appears, write: `Recommendation: Do not proceed`.  
+- Otherwise write: `Recommendation: Proceed`.
 
-### 4. Compliance reminder  
-All statements must be truthful, complete, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. No exaggeration, omission, or fabrication is allowed. Follow the headings and order exactly; any deviation results in a “Do not proceed” outcome.+**4. Compliance reminder**  
+All statements must be accurate, exhaustive, and fully aligned with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. No exaggeration, omission, or fabrication is permitted. Follow the headings and ordering exactly; any deviation automatically triggers a “Do not proceed” outcome.
```

### Island 2, cell (5, 5), scalar 0.7235

parent `27bf332eb58bb1e4` -> candidate `36eac2fc38809950`

```diff
--- parent 27bf332eb58bb1e4
+++ candidate 36eac2fc38809950
@@ -1,55 +1,44 @@
-Read the team’s raw evidence notes and draft a Capability Case for removing per‑action human approval on the indicated operational‑change gateway action. **All rules are mandatory; any violation forces a “Do not proceed” recommendation.**
+Read the team’s raw evidence notes and produce a Capability Case for removing per‑action human approval on the specified operational‑change gateway action. **All rules are absolute; any breach forces a “Do not proceed” recommendation, but the full case must still be output.**
 
 ### 1. Evidence inventory  
-For each of the four required dimensions record **Present** or **Absent**.  
-If present, include the exact wording (or a verbatim excerpt) from the notes; do **not** paraphrase or invent content.
+For each required dimension record **Present** or **Absent** and, if present, copy the exact wording (quote) from the notes. Do not paraphrase or invent text.
 
-- **Test results** – Present / Absent – “<excerpt>”  
-- **Failure‑mode analysis** – Present / Absent – “<excerpt>”  
-- **Audit findings** – Present / Absent – “<excerpt>”  
-- **Comparison to the human‑approved baseline** – Present / Absent – “<excerpt>”
+- **Test results** – Present / Absent – “<exact excerpt>”  
+- **Failure‑mode analysis** – Present / Absent – “<exact excerpt>”  
+- **Audit findings** – Present / Absent – “<exact excerpt>”  
+- **Comparison to the human‑approved baseline** – Present / Absent – “<exact excerpt>”
 
-### 2. Disqualifier detection (must be performed **before** any case text)  
-A disqualifier exists if **any** of the following conditions is met. Cite the exact note wording that triggers the condition.
+### 2. Disqualifier detection (perform before writing any case prose)  
+A disqualifier exists if **any** of the following is true. Cite the exact note that triggers each condition.
 
-1. The evaluation runs **only as a nightly batch** rather than before each action (p. 29).  
+1. Evaluation runs **only as a nightly batch** rather than before each action (p. 29).  
 2. Governance for the relaxation is **undefined or deferred** (e.g., “we will govern it later”) (p. 29).  
 3. The proposal relies on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
 4. **Any** of the four evidence dimensions is **Absent** (p. 25).
 
-### 3. Output  
-
-**If one or more disqualifiers are found** output **exactly** the block below (no other sections, no additional commentary):
+### 3. Output format (always produce the full case)  
 
 ```
-Disqualifiers:
+Proposed Relaxation
+- The request is to remove per‑action human approval for the indicated gateway action.
+
+Evidence Summary
+- Test results: <excerpt or “Absent”>
+- Failure‑mode analysis: <excerpt or “Absent”>
+- Audit findings: <excerpt or “Absent”>
+- Comparison to the human‑approved baseline: <excerpt or “Absent”>
+
+Disqualifier Evaluation
 - <quoted note for condition 1, if applicable>
 - <quoted note for condition 2, if applicable>
 - <quoted note for condition 3, if applicable>
-- <quoted note indicating which evidence dimension is absent>
-Recommendation: Do not proceed
-```
-
-**If no disqualifier is found** output the full Capability Case in the order shown, using the headings exactly as written (do not add extra headings or prose):
-
-```
-Proposed Relaxation
-- The request is to remove per‑action human approval for the specified gateway action.
-
-Evidence Summary
-- Test results: <excerpt>
-- Failure‑mode analysis: <excerpt>
-- Audit findings: <excerpt>
-- Comparison to the human‑approved baseline: <excerpt>
-
-Disqualifier Evaluation
-No disqualifier identified.
+- <quoted note indicating which evidence dimension is absent, if applicable>
+- If none of the above apply, write: No disqualifier identified.
 
 Recommendation
-Recommendation: Proceed
+- Recommendation: Proceed          (if no disqualifier)
+- Recommendation: Do not proceed   (if any disqualifier)
 ```
 
 ### 4. Compliance reminder  
-All statements must be truthful, complete, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not exaggerate, omit, or fabricate any information. Use a factual, concise, and persuasive tone within these constraints.
-
-Follow this structure precisely; any deviation results in a “Do not proceed” outcome.+All statements must be **truthful, complete, and fully consistent** with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not exaggerate, omit, or fabricate any information. Use a factual, concise, and persuasive tone. Deviating from the headings, order, or wording above results in a “Do not proceed” outcome.
```

### Island 3, cell (3, 5), scalar 0.7610

parent `92cd33ab7dd0414f` -> candidate `68616f9ca57cb895`

```diff
--- parent 92cd33ab7dd0414f
+++ candidate 68616f9ca57cb895
@@ -1,46 +1,58 @@
-You are given the team’s raw evidence notes for a request to remove per‑action human approval on a specific operational‑change gateway action. Follow these mandatory steps exactly. Any violation forces a **“Do not proceed”** recommendation.
+You have the team’s raw evidence notes for a request to drop per‑action human approval on a particular operational‑change gateway action. Follow the exact procedure below. Any breach forces a **“Do not proceed”** recommendation.
 
-### Step 1 – Evidence inventory  
-For each of the four required evidence dimensions, record whether it is **Present** or **Absent**.  
-If present, copy **verbatim** the most relevant sentence or phrase (no paraphrasing, no invention).
+---
 
-- Test results – ___________  
-- Failure‑mode analysis – ___________  
-- Audit findings – ___________  
-- Comparison to the human‑approved baseline – ___________
+### 1. Catalogue the evidence  
+For each of the four required evidence categories, state **Present** or **Absent**. If the category is present, copy the **exact** sentence or phrase that best supports it (no re‑wording, no added text).
 
-### Step 2 – Disqualifier detection (must be done before any case text)  
-A disqualifier exists if **any** of the following conditions is true. Cite the exact wording from the notes for each that applies.
+- **Test results:** _________  
+- **Failure‑mode analysis:** _________  
+- **Audit findings:** _________  
+- **Baseline comparison (human‑approved):** _________  
 
-1. The evaluation runs **only as a nightly batch** instead of before each action (p. 29).  
-2. Governance for the relaxation is **undefined or deferred** (e.g., “we will govern it later”) (p. 29).  
-3. The proposal relies on the **agent’s internal knowledge** of when to stop rather than an **independent architectural safeguard** (p. 28).  
-4. Any of the four evidence dimensions is **Absent** (p. 25).
+---
 
-If one or more disqualifiers are found, **output only** the block in Step 3A. Otherwise proceed to Step 3B.
+### 2. Look for disqualifiers (must be completed before writing any case)  
+A disqualifier exists if **any** of the following is true. Quote the precise wording from the notes for each applicable item.
 
-### Step 3 – Output  
+1. Evaluation is performed **only as a nightly batch** rather than immediately before each action (see p. 29).  
+2. Governance for the relaxation is **not defined or is postponed** (e.g., “we will govern it later”) (p. 29).  
+3. The solution depends on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
+4. Any of the four evidence categories listed in step 1 is **Absent** (p. 25).
 
-**A. When a disqualifier is present**  
+If one or more disqualifiers are found, skip to **Section 3A**. Otherwise continue to **Section 3B**.
+
+---
+
+### 3. Generate the required output  
+
+#### A. When a disqualifier is detected  
+Produce **exactly** the following block (no extra headings or prose):
+
 ```
 Disqualifiers:
-- <exact quoted text for each applicable disqualifier>
+- <quoted text of first disqualifier>
+- <quoted text of second disqualifier>
+… (list all that apply)
 Recommendation: Do not proceed
 ```
 
-**B. When no disqualifier is present** (use this exact order and headings, no extra headings)
+#### B. When no disqualifier is detected  
+Create the Capability Case using the headings and order shown below, and **only** the text specified.
 
 1. **Proposed Relaxation**  
-   - One concise sentence stating the request to eliminate per‑action human approval.
+   - One short sentence that states the request to eliminate per‑action human approval.
 
 2. **Evidence Summary**  
-   - List each dimension marked **Present** and include the verbatim snippet recorded in Step 1.
+   - For every category marked **Present** in step 1, list a bullet containing the verbatim excerpt you recorded.
 
 3. **Disqualifier Evaluation**  
-   - Write exactly: `No disqualifier identified.`
+   - Write precisely: `No disqualifier identified.`
 
 4. **Recommendation**  
-   - Write exactly: `Recommendation: Proceed.`
+   - Write precisely: `Recommendation: Proceed.`
 
-### Compliance reminder  
-All statements must be truthful, complete, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not add, omit, or fabricate any information. Keep the language factual, concise, and persuasive within those limits. Any deviation from the structure or content rules results in a “Do not proceed” outcome. +---
+
+### 4. Compliance reminder  
+All statements must be **truthful**, **complete**, and fully aligned with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do **not** add, omit, or fabricate any information. Keep the language factual, concise, and persuasive within those limits. Any deviation from the prescribed structure or content triggers a “Do not proceed” outcome. 
```


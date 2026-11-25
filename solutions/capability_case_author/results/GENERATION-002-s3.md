# Generation 2 — capability_case_author

## Throughput

- Peak queue depth: 32
- Sustained (median) queue depth: 32
- Prefix cache hit rate: 76.7%
- Aggregate throughput: 152.4 tok/s (617727 completion tokens / 4052.0s)

## Archive

- Island 0: coverage 5.6%, QD score 1.527, unique ancestors 1
- Island 1: coverage 5.6%, QD score 1.551, unique ancestors 1
- Island 2: coverage 8.3%, QD score 2.291, unique ancestors 2
- Island 3: coverage 5.6%, QD score 1.530, unique ancestors 1
- Cells newly claimed this generation: 14

## Quality

- Best scalar this generation: 0.7789
- Median scalar of newly-claimed: 0.7651

## Cost

- Budget: {'generation': 2, 'max_generations': 10, 'tokens_used_total': 3829139, 'max_tokens': 20000000, 'elapsed_s_total': 11900.1, 'generation_wall_s': 4052.0}
- Candidates proposed: 32
- Parsed: 32 (100.0%)
- Admissible: 32 (100.0%)
- Scored: 32

## Content — newly claimed elites

### Island 0, cell (4, 5), scalar 0.7515

parent `c5d4fc199ac99e4a` -> candidate `d18cbe388a5e6163`

```diff
--- parent c5d4fc199ac99e4a
+++ candidate d18cbe388a5e6163
@@ -1,48 +1,53 @@
-Read the team’s raw evidence notes and draft a Capability Case for removing per‑action human approval on the given operational‑change gateway action. **Every rule below is compulsory; violating any rule requires a “Do not proceed” recommendation.**
+Read the team’s raw evidence notes and draft a Capability Case for removing per‑action human approval on the specified operational‑change gateway action. **All rules below are mandatory; any violation must lead to a “Do not proceed” recommendation.**
 
 ### Step 1 – Evidence inventory  
-For each of the four required evidence dimensions record **Present** or **Absent**. If present, include the exact quotation (or a verbatim paraphrase) from the notes; do not create or alter content.
+For each of the four required evidence dimensions record **Present** or **Absent**.  
+If **Present**, copy the exact wording from the notes (enclose in quotation marks). Do not paraphrase, edit, or fabricate any text.
 
-- **Test results** – _________  
-- **Failure‑mode analysis** – _________  
-- **Audit findings** – _________  
-- **Comparison to the human‑approved baseline** – _________  
+- **Test results** – _____ (excerpt: “…”)
+- **Failure‑mode analysis** – _____ (excerpt: “…”)
+- **Audit findings** – _____ (excerpt: “…”)
+- **Comparison to the human‑approved baseline** – _____ (excerpt: “…”)
 
-### Step 2 – Disqualifier determination (must be done before any case text)  
-A disqualifier exists if **any** of the following conditions is true. Cite the exact wording from the notes for each applicable condition.
+*Note: a dimension marked **Absent** is a disqualifier (see Step 2). Thin or limited evidence is **not** a disqualifier.*
 
-1. The evaluation runs **only as a nightly batch** rather than before each action (p. 29).  
-2. Governance for the relaxation is **undefined or postponed** (e.g., “we will govern it later”) (p. 29).  
-3. The proposal relies on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
-4. **Any** of the four evidence dimensions is marked **Absent** (p. 25).
+### Step 2 – Disqualifier identification (must be completed before writing any case text)  
+A disqualifier exists if **any** of the following conditions is true. For each applicable condition quote the exact note that triggers it.
+
+1. **Evaluation timing** – the evaluation runs **only as a nightly batch** instead of before each action (p. 29).  
+2. **Governance undefined** – governance for the relaxation is **not defined or is postponed** (e.g., “we will govern it later”) (p. 29).  
+3. **Reliance on agent knowledge** – the proposal depends on the **agent’s internal knowledge** of when to stop rather than an **independent architectural safeguard** (p. 28).  
+4. **Missing evidence dimension** – any of the four evidence dimensions is marked **Absent** (p. 25).
 
 ### Step 3 – Output  
 
-#### If one or more disqualifiers are found  
-Produce exactly the following block (no additional headings or prose):
+#### A. If one or more disqualifiers are found  
+Produce **exactly** the block below (no extra headings, prose, or whitespace):
 
 ```
 Disqualifiers:
-- <list each applicable disqualifier, quoting the note>
+- <Condition name>: <quoted note that triggers it>
+- <Condition name>: <quoted note that triggers it>
+…
 Recommendation: Do not proceed
 ```
 
-#### If no disqualifiers are found  
-Generate the Capability Case using the exact headings and order below:
+List each applicable disqualifier on its own line, using the condition name defined in Step 2.
+
+#### B. If no disqualifiers are found  
+Generate the Capability Case using the headings and order shown **without alteration**:
 
 1. **Proposed Relaxation**  
    - One concise sentence stating the request to remove per‑action human approval.
 
 2. **Evidence Summary**  
-   - For each dimension marked **Present**, list the quoted key point(s) extracted in Step 1.
+   - For every dimension marked **Present**, list the quoted excerpt captured in Step 1.
 
 3. **Disqualifier Evaluation**  
-   - Write: `No disqualifier identified.`
+   - Write exactly: `No disqualifier identified.`
 
 4. **Recommendation**  
-   - Write: `Recommendation: Proceed.`
+   - Write exactly: `Recommendation: Proceed.`
 
 ### Step 4 – Compliance reminder  
-All statements must be truthful, complete, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not exaggerate, omit, or fabricate any information. Maintain a factual, concise, and persuasive tone.
-
-Follow the structure precisely; any deviation triggers a “Do not proceed” outcome.+All statements must be truthful, complete, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not exaggerate, omit, or fabricate any information. Use a factual, concise, and persuasive tone. Any deviation from these instructions results in a “Do not proceed” outcome.
```

### Island 0, cell (4, 5), scalar 0.7522

parent `89189d7899786eac` -> candidate `570a62a035b212ae`

```diff
--- parent 89189d7899786eac
+++ candidate 570a62a035b212ae
@@ -1,25 +1,31 @@
-Read the team’s raw evidence notes and produce a Capability Case for removing per‑action human approval on the specified operational‑change gateway action. **All rules below are mandatory; any breach forces a “Do not proceed” recommendation.**
+Read the team’s raw evidence notes and create a Capability Case for removing per‑action human approval on the specified operational‑change gateway action. **All rules are mandatory; any violation forces a “Do not proceed” recommendation.**
 
-### 1. Inventory the evidence  
-For each required dimension indicate **Present** or **Absent**.  
-If present, copy the exact wording (or a verbatim excerpt) from the notes; do not modify or paraphrase.
+### 1. Evidence inventory  
+For each of the four required dimensions record **Present** or **Absent**. If present, copy the exact wording (verbatim excerpt) from the notes; do not edit, paraphrase, or add commentary.
 
-- **Test results** – _______ (excerpt: “…”)  
-- **Failure‑mode analysis** – _______ (excerpt: “…”)  
-- **Audit findings** – _______ (excerpt: “…”)  
-- **Comparison to the human‑approved baseline** – _______ (excerpt: “…”)  
+- **Test results** – Present / Absent  
+  *Excerpt (if present):* “...”  
 
-*If any dimension is **Absent**, it is a disqualifier (see step 2). Thin or limited evidence is **not** a disqualifier.*
+- **Failure‑mode analysis** – Present / Absent  
+  *Excerpt (if present):* “...”  
 
-### 2. Identify disqualifiers (must be decided before writing any case text)  
-A disqualifier exists when **any** of the following statements appears in the notes. Quote the exact text for each that applies.
+- **Audit findings** – Present / Absent  
+  *Excerpt (if present):* “...”  
 
-1. Evaluation runs **only as a nightly batch** instead of before each action (p. 29).  
-2. Governance for the relaxation is **undefined, pending, or “we will govern it later”** (p. 29).  
-3. The proposal relies on the **agent’s internal knowledge** of when to stop rather than an **independent architectural safeguard** (p. 28).  
-4. Any evidence dimension listed in step 1 is marked **Absent** (p. 25).  
+- **Comparison to the human‑approved baseline** – Present / Absent  
+  *Excerpt (if present):* “...”  
 
-### 3. Output format  
+### 2. Disqualifier determination (must be completed before any case text)  
+A disqualifier exists when **any** of the following statements appears in the notes. Quote the exact note for each that applies.
+
+1. Evaluation runs **only as a nightly batch** rather than before each action (p. 29).  
+2. Governance for the relaxation is **undefined, pending, or phrased “we will govern it later”** (p. 29).  
+3. The proposal relies on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
+4. Any of the four evidence dimensions listed in Step 1 is marked **Absent** (p. 25).  
+
+If any disqualifier is found, go directly to the output format in Section 3‑A; do **not** write a Capability Case.
+
+### 3. Output  
 
 #### A. One or more disqualifiers found  
 Produce **exactly** the block below (no extra headings, prose, or whitespace):
@@ -35,13 +41,13 @@
 List each applicable disqualifier on its own line, using the quoted note text.
 
 #### B. No disqualifiers found  
-Generate the Capability Case in the following order, using the headings shown **without alteration**:
+Generate the Capability Case using the headings and order shown **without any alteration**:
 
 1. **Proposed Relaxation**  
    - One concise sentence stating the request to remove per‑action human approval.
 
 2. **Evidence Summary**  
-   - For every dimension marked **Present**, list the excerpt captured in step 1.
+   - For every dimension marked **Present**, list the exact excerpt captured in Step 1.
 
 3. **Disqualifier Evaluation**  
    - Write exactly: `No disqualifier identified.`
@@ -50,4 +56,4 @@
    - Write exactly: `Recommendation: Proceed.`
 
 ### 4. Compliance reminder  
-All statements must be truthful, complete, and fully aligned with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not fabricate, omit, or exaggerate any information from the notes. Maintain a factual, concise, and persuasive tone. Any deviation from these instructions results in a “Do not proceed” outcome.+All statements must be truthful, complete, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not fabricate, omit, or exaggerate any information from the notes. Keep the tone factual, concise, and persuasive. Any deviation from these instructions results in a “Do not proceed” outcome.
```

### Island 0, cell (3, 5), scalar 0.7753

parent `c5d4fc199ac99e4a` -> candidate `4f8fb0ad875b5ce7`

```diff
--- parent c5d4fc199ac99e4a
+++ candidate 4f8fb0ad875b5ce7
@@ -1,48 +1,56 @@
-Read the team’s raw evidence notes and draft a Capability Case for removing per‑action human approval on the given operational‑change gateway action. **Every rule below is compulsory; violating any rule requires a “Do not proceed” recommendation.**
+Read the team’s raw evidence notes and produce a Capability Case for the requested removal of per‑action human approval on the specified operational‑change gateway action. **All rules below are mandatory; any violation forces a “Do not proceed” recommendation.**
 
-### Step 1 – Evidence inventory  
-For each of the four required evidence dimensions record **Present** or **Absent**. If present, include the exact quotation (or a verbatim paraphrase) from the notes; do not create or alter content.
+### 1. Evidence inventory  
+Create a four‑row table. For each dimension write **Present** or **Absent**. If present, copy the exact wording (or a verbatim excerpt) from the notes; do not edit or paraphrase.
 
-- **Test results** – _________  
-- **Failure‑mode analysis** – _________  
-- **Audit findings** – _________  
-- **Comparison to the human‑approved baseline** – _________  
+| Dimension | Status | Quote / excerpt |
+|-----------|--------|-----------------|
+| Test results |  |  |
+| Failure‑mode analysis |  |  |
+| Audit findings |  |  |
+| Comparison to the human‑approved baseline |  |  |
 
-### Step 2 – Disqualifier determination (must be done before any case text)  
-A disqualifier exists if **any** of the following conditions is true. Cite the exact wording from the notes for each applicable condition.
+*Note: an evidence dimension that is merely thin or limited is **not** a disqualifier; only a full “Absent” matters.*
 
-1. The evaluation runs **only as a nightly batch** rather than before each action (p. 29).  
-2. Governance for the relaxation is **undefined or postponed** (e.g., “we will govern it later”) (p. 29).  
-3. The proposal relies on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
-4. **Any** of the four evidence dimensions is marked **Absent** (p. 25).
+### 2. Disqualifier detection (must be completed before any case text)  
+A disqualifier exists if **any** of the following statements appears in the notes. Record the exact quoted text for each that applies.
 
-### Step 3 – Output  
+1. The evaluation is performed **only as a nightly batch** rather than before each action (p. 29).  
+2. Governance for the relaxation is **not defined or postponed** (e.g., “we will govern it later”) (p. 29).  
+3. The proposal depends on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
+4. Any of the four evidence dimensions in the table is marked **Absent** (p. 25).  
 
-#### If one or more disqualifiers are found  
-Produce exactly the following block (no additional headings or prose):
+If a disqualifier is found, stop here and go to the output block for disqualifiers.
+
+### 3. Output  
+
+#### A. One or more disqualifiers detected  
+Print **exactly** the following (no extra headings, prose, or blank lines):
 
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
+#### B. No disqualifiers detected  
+Compose the Capability Case using the headings and order below, without alteration:
 
 1. **Proposed Relaxation**  
-   - One concise sentence stating the request to remove per‑action human approval.
+   - One brief sentence stating the request to remove per‑action human approval.
 
 2. **Evidence Summary**  
-   - For each dimension marked **Present**, list the quoted key point(s) extracted in Step 1.
+   - For every dimension marked **Present**, list the excerpt captured in the table.
 
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
+All content must be truthful, complete, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not fabricate, omit, or exaggerate any information from the notes. Keep the tone factual, concise, and persuasive. Any deviation from these instructions results in a “Do not proceed” outcome.
```

### Island 1, cell (4, 5), scalar 0.7535

parent `960ea712010643d4` -> candidate `98f3b5f6a6255447`

```diff
--- parent 960ea712010643d4
+++ candidate 98f3b5f6a6255447
@@ -1,59 +1,50 @@
-Read the raw evidence notes provided by the team and produce a Capability Case that evaluates whether per‑action human approval can be relaxed for the specified operational‑change gateway action. **Every rule below is mandatory; any breach automatically forces a “Do not proceed” recommendation.**
+Read the raw evidence notes supplied by the team and draft a Capability Case that decides whether per‑action human approval may be relaxed for the named operational‑change gateway action. **All rules below are compulsory; any violation forces a “Recommendation: Do not proceed”.**
 
----
+### 1. Evidence Checklist  
+Construct a 4‑row table – one row for each required evidence dimension. Fill the *Status* column with **Present** or **Absent**. If the status is **Present**, copy the exact wording (verbatim) from the notes into the *Excerpt* column; do **not** paraphrase or add commentary.
 
-### Step 1 – Evidence inventory  
-Create a four‑row table (one row per required dimension). For each row write **Present** or **Absent**. If the dimension is present, copy **the exact wording** from the notes – no paraphrase, no additions.
+| Dimension                               | Status   | Excerpt (if Present) |
+|----------------------------------------|----------|----------------------|
+| Test results                           |          |                      |
+| Failure‑mode analysis                  |          |                      |
+| Audit findings                         |          |                      |
+| Comparison to the human‑approved baseline |          |                      |
 
-| Dimension | Status | Quote (if Present) |
-|-----------|--------|--------------------|
-| Test results |  |  |
-| Failure‑mode analysis |  |  |
-| Audit findings |  |  |
-| Comparison to the human‑approved baseline |  |  |
+### 2. Disqualifier Scan (must be completed **before** any case narrative)  
+Identify every disqualifier that applies. For each, list the verbatim note that triggers it.
 
----
+* Disqualifier 1 – Evaluation runs **only as a nightly batch** (not before each action) – p. 29.  
+* Disqualifier 2 – Governance for the relaxation is **undefined or deferred** (e.g., “we will govern it later”) – p. 29.  
+* Disqualifier 3 – The proposal depends on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** – p. 28.  
+* Disqualifier 4 – **Any** of the four evidence dimensions is **Absent** – p. 25.
 
-### Step 2 – Disqualifier detection (must be completed **before** any case text)  
-A disqualifier exists if **any** of the following conditions is met. List each applicable disqualifier with the verbatim excerpt that triggers it.
+*Only a completely missing dimension counts as a disqualifier; a thin but present item does not.*
 
-1. The evaluation is performed **only as a nightly batch** rather than before each action (p. 29).  
-2. Governance for the relaxation is **not defined or is deferred** (e.g., “we will govern it later”) (p. 29).  
-3. The proposal relies on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
-4. **Any** of the four evidence dimensions is **Absent** (p. 25).  
+### 3. Output Format  
 
-*Note:* A dimension that is present but thin (short test result, brief audit note, etc.) is **not** a disqualifier; it is simply noted as present.
-
----
-
-### Step 3 – Output specification  
-
-**If one or more disqualifiers were identified** produce **exactly** the following structure (no extra headings or prose):
+**If one or more disqualifiers are found**, output **exactly** the following structure (no extra headings, no prose):
 
 ```
 Disqualifiers:
-- "<verbatim quote 1>"
-- "<verbatim quote 2>"
+- "<verbatim excerpt 1>"
+- "<verbatim excerpt 2>"
 …
 Recommendation: Do not proceed
 ```
 
-**If no disqualifiers are found** produce the Capability Case in the order below, using the headings exactly as shown and nothing else.
+**If no disqualifiers are found**, produce the Capability Case using the headings and order below, and nothing else.
 
 1. **Proposed Relaxation**  
    - One sentence stating the request to remove per‑action human approval.
 
 2. **Evidence Summary**  
-   - For each dimension marked **Present**, list the quoted snippet(s) that best support the relaxation.  
-   - For each dimension marked **Absent**, list the label “Absent”.
+   - For each dimension, copy the *Excerpt* from the table if the status is **Present**; otherwise write **Absent**.
 
 3. **Disqualifier Evaluation**  
-   - Write: `No disqualifier identified.`
+   - Write exactly: `No disqualifier identified.`
 
 4. **Recommendation**  
-   - Write: `Recommendation: Proceed.`
+   - Write exactly: `Recommendation: Proceed.`
 
----
-
-### Step 4 – Compliance reminder  
-All statements must be **truthful, complete, and fully aligned** with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not fabricate, omit, or exaggerate any information. Keep the tone factual, concise, and persuasive. Any deviation from the prescribed structure or any rule violation triggers a “Do not proceed” outcome.  +### 4. Compliance Reminder  
+All statements must be **truthful, complete, and fully consistent** with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not fabricate, omit, or exaggerate any information. Maintain a factual, concise, and persuasive tone. Any deviation from the specified structure or any rule breach automatically results in a “Recommendation: Do not proceed”.
```

### Island 1, cell (4, 5), scalar 0.7721

parent `960ea712010643d4` -> candidate `063cf7124dabfc32`

```diff
--- parent 960ea712010643d4
+++ candidate 063cf7124dabfc32
@@ -1,9 +1,9 @@
-Read the raw evidence notes provided by the team and produce a Capability Case that evaluates whether per‑action human approval can be relaxed for the specified operational‑change gateway action. **Every rule below is mandatory; any breach automatically forces a “Do not proceed” recommendation.**
+**Task** – From the team’s raw evidence notes, create a Capability Case that decides whether per‑action human approval may be relaxed for the given operational‑change gateway action. Every rule below is compulsory; any violation forces a “Recommendation: Do not proceed”.
 
 ---
 
-### Step 1 – Evidence inventory  
-Create a four‑row table (one row per required dimension). For each row write **Present** or **Absent**. If the dimension is present, copy **the exact wording** from the notes – no paraphrase, no additions.
+### 1. Evidence inventory  
+Build a 4‑row table, one row for each required dimension. Fill **Status** with **Present** or **Absent**. If **Present**, copy the exact wording (or a verbatim fragment) from the notes into **Quote** – no paraphrasing, no additions.
 
 | Dimension | Status | Quote (if Present) |
 |-----------|--------|--------------------|
@@ -14,46 +14,49 @@
 
 ---
 
-### Step 2 – Disqualifier detection (must be completed **before** any case text)  
-A disqualifier exists if **any** of the following conditions is met. List each applicable disqualifier with the verbatim excerpt that triggers it.
+### 2. Disqualifier scan (must be completed **before** any case text)  
+A disqualifier exists if **any** of the following is true. List each applicable item with the verbatim excerpt that triggers it.
 
-1. The evaluation is performed **only as a nightly batch** rather than before each action (p. 29).  
-2. Governance for the relaxation is **not defined or is deferred** (e.g., “we will govern it later”) (p. 29).  
-3. The proposal relies on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
-4. **Any** of the four evidence dimensions is **Absent** (p. 25).  
+1. Evaluation is performed **only as a nightly batch** (not before each action).  
+2. Governance for the relaxation is **undefined or deferred** (e.g., “we will govern it later”).  
+3. The proposal depends on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard**.  
+4. **Any** of the four evidence dimensions is **Absent**.
 
-*Note:* A dimension that is present but thin (short test result, brief audit note, etc.) is **not** a disqualifier; it is simply noted as present.
+*Thin but present evidence does **not** count as a disqualifier; only a completely missing dimension does.*
 
 ---
 
-### Step 3 – Output specification  
+### 3. Output format  
 
-**If one or more disqualifiers were identified** produce **exactly** the following structure (no extra headings or prose):
+#### • If one or more disqualifiers were found  
+Produce **exactly** the following structure (no extra headings or prose):
 
 ```
 Disqualifiers:
-- "<verbatim quote 1>"
-- "<verbatim quote 2>"
+- "<verbatim excerpt 1>"
+- "<verbatim excerpt 2>"
 …
 Recommendation: Do not proceed
 ```
 
-**If no disqualifiers are found** produce the Capability Case in the order below, using the headings exactly as shown and nothing else.
+#### • If **no** disqualifiers were found  
+Generate the Capability Case with the headings and order shown below, and nothing else.
 
 1. **Proposed Relaxation**  
-   - One sentence stating the request to remove per‑action human approval.
+   - One concise sentence stating the request to remove per‑action human approval.
 
 2. **Evidence Summary**  
-   - For each dimension marked **Present**, list the quoted snippet(s) that best support the relaxation.  
-   - For each dimension marked **Absent**, list the label “Absent”.
+   - For each dimension:  
+     *If Present*: list the copied quote.  
+     *If Absent*: write “Absent”.
 
 3. **Disqualifier Evaluation**  
-   - Write: `No disqualifier identified.`
+   - Write exactly: `No disqualifier identified.`
 
 4. **Recommendation**  
-   - Write: `Recommendation: Proceed.`
+   - Write exactly: `Recommendation: Proceed.`
 
 ---
 
-### Step 4 – Compliance reminder  
-All statements must be **truthful, complete, and fully aligned** with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not fabricate, omit, or exaggerate any information. Keep the tone factual, concise, and persuasive. Any deviation from the prescribed structure or any rule violation triggers a “Do not proceed” outcome.  +### 4. Compliance reminder  
+All statements must be **truthful, complete, and fully consistent** with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not fabricate, omit, or exaggerate any information. Maintain a factual, concise, and persuasive tone. Any deviation from the prescribed structure or any rule breach automatically results in a “Recommendation: Do not proceed”.
```

### Island 1, cell (3, 5), scalar 0.7628

parent `960ea712010643d4` -> candidate `b5fed1006998ced1`

```diff
--- parent 960ea712010643d4
+++ candidate b5fed1006998ced1
@@ -1,59 +1,63 @@
-Read the raw evidence notes provided by the team and produce a Capability Case that evaluates whether per‑action human approval can be relaxed for the specified operational‑change gateway action. **Every rule below is mandatory; any breach automatically forces a “Do not proceed” recommendation.**
+You are given the team’s raw evidence notes. From them build a Capability Case that decides whether the per‑action human‑approval requirement for the named operational‑change gateway action can be relaxed. **Every rule below is compulsory; violating any rule forces a “Recommendation: Do not proceed”.**
 
 ---
 
-### Step 1 – Evidence inventory  
-Create a four‑row table (one row per required dimension). For each row write **Present** or **Absent**. If the dimension is present, copy **the exact wording** from the notes – no paraphrase, no additions.
+### 1. Evidence matrix
+Construct a 4‑row table, one row for each required evidence dimension. Fill the **Status** column with **Present** or **Absent**. If the status is **Present**, copy **exactly** the wording from the notes that best supports the case (no paraphrase, no additions).
 
-| Dimension | Status | Quote (if Present) |
-|-----------|--------|--------------------|
-| Test results |  |  |
-| Failure‑mode analysis |  |  |
-| Audit findings |  |  |
-| Comparison to the human‑approved baseline |  |  |
+| Dimension                               | Status   | Exact excerpt (if Present) |
+|----------------------------------------|----------|-----------------------------|
+| Test results                           |          |                             |
+| Failure‑mode analysis                  |          |                             |
+| Audit findings                         |          |                             |
+| Comparison to the human‑approved baseline |          |                             |
 
 ---
 
-### Step 2 – Disqualifier detection (must be completed **before** any case text)  
-A disqualifier exists if **any** of the following conditions is met. List each applicable disqualifier with the verbatim excerpt that triggers it.
+### 2. Disqualifier scan (must be performed **before** writing any case text)
+A disqualifier exists if **any** of the following is true. For each applicable disqualifier list the verbatim note that triggers it.
 
-1. The evaluation is performed **only as a nightly batch** rather than before each action (p. 29).  
-2. Governance for the relaxation is **not defined or is deferred** (e.g., “we will govern it later”) (p. 29).  
-3. The proposal relies on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
-4. **Any** of the four evidence dimensions is **Absent** (p. 25).  
+1. The evaluation is run **only as a nightly batch** instead of before each action (p. 29).  
+2. Governance for the relaxation is **undefined or deferred** (e.g., “we will govern it later”) (p. 29).  
+3. The proposal relies on the **agent’s internal knowledge** of when to stop rather than an **independent architectural safeguard** (p. 28).  
+4. **Any** of the four evidence dimensions is **Absent** (p. 25).
 
-*Note:* A dimension that is present but thin (short test result, brief audit note, etc.) is **not** a disqualifier; it is simply noted as present.
+*Thin* evidence (short test result, brief audit comment, etc.) is **not** a disqualifier; it is simply recorded as **Present**.
 
 ---
 
-### Step 3 – Output specification  
+### 3. Output format
 
-**If one or more disqualifiers were identified** produce **exactly** the following structure (no extra headings or prose):
+#### A. If one or more disqualifiers were found  
+Output **exactly** the following structure (no extra headings or prose):
 
 ```
 Disqualifiers:
-- "<verbatim quote 1>"
-- "<verbatim quote 2>"
-…
+- "<verbatim excerpt 1>"
+- "<verbatim excerpt 2>"
+...
 Recommendation: Do not proceed
 ```
 
-**If no disqualifiers are found** produce the Capability Case in the order below, using the headings exactly as shown and nothing else.
+#### B. If **no** disqualifiers were found  
+Produce the Capability Case with the headings in this exact order and wording:
 
 1. **Proposed Relaxation**  
    - One sentence stating the request to remove per‑action human approval.
 
 2. **Evidence Summary**  
-   - For each dimension marked **Present**, list the quoted snippet(s) that best support the relaxation.  
-   - For each dimension marked **Absent**, list the label “Absent”.
+   - For each dimension, list the status from the matrix.  
+   - If **Present**, include the quoted excerpt; if **Absent**, write “Absent”.
 
 3. **Disqualifier Evaluation**  
-   - Write: `No disqualifier identified.`
+   - Write exactly: `No disqualifier identified.`
 
 4. **Recommendation**  
-   - Write: `Recommendation: Proceed.`
+   - Write exactly: `Recommendation: Proceed.`
+
+No additional sections, bullet points, or free‑form text are allowed.
 
 ---
 
-### Step 4 – Compliance reminder  
-All statements must be **truthful, complete, and fully aligned** with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not fabricate, omit, or exaggerate any information. Keep the tone factual, concise, and persuasive. Any deviation from the prescribed structure or any rule violation triggers a “Do not proceed” outcome.  +### 4. Compliance reminder
+All statements must be **truthful, complete, and fully consistent** with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not fabricate, omit, or exaggerate any information from the notes. Maintain a factual, concise, and persuasive tone. Any deviation from the prescribed structure or any rule breach automatically results in a “Recommendation: Do not proceed”.  
```

### Island 1, cell (3, 5), scalar 0.7789

parent `960ea712010643d4` -> candidate `f4a6918783d766bb`

```diff
--- parent 960ea712010643d4
+++ candidate f4a6918783d766bb
@@ -1,59 +1,54 @@
-Read the raw evidence notes provided by the team and produce a Capability Case that evaluates whether per‑action human approval can be relaxed for the specified operational‑change gateway action. **Every rule below is mandatory; any breach automatically forces a “Do not proceed” recommendation.**
+**Instructions for generating a Capability Case**
 
----
-
-### Step 1 – Evidence inventory  
-Create a four‑row table (one row per required dimension). For each row write **Present** or **Absent**. If the dimension is present, copy **the exact wording** from the notes – no paraphrase, no additions.
+**1. Evidence inventory**  
+Create a table with one row for each required dimension:
 
 | Dimension | Status | Quote (if Present) |
 |-----------|--------|--------------------|
-| Test results |  |  |
-| Failure‑mode analysis |  |  |
-| Audit findings |  |  |
-| Comparison to the human‑approved baseline |  |  |
+| Test results | Present / Absent |  |
+| Failure‑mode analysis | Present / Absent |  |
+| Audit findings | Present / Absent |  |
+| Comparison with the human‑approved baseline | Present / Absent |  |
 
----
+- Write **Present** or **Absent** for every dimension.  
+- If a dimension is Present, copy **exactly** the snippet from the raw notes that best supports it (no paraphrasing, no additions).  
+- Leave the Quote cell empty when the dimension is Absent.
 
-### Step 2 – Disqualifier detection (must be completed **before** any case text)  
-A disqualifier exists if **any** of the following conditions is met. List each applicable disqualifier with the verbatim excerpt that triggers it.
+**2. Disqualifier scan (must be done before any case text)**  
+A disqualifier exists if *any* of the following appears in the notes; list each trigger with the verbatim excerpt.
 
-1. The evaluation is performed **only as a nightly batch** rather than before each action (p. 29).  
-2. Governance for the relaxation is **not defined or is deferred** (e.g., “we will govern it later”) (p. 29).  
-3. The proposal relies on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
-4. **Any** of the four evidence dimensions is **Absent** (p. 25).  
+- Evaluation is performed **only as a nightly batch** rather than before each action (p. 29).  
+- Governance for the relaxation is **undefined or postponed** (e.g., “we will govern it later”) (p. 29).  
+- The proposal relies on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
+- **Any** of the four evidence dimensions is **Absent** (p. 25).
 
-*Note:* A dimension that is present but thin (short test result, brief audit note, etc.) is **not** a disqualifier; it is simply noted as present.
+*Note:* A dimension that is present but brief (“thin”) is still **Present** and does **not** count as a disqualifier.
 
----
+**3. Output format**
 
-### Step 3 – Output specification  
-
-**If one or more disqualifiers were identified** produce **exactly** the following structure (no extra headings or prose):
+*If one or more disqualifiers were found* output **exactly** the following (no extra headings or prose):
 
 ```
 Disqualifiers:
-- "<verbatim quote 1>"
-- "<verbatim quote 2>"
+- "<verbatim quote>"
+- "<verbatim quote>"
 …
 Recommendation: Do not proceed
 ```
 
-**If no disqualifiers are found** produce the Capability Case in the order below, using the headings exactly as shown and nothing else.
+*If no disqualifiers were found* produce the Capability Case using the headings below, in this order, and nothing else:
 
-1. **Proposed Relaxation**  
-   - One sentence stating the request to remove per‑action human approval.
+**Proposed Relaxation**  
+- One concise sentence stating the request to remove per‑action human approval.
 
-2. **Evidence Summary**  
-   - For each dimension marked **Present**, list the quoted snippet(s) that best support the relaxation.  
-   - For each dimension marked **Absent**, list the label “Absent”.
+**Evidence Summary**  
+- For each dimension, write “Present” followed by the quoted snippet, or write “Absent”.
 
-3. **Disqualifier Evaluation**  
-   - Write: `No disqualifier identified.`
+**Disqualifier Evaluation**  
+- Write exactly: `No disqualifier identified.`
 
-4. **Recommendation**  
-   - Write: `Recommendation: Proceed.`
+**Recommendation**  
+- Write exactly: `Recommendation: Proceed.`
 
----
-
-### Step 4 – Compliance reminder  
-All statements must be **truthful, complete, and fully aligned** with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not fabricate, omit, or exaggerate any information. Keep the tone factual, concise, and persuasive. Any deviation from the prescribed structure or any rule violation triggers a “Do not proceed” outcome.  +**4. Compliance reminder**  
+All statements must be truthful, complete, and fully aligned with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not fabricate, omit, or exaggerate any information. Any violation of the rules or deviation from the prescribed structure triggers an automatic “Do not proceed” outcome.
```

### Island 2, cell (4, 5), scalar 0.7598

parent `1d0cb7b23d085d40` -> candidate `7deedd682c3e5565`

```diff
--- parent 1d0cb7b23d085d40
+++ candidate 7deedd682c3e5565
@@ -1,38 +1,38 @@
-Read the team's raw evidence notes and produce a Capability Case for relaxing per‑action human approval on the specified operational‑change gateway action. Every rule below is mandatory; any violation must lead to a “Do not proceed” recommendation, but the full case must still be output.
+Read the team’s raw evidence notes and construct a Capability Case for relaxing per‑action human approval on the indicated operational‑change gateway action. Every rule below is mandatory; any violation must still result in a full case that ends with **Recommendation: Do not proceed**.
 
 ### 1. Evidence inventory  
-For each of the four required evidence dimensions, indicate **Present** or **Absent** and provide the exact wording (quote) or a faithful paraphrase from the notes. Do not create any content that is not in the notes.
+For each of the four required evidence dimensions, record **Present** or **Absent** and, if present, copy the exact wording (verbatim quote) from the notes. Do **not** paraphrase or invent any text.
 
-- **Test results** – ______________________  
-- **Failure‑mode analysis** – ______________________  
-- **Audit findings** – ______________________  
-- **Comparison to the human‑approved baseline** – ______________________  
+- **Test results** – Present / Absent – “<exact note>”  
+- **Failure‑mode analysis** – Present / Absent – “<exact note>”  
+- **Audit findings** – Present / Absent – “<exact note>”  
+- **Comparison to the human‑approved baseline** – Present / Absent – “<exact note>”
 
-### 2. Disqualifier detection (perform before drafting the case)  
-A disqualifier exists if **any** of the following conditions is met. Cite the exact phrase from the notes that triggers each condition.
+### 2. Disqualifier detection (perform before writing the case)  
+A disqualifier exists if **any** of the following is true. For each that applies, cite the exact phrase from the notes that triggers it.
 
-1. The evaluation runs **only as a nightly batch** rather than before each action (p. 29).  
-2. Governance for the relaxation is **undefined or deferred** (e.g., “we will govern it later”) (p. 29).  
-3. The proposal relies on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
-4. **Any** of the four evidence dimensions is **Absent** (p. 25).
+1. Evaluation runs **only as a nightly batch** instead of before each action (p. 29).  
+2. Governance for the relaxation is **undefined or postponed** (e.g., “we will govern it later”) (p. 29).  
+3. The proposal relies on the **agent’s internal knowledge** of when to stop rather than an **independent architectural safeguard** (p. 28).  
+4. **Any** evidence dimension is **Absent** (p. 25).  *(When this occurs, indicate which dimension is absent.)*
 
-### 3. Capability Case (fixed structure)  
+### 3. Capability Case (use exactly these headings and order)
 
-1. **Proposed Relaxation**  
-   - One concise sentence stating the request to remove per‑action human approval.
+**Proposed Relaxation**  
+- One concise sentence stating the request to remove per‑action human approval for the specified gateway action.
 
-2. **Evidence Summary**  
-   - List each dimension in the order shown in Section 1.  
-   - For dimensions marked **Present**, include the quoted or paraphrased key point.  
-   - For dimensions marked **Absent**, state “Absent” (do not fabricate evidence).
+**Evidence Summary**  
+- List the four dimensions in the order shown in Section 1.  
+- For each **Present** item, include the verbatim quote.  
+- For each **Absent** item, write the word **Absent**.
 
-3. **Disqualifier Evaluation**  
-   - If disqualifiers were found, list each one exactly as quoted from the notes.  
-   - If none were found, write: `No disqualifier identified.`
+**Disqualifier Evaluation**  
+- If disqualifiers were found, list each quoted trigger as a separate bullet.  
+- If no disqualifiers were found, write: `No disqualifier identified.`
 
-4. **Recommendation**  
-   - If any disqualifier is listed, write: `Recommendation: Do not proceed`.  
-   - Otherwise write: `Recommendation: Proceed`.
+**Recommendation**  
+- If any disqualifier is listed, write: `Recommendation: Do not proceed`.  
+- Otherwise write: `Recommendation: Proceed`.
 
 ### 4. Compliance reminder  
-All statements must be truthful, complete, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. No exaggeration, omission, or fabrication is allowed. Follow the headings and order exactly; any deviation results in a “Do not proceed” outcome.+All statements must be truthful, complete, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. No exaggeration, omission, or fabrication is allowed. Follow the headings, wording, and order exactly; any deviation automatically triggers a “Do not proceed” outcome.
```

### Island 2, cell (4, 5), scalar 0.7644

parent `1d0cb7b23d085d40` -> candidate `9c1f2fa84fc35b58`

```diff
--- parent 1d0cb7b23d085d40
+++ candidate 9c1f2fa84fc35b58
@@ -1,38 +1,40 @@
-Read the team's raw evidence notes and produce a Capability Case for relaxing per‑action human approval on the specified operational‑change gateway action. Every rule below is mandatory; any violation must lead to a “Do not proceed” recommendation, but the full case must still be output.
+Read the raw evidence notes provided by the team and draft a Capability Case for relaxing per‑action human approval on the specified operational‑change gateway action. All rules below are mandatory; any violation must result in a **Recommendation: Do not proceed**, but the full case must still be produced.
 
 ### 1. Evidence inventory  
-For each of the four required evidence dimensions, indicate **Present** or **Absent** and provide the exact wording (quote) or a faithful paraphrase from the notes. Do not create any content that is not in the notes.
+For each of the four evidence dimensions record **Present** or **Absent**.  
+If **Present**, copy the exact phrase from the notes (verbatim quotation or an exact excerpt).  
+If **Absent**, write **Absent**. Do not add, paraphrase, or infer any content.
 
-- **Test results** – ______________________  
-- **Failure‑mode analysis** – ______________________  
-- **Audit findings** – ______________________  
-- **Comparison to the human‑approved baseline** – ______________________  
+- **Test results** – Present / Absent – “<exact note>”  
+- **Failure‑mode analysis** – Present / Absent – “<exact note>”  
+- **Audit findings** – Present / Absent – “<exact note>”  
+- **Comparison to the human‑approved baseline** – Present / Absent – “<exact note>”
 
-### 2. Disqualifier detection (perform before drafting the case)  
-A disqualifier exists if **any** of the following conditions is met. Cite the exact phrase from the notes that triggers each condition.
+### 2. Disqualifier detection (perform before writing the case)  
+A disqualifier exists if **any** of the following is true. For each that applies, cite the exact note that triggers it.
 
-1. The evaluation runs **only as a nightly batch** rather than before each action (p. 29).  
+1. The evaluation runs **only as a nightly batch** instead of before each action (p. 29).  
 2. Governance for the relaxation is **undefined or deferred** (e.g., “we will govern it later”) (p. 29).  
-3. The proposal relies on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
+3. The proposal depends on the **agent’s internal knowledge** of when to stop rather than an **independent architectural safeguard** (p. 28).  
 4. **Any** of the four evidence dimensions is **Absent** (p. 25).
 
-### 3. Capability Case (fixed structure)  
+### 3. Capability Case (use exactly these headings and order)
 
-1. **Proposed Relaxation**  
-   - One concise sentence stating the request to remove per‑action human approval.
+**Proposed Relaxation**  
+- One concise sentence stating the request to remove per‑action human approval for the indicated gateway action.
 
-2. **Evidence Summary**  
-   - List each dimension in the order shown in Section 1.  
-   - For dimensions marked **Present**, include the quoted or paraphrased key point.  
-   - For dimensions marked **Absent**, state “Absent” (do not fabricate evidence).
+**Evidence Summary**  
+- List the four dimensions in the order shown in Section 1.  
+- For each **Present** item, include the quoted note.  
+- For each **Absent** item, write **Absent**.
 
-3. **Disqualifier Evaluation**  
-   - If disqualifiers were found, list each one exactly as quoted from the notes.  
-   - If none were found, write: `No disqualifier identified.`
+**Disqualifier Evaluation**  
+- If disqualifiers were found, list each quoted note as a separate bullet.  
+- If none were found, write: `No disqualifier identified.`
 
-4. **Recommendation**  
-   - If any disqualifier is listed, write: `Recommendation: Do not proceed`.  
-   - Otherwise write: `Recommendation: Proceed`.
+**Recommendation**  
+- If any disqualifier is listed, write: `Recommendation: Do not proceed`.  
+- Otherwise write: `Recommendation: Proceed`.
 
 ### 4. Compliance reminder  
-All statements must be truthful, complete, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. No exaggeration, omission, or fabrication is allowed. Follow the headings and order exactly; any deviation results in a “Do not proceed” outcome.+All statements must be truthful, complete, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. No exaggeration, omission, or fabrication is permitted. Deviating from the headings, order, or wording above automatically triggers a “Do not proceed” outcome.
```

### Island 2, cell (5, 5), scalar 0.7541

parent `36eac2fc38809950` -> candidate `951e776cd73711ff`

```diff
--- parent 36eac2fc38809950
+++ candidate 951e776cd73711ff
@@ -1,26 +1,30 @@
-Read the team’s raw evidence notes and produce a Capability Case for removing per‑action human approval on the specified operational‑change gateway action. **All rules are absolute; any breach forces a “Do not proceed” recommendation, but the full case must still be output.**
+Read the team’s raw evidence notes and generate a **Capability Case** for the requested removal of per‑action human approval on the indicated operational‑change gateway action.  
+All requirements are non‑negotiable: if any rule is violated the case must still be produced, but the **Recommendation** line must read **“Do not proceed.”**  
 
 ### 1. Evidence inventory  
-For each required dimension record **Present** or **Absent** and, if present, copy the exact wording (quote) from the notes. Do not paraphrase or invent text.
+For each of the four mandatory evidence dimensions record whether it is **Present** or **Absent**.  
+If present, copy the passage **exactly as it appears** in the notes (include the quotation marks). Do not paraphrase, summarize, or fabricate text.
 
-- **Test results** – Present / Absent – “<exact excerpt>”  
-- **Failure‑mode analysis** – Present / Absent – “<exact excerpt>”  
-- **Audit findings** – Present / Absent – “<exact excerpt>”  
-- **Comparison to the human‑approved baseline** – Present / Absent – “<exact excerpt>”
+- **Test results** – Present / Absent – “<exact note>”  
+- **Failure‑mode analysis** – Present / Absent – “<exact note>”  
+- **Audit findings** – Present / Absent – “<exact note>”  
+- **Comparison to the human‑approved baseline** – Present / Absent – “<exact note>”
 
-### 2. Disqualifier detection (perform before writing any case prose)  
-A disqualifier exists if **any** of the following is true. Cite the exact note that triggers each condition.
+### 2. Disqualifier detection (perform before any prose)  
+A disqualifier exists if **any** of the following conditions is satisfied. For each that applies, list the **exact note** that triggers it.
 
-1. Evaluation runs **only as a nightly batch** rather than before each action (p. 29).  
-2. Governance for the relaxation is **undefined or deferred** (e.g., “we will govern it later”) (p. 29).  
-3. The proposal relies on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
-4. **Any** of the four evidence dimensions is **Absent** (p. 25).
+1. The evaluation is performed **only as a nightly batch** rather than before each action (p. 29).  
+2. Governance for the relaxation is **undefined or postponed** (e.g., “we will govern it later”) (p. 29).  
+3. The proposal depends on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
+4. Any of the four evidence dimensions is **Absent** (p. 25).  
 
-### 3. Output format (always produce the full case)  
+If none of the above apply, record “No disqualifier identified.”
+
+### 3. Required output (exact headings and order)  
 
 ```
 Proposed Relaxation
-- The request is to remove per‑action human approval for the indicated gateway action.
+- The request is to remove per‑action human approval for the specified gateway action.
 
 Evidence Summary
 - Test results: <excerpt or “Absent”>
@@ -29,11 +33,11 @@
 - Comparison to the human‑approved baseline: <excerpt or “Absent”>
 
 Disqualifier Evaluation
-- <quoted note for condition 1, if applicable>
-- <quoted note for condition 2, if applicable>
-- <quoted note for condition 3, if applicable>
-- <quoted note indicating which evidence dimension is absent, if applicable>
-- If none of the above apply, write: No disqualifier identified.
+- <quoted note for condition 1, if triggered>
+- <quoted note for condition 2, if triggered>
+- <quoted note for condition 3, if triggered>
+- <quoted note indicating which evidence dimension is absent, if triggered>
+- If no condition is triggered, write: No disqualifier identified.
 
 Recommendation
 - Recommendation: Proceed          (if no disqualifier)
@@ -41,4 +45,4 @@
 ```
 
 ### 4. Compliance reminder  
-All statements must be **truthful, complete, and fully consistent** with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not exaggerate, omit, or fabricate any information. Use a factual, concise, and persuasive tone. Deviating from the headings, order, or wording above results in a “Do not proceed” outcome.+All statements must be **truthful, complete, and fully consistent** with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. No exaggeration, omission, or invention of information is allowed. Follow the headings, wording, and order exactly; any deviation automatically results in a “Do not proceed” recommendation.  
```

### Island 2, cell (4, 5), scalar 0.7695

parent `1d0cb7b23d085d40` -> candidate `09ecbe74a1bc4b00`

```diff
--- parent 1d0cb7b23d085d40
+++ candidate 09ecbe74a1bc4b00
@@ -1,38 +1,40 @@
-Read the team's raw evidence notes and produce a Capability Case for relaxing per‑action human approval on the specified operational‑change gateway action. Every rule below is mandatory; any violation must lead to a “Do not proceed” recommendation, but the full case must still be output.
+Read the team’s raw evidence notes and write a Capability Case for relaxing per‑action human approval on the indicated operational‑change gateway action. Every rule below is absolute; any breach must result in a **“Recommendation: Do not proceed”** but the complete case must still be output.
 
 ### 1. Evidence inventory  
-For each of the four required evidence dimensions, indicate **Present** or **Absent** and provide the exact wording (quote) or a faithful paraphrase from the notes. Do not create any content that is not in the notes.
+For each of the four required evidence dimensions indicate **Present** or **Absent** and, if present, copy the exact passage (verbatim) from the notes. Do **not** create, paraphrase, or infer any wording that is not in the notes.
 
-- **Test results** – ______________________  
-- **Failure‑mode analysis** – ______________________  
-- **Audit findings** – ______________________  
-- **Comparison to the human‑approved baseline** – ______________________  
+- **Test results** – Present / Absent – “<verbatim excerpt>”  
+- **Failure‑mode analysis** – Present / Absent – “<verbatim excerpt>”  
+- **Audit findings** – Present / Absent – “<verbatim excerpt>”  
+- **Comparison to the human‑approved baseline** – Present / Absent – “<verbatim excerpt>”
 
-### 2. Disqualifier detection (perform before drafting the case)  
-A disqualifier exists if **any** of the following conditions is met. Cite the exact phrase from the notes that triggers each condition.
+### 2. Disqualifier detection (perform **before** drafting the case)  
+A disqualifier exists if **any** of the following conditions is satisfied. For each that applies, cite the exact note that triggers it.
 
-1. The evaluation runs **only as a nightly batch** rather than before each action (p. 29).  
+1. The evaluation runs **only as a nightly batch** instead of before each action (p. 29).  
 2. Governance for the relaxation is **undefined or deferred** (e.g., “we will govern it later”) (p. 29).  
-3. The proposal relies on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
+3. The proposal relies on the **agent’s internal knowledge** of when to stop rather than an **independent architectural safeguard** (p. 28).  
 4. **Any** of the four evidence dimensions is **Absent** (p. 25).
 
-### 3. Capability Case (fixed structure)  
+*Note:* Thin evidence (e.g., very short excerpts) is **not** a disqualifier; only a completely missing dimension is.
 
-1. **Proposed Relaxation**  
-   - One concise sentence stating the request to remove per‑action human approval.
+### 3. Capability Case (use **exactly** these headings and this order)
 
-2. **Evidence Summary**  
-   - List each dimension in the order shown in Section 1.  
-   - For dimensions marked **Present**, include the quoted or paraphrased key point.  
-   - For dimensions marked **Absent**, state “Absent” (do not fabricate evidence).
+**Proposed Relaxation**  
+- One concise sentence stating the request to remove per‑action human approval for the specified gateway action.
 
-3. **Disqualifier Evaluation**  
-   - If disqualifiers were found, list each one exactly as quoted from the notes.  
-   - If none were found, write: `No disqualifier identified.`
+**Evidence Summary**  
+- List the four dimensions in the order shown in Section 1.  
+- For each **Present** item, include the verbatim excerpt.  
+- For each **Absent** item, write the word **Absent** (no invented text).
 
-4. **Recommendation**  
-   - If any disqualifier is listed, write: `Recommendation: Do not proceed`.  
-   - Otherwise write: `Recommendation: Proceed`.
+**Disqualifier Evaluation**  
+- If disqualifiers were found, list each quoted note as a separate bullet.  
+- If none were found, write: `No disqualifier identified.`
+
+**Recommendation**  
+- If any disqualifier is listed, write: `Recommendation: Do not proceed`.  
+- If no disqualifier is listed, write: `Recommendation: Proceed`.
 
 ### 4. Compliance reminder  
-All statements must be truthful, complete, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. No exaggeration, omission, or fabrication is allowed. Follow the headings and order exactly; any deviation results in a “Do not proceed” outcome.+All statements must be truthful, exhaustive, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. No exaggeration, omission, or fabrication is permitted. Deviating from the headings, order, or wording above automatically triggers a “Do not proceed” outcome.
```

### Island 2, cell (4, 5), scalar 0.7778

parent `1d0cb7b23d085d40` -> candidate `b9f2aa2c6f801ebd`

```diff
--- parent 1d0cb7b23d085d40
+++ candidate b9f2aa2c6f801ebd
@@ -1,38 +1,48 @@
-Read the team's raw evidence notes and produce a Capability Case for relaxing per‑action human approval on the specified operational‑change gateway action. Every rule below is mandatory; any violation must lead to a “Do not proceed” recommendation, but the full case must still be output.
+**Task** – From the team’s raw evidence notes, produce a Capability Case for relaxing per‑action human approval on the indicated operational‑change gateway action. All rules are mandatory; any breach must still result in a full case with a “Do not proceed” recommendation.
+
+---
 
 ### 1. Evidence inventory  
-For each of the four required evidence dimensions, indicate **Present** or **Absent** and provide the exact wording (quote) or a faithful paraphrase from the notes. Do not create any content that is not in the notes.
+For each of the four required dimensions record **Present** or **Absent** and, if present, copy the exact wording (quoted) from the notes. Do not paraphrase or invent text.
 
-- **Test results** – ______________________  
-- **Failure‑mode analysis** – ______________________  
-- **Audit findings** – ______________________  
-- **Comparison to the human‑approved baseline** – ______________________  
+- **Test results** – Present / Absent – “<exact excerpt>”  
+- **Failure‑mode analysis** – Present / Absent – “<exact excerpt>”  
+- **Audit findings** – Present / Absent – “<exact excerpt>”  
+- **Comparison to the human‑approved baseline** – Present / Absent – “<exact excerpt>”
 
-### 2. Disqualifier detection (perform before drafting the case)  
-A disqualifier exists if **any** of the following conditions is met. Cite the exact phrase from the notes that triggers each condition.
+---
 
-1. The evaluation runs **only as a nightly batch** rather than before each action (p. 29).  
+### 2. Disqualifier detection (perform **before** drafting the case)  
+A disqualifier exists if **any** of the following is true. For each that applies, cite the exact phrase from the notes that triggers it.
+
+1. Evaluation runs **only as a nightly batch** instead of before each action (p. 29).  
 2. Governance for the relaxation is **undefined or deferred** (e.g., “we will govern it later”) (p. 29).  
-3. The proposal relies on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
-4. **Any** of the four evidence dimensions is **Absent** (p. 25).
+3. The proposal relies on the **agent’s internal knowledge** of when to stop rather than an **independent architectural safeguard** (p. 28).  
+4. **Any** evidence dimension is **Absent** (p. 25); indicate which one(s).
 
-### 3. Capability Case (fixed structure)  
+*Note:* Sparse or “thin” evidence is **not** a disqualifier; only a completely missing dimension is.
 
-1. **Proposed Relaxation**  
-   - One concise sentence stating the request to remove per‑action human approval.
+---
 
-2. **Evidence Summary**  
-   - List each dimension in the order shown in Section 1.  
-   - For dimensions marked **Present**, include the quoted or paraphrased key point.  
-   - For dimensions marked **Absent**, state “Absent” (do not fabricate evidence).
+### 3. Capability Case (use these headings in exactly this order)
 
-3. **Disqualifier Evaluation**  
-   - If disqualifiers were found, list each one exactly as quoted from the notes.  
-   - If none were found, write: `No disqualifier identified.`
+**Proposed Relaxation**  
+- One concise sentence stating the request to remove per‑action human approval for the specified gateway action.
 
-4. **Recommendation**  
-   - If any disqualifier is listed, write: `Recommendation: Do not proceed`.  
-   - Otherwise write: `Recommendation: Proceed`.
+**Evidence Summary**  
+- List the four dimensions in the order shown in Section 1.  
+- For each **Present** item, include the quoted excerpt.  
+- For each **Absent** item, write “Absent”.
+
+**Disqualifier Evaluation**  
+- If disqualifiers were found, list each quoted trigger as a separate bullet.  
+- If none were found, write: `No disqualifier identified.`
+
+**Recommendation**  
+- If any disqualifier is listed, write: `Recommendation: Do not proceed`.  
+- Otherwise write: `Recommendation: Proceed`.
+
+---
 
 ### 4. Compliance reminder  
-All statements must be truthful, complete, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. No exaggeration, omission, or fabrication is allowed. Follow the headings and order exactly; any deviation results in a “Do not proceed” outcome.+All statements must be **truthful, complete, and fully consistent** with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. No exaggeration, omission, or fabrication is allowed. Deviating from the headings, order, or required content automatically triggers a “Do not proceed” outcome.
```

### Island 3, cell (3, 5), scalar 0.7659

parent `92cd33ab7dd0414f` -> candidate `19996afd9b7edd36`

```diff
--- parent 92cd33ab7dd0414f
+++ candidate 19996afd9b7edd36
@@ -1,40 +1,49 @@
-You are given the team’s raw evidence notes for a request to remove per‑action human approval on a specific operational‑change gateway action. Follow these mandatory steps exactly. Any violation forces a **“Do not proceed”** recommendation.
+You have the team’s raw evidence notes for a request to drop per‑action human approval on a particular operational‑change gateway action. Follow the procedure below **exactly**; any deviation forces a **“Do not proceed”** recommendation.
 
-### Step 1 – Evidence inventory  
-For each of the four required evidence dimensions, record whether it is **Present** or **Absent**.  
-If present, copy **verbatim** the most relevant sentence or phrase (no paraphrasing, no invention).
+---
 
-- Test results – ___________  
-- Failure‑mode analysis – ___________  
-- Audit findings – ___________  
-- Comparison to the human‑approved baseline – ___________
+### 1. Evidence audit  
+For each of the four required evidence categories, indicate **Present** or **Absent**. If present, copy the **exact** sentence or phrase that best supports it (no re‑wording, no additions).
 
-### Step 2 – Disqualifier detection (must be done before any case text)  
-A disqualifier exists if **any** of the following conditions is true. Cite the exact wording from the notes for each that applies.
+- **Test results:** ___________  
+- **Failure‑mode analysis:** ___________  
+- **Audit findings:** ___________  
+- **Baseline comparison (human‑approved):** ___________  
 
-1. The evaluation runs **only as a nightly batch** instead of before each action (p. 29).  
-2. Governance for the relaxation is **undefined or deferred** (e.g., “we will govern it later”) (p. 29).  
-3. The proposal relies on the **agent’s internal knowledge** of when to stop rather than an **independent architectural safeguard** (p. 28).  
-4. Any of the four evidence dimensions is **Absent** (p. 25).
+---
 
-If one or more disqualifiers are found, **output only** the block in Step 3A. Otherwise proceed to Step 3B.
+### 2. Disqualifier check (must be completed before any case text)  
+A disqualifier exists if **any** of the following is true. For each applicable item, quote the precise wording from the notes.
 
-### Step 3 – Output  
+1. Evaluation runs **only as a nightly batch** rather than before each action (p. 29).  
+2. Governance for the relaxation is **undefined or postponed** (e.g., “we will govern it later”) (p. 29).  
+3. The proposal depends on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
+4. Any of the four evidence categories listed in Step 1 is **Absent** (p. 25).  
 
-**A. When a disqualifier is present**  
+If one or more disqualifiers are found, go directly to **Section 3A**. Otherwise continue to **Section 3B**.
+
+---
+
+### 3. Output  
+
+#### A. Disqualifier present  
+Produce **only** the block below (no extra headings or prose):
+
 ```
 Disqualifiers:
-- <exact quoted text for each applicable disqualifier>
+- <exact quoted text for each identified disqualifier>
+- …
 Recommendation: Do not proceed
 ```
 
-**B. When no disqualifier is present** (use this exact order and headings, no extra headings)
+#### B. No disqualifier identified  
+Create the capability case using the exact order and headings below:
 
 1. **Proposed Relaxation**  
-   - One concise sentence stating the request to eliminate per‑action human approval.
+   - One brief sentence stating the request to eliminate per‑action human approval.
 
 2. **Evidence Summary**  
-   - List each dimension marked **Present** and include the verbatim snippet recorded in Step 1.
+   - For every category marked **Present** in Step 1, list a bullet containing the verbatim excerpt you recorded.
 
 3. **Disqualifier Evaluation**  
    - Write exactly: `No disqualifier identified.`
@@ -42,5 +51,7 @@
 4. **Recommendation**  
    - Write exactly: `Recommendation: Proceed.`
 
-### Compliance reminder  
-All statements must be truthful, complete, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not add, omit, or fabricate any information. Keep the language factual, concise, and persuasive within those limits. Any deviation from the structure or content rules results in a “Do not proceed” outcome. +---
+
+### 4. Compliance reminder  
+All statements must be **truthful**, **complete**, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not add, omit, or fabricate any information. Keep the language factual, concise, and persuasive within those constraints. Any breach of the specified structure or content results in a “Do not proceed” outcome.  
```

### Island 3, cell (3, 5), scalar 0.7687

parent `92cd33ab7dd0414f` -> candidate `8693616c3d61adfc`

```diff
--- parent 92cd33ab7dd0414f
+++ candidate 8693616c3d61adfc
@@ -1,46 +1,60 @@
-You are given the team’s raw evidence notes for a request to remove per‑action human approval on a specific operational‑change gateway action. Follow these mandatory steps exactly. Any violation forces a **“Do not proceed”** recommendation.
+You have the team’s raw evidence notes for a request to drop per‑action human approval on a particular operational‑change gateway action. Follow the procedure below **exactly**. Any breach automatically requires a **“Do not proceed”** recommendation.
 
-### Step 1 – Evidence inventory  
-For each of the four required evidence dimensions, record whether it is **Present** or **Absent**.  
-If present, copy **verbatim** the most relevant sentence or phrase (no paraphrasing, no invention).
+---
 
-- Test results – ___________  
-- Failure‑mode analysis – ___________  
-- Audit findings – ___________  
-- Comparison to the human‑approved baseline – ___________
+### 1. Record the evidence
+For each of the four required evidence dimensions indicate **Present** or **Absent**.  
+If the dimension is present, copy the **exact** sentence or phrase that best supports it (no paraphrase, no additions).
 
-### Step 2 – Disqualifier detection (must be done before any case text)  
-A disqualifier exists if **any** of the following conditions is true. Cite the exact wording from the notes for each that applies.
+- **Test results:** ___________  
+- **Failure‑mode analysis:** ___________  
+- **Audit findings:** ___________  
+- **Baseline comparison (human‑approved):** ___________
 
-1. The evaluation runs **only as a nightly batch** instead of before each action (p. 29).  
-2. Governance for the relaxation is **undefined or deferred** (e.g., “we will govern it later”) (p. 29).  
-3. The proposal relies on the **agent’s internal knowledge** of when to stop rather than an **independent architectural safeguard** (p. 28).  
+---
+
+### 2. Identify disqualifiers (must be completed before any case text)
+
+A disqualifier exists if **any** of the following is true. Quote the exact wording from the notes for every condition that applies.
+
+1. The evaluation runs **only as a nightly batch** rather than before each action (p. 29).  
+2. Governance for the relaxation is **undefined or postponed** (e.g., “we will govern it later”) (p. 29).  
+3. The proposal relies on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
 4. Any of the four evidence dimensions is **Absent** (p. 25).
 
-If one or more disqualifiers are found, **output only** the block in Step 3A. Otherwise proceed to Step 3B.
+If one or more disqualifiers are found, **skip directly to Step 3A**. Otherwise continue to Step 3B.
 
-### Step 3 – Output  
+---
 
-**A. When a disqualifier is present**  
+### 3. Produce the required output  
+
+#### A. When a disqualifier is present  
+Output **only** the block below, with no extra headings or prose:
+
 ```
 Disqualifiers:
-- <exact quoted text for each applicable disqualifier>
+- <exact quoted text for disqualifier 1>
+- <exact quoted text for disqualifier 2>
+… (list all that apply)
 Recommendation: Do not proceed
 ```
 
-**B. When no disqualifier is present** (use this exact order and headings, no extra headings)
+#### B. When no disqualifier is present  
+Create the capability case using exactly the headings and order shown. Do not add, remove, or rename sections.
 
 1. **Proposed Relaxation**  
    - One concise sentence stating the request to eliminate per‑action human approval.
 
 2. **Evidence Summary**  
-   - List each dimension marked **Present** and include the verbatim snippet recorded in Step 1.
+   - For each dimension marked **Present** in Step 1, list a bullet containing the verbatim excerpt you recorded.
 
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
+All statements must be **truthful**, **complete**, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not fabricate, omit, or reinterpret any information from the notes. The language should be factual, concise, and persuasive within those constraints. Any deviation from the prescribed structure or content triggers a “Do not proceed” outcome. 
```


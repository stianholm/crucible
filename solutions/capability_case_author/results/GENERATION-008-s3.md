# Generation 8 — capability_case_author

## Throughput

- Peak queue depth: 32
- Sustained (median) queue depth: 32
- Prefix cache hit rate: 77.4%
- Aggregate throughput: 150.6 tok/s (599588 completion tokens / 3980.6s)

## Archive

- Island 0: coverage 5.6%, QD score 1.570, unique ancestors 1
- Island 1: coverage 5.6%, QD score 1.558, unique ancestors 1
- Island 2: coverage 8.3%, QD score 2.310, unique ancestors 2
- Island 3: coverage 8.3%, QD score 2.321, unique ancestors 2
- Cells newly claimed this generation: 2

## Quality

- Best scalar this generation: 0.7813
- Median scalar of newly-claimed: 0.7803

## Cost

- Budget: {'generation': 8, 'max_generations': 10, 'tokens_used_total': 11626728, 'max_tokens': 20000000, 'elapsed_s_total': 35918.0, 'generation_wall_s': 3980.6}
- Candidates proposed: 32
- Parsed: 32 (100.0%)
- Admissible: 32 (100.0%)
- Scored: 32

## Content — newly claimed elites

### Island 0, cell (4, 5), scalar 0.7813

parent `448c399b7ad91f89` -> candidate `f73431a98409d3cd`

```diff
--- parent 448c399b7ad91f89
+++ candidate f73431a98409d3cd
@@ -1,21 +1,21 @@
-You have the team’s raw evidence notes for a request to drop per‑action human approval on a specific operational‑change gateway action. Follow the procedure **exactly**; any rule breach forces a **“Do not proceed”** recommendation.
+You have the team’s raw evidence notes concerning a request to drop per‑action human approval for a particular operational‑change gateway action. Follow the steps below **exactly**. Any violation of the rules forces a **“Do not proceed”** recommendation.
 
 ---
 
-### 1. Evidence inventory  
-For each of the four required dimensions record **Present** or **Absent**.  
-If **Present**, copy **the exact wording** (sentence or phrase) from the notes that best demonstrates the evidence – no paraphrasing, no additions.
+### Step 1 – Evidence inventory  
+For each of the four required evidence dimensions record **Present** or **Absent**.  
+If the dimension is **Present**, copy **the verbatim phrase or sentence** from the notes that best demonstrates it (no paraphrasing, no additions).
 
-- **Test results:** _______________________  
-- **Failure‑mode analysis:** _______________________  
-- **Audit findings:** _______________________  
-- **Baseline comparison (human‑approved):** _______________________
+- **Test results:** ________  
+- **Failure‑mode analysis:** ________  
+- **Audit findings:** ________  
+- **Baseline comparison (human‑approved):** ________
 
-*Only an **Absent** dimension creates a disqualifier. Brief mentions count as Present.*
+*Only a dimension marked **Absent** creates a disqualifier. Short mentions count as Present.*
 
 ---
 
-### 2. Disqualifier check (must be done before any case text)  
+### Step 2 – Disqualifier scan (must be completed before writing any case text)  
 A disqualifier exists if **any** of the following is true. For each that applies, quote the **exact text** from the notes.
 
 1. Evaluation runs **only as a nightly batch** rather than before each action (p. 29).  
@@ -23,14 +23,14 @@
 3. The proposal relies on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
 4. Any of the four evidence dimensions is **Absent** (p. 25).
 
-If one or more disqualifiers are found, skip to **Step 3A**; otherwise continue to **Step 3B**.
+If one or more disqualifiers are found, go to **Step 3A**; otherwise continue to **Step 3B**.
 
 ---
 
-### 3. Output  
+### Step 3 – Output  
 
-#### A. Disqualifier present  
-Output **only** the block below, with no extra headings, blank lines, or commentary:
+#### 3A – Disqualifiers present  
+Output **exactly** the block below, with no extra headings, blank lines, or commentary:
 
 ```
 Disqualifiers:
@@ -40,14 +40,14 @@
 Recommendation: Do not proceed
 ```
 
-#### B. No disqualifier  
-Produce the capability case using **exactly** the headings and order shown. Do not add, rename, or omit sections.
+#### 3B – No disqualifiers  
+Produce a capability case using **the headings and order shown**. Do not add, rename, or omit sections.
 
 1. **Proposed Relaxation**  
    - One concise sentence stating the request to eliminate per‑action human approval.
 
 2. **Evidence Summary**  
-   - For every dimension marked **Present** in Step 1, list a bullet containing the verbatim excerpt recorded.
+   - For every dimension marked **Present** in Step 1, add a bullet containing the verbatim excerpt captured.
 
 3. **Disqualifier Evaluation**  
    - Write precisely: `No disqualifier identified.`
@@ -57,5 +57,5 @@
 
 ---
 
-### 4. Compliance reminder  
-All statements must be **truthful**, **complete**, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do **not** fabricate, omit, or reinterpret any information from the notes. Any deviation from the prescribed structure or content results in a “Do not proceed” outcome. +### Step 4 – Compliance reminder  
+All statements must be **truthful, complete, and fully consistent** with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do **not** fabricate, omit, or reinterpret any information from the notes. Any deviation from the prescribed structure or content automatically results in a “Do not proceed” outcome. 
```

### Island 1, cell (3, 5), scalar 0.7794

parent `b33a2526597cd869` -> candidate `ee78ae696ad18d8a`

```diff
--- parent b33a2526597cd869
+++ candidate ee78ae696ad18d8a
@@ -1,53 +1,64 @@
 **Capability‑Case Generation Instructions**
 
-**Step 1 – Extract Evidence**  
-Create a three‑column table covering the four mandatory dimensions:
+---
 
-| Dimension | Status | Quote |
-|-----------|--------|-------|
-| Test results | Present / Absent | (verbatim snippet) |
-| Failure‑mode analysis | Present / Absent | (verbatim snippet) |
-| Audit findings | Present / Absent | (verbatim snippet) |
-| Comparison with the human‑approved baseline | Present / Absent | (verbatim snippet) |
+### 1. Assemble Evidence Table  
+Create a three‑column markdown table with one row for each required dimension.
 
-- Write **Present** if the raw notes contain any excerpt for the dimension, otherwise **Absent**.  
-- When **Present**, copy the exact wording (or the smallest exact fragment) from the notes into the *Quote* cell; do **not** paraphrase or add anything.  
-- Leave the *Quote* cell empty for **Absent** entries.  
-- A brief or “thin” excerpt still counts as **Present** and does **not** trigger a disqualifier.
+| Dimension                              | Status (Present / Absent) | Quote (verbatim) |
+|----------------------------------------|---------------------------|------------------|
+| Test results                           |                           |                  |
+| Failure‑mode analysis                  |                           |                  |
+| Audit findings                         |                           |                  |
+| Comparison with the human‑approved baseline |                           |                  |
 
-**Step 2 – Scan for Disqualifiers (must be completed before any case text)**  
-A disqualifier exists if **any** of the following conditions is met in the notes. List each triggered condition with the exact excerpt that caused it.
+* **Present** → copy the smallest exact fragment that appears in the raw notes.  
+* **Absent** → leave the Quote cell empty.  
+* A brief fragment still counts as **Present** and does **not** trigger a disqualifier.
 
-1. Evaluation is performed **only as a nightly batch** rather than before each action (p. 29).  
-2. Governance for the relaxation is **undefined or deferred** (e.g., “we will govern it later”) (p. 29).  
-3. The proposal relies on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** (p. 28).  
-4. **Any** of the four evidence dimensions is marked **Absent** (p. 25).
+---
 
-**Step 3 – Produce Output**
+### 2. Identify Disqualifiers (must be done **before** any case text)  
+Scan the notes; for every condition below that is true, add an entry to a **Disqualifiers** list containing the exact excerpt that caused the trigger.
 
-*If one or more disqualifiers were found* output **exactly** the block below (no extra headings, no prose):
+1. Evaluation runs **only as a nightly batch** (not before each action) – p. 29.  
+2. Governance for the relaxation is **undefined or deferred** (e.g., “we will govern it later”) – p. 29.  
+3. The proposal relies on the **agent’s internal knowledge** of when to stop rather than an **independent architectural safeguard** – p. 28.  
+4. Any of the four evidence dimensions is **Absent** – p. 25.  
+
+*If a dimension is Absent, use the phrase “\<Dimension> absent” as the excerpt.*
+
+---
+
+### 3. Produce Output  
+
+#### • If the Disqualifiers list is non‑empty  
+Output **exactly** the block below (no extra headings, no prose):
 
 ```
 Disqualifiers:
-- "<verbatim excerpt>"
-- "<verbatim excerpt>"
+- "<verbatim excerpt or “<Dimension> absent”>"
+- "<verbatim excerpt …>"
 …
 Recommendation: Do not proceed
 ```
 
-*If no disqualifiers were found* generate the Capability Case using **only** the headings and order shown:
+#### • If no disqualifiers were found  
+Generate the Capability Case using **only** the headings and order shown:
 
-1. **Proposed Relaxation**  
-   - One concise sentence stating the request to remove per‑action human approval.
+**Proposed Relaxation**  
+- One concise sentence stating the request to remove per‑action human approval.
 
-2. **Evidence Summary**  
-   - For each dimension, write `Present: <verbatim quote>` or `Absent`.
+**Evidence Summary**  
+- For each dimension, write `Present: <verbatim quote>` or `Absent`.
 
-3. **Disqualifier Evaluation**  
-   - Write exactly: `No disqualifier identified.`
+**Disqualifier Evaluation**  
+- Write exactly: `No disqualifier identified.`
 
-4. **Recommendation**  
-   - Write exactly: `Recommendation: Proceed.`
+**Recommendation**  
+- Write exactly: `Recommendation: Proceed.`
 
-**Step 4 – Compliance Check**  
-All statements must be truthful, complete, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not fabricate, omit, or exaggerate any information. Violating any rule or deviating from the prescribed structure automatically results in a “Recommendation: Do not proceed”.+---
+
+### 4. Compliance Check  
+All statements must be **truthful, complete, and fully consistent** with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not fabricate, omit, or extrapolate beyond the raw notes. Any breach of these rules or any deviation from the prescribed structure automatically results in a “Recommendation: Do not proceed”.
```


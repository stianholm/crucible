# Generation 9 — capability_case_author

## Throughput

- Peak queue depth: 32
- Sustained (median) queue depth: 32
- Prefix cache hit rate: 77.5%
- Aggregate throughput: 151.2 tok/s (603948 completion tokens / 3994.2s)

## Archive

- Island 0: coverage 5.6%, QD score 1.570, unique ancestors 1
- Island 1: coverage 5.6%, QD score 1.569, unique ancestors 1
- Island 2: coverage 8.3%, QD score 2.310, unique ancestors 2
- Island 3: coverage 8.3%, QD score 2.321, unique ancestors 2
- Cells newly claimed this generation: 1

## Quality

- Best scalar this generation: 0.7904
- Median scalar of newly-claimed: 0.7904

## Cost

- Budget: {'generation': 9, 'max_generations': 10, 'tokens_used_total': 12941518, 'max_tokens': 20000000, 'elapsed_s_total': 39912.2, 'generation_wall_s': 3994.2}
- Candidates proposed: 32
- Parsed: 32 (100.0%)
- Admissible: 32 (100.0%)
- Scored: 32

## Content — newly claimed elites

### Island 1, cell (3, 5), scalar 0.7904

parent `ee78ae696ad18d8a` -> candidate `a784758c41c1f274`

```diff
--- parent ee78ae696ad18d8a
+++ candidate a784758c41c1f274
@@ -2,38 +2,38 @@
 
 ---
 
-### 1. Assemble Evidence Table  
-Create a three‑column markdown table with one row for each required dimension.
+### 1. Extract Evidence  
+Create a three‑column markdown table – one row for each required dimension.
 
-| Dimension                              | Status (Present / Absent) | Quote (verbatim) |
-|----------------------------------------|---------------------------|------------------|
-| Test results                           |                           |                  |
-| Failure‑mode analysis                  |                           |                  |
-| Audit findings                         |                           |                  |
-| Comparison with the human‑approved baseline |                           |                  |
+| Dimension | Present / Absent | Quote (verbatim) |
+|-----------|------------------|------------------|
+| Test results | | |
+| Failure‑mode analysis | | |
+| Audit findings | | |
+| Comparison with the human‑approved baseline | | |
 
-* **Present** → copy the smallest exact fragment that appears in the raw notes.  
-* **Absent** → leave the Quote cell empty.  
-* A brief fragment still counts as **Present** and does **not** trigger a disqualifier.
+* **Present** – copy the smallest exact fragment from the raw notes into the *Quote* cell.  
+* **Absent** – leave the *Quote* cell empty and write **Absent** in the status column.  
+A brief fragment still counts as **Present** and does **not** trigger a disqualifier.
 
 ---
 
-### 2. Identify Disqualifiers (must be done **before** any case text)  
-Scan the notes; for every condition below that is true, add an entry to a **Disqualifiers** list containing the exact excerpt that caused the trigger.
+### 2. Identify Disqualifiers (must be completed **before** any case text)  
+For each condition below that applies, add an entry to a **Disqualifiers** list. Use the exact excerpt that caused the trigger; for a missing evidence dimension use the literal string “\<Dimension> absent”.
 
 1. Evaluation runs **only as a nightly batch** (not before each action) – p. 29.  
 2. Governance for the relaxation is **undefined or deferred** (e.g., “we will govern it later”) – p. 29.  
-3. The proposal relies on the **agent’s internal knowledge** of when to stop rather than an **independent architectural safeguard** – p. 28.  
-4. Any of the four evidence dimensions is **Absent** – p. 25.  
+3. The proposal relies on the **agent’s internal knowledge** of when to stop instead of an **independent architectural safeguard** – p. 28.  
+4. **Any** of the four evidence dimensions is **Absent** – p. 25.  
 
-*If a dimension is Absent, use the phrase “\<Dimension> absent” as the excerpt.*
+If the list contains one or more items, the case must be rejected.
 
 ---
 
 ### 3. Produce Output  
 
-#### • If the Disqualifiers list is non‑empty  
-Output **exactly** the block below (no extra headings, no prose):
+#### • When the Disqualifiers list is non‑empty  
+Output **exactly** the following block (no extra headings or prose):
 
 ```
 Disqualifiers:
@@ -43,7 +43,7 @@
 Recommendation: Do not proceed
 ```
 
-#### • If no disqualifiers were found  
+#### • When no disqualifiers are found  
 Generate the Capability Case using **only** the headings and order shown:
 
 **Proposed Relaxation**  
@@ -61,4 +61,4 @@
 ---
 
 ### 4. Compliance Check  
-All statements must be **truthful, complete, and fully consistent** with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not fabricate, omit, or extrapolate beyond the raw notes. Any breach of these rules or any deviation from the prescribed structure automatically results in a “Recommendation: Do not proceed”.+All statements must be truthful, complete, and fully consistent with **Section 8 (Strategy C)** of the ITOT‑boundary‑as‑architecture whitepaper. Do not fabricate, omit, or extrapolate beyond the raw notes. Any breach of these rules or any deviation from the prescribed structure automatically results in a “Recommendation: Do not proceed”.
```


## Held-out check (best-ever candidate)

- Candidate: `a784758c41c1f274` (rotation scalar 0.7904)
- Held-out quality: 0.9071 (passes: 0.9077, 0.9065)
- Held-out scalar: 0.7661 (passes: 0.7668, 0.7655)
- All held-out tasks valid: True

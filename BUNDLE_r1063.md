# Bundle r1063 — corpus-wide CPT / charge-conjugation / A-B coherence sweep, and the ontology map brought current

Following the r1057–r1062 core edits (charge conjugation as a geometric symmetry; the P7 synthesis
figure), this revision ran a **corpus-wide reading sweep** to catch everywhere gone stale on the new
revision — the C-conjugation results and the removal of the old A/B-as-species distinction — and brought
the ontology map coherent.

## The sweep (by reading, no grep for discovery)
Read all 11 not-yet-edited papers against a written delta-spec (`CPT_COHERENCE_SWEEP.md`, Δ1–Δ6):
- **7 LOW/MED (P1,P2,P4,P6,P10,P11,P15)** — parallel reader-agents, verified by me: **all CLEAN.**
- **4 HIGH (P8,P12,P14,P16)** — read by me at weight: **all CLEAN.**

**Result: no paper needed editing.** The corpus was already reconciled by the earlier r968 symbol-canon
(R/P/T) and r990 antimatter-naming passes. The A/B-as-species error was **not present in any paper**; the
C-conjugation work had only touched the charge-discussing papers (P13/P3/P5/P9/p0), already done at r1057–62,
and P14's charge statement is consistent.

## Where the staleness actually was: the ontology map (the glossary of record)
`ONTOLOGY_FOUNDATION_INDEX.md` lagged the edited papers. Fixed (backup `*.pre_P13CP`):
- **§0 `C` glossary entry:** "metric is C-blind (absence)" → charge conjugation present **as a symmetry**
  (`Q↦−Q` even degeneracy), charge **R-even** / mass **R-odd**, **C is NOT the outer ℤ₂** (that's R) — C
  adjoins an independent ℤ₂ `D₆→D₆×ℤ₂` (`prop:conjugation-parity`, `rem:C-not-R`).
- **§0 `ruling A,B` entry:** dropped the A/B-as-species framing → **neither A nor B is a species; each
  ruling laps through r=0 and changes species at the equator; species = sign(r), local.**
- **§1m `rem:charge`, §1p boundary quote (was quoting the old §258), §1p CPT card, and two more blockquotes:**
  all "C-blind (absence)" → "charge conjugation as a symmetry"; §258 quote updated; `rem:C-not-R` added.
- Index re-scanned: **0 stale patterns remain.** `CORPUS_MAP.md` untouched (its hits are historical changelog).

## The A/B point, clarified (Daryl)
The whole of the A/B removal is: **neither A nor B is a species.** The two null rulings are real and
unchanged; each laps through r=0 and so **changes species at the equator** (blue r>0 / red r<0); species is
sign(r), local. It says **nothing** about how symmetries act on the rulings (R swaps them — geometrically
fine, P12, and irrelevant to the point). An earlier "R-swaps-the-rulings vs storyboard" flag of mine was
confusion, retracted; receipt `ruling_swaps.py` records the geometry (every det−1 reflection swaps the
rulings; the A↔B swap of the strung worldline is τ↦−τ = T) but was answering the wrong question.

## New receipts
`ruling_swaps.py` (the ruling geometry). Control doc: `CPT_COHERENCE_SWEEP.md` (delta-spec + findings ledger).

## Remaining minor / optional
P11 l.82 header comment labels the vantage-swap "P" not "R" (non-rendered comment); an optional one-clause
P14 pointer to `prop:conjugation-parity`. Neither load-bearing.

## Excludes
Build artifacts, `*.pre_P13CP` backups, `__pycache__`. Compiled PDFs included (unchanged this phase — the
edits are markdown).

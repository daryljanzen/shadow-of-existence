# Bundle r1064 — the "minor/optional/flagged" items all fixed (no deferrals)

Closing out everything the r1063 sweep had parked as "minor," "optional," or "flagged for later" —
because those are exactly the things to fix.

## Fixed
- **P11 (dynamics) l.82 header comment:** "the A₂ diagram automorphism **P**" → **R** (r968 canon;
  `= γ⁵` noted). Scanned every paper for other pre-r968 P-for-R slips — none. Recompiles clean (11pp).
- **P14 (matter sector):** added the one-clause pointer at the "charge field-level" sentence —
  "the charge entering the geometry only as the **R-even Q²**, so charge conjugation is present there
  **as a symmetry** rather than an absence and is no substrate isometry, the outer ℤ₂ of Aut(A₂)=D₆
  being **R and not C**" (`cite{JanzenBoundary}`). Recompiles clean (9pp).
- **Ontology index `R = γ⁵ ∝ PT` AUDIT FLAG (§0 Klein-four, l.66): RESOLVED & baked** (receipt
  `storyboard_receipts/R_eq_PT.py`). The flag was a category conflation: `R = γ⁵ ∝ PT` is a statement
  about the induced **4D-cut spinor operators** (`P·T = ±i·γ⁵`, computed), while "R horn-preserving /
  T horn-flipping" is about the **5D geometric reflections**. They differ because R reflects the
  **transverse cut-normal** (fixing all four spacetime legs → horn-preserving; its cut-spinor action
  the 4D volume element γ⁵), whereas P,T reflect **in-cut** legs (T flips X₀ → horn-flipping) and their
  spinor product is that same γ⁵. Same cut-spinor operator, distinct geometric reflections — no tension.
- **Storyboard cleanups:** the retired `τ̃↔τ̄̃` "geometric home for C" D-C entry (§8) marked **⛔ SUPERSEDED**
  at its header (kept as history, not read as live); the "stays a reach for Daryl" note (§7) updated to
  **★ RESOLVED** (C is not the outer ℤ₂ — that's R; `rem:C-not-R`); the A/B-chirality note aligned to
  "neither A nor B is a species."
- Control doc `CPT_COHERENCE_SWEEP.md` PART 5 + ledger: every "optional / if-wanted / minor" note flipped
  to **DONE r1064**.

## New receipt
`storyboard_receipts/R_eq_PT.py` (the R=γ⁵∝PT resolution).

## Standing state
The corpus is coherent on CPT, charge-conjugation-as-symmetry, and the A/B removal, **end to end** — the
paper bodies, the figure, the ontology glossary of record, and the storyboard. No known dangling item.

## Excludes
Build artifacts, `*.pre_P13CP` backups, `__pycache__`. Compiled PDFs included.

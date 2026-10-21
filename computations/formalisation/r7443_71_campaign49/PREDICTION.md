# `r7443+71.49` — PRE-REGISTRATION: campaign 49, row 62's two open data gates — the contraction entries in-kernel, and the six configurations' S³ integrals. ⌗ `900` lines (band 400–2200), ⛔ stop `3000`. ⌗ p `0.40` for both; p `0.60` for (ii) alone

*Under `r7443`. Campaign 48 K (`probes/Row62Claims.lean`) left two gates BUILT IN PART. No Lean was written before
this registration.*

## ① The pieces

***(i) The contraction entries.***
- K's rank matrices carry about 35 000 entries. Each is a 3⁵-index contraction of a jet, and K checked 11 of them
  in the kernel, at about 1 s and 100 MB each.
- Route: an integer evaluator. Jets are scaled to integers and the contractions are written as `Int`
  sums-of-products in a `List`-recursive `def` with no `ℚ` normalisation inside the loop. The kernel's
  GMP-accelerated `Nat`/`Int` arithmetic should make each entry milliseconds.
- One theorem then states that the evaluator equals K's `evF` (a definitional or `ring` lemma). Every table
  entry follows by `decide +kernel` in chunks.
- ***If it works, the rank theorems rest on Lean-computed matrices, and no receipt data remains.***

***(ii) The six configurations' S³ integrals.***
- K's 6×8 rows are the receipt's integrals over the Euler box of trigonometric polynomials (its `tri`).
- Route: row 59's `section_e_integrals` machinery. Products of `sin`/`cos` integrate in closed form by
  product-to-sum and `integral_cos`/`integral_sin`.

***Failable:*** (i) and (ii) are each BUILT, BUILT IN PART, or REPORTED. ***Row 62 → `DONE`*** if both are BUILT. The
census also needs claim 1, which is complete since campaign 48. ***Risk:*** the kernel cost of `List` recursion over
35 000 entries; the fallback is chunked theorems and a measured rate.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

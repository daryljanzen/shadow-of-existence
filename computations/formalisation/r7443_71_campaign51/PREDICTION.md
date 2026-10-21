# `r7443+71.54` — PRE-REGISTRATION: campaign 51, the open halves of rows 65 and 66 — the hard-cutoff slope `→ 15/4` analytically, and the TT spectrum of `S³` built to a named obstruction. ⌗ `1200` lines in two probes (band 500–2400), ⛔ stop `3200`. ⌗ p `0.55` for the slope; p `0.35` for the spectrum's eigen-tensors at every level

*Under `r7443`. Rows 65 and 66 are `DONE (chartable half)`. Their open halves are row 65's floating cutoff slope,
row 66's deficiency claim (prose), and, shared by both, the imported TT spectrum. No Lean was written before this
registration.*

## ① The pieces

***S — row 65's hard-cutoff slope*** (`probes/Row65Slope.lean`).
- The receipt measures `d/d ln M` of its hard-cutoff level sum at `M = 2000, 4000, 8000`, getting `3.7497`
  against `15/4`.
- Prove the ***limit***: the hard-cutoff sum's logarithmic slope tends to `15/4` as `M → ∞`, as a `Tendsto`
  statement. The route is Faulhaber's closed forms and `Real.tendsto_harmonic_sub_log`.
- Prove the receipt's printed slopes as rational brackets at its three `M`.
- Done the same way for the receipt's control frequencies, both the old and the corrected one.

***T — the TT spectrum of the round `S³`*** (`probes/S3TTSpectrum.lean`).
- ***Lower half, buildable.*** For every level `m ≥ 3`, exhibit transverse-traceless symmetric tensors in the
  left-invariant frame that satisfy the TT eigen-equation with eigenvalue `m² − 3`, at the normalisation the corpus
  uses. They are built from SU(2) matrix coefficients via the engine's frame calculus. If the full multiplicity
  `2(m² − 4)` is out of reach, give multiplicity lower bounds, at least for `m = 3, 4, 5`.
- ***Upper half, the expected obstruction.*** That these are ALL the TT eigen-tensors, i.e. completeness of the
  spectrum. That needs harmonic analysis on `S³`: Peter–Weyl for SU(2), and a Laplace–Beltrami operator with
  self-adjoint spectral theory. The searches already recorded in `r7453_71_gap_class/CLASS.md` found none of it in
  Mathlib. They are re-run on the object and recorded.

***Row 66's deficiency claim*** is prose, a sentence of the paper, not a computation. Like the text pins of every
`DONE` row, it is excepted, and it is recorded as such.

***Census.***
- If S is built and T reaches its named obstruction, rows 65 and 66 stay `DONE (chartable half)`. Each open half is
  narrowed to exactly ***completeness of the TT spectrum (Peter–Weyl on S³, absent from Mathlib)***. That is the
  order's other exit.
- If T is fully built, including completeness, both rows → `DONE`.

***Failable:*** S and T are each BUILT, BUILT IN PART, or REPORTED.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

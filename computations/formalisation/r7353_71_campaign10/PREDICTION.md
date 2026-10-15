# `r7353+71.11` — PRE-REGISTRATION: campaign 10, row 58's measure gate: `det E(ε) = 1 + O(ε³)` for the receipt's truncated exponential and any traceless `3 × 3` `H`, as exact polynomial algebra. ⌗ `90` lines (band 45–170), ⛔ stop `200`, no table. ⌗ p `0.65`

*Orders: `FOR_71.md` §`r7353` ① (register before building, census in the same push). Written before anything is
built. Row 58's receipt was opened at `r7351`. The gate is its first one: "`H` is traceless, so `det exp(εH) = 1`
to this order".*

## ① The piece

***A.*** Over `ℝ[X]`, with `ε` as `X`, take `E = 1 + X·B` and `B = H + (X/2)H² + (X²/6)H³` (the receipt's `NORD = 3`
truncation).
1. Prove the `3 × 3` identity `det(1 + A) = 1 + tr A + ½((tr A)² − tr A²) + det A` over any commutative ring.
2. Read off the coefficients of `det E`: `1`, then `tr H = 0`, then `½tr H² − ½tr H² = 0`.

***Failable:*** BUILT, BUILT IN PART or REPORTED. p `0.65` under the stop.
- ***Risk:*** coefficient extraction through `det_fin_three` with nine symbolic entries. If it explodes, the
  identity is proved at the level of traces instead.
- ***What it will not build:*** the receipt's statement is about the true `exp`. `mathlib` has no `det_exp`, so the
  truncated form is the object, as in `r7353+71.2`.

## ② Decisive fraction, survival, compile

- ***Decisive:*** the coefficient-`2` cancellation. Coefficient `1` is trivially `tr H`.
- ***Readings:*** none new. The running rate stays `14` of `21`.
- ***Compile:*** no table, so under a minute.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

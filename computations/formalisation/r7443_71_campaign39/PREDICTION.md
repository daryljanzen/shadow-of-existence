# `r7443+71.22` — PRE-REGISTRATION: campaign 39, library-gap row 57 (second order is an order the construction does not reach). ⌗ `700` lines (band 400–1300), ⛔ stop `1800`. ⌗ p `0.40`

*Under `r7443` ②, step 4, next in `PRICING.md`'s order. The receipt is
`P10_second_order_is_an_order_the_construction_does_not_reach_and_the_one_new_direction_carries_no_new_convention.py`.
No Lean was written before this registration.*

## ① The piece: `probes/Row57Second.lean`

The receipt's computed checks (A1–A3, B1, B2, the asymptotics, the harmonic sum, C and D) as `PRICING.md` lists them.
- ***A1:*** the `cosh` turnover.
- ***A2:*** the decimal `ε` bounds, as exact inequalities.
- ***A3:*** the sectional-curvature model's `ε¹` and `ε²` coefficients.
- ***B1:*** the `5 × 4` rank `3`, equal to its condition, and raised by `K₂³`.
- ***B2:*** the log structure, and the sample-point ranks `1, 1, 2`. The ranks carry `log` entries: an exhibited
  minor needs bounds on `log`, and Mathlib's `Real.log_two_gt_d9` and friends are expected.
- ***Asymptotics:*** `L = 15/4`.
- ***The harmonic sum's*** log coefficient `L` and its missing `M⁵` term.
- ***C:*** `L·h·ζ(1 + h) → L`, by `riemannZeta_residue_one`, replacing the receipt's numeric probe. The trace and
  `R − 4Λ` facts, and the control weight.
- ***D:*** the rank under a scaled vertex.

***Caveats, registered.***
- ***Imported:***
  - the TT weights;
  - the FRW sectional-curvature invariant formulas in `K₁` and `K₂`;
  - the measured `Λ` and `ℓ_P²`.
- The meromorphic continuation of the level Dirichlet series is not in this campaign; the receipt does not do it.
- Paper-text checks are pins.

***Failable:*** BUILT, BUILT IN PART (per section), or REPORTED. p `0.40`.

***Census if BUILT:*** row 57 → `DONE`, imports named, `decl` filled.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

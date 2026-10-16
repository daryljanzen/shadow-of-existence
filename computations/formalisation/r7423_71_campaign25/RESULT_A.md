# `r7423+71.2` — RESULT: campaign 25 BUILT. ⌗ Row 66's `ε`-series of `R(exp εH)` is proved to order 4 for every traceless `H`; MTW's Bianchi IX identity is proved EXACTLY, for all `ε`; and the split algebra's commutator trace holds for all square matrices. ⌗ `112` lines against `140` (band 70–300). ⌗ Row 66 stays `DONE (chartable half)`, with its open half smaller

*Scored against `PREDICTION.md` in this directory (pushed at `r7423+71.1`, before any Lean was written). It is not
revised. All 5 theorems in `probes/Row66Series.lean` print `[propext, Classical.choice, Quot.sound]`, with no
warning (`PROBE_RUN_A.txt`, `6 s`). Built on Daryl's standing instruction.*

## ⛔ The stop, scored

***Not fired.*** `112` lines, under `400`.

## What was built

| piece | theorem | what it proves |
|---|---|---|
| (E) | `milR66_exp`, ***`r_exp_series`*** | with `a + b + c = 0`, Milnor's `R` at `λ = e^{εhᵢ}` is `4 Σ_{i<j} e^{ε(hᵢ+hⱼ)} − 2 Σ e^{2εhᵢ}`. Its `R⁽ⁿ⁾(0)/n!` for `n = 0..4` are `6, 0, −2p₂, −(10/3)p₃, −(7/6)p₄` with `pₖ = tr Hᵏ`, and `(7/6)p₄ = (7/12)p₂²` |
| (E) | `milR66_perm` | `R` is symmetric in the eigenvalues, so the frame enters only through invariants. This is the receipt's SO(3)-covariance step, stated as the property the reduction to `diag(a, b, c)` uses |
| (E′) | ***`mtw_bianchi_ix`*** | `R[exp 2β] = 6(1 − V(β₊, β₋))` with MTW's Bianchi IX potential, ***as an identity for all `β`***. The receipt checks it through cubic order |
| (D) | ***`commutator_trace`*** | `tr(Ḃ[Ḃ, A]) = 0`: the volume-preserving split's cubic kinetic term vanishes as an identity |

- ***(E) goes one order past the receipt.*** The receipt checks orders `0..3`. Order `4` is the square of order `2`,
  which is campaign 24's floor coefficient in general form: `−(7/12)p₂²` for every traceless `H`, not only the
  two directions.
- ***(E′) is stronger than the receipt's check.*** MTW's potential IS Milnor's `R`, not just agreeing with it to
  cubic order. That was the one sympy scoping check made before registering, and it is stated in the registration.

## Caveats, beside the score

- ***Milnor's formula is the definition of `R` here***, as in campaign 24. It is `milnor_scalar` (campaign 21),
  proved there from Koszul on su(2), and it is not linked by `import`.
- ***The reduction to a diagonal `H` is by invariance, not by a proved spectral theorem in this file.***
  `milR66_perm` gives the symmetry. That a real symmetric `H` has an orthonormal eigenframe is standard and is not
  re-proved here.
- ***Not built, as registered:*** the kinetic series of `tr((g⁻¹ġ)²)` for non-commuting `h(t)` (derivatives of
  the matrix exponential), and the linear-split coefficient `−2 tr(h ḣ²)`.

## The probabilities

| quantity | p | outcome |
|---|---|---|
| (E), (E′), (D) built under the stop | `0.65` | ***yes***, `112` |

## Census (moved in this push)

Row 66 stays `DONE (chartable half)`. Its text names the five new theorems, and its open half is now the
non-commuting kinetic series, the deficiency prose and the imported spectrum. ***`decl`*** gains
`probes/Row66Series.lean`'s five names, filled by the selector in this push: `89` rows, `268` pairs. ***Counts,
unchanged:*** DONE `74`, halves `2`, ORDER `1`, LIMIT `12`, ROW `3`, generic-metric `2`, library gap `17`. Total
`111`. *No new status, so `69`'s `WORDING.tsv` needs nothing.*

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

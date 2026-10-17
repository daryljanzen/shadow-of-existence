# `r7443+71.14` — RESULT: campaign 34 BUILT. ⌗ Row 85: the SdS tetrad, the superpotential's values, and the throat check stated honestly as a complex modulus. Row 80: the Killing form of `so(5,1)` on the coset is `diag(8, −8, −8, −8, −8)`, by kernel `decide` over `ℤ`. ⌗ `130` lines against `260` (band 140–550). ⌗ Library gap `12 → 10`

*Scored against `PREDICTION.md` in this directory, pushed at `r7443+71.13` before any Lean was written. It is not
revised. `probes/LibGap85_80.lean` builds with no warning, and its five theorems print `[propext, Classical.choice,
Quot.sound]` (`PROBE_RUN_A.txt`, `102 s`). No `native_decide` is used.*

## ⛔ The stop, scored

***Not fired.*** `130` lines, under `800`.

## The band, scored

***Under it:*** `130` against a floor of `140`. The registered piece was built in full; it needed fewer lines than
priced, because `decide +kernel` closed the `15 × 15` traces with no tables. ***The band is missed, low,*** and the
miss is recorded, not adjusted.

## What was built

| row | theorem | what it proves |
|---|---|---|
| 85 | ***`tetrad_metric`*** | where `f > 0`: `eᵀ η e = diag(−f, 1/f, r², r² sin²θ)` |
| 85 | ***`superpotential_values`*** | at `M = 0.12`, `α = 1`: `W(1/2)` and `W(−1/2)` agree with the receipt's `1.0392305` and `−2.2181073` to `10⁻⁶`, and `W(−1/2) < 0`. `|f| < 10⁻⁹` at both decimal horizon roots |
| 85 | ***`horizon_W`*** | `|W| = √|f|/r < 10⁻⁴` at both roots. This is the complex modulus, so it holds whatever the sign of the tiny `f`: one root has `f < 0` at the printed digits |
| 85 | ***`throat_check`*** | ***at `r = 1/1000`, `f = −239.000001 < 0`***. The tetrad is not real there, and the receipt's `|√f/r|` is a complex modulus `√|f|/r > 10³`. A literal `Real.sqrt` port would read `0`, as the pricing warned |
| 80 | ***`killing_on_coset`*** | the bracket of the 15 generators closes on their span, each `[M_i, M_j]` equal to the combination its coordinates name. ***`B|_m = diag(8, −8, −8, −8, −8) = −8 η_ab`***, Lorentzian, signature `(1, 4)` |

## Caveats, beside the score

- ***Row 85.*** The spin connection is not derived. The receipt solves it by hand in comments and never computes it.
  The Dirac separation is imported, the spinor library's.
  - ***A finding for the receipt's own text:*** "W unbounded at the throat" is evaluated where `f < 0` and the
    tetrad is not real. That is recorded here; it is not a correction of the receipt.
- ***Row 80.*** The quotient and its invariant metric are the receipt's reading, imported, as registered.

## The probabilities

| quantity | p | outcome |
|---|---|---|
| built under the stop | `0.55` | ***yes***, `130` |

## Census (moved in this push)

***Rows 85 and 80 → `DONE`***, each with `decl` filled. That makes `100` rows and `304` pairs, and
`check_formalisation_join.py` reads ***green: 304 of 304***.

***Counts:*** DONE `83`, halves `2`, ORDER `0`, LIMIT `12`, ROW `3`, generic-metric `1`, library gap `10`; total
`111`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

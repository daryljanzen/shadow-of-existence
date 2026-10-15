# `r7353+71.12` — RESULT: campaign 10 BUILT. ⌗ Row 58's measure gate: `det E(ε) = 1 + O(ε³)` for the receipt's truncated `exp(εH)` and every traceless `3 × 3` `H`, exact over `ℝ[X]` (`row58_det_gate`). ⌗ `58` lines against `90` (band 45–170, ⛔ stop `200`): in the band. ⌗ `11 s`, no table. ⌗ Row 58 stays a half; its open half shrinks to the Legendre transform

*Scored against `PREDICTION.md` in this directory (pushed at `r7353+71.11`). It is not revised. The axiom line is
`[propext, Classical.choice, Quot.sound]`, with no `sorryAx` (`PROBE_RUN_A.txt`). The new code is appended to
`probes/Campaign7.lean`, beside `row58_adm_kinetic`; nothing earlier in the file is touched.*

## ⛔ The stop, scored first

***Not fired.*** `58` lines (lines 79–136 of the file, with the `#print axioms` line), under `200`.

## What was built

| piece | what it proves | lines |
|---|---|---|
| `det_one_add_fin3` | `2·det(1 + A) = 2 + 2tr A + (tr A)² − tr A² + 2det A`, for `3 × 3` over ANY commutative ring | `7` |
| `detBody`, `detBody_eval` | `B = H + (X/2)H² + (X²/6)H³` over `ℝ[X]`, so `E = 1 + X·B`; `B` at `X = 0` is `H` | `8` |
| `coeff0_trace` | coefficient `0` of a trace is the trace at `X = 0` | `3` |
| ***`row58_det_gate`*** | `det E` has coefficients `1`, `0`, `0` at `ε⁰`, `ε¹`, `ε²` when `tr H = 0` | `35` |
| header, docstrings, `#print axioms` | | `5` |
| | ***campaign 10*** | ***`58`*** |

***How the cancellation reads in the proof*** (the registered decisive step):
- `det_one_add_fin3` at `A = X·B` gives `2 det E = 2 + 2X·tr B + X²(tr B)² − X²·tr(B²) + 2X³det B`.
- Coefficient `0`: `2 det = 2`. Coefficient `1`: `2·tr H = 0`.
- Coefficient `2`: `2·(coefficient 1 of tr B) + (tr H)² − tr H²`, which is `2·½tr H² + 0 − tr H² = 0`.
- The `X³det B` term never reaches `ε²`. That is the `O(ε³)`.

***The registered risk did not fire.*** The extraction never went through `det_fin_three` with nine symbolic entries.
The trace identity was proved once over a general commutative ring, and everything after it is about traces.

## Caveats beside the score

- ***The object is the truncation,*** as registered and as in `r7353+71.2`. `mathlib` has no `det_exp`, so the true
  `exp` is not what is proved. The receipt's own `NORD = 3` truncation is.
- ***Only to `ε²`.*** The truncated `det E` is NOT `1` at `ε³` and above in general. The receipt claims the gate
  "to this order", and that is the order proved.
- ***What it does not build:*** the Legendre transform, and the Hamiltonian sign the receipt draws from the positive
  kinetic term. These remain row 58's open half.

## Compile time

| | registered | measured |
|---|---|---|
| wall | under a minute (no table) | ***`11 s`*** |

## The probabilities

| quantity | p | outcome |
|---|---|---|
| campaign 10 BUILT under its stop | `0.65` | ***yes***, `58` |

## Census (moved in this push)

Row 58's text now names the det gate closed at `r7353+71.12`, and its open half is the Legendre transform alone. The
row stays `DONE (chartable half)`. ***Counts unchanged and checked before the commit:*** DONE `45`, halves `12`,
generic-metric `2` (20, 62), library gap `17`, no-connection `32`, real obstruction `3`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

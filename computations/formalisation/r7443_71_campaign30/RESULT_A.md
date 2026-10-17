# `r7443+71.6` — RESULT: campaign 30 BUILT. ⌗ Row 20's general identity was already in the tree: `contracted_bianchi`, row 6's, cited and not rebuilt. The receipt's computed half is built beside it: TT waves, a divergence-free two-wave superposition, the exact de Sitter mode equation, and `σ²`. ⌗ `134` lines against `150` (band 80–320). ⌗ ***Row 20 → `DONE`***

*Scored against `PREDICTION.md` in this directory, pushed at `r7443+71.5` before any Lean was written. It is not
revised. Built under `r7443` ②, step 2. `probes/Row20Freedom.lean` builds with no warning, and its four theorems
print `[propext, Classical.choice, Quot.sound]` (`PROBE_RUN_A.txt`, `6 s`).*

## ⛔ The stop, scored

***Not fired.*** `134` lines, under `450`.

## The finding the registration led with

Row 20 was parked as "index algebra over an arbitrary (non-diagonal) metric: a separate item". The receipt's
mechanism is the contracted Bianchi identity, "an off-shell geometric identity, true for every metric". That item
was built at `r7353+71.8`:
- ***`contracted_bianchi`*** (`probes/Bianchi2.lean`, row 6), for THE connection of ANY smooth symmetric
  nondegenerate metric on `ℝⁿ`.
- Row 20's text predates it, and the row was never moved.

***So row 20's general half was done a campaign before it was looked at again.*** That is the `r7443` ① pattern: a
row parked by its own wording, not by its mathematics.

## What was built

| theorem | what it proves |
|---|---|
| ***`tt_waves`*** | `e₁₊, e₁ₓ, e₂₊, e₂ₓ` are each trace-free and transverse to their own `k`. `k₁ · k₂ = 0` and `k₁ × k₂ ≠ 0`, so the two directions are not parallel and the data is not the single Gowdy mode |
| ***`superposition_transverse`*** | for arbitrary complex `A₁, A₂`, the three partials of `h_i·` exist at every point (`HasDerivAt`, complex-valued) and they sum to zero. That is the momentum constraint for general TT data, from each wave's transversality alone |
| ***`mode_equation`*** | for real `η ≠ 0` and `k ≠ 0`, `u = e^{−ikη}(1 − i/(kη))` has the two derivatives stated, and `u'' + (k² − 2/η²) u = 0` exactly |
| ***`shear_square`*** | `e:e = 2, 2, 0`, and `σ = ½ εḣ e₊` gives `σ² = ½ ε²ḣ²`, positive when `εḣ ≠ 0`. It is a scalar of order `ε²` |

## Caveats, beside the score

- ***The polarized-leaf instance of `∇_μ G^{μν} = 0` is not rebuilt***, as registered. The general identity covers
  it.
  - Row 6's caveat carries over: `contracted_bianchi`'s right side is `g^{ac} ∇_b R_ac`, which is `½ ∂_b R` only
    through metric compatibility.
  - `compat_lc` is built beside it, but the two are not composed into the `∂_b R` form here.
- ***The paper-text checks are pins, not mathematics***, and they are not formalised.

## The probabilities

| quantity | p | outcome |
|---|---|---|
| built under the stop | `0.65` | ***yes***, `134` |

## Census (moved in this push)

***Row 20 → `DONE`.*** ***`decl`*** gained the four new names and `Bianchi2.lean`'s `contracted_bianchi` in this push.
That makes `91` rows and `284` pairs, and `check_formalisation_join.py` reads ***green: 284 of 284***.

***Counts:*** DONE `76`, halves `2`, ORDER `0`, LIMIT `12`, ROW `3`, generic-metric `1` (row 62), library gap `17`;
total `111`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

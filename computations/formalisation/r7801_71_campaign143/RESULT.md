# `r7801+71.2` — RESULT: campaign 143, **P14's `prop:wall`: the five reachable rows all BUILT (Z1–Z5)**. ⌗ `297` lines (band 220–420, estimate 300, **in band**), at p(all five) `0.65`

*The census and registration are `PREDICTION.md`. The probe is the new standalone file `probes/MatterWall.lean`
(`mw_`), P14's citable file.*

## Verification
- `lake env lean probes/MatterWall.lean` gives **0 errors and 0 warnings**.
- **12 axiom lines**, every one `[propext, Classical.choice, Quot.sound]`.
- The forbidden-token grep is clean, imports are `Mathlib` only, and `check_no_sorry.py` reports ALL 29. No options are
  set.

## Rows

| Row | Statement (Lean) | Mark |
|---|---|---|
| Z1 | `mw_chirality`: `σ_y χ₊ = χ₊`, `σ_y χ₋ = −χ₋` (`χ± = (1, ±i)`); `aχ₊ + bχ₋ = 0 ⟹ a = b = 0`; `−mσ_y(fχ₊ + gχ₋) = (−mf)χ₊ + (mg)χ₋` | **BUILT** |
| Z2 | `mw_exactly_one`: for a kink `m` (`m ≥ m₀ > 0` on `[X, ∞)`, `m ≤ −m₀` on `(−∞, −X]`) with antiderivative `F`: `e^{−F}` solves `f′ = −mf`; `(e^{−F})²` is integrable on `ℝ`; every solution of `f′ = −mf` is `c·e^{−F}`; and every square-integrable solution of `g′ = mg` is `0`. Supporting lemmas: `mw_unique_minus`, `mw_unique_plus` (uniqueness); `mw_F_lower` (`F ≥ m₀|x| − K`); `mw_exp_abs_integrable`, `mw_bound_integrable`, `mw_conj_not_integrable` | **BUILT** |
| Z3 | `mw_flip`: for the reversed wall, the normalizable modes are exactly `{(0, c·e^{F})}`, the `σ_y = −1` chirality | **BUILT** |
| Z4 | `mw_tanh`: `m = tanh(x/a)` (`a > 0`, `F = a log cosh(x/a)`, a kink with `m₀ = ½`, `X = a`). `cosh^{−a}(x/a)` solves `f′ = −mf` and is normalizable; every solution is a multiple of it; `cosh^{a}(x/a)` is not normalizable | **BUILT** |
| Z5 | `mw_operator`: for `f > 0`, the tortoise form `fψ_r r = λ√fψ` and the frame form `√fψ_r r = λψ` are both `ψ_r·r√f = λψ`, the one logarithmic derivative `λ/(r√f)`. `f(−r; −M) = f(r; M)`, so `W = λ√f/r` is odd. `f = 0 ⟹ W = 0` | **BUILT** |
| Z6 | "That operator is the diagram-automorphism parity `R = γ⁵`" | **interpretive** |
| Z7 | The bound mode on the slicing curve's own `W = λ√f/r`, in the leaf norm | **NOT BEGUN** (beyond) |

**Witnesses** (`mw_witness`):
- at `a = 1` the bound mode is `1` at the wall's centre, so nonzero, and it is normalizable;
- `χ₊ ≠ 0`;
- `f = 0.35 > 0` at `M = 1`, `α² = 100`, `r = 5`;
- `f = 0` at `M = 1`, `α² = 27`, `r = 3`.

**Against the registration:**
- **The named stop did not hold.** Z2's integrability closed through an explicit `e^{−c|x|}` dominator, and the
  `tanh`-only fallback was not needed.
- **Z2 is the general Jackiw–Rebbi statement**, for any kink with an antiderivative, not the `tanh` wall alone. Z4 is
  its instance.
- **A witness was corrected.** The registered `f > 0` point (`M = 1`, `α² = 27`, `r = 3`) is in fact the Nariai
  double horizon (`27M² = α²`), where `f = 0`. It is used as the `W = 0` witness, and the `f > 0` witness moved to
  `α² = 100`, `r = 5`.
- **Z5 is stated cleared of the `r` denominator** (`ψ_r · r√f = λψ`), the same content.
- **"Exactly one" is formalised as one line of normalizable modes** in the `σ_y = +1` component, with zero in the
  other: one mode up to scale.

**P14 tally:** `prop:wall` has 7 rows; **5 are BUILT** (Z1–Z5), Z6 is interpretive and Z7 is beyond. `prop:forced`
is interpretive.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

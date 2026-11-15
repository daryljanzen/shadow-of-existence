# `r7801+71.1` — CENSUS AND PRE-REGISTRATION: campaign 143, **P14's `prop:wall`: exactly one normalizable chiral zero-mode per wall, its chirality the sign of the flip**. ⌗ `300` lines (band 220–420), p(all five BUILT) `0.65`

*Registered before any Lean, per r7801. The paper is P14, `corpus/matter_sector_paper.tex`, read at `0205396a1`.
The probe is the new standalone `probes/MatterWall.lean` (`mw_`), P14's citable file. Mathlib only.*

## Census: P14's propositions
- **`prop:forced`** ("Within CR the three-plane construction is forced") is a statement about the programme's criterion
  of necessity. It is **interpretive**, with no cored row.
- **`prop:wall`** (l.181) is the formal one. The rows are fixed below.

## The paper's own wall and reduction (`sec:chirality`)
- **The reduction.** The massless radial Dirac problem on the slicing curve is a first-order pair with superpotential
  `W = λ√f/r` in the tortoise variable `dx = dr/f`, where `f = 1 − 2M/r − r²/α²` and `λ = j + ½`. Equivalently it is
  `W = λ/r` against the frame derivative `√f d/dr`. Both forms give one logarithmic derivative,
  `ψ′/ψ = λ/(r√f)`.
- **The wall.** `r` is signed, so `W` changes sign at `r = 0`: a domain wall.
- **The displayed model.** `ψ′ = −mσ_yψ` gives `ψ = exp(−∫m)χ₊`, with `χ₊` the `σ_y = +1` eigenspinor. For
  `m = tanh(x/a)` this is `ψ = cosh^{−a}(x/a)χ₊`, normalizable, while `χ₋` grows as `cosh^{+a}` and is rejected.

## Rows

| Row | Statement | Lines | p | Note |
|---|---|---|---|---|
| Z1 | **The chirality basis.** `σ_y = !![0, −i; i, 0]` has `σ_y χ± = ±χ±` with `χ± = (1, ±i)`. `χ₊, χ₋` are independent, and `−mσ_y(fχ₊ + gχ₋) = (−mf)χ₊ + (mg)χ₋`: the pair decouples into `f′ = −mf` and `g′ = +mg` | 30–50 | 0.9 | |
| Z2 | **Exactly one, for any kink.** Let `m` have an antiderivative `F`, and let `m ≥ m₀ > 0` for `x ≥ X` and `m ≤ −m₀` for `x ≤ −X`. Then every solution of `f′ = −mf` is `c·e^{−F}`, and every solution of `g′ = mg` is `c·e^{F}`. `(e^{−F})²` is integrable on `ℝ`, and `(c·e^{F})²` is integrable only for `c = 0`. So the normalizable zero modes are exactly the line `{(c·e^{−F}, 0)}`: one mode, chirality `σ_y = +1` | 120–200 | 0.65 | **The expected stop**: the integrability bounds. **The fallback** is Z2 for the `tanh` wall alone, marked BUILT IN PART |
| Z3 | **The flip.** For the reversed wall (`−m`) the normalizable modes are exactly `{(0, c·e^{F})}`, chirality `σ_y = −1`: reversing the wall reverses the chirality | 15–30 | 0.9 | From Z2 |
| Z4 | **The displayed wall.** `m = tanh(x/a)` (`a > 0`) is a kink (`m₀ = ½`, `X = a`), with `F = a log cosh(x/a)`. The bound mode is `cosh^{−a}(x/a)χ₊`, and the conjugate `cosh^{a}(x/a)χ₋` is not normalizable | 40–70 | 0.8 | |
| Z5 | **The paper's operator.** For `f > 0`, the tortoise form `fψ_r = (λ√f/r)ψ` and the frame form `√fψ_r = (λ/r)ψ` are both `ψ_r = λψ/(r√f)`. `W = λ√f/r` is odd under `(r, M) ↦ (−r, −M)` (`f` even), and vanishes at the horizons `f = 0` | 30–60 | 0.9 | |
| Z6 | "That operator is the diagram-automorphism parity `R = γ⁵`" | — | — | **Interpretive**: a cross-paper identification (P12 reads it off the constraint algebra) |
| Z7 | The bound mode on the slicing curve's own `W = λ√f/r`, in the leaf norm `∫|ψ|² dℓ` | — | — | **Beyond**: the paper places the selection on the static region (amplitude `r^{∓λ}`), with the turning points at finite proper distance and the `r = 0` crossing a bounded phase. Its exact formal content (which region, which norm, which endpoint behaviour selects) is not fixed in closed form by the text. Z2 is the kink mechanism it rests on |

**Totals.** `prop:wall`: **7 rows, 5 within reach** (Z1–Z5). Z6 is interpretive and Z7 is beyond. `prop:forced`
is interpretive.

## Registration: campaign 143
- **Rows:** Z1–Z5, in `probes/MatterWall.lean`.
- **Price:** 300 lines (band 220–420). p(all five BUILT) `0.65`.
- **The expected stop** is Z2's integrability.
- **Non-vacuity:** `a = 1` (the `tanh` wall); `M = 1`, `α² = 27`, `r = 3` for Z5's `f > 0` point.
- **Per r7801:** if P14 finishes under its band, K4 (P11's type I) is raised in the report. Otherwise it stays priced
  as it is.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

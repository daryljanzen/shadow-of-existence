# `r7745+71.1` — PRE-REGISTRATION: campaign 133, **P9's reachable rows: the Kantowski–Sachs Einstein tensor and its vacuum kernel (3a–c), and the pp-wave's Ricci (8a)**. ⌗ `600` new lines (band 400–850), p `0.6`. **Expected stop:** the KS Christoffel table, which depends on `τ` and `θ`

*Registered before any Lean. The inventory is `r7745_71_survey/SURVEY.md`.*
- **The probe** is a new standalone file, `probes/Range.lean`, prefix `rn_`. It imports only Mathlib. Campaign 134
  appends to it, so it becomes P9's citable file.
- **The copy.** `StaticEinstein.lean`'s `KrCurvature` section (with `KrTrig`) is copied verbatim, with names kept.
  `rn_Ric`, `rn_scal` and `rn_G` repeat `es_Ric`, `es_scal` and `es_G`'s definitions.

## Rows

| Row | Statement | Lines | p |
|---|---|---|---|
| 3a | `g = diag(−1, X(τ)², Y(τ)², Y(τ)² sin²θ)`, at a point with `X, Y, sin θ ≠ 0`, `X`, `Y` twice differentiable: `−G^τ_τ = (Y′/Y)² + 1/Y² + 2X′Y′/(XY)`, `G^χ_χ = −2Y″/Y − (Y′/Y)² − 1/Y²`, `G^θ_θ = G^φ_φ = −Y″/Y − X″/X − X′Y′/(XY)`, and `G^μ_ν = 0` for `μ ≠ ν` | 250–450 | 0.65 |
| 3b | If `Y′ = X`, `X′ = −f′(Y)/2` (so `X″ = −f″(Y)X/2`), `X² = −f(Y)` and `f = 1 − 2M/Y − ΛY²/3`, then `G^μ_ν + Λδ^μ_ν = 0` for all 16. **Non-vacuity:** `M = 0`, `Λ = 3/α²`, `Y = α cosh(τ/α)`, `X = sinh(τ/α)` at `τ > 0` | 80–150 | 0.75 |
| 3c | Nariai: `Y = 1/√Λ`, `X = e^{√Λτ}` gives `G^μ_ν + Λδ^μ_ν = 0` for all 16 | 30–60 | 0.9 |
| 8a | pp-wave, `H(u, x, y)`: `R_uu = −½(∂²_x H + ∂²_y H)` (as `kr_pd` of `kr_pd`) and `R_μν = 0` otherwise. So `R_μν = 0` for all `(μ, ν)` iff `∂²_x H + ∂²_y H = 0`. **Non-vacuity:** `H = x² − y²` | 120–250 | 0.7 |

**The expected stop** is 3a's table on a neighbourhood: `X(y₀)`, `Y(y₀)` and `sin y₂` are non-zero near the point.
This is the `es_Hyp.U` pattern with two variables. **The fallback** is to state 3a at points where the hypotheses
hold on an open set given as a hypothesis, which is the same content with weaker packaging.

**Interpretive, not formalised:** "the seam reappears" and the Kretschmann reading.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

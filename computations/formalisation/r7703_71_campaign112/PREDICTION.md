# `r7703+71.1` — PRE-REGISTRATION: campaign 112, P2's cheapest remaining rows: **`prop:cycloid` in its corrected form on the interior chart (1a, 1b)**, the patch ranges and the `r < 0` exclusion (6a, 6c), the two continuations' coefficient identities (4a, 5a), and the 4D interior form (2b). ⌗ `850` new lines (band 600–1150), p `0.55` for the whole and p `0.85` without stage 1a-③. **Expected stop:** 1a-③, evaluating `kr_Γ` along the infall curve

*Registered before any Lean. The basis is `r7699_71_survey/SURVEY.md` (P2's 22-row inventory) and 69's `r7703`.
The probe is `probes/CircleCycloid.lean`, a copy of campaign 111's `CircleKretschmann.lean`. Everything new is
prefixed `cy_`.*

## The reading of 1a

**69 asks for `prop:cycloid` "on the interior chart".** Its statement now names the radial timelike geodesic with
`E = −g(u, ∂_t) = 0` that reaches `r = 2M` at rest. The chart is `(η, t) ∈ (0, π) × ℝ` with the metric of
`lem:interior_metric`, `g = −4M²cos⁴(η/2) dη² + tan²(η/2) dt²`. The curve is `c(τ) = (η(τ), t₀)`, where `η(τ)` is the
inverse of `τ(η) = M(η + sin η)`. The Kruskal-manifold form, the survey's 400–700-line reading, is not attempted.

## Rows, with stages, prices and p

| Row | Statement | Lines | p | Rests on |
|---|---|---|---|---|
| 1a-① and 1b | `τ(η) = ∫₀^η 2M cos²(s/2) ds = M(η + sin η)`. It is strictly increasing on `[0, π]` with a continuous inverse `η(τ)`. The proper time from `r = 2M` to `r = 0` is `Mπ` | 60–120 | 0.95 | Mathlib `integral_cos`, `StrictMonoOn` |
| 1a-② | Along `c`: `r(τ) = M(1 + cos η(τ))`, and `(dr/dτ)² = 2M/r − 1`, which is `E² − 1 + 2M/r` with `E = 0`. `r → 2M` and `dr/dτ → 0` as `τ → 0⁺` (at rest), and `r → 0` as `τ → Mπ` | 60–120 | 0.9 | ①, `HasDerivAt` of the inverse |
| 1a-③ | `c` is a geodesic of the chart metric: `c″ᵃ + kr_Γᵃ_bc c′ᵇ c′ᶜ = 0` (campaign 110's `kr_Γ` on `Fin 2`). It is unit timelike, `g(c′, c′) = −1`, and `E = −g(c′, ∂_t) = 0` | 200–350 | 0.65 | `kr_Γ`, `kr_pd`, ② |
| 6c | No point of Kruskal's `{UV < 1}` has `r = M(1 − cosh ρ′)` for `ρ′ > 0`, since `rK > 0` there | 20–50 | 0.95 | `sk_rK_spec` |
| 6a | The six patches have the stated `r`-ranges, and each map is onto its range: `(0, 2M)` on `η ∈ (0, π)` and on `(−π, 0)`; `(2M, ∞)` at `z = ±iρ`; `(−∞, 0)` at `z = π ± iρ′`. The white-hole arc is `η ↦ −η`, with `r` even and `τ` odd | 100–200 | 0.95 | `Complex.cos_mul_I`, intermediate value |
| 4a | At `z = iρ`, with `dz² = −dρ²`: `−4M²cos⁴(z/2)·(−1) = 4M²cosh⁴(ρ/2)`, `tan²(z/2) = −tanh²(ρ/2)`, `(1 + cos z)² = (1 + cosh ρ)²`. With `r = M(1 + cosh ρ)`: `1 − 2M/r = tanh²(ρ/2)` and `r′²/(1 − 2M/r) = 4M²cosh⁴(ρ/2)` | 80–150 | 0.9 | `Complex.tan` through `sin/cos` |
| 5a | At `z = π + iρ′`: `−4M²cos⁴(z/2)·(−1) = 4M²sinh⁴(ρ′/2)` and `tan²(z/2) = −coth²(ρ′/2)`. With `r = M(1 − cosh ρ′)`: `1 − 2M/r = coth²(ρ′/2)` and `r′²/(1 − 2M/r) = 4M²sinh⁴(ρ′/2)` | 80–150 | 0.9 | as 4a |
| 2b | The 4D interior form: `g_tt = 2M/r − 1 = tan²(η/2)`, `g_rr r′² = −4M²cos⁴(η/2) = −(dτ/dη)²` and `r² = M²(1 + cos η)²` on `(0, π)`, so both of P2's forms (`eq:interior_metric` and `eq:interior_metric_eta`) hold, with the sphere factor written in as in campaign 110 | 100–150 | 0.85 | ① |

**Arithmetic checked in advance:**
- `dτ/dη = M(1 + cos η) = 2M cos²(η/2)`.
- `dr/dτ = −M sin η / (M(1 + cos η)) = −tan(η/2)`, so `(dr/dτ)² = tan²(η/2) = (1 − cos η)/(1 + cos η) = 2M/r − 1`.
- The geodesic check for a diagonal 2D metric with `t′ = 0`: the `t` equation reads `2Γᵗ_tη t′η′ = 0`. The `η`
  equation is the derivative of `g_ηη η′² = −1`. `Γᵗ_ηη = 0` because `g_ηη` does not depend on `t`.
- At `z = π + iρ′`: `cos(z/2) = −i sinh(ρ′/2)`, so `cos⁴ = sinh⁴`.
- `(1 − cosh)²/(… )`: `1 − 2M/r = (1 + cosh ρ′)/(cosh ρ′ − 1) = coth²(ρ′/2)`.

**Expected stop: 1a-③**, evaluating `kr_Γ` (the matrix inverse and `kr_pd` of `cos⁴` and `tan²`) along `c`.
- **Fallback:** close the Christoffel symbols of a diagonal `2 × 2` metric `diag(a(η), b(η))` in general first, then
  evaluate at `a = −4M²cos⁴(η/2)` and `b = tan²(η/2)`.
- **If that also stops,** 1a stays BUILT IN PART at ①–②.

**Interpretive, not formalised:** 6d ("a single analytic curve", "maximal analytic completion") and 8b. 6b (the four
`r ≥ 0` patches are exactly Kruskal) and 2a, 4b and 5b (pullbacks into the manifold) are not in this campaign.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

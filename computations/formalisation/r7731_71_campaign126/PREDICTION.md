# `r7731+71.1` — PRE-REGISTRATION: campaign 126, **P8's three leaves (rows 5a–c, `prop:trichotomy`), which close P8, and 60's two stale headers**. ⌗ `500` new lines (band 300–850), p `0.55`. **Expected stop:** the pullback metric, i.e. the partial derivatives of the embeddings' three-variable products

*Registered before any Lean.*
- **Everything goes into `probes/StaticEinstein.lean`, the file P8 cites,** in a new `section LfLeaves`. New names
  are prefixed `lf_`. The `kr_` kit already in the file is used as it stands.
- **The substrate:** `η(X, Y) = −X₀Y₀ + X₁Y₁ + … + X₄Y₄` on `Fin 5 → ℝ`, and the hyperboloid `η(X, X) = α²`.
- **The induced metric** of a chart `Φ : (Fin 3 → ℝ) → (Fin 5 → ℝ)` is `g_ij = Σ_A ε_A ∂_iΦ^A ∂_jΦ^A`, with
  `∂ = kr_pd` and `ε = (−1, 1, 1, 1, 1)`.

## One curvature theorem for the curved leaves

| Item | Statement | Lines | p |
|---|---|---|---|
| `lf_curv` | For `g = R² diag(1, S(χ)², S(χ)² sin²θ)` on `Fin 3`, with `S′` differentiable, `S″ = −kS` and `S′² + kS² = 1`, at a point with `S(χ) ≠ 0` and `sin θ ≠ 0`: `R_{abcd} = (k/R²)(g_ac g_bd − g_ad g_bc)` for all 81 `(a, b, c, d)`. Constant sectional curvature `k/R²` | 150–300 | 0.7 |
| `lf_pull` | The induced metric of `Φ = (U₀(χ), U₁(χ), R S(χ) n̂(θ, φ))` is `diag(−U₀′² + U₁′² + R²S′², R²S², R²S² sin²θ)` | 100–200 | 0.6 |

## Rows

| Row | Statement | Lines | p |
|---|---|---|---|
| 5a | On the hyperboloid, `X₀ = c` ⟺ `X₀ = c` and `X₁² + … + X₄² = α² + c²`. The chart `(c, R cos χ, R sin χ n̂)`, `R = √(α² + c²)`, lies on it and induces `R²(dχ² + sin²χ dΩ²)`. By `lf_curv` with `S = sin`, `k = 1`: curvature `+1/(α² + c²)` | 40–80 | 0.85 |
| 5b | For the null `B = (1, 1, 0, 0, 0)` and `s ≠ 0`: the chart `y ↦ (X₀(y), X₁(y), y)` with `X₁ − X₀ = s` and `X₁ + X₀ = (α² − |y|²)/s` is a bijection from `ℝ³` onto `{hyperboloid, η(X, B) = s}`. Its induced metric is `δ_ij`, so every `R^a_{bcd} = 0`: curvature `0` | 60–120 | 0.8 |
| 5c | On the hyperboloid, `X₁ = b` gives `X₀² − (X₂² + X₃² + X₄²) = b² − α²`. For `b > α`, `X₀ ≠ 0` there (two sheets). The chart `(A cosh ρ, b, A sinh ρ n̂)`, `A = √(b² − α²)`, lies on it and induces `A²(dρ² + sinh²ρ dΩ²)`. By `lf_curv` with `S = sinh`, `k = −1`: curvature `−1/(b² − α²)` | 40–80 | 0.85 |
| 5d | "They carry `k = +1, 0, −1`": the curvature signs are `lf_curv`'s `k`. The FLRW reading of `k` stays interpretive. **No formal core**, as surveyed | — | — |

**Non-vacuity:** each chart is evaluated at a concrete point (e.g. `χ = θ = π/2`) where the hypotheses hold.

## 60's two stale headers

- **`OperatorKernel.lean`:** "It backs P8: `thm:kernel` and `prop:bend`" becomes a statement that the file is
  superseded by `StaticEinstein.lean` as P8's citable file. This is a docstring change only.
- **`StaticEinstein.lean`:** the kept campaign-123 header's "it copies no earlier probe" is marked as the header of
  the copied campaign-123 section, which is false of the whole file.

**The expected stop** is `lf_pull`: `kr_pd` of `R S(y₀) sin(y₁) cos(y₂)` and its siblings in each of three
coordinates. **The fallback** is to state the two curved leaves' induced metrics separately, by direct
computation, without the general `lf_pull`. If `lf_curv` stalls, the fallback is the Ricci form
`R_{bd} = 2(k/R²) g_bd` with 5a and 5c marked BUILT IN PART.

**Interpretive, not formalised:** the FLRW identification of `k` (5d) and the open slicing eq. `openembed`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

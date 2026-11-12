# `r7747+71.1` — PRE-REGISTRATION: campaign 134, **P9's Kerr rows: Kerr–de Sitter is vacuum-Λ (4a), its limits (4b), the constant-curvature `M = 0` member (4c), the structure functions (4d) and `J` (4e)**. ⌗ `1100` new lines (band 700–1600), p `0.45`. **Expected stop:** `field_simp; ring` on the ten Ricci components

*Registered before any Lean. The inventory is `r7745_71_survey/SURVEY.md`, which priced 4a at 1500–4000, p 0.3. The
re-price comes from a sympy pass (not Lean): in the chart below the Christoffel table has **20** independent non-zero
entries, each a rational function of `(r, x)` with numerators of degree ≤ 10.*

- **The probe:** append to `probes/Range.lean` (`rn_kds_`), P9's citable file. Mathlib only.
- **The chart.** Boyer–Lindquist `(t, r, θ, φ)` with the polar coordinate replaced by `x = cos θ`, so
  `dθ² = dx²/(1 − x²)` and `sin²θ = 1 − x²`. Every component is then rational in `(r, x)`, with no trigonometry.
  `x = cos θ` is a diffeomorphism of `(0, π)` onto `(−1, 1)`. **The transfer of `R_μν = Λg_μν` back to the θ chart
  is not formalised**, and the RESULT will say so in terms.
- **The metric:** `ρ² = r² + a²x²`, `Δ_r = (r² + a²)(1 − Λr²/3) − 2Mr`, `Δ_x = 1 + Λa²x²/3`, `Ξ = 1 + Λa²/3`, and
  `g = −(Δ_r/ρ²Ξ²)(dt − a(1−x²)dφ)² + (Δ_x(1−x²)/ρ²Ξ²)(a dt − (r²+a²)dφ)² + (ρ²/Δ_r)dr² + (ρ²/(Δ_x(1−x²)))dx²`.
- **The method.**
  - A generator (Python, recorded with the result) emits each `HasDerivAt` proof structurally from the expression
    tree and closes it with `congr_deriv` by `field_simp; ring`.
  - `kr_Γ = table` on the open set `ρ² ≠ 0`, `Δ_r ≠ 0`, `x² ≠ 1` (`Δ_x, Ξ > 0` for `Λ ≥ 0`), as in `rn_Hyp.U`.
  - The ten Ricci components are closed by `field_simp; ring`.

## Rows

| Row | Statement | Lines | p |
|---|---|---|---|
| 4a | `rn_Ric (rn_kds a M Λ) y μ ν = Λ · rn_kds a M Λ y μ ν` for all 16, at every point with `ρ² ≠ 0`, `Δ_r ≠ 0`, `x² ≠ 1`, `Λ ≥ 0`. **Non-vacuity:** a point with `a, M, Λ ≠ 0` satisfying the hypotheses | 800–1300 | 0.45 |
| 4b | `a = 0`: the metric is SdS, `diag(−f, 1/f, r²/(1−x²), r²(1−x²))`, `f = 1 − 2M/r − Λr²/3`, component by component. `a = M = 0`: static de Sitter. (`M = 0`, `a ≠ 0` is de Sitter by 4c.) | 40–80 | 0.9 |
| 4c | `M = 0`: `R_{abcd} = (Λ/3)(g_ac g_bd − g_ad g_bc)`, all 256 | 100–250 | 0.5 |
| 4d | `Δ_r = r²f_SdS + a²f_dS`, `Δ_θ = 1 + (a/α)²cos²θ`, `Ξ = 1 + (a/α)²` with `α² = 3/Λ` | 20–40 | 0.95 |
| 4e | `J = Ma/Ξ²` is zero iff `M = 0` or `a = 0` | 10–20 | 0.95 |

**The expected stop** is `field_simp; ring` on the Ricci components: the risk is time-out, not falsity. **Fallbacks,
in order:** (i) split each component by hand into a common-denominator numerator, the polynomial identity proved by
`ring`; (ii) the `M = 0` case (4c's Ricci) only; (iii) the equatorial reduction. Any fallback marks 4a BUILT IN PART
with the gap named.

**Interpretive, not formalised:** "the offset taken in a twisted slice", and the sharing of the throat beyond
`α² = 3/Λ`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

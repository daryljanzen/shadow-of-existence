# `r7749+71.1` — PRE-REGISTRATION: campaign 135, **P9's last cored rows: the Carter "iff" (5), vacuum Bianchi I (7a), its type I (7b), and the pp-wave's type N (8b)**. ⌗ `1700` new lines (band 1200–2400), p(all four BUILT) `0.25`

*Registered before any Lean. The inventory is `r7745_71_survey/SURVEY.md`, as corrected in `r7747_71_campaign134/RESULT.md`:
17 rows, 13 cored, 9 BUILT. A sympy pass (not Lean) on `eq:carter` confirms `thm:pd`'s two cleared equations. With
the quartics substituted, every component of `R_μν − Λg_μν` is `(c₀ − d₀)` times a rational function. So the "iff"
holds as stated, and both directions are priced as buildable.*

- **The probe:** append to `probes/Range.lean`, P9's citable file, with prefixes `car_`, `bi_` and `pw_`. Mathlib only.
- **The method:** campaign 134's generator, re-parametrised with **abstract** structure functions.
  - `Δ_r = R(r)` and `Δ_p = P(p)` come with global `HasDerivAt` hypotheses `R′ = R1` and `R1′ = R2` (likewise for `P`).
    The atoms are `Σ = r² + p²`, `R` and `P`.
  - Lean checks every emitted lemma; nothing rests on sympy.

## Rows

| Row | Statement | Lines | p | Expected stop |
|---|---|---|---|---|
| 5 "if" | On `(τ, σ, r, p)` with `eq:carter`: if `Δ_r, Δ_p` are the quartics of `eq:quartics` (with `d₀ = c₀`), then `R_μν = Λg_μν` for all 16 wherever `Σ, Δ_r, Δ_p ≠ 0`. This is via the abstract Ricci tensor: all 16 components in terms of `R, R1, R2, P, P1, P2`. **Non-vacuity:** Kerr–de Sitter's own coefficients at a non-degenerate point, with `c₁, c₀, d₁ ≠ 0` | 600–1000 | 0.6 | `field_simp; ring` on the abstract Ricci, now with six function atoms |
| 5 "only if" | On an open rectangle `I × J` where `Σ, Δ_r, Δ_p ≠ 0`: if `R_rr = Λg_rr` and `R_pp = Λg_pp` hold throughout, then there are `c₀, c₁, c₂, d₁` with `Δ_r = −Λr⁴/3 + c₂r² + c₁r + c₀` on `I` and `Δ_p = −Λp⁴/3 − c₂p² + d₁p + c₀` on `J`. The steps are the separation of eq. `separated`, two integrations on an interval, and `d₀ = c₀` from the `rr` component | 200–400 | 0.5 | The interval integrations (`deriv = 0` ⇒ constant on a preconnected open set) |
| 7a | `ds² = −dt² + Σ aᵢ²dxᵢ²`, `aᵢ = sinh(3t)^{1/3} tanh(3t/2)^{Cᵢ/3}` (`Real.rpow`), `Λ = 3`, `ΣCᵢ = 0`, `ΣCᵢ² = 6`, at `t > 0`: `R_μν = 3g_μν`, all 16. Internally `aᵢ = exp(qᵢ)`, with `qᵢ′ = coth 3t + Cᵢ/sinh 3t` | 150–350 | 0.65 | The `rpow` ↔ `exp ∘ log` bridge and `d/dt log tanh(3t/2) = 3/sinh 3t` |
| 7b | Type I. **Target:** `I³ ≠ 27J²` from the Weyl tensor, for distinct `Cᵢ`. **Expected:** BUILT IN PART, as `pw_Weyl` (the 4-D Weyl tensor) plus Bianchi I's three electric eigenvalues `C^{ti}{}_{ti}`, pairwise distinct iff the `Cᵢ` are, two equal when two `Cᵢ` are (Type D). The link from distinct eigenvalues with zero magnetic part to `I³ ≠ 27J²` is not formalised | 120–300 | 0.45 | The Levi-Civita contraction for `I` and `J` |
| 8b | The pp-wave with harmonic `H`: Weyl = Riemann; the Weyl bivector operator squares to zero (`C^{ab}{}_{cd}C^{cd}{}_{ef} = 0`, all 256); `kr_K = 0`. **Non-vacuity:** `H = x² − y²` has Weyl ≠ 0. **Target:** `I = J = 0` with `ε` built as a determinant of unit rows. **Fallback:** nilpotency alone, BUILT IN PART with the `I, J` step named | 120–300 | 0.45 | The `ε` contraction |

**If the Carter "only if" stops,** 5 is marked BUILT IN PART with "if" built, and the stop is named. **If 7b and 8b stop at
the `ε` contraction,** both are marked BUILT IN PART, with the electric eigenvalues and the nilpotency as what is built.

**Interpretive, not formalised:** `cor:carter`, `rem:carter-chain`, "high symmetry forbids it" (Birkhoff and the Weyl
class), and Zipoy–Voorhees (not in the inventory's rows).

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

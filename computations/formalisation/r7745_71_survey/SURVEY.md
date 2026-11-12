# Inventory of the seventh paper, P9 (`corpus/range_paper.tex`): `r7745+71.1`

*An inventory, not a campaign. 69 ordered P9 (r7745). The corpus is read at `ad0a30ff` and the probes through campaign
132. Marks as before. Prices are new lines; p is the chance of success.*

**Notation:** `8πT^μ_ν = G^μ_ν + Λδ^μ_ν`.

The grep finds **11** statements, split into **16 rows**. 9 rows have a formal core.

## 1. `thm:bound` (l.139)
- **1.** Invariance of a generated geometry under the sweep subgroup. **No formal core:** it holds by construction.

## 2. `prop:surj` (l.155)
- **2.** Function counting. **No formal core.**

## 3. `prop:ksvac` (l.175) and eq. `ks`, `ksrho`
- **3a.** For `ds² = −dτ² + X(τ)²dχ² + Y(τ)²dΩ²`, the mixed Einstein tensor is diagonal, with:
  - `−G^τ_τ = (Y′/Y)² + 1/Y² + 2(X′/X)(Y′/Y)`;
  - `G^χ_χ = −2Y″/Y − (Y′/Y)² − 1/Y²`;
  - `G^θ_θ = G^φ_φ = −Y″/Y − X″/X − (X′/X)(Y′/Y)`.
  - These are eq. `ksrho` and its partners.
  - **NOT BEGUN.** 250–450, p 0.65. **Stop:** the Christoffel table in `τ` and `θ`.
- **3b.** The SdS interior is vacuum: `Y′² = −f(Y)`, `X = Y′`, `f = 1 − 2M/Y − ΛY²/3`. **NOT BEGUN.** 60–120, p 0.8.
- **3c.** The Nariai member is vacuum: `Y = 1/√Λ`, `X = e^{√Λτ}`. **NOT BEGUN.** 30–60, p 0.9.

## 4. `prop:kerr` (l.191)
- **4a.** Kerr–de Sitter has `R_μν = Λg_μν`, from the coordinate Riemann tensor of the non-diagonal Boyer–Lindquist
  metric. **NOT BEGUN.** **The corpus's hardest target.** Priced below.
- **4b.** The limits: `a → 0` gives SdS and `M → 0` gives de Sitter, metric component by component. **NOT BEGUN.** 40–80,
  p 0.9.
- **4c.** At `M = 0`, `a ≠ 0`, the Riemann tensor is the constant-curvature form. **NOT BEGUN.** It rides on 4a.
- **4d.** `Δ_r = r²f_SdS + a²f_dS`, `Δ_θ`, `Ξ`: algebraic identities. **NOT BEGUN.** 20–40, p 0.95.
- **4e.** `J = Ma/Ξ²` vanishes iff `M = 0` or `a = 0`. **NOT BEGUN.** 10–20, p 0.95.

## 5. `thm:pd` (l.212)
- **5.** The Carter-form cut is vacuum-`Λ` iff `Δ_r` and `Δ_p` are the stated quartics. **NOT BEGUN.** This is beyond 4a:
  an "iff" over two free functions.

## 6. `cor:carter` (l.234)
- **6.** The Killing tensor reading. **No formal core** as stated.

## 7. `prop:typeI` (l.280)
- **7a.** The vacuum-`Λ` Bianchi-I solution with `a_i = sinh(3t)^{1/3} tanh(3t/2)^{C_i/3}`. **NOT BEGUN.** 200–400, p 0.5.
  **Stop:** real powers, `Real.rpow`.
- **7b.** Petrov type I. **NOT BEGUN.** It needs the Weyl invariants.

## 8. `prop:radiative` (l.290)
- **8a.** The pp-wave `ds² = H du² − 2du dv + dx² + dy²` with `H(u, x, y)` has `R_uu = −½(H_xx + H_yy)` and all other
  `R_μν = 0`. So it is vacuum iff `H` is harmonic in `(x, y)`. **NOT BEGUN.** 120–250, p 0.7.
- **8b.** `I = J = 0` with the Weyl tensor non-zero (type N). **NOT BEGUN.** 200–400, p 0.5.

## 9. `thm:range`, `cor:wall`, `cor:radiation`
- **9.** The range statements. **No formal core** as stated.

## Totals
- **16 rows**, 9 with a formal core. Within reach now: 3a, 3b, 3c, 4b, 4d, 4e and 8a.
- **Marks:** 0 BUILT, 0 BUILT IN PART, 9 NOT BEGUN, and 7 with no formal core.

## The Kerr–de Sitter attempt (4a), priced before building
- **The metric:** Boyer–Lindquist `(t, r, θ, φ)`, `g = g(r, θ)`, with the cross term `g_tφ ≠ 0`. The inverse is
  block-diagonal: a `(t, φ)` 2×2 block and a diagonal `(r, θ)` block.
- **The plan:**
  - Use `kr_` on `Fin 4` with Christoffel entries named as functions of `(r, θ)`.
  - Unlike P8, the entries depend on two variables, so each `kr_pd` needs a two-variable `HasDerivAt`.
  - Prove `R_μν = Λg_μν` component by component: 10 independent components, with the off-block ones vanishing
    structurally.
- **Price:** 1500–4000 lines, p 0.3.
- **The stop:** `field_simp` on the Ricci components. Each is a rational function of `r`, `cos θ`, `a`, `M` and `α` with
  large numerators, and the risk is that the final `ring` normalisation times out.
- **The fallback:**
  - Prove the `M = 0` case first (4c, constant curvature), where `Δ_r` is quadratic.
  - Or prove the equatorial reduction `θ = π/2` (still non-diagonal).
  - Mark 4a BUILT IN PART with the gap named.

## Campaign order
- **133:** 3a, 3b, 3c and 8a, in a new probe `probes/Range.lean`.
- **134:** 4b, 4d, 4e and the registered attempt at 4a.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

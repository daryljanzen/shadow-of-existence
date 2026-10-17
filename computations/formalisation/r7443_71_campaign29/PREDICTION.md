# `r7443+71.3` — PRE-REGISTRATION: campaign 29, row 59's last piece: section E's non-constant `H4` series and its integrals. ⌗ `380` lines (band 200–750), ⛔ stop `1000`. ⌗ p `0.50`

*Under `r7443` ②. The receipt's section E was re-read. Pricing was done in sympy before this registration, and no
Lean was written before it.*
- *In the left-invariant frame on `S³` (`e = σ/2`), the brackets are `[X_a, X_b] = 2 ε_abk X_k`.*
- *`X_a Rad = Rad · L_a` with `(L_a)_jk = −2 ε_ajk`. So `H4`'s frame components, which are polynomials in `Rad`'s
  first row `u`, have frame derivatives that are again polynomials in `u`.*
- *The frame metric is `exp(εH4)`, with inverse `exp(−εH4)`, and both are polynomial. The frame Koszul formula then
  gives the scalar series as polynomials in `u`:*
  - *`6, 0, −10u₀² − 10u₁² − 4u₂², −(4/3)u₀³ + 4u₀u₁², −5u₀⁴ − 10u₀²u₁² − 2u₀²u₂² − 5u₁⁴ − 2u₁²u₂²`;*
  - *over the Euler box with `sin θ/8`, these integrate to the receipt's `12, 0, −16, 0, −88/15` times `π²`, exactly.*
- *The intermediate tables are small: at most `36` terms per order.*

## ① The piece: `probes/Row59Series.lean`

- ***(E1) `frame_series`.*** Take any field `K` of characteristic zero, three derivations `D_a` (additive, Leibniz,
  killing rationals), and `u : Fin 3 → K` with `D_a u = u L_a`.
  - The frame metric is `G = Σ εᵏ Hᵏ/k!`, with `H = H(u)` the receipt's `H4`. Its inverse is `Σ (−ε)ᵏ Hᵏ/k!`.
  - The Christoffel series is taken from the frame Koszul formula with `c = 2ε`. The scalar series is
    `R(X_a, X_b)X_c` from it, then traced, as truncated Cauchy products.
  - Claim: its coefficients `0..4` are the five polynomials above.
- ***(E2) `rad_row_frame`, the chart link.*** The actual functions `u = Rad 0 ·` on the Euler chart satisfy
  `∂_k u_j = Σ_a (u L_a)_j eL[a, k]` for every `k, j`. That is, `du_j = Σ_a (u L_a)_j σ^a`, the relation (E1) assumes,
  with real derivatives.
- ***(E3) `section_e_integrals`.*** The five polynomials at `u = Rad 0 ·`, integrated over `[0, 2π] × [0, π] × [0, 4π]`
  with `sin θ/8`, give ***`12π², 0, −16π², 0, −(88/15)π²`***.

***Caveats, registered.***
- ***The frame Koszul formula is taken as the definition of the scalar curvature***, as Milnor's formula was in
  campaign 24, now with non-constant components. It is not linked to `ShadowEngine`'s `curv` by import.
- ***(E1) is stated over a field.*** The chart's functions form a ring, not a field, and the relations (E2) proves are
  what (E1) uses. Instantiating (E1) on those functions is argued, not built. Every expression (E1) evaluates is a
  polynomial in `u` with rational coefficients.
- The series is the receipt's truncation at `ε⁴`, and `exp` is not used.

***Failable:*** BUILT, BUILT IN PART (scored per piece E1, E2, E3), or REPORTED. p `0.50` for all three.
- ***Risk:*** the trig integrals in (E3), and the derivative bookkeeping in (E1).

***Census if BUILT:*** row 59's "still to build" empties. It moves to `DONE`, with the imported TT labels and the
stated caveats in its text. Its `decl` gains the new names in the same push.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

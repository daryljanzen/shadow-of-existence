# `r7423+71.1` — PRE-REGISTRATION: campaign 25, row 66's `ε`-series of `R(exp εH)` and the split algebra. ⌗ `140` lines (band 70–300), ⛔ stop `400`. ⌗ p `0.65`

*Daryl's standing instruction: build. Row 66 is `DONE (chartable half)`. Its open half names "the `ε`-series of
`R(exp εH)` and the split algebra", the deficiency claim (prose), and the imported TT spectrum. The receipt
(`P10_the_kinetic_cubic_vertex_is_a_split_artefact…`) was read for this campaign, sections B–E. One scoping check
was made with sympy before this registration: MTW's identity holds EXACTLY, not only to third order.*

## ① The piece: `probes/Row66Series.lean`

- ***(E) the series, for every traceless `H`:*** in an eigenframe, Milnor's `R` at `λ = exp(εhᵢ)` with
  `h₁ + h₂ + h₃ = 0` is the exponential sum `4 Σ_{i<j} e^{ε(hᵢ+hⱼ)} − 2 Σ e^{2εhᵢ}`. Its `R⁽ⁿ⁾(0)/n!` for
  `n = 0..4` are `6, 0, −2p₂, −(10/3)p₃, −(7/6)p₄` with `pₖ = Σ hᵢᵏ`, and `(7/6)p₄ = (7/12)p₂²`. This is the
  receipt's `6 − 2 tr h² − (10/3) tr h³ + O(h⁴)`, carried one order further. The eigenframe reduction is the
  receipt's own SO(3)-covariance step, and it is stated as such: Milnor's `R` depends only on the invariants.
- ***(E′) MTW, exactly:*** `R[exp 2β] = 6(1 − V(β))` for the Bianchi IX potential `V(β₊, β₋)`, as an identity for
  all `ε`. The receipt checks it through cubic order only.
- ***(D) the split algebra:*** `tr(Ḃ[Ḃ, A]) = 0` for all `3 × 3` matrices, the receipt's "trace of a commutator".
  The cubic term of the volume-preserving split vanishes by exactly this identity.

***Not built:*** the kinetic series of `tr((g⁻¹ġ)²)` for non-commuting `h(t)`, which needs derivatives of the
matrix exponential; and the linear-split coefficient `−2 tr(h ḣ²)`. Both stay in row 66's open half, named.

***Failable:*** BUILT (E, E′, D), BUILT IN PART, or REPORTED. p `0.65`.
- ***Risk:*** order-4 `iteratedDeriv` over a six-term exponential sum with symbolic exponents, closed by
  polynomial identities under `h₃ = −h₁ − h₂`.

***Census if BUILT:*** row 66 stays `DONE (chartable half)`. Its open half shrinks to the kinetic series of the
non-commuting split, the deficiency prose and the imported spectrum. The `decl` cell gains the new names in the
same push.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

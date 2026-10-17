# `r7437+71.1` — PRE-REGISTRATION: campaign 27, row 66's kinetic series for non-commuting modes, in both splits. ⌗ `150` lines (band 80–320), ⛔ stop `450`. ⌗ p `0.60`

*Daryl's instruction, in session: "Build it" (row 66's non-commuting kinetic series, offered last turn). The receipt
(`P10_the_kinetic_cubic_vertex_is_a_split_artefact…`) was re-read at sections C–D. One scoping check was made with
sympy before this registration. At `h = M₁ = diag(1, −1, 0)`, `ḣ = M₂` (the receipt's two non-commuting modes), the
truncated series `tr(u²)` gives:*
- *volume-preserving split: orders `0..4` are `0, 0, 4, 0, 5/6`;*
- *linear split: orders `0..4` are `0, 0, 4, 2, 4`, with `−2 tr(hḣ²) = 2`.*

## ① The piece: `probes/Row66Kinetic.lean`

- ***The object, as the receipt computes it.*** A matrix series truncated at `ε⁴` is a sequence of `3 × 3` matrices,
  multiplied by the truncated Cauchy product.
  - The volume-preserving split: `g = Σ (εh)ᵏ/k!` and `g⁻¹ = Σ (−εh)ᵏ/k!`. `ġ` is taken term by term, with
    `d(hᵏ) = Σᵢ hⁱ ḣ hᵏ⁻¹⁻ⁱ`, with `h = A` and `ḣ = B` as independent matrices.
  - The linear split: `g = 1 + εh`, `g⁻¹ = Σ (−εh)ᵏ`, `ġ = εḣ`.
  - In both, `u = g⁻¹ ġ` and the kinetic series is `tr(u ⋆ u)`.
- ***(C) volume-preserving split, for all `A, B`:***
  - order 2 is `tr(B²)`;
  - ***order 3 vanishes identically***;
  - `tr u` vanishes at orders 1 and 2 when `tr B = 0`.
- ***(D) linear split, for all `A, B`:***
  - order 2 is `tr(B²)`;
  - ***order 3 is `−2 tr(A B²)`.***
- ***Non-vanishing, at the receipt's `M₁, M₂`:***
  - the volume-preserving order 4 is `5/6 ≠ 0`, the receipt's "the first kinetic correction is a quartic";
  - the linear order 3 is `2 ≠ 0`, the receipt's "the sym(π²φ) structure exists or does not according to the split".

***Caveats, registered.***
- `ḣ`'s term-by-term derivative is the Leibniz expansion, taken as the definition, as in the receipt's symbolic
  differentiation. It is not derived from `HasDerivAt` on matrix-valued functions.
- The series is the receipt's truncation at `ε⁴`, not `Matrix.exp`.
- The linear split's `√det g` factor is `1 + O(ε²)` for traceless `h`, so it cannot reach order 3. That step is
  argued, not built.

***Failable:*** BUILT, BUILT IN PART, or REPORTED. p `0.60`.
- ***Risk:*** the order-3 identities over generic `3 × 3` entries, which expand to many terms before `ring` closes
  them.

***Census if BUILT:*** row 66 stays `DONE (chartable half)`. Its open half drops the non-commuting kinetic series and
keeps the deficiency prose and the imported spectrum. Its `decl` gains the new names in the same push.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

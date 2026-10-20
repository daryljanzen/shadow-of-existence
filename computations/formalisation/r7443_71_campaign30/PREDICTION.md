# `r7443+71.5` — PRE-REGISTRATION: campaign 30, row 20, the first general identity: the receipt's computed half, and the contracted Bianchi identity it rests on. ⌗ `150` lines (band 80–320), ⛔ stop `450`. ⌗ p `0.65`

*Under `r7443` ②, step 2. The receipt (`L801…/N1_the_nonlinear_freedom_is_the_general_first_class_structure.py`)
was re-read in full, and no Lean was written before this registration.*

***A finding first, read from the tree.*** Row 20's need is "index algebra over an arbitrary (non-diagonal) metric",
and the receipt's mechanism is the contracted Bianchi identity, which it calls "an off-shell geometric identity,
true for every metric". That identity is already built:
- `contracted_bianchi` in `probes/Bianchi2.lean` (row 6, `r7353+71.8`), for THE connection of ANY smooth symmetric
  nondegenerate metric on `ℝⁿ`.
- Row 20's text predates it and was never moved.

So the general half is cited, not rebuilt. The pieces below are what the receipt computes beside it.

## ① The piece: `probes/Row20Freedom.lean`

- ***(1) `tt_waves`.***
  - The four polarisation tensors `e₁₊, e₁ₓ` (along `k₁ = k ẑ`) and `e₂₊, e₂ₓ` (along `k₂ = k x̂`) are each
    trace-free and transverse to their own `k`.
  - `k₁ · k₂ = 0` and `k₁ × k₂ ≠ 0`: the directions are not parallel.
- ***(2) `superposition_transverse`.*** For arbitrary complex amplitudes `A₁, A₂`, the superposition
  `A₁(e₁₊ + e₁ₓ) e^{i k z} + A₂(e₂₊ + e₂ₓ) e^{i k x}` has `∂_j h_ij = 0` at every point, with real partial derivatives
  of the complex-valued field.
- ***(3) `mode_equation`.*** `u(η) = e^{−ikη}(1 − i/(kη))` satisfies `u'' + (k² − 2/η²) u = 0` exactly, for `η ≠ 0`
  and `k ≠ 0`, with `HasDerivAt` in `ℂ` over real `η`.
- ***(4) `shear_square`.*** `e:e = 2` for each polarisation and `0` across. With `σ = ½ ε ḣ e₊`, `σ² = ½ ε² ḣ²`,
  positive for `ε ḣ ≠ 0`, and `σ²/ε²` is independent of `ε`.

***Caveats, registered.***
- The polarized-leaf instance of `∇_μ G^{μν} = 0` is ***not*** rebuilt. `contracted_bianchi` covers every metric,
  and the receipt itself says it exhibits the general object. Its row-6 caveat carries over: the right side is
  `g^{ac} ∇_b R_ac`, not `∂_b R`.
- The receipt's paper-text checks (P11 and P9 phrases) are text pins, not mathematics, and they are not formalised.

***Failable:*** BUILT, BUILT IN PART, or REPORTED. p `0.65`.
- ***Risk:*** the second derivative of `u`, a complex quotient, in (3).

***Census if BUILT:*** row 20 → `DONE`. Its `decl` gains the new names and `Bianchi2.lean`'s `contracted_bianchi`,
in the same push.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

# `r7443+71.13` — PRE-REGISTRATION: campaign 34, library-gap rows 85 (the SdS tetrad and superpotential) and 80 (the Killing form on the dS₅ coset). ⌗ `260` lines (band 140–550), ⛔ stop `800`. ⌗ p `0.55`

*Under `r7443` ②, step 4, next in `PRICING.md`'s order. No Lean was written before this registration.*

## ① The pieces: `probes/LibGap85_80.lean`

***Row 85*** (`P14_B3_spinor_vielbein.py`), with `f = 1 − 2M/r − r²/α²`.
- ***`tetrad_metric`.*** Where `f > 0`, the tetrad `(√f dt, dr/√f, r dθ, r sinθ dφ)` gives
  `η_ab e^a e^b = diag(−f, 1/f, r², r² sin²θ)`.
- ***`superpotential_values`***, at `M = 0.12` and `α = 1`:
  - `√f/r` at `r = 1/2` agrees with the receipt's `1.0392305` to its printed digits;
  - `|f| < 10⁻⁹` at the two decimal horizon roots, and `|W| < 10⁻⁴` there (`W = λ√f/r`, at `λ = 1`, the receipt's
    value);
  - `W(−1/2) < 0`.
- ***`throat_check`*** is ***stated as what it is***. At `r = 1/1000`, `f < 0`, so the tetrad is not real there. The
  receipt's `|√f/r|` is a complex modulus, and it is built as `√|f|/r > 10³`. This is the fidelity trap the pricing
  found: a literal `Real.sqrt` port would read `0`.

***Row 80*** (`P12_coset_metric.py`).
- ***`killing_on_coset`.*** The 15 generators `M_μν` of `so(5,1)`, as integer `6 × 6` matrices, with
  `(M)_ρσ = δ_ρμ η_νσ − δ_ρν η_μσ`.
  - `ad` is computed by commutators and read back in the `M_μν` coordinates.
  - `B_ij = tr(ad_i ad_j)` restricted to `m = span{M_a5}` is ***`diag(8, −8, −8, −8, −8)`***: proportional to `η_ab`
    with constant `−8`, signature `(1, 4)`.

***Caveats, registered.***
- ***Row 85.*** The spin connection is not derived; the receipt solves it by hand in comments, and never computes
  it. The Dirac operator's separation (`λ = j + ½`, superpotential `λ ω²₁`) is imported, the spinor library's.
- ***Row 80.*** The quotient `SO(5,1)/SO(4,1)` as a manifold with an invariant metric is not built. That `B|_m` is its
  metric at the base point is the receipt's reading, imported.

***Failable:*** BUILT, BUILT IN PART (per row), or REPORTED. p `0.55`.
- ***Risk:*** the `15 × 15` `ad` traces without `native_decide`, and the decimal square-root bounds.

***Census if BUILT:*** rows 85 and 80 → `DONE`, with their imports named. `decl` is filled in the same push. That
gives library gap `12 → 10`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

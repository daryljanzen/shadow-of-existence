# `r7411+71.10` — PRE-REGISTRATION: campaign 23, the Euler-chart half of rows 66 and 67 under THE connection: `S³` in Euler angles as a non-diagonal `Fin 3` instance of the `r7351` engine. ⌗ `300` lines (band 180–600), ⛔ stop `750`. ⌗ p `0.50`

*Daryl's instruction: build. Rows 66 and 67 are `DONE (chartable half)` since `r7411+71.7`; their named open half
is the Euler-chart coordinate checks (structure equations, transversality via coordinate Christoffels), which wait
on "a non-diagonal `Fin 3` instance". That instance is this campaign. The receipts were read in full at `+71.2`.
Before registering I checked every target identity with sympy (scratch, not committed): the structure equations
hold in the receipt's convention `σ¹ = (0, cos ψ, sin ψ sin θ)`, `σ² = (0, −sin ψ, cos ψ sin θ)`,
`σ³ = (1, 0, cos θ)`, the divergence and trace vanish, and `R = 6`.*

## ① The piece: a new `section EulerS3` in `probes/NonDiag.lean` (the engine lives there; probes do not import each other)

- ***(A) The instance:*** `G = ¼ I + ¼ C(θ)(E₀₂ + E₂₀)` on `ℝ³` (coordinates `ψ, θ, φ`), with `C` ANY smooth profile
  with `C² < 1` everywhere (so the form is nondegenerate on all of `ℝ³`, which the engine requires; the Euler chart
  itself degenerates at the poles). Symmetry, smoothness, nondegeneracy, first and second partials.
- ***(B) The tables:*** inverse, `∂G`, `∂²G`, `Γ`, and Ricci as functions of `C, C′, C″` at the point; then THE
  connection's scalar curvature for EVERY such profile, `R = −2(4C³C″ − C²C′² − 4CC″ − 3C′²)/(1 − C²)²`.
- ***(C) The Euler chart:*** where the profile's 2-jet is `cos`'s (`C = cos θ`, `C′ = −sin θ`, `C″ = −cos θ`):
  `R = 6` and `Ric = 2G`. With a witness that such a profile exists at every `θ` off the poles (so (C) is not
  vacuous), and the eventually-equal form (`C = cos` near `θ` gives the jet).
- ***(D) Chart algebra:*** `G = ¼ Σₐ σᵃ ⊗ σᵃ` for the receipt's σ's; `det σ = sin θ`, `det G = sin²θ/64`; the
  structure equations `∂ᵢσᵃⱼ − ∂ⱼσᵃᵢ = −Σ εₐbc σᵇᵢ σᶜⱼ` (partials proved, not asserted); `G⁻¹`-trace of
  `hᵢⱼ = Σ Hₐb σᵃᵢ σᵇⱼ` vanishes for traceless `H`.
- ***(E) Transversality:*** `∇ⁱhᵢⱼ = 0` at the point, with `Γ` THE connection's (`lcGam`) and the partials of `h`
  proved, for every symmetric traceless constant `H`.

***Not built:*** the `ε`-series of `R(exp εH)` and the split algebra (row 66), the deficiency claim (prose), and
the imported TT spectrum (the spectral library gap).

***Failable:*** BUILT (A–E), BUILT IN PART, or REPORTED. p `0.50`.
- ***Risks:*** (E) is the heaviest identity (five free `H` entries through the `Γ` table and `σ`'s partials); and
  the witness in (C), which needs a smooth bounded reparametrisation and its second derivative.

***Census if BUILT:*** row 67 `DONE (chartable half)` → `DONE` (its only remaining item is the imported spectrum,
already the named library gap); row 66 stays `DONE (chartable half)`, with the coordinate checks moved out of its
open half.

## ② Compile

Priced `2–8` minutes for the section.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

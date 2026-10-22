# `r7503+71.1` — PRE-REGISTRATION: campaign 56, `r7489` ②, the three results that landed after the list was cut, each as a short exact Lean statement. ⌗ `900` lines in up to three probes (band 400–2000), ⛔ stop `2800`. ⌗ p: F-law `0.35`, P16 first integral `0.75`, P16 involution `0.65`

*Under `r7489` ② and `r7503`. Formalising landed results is consolidation work; `r7503` resumes it and bars only
new open-problem rows, and these are not rows. No Lean was written before this registration.*

## ① The pieces

***F — the full-sky law*** (`probes/FLaw.lean`). The receipt is
`P15_the_selective_quadrupole_suppression_is_the_skys_own_and_lcdm_carries_it_at_the_same_size.py`.
- For real `ν₁, ν₂ > 0`, let `X ~ χ²_{ν₁}/ν₁` and `Y ~ χ²_{ν₂}/ν₂` be independent. Then the law of `X/Y` has the
  `F(ν₁, ν₂)` density `f(r) = (ν₁/ν₂)^{ν₁/2} r^{ν₁/2−1} (1 + ν₁r/ν₂)^{−(ν₁+ν₂)/2} / B(ν₁/2, ν₂/2)` on `r > 0`.
- χ² is stated as the Gamma(`ν/2`, rate `1/2`) law. Use Mathlib's `gammaMeasure`/`gammaPDF` if present; otherwise
  define it by its density, normalised via `Real.Gamma`.
- ***Scope:***
  - the law, as a statement about the pushforward of the product measure. The receipt's numerical `p`-values
    (`stats.f.cdf` floats) are not claimed;
  - the scale form `R/(d₂/d₃) ~ F(5,7)` follows by a linear change of variable, and is stated as a corollary.

***I — the interior's first integral and the evenness*** (`probes/P16Interior.lean`). The receipt is
`P16_no_observable_reads_the_sign_of_the_radiation_amplitude.py`.
- `a(η) = (A/2)(1 − cos η) + √B sin η` satisfies `a′² = B + A a − a²` for all `η`.
- `a(−η; −√B) = a(η; √B)`, so every function of `a` taken along the solution is even in `√B`, up to reflecting
  `η`. Stated exactly as the receipt states it, and extended to the receipt's named observables where it lists them.

***V — the dust crossing's involution*** (`probes/P16Involution.lean`). The receipt is
`P16_the_crossing_is_an_involution_and_the_density_is_even_on_the_unsigned_radius.py`.
- The receipt's crossing map is an involution, and the density is even on the unsigned radius, as the receipt
  computes them.

***Failable,*** per piece: BUILT, BUILT IN PART, or REPORTED. ***Risk:*** F's change of variables and its Beta
normalisation, and whether Mathlib's gamma-distribution API is usable as is.

***Census:*** none of these is a ROWS.tsv row. They are recorded as formalised results in this campaign's RESULT,
for 69 to cite.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

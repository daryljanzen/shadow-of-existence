# `r7661+71.3` — RESULT: campaign 90 (b), `r7661` ②, **ℝ² × S¹ with a Rindler horizon, BUILT**. It is three-dimensional, and no chart of its atlas covers it. The Cauchy property is proved on `N` with no global chart, and every hypothesis of the accumulation and cone headlines is discharged. Tangency is instantiated at every horizon point. The registered expected stop was not hit. **The conformal-extension clause is REPORTED:** the obvious compactification is not conformal for this product metric. ⌗ `6312` lines in one probe (about `980` new, just under the band 1000–3500). ⌗ p `0.3`: came true for the registered pieces

*Against `PREDICTION.md` (`r7661+71.1`). 71 re-ran `lake env lean probes/CylinderWitness.lean`. It exits 0 with no
errors and no warnings. All `69` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`: `44` are kept
and `25` are new. The forbidden-token grep is clean. `check_no_sorry.py` reports ALL 29 THEOREMS COMPILE. The probe
copies campaign 90 (a)'s general theory but drops its `NModel` witnesses (campaigns 87–90a) to save compile time. They
stand in their own files.*

## The construction

- `N = (ℝ × ℝ) × Circle`, with Mathlib's stereographic charts on the circle, modelled on
  `E = (ℝ × ℝ) × EuclideanSpace ℝ (Fin 1)`.
- `cy_dim` gives `finrank E = 3`.
- `g = −dU dV + |dY|²` is defined intrinsically, with `Y : N → ℂ` the circle coordinate. `T = ∂_U + ∂_V`, and
  `M = univ`.

## The pieces — all BUILT

***The atlas.***
- **No chart covers `N`.** `cy_chart_ne_univ : ∀ x, (chartAt E x).source ≠ univ`, and also `cy_not_oneChart`.
- `cy_locallyOneChart` holds.

***The observer and the horizon.***
- The observer is `cy_O τ = (O' τ, 1)`, where `O'` is campaign 79's adapted reparametrisation.
- `hOD`, `cy_hmono` and `cy_JM` hold.
- `cy_D_eq`: `D = {U < 0}`. The proof uses a timelike step that winds round the circle.
- `cy_H_eq`: `𝓗⁺ = {U = 0} × S¹`, a null cylinder, with `cy_H_nonempty` and `cy_HM`.

***The Cauchy property on `N`*** — the registered expected stop, not hit.
- `cy_isCauchyTemporalOn` gives `Θ = −log(−U) + V`, proved by the registered route:
  - causal vectors project to causal vectors of the plane;
  - `cy_lip`: `‖ΔY‖ ≤ Δ(U+V)/2` along a causal curve;
  - `cy_converge`: inextendibility descends, because the circle is closed in `ℂ`;
  - campaign 81's `hl_cauchy_Θ₀` finishes.

***The headline and tangency.***
- `cy_witness_headline` discharges every hypothesis of `mh_causal_alignment_gh_N` and `mc_cone_kuratowski_N`, and
  concludes properness with `KLi = KLs = {U = 0}` for the slices and for the cones.
- Every slice is non-empty (`cy_slice_nonempty`).
- `cy_witness_tangency q` holds at every horizon point `q`, with `ℓ = ∂_V`, `n = 2∂_U` and the rate `−U/2 → 0`. The
  limit is `½ dU = −g(ℓ, ·)`.

## REPORTED: the conformal extension

`ι = (arctan U, arctan V, y)` is not conformal for `−dU dV + dy²`. A target metric `h(−du dv) + k dy²` with
`ι*g̃ = Ω² g` forces `k = Ω²` and `h = Ω²(1+U²)(1+V²)`. So either the circle shrinks to zero size at `𝒥⁺` or `h` blows
up there, and either way `𝒥⁺` does not sit in a Lorentzian `M̃`.

So `mx_prop_causal_alignment` is not instantiated on this `N`. Its accumulation, cone and tangency clauses are, with
`𝓗⁺ = ∂J⁻(O)`. A conformal compactification of this flat product would be a real construction, not a corollary.

## Stated in advance, and holding

`ℝ² × S¹` is homeomorphic to an open subset of `ℝ³`. The witness exercises an atlas no single chart of which covers the
space, in three dimensions. It does not exercise a space that no chart could cover.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

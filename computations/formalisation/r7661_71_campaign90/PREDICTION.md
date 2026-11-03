# `r7661+71.1` — PRE-REGISTRATION: campaign 90, `r7661` ②, the two witnesses the limits name. **(a) A genuine compactification is built first.** **(b) is corrected before any Lean:** the flat two-dimensional cylinder has no horizon for any observer, so it is replaced by ℝ² × S¹ with a Rindler horizon. ⌗ (a) `600` new lines (band 250–1500), p `0.6`; the curved stretch p `0.25`. ⌗ (b) `2000` new lines (band 1000–3500), p `0.3`, registered now and built after (a). **Expected stop for (a): `LocallyOneChart` and `ContMDiff ι` across two distinct types. For (b): the Cauchy property on `N` with no global chart to transport through**

*Under `r7661` ②. A new probe for (a), `probes/Compactification.lean`, copying campaign 89's `ConformalBoundary.lean`. No
Lean was written before this registration.*

## (a) A genuine compactification, `Ñ ≠ N`

***The construction.***
- `N = Pt`, the two-chart model, with `minkN`, so `g = −dU dV`.
- `Ñ = P`, the model space itself with its trivial one-chart structure. It is a different type from `Pt`.
- `St` on `Ñ` is flat, `g̃ = −du dv`.
- `ι(U, V) = (arctan U, arctan V)` through `φ`, so the closure of `ι(N)` is `[−π/2, π/2]²`, which is compact.
- `Ω² = 1/((1+U²)(1+V²))`, since `ι*g̃ = −dU dV / ((1+U²)(1+V²))`.

***The boundary and the horizon.***
- `𝒥⁺ = {v = π/2, −π/2 < u < 0}` is a segment of the null boundary.
- `I⁻_Ñ(𝒥⁺) = {u < 0, v < π/2}`, whose preimage is `D = {U < 0}`.
- So `∂J⁻(𝒥⁺) = {U = 0}`.

***What it shows.*** `mx_prop_causal_alignment` runs end to end with `Ñ ≠ N`, a relatively compact image, and a conformal
factor that is not constant in either variable.

***Stated in advance.***
- The observer `UV = −1` ends at `(0, π/2)`, the future end of the horizon on `𝒥⁺`, not at `i⁺ = (π/2, π/2)`.
- The Lean does not use `O(τ) → i⁺`.

***Stretch, p `0.25`: curved.***
- Give `N` the metric `−F dU dV` for any positive C¹ `F`. Schwarzschild's Kruskal `F` is the target.
- This needs conformal invariance of `TStep`, `CStep` and temporality on `N`, so the flat causal computations carry
  over, plus `F`'s C¹ chart representation.
- Schwarzschild's `F` itself needs campaign 80's `r(U, V)` brought in.

## (b) The cylinder, corrected

***Why the flat two-dimensional cylinder fails.*** Take `ℝ_t × S¹_x`, lifted to the universal cover. `I⁻(p)` is the
union over `k` of `{u < u_p − 2πk, v < v_p + 2πk}`. Along any future-inextendible observer `v → ∞` while `u` stays
bounded above, so taking `k → −∞` covers every point.
- So `D = N` and `𝓗⁺ = ∅`. The headline would hold only vacuously.
- A Rindler horizon `t = x` is not invariant under `x ↦ x + 2π`, so no horizon survives the quotient.
- This was my error in campaign 87's limits, carried into r7661.

***Replacement.*** `N = ℝ_t × ℝ_x × S¹_y` with `g = −dU dV + dy²` and the Rindler observer `UV = −1` at fixed `y`.
- The horizon `{U = 0} × S¹` is invariant under `y`, so `D = {U < 0} × S¹` and `𝓗⁺ = {U = 0} × S¹`, a null cylinder.
- `Θ = −log(−U) + V` is well defined.

***How it would be built.***
- `N` is Mathlib's product `ℝ² × Circle`, modelled on `ℝ² × EuclideanSpace ℝ (Fin 1)`, with stereographic charts on
  the circle.
- `LocallyOneChart` needs `g` C¹ through those charts, where `dy²` reads as `4 ds²/(1+s²)²`.
- The Cauchy property is proved on `N` by projecting to `(U, V)`:
  - causal vectors project to causal vectors, since `v_U v_V ≥ v_y²`;
  - the `y`-length of a causal curve is bounded by `(ΔU + ΔV)/2`, so inextendibility descends.

***Stated in advance.***
- `ℝ² × S¹` is homeomorphic to an open subset of `ℝ³`, so as a topological space it can be covered by one chart.
- No chart of its atlas covers it, so the witness exercises the multi-chart machinery. It does not exercise a space
  that cannot be covered by one chart; no flat spacetime with such a horizon is that simple.
- Being three-dimensional, it also shows the headline is not exercised only in two dimensions.

***Failable:*** each is BUILT, BUILT IN PART, or REPORTED, with the step that stopped.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

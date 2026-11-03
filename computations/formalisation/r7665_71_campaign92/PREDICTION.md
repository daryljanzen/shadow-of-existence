# `r7665+71.1` — PRE-REGISTRATION: campaign 92, `r7665`, two pieces in 69's order. ① The unbounded-stretch clause, stated formally, with an argument that the statement is P1's, then built. ② A three-dimensional witness `−dU dV + e^{2UV} dy²` whose Cotton tensor is non-zero. ⌗ ① `300` new lines (band 100–900), p `0.8`. ② `1300` new lines (band 600–3000): the causal witness p `0.6`; the Cotton tensor non-zero in coordinates p `0.4`; the invariance theorem (conformally flat ⟹ Cotton = 0) p `0.05`, REPORTED in advance as not attempted. **Expected stops:** ① the uniformity step on a compact subset of `𝓗⁺`; ② third derivatives of the metric, since the Lean has no curvature on `MSpacetime`

*Under `r7665`. Two new probes: `probes/HorizonStretch.lean` for ①, from campaign 91's `ConeDisjoint.lean`, and
`probes/WarpedWitness.lean` for ②, from campaign 91's `FourDWitness.lean`. No Lean was written before this
registration.*

## ① The unbounded-stretch clause

***P1's words.*** "the past light cones `∂J⁻(O(τ))` … converge to it as `τ → ∞`, the stretch of `𝓗⁺` they approach to
within any given distance extending to the future without bound".

***The formal statement.***

Take `N` with **any** metric `d` inducing its topology (`[MetricSpace N]`, the manifold structure on top). Define the
ε-stretch at time `τ` as `stretch τ ε := {q ∈ 𝓗⁺ | infDist q (cone O τ) < ε}`.
- **(S1) Uniform approach on compacts.** For every `ε > 0` and every compact `K ⊆ 𝓗⁺`, eventually in `τ`,
  `K ⊆ stretch τ ε`.
- **(S2) Unboundedness.** If `𝓗⁺` lies in no compact set, then for every `ε > 0` and every compact `K ⊆ N`, eventually
  `stretch τ ε ⊄ K`.

***Why this is P1's clause.***
- "The stretch they approach to within any given distance" is `stretch τ ε`, for a fixed `ε`.
- "Extends without bound" is (S1) and (S2): as `τ` grows, the ε-stretch comes to contain every bounded part of `𝓗⁺`,
  so it leaves every compact set.
- The statement holds for **every** compatible metric, so no choice of distance is smuggled in.

***Proof route.***
- (S1): campaign 88's Kuratowski lower limit gives the approach pointwise. `infDist · (cone τ)` is 1-Lipschitz, so a
  finite `ε/2`-cover of `K` makes it uniform. This is the expected stop.
- (S2) follows from (S1).

***"To the future", stated in advance.***
- The general theorem says the stretch is unbounded. It does not say the stretch runs *futureward along the
  generators*. That needs the generators' future inextendibility, which is not formalised.
- The witness shows the futureward direction explicitly:
  - `𝓗⁺ = {U = 0}` lies in no compact set;
  - for every `T`, eventually `stretch τ ε` contains a point with `V > T`;
  - `J⁺(q) ∩ 𝓗⁺` is unbounded for each `q ∈ 𝓗⁺`.
- The witness is on campaign 91's `ℝ⁴`, which is a metric space natively. A `Pt` metric instance is avoided because
  of the instance diamond with its charted topology.

***Not formalised:*** P1's proof says the cones approach "monotonically from outside". That is not in the statement.

## ② A witness that is not conformally flat

***Why this choice.*** In three dimensions a metric is conformally flat exactly when its Cotton tensor vanishes. A
sympy check (`cotton_check.py`) of `g = −dU dV + w(U,V)² dy²` finds:
- for `w = 1+U²`, `e^V`, `cosh V`, `2 + sin V` and `e^{U+V}`, the Cotton tensor **vanishes**: warping by one null
  coordinate, or by `U + V`, stays conformally flat;
- for **`w = e^{UV}`, it does not**: for example `C_{UUV} = −2V` and `C_{VUV} = 2U`.

***The causal witness, p `0.6`.***
- `N = ℝ³` as the model space, with `g = −dU dV + e^{2UV} dy²`, `T = ∂_U + ∂_V`, and a Rindler observer at `y = 0`.
- `D = {U < 0}` and `𝓗⁺ = {U = 0}`.
- `Θ = −log(−U) + V`, Cauchy on `N` by campaign 91's projection.
  - Causal vectors satisfy `v_U v_V ≥ e^{2UV} v_y²`, so `v_U, v_V ≥ 0`.
  - If the projection converges, it stays in a compact region where `e^{UV} ≥ c > 0`, so the `y`-length is bounded and
    inextendibility descends.
- Conclusions: every conclusion of the headline, ① above, and tangency with `ℓ = ∂_V`, `n = 2∂_U` and `W` spanned by
  `e^{−UV} ∂_y`.

***The Cotton tensor, p `0.4`.*** It is non-zero, computed in the global chart from the coordinate formulas. This needs
Christoffel symbols and the Schouten tensor by hand in Lean, to third derivatives of `e^{2UV}`.

***REPORTED in advance, p `0.05`.*** The invariance theorem, that a conformally flat metric has vanishing Cotton
tensor, is not attempted. Its transformation law under conformal rescaling and diffeomorphism is a substantial
formalisation of its own. So "not conformally flat" is proved only **modulo that standard theorem**, and RESULT will
say so.

***Failable:*** each piece is BUILT, BUILT IN PART, or REPORTED, with the step that stopped. Non-vacuity is mandatory.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

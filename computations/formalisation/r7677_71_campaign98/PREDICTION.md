# `r7677+71.1` — PRE-REGISTRATION: campaign 98, `r7677`. **The foundation fix:** Schwarzschild on EF's domain `W = {V > 0, UV < 1}` as an `Opens` manifold, with `𝓗⁺ = {U = 0, V > 0} ⊆ M`, and **the headline run on Schwarzschild** with the stationary `t`. Then **row 8**: both of `lem:alignment`'s slicings align with the generator. ⌗ The whole is `2000` new lines (band 1000–4000) at p `0.35`, as priced. ① foundation `600`, p `0.6`. ② `t` Cauchy and the headline `800`, p `0.45`. ③ stationary tangency `300`, p `0.7`. ④ retarded tangency `300`, p `0.6`. ④′ the retarded slicing's Cauchy property, a stretch, p `0.2`. **Expected stops:** ① the `Opens` manifold structure carrying the kit (`LocallyOneChart`, the causal relation inside `W`); ② the Cauchy property of `t` through the relabelling `V ↦ log V`

*Under `r7677`. Two probes, built in parallel:
- `probes/SchwarzschildEF.lean` for ① and ②, from campaign 97's `SchwarzschildKruskal.lean`;
- `probes/SchwarzschildAlign.lean` for ③ and ④, also from `SchwarzschildKruskal.lean`. Tangency is local, so it is
  stated at the horizon points `{U = 0, V > 0}` of campaign 97's `sk_S`. Those points also lie in `W` with the same
  metric, and RESULT states this.

No Lean was written before this registration.*

## ① The foundation on `W`

***The spacetime.***
- `N := W`, the open set `{V > 0, UV < 1}` of the plane, which is regions I and II: EF's domain.
- It is a manifold through Mathlib's open-subset charted structure.
- `M = univ`, and `g = −F(r) dU dV` is restricted from campaign 97.

***`LocallyOneChart`*** comes from campaign 97's C¹ `F` on `{UV < 1}`.

***The causal relation inside `W`.***
- Causal curves in `W` have `U` and `V` non-decreasing.
- Straight segments with `U` and `V` increasing stay in `W`: `V > 0` is preserved, and `UV < 1` by campaign 97's
  `sk_seg_mem`.
- So `Chr_W` is the flat relation restricted to `W`.

***The observer and the horizon.***
- `D = I⁻(O) = {U < 0, V > 0}`, region I, which is P1's exterior `r > r_h`.
- `𝓗⁺ = frontier_W J⁻(O) = {U = 0, V > 0}`. It lies inside `M`, so the condition that failed in campaign 97 now holds.
- On it, `r = r_h`.

## ② `t` is Cauchy temporal on region I, and the headline runs

***`t` and its Cauchy property.***
- `t = 2M log(−V/U)` on region I, and `Θ = √(1 − 2M/r₀) · t`, adapted to the static observer's proper time.
- **Route.** `ψ(U, V) = (U, log V)` maps region I onto `{U < 0} × ℝ` and preserves the null-coordinate order, so the
  causal relations correspond. `t` becomes `−2M log(−U) + 2M V′`, which is campaign 79's `ThetaG` form, already Cauchy.
  Transporting through `ψ` is the expected stop.

***The headline.*** `cd_prop_causal_alignment` instantiated on Schwarzschild gives:
- accumulation `KLi = KLs = 𝓗⁺` for the slices of `t`, and properness;
- cone convergence;
- cone disjointness;
- the stretch;
- **with `𝓗⁺ = {U = 0, V > 0}`, which is `r = r_h`.**

So 8i and the stationary half of 8ii-b are **BUILT**.

## ③ and ④ Row 8ii-a: the slicings align, on the manifold

***③ Stationary.***
- With `t = 2M(log V − log(−U))`, the frame is `ℓ = ∂_V` and `n = (2/F)∂_U`.
- The rate is `dt(ℓ)/dt(n) = F·(−U)/(2V) → 0` at each `(0, V₀)` with `V₀ > 0`.
- `mc_tangency_at_N` then gives alignment, with limit `(F/2) dU`.
- This lifts campaign 80's `tc_stationary` onto `N`.

***④ Retarded.***
- `Θ = a(u + ηr)`, with `u = −4M log(−U)`.
- `dΘ(ℓ) = aη r_V → 0`, since `r_V ∝ U`, while `dΘ(n) → ∞`.
- The limit is `(F/2) dU`.
- This lifts campaign 80's `tc_retarded`.

***④′ Stretch, p `0.2`.*** The retarded slicing's Cauchy property on region I, for the retarded half of 8ii-b. It is
not required.

## Is curvature needed?

No. Vacuum is neither used nor checked, as in campaign 97.

***Failable:*** each piece is BUILT, BUILT IN PART, or REPORTED. Non-vacuity is mandatory.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

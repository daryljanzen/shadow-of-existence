# `r7677+71.3` — RESULT: campaign 98 ① and ②, **Schwarzschild on EF's domain `W = {V > 0, UV < 1}` as an `Opens` manifold, with `𝓗⁺ = {U = 0, V > 0} ⊆ M`; the stationary `t` is Cauchy temporal on region I; the headline runs on Schwarzschild. BUILT, with no named hypothesis.** ⌗ `9034` lines in one probe (`1025` new). The campaign total is `1581` new lines across two probes, inside the registered band of 1000–4000. ⌗ p: ① `0.6` came true; ② `0.45` came true. The whole campaign (p `0.35`) came true, except ④′

*Against `PREDICTION.md` (`r7677+71.1`). 71 re-ran `lake env lean probes/SchwarzschildEF.lean`. It exits 0 with no
errors and no warnings. All `149` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`: `112`
inherited and `37` new. The forbidden-token grep is clean, and the probe imports only Mathlib. `check_no_sorry.py`
reads ALL 29 THEOREMS COMPILE. The probe copies campaign 97's `SchwarzschildKruskal.lean`, plus about 50 lines of
`cd_` from `ConeDisjoint.lean` and about 85 lines of `hs_` from `HorizonStretch.lean`.*

## ① The foundation — BUILT. The expected stop was not hit

***`W` as a manifold.***
- `seW : Opens P := {p | 0 < p.2 ∧ p.1·p.2 < 1}`, with `N = ↥seW`.
- Mathlib's open-subset `ChartedSpace`, `IsManifold` and `T2Space` instances apply.
- There is one chart, the inclusion, and its `mfderiv` is the identity (`se_dchart`).

***The spacetime.***
- `se_S := se_flat.cz_scale (FS M ∘ val)`, which is `−F(r) dU dV` on `W`, with `M = univ`.
- One new kit piece, `Spacetime.SeAgree`, says two spacetimes have the same `M` and agree in `g` and `T` on `M`. It
  carries `Chr`, `D`, `J⁻`, `H`, `Dsp` and `IsCauchyTemporal` across. It was needed because the chart spacetime's
  representative is junk off `W`, so equality of spacetimes fails.

***`se_foundation` holds:***
- `LocallyOneChart`.
- `Chr x y ↔ U_x < U_y ∧ V_x < V_y`.
- `D` is region I, `{U < 0, V > 0}`.
- `𝓗⁺ = {U = 0, V > 0}`, which **lies in `M`**, is non-empty, and has `r = 2M` on it.

**The clause that failed in campaign 97, `𝓗⁺ ⊆ M`, now holds, with the frontier taken in `W`.**

## ② `t` Cauchy, and the headline — BUILT. The expected stop was not hit

***Cauchy (`se_cauchy_RI`, `se_cauchy`).***
- `ψ(U, V) = (U, log V)` sends causal curves of region I to causal curves of the flat model. Its continuous inverse
  `(U, s) ↦ (U, eˢ)` keeps inextendibility.
- `k(log V − log(−U)) = k · Θ₀ ∘ ψ`, so campaign 79's `hl_cauchy_Θ₀` finishes the Cauchy property.
- Temporality is direct: `dΘ(v) = k(v_V/V + v_U/(−U))`.
- The result lifts to `W` through `SeAgree` and `cz_scale`.

***The observer (`se_proper_time`).*** The static observer sits at `r₀ > 2M`, and `Θ = √(1 − 2M/r₀) · t` is its
proper time: `Θ(O τ) = τ`, `r(O τ) = r₀`, and `g(Ȯ, Ȯ) = −1`.

***`se_headline`:***
- `Θ` is Cauchy temporal on `D`, and `SublevelProper` holds.
- For the slices of `Θ`, `KLi = KLs = 𝓗⁺`, via `mh_causal_alignment_gh_N`.
- For the cones, `KLi = KLs = 𝓗⁺`, via `mc_cone_kuratowski_N`.
- `cone(τ) ∩ 𝓗⁺ = ∅` for every `τ`, via `cd_cone_disjoint`.
- `𝓗⁺` and every cone are non-empty.
- **`𝓗⁺ = {U = 0, V > 0}`, which is `r = r_h`.**

***`se_stretch`.***
- Every compact `K ⊆ 𝓗⁺` eventually lies inside the cones' ε-stretch.
- The stretch eventually leaves every compact set.

***Non-vacuity (`se_nonvacuous`).***
- It takes `M = 1`, `r₀ = 4`.
- `𝓗⁺` and the cones are non-empty, and the disjointness holds.
- `g ≠ gM` at `(0, 1)`, so the metric is not flat. `F` is not constant.

## One difference from the registration

**`cd_prop_causal_alignment` itself was not instantiated, because campaign 89's `ConformalExtension` is not built on
`W`.** The headline instead runs the three theorems that proposition bundles: the Cauchy theorem, cone convergence and
cone disjointness. It also runs the stretch. So every registered bullet of ② is BUILT except the conformal-boundary
reading of `𝓗⁺`. In its place, `𝓗⁺` is identified directly as `{U = 0, V > 0}`.

## Marks

- **8i → BUILT on Schwarzschild.** `𝓗⁺` is `r = r_h`, and accumulation, cone convergence, disjointness and the stretch
  all hold for the stationary slicing.
- **The stationary half of 8ii-b → BUILT.**
- 8ii-a was BUILT in `RESULT_34.md`.
- ④′ is still REPORTED.
- Curvature was not checked or used.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

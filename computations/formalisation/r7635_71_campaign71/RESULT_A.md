# `r7635+71.4` — RESULT: campaign 71, `r7635` ①, local geodesics and `exp` BUILT, **the Gauss lemma BUILT**, local maximality BUILT IN PART, and the generators as null geodesics REPORTED, with its first missing lemma (the ray lemma) stated exactly. ⌗ `1501` lines in one probe (about `1060` new, band 400–3500 new). ⌗ p: `①` `0.55` came true; `②` `0.25` came true in its hard step and partly in its conclusion; `③` `0.15` did not

*Against `PREDICTION.md` (`r7635+71.1`). 71 re-ran `lake env lean probes/LipschitzCornerCutting.lean`. It exits 0
with no errors. All `39` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`. The setting is one
chart with `g ∈ C²`.*

## ① Local geodesics and the exponential map

***The Christoffel symbols.***
- `Γ` is redefined through `ContinuousLinearMap.inverse (g x)` applied to the Koszul covector.
- This makes it C¹ in `x`: `lk_christoffel_contDiffAt`, via `contDiffAt_map_inverse`.

***The geodesic flow.***
- The spray `(x,u) ↦ (u, −Γ_x(u,u))` is cut off by a bump. With that, campaign 62's `FlowData` applies, packaged as
  `GeoFlow`.
- `lk_geodesic`: the flow solves the geodesic equation.
- `lk_scaling`: the scaling law.

***The exponential map.***
- `expp v = π₁φ(p, c v)`. `lk_expp_smul` gives radial geodesics. `lk_expp_contDiffAt` gives C¹.
- **`lk_Dexp_zero`: `D exp_p(0) = id`.**
- `lk_expp_localDiffeo`: `exp_p` is a C¹ local diffeomorphism, with a C¹ inverse.

## ② The Gauss lemma: the registered likely stop did not stop

- `lk_energy_cons`: `g(u,u)` is conserved along geodesics.
- `lk_energy_variation`: that conservation law, differentiated in the initial data.
- `lk_gauss_flow`: `g(u(t), X(t)) = t·g_p(a,b)`.
  - The variational equation supplies `X′ = U`, so no C² flow and no second variation are needed.
- **`lk_gauss`: `g_{exp_p v}(D exp_p(v) v, D exp_p(v) w) = g_p(v,w)`.**

## ③ Local maximality: BUILT IN PART

***Built.***
- The normal chart, with `Q(x) = g_p(exp⁻¹x, exp⁻¹x)` and the position field `P`.
- `lk_grad_Q`: `DQ = 2g(P,·)`.
- `lk_P_energy`: `g(P,P) = Q`.
- `lk_P_euler`: `P` is the Euler field in normal coordinates.
- `lk_causal_perp_null`: a causal vector orthogonal to a null vector is a multiple of it.
- **`lk_ae_null_tangent`**: a Lipschitz curve that stays in `{Q = 0}` with causal velocity a.e. has velocity `∥ P`
  a.e.
- **`lk_chr_of_timelike` / `lk_chr_of_Q_neg`**: `Q(x) < 0` with `exp⁻¹x` future-directed and small gives `p ≪ x`,
  along the radial geodesic as one C¹ timelike step.

***REPORTED.***
- **(a) The ray lemma, the first missing lemma.** Let `σ : ℝ → V` be Lipschitz on `[0,1]`, with `σ(t) ≠ 0` on
  `(0,1]`, and `σ′(t) = k(t)σ(t)` a.e. Then `σ(t) = μσ(1)` with `μ > 0`, for every `t ∈ (0,1]`. Applied in normal
  coordinates, this makes a Lipschitz causal curve in `{Q = 0}` a reparametrised radial null geodesic.
- **(b) Monotonicity of `Q` along Lipschitz future-causal curves from `p`.** Equivalently,
  `J⁺(p) ∩ U ⊆ exp_p(closed future cone)`. It needs monotonicity from a.e. derivatives of Lipschitz functions,
  together with the reverse Cauchy–Schwarz sign `g(P,w) ≤ 0`.

## ④ Generators are null geodesics: REPORTED

As registered, this did not close. It stops at ③(a) and ③(b).

***What then remains for differential tangency.*** With (a) and (b), a generator is locally a reparametrised null
geodesic. It is then C², and campaign 70's `ct_H_generator_null_pregeodesic` applies to it.

No census row moves.

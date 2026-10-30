# `r7641+71.7` — RESULT: campaign 77, `r7641` ①. The causal-`P` bootstrap for a merely Lipschitz start is BUILT, with no named hypothesis: the uniform expansion of `exp⁻¹` is proved, not assumed. The generators of `𝓗⁺` are null geodesics with every C¹-start hypothesis removed. The tangent hyperplane of `𝓗⁺`, wherever a curve in it is differentiable, is BUILT as the generator's null hyperplane. ⌗ `3662` lines in one probe (about `580` new, band 200–2500 new). ⌗ p: Lipschitz-start bootstrap `0.5`, generator theorem with C¹-start hypotheses removed `0.45`, tangent hyperplane `0.55`: all came true; the registered reachable negative (a named expansion hypothesis) did not occur

*Against `PREDICTION.md` (`r7641+71.2`). 71 re-ran `lake env lean probes/LipschitzBootstrap.lean`. It exits 0 with no
errors; the 7 warnings are linter notes in copied code. All `21` `#print axioms` lines read
`[propext, Classical.choice, Quot.sound]`. The forbidden-token grep is clean. The probe is campaign 76's, copied in under
`ShadowProbe.LipschitzBootstrapProbe` with the prefix `lb_`. Campaign 76's C¹-start theorems are dropped, since these
supersede them.*

## ① The bootstrap

***The ingredients.***
- `lb_cone_const`: `−g(w,T) ≥ c‖w‖` near `p`, for causal `w`.
- `lb_expansion`: the uniform first-order expansion of `exp⁻¹` at `p`. It is proved from the continuity of `D exp⁻¹` at
  `p` and of `D exp` at `0`.

***The route.*** Time is measured by `a(t) = −g_p(exp⁻¹γ(t), T p)`, not by the registered `T`-arclength.
- The two agree to first order: `a′ ≥ (29/30)·s′` a.e.
- The registered steps then go through: `c‖exp⁻¹γ‖ ≤ 3a`, `−g(P,T) ≥ (9/10)a`, and the near-conoid step
  `Q ≤ r a² ⇒ Q ≤ (3/5) r a²`, iterated to `Q ≤ 0`.

***The theorems.***
- `lb_causal_in_conoid`: for a Lipschitz curve from `p`, causal a.e. and avoiding `p` after time `0`, `P(γ t)` is
  future causal on `(0,1]` and `Q∘γ ≤ 0` on `[0,1]`. The hypotheses `u`, `hu`, `hd0` and `hC1` are gone.
- `lb_H_generator_null_geodesic`: a Lipschitz causal curve from `p` lying in `𝓗⁺` reparametrises one C² radial null
  pregeodesic, with `Q∘γ = 0` derived.

## ② The tangent hyperplane

- `lb_H_Q_nonneg_near`: `𝓗⁺` lies in `{Q ≥ 0}` near a generator point `x ≠ p`.
- `lb_tangent_hyperplane`: every curve `c` in `𝓗⁺` through `x`, differentiable at `0`, has `DQ(x)(c′) = 0` and
  `g(P(x), c′) = 0`. So it is tangent to the generator's null hyperplane.
- `lb_generator_tangent_hyperplane`: the same at every point of a generator, with `p ∈ 𝓗⁺` derived.
- The reverse inclusion "`𝓗⁺` = conoid" was not attempted, as registered.

## Non-vacuity

- **In Lean.** `lb_nonvacuous` exhibits a curve meeting every hypothesis of `lb_causal_in_conoid` in any C² spacetime,
  at any `p`. It uses `γ t = p + tδ·T p`, together with `lb_geoFlow_exists` and `lb_normalChart_exists`.
- **On paper only.** The `𝓗⁺`-hypothesis is argued: in Minkowski space with `J = {q}`, `q = p + k`, `k` future null,
  the null segment `p + tk` lies in `𝓗⁺`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

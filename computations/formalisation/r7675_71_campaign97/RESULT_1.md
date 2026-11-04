# `r7675+71.2` — RESULT: campaign 97 ①, **Schwarzschild as an `MSpacetime` in Kruskal's radial plane: BUILT. 3a: BUILT.** One registered clause was false and is corrected: `S.H J` is not `{U = 0}`. It also contains the white-hole singularity `{U < 0, UV = 1}`, which lies outside `M`. What holds is `S.H J ∩ M = {U = 0}`, with `r = 2M` there. ⌗ `8009` lines in one probe (`765` new, band 400–2000). ⌗ p `0.6`: came true, apart from the corrected clause

*Against `PREDICTION.md` (`r7675+71.1`). 71 re-ran `lake env lean probes/SchwarzschildKruskal.lean`. It exits 0 with
no errors and no warnings. All `112` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`: `95`
inherited and `17` new. The forbidden-token grep is clean, and the probe imports only Mathlib. It copies campaign 91's
`CurvedTangency.lean` and campaign 80's Kruskal `hK`, `rinv`, `rK` and `FS`.*

## The foundation

***The radius.***
- `sk_rinv_contDiffOn`: `rinv` is C¹ on `(−1, ∞)`, by the inverse function theorem.
- `sk_rK_contDiffOn`: `rK` is C¹ on `{UV < 1}`.
- `sk_rK_spec`: `r > 0` and `h(r) = −UV`.
- `sk_rK_eq_two_iff`: `r = 2M ⟺ UV = 0`.

***The conformal factor.***
- `sk_FS_pos` and `sk_FS_contDiffOn`: `F = (32M³/r) e^{−r/2M}` is positive and C¹ on `{UV < 1}`.
- `sk_FS_nonconst`: `F = 16M²/e` at `r = 2M`, and `8M²/e²` at `r = 4M`.

***The spacetime.***
- `NModel.sk_S` is the restriction of the flat `minkN` to `M = {UV < 1}`, rescaled by `F`. `F` is extended by `1` off
  `M`, so campaign 90's invariance lemmas apply unchanged.
- `sk_hRep`: in the chart, the metric is `g = F · (−dU dV)`.
- `sk_locallyOneChart` holds, through a new general lemma, `sk_scale_locallyOneChart`, which needs `F` C¹ only on the
  chart image of `M`.

***The observer.***
- `sk_observer` and `sk_static_observer`: for `r₀ > 2M`, `O` lies on `UV = −c` with `c = h(r₀) > 0`, and `r(O σ) = r₀`.
- `hOD` holds, with `D = {U < 0} ∩ M` (regions I and IV), together with `hmono` and `hJM`.

## The corrected clause

- **Registered:** `S.H J = {U = 0}`.
- **Proved:** `S.H J = {U = 0} ∪ {U < 0, UV = 1}`, and `S.H J ∩ M = {U = 0}`, with `r = 2M` on it (`sk_H_r`).
- **Why:** `H` is the frontier taken in `N = Pt`, and `M = {UV < 1}` is not closed. So the frontier of `J⁻(O)` also
  meets the past singularity `r = 0` of region IV, which is outside `M`.
- **Consequence:**
  - the headline's hypothesis `𝓗⁺ ⊆ M` fails on this `N`, so the slice and cone limits are not run on `sk_S`;
  - the fix is `N = M` as a manifold of its own, which is the same `Opens` construction row 8 needs.

## 3a — `sk_cor_EF_events`

For `0 < V₁ < V₂`, with `p = (0, V₁)` and `q = (0, V₂)`:
- `p, q ∈ S.H J ∩ M`, the static observer's `∂J⁻` within the spacetime;
- `p ≠ q`;
- `S.Cau p q`, so they are causally ordered;
- `¬ S.Chr p q`, so they are null-related;
- `r p = r q = 2M`.

***EF reading.*** In ingoing EF, `v = 4M log V` on the region `V > 0`, so `p` and `q` sit at `v₁ < v₂`, both on
`r = 2M`.

***Non-vacuity.*** `sk_nonvacuous` sets `M = 1` and `r₀ = 4`, gets all of 3a, and shows the metric differs from the
flat one and `F` is non-constant.

## Curvature

Curvature was neither checked nor used.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

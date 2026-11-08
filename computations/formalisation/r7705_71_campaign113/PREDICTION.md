# `r7705+71.1` — PRE-REGISTRATION: campaign 113, **2a: the interior chart into the Kruskal manifold, so the cycloid is a geodesic of Schwarzschild itself**; with the map of rows 2b, 4a, 5a, 6a and 6c to P2's labels (delivered here, below). ⌗ `650` new lines (band 500–850), p `0.5` for the whole, p `0.85` for ① alone. **Expected stop:** ②-ii, the Koszul form along the curve

*Registered before any Lean. The probe is `probes/CircleChart.lean`, a copy of campaign 112's `CircleCycloid.lean`.
Everything new is prefixed `cc_`.*

## The reading

**The manifold is campaign 98's `se_S`.** That is Schwarzschild on the Eddington–Finkelstein domain
`W = {V > 0, UV < 1}`, with `g = −F dU dV`, `F = (32M³/r)e^{−r/2M}`, and a single chart (the inclusion). The interior
quadrant `{U > 0, V > 0, UV < 1}` lies in `W`. Campaign 107's horizon geodesic (`ng_isGeodesicOn`) was built on the
same manifold.

**The map is `Φ(η, t) = (s(η)e^{−t/4M}, s(η)e^{t/4M})`, with `s(η) = sin(η/2)·e^{r/4M}` and `r = M(1 + cos η)`.**
- No square root is needed: `UV = s² = (1 − r/2M)e^{r/2M} = −hK(r)`, so `rK(Φ) = r` (`rinv_hK`).
- **Checked in advance:**
  - `s′ = e^{r/4M}cos³(η/2)/2`;
  - `F s′² = 4M²cos⁴(η/2)` and `F s²/16M² = tan²(η/2)`;
  - so `Φ*g = −4M²cos⁴(η/2) dη² + tan²(η/2) dt²`, which is campaign 112's `cy_g`.

## Stages

| Stage | Statement | Lines | p | Rests on |
|---|---|---|---|---|
| ① | `Φ` maps `(0, π) × ℝ` into the interior quadrant of `W`, with `rK ∘ Φ = M(1 + cos η)`. It is injective, since `UV` fixes `η` and `V/U` fixes `t`. With `∂_ηΦ` and `∂_tΦ` as `HasDerivAt`, `g(∂_ηΦ, ∂_ηΦ) = −4M²cos⁴(η/2)`, `g(∂_tΦ, ∂_tΦ) = tan²(η/2)` and `g(∂_ηΦ, ∂_tΦ) = 0`, read through `se_hRep` | 150–250 | 0.85 | `se_hRep`, `gM_apply`, `rinv_hK`, `hK` |
| ②-i | `η(τ)` is `C²` on `(0, Mπ)`, as the local inverse of the smooth `τ(η)` with `τ′ ≠ 0` | 60–120 | 0.75 | Mathlib `ContDiffAt.to_localInverse`, `cy_η_spec` |
| ②-ii | `γ(τ) = Φ(η(τ), t₀)` is `IsGeodesicOn (se_S hM)` on every `[a, b] ⊂ (0, Mπ)`. The route: differentiate `F(γ)·S′² = 1` (with `S = s ∘ η`) and `hK(r(τ)) = −S²`, which gives `F S″ + ∂_U F·S′² = 0`; feed that into the Koszul form at `w = (1, 0)` and `(0, 1)`, and close by linearity | 200–350 | 0.6 | `st_hRep_eventually`, `st_FS_diff`, `sq_smul_fderiv_apply`, `kr_r_U`, `kr_hasDerivAt_φ` |
| ③ | On the manifold, `g(γ′, γ′) = −1`, and the Killing energy for the boost field `K = (−U/4M, V/4M)`, which is `∂_t` pushed forward by `Φ`, is `E = −g(γ′, K) = 0` | 50–100 | 0.85 | ①, ② |

**Expected stop: ②-ii.** It is the Koszul form of `F·gM` along a curve off the horizon. `ng_isGeodesicOn` only had
it on `U = 0`, where it vanishes.
- **Fallback:** prove the geodesic equation for `t₀ = 0` only, where `U = V` and the two components coincide. The
  boost isometry then carries it to any `t₀`, but only as a stated, unbuilt remark.
- **If ②-i stops:** derive `C²` directly from `η′ = 1/r(η)`, using `contDiffOn_succ_iff_deriv_of_isOpen` twice.

## Order ②: the built rows mapped to P2's labels (today's tree)

| Row | P2 label | The sentence it supports | Lean names |
|---|---|---|---|
| 2b | `lem:interior_metric` (l.149) | the statement: both forms `eq:interior_metric` and `eq:interior_metric_eta`, and the proof's `g_tt = tan²(η/2)` and `g_rr dr² = −4M²cos⁴(η/2) dη² = −dτ²` | `cy_interior_forms` |
| 4a | `prop:region_I_metric` (l.215) | the statement's "the metric becomes `eq:Region_I_metric`" (the proof's three `↦` lines, l.232–236) and "agrees with the Schwarzschild exterior metric for `r ∈ (2M, ∞)` under the identification `r = M(1 + cosh ρ)`" (l.220, and the proof's `1 − 2M/r = tanh²(ρ/2)` and `dr²/(1 − 2M/r) = 4M²cosh⁴(ρ/2)dρ²`) | `cy_regionI_coeffs`, `cy_regionI_schw` |
| 5a | `prop:back_seam_metric` (l.264) | the statement's "the metric becomes `eq:back_seam_metric`" (the proof's `↦` lines, l.278–282) and "agrees with the Schwarzschild form for `r ∈ (−∞, 0)` under `r = M(1 − cosh ρ′)`" (l.269, and the proof's `1 − 2M/r = coth²(ρ′/2)`, l.292). The radial counterpart, `dr²/(1 − 2M/r) = 4M²sinh⁴(ρ′/2)`, is built too; the proof does not state it | `cy_backseam_coeffs`, `cy_backseam_schw` |
| 6a | `prop:four_regions` (l.303) | items 1–4 (l.306–309): each patch's `r`-range, each map onto its range. The proof's "the white-hole interior is obtained from the black-hole interior by `η ↦ −η`" (l.315) is `r` even and `τ` odd | `cy_patches` |
| 6c | `prop:four_regions` (l.311) | "The Kruskal–Szekeres extension does not contain them": no point of `{UV < 1}` has `r = M(1 − cosh ρ′)` | `cy_backseam_not_kruskal` |

**Not covered by these rows:**
- In l.308, "isometric and meeting at the bifurcation 2-sphere".
- In l.309, "horizonless and asymptotically flat".
- In l.311, "precisely the maximal Kruskal–Szekeres extension". That is row 6b.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

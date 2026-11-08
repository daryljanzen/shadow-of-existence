# `r7711+71.1` — PRE-REGISTRATION: campaign 116, **5b: the `r < 0` back-seam regions as a geometry in their own right** (5b-i the coefficients, 5b-ii the tortoise null chart and `K = 48M²/r⁶ → 0`); with **maximality priced**. ⌗ `480` new lines (band 340–580), p `0.55` for the whole, p `0.95` for 5b-i alone. **Expected stop:** 5b-ii-②, the tortoise inverse's derivatives feeding `kr_warped`

*Registered before any Lean. The probe is `probes/CircleBackSeam.lean`, a copy of campaign 115's
`CirclePatches.lean`. Everything new is prefixed `bs_`.*

## The reading

**The region:** `r < 0` with `f(r) = 1 − 2M/r`, the "Schwarzschild form for `r ∈ (−∞, 0)`" of
`prop:back_seam_metric`.
- **On `r < 0`:** `f > 1`, so `g_tt = −f` never vanishes and `∂_t` is timelike everywhere. That is "horizonless".
- **As `r → −∞`:** `f → 1`. That is "asymptotically flat" in the coefficients.
- **Not Kruskal:** campaign 112's `cy_backseam_not_kruskal` already gives that the region is not in Kruskal.

## Stages

| Stage | Statement | Lines | p |
|---|---|---|---|
| 5b-i | On `r < 0`: `f(r) > 1` (horizonless: `g_tt < 0` everywhere, `g_rr > 0`), and `f → 1`, `g_rr = f⁻¹ → 1` as `r → −∞`. At `r = M(1 − cosh ρ′)`, `f = coth²(ρ′/2)` (`cy_backseam_schw`), so the back-seam metric of `prop:back_seam_metric` is this form | 40–80 | 0.95 |
| 5b-ii-① | The tortoise `r*(r) = r + 2M log(1 − r/2M)` on `(−∞, 0)`. Its derivative is `1/f`, so it is strictly increasing, and its range is `(−∞, 0)`. Its inverse `bs_r` is `C²`, with `bs_r′ = f(bs_r)` | 100–180 | 0.7 |
| 5b-ii-② | The null chart `u = t − r*`, `v = t + r*` on `{v − u < 0}`, and the warped metric `−f(r) du dv + r²(dθ² + sin²θ dφ²)` with `r = bs_r((v − u)/2)`, as a `kr_WD` datum. It needs `F = f ∘ r`, `R = r`, `R_u = −f/2`, `R_v = f/2` and the second derivatives, each as `HasDerivAt`, plus `Good` on the chart's domain | 150–250 | 0.6 |
| 5b-ii-③ | Campaign 110's `kr_warped` gives `K = 48M²/r⁶` on the chart, so `K → 0` as `r → −∞`. As in `kr_schwarzschild`, the checks are `\|∇R\|² = 1 − 2M/r`, `k₂ = 4M/r³` and `\|∇∇R\|² = 2M²/r⁴` | 50–100 | 0.8 |

**Expected stop: 5b-ii-②.** It is the second derivatives of `F = f ∘ bs_r ∘ ((v − u)/2)` and their `kr_WD`
bookkeeping. Campaign 110 needed `kr_comp_U`/`kr_comp_V` for the same step.
- **Fallback:** stop at 5b-ii-①, with the coefficients in `(u, v)` stated (`−f du dv`) but without `K`.
- **What the fallback would leave:** 5b would stay BUILT IN PART, with the curvature clause unformalised.

## Maximality, priced (not built)

The clause is "the Kruskal–Szekeres extension is maximal". It has two readings.

| Reading | What it needs | Lines | p |
|---|---|---|---|
| (a) Within the chart plane | Every boundary point of `{UV < 1}` in `ℝ²` lies on `UV = 1`, where `K → ∞` (`kr_blowup`, `kr_nhds_le_toSig`). So the metric admits no `C²` extension, with `K` continuous, across any boundary point of the chart's domain. That is chart-level `C²` inextendibility | 80–150 | 0.85 |
| (b) As a spacetime | No Lorentzian manifold properly contains `{UV < 1}` isometrically. That needs, as well, completeness or an inextendibility theorem at the ends `U, V → ±∞`, and an abstract notion of extension | 2000+ | < 0.1 |

**Not attempted:** reading (b). It needs tools the kit does not have (inextendibility of spacetimes, geodesic
completeness of the asymptotic ends). Reading (a) is the honest formal content and is cheap.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

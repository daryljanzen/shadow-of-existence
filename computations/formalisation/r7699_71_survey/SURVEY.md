# Survey for the second paper to formalise: `r7699+71`

*A survey, not a campaign. No Lean was written. It reads the corpus as it stands, and the probes through campaign 110
(`Kretschmann.lean`). The method and the marking rule are those of `r7685_71_inventory/INVENTORY.md`: **BUILT**,
**BUILT IN PART** (gap named), **NOT BEGUN**. Every Lean name below was grepped in the probes, `ShadowEngine.lean`
or `ShadowFormal/`. Prices are new lines; p is the chance of success.*

**Recommendation: P2, `corpus/janzen_circle_v3.tex`.** First campaign: `prop:Kretschmann` with `prop:critical`, in a
copy of `Kretschmann.lean`. About 460–920 lines, p 0.75. P3 (`SdS-slicing-curve_v2.tex`) is a close second, and the
better choice only if cheap rows matter more than using the kit.

## Paper numbers

The numbers come from each paper's `\input{appendix_ledgers_P*}` line.

| P | file | P | file |
|---|---|---|---|
| 1 | `BH_causality_v2` | 10 | `canonical_time` |
| 2 | `janzen_circle_v3` | 11 | `dynamics_paper` |
| 3 | `SdS-slicing-curve_v2` | 12 | `algebroid_paper` |
| 4 | `modern_parallax` | 13 | `boundary_paper` |
| 5 | `groupoid_paper` | 14 | `matter_sector_paper` |
| 6 | `shadow_of_existence` | 15 | `CR_cosmology` |
| 7 | `CR_framework` | 16 | `cosmogenesis_paper` |
| 8 | `slicing_operator` | 17 | `geometric_core_paper` |
| 9 | `range_paper` | 18 | `CR_synthesis` (no ledger appendix; named P18 at `CORPUS_MAP.md` l.6063) |

## Scores for every candidate

"Fit" means how well the paper suits the kit: Lorentzian causal structure, horizons, Schwarzschild and de Sitter,
and curvature by hand.

| P | file | stmts | fit | reason |
|---|---|---|---|---|
| **2** | `janzen_circle_v3` | 8 | **High** | Schwarzschild interior, a radial geodesic, Kruskal's four regions and the Kretschmann scalar. These land on `sk_`, `ng_` and `kr_schwarzschild`. Six of the eight statements are precise. |
| 3 | `SdS-slicing-curve_v2` | 15 | Medium–high | Precise and cheap, but about 10 of the 15 are polynomial or trig identities over ℝ with no Lorentzian content. Three are interpretive (`prop:gnomonic`, `prop:rigidity`, `prop:morphism-generation`). Several are already built at the receipt level. |
| 8 | `slicing_operator` | 5 | Medium | Einstein tensors of static spherical metrics, an ODE, a geodesic and the constant-curvature leaves. All are precise, but the probes have no Ricci or Einstein tensor. Most are built at the receipt level (`SecondSeatStatic.lean`, `CurvatureInstances.lean`). |
| 5 | `groupoid_paper` | 13 | Low–medium | The "groupoid of observer descriptions" is never defined. The precise parts are D₃ relations, S₃ monodromy (mostly in `Row18Monodromy.lean`) and Aut(A₂). That is Mathlib algebra, with no use of the kit. |
| 17 | `geometric_core_paper` | 2 | Low–medium | `prop:tangentnull` is precise and cheap. `prop:unique` needs a precise reading: read plainly, anti-de Sitter and Minkowski are maximally symmetric and Lorentzian too. |
| 12 | `algebroid_paper` | 1 | Low–medium | Bracket inclusions in `so(5,1)`. Precise, but a matrix computation with no use of the kit. |
| 7 | `CR_framework` | 20 | Low | Mostly about "ontological layers" and "projections", which are undefined. Only two or three are precise: the asymptotic non-intersection theorem, which is close to P1's slice results, and parts of `thm:null-boundary`. |
| 9 | `range_paper` | 11 | Low | Needs the Einstein equations, the Petrov classification and the "operator range", which is undefined. The computable kernels are already built at the receipt level. |
| 15 | `CR_cosmology` | 7 | Low | Perturbation amplitudes and numbers. Only `prop:throat` and `prop:flat` (curvature) suit the kit. |
| 11 | `dynamics_paper` | 3 | Low | Hamiltonian quantisation. `prop:twoKV` is precise and already built at the receipt level. |
| 13 | `boundary_paper` | 4 | Low | Standard Model gauge groups and spinors. |
| 14 | `matter_sector_paper` | 2 | Low | Spinor zero-modes; "forced within CR". |
| 6 | `shadow_of_existence` | 2 | Low | Philosophy of science. |
| 4 | `modern_parallax` | 1 | Low | A philosophical theorem. |
| 18 | `CR_synthesis` | 1 | Low | The same de Sitter uniqueness claim as P17. |

## The choice: P2, and why not P3

**For P2:**
- **It continues the thread the kit was built for.** Campaigns 97–110 built Schwarzschild on Kruskal's `{UV < 1}`, so
  the black-hole interior and the bifurcation sphere are already in the kit:
  - `sk_S` on `Pt`, with `sk_kM`, `rK`, `sk_rK_spec` and `sk_rK_eq_two_iff`;
  - geodesics on an `MSpacetime`: `IsGeodesicOn`, `ng_Γ`, `ng_geod_iff`, `ng_energy_const`;
  - **`kr_schwarzschild`: `K = 48M²/r⁶` on all of `{UV < 1}`**, proved from the coordinate Riemann tensor.
- **The headline rows are cheap.** P2's Kretschmann proposition is that value composed with `r = M(1 + cos z)`.
- **Its precise statements are true.** Its one flaw is a scope flag (row 1a).
- **It is small enough to finish.** It is P1's direct companion: P1 l.140 and P2 §7 both read `r = 2M` and `r = 0`
  as P1's metric singularities.

**Against P3:**
- **Most of P3 does not use the kit.** It is mostly the horizon cubic `r³ − r + 2M` and the trig of its sky angle.
  That is Mathlib algebra, and it is largely done:
  - `ShadowFormal/Nariai.lean` (`discr_horizon`, `factor_general`, `nariai_factorisation`, `nariai_double_root`);
  - `Row18Cubic.lean` (`no_triple_root`, `cubic_disc_roots`);
  - `Row18Monodromy.lean`;
  - `slice_gauss` / `sds_slice_gauss` (`prop:curvature`), `throat_join` (`prop:flip`), `hinge_interval`
    (`prop:twoalpha` (vi)).
- **Its geometric statements are thin.** `prop:turning` is an ODE row. `prop:r0zero` is "pure de Sitter". Three of
  its rows are interpretive.
- **Rough cost of P3:** about 1,500–3,000 lines in total, most of it at p ≥ 0.85. It could run in parallel without
  the kit.
- **Reading flags found while skimming P3:**
  - **`prop:involution`:** `σ∘σ = id` holds on `[0, 2/√3]`, but `σ` maps that interval onto `[−1/√3, 1]`, not into
    itself. `σ` is an involution of `[−1/√3, 2/√3]`. It sends `r₀` to "the second positive root" only for
    `r₀ ≤ 1`.
  - **`prop:curvature`:** `K_G = −f′/2r` is the curvature of `dr²/f + r²dφ²`. On the paper's own slicing surface,
    `dl = dr/√|f|`, it is `−|f|′/2r`. Where `f < 0` that is `+f′/2r`, so the sign flips.

---

# Inventory of P2 (`corpus/janzen_circle_v3.tex`)

The grep for `\begin{theorem|proposition|lemma|corollary}` finds **8** statements. They are split into **22 rows**
below, in the same way as P1's.

- **The two kits.** The P1 kit is the probes (`MSpacetime`, `sk_`, `ng_`, `kr_`). It imports only Mathlib, and
  probes cannot import probes.
- **Receipt-level work.** The earlier receipt census (`r7325_71_inventory/ROWS.tsv`, rows 27–31) already built some of
  P2 at chart level:
  - in `ShadowEngine.lean`: `interior_chart`, `cycloid_proper_time`, `interior_geodesic`;
  - in `NoConnectionSweep.lean`: `interior_cycloid`, `interior_gtt_zero`, `circle_continuation`, `three_axes`.
  - These count as **BUILT IN PART**. The gap is the same each time: they are not on an `MSpacetime`.
- **One reading throughout.** "Analytic continuation of the metric" is read as substituting into the holomorphic
  extension of each coefficient function, with `dz² ↦ (dz/dρ)² dρ²`. Mathlib has no continuation of a metric.

## 1. `prop:cycloid` (l.113)

**1a.** A radial timelike geodesic in `0 < r < 2M` has `r = M(1 + cos η)` and `τ = M(η + sin η)`, `η ∈ [0, π]`.
- **Reading flag:** this holds only for the **`E = 0` geodesic**: `t = const` inside, `U = V` in Kruskal, starting
  at the bifurcation sphere.
  - A radial geodesic with energy `E` is a cycloid of amplitude `r_max = 2M/(1 − E²)`, and it does not meet
    `r = 2M` at `η = 0`.
  - The proof's `dτ² = dr²/(2M/r − 1)` is the `E = 0` case.
  - So the statement needs "the geodesic with `E = 0`", or "some geodesic".
- **Kit:**
  - `ShadowEngine`: `interior_geodesic` (the infall field is geodesic for the Levi-Civita connection on the `(u, t)`
    chart), `cycloid_proper_time`, `interior_chart`.
  - On the manifold: `IsGeodesicOn`, `ng_geod_iff`, `ng_Γ`, and `sk_S` / `sk_kM` / `rK`.
- **Mark: BUILT IN PART.** The gap is that it is chart-level only and in the other engine.
- **Remains:** the curve `η ↦ (S(η), S(η))`, with `−hK(M(1 + cos η)) = S²`, is `IsGeodesicOn (sk_S hM)` on
  `(0, π)`, and `g(γ′, γ′) = −(M(1 + cos η))²`.
- **Price:** 400–700 lines, p 0.65.
- **Expected stop:** differentiating `S = √(·)` at the ends. Work on the open interval, and get the endpoints by
  continuity.
- **Interpretive:** no.

**1b.** The proper time from `η = 0` to `η = π` is `Mπ`.
- **Kit:** none; it follows from 1a. **Mark: NOT BEGUN.** 30–60 lines, p 0.95, no stop. **Interpretive:** no.

## 2. `lem:interior_metric` (l.147)

**2a.** On the radial plane, `(η, t)` coordinates pull the interior metric back to
`−4M²cos⁴(η/2) dη² + tan²(η/2) dt²`.
- **Kit:** `interior_cycloid` gives the coefficient identities: `g_tt = tan²(η/2)` and
  `g_rr r′² = −4M²cos⁴(η/2)`.
- **Mark: BUILT IN PART.** The gap is that no map into the manifold exists.
- **Remains:** a chart `Φ(η, t) = (U, V)` into the quadrant `U, V > 0` of `sk_kM`, with `Φ*(sk_S.g)` equal to the
  form above. It needs the `rK` chain rule (`kr_r_U`, `kr_r_V`) and `sk_hRep`.
- **Price:** 300–500 lines, p 0.7.
- **Expected stop:** the conformal factor `FS` composed through `rK`, and the normalisation of `gM`.
- **Interpretive:** no.

**2b.** The 4D form, with `M²(1 + cos η)² dΩ²`, and its equivalent in `dτ`.
- **Kit:** `kr_`'s `Fin 4` coordinate metrics. **Mark: NOT BEGUN.** 100–150 lines, p 0.85.
- **Stop:** none. The sphere factor is added by hand, as in campaign 110. **Interpretive:** no.

## 3. `prop:critical` (l.185)

**3.** `r(z) = M(1 + cos z)` has critical points exactly at `πℤ`, all non-degenerate:
- `r = 2M` and `r″ = −M` (a maximum) at `2kπ`;
- `r = 0` and `r″ = M` (a minimum) at `(2k + 1)π`.
- **Kit:** none (`three_axes` has only the evenness of `r`). Mathlib supplies `Real.sin_eq_zero_iff` and
  `cos ≤ 1`.
- **Mark: NOT BEGUN.** 60–120 lines, p 0.95, no stop.
- **Interpretive:** no. The Morse reading is a citation.

## 4. `prop:region_I_metric` (l.213)

**4a.** At `z = iρ`:
- `−4M²cos⁴(z/2)(dz/dρ)² = 4M²cosh⁴(ρ/2)`;
- `tan²(z/2) = −tanh²(ρ/2)`;
- `(1 + cos z)² = (1 + cosh ρ)²`.
- **Kit:** `circle_continuation` has `cos(iρ)` and `sin(iρ)`. **Mark: BUILT IN PART.**
- **Remains:** the half-angle `tan` and `cos⁴` identities, and the `i² = −1` bookkeeping.
- **Price:** 80–150 lines, p 0.9. **Stop:** `Complex.tan` at `iρ/2`, solved through `sin/cos`.
- **Interpretive:** no.

**4b.** With `r = M(1 + cosh ρ)`, this is the exterior Schwarzschild metric.
- **Kit:** `circle_continuation`: `1 − 2M/r = tanh²(ρ/2)` and `r′²/(1 − 2M/r) = 4M²cosh⁴(ρ/2)`.
- **Mark: BUILT IN PART.**
- **Remains:** the manifold form, a chart `(ρ, t) → {U < 0 < V} ∩ sk_kM` pulling `sk_S.g` back to the form above.
  It reuses 2a's method.
- **Price:** 250–450 lines, p 0.7. **Interpretive:** no.

## 5. `prop:back_seam_metric` (l.262)

**5a.** The coefficients at `z = π + iρ′`, and the identity `1 − 2M/r = coth²(ρ′/2)` for `r = M(1 − cosh ρ′)`.
- **Kit:** `three_axes` and the last clause of `circle_continuation` give `r = M(1 − cosh ρ′)`.
- **Mark: BUILT IN PART.** The `coth` identities are missing.
- **Price:** 80–150 lines, p 0.9. **Interpretive:** no.

**5b.** "The Schwarzschild form for `r < 0`" as a geometry.
- **Kit:** none. The kit's Schwarzschild has `r > 0` only.
- **Mark: NOT BEGUN.**
- **Remains:** the cheap route is coordinates. Write the region in null coordinates `(u, v)` built from the tortoise
  `r*`, with `F = f`, `R = r`. Then `kr_warped` applies unchanged and gives `K = 48M²/r⁶`, so `K → 0` as `r → −∞`.
- **Price:** 200–400 lines, p 0.6.
- **Stop:** the tortoise inverse for `r < 0`, the analogue of `rK`.
- **Interpretive:** in part. "Agrees with the Schwarzschild form" is the coefficient identity. Calling it a region
  of the same spacetime is a reading.

## 6. `prop:four_regions` (l.301)

**6a.** The six patches have the stated `r`-ranges, and the white-hole interior is `η ↦ −η`.
- **Kit:** `three_axes` has `r` even and `τ` odd. **Mark: BUILT IN PART.**
- **Price:** 80–150 lines, p 0.95. **Interpretive:** no.

**6b.** The four patches with `r ≥ 0`, together with their meeting set, are exactly Kruskal's `{UV < 1}`.
- **What it claims:** each patch's chart (2a, 4b, and their reflections `U ↔ V`, `(U, V) ↦ (−U, −V)`) lands in one
  quadrant, and the images together with `{UV = 0}` cover `sk_kM`.
- **Kit:** `sk_kM`, `sk_rK_eq_two_iff` (`r = 2M ⟺ UV = 0`), `kr_BH_eq`. **Mark: NOT BEGUN.**
- **Price:** 300–600 lines, p 0.6.
- **Stop:** the two horizons `UV = 0, U ≠ V` are in no patch. "Meet at the bifurcation sphere" holds in the
  `(η, t)` chart, where `η → 0` with `t` fixed reaches `U = V = 0`. In the manifold, the patches meet along all four
  horizon halves.
- **Interpretive:** no, once read this way.

**6c.** The `r < 0` patches are not in Kruskal.
- **Kit:** `sk_rK_spec` (`rK > 0`). **Mark: NOT BEGUN.** 20–50 lines, p 0.95. **Interpretive:** no.

**6d.** "A single analytic curve, hyperbola–circle–hyperbola", and "maximal analytic completion".
- **Mark: NOT BEGUN.**
- **Interpretive: yes.** The formal remains are 6b and 6c, plus `three_axes`' reality locus. "Continue through
  `r = 0`" is not a spacetime extension: `kr_blowup` gives `K → ∞` there.

## 7. `prop:Kretschmann` (l.327)

**7a.** `K = 3/(4M⁴)` at `z = 0` (`r = 2M`), read on the manifold at the bifurcation sphere `U = V = 0`.
- **Kit:** `kr_schwarzschild` holds on all of `sk_kM`, which contains `(0, 0)`, and `sk_rK_eq_two_iff`.
- **Mark: BUILT IN PART.** The evaluation is missing.
- **Price:** 40–80 lines, p 0.95. **Stop:** none. **Interpretive:** no.

**7b.** `K` along the interior chart is `48/(M⁴(1 + cos η)⁶)`.
- **Kit:** `kr_schwarzschild` composed with `rK = M(1 + cos η)`. **Mark: NOT BEGUN.**
- **Price:** 60–120 lines, p 0.9. It can be tied to 2a's `Φ` later. **Interpretive:** no.

**7c.** `z ↦ 48/(M⁴(1 + cos z)⁶)` has a pole of order exactly 12 at `π`.
- **Kit:** Mathlib's `meromorphicOrderAt_pow` and `meromorphicOrderAt_inv` (`Analysis/Meromorphic/Order.lean`).
  **Mark: NOT BEGUN.**
- **Remains:** `analyticOrderAt (1 + cos) π = 2`.
- **Price:** 150–300 lines, p 0.75.
- **Expected stop:** that order, through `1 + cos z = 2 sin²((z − π)/2)` and a nonvanishing quotient.
- **Fallback:** the real form `(z − π)¹² K(z) → 3072/M⁴`, at p 0.9.
- **Interpretive:** no.

**7d.** `K` is bounded near `z = 0`.
- **Kit:** continuity. **Mark: NOT BEGUN.** 20–40 lines, p 0.95. **Interpretive:** no.

**7e.** "The pole is generated by the chain rule at a non-degenerate critical point".
- **What it claims, formally:** a general lemma. If `h` is analytic with `h(z₀) = h′(z₀) = 0` and `h″(z₀) ≠ 0`, then
  `c/h⁶` has order `−12` at `z₀`.
- **Mark: NOT BEGUN.** 100–200 lines, p 0.8.
- **Interpretive:** in part. "Generated" is a gloss on the lemma.

## 8. `cor:Kretschmann_at_z0` (l.347)

**8a.** Had the maximum been labelled `r = 0`, `K` would diverge there. Its formal content is 7e applied at `z₀ = 0`
to `h = M(cos z − 1)`.
- **Mark: NOT BEGUN.** 30–60 lines, p 0.9, given 7e.
- **Interpretive:** in part.

**8b.** "The labelling is part of the perspectival construction".
- **Interpretive: yes.** It has no formal content.
- *Note:* `48M²/r⁶` is a function of the areal radius. Relabelling changes the metric, not the chart. The invariant
  fact the kit can state is 7a: `K` is finite at `U = V = 0` in a regular chart.

## Summary of the marks

| mark | rows |
|---|---|
| BUILT | 0 |
| BUILT IN PART | 1a, 2a, 4a, 4b, 5a, 6a, 7a (7) |
| NOT BEGUN | 1b, 2b, 3, 5b, 6b, 6c, 6d, 7b, 7c, 7d, 7e, 8a, 8b (13) |
| interpretive (in whole) | 6d, 8b |

That is 22 rows: 20 formal and 2 wholly interpretive. **Total: about 2,300–4,300 new lines.** All of it is buildable
except 6d and 8b.

## Rows ranked by cost

| rank | rows | price | p | stop |
|---|---|---|---|---|
| 1 | 7a, 7d, 6c, 1b | 110–230 | 0.95 | none |
| 2 | 3, 6a | 140–270 | 0.95 | none |
| 3 | 7b | 60–120 | 0.9 | none |
| 4 | 4a, 5a | 160–300 | 0.9 | `Complex.tan` half-angles |
| 5 | 7e, 8a | 130–260 | 0.8 | the analytic order of `h` |
| 6 | 7c | 150–300 | 0.75 (0.9 with the fallback) | `analyticOrderAt (1 + cos) π = 2` |
| 7 | 2b | 100–150 | 0.85 | none |
| 8 | 2a, 4b | 550–950 | 0.7 | pullback through `rK` and `FS` |
| 9 | 1a | 400–700 | 0.65 | `√` at the ends |
| 10 | 6b | 300–600 | 0.6 | horizons outside the patches |
| 11 | 5b | 200–400 | 0.6 | the tortoise inverse for `r < 0` |
| — | 6d, 8b | — | — | interpretive |

## Recommended first campaign

**The Kretschmann campaign: rows 7a–7e, 3 and 8a, in a copy of `Kretschmann.lean`.** It adds about 460–920 lines, at
p 0.75. With 7c's real-variable fallback, p is 0.85.
- **What it moves:**
  - `prop:Kretschmann`, the paper's headline, to BUILT;
  - `prop:critical` to BUILT;
  - the formal part of `cor:Kretschmann_at_z0` to BUILT.
- **Why it comes first:**
  - every piece rests on `kr_schwarzschild`, which already holds on the interior and at the bifurcation sphere;
  - it needs no new geometry;
  - its one stop has a cheap fallback.
- **The second campaign: 2a, 2b and 1a**, the interior chart on `sk_S` and the `E = 0` geodesic. About 800–1,350
  lines, p 0.6.
  - It moves `lem:interior_metric` and `prop:cycloid`.
  - 1a's scope flag goes to 69 first.
- **Then 4, 5 and 6**, which reuse 2a's pullback.
- **One question for 69 now (row 1a):** read `prop:cycloid` as the `E = 0` geodesic. As written ("a radial timelike
  geodesic"), it is false for `E ≠ 0`.

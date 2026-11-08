import Mathlib

/-!
# Probe `r7707+71.2` (campaign 114): 4b, P2's Region I chart pulled back from the Kruskal manifold

Registration: `computations/formalisation/r7707_71_campaign114/PREDICTION.md`. Nothing imports this file, and it
imports only Mathlib. It starts as a copy of campaign 113's `probes/CircleChart.lean` (namespace renamed
`ShadowProbe.CircleExteriorProbe`, all old names kept; the older headers below are kept verbatim and still name the
namespaces of their own campaigns). Everything new has the prefix `ce_`, in `namespace CEModel`, just before the
`#print axioms` block. The manifold is campaign 98's `se_S` on `W = {V > 0, UV < 1}`, as in campaign 113.

* **4b-① — BUILT.** `ce_Ψ M ρ t = (−σ e^{−t/4M}, σ e^{t/4M})`, `σ = ce_σ = sinh(ρ/2)·e^{r/4M}`,
  `r = ce_r = M(1 + cosh ρ)` (`ce_hK`: `hK(r) = σ²`). `ce_Ψ_mem`: for `ρ > 0`, `Ψ(ρ, t) ∈ W`, `U < 0`, `UV < 1`,
  `rK(Ψ) = M(1 + cosh ρ)`. `ce_Ψ_inj`: one-to-one on `(0, ∞) × ℝ`.
* **4b-② — BUILT.** `ce_dρ`, `ce_dt`: `∂_ρΨ = ce_a`, `∂_tΨ = ce_b`. `ce_pullback`: through `se_hRep`,
  `g(∂_ρ, ∂_ρ) = 4M²cosh⁴(ρ/2)`, `g(∂_t, ∂_t) = −tanh²(ρ/2)`, `g(∂_ρ, ∂_t) = 0` — P2's `eq:Region_I_metric`
  (radial part).
* **4b-③ — BUILT.** `ce_reflection`: `(U, V) ↦ (−U, −V)` preserves `rK` and `F·gM` coefficient-wise, so the
  second exterior (`z = −iρ`, `{U > 0 > V}`, outside `W`) carries the same coefficients.
-/

/-!
# Probe `r7705+71.2` (campaign 113): 2a, P2's interior chart into the Kruskal manifold — the cycloid is a geodesic of Schwarzschild itself

Registration: `computations/formalisation/r7705_71_campaign113/PREDICTION.md`. Nothing imports this file, and it
imports only Mathlib. It starts as a copy of campaign 112's `probes/CircleCycloid.lean` (namespace renamed
`ShadowProbe.CircleExteriorProbe`, all old names kept; the older headers below are kept verbatim and still name the
namespaces of their own campaigns). Everything new has the prefix `cc_`, in `namespace CCModel`, just before the
`#print axioms` block. The manifold is campaign 98's `se_S` on `W = {V > 0, UV < 1}` (one chart, the inclusion),
the one campaign 107's `ng_isGeodesicOn` uses.

* **① The chart — BUILT.** `cc_Φ M η t = (s e^{−t/4M}, s e^{t/4M})`, `s = cc_s = sin(η/2)·e^{r/4M}`,
  `r = M(1 + cos η)` (`cc_hK`: `hK(r) = −s²`, no square root). `cc_Φ_mem`: for `0 < η < π`, `Φ(η, t) ∈ W`, `U > 0`,
  `UV < 1`, `rK(Φ) = M(1 + cos η)`. `cc_Φ_inj`: one-to-one on `(0, π) × ℝ`. `cc_dη`, `cc_dt`: `∂_ηΦ = cc_a`,
  `∂_tΦ = cc_b`. `cc_pullback`: through `se_hRep`, `g(∂_η, ∂_η) = cy_A`, `g(∂_t, ∂_t) = cy_B`, `g(∂_η, ∂_t) = 0` —
  `Φ*g` is campaign 112's `cy_g`.
* **②-i — BUILT, by the registered fallback.** `cc_η_contDiffOn`: `η(τ)` is `C²` on `(0, Mπ)`, from `η′ = g ∘ η`
  with `g = 1/(M(1 + cos))` smooth (`contDiffOn_succ_iff_deriv_of_isOpen` twice), not through Mathlib's local inverse.
* **②-ii — BUILT.** `cc_unit`: `F(r)·S′² = 1` along `S = s ∘ η`. `cc_scalar`: `F S″ + D S′² = 0`,
  `D = −F′(r) S/hK′(r)`, from differentiating `F(r) S′² = 1` and `hK(r) = −S²`. `cc_dF`: `∂_U F`, `∂_V F` from
  `kr_comp_U`, `kr_comp_V`. **`cc_isGeodesicOn`: for every `t₀` and `[a, b] ⊂ (0, Mπ)`,
  `γ = cc_γ = Φ(η(τ), t₀)` is `(se_S hM).IsGeodesicOn`** (Koszul form of `g = F·gM`, in `W`'s chart).
* **③ — BUILT.** `cc_unit_energy`: on the manifold `g(γ′, γ′) = −1`, and `g(γ′, χ) = 0` for the boost Killing field
  `χ = sq_L = (−U/4M, V/4M)`, `∂_t` pushed forward by `Φ`: Killing energy zero.

Limit: the angular sphere is not in `se_S` (the radial plane), as throughout the kit.
-/

/-!
# Probe `r7703+71.2` (campaign 112): P2's `prop:cycloid` (corrected, `E = 0`) on the interior chart, the patch ranges, the two continuations' coefficients and the 4D interior form

Registration: `computations/formalisation/r7703_71_campaign112/PREDICTION.md`. Nothing imports this file, and it
imports only Mathlib. It starts as a copy of campaign 111's `probes/CircleKretschmann.lean` (namespace renamed
`ShadowProbe.CircleExteriorProbe`, all old names kept; the older headers below are kept verbatim and still name the
namespaces of their own campaigns). Everything new has the prefix `cy_` and sits just before the `#print axioms`
block.

* **1a-① and 1b — BUILT** (`section CyCycloid`). `cy_proper_time`: `∫₀^η 2M cos²(s/2) ds = M(η + sin η)`;
  `cy_Mpi`: from `η = 0` to `π` it is `Mπ`. `cy_τ_strictMonoOn`, and its inverse `cy_η` on `[0, Mπ]`
  (`cy_η_spec`, `cy_η_τ`, `cy_η_mem_Ioo`), with `cy_hasDerivAt_η`: `dη/dτ = 1/(M(1 + cos η))`.
* **1a-② — BUILT.** `cy_radial`: `dr/dτ = −sin η/(1 + cos η)` and `(dr/dτ)² = 2M/r − 1` (`E² − 1 + 2M/r` at
  `E = 0`). `cy_ends`: `r → 2M` and `dr/dτ → 0` as `τ → 0⁺` (at rest at `r = 2M`), `r → 0` as `τ → Mπ⁻`.
* **1a-③ — BUILT, through the registered fallback** (`section CyDiag`, `section CyGeodesic`). `cy_diag_Γ`: the
  Christoffel symbols (campaign 110's `kr_Γ`) of `diag(A(x⁰), B(x⁰))` in closed form. `cy_g`: the interior chart's
  metric `−4M²cos⁴(η/2) dη² + tan²(η/2) dt²`, written `diag(−(M(1 + cos η))², (1 − cos η)/(1 + cos η))`.
  `cy_geodesic`: `c(τ) = (η(τ), t₀)` satisfies `c″ᵃ + Γᵃ_bd c′ᵇc′ᵈ = 0` on `0 < τ < Mπ` (`cy_IsGeodesic`), is unit
  timelike, and has `E = −g(c′, ∂_t) = 0`.
* **2b — BUILT** (`section CyForms`). `cy_interior_forms`: `2M/r − 1 = tan²(η/2) = (1 − cos η)/(1 + cos η)`,
  `(1 − 2M/r)⁻¹(dr/dη)² = −4M²cos⁴(η/2) = −(M(1 + cos η))² = −(dτ/dη)²`, `r² = M²(1 + cos η)²`.
* **4a — BUILT.** `cy_regionI_coeffs` (at `z = iρ`) and `cy_regionI_schw` (`r = M(1 + cosh ρ)`).
* **5a — BUILT.** `cy_backseam_coeffs` (at `z = π + iρ′`) and `cy_backseam_schw` (`r = M(1 − cosh ρ′)`).
* **6a — BUILT.** `cy_patches`: the six patches' `r`-ranges, each onto; `r` even and `τ` odd under `η ↦ −η`.
* **6c — BUILT** (`namespace KRModel`). `cy_backseam_not_kruskal`: `rK ≠ M(1 − cosh ρ′)` on `{UV < 1}`.

Limits: the interior chart `(η, t)` is a coordinate metric, not tied to `sk_S` (row 2a). "Analytic continuation
of the metric" is read as substituting into each coefficient's holomorphic extension with `dz² ↦ (dz/dρ)² dρ²`.
-/

/-!
# Probe `r7701+71.1` (campaign 111): P2's `prop:Kretschmann`, `prop:critical` and `cor:Kretschmann_at_z0`

Registration: `computations/formalisation/r7699_71_campaign111/PREDICTION.md`. Nothing imports this file, and it
imports only Mathlib. It starts as a copy of campaign 110's `probes/Kretschmann.lean` (namespace renamed
`ShadowProbe.CircleExteriorProbe`, all old names kept; the older headers below are kept verbatim and still name
the namespaces of their own campaigns). Everything new has the prefix `ck_` and sits just before the
`#print axioms` block.

* **7e — BUILT** (`section CkChain`, any complete non-trivially normed field of characteristic `0`).
  `ck_order_two`: `h` analytic at `z₀` with `h z₀ = 0`, `h′ z₀ = 0`, `h″ z₀ ≠ 0` has analytic order `2`.
  `ck_chain_rule`: then `c/h⁶` (`c ≠ 0`) has meromorphic order `−12` at `z₀`, a pole of order exactly `12`.
* **7c — BUILT** (`section CkC`, over `ℂ`). `ck_pole_pi`: `48M²/r(z)⁶`, `r(z) = M(1 + cos z)`, has meromorphic
  order `−12` at `π`; `ck_K_form`: it equals `48/(M⁴(1 + cos z)⁶)`; `ck_pole_pi'`: the order in that form.
  The registered expected stop (`analyticOrderAt (1 + cos) π = 2`) did not occur: Mathlib's
  `analyticOrderAt_eq_nat_iff_iteratedDeriv_eq_zero` gives it, so the fallback was not needed.
* **7d — BUILT.** `ck_order_zero`: order `0` at `z = 0` (analytic, non-zero there); `ck_bounded_zero`:
  `48M²/r⁶ ≤ 48/M⁴` on `(−π/2, π/2)`; `ck_value_zero`: the value `3/(4M⁴)` at `0`.
* **Row 3 — BUILT** (`section CkR`, over `ℝ`). `ck_prop_critical`: critical points exactly `πℤ`
  (`ck_critical`); `r = 2M`, `r″ = −M` at `2kπ` (`ck_critical_even`); `r = 0`, `r″ = M` at `(2k + 1)π`
  (`ck_critical_odd`); all non-degenerate; `0 ≤ r ≤ 2M` everywhere (`ck_max_min`).
* **8a — BUILT.** `ck_mislabel`: `48M²/(M(cos z − 1))⁶` has order `−12` at `0`.
* **7a, 7b — BUILT** (`namespace KRModel`, on campaign 110's `kr_schwarzschild`, the Kretschmann scalar of the
  Kruskal chart's coordinate Riemann tensor). `ck_horizon`: `K = 3/(4M⁴)` on `UV = 0`; `ck_bifurcation`: at
  `U = V = 0`. `ck_interior`: `K = 48/(M⁴(1 + cos η)⁶)` wherever `r = M(1 + cos η)`; `ck_interior_witness`: every
  `η` with `1 + cos η ≠ 0` is reached, with `UV ≥ 0`.
* **Headlines.** `ck_prop_Kretschmann` (7a–7d) and `ck_cor_Kretschmann_at_z0` (8a with 7d).

Interpretive, not formalised: "generated by the chain rule" and the counterfactual labelling, whose formal content is
`ck_chain_rule` and `ck_mislabel`.
-/

/-!
# Probe `r7697+71.1` (campaign 110): `7c` staged, the Schwarzschild curvature singularity lies in the black-hole region and on no finite exterior slice

Registration: `computations/formalisation/r7697_71_campaign110/PREDICTION.md`. Nothing imports this file, and it
imports only Mathlib. It starts as a copy of campaign 107's `probes/NullGeodesic.lean` (namespace renamed
`ShadowProbe.CircleExteriorProbe`, all old names kept; the older headers below are kept verbatim and still name the
namespaces of their own campaigns). Everything new has the prefix `kr_` and sits just before the `#print axioms`
block.

* **① The locus and the slices — BUILT** (`namespace KRModel`). `kr_Sig = {UV = 1}`.
  `kr_JpastSet`: `J⁻(O) = {U < 0}` on `W`; `kr_BH_eq`: the black-hole region `kr_BH = W ∖ J⁻(O)` is `{U ≥ 0}`.
  `kr_locus_BH`: `Σ ∩ {V > 0}` lies in the closure (in `P`) of `val '' kr_BH`, and `U > 0` on it;
  `kr_Sig_closure_W`: `Σ ∩ closure W = Σ ∩ {V > 0}`. `kr_slice_far`: for every `Θ` and `τ`,
  `Σ ∩ closure (val '' slice τ) = ∅`. `kr_r_to_zero`: `r → 0⁺` along `kr_toSig` (`UV → 1⁻` in `W`, a non-trivial
  filter: `kr_toSig_neBot`), and conversely `UV → 1⁻` as `r → 0⁺`.
* **② Curvature in coordinates — BUILT** (`section KrCurvature`). For `g : (Fin n → ℝ) → Matrix (Fin n) (Fin n) ℝ`:
  `kr_pd f x c` (the classical partial derivative, along the `c`-th coordinate line), `kr_Γ` (index form, with the
  matrix inverse `(g x)⁻¹`), `kr_Riem` (`R^a_{bcd} = ∂_cΓ^a_{db} − ∂_dΓ^a_{cb} + Γ^a_{ce}Γ^e_{db} − Γ^a_{de}Γ^e_{cb}`),
  `kr_Rlow`, `kr_Rup` and `kr_K = R_{abcd}R^{abcd}`. Sanity: `kr_K_const` (a constant metric has `K = 0`) and
  `kr_K_sphere` (the round sphere of radius `ρ ≠ 0` in `(θ, φ)`, `sin θ ≠ 0`, has `K = 4/ρ⁴`). The index form is used
  instead of `ng_Γ`, since it is what makes ③ computable.
* **③ The warped product — BUILT, not the fallback** (`section KrWarped`; the registered expected stop was not hit).
  `kr_WD` holds `F, R` and their partials to order two (one mixed partial each); `kr_WD.Good D Ω` says `Ω ⊆ ℝ²` is
  open, `F, R > 0` on `Ω`, and each partial is the derivative along its coordinate line. `kr_WD.gW` is
  `g = −F dU dV + R²(dθ² + sin²θ dφ²)` in `(U, V, θ, φ)`. Proved component by component: the inverse (`gW_inv`),
  `∂g` (`gW_pd`), all 64 `Γ` (`Γ_eq`), all 256 `R^a_{bcd}` (`Riem_eq`, 40 non-zero, table `kr_RWv`), and
  **`kr_WD.kr_warped`**: for `(U, V) ∈ Ω`, `sin θ ≠ 0`,
  `K = k₂² + 8|∇∇R|²/R² + 4(1 − |∇R|²)²/R⁴` with `k₂ = 4(F F_UV − F_U F_V)/F³` (`k2`),
  `|∇R|² = −(4/F)R_U R_V` (`gradR2`) and `|∇∇R|² = (8/F²)(∇_U∇_U R ∇_V∇_V R + R_UV²)` (`hessR2`).
* **④ `KRModel.kr_schwarzschild` — BUILT** (on ③ as proved, not on a cited formula). `kr_SD M` is the Schwarzschild
  data (`F = FS M = (32M³/r)e^{−r/2M}`, `R = rK M`, `r_U = −V/h′(r)`, `r_V = −U/h′(r)` and the second partials);
  `kr_SD_good`: it is good on `{UV < 1}` (`hK` derivative identities, `rinv_hasDerivAt`). At every `(U, V, θ, φ)`
  with `UV < 1` and `sin θ ≠ 0`: `kr_K (kr_SD M).gW x = 48M²/r⁶`, `r = rK M (U, V)`.
* **⑤ `KRModel.kr_blowup` and `kr_cor_densities_c` — BUILT.** `kr_KS M θ φ x` is `K` at `x ∈ W` and angles
  `(θ, φ)`. `kr_blowup`: for `sin θ ≠ 0`, `K → +∞` along `kr_toSig` (`UV → 1⁻` in `W`). `kr_cor_densities_c`
  (7c): `K = 48M²/r⁶` on `W`; `kr_toSig` is non-trivial and `K → ∞` along it; every `p ∈ Σ ∩ closure W` is
  approached non-trivially from `W`, `K → ∞` as `x → p`, `p` lies in the closure of the black-hole region and
  `U > 0` there; and for every `Θ`, `τ`, `Σ ∩ closure (val '' slice τ) = ∅`.

Limits: coordinate-level curvature (the classical partial derivatives along coordinate lines, on the
`(U, V, θ, φ)` chart of `{UV < 1} × (sin θ ≠ 0)`); it is not linked to the manifold `seW` or to `ng_Γ`. The angular
factor is added by hand (`kr_WD.gW`), not built as a product manifold.
-/


/-!
# Probe `r7691+71` (campaign 107): `2iii` on `N`, a null geodesic stays null, witnessed on Schwarzschild's `∂J⁻(𝒥⁺)`

Registration: `computations/formalisation/r7691_71_campaign107/PREDICTION.md` ("Campaign 107: 2iii"; P1,
`corpus/BH_causality_v2.tex` l.176–180: for `γ` a null geodesic segment, `g(γ̇, γ̇) = 0` along the
whole segment). Nothing imports this file, and it imports only Mathlib. It starts as a copy of
campaign 106's `probes/StationaryHorizon.lean` (namespace renamed `ShadowProbe.NullGeodesicProbe`, all
old names kept; the older headers below are kept verbatim and still name the namespaces of their own
campaigns). Everything new has the prefix `ng_` and sits just before the `#print axioms` block.

* **① Definitions — BUILT.** `ng_kos G y u v w = ½(DG(u)(v,w) + DG(v)(u,w) − DG(w)(u,v))` (Koszul);
  `ng_Γ G y u v`, the Christoffel map, as the `z` with `G(y)(z, ·) = kos(y)(u, v, ·)` (`ng_Γ_spec`,
  `ng_Γ_unique` for `G(y)` nondegenerate, `ng_Γ_exists` on finite-dimensional `E`).
  `MSpacetime.IsGeodesicOn S γ a b`: for each `t ∈ [a, b]`, on some `(t − ε, t + ε)`, `γ` stays in
  the preferred chart at `p = γ t`, `c = φ_p ∘ γ` (`ng_c`) is `C²`, and `c″ = −Γ(c)(c′, c′)` in its
  Koszul form `hRep g p (c)(c″, w) = −kos(c)(c′, c′, w)` for all `w` (no inverse of `g`); `ng_geod_iff`
  shows it is the same as `c″ = −ng_Γ (hRep g p) c c′ c′` where `hRep g p (c)` is nondegenerate.
* **② `MSpacetime.ng_energy_const` — BUILT.** On `IsGeodesicOn` with `LocallyOneChart` and `γ` in
  `M`, `t ↦ g(γ t)(γ̇, γ̇)` is constant on `[a, b]`: `d/dt G(c)(c′, c′) = DG(c′)(c′, c′) + 2G(c″, c′)`
  `= 0` (Koszul at `w = c′`, `ng_chart_energy_deriv`); the intrinsic value equals the chart value
  (`ld_h_eq_hRep`, `ng_vel_chart`); zero derivative on `[a, b]` ⇒ constant.
* **③ `MSpacetime.ng_cor_threefold_iii` — BUILT.** A geodesic on `[a, b]` null at one `t₀ ∈ [a, b]` is
  null at every `t ∈ [a, b]`.
* **④ `NGModel.ng_witness` — BUILT on `W` (not the flat fallback).** On `se_S hM` (Schwarzschild,
  `g = −F dU dV`), the horizon generator `γ s = (0, V₀ + s)` on `[0, b]` lies in
  `𝓗⁺ = S.H J = ∂J⁻(𝒥⁺)` (`sx_prop_causal_alignment`, `st_mem_H`), is `IsGeodesicOn` (`ng_isGeodesicOn`:
  in `W`'s inclusion chart `c″ = 0`, and the Koszul form of `F • gM` vanishes for `u = ∂_V` at
  `U = 0`, since `∂_V F = 0` there (`ng_FS_dV`: `F` depends on `UV` only) and `gM(∂_V, ∂_V) = 0`;
  also `c″ = −ng_Γ(…)` in the inverted form, via `ng_nondeg`), has `γ̇ = ∂_V`, is null at `s = 0`,
  and so by ③ is null on all of `[0, b]`.

Limits: the radial plane only; the geodesic condition is local (an open interval about each `t` in
the chart at `γ t`), so a segment on `[a, b]` is a geodesic slightly beyond its endpoints.

# Campaign 106's header, kept
-/

/-!
# Probe `r7689+71.1` (campaign 106): `cor:stationary` on `N`, witnessed on Schwarzschild's `∂J⁻(𝒥⁺)`

Registration: `computations/formalisation/r7689_71_campaign106/PREDICTION.md` (P1 `cor:stationary`,
l.283; inventory row 5). Nothing imports this file, and it imports only Mathlib. It starts as a copy
of campaign 100's `probes/SchwarzschildConformal.lean` (namespace renamed
`ShadowProbe.StationaryHorizonProbe`, all old names kept). Merged in, names kept:
* campaign 96's `probes/KillingWhole.lean` kit (`ld_`, `kl_`, `kg_`, `kw_`, with
  `kw_lemma_killing_whole`), in `section KillingWholeKit` after `SXModel`. The eight declarations it
  shares with the campaign-68 kit already here (`chartRep`, `hRep`, `ld_mdifferentiableAt_symm`,
  `ld_hRep_apply`, `ld_mfderiv_symm_chart`, `ld_mfderiv_chart_symm`, `ld_chartRep_apply_chart`,
  `ld_h_eq_hRep`) were checked textually identical (up to docstrings) and are kept once, in
  campaign 100's `section Manifold`;
* from campaign 97 ③'s `probes/SchwarzschildKilling.lean`: `sq_smul_hasFDerivAt`,
  `sq_smul_fderiv_apply`, `sq_L`, `sq_L_apply` (the rest of `sq_` is on the model plane `ℝ²` with
  its own radius function, and is not needed on `W`).

Everything new has the prefix `st_`, just before the `#print axioms` block.

* **① `MSpacetime.IsKillingHorizon S X Hs` and `st_cor_stationary` — BUILT.** The predicate is
  `kw_lemma_killing_whole`'s hypotheses stated pointwise on `Hs`: `X` `C¹` as a section and `≠ 0` on
  `Hs`; `hRep g` differentiable near `Hs`; `L_X g = 0` near `Hs`; through each `p ∈ Hs` an integral
  curve of `X` inside `Hs`, null somewhere (`st_null_of_isKillingHorizon` then makes `X` null on all
  of `Hs`). `st_cor_stationary`: along every generator `γ` on `[a, b]` with `γ '' [a, b] ⊆ S.H J`, all
  of `kw_lemma_killing_whole`'s conclusions (null, `kg_Related` for every pair, `Δτ = 0`, and the
  horizon splitting's `h = g`, `Δx = 0`, `Δτ = 0`). **Rigidity is the hypothesis, as P1 cites it**
  (the proof of `cor:stationary`: Hawking, with analyticity); it needs the Einstein equations, which are not in the kit.
  "Stationary" has no formal content beyond invoking it.
* **② `st_witness` — BUILT on `W` (the registered expected stop was not hit).** On `se_S hM`,
  `S.H J = ∂J⁻(𝒥⁺)` (`sx_prop_causal_alignment`) is a Killing horizon of
  `χ = ∂_t = (V∂_V − U∂_U)/4M` (`st_isKillingHorizon`), and two events `(0, V₁) ≠ (0, V₂)` on it are
  metrically coincident. The Lie derivative on the `Opens` subtype (`st_lieDeriv`) goes through
  `ld_lieDeriv_chart_self` in the inclusion chart (`se_dchart`), then the germs `hRep g = F • gM` and
  `chartRep χ = sq_L` at `x` (`st_chartLie_congr`); `χ(F) = 0` from `F`'s boost invariance
  (`st_chi_F`). `χ` is `C¹` as a section via `contMDiffAt_section` and `ld_chartRep_eq_triv`
  (`st_hX`); the integral curve `γ s = (0, V₀ e^{s/4M})` is read through the inclusion chart
  (`st_integral`).

Limits (as registered): the radial plane only; rigidity is assumed.

# Campaign 100's header, kept
-/

/-!
# Probe `r7681+71` (campaign 100): a `ConformalExtension` on Schwarzschild's `W`, so that `𝓗⁺ = ∂J⁻(𝒥⁺)`

Registration: `computations/formalisation/r7681_71_campaign100/PREDICTION.md`. Nothing imports this
file, and it imports only Mathlib. It starts as a copy of campaign 99's
`probes/SchwarzschildRetarded.lean` (namespace renamed `ShadowProbe.StationaryHorizonProbe`,
all old names kept), with campaign 91's `cd_prop_causal_alignment` (from `probes/ConeDisjoint.lean`,
name kept) copied in. Everything new has the prefix `sx_` and sits in namespace `SXModel`, just
before the `#print axioms` block.

Setting: campaign 98's `se_S hM` on `N = W = {V > 0, UV < 1}`, `g = −F dU dV`, `T = (1, 1)`;
campaign 90's flat `S̃ = cz_St` on `P` (`g̃ = −du dv`, `M̃ = P`, `T̃ = (1, 1)`), `𝒥⁺ = cz_scri`.

* **① `sx_ext : ConformalExtension (se_S hM) cz_St` — BUILT, every field.** `ι = cz_fB ∘ val`,
  `(U, V) ↦ (arctan U, arctan V)`; open embedding (`cz_fB_isOpenEmbedding` after the open
  inclusion); `C¹` (`contMDiff_subtype_val`); `Dι = diag(1/(1+U²), 1/(1+V²))` (`sx_dι_eq`, via
  `mfderiv_comp` and `se_dchart`, the inclusion being the chart); `Ω = (F (1+U²)(1+V²))^{−1/2}`.
* **② `sx_hI` — BUILT:** `I⁻(O) = D = {U < 0}` is `ι⁻¹ Ĩ⁻(𝒥⁺) = ι⁻¹ {u < 0, v < π/2}`.
* **③ `sx_prop_causal_alignment` — BUILT:** `cd_prop_causal_alignment` for `sx_ext`, static
  observer, `Θ = se_Θst M r₀`, `c = 0`: `𝓗⁺ = ∂J⁻(𝒥⁺)`, `val '' ∂J⁻(𝒥⁺) = {U = 0, V > 0}`,
  `r = 2M` there, properness, `KLi = KLs = ∂J⁻(𝒥⁺)` (slices and cones), the tangency clause in
  its general form, and no cone meets `∂J⁻(𝒥⁺)`.
* **`sx_nonvacuous` — BUILT** (`M = 1`, `r₀ = 4`): `(0, 1) ∈ ∂J⁻(𝒥⁺)`, `Ω(0, 1) ≠ Ω(0, 2)`, and
  `g` is not flat at `(0, 1)`.
* The optional instantiation of the tangency clause at a horizon point is not attempted.

Limits (as registered): the radial plane only; `S̃` is flat `ℝ²`, not Penrose's compactified
Schwarzschild.

# Campaign 99's header, kept
-/

/-!
# Probe `r7679+71` (campaign 99), ④′: the retarded slicing on Schwarzschild's region I is not Cauchy

Registration: `computations/formalisation/r7679_71_campaign99/PREDICTION.md`. Nothing imports this
file, and it imports only Mathlib. It starts as a copy of campaign 98's `probes/SchwarzschildEF.lean`
(namespace renamed `ShadowProbe.StationaryHorizonProbe`, all old names kept), with the `r_U`,
`r_V` calculus of campaign 98's ④ (`sa_uP`, `sa_rD`, `sa_uD`, `sa_rK_hasFDerivAt`,
`sa_uP_hasFDerivAt`, `sa_uP_contDiffOn`, `sa_k`, `sa_hK'_pos`, `sa_uD_U`, `sa_uD_V`, from
`probes/SchwarzschildAlign.lean`, names kept, `sa_IP` read as `Model.seR`) copied in. Everything new
has the prefix `sr_` and sits in namespace `SRModel`, just before the `#print axioms` block.

Setting: campaign 98's `se_S hM` on `N = W = {V > 0, UV < 1}`, `g = −F dU dV`, `T = (1, 1)`;
`D = (se_S hM).D (range (se_Ost hM hr₀))`, which is region I `{x | x.1.1 < 0}` (`sr_D_eq`, from
`se_foundation`). `Θ_ret = sr_Θ M a η`, `sr_Θ M a η x = a (−4M log(−U) + η r)`, `r = se_r M x`.

**ⓐ Temporality and the sharp η bound — BUILT.**
* `sr_dU_pos_iff`: on `D`, `dΘ(∂_U) > 0 ↔ η (r − 2M) < 2r` (P1's `η f < 2`); via
  `k = 4M h′(r) − ηV(−U) = e^{r/2M}((2 − η)(r/2M − 1) + 2)` (`sr_k_eq`) and `Θ_U = a k/((−U)h′)`.
* `sr_temporal`: `IsTemporalOn D Θ_ret` for `0 < η ≤ 2` (`Θ_V = aη(−U)/h′ > 0`, `Θ_U > 0`).
* `sr_not_temporal`: for `η > 2`, at the point `U = −1`, `r = 2Mη/(η − 2)` of `D`, the future null
  `∂_U` has `dΘ(∂_U) = 0`; hence `¬ IsTemporalOn D Θ_ret`.

**ⓑ The refutation — BUILT.**
* `sr_curve`: `γ(s) = (U₀, eˢ)`, `U₀ < 0`, as an `InextCausalCurveIn D` (null, velocity `(0, eˢ)`,
  no breaks; `V → ∞` to the future; to the past a limit `p ∈ D` would force `V(p) = 0`).
* `sr_not_cauchy`: for every `a, η > 0` there is such a curve (`U₀ = −1`) and a level (`0`) that
  `Θ_ret ∘ γ = aη r > 0` never takes. `sr_not_isCauchy`: `¬ IsCauchyTemporalOn D Θ_ret`.
  It does not depend on ⓐ.

**ⓒ The future half — BUILT** (the registered expected stop, the monotone-limit step, was not hit).
* `sr_coord_mono`: `U`, `V` non-decreasing on `[0, ∞)` along every causal curve (`mono_brk`).
* `sr_future_diverges`: `Θ_ret → +∞` along every `InextCausalCurveIn D`, for **every** `a, η > 0`
  (the bound `η ≤ 2` is not needed): bounded monotone limits would land in `D`; `U → 0⁻` gives
  `−log(−U) → ∞`; `V → ∞` with `U ≤ L < 0` gives `h(r) = −UV → ∞`, so `r → ∞`.
* The stretch (`Θ_ret → −∞` towards past null infinity) is not attempted.

**Non-vacuity — BUILT.** `sr_nonvacuous` (`M = 1`, `r₀ = 4`, `a = 1`): the witness (`(−1, eᵗ)`,
level `0` missed, `Θ_ret → ∞` along it), `¬ IsCauchyTemporalOn` at `η = 1`, temporality at `η = 1`,
and the failure at `η = 3` (at `r = 6`).

`#print axioms` for every new declaration at the end: each reads
`[propext, Classical.choice, Quot.sound]`.

# Campaign 98's header, kept
-/

/-!
# Probe `r7677+71` (campaign 98), pieces ① and ②: Schwarzschild on EF's domain `W = {V > 0, UV < 1}`

Registration: `computations/formalisation/r7677_71_campaign98/PREDICTION.md`, pieces ① and ② only
(③ and ④ are `probes/SchwarzschildAlign.lean`, not in this file). Nothing imports this file, and it
imports no other probe. It starts as a copy of campaign 97's `probes/SchwarzschildKruskal.lean`
(namespace renamed `ShadowProbe.SchwarzschildEFProbe`, all old names kept), with campaign 91's cone
disjointness (`cd_chr_of_mem_closure_Jpast` … `cd_cone_disjoint`, from `probes/ConeDisjoint.lean`)
and campaign 92's stretch (`hs_stretch` … `hs_stretch_N`, from `probes/HorizonStretch.lean`) copied
in, names kept. Everything new has the prefix `se_` (`seR`, `seW`, `seK`, … for sets and
spacetimes) and sits in one section before the `#print axioms` block.

**① The foundation on `W` — BUILT.**
* `N := ↥SEModel.seW`, `seW : TopologicalSpace.Opens P` the open set `{V > 0, UV < 1}` of the null
  plane `P = ℝ²` (the model space), with Mathlib's `Opens.instChartedSpace` / open-subset
  `IsManifold` (one chart, the inclusion; `se_dchart`: `mfderiv` of the chart is `id`).
* `se_S hM = se_flat.cz_scale F`, `M = univ`, `g = F · (−dU dV)` (`se_hRep`), `T = ∂_U + ∂_V`,
  `F = FS M` (campaign 97, positive and `C¹` on `{UV < 1} ⊇ W`); `se_locallyOneChart`.
* The chart spacetime agrees with `mink` restricted to `W` (`se_chartSp_agree`, through the new
  `Spacetime.SeAgree` congruence kit), and `≪` on `W` is the flat relation (`se_chr_iff_lt`), straight
  segments staying in `W` (`se_seg_mem`).
* `se_foundation`: for the observer `se_O` on `UV = −a²`: `hOD`, `D` = region I `{U < 0, V > 0}`,
  `hmono`, `J ⊆ M`, **`S.H J = {U = 0}` in `W`, i.e. `{U = 0, V > 0}` in the plane** (frontier
  taken in `W`), `𝓗⁺ ⊆ M` (the clause that failed on campaign 97's `Pt`), `𝓗⁺ ≠ ∅`, `r = 2M` on `𝓗⁺`.

**② `t` Cauchy on region I, and the headline — BUILT.** The registered expected stop (transport
through `V ↦ log V`) was not hit.
* `Model.se_cauchy_RI`: `Θ_k = k (log V − log(−U))` is Cauchy temporal on `mink` restricted to region
  I, by carrying each inextendible causal curve through `ψ(U, V) = (U, log V)` to `{U < 0}`, where
  campaign 81's `hl_cauchy_Θ₀` applies (`Θ_k = k · Θ₀ ∘ ψ`); temporality directly.
* `SEModel.se_cauchy`: hence `IsCauchyTemporalOn (D J) Θ_k` on `W` (`SeAgree`, `ch_isCauchy_VN`,
  `cz_scale_isCauchyTemporalOn`).
* `se_proper_time`: with `k = 2M√(1 − 2M/r₀)`, `a = √h(r₀)`, the observer `se_Ost` sits at `r = r₀`,
  `Θ(O τ) = τ` and `g(Ȯ, Ȯ) = −1`: `Θ = √(1 − 2M/r₀) · t` is the static observer's proper time.
* `SEModel.se_headline`: Cauchy, adapted, `D` = region I, `𝓗⁺ = {U = 0, V > 0}` with `r = 2M`,
  properness, `KLi = KLs = 𝓗⁺` for the slices (`mh_causal_alignment_gh_N`) and the cones
  (`mc_cone_kuratowski_N`), cone disjointness (`cd_cone_disjoint`), `𝓗⁺ ≠ ∅`, every cone non-empty
  (`se_O_mem_cone`). `se_nonvacuous` at `M = 1`, `r₀ = 4`: also `g ≠ g_flat`, `F` non-constant.
* `se_stretch`: the stretch, for `W`'s subtype metric (`hs_stretch_N` with `hm = rfl`); `𝓗⁺` lies
  in no compact set of `W` (`se_H_not_compact`), so the `ε`-stretch eventually leaves every compact.
* Not done: campaign 89's `ConformalExtension` (`𝓗⁺ = ∂J⁻(𝒥⁺)`, `cd_prop_causal_alignment`) is
  not instantiated on `W`; the headline is stated through `mh_causal_alignment_gh_N`,
  `mc_cone_kuratowski_N` and `cd_cone_disjoint` with `J = range O`.

Curvature is neither checked nor used. `#print axioms` at the end: every line reads
`[propext, Classical.choice, Quot.sound]`.

# Campaign 97's header, kept

## Probe `r7675+71` (campaign 97), piece ①: Schwarzschild as an `MSpacetime` in Kruskal's radial plane

Registration: `computations/formalisation/r7675_71_campaign97/PREDICTION.md`, piece ① only (② is
`probes/SchwarzschildKilling.lean`, not in this file). Nothing imports this file, and it imports no
other probe. It starts as a copy of campaign 91 ③'s `probes/CurvedTangency.lean` (namespace renamed
`ShadowProbe.SchwarzschildKruskalProbe`, all old names kept), with campaign 80's Kruskal radius
(`hK`, `hK'`, `rinv`, `rK`, `FS`, from `probes/TangencyCondition.lean`, names kept, namespace
`Kruskal`) copied in. Everything new has the prefix `sk_` and sits in one section before the
`#print axioms` block.

## NEW (campaign 97 ①)

**`r` and `F` on all of `{UV < 1}` — BUILT.** `rinv` already inverts `h` on all of `(−1, ∞)`, i.e. on
all of `−UV > −1`. `Kruskal.sk_rinv_contDiffOn` (`C¹` on `(−1, ∞)`, inverse function theorem,
`h′(r) = r e^{r/2M}/4M² > 0`), `sk_rK_contDiffOn : ContDiffOn ℝ 1 (rK M) {UV < 1}`, `sk_rK_spec`
(`r > 0`, `h(r) = −UV`), `sk_rK_eq_two_iff` (`r = 2M ↔ UV = 0`), `sk_FS_contDiffOn`, `sk_FS_pos`,
`sk_FS_nonconst` (`F = 16M²/e` at `r = 2M`, `8M²/e²` at `r = 4M`).

**The spacetime `sk_S hM` — BUILT.** `N = Pt`, `M = sk_MN = φ⁻¹{UV < 1}`,
`sk_S hM = (minkN.restrictM M).cz_scale F̃`, where **`F` is handled by extension**: `sk_F` is
`FS ∘ φ` on `M` and `1` off `M` (positive everywhere, so all of campaign 90's `cz_scale_*` lemmas
apply unchanged); `NModel.sk_hRep`: in the global null chart, `hRep g p₀ (U,V) = F(U,V) • gM`, i.e.
`g = −F(r(U,V)) dU dV`, at every point of `{UV < 1}`. The only new scaling lemma is
`MSpacetime.sk_scale_locallyOneChart`, which asks `F` to be `C¹` only on the chart images of `M`
(not on the whole chart target, as `cz_scale_locallyOneChart` does).

**`LocallyOneChart` — BUILT (the registered expected stop was not hit).**
`NModel.sk_locallyOneChart : (sk_S hM).LocallyOneChart`, from `me_locallyOneChart.restrict` and
`sk_FS_contDiffOn`. **The causal transfer — BUILT:** `sk_R` (the restriction) has `OneChart p₀`,
and its chart spacetime is `Model.sk_K = mink.restrict {UV < 1}` (`sk_chartSp_eq`); `sk_chr_iff`,
`sk_cau_iff`, `sk_mem_D_iff`, `sk_mem_H_iff` move `≪`, `≤`, `D`, `𝓗⁺` to `sk_K`, where straight
segments stay in `{UV < 1}` (`sk_seg_mem`: `UV` is convex along a segment with `U`, `V`
non-decreasing).

**The observer and its horizon — BUILT, with one registered clause corrected.**
`NModel.sk_static_observer` (`r₀ > 2M`): `c = h(r₀) > 0`, `O(σ) = φ⁻¹(−√c e^{−σ}, √c e^{σ})` on
`UV = −c` at `r = r₀`; `NModel.sk_observer` (any `a > 0`): `I⁻(range O) = D = {U < 0} ∩ M`
(regions I and IV), `hmono`, `range O ⊆ M`, and
`𝓗⁺ = ∂J⁻(O) = {U = 0} ∪ {U < 0, UV = 1}`. **Correction to the registration:** the frontier is
taken in `N = Pt`, and `M = {UV < 1}` is not closed, so `∂J⁻(O)` also contains the past singularity
`r = 0` of region IV, `{U < 0, UV = 1}`, which lies outside `M`. What holds is
`𝓗⁺ ∩ M = {U = 0}` (non-empty, `⊆ M`), and `r = 2M` on `𝓗⁺ ∩ M` (`sk_H_r` is the last clause of
`sk_observer`). The registered `S.H J = {U = 0}` (and with it the `𝓗⁺ ⊆ M` hypothesis of
`mh_causal_alignment_gh_N`) needs `N = M` as a manifold in its own right (row 8's `Opens` route).

**3a, `NModel.sk_cor_EF_events` — BUILT.** For `0 < V₁ < V₂`, `p = φ⁻¹(0, V₁)`, `q = φ⁻¹(0, V₂)`:
`p, q ∈ ∂J⁻(O)`, `p, q ∈ M`, `p ≠ q`, `S.Cau p q`, `¬ S.Chr p q`, `r p = r q = 2M`.

**Non-vacuity — BUILT.** `NModel.sk_nonvacuous`: at `M = 1`, `r₀ = 4`, `V₁ = 1`, `V₂ = 2` every
clause of 3a holds, `hRep g p₀ (0,0) ≠` the flat one (`F = 16/e ≠ 1`), and `F` is non-constant.

**Not done.** Curvature (`Ric = 0`) is neither checked nor used (that the metric is Schwarzschild's
is by definition of `F`, as in campaign 80). No Cauchy temporal function on `D` and no slice /
cone limits for `sk_S` (they need `𝓗⁺ ⊆ M`, see the correction above).

`#print axioms` at the end: every new headline reads `[propext, Classical.choice, Quot.sound]`.

---

*Inherited header of `probes/CurvedTangency.lean` (campaign 91 ③) follows.*
-/


/-!
# Probe `r7663+71` (campaign 91), piece ③: tangency instantiated on the curved `−F̂ dU dV`

Registration: `computations/formalisation/r7663_71_campaign91/PREDICTION.md`, piece ③ only (① is
`probes/ConeDisjoint.lean`, ② is `probes/FourDWitness.lean`; neither is in this file). Nothing imports
this file, and it imports no other probe. It starts as a copy of campaign 90 (a)'s
`probes/Compactification.lean` (namespace renamed `ShadowProbe.SchwarzschildKruskalProbe`, all old names
kept); everything new has the prefix `ct_` and sits in one section before the `#print axioms` block.

## NEW (campaign 91 ③) — BUILT

**The rescaled frame — BUILT.** On `cz_minkF hpos` (`g_F = −F̂(U,V) dU dV`, `F̂ : P → ℝ` positive, `C¹`):
`ℓ = ℓN` (`= ∂_V`, the flat witness's) and `n = ct_nN x = F̂(φ x)⁻¹ • nN x` (`= (2/F̂) ∂_U`), so
`g_F(ℓ, n) = −1`. `ct_frameHyp_scaled`: the frame hypotheses for `c • gM`, `ℓ = ∂_V`, `n = c⁻¹(2,0)`,
any `c > 0`; `ct_frameHyp`: the intrinsic `FrameHyp (g_F)_x ℓ n dΘ₀_x` at every `x ∈ D`
(via `mc_frameHyp_ofChart` and `ct_gCh_p₀ : gCh_F p₀ x = F̂(φ x) • gM`).

**The rate — BUILT.** `ct_ratio`: `dΘ₀(ℓ)/dΘ₀(n) = (−U/2)·F̂(U,V)`, which tends to `0` at `{U = 0}`
by continuity of `F̂`.

**The chart bound — BUILT (the registered expected stop was not hit).** `ct_bound`: `F̂` continuous
and positive ⟹ `F̂ ∘ φ > F̂(φ q)/2` near `q`, so `‖F̂(φ x)⁻¹ nvec‖ ≤ (2/F̂(φ q))‖nvec‖`.
`ct_dchartL_q`: in the preferred chart at any `q`, `dchartL q x ∘ dchartInvL p₀ x = ct_Tq q`, a
constant map (`nullInvL` if `t(q) < 0`, `id` otherwise), so `‖dchartL q x (n x)‖ ≤ ‖T_q‖·C` and
`dchartL q x (ℓ x) = T_q ∂_V` (constant).

**`ct_witness_tangency_F` — BUILT, at every horizon point `q`.** Along `𝓝[D] q` (proper): frame
hypotheses eventually, rate `→ 0`, the chart-`q` bound and limit `ℓ₀ = T_q ∂_V`, then
`mc_tangency_at_N` gives `dΘ^{e_q}/dΘ(n) → −g_{F,q}(T_q ∂_V, ·)`, and `mc_tangency_limit_N` in `φ`
gives `dΘ^φ/dΘ(n) → (F̂(φ q)/2) dU`.

**`ct_witness_headline_F` — BUILT.** The conclusion of `cz_witness_headline_F` with its (∀-frames)
tangency clause instantiated (the clause of `cz_witness_headline_F` itself is applied) at every
`q ∈ ∂J⁻(𝒥⁺) = 𝓗⁺`, plus `p₀ ∈ 𝓗⁺` with limit `−g_{F,p₀}(∂_V, ·) = (F̂(0,0)/2) dU`. Hypotheses: only
`hFc : ContDiff ℝ 1 F̂` and `hpos : ∀ y, 0 < F̂ y`, as in campaign 90.

**Non-vacuity — BUILT.** `ct_exp` (`F̂ = e^{UV}`): hypotheses hold, `p₀ ∈ 𝓗⁺`, `𝓝[D] p₀` proper,
frame and rate hold, `n ≠ nN` at `φ⁻¹(−1, 1)`, limit `½ dU` (since `e^{UV} = 1` on `{U = 0}`, this
`F̂` gives the flat limit). `ct_expV_differs` (`F̂ = e^V`): at `q = φ⁻¹(0, 1) ∈ 𝓗⁺` the limit is
`(e/2) dU ≠ ½ dU`.

-/

/-!
# (kept) Probe `r7661+71` (campaign 90), part (a): a genuine compactification, `Ñ = P ≠ N = Pt`

Registration: `computations/formalisation/r7661_71_campaign90/PREDICTION.md`, part (a) only (part (b),
the `ℝ² × S¹` Rindler witness, is not in this file). Nothing imports this file, and it imports no
other probe. It starts as a copy of campaign 89's `probes/ConformalBoundary.lean` (namespace renamed
`ShadowProbe.CompactificationProbe`, all old names kept); everything new has the prefix `cz_`.

## NEW (campaign 90)

**`Ñ` and `S̃` — BUILT.** `Ñ = P = ℝ × ℝ` with Mathlib's self-charted structure
(`chartAt = refl`, `extChartAt = PartialEquiv.refl`), a different type from the two-chart `Pt`.
`NModel.cz_St : MSpacetime P P`: `M̃ = P`, `g̃ = gM = −du dv` (campaign 81's, the convention of
`minkN` read in `φ`), `T̃ = (1, 1)`. `cz_locallyOneChart : cz_St.LocallyOneChart` (`hRep g̃ p = gM`,
`chartRep T̃ p = (1,1)`); `cz_oneChart`, `cz_chartSp_eq : chartSp cz_oneChart = mink` transport `≪` to
campaign 81's `mink`.

**The extension — BUILT.** `cz_ι = cz_fB ∘ φ : Pt → P`, `cz_fB (U, V) = (arctan U, arctan V)`.
`cz_ι_isOpenEmbedding`, `cz_ι_contMDiff : ContMDiff 𝓘(ℝ,P) 𝓘(ℝ,P) 1 cz_ι`,
`cz_dι_eq : mx_dι cz_ι x v = cz_DfB (φ x) (dchart p₀ x v)` with
`cz_DfB (U,V) = diag(1/(1+U²), 1/(1+V²))`, `cz_Ω x = ((1+U²)(1+V²))^{−1/2}` (`cz_Ω_sq`:
`Ω² = 1/((1+U²)(1+V²))`, from `ι*g̃ = −dU dV/((1+U²)(1+V²))`; `cz_Ω_nonconst`), and
`cz_witnessExt : ConformalExtension minkN cz_St` with every field. **The registered expected stop
(`LocallyOneChart` / `ContMDiff ι` across two distinct types) was not hit:** the target is the model
space, so `ContMDiff` is `contMDiff_iff_contDiff` composed with `φ`'s, and the self chart makes
`LocallyOneChart` constant data.

**Relative compactness — BUILT.** `cz_range_ι : range cz_ι = (−π/2, π/2)²`,
`cz_closure_range : closure (range cz_ι) = [−π/2, π/2]²`, `cz_isCompact_closure`, `cz_range_ne_univ`.

**`𝒥⁺` and `hI` — BUILT.** `cz_scri = {p | −π/2 < p.1 ∧ p.1 < 0 ∧ p.2 = π/2}`:
`cz_scri_subset_frontier : cz_scri ⊆ frontier (range cz_ι)`, `cz_scri ⊆ M̃`, `cz_scri_nonempty`,
`cz_mem_Ipast_scri : p ∈ cz_St.IpastSet cz_scri ↔ p.1 < 0 ∧ p.2 < π/2` (the lower bound `u > −π/2` of
`𝒥⁺` does not survive in `I⁻`), `cz_preimage_Ipast_scri : cz_ι ⁻¹' cz_St.IpastSet cz_scri = minkN.D JN`
(`= {U < 0}`).

**The witness theorems — BUILT.** `cz_witness_boundary`: `∂J⁻(𝒥⁺)` pulled back is `{U = 0}`,
non-empty, `= 𝓗⁺ = minkN.H JN` (by `mx_H_eq_boundary` with `hLt = cz_locallyOneChart`), with the
closure, compactness and `range ≠ univ` clauses. `cz_witness_headline`: `mx_prop_causal_alignment`
for `cz_witnessExt` and `Θ₀ ∘ φ`, every clause, tangency instantiated at `p₀` as in
`mx_witness_headline`. No hypothesis beyond the registration.

**Stretch, curved `N` — BUILT (tangency left in its general form).** `MSpacetime.cz_scale S F hF`
(`F > 0`, `g ↦ F g`): `FutTimelike`/`FutCausal`, `TStep`, `CStep`, `Chr`, `Cau`, `I⁻`, `J⁻`, `D`, `𝓗⁺`,
slices, properness, cones unchanged (`cz_scale_*`), `cz_scale_isCauchyTemporalOn`,
`cz_scale_locallyOneChart` (needs `F` `C¹` in each preferred chart). On `Pt`,
`cz_minkF hpos = minkN.cz_scale (F̂ ∘ φ)`, `g_F = −F̂(U,V) dU dV`, for any `F̂ : P → ℝ` positive and
`C¹`; `cz_witnessExtF : ConformalExtension (cz_minkF hpos) cz_St` (same `ι`,
`Ω² = 1/(F̂ (1+U²)(1+V²))`); `cz_witness_headline_F`: every clause of `mx_prop_causal_alignment`,
the tangency clause in its general (∀) form, not instantiated at a point (the null frame would have to
be rescaled by `F̂`). Non-vacuity: `cz_exp_nonvacuous` (`F̂ = e^{UV}`, `g_F ≠ g`). Schwarzschild's
Kruskal `F` (campaign 80's `r(U, V)`) is not brought in.

-/

/-!
# (kept) Probe `r7659+71` (campaign 89): `𝓗⁺ = ∂J⁻(𝒥⁺)` from a conformal extension, witnessed on `Pt`
compactified by `arctan V`, and `prop:causal-alignment` assembled whole

Registration: `computations/formalisation/r7659_71_campaign89/PREDICTION.md`. Nothing imports this
file, and it imports no other probe. It starts as a copy of campaign 88's `probes/ManifoldCones.lean`
(namespace renamed `ShadowProbe.ConformalBoundaryProbe`, all old names kept); everything new has the
prefix `mx_`.

## NEW (campaign 89)

**The definition.** `ConformalExtension S St` (`S` on `N`, `St` (`S̃`) on `Ñ`, same model `E`): `ι : N → Ñ`,
`isOpenEmbedding`, `contMDiff` (class `1`), `Ω > 0` with
`g̃_{ι x}(Dι v, Dι w) = Ω x ² g_x(v, w)` (`conformal`, with `Dι = mx_dι ι x = mfderiv ι x`),
`Dι(T x)` future-timelike for `S̃` on `M` (`timeOrient`), `ι(M) ⊆ M̃` (`maps_M`).

**① The identification — BUILT.** `MSpacetime.mx_frontier_JpastSet`: on any `LocallyOneChart`
spacetime and `A ⊆ M`, `∂J⁻(A) = closure I⁻(A) ∖ I⁻(A)` (`mh_hint`, `mh_hcl`, `mk_isOpen_D`);
`mx_preimage_frontier` / `mx_preimage_closure` (Mathlib's `IsOpenMap.preimage_*`). Headline
`MSpacetime.mx_H_eq_boundary (hL : S.LocallyOneChart) (hLt : St.LocallyOneChart)
(X : ConformalExtension S St) (h𝒥 : 𝒥 ⊆ St.M) (hOD : S.IpastSet (range O) = S.D J)
(hmono : ∀ s t, s < t → S.Chr (O s) (O t)) (hJM : J ⊆ S.M)
(hI : S.IpastSet (range O) = X.ι ⁻¹' St.IpastSet 𝒥) :
S.H (range O) = frontier (X.ι ⁻¹' St.JpastSet 𝒥) ∧ S.H J = frontier (X.ι ⁻¹' St.JpastSet 𝒥)`.
*As stated in advance, only `ι` and `isOpenEmbedding` are used*; the conformal, time-orientation,
`C¹` and `ι(M) ⊆ M̃` fields belong to the definition but not to the proof. No hypothesis beyond the
registration (`hOD` and `hJM` serve only the `S.H J` form; `hmono` gives `range O ⊆ M`).

**② The witness — BUILT.** On `Pt` (`S = St = minkN`), `mx_ι = ψ ∘ mx_fA ∘ φ`,
`mx_fA (U, V) = (U, arctan V)`, through the `nullH` chart `φ`:
* `mx_ι_isOpenEmbedding` (`arctan = val ∘ tanOrderIso.symm`), `mx_ι_contMDiff` (Mathlib's
  `contMDiffOn_extChartAt(_symm)` on the global chart, `contMDiff_iff_contDiff`) — the registered
  expected stop was not hit;
* `mx_dι_eq`: `Dφ ∘ Dι = diag(1, 1/(1+V²)) ∘ Dφ` (`mfderiv_comp`), so with `g = −dU dV`,
  `Ω = (1+V²)^{−1/2}`, `Ω² = 1/(1+V²)` (as registered);
* `mx_witnessExt : ConformalExtension minkN minkN` — every field proved;
* `𝒥⁺ = mx_scri = ψ '' {(U, π/2) : U < 0}`; `mx_scri_subset_frontier : 𝒥⁺ ⊆ ∂ι(Pt)`;
  `mx_mem_mink_D_JA`: `Ĩ⁻(𝒥⁺) = ψ '' {U < 0, V < π/2}` (`chr_lt`, `tstep_of_lt`; the registered
  second-likeliest stop was not hit: no curve need stay in `ι(Pt)`, since `Ĩ⁻` is computed in `Ñ`);
  `mx_preimage_Ipast_scri : ι⁻¹ Ĩ⁻(𝒥⁺) = {U < 0} = D`.
* `NModel.mx_witness_boundary`: all of the above, `hI`, and by `mx_H_eq_boundary`,
  `∂J⁻(𝒥⁺) = 𝓗⁺ = {U = 0}`, non-empty.

**③ The headline whole — BUILT.** `MSpacetime.mx_prop_causal_alignment [T2Space N]` with the
hypotheses of ① plus `hHM : ∂J⁻(𝒥⁺) ⊆ S.M`, `hΘ : S.IsCauchyTemporalOn (S.D J) Θ`,
`hadapt : ∀ τ, Θ (O τ) = τ + c`, concluding, with `𝓗⁺ := frontier (X.ι ⁻¹' St.JpastSet 𝒥)`:
`S.H J = 𝓗⁺`, `SublevelProper`, `KLi/KLs (slice) = 𝓗⁺`, `KLi/KLs (cone O) = 𝓗⁺`, and for every
`q ∈ 𝓗⁺` and every frame `(ℓ, n)`, filter `L ≤ 𝓝 q`, under `mc_tangency_at_N`'s hypotheses,
`(dΘ(n))⁻¹ • dΘ^{e_q} → −g_q(ℓ₀, ·)`. `NModel.mx_witness_headline`: on `Pt` with `Θ₀ ∘ φ`, every
hypothesis discharged and every clause read off, the tangency hypotheses discharged at `p₀ ∈ 𝓗⁺`
with `(ℓN, nN)` along `𝓝[D] p₀`.

*Non-vacuity:* every new theorem's hypotheses are discharged on `Pt`. *Limit:* `Ñ = N = Pt` as
types, and `Pt` still has one global chart.

`#print axioms` at the end: every line reads `[propext, Classical.choice, Quot.sound]`.

# Campaign 88's header, kept

## Probe `r7657+71` (campaign 88): the cone-convergence and tangency clauses of
`prop:causal-alignment` on a multi-chart manifold `N`, witnessed on the two-chart `Pt`

Registration: `computations/formalisation/r7657_71_campaign88/PREDICTION.md`. Nothing imports this
file, and it imports no other probe. It starts as a copy of campaign 87's
`probes/ManifoldHeadline.lean` (namespace renamed `ShadowProbe.ManifoldConesProbe`, all `mh_`/`mk_`/
`me_`/`ch_`/`hl_` names kept); everything new has the prefix `mc_`.

## Copied in for campaign 88

* Campaign 80's `TangencyCondition.lean`, sections ① frame-free and normed, inside namespace `TCF`
  (names `tc_…` kept): `NullFrame`, `FutCausal`, `projW`, `tc_futCausal_iff`, `tc_pos`,
  `tc_W_bound`, `tc_pointwise`, `bil`, `FrameHyp`, `tc_opNorm_bound`, `tc_ratio_of_bounded`,
  `tc_tendsto`, `tc_tendsto_limit`, `tc_sequence`.
* Campaign 72's `hc_preconnected_inter_frontier` (as `mc_preconnected_inter_frontier`, now in any
  topological space) and the shape of `hc_lower_limit` / `hc_upper_limit` / `hc_kuratowski`.
* Campaign 79's frame `ℓ = ∂_V`, `n = 2∂_U` (`Model.ellV`, `Model.nvec`), the sequence `sm`, `xm`
  with `log_sm`, `cos_log_sm`, `deriv_Ffail_sm`, `xm_mem`, and the computations behind `st_aligned`
  (`dΘ₀(ℓ)/dΘ₀(n) = −U/2`) and `st_tangency_fails` (`dΘ = dU + dV` at `x_m`); campaign 80's
  `tc_frameHyp2` at `F = 1` (`Model.mc_frameHyp_gM`).

## NEW (campaign 88)

**① Cone convergence on `N` — BUILT.** `MSpacetime.cone S O τ = ∂_N J⁻(O τ)`.
`mc_lower_limit` (a connected open neighbourhood of `p ∈ 𝓗⁺` — `N` is locally connected by
`ChartedSpace.locallyConnectedSpace` — meets `D` by `mh_hcl`, hence `I⁻(O τ)` for large `τ`, and
`p ∉ int J⁻(O τ)` because `J⁻(O τ) ⊆ J⁻(J)`; so it meets `∂J⁻(O τ)`), `mc_upper_limit` (limit point
in `closure J⁻(J)`, not in `D` since `I⁻(O σ)` is open (`mk_isOpen_Ipast`) and lies in
`int J⁻(O τ)` for `τ ≥ σ`, then `mh_hint`), and the headline
`MSpacetime.mc_cone_kuratowski_N (hL : S.LocallyOneChart) (hOD : S.IpastSet (range O) = S.D J)
(hmono : ∀ s t, s < t → S.Chr (O s) (O t)) (hJM : J ⊆ S.M) :
KLi (S.cone O) = S.H J ∧ KLs (S.cone O) = S.H J`.
Fewer hypotheses than registered: neither `T2Space N` nor `𝓗⁺ ⊆ M` is used, and push-up is not
needed for `p ∉ int J⁻(O τ)` (transitivity suffices, as in campaign 72).

**② Tangency on `N` — BUILT (in chart-component form, with the transformation law).**
Mathlib reads `dΘ_x = mfderiv Θ x` (`dcov`), `g_x` and frames `ℓ_x, n_x` in the preferred chart at
`x`. For a chart `e = extChartAt p` and `x ∈ src e`: `A_x = D e_x` (`dchartL`),
`B_x = D(e⁻¹)_{e x}` (`dchartInvL`, `= tangentCoordChange p x x`, `mc_B_eq`), covector
`covCh Θ p x = dΘ_x ∘ B_x`, metric `gCh p x = hRep g p (e x)`.
* `mc_frameHyp_pullback`, `MSpacetime.mc_frameHyp_toChart` / `mc_frameHyp_ofChart`: the frame
  hypotheses are chart-free; `mc_covCh_A`: so is the rate `dΘ_x(ℓ_x)/dΘ_x(n_x)`.
* `MSpacetime.mc_tangency_N` (any chart, any filter): intrinsic frame hypotheses eventually,
  `‖g^e‖`, `‖g^e‖‖n^e‖`, `‖ℓ^e‖` bounded, rate `→ 0` ⟹
  `dΘ^e_x/dΘ_x(n_x) + g^e_x(ℓ^e_x, ·) → 0` (campaign 80's `tc_tendsto` on the `e`-components).
* `MSpacetime.mc_tangency_limit_N`: `L ≤ 𝓝 q`, `hRep g p` continuous at `e q`, `‖n^e‖` bounded,
  `ℓ^e_x → ℓ₀` ⟹ `dΘ^e_x/dΘ_x(n_x) → −g^e_{e q}(ℓ₀, ·)`.
* `MSpacetime.mc_tangency_at_N` (the registered statement): with `LocallyOneChart` and the chart at
  the horizon point `q` itself, the continuity is supplied and the limit is `−g_q(ℓ₀, ·)`.
* `mc_chart_change` (registered chart-independence): if the components in `e'` converge to `λ'`,
  those in `e` converge to `λ' ∘ tangentCoordChange p p' q` (`mc_covCh_change`, Mathlib's
  `continuousOn_tangentCoordChange`).
*The registered expected stop was not hit in this form.* What is **not** built: a statement in the
cotangent bundle as a space (convergence of `(x, dΘ_x/dΘ_x(n_x))` in `TotalSpace` of `T*N`);
here convergence is stated, as is standard, by components in a chart together with the
transformation law between charts. In a chart other than the one at `q`, continuity of `hRep g p` at
`e q` is a hypothesis (it is not derived from `LocallyOneChart`).

**③ The witness on `Pt` — BUILT.** Through the global chart `φ = extChartAt p₀` (`nullH`), with the
intrinsic frame `ℓN x = B_x ∂_V`, `nN x = B_x (2∂_U)`; `mc_covCh_comp_chart` (chain rule in a chart:
`d(f ∘ φ)` read in `φ` is `fderiv f`).
* `NModel.mc_witness_frameHyp`: the intrinsic frame hypotheses at every point of `D` for every good
  profile.
* `NModel.mc_witness_tangency_holds` (`Θ₀ ∘ φ`, every `q ∈ 𝓗⁺`): Cauchy temporal on `D`,
  `𝓝[D] q ≠ ⊥`, frame hypotheses, rate `−U/2 → 0`, the conclusion of `mc_tangency_N`, and by
  `mc_tangency_limit_N` the limit `½ dU = −g(ℓ, ·)`.
* `NModel.mc_witness_tangency_at` (`q = p₀`): `mc_tangency_at_N` with `LocallyOneChart`, and
  `mc_chart_change` to the other chart `idH`, with the coordinate change computed
  (`tCC_neg_p₀ = nullL`) and the limit `½ (dt − dx)`.
* `NModel.mc_witness_tangency_fails` (`Θf ∘ φ`, at `p₀`): Cauchy temporal on `D`, frame hypotheses
  at every point of `D`, but along `ψ(x_m) → p₀` the rate is `1/2`, so neither the rate condition
  nor the conclusion holds.
* `NModel.mc_witness_cones`: `KLi = KLs = 𝓗⁺ = {U = 0}` (non-empty) for the past cones on `Pt`, via
  `mc_cone_kuratowski_N`.
Every new theorem's hypotheses are discharged on `Pt` by these.
*Limit, as registered:* one chart of `Pt`'s atlas covers `Pt`; the flat cylinder still waits.

**④ `𝓗⁺ = ∂J⁻(𝒥⁺)` — registered and priced, not built (not attempted here).**

`#print axioms` at the end: every line reads `[propext, Classical.choice, Quot.sound]`.

# Campaign 87's header, kept

### Copied

* Campaign 84's `probes/ChartHeadline.lean`, nearly all of it (its module docstring dropped): the
  `V`-side chain of campaigns 60–81 with campaign 81's two-sided Rindler `Model` (`hl_cauchy`,
  `hl_adapted`, `GoodG`, `Θ₀`, `Θf`), campaign 68's `chartRep`/`hRep`, the intrinsic `MSpacetime`
  (`TStep`, `Chr`, `Cau`, `D`, `H`, `slice`, `SublevelProper`, `KLi`/`KLs`, `IsTemporalOn`,
  `IsCauchyTemporalOn`), `OneChart`, the chart transfer, `ch_isCauchy_VN`,
  `ch_causal_alignment_gh_N`, and `NModel` (`Pt`, two-chart atlas, `minkN`, `ch_oneChart`,
  `ch_chartSp_eq`, `JN`, `mem_D_N`, `mem_H_N`, `ch_witness_hypotheses`).
* Campaign 85's `probes/ManifoldExtension.lean`: `restrictM`, `LocallyOneChart`(`.restrict`),
  `me_local_step`, `me_temporal_*`, the drop/vertices/gluing, `me_past_extension`,
  `FutInextCurveIn`, `FutCauchyTemporalOn`, `me_futCauchy_of_cauchy_N`; and in `NModel`
  `nullInvL`, `chartAt_neg`/`_nonneg`, `me_dchart_neg`, `hRep_neg`, `chartRep_neg`,
  `me_charts_differ`, `me_locallyOneChart`.
* Campaign 86's `probes/ManifoldLocalKit.lean`, pieces 1–5 (`mk_*`): restriction, openness of
  `I^±` and `D J` on `N`, `mk_local_step_fut` (`Safe2`), `mk_curve_into`, `mk_curve_inext_D`,
  push-up `mk_pushup`/`mk_pushup'`.

### NEW (`hL : S.LocallyOneChart`; `[T2Space N]` where the curve into a point is used)

1. **Temporal increase along `≪` into `D` — BUILT.** `DspN hL J := S.restrictM (D J)`;
   `mh_tstep_DspN` (a `TStep_N` ending in `D` runs inside `D`, via `mk_tstep_sub`);
   `mh_temporalD_chr` (`IsTemporalOn (D J) Θ`, `x ≪ y ∈ D ⟹ Θ x < Θ y`: `me_temporal_tstep` in
   `DspN` plus induction — campaign 75/78's `cr_temporalD_chr` reproduced on `N`).
2. **`hint` and `hcl` on `N` — BUILT.** `mh_future_step` (`mk_local_step_fut` at `x`, cut short by
   `mk_tstep_restrict`), `mh_past_step` (tail of `mk_curve_into`), `mh_hint`
   (`int J⁻(J) ⊆ D`, by `mk_pushup'`), `mh_hcl` (`closure J⁻(J) ⊆ closure D`, by `mk_pushup'`).
3. **Properness on `N` — BUILT** (the registered second-likeliest stop, not hit).
   `mh_blowup` (`mk_curve_inext_D` + the future Cauchy property + `I⁺(r)` open,
   `mk_isOpen_Ifut`), `mh_sublevelProper`. The future Cauchy property comes from
   `me_futCauchy_of_cauchy_N` at `U = D J`, open by `mk_isOpen_D`.
4. **Slice lower limit — BUILT.** `mh_mem_KLi_slice`, `mh_slice_lower_limit` (the curve's tail).
5. **Slice upper limit and Kuratowski — BUILT** (the registered expected stop, not hit).
   Campaign 81's argument turned out to use no vector-space structure: only that `I⁻(O σ)` is open
   (now `mk_isOpen_Ipast`), `D ⊆ J⁻(J)` and `Θ` increasing along `≪` into `D` (piece 1).
   `mh_slice_upper_limit`, `mh_slice_kuratowski`.
6. **The headline — BUILT.** `MSpacetime.mh_causal_alignment_gh_N (hL : S.LocallyOneChart)
   [T2Space N] (hOD : S.IpastSet (range O) = S.D J) (hmono : ∀ s t, s < t → S.Chr (O s) (O t))
   (hJM : J ⊆ S.M) (hHM : S.H J ⊆ S.M) (hΘ : S.IsCauchyTemporalOn (S.D J) Θ)
   (hadapt : ∀ τ, Θ (O τ) = τ + c) :
   S.SublevelProper J Θ ∧ KLi (S.slice J Θ) = S.H J ∧ KLs (S.slice J Θ) = S.H J`.

### Witness — BUILT

`NModel.mh_witness_hypotheses`: on the two-chart `Pt` (preferred chart `idH` on `{t < 0}`,
`nullH` on `{t ≥ 0}`, `me_charts_differ`), `LocallyOneChart`, `T2Space Pt`, and every other
hypothesis, **including `IsCauchyTemporalOn (D JN) (Θ_G ∘ φ)`** (left open by campaign 85), by
campaign 84's transport `ch_isCauchy_VN` through the global chart `nullH` from campaign 81's
two-sided model `Model.hl_cauchy`. `NModel.mh_witness_headline`: for `Θ₀ ∘ φ` and `Θf ∘ φ`,
properness and `KLi = KLs = 𝓗⁺ = {U = 0}` (non-empty), via `mh_causal_alignment_gh_N`.
*Limit, as registered:* one chart of `Pt`'s atlas covers `Pt`, so the witness does not need two
charts; it exercises the multi-chart theorem with differing preferred charts.

### Stretch — REPORTED

A witness no single chart covers (flat cylinder `ℝ × S¹`) is not attempted: it needs a new
charted space, `LocallyOneChart` on it, and a Cauchy proof on `N` with no global chart to transport
through.

`#print axioms` at the end. `set_option synthInstance.maxHeartbeats 400000` inside `Model` (copied).
-/

open Set Filter Topology Metric

namespace ShadowProbe.CircleExteriorProbe

variable {V : Type*} [NormedAddCommGroup V] [NormedSpace ℝ V]

/-- A time-oriented Lorentzian chart (campaign 60). -/
structure Spacetime (V : Type*) [NormedAddCommGroup V] [NormedSpace ℝ V] where
  M : Set V
  isOpen_M : IsOpen M
  g : V → V →L[ℝ] V →L[ℝ] ℝ
  cont_g : ContinuousOn g M
  symm : ∀ x v w, g x v w = g x w v
  T : V → V
  cont_T : ContinuousOn T M
  T_timelike : ∀ x ∈ M, g x (T x) (T x) < 0
  pos_on_perp : ∀ x ∈ M, ∀ v, g x v (T x) = 0 → v ≠ 0 → 0 < g x v v

namespace Spacetime
variable (S : Spacetime V)

/-- Future-directed timelike vector at `x`. -/
def FutTimelike (x v : V) : Prop := S.g x v v < 0 ∧ S.g x v (S.T x) < 0
/-- Future-directed causal vector at `x`. -/
def FutCausal (x v : V) : Prop := S.g x v v ≤ 0 ∧ S.g x v (S.T x) < 0

/-- One `C¹` future-timelike piece from `x` to `y`. -/
def TStep (x y : V) : Prop :=
  ∃ γ : ℝ → V, ContDiff ℝ 1 γ ∧ γ 0 = x ∧ γ 1 = y ∧
    ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ S.M ∧ S.FutTimelike (γ t) (deriv γ t)

/-- One `C¹` future-causal piece from `x` to `y`. -/
def CStep (x y : V) : Prop :=
  ∃ γ : ℝ → V, ContDiff ℝ 1 γ ∧ γ 0 = x ∧ γ 1 = y ∧
    ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ S.M ∧ S.FutCausal (γ t) (deriv γ t)

/-- `x ≪ y`. -/
def Chr (x y : V) : Prop := Relation.TransGen S.TStep x y
/-- `x ≤ y`. -/
def Cau (x y : V) : Prop := Relation.ReflTransGen S.CStep x y

/-- `I⁻(p)`. -/
def Ipast (p : V) : Set V := {q | S.Chr q p}
/-- `J⁻(p)`. -/
def Jpast (p : V) : Set V := {q | S.Cau q p}
/-- `I⁻(A)`. -/
def IpastSet (A : Set V) : Set V := ⋃ p ∈ A, S.Ipast p
/-- `J⁻(A)`. -/
def JpastSet (A : Set V) : Set V := ⋃ p ∈ A, S.Jpast p

/-- c1: `T` is continuous at points of `M` (`cont_T` is now only `ContinuousOn T M`, `M` open). -/
lemma contAt_T {x : V} (hx : x ∈ S.M) : ContinuousAt S.T x :=
  S.cont_T.continuousAt (S.isOpen_M.mem_nhds hx)

/-- c1: the pointwise form of campaign 60's `cont_gvw`, at a parameter whose base point lies in `M`. -/
lemma cont_gvw_at {X : Type*} [TopologicalSpace X] {x v w : X → V} {a : X} (hx : ContinuousAt x a)
    (hxM : x a ∈ S.M) (hv : ContinuousAt v a) (hw : ContinuousAt w a) :
    ContinuousAt (fun a => S.g (x a) (v a) (w a)) a :=
  (((S.cont_g.continuousAt (S.isOpen_M.mem_nhds hxM)).comp hx).clm_apply hv).clm_apply hw

lemma isOpen_timelikePairs :
    IsOpen {pv : V × V | pv.1 ∈ S.M ∧ S.FutTimelike pv.1 pv.2} := by
  refine isOpen_iff_mem_nhds.2 fun pv ⟨hM, h1, h2⟩ => ?_
  have e1 : ∀ᶠ q : V × V in 𝓝 pv, q.1 ∈ S.M :=
    continuousAt_fst.eventually_mem (S.isOpen_M.mem_nhds hM)
  have e2 : ∀ᶠ q : V × V in 𝓝 pv, S.g q.1 q.2 q.2 < 0 :=
    (S.cont_gvw_at continuousAt_fst hM continuousAt_snd continuousAt_snd).eventually_lt
      continuousAt_const h1
  have e3 : ∀ᶠ q : V × V in 𝓝 pv, S.g q.1 q.2 (S.T q.1) < 0 :=
    (S.cont_gvw_at continuousAt_fst hM continuousAt_snd
      ((S.contAt_T hM).comp continuousAt_fst)).eventually_lt continuousAt_const h2
  filter_upwards [e1, e2, e3] with q a b c using ⟨a, b, c⟩

lemma tube {P Q : V → ℝ → V} (hP : Continuous fun z : V × ℝ => P z.1 z.2)
    (hQ : Continuous fun z : V × ℝ => Q z.1 z.2)
    (h0 : ∀ t ∈ Icc (0:ℝ) 1, P 0 t ∈ S.M ∧ S.FutTimelike (P 0 t) (Q 0 t)) :
    ∀ᶠ w in 𝓝 (0:V), ∀ t ∈ Icc (0:ℝ) 1, P w t ∈ S.M ∧ S.FutTimelike (P w t) (Q w t) := by
  refine isCompact_Icc.eventually_forall_of_forall_eventually fun t ht => ?_
  have hO := S.isOpen_timelikePairs.preimage (hP.prodMk hQ)
  exact hO.mem_nhds (h0 t ht)

lemma hasDerivAt_of_contDiff {γ : ℝ → V} (hγ : ContDiff ℝ 1 γ) (t : ℝ) :
    HasDerivAt γ (deriv γ t) t :=
  ((hγ.differentiable one_ne_zero) t).hasDerivAt

/-- The start of a timelike step can be moved in an open set. -/
lemma tstep_start_eventually {p y : V} (h : S.TStep p y) : ∀ᶠ p' in 𝓝 p, S.TStep p' y := by
  obtain ⟨γ, hγ, h0, h1, hγt⟩ := h
  have hdc : Continuous (deriv γ) := hγ.continuous_deriv le_rfl
  have hT := S.tube (P := fun w t => γ t + (1 - t) • w) (Q := fun w t => deriv γ t - w)
    ((hγ.continuous.comp continuous_snd).add
      ((continuous_const.sub continuous_snd).smul continuous_fst))
    ((hdc.comp continuous_snd).sub continuous_fst) (by simpa using hγt)
  have hlim : Tendsto (fun p' => p' - p) (𝓝 p) (𝓝 0) := tendsto_sub_nhds_zero_iff.2 tendsto_id
  filter_upwards [hlim.eventually hT] with p' hp'
  refine ⟨fun t => γ t + (1 - t) • (p' - p),
    hγ.add ((contDiff_const.sub contDiff_id).smul contDiff_const), by simp [h0],
    by simp [h1], fun t ht => ?_⟩
  have hd : deriv (fun t => γ t + (1 - t) • (p' - p)) t = deriv γ t - (p' - p) := by
    have h : HasDerivAt (fun t => γ t + (1 - t) • (p' - p))
        (deriv γ t + ((0:ℝ) - 1) • (p' - p)) t :=
      (hasDerivAt_of_contDiff hγ t).add
        (((hasDerivAt_const t (1:ℝ)).sub (hasDerivAt_id' t)).smul_const (p' - p))
    rw [h.deriv, zero_sub, neg_one_smul, ← sub_eq_add_neg]
  rw [hd]; exact hp' t ht

/-- `I⁻(p)` is open (campaign 60's `hl_isOpen_Ipast`). -/
theorem hl_isOpen_Ipast (p : V) : IsOpen (S.Ipast p) := by
  refine isOpen_iff_mem_nhds.2 fun q hq => ?_
  obtain ⟨y, hqy, hyp⟩ := Relation.TransGen.head'_iff.1 hq
  filter_upwards [S.tstep_start_eventually hqy] with q' hq'
  exact Relation.TransGen.head' hq' hyp

lemma tstep_to_cstep {x y : V} (h : S.TStep x y) : S.CStep x y := by
  obtain ⟨γ, hγ, h0, h1, hγt⟩ := h
  exact ⟨γ, hγ, h0, h1, fun t ht => ⟨(hγt t ht).1, (hγt t ht).2.1.le, (hγt t ht).2.2⟩⟩

/-- `≪ ⊆ ≤`. -/
theorem hl_chr_cau {x y : V} (h : S.Chr x y) : S.Cau x y := by
  induction h with
  | single h => exact Relation.ReflTransGen.single (S.tstep_to_cstep h)
  | tail _ h ih => exact ih.tail (S.tstep_to_cstep h)

theorem hl_chr_trans {x y z : V} (h1 : S.Chr x y) (h2 : S.Chr y z) : S.Chr x z :=
  Relation.TransGen.trans h1 h2

theorem hl_cau_trans {x y z : V} (h1 : S.Cau x y) (h2 : S.Cau y z) : S.Cau x z :=
  Relation.ReflTransGen.trans h1 h2

theorem hl_Ipast_subset_Jpast (p : V) : S.Ipast p ⊆ S.Jpast p := fun _ h => S.hl_chr_cau h

/-! ## Copied from campaign 60 (`probes/CausalStructure.lean`): push-up and time reversal -/

/-- Positive rescaling preserves future-timelikeness. -/
lemma futTimelike_smul {x u : V} {c : ℝ} (hc : 0 < c) (h : S.FutTimelike x u) :
    S.FutTimelike x (c • u) := by
  obtain ⟨h1, h2⟩ := h
  refine ⟨?_, ?_⟩
  · simp only [map_smul, FunLike.coe_smul, Pi.smul_apply, smul_eq_mul]
    nlinarith [mul_pos hc hc]
  · simp only [map_smul, FunLike.coe_smul, Pi.smul_apply, smul_eq_mul]
    nlinarith

/-- Lipschitz control of the quadratic form. -/
lemma quad_le {K : NNReal} {N : Set V} (hK : LipschitzOnWith K S.g N) {p q : V} (hp : p ∈ N)
    (hq : q ∈ N) (a : V) : S.g p a a ≤ S.g q a a + K * dist p q * (‖a‖ * ‖a‖) := by
  have h1 : |S.g p a a - S.g q a a| ≤ ‖S.g p - S.g q‖ * ‖a‖ * ‖a‖ := by
    have := (S.g p - S.g q).le_opNorm₂ a a
    simpa [Real.norm_eq_abs] using this
  have h2 : ‖S.g p - S.g q‖ ≤ K * dist p q := by
    have := hK.dist_le_mul p hp q hq
    rwa [dist_eq_norm] at this
  have h3 := (abs_le.1 h1).2
  have h4 : ‖S.g p - S.g q‖ * ‖a‖ * ‖a‖ ≤ K * dist p q * (‖a‖ * ‖a‖) := by
    rw [mul_assoc]; exact mul_le_mul_of_nonneg_right h2 (by positivity)
  linarith

/-- Local push-up. -/
lemma local_pushup (hL : LocallyLipschitzOn S.M S.g) {α : ℝ → V} (hα : ContDiff ℝ 1 α)
    (hc : ∀ t ∈ Icc (0:ℝ) 1, α t ∈ S.M ∧ S.FutCausal (α t) (deriv α t))
    {s : ℝ} (hs : s ∈ Icc (0:ℝ) 1) :
    ∃ ε > 0, ∀ t ∈ Icc (0:ℝ) 1, s < t → t < s + ε → ∀ l : ℝ, 0 < l → l < ε →
      S.TStep (α s) (α t + (l * (t - s)) • S.T (α s)) := by
  obtain ⟨hx₀M, -, hb⟩ := hc s hs
  obtain ⟨K, N, hN, hK⟩ := hL hx₀M
  rw [S.isOpen_M.nhdsWithin_eq hx₀M] at hN
  have hvv : S.g (α s) (S.T (α s)) (S.T (α s)) < 0 := S.T_timelike _ hx₀M
  -- abbreviations
  have hdc : Continuous (deriv α) := hα.continuous_deriv le_rfl
  let v := S.T (α s)
  let u₀ := deriv α s
  let b := -(S.g (α s) u₀ v)
  have hbpos : 0 < b := by simp only [b]; linarith
  let P : V × V → Prop := fun pu => pu.1 ∈ S.M ∧ S.g pu.1 pu.2 v < -(b/2) ∧
    S.g pu.1 v v < 0 ∧ S.g pu.1 pu.2 (S.T pu.1) < 0 ∧ S.g pu.1 v (S.T pu.1) < 0 ∧
    pu.1 ∈ N ∧ ‖pu.2‖ < ‖u₀‖ + 1
  have hW : ∀ᶠ pu in 𝓝 (α s, u₀), P pu := by
    have e1 : ∀ᶠ pu : V × V in 𝓝 (α s, u₀), pu.1 ∈ S.M :=
      continuousAt_fst.eventually_mem (S.isOpen_M.mem_nhds hx₀M)
    have e2 : ∀ᶠ pu : V × V in 𝓝 (α s, u₀), S.g pu.1 pu.2 v < -(b/2) :=
      (S.cont_gvw_at continuousAt_fst hx₀M continuousAt_snd continuousAt_const).eventually_lt
        continuousAt_const (by simp only [b, u₀]; linarith)
    have e3 : ∀ᶠ pu : V × V in 𝓝 (α s, u₀), S.g pu.1 v v < 0 :=
      (S.cont_gvw_at continuousAt_fst hx₀M continuousAt_const continuousAt_const).eventually_lt
        continuousAt_const hvv
    have e4 : ∀ᶠ pu : V × V in 𝓝 (α s, u₀), S.g pu.1 pu.2 (S.T pu.1) < 0 :=
      (S.cont_gvw_at continuousAt_fst hx₀M continuousAt_snd
        ((S.contAt_T hx₀M).comp (x := (α s, u₀)) continuousAt_fst)).eventually_lt continuousAt_const hb
    have e5 : ∀ᶠ pu : V × V in 𝓝 (α s, u₀), S.g pu.1 v (S.T pu.1) < 0 :=
      (S.cont_gvw_at continuousAt_fst hx₀M continuousAt_const
        ((S.contAt_T hx₀M).comp (x := (α s, u₀)) continuousAt_fst)).eventually_lt continuousAt_const hvv
    have e6 : ∀ᶠ pu : V × V in 𝓝 (α s, u₀), pu.1 ∈ N := continuousAt_fst.eventually_mem hN
    have e7 : ∀ᶠ pu : V × V in 𝓝 (α s, u₀), ‖pu.2‖ < ‖u₀‖ + 1 :=
      (continuous_norm.comp continuous_snd).continuousAt.eventually_lt continuousAt_const
        (by simp)
    filter_upwards [e1, e2, e3, e4, e5, e6, e7] with pu h1 h2 h3 h4 h5 h6 h7
    exact ⟨h1, h2, h3, h4, h5, h6, h7⟩
  let Φ : ℝ × ℝ → V × V := fun z => (α z.1 + (z.2 * (z.1 - s)) • v, deriv α z.1)
  have hΦc : Continuous Φ := by
    refine Continuous.prodMk ?_ (hdc.comp continuous_fst)
    exact (hα.continuous.comp continuous_fst).add
      ((continuous_snd.mul (continuous_fst.sub continuous_const)).smul continuous_const)
  have hΦ : Tendsto Φ (𝓝 (s, 0)) (𝓝 (α s, u₀)) := by
    have := hΦc.tendsto (s, 0)
    simpa [Φ, u₀] using this
  have hαN : ∀ᶠ z : ℝ × ℝ in 𝓝 (s, 0), α z.1 ∈ N :=
    ((hα.continuous.comp continuous_fst).tendsto (s, 0)).eventually_mem (by simpa using hN)
  have hLip : ∀ᶠ z : ℝ × ℝ in 𝓝 (s, 0),
      (K:ℝ) * |z.1 - s| * ‖v‖ * (‖u₀‖ + 1) ^ 2 < b / 2 := by
    refine ContinuousAt.eventually_lt (by fun_prop) continuousAt_const ?_
    simp; linarith
  obtain ⟨ε, hε, hεP⟩ := Metric.eventually_nhds_iff.1 ((hΦ.eventually hW).and (hαN.and hLip))
  refine ⟨ε, hε, fun t ht hst htε l hl hlε => ?_⟩
  refine ⟨fun r => α (s + r * (t - s)) + (l * (r * (t - s))) • v,
    (hα.comp (contDiff_const.add (contDiff_id.mul contDiff_const))).add
      ((contDiff_const.mul (contDiff_id.mul contDiff_const)).smul contDiff_const),
    by simp, by simp [v], fun r hr => ?_⟩
  have hts : 0 < t - s := sub_pos.2 hst
  set s' := s + r * (t - s) with hs'
  have hs's : s' - s = r * (t - s) := by rw [hs']; ring
  have hs'0 : 0 ≤ s' - s := by rw [hs's]; exact mul_nonneg hr.1 hts.le
  have hs'1 : s' - s ≤ t - s := by rw [hs's]; nlinarith [hr.2]
  have hs'I : s' ∈ Icc (0:ℝ) 1 := ⟨by linarith [hs.1], by linarith [ht.2]⟩
  -- the derivative
  have hin : HasDerivAt (fun r => s + r * (t - s)) (t - s) r := by
    simpa using ((hasDerivAt_id r).mul_const (t - s)).const_add s
  have h1 : HasDerivAt (fun r => α (s + r * (t - s))) ((t - s) • deriv α s') r :=
    (hasDerivAt_of_contDiff hα _).scomp r hin
  have h2 : HasDerivAt (fun r => (l * (r * (t - s))) • v) ((l * (t - s)) • v) r := by
    simpa using (((hasDerivAt_id r).mul_const (t - s)).const_mul l).smul_const v
  have hd : deriv (fun r => α (s + r * (t - s)) + (l * (r * (t - s))) • v) r =
      (t - s) • (deriv α s' + l • v) := by
    have h3 : HasDerivAt (fun r => α (s + r * (t - s)) + (l * (r * (t - s))) • v)
        ((t - s) • deriv α s' + (l * (t - s)) • v) r := h1.add h2
    rw [h3.deriv, smul_add, smul_smul, mul_comm l]
  have hpt : α (s + r * (t - s)) + (l * (r * (t - s))) • v = α s' + (l * (s' - s)) • v := by
    rw [hs's]
  rw [hd]
  beta_reduce
  rw [hpt]
  -- the estimates at `(s', l)`
  have hdist : dist (s', l) (s, 0) < ε := by
    rw [Prod.dist_eq, max_lt_iff, Real.dist_eq, Real.dist_eq, sub_zero, abs_of_nonneg hs'0,
      abs_of_pos hl]
    exact ⟨by linarith, hlε⟩
  obtain ⟨⟨hpM, hav, hvv', haT, hvT, hpN, hna⟩, hαN', hLip'⟩ := hεP hdist
  simp only [Φ] at hpM hav hvv' haT hvT hpN hna hαN' hLip'
  set p := α s' + (l * (s' - s)) • v with hp
  set a := deriv α s' with ha
  have hcaus := (hc s' hs'I).2.1
  have hq := S.quad_le hK hpN hαN' a
  have hdp : dist p (α s') = l * (s' - s) * ‖v‖ := by
    rw [hp, dist_eq_norm, add_sub_cancel_left, norm_smul, Real.norm_eq_abs,
      abs_of_nonneg (mul_nonneg hl.le hs'0)]
  rw [hdp] at hq
  have hna0 : 0 ≤ ‖a‖ := norm_nonneg a
  have hasq : ‖a‖ * ‖a‖ ≤ (‖u₀‖ + 1) ^ 2 := by nlinarith
  have hQ0 : 0 ≤ (K:ℝ) * (s' - s) * ‖v‖ := by positivity
  have hLip'' : (K:ℝ) * (s' - s) * ‖v‖ * (‖u₀‖ + 1) ^ 2 < b / 2 := by
    rwa [abs_of_nonneg hs'0] at hLip'
  have hKa : (K:ℝ) * (l * (s' - s) * ‖v‖) * (‖a‖ * ‖a‖) ≤ l * (b / 2) := by
    have : (K:ℝ) * (s' - s) * ‖v‖ * (‖a‖ * ‖a‖) ≤ (K:ℝ) * (s' - s) * ‖v‖ * (‖u₀‖ + 1) ^ 2 :=
      mul_le_mul_of_nonneg_left hasq hQ0
    nlinarith
  have hgaa : S.g p a a ≤ l * (b / 2) := by linarith
  refine ⟨hpM, S.futTimelike_smul hts ⟨?_, ?_⟩⟩
  · simp only [map_add, map_smul, FunLike.coe_add, Pi.add_apply, FunLike.coe_smul, Pi.smul_apply,
      smul_eq_mul]
    rw [S.symm p v a]
    nlinarith [mul_pos hl hl]
  · simp only [map_add, map_smul, FunLike.coe_add, Pi.add_apply, FunLike.coe_smul, Pi.smul_apply,
      smul_eq_mul]
    nlinarith

/-- Push-up along one causal step: a causal step followed by a timelike chain is a timelike
chain. Needs `g` locally Lipschitz. -/
lemma pushup_cstep (hL : LocallyLipschitzOn S.M S.g) {x y z : V} (hxy : S.CStep x y)
    (hyz : S.Chr y z) : S.Chr x z := by
  obtain ⟨α, hα, h0, h1, hc⟩ := hxy
  let A : Set ℝ := {t | t ∈ Icc (0:ℝ) 1 ∧ S.Chr (α t) z}
  have h1A : (1:ℝ) ∈ A := ⟨⟨zero_le_one, le_rfl⟩, by simp only [h1]; exact hyz⟩
  have hne : A.Nonempty := ⟨1, h1A⟩
  have hbdd : BddBelow A := ⟨0, fun t ht => ht.1.1⟩
  have hs0 : 0 ≤ sInf A := le_csInf hne fun t ht => ht.1.1
  have hs1 : sInf A ≤ 1 := csInf_le hbdd h1A
  have hαc := hα.continuous
  have hsA : S.Chr (α (sInf A)) z := by
    obtain ⟨ε, hε, hloc⟩ := S.local_pushup hL hα hc ⟨hs0, hs1⟩
    obtain ⟨t, htA, hts⟩ := exists_lt_of_csInf_lt hne (show sInf A < sInf A + ε by linarith)
    have hst : sInf A ≤ t := csInf_le hbdd htA
    rcases hst.lt_or_eq with hst | hst
    · have hcl : Continuous fun l : ℝ => α t + (l * (t - sInf A)) • S.T (α (sInf A)) := by
        fun_prop
      have hev : ∀ᶠ l in 𝓝 (0:ℝ), S.Chr (α t + (l * (t - sInf A)) • S.T (α (sInf A))) z := by
        have := hcl.tendsto 0
        simp only [zero_mul, zero_smul, add_zero] at this
        exact this.eventually ((S.hl_isOpen_Ipast z).mem_nhds htA.2)
      obtain ⟨l, hl, hlpos, hlε⟩ :=
        ((hev.filter_mono nhdsWithin_le_nhds).and (Ioo_mem_nhdsGT hε)).exists
      exact Relation.TransGen.head (hloc t htA.1 hst hts l hlpos hlε) hl
    · rw [hst]; exact htA.2
  have hs : sInf A = 0 := by
    by_contra hne0
    have hspos : 0 < sInf A := lt_of_le_of_ne hs0 (Ne.symm hne0)
    have hev : ∀ᶠ t in 𝓝 (sInf A), S.Chr (α t) z :=
      (hαc.tendsto _).eventually ((S.hl_isOpen_Ipast z).mem_nhds hsA)
    obtain ⟨δ, hδ, hδP⟩ := Metric.eventually_nhds_iff.1 hev
    have hm1 := min_le_left δ (sInf A)
    have hm2 := min_le_right δ (sInf A)
    have hm3 := lt_min hδ hspos
    have ht : sInf A - min δ (sInf A) / 2 ∈ A := by
      refine ⟨⟨by linarith, by linarith⟩, hδP ?_⟩
      rw [Real.dist_eq, abs_lt]; constructor <;> linarith
    have := csInf_le hbdd ht
    linarith
  rw [← h0, ← hs]; exact hsA

/-- **Push-up** `J⁻(I⁻(z)) ⊆ I⁻(z)`: `q ≤ p ≪ z ⟹ q ≪ z`, for locally Lipschitz `g`. -/
theorem hl_pushup (hL : LocallyLipschitzOn S.M S.g) {q p z : V} (hqp : S.Cau q p) (hpz : S.Chr p z) :
    S.Chr q z := by
  induction hqp using Relation.ReflTransGen.head_induction_on with
  | refl => exact hpz
  | head h _ ih => exact S.pushup_cstep hL h ih

/-! ### Time reversal, and the dual push-up `I⁻ ∘ J⁻ ⊆ I⁻` -/

/-- The time-reversed chart: same `g`, orientation `-T`. -/
def rev : Spacetime V where
  M := S.M
  isOpen_M := S.isOpen_M
  g := S.g
  cont_g := S.cont_g
  symm := S.symm
  T x := -S.T x
  cont_T := S.cont_T.neg
  T_timelike x hx := by simpa using S.T_timelike x hx
  pos_on_perp x hx v hv := S.pos_on_perp x hx v (by simpa using hv)

lemma rev_futTimelike (x v : V) : S.rev.FutTimelike x v ↔ S.FutTimelike x (-v) := by
  simp [FutTimelike, rev]

lemma rev_futCausal (x v : V) : S.rev.FutCausal x v ↔ S.FutCausal x (-v) := by
  simp [FutCausal, rev]

lemma reverse_curve {γ : ℝ → V} (hγ : ContDiff ℝ 1 γ) :
    ContDiff ℝ 1 (fun t => γ (1 - t)) ∧ ∀ t, deriv (fun t => γ (1 - t)) t = -deriv γ (1 - t) := by
  refine ⟨hγ.comp (contDiff_const.sub contDiff_id), fun t => ?_⟩
  have hin : HasDerivAt (fun t : ℝ => 1 - t) (0 - 1) t :=
    (hasDerivAt_const t (1:ℝ)).sub (hasDerivAt_id' t)
  have h : HasDerivAt (fun t => γ (1 - t)) (((0:ℝ) - 1) • deriv γ (1 - t)) t :=
    (hasDerivAt_of_contDiff hγ (1 - t)).scomp t hin
  rw [h.deriv, zero_sub, neg_one_smul]

lemma rev_tstep_iff (x y : V) : S.rev.TStep x y ↔ S.TStep y x := by
  constructor
  · rintro ⟨γ, hγ, h0, h1, ht⟩
    obtain ⟨hc, hd⟩ := reverse_curve hγ
    refine ⟨fun t => γ (1 - t), hc, by simp [h1], by simp [h0], fun t htI => ?_⟩
    have hI : 1 - t ∈ Icc (0:ℝ) 1 := ⟨by linarith [htI.2], by linarith [htI.1]⟩
    obtain ⟨hm, hf⟩ := ht _ hI
    exact ⟨hm, by rw [hd]; exact (S.rev_futTimelike _ _).1 hf⟩
  · rintro ⟨γ, hγ, h0, h1, ht⟩
    obtain ⟨hc, hd⟩ := reverse_curve hγ
    refine ⟨fun t => γ (1 - t), hc, by simp [h1], by simp [h0], fun t htI => ?_⟩
    have hI : 1 - t ∈ Icc (0:ℝ) 1 := ⟨by linarith [htI.2], by linarith [htI.1]⟩
    obtain ⟨hm, hf⟩ := ht _ hI
    exact ⟨hm, by rw [hd, S.rev_futTimelike, neg_neg]; exact hf⟩

lemma rev_cstep_iff (x y : V) : S.rev.CStep x y ↔ S.CStep y x := by
  constructor
  · rintro ⟨γ, hγ, h0, h1, ht⟩
    obtain ⟨hc, hd⟩ := reverse_curve hγ
    refine ⟨fun t => γ (1 - t), hc, by simp [h1], by simp [h0], fun t htI => ?_⟩
    have hI : 1 - t ∈ Icc (0:ℝ) 1 := ⟨by linarith [htI.2], by linarith [htI.1]⟩
    obtain ⟨hm, hf⟩ := ht _ hI
    exact ⟨hm, by rw [hd]; exact (S.rev_futCausal _ _).1 hf⟩
  · rintro ⟨γ, hγ, h0, h1, ht⟩
    obtain ⟨hc, hd⟩ := reverse_curve hγ
    refine ⟨fun t => γ (1 - t), hc, by simp [h1], by simp [h0], fun t htI => ?_⟩
    have hI : 1 - t ∈ Icc (0:ℝ) 1 := ⟨by linarith [htI.2], by linarith [htI.1]⟩
    obtain ⟨hm, hf⟩ := ht _ hI
    exact ⟨hm, by rw [hd, S.rev_futCausal, neg_neg]; exact hf⟩

theorem hl_rev_chr (x y : V) : S.rev.Chr x y ↔ S.Chr y x := by
  have e : S.rev.TStep = Function.swap S.TStep := by
    funext x y; exact propext (S.rev_tstep_iff x y)
  unfold Chr; rw [e]; exact Relation.transGen_swap

theorem hl_rev_cau (x y : V) : S.rev.Cau x y ↔ S.Cau y x := by
  have e : S.rev.CStep = Function.swap S.CStep := by
    funext x y; exact propext (S.rev_cstep_iff x y)
  unfold Cau; rw [e]; exact Relation.reflTransGen_swap

/-- **Dual push-up** `q ≪ p ≤ z ⟹ q ≪ z`, by time reversal. -/
theorem hl_pushup' (hL : LocallyLipschitzOn S.M S.g) {q p z : V} (hqp : S.Chr q p) (hpz : S.Cau p z) :
    S.Chr q z := by
  have h := S.rev.hl_pushup (z := q) hL ((S.hl_rev_cau z p).2 hpz) ((S.hl_rev_chr p q).2 hqp)
  exact (S.hl_rev_chr z q).1 h

/-! ### Temporal functions (campaign 60) -/

/-- **A temporal function, repaired (campaign 78, ⓪).** `τ` is `C¹` *on `M`* (not on the whole
chart `V`), with `dτ(v) > 0` for every future-causal `v` at points of `M`. Since `M` is open,
`fderiv ℝ τ x` at `x ∈ M` is the honest derivative of `τ|_M`.

*Change from campaigns 60/72/74/75:* those required `ContDiff ℝ 1 τ` on all of `V`. Applied to
`Dsp J` (whose `M` is `D`), that made `Θ` continuous at every horizon point, contradicting the
blow-up `Θ → ∞` along `𝓝[D] q`, `q ∈ 𝓗⁺`, that the Cauchy property forces (`r7641+71.1`,
`probes/VacuityCheck.lean`): the hypotheses were unsatisfiable whenever `𝓗⁺ ≠ ∅`. The repaired
definition constrains `τ` on `M` only (campaign 78's `cr_isTemporal_congr`, not copied), so no continuity across `∂M` is
imposed. -/
def IsTemporal (τ : V → ℝ) : Prop :=
  ContDiffOn ℝ 1 τ S.M ∧ ∀ x ∈ S.M, ∀ v, S.FutCausal x v → 0 < fderiv ℝ τ x v

/-- A `C¹` curve on `[0,1]` inside `M`, future-causal there, raises a temporal `τ` (repaired
definition: only `τ|_M` is used, via `ContDiffOn.contDiffAt` at the open `M`). -/
lemma temporal_curve {τ : V → ℝ} (hτ : S.IsTemporal τ) {γ : ℝ → V} (hγ : ContDiff ℝ 1 γ)
    (hγt : ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ S.M ∧ S.FutCausal (γ t) (deriv γ t)) :
    τ (γ 0) < τ (γ 1) := by
  have hcont : ContinuousOn (τ ∘ γ) (Icc (0:ℝ) 1) :=
    hτ.1.continuousOn.comp hγ.continuous.continuousOn fun t ht => (hγt t ht).1
  have hmono : StrictMonoOn (τ ∘ γ) (Icc (0:ℝ) 1) := by
    refine strictMonoOn_of_deriv_pos (convex_Icc 0 1) hcont fun t ht => ?_
    rw [interior_Icc] at ht
    have hti : t ∈ Icc (0:ℝ) 1 := Ioo_subset_Icc_self ht
    obtain ⟨hm, h12⟩ := hγt t hti
    have hdτ : DifferentiableAt ℝ τ (γ t) :=
      (hτ.1.contDiffAt (S.isOpen_M.mem_nhds hm)).differentiableAt one_ne_zero
    have hd : HasDerivAt (τ ∘ γ) (fderiv ℝ τ (γ t) (deriv γ t)) t :=
      hdτ.hasFDerivAt.comp_hasDerivAt t (hasDerivAt_of_contDiff hγ t)
    rw [hd.deriv]
    exact hτ.2 _ hm _ h12
  exact hmono ⟨le_rfl, zero_le_one⟩ ⟨zero_le_one, le_rfl⟩ zero_lt_one

lemma temporal_tstep {τ : V → ℝ} (hτ : S.IsTemporal τ) {x y : V} (h : S.TStep x y) :
    τ x < τ y := by
  obtain ⟨γ, hγ, h0, h1, hγt⟩ := h
  have := S.temporal_curve hτ hγ fun t ht => ⟨(hγt t ht).1, (hγt t ht).2.1.le, (hγt t ht).2.2⟩
  rwa [h0, h1] at this

/-- A temporal function increases strictly along `≪` (campaign 60's `hl_temporal_chr`). -/
theorem hl_temporal_chr {τ : V → ℝ} (hτ : S.IsTemporal τ) {x y : V} (h : S.Chr x y) :
    τ x < τ y := by
  induction h with
  | single h => exact S.temporal_tstep hτ h
  | tail _ h ih => exact ih.trans (S.temporal_tstep hτ h)

/-! ### Exterior and horizon -/

variable (J : Set V)

/-- `D = I⁻(𝒥⁺)`. -/
def D : Set V := S.IpastSet J
/-- `𝓗⁺ = ∂J⁻(𝒥⁺)`. -/
def H : Set V := frontier (S.JpastSet J)
/-- A finite slice `S_τ = {x ∈ D | Θ x = τ}`. -/
def slice (Θ : V → ℝ) (τ : ℝ) : Set V := {x | x ∈ S.D J ∧ Θ x = τ}

theorem hl_D_subset_JpastSet : S.D J ⊆ S.JpastSet J :=
  biUnion_mono subset_rfl fun p _ => S.hl_Ipast_subset_Jpast p

end Spacetime

section KL
variable {X : Type*} [TopologicalSpace X]

/-- Kuratowski lower limit of a family of sets as `τ → ∞` (c2: on any topological space). -/
def KLi (A : ℝ → Set X) : Set X := {p | ∀ U ∈ 𝓝 p, ∀ᶠ τ in atTop, (A τ ∩ U).Nonempty}
/-- Kuratowski upper limit of a family of sets as `τ → ∞`. -/
def KLs (A : ℝ → Set X) : Set X := {p | ∀ U ∈ 𝓝 p, ∃ᶠ τ in atTop, (A τ ∩ U).Nonempty}

/-- `Li ⊆ Ls`. -/
theorem hl_KLi_subset_KLs (A : ℝ → Set X) : KLi A ⊆ KLs A :=
  fun _ hp U hU => (hp U hU).frequently

/-- c2: `Ls A ⊆ closure (⋃ A)`, for `A τ ⊆ B`. -/
theorem ch_KLs_subset_closure {A : ℝ → Set X} {B : Set X} (hAB : ∀ τ, A τ ⊆ B) :
    KLs A ⊆ closure B := by
  intro p hp
  rw [mem_closure_iff_nhds]
  intro U hU
  obtain ⟨τ, z, hz, hzU⟩ := (hp U hU).exists
  exact ⟨z, hzU, hAB τ hz⟩

end KL

namespace Spacetime
variable (S : Spacetime V) (J : Set V)

section Observer
variable {S J} {O : ℝ → V} (hOD : S.IpastSet (range O) = S.D J)
  (hmono : ∀ s t : ℝ, s < t → S.Chr (O s) (O t))
include hOD hmono

omit hOD in
/-- `I⁻(O σ) ⊆ I⁻(O τ)` for `σ ≤ τ`. -/
theorem hl_Ipast_mono {σ τ : ℝ} (h : σ ≤ τ) : S.Ipast (O σ) ⊆ S.Ipast (O τ) := by
  rcases h.lt_or_eq with h | h
  · exact fun q hq => S.hl_chr_trans hq (hmono σ τ h)
  · rw [h]

/-- Each `O τ` lies in `D`. -/
theorem hl_observer_mem_D (τ : ℝ) : O τ ∈ S.D J := by
  rw [← hOD]
  exact mem_biUnion (mem_range_self (τ + 1)) (hmono τ (τ + 1) (by linarith))


end Observer

/-! ## Campaign 74: the slice lower limit

### Campaign 60's Cauchy-temporal definitions (copied) -/

/-- Points of `I⁻(z)` lie in `M` (campaign 60's `hl_Ipast_subset_M`). -/
theorem hl_Ipast_subset_M (z : V) : S.Ipast z ⊆ S.M := by
  intro q hq
  obtain ⟨b, ⟨γ, -, h0, -, hγ⟩, -⟩ := Relation.TransGen.head'_iff.1 hq
  rw [← h0]; exact (hγ 0 ⟨le_rfl, zero_le_one⟩).1

/-- `D` is open (campaign 60's `hl_D_open`). -/
theorem hl_D_open : IsOpen (S.D J) := isOpen_biUnion fun z _ => S.hl_isOpen_Ipast z

/-- `D ⊆ M` (campaign 60's `hl_D_subset_M`). -/
theorem hl_D_subset_M : S.D J ⊆ S.M := iUnion₂_subset fun z _ => S.hl_Ipast_subset_M z

/-- The same chart with `M` replaced by an open subset `U ⊆ M` (campaign 60). -/
def restrict (U : Set V) (hU : IsOpen U) (hUM : U ⊆ S.M) : Spacetime V where
  M := U
  isOpen_M := hU
  g := S.g
  cont_g := S.cont_g.mono hUM
  symm := S.symm
  T := S.T
  cont_T := S.cont_T.mono hUM
  T_timelike x hx := S.T_timelike x (hUM hx)
  pos_on_perp x hx := S.pos_on_perp x (hUM hx)

/-- A future-directed, inextendible, piecewise-`C¹` causal curve (campaign 60). -/
structure InextCausalCurve where
  γ : ℝ → V
  cont : Continuous γ
  mem : ∀ t, γ t ∈ S.M
  brk : Set ℝ
  brk_fin : ∀ a b : ℝ, (brk ∩ Icc a b).Finite
  causal : ∀ t ∉ brk, DifferentiableAt ℝ γ t ∧ S.FutCausal (γ t) (deriv γ t)
  inext_future : ¬ ∃ p ∈ S.M, Tendsto γ atTop (𝓝 p)
  inext_past : ¬ ∃ p ∈ S.M, Tendsto γ atBot (𝓝 p)

/-- A Cauchy temporal function (campaign 60): temporal, and every inextendible causal curve meets
every level set exactly once. -/
def IsCauchyTemporal (τ : V → ℝ) : Prop :=
  S.IsTemporal τ ∧ ∀ c : S.InextCausalCurve, ∀ a : ℝ, ∃! t : ℝ, τ (c.γ t) = a

/-- The exterior `D` regarded as a spacetime in its own right. -/
def Dsp : Spacetime V := S.restrict (S.D J) (S.hl_D_open J) (S.hl_D_subset_M J)

/-! ### `Θ` temporal on `D` only: increase along `≪` into `D`

This removes campaign 72's need for `Θ` temporal on all of `M`: a timelike step ending in `D` runs
inside `D`, so a function temporal on `D` (the paper's setting) increases along it. -/

/-- `≪` into `D` starts in `D`. -/
theorem hl_D_of_chr {x y : V} (h : S.Chr x y) (hy : y ∈ S.D J) : x ∈ S.D J := by
  simp only [D, IpastSet, mem_iUnion] at hy ⊢
  obtain ⟨z, hz, hyz⟩ := hy
  exact ⟨z, hz, S.hl_chr_trans h hyz⟩

/-- The tail `γ|[t,1]` of a timelike step, reparametrised onto `[0,1]`, is again a timelike step. -/
lemma tstep_tail {γ : ℝ → V} (hγ : ContDiff ℝ 1 γ)
    (hγt : ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ S.M ∧ S.FutTimelike (γ t) (deriv γ t))
    {t : ℝ} (ht : t ∈ Ico (0:ℝ) 1) : S.TStep (γ t) (γ 1) := by
  have hc : 0 < 1 - t := by linarith [ht.2]
  refine ⟨fun s => γ (t + s * (1 - t)),
    hγ.comp (contDiff_const.add (contDiff_id.mul contDiff_const)), by simp,
    by simp, fun s hs => ?_⟩
  have hmem : t + s * (1 - t) ∈ Icc (0:ℝ) 1 := by
    constructor <;> nlinarith [ht.1, hs.1, hs.2]
  have hd : deriv (fun s => γ (t + s * (1 - t))) s = (1 - t) • deriv γ (t + s * (1 - t)) := by
    have ha : HasDerivAt (fun s : ℝ => t + s * (1 - t)) (1 * (1 - t)) s :=
      ((hasDerivAt_id s).mul_const (1 - t)).const_add t
    have h := (hasDerivAt_of_contDiff hγ (t + s * (1 - t))).scomp s ha
    rw [one_mul] at h
    exact h.deriv
  obtain ⟨hm, h1, h2⟩ := hγt _ hmem
  refine ⟨hm, ?_, ?_⟩
  · rw [hd]
    simp only [map_smul, smul_apply, smul_eq_mul]
    have : 0 < (1 - t) * (1 - t) := mul_pos hc hc
    nlinarith
  · rw [hd]
    simp only [map_smul, smul_apply, smul_eq_mul]
    exact mul_neg_of_pos_of_neg hc h2

/-- A timelike step ending in `D` has every point in `D`. -/
lemma tstep_in_D {γ : ℝ → V} (hγ : ContDiff ℝ 1 γ)
    (hγt : ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ S.M ∧ S.FutTimelike (γ t) (deriv γ t))
    (hy : γ 1 ∈ S.D J) {t : ℝ} (ht : t ∈ Icc (0:ℝ) 1) : γ t ∈ S.D J := by
  rcases ht.2.lt_or_eq with h | h
  · exact S.hl_D_of_chr J (Relation.TransGen.single (S.tstep_tail hγ hγt ⟨ht.1, h⟩)) hy
  · rw [h]; exact hy

/-- A timelike step of `S` ending in `D` is a timelike step of `Dsp J`. -/
lemma tstep_Dsp {x y : V} (h : S.TStep x y) (hy : y ∈ S.D J) : (S.Dsp J).TStep x y := by
  obtain ⟨γ, hγ, h0, h1, hγt⟩ := h
  exact ⟨γ, hγ, h0, h1, fun t ht => ⟨S.tstep_in_D J hγ hγt (h1 ▸ hy) ht, (hγt t ht).2⟩⟩

lemma temporalD_tstep {Θ : V → ℝ} (hΘ : (S.Dsp J).IsTemporal Θ) {x y : V} (h : S.TStep x y)
    (hy : y ∈ S.D J) : Θ x < Θ y :=
  (S.Dsp J).temporal_tstep hΘ (S.tstep_Dsp J h hy)

/-- **A function temporal on `D` only increases along every `≪` ending in `D`.** -/
theorem hl_temporalD_chr {Θ : V → ℝ} (hΘ : (S.Dsp J).IsTemporal Θ) {x y : V} (h : S.Chr x y)
    (hy : y ∈ S.D J) : Θ x < Θ y := by
  induction h with
  | single h => exact S.temporalD_tstep J hΘ h hy
  | @tail b c hxb hbc ih =>
    have hb : b ∈ S.D J := S.hl_D_of_chr J (Relation.TransGen.single hbc) hy
    exact (ih hb).trans (S.temporalD_tstep J hΘ hbc hy)

/-! ### ① `Θ → ∞` at the horizon, from a properness hypothesis -/

/-- **Properness of `Θ` on `D`**: no sublevel set `{x ∈ D | Θ x ≤ T}` accumulates outside `D`
(equivalently, for continuous `Θ`, every sublevel set is closed in `V`: campaign 78's `cr_sublevelProper_iff`, not copied).
This is the content of "`Θ` is a Cauchy time function of `D` whose levels do not reach `∂D`". -/
def SublevelProper (Θ : V → ℝ) : Prop := ∀ T : ℝ, closure {x | x ∈ S.D J ∧ Θ x ≤ T} ⊆ S.D J

/-- `𝓗⁺ ∩ D = ∅`: a horizon point is not in `D`. -/
theorem hl_not_mem_D_of_H {p : V} (hp : p ∈ S.H J) : p ∉ S.D J := fun hpD =>
  hp.2 (interior_maximal (S.hl_D_subset_JpastSet J) (S.hl_D_open J) hpD)

/-! ## Campaign 75: properness and the slice lower limit from the Cauchy property

### Step 1: `q ∈ closure D ⟹ I⁻(q) ⊆ D` -/

/-- The end of a timelike step can be moved in an open set (mirror of `tstep_start_eventually`). -/
lemma tstep_end_eventually {x q : V} (h : S.TStep x q) : ∀ᶠ q' in 𝓝 q, S.TStep x q' := by
  obtain ⟨γ, hγ, h0, h1, hγt⟩ := h
  have hdc : Continuous (deriv γ) := hγ.continuous_deriv le_rfl
  have hT := S.tube (P := fun w t => γ t + t • w) (Q := fun w t => deriv γ t + w)
    ((hγ.continuous.comp continuous_snd).add (continuous_snd.smul continuous_fst))
    ((hdc.comp continuous_snd).add continuous_fst) (by simpa using hγt)
  have hlim : Tendsto (fun q' => q' - q) (𝓝 q) (𝓝 0) := tendsto_sub_nhds_zero_iff.2 tendsto_id
  filter_upwards [hlim.eventually hT] with q' hq'
  refine ⟨fun t => γ t + t • (q' - q), hγ.add (contDiff_id.smul contDiff_const), by simp [h0],
    by simp [h1], fun t ht => ?_⟩
  have hd : deriv (fun t => γ t + t • (q' - q)) t = deriv γ t + (q' - q) := by
    have h : HasDerivAt (fun t => γ t + t • (q' - q)) (deriv γ t + (1:ℝ) • (q' - q)) t :=
      (hasDerivAt_of_contDiff hγ t).add ((hasDerivAt_id' t).smul_const (q' - q))
    rw [h.deriv, one_smul]
  rw [hd]; exact hq' t ht

/-- `I⁺(x) = {y | x ≪ y}` is open. -/
theorem hl_isOpen_Ifut (x : V) : IsOpen {y | S.Chr x y} := by
  refine isOpen_iff_mem_nhds.2 fun q hq => ?_
  obtain ⟨y, hxy, hyq⟩ := Relation.TransGen.tail'_iff.1 hq
  filter_upwards [S.tstep_end_eventually hyq] with q' hq'
  exact Relation.TransGen.tail' hxy hq'

/-- **Step 1.** `q ∈ closure D ⟹ I⁻(q) ⊆ D`: if `x ≪ q`, the open set `I⁺(x)` meets `D` at some
`d`, and `x ≪ d ∈ D` gives `x ∈ D`. -/
theorem hl_Ipast_subset_D {q : V} (hq : q ∈ closure (S.D J)) : S.Ipast q ⊆ S.D J := by
  intro x hx
  obtain ⟨d, hd, hdD⟩ := mem_closure_iff_nhds.1 hq _ ((S.hl_isOpen_Ifut x).mem_nhds hx)
  exact S.hl_D_of_chr J hd hdD

/-! ### Step 2: a timelike segment into `q` along `T(q)` -/

/-- The straight segment `r ↦ q + r • T(q)`. -/
def seg (q : V) (r : ℝ) : V := q + r • S.T q

lemma seg_zero (q : V) : S.seg q 0 = q := by simp [seg]

/-- Near `q ∈ M` the segment stays in `M` with `T(q)` future-timelike along it. -/
lemma seg_timelike {q : V} (hq : q ∈ S.M) : ∃ ε > 0, ∀ r ∈ Icc (-ε) 0,
    S.seg q r ∈ S.M ∧ S.FutTimelike (S.seg q r) (S.T q) := by
  have hc : Continuous fun r : ℝ => (S.seg q r, S.T q) :=
    (continuous_const.add (continuous_id.smul continuous_const)).prodMk continuous_const
  have hO := S.isOpen_timelikePairs.preimage hc
  have h0 : (0:ℝ) ∈ (fun r : ℝ => (S.seg q r, S.T q)) ⁻¹'
      {pv : V × V | pv.1 ∈ S.M ∧ S.FutTimelike pv.1 pv.2} := by
    show S.seg q 0 ∈ S.M ∧ S.FutTimelike (S.seg q 0) (S.T q)
    rw [seg_zero]; exact ⟨hq, S.T_timelike q hq, S.T_timelike q hq⟩
  obtain ⟨δ, hδ, hball⟩ := Metric.isOpen_iff.1 hO 0 h0
  refine ⟨δ / 2, by positivity, fun r hr => hball ?_⟩
  rw [mem_ball, Real.dist_eq, sub_zero, abs_lt]
  constructor <;> linarith [hr.1, hr.2]

/-- Along the segment, `seg q s ≪ seg q s'` (one timelike step) for `-ε ≤ s < s' ≤ 0`. -/
lemma seg_tstep {q : V} {a b : ℝ}
    (hε : ∀ r ∈ Icc a b, S.seg q r ∈ S.M ∧ S.FutTimelike (S.seg q r) (S.T q))
    {s s' : ℝ} (hs : a ≤ s) (hss : s < s') (hs' : s' ≤ b) :
    S.TStep (S.seg q s) (S.seg q s') := by
  have hc : 0 < s' - s := by linarith
  refine ⟨fun u => q + (s + u * (s' - s)) • S.T q, ?_, by simp [seg], by simp [seg], fun u hu => ?_⟩
  · exact contDiff_const.add
      ((contDiff_const.add (contDiff_id.mul contDiff_const)).smul contDiff_const)
  have hd : deriv (fun u => q + (s + u * (s' - s)) • S.T q) u = (s' - s) • S.T q := by
    have h : HasDerivAt (fun u => q + (s + u * (s' - s)) • S.T q) ((1 * (s' - s)) • S.T q) u :=
      ((((hasDerivAt_id u).mul_const (s' - s)).const_add s).smul_const (S.T q)).const_add q
    rw [h.deriv, one_mul]
  have hmem : s + u * (s' - s) ∈ Icc a b := by
    constructor <;> nlinarith [hu.1, hu.2]
  obtain ⟨hm, h1, h2⟩ := hε _ hmem
  refine ⟨hm, ?_, ?_⟩
  · rw [hd]
    simp only [map_smul, smul_apply, smul_eq_mul]
    have : 0 < (s' - s) * (s' - s) := mul_pos hc hc
    exact (by nlinarith : (s' - s) * ((s' - s) * S.g (S.seg q (s + u * (s' - s))) (S.T q) (S.T q)) < 0)
  · rw [hd]
    simp only [map_smul, smul_apply, smul_eq_mul]
    exact mul_neg_of_pos_of_neg hc h2

/-! ### Step 3: the Cauchy property, future-inextendible form -/

/-- A future-directed piecewise-`C¹` causal curve on `[0, ∞)`, future-inextendible in `M`
(the future half of campaign 60's `InextCausalCurve`). -/
structure FutInextCurve where
  γ : ℝ → V
  cont : ContinuousOn γ (Ici 0)
  mem : ∀ t, 0 ≤ t → γ t ∈ S.M
  brk : Set ℝ
  brk_fin : ∀ a b : ℝ, (brk ∩ Icc a b).Finite
  causal : ∀ t, 0 < t → t ∉ brk → DifferentiableAt ℝ γ t ∧ S.FutCausal (γ t) (deriv γ t)
  inext_future : ¬ ∃ p ∈ S.M, Tendsto γ atTop (𝓝 p)

/-- **Cauchy temporal, future form**: `Θ` is temporal, and every future-inextendible causal curve
from `γ 0` attains every level `a ≥ Θ (γ 0)`. Campaign 78: implied by campaign 60's
`IsCauchyTemporal` (`hl_futCauchy_of_cauchy`, ②), and together with the past form equivalent to it
(`hl_cauchy_iff`). -/
def FutCauchyTemporal (Θ : V → ℝ) : Prop :=
  S.IsTemporal Θ ∧ ∀ c : S.FutInextCurve, ∀ a : ℝ, Θ (c.γ 0) ≤ a → ∃ t, 0 ≤ t ∧ Θ (c.γ t) = a


/-! ## Campaign 78 ①: a polygonal past-inextendible extension

Generic in the spacetime `S` (applied below to `Dsp J`, whose `M` is `D`). Vertices
`X 0 = x`, `X (k+1) = X k - ℓ_k • T(X k)`, with the **dyadic safe length**
`ℓ_k = 2^{-n}` for the least `n` such that the segment `X k + r • T(X k)`, `r ∈ [-2^{-n}, 0]`, stays
in `M` and `T(X k)` is future-timelike along it. (The registered "largest safe `ℓ`" supremum is
replaced by this `Nat.find`, the registered fallback; it is locally bounded below by the tube
lemma, `safe_uniform`.) Piece `k` is traversed on `t ∈ [-(k+1), -k]`, so the breaks are integers. -/

/-- `Safe y ℓ`: on `r ∈ [-ℓ, 0]`, `y + r • T y ∈ M` and `T y` is future-timelike there. -/
def Safe (y : V) (ℓ : ℝ) : Prop :=
  ∀ r ∈ Icc (-ℓ) 0, S.seg y r ∈ S.M ∧ S.FutTimelike (S.seg y r) (S.T y)

lemma safe_mono {y : V} {ℓ ℓ' : ℝ} (h : S.Safe y ℓ) (hl : ℓ' ≤ ℓ) : S.Safe y ℓ' :=
  fun r hr => h r ⟨by linarith [hr.1], hr.2⟩

/-- **Tube lemma: a locally uniform safe length.** -/
lemma safe_uniform {x : V} (hx : x ∈ S.M) : ∃ ℓ > 0, ∀ᶠ y in 𝓝 x, S.Safe y ℓ := by
  obtain ⟨ε, hε0, hε⟩ := S.seg_timelike hx
  refine ⟨ε, hε0, ?_⟩
  have hc : ∀ r : ℝ, ContinuousAt (fun z : V × ℝ => (S.seg z.1 z.2, S.T z.1)) (x, r) := fun r =>
    (continuousAt_fst.add (continuousAt_snd.smul ((S.contAt_T hx).comp continuousAt_fst))).prodMk
      ((S.contAt_T hx).comp continuousAt_fst)
  exact isCompact_Icc.eventually_forall_of_forall_eventually
    (P := fun y r => S.seg y r ∈ S.M ∧ S.FutTimelike (S.seg y r) (S.T y))
    fun r hr => (hc r).preimage_mem_nhds (S.isOpen_timelikePairs.mem_nhds (hε r hr))

lemma exists_safe_pow {y : V} (hy : y ∈ S.M) : ∃ n : ℕ, S.Safe y ((1/2:ℝ) ^ n) := by
  obtain ⟨ε, hε0, hε⟩ := S.seg_timelike hy
  obtain ⟨n, hn⟩ := exists_pow_lt_of_lt_one hε0 (by norm_num : (1/2:ℝ) < 1)
  exact ⟨n, S.safe_mono hε hn.le⟩

open Classical in
/-- The dyadic safe length (`1` off `M`, where it is never used). -/
noncomputable def safeLen (y : V) : ℝ :=
  if h : ∃ n : ℕ, S.Safe y ((1/2:ℝ) ^ n) then (1/2:ℝ) ^ (Nat.find h) else 1

lemma safeLen_pos (y : V) : 0 < S.safeLen y := by
  unfold safeLen; split_ifs <;> positivity

open Classical in
lemma safeLen_safe {y : V} (hy : y ∈ S.M) : S.Safe y (S.safeLen y) := by
  have h := S.exists_safe_pow hy
  unfold safeLen; split_ifs with h'
  · exact Nat.find_spec h'
  · exact absurd h h'

open Classical in
lemma safeLen_ge {y : V} {m : ℕ} (h : S.Safe y ((1/2:ℝ) ^ m)) : (1/2:ℝ) ^ m ≤ S.safeLen y := by
  have he : ∃ n : ℕ, S.Safe y ((1/2:ℝ) ^ n) := ⟨m, h⟩
  unfold safeLen; split_ifs with h'
  · exact pow_le_pow_of_le_one (by norm_num) (by norm_num) (Nat.find_min' h' h)
  · exact absurd he h'

/-- The vertices of the polygon. -/
noncomputable def pvert (x : V) : ℕ → V
  | 0 => x
  | k + 1 => S.seg (pvert x k) (-S.safeLen (pvert x k))

lemma pvert_succ_sub (x : V) (k : ℕ) :
    S.pvert x (k + 1) - S.pvert x k = (-S.safeLen (S.pvert x k)) • S.T (S.pvert x k) := by
  simp [pvert, seg]

lemma pvert_mem {x : V} (hx : x ∈ S.M) : ∀ k, S.pvert x k ∈ S.M
  | 0 => hx
  | k + 1 => (S.safeLen_safe (pvert_mem hx k) _
      ⟨le_rfl, neg_nonpos.2 (S.safeLen_pos _).le⟩).1

lemma pvert_tstep {x : V} (hx : x ∈ S.M) (k : ℕ) : S.TStep (S.pvert x (k + 1)) (S.pvert x k) := by
  have h := S.seg_tstep (S.safeLen_safe (S.pvert_mem hx k)) le_rfl
    (neg_lt_zero.2 (S.safeLen_pos _)) le_rfl
  rwa [seg_zero] at h

lemma pvert_rtg {x : V} (hx : x ∈ S.M) : ∀ k, Relation.ReflTransGen S.TStep (S.pvert x k) x
  | 0 => Relation.ReflTransGen.refl
  | k + 1 => Relation.ReflTransGen.head (S.pvert_tstep hx k) (pvert_rtg hx k)

/-- Piece `k` as a function of `u = -t`. -/
noncomputable def ppiece (x : V) (k : ℕ) (u : ℝ) : V :=
  S.pvert x k + (u - k) • (S.pvert x (k + 1) - S.pvert x k)

lemma ppiece_continuous (x : V) (k : ℕ) : Continuous (S.ppiece x k) :=
  continuous_const.add ((continuous_id.sub continuous_const).smul continuous_const)

lemma ppiece_eq_seg (x : V) (k : ℕ) (u : ℝ) :
    S.ppiece x k u = S.seg (S.pvert x k) (-((u - k) * S.safeLen (S.pvert x k))) := by
  rw [ppiece, pvert_succ_sub, smul_smul, seg]; ring_nf

/-- The polygon, as a function of `u = -t` (`Nat.floor` makes it piece `0` for `u < 0`). -/
noncomputable def ppoly (x : V) (u : ℝ) : V := S.ppiece x ⌊u⌋₊ u

lemma ppoly_eq (x : V) (k : ℕ) {u : ℝ} (h1 : (k:ℝ) ≤ u ∨ k = 0) (h2 : u ≤ k + 1) :
    S.ppoly x u = S.ppiece x k u := by
  rcases h2.lt_or_eq with h2 | h2
  · have hk : ⌊u⌋₊ = k := by
      by_cases hu : 0 ≤ u
      · rw [Nat.floor_eq_iff hu]
        rcases h1 with h1 | h1
        · exact ⟨h1, h2⟩
        · subst h1; exact ⟨by simpa using hu, h2⟩
      · rw [Nat.floor_eq_zero.2 (by linarith)]
        rcases h1 with h1 | h1
        · exact absurd (le_trans (Nat.cast_nonneg k) h1) hu
        · exact h1.symm
    rw [ppoly, hk]
  · have hk : ⌊u⌋₊ = k + 1 := by rw [h2]; exact_mod_cast Nat.floor_natCast (k + 1)
    rw [ppoly, hk, ppiece, ppiece, h2]
    simp

lemma ppoly_continuous (x : V) : Continuous (S.ppoly x) := by
  rw [continuous_iff_continuousAt]
  intro u
  by_cases hu1 : u < 1
  · refine (S.ppiece_continuous x 0).continuousAt.congr ?_
    filter_upwards [Iio_mem_nhds hu1] with v hv
    exact (S.ppoly_eq x 0 (Or.inr rfl) (by simpa using hv.le)).symm
  set n := ⌊u⌋₊ with hn
  have hnu : (n:ℝ) ≤ u := Nat.floor_le (by linarith)
  have hun : u < n + 1 := Nat.lt_floor_add_one u
  by_cases hne : (n:ℝ) < u
  · refine (S.ppiece_continuous x n).continuousAt.congr ?_
    filter_upwards [Ioo_mem_nhds hne hun] with v hv
    exact (S.ppoly_eq x n (Or.inl hv.1.le) hv.2.le).symm
  have hequ : u = n := le_antisymm (not_lt.1 hne) hnu
  have hn1 : 1 ≤ n := by
    by_contra h
    have : n = 0 := by omega
    rw [this] at hequ; norm_num at hequ; linarith
  obtain ⟨k, hk⟩ : ∃ k, n = k + 1 := ⟨n - 1, by omega⟩
  rw [hk] at hequ
  push_cast at hequ
  have hA : ContinuousWithinAt (S.ppoly x) (Icc (k:ℝ) (k + 1)) u :=
    (S.ppiece_continuous x k).continuousWithinAt.congr
      (fun v hv => S.ppoly_eq x k (Or.inl hv.1) hv.2) (S.ppoly_eq x k (Or.inl (by linarith)) hequ.le)
  have hB : ContinuousWithinAt (S.ppoly x) (Icc ((k:ℝ) + 1) (k + 1 + 1)) u :=
    (S.ppiece_continuous x (k + 1)).continuousWithinAt.congr
      (fun v hv => S.ppoly_eq x (k + 1) (Or.inl (by push_cast; exact hv.1)) (by push_cast; exact hv.2))
      (S.ppoly_eq x (k + 1) (Or.inl (by push_cast; linarith)) (by push_cast; linarith))
  refine (hA.union hB).continuousAt (mem_of_superset (Ioo_mem_nhds (a := (k:ℝ))
    (b := k + 1 + 1) (by linarith) (by linarith)) fun v hv => ?_)
  rcases le_total v (k + 1) with h | h
  · exact Or.inl ⟨hv.1.le, h⟩
  · exact Or.inr ⟨h, hv.2.le⟩

/-- On piece `k`, the polygon point is on the safe segment of `X k`. -/
lemma ppoly_seg {x : V} (k : ℕ) {u : ℝ} (h1 : (k:ℝ) ≤ u) (h2 : u ≤ k + 1) :
    S.ppoly x u = S.seg (S.pvert x k) (-((u - k) * S.safeLen (S.pvert x k))) ∧
      -((u - k) * S.safeLen (S.pvert x k)) ∈ Icc (-S.safeLen (S.pvert x k)) 0 := by
  refine ⟨by rw [S.ppoly_eq x k (Or.inl h1) h2, ppiece_eq_seg], ?_⟩
  have hl := S.safeLen_pos (S.pvert x k)
  constructor <;> nlinarith

/-- The integers, as break points, are finite on compacts. -/
lemma int_brk_fin (a b : ℝ) : (range (Int.cast : ℤ → ℝ) ∩ Icc a b).Finite := by
  refine ((Set.finite_Icc ⌊a⌋ ⌈b⌉).image (Int.cast : ℤ → ℝ)).subset ?_
  rintro _ ⟨⟨z, rfl⟩, hz1, hz2⟩
  refine ⟨z, ⟨?_, ?_⟩, rfl⟩
  · exact Int.floor_le_iff.2 (by linarith)
  · exact Int.le_ceil_iff.2 (by linarith) 

/-- **① BUILT. A polygonal past-inextendible extension.** From any `x ∈ M` there is a continuous
`p : ℝ → V` with `p 0 = x`, `p t ∈ M` and `p t ≪ x` for `t < 0`, `C¹` and future-timelike (so
future-causal) off the integers on `t < 0`, and with no past limit in `M`.

*Joint satisfiability:* the only hypothesis is `x ∈ M` (e.g. any point of `D` for `Dsp J`).

*No past limit:* if `p t → x* ∈ M` as `t → -∞`, then `X k → x*`, the tube lemma at `x*` bounds
`ℓ_k ≥ 2^{-m}` eventually, and `‖X (k+1) - X k‖ = ℓ_k ‖T (X k)‖ → 0` contradicts
`‖T (X k)‖ → ‖T x*‖ > 0`. -/
theorem hl_past_extension {x : V} (hx : x ∈ S.M) :
    ∃ p : ℝ → V, Continuous p ∧ p 0 = x ∧ (∀ t ≤ 0, p t ∈ S.M) ∧ (∀ t < 0, S.Chr (p t) x) ∧
      (∀ t < 0, t ∉ range (Int.cast : ℤ → ℝ) →
        DifferentiableAt ℝ p t ∧ S.FutTimelike (p t) (deriv p t)) ∧
      ¬ ∃ q ∈ S.M, Tendsto p atBot (𝓝 q) := by
  refine ⟨fun t => S.ppoly x (-t), (S.ppoly_continuous x).comp continuous_neg, ?_, ?_, ?_, ?_, ?_⟩
  · show S.ppoly x (-0) = x
    rw [neg_zero, S.ppoly_eq x 0 (Or.inr rfl) (by norm_num), ppiece]; simp [pvert]
  · intro t ht
    set u := -t
    have hu : 0 ≤ u := by simp [u]; linarith
    obtain ⟨hs, hr⟩ := S.ppoly_seg (x := x) ⌊u⌋₊ (Nat.floor_le hu) (Nat.lt_floor_add_one u).le
    show S.ppoly x u ∈ S.M
    rw [hs]; exact (S.safeLen_safe (S.pvert_mem hx _) _ hr).1
  · intro t ht
    set u := -t
    have hu : 0 < u := by simp [u]; linarith
    set k := ⌈u⌉₊ - 1
    have hc1 : 1 ≤ ⌈u⌉₊ := Nat.one_le_iff_ne_zero.2 (by positivity)
    have hk : (k:ℝ) + 1 = ⌈u⌉₊ := by simp only [k]; push_cast [Nat.cast_sub hc1]; ring
    have h1 : (k:ℝ) < u := by linarith [Nat.ceil_lt_add_one hu.le]
    have h2 : u ≤ k + 1 := hk ▸ Nat.le_ceil u
    obtain ⟨hs, hr⟩ := S.ppoly_seg (x := x) k h1.le h2
    show S.Chr (S.ppoly x u) x
    rw [hs]
    have hl := S.safeLen_pos (S.pvert x k)
    have hst := S.seg_tstep (S.safeLen_safe (S.pvert_mem hx k)) hr.1
      (by have : 0 < (u - k) * S.safeLen (S.pvert x k) := mul_pos (by linarith) hl
          linarith) le_rfl
    rw [seg_zero] at hst
    exact Relation.TransGen.head' hst (S.pvert_rtg hx k)
  · intro t ht hbrk
    set u := -t with hu_def
    have hu : 0 < u := by simp [u]; linarith
    set n := ⌊u⌋₊
    have hnu : (n:ℝ) ≤ u := Nat.floor_le hu.le
    have hun : u < n + 1 := Nat.lt_floor_add_one u
    have hne : (n:ℝ) < u := by
      refine lt_of_le_of_ne hnu fun h => hbrk ⟨-(n:ℤ), ?_⟩
      push_cast; rw [h, hu_def, neg_neg]
    have hev : (fun t => S.ppoly x (-t)) =ᶠ[𝓝 t] fun s => S.ppiece x n (-s) := by
      filter_upwards [(continuous_neg.tendsto t).eventually (Ioo_mem_nhds hne hun)] with s hs
      exact S.ppoly_eq x n (Or.inl hs.1.le) hs.2.le
    have hd : HasDerivAt (fun s => S.ppiece x n (-s))
        (S.safeLen (S.pvert x n) • S.T (S.pvert x n)) t := by
      have h := (((hasDerivAt_neg t).sub_const (n:ℝ)).smul_const
        (S.pvert x (n + 1) - S.pvert x n)).const_add (S.pvert x n)
      rw [pvert_succ_sub, smul_smul] at h
      simpa [ppiece, pvert_succ_sub] using h
    refine ⟨hd.differentiableAt.congr_of_eventuallyEq hev, ?_⟩
    rw [hev.deriv_eq, hd.deriv]
    obtain ⟨hs, hr⟩ := S.ppoly_seg (x := x) n hnu hun.le
    obtain ⟨-, h1, h2⟩ := S.safeLen_safe (S.pvert_mem hx n) _ hr
    have hl := S.safeLen_pos (S.pvert x n)
    show S.FutTimelike (S.ppoly x u) _
    rw [hs]
    refine ⟨?_, ?_⟩ <;> simp only [map_smul, smul_apply, smul_eq_mul]
    · have : 0 < S.safeLen (S.pvert x n) * S.safeLen (S.pvert x n) := mul_pos hl hl
      nlinarith
    · exact mul_neg_of_pos_of_neg hl h2
  · rintro ⟨q, hq, hlim⟩
    have hX : Tendsto (S.pvert x) atTop (𝓝 q) := by
      have h := hlim.comp (tendsto_neg_atTop_atBot.comp tendsto_natCast_atTop_atTop)
      refine h.congr fun k => ?_
      show S.ppoly x (-(-(k:ℝ))) = S.pvert x k
      rw [neg_neg, S.ppoly_eq x k (Or.inl le_rfl) (by linarith)]; simp [ppiece]
    obtain ⟨ℓ₀, hℓ₀, hsafe⟩ := S.safe_uniform hq
    obtain ⟨m, hm⟩ := exists_pow_lt_of_lt_one hℓ₀ (by norm_num : (1/2:ℝ) < 1)
    set c : ℝ := (1/2:ℝ) ^ m
    have hc : 0 < c := by positivity
    have hTq : 0 < ‖S.T q‖ := norm_pos_iff.2 fun h0 => by
      have := S.T_timelike q hq; rw [h0] at this; simp at this
    have hev1 : ∀ᶠ k in atTop, c ≤ S.safeLen (S.pvert x k) :=
      (hX.eventually hsafe).mono fun k hk => S.safeLen_ge (S.safe_mono hk hm.le)
    have hev2 : ∀ᶠ k in atTop, ‖S.T q‖ / 2 < ‖S.T (S.pvert x k)‖ :=
      ((S.contAt_T hq).tendsto.comp hX).norm.eventually (lt_mem_nhds (by linarith))
    have hdiff : Tendsto (fun k => S.pvert x (k + 1) - S.pvert x k) atTop (𝓝 0) := by
      have := (hX.comp (tendsto_add_atTop_nat 1)).sub hX
      rwa [sub_self] at this
    have hev3 : ∀ᶠ k in atTop, ‖S.pvert x (k + 1) - S.pvert x k‖ < c * (‖S.T q‖ / 2) :=
      hdiff.norm.eventually (by rw [norm_zero]; exact gt_mem_nhds (show (0:ℝ) < c * (‖S.T q‖ / 2) by positivity))
    obtain ⟨k, h1, h2, h3⟩ := (hev1.and (hev2.and hev3)).exists
    rw [pvert_succ_sub, norm_smul, Real.norm_eq_abs, abs_neg,
      abs_of_pos (S.safeLen_pos _)] at h3
    have : c * (‖S.T q‖ / 2) ≤ S.safeLen (S.pvert x k) * ‖S.T (S.pvert x k)‖ :=
      mul_le_mul h1 h2.le (by positivity) (S.safeLen_pos _).le
    linarith

/-! ## Campaign 78 ②: two-sided Cauchy ⇒ future form -/

/-- **② BUILT. Campaign 60's two-sided Cauchy property implies the future form** (both with the
repaired `IsTemporal`), in any spacetime. A future-inextendible curve `c` is glued at `0` to the
polygonal past extension of `c.γ 0` (①); the glued curve is inextendible, so it meets level `a`
exactly once, and since `Θ` strictly increases along `≪` the hit of `a ≥ Θ (c.γ 0)` is at `t ≥ 0`.

*Joint satisfiability:* a single hypothesis, `IsCauchyTemporal Θ`; e.g. in Minkowski space the
time coordinate is Cauchy temporal (standard; not formalised here). -/
theorem hl_futCauchy_of_cauchy {Θ : V → ℝ} (hΘ : S.IsCauchyTemporal Θ) : S.FutCauchyTemporal Θ := by
  refine ⟨hΘ.1, fun c a ha => ?_⟩
  obtain ⟨p, hpc, hp0, hpM, hpchr, hpd, hpinext⟩ := S.hl_past_extension (c.mem 0 le_rfl)
  set γ : ℝ → V := fun t => if t ≤ 0 then p t else c.γ t with hγ
  have hγc : Continuous γ :=
    continuous_if_le (f := fun t : ℝ => t) (g := fun _ => (0:ℝ)) continuous_id continuous_const
      hpc.continuousOn c.cont fun t (ht : t = 0) => by rw [ht, hp0]
  have hγneg : ∀ t ≤ 0, γ t = p t := fun t ht => by simp [hγ, ht]
  have hγpos : ∀ t, 0 < t → γ t = c.γ t := fun t ht => by simp [hγ, not_le.2 ht]
  have hγ0 : ∀ t, 0 ≤ t → γ t = c.γ t := by
    intro t ht
    rcases ht.lt_or_eq with h | h
    · exact hγpos t h
    · rw [← h, hγneg 0 le_rfl, hp0]
  let C : S.InextCausalCurve :=
    { γ := γ
      cont := hγc
      mem := fun t => by
        rcases le_or_gt t 0 with h | h
        · rw [hγneg t h]; exact hpM t h
        · rw [hγpos t h]; exact c.mem t h.le
      brk := c.brk ∪ range (Int.cast : ℤ → ℝ)
      brk_fin := fun a b => by
        rw [union_inter_distrib_right]; exact (c.brk_fin a b).union (int_brk_fin a b)
      causal := fun t ht => by
        have ht0 : t ≠ 0 := fun h => ht (Or.inr ⟨0, by simp [h]⟩)
        rcases lt_or_gt_of_ne ht0 with h | h
        · have hev : γ =ᶠ[𝓝 t] p := by
            filter_upwards [Iio_mem_nhds h] with s hs using hγneg s hs.le
          obtain ⟨hd, hft⟩ := hpd t h fun hb => ht (Or.inr hb)
          refine ⟨hd.congr_of_eventuallyEq hev, ?_⟩
          rw [hev.deriv_eq, hγneg t h.le]; exact ⟨hft.1.le, hft.2⟩
        · have hev : γ =ᶠ[𝓝 t] c.γ := by
            filter_upwards [Ioi_mem_nhds h] with s hs using hγpos s hs
          obtain ⟨hd, hft⟩ := c.causal t h fun hb => ht (Or.inl hb)
          refine ⟨hd.congr_of_eventuallyEq hev, ?_⟩
          rw [hev.deriv_eq, hγpos t h]; exact hft
      inext_future := by
        rintro ⟨q, hq, hlim⟩
        refine c.inext_future ⟨q, hq, hlim.congr' ?_⟩
        filter_upwards [eventually_gt_atTop 0] with s hs using hγpos s hs
      inext_past := by
        rintro ⟨q, hq, hlim⟩
        refine hpinext ⟨q, hq, hlim.congr' ?_⟩
        filter_upwards [eventually_le_atBot 0] with s hs using hγneg s hs }
  obtain ⟨t, ht, -⟩ := hΘ.2 C a
  change Θ (γ t) = a at ht
  rcases lt_or_ge t 0 with h | h
  · rw [hγneg t h.le] at ht
    have := S.hl_temporal_chr hΘ.1 (hpchr t h)
    linarith
  · exact ⟨t, h, by rw [← hγ0 t h]; exact ht⟩


/-! ## Campaign 78, stretch: two-sided ⇔ future ∧ past

The past form, by time reversal: `rev` flips `T`, so `rev`'s polygonal past extension (①) is a
future extension of `S`. -/

/-- A future-directed piecewise-`C¹` causal curve on `(-∞, 0]`, past-inextendible in `M`. -/
structure PastInextCurve where
  γ : ℝ → V
  cont : ContinuousOn γ (Iic 0)
  mem : ∀ t, t ≤ 0 → γ t ∈ S.M
  brk : Set ℝ
  brk_fin : ∀ a b : ℝ, (brk ∩ Icc a b).Finite
  causal : ∀ t, t < 0 → t ∉ brk → DifferentiableAt ℝ γ t ∧ S.FutCausal (γ t) (deriv γ t)
  inext_past : ¬ ∃ p ∈ S.M, Tendsto γ atBot (𝓝 p)

/-- **Cauchy temporal, past form**: every past-inextendible causal curve ending at `γ 0` attains
every level `a ≤ Θ (γ 0)`. -/
def PastCauchyTemporal (Θ : V → ℝ) : Prop :=
  S.IsTemporal Θ ∧ ∀ c : S.PastInextCurve, ∀ a : ℝ, a ≤ Θ (c.γ 0) → ∃ t, t ≤ 0 ∧ Θ (c.γ t) = a

/-- **Future polygonal extension** (① for `rev`, reversed): from `x ∈ M`, a continuous `p` with
`p 0 = x`, `x ≪ p t` for `t > 0`, future-timelike off the integers, no future limit in `M`. -/
theorem hl_future_extension {x : V} (hx : x ∈ S.M) :
    ∃ p : ℝ → V, Continuous p ∧ p 0 = x ∧ (∀ t, 0 ≤ t → p t ∈ S.M) ∧
      (∀ t, 0 < t → S.Chr x (p t)) ∧
      (∀ t, 0 < t → t ∉ range (Int.cast : ℤ → ℝ) →
        DifferentiableAt ℝ p t ∧ S.FutTimelike (p t) (deriv p t)) ∧
      ¬ ∃ q ∈ S.M, Tendsto p atTop (𝓝 q) := by
  obtain ⟨p, hpc, hp0, hpM, hpchr, hpd, hpinext⟩ := S.rev.hl_past_extension (x := x) hx
  refine ⟨fun t => p (-t), hpc.comp continuous_neg, by simp [hp0],
    fun t ht => hpM (-t) (by linarith), fun t ht => (S.hl_rev_chr _ _).1 (hpchr (-t) (by linarith)),
    fun t ht hb => ?_, ?_⟩
  · have hb' : -t ∉ range (Int.cast : ℤ → ℝ) := fun ⟨z, hz⟩ =>
      hb ⟨-z, by push_cast; rw [hz, neg_neg]⟩
    obtain ⟨hd, hft⟩ := hpd (-t) (by linarith) hb'
    have hD : HasDerivAt (fun t => p (-t)) (-deriv p (-t)) t := by
      have := hd.hasDerivAt.scomp t (hasDerivAt_neg t)
      simpa [Function.comp_def] using this
    exact ⟨hD.differentiableAt, hD.deriv ▸ (S.rev_futTimelike _ _).1 hft⟩
  · rintro ⟨q, hq, hlim⟩
    exact hpinext ⟨q, hq, by simpa [Function.comp_def] using hlim.comp tendsto_neg_atBot_atTop⟩

/-- **Two-sided ⇒ past form** (mirror of ②, gluing the future extension at `0`). -/
theorem hl_pastCauchy_of_cauchy {Θ : V → ℝ} (hΘ : S.IsCauchyTemporal Θ) :
    S.PastCauchyTemporal Θ := by
  refine ⟨hΘ.1, fun c a ha => ?_⟩
  obtain ⟨p, hpc, hp0, hpM, hpchr, hpd, hpinext⟩ := S.hl_future_extension (c.mem 0 le_rfl)
  set γ : ℝ → V := fun t => if t ≤ 0 then c.γ t else p t with hγ
  have hγc : Continuous γ :=
    continuous_if_le (f := fun t : ℝ => t) (g := fun _ => (0:ℝ)) continuous_id continuous_const
      c.cont hpc.continuousOn fun t (ht : t = 0) => by rw [ht, hp0]
  have hγneg : ∀ t ≤ 0, γ t = c.γ t := fun t ht => by simp [hγ, ht]
  have hγpos : ∀ t, 0 < t → γ t = p t := fun t ht => by simp [hγ, not_le.2 ht]
  let C : S.InextCausalCurve :=
    { γ := γ
      cont := hγc
      mem := fun t => by
        rcases le_or_gt t 0 with h | h
        · rw [hγneg t h]; exact c.mem t h
        · rw [hγpos t h]; exact hpM t h.le
      brk := c.brk ∪ range (Int.cast : ℤ → ℝ)
      brk_fin := fun a b => by
        rw [union_inter_distrib_right]; exact (c.brk_fin a b).union (int_brk_fin a b)
      causal := fun t ht => by
        have ht0 : t ≠ 0 := fun h => ht (Or.inr ⟨0, by simp [h]⟩)
        rcases lt_or_gt_of_ne ht0 with h | h
        · have hev : γ =ᶠ[𝓝 t] c.γ := by
            filter_upwards [Iio_mem_nhds h] with s hs using hγneg s hs.le
          obtain ⟨hd, hft⟩ := c.causal t h fun hb => ht (Or.inl hb)
          refine ⟨hd.congr_of_eventuallyEq hev, ?_⟩
          rw [hev.deriv_eq, hγneg t h.le]; exact hft
        · have hev : γ =ᶠ[𝓝 t] p := by
            filter_upwards [Ioi_mem_nhds h] with s hs using hγpos s hs
          obtain ⟨hd, hft⟩ := hpd t h fun hb => ht (Or.inr hb)
          refine ⟨hd.congr_of_eventuallyEq hev, ?_⟩
          rw [hev.deriv_eq, hγpos t h]; exact ⟨hft.1.le, hft.2⟩
      inext_future := by
        rintro ⟨q, hq, hlim⟩
        refine hpinext ⟨q, hq, hlim.congr' ?_⟩
        filter_upwards [eventually_gt_atTop 0] with s hs using hγpos s hs
      inext_past := by
        rintro ⟨q, hq, hlim⟩
        refine c.inext_past ⟨q, hq, hlim.congr' ?_⟩
        filter_upwards [eventually_le_atBot 0] with s hs using hγneg s hs }
  obtain ⟨t, ht, -⟩ := hΘ.2 C a
  change Θ (γ t) = a at ht
  rcases le_or_gt t 0 with h | h
  · exact ⟨t, h, by rw [← hγneg t h]; exact ht⟩
  · rw [hγpos t h] at ht
    have := S.hl_temporal_chr hΘ.1 (hpchr t h)
    linarith

/-- A continuous `f` with `f' > 0` off a set `B` finite on bounded intervals is strictly
increasing on every `[a, b]` (induction on the number of breaks). -/
lemma strictMonoOn_of_brk {f : ℝ → ℝ} {B : Set ℝ} (hf : Continuous f)
    (hd : ∀ x ∉ B, 0 < deriv f x) :
    ∀ n : ℕ, ∀ a b : ℝ, (B ∩ Ioo a b).Finite → (B ∩ Ioo a b).ncard ≤ n →
      StrictMonoOn f (Icc a b) := by
  have base : ∀ a b : ℝ, B ∩ Ioo a b = ∅ → StrictMonoOn f (Icc a b) := fun a b hE =>
    strictMonoOn_of_deriv_pos (convex_Icc a b) hf.continuousOn fun x hx => hd x fun hxB => by
      rw [interior_Icc] at hx
      have : x ∈ B ∩ Ioo a b := ⟨hxB, hx⟩
      rw [hE] at this; exact this
  intro n
  induction n with
  | zero =>
    intro a b hfin hn
    exact base a b ((Set.ncard_eq_zero hfin).1 (Nat.le_zero.1 hn))
  | succ n ih =>
    intro a b hfin hn
    rcases (B ∩ Ioo a b).eq_empty_or_nonempty with hE | ⟨c, hcB, hc⟩
    · exact base a b hE
    have hsub : ∀ a' b' : ℝ, a ≤ a' → b' ≤ b → c ∉ Ioo a' b' →
        StrictMonoOn f (Icc a' b') := by
      intro a' b' ha hb hcn
      have hs : B ∩ Ioo a' b' ⊆ B ∩ Ioo a b :=
        inter_subset_inter_right _ (Ioo_subset_Ioo ha hb)
      have hss : B ∩ Ioo a' b' ⊂ B ∩ Ioo a b :=
        (Set.ssubset_iff_of_subset hs).2 ⟨c, ⟨hcB, hc⟩, fun h => hcn h.2⟩
      exact ih a' b' (hfin.subset hs) (Nat.lt_succ_iff.1 ((Set.ncard_lt_ncard hss hfin).trans_le hn))
    have h1 := hsub a c le_rfl hc.2.le fun h => lt_irrefl c h.2
    have h2 := hsub c b hc.1.le le_rfl fun h => lt_irrefl c h.1
    have := h1.union h2 (isGreatest_Icc hc.1.le) (isLeast_Icc hc.2.le)
    rwa [Icc_union_Icc_eq_Icc hc.1.le hc.2.le] at this

/-- A temporal `Θ` strictly increases along every inextendible causal curve. -/
theorem hl_strictMono_curve {Θ : V → ℝ} (hΘ : S.IsTemporal Θ) (c : S.InextCausalCurve) :
    StrictMono (Θ ∘ c.γ) := by
  have hf : Continuous (Θ ∘ c.γ) := hΘ.1.continuousOn.comp_continuous c.cont c.mem
  have hd : ∀ t ∉ c.brk, 0 < deriv (Θ ∘ c.γ) t := by
    intro t ht
    obtain ⟨hγd, hft⟩ := c.causal t ht
    have hdΘ : DifferentiableAt ℝ Θ (c.γ t) :=
      (hΘ.1.contDiffAt (S.isOpen_M.mem_nhds (c.mem t))).differentiableAt one_ne_zero
    rw [(hdΘ.hasFDerivAt.comp_hasDerivAt t hγd.hasDerivAt).deriv]
    exact hΘ.2 _ (c.mem t) _ hft
  intro s t hst
  have hfin : (c.brk ∩ Ioo s t).Finite :=
    (c.brk_fin s t).subset (inter_subset_inter_right _ Ioo_subset_Icc_self)
  exact strictMonoOn_of_brk hf hd _ s t hfin le_rfl ⟨le_rfl, hst.le⟩ ⟨hst.le, le_rfl⟩ hst

/-- **Stretch BUILT: two-sided ⇔ future ∧ past.** Campaign 60's `IsCauchyTemporal` is exactly the
conjunction of the future and past forms (all with the repaired `IsTemporal`). The future form
alone is weaker (`exp ∘ Θ` is future Cauchy and never negative; not formalised).

*Joint satisfiability:* an equivalence; either side holds e.g. for the time coordinate of
Minkowski space (standard; not formalised here). -/
theorem hl_cauchy_iff {Θ : V → ℝ} :
    S.IsCauchyTemporal Θ ↔ S.FutCauchyTemporal Θ ∧ S.PastCauchyTemporal Θ := by
  refine ⟨fun h => ⟨S.hl_futCauchy_of_cauchy h, S.hl_pastCauchy_of_cauchy h⟩,
    fun ⟨hF, hP⟩ => ⟨hF.1, fun c a => ?_⟩⟩
  obtain ⟨t, ht⟩ : ∃ t, Θ (c.γ t) = a := by
    rcases le_total (Θ (c.γ 0)) a with h | h
    · obtain ⟨t, -, ht⟩ := hF.2 ⟨c.γ, c.cont.continuousOn, fun t _ => c.mem t, c.brk, c.brk_fin,
        fun t _ hb => c.causal t hb, c.inext_future⟩ a h
      exact ⟨t, ht⟩
    · obtain ⟨t, -, ht⟩ := hP.2 ⟨c.γ, c.cont.continuousOn, fun t _ => c.mem t, c.brk, c.brk_fin,
        fun t _ hb => c.causal t hb, c.inext_past⟩ a h
      exact ⟨t, ht⟩
  exact ⟨t, ht, fun s hs => (S.hl_strictMono_curve hF.1 c).injective (hs.trans ht.symm)⟩

/-! ## Campaign 81 ①: `hint` and `hcl` by push-up -/

/-- The segment `r ↦ q + r • T(q)`, `|r| ≤ ε`, stays in `M` with `T(q)` future-timelike along it
(two-sided form of `seg_timelike`). -/
lemma hl_seg_timelike2 {q : V} (hq : q ∈ S.M) : ∃ ε > 0, ∀ r ∈ Icc (-ε) ε,
    S.seg q r ∈ S.M ∧ S.FutTimelike (S.seg q r) (S.T q) := by
  have hc : Continuous fun r : ℝ => (S.seg q r, S.T q) :=
    (continuous_const.add (continuous_id.smul continuous_const)).prodMk continuous_const
  have hO := S.isOpen_timelikePairs.preimage hc
  have h0 : (0:ℝ) ∈ (fun r : ℝ => (S.seg q r, S.T q)) ⁻¹'
      {pv : V × V | pv.1 ∈ S.M ∧ S.FutTimelike pv.1 pv.2} := by
    show S.seg q 0 ∈ S.M ∧ S.FutTimelike (S.seg q 0) (S.T q)
    rw [seg_zero]; exact ⟨hq, S.T_timelike q hq, S.T_timelike q hq⟩
  obtain ⟨δ, hδ, hball⟩ := Metric.isOpen_iff.1 hO 0 h0
  refine ⟨δ / 2, by positivity, fun r hr => hball ?_⟩
  rw [mem_ball, Real.dist_eq, sub_zero, abs_lt]
  constructor <;> linarith [hr.1, hr.2]

lemma hl_seg_tendsto (q : V) : Tendsto (S.seg q) (𝓝 0) (𝓝 q) := by
  have h : Continuous (S.seg q) := continuous_const.add (continuous_id.smul continuous_const)
  have := h.tendsto 0
  rwa [S.seg_zero] at this

/-- **The short future step** (the registered "reachable negative" lemma, BUILT): for `x ∈ M`, every
neighbourhood `N` of `x` contains a `y = x + r T(x)` with `x ≪ y`, via one `TStep` inside `M`. -/
theorem hl_future_step {x : V} (hx : x ∈ S.M) {N : Set V} (hN : N ∈ 𝓝 x) :
    ∃ y ∈ N, S.Chr x y := by
  obtain ⟨ε, hε, hseg⟩ := S.hl_seg_timelike2 hx
  have hc := (S.hl_seg_tendsto x).mono_left (nhdsWithin_le_nhds (s := Ioi 0))
  obtain ⟨r, hrN, hr0, hrε⟩ := ((hc.eventually hN).and (Ioo_mem_nhdsGT hε)).exists
  refine ⟨S.seg x r, hrN, Relation.TransGen.single ?_⟩
  have h := S.seg_tstep hseg (by linarith) hr0 hrε.le
  rwa [seg_zero] at h

/-- **The short past step**: every neighbourhood of `x ∈ M` contains a `y = x − r T(x)`, `y ≪ x`. -/
theorem hl_past_step {x : V} (hx : x ∈ S.M) {N : Set V} (hN : N ∈ 𝓝 x) :
    ∃ y ∈ N, S.Chr y x := by
  obtain ⟨ε, hε, hseg⟩ := S.hl_seg_timelike2 hx
  have hc := (S.hl_seg_tendsto x).mono_left (nhdsWithin_le_nhds (s := Iio 0))
  obtain ⟨r, hrN, hrε, hr0⟩ := ((hc.eventually hN).and (Ioo_mem_nhdsLT (neg_lt_zero.2 hε))).exists
  refine ⟨S.seg x r, hrN, Relation.TransGen.single ?_⟩
  have h := S.seg_tstep hseg hrε.le hr0 hε.le
  rwa [seg_zero] at h

/-- A point of `J⁻(z)` is `z` itself or lies in `M`. -/
lemma hl_cau_mem {x z : V} (h : S.Cau x z) : x ∈ S.M ∨ x = z := by
  rcases Relation.ReflTransGen.cases_head h with h | ⟨b, ⟨γ, -, h0, -, hγ⟩, -⟩
  · exact Or.inr h
  · left; rw [← h0]; exact (hγ 0 ⟨le_rfl, zero_le_one⟩).1

/-- `J ⊆ M ⟹ J⁻(J) ⊆ M`. -/
theorem hl_JpastSet_subset_M (hJM : J ⊆ S.M) : S.JpastSet J ⊆ S.M := by
  intro x hx
  simp only [JpastSet, mem_iUnion] at hx
  obtain ⟨z, hz, hxz⟩ := hx
  rcases S.hl_cau_mem hxz with h | h
  · exact h
  · exact h ▸ hJM hz



end Spacetime

/-! ## (1) The model: 2D Minkowski in null coordinates, `J` the Rindler worldline

The chart is `P = ℝ × ℝ` with `p = (U, V)`, `U = t − x`, `V = t + x`. Then
`−dt² + dx² = −dU dV`, i.e. `g(a, b) = −(a_U b_V + a_V b_U)/2`, and `T = ∂_t = ∂_U + ∂_V = (1, 1)`.
`M` is the whole plane. -/

namespace Model
open ContinuousLinearMap

set_option synthInstance.maxHeartbeats 400000

/-- Null coordinates `p = (U, V)`. -/
abbrev P := ℝ × ℝ

/-- `g = −dU dV` (symmetrised). -/
noncomputable def gM : P →L[ℝ] P →L[ℝ] ℝ :=
  (-(1/2 : ℝ)) • ((fst ℝ ℝ ℝ).smulRight (snd ℝ ℝ ℝ) + (snd ℝ ℝ ℝ).smulRight (fst ℝ ℝ ℝ))

lemma gM_apply (v w : P) : gM v w = -(v.1 * w.2 + v.2 * w.1) / 2 := by
  simp [gM]; ring

/-- 2D Minkowski space, `M = ℝ²`, `T = ∂_t`. -/
noncomputable def mink : Spacetime P where
  M := univ
  isOpen_M := isOpen_univ
  g := fun _ => gM
  cont_g := continuousOn_const
  symm := fun _ v w => by rw [gM_apply, gM_apply]; ring
  T := fun _ => (1, 1)
  cont_T := continuousOn_const
  T_timelike := fun _ _ => by rw [gM_apply]; norm_num
  pos_on_perp := fun _ _ v h hv => by
    rw [gM_apply] at h ⊢
    have h2 : v.2 = -v.1 := by linarith
    have h1 : v.1 ≠ 0 := by
      intro h1; apply hv; ext
      · exact h1
      · rw [h2, h1]; simp
    rw [h2]; nlinarith [sq_pos_of_ne_zero h1]

/-- Future-causal in null coordinates: `v_U ≥ 0`, `v_V ≥ 0`, not both `0`. -/
lemma futCausal_iff (x v : P) : mink.FutCausal x v ↔ 0 ≤ v.1 ∧ 0 ≤ v.2 ∧ 0 < v.1 + v.2 := by
  show gM v v ≤ 0 ∧ gM v (1, 1) < 0 ↔ _
  rw [gM_apply, gM_apply]
  constructor
  · rintro ⟨h1, h2⟩
    have hs : 0 < v.1 + v.2 := by linarith
    have hp : 0 ≤ v.1 * v.2 := by linarith
    refine ⟨?_, ?_, hs⟩ <;> by_contra h <;> push Not at h <;> nlinarith
  · rintro ⟨h1, h2, h3⟩; constructor <;> nlinarith

/-- Future-timelike in null coordinates: `v_U > 0`, `v_V > 0`. -/
lemma futTimelike_iff (x v : P) : mink.FutTimelike x v ↔ 0 < v.1 ∧ 0 < v.2 := by
  show gM v v < 0 ∧ gM v (1, 1) < 0 ↔ _
  rw [gM_apply, gM_apply]
  constructor
  · rintro ⟨h1, h2⟩
    have hs : 0 < v.1 + v.2 := by linarith
    have hp : 0 < v.1 * v.2 := by linarith
    refine ⟨?_, ?_⟩ <;> by_contra h <;> push Not at h <;> nlinarith
  · rintro ⟨h1, h2⟩; constructor <;> nlinarith

lemma hasDerivAt_lin {γ : ℝ → P} (φ : P →L[ℝ] ℝ) {t : ℝ} (h : DifferentiableAt ℝ γ t) :
    HasDerivAt (fun t => φ (γ t)) (φ (deriv γ t)) t :=
  φ.hasFDerivAt.comp_hasDerivAt t h.hasDerivAt

lemma lin_le_of_step {γ : ℝ → P} (hγ : ContDiff ℝ 1 γ) (φ : P →L[ℝ] ℝ)
    (h : ∀ t ∈ Icc (0:ℝ) 1, 0 ≤ φ (deriv γ t)) : φ (γ 0) ≤ φ (γ 1) := by
  have hd : ∀ t, HasDerivAt (fun t => φ (γ t)) (φ (deriv γ t)) t := fun t =>
    hasDerivAt_lin φ ((hγ.differentiable one_ne_zero) t)
  have hm : MonotoneOn (fun t => φ (γ t)) (Icc (0:ℝ) 1) :=
    monotoneOn_of_deriv_nonneg (convex_Icc 0 1)
      (fun t _ => (hd t).continuousAt.continuousWithinAt)
      (fun t _ => (hd t).differentiableAt.differentiableWithinAt)
      (fun t ht => by
        rw [interior_Icc] at ht; rw [(hd t).deriv]; exact h t (Ioo_subset_Icc_self ht))
  exact hm ⟨le_rfl, zero_le_one⟩ ⟨zero_le_one, le_rfl⟩ zero_le_one

lemma lin_lt_of_step {γ : ℝ → P} (hγ : ContDiff ℝ 1 γ) (φ : P →L[ℝ] ℝ)
    (h : ∀ t ∈ Icc (0:ℝ) 1, 0 < φ (deriv γ t)) : φ (γ 0) < φ (γ 1) := by
  have hd : ∀ t, HasDerivAt (fun t => φ (γ t)) (φ (deriv γ t)) t := fun t =>
    hasDerivAt_lin φ ((hγ.differentiable one_ne_zero) t)
  have hm : StrictMonoOn (fun t => φ (γ t)) (Icc (0:ℝ) 1) :=
    strictMonoOn_of_deriv_pos (convex_Icc 0 1)
      (fun t _ => (hd t).continuousAt.continuousWithinAt)
      (fun t ht => by
        rw [interior_Icc] at ht; rw [(hd t).deriv]; exact h t (Ioo_subset_Icc_self ht))
  exact hm ⟨le_rfl, zero_le_one⟩ ⟨zero_le_one, le_rfl⟩ zero_lt_one

/-- `U` and `V` increase strictly along a timelike step. -/
lemma tstep_lt {x y : P} (h : mink.TStep x y) : x.1 < y.1 ∧ x.2 < y.2 := by
  obtain ⟨γ, hγ, h0, h1, hγt⟩ := h
  have k := fun t ht => (futTimelike_iff _ _).1 (hγt t ht).2
  subst h0 h1
  exact ⟨by simpa using lin_lt_of_step hγ (fst ℝ ℝ ℝ) (fun t ht => by simpa using (k t ht).1),
    by simpa using lin_lt_of_step hγ (snd ℝ ℝ ℝ) (fun t ht => by simpa using (k t ht).2)⟩

/-- `U` and `V` do not decrease along a causal step. -/
lemma cstep_le {x y : P} (h : mink.CStep x y) : x.1 ≤ y.1 ∧ x.2 ≤ y.2 := by
  obtain ⟨γ, hγ, h0, h1, hγt⟩ := h
  have k := fun t ht => (futCausal_iff _ _).1 (hγt t ht).2
  subst h0 h1
  exact ⟨by simpa using lin_le_of_step hγ (fst ℝ ℝ ℝ) (fun t ht => by simpa using (k t ht).1),
    by simpa using lin_le_of_step hγ (snd ℝ ℝ ℝ) (fun t ht => by simpa using (k t ht).2.1)⟩

lemma chr_lt {x y : P} (h : mink.Chr x y) : x.1 < y.1 ∧ x.2 < y.2 := by
  induction h with
  | single h => exact tstep_lt h
  | tail _ h ih => exact ⟨ih.1.trans (tstep_lt h).1, ih.2.trans (tstep_lt h).2⟩

lemma cau_le {x y : P} (h : mink.Cau x y) : x.1 ≤ y.1 ∧ x.2 ≤ y.2 := by
  induction h with
  | refl => exact ⟨le_rfl, le_rfl⟩
  | tail _ h ih => exact ⟨ih.1.trans (cstep_le h).1, ih.2.trans (cstep_le h).2⟩

/-- The straight segment is a timelike step when both null coordinates increase. -/
lemma tstep_of_lt {x y : P} (h1 : x.1 < y.1) (h2 : x.2 < y.2) : mink.TStep x y := by
  refine ⟨fun t => x + t • (y - x), contDiff_const.add (contDiff_id.smul contDiff_const),
    by simp, by simp, fun t _ => ⟨mem_univ _, ?_⟩⟩
  have hd : deriv (fun t : ℝ => x + t • (y - x)) t = y - x := by
    have h : HasDerivAt (fun t : ℝ => x + t • (y - x)) ((1:ℝ) • (y - x)) t :=
      ((hasDerivAt_id' t).smul_const (y - x)).const_add x
    rw [h.deriv, one_smul]
  rw [hd, futTimelike_iff]
  simp only [Prod.fst_sub, Prod.snd_sub, sub_pos]
  exact ⟨h1, h2⟩

/-- The Rindler worldline `O(σ) = (U, V) = (−e^{−σ}, e^{σ})`, on `U·V = −1`. -/
noncomputable def O (σ : ℝ) : P := (-Real.exp (-σ), Real.exp σ)

lemma O_UV (σ : ℝ) : (O σ).1 * (O σ).2 = -1 := by
  simp only [O, neg_mul, ← Real.exp_add, neg_add_cancel, Real.exp_zero]

/-- `O` is future-timelike: `O s ≪ O t` for `s < t`. -/
theorem hl_O_mono (s t : ℝ) (h : s < t) : mink.Chr (O s) (O t) := by
  refine Relation.TransGen.single (tstep_of_lt ?_ ?_)
  · simp only [O, neg_lt_neg_iff, Real.exp_lt_exp]; linarith
  · simp only [O, Real.exp_lt_exp]; exact h

/-- **`D = {U < 0}`.** -/
theorem hl_D_eq : mink.D (range O) = {p : P | p.1 < 0} := by
  ext p
  simp only [Spacetime.D, Spacetime.IpastSet, mem_iUnion, mem_ofPred_eq, Spacetime.Ipast,
    exists_prop]
  constructor
  · rintro ⟨_, ⟨σ, rfl⟩, h⟩
    have h1 := (chr_lt h).1
    have h2 : 0 < Real.exp (-σ) := Real.exp_pos _
    simp only [O] at h1; linarith
  · intro hp
    have e1 : ∀ᶠ σ in atTop, Real.exp (-σ) < -p.1 :=
      (tendsto_order.1 Real.tendsto_exp_neg_atTop_nhds_zero).2 _ (by linarith)
    have e2 : ∀ᶠ σ in atTop, p.2 < Real.exp σ := Real.tendsto_exp_atTop.eventually_gt_atTop p.2
    obtain ⟨σ, h1, h2⟩ := (e1.and e2).exists
    exact ⟨O σ, mem_range_self σ, Relation.TransGen.single
      (tstep_of_lt (by simp only [O]; linarith) h2)⟩

/-- `J⁻(𝒥⁺) = {U < 0}` too. -/
theorem hl_JpastSet_eq : mink.JpastSet (range O) = {p : P | p.1 < 0} := by
  apply Subset.antisymm
  · intro p hp
    simp only [Spacetime.JpastSet, mem_iUnion, Spacetime.Jpast, mem_ofPred_eq, exists_prop] at hp
    obtain ⟨_, ⟨σ, rfl⟩, h⟩ := hp
    have h1 := (cau_le h).1
    have h2 : 0 < Real.exp (-σ) := Real.exp_pos _
    show p.1 < 0
    simp only [O] at h1; linarith
  · rw [← hl_D_eq]
    intro p hp
    simp only [Spacetime.D, Spacetime.IpastSet, Spacetime.JpastSet, mem_iUnion] at hp ⊢
    obtain ⟨z, hz, h⟩ := hp
    exact ⟨z, hz, mink.hl_chr_cau h⟩

/-- **`𝓗⁺ = {U = 0}`.** -/
theorem hl_H_eq : mink.H (range O) = {p : P | p.1 = 0} := by
  have h := (IsOpenMap.preimage_frontier_eq_frontier_preimage (f := (Prod.fst : P → ℝ))
    isOpenMap_fst continuous_fst (Iio (0:ℝ))).symm
  rw [Spacetime.H, hl_JpastSet_eq]
  have e : {p : P | p.1 < 0} = Prod.fst ⁻¹' Iio 0 := rfl
  rw [e, h, frontier_Iio]
  rfl

/-! ## Temporal functions `Θ = G(−U) + V` on `D` and their future Cauchy property -/

/-- `Θ_G(U, V) = G(−U) + V`. -/
noncomputable def ThetaG (G : ℝ → ℝ) (p : P) : ℝ := G (-p.1) + p.2

/-- Conditions on the profile `G` (on `s = −U > 0`). -/
structure GoodG (G : ℝ → ℝ) : Prop where
  cdiff : ContDiffOn ℝ 1 G (Ioi 0)
  deriv_neg : ∀ s, 0 < s → deriv G s < 0
  tendsto_zero : Tendsto G (𝓝[>] 0) atTop
  tendsto_top : Tendsto G atTop atBot

/-- The derivative `dΘ_G = −G′(−U) dU + dV`. -/
noncomputable def dTh (G : ℝ → ℝ) (p : P) : P →L[ℝ] ℝ :=
  deriv G (-p.1) • (-(fst ℝ ℝ ℝ)) + snd ℝ ℝ ℝ

lemma dTh_apply (G : ℝ → ℝ) (p v : P) : dTh G p v = deriv G (-p.1) * (-v.1) + v.2 := by
  simp [dTh]

namespace GoodG
variable {G : ℝ → ℝ} (hG : GoodG G)
include hG

lemma hasDerivAt {s : ℝ} (hs : 0 < s) : HasDerivAt G (deriv G s) s :=
  ((hG.cdiff.differentiableOn one_ne_zero s hs).differentiableAt (Ioi_mem_nhds hs)).hasDerivAt

lemma hasFDerivAt {p : P} (hp : p.1 < 0) : HasFDerivAt (ThetaG G) (dTh G p) p := by
  have h1 : HasFDerivAt (fun p : P => -p.1) (-(fst ℝ ℝ ℝ)) p := hasFDerivAt_fst.neg
  have h2 := (hG.hasDerivAt (s := -p.1) (by linarith)).comp_hasFDerivAt p h1
  exact h2.add hasFDerivAt_snd

lemma fderiv_eq {p : P} (hp : p.1 < 0) : fderiv ℝ (ThetaG G) p = dTh G p :=
  (hG.hasFDerivAt hp).fderiv

lemma contDiffOn : ContDiffOn ℝ 1 (ThetaG G) {p : P | p.1 < 0} := by
  have h1 : ContDiffOn ℝ 1 (fun p : P => G (-p.1)) {p : P | p.1 < 0} :=
    hG.cdiff.comp (contDiff_fst.neg.contDiffOn) (fun p (hp : p.1 < 0) => by
      show 0 < -p.1; linarith)
  exact h1.add contDiff_snd.contDiffOn

lemma anti : StrictAntiOn G (Ioi 0) :=
  strictAntiOn_of_deriv_neg (convex_Ioi 0) hG.cdiff.continuousOn
    (fun x hx => by rw [interior_Ioi] at hx; exact hG.deriv_neg x hx)

/-- `G(s) ≤ K` forces `s ≥ δ > 0`. -/
lemma lower (K : ℝ) : ∃ δ > 0, ∀ s, 0 < s → G s ≤ K → δ ≤ s := by
  obtain ⟨u, hu, hsub⟩ :=
    (mem_nhdsGT_iff_exists_Ioo_subset).1 (hG.tendsto_zero.eventually_gt_atTop K)
  refine ⟨u, hu, fun s hs hK => le_of_not_gt fun hsu => ?_⟩
  have : K < G s := hsub ⟨hs, hsu⟩
  linarith

/-- `Θ_G` is temporal on `{U < 0}`: `dΘ_G(v) = (−G′) v_U + v_V > 0` for future-causal `v`. -/
lemma dTh_pos {p : P} (hp : p.1 < 0) {v : P} (hv : mink.FutCausal p v) : 0 < dTh G p v := by
  rw [dTh_apply]
  obtain ⟨h1, h2, h3⟩ := (futCausal_iff _ _).1 hv
  have hd := hG.deriv_neg (-p.1) (by linarith)
  rcases h1.eq_or_lt with h | h
  · rw [← h]; simp only [neg_zero, mul_zero, zero_add]; linarith
  · nlinarith

end GoodG

/-- Monotonicity of a function continuous on `[0, ∞)` with nonnegative derivative off a locally
finite set of break points. -/
lemma mono_brk {f : ℝ → ℝ} {B : Set ℝ} (hB : ∀ a b, (B ∩ Icc a b).Finite)
    (hf : ContinuousOn f (Ici 0))
    (hd : ∀ t, 0 < t → t ∉ B → DifferentiableAt ℝ f t ∧ 0 ≤ deriv f t) :
    MonotoneOn f (Ici 0) := by
  have hfin : ∀ a b, (B ∩ Ioo a b).Finite := fun a b =>
    (hB a b).subset (inter_subset_inter_right _ Ioo_subset_Icc_self)
  have base : ∀ a b, 0 ≤ a → a ≤ b → B ∩ Ioo a b = ∅ → f a ≤ f b := by
    intro a b ha hab he
    have hm : MonotoneOn f (Icc a b) := by
      refine monotoneOn_of_deriv_nonneg (convex_Icc a b)
        (hf.mono fun t ht => le_trans ha ht.1) (fun t ht => ?_) (fun t ht => ?_)
      all_goals
        rw [interior_Icc] at ht
        have htB : t ∉ B := fun h => (he ▸ (⟨h, ht⟩ : t ∈ B ∩ Ioo a b) : t ∈ (∅ : Set ℝ))
        have := hd t (by linarith [ht.1]) htB
      · exact this.1.differentiableWithinAt
      · exact this.2
    exact hm ⟨le_rfl, hab⟩ ⟨hab, le_rfl⟩ hab
  have key : ∀ n : ℕ, ∀ a b, 0 ≤ a → a ≤ b → (B ∩ Ioo a b).ncard ≤ n → f a ≤ f b := by
    intro n
    induction n with
    | zero =>
      intro a b ha hab hn
      exact base a b ha hab ((Set.ncard_eq_zero (hfin a b)).1 (Nat.le_zero.1 hn))
    | succ n ih =>
      intro a b ha hab hn
      by_cases he : B ∩ Ioo a b = ∅
      · exact base a b ha hab he
      obtain ⟨c, hcB, hc⟩ := nonempty_iff_ne_empty.2 he
      have h1 : (B ∩ Ioo a c).ncard ≤ n := by
        have : B ∩ Ioo a c ⊂ B ∩ Ioo a b :=
          (ssubset_iff_of_subset (inter_subset_inter_right _
            (Ioo_subset_Ioo_right hc.2.le))).2 ⟨c, ⟨hcB, hc⟩, fun h => lt_irrefl c h.2.2⟩
        have := Set.ncard_lt_ncard this (hfin a b)
        omega
      have h2 : (B ∩ Ioo c b).ncard ≤ n := by
        have : B ∩ Ioo c b ⊂ B ∩ Ioo a b :=
          (ssubset_iff_of_subset (inter_subset_inter_right _
            (Ioo_subset_Ioo_left hc.1.le))).2 ⟨c, ⟨hcB, hc⟩, fun h => lt_irrefl c h.2.1⟩
        have := Set.ncard_lt_ncard this (hfin a b)
        omega
      exact (ih a c ha hc.1.le h1).trans (ih c b (ha.trans hc.1.le) hc.2.le h2)
  intro a ha b hb hab
  exact key _ a b ha hab le_rfl

/-- **Future Cauchy property in the model.** For a good profile `G`, `Θ_G = G(−U) + V` is
`FutCauchyTemporal` on `D` (with the repaired `IsTemporal`). Along a future-inextendible causal
curve in `D`, `U` and `V` are nondecreasing; if `Θ` stayed below `a`, then `V` and `U` would be
bounded (`U ≤ −δ` by the blow-up of `G` at `0⁺`), so the curve would converge to a point with
`U < 0`, i.e. in `D`, contradicting inextendibility; so some `Θ(γ T) ≥ a`, and the IVT. -/
theorem hl_futCauchy {G : ℝ → ℝ} (hG : GoodG G) :
    (mink.Dsp (range O)).FutCauchyTemporal (ThetaG G) := by
  have hM : (mink.Dsp (range O)).M = {p : P | p.1 < 0} := hl_D_eq
  refine ⟨⟨hM ▸ hG.contDiffOn, fun x hx v hv => ?_⟩, fun c a ha => ?_⟩
  · rw [hM] at hx
    rw [hG.fderiv_eq hx]
    exact hG.dTh_pos hx hv
  have hmem : ∀ t, 0 ≤ t → (c.γ t).1 < 0 := fun t ht => by
    have := c.mem t ht; rw [hM] at this; exact this
  have hcaus : ∀ t, 0 < t → t ∉ c.brk →
      DifferentiableAt ℝ c.γ t ∧ 0 ≤ (deriv c.γ t).1 ∧ 0 ≤ (deriv c.γ t).2 := by
    intro t ht hb
    obtain ⟨hd, hc⟩ := c.causal t ht hb
    obtain ⟨h1, h2, -⟩ := (futCausal_iff (c.γ t) _).1 hc
    exact ⟨hd, h1, h2⟩
  have hU : MonotoneOn (fun t => (c.γ t).1) (Ici 0) := by
    refine mono_brk c.brk_fin (continuous_fst.comp_continuousOn c.cont) fun t ht hb => ?_
    obtain ⟨hd, h1, -⟩ := hcaus t ht hb
    have h := hasDerivAt_lin (fst ℝ ℝ ℝ) hd
    refine ⟨h.differentiableAt, ?_⟩
    change 0 ≤ deriv (fun t => (fst ℝ ℝ ℝ) (c.γ t)) t
    rw [h.deriv]; simpa using h1
  have hV : MonotoneOn (fun t => (c.γ t).2) (Ici 0) := by
    refine mono_brk c.brk_fin (continuous_snd.comp_continuousOn c.cont) fun t ht hb => ?_
    obtain ⟨hd, -, h2⟩ := hcaus t ht hb
    have h := hasDerivAt_lin (snd ℝ ℝ ℝ) hd
    refine ⟨h.differentiableAt, ?_⟩
    change 0 ≤ deriv (fun t => (snd ℝ ℝ ℝ) (c.γ t)) t
    rw [h.deriv]; simpa using h2
  have hcont : ContinuousOn (fun t => ThetaG G (c.γ t)) (Ici 0) :=
    hG.contDiffOn.continuousOn.comp c.cont (fun t ht => hmem t ht)
  suffices h : ∃ T, 0 ≤ T ∧ a ≤ ThetaG G (c.γ T) by
    obtain ⟨T, hT, haT⟩ := h
    obtain ⟨t, ht, hta⟩ := intermediate_value_Icc hT (hcont.mono Icc_subset_Ici_self) ⟨ha, haT⟩
    exact ⟨t, ht.1, hta⟩
  by_contra hno
  push Not at hno
  have h0 : (0:ℝ) ∈ Ici (0:ℝ) := mem_Ici.2 le_rfl
  obtain ⟨δ, hδ, hδs⟩ := hG.lower (a - (c.γ 0).2)
  have hUle : ∀ t, 0 ≤ t → (c.γ t).1 ≤ -δ := by
    intro t ht
    have h1 := hno t ht
    have h2 : (c.γ 0).2 ≤ (c.γ t).2 := hV h0 ht ht
    unfold ThetaG at h1
    have := hδs (-(c.γ t).1) (by linarith [hmem t ht]) (by linarith)
    linarith
  have hVle : ∀ t, 0 ≤ t → (c.γ t).2 ≤ a - G (-(c.γ 0).1) := by
    intro t ht
    have h1 := hno t ht
    have hU0 : (c.γ 0).1 ≤ (c.γ t).1 := hU h0 ht ht
    have hanti : G (-(c.γ 0).1) ≤ G (-(c.γ t).1) := by
      rcases hU0.eq_or_lt with h | h
      · rw [h]
      · exact (hG.anti (show (0:ℝ) < -(c.γ t).1 by linarith [hmem t ht])
          (show (0:ℝ) < -(c.γ 0).1 by linarith [hmem 0 le_rfl]) (by linarith)).le
    unfold ThetaG at h1
    linarith
  set u : ℝ → ℝ := fun t => (c.γ (max t 0)).1 with hu
  set w : ℝ → ℝ := fun t => (c.γ (max t 0)).2 with hw
  have hum : Monotone u := fun x y hxy =>
    hU (le_max_right x 0) (le_max_right y 0) (max_le_max hxy le_rfl)
  have hwm : Monotone w := fun x y hxy =>
    hV (le_max_right x 0) (le_max_right y 0) (max_le_max hxy le_rfl)
  have hub : BddAbove (range u) :=
    ⟨-δ, by rintro _ ⟨t, rfl⟩; exact hUle _ (le_max_right _ _)⟩
  have hwb : BddAbove (range w) :=
    ⟨a - G (-(c.γ 0).1), by rintro _ ⟨t, rfl⟩; exact hVle _ (le_max_right _ _)⟩
  have hlim : Tendsto c.γ atTop (𝓝 ((⨆ t, u t), (⨆ t, w t))) := by
    have h := (tendsto_atTop_ciSup hum hub).prodMk_nhds (tendsto_atTop_ciSup hwm hwb)
    refine h.congr' ?_
    filter_upwards [eventually_ge_atTop 0] with t ht
    simp [u, w, max_eq_left ht]
  apply c.inext_future
  refine ⟨_, ?_, hlim⟩
  rw [hM]
  show (⨆ t, u t) < 0
  exact lt_of_le_of_lt (ciSup_le fun t => hUle _ (le_max_right _ _)) (by linarith)

/-! ### Adaptation: reparametrise `O` so that `Θ(O' τ) = τ` -/

/-- `φ(σ) = Θ_G(O σ) = G(e^{−σ}) + e^{σ}`. -/
noncomputable def phiG (G : ℝ → ℝ) (σ : ℝ) : ℝ := ThetaG G (O σ)

lemma phiG_eq (G : ℝ → ℝ) (σ : ℝ) : phiG G σ = G (Real.exp (-σ)) + Real.exp σ := by
  simp [phiG, ThetaG, O]

namespace GoodG
variable {G : ℝ → ℝ} (hG : GoodG G)
include hG

lemma phiG_strictMono : StrictMono (phiG G) := by
  intro s t hst
  rw [phiG_eq, phiG_eq]
  have h1 : Real.exp (-t) < Real.exp (-s) := Real.exp_lt_exp.2 (by linarith)
  have h2 := hG.anti (Real.exp_pos (-t)) (Real.exp_pos (-s)) h1
  have h3 : Real.exp s < Real.exp t := Real.exp_lt_exp.2 hst
  linarith

lemma phiG_surjective : Function.Surjective (phiG G) := by
  have he : (phiG G) = fun σ => G (Real.exp (-σ)) + Real.exp σ := funext (phiG_eq G)
  rw [he]
  refine Continuous.surjective ?_ ?_ ?_
  · exact (hG.cdiff.continuousOn.comp_continuous (Real.continuous_exp.comp continuous_neg)
      (fun σ => Real.exp_pos _)).add Real.continuous_exp
  · have hexp0 : Tendsto (fun σ => Real.exp (-σ)) atTop (𝓝[>] 0) :=
      tendsto_nhdsWithin_iff.2 ⟨Real.tendsto_exp_neg_atTop_nhds_zero,
        Eventually.of_forall fun _ => Real.exp_pos _⟩
    exact (hG.tendsto_zero.comp hexp0).atTop_add_atTop Real.tendsto_exp_atTop
  · exact (hG.tendsto_top.comp (Real.tendsto_exp_atTop.comp tendsto_neg_atBot_atTop)).atBot_add
      Real.tendsto_exp_atBot

/-- **Adaptation.** A reparametrisation `O'` of the Rindler worldline, with the same range, still
future-timelike, along which `Θ_G(O' τ) = τ`. -/
theorem hl_adapted : ∃ O' : ℝ → P, range O' = range O ∧
    mink.IpastSet (range O') = mink.D (range O) ∧
    (∀ s t : ℝ, s < t → mink.Chr (O' s) (O' t)) ∧ ∀ τ, ThetaG G (O' τ) = τ + 0 := by
  have hs := hG.phiG_surjective
  have hm := hG.phiG_strictMono
  set ψ := Function.surjInv hs
  have hψ : ∀ τ, phiG G (ψ τ) = τ := Function.surjInv_eq hs
  have hrange : range (fun τ => O (ψ τ)) = range O := by
    apply Subset.antisymm
    · rintro _ ⟨τ, rfl⟩; exact mem_range_self _
    · rintro _ ⟨σ, rfl⟩
      exact ⟨phiG G σ, by show O (ψ (phiG G σ)) = O σ; rw [hm.injective (hψ (phiG G σ))]⟩
  refine ⟨fun τ => O (ψ τ), hrange, by rw [hrange]; rfl, fun s t hst => hl_O_mono _ _ ?_,
    fun τ => by rw [add_zero]; exact hψ τ⟩
  rw [← hm.lt_iff_lt, hψ, hψ]; exact hst

end GoodG

/-! ## The aligned `Θ₀ = −log(−U) + V` and the failing `Θ = F(−U) + V` -/

/-- `G₀(s) = −log s`. -/
lemma goodG_log : GoodG fun s => -Real.log s where
  cdiff := Real.contDiffOn_log.neg.mono fun s (hs : 0 < s) => by simpa using hs.ne'
  deriv_neg s hs := by
    have h : HasDerivAt (fun s => -Real.log s) (-s⁻¹) s := (Real.hasDerivAt_log hs.ne').neg
    rw [h.deriv]
    simpa using hs
  tendsto_zero := tendsto_neg_atBot_atTop.comp Real.tendsto_log_nhdsGT_zero
  tendsto_top := tendsto_neg_atTop_atBot.comp Real.tendsto_log_atTop

/-- The failing profile `F(s) = −log s − sin(log s) − s`. -/
noncomputable def Ffail (s : ℝ) : ℝ := -Real.log s - Real.sin (Real.log s) - s

lemma Ffail_hasDerivAt {s : ℝ} (hs : 0 < s) :
    HasDerivAt Ffail (-s⁻¹ - Real.cos (Real.log s) * s⁻¹ - 1) s := by
  have hl := Real.hasDerivAt_log hs.ne'
  exact (hl.neg.sub ((Real.hasDerivAt_sin (Real.log s)).comp s hl)).sub (hasDerivAt_id s)

lemma goodG_Ffail : GoodG Ffail where
  cdiff := fun s (hs : 0 < s) => by
    have hl := Real.contDiffAt_log (n := 1).2 hs.ne'
    exact ((hl.neg.sub (Real.contDiff_sin.contDiffAt.comp s hl)).sub
      contDiffAt_id).contDiffWithinAt
  deriv_neg s hs := by
    rw [(Ffail_hasDerivAt hs).deriv]
    have hi := inv_pos.2 hs
    nlinarith [Real.neg_one_le_cos (Real.log s)]
  tendsto_zero := by
    have h1 : Tendsto (fun s => -Real.log s + -2) (𝓝[>] 0) atTop :=
      tendsto_atTop_add_const_right _ (-2)
        (tendsto_neg_atBot_atTop.comp Real.tendsto_log_nhdsGT_zero)
    refine tendsto_atTop_mono' _ ?_ h1
    filter_upwards [Ioo_mem_nhdsGT (zero_lt_one' ℝ)] with s hs
    simp only [Ffail]
    nlinarith [Real.sin_le_one (Real.log s), hs.2]
  tendsto_top := by
    have h1 : Tendsto (fun s : ℝ => 1 + -s) atTop atBot :=
      tendsto_atBot_add_const_left _ 1 tendsto_neg_atTop_atBot
    refine tendsto_atBot_mono' _ ?_ h1
    filter_upwards [eventually_ge_atTop 1] with s hs
    simp only [Ffail]
    nlinarith [Real.neg_one_le_sin (Real.log s), Real.log_nonneg hs]

/-- The aligned slicing function `Θ₀ = −log(−U) + V`. -/
noncomputable def Θ₀ : P → ℝ := ThetaG fun s => -Real.log s
/-- The failing slicing function `Θ = F(−U) + V`. -/
noncomputable def Θf : P → ℝ := ThetaG Ffail

/-! ## Campaign 81 ②: the model, two-sided -/

/-- The model's metric is constant, hence locally Lipschitz. -/
theorem hl_lipschitz : LocallyLipschitzOn mink.M mink.g :=
  (LipschitzWith.const (α := P) gM).locallyLipschitz.locallyLipschitzOn

/-- **Past Cauchy property in the model (BUILT).** For a good profile `G`, every past-inextendible
causal curve of `D` ending at `γ 0` attains every level `a ≤ Θ_G(γ 0)`. Into the past `U` and `V`
are non-increasing; if `Θ_G > a` along the whole curve, then `−U` is bounded above (`G → −∞` at `∞`)
and `V` is bounded below (`G` decreasing), so the curve converges as `t → −∞` to a point with
`U ≤ U(γ 0) < 0`, i.e. in `D`, contradicting past-inextendibility; then the IVT. -/
theorem hl_pastCauchy {G : ℝ → ℝ} (hG : GoodG G) :
    (mink.Dsp (range O)).PastCauchyTemporal (ThetaG G) := by
  have hM : (mink.Dsp (range O)).M = {p : P | p.1 < 0} := hl_D_eq
  refine ⟨(hl_futCauchy hG).1, fun c a ha => ?_⟩
  have hmem : ∀ t, t ≤ 0 → (c.γ t).1 < 0 := fun t ht => by
    have := c.mem t ht; rw [hM] at this; exact this
  have hB : ∀ a b : ℝ, ((fun s : ℝ => -s) ⁻¹' c.brk ∩ Icc a b).Finite := by
    intro a b
    refine ((c.brk_fin (-b) (-a)).preimage neg_injective.injOn).subset ?_
    rintro s ⟨hs, h1, h2⟩
    exact ⟨hs, by linarith, by linarith⟩
  -- the reflected coordinates `s ↦ −φ(γ(−s))` are nondecreasing on `[0, ∞)`
  have hrefl : ∀ φ : P →L[ℝ] ℝ, (∀ t, t < 0 → t ∉ c.brk → 0 ≤ φ (deriv c.γ t)) →
      MonotoneOn (fun s => -φ (c.γ (-s))) (Ici 0) := by
    intro φ hφ
    refine mono_brk hB ?_ fun s hs hb => ?_
    · exact (φ.continuous.comp_continuousOn (c.cont.comp continuous_neg.continuousOn
        fun s (hs : 0 ≤ s) => show -s ≤ 0 by linarith)).neg
    · obtain ⟨hd, -⟩ := c.causal (-s) (by linarith) hb
      have h1 : HasDerivAt (fun s => c.γ (-s)) ((-1 : ℝ) • deriv c.γ (-s)) s := by
        have := hd.hasDerivAt.scomp s (hasDerivAt_neg s)
        simpa [Function.comp_def] using this
      have h2 : HasDerivAt (fun s => -φ (c.γ (-s))) (-φ ((-1 : ℝ) • deriv c.γ (-s))) s :=
        (φ.hasFDerivAt.comp_hasDerivAt s h1).neg
      refine ⟨h2.differentiableAt, ?_⟩
      rw [h2.deriv, map_smul, smul_eq_mul, neg_one_mul, neg_neg]
      exact hφ _ (by linarith) hb
  have hUV : ∀ t t', t ≤ t' → t' ≤ 0 → (c.γ t).1 ≤ (c.γ t').1 ∧ (c.γ t).2 ≤ (c.γ t').2 := by
    intro t t' htt ht'
    have k : ∀ t, t < 0 → t ∉ c.brk → 0 ≤ (deriv c.γ t).1 ∧ 0 ≤ (deriv c.γ t).2 :=
      fun t ht hb => by
        obtain ⟨h1, h2, -⟩ := (futCausal_iff (c.γ t) _).1 (c.causal t ht hb).2
        exact ⟨h1, h2⟩
    have h1 := hrefl (fst ℝ ℝ ℝ) (fun t ht hb => by simpa using (k t ht hb).1)
      (show (0:ℝ) ≤ -t' by linarith) (show (0:ℝ) ≤ -t by linarith) (by linarith)
    have h2 := hrefl (snd ℝ ℝ ℝ) (fun t ht hb => by simpa using (k t ht hb).2)
      (show (0:ℝ) ≤ -t' by linarith) (show (0:ℝ) ≤ -t by linarith) (by linarith)
    simp only [neg_neg, coe_fst', coe_snd', neg_le_neg_iff] at h1 h2
    exact ⟨h1, h2⟩
  have hcont : ContinuousOn (fun t => ThetaG G (c.γ t)) (Iic 0) :=
    hG.contDiffOn.continuousOn.comp c.cont (fun t ht => hmem t ht)
  suffices h : ∃ T, T ≤ 0 ∧ ThetaG G (c.γ T) ≤ a by
    obtain ⟨T, hT, haT⟩ := h
    obtain ⟨t, ht, hta⟩ := intermediate_value_Icc hT (hcont.mono Icc_subset_Iic_self) ⟨haT, ha⟩
    exact ⟨t, ht.2, hta⟩
  by_contra hno
  push Not at hno
  obtain ⟨R, hR⟩ := eventually_atTop.1 (hG.tendsto_top.eventually_lt_atBot (a - (c.γ 0).2))
  have hUge : ∀ t, t ≤ 0 → -R ≤ (c.γ t).1 := by
    intro t ht
    by_contra h
    push Not at h
    have h1 := hno t ht
    have h2 := (hUV t 0 ht le_rfl).2
    have h3 := hR (-(c.γ t).1) (by linarith)
    unfold ThetaG at h1
    linarith
  have hVge : ∀ t, t ≤ 0 → a - G (-(c.γ 0).1) ≤ (c.γ t).2 := by
    intro t ht
    have h1 := hno t ht
    have hU0 := (hUV t 0 ht le_rfl).1
    have hanti : G (-(c.γ t).1) ≤ G (-(c.γ 0).1) := by
      rcases hU0.eq_or_lt with h | h
      · rw [h]
      · exact (hG.anti (show (0:ℝ) < -(c.γ 0).1 by linarith [hmem 0 le_rfl])
          (show (0:ℝ) < -(c.γ t).1 by linarith [hmem t ht]) (by linarith)).le
    unfold ThetaG at h1
    linarith
  set u : ℝ → ℝ := fun t => (c.γ (min t 0)).1 with hu
  set w : ℝ → ℝ := fun t => (c.γ (min t 0)).2 with hw
  have hum : Monotone u := fun x y hxy =>
    (hUV _ _ (min_le_min hxy le_rfl) (min_le_right _ _)).1
  have hwm : Monotone w := fun x y hxy =>
    (hUV _ _ (min_le_min hxy le_rfl) (min_le_right _ _)).2
  have hub : BddBelow (range u) :=
    ⟨-R, by rintro _ ⟨t, rfl⟩; exact hUge _ (min_le_right _ _)⟩
  have hwb : BddBelow (range w) :=
    ⟨a - G (-(c.γ 0).1), by rintro _ ⟨t, rfl⟩; exact hVge _ (min_le_right _ _)⟩
  have hlim : Tendsto c.γ atBot (𝓝 ((⨅ t, u t), (⨅ t, w t))) := by
    have h := (tendsto_atBot_ciInf hum hub).prodMk_nhds (tendsto_atBot_ciInf hwm hwb)
    refine h.congr' ?_
    filter_upwards [eventually_le_atBot 0] with t ht
    simp [u, w, min_eq_left ht]
  apply c.inext_past
  refine ⟨_, ?_, hlim⟩
  rw [hM]
  show (⨅ t, u t) < 0
  refine lt_of_le_of_lt (ciInf_le hub 0) ?_
  show (c.γ (min 0 0)).1 < 0
  rw [min_self]; exact hmem 0 le_rfl

/-- **② Two-sided Cauchy in the model (BUILT)**, via `hl_cauchy_iff`: `Θ_G` is campaign 60's
`IsCauchyTemporal` on `D`, with the repaired `IsTemporal`. -/
theorem hl_cauchy {G : ℝ → ℝ} (hG : GoodG G) :
    (mink.Dsp (range O)).IsCauchyTemporal (ThetaG G) :=
  (mink.Dsp (range O)).hl_cauchy_iff.2 ⟨hl_futCauchy hG, hl_pastCauchy hG⟩

theorem hl_cauchy_Θ₀ : (mink.Dsp (range O)).IsCauchyTemporal Θ₀ := hl_cauchy goodG_log
theorem hl_cauchy_Θf : (mink.Dsp (range O)).IsCauchyTemporal Θf := hl_cauchy goodG_Ffail

end Model

/-! ## Campaign 84 c2: the manifold side

### Small `V`-side helpers -/

namespace Spacetime
variable (S : Spacetime V)

lemma ch_futCausal_smul {x u : V} {c : ℝ} (hc : 0 < c) (h : S.FutCausal x u) :
    S.FutCausal x (c • u) := by
  obtain ⟨h1, h2⟩ := h
  refine ⟨?_, ?_⟩
  · simp only [map_smul, FunLike.coe_smul, Pi.smul_apply, smul_eq_mul]
    nlinarith [mul_pos hc hc]
  · simp only [map_smul, FunLike.coe_smul, Pi.smul_apply, smul_eq_mul]
    nlinarith

lemma ch_tstep_mem {x y : V} (h : S.TStep x y) : x ∈ S.M ∧ y ∈ S.M := by
  obtain ⟨γ, -, h0, h1, hγ⟩ := h
  exact ⟨h0 ▸ (hγ 0 ⟨le_rfl, zero_le_one⟩).1, h1 ▸ (hγ 1 ⟨zero_le_one, le_rfl⟩).1⟩

lemma ch_cstep_mem {x y : V} (h : S.CStep x y) : x ∈ S.M ∧ y ∈ S.M := by
  obtain ⟨γ, -, h0, h1, hγ⟩ := h
  exact ⟨h0 ▸ (hγ 0 ⟨le_rfl, zero_le_one⟩).1, h1 ▸ (hγ 1 ⟨zero_le_one, le_rfl⟩).1⟩

end Spacetime

/-! ### The squash reparametrisation -/

/-- An open interval around `[0,1]` inside an open `U ⊇ [0,1]`. -/
lemma ch_exists_Ioo {U : Set ℝ} (hU : IsOpen U) (h : Icc (0:ℝ) 1 ⊆ U) :
    ∃ δ > 0, Ioo (-δ) (1 + δ) ⊆ U := by
  obtain ⟨δ, hδ, hsub⟩ := isCompact_Icc.exists_thickening_subset_open hU h
  refine ⟨δ, hδ, fun t ht => hsub ?_⟩
  rw [Metric.mem_thickening_iff]
  refine ⟨max 0 (min t 1), ⟨le_max_left _ _, max_le zero_le_one (min_le_right _ _)⟩, ?_⟩
  rw [Real.dist_eq, abs_lt]
  rcases le_total t 1 with h | h
  · rw [min_eq_left h]
    rcases le_total 0 t with h' | h'
    · rw [max_eq_right h']; constructor <;> linarith
    · rw [max_eq_left h']; constructor <;> linarith [ht.1]
  · rw [min_eq_right h, max_eq_right zero_le_one]; constructor <;> linarith [ht.2]

/-- **The squash.** For `δ > 0`, a smooth `σ : ℝ → (-δ, 1+δ)` with `σ 0 = 0`, `σ 1 = 1`, `σ' > 0`:
`σ t = 1/2 + ((1+δ)/Real.pi) arctan (b (2t − 1))`, `b = tan (Real.pi / (2(1+δ)))`. -/
lemma ch_squash {δ : ℝ} (hδ : 0 < δ) : ∃ σ : ℝ → ℝ, ContDiff ℝ 1 σ ∧ σ 0 = 0 ∧ σ 1 = 1 ∧
    (∀ t, σ t ∈ Ioo (-δ) (1 + δ)) ∧ (∀ t, HasDerivAt σ (deriv σ t) t ∧ 0 < deriv σ t) ∧
    ∀ t ∈ Icc (0:ℝ) 1, σ t ∈ Icc (0:ℝ) 1 := by
  set a : ℝ := Real.pi / (2 * (1 + δ)) with ha
  have ha0 : 0 < a := by positivity
  have ha1 : a < Real.pi / 2 := by
    rw [ha, div_lt_div_iff₀ (by positivity) (by norm_num)]; nlinarith [Real.pi_pos]
  set b := Real.tan a with hb
  have hb0 : 0 < b := Real.tan_pos_of_pos_of_lt_pi_div_two ha0 ha1
  have hab : Real.arctan b = a := Real.arctan_tan (by linarith) ha1
  set k : ℝ := (1 + δ) / Real.pi with hk
  have hk0 : 0 < k := by positivity
  have hka : k * a = 1 / 2 := by
    rw [hk, ha]; field_simp
  set σ : ℝ → ℝ := fun t => 1 / 2 + k * Real.arctan (b * (2 * t - 1)) with hσ
  have hd : ∀ t, HasDerivAt σ (k * (1 / (1 + (b * (2 * t - 1)) ^ 2) * (b * 2))) t := by
    intro t
    have h1 : HasDerivAt (fun t : ℝ => b * (2 * t - 1)) (b * 2) t := by
      simpa using (((hasDerivAt_id t).const_mul 2).sub_const 1).const_mul b
    exact ((Real.hasDerivAt_arctan _).comp t h1).const_mul k |>.const_add (1 / 2)
  have hdpos : ∀ t, 0 < k * (1 / (1 + (b * (2 * t - 1)) ^ 2) * (b * 2)) := fun t => by positivity
  have hmono : StrictMono σ := strictMono_of_deriv_pos fun t => by
    rw [(hd t).deriv]; exact hdpos t
  have h0 : σ 0 = 0 := by
    simp only [hσ]; rw [show b * (2 * 0 - 1) = -b by ring, Real.arctan_neg, hab]; linarith
  have h1 : σ 1 = 1 := by
    simp only [hσ]; rw [show b * (2 * 1 - 1) = b by ring, hab]; linarith
  refine ⟨σ, ?_, h0, h1, fun t => ?_, fun t => ⟨(hd t).deriv ▸ hd t, (hd t).deriv ▸ hdpos t⟩,
    fun t ht => ⟨h0 ▸ hmono.monotone ht.1, h1 ▸ hmono.monotone ht.2⟩⟩
  · exact contDiff_const.add (contDiff_const.mul (Real.contDiff_arctan.comp
      (contDiff_const.mul ((contDiff_const.mul contDiff_id).sub contDiff_const))))
  · have l1 := Real.arctan_lt_pi_div_two (b * (2 * t - 1))
    have l2 := Real.neg_pi_div_two_lt_arctan (b * (2 * t - 1))
    have e : k * (Real.pi / 2) = (1 + δ) / 2 := by rw [hk]; field_simp
    have u1 : k * Real.arctan (b * (2 * t - 1)) < (1 + δ) / 2 := by
      rw [← e]; exact mul_lt_mul_of_pos_left l1 hk0
    have u2 : -((1 + δ) / 2) < k * Real.arctan (b * (2 * t - 1)) := by
      rw [← e, ← mul_neg]; exact mul_lt_mul_of_pos_left l2 hk0
    simp only [hσ]
    constructor <;> linarith

/-! ### Copied from campaign 68 (`probes/LieDerivManifold.lean`): chart representatives -/

/-! ## Copied (campaign 80, `TangencyCondition.lean`, sections ① frame-free and normed, names `tc_…`
kept, inside namespace `TCF`): the null-frame inequality and its filter corollary. -/

namespace TCF

/-! ## ① Frame-free: the pointwise inequality (pure linear algebra, no basis, no dimension) -/

section FrameFree

variable {E : Type*} [AddCommGroup E] [Module ℝ E]

/-- A null frame `ℓ, n` for a symmetric bilinear `g`: `g(ℓ,ℓ) = g(n,n) = 0`, `g(ℓ,n) = −1`, and `g`
positive **semi**definite on `W = {ℓ,n}^⊥` (weaker than the registered "positive definite"). -/
structure NullFrame (g : LinearMap.BilinForm ℝ E) (ℓ n : E) : Prop where
  symm : ∀ v w, g v w = g w v
  ll : g ℓ ℓ = 0
  nn : g n n = 0
  ln : g ℓ n = -1
  posW : ∀ e, g ℓ e = 0 → g n e = 0 → 0 ≤ g e e

/-- Future causal: `g(v,v) ≤ 0` and `g(v, ℓ+n) < 0` (`ℓ + n` is future timelike, `g = −2`). Such `v`
are automatically nonzero. `tc_futCausal_iff` shows this is exactly the cone
`{αℓ + βn + e | α, β ≥ 0, e ∈ W, g(e,e) ≤ 2αβ, (α,β) ≠ 0}`. -/
def FutCausal (g : LinearMap.BilinForm ℝ E) (ℓ n v : E) : Prop := g v v ≤ 0 ∧ g v (ℓ + n) < 0

/-- The `g`-orthogonal projection onto `W`: `w_W = w + g(n,w) ℓ + g(ℓ,w) n`. -/
def projW (g : LinearMap.BilinForm ℝ E) (ℓ n w : E) : E := w + g n w • ℓ + g ℓ w • n

/-- The splitting `w = (−g(n,w)) ℓ + (−g(ℓ,w)) n + w_W`. -/
lemma decompW (g : LinearMap.BilinForm ℝ E) (ℓ n w : E) :
    w = (-g n w) • ℓ + (-g ℓ w) • n + projW g ℓ n w := by
  simp only [projW, neg_smul]; abel

variable {g : LinearMap.BilinForm ℝ E} {ℓ n : E}

namespace NullFrame
variable (hF : NullFrame g ℓ n)
include hF

lemma nl : g n ℓ = -1 := by rw [hF.symm]; exact hF.ln

lemma projW_l (w : E) : g ℓ (projW g ℓ n w) = 0 := by
  simp [projW, hF.ll, hF.ln]

lemma projW_n (w : E) : g n (projW g ℓ n w) = 0 := by
  simp [projW, hF.nn, hF.nl]


/-- `g(αℓ + βn + e, αℓ + βn + e) = −2αβ + g(e,e)` for `e ∈ W`. -/
lemma quad (α β : ℝ) {e : E} (he1 : g ℓ e = 0) (he2 : g n e = 0) :
    g (α • ℓ + β • n + e) (α • ℓ + β • n + e) = -2 * α * β + g e e := by
  have h1 : g e ℓ = 0 := by rw [hF.symm]; exact he1
  have h2 : g e n = 0 := by rw [hF.symm]; exact he2
  simp [hF.ll, hF.nn, hF.ln, hF.nl, he1, he2, h1, h2]; ring

/-- `g(αℓ + βn + e, ℓ + n) = −α − β` for `e ∈ W`. -/
lemma lin (α β : ℝ) {e : E} (he1 : g ℓ e = 0) (he2 : g n e = 0) :
    g (α • ℓ + β • n + e) (ℓ + n) = -α - β := by
  have h1 : g e ℓ = 0 := by rw [hF.symm]; exact he1
  have h2 : g e n = 0 := by rw [hF.symm]; exact he2
  simp [hF.ll, hF.nn, hF.ln, hF.nl, h1, h2]; ring

end NullFrame

/-- The future causal cone, made explicit in the splitting `ℓ, n, W`. -/
theorem tc_futCausal_iff (hF : NullFrame g ℓ n) (v : E) :
    FutCausal g ℓ n v ↔ ∃ α β : ℝ, ∃ e : E, 0 ≤ α ∧ 0 ≤ β ∧ g ℓ e = 0 ∧ g n e = 0 ∧
      g e e ≤ 2 * α * β ∧ (α ≠ 0 ∨ β ≠ 0) ∧ v = α • ℓ + β • n + e := by
  constructor
  · rintro ⟨h1, h2⟩
    have hd := decompW g ℓ n v
    set α := -g n v
    set β := -g ℓ v
    set e := projW g ℓ n v
    have he1 := hF.projW_l v
    have he2 := hF.projW_n v
    have hq := hF.quad α β he1 he2
    have hl := hF.lin α β he1 he2
    rw [← hd] at hq hl
    have hW := hF.posW e he1 he2
    have hs : 0 < α + β := by linarith
    have hab : 0 ≤ α * β := by linarith
    have hα : 0 ≤ α := by
      by_contra h; push Not at h; nlinarith
    have hβ : 0 ≤ β := by
      by_contra h; push Not at h; nlinarith
    refine ⟨α, β, e, hα, hβ, he1, he2, by linarith, ?_, hd⟩
    by_contra h; push Not at h; rw [h.1, h.2] at hs; simp at hs
  · rintro ⟨α, β, e, hα, hβ, he1, he2, hq, hne, rfl⟩
    refine ⟨by rw [hF.quad α β he1 he2]; linarith, ?_⟩
    rw [hF.lin α β he1 he2]
    rcases hne with h | h
    · have := lt_of_le_of_ne hα (Ne.symm h); linarith
    · have := lt_of_le_of_ne hβ (Ne.symm h); linarith

variable {ξ : E →ₗ[ℝ] ℝ}

/-- Temporality forces `ξ(ℓ) > 0` and `ξ(n) > 0`. -/
theorem tc_pos (hF : NullFrame g ℓ n) (hξ : ∀ v, FutCausal g ℓ n v → 0 < ξ v) :
    0 < ξ ℓ ∧ 0 < ξ n := by
  refine ⟨hξ ℓ ⟨by rw [hF.ll], ?_⟩, hξ n ⟨by rw [hF.nn], ?_⟩⟩
  · simp [hF.ll, hF.ln]
  · simp [hF.nn, hF.nl]

/-- **The basis-free form of campaign 79's `st_null_frame_bound`**: for `e ∈ W`,
`ξ(e)² ≤ 2 ξ(ℓ) ξ(n) g(e,e)`. Proof: test `ξ` on the null vector `αℓ + βn ∓ e` with
`β = |ξ e|/(2ξ(n))`, `α = g(e,e) ξ(n)/|ξ e|`. -/
theorem tc_W_bound (hF : NullFrame g ℓ n) (hξ : ∀ v, FutCausal g ℓ n v → 0 < ξ v) {e : E}
    (he1 : g ℓ e = 0) (he2 : g n e = 0) : ξ e ^ 2 ≤ 2 * ξ ℓ * ξ n * g e e := by
  obtain ⟨ha, hb⟩ := tc_pos hF hξ
  have hq := hF.posW e he1 he2
  set a := ξ ℓ
  set b := ξ n
  set q := g e e
  have key : ∀ s : ℝ, s * s = 1 → 0 < s * ξ e → (s * ξ e) ^ 2 < 2 * a * b * q := by
    intro s hs hc
    set c := s * ξ e
    have hse1 : g ℓ ((-s) • e) = 0 := by simp [he1]
    have hse2 : g n ((-s) • e) = 0 := by simp [he2]
    have hqs : g ((-s) • e) ((-s) • e) = q := by simp [q]; nlinarith
    set β := c / (2 * b)
    set α := q * b / c
    have hβ : 0 < β := by positivity
    have hα : 0 ≤ α := by positivity
    have hv : FutCausal g ℓ n (α • ℓ + β • n + (-s) • e) := by
      refine ⟨?_, ?_⟩
      · rw [hF.quad α β hse1 hse2, hqs]
        have : α * β = q / 2 := by simp only [α, β]; field_simp
        linarith
      · rw [hF.lin α β hse1 hse2]; linarith
    have hp := hξ _ hv
    simp only [map_add, map_smul, smul_eq_mul] at hp
    have : -s * ξ e = -c := by simp [c]
    rw [this] at hp
    have e1 : α * a = q * a * b / c := by simp only [α]; ring
    have e2 : β * b = c / 2 := by simp only [β]; field_simp
    rw [e1, e2] at hp
    have : c / 2 < q * a * b / c := by linarith
    rw [lt_div_iff₀ hc] at this
    nlinarith
  rcases lt_trichotomy (ξ e) 0 with h | h | h
  · have := key (-1) (by norm_num) (by linarith); nlinarith
  · rw [h]; have := mul_nonneg (mul_pos (mul_pos two_pos ha) hb).le hq; nlinarith
  · have := key 1 (by norm_num) (by linarith); nlinarith

/-- **① The pointwise, basis-free inequality.** For every `w`,
`|ξ(w) − ξ(n)·(−g(ℓ,w))| ≤ ξ(ℓ)·|g(n,w)| + √(2 ξ(ℓ) ξ(n))·√(g(w_W, w_W))`,
`w_W = w + g(n,w) ℓ + g(ℓ,w) n`. -/
theorem tc_pointwise (hF : NullFrame g ℓ n) (hξ : ∀ v, FutCausal g ℓ n v → 0 < ξ v) (w : E) :
    |ξ w - ξ n * (-g ℓ w)| ≤
      ξ ℓ * |g n w| + Real.sqrt (2 * ξ ℓ * ξ n) * Real.sqrt (g (projW g ℓ n w) (projW g ℓ n w)) := by
  obtain ⟨ha, hb⟩ := tc_pos hF hξ
  have he1 := hF.projW_l w
  have he2 := hF.projW_n w
  have hB := tc_W_bound hF hξ he1 he2
  have hxi : ξ w = (-g n w) * ξ ℓ + (-g ℓ w) * ξ n + ξ (projW g ℓ n w) := by
    conv_lhs => rw [decompW g ℓ n w]
    simp
  have habs : |ξ (projW g ℓ n w)| ≤
      Real.sqrt (2 * ξ ℓ * ξ n) * Real.sqrt (g (projW g ℓ n w) (projW g ℓ n w)) := by
    rw [← Real.sqrt_mul (by positivity)]; exact Real.abs_le_sqrt hB
  have : ξ w - ξ n * (-g ℓ w) = -(ξ ℓ * g n w) + ξ (projW g ℓ n w) := by rw [hxi]; ring
  rw [this]
  calc |-(ξ ℓ * g n w) + ξ (projW g ℓ n w)| ≤ |-(ξ ℓ * g n w)| + |ξ (projW g ℓ n w)| :=
        abs_add_le _ _
    _ ≤ _ := by rw [abs_neg, abs_mul, abs_of_pos ha]; linarith

end FrameFree

/-! ## ① The operator-norm bound and the corollary (normed setting, frames and metrics may move) -/

section Normed

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]

/-- A continuous bilinear form as a `LinearMap.BilinForm`. -/
noncomputable def bil (g : E →L[ℝ] E →L[ℝ] ℝ) : LinearMap.BilinForm ℝ E :=
  LinearMap.mk₂ ℝ (fun v w => g v w) (by simp) (by simp) (by simp) (by simp)

@[simp] lemma bil_apply (g : E →L[ℝ] E →L[ℝ] ℝ) (v w : E) : bil g v w = g v w := rfl

/-- The frame hypotheses at one point: `(ℓ, n)` is a null frame for `g` and `ξ` is positive on the
future causal cone. -/
def FrameHyp (g : E →L[ℝ] E →L[ℝ] ℝ) (ℓ n : E) (ξ : E →L[ℝ] ℝ) : Prop :=
  NullFrame (bil g) ℓ n ∧ ∀ v, FutCausal (bil g) ℓ n v → 0 < ξ v

/-- **① in operator norm.** Under the frame hypotheses,
`‖ξ/ξ(n) + g(ℓ,·)‖ ≤ (ξℓ/ξn)·‖g‖‖n‖ + √(2 ξℓ/ξn)·√‖g‖·(1 + 2‖g‖‖n‖‖ℓ‖)`. -/
theorem tc_opNorm_bound {g : E →L[ℝ] E →L[ℝ] ℝ} {ℓ n : E} {ξ : E →L[ℝ] ℝ}
    (h : FrameHyp g ℓ n ξ) :
    ‖(ξ n)⁻¹ • ξ + g ℓ‖ ≤ ξ ℓ / ξ n * (‖g‖ * ‖n‖) +
      Real.sqrt (2 * (ξ ℓ / ξ n)) * (Real.sqrt ‖g‖ * (1 + 2 * (‖g‖ * ‖n‖) * ‖ℓ‖)) := by
  obtain ⟨hF, hξ⟩ := h
  have hξ' : ∀ v, FutCausal (bil g) ℓ n v → 0 < (ξ : E →ₗ[ℝ] ℝ) v := hξ
  obtain ⟨ha, hb⟩ := tc_pos hF hξ'
  set a := ξ ℓ
  set b := ξ n
  have ha' : 0 < a := ha
  have hb' : 0 < b := hb
  have hr : 0 ≤ a / b := by positivity
  refine ContinuousLinearMap.opNorm_le_bound _ (by positivity) fun w => ?_
  have hP := tc_pointwise hF hξ' w
  simp only [bil_apply, ContinuousLinearMap.coe_coe] at hP
  set e := projW (bil g) ℓ n w
  -- the size of `w_W`
  have hgn : |g n w| ≤ ‖g‖ * ‖n‖ * ‖w‖ := by
    rw [← Real.norm_eq_abs]; exact g.le_opNorm₂ n w
  have hgl : |g ℓ w| ≤ ‖g‖ * ‖ℓ‖ * ‖w‖ := by
    rw [← Real.norm_eq_abs]; exact g.le_opNorm₂ ℓ w
  have he : ‖e‖ ≤ (1 + 2 * (‖g‖ * ‖n‖) * ‖ℓ‖) * ‖w‖ := by
    have : ‖e‖ ≤ ‖w‖ + |g n w| * ‖ℓ‖ + |g ℓ w| * ‖n‖ := by
      simp only [e, projW, bil_apply]
      refine (norm_add₃_le).trans ?_
      rw [norm_smul, norm_smul, Real.norm_eq_abs, Real.norm_eq_abs]
    have h1 := mul_le_mul_of_nonneg_right hgn (norm_nonneg ℓ)
    have h2 := mul_le_mul_of_nonneg_right hgl (norm_nonneg n)
    nlinarith [norm_nonneg w, norm_nonneg g, norm_nonneg ℓ, norm_nonneg n]
  have hq : Real.sqrt (g e e) ≤ Real.sqrt ‖g‖ * ‖e‖ := by
    have : g e e ≤ ‖g‖ * ‖e‖ ^ 2 := by
      have := g.le_opNorm₂ e e
      rw [Real.norm_eq_abs] at this
      nlinarith [le_abs_self (g e e)]
    calc Real.sqrt (g e e) ≤ Real.sqrt (‖g‖ * ‖e‖ ^ 2) := Real.sqrt_le_sqrt this
      _ = Real.sqrt ‖g‖ * ‖e‖ := by
        rw [Real.sqrt_mul (norm_nonneg g), Real.sqrt_sq (norm_nonneg e)]
  have hsq : Real.sqrt (2 * a * b) = Real.sqrt (2 * (a / b)) * b := by
    have : 2 * a * b = 2 * (a / b) * b ^ 2 := by field_simp
    rw [this, Real.sqrt_mul (by positivity), Real.sqrt_sq hb'.le]
  -- assemble
  have hval : ((b)⁻¹ • ξ + g ℓ) w = (ξ w - b * (-g ℓ w)) / b := by
    simp only [FunLike.coe_add, FunLike.coe_smul, Pi.add_apply,
      Pi.smul_apply, smul_eq_mul]
    have hbb : b⁻¹ * b = 1 := inv_mul_cancel₀ hb'.ne'
    rw [eq_div_iff hb'.ne']
    linear_combination (ξ w) * hbb
  rw [hval, Real.norm_eq_abs, abs_div, abs_of_pos hb', div_le_iff₀ hb']
  rw [hsq] at hP
  have hs0 : 0 ≤ Real.sqrt (2 * (a / b)) := Real.sqrt_nonneg _
  have hsg : 0 ≤ Real.sqrt ‖g‖ := Real.sqrt_nonneg _
  have hab : a = a / b * b := by field_simp
  calc |ξ w - b * -g ℓ w| ≤ a * |g n w| + Real.sqrt (2 * (a / b)) * b * Real.sqrt (g e e) := hP
    _ ≤ a / b * b * (‖g‖ * ‖n‖ * ‖w‖) +
        Real.sqrt (2 * (a / b)) * b * (Real.sqrt ‖g‖ * ((1 + 2 * (‖g‖ * ‖n‖) * ‖ℓ‖) * ‖w‖)) := by
      rw [← hab]
      gcongr
      exact hq.trans (mul_le_mul_of_nonneg_left he hsg)
    _ = _ := by ring

/-- `a` eventually positive and bounded above, `b → ∞` ⟹ `a/b → 0`. -/
theorem tc_ratio_of_bounded {ι : Type*} {L : Filter ι} {a b : ι → ℝ} {A : ℝ}
    (ha : ∀ᶠ i in L, 0 < a i) (hA : ∀ᶠ i in L, a i ≤ A) (hb : Tendsto b L atTop) :
    Tendsto (fun i => a i / b i) L (𝓝 0) := by
  have hAb : Tendsto (fun i => A / b i) L (𝓝 0) := tendsto_const_nhds.div_atTop hb
  refine tendsto_of_tendsto_of_tendsto_of_le_of_le' tendsto_const_nhds hAb ?_ ?_
  · filter_upwards [ha, hb.eventually_gt_atTop 0] with i h1 h2; positivity
  · filter_upwards [hA, hb.eventually_gt_atTop 0] with i h1 h2
    exact div_le_div_of_nonneg_right h1 h2.le

/-- **① The corollary, moving frames and moving metrics, in operator norm.** Along any filter, if
the frame hypotheses hold eventually, `‖g_i‖`, `‖g_i‖‖n_i‖` and `‖ℓ_i‖` stay bounded, and
`ξ_i(ℓ_i)/ξ_i(n_i) → 0`, then `ξ_i/ξ_i(n_i) + g_i(ℓ_i,·) → 0` in operator norm. -/
theorem tc_tendsto {ι : Type*} {L : Filter ι} {g : ι → E →L[ℝ] E →L[ℝ] ℝ} {ℓ n : ι → E}
    {ξ : ι → E →L[ℝ] ℝ} {C : ℝ} (hF : ∀ᶠ i in L, FrameHyp (g i) (ℓ i) (n i) (ξ i))
    (hg : ∀ᶠ i in L, ‖g i‖ ≤ C) (hgn : ∀ᶠ i in L, ‖g i‖ * ‖n i‖ ≤ C)
    (hl : ∀ᶠ i in L, ‖ℓ i‖ ≤ C)
    (hr : Tendsto (fun i => ξ i (ℓ i) / ξ i (n i)) L (𝓝 0)) :
    Tendsto (fun i => (ξ i (n i))⁻¹ • ξ i + g i (ℓ i)) L (𝓝 0) := by
  set K := Real.sqrt C * (1 + 2 * C * C)
  have hlim : Tendsto (fun i => ξ i (ℓ i) / ξ i (n i) * C +
      Real.sqrt (2 * (ξ i (ℓ i) / ξ i (n i))) * K) L (𝓝 0) := by
    have h1 := hr.mul_const C
    have h2 := ((Real.continuous_sqrt.tendsto _).comp (hr.const_mul 2)).mul_const K
    simpa using h1.add h2
  refine squeeze_zero_norm' ?_ hlim
  filter_upwards [hF, hg, hgn, hl] with i hFi hgi hgni hli
  refine (tc_opNorm_bound hFi).trans ?_
  have hξ' : ∀ v, FutCausal (bil (g i)) (ℓ i) (n i) v → 0 < ((ξ i) : E →ₗ[ℝ] ℝ) v := hFi.2
  obtain ⟨ha, hb⟩ := tc_pos hFi.1 hξ'
  have ha' : 0 < ξ i (ℓ i) := ha
  have hb' : 0 < ξ i (n i) := hb
  have hr0 : 0 ≤ ξ i (ℓ i) / ξ i (n i) := by positivity
  have hC : 0 ≤ C := (norm_nonneg (g i)).trans hgi
  have h1 : Real.sqrt ‖g i‖ ≤ Real.sqrt C := Real.sqrt_le_sqrt hgi
  have h2 : 1 + 2 * (‖g i‖ * ‖n i‖) * ‖ℓ i‖ ≤ 1 + 2 * C * C := by
    nlinarith [mul_le_mul hgni hli (norm_nonneg _) hC]
  have hK : Real.sqrt ‖g i‖ * (1 + 2 * (‖g i‖ * ‖n i‖) * ‖ℓ i‖) ≤ K :=
    mul_le_mul h1 h2 (by positivity) (Real.sqrt_nonneg _)
  exact add_le_add (mul_le_mul_of_nonneg_left hgni hr0)
    (mul_le_mul_of_nonneg_left hK (Real.sqrt_nonneg _))

/-- The limit form: if moreover `g_i(ℓ_i,·) → G₀`, then `ξ_i/ξ_i(n_i) → −G₀` in operator norm. -/
theorem tc_tendsto_limit {ι : Type*} {L : Filter ι} {g : ι → E →L[ℝ] E →L[ℝ] ℝ} {ℓ n : ι → E}
    {ξ : ι → E →L[ℝ] ℝ} {C : ℝ} {G₀ : E →L[ℝ] ℝ}
    (hF : ∀ᶠ i in L, FrameHyp (g i) (ℓ i) (n i) (ξ i))
    (hg : ∀ᶠ i in L, ‖g i‖ ≤ C) (hgn : ∀ᶠ i in L, ‖g i‖ * ‖n i‖ ≤ C)
    (hl : ∀ᶠ i in L, ‖ℓ i‖ ≤ C)
    (hr : Tendsto (fun i => ξ i (ℓ i) / ξ i (n i)) L (𝓝 0))
    (hG : Tendsto (fun i => g i (ℓ i)) L (𝓝 G₀)) :
    Tendsto (fun i => (ξ i (n i))⁻¹ • ξ i) L (𝓝 (-G₀)) := by
  have := (tc_tendsto hF hg hgn hl hr).sub hG
  simpa using this

/-- **① The sequence corollary, fixed frame** (the registered form with `ℓ_m = ℓ`, `n_m = n`):
`ξ_m(ℓ) ≤ A` and `ξ_m(n) → ∞` ⟹ `ξ_m/ξ_m(n) → −g(ℓ,·)` in operator norm, hence pointwise. -/
theorem tc_sequence {g : E →L[ℝ] E →L[ℝ] ℝ} {ℓ n : E} {ξ : ℕ → E →L[ℝ] ℝ} {A : ℝ}
    (hF : ∀ m, FrameHyp g ℓ n (ξ m)) (hA : ∀ m, ξ m ℓ ≤ A)
    (hb : Tendsto (fun m => ξ m n) atTop atTop) :
    Tendsto (fun m => (ξ m n)⁻¹ • ξ m) atTop (𝓝 (-g ℓ)) ∧
      ∀ w, Tendsto (fun m => ξ m w / ξ m n) atTop (𝓝 (-g ℓ w)) := by
  have hpos : ∀ m, 0 < ξ m ℓ := fun m => by
    have hξ' : ∀ v, FutCausal (bil g) ℓ n v → 0 < ((ξ m) : E →ₗ[ℝ] ℝ) v := (hF m).2
    exact (tc_pos (hF m).1 hξ').1
  have hr := tc_ratio_of_bounded (Eventually.of_forall hpos) (Eventually.of_forall hA) hb
  have hop := tc_tendsto_limit (C := max ‖g‖ (max (‖g‖ * ‖n‖) ‖ℓ‖)) (G₀ := g ℓ)
    (Eventually.of_forall hF) (Eventually.of_forall fun _ => le_max_left _ _)
    (Eventually.of_forall fun _ => (le_max_left _ _).trans (le_max_right _ _))
    (Eventually.of_forall fun _ => (le_max_right _ _).trans (le_max_right _ _)) hr
    tendsto_const_nhds
  refine ⟨hop, fun w => ?_⟩
  have := ((ContinuousLinearMap.apply ℝ ℝ w).continuous.tendsto _).comp hop
  simpa [Function.comp_def, div_eq_inv_mul] using this

end Normed

end TCF

section Manifold
open Manifold
set_option linter.unusedSectionVars false

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
variable {N : Type*} [TopologicalSpace N] [ChartedSpace E N] [IsManifold 𝓘(ℝ, E) 1 N]

/-- The chart representative of a vector field (campaign 68). -/
noncomputable def chartRep (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N) (y : E) : E :=
  mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) ((extChartAt 𝓘(ℝ, E) p).symm y)
    (X ((extChartAt 𝓘(ℝ, E) p).symm y))

/-- `(extChartAt p).symm` is manifold-differentiable on the chart target (campaign 68). -/
theorem ld_mdifferentiableAt_symm (p : N) {y : E} (hy : y ∈ (extChartAt 𝓘(ℝ, E) p).target) :
    MDifferentiableAt 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p).symm y := by
  have h := mdifferentiableWithinAt_extChartAt_symm (I := 𝓘(ℝ, E)) (x := p) hy
  rwa [ModelWithCorners.range_eq_univ, mdifferentiableWithinAt_univ] at h

/-- The chart representative of a `(0,2)`-tensor field (campaign 68). -/
noncomputable def hRep
    (h : Π x : N, TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x →L[ℝ] ℝ)
    (p : N) (y : E) : E →L[ℝ] E →L[ℝ] ℝ :=
  let D : E →L[ℝ] E := mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p).symm y
  let H : E →L[ℝ] E →L[ℝ] ℝ := h ((extChartAt 𝓘(ℝ, E) p).symm y)
  H.bilinearComp D D

theorem ld_hRep_apply
    (h : Π x : N, TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x →L[ℝ] ℝ)
    (p : N) (y v w : E) :
    hRep h p y v w = h ((extChartAt 𝓘(ℝ, E) p).symm y)
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p).symm y v)
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p).symm y w) := rfl

theorem ld_mfderiv_symm_chart (p : N) {x : N} (hx : x ∈ (chartAt E p).source) (a : E) :
    mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p).symm (extChartAt 𝓘(ℝ, E) p x)
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) x a) = a := by
  have hxs : x ∈ (extChartAt 𝓘(ℝ, E) p).source := by rwa [extChartAt_source]
  have h := mfderivWithin_extChartAt_symm_comp_mfderiv_extChartAt' (I := 𝓘(ℝ, E)) hxs
  rw [ModelWithCorners.range_eq_univ, mfderivWithin_univ] at h
  exact DFunLike.congr_fun h a

theorem ld_mfderiv_chart_symm (p : N) {x : N} (hx : x ∈ (chartAt E p).source) (a : E) :
    mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) x
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p).symm (extChartAt 𝓘(ℝ, E) p x) a) = a := by
  have hxs : x ∈ (extChartAt 𝓘(ℝ, E) p).source := by rwa [extChartAt_source]
  have hy := (extChartAt 𝓘(ℝ, E) p).map_source hxs
  have h := mfderiv_extChartAt_comp_mfderivWithin_extChartAt_symm (I := 𝓘(ℝ, E)) hy
  rw [ModelWithCorners.range_eq_univ, mfderivWithin_univ] at h
  have h0 : mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p)
      ((extChartAt 𝓘(ℝ, E) p).symm (extChartAt 𝓘(ℝ, E) p x))
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p).symm (extChartAt 𝓘(ℝ, E) p x) a) = a := by
    have := DFunLike.congr_fun h a
    exact this
  have key : ∀ z, z = x → ∀ b : E, mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) z b =
      mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) x b := by rintro z rfl b; rfl
  exact (key _ ((extChartAt 𝓘(ℝ, E) p).left_inv hxs) _).symm.trans h0

theorem ld_chartRep_apply_chart (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N) {x : N}
    (hx : x ∈ (chartAt E p).source) :
    chartRep X p (extChartAt 𝓘(ℝ, E) p x) = mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) x (X x) := by
  have hxs : x ∈ (extChartAt 𝓘(ℝ, E) p).source := by rwa [extChartAt_source]
  have key : ∀ z, z = x → mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) z (X z) =
      mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) x (X x) := by rintro z rfl; rfl
  exact key _ ((extChartAt 𝓘(ℝ, E) p).left_inv hxs)

theorem ld_h_eq_hRep
    (h : Π x : N, TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x →L[ℝ] ℝ)
    (p : N) {x : N} (hx : x ∈ (chartAt E p).source) (a b : E) :
    h x a b = hRep h p (extChartAt 𝓘(ℝ, E) p x)
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) x a)
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) x b) := by
  have hxs : x ∈ (extChartAt 𝓘(ℝ, E) p).source := by rwa [extChartAt_source]
  have e1 := ld_mfderiv_symm_chart p hx a
  have e2 := ld_mfderiv_symm_chart p hx b
  have key : ∀ z, z = x → ∀ a' b' : E, a' = a → b' = b → h x a b = h z a' b' := by
    rintro z rfl a' b' rfl rfl; rfl
  exact key _ ((extChartAt 𝓘(ℝ, E) p).left_inv hxs) _ _ e1 e2

/-! ### Chart bookkeeping (new) -/

variable (p₀ : N)

lemma ch_mem_target {x : N} (hx : x ∈ (chartAt E p₀).source) :
    extChartAt 𝓘(ℝ, E) p₀ x ∈ (extChartAt 𝓘(ℝ, E) p₀).target :=
  (extChartAt 𝓘(ℝ, E) p₀).map_source (by rwa [extChartAt_source])

lemma ch_left_inv {x : N} (hx : x ∈ (chartAt E p₀).source) :
    (extChartAt 𝓘(ℝ, E) p₀).symm (extChartAt 𝓘(ℝ, E) p₀ x) = x :=
  (extChartAt 𝓘(ℝ, E) p₀).left_inv (by rwa [extChartAt_source])

lemma ch_symm_mem {y : E} (hy : y ∈ (extChartAt 𝓘(ℝ, E) p₀).target) :
    (extChartAt 𝓘(ℝ, E) p₀).symm y ∈ (chartAt E p₀).source := by
  rw [← extChartAt_source (I := 𝓘(ℝ, E))]; exact (extChartAt 𝓘(ℝ, E) p₀).map_target hy

lemma ch_right_inv {y : E} (hy : y ∈ (extChartAt 𝓘(ℝ, E) p₀).target) :
    extChartAt 𝓘(ℝ, E) p₀ ((extChartAt 𝓘(ℝ, E) p₀).symm y) = y :=
  (extChartAt 𝓘(ℝ, E) p₀).right_inv hy

lemma ch_contAt {x : N} (hx : x ∈ (chartAt E p₀).source) :
    ContinuousAt (extChartAt 𝓘(ℝ, E) p₀) x :=
  continuousAt_extChartAt' (by rwa [extChartAt_source])

/-- For a curve `γ : ℝ → N` differentiable at `s` with `γ s` in the chart: `φ ∘ γ` has derivative
`Dφ (γ' s)` at `s`, where `γ' s = mfderiv γ s 1`. -/
lemma ch_hasDerivAt_chart {γ : ℝ → N} {s : ℝ} (hγ : MDifferentiableAt 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ s)
    (hs : γ s ∈ (chartAt E p₀).source) :
    HasDerivAt (fun s => extChartAt 𝓘(ℝ, E) p₀ (γ s))
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p₀) (γ s)
        (mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ s (1 : ℝ))) s := by
  have hφ : MDifferentiableAt 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p₀) (γ s) :=
    mdifferentiableAt_extChartAt hs
  have hc := hφ.comp s hγ
  have hd : DifferentiableAt ℝ (extChartAt 𝓘(ℝ, E) p₀ ∘ γ) s :=
    mdifferentiableAt_iff_differentiableAt.1 hc
  have e2 : mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p₀ ∘ γ) s (1 : ℝ) =
      deriv (extChartAt 𝓘(ℝ, E) p₀ ∘ γ) s := by rw [mfderiv_eq_fderiv]; rfl
  have e3 : deriv (extChartAt 𝓘(ℝ, E) p₀ ∘ γ) s = mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E)
      (extChartAt 𝓘(ℝ, E) p₀) (γ s) (mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ s (1 : ℝ)) := by
    rw [← e2, mfderiv_comp s hφ hγ]; rfl
  rw [← e3]; exact hd.hasDerivAt

/-- For `β : ℝ → E` differentiable at `s` with `β s` in the chart target: `φ⁻¹ ∘ β` is
manifold-differentiable at `s` with velocity `Dφ⁻¹ (β' s)`. -/
lemma ch_vel_symm {β : ℝ → E} {s : ℝ} (hβ : DifferentiableAt ℝ β s)
    (hs : β s ∈ (extChartAt 𝓘(ℝ, E) p₀).target) :
    MDifferentiableAt 𝓘(ℝ, ℝ) 𝓘(ℝ, E) (fun s => (extChartAt 𝓘(ℝ, E) p₀).symm (β s)) s ∧
      (mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, E) (fun s => (extChartAt 𝓘(ℝ, E) p₀).symm (β s)) s (1 : ℝ) : E) =
        mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p₀).symm (β s) (deriv β s) := by
  have hφ := ld_mdifferentiableAt_symm p₀ hs
  have hb : MDifferentiableAt 𝓘(ℝ, ℝ) 𝓘(ℝ, E) β s := mdifferentiableAt_iff_differentiableAt.2 hβ
  refine ⟨hφ.comp s hb, ?_⟩
  have e : (fun s => (extChartAt 𝓘(ℝ, E) p₀).symm (β s)) = (extChartAt 𝓘(ℝ, E) p₀).symm ∘ β := rfl
  rw [e, mfderiv_comp s hφ hb]
  have e2 : mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, E) β s (1 : ℝ) = deriv β s := by rw [mfderiv_eq_fderiv]; rfl
  change mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p₀).symm (β s)
    (mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, E) β s (1 : ℝ)) = _
  exact congrArg _ e2


/-! ### The manifold spacetime (intrinsic definitions) -/

variable (E N) in
/-- **A time-oriented Lorentzian region of a manifold** `N` (intrinsic): an open `M ⊆ N`, a section
`g` of `T*N ⊗ T*N`, symmetric, and a section `T` of `TN`, timelike on `M`, with `g` positive on
`T^⊥` at points of `M`. (Mathlib's `TangentSpace 𝓘(ℝ,E) x` is by definition `E`; tangent vectors are
read in the preferred chart `chartAt E x`, which is how Mathlib's `mfderiv` is defined.) -/
structure MSpacetime where
  M : Set N
  isOpen_M : IsOpen M
  g : Π x : N, TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x →L[ℝ] ℝ
  symm : ∀ x (v w : E), g x v w = g x w v
  T : Π x : N, TangentSpace 𝓘(ℝ, E) x
  T_timelike : ∀ x ∈ M, g x (T x) (T x) < 0
  pos_on_perp : ∀ x ∈ M, ∀ v : E, g x v (T x) = 0 → v ≠ 0 → 0 < g x v v

namespace MSpacetime
variable (S : MSpacetime E N)

/-- `g_x` read as a bilinear form on `E` (Mathlib's `T_xN` is `E` by definition). -/
def gE (x : N) : E →L[ℝ] E →L[ℝ] ℝ := S.g x

/-- Future-directed timelike tangent vector at `x`. -/
def FutTimelike (x : N) (v : E) : Prop := S.gE x v v < 0 ∧ S.gE x v (S.T x) < 0
/-- Future-directed causal tangent vector at `x`. -/
def FutCausal (x : N) (v : E) : Prop := S.gE x v v ≤ 0 ∧ S.gE x v (S.T x) < 0

/-- `dτ_x(v) = mfderiv τ x v`, for `τ : N → ℝ`. -/
noncomputable def dfun (τ : N → ℝ) (x : N) (v : E) : ℝ := mfderiv 𝓘(ℝ, E) 𝓘(ℝ, ℝ) τ x v

/-- The velocity `γ'(t) = mfderiv γ t 1 ∈ T_{γ t} N` of a curve `γ : ℝ → N`. -/
noncomputable def vel (γ : ℝ → N) (t : ℝ) : E := mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ t (1 : ℝ)

/-- **The manifold timelike step** (intrinsic): a `C¹` curve `ℝ → N` (`ContMDiff`) from `x` to `y`,
inside `M` and with future-timelike `mfderiv` velocity on `[0,1]`. -/
def TStep (x y : N) : Prop :=
  ∃ γ : ℝ → N, ContMDiff 𝓘(ℝ, ℝ) 𝓘(ℝ, E) 1 γ ∧ γ 0 = x ∧ γ 1 = y ∧
    ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ S.M ∧ S.FutTimelike (γ t) (vel γ t)

/-- The manifold causal step (intrinsic). -/
def CStep (x y : N) : Prop :=
  ∃ γ : ℝ → N, ContMDiff 𝓘(ℝ, ℝ) 𝓘(ℝ, E) 1 γ ∧ γ 0 = x ∧ γ 1 = y ∧
    ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ S.M ∧ S.FutCausal (γ t) (vel γ t)

def Chr (x y : N) : Prop := Relation.TransGen S.TStep x y
def Cau (x y : N) : Prop := Relation.ReflTransGen S.CStep x y
def Ipast (p : N) : Set N := {q | S.Chr q p}
def Jpast (p : N) : Set N := {q | S.Cau q p}
def IpastSet (A : Set N) : Set N := ⋃ p ∈ A, S.Ipast p
def JpastSet (A : Set N) : Set N := ⋃ p ∈ A, S.Jpast p
/-- `D = I⁻(J)` on `N`. -/
def D (J : Set N) : Set N := S.IpastSet J
/-- `𝓗⁺ = ∂_N J⁻(J)`: the frontier in `N`. -/
def H (J : Set N) : Set N := frontier (S.JpastSet J)
def slice (J : Set N) (Θ : N → ℝ) (τ : ℝ) : Set N := {x | x ∈ S.D J ∧ Θ x = τ}
def SublevelProper (J : Set N) (Θ : N → ℝ) : Prop :=
  ∀ T : ℝ, closure {x | x ∈ S.D J ∧ Θ x ≤ T} ⊆ S.D J

/-- **Temporal on an open `U`** (intrinsic): `τ` is `C¹` on `U` (`ContMDiffOn`) and
`dτ = mfderiv τ` is positive on future-causal vectors. -/
def IsTemporalOn (U : Set N) (τ : N → ℝ) : Prop :=
  ContMDiffOn 𝓘(ℝ, E) 𝓘(ℝ, ℝ) 1 τ U ∧
    ∀ x ∈ U, ∀ v : E, S.FutCausal x v → 0 < dfun τ x v

/-- An inextendible piecewise-`C¹` future causal curve in `U` (intrinsic). -/
structure InextCausalCurveIn (U : Set N) where
  γ : ℝ → N
  cont : Continuous γ
  mem : ∀ t, γ t ∈ U
  brk : Set ℝ
  brk_fin : ∀ a b : ℝ, (brk ∩ Icc a b).Finite
  causal : ∀ t ∉ brk, MDifferentiableAt 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ t ∧ S.FutCausal (γ t) (vel γ t)
  inext_future : ¬ ∃ p ∈ U, Tendsto γ atTop (𝓝 p)
  inext_past : ¬ ∃ p ∈ U, Tendsto γ atBot (𝓝 p)

/-- A Cauchy temporal function on `U` (intrinsic; campaign 60's definition read on `N`). -/
def IsCauchyTemporalOn (U : Set N) (τ : N → ℝ) : Prop :=
  S.IsTemporalOn U τ ∧ ∀ c : S.InextCausalCurveIn U, ∀ a : ℝ, ∃! t : ℝ, τ (c.γ t) = a

lemma futTimelike_smul {x : N} {u : E} {c : ℝ} (hc : 0 < c) (h : S.FutTimelike x u) :
    S.FutTimelike x (c • u) := by
  obtain ⟨h1, h2⟩ := h
  refine ⟨?_, ?_⟩
  · simp only [map_smul, FunLike.coe_smul, Pi.smul_apply, smul_eq_mul]
    nlinarith [mul_pos hc hc]
  · simp only [map_smul, FunLike.coe_smul]
    change c * S.gE x u (S.T x) < 0
    nlinarith

lemma futCausal_smul {x : N} {u : E} {c : ℝ} (hc : 0 < c) (h : S.FutCausal x u) :
    S.FutCausal x (c • u) := by
  obtain ⟨h1, h2⟩ := h
  refine ⟨?_, ?_⟩
  · simp only [map_smul, FunLike.coe_smul, Pi.smul_apply, smul_eq_mul]
    nlinarith [mul_pos hc hc]
  · simp only [map_smul, FunLike.coe_smul]
    change c * S.gE x u (S.T x) < 0
    nlinarith

lemma tstep_mem {x y : N} (h : S.TStep x y) : x ∈ S.M ∧ y ∈ S.M := by
  obtain ⟨γ, -, h0, h1, hγ⟩ := h
  exact ⟨h0 ▸ (hγ 0 ⟨le_rfl, zero_le_one⟩).1, h1 ▸ (hγ 1 ⟨zero_le_one, le_rfl⟩).1⟩

lemma cstep_mem {x y : N} (h : S.CStep x y) : x ∈ S.M ∧ y ∈ S.M := by
  obtain ⟨γ, -, h0, h1, hγ⟩ := h
  exact ⟨h0 ▸ (hγ 0 ⟨le_rfl, zero_le_one⟩).1, h1 ▸ (hγ 1 ⟨zero_le_one, le_rfl⟩).1⟩

lemma chr_mem {x y : N} (h : S.Chr x y) : x ∈ S.M ∧ y ∈ S.M := by
  induction h with
  | single h => exact S.tstep_mem h
  | tail _ h ih => exact ⟨ih.1, (S.tstep_mem h).2⟩

lemma D_subset_M (J : Set N) : S.D J ⊆ S.M := fun x hx => by
  obtain ⟨p, -, h⟩ := mem_iUnion₂.1 hx
  exact (S.chr_mem h).1

lemma JpastSet_subset_M {J : Set N} (hJ : J ⊆ S.M) : S.JpastSet J ⊆ S.M := fun x hx => by
  obtain ⟨p, hp, h⟩ := mem_iUnion₂.1 hx
  rcases Relation.ReflTransGen.cases_head h with h | ⟨b, hb, -⟩
  · exact h ▸ hJ hp
  · exact (S.cstep_mem hb).1

lemma tstep_cstep {x y : N} (h : S.TStep x y) : S.CStep x y := by
  obtain ⟨γ, hγ, h0, h1, ht⟩ := h
  exact ⟨γ, hγ, h0, h1, fun t htI => ⟨(ht t htI).1, (ht t htI).2.1.le, (ht t htI).2.2⟩⟩

lemma chr_cau {x y : N} (h : S.Chr x y) : S.Cau x y := by
  induction h with
  | single h => exact Relation.ReflTransGen.single (S.tstep_cstep h)
  | tail _ h ih => exact ih.tail (S.tstep_cstep h)

lemma D_subset_JpastSet (J : Set N) : S.D J ⊆ S.JpastSet J := fun x hx => by
  obtain ⟨p, hp, h⟩ := mem_iUnion₂.1 hx
  exact mem_iUnion₂.2 ⟨p, hp, S.chr_cau h⟩

/-! ### The chart spacetime (chart-defined) -/

/-- **The one-chart hypothesis** (chart-defined regularity): `M` lies in the source of the preferred
chart at `p₀`, the chart representative `hRep g p₀` is `C¹` and `chartRep T p₀` is continuous on
`φ(M)`. -/
structure OneChart (p₀ : N) : Prop where
  sub : S.M ⊆ (chartAt E p₀).source
  g_C1 : ContDiffOn ℝ 1 (hRep S.g p₀) (extChartAt 𝓘(ℝ, E) p₀ '' S.M)
  T_cont : ContinuousOn (chartRep S.T p₀) (extChartAt 𝓘(ℝ, E) p₀ '' S.M)

variable {S} {p₀ : N}

lemma isOpen_chartImage (hC : S.OneChart p₀) : IsOpen (extChartAt 𝓘(ℝ, E) p₀ '' S.M) := by
  have hs : S.M ⊆ (extChartAt 𝓘(ℝ, E) p₀).source := by rw [extChartAt_source]; exact hC.sub
  rw [(extChartAt 𝓘(ℝ, E) p₀).image_eq_target_inter_inv_preimage hs]
  exact (continuousOn_extChartAt_symm p₀).isOpen_inter_preimage (isOpen_extChartAt_target p₀)
    S.isOpen_M

lemma chart_g {x : N} (hx : x ∈ (chartAt E p₀).source) (a b : E) :
    hRep S.g p₀ (extChartAt 𝓘(ℝ, E) p₀ x) (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p₀) x a)
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p₀) x b) = S.g x a b :=
  (ld_h_eq_hRep S.g p₀ hx a b).symm

/-- **The chart spacetime** on `E`: `M_V = φ(M)`, `g_V = hRep g p₀`, `T_V = chartRep T p₀`. -/
noncomputable def chartSp (hC : S.OneChart p₀) : Spacetime E where
  M := extChartAt 𝓘(ℝ, E) p₀ '' S.M
  isOpen_M := isOpen_chartImage hC
  g := hRep S.g p₀
  cont_g := hC.g_C1.continuousOn
  symm y v w := by rw [ld_hRep_apply, ld_hRep_apply]; exact S.symm _ _ _
  T := chartRep S.T p₀
  cont_T := hC.T_cont
  T_timelike := by
    rintro _ ⟨x, hx, rfl⟩
    rw [ld_chartRep_apply_chart _ _ (hC.sub hx), chart_g (hC.sub hx) (S.T x) (S.T x)]
    exact S.T_timelike x hx
  pos_on_perp := by
    rintro _ ⟨x, hx, rfl⟩ w hw hw0
    have hxs := hC.sub hx
    obtain ⟨v, rfl⟩ : ∃ v : E, mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p₀) x v = w :=
      ⟨_, ld_mfderiv_chart_symm p₀ hxs w⟩
    rw [ld_chartRep_apply_chart _ _ hxs, chart_g hxs v (S.T x)] at hw
    rw [chart_g hxs v v]
    refine S.pos_on_perp x hx v hw fun hv => hw0 ?_
    rw [hv]; exact map_zero _

variable (hC : S.OneChart p₀)
include hC

lemma futTimelike_chart {x : N} (hx : x ∈ (chartAt E p₀).source) (v : E) :
    (chartSp hC).FutTimelike (extChartAt 𝓘(ℝ, E) p₀ x)
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p₀) x v) ↔ S.FutTimelike x v := by
  show hRep S.g p₀ _ _ _ < 0 ∧ hRep S.g p₀ _ _ (chartRep S.T p₀ _) < 0 ↔ _
  rw [ld_chartRep_apply_chart _ _ hx, chart_g hx v v, chart_g hx v (S.T x)]; rfl

lemma futCausal_chart {x : N} (hx : x ∈ (chartAt E p₀).source) (v : E) :
    (chartSp hC).FutCausal (extChartAt 𝓘(ℝ, E) p₀ x)
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p₀) x v) ↔ S.FutCausal x v := by
  show hRep S.g p₀ _ _ _ ≤ 0 ∧ hRep S.g p₀ _ _ (chartRep S.T p₀ _) < 0 ↔ _
  rw [ld_chartRep_apply_chart _ _ hx, chart_g hx v v, chart_g hx v (S.T x)]; rfl

lemma futTimelike_chart' {u : E} (hu : u ∈ (extChartAt 𝓘(ℝ, E) p₀).target) (w : E) :
    (chartSp hC).FutTimelike u w ↔ S.FutTimelike ((extChartAt 𝓘(ℝ, E) p₀).symm u)
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p₀).symm u w) := by
  obtain ⟨x, hx, rfl⟩ : ∃ x ∈ (chartAt E p₀).source, extChartAt 𝓘(ℝ, E) p₀ x = u :=
    ⟨_, ch_symm_mem p₀ hu, ch_right_inv p₀ hu⟩
  have h1 := futTimelike_chart hC hx
    (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p₀).symm (extChartAt 𝓘(ℝ, E) p₀ x) w)
  rw [ld_mfderiv_chart_symm p₀ hx w] at h1
  have key : ∀ z, z = x → ∀ v : E, (S.FutTimelike x v ↔ S.FutTimelike z v) := by rintro z rfl v; rfl
  exact h1.trans (key _ (ch_left_inv p₀ hx) _)

lemma futCausal_chart' {u : E} (hu : u ∈ (extChartAt 𝓘(ℝ, E) p₀).target) (w : E) :
    (chartSp hC).FutCausal u w ↔ S.FutCausal ((extChartAt 𝓘(ℝ, E) p₀).symm u)
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p₀).symm u w) := by
  obtain ⟨x, hx, rfl⟩ : ∃ x ∈ (chartAt E p₀).source, extChartAt 𝓘(ℝ, E) p₀ x = u :=
    ⟨_, ch_symm_mem p₀ hu, ch_right_inv p₀ hu⟩
  have h1 := futCausal_chart hC hx
    (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p₀).symm (extChartAt 𝓘(ℝ, E) p₀ x) w)
  rw [ld_mfderiv_chart_symm p₀ hx w] at h1
  have key : ∀ z, z = x → ∀ v : E, (S.FutCausal x v ↔ S.FutCausal z v) := by rintro z rfl v; rfl
  exact h1.trans (key _ (ch_left_inv p₀ hx) _)

end MSpacetime

/-! ### The curve transfer (the registered likeliest stop): squash + `mfderiv`/`deriv` -/

variable {p₀ : N}

/-- `Dφ_x` with values in `E` (`T_{φ x}E = E`). -/
noncomputable def dchart (p₀ x : N) (v : E) : E :=
  mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p₀) x v
/-- `Dφ⁻¹_u` with values in `E`. -/
noncomputable def dchartInv (p₀ : N) (u w : E) : E :=
  mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p₀).symm u w

lemma dchartInv_smul (u w : E) (c : ℝ) : dchartInv p₀ u (c • w) = c • dchartInv p₀ u w :=
  (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p₀).symm u).map_smul c w

/-- **Curves, `N → V`.** A `C¹` curve of `N` inside `M ⊆ src` on `[0,1]` with `P`-velocity there gives
a `C¹` curve `β = φ ∘ γ ∘ σ` of `E` on all of `ℝ` (squash `σ`, since `φ ∘ γ` is only defined near
`[0,1]`), inside `φ(M)` with `Q`-velocity on `[0,1]`. -/
theorem ch_curve_NV {M : Set N} (hsub : M ⊆ (chartAt E p₀).source) {P : N → E → Prop}
    {Q : E → E → Prop}
    (hPQ : ∀ x ∈ (chartAt E p₀).source, ∀ v : E, P x v →
      Q (extChartAt 𝓘(ℝ, E) p₀ x) (dchart p₀ x v))
    (hQ : ∀ u w (c : ℝ), 0 < c → Q u w → Q u (c • w))
    {γ : ℝ → N} (hγ : ContMDiff 𝓘(ℝ, ℝ) 𝓘(ℝ, E) 1 γ)
    (ht : ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ M ∧ P (γ t) (MSpacetime.vel γ t)) :
    ∃ β : ℝ → E, ContDiff ℝ 1 β ∧ β 0 = extChartAt 𝓘(ℝ, E) p₀ (γ 0) ∧
      β 1 = extChartAt 𝓘(ℝ, E) p₀ (γ 1) ∧
      ∀ t ∈ Icc (0:ℝ) 1, β t ∈ extChartAt 𝓘(ℝ, E) p₀ '' M ∧ Q (β t) (deriv β t) := by
  have hU : IsOpen (γ ⁻¹' (chartAt E p₀).source) :=
    (chartAt E p₀).open_source.preimage hγ.continuous
  obtain ⟨δ, hδ, hδU⟩ := ch_exists_Ioo hU fun t ht' => hsub (ht t ht').1
  obtain ⟨σ, hσ, hσ0, hσ1, hσr, hσd, hσI⟩ := ch_squash hδ
  have hsrc : ∀ t, γ (σ t) ∈ (chartAt E p₀).source := fun t => hδU (hσr t)
  have hφγ : ∀ s, γ s ∈ (chartAt E p₀).source →
      HasDerivAt (fun s => extChartAt 𝓘(ℝ, E) p₀ (γ s)) (dchart p₀ (γ s) (MSpacetime.vel γ s)) s :=
    fun s hs => ch_hasDerivAt_chart p₀ (hγ.mdifferentiableAt one_ne_zero) hs
  refine ⟨fun t => extChartAt 𝓘(ℝ, E) p₀ (γ (σ t)), ?_, by simp only [hσ0], by simp only [hσ1],
    fun t htI => ?_⟩
  · refine contDiff_iff_contDiffAt.2 fun t => ?_
    have h1 : ContMDiffAt 𝓘(ℝ, ℝ) 𝓘(ℝ, E) 1 (fun s => extChartAt 𝓘(ℝ, E) p₀ (γ s)) (σ t) :=
      (contMDiffAt_extChartAt' (hsrc t)).comp (σ t) (hγ (σ t))
    exact (contMDiffAt_iff_contDiffAt.1 h1).comp t hσ.contDiffAt
  · have hd : HasDerivAt (fun t => extChartAt 𝓘(ℝ, E) p₀ (γ (σ t)))
        (deriv σ t • dchart p₀ (γ (σ t)) (MSpacetime.vel γ (σ t))) t :=
      (hφγ _ (hsrc t)).scomp t (hσd t).1
    rw [hd.deriv]
    obtain ⟨hm, hP⟩ := ht _ (hσI t htI)
    exact ⟨⟨_, hm, rfl⟩, hQ _ _ _ (hσd t).2 (hPQ _ (hsub hm) _ hP)⟩

/-- **Curves, `V → N`.** The converse: `γ = φ⁻¹ ∘ β ∘ σ`. -/
theorem ch_curve_VN {M : Set N} (hsub : M ⊆ (chartAt E p₀).source) {P : N → E → Prop}
    {Q : E → E → Prop}
    (hQP : ∀ u ∈ (extChartAt 𝓘(ℝ, E) p₀).target, ∀ w : E, Q u w →
      P ((extChartAt 𝓘(ℝ, E) p₀).symm u) (dchartInv p₀ u w))
    (hP : ∀ x v (c : ℝ), 0 < c → P x v → P x (c • v))
    {β : ℝ → E} (hβ : ContDiff ℝ 1 β)
    (ht : ∀ t ∈ Icc (0:ℝ) 1, β t ∈ extChartAt 𝓘(ℝ, E) p₀ '' M ∧ Q (β t) (deriv β t)) :
    ∃ γ : ℝ → N, ContMDiff 𝓘(ℝ, ℝ) 𝓘(ℝ, E) 1 γ ∧ γ 0 = (extChartAt 𝓘(ℝ, E) p₀).symm (β 0) ∧
      γ 1 = (extChartAt 𝓘(ℝ, E) p₀).symm (β 1) ∧
      ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ M ∧ P (γ t) (MSpacetime.vel γ t) := by
  have himg : ∀ {u}, u ∈ extChartAt 𝓘(ℝ, E) p₀ '' M → u ∈ (extChartAt 𝓘(ℝ, E) p₀).target ∧
      (extChartAt 𝓘(ℝ, E) p₀).symm u ∈ M := by
    rintro _ ⟨x, hx, rfl⟩
    exact ⟨ch_mem_target p₀ (hsub hx), by rw [ch_left_inv p₀ (hsub hx)]; exact hx⟩
  have hU : IsOpen (β ⁻¹' (extChartAt 𝓘(ℝ, E) p₀).target) :=
    (isOpen_extChartAt_target p₀).preimage hβ.continuous
  obtain ⟨δ, hδ, hδU⟩ := ch_exists_Ioo hU fun t ht' => (himg (ht t ht').1).1
  obtain ⟨σ, hσ, hσ0, hσ1, hσr, hσd, hσI⟩ := ch_squash hδ
  have htg : ∀ t, β (σ t) ∈ (extChartAt 𝓘(ℝ, E) p₀).target := fun t => hδU (hσr t)
  have hβσ : ContDiff ℝ 1 (fun t => β (σ t)) := hβ.comp hσ
  refine ⟨fun t => (extChartAt 𝓘(ℝ, E) p₀).symm (β (σ t)), fun t => ?_, by simp only [hσ0],
    by simp only [hσ1], fun t htI => ?_⟩
  · have h1 : ContMDiffAt 𝓘(ℝ, E) 𝓘(ℝ, E) 1 (extChartAt 𝓘(ℝ, E) p₀).symm (β (σ t)) :=
      (contMDiffOn_extChartAt_symm p₀).contMDiffAt
        ((isOpen_extChartAt_target p₀).mem_nhds (htg t))
    exact h1.comp t ((contMDiff_iff_contDiff.2 hβσ) t)
  · obtain ⟨-, hv⟩ := ch_vel_symm p₀ (hβσ.differentiable one_ne_zero t) (htg t)
    have hd : HasDerivAt (fun t => β (σ t)) (deriv σ t • deriv β (σ t)) t :=
      ((hβ.differentiable one_ne_zero (σ t)).hasDerivAt).scomp t (hσd t).1
    obtain ⟨hm, hQ⟩ := ht _ (hσI t htI)
    refine ⟨(himg hm).2, ?_⟩
    have e : MSpacetime.vel (fun t => (extChartAt 𝓘(ℝ, E) p₀).symm (β (σ t))) t =
        deriv σ t • dchartInv p₀ (β (σ t)) (deriv β (σ t)) := by
      have hv' : MSpacetime.vel (fun t => (extChartAt 𝓘(ℝ, E) p₀).symm (β (σ t))) t =
          dchartInv p₀ (β (σ t)) (deriv (fun t => β (σ t)) t) := hv
      rw [hv', hd.deriv, dchartInv_smul]
    have key := hP _ _ _ (hσd t).2 (hQP _ (htg t) _ hQ)
    rw [← e] at key
    exact key

namespace MSpacetime
variable {S : MSpacetime E N} (hC : S.OneChart p₀)
include hC

theorem ch_tstep_NV {x y : N} (h : S.TStep x y) :
    (chartSp hC).TStep (extChartAt 𝓘(ℝ, E) p₀ x) (extChartAt 𝓘(ℝ, E) p₀ y) := by
  obtain ⟨γ, hγ, rfl, rfl, ht⟩ := h
  exact ch_curve_NV hC.sub (fun x hx v h => (futTimelike_chart hC hx v).2 h)
    (fun u w c hc h => (chartSp hC).futTimelike_smul hc h) hγ ht

theorem ch_cstep_NV {x y : N} (h : S.CStep x y) :
    (chartSp hC).CStep (extChartAt 𝓘(ℝ, E) p₀ x) (extChartAt 𝓘(ℝ, E) p₀ y) := by
  obtain ⟨γ, hγ, rfl, rfl, ht⟩ := h
  exact ch_curve_NV hC.sub (fun x hx v h => (futCausal_chart hC hx v).2 h)
    (fun u w c hc h => (chartSp hC).ch_futCausal_smul hc h) hγ ht

theorem ch_tstep_VN {u v : E} (h : (chartSp hC).TStep u v) :
    S.TStep ((extChartAt 𝓘(ℝ, E) p₀).symm u) ((extChartAt 𝓘(ℝ, E) p₀).symm v) := by
  obtain ⟨β, hβ, rfl, rfl, ht⟩ := h
  exact ch_curve_VN hC.sub (fun u hu w h => (futTimelike_chart' hC hu w).1 h)
    (fun x v c hc h => S.futTimelike_smul hc h) hβ ht

theorem ch_cstep_VN {u v : E} (h : (chartSp hC).CStep u v) :
    S.CStep ((extChartAt 𝓘(ℝ, E) p₀).symm u) ((extChartAt 𝓘(ℝ, E) p₀).symm v) := by
  obtain ⟨β, hβ, rfl, rfl, ht⟩ := h
  exact ch_curve_VN hC.sub (fun u hu w h => (futCausal_chart' hC hu w).1 h)
    (fun x v c hc h => S.futCausal_smul hc h) hβ ht

/-- **`TStep` transfer (BUILT).** For `x, y` in the chart: `TStep_N x y ↔ TStep_V (φ x) (φ y)`. -/
theorem ch_tstep_iff {x y : N} (hx : x ∈ (chartAt E p₀).source) (hy : y ∈ (chartAt E p₀).source) :
    S.TStep x y ↔ (chartSp hC).TStep (extChartAt 𝓘(ℝ, E) p₀ x) (extChartAt 𝓘(ℝ, E) p₀ y) := by
  refine ⟨ch_tstep_NV hC, fun h => ?_⟩
  have := ch_tstep_VN hC h
  rwa [ch_left_inv p₀ hx, ch_left_inv p₀ hy] at this

/-- **`≪` transfer (BUILT).** -/
theorem ch_chr_iff {x y : N} (hx : x ∈ (chartAt E p₀).source) (hy : y ∈ (chartAt E p₀).source) :
    S.Chr x y ↔ (chartSp hC).Chr (extChartAt 𝓘(ℝ, E) p₀ x) (extChartAt 𝓘(ℝ, E) p₀ y) := by
  refine ⟨fun h => Relation.TransGen.lift _ (fun a b hab => ch_tstep_NV hC hab) _ _ h, fun h => ?_⟩
  have : S.Chr ((extChartAt 𝓘(ℝ, E) p₀).symm (extChartAt 𝓘(ℝ, E) p₀ x))
      ((extChartAt 𝓘(ℝ, E) p₀).symm (extChartAt 𝓘(ℝ, E) p₀ y)) :=
    Relation.TransGen.lift (r := (chartSp hC).TStep) (p := S.TStep)
      (fun u => (extChartAt 𝓘(ℝ, E) p₀).symm u) (fun a b hab => ch_tstep_VN hC hab) _ _ h
  rwa [ch_left_inv p₀ hx, ch_left_inv p₀ hy] at this

/-- **`≤` transfer (BUILT).** -/
theorem ch_cau_iff {x y : N} (hx : x ∈ (chartAt E p₀).source) (hy : y ∈ (chartAt E p₀).source) :
    S.Cau x y ↔ (chartSp hC).Cau (extChartAt 𝓘(ℝ, E) p₀ x) (extChartAt 𝓘(ℝ, E) p₀ y) := by
  refine ⟨fun h => Relation.ReflTransGen.lift _ (fun a b hab => ch_cstep_NV hC hab) _ _ h, fun h => ?_⟩
  have : S.Cau ((extChartAt 𝓘(ℝ, E) p₀).symm (extChartAt 𝓘(ℝ, E) p₀ x))
      ((extChartAt 𝓘(ℝ, E) p₀).symm (extChartAt 𝓘(ℝ, E) p₀ y)) :=
    Relation.ReflTransGen.lift (r := (chartSp hC).CStep) (p := S.CStep)
      (fun u => (extChartAt 𝓘(ℝ, E) p₀).symm u) (fun a b hab => ch_cstep_VN hC hab) _ _ h
  rwa [ch_left_inv p₀ hx, ch_left_inv p₀ hy] at this

/-! ### Sets: `D`, `J⁻`, `𝓗⁺`, slices -/

theorem ch_mem_D_iff {A : Set N} (hA : A ⊆ (chartAt E p₀).source) {x : N}
    (hx : x ∈ (chartAt E p₀).source) :
    x ∈ S.D A ↔ extChartAt 𝓘(ℝ, E) p₀ x ∈ (chartSp hC).D (extChartAt 𝓘(ℝ, E) p₀ '' A) := by
  constructor
  · intro h
    obtain ⟨p, hp, h⟩ := mem_iUnion₂.1 h
    exact mem_iUnion₂.2 ⟨_, mem_image_of_mem _ hp, (ch_chr_iff hC hx (hA hp)).1 h⟩
  · intro h
    obtain ⟨_, ⟨p, hp, rfl⟩, h⟩ := mem_iUnion₂.1 h
    exact mem_iUnion₂.2 ⟨p, hp, (ch_chr_iff hC hx (hA hp)).2 h⟩

theorem ch_mem_JpastSet_iff {A : Set N} (hA : A ⊆ (chartAt E p₀).source) {x : N}
    (hx : x ∈ (chartAt E p₀).source) :
    x ∈ S.JpastSet A ↔
      extChartAt 𝓘(ℝ, E) p₀ x ∈ (chartSp hC).JpastSet (extChartAt 𝓘(ℝ, E) p₀ '' A) := by
  constructor
  · intro h
    obtain ⟨p, hp, h⟩ := mem_iUnion₂.1 h
    exact mem_iUnion₂.2 ⟨_, mem_image_of_mem _ hp, (ch_cau_iff hC hx (hA hp)).1 h⟩
  · intro h
    obtain ⟨_, ⟨p, hp, rfl⟩, h⟩ := mem_iUnion₂.1 h
    exact mem_iUnion₂.2 ⟨p, hp, (ch_cau_iff hC hx (hA hp)).2 h⟩

/-- `D` of the chart spacetime, read through `φ⁻¹`. -/
theorem ch_mem_chartD_iff {A : Set N} (hA : A ⊆ (chartAt E p₀).source) {u : E} :
    u ∈ (chartSp hC).D (extChartAt 𝓘(ℝ, E) p₀ '' A) ↔
      u ∈ (extChartAt 𝓘(ℝ, E) p₀).target ∧ (extChartAt 𝓘(ℝ, E) p₀).symm u ∈ S.D A := by
  constructor
  · intro h
    obtain ⟨x, hxM, rfl⟩ := (chartSp hC).hl_D_subset_M _ h
    have hx := hC.sub hxM
    exact ⟨ch_mem_target p₀ hx, by rw [ch_left_inv p₀ hx]; exact (ch_mem_D_iff hC hA hx).2 h⟩
  · rintro ⟨hu, h⟩
    have := (ch_mem_D_iff hC hA (ch_symm_mem p₀ hu)).1 h
    rwa [ch_right_inv p₀ hu] at this

theorem ch_isOpen_D (J : Set N) (hJ : J ⊆ (chartAt E p₀).source) : IsOpen (S.D J) := by
  have e : S.D J = (chartAt E p₀).source ∩
      extChartAt 𝓘(ℝ, E) p₀ ⁻¹' (chartSp hC).D (extChartAt 𝓘(ℝ, E) p₀ '' J) := by
    ext x
    exact ⟨fun h => ⟨hC.sub (S.D_subset_M J h), (ch_mem_D_iff hC hJ (hC.sub (S.D_subset_M J h))).1 h⟩,
      fun h => (ch_mem_D_iff hC hJ h.1).2 h.2⟩
  rw [e]
  have hc : ContinuousOn (extChartAt 𝓘(ℝ, E) p₀) (chartAt E p₀).source := by
    rw [← extChartAt_source (I := 𝓘(ℝ, E))]; exact continuousOn_extChartAt p₀
  exact hc.isOpen_inter_preimage (chartAt E p₀).open_source ((chartSp hC).hl_D_open _)

end MSpacetime

/-! ### Topology through the chart: closure, frontier, Kuratowski limits -/

/-- For `A ⊆ N`, `B ⊆ E` that correspond on the chart (`x ∈ A ↔ φ x ∈ B` for `x` in the source):
`p ∈ closure A ↔ φ p ∈ closure B` at points of the source. -/
theorem ch_mem_closure_iff {A : Set N} {B : Set E}
    (hAB : ∀ x ∈ (chartAt E p₀).source, x ∈ A ↔ extChartAt 𝓘(ℝ, E) p₀ x ∈ B) {p : N}
    (hp : p ∈ (chartAt E p₀).source) :
    p ∈ closure A ↔ extChartAt 𝓘(ℝ, E) p₀ p ∈ closure B := by
  constructor
  · intro h
    have h1 : p ∈ closure ((chartAt E p₀).source ∩ A) :=
      (chartAt E p₀).open_source.inter_closure ⟨hp, h⟩
    refine closure_mono ?_ (mem_closure_image (ch_contAt p₀ hp) h1)
    rintro _ ⟨x, ⟨hx, hxA⟩, rfl⟩
    exact (hAB x hx).1 hxA
  · intro h
    have ht := ch_mem_target p₀ hp
    have h1 : extChartAt 𝓘(ℝ, E) p₀ p ∈ closure ((extChartAt 𝓘(ℝ, E) p₀).target ∩ B) :=
      (isOpen_extChartAt_target p₀).inter_closure ⟨ht, h⟩
    have h2 := mem_closure_image (continuousAt_extChartAt_symm'' ht) h1
    rw [ch_left_inv p₀ hp] at h2
    refine closure_mono ?_ h2
    rintro _ ⟨u, ⟨hu, huB⟩, rfl⟩
    exact (hAB _ (ch_symm_mem p₀ hu)).2 (by rwa [ch_right_inv p₀ hu])

theorem ch_mem_frontier_iff {A : Set N} {B : Set E}
    (hAB : ∀ x ∈ (chartAt E p₀).source, x ∈ A ↔ extChartAt 𝓘(ℝ, E) p₀ x ∈ B) {p : N}
    (hp : p ∈ (chartAt E p₀).source) :
    p ∈ frontier A ↔ extChartAt 𝓘(ℝ, E) p₀ p ∈ frontier B := by
  rw [frontier_eq_closure_inter_closure, frontier_eq_closure_inter_closure, mem_inter_iff,
    mem_inter_iff, ch_mem_closure_iff hAB hp,
    ch_mem_closure_iff (A := Aᶜ) (B := Bᶜ) (fun x hx => not_congr (hAB x hx)) hp]

lemma ch_nhds_NV {p : N} (hp : p ∈ (chartAt E p₀).source) {U' : Set E}
    (hU' : U' ∈ 𝓝 (extChartAt 𝓘(ℝ, E) p₀ p)) :
    (chartAt E p₀).source ∩ extChartAt 𝓘(ℝ, E) p₀ ⁻¹' U' ∈ 𝓝 p :=
  inter_mem ((chartAt E p₀).open_source.mem_nhds hp) ((ch_contAt p₀ hp).preimage_mem_nhds hU')

lemma ch_nhds_VN {p : N} (hp : p ∈ (chartAt E p₀).source) {U : Set N} (hU : U ∈ 𝓝 p) :
    (extChartAt 𝓘(ℝ, E) p₀).target ∩ (extChartAt 𝓘(ℝ, E) p₀).symm ⁻¹' U ∈
      𝓝 (extChartAt 𝓘(ℝ, E) p₀ p) := by
  have ht := ch_mem_target p₀ hp
  refine inter_mem ((isOpen_extChartAt_target p₀).mem_nhds ht)
    ((continuousAt_extChartAt_symm'' ht).preimage_mem_nhds ?_)
  rwa [ch_left_inv p₀ hp]

theorem ch_mem_KLi_iff {A : ℝ → Set N} {B : ℝ → Set E}
    (hAB : ∀ τ, ∀ x ∈ (chartAt E p₀).source, x ∈ A τ ↔ extChartAt 𝓘(ℝ, E) p₀ x ∈ B τ) {p : N}
    (hp : p ∈ (chartAt E p₀).source) :
    p ∈ KLi A ↔ extChartAt 𝓘(ℝ, E) p₀ p ∈ KLi B := by
  constructor
  · intro h U' hU'
    filter_upwards [h _ (ch_nhds_NV hp hU')] with τ ⟨z, hzA, hzs, hzU⟩
    exact ⟨_, (hAB τ z hzs).1 hzA, hzU⟩
  · intro h U hU
    filter_upwards [h _ (ch_nhds_VN hp hU)] with τ ⟨w, hwB, hwt, hwU⟩
    exact ⟨_, (hAB τ _ (ch_symm_mem p₀ hwt)).2 (by rwa [ch_right_inv p₀ hwt]), hwU⟩

theorem ch_mem_KLs_iff {A : ℝ → Set N} {B : ℝ → Set E}
    (hAB : ∀ τ, ∀ x ∈ (chartAt E p₀).source, x ∈ A τ ↔ extChartAt 𝓘(ℝ, E) p₀ x ∈ B τ) {p : N}
    (hp : p ∈ (chartAt E p₀).source) :
    p ∈ KLs A ↔ extChartAt 𝓘(ℝ, E) p₀ p ∈ KLs B := by
  constructor
  · intro h U' hU'
    refine (h _ (ch_nhds_NV hp hU')).mono fun τ ⟨z, hzA, hzs, hzU⟩ => ?_
    exact ⟨_, (hAB τ z hzs).1 hzA, hzU⟩
  · intro h U hU
    refine (h _ (ch_nhds_VN hp hU)).mono fun τ ⟨w, hwB, hwt, hwU⟩ => ?_
    exact ⟨_, (hAB τ _ (ch_symm_mem p₀ hwt)).2 (by rwa [ch_right_inv p₀ hwt]), hwU⟩

namespace MSpacetime
variable {S : MSpacetime E N} (hC : S.OneChart p₀)
include hC

theorem ch_mem_H_iff {J : Set N} (hJ : J ⊆ (chartAt E p₀).source) {x : N}
    (hx : x ∈ (chartAt E p₀).source) :
    x ∈ S.H J ↔ extChartAt 𝓘(ℝ, E) p₀ x ∈ (chartSp hC).H (extChartAt 𝓘(ℝ, E) p₀ '' J) :=
  ch_mem_frontier_iff (fun _ hy => ch_mem_JpastSet_iff hC hJ hy) hx

/-! ### Temporal and Cauchy functions -/

/-- **Cauchy transport, `N → V` (BUILT).** A Cauchy temporal function on `D_N` gives, through
`φ⁻¹`, a Cauchy temporal function of the chart exterior `Dsp (φ J)`. -/
theorem ch_isCauchy_NV {J : Set N} (hJ : J ⊆ S.M) {Θ : N → ℝ}
    (hΘ : S.IsCauchyTemporalOn (S.D J) Θ) :
    ((chartSp hC).Dsp (extChartAt 𝓘(ℝ, E) p₀ '' J)).IsCauchyTemporal
      (Θ ∘ (extChartAt 𝓘(ℝ, E) p₀).symm) := by
  have hJs := hJ.trans hC.sub
  have hD : ∀ u ∈ (chartSp hC).D (extChartAt 𝓘(ℝ, E) p₀ '' J),
      u ∈ (extChartAt 𝓘(ℝ, E) p₀).target ∧ (extChartAt 𝓘(ℝ, E) p₀).symm u ∈ S.D J :=
    fun u hu => (ch_mem_chartD_iff hC hJs).1 hu
  have hDo := ch_isOpen_D hC J hJs
  have hΘd : ∀ u ∈ (chartSp hC).D (extChartAt 𝓘(ℝ, E) p₀ '' J),
      ContMDiffAt 𝓘(ℝ, E) 𝓘(ℝ, ℝ) 1 (Θ ∘ (extChartAt 𝓘(ℝ, E) p₀).symm) u := fun u hu =>
    (hΘ.1.1.contMDiffAt (hDo.mem_nhds (hD u hu).2)).comp u
      ((contMDiffOn_extChartAt_symm p₀).contMDiffAt
        ((isOpen_extChartAt_target p₀).mem_nhds (hD u hu).1))
  refine ⟨⟨fun u hu => (contMDiffAt_iff_contDiffAt.1 (hΘd u hu)).contDiffWithinAt,
    fun u hu w hw => ?_⟩, fun c a => ?_⟩
  · obtain ⟨hut, hxD⟩ := hD u hu
    have h1 := (hΘ.1.1.contMDiffAt (hDo.mem_nhds hxD)).mdifferentiableAt one_ne_zero
    have h2 := ld_mdifferentiableAt_symm p₀ hut
    have e : fderiv ℝ (Θ ∘ (extChartAt 𝓘(ℝ, E) p₀).symm) u w =
        dfun Θ ((extChartAt 𝓘(ℝ, E) p₀).symm u) (dchartInv p₀ u w) := by
      have e1 : mfderiv 𝓘(ℝ, E) 𝓘(ℝ, ℝ) (Θ ∘ (extChartAt 𝓘(ℝ, E) p₀).symm) u w =
          fderiv ℝ (Θ ∘ (extChartAt 𝓘(ℝ, E) p₀).symm) u w := by rw [mfderiv_eq_fderiv]; rfl
      rw [← e1, mfderiv_comp u h1 h2]; rfl
    rw [e]
    exact hΘ.1.2 _ hxD _ ((futCausal_chart' hC hut w).1 hw)
  · have hDc := fun t => hD _ (c.mem t)
    let c' : S.InextCausalCurveIn (S.D J) :=
      { γ := fun t => (extChartAt 𝓘(ℝ, E) p₀).symm (c.γ t)
        cont := (continuousOn_extChartAt_symm p₀).comp_continuous c.cont fun t => (hDc t).1
        mem := fun t => (hDc t).2
        brk := c.brk
        brk_fin := c.brk_fin
        causal := fun t ht => by
          obtain ⟨hd, hcaus⟩ := c.causal t ht
          obtain ⟨hmd, hvel⟩ := ch_vel_symm p₀ hd (hDc t).1
          refine ⟨hmd, ?_⟩
          show S.FutCausal _ (mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, E) _ t (1 : ℝ))
          rw [hvel]
          exact (futCausal_chart' hC (hDc t).1 _).1 hcaus
        inext_future := by
          rintro ⟨p, hp, hlim⟩
          apply c.inext_future
          have hps := hC.sub (S.D_subset_M J hp)
          refine ⟨_, (ch_mem_D_iff hC hJs hps).1 hp, ?_⟩
          refine ((ch_contAt p₀ hps).tendsto.comp hlim).congr fun t => ?_
          exact ch_right_inv p₀ (hDc t).1
        inext_past := by
          rintro ⟨p, hp, hlim⟩
          apply c.inext_past
          have hps := hC.sub (S.D_subset_M J hp)
          refine ⟨_, (ch_mem_D_iff hC hJs hps).1 hp, ?_⟩
          refine ((ch_contAt p₀ hps).tendsto.comp hlim).congr fun t => ?_
          exact ch_right_inv p₀ (hDc t).1 }
    exact hΘ.2 c' a

end MSpacetime

/-! ### The headline on `N` -/

namespace MSpacetime
variable {S : MSpacetime E N} (hC : S.OneChart p₀)
include hC

/-- `g` `C¹` in the chart gives `LocallyLipschitzOn` for the chart spacetime. -/
theorem ch_chart_lipschitz : LocallyLipschitzOn (chartSp hC).M (chartSp hC).g := by
  intro u hu
  obtain ⟨K, t, ht, hK⟩ :=
    ((hC.g_C1 u hu).contDiffAt ((chartSp hC).isOpen_M.mem_nhds hu)).exists_lipschitzOnWith
  exact ⟨K, t, nhdsWithin_le_nhds ht, hK⟩

/-- **Cauchy transport, `V → N` (BUILT)**, the converse of `ch_isCauchy_NV` (used by the witness):
a Cauchy temporal function of the chart exterior pulls back by `φ` to one on `D_N`. -/
theorem ch_isCauchy_VN {J : Set N} (hJ : J ⊆ S.M) {Θ' : E → ℝ}
    (hΘ : ((chartSp hC).Dsp (extChartAt 𝓘(ℝ, E) p₀ '' J)).IsCauchyTemporal Θ') :
    S.IsCauchyTemporalOn (S.D J) (Θ' ∘ extChartAt 𝓘(ℝ, E) p₀) := by
  have hJs := hJ.trans hC.sub
  have hDs : ∀ x ∈ S.D J, x ∈ (chartAt E p₀).source := fun x hx => hC.sub (S.D_subset_M J hx)
  have hD : ∀ x ∈ S.D J, extChartAt 𝓘(ℝ, E) p₀ x ∈ (chartSp hC).D (extChartAt 𝓘(ℝ, E) p₀ '' J) :=
    fun x hx => (ch_mem_D_iff hC hJs (hDs x hx)).1 hx
  have hDo : IsOpen ((chartSp hC).D (extChartAt 𝓘(ℝ, E) p₀ '' J)) := (chartSp hC).hl_D_open _
  have hΘd : ∀ x ∈ S.D J, ContMDiffAt 𝓘(ℝ, E) 𝓘(ℝ, ℝ) 1 Θ' (extChartAt 𝓘(ℝ, E) p₀ x) :=
    fun x hx => contMDiffAt_iff_contDiffAt.2 ((hΘ.1.1 _ (hD x hx)).contDiffAt
      (hDo.mem_nhds (hD x hx)))
  refine ⟨⟨fun x hx => ((hΘd x hx).comp x (contMDiffAt_extChartAt' (hDs x hx))).contMDiffWithinAt,
    fun x hx v hv => ?_⟩, fun c a => ?_⟩
  · have h1 := (hΘd x hx).mdifferentiableAt one_ne_zero
    have h2 : MDifferentiableAt 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p₀) x :=
      mdifferentiableAt_extChartAt (hDs x hx)
    have e : dfun (Θ' ∘ extChartAt 𝓘(ℝ, E) p₀) x v =
        fderiv ℝ Θ' (extChartAt 𝓘(ℝ, E) p₀ x) (dchart p₀ x v) := by
      have e1 : mfderiv 𝓘(ℝ, E) 𝓘(ℝ, ℝ) Θ' (extChartAt 𝓘(ℝ, E) p₀ x) =
          fderiv ℝ Θ' (extChartAt 𝓘(ℝ, E) p₀ x) := by rw [mfderiv_eq_fderiv]; rfl
      show mfderiv 𝓘(ℝ, E) 𝓘(ℝ, ℝ) (Θ' ∘ extChartAt 𝓘(ℝ, E) p₀) x v = _
      rw [mfderiv_comp x h1 h2, ← e1]; rfl
    rw [e]
    exact hΘ.1.2 _ (hD x hx) _ ((futCausal_chart hC (hDs x hx) v).2 hv)
  · have hcs := fun t => hDs _ (c.mem t)
    let c' : ((chartSp hC).Dsp (extChartAt 𝓘(ℝ, E) p₀ '' J)).InextCausalCurve :=
      { γ := fun t => extChartAt 𝓘(ℝ, E) p₀ (c.γ t)
        cont := continuous_iff_continuousAt.2 fun t => (ch_contAt p₀ (hcs t)).comp c.cont.continuousAt
        mem := fun t => hD _ (c.mem t)
        brk := c.brk
        brk_fin := c.brk_fin
        causal := fun t ht => by
          obtain ⟨hd, hcaus⟩ := c.causal t ht
          have h := ch_hasDerivAt_chart p₀ hd (hcs t)
          refine ⟨h.differentiableAt, ?_⟩
          rw [h.deriv]
          exact (futCausal_chart hC (hcs t) _).2 hcaus
        inext_future := by
          rintro ⟨u, hu, hlim⟩
          apply c.inext_future
          obtain ⟨hut, hx⟩ := (ch_mem_chartD_iff hC hJs).1 hu
          refine ⟨_, hx, ((continuousAt_extChartAt_symm'' hut).tendsto.comp hlim).congr fun t => ?_⟩
          exact ch_left_inv p₀ (hcs t)
        inext_past := by
          rintro ⟨u, hu, hlim⟩
          apply c.inext_past
          obtain ⟨hut, hx⟩ := (ch_mem_chartD_iff hC hJs).1 hu
          refine ⟨_, hx, ((continuousAt_extChartAt_symm'' hut).tendsto.comp hlim).congr fun t => ?_⟩
          exact ch_left_inv p₀ (hcs t) }
    exact hΘ.2 c' a

end MSpacetime

/-! ## Copied (campaign 85, `ManifoldExtension.lean`): the local one-chart hypothesis, the local past step,
the past extension and two-sided ⇒ future Cauchy on `N` -/

namespace MSpacetime
variable (S : MSpacetime E N)

/-- The same spacetime with `M` shrunk to an open `U ⊆ M` (same `g`, `T`). -/
def restrictM (U : Set N) (hU : IsOpen U) (hUM : U ⊆ S.M) : MSpacetime E N where
  M := U
  isOpen_M := hU
  g := S.g
  symm := S.symm
  T := S.T
  T_timelike := fun x hx => S.T_timelike x (hUM hx)
  pos_on_perp := fun x hx => S.pos_on_perp x (hUM hx)

lemma restrictM_tstep {U : Set N} {hU : IsOpen U} {hUM : U ⊆ S.M} {x y : N}
    (h : (S.restrictM U hU hUM).TStep x y) : S.TStep x y := by
  obtain ⟨γ, hγ, h0, h1, ht⟩ := h
  exact ⟨γ, hγ, h0, h1, fun t htI => ⟨hUM (ht t htI).1, (ht t htI).2⟩⟩

/-- **The local one-chart hypothesis** (chart-defined regularity, the local form of campaign 84's
`OneChart`): every `p ∈ M` has an open `U ∋ φ_p(p)`, `φ_p = extChartAt p` the preferred chart at
`p`, with `U ⊆ φ_p(M ∩ src_p)`, on which `hRep g p` is `C¹` and `chartRep T p` is continuous. -/
def LocallyOneChart : Prop :=
  ∀ p ∈ S.M, ∃ U : Set E, IsOpen U ∧ extChartAt 𝓘(ℝ, E) p p ∈ U ∧
    U ⊆ extChartAt 𝓘(ℝ, E) p '' (S.M ∩ (chartAt E p).source) ∧
    ContDiffOn ℝ 1 (hRep S.g p) U ∧ ContinuousOn (chartRep S.T p) U

variable {S}

/-- `LocallyOneChart` passes to an open `U ⊆ M`. -/
lemma LocallyOneChart.restrict (hL : S.LocallyOneChart) {U : Set N} (hU : IsOpen U)
    (hUM : U ⊆ S.M) : (S.restrictM U hU hUM).LocallyOneChart := by
  intro p hp
  obtain ⟨W, hW, hpW, hWsub, hg, hT⟩ := hL p (hUM hp)
  refine ⟨W ∩ ((extChartAt 𝓘(ℝ, E) p).target ∩ (extChartAt 𝓘(ℝ, E) p).symm ⁻¹' U),
    hW.inter ((continuousOn_extChartAt_symm p).isOpen_inter_preimage
      (isOpen_extChartAt_target p) hU),
    ⟨hpW, mem_extChartAt_target p, ?_⟩, ?_, hg.mono inter_subset_left, hT.mono inter_subset_left⟩
  · show (extChartAt 𝓘(ℝ, E) p).symm (extChartAt 𝓘(ℝ, E) p p) ∈ U
    rw [extChartAt_to_inv]; exact hp
  · rintro y ⟨hyW, -, hyU⟩
    obtain ⟨x, ⟨-, hxs⟩, rfl⟩ := hWsub hyW
    refine ⟨x, ⟨?_, hxs⟩, rfl⟩
    have h := ch_left_inv p hxs
    rw [mem_preimage, h] at hyU
    exact hyU

variable (S)

/-- **The local past step (BUILT), through `q`'s own chart.** For `q ∈ M` there is a map `f`,
continuous at `q`, with `f q ∈ M` and `TStep_N (f x) x` for all `x` near `q`:
`f x = φ_q⁻¹(φ_q x − ℓ T_V(φ_q x))`, `ℓ` a uniform safe length of the chart spacetime of the
restriction of `S` to `W = src_q ∩ φ_q⁻¹ U ∩ M` (tube lemma `safe_uniform`), transferred by
campaign 84's `ch_tstep_VN`. -/
theorem me_local_step (hL : S.LocallyOneChart) {q : N} (hq : q ∈ S.M) :
    ∃ f : N → N, ContinuousAt f q ∧ f q ∈ S.M ∧ ∀ᶠ x in 𝓝 q, S.TStep (f x) x := by
  obtain ⟨U, hU, hqU, -, hg, hT⟩ := hL q hq
  have hcs : ContinuousOn (extChartAt 𝓘(ℝ, E) q) (chartAt E q).source := by
    rw [← extChartAt_source (I := 𝓘(ℝ, E))]; exact continuousOn_extChartAt q
  set W : Set N := ((chartAt E q).source ∩ extChartAt 𝓘(ℝ, E) q ⁻¹' U) ∩ S.M with hWdef
  have hWo : IsOpen W :=
    (hcs.isOpen_inter_preimage (chartAt E q).open_source hU).inter S.isOpen_M
  have hWM : W ⊆ S.M := inter_subset_right
  have hWU : extChartAt 𝓘(ℝ, E) q '' W ⊆ U := by rintro _ ⟨x, hx, rfl⟩; exact hx.1.2
  have hC : (S.restrictM W hWo hWM).OneChart q :=
    { sub := fun x hx => hx.1.1
      g_C1 := hg.mono hWU
      T_cont := hT.mono hWU }
  set Sp := chartSp hC with hSp
  have hqW : q ∈ W := ⟨⟨mem_chart_source E q, hqU⟩, hq⟩
  have huM : extChartAt 𝓘(ℝ, E) q q ∈ Sp.M := ⟨q, hqW, rfl⟩
  obtain ⟨ℓ, hℓ, hsafe⟩ := Sp.safe_uniform huM
  have hmem : Sp.seg (extChartAt 𝓘(ℝ, E) q q) (-ℓ) ∈ Sp.M :=
    (hsafe.self_of_nhds (-ℓ) ⟨le_rfl, by linarith⟩).1
  obtain ⟨z, hzW, hze⟩ := hmem
  have htgt : Sp.seg (extChartAt 𝓘(ℝ, E) q q) (-ℓ) ∈ (extChartAt 𝓘(ℝ, E) q).target := by
    rw [← hze]; exact ch_mem_target q hzW.1.1
  have h1 : ContinuousAt (extChartAt 𝓘(ℝ, E) q) q := ch_contAt q (mem_chart_source E q)
  refine ⟨fun x => (extChartAt 𝓘(ℝ, E) q).symm (Sp.seg (extChartAt 𝓘(ℝ, E) q x) (-ℓ)), ?_, ?_, ?_⟩
  · have h2 : ContinuousAt (fun x => Sp.seg (extChartAt 𝓘(ℝ, E) q x) (-ℓ)) q := by
      show ContinuousAt (fun x => extChartAt 𝓘(ℝ, E) q x + (-ℓ) • Sp.T (extChartAt 𝓘(ℝ, E) q x)) q
      exact h1.add (continuousAt_const.smul ((Sp.contAt_T huM).comp h1))
    exact ContinuousAt.comp (g := (extChartAt 𝓘(ℝ, E) q).symm)
      (f := fun x => Sp.seg (extChartAt 𝓘(ℝ, E) q x) (-ℓ))
      ((continuousOn_extChartAt_symm q).continuousAt
        ((isOpen_extChartAt_target q).mem_nhds htgt)) h2
  · show (extChartAt 𝓘(ℝ, E) q).symm (Sp.seg (extChartAt 𝓘(ℝ, E) q q) (-ℓ)) ∈ S.M
    rw [← hze, ch_left_inv q hzW.1.1]; exact hzW.2
  · have hev : ∀ᶠ x in 𝓝 q, x ∈ (chartAt E q).source ∧ Sp.Safe (extChartAt 𝓘(ℝ, E) q x) ℓ :=
      Filter.Eventually.and ((chartAt E q).open_source.mem_nhds (mem_chart_source E q))
        (h1.tendsto.eventually hsafe)
    filter_upwards [hev] with x hx
    have hst := Sp.seg_tstep hx.2 le_rfl (by linarith : -ℓ < 0) le_rfl
    rw [Spacetime.seg_zero] at hst
    have h := ch_tstep_VN hC hst
    rw [ch_left_inv q hx.1] at h
    exact S.restrictM_tstep h

/-! ### A temporal `Θ` along manifold curves -/

lemma me_temporal_hasDerivAt {Θ : N → ℝ} {U : Set N} (hU : IsOpen U)
    (hΘ : ContMDiffOn 𝓘(ℝ, E) 𝓘(ℝ, ℝ) 1 Θ U) {γ : ℝ → N} {t : ℝ}
    (hγ : MDifferentiableAt 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ t) (ht : γ t ∈ U) :
    HasDerivAt (fun s => Θ (γ s)) (dfun (E := E) Θ (γ t) (vel (E := E) γ t)) t := by
  have hΘd : MDifferentiableAt 𝓘(ℝ, E) 𝓘(ℝ, ℝ) Θ (γ t) :=
    (hΘ.contMDiffAt (hU.mem_nhds ht)).mdifferentiableAt one_ne_zero
  have hc := hΘd.comp t hγ
  have hd : DifferentiableAt ℝ (Θ ∘ γ) t := mdifferentiableAt_iff_differentiableAt.1 hc
  have e2 : mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, ℝ) (Θ ∘ γ) t (1 : ℝ) = deriv (Θ ∘ γ) t := by
    rw [mfderiv_eq_fderiv]; rfl
  have e3 : deriv (Θ ∘ γ) t = dfun (E := E) Θ (γ t) (vel (E := E) γ t) := by
    rw [← e2, mfderiv_comp t hΘd hγ]; rfl
  rw [← e3]; exact hd.hasDerivAt

/-- A temporal `Θ` strictly increases along a manifold timelike piece on `[0,1]`. -/
lemma me_temporal_strictMonoOn {Θ : N → ℝ} (hΘ : S.IsTemporalOn S.M Θ) {γ : ℝ → N}
    (hγ : ContMDiff 𝓘(ℝ, ℝ) 𝓘(ℝ, E) 1 γ)
    (ht : ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ S.M ∧ S.FutTimelike (γ t) (vel γ t)) :
    StrictMonoOn (fun s => Θ (γ s)) (Icc 0 1) := by
  have hcont : ContinuousOn (fun s => Θ (γ s)) (Icc (0:ℝ) 1) :=
    hΘ.1.continuousOn.comp hγ.continuous.continuousOn fun t h => (ht t h).1
  refine strictMonoOn_of_deriv_pos (convex_Icc 0 1) hcont fun t htI => ?_
  rw [interior_Icc] at htI
  obtain ⟨hm, h1, h2⟩ := ht t (Ioo_subset_Icc_self htI)
  rw [(me_temporal_hasDerivAt S.isOpen_M hΘ.1 (hγ.mdifferentiableAt one_ne_zero) hm).deriv]
  exact hΘ.2 _ hm _ ⟨h1.le, h2⟩

lemma me_temporal_tstep {Θ : N → ℝ} (hΘ : S.IsTemporalOn S.M Θ) {x y : N} (h : S.TStep x y) :
    Θ x < Θ y := by
  obtain ⟨γ, hγ, h0, h1, ht⟩ := h
  have := S.me_temporal_strictMonoOn hΘ hγ ht ⟨le_rfl, zero_le_one⟩ ⟨zero_le_one, le_rfl⟩
    zero_lt_one
  simpa [h0, h1] using this

lemma me_contAt {Θ : N → ℝ} (hΘ : S.IsTemporalOn S.M Θ) {x : N} (hx : x ∈ S.M) :
    ContinuousAt Θ x :=
  hΘ.1.continuousOn.continuousAt (S.isOpen_M.mem_nhds hx)

/-! ### The drop `δ`, the vertices, and no past limit -/

/-- **The step size** `δ(x) = sup {min(1, Θ x − Θ y) : TStep_N y x}` (no metric; the `min` is
inside the `sup` so that the set is bounded above). -/
noncomputable def pastDrop (Θ : N → ℝ) (x : N) : ℝ :=
  sSup ((fun y => min 1 (Θ x - Θ y)) '' {y | S.TStep y x})

lemma pastDrop_bdd (Θ : N → ℝ) (x : N) :
    BddAbove ((fun y => min 1 (Θ x - Θ y)) '' {y | S.TStep y x}) :=
  ⟨1, by rintro _ ⟨y, -, rfl⟩; exact min_le_left _ _⟩

lemma le_pastDrop {Θ : N → ℝ} {x y : N} (h : S.TStep y x) :
    min 1 (Θ x - Θ y) ≤ S.pastDrop Θ x :=
  le_csSup (S.pastDrop_bdd Θ x) ⟨y, h, rfl⟩

open Classical in
/-- The next vertex: a `y` with `TStep_N y x` and drop `Θ x − Θ y > δ(x)/2`. -/
noncomputable def nextV (Θ : N → ℝ) (x : N) : N :=
  if h : ∃ y, S.TStep y x ∧ S.pastDrop Θ x / 2 < Θ x - Θ y then h.choose else x

lemma nextV_spec (hL : S.LocallyOneChart) {Θ : N → ℝ} (hΘ : S.IsTemporalOn S.M Θ) {x : N}
    (hx : x ∈ S.M) :
    S.TStep (S.nextV Θ x) x ∧ S.pastDrop Θ x / 2 < Θ x - Θ (S.nextV Θ x) := by
  obtain ⟨f, -, -, hf⟩ := S.me_local_step hL hx
  have hy := hf.self_of_nhds
  have hpos : 0 < min 1 (Θ x - Θ (f x)) :=
    lt_min one_pos (sub_pos.2 (S.me_temporal_tstep hΘ hy))
  have hδ : 0 < S.pastDrop Θ x := hpos.trans_le (S.le_pastDrop hy)
  have hex : ∃ y, S.TStep y x ∧ S.pastDrop Θ x / 2 < Θ x - Θ y := by
    have hne : ((fun y => min 1 (Θ x - Θ y)) '' {y | S.TStep y x}).Nonempty :=
      ⟨_, ⟨f x, hy, rfl⟩⟩
    obtain ⟨_, ⟨y, hy, rfl⟩, hlt⟩ := exists_lt_of_lt_csSup hne (half_lt_self hδ)
    exact ⟨y, hy, hlt.trans_le (min_le_right _ _)⟩
  have e : S.nextV Θ x = hex.choose := by
    unfold nextV; split_ifs with h
    · rfl
    · exact absurd hex h
  rw [e]; exact hex.choose_spec

/-- The vertices `X 0 = x`, `X (k+1) = nextV (X k)`. -/
noncomputable def mvert (Θ : N → ℝ) (x : N) : ℕ → N
  | 0 => x
  | k + 1 => S.nextV Θ (mvert Θ x k)

variable {S}
variable (hL : S.LocallyOneChart) {Θ : N → ℝ} (hΘ : S.IsTemporalOn S.M Θ) {x : N} (hx : x ∈ S.M)
include hL hΘ hx

lemma mvert_mem : ∀ k, S.mvert Θ x k ∈ S.M
  | 0 => hx
  | k + 1 => (S.tstep_mem (S.nextV_spec hL hΘ (mvert_mem k)).1).1

lemma mvert_step (k : ℕ) : S.TStep (S.mvert Θ x (k + 1)) (S.mvert Θ x k) ∧
    S.pastDrop Θ (S.mvert Θ x k) / 2 < Θ (S.mvert Θ x k) - Θ (S.mvert Θ x (k + 1)) :=
  S.nextV_spec hL hΘ (mvert_mem hL hΘ hx k)

lemma mvert_le : ∀ k, Θ (S.mvert Θ x k) ≤ Θ x
  | 0 => le_rfl
  | k + 1 => (S.me_temporal_tstep hΘ (mvert_step hL hΘ hx k).1).le.trans (mvert_le k)

/-- **No past limit of the vertices (BUILT).** If `X k → q ∈ M`, the local step at `q` (in `q`'s
own chart) gives `δ ≥ min(1, d/2)` near `q`, `d = Θ q − Θ (f q) > 0`, so the drops
`Θ (X k) − Θ (X (k+1))` stay above `min(1, d/2)/2`, contradicting `Θ (X k) → Θ q`. -/
theorem mvert_no_limit : ¬ ∃ q ∈ S.M, Tendsto (S.mvert Θ x) atTop (𝓝 q) := by
  rintro ⟨q, hq, hlim⟩
  obtain ⟨f, hfc, hfq, hf⟩ := S.me_local_step hL hq
  set d := Θ q - Θ (f q) with hd_def
  have hd : 0 < d := sub_pos.2 (S.me_temporal_tstep hΘ hf.self_of_nhds)
  have hgc : ContinuousAt (fun z => Θ z - Θ (f z)) q :=
    (S.me_contAt hΘ hq).sub ((S.me_contAt hΘ hfq).comp hfc)
  have hev : ∀ᶠ z in 𝓝 q, S.TStep (f z) z ∧ d / 2 < Θ z - Θ (f z) :=
    hf.and (hgc.eventually (lt_mem_nhds (half_lt_self hd)))
  have hc : 0 < min 1 (d / 2) / 2 := half_pos (lt_min one_pos (half_pos hd))
  have hev2 : ∀ᶠ k in atTop, min 1 (d / 2) / 2 < Θ (S.mvert Θ x k) - Θ (S.mvert Θ x (k + 1)) :=
    (hlim.eventually hev).mono fun k hk => by
      have h3 := S.le_pastDrop (Θ := Θ) hk.1
      have h4 : min 1 (d / 2) ≤ min 1 (Θ (S.mvert Θ x k) - Θ (f (S.mvert Θ x k))) :=
        min_le_min le_rfl hk.2.le
      have h5 := (mvert_step hL hΘ hx k).2
      linarith
  have hlim2 : Tendsto (fun k => Θ (S.mvert Θ x k) - Θ (S.mvert Θ x (k + 1))) atTop (𝓝 0) := by
    have h := (S.me_contAt hΘ hq).tendsto.comp hlim
    have h' := h.sub (h.comp (tendsto_add_atTop_nat 1))
    rw [sub_self] at h'
    exact h'
  obtain ⟨k, hk1, hk2⟩ := (hev2.and (hlim2.eventually (gt_mem_nhds hc))).exists
  linarith

/-- **The reachable-negative form (BUILT): the extension as a sequence.** -/
theorem me_past_sequence : ∃ X : ℕ → N, X 0 = x ∧ (∀ k, S.TStep (X (k + 1)) (X k)) ∧
    (∀ k, Θ (X k) ≤ Θ x) ∧ ¬ ∃ q ∈ S.M, Tendsto X atTop (𝓝 q) :=
  ⟨S.mvert Θ x, rfl, fun k => (mvert_step hL hΘ hx k).1, mvert_le hL hΘ hx,
    mvert_no_limit hL hΘ hx⟩

omit hL hΘ hx

end MSpacetime

/-! ### Gluing the steps into one curve (the registered expected stop) -/

section Glue
variable {X : Type*} [TopologicalSpace X]

/-- Piece `k` as a function of `u = -t`: `γ k (k + 1 − u)`, so `u ∈ [k, k+1]` runs `γ k` over
`[0,1]` backwards in `u`, i.e. forwards in `t`. -/
noncomputable def gpiece (γ : ℕ → ℝ → X) (k : ℕ) (u : ℝ) : X := γ k (k + 1 - u)

/-- The glued curve as a function of `u = -t` (`Nat.floor` makes it piece `0` for `u < 0`). -/
noncomputable def gpoly (γ : ℕ → ℝ → X) (u : ℝ) : X := gpiece γ ⌊u⌋₊ u

variable {γ : ℕ → ℝ → X} (hj : ∀ k, γ (k + 1) 1 = γ k 0)
include hj

lemma gpoly_eq (k : ℕ) {u : ℝ} (h1 : (k:ℝ) ≤ u ∨ k = 0) (h2 : u ≤ k + 1) :
    gpoly γ u = gpiece γ k u := by
  rcases h2.lt_or_eq with h2 | h2
  · have hk : ⌊u⌋₊ = k := by
      by_cases hu : 0 ≤ u
      · rw [Nat.floor_eq_iff hu]
        rcases h1 with h1 | h1
        · exact ⟨h1, h2⟩
        · subst h1; exact ⟨by simpa using hu, h2⟩
      · rw [Nat.floor_eq_zero.2 (by linarith)]
        rcases h1 with h1 | h1
        · exact absurd (le_trans (Nat.cast_nonneg k) h1) hu
        · exact h1.symm
    rw [gpoly, hk]
  · have hk : ⌊u⌋₊ = k + 1 := by rw [h2]; exact_mod_cast Nat.floor_natCast (k + 1)
    rw [gpoly, hk, gpiece, gpiece, h2]
    have e1 : ((k + 1 : ℕ) : ℝ) + 1 - ((k:ℝ) + 1) = 1 := by push_cast; ring
    have e2 : (k : ℝ) + 1 - ((k:ℝ) + 1) = 0 := by ring
    rw [e1, e2, hj]

lemma gpoly_continuous (hc : ∀ k, Continuous (γ k)) : Continuous (gpoly γ) := by
  have hpc : ∀ k, Continuous (gpiece γ k) := fun k =>
    (hc k).comp (continuous_const.sub continuous_id)
  rw [continuous_iff_continuousAt]
  intro u
  by_cases hu1 : u < 1
  · refine (hpc 0).continuousAt.congr ?_
    filter_upwards [Iio_mem_nhds hu1] with v hv
    exact (gpoly_eq hj 0 (Or.inr rfl) (by simpa using hv.le)).symm
  set n := ⌊u⌋₊ with hn
  have hnu : (n:ℝ) ≤ u := Nat.floor_le (by linarith)
  have hun : u < n + 1 := Nat.lt_floor_add_one u
  by_cases hne : (n:ℝ) < u
  · refine (hpc n).continuousAt.congr ?_
    filter_upwards [Ioo_mem_nhds hne hun] with v hv
    exact (gpoly_eq hj n (Or.inl hv.1.le) hv.2.le).symm
  have hequ : u = n := le_antisymm (not_lt.1 hne) hnu
  have hn1 : 1 ≤ n := by
    by_contra h
    have : n = 0 := by omega
    rw [this] at hequ; norm_num at hequ; linarith
  obtain ⟨k, hk⟩ : ∃ k, n = k + 1 := ⟨n - 1, by omega⟩
  rw [hk] at hequ
  push_cast at hequ
  have hA : ContinuousWithinAt (gpoly γ) (Icc (k:ℝ) (k + 1)) u :=
    (hpc k).continuousWithinAt.congr
      (fun v hv => gpoly_eq hj k (Or.inl hv.1) hv.2) (gpoly_eq hj k (Or.inl (by linarith)) hequ.le)
  have hB : ContinuousWithinAt (gpoly γ) (Icc ((k:ℝ) + 1) (k + 1 + 1)) u :=
    (hpc (k + 1)).continuousWithinAt.congr
      (fun v hv => gpoly_eq hj (k + 1) (Or.inl (by push_cast; exact hv.1))
        (by push_cast; exact hv.2))
      (gpoly_eq hj (k + 1) (Or.inl (by push_cast; linarith)) (by push_cast; linarith))
  refine (hA.union hB).continuousAt (mem_of_superset (Ioo_mem_nhds (a := (k:ℝ))
    (b := k + 1 + 1) (by linarith) (by linarith)) fun v hv => ?_)
  rcases le_total v (k + 1) with h | h
  · exact Or.inl ⟨hv.1.le, h⟩
  · exact Or.inr ⟨h, hv.2.le⟩

end Glue

namespace MSpacetime

/-- Velocities agree for curves agreeing near `t`. -/
lemma vel_congr {γ₁ γ₂ : ℝ → N} {t : ℝ} (h : γ₁ =ᶠ[𝓝 t] γ₂) :
    vel (E := E) γ₁ t = vel (E := E) γ₂ t := by
  unfold vel; rw [h.mfderiv_eq]; rfl

/-- The velocity of a translate `s ↦ γ (c + s)`. -/
lemma vel_comp_add {γ : ℝ → N} {c t : ℝ} (hγ : MDifferentiableAt 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ (c + t)) :
    vel (E := E) (fun s => γ (c + s)) t = vel (E := E) γ (c + t) := by
  have hτ : MDifferentiableAt 𝓘(ℝ, ℝ) 𝓘(ℝ, ℝ) (fun s : ℝ => c + s) t :=
    mdifferentiableAt_iff_differentiableAt.2 (differentiableAt_id.const_add c)
  have e : (fun s => γ (c + s)) = γ ∘ (fun s => c + s) := rfl
  have e2 : mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, ℝ) (fun s : ℝ => c + s) t (1 : ℝ) = 1 := by
    rw [mfderiv_eq_fderiv]
    show fderiv ℝ (fun s : ℝ => c + s) t 1 = 1
    rw [((hasDerivAt_id' t).const_add c).hasFDerivAt.fderiv]; simp
  unfold vel; rw [e, mfderiv_comp t hγ hτ]
  change mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ (c + t)
    (mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, ℝ) (fun s : ℝ => c + s) t (1 : ℝ)) = _
  rw [e2]; rfl

variable {S : MSpacetime E N}
variable (hL : S.LocallyOneChart) {Θ : N → ℝ} (hΘ : S.IsTemporalOn S.M Θ) {x : N} (hx : x ∈ S.M)
include hL hΘ hx

/-- **The past extension on `N` (BUILT, gluing included).** For `Θ` temporal on `M` and
`LocallyOneChart`, every `x ∈ M` is the endpoint of a continuous `p : ℝ → N`, `p 0 = x`, inside `M`
on `t ≤ 0` with `Θ (p t) < Θ x` for `t < 0`, `ContMDiff` with future-timelike `mfderiv` velocity off
the integers on `t < 0`, and with no past limit in `M`. Piece `k` is the `k`-th `TStep_N` of
`me_past_sequence`, traversed on `[−k−1, −k]`. -/
theorem me_past_extension :
    ∃ p : ℝ → N, Continuous p ∧ p 0 = x ∧ (∀ t ≤ 0, p t ∈ S.M) ∧ (∀ t < 0, Θ (p t) < Θ x) ∧
      (∀ t < 0, t ∉ range (Int.cast : ℤ → ℝ) →
        ContMDiffAt 𝓘(ℝ, ℝ) 𝓘(ℝ, E) 1 p t ∧ S.FutTimelike (p t) (vel p t)) ∧
      ¬ ∃ q ∈ S.M, Tendsto p atBot (𝓝 q) := by
  have hstep : ∀ k, S.TStep (S.mvert Θ x (k + 1)) (S.mvert Θ x k) := fun k =>
    (mvert_step hL hΘ hx k).1
  choose γ hγ h0 h1 hγt using hstep
  have hj : ∀ k, γ (k + 1) 1 = γ k 0 := fun k => by rw [h1, h0]
  have hpk : ∀ k : ℕ, gpoly γ (k : ℝ) = S.mvert Θ x k := fun k => by
    rw [gpoly_eq hj k (Or.inl le_rfl) (by linarith), gpiece,
      show (k : ℝ) + 1 - k = 1 by ring, h1]
  refine ⟨fun t => gpoly γ (-t),
    (gpoly_continuous hj fun k => (hγ k).continuous).comp continuous_neg, ?_, ?_, ?_, ?_, ?_⟩
  · show gpoly γ (-0) = x
    rw [neg_zero]; exact_mod_cast hpk 0
  · intro t ht
    set u := -t
    have hu : 0 ≤ u := by simp [u]; linarith
    set k := ⌊u⌋₊
    have hk1 : (k:ℝ) ≤ u := Nat.floor_le hu
    have hk2 : u < k + 1 := Nat.lt_floor_add_one u
    show gpoly γ u ∈ S.M
    rw [gpoly_eq hj k (Or.inl hk1) hk2.le, gpiece]
    exact (hγt k _ ⟨by linarith, by linarith⟩).1
  · intro t ht
    set u := -t
    have hu : 0 < u := by simp [u]; linarith
    set k := ⌈u⌉₊ - 1
    have hc1 : 1 ≤ ⌈u⌉₊ := Nat.one_le_iff_ne_zero.2 (by positivity)
    have hk : (k:ℝ) + 1 = ⌈u⌉₊ := by simp only [k]; push_cast [Nat.cast_sub hc1]; ring
    have hk1 : (k:ℝ) < u := by linarith [Nat.ceil_lt_add_one hu.le]
    have hk2 : u ≤ k + 1 := hk ▸ Nat.le_ceil u
    show Θ (gpoly γ u) < Θ x
    rw [gpoly_eq hj k (Or.inl hk1.le) hk2, gpiece]
    have hmono := S.me_temporal_strictMonoOn hΘ (hγ k) (hγt k)
    have hlt : Θ (γ k (k + 1 - u)) < Θ (γ k 1) :=
      hmono ⟨by linarith, by linarith⟩ ⟨zero_le_one, le_rfl⟩ (by linarith)
    rw [h1] at hlt
    exact hlt.trans_le (mvert_le hL hΘ hx k)
  · intro t ht hbrk
    set u := -t with hu_def
    have hu : 0 < u := by simp [u]; linarith
    set n := ⌊u⌋₊
    have hnu : (n:ℝ) ≤ u := Nat.floor_le hu.le
    have hun : u < n + 1 := Nat.lt_floor_add_one u
    have hne : (n:ℝ) < u := by
      refine lt_of_le_of_ne hnu fun h => hbrk ⟨-(n:ℤ), ?_⟩
      push_cast; rw [h, hu_def, neg_neg]
    have hev : (fun t => gpoly γ (-t)) =ᶠ[𝓝 t] fun s => γ n (((n:ℝ) + 1) + s) := by
      filter_upwards [(continuous_neg.tendsto t).eventually (Ioo_mem_nhds hne hun)] with s hs
      rw [gpoly_eq hj n (Or.inl hs.1.le) hs.2.le, gpiece, sub_neg_eq_add]
    have hsI : ((n:ℝ) + 1) + t ∈ Icc (0:ℝ) 1 := ⟨by linarith, by linarith⟩
    have hτ : ContMDiff 𝓘(ℝ, ℝ) 𝓘(ℝ, ℝ) 1 (fun s : ℝ => ((n:ℝ) + 1) + s) :=
      contMDiff_iff_contDiff.2 (contDiff_const.add contDiff_id)
    have hcm : ContMDiffAt 𝓘(ℝ, ℝ) 𝓘(ℝ, E) 1 (fun s => γ n (((n:ℝ) + 1) + s)) t :=
      ContMDiffAt.comp (g := γ n) (f := fun s : ℝ => ((n:ℝ) + 1) + s) t
        ((hγ n).contMDiffAt) (hτ.contMDiffAt)
    refine ⟨hcm.congr_of_eventuallyEq hev, ?_⟩
    have he : gpoly γ (-t) = γ n (((n:ℝ) + 1) + t) := hev.eq_of_nhds
    show S.FutTimelike (gpoly γ (-t)) (vel (fun t => gpoly γ (-t)) t)
    rw [vel_congr hev, vel_comp_add ((hγ n).mdifferentiableAt one_ne_zero), he]
    exact (hγt n _ hsI).2
  · rintro ⟨q, hq, hlim⟩
    refine mvert_no_limit hL hΘ hx ⟨q, hq, ?_⟩
    have h := hlim.comp (tendsto_neg_atTop_atBot.comp tendsto_natCast_atTop_atTop)
    refine h.congr fun k => ?_
    show gpoly γ (-(-(k:ℝ))) = S.mvert Θ x k
    rw [neg_neg, hpk]

omit hL hΘ hx

/-! ### Two-sided Cauchy ⇒ future Cauchy on `N` -/

variable (S) in
/-- A future-directed piecewise-`C¹` causal curve on `[0, ∞)`, future-inextendible in `U`
(the `N`-analogue of campaign 78's `FutInextCurve`, intrinsic). -/
structure FutInextCurveIn (U : Set N) where
  γ : ℝ → N
  cont : ContinuousOn γ (Ici 0)
  mem : ∀ t, 0 ≤ t → γ t ∈ U
  brk : Set ℝ
  brk_fin : ∀ a b : ℝ, (brk ∩ Icc a b).Finite
  causal : ∀ t, 0 < t → t ∉ brk →
    MDifferentiableAt 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ t ∧ S.FutCausal (γ t) (vel γ t)
  inext_future : ¬ ∃ p ∈ U, Tendsto γ atTop (𝓝 p)

variable (S) in
/-- **Cauchy temporal on `U`, future form** (intrinsic): `Θ` temporal on `U`, and every
future-inextendible causal curve in `U` from `γ 0` attains every level `a ≥ Θ (γ 0)`. -/
def FutCauchyTemporalOn (U : Set N) (Θ : N → ℝ) : Prop :=
  S.IsTemporalOn U Θ ∧
    ∀ c : S.FutInextCurveIn U, ∀ a : ℝ, Θ (c.γ 0) ≤ a → ∃ t, 0 ≤ t ∧ Θ (c.γ t) = a

/-- **Two-sided ⇒ future Cauchy on `N` (BUILT).** For `LocallyOneChart S` and an open `U ⊆ M`
(e.g. `U = D J` once `D J` is known to be open): campaign 84's two-sided `IsCauchyTemporalOn U Θ`
implies the future form. A future-inextendible `c` is glued at `0` to the past extension
`me_past_extension` of `c.γ 0` in the restriction of `S` to `U`; the glued curve is an
`InextCausalCurveIn U`, so it meets level `a` once, and since `Θ (p t) < Θ (c.γ 0) ≤ a` for `t < 0`
the hit is at `t ≥ 0`. -/
theorem me_futCauchy_of_cauchy_N (hL : S.LocallyOneChart) {U : Set N} (hU : IsOpen U)
    (hUM : U ⊆ S.M) {Θ : N → ℝ} (hΘ : S.IsCauchyTemporalOn U Θ) : S.FutCauchyTemporalOn U Θ := by
  refine ⟨hΘ.1, fun c a ha => ?_⟩
  have hL' := hL.restrict hU hUM
  have hΘ' : (S.restrictM U hU hUM).IsTemporalOn (S.restrictM U hU hUM).M Θ := hΘ.1
  obtain ⟨p, hpc, hp0, hpM, hpΘ, hpd, hpinext⟩ :=
    me_past_extension hL' hΘ' (x := c.γ 0) (c.mem 0 le_rfl)
  set γ : ℝ → N := fun t => if t ≤ 0 then p t else c.γ t with hγ
  have hγc : Continuous γ :=
    continuous_if_le (f := fun t : ℝ => t) (g := fun _ => (0:ℝ)) continuous_id continuous_const
      hpc.continuousOn c.cont fun t (ht : t = 0) => by rw [ht, hp0]
  have hγneg : ∀ t ≤ 0, γ t = p t := fun t ht => by simp [hγ, ht]
  have hγpos : ∀ t, 0 < t → γ t = c.γ t := fun t ht => by simp [hγ, not_le.2 ht]
  have hγ0 : ∀ t, 0 ≤ t → γ t = c.γ t := by
    intro t ht
    rcases ht.lt_or_eq with h | h
    · exact hγpos t h
    · rw [← h, hγneg 0 le_rfl, hp0]
  let C : S.InextCausalCurveIn U :=
    { γ := γ
      cont := hγc
      mem := fun t => by
        rcases le_or_gt t 0 with h | h
        · rw [hγneg t h]; exact hpM t h
        · rw [hγpos t h]; exact c.mem t h.le
      brk := c.brk ∪ range (Int.cast : ℤ → ℝ)
      brk_fin := fun a b => by
        rw [union_inter_distrib_right]
        exact (c.brk_fin a b).union (Spacetime.int_brk_fin a b)
      causal := fun t ht => by
        have ht0 : t ≠ 0 := fun h => ht (Or.inr ⟨0, by simp [h]⟩)
        rcases lt_or_gt_of_ne ht0 with h | h
        · have hev : γ =ᶠ[𝓝 t] p := by
            filter_upwards [Iio_mem_nhds h] with s hs using hγneg s hs.le
          obtain ⟨hd, hft⟩ := hpd t h fun hb => ht (Or.inr hb)
          refine ⟨(hd.mdifferentiableAt one_ne_zero).congr_of_eventuallyEq hev, ?_⟩
          rw [vel_congr hev, hγneg t h.le]; exact ⟨hft.1.le, hft.2⟩
        · have hev : γ =ᶠ[𝓝 t] c.γ := by
            filter_upwards [Ioi_mem_nhds h] with s hs using hγpos s hs
          obtain ⟨hd, hft⟩ := c.causal t h fun hb => ht (Or.inl hb)
          refine ⟨hd.congr_of_eventuallyEq hev, ?_⟩
          rw [vel_congr hev, hγpos t h]; exact hft
      inext_future := by
        rintro ⟨q, hq, hlim⟩
        refine c.inext_future ⟨q, hq, hlim.congr' ?_⟩
        filter_upwards [eventually_gt_atTop 0] with s hs using hγpos s hs
      inext_past := by
        rintro ⟨q, hq, hlim⟩
        refine hpinext ⟨q, hq, hlim.congr' ?_⟩
        filter_upwards [eventually_le_atBot 0] with s hs using hγneg s hs }
  obtain ⟨t, ht, -⟩ := hΘ.2 C a
  change Θ (γ t) = a at ht
  rcases lt_or_ge t 0 with h | h
  · rw [hγneg t h.le] at ht
    have := hpΘ t h
    linarith
  · exact ⟨t, h, by rw [← hγ0 t h]; exact ht⟩

end MSpacetime


/-! ## Copied (campaign 86, `ManifoldLocalKit.lean`): the local kit on `N` -/

/-! ### Piece 1: restriction and reparametrisation -/

/-- The velocity of an affine reparametrisation `s ↦ γ (a + b s)` is `b • γ'(a + b t)`. -/
lemma mk_vel_affine {γ : ℝ → N} {a b t : ℝ}
    (hγ : MDifferentiableAt 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ (a + b * t)) :
    MSpacetime.vel (E := E) (fun s => γ (a + b * s)) t = b • MSpacetime.vel (E := E) γ (a + b * t) := by
  have hτd : HasDerivAt (fun s : ℝ => a + b * s) b t := by
    simpa using ((hasDerivAt_id t).const_mul b).const_add a
  have hτ : MDifferentiableAt 𝓘(ℝ, ℝ) 𝓘(ℝ, ℝ) (fun s : ℝ => a + b * s) t :=
    mdifferentiableAt_iff_differentiableAt.2 hτd.differentiableAt
  have e : (fun s => γ (a + b * s)) = γ ∘ (fun s => a + b * s) := rfl
  have e2 : mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, ℝ) (fun s : ℝ => a + b * s) t (1 : ℝ) = b • (1 : ℝ) := by
    rw [mfderiv_eq_fderiv]
    show fderiv ℝ (fun s : ℝ => a + b * s) t 1 = b • (1 : ℝ)
    rw [hτd.hasFDerivAt.fderiv]; simp
  unfold MSpacetime.vel; rw [e, mfderiv_comp t hγ hτ]
  change mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ (a + b * t)
    (mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, ℝ) (fun s : ℝ => a + b * s) t (1 : ℝ)) = _
  rw [e2]
  exact (mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ (a + b * t)).map_smul b (1 : ℝ)

/-- **Restriction (generic).** A `C¹` curve with a cone-type property `P` (closed under positive
rescaling) on `[a,b]`, inside `W`, reparametrised as `s ↦ γ (a + (b − a) s)`, is a curve with
property `P` on `[0,1]`, inside `W`, from `γ a` to `γ b`. -/
lemma mk_restrict_curve {P : N → E → Prop} (hP : ∀ x v (c : ℝ), 0 < c → P x v → P x (c • v))
    {W : Set N} {γ : ℝ → N} (hγ : ContMDiff 𝓘(ℝ, ℝ) 𝓘(ℝ, E) 1 γ) {a b : ℝ} (hab : a < b)
    (ht : ∀ t ∈ Icc a b, γ t ∈ W ∧ P (γ t) (MSpacetime.vel γ t)) :
    ∃ γ' : ℝ → N, ContMDiff 𝓘(ℝ, ℝ) 𝓘(ℝ, E) 1 γ' ∧ γ' 0 = γ a ∧ γ' 1 = γ b ∧
      ∀ t ∈ Icc (0:ℝ) 1, γ' t ∈ W ∧ P (γ' t) (MSpacetime.vel γ' t) := by
  have hτ : ContMDiff 𝓘(ℝ, ℝ) 𝓘(ℝ, ℝ) 1 (fun s : ℝ => a + (b - a) * s) :=
    contMDiff_iff_contDiff.2 (contDiff_const.add (contDiff_const.mul contDiff_id))
  refine ⟨fun s => γ (a + (b - a) * s), hγ.comp hτ, by simp, by simp, fun t htI => ?_⟩
  have hba : 0 < b - a := sub_pos.2 hab
  have hm : a + (b - a) * t ∈ Icc a b :=
    ⟨by nlinarith [htI.1], by nlinarith [htI.2]⟩
  obtain ⟨hW, hPt⟩ := ht _ hm
  refine ⟨hW, ?_⟩
  rw [mk_vel_affine ((hγ _).mdifferentiableAt one_ne_zero)]
  exact hP _ _ _ hba hPt

/-- A point of `[0,1]` has a neighbourhood mapped into an open `W ∋ γ s`. -/
lemma mk_near {X : Type*} [TopologicalSpace X] {γ : ℝ → X} (hγ : Continuous γ) {W : Set X}
    (hW : IsOpen W) {s : ℝ} (hs : γ s ∈ W) : ∃ δ > 0, ∀ t, |t - s| < δ → γ t ∈ W := by
  obtain ⟨δ, hδ, h⟩ := Metric.isOpen_iff.1 (hW.preimage hγ) s hs
  exact ⟨δ, hδ, fun t ht => h (by rwa [mem_ball, Real.dist_eq])⟩

namespace MSpacetime
variable (S : MSpacetime E N)

lemma restrictM_cstep {U : Set N} {hU : IsOpen U} {hUM : U ⊆ S.M} {x y : N}
    (h : (S.restrictM U hU hUM).CStep x y) : S.CStep x y := by
  obtain ⟨γ, hγ, h0, h1, ht⟩ := h
  exact ⟨γ, hγ, h0, h1, fun t htI => ⟨hUM (ht t htI).1, (ht t htI).2⟩⟩

lemma restrictM_chr {U : Set N} {hU : IsOpen U} {hUM : U ⊆ S.M} {x y : N}
    (h : (S.restrictM U hU hUM).Chr x y) : S.Chr x y := by
  induction h with
  | single h => exact Relation.TransGen.single (S.restrictM_tstep h)
  | tail _ h ih => exact ih.tail (S.restrictM_tstep h)

variable {S}

/-- **Piece 1, `TStep` (BUILT).** A sub-arc `[a,b] ⊆ [0,1]` (`a < b`) of a timelike step's
curve, reparametrised onto `[0,1]`, is a `TStep_N (γ a) (γ b)`. -/
theorem mk_tstep_sub {γ : ℝ → N} (hγ : ContMDiff 𝓘(ℝ, ℝ) 𝓘(ℝ, E) 1 γ)
    (ht : ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ S.M ∧ S.FutTimelike (γ t) (vel γ t)) {a b : ℝ}
    (ha : 0 ≤ a) (hab : a < b) (hb : b ≤ 1) : S.TStep (γ a) (γ b) :=
  mk_restrict_curve (P := S.FutTimelike) (W := S.M) (fun _ _ _ hc h => S.futTimelike_smul hc h) hγ hab
    fun t h => ht t ⟨ha.trans h.1, h.2.trans hb⟩

/-- **Piece 1, `CStep` (BUILT).** -/
theorem mk_cstep_sub {γ : ℝ → N} (hγ : ContMDiff 𝓘(ℝ, ℝ) 𝓘(ℝ, E) 1 γ)
    (ht : ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ S.M ∧ S.FutCausal (γ t) (vel γ t)) {a b : ℝ}
    (ha : 0 ≤ a) (hab : a < b) (hb : b ≤ 1) : S.CStep (γ a) (γ b) :=
  mk_restrict_curve (P := S.FutCausal) (W := S.M) (fun _ _ _ hc h => S.futCausal_smul hc h) hγ hab
    fun t h => ht t ⟨ha.trans h.1, h.2.trans hb⟩

/-- Piece 1 inside a patch `W`: the sub-arc is a step of `S.restrictM W`. -/
theorem mk_tstep_sub_in {W : Set N} (hW : IsOpen W) (hWM : W ⊆ S.M) {γ : ℝ → N}
    (hγ : ContMDiff 𝓘(ℝ, ℝ) 𝓘(ℝ, E) 1 γ)
    (ht : ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ S.M ∧ S.FutTimelike (γ t) (vel γ t)) {a b : ℝ}
    (ha : 0 ≤ a) (hab : a < b) (hb : b ≤ 1) (hγW : ∀ t ∈ Icc a b, γ t ∈ W) :
    (S.restrictM W hW hWM).TStep (γ a) (γ b) :=
  mk_restrict_curve (P := (S.restrictM W hW hWM).FutTimelike) (W := W) (fun _ _ _ hc h => (S.restrictM W hW hWM).futTimelike_smul hc h) hγ hab
    fun t h => ⟨hγW t h, (ht t ⟨ha.trans h.1, h.2.trans hb⟩).2⟩

theorem mk_cstep_sub_in {W : Set N} (hW : IsOpen W) (hWM : W ⊆ S.M) {γ : ℝ → N}
    (hγ : ContMDiff 𝓘(ℝ, ℝ) 𝓘(ℝ, E) 1 γ)
    (ht : ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ S.M ∧ S.FutCausal (γ t) (vel γ t)) {a b : ℝ}
    (ha : 0 ≤ a) (hab : a < b) (hb : b ≤ 1) (hγW : ∀ t ∈ Icc a b, γ t ∈ W) :
    (S.restrictM W hW hWM).CStep (γ a) (γ b) :=
  mk_restrict_curve (P := (S.restrictM W hW hWM).FutCausal) (W := W) (fun _ _ _ hc h => (S.restrictM W hW hWM).futCausal_smul hc h) hγ hab
    fun t h => ⟨hγW t h, (ht t ⟨ha.trans h.1, h.2.trans hb⟩).2⟩

/-- **Piece 1, as registered (BUILT).** A `TStep_N x y` has a continuous curve `γ` from `x` to
`y` with `TStep_N (γ s) y` for every `s ∈ [0,1)` and `TStep_N x (γ s)` for `s ∈ (0,1]`; so
`x ≪ y` has points `w = γ s ≪ y` arbitrarily close to `y` (and to `x`). -/
theorem mk_tstep_restrict {x y : N} (h : S.TStep x y) :
    ∃ γ : ℝ → N, Continuous γ ∧ γ 0 = x ∧ γ 1 = y ∧
      (∀ s ∈ Ico (0:ℝ) 1, S.TStep (γ s) y) ∧ ∀ s ∈ Ioc (0:ℝ) 1, S.TStep x (γ s) := by
  obtain ⟨γ, hγ, h0, h1, ht⟩ := h
  refine ⟨γ, hγ.continuous, h0, h1, fun s hs => ?_, fun s hs => ?_⟩
  · have := mk_tstep_sub hγ ht hs.1 hs.2 le_rfl; rwa [h1] at this
  · have := mk_tstep_sub hγ ht le_rfl hs.1 hs.2; rwa [h0] at this

/-! ### Each point's `OneChart` patch -/

variable (S) in
/-- **The patch of `p`** (from `LocallyOneChart`, as in campaign 85's `me_local_step`): an open
`W ∋ p` inside `M` with `S.restrictM W` `OneChart` at `p` (in `p`'s own chart). -/
theorem mk_patch (hL : S.LocallyOneChart) {p : N} (hp : p ∈ S.M) :
    ∃ W : Set N, ∃ hW : IsOpen W, ∃ hWM : W ⊆ S.M, p ∈ W ∧ (S.restrictM W hW hWM).OneChart p := by
  obtain ⟨U, hU, hpU, -, hg, hT⟩ := hL p hp
  have hcs : ContinuousOn (extChartAt 𝓘(ℝ, E) p) (chartAt E p).source := by
    rw [← extChartAt_source (I := 𝓘(ℝ, E))]; exact continuousOn_extChartAt p
  set W : Set N := ((chartAt E p).source ∩ extChartAt 𝓘(ℝ, E) p ⁻¹' U) ∩ S.M with hWdef
  have hWo : IsOpen W :=
    (hcs.isOpen_inter_preimage (chartAt E p).open_source hU).inter S.isOpen_M
  have hWU : extChartAt 𝓘(ℝ, E) p '' W ⊆ U := by rintro _ ⟨x, hx, rfl⟩; exact hx.1.2
  exact ⟨W, hWo, inter_subset_right, ⟨⟨mem_chart_source E p, hpU⟩, hp⟩,
    { sub := fun x hx => hx.1.1, g_C1 := hg.mono hWU, T_cont := hT.mono hWU }⟩

/-! ### Piece 2: openness of `I⁺(x)`, `I⁻(z)` and `D J` on `N` -/

variable (S) in
/-- **`I⁺(x)` is open on `N` (BUILT).** For `x ≪ y`, the last step `b → y` is cut at `s` close to
`1`, so that `γ([s,1])` lies in `y`'s patch; `TStep (γ s) y` read in `y`'s chart, campaign 75's
`tstep_end_eventually`, and the transfer back give `TStep (γ s) y'` for `y'` near `y`. -/
theorem mk_isOpen_Ifut (hL : S.LocallyOneChart) (x : N) : IsOpen {y | S.Chr x y} := by
  refine isOpen_iff_mem_nhds.2 fun y hy => ?_
  obtain ⟨b, hxb, hby⟩ := Relation.TransGen.tail'_iff.1 hy
  have hyM := (S.tstep_mem hby).2
  obtain ⟨γ, hγ, h0, h1, ht⟩ := hby
  obtain ⟨W, hW, hWM, hyW, hC⟩ := S.mk_patch hL hyM
  obtain ⟨δ, hδ, hnear⟩ := mk_near hγ.continuous hW (s := 1) (by rw [h1]; exact hyW)
  set s : ℝ := max (1/2) (1 - δ/2) with hs
  have hs1 : s < 1 := max_lt (by norm_num) (by linarith)
  have hs0 : 0 < s := lt_max_of_lt_left (by norm_num)
  have hsW : ∀ t ∈ Icc s 1, γ t ∈ W := fun t h => hnear t (by
    rw [abs_lt]; constructor <;> linarith [h.1, h.2, le_max_right (1/2:ℝ) (1 - δ/2)])
  have hxs : S.Chr x (γ s) := by
    have := mk_tstep_sub hγ ht le_rfl hs0 hs1.le
    rw [h0] at this
    exact Relation.TransGen.tail' hxb this
  have hV := ch_tstep_NV hC (mk_tstep_sub_in hW hWM hγ ht hs0.le hs1 le_rfl hsW)
  rw [h1] at hV
  have hsrc : γ s ∈ (chartAt E y).source := hC.sub (hsW s ⟨le_rfl, hs1.le⟩)
  have hev : ∀ᶠ y' in 𝓝 y, y' ∈ (chartAt E y).source ∧
      (chartSp hC).TStep (extChartAt 𝓘(ℝ, E) y (γ s)) (extChartAt 𝓘(ℝ, E) y y') :=
    Filter.Eventually.and ((chartAt E y).open_source.mem_nhds (mem_chart_source E y))
      ((ch_contAt y (mem_chart_source E y)).tendsto.eventually
        ((chartSp hC).tstep_end_eventually hV))
  filter_upwards [hev] with y' hy'
  have h := ch_tstep_VN hC hy'.2
  rw [ch_left_inv y hsrc, ch_left_inv y hy'.1] at h
  exact Relation.TransGen.tail hxs (S.restrictM_tstep h)

variable (S) in
/-- **`I⁻(z)` is open on `N` (BUILT)**, the mirror: the first step `y → c` is cut at `s` close to
`0`, and campaign 60's `tstep_start_eventually` is used in `y`'s chart. -/
theorem mk_isOpen_Ipast (hL : S.LocallyOneChart) (z : N) : IsOpen (S.Ipast z) := by
  refine isOpen_iff_mem_nhds.2 fun y hy => ?_
  have hy : S.Chr y z := hy
  obtain ⟨c, hyc, hcz⟩ := Relation.TransGen.head'_iff.1 hy
  have hyM := (S.tstep_mem hyc).1
  obtain ⟨γ, hγ, h0, h1, ht⟩ := hyc
  obtain ⟨W, hW, hWM, hyW, hC⟩ := S.mk_patch hL hyM
  obtain ⟨δ, hδ, hnear⟩ := mk_near hγ.continuous hW (s := 0) (by rw [h0]; exact hyW)
  set s : ℝ := min (1/2) (δ/2) with hs
  have hs1 : s < 1 := lt_of_le_of_lt (min_le_left _ _) (by norm_num)
  have hs0 : 0 < s := lt_min (by norm_num) (by linarith)
  have hsW : ∀ t ∈ Icc 0 s, γ t ∈ W := fun t h => hnear t (by
    rw [abs_lt]; constructor <;> linarith [h.1, h.2, min_le_right (1/2:ℝ) (δ/2)])
  have hsz : S.Chr (γ s) z := by
    have := mk_tstep_sub hγ ht hs0.le hs1 le_rfl
    rw [h1] at this
    exact Relation.TransGen.head' this hcz
  have hV := ch_tstep_NV hC (mk_tstep_sub_in hW hWM hγ ht le_rfl hs0 hs1.le hsW)
  rw [h0] at hV
  have hsrc : γ s ∈ (chartAt E y).source := hC.sub (hsW s ⟨hs0.le, le_rfl⟩)
  have hev : ∀ᶠ y' in 𝓝 y, y' ∈ (chartAt E y).source ∧
      (chartSp hC).TStep (extChartAt 𝓘(ℝ, E) y y') (extChartAt 𝓘(ℝ, E) y (γ s)) :=
    Filter.Eventually.and ((chartAt E y).open_source.mem_nhds (mem_chart_source E y))
      ((ch_contAt y (mem_chart_source E y)).tendsto.eventually
        ((chartSp hC).tstep_start_eventually hV))
  filter_upwards [hev] with y' hy'
  have h := ch_tstep_VN hC hy'.2
  rw [ch_left_inv y hsrc, ch_left_inv y hy'.1] at h
  exact Relation.TransGen.head (S.restrictM_tstep h) hsz

variable (S) in
/-- **`D J = I⁻(J)` is open on `N` (BUILT)**, for every `J`: what campaign 85's
`me_futCauchy_of_cauchy_N` needs for `U = D J`. -/
theorem mk_isOpen_D (hL : S.LocallyOneChart) (J : Set N) : IsOpen (S.D J) :=
  isOpen_biUnion fun z _ => S.mk_isOpen_Ipast hL z

variable (S) in
/-- `q ∈ closure D ⟹ I⁻(q) ⊆ D` on `N` (campaign 75's step 1, through `mk_isOpen_Ifut`). -/
theorem mk_Ipast_subset_D (hL : S.LocallyOneChart) {J : Set N} {q : N}
    (hq : q ∈ closure (S.D J)) : S.Ipast q ⊆ S.D J := by
  intro x hx
  obtain ⟨d, hd, hdD⟩ := mem_closure_iff_nhds.1 hq _ ((S.mk_isOpen_Ifut hL x).mem_nhds hx)
  obtain ⟨j, hj, hdj⟩ := mem_iUnion₂.1 hdD
  exact mem_iUnion₂.2 ⟨j, hj, Relation.TransGen.trans hd hdj⟩

end MSpacetime

/-! ### Piece 3: the short future step near `q` (`V` side: a two-sided tube) -/

namespace Spacetime
variable (S : Spacetime V)

/-- `Safe2 y ℓ`: on `r ∈ [-ℓ, ℓ]`, `y + r • T y ∈ M` and `T y` is future-timelike there. -/
def Safe2 (y : V) (ℓ : ℝ) : Prop :=
  ∀ r ∈ Icc (-ℓ) ℓ, S.seg y r ∈ S.M ∧ S.FutTimelike (S.seg y r) (S.T y)

/-- **Tube lemma, two-sided** (campaign 78's `safe_uniform` with `hl_seg_timelike2`). -/
lemma safe2_uniform {x : V} (hx : x ∈ S.M) : ∃ ℓ > 0, ∀ᶠ y in 𝓝 x, S.Safe2 y ℓ := by
  obtain ⟨ε, hε0, hε⟩ := S.hl_seg_timelike2 hx
  refine ⟨ε, hε0, ?_⟩
  have hc : ∀ r : ℝ, ContinuousAt (fun z : V × ℝ => (S.seg z.1 z.2, S.T z.1)) (x, r) := fun r =>
    (continuousAt_fst.add (continuousAt_snd.smul ((S.contAt_T hx).comp continuousAt_fst))).prodMk
      ((S.contAt_T hx).comp continuousAt_fst)
  exact isCompact_Icc.eventually_forall_of_forall_eventually
    (P := fun y r => S.seg y r ∈ S.M ∧ S.FutTimelike (S.seg y r) (S.T y))
    fun r hr => (hc r).preimage_mem_nhds (S.isOpen_timelikePairs.mem_nhds (hε r hr))

end Spacetime

namespace MSpacetime
variable (S : MSpacetime E N)

/-- **Piece 3: the local future step (BUILT)**, campaign 85's `me_local_step` with `+T`: for
`q ∈ M` there is `f`, continuous at `q`, with `f q ∈ M` and `TStep_N x (f x)` for all `x` near `q`;
`f x = φ_q⁻¹(φ_q x + ℓ T_V(φ_q x))` in `q`'s patch. -/
theorem mk_local_step_fut (hL : S.LocallyOneChart) {q : N} (hq : q ∈ S.M) :
    ∃ f : N → N, ContinuousAt f q ∧ f q ∈ S.M ∧ ∀ᶠ x in 𝓝 q, S.TStep x (f x) := by
  obtain ⟨W, hW, hWM, hqW, hC⟩ := S.mk_patch hL hq
  set Sp := chartSp hC with hSp
  have huM : extChartAt 𝓘(ℝ, E) q q ∈ Sp.M := ⟨q, hqW, rfl⟩
  obtain ⟨ℓ, hℓ, hsafe⟩ := Sp.safe2_uniform huM
  have hmem : Sp.seg (extChartAt 𝓘(ℝ, E) q q) ℓ ∈ Sp.M :=
    (hsafe.self_of_nhds ℓ ⟨by linarith, le_rfl⟩).1
  obtain ⟨z, hzW, hze⟩ := hmem
  have htgt : Sp.seg (extChartAt 𝓘(ℝ, E) q q) ℓ ∈ (extChartAt 𝓘(ℝ, E) q).target := by
    rw [← hze]; exact ch_mem_target q (hC.sub hzW)
  have h1 : ContinuousAt (extChartAt 𝓘(ℝ, E) q) q := ch_contAt q (mem_chart_source E q)
  refine ⟨fun x => (extChartAt 𝓘(ℝ, E) q).symm (Sp.seg (extChartAt 𝓘(ℝ, E) q x) ℓ), ?_, ?_, ?_⟩
  · have h2 : ContinuousAt (fun x => Sp.seg (extChartAt 𝓘(ℝ, E) q x) ℓ) q := by
      show ContinuousAt (fun x => extChartAt 𝓘(ℝ, E) q x + ℓ • Sp.T (extChartAt 𝓘(ℝ, E) q x)) q
      exact h1.add (continuousAt_const.smul ((Sp.contAt_T huM).comp h1))
    exact ContinuousAt.comp (g := (extChartAt 𝓘(ℝ, E) q).symm)
      (f := fun x => Sp.seg (extChartAt 𝓘(ℝ, E) q x) ℓ)
      ((continuousOn_extChartAt_symm q).continuousAt
        ((isOpen_extChartAt_target q).mem_nhds htgt)) h2
  · show (extChartAt 𝓘(ℝ, E) q).symm (Sp.seg (extChartAt 𝓘(ℝ, E) q q) ℓ) ∈ S.M
    rw [← hze, ch_left_inv q (hC.sub hzW)]; exact hWM hzW
  · have hev : ∀ᶠ x in 𝓝 q, x ∈ (chartAt E q).source ∧ Sp.Safe2 (extChartAt 𝓘(ℝ, E) q x) ℓ :=
      Filter.Eventually.and ((chartAt E q).open_source.mem_nhds (mem_chart_source E q))
        (h1.tendsto.eventually hsafe)
    filter_upwards [hev] with x hx
    have hst := Sp.seg_tstep hx.2 (by linarith : -ℓ ≤ 0) hℓ le_rfl
    rw [Spacetime.seg_zero] at hst
    have h := ch_tstep_VN hC hst
    rw [ch_left_inv q hx.1] at h
    exact S.restrictM_tstep h

/-! ### Piece 4: the curve into a point -/

/-- **Piece 4: the curve into `q` (BUILT).** In `q`'s patch, `c t = φ_q⁻¹(φ_q q − ε e^{−t} T_V)`
(campaign 75's `hl_curve`, transferred): `c t → q`, for `t ≥ 0` the points lie in `M`, differ
from `q`, satisfy `c t ≪ q` and `c t ≪ c t'` (`t < t'`), and `c` is manifold-differentiable with
future-timelike `mfderiv` velocity. -/
theorem mk_curve_into (hL : S.LocallyOneChart) {q : N} (hq : q ∈ S.M) :
    ∃ c : ℝ → N, Tendsto c atTop (𝓝 q) ∧ (∀ t, 0 ≤ t → c t ∈ S.M ∧ c t ≠ q) ∧
      (∀ t, 0 ≤ t → S.Chr (c t) q) ∧ (∀ t t', 0 ≤ t → t < t' → S.Chr (c t) (c t')) ∧
      ∀ t, 0 ≤ t → MDifferentiableAt 𝓘(ℝ, ℝ) 𝓘(ℝ, E) c t ∧ S.FutTimelike (c t) (vel c t) := by
  obtain ⟨W, hW, hWM, hqW, hC⟩ := S.mk_patch hL hq
  set Sp := chartSp hC with hSp
  set u₀ := extChartAt 𝓘(ℝ, E) q q with hu₀
  have huM : u₀ ∈ Sp.M := ⟨q, hqW, rfl⟩
  obtain ⟨ε, hε0, hε⟩ := Sp.seg_timelike huM
  set r : ℝ → ℝ := fun t => -ε * Real.exp (-t) with hr
  have hr_mem : ∀ t, 0 ≤ t → -ε ≤ r t ∧ r t < 0 := by
    intro t ht
    have h1 : Real.exp (-t) ≤ 1 := Real.exp_le_one_iff.2 (by linarith)
    have h2 : 0 < Real.exp (-t) := Real.exp_pos _
    constructor <;> simp only [hr] <;> nlinarith
  have hr_lt : ∀ t t', t < t' → r t < r t' := by
    intro t t' h
    have : Real.exp (-t') < Real.exp (-t) := Real.exp_lt_exp.2 (by linarith)
    simp only [hr]; nlinarith
  set β : ℝ → E := fun t => Sp.seg u₀ (r t) with hβ
  have hβmem : ∀ t, 0 ≤ t → β t ∈ (extChartAt 𝓘(ℝ, E) q).target ∧
      (extChartAt 𝓘(ℝ, E) q).symm (β t) ∈ W := by
    intro t ht
    obtain ⟨z, hzW, hz⟩ := (hε _ ⟨(hr_mem t ht).1, (hr_mem t ht).2.le⟩).1
    have hzs := hC.sub hzW
    refine ⟨?_, ?_⟩
    · show Sp.seg u₀ (r t) ∈ _
      rw [← hz]; exact ch_mem_target q hzs
    · show (extChartAt 𝓘(ℝ, E) q).symm (Sp.seg u₀ (r t)) ∈ W
      rw [← hz, ch_left_inv q hzs]; exact hzW
  have hqs : q ∈ (chartAt E q).source := mem_chart_source E q
  have hderiv : ∀ t, HasDerivAt β ((ε * Real.exp (-t)) • Sp.T u₀) t := by
    intro t
    have h := ((((hasDerivAt_neg t).exp).const_mul (-ε)).smul_const (Sp.T u₀)).const_add u₀
    have e : ε * Real.exp (-t) = -ε * (Real.exp (-t) * -1) := by ring
    rw [e]; exact h
  refine ⟨fun t => (extChartAt 𝓘(ℝ, E) q).symm (β t), ?_, fun t ht => ⟨hWM (hβmem t ht).2, ?_⟩,
    fun t ht => ?_, fun t t' ht htt => ?_, fun t ht => ?_⟩
  · have hlim : Tendsto β atTop (𝓝 u₀) := by
      have h := ((tendsto_const_nhds (x := -ε)).mul
        Real.tendsto_exp_neg_atTop_nhds_zero).smul_const (Sp.T u₀) |>.const_add u₀
      simpa [Spacetime.seg, hβ, hr] using h
    have hc : ContinuousAt (extChartAt 𝓘(ℝ, E) q).symm u₀ :=
      (continuousOn_extChartAt_symm q).continuousAt
        ((isOpen_extChartAt_target q).mem_nhds (mem_extChartAt_target q))
    have h := hc.tendsto.comp hlim
    rwa [hu₀, extChartAt_to_inv] at h
  · intro he
    have he' : (extChartAt 𝓘(ℝ, E) q).symm (β t) = q := he
    have h1 : β t = u₀ := by
      have := ch_right_inv q (hβmem t ht).1
      rw [he'] at this; exact this.symm
    have h2 : r t • Sp.T u₀ = 0 := by
      have : u₀ + r t • Sp.T u₀ = u₀ + 0 := by rw [add_zero]; exact h1
      exact add_left_cancel this
    have h3 : Sp.T u₀ = 0 := (smul_eq_zero.1 h2).resolve_left (hr_mem t ht).2.ne
    have h4 := Sp.T_timelike u₀ huM
    rw [h3] at h4; simp at h4
  · have h := Sp.seg_tstep hε (hr_mem t ht).1 (hr_mem t ht).2 le_rfl
    rw [Spacetime.seg_zero] at h
    have h' := ch_tstep_VN hC h
    rw [hu₀, ch_left_inv q hqs] at h'
    exact Relation.TransGen.single (S.restrictM_tstep h')
  · have h := Sp.seg_tstep hε (hr_mem t ht).1 (hr_lt t t' htt) (hr_mem t' (by linarith)).2.le
    exact Relation.TransGen.single (S.restrictM_tstep (ch_tstep_VN hC h))
  · obtain ⟨hmd, hv⟩ := ch_vel_symm q (hderiv t).differentiableAt (hβmem t ht).1
    refine ⟨hmd, ?_⟩
    have hft : Sp.FutTimelike (β t) (deriv β t) := by
      rw [(hderiv t).deriv]
      exact Sp.futTimelike_smul (mul_pos hε0 (Real.exp_pos _))
        (hε _ ⟨(hr_mem t ht).1, (hr_mem t ht).2.le⟩).2
    have h := (futTimelike_chart' hC (hβmem t ht).1 _).1 hft
    have e : vel (fun t => (extChartAt 𝓘(ℝ, E) q).symm (β t)) t =
        dchartInv q (β t) (deriv β t) := hv
    show S.FutTimelike ((extChartAt 𝓘(ℝ, E) q).symm (β t))
      (vel (fun t => (extChartAt 𝓘(ℝ, E) q).symm (β t)) t)
    rw [e]; exact h

/-- **Piece 4, `N ∖ {q}` form (BUILT).** For `N` Hausdorff, the curve into `q` is a
future-inextendible causal curve in `M ∖ {q}`, with `c t → q`, `c t ≪ q`, `c t ≪ c t'`. -/
theorem mk_curve_inext_punctured [T2Space N] (hL : S.LocallyOneChart) {q : N} (hq : q ∈ S.M) :
    ∃ c : S.FutInextCurveIn (S.M \ {q}), Tendsto c.γ atTop (𝓝 q) ∧
      (∀ t, 0 ≤ t → S.Chr (c.γ t) q) ∧ (∀ t t', 0 ≤ t → t < t' → S.Chr (c.γ t) (c.γ t')) := by
  obtain ⟨c, hlim, hmem, hq', hcc, hd⟩ := S.mk_curve_into hL hq
  refine ⟨⟨c, fun t ht => ((hd t ht).1.continuousAt).continuousWithinAt,
    fun t ht => ⟨(hmem t ht).1, (hmem t ht).2⟩, ∅, fun a b => by simp,
    fun t ht _ => ⟨(hd t ht.le).1, (hd t ht.le).2.1.le, (hd t ht.le).2.2⟩, ?_⟩, hlim, hq', hcc⟩
  rintro ⟨p, hp, hpl⟩
  exact hp.2 (tendsto_nhds_unique hpl hlim)

/-- **Piece 4, `D` form (BUILT).** For `q ∈ M ∩ closure D \ D` (`N` Hausdorff), the curve into `q`
is a future-inextendible causal curve in `D J` (`I⁻(q) ⊆ D` by `mk_Ipast_subset_D`). -/
theorem mk_curve_inext_D [T2Space N] (hL : S.LocallyOneChart) {J : Set N} {q : N} (hq : q ∈ S.M)
    (hqcl : q ∈ closure (S.D J)) (hqD : q ∉ S.D J) :
    ∃ c : S.FutInextCurveIn (S.D J), Tendsto c.γ atTop (𝓝 q) ∧
      (∀ t, 0 ≤ t → S.Chr (c.γ t) q) ∧ (∀ t t', 0 ≤ t → t < t' → S.Chr (c.γ t) (c.γ t')) := by
  obtain ⟨c, hlim, -, hq', hcc, hd⟩ := S.mk_curve_into hL hq
  refine ⟨⟨c, fun t ht => ((hd t ht).1.continuousAt).continuousWithinAt,
    fun t ht => S.mk_Ipast_subset_D hL hqcl (hq' t ht), ∅, fun a b => by simp,
    fun t ht _ => ⟨(hd t ht.le).1, (hd t ht.le).2.1.le, (hd t ht.le).2.2⟩, ?_⟩, hlim, hq', hcc⟩
  rintro ⟨p, hp, hpl⟩
  exact hqD (tendsto_nhds_unique hpl hlim ▸ hp)

/-! ### Piece 5: push-up on `N` -/

variable {S}

/-- **Push-up inside one patch (BUILT; the registered reachable negative).** A causal step of
`S.restrictM W` (`W` a `OneChart` patch of `p`), followed by `b ≪ z` in `N`, gives `a ≪ z`: the
first step out of `b` is cut inside `W`, and campaign 60's `pushup_cstep` is applied in `p`'s
chart (`g` is locally Lipschitz there, being `C¹`). -/
theorem mk_pushup_patch {W : Set N} {hW : IsOpen W} {hWM : W ⊆ S.M} {p : N}
    (hC : (S.restrictM W hW hWM).OneChart p) {a b z : N}
    (hab : (S.restrictM W hW hWM).CStep a b) (hbz : S.Chr b z) : S.Chr a z := by
  have haW := ((S.restrictM W hW hWM).cstep_mem hab).1
  have hbW := ((S.restrictM W hW hWM).cstep_mem hab).2
  obtain ⟨c, hbc, hcz⟩ := Relation.TransGen.head'_iff.1 hbz
  obtain ⟨γ, hγ, h0, h1, ht⟩ := hbc
  obtain ⟨δ, hδ, hnear⟩ := mk_near hγ.continuous hW (s := 0) (by rw [h0]; exact hbW)
  set s : ℝ := min (1/2) (δ/2) with hs
  have hs1 : s < 1 := lt_of_le_of_lt (min_le_left _ _) (by norm_num)
  have hs0 : 0 < s := lt_min (by norm_num) (by linarith)
  have hsW : ∀ t ∈ Icc 0 s, γ t ∈ W := fun t h => hnear t (by
    rw [abs_lt]; constructor <;> linarith [h.1, h.2, min_le_right (1/2:ℝ) (δ/2)])
  have hsz : S.Chr (γ s) z := by
    have := mk_tstep_sub hγ ht hs0.le hs1 le_rfl
    rw [h1] at this
    exact Relation.TransGen.head' this hcz
  have hbs : (S.restrictM W hW hWM).TStep b (γ s) := by
    have := mk_tstep_sub_in hW hWM hγ ht le_rfl hs0 hs1.le hsW
    rwa [h0] at this
  have hV := (chartSp hC).pushup_cstep (ch_chart_lipschitz hC) (ch_cstep_NV hC hab)
    (Relation.TransGen.single (ch_tstep_NV hC hbs))
  have hN := (ch_chr_iff hC (hC.sub haW) (hC.sub (hsW s ⟨hs0.le, le_rfl⟩))).2 hV
  exact Relation.TransGen.trans (S.restrictM_chr hN) hsz

/-- **Dual push-up inside one patch (BUILT).** `x ≪ a` in `N` and a causal step `a → b` of
`S.restrictM W` give `x ≪ b` (campaign 60's `hl_pushup'` in `p`'s chart). -/
theorem mk_pushup_patch' {W : Set N} {hW : IsOpen W} {hWM : W ⊆ S.M} {p : N}
    (hC : (S.restrictM W hW hWM).OneChart p) {x a b : N} (hxa : S.Chr x a)
    (hab : (S.restrictM W hW hWM).CStep a b) : S.Chr x b := by
  have haW := ((S.restrictM W hW hWM).cstep_mem hab).1
  have hbW := ((S.restrictM W hW hWM).cstep_mem hab).2
  obtain ⟨c, hxc, hca⟩ := Relation.TransGen.tail'_iff.1 hxa
  obtain ⟨γ, hγ, h0, h1, ht⟩ := hca
  obtain ⟨δ, hδ, hnear⟩ := mk_near hγ.continuous hW (s := 1) (by rw [h1]; exact haW)
  set s : ℝ := max (1/2) (1 - δ/2) with hs
  have hs1 : s < 1 := max_lt (by norm_num) (by linarith)
  have hs0 : 0 < s := lt_max_of_lt_left (by norm_num)
  have hsW : ∀ t ∈ Icc s 1, γ t ∈ W := fun t h => hnear t (by
    rw [abs_lt]; constructor <;> linarith [h.1, h.2, le_max_right (1/2:ℝ) (1 - δ/2)])
  have hxs : S.Chr x (γ s) := by
    have := mk_tstep_sub hγ ht le_rfl hs0 hs1.le
    rw [h0] at this
    exact Relation.TransGen.tail' hxc this
  have hsa : (S.restrictM W hW hWM).TStep (γ s) a := by
    have := mk_tstep_sub_in hW hWM hγ ht hs0.le hs1 le_rfl hsW
    rwa [h1] at this
  have hV := (chartSp hC).hl_pushup' (ch_chart_lipschitz hC)
    (Relation.TransGen.single (ch_tstep_NV hC hsa))
    (Relation.ReflTransGen.single (ch_cstep_NV hC hab))
  have hN := (ch_chr_iff hC (hC.sub (hsW s ⟨le_rfl, hs1.le⟩)) (hC.sub hbW)).2 hV
  exact Relation.TransGen.trans hxs (S.restrictM_chr hN)

variable (S) in
/-- **Push-up across one `CStep_N` (BUILT).** `CStep_N x y`, `y ≪ z` ⟹ `x ≪ z`, for a step that
may cross any number of charts. No Lebesgue subdivision: campaign 60's `sInf` argument runs on
`[0,1]` directly, with the local step at `s = inf {t | α t ≪ z}` taken in `α s`'s own patch
(`mk_pushup_patch`) and openness of `I⁻(z)` on `N` (`mk_isOpen_Ipast`) forcing `s = 0`. -/
theorem mk_pushup_cstep (hL : S.LocallyOneChart) {x y z : N} (hxy : S.CStep x y)
    (hyz : S.Chr y z) : S.Chr x z := by
  obtain ⟨α, hα, h0, h1, hc⟩ := hxy
  let A : Set ℝ := {t | t ∈ Icc (0:ℝ) 1 ∧ S.Chr (α t) z}
  have h1A : (1:ℝ) ∈ A := ⟨⟨zero_le_one, le_rfl⟩, by show S.Chr (α 1) z; rw [h1]; exact hyz⟩
  have hne : A.Nonempty := ⟨1, h1A⟩
  have hbdd : BddBelow A := ⟨0, fun t ht => ht.1.1⟩
  have hs0 : 0 ≤ sInf A := le_csInf hne fun t ht => ht.1.1
  have hs1 : sInf A ≤ 1 := csInf_le hbdd h1A
  have hsA : S.Chr (α (sInf A)) z := by
    obtain ⟨W, hW, hWM, hW', hC⟩ := S.mk_patch hL (hc _ ⟨hs0, hs1⟩).1
    obtain ⟨δ, hδ, hnear⟩ := mk_near hα.continuous hW hW'
    obtain ⟨t, htA, hts⟩ := exists_lt_of_csInf_lt hne (show sInf A < sInf A + δ by linarith)
    have hst : sInf A ≤ t := csInf_le hbdd htA
    rcases hst.lt_or_eq with hst | hst
    · have hab := mk_cstep_sub_in hW hWM hα hc hs0 hst htA.1.2 fun u hu => hnear u (by
        rw [abs_lt]; constructor <;> linarith [hu.1, hu.2])
      exact mk_pushup_patch hC hab htA.2
    · rw [hst]; exact htA.2
  have hs : sInf A = 0 := by
    by_contra hne0
    have hspos : 0 < sInf A := lt_of_le_of_ne hs0 (Ne.symm hne0)
    have hev : ∀ᶠ t in 𝓝 (sInf A), S.Chr (α t) z :=
      (hα.continuous.tendsto _).eventually ((S.mk_isOpen_Ipast hL z).mem_nhds hsA)
    obtain ⟨δ, hδ, hδP⟩ := Metric.eventually_nhds_iff.1 hev
    have hm1 := min_le_left δ (sInf A)
    have hm2 := min_le_right δ (sInf A)
    have hm3 := lt_min hδ hspos
    have ht : sInf A - min δ (sInf A) / 2 ∈ A := by
      refine ⟨⟨by linarith, by linarith⟩, hδP ?_⟩
      rw [Real.dist_eq, abs_lt]; constructor <;> linarith
    have := csInf_le hbdd ht
    linarith
  rw [← h0, ← hs]; exact hsA

variable (S) in
/-- **Dual push-up across one `CStep_N` (BUILT).** `x ≪ y`, `CStep_N y z` ⟹ `x ≪ z`: the `sSup`
mirror, with `mk_pushup_patch'` and openness of `I⁺(x)` on `N`. -/
theorem mk_pushup_cstep' (hL : S.LocallyOneChart) {x y z : N} (hxy : S.Chr x y)
    (hyz : S.CStep y z) : S.Chr x z := by
  obtain ⟨α, hα, h0, h1, hc⟩ := hyz
  let A : Set ℝ := {t | t ∈ Icc (0:ℝ) 1 ∧ S.Chr x (α t)}
  have h0A : (0:ℝ) ∈ A := ⟨⟨le_rfl, zero_le_one⟩, by show S.Chr x (α 0); rw [h0]; exact hxy⟩
  have hne : A.Nonempty := ⟨0, h0A⟩
  have hbdd : BddAbove A := ⟨1, fun t ht => ht.1.2⟩
  have hs0 : 0 ≤ sSup A := le_csSup hbdd h0A
  have hs1 : sSup A ≤ 1 := csSup_le hne fun t ht => ht.1.2
  have hsA : S.Chr x (α (sSup A)) := by
    obtain ⟨W, hW, hWM, hW', hC⟩ := S.mk_patch hL (hc _ ⟨hs0, hs1⟩).1
    obtain ⟨δ, hδ, hnear⟩ := mk_near hα.continuous hW hW'
    obtain ⟨t, htA, hts⟩ := exists_lt_of_lt_csSup hne (show sSup A - δ < sSup A by linarith)
    have hst : t ≤ sSup A := le_csSup hbdd htA
    rcases hst.lt_or_eq with hst | hst
    · have hab := mk_cstep_sub_in hW hWM hα hc htA.1.1 hst hs1 fun u hu => hnear u (by
        rw [abs_lt]; constructor <;> linarith [hu.1, hu.2])
      exact mk_pushup_patch' hC htA.2 hab
    · rw [← hst]; exact htA.2
  have hs : sSup A = 1 := by
    by_contra hne1
    have hslt : sSup A < 1 := lt_of_le_of_ne hs1 hne1
    have hev : ∀ᶠ t in 𝓝 (sSup A), S.Chr x (α t) :=
      (hα.continuous.tendsto _).eventually ((S.mk_isOpen_Ifut hL x).mem_nhds hsA)
    obtain ⟨δ, hδ, hδP⟩ := Metric.eventually_nhds_iff.1 hev
    have hm1 := min_le_left δ (1 - sSup A)
    have hm2 := min_le_right δ (1 - sSup A)
    have hm3 := lt_min hδ (sub_pos.2 hslt)
    have ht : sSup A + min δ (1 - sSup A) / 2 ∈ A := by
      refine ⟨⟨by linarith, by linarith⟩, hδP ?_⟩
      rw [Real.dist_eq, abs_lt]; constructor <;> linarith
    have := le_csSup hbdd ht
    linarith
  rw [← h1, ← hs]; exact hsA

variable (S) in
/-- **Push-up on `N` (BUILT).** `x ≤ y ≪ z ⟹ x ≪ z`, for `LocallyOneChart S`. -/
theorem mk_pushup (hL : S.LocallyOneChart) {x y z : N} (hxy : S.Cau x y) (hyz : S.Chr y z) :
    S.Chr x z := by
  induction hxy using Relation.ReflTransGen.head_induction_on with
  | refl => exact hyz
  | head h _ ih => exact S.mk_pushup_cstep hL h ih

variable (S) in
/-- **Dual push-up on `N` (BUILT).** `x ≪ y ≤ z ⟹ x ≪ z`. -/
theorem mk_pushup' (hL : S.LocallyOneChart) {x y z : N} (hxy : S.Chr x y) (hyz : S.Cau y z) :
    S.Chr x z := by
  induction hyz with
  | refl => exact hxy
  | tail _ h ih => exact S.mk_pushup_cstep' hL ih h

end MSpacetime

/-! ## NEW (campaign 87): the assembly on a multi-chart `N`

Everything below is read in `N`: `hL : S.LocallyOneChart`, `[T2Space N]` (only for the curve into
a point), and campaign 84's intrinsic `D`, `𝓗⁺ = ∂_N J⁻(J)`, slices, `SublevelProper`, `KLi`/`KLs`. -/

namespace MSpacetime
variable (S : MSpacetime E N)

/-! ### Piece 1: `Θ` strictly increasing along `≪` into `D` -/

/-- `≪` into `D` starts in `D`. -/
theorem mh_D_of_chr {J : Set N} {x y : N} (h : S.Chr x y) (hy : y ∈ S.D J) : x ∈ S.D J := by
  obtain ⟨z, hz, hyz⟩ := mem_iUnion₂.1 hy
  exact mem_iUnion₂.2 ⟨z, hz, Relation.TransGen.trans h hyz⟩

/-- `𝓗⁺ ∩ D = ∅` on `N` (`D` open). -/
theorem mh_not_mem_D_of_H (hL : S.LocallyOneChart) {J : Set N} {p : N} (hp : p ∈ S.H J) :
    p ∉ S.D J := fun hpD =>
  hp.2 (interior_maximal (S.D_subset_JpastSet J) (S.mk_isOpen_D hL J) hpD)

/-- The exterior `D J` as a manifold spacetime in its own right. -/
def DspN (hL : S.LocallyOneChart) (J : Set N) : MSpacetime E N :=
  S.restrictM (S.D J) (S.mk_isOpen_D hL J) (S.D_subset_M J)

/-- **A timelike step of `N` ending in `D` runs inside `D`** (every point of its curve is `≪` its
end, by campaign 86's `mk_tstep_sub`), so it is a timelike step of `DspN`. -/
theorem mh_tstep_DspN (hL : S.LocallyOneChart) {J : Set N} {x y : N} (h : S.TStep x y)
    (hy : y ∈ S.D J) : (S.DspN hL J).TStep x y := by
  obtain ⟨γ, hγ, h0, h1, ht⟩ := h
  refine ⟨γ, hγ, h0, h1, fun t htI => ⟨?_, (ht t htI).2⟩⟩
  rcases htI.2.lt_or_eq with hlt | heq
  · have hs := mk_tstep_sub hγ ht htI.1 hlt le_rfl
    rw [h1] at hs
    exact S.mh_D_of_chr (Relation.TransGen.single hs) hy
  · rw [heq, h1]; exact hy

/-- **Piece 1 (BUILT).** A function temporal on `D` (intrinsic, `IsTemporalOn (D J)`) strictly
increases along every `≪` of `N` ending in `D`: `me_temporal_tstep` in `DspN` and induction. -/
theorem mh_temporalD_chr (hL : S.LocallyOneChart) {J : Set N} {Θ : N → ℝ}
    (hΘ : S.IsTemporalOn (S.D J) Θ) {x y : N} (h : S.Chr x y) (hy : y ∈ S.D J) : Θ x < Θ y := by
  have hΘ' : (S.DspN hL J).IsTemporalOn (S.DspN hL J).M Θ := hΘ
  induction h with
  | single h => exact (S.DspN hL J).me_temporal_tstep hΘ' (S.mh_tstep_DspN hL h hy)
  | @tail b c hxb hbc ih =>
    have hb : b ∈ S.D J := S.mh_D_of_chr (Relation.TransGen.single hbc) hy
    exact (ih hb).trans ((S.DspN hL J).me_temporal_tstep hΘ' (S.mh_tstep_DspN hL hbc hy))

/-! ### Piece 2: `hint` and `hcl` on `N` -/

/-- **The short future step on `N` (BUILT).** Every neighbourhood of `x ∈ M` contains a `y` with
`x ≪ y`: campaign 86's `mk_local_step_fut` at `x`, cut short by `mk_tstep_restrict`. -/
theorem mh_future_step (hL : S.LocallyOneChart) {x : N} (hx : x ∈ S.M) {U : Set N}
    (hU : U ∈ 𝓝 x) : ∃ y ∈ U, S.Chr x y := by
  obtain ⟨f, -, -, hev⟩ := S.mk_local_step_fut hL hx
  obtain ⟨γ, hγc, h0, -, -, hfwd⟩ := mk_tstep_restrict hev.self_of_nhds
  have hlim : Tendsto γ (𝓝 0) (𝓝 x) := by rw [← h0]; exact hγc.tendsto 0
  obtain ⟨δ, hδ, hδU⟩ := Metric.eventually_nhds_iff.1 (hlim.eventually hU)
  set s : ℝ := min (δ / 2) 1 with hs
  have hs0 : 0 < s := lt_min (by linarith) one_pos
  have hs1 : s ≤ 1 := min_le_right _ _
  refine ⟨γ s, hδU ?_, Relation.TransGen.single (hfwd s ⟨hs0, hs1⟩)⟩
  rw [Real.dist_eq, sub_zero, abs_of_pos hs0]
  exact lt_of_le_of_lt (min_le_left _ _) (by linarith)

/-- **The short past step on `N` (BUILT).** Every neighbourhood of `x ∈ M` contains a `y ≪ x`:
the tail of campaign 86's curve into `x`. -/
theorem mh_past_step (hL : S.LocallyOneChart) {x : N} (hx : x ∈ S.M) {U : Set N}
    (hU : U ∈ 𝓝 x) : ∃ y ∈ U, S.Chr y x := by
  obtain ⟨c, hlim, -, hcx, -, -⟩ := S.mk_curve_into hL hx
  obtain ⟨t, htU, ht0⟩ := ((hlim.eventually hU).and (eventually_ge_atTop 0)).exists
  exact ⟨c t, htU, hcx t ht0⟩

/-- **`hint` on `N` (BUILT).** `int J⁻(J) ⊆ D`: a short future step `x ≪ y` inside the interior,
`y ≤ z ∈ J`, and campaign 86's dual push-up `mk_pushup'`. -/
theorem mh_hint (hL : S.LocallyOneChart) {J : Set N} (hJM : J ⊆ S.M) :
    interior (S.JpastSet J) ⊆ S.D J := by
  intro x hx
  obtain ⟨y, hy, hxy⟩ := S.mh_future_step hL (S.JpastSet_subset_M hJM (interior_subset hx))
    (isOpen_interior.mem_nhds hx)
  obtain ⟨z, hz, hyz⟩ := mem_iUnion₂.1 (interior_subset hy)
  exact mem_iUnion₂.2 ⟨z, hz, S.mk_pushup' hL hxy hyz⟩

/-- `J⁻(J) ⊆ closure D` on `N`: past steps `y ≪ x ≤ z ∈ J` give `y ≪ z`, with `y → x`. -/
theorem mh_JpastSet_subset_closure_D (hL : S.LocallyOneChart) {J : Set N} (hJM : J ⊆ S.M) :
    S.JpastSet J ⊆ closure (S.D J) := by
  intro x hx
  have hxM := S.JpastSet_subset_M hJM hx
  obtain ⟨z, hz, hxz⟩ := mem_iUnion₂.1 hx
  rw [mem_closure_iff_nhds]
  intro U hU
  obtain ⟨y, hy, hyx⟩ := S.mh_past_step hL hxM hU
  exact ⟨y, hy, mem_iUnion₂.2 ⟨z, hz, S.mk_pushup' hL hyx hxz⟩⟩

/-- **`hcl` on `N` (BUILT).** `closure J⁻(J) ⊆ closure D`. -/
theorem mh_hcl (hL : S.LocallyOneChart) {J : Set N} (hJM : J ⊆ S.M) :
    closure (S.JpastSet J) ⊆ closure (S.D J) :=
  closure_minimal (S.mh_JpastSet_subset_closure_D hL hJM) isClosed_closure

/-! ### Piece 3: properness on `N` -/

/-- `Θ` (temporal on `D`) is monotone along campaign 86's curve into a point. -/
theorem mh_curve_mono (hL : S.LocallyOneChart) {J : Set N} {Θ : N → ℝ}
    (hΘ : S.IsTemporalOn (S.D J) Θ) (c : S.FutInextCurveIn (S.D J))
    (hc : ∀ t t', 0 ≤ t → t < t' → S.Chr (c.γ t) (c.γ t')) {t t' : ℝ} (ht : 0 ≤ t)
    (htt : t ≤ t') : Θ (c.γ t) ≤ Θ (c.γ t') := by
  rcases htt.lt_or_eq with h | h
  · exact (S.mh_temporalD_chr hL hΘ (hc t t' ht h) (c.mem t' (by linarith))).le
  · rw [h]

/-- **`Θ → ∞` at `q` (BUILT).** For `q ∈ M ∩ closure D \ D` and every `T'`, some neighbourhood
`U ∋ q` has `Θ > T'` on `U ∩ D`: campaign 86's curve `c` into `q` (`mk_curve_inext_D`), the future
Cauchy property gives `r = c t` with `Θ r ≥ T' + 1`, and `U = I⁺(r)` is open on `N`
(`mk_isOpen_Ifut`) and contains `q`. -/
theorem mh_blowup [T2Space N] (hL : S.LocallyOneChart) {J : Set N} {Θ : N → ℝ}
    (hΘ : S.FutCauchyTemporalOn (S.D J) Θ) {q : N} (hqM : q ∈ S.M)
    (hqcl : q ∈ closure (S.D J)) (hqD : q ∉ S.D J) (T' : ℝ) :
    ∃ U ∈ 𝓝 q, ∀ x ∈ U ∩ S.D J, T' < Θ x := by
  obtain ⟨c, -, hcq, -⟩ := S.mk_curve_inext_D hL hqM hqcl hqD
  obtain ⟨t, ht, hta⟩ := hΘ.2 c (max (T' + 1) (Θ (c.γ 0))) (le_max_right _ _)
  refine ⟨{y | S.Chr (c.γ t) y}, (S.mk_isOpen_Ifut hL _).mem_nhds (hcq t ht), fun x hx => ?_⟩
  have h := S.mh_temporalD_chr hL hΘ.1 hx.1 hx.2
  have := le_max_left (T' + 1) (Θ (c.γ 0))
  linarith

/-- **Piece 3 (BUILT): properness on `N`.** From the future Cauchy property, `hint` and
`𝓗⁺ ⊆ M`. -/
theorem mh_sublevelProper [T2Space N] (hL : S.LocallyOneChart) {J : Set N}
    (hint : interior (S.JpastSet J) ⊆ S.D J) (hHM : S.H J ⊆ S.M) {Θ : N → ℝ}
    (hΘ : S.FutCauchyTemporalOn (S.D J) Θ) : S.SublevelProper J Θ := by
  intro T' p hp
  by_contra hpD
  have hpcl : p ∈ closure (S.D J) := closure_mono (fun x hx => hx.1) hp
  have hpH : p ∈ S.H J :=
    ⟨closure_mono (S.D_subset_JpastSet J) hpcl, fun hi => hpD (hint hi)⟩
  obtain ⟨U, hU, hUT⟩ := S.mh_blowup hL hΘ (hHM hpH) hpcl hpD T'
  obtain ⟨x, hxU, hxD, hxT⟩ := mem_closure_iff_nhds.1 hp U hU
  linarith [hUT x ⟨hxU, hxD⟩]

/-! ### Piece 4: the slice lower limit on `N` -/

/-- **Pointwise lower limit (BUILT).** `q ∈ M ∩ closure D \ D ⟹ q ∈ KLi(S_τ)`: the tail of the
curve into `q` lies in any neighbourhood `U`, and the levels `τ ≥ Θ(c t₀)` are hit on that tail. -/
theorem mh_mem_KLi_slice [T2Space N] (hL : S.LocallyOneChart) {J : Set N} {Θ : N → ℝ}
    (hΘ : S.FutCauchyTemporalOn (S.D J) Θ) {q : N} (hqM : q ∈ S.M)
    (hqcl : q ∈ closure (S.D J)) (hqD : q ∉ S.D J) : q ∈ KLi (S.slice J Θ) := by
  intro U hU
  obtain ⟨c, hlim, -, hchr⟩ := S.mk_curve_inext_D hL hqM hqcl hqD
  obtain ⟨t₀, ht₀⟩ := eventually_atTop.1 ((hlim.eventually hU).and (eventually_ge_atTop 0))
  have ht₀0 : 0 ≤ t₀ := (ht₀ t₀ le_rfl).2
  filter_upwards [eventually_ge_atTop (Θ (c.γ t₀))] with τ hτ
  obtain ⟨t, ht0, htτ⟩ :=
    hΘ.2 c τ ((S.mh_curve_mono hL hΘ.1 c hchr le_rfl ht₀0).trans hτ)
  have htt : t₀ ≤ t := by
    by_contra h
    rw [not_le] at h
    have := S.mh_temporalD_chr hL hΘ.1 (hchr t t₀ ht0 h) (c.mem t₀ ht₀0)
    linarith
  exact ⟨c.γ t, ⟨c.mem t ht0, htτ⟩, (ht₀ t htt).1⟩

/-- **Piece 4 (BUILT): `𝓗⁺ ⊆ KLi(S_τ)` on `N`.** -/
theorem mh_slice_lower_limit [T2Space N] (hL : S.LocallyOneChart) {J : Set N}
    (hcl : closure (S.JpastSet J) ⊆ closure (S.D J)) (hHM : S.H J ⊆ S.M) {Θ : N → ℝ}
    (hΘ : S.FutCauchyTemporalOn (S.D J) Θ) : S.H J ⊆ KLi (S.slice J Θ) := fun _ hq =>
  S.mh_mem_KLi_slice hL hΘ (hHM hq) (hcl (frontier_subset_closure hq))
    (S.mh_not_mem_D_of_H hL hq)

/-! ### Piece 5: the slice upper limit and Kuratowski on `N` -/

section Observer
variable {S} {J : Set N} {O : ℝ → N} (hOD : S.IpastSet (range O) = S.D J)
include hOD

/-- Each `O τ` lies in `D`. -/
theorem mh_observer_mem_D (hmono : ∀ s t : ℝ, s < t → S.Chr (O s) (O t)) (τ : ℝ) :
    O τ ∈ S.D J := by
  rw [← hOD]
  exact mem_iUnion₂.2 ⟨_, mem_range_self (τ + 1), hmono τ (τ + 1) (by linarith)⟩

/-- **Piece 5, upper limit (BUILT), in `N`'s topology.** For `Θ` adapted to the observer and
increasing along every `≪` ending on it: `Ls S_τ ⊆ closure J⁻(J) \ D`, hence `⊆ 𝓗⁺` given `hint`.
A point `y ∈ D = I⁻(O)` has the open neighbourhood `I⁻(O σ)` (`mk_isOpen_Ipast`), on which
`Θ < σ + c`, so only finitely-early slices meet it. -/
theorem mh_slice_upper_limit (hL : S.LocallyOneChart) {Θ : N → ℝ} {c : ℝ}
    (hadapt : ∀ τ, Θ (O τ) = τ + c) (hΘ : ∀ x σ, S.Chr x (O σ) → Θ x < Θ (O σ))
    (hint : interior (S.JpastSet J) ⊆ S.D J) : KLs (S.slice J Θ) ⊆ S.H J := by
  intro y hy
  have hcl : y ∈ closure (S.JpastSet J) :=
    ch_KLs_subset_closure (fun τ x hx => S.D_subset_JpastSet J hx.1) hy
  refine ⟨hcl, fun hi => ?_⟩
  have hyD := hint hi
  rw [← hOD] at hyD
  obtain ⟨_, ⟨σ, rfl⟩, hσ⟩ := mem_iUnion₂.1 hyD
  have hfr := hy _ ((S.mk_isOpen_Ipast hL (O σ)).mem_nhds hσ)
  obtain ⟨τ, hτ, z, hz, hzI⟩ := frequently_atTop.1 hfr (σ + c + 1)
  have := hΘ z σ hzI
  rw [hadapt, hz.2] at this
  linarith

/-- **Piece 5, Kuratowski (BUILT).** `KLi(S_τ) = KLs(S_τ) = 𝓗⁺` on `N`, from `hcl`, `hint`,
`𝓗⁺ ⊆ M`, the future Cauchy property on `D` and an adapted observer. -/
theorem mh_slice_kuratowski [T2Space N] (hL : S.LocallyOneChart)
    (hmono : ∀ s t : ℝ, s < t → S.Chr (O s) (O t))
    (hcl : closure (S.JpastSet J) ⊆ closure (S.D J))
    (hint : interior (S.JpastSet J) ⊆ S.D J) (hHM : S.H J ⊆ S.M) {Θ : N → ℝ} {c : ℝ}
    (hΘ : S.FutCauchyTemporalOn (S.D J) Θ) (hadapt : ∀ τ, Θ (O τ) = τ + c) :
    KLi (S.slice J Θ) = S.H J ∧ KLs (S.slice J Θ) = S.H J := by
  have h1 := S.mh_slice_lower_limit hL hcl hHM hΘ
  have h2 := mh_slice_upper_limit hOD hL hadapt
    (fun x σ h => S.mh_temporalD_chr hL hΘ.1 h (mh_observer_mem_D hOD hmono σ)) hint
  have h3 := hl_KLi_subset_KLs (S.slice J Θ)
  exact ⟨(h3.trans h2).antisymm h1, h2.antisymm (h1.trans h3)⟩

end Observer

variable {S}

/-! ### Piece 6: the multi-chart headline -/

/-- **Piece 6 (BUILT): `prop:causal-alignment` on a multi-chart manifold.** For a manifold
spacetime `S` on a Hausdorff `N` satisfying campaign 85's `LocallyOneChart` (every point of `M` has
a chart neighbourhood in which `g` is `C¹` and `T` continuous — no single chart need cover `M`),
an observer `O` with `I⁻(O) = D`, future-directed, `J ⊆ M`, `𝓗⁺ ⊆ M`, and `Θ` two-sided Cauchy
temporal on `D` (campaign 84's intrinsic `IsCauchyTemporalOn`) adapted to `O`: properness, and
`KLi(S_τ) = KLs(S_τ) = 𝓗⁺`, all in `N`. -/
theorem mh_causal_alignment_gh_N (hL : S.LocallyOneChart) [T2Space N] {J : Set N} {O : ℝ → N}
    (hOD : S.IpastSet (range O) = S.D J) (hmono : ∀ s t : ℝ, s < t → S.Chr (O s) (O t)) (hJM : J ⊆ S.M) (hHM : S.H J ⊆ S.M)
    {Θ : N → ℝ} {c : ℝ} (hΘ : S.IsCauchyTemporalOn (S.D J) Θ) (hadapt : ∀ τ, Θ (O τ) = τ + c) :
    S.SublevelProper J Θ ∧ KLi (S.slice J Θ) = S.H J ∧ KLs (S.slice J Θ) = S.H J := by
  have hF : S.FutCauchyTemporalOn (S.D J) Θ :=
    me_futCauchy_of_cauchy_N hL (S.mk_isOpen_D hL J) (S.D_subset_M J) hΘ
  have hint := S.mh_hint hL hJM
  have hcl := S.mh_hcl hL hJM
  exact ⟨S.mh_sublevelProper hL hint hHM hF,
    mh_slice_kuratowski hOD hL hmono hcl hint hHM hF hadapt⟩

end MSpacetime




/-! ## NEW (campaign 88) ①: the past cones `∂J⁻(O τ)` converge to `𝓗⁺` on `N`

Campaign 72's `hc_lower_limit` / `hc_upper_limit` / `hc_kuratowski` (`HorizonConvergence.lean`),
read on a multi-chart `N`. The ball of `V` around a horizon point is replaced by a connected open
neighbourhood (`N` is locally connected because its model `E` is: `ChartedSpace.locallyConnectedSpace`);
`hcl` and `hint` are campaign 87's `mh_hcl`, `mh_hint`; openness of `I⁻(O σ)` is `mk_isOpen_Ipast`. -/

section ConeTopology
variable {X : Type*} [TopologicalSpace X]

/-- Campaign 72's `hc_preconnected_inter_frontier`, in any topological space: a preconnected set
that meets `A` and contains a point `p ∉ int A` meets `∂A`. -/
theorem mc_preconnected_inter_frontier {C A : Set X} (hC : IsPreconnected C) {a p : X}
    (ha : a ∈ C ∩ A) (hp : p ∈ C) (hpA : p ∉ interior A) : (C ∩ frontier A).Nonempty := by
  by_contra hne
  rw [not_nonempty_iff_eq_empty] at hne
  have hnot : ∀ x ∈ C, x ∉ frontier A := fun x hx hf =>
    (eq_empty_iff_forall_notMem.1 hne) x ⟨hx, hf⟩
  have hcov : C ⊆ interior A ∪ (closure A)ᶜ := by
    intro x hx
    by_cases hcl : x ∈ closure A
    · left; by_contra hi; exact hnot x hx ⟨hcl, hi⟩
    · right; exact hcl
  have h1 : (C ∩ interior A).Nonempty := by
    refine ⟨a, ha.1, ?_⟩
    by_contra hi; exact hnot a ha.1 ⟨subset_closure ha.2, hi⟩
  have h2 : (C ∩ (closure A)ᶜ).Nonempty := by
    refine ⟨p, hp, fun hcl => hnot p hp ⟨hcl, hpA⟩⟩
  obtain ⟨x, -, hxi, hxc⟩ := hC _ _ isOpen_interior isClosed_closure.isOpen_compl hcov h1 h2
  exact hxc (interior_subset_closure hxi)

end ConeTopology

namespace MSpacetime
variable (S : MSpacetime E N)

/-- The family of past light cones `∂_N J⁻(O τ)`. -/
def cone (O : ℝ → N) (τ : ℝ) : Set N := frontier (S.Jpast (O τ))

theorem mc_Ipast_subset_Jpast (p : N) : S.Ipast p ⊆ S.Jpast p := fun _ h => S.chr_cau h

/-- `I⁻(p) ⊆ int J⁻(p)` on `N`. -/
theorem mc_Ipast_subset_interior (hL : S.LocallyOneChart) (p : N) :
    S.Ipast p ⊆ interior (S.Jpast p) :=
  interior_maximal (S.mc_Ipast_subset_Jpast p) (S.mk_isOpen_Ipast hL p)

/-- `p ∈ D ⟹ J⁻(p) ⊆ J⁻(J)` (transitivity only). -/
theorem mc_Jpast_subset_JpastSet {J : Set N} {p : N} (hp : p ∈ S.D J) :
    S.Jpast p ⊆ S.JpastSet J := by
  intro q hq
  obtain ⟨z, hz, hpz⟩ := mem_iUnion₂.1 hp
  exact mem_iUnion₂.2 ⟨z, hz, Relation.ReflTransGen.trans (show S.Cau q p from hq) (S.chr_cau hpz)⟩

section ConeObserver
variable {S} {J : Set N} {O : ℝ → N} (hOD : S.IpastSet (range O) = S.D J)
  (hmono : ∀ s t : ℝ, s < t → S.Chr (O s) (O t))
include hOD hmono

omit hOD in
theorem mc_Ipast_mono {σ τ : ℝ} (h : σ ≤ τ) : S.Ipast (O σ) ⊆ S.Ipast (O τ) := by
  rcases h.lt_or_eq with h | h
  · exact fun q hq => Relation.TransGen.trans (show S.Chr q (O σ) from hq) (hmono σ τ h)
  · rw [h]

/-- `x ∈ D ⟹ x ∈ I⁻(O τ)` for all large `τ`. -/
theorem mc_D_eventually {x : N} (hx : x ∈ S.D J) : ∀ᶠ τ in atTop, x ∈ S.Ipast (O τ) := by
  rw [← hOD] at hx
  obtain ⟨_, ⟨σ, rfl⟩, hσ⟩ := mem_iUnion₂.1 hx
  filter_upwards [eventually_ge_atTop σ] with τ hτ
  exact mc_Ipast_mono hmono hτ hσ

theorem mc_interior_cone_subset (τ : ℝ) :
    interior (S.Jpast (O τ)) ⊆ interior (S.JpastSet J) :=
  interior_mono (S.mc_Jpast_subset_JpastSet (mh_observer_mem_D hOD hmono τ))

/-- **① Lower limit on `N` (BUILT).** `𝓗⁺ ⊆ KLi(∂J⁻(O τ))`: a connected open neighbourhood `C`
of `p ∈ 𝓗⁺` meets `D` (`mh_hcl`), hence `I⁻(O τ)` for all large `τ`; `p ∉ int J⁻(O τ)` since
`J⁻(O τ) ⊆ J⁻(J)` and `p ∉ int J⁻(J)`; so `C` meets `∂J⁻(O τ)`. -/
theorem mc_lower_limit (hL : S.LocallyOneChart) (hJM : J ⊆ S.M) :
    S.H J ⊆ KLi (S.cone O) := by
  have : LocallyConnectedSpace N := ChartedSpace.locallyConnectedSpace E N
  intro p hp U hU
  obtain ⟨C, ⟨hCo, hpC, hCc⟩, hCU⟩ := (LocallyConnectedSpace.open_connected_basis p).mem_iff.1 hU
  have hpD : p ∈ closure (S.D J) := S.mh_hcl hL hJM (frontier_subset_closure hp)
  obtain ⟨x, hxC, hxD⟩ := mem_closure_iff.1 hpD C hCo hpC
  filter_upwards [mc_D_eventually hOD hmono hxD] with τ hτ
  have hpi : p ∉ interior (S.Jpast (O τ)) :=
    fun h => hp.2 (mc_interior_cone_subset hOD hmono τ h)
  obtain ⟨y, hyC, hyf⟩ := mc_preconnected_inter_frontier hCc.isPreconnected
    ⟨hxC, S.mc_Ipast_subset_Jpast _ hτ⟩ hpC hpi
  exact ⟨y, hyf, hCU hyC⟩

/-- **① Upper limit on `N` (BUILT).** `KLs(∂J⁻(O τ)) ⊆ 𝓗⁺`: a limit point lies in
`closure J⁻(J)`; it is not in `D`, because a point of `D` has the open neighbourhood `I⁻(O σ)`
(`mk_isOpen_Ipast`), which lies in `int J⁻(O τ)` for every `τ ≥ σ`; and `int J⁻(J) ⊆ D`
(`mh_hint`). -/
theorem mc_upper_limit (hL : S.LocallyOneChart) (hJM : J ⊆ S.M) :
    KLs (S.cone O) ⊆ S.H J := by
  intro y hy
  have hcl : y ∈ closure (S.JpastSet J) := by
    rw [mem_closure_iff_nhds]
    intro U hU
    obtain ⟨W, hWU, hWo, hyW⟩ := _root_.mem_nhds_iff.1 hU
    obtain ⟨τ, z, hzf, hzW⟩ := (hy W (hWo.mem_nhds hyW)).exists
    obtain ⟨w, hwW, hwJ⟩ := mem_closure_iff.1 (frontier_subset_closure hzf) W hWo hzW
    exact ⟨w, hWU hwW, S.mc_Jpast_subset_JpastSet (mh_observer_mem_D hOD hmono τ) hwJ⟩
  have hnD : y ∉ S.D J := by
    intro hyD
    rw [← hOD] at hyD
    obtain ⟨_, ⟨σ, rfl⟩, hσ⟩ := mem_iUnion₂.1 hyD
    have hfr := hy _ ((S.mk_isOpen_Ipast hL (O σ)).mem_nhds hσ)
    obtain ⟨τ, hτσ, z, hzf, hzI⟩ := frequently_atTop.1 hfr σ
    exact hzf.2 (S.mc_Ipast_subset_interior hL _ (mc_Ipast_mono hmono hτσ hzI))
  exact ⟨hcl, fun hi => hnD (S.mh_hint hL hJM hi)⟩

theorem mc_cone_kuratowski (hL : S.LocallyOneChart) (hJM : J ⊆ S.M) :
    KLi (S.cone O) = S.H J ∧ KLs (S.cone O) = S.H J := by
  have h1 := mc_lower_limit hOD hmono hL hJM
  have h2 := mc_upper_limit hOD hmono hL hJM
  have h3 := hl_KLi_subset_KLs (S.cone O)
  exact ⟨(h3.trans h2).antisymm h1, h2.antisymm (h1.trans h3)⟩

end ConeObserver

variable {S}

/-- **① The headline (BUILT): `∂J⁻(O τ) → 𝓗⁺` in the Kuratowski sense on a multi-chart `N`.**
On the hypotheses of `mh_causal_alignment_gh_N` minus `Θ` (and minus `T2Space N` and `𝓗⁺ ⊆ M`,
which are not needed): `LocallyOneChart`, `I⁻(O) = D`, `O` future-directed, `J ⊆ M`. -/
theorem mc_cone_kuratowski_N (hL : S.LocallyOneChart) {J : Set N} {O : ℝ → N}
    (hOD : S.IpastSet (range O) = S.D J) (hmono : ∀ s t : ℝ, s < t → S.Chr (O s) (O t))
    (hJM : J ⊆ S.M) :
    KLi (S.cone O) = S.H J ∧ KLs (S.cone O) = S.H J :=
  mc_cone_kuratowski hOD hmono hL hJM

end MSpacetime

/-! ## NEW (campaign 88) ②: the tangency clause on `N`

Mathlib reads a tangent vector at `x` (and `dΘ_x = mfderiv Θ x`, `g_x`, `T_x`) in the preferred chart
at `x`. Fix a chart `e = extChartAt p` (any `p`) and re-read everything at `x ∈ src e` in `e`:
* vectors: `A_x = D e_x = mfderiv e x` (`dchartL p x`);
* covectors: `ξ ↦ ξ ∘ B_x`, `B_x = D(e⁻¹)_{e x}` (`dchartInvL p x`), so `dΘ_x` becomes
  `covCh Θ p x = dΘ_x ∘ B_x`;
* the metric: `gCh p x = hRep g p (e x)` (campaign 68's chart representative).
`B_x ∘ A_x = id = A_x ∘ B_x` (campaign 68's `ld_mfderiv_symm_chart`, `ld_mfderiv_chart_symm`).
The frame hypotheses and the rate `ξ(ℓ)/ξ(n)` are chart-free (`mc_frameHyp_toChart`,
`mc_covCh_A`), so campaign 80's `tc_tendsto` applies to the `e`-components. -/

/-- `D e_x : T_xN → E` for `e = extChartAt p`, as a map `E →L E`. -/
noncomputable def dchartL (p x : N) : E →L[ℝ] E :=
  mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) x
/-- `D(e⁻¹)_{e x} : E → T_xN`, as a map `E →L E`. -/
noncomputable def dchartInvL (p x : N) : E →L[ℝ] E :=
  mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p).symm (extChartAt 𝓘(ℝ, E) p x)
/-- `dΘ_x = mfderiv Θ x` as a covector `E →L ℝ` (in the preferred chart at `x`). -/
noncomputable def dcov (Θ : N → ℝ) (x : N) : E →L[ℝ] ℝ := mfderiv 𝓘(ℝ, E) 𝓘(ℝ, ℝ) Θ x
/-- `dΘ_x` re-read in the chart `e = extChartAt p`: `dΘ_x ∘ D(e⁻¹)_{e x}`. -/
noncomputable def covCh (Θ : N → ℝ) (p x : N) : E →L[ℝ] ℝ := (dcov Θ x).comp (dchartInvL p x)

lemma mc_dcov_eq_dfun (Θ : N → ℝ) (x : N) (v : E) : dcov Θ x v = MSpacetime.dfun Θ x v := rfl

lemma mc_BA (p : N) {x : N} (hx : x ∈ (chartAt E p).source) (a : E) :
    dchartInvL p x (dchartL p x a) = a := ld_mfderiv_symm_chart p hx a

lemma mc_AB (p : N) {x : N} (hx : x ∈ (chartAt E p).source) (a : E) :
    dchartL p x (dchartInvL p x a) = a := ld_mfderiv_chart_symm p hx a

/-- The rate quantities are chart-free: `(dΘ_x ∘ B_x)(A_x v) = dΘ_x(v)`. -/
lemma mc_covCh_A (Θ : N → ℝ) (p : N) {x : N} (hx : x ∈ (chartAt E p).source) (v : E) :
    covCh Θ p x (dchartL p x v) = dcov Θ x v := by
  show dcov Θ x (dchartInvL p x (dchartL p x v)) = _
  rw [mc_BA p hx]

/-- `D e_p` at `p` itself is the identity (`tangentCoordChange_self`). -/
lemma mc_A_self (p : N) (a : E) : mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) p a = a := by
  have e : (extChartAt 𝓘(ℝ, E) p : N → E) = chartAt E p := rfl
  rw [e, mfderiv_chartAt_eq_tangentCoordChange (mem_chart_source E p)]
  exact tangentCoordChange_self (I := 𝓘(ℝ, E)) (mem_extChartAt_source (I := 𝓘(ℝ, E)) p)

/-- `D e_x = tangentCoordChange x p x` and `D(e⁻¹)_{e x} = tangentCoordChange p x x`. -/
lemma mc_A_eq (p : N) {x : N} (hx : x ∈ (chartAt E p).source) (a : E) :
    dchartL p x a = tangentCoordChange 𝓘(ℝ, E) x p x a := by
  have e : (extChartAt 𝓘(ℝ, E) p : N → E) = chartAt E p := rfl
  show mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) x a = _
  rw [e, mfderiv_chartAt_eq_tangentCoordChange hx]
  rfl

lemma mc_B_eq (p : N) {x : N} (hx : x ∈ (chartAt E p).source) (a : E) :
    dchartInvL p x a = tangentCoordChange 𝓘(ℝ, E) p x x a := by
  have hxs : x ∈ (extChartAt 𝓘(ℝ, E) p).source := by rwa [extChartAt_source]
  have hxx : x ∈ (extChartAt 𝓘(ℝ, E) x).source := mem_extChartAt_source x
  have h1 : dchartL p x (tangentCoordChange 𝓘(ℝ, E) p x x a) = a := by
    rw [mc_A_eq p hx, tangentCoordChange_comp ⟨⟨hxs, hxx⟩, hxs⟩, tangentCoordChange_self hxs]
  calc dchartInvL p x a = dchartInvL p x (dchartL p x (tangentCoordChange 𝓘(ℝ, E) p x x a)) := by
        rw [h1]
    _ = _ := mc_BA p hx _

/-- The coordinate change `D(e' ∘ e⁻¹)_{e x} = tangentCoordChange p p' x` is `A'_x ∘ B_x`. -/
lemma mc_tCC_eq {p p' x : N} (hx : x ∈ (chartAt E p).source) (hx' : x ∈ (chartAt E p').source)
    (v : E) : tangentCoordChange 𝓘(ℝ, E) p p' x v = dchartL p' x (dchartInvL p x v) := by
  have hxs : x ∈ (extChartAt 𝓘(ℝ, E) p).source := by rwa [extChartAt_source]
  have hxs' : x ∈ (extChartAt 𝓘(ℝ, E) p').source := by rwa [extChartAt_source]
  have hxx : x ∈ (extChartAt 𝓘(ℝ, E) x).source := mem_extChartAt_source x
  rw [mc_B_eq p hx, mc_A_eq p' hx', tangentCoordChange_comp ⟨⟨hxs, hxx⟩, hxs'⟩]

/-- **Chart change of components.** For `x` in the sources of `e = extChartAt p` and
`e' = extChartAt p'`: `dΘ_x` read in `e` is `dΘ_x` read in `e'` composed with the coordinate change
`D(e' ∘ e⁻¹)_{e x} = tangentCoordChange p p' x`. -/
lemma mc_covCh_change (Θ : N → ℝ) {p p' x : N} (hx : x ∈ (chartAt E p).source)
    (hx' : x ∈ (chartAt E p').source) :
    covCh Θ p x = (covCh Θ p' x).comp (tangentCoordChange 𝓘(ℝ, E) p p' x) := by
  ext v
  show dcov Θ x (dchartInvL p x v) = dcov Θ x (dchartInvL p' x (tangentCoordChange 𝓘(ℝ, E) p p' x v))
  rw [mc_tCC_eq hx hx', mc_BA p' hx']

/-- **Frame hypotheses pull back along a linear map** (pure linear algebra): if `g' = g(B·,B·)`,
`ξ' = ξ ∘ B`, `B ℓ' = ℓ`, `B n' = n`, then `FrameHyp g ℓ n ξ ⟹ FrameHyp g' ℓ' n' ξ'`. -/
theorem mc_frameHyp_pullback {g g' : E →L[ℝ] E →L[ℝ] ℝ} {ℓ n ℓ' n' : E} {ξ ξ' : E →L[ℝ] ℝ}
    (B : E →L[ℝ] E) (hg : ∀ a b, g' a b = g (B a) (B b)) (hξ : ∀ a, ξ' a = ξ (B a))
    (hl : B ℓ' = ℓ) (hn : B n' = n) (h : TCF.FrameHyp g ℓ n ξ) : TCF.FrameHyp g' ℓ' n' ξ' := by
  obtain ⟨⟨hs, hll, hnn, hln, hW⟩, hpos⟩ := h
  simp only [TCF.bil_apply] at hs hll hnn hln hW
  refine ⟨⟨fun v w => ?_, ?_, ?_, ?_, fun e he1 he2 => ?_⟩, fun v hv => ?_⟩
  · simp only [TCF.bil_apply, hg]; exact hs _ _
  · simp only [TCF.bil_apply, hg, hl]; exact hll
  · simp only [TCF.bil_apply, hg, hn]; exact hnn
  · simp only [TCF.bil_apply, hg, hl, hn]; exact hln
  · simp only [TCF.bil_apply, hg, hl, hn] at he1 he2 ⊢
    exact hW _ he1 he2
  · obtain ⟨hv1, hv2⟩ := hv
    simp only [TCF.bil_apply, hg, map_add, hl, hn] at hv1 hv2
    rw [hξ]
    exact hpos _ ⟨by simpa only [TCF.bil_apply] using hv1, by
      simpa only [TCF.bil_apply, map_add] using hv2⟩

/-- Campaign 80's `tc_tendsto_limit` with the bounds on `‖g_i‖` and `‖ℓ_i‖` derived from
convergence `g_i → g₀`, `ℓ_i → ℓ₀` (only `‖n_i‖` needs a bound). -/
theorem mc_tendsto_limit_aux {ι : Type*} {L : Filter ι} {g : ι → E →L[ℝ] E →L[ℝ] ℝ}
    {g₀ : E →L[ℝ] E →L[ℝ] ℝ} {l n : ι → E} {ℓ₀ : E} {ξ : ι → E →L[ℝ] ℝ} {C : ℝ}
    (hF : ∀ᶠ i in L, TCF.FrameHyp (g i) (l i) (n i) (ξ i)) (hG : Tendsto g L (𝓝 g₀))
    (hn : ∀ᶠ i in L, ‖n i‖ ≤ C) (hl : Tendsto l L (𝓝 ℓ₀))
    (hr : Tendsto (fun i => ξ i (l i) / ξ i (n i)) L (𝓝 0)) :
    Tendsto (fun i => (ξ i (n i))⁻¹ • ξ i) L (𝓝 (-(g₀ ℓ₀))) := by
  have hGb : ∀ᶠ i in L, ‖g i‖ ≤ ‖g₀‖ + 1 := by
    filter_upwards [hG (closedBall_mem_nhds g₀ one_pos)] with i hi
    have h1 := mem_closedBall.1 hi
    have h2 := norm_sub_norm_le (g i) g₀
    rw [← dist_eq_norm] at h2
    linarith
  have hlb : ∀ᶠ i in L, ‖l i‖ ≤ ‖ℓ₀‖ + 1 := by
    filter_upwards [hl (closedBall_mem_nhds ℓ₀ one_pos)] with i hi
    have h1 := mem_closedBall.1 hi
    have h2 := norm_sub_norm_le (l i) ℓ₀
    rw [← dist_eq_norm] at h2
    linarith
  have hGl : Tendsto (fun i => g i (l i)) L (𝓝 (g₀ ℓ₀)) :=
    (isBoundedBilinearMap_apply.continuous.tendsto (g₀, ℓ₀)).comp (hG.prodMk_nhds hl)
  have hA : (0:ℝ) ≤ ‖g₀‖ + 1 := by have := norm_nonneg g₀; linarith
  refine TCF.tc_tendsto_limit (C := max (‖g₀‖ + 1) (max ((‖g₀‖ + 1) * max C 0) (‖ℓ₀‖ + 1)))
    hF ?_ ?_ ?_ hr hGl
  · filter_upwards [hGb] with i h using h.trans (le_max_left _ _)
  · filter_upwards [hGb, hn] with i h1 h2
    refine le_trans ?_ ((le_max_left _ _).trans (le_max_right _ _))
    exact mul_le_mul h1 (h2.trans (le_max_left _ _)) (norm_nonneg _) hA
  · filter_upwards [hlb] with i h using h.trans ((le_max_right _ _).trans (le_max_right _ _))

namespace MSpacetime
variable (S : MSpacetime E N)

/-- The metric at `x` read in the chart `e = extChartAt p`. -/
noncomputable def gCh (p x : N) : E →L[ℝ] E →L[ℝ] ℝ := hRep S.g p (extChartAt 𝓘(ℝ, E) p x)

lemma mc_gCh_apply (p : N) {x : N} (hx : x ∈ (chartAt E p).source) (a b : E) :
    S.gCh p x a b = S.gE x (dchartInvL p x a) (dchartInvL p x b) := by
  have h := ld_h_eq_hRep S.g p hx (dchartInvL p x a) (dchartInvL p x b)
  have h1 := mc_AB p hx a
  have h2 := mc_AB p hx b
  unfold dchartL at h1 h2
  have e : ∀ u w : E, u = a → w = b →
      hRep S.g p (extChartAt 𝓘(ℝ, E) p x) u w = hRep S.g p (extChartAt 𝓘(ℝ, E) p x) a b := by
    rintro u w rfl rfl; rfl
  exact (h.trans (e _ _ h1 h2)).symm

/-- At the base point the chart is the preferred one: `gCh p p = g_p`. -/
lemma mc_gCh_self (p : N) : hRep S.g p (extChartAt 𝓘(ℝ, E) p p) = S.gE p := by
  refine ContinuousLinearMap.ext fun a => ContinuousLinearMap.ext fun b => ?_
  show _ = S.g p a b
  rw [ld_h_eq_hRep S.g p (mem_chart_source E p) a b, mc_A_self, mc_A_self]

/-- **Intrinsic frame hypotheses ⟹ chart-`e` frame hypotheses.** -/
theorem mc_frameHyp_toChart {Θ : N → ℝ} (p : N) {x : N} (hx : x ∈ (chartAt E p).source)
    {ℓ n : E} (h : TCF.FrameHyp (S.gE x) ℓ n (dcov Θ x)) :
    TCF.FrameHyp (S.gCh p x) (dchartL p x ℓ) (dchartL p x n) (covCh Θ p x) :=
  mc_frameHyp_pullback (dchartInvL p x) (S.mc_gCh_apply p hx) (fun _ => rfl) (mc_BA p hx ℓ)
    (mc_BA p hx n) h

/-- **Chart-`e` frame hypotheses ⟹ intrinsic frame hypotheses** (with the frame read back). -/
theorem mc_frameHyp_ofChart {Θ : N → ℝ} (p : N) {x : N} (hx : x ∈ (chartAt E p).source)
    {ℓ' n' : E} (h : TCF.FrameHyp (S.gCh p x) ℓ' n' (covCh Θ p x)) :
    TCF.FrameHyp (S.gE x) (dchartInvL p x ℓ') (dchartInvL p x n') (dcov Θ x) := by
  refine mc_frameHyp_pullback (dchartL p x) (fun a b => ?_) (fun a => ?_) (mc_AB p hx ℓ')
    (mc_AB p hx n') h
  · rw [S.mc_gCh_apply p hx, mc_BA p hx, mc_BA p hx]
  · rw [mc_covCh_A Θ p hx]

/-- **② Tangency on `N`, in a chart `e = extChartAt p` (BUILT).** Along any filter `L` of points in
`src e`: if the frame hypotheses hold eventually *intrinsically* (`ℓ_x, n_x` a null frame of `g_x`,
`dΘ_x` positive on its future cone), the `e`-components `‖g^e_x‖`, `‖g^e_x‖‖n^e_x‖`, `‖ℓ^e_x‖` stay
bounded, and the chart-free rate `dΘ_x(ℓ_x)/dΘ_x(n_x) → 0`, then in `e`:
`dΘ^e_x / dΘ_x(n_x) + g^e_x(ℓ^e_x, ·) → 0` in operator norm. -/
theorem mc_tangency_N {Θ : N → ℝ} {ℓ n : N → E} (p : N) {L : Filter N} {C : ℝ}
    (hsrc : ∀ᶠ x in L, x ∈ (chartAt E p).source)
    (hF : ∀ᶠ x in L, TCF.FrameHyp (S.gE x) (ℓ x) (n x) (dcov Θ x))
    (hg : ∀ᶠ x in L, ‖S.gCh p x‖ ≤ C)
    (hgn : ∀ᶠ x in L, ‖S.gCh p x‖ * ‖dchartL p x (n x)‖ ≤ C)
    (hl : ∀ᶠ x in L, ‖dchartL p x (ℓ x)‖ ≤ C)
    (hr : Tendsto (fun x => dcov Θ x (ℓ x) / dcov Θ x (n x)) L (𝓝 0)) :
    Tendsto (fun x => (dcov Θ x (n x))⁻¹ • covCh Θ p x + S.gCh p x (dchartL p x (ℓ x))) L
      (𝓝 0) := by
  have hF' : ∀ᶠ x in L, TCF.FrameHyp (S.gCh p x) (dchartL p x (ℓ x)) (dchartL p x (n x))
      (covCh Θ p x) := by
    filter_upwards [hsrc, hF] with x hx h using S.mc_frameHyp_toChart p hx h
  have hr' : Tendsto (fun x => covCh Θ p x (dchartL p x (ℓ x)) / covCh Θ p x (dchartL p x (n x)))
      L (𝓝 0) := by
    refine hr.congr' ?_
    filter_upwards [hsrc] with x hx
    rw [mc_covCh_A Θ p hx, mc_covCh_A Θ p hx]
  refine (TCF.tc_tendsto hF' hg hgn hl hr').congr' ?_
  filter_upwards [hsrc] with x hx
  rw [mc_covCh_A Θ p hx]

/-- **② The limit form (BUILT).** At a point `q ∈ src e` with `L ≤ 𝓝 q`: if `g^e = hRep g p` is
continuous at `e q`, `‖n^e_x‖` stays bounded, `ℓ^e_x → ℓ₀`, the frame hypotheses hold eventually and
the rate tends to `0`, then `dΘ^e_x / dΘ_x(n_x) → −g^e_{e q}(ℓ₀, ·)` in operator norm. -/
theorem mc_tangency_limit_N {Θ : N → ℝ} {ℓ n : N → E} (p : N) {q : N}
    (hq : q ∈ (chartAt E p).source) {L : Filter N} (hLq : L ≤ 𝓝 q) {C : ℝ} {ℓ₀ : E}
    (hgc : ContinuousAt (hRep S.g p) (extChartAt 𝓘(ℝ, E) p q))
    (hF : ∀ᶠ x in L, TCF.FrameHyp (S.gE x) (ℓ x) (n x) (dcov Θ x))
    (hn : ∀ᶠ x in L, ‖dchartL p x (n x)‖ ≤ C)
    (hℓ : Tendsto (fun x => dchartL p x (ℓ x)) L (𝓝 ℓ₀))
    (hr : Tendsto (fun x => dcov Θ x (ℓ x) / dcov Θ x (n x)) L (𝓝 0)) :
    Tendsto (fun x => (dcov Θ x (n x))⁻¹ • covCh Θ p x) L
      (𝓝 (-(hRep S.g p (extChartAt 𝓘(ℝ, E) p q) ℓ₀))) := by
  have hsrc : ∀ᶠ x in L, x ∈ (chartAt E p).source :=
    hLq ((chartAt E p).open_source.mem_nhds hq)
  have hG : Tendsto (fun x => S.gCh p x) L (𝓝 (hRep S.g p (extChartAt 𝓘(ℝ, E) p q))) :=
    hgc.tendsto.comp ((ch_contAt p hq).tendsto.mono_left hLq)
  have hF' : ∀ᶠ x in L, TCF.FrameHyp (S.gCh p x) (dchartL p x (ℓ x)) (dchartL p x (n x))
      (covCh Θ p x) := by
    filter_upwards [hsrc, hF] with x hx h using S.mc_frameHyp_toChart p hx h
  have hr' : Tendsto (fun x => covCh Θ p x (dchartL p x (ℓ x)) / covCh Θ p x (dchartL p x (n x)))
      L (𝓝 0) := by
    refine hr.congr' ?_
    filter_upwards [hsrc] with x hx
    rw [mc_covCh_A Θ p hx, mc_covCh_A Θ p hx]
  refine (mc_tendsto_limit_aux hF' hG hn hℓ hr').congr' ?_
  filter_upwards [hsrc] with x hx
  rw [mc_covCh_A Θ p hx]

/-- **② In the preferred chart at the horizon point (BUILT).** With `LocallyOneChart` (which makes
`hRep g q` `C¹`, hence continuous, at `e_q q`) and `e = extChartAt q`: the limit is
`−g_q(ℓ₀, ·)`, with `g_q` the metric at `q` itself (`mc_gCh_self`). -/
theorem mc_tangency_at_N (hL : S.LocallyOneChart) {Θ : N → ℝ} {ℓ n : N → E} {q : N}
    (hqM : q ∈ S.M) {L : Filter N} (hLq : L ≤ 𝓝 q) {C : ℝ} {ℓ₀ : E}
    (hF : ∀ᶠ x in L, TCF.FrameHyp (S.gE x) (ℓ x) (n x) (dcov Θ x))
    (hn : ∀ᶠ x in L, ‖dchartL q x (n x)‖ ≤ C)
    (hℓ : Tendsto (fun x => dchartL q x (ℓ x)) L (𝓝 ℓ₀))
    (hr : Tendsto (fun x => dcov Θ x (ℓ x) / dcov Θ x (n x)) L (𝓝 0)) :
    Tendsto (fun x => (dcov Θ x (n x))⁻¹ • covCh Θ q x) L (𝓝 (-(S.gE q ℓ₀))) := by
  obtain ⟨U, hU, hqU, -, hg, -⟩ := hL q hqM
  have hgc : ContinuousAt (hRep S.g q) (extChartAt 𝓘(ℝ, E) q q) :=
    hg.continuousOn.continuousAt (hU.mem_nhds hqU)
  have h := S.mc_tangency_limit_N q (mem_chart_source E q) hLq hgc hF hn hℓ hr
  rwa [S.mc_gCh_self q] at h

end MSpacetime

/-- **② Chart-independence (BUILT).** If `q` lies in the sources of `e = extChartAt p` and
`e' = extChartAt p'`, `L ≤ 𝓝 q`, and the rescaled covectors read in `e'` converge to `λ'`, then read
in `e` they converge to `λ' ∘ D(e' ∘ e⁻¹)_{e q}` (`tangentCoordChange p p' q`): the limit changes by
the coordinate change at `q`. (Continuity of `tangentCoordChange` is Mathlib's
`continuousOn_tangentCoordChange`.) -/
theorem mc_chart_change (Θ : N → ℝ) {p p' q : N} (hq : q ∈ (chartAt E p).source)
    (hq' : q ∈ (chartAt E p').source) {L : Filter N} (hLq : L ≤ 𝓝 q) {c : N → ℝ}
    {lam : E →L[ℝ] ℝ} (h : Tendsto (fun x => c x • covCh Θ p' x) L (𝓝 lam)) :
    Tendsto (fun x => c x • covCh Θ p x) L
      (𝓝 (lam.comp (tangentCoordChange 𝓘(ℝ, E) p p' q))) := by
  have hO : IsOpen ((extChartAt 𝓘(ℝ, E) p).source ∩ (extChartAt 𝓘(ℝ, E) p').source) :=
    (isOpen_extChartAt_source p).inter (isOpen_extChartAt_source p')
  have hqs : q ∈ (extChartAt 𝓘(ℝ, E) p).source ∩ (extChartAt 𝓘(ℝ, E) p').source := by
    rw [extChartAt_source, extChartAt_source]; exact ⟨hq, hq'⟩
  have hK : Tendsto (tangentCoordChange 𝓘(ℝ, E) p p') L
      (𝓝 (tangentCoordChange 𝓘(ℝ, E) p p' q)) :=
    (((continuousOn_tangentCoordChange p p').continuousAt (hO.mem_nhds hqs)).tendsto).mono_left hLq
  have hc := ((ContinuousLinearMap.compL ℝ E E ℝ).continuous₂.tendsto
    (lam, tangentCoordChange 𝓘(ℝ, E) p p' q)).comp (h.prodMk_nhds hK)
  refine hc.congr' ?_
  filter_upwards [hLq (hO.mem_nhds hqs)] with x hx
  rw [extChartAt_source, extChartAt_source] at hx
  show (ContinuousLinearMap.compL ℝ E E ℝ) (c x • covCh Θ p' x) (tangentCoordChange 𝓘(ℝ, E) p p' x)
    = c x • covCh Θ p x
  rw [mc_covCh_change Θ hx.1 hx.2, ContinuousLinearMap.compL_apply,
    ContinuousLinearMap.smul_comp]

/-- **The chain rule in a chart.** For `f : E → ℝ` differentiable at `e x`:
`d(f ∘ e)_x` read in `e` is `fderiv f (e x)`. -/
theorem mc_covCh_comp_chart (p : N) {f : E → ℝ} {x : N} (hx : x ∈ (chartAt E p).source)
    (hf : DifferentiableAt ℝ f (extChartAt 𝓘(ℝ, E) p x)) :
    covCh (f ∘ extChartAt 𝓘(ℝ, E) p) p x = fderiv ℝ f (extChartAt 𝓘(ℝ, E) p x) := by
  have hy : extChartAt 𝓘(ℝ, E) p x ∈ (extChartAt 𝓘(ℝ, E) p).target := ch_mem_target p hx
  have hψ := ld_mdifferentiableAt_symm p hy
  have hxs : x ∈ (extChartAt 𝓘(ℝ, E) p).source := by rwa [extChartAt_source]
  have hφ : MDifferentiableAt 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) x :=
    mdifferentiableAt_extChartAt hx
  have hfφ : MDifferentiableAt 𝓘(ℝ, E) 𝓘(ℝ, ℝ) (f ∘ extChartAt 𝓘(ℝ, E) p) x :=
    (mdifferentiableAt_iff_differentiableAt.2 hf).comp x hφ
  have hfφ' : MDifferentiableAt 𝓘(ℝ, E) 𝓘(ℝ, ℝ) (f ∘ extChartAt 𝓘(ℝ, E) p)
      ((extChartAt 𝓘(ℝ, E) p).symm (extChartAt 𝓘(ℝ, E) p x)) := by
    rw [ch_left_inv p hx]; exact hfφ
  have hev : (f ∘ extChartAt 𝓘(ℝ, E) p) ∘ (extChartAt 𝓘(ℝ, E) p).symm
      =ᶠ[𝓝 (extChartAt 𝓘(ℝ, E) p x)] f := by
    filter_upwards [(isOpen_extChartAt_target p).mem_nhds hy] with z hz
    simp only [Function.comp_apply, ch_right_inv p hz]
  have hD := (hf.hasFDerivAt.hasMFDerivAt).congr_of_eventuallyEq hev
  have hC := hfφ'.hasMFDerivAt.comp (extChartAt 𝓘(ℝ, E) p x) hψ.hasMFDerivAt
  ext v
  have hE := DFunLike.congr_fun (hC.mfderiv.symm.trans hD.mfderiv) v
  have key : ∀ z, z = x → ∀ w : E, (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, ℝ) (f ∘ extChartAt 𝓘(ℝ, E) p) z w : ℝ)
      = mfderiv 𝓘(ℝ, E) 𝓘(ℝ, ℝ) (f ∘ extChartAt 𝓘(ℝ, E) p) x w := by rintro z rfl w; rfl
  exact (key _ (ch_left_inv p hx) _).symm.trans hE

end Manifold

/-! ## NEW (campaign 89) ①, ③: the conformal extension, `𝓗⁺ = ∂J⁻(𝒥⁺)`, and the headline whole -/

section Conformal
open Manifold
set_option linter.unusedSectionVars false

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
variable {N : Type*} [TopologicalSpace N] [ChartedSpace E N] [IsManifold 𝓘(ℝ, E) 1 N]
variable {Ñ : Type*} [TopologicalSpace Ñ] [ChartedSpace E Ñ] [IsManifold 𝓘(ℝ, E) 1 Ñ]

/-- `Dι_x : T_xN → T_{ι x}Ñ` read as a map `E →L E` (both tangent spaces are `E`). -/
noncomputable def mx_dι (ι : N → Ñ) (x : N) : E →L[ℝ] E := mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) ι x

/-- **A conformal extension** of `S` (on `N`) into `St` (on `Ñ`, same model `E`): an open
embedding `ι : N → Ñ` of class `C¹`, a positive conformal factor `Ω` with
`g̃(Dι v, Dι w) = Ω² g(v, w)`, time orientations agreeing on `M`, and `ι(M) ⊆ M̃`. -/
structure ConformalExtension (S : MSpacetime E N) (St : MSpacetime E Ñ) where
  ι : N → Ñ
  isOpenEmbedding : IsOpenEmbedding ι
  contMDiff : ContMDiff 𝓘(ℝ, E) 𝓘(ℝ, E) 1 ι
  Ω : N → ℝ
  Ω_pos : ∀ x, 0 < Ω x
  conformal : ∀ x (v w : E), St.gE (ι x) (mx_dι ι x v) (mx_dι ι x w) = Ω x ^ 2 * S.gE x v w
  timeOrient : ∀ x ∈ S.M, St.FutTimelike (ι x) (mx_dι ι x (S.T x))
  maps_M : ι '' S.M ⊆ St.M

/-- Preimage under an open embedding commutes with the frontier. -/
theorem mx_preimage_frontier {X Y : Type*} [TopologicalSpace X] [TopologicalSpace Y] {f : X → Y}
    (hf : IsOpenEmbedding f) (s : Set Y) : f ⁻¹' frontier s = frontier (f ⁻¹' s) :=
  hf.isOpenMap.preimage_frontier_eq_frontier_preimage hf.continuous s

/-- Preimage under an open embedding commutes with the closure. -/
theorem mx_preimage_closure {X Y : Type*} [TopologicalSpace X] [TopologicalSpace Y] {f : X → Y}
    (hf : IsOpenEmbedding f) (s : Set Y) : f ⁻¹' closure s = closure (f ⁻¹' s) :=
  hf.isOpenMap.preimage_closure_eq_closure_preimage hf.continuous s

namespace MSpacetime

/-- **`∂J⁻(A) = closure I⁻(A) ∖ I⁻(A)`** on any `LocallyOneChart` manifold spacetime, for
`A ⊆ M`: `int J⁻(A) = I⁻(A)` (`mh_hint` and `I⁻(A)` open, `mk_isOpen_D`) and
`closure J⁻(A) = closure I⁻(A)` (`mh_hcl`). -/
theorem mx_frontier_JpastSet {S : MSpacetime E N} (hL : S.LocallyOneChart) {A : Set N}
    (hA : A ⊆ S.M) : frontier (S.JpastSet A) = closure (S.D A) \ S.D A := by
  have hint : interior (S.JpastSet A) = S.D A :=
    (S.mh_hint hL hA).antisymm (interior_maximal (S.D_subset_JpastSet A) (S.mk_isOpen_D hL A))
  have hcl : closure (S.JpastSet A) = closure (S.D A) :=
    (S.mh_hcl hL hA).antisymm (closure_mono (S.D_subset_JpastSet A))
  rw [frontier, hint, hcl]

/-- A future-directed observer lies in `M`. -/
theorem mx_range_subset_M {S : MSpacetime E N} {O : ℝ → N}
    (hmono : ∀ s t : ℝ, s < t → S.Chr (O s) (O t)) : range O ⊆ S.M := by
  rintro _ ⟨s, rfl⟩
  exact (S.chr_mem (hmono s (s + 1) (by linarith))).1

/-- **① The identification (BUILT).** In a conformal extension, if `I⁻(O) = ι⁻¹ Ĩ⁻(𝒥⁺)` then
`𝓗⁺ = ∂J⁻(O) = ∂J⁻(J)` equals P1's `∂J⁻(𝒥⁺) := ∂ (ι⁻¹ J̃⁻(𝒥⁺))`. Only `ι` and
`isOpenEmbedding` of the conformal extension are used. -/
theorem mx_H_eq_boundary {S : MSpacetime E N} {St : MSpacetime E Ñ} (hL : S.LocallyOneChart)
    (hLt : St.LocallyOneChart) (X : ConformalExtension S St) {𝒥 : Set Ñ} (h𝒥 : 𝒥 ⊆ St.M)
    {J : Set N} {O : ℝ → N} (hOD : S.IpastSet (range O) = S.D J)
    (hmono : ∀ s t : ℝ, s < t → S.Chr (O s) (O t)) (hJM : J ⊆ S.M)
    (hI : S.IpastSet (range O) = X.ι ⁻¹' St.IpastSet 𝒥) :
    S.H (range O) = frontier (X.ι ⁻¹' St.JpastSet 𝒥) ∧
      S.H J = frontier (X.ι ⁻¹' St.JpastSet 𝒥) := by
  have key : frontier (X.ι ⁻¹' St.JpastSet 𝒥) =
      closure (S.IpastSet (range O)) \ S.IpastSet (range O) := by
    rw [← mx_preimage_frontier X.isOpenEmbedding, St.mx_frontier_JpastSet hLt h𝒥, preimage_sdiff,
      mx_preimage_closure X.isOpenEmbedding, hI]
    rfl
  refine ⟨?_, ?_⟩
  · rw [key, H, S.mx_frontier_JpastSet hL (mx_range_subset_M hmono)]; rfl
  · rw [key, H, S.mx_frontier_JpastSet hL hJM, ← hOD]

/-- **③ `prop:causal-alignment`, every clause, with `𝓗⁺ := ∂J⁻(𝒥⁺) = ∂(ι⁻¹ J̃⁻(𝒥⁺))` (BUILT).**
In a conformal extension with `I⁻(O) = ι⁻¹ Ĩ⁻(𝒥⁺)`:
* `𝓗⁺_N = ∂J⁻(J) = ∂J⁻(𝒥⁺)` (①);
* properness and `KLi(S_τ) = KLs(S_τ) = ∂J⁻(𝒥⁺)` (`mh_causal_alignment_gh_N`);
* cone convergence `KLi(∂J⁻(O τ)) = KLs(∂J⁻(O τ)) = ∂J⁻(𝒥⁺)` (`mc_cone_kuratowski_N`);
* tangency at every `q ∈ ∂J⁻(𝒥⁺)`, in the chart at `q`, under its hypotheses (`mc_tangency_at_N`). -/
theorem mx_prop_causal_alignment [T2Space N] {S : MSpacetime E N} {St : MSpacetime E Ñ}
    (hL : S.LocallyOneChart) (hLt : St.LocallyOneChart) (X : ConformalExtension S St)
    {𝒥 : Set Ñ} (h𝒥 : 𝒥 ⊆ St.M) {J : Set N} {O : ℝ → N} (hOD : S.IpastSet (range O) = S.D J)
    (hmono : ∀ s t : ℝ, s < t → S.Chr (O s) (O t)) (hJM : J ⊆ S.M)
    (hI : S.IpastSet (range O) = X.ι ⁻¹' St.IpastSet 𝒥)
    (hHM : frontier (X.ι ⁻¹' St.JpastSet 𝒥) ⊆ S.M)
    {Θ : N → ℝ} {c : ℝ} (hΘ : S.IsCauchyTemporalOn (S.D J) Θ) (hadapt : ∀ τ, Θ (O τ) = τ + c) :
    S.H J = frontier (X.ι ⁻¹' St.JpastSet 𝒥) ∧
    S.SublevelProper J Θ ∧
    KLi (S.slice J Θ) = frontier (X.ι ⁻¹' St.JpastSet 𝒥) ∧
    KLs (S.slice J Θ) = frontier (X.ι ⁻¹' St.JpastSet 𝒥) ∧
    KLi (S.cone O) = frontier (X.ι ⁻¹' St.JpastSet 𝒥) ∧
    KLs (S.cone O) = frontier (X.ι ⁻¹' St.JpastSet 𝒥) ∧
    ∀ q ∈ frontier (X.ι ⁻¹' St.JpastSet 𝒥), ∀ (ℓ n : N → E) (L : Filter N) (C : ℝ) (ℓ₀ : E),
      L ≤ 𝓝 q →
      (∀ᶠ x in L, TCF.FrameHyp (S.gE x) (ℓ x) (n x) (dcov Θ x)) →
      (∀ᶠ x in L, ‖dchartL q x (n x)‖ ≤ C) →
      Tendsto (fun x => dchartL q x (ℓ x)) L (𝓝 ℓ₀) →
      Tendsto (fun x => dcov Θ x (ℓ x) / dcov Θ x (n x)) L (𝓝 0) →
      Tendsto (fun x => (dcov Θ x (n x))⁻¹ • covCh Θ q x) L (𝓝 (-(S.gE q ℓ₀))) := by
  have hH := (mx_H_eq_boundary hL hLt X h𝒥 hOD hmono hJM hI).2
  rw [← hH] at hHM ⊢
  obtain ⟨h1, h2, h3⟩ := S.mh_causal_alignment_gh_N hL hOD hmono hJM hHM hΘ hadapt
  obtain ⟨h4, h5⟩ := mc_cone_kuratowski_N hL hOD hmono hJM
  exact ⟨rfl, h1, h2, h3, h4, h5, fun q hq ℓ n L C ℓ₀ hLq hF hn hℓ hr =>
    S.mc_tangency_at_N hL (hHM hq) hLq hF hn hℓ hr⟩

end MSpacetime

end Conformal

/-- Two spacetimes with the same `M`, `g`, `T` are equal. -/
theorem Spacetime.ch_ext {S S' : Spacetime V} (hM : S.M = S'.M) (hg : S.g = S'.g)
    (hT : S.T = S'.T) : S = S' := by
  cases S; cases S'; cases hM; cases hg; cases hT; rfl

/-! ## c2 witness: the Rindler model on a manifold with two charts

`Pt` is a copy of `ℝ²` (points `(t, x)`), a separate type with its own charted-space structure: the
atlas `{idH, nullH}`, `idH = id`, `nullH : (t, x) ↦ (U, V) = (t − x, t + x)`; the preferred chart is
`idH` on `{t < 0}` and `nullH` on `{t ≥ 0}`. Mathlib reads tangent vectors in the preferred chart, so
`g`, `T` on `Pt` are `−dt² + dx²`, `∂_t = (1,0)` on `{t < 0}` and `−dU dV`, `(1,1)` on `{t ≥ 0}`.
`p₀ = (0,0)`, so `φ = extChartAt p₀ = nullH`, which is not the identity map (`ch_chart_ne_id`).

*What is exercised:* points, curves, `≪`, `D`, `𝓗⁺`, slices and the Cauchy property go through the
non-identity map `φ`; and `Dφ = mfderiv φ` is **not** the identity on `{t < 0}` (`ch_dchart_eq`,
`ch_dchart_ne_id`: it is `nullL`), so `hRep`/`chartRep` really change the components there. The chart
spacetime is nevertheless exactly campaign 81's `mink` (`ch_chartSp_eq`), which is what lets the model
facts be reused. -/

namespace NModel
open Model Manifold ContinuousLinearMap

/-- The plane as a separate type, points `(t, x)`. -/
def Pt : Type := ℝ × ℝ

instance : TopologicalSpace Pt := inferInstanceAs (TopologicalSpace (ℝ × ℝ))

/-- The null-coordinate chart `(t, x) ↦ (t − x, t + x)`. -/
noncomputable def nullH : Pt ≃ₜ P where
  toFun := fun p : ℝ × ℝ => (p.1 - p.2, p.1 + p.2)
  invFun := fun q : P => (((q.1 + q.2) / 2, (q.2 - q.1) / 2) : ℝ × ℝ)
  left_inv := fun p : ℝ × ℝ => Prod.ext (by simp only; ring) (by simp only; ring)
  right_inv := fun q : P => Prod.ext (by simp only; ring) (by simp only; ring)
  continuous_toFun := by
    show Continuous fun p : ℝ × ℝ => (p.1 - p.2, p.1 + p.2)
    fun_prop
  continuous_invFun := by
    show Continuous fun q : ℝ × ℝ => (((q.1 + q.2) / 2, (q.2 - q.1) / 2) : ℝ × ℝ)
    fun_prop

/-- The time coordinate `t` of a point of `Pt`. -/
def tco (x : Pt) : ℝ := Prod.fst (α := ℝ) (β := ℝ) x

/-- The identity chart `(t, x) ↦ (t, x)`. -/
noncomputable def idH : Pt ≃ₜ P where
  toFun := fun p : ℝ × ℝ => p
  invFun := fun q : P => (q : ℝ × ℝ)
  left_inv := fun _ => rfl
  right_inv := fun _ => rfl
  continuous_toFun := continuous_id
  continuous_invFun := continuous_id

/-- **Two charts.** The preferred chart is the identity chart on `{t < 0}` and the null chart on
`{t ≥ 0}` (Mathlib allows any choice of preferred chart). -/
noncomputable instance : ChartedSpace P Pt where
  atlas := {idH.toOpenPartialHomeomorph, nullH.toOpenPartialHomeomorph}
  chartAt x := if tco x < 0 then idH.toOpenPartialHomeomorph
    else nullH.toOpenPartialHomeomorph
  mem_chart_source x := by split_ifs <;> simp
  chart_mem_atlas x := by split_ifs <;> simp

lemma cd_id_id : ContDiff ℝ 1 (fun y : P => idH (idH.symm y)) := by
  show ContDiff ℝ 1 (fun y : P => y); fun_prop
lemma cd_null_id : ContDiff ℝ 1 (fun y : P => nullH (idH.symm y)) := by
  show ContDiff ℝ 1 (fun y : P => (y.1 - y.2, y.1 + y.2)); fun_prop
lemma cd_id_null : ContDiff ℝ 1 (fun y : P => idH (nullH.symm y)) := by
  show ContDiff ℝ 1 (fun y : P => (((y.1 + y.2) / 2, (y.2 - y.1) / 2) : ℝ × ℝ)); fun_prop
lemma cd_null_null : ContDiff ℝ 1 (fun y : P => nullH (nullH.symm y)) := by
  show ContDiff ℝ 1 (fun y : P => ((((y.1 + y.2) / 2) - (y.2 - y.1) / 2,
    ((y.1 + y.2) / 2) + (y.2 - y.1) / 2) : ℝ × ℝ)); fun_prop

instance : IsManifold 𝓘(ℝ, P) 1 Pt := by
  apply isManifold_of_contDiffOn
  intro e e' he he'
  have he1 : e = idH.toOpenPartialHomeomorph ∨ e = nullH.toOpenPartialHomeomorph := he
  have he2 : e' = idH.toOpenPartialHomeomorph ∨ e' = nullH.toOpenPartialHomeomorph := he'
  rcases he1 with rfl | rfl <;> rcases he2 with rfl | rfl
  · exact cd_id_id.contDiffOn.congr fun y _ => by simp
  · exact cd_null_id.contDiffOn.congr fun y _ => by simp
  · exact cd_id_null.contDiffOn.congr fun y _ => by simp
  · exact cd_null_null.contDiffOn.congr fun y _ => by simp

/-- The point `(a, b)` of `Pt`. -/
def mkPt (a b : ℝ) : Pt := ((a, b) : ℝ × ℝ)

/-- The base point. -/
def p₀ : Pt := mkPt 0 0

lemma chartAt_eq (x : Pt) : chartAt P x = if tco x < 0 then
    idH.toOpenPartialHomeomorph else nullH.toOpenPartialHomeomorph := rfl

lemma chartAt_p₀ : chartAt P p₀ = nullH.toOpenPartialHomeomorph := by
  rw [chartAt_eq]; exact ite_eq_right (lt_irrefl (0:ℝ))

lemma chart_apply (x : Pt) : extChartAt 𝓘(ℝ, P) p₀ x = nullH x := by
  rw [extChartAt_coe, Function.comp_apply, chartAt_p₀]; rfl

/-- The chart is not the identity map of `ℝ²`. -/
theorem ch_chart_ne_id : extChartAt 𝓘(ℝ, P) p₀ (mkPt 1 0) ≠ ((1, 0) : ℝ × ℝ) := by
  rw [chart_apply]
  show ((1 - 0, 1 + 0) : ℝ × ℝ) ≠ (1, 0)
  norm_num

lemma source_eq : (chartAt P p₀).source = univ := by rw [chartAt_p₀]; simp

lemma target_eq : (extChartAt 𝓘(ℝ, P) p₀).target = univ := by
  rw [extChartAt_target, chartAt_p₀]; simp

lemma src (x : Pt) : x ∈ (chartAt P p₀).source := by rw [source_eq]; exact mem_univ _

/-- `nullH` as a linear map of `ℝ²`. -/
noncomputable def nullL : P →L[ℝ] P :=
  ((fst ℝ ℝ ℝ) - (snd ℝ ℝ ℝ)).prod ((fst ℝ ℝ ℝ) + (snd ℝ ℝ ℝ))

lemma nullL_apply (v : P) : nullL v = (v.1 - v.2, v.1 + v.2) := by simp [nullL]

/-- **`Dφ ≠ id` on `{t < 0}`**: there the tangent vectors are read in the identity chart, and
`Dφ = D(nullH ∘ idH⁻¹) = nullL`; on `{t ≥ 0}`, `Dφ = id`. -/
theorem ch_dchart_eq (x : Pt) (v : P) :
    dchart p₀ x v = if tco x < 0 then nullL v else v := by
  show mfderiv 𝓘(ℝ, P) 𝓘(ℝ, P) (extChartAt 𝓘(ℝ, P) p₀) x v = _
  have e : (extChartAt 𝓘(ℝ, P) p₀ : Pt → P) = chartAt P p₀ := rfl
  rw [e, mfderiv_chartAt_eq_tangentCoordChange (src x), tangentCoordChange_def,
    ModelWithCorners.range_eq_univ, fderivWithin_univ]
  have e1 : ∀ y, (extChartAt 𝓘(ℝ, P) p₀ ∘ (extChartAt 𝓘(ℝ, P) x).symm) y =
      nullH ((chartAt P x).symm y) := fun y => by
    rw [Function.comp_apply, chart_apply, extChartAt_coe_symm]; rfl
  split_ifs with h
  · have hf : (extChartAt 𝓘(ℝ, P) p₀ ∘ (extChartAt 𝓘(ℝ, P) x).symm) = nullL := by
      funext y; rw [e1, chartAt_eq, ite_eq_left h, nullL_apply]; rfl
    rw [hf, ContinuousLinearMap.fderiv]; rfl
  · have hf : (extChartAt 𝓘(ℝ, P) p₀ ∘ (extChartAt 𝓘(ℝ, P) x).symm) = id := by
      funext y; rw [e1, chartAt_eq, ite_eq_right h]; exact nullH.apply_symm_apply y
    rw [hf, fderiv_id]; rfl

theorem ch_dchart_ne_id :
    mfderiv 𝓘(ℝ, P) 𝓘(ℝ, P) (extChartAt 𝓘(ℝ, P) p₀) (mkPt (-1) 0) ((1, 0) : P) ≠
      ((1, 0) : P) := by
  show dchart p₀ (mkPt (-1) 0) ((1, 0) : P) ≠ ((1, 0) : P)
  rw [ch_dchart_eq, ite_eq_left (show tco (mkPt (-1) 0) < 0 by show (-1 : ℝ) < 0; norm_num), nullL_apply]
  intro h
  have := congrArg Prod.snd h
  norm_num at this

lemma dinv_eq (x : Pt) (w : P) :
    dchartInv p₀ (extChartAt 𝓘(ℝ, P) p₀ x) w =
      if tco x < 0 then (((w.1 + w.2) / 2, (w.2 - w.1) / 2) : P) else w := by
  have h : dchart p₀ x (dchartInv p₀ (extChartAt 𝓘(ℝ, P) p₀ x) w) = w :=
    ld_mfderiv_chart_symm p₀ (src x) w
  rw [ch_dchart_eq] at h
  by_cases hx : tco x < 0
  · rw [ite_eq_left hx, nullL_apply] at h
    rw [ite_eq_left hx]
    have h1 := congrArg Prod.fst h
    have h2 := congrArg Prod.snd h
    simp only at h1 h2
    exact Prod.ext (by simp only; linarith) (by simp only; linarith)
  · rw [ite_eq_right hx] at h
    rw [ite_eq_right hx]; exact h

/-- Minkowski in `(t, x)` coordinates, `−dt² + dx²`. -/
noncomputable def gTX : P →L[ℝ] P →L[ℝ] ℝ :=
  -((fst ℝ ℝ ℝ).smulRight (fst ℝ ℝ ℝ)) + (snd ℝ ℝ ℝ).smulRight (snd ℝ ℝ ℝ)

lemma gTX_apply (v w : P) : gTX v w = -(v.1 * w.1) + v.2 * w.2 := by simp [gTX]

/-- The metric on `Pt`, in the preferred chart's coordinates at each point. -/
noncomputable def gN (x : Pt) : P →L[ℝ] P →L[ℝ] ℝ :=
  if tco x < 0 then gTX else gM
/-- The time orientation `∂_t`, in the preferred chart's coordinates. -/
noncomputable def TN (x : Pt) : P := if tco x < 0 then (1, 0) else (1, 1)

/-- **The manifold spacetime**: `M = Pt`, the flat metric and `T = ∂_t`, written in the preferred
chart at each point (`(t,x)` on `{t < 0}`, `(U,V)` on `{t ≥ 0}`). -/
noncomputable def minkN : MSpacetime P Pt where
  M := univ
  isOpen_M := isOpen_univ
  g := gN
  symm := fun x v w => by
    show gN x v w = gN x w v
    unfold gN; split_ifs
    · rw [gTX_apply, gTX_apply]; ring
    · exact mink.symm 0 v w
  T := TN
  T_timelike := fun x _ => by
    show gN x (TN x) (TN x) < 0
    unfold gN TN; split_ifs
    · rw [gTX_apply]; norm_num
    · exact mink.T_timelike 0 (mem_univ _)
  pos_on_perp := fun x _ v h hv => by
    change gN x v (TN x) = 0 at h
    show 0 < gN x v v
    unfold gN TN at *
    split_ifs at h ⊢
    · rw [gTX_apply] at h ⊢
      have h1 : v.1 = 0 := by linarith
      have h2 : v.2 ≠ 0 := fun h2 => hv (Prod.ext h1 h2)
      rw [h1]; nlinarith [sq_pos_of_ne_zero h2]
    · exact mink.pos_on_perp 0 (mem_univ _) v h hv

lemma hRep_eq : hRep minkN.g p₀ = fun _ => gM := by
  funext y
  obtain ⟨x, rfl⟩ : ∃ x, extChartAt 𝓘(ℝ, P) p₀ x = y :=
    ⟨_, (extChartAt 𝓘(ℝ, P) p₀).right_inv (by rw [target_eq]; exact mem_univ y)⟩
  refine ContinuousLinearMap.ext fun v => ContinuousLinearMap.ext fun w => ?_
  show gN ((extChartAt 𝓘(ℝ, P) p₀).symm (extChartAt 𝓘(ℝ, P) p₀ x))
    (dchartInv p₀ (extChartAt 𝓘(ℝ, P) p₀ x) v) (dchartInv p₀ (extChartAt 𝓘(ℝ, P) p₀ x) w) = gM v w
  rw [dinv_eq x v, dinv_eq x w, ch_left_inv p₀ (src x)]
  unfold gN; split_ifs
  · rw [gTX_apply, gM_apply]; ring
  · rfl

lemma chartRep_eq : chartRep minkN.T p₀ = fun _ => ((1, 1) : P) := by
  funext y
  obtain ⟨x, rfl⟩ : ∃ x, extChartAt 𝓘(ℝ, P) p₀ x = y :=
    ⟨_, (extChartAt 𝓘(ℝ, P) p₀).right_inv (by rw [target_eq]; exact mem_univ y)⟩
  rw [ld_chartRep_apply_chart _ _ (src x)]
  show dchart p₀ x (TN x) = _
  rw [ch_dchart_eq]
  unfold TN; split_ifs
  · rw [nullL_apply]; norm_num
  · rfl

theorem ch_oneChart : minkN.OneChart p₀ where
  sub := by rw [source_eq]; exact subset_univ _
  g_C1 := by rw [hRep_eq]; exact contDiffOn_const
  T_cont := by rw [chartRep_eq]; exact continuousOn_const

/-- **The chart spacetime of `minkN` is campaign 81's `mink`.** -/
theorem ch_chartSp_eq : MSpacetime.chartSp ch_oneChart = mink := by
  refine Spacetime.ch_ext ?_ hRep_eq chartRep_eq
  show extChartAt 𝓘(ℝ, P) p₀ '' univ = univ
  refine eq_univ_of_forall fun y => ⟨(extChartAt 𝓘(ℝ, P) p₀).symm y, mem_univ _, ?_⟩
  exact (extChartAt 𝓘(ℝ, P) p₀).right_inv (by rw [target_eq]; exact mem_univ y)

/-- `φ⁻¹`. -/
noncomputable def ψ : P → Pt := (extChartAt 𝓘(ℝ, P) p₀).symm

lemma φψ (y : P) : extChartAt 𝓘(ℝ, P) p₀ (ψ y) = y :=
  (extChartAt 𝓘(ℝ, P) p₀).right_inv (by rw [target_eq]; exact mem_univ y)

/-- The worldline `J_N = φ⁻¹(range O)` on `Pt`. -/
noncomputable def JN : Set Pt := ψ '' range O

lemma image_JN : extChartAt 𝓘(ℝ, P) p₀ '' JN = range O := by
  rw [JN, image_image]; simp only [φψ, image_id']

lemma mem_D_N (A : Set P) (x : Pt) :
    x ∈ minkN.D (ψ '' A) ↔ extChartAt 𝓘(ℝ, P) p₀ x ∈ mink.D A := by
  rw [MSpacetime.ch_mem_D_iff ch_oneChart (fun _ _ => src _) (src x), ch_chartSp_eq, image_image]
  simp only [φψ, image_id']

lemma mem_H_N (x : Pt) : x ∈ minkN.H JN ↔ (extChartAt 𝓘(ℝ, P) p₀ x).1 = 0 := by
  rw [MSpacetime.ch_mem_H_iff ch_oneChart (fun _ _ => src _) (src x), ch_chartSp_eq, image_JN,
    hl_H_eq]
  rfl

/-- **Every hypothesis of `ch_causal_alignment_gh_N` holds on `Pt`**, for every good profile `G`,
with `Θ_N = Θ_G ∘ φ`, `J_N = φ⁻¹(range O)` and the observer `φ⁻¹ ∘ O'`. -/
theorem ch_witness_hypotheses {G : ℝ → ℝ} (hG : GoodG G) :
    ∃ O_N : ℝ → Pt, minkN.IpastSet (range O_N) = minkN.D JN ∧
      (∀ s t : ℝ, s < t → minkN.Chr (O_N s) (O_N t)) ∧ JN ⊆ minkN.M ∧ minkN.H JN ⊆ minkN.M ∧
      minkN.IsCauchyTemporalOn (minkN.D JN) (ThetaG G ∘ extChartAt 𝓘(ℝ, P) p₀) ∧
      ∀ τ, (ThetaG G ∘ extChartAt 𝓘(ℝ, P) p₀) (O_N τ) = τ + 0 := by
  obtain ⟨O', hrange, hOD, hmono, hadapt⟩ := hG.hl_adapted
  refine ⟨fun τ => ψ (O' τ), ?_, fun s t h => ?_, subset_univ _, subset_univ _, ?_, fun τ => ?_⟩
  · show minkN.D _ = _
    have e : range (fun τ => ψ (O' τ)) = ψ '' range O' := (range_comp ψ O').symm ▸ rfl
    ext x
    rw [e, mem_D_N, JN, mem_D_N]
    have h' : mink.D (range O') = mink.D (range O) := hOD
    rw [h']
  · rw [MSpacetime.ch_chr_iff ch_oneChart (src _) (src _), ch_chartSp_eq, φψ, φψ]
    exact hmono s t h
  · refine MSpacetime.ch_isCauchy_VN ch_oneChart (subset_univ _) ?_
    rw [ch_chartSp_eq, image_JN]
    exact hl_cauchy hG
  · show ThetaG G (extChartAt 𝓘(ℝ, P) p₀ (ψ (O' τ))) = _
    rw [φψ]; exact hadapt τ


/-! ### Copied (campaign 85): every point's own chart -/

/-- The inverse null map `(U, V) ↦ ((U+V)/2, (V−U)/2)` as a linear map. -/
noncomputable def nullInvL : P →L[ℝ] P :=
  ((1/2 : ℝ) • ((fst ℝ ℝ ℝ) + (snd ℝ ℝ ℝ))).prod ((1/2 : ℝ) • ((snd ℝ ℝ ℝ) - (fst ℝ ℝ ℝ)))

lemma nullInvL_apply (v : P) : nullInvL v = ((v.1 + v.2) / 2, (v.2 - v.1) / 2) := by
  ext <;> simp [nullInvL] <;> ring

lemma chartAt_neg {p : Pt} (hp : tco p < 0) : chartAt P p = idH.toOpenPartialHomeomorph := by
  rw [chartAt_eq, ite_eq_left hp]

lemma chartAt_nonneg {p : Pt} (hp : ¬ tco p < 0) : chartAt P p = chartAt P p₀ := by
  rw [chartAt_eq, ite_eq_right hp, chartAt_p₀]

lemma extChartAt_nonneg {p : Pt} (hp : ¬ tco p < 0) :
    extChartAt 𝓘(ℝ, P) p = extChartAt 𝓘(ℝ, P) p₀ := by
  unfold extChartAt; rw [chartAt_nonneg hp]

lemma chart_apply_neg {p : Pt} (hp : tco p < 0) (x : Pt) : extChartAt 𝓘(ℝ, P) p x = idH x := by
  rw [extChartAt_coe, Function.comp_apply, chartAt_neg hp]; rfl

lemma src_neg {p : Pt} (hp : tco p < 0) (x : Pt) : x ∈ (chartAt P p).source := by
  rw [chartAt_neg hp]; simp

/-- `Dφ_p` for a base point `p` with `t < 0` (chart `idH`): the identity on `{t < 0}` and the
inverse null map on `{t ≥ 0}`. -/
theorem me_dchart_neg {p : Pt} (hp : tco p < 0) (x : Pt) (v : P) :
    dchart p x v = if tco x < 0 then v else nullInvL v := by
  show mfderiv 𝓘(ℝ, P) 𝓘(ℝ, P) (extChartAt 𝓘(ℝ, P) p) x v = _
  have e : (extChartAt 𝓘(ℝ, P) p : Pt → P) = chartAt P p := rfl
  rw [e, mfderiv_chartAt_eq_tangentCoordChange (src_neg hp x), tangentCoordChange_def,
    ModelWithCorners.range_eq_univ, fderivWithin_univ]
  have e1 : ∀ y, (extChartAt 𝓘(ℝ, P) p ∘ (extChartAt 𝓘(ℝ, P) x).symm) y =
      idH ((chartAt P x).symm y) := fun y => by
    rw [Function.comp_apply, chart_apply_neg hp, extChartAt_coe_symm]; rfl
  split_ifs with h
  · have hf : (extChartAt 𝓘(ℝ, P) p ∘ (extChartAt 𝓘(ℝ, P) x).symm) = id := by
      funext y; rw [e1, chartAt_eq, ite_eq_left h]; exact idH.apply_symm_apply y
    rw [hf, fderiv_id]; rfl
  · have hf : (extChartAt 𝓘(ℝ, P) p ∘ (extChartAt 𝓘(ℝ, P) x).symm) = nullInvL := by
      funext y; rw [e1, chartAt_eq, ite_eq_right h, nullInvL_apply]; rfl
    rw [hf, ContinuousLinearMap.fderiv]; rfl

lemma dinv_neg {p : Pt} (hp : tco p < 0) (x : Pt) (w : P) :
    dchartInv p (extChartAt 𝓘(ℝ, P) p x) w = if tco x < 0 then w else nullL w := by
  have h : dchart p x (dchartInv p (extChartAt 𝓘(ℝ, P) p x) w) = w :=
    ld_mfderiv_chart_symm p (src_neg hp x) w
  rw [me_dchart_neg hp] at h
  by_cases hx : tco x < 0
  · rw [ite_eq_left hx] at h; rw [ite_eq_left hx]; exact h
  · rw [ite_eq_right hx, nullInvL_apply] at h
    rw [ite_eq_right hx, nullL_apply]
    have h1 := congrArg Prod.fst h
    have h2 := congrArg Prod.snd h
    simp only at h1 h2
    exact Prod.ext (by simp only; linarith) (by simp only; linarith)

lemma hRep_neg {p : Pt} (hp : tco p < 0) : hRep minkN.g p = fun _ => gTX := by
  funext y
  obtain ⟨x, rfl⟩ : ∃ x, extChartAt 𝓘(ℝ, P) p x = y :=
    ⟨idH.symm y, by rw [chart_apply_neg hp]; exact idH.apply_symm_apply y⟩
  refine ContinuousLinearMap.ext fun v => ContinuousLinearMap.ext fun w => ?_
  show gN ((extChartAt 𝓘(ℝ, P) p).symm (extChartAt 𝓘(ℝ, P) p x))
    (dchartInv p (extChartAt 𝓘(ℝ, P) p x) v) (dchartInv p (extChartAt 𝓘(ℝ, P) p x) w) = gTX v w
  rw [dinv_neg hp x v, dinv_neg hp x w, ch_left_inv p (src_neg hp x)]
  unfold gN; split_ifs
  · rfl
  · rw [gTX_apply, gM_apply, nullL_apply, nullL_apply]; ring

lemma chartRep_neg {p : Pt} (hp : tco p < 0) : chartRep minkN.T p = fun _ => ((1, 0) : P) := by
  funext y
  obtain ⟨x, rfl⟩ : ∃ x, extChartAt 𝓘(ℝ, P) p x = y :=
    ⟨idH.symm y, by rw [chart_apply_neg hp]; exact idH.apply_symm_apply y⟩
  rw [ld_chartRep_apply_chart _ _ (src_neg hp x)]
  show dchart p x (TN x) = _
  rw [me_dchart_neg hp]
  unfold TN; split_ifs
  · rfl
  · rw [nullInvL_apply]; norm_num

/-- Points of `Pt` use different preferred charts: `idH` at `(−1, 0)`, `nullH` at `(1, 0)`. -/
theorem me_charts_differ :
    extChartAt 𝓘(ℝ, P) (mkPt (-1) 0) (mkPt 1 0) ≠ extChartAt 𝓘(ℝ, P) (mkPt 1 0) (mkPt 1 0) := by
  have h1 : tco (mkPt (-1) 0) < 0 := by show (-1 : ℝ) < 0; norm_num
  have h2 : ¬ tco (mkPt 1 0) < 0 := by show ¬ (1 : ℝ) < 0; norm_num
  rw [chart_apply_neg h1, extChartAt_nonneg h2, chart_apply]
  show ((1, 0) : ℝ × ℝ) ≠ (1 - 0, 1 + 0)
  norm_num

/-- **`LocallyOneChart` on the two-chart manifold (BUILT).** At `p` with `t < 0` the preferred
chart is `idH`, and `hRep g p = −dt² + dx²`, `chartRep T p = (1, 0)` (`hRep_neg`, `chartRep_neg`,
through the non-identity `Dφ_p` on `{t ≥ 0}`); at `p` with `t ≥ 0` it is `nullH`, with campaign 84's
`hRep_eq`, `chartRep_eq`. -/
theorem me_locallyOneChart : minkN.LocallyOneChart := by
  intro p _
  by_cases hp : tco p < 0
  · refine ⟨univ, isOpen_univ, mem_univ _, fun y _ => ⟨idH.symm y, ⟨mem_univ _, src_neg hp _⟩, ?_⟩,
      ?_, ?_⟩
    · rw [chart_apply_neg hp]; exact idH.apply_symm_apply y
    · rw [hRep_neg hp]; exact contDiffOn_const
    · rw [chartRep_neg hp]; exact continuousOn_const
  · have hh : hRep minkN.g p = hRep minkN.g p₀ := by unfold hRep; rw [extChartAt_nonneg hp]
    have hc : chartRep minkN.T p = chartRep minkN.T p₀ := by
      unfold chartRep; rw [extChartAt_nonneg hp]
    refine ⟨univ, isOpen_univ, mem_univ _, fun y _ => ⟨ψ y, ⟨mem_univ _, ?_⟩, ?_⟩, ?_, ?_⟩
    · rw [chartAt_nonneg hp]; exact src _
    · rw [extChartAt_nonneg hp]; exact φψ y
    · rw [hh, hRep_eq]; exact contDiffOn_const
    · rw [hc, chartRep_eq]; exact continuousOn_const


/-! ### NEW (campaign 87): the multi-chart headline witnessed end to end on `Pt` -/

instance : T2Space Pt := inferInstanceAs (T2Space (ℝ × ℝ))

/-- **Every hypothesis of `mh_causal_alignment_gh_N` holds on the two-chart `Pt`** (BUILT), for
every good profile `G`, with `Θ_N = Θ_G ∘ φ`, `J_N = φ⁻¹(range O)`: `LocallyOneChart` (campaign 85,
preferred charts `idH` on `{t < 0}` and `nullH` on `{t ≥ 0}`), `T2Space Pt`, and, by campaign 84's
transport `ch_isCauchy_VN` from campaign 81's two-sided Rindler model `Model.hl_cauchy`, the
two-sided Cauchy property on `D_N` (the hypothesis campaign 85 left unwitnessed), with the observer,
`hOD`, `hmono`, `J ⊆ M`, `𝓗⁺ ⊆ M` and `hadapt`. -/
theorem mh_witness_hypotheses {G : ℝ → ℝ} (hG : GoodG G) :
    minkN.LocallyOneChart ∧ extChartAt 𝓘(ℝ, P) (mkPt (-1) 0) (mkPt 1 0) ≠ extChartAt 𝓘(ℝ, P) (mkPt 1 0) (mkPt 1 0) ∧
    ∃ O_N : ℝ → Pt, minkN.IpastSet (range O_N) = minkN.D JN ∧
      (∀ s t : ℝ, s < t → minkN.Chr (O_N s) (O_N t)) ∧ JN ⊆ minkN.M ∧ minkN.H JN ⊆ minkN.M ∧
      minkN.IsCauchyTemporalOn (minkN.D JN) (ThetaG G ∘ extChartAt 𝓘(ℝ, P) p₀) ∧
      ∀ τ, (ThetaG G ∘ extChartAt 𝓘(ℝ, P) p₀) (O_N τ) = τ + 0 :=
  ⟨me_locallyOneChart, me_charts_differ, ch_witness_hypotheses hG⟩

/-- **The multi-chart headline on `Pt`, end to end (BUILT).** `𝓗⁺_N = φ⁻¹{U = 0} ≠ ∅`, and for
every good `G`: properness and `KLi(S_τ) = KLs(S_τ) = 𝓗⁺_N`, obtained from
`mh_causal_alignment_gh_N` (not from campaign 84's one-chart theorem). -/
theorem mh_witness_headline_G {G : ℝ → ℝ} (hG : GoodG G) :
    (∀ x : Pt, x ∈ minkN.H JN ↔ (extChartAt 𝓘(ℝ, P) p₀ x).1 = 0) ∧ (minkN.H JN).Nonempty ∧
    minkN.SublevelProper JN (ThetaG G ∘ extChartAt 𝓘(ℝ, P) p₀) ∧
    KLi (minkN.slice JN (ThetaG G ∘ extChartAt 𝓘(ℝ, P) p₀)) = minkN.H JN ∧
    KLs (minkN.slice JN (ThetaG G ∘ extChartAt 𝓘(ℝ, P) p₀)) = minkN.H JN := by
  obtain ⟨hL, -, O_N, hOD, hmono, hJM, hHM, hΘ, hadapt⟩ := mh_witness_hypotheses hG
  exact ⟨mem_H_N, ⟨ψ (0, 0), (mem_H_N _).2 (by rw [φψ])⟩,
    MSpacetime.mh_causal_alignment_gh_N hL hOD hmono hJM hHM hΘ hadapt⟩

/-- **The registered witness (BUILT):** on the two-chart `Pt` (points with `t < 0` and `t ≥ 0` take
different preferred charts), for `Θ₀ ∘ φ` and the tangency-failing `Θf ∘ φ`:
`KLi = KLs = 𝓗⁺ = {U = 0}`, with properness, via `mh_causal_alignment_gh_N`. -/
theorem mh_witness_headline :
    minkN.LocallyOneChart ∧ extChartAt 𝓘(ℝ, P) (mkPt (-1) 0) (mkPt 1 0) ≠ extChartAt 𝓘(ℝ, P) (mkPt 1 0) (mkPt 1 0) ∧
    (∀ x : Pt, x ∈ minkN.H JN ↔ (extChartAt 𝓘(ℝ, P) p₀ x).1 = 0) ∧ (minkN.H JN).Nonempty ∧
    (minkN.SublevelProper JN (Θ₀ ∘ extChartAt 𝓘(ℝ, P) p₀) ∧
      KLi (minkN.slice JN (Θ₀ ∘ extChartAt 𝓘(ℝ, P) p₀)) = minkN.H JN ∧
      KLs (minkN.slice JN (Θ₀ ∘ extChartAt 𝓘(ℝ, P) p₀)) = minkN.H JN) ∧
    (minkN.SublevelProper JN (Θf ∘ extChartAt 𝓘(ℝ, P) p₀) ∧
      KLi (minkN.slice JN (Θf ∘ extChartAt 𝓘(ℝ, P) p₀)) = minkN.H JN ∧
      KLs (minkN.slice JN (Θf ∘ extChartAt 𝓘(ℝ, P) p₀)) = minkN.H JN) :=
  ⟨me_locallyOneChart, me_charts_differ, mem_H_N, (mh_witness_headline_G goodG_log).2.1,
    (mh_witness_headline_G goodG_log).2.2, (mh_witness_headline_G goodG_Ffail).2.2⟩

end NModel

/-! ## NEW (campaign 88) ③: the witness on the two-chart `Pt`

Campaign 79's `SliceTangency.lean` frame (`ℓ = ∂_V`, `n = 2∂_U` in null coordinates, `g = −dU dV`),
its sequence `x_m = (−e^{−(2m+1)π}, 0)` and the computations behind `st_aligned` /
`st_tangency_fails`, transported to `Pt` through the global chart `φ = extChartAt p₀` (`nullH`), the
way campaign 87 transports the Cauchy hypothesis. -/

namespace Model
open ContinuousLinearMap

set_option synthInstance.maxHeartbeats 400000

/-- The generator direction `ℓ = ∂_V` of `𝓗⁺ = {U = 0}` (campaign 79's `ℓ`). -/
def ellV : P := (0, 1)
/-- The transverse null vector `n = 2∂_U`, `g(ℓ, n) = −1` (campaign 79's `nvec`). -/
def nvec : P := (2, 0)

/-- **The frame hypotheses for `g = −dU dV`** (campaign 80's `tc_frameHyp2` at `F = 1`): `(ℓ, n)`
is a null frame, and any covector with `ξ(∂_U) > 0`, `ξ(∂_V) > 0` is positive on the future cone. -/
theorem mc_frameHyp_gM {ξ : P →L[ℝ] ℝ} (h1 : 0 < ξ (1, 0)) (h2 : 0 < ξ (0, 1)) :
    TCF.FrameHyp gM ellV nvec ξ := by
  refine ⟨⟨fun v w => ?_, ?_, ?_, ?_, fun e he1 he2 => ?_⟩, fun v hv => ?_⟩
  · simp only [TCF.bil_apply, gM_apply]; ring
  · simp only [TCF.bil_apply, gM_apply, ellV]; norm_num
  · simp only [TCF.bil_apply, gM_apply, nvec]; norm_num
  · simp only [TCF.bil_apply, gM_apply, ellV, nvec]; norm_num
  · simp only [TCF.bil_apply, gM_apply, ellV, nvec] at he1 he2 ⊢
    have h1 : e.1 = 0 := by linarith
    have h2 : e.2 = 0 := by linarith
    rw [h1, h2]; norm_num
  · obtain ⟨hv1, hv2⟩ := hv
    simp only [TCF.bil_apply, gM_apply, ellV, nvec, Prod.fst_add, Prod.snd_add] at hv1 hv2
    have hs : 0 < v.1 + 2 * v.2 := by nlinarith
    have hp : 0 ≤ v.1 * v.2 := by nlinarith
    have hv1' : 0 ≤ v.1 := by
      by_contra h; push Not at h
      have : v.2 ≤ 0 := by nlinarith
      nlinarith
    have hv2' : 0 ≤ v.2 := by
      by_contra h; push Not at h
      have : v.1 ≤ 0 := by nlinarith
      nlinarith
    have hv : v = v.1 • ((1, 0) : P) + v.2 • ((0, 1) : P) := by ext <;> simp
    rw [hv, map_add, map_smul, map_smul, smul_eq_mul, smul_eq_mul]
    rcases hv1'.eq_or_lt with h0 | h0
    · rw [← h0] at hs ⊢
      have : 0 < v.2 := by linarith
      simp only [zero_mul, zero_add]; positivity
    · have := mul_pos h0 h1
      nlinarith [mul_nonneg hv2' h2.le]

/-- `dΘ_G(∂_U) > 0` and `dΘ_G(∂_V) = 1` on `{U < 0}`. -/
lemma mc_dTh_pos {G : ℝ → ℝ} (hG : GoodG G) {p : P} (hp : p.1 < 0) :
    0 < dTh G p (1, 0) ∧ 0 < dTh G p (0, 1) := by
  rw [dTh_apply, dTh_apply]
  have := hG.deriv_neg (-p.1) (by linarith)
  constructor
  · simp; linarith
  · simp

/-- `−g(ℓ, ·) = ½ dU`. -/
lemma mc_neg_gM_ell : -(gM ellV) = (1 / 2 : ℝ) • fst ℝ ℝ ℝ := by
  ext
  · simp [gM_apply, ellV]; norm_num
  · simp [gM_apply, ellV]

/-! Campaign 79's sequence, copied. -/

/-- `s_m = e^{−(2m+1)π}`. -/
noncomputable def sm (m : ℕ) : ℝ := Real.exp (-((2 * m + 1) * Real.pi))
/-- `x_m = (U, V) = (−s_m, 0)`. -/
noncomputable def xm (m : ℕ) : P := (-sm m, 0)

lemma log_sm (m : ℕ) : Real.log (sm m) = -((2 * m + 1) * Real.pi) := Real.log_exp _

lemma cos_log_sm (m : ℕ) : Real.cos (Real.log (sm m)) = -1 := by
  rw [log_sm, Real.cos_neg]
  have : (2 * (m:ℝ) + 1) * Real.pi = Real.pi + m * (2 * Real.pi) := by ring
  rw [this, Real.cos_add_nat_mul_two_pi, Real.cos_pi]

lemma deriv_Ffail_sm (m : ℕ) : deriv Ffail (sm m) = -1 := by
  have hs : 0 < sm m := Real.exp_pos _
  rw [(Ffail_hasDerivAt hs).deriv, cos_log_sm]
  ring

lemma xm_mem (m : ℕ) : (xm m).1 < 0 := by
  simp only [xm, Left.neg_neg_iff]; exact Real.exp_pos _

/-- At `x_m`, `dΘ = dU + dV` (campaign 79's `fderiv_xm`, via `dTh`). -/
lemma dTh_xm (m : ℕ) (v : P) : dTh Ffail (xm m) v = v.1 + v.2 := by
  rw [dTh_apply]
  have : -(xm m).1 = sm m := by simp [xm]
  rw [this, deriv_Ffail_sm]; ring

lemma xm_tendsto : Tendsto xm atTop (𝓝 (0, 0)) := by
  have hsm : Tendsto sm atTop (𝓝 0) := by
    refine Real.tendsto_exp_atBot.comp ?_
    refine tendsto_neg_atTop_atBot.comp ?_
    refine Tendsto.atTop_mul_const Real.pi_pos ?_
    exact tendsto_atTop_add_const_right _ 1
      (Tendsto.const_mul_atTop two_pos tendsto_natCast_atTop_atTop)
  have := (hsm.neg).prodMk_nhds (tendsto_const_nhds (x := (0:ℝ)))
  rw [neg_zero] at this
  exact this

end Model

namespace NModel
open Model Manifold ContinuousLinearMap

/-- `φ = extChartAt p₀` (the null chart `nullH`). -/
noncomputable def φ : Pt → P := extChartAt 𝓘(ℝ, P) p₀

lemma φ_continuous : Continuous φ := by
  have e : φ = fun x => nullH x := funext chart_apply
  rw [e]; exact nullH.continuous

lemma ψ_continuous : Continuous ψ := by
  have h := continuousOn_extChartAt_symm (I := 𝓘(ℝ, P)) p₀
  rw [target_eq] at h
  exact continuousOn_univ.1 h

lemma φ_p₀ : φ p₀ = (0, 0) := by
  show extChartAt 𝓘(ℝ, P) p₀ p₀ = _
  rw [chart_apply]
  show ((0:ℝ) - 0, (0:ℝ) + 0) = ((0:ℝ), (0:ℝ))
  norm_num

lemma ψ_zero : ψ (0, 0) = p₀ := by
  rw [← φ_p₀]; exact ch_left_inv p₀ (src p₀)

lemma mem_D_JN_iff (x : Pt) : x ∈ minkN.D JN ↔ (φ x).1 < 0 := by
  rw [JN, mem_D_N, hl_D_eq]; rfl

lemma φ_tendsto (q : Pt) :
    Tendsto φ (𝓝[minkN.D JN] q) (𝓝[{p : P | p.1 < 0}] (φ q)) :=
  tendsto_nhdsWithin_iff.2 ⟨(φ_continuous.tendsto q).mono_left nhdsWithin_le_nhds,
    eventually_mem_nhdsWithin.mono fun x hx => (mem_D_JN_iff x).1 hx⟩

/-- The intrinsic null frame on `Pt`: `ℓ = ∂_V`, `n = 2∂_U` (null coordinates), read in each
point's preferred chart. -/
noncomputable def ℓN (x : Pt) : P := dchartInvL p₀ x ellV
noncomputable def nN (x : Pt) : P := dchartInvL p₀ x nvec

lemma A_ℓN (x : Pt) : dchartL p₀ x (ℓN x) = ellV := mc_AB p₀ (src x) _
lemma A_nN (x : Pt) : dchartL p₀ x (nN x) = nvec := mc_AB p₀ (src x) _

/-- `dΘ_x` read in `φ` is `dΘ_G` at `φ x`. -/
lemma covCh_ThetaG {G : ℝ → ℝ} (hG : GoodG G) {x : Pt} (hx : x ∈ minkN.D JN) :
    covCh (ThetaG G ∘ φ) p₀ x = dTh G (φ x) := by
  have hx' := (mem_D_JN_iff x).1 hx
  rw [φ, mc_covCh_comp_chart p₀ (src x) (hG.hasFDerivAt hx').differentiableAt]
  exact hG.fderiv_eq hx'

lemma dcov_ℓN {G : ℝ → ℝ} (hG : GoodG G) {x : Pt} (hx : x ∈ minkN.D JN) :
    dcov (ThetaG G ∘ φ) x (ℓN x) = dTh G (φ x) ellV := by
  show covCh (ThetaG G ∘ φ) p₀ x ellV = _
  rw [covCh_ThetaG hG hx]

lemma dcov_nN {G : ℝ → ℝ} (hG : GoodG G) {x : Pt} (hx : x ∈ minkN.D JN) :
    dcov (ThetaG G ∘ φ) x (nN x) = dTh G (φ x) nvec := by
  show covCh (ThetaG G ∘ φ) p₀ x nvec = _
  rw [covCh_ThetaG hG hx]

lemma gCh_p₀ (x : Pt) : minkN.gCh p₀ x = gM := by
  show hRep minkN.g p₀ _ = gM
  rw [hRep_eq]

/-- **The intrinsic frame hypotheses on `Pt`, for every good profile, at every point of `D`.** -/
theorem mc_witness_frameHyp {G : ℝ → ℝ} (hG : GoodG G) {x : Pt} (hx : x ∈ minkN.D JN) :
    TCF.FrameHyp (minkN.gE x) (ℓN x) (nN x) (dcov (ThetaG G ∘ φ) x) := by
  refine minkN.mc_frameHyp_ofChart p₀ (src x) ?_
  rw [gCh_p₀, covCh_ThetaG hG hx]
  have h := mc_dTh_pos hG ((mem_D_JN_iff x).1 hx)
  exact mc_frameHyp_gM h.1 h.2

lemma ratio_Θ₀ {x : Pt} (hx : x ∈ minkN.D JN) :
    dcov (Θ₀ ∘ φ) x (ℓN x) / dcov (Θ₀ ∘ φ) x (nN x) = -(φ x).1 / 2 := by
  have hx' := (mem_D_JN_iff x).1 hx
  have hs : (0:ℝ) < -(φ x).1 := by linarith
  rw [Θ₀, dcov_ℓN goodG_log hx, dcov_nN goodG_log hx, dTh_apply, dTh_apply]
  have hl : HasDerivAt (fun s => -Real.log s) (-(-(φ x).1)⁻¹) (-(φ x).1) :=
    (Real.hasDerivAt_log hs.ne').neg
  rw [hl.deriv]
  simp only [ellV, nvec]
  have hne : (φ x).1 ≠ 0 := hx'.ne
  field_simp
  ring

/-- **③ Alignment holds for `Θ₀ ∘ φ` at every horizon point (BUILT).** Along `𝓝[D] q` (a proper
filter): the intrinsic frame hypotheses, the rate `dΘ(ℓ)/dΘ(n) = −U/2 → 0`, the conclusion of
`mc_tangency_N` in the chart `φ`, and the limit `dΘ^φ/dΘ(n) → −g(ℓ, ·) = ½ dU` by
`mc_tangency_limit_N`. -/
theorem mc_witness_tangency_holds (q : Pt) (hq : q ∈ minkN.H JN) :
    minkN.IsCauchyTemporalOn (minkN.D JN) (Θ₀ ∘ φ) ∧ (𝓝[minkN.D JN] q).NeBot ∧
    (∀ᶠ x in 𝓝[minkN.D JN] q, TCF.FrameHyp (minkN.gE x) (ℓN x) (nN x) (dcov (Θ₀ ∘ φ) x)) ∧
    Tendsto (fun x => dcov (Θ₀ ∘ φ) x (ℓN x) / dcov (Θ₀ ∘ φ) x (nN x)) (𝓝[minkN.D JN] q)
      (𝓝 0) ∧
    Tendsto (fun x => (dcov (Θ₀ ∘ φ) x (nN x))⁻¹ • covCh (Θ₀ ∘ φ) p₀ x +
      minkN.gCh p₀ x (dchartL p₀ x (ℓN x))) (𝓝[minkN.D JN] q) (𝓝 0) ∧
    Tendsto (fun x => (dcov (Θ₀ ∘ φ) x (nN x))⁻¹ • covCh (Θ₀ ∘ φ) p₀ x) (𝓝[minkN.D JN] q)
      (𝓝 ((1 / 2 : ℝ) • fst ℝ ℝ ℝ)) := by
  have hne : (𝓝[minkN.D JN] q).NeBot :=
    mem_closure_iff_nhdsWithin_neBot.1
      (minkN.mh_hcl me_locallyOneChart (subset_univ _) (frontier_subset_closure hq))
  have hF : ∀ᶠ x in 𝓝[minkN.D JN] q,
      TCF.FrameHyp (minkN.gE x) (ℓN x) (nN x) (dcov (Θ₀ ∘ φ) x) := by
    filter_upwards [self_mem_nhdsWithin] with x hx using mc_witness_frameHyp goodG_log hx
  have hq0 : (φ q).1 = 0 := (mem_H_N q).1 hq
  have hr : Tendsto (fun x => dcov (Θ₀ ∘ φ) x (ℓN x) / dcov (Θ₀ ∘ φ) x (nN x))
      (𝓝[minkN.D JN] q) (𝓝 0) := by
    have hc : Tendsto (fun x => -(φ x).1 / 2) (𝓝[minkN.D JN] q) (𝓝 0) := by
      have := (((continuous_fst.comp φ_continuous).neg.div_const (2:ℝ)).tendsto q).mono_left
        (nhdsWithin_le_nhds (s := minkN.D JN))
      simpa [Function.comp_def, hq0] using this
    refine hc.congr' ?_
    filter_upwards [self_mem_nhdsWithin] with x hx using (ratio_Θ₀ hx).symm
  have hgn : ∀ᶠ x in 𝓝[minkN.D JN] q, ‖minkN.gCh p₀ x‖ * ‖dchartL p₀ x (nN x)‖ ≤
      ‖gM‖ * ‖nvec‖ + ‖gM‖ + ‖ellV‖ :=
    Eventually.of_forall fun x => by
      rw [gCh_p₀, A_nN]; have := norm_nonneg gM; have := norm_nonneg ellV; linarith
  have h1 := minkN.mc_tangency_N p₀ (C := ‖gM‖ * ‖nvec‖ + ‖gM‖ + ‖ellV‖)
    (Eventually.of_forall fun x => src x) hF
    (Eventually.of_forall fun x => by
      rw [gCh_p₀]; have := mul_nonneg (norm_nonneg gM) (norm_nonneg nvec)
      have := norm_nonneg ellV; linarith) hgn
    (Eventually.of_forall fun x => by
      rw [A_ℓN]; have := mul_nonneg (norm_nonneg gM) (norm_nonneg nvec)
      have := norm_nonneg gM; linarith) hr
  have hgc : ContinuousAt (hRep minkN.g p₀) (extChartAt 𝓘(ℝ, P) p₀ q) := by
    rw [hRep_eq]; exact continuousAt_const
  have h2 := minkN.mc_tangency_limit_N p₀ (src q) nhdsWithin_le_nhds (C := ‖nvec‖) (ℓ₀ := ellV)
    hgc hF (Eventually.of_forall fun x => by rw [A_nN])
    (tendsto_const_nhds.congr fun x => (A_ℓN x).symm) hr
  rw [hRep_eq] at h2
  obtain ⟨-, -, -, -, -, hΘ, -⟩ := ch_witness_hypotheses goodG_log
  exact ⟨hΘ, hne, hF, hr, h1, by simpa only [mc_neg_gM_ell] using h2⟩

/-- The coordinate change from `idH` (the chart at `(−1, 0)`) to `nullH` at `p₀` is `nullL`. -/
lemma tCC_neg_p₀ : tangentCoordChange 𝓘(ℝ, P) (mkPt (-1) 0) p₀ p₀ = nullL := by
  have hneg : tco (mkPt (-1) 0) < 0 := by show (-1 : ℝ) < 0; norm_num
  refine ContinuousLinearMap.ext fun w => ?_
  rw [mc_tCC_eq (src_neg hneg p₀) (src p₀)]
  have h1 : dchartInvL (mkPt (-1) 0) p₀ w = nullL w := by
    show dchartInv (mkPt (-1) 0) (extChartAt 𝓘(ℝ, P) (mkPt (-1) 0) p₀) w = _
    rw [dinv_neg hneg, ite_eq_right (show ¬ tco p₀ < 0 from lt_irrefl (0:ℝ))]
  rw [h1]
  exact mc_A_self p₀ _

/-- **③ At `q = p₀ = (0,0)`, in the preferred chart at `q` (`LocallyOneChart`), and re-read in the
other chart `idH` (BUILT).** `mc_tangency_at_N` gives `dΘ^{e_q}/dΘ(n) → −g_q(ℓ, ·) = ½ dU`, and
`mc_chart_change` moves the limit to the chart at `(−1, 0)` (`idH`, `(t, x)` coordinates, a different
chart) as `½ dU ∘ tangentCoordChange = ½ dU ∘ nullL = ½ (dt − dx)`. -/
theorem mc_witness_tangency_at :
    p₀ ∈ minkN.H JN ∧
    Tendsto (fun x => (dcov (Θ₀ ∘ φ) x (nN x))⁻¹ • covCh (Θ₀ ∘ φ) p₀ x) (𝓝[minkN.D JN] p₀)
      (𝓝 (-(minkN.gE p₀ ellV))) ∧
    minkN.gE p₀ = gM ∧
    chartAt P (mkPt (-1) 0) ≠ chartAt P p₀ ∧
    Tendsto (fun x => (dcov (Θ₀ ∘ φ) x (nN x))⁻¹ • covCh (Θ₀ ∘ φ) (mkPt (-1) 0) x)
      (𝓝[minkN.D JN] p₀)
      (𝓝 ((-(gM ellV)).comp (tangentCoordChange 𝓘(ℝ, P) (mkPt (-1) 0) p₀ p₀))) ∧
    (-(gM ellV)).comp (tangentCoordChange 𝓘(ℝ, P) (mkPt (-1) 0) p₀ p₀) =
      (1 / 2 : ℝ) • (fst ℝ ℝ ℝ - snd ℝ ℝ ℝ) := by
  have hp : p₀ ∈ minkN.H JN := (mem_H_N p₀).2 (by rw [show extChartAt 𝓘(ℝ, P) p₀ p₀ = φ p₀ from rfl,
    φ_p₀])
  obtain ⟨-, -, hF, hr, -, -⟩ := mc_witness_tangency_holds p₀ hp
  have hg : minkN.gE p₀ = gM := by
    show gN p₀ = gM
    unfold gN; rw [ite_eq_right (show ¬ tco p₀ < 0 from lt_irrefl (0:ℝ))]
  have h := minkN.mc_tangency_at_N me_locallyOneChart (mem_univ p₀) nhdsWithin_le_nhds
    (C := ‖nvec‖) (ℓ₀ := ellV) hF (Eventually.of_forall fun x => by rw [A_nN])
    (tendsto_const_nhds.congr fun x => (A_ℓN x).symm) hr
  have hneg : tco (mkPt (-1) 0) < 0 := by show (-1 : ℝ) < 0; norm_num
  refine ⟨hp, h, hg, ?_, ?_, ?_⟩
  · rw [chartAt_neg hneg, chartAt_p₀]
    intro h'
    have := congrArg (fun e : OpenPartialHomeomorph Pt P => e (mkPt 1 0)) h'
    have h2 : idH (mkPt 1 0) = nullH (mkPt 1 0) := this
    have h3 := congrArg Prod.snd h2
    change (0:ℝ) = 1 + 0 at h3
    norm_num at h3
  · rw [hg] at h
    exact mc_chart_change (Θ₀ ∘ φ) (src_neg hneg p₀) (src p₀) nhdsWithin_le_nhds h
  · rw [tCC_neg_p₀]
    ext
    · simp [nullL_apply, gM_apply, ellV]; norm_num
    · simp [nullL_apply, gM_apply, ellV]

/-- **③ Alignment fails for `Θf ∘ φ` (BUILT).** At the horizon point `p₀`: the intrinsic frame
hypotheses hold on all of `D` and `Θf ∘ φ` is two-sided Cauchy temporal on `D` (campaign 87's
witness), yet along the points `ψ(x_m) → p₀` of `D`, `dΘ = dU + dV`, so the rate is `1/2` and does
not tend to `0`, and the conclusion `dΘ^φ/dΘ(n) → −g(ℓ, ·)` fails (its value on `ℓ` is `1/2`, not
`0`). -/
theorem mc_witness_tangency_fails :
    p₀ ∈ minkN.H JN ∧
    minkN.IsCauchyTemporalOn (minkN.D JN) (Θf ∘ φ) ∧
    (∀ x ∈ minkN.D JN, TCF.FrameHyp (minkN.gE x) (ℓN x) (nN x) (dcov (Θf ∘ φ) x)) ∧
    ¬ Tendsto (fun x => dcov (Θf ∘ φ) x (ℓN x) / dcov (Θf ∘ φ) x (nN x)) (𝓝[minkN.D JN] p₀)
      (𝓝 0) ∧
    ¬ Tendsto (fun x => (dcov (Θf ∘ φ) x (nN x))⁻¹ • covCh (Θf ∘ φ) p₀ x) (𝓝[minkN.D JN] p₀)
      (𝓝 (-(gM ellV))) := by
  have hp : p₀ ∈ minkN.H JN := (mem_H_N p₀).2 (by rw [show extChartAt 𝓘(ℝ, P) p₀ p₀ = φ p₀ from rfl,
    φ_p₀])
  obtain ⟨-, -, -, -, -, hΘ, -⟩ := ch_witness_hypotheses goodG_Ffail
  have hmem : ∀ m, ψ (xm m) ∈ minkN.D JN := fun m => by
    rw [mem_D_JN_iff]; show (extChartAt 𝓘(ℝ, P) p₀ (ψ (xm m))).1 < 0
    rw [φψ]; exact xm_mem m
  have hφx : ∀ m, φ (ψ (xm m)) = xm m := fun m => φψ _
  have hseq : Tendsto (fun m => ψ (xm m)) atTop (𝓝[minkN.D JN] p₀) := by
    refine tendsto_nhdsWithin_iff.2 ⟨?_, Eventually.of_forall hmem⟩
    rw [← ψ_zero]; exact (ψ_continuous.tendsto _).comp xm_tendsto
  have hval : ∀ m, covCh (Θf ∘ φ) p₀ (ψ (xm m)) = dTh Ffail (xm m) := fun m => by
    rw [Θf, covCh_ThetaG goodG_Ffail (hmem m), hφx]
  have hn : ∀ m, dcov (Θf ∘ φ) (ψ (xm m)) (nN (ψ (xm m))) = 2 := fun m => by
    rw [Θf, dcov_nN goodG_Ffail (hmem m), hφx, dTh_xm]; simp [nvec]
  have hl : ∀ m, dcov (Θf ∘ φ) (ψ (xm m)) (ℓN (ψ (xm m))) = 1 := fun m => by
    rw [Θf, dcov_ℓN goodG_Ffail (hmem m), hφx, dTh_xm]; simp [ellV]
  refine ⟨hp, hΘ, fun x hx => mc_witness_frameHyp goodG_Ffail hx, fun h => ?_, fun h => ?_⟩
  · have h2 := h.comp hseq
    have hc : ((fun x => dcov (Θf ∘ φ) x (ℓN x) / dcov (Θf ∘ φ) x (nN x)) ∘
        fun m => ψ (xm m)) = fun _ => (1:ℝ) / 2 := by
      funext m; simp only [Function.comp_apply, hl, hn]
    rw [hc] at h2
    have := tendsto_nhds_unique h2 tendsto_const_nhds
    norm_num at this
  · have h2 := ((ContinuousLinearMap.apply ℝ ℝ ellV).continuous.tendsto _).comp (h.comp hseq)
    have hc : (ContinuousLinearMap.apply ℝ ℝ ellV ∘ (fun x =>
        (dcov (Θf ∘ φ) x (nN x))⁻¹ • covCh (Θf ∘ φ) p₀ x) ∘ fun m => ψ (xm m)) =
        fun _ => (1:ℝ) / 2 := by
      funext m
      simp only [Function.comp_apply, ContinuousLinearMap.apply_apply, smul_apply, hn, hval,
        dTh_xm, smul_eq_mul]
      simp [ellV]
    rw [hc] at h2
    have := tendsto_nhds_unique h2 tendsto_const_nhds
    simp [gM_apply, ellV] at this

/-- **③ Cone convergence on `Pt` (BUILT).** For the observer of campaign 87's witness:
`KLi(∂J⁻(O τ)) = KLs(∂J⁻(O τ)) = 𝓗⁺ = {U = 0}` (non-empty), via `mc_cone_kuratowski_N`. -/
theorem mc_witness_cones :
    ∃ O_N : ℝ → Pt, minkN.IpastSet (range O_N) = minkN.D JN ∧
      (∀ s t : ℝ, s < t → minkN.Chr (O_N s) (O_N t)) ∧
      KLi (minkN.cone O_N) = minkN.H JN ∧ KLs (minkN.cone O_N) = minkN.H JN ∧
      (∀ x : Pt, x ∈ minkN.H JN ↔ (φ x).1 = 0) ∧ (minkN.H JN).Nonempty := by
  obtain ⟨O_N, hOD, hmono, hJM, -, -, -⟩ := ch_witness_hypotheses goodG_log
  obtain ⟨h1, h2⟩ := MSpacetime.mc_cone_kuratowski_N me_locallyOneChart hOD hmono hJM
  exact ⟨O_N, hOD, hmono, h1, h2, mem_H_N, ⟨ψ (0, 0), (mem_H_N _).2 (by rw [φψ])⟩⟩

end NModel

/-! ## NEW (campaign 89) ②: the witness, `Pt` compactified by `arctan V` inside `Pt`

In null coordinates `(U, V) = φ x`, `ι = ψ ∘ mx_fA ∘ φ` with `mx_fA (U, V) = (U, arctan V)`, so
`ι(Pt) = φ⁻¹{−π/2 < V < π/2}` and `𝒥⁺ = φ⁻¹{(U, π/2) : U < 0}` lies on its frontier. With
`g = −dU dV`, `Dι = diag(1, 1/(1+V²))` in `φ`, so `Ω² = 1/(1+V²)`. -/

namespace NModel
open Model Manifold ContinuousLinearMap

/-- `(U, V) ↦ (U, arctan V)`. -/
noncomputable def mx_fA (y : P) : P := (y.1, Real.arctan y.2)

/-- `mx_DfA = diag(1, 1/(1+V²))`. -/
noncomputable def mx_DfA (y : P) : P →L[ℝ] P :=
  (fst ℝ ℝ ℝ).prod ((1 / (1 + y.2 ^ 2)) • snd ℝ ℝ ℝ)

lemma mx_DfA_apply (y v : P) : mx_DfA y v = (v.1, (1 / (1 + y.2 ^ 2)) * v.2) := by
  simp [mx_DfA]

lemma mx_fA_hasFDerivAt (y : P) : HasFDerivAt mx_fA (mx_DfA y) y :=
  hasFDerivAt_fst.prodMk ((Real.hasDerivAt_arctan y.2).comp_hasFDerivAt y hasFDerivAt_snd)

lemma mx_fA_contDiff : ContDiff ℝ 1 mx_fA :=
  contDiff_fst.prodMk (Real.contDiff_arctan.comp contDiff_snd)

lemma mx_arctan_eq : Real.arctan = Subtype.val ∘ Real.tanOrderIso.symm := rfl

lemma mx_arctan_isOpenEmbedding : IsOpenEmbedding Real.arctan := by
  rw [mx_arctan_eq]
  exact isOpen_Ioo.isOpenEmbedding_subtypeVal.comp
    Real.tanOrderIso.symm.toHomeomorph.isOpenEmbedding

lemma mx_fA_isOpenEmbedding : IsOpenEmbedding mx_fA :=
  IsOpenEmbedding.id.prodMap mx_arctan_isOpenEmbedding

/-- **The witness's embedding** `ι = ψ ∘ mx_fA ∘ φ : Pt → Pt`. -/
noncomputable def mx_ι : Pt → Pt := ψ ∘ mx_fA ∘ φ

lemma mx_φ_eq : φ = fun x => nullH x := funext chart_apply

lemma mx_ψ_eq (y : P) : ψ y = nullH.symm y := by
  rw [Homeomorph.eq_symm_apply]; exact (chart_apply _).symm.trans (φψ y)

lemma mx_φ_ι (x : Pt) : φ (mx_ι x) = mx_fA (φ x) := φψ _

lemma mx_ι_isOpenEmbedding : IsOpenEmbedding mx_ι := by
  have e : mx_ι = nullH.symm ∘ mx_fA ∘ nullH := by
    funext x; show ψ (mx_fA (φ x)) = _; rw [mx_ψ_eq, mx_φ_eq]; rfl
  rw [e]
  exact nullH.symm.isOpenEmbedding.comp (mx_fA_isOpenEmbedding.comp nullH.isOpenEmbedding)

lemma mx_φ_contMDiff : ContMDiff 𝓘(ℝ, P) 𝓘(ℝ, P) 1 φ := by
  have h := contMDiffOn_extChartAt (I := 𝓘(ℝ, P)) (n := 1) (x := p₀)
  rw [source_eq] at h
  exact contMDiffOn_univ.1 h

lemma mx_ψ_contMDiff : ContMDiff 𝓘(ℝ, P) 𝓘(ℝ, P) 1 ψ := by
  have h := contMDiffOn_extChartAt_symm (I := 𝓘(ℝ, P)) (n := 1) p₀
  rw [target_eq] at h
  exact contMDiffOn_univ.1 h

/-- **`ι` is `C¹` through the `nullH` chart** (the registered expected stop). -/
lemma mx_ι_contMDiff : ContMDiff 𝓘(ℝ, P) 𝓘(ℝ, P) 1 mx_ι :=
  mx_ψ_contMDiff.comp ((contMDiff_iff_contDiff.2 mx_fA_contDiff).comp mx_φ_contMDiff)

/-- `Dφ ∘ Dψ = id` at `ψ y`. -/
lemma mx_dchart_dchartInv (y a : P) : dchart p₀ (ψ y) (dchartInv p₀ y a) = a := by
  have h := ld_mfderiv_chart_symm p₀ (src (ψ y)) a
  have e : extChartAt 𝓘(ℝ, P) p₀ (ψ y) = y := φψ y
  rw [e] at h
  exact h

/-- `Dι` read in `φ` at both ends is `mx_DfA`. -/
lemma mx_dι_eq (x : Pt) (v : P) :
    dchart p₀ (mx_ι x) (mx_dι mx_ι x v) =
      mx_DfA (φ x) (dchart p₀ x v) := by
  have hφ : MDifferentiableAt 𝓘(ℝ, P) 𝓘(ℝ, P) φ x :=
    mdifferentiableAt_extChartAt (src x)
  have hf : MDifferentiableAt 𝓘(ℝ, P) 𝓘(ℝ, P) mx_fA (φ x) :=
    mdifferentiableAt_iff_differentiableAt.2 (mx_fA_hasFDerivAt _).differentiableAt
  have hψ : MDifferentiableAt 𝓘(ℝ, P) 𝓘(ℝ, P) ψ (mx_fA (φ x)) :=
    ld_mdifferentiableAt_symm p₀ (by rw [target_eq]; exact mem_univ _)
  have hfφ : MDifferentiableAt 𝓘(ℝ, P) 𝓘(ℝ, P) (mx_fA ∘ φ) x := hf.comp x hφ
  have h1 : mx_dι mx_ι x = (mx_dι (E := P) ψ (mx_fA (φ x))).comp ((mx_dι (E := P) mx_fA (φ x)).comp (mx_dι (E := P) φ x)) := by
    show mfderiv 𝓘(ℝ, P) 𝓘(ℝ, P) (ψ ∘ (mx_fA ∘ φ)) x = _
    rw [mfderiv_comp x hψ hfφ, mfderiv_comp x hf hφ]
    rfl
  have h2 : mx_dι (E := P) mx_fA (φ x) = mx_DfA (φ x) := by
    show mfderiv 𝓘(ℝ, P) 𝓘(ℝ, P) mx_fA (φ x) = _
    rw [mfderiv_eq_fderiv]; exact (mx_fA_hasFDerivAt _).fderiv
  rw [h1, ContinuousLinearMap.comp_apply, ContinuousLinearMap.comp_apply, h2]
  exact mx_dchart_dchartInv (mx_fA (φ x)) _

/-- The metric of `minkN` read in `φ`: `g_x(v, w) = gM(Dφ v, Dφ w)`. -/
lemma mx_g_eq_gM (x : Pt) (v w : P) :
    minkN.gE x v w = gM (dchart p₀ x v) (dchart p₀ x w) := by
  have h := ld_h_eq_hRep minkN.g p₀ (src x) v w
  rw [hRep_eq] at h
  exact h

/-- `gM(mx_DfA a, mx_DfA b) = gM(a, b)/(1+V²)`. -/
lemma mx_gM_DfA (y a b : P) : gM (mx_DfA y a) (mx_DfA y b) = (1 / (1 + y.2 ^ 2)) * gM a b := by
  rw [mx_DfA_apply, mx_DfA_apply, gM_apply, gM_apply]; ring

/-- The conformal factor `Ω = (1 + V²)^{−1/2}`. -/
noncomputable def mx_Ω (x : Pt) : ℝ := (Real.sqrt (1 + (φ x).2 ^ 2))⁻¹

lemma mx_Ω_pos (x : Pt) : 0 < mx_Ω x := inv_pos.2 (Real.sqrt_pos.2 (by positivity))

lemma mx_Ω_sq (x : Pt) : mx_Ω x ^ 2 = 1 / (1 + (φ x).2 ^ 2) := by
  rw [mx_Ω, inv_pow, Real.sq_sqrt (by positivity), one_div]

lemma mx_dchart_T (x : Pt) : dchart p₀ x (TN x) = ((1, 1) : P) := by
  have h := ld_chartRep_apply_chart minkN.T p₀ (src x)
  rw [chartRep_eq] at h
  exact h.symm

/-- **The conformal extension on `Pt` (BUILT): every field.** -/
noncomputable def mx_witnessExt : ConformalExtension minkN minkN where
  ι := mx_ι
  isOpenEmbedding := mx_ι_isOpenEmbedding
  contMDiff := mx_ι_contMDiff
  Ω := mx_Ω
  Ω_pos := mx_Ω_pos
  conformal := fun x v w => by
    rw [mx_g_eq_gM, mx_g_eq_gM, mx_dι_eq, mx_dι_eq, mx_gM_DfA, mx_Ω_sq]
  timeOrient := fun x _ => by
    rw [← MSpacetime.futTimelike_chart ch_oneChart (src (mx_ι x)), ch_chartSp_eq]
    show mink.FutTimelike _ (dchart p₀ (mx_ι x) (mx_dι mx_ι x (TN x)))
    rw [mx_dι_eq, mx_dchart_T, futTimelike_iff, mx_DfA_apply]
    exact ⟨one_pos, by simp only [mul_one]; positivity⟩
  maps_M := subset_univ _

/-- `𝒥⁺` in null coordinates: `{(U, π/2) : U < 0}`. -/
def mx_JA : Set P := {p : P | p.1 < 0 ∧ p.2 = Real.pi / 2}

/-- `𝒥⁺ = φ⁻¹{(U, π/2) : U < 0}` on `Pt`. -/
noncomputable def mx_scri : Set Pt := ψ '' mx_JA

/-- **`I⁻(𝒥⁺)` in null coordinates** (`chr_lt`, `tstep_of_lt`): `{U < 0, V < π/2}`. -/
lemma mx_mem_mink_D_JA (p : P) : p ∈ mink.D mx_JA ↔ p.1 < 0 ∧ p.2 < Real.pi / 2 := by
  show p ∈ ⋃ a ∈ mx_JA, mink.Ipast a ↔ _
  rw [mem_iUnion₂]
  constructor
  · rintro ⟨a, ⟨ha1, ha2⟩, hpa⟩
    have h := chr_lt hpa
    exact ⟨h.1.trans ha1, ha2 ▸ h.2⟩
  · rintro ⟨h1, h2⟩
    refine ⟨(p.1 / 2, Real.pi / 2), ⟨by simp only; linarith, rfl⟩,
      Relation.TransGen.single (tstep_of_lt (by simp only; linarith) h2)⟩

lemma mx_mem_Ipast_scri (x : Pt) :
    x ∈ minkN.IpastSet mx_scri ↔ (φ x).1 < 0 ∧ (φ x).2 < Real.pi / 2 :=
  (mem_D_N mx_JA x).trans (mx_mem_mink_D_JA _)

/-- **`hI` on the witness (BUILT):** `ι⁻¹ Ĩ⁻(𝒥⁺) = {U < 0} = D`. -/
lemma mx_preimage_Ipast_scri : mx_ι ⁻¹' minkN.IpastSet mx_scri = minkN.D JN := by
  ext x
  rw [mem_preimage, mx_mem_Ipast_scri, mx_φ_ι, mem_D_JN_iff]
  exact ⟨fun h => h.1, fun h => ⟨h, Real.arctan_lt_pi_div_two _⟩⟩

/-- **`𝒥⁺ ⊆ ∂ι(Pt)`** (BUILT): `ψ(U, π/2)` is not in `ι(Pt)` (`arctan < π/2`) but is the limit of
`ψ(U, s) = ι(ψ(U, tan s))` as `s → π/2⁻`. -/
lemma mx_scri_subset_frontier : mx_scri ⊆ frontier (range mx_ι) := by
  rintro _ ⟨p, ⟨hp1, hp2⟩, rfl⟩
  have hnot : ψ p ∉ range mx_ι := by
    rintro ⟨w, hw⟩
    have h := congrArg Prod.snd (congrArg φ hw)
    rw [mx_φ_ι, show φ (ψ p) = p from φψ p] at h
    have := Real.arctan_lt_pi_div_two (φ w).2
    change Real.arctan (φ w).2 = p.2 at h
    linarith
  have hpi := Real.pi_pos
  have hcl : ψ p ∈ closure (range mx_ι) := by
    have ht : Tendsto (fun s : ℝ => ψ (p.1, s)) (𝓝[<] (Real.pi / 2)) (𝓝 (ψ p)) := by
      have hc : Continuous fun s : ℝ => ψ (p.1, s) :=
        ψ_continuous.comp (continuous_const.prodMk continuous_id)
      have h0 : ψ p = (fun s : ℝ => ψ (p.1, s)) (Real.pi / 2) := by
        simp only; rw [← hp2]
      rw [h0]; exact (hc.tendsto _).mono_left nhdsWithin_le_nhds
    refine mem_closure_of_tendsto ht ?_
    filter_upwards [Ioo_mem_nhdsLT (show -(Real.pi / 2) < Real.pi / 2 by linarith)] with s hs
    refine ⟨ψ (p.1, Real.tan s), ?_⟩
    show ψ (mx_fA (φ (ψ (p.1, Real.tan s)))) = _
    rw [show φ (ψ (p.1, Real.tan s)) = (p.1, Real.tan s) from φψ _]
    show ψ (p.1, Real.arctan (Real.tan s)) = _
    rw [Real.arctan_tan hs.1 hs.2]
  exact ⟨hcl, fun h => hnot (interior_subset h)⟩

/-- **② The witness (BUILT).** On `Pt`, with `ι = ψ ∘ (id × arctan) ∘ φ`, `Ω² = 1/(1+V²)` and
`𝒥⁺ = φ⁻¹{(U, π/2) : U < 0}`: `ι` is a conformal extension (`mx_witnessExt`), `𝒥⁺ ⊆ ∂ι(Pt)`,
`𝒥⁺ ⊆ M̃`, `Ĩ⁻(𝒥⁺) = φ⁻¹{U < 0, V < π/2}`, `hI : I⁻(O) = ι⁻¹ Ĩ⁻(𝒥⁺)`, and by
`mx_H_eq_boundary`: `{U = 0} = 𝓗⁺ = ∂J⁻(𝒥⁺)`, a non-empty set. -/
theorem mx_witness_boundary :
    ∃ O_N : ℝ → Pt, minkN.IpastSet (range O_N) = minkN.D JN ∧
      (∀ s t : ℝ, s < t → minkN.Chr (O_N s) (O_N t)) ∧
      mx_witnessExt.ι = ψ ∘ mx_fA ∘ φ ∧ (∀ x, mx_witnessExt.Ω x ^ 2 = 1 / (1 + (φ x).2 ^ 2)) ∧
      mx_scri ⊆ frontier (range mx_witnessExt.ι) ∧ mx_scri ⊆ minkN.M ∧ mx_scri.Nonempty ∧
      (∀ x, x ∈ minkN.IpastSet mx_scri ↔ (φ x).1 < 0 ∧ (φ x).2 < Real.pi / 2) ∧
      minkN.IpastSet (range O_N) = mx_witnessExt.ι ⁻¹' minkN.IpastSet mx_scri ∧
      minkN.H (range O_N) = frontier (mx_witnessExt.ι ⁻¹' minkN.JpastSet mx_scri) ∧
      minkN.H JN = frontier (mx_witnessExt.ι ⁻¹' minkN.JpastSet mx_scri) ∧
      (∀ x, x ∈ frontier (mx_witnessExt.ι ⁻¹' minkN.JpastSet mx_scri) ↔ (φ x).1 = 0) ∧
      (frontier (mx_witnessExt.ι ⁻¹' minkN.JpastSet mx_scri)).Nonempty := by
  obtain ⟨O_N, hOD, hmono, hJM, -, -, -⟩ := ch_witness_hypotheses goodG_log
  have hI : minkN.IpastSet (range O_N) = mx_witnessExt.ι ⁻¹' minkN.IpastSet mx_scri := by
    rw [hOD]; exact mx_preimage_Ipast_scri.symm
  have hB := MSpacetime.mx_H_eq_boundary me_locallyOneChart me_locallyOneChart mx_witnessExt
    (subset_univ _) hOD hmono hJM hI
  have hmem : ∀ x, x ∈ frontier (mx_witnessExt.ι ⁻¹' minkN.JpastSet mx_scri) ↔ (φ x).1 = 0 :=
    fun x => by rw [← hB.2]; exact mem_H_N x
  refine ⟨O_N, hOD, hmono, rfl, mx_Ω_sq, mx_scri_subset_frontier, subset_univ _,
    ⟨ψ (-1, Real.pi / 2), mem_image_of_mem ψ (show ((-1 : ℝ), Real.pi / 2) ∈ mx_JA from ⟨by norm_num, rfl⟩)⟩, mx_mem_Ipast_scri, hI, hB.1, hB.2, hmem,
    ⟨ψ (0, 0), (hmem _).2 (by rw [show φ (ψ (0, 0)) = (0, 0) from φψ _])⟩⟩

/-- **③ The headline witnessed end to end on `Pt` (BUILT), for `Θ₀ ∘ φ`.** Every hypothesis of
`mx_prop_causal_alignment` is discharged, and its conclusion read off: `𝓗⁺ = ∂J⁻(𝒥⁺) = {U = 0}`
(non-empty), properness, `KLi = KLs = ∂J⁻(𝒥⁺)` for slices and for past cones, and the tangency
clause, whose hypotheses are discharged at the horizon point `p₀` with the frame `(ℓN, nN)` along
`𝓝[D] p₀`, giving the limit `−g_{p₀}(ℓ, ·)`. -/
theorem mx_witness_headline :
    ∃ O_N : ℝ → Pt,
      (∀ x, x ∈ frontier (mx_witnessExt.ι ⁻¹' minkN.JpastSet mx_scri) ↔ (φ x).1 = 0) ∧
      (frontier (mx_witnessExt.ι ⁻¹' minkN.JpastSet mx_scri)).Nonempty ∧
      minkN.H JN = frontier (mx_witnessExt.ι ⁻¹' minkN.JpastSet mx_scri) ∧
      minkN.SublevelProper JN (Θ₀ ∘ φ) ∧
      KLi (minkN.slice JN (Θ₀ ∘ φ)) = frontier (mx_witnessExt.ι ⁻¹' minkN.JpastSet mx_scri) ∧
      KLs (minkN.slice JN (Θ₀ ∘ φ)) = frontier (mx_witnessExt.ι ⁻¹' minkN.JpastSet mx_scri) ∧
      KLi (minkN.cone O_N) = frontier (mx_witnessExt.ι ⁻¹' minkN.JpastSet mx_scri) ∧
      KLs (minkN.cone O_N) = frontier (mx_witnessExt.ι ⁻¹' minkN.JpastSet mx_scri) ∧
      p₀ ∈ frontier (mx_witnessExt.ι ⁻¹' minkN.JpastSet mx_scri) ∧
      Tendsto (fun x => (dcov (Θ₀ ∘ φ) x (nN x))⁻¹ • covCh (Θ₀ ∘ φ) p₀ x) (𝓝[minkN.D JN] p₀)
        (𝓝 (-(minkN.gE p₀ ellV))) := by
  obtain ⟨hL, -, O_N, hOD, hmono, hJM, hHM, hΘ, hadapt⟩ := mh_witness_hypotheses goodG_log
  obtain ⟨_, -, -, -, -, -, -, -, -, -, -, -, hmem, hne⟩ := mx_witness_boundary
  -- `mx_witness_boundary`'s observer is existential: rebuild `hI` for this one through `hOD`.
  have hI' : minkN.IpastSet (range O_N) = mx_witnessExt.ι ⁻¹' minkN.IpastSet mx_scri := by
    rw [hOD]; exact mx_preimage_Ipast_scri.symm
  have hHM' : frontier (mx_witnessExt.ι ⁻¹' minkN.JpastSet mx_scri) ⊆ minkN.M := subset_univ _
  obtain ⟨h0, h1, h2, h3, h4, h5, h6⟩ := MSpacetime.mx_prop_causal_alignment hL hL mx_witnessExt
    (subset_univ _) hOD hmono hJM hI' hHM' hΘ hadapt
  have hp : p₀ ∈ frontier (mx_witnessExt.ι ⁻¹' minkN.JpastSet mx_scri) :=
    (hmem p₀).2 (by rw [φ_p₀])
  obtain ⟨-, -, hF, hr, -, -⟩ := mc_witness_tangency_holds p₀ (h0 ▸ hp)
  have ht := h6 p₀ hp ℓN nN (𝓝[minkN.D JN] p₀) ‖nvec‖ ellV nhdsWithin_le_nhds hF
    (Eventually.of_forall fun x => by rw [A_nN])
    (tendsto_const_nhds.congr fun x => (A_ℓN x).symm) hr
  exact ⟨O_N, hmem, hne, h0, h1, h2, h3, h4, h5, hp, ht⟩

end NModel

/-! ## NEW (campaign 90) (a): a genuine compactification, `Ñ = P ≠ Pt = N`

`Ñ` is the model space `P = ℝ × ℝ` itself, with Mathlib's one-chart self structure (`chartAt = refl`,
`extChartAt = PartialEquiv.refl`), a different type from the two-chart `Pt`. On it `cz_St` is flat,
`g̃ = −du dv` (campaign 81's `gM`, the same null-coordinate convention as `minkN` in `φ`), `T̃ = (1,1)`.
The embedding is `ι = cz_fB ∘ φ : Pt → P`, `cz_fB (U, V) = (arctan U, arctan V)`, so
`ι(Pt) = (−π/2, π/2)²`, whose closure `[−π/2, π/2]²` is compact. In `φ`,
`Dι = diag(1/(1+U²), 1/(1+V²))`, so `ι*g̃ = −dU dV / ((1+U²)(1+V²))` and
`Ω = ((1+U²)(1+V²))^{−1/2}`. `𝒥⁺ = {(u, π/2) : −π/2 < u < 0}`, `Ĩ⁻(𝒥⁺) = {u < 0, v < π/2}`, whose
preimage is `D = {U < 0}`. -/

namespace NModel
open Model Manifold ContinuousLinearMap

/-- **The compactified spacetime** `S̃` on `Ñ = P` (self-charted): `M̃ = P`, `g̃ = −du dv`,
`T̃ = (1, 1)`. -/
noncomputable def cz_St : MSpacetime P P where
  M := univ
  isOpen_M := isOpen_univ
  g := fun _ => gM
  symm := fun _ v w => mink.symm 0 v w
  T := fun _ => ((1, 1) : P)
  T_timelike := fun _ _ => mink.T_timelike 0 (mem_univ _)
  pos_on_perp := fun _ _ v h hv => mink.pos_on_perp 0 (mem_univ _) v h hv

/-- The self chart of `P` is the identity, and so is its derivative. -/
lemma cz_extChart_apply (p y : P) : extChartAt 𝓘(ℝ, P) p y = y := by
  rw [extChartAt_model_space_eq_id]; rfl

lemma cz_extChart_symm_apply (p y : P) : (extChartAt 𝓘(ℝ, P) p).symm y = y := by
  rw [extChartAt_model_space_eq_id]; rfl

lemma cz_mfderiv_chart (p y v : P) : mfderiv 𝓘(ℝ, P) 𝓘(ℝ, P) (extChartAt 𝓘(ℝ, P) p) y v = v := by
  rw [extChartAt_model_space_eq_id, PartialEquiv.refl_coe, mfderiv_id]; rfl

lemma cz_mfderiv_chart_symm (p y v : P) :
    mfderiv 𝓘(ℝ, P) 𝓘(ℝ, P) (extChartAt 𝓘(ℝ, P) p).symm y v = v := by
  rw [extChartAt_model_space_eq_id, PartialEquiv.refl_symm, PartialEquiv.refl_coe, mfderiv_id]; rfl

lemma cz_src (p y : P) : y ∈ (chartAt P p).source := by
  rw [chartAt_self_eq]; exact mem_univ _

lemma cz_hRep (p : P) : hRep cz_St.g p = fun _ => gM := by
  funext y
  refine ContinuousLinearMap.ext fun v => ContinuousLinearMap.ext fun w => ?_
  rw [ld_hRep_apply, cz_mfderiv_chart_symm, cz_mfderiv_chart_symm]; rfl

lemma cz_chartRep (p : P) : chartRep cz_St.T p = fun _ => ((1, 1) : P) := by
  funext y
  exact cz_mfderiv_chart p _ _

/-- **`S̃.LocallyOneChart` (BUILT):** with the self chart, `hRep g̃ p = gM` and
`chartRep T̃ p = (1, 1)` are constant on all of `P`. -/
theorem cz_locallyOneChart : cz_St.LocallyOneChart := by
  intro p _
  refine ⟨univ, isOpen_univ, mem_univ _, fun y _ => ⟨y, ⟨mem_univ _, cz_src p y⟩,
    cz_extChart_apply p y⟩, ?_, ?_⟩
  · rw [cz_hRep]; exact contDiffOn_const
  · rw [cz_chartRep]; exact continuousOn_const

/-- `S̃` is one-chart at `0`, for the causal transport to `mink`. -/
theorem cz_oneChart : cz_St.OneChart (0 : P) where
  sub := fun y _ => cz_src 0 y
  g_C1 := by rw [cz_hRep]; exact contDiffOn_const
  T_cont := by rw [cz_chartRep]; exact continuousOn_const

/-- **The chart spacetime of `S̃` is campaign 81's `mink`.** -/
theorem cz_chartSp_eq : MSpacetime.chartSp cz_oneChart = mink := by
  refine Spacetime.ch_ext ?_ (cz_hRep 0) (cz_chartRep 0)
  show extChartAt 𝓘(ℝ, P) (0 : P) '' univ = univ
  exact eq_univ_of_forall fun y => ⟨y, mem_univ _, cz_extChart_apply 0 y⟩

/-- `I⁻` in `S̃` is `I⁻` in `mink`. -/
lemma cz_mem_D (A : Set P) (x : P) : x ∈ cz_St.D A ↔ x ∈ mink.D A := by
  rw [MSpacetime.ch_mem_D_iff cz_oneChart (fun y _ => cz_src 0 y) (cz_src 0 x), cz_chartSp_eq,
    cz_extChart_apply]
  have e : extChartAt 𝓘(ℝ, P) (0 : P) '' A = A := by
    ext y; constructor
    · rintro ⟨z, hz, rfl⟩; rw [cz_extChart_apply]; exact hz
    · intro hy; exact ⟨y, hy, cz_extChart_apply 0 y⟩
  rw [e]

/-- `(U, V) ↦ (arctan U, arctan V)`. -/
noncomputable def cz_fB (y : P) : P := (Real.arctan y.1, Real.arctan y.2)

/-- `cz_DfB = diag(1/(1+U²), 1/(1+V²))`. -/
noncomputable def cz_DfB (y : P) : P →L[ℝ] P :=
  ((1 / (1 + y.1 ^ 2)) • fst ℝ ℝ ℝ).prod ((1 / (1 + y.2 ^ 2)) • snd ℝ ℝ ℝ)

lemma cz_DfB_apply (y v : P) :
    cz_DfB y v = ((1 / (1 + y.1 ^ 2)) * v.1, (1 / (1 + y.2 ^ 2)) * v.2) := by
  simp [cz_DfB]

lemma cz_fB_hasFDerivAt (y : P) : HasFDerivAt cz_fB (cz_DfB y) y :=
  ((Real.hasDerivAt_arctan y.1).comp_hasFDerivAt y hasFDerivAt_fst).prodMk
    ((Real.hasDerivAt_arctan y.2).comp_hasFDerivAt y hasFDerivAt_snd)

lemma cz_fB_contDiff : ContDiff ℝ 1 cz_fB :=
  (Real.contDiff_arctan.comp contDiff_fst).prodMk (Real.contDiff_arctan.comp contDiff_snd)

lemma cz_fB_eq : cz_fB = Prod.map Real.arctan Real.arctan := rfl

lemma cz_fB_isOpenEmbedding : IsOpenEmbedding cz_fB := by
  rw [cz_fB_eq]; exact mx_arctan_isOpenEmbedding.prodMap mx_arctan_isOpenEmbedding

/-- **The compactifying embedding** `ι = cz_fB ∘ φ : Pt → P`. -/
noncomputable def cz_ι : Pt → P := cz_fB ∘ φ

lemma cz_ι_apply (x : Pt) : cz_ι x = (Real.arctan (φ x).1, Real.arctan (φ x).2) := rfl

/-- **`ι` is an open embedding (BUILT).** -/
theorem cz_ι_isOpenEmbedding : IsOpenEmbedding cz_ι := by
  have e : cz_ι = cz_fB ∘ nullH := by rw [cz_ι, mx_φ_eq]
  rw [e]; exact cz_fB_isOpenEmbedding.comp nullH.isOpenEmbedding

/-- **`ι : Pt → P` is `C¹` across the two types (BUILT):** the target is the model space, so
`ι = cz_fB ∘ φ` with `cz_fB` `C¹` on `ℝ²` and `φ = extChartAt p₀` `C¹`. -/
theorem cz_ι_contMDiff : ContMDiff 𝓘(ℝ, P) 𝓘(ℝ, P) 1 cz_ι :=
  (contMDiff_iff_contDiff.2 cz_fB_contDiff).comp mx_φ_contMDiff

/-- **`Dι` read in `φ` (BUILT):** `Dι_x v = diag(1/(1+U²), 1/(1+V²)) (Dφ_x v)`, `(U, V) = φ x`
(on `Ñ = P` the chart is the identity). -/
theorem cz_dι_eq (x : Pt) (v : P) : mx_dι cz_ι x v = cz_DfB (φ x) (dchart p₀ x v) := by
  have hφ : MDifferentiableAt 𝓘(ℝ, P) 𝓘(ℝ, P) φ x := mdifferentiableAt_extChartAt (src x)
  have hf : MDifferentiableAt 𝓘(ℝ, P) 𝓘(ℝ, P) cz_fB (φ x) :=
    mdifferentiableAt_iff_differentiableAt.2 (cz_fB_hasFDerivAt _).differentiableAt
  have h1 : mx_dι cz_ι x = (mx_dι (E := P) cz_fB (φ x)).comp (mx_dι (E := P) φ x) := by
    show mfderiv 𝓘(ℝ, P) 𝓘(ℝ, P) (cz_fB ∘ φ) x = _
    rw [mfderiv_comp x hf hφ]; rfl
  have h2 : mx_dι (E := P) cz_fB (φ x) = cz_DfB (φ x) := by
    show mfderiv 𝓘(ℝ, P) 𝓘(ℝ, P) cz_fB (φ x) = _
    rw [mfderiv_eq_fderiv]; exact (cz_fB_hasFDerivAt _).fderiv
  rw [h1, ContinuousLinearMap.comp_apply, h2]; rfl

/-- `gM(DfB a, DfB b) = gM(a, b) / ((1+U²)(1+V²))`. -/
lemma cz_gM_DfB (y a b : P) :
    gM (cz_DfB y a) (cz_DfB y b) = (1 / ((1 + y.1 ^ 2) * (1 + y.2 ^ 2))) * gM a b := by
  have h1 : (1 + y.1 ^ 2) ≠ 0 := by positivity
  have h2 : (1 + y.2 ^ 2) ≠ 0 := by positivity
  rw [cz_DfB_apply, cz_DfB_apply, gM_apply, gM_apply]
  field_simp

/-- **The conformal factor** `Ω = ((1+U²)(1+V²))^{−1/2}`. -/
noncomputable def cz_Ω (x : Pt) : ℝ := (Real.sqrt ((1 + (φ x).1 ^ 2) * (1 + (φ x).2 ^ 2)))⁻¹

theorem cz_Ω_pos (x : Pt) : 0 < cz_Ω x := inv_pos.2 (Real.sqrt_pos.2 (by positivity))

theorem cz_Ω_sq (x : Pt) : cz_Ω x ^ 2 = 1 / ((1 + (φ x).1 ^ 2) * (1 + (φ x).2 ^ 2)) := by
  rw [cz_Ω, inv_pow, Real.sq_sqrt (by positivity), one_div]

/-- **The conformal extension `minkN → S̃` with `Ñ = P ≠ Pt` (BUILT): every field.** -/
noncomputable def cz_witnessExt : ConformalExtension minkN cz_St where
  ι := cz_ι
  isOpenEmbedding := cz_ι_isOpenEmbedding
  contMDiff := cz_ι_contMDiff
  Ω := cz_Ω
  Ω_pos := cz_Ω_pos
  conformal := fun x v w => by
    rw [mx_g_eq_gM, cz_dι_eq, cz_dι_eq, cz_Ω_sq]
    exact cz_gM_DfB _ _ _
  timeOrient := fun x _ => by
    show mink.FutTimelike (cz_ι x) (mx_dι cz_ι x (TN x))
    rw [cz_dι_eq, mx_dchart_T, futTimelike_iff, cz_DfB_apply]
    exact ⟨by simp only [mul_one]; positivity, by simp only [mul_one]; positivity⟩
  maps_M := subset_univ _

/-- **The conformal factor is not constant in either variable** (non-vacuity of `Ω`). -/
theorem cz_Ω_nonconst :
    cz_Ω (ψ (0, 0)) ^ 2 = 1 ∧ cz_Ω (ψ (1, 0)) ^ 2 = 1 / 2 ∧ cz_Ω (ψ (0, 1)) ^ 2 = 1 / 2 := by
  refine ⟨?_, ?_, ?_⟩ <;> rw [cz_Ω_sq] <;> simp only [φ, φψ] <;> norm_num

/-- The open box `(−π/2, π/2)²`. -/
lemma cz_range_ι :
    range cz_ι = Ioo (-(Real.pi / 2)) (Real.pi / 2) ×ˢ Ioo (-(Real.pi / 2)) (Real.pi / 2) := by
  have e : range cz_ι = range cz_fB := by
    ext y; constructor
    · rintro ⟨x, rfl⟩; exact ⟨φ x, rfl⟩
    · rintro ⟨z, rfl⟩; exact ⟨ψ z, by show cz_fB (φ (ψ z)) = _; rw [show φ (ψ z) = z from φψ z]⟩
  rw [e, cz_fB_eq, range_prodMap, Real.range_arctan]

/-- **Relative compactness (BUILT):** `closure ι(Pt) = [−π/2, π/2]²`. -/
theorem cz_closure_range :
    closure (range cz_ι) = Icc (-(Real.pi / 2)) (Real.pi / 2) ×ˢ Icc (-(Real.pi / 2)) (Real.pi / 2) := by
  have hne : -(Real.pi / 2) ≠ Real.pi / 2 := by linarith [Real.pi_pos]
  rw [cz_range_ι, closure_prod_eq, closure_Ioo hne]

theorem cz_isCompact_closure : IsCompact (closure (range cz_ι)) := by
  rw [cz_closure_range]; exact isCompact_Icc.prod isCompact_Icc

theorem cz_range_ne_univ : range cz_ι ≠ univ := by
  intro h
  have hm : ((Real.pi / 2, 0) : P) ∈ range cz_ι := h ▸ mem_univ _
  rw [cz_range_ι] at hm
  exact lt_irrefl _ hm.1.2

/-- `𝒥⁺ = {(u, π/2) : −π/2 < u < 0}`, a segment of the null boundary of the box. -/
def cz_scri : Set P := {p : P | -(Real.pi / 2) < p.1 ∧ p.1 < 0 ∧ p.2 = Real.pi / 2}

theorem cz_scri_subset_frontier : cz_scri ⊆ frontier (range cz_ι) := by
  rintro p ⟨h1, h2, h3⟩
  have hpi := Real.pi_pos
  rw [frontier, cz_ι_isOpenEmbedding.isOpen_range.interior_eq, cz_closure_range]
  refine ⟨⟨⟨h1.le, by linarith⟩, ⟨by linarith, h3.le⟩⟩, fun hm => ?_⟩
  rw [cz_range_ι] at hm
  exact lt_irrefl _ (h3 ▸ hm.2.2)

theorem cz_scri_nonempty : cz_scri.Nonempty :=
  ⟨(-1, Real.pi / 2), ⟨show -(Real.pi / 2) < -1 by linarith [Real.pi_gt_three],
    show (-1 : ℝ) < 0 by norm_num, rfl⟩⟩

/-- **`Ĩ⁻(𝒥⁺)` in `mink` (BUILT):** `{u < 0, v < π/2}`. -/
lemma cz_mem_mink_D (p : P) : p ∈ mink.D cz_scri ↔ p.1 < 0 ∧ p.2 < Real.pi / 2 := by
  show p ∈ ⋃ a ∈ cz_scri, mink.Ipast a ↔ _
  rw [mem_iUnion₂]
  constructor
  · rintro ⟨a, ⟨-, ha1, ha2⟩, hpa⟩
    have h := chr_lt hpa
    exact ⟨h.1.trans ha1, ha2 ▸ h.2⟩
  · rintro ⟨h1, h2⟩
    have hpi := Real.pi_gt_three
    refine ⟨(max (p.1 / 2) (-(1 / 2)), Real.pi / 2), ⟨?_, ?_, rfl⟩,
      Relation.TransGen.single (tstep_of_lt ?_ h2)⟩
    · show -(Real.pi / 2) < max (p.1 / 2) (-(1 / 2))
      exact lt_of_lt_of_le (by linarith) (le_max_right _ _)
    · show max (p.1 / 2) (-(1 / 2)) < 0
      exact max_lt (by linarith) (by norm_num)
    · show p.1 < max (p.1 / 2) (-(1 / 2))
      exact lt_of_lt_of_le (by linarith) (le_max_left _ _)

/-- **`Ĩ⁻(𝒥⁺)` in `S̃` (BUILT):** `{u < 0, v < π/2}`. -/
theorem cz_mem_Ipast_scri (p : P) :
    p ∈ cz_St.IpastSet cz_scri ↔ p.1 < 0 ∧ p.2 < Real.pi / 2 :=
  (cz_mem_D cz_scri p).trans (cz_mem_mink_D p)

lemma cz_arctan_neg_iff (a : ℝ) : Real.arctan a < 0 ↔ a < 0 := by
  constructor
  · intro h; by_contra hc
    have := Real.arctan_strictMono.monotone (not_lt.1 hc)
    rw [Real.arctan_zero] at this; linarith
  · intro h; have := Real.arctan_strictMono h; rwa [Real.arctan_zero] at this

/-- **`hI` (BUILT):** `ι⁻¹ Ĩ⁻(𝒥⁺) = {U < 0} = D`. -/
theorem cz_preimage_Ipast_scri : cz_ι ⁻¹' cz_St.IpastSet cz_scri = minkN.D JN := by
  ext x
  rw [mem_preimage, cz_mem_Ipast_scri, cz_ι_apply, mem_D_JN_iff]
  exact ⟨fun h => (cz_arctan_neg_iff _).1 h.1,
    fun h => ⟨(cz_arctan_neg_iff _).2 h, Real.arctan_lt_pi_div_two _⟩⟩

/-- **(a) The witness with `Ñ = P ≠ Pt` (BUILT).** `ι = (arctan × arctan) ∘ φ` is a conformal
extension of `minkN` into the self-charted flat `S̃` on `P`, `Ω² = 1/((1+U²)(1+V²))`, the image
is relatively compact (`closure = [−π/2, π/2]²`, not all of `P`), `𝒥⁺ ⊆ ∂ι(Pt)`, `𝒥⁺ ⊆ M̃`,
`Ĩ⁻(𝒥⁺) = {u < 0, v < π/2}`, `hI`, and by `mx_H_eq_boundary`: `𝓗⁺ = ∂J⁻(𝒥⁺) = {U = 0} ≠ ∅`. -/
theorem cz_witness_boundary :
    ∃ O_N : ℝ → Pt, minkN.IpastSet (range O_N) = minkN.D JN ∧
      (∀ s t : ℝ, s < t → minkN.Chr (O_N s) (O_N t)) ∧
      cz_witnessExt.ι = cz_fB ∘ φ ∧
      (∀ x, cz_witnessExt.Ω x ^ 2 = 1 / ((1 + (φ x).1 ^ 2) * (1 + (φ x).2 ^ 2))) ∧
      closure (range cz_witnessExt.ι) =
        Icc (-(Real.pi / 2)) (Real.pi / 2) ×ˢ Icc (-(Real.pi / 2)) (Real.pi / 2) ∧
      IsCompact (closure (range cz_witnessExt.ι)) ∧ range cz_witnessExt.ι ≠ univ ∧
      cz_scri ⊆ frontier (range cz_witnessExt.ι) ∧ cz_scri ⊆ cz_St.M ∧ cz_scri.Nonempty ∧
      (∀ p, p ∈ cz_St.IpastSet cz_scri ↔ p.1 < 0 ∧ p.2 < Real.pi / 2) ∧
      minkN.IpastSet (range O_N) = cz_witnessExt.ι ⁻¹' cz_St.IpastSet cz_scri ∧
      minkN.H (range O_N) = frontier (cz_witnessExt.ι ⁻¹' cz_St.JpastSet cz_scri) ∧
      minkN.H JN = frontier (cz_witnessExt.ι ⁻¹' cz_St.JpastSet cz_scri) ∧
      (∀ x, x ∈ frontier (cz_witnessExt.ι ⁻¹' cz_St.JpastSet cz_scri) ↔ (φ x).1 = 0) ∧
      (frontier (cz_witnessExt.ι ⁻¹' cz_St.JpastSet cz_scri)).Nonempty := by
  obtain ⟨O_N, hOD, hmono, hJM, -, -, -⟩ := ch_witness_hypotheses goodG_log
  have hI : minkN.IpastSet (range O_N) = cz_witnessExt.ι ⁻¹' cz_St.IpastSet cz_scri := by
    rw [hOD]; exact cz_preimage_Ipast_scri.symm
  have hB := MSpacetime.mx_H_eq_boundary me_locallyOneChart cz_locallyOneChart cz_witnessExt
    (subset_univ _) hOD hmono hJM hI
  have hmem : ∀ x, x ∈ frontier (cz_witnessExt.ι ⁻¹' cz_St.JpastSet cz_scri) ↔ (φ x).1 = 0 :=
    fun x => by rw [← hB.2]; exact mem_H_N x
  refine ⟨O_N, hOD, hmono, rfl, cz_Ω_sq, cz_closure_range, cz_isCompact_closure, cz_range_ne_univ,
    cz_scri_subset_frontier, subset_univ _, cz_scri_nonempty, cz_mem_Ipast_scri, hI, hB.1, hB.2,
    hmem, ⟨ψ (0, 0), (hmem _).2 (by rw [show φ (ψ (0, 0)) = (0, 0) from φψ _])⟩⟩

/-- **(a) The headline end to end with `Ñ = P ≠ Pt` (BUILT), for `Θ₀ ∘ φ`.** Every hypothesis of
`mx_prop_causal_alignment` is discharged for `cz_witnessExt : ConformalExtension minkN cz_St`
(`hLt = cz_locallyOneChart` on the self-charted `P`), and its conclusion read off as in
`mx_witness_headline`, with the tangency clause at `p₀`. -/
theorem cz_witness_headline :
    ∃ O_N : ℝ → Pt,
      IsCompact (closure (range cz_witnessExt.ι)) ∧ range cz_witnessExt.ι ≠ univ ∧
      (∀ x, x ∈ frontier (cz_witnessExt.ι ⁻¹' cz_St.JpastSet cz_scri) ↔ (φ x).1 = 0) ∧
      (frontier (cz_witnessExt.ι ⁻¹' cz_St.JpastSet cz_scri)).Nonempty ∧
      minkN.H JN = frontier (cz_witnessExt.ι ⁻¹' cz_St.JpastSet cz_scri) ∧
      minkN.SublevelProper JN (Θ₀ ∘ φ) ∧
      KLi (minkN.slice JN (Θ₀ ∘ φ)) = frontier (cz_witnessExt.ι ⁻¹' cz_St.JpastSet cz_scri) ∧
      KLs (minkN.slice JN (Θ₀ ∘ φ)) = frontier (cz_witnessExt.ι ⁻¹' cz_St.JpastSet cz_scri) ∧
      KLi (minkN.cone O_N) = frontier (cz_witnessExt.ι ⁻¹' cz_St.JpastSet cz_scri) ∧
      KLs (minkN.cone O_N) = frontier (cz_witnessExt.ι ⁻¹' cz_St.JpastSet cz_scri) ∧
      p₀ ∈ frontier (cz_witnessExt.ι ⁻¹' cz_St.JpastSet cz_scri) ∧
      Tendsto (fun x => (dcov (Θ₀ ∘ φ) x (nN x))⁻¹ • covCh (Θ₀ ∘ φ) p₀ x) (𝓝[minkN.D JN] p₀)
        (𝓝 (-(minkN.gE p₀ ellV))) := by
  obtain ⟨hL, -, O_N, hOD, hmono, hJM, -, hΘ, hadapt⟩ := mh_witness_hypotheses goodG_log
  obtain ⟨_, -, -, -, -, -, -, -, -, -, -, -, -, -, -, hmem, hne⟩ := cz_witness_boundary
  have hI' : minkN.IpastSet (range O_N) = cz_witnessExt.ι ⁻¹' cz_St.IpastSet cz_scri := by
    rw [hOD]; exact cz_preimage_Ipast_scri.symm
  have hHM' : frontier (cz_witnessExt.ι ⁻¹' cz_St.JpastSet cz_scri) ⊆ minkN.M := subset_univ _
  obtain ⟨h0, h1, h2, h3, h4, h5, h6⟩ := MSpacetime.mx_prop_causal_alignment hL cz_locallyOneChart
    cz_witnessExt (subset_univ _) hOD hmono hJM hI' hHM' hΘ hadapt
  have hp : p₀ ∈ frontier (cz_witnessExt.ι ⁻¹' cz_St.JpastSet cz_scri) :=
    (hmem p₀).2 (by rw [φ_p₀])
  obtain ⟨-, -, hF, hr, -, -⟩ := mc_witness_tangency_holds p₀ (h0 ▸ hp)
  have ht := h6 p₀ hp ℓN nN (𝓝[minkN.D JN] p₀) ‖nvec‖ ellV nhdsWithin_le_nhds hF
    (Eventually.of_forall fun x => by rw [A_nN])
    (tendsto_const_nhds.congr fun x => (A_ℓN x).symm) hr
  exact ⟨O_N, cz_isCompact_closure, cz_range_ne_univ, hmem, hne, h0, h1, h2, h3, h4, h5, hp, ht⟩

end NModel

/-! ## NEW (campaign 90) (a) stretch: a curved `N`, `g_F = −F dU dV`

`cz_scale S F` multiplies the metric by a positive function `F` and keeps `M` and `T`. Future
timelike and future causal vectors are unchanged, so every causal object (`TStep`, `CStep`, `≪`, `≤`,
`I⁻`, `J⁻`, `D`, `𝓗⁺`, slices, properness, past cones, temporality, the Cauchy property) is unchanged
(`cz_scale_*`); `LocallyOneChart` passes to `cz_scale S F` when `F` is `C¹` in every preferred chart.
On `Pt`, `F = F̂ ∘ φ` for any positive `C¹` `F̂ : P → ℝ` (in null coordinates), and the same `ι`
is a conformal extension into the flat `S̃` with `Ω² = 1/(F (1+U²)(1+V²))`. -/

section Scale
open Manifold
set_option linter.unusedSectionVars false

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
variable {N : Type*} [TopologicalSpace N] [ChartedSpace E N] [IsManifold 𝓘(ℝ, E) 1 N]

namespace MSpacetime

lemma cz_mul_neg_iff {c a : ℝ} (hc : 0 < c) : c * a < 0 ↔ a < 0 :=
  ⟨fun h => by by_contra h'; exact absurd h (not_lt.2 (mul_nonneg hc.le (not_lt.1 h'))),
    fun h => mul_neg_of_pos_of_neg hc h⟩

lemma cz_mul_nonpos_iff {c a : ℝ} (hc : 0 < c) : c * a ≤ 0 ↔ a ≤ 0 :=
  ⟨fun h => by by_contra h'; exact absurd h (not_le.2 (mul_pos hc (not_le.1 h'))),
    fun h => by nlinarith⟩

/-- **The conformally rescaled spacetime** `(M, F g, T)`, `F > 0`. -/
noncomputable def cz_scale (S : MSpacetime E N) (F : N → ℝ) (hF : ∀ x, 0 < F x) :
    MSpacetime E N where
  M := S.M
  isOpen_M := S.isOpen_M
  g := fun x => F x • S.g x
  symm := fun x v w => by
    show F x * S.g x v w = F x * S.g x w v
    rw [S.symm]
  T := S.T
  T_timelike := fun x hx => by
    show F x * S.g x (S.T x) (S.T x) < 0
    exact mul_neg_of_pos_of_neg (hF x) (S.T_timelike x hx)
  pos_on_perp := fun x hx v h hv => by
    change F x * S.g x v (S.T x) = 0 at h
    show 0 < F x * S.g x v v
    exact mul_pos (hF x) (S.pos_on_perp x hx v
      ((mul_eq_zero.1 h).resolve_left (hF x).ne') hv)

variable (S : MSpacetime E N) {F : N → ℝ} (hF : ∀ x, 0 < F x)

lemma cz_scale_gE (x : N) (v w : E) : (S.cz_scale F hF).gE x v w = F x * S.gE x v w := rfl

lemma cz_scale_futTimelike : (S.cz_scale F hF).FutTimelike = S.FutTimelike := by
  funext x v
  show (F x * S.gE x v v < 0 ∧ F x * S.gE x v (S.T x) < 0) = S.FutTimelike x v
  rw [cz_mul_neg_iff (hF x), cz_mul_neg_iff (hF x)]; rfl

lemma cz_scale_futCausal : (S.cz_scale F hF).FutCausal = S.FutCausal := by
  funext x v
  show (F x * S.gE x v v ≤ 0 ∧ F x * S.gE x v (S.T x) < 0) = S.FutCausal x v
  rw [cz_mul_nonpos_iff (hF x), cz_mul_neg_iff (hF x)]; rfl

lemma cz_scale_tstep : (S.cz_scale F hF).TStep = S.TStep := by
  funext x y
  show (∃ γ : ℝ → N, ContMDiff 𝓘(ℝ, ℝ) 𝓘(ℝ, E) 1 γ ∧ γ 0 = x ∧ γ 1 = y ∧
    ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ S.M ∧ (S.cz_scale F hF).FutTimelike (γ t) (vel γ t)) = _
  rw [cz_scale_futTimelike]; rfl

lemma cz_scale_cstep : (S.cz_scale F hF).CStep = S.CStep := by
  funext x y
  show (∃ γ : ℝ → N, ContMDiff 𝓘(ℝ, ℝ) 𝓘(ℝ, E) 1 γ ∧ γ 0 = x ∧ γ 1 = y ∧
    ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ S.M ∧ (S.cz_scale F hF).FutCausal (γ t) (vel γ t)) = _
  rw [cz_scale_futCausal]; rfl

lemma cz_scale_chr : (S.cz_scale F hF).Chr = S.Chr := by
  show Relation.TransGen (S.cz_scale F hF).TStep = Relation.TransGen S.TStep
  rw [cz_scale_tstep]

lemma cz_scale_cau : (S.cz_scale F hF).Cau = S.Cau := by
  show Relation.ReflTransGen (S.cz_scale F hF).CStep = Relation.ReflTransGen S.CStep
  rw [cz_scale_cstep]

lemma cz_scale_Ipast : (S.cz_scale F hF).Ipast = S.Ipast := by
  funext p; show {q | (S.cz_scale F hF).Chr q p} = {q | S.Chr q p}; rw [cz_scale_chr]

lemma cz_scale_Jpast : (S.cz_scale F hF).Jpast = S.Jpast := by
  funext p; show {q | (S.cz_scale F hF).Cau q p} = {q | S.Cau q p}; rw [cz_scale_cau]

lemma cz_scale_IpastSet : (S.cz_scale F hF).IpastSet = S.IpastSet := by
  funext A; show (⋃ p ∈ A, (S.cz_scale F hF).Ipast p) = ⋃ p ∈ A, S.Ipast p; rw [cz_scale_Ipast]

lemma cz_scale_JpastSet : (S.cz_scale F hF).JpastSet = S.JpastSet := by
  funext A; show (⋃ p ∈ A, (S.cz_scale F hF).Jpast p) = ⋃ p ∈ A, S.Jpast p; rw [cz_scale_Jpast]

lemma cz_scale_D : (S.cz_scale F hF).D = S.D := cz_scale_IpastSet S hF

lemma cz_scale_H : (S.cz_scale F hF).H = S.H := by
  funext J; show frontier ((S.cz_scale F hF).JpastSet J) = frontier (S.JpastSet J)
  rw [cz_scale_JpastSet]

lemma cz_scale_slice : (S.cz_scale F hF).slice = S.slice := by
  funext J Θ τ; show {x | x ∈ (S.cz_scale F hF).D J ∧ Θ x = τ} = {x | x ∈ S.D J ∧ Θ x = τ}
  rw [cz_scale_D]

lemma cz_scale_cone : (S.cz_scale F hF).cone = S.cone := by
  funext O τ; show frontier ((S.cz_scale F hF).Jpast (O τ)) = frontier (S.Jpast (O τ))
  rw [cz_scale_Jpast]

lemma cz_scale_sublevelProper : (S.cz_scale F hF).SublevelProper = S.SublevelProper := by
  funext J Θ
  show (∀ T : ℝ, closure {x | x ∈ (S.cz_scale F hF).D J ∧ Θ x ≤ T} ⊆ (S.cz_scale F hF).D J) = _
  rw [cz_scale_D]; rfl

/-- **The Cauchy property is conformally invariant.** -/
theorem cz_scale_isCauchyTemporalOn {U : Set N} {τ : N → ℝ} (h : S.IsCauchyTemporalOn U τ) :
    (S.cz_scale F hF).IsCauchyTemporalOn U τ := by
  obtain ⟨⟨h1, h2⟩, h3⟩ := h
  refine ⟨⟨h1, fun x hx v hv => h2 x hx v (by rwa [cz_scale_futCausal] at hv)⟩, fun c a => ?_⟩
  exact h3 ⟨c.γ, c.cont, c.mem, c.brk, c.brk_fin,
    fun t ht => ⟨(c.causal t ht).1, by rw [← cz_scale_futCausal S hF]; exact (c.causal t ht).2⟩,
    c.inext_future, c.inext_past⟩ a

lemma cz_hRep_scale (p : N) (y : E) :
    hRep (S.cz_scale F hF).g p y = F ((extChartAt 𝓘(ℝ, E) p).symm y) • hRep S.g p y :=
  ContinuousLinearMap.ext fun _ => ContinuousLinearMap.ext fun _ => rfl

/-- **`LocallyOneChart` passes to `F g`** when `F` is `C¹` in each preferred chart. -/
theorem cz_scale_locallyOneChart (hL : S.LocallyOneChart)
    (hFc : ∀ p ∈ S.M, ContDiffOn ℝ 1 (fun y => F ((extChartAt 𝓘(ℝ, E) p).symm y))
      (extChartAt 𝓘(ℝ, E) p).target) :
    (S.cz_scale F hF).LocallyOneChart := by
  intro p hp
  obtain ⟨U, hU, hpU, hUsub, hg, hT⟩ := hL p hp
  have hUt : U ⊆ (extChartAt 𝓘(ℝ, E) p).target := by
    intro y hy
    obtain ⟨x, ⟨-, hx⟩, rfl⟩ := hUsub hy
    exact ch_mem_target p hx
  refine ⟨U, hU, hpU, hUsub, ?_, hT⟩
  rw [show hRep (S.cz_scale F hF).g p = fun y => F ((extChartAt 𝓘(ℝ, E) p).symm y) • hRep S.g p y
    from funext (cz_hRep_scale S hF p)]
  have : IsBoundedSMul ℝ (E →L[ℝ] E →L[ℝ] ℝ) :=
    @NormedSpace.toIsBoundedSMul ℝ (E →L[ℝ] E →L[ℝ] ℝ) _ _ _
  exact ((hFc p hp).mono hUt).smul hg

end MSpacetime

end Scale

namespace NModel
open Model Manifold ContinuousLinearMap

variable {Fh : P → ℝ}

/-- `φ ∘ (extChartAt p)⁻¹` is `C¹` on the target, for every `p : Pt`. -/
lemma cz_φ_symm_contDiff (p : Pt) :
    ContDiff ℝ 1 (fun y => φ ((extChartAt 𝓘(ℝ, P) p).symm y)) := by
  by_cases hp : tco p < 0
  · have e : ∀ y, (extChartAt 𝓘(ℝ, P) p).symm y = idH.symm y := fun y => by
      have h := ch_left_inv p (src_neg hp (idH.symm y))
      rwa [chart_apply_neg hp, idH.apply_symm_apply] at h
    have e2 : (fun y => φ ((extChartAt 𝓘(ℝ, P) p).symm y)) = fun y : P => nullH (idH.symm y) := by
      funext y; rw [e, mx_φ_eq]
    rw [e2]; exact cd_null_id
  · have e2 : (fun y => φ ((extChartAt 𝓘(ℝ, P) p).symm y)) = id := by
      funext y; rw [extChartAt_nonneg hp]; exact φψ y
    rw [e2]; exact contDiff_id

/-- **The curved `N`:** `minkN` with `g_F = F g`, `F = F̂ ∘ φ`, i.e. `−F̂(U, V) dU dV`. -/
noncomputable def cz_minkF (hpos : ∀ y, 0 < Fh y) : MSpacetime P Pt :=
  minkN.cz_scale (Fh ∘ φ) (fun x => hpos (φ x))

variable (hFc : ContDiff ℝ 1 Fh) (hpos : ∀ y, 0 < Fh y)

include hFc in
theorem cz_minkF_locallyOneChart : (cz_minkF hpos).LocallyOneChart :=
  minkN.cz_scale_locallyOneChart _ me_locallyOneChart fun p _ =>
    (hFc.comp (cz_φ_symm_contDiff p)).contDiffOn

/-- The conformal factor for the curved `N`: `Ω_F = (F (1+U²)(1+V²))^{−1/2}`. -/
noncomputable def cz_ΩF (x : Pt) : ℝ :=
  (Real.sqrt (Fh (φ x) * ((1 + (φ x).1 ^ 2) * (1 + (φ x).2 ^ 2))))⁻¹

include hpos in
lemma cz_ΩF_pos (x : Pt) : 0 < cz_ΩF (Fh := Fh) x :=
  inv_pos.2 (Real.sqrt_pos.2 (mul_pos (hpos _) (by positivity)))

include hpos in
lemma cz_ΩF_sq (x : Pt) :
    cz_ΩF (Fh := Fh) x ^ 2 = 1 / (Fh (φ x) * ((1 + (φ x).1 ^ 2) * (1 + (φ x).2 ^ 2))) := by
  rw [cz_ΩF, inv_pow, Real.sq_sqrt (mul_pos (hpos _) (by positivity)).le, one_div]

/-- **The conformal extension of the curved `N` into the flat compact `S̃` (BUILT).** -/
noncomputable def cz_witnessExtF : ConformalExtension (cz_minkF hpos) cz_St where
  ι := cz_ι
  isOpenEmbedding := cz_ι_isOpenEmbedding
  contMDiff := cz_ι_contMDiff
  Ω := cz_ΩF (Fh := Fh)
  Ω_pos := cz_ΩF_pos hpos
  conformal := fun x v w => by
    rw [cz_minkF, MSpacetime.cz_scale_gE, cz_ΩF_sq hpos]
    have h := cz_witnessExt.conformal x v w
    change cz_St.gE (cz_ι x) (mx_dι cz_ι x v) (mx_dι cz_ι x w) = cz_Ω x ^ 2 * minkN.gE x v w at h
    rw [h, cz_Ω_sq]
    have h0 : Fh (φ x) ≠ 0 := (hpos _).ne'
    have h1 : (1 + (φ x).1 ^ 2) ≠ 0 := by positivity
    have h2 : (1 + (φ x).2 ^ 2) ≠ 0 := by positivity
    simp only [Function.comp_apply]
    field_simp
  timeOrient := fun x hx => cz_witnessExt.timeOrient x hx
  maps_M := subset_univ _

include hFc in
/-- **(a) stretch: the headline end to end on the curved `N` (BUILT, tangency clause left in
its general form).** For every positive `C¹` `F̂`, with `g_F = −F̂ dU dV` on `Pt`, `S̃` flat on `P`,
`ι = (arctan × arctan) ∘ φ` and `𝒥⁺ = cz_scri`, every hypothesis of `mx_prop_causal_alignment`
is discharged (the causal ones by conformal invariance, `LocallyOneChart` by
`cz_scale_locallyOneChart`), and its conclusion holds: `𝓗⁺_F = ∂J⁻(𝒥⁺) = {U = 0} ≠ ∅`,
properness, `KLi = KLs = ∂J⁻(𝒥⁺)` for slices and for past cones, and the tangency clause. -/
theorem cz_witness_headline_F :
    ∃ O_N : ℝ → Pt,
      (∀ x, (cz_witnessExtF hpos).Ω x ^ 2 =
        1 / (Fh (φ x) * ((1 + (φ x).1 ^ 2) * (1 + (φ x).2 ^ 2)))) ∧
      (∀ x, x ∈ frontier ((cz_witnessExtF hpos).ι ⁻¹' cz_St.JpastSet cz_scri) ↔ (φ x).1 = 0) ∧
      (frontier ((cz_witnessExtF hpos).ι ⁻¹' cz_St.JpastSet cz_scri)).Nonempty ∧
      (cz_minkF hpos).H JN = frontier ((cz_witnessExtF hpos).ι ⁻¹' cz_St.JpastSet cz_scri) ∧
      (cz_minkF hpos).SublevelProper JN (Θ₀ ∘ φ) ∧
      KLi ((cz_minkF hpos).slice JN (Θ₀ ∘ φ)) =
        frontier ((cz_witnessExtF hpos).ι ⁻¹' cz_St.JpastSet cz_scri) ∧
      KLs ((cz_minkF hpos).slice JN (Θ₀ ∘ φ)) =
        frontier ((cz_witnessExtF hpos).ι ⁻¹' cz_St.JpastSet cz_scri) ∧
      KLi ((cz_minkF hpos).cone O_N) =
        frontier ((cz_witnessExtF hpos).ι ⁻¹' cz_St.JpastSet cz_scri) ∧
      KLs ((cz_minkF hpos).cone O_N) =
        frontier ((cz_witnessExtF hpos).ι ⁻¹' cz_St.JpastSet cz_scri) ∧
      ∀ q ∈ frontier ((cz_witnessExtF hpos).ι ⁻¹' cz_St.JpastSet cz_scri),
        ∀ (ℓ n : Pt → P) (L : Filter Pt) (C : ℝ) (ℓ₀ : P), L ≤ 𝓝 q →
        (∀ᶠ x in L, TCF.FrameHyp ((cz_minkF hpos).gE x) (ℓ x) (n x) (dcov (Θ₀ ∘ φ) x)) →
        (∀ᶠ x in L, ‖dchartL q x (n x)‖ ≤ C) →
        Tendsto (fun x => dchartL q x (ℓ x)) L (𝓝 ℓ₀) →
        Tendsto (fun x => dcov (Θ₀ ∘ φ) x (ℓ x) / dcov (Θ₀ ∘ φ) x (n x)) L (𝓝 0) →
        Tendsto (fun x => (dcov (Θ₀ ∘ φ) x (n x))⁻¹ • covCh (Θ₀ ∘ φ) q x) L
          (𝓝 (-((cz_minkF hpos).gE q ℓ₀))) := by
  obtain ⟨-, -, O_N, hOD, hmono, hJM, -, hΘ, hadapt⟩ := mh_witness_hypotheses goodG_log
  obtain ⟨_, -, -, -, -, -, -, -, -, -, -, -, -, -, -, hmem, hne⟩ := cz_witness_boundary
  have eI : (cz_minkF hpos).IpastSet = minkN.IpastSet := minkN.cz_scale_IpastSet _
  have eD : (cz_minkF hpos).D = minkN.D := minkN.cz_scale_D _
  have eC : (cz_minkF hpos).Chr = minkN.Chr := minkN.cz_scale_chr _
  have hOD' : (cz_minkF hpos).IpastSet (range O_N) = (cz_minkF hpos).D JN := by
    rw [eI, eD]; exact hOD
  have hmono' : ∀ s t : ℝ, s < t → (cz_minkF hpos).Chr (O_N s) (O_N t) := by
    rw [eC]; exact hmono
  have hI' : (cz_minkF hpos).IpastSet (range O_N) =
      (cz_witnessExtF hpos).ι ⁻¹' cz_St.IpastSet cz_scri := by
    rw [eI, hOD]; exact cz_preimage_Ipast_scri.symm
  have hΘ' : (cz_minkF hpos).IsCauchyTemporalOn ((cz_minkF hpos).D JN) (Θ₀ ∘ φ) := by
    rw [eD]; exact minkN.cz_scale_isCauchyTemporalOn _ hΘ
  obtain ⟨h0, h1, h2, h3, h4, h5, h6⟩ := MSpacetime.mx_prop_causal_alignment
    (cz_minkF_locallyOneChart hFc hpos) cz_locallyOneChart (cz_witnessExtF hpos) (subset_univ _)
    hOD' hmono' hJM hI' (subset_univ _) hΘ' hadapt
  exact ⟨O_N, cz_ΩF_sq hpos, hmem, hne, h0, h1, h2, h3, h4, h5, h6⟩

/-- **Non-vacuity of the curved stretch:** `F̂ = e^{UV}` (a function of `UV`, as Kruskal's is) is
positive and `C¹`, and `g_F ≠ g` (at `φ⁻¹(1, 1)`). -/
theorem cz_exp_nonvacuous :
    ContDiff ℝ 1 (fun y : P => Real.exp (y.1 * y.2)) ∧ (∀ y : P, 0 < Real.exp (y.1 * y.2)) ∧
    (cz_minkF (Fh := fun y : P => Real.exp (y.1 * y.2)) (fun _ => Real.exp_pos _)).gE (ψ (1, 1)) ≠
      minkN.gE (ψ (1, 1)) := by
  refine ⟨Real.contDiff_exp.comp (contDiff_fst.mul contDiff_snd), fun _ => Real.exp_pos _,
    fun h => ?_⟩
  have h1 := congrArg (fun B : P →L[ℝ] P →L[ℝ] ℝ => B (TN (ψ (1, 1))) (TN (ψ (1, 1)))) h
  have hT := minkN.T_timelike (ψ (1, 1)) (mem_univ _)
  change (Real.exp ((φ (ψ (1, 1))).1 * (φ (ψ (1, 1))).2)) * minkN.gE _ _ _ = minkN.gE _ _ _ at h1
  rw [show φ (ψ (1, 1)) = (1, 1) from φψ _] at h1
  have he := Real.add_one_lt_exp (show (1 : ℝ) * 1 ≠ 0 by norm_num)
  change minkN.gE (ψ (1, 1)) (TN (ψ (1, 1))) (TN (ψ (1, 1))) < 0 at hT
  nlinarith

end NModel

/-! ## Campaign 91 ③ (`r7663+71`): the tangency clause instantiated on the curved `N`

On `cz_minkF hpos` (`g_F = −F̂(U, V) dU dV`) the frame is `ℓ = ℓN = ∂_V` (unchanged) and
`n = ct_nN = F̂(φ x)⁻¹ • nN` (`= (2/F̂) ∂_U`), so `g_F(ℓ, n) = −1`. Every new name has the prefix
`ct_`. -/

namespace NModel
open Model Manifold ContinuousLinearMap

variable {Fh : P → ℝ}

/-- **The null frame for `c • gM`, `c > 0`:** `ℓ = ∂_V`, `n = c⁻¹ (2, 0)`. -/
theorem ct_frameHyp_scaled {c : ℝ} (hc : 0 < c) {ξ : P →L[ℝ] ℝ} (h1 : 0 < ξ (1, 0))
    (h2 : 0 < ξ (0, 1)) : TCF.FrameHyp (c • gM) ellV (c⁻¹ • nvec) ξ := by
  have hg : ∀ v w : P, (c • gM) v w = c * (-(v.1 * w.2 + v.2 * w.1) / 2) := fun v w => by
    rw [smul_apply, smul_apply, gM_apply, smul_eq_mul]
  have hcc : c * c⁻¹ = 1 := mul_inv_cancel₀ hc.ne'
  refine ⟨⟨fun v w => ?_, ?_, ?_, ?_, fun e he1 he2 => ?_⟩, fun v hv => ?_⟩
  · simp only [TCF.bil_apply, hg]; ring
  · simp only [TCF.bil_apply, hg, ellV]; norm_num
  · simp only [TCF.bil_apply, hg, nvec, Prod.smul_fst, Prod.smul_snd, smul_eq_mul]; ring
  · simp only [TCF.bil_apply, hg, ellV, nvec, Prod.smul_fst, Prod.smul_snd, smul_eq_mul]
    linear_combination (-1 : ℝ) * hcc
  · simp only [TCF.bil_apply, hg, ellV, nvec, Prod.smul_fst, Prod.smul_snd, smul_eq_mul]
      at he1 he2 ⊢
    have h1' : c * e.1 = 0 := by linear_combination (-2 : ℝ) * he1
    have he1' : e.1 = 0 := (mul_eq_zero.1 h1').resolve_left hc.ne'
    have he2' : e.2 = 0 := by linear_combination (-1 : ℝ) * he2 - e.2 * hcc
    rw [he1', he2']; norm_num
  · obtain ⟨hv1, hv2⟩ := hv
    have k1 : (c • gM) v v = -(c * (v.1 * v.2)) := by rw [hg]; ring
    have k2 : (c • gM) v (ellV + c⁻¹ • nvec) = -(c * v.1 + 2 * v.2) / 2 := by
      rw [hg]
      simp only [ellV, nvec, Prod.fst_add, Prod.snd_add, Prod.smul_fst, Prod.smul_snd, smul_eq_mul]
      linear_combination (-(v.2 : ℝ)) * hcc
    rw [TCF.bil_apply, k1] at hv1
    rw [TCF.bil_apply, k2] at hv2
    have hs : 0 < c * v.1 + 2 * v.2 := by linarith
    have hp : 0 ≤ v.1 * v.2 := by
      have : 0 ≤ c * (v.1 * v.2) := by linarith
      exact (mul_nonneg_iff_of_pos_left hc).1 this
    have hv1' : 0 ≤ v.1 := by
      by_contra h; push Not at h
      have : 0 < v.2 := by nlinarith
      nlinarith
    have hv2' : 0 ≤ v.2 := by
      by_contra h; push Not at h
      have : 0 < v.1 := by nlinarith
      nlinarith
    have hv : v = v.1 • ((1, 0) : P) + v.2 • ((0, 1) : P) := by ext <;> simp
    rw [hv, map_add, map_smul, map_smul, smul_eq_mul, smul_eq_mul]
    rcases hv1'.eq_or_lt with h0 | h0
    · rw [← h0] at hs ⊢
      have : 0 < v.2 := by linarith
      simp only [zero_mul, zero_add]; positivity
    · have := mul_pos h0 h1
      nlinarith [mul_nonneg hv2' h2.le]

/-- `−(c • gM)(ℓ, ·) = (c/2) dU`. -/
lemma ct_neg_scaled_ell (c : ℝ) : -((c • gM) ellV) = (c / 2) • fst ℝ ℝ ℝ := by
  ext
  · simp [gM_apply, ellV]; ring
  · simp [gM_apply, ellV]

variable (hpos : ∀ y, 0 < Fh y)

/-- **The rescaled transverse null vector** `n = F̂(φ x)⁻¹ • nN x` (`= (2/F̂) ∂_U`). -/
noncomputable def ct_nN (x : Pt) : P := (Fh (φ x))⁻¹ • nN x

lemma ct_nN_eq (x : Pt) : ct_nN (Fh := Fh) x = dchartInvL p₀ x ((Fh (φ x))⁻¹ • nvec) := by
  rw [ct_nN, nN, map_smul]

lemma ct_A_nN (x : Pt) : dchartL p₀ x (ct_nN (Fh := Fh) x) = (Fh (φ x))⁻¹ • nvec := by
  rw [ct_nN_eq, mc_AB p₀ (src x)]

include hpos in
/-- The chart representative of `g_F` in `φ`: `y ↦ F̂(y) gM`. -/
lemma ct_hRep : hRep (cz_minkF hpos).g p₀ = fun y => Fh y • gM := by
  funext y
  rw [cz_minkF, MSpacetime.cz_hRep_scale, hRep_eq]
  show Fh (extChartAt 𝓘(ℝ, P) p₀ (ψ y)) • gM = _
  rw [φψ]

include hpos in
lemma ct_gCh_p₀ (x : Pt) : (cz_minkF hpos).gCh p₀ x = Fh (φ x) • gM := by
  show hRep (cz_minkF hpos).g p₀ (φ x) = _
  rw [ct_hRep hpos]

include hpos in
lemma ct_D_eq : (cz_minkF hpos).D JN = minkN.D JN := by
  rw [cz_minkF, minkN.cz_scale_D]

include hpos in
lemma ct_H_eq : (cz_minkF hpos).H JN = minkN.H JN := by
  rw [cz_minkF, minkN.cz_scale_H]

include hpos in
/-- **The intrinsic frame hypotheses on the curved `N`, at every point of `D`.** -/
theorem ct_frameHyp {x : Pt} (hx : x ∈ minkN.D JN) :
    TCF.FrameHyp ((cz_minkF hpos).gE x) (ℓN x) (ct_nN (Fh := Fh) x) (dcov (Θ₀ ∘ φ) x) := by
  have hc : covCh (Θ₀ ∘ φ) p₀ x = dTh (fun s => -Real.log s) (φ x) := covCh_ThetaG goodG_log hx
  have h := (cz_minkF hpos).mc_frameHyp_ofChart (Θ := Θ₀ ∘ φ) p₀ (src x) (ℓ' := ellV)
    (n' := (Fh (φ x))⁻¹ • nvec) (by
      rw [ct_gCh_p₀ hpos, hc]
      have h := mc_dTh_pos goodG_log ((mem_D_JN_iff x).1 hx)
      exact ct_frameHyp_scaled (hpos _) h.1 h.2)
  rw [ct_nN_eq]; exact h

include hpos in
/-- The rate on the curved `N`: `dΘ₀(ℓ)/dΘ₀(n) = (−U/2)·F̂(U, V)`. -/
lemma ct_ratio {x : Pt} (hx : x ∈ minkN.D JN) :
    dcov (Θ₀ ∘ φ) x (ℓN x) / dcov (Θ₀ ∘ φ) x (ct_nN (Fh := Fh) x) = -(φ x).1 / 2 * Fh (φ x) := by
  have hF := mc_witness_frameHyp goodG_log hx
  have hξ' : ∀ v, TCF.FutCausal (TCF.bil (minkN.gE x)) (ℓN x) (nN x) v →
      0 < ((dcov (Θ₀ ∘ φ) x : P →L[ℝ] ℝ) : P →ₗ[ℝ] ℝ) v := hF.2
  obtain ⟨-, hb⟩ := TCF.tc_pos hF.1 hξ'
  have hb' : 0 < dcov (Θ₀ ∘ φ) x (nN x) := hb
  have hc : Fh (φ x) ≠ 0 := (hpos _).ne'
  rw [ct_nN, map_smul, smul_eq_mul, ← ratio_Θ₀ hx]
  field_simp

include hpos in
/-- **The chart bound:** `F̂` continuous and positive ⟹ `F̂ ∘ φ > F̂(φ q)/2` near `q`, so
`‖F̂(φ x)⁻¹ nvec‖ ≤ (2/F̂(φ q)) ‖nvec‖`. -/
lemma ct_bound (hFc : Continuous Fh) (q : Pt) :
    ∀ᶠ x in 𝓝 q, ‖(Fh (φ x))⁻¹ • nvec‖ ≤ 2 / Fh (φ q) * ‖nvec‖ := by
  have hcq : ContinuousAt (fun x => Fh (φ x)) q := (hFc.comp φ_continuous).continuousAt
  have hq := hpos (φ q)
  filter_upwards [hcq.eventually (lt_mem_nhds (show Fh (φ q) / 2 < Fh (φ q) by linarith))]
    with x hx
  rw [norm_smul, Real.norm_eq_abs, abs_inv, abs_of_pos (hpos _)]
  refine mul_le_mul_of_nonneg_right ?_ (norm_nonneg _)
  rw [inv_eq_one_div, div_le_div_iff₀ (hpos _) hq]
  linarith

/-- The constant coordinate change `D(e_q ∘ φ⁻¹)`: `nullInvL` if `t(q) < 0`, else `id`. -/
noncomputable def ct_Tq (q : Pt) : P →L[ℝ] P :=
  if tco q < 0 then nullInvL else ContinuousLinearMap.id ℝ P

lemma ct_dchartL_q (q x : Pt) (w : P) : dchartL q x (dchartInvL p₀ x w) = ct_Tq q w := by
  by_cases hq : tco q < 0
  · rw [ct_Tq, ite_eq_left hq]
    show dchart q x (dchartInv p₀ (extChartAt 𝓘(ℝ, P) p₀ x) w) = _
    rw [me_dchart_neg hq, dinv_eq]
    by_cases hx : tco x < 0
    · simp only [hx, ite_true, nullInvL_apply]
    · simp only [hx, ite_false]
  · rw [ct_Tq, ite_eq_right hq]
    have e : (dchartL q x : P →L[ℝ] P) = dchartL p₀ x := by
      unfold dchartL; rw [extChartAt_nonneg hq]
    rw [e, mc_AB p₀ (src x)]; rfl

lemma ct_Tq_p₀ : ct_Tq p₀ = ContinuousLinearMap.id ℝ P := by
  rw [ct_Tq, ite_eq_right (show ¬ tco p₀ < 0 from lt_irrefl (0:ℝ))]

variable (hFc : ContDiff ℝ 1 Fh)

include hFc in
/-- **③ Tangency on the curved `N`, at every horizon point (BUILT).** For every positive `C¹`
`F̂`, `g_F = −F̂ dU dV`, `Θ₀ ∘ φ` and the rescaled frame `ℓ = ℓN`, `n = ct_nN`, along `𝓝[D] q`
(a proper filter): the frame hypotheses hold eventually; the rate `(−U/2) F̂ → 0`; the components
in the preferred chart at `q` satisfy `‖dchartL q x (n x)‖ ≤ C` and `dchartL q x (ℓ x) → ℓ₀ = T_q ∂_V`;
`mc_tangency_at_N` gives `dΘ^{e_q}/dΘ(n) → −g_{F,q}(ℓ₀, ·)`; and in the global chart `φ`
(`mc_tangency_limit_N`) `dΘ^φ/dΘ(n) → (F̂(φ q)/2) dU`. -/
theorem ct_witness_tangency_F (q : Pt) (hq : q ∈ (cz_minkF hpos).H JN) :
    (𝓝[(cz_minkF hpos).D JN] q).NeBot ∧
    (∀ᶠ x in 𝓝[(cz_minkF hpos).D JN] q,
      TCF.FrameHyp ((cz_minkF hpos).gE x) (ℓN x) (ct_nN (Fh := Fh) x) (dcov (Θ₀ ∘ φ) x)) ∧
    Tendsto (fun x => dcov (Θ₀ ∘ φ) x (ℓN x) / dcov (Θ₀ ∘ φ) x (ct_nN (Fh := Fh) x))
      (𝓝[(cz_minkF hpos).D JN] q) (𝓝 0) ∧
    (∃ C : ℝ, ∀ᶠ x in 𝓝[(cz_minkF hpos).D JN] q, ‖dchartL q x (ct_nN (Fh := Fh) x)‖ ≤ C) ∧
    Tendsto (fun x => dchartL q x (ℓN x)) (𝓝[(cz_minkF hpos).D JN] q) (𝓝 (ct_Tq q ellV)) ∧
    Tendsto (fun x => (dcov (Θ₀ ∘ φ) x (ct_nN (Fh := Fh) x))⁻¹ • covCh (Θ₀ ∘ φ) q x)
      (𝓝[(cz_minkF hpos).D JN] q) (𝓝 (-((cz_minkF hpos).gE q (ct_Tq q ellV)))) ∧
    Tendsto (fun x => (dcov (Θ₀ ∘ φ) x (ct_nN (Fh := Fh) x))⁻¹ • covCh (Θ₀ ∘ φ) p₀ x)
      (𝓝[(cz_minkF hpos).D JN] q) (𝓝 ((Fh (φ q) / 2) • fst ℝ ℝ ℝ)) := by
  rw [ct_D_eq hpos]
  rw [ct_H_eq hpos] at hq
  have hne : (𝓝[minkN.D JN] q).NeBot :=
    mem_closure_iff_nhdsWithin_neBot.1
      (minkN.mh_hcl me_locallyOneChart (subset_univ _) (frontier_subset_closure hq))
  have hF : ∀ᶠ x in 𝓝[minkN.D JN] q,
      TCF.FrameHyp ((cz_minkF hpos).gE x) (ℓN x) (ct_nN (Fh := Fh) x) (dcov (Θ₀ ∘ φ) x) := by
    filter_upwards [self_mem_nhdsWithin] with x hx using ct_frameHyp hpos hx
  have hq0 : (φ q).1 = 0 := (mem_H_N q).1 hq
  have hFcont : Continuous Fh := hFc.continuous
  have hr : Tendsto (fun x => dcov (Θ₀ ∘ φ) x (ℓN x) / dcov (Θ₀ ∘ φ) x (ct_nN (Fh := Fh) x))
      (𝓝[minkN.D JN] q) (𝓝 0) := by
    have hc : Tendsto (fun x => -(φ x).1 / 2 * Fh (φ x)) (𝓝[minkN.D JN] q) (𝓝 0) := by
      have hcont : Continuous fun x => -(φ x).1 / 2 * Fh (φ x) :=
        ((continuous_fst.comp φ_continuous).neg.div_const (2:ℝ)).mul (hFcont.comp φ_continuous)
      have := (hcont.tendsto q).mono_left (nhdsWithin_le_nhds (s := minkN.D JN))
      simpa [Function.comp_def, hq0] using this
    refine hc.congr' ?_
    filter_upwards [self_mem_nhdsWithin] with x hx using (ct_ratio hpos hx).symm
  have hb := (ct_bound hpos hFcont q).filter_mono (nhdsWithin_le_nhds (s := minkN.D JN))
  -- in the chart at `q`
  have hnq : ∀ᶠ x in 𝓝[minkN.D JN] q,
      ‖dchartL q x (ct_nN (Fh := Fh) x)‖ ≤ ‖ct_Tq q‖ * (2 / Fh (φ q) * ‖nvec‖) := by
    filter_upwards [hb] with x hx
    rw [ct_nN_eq, ct_dchartL_q]
    exact (ct_Tq q).le_opNorm_of_le hx
  have hℓq : Tendsto (fun x => dchartL q x (ℓN x)) (𝓝[minkN.D JN] q) (𝓝 (ct_Tq q ellV)) :=
    tendsto_const_nhds.congr fun x => (ct_dchartL_q q x ellV).symm
  have hat := (cz_minkF hpos).mc_tangency_at_N (cz_minkF_locallyOneChart hFc hpos) (mem_univ q)
    nhdsWithin_le_nhds hF hnq hℓq hr
  -- in the chart `φ`
  have hgc : ContinuousAt (hRep (cz_minkF hpos).g p₀) (extChartAt 𝓘(ℝ, P) p₀ q) := by
    rw [ct_hRep hpos]; exact (hFcont.smul continuous_const).continuousAt
  have hnp : ∀ᶠ x in 𝓝[minkN.D JN] q, ‖dchartL p₀ x (ct_nN (Fh := Fh) x)‖ ≤
      2 / Fh (φ q) * ‖nvec‖ := by
    filter_upwards [hb] with x hx
    rw [ct_A_nN]; exact hx
  have h2 := (cz_minkF hpos).mc_tangency_limit_N p₀ (src q) nhdsWithin_le_nhds (ℓ₀ := ellV)
    hgc hF hnp (tendsto_const_nhds.congr fun x => (A_ℓN x).symm) hr
  rw [ct_hRep hpos] at h2
  refine ⟨hne, hF, hr, ⟨_, hnq⟩, hℓq, hat, ?_⟩
  have e : -((fun y => Fh y • gM) (extChartAt 𝓘(ℝ, P) p₀ q) ellV) = (Fh (φ q) / 2) • fst ℝ ℝ ℝ :=
    ct_neg_scaled_ell _
  rwa [e] at h2

include hFc in
/-- **The headline on the curved `N`, tangency clause instantiated (BUILT).** The conclusion of
`cz_witness_headline_F`, with its general (∀ frames) tangency clause instantiated, at every point
`q` of `∂J⁻(𝒥⁺) = 𝓗⁺`, at the rescaled frame `ℓ = ℓN`, `n = ct_nN`, along `𝓝[D] q`: the limit
`−g_{F,q}(T_q ∂_V, ·)` in the preferred chart at `q` and `(F̂(φ q)/2) dU` in `φ`; at `p₀`, where the
two charts agree, the limit is `−g_{F,p₀}(∂_V, ·) = (F̂(0,0)/2) dU`. -/
theorem ct_witness_headline_F :
    ∃ O_N : ℝ → Pt,
      (∀ x, (cz_witnessExtF hpos).Ω x ^ 2 =
        1 / (Fh (φ x) * ((1 + (φ x).1 ^ 2) * (1 + (φ x).2 ^ 2)))) ∧
      (∀ x, x ∈ frontier ((cz_witnessExtF hpos).ι ⁻¹' cz_St.JpastSet cz_scri) ↔ (φ x).1 = 0) ∧
      (frontier ((cz_witnessExtF hpos).ι ⁻¹' cz_St.JpastSet cz_scri)).Nonempty ∧
      (cz_minkF hpos).H JN = frontier ((cz_witnessExtF hpos).ι ⁻¹' cz_St.JpastSet cz_scri) ∧
      (cz_minkF hpos).SublevelProper JN (Θ₀ ∘ φ) ∧
      KLi ((cz_minkF hpos).slice JN (Θ₀ ∘ φ)) =
        frontier ((cz_witnessExtF hpos).ι ⁻¹' cz_St.JpastSet cz_scri) ∧
      KLs ((cz_minkF hpos).slice JN (Θ₀ ∘ φ)) =
        frontier ((cz_witnessExtF hpos).ι ⁻¹' cz_St.JpastSet cz_scri) ∧
      KLi ((cz_minkF hpos).cone O_N) =
        frontier ((cz_witnessExtF hpos).ι ⁻¹' cz_St.JpastSet cz_scri) ∧
      KLs ((cz_minkF hpos).cone O_N) =
        frontier ((cz_witnessExtF hpos).ι ⁻¹' cz_St.JpastSet cz_scri) ∧
      (∀ q ∈ frontier ((cz_witnessExtF hpos).ι ⁻¹' cz_St.JpastSet cz_scri),
        Tendsto (fun x => (dcov (Θ₀ ∘ φ) x (ct_nN (Fh := Fh) x))⁻¹ • covCh (Θ₀ ∘ φ) q x)
          (𝓝[(cz_minkF hpos).D JN] q) (𝓝 (-((cz_minkF hpos).gE q (ct_Tq q ellV)))) ∧
        Tendsto (fun x => (dcov (Θ₀ ∘ φ) x (ct_nN (Fh := Fh) x))⁻¹ • covCh (Θ₀ ∘ φ) p₀ x)
          (𝓝[(cz_minkF hpos).D JN] q) (𝓝 ((Fh (φ q) / 2) • fst ℝ ℝ ℝ))) ∧
      p₀ ∈ frontier ((cz_witnessExtF hpos).ι ⁻¹' cz_St.JpastSet cz_scri) ∧
      Tendsto (fun x => (dcov (Θ₀ ∘ φ) x (ct_nN (Fh := Fh) x))⁻¹ • covCh (Θ₀ ∘ φ) p₀ x)
        (𝓝[(cz_minkF hpos).D JN] p₀) (𝓝 (-((cz_minkF hpos).gE p₀ ellV))) ∧
      -((cz_minkF hpos).gE p₀ ellV) = (Fh (0, 0) / 2) • fst ℝ ℝ ℝ := by
  obtain ⟨O_N, hΩ, hmem, hne, h0, h1, h2, h3, h4, h5, h6⟩ := cz_witness_headline_F hFc hpos
  have hcl : ∀ q ∈ frontier ((cz_witnessExtF hpos).ι ⁻¹' cz_St.JpastSet cz_scri),
      Tendsto (fun x => (dcov (Θ₀ ∘ φ) x (ct_nN (Fh := Fh) x))⁻¹ • covCh (Θ₀ ∘ φ) q x)
        (𝓝[(cz_minkF hpos).D JN] q) (𝓝 (-((cz_minkF hpos).gE q (ct_Tq q ellV)))) ∧
      Tendsto (fun x => (dcov (Θ₀ ∘ φ) x (ct_nN (Fh := Fh) x))⁻¹ • covCh (Θ₀ ∘ φ) p₀ x)
        (𝓝[(cz_minkF hpos).D JN] q) (𝓝 ((Fh (φ q) / 2) • fst ℝ ℝ ℝ)) := by
    intro q hq
    have hqH : q ∈ (cz_minkF hpos).H JN := h0 ▸ hq
    obtain ⟨-, hF, hr, ⟨C, hn⟩, hℓ, -, hp⟩ := ct_witness_tangency_F hpos hFc q hqH
    -- the headline's own (∀) tangency clause, instantiated
    exact ⟨h6 q hq ℓN ct_nN _ C _ nhdsWithin_le_nhds hF hn hℓ hr, hp⟩
  have hp₀ : p₀ ∈ frontier ((cz_witnessExtF hpos).ι ⁻¹' cz_St.JpastSet cz_scri) :=
    (hmem p₀).2 (by rw [φ_p₀])
  have hg : -((cz_minkF hpos).gE p₀ ellV) = (Fh (0, 0) / 2) • fst ℝ ℝ ℝ := by
    have e : (cz_minkF hpos).gE p₀ = (cz_minkF hpos).gCh p₀ p₀ := by
      show _ = hRep (cz_minkF hpos).g p₀ (extChartAt 𝓘(ℝ, P) p₀ p₀)
      rw [(cz_minkF hpos).mc_gCh_self p₀]
    rw [e, ct_gCh_p₀ hpos, φ_p₀]; exact ct_neg_scaled_ell _
  have hat := (hcl p₀ hp₀).1
  rw [ct_Tq_p₀] at hat
  exact ⟨O_N, hΩ, hmem, hne, h0, h1, h2, h3, h4, h5, hcl, hp₀, hat, hg⟩

/-- **Non-vacuity, `F̂ = e^{UV}` (BUILT).** The hypotheses hold (`C¹`, positive), `p₀ ∈ 𝓗⁺`, the
filter `𝓝[D] p₀` is proper, the frame hypotheses and the rate hold there, the rescaled `n` differs
from the flat `nN` (at `φ⁻¹(−1, 1)`, where `F̂ = e^{−1}`), and the limit at `p₀` is
`(e^0/2) dU = ½ dU` (`F̂ ≡ 1` on `{U = 0}`, so on this `F̂` the limit agrees with the flat one). -/
theorem ct_exp :
    let Fe : P → ℝ := fun y => Real.exp (y.1 * y.2)
    let hpe : ∀ y, 0 < Fe y := fun _ => Real.exp_pos _
    ContDiff ℝ 1 Fe ∧ p₀ ∈ (cz_minkF hpe).H JN ∧ (𝓝[(cz_minkF hpe).D JN] p₀).NeBot ∧
    (∀ᶠ x in 𝓝[(cz_minkF hpe).D JN] p₀,
      TCF.FrameHyp ((cz_minkF hpe).gE x) (ℓN x) (ct_nN (Fh := Fe) x) (dcov (Θ₀ ∘ φ) x)) ∧
    Tendsto (fun x => dcov (Θ₀ ∘ φ) x (ℓN x) / dcov (Θ₀ ∘ φ) x (ct_nN (Fh := Fe) x))
      (𝓝[(cz_minkF hpe).D JN] p₀) (𝓝 0) ∧
    ct_nN (Fh := Fe) (ψ (-1, 1)) ≠ nN (ψ (-1, 1)) ∧
    Tendsto (fun x => (dcov (Θ₀ ∘ φ) x (ct_nN (Fh := Fe) x))⁻¹ • covCh (Θ₀ ∘ φ) p₀ x)
      (𝓝[(cz_minkF hpe).D JN] p₀) (𝓝 ((1 / 2 : ℝ) • fst ℝ ℝ ℝ)) := by
  intro Fe hpe
  have hFc : ContDiff ℝ 1 Fe := Real.contDiff_exp.comp (contDiff_fst.mul contDiff_snd)
  have hp : p₀ ∈ (cz_minkF hpe).H JN := by
    rw [ct_H_eq hpe]; exact (mem_H_N p₀).2 (by rw [show extChartAt 𝓘(ℝ, P) p₀ p₀ = φ p₀ from rfl,
      φ_p₀])
  obtain ⟨hne, hF, hr, -, -, -, hlim⟩ := ct_witness_tangency_F hpe hFc p₀ hp
  refine ⟨hFc, hp, hne, hF, hr, fun h => ?_, ?_⟩
  · have h1 := congrArg (dchartL p₀ (ψ (-1, 1))) h
    rw [ct_A_nN, A_nN] at h1
    have h2 := congrArg Prod.fst h1
    simp only [nvec, Prod.smul_fst, smul_eq_mul, Fe] at h2
    rw [show φ (ψ (-1, 1)) = (-1, 1) from φψ _] at h2
    have h3 : (Real.exp ((-1 : ℝ) * 1))⁻¹ = 1 := by linarith
    have h4 : Real.exp ((-1 : ℝ) * 1) = 1 := by rw [← inv_inv (Real.exp _), h3, inv_one]
    have h5 : ((-1 : ℝ) * 1) = 0 := Real.exp_eq_one_iff _ |>.1 h4
    norm_num at h5
  · have e : Fe (φ p₀) / 2 = 1 / 2 := by simp only [Fe, φ_p₀]; norm_num
    rwa [e] at hlim

/-- **Non-vacuity, a limit that differs from the flat one (BUILT).** For `F̂ = e^V` at the horizon
point `q = φ⁻¹(0, 1)`, the instantiated limit in `φ` is `(e/2) dU ≠ ½ dU` (the flat limit of
`mc_witness_tangency_holds`). -/
theorem ct_expV_differs :
    let Fv : P → ℝ := fun y => Real.exp y.2
    let hpv : ∀ y, 0 < Fv y := fun _ => Real.exp_pos _
    ψ (0, 1) ∈ (cz_minkF hpv).H JN ∧
    Tendsto (fun x => (dcov (Θ₀ ∘ φ) x (ct_nN (Fh := Fv) x))⁻¹ • covCh (Θ₀ ∘ φ) p₀ x)
      (𝓝[(cz_minkF hpv).D JN] (ψ (0, 1))) (𝓝 ((Real.exp 1 / 2) • fst ℝ ℝ ℝ)) ∧
    (Real.exp 1 / 2) • fst ℝ ℝ ℝ ≠ (1 / 2 : ℝ) • fst ℝ ℝ ℝ := by
  intro Fv hpv
  have hFc : ContDiff ℝ 1 Fv := Real.contDiff_exp.comp contDiff_snd
  have hφ : φ (ψ (0, 1)) = (0, 1) := φψ _
  have hq : ψ (0, 1) ∈ (cz_minkF hpv).H JN := by
    rw [ct_H_eq hpv]; exact (mem_H_N _).2 (by rw [show extChartAt 𝓘(ℝ, P) p₀ (ψ (0, 1)) =
      φ (ψ (0, 1)) from rfl, hφ])
  obtain ⟨-, -, -, -, -, -, hlim⟩ := ct_witness_tangency_F hpv hFc _ hq
  refine ⟨hq, ?_, fun h => ?_⟩
  · have e : Fv (φ (ψ (0, 1))) / 2 = Real.exp 1 / 2 := by simp only [Fv, hφ]
    rwa [e] at hlim
  · have h1 := congrArg (fun f : P →L[ℝ] ℝ => f ((1, 0) : P)) h
    simp only [smul_apply, ContinuousLinearMap.coe_fst', smul_eq_mul,
      mul_one] at h1
    have : Real.exp 1 = 1 := by linarith
    have h5 := (Real.exp_eq_one_iff _).1 this
    norm_num at h5

end NModel

/-! ## NEW (campaign 97 ①, `r7675+71`): Schwarzschild in Kruskal's radial plane

`r(U, V)` (campaign 80's `rK`, the inverse of `h(r) = (r/2M − 1) e^{r/2M}` at `−UV`) and
`F = (32M³/r) e^{−r/2M}` (campaign 80's `FS`) are copied in (namespace `Kruskal`, names kept). New:
`r` is `C¹` on all of `{UV < 1}` (`sk_rK_contDiffOn`), so is `F` (`sk_FS_contDiffOn`); the spacetime
`sk_S hM = (minkN restricted to M = φ⁻¹{UV < 1}).cz_scale F̃`, with `F̃ = F` on `M` and `1` off `M`
(`sk_F`), so `hRep g p₀ = F • gM` (`g = −F dU dV`) on `{UV < 1}`; `LocallyOneChart`; the static
observer on `UV = −hK r₀`; `D`, `𝓗⁺` and 3a. Every new name has the prefix `sk_`. -/

namespace Kruskal
open Model

/-! ### Copied (campaign 80, `TangencyCondition.lean`): the areal radius `r(U,V)` -/

/-- `h(x) = (x/(2M) − 1) e^{x/(2M)}`; `r` solves `h(r) = −UV`. -/
noncomputable def hK (M x : ℝ) : ℝ := (x / (2 * M) - 1) * Real.exp (x / (2 * M))

/-- `h′(x) = x/(4M²) e^{x/(2M)}`. -/
noncomputable def hK' (M x : ℝ) : ℝ := x / (4 * M ^ 2) * Real.exp (x / (2 * M))

section Radius
variable {M : ℝ} (hM : 0 < M)
include hM

lemma hasDerivAt_hK (x : ℝ) : HasDerivAt (hK M) (hK' M x) x := by
  have h1 : HasDerivAt (fun x : ℝ => x / (2 * M)) (1 / (2 * M)) x :=
    (hasDerivAt_id x).div_const _
  have h := (h1.sub_const 1).mul h1.exp
  refine h.congr_deriv ?_
  simp only [hK']; field_simp; ring

omit hM in
lemma continuous_hK : Continuous (hK M) := by
  unfold hK; fun_prop

lemma hK_strictMonoOn : StrictMonoOn (hK M) (Ici 0) := by
  refine strictMonoOn_of_deriv_pos (convex_Ici 0) continuous_hK.continuousOn fun x hx => ?_
  rw [interior_Ici] at hx
  rw [(hasDerivAt_hK hM x).deriv]
  have : 0 < x := hx
  unfold hK'; positivity

omit hM in
lemma hK_zero : hK M 0 = -1 := by simp [hK]

lemma hK_two : hK M (2 * M) = 0 := by
  simp only [hK]; rw [div_self (by positivity)]; simp

lemma hK_gt {x : ℝ} (hx : 0 < x) : -1 < hK M x := by
  rw [← hK_zero]
  exact hK_strictMonoOn hM (mem_Ici.2 le_rfl) hx.le hx

lemma hK_exists {y : ℝ} (hy : -1 < y) : ∃ x, 0 < x ∧ hK M x = y := by
  set b := 2 * M * (|y| + 2)
  have hb : 0 ≤ b := by positivity
  have hyb : y ≤ hK M b := by
    have h1 : 0 ≤ b / (2 * M) - 1 := by
      rw [show b / (2 * M) = |y| + 2 by simp only [b]; field_simp]
      linarith [abs_nonneg y]
    have h2 : b / (2 * M) - 1 ≤ hK M b :=
      le_mul_of_one_le_right h1 (Real.one_le_exp (by positivity))
    have h3 : b / (2 * M) - 1 = |y| + 1 := by simp only [b]; field_simp; ring
    linarith [le_abs_self y]
  obtain ⟨x, hx, hxy⟩ := intermediate_value_Icc hb continuous_hK.continuousOn
    ⟨by rw [hK_zero]; exact hy.le, hyb⟩
  refine ⟨x, ?_, hxy⟩
  rcases hx.1.eq_or_lt with h | h
  · rw [← h, hK_zero] at hxy; linarith
  · exact h

end Radius

open Classical in
/-- The inverse of `h` on `(−1, ∞) → (0, ∞)` (junk value `0` elsewhere). -/
noncomputable def rinv (M y : ℝ) : ℝ :=
  if h : ∃ x, 0 < x ∧ hK M x = y then h.choose else 0

section Radius2
variable {M : ℝ} (hM : 0 < M)
include hM

lemma rinv_spec {y : ℝ} (hy : -1 < y) : 0 < rinv M y ∧ hK M (rinv M y) = y := by
  have h := hK_exists hM hy
  simp only [rinv, h, ↓reduceDIte]
  exact h.choose_spec

lemma rinv_hK {x : ℝ} (hx : 0 < x) : rinv M (hK M x) = x := by
  obtain ⟨h1, h2⟩ := rinv_spec hM (hK_gt hM hx)
  exact (hK_strictMonoOn hM).injOn (mem_Ici.2 h1.le) (mem_Ici.2 hx.le) h2

lemma rinv_zero : rinv M 0 = 2 * M := by
  rw [← hK_two hM, rinv_hK hM (by positivity)]

lemma rinv_strictMonoOn : StrictMonoOn (rinv M) (Ioi (-1)) := by
  intro y₁ hy₁ y₂ hy₂ hlt
  obtain ⟨a1, b1⟩ := rinv_spec hM hy₁
  obtain ⟨a2, b2⟩ := rinv_spec hM hy₂
  by_contra h; push Not at h
  have := (hK_strictMonoOn hM).monotoneOn (mem_Ici.2 a2.le) (mem_Ici.2 a1.le) h
  rw [b1, b2] at this; linarith

lemma rinv_continuousAt {a : ℝ} (ha : -1 < a) : ContinuousAt (rinv M) a := by
  refine continuousAt_of_monotoneOn_of_image_mem_nhds (rinv_strictMonoOn hM).monotoneOn
    (Ioi_mem_nhds ha) ?_
  refine mem_of_superset (Ioi_mem_nhds (rinv_spec hM ha).1) fun x hx => ?_
  exact ⟨hK M x, hK_gt hM hx, rinv_hK hM hx⟩

/-- **The derivative of the inverse** (inverse function theorem in one variable). -/
lemma rinv_hasDerivAt {a : ℝ} (ha : -1 < a) :
    HasDerivAt (rinv M) (hK' M (rinv M a))⁻¹ a := by
  refine HasDerivAt.of_local_left_inverse (rinv_continuousAt hM ha) (hasDerivAt_hK hM _) ?_ ?_
  · have := (rinv_spec hM ha).1; unfold hK'; positivity
  · filter_upwards [Ioi_mem_nhds ha] with y hy using (rinv_spec hM hy).2

end Radius2

/-- The areal radius in Kruskal coordinates: `r(U,V) = h⁻¹(−UV)`. -/
noncomputable def rK (M : ℝ) (p : P) : ℝ := rinv M (-(p.1 * p.2))

/-- `F = (32M³/r) e^{−r/2M}`, with `r = rK`. -/
noncomputable def FS (M : ℝ) (p : P) : ℝ := 32 * M ^ 3 / rK M p * Real.exp (-rK M p / (2 * M))

/-! ### NEW: `r` and `F` on the whole of `{UV < 1}` -/

/-- **The Kruskal domain** `{UV < 1}` (`r > 0`), in null coordinates. -/
def sk_kM : Set P := {p | p.1 * p.2 < 1}

lemma sk_kM_open : IsOpen sk_kM :=
  isOpen_lt (continuous_fst.mul continuous_snd) continuous_const

lemma sk_kM_UV {p : P} (hp : p ∈ sk_kM) : -1 < -(p.1 * p.2) := by
  have : p.1 * p.2 < 1 := hp
  linarith

section SK
variable {M : ℝ} (hM : 0 < M)
include hM

lemma sk_rinv_continuousOn : ContinuousOn (rinv M) (Ioi (-1)) :=
  fun _ ha => (rinv_continuousAt hM ha).continuousWithinAt

/-- **`r` is `C¹` in `−UV` on `(−1, ∞)`** (inverse function theorem: `h′(r) = r e^{r/2M}/4M² > 0`). -/
lemma sk_rinv_contDiffOn : ContDiffOn ℝ 1 (rinv M) (Ioi (-1)) := by
  rw [show (1 : WithTop ℕ∞) = 0 + 1 from rfl, contDiffOn_succ_iff_deriv_of_isOpen isOpen_Ioi]
  refine ⟨fun a ha => (rinv_hasDerivAt hM ha).differentiableAt.differentiableWithinAt,
    by simp, ?_⟩
  rw [contDiffOn_zero]
  have hc : ContinuousOn (fun a => (hK' M (rinv M a))⁻¹) (Ioi (-1)) := by
    refine ContinuousOn.inv₀ ?_ ?_
    · unfold hK'
      exact ((sk_rinv_continuousOn hM).div_const _).mul
        ((sk_rinv_continuousOn hM).div_const _).rexp
    · intro a ha
      have := (rinv_spec hM ha).1
      unfold hK'; positivity
  exact hc.congr fun a ha => (rinv_hasDerivAt hM ha).deriv

/-- `r > 0` and `h(r) = −UV` on all of `{UV < 1}`. -/
lemma sk_rK_spec {p : P} (hp : p ∈ sk_kM) : 0 < rK M p ∧ hK M (rK M p) = -(p.1 * p.2) :=
  rinv_spec hM (sk_kM_UV hp)

/-- **`r(U, V)` is `C¹` on `{UV < 1}`.** -/
theorem sk_rK_contDiffOn : ContDiffOn ℝ 1 (rK M) sk_kM := by
  have e : rK M = rinv M ∘ (fun p : P => -(p.1 * p.2)) := rfl
  rw [e]
  exact (sk_rinv_contDiffOn hM).comp (contDiff_fst.mul contDiff_snd).neg.contDiffOn
    fun p hp => sk_kM_UV hp

/-- **`r = 2M ⇔ UV = 0`** on `{UV < 1}`. -/
theorem sk_rK_eq_two_iff {p : P} (hp : p ∈ sk_kM) : rK M p = 2 * M ↔ p.1 * p.2 = 0 := by
  constructor
  · intro h
    have := (sk_rK_spec hM hp).2
    rw [h, hK_two hM] at this; linarith
  · intro h
    show rinv M (-(p.1 * p.2)) = 2 * M
    rw [h, neg_zero, rinv_zero hM]

lemma sk_FS_pos {p : P} (hp : p ∈ sk_kM) : 0 < FS M p := by
  have := (sk_rK_spec hM hp).1; unfold FS; positivity

/-- **`F = (32M³/r) e^{−r/2M}` is `C¹` on `{UV < 1}`.** -/
theorem sk_FS_contDiffOn : ContDiffOn ℝ 1 (FS M) sk_kM := by
  have hr := sk_rK_contDiffOn hM
  have h := (contDiffOn_const (c := 32 * M ^ 3)).div hr fun p hp => (sk_rK_spec hM hp).1.ne'
  exact (h.mul ((hr.neg.div_const (2 * M)).exp)).congr fun p _ => rfl

lemma sk_rK_hK {x : ℝ} (hx : 0 < x) (U : ℝ) (hU : U ≠ 0) :
    rK M (U, -hK M x / U) = x := by
  show rinv M (-(U * (-hK M x / U))) = x
  rw [show -(U * (-hK M x / U)) = hK M x by field_simp]
  exact rinv_hK hM hx

/-- **`F` is not constant** (non-vacuity): `F = 16M²/e` at `r = 2M` (`(0,0)`), `F = 8M²/e²` at
`r = 4M` (`(−1, h(4M))`). -/
theorem sk_FS_nonconst :
    FS M (0, 0) = 16 * M ^ 2 * Real.exp (-1) ∧
    FS M (-1, -hK M (4 * M) / (-1)) = 8 * M ^ 2 * Real.exp (-2) ∧
    FS M (0, 0) ≠ FS M (-1, -hK M (4 * M) / (-1)) := by
  have h0 : rK M (0, 0) = 2 * M := (sk_rK_eq_two_iff hM (p := (0, 0))
    (show (0:ℝ) * 0 < 1 by norm_num)).2 (by norm_num)
  have h1 : rK M (-1, -hK M (4 * M) / (-1)) = 4 * M :=
    sk_rK_hK hM (by positivity) (-1) (by norm_num)
  have e0 : FS M (0, 0) = 16 * M ^ 2 * Real.exp (-1) := by
    unfold FS; rw [h0, show -(2 * M) / (2 * M) = -1 by field_simp]; field_simp; ring
  have e1 : FS M (-1, -hK M (4 * M) / (-1)) = 8 * M ^ 2 * Real.exp (-2) := by
    unfold FS; rw [h1, show -(4 * M) / (2 * M) = -2 by field_simp; ring]; field_simp; ring
  refine ⟨e0, e1, ?_⟩
  rw [e0, e1]
  intro h
  have h2 : Real.exp (-2) = Real.exp (-1) * Real.exp (-1) := by rw [← Real.exp_add]; norm_num
  have he : 0 < Real.exp (-1) := Real.exp_pos _
  have hlt : Real.exp (-1) < 1 := by
    rw [show (1:ℝ) = Real.exp 0 from Real.exp_zero.symm]; exact Real.exp_lt_exp.2 (by norm_num)
  rw [h2] at h
  have hM2 : 0 < M ^ 2 := by positivity
  nlinarith [mul_pos (mul_pos hM2 he) (sub_pos.2 hlt)]

end SK

end Kruskal

/-! ### NEW: scaling by `F > 0` given only on `M` (as `F̃ = F` on `M`) -/

section SkScale
open Manifold
set_option linter.unusedSectionVars false

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
variable {N : Type*} [TopologicalSpace N] [ChartedSpace E N] [IsManifold 𝓘(ℝ, E) 1 N]

namespace MSpacetime

/-- **`LocallyOneChart` passes to `F g` when `F` is `C¹` only on the chart images of `M`**
(generalises `cz_scale_locallyOneChart`, which asks for `C¹` on the whole chart target). -/
theorem sk_scale_locallyOneChart (S : MSpacetime E N) {F : N → ℝ} (hF : ∀ x, 0 < F x)
    (hL : S.LocallyOneChart)
    (hFc : ∀ p ∈ S.M, ContDiffOn ℝ 1 (fun y => F ((extChartAt 𝓘(ℝ, E) p).symm y))
      (extChartAt 𝓘(ℝ, E) p '' (S.M ∩ (chartAt E p).source))) :
    (S.cz_scale F hF).LocallyOneChart := by
  intro p hp
  obtain ⟨U, hU, hpU, hUsub, hg, hT⟩ := hL p hp
  refine ⟨U, hU, hpU, hUsub, ?_, hT⟩
  rw [show hRep (S.cz_scale F hF).g p = fun y => F ((extChartAt 𝓘(ℝ, E) p).symm y) • hRep S.g p y
    from funext (cz_hRep_scale S hF p)]
  have : IsBoundedSMul ℝ (E →L[ℝ] E →L[ℝ] ℝ) :=
    @NormedSpace.toIsBoundedSMul ℝ (E →L[ℝ] E →L[ℝ] ℝ) _ _ _
  exact ((hFc p hp).mono hUsub).smul hg

end MSpacetime

end SkScale

/-! ### NEW: the flat plane restricted to `{UV < 1}`, in null coordinates -/

namespace Model
open Kruskal

/-- `mink` restricted to `{UV < 1}`. -/
noncomputable def sk_K : Spacetime P := mink.restrict sk_kM sk_kM_open (subset_univ _)

lemma sk_K_tstep_mink {x y : P} (h : sk_K.TStep x y) : mink.TStep x y := by
  obtain ⟨γ, hγ, h0, h1, ht⟩ := h
  exact ⟨γ, hγ, h0, h1, fun t htI => ⟨mem_univ _, (ht t htI).2⟩⟩

lemma sk_K_cstep_mink {x y : P} (h : sk_K.CStep x y) : mink.CStep x y := by
  obtain ⟨γ, hγ, h0, h1, ht⟩ := h
  exact ⟨γ, hγ, h0, h1, fun t htI => ⟨mem_univ _, (ht t htI).2⟩⟩

lemma sk_K_chr_mink {x y : P} (h : sk_K.Chr x y) : mink.Chr x y := by
  induction h with
  | single h => exact Relation.TransGen.single (sk_K_tstep_mink h)
  | tail _ h ih => exact ih.tail (sk_K_tstep_mink h)

lemma sk_K_cau_mink {x y : P} (h : sk_K.Cau x y) : mink.Cau x y := by
  induction h with
  | refl => exact Relation.ReflTransGen.refl
  | tail _ h ih => exact ih.tail (sk_K_cstep_mink h)

/-- The straight segment between two points of `{UV < 1}` with `U`, `V` non-decreasing stays in
`{UV < 1}` (`UV` is convex along it). -/
lemma sk_seg_mem {x y : P} (hx : x ∈ sk_kM) (hy : y ∈ sk_kM) (h1 : x.1 ≤ y.1) (h2 : x.2 ≤ y.2)
    {t : ℝ} (ht : t ∈ Icc (0:ℝ) 1) : x + t • (y - x) ∈ sk_kM := by
  have hx' : x.1 * x.2 < 1 := hx
  have hy' : y.1 * y.2 < 1 := hy
  simp only [sk_kM, mem_ofPred_eq, Prod.fst_add, Prod.snd_add, Prod.smul_fst, Prod.smul_snd,
    Prod.fst_sub, Prod.snd_sub, smul_eq_mul]
  have e : (x.1 + t * (y.1 - x.1)) * (x.2 + t * (y.2 - x.2)) =
      (1 - t) * (x.1 * x.2) + t * (y.1 * y.2) - (y.1 - x.1) * (y.2 - x.2) * (t * (1 - t)) := by
    ring
  rw [e]
  have ha : 0 ≤ y.1 - x.1 := by linarith
  have hb : 0 ≤ y.2 - x.2 := by linarith
  have key := mul_nonneg (mul_nonneg ha hb) (mul_nonneg ht.1 (sub_nonneg.2 ht.2))
  rcases ht.2.lt_or_eq with h | h
  · have h3 : (1 - t) * (x.1 * x.2) < (1 - t) * 1 :=
      mul_lt_mul_of_pos_left hx' (by linarith)
    have h4 : t * (y.1 * y.2) ≤ t * 1 := mul_le_mul_of_nonneg_left hy'.le ht.1
    linarith
  · subst h; nlinarith

lemma sk_deriv_seg (x y : P) (t : ℝ) : deriv (fun t : ℝ => x + t • (y - x)) t = y - x := by
  have h : HasDerivAt (fun t : ℝ => x + t • (y - x)) ((1:ℝ) • (y - x)) t :=
    ((hasDerivAt_id' t).smul_const (y - x)).const_add x
  rw [h.deriv, one_smul]

/-- A timelike step inside `{UV < 1}`: the straight segment. -/
lemma sk_K_tstep_of_lt {x y : P} (hx : x ∈ sk_kM) (hy : y ∈ sk_kM) (h1 : x.1 < y.1)
    (h2 : x.2 < y.2) : sk_K.TStep x y := by
  refine ⟨fun t => x + t • (y - x), contDiff_const.add (contDiff_id.smul contDiff_const),
    by simp, by simp, fun t ht => ⟨sk_seg_mem hx hy h1.le h2.le ht, ?_⟩⟩
  show mink.FutTimelike (x + t • (y - x)) (deriv (fun t : ℝ => x + t • (y - x)) t)
  rw [sk_deriv_seg, futTimelike_iff]
  simp only [Prod.fst_sub, Prod.snd_sub, sub_pos]
  exact ⟨h1, h2⟩

/-- A causal step inside `{UV < 1}`: the straight segment. -/
lemma sk_K_cstep_of_le {x y : P} (hx : x ∈ sk_kM) (hy : y ∈ sk_kM) (h1 : x.1 ≤ y.1)
    (h2 : x.2 ≤ y.2) (h3 : x.1 + x.2 < y.1 + y.2) : sk_K.CStep x y := by
  refine ⟨fun t => x + t • (y - x), contDiff_const.add (contDiff_id.smul contDiff_const),
    by simp, by simp, fun t ht => ⟨sk_seg_mem hx hy h1 h2 ht, ?_⟩⟩
  show mink.FutCausal (x + t • (y - x)) (deriv (fun t : ℝ => x + t • (y - x)) t)
  rw [sk_deriv_seg, futCausal_iff]
  simp only [Prod.fst_sub, Prod.snd_sub, sub_nonneg]
  exact ⟨h1, h2, by linarith⟩

/-- **The static observer**, `O_a(σ) = (−a e^{−σ}, a e^{σ})`, on `UV = −a²`. -/
noncomputable def sk_O (a σ : ℝ) : P := (-(a * Real.exp (-σ)), a * Real.exp σ)

lemma sk_O_UV (a σ : ℝ) : (sk_O a σ).1 * (sk_O a σ).2 = -a ^ 2 := by
  simp only [sk_O]
  have : Real.exp (-σ) * Real.exp σ = 1 := by rw [← Real.exp_add, neg_add_cancel, Real.exp_zero]
  linear_combination (-(a ^ 2)) * this

lemma sk_O_mem (a σ : ℝ) : sk_O a σ ∈ sk_kM := by
  show (sk_O a σ).1 * (sk_O a σ).2 < 1
  rw [sk_O_UV]; nlinarith [sq_nonneg a]

lemma sk_O_mono {a : ℝ} (ha : 0 < a) {s t : ℝ} (h : s < t) :
    (sk_O a s).1 < (sk_O a t).1 ∧ (sk_O a s).2 < (sk_O a t).2 := by
  simp only [sk_O, neg_lt_neg_iff]
  exact ⟨mul_lt_mul_of_pos_left (Real.exp_lt_exp.2 (by linarith)) ha,
    mul_lt_mul_of_pos_left (Real.exp_lt_exp.2 h) ha⟩

/-- **`D = I⁻(O) = {U < 0} ∩ {UV < 1}`** (regions I and IV). -/
theorem sk_K_D {a : ℝ} (ha : 0 < a) : sk_K.D (range (sk_O a)) = {p : P | p.1 < 0} ∩ sk_kM := by
  ext p
  constructor
  · intro hp
    have hpM : p ∈ sk_kM := sk_K.hl_D_subset_M _ hp
    obtain ⟨_, ⟨σ, rfl⟩, h⟩ := mem_iUnion₂.1 hp
    have h1 := (chr_lt (sk_K_chr_mink h)).1
    have h2 : 0 < a * Real.exp (-σ) := mul_pos ha (Real.exp_pos _)
    simp only [sk_O] at h1
    exact ⟨by show p.1 < 0; linarith, hpM⟩
  · rintro ⟨hp1, hpM⟩
    have hp1' : p.1 < 0 := hp1
    have e1 : ∀ᶠ σ in atTop, a * Real.exp (-σ) < -p.1 := by
      have h := Real.tendsto_exp_neg_atTop_nhds_zero.const_mul a
      rw [mul_zero] at h
      exact (tendsto_order.1 h).2 _ (by linarith)
    have e2 : ∀ᶠ σ in atTop, p.2 < a * Real.exp σ :=
      (Real.tendsto_exp_atTop.const_mul_atTop ha).eventually_gt_atTop p.2
    obtain ⟨σ, h1, h2⟩ := (e1.and e2).exists
    exact mem_iUnion₂.2 ⟨sk_O a σ, mem_range_self σ, Relation.TransGen.single
      (sk_K_tstep_of_lt hpM (sk_O_mem a σ) (by simp only [sk_O]; linarith) h2)⟩

/-- `J⁻(O) = {U < 0} ∩ {UV < 1}` too. -/
theorem sk_K_JpastSet {a : ℝ} (ha : 0 < a) :
    sk_K.JpastSet (range (sk_O a)) = {p : P | p.1 < 0} ∩ sk_kM := by
  apply Subset.antisymm
  · intro p hp
    obtain ⟨_, ⟨σ, rfl⟩, h⟩ := mem_iUnion₂.1 hp
    have h1 := (cau_le (sk_K_cau_mink h)).1
    have h2 : 0 < a * Real.exp (-σ) := mul_pos ha (Real.exp_pos _)
    have hpM : p ∈ sk_kM := by
      rcases Relation.ReflTransGen.cases_head h with h | ⟨b, hb, -⟩
      · rw [h]; exact sk_O_mem a σ
      · exact (sk_K.ch_cstep_mem hb).1
    simp only [sk_O] at h1
    exact ⟨by show p.1 < 0; linarith, hpM⟩
  · rw [← sk_K_D ha]
    intro p hp
    obtain ⟨z, hz, h⟩ := mem_iUnion₂.1 hp
    exact mem_iUnion₂.2 ⟨z, hz, sk_K.hl_chr_cau h⟩

/-- The closure of `{U < 0, UV < 1}` is `{U ≤ 0, UV ≤ 1}`. -/
lemma sk_closure_D : closure ({p : P | p.1 < 0} ∩ sk_kM) = {p : P | p.1 ≤ 0 ∧ p.1 * p.2 ≤ 1} := by
  apply Subset.antisymm
  · refine closure_minimal (fun p hp => ⟨le_of_lt hp.1, le_of_lt hp.2⟩) ?_
    exact (isClosed_le continuous_fst continuous_const).inter
      (isClosed_le (continuous_fst.mul continuous_snd) continuous_const)
  · rintro p ⟨hp1, hp2⟩
    rcases hp2.lt_or_eq with h | h
    · have hf : Tendsto (fun ε : ℝ => ((p.1 - ε, p.2) : P)) (𝓝[>] 0) (𝓝 p) := by
        have hc : Continuous (fun ε : ℝ => ((p.1 - ε, p.2) : P)) := by fun_prop
        simpa using (hc.tendsto 0).mono_left nhdsWithin_le_nhds
      refine mem_closure_of_tendsto hf ?_
      have hg : Tendsto (fun ε : ℝ => (p.1 - ε) * p.2) (𝓝[>] 0) (𝓝 (p.1 * p.2)) := by
        have hc : Continuous (fun ε : ℝ => (p.1 - ε) * p.2) := by fun_prop
        simpa using (hc.tendsto 0).mono_left nhdsWithin_le_nhds
      filter_upwards [self_mem_nhdsWithin, hg.eventually (gt_mem_nhds h)] with ε hε hε2
      have : (0:ℝ) < ε := hε
      exact ⟨by show p.1 - ε < 0; linarith, hε2⟩
    · have hp1' : p.1 < 0 := by
        rcases hp1.lt_or_eq with h' | h'
        · exact h'
        · rw [h'] at h; norm_num at h
      have hf : Tendsto (fun ε : ℝ => ((p.1, p.2 + ε) : P)) (𝓝[>] 0) (𝓝 p) := by
        have hc : Continuous (fun ε : ℝ => ((p.1, p.2 + ε) : P)) := by fun_prop
        simpa using (hc.tendsto 0).mono_left nhdsWithin_le_nhds
      refine mem_closure_of_tendsto hf ?_
      filter_upwards [self_mem_nhdsWithin] with ε hε
      have : (0:ℝ) < ε := hε
      refine ⟨hp1', ?_⟩
      show p.1 * (p.2 + ε) < 1
      nlinarith

/-- **`∂J⁻(O)` in the plane: `{U = 0} ∪ {U < 0, UV = 1}`.** The second piece is the past
singularity `r = 0` of region IV, which lies outside `M = {UV < 1}`. -/
theorem sk_K_H {a : ℝ} (ha : 0 < a) :
    sk_K.H (range (sk_O a)) = {p : P | p.1 = 0} ∪ {p : P | p.1 < 0 ∧ p.1 * p.2 = 1} := by
  rw [Spacetime.H, sk_K_JpastSet ha,
    (isOpen_lt continuous_fst continuous_const |>.inter sk_kM_open).frontier_eq, sk_closure_D]
  ext p
  simp only [Set.mem_sdiff, mem_ofPred_eq, mem_inter_iff, mem_union, sk_kM]
  constructor
  · rintro ⟨⟨h1, h2⟩, h3⟩
    rcases h1.lt_or_eq with h | h
    · right; exact ⟨h, le_antisymm h2 (not_lt.1 fun h' => h3 ⟨h, h'⟩)⟩
    · left; exact h
  · rintro (h | ⟨h1, h2⟩)
    · refine ⟨⟨h.le, by rw [h]; norm_num⟩, fun h' => ?_⟩
      rw [h] at h'; exact lt_irrefl _ h'.1
    · exact ⟨⟨h1.le, h2.le⟩, fun h' => by rw [h2] at h'; exact lt_irrefl _ h'.2⟩

end Model

/-! ### NEW: the Schwarzschild spacetime `sk_S` on `Pt` -/

namespace NModel
open Model Manifold Kruskal ContinuousLinearMap

/-- `M = φ⁻¹{UV < 1}`: the Kruskal domain `r > 0` on `Pt`. -/
def sk_MN : Set Pt := φ ⁻¹' sk_kM

lemma sk_MN_open : IsOpen sk_MN := sk_kM_open.preimage φ_continuous

/-- `r : Pt → ℝ`, `r = rK ∘ φ`. -/
noncomputable def sk_r (M : ℝ) (x : Pt) : ℝ := rK M (φ x)

open Classical in
/-- **`F̃`**: Schwarzschild's `F ∘ φ` on `M`, extended by `1` off `M` (positive everywhere; only its
values on `M` enter `g` where it is Lorentzian, and only `M` enters the causal notions). -/
noncomputable def sk_F (M : ℝ) (x : Pt) : ℝ := if φ x ∈ sk_kM then FS M (φ x) else 1

variable {M : ℝ} (hM : 0 < M)

include hM in
lemma sk_F_pos (x : Pt) : 0 < sk_F M x := by
  unfold sk_F; split_ifs with h
  · exact sk_FS_pos hM h
  · exact one_pos

/-- `minkN` restricted to `M = {UV < 1}`. -/
noncomputable def sk_R : MSpacetime P Pt := minkN.restrictM sk_MN sk_MN_open (subset_univ _)

/-- **Schwarzschild in Kruskal's radial plane:** `M = {UV < 1}`, `g = F̃ · g_flat`. -/
noncomputable def sk_S : MSpacetime P Pt := sk_R.cz_scale (sk_F M) (sk_F_pos hM)

lemma sk_S_M : (sk_S hM).M = sk_MN := rfl

/-- **The metric in the global null chart:** `hRep g p₀ (U, V) = F(U, V) • gM`, i.e.
`g = −F(r(U, V)) dU dV` with `F = (32M³/r) e^{−r/2M}`, at every point of `{UV < 1}`. -/
theorem sk_hRep {y : P} (hy : y ∈ sk_kM) : hRep (sk_S hM).g p₀ y = FS M y • gM := by
  rw [sk_S, MSpacetime.cz_hRep_scale]
  have e : hRep sk_R.g p₀ y = gM := by
    show hRep minkN.g p₀ y = gM; rw [hRep_eq]
  rw [e]
  show sk_F M (ψ y) • gM = _
  rw [sk_F, show φ (ψ y) = y from φψ y, ite_eq_left hy]

theorem sk_hRep_apply {y : P} (hy : y ∈ sk_kM) (v w : P) :
    hRep (sk_S hM).g p₀ y v w = -FS M y * (v.1 * w.2 + v.2 * w.1) / 2 := by
  rw [sk_hRep hM hy, smul_apply, smul_apply, gM_apply,
    smul_eq_mul]
  ring

lemma sk_R_oneChart : sk_R.OneChart p₀ where
  sub := by rw [source_eq]; exact subset_univ _
  g_C1 := by
    show ContDiffOn ℝ 1 (hRep minkN.g p₀) _
    rw [hRep_eq]; exact contDiffOn_const
  T_cont := by
    show ContinuousOn (chartRep minkN.T p₀) _
    rw [chartRep_eq]; exact continuousOn_const

lemma sk_φ_image : extChartAt 𝓘(ℝ, P) p₀ '' sk_MN = sk_kM := by
  ext y; constructor
  · rintro ⟨x, hx, rfl⟩; exact hx
  · intro hy
    refine ⟨ψ y, ?_, φψ y⟩
    show φ (ψ y) ∈ sk_kM
    rwa [show φ (ψ y) = y from φψ y]

/-- **The chart spacetime of `sk_R` is the flat plane restricted to `{UV < 1}`.** -/
theorem sk_chartSp_eq : MSpacetime.chartSp sk_R_oneChart = sk_K := by
  refine Spacetime.ch_ext ?_ ?_ ?_
  · exact sk_φ_image
  · show hRep minkN.g p₀ = fun _ => gM; exact hRep_eq
  · show chartRep minkN.T p₀ = fun _ => ((1, 1) : P); exact chartRep_eq

/-- **`LocallyOneChart` for `sk_S` (BUILT)**, from `me_locallyOneChart` restricted to `M` and
`sk_scale_locallyOneChart` with `F` `C¹` on `{UV < 1}` (`sk_FS_contDiffOn`). -/
theorem sk_locallyOneChart : (sk_S hM).LocallyOneChart := by
  refine sk_R.sk_scale_locallyOneChart (sk_F_pos hM)
    (me_locallyOneChart.restrict sk_MN_open (subset_univ _)) fun p _ => ?_
  have hmaps : MapsTo (fun y => φ ((extChartAt 𝓘(ℝ, P) p).symm y))
      (extChartAt 𝓘(ℝ, P) p '' (sk_R.M ∩ (chartAt P p).source)) sk_kM := by
    rintro _ ⟨x, ⟨hxM, hxs⟩, rfl⟩
    show φ ((extChartAt 𝓘(ℝ, P) p).symm (extChartAt 𝓘(ℝ, P) p x)) ∈ sk_kM
    rw [ch_left_inv p hxs]; exact hxM
  refine ((sk_FS_contDiffOn hM).comp (cz_φ_symm_contDiff p).contDiffOn hmaps).congr ?_
  intro y hy
  show sk_F M _ = FS M (φ _)
  rw [sk_F, ite_eq_left (hmaps hy)]

/-- The observer on `Pt`. -/
noncomputable def sk_ON (a : ℝ) (σ : ℝ) : Pt := ψ (sk_O a σ)

lemma sk_image_ON (a : ℝ) : extChartAt 𝓘(ℝ, P) p₀ '' range (sk_ON a) = range (sk_O a) := by
  rw [show range (sk_ON a) = ψ '' range (sk_O a) from (range_comp ψ (sk_O a)), image_image]
  simp only [φψ, image_id']

lemma sk_chr_iff {x y : Pt} : (sk_S hM).Chr x y ↔ sk_K.Chr (φ x) (φ y) := by
  rw [sk_S, sk_R.cz_scale_chr, MSpacetime.ch_chr_iff sk_R_oneChart (src _) (src _),
    sk_chartSp_eq]; rfl

lemma sk_cau_iff {x y : Pt} : (sk_S hM).Cau x y ↔ sk_K.Cau (φ x) (φ y) := by
  rw [sk_S, sk_R.cz_scale_cau, MSpacetime.ch_cau_iff sk_R_oneChart (src _) (src _),
    sk_chartSp_eq]; rfl

lemma sk_mem_D_iff {a : ℝ} (x : Pt) :
    x ∈ (sk_S hM).D (range (sk_ON a)) ↔ φ x ∈ sk_K.D (range (sk_O a)) := by
  rw [sk_S, sk_R.cz_scale_D, MSpacetime.ch_mem_D_iff sk_R_oneChart (fun _ _ => src _) (src x),
    sk_chartSp_eq, sk_image_ON]; rfl

lemma sk_mem_H_iff {a : ℝ} (x : Pt) :
    x ∈ (sk_S hM).H (range (sk_ON a)) ↔ φ x ∈ sk_K.H (range (sk_O a)) := by
  rw [sk_S, sk_R.cz_scale_H, MSpacetime.ch_mem_H_iff sk_R_oneChart (fun _ _ => src _) (src x),
    sk_chartSp_eq, sk_image_ON]; rfl

/-- **The observer and its horizon on `sk_S` (BUILT, with the frontier read in `N = Pt`).**
For any `a > 0` (`O` on `UV = −a²`): `I⁻(O) = D = {U < 0} ∩ M` (regions I, IV); `O` is
future-timelike; `range O ⊆ M`; `𝓗⁺ = ∂J⁻(O) = {U = 0} ∪ {U < 0, UV = 1}`, whose part in `M`
is `{U = 0}` (non-empty, `⊆ M`), and `r = 2M` on `𝓗⁺ ∩ M`. -/
theorem sk_observer {a : ℝ} (ha : 0 < a) :
    (sk_S hM).IpastSet (range (sk_ON a)) = {x | (φ x).1 < 0} ∩ (sk_S hM).M ∧
    (sk_S hM).D (range (sk_ON a)) = {x | (φ x).1 < 0} ∩ (sk_S hM).M ∧
    (∀ s t : ℝ, s < t → (sk_S hM).Chr (sk_ON a s) (sk_ON a t)) ∧
    range (sk_ON a) ⊆ (sk_S hM).M ∧
    (sk_S hM).H (range (sk_ON a)) =
      {x | (φ x).1 = 0} ∪ {x | (φ x).1 < 0 ∧ (φ x).1 * (φ x).2 = 1} ∧
    (sk_S hM).H (range (sk_ON a)) ∩ (sk_S hM).M = {x | (φ x).1 = 0} ∧
    {x : Pt | (φ x).1 = 0} ⊆ (sk_S hM).M ∧ {x : Pt | (φ x).1 = 0}.Nonempty ∧
    (∀ x ∈ (sk_S hM).H (range (sk_ON a)), x ∈ (sk_S hM).M → sk_r M x = 2 * M) := by
  have hD : (sk_S hM).D (range (sk_ON a)) = {x | (φ x).1 < 0} ∩ (sk_S hM).M := by
    ext x; rw [sk_mem_D_iff, sk_K_D ha]; rfl
  have hH : (sk_S hM).H (range (sk_ON a)) =
      {x | (φ x).1 = 0} ∪ {x | (φ x).1 < 0 ∧ (φ x).1 * (φ x).2 = 1} := by
    ext x; rw [sk_mem_H_iff, sk_K_H ha]; rfl
  have hU0 : {x : Pt | (φ x).1 = 0} ⊆ (sk_S hM).M := fun x hx => by
    show (φ x).1 * (φ x).2 < 1
    rw [show (φ x).1 = 0 from hx]; norm_num
  have hHM : (sk_S hM).H (range (sk_ON a)) ∩ (sk_S hM).M = {x | (φ x).1 = 0} := by
    rw [hH]
    ext x
    simp only [mem_inter_iff, mem_union, mem_ofPred_eq]
    constructor
    · rintro ⟨h | ⟨-, h2⟩, hxM⟩
      · exact h
      · exfalso
        have : (φ x).1 * (φ x).2 < 1 := hxM
        linarith
    · intro h; exact ⟨Or.inl h, hU0 h⟩
  refine ⟨hD, hD, fun s t hst => ?_, ?_, hH, hHM, hU0, ⟨ψ (0, 0), ?_⟩, fun x hx hxM => ?_⟩
  · rw [sk_chr_iff]
    show sk_K.Chr (φ (ψ (sk_O a s))) (φ (ψ (sk_O a t)))
    rw [show φ (ψ (sk_O a s)) = sk_O a s from φψ _, show φ (ψ (sk_O a t)) = sk_O a t from φψ _]
    exact Relation.TransGen.single (sk_K_tstep_of_lt (sk_O_mem a s) (sk_O_mem a t)
      (sk_O_mono ha hst).1 (sk_O_mono ha hst).2)
  · rintro _ ⟨σ, rfl⟩
    show φ (ψ (sk_O a σ)) ∈ sk_kM
    rw [show φ (ψ (sk_O a σ)) = sk_O a σ from φψ _]; exact sk_O_mem a σ
  · show (φ (ψ (0, 0))).1 = 0
    rw [show φ (ψ (0, 0)) = (0, 0) from φψ _]
  · have h0 : (φ x).1 = 0 := by
      have : x ∈ (sk_S hM).H (range (sk_ON a)) ∩ (sk_S hM).M := ⟨hx, hxM⟩
      rw [hHM] at this; exact this
    exact (sk_rK_eq_two_iff hM (p := φ x) hxM).2 (by rw [h0, zero_mul])

/-- **The static observer at `r₀ > 2M`** (BUILT): `a = √c`, `c = h(r₀) = (r₀/2M − 1)e^{r₀/2M} > 0`;
`O(σ) = φ⁻¹(−a e^{−σ}, a e^{σ})` lies on `UV = −c`, at `r = r₀`, and every clause of
`sk_observer` holds for it. -/
theorem sk_static_observer {r₀ : ℝ} (hr₀ : 2 * M < r₀) :
    0 < hK M r₀ ∧
    (∀ σ, (φ (sk_ON (Real.sqrt (hK M r₀)) σ)).1 * (φ (sk_ON (Real.sqrt (hK M r₀)) σ)).2 =
      -hK M r₀) ∧
    (∀ σ, sk_r M (sk_ON (Real.sqrt (hK M r₀)) σ) = r₀) ∧
    (sk_S hM).IpastSet (range (sk_ON (Real.sqrt (hK M r₀)))) =
      {x | (φ x).1 < 0} ∩ (sk_S hM).M ∧
    (∀ s t : ℝ, s < t → (sk_S hM).Chr (sk_ON (Real.sqrt (hK M r₀)) s)
      (sk_ON (Real.sqrt (hK M r₀)) t)) ∧
    range (sk_ON (Real.sqrt (hK M r₀))) ⊆ (sk_S hM).M ∧
    (sk_S hM).H (range (sk_ON (Real.sqrt (hK M r₀)))) ∩ (sk_S hM).M = {x | (φ x).1 = 0} ∧
    (∀ x ∈ (sk_S hM).H (range (sk_ON (Real.sqrt (hK M r₀)))), x ∈ (sk_S hM).M →
      sk_r M x = 2 * M) := by
  have hc : 0 < hK M r₀ := by
    rw [← hK_two hM]
    exact hK_strictMonoOn hM (mem_Ici.2 (by positivity)) (mem_Ici.2 (by linarith)) hr₀
  have ha : 0 < Real.sqrt (hK M r₀) := Real.sqrt_pos.2 hc
  have hUV : ∀ σ, (φ (sk_ON (Real.sqrt (hK M r₀)) σ)).1 * (φ (sk_ON (Real.sqrt (hK M r₀)) σ)).2 =
      -hK M r₀ := fun σ => by
    show (φ (ψ _)).1 * (φ (ψ _)).2 = _
    rw [show ∀ y, φ (ψ y) = y from φψ, sk_O_UV, Real.sq_sqrt hc.le]
  obtain ⟨h1, -, h3, h4, -, h6, -, -, h9⟩ := sk_observer hM ha
  refine ⟨hc, hUV, fun σ => ?_, h1, h3, h4, h6, h9⟩
  show rinv M (-((φ _).1 * (φ _).2)) = r₀
  rw [hUV, neg_neg, rinv_hK hM (by linarith)]

/-- **3a, `sk_cor_EF_events` (BUILT).** For `0 < V₁ < V₂`, `p = φ⁻¹(0, V₁)`, `q = φ⁻¹(0, V₂)` on the
future horizon branch `U = 0, V > 0`: both lie on `∂J⁻(O)` and in `M`, `p ≠ q`, `p ≤ q`, `¬ p ≪ q`
(null-related), and both are at `r = 2M`. -/
theorem sk_cor_EF_events {a : ℝ} (ha : 0 < a) {V₁ V₂ : ℝ} (_h1 : 0 < V₁) (h12 : V₁ < V₂) :
    ψ (0, V₁) ∈ (sk_S hM).H (range (sk_ON a)) ∧ ψ (0, V₂) ∈ (sk_S hM).H (range (sk_ON a)) ∧
    ψ (0, V₁) ∈ (sk_S hM).M ∧ ψ (0, V₂) ∈ (sk_S hM).M ∧
    ψ (0, V₁) ≠ ψ (0, V₂) ∧
    (sk_S hM).Cau (ψ (0, V₁)) (ψ (0, V₂)) ∧ ¬ (sk_S hM).Chr (ψ (0, V₁)) (ψ (0, V₂)) ∧
    sk_r M (ψ (0, V₁)) = 2 * M ∧ sk_r M (ψ (0, V₂)) = 2 * M := by
  obtain ⟨-, -, -, -, hH, -, hU0, -, hr⟩ := sk_observer hM ha
  have e : ∀ y, φ (ψ y) = y := φψ
  have hmem : ∀ V : ℝ, ψ (0, V) ∈ (sk_S hM).H (range (sk_ON a)) := fun V => by
    rw [hH]; left; show (φ (ψ (0, V))).1 = 0; rw [e]
  have hM' : ∀ V : ℝ, ψ (0, V) ∈ (sk_S hM).M := fun V => hU0 (by show (φ (ψ (0, V))).1 = 0; rw [e])
  have hk : ∀ V : ℝ, ((0 : ℝ), V) ∈ sk_kM := fun V => by
    show (0:ℝ) * V < 1; norm_num
  refine ⟨hmem V₁, hmem V₂, hM' V₁, hM' V₂, fun h => ?_, ?_, fun h => ?_,
    hr _ (hmem V₁) (hM' V₁), hr _ (hmem V₂) (hM' V₂)⟩
  · have := congrArg (fun x => (φ x).2) h
    simp only [e] at this
    linarith
  · rw [sk_cau_iff, e, e]
    exact Relation.ReflTransGen.single
      (sk_K_cstep_of_le (hk V₁) (hk V₂) le_rfl h12.le (by simpa using h12))
  · rw [sk_chr_iff, e, e] at h
    exact lt_irrefl _ (chr_lt (sk_K_chr_mink h)).1

/-- **Non-vacuity (BUILT):** at `M = 1`, `r₀ = 4` (`c = e²`), `V₁ = 1`, `V₂ = 2`, every clause of
3a holds, and `g ≠ g_flat` at `φ⁻¹(0,0)` (`F = 16/e ≠ 1`); `F` is non-constant. -/
theorem sk_nonvacuous :
    0 < hK 1 4 ∧
    ψ (0, 1) ∈ (sk_S one_pos).H (range (sk_ON (Real.sqrt (hK 1 4)))) ∧
    (sk_S one_pos).Cau (ψ (0, 1)) (ψ (0, 2)) ∧ ¬ (sk_S one_pos).Chr (ψ (0, 1)) (ψ (0, 2)) ∧
    ψ (0, (1:ℝ)) ≠ ψ (0, 2) ∧ sk_r 1 (ψ (0, 1)) = 2 * 1 ∧
    hRep (sk_S one_pos).g p₀ (0, 0) ≠ hRep minkN.g p₀ (0, 0) ∧
    FS 1 (0, 0) ≠ FS 1 (-1, -hK 1 (4 * 1) / (-1)) := by
  obtain ⟨hc, -⟩ := sk_static_observer one_pos (r₀ := 4) (by norm_num)
  have ha : 0 < Real.sqrt (hK 1 4) := Real.sqrt_pos.2 hc
  obtain ⟨h1, -, -, -, hne, hcau, hchr, hr1, -⟩ :=
    sk_cor_EF_events one_pos ha (V₁ := 1) (V₂ := 2) one_pos (by norm_num)
  obtain ⟨e0, -, hnc⟩ := sk_FS_nonconst one_pos
  refine ⟨hc, h1, hcau, hchr, hne, hr1, fun h => ?_, hnc⟩
  rw [sk_hRep one_pos (show ((0:ℝ), (0:ℝ)) ∈ sk_kM by show (0:ℝ) * 0 < 1; norm_num), hRep_eq,
    e0] at h
  have h2 := congrArg (fun B : P →L[ℝ] P →L[ℝ] ℝ => B (1, 1) (1, 1)) h
  simp only [smul_apply, gM_apply, smul_eq_mul] at h2
  have hm : Real.exp (-1) * Real.exp 1 = 1 := by rw [← Real.exp_add]; norm_num
  have := Real.exp_one_lt_d9
  nlinarith [Real.exp_pos (-1)]

end NModel

/-! ## NEW (campaign 98 ①②, `r7677+71`): Schwarzschild on EF's domain `W = {V > 0, UV < 1}`

`N = W` is the open subset `{V > 0, UV < 1}` of the null plane `P = ℝ²`, as a manifold through
Mathlib's `TopologicalSpace.Opens` charted structure (one chart, the inclusion `W ↪ P`). The metric
is `g = F · (−dU dV)`, `F = (32M³/r) e^{−r/2M}` (campaign 97's `FS`), `T = ∂_U + ∂_V`, `M = W`.
Every new name has the prefix `se_`. -/

namespace Spacetime

/-! ### Two chart spacetimes that agree on `M` have the same causal structure -/

/-- `S` and `S'` agree: same `M`, and the same `g`, `T` at points of `M`. -/
def SeAgree (S S' : Spacetime V) : Prop :=
  S.M = S'.M ∧ ∀ x ∈ S.M, S.g x = S'.g x ∧ S.T x = S'.T x

variable {S S' S'' : Spacetime V}

lemma SeAgree.mem (h : S.SeAgree S') {x : V} : x ∈ S.M ↔ x ∈ S'.M := by rw [h.1]

lemma SeAgree.symm (h : S.SeAgree S') : S'.SeAgree S :=
  ⟨h.1.symm, fun x hx => ⟨(h.2 x (h.mem.2 hx)).1.symm, (h.2 x (h.mem.2 hx)).2.symm⟩⟩

lemma SeAgree.trans (h : S.SeAgree S') (h' : S'.SeAgree S'') : S.SeAgree S'' :=
  ⟨h.1.trans h'.1, fun x hx => ⟨(h.2 x hx).1.trans (h'.2 x (h.mem.1 hx)).1,
    (h.2 x hx).2.trans (h'.2 x (h.mem.1 hx)).2⟩⟩

lemma SeAgree.futTimelike (h : S.SeAgree S') {x : V} (hx : x ∈ S.M) (v : V) :
    S.FutTimelike x v ↔ S'.FutTimelike x v := by
  unfold FutTimelike; rw [(h.2 x hx).1, (h.2 x hx).2]

lemma SeAgree.futCausal (h : S.SeAgree S') {x : V} (hx : x ∈ S.M) (v : V) :
    S.FutCausal x v ↔ S'.FutCausal x v := by
  unfold FutCausal; rw [(h.2 x hx).1, (h.2 x hx).2]

lemma SeAgree.tstep (h : S.SeAgree S') {x y : V} (hxy : S.TStep x y) : S'.TStep x y := by
  obtain ⟨γ, hγ, h0, h1, ht⟩ := hxy
  exact ⟨γ, hγ, h0, h1, fun t htI =>
    ⟨h.mem.1 (ht t htI).1, (h.futTimelike (ht t htI).1 _).1 (ht t htI).2⟩⟩

lemma SeAgree.cstep (h : S.SeAgree S') {x y : V} (hxy : S.CStep x y) : S'.CStep x y := by
  obtain ⟨γ, hγ, h0, h1, ht⟩ := hxy
  exact ⟨γ, hγ, h0, h1, fun t htI =>
    ⟨h.mem.1 (ht t htI).1, (h.futCausal (ht t htI).1 _).1 (ht t htI).2⟩⟩

lemma SeAgree.chr (h : S.SeAgree S') {x y : V} (hxy : S.Chr x y) : S'.Chr x y := by
  induction hxy with
  | single h' => exact Relation.TransGen.single (h.tstep h')
  | tail _ h' ih => exact ih.tail (h.tstep h')

lemma SeAgree.cau (h : S.SeAgree S') {x y : V} (hxy : S.Cau x y) : S'.Cau x y := by
  induction hxy with
  | refl => exact Relation.ReflTransGen.refl
  | tail _ h' ih => exact ih.tail (h.cstep h')

lemma SeAgree.chr_iff (h : S.SeAgree S') {x y : V} : S.Chr x y ↔ S'.Chr x y :=
  ⟨h.chr, h.symm.chr⟩

lemma SeAgree.cau_iff (h : S.SeAgree S') {x y : V} : S.Cau x y ↔ S'.Cau x y :=
  ⟨h.cau, h.symm.cau⟩

lemma SeAgree.D_eq (h : S.SeAgree S') (J : Set V) : S.D J = S'.D J := by
  ext x
  simp only [D, IpastSet, Ipast, mem_iUnion, mem_ofPred_eq, h.chr_iff]

lemma SeAgree.JpastSet_eq (h : S.SeAgree S') (J : Set V) : S.JpastSet J = S'.JpastSet J := by
  ext x
  simp only [JpastSet, Jpast, mem_iUnion, mem_ofPred_eq, h.cau_iff]

lemma SeAgree.H_eq (h : S.SeAgree S') (J : Set V) : S.H J = S'.H J := by
  rw [H, H, h.JpastSet_eq]

lemma SeAgree.Dsp (h : S.SeAgree S') (J : Set V) : (S.Dsp J).SeAgree (S'.Dsp J) :=
  ⟨h.D_eq J, fun x hx => h.2 x (S.hl_D_subset_M J hx)⟩

/-- **The Cauchy property passes between agreeing spacetimes.** -/
theorem SeAgree.isCauchyTemporal (h : S.SeAgree S') {Θ : V → ℝ} (hΘ : S.IsCauchyTemporal Θ) :
    S'.IsCauchyTemporal Θ := by
  refine ⟨⟨h.1 ▸ hΘ.1.1, fun x hx v hv =>
    hΘ.1.2 x (h.mem.2 hx) v ((h.futCausal (h.mem.2 hx) v).2 hv)⟩, fun c a => ?_⟩
  exact hΘ.2 ⟨c.γ, c.cont, fun t => h.mem.2 (c.mem t), c.brk, c.brk_fin,
    fun t ht => ⟨(c.causal t ht).1, (h.futCausal (h.mem.2 (c.mem t)) _).2 (c.causal t ht).2⟩,
    fun ⟨p, hp, hl⟩ => c.inext_future ⟨p, h.mem.1 hp, hl⟩,
    fun ⟨p, hp, hl⟩ => c.inext_past ⟨p, h.mem.1 hp, hl⟩⟩ a

end Spacetime

/-! ### ② on the plane: `t` is Cauchy on region I, through the relabelling `ψ(U,V) = (U, log V)` -/

namespace Model
open Kruskal ContinuousLinearMap

/-- **Region I** in Kruskal's null coordinates: `{U < 0, V > 0}`. -/
def seR : Set P := {p | p.1 < 0 ∧ 0 < p.2}

lemma seR_open : IsOpen seR :=
  (isOpen_lt continuous_fst continuous_const).inter (isOpen_lt continuous_const continuous_snd)

/-- The flat plane restricted to region I. -/
noncomputable def se_RI : Spacetime P := mink.restrict seR seR_open (subset_univ _)

/-- **The relabelling** `ψ(U, V) = (U, log V)`: region I `≅ {U < 0} × ℝ`, order-preserving in each
null coordinate. -/
noncomputable def seψ (p : P) : P := (p.1, Real.log p.2)

/-- Its inverse `(U, s) ↦ (U, e^s)`. -/
noncomputable def seψinv (q : P) : P := (q.1, Real.exp q.2)

lemma seψinv_continuous : Continuous seψinv := by unfold seψinv; fun_prop

lemma seψinv_seψ {p : P} (hp : 0 < p.2) : seψinv (seψ p) = p := by
  simp only [seψinv, seψ, Real.exp_log hp]

/-- **`Θ_k(U, V) = k (log V − log(−U))`**: with `k = 2M √(1 − 2M/r₀)`, this is
`√(1 − 2M/r₀) · t`, `t = 2M log(−V/U)` the Schwarzschild time. -/
noncomputable def seΘP (k : ℝ) (p : P) : ℝ := k * (Real.log p.2 - Real.log (-p.1))

/-- `Θ_k = k · Θ₀ ∘ ψ`: the `V`-term of `Θ₀ = −log(−U) + V` becomes `log V`. -/
lemma seΘP_eq (k : ℝ) (p : P) : seΘP k p = k * Θ₀ (seψ p) := by
  simp only [seΘP, Θ₀, ThetaG, seψ]; ring

lemma seΘP_hasFDerivAt (k : ℝ) {p : P} (hp : p ∈ seR) :
    HasFDerivAt (seΘP k)
      (k • ((p.2)⁻¹ • snd ℝ ℝ ℝ - (-p.1)⁻¹ • (-fst ℝ ℝ ℝ))) p := by
  have h2 : HasFDerivAt (fun q : P => Real.log q.2) ((p.2)⁻¹ • snd ℝ ℝ ℝ) p :=
    (hasFDerivAt_snd).log hp.2.ne'
  have h1 : HasFDerivAt (fun q : P => Real.log (-q.1)) ((-p.1)⁻¹ • (-fst ℝ ℝ ℝ)) p :=
    (hasFDerivAt_fst.neg).log (show -p.1 ≠ 0 from neg_ne_zero.2 hp.1.ne)
  exact (h2.sub h1).const_mul k

/-- **`Θ_k` is temporal on region I** (`k > 0`): `dΘ_k(v) = k (v_V/V + v_U/(−U)) > 0` on future
causal `v`. -/
theorem se_temporal_RI {k : ℝ} (hk : 0 < k) : se_RI.IsTemporal (seΘP k) := by
  refine ⟨fun p hp => ?_, fun p hp v hv => ?_⟩
  · have hp' : p ∈ seR := hp
    have h1 : -p.1 ≠ 0 := by have := hp'.1; linarith
    refine ContDiffAt.contDiffWithinAt ?_
    unfold seΘP
    exact contDiffAt_const.mul ((contDiffAt_snd.log hp'.2.ne').sub (contDiffAt_fst.neg.log h1))
  · have hp' : p ∈ seR := hp
    have hv' : mink.FutCausal p v := hv
    rw [futCausal_iff] at hv'
    obtain ⟨hv1, hv2, hv3⟩ := hv'
    rw [(seΘP_hasFDerivAt k hp').fderiv]
    simp only [smul_apply, sub_apply, neg_apply, smul_eq_mul]
    change 0 < k * ((p.2)⁻¹ * v.2 - (-p.1)⁻¹ * -v.1)
    have ha : 0 < (-p.1)⁻¹ := inv_pos.2 (by linarith [hp'.1])
    have hb : 0 < (p.2)⁻¹ := inv_pos.2 hp'.2
    have hpos : 0 < (p.2)⁻¹ * v.2 + (-p.1)⁻¹ * v.1 := by
      rcases hv1.lt_or_eq with h | h
      · nlinarith [mul_pos ha h, mul_nonneg hb.le hv2]
      · rw [← h] at hv3
        nlinarith [mul_pos hb (show 0 < v.2 by linarith)]
    have : (p.2)⁻¹ * v.2 - (-p.1)⁻¹ * -v.1 = (p.2)⁻¹ * v.2 + (-p.1)⁻¹ * v.1 := by ring
    rw [this]; exact mul_pos hk hpos

/-- **② on the plane (BUILT): `Θ_k` is Cauchy temporal on region I.** Every inextendible causal
curve `γ` of region I is carried by `ψ` to one of `{U < 0}` (`ψ` preserves future causality and,
with its continuous inverse, inextendibility), where campaign 81's `hl_cauchy_Θ₀` applies, and
`Θ_k ∘ γ = k · Θ₀ ∘ (ψ ∘ γ)`. -/
theorem se_cauchy_RI {k : ℝ} (hk : 0 < k) : se_RI.IsCauchyTemporal (seΘP k) := by
  refine ⟨se_temporal_RI hk, fun c a => ?_⟩
  have hmem : ∀ t, (c.γ t).1 < 0 ∧ 0 < (c.γ t).2 := c.mem
  have hcont2 : Continuous fun t => (c.γ t).2 := continuous_snd.comp c.cont
  have hback : ∀ q : P, q.1 < 0 → Filter.Tendsto (fun t => seψ (c.γ t)) Filter.atTop (𝓝 q) →
      Filter.Tendsto c.γ Filter.atTop (𝓝 (seψinv q)) := fun q _ hl => by
    have := (seψinv_continuous.tendsto q).comp hl
    refine this.congr fun t => ?_
    exact seψinv_seψ (hmem t).2
  have hback' : ∀ q : P, q.1 < 0 → Filter.Tendsto (fun t => seψ (c.γ t)) Filter.atBot (𝓝 q) →
      Filter.Tendsto c.γ Filter.atBot (𝓝 (seψinv q)) := fun q _ hl => by
    have := (seψinv_continuous.tendsto q).comp hl
    refine this.congr fun t => ?_
    exact seψinv_seψ (hmem t).2
  have hR : ∀ q : P, q.1 < 0 → seψinv q ∈ se_RI.M := fun q hq => ⟨hq, Real.exp_pos _⟩
  let c' : (mink.Dsp (range O)).InextCausalCurve :=
    { γ := fun t => seψ (c.γ t)
      cont := (continuous_fst.comp c.cont).prodMk (hcont2.log fun t => (hmem t).2.ne')
      mem := fun t => by
        show seψ (c.γ t) ∈ mink.D (range O)
        rw [hl_D_eq]; exact (hmem t).1
      brk := c.brk
      brk_fin := c.brk_fin
      causal := fun t ht => by
        obtain ⟨hd, hfc⟩ := c.causal t ht
        have hfc' : mink.FutCausal (c.γ t) (deriv c.γ t) := hfc
        rw [futCausal_iff] at hfc'
        have h1 : HasDerivAt (fun s => (c.γ s).1) (deriv c.γ t).1 t :=
          hasDerivAt_lin (fst ℝ ℝ ℝ) hd
        have h2 : HasDerivAt (fun s => (c.γ s).2) (deriv c.γ t).2 t :=
          hasDerivAt_lin (snd ℝ ℝ ℝ) hd
        have hpr : HasDerivAt (fun s => seψ (c.γ s))
            ((deriv c.γ t).1, (deriv c.γ t).2 / (c.γ t).2) t :=
          h1.prodMk (h2.log (hmem t).2.ne')
        refine ⟨hpr.differentiableAt, ?_⟩
        show mink.FutCausal (seψ (c.γ t)) (deriv (fun s => seψ (c.γ s)) t)
        rw [hpr.deriv, futCausal_iff]
        obtain ⟨hv1, hv2, hv3⟩ := hfc'
        have hV := (hmem t).2
        refine ⟨hv1, div_nonneg hv2 hV.le, ?_⟩
        rcases hv1.lt_or_eq with h | h
        · simp only; positivity
        · simp only; rw [← h] at hv3 ⊢; simp only [zero_add] at hv3 ⊢
          exact div_pos hv3 hV
      inext_future := by
        rintro ⟨q, hq, hl⟩
        change q ∈ mink.D (range O) at hq
        rw [hl_D_eq] at hq
        exact c.inext_future ⟨seψinv q, hR q hq, hback q hq hl⟩
      inext_past := by
        rintro ⟨q, hq, hl⟩
        change q ∈ mink.D (range O) at hq
        rw [hl_D_eq] at hq
        exact c.inext_past ⟨seψinv q, hR q hq, hback' q hq hl⟩ }
  have e : ∀ t, seΘP k (c.γ t) = a ↔ Θ₀ (c'.γ t) = a / k := fun t => by
    rw [seΘP_eq, eq_div_iff hk.ne', mul_comm]
  obtain ⟨t, ht, huniq⟩ := hl_cauchy_Θ₀.2 c' (a / k)
  exact ⟨t, (e t).2 ht, fun s hs => huniq s ((e s).1 hs)⟩

/-! ### The flat plane on `W` -/

/-- **EF's domain** `W = {V > 0, UV < 1}` (regions I and II). -/
def seWS : Set P := {p | 0 < p.2 ∧ p.1 * p.2 < 1}

lemma seWS_open : IsOpen seWS :=
  (isOpen_lt continuous_const continuous_snd).inter
    (isOpen_lt (continuous_fst.mul continuous_snd) continuous_const)

lemma seWS_kM {p : P} (hp : p ∈ seWS) : p ∈ sk_kM := hp.2

lemma seR_subset_WS : seR ⊆ seWS := fun p hp =>
  ⟨hp.2, by have := mul_neg_of_neg_of_pos hp.1 hp.2; linarith⟩

/-- `mink` restricted to `W`. -/
noncomputable def seK : Spacetime P := mink.restrict seWS seWS_open (subset_univ _)

lemma seK_tstep_mink {x y : P} (h : seK.TStep x y) : mink.TStep x y := by
  obtain ⟨γ, hγ, h0, h1, ht⟩ := h
  exact ⟨γ, hγ, h0, h1, fun t htI => ⟨mem_univ _, (ht t htI).2⟩⟩

lemma seK_cstep_mink {x y : P} (h : seK.CStep x y) : mink.CStep x y := by
  obtain ⟨γ, hγ, h0, h1, ht⟩ := h
  exact ⟨γ, hγ, h0, h1, fun t htI => ⟨mem_univ _, (ht t htI).2⟩⟩

lemma seK_chr_mink {x y : P} (h : seK.Chr x y) : mink.Chr x y := by
  induction h with
  | single h => exact Relation.TransGen.single (seK_tstep_mink h)
  | tail _ h ih => exact ih.tail (seK_tstep_mink h)

lemma seK_cau_mink {x y : P} (h : seK.Cau x y) : mink.Cau x y := by
  induction h with
  | refl => exact Relation.ReflTransGen.refl
  | tail _ h ih => exact ih.tail (seK_cstep_mink h)

/-- **Straight segments with `U`, `V` non-decreasing stay in `W`**: `V > 0` is preserved, and
`UV < 1` by campaign 97's `sk_seg_mem`. -/
lemma se_seg_mem {x y : P} (hx : x ∈ seWS) (hy : y ∈ seWS) (h1 : x.1 ≤ y.1) (h2 : x.2 ≤ y.2)
    {t : ℝ} (ht : t ∈ Icc (0:ℝ) 1) : x + t • (y - x) ∈ seWS := by
  refine ⟨?_, sk_seg_mem hx.2 hy.2 h1 h2 ht⟩
  show 0 < (x + t • (y - x)).2
  simp only [Prod.snd_add, Prod.smul_snd, Prod.snd_sub, smul_eq_mul]
  have := hx.1
  nlinarith [mul_nonneg ht.1 (sub_nonneg.2 h2)]

lemma seK_tstep_of_lt {x y : P} (hx : x ∈ seWS) (hy : y ∈ seWS) (h1 : x.1 < y.1)
    (h2 : x.2 < y.2) : seK.TStep x y := by
  refine ⟨fun t => x + t • (y - x), contDiff_const.add (contDiff_id.smul contDiff_const),
    by simp, by simp, fun t ht => ⟨se_seg_mem hx hy h1.le h2.le ht, ?_⟩⟩
  show mink.FutTimelike (x + t • (y - x)) (deriv (fun t : ℝ => x + t • (y - x)) t)
  rw [sk_deriv_seg, futTimelike_iff]
  simp only [Prod.fst_sub, Prod.snd_sub, sub_pos]
  exact ⟨h1, h2⟩

lemma seK_cstep_of_le {x y : P} (hx : x ∈ seWS) (hy : y ∈ seWS) (h1 : x.1 ≤ y.1)
    (h2 : x.2 ≤ y.2) (h3 : x.1 + x.2 < y.1 + y.2) : seK.CStep x y := by
  refine ⟨fun t => x + t • (y - x), contDiff_const.add (contDiff_id.smul contDiff_const),
    by simp, by simp, fun t ht => ⟨se_seg_mem hx hy h1 h2 ht, ?_⟩⟩
  show mink.FutCausal (x + t • (y - x)) (deriv (fun t : ℝ => x + t • (y - x)) t)
  rw [sk_deriv_seg, futCausal_iff]
  simp only [Prod.fst_sub, Prod.snd_sub, sub_nonneg]
  exact ⟨h1, h2, by linarith⟩

/-- **`≪` inside `W` is the flat relation restricted to `W`.** -/
theorem se_K_chr_iff {x y : P} (hx : x ∈ seWS) (hy : y ∈ seWS) :
    seK.Chr x y ↔ x.1 < y.1 ∧ x.2 < y.2 :=
  ⟨fun h => chr_lt (seK_chr_mink h),
    fun h => Relation.TransGen.single (seK_tstep_of_lt hx hy h.1 h.2)⟩

lemma sk_O_memW {a : ℝ} (ha : 0 < a) (σ : ℝ) : sk_O a σ ∈ seWS :=
  ⟨mul_pos ha (Real.exp_pos σ), sk_O_mem a σ⟩

/-- **`D = I⁻(O) = {U < 0, V > 0}`, region I** (the exterior `r > 2M`). -/
theorem se_K_D {a : ℝ} (ha : 0 < a) : seK.D (range (sk_O a)) = seR := by
  ext p
  constructor
  · intro hp
    have hpM : p ∈ seWS := seK.hl_D_subset_M _ hp
    obtain ⟨_, ⟨σ, rfl⟩, h⟩ := mem_iUnion₂.1 hp
    have h1 := (chr_lt (seK_chr_mink h)).1
    have h2 : 0 < a * Real.exp (-σ) := mul_pos ha (Real.exp_pos _)
    simp only [sk_O] at h1
    exact ⟨by linarith, hpM.1⟩
  · rintro hp
    have hpM := seR_subset_WS hp
    have e1 : ∀ᶠ σ in atTop, a * Real.exp (-σ) < -p.1 := by
      have h := Real.tendsto_exp_neg_atTop_nhds_zero.const_mul a
      rw [mul_zero] at h
      exact (tendsto_order.1 h).2 _ (by linarith [hp.1])
    have e2 : ∀ᶠ σ in atTop, p.2 < a * Real.exp σ :=
      (Real.tendsto_exp_atTop.const_mul_atTop ha).eventually_gt_atTop p.2
    obtain ⟨σ, h1, h2⟩ := (e1.and e2).exists
    exact mem_iUnion₂.2 ⟨sk_O a σ, mem_range_self σ, Relation.TransGen.single
      (seK_tstep_of_lt hpM (sk_O_memW ha σ) (by simp only [sk_O]; linarith) h2)⟩

/-- `J⁻(O) = {U < 0, V > 0}` too. -/
theorem se_K_JpastSet {a : ℝ} (ha : 0 < a) : seK.JpastSet (range (sk_O a)) = seR := by
  apply Subset.antisymm
  · intro p hp
    obtain ⟨_, ⟨σ, rfl⟩, h⟩ := mem_iUnion₂.1 hp
    have h1 := (cau_le (seK_cau_mink h)).1
    have h2 : 0 < a * Real.exp (-σ) := mul_pos ha (Real.exp_pos _)
    have hpM : p ∈ seWS := by
      rcases Relation.ReflTransGen.cases_head h with h | ⟨b, hb, -⟩
      · rw [h]; exact sk_O_memW ha σ
      · exact (seK.ch_cstep_mem hb).1
    simp only [sk_O] at h1
    exact ⟨by linarith, hpM.1⟩
  · rw [← se_K_D ha]
    intro p hp
    obtain ⟨z, hz, h⟩ := mem_iUnion₂.1 hp
    exact mem_iUnion₂.2 ⟨z, hz, seK.hl_chr_cau h⟩

/-- **`𝓗⁺ ∩ W = {U = 0, V > 0}`** in the plane. -/
theorem se_K_H {a : ℝ} (ha : 0 < a) {y : P} (hy : y ∈ seWS) :
    y ∈ seK.H (range (sk_O a)) ↔ y.1 = 0 := by
  rw [Spacetime.H, se_K_JpastSet ha, seR_open.frontier_eq]
  have hcl : closure seR ⊆ {p : P | p.1 ≤ 0} :=
    closure_minimal (fun p hp => le_of_lt hp.1) (isClosed_le continuous_fst continuous_const)
  constructor
  · rintro ⟨h1, h2⟩
    have h3 : y.1 ≤ 0 := hcl h1
    rcases h3.lt_or_eq with h | h
    · exact absurd ⟨h, hy.1⟩ h2
    · exact h
  · intro h0
    refine ⟨?_, fun h => by have h' := h.1; rw [h0] at h'; exact lt_irrefl _ h'⟩
    have hf : Tendsto (fun ε : ℝ => ((y.1 - ε, y.2) : P)) (𝓝[>] 0) (𝓝 y) := by
      have hc : Continuous (fun ε : ℝ => ((y.1 - ε, y.2) : P)) := by fun_prop
      simpa using (hc.tendsto 0).mono_left nhdsWithin_le_nhds
    refine mem_closure_of_tendsto hf ?_
    filter_upwards [self_mem_nhdsWithin] with ε hε
    have : (0:ℝ) < ε := hε
    exact ⟨by show y.1 - ε < 0; linarith, hy.1⟩

end Model

/-! ### ① The manifold `N = W` (Mathlib's `Opens` charted structure) -/

namespace SEModel
open Model Kruskal Manifold ContinuousLinearMap TopologicalSpace

/-- **`W = {V > 0, UV < 1}` as an open subset of the plane**; its type `↥seW` is the manifold `N`,
with Mathlib's `Opens.instChartedSpace` and the open-subset `IsManifold` instance. -/
def seW : Opens P := ⟨seWS, seWS_open⟩

example : IsManifold 𝓘(ℝ, P) 1 seW := inferInstance
example : T2Space seW := inferInstance

/-- The single chart is the inclusion `W ↪ P`, whatever the base point. -/
lemma se_ext_apply (p z : seW) : extChartAt 𝓘(ℝ, P) p z = (z : P) := rfl

lemma se_src (p z : seW) : z ∈ (chartAt P p).source := by
  simp [Opens.chartAt_eq]

lemma se_symm_apply (p : seW) {y : P} (hy : y ∈ seWS) :
    (extChartAt 𝓘(ℝ, P) p).symm y = ⟨y, hy⟩ :=
  (extChartAt 𝓘(ℝ, P) p).left_inv (x := (⟨y, hy⟩ : seW))
    (by rw [extChartAt_source]; exact se_src p _)

/-- **`D(chart) = id`**: tangent vectors on `W` are read in the plane's own coordinates. -/
lemma se_dchart (p x : seW) (v : P) :
    mfderiv 𝓘(ℝ, P) 𝓘(ℝ, P) (extChartAt 𝓘(ℝ, P) p) x v = v := by
  have e : (extChartAt 𝓘(ℝ, P) p : seW → P) = chartAt P p := rfl
  rw [e, mfderiv_chartAt_eq_tangentCoordChange (se_src p x), tangentCoordChange_def,
    ModelWithCorners.range_eq_univ, fderivWithin_univ]
  have hev : (extChartAt 𝓘(ℝ, P) p ∘ (extChartAt 𝓘(ℝ, P) x).symm)
      =ᶠ[𝓝 (extChartAt 𝓘(ℝ, P) x x)] id := by
    filter_upwards [seWS_open.mem_nhds x.2] with y hy
    rw [Function.comp_apply, se_symm_apply x hy]; rfl
  rw [hev.fderiv_eq, fderiv_id]; rfl

lemma se_dchartInv (p : seW) {y : P} (hy : y ∈ seWS) (v : P) :
    mfderiv 𝓘(ℝ, P) 𝓘(ℝ, P) (extChartAt 𝓘(ℝ, P) p).symm y v = v := by
  have h := ld_mfderiv_symm_chart p (se_src p ⟨y, hy⟩) v
  rw [se_dchart] at h
  exact h

lemma se_image (p : seW) (A : Set seW) : extChartAt 𝓘(ℝ, P) p '' A = Subtype.val '' A := rfl

lemma se_image_univ (p : seW) : extChartAt 𝓘(ℝ, P) p '' univ = seWS := by
  rw [se_image, image_univ, Subtype.range_coe]; rfl

/-- The flat metric `−dU dV` and `T = ∂_U + ∂_V` on `W`, `M = W`. -/
noncomputable def se_flat : MSpacetime P seW where
  M := univ
  isOpen_M := isOpen_univ
  g := fun _ => gM
  symm := fun _ v w => mink.symm 0 v w
  T := fun _ => ((1, 1) : P)
  T_timelike := fun _ _ => mink.T_timelike 0 (mem_univ _)
  pos_on_perp := fun _ _ v h hv => mink.pos_on_perp 0 (mem_univ _) v h hv

lemma se_hRep_flat (p : seW) {y : P} (hy : y ∈ seWS) : hRep se_flat.g p y = gM := by
  refine ContinuousLinearMap.ext fun v => ContinuousLinearMap.ext fun w => ?_
  rw [ld_hRep_apply, se_dchartInv p hy, se_dchartInv p hy]; rfl

lemma se_chartRep_flat (p : seW) {y : P} (_hy : y ∈ seWS) :
    chartRep se_flat.T p y = ((1, 1) : P) := by
  unfold chartRep; exact se_dchart p _ _

/-- The base point `(U, V) = (0, 1)` of `W`. -/
def seP0 : seW := ⟨((0 : ℝ), (1 : ℝ)), ⟨one_pos, by norm_num⟩⟩

lemma se_oneChart : se_flat.OneChart seP0 where
  sub := fun x _ => se_src _ x
  g_C1 := by
    show ContDiffOn ℝ 1 _ (extChartAt 𝓘(ℝ, P) seP0 '' univ)
    rw [se_image_univ]
    exact contDiffOn_const.congr fun y hy => se_hRep_flat seP0 hy
  T_cont := by
    show ContinuousOn _ (extChartAt 𝓘(ℝ, P) seP0 '' univ)
    rw [se_image_univ]
    exact continuousOn_const.congr fun y hy => se_chartRep_flat seP0 hy

lemma se_flat_locallyOneChart : se_flat.LocallyOneChart := by
  intro p _
  refine ⟨seWS, seWS_open, p.2, ?_, contDiffOn_const.congr fun y hy => se_hRep_flat p hy,
    continuousOn_const.congr fun y hy => se_chartRep_flat p hy⟩
  intro y hy
  exact ⟨⟨y, hy⟩, ⟨mem_univ _, se_src p _⟩, rfl⟩

/-- **The chart spacetime of `se_flat` agrees with `mink` restricted to `W`.** -/
theorem se_chartSp_agree : (MSpacetime.chartSp se_oneChart).SeAgree seK := by
  refine ⟨se_image_univ seP0, fun y hy => ?_⟩
  have hy' : y ∈ seWS := by rw [← se_image_univ seP0]; exact hy
  exact ⟨se_hRep_flat seP0 hy', se_chartRep_flat seP0 hy'⟩

/-! ### The Schwarzschild spacetime on `W` -/

/-- `F(U, V) = (32M³/r) e^{−r/2M}` on `W`. -/
noncomputable def se_F (M : ℝ) (x : seW) : ℝ := FS M x.1

/-- The areal radius `r(U, V)` on `W`. -/
noncomputable def se_r (M : ℝ) (x : seW) : ℝ := rK M x.1

variable {M : ℝ} (hM : 0 < M)

include hM in
lemma se_F_pos (x : seW) : 0 < se_F M x := sk_FS_pos hM x.2.2

/-- **Schwarzschild on EF's domain**: `N = W`, `M = W`, `g = F · (−dU dV)`, `T = ∂_U + ∂_V`. -/
noncomputable def se_S : MSpacetime P seW := se_flat.cz_scale (se_F M) (se_F_pos hM)

lemma se_S_M : (se_S hM).M = univ := rfl

/-- **The metric in the chart:** `hRep g (U, V) = F(U, V) • gM`, i.e. `g = −F(r) dU dV`. -/
theorem se_hRep (p : seW) {y : P} (hy : y ∈ seWS) : hRep (se_S hM).g p y = FS M y • gM := by
  rw [se_S, MSpacetime.cz_hRep_scale, se_hRep_flat p hy, se_symm_apply p hy]; rfl

/-- **`LocallyOneChart` for `se_S` (BUILT)**, from `F` `C¹` on `{UV < 1} ⊇ W`. -/
theorem se_locallyOneChart : (se_S hM).LocallyOneChart := by
  refine se_flat.sk_scale_locallyOneChart (se_F_pos hM) se_flat_locallyOneChart fun p _ => ?_
  have hsub : extChartAt 𝓘(ℝ, P) p '' (se_flat.M ∩ (chartAt P p).source) ⊆ seWS := by
    rintro _ ⟨x, -, rfl⟩; exact x.2
  refine ((sk_FS_contDiffOn hM).mono fun y hy => seWS_kM (hsub hy)).congr fun y hy => ?_
  show FS M ((extChartAt 𝓘(ℝ, P) p).symm y).1 = FS M y
  rw [se_symm_apply p (hsub hy)]

lemma se_chr_iff {x y : seW} : (se_S hM).Chr x y ↔ seK.Chr x.1 y.1 := by
  rw [se_S, se_flat.cz_scale_chr, MSpacetime.ch_chr_iff se_oneChart (se_src _ _) (se_src _ _),
    se_chartSp_agree.chr_iff]; rfl

lemma se_cau_iff {x y : seW} : (se_S hM).Cau x y ↔ seK.Cau x.1 y.1 := by
  rw [se_S, se_flat.cz_scale_cau, MSpacetime.ch_cau_iff se_oneChart (se_src _ _) (se_src _ _),
    se_chartSp_agree.cau_iff]; rfl

/-- **`≪` on `W` is the flat relation:** `x ≪ y ⟺ U_x < U_y ∧ V_x < V_y`. -/
theorem se_chr_iff_lt {x y : seW} : (se_S hM).Chr x y ↔ x.1.1 < y.1.1 ∧ x.1.2 < y.1.2 := by
  rw [se_chr_iff, se_K_chr_iff x.2 y.2]

/-! ### The static observer -/

/-- The observer `O(τ) = (−a e^{−τ/2k}, a e^{τ/2k})` on `UV = −a²`, as a point of `W`. -/
noncomputable def se_O {a : ℝ} (ha : 0 < a) (k τ : ℝ) : seW :=
  ⟨sk_O a (τ / (2 * k)), sk_O_memW ha _⟩

lemma se_image_O {a : ℝ} (ha : 0 < a) {k : ℝ} (hk : 0 < k) :
    extChartAt 𝓘(ℝ, P) seP0 '' range (se_O ha k) = range (sk_O a) := by
  rw [se_image, ← range_comp]
  ext y; constructor
  · rintro ⟨τ, rfl⟩; exact ⟨_, rfl⟩
  · rintro ⟨σ, rfl⟩
    refine ⟨2 * k * σ, ?_⟩
    show sk_O a (2 * k * σ / (2 * k)) = sk_O a σ
    rw [mul_div_cancel_left₀ _ (by positivity)]

lemma se_mem_D_iff {a : ℝ} (ha : 0 < a) {k : ℝ} (hk : 0 < k) (x : seW) :
    x ∈ (se_S hM).D (range (se_O ha k)) ↔ x.1 ∈ seR := by
  rw [se_S, se_flat.cz_scale_D,
    MSpacetime.ch_mem_D_iff se_oneChart (fun _ _ => se_src _ _) (se_src _ x),
    se_chartSp_agree.D_eq, se_image_O ha hk, se_K_D ha]; rfl

lemma se_mem_H_iff {a : ℝ} (ha : 0 < a) {k : ℝ} (hk : 0 < k) (x : seW) :
    x ∈ (se_S hM).H (range (se_O ha k)) ↔ x.1.1 = 0 := by
  rw [se_S, se_flat.cz_scale_H,
    MSpacetime.ch_mem_H_iff se_oneChart (fun _ _ => se_src _ _) (se_src _ x),
    se_chartSp_agree.H_eq, se_image_O ha hk]
  exact se_K_H ha x.2

/-- **① The foundation (BUILT).** On `N = W = {V > 0, UV < 1}` with `M = W`, for any `a, k > 0`:
`LocallyOneChart`; `g = −F dU dV` in the chart; `≪` is the flat relation; `I⁻(O) = D` is region I
`{U < 0, V > 0}`; `O` is future-directed; `J ⊆ M`; `𝓗⁺ = ∂_W J⁻(O)` is `{U = 0}` in `W`, i.e.
`{U = 0, V > 0}` in the plane, it lies in `M` and is non-empty, and `r = 2M` on it. -/
theorem se_foundation {a : ℝ} (ha : 0 < a) {k : ℝ} (hk : 0 < k) :
    (se_S hM).M = univ ∧ (se_S hM).LocallyOneChart ∧
    (∀ (p : seW) {y : P}, y ∈ seWS → hRep (se_S hM).g p y = FS M y • gM) ∧
    (∀ x y : seW, (se_S hM).Chr x y ↔ x.1.1 < y.1.1 ∧ x.1.2 < y.1.2) ∧
    (se_S hM).IpastSet (range (se_O ha k)) = (se_S hM).D (range (se_O ha k)) ∧
    (se_S hM).D (range (se_O ha k)) = {x | x.1.1 < 0} ∧
    Subtype.val '' (se_S hM).D (range (se_O ha k)) = {p : P | p.1 < 0 ∧ 0 < p.2} ∧
    (∀ s t : ℝ, s < t → (se_S hM).Chr (se_O ha k s) (se_O ha k t)) ∧
    range (se_O ha k) ⊆ (se_S hM).M ∧
    (se_S hM).H (range (se_O ha k)) = {x | x.1.1 = 0} ∧
    Subtype.val '' (se_S hM).H (range (se_O ha k)) = {p : P | p.1 = 0 ∧ 0 < p.2} ∧
    (se_S hM).H (range (se_O ha k)) ⊆ (se_S hM).M ∧
    ((se_S hM).H (range (se_O ha k))).Nonempty ∧
    (∀ x ∈ (se_S hM).H (range (se_O ha k)), se_r M x = 2 * M) := by
  have hD : (se_S hM).D (range (se_O ha k)) = {x | x.1.1 < 0} := by
    ext x; rw [se_mem_D_iff hM ha hk]
    exact ⟨fun h => h.1, fun h => ⟨h, x.2.1⟩⟩
  have hH : (se_S hM).H (range (se_O ha k)) = {x | x.1.1 = 0} := by
    ext x; exact se_mem_H_iff hM ha hk x
  refine ⟨rfl, se_locallyOneChart hM, fun p y hy => se_hRep hM p hy, fun x y => se_chr_iff_lt hM,
    rfl, hD, ?_, fun s t hst => ?_, subset_univ _, hH, ?_, subset_univ _, ⟨seP0, ?_⟩,
    fun x hx => ?_⟩
  · rw [hD]; ext p; constructor
    · rintro ⟨x, hx, rfl⟩; exact ⟨hx, x.2.1⟩
    · rintro ⟨h1, h2⟩
      exact ⟨⟨p, seR_subset_WS ⟨h1, h2⟩⟩, h1, rfl⟩
  · rw [se_chr_iff_lt]
    have : s / (2 * k) < t / (2 * k) := div_lt_div_of_pos_right hst (by positivity)
    exact sk_O_mono ha this
  · rw [hH]; ext p; constructor
    · rintro ⟨x, hx, rfl⟩; exact ⟨hx, x.2.1⟩
    · rintro ⟨h1, h2⟩
      exact ⟨⟨p, ⟨h2, by rw [h1]; norm_num⟩⟩, h1, rfl⟩
  · rw [hH]; rfl
  · rw [hH] at hx
    exact (sk_rK_eq_two_iff hM (p := x.1) x.2.2).2 (by rw [show x.1.1 = 0 from hx, zero_mul])

/-! ### ② The stationary time `Θ = √(1 − 2M/r₀) · t` and the headline -/

/-- `Θ_k` on `W`: `Θ_k(x) = k (log V − log(−U))`. -/
noncomputable def se_Θ (k : ℝ) (x : seW) : ℝ := seΘP k x.1

/-- **② `Θ_k` is Cauchy temporal on `D` (BUILT)**, for any `a, k > 0`: `se_cauchy_RI` carried to the
chart spacetime by `SeAgree` (`se_chartSp_agree`, `se_K_D`), to `W` by campaign 84's
`ch_isCauchy_VN`, and to `g = F g_flat` by conformal invariance (`cz_scale_isCauchyTemporalOn`). -/
theorem se_cauchy {a : ℝ} (ha : 0 < a) {k : ℝ} (hk : 0 < k) :
    (se_S hM).IsCauchyTemporalOn ((se_S hM).D (range (se_O ha k))) (se_Θ k) := by
  have hagree : se_RI.SeAgree
      ((MSpacetime.chartSp se_oneChart).Dsp (extChartAt 𝓘(ℝ, P) seP0 '' range (se_O ha k))) := by
    rw [se_image_O ha hk]
    have h1 : se_RI.SeAgree (seK.Dsp (range (sk_O a))) :=
      ⟨(se_K_D ha).symm, fun _ _ => ⟨rfl, rfl⟩⟩
    exact h1.trans (se_chartSp_agree.symm.Dsp _)
  have h := MSpacetime.ch_isCauchy_VN se_oneChart (J := range (se_O ha k)) (subset_univ _)
    (hagree.isCauchyTemporal (se_cauchy_RI hk))
  rw [se_S, se_flat.cz_scale_D]
  exact se_flat.cz_scale_isCauchyTemporalOn (se_F_pos hM) h

lemma se_Θ_O {a : ℝ} (ha : 0 < a) {k : ℝ} (hk : 0 < k) (τ : ℝ) : se_Θ k (se_O ha k τ) = τ := by
  show k * (Real.log (a * Real.exp (τ / (2 * k))) -
    Real.log (-(-(a * Real.exp (-(τ / (2 * k))))))) = τ
  rw [neg_neg, Real.log_mul ha.ne' (Real.exp_pos _).ne', Real.log_mul ha.ne' (Real.exp_pos _).ne',
    Real.log_exp, Real.log_exp]
  field_simp; ring

/-- The constant `κ · 2M`, `κ = √(1 − 2M/r₀)`. -/
noncomputable def se_k (M r₀ : ℝ) : ℝ := 2 * M * Real.sqrt (1 - 2 * M / r₀)

/-- The observer's Kruskal scale `a = √(h(r₀))`, `UV = −h(r₀)`. -/
noncomputable def se_a (M r₀ : ℝ) : ℝ := Real.sqrt (hK M r₀)

include hM in
lemma se_hK_pos {r₀ : ℝ} (hr₀ : 2 * M < r₀) : 0 < hK M r₀ := by
  rw [← hK_two hM]
  exact hK_strictMonoOn hM (mem_Ici.2 (by positivity)) (mem_Ici.2 (by linarith)) hr₀

include hM in
lemma se_a_pos {r₀ : ℝ} (hr₀ : 2 * M < r₀) : 0 < se_a M r₀ := Real.sqrt_pos.2 (se_hK_pos hM hr₀)

include hM in
lemma se_k_pos {r₀ : ℝ} (hr₀ : 2 * M < r₀) : 0 < se_k M r₀ := by
  have hr : 0 < r₀ := by linarith
  have : 2 * M / r₀ < 1 := by rw [div_lt_one hr]; exact hr₀
  exact mul_pos (by positivity) (Real.sqrt_pos.2 (by linarith))

/-- **The static observer at `r₀ > 2M`**, parametrised by `Θ`: `O(τ) = (−a e^{−τ/2k}, a e^{τ/2k})`,
`a = √h(r₀)`, `k = 2M√(1 − 2M/r₀)`. -/
noncomputable def se_Ost {r₀ : ℝ} (hr₀ : 2 * M < r₀) : ℝ → seW :=
  se_O (se_a_pos hM hr₀) (se_k M r₀)

/-- The stationary time adapted to the static observer, `Θ = √(1 − 2M/r₀) · 2M (log V − log(−U))`. -/
noncomputable def se_Θst (M r₀ : ℝ) : seW → ℝ := se_Θ (se_k M r₀)

lemma se_r_Ost {r₀ : ℝ} (hr₀ : 2 * M < r₀) (τ : ℝ) : se_r M (se_Ost hM hr₀ τ) = r₀ := by
  show rinv M (-((sk_O (se_a M r₀) _).1 * (sk_O (se_a M r₀) _).2)) = r₀
  rw [sk_O_UV, se_a, Real.sq_sqrt (se_hK_pos hM hr₀).le, neg_neg, rinv_hK hM (by linarith)]

/-- **The static observer is at `r = r₀` and `Θ` is its proper-time parameter:** `Θ(O τ) = τ`, and
`g(Ȯ, Ȯ) = −F U̇ V̇ = −1` at every `τ`. -/
theorem se_proper_time {r₀ : ℝ} (hr₀ : 2 * M < r₀) (τ : ℝ) :
    se_r M (se_Ost hM hr₀ τ) = r₀ ∧ se_Θst M r₀ (se_Ost hM hr₀ τ) = τ ∧
    hRep (se_S hM).g seP0 (se_Ost hM hr₀ τ).1
      (deriv (fun s => (se_Ost hM hr₀ s).1) τ) (deriv (fun s => (se_Ost hM hr₀ s).1) τ) = -1 := by
  refine ⟨se_r_Ost hM hr₀ τ, se_Θ_O _ (se_k_pos hM hr₀) τ, ?_⟩
  set a := se_a M r₀
  set k := se_k M r₀
  have hk := se_k_pos hM hr₀
  have hσ : HasDerivAt (fun s : ℝ => s / (2 * k)) (1 / (2 * k)) τ :=
    (hasDerivAt_id τ).div_const _
  have hU : HasDerivAt (fun s : ℝ => -(a * Real.exp (-(s / (2 * k)))))
      (-(a * (Real.exp (-(τ / (2 * k))) * (-(1 / (2 * k)))))) τ :=
    ((hσ.neg.exp).const_mul a).neg
  have hV : HasDerivAt (fun s : ℝ => a * Real.exp (s / (2 * k)))
      (a * (Real.exp (τ / (2 * k)) * (1 / (2 * k)))) τ :=
    (hσ.exp).const_mul a
  have hd : deriv (fun s => (se_Ost hM hr₀ s).1) τ =
      ((-(a * (Real.exp (-(τ / (2 * k))) * (-(1 / (2 * k))))),
        a * (Real.exp (τ / (2 * k)) * (1 / (2 * k)))) : P) :=
    (hU.prodMk hV).deriv
  rw [hd, se_hRep hM seP0 (se_Ost hM hr₀ τ).2, smul_apply, smul_apply, gM_apply, smul_eq_mul]
  have hr : rK M (se_Ost hM hr₀ τ).1 = r₀ := se_r_Ost hM hr₀ τ
  unfold FS; rw [hr]
  simp only
  have hexp : Real.exp (-(τ / (2 * k))) * Real.exp (τ / (2 * k)) = 1 := by
    rw [← Real.exp_add, neg_add_cancel, Real.exp_zero]
  have ha2 : a ^ 2 = hK M r₀ := Real.sq_sqrt (se_hK_pos hM hr₀).le
  have hr0 : 0 < r₀ := by linarith
  have hk2 : k ^ 2 = 4 * M ^ 2 * (1 - 2 * M / r₀) := by
    rw [show k = 2 * M * Real.sqrt (1 - 2 * M / r₀) from rfl, mul_pow, Real.sq_sqrt]
    · ring
    rw [sub_nonneg, div_le_one hr0]; linarith
  have hh : hK M r₀ * Real.exp (-r₀ / (2 * M)) = r₀ / (2 * M) - 1 := by
    unfold hK
    rw [mul_assoc, ← Real.exp_add, show r₀ / (2 * M) + -r₀ / (2 * M) = 0 by ring, Real.exp_zero,
      mul_one]
  have hkne : k ≠ 0 := hk.ne'
  have hMne : M ≠ 0 := hM.ne'
  have key : 32 * M ^ 3 / r₀ * Real.exp (-r₀ / (2 * M)) * (a ^ 2 / (4 * k ^ 2)) = 1 := by
    rw [ha2, hk2]
    have hlt : 2 * M / r₀ < 1 := by rw [div_lt_one hr0]; exact hr₀
    have hne : 16 * M ^ 2 * (1 - 2 * M / r₀) ≠ 0 := by
      have : 0 < 1 - 2 * M / r₀ := by linarith
      positivity
    rw [show 32 * M ^ 3 / r₀ * Real.exp (-r₀ / (2 * M)) *
        (hK M r₀ / (4 * (4 * M ^ 2 * (1 - 2 * M / r₀)))) =
        32 * M ^ 3 / r₀ * (hK M r₀ * Real.exp (-r₀ / (2 * M))) / (16 * M ^ 2 * (1 - 2 * M / r₀))
        by ring, hh, div_eq_one_iff_eq hne]
    field_simp; ring
  have hUV : -(a * (Real.exp (-(τ / (2 * k))) * (-(1 / (2 * k))))) *
      (a * (Real.exp (τ / (2 * k)) * (1 / (2 * k)))) = a ^ 2 / (4 * k ^ 2) := by
    have : -(a * (Real.exp (-(τ / (2 * k))) * (-(1 / (2 * k))))) *
        (a * (Real.exp (τ / (2 * k)) * (1 / (2 * k)))) =
        a ^ 2 * (Real.exp (-(τ / (2 * k))) * Real.exp (τ / (2 * k))) / (4 * k ^ 2) := by
      field_simp; ring
    rw [this, hexp, mul_one]
  linear_combination (-(32 * M ^ 3 / r₀ * Real.exp (-r₀ / (2 * M)))) * hUV + (-1 : ℝ) * key

/-! ### Cone disjointness (campaign 91's `cd_`, copied from `ConeDisjoint.lean`) -/

end SEModel

section SeCone
open Manifold
set_option linter.unusedSectionVars false

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
variable {N : Type*} [TopologicalSpace N] [ChartedSpace E N] [IsManifold 𝓘(ℝ, E) 1 N]

namespace MSpacetime

theorem cd_chr_of_mem_closure_Jpast {S : MSpacetime E N} (hL : S.LocallyOneChart) {p x y : N}
    (hx : x ∈ closure (S.Jpast p)) (hyx : S.Chr y x) : S.Chr y p := by
  obtain ⟨w, hyw, hwp⟩ := mem_closure_iff_nhds.1 hx _ ((S.mk_isOpen_Ifut hL y).mem_nhds hyx)
  exact S.mk_pushup' hL hyw hwp

theorem cd_mem_closure_sublevel {S : MSpacetime E N} (hL : S.LocallyOneChart) {J : Set N}
    {Θ : N → ℝ} (hΘ : S.IsTemporalOn (S.D J) Θ) {p x : N} (hp : p ∈ S.D J) (hxM : x ∈ S.M)
    (hx : x ∈ closure (S.Jpast p)) : x ∈ closure {y | y ∈ S.D J ∧ Θ y ≤ Θ p} := by
  rw [mem_closure_iff_nhds]
  intro U hU
  obtain ⟨y, hyU, hyx⟩ := S.mh_past_step hL hxM hU
  have hyp := cd_chr_of_mem_closure_Jpast hL hx hyx
  exact ⟨y, hyU, S.mh_D_of_chr hyp hp, (S.mh_temporalD_chr hL hΘ hyp hp).le⟩

theorem cd_closure_Jpast_subset_D {S : MSpacetime E N} (hL : S.LocallyOneChart) {J : Set N}
    {Θ : N → ℝ} (hΘ : S.IsTemporalOn (S.D J) Θ) (hP : S.SublevelProper J Θ) {p : N}
    (hp : p ∈ S.D J) : closure (S.Jpast p) ∩ S.M ⊆ S.D J := fun _ hx =>
  hP (Θ p) (cd_mem_closure_sublevel hL hΘ hp hx.2 hx.1)

theorem cd_closure_Jpast_inter_H {S : MSpacetime E N} (hL : S.LocallyOneChart) {J : Set N}
    {O : ℝ → N} (hOD : S.IpastSet (range O) = S.D J)
    (hmono : ∀ s t : ℝ, s < t → S.Chr (O s) (O t)) (hHM : S.H J ⊆ S.M) {Θ : N → ℝ}
    (hΘ : S.IsTemporalOn (S.D J) Θ) (hP : S.SublevelProper J Θ) (τ : ℝ) :
    closure (S.Jpast (O τ)) ∩ S.H J = ∅ := by
  refine eq_empty_iff_forall_notMem.2 fun x hx => S.mh_not_mem_D_of_H hL hx.2 ?_
  exact cd_closure_Jpast_subset_D hL hΘ hP (mh_observer_mem_D hOD hmono τ) ⟨hx.1, hHM hx.2⟩

/-- **Campaign 91's clause (copied): no past light cone meets `𝓗⁺`.** -/
theorem cd_cone_disjoint [T2Space N] {S : MSpacetime E N} (hL : S.LocallyOneChart) {J : Set N}
    {O : ℝ → N} (hOD : S.IpastSet (range O) = S.D J)
    (hmono : ∀ s t : ℝ, s < t → S.Chr (O s) (O t)) (hJM : J ⊆ S.M) (hHM : S.H J ⊆ S.M)
    {Θ : N → ℝ} (hΘ : S.IsCauchyTemporalOn (S.D J) Θ) :
    ∀ τ, S.cone O τ ∩ S.H J = ∅ := by
  have hF : S.FutCauchyTemporalOn (S.D J) Θ :=
    me_futCauchy_of_cauchy_N hL (S.mk_isOpen_D hL J) (S.D_subset_M J) hΘ
  have hP := S.mh_sublevelProper hL (S.mh_hint hL hJM) hHM hF
  intro τ
  exact subset_empty_iff.1 fun x hx =>
    (cd_closure_Jpast_inter_H hL hOD hmono hHM hΘ.1 hP τ).subset
      ⟨frontier_subset_closure hx.1, hx.2⟩

end MSpacetime

end SeCone

/-! ### The unbounded stretch (campaign 92's `hs_`, copied from `HorizonStretch.lean`) -/

section HSMetric
variable {X : Type*} [MetricSpace X]

/-- **The `ε`-stretch at time `τ`**: the points of `H` within `infDist < ε` of `A τ`. -/
noncomputable def hs_stretch (A : ℝ → Set X) (H : Set X) (τ ε : ℝ) : Set X :=
  {q | q ∈ H ∧ Metric.infDist q (A τ) < ε}

theorem hs_stretch_subset (A : ℝ → Set X) (H : Set X) (τ ε : ℝ) : hs_stretch A H τ ε ⊆ H :=
  fun _ h => h.1

/-- Pointwise approach from the Kuratowski lower limit: eventually `A τ` meets `ball q r`. -/
theorem hs_pointwise {A : ℝ → Set X} {q : X} (hq : q ∈ KLi A) {r : ℝ} (hr : 0 < r) :
    ∀ᶠ τ in atTop, ∃ a ∈ A τ, dist q a < r := by
  filter_upwards [hq _ (Metric.ball_mem_nhds q hr)] with τ ⟨a, ha, hd⟩
  exact ⟨a, ha, by rw [dist_comm]; exact hd⟩

/-- **(S1), with points.** If `H ⊆ KLi A`, then for every compact `K ⊆ H` and `ε > 0`, eventually
every `q ∈ K` has a point of `A τ` within `ε`. -/
theorem hs_uniform_on_compact_pts {A : ℝ → Set X} {H : Set X} (_hH : H ⊆ KLi A) {ε : ℝ}
    (hε : 0 < ε) {K : Set X} (hKH : K ⊆ H) (hK : IsCompact K) :
    ∀ᶠ τ in atTop, ∀ q ∈ K, ∃ a ∈ A τ, dist q a < ε := by
  obtain ⟨t, htK, htf, hcov⟩ := finite_cover_balls_of_compact hK (half_pos hε)
  have hall : ∀ᶠ τ in atTop, ∀ c ∈ t, ∃ a ∈ A τ, dist c a < ε / 2 :=
    (htf.eventually_all).2 fun c hc => hs_pointwise (_hH (hKH (htK hc))) (half_pos hε)
  filter_upwards [hall] with τ hτ q hq
  obtain ⟨c, hc, hqc⟩ := mem_iUnion₂.1 (hcov hq)
  obtain ⟨a, ha, hca⟩ := hτ c hc
  refine ⟨a, ha, ?_⟩
  have := dist_triangle q c a
  rw [Metric.mem_ball] at hqc
  linarith

/-- **(S1) Uniform approach on compacts.** -/
theorem hs_uniform_on_compact {A : ℝ → Set X} {H : Set X} (hH : H ⊆ KLi A) {ε : ℝ}
    (hε : 0 < ε) {K : Set X} (hKH : K ⊆ H) (hK : IsCompact K) :
    ∀ᶠ τ in atTop, K ⊆ hs_stretch A H τ ε := by
  filter_upwards [hs_uniform_on_compact_pts hH hε hKH hK] with τ hτ q hq
  obtain ⟨a, ha, hd⟩ := hτ q hq
  exact ⟨hKH hq, lt_of_le_of_lt (Metric.infDist_le_dist_of_mem ha) hd⟩

/-- **(S2) Unboundedness.** If `H ⊆ KLi A` and `H` lies in no compact set, then for every `ε > 0`
and every compact `K`, eventually the `ε`-stretch is not inside `K`. -/
theorem hs_unbounded {A : ℝ → Set X} {H : Set X} (hH : H ⊆ KLi A)
    (hnc : ∀ K : Set X, IsCompact K → ¬ H ⊆ K) {ε : ℝ} (hε : 0 < ε) {K : Set X}
    (hK : IsCompact K) : ∀ᶠ τ in atTop, ¬ hs_stretch A H τ ε ⊆ K := by
  obtain ⟨q, hqH, hqK⟩ := not_subset.1 (hnc K hK)
  filter_upwards [hs_uniform_on_compact hH hε (singleton_subset_iff.2 hqH) isCompact_singleton]
    with τ hτ hsub
  exact hqK (hsub (hτ rfl))

end HSMetric

section HSManifold
open Manifold
set_option linter.unusedSectionVars false

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
variable {N : Type*} [tN : TopologicalSpace N] [ChartedSpace E N] [IsManifold 𝓘(ℝ, E) 1 N]

namespace MSpacetime
variable {S : MSpacetime E N}

/-- **(S1) and (S2) on `N`, for the past light cones.** Under `mc_cone_kuratowski_N`'s hypotheses,
for **any** metric `m` on `N` inducing `N`'s (charted) topology: every compact `K ⊆ 𝓗⁺` is
eventually in the `ε`-stretch of the cones `∂J⁻(O τ)`, and if `𝓗⁺` lies in no compact set the
`ε`-stretch eventually leaves every compact set. (The metric is a separate argument: the
`MSpacetime` layer fixes `[TopologicalSpace N]`, and `hm` identifies the two topologies.) -/
theorem hs_stretch_N (hL : S.LocallyOneChart) {J : Set N} {O : ℝ → N}
    (hOD : S.IpastSet (range O) = S.D J) (hmono : ∀ s t : ℝ, s < t → S.Chr (O s) (O t))
    (hJM : J ⊆ S.M) (m : MetricSpace N)
    (hm : m.toUniformSpace.toTopologicalSpace = tN) {ε : ℝ} (hε : 0 < ε) :
    (∀ K : Set N, K ⊆ S.H J → IsCompact K →
      ∀ᶠ τ in atTop, K ⊆ @hs_stretch N m (S.cone O) (S.H J) τ ε) ∧
    ((∀ K : Set N, IsCompact K → ¬ S.H J ⊆ K) → ∀ K : Set N, IsCompact K →
      ∀ᶠ τ in atTop, ¬ @hs_stretch N m (S.cone O) (S.H J) τ ε ⊆ K) := by
  have hKL : S.H J ⊆ KLi (S.cone O) := (mc_cone_kuratowski_N hL hOD hmono hJM).1.symm.subset
  revert hKL
  generalize S.H J = H
  generalize S.cone O = A
  subst hm
  intro hKL
  exact ⟨fun K hKH hK => hs_uniform_on_compact hKL hε hKH hK,
    fun hnc K hK => hs_unbounded hKL hnc hε hK⟩

end MSpacetime

end HSManifold

namespace SEModel
open Model Kruskal Manifold ContinuousLinearMap TopologicalSpace

variable {M : ℝ} (hM : 0 < M)

/-- **Every cone is non-empty**: `O τ ∈ ∂_W J⁻(O τ)` (`O(s) → O(τ)` as `s ↓ τ`, and `O(s) ∉ J⁻(O τ)`
for `s > τ`, since `U` increases along `O`). -/
theorem se_O_mem_cone {a : ℝ} (ha : 0 < a) {k : ℝ} (hk : 0 < k) (τ : ℝ) :
    se_O ha k τ ∈ (se_S hM).cone (se_O ha k) τ := by
  refine ⟨subset_closure Relation.ReflTransGen.refl, fun hint => ?_⟩
  have hc : Continuous (se_O ha k) := by
    refine Continuous.subtype_mk ?_ _
    unfold sk_O; fun_prop
  have hev : ∀ᶠ s in 𝓝[>] τ, se_O ha k s ∈ (se_S hM).Jpast (se_O ha k τ) :=
    ((hc.tendsto τ).mono_left nhdsWithin_le_nhds).eventually (mem_interior_iff_mem_nhds.1 hint)
  obtain ⟨s, hs, hsτ⟩ := (hev.and self_mem_nhdsWithin).exists
  have h1 := (cau_le (seK_cau_mink ((se_cau_iff hM).1 hs))).1
  have h2 := (sk_O_mono ha (div_lt_div_of_pos_right (show τ < s from hsτ)
    (by positivity : (0:ℝ) < 2 * k))).1
  exact absurd h1 (not_le.2 h2)

/-- **② The headline on Schwarzschild (BUILT).** For `M > 0`, `r₀ > 2M`, the static observer
`O = se_Ost` at `r = r₀` and `Θ = √(1 − 2M/r₀) · t` on `N = W = {V > 0, UV < 1}`, `M = W`:
`Θ` is Cauchy temporal on `D` (region I) and adapted (`Θ(O τ) = τ`, proper time); properness;
`KLi = KLs = 𝓗⁺` for the slices of `Θ` and for the past cones `∂J⁻(O τ)`; no cone meets `𝓗⁺`;
and `𝓗⁺ = {U = 0, V > 0}`, on which `r = 2M`. Non-vacuity: `𝓗⁺ ≠ ∅` and every cone contains
`O τ`. -/
theorem se_headline {r₀ : ℝ} (hr₀ : 2 * M < r₀) :
    (se_S hM).IsCauchyTemporalOn ((se_S hM).D (range (se_Ost hM hr₀))) (se_Θst M r₀) ∧
    (∀ τ, se_Θst M r₀ (se_Ost hM hr₀ τ) = τ) ∧
    (∀ τ, se_r M (se_Ost hM hr₀ τ) = r₀) ∧
    Subtype.val '' (se_S hM).D (range (se_Ost hM hr₀)) = {p : P | p.1 < 0 ∧ 0 < p.2} ∧
    Subtype.val '' (se_S hM).H (range (se_Ost hM hr₀)) = {p : P | p.1 = 0 ∧ 0 < p.2} ∧
    (∀ x ∈ (se_S hM).H (range (se_Ost hM hr₀)), se_r M x = 2 * M) ∧
    (se_S hM).SublevelProper (range (se_Ost hM hr₀)) (se_Θst M r₀) ∧
    KLi ((se_S hM).slice (range (se_Ost hM hr₀)) (se_Θst M r₀)) =
      (se_S hM).H (range (se_Ost hM hr₀)) ∧
    KLs ((se_S hM).slice (range (se_Ost hM hr₀)) (se_Θst M r₀)) =
      (se_S hM).H (range (se_Ost hM hr₀)) ∧
    KLi ((se_S hM).cone (se_Ost hM hr₀)) = (se_S hM).H (range (se_Ost hM hr₀)) ∧
    KLs ((se_S hM).cone (se_Ost hM hr₀)) = (se_S hM).H (range (se_Ost hM hr₀)) ∧
    (∀ τ, (se_S hM).cone (se_Ost hM hr₀) τ ∩ (se_S hM).H (range (se_Ost hM hr₀)) = ∅) ∧
    ((se_S hM).H (range (se_Ost hM hr₀))).Nonempty ∧
    (∀ τ, ((se_S hM).cone (se_Ost hM hr₀) τ).Nonempty) := by
  have ha := se_a_pos hM hr₀
  have hk := se_k_pos hM hr₀
  obtain ⟨-, hL, -, -, hOD, -, hDv, hmono, hJM, -, hHv, hHM, hne, hr⟩ := se_foundation hM ha hk
  have hΘ := se_cauchy hM ha hk
  have hadapt : ∀ τ, se_Θst M r₀ (se_Ost hM hr₀ τ) = τ + 0 := fun τ => by
    rw [add_zero]; exact se_Θ_O ha hk τ
  obtain ⟨h1, h2, h3⟩ := (se_S hM).mh_causal_alignment_gh_N hL hOD hmono hJM hHM hΘ hadapt
  obtain ⟨h4, h5⟩ := MSpacetime.mc_cone_kuratowski_N hL hOD hmono hJM
  exact ⟨hΘ, fun τ => se_Θ_O ha hk τ, se_r_Ost hM hr₀, hDv, hHv, hr, h1, h2, h3, h4, h5,
    MSpacetime.cd_cone_disjoint hL hOD hmono hJM hHM hΘ, hne,
    fun τ => ⟨_, se_O_mem_cone hM ha hk τ⟩⟩

/-- `𝓗⁺ = {U = 0, V > 0}` lies in no compact set of `W` (`V` is unbounded on it). -/
theorem se_H_not_compact {r₀ : ℝ} (hr₀ : 2 * M < r₀) (K : Set seW) (hK : IsCompact K) :
    ¬ (se_S hM).H (range (se_Ost hM hr₀)) ⊆ K := by
  intro hsub
  have hH := (se_foundation hM (se_a_pos hM hr₀) (se_k_pos hM hr₀)).2.2.2.2.2.2.2.2.2.1
  obtain ⟨T, hT⟩ := (hK.image (continuous_snd.comp continuous_subtype_val)).bddAbove
  have hmem : (⟨((0:ℝ), |T| + 1), ⟨by positivity, by norm_num⟩⟩ : seW) ∈
      (se_S hM).H (range (se_Ost hM hr₀)) := by
    rw [se_Ost, hH]; rfl
  have h := hT ⟨_, hsub hmem, rfl⟩
  have : |T| + 1 ≤ T := h
  linarith [le_abs_self T]

/-- **The stretch on Schwarzschild (BUILT)**, for `W`'s own (subtype) metric, which induces its
manifold topology (`rfl`): every compact `K ⊆ 𝓗⁺` is eventually inside the `ε`-stretch of the past
cones, and the `ε`-stretch eventually leaves every compact set of `W`. -/
theorem se_stretch {r₀ : ℝ} (hr₀ : 2 * M < r₀) {ε : ℝ} (hε : 0 < ε) :
    (∀ K : Set seW, K ⊆ (se_S hM).H (range (se_Ost hM hr₀)) → IsCompact K →
      ∀ᶠ τ in atTop, K ⊆ hs_stretch ((se_S hM).cone (se_Ost hM hr₀))
        ((se_S hM).H (range (se_Ost hM hr₀))) τ ε) ∧
    (∀ K : Set seW, IsCompact K →
      ∀ᶠ τ in atTop, ¬ hs_stretch ((se_S hM).cone (se_Ost hM hr₀))
        ((se_S hM).H (range (se_Ost hM hr₀))) τ ε ⊆ K) := by
  obtain ⟨-, hL, -, -, hOD, -, -, hmono, hJM, -⟩ :=
    se_foundation hM (se_a_pos hM hr₀) (se_k_pos hM hr₀)
  obtain ⟨h1, h2⟩ := MSpacetime.hs_stretch_N hL hOD hmono hJM inferInstance rfl hε
  exact ⟨h1, h2 (se_H_not_compact hM hr₀)⟩

/-- **Non-vacuity (BUILT):** at `M = 1`, `r₀ = 4`, the headline holds, `𝓗⁺` and every cone are
non-empty, `g ≠ g_flat` (at `(0, 1)`, `F = 16/e ≠ 1`), and `F` is non-constant. -/
theorem se_nonvacuous :
    ((se_S one_pos).H (range (se_Ost one_pos (r₀ := 4) (by norm_num)))).Nonempty ∧
    (∀ τ, ((se_S one_pos).cone (se_Ost one_pos (r₀ := 4) (by norm_num)) τ).Nonempty) ∧
    (∀ τ, ((se_S one_pos).cone (se_Ost one_pos (r₀ := 4) (by norm_num)) τ ∩
      (se_S one_pos).H (range (se_Ost one_pos (r₀ := 4) (by norm_num)))) = ∅) ∧
    hRep (se_S one_pos).g seP0 (0, 1) ≠ gM ∧
    FS 1 (0, 0) ≠ FS 1 (-1, -hK 1 (4 * 1) / (-1)) := by
  obtain ⟨-, -, -, -, -, -, -, -, -, -, -, hdis, hne, hcone⟩ :=
    se_headline one_pos (r₀ := 4) (by norm_num)
  obtain ⟨-, -, hnc⟩ := sk_FS_nonconst one_pos
  refine ⟨hne, hcone, hdis, fun h => ?_, hnc⟩
  have h0 : rK 1 ((0:ℝ), (1:ℝ)) = 2 * 1 :=
    (sk_rK_eq_two_iff one_pos (p := ((0:ℝ), (1:ℝ))) (by show (0:ℝ) * 1 < 1; norm_num)).2
      (by norm_num)
  rw [se_hRep one_pos seP0 (show ((0:ℝ), (1:ℝ)) ∈ seWS from seP0.2)] at h
  have h2 := congrArg (fun B : P →L[ℝ] P →L[ℝ] ℝ => B (1, 1) (1, 1)) h
  simp only [smul_apply, gM_apply, smul_eq_mul] at h2
  unfold FS at h2; rw [h0] at h2
  have he : Real.exp (-(2 * 1) / (2 * 1)) = Real.exp (-1) := by norm_num
  rw [he] at h2
  have hm : Real.exp (-1) * Real.exp 1 = 1 := by rw [← Real.exp_add]; norm_num
  have := Real.exp_one_lt_d9
  nlinarith [Real.exp_pos (-1)]

end SEModel

/-! ## NEW (campaign 99): the retarded slicing `Θ_ret = a(u + η r)` on region I -/

namespace SRModel
open Model SEModel Kruskal Manifold ContinuousLinearMap TopologicalSpace

set_option synthInstance.maxHeartbeats 400000

variable {M : ℝ} (hM : 0 < M)

lemma sr_seR_kM {y : P} (hy : y ∈ seR) : y ∈ sk_kM := (seR_subset_WS hy).2

/-! ### Copied from campaign 98's `SchwarzschildAlign.lean` (④), names kept, `sa_IP` read as `seR` -/

/-- `Θ_ret = a(u + η r)` with `u = −4M log(−U)`, as a function of the null coordinates. -/
noncomputable def sa_uP (M a η : ℝ) (y : P) : ℝ :=
  a * (-(4 * M) * Real.log (-y.1) + η * rK M y)

/-- `dr = −(V dU + U dV)/h′(r)` (from `h(r) = −UV`). -/
noncomputable def sa_rD (M : ℝ) (y : P) : P →L[ℝ] ℝ :=
  (hK' M (rK M y))⁻¹ • -(y.1 • snd ℝ ℝ ℝ + y.2 • fst ℝ ℝ ℝ)

/-- `dΘ_ret = a(4M dU/(−U) + η dr)`. -/
noncomputable def sa_uD (M a η : ℝ) (y : P) : P →L[ℝ] ℝ :=
  a • ((-(4 * M)) • ((-y.1)⁻¹ • -(fst ℝ ℝ ℝ)) + η • sa_rD M y)

include hM in
/-- `r_U = −V/h′(r)`, `r_V = −U/h′(r)`. -/
lemma sa_rK_hasFDerivAt {y : P} (hy : y ∈ sk_kM) : HasFDerivAt (rK M) (sa_rD M y) y := by
  have h0 : HasFDerivAt (fun y : P => -(y.1 * y.2)) (-(y.1 • snd ℝ ℝ ℝ + y.2 • fst ℝ ℝ ℝ)) y :=
    (hasFDerivAt_fst.mul hasFDerivAt_snd).neg
  exact HasDerivAt.comp_hasFDerivAt y (rinv_hasDerivAt hM (sk_kM_UV hy)) h0

include hM in
lemma sa_uP_hasFDerivAt (a η : ℝ) {y : P} (hy : y ∈ seR) :
    HasFDerivAt (sa_uP M a η) (sa_uD M a η y) y := by
  have h2 : HasFDerivAt (fun y : P => Real.log (-y.1)) ((-y.1)⁻¹ • -(fst ℝ ℝ ℝ)) y :=
    hasFDerivAt_fst.neg.log (neg_pos.2 hy.1).ne'
  exact ((h2.const_mul (-(4 * M))).add
    ((sa_rK_hasFDerivAt hM (sr_seR_kM hy)).const_mul η)).const_mul a

include hM in
/-- `Θ_ret` is `C¹` on region I. -/
lemma sa_uP_contDiffOn (a η : ℝ) : ContDiffOn ℝ 1 (sa_uP M a η) seR := by
  have h2 : ContDiffOn ℝ 1 (fun y : P => Real.log (-y.1)) seR :=
    contDiff_fst.neg.contDiffOn.log fun y hy => (neg_pos.2 hy.1).ne'
  have hr : ContDiffOn ℝ 1 (rK M) seR :=
    (sk_rK_contDiffOn hM).mono fun y hy => sr_seR_kM hy
  exact contDiffOn_const.mul ((contDiffOn_const.mul h2).add (contDiffOn_const.mul hr))

/-- `k = 4M h′(r) − ηV(−U)`, so that `∂_U Θ_ret = a k/((−U) h′(r))`. -/
noncomputable def sa_k (M η : ℝ) (y : P) : ℝ := 4 * M * hK' M (rK M y) - η * y.2 * (-y.1)

include hM in
lemma sa_hK'_pos {x : ℝ} (hx : 0 < x) : 0 < hK' M x := by unfold hK'; positivity

lemma sa_uD_U (a η : ℝ) {y : P} (hu : 0 < -y.1) (hh : 0 < hK' M (rK M y)) :
    sa_uD M a η y (1, 0) = a * sa_k M η y / ((-y.1) * hK' M (rK M y)) := by
  have hu' : y.1 ≠ 0 := by intro h; rw [h] at hu; simp at hu
  simp [sa_uD, sa_rD, sa_k]
  field_simp
  ring

lemma sa_uD_V (a η : ℝ) (y : P) :
    sa_uD M a η y (0, 1) = a * η * (-y.1) / hK' M (rK M y) := by
  simp [sa_uD, sa_rD]
  ring

/-! ### Calculus on `W` (the chart is the identity) -/

/-- Future causal on `W`: `v_U ≥ 0`, `v_V ≥ 0`, not both `0` (conformal invariance). -/
lemma sr_futCausal_iff (x : seW) (v : P) :
    (se_S hM).FutCausal x v ↔ 0 ≤ v.1 ∧ 0 ≤ v.2 ∧ 0 < v.1 + v.2 := by
  rw [se_S, MSpacetime.cz_scale_futCausal]
  exact futCausal_iff x.1 v

/-- A curve in `W` differentiable at `t` has, as a curve in the plane, derivative `vel γ t`. -/
lemma sr_hasDerivAt {γ : ℝ → seW} {t : ℝ} (hγ : MDifferentiableAt 𝓘(ℝ, ℝ) 𝓘(ℝ, P) γ t) :
    HasDerivAt (fun s => (γ s : P)) (MSpacetime.vel γ t) t := by
  have h := ch_hasDerivAt_chart seP0 hγ (se_src _ _)
  exact h.congr_deriv (se_dchart seP0 (γ t) _)

/-- `dτ` on `W` for `τ = f ∘ val`: `dτ_x(v) = f′(x)(v)`. -/
lemma sr_dfun {f : P → ℝ} {f' : P →L[ℝ] ℝ} {x : seW} (hf : HasFDerivAt f f' x.1) (v : P) :
    MSpacetime.dfun (fun y : seW => f y.1) x v = f' v := by
  have h1 : MDifferentiableAt 𝓘(ℝ, P) 𝓘(ℝ, ℝ) f (extChartAt 𝓘(ℝ, P) seP0 x) :=
    mdifferentiableAt_iff_differentiableAt.2 hf.differentiableAt
  have h2 : MDifferentiableAt 𝓘(ℝ, P) 𝓘(ℝ, P) (extChartAt 𝓘(ℝ, P) seP0) x :=
    mdifferentiableAt_extChartAt (se_src _ _)
  have e : (fun y : seW => f y.1) = f ∘ extChartAt 𝓘(ℝ, P) seP0 := rfl
  show mfderiv 𝓘(ℝ, P) 𝓘(ℝ, ℝ) (fun y : seW => f y.1) x v = _
  rw [e, mfderiv_comp x h1 h2]
  show mfderiv 𝓘(ℝ, P) 𝓘(ℝ, ℝ) f (extChartAt 𝓘(ℝ, P) seP0 x)
    (mfderiv 𝓘(ℝ, P) 𝓘(ℝ, P) (extChartAt 𝓘(ℝ, P) seP0) x v) = _
  rw [se_dchart, mfderiv_eq_fderiv]
  exact congrArg (fun L : P →L[ℝ] ℝ => L v) hf.fderiv

/-- `C¹` on an open set of the plane gives `C¹` on its trace in `W`. -/
lemma sr_contMDiffOn {f : P → ℝ} {A : Set P} (hA : IsOpen A) (hf : ContDiffOn ℝ 1 f A) :
    ContMDiffOn 𝓘(ℝ, P) 𝓘(ℝ, ℝ) 1 (fun y : seW => f y.1) {x | x.1 ∈ A} := by
  intro x hx
  have h1 : ContMDiffAt 𝓘(ℝ, P) 𝓘(ℝ, ℝ) 1 f (extChartAt 𝓘(ℝ, P) seP0 x) :=
    contMDiffAt_iff_contDiffAt.2 ((hf _ hx).contDiffAt (hA.mem_nhds hx))
  exact (h1.comp x (contMDiffAt_extChartAt' (se_src _ _))).contMDiffWithinAt

lemma sr_split (L : P →L[ℝ] ℝ) (v : P) : L v = v.1 * L (1, 0) + v.2 * L (0, 1) := by
  have h : v = v.1 • ((1 : ℝ), (0 : ℝ)) + v.2 • ((0 : ℝ), (1 : ℝ)) := by ext <;> simp
  conv_lhs => rw [h]
  rw [map_add, map_smul, map_smul, smul_eq_mul, smul_eq_mul]

lemma sr_pos_of_causal {A B v₁ v₂ : ℝ} (hA : 0 < A) (hB : 0 < B) (h1 : 0 ≤ v₁) (h2 : 0 ≤ v₂)
    (h3 : 0 < v₁ + v₂) : 0 < v₁ * A + v₂ * B := by
  rcases h1.lt_or_eq with h | h
  · nlinarith [mul_pos h hA, mul_nonneg h2 hB.le]
  · rw [← h] at h3 ⊢
    nlinarith [mul_pos (show 0 < v₂ by linarith) hB]

/-! ### The retarded time and region I -/

/-- **The retarded time function on `W`**: `Θ_ret = a(−4M log(−U) + η r)`. -/
noncomputable def sr_Θ (M a η : ℝ) (x : seW) : ℝ :=
  a * (-4 * M * Real.log (-x.1.1) + η * se_r M x)

lemma sr_Θ_eq (M a η : ℝ) : sr_Θ M a η = fun x : seW => sa_uP M a η x.1 := by
  funext x; simp only [sr_Θ, sa_uP, se_r]; ring

/-- The campaign-98 headline's `D` (the static observer at `r₀`) is region I. -/
theorem sr_D_eq {r₀ : ℝ} (hr₀ : 2 * M < r₀) :
    (se_S hM).D (range (se_Ost hM hr₀)) = {x | x.1.1 < 0} :=
  (se_foundation hM (se_a_pos hM hr₀) (se_k_pos hM hr₀)).2.2.2.2.2.1

include hM in
/-- `k = e^{r/2M} ((2 − η)(r/2M − 1) + 2)` on `{UV < 1}`. -/
lemma sr_k_eq (η : ℝ) {y : P} (hy : y ∈ sk_kM) :
    sa_k M η y = Real.exp (rK M y / (2 * M)) * ((2 - η) * (rK M y / (2 * M) - 1) + 2) := by
  have hh := (sk_rK_spec hM hy).2
  unfold hK at hh
  unfold sa_k hK'
  set r := rK M y
  set e := Real.exp (r / (2 * M))
  have hM' : M ≠ 0 := hM.ne'
  have h4 : 4 * M * (r / (4 * M ^ 2) * e) = 2 * (r / (2 * M)) * e := by field_simp
  rw [h4]
  linear_combination η * hh

include hM in
/-- On region I, `r > 2M`, i.e. `r/2M − 1 > 0`. -/
lemma sr_q_pos {y : P} (hy : y ∈ seR) : 0 < rK M y / (2 * M) - 1 := by
  have hh := (sk_rK_spec hM (sr_seR_kM hy)).2
  unfold hK at hh
  have hpos : 0 < -(y.1 * y.2) := by nlinarith [hy.1, hy.2]
  rw [← hh] at hpos
  exact pos_of_mul_pos_left hpos (Real.exp_pos _).le

/-- **`∂_U Θ_ret > 0` exactly when `η(r − 2M) < 2r`** (P1's `η f < 2`), on region I. -/
theorem sr_dU_pos_iff {r₀ : ℝ} (hr₀ : 2 * M < r₀) {a η : ℝ} (ha : 0 < a) {x : seW}
    (hx : x ∈ (se_S hM).D (range (se_Ost hM hr₀))) :
    0 < MSpacetime.dfun (sr_Θ M a η) x ((1 : ℝ), (0 : ℝ)) ↔
      η * (se_r M x - 2 * M) < 2 * se_r M x := by
  rw [sr_D_eq hM hr₀] at hx
  have hxR : x.1 ∈ seR := ⟨hx, x.2.1⟩
  have hu : 0 < -x.1.1 := neg_pos.2 hx
  have hh := sa_hK'_pos hM (sk_rK_spec hM (sr_seR_kM hxR)).1
  rw [sr_Θ_eq, sr_dfun (sa_uP_hasFDerivAt hM a η hxR), sa_uD_U a η hu hh,
    sr_k_eq hM η (sr_seR_kM hxR)]
  have hden : 0 < -x.1.1 * hK' M (rK M x.1) := mul_pos hu hh
  rw [div_pos_iff_of_pos_right hden, mul_pos_iff_of_pos_left ha,
    mul_pos_iff_of_pos_left (Real.exp_pos _)]
  show 0 < (2 - η) * (rK M x.1 / (2 * M) - 1) + 2 ↔ η * (rK M x.1 - 2 * M) < 2 * rK M x.1
  have hM2 : 0 < 2 * M := by positivity
  have e : (2 - η) * (rK M x.1 / (2 * M) - 1) + 2 =
      (2 * rK M x.1 - η * (rK M x.1 - 2 * M)) / (2 * M) := by
    field_simp; ring
  rw [e, div_pos_iff_of_pos_right hM2, sub_pos]

/-! ### ⓐ Temporality, and the sharp bound `η ≤ 2` -/

/-- **ⓐ `Θ_ret` is temporal on region I for `0 < η ≤ 2` (BUILT).** `dΘ(v) = v_U Θ_U + v_V Θ_V`
with `Θ_V = aη(−U)/h′(r) > 0` and `Θ_U = a k/((−U)h′(r))`,
`k = e^{r/2M}((2 − η)(r/2M − 1) + 2) > 0`. -/
theorem sr_temporal {r₀ : ℝ} (hr₀ : 2 * M < r₀) {a η : ℝ} (ha : 0 < a) (hη : 0 < η)
    (hη2 : η ≤ 2) :
    (se_S hM).IsTemporalOn ((se_S hM).D (range (se_Ost hM hr₀))) (sr_Θ M a η) := by
  rw [sr_D_eq hM hr₀, sr_Θ_eq]
  refine ⟨(sr_contMDiffOn seR_open (sa_uP_contDiffOn hM a η)).mono fun x hx => ⟨hx, x.2.1⟩,
    fun x hx v hv => ?_⟩
  have hx' : x.1.1 < 0 := hx
  have hxR : x.1 ∈ seR := ⟨hx', x.2.1⟩
  have hu : 0 < -x.1.1 := neg_pos.2 hx'
  have hh := sa_hK'_pos hM (sk_rK_spec hM (sr_seR_kM hxR)).1
  rw [sr_dfun (sa_uP_hasFDerivAt hM a η hxR), sr_split]
  obtain ⟨h1, h2, h3⟩ := (sr_futCausal_iff hM x v).1 hv
  have hq := sr_q_pos hM hxR
  have hk : 0 < sa_k M η x.1 := by
    rw [sr_k_eq hM η (sr_seR_kM hxR)]
    refine mul_pos (Real.exp_pos _) ?_
    nlinarith [mul_nonneg (show 0 ≤ 2 - η by linarith) hq.le]
  have hA : 0 < sa_uD M a η x.1 (1, 0) := by
    rw [sa_uD_U a η hu hh]; exact div_pos (mul_pos ha hk) (mul_pos hu hh)
  have hB : 0 < sa_uD M a η x.1 (0, 1) := by
    rw [sa_uD_V]; exact div_pos (mul_pos (mul_pos ha hη) hu) hh
  exact sr_pos_of_causal hA hB h1 h2 h3

include hM in
/-- The point `(−1, h(r₁))` of region I, at which `r = r₁` (for `r₁ > 2M`). -/
lemma sr_pt_mem {r₁ : ℝ} (hr₁ : 2 * M < r₁) : ((-1 : ℝ), hK M r₁) ∈ seWS := by
  have h := se_hK_pos hM hr₁
  exact ⟨h, by nlinarith⟩

include hM in
lemma sr_pt_r {r₁ : ℝ} (hr₁ : 2 * M < r₁) : rK M ((-1 : ℝ), hK M r₁) = r₁ := by
  show rinv M (-((-1) * hK M r₁)) = r₁
  rw [show -((-1) * hK M r₁) = hK M r₁ by ring, rinv_hK hM (by linarith)]

/-- **ⓐ The bound is sharp (BUILT):** for `η > 2`, at the point `U = −1`, `r = 2Mη/(η − 2)` of
region I, the future null vector `∂_U` has `dΘ_ret(∂_U) = 0`; so `Θ_ret` is not temporal on `D`. -/
theorem sr_not_temporal {r₀ : ℝ} (hr₀ : 2 * M < r₀) {a η : ℝ} (hη : 2 < η) :
    (∃ x ∈ (se_S hM).D (range (se_Ost hM hr₀)), se_r M x = 2 * M * η / (η - 2) ∧
      (se_S hM).FutCausal x ((1 : ℝ), (0 : ℝ)) ∧
      MSpacetime.dfun (sr_Θ M a η) x ((1 : ℝ), (0 : ℝ)) = 0) ∧
    ¬ (se_S hM).IsTemporalOn ((se_S hM).D (range (se_Ost hM hr₀))) (sr_Θ M a η) := by
  set r₁ := 2 * M * η / (η - 2)
  have hη2 : 0 < η - 2 := by linarith
  have hr₁ : 2 * M < r₁ := by
    rw [lt_div_iff₀ hη2]; nlinarith
  let x : seW := ⟨((-1 : ℝ), hK M r₁), sr_pt_mem hM hr₁⟩
  have hxD : x ∈ (se_S hM).D (range (se_Ost hM hr₀)) := by
    rw [sr_D_eq hM hr₀]; show (-1 : ℝ) < 0; norm_num
  have hxR : x.1 ∈ seR := ⟨show (-1 : ℝ) < 0 by norm_num, x.2.1⟩
  have hr : rK M x.1 = r₁ := sr_pt_r hM hr₁
  have hc : (se_S hM).FutCausal x ((1 : ℝ), (0 : ℝ)) := by
    rw [sr_futCausal_iff]; norm_num
  have hd : MSpacetime.dfun (sr_Θ M a η) x ((1 : ℝ), (0 : ℝ)) = 0 := by
    have hu : 0 < -x.1.1 := by show (0 : ℝ) < -(-1); norm_num
    have hh := sa_hK'_pos hM (sk_rK_spec hM (sr_seR_kM hxR)).1
    rw [sr_Θ_eq, sr_dfun (sa_uP_hasFDerivAt hM a η hxR), sa_uD_U a η hu hh,
      sr_k_eq hM η (sr_seR_kM hxR), hr]
    have hM' : M ≠ 0 := hM.ne'
    have h0 : (2 - η) * (r₁ / (2 * M) - 1) + 2 = 0 := by
      simp only [r₁]; field_simp; ring
    rw [h0]; simp
  refine ⟨⟨x, hxD, hr, hc, hd⟩, fun hT => ?_⟩
  have := hT.2 x hxD _ hc
  rw [hd] at this
  exact lt_irrefl _ this

/-! ### ⓑ The refutation: a null curve into the white-hole horizon -/

lemma sr_γ_memW {U₀ : ℝ} (hU₀ : U₀ < 0) (s : ℝ) : (U₀, Real.exp s) ∈ seWS := by
  have := mul_neg_of_neg_of_pos hU₀ (Real.exp_pos s)
  exact ⟨Real.exp_pos s, by show U₀ * Real.exp s < 1; linarith⟩

/-- **The witness** `γ(s) = (U₀, eˢ)`: an outgoing null ray of region I, from the white-hole horizon
`V = 0` (to the past) to `V = ∞` (to the future). -/
noncomputable def sr_γ {U₀ : ℝ} (hU₀ : U₀ < 0) (s : ℝ) : seW := ⟨(U₀, Real.exp s), sr_γ_memW hU₀ s⟩

lemma sr_γ_eq {U₀ : ℝ} (hU₀ : U₀ < 0) :
    sr_γ hU₀ = fun s => (extChartAt 𝓘(ℝ, P) seP0).symm ((U₀, Real.exp s) : P) := by
  funext s; exact (se_symm_apply seP0 (sr_γ_memW hU₀ s)).symm

/-- `γ` is differentiable with velocity `(0, eˢ)`. -/
lemma sr_γ_vel {U₀ : ℝ} (hU₀ : U₀ < 0) (s : ℝ) :
    MDifferentiableAt 𝓘(ℝ, ℝ) 𝓘(ℝ, P) (sr_γ hU₀) s ∧
      MSpacetime.vel (sr_γ hU₀) s = ((0 : ℝ), Real.exp s) := by
  have hβ : HasDerivAt (fun s : ℝ => ((U₀, Real.exp s) : P)) ((0 : ℝ), Real.exp s) s :=
    (hasDerivAt_const s U₀).prodMk (Real.hasDerivAt_exp s)
  have ht : ((U₀, Real.exp s) : P) ∈ (extChartAt 𝓘(ℝ, P) seP0).target :=
    ch_mem_target seP0 (se_src seP0 (sr_γ hU₀ s))
  obtain ⟨h1, h2⟩ := ch_vel_symm seP0 hβ.differentiableAt ht
  rw [sr_γ_eq hU₀]
  refine ⟨h1, ?_⟩
  unfold MSpacetime.vel
  rw [h2]
  exact (se_dchartInv seP0 (sr_γ_memW hU₀ s) _).trans hβ.deriv

/-- **The witness as an inextendible causal curve of region I.** Null, future-directed
(`v = (0, eˢ)`); to the future `V → ∞`; to the past `γ → (U₀, 0) ∉ W`, so it has no limit in `D`
(a limit `p` would force `V(p) = 0`, by continuity of `val`). -/
noncomputable def sr_curve {r₀ : ℝ} (hr₀ : 2 * M < r₀) {U₀ : ℝ} (hU₀ : U₀ < 0) :
    (se_S hM).InextCausalCurveIn ((se_S hM).D (range (se_Ost hM hr₀))) where
  γ := sr_γ hU₀
  cont := Continuous.subtype_mk (by fun_prop) _
  mem := fun t => by rw [sr_D_eq hM hr₀]; exact hU₀
  brk := ∅
  brk_fin := fun _ _ => by simp
  causal := fun t _ => ⟨(sr_γ_vel hU₀ t).1, by
    rw [(sr_γ_vel hU₀ t).2, sr_futCausal_iff]
    exact ⟨le_rfl, (Real.exp_pos t).le, by simp [Real.exp_pos]⟩⟩
  inext_future := by
    rintro ⟨p, -, hp⟩
    have h : Tendsto (fun t => ((sr_γ hU₀ t : seW) : P).2) atTop (𝓝 (p : P).2) :=
      ((continuous_snd.comp continuous_subtype_val).tendsto p).comp hp
    exact not_tendsto_nhds_of_tendsto_atTop Real.tendsto_exp_atTop _ h
  inext_past := by
    rintro ⟨p, -, hp⟩
    have h : Tendsto (fun t => ((sr_γ hU₀ t : seW) : P).2) atBot (𝓝 (p : P).2) :=
      ((continuous_snd.comp continuous_subtype_val).tendsto p).comp hp
    have h0 : Tendsto (fun t => ((sr_γ hU₀ t : seW) : P).2) atBot (𝓝 0) := Real.tendsto_exp_atBot
    exact p.2.1.ne' (tendsto_nhds_unique h h0)

lemma sr_curve_γ {r₀ : ℝ} (hr₀ : 2 * M < r₀) {U₀ : ℝ} (hU₀ : U₀ < 0) (t : ℝ) :
    ((sr_curve hM hr₀ hU₀).γ t : P) = (U₀, Real.exp t) := rfl

/-- Along the witness, `u = −4M log(−U₀)` is constant and `r > 0`: `Θ_ret > −4Ma log(−U₀)`. -/
lemma sr_Θ_curve_gt {r₀ : ℝ} (hr₀ : 2 * M < r₀) {U₀ : ℝ} (hU₀ : U₀ < 0) {a η : ℝ} (ha : 0 < a)
    (hη : 0 < η) (t : ℝ) :
    a * (-4 * M * Real.log (-U₀)) < sr_Θ M a η ((sr_curve hM hr₀ hU₀).γ t) := by
  have hr : 0 < se_r M ((sr_curve hM hr₀ hU₀).γ t) :=
    (sk_rK_spec hM ((sr_curve hM hr₀ hU₀).γ t).2.2).1
  show a * (-4 * M * Real.log (-U₀)) <
    a * (-4 * M * Real.log (-U₀) + η * se_r M ((sr_curve hM hr₀ hU₀).γ t))
  nlinarith [mul_pos ha (mul_pos hη hr)]

/-- **ⓑ `sr_not_cauchy` (BUILT): the Cauchy clause fails for every `a, η > 0`.** The outgoing null
ray `γ(s) = (−1, eˢ)` is an inextendible causal curve of `D` (region I) along which
`Θ_ret = aη r > 0`; the level `0` is never met. -/
theorem sr_not_cauchy {r₀ : ℝ} (hr₀ : 2 * M < r₀) {a η : ℝ} (ha : 0 < a) (hη : 0 < η) :
    ∃ c : (se_S hM).InextCausalCurveIn ((se_S hM).D (range (se_Ost hM hr₀))),
      (∀ t, (c.γ t : P) = (-1, Real.exp t)) ∧ ∃ lev : ℝ, ∀ t, sr_Θ M a η (c.γ t) ≠ lev := by
  refine ⟨sr_curve hM hr₀ (U₀ := -1) (by norm_num), fun t => rfl, 0, fun t => ?_⟩
  have h := sr_Θ_curve_gt hM hr₀ (U₀ := -1) (by norm_num) ha hη t
  rw [neg_neg, Real.log_one, mul_zero, mul_zero] at h
  exact h.ne'

/-- **ⓑ Corollary: `Θ_ret` is not Cauchy temporal on region I**, for any `a, η > 0`. -/
theorem sr_not_isCauchy {r₀ : ℝ} (hr₀ : 2 * M < r₀) {a η : ℝ} (ha : 0 < a) (hη : 0 < η) :
    ¬ (se_S hM).IsCauchyTemporalOn ((se_S hM).D (range (se_Ost hM hr₀))) (sr_Θ M a η) := by
  intro h
  obtain ⟨c, -, lev, hlev⟩ := sr_not_cauchy hM hr₀ ha hη
  obtain ⟨t, ht, -⟩ := h.2 c lev
  exact hlev t ht

/-! ### ⓒ The future half -/

/-- **`U` and `V` are non-decreasing along every causal curve of `W`**, on `[0, ∞)` (campaign 81's
`mono_brk`: `φ(γ)′ = φ(γ′) ≥ 0` off the breaks, for `φ = dU, dV`). -/
lemma sr_coord_mono {U : Set seW} (c : (se_S hM).InextCausalCurveIn U) (φ : P →L[ℝ] ℝ)
    (hφ : ∀ v : P, 0 ≤ v.1 → 0 ≤ v.2 → 0 ≤ φ v) :
    MonotoneOn (fun t => φ (c.γ t : P)) (Ici 0) := by
  refine mono_brk c.brk_fin
    (φ.continuous.comp (continuous_subtype_val.comp c.cont)).continuousOn fun t _ ht => ?_
  obtain ⟨hd, hfc⟩ := c.causal t ht
  have h : HasDerivAt (fun s => φ (c.γ s : P)) (φ (MSpacetime.vel c.γ t)) t :=
    φ.hasFDerivAt.comp_hasDerivAt t (sr_hasDerivAt hd)
  obtain ⟨h1, h2, -⟩ := (sr_futCausal_iff hM _ _).1 hfc
  exact ⟨h.differentiableAt, by rw [h.deriv]; exact hφ _ h1 h2⟩

/-- **ⓒ `sr_future_diverges` (BUILT): `Θ_ret → +∞` along every inextendible causal curve of
region I**, for every `a, η > 0` (no bound on `η` is used). `U`, `V` are non-decreasing; with
`U → L ≤ 0`: if `L < 0` and `V` is bounded, the curve converges in `D` (excluded); if `L < 0` and
`V → ∞`, then `h(r) = −UV ≥ (−L)V → ∞`, so `r → ∞` while `log(−U) ≤ log(−U(0))`; if `L = 0`,
`−log(−U) → ∞` while `r > 0`. -/
theorem sr_future_diverges {r₀ : ℝ} (hr₀ : 2 * M < r₀) {a η : ℝ} (ha : 0 < a) (hη : 0 < η)
    (c : (se_S hM).InextCausalCurveIn ((se_S hM).D (range (se_Ost hM hr₀)))) :
    Tendsto (fun t => sr_Θ M a η (c.γ t)) atTop atTop := by
  set U : ℝ → ℝ := fun t => (c.γ t : P).1 with hUdef
  set V : ℝ → ℝ := fun t => (c.γ t : P).2 with hVdef
  have hUneg : ∀ t, U t < 0 := fun t => by
    exact (Set.ext_iff.1 (sr_D_eq hM hr₀) (c.γ t)).1 (c.mem t)
  have hVpos : ∀ t, 0 < V t := fun t => (c.γ t).2.1
  have hUm : MonotoneOn U (Ici 0) := sr_coord_mono hM c (fst ℝ ℝ ℝ) fun v h1 _ => h1
  have hVm : MonotoneOn V (Ici 0) := sr_coord_mono hM c (snd ℝ ℝ ℝ) fun v _ h2 => h2
  set U' : ℝ → ℝ := fun t => U (max t 0) with hU'def
  set V' : ℝ → ℝ := fun t => V (max t 0) with hV'def
  have hU'm : Monotone U' := fun s t hst =>
    hUm (mem_Ici.2 (le_max_right s 0)) (mem_Ici.2 (le_max_right t 0)) (max_le_max hst le_rfl)
  have hV'm : Monotone V' := fun s t hst =>
    hVm (mem_Ici.2 (le_max_right s 0)) (mem_Ici.2 (le_max_right t 0)) (max_le_max hst le_rfl)
  have hevU : U' =ᶠ[atTop] U := by
    filter_upwards [eventually_ge_atTop 0] with t ht
    simp only [U', max_eq_left ht]
  have hevV : V' =ᶠ[atTop] V := by
    filter_upwards [eventually_ge_atTop 0] with t ht
    simp only [V', max_eq_left ht]
  have hrpos : ∀ t, 0 < se_r M (c.γ t) := fun t => (sk_rK_spec hM (c.γ t).2.2).1
  have hΘ : ∀ t, sr_Θ M a η (c.γ t) = a * (-4 * M * Real.log (-U t) + η * se_r M (c.γ t)) :=
    fun t => rfl
  have hUbdd : BddAbove (range U') := ⟨0, by rintro _ ⟨t, rfl⟩; exact (hUneg _).le⟩
  set LU := ⨆ t, U' t with hLUdef
  have hLU : Tendsto U' atTop (𝓝 LU) := tendsto_atTop_ciSup hU'm hUbdd
  have hLU0 : LU ≤ 0 := ciSup_le fun t => (hUneg _).le
  have hUle : ∀ t, U' t ≤ LU := fun t => le_ciSup hUbdd t
  rcases hLU0.lt_or_eq with hLUn | hLU0'
  · by_cases hVb : BddAbove (range V')
    · -- bounded monotone limits land in `D`: excluded
      exfalso
      set LV := ⨆ t, V' t with hLVdef
      have hLV : Tendsto V' atTop (𝓝 LV) := tendsto_atTop_ciSup hV'm hVb
      have hLVpos : 0 < LV := lt_of_lt_of_le (hVpos (max 0 0)) (le_ciSup hVb 0)
      have hpW : ((LU, LV) : P) ∈ seWS := ⟨hLVpos, by show LU * LV < 1; nlinarith⟩
      apply c.inext_future
      refine ⟨⟨(LU, LV), hpW⟩, ?_, ?_⟩
      · rw [sr_D_eq hM hr₀]; exact hLUn
      · rw [tendsto_subtype_rng]
        exact (hLU.congr' hevU).prodMk_nhds (hLV.congr' hevV)
    · -- `V → ∞` with `U ≤ L < 0`: `r → ∞`
      have hVt : Tendsto V' atTop atTop := tendsto_atTop_atTop_of_monotone hV'm fun b => by
        by_contra h; push Not at h
        exact hVb ⟨b, by rintro _ ⟨t, rfl⟩; exact (h t).le⟩
      have hVt' : Tendsto V atTop atTop := hVt.congr' hevV
      have hr : Tendsto (fun t => se_r M (c.γ t)) atTop atTop := by
        rw [Filter.tendsto_atTop]
        intro R
        set R' := max R 1
        have hR' : 0 < R' := lt_of_lt_of_le one_pos (le_max_right _ _)
        have h1 : Tendsto (fun t => (-LU) * V t) atTop atTop :=
          hVt'.const_mul_atTop (neg_pos.2 hLUn)
        filter_upwards [h1.eventually_gt_atTop (hK M R'), eventually_ge_atTop 0] with t ht ht0
        have hUt : U t ≤ LU := by
          have := hUle t; simp only [U', max_eq_left ht0] at this; exact this
        have hh : hK M (se_r M (c.γ t)) = -(U t * V t) := (sk_rK_spec hM (c.γ t).2.2).2
        have hVt0 := hVpos t
        have hkey : hK M R' < hK M (se_r M (c.γ t)) := by
          rw [hh]; nlinarith
        by_contra hlt; push Not at hlt
        have hle : se_r M (c.γ t) ≤ R' := le_trans hlt.le (le_max_left R 1)
        have := (hK_strictMonoOn hM).monotoneOn (mem_Ici.2 (hrpos t).le) (mem_Ici.2 hR'.le) hle
        linarith
      have hlow : ∀ᶠ t in atTop,
          a * (-4 * M * Real.log (-U 0)) + (a * η) * se_r M (c.γ t) ≤ sr_Θ M a η (c.γ t) := by
        filter_upwards [eventually_ge_atTop 0] with t ht0
        have hU0t : U 0 ≤ U t := hUm (mem_Ici.2 le_rfl) (mem_Ici.2 ht0) ht0
        have hlog : Real.log (-U t) ≤ Real.log (-U 0) :=
          Real.log_le_log (neg_pos.2 (hUneg t)) (by linarith)
        rw [hΘ]
        nlinarith [mul_nonneg (mul_pos ha hM).le (sub_nonneg.2 hlog)]
      exact tendsto_atTop_mono' atTop hlow
        (tendsto_atTop_add_const_left _ _ (hr.const_mul_atTop (mul_pos ha hη)))
  · -- `U → 0⁻`: `−log(−U) → ∞`
    rw [hLU0'] at hLU
    have hU0 : Tendsto U atTop (𝓝 0) := hLU.congr' hevU
    have hneg : Tendsto (fun t => -U t) atTop (𝓝[>] 0) := by
      refine tendsto_nhdsWithin_iff.2 ⟨?_, Eventually.of_forall fun t => neg_pos.2 (hUneg t)⟩
      simpa using hU0.neg
    have hlog : Tendsto (fun t => -Real.log (-U t)) atTop atTop :=
      tendsto_neg_atBot_atTop.comp (Real.tendsto_log_nhdsGT_zero.comp hneg)
    have hlow : ∀ t, (a * (4 * M)) * (-Real.log (-U t)) ≤ sr_Θ M a η (c.γ t) := fun t => by
      rw [hΘ]; nlinarith [mul_pos ha (mul_pos hη (hrpos t))]
    exact tendsto_atTop_mono hlow (hlog.const_mul_atTop (mul_pos ha (by positivity)))

/-! ### Non-vacuity -/

/-- **Non-vacuity (BUILT)** at `M = 1`, `r₀ = 4`, `a = 1`: ⓑ's witness exists (the null ray
`(−1, eᵗ)`, with level `0` missed) and the Cauchy clause fails at `η = 1`; `Θ_ret` is temporal at
`η = 1` (so ⓐ's hypotheses are met); temporality fails at `η = 3` (at `r = 6`); and `Θ_ret → ∞`
along the witness. -/
theorem sr_nonvacuous :
    (∃ c : (se_S one_pos).InextCausalCurveIn
        ((se_S one_pos).D (range (se_Ost one_pos (r₀ := 4) (by norm_num)))),
      (∀ t, (c.γ t : P) = (-1, Real.exp t)) ∧ (∀ t, sr_Θ 1 1 1 (c.γ t) ≠ 0) ∧
      Tendsto (fun t => sr_Θ 1 1 1 (c.γ t)) atTop atTop) ∧
    ¬ (se_S one_pos).IsCauchyTemporalOn
      ((se_S one_pos).D (range (se_Ost one_pos (r₀ := 4) (by norm_num)))) (sr_Θ 1 1 1) ∧
    (se_S one_pos).IsTemporalOn
      ((se_S one_pos).D (range (se_Ost one_pos (r₀ := 4) (by norm_num)))) (sr_Θ 1 1 1) ∧
    (∃ x ∈ (se_S one_pos).D (range (se_Ost one_pos (r₀ := 4) (by norm_num))), se_r 1 x = 6 ∧
      ¬ 0 < MSpacetime.dfun (sr_Θ 1 1 3) x ((1 : ℝ), (0 : ℝ))) := by
  have hr₀ : 2 * (1 : ℝ) < 4 := by norm_num
  refine ⟨⟨sr_curve one_pos hr₀ (U₀ := -1) (by norm_num), fun t => rfl, fun t => ?_,
    sr_future_diverges one_pos hr₀ one_pos one_pos _⟩,
    sr_not_isCauchy one_pos hr₀ one_pos one_pos,
    sr_temporal one_pos hr₀ one_pos one_pos (by norm_num), ?_⟩
  · have h := sr_Θ_curve_gt one_pos hr₀ (U₀ := -1) (by norm_num) one_pos one_pos t
    rw [neg_neg, Real.log_one, mul_zero, mul_zero] at h
    exact h.ne'
  · obtain ⟨⟨x, hx, hr, -, hd⟩, -⟩ :=
      sr_not_temporal one_pos hr₀ (a := 1) (η := 3) (by norm_num)
    refine ⟨x, hx, by rw [hr]; norm_num, by rw [hd]; exact lt_irrefl 0⟩

end SRModel

/-! ## NEW (campaign 100): a `ConformalExtension` of Schwarzschild's `W` into the flat `S̃` -/

section SXConformal
open Manifold
set_option linter.unusedSectionVars false

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
variable {N : Type*} [TopologicalSpace N] [ChartedSpace E N] [IsManifold 𝓘(ℝ, E) 1 N]
variable {Ñ : Type*} [TopologicalSpace Ñ] [ChartedSpace E Ñ] [IsManifold 𝓘(ℝ, E) 1 Ñ]

namespace MSpacetime

/-- **Campaign 91's headline (copied from `ConeDisjoint.lean`): `mx_prop_causal_alignment` with an
eighth conjunct**, `∂J⁻(O τ) ∩ ∂J⁻(𝒥⁺) = ∅` for every `τ`, and no new hypothesis. -/
theorem cd_prop_causal_alignment [T2Space N] {S : MSpacetime E N} {St : MSpacetime E Ñ}
    (hL : S.LocallyOneChart) (hLt : St.LocallyOneChart) (X : ConformalExtension S St)
    {𝒥 : Set Ñ} (h𝒥 : 𝒥 ⊆ St.M) {J : Set N} {O : ℝ → N} (hOD : S.IpastSet (range O) = S.D J)
    (hmono : ∀ s t : ℝ, s < t → S.Chr (O s) (O t)) (hJM : J ⊆ S.M)
    (hI : S.IpastSet (range O) = X.ι ⁻¹' St.IpastSet 𝒥)
    (hHM : frontier (X.ι ⁻¹' St.JpastSet 𝒥) ⊆ S.M)
    {Θ : N → ℝ} {c : ℝ} (hΘ : S.IsCauchyTemporalOn (S.D J) Θ) (hadapt : ∀ τ, Θ (O τ) = τ + c) :
    S.H J = frontier (X.ι ⁻¹' St.JpastSet 𝒥) ∧
    S.SublevelProper J Θ ∧
    KLi (S.slice J Θ) = frontier (X.ι ⁻¹' St.JpastSet 𝒥) ∧
    KLs (S.slice J Θ) = frontier (X.ι ⁻¹' St.JpastSet 𝒥) ∧
    KLi (S.cone O) = frontier (X.ι ⁻¹' St.JpastSet 𝒥) ∧
    KLs (S.cone O) = frontier (X.ι ⁻¹' St.JpastSet 𝒥) ∧
    (∀ q ∈ frontier (X.ι ⁻¹' St.JpastSet 𝒥), ∀ (ℓ n : N → E) (L : Filter N) (C : ℝ) (ℓ₀ : E),
      L ≤ 𝓝 q →
      (∀ᶠ x in L, TCF.FrameHyp (S.gE x) (ℓ x) (n x) (dcov Θ x)) →
      (∀ᶠ x in L, ‖dchartL q x (n x)‖ ≤ C) →
      Tendsto (fun x => dchartL q x (ℓ x)) L (𝓝 ℓ₀) →
      Tendsto (fun x => dcov Θ x (ℓ x) / dcov Θ x (n x)) L (𝓝 0) →
      Tendsto (fun x => (dcov Θ x (n x))⁻¹ • covCh Θ q x) L (𝓝 (-(S.gE q ℓ₀)))) ∧
    ∀ τ, S.cone O τ ∩ frontier (X.ι ⁻¹' St.JpastSet 𝒥) = ∅ := by
  obtain ⟨h0, h1, h2, h3, h4, h5, h6⟩ :=
    mx_prop_causal_alignment hL hLt X h𝒥 hOD hmono hJM hI hHM hΘ hadapt
  refine ⟨h0, h1, h2, h3, h4, h5, h6, ?_⟩
  rw [← h0] at hHM ⊢
  exact cd_cone_disjoint hL hOD hmono hJM hHM hΘ

end MSpacetime

end SXConformal

namespace SXModel
open Model NModel SEModel Kruskal Manifold ContinuousLinearMap TopologicalSpace

variable {M : ℝ} (hM : 0 < M)

/-! ### ① The extension `ι = cz_fB ∘ val : W → P` -/

/-- **The embedding** `ι : W → P`, `(U, V) ↦ (arctan U, arctan V)`. -/
noncomputable def sx_ι : seW → P := cz_fB ∘ Subtype.val

lemma sx_ι_apply (x : seW) : sx_ι x = (Real.arctan x.1.1, Real.arctan x.1.2) := rfl

/-- `ι` is an open embedding: an open inclusion followed by a homeomorphism onto `(−π/2, π/2)²`. -/
theorem sx_ι_isOpenEmbedding : IsOpenEmbedding sx_ι :=
  cz_fB_isOpenEmbedding.comp seW.isOpen.isOpenEmbedding_subtypeVal

/-- `ι` is `C¹`. -/
theorem sx_ι_contMDiff : ContMDiff 𝓘(ℝ, P) 𝓘(ℝ, P) 1 sx_ι :=
  (contMDiff_iff_contDiff.2 cz_fB_contDiff).comp contMDiff_subtype_val

/-- **`Dι = diag(1/(1+U²), 1/(1+V²))`**, through `se_dchart` (the inclusion is the chart). -/
theorem sx_dι_eq (x : seW) (v : P) : mx_dι sx_ι x v = cz_DfB x.1 v := by
  have hval : MDifferentiableAt 𝓘(ℝ, P) 𝓘(ℝ, P) (Subtype.val : seW → P) x :=
    contMDiff_subtype_val.mdifferentiableAt one_ne_zero
  have hf : MDifferentiableAt 𝓘(ℝ, P) 𝓘(ℝ, P) cz_fB x.1 :=
    mdifferentiableAt_iff_differentiableAt.2 (cz_fB_hasFDerivAt _).differentiableAt
  have h1 : mx_dι sx_ι x = (mx_dι (E := P) cz_fB x.1).comp
      (mx_dι (E := P) (Subtype.val : seW → P) x) := by
    show mfderiv 𝓘(ℝ, P) 𝓘(ℝ, P) (cz_fB ∘ Subtype.val) x = _
    rw [mfderiv_comp x hf hval]; rfl
  have h2 : mx_dι (E := P) cz_fB x.1 = cz_DfB x.1 := by
    show mfderiv 𝓘(ℝ, P) 𝓘(ℝ, P) cz_fB x.1 = _
    rw [mfderiv_eq_fderiv]; exact (cz_fB_hasFDerivAt _).fderiv
  have h3 : mx_dι (E := P) (Subtype.val : seW → P) x v = v := by
    show mfderiv 𝓘(ℝ, P) 𝓘(ℝ, P) (Subtype.val : seW → P) x v = v
    have e : (Subtype.val : seW → P) = (extChartAt 𝓘(ℝ, P) x : seW → P) := rfl
    rw [e]; exact se_dchart x x v
  rw [h1, ContinuousLinearMap.comp_apply, h3, h2]

/-- **The conformal factor** `Ω = (F (1+U²)(1+V²))^{−1/2}`. -/
noncomputable def sx_Ω (M : ℝ) (x : seW) : ℝ :=
  (Real.sqrt (FS M x.1 * ((1 + x.1.1 ^ 2) * (1 + x.1.2 ^ 2))))⁻¹

include hM in
lemma sx_F_pos (x : seW) : 0 < FS M x.1 := sk_FS_pos hM x.2.2

include hM in
theorem sx_Ω_pos (x : seW) : 0 < sx_Ω M x :=
  inv_pos.2 (Real.sqrt_pos.2 (mul_pos (sx_F_pos hM x) (by positivity)))

include hM in
theorem sx_Ω_sq (x : seW) :
    sx_Ω M x ^ 2 = 1 / (FS M x.1 * ((1 + x.1.1 ^ 2) * (1 + x.1.2 ^ 2))) := by
  rw [sx_Ω, inv_pow, Real.sq_sqrt (mul_pos (sx_F_pos hM x) (by positivity)).le, one_div]

/-- **① The conformal extension of Schwarzschild's `W` into the flat `S̃` (BUILT): every field.** -/
noncomputable def sx_ext : ConformalExtension (se_S hM) cz_St where
  ι := sx_ι
  isOpenEmbedding := sx_ι_isOpenEmbedding
  contMDiff := sx_ι_contMDiff
  Ω := sx_Ω M
  Ω_pos := sx_Ω_pos hM
  conformal := fun x v w => by
    rw [se_S, MSpacetime.cz_scale_gE, sx_dι_eq, sx_dι_eq, sx_Ω_sq hM]
    show gM (cz_DfB x.1 v) (cz_DfB x.1 w) = _ * (FS M x.1 * gM v w)
    rw [cz_gM_DfB]
    have h0 : FS M x.1 ≠ 0 := (sx_F_pos hM x).ne'
    have h1 : (1 + x.1.1 ^ 2) ≠ 0 := by positivity
    have h2 : (1 + x.1.2 ^ 2) ≠ 0 := by positivity
    field_simp
  timeOrient := fun x _ => by
    show mink.FutTimelike (sx_ι x) (mx_dι sx_ι x ((1, 1) : P))
    rw [sx_dι_eq, futTimelike_iff, cz_DfB_apply]
    exact ⟨by simp only [mul_one]; positivity, by simp only [mul_one]; positivity⟩
  maps_M := subset_univ _

lemma sx_ext_ι : (sx_ext hM).ι = cz_fB ∘ Subtype.val := rfl

lemma sx_ext_Ω_sq (x : seW) :
    (sx_ext hM).Ω x ^ 2 = 1 / (FS M x.1 * ((1 + x.1.1 ^ 2) * (1 + x.1.2 ^ 2))) :=
  sx_Ω_sq hM x

/-- `Dι T = (1/(1+U²), 1/(1+V²))`. -/
theorem sx_dι_T (x : seW) :
    mx_dι (E := P) (sx_ext hM).ι x ((se_S hM).T x) = (1 / (1 + x.1.1 ^ 2), 1 / (1 + x.1.2 ^ 2)) := by
  show mx_dι sx_ι x ((1, 1) : P) = _
  rw [sx_dι_eq, cz_DfB_apply, mul_one, mul_one]

/-! ### ② `hI`: `I⁻(O) = ι⁻¹ Ĩ⁻(𝒥⁺)` -/

/-- **② `hI` (BUILT):** `I⁻(O) = D = {U < 0}` (region I) is `ι⁻¹ {u < 0, v < π/2}`. -/
theorem sx_hI {r₀ : ℝ} (hr₀ : 2 * M < r₀) :
    (se_S hM).IpastSet (range (se_Ost hM hr₀)) = (sx_ext hM).ι ⁻¹' cz_St.IpastSet cz_scri := by
  have hD : (se_S hM).D (range (se_Ost hM hr₀)) = {x | x.1.1 < 0} :=
    (se_foundation hM (se_a_pos hM hr₀) (se_k_pos hM hr₀)).2.2.2.2.2.1
  show (se_S hM).D (range (se_Ost hM hr₀)) = _
  rw [hD]
  ext x
  rw [mem_preimage, cz_mem_Ipast_scri, sx_ext_ι, Function.comp_apply]
  show x.1.1 < 0 ↔ Real.arctan x.1.1 < 0 ∧ Real.arctan x.1.2 < Real.pi / 2
  exact ⟨fun h => ⟨(cz_arctan_neg_iff _).2 h, Real.arctan_lt_pi_div_two _⟩,
    fun h => (cz_arctan_neg_iff _).1 h.1⟩

/-! ### ③ The headline -/

/-- **③ `prop:causal-alignment` on Schwarzschild with `𝓗⁺ := ∂J⁻(𝒥⁺)` (BUILT).** For `M > 0`,
`r₀ > 2M`, the static observer `O = se_Ost` at `r₀`, `J = range O`, `Θ = √(1 − 2M/r₀) t` (`c = 0`),
the conformal extension `sx_ext` into the flat `S̃` and `𝒥⁺ = cz_scri`: every conclusion of
`cd_prop_causal_alignment`, together with `∂J⁻(𝒥⁺) = {U = 0, V > 0}` in the plane (`r = 2M`). -/
theorem sx_prop_causal_alignment {r₀ : ℝ} (hr₀ : 2 * M < r₀) :
    (se_S hM).H (range (se_Ost hM hr₀)) =
      frontier ((sx_ext hM).ι ⁻¹' cz_St.JpastSet cz_scri) ∧
    Subtype.val '' frontier ((sx_ext hM).ι ⁻¹' cz_St.JpastSet cz_scri) =
      {p : P | p.1 = 0 ∧ 0 < p.2} ∧
    (∀ x ∈ frontier ((sx_ext hM).ι ⁻¹' cz_St.JpastSet cz_scri), se_r M x = 2 * M) ∧
    (se_S hM).SublevelProper (range (se_Ost hM hr₀)) (se_Θst M r₀) ∧
    KLi ((se_S hM).slice (range (se_Ost hM hr₀)) (se_Θst M r₀)) =
      frontier ((sx_ext hM).ι ⁻¹' cz_St.JpastSet cz_scri) ∧
    KLs ((se_S hM).slice (range (se_Ost hM hr₀)) (se_Θst M r₀)) =
      frontier ((sx_ext hM).ι ⁻¹' cz_St.JpastSet cz_scri) ∧
    KLi ((se_S hM).cone (se_Ost hM hr₀)) = frontier ((sx_ext hM).ι ⁻¹' cz_St.JpastSet cz_scri) ∧
    KLs ((se_S hM).cone (se_Ost hM hr₀)) = frontier ((sx_ext hM).ι ⁻¹' cz_St.JpastSet cz_scri) ∧
    (∀ q ∈ frontier ((sx_ext hM).ι ⁻¹' cz_St.JpastSet cz_scri),
      ∀ (ℓ n : seW → P) (L : Filter seW) (C : ℝ) (ℓ₀ : P), L ≤ 𝓝 q →
      (∀ᶠ x in L, TCF.FrameHyp ((se_S hM).gE x) (ℓ x) (n x) (dcov (se_Θst M r₀) x)) →
      (∀ᶠ x in L, ‖dchartL q x (n x)‖ ≤ C) →
      Tendsto (fun x => dchartL q x (ℓ x)) L (𝓝 ℓ₀) →
      Tendsto (fun x => dcov (se_Θst M r₀) x (ℓ x) / dcov (se_Θst M r₀) x (n x)) L (𝓝 0) →
      Tendsto (fun x => (dcov (se_Θst M r₀) x (n x))⁻¹ • covCh (se_Θst M r₀) q x) L
        (𝓝 (-((se_S hM).gE q ℓ₀)))) ∧
    (∀ τ, (se_S hM).cone (se_Ost hM hr₀) τ ∩
      frontier ((sx_ext hM).ι ⁻¹' cz_St.JpastSet cz_scri) = ∅) := by
  have ha := se_a_pos hM hr₀
  have hk := se_k_pos hM hr₀
  obtain ⟨-, hL, -, -, hOD, -, -, hmono, hJM, -, -, -, -, -⟩ := se_foundation hM ha hk
  obtain ⟨hΘ, hO, -, -, hHv, hr, -⟩ := se_headline hM hr₀
  have hadapt : ∀ τ, se_Θst M r₀ (se_Ost hM hr₀ τ) = τ + 0 := fun τ => by rw [add_zero]; exact hO τ
  obtain ⟨h0, h1, h2, h3, h4, h5, h6, h7⟩ := MSpacetime.cd_prop_causal_alignment
    (se_locallyOneChart hM) cz_locallyOneChart (sx_ext hM) (subset_univ _) hOD hmono hJM
    (sx_hI hM hr₀) (subset_univ _) hΘ hadapt
  refine ⟨h0, ?_, ?_, h1, h2, h3, h4, h5, h6, h7⟩
  · rw [← h0]; exact hHv
  · rw [← h0]; exact hr

/-- **Non-vacuity (BUILT):** at `M = 1`, `r₀ = 4`: `∂J⁻(𝒥⁺)` is non-empty (it contains `(0, 1)`),
`Ω` is not constant (`Ω(0, 1) ≠ Ω(0, 2)`: same `F`, since `UV = 0` at both, but `1 + V²` differs),
and `g` is not flat at `(0, 1)`. -/
theorem sx_nonvacuous :
    (frontier ((sx_ext one_pos).ι ⁻¹' cz_St.JpastSet cz_scri)).Nonempty ∧
    seP0 ∈ frontier ((sx_ext one_pos).ι ⁻¹' cz_St.JpastSet cz_scri) ∧
    (∃ x y : seW, (sx_ext one_pos).Ω x ≠ (sx_ext one_pos).Ω y) ∧
    hRep (se_S one_pos).g seP0 (0, 1) ≠ gM := by
  obtain ⟨h0, hv, -⟩ := sx_prop_causal_alignment one_pos (r₀ := 4) (by norm_num)
  have hP0 : seP0 ∈ frontier ((sx_ext one_pos).ι ⁻¹' cz_St.JpastSet cz_scri) := by
    have hm : ((0 : ℝ), (1 : ℝ)) ∈ Subtype.val ''
        frontier ((sx_ext one_pos).ι ⁻¹' cz_St.JpastSet cz_scri) := by
      rw [hv]; exact ⟨rfl, one_pos⟩
    obtain ⟨x, hx, hx1⟩ := hm
    have : x = seP0 := Subtype.ext hx1
    rwa [this] at hx
  obtain ⟨-, -, -, hflat, -⟩ := SEModel.se_nonvacuous
  let y : seW := ⟨((0 : ℝ), (2 : ℝ)), ⟨two_pos, by norm_num⟩⟩
  refine ⟨⟨seP0, hP0⟩, hP0, ⟨seP0, y, fun h => ?_⟩, hflat⟩
  have h2 : (sx_ext one_pos).Ω seP0 ^ 2 = (sx_ext one_pos).Ω y ^ 2 := by rw [h]
  rw [sx_ext_Ω_sq, sx_ext_Ω_sq] at h2
  have hF : FS 1 (seP0 : P) = FS 1 (y : P) := by
    show FS 1 ((0 : ℝ), (1 : ℝ)) = FS 1 ((0 : ℝ), (2 : ℝ))
    simp only [FS, rK, zero_mul]
  rw [← hF] at h2
  have hpos : 0 < FS 1 (seP0 : P) := sx_F_pos one_pos seP0
  change 1 / (FS 1 (seP0 : P) * ((1 + (0:ℝ) ^ 2) * (1 + (1:ℝ) ^ 2))) =
    1 / (FS 1 (seP0 : P) * ((1 + (0:ℝ) ^ 2) * (1 + (2:ℝ) ^ 2))) at h2
  field_simp at h2
  nlinarith

end SXModel

/-! ## Campaign 96's `KillingWhole.lean` kit (`ld_`, `kl_`, `kg_`, `kw_`), copied, names kept

Eight declarations shared with the campaign-68 kit above (`chartRep`, `hRep`, six `ld_`) were checked
textually identical (up to docstrings) and are kept once, above. -/

section KillingWholeKit

open scoped NNReal
set_option linter.unusedSectionVars false

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]

/-! ## Copied from `SmoothFlowProbe.lean` (steps 1, 2, 4(a)), renamed -/

/-- **1.** The first-order remainder of a `C¹` map is uniformly small on a closed ball. -/
theorem ld_remainder_unif (f : E → E) (hf : ContDiff ℝ 1 f) (x₀ : E) (R ε : ℝ) (hε : 0 < ε) :
    ∃ δ > 0, ∀ y ∈ closedBall x₀ R, ∀ z ∈ closedBall x₀ R, ‖y - z‖ < δ →
      ‖f y - f z - fderiv ℝ f z (y - z)‖ ≤ ε * ‖y - z‖ := by
  have hU : UniformContinuousOn (fderiv ℝ f) (closedBall x₀ (R + 1)) :=
    (isCompact_closedBall x₀ (R + 1)).uniformContinuousOn_of_continuous
      (hf.continuous_fderiv one_ne_zero).continuousOn
  obtain ⟨δ', hδ', hδ⟩ := Metric.uniformContinuousOn_iff.1 hU ε hε
  refine ⟨min δ' 1, by positivity, fun y hy z hz hyz => ?_⟩
  have hsub : ball z (min δ' 1) ⊆ closedBall x₀ (R + 1) := fun w hw => by
    rw [mem_closedBall] at hz ⊢; rw [mem_ball] at hw
    linarith [dist_triangle w z x₀, min_le_right δ' 1]
  have hz1 : z ∈ closedBall x₀ (R + 1) := hsub (mem_ball_self (by positivity))
  have hd : ∀ w ∈ ball z (min δ' 1), DifferentiableAt ℝ (fun w => f w - fderiv ℝ f z w) w :=
    fun w _ => (hf.differentiable one_ne_zero w).sub (fderiv ℝ f z).differentiableAt
  have hb : ∀ w ∈ ball z (min δ' 1), ‖fderiv ℝ (fun w => f w - fderiv ℝ f z w) w‖ ≤ ε := by
    intro w hw
    rw [fderiv_fun_sub (hf.differentiable one_ne_zero w) (fderiv ℝ f z).differentiableAt,
      ContinuousLinearMap.fderiv, ← dist_eq_norm]
    exact (hδ w (hsub hw) z hz1 (lt_of_lt_of_le (mem_ball.1 hw) (min_le_left _ _))).le
  have := Convex.norm_image_sub_le_of_norm_fderiv_le hd hb (convex_ball z (min δ' 1))
    (mem_ball_self (by positivity)) (by rw [mem_ball, dist_eq_norm]; exact hyz)
  rw [map_sub] at *
  convert this using 2
  abel

/-- **2.** The local flow of a `C¹` field, Lipschitz in the initial point. -/
theorem ld_local_flow (f : E → E) (hf : ContDiff ℝ 1 f) (x₀ : E) :
    ∃ τ > (0 : ℝ), ∃ r > (0 : ℝ), ∃ α : E → ℝ → E, ∃ L : ℝ≥0,
      (∀ x ∈ closedBall x₀ r, α x 0 = x ∧
        ∀ t ∈ Icc (-τ) τ, HasDerivWithinAt (α x) (f (α x t)) (Icc (-τ) τ) t) ∧
      ∀ t ∈ Icc (-τ) τ, LipschitzOnWith L (α · t) (closedBall x₀ r) := by
  obtain ⟨τ, hτ, a, r, L, K, hr, hPL⟩ := IsPicardLindelof.of_contDiffAt_one (hf.contDiffAt (x := x₀))
  obtain ⟨α, hα, L', hL'⟩ :=
    (hPL 0).exists_forall_mem_closedBall_eq_hasDerivWithinAt_lipschitzOnWith
  simp only [zero_sub, zero_add] at hα hL'
  exact ⟨τ, hτ, r, hr, α, L', hα, hL'⟩

/-- **4(a).** The trajectories from `closedBall x₀ r` over `[-τ, τ]` stay in one closed ball. -/
theorem ld_flow_bounded (f : E → E) (τ r : ℝ) (α : E → ℝ → E) (L : ℝ≥0) (x₀ : E)
    (hα : ∀ x ∈ closedBall x₀ r, α x 0 = x ∧
      ∀ t ∈ Icc (-τ) τ, HasDerivWithinAt (α x) (f (α x t)) (Icc (-τ) τ) t)
    (hL : ∀ t ∈ Icc (-τ) τ, LipschitzOnWith L (α · t) (closedBall x₀ r)) :
    ∃ R, ∀ x ∈ closedBall x₀ r, ∀ t ∈ Icc (-τ) τ, α x t ∈ closedBall x₀ R := by
  have hc : ContinuousOn (fun p : E × ℝ => α p.1 p.2) (closedBall x₀ r ×ˢ Icc (-τ) τ) :=
    continuousOn_prod_of_continuousOn_lipschitzOnWith _ L
      (fun x hx => fun t ht => ((hα x hx).2 t ht).continuousWithinAt) hL
  obtain ⟨R, hR⟩ := (((isCompact_closedBall x₀ r).prod isCompact_Icc).image_of_continuousOn
    hc).isBounded.subset_closedBall x₀
  exact ⟨R, fun x hx t ht => hR ⟨(x, t), ⟨hx, ht⟩, rfl⟩⟩

/-! ## A linear ODE on `[-T, T]` in one Picard–Lindelöf step, and a two-sided Grönwall -/

section Linear

variable {F : Type*} [NormedAddCommGroup F] [NormedSpace ℝ F]

/-- A linear ODE `W′ = A(t) W` with `‖A‖ ≤ M`, `M T ≤ 1/2`, has a solution on `[-T, T]` through `v`. -/
theorem ld_linear_exists [CompleteSpace F] (A : ℝ → F →L[ℝ] F) (T M : ℝ) (hT : 0 ≤ T) (hM : 0 ≤ M)
    (hMT : M * T ≤ 1 / 2) (hA : ContinuousOn A (Icc (-T) T))
    (hAM : ∀ t ∈ Icc (-T) T, ‖A t‖ ≤ M) (v : F) :
    ∃ W : ℝ → F, W 0 = v ∧
      ∀ t ∈ Icc (-T) T, HasDerivWithinAt W (A t (W t)) (Icc (-T) T) t := by
  have h0 : (0 : ℝ) ∈ Icc (-T) T := ⟨by linarith, hT⟩
  have hPL : IsPicardLindelof (fun t y => A t y) (⟨0, h0⟩ : Icc (-T) T) v
      ⟨‖v‖ + 1, by positivity⟩ 0 ⟨M * (2 * ‖v‖ + 1), by positivity⟩ ⟨M, hM⟩ := by
    refine ⟨fun t ht => ?_, fun y _ => ?_, fun t ht y hy => ?_, ?_⟩
    · refine LipschitzWith.lipschitzOnWith (LipschitzWith.of_dist_le_mul fun y z => ?_)
      rw [dist_eq_norm, dist_eq_norm, ← map_sub]
      exact (A t).le_of_opNorm_le (hAM t ht) _
    · exact hA.clm_apply continuousOn_const
    · have hy' : ‖y‖ ≤ 2 * ‖v‖ + 1 := by
        rw [Metric.mem_closedBall, dist_eq_norm] at hy
        have := norm_le_norm_add_norm_sub' y v
        have hy2 : ‖y - v‖ ≤ ‖v‖ + 1 := hy
        linarith
      exact ((A t).le_opNorm y).trans (mul_le_mul (hAM t ht) hy' (norm_nonneg _) hM)
    · show M * (2 * ‖v‖ + 1) * max (T - 0) (0 - -T) ≤ (‖v‖ + 1) - 0
      rw [sub_zero, zero_sub, neg_neg, max_self, sub_zero]
      nlinarith [norm_nonneg v, mul_le_mul_of_nonneg_right hMT (by positivity : 0 ≤ 2 * ‖v‖ + 1)]
  exact hPL.exists_eq_forall_mem_Icc_hasDerivWithinAt₀

/-- Grönwall forward on `[0, T]`, from a derivative within `[-T, T]`. -/
theorem ld_gronwall_fwd (e e' : ℝ → F) (T δ K c : ℝ)
    (he : ∀ s ∈ Icc (-T) T, HasDerivWithinAt e (e' s) (Icc (-T) T) s) (h0 : ‖e 0‖ ≤ δ)
    (hb : ∀ s ∈ Icc (-T) T, ‖e' s‖ ≤ K * ‖e s‖ + c) :
    ∀ s ∈ Icc 0 T, ‖e s‖ ≤ gronwallBound δ K c s := by
  intro s hs
  have hT : 0 ≤ T := hs.1.trans hs.2
  have hsub : Icc 0 T ⊆ Icc (-T) T := Icc_subset_Icc (by linarith) le_rfl
  have := norm_le_gronwallBound_of_norm_deriv_right_le (f := e) (f' := e') (a := 0) (b := T)
    (fun u hu => (he u (hsub hu)).continuousWithinAt.mono hsub)
    (fun u hu => (he u (hsub (Ico_subset_Icc_self hu))).mono_of_mem_nhdsWithin
      (mem_of_superset (Icc_mem_nhdsGE hu.2) (Icc_subset_Icc (by linarith [hu.1]) le_rfl)))
    h0 (fun u hu => hb u (hsub (Ico_subset_Icc_self hu))) s hs
  rwa [sub_zero] at this

/-- **Two-sided Grönwall.** On `[-T, T]`, from `‖e 0‖ ≤ δ` and `‖e′‖ ≤ K ‖e‖ + c`. -/
theorem ld_gronwall_symm (e e' : ℝ → F) (T δ K c : ℝ)
    (he : ∀ s ∈ Icc (-T) T, HasDerivWithinAt e (e' s) (Icc (-T) T) s) (h0 : ‖e 0‖ ≤ δ)
    (hb : ∀ s ∈ Icc (-T) T, ‖e' s‖ ≤ K * ‖e s‖ + c) :
    ∀ s ∈ Icc (-T) T, ‖e s‖ ≤ gronwallBound δ K c |s| := by
  intro s hs
  rcases le_total 0 s with h | h
  · rw [abs_of_nonneg h]; exact ld_gronwall_fwd e e' T δ K c he h0 hb s ⟨h, hs.2⟩
  · have hneg : ∀ u ∈ Icc (-T) T, -u ∈ Icc (-T) T := fun u hu => ⟨by linarith [hu.2], by linarith [hu.1]⟩
    have := ld_gronwall_fwd (fun u => e (-u)) (fun u => -e' (-u)) T δ K c
      (fun u hu => by
        have := (he (-u) (hneg u hu)).scomp u ((hasDerivAt_neg u).hasDerivWithinAt)
          (fun w hw => hneg w hw)
        simpa [Function.comp_def] using this)
      (by simpa using h0) (fun u hu => by simpa using hb (-u) (hneg u hu)) (-s)
      ⟨by linarith, by linarith [hs.1]⟩
    rw [abs_of_nonpos h]; simpa using this

end Linear

/-- The Grönwall bound with `δ = 0`, linear in `c`, uniformly on `[0, T]`. -/
theorem ld_gronwallBound_le (K c x T : ℝ) (hK : 0 < K) (hc : 0 ≤ c) (hxT : x ≤ T) :
    gronwallBound 0 K c x ≤ c * ((Real.exp (K * T) - 1) / K) := by
  rw [gronwallBound_of_K_ne_0 hK.ne']
  simp only [zero_mul, zero_add]
  calc c / K * (Real.exp (K * x) - 1) = c * ((Real.exp (K * x) - 1) / K) := by ring
    _ ≤ c * ((Real.exp (K * T) - 1) / K) := by
      gcongr

/-! ## The flow data -/

/-- A local flow of `f` near `x₀`, packaged: `α x t` for `x ∈ closedBall x₀ r`, `t ∈ [-τ, τ]`, Lipschitz in `x`,
inside `closedBall x₀ R` on which `‖Df‖ ≤ M`, with `M τ ≤ 1/2`. -/
structure FlowData (f : E → E) (x₀ : E) where
  τ : ℝ
  r : ℝ
  R : ℝ
  M : ℝ
  L : ℝ≥0
  α : E → ℝ → E
  τ_pos : 0 < τ
  r_pos : 0 < r
  M_pos : 0 < M
  Mτ : M * τ ≤ 1 / 2
  init : ∀ x ∈ closedBall x₀ r, α x 0 = x
  deriv : ∀ x ∈ closedBall x₀ r, ∀ t ∈ Icc (-τ) τ,
    HasDerivWithinAt (α x) (f (α x t)) (Icc (-τ) τ) t
  lip : ∀ t ∈ Icc (-τ) τ, LipschitzOnWith L (α · t) (closedBall x₀ r)
  mem : ∀ x ∈ closedBall x₀ r, ∀ t ∈ Icc (-τ) τ, α x t ∈ closedBall x₀ R
  dbound : ∀ y ∈ closedBall x₀ R, ‖fderiv ℝ f y‖ ≤ M

variable {f : E → E} {x₀ : E}

/-- Every `C¹` field has flow data at every point (Picard–Lindelöf, then shrink `τ`). -/
theorem ld_flowData_exists (hf : ContDiff ℝ 1 f) (x₀ : E) : Nonempty (FlowData f x₀) := by
  obtain ⟨τ₀, hτ₀, r, hr, α, L, hα, hL⟩ := ld_local_flow f hf x₀
  obtain ⟨R, hR⟩ := ld_flow_bounded f τ₀ r α L x₀ hα hL
  obtain ⟨C, hC⟩ := (isCompact_closedBall x₀ R).exists_bound_of_continuousOn
    (hf.continuous_fderiv one_ne_zero).continuousOn
  set M := max C 0 + 1 with hM
  have hM0 : 0 < M := by positivity
  set τ := min τ₀ (1 / (2 * M)) with hτ
  have hτ0 : 0 < τ := lt_min hτ₀ (by positivity)
  have hsub : Icc (-τ) τ ⊆ Icc (-τ₀) τ₀ :=
    Icc_subset_Icc (neg_le_neg (min_le_left _ _)) (min_le_left _ _)
  refine ⟨⟨τ, r, R, M, L, α, hτ0, hr, hM0, ?_, fun x hx => (hα x hx).1,
    fun x hx t ht => ((hα x hx).2 t (hsub ht)).mono hsub, fun t ht => hL t (hsub ht),
    fun x hx t ht => hR x hx t (hsub ht), fun y hy => (hC y hy).trans ?_⟩⟩
  · calc M * τ ≤ M * (1 / (2 * M)) := mul_le_mul_of_nonneg_left (min_le_right _ _) hM0.le
      _ = 1 / 2 := by field_simp
  · rw [hM]; linarith [le_max_left C 0]

namespace FlowData

variable (D : FlowData f x₀)

/-- `W` solves the variational equation along `α x`. -/
def IsVar (x : E) (W : ℝ → E →L[ℝ] E) : Prop :=
  W 0 = ContinuousLinearMap.id ℝ E ∧ ∀ t ∈ Icc (-D.τ) D.τ,
    HasDerivWithinAt W ((fderiv ℝ f (D.α x t)).comp (W t)) (Icc (-D.τ) D.τ) t

open Classical in
/-- The solution of the variational equation along `α x` (junk off `closedBall x₀ r`). -/
noncomputable def J (x : E) : ℝ → E →L[ℝ] E := if h : ∃ W, D.IsVar x W then h.choose else 0

theorem ld_Icc_mem {t : ℝ} (ht : t ∈ Icc (-D.τ) D.τ) : |t| ≤ D.τ := abs_le.2 ht

theorem ld_alpha_continuousOn (x : E) (hx : x ∈ closedBall x₀ D.r) :
    ContinuousOn (D.α x) (Icc (-D.τ) D.τ) :=
  fun t ht => (D.deriv x hx t ht).continuousWithinAt

theorem ld_var_exists (hf : ContDiff ℝ 1 f) (x : E) (hx : x ∈ closedBall x₀ D.r) :
    ∃ W, D.IsVar x W := by
  obtain ⟨W, hW0, hW⟩ := ld_linear_exists
    (fun t => ContinuousLinearMap.compL ℝ E E E (fderiv ℝ f (D.α x t))) D.τ D.M D.τ_pos.le
    D.M_pos.le D.Mτ
    ((ContinuousLinearMap.compL ℝ E E E).continuous.comp_continuousOn
      ((hf.continuous_fderiv one_ne_zero).comp_continuousOn (D.ld_alpha_continuousOn x hx)))
    (fun t ht => ContinuousLinearMap.opNorm_le_bound _ D.M_pos.le fun W =>
      ((ContinuousLinearMap.opNorm_comp_le _ _).trans
        (mul_le_mul_of_nonneg_right (D.dbound _ (D.mem x hx t ht)) (norm_nonneg _))))
    (ContinuousLinearMap.id ℝ E)
  exact ⟨W, hW0, fun t ht => by simpa using hW t ht⟩

theorem ld_J_spec (hf : ContDiff ℝ 1 f) (x : E) (hx : x ∈ closedBall x₀ D.r) :
    D.IsVar x (D.J x) := by
  have h := D.ld_var_exists hf x hx
  unfold J; rw [dite_eq_left h]; exact h.choose_spec

/-- The constant of the Grönwall bound on `[-τ, τ]`. -/
noncomputable def C : ℝ := (Real.exp (D.M * D.τ) - 1) / D.M

theorem ld_C_nonneg : 0 ≤ D.C := by
  unfold C
  have : 1 ≤ Real.exp (D.M * D.τ) := Real.one_le_exp (by nlinarith [D.M_pos, D.τ_pos])
  exact div_nonneg (by linarith) D.M_pos.le

theorem ld_gb_le {c s : ℝ} (hc : 0 ≤ c) (hs : s ∈ Icc (-D.τ) D.τ) :
    gronwallBound 0 D.M c |s| ≤ c * D.C :=
  ld_gronwallBound_le _ _ _ _ D.M_pos hc (D.ld_Icc_mem hs)

/-- `‖J x s‖ ≤ exp (M τ)` on `[-τ, τ]`. -/
theorem ld_J_norm_le (hf : ContDiff ℝ 1 f) (x : E) (hx : x ∈ closedBall x₀ D.r)
    (s : ℝ) (hs : s ∈ Icc (-D.τ) D.τ) : ‖D.J x s‖ ≤ Real.exp (D.M * D.τ) := by
  obtain ⟨h0, hd⟩ := D.ld_J_spec hf x hx
  have := ld_gronwall_symm (D.J x) (fun t => (fderiv ℝ f (D.α x t)).comp (D.J x t)) D.τ 1 D.M 0 hd
    (by rw [h0]; exact ContinuousLinearMap.norm_id_le)
    (fun t ht => by
      rw [add_zero]
      exact (ContinuousLinearMap.opNorm_comp_le _ _).trans
        (mul_le_mul_of_nonneg_right (D.dbound _ (D.mem x hx t ht)) (norm_nonneg _))) s hs
  rw [gronwallBound_ε0, one_mul] at this
  exact this.trans (Real.exp_le_exp.2 (mul_le_mul_of_nonneg_left (D.ld_Icc_mem hs) D.M_pos.le))

/-- **Grönwall #1, uniform in time.** `‖α y s − α x s − J x s (y − x)‖ ≤ ε ‖y − x‖` for `y` near `x`,
for every `s ∈ [-τ, τ]` at once. -/
theorem ld_remainder_uniform (hf : ContDiff ℝ 1 f) (x : E) (hx : x ∈ closedBall x₀ D.r)
    (ε : ℝ) (hε : 0 < ε) :
    ∃ δ > 0, ∀ y ∈ closedBall x₀ D.r, ‖y - x‖ < δ → ∀ s ∈ Icc (-D.τ) D.τ,
      ‖D.α y s - D.α x s - D.J x s (y - x)‖ ≤ ε * ‖y - x‖ := by
  set ε' := ε / (((D.L : ℝ) + 1) * (D.C + 1)) with hε'
  have hC := D.ld_C_nonneg
  have hε'0 : 0 < ε' := by positivity
  obtain ⟨δ₀, hδ₀, hrem⟩ := ld_remainder_unif f hf x₀ D.R ε' hε'0
  refine ⟨δ₀ / ((D.L : ℝ) + 1), by positivity, fun y hy hyx s hs => ?_⟩
  obtain ⟨hJ0, hJd⟩ := D.ld_J_spec hf x hx
  have hlip : ∀ s ∈ Icc (-D.τ) D.τ, ‖D.α y s - D.α x s‖ ≤ D.L * ‖y - x‖ :=
    fun s hs => (D.lip s hs).norm_sub_le hy hx
  have hclose : ∀ s ∈ Icc (-D.τ) D.τ, ‖D.α y s - D.α x s‖ < δ₀ := fun s hs => by
    have h1 := hlip s hs
    have h2 : ((D.L : ℝ) + 1) * ‖y - x‖ < δ₀ := by
      rwa [lt_div_iff₀ (by positivity), mul_comm] at hyx
    nlinarith [norm_nonneg (y - x)]
  have key := ld_gronwall_symm (fun s => D.α y s - D.α x s - D.J x s (y - x))
    (fun s => f (D.α y s) - f (D.α x s) - (fderiv ℝ f (D.α x s)).comp (D.J x s) (y - x))
    D.τ 0 D.M (ε' * (D.L * ‖y - x‖))
    (fun s hs => by
      have := ((D.deriv y hy s hs).fun_sub (D.deriv x hx s hs)).fun_sub
        ((hJd s hs).clm_apply (hasDerivWithinAt_const s _ (y - x)))
      simpa using this)
    (by simp [D.init y hy, D.init x hx, hJ0])
    (fun s hs => by
      have hsplit : f (D.α y s) - f (D.α x s) - (fderiv ℝ f (D.α x s)).comp (D.J x s) (y - x) =
          (f (D.α y s) - f (D.α x s) - fderiv ℝ f (D.α x s) (D.α y s - D.α x s)) +
          fderiv ℝ f (D.α x s) (D.α y s - D.α x s - D.J x s (y - x)) := by
        simp only [ContinuousLinearMap.comp_apply, map_sub]; abel
      rw [hsplit]
      refine (norm_add_le _ _).trans ?_
      have h1 := hrem _ (D.mem y hy s hs) _ (D.mem x hx s hs) (hclose s hs)
      have h2 := (fderiv ℝ f (D.α x s)).le_opNorm (D.α y s - D.α x s - D.J x s (y - x))
      have h3 := D.dbound _ (D.mem x hx s hs)
      have h4 := hlip s hs
      nlinarith [norm_nonneg (D.α y s - D.α x s - D.J x s (y - x)), norm_nonneg (D.α y s - D.α x s)])
    s hs
  refine key.trans ((D.ld_gb_le (by positivity) hs).trans ?_)
  have : ε' * D.L * D.C ≤ ε := by
    rw [hε']
    rw [div_mul_eq_mul_div, div_mul_eq_mul_div, div_le_iff₀ (by positivity)]
    nlinarith [mul_le_mul (le_add_of_nonneg_right zero_le_one : (D.L : ℝ) ≤ D.L + 1)
      (le_add_of_nonneg_right zero_le_one : D.C ≤ D.C + 1) hC (by positivity)]
  nlinarith [norm_nonneg (y - x)]

/-- **Grönwall #2, uniform in time.** `‖J y s − J x s‖ ≤ ε` for `y` near `x`, every `s ∈ [-τ, τ]`. -/
theorem ld_J_uniform (hf : ContDiff ℝ 1 f) (x : E) (hx : x ∈ closedBall x₀ D.r)
    (ε : ℝ) (hε : 0 < ε) :
    ∃ δ > 0, ∀ y ∈ closedBall x₀ D.r, ‖y - x‖ < δ → ∀ s ∈ Icc (-D.τ) D.τ,
      ‖D.J y s - D.J x s‖ ≤ ε := by
  set B := Real.exp (D.M * D.τ) with hB
  have hB0 : 0 < B := Real.exp_pos _
  have hC := D.ld_C_nonneg
  set ε' := ε / (B * (D.C + 1)) with hε'
  have hε'0 : 0 < ε' := by positivity
  have hU : UniformContinuousOn (fderiv ℝ f) (closedBall x₀ D.R) :=
    (isCompact_closedBall x₀ D.R).uniformContinuousOn_of_continuous
      (hf.continuous_fderiv one_ne_zero).continuousOn
  obtain ⟨δ₀, hδ₀, hδ⟩ := Metric.uniformContinuousOn_iff.1 hU ε' hε'0
  refine ⟨δ₀ / ((D.L : ℝ) + 1), by positivity, fun y hy hyx s hs => ?_⟩
  obtain ⟨hJ0x, hJdx⟩ := D.ld_J_spec hf x hx
  obtain ⟨hJ0y, hJdy⟩ := D.ld_J_spec hf y hy
  have hDf : ∀ s ∈ Icc (-D.τ) D.τ, ‖fderiv ℝ f (D.α y s) - fderiv ℝ f (D.α x s)‖ ≤ ε' := by
    intro s hs
    have h1 := (D.lip s hs).norm_sub_le hy hx
    have h2 : ((D.L : ℝ) + 1) * ‖y - x‖ < δ₀ := by
      rwa [lt_div_iff₀ (by positivity), mul_comm] at hyx
    rw [← dist_eq_norm]
    refine (hδ _ (D.mem y hy s hs) _ (D.mem x hx s hs) ?_).le
    rw [dist_eq_norm]; nlinarith [norm_nonneg (y - x)]
  have key := ld_gronwall_symm (fun s => D.J y s - D.J x s)
    (fun s => (fderiv ℝ f (D.α y s)).comp (D.J y s) - (fderiv ℝ f (D.α x s)).comp (D.J x s))
    D.τ 0 D.M (ε' * B) (fun s hs => (hJdy s hs).fun_sub (hJdx s hs)) (by simp [hJ0x, hJ0y])
    (fun s hs => by
      have hsplit : (fderiv ℝ f (D.α y s)).comp (D.J y s) - (fderiv ℝ f (D.α x s)).comp (D.J x s) =
          (fderiv ℝ f (D.α y s)).comp (D.J y s - D.J x s) +
          (fderiv ℝ f (D.α y s) - fderiv ℝ f (D.α x s)).comp (D.J x s) := by
        rw [ContinuousLinearMap.comp_sub, ContinuousLinearMap.sub_comp]; abel
      rw [hsplit]
      refine (norm_add_le _ _).trans ?_
      have h1 := ContinuousLinearMap.opNorm_comp_le (fderiv ℝ f (D.α y s)) (D.J y s - D.J x s)
      have h2 := ContinuousLinearMap.opNorm_comp_le
        (fderiv ℝ f (D.α y s) - fderiv ℝ f (D.α x s)) (D.J x s)
      have h3 := D.dbound _ (D.mem y hy s hs)
      have h4 := hDf s hs
      have h5 := D.ld_J_norm_le hf x hx s hs
      nlinarith [norm_nonneg (D.J y s - D.J x s), norm_nonneg (D.J x s),
        norm_nonneg (fderiv ℝ f (D.α y s) - fderiv ℝ f (D.α x s))])
    s hs
  refine key.trans ((D.ld_gb_le (by positivity) hs).trans ?_)
  rw [hε', div_mul_eq_mul_div, div_mul_eq_mul_div, div_le_iff₀ (by positivity)]
  nlinarith [mul_le_mul_of_nonneg_left (le_add_of_nonneg_right zero_le_one : D.C ≤ D.C + 1) hB0.le]

/-! ## ① The flow is differentiable, and `C¹`, in the initial point -/

/-- **① (a), T3b's stop.** `y ↦ α y t` has derivative `J x t` at every `x ∈ ball x₀ r`, `t ∈ [-τ, τ]`. -/
theorem ld_flow_hasFDerivAt (hf : ContDiff ℝ 1 f) (x : E) (hx : x ∈ ball x₀ D.r)
    (t : ℝ) (ht : t ∈ Icc (-D.τ) D.τ) : HasFDerivAt (fun y => D.α y t) (D.J x t) x := by
  rw [hasFDerivAt_iff_isLittleO]
  refine Asymptotics.IsLittleO.of_bound fun c hc => ?_
  obtain ⟨δ, hδ, h⟩ := D.ld_remainder_uniform hf x (ball_subset_closedBall hx) c hc
  filter_upwards [ball_mem_nhds x hδ, isOpen_ball.mem_nhds hx] with y hy1 hy2
  rw [mem_ball, dist_eq_norm] at hy1
  exact h y (ball_subset_closedBall hy2) hy1 t ht

/-- **① (b).** The derivative `x ↦ J x t` is continuous on `closedBall x₀ r`, uniformly in `t`. -/
theorem ld_J_continuousOn (hf : ContDiff ℝ 1 f) (t : ℝ) (ht : t ∈ Icc (-D.τ) D.τ) :
    ContinuousOn (fun x => D.J x t) (closedBall x₀ D.r) := by
  intro x hx
  rw [Metric.continuousWithinAt_iff]
  intro ε hε
  obtain ⟨δ, hδ, h⟩ := D.ld_J_uniform hf x hx (ε / 2) (half_pos hε)
  refine ⟨δ, hδ, fun y hy hyx => ?_⟩
  rw [dist_eq_norm] at hyx ⊢
  exact (h y hy hyx t ht).trans_lt (half_lt_self hε)

/-- **① (c).** For every `t ∈ [-τ, τ]`, `x ↦ α x t` is `C¹` on `ball x₀ r`. -/
theorem ld_flow_contDiffOn (hf : ContDiff ℝ 1 f) (t : ℝ) (ht : t ∈ Icc (-D.τ) D.τ) :
    ContDiffOn ℝ 1 (fun y => D.α y t) (ball x₀ D.r) := fun _x hx =>
  (contDiffAt_one_iff.2 ⟨fun y => D.J y t, ball x₀ D.r, isOpen_ball.mem_nhds hx,
    (D.ld_J_continuousOn hf t ht).mono ball_subset_closedBall,
    fun y hy => D.ld_flow_hasFDerivAt hf y hy t ht⟩).contDiffWithinAt

/-- The open domain of the joint statement. -/
def U : Set (ℝ × E) := Ioo (-D.τ) D.τ ×ˢ ball x₀ D.r

theorem ld_U_open : IsOpen D.U := isOpen_Ioo.prod isOpen_ball

/-- The joint derivative: `(s, h) ↦ s • f (α x t) + J x t h`. -/
noncomputable def Dflow (p : ℝ × E) : ℝ × E →L[ℝ] E :=
  (ContinuousLinearMap.fst ℝ ℝ E).smulRight (f (D.α p.2 p.1)) +
    (D.J p.2 p.1).comp (ContinuousLinearMap.snd ℝ ℝ E)

theorem ld_Dflow_apply (p q : ℝ × E) : D.Dflow p q = q.1 • f (D.α p.2 p.1) + D.J p.2 p.1 q.2 := by
  simp [Dflow]

/-- `(t, x) ↦ J x t` is jointly continuous on `U`. -/
theorem ld_J_continuousAt_joint (hf : ContDiff ℝ 1 f) (p : ℝ × E) (hp : p ∈ D.U) :
    ContinuousAt (fun q : ℝ × E => D.J q.2 q.1) p := by
  obtain ⟨t, x⟩ := p
  obtain ⟨ht, hx⟩ := hp
  have htI : Icc (-D.τ) D.τ ∈ 𝓝 t := Icc_mem_nhds ht.1 ht.2
  have hJt : ContinuousAt (D.J x) t :=
    (((D.ld_J_spec hf x (ball_subset_closedBall hx)).2 t (Ioo_subset_Icc_self ht)).hasDerivAt
      htI).continuousAt
  rw [Metric.continuousAt_iff']
  intro ε hε
  obtain ⟨δ, hδ, h⟩ := D.ld_J_uniform hf x (ball_subset_closedBall hx) (ε / 4) (by positivity)
  have h1 : ∀ᶠ q in 𝓝 (t, x), q.1 ∈ Icc (-D.τ) D.τ := continuousAt_fst.preimage_mem_nhds htI
  have h2 : ∀ᶠ q in 𝓝 (t, x), q.2 ∈ ball x₀ D.r :=
    continuousAt_snd.preimage_mem_nhds (isOpen_ball.mem_nhds hx)
  have h3 : ∀ᶠ q in 𝓝 (t, x), q.2 ∈ ball x δ :=
    continuousAt_snd.preimage_mem_nhds (ball_mem_nhds x hδ)
  have h4 : ∀ᶠ q in 𝓝 (t, x), dist (D.J x q.1) (D.J x t) < ε / 2 :=
    (hJt.comp continuousAt_fst).eventually (Metric.ball_mem_nhds _ (half_pos hε))
  filter_upwards [h1, h2, h3, h4] with q hq1 hq2 hq3 hq4
  rw [mem_ball, dist_eq_norm] at hq3
  have := h q.2 (ball_subset_closedBall hq2) hq3 q.1 hq1
  rw [dist_eq_norm] at hq4 ⊢
  calc ‖D.J q.2 q.1 - D.J x t‖ ≤ ‖D.J q.2 q.1 - D.J x q.1‖ + ‖D.J x q.1 - D.J x t‖ :=
        norm_sub_le_norm_sub_add_norm_sub _ _ _
    _ < ε := by linarith

/-- **① (d).** `(t, x) ↦ α x t` has derivative `Dflow (t, x)` at every point of `U`. -/
theorem ld_flow_hasFDerivAt_joint (hf : ContDiff ℝ 1 f) (p : ℝ × E) (hp : p ∈ D.U) :
    HasFDerivAt (fun q : ℝ × E => D.α q.2 q.1) (D.Dflow p) p := by
  obtain ⟨t, x⟩ := p
  obtain ⟨ht, hx⟩ := hp
  have hxc := ball_subset_closedBall hx
  have htI : Icc (-D.τ) D.τ ∈ 𝓝 t := Icc_mem_nhds ht.1 ht.2
  -- the time part
  have hA : HasFDerivAt (fun q : ℝ × E => D.α x q.1)
      ((ContinuousLinearMap.fst ℝ ℝ E).smulRight (f (D.α x t))) (t, x) := by
    have := ((D.deriv x hxc t (Ioo_subset_Icc_self ht)).hasDerivAt htI).hasFDerivAt.comp (t, x)
      (hasFDerivAt_fst (𝕜 := ℝ) (p := (t, x)))
    exact this.congr_fderiv (ContinuousLinearMap.ext fun q => by simp)
  -- the space part, through the uniform remainder and the continuity of `J x` in time
  have hJt : ContinuousAt (D.J x) t :=
    (((D.ld_J_spec hf x hxc).2 t (Ioo_subset_Icc_self ht)).hasDerivAt htI).continuousAt
  have hB : HasFDerivAt (fun q : ℝ × E => D.α q.2 q.1 - D.α x q.1)
      ((D.J x t).comp (ContinuousLinearMap.snd ℝ ℝ E)) (t, x) := by
    rw [hasFDerivAt_iff_isLittleO]
    refine Asymptotics.IsLittleO.of_bound fun c hc => ?_
    obtain ⟨δ, hδ, h⟩ := D.ld_remainder_uniform hf x hxc (c / 2) (half_pos hc)
    have h1 : ∀ᶠ q in 𝓝 (t, x), q.1 ∈ Icc (-D.τ) D.τ := continuousAt_fst.preimage_mem_nhds htI
    have h2 : ∀ᶠ q in 𝓝 (t, x), q.2 ∈ ball x₀ D.r :=
      continuousAt_snd.preimage_mem_nhds (isOpen_ball.mem_nhds hx)
    have h3 : ∀ᶠ q in 𝓝 (t, x), q.2 ∈ ball x δ :=
      continuousAt_snd.preimage_mem_nhds (ball_mem_nhds x hδ)
    have h4 : ∀ᶠ q in 𝓝 (t, x), dist (D.J x q.1) (D.J x t) < c / 2 :=
      (hJt.comp continuousAt_fst).eventually (Metric.ball_mem_nhds _ (half_pos hc))
    filter_upwards [h1, h2, h3, h4] with q hq1 hq2 hq3 hq4
    rw [mem_ball, dist_eq_norm] at hq3
    rw [dist_eq_norm] at hq4
    have hr := h q.2 (ball_subset_closedBall hq2) hq3 q.1 hq1
    have hsn : ‖q.2 - x‖ ≤ ‖q - (t, x)‖ := by
      have := norm_snd_le (q - (t, x)); simpa using this
    have hJ : ‖(D.J x q.1 - D.J x t) (q.2 - x)‖ ≤ c / 2 * ‖q.2 - x‖ :=
      ((D.J x q.1 - D.J x t).le_opNorm _).trans
        (mul_le_mul_of_nonneg_right hq4.le (norm_nonneg _))
    have heq : D.α q.2 q.1 - D.α x q.1 - (D.α x t - D.α x t) -
        ((D.J x t).comp (ContinuousLinearMap.snd ℝ ℝ E)) (q - (t, x)) =
        (D.α q.2 q.1 - D.α x q.1 - D.J x q.1 (q.2 - x)) + (D.J x q.1 - D.J x t) (q.2 - x) := by
      simp only [sub_self, sub_zero, ContinuousLinearMap.comp_apply, ContinuousLinearMap.coe_snd',
        Prod.snd_sub, sub_apply]
      abel
    rw [heq]
    calc _ ≤ _ := norm_add_le _ _
      _ ≤ c / 2 * ‖q.2 - x‖ + c / 2 * ‖q.2 - x‖ := add_le_add hr hJ
      _ = c * ‖q.2 - x‖ := by ring
      _ ≤ c * ‖q - (t, x)‖ := mul_le_mul_of_nonneg_left hsn hc.le
  have := hB.add hA
  convert this using 1
  · funext q; simp
  · rw [Dflow, add_comm]

/-- The flow is continuous on `U`. -/
theorem ld_flow_continuousOn_joint (hf : ContDiff ℝ 1 f) :
    ContinuousOn (fun q : ℝ × E => D.α q.2 q.1) D.U := fun p hp =>
  (D.ld_flow_hasFDerivAt_joint hf p hp).continuousAt.continuousWithinAt

theorem ld_Dflow_continuousOn (hf : ContDiff ℝ 1 f) : ContinuousOn D.Dflow D.U := by
  have h1 : ContinuousOn (fun p : ℝ × E => f (D.α p.2 p.1)) D.U :=
    hf.continuous.comp_continuousOn (D.ld_flow_continuousOn_joint hf)
  have h2 : ContinuousOn (fun p : ℝ × E => D.J p.2 p.1) D.U := fun p hp =>
    (D.ld_J_continuousAt_joint hf p hp).continuousWithinAt
  have h3 : ContinuousOn (fun p : ℝ × E =>
      (ContinuousLinearMap.fst ℝ ℝ E).smulRight (f (D.α p.2 p.1))) D.U := by
    have := (ContinuousLinearMap.smulRightL ℝ (ℝ × E) E (ContinuousLinearMap.fst ℝ ℝ E)).continuous.comp_continuousOn h1
    convert this using 1
    funext p
    exact ContinuousLinearMap.ext fun q => by simp
  exact h3.add (h2.clm_comp continuousOn_const)

/-- **① (e), the registered theorem.** The flow `(t, x) ↦ α x t` is `C¹` jointly on
`Ioo (-τ) τ ×ˢ ball x₀ r`. -/
theorem ld_flow_contDiffOn_joint (hf : ContDiff ℝ 1 f) :
    ContDiffOn ℝ 1 (fun q : ℝ × E => D.α q.2 q.1) D.U := fun _p hp =>
  (contDiffAt_one_iff.2 ⟨D.Dflow, D.U, D.ld_U_open.mem_nhds hp, D.ld_Dflow_continuousOn hf,
    fun q hq => D.ld_flow_hasFDerivAt_joint hf q hq⟩).contDiffWithinAt

end FlowData

/-- **① headline, without `FlowData`.** A `C¹` field on a finite-dimensional space has a local flow
`α x t` (`x ∈ closedBall x₀ r`, `t ∈ [-τ, τ]`) that is `C¹` jointly in `(t, x)` on `Ioo (-τ) τ ×ˢ ball x₀ r`,
`C¹` in `x` for each `t ∈ [-τ, τ]`, with `x`-derivative solving the variational equation. -/
theorem ld_flow_C1 (hf : ContDiff ℝ 1 f) (x₀ : E) :
    ∃ τ > (0 : ℝ), ∃ r > (0 : ℝ), ∃ α : E → ℝ → E, ∃ J : E → ℝ → E →L[ℝ] E,
      (∀ x ∈ closedBall x₀ r, α x 0 = x ∧
        ∀ t ∈ Icc (-τ) τ, HasDerivWithinAt (α x) (f (α x t)) (Icc (-τ) τ) t) ∧
      (∀ x ∈ closedBall x₀ r, J x 0 = ContinuousLinearMap.id ℝ E ∧ ∀ t ∈ Icc (-τ) τ,
        HasDerivWithinAt (J x) ((fderiv ℝ f (α x t)).comp (J x t)) (Icc (-τ) τ) t) ∧
      (∀ x ∈ ball x₀ r, ∀ t ∈ Icc (-τ) τ, HasFDerivAt (fun y => α y t) (J x t) x) ∧
      (∀ t ∈ Icc (-τ) τ, ContDiffOn ℝ 1 (fun y => α y t) (ball x₀ r)) ∧
      ContDiffOn ℝ 1 (fun q : ℝ × E => α q.2 q.1) (Ioo (-τ) τ ×ˢ ball x₀ r) := by
  obtain ⟨D⟩ := ld_flowData_exists hf x₀
  exact ⟨D.τ, D.τ_pos, D.r, D.r_pos, D.α, D.J, fun x hx => ⟨D.init x hx, D.deriv x hx⟩,
    fun x hx => D.ld_J_spec hf x hx, fun x hx t ht => D.ld_flow_hasFDerivAt hf x hx t ht,
    fun t ht => D.ld_flow_contDiffOn hf t ht, D.ld_flow_contDiffOn_joint hf⟩

/-! ## ② The flow-box chart -/

/-- A complement `H` of `ℝ ∙ v`, `v ≠ 0`, gives `ℝ × H ≃L E`, `(a, h) ↦ a • v + h`. -/
theorem ld_complement_equiv (v : E) (hv : v ≠ 0) (H : Submodule ℝ E) (hH : IsCompl (ℝ ∙ v) H) :
    ∃ e : (ℝ × H) ≃L[ℝ] E, ∀ p : ℝ × H, e p = p.1 • v + p.2 := by
  let ℓ : ℝ × H →ₗ[ℝ] E := (LinearMap.fst ℝ ℝ H).smulRight v + H.subtype ∘ₗ LinearMap.snd ℝ ℝ H
  have hℓ : ∀ p, ℓ p = p.1 • v + p.2 := fun p => by simp [ℓ]
  have hinj : Function.Injective ℓ := by
    rw [← LinearMap.ker_eq_bot, LinearMap.ker_eq_bot']
    intro p hp
    rw [hℓ] at hp
    have h1 : p.1 • v = -(p.2 : E) := eq_neg_of_add_eq_zero_left hp
    have h2 : p.1 • v = 0 := Submodule.disjoint_def.1 hH.disjoint _
      (Submodule.mem_span_singleton.2 ⟨p.1, rfl⟩) (by rw [h1]; exact H.neg_mem p.2.2)
    have h3 : p.1 = 0 := (smul_eq_zero.1 h2).resolve_right hv
    have h4 : (p.2 : E) = 0 := by rw [h3, zero_smul, zero_add] at hp; exact hp
    exact Prod.ext h3 (Subtype.ext h4)
  have hsurj : Function.Surjective ℓ := by
    intro x
    have hx : x ∈ (ℝ ∙ v) ⊔ H := by rw [hH.sup_eq_top]; trivial
    obtain ⟨y, hy, z, hz, rfl⟩ := Submodule.mem_sup.1 hx
    obtain ⟨a, rfl⟩ := Submodule.mem_span_singleton.1 hy
    exact ⟨(a, ⟨z, hz⟩), by rw [hℓ]⟩
  exact ⟨(LinearEquiv.ofBijective ℓ ⟨hinj, hsurj⟩).toContinuousLinearEquiv, fun p => hℓ p⟩

namespace FlowData

variable (D : FlowData f x₀)

/-- What a flow-box chart `Φ : ℝ × H → E` for `D` at `x₀` satisfies. -/
structure IsFlowBox (H : Submodule ℝ E) (Φ : OpenPartialHomeomorph (ℝ × H) E) : Prop where
  zero_mem : ((0 : ℝ), (0 : H)) ∈ Φ.source
  map_zero : Φ (0, 0) = x₀
  symm_x₀ : Φ.symm x₀ = (0, 0)
  /-- `Φ (λ, h) = α (x₀ + h) λ`, inside the domain of the joint statement. -/
  source_sub : ∀ p ∈ Φ.source, (p.1, x₀ + (p.2 : E)) ∈ D.U
  apply_eq : ∀ p ∈ Φ.source, Φ p = D.α (x₀ + p.2) p.1
  contDiffOn : ContDiffOn ℝ 1 Φ Φ.source
  /-- `DΦ (0, 0) (a, h) = a • f x₀ + h`, the invertible derivative. -/
  fderiv_zero : ∀ (a : ℝ) (h : H), fderiv ℝ Φ (0, 0) (a, h) = a • f x₀ + h
  /-- `DΦ p (a, h) = a • f (Φ p) + J (x₀ + h) λ h`. -/
  fderiv_eq : ∀ p ∈ Φ.source, ∀ u : ℝ × H,
    fderiv ℝ Φ p u = u.1 • f (Φ p) + D.J (x₀ + p.2) p.1 u.2
  /-- `f = ∂_λ` in the chart: `DΦ · (1, 0) = f ∘ Φ`. -/
  straightens : ∀ p ∈ Φ.source, fderiv ℝ Φ p (1, 0) = f (Φ p)
  /-- The inverse is `C¹` near `x₀`. -/
  symm_contDiffAt : ∀ᶠ y in 𝓝 x₀, ContDiffAt ℝ 1 Φ.symm y

/-- **② The flow-box chart.** If `f x₀ ≠ 0` and `H` is a complement of `ℝ ∙ f x₀`, then
`Ψ (λ, h) = α (x₀ + h) λ` restricts to an open partial homeomorphism `ℝ × H → E` around `(0, 0)` that is `C¹`
on its source, with `DΨ (0, 0) (a, h) = a • f x₀ + h`, `DΨ · (1, 0) = f ∘ Ψ` (so `f = ∂_λ` in the chart),
and a `C¹` inverse near `x₀`. -/
theorem ld_flowBox (hf : ContDiff ℝ 1 f) (hfx : f x₀ ≠ 0) (H : Submodule ℝ E)
    (hH : IsCompl (ℝ ∙ f x₀) H) : ∃ Φ : OpenPartialHomeomorph (ℝ × H) E, D.IsFlowBox H Φ := by
  obtain ⟨e, he⟩ := ld_complement_equiv (f x₀) hfx H hH
  -- the affine map `(λ, h) ↦ (λ, x₀ + h)`
  set Lg : ℝ × H →L[ℝ] ℝ × E :=
    (ContinuousLinearMap.fst ℝ ℝ H).prod (H.subtypeL.comp (ContinuousLinearMap.snd ℝ ℝ H)) with hLg
  set g : ℝ × H → ℝ × E := fun p => ((0 : ℝ), x₀) + Lg p with hg
  have hgp : ∀ p : ℝ × H, g p = (p.1, x₀ + (p.2 : E)) := fun p => by simp [hg, hLg]
  have hgd : ∀ p, HasFDerivAt g Lg p := fun p => Lg.hasFDerivAt.const_add _
  have hgc : ContDiff ℝ 1 g := contDiff_const.add Lg.contDiff
  set Ψ : ℝ × H → E := fun p => D.α (x₀ + (p.2 : E)) p.1 with hΨ
  have hΨg : Ψ = (fun q : ℝ × E => D.α q.2 q.1) ∘ g := by
    funext p; simp only [Function.comp, hgp, hΨ]
  set V := g ⁻¹' D.U with hV
  have hVo : IsOpen V := D.ld_U_open.preimage hgc.continuous
  have hV0 : ((0 : ℝ), (0 : H)) ∈ V := by
    show g (0, 0) ∈ D.U
    rw [hgp]
    exact ⟨⟨by linarith [D.τ_pos], D.τ_pos⟩, by simpa using D.r_pos⟩
  have hΨc : ContDiffOn ℝ 1 Ψ V := by
    rw [hΨg]; exact (D.ld_flow_contDiffOn_joint hf).comp hgc.contDiffOn fun p hp => hp
  have hΨd : ∀ p ∈ V, HasFDerivAt Ψ ((D.Dflow (g p)).comp Lg) p := fun p hp => by
    rw [hΨg]; exact (D.ld_flow_hasFDerivAt_joint hf (g p) hp).comp p (hgd p)
  have hΨu : ∀ p ∈ V, ∀ u, fderiv ℝ Ψ p u = u.1 • f (Ψ p) + D.J (x₀ + p.2) p.1 u.2 :=
    fun p hp u => by
      rw [(hΨd p hp).fderiv, ContinuousLinearMap.comp_apply, ld_Dflow_apply, hgp]
      simp [hLg, hΨ]
  have hx₀ : x₀ ∈ closedBall x₀ D.r := mem_closedBall_self D.r_pos.le
  have hD0 : (D.Dflow (g (0, 0))).comp Lg = (e : ℝ × H →L[ℝ] E) := by
    refine ContinuousLinearMap.ext fun q => ?_
    rw [ContinuousLinearMap.comp_apply, ld_Dflow_apply, hgp, ContinuousLinearEquiv.coe_coe, he]
    simp [hLg, D.init x₀ hx₀, (D.ld_J_spec hf x₀ hx₀).1]
  have hΨ0 : HasFDerivAt Ψ (e : ℝ × H →L[ℝ] E) (0, 0) := hD0 ▸ hΨd _ hV0
  have hΨ00 : Ψ (0, 0) = x₀ := by simp [hΨ, D.init x₀ hx₀]
  have hΨa : ContDiffAt ℝ 1 Ψ (0, 0) := hΨc.contDiffAt (hVo.mem_nhds hV0)
  have hn : (1 : WithTop ℕ∞) ≠ 0 := by norm_num
  set Φ₀ := hΨa.toOpenPartialHomeomorph Ψ hΨ0 hn
  refine ⟨Φ₀.restrOpen V hVo, ⟨⟨hΨa.mem_toOpenPartialHomeomorph_source hΨ0 hn, hV0⟩, hΨ00, ?_,
    fun p hp => by have := hp.2; rwa [Set.mem_preimage, hgp] at this, fun p _ => rfl,
    hΨc.mono inter_subset_right, fun a h => ?_, fun p hp u => hΨu p hp.2 u, fun p hp => ?_, ?_⟩⟩
  · have := hΨa.localInverse_apply_image hΨ0 hn
    rw [hΨ00] at this
    exact this
  · show fderiv ℝ Ψ (0, 0) (a, h) = a • f x₀ + h
    rw [hΨ0.fderiv, ContinuousLinearEquiv.coe_coe, he]
  · show fderiv ℝ Ψ p (1, 0) = f (Ψ p)
    rw [hΨu p hp.2]; simp
  · have := (hΨa.to_localInverse hΨ0 hn).eventually (by simp)
    rw [hΨ00] at this
    exact this

end FlowData

/-- **② as an existence statement.** At a point where a `C¹` field does not vanish there is a complement
`H` of `ℝ ∙ f x₀`, a flow, and a flow-box chart `ℝ × H → E` straightening `f` to `∂_λ`. -/
theorem ld_flowBox_exists (hf : ContDiff ℝ 1 f) (x₀ : E) (hfx : f x₀ ≠ 0) :
    ∃ (H : Submodule ℝ E) (D : FlowData f x₀) (Φ : OpenPartialHomeomorph (ℝ × H) E),
      D.IsFlowBox H Φ := by
  obtain ⟨H, hH⟩ := Submodule.exists_isCompl (ℝ ∙ f x₀)
  obtain ⟨D⟩ := ld_flowData_exists hf x₀
  obtain ⟨Φ, hΦ⟩ := D.ld_flowBox hf hfx H hH
  exact ⟨H, D, Φ, hΦ⟩

/-! ## ① The local constructor: cutoff, small flow data, transfer -/

/-- **Cutoff.** A field `C¹` on `ball x₀ ρ` agrees, near every point of `ball x₀ (ρ / 4)`, with a global `C¹`
field: `χ • f`, `χ` a `ContDiffBump x₀` equal to `1` on `closedBall x₀ (ρ / 4)`, support `ball x₀ (ρ / 2)`. -/
theorem ld_cutoff {ρ : ℝ} (hρ : 0 < ρ) (hf : ContDiffOn ℝ 1 f (ball x₀ ρ)) :
    ∃ g : E → E, ContDiff ℝ 1 g ∧ ∀ y ∈ ball x₀ (ρ / 4), g =ᶠ[𝓝 y] f := by
  let χ : ContDiffBump x₀ := ⟨ρ / 4, ρ / 2, by positivity, by linarith⟩
  have hrIn : χ.rIn = ρ / 4 := rfl
  have hrOut : χ.rOut = ρ / 2 := rfl
  refine ⟨fun y => χ y • f y, ?_, fun y hy => ?_⟩
  · rw [contDiff_iff_contDiffAt]
    intro y
    by_cases hy : y ∈ ball x₀ ρ
    · exact χ.contDiff.contDiffAt.smul (hf.contDiffAt (isOpen_ball.mem_nhds hy))
    · have hy' : y ∉ tsupport χ := by
        rw [χ.tsupport_eq, hrOut]
        intro h
        apply hy
        rw [mem_closedBall] at h
        rw [mem_ball]
        linarith
      have h0 : (fun y => χ y • f y) =ᶠ[𝓝 y] fun _ => (0 : E) := by
        filter_upwards [notMem_tsupport_iff_eventuallyEq.1 hy'] with z hz
        simp [hz]
      exact contDiffAt_const.congr_of_eventuallyEq h0
  · filter_upwards [isOpen_ball.mem_nhds hy] with z hz
    rw [χ.one_of_mem_closedBall (by rw [hrIn]; exact ball_subset_closedBall hz), one_smul]

/-- **Small flow data.** For a global `C¹` field, flow data whose trajectory ball `closedBall x₀ R` has
`R < R₀`: the speed along `[-τ₀, τ₀]` is bounded by some `S`, and then `τ ≤ R / (2 S)`, `r ≤ R / 2`. -/
theorem ld_flowData_small {g : E → E} (hg : ContDiff ℝ 1 g) (x₀ : E) {R₀ : ℝ} (hR₀ : 0 < R₀) :
    ∃ D : FlowData g x₀, D.R < R₀ := by
  obtain ⟨τ₀, hτ₀, r₀, hr₀, α, L, hα, hL⟩ := ld_local_flow g hg x₀
  obtain ⟨R₁, hR₁⟩ := ld_flow_bounded g τ₀ r₀ α L x₀ hα hL
  obtain ⟨C, hC⟩ := (isCompact_closedBall x₀ R₁).exists_bound_of_continuousOn
    hg.continuous.continuousOn
  set R := R₀ / 2 with hR
  have hR0 : 0 < R := by positivity
  obtain ⟨C', hC'⟩ := (isCompact_closedBall x₀ R).exists_bound_of_continuousOn
    (hg.continuous_fderiv one_ne_zero).continuousOn
  set S := max C 0 + 1 with hS
  have hS0 : 0 < S := by positivity
  set M := max C' 0 + 1 with hM
  have hM0 : 0 < M := by positivity
  set τ := min (min τ₀ (1 / (2 * M))) (R / (2 * S)) with hτ
  have hτ0 : 0 < τ := lt_min (lt_min hτ₀ (by positivity)) (by positivity)
  have hττ₀ : τ ≤ τ₀ := (min_le_left _ _).trans (min_le_left _ _)
  have hτM : τ ≤ 1 / (2 * M) := (min_le_left _ _).trans (min_le_right _ _)
  have hτS : τ ≤ R / (2 * S) := min_le_right _ _
  set r := min r₀ (R / 2) with hr
  have hr0 : 0 < r := lt_min hr₀ (by positivity)
  have hrr₀ : r ≤ r₀ := min_le_left _ _
  have hrR : r ≤ R / 2 := min_le_right _ _
  have hsub : Icc (-τ) τ ⊆ Icc (-τ₀) τ₀ := Icc_subset_Icc (neg_le_neg hττ₀) hττ₀
  have hbsub : closedBall x₀ r ⊆ closedBall x₀ r₀ := closedBall_subset_closedBall hrr₀
  have hmem : ∀ x ∈ closedBall x₀ r, ∀ t ∈ Icc (-τ) τ, α x t ∈ closedBall x₀ R := by
    intro x hx t ht
    have hd : ∀ u ∈ Icc (-τ) τ, HasDerivWithinAt (α x) (g (α x u)) (Icc (-τ) τ) u :=
      fun u hu => ((hα x (hbsub hx)).2 u (hsub hu)).mono hsub
    have hb : ∀ u ∈ Icc (-τ) τ, ‖g (α x u)‖ ≤ S := fun u hu =>
      (hC _ (hR₁ x (hbsub hx) u (hsub hu))).trans (by rw [hS]; linarith [le_max_left C 0])
    have h0 : (0 : ℝ) ∈ Icc (-τ) τ := ⟨by linarith, hτ0.le⟩
    have key := (convex_Icc (-τ) τ).norm_image_sub_le_of_norm_hasDerivWithin_le hd hb h0 ht
    rw [(hα x (hbsub hx)).1, sub_zero, Real.norm_eq_abs] at key
    have ht' : |t| ≤ τ := abs_le.2 ht
    have h1 : S * |t| ≤ R / 2 := by
      calc S * |t| ≤ S * (R / (2 * S)) := mul_le_mul_of_nonneg_left (ht'.trans hτS) hS0.le
        _ = R / 2 := by field_simp
    rw [mem_closedBall] at hx ⊢
    calc dist (α x t) x₀ ≤ dist (α x t) x + dist x x₀ := dist_triangle _ _ _
      _ ≤ R / 2 + R / 2 := by rw [dist_eq_norm]; linarith
      _ = R := by ring
  refine ⟨⟨τ, r, R, M, L, α, hτ0, hr0, hM0, ?_, fun x hx => (hα x (hbsub hx)).1,
    fun x hx t ht => ((hα x (hbsub hx)).2 t (hsub ht)).mono hsub,
    fun t ht => (hL t (hsub ht)).mono hbsub, hmem, fun y hy => (hC' y hy).trans ?_⟩, ?_⟩
  · calc M * τ ≤ M * (1 / (2 * M)) := mul_le_mul_of_nonneg_left hτM hM0.le
      _ = 1 / 2 := by field_simp
  · rw [hM]; linarith [le_max_left C' 0]
  · show R < R₀
    rw [hR]; linarith

/-- Two fields that agree near every point of `ball x₀ s` agree to first order on `closedBall x₀ R`, `R < s`. -/
theorem ld_agree {g : E → E} {s R : ℝ} (hgf : ∀ y ∈ ball x₀ s, g =ᶠ[𝓝 y] f) (hR : R < s) :
    ∀ y ∈ closedBall x₀ R, f y = g y ∧ fderiv ℝ f y = fderiv ℝ g y := fun y hy =>
  ⟨(hgf y (closedBall_subset_ball hR hy)).eq_of_nhds.symm,
    (hgf y (closedBall_subset_ball hR hy)).fderiv_eq.symm⟩

namespace FlowData

variable {g : E → E}

/-- `x₀` lies in the trajectory ball. -/
theorem ld_x₀_mem (D : FlowData g x₀) : x₀ ∈ closedBall x₀ D.R := by
  have hx := mem_closedBall_self (x := x₀) D.r_pos.le
  have := D.mem x₀ hx 0 ⟨by linarith [D.τ_pos], D.τ_pos.le⟩
  rwa [D.init x₀ hx] at this

/-- **Transfer.** Flow data for `g` is flow data for `f` when `f = g` to first order on `closedBall x₀ R`:
same `τ, r, R, M, L, α`. -/
def transfer (D : FlowData g x₀)
    (hfg : ∀ y ∈ closedBall x₀ D.R, f y = g y ∧ fderiv ℝ f y = fderiv ℝ g y) : FlowData f x₀ where
  τ := D.τ
  r := D.r
  R := D.R
  M := D.M
  L := D.L
  α := D.α
  τ_pos := D.τ_pos
  r_pos := D.r_pos
  M_pos := D.M_pos
  Mτ := D.Mτ
  init := D.init
  deriv := fun x hx t ht => by
    rw [(hfg _ (D.mem x hx t ht)).1]; exact D.deriv x hx t ht
  lip := D.lip
  mem := D.mem
  dbound := fun y hy => by rw [(hfg y hy).2]; exact D.dbound y hy

variable (D : FlowData g x₀)
  (hfg : ∀ y ∈ closedBall x₀ D.R, f y = g y ∧ fderiv ℝ f y = fderiv ℝ g y)

/-- The transferred data has the same variational solution `J`. -/
theorem ld_transfer_J (x : E) (hx : x ∈ closedBall x₀ D.r) : (D.transfer hfg).J x = D.J x := by
  have h : (D.transfer hfg).IsVar x = D.IsVar x := by
    funext W
    apply propext
    unfold IsVar
    dsimp only [transfer]
    constructor
    · rintro ⟨h0, hd⟩
      exact ⟨h0, fun t ht => by have := hd t ht; rwa [(hfg _ (D.mem x hx t ht)).2] at this⟩
    · rintro ⟨h0, hd⟩
      exact ⟨h0, fun t ht => by rw [(hfg _ (D.mem x hx t ht)).2]; exact hd t ht⟩
  unfold J
  rw [h]

/-- A flow-box point lies in the trajectory ball. -/
theorem ld_isFlowBox_mem {H : Submodule ℝ E} {Φ : OpenPartialHomeomorph (ℝ × H) E}
    (hΦ : D.IsFlowBox H Φ) (p : ℝ × H) (hp : p ∈ Φ.source) : Φ p ∈ closedBall x₀ D.R := by
  obtain ⟨ht, hy⟩ := hΦ.source_sub p hp
  rw [hΦ.apply_eq p hp]
  exact D.mem _ (ball_subset_closedBall hy) _ (Ioo_subset_Icc_self ht)

/-- **Transfer of the flow box.** A flow-box chart for `g` is a flow-box chart for `f`, with `f` itself in
`straightens`: `DΦ · (1, 0) = f ∘ Φ`. -/
theorem ld_transfer_isFlowBox {H : Submodule ℝ E} {Φ : OpenPartialHomeomorph (ℝ × H) E}
    (hΦ : D.IsFlowBox H Φ) : (D.transfer hfg).IsFlowBox H Φ := by
  have hx₀ := (hfg x₀ D.ld_x₀_mem).1
  refine ⟨hΦ.zero_mem, hΦ.map_zero, hΦ.symm_x₀, hΦ.source_sub, hΦ.apply_eq, hΦ.contDiffOn,
    fun a h => ?_, fun p hp u => ?_, fun p hp => ?_, hΦ.symm_contDiffAt⟩
  · rw [hx₀]; exact hΦ.fderiv_zero a h
  · obtain ⟨_, hy⟩ := hΦ.source_sub p hp
    rw [(hfg _ (D.ld_isFlowBox_mem hΦ p hp)).1,
      D.ld_transfer_J hfg _ (ball_subset_closedBall hy)]
    exact hΦ.fderiv_eq p hp u
  · rw [(hfg _ (D.ld_isFlowBox_mem hΦ p hp)).1]; exact hΦ.straightens p hp

end FlowData

/-- **① The local constructor.** A field that is `C¹` on `ball x₀ ρ` has flow data at `x₀` (for `f` itself),
with trajectory ball inside `ball x₀ (ρ / 4)`. -/
theorem ld_flowData_exists_of_contDiffOn {ρ : ℝ} (hρ : 0 < ρ) (hf : ContDiffOn ℝ 1 f (ball x₀ ρ)) :
    ∃ D : FlowData f x₀, D.R < ρ / 4 := by
  obtain ⟨g, hg, hgf⟩ := ld_cutoff hρ hf
  obtain ⟨D, hD⟩ := ld_flowData_small hg x₀ (by positivity : 0 < ρ / 4)
  exact ⟨D.transfer (ld_agree hgf hD), hD⟩

/-- **① The local flow box.** A field `C¹` on `ball x₀ ρ`, `f x₀ ≠ 0`: flow data for `f` and a flow-box chart
for it (all `IsFlowBox` properties, with `f` itself), trajectory ball inside `ball x₀ (ρ / 4)`. -/
theorem ld_flowBox_exists_of_contDiffOn {ρ : ℝ} (hρ : 0 < ρ) (hf : ContDiffOn ℝ 1 f (ball x₀ ρ))
    (hfx : f x₀ ≠ 0) :
    ∃ (H : Submodule ℝ E) (D : FlowData f x₀) (Φ : OpenPartialHomeomorph (ℝ × H) E),
      D.IsFlowBox H Φ ∧ D.R < ρ / 4 := by
  obtain ⟨g, hg, hgf⟩ := ld_cutoff hρ hf
  obtain ⟨D, hD⟩ := ld_flowData_small hg x₀ (by positivity : 0 < ρ / 4)
  have hfg := ld_agree hgf hD
  have hx₀ := (hfg x₀ D.ld_x₀_mem).1
  obtain ⟨H, hH⟩ := Submodule.exists_isCompl (ℝ ∙ f x₀)
  rw [hx₀] at hfx hH
  obtain ⟨Φ, hΦ⟩ := D.ld_flowBox hg hfx H hH
  exact ⟨H, D.transfer hfg, Φ, D.ld_transfer_isFlowBox hfg hΦ, hD⟩

/-- **① The usable form, without `FlowData`.** For `f` `C¹` on `ball x₀ ρ` with `f x₀ ≠ 0` there is a
flow-box chart `Φ : ℝ × H → E` at `x₀`, mapping its source into `ball x₀ (ρ / 4)`, `C¹`, with
`DΦ (0,0) (a, h) = a • f x₀ + h`, `DΦ · (1, 0) = f ∘ Φ` on the source, and a `C¹` inverse near `x₀`. -/
theorem ld_flowBox_chart_of_contDiffOn {ρ : ℝ} (hρ : 0 < ρ) (hf : ContDiffOn ℝ 1 f (ball x₀ ρ))
    (hfx : f x₀ ≠ 0) :
    ∃ (H : Submodule ℝ E) (Φ : OpenPartialHomeomorph (ℝ × H) E),
      ((0 : ℝ), (0 : H)) ∈ Φ.source ∧ Φ (0, 0) = x₀ ∧ Φ.symm x₀ = (0, 0) ∧
      MapsTo Φ Φ.source (ball x₀ (ρ / 4)) ∧ ContDiffOn ℝ 1 Φ Φ.source ∧
      (∀ (a : ℝ) (h : H), fderiv ℝ Φ (0, 0) (a, h) = a • f x₀ + h) ∧
      (∀ p ∈ Φ.source, fderiv ℝ Φ p (1, 0) = f (Φ p)) ∧
      (∀ᶠ y in 𝓝 x₀, ContDiffAt ℝ 1 Φ.symm y) := by
  obtain ⟨H, D, Φ, hΦ, hR⟩ := ld_flowBox_exists_of_contDiffOn hρ hf hfx
  exact ⟨H, Φ, hΦ.zero_mem, hΦ.map_zero, hΦ.symm_x₀,
    fun p hp => closedBall_subset_ball hR (D.ld_isFlowBox_mem hΦ p hp), hΦ.contDiffOn,
    hΦ.fderiv_zero, hΦ.straightens, hΦ.symm_contDiffAt⟩

/-! ## ② The flow-box chart on a manifold chart -/

section Manifold

open Manifold

variable {N : Type*} [TopologicalSpace N] [ChartedSpace E N] [IsManifold 𝓘(ℝ, E) 1 N]

-- `chartRep` (campaign 68 kit): textually identical copy kept above (campaign-100 `section Manifold`).
/-- Pushing the chart representative back by `(extChartAt p).symm` returns `X`. -/
theorem ld_chartRep_inv (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N) {y : E}
    (hy : y ∈ (extChartAt 𝓘(ℝ, E) p).target) :
    mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p).symm y (chartRep (E := E) X p y) =
      X ((extChartAt 𝓘(ℝ, E) p).symm y) := by
  have h := mfderivWithin_extChartAt_symm_comp_mfderiv_extChartAt (I := 𝓘(ℝ, E)) (x := p) hy
  rw [ModelWithCorners.range_eq_univ, mfderivWithin_univ] at h
  exact DFunLike.congr_fun h (X ((extChartAt 𝓘(ℝ, E) p).symm y))

-- `ld_mdifferentiableAt_symm`: textually identical copy kept above.
/-- **② The flow-box chart on a manifold.** Let `X` be a vector field on `N` whose chart representative at
`p` is `C¹` on the chart target, with `X p ≠ 0`. Then there is a flow-box chart `Φ : ℝ × H → E` into the chart
target such that `ψ = (extChartAt p).symm ∘ Φ` sends `(0, 0)` to `p` and straightens `X`:
`mfderiv ψ q (1, 0) = X (ψ q)` on the source. -/
theorem ld_manifold_flowBox (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N)
    (hX : ContDiffOn ℝ 1 (chartRep X p) (extChartAt 𝓘(ℝ, E) p).target) (hXp : X p ≠ 0) :
    ∃ (H : Submodule ℝ E) (Φ : OpenPartialHomeomorph (ℝ × H) E),
      ((0 : ℝ), (0 : H)) ∈ Φ.source ∧ Φ (0, 0) = extChartAt 𝓘(ℝ, E) p p ∧
      ((extChartAt 𝓘(ℝ, E) p).symm ∘ Φ) (0, 0) = p ∧
      MapsTo Φ Φ.source (extChartAt 𝓘(ℝ, E) p).target ∧ ContDiffOn ℝ 1 Φ Φ.source ∧
      (∀ q ∈ Φ.source, fderiv ℝ Φ q (1, 0) = chartRep X p (Φ q)) ∧
      (∀ q ∈ Φ.source, mfderiv 𝓘(ℝ, ℝ × H) 𝓘(ℝ, E) ((extChartAt 𝓘(ℝ, E) p).symm ∘ Φ) q (1, 0) =
        X (((extChartAt 𝓘(ℝ, E) p).symm ∘ Φ) q)) := by
  set e := extChartAt 𝓘(ℝ, E) p with he
  have hto : IsOpen e.target := isOpen_extChartAt_target p
  have hx0 : e p ∈ e.target := mem_extChartAt_target p
  obtain ⟨ρ, hρ, hball⟩ := Metric.isOpen_iff.1 hto _ hx0
  have hf : ContDiffOn ℝ 1 (chartRep X p) (ball (e p) ρ) := hX.mono hball
  have hep : e.symm (e p) = p := e.left_inv (mem_extChartAt_source p)
  have hfx : chartRep X p (e p) ≠ 0 := by
    intro h
    apply hXp
    have := ld_chartRep_inv X p hx0
    rw [h] at this
    have hz := (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p).symm (e p)).map_zero
    have key : ∀ z, z = p → X z = 0 → X p = 0 := by rintro z rfl h; exact h
    exact key _ hep (this.symm.trans hz)
  obtain ⟨H, Φ, h0, hΦ0, -, hmaps, hc, -, hstr, -⟩ := ld_flowBox_chart_of_contDiffOn hρ hf hfx
  have hmaps' : MapsTo Φ Φ.source e.target := fun q hq =>
    hball (ball_subset_ball (by linarith) (hmaps hq))
  refine ⟨H, Φ, h0, hΦ0, by simp [hΦ0, hep], hmaps', hc, hstr, fun q hq => ?_⟩
  have hΦd : DifferentiableAt ℝ Φ q :=
    (hc.contDiffAt (Φ.open_source.mem_nhds hq)).differentiableAt one_ne_zero
  have hy := hmaps' hq
  have key := mfderiv_comp_apply q (ld_mdifferentiableAt_symm p hy)
    (mdifferentiableAt_iff_differentiableAt.2 hΦd) ((1, 0) : ℝ × H)
  have hm : mfderiv 𝓘(ℝ, ℝ × H) 𝓘(ℝ, E) Φ q = fderiv ℝ Φ q := hΦd.hasFDerivAt.hasMFDerivAt.mfderiv
  have hm' : mfderiv 𝓘(ℝ, ℝ × H) 𝓘(ℝ, E) Φ q ((1, 0) : ℝ × H) = chartRep X p (Φ q) :=
    (DFunLike.congr_fun hm ((1, 0) : ℝ × H)).trans (hstr q hq)
  refine key.trans ?_
  rw [hm']
  exact ld_chartRep_inv X p hy

end Manifold

/-! ## ③ (b) of `lem:killing`, copied from `FlowC1.lean` and localized

The localized forms ask for `f`, `g` differentiable and the Killing equation only on the trajectory ball
`closedBall x₀ R`, and take the variational equation `D.IsVar x (D.J x)` as a hypothesis, so that they apply to
the transferred flow data of campaign 64 (where `f` is only `C¹` on a ball). The global forms of campaign 62 are
recovered as corollaries. -/

namespace FlowData

variable (D : FlowData f x₀)

/-- The flow pushes the field forward, `f (α x t) = J x t (f x)`; local form. -/
theorem ld_flow_pushes_field_loc (hfd : ∀ y ∈ closedBall x₀ D.R, DifferentiableAt ℝ f y)
    (x : E) (hx : x ∈ closedBall x₀ D.r) (hJ : D.IsVar x (D.J x))
    (t : ℝ) (ht : t ∈ Icc (-D.τ) D.τ) : f (D.α x t) = D.J x t (f x) := by
  obtain ⟨hJ0, hJd⟩ := hJ
  have key := ld_gronwall_symm (fun s => f (D.α x s) - D.J x s (f x))
    (fun s => fderiv ℝ f (D.α x s) (f (D.α x s) - D.J x s (f x))) D.τ 0 D.M 0
    (fun s hs => by
      have h1 := ((hfd _ (D.mem x hx s hs)).hasFDerivAt.comp_hasDerivWithinAt s
        (D.deriv x hx s hs))
      have h2 := (hJd s hs).clm_apply (hasDerivWithinAt_const s _ (f x))
      refine (h1.fun_sub h2).congr_deriv ?_
      simp only [map_sub, map_zero, add_zero, ContinuousLinearMap.comp_apply])
    (by simp [D.init x hx, hJ0])
    (fun s hs => by
      rw [add_zero]
      exact ((fderiv ℝ f (D.α x s)).le_opNorm _).trans
        (mul_le_mul_of_nonneg_right (D.dbound _ (D.mem x hx s hs)) (norm_nonneg _))) t ht
  rw [gronwallBound_ε0, zero_mul] at key
  exact sub_eq_zero.1 (norm_le_zero_iff.1 key)

/-- Campaign 62's `fc_flow_pushes_field`. -/
theorem ld_flow_pushes_field (hf : ContDiff ℝ 1 f) (x : E) (hx : x ∈ closedBall x₀ D.r)
    (t : ℝ) (ht : t ∈ Icc (-D.τ) D.τ) : f (D.α x t) = D.J x t (f x) :=
  D.ld_flow_pushes_field_loc (fun y _ => hf.differentiable one_ne_zero y) x hx
    (D.ld_J_spec hf x hx) t ht

/-- **Isometry**, local form: if `L_f g = 0` on the trajectory ball then `g (α x t) (J v) (J w) = g x v w`. -/
theorem ld_flow_isometry_loc (g : E → E →L[ℝ] E →L[ℝ] ℝ)
    (hg : ∀ y ∈ closedBall x₀ D.R, DifferentiableAt ℝ g y)
    (hK : ∀ y ∈ closedBall x₀ D.R, ∀ v w,
      fderiv ℝ g y (f y) v w + g y (fderiv ℝ f y v) w + g y v (fderiv ℝ f y w) = 0)
    (x : E) (hx : x ∈ closedBall x₀ D.r) (hJ : D.IsVar x (D.J x))
    (t : ℝ) (ht : t ∈ Icc (-D.τ) D.τ) (v w : E) :
    g (D.α x t) (D.J x t v) (D.J x t w) = g x v w := by
  obtain ⟨hJ0, hJd⟩ := hJ
  set Q : ℝ → ℝ := fun s => g (D.α x s) (D.J x s v) (D.J x s w) with hQ
  have hQd : ∀ s ∈ Icc (-D.τ) D.τ, HasDerivWithinAt Q 0 (Icc (-D.τ) D.τ) s := fun s hs => by
    have h1 := HasFDerivAt.comp_hasDerivWithinAt (l := g) (f := D.α x) s
      (hg _ (D.mem x hx s hs)).hasFDerivAt (D.deriv x hx s hs)
    have h2 := (hJd s hs).clm_apply (hasDerivWithinAt_const s _ v)
    have h3 := (hJd s hs).clm_apply (hasDerivWithinAt_const s _ w)
    have hz := hK _ (D.mem x hx s hs) (D.J x s v) (D.J x s w)
    refine ((h1.clm_apply h2).clm_apply h3).congr_deriv ?_
    simp only [map_zero, add_zero, ContinuousLinearMap.comp_apply, Function.comp_apply,
      add_apply]
    linarith
  have key := ld_gronwall_symm (fun s => Q s - Q 0) (fun _ => 0) D.τ 0 0 0
    (fun s hs => (hQd s hs).sub_const _) (by simp) (fun s _ => by simp) t ht
  rw [gronwallBound_ε0_δ0] at key
  have h := sub_eq_zero.1 (norm_le_zero_iff.1 key)
  simp only [hQ] at h
  rw [h]
  simp [D.init x hx, hJ0]

/-- Campaign 62's `fc_flow_isometry`. -/
theorem ld_flow_isometry (hf : ContDiff ℝ 1 f) (g : E → E →L[ℝ] E →L[ℝ] ℝ)
    (hg : Differentiable ℝ g)
    (hK : ∀ x v w, fderiv ℝ g x (f x) v w + g x (fderiv ℝ f x v) w + g x v (fderiv ℝ f x w) = 0)
    (x : E) (hx : x ∈ closedBall x₀ D.r) (t : ℝ) (ht : t ∈ Icc (-D.τ) D.τ) (v w : E) :
    g (D.α x t) (D.J x t v) (D.J x t w) = g x v w :=
  D.ld_flow_isometry_loc g (fun y _ => hg y) (fun y _ => hK y) x hx (D.ld_J_spec hf x hx) t ht v w

/-- **In the flow box**, local form: the pulled-back metric is
`(u, u') ↦ g_y (u.1 • f y + u.2) (u'.1 • f y + u'.2)`, `y = x₀ + h`; it does not involve `λ`. -/
theorem ld_flowBox_pullback_loc (hfd : ∀ y ∈ closedBall x₀ D.R, DifferentiableAt ℝ f y)
    (hJ : ∀ x ∈ closedBall x₀ D.r, D.IsVar x (D.J x)) (g : E → E →L[ℝ] E →L[ℝ] ℝ)
    (hg : ∀ y ∈ closedBall x₀ D.R, DifferentiableAt ℝ g y)
    (hK : ∀ y ∈ closedBall x₀ D.R, ∀ v w,
      fderiv ℝ g y (f y) v w + g y (fderiv ℝ f y v) w + g y v (fderiv ℝ f y w) = 0)
    {H : Submodule ℝ E} {Φ : OpenPartialHomeomorph (ℝ × H) E} (hΦ : D.IsFlowBox H Φ)
    (p : ℝ × H) (hp : p ∈ Φ.source) (u u' : ℝ × H) :
    g (Φ p) (fderiv ℝ Φ p u) (fderiv ℝ Φ p u') =
      g (x₀ + p.2) (u.1 • f (x₀ + p.2) + u.2) (u'.1 • f (x₀ + p.2) + u'.2) := by
  obtain ⟨ht, hy⟩ := hΦ.source_sub p hp
  have hyc := ball_subset_closedBall hy
  have htc := Ioo_subset_Icc_self ht
  have hpush := D.ld_flow_pushes_field_loc hfd _ hyc (hJ _ hyc) _ htc
  have hlin : ∀ u : ℝ × H, fderiv ℝ Φ p u = D.J (x₀ + p.2) p.1 (u.1 • f (x₀ + p.2) + u.2) := by
    intro u
    rw [hΦ.fderiv_eq p hp u, hΦ.apply_eq p hp, hpush, map_add, map_smul]
  rw [hlin, hlin, hΦ.apply_eq p hp]
  exact D.ld_flow_isometry_loc g hg hK _ hyc (hJ _ hyc) _ htc _ _

/-- Campaign 62's `fc_flowBox_pullback`. -/
theorem ld_flowBox_pullback (hf : ContDiff ℝ 1 f) (g : E → E →L[ℝ] E →L[ℝ] ℝ)
    (hg : Differentiable ℝ g)
    (hK : ∀ x v w, fderiv ℝ g x (f x) v w + g x (fderiv ℝ f x v) w + g x v (fderiv ℝ f x w) = 0)
    {H : Submodule ℝ E} {Φ : OpenPartialHomeomorph (ℝ × H) E} (hΦ : D.IsFlowBox H Φ)
    (p : ℝ × H) (hp : p ∈ Φ.source) (u u' : ℝ × H) :
    g (Φ p) (fderiv ℝ Φ p u) (fderiv ℝ Φ p u') =
      g (x₀ + p.2) (u.1 • f (x₀ + p.2) + u.2) (u'.1 • f (x₀ + p.2) + u'.2) :=
  D.ld_flowBox_pullback_loc (fun y _ => hf.differentiable one_ne_zero y)
    (fun x hx => D.ld_J_spec hf x hx) g (fun y _ => hg y) (fun y _ => hK y) hΦ p hp u u'

/-- Campaign 62's `fc_flowBox_killing`: `∂_λ g_ab = 0`. -/
theorem ld_flowBox_killing (hf : ContDiff ℝ 1 f) (g : E → E →L[ℝ] E →L[ℝ] ℝ)
    (hg : Differentiable ℝ g)
    (hK : ∀ x v w, fderiv ℝ g x (f x) v w + g x (fderiv ℝ f x v) w + g x v (fderiv ℝ f x w) = 0)
    {H : Submodule ℝ E} {Φ : OpenPartialHomeomorph (ℝ × H) E} (hΦ : D.IsFlowBox H Φ)
    (p q : ℝ × H) (hp : p ∈ Φ.source) (hq : q ∈ Φ.source) (hpq : p.2 = q.2) (u u' : ℝ × H) :
    g (Φ p) (fderiv ℝ Φ p u) (fderiv ℝ Φ p u') = g (Φ q) (fderiv ℝ Φ q u) (fderiv ℝ Φ q u') := by
  rw [D.ld_flowBox_pullback hf g hg hK hΦ p hp, D.ld_flowBox_pullback hf g hg hK hΦ q hq, hpq]

/-- The transferred flow data (campaign 64) solves the variational equation of `f`. -/
theorem ld_transfer_isVar {g : E → E} (hg : ContDiff ℝ 1 g) (D : FlowData g x₀)
    (hfg : ∀ y ∈ closedBall x₀ D.R, f y = g y ∧ fderiv ℝ f y = fderiv ℝ g y)
    (x : E) (hx : x ∈ closedBall x₀ D.r) : (D.transfer hfg).IsVar x ((D.transfer hfg).J x) := by
  rw [D.ld_transfer_J hfg x hx]
  obtain ⟨h0, hd⟩ := D.ld_J_spec hg x hx
  unfold IsVar
  dsimp only [transfer]
  exact ⟨h0, fun t ht => by rw [(hfg _ (D.mem x hx t ht)).2]; exact hd t ht⟩

end FlowData

/-- **The local flow box, with the variational equation.** As `ld_flowBox_exists_of_contDiffOn`, and the flow
data solve the variational equation of `f` on `closedBall x₀ r`. -/
theorem ld_flowBox_exists_of_contDiffOn_var {ρ : ℝ} (hρ : 0 < ρ) (hf : ContDiffOn ℝ 1 f (ball x₀ ρ))
    (hfx : f x₀ ≠ 0) :
    ∃ (H : Submodule ℝ E) (D : FlowData f x₀) (Φ : OpenPartialHomeomorph (ℝ × H) E),
      D.IsFlowBox H Φ ∧ D.R < ρ / 4 ∧ ∀ x ∈ closedBall x₀ D.r, D.IsVar x (D.J x) := by
  obtain ⟨g, hg, hgf⟩ := ld_cutoff hρ hf
  obtain ⟨D, hD⟩ := ld_flowData_small hg x₀ (by positivity : 0 < ρ / 4)
  have hfg := ld_agree hgf hD
  have hx₀ := (hfg x₀ D.ld_x₀_mem).1
  obtain ⟨H, hH⟩ := Submodule.exists_isCompl (ℝ ∙ f x₀)
  rw [hx₀] at hfx hH
  obtain ⟨Φ, hΦ⟩ := D.ld_flowBox hg hfx H hH
  exact ⟨H, D.transfer hfg, Φ, D.ld_transfer_isFlowBox hfg hΦ, hD,
    fun x hx => FlowData.ld_transfer_isVar hg D hfg x hx⟩

/-- **`lem:killing` (b) for the local flow box.** `f` `C¹` on `ball x₀ ρ`, `f x₀ ≠ 0`, `g` differentiable on the
ball with `L_f g = 0` there. Then there is a flow-box chart `Φ` into `ball x₀ (ρ / 4)` with `DΦ · (1, 0) = f ∘ Φ`
in which the pulled-back metric is `g_{x₀+h} (u.1 • f + u.2) (u'.1 • f + u'.2)`: `λ`-independent. -/
theorem ld_flowBox_killing_of_contDiffOn {ρ : ℝ} (hρ : 0 < ρ) (hf : ContDiffOn ℝ 1 f (ball x₀ ρ))
    (hfx : f x₀ ≠ 0) (g : E → E →L[ℝ] E →L[ℝ] ℝ) (hg : DifferentiableOn ℝ g (ball x₀ ρ))
    (hK : ∀ y ∈ ball x₀ ρ, ∀ v w,
      fderiv ℝ g y (f y) v w + g y (fderiv ℝ f y v) w + g y v (fderiv ℝ f y w) = 0) :
    ∃ (H : Submodule ℝ E) (Φ : OpenPartialHomeomorph (ℝ × H) E),
      ((0 : ℝ), (0 : H)) ∈ Φ.source ∧ Φ (0, 0) = x₀ ∧ MapsTo Φ Φ.source (ball x₀ (ρ / 4)) ∧
      ContDiffOn ℝ 1 Φ Φ.source ∧ (∀ q ∈ Φ.source, fderiv ℝ Φ q (1, 0) = f (Φ q)) ∧
      (∀ q ∈ Φ.source, x₀ + (q.2 : E) ∈ ball x₀ (ρ / 4)) ∧
      ∀ q ∈ Φ.source, ∀ u u' : ℝ × H, g (Φ q) (fderiv ℝ Φ q u) (fderiv ℝ Φ q u') =
        g (x₀ + q.2) (u.1 • f (x₀ + q.2) + u.2) (u'.1 • f (x₀ + q.2) + u'.2) := by
  obtain ⟨H, D, Φ, hΦ, hR, hJ⟩ := ld_flowBox_exists_of_contDiffOn_var hρ hf hfx
  have hsub : closedBall x₀ D.R ⊆ ball x₀ ρ :=
    (closedBall_subset_ball hR).trans (ball_subset_ball (by linarith))
  have hfd : ∀ y ∈ closedBall x₀ D.R, DifferentiableAt ℝ f y := fun y hy =>
    (hf.differentiableOn one_ne_zero).differentiableAt (isOpen_ball.mem_nhds (hsub hy))
  have hgd : ∀ y ∈ closedBall x₀ D.R, DifferentiableAt ℝ g y := fun y hy =>
    hg.differentiableAt (isOpen_ball.mem_nhds (hsub hy))
  have hrR : ∀ q ∈ Φ.source, x₀ + (q.2 : E) ∈ closedBall x₀ D.R := fun q hq => by
    have hy := ball_subset_closedBall (hΦ.source_sub q hq).2
    have := D.mem _ hy 0 ⟨by linarith [D.τ_pos], D.τ_pos.le⟩
    rwa [D.init _ hy] at this
  exact ⟨H, Φ, hΦ.zero_mem, hΦ.map_zero,
    fun q hq => closedBall_subset_ball hR (D.ld_isFlowBox_mem hΦ q hq), hΦ.contDiffOn,
    hΦ.straightens, fun q hq => closedBall_subset_ball hR (hrR q hq),
    fun q hq u u' => D.ld_flowBox_pullback_loc hfd hJ g hgd
      (fun y hy => hK y (hsub hy)) hΦ q hq u u'⟩

/-! ## ③ (b), linked to `LieDerivProbe.lean`'s `IsKilling` (copied from `FlowC1.lean`)

`lieDerivForm`, `IsConformalKilling` and `IsKilling` are copied verbatim from `LieDerivProbe.lean` (P1, P2). -/

section LieLink

open Manifold VectorField
open scoped ContDiff

variable {E' : Type*} [NormedAddCommGroup E'] [NormedSpace ℝ E']
  {H' : Type*} [TopologicalSpace H'] {I : ModelWithCorners ℝ E' H'}
  {M : Type*} [TopologicalSpace M] [ChartedSpace H' M] [IsManifold I 1 M]

/-- Copied from `LieDerivProbe.lean` (P1). -/
noncomputable def lieDerivForm (g : Π x : M, TangentSpace I x →L[ℝ] TangentSpace I x →L[ℝ] ℝ)
    (X Y Z : Π x : M, TangentSpace I x) (x : M) : ℝ :=
  (show ℝ from mfderiv I 𝓘(ℝ, ℝ) (fun y => g y (Y y) (Z y)) x (X x))
    - g x (mlieBracket I X Y x) (Z x) - g x (Y x) (mlieBracket I X Z x)

/-- Copied from `LieDerivProbe.lean` (P2). -/
def IsConformalKilling (g : Π x : M, TangentSpace I x →L[ℝ] TangentSpace I x →L[ℝ] ℝ)
    (X : Π x : M, TangentSpace I x) (σ : M → ℝ) (x : M) : Prop :=
  ∀ Y Z : Π x : M, TangentSpace I x, CMDiffAt 1 (T% Y) x → CMDiffAt 1 (T% Z) x →
    lieDerivForm g X Y Z x = 2 * σ x * g x (Y x) (Z x)

/-- Copied from `LieDerivProbe.lean` (P2). -/
def IsKilling (g : Π x : M, TangentSpace I x →L[ℝ] TangentSpace I x →L[ℝ] ℝ)
    (X : Π x : M, TangentSpace I x) (x : M) : Prop :=
  IsConformalKilling g X 0 x

end LieLink

section LieLinkE

open Manifold VectorField
open scoped ContDiff

/-- Campaign 62's `fc_isKilling_lie`, with `g` differentiable only at `x`: on the model space,
`IsKilling g X x` (tested with constant fields) gives `Dg_x (X x) v w + g_x (DX_x v) w + g_x v (DX_x w) = 0`. -/
theorem ld_isKilling_lie (g : E → E →L[ℝ] E →L[ℝ] ℝ) (X : E → E) (x : E)
    (hg : DifferentiableAt ℝ g x)
    (hK : IsKilling (I := 𝓘(ℝ, E)) (M := E) g X x) (v w : E) :
    fderiv ℝ g x (X x) v w + g x (fderiv ℝ X x v) w +
      g x v (fderiv ℝ X x w) = 0 := by
  set Y : Π y : E, TangentSpace 𝓘(ℝ, E) y := fun _ => v with hY
  set Z : Π y : E, TangentSpace 𝓘(ℝ, E) y := fun _ => w with hZ
  have hYc : CMDiffAt 1 (T% Y) x := by
    rw [contMDiffAt_vectorSpace_iff_contDiffAt]; exact contDiffAt_const
  have hZc : CMDiffAt 1 (T% Z) x := by
    rw [contMDiffAt_vectorSpace_iff_contDiffAt]; exact contDiffAt_const
  have h := hK Y Z hYc hZc
  have hbr : ∀ V W : Π y : E, TangentSpace 𝓘(ℝ, E) y, mlieBracket 𝓘(ℝ, E) V W x =
      fderiv ℝ (W : E → E) x (V x) - fderiv ℝ (V : E → E) x (W x) := by
    intro V W
    rw [← mlieBracketWithin_univ, mlieBracketWithin_eq_lieBracketWithin]
    set W' : E → E := W
    set V' : E → E := V
    show fderivWithin ℝ W' Set.univ x (V' x) - fderivWithin ℝ V' Set.univ x (W' x) = _
    rw [fderivWithin_univ, fderivWithin_univ]
  have hd : HasFDerivAt (fun y : E => (g y v) w) (((fderiv ℝ g x).flip v).flip w) x := by
    have := (hg.hasFDerivAt.clm_apply (hasFDerivAt_const v x)).clm_apply (hasFDerivAt_const w x)
    convert this using 1
    ext u; simp
  have hm : (show ℝ from mfderiv 𝓘(ℝ, E) 𝓘(ℝ, ℝ) (fun y => g y (Y y) (Z y)) x (X x)) =
      fderiv ℝ (fun y : E => (g y v) w) x (X x) := by
    rw [mfderiv_eq_fderiv]
    rfl
  have key : lieDerivForm g X Y Z x = fderiv ℝ (fun y : E => (g y v) w) x (X x) -
      g x (mlieBracket 𝓘(ℝ, E) X Y x) (Z x) - g x (Y x) (mlieBracket 𝓘(ℝ, E) X Z x) :=
    congrArg (fun a : ℝ => a - g x (mlieBracket 𝓘(ℝ, E) X Y x) (Z x) -
      g x (Y x) (mlieBracket 𝓘(ℝ, E) X Z x)) hm
  have hb1 : mlieBracket 𝓘(ℝ, E) X Y x = -fderiv ℝ X x v := (hbr X Y).trans (by
    show fderiv ℝ (fun _ : E => v) x (X x) - fderiv ℝ X x v = -fderiv ℝ X x v; simp)
  have hb2 : mlieBracket 𝓘(ℝ, E) X Z x = -fderiv ℝ X x w := (hbr X Z).trans (by
    show fderiv ℝ (fun _ : E => w) x (X x) - fderiv ℝ X x w = -fderiv ℝ X x w; simp)
  have aux : ∀ b1 b2 : E, b1 = -fderiv ℝ X x v → b2 = -fderiv ℝ X x w →
      fderiv ℝ (fun y : E => (g y v) w) x (X x) - g x b1 w - g x v b2 = 2 * 0 * g x v w →
      fderiv ℝ g x (X x) v w + g x (fderiv ℝ X x v) w + g x v (fderiv ℝ X x w) = 0 := by
    rintro b1 b2 rfl rfl h
    rw [hd.fderiv] at h
    simp only [map_neg, neg_apply, ContinuousLinearMap.flip_apply, mul_zero,
      zero_mul] at h
    linarith
  rw [key] at h
  exact aux _ _ hb1 hb2 h

/-- Campaign 62's `fc_flowBox_killing_of_isKilling`. -/
theorem ld_flowBox_killing_of_isKilling (hf : ContDiff ℝ 1 f) (D : FlowData f x₀)
    (g : E → E →L[ℝ] E →L[ℝ] ℝ) (hg : Differentiable ℝ g)
    (hK : ∀ x, IsKilling (I := 𝓘(ℝ, E)) (M := E) g f x)
    {H : Submodule ℝ E} {Φ : OpenPartialHomeomorph (ℝ × H) E} (hΦ : D.IsFlowBox H Φ)
    (p : ℝ × H) (hp : p ∈ Φ.source) (u u' : ℝ × H) :
    g (Φ p) (fderiv ℝ Φ p u) (fderiv ℝ Φ p u') =
      g (x₀ + p.2) (u.1 • f (x₀ + p.2) + u.2) (u'.1 • f (x₀ + p.2) + u'.2) :=
  D.ld_flowBox_pullback hf g hg
    (fun x v w => ld_isKilling_lie g f x (hg x) (hK x) v w) hΦ p hp u u'

end LieLinkE

/-! ## ① The section form of the field's `C¹` hypothesis

The trivialisation of `TangentBundle 𝓘(ℝ, E) N` at `p` has fibre map `mfderiv (extChartAt p)` on the chart source
(`TangentBundle.continuousLinearMapAt_trivializationAt`), so `chartRep X p` is the trivialisation coordinate of the
section read through `(extChartAt p).symm`. `contMDiffAt_section` reads smoothness at `p` in the trivialisation at
`p` (needing only `IsManifold 𝓘(ℝ, E) 1 N`). At other points `x` of the chart, smoothness is defined through the
trivialisation at `x`; changing it to the one at `p` (`Trivialization.contMDiffOn_section_iff`) needs the tangent
bundle to be a `C¹` vector bundle, i.e. `IsManifold 𝓘(ℝ, E) 2 N`. -/

section ManifoldSection

open Manifold Bundle

variable {N : Type*} [TopologicalSpace N] [ChartedSpace E N] [IsManifold 𝓘(ℝ, E) 1 N]

/-- On the chart target, `chartRep X p y` is the fibre coordinate of `⟨φ⁻¹ y, X (φ⁻¹ y)⟩` in the tangent-bundle
trivialisation at `p`. -/
theorem ld_chartRep_eq_triv (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N) {y : E}
    (hy : y ∈ (extChartAt 𝓘(ℝ, E) p).target) :
    chartRep (E := E) X p y = (trivializationAt E (TangentSpace 𝓘(ℝ, E)) p
      (⟨(extChartAt 𝓘(ℝ, E) p).symm y, X ((extChartAt 𝓘(ℝ, E) p).symm y)⟩ :
        TangentBundle 𝓘(ℝ, E) N)).2 := by
  have hx : (extChartAt 𝓘(ℝ, E) p).symm y ∈ (chartAt E p).source := by
    rw [← extChartAt_source 𝓘(ℝ, E)]; exact (extChartAt 𝓘(ℝ, E) p).map_target hy
  rw [← Trivialization.continuousLinearMapAt_apply_of_mem (R := ℝ) _ (by simpa using hx),
    TangentBundle.continuousLinearMapAt_trivializationAt hx]
  rfl

/-- If the trivialisation coordinate (at `p`) of the section is `C¹` at a point `x` of the chart, then
`chartRep X p` is `C¹` at `φ x`. -/
theorem ld_chartRep_contDiffAt_of_triv (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N) {x : N}
    (hx : x ∈ (chartAt E p).source)
    (hF : ContMDiffAt 𝓘(ℝ, E) 𝓘(ℝ, E) 1 (fun z ↦ (trivializationAt E (TangentSpace 𝓘(ℝ, E)) p
      (⟨z, X z⟩ : TangentBundle 𝓘(ℝ, E) N)).2) x) :
    ContDiffAt ℝ 1 (chartRep (E := E) X p) (extChartAt 𝓘(ℝ, E) p x) := by
  set e := extChartAt 𝓘(ℝ, E) p with he
  have hxs : x ∈ e.source := by rwa [extChartAt_source]
  have hy : e x ∈ e.target := e.map_source hxs
  have hto : IsOpen e.target := isOpen_extChartAt_target p
  have h1 : ContMDiffAt 𝓘(ℝ, E) 𝓘(ℝ, E) 1 e.symm (e x) :=
    (contMDiffOn_extChartAt_symm p).contMDiffAt (hto.mem_nhds hy)
  have h2 := hF.comp_of_eq h1 (e.left_inv hxs)
  rw [contMDiffAt_iff_contDiffAt] at h2
  refine h2.congr_of_eventuallyEq ?_
  filter_upwards [hto.mem_nhds hy] with y hy'
  exact ld_chartRep_eq_triv X p hy'

/-- **① at the point.** The section `x ↦ ⟨x, X x⟩` `C¹` at `p` (into `TangentBundle 𝓘(ℝ, E) N`) gives
`chartRep X p` `C¹` at `extChartAt p p`. -/
theorem ld_chartRep_contDiffAt_of_section (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N)
    (hX : ContMDiffAt 𝓘(ℝ, E) 𝓘(ℝ, E).tangent 1
      (fun x ↦ (⟨x, X x⟩ : TangentBundle 𝓘(ℝ, E) N)) p) :
    ContDiffAt ℝ 1 (chartRep (E := E) X p) (extChartAt 𝓘(ℝ, E) p p) :=
  ld_chartRep_contDiffAt_of_triv X p (mem_chart_source E p) ((contMDiffAt_section p).1 hX)

/-- `C¹` at `extChartAt p p` gives `C¹` on a ball around it inside the chart target. -/
theorem ld_chartRep_ball_of_contDiffAt (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N)
    (hX : ContDiffAt ℝ 1 (chartRep (E := E) X p) (extChartAt 𝓘(ℝ, E) p p)) :
    ∃ ρ > 0, ball (extChartAt 𝓘(ℝ, E) p p) ρ ⊆ (extChartAt 𝓘(ℝ, E) p).target ∧
      ContDiffOn ℝ 1 (chartRep (E := E) X p) (ball (extChartAt 𝓘(ℝ, E) p p) ρ) := by
  have h := (hX.eventually (by simp)).and
    ((isOpen_extChartAt_target p).mem_nhds (mem_extChartAt_target p))
  obtain ⟨ρ, hρ, hb⟩ := Metric.eventually_nhds_iff_ball.1 h
  exact ⟨ρ, hρ, fun y hy => (hb y hy).2, fun y hy => (hb y hy).1.contDiffWithinAt⟩

/-- **① on a neighbourhood.** The section `C¹` at `p` gives `chartRep X p` `C¹` on a ball around
`extChartAt p p` inside the chart target. -/
theorem ld_chartRep_ball_of_section (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N)
    (hX : ContMDiffAt 𝓘(ℝ, E) 𝓘(ℝ, E).tangent 1
      (fun x ↦ (⟨x, X x⟩ : TangentBundle 𝓘(ℝ, E) N)) p) :
    ∃ ρ > 0, ball (extChartAt 𝓘(ℝ, E) p p) ρ ⊆ (extChartAt 𝓘(ℝ, E) p).target ∧
      ContDiffOn ℝ 1 (chartRep (E := E) X p) (ball (extChartAt 𝓘(ℝ, E) p p) ρ) :=
  ld_chartRep_ball_of_contDiffAt X p (ld_chartRep_contDiffAt_of_section X p hX)

/-- `X p ≠ 0` gives `chartRep X p (φ p) ≠ 0`. -/
theorem ld_chartRep_ne_zero (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N) (hXp : X p ≠ 0) :
    chartRep (E := E) X p (extChartAt 𝓘(ℝ, E) p p) ≠ 0 := by
  set e := extChartAt 𝓘(ℝ, E) p with he
  have hx0 : e p ∈ e.target := mem_extChartAt_target p
  have hep : e.symm (e p) = p := e.left_inv (mem_extChartAt_source p)
  intro h
  apply hXp
  have := ld_chartRep_inv X p hx0
  rw [h] at this
  have hz := (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p).symm (e p)).map_zero
  have key : ∀ z, z = p → X z = 0 → X p = 0 := by rintro z rfl h; exact h
  exact key _ hep (this.symm.trans hz)

/-- A chart `Φ` into the chart target with `DΦ · (1, 0) = chartRep X p ∘ Φ` straightens `X` on `N`:
`mfderiv ((extChartAt p).symm ∘ Φ) q (1, 0) = X (ψ q)`. -/
theorem ld_mfderiv_straightens (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N) {H : Submodule ℝ E}
    (Φ : OpenPartialHomeomorph (ℝ × H) E)
    (hmaps : MapsTo Φ Φ.source (extChartAt 𝓘(ℝ, E) p).target) (hc : ContDiffOn ℝ 1 Φ Φ.source)
    (hstr : ∀ q ∈ Φ.source, fderiv ℝ Φ q (1, 0) = chartRep (E := E) X p (Φ q))
    (q : ℝ × H) (hq : q ∈ Φ.source) :
    mfderiv 𝓘(ℝ, ℝ × H) 𝓘(ℝ, E) ((extChartAt 𝓘(ℝ, E) p).symm ∘ Φ) q (1, 0) =
      X (((extChartAt 𝓘(ℝ, E) p).symm ∘ Φ) q) := by
  have hΦd : DifferentiableAt ℝ Φ q :=
    (hc.contDiffAt (Φ.open_source.mem_nhds hq)).differentiableAt one_ne_zero
  have hy := hmaps hq
  have key := mfderiv_comp_apply q (ld_mdifferentiableAt_symm p hy)
    (mdifferentiableAt_iff_differentiableAt.2 hΦd) ((1, 0) : ℝ × H)
  have hm : mfderiv 𝓘(ℝ, ℝ × H) 𝓘(ℝ, E) Φ q = fderiv ℝ Φ q := hΦd.hasFDerivAt.hasMFDerivAt.mfderiv
  have hm' : mfderiv 𝓘(ℝ, ℝ × H) 𝓘(ℝ, E) Φ q ((1, 0) : ℝ × H) = chartRep X p (Φ q) :=
    (DFunLike.congr_fun hm ((1, 0) : ℝ × H)).trans (hstr q hq)
  refine key.trans ?_
  rw [hm']
  exact ld_chartRep_inv X p hy

/-- **`ld_manifold_flowBox` from `C¹` at the point only.** -/
theorem ld_manifold_flowBox_of_contDiffAt (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N)
    (hX : ContDiffAt ℝ 1 (chartRep (E := E) X p) (extChartAt 𝓘(ℝ, E) p p)) (hXp : X p ≠ 0) :
    ∃ (H : Submodule ℝ E) (Φ : OpenPartialHomeomorph (ℝ × H) E),
      ((0 : ℝ), (0 : H)) ∈ Φ.source ∧ Φ (0, 0) = extChartAt 𝓘(ℝ, E) p p ∧
      ((extChartAt 𝓘(ℝ, E) p).symm ∘ Φ) (0, 0) = p ∧
      MapsTo Φ Φ.source (extChartAt 𝓘(ℝ, E) p).target ∧ ContDiffOn ℝ 1 Φ Φ.source ∧
      (∀ q ∈ Φ.source, fderiv ℝ Φ q (1, 0) = chartRep X p (Φ q)) ∧
      (∀ q ∈ Φ.source, mfderiv 𝓘(ℝ, ℝ × H) 𝓘(ℝ, E) ((extChartAt 𝓘(ℝ, E) p).symm ∘ Φ) q (1, 0) =
        X (((extChartAt 𝓘(ℝ, E) p).symm ∘ Φ) q)) := by
  obtain ⟨ρ, hρ, hball, hf⟩ := ld_chartRep_ball_of_contDiffAt X p hX
  obtain ⟨H, Φ, h0, hΦ0, -, hmaps, hc, -, hstr, -⟩ :=
    ld_flowBox_chart_of_contDiffOn hρ hf (ld_chartRep_ne_zero X p hXp)
  have hmaps' : MapsTo Φ Φ.source (extChartAt 𝓘(ℝ, E) p).target := fun q hq =>
    hball (ball_subset_ball (by linarith) (hmaps hq))
  exact ⟨H, Φ, h0, hΦ0, by simp [hΦ0], hmaps', hc, hstr,
    ld_mfderiv_straightens X p Φ hmaps' hc hstr⟩

/-- **① `ld_manifold_flowBox` with the section hypothesis at `p`.** If the section `x ↦ ⟨x, X x⟩` of
`TangentBundle 𝓘(ℝ, E) N` is `C¹` at `p` and `X p ≠ 0`, there is a flow box `Φ` in the chart at `p` with
`ψ = (extChartAt p).symm ∘ Φ`, `ψ (0, 0) = p`, `mfderiv ψ q (1, 0) = X (ψ q)`. -/
theorem ld_manifold_flowBox_section (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N)
    (hX : ContMDiffAt 𝓘(ℝ, E) 𝓘(ℝ, E).tangent 1
      (fun x ↦ (⟨x, X x⟩ : TangentBundle 𝓘(ℝ, E) N)) p) (hXp : X p ≠ 0) :
    ∃ (H : Submodule ℝ E) (Φ : OpenPartialHomeomorph (ℝ × H) E),
      ((0 : ℝ), (0 : H)) ∈ Φ.source ∧ Φ (0, 0) = extChartAt 𝓘(ℝ, E) p p ∧
      ((extChartAt 𝓘(ℝ, E) p).symm ∘ Φ) (0, 0) = p ∧
      MapsTo Φ Φ.source (extChartAt 𝓘(ℝ, E) p).target ∧ ContDiffOn ℝ 1 Φ Φ.source ∧
      (∀ q ∈ Φ.source, fderiv ℝ Φ q (1, 0) = chartRep X p (Φ q)) ∧
      (∀ q ∈ Φ.source, mfderiv 𝓘(ℝ, ℝ × H) 𝓘(ℝ, E) ((extChartAt 𝓘(ℝ, E) p).symm ∘ Φ) q (1, 0) =
        X (((extChartAt 𝓘(ℝ, E) p).symm ∘ Φ) q)) :=
  ld_manifold_flowBox_of_contDiffAt X p (ld_chartRep_contDiffAt_of_section X p hX) hXp

end ManifoldSection

section ManifoldSection2

open Manifold Bundle

variable {N : Type*} [TopologicalSpace N] [ChartedSpace E N] [IsManifold 𝓘(ℝ, E) 2 N]

/-- **① on the whole chart.** On a `C²` manifold, the section `x ↦ ⟨x, X x⟩` `C¹` on the chart source at `p`
gives `chartRep X p` `C¹` on the whole chart target. -/
theorem ld_chartRep_contDiffOn_of_section (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N)
    (hX : ContMDiffOn 𝓘(ℝ, E) 𝓘(ℝ, E).tangent 1
      (fun x ↦ (⟨x, X x⟩ : TangentBundle 𝓘(ℝ, E) N)) (chartAt E p).source) :
    ContDiffOn ℝ 1 (chartRep (E := E) X p) (extChartAt 𝓘(ℝ, E) p).target := by
  have : IsManifold 𝓘(ℝ, E) 1 N := IsManifold.of_le (n := 2) (by norm_num)
  intro y hy
  set e := extChartAt 𝓘(ℝ, E) p with he
  have hxs : e.symm y ∈ e.source := e.map_target hy
  have hx : e.symm y ∈ (chartAt E p).source := by rwa [extChartAt_source] at hxs
  have hF := ((Trivialization.contMDiffOn_section_iff (trivializationAt E (TangentSpace 𝓘(ℝ, E)) p)
    (chartAt E p).open_source (by simp)).1 hX).contMDiffAt ((chartAt E p).open_source.mem_nhds hx)
  have := ld_chartRep_contDiffAt_of_triv X p hx hF
  rw [e.right_inv hy] at this
  exact this.contDiffWithinAt

/-- **① `ld_manifold_flowBox` with the section hypothesis on the chart source** (`C²` manifold): the
registered statement, through `ld_chartRep_contDiffOn_of_section` and campaign 64's `ld_manifold_flowBox`. -/
theorem ld_manifold_flowBox_sectionOn (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N)
    (hX : ContMDiffOn 𝓘(ℝ, E) 𝓘(ℝ, E).tangent 1
      (fun x ↦ (⟨x, X x⟩ : TangentBundle 𝓘(ℝ, E) N)) (chartAt E p).source) (hXp : X p ≠ 0) :
    ∃ (H : Submodule ℝ E) (Φ : OpenPartialHomeomorph (ℝ × H) E),
      ((0 : ℝ), (0 : H)) ∈ Φ.source ∧ Φ (0, 0) = extChartAt 𝓘(ℝ, E) p p ∧
      ((extChartAt 𝓘(ℝ, E) p).symm ∘ Φ) (0, 0) = p ∧
      MapsTo Φ Φ.source (extChartAt 𝓘(ℝ, E) p).target ∧ ContDiffOn ℝ 1 Φ Φ.source ∧
      (∀ q ∈ Φ.source, fderiv ℝ Φ q (1, 0) = chartRep X p (Φ q)) ∧
      (∀ q ∈ Φ.source, mfderiv 𝓘(ℝ, ℝ × H) 𝓘(ℝ, E) ((extChartAt 𝓘(ℝ, E) p).symm ∘ Φ) q (1, 0) =
        X (((extChartAt 𝓘(ℝ, E) p).symm ∘ Φ) q)) := by
  have : IsManifold 𝓘(ℝ, E) 1 N := IsManifold.of_le (n := 2) (by norm_num)
  exact ld_manifold_flowBox X p (ld_chartRep_contDiffOn_of_section X p hX) hXp

end ManifoldSection2

/-! ## ② `lem:killing` (b) on a manifold, metric and Killing condition in chart form

The metric is given in the chart at `p` as `gc : E → E →L E →L ℝ` (on the chart target), and `X` is Killing in
campaign 62's coordinate sense: `IsKilling gc (chartRep X p)` on the model space. Mathlib has no Lie derivative of
`(0,2)`-tensor fields on `N`, so the coordinate-free Killing condition on `N` is not stated. -/

section ManifoldKilling

open Manifold

variable {N : Type*} [TopologicalSpace N] [ChartedSpace E N] [IsManifold 𝓘(ℝ, E) 1 N]

/-- A local Killing chart around `p` (the local form of campaign 59's `KillingChart`): a flow box `Φ` in the
chart at `p`, `ψ = (extChartAt p).symm ∘ Φ`, with `X = ∂_λ` (`mfderiv ψ q (1, 0) = X (ψ q)`) and the metric
pulled back by `Φ`, `gc (Φ q) (DΦ u) (DΦ u')`, a function `gH q.2 u u'` of the transverse coordinate only. -/
structure LocalKillingChart (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N)
    (gc : E → E →L[ℝ] E →L[ℝ] ℝ) where
  H : Submodule ℝ E
  Φ : OpenPartialHomeomorph (ℝ × H) E
  zero_mem : ((0 : ℝ), (0 : H)) ∈ Φ.source
  map_zero : Φ (0, 0) = extChartAt 𝓘(ℝ, E) p p
  ψ_zero : ((extChartAt 𝓘(ℝ, E) p).symm ∘ Φ) (0, 0) = p
  mapsTo : MapsTo Φ Φ.source (extChartAt 𝓘(ℝ, E) p).target
  contDiffOn : ContDiffOn ℝ 1 Φ Φ.source
  /-- `X = ∂_λ` on `N`. -/
  straightens : ∀ q ∈ Φ.source,
    mfderiv 𝓘(ℝ, ℝ × H) 𝓘(ℝ, E) ((extChartAt 𝓘(ℝ, E) p).symm ∘ Φ) q (1, 0) =
      X (((extChartAt 𝓘(ℝ, E) p).symm ∘ Φ) q)
  /-- The pulled-back metric components, as a function of `h` only. -/
  gH : H → (ℝ × H) → (ℝ × H) → ℝ
  metric_eq : ∀ q ∈ Φ.source, ∀ u u' : ℝ × H,
    gc (Φ q) (fderiv ℝ Φ q u) (fderiv ℝ Φ q u') = gH q.2 u u'

/-- `∂_λ g_ab = 0` in a local Killing chart: two source points with the same `h` see the same components. -/
theorem LocalKillingChart.ld_lambda_indep {X : Π x : N, TangentSpace 𝓘(ℝ, E) x} {p : N}
    {gc : E → E →L[ℝ] E →L[ℝ] ℝ} (K : LocalKillingChart X p gc) (q q' : ℝ × K.H)
    (hq : q ∈ K.Φ.source) (hq' : q' ∈ K.Φ.source) (h : q.2 = q'.2) (u u' : ℝ × K.H) :
    gc (K.Φ q) (fderiv ℝ K.Φ q u) (fderiv ℝ K.Φ q u') =
      gc (K.Φ q') (fderiv ℝ K.Φ q' u) (fderiv ℝ K.Φ q' u') := by
  rw [K.metric_eq q hq, K.metric_eq q' hq', h]

/-- **② `lem:killing` (b) on a manifold.** `X` a vector field on `N` with `chartRep X p` `C¹` at `φ p`,
`X p ≠ 0`; `gc` a field of bilinear forms on the chart target, differentiable there, with `chartRep X p` Killing
for `gc` (`IsKilling`, the model-space Lie derivative) at every point of the chart target. Then there is a local
Killing chart around `p`: `X = ∂_λ`, and the pulled-back metric is
`gH h u u' = gc_{φp+h} (u.1 • X̃ + u.2) (u'.1 • X̃ + u'.2)`, `X̃ = chartRep X p (φ p + h)`, independent of `λ`. -/
theorem ld_manifold_killingChart (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N)
    (gc : E → E →L[ℝ] E →L[ℝ] ℝ)
    (hX : ContDiffAt ℝ 1 (chartRep (E := E) X p) (extChartAt 𝓘(ℝ, E) p p)) (hXp : X p ≠ 0)
    (hgc : DifferentiableOn ℝ gc (extChartAt 𝓘(ℝ, E) p).target)
    (hK : ∀ y ∈ (extChartAt 𝓘(ℝ, E) p).target,
      IsKilling (I := 𝓘(ℝ, E)) (M := E) gc (chartRep (E := E) X p) y) :
    Nonempty (LocalKillingChart X p gc) := by
  set e := extChartAt 𝓘(ℝ, E) p with he
  have hto : IsOpen e.target := isOpen_extChartAt_target p
  obtain ⟨ρ, hρ, hball, hf⟩ := ld_chartRep_ball_of_contDiffAt X p hX
  have hgd : DifferentiableOn ℝ gc (ball (e p) ρ) := hgc.mono hball
  have hKb : ∀ y ∈ ball (e p) ρ, ∀ v w, fderiv ℝ gc y (chartRep X p y) v w +
      gc y (fderiv ℝ (chartRep X p) y v) w + gc y v (fderiv ℝ (chartRep X p) y w) = 0 :=
    fun y hy v w => ld_isKilling_lie gc (chartRep X p) y
      (hgc.differentiableAt (hto.mem_nhds (hball hy))) (hK y (hball hy)) v w
  obtain ⟨H, Φ, h0, hΦ0, hmaps, hc, hstr, -, hpull⟩ :=
    ld_flowBox_killing_of_contDiffOn hρ hf (ld_chartRep_ne_zero X p hXp) gc hgd hKb
  have hmaps' : MapsTo Φ Φ.source e.target := fun q hq =>
    hball (ball_subset_ball (by linarith) (hmaps hq))
  exact ⟨⟨H, Φ, h0, hΦ0, by simp [hΦ0], hmaps', hc,
    ld_mfderiv_straightens X p Φ hmaps' hc hstr,
    fun h u u' => gc (e p + h) (u.1 • chartRep X p (e p + h) + u.2)
      (u'.1 • chartRep X p (e p + h) + u'.2),
    fun q hq u u' => hpull q hq u u'⟩⟩

/-- **② with the section hypothesis.** As `ld_manifold_killingChart`, with `X` `C¹` at `p` as a section of the
tangent bundle. -/
theorem ld_manifold_killingChart_section (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N)
    (gc : E → E →L[ℝ] E →L[ℝ] ℝ)
    (hX : ContMDiffAt 𝓘(ℝ, E) 𝓘(ℝ, E).tangent 1
      (fun x ↦ (⟨x, X x⟩ : TangentBundle 𝓘(ℝ, E) N)) p) (hXp : X p ≠ 0)
    (hgc : DifferentiableOn ℝ gc (extChartAt 𝓘(ℝ, E) p).target)
    (hK : ∀ y ∈ (extChartAt 𝓘(ℝ, E) p).target,
      IsKilling (I := 𝓘(ℝ, E)) (M := E) gc (chartRep (E := E) X p) y) :
    Nonempty (LocalKillingChart X p gc) :=
  ld_manifold_killingChart X p gc (ld_chartRep_contDiffAt_of_section X p hX) hXp hgc hK

end ManifoldKilling

/-! ## NEW (campaign 68): the Lie derivative of `(0,2)`-tensor fields on `N`

Route: the registered bracket route. `lieDeriv X h x v w` is campaign 62's test-field expression
`lieDerivForm h X V W x = X(h(V,W)) − h([X,V],W) − h(V,[X,W])` (Mathlib's `mlieBracket`), evaluated on the
canonical extensions `V = constExt x v`, `W = constExt x w` (the fields that are constant in the chart at `x`,
`constExt x v = mpullback (extChartAt x) (const (Dφ_x v))`). The work is the chart formula: in any chart at
`p` whose source contains `x`, `lieDerivForm h X V W x` is the model-space expression
`chartLie (hRep h p) (chartRep X p) = Dh̃(X̃)(·,·) + h̃(DX̃ ·, ·) + h̃(·, DX̃ ·)` at `φ_p x`, applied to `Dφ_p V x`,
`Dφ_p W x`. It depends on `V`, `W` only through `V x`, `W x` (tensoriality) and gives the same value in every
chart (chart independence). -/

section LieDerivNew

open Manifold VectorField Bundle
open scoped ContDiff

/-- **The model-space chart formula** `Dh(X)(v,w) + h(DX v, w) + h(v, DX w)` at `z`. -/
noncomputable def chartLie (F : E → E →L[ℝ] E →L[ℝ] ℝ) (X' : E → E) (z v w : E) : ℝ :=
  fderiv ℝ F z (X' z) v w + F z (fderiv ℝ X' z v) w + F z v (fderiv ℝ X' z w)

/-- **The core identity** on `E`: `X(F(V,W)) − F([X,V],W) − F(V,[X,W]) = chartLie F X (V z) (W z)`. -/
theorem ld_chartLie_core (F : E → E →L[ℝ] E →L[ℝ] ℝ) (X' V' W' : E → E) (z : E)
    (hF : DifferentiableAt ℝ F z) (hV : DifferentiableAt ℝ V' z)
    (hW : DifferentiableAt ℝ W' z) :
    fderiv ℝ (fun y => F y (V' y) (W' y)) z (X' z)
      - F z (lieBracket ℝ X' V' z) (W' z) - F z (V' z) (lieBracket ℝ X' W' z)
      = chartLie F X' z (V' z) (W' z) := by
  have hd := (hF.hasFDerivAt.clm_apply hV.hasFDerivAt).clm_apply hW.hasFDerivAt
  rw [hd.fderiv]
  simp only [lieBracket_eq, chartLie, map_sub, sub_apply, add_apply,
    ContinuousLinearMap.comp_apply, ContinuousLinearMap.flip_apply]
  ring

section ManifoldNew

variable {N : Type*} [TopologicalSpace N] [ChartedSpace E N] [IsManifold 𝓘(ℝ, E) 1 N]

-- `hRep`, `ld_hRep_apply`, `ld_mfderiv_symm_chart`, `ld_mfderiv_chart_symm`, `ld_chartRep_apply_chart`,
-- `ld_h_eq_hRep`: textually identical copies kept above (campaign-100 `section Manifold`).

/-- the general chart computation, given the bracket in the chart. -/
theorem ld_lieDerivForm_chart_of_bracket
    (h : Π x : N, TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x →L[ℝ] ℝ)
    (X V W : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N) {x : N} (hx : x ∈ (chartAt E p).source)
    (hh : DifferentiableAt ℝ (hRep h p) (extChartAt 𝓘(ℝ, E) p x))
    (hV : DifferentiableAt ℝ (chartRep V p) (extChartAt 𝓘(ℝ, E) p x))
    (hW : DifferentiableAt ℝ (chartRep W p) (extChartAt 𝓘(ℝ, E) p x))
    (hbV : mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) x (mlieBracket 𝓘(ℝ, E) X V x) =
      lieBracket ℝ (chartRep X p) (chartRep V p) (extChartAt 𝓘(ℝ, E) p x))
    (hbW : mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) x (mlieBracket 𝓘(ℝ, E) X W x) =
      lieBracket ℝ (chartRep X p) (chartRep W p) (extChartAt 𝓘(ℝ, E) p x)) :
    lieDerivForm h X V W x = chartLie (hRep h p) (chartRep X p) (extChartAt 𝓘(ℝ, E) p x)
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) x (V x))
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) x (W x)) := by
  set e := extChartAt 𝓘(ℝ, E) p with he
  set G : E → ℝ := fun z => hRep h p z (chartRep V p z) (chartRep W p z) with hG
  have hGd : DifferentiableAt ℝ G (e x) := (hh.clm_apply hV).clm_apply hW
  have heq : (fun y => h y (V y) (W y)) =ᶠ[𝓝 x] G ∘ e := by
    filter_upwards [(chartAt E p).open_source.mem_nhds hx] with y hy
    simp only [Function.comp_apply, hG]
    rw [ld_chartRep_apply_chart V p hy, ld_chartRep_apply_chart W p hy]
    exact ld_h_eq_hRep h p hy _ _
  have hm : (show ℝ from mfderiv 𝓘(ℝ, E) 𝓘(ℝ, ℝ) (fun y => h y (V y) (W y)) x (X x)) =
      fderiv ℝ G (e x) (chartRep X p (e x)) := by
    show mfderiv 𝓘(ℝ, E) 𝓘(ℝ, ℝ) (fun y => h y (V y) (W y)) x (X x) = _
    rw [heq.mfderiv_eq, mfderiv_comp x hGd.mdifferentiableAt (mdifferentiableAt_extChartAt hx),
      mfderiv_eq_fderiv, ld_chartRep_apply_chart X p hx]
    rfl
  have hl : lieDerivForm h X V W x = fderiv ℝ G (e x) (chartRep X p (e x)) -
      h x (mlieBracket 𝓘(ℝ, E) X V x) (W x) - h x (V x) (mlieBracket 𝓘(ℝ, E) X W x) :=
    congrArg (fun a : ℝ => a - h x (mlieBracket 𝓘(ℝ, E) X V x) (W x) -
      h x (V x) (mlieBracket 𝓘(ℝ, E) X W x)) hm
  have t1 : h x (mlieBracket 𝓘(ℝ, E) X V x) (W x) =
      hRep h p (e x) (lieBracket ℝ (chartRep X p) (chartRep V p) (e x)) (chartRep W p (e x)) :=
    (ld_h_eq_hRep h p hx _ _).trans (congrArg₂ (fun a b => hRep h p (e x) a b) hbV
      (ld_chartRep_apply_chart W p hx).symm)
  have t2 : h x (V x) (mlieBracket 𝓘(ℝ, E) X W x) =
      hRep h p (e x) (chartRep V p (e x)) (lieBracket ℝ (chartRep X p) (chartRep W p) (e x)) :=
    (ld_h_eq_hRep h p hx _ _).trans (congrArg₂ (fun a b => hRep h p (e x) a b)
      (ld_chartRep_apply_chart V p hx).symm hbW)
  have t3 : chartLie (hRep h p) (chartRep X p) (e x) (chartRep V p (e x)) (chartRep W p (e x)) =
      chartLie (hRep h p) (chartRep X p) (e x)
        (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) x (V x))
        (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) x (W x)) :=
    congrArg₂ (fun a b => chartLie (hRep h p) (chartRep X p) (e x) a b)
      (ld_chartRep_apply_chart V p hx) (ld_chartRep_apply_chart W p hx)
  have core := ld_chartLie_core (hRep h p) (chartRep X p) (chartRep V p) (chartRep W p) (e x)
    hh hV hW
  rw [hl]
  exact (congrArg₂ (fun a b => fderiv ℝ G (e x) (chartRep X p (e x)) - a - b) t1 t2).trans
    (core.trans t3)

/-- bracket in the chart at the point itself (C¹ manifold). -/
theorem ld_mlieBracket_chart_self (X V : Π x : N, TangentSpace 𝓘(ℝ, E) x) (x : N) :
    mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) x) x (mlieBracket 𝓘(ℝ, E) X V x) =
      lieBracket ℝ (chartRep X x) (chartRep V x) (extChartAt 𝓘(ℝ, E) x x) := by
  have hinv := isInvertible_mfderiv_extChartAt (I := 𝓘(ℝ, E)) (mem_extChartAt_source (I := 𝓘(ℝ, E)) x)
  rw [← mlieBracketWithin_univ, mlieBracketWithin_apply]
  refine (hinv.self_apply_inverse _).trans ?_
  simp only [preimage_univ, univ_inter, ModelWithCorners.range_eq_univ,
    mpullbackWithin_univ]
  have hp : ∀ Y : Π x : N, TangentSpace 𝓘(ℝ, E) x,
      mpullback 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) x).symm Y =ᶠ[𝓝 (extChartAt 𝓘(ℝ, E) x x)]
        chartRep Y x := by
    intro Y
    filter_upwards [(isOpen_extChartAt_target x).mem_nhds (mem_extChartAt_target x)] with z hz
    have hi := isInvertible_mfderivWithin_extChartAt_symm (I := 𝓘(ℝ, E)) hz
    rw [ModelWithCorners.range_eq_univ, mfderivWithin_univ] at hi
    rw [mpullback_apply]
    exact hi.inverse_apply_eq.2 (ld_chartRep_inv Y x hz).symm
  have hu : ∀ A B : E → E, lieBracketWithin ℝ A B univ (extChartAt 𝓘(ℝ, E) x x) =
      lieBracket ℝ A B (extChartAt 𝓘(ℝ, E) x x) := fun A B => by rw [lieBracketWithin_univ]
  exact (hu _ _).trans ((hp X).lieBracket_vectorField_eq (hp V))

/-! ### new C¹ -/

/-- The extension of `v ∈ T_x N` that is constant in the chart at `x`: `mpullback (extChartAt x)` of the
constant field `Dφ_x v`. -/
noncomputable def constExt (x : N) (v : E) : Π y : N, TangentSpace 𝓘(ℝ, E) y :=
  mpullback 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) x)
    (fun _ : E => (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) x) x v : E))

theorem ld_constExt_self (x : N) (v : E) : constExt x v x = v :=
  (isInvertible_mfderiv_extChartAt (I := 𝓘(ℝ, E))
    (mem_extChartAt_source (I := 𝓘(ℝ, E)) x)).inverse_apply_self v

theorem ld_chartRep_constExt (x : N) (v : E) {z : E} (hz : z ∈ (extChartAt 𝓘(ℝ, E) x).target) :
    chartRep (constExt x v) x z = mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) x) x v :=
  (isInvertible_mfderiv_extChartAt (I := 𝓘(ℝ, E))
    ((extChartAt 𝓘(ℝ, E) x).map_target hz)).self_apply_inverse _

theorem ld_chartRep_constExt_contDiffAt (x : N) (v : E) :
    ContDiffAt ℝ 1 (chartRep (constExt x v) x) (extChartAt 𝓘(ℝ, E) x x) := by
  have hc : ContDiffAt ℝ 1 (fun _ : E =>
      (show E from mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) x) x v))
      (extChartAt 𝓘(ℝ, E) x x) := contDiffAt_const
  refine hc.congr_of_eventuallyEq ?_
  filter_upwards [(isOpen_extChartAt_target x).mem_nhds (mem_extChartAt_target x)] with z hz
  exact ld_chartRep_constExt x v hz

/-- **The Lie derivative** `(L_X h)_x (v, w)` of a `(0,2)`-tensor field, by the test-field (bracket) formula
`X(h(V,W)) − h([X,V],W) − h(V,[X,W])` at `x` on the extensions `constExt x v`, `constExt x w`. -/
noncomputable def lieDeriv (X : Π x : N, TangentSpace 𝓘(ℝ, E) x)
    (h : Π x : N, TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x →L[ℝ] ℝ)
    (x : N) (v w : E) : ℝ :=
  lieDerivForm h X (constExt x v) (constExt x w) x

/-- The chart computation in the chart at the point itself (`C¹` manifold). -/
theorem ld_lieDerivForm_chart_self
    (h : Π x : N, TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x →L[ℝ] ℝ)
    (X V W : Π x : N, TangentSpace 𝓘(ℝ, E) x) (x : N)
    (hh : DifferentiableAt ℝ (hRep h x) (extChartAt 𝓘(ℝ, E) x x))
    (hV : DifferentiableAt ℝ (chartRep V x) (extChartAt 𝓘(ℝ, E) x x))
    (hW : DifferentiableAt ℝ (chartRep W x) (extChartAt 𝓘(ℝ, E) x x)) :
    lieDerivForm h X V W x = chartLie (hRep h x) (chartRep X x) (extChartAt 𝓘(ℝ, E) x x)
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) x) x (V x))
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) x) x (W x)) :=
  ld_lieDerivForm_chart_of_bracket h X V W x (mem_chart_source E x) hh hV hW
    (ld_mlieBracket_chart_self X V x) (ld_mlieBracket_chart_self X W x)

/-- **Chart formula at `x`** (`C¹` manifold): `lieDeriv` is `chartLie` of the representatives in the chart
at `x`. No hypothesis on `X` is needed (both sides use `fderiv` of `chartRep X x`). -/
theorem ld_lieDeriv_chart_self (X : Π x : N, TangentSpace 𝓘(ℝ, E) x)
    (h : Π x : N, TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x →L[ℝ] ℝ) (x : N) (v w : E)
    (hh : DifferentiableAt ℝ (hRep h x) (extChartAt 𝓘(ℝ, E) x x)) :
    lieDeriv X h x v w = chartLie (hRep h x) (chartRep X x) (extChartAt 𝓘(ℝ, E) x x)
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) x) x v)
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) x) x w) :=
  (ld_lieDerivForm_chart_self h X (constExt x v) (constExt x w) x hh
    ((ld_chartRep_constExt_contDiffAt x v).differentiableAt one_ne_zero)
    ((ld_chartRep_constExt_contDiffAt x w).differentiableAt one_ne_zero)).trans
    (congrArg₂ (fun a b : E => chartLie (hRep h x) (chartRep X x) (extChartAt 𝓘(ℝ, E) x x)
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) x) x a)
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) x) x b))
      (ld_constExt_self x v) (ld_constExt_self x w))

/-- **Tensoriality** (`C¹` manifold): for any test sections `V`, `W` that are `C¹` at `x`, the test-field
expression equals `lieDeriv X h x (V x) (W x)`. -/
theorem ld_lieDerivForm_eq_lieDeriv
    (h : Π x : N, TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x →L[ℝ] ℝ)
    (X V W : Π x : N, TangentSpace 𝓘(ℝ, E) x) (x : N)
    (hh : DifferentiableAt ℝ (hRep h x) (extChartAt 𝓘(ℝ, E) x x))
    (hV : ContMDiffAt 𝓘(ℝ, E) 𝓘(ℝ, E).tangent 1
      (fun y ↦ (⟨y, V y⟩ : TangentBundle 𝓘(ℝ, E) N)) x)
    (hW : ContMDiffAt 𝓘(ℝ, E) 𝓘(ℝ, E).tangent 1
      (fun y ↦ (⟨y, W y⟩ : TangentBundle 𝓘(ℝ, E) N)) x) :
    lieDerivForm h X V W x = lieDeriv X h x (V x) (W x) :=
  (ld_lieDerivForm_chart_self h X V W x hh
    ((ld_chartRep_contDiffAt_of_section V x hV).differentiableAt one_ne_zero)
    ((ld_chartRep_contDiffAt_of_section W x hW).differentiableAt one_ne_zero)).trans
    (ld_lieDeriv_chart_self X h x (V x) (W x) hh).symm


end ManifoldNew

/-! ### model space -/

/-- `mlieBracket` on the model space is `lieBracket`. -/
theorem ld_mlieBracket_model (A B : Π y : E, TangentSpace 𝓘(ℝ, E) y) (z : E) :
    mlieBracket 𝓘(ℝ, E) A B z = lieBracket ℝ (A : E → E) (B : E → E) z := by
  rw [← mlieBracketWithin_univ, mlieBracketWithin_eq_lieBracketWithin]
  set A' : E → E := A
  set B' : E → E := B
  show lieBracketWithin ℝ A' B' univ z = lieBracket ℝ A' B' z
  rw [lieBracketWithin_univ]

/-- On the model space, the test-field expression is `chartLie` (tensorial in `V`, `W`). -/
theorem ld_lieDerivForm_model (F : E → E →L[ℝ] E →L[ℝ] ℝ) (X' V W : E → E) (z : E)
    (hF : DifferentiableAt ℝ F z) (hV : DifferentiableAt ℝ V z) (hW : DifferentiableAt ℝ W z) :
    (show ℝ from mfderiv 𝓘(ℝ, E) 𝓘(ℝ, ℝ) (fun y => F y (V y) (W y)) z (X' z))
    - F z (mlieBracket 𝓘(ℝ, E) X' V z) (W z) - F z (V z) (mlieBracket 𝓘(ℝ, E) X' W z)
      = chartLie F X' z (V z) (W z) := by
  have hm : (show ℝ from mfderiv 𝓘(ℝ, E) 𝓘(ℝ, ℝ) (fun y => F y (V y) (W y)) z (X' z)) =
      fderiv ℝ (fun y => F y (V y) (W y)) z (X' z) := by
    rw [mfderiv_eq_fderiv]
    rfl
  have hl := (congrArg (fun a : ℝ => a - F z (mlieBracket 𝓘(ℝ, E) X' V z) (W z) -
      F z (V z) (mlieBracket 𝓘(ℝ, E) X' W z)) hm).trans
    (congrArg₂ (fun a b : E => fderiv ℝ (fun y => F y (V y) (W y)) z (X' z) - F z a (W z) -
      F z (V z) b) (ld_mlieBracket_model X' V z) (ld_mlieBracket_model X' W z))
  exact hl.trans (ld_chartLie_core F X' V W z hF hV hW)

/-- The chart Killing equation gives the model-space `IsKilling`. -/
theorem ld_isKilling_of_chartLie (F : E → E →L[ℝ] E →L[ℝ] ℝ) (X' : E → E) (z : E)
    (hF : DifferentiableAt ℝ F z) (h0 : ∀ v w, chartLie F X' z v w = 0) :
    IsKilling (I := 𝓘(ℝ, E)) (M := E) F X' z := by
  unfold IsKilling IsConformalKilling
  intro Y Z hY hZ
  rw [contMDiffAt_vectorSpace_iff_contDiffAt] at hY hZ
  refine (ld_lieDerivForm_model F X' Y Z z hF (hY.differentiableAt one_ne_zero)
    (hZ.differentiableAt one_ne_zero)).trans ?_
  exact (h0 _ _).trans (by simp)


/-! ### C² -/
section C2
variable {N : Type*} [TopologicalSpace N] [ChartedSpace E N] [IsManifold 𝓘(ℝ, E) 1 N]
  [IsManifold 𝓘(ℝ, E) 2 N]

/-- The Lie bracket at `x` read in the chart at any `p` whose source contains `x` (`C²` manifold, via Mathlib's
invariance of `mlieBracket`, `mpullback_mlieBracket`). -/
theorem ld_mlieBracket_chart (X V : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N) {x : N}
    (hx : x ∈ (chartAt E p).source)
    (hX : ContDiffAt ℝ 1 (chartRep X p) (extChartAt 𝓘(ℝ, E) p x))
    (hV : ContDiffAt ℝ 1 (chartRep V p) (extChartAt 𝓘(ℝ, E) p x)) :
    mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) x (mlieBracket 𝓘(ℝ, E) X V x) =
      lieBracket ℝ (chartRep X p) (chartRep V p) (extChartAt 𝓘(ℝ, E) p x) := by
  have : IsManifold 𝓘(ℝ, E) (minSmoothness ℝ 2) N := by
    rw [minSmoothness_of_isRCLikeNormedField]; infer_instance
  have hxs : x ∈ (extChartAt 𝓘(ℝ, E) p).source := by rwa [extChartAt_source]
  have hinv := isInvertible_mfderiv_extChartAt (I := 𝓘(ℝ, E)) hxs
  have hX' := ((contMDiffAt_vectorSpace_iff_contDiffAt
    (V := (chartRep X p : Π y : E, TangentSpace 𝓘(ℝ, E) y))).2 hX).mdifferentiableAt one_ne_zero
  have hV' := ((contMDiffAt_vectorSpace_iff_contDiffAt
    (V := (chartRep V p : Π y : E, TangentSpace 𝓘(ℝ, E) y))).2 hV).mdifferentiableAt one_ne_zero
  have hf : ContMDiffAt 𝓘(ℝ, E) 𝓘(ℝ, E) 2 (extChartAt 𝓘(ℝ, E) p) x := contMDiffAt_extChartAt' hx
  have key := mpullback_mlieBracket (I := 𝓘(ℝ, E)) (I' := 𝓘(ℝ, E)) hX' hV' hf (by simp)
  have hp : ∀ Y : Π x : N, TangentSpace 𝓘(ℝ, E) x,
      mpullback 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p)
        (chartRep Y p : Π y : E, TangentSpace 𝓘(ℝ, E) y) =ᶠ[𝓝 x] Y := by
    intro Y
    filter_upwards [(chartAt E p).open_source.mem_nhds hx] with y hy
    have hys : y ∈ (extChartAt 𝓘(ℝ, E) p).source := by rwa [extChartAt_source]
    exact (isInvertible_mfderiv_extChartAt (I := 𝓘(ℝ, E)) hys).inverse_apply_eq.2
      (ld_chartRep_apply_chart Y p hy)
  rw [(hp X).mlieBracket_vectorField_eq (hp V)] at key
  rw [← key]
  exact (hinv.self_apply_inverse _).trans (ld_mlieBracket_model _ _ _)

/-- A section `C¹` at `x` has its representative in the chart at `p` `C¹` at `φ_p x` (`C²` manifold). -/
theorem ld_chartRep_contDiffAt_of_section_chart (V : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N)
    {x : N} (hx : x ∈ (chartAt E p).source)
    (hV : ContMDiffAt 𝓘(ℝ, E) 𝓘(ℝ, E).tangent 1
      (fun y ↦ (⟨y, V y⟩ : TangentBundle 𝓘(ℝ, E) N)) x) :
    ContDiffAt ℝ 1 (chartRep V p) (extChartAt 𝓘(ℝ, E) p x) := by
  set e := extChartAt 𝓘(ℝ, E) p with he
  have hxs : x ∈ e.source := by rwa [extChartAt_source]
  have hy : e x ∈ e.target := e.map_source hxs
  have hto : IsOpen e.target := isOpen_extChartAt_target p
  have h1 : ContMDiffAt 𝓘(ℝ, E) 𝓘(ℝ, E) 2 e.symm (e x) :=
    (contMDiffOn_extChartAt_symm p).contMDiffAt (hto.mem_nhds hy)
  have h1' : (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) e.symm (e x)).IsInvertible := by
    have := isInvertible_mfderivWithin_extChartAt_symm (I := 𝓘(ℝ, E)) hy
    rwa [ModelWithCorners.range_eq_univ, mfderivWithin_univ] at this
  have hV' : ContMDiffAt 𝓘(ℝ, E) 𝓘(ℝ, E).tangent 1
      (fun y ↦ (⟨y, V y⟩ : TangentBundle 𝓘(ℝ, E) N)) (e.symm (e x)) := by
    rw [e.left_inv hxs]; exact hV
  have h2 := ContMDiffAt.mpullback_vectorField_preimage hV' h1 h1' (by norm_num)
  rw [contMDiffAt_vectorSpace_iff_contDiffAt] at h2
  refine h2.congr_of_eventuallyEq ?_
  filter_upwards [hto.mem_nhds hy] with z hz
  have hi := isInvertible_mfderivWithin_extChartAt_symm (I := 𝓘(ℝ, E)) hz
  rw [ModelWithCorners.range_eq_univ, mfderivWithin_univ] at hi
  exact (hi.inverse_apply_eq.2 (ld_chartRep_inv V p hz).symm).symm

/-- `constExt x v` is a `C¹` section at `x` (`C²` manifold). -/
theorem ld_constExt_section (x : N) (v : E) :
    ContMDiffAt 𝓘(ℝ, E) 𝓘(ℝ, E).tangent 1
      (fun y ↦ (⟨y, constExt x v y⟩ : TangentBundle 𝓘(ℝ, E) N)) x :=
  ContMDiffAt.mpullback_vectorField_preimage
    ((contMDiffAt_vectorSpace_iff_contDiffAt (V := fun _ : E =>
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) x) x v : E))).2 contDiffAt_const)
    (contMDiffAt_extChartAt' (n := 2) (mem_chart_source E x))
    (isInvertible_mfderiv_extChartAt (mem_extChartAt_source x)) (by norm_num)

/-- **The chart formula in the chart at `p`** (`C²` manifold), for any `C¹` test sections. -/
theorem ld_lieDerivForm_chart
    (h : Π x : N, TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x →L[ℝ] ℝ)
    (X V W : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N) {x : N} (hx : x ∈ (chartAt E p).source)
    (hX : ContDiffAt ℝ 1 (chartRep X p) (extChartAt 𝓘(ℝ, E) p x))
    (hh : DifferentiableAt ℝ (hRep h p) (extChartAt 𝓘(ℝ, E) p x))
    (hV : ContMDiffAt 𝓘(ℝ, E) 𝓘(ℝ, E).tangent 1
      (fun y ↦ (⟨y, V y⟩ : TangentBundle 𝓘(ℝ, E) N)) x)
    (hW : ContMDiffAt 𝓘(ℝ, E) 𝓘(ℝ, E).tangent 1
      (fun y ↦ (⟨y, W y⟩ : TangentBundle 𝓘(ℝ, E) N)) x) :
    lieDerivForm h X V W x = chartLie (hRep h p) (chartRep X p) (extChartAt 𝓘(ℝ, E) p x)
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) x (V x))
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) x (W x)) := by
  have hV' := ld_chartRep_contDiffAt_of_section_chart V p hx hV
  have hW' := ld_chartRep_contDiffAt_of_section_chart W p hx hW
  exact ld_lieDerivForm_chart_of_bracket h X V W p hx hh (hV'.differentiableAt one_ne_zero)
    (hW'.differentiableAt one_ne_zero) (ld_mlieBracket_chart X V p hx hX hV')
    (ld_mlieBracket_chart X W p hx hX hW')

/-- **Chart independence** (`C²` manifold): computed in the chart at any `p` whose source contains `x`,
`lieDeriv X h x v w = chartLie (hRep h p) (chartRep X p) (φ_p x) (Dφ_p v) (Dφ_p w)`. -/
theorem ld_lieDeriv_chart (X : Π x : N, TangentSpace 𝓘(ℝ, E) x)
    (h : Π x : N, TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x →L[ℝ] ℝ)
    (p : N) {x : N} (hx : x ∈ (chartAt E p).source)
    (hX : ContDiffAt ℝ 1 (chartRep X p) (extChartAt 𝓘(ℝ, E) p x))
    (hh : DifferentiableAt ℝ (hRep h p) (extChartAt 𝓘(ℝ, E) p x)) (v w : E) :
    lieDeriv X h x v w = chartLie (hRep h p) (chartRep X p) (extChartAt 𝓘(ℝ, E) p x)
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) x v)
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) x w) :=
  (ld_lieDerivForm_chart h X (constExt x v) (constExt x w) p hx hX hh (ld_constExt_section x v)
    (ld_constExt_section x w)).trans
    (congrArg₂ (fun a b : E => chartLie (hRep h p) (chartRep X p) (extChartAt 𝓘(ℝ, E) p x)
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) x a)
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) x b))
      (ld_constExt_self x v) (ld_constExt_self x w))

/-- `L_X h = 0` at `x` gives the chart Killing equation at `φ_p x` for all chart vectors. -/
theorem ld_chartLie_zero_of_lieDeriv (X : Π x : N, TangentSpace 𝓘(ℝ, E) x)
    (h : Π x : N, TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x →L[ℝ] ℝ)
    (p : N) {x : N} (hx : x ∈ (chartAt E p).source)
    (hX : ContDiffAt ℝ 1 (chartRep X p) (extChartAt 𝓘(ℝ, E) p x))
    (hh : DifferentiableAt ℝ (hRep h p) (extChartAt 𝓘(ℝ, E) p x))
    (h0 : ∀ v w, lieDeriv X h x v w = 0) (v' w' : E) :
    chartLie (hRep h p) (chartRep X p) (extChartAt 𝓘(ℝ, E) p x) v' w' = 0 := by
  have t := (ld_lieDeriv_chart X h p hx hX hh
    (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p).symm (extChartAt 𝓘(ℝ, E) p x) v')
    (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p).symm (extChartAt 𝓘(ℝ, E) p x) w')).symm.trans
    (h0 _ _)
  exact (congrArg₂ (fun a b : E => chartLie (hRep h p) (chartRep X p) (extChartAt 𝓘(ℝ, E) p x) a b)
    (ld_mfderiv_chart_symm p hx v').symm (ld_mfderiv_chart_symm p hx w').symm).trans t

/-- `L_X h = 0` at `x` gives campaign 62's model-space `IsKilling (hRep h p) (chartRep X p)` at `φ_p x`. -/
theorem ld_isKilling_of_lieDeriv (X : Π x : N, TangentSpace 𝓘(ℝ, E) x)
    (h : Π x : N, TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x →L[ℝ] ℝ)
    (p : N) {x : N} (hx : x ∈ (chartAt E p).source)
    (hX : ContDiffAt ℝ 1 (chartRep X p) (extChartAt 𝓘(ℝ, E) p x))
    (hh : DifferentiableAt ℝ (hRep h p) (extChartAt 𝓘(ℝ, E) p x))
    (h0 : ∀ v w, lieDeriv X h x v w = 0) :
    IsKilling (I := 𝓘(ℝ, E)) (M := E) (hRep h p) (chartRep X p) (extChartAt 𝓘(ℝ, E) p x) :=
  ld_isKilling_of_chartLie _ _ _ hh (ld_chartLie_zero_of_lieDeriv X h p hx hX hh h0)

end C2

/-! ## NEW (campaign 68) ②: `lem:killing` (b) with the coordinate-free Killing condition `L_X g = 0` -/

section KillingC2

variable {N : Type*} [TopologicalSpace N] [ChartedSpace E N] [IsManifold 𝓘(ℝ, E) 1 N]
  [IsManifold 𝓘(ℝ, E) 2 N]

/-- **② `lem:killing` (b), coordinate-free.** `N` a `C²` manifold, `X` a vector field `C¹` at `p` as a section of
the tangent bundle with `X p ≠ 0`, `g` a `(0,2)`-tensor field whose chart representative at `p` is
differentiable near `φ p`, and `L_X g = 0` (the Lie derivative `lieDeriv` of this file) on a neighbourhood of `p`.
Then there is a local Killing chart around `p` for the chart metric `hRep g p`. -/
theorem ld_manifold_killingChart_lieDeriv (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N)
    (g : Π x : N, TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x →L[ℝ] ℝ)
    (hX : ContMDiffAt 𝓘(ℝ, E) 𝓘(ℝ, E).tangent 1
      (fun x ↦ (⟨x, X x⟩ : TangentBundle 𝓘(ℝ, E) N)) p) (hXp : X p ≠ 0)
    (hg : ∀ᶠ y in 𝓝 (extChartAt 𝓘(ℝ, E) p p), DifferentiableAt ℝ (hRep g p) y)
    (hK : ∀ᶠ x in 𝓝 p, ∀ v w, lieDeriv X g x v w = 0) :
    Nonempty (LocalKillingChart X p (hRep g p)) := by
  set e := extChartAt 𝓘(ℝ, E) p with he
  obtain ⟨ρ, hρ, hball, hf⟩ := ld_chartRep_ball_of_section X p hX
  have hK' : ∀ᶠ y in 𝓝 (e p), ∀ v w, lieDeriv X g (e.symm y) v w = 0 := by
    have hc := continuousAt_extChartAt_symm (I := 𝓘(ℝ, E)) p
    rw [ContinuousAt, extChartAt_to_inv] at hc
    exact hc hK
  obtain ⟨ρ', hρ', hb⟩ := Metric.eventually_nhds_iff_ball.1 (hK'.and hg)
  set r := min ρ ρ' with hr_def
  have hr : 0 < r := lt_min hρ hρ'
  have hrρ : ball (e p) r ⊆ ball (e p) ρ := ball_subset_ball (min_le_left _ _)
  have hrρ' : ball (e p) r ⊆ ball (e p) ρ' := ball_subset_ball (min_le_right _ _)
  have hballr : ball (e p) r ⊆ e.target := hrρ.trans hball
  have hfr : ContDiffOn ℝ 1 (chartRep X p) (ball (e p) r) := hf.mono hrρ
  have hgd : DifferentiableOn ℝ (hRep g p) (ball (e p) r) := fun y hy =>
    (hb y (hrρ' hy)).2.differentiableWithinAt
  have hKb : ∀ y ∈ ball (e p) r, ∀ v w, fderiv ℝ (hRep g p) y (chartRep X p y) v w +
      hRep g p y (fderiv ℝ (chartRep X p) y v) w + hRep g p y v (fderiv ℝ (chartRep X p) y w) = 0 := by
    intro y hy v w
    have hyt := hballr hy
    have hx : e.symm y ∈ (chartAt E p).source := by
      rw [← extChartAt_source 𝓘(ℝ, E)]; exact e.map_target hyt
    have hey : e (e.symm y) = y := e.right_inv hyt
    have hXc : ContDiffAt ℝ 1 (chartRep X p) (e (e.symm y)) := by
      rw [hey]; exact hfr.contDiffAt (isOpen_ball.mem_nhds hy)
    have hhd : DifferentiableAt ℝ (hRep g p) (e (e.symm y)) := by
      rw [hey]; exact (hb y (hrρ' hy)).2
    have hc := ld_chartLie_zero_of_lieDeriv X g p hx hXc hhd (hb y (hrρ' hy)).1 v w
    rw [hey] at hc
    exact hc
  obtain ⟨H, Φ, h0, hΦ0, hmaps, hc, hstr, -, hpull⟩ :=
    ld_flowBox_killing_of_contDiffOn hr hfr (ld_chartRep_ne_zero X p hXp) (hRep g p) hgd hKb
  have hmaps' : MapsTo Φ Φ.source e.target := fun q hq =>
    hballr (ball_subset_ball (by linarith) (hmaps hq))
  exact ⟨⟨H, Φ, h0, hΦ0, by simp only [Function.comp_apply, hΦ0]; exact extChartAt_to_inv p,
    hmaps', hc, ld_mfderiv_straightens X p Φ hmaps' hc hstr,
    fun h u u' => hRep g p (e p + h) (u.1 • chartRep X p (e p + h) + u.2)
      (u'.1 • chartRep X p (e p + h) + u'.2),
    fun q hq u u' => hpull q hq u u'⟩⟩

end KillingC2

section KillingC1

variable {N : Type*} [TopologicalSpace N] [ChartedSpace E N] [IsManifold 𝓘(ℝ, E) 1 N]

/-- **The local Killing chart, read on `N`.** For the chart metric `hRep g p`, the components `gH` of a local
Killing chart are the components of `g` itself in the chart `ψ = (extChartAt p).symm ∘ Φ`:
`g_{ψ q} (Dψ_q u) (Dψ_q u') = gH q.2 u u'`. So `∂_λ g_ab = 0` is a statement about `g` on `N`. -/
theorem LocalKillingChart.ld_metric_N {X : Π x : N, TangentSpace 𝓘(ℝ, E) x} {p : N}
    {g : Π x : N, TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x →L[ℝ] ℝ}
    (K : LocalKillingChart X p (hRep g p)) (q : ℝ × K.H) (hq : q ∈ K.Φ.source) (u u' : ℝ × K.H) :
    g (((extChartAt 𝓘(ℝ, E) p).symm ∘ K.Φ) q)
      (mfderiv 𝓘(ℝ, ℝ × K.H) 𝓘(ℝ, E) ((extChartAt 𝓘(ℝ, E) p).symm ∘ K.Φ) q u)
      (mfderiv 𝓘(ℝ, ℝ × K.H) 𝓘(ℝ, E) ((extChartAt 𝓘(ℝ, E) p).symm ∘ K.Φ) q u') =
      K.gH q.2 u u' := by
  have hΦd : DifferentiableAt ℝ K.Φ q :=
    (K.contDiffOn.contDiffAt (K.Φ.open_source.mem_nhds hq)).differentiableAt one_ne_zero
  have hy := K.mapsTo hq
  have key : mfderiv 𝓘(ℝ, ℝ × K.H) 𝓘(ℝ, E) ((extChartAt 𝓘(ℝ, E) p).symm ∘ K.Φ) q =
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p).symm (K.Φ q)).comp (fderiv ℝ K.Φ q) := by
    rw [mfderiv_comp q (ld_mdifferentiableAt_symm p hy)
      (mdifferentiableAt_iff_differentiableAt.2 hΦd)]
    exact congrArg _ hΦd.hasFDerivAt.hasMFDerivAt.mfderiv
  rw [key]
  exact K.metric_eq q hq u u'

end KillingC1

end LieDerivNew

/-! ## NEW (campaign 94 ②, `r7669+71`): `lem:killing` stage 1, on one flow box

`ψ = (extChartAt p).symm ∘ Φ` is the adapted chart of a `LocalKillingChart` read on `N`. The orbit of `X`
through `p` inside the flow box is `t ↦ ψ (t, 0)`, its velocity is `Dψ (1, 0) = X` (`straightens`), and the
components of `g` in the adapted chart are `kl_comps g K q u u' = g_{ψ q} (Dψ_q u) (Dψ_q u')`, which equal
`K.gH q.2 u u'` (`ld_metric_N`) and so depend on the transverse coordinate `q.2` only. -/

section KillingLocalNew

open Manifold

variable {N : Type*} [TopologicalSpace N] [ChartedSpace E N] [IsManifold 𝓘(ℝ, E) 1 N]
variable {X : Π x : N, TangentSpace 𝓘(ℝ, E) x} {p : N} {gc : E → E →L[ℝ] E →L[ℝ] ℝ}

/-- The adapted chart `ψ = φ⁻¹ ∘ Φ : ℝ × H → N` of a local Killing chart. -/
noncomputable def kl_psi (K : LocalKillingChart X p gc) : ℝ × K.H → N :=
  (extChartAt 𝓘(ℝ, E) p).symm ∘ K.Φ

/-- Its differential `Dψ_q : ℝ × H → T_{ψ q} N`. -/
noncomputable def kl_dpsi (K : LocalKillingChart X p gc) (q : ℝ × K.H) :
    ℝ × K.H →L[ℝ] TangentSpace 𝓘(ℝ, E) (kl_psi K q) :=
  mfderiv 𝓘(ℝ, ℝ × K.H) 𝓘(ℝ, E) (kl_psi K) q

/-- The components of a `(0,2)`-tensor field `g` on `N` in the adapted chart at `q`:
`(u, u') ↦ g_{ψ q} (Dψ_q u) (Dψ_q u')`. -/
noncomputable def kl_comps (g : Π x : N, TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x →L[ℝ] ℝ)
    (K : LocalKillingChart X p gc) (q : ℝ × K.H) : (ℝ × K.H) → (ℝ × K.H) → ℝ :=
  fun u u' => g (kl_psi K q) (kl_dpsi K q u) (kl_dpsi K q u')

/-- `|X|²` at a point of `N`. -/
def kl_normSq (g : Π x : N, TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x →L[ℝ] ℝ)
    (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (x : N) : ℝ :=
  g x (X x) (X x)

/-- `ψ (0, 0) = p`. -/
theorem kl_psi_zero (K : LocalKillingChart X p gc) : kl_psi K (0, 0) = p := K.ψ_zero

/-- **The velocity of the orbit is `X`:** `Dψ_q (1, 0) = X (ψ q)`. -/
theorem kl_velocity (K : LocalKillingChart X p gc) (q : ℝ × K.H) (hq : q ∈ K.Φ.source) :
    kl_dpsi K q (1, 0) = X (kl_psi K q) := K.straightens q hq

/-- **`ψ` is injective on the flow box.** -/
theorem kl_psi_injOn (K : LocalKillingChart X p gc) : InjOn (kl_psi K) K.Φ.source := by
  intro q hq q' hq' h
  have h1 : K.Φ q = K.Φ q' :=
    (extChartAt 𝓘(ℝ, E) p).symm.injOn (by simpa using K.mapsTo hq) (by simpa using K.mapsTo hq') h
  exact K.Φ.injOn hq hq' h1

/-- **Distinct orbit parameters give distinct events.** -/
theorem kl_orbit_ne (K : LocalKillingChart X p gc) {a b : ℝ}
    (ha : ((a, 0) : ℝ × K.H) ∈ K.Φ.source) (hb : ((b, 0) : ℝ × K.H) ∈ K.Φ.source) (hab : a ≠ b) :
    kl_psi K (a, 0) ≠ kl_psi K (b, 0) := fun h =>
  hab (congrArg Prod.fst (kl_psi_injOn K ha hb h))

/-- **A uniform orbit segment in the flow box:** `(t, 0) ∈ Φ.source` for `|t| < ε`. -/
theorem kl_exists_eps (K : LocalKillingChart X p gc) :
    ∃ ε > 0, ∀ t : ℝ, |t| < ε → ((t, 0) : ℝ × K.H) ∈ K.Φ.source := by
  have hc : Continuous fun t : ℝ => ((t, 0) : ℝ × K.H) := continuous_id.prodMk continuous_const
  have ho : IsOpen ((fun t : ℝ => ((t, 0) : ℝ × K.H)) ⁻¹' K.Φ.source) := K.Φ.open_source.preimage hc
  obtain ⟨ε, hε, hb⟩ := Metric.isOpen_iff.1 ho 0 (by simpa using K.zero_mem)
  refine ⟨ε, hε, fun t ht => hb ?_⟩
  rwa [mem_ball, Real.dist_eq, sub_zero]

/-- Points of `[a, b]` (either order) lie in `(-ε, ε)` when `a` and `b` do. -/
theorem kl_uIcc_abs_lt {a b ε t : ℝ} (ha : |a| < ε) (hb : |b| < ε) (ht : t ∈ uIcc a b) : |t| < ε := by
  rw [abs_lt] at ha hb ⊢
  rcases mem_uIcc.1 ht with ⟨h1, h2⟩ | ⟨h1, h2⟩ <;> constructor <;> linarith

variable {g : Π x : N, TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x →L[ℝ] ℝ}

/-- The adapted components are `gH`: `kl_comps g K q = K.gH q.2` on the flow box (`ld_metric_N`). -/
theorem kl_comps_eq_gH (K : LocalKillingChart X p (hRep g p)) (q : ℝ × K.H) (hq : q ∈ K.Φ.source) :
    kl_comps g K q = K.gH q.2 := by
  funext u u'
  exact K.ld_metric_N q hq u u'

/-- **`∂_λ g_ab = 0` on `N`:** two flow-box points with the same transverse coordinate see the same
components of `g`. In particular the components at `(a, y)` and `(b, y)` agree. -/
theorem kl_lambda_indep_N (K : LocalKillingChart X p (hRep g p)) (q q' : ℝ × K.H)
    (hq : q ∈ K.Φ.source) (hq' : q' ∈ K.Φ.source) (h : q.2 = q'.2) :
    kl_comps g K q = kl_comps g K q' := by
  rw [kl_comps_eq_gH K q hq, kl_comps_eq_gH K q' hq', h]

/-- `|X|²` is a component: `|X|²(ψ q) = (kl_comps g K q) (1,0) (1,0)`. -/
theorem kl_normSq_eq_comps (K : LocalKillingChart X p (hRep g p)) (q : ℝ × K.H) (hq : q ∈ K.Φ.source) :
    kl_normSq g X (kl_psi K q) = kl_comps g K q (1, 0) (1, 0) := by
  unfold kl_normSq kl_comps
  rw [kl_velocity K q hq]

/-- **4b, local `kh_interval_orbit`:** along the orbit, with `dλ = c`, `ds² = c² |X|²`. -/
theorem kl_interval_orbit (K : LocalKillingChart X p (hRep g p)) (q : ℝ × K.H) (hq : q ∈ K.Φ.source)
    (c : ℝ) : kl_comps g K q (c, 0) (c, 0) = c ^ 2 * kl_normSq g X (kl_psi K q) := by
  have hc : ((c, 0) : ℝ × K.H) = c • ((1, 0) : ℝ × K.H) := by ext <;> simp
  unfold kl_comps kl_normSq
  rw [hc, map_smul, kl_velocity K q hq]
  simp only [map_smul, FunLike.coe_smul, Pi.smul_apply, smul_eq_mul]
  ring

/-- **4b, local `kh_forcing`:** null with `dλ = c ≠ 0` forces `|X|² = 0`. -/
theorem kl_forcing (K : LocalKillingChart X p (hRep g p)) (q : ℝ × K.H) (hq : q ∈ K.Φ.source)
    (c : ℝ) (hc : c ≠ 0) (hnull : kl_comps g K q (c, 0) (c, 0) = 0) :
    kl_normSq g X (kl_psi K q) = 0 := by
  rw [kl_interval_orbit K q hq] at hnull
  rcases mul_eq_zero.mp hnull with h | h
  · exact absurd (pow_eq_zero_iff two_ne_zero |>.mp h) hc
  · exact h

/-- **Killing invariance of `|X|²` along the orbit (in the flow box).** -/
theorem kl_normSq_orbit_const (K : LocalKillingChart X p (hRep g p)) (q q' : ℝ × K.H)
    (hq : q ∈ K.Φ.source) (hq' : q' ∈ K.Φ.source) (h : q.2 = q'.2) :
    kl_normSq g X (kl_psi K q) = kl_normSq g X (kl_psi K q') := by
  rw [kl_normSq_eq_comps K q hq, kl_normSq_eq_comps K q' hq', kl_lambda_indep_N K q q' hq hq' h]

/-- **4b, local `kh_null_along_generator`:** `g_p(X p, X p) = 0` gives `|X|² = 0` and `ds² = 0` (every
`dλ = c`) at every flow-box point `(t, 0)` of the orbit through `p`. -/
theorem kl_null_along_orbit (K : LocalKillingChart X p (hRep g p)) (hnull : g p (X p) (X p) = 0)
    (t : ℝ) (ht : ((t, 0) : ℝ × K.H) ∈ K.Φ.source) :
    kl_normSq g X (kl_psi K (t, 0)) = 0 ∧ ∀ c : ℝ, kl_comps g K (t, 0) (c, 0) (c, 0) = 0 := by
  have h0 : kl_normSq g X (kl_psi K (0, 0)) = 0 := by
    rw [kl_psi_zero]; exact hnull
  have ht0 : kl_normSq g X (kl_psi K (t, 0)) = 0 := by
    rw [kl_normSq_orbit_const K (t, 0) (0, 0) ht K.zero_mem rfl]; exact h0
  exact ⟨ht0, fun c => by rw [kl_interval_orbit K _ ht, ht0, mul_zero]⟩

/-- **The local form of `MetricallyCoincident`** for the orbit points `ψ (a, 0)`, `ψ (b, 0)` of a local
Killing chart `K` for the chart metric `hRep g p`. -/
structure kl_MetricallyCoincidentLocal
    (g : Π x : N, TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x →L[ℝ] ℝ)
    (K : LocalKillingChart X p (hRep g p)) (a b : ℝ) : Prop where
  /-- The orbit segment `{(t, 0) : t ∈ [a, b]}` lies in the flow box. -/
  mem : ∀ t ∈ uIcc a b, ((t, 0) : ℝ × K.H) ∈ K.Φ.source
  /-- The segment `t ↦ ψ (t, 0)` is an integral curve of `X`: velocity `Dψ (1, 0) = X`. -/
  velocity : ∀ t ∈ uIcc a b, kl_dpsi K (t, 0) (1, 0) = X (kl_psi K (t, 0))
  /-- (a): `|X|² = g(X, X) = 0` at every point of the segment. -/
  hypA : ∀ t ∈ uIcc a b, kl_normSq g X (kl_psi K (t, 0)) = 0
  /-- (a), as a line element: `ds² = |X|² dλ² = 0` along the segment, for every `dλ = c`. -/
  hypA_interval : ∀ t ∈ uIcc a b, ∀ c : ℝ, kl_comps g K (t, 0) (c, 0) (c, 0) = 0
  /-- (b): every transverse invariant (a function of the transverse coordinate and of the adapted components
  of `g`) takes the same value at `ψ (a, 0)` and at `ψ (b, 0)`. -/
  hypB : ∀ (α : Type) (F : K.H → ((ℝ × K.H) → (ℝ × K.H) → ℝ) → α),
    F ((b, 0) : ℝ × K.H).2 (kl_comps g K (b, 0)) = F ((a, 0) : ℝ × K.H).2 (kl_comps g K (a, 0))
  /-- (b), between: and at every point of the connecting segment. -/
  hypB_between : ∀ (α : Type) (F : K.H → ((ℝ × K.H) → (ℝ × K.H) → ℝ) → α), ∀ t ∈ uIcc a b,
    F ((t, 0) : ℝ × K.H).2 (kl_comps g K (t, 0)) = F ((a, 0) : ℝ × K.H).2 (kl_comps g K (a, 0))
  /-- `Δx = 0` in the adapted frame. -/
  deltaX : ‖((b, 0) : ℝ × K.H).2 - ((a, 0) : ℝ × K.H).2‖ = 0
  /-- `Δτ = 0` from `Δs² = Δx² − Δτ²` on the null connection. -/
  deltaTau : ∀ Δτ : ℝ, 0 = ‖((b, 0) : ℝ × K.H).2 - ((a, 0) : ℝ × K.H).2‖ ^ 2 - Δτ ^ 2 → Δτ = 0
  /-- The two events are distinct when `a ≠ b`. -/
  distinct : a ≠ b → kl_psi K (a, 0) ≠ kl_psi K (b, 0)

/-- **Stage 1 on a given chart.** For any local Killing chart `K` of `hRep g p` with `X` null at `p`, there is
`ε > 0` such that `ψ (a, 0)`, `ψ (b, 0)` are locally metrically coincident whenever `|a|, |b| < ε`. -/
theorem kl_lemma_killing_chart (K : LocalKillingChart X p (hRep g p)) (hnull : g p (X p) (X p) = 0) :
    ∃ ε > 0, ∀ a b : ℝ, |a| < ε → |b| < ε → kl_MetricallyCoincidentLocal g K a b := by
  obtain ⟨ε, hε, hsrc⟩ := kl_exists_eps K
  refine ⟨ε, hε, fun a b ha hb => ?_⟩
  have hmem : ∀ t ∈ uIcc a b, ((t, 0) : ℝ × K.H) ∈ K.Φ.source := fun t ht =>
    hsrc t (kl_uIcc_abs_lt ha hb ht)
  have hma := hmem a left_mem_uIcc
  have hmb := hmem b right_mem_uIcc
  refine ⟨hmem, fun t ht => kl_velocity K _ (hmem t ht),
    fun t ht => (kl_null_along_orbit K hnull t (hmem t ht)).1,
    fun t ht => (kl_null_along_orbit K hnull t (hmem t ht)).2, ?_, ?_, by simp, ?_,
    kl_orbit_ne K hma hmb⟩
  · intro α F; rw [kl_lambda_indep_N K (b, 0) (a, 0) hmb hma rfl]
  · intro α F t ht; rw [kl_lambda_indep_N K (t, 0) (a, 0) (hmem t ht) hma rfl]
  · intro Δτ h
    simp only [sub_self, norm_zero] at h
    have : Δτ ^ 2 = 0 := by linarith
    exact pow_eq_zero_iff two_ne_zero |>.mp this

end KillingLocalNew

section KillingLocalHeadline

open Manifold

variable {N : Type*} [TopologicalSpace N] [ChartedSpace E N] [IsManifold 𝓘(ℝ, E) 1 N]
  [IsManifold 𝓘(ℝ, E) 2 N]

/-- **`lem:killing` stage 1, `kl_lemma_killing_local`.** Under `ld_manifold_killingChart_lieDeriv`'s
hypotheses (`N` a `C²` manifold, `X` `C¹` at `p` as a section with `X p ≠ 0`, `hRep g p` differentiable near
`φ p`, `L_X g = 0` near `p`) and `g_p(X p, X p) = 0`: there are a local Killing chart at `p` and `ε > 0` such
that for `|a|, |b| < ε` the orbit points `ψ (a, 0)`, `ψ (b, 0)` are locally metrically coincident. -/
theorem kl_lemma_killing_local (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N)
    (g : Π x : N, TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x →L[ℝ] ℝ)
    (hX : ContMDiffAt 𝓘(ℝ, E) 𝓘(ℝ, E).tangent 1
      (fun x ↦ (⟨x, X x⟩ : TangentBundle 𝓘(ℝ, E) N)) p) (hXp : X p ≠ 0)
    (hg : ∀ᶠ y in 𝓝 (extChartAt 𝓘(ℝ, E) p p), DifferentiableAt ℝ (hRep g p) y)
    (hK : ∀ᶠ x in 𝓝 p, ∀ v w, lieDeriv X g x v w = 0)
    (hnull : g p (X p) (X p) = 0) :
    ∃ K : LocalKillingChart X p (hRep g p), ∃ ε > 0, ∀ a b : ℝ, |a| < ε → |b| < ε →
      kl_MetricallyCoincidentLocal g K a b := by
  obtain ⟨K⟩ := ld_manifold_killingChart_lieDeriv X p g hX hXp hg hK
  exact ⟨K, kl_lemma_killing_chart K hnull⟩

end KillingLocalHeadline

/-! ### The orbit on the model space: `ψ (t, 0) = p + t • v` for a constant field `v` -/

section KillingLocalModel

open Manifold

/-- The chart formula vanishes for a constant metric and a constant field. -/
theorem kl_chartLie_const (B : E →L[ℝ] E →L[ℝ] ℝ) (c z a b : E) :
    chartLie (fun _ => B) (fun _ => c) z a b = 0 := by
  simp [chartLie]

/-- On the model space `N = E`, `ψ = Φ`. -/
theorem kl_psi_model {X : Π x : E, TangentSpace 𝓘(ℝ, E) x} {p : E} {gc : E → E →L[ℝ] E →L[ℝ] ℝ}
    (K : LocalKillingChart X p gc) : kl_psi K = K.Φ := by
  funext q; simp [kl_psi]

/-- **The orbit of a constant field, explicitly.** On the model space with `X ≡ v`, the orbit segment of any
local Killing chart is the straight line: `ψ (t, 0) = p + t • v` on any `(-ε, ε)` inside the flow box. -/
theorem kl_model_orbit {X : Π x : E, TangentSpace 𝓘(ℝ, E) x} (v : E) (hXv : ∀ x, X x = v) {p : E}
    {gc : E → E →L[ℝ] E →L[ℝ] ℝ} (K : LocalKillingChart X p gc) {ε : ℝ}
    (hsrc : ∀ t : ℝ, |t| < ε → ((t, 0) : ℝ × K.H) ∈ K.Φ.source) (t : ℝ) (ht : |t| < ε) :
    kl_psi K (t, 0) = p + t • v := by
  rw [kl_psi_model]
  set f : ℝ → E := fun s => K.Φ (s, 0) - s • v with hf
  have hderiv : ∀ s ∈ Ioo (-ε) ε, HasDerivAt f 0 s := by
    intro s hs
    have hs' : ((s, 0) : ℝ × K.H) ∈ K.Φ.source := hsrc s (abs_lt.2 hs)
    have hΦ : HasFDerivAt K.Φ (fderiv ℝ K.Φ (s, 0)) (s, 0) :=
      ((K.contDiffOn.contDiffAt (K.Φ.open_source.mem_nhds hs')).differentiableAt
        one_ne_zero).hasFDerivAt
    have hl : HasDerivAt (fun t : ℝ => ((t, 0) : ℝ × K.H)) ((1 : ℝ), (0 : K.H)) s :=
      (hasDerivAt_id s).prodMk (hasDerivAt_const s (0 : K.H))
    have hv : fderiv ℝ K.Φ (s, 0) ((1 : ℝ), (0 : K.H)) = v := by
      have h := kl_velocity K (s, 0) hs'
      unfold kl_dpsi at h
      rw [kl_psi_model, mfderiv_eq_fderiv, hXv] at h
      exact h
    have h1 := hΦ.comp_hasDerivAt s hl
    rw [hv] at h1
    have h2 := h1.sub ((hasDerivAt_id s).smul_const v)
    have h3 : v - (1 : ℝ) • v = 0 := by simp
    rw [h3] at h2
    exact h2
  have hε : 0 < ε := lt_of_le_of_lt (abs_nonneg t) ht
  have hc := isOpen_Ioo.is_const_of_deriv_eq_zero isPreconnected_Ioo
    (fun s hs => (hderiv s hs).differentiableAt.differentiableWithinAt)
    (fun s hs => (hderiv s hs).deriv) (abs_lt.1 ht) ⟨by linarith, hε⟩
  have h0 : K.Φ (0, 0) = p := by rw [K.map_zero]; simp
  simp only [hf, zero_smul, sub_zero, h0] at hc
  exact eq_add_of_sub_eq hc

end KillingLocalModel

/-! ### `kl_witness`: Minkowski `1+1` in light-cone form, `g = 2 dλ dx`, `X = ∂_λ` a null translation -/

section KillingLocalWitness

open Manifold

/-- The constant bilinear form `2 dλ dx` (symmetrised: `g(v, w) = v₁ w₂ + v₂ w₁`) on `ℝ × ℝ`. -/
noncomputable def kl_w_B : (ℝ × ℝ) →L[ℝ] (ℝ × ℝ) →L[ℝ] ℝ :=
  (ContinuousLinearMap.mul ℝ ℝ).bilinearComp (ContinuousLinearMap.fst ℝ ℝ ℝ)
      (ContinuousLinearMap.snd ℝ ℝ ℝ) +
    (ContinuousLinearMap.mul ℝ ℝ).bilinearComp (ContinuousLinearMap.snd ℝ ℝ ℝ)
      (ContinuousLinearMap.fst ℝ ℝ ℝ)

theorem kl_w_B_apply (v w : ℝ × ℝ) : kl_w_B v w = v.1 * w.2 + v.2 * w.1 := by
  simp [kl_w_B]

/-- The metric field on the model space `N = ℝ × ℝ`: the constant `2 dλ dx`. -/
noncomputable def kl_w_g :
    Π x : ℝ × ℝ, TangentSpace 𝓘(ℝ, ℝ × ℝ) x →L[ℝ] TangentSpace 𝓘(ℝ, ℝ × ℝ) x →L[ℝ] ℝ :=
  fun _ => kl_w_B

/-- The field `X = ∂_λ = (1, 0)`, constant. -/
def kl_w_X : Π x : ℝ × ℝ, TangentSpace 𝓘(ℝ, ℝ × ℝ) x := fun _ => ((1 : ℝ), (0 : ℝ))

/-- `2 dλ dx` is Lorentzian: symmetric, nondegenerate, with a timelike `(1, -1)` and a spacelike `(1, 1)`;
so the zero metric is excluded. -/
theorem kl_w_lorentzian :
    (∀ v w : ℝ × ℝ, kl_w_B v w = kl_w_B w v) ∧
    (∀ v : ℝ × ℝ, (∀ w, kl_w_B v w = 0) → v = 0) ∧
    kl_w_B (1, -1) (1, -1) < 0 ∧ 0 < kl_w_B (1, 1) (1, 1) := by
  refine ⟨fun v w => by simp only [kl_w_B_apply]; ring, fun v hv => ?_, ?_, ?_⟩
  · have h1 := hv (1, 0); have h2 := hv (0, 1)
    simp only [kl_w_B_apply] at h1 h2
    ext <;> simp <;> linarith
  · rw [kl_w_B_apply]; norm_num
  · rw [kl_w_B_apply]; norm_num

theorem kl_w_mfderiv_chart (p y : ℝ × ℝ) :
    mfderiv 𝓘(ℝ, ℝ × ℝ) 𝓘(ℝ, ℝ × ℝ) (extChartAt 𝓘(ℝ, ℝ × ℝ) p) y = ContinuousLinearMap.id ℝ _ := by
  rw [extChartAt_model_space_eq_id, PartialEquiv.refl_coe]
  exact mfderiv_id

theorem kl_w_mfderiv_chart_symm (p y : ℝ × ℝ) :
    mfderiv 𝓘(ℝ, ℝ × ℝ) 𝓘(ℝ, ℝ × ℝ) (extChartAt 𝓘(ℝ, ℝ × ℝ) p).symm y =
      ContinuousLinearMap.id ℝ _ := by
  rw [extChartAt_model_space_eq_id, PartialEquiv.refl_symm, PartialEquiv.refl_coe]
  exact mfderiv_id

/-- The chart representative of `g` is the constant `2 dλ dx`. -/
theorem kl_w_hRep (p : ℝ × ℝ) : hRep kl_w_g p = fun _ => kl_w_B := by
  funext y
  show kl_w_B.bilinearComp _ _ = kl_w_B
  rw [kl_w_mfderiv_chart_symm]
  exact ContinuousLinearMap.ext fun v => ContinuousLinearMap.ext fun w => rfl

/-- The chart representative of `X` is the constant `(1, 0)`. -/
theorem kl_w_chartRep (p : ℝ × ℝ) : chartRep kl_w_X p = fun _ => ((1 : ℝ), (0 : ℝ)) := by
  funext y
  show mfderiv 𝓘(ℝ, ℝ × ℝ) 𝓘(ℝ, ℝ × ℝ) (extChartAt 𝓘(ℝ, ℝ × ℝ) p) _ ((1 : ℝ), (0 : ℝ)) = _
  rw [kl_w_mfderiv_chart]
  rfl

/-- **`L_X g = 0` everywhere**, through the registered `lieDeriv` (`ld_lieDeriv_chart_self`): every term of
the chart formula vanishes for constant `g` and `X`. -/
theorem kl_w_lieDeriv (x v w : ℝ × ℝ) : lieDeriv kl_w_X kl_w_g x v w = 0 := by
  rw [ld_lieDeriv_chart_self kl_w_X kl_w_g x v w
    (by rw [kl_w_hRep]; exact differentiableAt_const _)]
  rw [kl_w_hRep, kl_w_chartRep]
  exact kl_chartLie_const _ _ _ _ _

/-- `X` is `C¹` as a section of the tangent bundle. -/
theorem kl_w_hX (p : ℝ × ℝ) : ContMDiffAt 𝓘(ℝ, ℝ × ℝ) 𝓘(ℝ, ℝ × ℝ).tangent 1
    (fun x ↦ (⟨x, kl_w_X x⟩ : TangentBundle 𝓘(ℝ, ℝ × ℝ) (ℝ × ℝ))) p :=
  (contMDiffAt_vectorSpace_iff_contDiffAt (V := kl_w_X)).2 contDiffAt_const

theorem kl_w_hXp (p : ℝ × ℝ) : kl_w_X p ≠ 0 := by
  show ((1 : ℝ), (0 : ℝ)) ≠ 0
  simp

/-- `X` is null: `g(X, X) = 0`. -/
theorem kl_w_null (p : ℝ × ℝ) : kl_w_g p (kl_w_X p) (kl_w_X p) = 0 := by
  show kl_w_B ((1 : ℝ), (0 : ℝ)) ((1 : ℝ), (0 : ℝ)) = 0
  rw [kl_w_B_apply]; norm_num

/-- **`kl_witness`.** On Minkowski `1+1` in light-cone form (`N = ℝ × ℝ`, `g = 2 dλ dx`, `X = ∂_λ`), every
hypothesis of `kl_lemma_killing_local` holds at `p = (0, 0)`, and the chart and `ε` it returns give explicit
distinct coincident events: for `|a|, |b| < ε` the orbit points are `ψ (a, 0) = (a, 0)`, `ψ (b, 0) = (b, 0)`;
in particular `(0, 0) ≠ (ε/2, 0)` are locally metrically coincident. -/
theorem kl_witness :
    ∃ K : LocalKillingChart kl_w_X ((0 : ℝ), (0 : ℝ)) (hRep kl_w_g (0, 0)), ∃ ε > 0,
      (∀ a b : ℝ, |a| < ε → |b| < ε →
        kl_MetricallyCoincidentLocal kl_w_g K a b ∧
          kl_psi K (a, 0) = (a, 0) ∧ kl_psi K (b, 0) = (b, 0)) ∧
      kl_MetricallyCoincidentLocal kl_w_g K 0 (ε / 2) ∧
      kl_psi K (0, 0) = ((0 : ℝ), (0 : ℝ)) ∧ kl_psi K (ε / 2, 0) = (ε / 2, 0) ∧
      kl_psi K (0, 0) ≠ kl_psi K (ε / 2, 0) := by
  obtain ⟨K, ε, hε, hC⟩ := kl_lemma_killing_local kl_w_X (0, 0) kl_w_g (kl_w_hX _) (kl_w_hXp _)
    (Filter.Eventually.of_forall fun y => by rw [kl_w_hRep]; exact differentiableAt_const _)
    (Filter.Eventually.of_forall fun x v w => kl_w_lieDeriv x v w) (kl_w_null _)
  obtain ⟨ε', hε', hsrc⟩ := kl_exists_eps K
  set δ := min ε ε' with hδ
  have hδ0 : 0 < δ := lt_min hε hε'
  have hpos : ∀ t : ℝ, |t| < δ → kl_psi K (t, 0) = (t, 0) := fun t ht => by
    have := kl_model_orbit (E := ℝ × ℝ) ((1 : ℝ), (0 : ℝ)) (fun _ => rfl) K (ε := ε')
      hsrc t (lt_of_lt_of_le ht (min_le_right _ _))
    exact this.trans (by ext <;> simp)
  have hC' : ∀ a b : ℝ, |a| < δ → |b| < δ → kl_MetricallyCoincidentLocal kl_w_g K a b :=
    fun a b ha hb => hC a b (lt_of_lt_of_le ha (min_le_left _ _)) (lt_of_lt_of_le hb (min_le_left _ _))
  have h0 : |(0 : ℝ)| < δ := by simpa using hδ0
  have h2 : |δ / 2| < δ := by rw [abs_of_pos (by positivity)]; linarith
  refine ⟨K, δ, hδ0, fun a b ha hb => ⟨hC' a b ha hb, hpos a ha, hpos b hb⟩, hC' 0 (δ / 2) h0 h2,
    hpos 0 h0, hpos _ h2, (hC' 0 (δ / 2) h0 h2).distinct (by positivity : (0 : ℝ) < δ / 2).ne⟩

end KillingLocalWitness


/-! ## NEW (campaign 95, `r7671+71`): `lem:killing` stage 2, along a whole generator

Prefix `kg_`. See the header. -/

set_option linter.unusedSectionVars false

section KGBox

variable {f : E → E} {x₀ : E}

theorem kg_flowBox_killing_symm {ρ : ℝ} (hρ : 0 < ρ) (hf : ContDiffOn ℝ 1 f (ball x₀ ρ))
    (hfx : f x₀ ≠ 0) (g : E → E →L[ℝ] E →L[ℝ] ℝ) (hg : DifferentiableOn ℝ g (ball x₀ ρ))
    (hK : ∀ y ∈ ball x₀ ρ, ∀ v w,
      fderiv ℝ g y (f y) v w + g y (fderiv ℝ f y v) w + g y v (fderiv ℝ f y w) = 0) :
    ∃ (H : Submodule ℝ E) (Φ : OpenPartialHomeomorph (ℝ × H) E),
      ((0 : ℝ), (0 : H)) ∈ Φ.source ∧ Φ (0, 0) = x₀ ∧ MapsTo Φ Φ.source (ball x₀ (ρ / 4)) ∧
      ContDiffOn ℝ 1 Φ Φ.source ∧ (∀ q ∈ Φ.source, fderiv ℝ Φ q (1, 0) = f (Φ q)) ∧
      (∀ᶠ y in 𝓝 x₀, ContDiffAt ℝ 1 Φ.symm y) ∧
      ∀ q ∈ Φ.source, ∀ u u' : ℝ × H, g (Φ q) (fderiv ℝ Φ q u) (fderiv ℝ Φ q u') =
        g (x₀ + q.2) (u.1 • f (x₀ + q.2) + u.2) (u'.1 • f (x₀ + q.2) + u'.2) := by
  obtain ⟨H, D, Φ, hΦ, hR, hJ⟩ := ld_flowBox_exists_of_contDiffOn_var hρ hf hfx
  have hsub : closedBall x₀ D.R ⊆ ball x₀ ρ :=
    (closedBall_subset_ball hR).trans (ball_subset_ball (by linarith))
  have hfd : ∀ y ∈ closedBall x₀ D.R, DifferentiableAt ℝ f y := fun y hy =>
    (hf.differentiableOn one_ne_zero).differentiableAt (isOpen_ball.mem_nhds (hsub hy))
  have hgd : ∀ y ∈ closedBall x₀ D.R, DifferentiableAt ℝ g y := fun y hy =>
    hg.differentiableAt (isOpen_ball.mem_nhds (hsub hy))
  exact ⟨H, Φ, hΦ.zero_mem, hΦ.map_zero,
    fun q hq => closedBall_subset_ball hR (D.ld_isFlowBox_mem hΦ q hq), hΦ.contDiffOn,
    hΦ.straightens, hΦ.symm_contDiffAt,
    fun q hq u u' => D.ld_flowBox_pullback_loc hfd hJ g hgd
      (fun y hy => hK y (hsub hy)) hΦ q hq u u'⟩

end KGBox


section KGChart

open Manifold

variable {N : Type*} [TopologicalSpace N] [ChartedSpace E N] [IsManifold 𝓘(ℝ, E) 1 N]

/-- A local Killing chart whose flow-box map has a `C¹` inverse on its whole target. -/
def kg_SymmC1 {X : Π x : N, TangentSpace 𝓘(ℝ, E) x} {p : N} {gc : E → E →L[ℝ] E →L[ℝ] ℝ}
    (K : LocalKillingChart X p gc) : Prop :=
  ∀ y ∈ K.Φ.target, ContDiffAt ℝ 1 K.Φ.symm y

/-- **Restricting a local Killing chart** to the part of its source mapped into an open set `W ∋ φ p`. -/
noncomputable def kg_restrict {X : Π x : N, TangentSpace 𝓘(ℝ, E) x} {p : N}
    {gc : E → E →L[ℝ] E →L[ℝ] ℝ} (K : LocalKillingChart X p gc) (W : Set E) (hW : IsOpen W)
    (hpW : extChartAt 𝓘(ℝ, E) p p ∈ W) : LocalKillingChart X p gc where
  H := K.H
  Φ := K.Φ.restrOpen (K.Φ.source ∩ K.Φ ⁻¹' W)
    (K.Φ.continuousOn.isOpen_inter_preimage K.Φ.open_source hW)
  zero_mem := ⟨K.zero_mem, K.zero_mem, by simp only [mem_preimage, K.map_zero]; exact hpW⟩
  map_zero := K.map_zero
  ψ_zero := K.ψ_zero
  mapsTo := fun q hq => K.mapsTo hq.1
  contDiffOn := K.contDiffOn.mono fun q hq => hq.1
  straightens := fun q hq => K.straightens q hq.1
  gH := K.gH
  metric_eq := fun q hq u u' => K.metric_eq q hq.1 u u'

theorem kg_restrict_source {X : Π x : N, TangentSpace 𝓘(ℝ, E) x} {p : N}
    {gc : E → E →L[ℝ] E →L[ℝ] ℝ} (K : LocalKillingChart X p gc) (W : Set E) (hW : IsOpen W)
    (hpW : extChartAt 𝓘(ℝ, E) p p ∈ W) {q : ℝ × K.H} (hq : q ∈ (kg_restrict K W hW hpW).Φ.source) :
    K.Φ q ∈ W := hq.2.2

theorem kg_restrict_symmC1 {X : Π x : N, TangentSpace 𝓘(ℝ, E) x} {p : N}
    {gc : E → E →L[ℝ] E →L[ℝ] ℝ} (K : LocalKillingChart X p gc) (W : Set E) (hW : IsOpen W)
    (hpW : extChartAt 𝓘(ℝ, E) p p ∈ W) (hWs : ∀ y ∈ W, ContDiffAt ℝ 1 K.Φ.symm y) :
    kg_SymmC1 (kg_restrict K W hW hpW) := by
  intro y hy
  set K' := kg_restrict K W hW hpW
  have h1 := K'.Φ.map_target hy
  have h2 := K'.Φ.right_inv hy
  have h3 : K.Φ (K.Φ.symm y) ∈ W := kg_restrict_source K W hW hpW h1
  have h4 : K.Φ (K.Φ.symm y) = y := h2
  rw [h4] at h3
  exact hWs y h3

end KGChart

section KGChart2

open Manifold

variable {N : Type*} [TopologicalSpace N] [ChartedSpace E N] [IsManifold 𝓘(ℝ, E) 1 N]
  [IsManifold 𝓘(ℝ, E) 2 N]

/-- **A local Killing chart with a `C¹` inverse**, under `ld_manifold_killingChart_lieDeriv`'s hypotheses
(the proof is that theorem's, keeping the flow box's `symm_contDiffAt`, then restricting). -/
theorem kg_killingChart_symm (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N)
    (g : Π x : N, TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x →L[ℝ] ℝ)
    (hX : ContMDiffAt 𝓘(ℝ, E) 𝓘(ℝ, E).tangent 1
      (fun x ↦ (⟨x, X x⟩ : TangentBundle 𝓘(ℝ, E) N)) p) (hXp : X p ≠ 0)
    (hg : ∀ᶠ y in 𝓝 (extChartAt 𝓘(ℝ, E) p p), DifferentiableAt ℝ (hRep g p) y)
    (hK : ∀ᶠ x in 𝓝 p, ∀ v w, lieDeriv X g x v w = 0) :
    ∃ K : LocalKillingChart X p (hRep g p), kg_SymmC1 K := by
  set e := extChartAt 𝓘(ℝ, E) p with he
  obtain ⟨ρ, hρ, hball, hf⟩ := ld_chartRep_ball_of_section X p hX
  have hK' : ∀ᶠ y in 𝓝 (e p), ∀ v w, lieDeriv X g (e.symm y) v w = 0 := by
    have hc := continuousAt_extChartAt_symm (I := 𝓘(ℝ, E)) p
    rw [ContinuousAt, extChartAt_to_inv] at hc
    exact hc hK
  obtain ⟨ρ', hρ', hb⟩ := Metric.eventually_nhds_iff_ball.1 (hK'.and hg)
  set r := min ρ ρ' with hr_def
  have hr : 0 < r := lt_min hρ hρ'
  have hrρ : ball (e p) r ⊆ ball (e p) ρ := ball_subset_ball (min_le_left _ _)
  have hrρ' : ball (e p) r ⊆ ball (e p) ρ' := ball_subset_ball (min_le_right _ _)
  have hballr : ball (e p) r ⊆ e.target := hrρ.trans hball
  have hfr : ContDiffOn ℝ 1 (chartRep X p) (ball (e p) r) := hf.mono hrρ
  have hgd : DifferentiableOn ℝ (hRep g p) (ball (e p) r) := fun y hy =>
    (hb y (hrρ' hy)).2.differentiableWithinAt
  have hKb : ∀ y ∈ ball (e p) r, ∀ v w, fderiv ℝ (hRep g p) y (chartRep X p y) v w +
      hRep g p y (fderiv ℝ (chartRep X p) y v) w + hRep g p y v (fderiv ℝ (chartRep X p) y w) = 0 := by
    intro y hy v w
    have hyt := hballr hy
    have hx : e.symm y ∈ (chartAt E p).source := by
      rw [← extChartAt_source 𝓘(ℝ, E)]; exact e.map_target hyt
    have hey : e (e.symm y) = y := e.right_inv hyt
    have hXc : ContDiffAt ℝ 1 (chartRep X p) (e (e.symm y)) := by
      rw [hey]; exact hfr.contDiffAt (isOpen_ball.mem_nhds hy)
    have hhd : DifferentiableAt ℝ (hRep g p) (e (e.symm y)) := by
      rw [hey]; exact (hb y (hrρ' hy)).2
    have hc := ld_chartLie_zero_of_lieDeriv X g p hx hXc hhd (hb y (hrρ' hy)).1 v w
    rw [hey] at hc
    exact hc
  obtain ⟨H, Φ, h0, hΦ0, hmaps, hc, hstr, hsymm, hpull⟩ :=
    kg_flowBox_killing_symm hr hfr (ld_chartRep_ne_zero X p hXp) (hRep g p) hgd hKb
  have hmaps' : MapsTo Φ Φ.source e.target := fun q hq =>
    hballr (ball_subset_ball (by linarith) (hmaps hq))
  let K : LocalKillingChart X p (hRep g p) :=
    ⟨H, Φ, h0, hΦ0, by simp only [Function.comp_apply, hΦ0]; exact extChartAt_to_inv p,
      hmaps', hc, ld_mfderiv_straightens X p Φ hmaps' hc hstr,
      fun h u u' => hRep g p (e p + h) (u.1 • chartRep X p (e p + h) + u.2)
        (u'.1 • chartRep X p (e p + h) + u'.2),
      fun q hq u u' => hpull q hq u u'⟩
  obtain ⟨W, hWs, hWo, hpW⟩ := _root_.eventually_nhds_iff.1 hsymm
  exact ⟨kg_restrict K W hWo hpW, kg_restrict_symmC1 K W hWo hpW hWs⟩

end KGChart2

section KGShift

open Manifold

variable {N : Type*} [TopologicalSpace N] [ChartedSpace E N] [IsManifold 𝓘(ℝ, E) 1 N]
variable {X : Π x : N, TangentSpace 𝓘(ℝ, E) x} {p : N} {gc : E → E →L[ℝ] E →L[ℝ] ℝ}

/-- The inverse adapted chart `ψ⁻¹ = Φ⁻¹ ∘ φ : N → ℝ × H`. -/
noncomputable def kg_chi (K : LocalKillingChart X p gc) (x : N) : ℝ × K.H :=
  K.Φ.symm (extChartAt 𝓘(ℝ, E) p x)

/-- The image of the flow box in `N`: the domain of `ψ⁻¹`. -/
def kg_dom (K : LocalKillingChart X p gc) : Set N :=
  (extChartAt 𝓘(ℝ, E) p).source ∩ extChartAt 𝓘(ℝ, E) p ⁻¹' K.Φ.target

/-- **The flow-box translation** `F_δ = ψ ∘ (· + (δ, 0)) ∘ ψ⁻¹ : N → N`. -/
noncomputable def kg_shift (K : LocalKillingChart X p gc) (δ : ℝ) (x : N) : N :=
  kl_psi K (kg_chi K x + (δ, 0))

/-- Where `F_δ` is defined by the box: `x ∈ ψ(box)` with `ψ⁻¹ x + (δ, 0)` still in the box. -/
def kg_U (K : LocalKillingChart X p gc) (δ : ℝ) : Set N :=
  kg_dom K ∩ kg_chi K ⁻¹' ((fun q : ℝ × K.H => q + ((δ, 0) : ℝ × K.H)) ⁻¹' K.Φ.source)

theorem kg_chi_psi (K : LocalKillingChart X p gc) {q : ℝ × K.H} (hq : q ∈ K.Φ.source) :
    kg_chi K (kl_psi K q) = q := by
  unfold kg_chi kl_psi
  rw [Function.comp_apply, (extChartAt 𝓘(ℝ, E) p).right_inv (K.mapsTo hq), K.Φ.left_inv hq]

theorem kg_psi_mem_dom (K : LocalKillingChart X p gc) {q : ℝ × K.H} (hq : q ∈ K.Φ.source) :
    kl_psi K q ∈ kg_dom K := by
  refine ⟨(extChartAt 𝓘(ℝ, E) p).map_target (K.mapsTo hq), ?_⟩
  show extChartAt 𝓘(ℝ, E) p ((extChartAt 𝓘(ℝ, E) p).symm (K.Φ q)) ∈ K.Φ.target
  rw [(extChartAt 𝓘(ℝ, E) p).right_inv (K.mapsTo hq)]
  exact K.Φ.map_source hq

theorem kg_psi_chi (K : LocalKillingChart X p gc) {x : N} (hx : x ∈ kg_dom K) :
    kl_psi K (kg_chi K x) = x := by
  unfold kg_chi kl_psi
  rw [Function.comp_apply, K.Φ.right_inv hx.2, (extChartAt 𝓘(ℝ, E) p).left_inv hx.1]

theorem kg_chi_mem (K : LocalKillingChart X p gc) {x : N} (hx : x ∈ kg_dom K) :
    kg_chi K x ∈ K.Φ.source := K.Φ.map_target hx.2

theorem kg_dom_open (K : LocalKillingChart X p gc) : IsOpen (kg_dom K) :=
  isOpen_extChartAt_preimage' p K.Φ.open_target

theorem kg_chi_mdiff (K : LocalKillingChart X p gc) (hS : kg_SymmC1 K) {x : N} (hx : x ∈ kg_dom K) :
    MDifferentiableAt 𝓘(ℝ, E) 𝓘(ℝ, ℝ × K.H) (kg_chi K) x := by
  have h1 : MDifferentiableAt 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) x :=
    mdifferentiableAt_extChartAt (by rw [← extChartAt_source 𝓘(ℝ, E)]; exact hx.1)
  have h2 : MDifferentiableAt 𝓘(ℝ, E) 𝓘(ℝ, ℝ × K.H) K.Φ.symm (extChartAt 𝓘(ℝ, E) p x) :=
    mdifferentiableAt_iff_differentiableAt.2 ((hS _ hx.2).differentiableAt one_ne_zero)
  exact h2.comp x h1

theorem kg_U_open (K : LocalKillingChart X p gc) (hS : kg_SymmC1 K) (δ : ℝ) : IsOpen (kg_U K δ) := by
  have hc : ContinuousOn (kg_chi K) (kg_dom K) := fun x hx =>
    (kg_chi_mdiff K hS hx).continuousAt.continuousWithinAt
  exact hc.isOpen_inter_preimage (kg_dom_open K)
    (K.Φ.open_source.preimage (continuous_id.add continuous_const))

theorem kg_psi_mdiff (K : LocalKillingChart X p gc) {q : ℝ × K.H} (hq : q ∈ K.Φ.source) :
    MDifferentiableAt 𝓘(ℝ, ℝ × K.H) 𝓘(ℝ, E) (kl_psi K) q := by
  have hΦd : DifferentiableAt ℝ K.Φ q :=
    (K.contDiffOn.contDiffAt (K.Φ.open_source.mem_nhds hq)).differentiableAt one_ne_zero
  exact (ld_mdifferentiableAt_symm p (K.mapsTo hq)).comp q
    (mdifferentiableAt_iff_differentiableAt.2 hΦd)

/-- `Dψ ∘ Dψ⁻¹ = id` on the box image. -/
theorem kg_dpsi_dchi (K : LocalKillingChart X p gc) (hS : kg_SymmC1 K) {x : N} (hx : x ∈ kg_dom K)
    (v : E) : kl_dpsi K (kg_chi K x) (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, ℝ × K.H) (kg_chi K) x v) = v := by
  have hc := mfderiv_comp x (kg_psi_mdiff K (kg_chi_mem K hx)) (kg_chi_mdiff K hS hx)
  have he : kl_psi K ∘ kg_chi K =ᶠ[𝓝 x] id :=
    Filter.eventually_of_mem ((kg_dom_open K).mem_nhds hx) fun y hy => kg_psi_chi K hy
  rw [he.mfderiv_eq, mfderiv_id] at hc
  exact (DFunLike.congr_fun hc v).symm

end KGShift

section KGShift2

open Manifold

variable {N : Type*} [TopologicalSpace N] [ChartedSpace E N] [IsManifold 𝓘(ℝ, E) 1 N]
variable {X : Π x : N, TangentSpace 𝓘(ℝ, E) x} {p : N} {gc : E → E →L[ℝ] E →L[ℝ] ℝ}

theorem kg_add_mdiff {H : Submodule ℝ E} (c q : ℝ × H) :
    HasMFDerivAt 𝓘(ℝ, ℝ × H) 𝓘(ℝ, ℝ × H) (fun q : ℝ × H => q + c) q
      (ContinuousLinearMap.id ℝ (ℝ × H)) :=
  ((hasFDerivAt_id q).add_const c).hasMFDerivAt

/-- `F_δ` is differentiable on `kg_U`, with `DF_δ v = Dψ_{ψ⁻¹x + (δ,0)} (Dψ⁻¹_x v)`. -/
theorem kg_shift_hasMFDerivAt (K : LocalKillingChart X p gc) (hS : kg_SymmC1 K) (δ : ℝ) {x : N}
    (hx : x ∈ kg_U K δ) :
    HasMFDerivAt 𝓘(ℝ, E) 𝓘(ℝ, E) (kg_shift K δ) x
      ((kl_dpsi K (kg_chi K x + (δ, 0))).comp (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, ℝ × K.H) (kg_chi K) x)) := by
  have h1 := (kg_chi_mdiff K hS hx.1).hasMFDerivAt
  have h2 := kg_add_mdiff ((δ, 0) : ℝ × K.H) (kg_chi K x)
  have h3 := (kg_psi_mdiff K hx.2).hasMFDerivAt
  have h := h3.comp x (h2.comp x h1)
  exact h

theorem kg_shift_mdiff (K : LocalKillingChart X p gc) (hS : kg_SymmC1 K) (δ : ℝ) {x : N}
    (hx : x ∈ kg_U K δ) : MDifferentiableAt 𝓘(ℝ, E) 𝓘(ℝ, E) (kg_shift K δ) x :=
  (kg_shift_hasMFDerivAt K hS δ hx).mdifferentiableAt

theorem kg_mfderiv_shift (K : LocalKillingChart X p gc) (hS : kg_SymmC1 K) (δ : ℝ) {x : N}
    (hx : x ∈ kg_U K δ) (v : E) :
    mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (kg_shift K δ) x v =
      kl_dpsi K (kg_chi K x + (δ, 0)) (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, ℝ × K.H) (kg_chi K) x v) := by
  rw [(kg_shift_hasMFDerivAt K hS δ hx).mfderiv]; rfl

theorem kg_g_congr (g : Π x : N, TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x →L[ℝ] ℝ)
    {y z : N} (h : y = z) (a b : E) : g y a b = g z a b := by subst h; rfl

variable {g : Π x : N, TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x →L[ℝ] ℝ}

/-- **The flow-box translation is an isometry** on `kg_U K δ`: because the adapted components depend only
on the transverse coordinate (`kl_lambda_indep_N`). -/
theorem kg_shift_isometry (K : LocalKillingChart X p (hRep g p)) (hS : kg_SymmC1 K) (δ : ℝ) {x : N}
    (hx : x ∈ kg_U K δ) (v w : E) :
    g (kg_shift K δ x) (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (kg_shift K δ) x v)
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (kg_shift K δ) x w) = g x v w := by
  rw [kg_mfderiv_shift K hS δ hx v, kg_mfderiv_shift K hS δ hx w]
  set q := kg_chi K x
  have hq : q ∈ K.Φ.source := kg_chi_mem K hx.1
  have hq' : q + ((δ, 0) : ℝ × K.H) ∈ K.Φ.source := hx.2
  set u := mfderiv 𝓘(ℝ, E) 𝓘(ℝ, ℝ × K.H) (kg_chi K) x v
  set u' := mfderiv 𝓘(ℝ, E) 𝓘(ℝ, ℝ × K.H) (kg_chi K) x w
  have h1 : g (kg_shift K δ x) (kl_dpsi K (q + (δ, 0)) u) (kl_dpsi K (q + (δ, 0)) u') =
      kl_comps g K (q + (δ, 0)) u u' := rfl
  have h2 := kl_lambda_indep_N K (q + (δ, 0)) q hq' hq (by simp)
  rw [h1, h2]
  show g (kl_psi K q) (kl_dpsi K q u) (kl_dpsi K q u') = g x v w
  rw [kg_dpsi_dchi K hS hx.1 v, kg_dpsi_dchi K hS hx.1 w]
  exact kg_g_congr g (kg_psi_chi K hx.1) v w

/-- `x ∈ ψ(box)` with `ψ⁻¹ x = q` and `q + (δ, 0)` in the box gives `x ∈ kg_U K δ`. -/
theorem kg_psi_mem_U (K : LocalKillingChart X p gc) {q : ℝ × K.H} (hq : q ∈ K.Φ.source) (δ : ℝ)
    (hq' : q + ((δ, 0) : ℝ × K.H) ∈ K.Φ.source) : kl_psi K q ∈ kg_U K δ :=
  ⟨kg_psi_mem_dom K hq, by
    show kg_chi K (kl_psi K q) + ((δ, 0) : ℝ × K.H) ∈ K.Φ.source
    rw [kg_chi_psi K hq]; exact hq'⟩

theorem kg_shift_psi (K : LocalKillingChart X p gc) {q : ℝ × K.H} (hq : q ∈ K.Φ.source) (δ : ℝ) :
    kg_shift K δ (kl_psi K q) = kl_psi K (q + (δ, 0)) := by
  unfold kg_shift; rw [kg_chi_psi K hq]

/-- **The box orbit is an integral curve:** `s ↦ ψ(s − c, 0)` has velocity `X` where it is in the box. -/
theorem kg_orbit_hasMFDerivAt (K : LocalKillingChart X p gc) (c s : ℝ)
    (hs : ((s - c, 0) : ℝ × K.H) ∈ K.Φ.source) :
    HasMFDerivAt 𝓘(ℝ, ℝ) 𝓘(ℝ, E) (fun s => kl_psi K (s - c, 0)) s
      ((1 : ℝ →L[ℝ] ℝ).smulRight (X (kl_psi K (s - c, 0)))) := by
  have hL : HasDerivAt (fun s : ℝ => ((s - c, 0) : ℝ × K.H)) ((1 : ℝ), (0 : K.H)) s :=
    ((hasDerivAt_id s).sub_const c).prodMk (hasDerivAt_const s (0 : K.H))
  have hL' : HasMFDerivAt 𝓘(ℝ, ℝ) 𝓘(ℝ, ℝ × K.H) (fun s : ℝ => ((s - c, 0) : ℝ × K.H)) s
      ((1 : ℝ →L[ℝ] ℝ).smulRight ((1 : ℝ), (0 : K.H))) := hL.hasFDerivAt.hasMFDerivAt
  have h := (kg_psi_mdiff K hs).hasMFDerivAt.comp s hL'
  refine h.congr_mfderiv (ContinuousLinearMap.ext fun (r : ℝ) => ?_)
  have hst := K.straightens _ hs
  show mfderiv 𝓘(ℝ, ℝ × K.H) 𝓘(ℝ, E) (kl_psi K) ((s - c, 0) : ℝ × K.H) (r • ((1 : ℝ), (0 : K.H))) =
    r • X (kl_psi K (s - c, 0))
  exact (ContinuousLinearMap.map_smul _ r _).trans (congrArg (r • ·) hst)

/-- **Uniqueness of integral curves identifies `γ` with the box orbit** near `t`. -/
theorem kg_curve_eq_orbit (K : LocalKillingChart X p gc) {γ : ℝ → N} {t : ℝ} (hγt : γ t = p)
    (hX : ContMDiffAt 𝓘(ℝ, E) 𝓘(ℝ, E).tangent 1
      (fun x ↦ (⟨x, X x⟩ : TangentBundle 𝓘(ℝ, E) N)) (γ t))
    (hγ : IsMIntegralCurveAt γ X t) :
    ∃ ρ > 0, ∀ s ∈ ball t ρ, ((s - t, 0) : ℝ × K.H) ∈ K.Φ.source ∧ γ s = kl_psi K (s - t, 0) := by
  obtain ⟨ε, hε, hsrc⟩ := kl_exists_eps K
  have hmem : ∀ᶠ s in 𝓝 t, ((s - t, 0) : ℝ × K.H) ∈ K.Φ.source := by
    filter_upwards [Metric.ball_mem_nhds t hε] with s hs
    exact hsrc _ (by rw [← Real.dist_eq]; exact hs)
  have ho : IsMIntegralCurveAt (fun s => kl_psi K (s - t, 0)) X t := by
    filter_upwards [hmem] with s hs
    exact kg_orbit_hasMFDerivAt K t s hs
  have h0 : γ t = (fun s => kl_psi K (s - t, 0)) t := by
    simp only [sub_self]; rw [hγt]; exact (kl_psi_zero K).symm
  have heq := isMIntegralCurveAt_eventuallyEq_of_contMDiffAt_boundaryless hX hγ ho h0
  obtain ⟨ρ, hρ, hb⟩ := Metric.eventually_nhds_iff_ball.1 (hmem.and heq)
  exact ⟨ρ, hρ, fun s hs => hb s hs⟩

end KGShift2

section KGGenerator

open Manifold

variable {N : Type*} [TopologicalSpace N] [ChartedSpace E N] [IsManifold 𝓘(ℝ, E) 1 N]

/-- **Metric coincidence along a generator (b).** `t₁` and `t₂` are related when there are an open
`U ∋ γ t₁` and a map `F : N → N` with `F (γ t₁) = γ t₂`, `F` differentiable and an isometry of `g` on `U`
(`g_{F x}(DF v, DF w) = g_x(v, w)`), and `F` carrying the generator into itself:
`F (γ s) = γ (s + t₂ − t₁)` for `s` near `t₁`. -/
def kg_Related (g : Π x : N, TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x →L[ℝ] ℝ)
    (γ : ℝ → N) (t₁ t₂ : ℝ) : Prop :=
  ∃ U : Set N, ∃ F : N → N, IsOpen U ∧ γ t₁ ∈ U ∧ F (γ t₁) = γ t₂ ∧
    (∀ x ∈ U, MDifferentiableAt 𝓘(ℝ, E) 𝓘(ℝ, E) F x) ∧
    (∀ x ∈ U, ∀ v w : E, g (F x) (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) F x v)
      (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) F x w) = g x v w) ∧
    ∀ᶠ s in 𝓝 t₁, F (γ s) = γ (s + t₂ - t₁)

variable {g : Π x : N, TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x →L[ℝ] ℝ} {γ : ℝ → N}

/-- **Composition:** the relation is transitive (compose the isometries on `U₁ ∩ F₁⁻¹ U₂`). -/
theorem kg_related_trans {t₁ t₂ t₃ : ℝ} (h₁ : kg_Related g γ t₁ t₂) (h₂ : kg_Related g γ t₂ t₃) :
    kg_Related g γ t₁ t₃ := by
  obtain ⟨U₁, F₁, hU₁, hm₁, hF₁, hd₁, hi₁, hc₁⟩ := h₁
  obtain ⟨U₂, F₂, hU₂, hm₂, hF₂, hd₂, hi₂, hc₂⟩ := h₂
  have hcont : ContinuousOn F₁ U₁ := fun x hx => (hd₁ x hx).continuousAt.continuousWithinAt
  refine ⟨U₁ ∩ F₁ ⁻¹' U₂, F₂ ∘ F₁, hcont.isOpen_inter_preimage hU₁ hU₂,
    ⟨hm₁, by rw [mem_preimage, hF₁]; exact hm₂⟩, by rw [Function.comp_apply, hF₁, hF₂],
    fun x hx => (hd₂ _ hx.2).comp x (hd₁ x hx.1), fun x hx v w => ?_, ?_⟩
  · have e1 := mfderiv_comp_apply x (hd₂ _ hx.2) (hd₁ x hx.1) v
    have e2 := mfderiv_comp_apply x (hd₂ _ hx.2) (hd₁ x hx.1) w
    exact (congrArg₂ (fun a b : E => g (F₂ (F₁ x)) a b) e1 e2).trans
      ((hi₂ _ hx.2 _ _).trans (hi₁ x hx.1 v w))
  · have ht : Tendsto (fun s : ℝ => s + t₂ - t₁) (𝓝 t₁) (𝓝 t₂) :=
      ((continuous_id.add continuous_const).sub continuous_const).tendsto' t₁ t₂ (by simp)
    filter_upwards [hc₁, ht.eventually hc₂] with s hs1 hs2
    rw [Function.comp_apply, hs1, hs2]
    congr 1; ring

variable [IsManifold 𝓘(ℝ, E) 2 N]

/-- **One box along the generator.** At `t₁` there are a local Killing chart at `γ t₁` (with `C¹` inverse)
and a window `ball t₁ ρ` on which `γ s = ψ (s − t₁, 0)`. -/
theorem kg_box_along (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (t₁ : ℝ)
    (hX : ContMDiffAt 𝓘(ℝ, E) 𝓘(ℝ, E).tangent 1
      (fun x ↦ (⟨x, X x⟩ : TangentBundle 𝓘(ℝ, E) N)) (γ t₁)) (hXp : X (γ t₁) ≠ 0)
    (hg : ∀ᶠ y in 𝓝 (extChartAt 𝓘(ℝ, E) (γ t₁) (γ t₁)), DifferentiableAt ℝ (hRep g (γ t₁)) y)
    (hK : ∀ᶠ x in 𝓝 (γ t₁), ∀ v w, lieDeriv X g x v w = 0)
    (hγ : IsMIntegralCurveAt γ X t₁) :
    ∃ K : LocalKillingChart X (γ t₁) (hRep g (γ t₁)), kg_SymmC1 K ∧ ∃ ρ > 0, ∀ s ∈ ball t₁ ρ,
      ((s - t₁, 0) : ℝ × K.H) ∈ K.Φ.source ∧ γ s = kl_psi K (s - t₁, 0) := by
  obtain ⟨K, hS⟩ := kg_killingChart_symm X (γ t₁) g hX hXp hg hK
  exact ⟨K, hS, kg_curve_eq_orbit K rfl hX hγ⟩

/-- **Locally, every pair is related:** inside one box window, `F_δ = ψ ∘ (· + (δ, 0)) ∘ ψ⁻¹`. -/
theorem kg_related_box {X : Π x : N, TangentSpace 𝓘(ℝ, E) x} {t₁ : ℝ}
    (K : LocalKillingChart X (γ t₁) (hRep g (γ t₁))) (hS : kg_SymmC1 K) {ρ : ℝ}
    (hb : ∀ s ∈ ball t₁ ρ, ((s - t₁, 0) : ℝ × K.H) ∈ K.Φ.source ∧ γ s = kl_psi K (s - t₁, 0))
    {t t' : ℝ} (ht : t ∈ ball t₁ ρ) (ht' : t' ∈ ball t₁ ρ) : kg_Related g γ t t' := by
  have hadd : ∀ s : ℝ, ((s - t₁, 0) : ℝ × K.H) + ((t' - t, 0) : ℝ × K.H) =
      ((s + t' - t - t₁, 0) : ℝ × K.H) := fun s => by ext <;> simp; ring
  have hq := (hb t ht).1
  have hU : γ t ∈ kg_U K (t' - t) := by
    rw [(hb t ht).2]
    refine kg_psi_mem_U K hq _ ?_
    rw [hadd]; convert (hb t' ht').1 using 3; ring
  refine ⟨kg_U K (t' - t), kg_shift K (t' - t), kg_U_open K hS _, hU, ?_,
    fun x hx => kg_shift_mdiff K hS _ hx, fun x hx v w => kg_shift_isometry K hS _ hx v w, ?_⟩
  · rw [(hb t ht).2, kg_shift_psi K hq, hadd, (hb t' ht').2]
    congr 2; ring
  · have hT : Tendsto (fun s : ℝ => s + t' - t) (𝓝 t) (𝓝 t') :=
      ((continuous_id.add continuous_const).sub continuous_const).tendsto' t t' (by simp)
    filter_upwards [isOpen_ball.mem_nhds ht, hT.eventually (isOpen_ball.mem_nhds ht')] with s hs hs'
    rw [(hb s hs).2, kg_shift_psi K (hb s hs).1, hadd, (hb _ hs').2]

/-- **|X|² is constant in one box window** (`kl_normSq_orbit_const`). -/
theorem kg_normSq_box {X : Π x : N, TangentSpace 𝓘(ℝ, E) x} {t₁ : ℝ}
    (K : LocalKillingChart X (γ t₁) (hRep g (γ t₁))) {ρ : ℝ}
    (hb : ∀ s ∈ ball t₁ ρ, ((s - t₁, 0) : ℝ × K.H) ∈ K.Φ.source ∧ γ s = kl_psi K (s - t₁, 0))
    {t t' : ℝ} (ht : t ∈ ball t₁ ρ) (ht' : t' ∈ ball t₁ ρ) :
    kl_normSq g X (γ t) = kl_normSq g X (γ t') := by
  rw [(hb t ht).2, (hb t' ht').2]
  exact kl_normSq_orbit_const K _ _ (hb t ht).1 (hb t' ht').1 rfl

end KGGenerator

section KGHeadline

open Manifold

variable {N : Type*} [TopologicalSpace N] [ChartedSpace E N] [IsManifold 𝓘(ℝ, E) 1 N]

/-- The adapted lapse along `X`: `n = |X| = √(max 0 (−g(X, X)))` (campaign 94 ①'s `σ.n` on the Rindler
horizon). -/
noncomputable def kg_lapse (g : Π x : N, TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x →L[ℝ] ℝ)
    (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (x : N) : ℝ :=
  √(max 0 (-(g x (X x) (X x))))

/-- `Δτ = ∫ₐᵇ n |dλ(γ′)| dt` along `γ`; in the adapted frame `γ′ = X = ∂_λ`, so `dλ(γ′) = 1`. -/
noncomputable def kg_deltaTau
    (g : Π x : N, TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x →L[ℝ] ℝ)
    (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (γ : ℝ → N) (a b : ℝ) : ℝ :=
  ∫ t in a..b, kg_lapse g X (γ t) * |(1 : ℝ)|

theorem kg_lapse_null {g : Π x : N, TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x →L[ℝ] ℝ}
    {X : Π x : N, TangentSpace 𝓘(ℝ, E) x} {x : N} (h : g x (X x) (X x) = 0) : kg_lapse g X x = 0 := by
  simp [kg_lapse, h]

/-- **(d) `Δτ = 0`** when `X` is null along `γ` on `[a, b]`. -/
theorem kg_deltaTau_zero {g : Π x : N, TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x →L[ℝ] ℝ}
    {X : Π x : N, TangentSpace 𝓘(ℝ, E) x} {γ : ℝ → N} {a b : ℝ} (hab : a ≤ b)
    (h : ∀ t ∈ Icc a b, g (γ t) (X (γ t)) (X (γ t)) = 0) : kg_deltaTau g X γ a b = 0 := by
  unfold kg_deltaTau
  rw [intervalIntegral.integral_congr (g := fun _ => (0 : ℝ)) fun t ht => by
    rw [uIcc_of_le hab] at ht
    simp only [kg_lapse_null (h t ht), zero_mul]]
  simp

variable [IsManifold 𝓘(ℝ, E) 2 N]

/-- **`lem:killing` stage 2, `kg_lemma_killing_generator`.** `N` a `C²` manifold modelled on `E`
(boundaryless), `X` `C¹` along `γ` as a section with `X ≠ 0` along `γ` (away from a bifurcation surface),
`hRep g (γ t)` differentiable near `φ (γ t)`, `L_X g = 0` on a neighbourhood of `γ([a, b])`, `γ` an integral
curve of `X` at every `t ∈ [a, b]`, and `g(X, X) = 0` at one `γ t₀`. Then:
* the registered velocity form: `mfderiv γ t 1 = X (γ t)` on `[a, b]`;
* **(a)** `g(X, X) = 0` and `ds² = g(γ′, γ′) = 0` at every `γ t`, `t ∈ [a, b]`;
* **(b)** every two parameters `t₁, t₂ ∈ [a, b]` are related by a local isometry `F` on an open `U ∋ γ t₁`
  with `F (γ t₁) = γ t₂` and `F (γ s) = γ (s + t₂ − t₁)` near `t₁` (`kg_Related`);
* **(c)** if `γ` is injective on `[a, b]`, distinct parameters give distinct events;
* **(d)** `Δτ = ∫ₐᵇ n |dλ(γ′)| = 0` for the adapted lapse `n = |X|`. -/
theorem kg_lemma_killing_generator (X : Π x : N, TangentSpace 𝓘(ℝ, E) x)
    (g : Π x : N, TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x →L[ℝ] ℝ)
    (γ : ℝ → N) (a b t₀ : ℝ) (hab : a ≤ b)
    (hX : ∀ t ∈ Icc a b, ContMDiffAt 𝓘(ℝ, E) 𝓘(ℝ, E).tangent 1
      (fun x ↦ (⟨x, X x⟩ : TangentBundle 𝓘(ℝ, E) N)) (γ t))
    (hXne : ∀ t ∈ Icc a b, X (γ t) ≠ 0)
    (hg : ∀ t ∈ Icc a b,
      ∀ᶠ y in 𝓝 (extChartAt 𝓘(ℝ, E) (γ t) (γ t)), DifferentiableAt ℝ (hRep g (γ t)) y)
    (hK : ∀ t ∈ Icc a b, ∀ᶠ x in 𝓝 (γ t), ∀ v w, lieDeriv X g x v w = 0)
    (hγ : ∀ t ∈ Icc a b, IsMIntegralCurveAt γ X t)
    (ht₀ : t₀ ∈ Icc a b) (hnull : g (γ t₀) (X (γ t₀)) (X (γ t₀)) = 0) :
    (∀ t ∈ Icc a b, mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ t (1 : ℝ) = X (γ t)) ∧
    (∀ t ∈ Icc a b, g (γ t) (X (γ t)) (X (γ t)) = 0 ∧
      g (γ t) (mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ t (1 : ℝ)) (mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ t (1 : ℝ)) = 0) ∧
    (∀ t₁ ∈ Icc a b, ∀ t₂ ∈ Icc a b, kg_Related g γ t₁ t₂) ∧
    (InjOn γ (Icc a b) → ∀ t₁ ∈ Icc a b, ∀ t₂ ∈ Icc a b, t₁ ≠ t₂ → γ t₁ ≠ γ t₂) ∧
    kg_deltaTau g X γ a b = 0 := by
  have hvel : ∀ t ∈ Icc a b, mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ t (1 : ℝ) = X (γ t) := fun t ht => by
    rw [(hγ t ht).hasMFDerivAt.mfderiv]
    show (1 : ℝ) • X (γ t) = X (γ t)
    exact one_smul ℝ _
  have hbox := fun t (ht : t ∈ Icc a b) => kg_box_along X t (hX t ht) (hXne t ht) (hg t ht) (hK t ht)
    (hγ t ht)
  have hloc : ∀ x ∈ Icc a b, ∃ ρ > 0, ∀ y ∈ ball x ρ, ∀ y' ∈ ball x ρ,
      kg_Related g γ y y' ∧ kl_normSq g X (γ y) = kl_normSq g X (γ y') := by
    intro x hx
    obtain ⟨K, hS, ρ, hρ, hb⟩ := hbox x hx
    exact ⟨ρ, hρ, fun y hy y' hy' => ⟨kg_related_box K hS hb hy hy', kg_normSq_box K hb hy hy'⟩⟩
  have hev : ∀ x ∈ Icc a b, ∀ᶠ y in 𝓝[Icc a b] x,
      (kg_Related g γ x y ∧ kl_normSq g X (γ x) = kl_normSq g X (γ y)) ∧
      (kg_Related g γ y x ∧ kl_normSq g X (γ y) = kl_normSq g X (γ x)) := by
    intro x hx
    obtain ⟨ρ, hρ, h⟩ := hloc x hx
    have hxb : x ∈ ball x ρ := mem_ball_self hρ
    filter_upwards [nhdsWithin_le_nhds (ball_mem_nhds x hρ)] with y hy
    exact ⟨h x hxb y hy, h y hy x hxb⟩
  have hall := fun t₁ (h₁ : t₁ ∈ Icc a b) t₂ (h₂ : t₂ ∈ Icc a b) =>
    isPreconnected_Icc.induction₂'
      (fun x y => kg_Related g γ x y ∧ kl_normSq g X (γ x) = kl_normSq g X (γ y)) hev
      (fun x y z _ _ _ hxy hyz => ⟨kg_related_trans hxy.1 hyz.1, hxy.2.trans hyz.2⟩) h₁ h₂
  have hA : ∀ t ∈ Icc a b, g (γ t) (X (γ t)) (X (γ t)) = 0 := fun t ht =>
    ((hall t ht t₀ ht₀).2.trans hnull)
  refine ⟨hvel, fun t ht => ⟨hA t ht, ?_⟩, fun t₁ h₁ t₂ h₂ => (hall t₁ h₁ t₂ h₂).1,
    fun hinj t₁ h₁ t₂ h₂ hne heq => hne (hinj h₁ h₂ heq), kg_deltaTau_zero hab hA⟩
  have e := hvel t ht
  exact (congrArg₂ (fun u v : E => g (γ t) u v) e e).trans (hA t ht)

end KGHeadline

section KGWitness

open Manifold ContinuousLinearMap

set_option synthInstance.maxHeartbeats 400000

/-- `g = −dU dV` (symmetrised), campaign 94 ①'s `gM`: `g(v, w) = −(v₁ w₂ + v₂ w₁)/2` on `(U, V)`. -/
noncomputable def kg_w_B : (ℝ × ℝ) →L[ℝ] (ℝ × ℝ) →L[ℝ] ℝ :=
  (-(1/2 : ℝ)) • ((fst ℝ ℝ ℝ).smulRight (snd ℝ ℝ ℝ) + (snd ℝ ℝ ℝ).smulRight (fst ℝ ℝ ℝ))

theorem kg_w_B_apply (v w : ℝ × ℝ) : kg_w_B v w = -(v.1 * w.2 + v.2 * w.1) / 2 := by
  simp [kg_w_B]; ring

/-- `−dU dV` is Lorentzian: symmetric, nondegenerate, with a timelike `(1, 1)` and a spacelike `(1, −1)`. -/
theorem kg_w_lorentzian :
    (∀ v w : ℝ × ℝ, kg_w_B v w = kg_w_B w v) ∧
    (∀ v : ℝ × ℝ, (∀ w, kg_w_B v w = 0) → v = 0) ∧
    kg_w_B (1, 1) (1, 1) < 0 ∧ 0 < kg_w_B (1, -1) (1, -1) := by
  refine ⟨fun v w => by simp only [kg_w_B_apply]; ring, fun v hv => ?_, ?_, ?_⟩
  · have h1 := hv (1, 0); have h2 := hv (0, 1)
    simp only [kg_w_B_apply] at h1 h2
    ext <;> simp <;> linarith
  · rw [kg_w_B_apply]; norm_num
  · rw [kg_w_B_apply]; norm_num

/-- The metric field on `N = ℝ × ℝ` (null coordinates `(U, V)`). -/
noncomputable def kg_w_g :
    Π x : ℝ × ℝ, TangentSpace 𝓘(ℝ, ℝ × ℝ) x →L[ℝ] TangentSpace 𝓘(ℝ, ℝ × ℝ) x →L[ℝ] ℝ :=
  fun _ => kg_w_B

/-- The boost `χ = V∂_V − U∂_U` as a linear map `(U, V) ↦ (−U, V)`. -/
noncomputable def kg_w_L : (ℝ × ℝ) →L[ℝ] (ℝ × ℝ) := (-(fst ℝ ℝ ℝ)).prod (snd ℝ ℝ ℝ)

theorem kg_w_L_apply (x : ℝ × ℝ) : kg_w_L x = (-x.1, x.2) := by simp [kg_w_L]

/-- The boost field `χ`. -/
noncomputable def kg_w_X : Π x : ℝ × ℝ, TangentSpace 𝓘(ℝ, ℝ × ℝ) x := fun x => kg_w_L x

/-- `g(χ, χ) = UV`: null exactly on the horizon `UV = 0`. -/
theorem kg_w_normSq (x : ℝ × ℝ) : kg_w_g x (kg_w_X x) (kg_w_X x) = x.1 * x.2 := by
  show kg_w_B (kg_w_L x) (kg_w_L x) = _
  rw [kg_w_B_apply, kg_w_L_apply]; ring

/-- The boost flow `Φ_t(U, V) = (e^{−t}U, e^{t}V)` (campaign 94 ①). -/
noncomputable def kg_w_Φ (t : ℝ) (x : ℝ × ℝ) : ℝ × ℝ := (Real.exp (-t) * x.1, Real.exp t * x.2)

/-- `χ` generates the boost (copy of `ac_boost_generator`). -/
theorem kg_w_boost_generator (x : ℝ × ℝ) : HasDerivAt (fun t => kg_w_Φ t x) (kg_w_X x) 0 := by
  have h1 : HasDerivAt (fun t => Real.exp (-t) * x.1) (-x.1) 0 := by
    have := ((Real.hasDerivAt_exp (-0)).comp 0 (hasDerivAt_neg 0)).mul_const x.1
    simpa using this
  have h2 : HasDerivAt (fun t => Real.exp t * x.2) x.2 0 := by
    simpa using (Real.hasDerivAt_exp 0).mul_const x.2
  have h := h1.prodMk h2
  show HasDerivAt _ (kg_w_L x) 0
  rw [kg_w_L_apply]; exact h

/-- The boost preserves `g` (copy of `ac_boost_isometry`). -/
theorem kg_w_boost_isometry (t : ℝ) (a b : ℝ × ℝ) : kg_w_B (kg_w_Φ t a) (kg_w_Φ t b) = kg_w_B a b := by
  rw [kg_w_B_apply, kg_w_B_apply]
  simp only [kg_w_Φ]
  have he : Real.exp (-t) * Real.exp t = 1 := by rw [← Real.exp_add]; simp
  linear_combination (-(a.1 * b.2 + a.2 * b.1) / 2) * he

/-- The Rindler horizon generator `γ s = (0, eˢ)` on `U = 0`, `V > 0`. -/
noncomputable def kg_w_γ (s : ℝ) : ℝ × ℝ := (0, Real.exp s)

theorem kg_w_hRep (p : ℝ × ℝ) : hRep kg_w_g p = fun _ => kg_w_B := by
  funext y
  show kg_w_B.bilinearComp _ _ = kg_w_B
  rw [kl_w_mfderiv_chart_symm]
  exact ContinuousLinearMap.ext fun v => ContinuousLinearMap.ext fun w => rfl

theorem kg_w_chartRep (p : ℝ × ℝ) : chartRep kg_w_X p = ⇑kg_w_L := by
  funext y
  show mfderiv 𝓘(ℝ, ℝ × ℝ) 𝓘(ℝ, ℝ × ℝ) (extChartAt 𝓘(ℝ, ℝ × ℝ) p) _
    (kg_w_L ((extChartAt 𝓘(ℝ, ℝ × ℝ) p).symm y)) = _
  rw [kl_w_mfderiv_chart, extChartAt_model_space_eq_id]
  rfl

/-- The chart Killing expression vanishes: `g(χ a, b) + g(a, χ b) = 0` for the boost. -/
theorem kg_w_chartLie (z a b : ℝ × ℝ) : chartLie (fun _ => kg_w_B) ⇑kg_w_L z a b = 0 := by
  unfold chartLie
  rw [fderiv_const_apply, ContinuousLinearMap.fderiv]
  simp only [_root_.zero_apply, zero_add]
  rw [kg_w_B_apply, kg_w_B_apply, kg_w_L_apply, kg_w_L_apply]
  ring

/-- **`χ` is Killing:** `L_χ g = 0` everywhere, through the registered `lieDeriv`. -/
theorem kg_w_lieDeriv (x v w : ℝ × ℝ) : lieDeriv kg_w_X kg_w_g x v w = 0 := by
  rw [ld_lieDeriv_chart_self kg_w_X kg_w_g x v w
    (by rw [kg_w_hRep]; exact differentiableAt_const _)]
  rw [kg_w_hRep, kg_w_chartRep]
  exact kg_w_chartLie _ _ _

theorem kg_w_hX (p : ℝ × ℝ) : ContMDiffAt 𝓘(ℝ, ℝ × ℝ) 𝓘(ℝ, ℝ × ℝ).tangent 1
    (fun x ↦ (⟨x, kg_w_X x⟩ : TangentBundle 𝓘(ℝ, ℝ × ℝ) (ℝ × ℝ))) p :=
  (contMDiffAt_vectorSpace_iff_contDiffAt (V := kg_w_X)).2 kg_w_L.contDiff.contDiffAt

theorem kg_w_X_γ (s : ℝ) : kg_w_X (kg_w_γ s) = ((0 : ℝ), Real.exp s) := by
  show kg_w_L _ = _
  rw [kg_w_L_apply]; simp [kg_w_γ]

theorem kg_w_hXne (s : ℝ) : kg_w_X (kg_w_γ s) ≠ 0 := by
  rw [kg_w_X_γ]
  intro h
  have := congrArg Prod.snd h
  simp only at this
  exact (Real.exp_pos s).ne' this

/-- `γ` is an integral curve of `χ` (everywhere). -/
theorem kg_w_integral (t : ℝ) : IsMIntegralCurveAt kg_w_γ kg_w_X t := by
  refine Filter.Eventually.of_forall fun s => ?_
  have hd : HasDerivAt kg_w_γ ((0 : ℝ), Real.exp s) s :=
    (hasDerivAt_const s (0:ℝ)).prodMk (Real.hasDerivAt_exp s)
  have h := hd.hasFDerivAt.hasMFDerivAt
  rw [kg_w_X_γ]
  exact h

theorem kg_w_null : kg_w_g (kg_w_γ 0) (kg_w_X (kg_w_γ 0)) (kg_w_X (kg_w_γ 0)) = 0 := by
  rw [kg_w_normSq]; simp [kg_w_γ]

theorem kg_w_injOn : InjOn kg_w_γ (Icc 0 10) := fun _ _ _ _ h =>
  Real.exp_injective (congrArg Prod.snd h)

/-- **`kg_witness`.** On the Rindler horizon (`N = ℝ × ℝ`, `g = −dU dV`, Killing boost
`χ = V∂_V − U∂_U`, generator `γ s = (0, eˢ)`, `s ∈ [0, 10]`), every hypothesis of
`kg_lemma_killing_generator` is discharged, and its conclusions give: `γ 0 = (0, 1)` and
`γ 10 = (0, e¹⁰)` are **distinct**, `χ` is null at both, and they are related by a local isometry carrying
the generator into itself (`kg_Related` at `t₁ = 0`, `t₂ = 10`), with `Δτ = 0` along the generator. -/
theorem kg_witness :
    (∀ x : ℝ × ℝ, kg_w_g x (kg_w_X x) (kg_w_X x) = x.1 * x.2) ∧
    (∀ x v w : ℝ × ℝ, lieDeriv kg_w_X kg_w_g x v w = 0) ∧
    (∀ t ∈ Icc (0 : ℝ) 10, kg_w_X (kg_w_γ t) ≠ 0) ∧
    kg_w_γ 0 = ((0 : ℝ), (1 : ℝ)) ∧ kg_w_γ 10 = ((0 : ℝ), Real.exp 10) ∧
    kg_w_γ 0 ≠ kg_w_γ 10 ∧
    kg_w_g (kg_w_γ 0) (kg_w_X (kg_w_γ 0)) (kg_w_X (kg_w_γ 0)) = 0 ∧
    kg_w_g (kg_w_γ 10) (kg_w_X (kg_w_γ 10)) (kg_w_X (kg_w_γ 10)) = 0 ∧
    kg_Related kg_w_g kg_w_γ 0 10 ∧ kg_Related kg_w_g kg_w_γ 10 0 ∧
    kg_deltaTau kg_w_g kg_w_X kg_w_γ 0 10 = 0 := by
  have hI : (0 : ℝ) ∈ Icc (0 : ℝ) 10 := ⟨le_rfl, by norm_num⟩
  have hI' : (10 : ℝ) ∈ Icc (0 : ℝ) 10 := ⟨by norm_num, le_rfl⟩
  obtain ⟨-, hA, hB, hC, hD⟩ := kg_lemma_killing_generator kg_w_X kg_w_g kg_w_γ 0 10 0 (by norm_num)
    (fun t _ => kg_w_hX _) (fun t _ => kg_w_hXne t)
    (fun t _ => Filter.Eventually.of_forall fun y => by rw [kg_w_hRep]; exact differentiableAt_const _)
    (fun t _ => Filter.Eventually.of_forall fun x v w => kg_w_lieDeriv x v w)
    (fun t _ => kg_w_integral t) hI kg_w_null
  have h0 : kg_w_γ 0 = ((0 : ℝ), (1 : ℝ)) := by simp [kg_w_γ]
  refine ⟨kg_w_normSq, kg_w_lieDeriv, fun t _ => kg_w_hXne t, h0, rfl,
    hC kg_w_injOn 0 hI 10 hI' (by norm_num), (hA 0 hI).1, (hA 10 hI').1, hB 0 hI 10 hI',
    hB 10 hI' 0 hI, hD⟩

end KGWitness

section KWSplitting

open Manifold ContinuousLinearMap

variable {N : Type*} [TopologicalSpace N] [ChartedSpace E N]

/-- **`dλ` exists.** In finite dimension, every non-zero `v : E` has a continuous linear form `φ` with
`φ v = 1` (Hahn–Banach, `exists_dual_vector`, rescaled by `1 / ‖v‖`). -/
theorem «kw_dλ_exists» (v : E) (hv : v ≠ 0) : ∃ φ : E →L[ℝ] ℝ, φ v = 1 := by
  obtain ⟨φ, hφ⟩ : ∃ φ : Module.Dual ℝ E, φ v ≠ 0 := by
    by_contra hc
    push Not at hc
    exact hv ((Module.forall_dual_apply_eq_zero_iff ℝ v).mp hc)
  refine ⟨(φ v)⁻¹ • LinearMap.toContinuousLinearMap φ, ?_⟩
  rw [smul_apply, LinearMap.coe_toContinuousLinearMap', smul_eq_mul]
  exact inv_mul_cancel₀ hφ

/-- `g_x` read as a bilinear form on `E` (campaign 94 ①'s `gE`, for a raw section `g`). -/
def kw_gE (g : Π x : N, TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x →L[ℝ] ℝ) (x : N) :
    E →L[ℝ] E →L[ℝ] ℝ := g x

/-- The velocity `γ′(t) = mfderiv γ t 1` (campaign 94 ①'s `vel`). -/
noncomputable def kw_vel (γ : ℝ → N) (t : ℝ) : E := mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ t (1 : ℝ)

/-- **Campaign 94 ①'s `AdaptedSplitting`, restated for a raw `g` on `[a, b]`.** A spatial form `h s`, a
lapse `n s ≥ 0` (allowed to vanish), a temporal one-form `dt s`, with
`g_{γ s} = h s − (n s)² dt s ⊗ dt s` and `h s (γ′ s, γ′ s) ≥ 0` on `[a, b]`. -/
structure kw_AdaptedSplitting
    (g : Π x : N, TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x →L[ℝ] ℝ)
    (γ : ℝ → N) (a b : ℝ) where
  h : ℝ → E →L[ℝ] E →L[ℝ] ℝ
  n : ℝ → ℝ
  dt : ℝ → E →L[ℝ] ℝ
  n_nonneg : ∀ s ∈ Icc a b, 0 ≤ n s
  split : ∀ s ∈ Icc a b, kw_gE g (γ s) = h s - (n s) ^ 2 • (dt s).smulRight (dt s)
  h_nonneg : ∀ s ∈ Icc a b, 0 ≤ h s (kw_vel γ s) (kw_vel γ s)

namespace kw_AdaptedSplitting

variable {g : Π x : N, TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x →L[ℝ] ℝ}
  {γ : ℝ → N} {a b : ℝ} (σ : kw_AdaptedSplitting g γ a b)

/-- `Δx := ∫ₐᵇ √(h(γ′, γ′))`. -/
noncomputable def Δx : ℝ := ∫ s in a..b, √(σ.h s (kw_vel γ s) (kw_vel γ s))

/-- `Δτ := ∫ₐᵇ n |dt(γ′)|`. -/
noncomputable def Δτ : ℝ := ∫ s in a..b, σ.n s * |σ.dt s (kw_vel γ s)|

/-- `g(γ′, γ′) = h(γ′, γ′) − n² dt(γ′)²` on `[a, b]`. -/
theorem kw_g_vel {s : ℝ} (hs : s ∈ Icc a b) :
    kw_gE g (γ s) (kw_vel γ s) (kw_vel γ s) =
      σ.h s (kw_vel γ s) (kw_vel γ s) - (σ.n s * σ.dt s (kw_vel γ s)) ^ 2 := by
  rw [σ.split s hs]
  simp only [sub_apply, smul_apply, ContinuousLinearMap.smulRight_apply, smul_eq_mul]
  ring

end kw_AdaptedSplitting

/-- Campaign 94 ①'s integral-zero lemma on `[a, b]`, `a < b`: continuous, non-negative, zero integral
⟹ zero on `[a, b]`. -/
theorem kw_eq_zero_of_integral_eq_zero {f : ℝ → ℝ} {a b : ℝ} (hab : a < b)
    (hc : ContinuousOn f (Icc a b)) (hnn : ∀ s ∈ Icc a b, 0 ≤ f s) (h0 : ∫ s in a..b, f s = 0) :
    ∀ s ∈ Icc a b, f s = 0 := by
  intro s hs
  by_contra hne
  have hpos : 0 < ∫ s in a..b, f s :=
    intervalIntegral.integral_pos hab hc (fun x hx => hnn x (Ioc_subset_Icc_self hx))
      ⟨s, hs, lt_of_le_of_ne (hnn s hs) (Ne.symm hne)⟩
  linarith

/-- **Campaign 94 ①'s `ac_metric_singularity_along`, on `[a, b]` for a raw `g`.** (a) `g(γ′, γ′) = 0`,
(b) `Δx = 0`, and continuity of `h(γ′, γ′)` give `Δτ = 0`, `n · dt(γ′) = 0` and `h(γ′, γ′) = 0`
on `[a, b]`. -/
theorem kw_metric_singularity_along
    {g : Π x : N, TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x →L[ℝ] ℝ}
    {γ : ℝ → N} {a b : ℝ} (hab : a < b) (σ : kw_AdaptedSplitting g γ a b)
    (ha : ∀ s ∈ Icc a b, kw_gE g (γ s) (kw_vel γ s) (kw_vel γ s) = 0)
    (hb : σ.Δx = 0)
    (hcont : ContinuousOn (fun s => σ.h s (kw_vel γ s) (kw_vel γ s)) (Icc a b)) :
    σ.Δτ = 0 ∧ (∀ s ∈ Icc a b, σ.n s * σ.dt s (kw_vel γ s) = 0) ∧
      (∀ s ∈ Icc a b, σ.h s (kw_vel γ s) (kw_vel γ s) = 0) := by
  have hsq : ∀ s ∈ Icc a b, √(σ.h s (kw_vel γ s) (kw_vel γ s)) = 0 :=
    kw_eq_zero_of_integral_eq_zero hab (Real.continuous_sqrt.comp_continuousOn hcont)
      (fun s _ => Real.sqrt_nonneg _) hb
  have hh : ∀ s ∈ Icc a b, σ.h s (kw_vel γ s) (kw_vel γ s) = 0 := fun s hs =>
    le_antisymm (Real.sqrt_eq_zero'.mp (hsq s hs)) (σ.h_nonneg s hs)
  have hnd : ∀ s ∈ Icc a b, σ.n s * σ.dt s (kw_vel γ s) = 0 := by
    intro s hs
    have h1 := σ.kw_g_vel hs
    rw [ha s hs, hh s hs] at h1
    have : (σ.n s * σ.dt s (kw_vel γ s)) ^ 2 = 0 := by linarith
    exact pow_eq_zero_iff two_ne_zero |>.mp this
  refine ⟨?_, hnd, hh⟩
  unfold kw_AdaptedSplitting.Δτ
  rw [intervalIntegral.integral_congr (g := fun _ => (0 : ℝ)) fun s hs => by
    rw [uIcc_of_le hab.le] at hs
    have h2 := hnd s hs
    show σ.n s * |σ.dt s (kw_vel γ s)| = 0
    rw [← abs_of_nonneg (σ.n_nonneg s hs), ← abs_mul, h2, abs_zero]]
  simp

/-! ### The horizon's own splitting along `γ` (ruling 2: adapted time `λ`, lapse `|χ|`) -/

/-- The lapse `n s = √(max 0 (−g(X, X)))` at `γ s` (`= kg_lapse g X (γ s)`). -/
noncomputable def kw_n (g : Π x : N, TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x →L[ℝ] ℝ)
    (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (γ : ℝ → N) (s : ℝ) : ℝ :=
  √(max 0 (-(g (γ s) (X (γ s)) (X (γ s)))))

/-- `dλ` at `γ s`: a chosen linear form with `dt s (X (γ s)) = 1` (`0` where `X (γ s) = 0`). -/
noncomputable def kw_dt (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (γ : ℝ → N) (s : ℝ) : E →L[ℝ] ℝ :=
  open Classical in
  if hX : (@id E (X (γ s))) = 0 then 0 else Classical.choose («kw_dλ_exists» (@id E (X (γ s))) hX)

/-- `h s = g_{γ s} + n² dt ⊗ dt`. -/
noncomputable def kw_h (g : Π x : N, TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x →L[ℝ] ℝ)
    (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (γ : ℝ → N) (s : ℝ) : E →L[ℝ] E →L[ℝ] ℝ :=
  kw_gE g (γ s) + (kw_n g X γ s) ^ 2 • (kw_dt X γ s).smulRight (kw_dt X γ s)

theorem kw_dt_X {X : Π x : N, TangentSpace 𝓘(ℝ, E) x} {γ : ℝ → N} {s : ℝ} (hX : (@id E (X (γ s))) ≠ 0) :
    kw_dt X γ s (@id E (X (γ s))) = 1 := by
  unfold kw_dt
  simp only [hX, ↓reduceDIte]
  exact Classical.choose_spec («kw_dλ_exists» (@id E (X (γ s))) hX)

/-- `g = h − n² dt ⊗ dt` (everywhere). -/
theorem kw_split (g : Π x : N, TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x →L[ℝ] ℝ)
    (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (γ : ℝ → N) (s : ℝ) :
    kw_gE g (γ s) = kw_h g X γ s - (kw_n g X γ s) ^ 2 • (kw_dt X γ s).smulRight (kw_dt X γ s) := by
  unfold kw_h; abel

/-- `h(X, X) = max(g(X, X), 0) ≥ 0` at `γ s` when `X (γ s) ≠ 0`. -/
theorem kw_h_X {g : Π x : N, TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x →L[ℝ] ℝ}
    {X : Π x : N, TangentSpace 𝓘(ℝ, E) x} {γ : ℝ → N} {s : ℝ} (hX : (@id E (X (γ s))) ≠ 0) :
    kw_h g X γ s (X (γ s)) (X (γ s)) = max (g (γ s) (X (γ s)) (X (γ s))) 0 := by
  have hd := kw_dt_X (γ := γ) hX
  have hn : (kw_n g X γ s) ^ 2 = max 0 (-(g (γ s) (X (γ s)) (X (γ s)))) :=
    Real.sq_sqrt (le_max_left _ _)
  have key : ∀ r : ℝ, r + max 0 (-r) = max r 0 := fun r => by
    rcases le_total 0 r with h | h
    · rw [max_eq_left (by linarith : -r ≤ 0), max_eq_left h]; ring
    · rw [max_eq_right (by linarith : 0 ≤ -r), max_eq_right h]; ring
  rw [← key, ← hn]
  change g (γ s) (X (γ s)) (X (γ s)) +
    kw_n g X γ s ^ 2 * (kw_dt X γ s (@id E (X (γ s))) * kw_dt X γ s (@id E (X (γ s)))) = _
  rw [hd]; ring

/-- **The horizon splitting along `γ` on `[a, b]`** (`n = |X|`, `dt = dλ`, `h = g + n² dλ²`), for `γ′ = X`
and `X ≠ 0` along `γ`. -/
noncomputable def kw_horizonSplitting
    (g : Π x : N, TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x →L[ℝ] ℝ)
    (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (γ : ℝ → N) (a b : ℝ)
    (hvel : ∀ s ∈ Icc a b, (kw_vel γ s : E) = X (γ s)) (hXne : ∀ s ∈ Icc a b, (@id E (X (γ s))) ≠ 0) :
    kw_AdaptedSplitting g γ a b where
  h := kw_h g X γ
  n := kw_n g X γ
  dt := kw_dt X γ
  n_nonneg := fun _ _ => Real.sqrt_nonneg _
  split := fun s _ => kw_split g X γ s
  h_nonneg := fun s hs => by
    show 0 ≤ kw_h g X γ s (kw_vel γ s) (kw_vel γ s)
    rw [hvel s hs, kw_h_X (hXne s hs)]
    exact le_max_right _ _

/-- The registered velocity form from integral curves (as in `kg_lemma_killing_generator`). -/
theorem kw_vel_eq [IsManifold 𝓘(ℝ, E) 1 N] {X : Π x : N, TangentSpace 𝓘(ℝ, E) x} {γ : ℝ → N}
    {a b : ℝ} (hγ : ∀ t ∈ Icc a b, IsMIntegralCurveAt γ X t) :
    ∀ t ∈ Icc a b, (kw_vel γ t : E) = X (γ t) := fun t ht => by
  unfold kw_vel
  rw [(hγ t ht).hasMFDerivAt.mfderiv]
  show (1 : ℝ) • X (γ t) = X (γ t)
  exact one_smul ℝ _

end KWSplitting

section KWHeadline

open Manifold ContinuousLinearMap

variable {N : Type*} [TopologicalSpace N] [ChartedSpace E N] [IsManifold 𝓘(ℝ, E) 2 N]

set_option synthInstance.maxHeartbeats 400000

/-- **`lem:killing` 4d whole, `kw_lemma_killing_whole`.** Under `kg_lemma_killing_generator`'s hypotheses:
stage 2's velocity form, (a), (b), (c) and `Δτ = 0`; and for the horizon splitting `σ`
(`n = |X|`, `dt = dλ` with `dλ(X) = 1`, `h = g + n² dλ²`) along `γ` on the **whole** of `[a, b]`:
`h s = g_{γ s}` and `h(γ′, γ′) = 0` there, `Δx = ∫ₐᵇ √h(γ′, γ′) = 0`, and
`Δτ = ∫ₐᵇ n |dt(γ′)| = 0` (via `kw_metric_singularity_along` when `a < b`). -/
theorem kw_lemma_killing_whole (X : Π x : N, TangentSpace 𝓘(ℝ, E) x)
    (g : Π x : N, TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x →L[ℝ] ℝ)
    (γ : ℝ → N) (a b t₀ : ℝ) (hab : a ≤ b)
    (hX : ∀ t ∈ Icc a b, ContMDiffAt 𝓘(ℝ, E) 𝓘(ℝ, E).tangent 1
      (fun x ↦ (⟨x, X x⟩ : TangentBundle 𝓘(ℝ, E) N)) (γ t))
    (hXne : ∀ t ∈ Icc a b, X (γ t) ≠ 0)
    (hg : ∀ t ∈ Icc a b,
      ∀ᶠ y in 𝓝 (extChartAt 𝓘(ℝ, E) (γ t) (γ t)), DifferentiableAt ℝ (hRep g (γ t)) y)
    (hK : ∀ t ∈ Icc a b, ∀ᶠ x in 𝓝 (γ t), ∀ v w, lieDeriv X g x v w = 0)
    (hγ : ∀ t ∈ Icc a b, IsMIntegralCurveAt γ X t)
    (ht₀ : t₀ ∈ Icc a b) (hnull : g (γ t₀) (X (γ t₀)) (X (γ t₀)) = 0) :
    (∀ t ∈ Icc a b, mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ t (1 : ℝ) = X (γ t)) ∧
    (∀ t ∈ Icc a b, g (γ t) (X (γ t)) (X (γ t)) = 0 ∧
      g (γ t) (mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ t (1 : ℝ)) (mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ t (1 : ℝ)) = 0) ∧
    (∀ t₁ ∈ Icc a b, ∀ t₂ ∈ Icc a b, kg_Related g γ t₁ t₂) ∧
    (InjOn γ (Icc a b) → ∀ t₁ ∈ Icc a b, ∀ t₂ ∈ Icc a b, t₁ ≠ t₂ → γ t₁ ≠ γ t₂) ∧
    kg_deltaTau g X γ a b = 0 ∧
    (∀ s ∈ Icc a b, (kw_horizonSplitting g X γ a b (kw_vel_eq hγ) hXne).h s = kw_gE g (γ s) ∧
      (kw_horizonSplitting g X γ a b (kw_vel_eq hγ) hXne).h s (kw_vel γ s) (kw_vel γ s) = 0) ∧
    (kw_horizonSplitting g X γ a b (kw_vel_eq hγ) hXne).Δx =
      ∫ s in a..b, √(kw_h g X γ s (kw_vel γ s) (kw_vel γ s)) ∧
    (kw_horizonSplitting g X γ a b (kw_vel_eq hγ) hXne).Δx = 0 ∧
    (kw_horizonSplitting g X γ a b (kw_vel_eq hγ) hXne).Δτ =
      ∫ s in a..b, kw_n g X γ s * |kw_dt X γ s (kw_vel γ s)| ∧
    (kw_horizonSplitting g X γ a b (kw_vel_eq hγ) hXne).Δτ = 0 := by
  obtain ⟨hvel, hA, hB, hC, hD⟩ :=
    kg_lemma_killing_generator X g γ a b t₀ hab hX hXne hg hK hγ ht₀ hnull
  set σ := kw_horizonSplitting g X γ a b (kw_vel_eq hγ) hXne with hσ
  have hn0 : ∀ s ∈ Icc a b, kw_n g X γ s = 0 := fun s hs => by
    simp [kw_n, (hA s hs).1]
  have hhg : ∀ s ∈ Icc a b, σ.h s = kw_gE g (γ s) := fun s hs => by
    show kw_gE g (γ s) + (kw_n g X γ s) ^ 2 • (kw_dt X γ s).smulRight (kw_dt X γ s) = _
    rw [hn0 s hs]
    ext v w
    change g (γ s) v w + (0:ℝ) ^ 2 * (kw_dt X γ s v * kw_dt X γ s w) = g (γ s) v w
    ring
  have hh0 : ∀ s ∈ Icc a b, σ.h s (kw_vel γ s) (kw_vel γ s) = 0 := fun s hs => by
    rw [hhg s hs]; exact (hA s hs).2
  have hΔx : σ.Δx = 0 := by
    unfold kw_AdaptedSplitting.Δx
    rw [intervalIntegral.integral_congr (g := fun _ => (0 : ℝ)) fun s hs => by
      rw [uIcc_of_le hab] at hs
      simp only [hh0 s hs, Real.sqrt_zero]]
    simp
  have hΔτ : σ.Δτ = 0 := by
    rcases hab.lt_or_eq with hlt | heq
    · refine (kw_metric_singularity_along hlt σ (fun s hs => (hA s hs).2) hΔx ?_).1
      exact continuousOn_const.congr fun s hs => hh0 s hs
    · subst heq; exact intervalIntegral.integral_same
  exact ⟨hvel, hA, hB, hC, hD, fun s hs => ⟨hhg s hs, hh0 s hs⟩, rfl, hΔx, rfl, hΔτ⟩

end KWHeadline

section KWWitness

open Manifold ContinuousLinearMap

set_option synthInstance.maxHeartbeats 400000

/-- **`kw_witness`.** On stage 2's Rindler generator (`g = −dU dV`, `χ = V∂_V − U∂_U`, `γ s = (0, eˢ)`,
`s ∈ [0, 10]`), the horizon splitting along the whole generator has `Δx = 0` and `Δτ = 0`, its
`dλ(γ′) = 1` integrates to `10` (the Killing parameter separates the endpoints), and
`γ 0 = (0, 1) ≠ (0, e¹⁰) = γ 10` are related both ways. -/
theorem kw_witness :
    ∃ σ : kw_AdaptedSplitting kg_w_g kg_w_γ 0 10,
      σ.n = kw_n kg_w_g kg_w_X kg_w_γ ∧ σ.dt = kw_dt kg_w_X kg_w_γ ∧
      σ.h = kw_h kg_w_g kg_w_X kg_w_γ ∧
      σ.Δx = 0 ∧ σ.Δτ = 0 ∧ (∫ s in (0:ℝ)..10, σ.dt s (kw_vel kg_w_γ s)) = 10 ∧
      kg_w_γ 0 = ((0 : ℝ), (1 : ℝ)) ∧ kg_w_γ 10 = ((0 : ℝ), Real.exp 10) ∧
      kg_w_γ 0 ≠ kg_w_γ 10 ∧
      kg_Related kg_w_g kg_w_γ 0 10 ∧ kg_Related kg_w_g kg_w_γ 10 0 := by
  have hI : (0 : ℝ) ∈ Icc (0 : ℝ) 10 := ⟨le_rfl, by norm_num⟩
  have hI' : (10 : ℝ) ∈ Icc (0 : ℝ) 10 := ⟨by norm_num, le_rfl⟩
  have hγ : ∀ t ∈ Icc (0 : ℝ) 10, IsMIntegralCurveAt kg_w_γ kg_w_X t := fun t _ => kg_w_integral t
  have hXne : ∀ t ∈ Icc (0 : ℝ) 10, kg_w_X (kg_w_γ t) ≠ 0 := fun t _ => kg_w_hXne t
  obtain ⟨-, -, hB, hC, -, -, -, hΔx, -, hΔτ⟩ :=
    kw_lemma_killing_whole kg_w_X kg_w_g kg_w_γ 0 10 0 (by norm_num)
    (fun t _ => kg_w_hX _) hXne
    (fun t _ => Filter.Eventually.of_forall fun y => by rw [kg_w_hRep]; exact differentiableAt_const _)
    (fun t _ => Filter.Eventually.of_forall fun x v w => kg_w_lieDeriv x v w)
    hγ hI kg_w_null
  have hdt : (∫ s in (0:ℝ)..10,
      (kw_horizonSplitting kg_w_g kg_w_X kg_w_γ 0 10 (kw_vel_eq hγ) hXne).dt s
        (kw_vel kg_w_γ s)) = 10 := by
    rw [intervalIntegral.integral_congr (g := fun _ => (1 : ℝ)) fun s hs => by
      rw [uIcc_of_le (by norm_num)] at hs
      show kw_dt kg_w_X kg_w_γ s (kw_vel kg_w_γ s) = 1
      rw [kw_vel_eq hγ s hs]; exact kw_dt_X (hXne s hs)]
    simp
  have h0 : kg_w_γ 0 = ((0 : ℝ), (1 : ℝ)) := by simp [kg_w_γ]
  exact ⟨_, rfl, rfl, rfl, hΔx, hΔτ, hdt, h0, rfl, hC kg_w_injOn 0 hI 10 hI' (by norm_num),
    hB 0 hI 10 hI', hB 10 hI' 0 hI⟩

end KWWitness


end KillingWholeKit


/-! ## Campaign 106 (`r7689+71`): `cor:stationary` on `N`, witnessed on Schwarzschild's `∂J⁻(𝒥⁺)` on `W` -/

/-! ### Campaign 97 ③'s `sq_` facts, copied from `SchwarzschildKilling.lean` (names kept)

Only the pieces the witness uses: the `t ↦ t • B` derivative and `χ = (1/4M)(V∂_V − U∂_U)` as a linear map. -/

section SQCopied

open Manifold ContinuousLinearMap

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]

/-- `y ↦ c(y) • B` for a fixed bilinear form `B` (generic `E`; the derivative goes through the continuous
linear map `t ↦ t • B`, avoiding a bounded-smul instance search on the bilinear-map space). -/
theorem sq_smul_hasFDerivAt (B : E →L[ℝ] E →L[ℝ] ℝ) {c : E → ℝ} {c' : E →L[ℝ] ℝ} {x : E}
    (hc : HasFDerivAt c c' x) :
    HasFDerivAt (fun y => c y • B) (((1 : ℝ →L[ℝ] ℝ).smulRight B).comp c') x := by
  have h0 := ContinuousLinearMap.hasFDerivAt (𝕜 := ℝ) (E := ℝ)
    (F := E →L[ℝ] E →L[ℝ] ℝ) (x := c x) ((1 : ℝ →L[ℝ] ℝ).smulRight B)
  have h : HasFDerivAt (((1 : ℝ →L[ℝ] ℝ).smulRight B) ∘ c)
      (((1 : ℝ →L[ℝ] ℝ).smulRight B).comp c') x :=
    HasFDerivAt.comp (g := ((1 : ℝ →L[ℝ] ℝ).smulRight B)) x h0 hc
  convert h using 1
  funext y; simp

/-- `D(c • B)_x(u)(v, w) = Dc_x(u) · B(v, w)`. -/
theorem sq_smul_fderiv_apply (B : E →L[ℝ] E →L[ℝ] ℝ) {c : E → ℝ} {x : E}
    (hc : DifferentiableAt ℝ c x) (u v w : E) :
    fderiv ℝ (fun y => c y • B) x u v w = fderiv ℝ c x u * B v w := by
  rw [(sq_smul_hasFDerivAt B hc.hasFDerivAt).fderiv]; simp

/-- `χ` as a linear map: `(U, V) ↦ (1/4M)(−U, V)`. -/
noncomputable def sq_L (M : ℝ) : (ℝ × ℝ) →L[ℝ] (ℝ × ℝ) := (1 / (4 * M)) • kg_w_L

theorem sq_L_apply (M : ℝ) (x : ℝ × ℝ) : sq_L M x = (-x.1 / (4 * M), x.2 / (4 * M)) := by
  simp only [sq_L, smul_apply, kg_w_L_apply, Prod.smul_mk, smul_eq_mul]
  ext <;> simp only <;> ring

end SQCopied

/-! ### ① `MSpacetime.IsKillingHorizon` and `st_cor_stationary` -/

section STCorollary

open Manifold

set_option linter.unusedSectionVars false
set_option synthInstance.maxHeartbeats 400000

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
variable {N : Type*} [TopologicalSpace N] [ChartedSpace E N] [IsManifold 𝓘(ℝ, E) 2 N]

namespace MSpacetime

/-- **`Hs` is a Killing horizon of `X`** for the `MSpacetime` `S`: the conclusion of the rigidity theorem
(Hawking, with analyticity), which P1 cites in the proof of `cor:stationary` and which is **taken here as a hypothesis**. The clauses
are exactly `kw_lemma_killing_whole`'s hypotheses, stated pointwise on `Hs`:
* `X` is `C¹` as a section of `TN` at each point of `Hs`, and `X ≠ 0` on `Hs`;
* the chart representative `hRep g` is differentiable near each point of `Hs`;
* `L_X g = 0` near each point of `Hs`;
* through each `p ∈ Hs` there is an integral curve of `X` (on the segment from `0` to some `t₀`, `γ 0 = p`)
  inside `Hs`, null at `γ t₀`. -/
structure IsKillingHorizon (S : MSpacetime E N) (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (Hs : Set N) :
    Prop where
  C1 : ∀ p ∈ Hs, ContMDiffAt 𝓘(ℝ, E) 𝓘(ℝ, E).tangent 1
    (fun x ↦ (⟨x, X x⟩ : TangentBundle 𝓘(ℝ, E) N)) p
  ne_zero : ∀ p ∈ Hs, X p ≠ 0
  hRep_diff : ∀ p ∈ Hs, ∀ᶠ y in 𝓝 (extChartAt 𝓘(ℝ, E) p p), DifferentiableAt ℝ (hRep S.g p) y
  killing : ∀ p ∈ Hs, ∀ᶠ x in 𝓝 p, ∀ v w, lieDeriv X S.g x v w = 0
  generator : ∀ p ∈ Hs, ∃ (γ : ℝ → N) (t₀ : ℝ), γ 0 = p ∧
    (∀ t ∈ uIcc 0 t₀, γ t ∈ Hs ∧ IsMIntegralCurveAt γ X t) ∧
    S.g (γ t₀) (X (γ t₀)) (X (γ t₀)) = 0

/-- On a Killing horizon `X` is null everywhere: through `p` take the generator of the definition and run
`kw_lemma_killing_whole` (a) on the segment from `0` to `t₀`. -/
theorem st_null_of_isKillingHorizon {S : MSpacetime E N} {X : Π x : N, TangentSpace 𝓘(ℝ, E) x}
    {Hs : Set N} (hH : S.IsKillingHorizon X Hs) {p : N} (hp : p ∈ Hs) :
    S.g p (X p) (X p) = 0 := by
  obtain ⟨δ, t₀, hδ0, hδ, hnull⟩ := hH.generator p hp
  have hmem : ∀ t ∈ Icc (min 0 t₀) (max 0 t₀), δ t ∈ Hs ∧ IsMIntegralCurveAt δ X t :=
    fun t ht => hδ t (by rw [uIcc]; exact ht)
  have h0 : (0 : ℝ) ∈ Icc (min 0 t₀) (max 0 t₀) := ⟨min_le_left _ _, le_max_left _ _⟩
  have ht₀ : t₀ ∈ Icc (min 0 t₀) (max 0 t₀) := ⟨min_le_right _ _, le_max_right _ _⟩
  obtain ⟨-, hA, -⟩ := kw_lemma_killing_whole X S.g δ (min 0 t₀) (max 0 t₀) t₀ min_le_max
    (fun t ht => hH.C1 _ (hmem t ht).1) (fun t ht => hH.ne_zero _ (hmem t ht).1)
    (fun t ht => hH.hRep_diff _ (hmem t ht).1) (fun t ht => hH.killing _ (hmem t ht).1)
    (fun t ht => (hmem t ht).2) ht₀ hnull
  have := (hA 0 h0).1
  rwa [hδ0] at this

end MSpacetime

/-- **`cor:stationary` on `N`, `st_cor_stationary`.** Let `S.H J = ∂J⁻(J)` be a Killing horizon of `X`
(`S.IsKillingHorizon X (S.H J)`). **This is rigidity's conclusion, taken as the hypothesis, exactly as P1
cites it** (in the proof of `cor:stationary`: Hawking's rigidity theorem, with analyticity). Rigidity itself is not proved: it needs the
Einstein equations, which are not in the kit; "stationary" has no formal content beyond invoking it.

Then along every generator `γ` (an integral curve of `X` on `[a, b]` with `γ '' [a, b] ⊆ 𝓗⁺`), all of
`kw_lemma_killing_whole`'s conclusions hold: `γ′ = X`; `X` and `γ′` are null; every pair of events of
`γ [a, b]` is `kg_Related` (related both ways by local isometries carrying the generator into itself: metric
coincidence), distinct when `γ` is injective; `Δτ = 0` (`kg_deltaTau`); and the horizon splitting `σ`
(`n = |X|`, `dt = dλ`, `h = g + n² dλ²`) has `h = g` on `γ`, `h(γ′, γ′) = 0`, `Δx = 0` and `Δτ = 0`. -/
theorem st_cor_stationary (S : MSpacetime E N) (J : Set N) (X : Π x : N, TangentSpace 𝓘(ℝ, E) x)
    (hH : S.IsKillingHorizon X (S.H J)) (γ : ℝ → N) (a b : ℝ) (hab : a ≤ b)
    (hγ : ∀ t ∈ Icc a b, IsMIntegralCurveAt γ X t) (hin : γ '' Icc a b ⊆ S.H J) :
    (∀ t ∈ Icc a b, mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ t (1 : ℝ) = X (γ t)) ∧
    (∀ t ∈ Icc a b, S.g (γ t) (X (γ t)) (X (γ t)) = 0 ∧
      S.g (γ t) (mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ t (1 : ℝ)) (mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ t (1 : ℝ)) = 0) ∧
    (∀ t₁ ∈ Icc a b, ∀ t₂ ∈ Icc a b, kg_Related S.g γ t₁ t₂) ∧
    (InjOn γ (Icc a b) → ∀ t₁ ∈ Icc a b, ∀ t₂ ∈ Icc a b, t₁ ≠ t₂ → γ t₁ ≠ γ t₂) ∧
    kg_deltaTau S.g X γ a b = 0 ∧
    ∃ σ : kw_AdaptedSplitting S.g γ a b,
      σ.n = kw_n S.g X γ ∧ σ.dt = kw_dt X γ ∧ σ.h = kw_h S.g X γ ∧
      (∀ s ∈ Icc a b, σ.h s = kw_gE S.g (γ s) ∧ σ.h s (kw_vel γ s) (kw_vel γ s) = 0) ∧
      σ.Δx = 0 ∧ σ.Δτ = 0 := by
  have hmem : ∀ t ∈ Icc a b, γ t ∈ S.H J := fun t ht => hin ⟨t, ht, rfl⟩
  have ha : a ∈ Icc a b := ⟨le_rfl, hab⟩
  obtain ⟨hvel, hA, hB, hC, hD, hE, -, hΔx, -, hΔτ⟩ :=
    kw_lemma_killing_whole X S.g γ a b a hab
    (fun t ht => hH.C1 _ (hmem t ht)) (fun t ht => hH.ne_zero _ (hmem t ht))
    (fun t ht => hH.hRep_diff _ (hmem t ht)) (fun t ht => hH.killing _ (hmem t ht))
    hγ ha (MSpacetime.st_null_of_isKillingHorizon hH (hmem a ha))
  exact ⟨hvel, hA, hB, hC, hD, _, rfl, rfl, rfl, hE, hΔx, hΔτ⟩

end STCorollary

/-! ### ② The witness: Schwarzschild's `𝓗⁺ = ∂J⁻(𝒥⁺)` on `W`, `χ = ∂_t = (V∂_V − U∂_U)/4M` -/

namespace STModel
open Model NModel SEModel SXModel Kruskal Manifold Bundle ContinuousLinearMap TopologicalSpace

set_option synthInstance.maxHeartbeats 400000

/-- `χ = ∂_t = (1/4M)(V∂_V − U∂_U)` on `W`, read in the inclusion chart. -/
noncomputable def st_χ (M : ℝ) : Π x : seW, TangentSpace 𝓘(ℝ, P) x := fun x => sq_L M x.1

/-- **The metric of `se_S` pointwise:** `g_x = F(x) · gM`. -/
lemma st_g_apply {M : ℝ} (hM : 0 < M) (x : seW) (v w : P) :
    (se_S hM).g x v w = FS M x.1 * gM v w := rfl

/-- **`chartRep χ = sq_L` on `W`** (the inclusion is the chart, `se_dchart`). -/
lemma st_chartRep (M : ℝ) (p : seW) {y : P} (hy : y ∈ seWS) : chartRep (st_χ M) p y = sq_L M y := by
  unfold chartRep
  refine (se_dchart p _ _).trans ?_
  show sq_L M ((extChartAt 𝓘(ℝ, P) p).symm y).1 = _
  rw [se_symm_apply p hy]

lemma st_chartRep_eventually (M : ℝ) (p : seW) {y : P} (hy : y ∈ seWS) :
    chartRep (st_χ M) p =ᶠ[𝓝 y] ⇑(sq_L M) := by
  filter_upwards [seWS_open.mem_nhds hy] with z hz using st_chartRep M p hz

lemma st_hRep_eventually {M : ℝ} (hM : 0 < M) (p : seW) {y : P} (hy : y ∈ seWS) :
    hRep (se_S hM).g p =ᶠ[𝓝 y] fun z => FS M z • gM := by
  filter_upwards [seWS_open.mem_nhds hy] with z hz using se_hRep hM p hz

lemma st_FS_diff {M : ℝ} (hM : 0 < M) {y : P} (hy : y ∈ sk_kM) : DifferentiableAt ℝ (FS M) y :=
  ((sk_FS_contDiffOn hM).contDiffAt (sk_kM_open.mem_nhds hy)).differentiableAt one_ne_zero

lemma st_gF_diff {M : ℝ} (hM : 0 < M) {y : P} (hy : y ∈ sk_kM) :
    DifferentiableAt ℝ (fun z => FS M z • gM) y :=
  (sq_smul_hasFDerivAt gM (st_FS_diff hM hy).hasFDerivAt).differentiableAt

/-- `F` depends on `(U, V)` only through `UV`: invariant under the boost `(e^{−t} U, e^t V)`. -/
lemma st_FS_boost (M t : ℝ) (y : P) :
    FS M (Real.exp (-t) * y.1, Real.exp t * y.2) = FS M y := by
  have e : (Real.exp (-t) * y.1) * (Real.exp t * y.2) = y.1 * y.2 := by
    have := Real.exp_neg t
    rw [this]; field_simp
  simp only [FS, rK, e]

/-- **`χ(F) = 0` on `{UV < 1}`**, by differentiating the boost invariance at `t = 0`. -/
lemma st_chi_F {M : ℝ} (hM : 0 < M) {y : P} (hy : y ∈ sk_kM) : fderiv ℝ (FS M) y (sq_L M y) = 0 := by
  have hc : HasDerivAt (fun t : ℝ => ((Real.exp (-t) * y.1, Real.exp t * y.2) : P)) (-y.1, y.2) 0 := by
    have h1 : HasDerivAt (fun t : ℝ => Real.exp (-t) * y.1) (-y.1) 0 := by
      have := ((hasDerivAt_neg (0:ℝ)).exp).mul_const y.1
      convert this using 1; simp
    have h2 : HasDerivAt (fun t : ℝ => Real.exp t * y.2) y.2 0 := by
      have := (Real.hasDerivAt_exp 0).mul_const y.2
      convert this using 1; simp
    exact h1.prodMk h2
  have hF := (st_FS_diff hM hy).hasFDerivAt
  have hc0 : (fun t : ℝ => ((Real.exp (-t) * y.1, Real.exp t * y.2) : P)) 0 = y := by simp
  rw [← hc0] at hF
  have hcomp := hF.comp_hasDerivAt (0 : ℝ) hc
  have hconst : HasDerivAt (FS M ∘ fun t : ℝ => ((Real.exp (-t) * y.1, Real.exp t * y.2) : P))
      0 0 := by
    have : (FS M ∘ fun t : ℝ => ((Real.exp (-t) * y.1, Real.exp t * y.2) : P)) = fun _ => FS M y := by
      funext t; exact st_FS_boost M t y
    rw [this]; exact hasDerivAt_const _ _
  have h0 : fderiv ℝ (FS M) y (-y.1, y.2) = 0 := by
    rw [hc0] at hcomp; exact hcomp.unique hconst
  have e : sq_L M y = (1 / (4 * M)) • ((-y.1, y.2) : P) := by
    rw [sq_L_apply]; ext <;> simp <;> ring
  rw [e, map_smul, h0, smul_zero]

/-- The chart Killing expression for `F • gM` and `sq_L` vanishes on `{UV < 1}`. -/
lemma st_chartLie {M : ℝ} (hM : 0 < M) {z : P} (hz : z ∈ sk_kM) (a b : P) :
    chartLie (fun y => FS M y • gM) ⇑(sq_L M) z a b = 0 := by
  unfold chartLie
  rw [sq_smul_fderiv_apply gM (st_FS_diff hM hz), st_chi_F hM hz, ContinuousLinearMap.fderiv, zero_mul,
    zero_add]
  simp only [smul_apply, smul_eq_mul, gM_apply, sq_L_apply]
  ring

/-- `chartLie` only sees the germs of its two arguments at `z`. -/
lemma st_chartLie_congr {F F' : P → P →L[ℝ] P →L[ℝ] ℝ} {X' X'' : P → P} {z : P}
    (hF : F =ᶠ[𝓝 z] F') (hX : X' =ᶠ[𝓝 z] X'') (a b : P) :
    chartLie F X' z a b = chartLie F' X'' z a b := by
  unfold chartLie
  rw [hF.fderiv_eq, hX.fderiv_eq, hF.eq_of_nhds, hX.eq_of_nhds]

/-- **`L_χ g = 0` on `W`** for Schwarzschild `se_S` on the `Opens` subtype: `ld_lieDeriv_chart_self` in the
inclusion chart, then the plane's chart computation (`hRep g = F • gM`, `chartRep χ = sq_L` near `x`). -/
theorem st_lieDeriv {M : ℝ} (hM : 0 < M) (x : seW) (v w : P) :
    lieDeriv (st_χ M) (se_S hM).g x v w = 0 := by
  have hx : (x : P) ∈ seWS := x.2
  have hxk : (x : P) ∈ sk_kM := seWS_kM hx
  have hh : DifferentiableAt ℝ (hRep (se_S hM).g x) (extChartAt 𝓘(ℝ, P) x x) :=
    (st_gF_diff hM hxk).congr_of_eventuallyEq (st_hRep_eventually hM x hx)
  rw [ld_lieDeriv_chart_self (st_χ M) (se_S hM).g x v w hh, se_dchart, se_dchart]
  change chartLie (hRep (se_S hM).g x) (chartRep (st_χ M) x) (x : P) v w = 0
  rw [st_chartLie_congr (st_hRep_eventually hM x hx) (st_chartRep_eventually M x hx)]
  exact st_chartLie hM hxk v w

/-- **`χ` is `C¹` as a section of `TW`** (`contMDiffAt_section`; the trivialisation coordinate is
`chartRep χ p ∘ val = sq_L ∘ val`). -/
theorem st_hX (M : ℝ) (p : seW) : ContMDiffAt 𝓘(ℝ, P) 𝓘(ℝ, P).tangent 1
    (fun x ↦ (⟨x, st_χ M x⟩ : TangentBundle 𝓘(ℝ, P) seW)) p := by
  refine (contMDiffAt_section p).2 ?_
  have e : (fun z : seW ↦ (trivializationAt P (TangentSpace 𝓘(ℝ, P)) p
      (⟨z, st_χ M z⟩ : TangentBundle 𝓘(ℝ, P) seW)).2) = fun z => sq_L M z.1 := by
    funext z
    have hy : (z : P) ∈ (extChartAt 𝓘(ℝ, P) p).target := by
      have := (extChartAt 𝓘(ℝ, P) p).map_source (x := z) (by rw [extChartAt_source]; exact se_src p z)
      exact this
    have h := ld_chartRep_eq_triv (st_χ M) p hy
    rw [se_symm_apply p z.2] at h
    rw [← h, st_chartRep M p z.2]
  rw [e]
  exact ((sq_L M).contDiff.contMDiff.comp contMDiff_subtype_val).contMDiffAt

/-- `g(χ, χ) = F · UV/(16M²)` on `W`. -/
lemma st_normSq {M : ℝ} (hM : 0 < M) (x : seW) :
    (se_S hM).g x (st_χ M x) (st_χ M x) = FS M x.1 * (x.1.1 * x.1.2) / (16 * M ^ 2) := by
  show FS M x.1 * gM (sq_L M x.1) (sq_L M x.1) = _
  rw [gM_apply, sq_L_apply]
  field_simp; ring

/-- The event `(0, V)` of `W` (`V > 0`). -/
def st_ev (V : ℝ) (hV : 0 < V) : seW := ⟨((0 : ℝ), V), ⟨hV, by simp⟩⟩

/-- The horizon generator through `(0, V₀)`: `γ s = (0, V₀ e^{s/4M})`. -/
noncomputable def st_γ (M V₀ : ℝ) (hV₀ : 0 < V₀) (s : ℝ) : seW :=
  st_ev (V₀ * Real.exp (s / (4 * M))) (mul_pos hV₀ (Real.exp_pos _))

lemma st_γ_zero (M V₀ : ℝ) (hV₀ : 0 < V₀) : st_γ M V₀ hV₀ 0 = st_ev V₀ hV₀ := by
  simp [st_γ, st_ev]

lemma st_χ_γ (M V₀ : ℝ) (hV₀ : 0 < V₀) (s : ℝ) :
    st_χ M (st_γ M V₀ hV₀ s) = ((0 : ℝ), V₀ * Real.exp (s / (4 * M)) / (4 * M)) := by
  show sq_L M _ = _
  rw [sq_L_apply]; simp [st_γ, st_ev]

/-- **`γ` is an integral curve of `χ` in `W`**: the chart of `W` is the inclusion, so `γ`'s chart
expression is the plane curve `(0, V₀ e^{s/4M})`. -/
theorem st_integral {M : ℝ} (V₀ : ℝ) (hV₀ : 0 < V₀) (t : ℝ) :
    IsMIntegralCurveAt (st_γ M V₀ hV₀) (st_χ M) t := by
  refine Filter.Eventually.of_forall fun s => ?_
  have he : HasDerivAt (fun s : ℝ => V₀ * Real.exp (s / (4 * M)))
      (V₀ * Real.exp (s / (4 * M)) / (4 * M)) s := by
    have := (((hasDerivAt_id s).div_const (4 * M)).exp).const_mul V₀
    refine this.congr_deriv ?_
    simp only [id]; ring
  have hd : HasDerivAt (fun s => ((st_γ M V₀ hV₀ s : seW) : P))
      ((0 : ℝ), V₀ * Real.exp (s / (4 * M)) / (4 * M)) s :=
    (hasDerivAt_const s (0:ℝ)).prodMk he
  have hcont : Continuous (st_γ M V₀ hV₀) :=
    Continuous.subtype_mk (continuous_const.prodMk
      (continuous_const.mul (Real.continuous_exp.comp (continuous_id.div_const _)))) _
  rw [st_χ_γ]
  refine ⟨hcont.continuousAt, ?_⟩
  simp only [mfld_simps]
  exact hd.hasFDerivAt.hasFDerivWithinAt

/-- **`𝓗⁺ = ∂J⁻(𝒥⁺)` on `W` is `{U = 0}`** (from `sx_prop_causal_alignment`: `val '' 𝓗⁺ = {U = 0, V > 0}`). -/
lemma st_mem_H {M : ℝ} (hM : 0 < M) {r₀ : ℝ} (hr₀ : 2 * M < r₀) (x : seW) :
    x ∈ (se_S hM).H (range (se_Ost hM hr₀)) ↔ x.1.1 = 0 := by
  have h := (sx_prop_causal_alignment hM hr₀).2.1
  rw [← (sx_prop_causal_alignment hM hr₀).1] at h
  constructor
  · intro hx
    have : (x : P) ∈ Subtype.val '' (se_S hM).H (range (se_Ost hM hr₀)) := ⟨x, hx, rfl⟩
    rw [h] at this; exact this.1
  · intro hx
    have : (x : P) ∈ ({p : P | p.1 = 0 ∧ 0 < p.2} : Set P) := ⟨hx, x.2.1⟩
    rw [← h] at this
    obtain ⟨y, hy, hyx⟩ := this
    rwa [← Subtype.ext hyx]

/-- **`∂J⁻(𝒥⁺)` is a Killing horizon of `χ = ∂_t` for Schwarzschild on `W`.** -/
theorem st_isKillingHorizon {M : ℝ} (hM : 0 < M) {r₀ : ℝ} (hr₀ : 2 * M < r₀) :
    (se_S hM).IsKillingHorizon (st_χ M) ((se_S hM).H (range (se_Ost hM hr₀))) where
  C1 := fun p _ => st_hX M p
  ne_zero := fun p _ h => by
    have h2 := congrArg Prod.snd h
    change (sq_L M p.1).2 = 0 at h2
    rw [sq_L_apply] at h2
    have : (0 : ℝ) < p.1.2 / (4 * M) := div_pos p.2.1 (by positivity)
    exact this.ne' h2
  hRep_diff := fun p _ => by
    filter_upwards [seWS_open.mem_nhds (show extChartAt 𝓘(ℝ, P) p p ∈ seWS from p.2)] with y hy
    exact (st_gF_diff hM (seWS_kM hy)).congr_of_eventuallyEq (st_hRep_eventually hM p hy)
  killing := fun p _ => Filter.Eventually.of_forall fun x v w => st_lieDeriv hM x v w
  generator := fun p hp => by
    have hU : p.1.1 = 0 := (st_mem_H hM hr₀ p).1 hp
    refine ⟨st_γ M p.1.2 p.2.1, 0, ?_, fun t _ => ⟨?_, st_integral _ _ t⟩, ?_⟩
    · rw [st_γ_zero]; exact Subtype.ext (Prod.ext hU.symm rfl)
    · rw [st_mem_H hM hr₀]; rfl
    · rw [st_normSq]; simp [st_γ, st_ev]

/-- **② `st_witness`.** Schwarzschild on `W` (`se_S`, `g = −F dU dV`), with the static observer at `r₀ > 2M`
and `𝓗⁺ = S.H J = ∂J⁻(𝒥⁺)` (`sx_prop_causal_alignment`): `𝓗⁺` is a Killing horizon of `χ = ∂_t =
(V∂_V − U∂_U)/4M`, so `st_cor_stationary` applies. For `0 < V₁ < V₂` the two events `(0, V₁) ≠ (0, V₂)` lie on
`∂J⁻(𝒥⁺)`, are joined by the generator `γ s = (0, V₁ e^{s/4M})`, `s ∈ [0, b]`, `b = 4M log(V₂/V₁) > 0`, and are
**metrically coincident**: `kg_Related` both ways, `Δτ = 0`, and the horizon splitting has `Δx = Δτ = 0`. -/
theorem st_witness {M : ℝ} (hM : 0 < M) {r₀ : ℝ} (hr₀ : 2 * M < r₀) {V₁ V₂ : ℝ} (h₁ : 0 < V₁)
    (h₁₂ : V₁ < V₂) :
    (se_S hM).H (range (se_Ost hM hr₀)) = frontier ((sx_ext hM).ι ⁻¹' cz_St.JpastSet cz_scri) ∧
    (se_S hM).IsKillingHorizon (st_χ M) ((se_S hM).H (range (se_Ost hM hr₀))) ∧
    st_ev V₁ h₁ ∈ (se_S hM).H (range (se_Ost hM hr₀)) ∧
    st_ev V₂ (h₁.trans h₁₂) ∈ (se_S hM).H (range (se_Ost hM hr₀)) ∧
    st_ev V₁ h₁ ≠ st_ev V₂ (h₁.trans h₁₂) ∧
    0 < 4 * M * Real.log (V₂ / V₁) ∧
    st_γ M V₁ h₁ 0 = st_ev V₁ h₁ ∧
    st_γ M V₁ h₁ (4 * M * Real.log (V₂ / V₁)) = st_ev V₂ (h₁.trans h₁₂) ∧
    st_γ M V₁ h₁ '' Icc 0 (4 * M * Real.log (V₂ / V₁)) ⊆ (se_S hM).H (range (se_Ost hM hr₀)) ∧
    kg_Related (se_S hM).g (st_γ M V₁ h₁) 0 (4 * M * Real.log (V₂ / V₁)) ∧
    kg_Related (se_S hM).g (st_γ M V₁ h₁) (4 * M * Real.log (V₂ / V₁)) 0 ∧
    kg_deltaTau (se_S hM).g (st_χ M) (st_γ M V₁ h₁) 0 (4 * M * Real.log (V₂ / V₁)) = 0 ∧
    ∃ σ : kw_AdaptedSplitting (se_S hM).g (st_γ M V₁ h₁) 0 (4 * M * Real.log (V₂ / V₁)),
      σ.n = kw_n (se_S hM).g (st_χ M) (st_γ M V₁ h₁) ∧ σ.dt = kw_dt (st_χ M) (st_γ M V₁ h₁) ∧
      σ.h = kw_h (se_S hM).g (st_χ M) (st_γ M V₁ h₁) ∧ σ.Δx = 0 ∧ σ.Δτ = 0 := by
  set b := 4 * M * Real.log (V₂ / V₁) with hb
  have hb0 : 0 < b := mul_pos (by positivity) (Real.log_pos ((one_lt_div h₁).2 h₁₂))
  have hH := st_isKillingHorizon hM hr₀
  have hin : st_γ M V₁ h₁ '' Icc 0 b ⊆ (se_S hM).H (range (se_Ost hM hr₀)) := by
    rintro _ ⟨t, -, rfl⟩; rw [st_mem_H hM hr₀]; rfl
  have hγb : st_γ M V₁ h₁ b = st_ev V₂ (h₁.trans h₁₂) := by
    simp only [st_γ, st_ev, hb]
    congr 2
    rw [mul_div_cancel_left₀ _ (by positivity : (4 * M : ℝ) ≠ 0), Real.exp_log (div_pos (h₁.trans h₁₂) h₁)]
    field_simp
  have hI0 : (0 : ℝ) ∈ Icc 0 b := ⟨le_rfl, hb0.le⟩
  have hIb : b ∈ Icc 0 b := ⟨hb0.le, le_rfl⟩
  obtain ⟨-, -, hB, -, hD, σ, hσ1, hσ2, hσ3, -, hΔx, hΔτ⟩ :=
    st_cor_stationary (se_S hM) (range (se_Ost hM hr₀)) (st_χ M) hH (st_γ M V₁ h₁) 0 b hb0.le
      (fun t _ => st_integral _ _ t) hin
  refine ⟨(sx_prop_causal_alignment hM hr₀).1, hH, (st_mem_H hM hr₀ _).2 rfl, (st_mem_H hM hr₀ _).2 rfl,
    fun h => h₁₂.ne (congrArg (fun x : seW => x.1.2) h), hb0, st_γ_zero M V₁ h₁, hγb, hin,
    hB 0 hI0 b hIb, hB b hIb 0 hI0, hD, σ, hσ1, hσ2, hσ3, hΔx, hΔτ⟩

end STModel

/-! ## Campaign 107: geodesics, energy conservation and `2iii` (prefix `ng_`) -/

section NullGeodesic
open Manifold
set_option linter.unusedSectionVars false

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]

/-- **The Koszul form** of a bilinear-form field `G : E → E →L E →L ℝ` (a chart metric):
`kos(y)(u, v, w) = ½ (DG(y)(u)(v, w) + DG(y)(v)(u, w) − DG(y)(w)(u, v))`, so that the Christoffel
map is defined by `G(y)(Γ(y)(u, v), w) = kos(y)(u, v, w)`. -/
noncomputable def ng_kos (G : E → E →L[ℝ] E →L[ℝ] ℝ) (y u v w : E) : ℝ :=
  (1 / 2 : ℝ) * (fderiv ℝ G y u v w + fderiv ℝ G y v u w - fderiv ℝ G y w u v)

open Classical in
/-- **The Christoffel map** of `G` (Koszul): the `z` with `G(y)(z, ·) = kos(y)(u, v, ·)` when one
exists (always, for `G(y)` nondegenerate on finite-dimensional `E`: `ng_Γ_exists`), junk `0`
otherwise. -/
noncomputable def ng_Γ (G : E → E →L[ℝ] E →L[ℝ] ℝ) (y u v : E) : E :=
  if h : ∃ z : E, ∀ w, G y z w = ng_kos G y u v w then h.choose else 0

/-- `ng_Γ` satisfies its defining (Koszul) identity whenever a representative exists. -/
lemma ng_Γ_spec {G : E → E →L[ℝ] E →L[ℝ] ℝ} {y u v : E}
    (h : ∃ z : E, ∀ w, G y z w = ng_kos G y u v w) (w : E) :
    G y (ng_Γ G y u v) w = ng_kos G y u v w := by
  simp only [ng_Γ, h, ↓reduceDIte]; exact h.choose_spec w

/-- Uniqueness: for `G(y)` nondegenerate, any `z` with the Koszul identity is `ng_Γ`. -/
lemma ng_Γ_unique {G : E → E →L[ℝ] E →L[ℝ] ℝ} {y u v : E}
    (hnd : ∀ z, (∀ w, G y z w = 0) → z = 0) {z : E} (hz : ∀ w, G y z w = ng_kos G y u v w) :
    ng_Γ G y u v = z := by
  have h : ∃ z : E, ∀ w, G y z w = ng_kos G y u v w := ⟨z, hz⟩
  refine sub_eq_zero.1 (hnd _ fun w => ?_)
  rw [map_sub, sub_apply, ng_Γ_spec h, hz, sub_self]

/-- Existence of the Koszul representative for `G(y)` nondegenerate, `E` finite-dimensional. -/
lemma ng_Γ_exists [FiniteDimensional ℝ E] {G : E → E →L[ℝ] E →L[ℝ] ℝ} {y : E}
    (hnd : ∀ z, (∀ w, G y z w = 0) → z = 0) (u v : E) :
    ∃ z : E, ∀ w, G y z w = ng_kos G y u v w := by
  let L : E →ₗ[ℝ] Module.Dual ℝ E :=
    { toFun := fun z => (G y z : E →L[ℝ] ℝ).toLinearMap
      map_add' := fun a b => by ext; simp
      map_smul' := fun c a => by ext; simp }
  have hinj : Function.Injective L := by
    rw [← LinearMap.ker_eq_bot, LinearMap.ker_eq_bot']
    intro z hz
    exact hnd z fun w => by simpa [L] using LinearMap.congr_fun hz w
  have hsurj : Function.Surjective L :=
    (LinearMap.injective_iff_surjective_of_finrank_eq_finrank
      (Subspace.dual_finrank_eq).symm).1 hinj
  let φ : Module.Dual ℝ E :=
    { toFun := fun w => ng_kos G y u v w
      map_add' := fun a b => by simp only [ng_kos, map_add, add_apply]; ring
      map_smul' := fun c a => by
        simp only [ng_kos, map_smul, smul_apply, smul_eq_mul,
          RingHom.id_apply]; ring }
  obtain ⟨z, hz⟩ := hsurj φ
  exact ⟨z, fun w => LinearMap.congr_fun hz w⟩

/-- **The two forms of the geodesic equation agree**: with a Koszul representative available,
`c″ = −Γ(c)(c′, c′)` gives `G(c)(c″, w) = −kos(c)(c′, c′, w)` for every `w` (the form used in
`IsGeodesicOn`), and conversely when `G(c)` is nondegenerate. -/
lemma ng_geod_iff {G : E → E →L[ℝ] E →L[ℝ] ℝ} {y u a : E}
    (hnd : ∀ z, (∀ w, G y z w = 0) → z = 0) (h : ∃ z : E, ∀ w, G y z w = ng_kos G y u u w) :
    a = -ng_Γ G y u u ↔ ∀ w, G y a w = -ng_kos G y u u w := by
  constructor
  · rintro rfl w
    rw [map_neg, neg_apply, ng_Γ_spec h]
  · intro ha
    have : -a = ng_Γ G y u u := (ng_Γ_unique hnd (fun w => by
      rw [map_neg, neg_apply, ha, neg_neg])).symm
    rw [← this, neg_neg]

variable {N : Type*} [TopologicalSpace N] [ChartedSpace E N] [IsManifold 𝓘(ℝ, E) 1 N]

variable (E) in
/-- The chart curve `c = φ_p ∘ γ` in the preferred chart at `p`. -/
noncomputable def ng_c (p : N) (γ : ℝ → N) (s : ℝ) : E := extChartAt 𝓘(ℝ, E) p (γ s)

namespace MSpacetime

/-- **① `S.IsGeodesicOn γ a b`** (an affinely parametrised geodesic segment): for every
`t ∈ [a, b]` there is `ε > 0` such that, in the preferred chart at `p = γ t`, `γ` stays in the chart
on `(t − ε, t + ε)`, the chart curve `c = φ_p ∘ γ` is `C²` there, and `c″ = −Γ(c)(c′, c′)` there,
in its Koszul form `hRep g p (c) (c″, w) = −kos(c)(c′, c′, w)` for all `w` (`ng_geod_iff`: the same
as `c″ = −ng_Γ (hRep g p) c c′ c′` when `hRep g p (c)` is nondegenerate). -/
def IsGeodesicOn (S : MSpacetime E N) (γ : ℝ → N) (a b : ℝ) : Prop :=
  ∀ t ∈ Icc a b, ∃ ε > 0,
    (∀ s ∈ Ioo (t - ε) (t + ε), γ s ∈ (chartAt E (γ t)).source) ∧
    ContDiffOn ℝ 2 (ng_c E (γ t) γ) (Ioo (t - ε) (t + ε)) ∧
    ∀ s ∈ Ioo (t - ε) (t + ε), ∀ w : E,
      hRep S.g (γ t) (ng_c E (γ t) γ s) (deriv (deriv (ng_c E (γ t) γ)) s) w =
        -ng_kos (hRep S.g (γ t)) (ng_c E (γ t) γ s) (deriv (ng_c E (γ t) γ) s)
          (deriv (ng_c E (γ t) γ) s) w

variable {S : MSpacetime E N}

/-- `hRep g` is symmetric. -/
lemma ng_hRep_symm (S : MSpacetime E N) (p : N) (y v w : E) :
    hRep S.g p y v w = hRep S.g p y w v := by
  rw [ld_hRep_apply, ld_hRep_apply]; exact S.symm _ _ _

/-- A curve whose chart curve is differentiable (and which stays in the chart) is
manifold-differentiable, and the chart curve's derivative is `Dφ_p (vel γ s)`. -/
lemma ng_vel_chart {γ : ℝ → N} {p : N} {I : Set ℝ} (hI : IsOpen I) {s : ℝ} (hs : s ∈ I)
    (hsrc : ∀ s ∈ I, γ s ∈ (chartAt E p).source) (hd : DifferentiableAt ℝ (ng_c E p γ) s) :
    MDifferentiableAt 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ s ∧
      HasDerivAt (fun s => extChartAt 𝓘(ℝ, E) p (γ s))
        (mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) (γ s)
          (mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ s (1 : ℝ))) s := by
  have hev : (fun s => (extChartAt 𝓘(ℝ, E) p).symm (ng_c E p γ s)) =ᶠ[𝓝 s] γ := by
    filter_upwards [hI.mem_nhds hs] with s' hs' using ch_left_inv p (hsrc s' hs')
  have hm := (ch_vel_symm p hd (ch_mem_target p (hsrc s hs))).1
  have hγ : MDifferentiableAt 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ s := hm.congr_of_eventuallyEq hev.symm
  exact ⟨hγ, ch_hasDerivAt_chart p hγ (hsrc s hs)⟩

/-- **The chart computation**: along a curve with `c` `C²` and `G = hRep g p` differentiable at
`c t`, `d/dt G(c)(c′, c′) = DG(c′)(c′, c′) + 2 G(c″, c′)`, which the Koszul identity at `w = c′`
makes `0`. -/
lemma ng_chart_energy_deriv (S : MSpacetime E N) (p : N) {c : ℝ → E} {t : ℝ}
    (hc : HasDerivAt c (deriv c t) t) (hc' : HasDerivAt (deriv c) (deriv (deriv c) t) t)
    (hG : DifferentiableAt ℝ (hRep S.g p) (c t))
    (hK : ∀ w, hRep S.g p (c t) (deriv (deriv c) t) w =
      -ng_kos (hRep S.g p) (c t) (deriv c t) (deriv c t) w) :
    HasDerivAt (fun s => hRep S.g p (c s) (deriv c s) (deriv c s)) 0 t := by
  have hB : HasDerivAt (fun s => hRep S.g p (c s)) (fderiv ℝ (hRep S.g p) (c t) (deriv c t)) t :=
    HasFDerivAt.comp_hasDerivAt (E := E →L[ℝ] E →L[ℝ] ℝ) (F := E) t hG.hasFDerivAt hc
  have h := (hB.clm_apply hc').clm_apply hc'
  refine h.congr_deriv ?_
  have hk := hK (deriv c t)
  simp only [ng_kos] at hk
  simp only [add_apply]
  rw [ng_hRep_symm S p (c t) (deriv c t) (deriv (deriv c) t)]
  linarith

/-- **The intrinsic `g(γ̇, γ̇)` has zero derivative at each `t ∈ [a, b]` of a geodesic** (with
`LocallyOneChart` for the `C¹` chart metric, and `γ` in `M`). -/
lemma ng_energy_hasDerivAt (hL : S.LocallyOneChart) {γ : ℝ → N} {a b : ℝ}
    (hγ : S.IsGeodesicOn γ a b) (hM : ∀ t ∈ Icc a b, γ t ∈ S.M) {t : ℝ} (ht : t ∈ Icc a b) :
    HasDerivAt (fun s => S.gE (γ s) (vel γ s) (vel γ s)) 0 t := by
  unfold IsGeodesicOn at hγ
  obtain ⟨ε, hε, hsrc, hC2, hK⟩ := hγ t ht
  set p := γ t
  set I := Ioo (t - ε) (t + ε) with hIdef
  have hI : IsOpen I := isOpen_Ioo
  have htI : t ∈ I := ⟨by linarith, by linarith⟩
  rw [show (2 : WithTop ℕ∞) = 1 + 1 from rfl, contDiffOn_succ_iff_deriv_of_isOpen hI] at hC2
  obtain ⟨hd, -, hC1⟩ := hC2
  have hd' : DifferentiableOn ℝ (deriv (ng_c E p γ)) I := hC1.differentiableOn one_ne_zero
  have hcd : ∀ s ∈ I, DifferentiableAt ℝ (ng_c E p γ) s := fun s hs =>
    (hd s hs).differentiableAt (hI.mem_nhds hs)
  -- the intrinsic value is the chart value on `I`
  have hev : (fun s => hRep S.g p (ng_c E p γ s) (deriv (ng_c E p γ) s) (deriv (ng_c E p γ) s))
      =ᶠ[𝓝 t] fun s => S.gE (γ s) (vel γ s) (vel γ s) := by
    filter_upwards [hI.mem_nhds htI] with s hs
    obtain ⟨-, hder⟩ := ng_vel_chart hI hs hsrc (hcd s hs)
    have hder' : HasDerivAt (ng_c E p γ) _ s := hder
    rw [hder'.deriv]
    exact (ld_h_eq_hRep S.g p (hsrc s hs) _ _).symm
  -- `G` is differentiable at `c t = φ_p(p)`
  obtain ⟨U, hU, hpU, -, hgU, -⟩ := hL p (hM t ht)
  have hG : DifferentiableAt ℝ (hRep S.g p) (ng_c E p γ t) :=
    (hgU.contDiffAt (hU.mem_nhds hpU)).differentiableAt one_ne_zero
  have h0 := ng_chart_energy_deriv S p (hcd t htI).hasDerivAt
    ((hd' t htI).differentiableAt (hI.mem_nhds htI)).hasDerivAt hG (hK t htI)
  exact h0.congr_of_eventuallyEq hev.symm

/-- **② `ng_energy_const`: energy conservation.** On a geodesic segment `γ` on `[a, b]` (in `M`,
`LocallyOneChart`), `t ↦ g(γ t)(γ̇, γ̇)` is constant on `[a, b]`. -/
theorem ng_energy_const (hL : S.LocallyOneChart) {γ : ℝ → N} {a b : ℝ}
    (hγ : S.IsGeodesicOn γ a b) (hM : ∀ t ∈ Icc a b, γ t ∈ S.M) :
    ∀ t ∈ Icc a b, S.gE (γ t) (vel γ t) (vel γ t) = S.gE (γ a) (vel γ a) (vel γ a) := by
  have hD := fun t ht => ng_energy_hasDerivAt hL hγ hM (t := t) ht
  refine constant_of_has_deriv_right_zero (fun t ht => (hD t ht).continuousAt.continuousWithinAt)
    fun t ht => (hD t (Ico_subset_Icc_self ht)).hasDerivWithinAt

/-- **③ `ng_cor_threefold_iii` (P1, l.176–180, 2iii):** a geodesic segment on `[a, b]` that is null
at one `t₀ ∈ [a, b]` is null at every `t ∈ [a, b]`. -/
theorem ng_cor_threefold_iii (hL : S.LocallyOneChart) {γ : ℝ → N} {a b : ℝ}
    (hγ : S.IsGeodesicOn γ a b) (hM : ∀ t ∈ Icc a b, γ t ∈ S.M) {t₀ : ℝ} (ht₀ : t₀ ∈ Icc a b)
    (h0 : S.gE (γ t₀) (vel γ t₀) (vel γ t₀) = 0) :
    ∀ t ∈ Icc a b, S.gE (γ t) (vel γ t) (vel γ t) = 0 := by
  intro t ht
  rw [ng_energy_const hL hγ hM t ht, ← ng_energy_const hL hγ hM t₀ ht₀, h0]

end MSpacetime

end NullGeodesic

/-! ### ④ The witness: the horizon generator of Schwarzschild's `∂J⁻(𝒥⁺)` on `W` -/

namespace NGModel
open Model NModel SEModel SXModel STModel Kruskal Manifold ContinuousLinearMap TopologicalSpace

set_option synthInstance.maxHeartbeats 400000

/-- **The horizon generator** `γ s = (0, V₀ + s)` (affine parameter `V`); off `V₀ + s > 0` a junk
value on the horizon. -/
noncomputable def ng_γ (V₀ : ℝ) (hV₀ : 0 < V₀) (s : ℝ) : seW :=
  if h : 0 < V₀ + s then ⟨((0 : ℝ), V₀ + s), ⟨h, by simp⟩⟩ else st_ev V₀ hV₀

lemma ng_γ_val {V₀ : ℝ} (hV₀ : 0 < V₀) {s : ℝ} (hs : 0 < V₀ + s) :
    (ng_γ V₀ hV₀ s : P) = ((0 : ℝ), V₀ + s) := by
  simp [ng_γ, hs]

lemma ng_γ_fst (V₀ : ℝ) (hV₀ : 0 < V₀) (s : ℝ) : (ng_γ V₀ hV₀ s : P).1 = 0 := by
  unfold ng_γ; split_ifs <;> rfl

/-- **`∂_V F = 0` on `U = 0`**: `F` depends on `UV` only. -/
lemma ng_FS_dV {M : ℝ} (hM : 0 < M) {y : P} (hy : y ∈ sk_kM) (hy1 : y.1 = 0) :
    fderiv ℝ (FS M) y ((0 : ℝ), (1 : ℝ)) = 0 := by
  have h1 : HasDerivAt (fun τ : ℝ => FS M (y + τ • ((0 : ℝ), (1 : ℝ))))
      (fderiv ℝ (FS M) y ((0 : ℝ), (1 : ℝ))) 0 := by
    have hl : HasDerivAt (fun τ : ℝ => y + τ • ((0 : ℝ), (1 : ℝ))) ((0 : ℝ), (1 : ℝ)) 0 := by
      simpa using ((hasDerivAt_id (0 : ℝ)).smul_const ((0 : ℝ), (1 : ℝ))).const_add y
    exact (st_FS_diff hM hy).hasFDerivAt.comp_hasDerivAt_of_eq (0 : ℝ) hl (by simp)
  have hconst : (fun τ : ℝ => FS M (y + τ • ((0 : ℝ), (1 : ℝ)))) = fun _ => FS M y := by
    funext τ
    obtain ⟨y1, y2⟩ := y
    simp only at hy1
    subst hy1
    simp [FS, rK]
  rw [hconst] at h1
  exact h1.unique (hasDerivAt_const _ _)

/-- **The Koszul form of `F • gM` vanishes at `U = 0` for `u = ∂_V`**: `DG(∂_V) = 0`, and
`gM(∂_V, ∂_V) = 0`. -/
lemma ng_kos_zero {M : ℝ} (hM : 0 < M) (p : seW) {y : P} (hy : y ∈ seWS) (hy1 : y.1 = 0) (w : P) :
    ng_kos (hRep (se_S hM).g p) y ((0 : ℝ), (1 : ℝ)) ((0 : ℝ), (1 : ℝ)) w = 0 := by
  have hf : fderiv ℝ (hRep (se_S hM).g p) y = fderiv ℝ (fun z => FS M z • gM) y :=
    (st_hRep_eventually hM p hy).fderiv_eq
  have hd := st_FS_diff hM (seWS_kM hy)
  simp only [ng_kos, hf, sq_smul_fderiv_apply gM hd, ng_FS_dV hM (seWS_kM hy) hy1, gM_apply]
  ring

/-- `hRep g (y)` is nondegenerate on `W` (`F > 0`, `gM` nondegenerate). -/
lemma ng_nondeg {M : ℝ} (hM : 0 < M) (p : seW) {y : P} (hy : y ∈ seWS) (z : P)
    (hz : ∀ w, hRep (se_S hM).g p y z w = 0) : z = 0 := by
  have hF : 0 < FS M y := sk_FS_pos hM (seWS_kM hy)
  have h1 := hz ((1 : ℝ), (0 : ℝ))
  have h2 := hz ((0 : ℝ), (1 : ℝ))
  rw [se_hRep hM p hy, smul_apply, smul_apply, smul_eq_mul, gM_apply] at h1 h2
  have a1 : z.2 = 0 := by
    have : FS M y * z.2 = 0 := by linarith
    exact (mul_eq_zero.1 this).resolve_left hF.ne'
  have a2 : z.1 = 0 := by
    have : FS M y * z.1 = 0 := by linarith
    exact (mul_eq_zero.1 this).resolve_left hF.ne'
  exact Prod.ext a2 a1

/-- The chart curve of `ng_γ` (in any chart of `W`, the inclusion) near `t ∈ [0, b]`. -/
lemma ng_c_eq {V₀ : ℝ} (hV₀ : 0 < V₀) (p : seW) {s : ℝ} (hs : 0 < V₀ + s) :
    ng_c P p (ng_γ V₀ hV₀) s = ((0 : ℝ), V₀ + s) := ng_γ_val hV₀ hs

/-- **`ng_γ` is a geodesic of Schwarzschild on `[0, b]`**: in `W`'s chart `c s = (0, V₀ + s)`,
`c″ = 0`, and the Koszul form vanishes on `U = 0`. -/
theorem ng_isGeodesicOn {M : ℝ} (hM : 0 < M) {V₀ : ℝ} (hV₀ : 0 < V₀) (b : ℝ) :
    (se_S hM).IsGeodesicOn (ng_γ V₀ hV₀) 0 b := by
  unfold MSpacetime.IsGeodesicOn
  intro t ht
  set p := ng_γ V₀ hV₀ t
  have hpos : ∀ s ∈ Ioo (t - V₀) (t + V₀), 0 < V₀ + s := fun s hs => by
    have := ht.1; have := hs.1; linarith
  have hI : IsOpen (Ioo (t - V₀) (t + V₀)) := isOpen_Ioo
  have hev : ∀ s ∈ Ioo (t - V₀) (t + V₀),
      ng_c P p (ng_γ V₀ hV₀) =ᶠ[𝓝 s] fun s => ((0 : ℝ), V₀ + s) := fun s hs => by
    filter_upwards [hI.mem_nhds hs] with s' hs' using ng_c_eq hV₀ p (hpos s' hs')
  have hd1 : ∀ s ∈ Ioo (t - V₀) (t + V₀), deriv (ng_c P p (ng_γ V₀ hV₀)) s = ((0 : ℝ), (1 : ℝ)) :=
    fun s hs => by
      rw [(hev s hs).deriv_eq]
      exact ((hasDerivAt_const s (0 : ℝ)).prodMk ((hasDerivAt_id s).const_add V₀)).deriv
  have hd2 : ∀ s ∈ Ioo (t - V₀) (t + V₀), deriv (deriv (ng_c P p (ng_γ V₀ hV₀))) s = 0 :=
    fun s hs => by
      have : deriv (ng_c P p (ng_γ V₀ hV₀)) =ᶠ[𝓝 s] fun _ => ((0 : ℝ), (1 : ℝ)) := by
        filter_upwards [hI.mem_nhds hs] with s' hs' using hd1 s' hs'
      rw [this.deriv_eq, deriv_const]
  refine ⟨V₀, hV₀, fun s _ => se_src _ _, ?_, fun s hs w => ?_⟩
  · have hcd : ContDiff ℝ 2 fun s : ℝ => ((0 : ℝ), V₀ + s) :=
      contDiff_const.prodMk (contDiff_const.add contDiff_id)
    exact hcd.contDiffOn.congr fun s hs => ng_c_eq hV₀ p (hpos s hs)
  · have hy : ng_c P p (ng_γ V₀ hV₀) s ∈ seWS := (ng_γ V₀ hV₀ s).2
    rw [hd2 s hs, hd1 s hs, map_zero, zero_apply,
      ng_kos_zero hM p hy (ng_γ_fst V₀ hV₀ s), neg_zero]

/-- **The velocity of `ng_γ` on `[0, b]` is `∂_V`** (the chart of `W` is the inclusion,
`se_dchart`). -/
lemma ng_vel {M : ℝ} (hM : 0 < M) {V₀ : ℝ} (hV₀ : 0 < V₀) {b t : ℝ} (ht : t ∈ Icc 0 b) :
    MSpacetime.vel (ng_γ V₀ hV₀) t = ((0 : ℝ), (1 : ℝ)) := by
  have hg := ng_isGeodesicOn hM hV₀ b
  unfold MSpacetime.IsGeodesicOn at hg
  obtain ⟨ε, hε, hsrc, hC2, -⟩ := hg t ht
  have hI : IsOpen (Ioo (t - ε) (t + ε)) := isOpen_Ioo
  have htI : t ∈ Ioo (t - ε) (t + ε) := ⟨by linarith, by linarith⟩
  have hd : DifferentiableAt ℝ (ng_c P (ng_γ V₀ hV₀ t) (ng_γ V₀ hV₀)) t :=
    (hC2.differentiableOn (by norm_num) t htI).differentiableAt (hI.mem_nhds htI)
  obtain ⟨-, hder⟩ := MSpacetime.ng_vel_chart hI htI hsrc hd
  have h3 : HasDerivAt (ng_c P (ng_γ V₀ hV₀ t) (ng_γ V₀ hV₀)) (MSpacetime.vel (ng_γ V₀ hV₀) t) t :=
    hder.congr_deriv (se_dchart _ _ _)
  have hpos : 0 < V₀ + t := by have := ht.1; linarith
  have hev : ng_c P (ng_γ V₀ hV₀ t) (ng_γ V₀ hV₀) =ᶠ[𝓝 t] fun s => ((0 : ℝ), V₀ + s) := by
    filter_upwards [Ioi_mem_nhds (show -V₀ < t by linarith)] with s hs
    exact ng_c_eq hV₀ _ (show 0 < V₀ + s by have : -V₀ < s := hs; linarith)
  have h2 : HasDerivAt (ng_c P (ng_γ V₀ hV₀ t) (ng_γ V₀ hV₀)) ((0 : ℝ), (1 : ℝ)) t :=
    ((hasDerivAt_const t (0 : ℝ)).prodMk ((hasDerivAt_id t).const_add V₀)).congr_of_eventuallyEq
      hev
  exact h3.unique h2

/-- **④ `ng_witness`.** Schwarzschild on `W` (`se_S`, `g = −F dU dV`), static observer at
`r₀ > 2M`, `𝓗⁺ = S.H J = ∂J⁻(𝒥⁺)` (`sx_prop_causal_alignment`). For `V₀ > 0`, `b ≥ 0`, the
horizon generator `γ s = (0, V₀ + s)` on `[0, b]` lies in `𝓗⁺`, is a geodesic (`IsGeodesicOn`,
with `c″ = 0 = −Γ(c)(c′, c′)` also in the inverted-`g` form `ng_Γ`), has velocity `∂_V`, is null at
`s = 0`, and hence (③) null on all of `[0, b]`. -/
theorem ng_witness {M : ℝ} (hM : 0 < M) {r₀ : ℝ} (hr₀ : 2 * M < r₀) {V₀ : ℝ} (hV₀ : 0 < V₀)
    {b : ℝ} (hb : 0 ≤ b) :
    (se_S hM).H (range (se_Ost hM hr₀)) = frontier ((sx_ext hM).ι ⁻¹' cz_St.JpastSet cz_scri) ∧
    (∀ s ∈ Icc 0 b, (ng_γ V₀ hV₀ s : P) = ((0 : ℝ), V₀ + s)) ∧
    ng_γ V₀ hV₀ '' Icc 0 b ⊆ (se_S hM).H (range (se_Ost hM hr₀)) ∧
    (se_S hM).IsGeodesicOn (ng_γ V₀ hV₀) 0 b ∧
    (∀ s ∈ Icc 0 b, ∀ p : seW,
      deriv (deriv (ng_c P p (ng_γ V₀ hV₀))) s = 0 ∧
      deriv (deriv (ng_c P p (ng_γ V₀ hV₀))) s =
        -ng_Γ (hRep (se_S hM).g p) (ng_c P p (ng_γ V₀ hV₀) s) (deriv (ng_c P p (ng_γ V₀ hV₀)) s)
          (deriv (ng_c P p (ng_γ V₀ hV₀)) s)) ∧
    (∀ s ∈ Icc 0 b, MSpacetime.vel (ng_γ V₀ hV₀) s = ((0 : ℝ), (1 : ℝ))) ∧
    (se_S hM).gE (ng_γ V₀ hV₀ 0) (MSpacetime.vel (ng_γ V₀ hV₀) 0) (MSpacetime.vel (ng_γ V₀ hV₀) 0) = 0 ∧
    ∀ s ∈ Icc 0 b, (se_S hM).gE (ng_γ V₀ hV₀ s) (MSpacetime.vel (ng_γ V₀ hV₀) s) (MSpacetime.vel (ng_γ V₀ hV₀) s) = 0 := by
  have hgeo := ng_isGeodesicOn hM hV₀ b
  have h0I : (0 : ℝ) ∈ Icc 0 b := ⟨le_rfl, hb⟩
  have hnull0 : (se_S hM).gE (ng_γ V₀ hV₀ 0) (MSpacetime.vel (ng_γ V₀ hV₀) 0) (MSpacetime.vel (ng_γ V₀ hV₀) 0) = 0 := by
    rw [ng_vel hM hV₀ h0I]
    show FS M _ * gM _ _ = 0
    rw [gM_apply]; ring
  -- the chart curve in any chart `p` of `W`
  have hloc : ∀ s ∈ Icc 0 b, ∀ p : seW,
      deriv (ng_c P p (ng_γ V₀ hV₀)) s = ((0 : ℝ), (1 : ℝ)) ∧
      deriv (deriv (ng_c P p (ng_γ V₀ hV₀))) s = 0 := by
    intro s hs p
    have hpos : 0 < V₀ + s := by have := hs.1; linarith
    have hev : ∀ s', 0 < V₀ + s' →
        ng_c P p (ng_γ V₀ hV₀) =ᶠ[𝓝 s'] fun s => ((0 : ℝ), V₀ + s) := fun s' hs' => by
      filter_upwards [Ioi_mem_nhds (show -V₀ < s' by linarith)] with u hu
      exact ng_c_eq hV₀ _ (show 0 < V₀ + u by have : -V₀ < u := hu; linarith)
    have hd1 : ∀ s', 0 < V₀ + s' → deriv (ng_c P p (ng_γ V₀ hV₀)) s' = ((0 : ℝ), (1 : ℝ)) :=
      fun s' hs' => by
        rw [(hev s' hs').deriv_eq]
        exact ((hasDerivAt_const s' (0 : ℝ)).prodMk ((hasDerivAt_id s').const_add V₀)).deriv
    refine ⟨hd1 s hpos, ?_⟩
    have : deriv (ng_c P p (ng_γ V₀ hV₀)) =ᶠ[𝓝 s] fun _ => ((0 : ℝ), (1 : ℝ)) := by
      filter_upwards [Ioi_mem_nhds (show -V₀ < s by linarith)] with u hu
      exact hd1 u (by have : -V₀ < u := hu; linarith)
    rw [this.deriv_eq, deriv_const]
  refine ⟨(sx_prop_causal_alignment hM hr₀).1, fun s hs => ng_γ_val hV₀ (by
      have := hs.1; linarith), ?_, hgeo, fun s hs p => ?_, fun s hs => ng_vel hM hV₀ hs, hnull0,
    MSpacetime.ng_cor_threefold_iii (se_locallyOneChart hM) hgeo (fun _ _ => mem_univ _) h0I
      hnull0⟩
  · rintro _ ⟨s, -, rfl⟩
    exact (st_mem_H hM hr₀ _).2 (ng_γ_fst V₀ hV₀ s)
  · obtain ⟨h1, h2⟩ := hloc s hs p
    refine ⟨h2, ?_⟩
    have hy : ng_c P p (ng_γ V₀ hV₀) s ∈ seWS := (ng_γ V₀ hV₀ s).2
    rw [h1, h2]
    have hz := ng_Γ_unique (ng_nondeg hM p hy) (z := 0) (u := ((0 : ℝ), (1 : ℝ)))
      (v := ((0 : ℝ), (1 : ℝ))) fun w => by
        rw [map_zero, zero_apply, ng_kos_zero hM p hy (ng_γ_fst V₀ hV₀ s)]
    rw [hz, neg_zero]

end NGModel


/-! ## NEW (campaign 110 ①): the locus `Σ = {UV = 1}`, the black-hole region and the slices -/

namespace KRModel
open Model SEModel Kruskal Manifold TopologicalSpace

/-- **The singular locus** `Σ = {UV = 1}` in the plane (`r → 0` there; it is not in `W`). -/
def kr_Sig : Set P := {p | p.1 * p.2 = 1}

/-- The product `UV` on `W`. -/
def kr_UV (x : seW) : ℝ := x.1.1 * x.1.2

variable {M : ℝ} (hM : 0 < M)

/-- **`J⁻(O)` on `W` is `{U < 0}`** (for any `a, k > 0`): `se_cau_iff` and the plane's
`se_K_JpastSet`. -/
theorem kr_JpastSet {a : ℝ} (ha : 0 < a) {k : ℝ} (hk : 0 < k) :
    (se_S hM).JpastSet (range (se_O ha k)) = {x | x.1.1 < 0} := by
  ext x
  simp only [MSpacetime.JpastSet, MSpacetime.Jpast, mem_iUnion, exists_prop]
  constructor
  · rintro ⟨_, ⟨τ, rfl⟩, h⟩
    have h : (se_S hM).Cau x (se_O ha k τ) := h
    rw [se_cau_iff] at h
    have : x.1 ∈ seK.JpastSet (range (sk_O a)) :=
      mem_iUnion₂.2 ⟨sk_O a (τ / (2 * k)), mem_range_self _, h⟩
    rw [se_K_JpastSet ha] at this
    exact this.1
  · intro hx
    have hmem : x.1 ∈ seK.JpastSet (range (sk_O a)) := by
      rw [se_K_JpastSet ha]; exact ⟨hx, x.2.1⟩
    obtain ⟨_, ⟨σ, rfl⟩, h⟩ := mem_iUnion₂.1 hmem
    refine ⟨se_O ha k (2 * k * σ), mem_range_self _, ?_⟩
    show (se_S hM).Cau x _
    rw [se_cau_iff]
    show seK.Cau x.1 (sk_O a (2 * k * σ / (2 * k)))
    rwa [mul_div_cancel_left₀ _ (by positivity)]

/-- **The black-hole region** `W ∖ J⁻(O)`, for the static observer at `r₀ > 2M`. -/
def kr_BH {r₀ : ℝ} (hr₀ : 2 * M < r₀) : Set seW :=
  univ \ (se_S hM).JpastSet (range (se_Ost hM hr₀))

/-- **`W ∖ J⁻(O) = {U ≥ 0} ∩ W`.** -/
theorem kr_BH_eq {r₀ : ℝ} (hr₀ : 2 * M < r₀) : kr_BH hM hr₀ = {x | 0 ≤ x.1.1} := by
  rw [kr_BH, se_Ost, kr_JpastSet hM _ (se_k_pos hM hr₀)]
  ext x; simp

lemma kr_BH_val {r₀ : ℝ} (hr₀ : 2 * M < r₀) :
    Subtype.val '' kr_BH hM hr₀ = {p : P | 0 ≤ p.1 ∧ 0 < p.2 ∧ p.1 * p.2 < 1} := by
  rw [kr_BH_eq]
  ext p; constructor
  · rintro ⟨x, hx, rfl⟩; exact ⟨hx, x.2.1, x.2.2⟩
  · rintro ⟨h1, h2, h3⟩; exact ⟨⟨p, h2, h3⟩, h1, rfl⟩

/-- **`kr_locus_BH`: `Σ ∩ {V > 0}` lies in the closure (in `P`) of the black-hole region, and
`U > 0` there.** `(U, tV) → (U, V)` as `t → 1⁻`, with `U·tV = t < 1`. -/
theorem kr_locus_BH {r₀ : ℝ} (hr₀ : 2 * M < r₀) {p : P} (hp : p ∈ kr_Sig) (hV : 0 < p.2) :
    p ∈ closure (Subtype.val '' kr_BH hM hr₀) ∧ 0 < p.1 := by
  have hp' : p.1 * p.2 = 1 := hp
  have hU : 0 < p.1 := by
    by_contra h; nlinarith [mul_nonpos_of_nonpos_of_nonneg (not_lt.1 h) hV.le]
  refine ⟨?_, hU⟩
  rw [kr_BH_val]
  have hf : Tendsto (fun t : ℝ => ((p.1, t * p.2) : P)) (𝓝[<] 1) (𝓝 p) := by
    have hc : Continuous (fun t : ℝ => ((p.1, t * p.2) : P)) := by fun_prop
    simpa using (hc.tendsto 1).mono_left nhdsWithin_le_nhds
  refine mem_closure_of_tendsto hf ?_
  filter_upwards [self_mem_nhdsWithin, Ioo_mem_nhdsLT (show (0:ℝ) < 1 by norm_num)] with t ht ht'
  have ht1 : t < 1 := ht
  refine ⟨hU.le, mul_pos ht'.1 hV, ?_⟩
  show p.1 * (t * p.2) < 1
  rw [show p.1 * (t * p.2) = t * (p.1 * p.2) by ring, hp', mul_one]; exact ht1

/-- **`Σ` meets the closure of `W` exactly in `Σ ∩ {V > 0}`.** -/
theorem kr_Sig_closure_W :
    kr_Sig ∩ closure (Subtype.val '' (univ : Set seW)) = kr_Sig ∩ {p : P | 0 < p.2} := by
  have hcl : closure (Subtype.val '' (univ : Set seW)) ⊆ {p : P | 0 ≤ p.2} :=
    closure_minimal (by rintro _ ⟨x, -, rfl⟩; exact x.2.1.le)
      (isClosed_le continuous_const continuous_snd)
  ext p; constructor
  · rintro ⟨hp, hc⟩
    refine ⟨hp, show (0:ℝ) < p.2 from (hcl hc).lt_of_ne fun h => ?_⟩
    have : p.1 * p.2 = 1 := hp
    rw [← h, mul_zero] at this; exact zero_ne_one this
  · rintro ⟨hp, hV⟩
    refine ⟨hp, closure_mono (image_mono (subset_univ _))
      (kr_locus_BH one_pos (r₀ := 4) (by norm_num) hp hV).1⟩

/-- **`kr_slice_far`: no finite exterior slice has `Σ` in its closure** (in `P`). Slices lie in
`D = {U < 0}`, whose image closes inside `{U ≤ 0, V ≥ 0}`, where `UV ≤ 0 < 1`. -/
theorem kr_slice_far {r₀ : ℝ} (hr₀ : 2 * M < r₀) (Θ : seW → ℝ) (τ : ℝ) :
    kr_Sig ∩ closure (Subtype.val '' (se_S hM).slice (range (se_Ost hM hr₀)) Θ τ) = ∅ := by
  have hD : (se_S hM).D (range (se_Ost hM hr₀)) = {x | x.1.1 < 0} :=
    (se_foundation hM (se_a_pos hM hr₀) (se_k_pos hM hr₀)).2.2.2.2.2.1
  have hsub : Subtype.val '' (se_S hM).slice (range (se_Ost hM hr₀)) Θ τ ⊆
      {p : P | p.1 ≤ 0 ∧ 0 ≤ p.2} := by
    rintro _ ⟨x, hx, rfl⟩
    have h1 : x ∈ (se_S hM).D (range (se_Ost hM hr₀)) := hx.1
    rw [hD] at h1
    exact ⟨le_of_lt h1, x.2.1.le⟩
  have hcl := closure_minimal hsub
    ((isClosed_le continuous_fst continuous_const).inter
      (isClosed_le continuous_const continuous_snd))
  ext p
  simp only [mem_inter_iff, mem_empty_iff_false, iff_false, not_and]
  intro hp hc
  obtain ⟨h1, h2⟩ := hcl hc
  have : p.1 * p.2 = 1 := hp
  nlinarith [mul_nonpos_of_nonpos_of_nonneg h1 h2]

/-- The filter "`UV → 1⁻` within `W`". -/
def kr_toSig : Filter seW := comap kr_UV (𝓝[<] 1)

/-- It is a genuine (non-trivial) approach: `(t, 1) ∈ W` has `UV = t`. -/
theorem kr_toSig_neBot : kr_toSig.NeBot := by
  rw [kr_toSig, comap_neBot_iff]
  intro t ht
  obtain ⟨s, hs, hs1⟩ :=
    Filter.nonempty_of_mem (inter_mem ht (self_mem_nhdsWithin : Iio (1:ℝ) ∈ 𝓝[<] 1))
  refine ⟨⟨((s, 1) : P), one_pos, by simpa using hs1⟩, ?_⟩
  show s * 1 ∈ t
  rwa [mul_one]

include hM in
lemma kr_rinv_to_zero : Tendsto (rinv M) (𝓝[>] (-1)) (𝓝[>] 0) := by
  rw [tendsto_nhdsWithin_iff]
  refine ⟨?_, ?_⟩
  · rw [tendsto_order]
    refine ⟨fun b hb => ?_, fun b hb => ?_⟩
    · filter_upwards [self_mem_nhdsWithin] with y hy
      exact hb.trans (rinv_spec hM hy).1
    · filter_upwards [Ioo_mem_nhdsGT (hK_gt hM hb)] with y hy
      obtain ⟨h0, h1⟩ := rinv_spec hM hy.1
      by_contra h
      have := (hK_strictMonoOn hM).monotoneOn (mem_Ici.2 hb.le) (mem_Ici.2 h0.le) (not_lt.1 h)
      rw [h1] at this; linarith [hy.2]
  · filter_upwards [self_mem_nhdsWithin] with y hy
    exact (rinv_spec hM hy).1

include hM in
/-- **`kr_r_to_zero`: `r → 0⁺` exactly as `UV → 1⁻` within `W`.** Forward: `r = h⁻¹(−UV)` and
`h⁻¹(y) → 0⁺` as `y → −1⁺` (`h(0) = −1`, `h` strictly increasing). Backward: `UV = −h(r)`, `h`
continuous with `h(0) = −1`, and `UV < 1` on all of `W`. -/
theorem kr_r_to_zero :
    Tendsto (se_r M) kr_toSig (𝓝[>] 0) ∧
    Tendsto kr_UV (comap (se_r M) (𝓝[>] 0)) (𝓝[<] 1) := by
  refine ⟨?_, ?_⟩
  · have h1 : Tendsto (fun x : seW => -kr_UV x) kr_toSig (𝓝[>] (-1)) := by
      have := (tendsto_comap (f := kr_UV) (x := 𝓝[<] (1:ℝ)))
      have hneg : Tendsto (fun y : ℝ => -y) (𝓝[<] 1) (𝓝[>] (-1)) := by
        simpa using (tendsto_neg_nhdsLT (a := (1:ℝ)))
      exact hneg.comp this
    exact (kr_rinv_to_zero hM).comp h1
  · rw [tendsto_nhdsWithin_iff]
    refine ⟨?_, Eventually.of_forall fun x => x.2.2⟩
    have hr : Tendsto (se_r M) (comap (se_r M) (𝓝[>] 0)) (𝓝 0) :=
      tendsto_comap.mono_right nhdsWithin_le_nhds
    have hh : Tendsto (fun x : seW => -hK M (se_r M x)) (comap (se_r M) (𝓝[>] 0)) (𝓝 1) := by
      have := ((continuous_hK (M := M)).tendsto 0).comp hr
      rw [hK_zero] at this
      simpa using this.neg
    refine hh.congr fun x => ?_
    have := (sk_rK_spec hM x.2.2).2
    show -hK M (rK M x.1) = x.1.1 * x.1.2
    rw [this, neg_neg]

end KRModel

section KrCurvature

variable {n : ℕ}

/-- The classical partial derivative `∂_c f(x)`: the derivative of `f` along the `c`-th coordinate line. -/
noncomputable def kr_pd (f : (Fin n → ℝ) → ℝ) (x : Fin n → ℝ) (c : Fin n) : ℝ :=
  deriv (fun t => f (Function.update x c t)) (x c)

/-- Christoffel symbols `Γ^a_{bc} = ½ g^{ad}(∂_b g_{dc} + ∂_c g_{db} − ∂_d g_{bc})`. -/
noncomputable def kr_Γ (g : (Fin n → ℝ) → Matrix (Fin n) (Fin n) ℝ) (x : Fin n → ℝ)
    (a b c : Fin n) : ℝ :=
  (1 / 2 : ℝ) * ∑ d, (g x)⁻¹ a d *
    (kr_pd (fun y => g y d c) x b + kr_pd (fun y => g y d b) x c - kr_pd (fun y => g y b c) x d)

/-- Riemann `R^a_{bcd} = ∂_c Γ^a_{db} − ∂_d Γ^a_{cb} + Γ^a_{ce}Γ^e_{db} − Γ^a_{de}Γ^e_{cb}`. -/
noncomputable def kr_Riem (g : (Fin n → ℝ) → Matrix (Fin n) (Fin n) ℝ) (x : Fin n → ℝ)
    (a b c d : Fin n) : ℝ :=
  kr_pd (fun y => kr_Γ g y a d b) x c - kr_pd (fun y => kr_Γ g y a c b) x d +
    ∑ e, (kr_Γ g x a c e * kr_Γ g x e d b - kr_Γ g x a d e * kr_Γ g x e c b)

/-- `R_{abcd} = g_{ae} R^e_{bcd}`. -/
noncomputable def kr_Rlow (g : (Fin n → ℝ) → Matrix (Fin n) (Fin n) ℝ) (x : Fin n → ℝ)
    (a b c d : Fin n) : ℝ :=
  ∑ e, g x a e * kr_Riem g x e b c d

/-- `R^{abcd} = g^{bb'} g^{cc'} g^{dd'} R^a_{b'c'd'}`. -/
noncomputable def kr_Rup (g : (Fin n → ℝ) → Matrix (Fin n) (Fin n) ℝ) (x : Fin n → ℝ)
    (a b c d : Fin n) : ℝ :=
  ∑ b', (g x)⁻¹ b b' * ∑ c', (g x)⁻¹ c c' * ∑ d', (g x)⁻¹ d d' * kr_Riem g x a b' c' d'

/-- **The Kretschmann scalar** `K = R_{abcd} R^{abcd}`. -/
noncomputable def kr_K (g : (Fin n → ℝ) → Matrix (Fin n) (Fin n) ℝ) (x : Fin n → ℝ) : ℝ :=
  ∑ a, ∑ b, ∑ c, ∑ d, kr_Rlow g x a b c d * kr_Rup g x a b c d

lemma kr_pd_const (C : ℝ) (x : Fin n → ℝ) (c : Fin n) : kr_pd (fun _ => C) x c = 0 := by
  simp [kr_pd]

lemma kr_pd_congr {f f' : (Fin n → ℝ) → ℝ} {x : Fin n → ℝ} {c : Fin n}
    (h : ∀ᶠ y in 𝓝 x, f y = f' y) : kr_pd f x c = kr_pd f' x c := by
  unfold kr_pd
  refine Filter.EventuallyEq.deriv_eq ?_
  have hc : ContinuousAt (fun t => Function.update x c t) (x c) :=
    (continuous_const.update c continuous_id).continuousAt
  have h' : ∀ᶠ y in 𝓝 (Function.update x c (x c)), f y = f' y := by
    rwa [Function.update_eq_self]
  exact hc.eventually h'

/-- **Sanity ①: a constant metric is flat**, `K = 0`. -/
theorem kr_K_const (G : Matrix (Fin n) (Fin n) ℝ) (x : Fin n → ℝ) : kr_K (fun _ => G) x = 0 := by
  have hΓ : ∀ y a b c, kr_Γ (fun _ => G) y a b c = 0 := by
    intro y a b c; simp [kr_Γ, kr_pd_const]
  have hR : ∀ a b c d, kr_Riem (fun _ => G) x a b c d = 0 := by
    intro a b c d; simp [kr_Riem, hΓ, kr_pd_const]
  simp [kr_K, kr_Rlow, hR]

section KrTrig

/-- `sin² θ`. -/
noncomputable def kr_s2 (t : ℝ) : ℝ := Real.sin t ^ 2
/-- `−sin θ cos θ`. -/
noncomputable def kr_nsc (t : ℝ) : ℝ := -(Real.sin t * Real.cos t)
/-- `cot θ = cos θ / sin θ`. -/
noncomputable def kr_cot (t : ℝ) : ℝ := Real.cos t / Real.sin t

lemma kr_hasDerivAt_s2 (t : ℝ) :
    HasDerivAt kr_s2 (2 * Real.sin t * Real.cos t) t := by
  have h := (Real.hasDerivAt_sin t).pow 2
  unfold kr_s2
  convert h using 1; push_cast; ring

lemma kr_deriv_s2 (t : ℝ) : deriv kr_s2 t = 2 * Real.sin t * Real.cos t :=
  (kr_hasDerivAt_s2 t).deriv

lemma kr_deriv_nsc (t : ℝ) :
    deriv kr_nsc t = Real.sin t ^ 2 - Real.cos t ^ 2 := by
  have h := ((Real.hasDerivAt_sin t).mul (Real.hasDerivAt_cos t)).neg
  refine (h.congr_deriv ?_).deriv
  ring

lemma kr_deriv_cot {t : ℝ} (ht : Real.sin t ≠ 0) :
    deriv kr_cot t = -(1 / Real.sin t ^ 2) := by
  have h := (Real.hasDerivAt_cos t).div (Real.hasDerivAt_sin t) ht
  refine (h.congr_deriv ?_).deriv
  field_simp
  have := Real.sin_sq_add_cos_sq t
  linear_combination (-1 : ℝ) * this

end KrTrig

section KrSphere

/-- The round 2-sphere of radius `ρ` in `(θ, φ)`: `g = ρ²(dθ² + sin²θ dφ²)`. -/
noncomputable def kr_sph (ρ : ℝ) (y : Fin 2 → ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  !![ρ ^ 2, 0; 0, ρ ^ 2 * kr_s2 (y 0)]

noncomputable def kr_sphI (ρ : ℝ) (y : Fin 2 → ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  !![1 / ρ ^ 2, 0; 0, 1 / (ρ ^ 2 * Real.sin (y 0) ^ 2)]

noncomputable def kr_sphΓ (y : Fin 2 → ℝ) : Fin 2 → Fin 2 → Fin 2 → ℝ :=
  ![![![0, 0], ![0, kr_nsc (y 0)]], ![![0, kr_cot (y 0)], ![kr_cot (y 0), 0]]]

variable {ρ : ℝ}

lemma kr_sph_inv (hρ : ρ ≠ 0) {y : Fin 2 → ℝ} (hy : Real.sin (y 0) ≠ 0) :
    (kr_sph ρ y)⁻¹ = kr_sphI ρ y := by
  refine Matrix.inv_eq_left_inv ?_
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, kr_sph, kr_sphI, kr_s2] <;> field_simp

lemma kr_sph_Γ (hρ : ρ ≠ 0) {y : Fin 2 → ℝ} (hy : Real.sin (y 0) ≠ 0) (a b c : Fin 2) :
    kr_Γ (kr_sph ρ) y a b c = kr_sphΓ y a b c := by
  simp only [kr_Γ, kr_sph_inv hρ hy]
  fin_cases a <;> fin_cases b <;> fin_cases c <;>
    simp [kr_pd, kr_sph, kr_sphI, kr_sphΓ, Function.update_apply, kr_deriv_s2]
  all_goals (try simp only [kr_nsc, kr_cot])
  all_goals field_simp

lemma kr_sph_D_open : IsOpen {y : Fin 2 → ℝ | Real.sin (y 0) ≠ 0} :=
  isOpen_ne_fun (Real.continuous_sin.comp (continuous_apply 0)) continuous_const

lemma kr_sph_pdΓ (hρ : ρ ≠ 0) {x : Fin 2 → ℝ} (hx : Real.sin (x 0) ≠ 0) (a b c d : Fin 2) :
    kr_pd (fun y => kr_Γ (kr_sph ρ) y a b c) x d = kr_pd (fun y => kr_sphΓ y a b c) x d :=
  kr_pd_congr (Filter.mem_of_superset (kr_sph_D_open.mem_nhds hx) fun _ hy => kr_sph_Γ hρ hy a b c)

/-- **Sanity ②: the round sphere of radius `ρ` has `K = 4/ρ⁴`.** -/
theorem kr_K_sphere (hρ : ρ ≠ 0) {x : Fin 2 → ℝ} (hx : Real.sin (x 0) ≠ 0) :
    kr_K (kr_sph ρ) x = 4 / ρ ^ 4 := by
  have hR : ∀ a b c d, kr_Riem (kr_sph ρ) x a b c d =
      ![![![![0, 0], ![0, 0]], ![![0, Real.sin (x 0) ^ 2], ![-Real.sin (x 0) ^ 2, 0]]],
        ![![![0, -1], ![1, 0]], ![![0, 0], ![0, 0]]]] a b c d := by
    intro a b c d
    simp only [kr_Riem, kr_sph_pdΓ hρ hx, kr_sph_Γ hρ hx]
    fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases d <;>
      simp [kr_pd, kr_sphΓ, kr_deriv_nsc, kr_deriv_cot hx]
    all_goals simp only [kr_nsc, kr_cot]
    all_goals field_simp
    all_goals linarith [Real.sin_sq_add_cos_sq (x 0)]
  simp only [kr_K, kr_Rlow, kr_Rup, hR, kr_sph_inv hρ hx]
  simp [Fin.sum_univ_two, kr_sph, kr_sphI, kr_s2]
  field_simp
  ring

end KrSphere
section KrWarped

/-! ### ③ The warped product `g = −F dU dV + R²(dθ² + sin²θ dφ²)` -/

/-- **Data of the warped metric**: `F, R` as functions of `(U, V)`, with their first and second partials
(one mixed partial each, so the mixed partials are symmetric by construction). -/
structure kr_WD where
  F : ℝ → ℝ → ℝ
  R : ℝ → ℝ → ℝ
  FU : ℝ → ℝ → ℝ
  FV : ℝ → ℝ → ℝ
  RU : ℝ → ℝ → ℝ
  RV : ℝ → ℝ → ℝ
  FUU : ℝ → ℝ → ℝ
  FUV : ℝ → ℝ → ℝ
  FVV : ℝ → ℝ → ℝ
  RUU : ℝ → ℝ → ℝ
  RUV : ℝ → ℝ → ℝ
  RVV : ℝ → ℝ → ℝ

/-- **The data is good on an open `Ω ⊆ ℝ²`**: `F, R > 0`, and each listed partial is the derivative
along the coordinate line (`∂_U ∂_V F = ∂_V ∂_U F = FUV`, likewise for `R`). -/
structure kr_WD.Good (D : kr_WD) (Ω : Set (ℝ × ℝ)) : Prop where
  isOpen : IsOpen Ω
  F_pos : ∀ u v, (u, v) ∈ Ω → 0 < D.F u v
  R_pos : ∀ u v, (u, v) ∈ Ω → 0 < D.R u v
  F_U : ∀ u v, (u, v) ∈ Ω → HasDerivAt (fun t => D.F t v) (D.FU u v) u
  F_V : ∀ u v, (u, v) ∈ Ω → HasDerivAt (fun t => D.F u t) (D.FV u v) v
  R_U : ∀ u v, (u, v) ∈ Ω → HasDerivAt (fun t => D.R t v) (D.RU u v) u
  R_V : ∀ u v, (u, v) ∈ Ω → HasDerivAt (fun t => D.R u t) (D.RV u v) v
  FU_U : ∀ u v, (u, v) ∈ Ω → HasDerivAt (fun t => D.FU t v) (D.FUU u v) u
  FU_V : ∀ u v, (u, v) ∈ Ω → HasDerivAt (fun t => D.FU u t) (D.FUV u v) v
  FV_U : ∀ u v, (u, v) ∈ Ω → HasDerivAt (fun t => D.FV t v) (D.FUV u v) u
  FV_V : ∀ u v, (u, v) ∈ Ω → HasDerivAt (fun t => D.FV u t) (D.FVV u v) v
  RU_U : ∀ u v, (u, v) ∈ Ω → HasDerivAt (fun t => D.RU t v) (D.RUU u v) u
  RU_V : ∀ u v, (u, v) ∈ Ω → HasDerivAt (fun t => D.RU u t) (D.RUV u v) v
  RV_U : ∀ u v, (u, v) ∈ Ω → HasDerivAt (fun t => D.RV t v) (D.RUV u v) u
  RV_V : ∀ u v, (u, v) ∈ Ω → HasDerivAt (fun t => D.RV u t) (D.RVV u v) v

namespace kr_WD
variable (D : kr_WD)

/-- `g_{UV} = −F/2`. -/
noncomputable def mh (u v : ℝ) : ℝ := -(D.F u v / 2)
/-- `R²`. -/
noncomputable def sq (u v : ℝ) : ℝ := D.R u v ^ 2
/-- `Γ^U_{UU} = F_U/F`. -/
noncomputable def q1 (u v : ℝ) : ℝ := D.FU u v / D.F u v
/-- `Γ^V_{VV} = F_V/F`. -/
noncomputable def q2 (u v : ℝ) : ℝ := D.FV u v / D.F u v
/-- `Γ^U_{θθ} = 2RR_V/F`. -/
noncomputable def q3 (u v : ℝ) : ℝ := 2 * D.R u v * D.RV u v / D.F u v
/-- `Γ^V_{θθ} = 2RR_U/F`. -/
noncomputable def q4 (u v : ℝ) : ℝ := 2 * D.R u v * D.RU u v / D.F u v
/-- `Γ^θ_{θU} = R_U/R`. -/
noncomputable def q5 (u v : ℝ) : ℝ := D.RU u v / D.R u v
/-- `Γ^θ_{θV} = R_V/R`. -/
noncomputable def q6 (u v : ℝ) : ℝ := D.RV u v / D.R u v

/-- **The warped metric** `g = −F dU dV + R²(dθ² + sin²θ dφ²)` in coordinates `(U, V, θ, φ)`. -/
noncomputable def gW (y : Fin 4 → ℝ) : Matrix (Fin 4) (Fin 4) ℝ :=
  !![0, D.mh (y 0) (y 1), 0, 0;
     D.mh (y 0) (y 1), 0, 0, 0;
     0, 0, D.sq (y 0) (y 1), 0;
     0, 0, 0, D.sq (y 0) (y 1) * kr_s2 (y 2)]

/-- Its inverse. -/
noncomputable def giW (y : Fin 4 → ℝ) : Matrix (Fin 4) (Fin 4) ℝ :=
  !![0, -2 / D.F (y 0) (y 1), 0, 0;
     -2 / D.F (y 0) (y 1), 0, 0, 0;
     0, 0, 1 / D.R (y 0) (y 1) ^ 2, 0;
     0, 0, 0, 1 / (D.R (y 0) (y 1) ^ 2 * Real.sin (y 2) ^ 2)]

/-- `∂_c g_{ab}`, indexed `c a b`. -/
noncomputable def dgW (y : Fin 4 → ℝ) : Fin 4 → Fin 4 → Fin 4 → ℝ :=
  ![!![0, -(D.FU (y 0) (y 1) / 2), 0, 0;
       -(D.FU (y 0) (y 1) / 2), 0, 0, 0;
       0, 0, 2 * D.R (y 0) (y 1) * D.RU (y 0) (y 1), 0;
       0, 0, 0, 2 * D.R (y 0) (y 1) * D.RU (y 0) (y 1) * kr_s2 (y 2)],
    !![0, -(D.FV (y 0) (y 1) / 2), 0, 0;
       -(D.FV (y 0) (y 1) / 2), 0, 0, 0;
       0, 0, 2 * D.R (y 0) (y 1) * D.RV (y 0) (y 1), 0;
       0, 0, 0, 2 * D.R (y 0) (y 1) * D.RV (y 0) (y 1) * kr_s2 (y 2)],
    !![0, 0, 0, 0; 0, 0, 0, 0; 0, 0, 0, 0;
       0, 0, 0, D.sq (y 0) (y 1) * (2 * Real.sin (y 2) * Real.cos (y 2))],
    0]

/-- The Christoffel symbols `Γ^a_{bc}` of `gW`, indexed `a b c`. -/
noncomputable def ΓW (y : Fin 4 → ℝ) : Fin 4 → Fin 4 → Fin 4 → ℝ :=
  ![!![D.q1 (y 0) (y 1), 0, 0, 0; 0, 0, 0, 0; 0, 0, D.q3 (y 0) (y 1), 0;
       0, 0, 0, D.q3 (y 0) (y 1) * kr_s2 (y 2)],
    !![0, 0, 0, 0; 0, D.q2 (y 0) (y 1), 0, 0; 0, 0, D.q4 (y 0) (y 1), 0;
       0, 0, 0, D.q4 (y 0) (y 1) * kr_s2 (y 2)],
    !![0, 0, D.q5 (y 0) (y 1), 0; 0, 0, D.q6 (y 0) (y 1), 0;
       D.q5 (y 0) (y 1), D.q6 (y 0) (y 1), 0, 0; 0, 0, 0, kr_nsc (y 2)],
    !![0, 0, 0, D.q5 (y 0) (y 1); 0, 0, 0, D.q6 (y 0) (y 1); 0, 0, 0, kr_cot (y 2);
       D.q5 (y 0) (y 1), D.q6 (y 0) (y 1), kr_cot (y 2), 0]]

/-- The domain `{(U, V) ∈ Ω, sin θ ≠ 0}`. -/
def dom (Ω : Set (ℝ × ℝ)) : Set (Fin 4 → ℝ) := {y | (y 0, y 1) ∈ Ω ∧ Real.sin (y 2) ≠ 0}

lemma dom_open {Ω : Set (ℝ × ℝ)} (hΩ : IsOpen Ω) : IsOpen (dom Ω) :=
  (hΩ.preimage ((continuous_apply 0).prodMk (continuous_apply 1))).inter
    (isOpen_ne_fun (Real.continuous_sin.comp (continuous_apply 2)) continuous_const)

end kr_WD
namespace kr_WD
variable {D : kr_WD} {Ω : Set (ℝ × ℝ)} (hG : D.Good Ω) {u v : ℝ} (h : (u, v) ∈ Ω)
include hG h

lemma d_mh_U : deriv (fun t => D.mh t v) u = -(D.FU u v / 2) :=
  ((hG.F_U u v h).div_const 2).neg.deriv
lemma d_mh_V : deriv (fun t => D.mh u t) v = -(D.FV u v / 2) :=
  ((hG.F_V u v h).div_const 2).neg.deriv
lemma d_sq_U : deriv (fun t => D.sq t v) u = 2 * D.R u v * D.RU u v := by
  refine (((hG.R_U u v h).pow 2).congr_deriv ?_).deriv; push_cast; ring
lemma d_sq_V : deriv (fun t => D.sq u t) v = 2 * D.R u v * D.RV u v := by
  refine (((hG.R_V u v h).pow 2).congr_deriv ?_).deriv; push_cast; ring
lemma d_q1_U : deriv (fun t => D.q1 t v) u =
    (D.FUU u v * D.F u v - D.FU u v * D.FU u v) / D.F u v ^ 2 :=
  ((hG.FU_U u v h).div (hG.F_U u v h) (hG.F_pos u v h).ne').deriv
lemma d_q1_V : deriv (fun t => D.q1 u t) v =
    (D.FUV u v * D.F u v - D.FU u v * D.FV u v) / D.F u v ^ 2 :=
  ((hG.FU_V u v h).div (hG.F_V u v h) (hG.F_pos u v h).ne').deriv
lemma d_q2_U : deriv (fun t => D.q2 t v) u =
    (D.FUV u v * D.F u v - D.FV u v * D.FU u v) / D.F u v ^ 2 :=
  ((hG.FV_U u v h).div (hG.F_U u v h) (hG.F_pos u v h).ne').deriv
lemma d_q2_V : deriv (fun t => D.q2 u t) v =
    (D.FVV u v * D.F u v - D.FV u v * D.FV u v) / D.F u v ^ 2 :=
  ((hG.FV_V u v h).div (hG.F_V u v h) (hG.F_pos u v h).ne').deriv
lemma d_q3_U : deriv (fun t => D.q3 t v) u =
    ((2 * D.RU u v * D.RV u v + 2 * D.R u v * D.RUV u v) * D.F u v -
      2 * D.R u v * D.RV u v * D.FU u v) / D.F u v ^ 2 := by
  refine ((((hG.R_U u v h).const_mul 2).mul (hG.RV_U u v h)).div (hG.F_U u v h)
    (hG.F_pos u v h).ne' |>.congr_deriv ?_).deriv
  simp only [Pi.mul_apply]
lemma d_q3_V : deriv (fun t => D.q3 u t) v =
    ((2 * D.RV u v * D.RV u v + 2 * D.R u v * D.RVV u v) * D.F u v -
      2 * D.R u v * D.RV u v * D.FV u v) / D.F u v ^ 2 := by
  refine ((((hG.R_V u v h).const_mul 2).mul (hG.RV_V u v h)).div (hG.F_V u v h)
    (hG.F_pos u v h).ne' |>.congr_deriv ?_).deriv
  simp only [Pi.mul_apply]
lemma d_q4_U : deriv (fun t => D.q4 t v) u =
    ((2 * D.RU u v * D.RU u v + 2 * D.R u v * D.RUU u v) * D.F u v -
      2 * D.R u v * D.RU u v * D.FU u v) / D.F u v ^ 2 := by
  refine ((((hG.R_U u v h).const_mul 2).mul (hG.RU_U u v h)).div (hG.F_U u v h)
    (hG.F_pos u v h).ne' |>.congr_deriv ?_).deriv
  simp only [Pi.mul_apply]
lemma d_q4_V : deriv (fun t => D.q4 u t) v =
    ((2 * D.RV u v * D.RU u v + 2 * D.R u v * D.RUV u v) * D.F u v -
      2 * D.R u v * D.RU u v * D.FV u v) / D.F u v ^ 2 := by
  refine ((((hG.R_V u v h).const_mul 2).mul (hG.RU_V u v h)).div (hG.F_V u v h)
    (hG.F_pos u v h).ne' |>.congr_deriv ?_).deriv
  simp only [Pi.mul_apply]
lemma d_q5_U : deriv (fun t => D.q5 t v) u =
    (D.RUU u v * D.R u v - D.RU u v * D.RU u v) / D.R u v ^ 2 :=
  ((hG.RU_U u v h).div (hG.R_U u v h) (hG.R_pos u v h).ne').deriv
lemma d_q5_V : deriv (fun t => D.q5 u t) v =
    (D.RUV u v * D.R u v - D.RU u v * D.RV u v) / D.R u v ^ 2 :=
  ((hG.RU_V u v h).div (hG.R_V u v h) (hG.R_pos u v h).ne').deriv
lemma d_q6_U : deriv (fun t => D.q6 t v) u =
    (D.RUV u v * D.R u v - D.RV u v * D.RU u v) / D.R u v ^ 2 :=
  ((hG.RV_U u v h).div (hG.R_U u v h) (hG.R_pos u v h).ne').deriv
lemma d_q6_V : deriv (fun t => D.q6 u t) v =
    (D.RVV u v * D.R u v - D.RV u v * D.RV u v) / D.R u v ^ 2 :=
  ((hG.RV_V u v h).div (hG.R_V u v h) (hG.R_pos u v h).ne').deriv

end kr_WD

namespace kr_WD
variable {D : kr_WD} {Ω : Set (ℝ × ℝ)} (hG : D.Good Ω)

include hG in
lemma gW_inv {y : Fin 4 → ℝ} (hy : y ∈ dom Ω) : (D.gW y)⁻¹ = D.giW y := by
  have hF := (hG.F_pos _ _ hy.1).ne'
  have hR := (hG.R_pos _ _ hy.1).ne'
  have hs := hy.2
  refine Matrix.inv_eq_left_inv ?_
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Fin.sum_univ_four, gW, giW, mh, sq, kr_s2] <;> field_simp

include hG in
lemma gW_pd {y : Fin 4 → ℝ} (hy : y ∈ dom Ω) (c a b : Fin 4) :
    kr_pd (fun z => D.gW z a b) y c = D.dgW y c a b := by
  have h := hy.1
  fin_cases c <;> fin_cases a <;> fin_cases b <;>
    simp [kr_pd, gW, dgW, d_mh_U hG h, d_mh_V hG h, d_sq_U hG h, d_sq_V hG h, kr_deriv_s2]

include hG in
lemma Γ_eq {y : Fin 4 → ℝ} (hy : y ∈ dom Ω) (a b c : Fin 4) :
    kr_Γ D.gW y a b c = D.ΓW y a b c := by
  have hF := (hG.F_pos _ _ hy.1).ne'
  have hR := (hG.R_pos _ _ hy.1).ne'
  have hs := hy.2
  simp only [kr_Γ, gW_inv hG hy, gW_pd hG hy]
  fin_cases a <;> fin_cases b <;> fin_cases c <;>
    simp [Fin.sum_univ_four, giW, dgW, ΓW]
  all_goals (try simp only [q1, q2, q3, q4, q5, q6, sq, kr_s2, kr_nsc, kr_cot])
  all_goals (try field_simp)
  all_goals ring

include hG in
lemma pdΓ_eq {x : Fin 4 → ℝ} (hx : x ∈ dom Ω) (a b c d : Fin 4) :
    kr_pd (fun y => kr_Γ D.gW y a b c) x d = kr_pd (fun y => D.ΓW y a b c) x d :=
  kr_pd_congr (Filter.mem_of_superset ((dom_open hG.isOpen).mem_nhds hx)
    fun _ hy => Γ_eq hG hy a b c)

end kr_WD
/-- **The non-zero components** `R^a_{bcd}` of the warped metric (40 of 256), as a table in the values of the data
and `s = sin θ` (`F_UU`, `F_VV` and `cos θ` drop out). -/
noncomputable def kr_RWv (F R FU FV RU RV FUV RUU RUV RVV s : ℝ) :
    Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ :=
  ![![![![0, (-(F*FUV - FU*FV)/F^2), 0, 0], ![((F*FUV - FU*FV)/F^2), 0, 0, 0], ![0, 0, 0, 0], ![0, 0,
    0, 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, 0, (2*R*RUV/F), 0],
    ![0, 0, (2*R*(F*RVV - FV*RV)/F^2), 0], ![(-2*R*RUV/F), (-2*R*(F*RVV - FV*RV)/F^2), 0, 0], ![0, 0,
    0, 0]], ![![0, 0, 0, (2*R*RUV*s^2/F)], ![0, 0, 0, (2*R*s^2*(F*RVV - FV*RV)/F^2)], ![0, 0, 0, 0],
    ![(-2*R*RUV*s^2/F), (-2*R*s^2*(F*RVV - FV*RV)/F^2), 0, 0]]], ![![![0, 0, 0, 0], ![0, 0, 0, 0],
    ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, ((F*FUV - FU*FV)/F^2), 0, 0], ![(-(F*FUV - FU*FV)/F^2), 0,
    0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, 0, (2*R*(F*RUU - FU*RU)/F^2), 0], ![0, 0,
    (2*R*RUV/F), 0], ![(-2*R*(F*RUU - FU*RU)/F^2), (-2*R*RUV/F), 0, 0], ![0, 0, 0, 0]], ![![0, 0, 0,
    (2*R*s^2*(F*RUU - FU*RU)/F^2)], ![0, 0, 0, (2*R*RUV*s^2/F)], ![0, 0, 0, 0],
    ![(-2*R*s^2*(F*RUU - FU*RU)/F^2), (-2*R*RUV*s^2/F), 0, 0]]], ![![![0, 0, ((F*RUU - FU*RU)/(F*R)),
    0], ![0, 0, (RUV/R), 0], ![(-(F*RUU - FU*RU)/(F*R)), (-RUV/R), 0, 0], ![0, 0, 0, 0]], ![![0, 0,
    (RUV/R), 0], ![0, 0, ((F*RVV - FV*RV)/(F*R)), 0], ![(-RUV/R), (-(F*RVV - FV*RV)/(F*R)), 0, 0],
    ![0, 0, 0, 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, 0, 0, 0],
    ![0, 0, 0, 0], ![0, 0, 0, (s^2*(F + 4*RU*RV)/F)], ![0, 0, (-s^2*(F + 4*RU*RV)/F), 0]]], ![![![0,
    0, 0, ((F*RUU - FU*RU)/(F*R))], ![0, 0, 0, (RUV/R)], ![0, 0, 0, 0], ![(-(F*RUU - FU*RU)/(F*R)),
    (-RUV/R), 0, 0]], ![![0, 0, 0, (RUV/R)], ![0, 0, 0, ((F*RVV - FV*RV)/(F*R))], ![0, 0, 0, 0],
    ![(-RUV/R), (-(F*RVV - FV*RV)/(F*R)), 0, 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0,
    (-(F + 4*RU*RV)/F)], ![0, 0, ((F + 4*RU*RV)/F), 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0,
    0], ![0, 0, 0, 0]]]]

namespace kr_WD
variable {D : kr_WD} {Ω : Set (ℝ × ℝ)} (hG : D.Good Ω)

/-- The Riemann table at `x`. -/
noncomputable def Rv (D : kr_WD) (x : Fin 4 → ℝ) : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ :=
  kr_RWv (D.F (x 0) (x 1)) (D.R (x 0) (x 1)) (D.FU (x 0) (x 1)) (D.FV (x 0) (x 1))
    (D.RU (x 0) (x 1)) (D.RV (x 0) (x 1)) (D.FUV (x 0) (x 1))
    (D.RUU (x 0) (x 1)) (D.RUV (x 0) (x 1)) (D.RVV (x 0) (x 1)) (Real.sin (x 2))

set_option maxHeartbeats 4000000 in
include hG in
/-- **The Riemann tensor of the warped metric**, component by component (all 256). -/
lemma Riem_eq {x : Fin 4 → ℝ} (hx : x ∈ dom Ω) (a b c d : Fin 4) :
    kr_Riem D.gW x a b c d = D.Rv x a b c d := by
  have h := hx.1
  have hF := (hG.F_pos _ _ h).ne'
  have hR := (hG.R_pos _ _ h).ne'
  have hs := hx.2
  simp only [kr_Riem, pdΓ_eq hG hx, Γ_eq hG hx]
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases d <;>
    simp [kr_pd, ΓW, Rv, kr_RWv, Fin.sum_univ_four, d_q1_U hG h, d_q1_V hG h, d_q2_U hG h,
      d_q2_V hG h, d_q3_U hG h, d_q3_V hG h, d_q4_U hG h, d_q4_V hG h, d_q5_U hG h, d_q5_V hG h,
      d_q6_U hG h, d_q6_V hG h, kr_deriv_s2, kr_deriv_nsc, kr_deriv_cot hs]
  all_goals (try simp only [q1, q2, q3, q4, q5, q6, kr_s2, kr_nsc, kr_cot])
  all_goals (try field_simp)
  all_goals first
    | ring1
    | linear_combination (D.F (x 0) (x 1)) * Real.sin_sq_add_cos_sq (x 2)
    | linear_combination (-D.F (x 0) (x 1)) * Real.sin_sq_add_cos_sq (x 2)

end kr_WD

namespace kr_WD
variable {D : kr_WD} {Ω : Set (ℝ × ℝ)} (hG : D.Good Ω)

/-- The partner index `σ = (U ↔ V)` of the (block-)diagonal metric. -/
def σ : Fin 4 → Fin 4 := ![1, 0, 2, 3]

/-- Lowering an index with `gW` picks one term. -/
lemma gW_row (x : Fin 4 → ℝ) (a : Fin 4) (f : Fin 4 → ℝ) :
    ∑ e, D.gW x a e * f e =
      ![D.mh (x 0) (x 1), D.mh (x 0) (x 1), D.sq (x 0) (x 1),
        D.sq (x 0) (x 1) * kr_s2 (x 2)] a * f (σ a) := by
  fin_cases a <;> simp [Fin.sum_univ_four, gW, σ]

/-- Raising an index with `giW` picks one term. -/
lemma giW_row (x : Fin 4 → ℝ) (a : Fin 4) (f : Fin 4 → ℝ) :
    ∑ e, D.giW x a e * f e =
      ![-2 / D.F (x 0) (x 1), -2 / D.F (x 0) (x 1), 1 / D.R (x 0) (x 1) ^ 2,
        1 / (D.R (x 0) (x 1) ^ 2 * Real.sin (x 2) ^ 2)] a * f (σ a) := by
  fin_cases a <;> simp [Fin.sum_univ_four, giW, σ]

/-- `k₂`, the scalar curvature of the 2-metric `−F dU dV`: `4(F F_UV − F_U F_V)/F³`. -/
noncomputable def k2 (D : kr_WD) (u v : ℝ) : ℝ :=
  4 * (D.FUV u v * D.F u v - D.FU u v * D.FV u v) / D.F u v ^ 3

/-- `|∇R|² = −(4/F) R_U R_V` for the 2-metric. -/
noncomputable def gradR2 (D : kr_WD) (u v : ℝ) : ℝ := -(4 / D.F u v) * D.RU u v * D.RV u v

/-- `|∇∇R|² = (8/F²)(∇_U∇_U R · ∇_V∇_V R + (∇_U∇_V R)²)`, with `∇_U∇_U R = R_UU − (F_U/F) R_U`,
`∇_V∇_V R = R_VV − (F_V/F) R_V`, `∇_U∇_V R = R_UV`. -/
noncomputable def hessR2 (D : kr_WD) (u v : ℝ) : ℝ :=
  8 / D.F u v ^ 2 * ((D.RUU u v - D.FU u v / D.F u v * D.RU u v) *
    (D.RVV u v - D.FV u v / D.F u v * D.RV u v) + D.RUV u v ^ 2)

set_option maxHeartbeats 1000000 in
include hG in
/-- **③ `kr_warped`: the Kretschmann scalar of `g = −F dU dV + R²(dθ² + sin²θ dφ²)`** (BUILT, all 256
components): at every `(U, V, θ, φ)` with `(U, V) ∈ Ω` and `sin θ ≠ 0`,
`K = k₂² + 8|∇∇R|²/R² + 4(1 − |∇R|²)²/R⁴`. The `θ`-dependence cancels. -/
theorem kr_warped {x : Fin 4 → ℝ} (hx : x ∈ dom Ω) :
    kr_K D.gW x = D.k2 (x 0) (x 1) ^ 2 + 8 * D.hessR2 (x 0) (x 1) / D.R (x 0) (x 1) ^ 2 +
      4 * (1 - D.gradR2 (x 0) (x 1)) ^ 2 / D.R (x 0) (x 1) ^ 4 := by
  have h := hx.1
  have hF := (hG.F_pos _ _ h).ne'
  have hR := (hG.R_pos _ _ h).ne'
  have hs := hx.2
  simp only [kr_K, kr_Rlow, kr_Rup, gW_inv hG hx, gW_row, giW_row, Riem_eq hG hx]
  simp [Fin.sum_univ_four, σ, Rv, kr_RWv]
  simp only [k2, hessR2, gradR2, mh, sq, kr_s2]
  field_simp
  ring

end kr_WD
end KrWarped
end KrCurvature

/-! ## NEW (campaign 110 ④⑤): Schwarzschild's Kretschmann scalar `48M²/r⁶` and its blow-up at `Σ` -/

namespace KRModel
open Model SEModel Kruskal

/-- `h″(r) = e^{r/2M}(1 + r/2M)/4M²`. -/
noncomputable def kr_hpp (M x : ℝ) : ℝ := Real.exp (x / (2 * M)) / (4 * M ^ 2) * (1 + x / (2 * M))
/-- `φ(r) = (32M³/r) e^{−r/2M}`, so `F = φ ∘ r`. -/
noncomputable def kr_φ (M x : ℝ) : ℝ := 32 * M ^ 3 / x * Real.exp (-x / (2 * M))
/-- `φ′(r) = −φ(r)(1/r + 1/2M)`. -/
noncomputable def kr_φ1 (M x : ℝ) : ℝ := -(kr_φ M x * (1 / x + 1 / (2 * M)))
/-- `φ″(r) = φ(r)((1/r + 1/2M)² + 1/r²)`. -/
noncomputable def kr_φ2 (M x : ℝ) : ℝ := kr_φ M x * ((1 / x + 1 / (2 * M)) ^ 2 + 1 / x ^ 2)

variable {M : ℝ} (hM : 0 < M)

lemma kr_hasDerivAt_hK' (x : ℝ) : HasDerivAt (hK' M) (kr_hpp M x) x := by
  have h1 : HasDerivAt (fun x : ℝ => x / (2 * M)) (1 / (2 * M)) x := (hasDerivAt_id x).div_const _
  have h := ((hasDerivAt_id x).div_const (4 * M ^ 2)).mul h1.exp
  refine h.congr_deriv ?_
  simp only [kr_hpp, id]; ring

include hM in
lemma kr_hasDerivAt_φ {x : ℝ} (hx : 0 < x) : HasDerivAt (kr_φ M) (kr_φ1 M x) x := by
  have h1 : HasDerivAt (fun x : ℝ => -x / (2 * M)) (-1 / (2 * M)) x :=
    (hasDerivAt_id x).neg.div_const _
  have h := ((hasDerivAt_const x (32 * M ^ 3)).div (hasDerivAt_id x) hx.ne').mul h1.exp
  refine h.congr_deriv ?_
  simp only [kr_φ1, kr_φ, id, Pi.div_apply]
  field_simp; ring

include hM in
lemma kr_hasDerivAt_φ1 {x : ℝ} (hx : 0 < x) : HasDerivAt (kr_φ1 M) (kr_φ2 M x) x := by
  have h2 : HasDerivAt (fun x : ℝ => 1 / x + 1 / (2 * M)) (-1 / x ^ 2) x := by
    have := ((hasDerivAt_const x (1:ℝ)).div (hasDerivAt_id x) hx.ne').add_const (1 / (2 * M))
    refine this.congr_deriv ?_; simp
  have h := ((kr_hasDerivAt_φ hM hx).mul h2).neg
  refine h.congr_deriv ?_
  simp only [kr_φ2, kr_φ1]
  field_simp; ring

/-- **The Schwarzschild data** on `{UV < 1}`: `F = (32M³/r)e^{−r/2M}`, `R = r(U, V)`, with
`r_U = −V/h′(r)`, `r_V = −U/h′(r)` and the second partials they imply. -/
noncomputable def kr_SD (M : ℝ) : kr_WD where
  F := fun u v => FS M (u, v)
  R := fun u v => rK M (u, v)
  RU := fun u v => -v / hK' M (rK M (u, v))
  RV := fun u v => -u / hK' M (rK M (u, v))
  FU := fun u v => kr_φ1 M (rK M (u, v)) * (-v / hK' M (rK M (u, v)))
  FV := fun u v => kr_φ1 M (rK M (u, v)) * (-u / hK' M (rK M (u, v)))
  RUU := fun u v => -(v ^ 2) * kr_hpp M (rK M (u, v)) / hK' M (rK M (u, v)) ^ 3
  RUV := fun u v => -1 / hK' M (rK M (u, v)) -
    u * v * kr_hpp M (rK M (u, v)) / hK' M (rK M (u, v)) ^ 3
  RVV := fun u v => -(u ^ 2) * kr_hpp M (rK M (u, v)) / hK' M (rK M (u, v)) ^ 3
  FUU := fun u v => kr_φ2 M (rK M (u, v)) * (-v / hK' M (rK M (u, v))) ^ 2 +
    kr_φ1 M (rK M (u, v)) * (-(v ^ 2) * kr_hpp M (rK M (u, v)) / hK' M (rK M (u, v)) ^ 3)
  FUV := fun u v => kr_φ2 M (rK M (u, v)) * (-v / hK' M (rK M (u, v))) *
      (-u / hK' M (rK M (u, v))) +
    kr_φ1 M (rK M (u, v)) * (-1 / hK' M (rK M (u, v)) -
      u * v * kr_hpp M (rK M (u, v)) / hK' M (rK M (u, v)) ^ 3)
  FVV := fun u v => kr_φ2 M (rK M (u, v)) * (-u / hK' M (rK M (u, v))) ^ 2 +
    kr_φ1 M (rK M (u, v)) * (-(u ^ 2) * kr_hpp M (rK M (u, v)) / hK' M (rK M (u, v)) ^ 3)

section SD
variable {u v : ℝ} (hp : (u, v) ∈ sk_kM)
include hM hp

lemma kr_r_U : HasDerivAt (fun t => rK M (t, v)) (-v / hK' M (rK M (u, v))) u := by
  have h1 : HasDerivAt (fun t : ℝ => -(t * v)) (-v) u :=
    ((hasDerivAt_id' u).mul_const v).neg.congr_deriv (by ring)
  have := (rinv_hasDerivAt hM (sk_kM_UV hp)).comp u h1
  exact this.congr_deriv (by simp only [rK]; ring)

lemma kr_r_V : HasDerivAt (fun t => rK M (u, t)) (-u / hK' M (rK M (u, v))) v := by
  have h1 : HasDerivAt (fun t : ℝ => -(u * t)) (-u) v :=
    ((hasDerivAt_id' v).const_mul u).neg.congr_deriv (by ring)
  have := (rinv_hasDerivAt hM (sk_kM_UV hp)).comp v h1
  exact this.congr_deriv (by simp only [rK]; ring)

lemma kr_r_pos : 0 < rK M (u, v) := (sk_rK_spec hM hp).1

lemma kr_hp_ne : hK' M (rK M (u, v)) ≠ 0 := (SRModel.sa_hK'_pos hM (kr_r_pos hM hp)).ne'

lemma kr_comp_U {g : ℝ → ℝ} {g' : ℝ} (hg : HasDerivAt g g' (rK M (u, v))) :
    HasDerivAt (fun t => g (rK M (t, v))) (g' * (-v / hK' M (rK M (u, v)))) u :=
  hg.comp u (kr_r_U hM hp)

lemma kr_comp_V {g : ℝ → ℝ} {g' : ℝ} (hg : HasDerivAt g g' (rK M (u, v))) :
    HasDerivAt (fun t => g (rK M (u, t))) (g' * (-u / hK' M (rK M (u, v)))) v :=
  hg.comp v (kr_r_V hM hp)

end SD

include hM in
/-- **The Schwarzschild data is good on `{UV < 1}`.** -/
theorem kr_SD_good : (kr_SD M).Good sk_kM := by
  refine
    { isOpen := sk_kM_open
      F_pos := fun u v hp => sk_FS_pos hM hp
      R_pos := fun u v hp => kr_r_pos hM hp
      F_U := fun u v hp => kr_comp_U hM hp (kr_hasDerivAt_φ hM (kr_r_pos hM hp))
      F_V := fun u v hp => kr_comp_V hM hp (kr_hasDerivAt_φ hM (kr_r_pos hM hp))
      R_U := fun u v hp => kr_r_U hM hp
      R_V := fun u v hp => kr_r_V hM hp
      FU_U := fun u v hp => ?_
      FU_V := fun u v hp => ?_
      FV_U := fun u v hp => ?_
      FV_V := fun u v hp => ?_
      RU_U := fun u v hp => ?_
      RU_V := fun u v hp => ?_
      RV_U := fun u v hp => ?_
      RV_V := fun u v hp => ?_ }
  all_goals
    have hne := kr_hp_ne hM hp
    have hU := kr_comp_U hM hp (kr_hasDerivAt_hK' (M := M) (rK M (u, v)))
    have hV := kr_comp_V hM hp (kr_hasDerivAt_hK' (M := M) (rK M (u, v)))
    have φU := kr_comp_U hM hp (kr_hasDerivAt_φ1 hM (kr_r_pos hM hp))
    have φV := kr_comp_V hM hp (kr_hasDerivAt_φ1 hM (kr_r_pos hM hp))
    simp only [kr_SD]
  · exact (φU.mul ((hasDerivAt_const u (-v)).div hU hne)).congr_deriv
      (by simp only [Pi.div_apply]; field_simp; ring)
  · exact (φV.mul ((hasDerivAt_id v).neg.div hV hne)).congr_deriv
      (by simp only [Pi.div_apply, Pi.neg_apply, id]; field_simp)
  · exact (φU.mul ((hasDerivAt_id u).neg.div hU hne)).congr_deriv
      (by simp only [Pi.div_apply, Pi.neg_apply, id]; field_simp)
  · exact (φV.mul ((hasDerivAt_const v (-u)).div hV hne)).congr_deriv
      (by simp only [Pi.div_apply]; field_simp; ring)
  · exact ((hasDerivAt_const u (-v)).div hU hne).congr_deriv (by field_simp; ring)
  · exact ((hasDerivAt_id v).neg.div hV hne).congr_deriv (by simp only [Pi.neg_apply, id]; field_simp)
  · exact ((hasDerivAt_id u).neg.div hU hne).congr_deriv (by simp only [Pi.neg_apply, id]; field_simp)
  · exact ((hasDerivAt_const v (-u)).div hV hne).congr_deriv (by field_simp; ring)

end KRModel


namespace KRModel
open Model SEModel Kruskal

variable {M : ℝ} (hM : 0 < M)

include hM in
/-- **④ `kr_schwarzschild`: the Kretschmann scalar of Schwarzschild is `48M²/r⁶`** (BUILT), at every
`(U, V, θ, φ)` with `UV < 1` (so on `W` and on all of `{UV < 1}`) and `sin θ ≠ 0`, for
`g = −F dU dV + r²(dθ² + sin²θ dφ²)` with Kruskal's `F = (32M³/r) e^{−r/2M}` and `r = r(UV)`. From
`kr_warped`: `|∇r|² = 1 − 2M/r`, `k₂ = 4M/r³`, `|∇∇r|² = 2M²/r⁴` (using `UV = (1 − r/2M) e^{r/2M}`). -/
theorem kr_schwarzschild {x : Fin 4 → ℝ} (hx : (x 0, x 1) ∈ sk_kM) (hs : Real.sin (x 2) ≠ 0) :
    kr_K (kr_SD M).gW x = 48 * M ^ 2 / rK M (x 0, x 1) ^ 6 := by
  rw [kr_WD.kr_warped (kr_SD_good hM) ⟨hx, hs⟩]
  set u := x 0
  set v := x 1
  have hr := kr_r_pos hM hx
  set r := rK M (u, v) with hr_def
  set E := Real.exp (r / (2 * M)) with hE_def
  have hE : 0 < E := Real.exp_pos _
  have huv : u * v = (1 - r / (2 * M)) * E := by
    have := (sk_rK_spec hM hx).2
    simp only [hK] at this
    rw [← hr_def, ← hE_def] at this
    linear_combination this
  have hEi : Real.exp (-r / (2 * M)) = E⁻¹ := by rw [neg_div, Real.exp_neg]
  have hφ : FS M (u, v) = 32 * M ^ 3 / r * E⁻¹ := by
    simp only [FS]; rw [← hr_def, hEi]
  have hhp : hK' M r = r / (4 * M ^ 2) * E := rfl
  have hhpp : kr_hpp M r = E / (4 * M ^ 2) * (1 + r / (2 * M)) := rfl
  have hφ1 : kr_φ1 M r = -(32 * M ^ 3 / r * E⁻¹ * (1 / r + 1 / (2 * M))) := by
    simp only [kr_φ1, kr_φ]; rw [hEi]
  have hφ2 : kr_φ2 M r = 32 * M ^ 3 / r * E⁻¹ * ((1 / r + 1 / (2 * M)) ^ 2 + 1 / r ^ 2) := by
    simp only [kr_φ2, kr_φ]; rw [hEi]
  have hMne := hM.ne'
  have hrne := hr.ne'
  have hEne := hE.ne'
  have hpne : hK' M r ≠ 0 := kr_hp_ne hM hx
  have hFne : FS M (u, v) ≠ 0 := (sk_FS_pos hM hx).ne'
  -- regroup, so that `U` and `V` enter only through `UV`
  have hg : (kr_SD M).gradR2 u v = -4 * (u * v) / (FS M (u, v) * hK' M r ^ 2) := by
    simp only [kr_WD.gradR2, kr_SD, ← hr_def]; field_simp
  have hk : (kr_SD M).k2 u v = 4 * (FS M (u, v) * (kr_φ2 M r * (u * v) / hK' M r ^ 2 +
      kr_φ1 M r * (-1 / hK' M r - (u * v) * kr_hpp M r / hK' M r ^ 3)) -
      kr_φ1 M r ^ 2 * (u * v) / hK' M r ^ 2) / FS M (u, v) ^ 3 := by
    simp only [kr_WD.k2, kr_SD, ← hr_def]; field_simp
  have hh : (kr_SD M).hessR2 u v = 8 / FS M (u, v) ^ 2 * ((u * v) ^ 2 *
      (-kr_hpp M r / hK' M r ^ 3 - kr_φ1 M r / (FS M (u, v) * hK' M r ^ 2)) ^ 2 +
      (-1 / hK' M r - (u * v) * kr_hpp M r / hK' M r ^ 3) ^ 2) := by
    simp only [kr_WD.hessR2, kr_SD, ← hr_def]; field_simp
  have hR : (kr_SD M).R u v = r := rfl
  rw [hg, hk, hh, hR, huv, hφ, hhp, hhpp, hφ1, hφ2]
  field_simp
  ring

end KRModel


namespace KRModel
open Model SEModel Kruskal

variable {M : ℝ} (hM : 0 < M)

/-- The Kretschmann scalar of Schwarzschild at the event `x ∈ W` and angles `(θ, φ)`. -/
noncomputable def kr_KS (M θ φ : ℝ) (x : seW) : ℝ := kr_K (kr_SD M).gW ![x.1.1, x.1.2, θ, φ]

include hM in
lemma kr_KS_eq {θ φ : ℝ} (hθ : Real.sin θ ≠ 0) (x : seW) :
    kr_KS M θ φ x = 48 * M ^ 2 / se_r M x ^ 6 :=
  kr_schwarzschild hM (x := ![x.1.1, x.1.2, θ, φ]) x.2.2 hθ

lemma kr_pow_blowup {c : ℝ} (hc : 0 < c) :
    Tendsto (fun r : ℝ => c / r ^ 6) (𝓝[>] 0) atTop := by
  have h := ((tendsto_pow_atTop (α := ℝ) (n := 6) (by norm_num)).comp
    tendsto_inv_nhdsGT_zero).const_mul_atTop hc
  refine h.congr fun r => ?_
  simp [div_eq_mul_inv, inv_pow]

include hM in
/-- **⑤ `kr_blowup`: `K → +∞` as `UV → 1⁻` within `W`** (BUILT), at any angles with `sin θ ≠ 0`:
`K = 48M²/r⁶` (④) and `r → 0⁺` (`kr_r_to_zero`). -/
theorem kr_blowup {θ φ : ℝ} (hθ : Real.sin θ ≠ 0) :
    Tendsto (kr_KS M θ φ) kr_toSig atTop := by
  have h := (kr_pow_blowup (c := 48 * M ^ 2) (by positivity)).comp (kr_r_to_zero hM).1
  exact h.congr fun x => (kr_KS_eq hM hθ x).symm

/-- Approaching a point `p` of `Σ` from inside `W` is approaching `Σ`: `UV → 1⁻`. -/
lemma kr_nhds_le_toSig {p : P} (hp : p ∈ kr_Sig) :
    Tendsto id (comap Subtype.val (𝓝 p) : Filter seW) kr_toSig := by
  rw [kr_toSig, tendsto_comap_iff, tendsto_nhdsWithin_iff]
  refine ⟨?_, Eventually.of_forall fun x => x.2.2⟩
  have hc : Continuous (fun q : P => q.1 * q.2) := continuous_fst.mul continuous_snd
  have h := (hc.tendsto p).comp (tendsto_comap (f := (Subtype.val : seW → P)) (x := 𝓝 p))
  have hp' : p.1 * p.2 = 1 := hp
  rw [hp'] at h
  exact h

include hM in
/-- **`kr_cor_densities_c` (7c)**: for the static observer at `r₀ > 2M` and any angles with
`sin θ ≠ 0`:
* the Kretschmann scalar is `48M²/r⁶` on all of `W`, and diverges as `UV → 1⁻` (a non-trivial approach);
* every point `p` of `Σ` that `W` reaches (`p ∈ closure W`) is approached from `W` (non-trivially), the
  curvature diverges there, `p` lies in the closure of the black-hole region `W ∖ J⁻(O)`, and `U > 0` at `p`;
* no finite exterior slice (any `Θ`, any `τ`) has a point of `Σ` in its closure. -/
theorem kr_cor_densities_c {r₀ : ℝ} (hr₀ : 2 * M < r₀) {θ φ : ℝ} (hθ : Real.sin θ ≠ 0) :
    (∀ x : seW, kr_KS M θ φ x = 48 * M ^ 2 / se_r M x ^ 6) ∧
    kr_toSig.NeBot ∧ Tendsto (kr_KS M θ φ) kr_toSig atTop ∧
    (∀ p ∈ kr_Sig ∩ closure (Subtype.val '' (univ : Set seW)),
      (comap Subtype.val (𝓝 p) : Filter seW).NeBot ∧
      Tendsto (kr_KS M θ φ) (comap Subtype.val (𝓝 p)) atTop ∧
      p ∈ closure (Subtype.val '' kr_BH hM hr₀) ∧ 0 < p.1) ∧
    (∀ (Θ : seW → ℝ) (τ : ℝ),
      kr_Sig ∩ closure (Subtype.val '' (se_S hM).slice (range (se_Ost hM hr₀)) Θ τ) = ∅) := by
  refine ⟨kr_KS_eq hM hθ, kr_toSig_neBot, kr_blowup hM hθ, fun p hp => ?_,
    fun Θ τ => kr_slice_far hM hr₀ Θ τ⟩
  have hp' := hp
  rw [kr_Sig_closure_W] at hp'
  obtain ⟨h1, h2⟩ := kr_locus_BH hM hr₀ hp'.1 hp'.2
  refine ⟨?_, (kr_blowup hM hθ).comp (kr_nhds_le_toSig hp.1), h1, h2⟩
  have hcl : p ∈ closure (seW : Set P) := by
    have := hp.2; rwa [image_univ, Subtype.range_coe] at this
  exact mem_closure_iff_comap_neBot.1 hcl

end KRModel

section CkChain
variable {𝕜 : Type*} [NontriviallyNormedField 𝕜] [CharZero 𝕜] [CompleteSpace 𝕜]

/-- 7e -/
theorem ck_order_two {h : 𝕜 → 𝕜} {z₀ : 𝕜} (hh : AnalyticAt 𝕜 h z₀) (h0 : h z₀ = 0)
    (h1 : deriv h z₀ = 0) (h2 : iteratedDeriv 2 h z₀ ≠ 0) : analyticOrderAt h z₀ = 2 := by
  have := (analyticOrderAt_eq_nat_iff_iteratedDeriv_eq_zero hh (n := 2)).2
  refine this ⟨fun k hk => ?_, h2⟩
  interval_cases k
  · simpa using h0
  · simpa using h1

theorem ck_chain_rule {h : 𝕜 → 𝕜} {z₀ : 𝕜} (hh : AnalyticAt 𝕜 h z₀) (h0 : h z₀ = 0)
    (h1 : deriv h z₀ = 0) (h2 : iteratedDeriv 2 h z₀ ≠ 0) {c : 𝕜} (hc : c ≠ 0) :
    meromorphicOrderAt (fun z => c / h z ^ 6) z₀ = -12 := by
  have ho := ck_order_two hh h0 h1 h2
  have hm : meromorphicOrderAt h z₀ = 2 := by
    rw [hh.meromorphicOrderAt_eq, ho]; rfl
  have hc' : meromorphicOrderAt (fun _ : 𝕜 => c) z₀ = 0 := by
    classical
    rw [meromorphicOrderAt_const]; simp [hc]
  rw [fun_meromorphicOrderAt_div (MeromorphicAt.const c z₀) (hh.meromorphicAt.fun_pow 6), hc',
    fun_meromorphicOrderAt_pow hh.meromorphicAt, hm]
  rfl
end CkChain

section CkC
open Complex

noncomputable def ck_rC (M : ℂ) (z : ℂ) : ℂ := M * (1 + Complex.cos z)

lemma ck_rC_deriv (M : ℂ) : deriv (ck_rC M) = fun z => -(M * Complex.sin z) := by
  funext z
  have h : HasDerivAt (ck_rC M) (-(M * Complex.sin z)) z := by
    have := ((hasDerivAt_const z (1:ℂ)).add (Complex.hasDerivAt_cos z)).const_mul M
    convert this using 1
    · rfl
    · ring
  exact h.deriv

lemma ck_rC_deriv2 (M z : ℂ) : iteratedDeriv 2 (ck_rC M) z = -(M * Complex.cos z) := by
  rw [iteratedDeriv_succ, iteratedDeriv_one, ck_rC_deriv]
  have := ((Complex.hasDerivAt_sin z).const_mul M).neg
  exact this.deriv

lemma ck_rC_analytic (M z : ℂ) : AnalyticAt ℂ (ck_rC M) z := by
  unfold ck_rC; fun_prop

theorem ck_pole_pi {M : ℂ} (hM : M ≠ 0) :
    meromorphicOrderAt (fun z => 48 * M ^ 2 / ck_rC M z ^ 6) (Real.pi : ℂ) = -12 := by
  refine ck_chain_rule (ck_rC_analytic M _) ?_ ?_ ?_ (by simpa using hM)
  · simp [ck_rC]
  · simp [ck_rC_deriv]
  · rw [ck_rC_deriv2]; simpa using hM

/-- the paper's form -/
theorem ck_K_form (M z : ℂ) (hM : M ≠ 0) :
    48 * M ^ 2 / ck_rC M z ^ 6 = 48 / (M ^ 4 * (1 + Complex.cos z) ^ 6) := by
  unfold ck_rC
  rcases eq_or_ne (1 + Complex.cos z) 0 with h | h
  · simp [h]
  · field_simp

theorem ck_pole_pi' {M : ℂ} (hM : M ≠ 0) :
    meromorphicOrderAt (fun z => 48 / (M ^ 4 * (1 + Complex.cos z) ^ 6)) (Real.pi : ℂ) = -12 := by
  rw [← ck_pole_pi hM]; congr 1; funext z; exact (ck_K_form M z hM).symm

theorem ck_order_zero {M : ℂ} (hM : M ≠ 0) :
    meromorphicOrderAt (fun z => 48 * M ^ 2 / ck_rC M z ^ 6) 0 = 0 := by
  have ha : AnalyticAt ℂ (fun z => 48 * M ^ 2 / ck_rC M z ^ 6) 0 := by
    refine AnalyticAt.div analyticAt_const ((ck_rC_analytic M 0).pow 6) ?_
    simp [ck_rC, hM]
  rw [ha.meromorphicOrderAt_eq, ha.analyticOrderAt_eq_zero.2]
  · rfl
  · have : ck_rC M 0 = 2 * M := by simp [ck_rC]; ring
    rw [this]; simp [hM]

/-- 8a -/
theorem ck_mislabel {M : ℂ} (hM : M ≠ 0) :
    meromorphicOrderAt (fun z => 48 * M ^ 2 / (M * (Complex.cos z - 1)) ^ 6) 0 = -12 := by
  have hd : deriv (fun z => M * (Complex.cos z - 1)) = fun z => -(M * Complex.sin z) := by
    funext z
    have h : HasDerivAt (fun z => M * (Complex.cos z - 1)) (-(M * Complex.sin z)) z := by
      have := ((Complex.hasDerivAt_cos z).sub_const (1:ℂ)).const_mul M
      convert this using 1; ring
    exact h.deriv
  refine ck_chain_rule (by fun_prop) (by simp) (by rw [hd]; simp) ?_ (by simpa using hM)
  rw [iteratedDeriv_succ, iteratedDeriv_one, hd]
  have h : HasDerivAt (fun z => -(M * Complex.sin z)) (-(M * Complex.cos 0)) 0 :=
    ((Complex.hasDerivAt_sin 0).const_mul M).neg
  rw [h.deriv]; simpa using hM
end CkC

section CkR
noncomputable def ck_r (M z : ℝ) : ℝ := M * (1 + Real.cos z)

lemma ck_r_deriv (M : ℝ) : deriv (ck_r M) = fun z => -(M * Real.sin z) := by
  funext z
  have h : HasDerivAt (ck_r M) (-(M * Real.sin z)) z := by
    have := ((hasDerivAt_const z (1:ℝ)).add (Real.hasDerivAt_cos z)).const_mul M
    convert this using 1
    · rfl
    · ring
  exact h.deriv

lemma ck_r_deriv2 (M z : ℝ) : iteratedDeriv 2 (ck_r M) z = -(M * Real.cos z) := by
  rw [iteratedDeriv_succ, iteratedDeriv_one, ck_r_deriv]
  exact ((Real.hasDerivAt_sin z).const_mul M).neg.deriv

/-- row 3 -/
theorem ck_critical {M : ℝ} (hM : M ≠ 0) (z : ℝ) :
    deriv (ck_r M) z = 0 ↔ ∃ k : ℤ, z = k * Real.pi := by
  rw [ck_r_deriv]
  simp only [neg_eq_zero, mul_eq_zero, hM, false_or, Real.sin_eq_zero_iff]
  exact ⟨fun ⟨k, hk⟩ => ⟨k, hk.symm⟩, fun ⟨k, hk⟩ => ⟨k, hk.symm⟩⟩

theorem ck_critical_even (M : ℝ) (k : ℤ) :
    ck_r M (2 * k * Real.pi) = 2 * M ∧ iteratedDeriv 2 (ck_r M) (2 * k * Real.pi) = -M := by
  have hc : Real.cos (2 * k * Real.pi) = 1 := by
    have := Real.cos_int_mul_two_pi k; rw [← this]; ring_nf
  refine ⟨by simp [ck_r, hc]; ring, by rw [ck_r_deriv2, hc]; ring⟩

theorem ck_critical_odd (M : ℝ) (k : ℤ) :
    ck_r M ((2 * k + 1) * Real.pi) = 0 ∧
      iteratedDeriv 2 (ck_r M) ((2 * k + 1) * Real.pi) = M := by
  have hc : Real.cos ((2 * k + 1) * Real.pi) = -1 := by
    have := Real.cos_int_mul_two_pi_add_pi k; rw [← this]; ring_nf
  refine ⟨by simp [ck_r, hc], by rw [ck_r_deriv2, hc]; ring⟩

theorem ck_max_min {M : ℝ} (hM : 0 < M) (z : ℝ) : 0 ≤ ck_r M z ∧ ck_r M z ≤ 2 * M := by
  have h1 := Real.cos_le_one z; have h2 := Real.neg_one_le_cos z
  constructor <;> unfold ck_r <;> nlinarith

/-- 7d, explicit -/
theorem ck_bounded_zero {M : ℝ} (hM : 0 < M) {z : ℝ} (hz : z ∈ Set.Ioo (-(Real.pi / 2)) (Real.pi / 2)) :
    48 * M ^ 2 / ck_r M z ^ 6 ≤ 48 / M ^ 4 := by
  have hc : 0 ≤ Real.cos z := Real.cos_nonneg_of_mem_Icc ⟨hz.1.le, hz.2.le⟩
  have hr : M ≤ ck_r M z := by unfold ck_r; nlinarith
  have hM6 : M ^ 6 ≤ ck_r M z ^ 6 := pow_le_pow_left₀ hM.le hr 6
  have hr0 : 0 < ck_r M z := lt_of_lt_of_le hM hr
  rw [div_le_div_iff₀ (by positivity) (by positivity)]
  nlinarith [pow_pos hM 4, pow_pos hM 2]

theorem ck_value_zero {M : ℝ} (hM : 0 < M) : 48 * M ^ 2 / ck_r M 0 ^ 6 = 3 / (4 * M ^ 4) := by
  simp [ck_r]; field_simp; ring

/-- **`prop:critical`** (row 3): the critical points of `r(z) = M(1 + cos z)` are exactly `πℤ`; at `2kπ`, `r = 2M`
and `r'' = −M`, the global maximum; at `(2k + 1)π`, `r = 0` and `r'' = M`, the global minimum; every critical
point is non-degenerate. -/
theorem ck_prop_critical {M : ℝ} (hM : 0 < M) :
    (∀ z, deriv (ck_r M) z = 0 ↔ ∃ k : ℤ, z = k * Real.pi) ∧
    (∀ k : ℤ, ck_r M (2 * k * Real.pi) = 2 * M ∧ iteratedDeriv 2 (ck_r M) (2 * k * Real.pi) = -M) ∧
    (∀ k : ℤ, ck_r M ((2 * k + 1) * Real.pi) = 0 ∧
      iteratedDeriv 2 (ck_r M) ((2 * k + 1) * Real.pi) = M) ∧
    (∀ z, deriv (ck_r M) z = 0 → iteratedDeriv 2 (ck_r M) z ≠ 0) ∧
    (∀ z, 0 ≤ ck_r M z ∧ ck_r M z ≤ 2 * M) := by
  refine ⟨ck_critical hM.ne', ck_critical_even M, ck_critical_odd M, fun z hz => ?_, ck_max_min hM⟩
  obtain ⟨k, rfl⟩ := (ck_critical hM.ne' z).1 hz
  rw [ck_r_deriv2]
  have hc : Real.cos (k * Real.pi) ≠ 0 := by
    intro h; have := Real.abs_cos_int_mul_pi k; rw [h] at this; norm_num at this
  exact neg_ne_zero.2 (mul_ne_zero hM.ne' hc)
end CkR

namespace KRModel
open Model SEModel Kruskal

variable {M : ℝ} (hM : 0 < M)

include hM in
/-- **7a: `K = 3/(4M⁴)` on the horizon `UV = 0`** (so at the bifurcation sphere `U = V = 0`), where `r = 2M`,
from `kr_schwarzschild` and `sk_rK_eq_two_iff`. -/
theorem ck_horizon {x : Fin 4 → ℝ} (hx : x 0 * x 1 = 0) (hs : Real.sin (x 2) ≠ 0) :
    kr_K (kr_SD M).gW x = 3 / (4 * M ^ 4) := by
  have hk : (x 0, x 1) ∈ sk_kM := by show x 0 * x 1 < 1; rw [hx]; norm_num
  rw [kr_schwarzschild hM hk hs, (sk_rK_eq_two_iff hM hk).2 hx]
  field_simp; ring

include hM in
/-- **7a at the bifurcation sphere** `U = V = 0`. -/
theorem ck_bifurcation {x : Fin 4 → ℝ} (hU : x 0 = 0) (hV : x 1 = 0) (hs : Real.sin (x 2) ≠ 0) :
    kr_K (kr_SD M).gW x = 3 / (4 * M ^ 4) :=
  ck_horizon hM (by rw [hU, hV, mul_zero]) hs

include hM in
/-- **7b: `K = 48/(M⁴(1 + cos η)⁶)` wherever `r = M(1 + cos η)`**, the curvature of the Kruskal chart's
coordinate Riemann tensor (`kr_schwarzschild`). -/
theorem ck_interior {x : Fin 4 → ℝ} (hx : (x 0, x 1) ∈ sk_kM) (hs : Real.sin (x 2) ≠ 0) {η : ℝ}
    (hr : rK M (x 0, x 1) = ck_r M η) :
    kr_K (kr_SD M).gW x = 48 / (M ^ 4 * (1 + Real.cos η) ^ 6) := by
  have hpos := kr_r_pos hM hx
  rw [kr_schwarzschild hM hx hs, hr]
  rw [hr] at hpos
  have hc : 1 + Real.cos η ≠ 0 := by
    intro h; simp [ck_r, h] at hpos
  unfold ck_r
  field_simp

include hM in
/-- **7b is not vacuous: every `η` with `1 + cos η ≠ 0` is reached in the interior `UV ≥ 0` (`r ≤ 2M`) of the
chart**, at `(U, V) = (1, −hK(r))`. -/
theorem ck_interior_witness {η : ℝ} (hη : 1 + Real.cos η ≠ 0) :
    ∃ x : Fin 4 → ℝ, (x 0, x 1) ∈ sk_kM ∧ 0 ≤ x 0 * x 1 ∧ Real.sin (x 2) ≠ 0 ∧
      rK M (x 0, x 1) = ck_r M η := by
  have hc1 := Real.cos_le_one η
  have hc0 : 0 < 1 + Real.cos η := lt_of_le_of_ne (by linarith [Real.neg_one_le_cos η]) (Ne.symm hη)
  set r := ck_r M η with hr_def
  have hr : 0 < r := by simp only [hr_def, ck_r]; positivity
  have hr2 : r ≤ 2 * M := by simp only [hr_def, ck_r]; nlinarith
  have hle : hK M r ≤ 0 := by
    rw [← hK_two hM]
    exact (hK_strictMonoOn hM).monotoneOn (Set.mem_Ici.2 hr.le) (Set.mem_Ici.2 (by linarith)) hr2
  have hgt := hK_gt hM hr
  refine ⟨![1, -hK M r, Real.pi / 2, 0], ?_, ?_, ?_, ?_⟩
  · show (1 : ℝ) * (-hK M r) < 1; linarith
  · show (0 : ℝ) ≤ 1 * (-hK M r); linarith
  · simp
  · show rinv M (-((1 : ℝ) * (-hK M r))) = r
    rw [one_mul, neg_neg, rinv_hK hM hr]

include hM in
/-- **`prop:Kretschmann`, its formal part** (rows 7a–7d): on the chart, `K = 3/(4M⁴)` on the horizon; as a function
of `z` (with `r = M(1 + cos z)`), `48M²/r⁶ = 48/(M⁴(1 + cos z)⁶)` has a pole of order exactly `12` at `z = π`
(meromorphic order `−12` over `ℂ`), and order `0` at `z = 0`, where it is bounded by `48/M⁴` on
`(−π/2, π/2)` and takes the value `3/(4M⁴)`. -/
theorem ck_prop_Kretschmann :
    (∀ x : Fin 4 → ℝ, x 0 * x 1 = 0 → Real.sin (x 2) ≠ 0 → kr_K (kr_SD M).gW x = 3 / (4 * M ^ 4)) ∧
    meromorphicOrderAt (fun z => 48 / ((M : ℂ) ^ 4 * (1 + Complex.cos z) ^ 6)) (Real.pi : ℂ) = -12 ∧
    meromorphicOrderAt (fun z => 48 * (M : ℂ) ^ 2 / ck_rC M z ^ 6) 0 = 0 ∧
    (∀ z ∈ Set.Ioo (-(Real.pi / 2)) (Real.pi / 2), 48 * M ^ 2 / ck_r M z ^ 6 ≤ 48 / M ^ 4) ∧
    48 * M ^ 2 / ck_r M 0 ^ 6 = 3 / (4 * M ^ 4) := by
  have hMC : (M : ℂ) ≠ 0 := by exact_mod_cast hM.ne'
  exact ⟨fun x hx hs => ck_horizon hM hx hs, ck_pole_pi' hMC, ck_order_zero hMC,
    fun z hz => ck_bounded_zero hM hz, ck_value_zero hM⟩

include hM in
/-- **`cor:Kretschmann_at_z0`, its formal part** (row 8a): with the maximum of `r(z)` labelled `0` instead of `2M`,
i.e. `h(z) = M(cos z − 1)`, `48M²/h⁶` has a pole of order exactly `12` at `z = 0`; with the chart's labelling
`r(0) = 2M` it is analytic there with value `3/(4M⁴)`. -/
theorem ck_cor_Kretschmann_at_z0 :
    meromorphicOrderAt (fun z => 48 * (M : ℂ) ^ 2 / ((M : ℂ) * (Complex.cos z - 1)) ^ 6) 0 = -12 ∧
    meromorphicOrderAt (fun z => 48 * (M : ℂ) ^ 2 / ck_rC M z ^ 6) 0 = 0 ∧
    48 * M ^ 2 / ck_r M 0 ^ 6 = 3 / (4 * M ^ 4) := by
  have hMC : (M : ℂ) ≠ 0 := by exact_mod_cast hM.ne'
  exact ⟨ck_mislabel hMC, ck_order_zero hMC, ck_value_zero hM⟩

end KRModel

section CyCycloid
variable {M : ℝ}

/-- `τ(η) = M(η + sin η)` -/
noncomputable def cy_τ (M η : ℝ) : ℝ := M * (η + Real.sin η)
/-- `r(η) = M(1 + cos η)` -/
noncomputable def cy_r (M η : ℝ) : ℝ := M * (1 + Real.cos η)

lemma cy_cos_half_sq (η : ℝ) : 2 * Real.cos (η / 2) ^ 2 = 1 + Real.cos η := by
  rw [Real.cos_sq]; ring_nf

lemma cy_hasDerivAt_τ (M η : ℝ) : HasDerivAt (cy_τ M) (M * (1 + Real.cos η)) η := by
  have := ((hasDerivAt_id η).add (Real.hasDerivAt_sin η)).const_mul M
  convert this using 1
  funext y; rfl

lemma cy_continuous_τ (M : ℝ) : Continuous (cy_τ M) := by unfold cy_τ; fun_prop

/-- **1a-①**: the proper time `∫₀^η 2M cos²(s/2) ds` is `M(η + sin η)`. -/
theorem cy_proper_time (M η : ℝ) :
    ∫ s in (0:ℝ)..η, 2 * M * Real.cos (s / 2) ^ 2 = cy_τ M η := by
  have h : ∀ s ∈ uIcc (0:ℝ) η, HasDerivAt (cy_τ M) (2 * M * Real.cos (s / 2) ^ 2) s := by
    intro s _
    convert cy_hasDerivAt_τ M s using 1
    have := cy_cos_half_sq s; linear_combination M * this
  rw [intervalIntegral.integral_eq_sub_of_hasDerivAt h]
  · simp [cy_τ]
  · apply Continuous.intervalIntegrable; fun_prop

/-- **1b**: the proper time from `r = 2M` (`η = 0`) to `r = 0` (`η = π`) is `Mπ`. -/
theorem cy_Mpi (M : ℝ) :
    ∫ s in (0:ℝ)..Real.pi, 2 * M * Real.cos (s / 2) ^ 2 = M * Real.pi := by
  rw [cy_proper_time]; simp [cy_τ]

lemma cy_cos_gt {x : ℝ} (hx : x ∈ Ioo 0 Real.pi) : -1 < Real.cos x := by
  have := Real.cos_lt_cos_of_nonneg_of_le_pi hx.1.le le_rfl hx.2
  rwa [Real.cos_pi] at this

theorem cy_τ_strictMonoOn (hM : 0 < M) : StrictMonoOn (cy_τ M) (Icc 0 Real.pi) := by
  apply strictMonoOn_of_deriv_pos (convex_Icc 0 Real.pi) (cy_continuous_τ M).continuousOn
  intro x hx
  rw [interior_Icc] at hx
  rw [(cy_hasDerivAt_τ M x).deriv]
  have := cy_cos_gt hx
  nlinarith

lemma cy_τ_zero : cy_τ M 0 = 0 := by simp [cy_τ]
lemma cy_τ_pi : cy_τ M Real.pi = M * Real.pi := by simp [cy_τ]

/-- `η(τ)`, the inverse of `τ` on `[0, π]`. -/
noncomputable def cy_η (M τ : ℝ) : ℝ := Function.invFunOn (cy_τ M) (Icc 0 Real.pi) τ

lemma cy_τ_surj (_hM : 0 < M) {τ : ℝ} (hτ : τ ∈ Icc 0 (M * Real.pi)) :
    ∃ η ∈ Icc 0 Real.pi, cy_τ M η = τ := by
  have := intermediate_value_Icc Real.pi_pos.le (cy_continuous_τ M).continuousOn
  rw [cy_τ_zero, cy_τ_pi] at this
  exact this hτ

theorem cy_η_spec (hM : 0 < M) {τ : ℝ} (hτ : τ ∈ Icc 0 (M * Real.pi)) :
    cy_η M τ ∈ Icc 0 Real.pi ∧ cy_τ M (cy_η M τ) = τ :=
  ⟨Function.invFunOn_mem (cy_τ_surj hM hτ), Function.invFunOn_eq (cy_τ_surj hM hτ)⟩

theorem cy_η_τ (hM : 0 < M) {η : ℝ} (hη : η ∈ Icc 0 Real.pi) : cy_η M (cy_τ M η) = η := by
  have hτ : cy_τ M η ∈ Icc 0 (M * Real.pi) := by
    rw [← cy_τ_zero (M := M), ← cy_τ_pi (M := M)]
    exact ⟨(cy_τ_strictMonoOn hM).monotoneOn ⟨le_rfl, Real.pi_pos.le⟩ hη hη.1,
      (cy_τ_strictMonoOn hM).monotoneOn hη ⟨Real.pi_pos.le, le_rfl⟩ hη.2⟩
  exact (cy_τ_strictMonoOn hM).injOn (cy_η_spec hM hτ).1 hη (cy_η_spec hM hτ).2

lemma cy_η_strictMonoOn (hM : 0 < M) : StrictMonoOn (cy_η M) (Icc 0 (M * Real.pi)) := by
  intro a ha b hb hab
  have h1 := cy_η_spec hM ha; have h2 := cy_η_spec hM hb
  by_contra h
  push Not at h
  have := (cy_τ_strictMonoOn hM).monotoneOn h2.1 h1.1 h
  rw [h1.2, h2.2] at this; linarith

lemma cy_η_image (hM : 0 < M) : cy_η M '' Icc 0 (M * Real.pi) = Icc 0 Real.pi := by
  ext η; constructor
  · rintro ⟨τ, hτ, rfl⟩; exact (cy_η_spec hM hτ).1
  · intro hη
    refine ⟨cy_τ M η, ?_, cy_η_τ hM hη⟩
    rw [← cy_τ_zero (M := M), ← cy_τ_pi (M := M)]
    exact ⟨(cy_τ_strictMonoOn hM).monotoneOn ⟨le_rfl, Real.pi_pos.le⟩ hη hη.1,
      (cy_τ_strictMonoOn hM).monotoneOn hη ⟨Real.pi_pos.le, le_rfl⟩ hη.2⟩

lemma cy_η_zero (hM : 0 < M) : cy_η M 0 = 0 := by
  have := cy_η_τ hM (η := 0) ⟨le_rfl, Real.pi_pos.le⟩; rwa [cy_τ_zero] at this

lemma cy_η_end (hM : 0 < M) : cy_η M (M * Real.pi) = Real.pi := by
  have := cy_η_τ hM (η := Real.pi) ⟨Real.pi_pos.le, le_rfl⟩; rwa [cy_τ_pi] at this

lemma cy_η_mem_Ioo (hM : 0 < M) {τ : ℝ} (hτ : τ ∈ Ioo 0 (M * Real.pi)) :
    cy_η M τ ∈ Ioo 0 Real.pi := by
  have hMp : 0 < M * Real.pi := by positivity
  have hm := cy_η_strictMonoOn hM
  have h0 := hm ⟨le_rfl, hMp.le⟩ (Ioo_subset_Icc_self hτ) hτ.1
  have h1 := hm (Ioo_subset_Icc_self hτ) ⟨hMp.le, le_rfl⟩ hτ.2
  rw [cy_η_zero hM] at h0; rw [cy_η_end hM] at h1
  exact ⟨h0, h1⟩

lemma cy_η_continuousAt (hM : 0 < M) {τ : ℝ} (hτ : τ ∈ Ioo 0 (M * Real.pi)) :
    ContinuousAt (cy_η M) τ := by
  refine (cy_η_strictMonoOn hM).continuousAt_of_image_mem_nhds (Icc_mem_nhds hτ.1 hτ.2) ?_
  rw [cy_η_image hM]
  have := cy_η_mem_Ioo hM hτ
  exact Icc_mem_nhds this.1 this.2

/-- `dη/dτ = 1/(M(1 + cos η))`. -/
theorem cy_hasDerivAt_η (hM : 0 < M) {τ : ℝ} (hτ : τ ∈ Ioo 0 (M * Real.pi)) :
    HasDerivAt (cy_η M) (1 / (M * (1 + Real.cos (cy_η M τ)))) τ := by
  have hη := cy_η_mem_Ioo hM hτ
  have hc := cy_cos_gt hη
  rw [one_div]
  refine HasDerivAt.of_local_left_inverse (cy_η_continuousAt hM hτ) (cy_hasDerivAt_τ M _)
    (by have : 0 < 1 + Real.cos (cy_η M τ) := by linarith
        positivity) ?_
  filter_upwards [Ioo_mem_nhds hτ.1 hτ.2] with y hy
  exact (cy_η_spec hM (Ioo_subset_Icc_self hy)).2

/-- **1a-②**: along the curve, `r(τ) = M(1 + cos η(τ))` has `dr/dτ = −sin η/(1 + cos η)`, and
`(dr/dτ)² = 2M/r − 1`, which is `E² − 1 + 2M/r` with `E = 0`. -/
theorem cy_radial (hM : 0 < M) {τ : ℝ} (hτ : τ ∈ Ioo 0 (M * Real.pi)) :
    HasDerivAt (fun σ => cy_r M (cy_η M σ))
      (-(Real.sin (cy_η M τ)) / (1 + Real.cos (cy_η M τ))) τ ∧
    (-(Real.sin (cy_η M τ)) / (1 + Real.cos (cy_η M τ))) ^ 2 =
      2 * M / cy_r M (cy_η M τ) - 1 := by
  have hc := cy_cos_gt (cy_η_mem_Ioo hM hτ)
  have hc' : 1 + Real.cos (cy_η M τ) ≠ 0 := by linarith
  constructor
  · have h := ((Real.hasDerivAt_cos _).comp τ (cy_hasDerivAt_η hM hτ)).const_add 1 |>.const_mul M
    convert h using 1
    · funext y; simp [cy_r]
    · field_simp
  · unfold cy_r
    have hs := Real.sin_sq_add_cos_sq (cy_η M τ)
    field_simp
    nlinarith [hs]

theorem cy_η_tendsto_zero (hM : 0 < M) : Tendsto (cy_η M) (𝓝[>] 0) (𝓝 0) := by
  have hMp : 0 < M * Real.pi := by positivity
  have h := continuousWithinAt_right_of_monotoneOn_of_image_mem_nhdsWithin
    (cy_η_strictMonoOn hM).monotoneOn (Icc_mem_nhdsGE hMp) (by
      rw [cy_η_image hM, cy_η_zero hM]; exact Icc_mem_nhdsGE Real.pi_pos)
  have := h.tendsto
  rw [cy_η_zero hM] at this
  exact this.mono_left (nhdsWithin_mono _ Ioi_subset_Ici_self)

theorem cy_η_tendsto_end (hM : 0 < M) :
    Tendsto (cy_η M) (𝓝[<] (M * Real.pi)) (𝓝 Real.pi) := by
  have hMp : 0 < M * Real.pi := by positivity
  have h := continuousWithinAt_left_of_monotoneOn_of_image_mem_nhdsWithin
    (cy_η_strictMonoOn hM).monotoneOn (Icc_mem_nhdsLE hMp) (by
      rw [cy_η_image hM, cy_η_end hM]; exact Icc_mem_nhdsLE Real.pi_pos)
  have := h.tendsto
  rw [cy_η_end hM] at this
  exact this.mono_left (nhdsWithin_mono _ Iio_subset_Iic_self)

/-- **1a-②, the ends**: `r → 2M` and `dr/dτ → 0` as `τ → 0⁺` (at rest at `r = 2M`); `r → 0` as `τ → Mπ⁻`. -/
theorem cy_ends (hM : 0 < M) :
    Tendsto (fun τ => cy_r M (cy_η M τ)) (𝓝[>] 0) (𝓝 (2 * M)) ∧
    Tendsto (fun τ => -(Real.sin (cy_η M τ)) / (1 + Real.cos (cy_η M τ))) (𝓝[>] 0) (𝓝 0) ∧
    Tendsto (fun τ => cy_r M (cy_η M τ)) (𝓝[<] (M * Real.pi)) (𝓝 0) := by
  have h0 := cy_η_tendsto_zero hM
  have h1 := cy_η_tendsto_end hM
  refine ⟨?_, ?_, ?_⟩
  · have : Continuous (cy_r M) := by unfold cy_r; fun_prop
    have := (this.tendsto 0).comp h0
    have e : cy_r M 0 = 2 * M := by simp [cy_r]; ring
    rw [e] at this; exact this
  · have hc : ContinuousAt (fun η => -(Real.sin η) / (1 + Real.cos η)) 0 := by
      apply ContinuousAt.div (by fun_prop) (by fun_prop); norm_num
    have := hc.tendsto.comp h0
    simpa [Function.comp_def] using this
  · have : Continuous (cy_r M) := by unfold cy_r; fun_prop
    have := (this.tendsto Real.pi).comp h1
    have e : cy_r M Real.pi = 0 := by simp [cy_r]
    rw [e] at this; exact this
end CyCycloid

section CyDiag

lemma cy_pd0 (f : ℝ → ℝ) (x : Fin 2 → ℝ) : kr_pd (fun y => f (y 0)) x 0 = deriv f (x 0) := by
  simp [kr_pd]

lemma cy_pd1 (f : ℝ → ℝ) (x : Fin 2 → ℝ) : kr_pd (fun y => f (y 0)) x 1 = 0 := by
  simp [kr_pd]

lemma cy_pdz (x : Fin 2 → ℝ) (c : Fin 2) : kr_pd (fun _ => (0:ℝ)) x c = 0 := by simp [kr_pd]

/-- A diagonal metric `diag(A(x⁰), B(x⁰))` on `ℝ²`. -/
noncomputable def cy_gD (A B : ℝ → ℝ) (x : Fin 2 → ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  Matrix.diagonal ![A (x 0), B (x 0)]

/-- **The Christoffel symbols of `diag(A(x⁰), B(x⁰))`** (the registered fallback): the non-zero ones are
`Γ⁰₀₀ = A′/2A`, `Γ⁰₁₁ = −B′/2A` and `Γ¹₀₁ = Γ¹₁₀ = B′/2B`. -/
theorem cy_diag_Γ (A B : ℝ → ℝ) (x : Fin 2 → ℝ) (hA : A (x 0) ≠ 0) (hB : B (x 0) ≠ 0) :
    kr_Γ (cy_gD A B) x 0 0 0 = deriv A (x 0) / (2 * A (x 0)) ∧
    kr_Γ (cy_gD A B) x 0 0 1 = 0 ∧ kr_Γ (cy_gD A B) x 0 1 0 = 0 ∧
    kr_Γ (cy_gD A B) x 0 1 1 = -(deriv B (x 0)) / (2 * A (x 0)) ∧
    kr_Γ (cy_gD A B) x 1 0 0 = 0 ∧
    kr_Γ (cy_gD A B) x 1 0 1 = deriv B (x 0) / (2 * B (x 0)) ∧
    kr_Γ (cy_gD A B) x 1 1 0 = deriv B (x 0) / (2 * B (x 0)) ∧
    kr_Γ (cy_gD A B) x 1 1 1 = 0 := by
  have e00 : (fun y => cy_gD A B y 0 0) = fun y => A (y 0) := by funext y; simp [cy_gD]
  have e11 : (fun y => cy_gD A B y 1 1) = fun y => B (y 0) := by funext y; simp [cy_gD]
  have e01 : (fun y => cy_gD A B y 0 1) = fun y => (fun _ : ℝ => (0:ℝ)) (y 0) := by
    funext y; simp [cy_gD]
  have e10 : (fun y => cy_gD A B y 1 0) = fun y => (fun _ : ℝ => (0:ℝ)) (y 0) := by
    funext y; simp [cy_gD]
  have hinv : (cy_gD A B x)⁻¹ = Matrix.diagonal ![(A (x 0))⁻¹, (B (x 0))⁻¹] := by
    refine Matrix.inv_eq_left_inv ?_
    rw [cy_gD, Matrix.diagonal_mul_diagonal, ← Matrix.diagonal_one]
    congr 1; funext i; fin_cases i <;> simp [hA, hB]
  simp only [kr_Γ, Fin.sum_univ_two, hinv, e00, e11, e01, e10, cy_pd0, cy_pd1]
  simp [Matrix.diagonal, cy_pdz]
  refine ⟨?_, ?_, ?_⟩ <;> field_simp
end CyDiag

section CyGeodesic
variable {M : ℝ}

/-- `g_ηη = −(M(1 + cos η))² = −4M²cos⁴(η/2)` -/
noncomputable def cy_A (M η : ℝ) : ℝ := -(M * (1 + Real.cos η)) ^ 2
/-- `g_tt = (1 − cos η)/(1 + cos η) = tan²(η/2)` -/
noncomputable def cy_B (η : ℝ) : ℝ := (1 - Real.cos η) / (1 + Real.cos η)
/-- **The interior chart's metric** `g = −4M²cos⁴(η/2) dη² + tan²(η/2) dt²` (P2 `eq:interior_metric_eta`, radial
part), on `(η, t)`. -/
noncomputable def cy_g (M : ℝ) : (Fin 2 → ℝ) → Matrix (Fin 2) (Fin 2) ℝ := cy_gD (cy_A M) cy_B

/-- The infall curve `c(τ) = (η(τ), t₀)`. -/
noncomputable def cy_c (M t₀ τ : ℝ) : Fin 2 → ℝ := ![cy_η M τ, t₀]

/-- The geodesic equation `c″ᵃ + Γᵃ_bd c′ᵇ c′ᵈ = 0` on `s`, with campaign 110's `kr_Γ`. -/
def cy_IsGeodesic (g : (Fin 2 → ℝ) → Matrix (Fin 2) (Fin 2) ℝ) (c : ℝ → Fin 2 → ℝ) (s : Set ℝ) :
    Prop :=
  ∀ τ ∈ s, ∀ a, deriv (fun σ => deriv (fun ρ => c ρ a) σ) τ +
    ∑ b, ∑ d, kr_Γ g (c τ) a b d * deriv (fun ρ => c ρ b) τ * deriv (fun ρ => c ρ d) τ = 0

lemma cy_cos_lt {x : ℝ} (hx : x ∈ Ioo 0 Real.pi) : Real.cos x < 1 := by
  have := Real.cos_lt_cos_of_nonneg_of_le_pi le_rfl hx.2.le hx.1
  rwa [Real.cos_zero] at this

lemma cy_hasDerivAt_A (M η : ℝ) :
    HasDerivAt (cy_A M) (2 * M ^ 2 * (1 + Real.cos η) * Real.sin η) η := by
  have h := (((hasDerivAt_const η (1:ℝ)).add (Real.hasDerivAt_cos η)).const_mul M).pow 2 |>.neg
  convert h using 1
  · funext y; simp [cy_A]
  · simp; ring

/-- **1a-③**: `c(τ) = (η(τ), t₀)` is a geodesic of the interior chart on `0 < τ < Mπ`, unit timelike
(`g(c′, c′) = −1`), with Killing energy `E = −g(c′, ∂_t) = 0`. -/
theorem cy_geodesic (hM : 0 < M) (t₀ : ℝ) :
    cy_IsGeodesic (cy_g M) (cy_c M t₀) (Ioo 0 (M * Real.pi)) ∧
    (∀ τ ∈ Ioo 0 (M * Real.pi), ∑ a, ∑ b, cy_g M (cy_c M t₀ τ) a b *
        deriv (fun ρ => cy_c M t₀ ρ a) τ * deriv (fun ρ => cy_c M t₀ ρ b) τ = -1) ∧
    (∀ τ ∈ Ioo 0 (M * Real.pi),
        -(∑ a, cy_g M (cy_c M t₀ τ) a 1 * deriv (fun ρ => cy_c M t₀ ρ a) τ) = 0) := by
  -- the velocity and acceleration
  have hd0 : ∀ τ ∈ Ioo 0 (M * Real.pi),
      deriv (fun ρ => cy_c M t₀ ρ 0) τ = 1 / (M * (1 + Real.cos (cy_η M τ))) := by
    intro τ hτ
    show deriv (fun ρ => cy_η M ρ) τ = _
    exact (cy_hasDerivAt_η hM hτ).deriv
  have hd1 : ∀ τ, deriv (fun ρ => cy_c M t₀ ρ 1) τ = 0 := by
    intro τ; show deriv (fun _ => t₀) τ = 0; simp
  have hdd0 : ∀ τ ∈ Ioo 0 (M * Real.pi),
      deriv (fun σ => deriv (fun ρ => cy_c M t₀ ρ 0) σ) τ =
        M * (Real.sin (cy_η M τ) * (1 / (M * (1 + Real.cos (cy_η M τ))))) /
          (M * (1 + Real.cos (cy_η M τ))) ^ 2 := by
    intro τ hτ
    have hev : (fun σ => deriv (fun ρ => cy_c M t₀ ρ 0) σ) =ᶠ[𝓝 τ]
        fun σ => (M * (1 + Real.cos (cy_η M σ)))⁻¹ := by
      filter_upwards [Ioo_mem_nhds hτ.1 hτ.2] with σ hσ
      rw [hd0 σ hσ, one_div]
    rw [hev.deriv_eq]
    have hc := cy_cos_gt (cy_η_mem_Ioo hM hτ)
    have hne : M * (1 + Real.cos (cy_η M τ)) ≠ 0 := by
      have : 0 < 1 + Real.cos (cy_η M τ) := by linarith
      positivity
    have h := (((Real.hasDerivAt_cos _).comp τ (cy_hasDerivAt_η hM hτ)).const_add 1
      |>.const_mul M).inv hne
    have e : (fun σ => (M * (1 + Real.cos (cy_η M σ)))⁻¹) =
        (fun y => M * (1 + (Real.cos ∘ cy_η M) y))⁻¹ := by
      funext y; simp
    rw [e, h.deriv]
    simp only [Function.comp_def]
    field_simp
  have hdd1 : ∀ τ, deriv (fun σ => deriv (fun ρ => cy_c M t₀ ρ 1) σ) τ = 0 := by
    intro τ; simp only [hd1]; simp
  refine ⟨fun τ hτ => ?_, fun τ hτ => ?_, fun τ hτ => ?_⟩
  all_goals
    have hη := cy_η_mem_Ioo hM hτ
    have hc := cy_cos_gt hη
    have hc1 := cy_cos_lt hη
    have hx0 : cy_c M t₀ τ 0 = cy_η M τ := rfl
    have hpos : 0 < 1 + Real.cos (cy_η M τ) := by linarith
    have hA : cy_A M (cy_c M t₀ τ 0) ≠ 0 := by
      rw [hx0, cy_A]
      have : 0 < M * (1 + Real.cos (cy_η M τ)) := by positivity
      nlinarith
    have hB : cy_B (cy_c M t₀ τ 0) ≠ 0 := by
      rw [hx0, cy_B]; apply div_ne_zero <;> linarith
  · obtain ⟨g000, g001, g010, g011, g100, g101, g110, g111⟩ :=
      cy_diag_Γ (cy_A M) cy_B (cy_c M t₀ τ) hA hB
    rw [Fin.forall_fin_two]
    constructor
    · rw [Fin.sum_univ_two, Fin.sum_univ_two, Fin.sum_univ_two, hdd0 τ hτ, hd0 τ hτ, hd1]
      simp only [cy_g, g000, g001, g010, g011, (cy_hasDerivAt_A M _).deriv, hx0, cy_A]
      field_simp
      ring
    · rw [Fin.sum_univ_two, Fin.sum_univ_two, Fin.sum_univ_two, hdd1, hd0 τ hτ, hd1]
      simp only [cy_g, g100]
      ring
  · rw [Fin.sum_univ_two, Fin.sum_univ_two, Fin.sum_univ_two, hd0 τ hτ, hd1]
    simp only [cy_g, cy_gD]
    simp [hx0, cy_A]
    field_simp
  · rw [Fin.sum_univ_two, hd0 τ hτ, hd1]
    simp [cy_g, cy_gD]
end CyGeodesic

section CyForms
open Complex
variable {M : ℝ}

/-- **2b**: on `0 < η < π`, with `r = M(1 + cos η)`: `g_tt = 2M/r − 1 = tan²(η/2)`;
`g_rr (dr/dη)² = (1 − 2M/r)⁻¹ (M sin η)² = −4M²cos⁴(η/2) = −(dτ/dη)²`; and `r² = M²(1 + cos η)²`. -/
theorem cy_interior_forms (hM : 0 < M) {η : ℝ} (hη : η ∈ Ioo 0 Real.pi) :
    2 * M / cy_r M η - 1 = Real.tan (η / 2) ^ 2 ∧
    (1 - 2 * M / cy_r M η)⁻¹ * (M * Real.sin η) ^ 2 = -(4 * M ^ 2 * Real.cos (η / 2) ^ 4) ∧
    4 * M ^ 2 * Real.cos (η / 2) ^ 4 = (M * (1 + Real.cos η)) ^ 2 ∧
    (1 - Real.cos η) / (1 + Real.cos η) = Real.tan (η / 2) ^ 2 ∧
    cy_r M η ^ 2 = M ^ 2 * (1 + Real.cos η) ^ 2 := by
  have hc2 := cy_cos_half_sq η
  have hpi := Real.pi_pos
  have hh : η / 2 ∈ Ioo (-(Real.pi / 2)) (Real.pi / 2) := ⟨by linarith [hη.1], by linarith [hη.2]⟩
  have hcpos : 0 < Real.cos (η / 2) := Real.cos_pos_of_mem_Ioo hh
  have hs : Real.sin η = 2 * Real.sin (η / 2) * Real.cos (η / 2) := by
    rw [← Real.sin_two_mul]; ring_nf
  have hc : Real.cos η = 2 * Real.cos (η / 2) ^ 2 - 1 := by linarith
  have hsc := Real.sin_sq_add_cos_sq (η / 2)
  have hspos : 0 < Real.sin (η / 2) := Real.sin_pos_of_pos_of_lt_pi (by linarith [hη.1]) (by linarith [hη.2])
  have hr : cy_r M η = 2 * M * Real.cos (η / 2) ^ 2 := by unfold cy_r; rw [← hc2]; ring
  have hd : 1 - 2 * M / cy_r M η = -(Real.sin (η / 2) ^ 2 / Real.cos (η / 2) ^ 2) := by
    rw [hr]; field_simp; nlinarith
  rw [Real.tan_eq_sin_div_cos]
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · rw [hr]; field_simp; nlinarith
  · rw [hd, hs, inv_neg, inv_div]; field_simp; norm_num
  · rw [← hc2]; ring
  · rw [hc]; field_simp; nlinarith
  · unfold cy_r; ring

/-- **4a**: at `z = iρ` (`dz/dρ = i`): `−4M²cos⁴(z/2)·i² = 4M²cosh⁴(ρ/2)`, `tan²(z/2) = −tanh²(ρ/2)`,
`(1 + cos z)² = (1 + cosh ρ)²`. -/
theorem cy_regionI_coeffs (M ρ : ℝ) :
    -4 * (M : ℂ) ^ 2 * Complex.cos ((ρ : ℂ) * I / 2) ^ 4 * I ^ 2 =
      ((4 * M ^ 2 * Real.cosh (ρ / 2) ^ 4 : ℝ) : ℂ) ∧
    Complex.tan ((ρ : ℂ) * I / 2) ^ 2 = -((Real.tanh (ρ / 2) ^ 2 : ℝ) : ℂ) ∧
    (1 + Complex.cos ((ρ : ℂ) * I)) ^ 2 = (((1 + Real.cosh ρ) ^ 2 : ℝ) : ℂ) := by
  have e : (ρ : ℂ) * I / 2 = ((ρ / 2 : ℝ) : ℂ) * I := by push_cast; ring
  rw [e, Complex.cos_mul_I, Complex.tan_mul_I, Complex.cos_mul_I]
  refine ⟨?_, ?_, ?_⟩
  · push_cast; rw [Complex.I_sq]; ring
  · push_cast; rw [mul_pow, Complex.I_sq]; ring
  · push_cast; rfl

/-- **4a, the identification**: with `r = M(1 + cosh ρ)`, `ρ ≠ 0`: `1 − 2M/r = tanh²(ρ/2)` and
`(dr/dρ)²/(1 − 2M/r) = 4M²cosh⁴(ρ/2)`. -/
theorem cy_regionI_schw (hM : 0 < M) {ρ : ℝ} (hρ : ρ ≠ 0) :
    1 - 2 * M / (M * (1 + Real.cosh ρ)) = Real.tanh (ρ / 2) ^ 2 ∧
    (M * Real.sinh ρ) ^ 2 / (1 - 2 * M / (M * (1 + Real.cosh ρ))) =
      4 * M ^ 2 * Real.cosh (ρ / 2) ^ 4 := by
  have hc : Real.cosh ρ = Real.cosh (ρ / 2) ^ 2 + Real.sinh (ρ / 2) ^ 2 := by
    rw [← Real.cosh_two_mul]; ring_nf
  have hs : Real.sinh ρ = 2 * Real.sinh (ρ / 2) * Real.cosh (ρ / 2) := by
    rw [← Real.sinh_two_mul]; ring_nf
  have hcs := Real.cosh_sq (ρ / 2)
  have hcpos := Real.cosh_pos (ρ / 2)
  have hsne : Real.sinh (ρ / 2) ≠ 0 := Real.sinh_ne_zero.2 (by intro h; apply hρ; linarith)
  rw [Real.tanh_eq_sinh_div_cosh, hc, hs]
  have hd : 1 - 2 * M / (M * (1 + (Real.cosh (ρ / 2) ^ 2 + Real.sinh (ρ / 2) ^ 2))) =
      (Real.sinh (ρ / 2) / Real.cosh (ρ / 2)) ^ 2 := by
    field_simp; nlinarith
  refine ⟨hd, ?_⟩
  rw [hd]; field_simp; norm_num

/-- **5a**: at `z = π + iρ′` (`dz/dρ′ = i`): `−4M²cos⁴(z/2)·i² = 4M²sinh⁴(ρ′/2)` and
`tan²(z/2) = −coth²(ρ′/2)`, `coth = cosh/sinh`. -/
theorem cy_backseam_coeffs (M ρ : ℝ) :
    -4 * (M : ℂ) ^ 2 * Complex.cos (((Real.pi : ℂ) + (ρ : ℂ) * I) / 2) ^ 4 * I ^ 2 =
      ((4 * M ^ 2 * Real.sinh (ρ / 2) ^ 4 : ℝ) : ℂ) ∧
    Complex.tan (((Real.pi : ℂ) + (ρ : ℂ) * I) / 2) ^ 2 =
      -(((Real.cosh (ρ / 2) / Real.sinh (ρ / 2)) ^ 2 : ℝ) : ℂ) := by
  have e : ((Real.pi : ℂ) + (ρ : ℂ) * I) / 2 = ((ρ / 2 : ℝ) : ℂ) * I + (Real.pi : ℂ) / 2 := by
    push_cast; ring
  rw [e, Complex.tan_eq_sin_div_cos, Complex.cos_add_pi_div_two, Complex.sin_add_pi_div_two,
    Complex.sin_mul_I, Complex.cos_mul_I]
  refine ⟨?_, ?_⟩
  · push_cast
    have h4 : I ^ 4 = 1 := by rw [show (4:ℕ) = 2 * 2 from rfl, pow_mul, Complex.I_sq]; norm_num
    rw [show (-(Complex.sinh ((ρ:ℂ) / 2) * I)) ^ 4 = Complex.sinh ((ρ:ℂ) / 2) ^ 4 * I ^ 4 by ring,
      h4, Complex.I_sq]
    ring
  · push_cast
    rw [div_pow, div_pow, neg_sq, mul_pow, Complex.I_sq, mul_neg_one, div_neg]

/-- **5a, the identification**: with `r = M(1 − cosh ρ′)`, `ρ′ ≠ 0`: `1 − 2M/r = coth²(ρ′/2)` and
`(dr/dρ′)²/(1 − 2M/r) = 4M²sinh⁴(ρ′/2)`. -/
theorem cy_backseam_schw (hM : 0 < M) {ρ : ℝ} (hρ : ρ ≠ 0) :
    1 - 2 * M / (M * (1 - Real.cosh ρ)) = (Real.cosh (ρ / 2) / Real.sinh (ρ / 2)) ^ 2 ∧
    (M * Real.sinh ρ) ^ 2 / (1 - 2 * M / (M * (1 - Real.cosh ρ))) =
      4 * M ^ 2 * Real.sinh (ρ / 2) ^ 4 := by
  have hc : Real.cosh ρ = Real.cosh (ρ / 2) ^ 2 + Real.sinh (ρ / 2) ^ 2 := by
    rw [← Real.cosh_two_mul]; ring_nf
  have hs : Real.sinh ρ = 2 * Real.sinh (ρ / 2) * Real.cosh (ρ / 2) := by
    rw [← Real.sinh_two_mul]; ring_nf
  have hcs := Real.cosh_sq (ρ / 2)
  have hcpos := Real.cosh_pos (ρ / 2)
  have hsne : Real.sinh (ρ / 2) ≠ 0 := Real.sinh_ne_zero.2 (by intro h; apply hρ; linarith)
  rw [hc, hs]
  have hd : 1 - 2 * M / (M * (1 - (Real.cosh (ρ / 2) ^ 2 + Real.sinh (ρ / 2) ^ 2))) =
      (Real.cosh (ρ / 2) / Real.sinh (ρ / 2)) ^ 2 := by
    have : 1 - (Real.cosh (ρ / 2) ^ 2 + Real.sinh (ρ / 2) ^ 2) = -(2 * Real.sinh (ρ / 2) ^ 2) := by
      linarith
    rw [this]; field_simp; nlinarith
  refine ⟨hd, ?_⟩
  rw [hd]; field_simp; norm_num

/-- **6a**: the six patches' `r`-ranges, each map onto its range. -/
theorem cy_patches (hM : 0 < M) :
    -- black-hole interior `η ∈ (0, π)`: `r ∈ (0, 2M)`, onto
    (∀ η ∈ Ioo 0 Real.pi, cy_r M η ∈ Ioo 0 (2 * M)) ∧
    (∀ r ∈ Ioo 0 (2 * M), ∃ η ∈ Ioo 0 Real.pi, cy_r M η = r) ∧
    -- white-hole interior `η ↦ −η`: `r` even, `τ` odd
    (∀ η, cy_r M (-η) = cy_r M η) ∧ (∀ η, cy_τ M (-η) = -cy_τ M η) ∧
    -- the two exteriors `z = ±iρ`: `r = M(1 + cosh ρ) ∈ (2M, ∞)`, onto
    (∀ ρ : ℝ, ∀ s : ℝ, s = 1 ∨ s = -1 →
      (M : ℂ) * (1 + Complex.cos (s * ρ * I)) = ((M * (1 + Real.cosh ρ) : ℝ) : ℂ)) ∧
    (∀ ρ > 0, M * (1 + Real.cosh ρ) ∈ Ioi (2 * M)) ∧
    (∀ r ∈ Ioi (2 * M), ∃ ρ > 0, M * (1 + Real.cosh ρ) = r) ∧
    -- the two `r < 0` regions `z = π ± iρ′`: `r = M(1 − cosh ρ′) ∈ (−∞, 0)`, onto
    (∀ ρ : ℝ, ∀ s : ℝ, s = 1 ∨ s = -1 →
      (M : ℂ) * (1 + Complex.cos (Real.pi + s * ρ * I)) = ((M * (1 - Real.cosh ρ) : ℝ) : ℂ)) ∧
    (∀ ρ > 0, M * (1 - Real.cosh ρ) ∈ Iio 0) ∧
    (∀ r ∈ Iio 0, ∃ ρ > 0, M * (1 - Real.cosh ρ) = r) := by
  have hcI : ∀ (ρ : ℝ) (s : ℝ), s = 1 ∨ s = -1 →
      Complex.cos ((s : ℂ) * ρ * I) = ((Real.cosh ρ : ℝ) : ℂ) := by
    intro ρ s hs
    rcases hs with rfl | rfl
    · simp [Complex.cos_mul_I, Complex.ofReal_cosh]
    · have : ((-1 : ℝ) : ℂ) * ρ * I = ((-ρ : ℝ) : ℂ) * I := by push_cast; ring
      rw [this, Complex.cos_mul_I, ← Complex.ofReal_cosh, Real.cosh_neg]
  refine ⟨fun η hη => ?_, fun r hr => ?_, fun η => ?_, fun η => ?_, fun ρ s hs => ?_,
    fun ρ hρ => ?_, fun r hr => ?_, fun ρ s hs => ?_, fun ρ hρ => ?_, fun r hr => ?_⟩
  · have h1 := Real.cos_lt_cos_of_nonneg_of_le_pi le_rfl hη.2.le hη.1
    have h2 := Real.cos_lt_cos_of_nonneg_of_le_pi hη.1.le le_rfl hη.2
    rw [Real.cos_zero] at h1; rw [Real.cos_pi] at h2
    unfold cy_r; constructor <;> nlinarith
  · have hy1 : -1 < r / M - 1 := by
      have : 0 < r / M := div_pos hr.1 hM; linarith
    have hy2 : r / M - 1 < 1 := by
      have : r / M < 2 := by rw [div_lt_iff₀ hM]; linarith [hr.2]
      linarith
    refine ⟨Real.arccos (r / M - 1), ⟨Real.arccos_pos.2 hy2, Real.arccos_lt_pi.2 hy1⟩, ?_⟩
    unfold cy_r
    rw [Real.cos_arccos hy1.le hy2.le]; field_simp; ring
  · simp [cy_r]
  · simp [cy_τ]; ring
  · rw [hcI ρ s hs]; push_cast; ring
  · have := Real.one_lt_cosh.2 hρ.ne'
    show 2 * M < M * (1 + Real.cosh ρ); nlinarith
  · have hy : 1 < r / M - 1 := by
      have : 2 < r / M := by rw [lt_div_iff₀ hM]; linarith [show (2:ℝ) * M < r from hr]
      linarith
    refine ⟨Real.arcosh (r / M - 1), Real.arcosh_pos hy, ?_⟩
    rw [Real.cosh_arcosh hy.le]; field_simp; ring
  · have e : (Real.pi : ℂ) + s * ρ * I = (s : ℂ) * ρ * I + Real.pi := by ring
    rw [e, Complex.cos_add_pi, hcI ρ s hs]; push_cast; ring
  · have := Real.one_lt_cosh.2 hρ.ne'
    show M * (1 - Real.cosh ρ) < 0; nlinarith
  · have hy : 1 < 1 - r / M := by
      have : r / M < 0 := div_neg_of_neg_of_pos hr hM
      linarith
    refine ⟨Real.arcosh (1 - r / M), Real.arcosh_pos hy, ?_⟩
    rw [Real.cosh_arcosh hy.le]; field_simp; ring
end CyForms


namespace KRModel
open Model SEModel Kruskal

variable {M : ℝ} (hM : 0 < M)

include hM in
/-- **6c**: no point of Kruskal's `{UV < 1}` has the back-seam radius `r = M(1 − cosh ρ′)`, `ρ′ > 0`: `rK > 0` there
(`sk_rK_spec`) and `M(1 − cosh ρ′) < 0`. -/
theorem cy_backseam_not_kruskal {p : P} (hp : p ∈ sk_kM) {ρ : ℝ} (hρ : 0 < ρ) :
    rK M p ≠ M * (1 - Real.cosh ρ) := by
  have h1 := (sk_rK_spec hM hp).1
  have h2 := Real.one_lt_cosh.2 hρ.ne'
  intro h; rw [h] at h1; nlinarith

end KRModel



namespace CCModel
open Model SEModel Kruskal NModel STModel ContinuousLinearMap

variable {M : ℝ}

/-- `s(η) = sin(η/2)·e^{r/4M}`, `r = M(1 + cos η)`, so `s² = −hK(r) = (1 − r/2M) e^{r/2M}`. -/
noncomputable def cc_s (M η : ℝ) : ℝ := Real.sin (η / 2) * Real.exp (cy_r M η / (4 * M))

/-- **The chart** `Φ(η, t) = (s e^{−t/4M}, s e^{t/4M})` into Kruskal's `(U, V)`. -/
noncomputable def cc_Φ (M η t : ℝ) : P :=
  (cc_s M η * Real.exp (-t / (4 * M)), cc_s M η * Real.exp (t / (4 * M)))

lemma cc_exp_pair (M t : ℝ) : Real.exp (-t / (4 * M)) * Real.exp (t / (4 * M)) = 1 := by
  rw [← Real.exp_add]; ring_nf; simp

lemma cc_exp_sq (hM : 0 < M) (x : ℝ) :
    Real.exp (-x / (2 * M)) * Real.exp (x / (4 * M)) ^ 2 = 1 := by
  rw [sq, ← Real.exp_add, ← Real.exp_add]
  have : -x / (2 * M) + (x / (4 * M) + x / (4 * M)) = 0 := by field_simp; ring
  rw [this, Real.exp_zero]

lemma cc_sin_half_sq (η : ℝ) : 2 * Real.sin (η / 2) ^ 2 = 1 - Real.cos η := by
  have h1 := cy_cos_half_sq η; have h2 := Real.sin_sq_add_cos_sq (η / 2); linarith

lemma cc_hK (hM : 0 < M) (η : ℝ) : hK M (cy_r M η) = -(cc_s M η) ^ 2 := by
  have h := cc_sin_half_sq η
  have he : Real.exp (cy_r M η / (4 * M)) ^ 2 = Real.exp (cy_r M η / (2 * M)) := by
    rw [sq, ← Real.exp_add]; congr 1; field_simp; ring
  unfold hK cc_s
  rw [mul_pow, he]
  have : cy_r M η / (2 * M) - 1 = -Real.sin (η / 2) ^ 2 := by
    unfold cy_r; field_simp; linarith
  rw [this]; ring

lemma cc_prod (M η t : ℝ) : (cc_Φ M η t).1 * (cc_Φ M η t).2 = cc_s M η ^ 2 := by
  show cc_s M η * Real.exp (-t / (4 * M)) * (cc_s M η * Real.exp (t / (4 * M))) = _
  have := cc_exp_pair M t
  calc _ = cc_s M η ^ 2 * (Real.exp (-t / (4 * M)) * Real.exp (t / (4 * M))) := by ring
    _ = _ := by rw [this, mul_one]

lemma cc_s_pos (hη : η ∈ Ioo 0 Real.pi) : 0 < cc_s M η := by
  unfold cc_s
  have : 0 < Real.sin (η / 2) :=
    Real.sin_pos_of_pos_of_lt_pi (by linarith [hη.1]) (by linarith [hη.2, Real.pi_pos])
  positivity

lemma cc_r_pos (hM : 0 < M) (hη : η ∈ Ioo 0 Real.pi) : 0 < cy_r M η := by
  unfold cy_r; have := cy_cos_gt hη
  have : 0 < 1 + Real.cos η := by linarith
  positivity

/-- **2a-①, the image**: for `0 < η < π`, `Φ(η, t)` lies in `W = {V > 0, UV < 1}` with `U > 0` (the black-hole
interior quadrant), and `rK(Φ(η, t)) = M(1 + cos η)`. -/
theorem cc_Φ_mem (hM : 0 < M) {η : ℝ} (hη : η ∈ Ioo 0 Real.pi) (t : ℝ) :
    cc_Φ M η t ∈ seWS ∧ 0 < (cc_Φ M η t).1 ∧ cc_Φ M η t ∈ sk_kM ∧
      rK M (cc_Φ M η t) = cy_r M η := by
  have hs := cc_s_pos (M := M) hη
  have hr := cc_r_pos hM hη
  have hgt := hK_gt hM hr
  have hk := cc_hK hM η
  have hp := cc_prod M η t
  have h1 : (cc_Φ M η t).1 * (cc_Φ M η t).2 < 1 := by rw [hp]; linarith
  refine ⟨⟨by show 0 < cc_s M η * Real.exp (t / (4 * M)); positivity, h1⟩,
    by show 0 < cc_s M η * Real.exp (-t / (4 * M)); positivity, h1, ?_⟩
  show rinv M (-((cc_Φ M η t).1 * (cc_Φ M η t).2)) = _
  rw [hp, ← neg_neg (cc_s M η ^ 2), ← hk, neg_neg, rinv_hK hM hr]

/-- **2a-①, injectivity**: `Φ` is one-to-one on `(0, π) × ℝ`. -/
theorem cc_Φ_inj (hM : 0 < M) {η η' t t' : ℝ} (hη : η ∈ Ioo 0 Real.pi)
    (hη' : η' ∈ Ioo 0 Real.pi) (h : cc_Φ M η t = cc_Φ M η' t') : η = η' ∧ t = t' := by
  have hr := (cc_Φ_mem hM hη t).2.2.2
  have hr' := (cc_Φ_mem hM hη' t').2.2.2
  rw [h] at hr
  have hrr : cy_r M η = cy_r M η' := hr.symm.trans hr'
  have hc : Real.cos η = Real.cos η' := by
    unfold cy_r at hrr
    have := mul_left_cancel₀ hM.ne' hrr; linarith
  have he : η = η' := Real.injOn_cos ⟨hη.1.le, hη.2.le⟩ ⟨hη'.1.le, hη'.2.le⟩ hc
  subst he
  refine ⟨rfl, ?_⟩
  have h2 := congrArg Prod.snd h
  simp only [cc_Φ] at h2
  have := mul_left_cancel₀ (cc_s_pos (M := M) hη).ne' h2
  have := Real.exp_injective this
  have h4 : (0:ℝ) < 4 * M := by positivity
  field_simp at this; linarith

lemma cc_hasDerivAt_s (hM : 0 < M) (η : ℝ) :
    HasDerivAt (cc_s M) (Real.exp (cy_r M η / (4 * M)) * Real.cos (η / 2) ^ 3 / 2) η := by
  have h1 : HasDerivAt (fun x => Real.sin (x / 2)) (Real.cos (η / 2) * (1 / 2)) η :=
    (Real.hasDerivAt_sin _).comp η ((hasDerivAt_id η).div_const 2)
  have h2 : HasDerivAt (fun x => cy_r M x / (4 * M)) (-(M * Real.sin η) / (4 * M)) η := by
    have := ((hasDerivAt_const η (1:ℝ)).add (Real.hasDerivAt_cos η)).const_mul M |>.div_const (4 * M)
    convert this using 1
    · funext x; rfl
    · ring
  have h3 := h1.mul ((Real.hasDerivAt_exp _).comp η h2)
  convert h3 using 1
  · funext x; rfl
  have hs : Real.sin η = 2 * Real.sin (η / 2) * Real.cos (η / 2) := by
    rw [← Real.sin_two_mul]; ring_nf
  have hsc := Real.sin_sq_add_cos_sq (η / 2)
  simp only [Function.comp_apply]
  rw [hs]; field_simp
  have : Real.cos (η / 2) ^ 3 = Real.cos (η / 2) * (1 - Real.sin (η / 2) ^ 2) := by
    rw [show 1 - Real.sin (η / 2) ^ 2 = Real.cos (η / 2) ^ 2 by linarith]; ring
  rw [this]; ring

/-- `∂_ηΦ = s′(η)·(e^{−t/4M}, e^{t/4M})`, `s′ = e^{r/4M} cos³(η/2)/2`. -/
noncomputable def cc_a (M η t : ℝ) : P :=
  ((Real.exp (cy_r M η / (4 * M)) * Real.cos (η / 2) ^ 3 / 2) * Real.exp (-t / (4 * M)),
   (Real.exp (cy_r M η / (4 * M)) * Real.cos (η / 2) ^ 3 / 2) * Real.exp (t / (4 * M)))

/-- `∂_tΦ = (s/4M)·(−e^{−t/4M}, e^{t/4M})`. -/
noncomputable def cc_b (M η t : ℝ) : P :=
  (cc_s M η * (Real.exp (-t / (4 * M)) * (-1 / (4 * M))),
   cc_s M η * (Real.exp (t / (4 * M)) * (1 / (4 * M))))

lemma cc_dη (hM : 0 < M) (η t : ℝ) : HasDerivAt (fun x => cc_Φ M x t) (cc_a M η t) η :=
  ((cc_hasDerivAt_s hM η).mul_const _).prodMk ((cc_hasDerivAt_s hM η).mul_const _)

lemma cc_dt (M η t : ℝ) : HasDerivAt (fun x => cc_Φ M η x) (cc_b M η t) t := by
  refine HasDerivAt.prodMk ?_ ?_
  · have h := ((Real.hasDerivAt_exp _).comp t (((hasDerivAt_id t).neg).div_const (4 * M))).const_mul
      (cc_s M η)
    convert h using 1
    · funext x; simp [neg_div]
    · simp [neg_div]
  · have h := ((Real.hasDerivAt_exp _).comp t ((hasDerivAt_id t).div_const (4 * M))).const_mul
      (cc_s M η)
    convert h using 1
    · simp
    · simp

lemma cc_exp_neg (x : ℝ) (c : ℝ) : Real.exp (-x / c) = (Real.exp (x / c))⁻¹ := by
  rw [neg_div, Real.exp_neg]

/-- **2a-①, the pullback**: through `se_hRep`, `g(∂_ηΦ, ∂_ηΦ) = cy_A = −(M(1 + cos η))² = −4M²cos⁴(η/2)`,
`g(∂_tΦ, ∂_tΦ) = cy_B = (1 − cos η)/(1 + cos η) = tan²(η/2)`, `g(∂_ηΦ, ∂_tΦ) = 0`: `Φ*g` is campaign 112's
interior metric `cy_g`. -/
theorem cc_pullback (hM : 0 < M) (p : seW) {η : ℝ} (hη : η ∈ Ioo 0 Real.pi) (t : ℝ) :
    hRep (se_S hM).g p (cc_Φ M η t) (cc_a M η t) (cc_a M η t) = cy_A M η ∧
    hRep (se_S hM).g p (cc_Φ M η t) (cc_b M η t) (cc_b M η t) = cy_B η ∧
    hRep (se_S hM).g p (cc_Φ M η t) (cc_a M η t) (cc_b M η t) = 0 := by
  obtain ⟨hW, -, hk, hr⟩ := cc_Φ_mem hM hη t
  have hc2 := cy_cos_half_sq η
  have hsn := cc_sin_half_sq η
  have hcpos : 0 < Real.cos (η / 2) :=
    Real.cos_pos_of_mem_Ioo ⟨by linarith [hη.1, Real.pi_pos], by linarith [hη.2]⟩
  have hrv : cy_r M η = 2 * M * Real.cos (η / 2) ^ 2 := by unfold cy_r; rw [← hc2]; ring
  have hG : Real.exp (-cy_r M η / (2 * M)) = (Real.exp (cy_r M η / (4 * M)) ^ 2)⁻¹ := by
    rw [cc_exp_neg, sq, ← Real.exp_add]; congr 2; field_simp; ring
  rw [se_hRep hM p hW]
  simp only [smul_apply, smul_eq_mul, gM_apply, cc_a, cc_b, cc_s, FS, hr, hG, cc_exp_neg t]
  have hE := Real.exp_pos (cy_r M η / (4 * M))
  have he := Real.exp_pos (t / (4 * M))
  refine ⟨?_, ?_, ?_⟩
  · unfold cy_A
    rw [show 1 + Real.cos η = 2 * Real.cos (η / 2) ^ 2 by linarith, hrv]
    field_simp; ring
  · unfold cy_B
    rw [show 1 + Real.cos η = 2 * Real.cos (η / 2) ^ 2 by linarith,
      show 1 - Real.cos η = 2 * Real.sin (η / 2) ^ 2 by linarith, hrv]
    field_simp; ring
  · ring

/-! ### ② The cycloid is a geodesic of `se_S` -/

/-- `η′ = g(η)`, `g(x) = 1/(M(1 + cos x))`. -/
noncomputable def cc_g (M x : ℝ) : ℝ := 1 / (M * (1 + Real.cos x))

lemma cc_g_contDiffOn (hM : 0 < M) : ContDiffOn ℝ 2 (cc_g M) (Ioo 0 Real.pi) := by
  unfold cc_g
  refine contDiffOn_const.div (by fun_prop) fun x hx => ?_
  have := cy_cos_gt hx
  have : 0 < 1 + Real.cos x := by linarith
  positivity

/-- **2a-②-i**: `η(τ)` is `C²` on `(0, Mπ)` (from `η′ = g ∘ η`, `g` smooth). -/
theorem cc_η_contDiffOn (hM : 0 < M) : ContDiffOn ℝ 2 (cy_η M) (Ioo 0 (M * Real.pi)) := by
  have hI : IsOpen (Ioo 0 (M * Real.pi)) := isOpen_Ioo
  have hder : ∀ τ ∈ Ioo 0 (M * Real.pi), deriv (cy_η M) τ = cc_g M (cy_η M τ) := fun τ hτ =>
    (cy_hasDerivAt_η hM hτ).deriv
  have hd : DifferentiableOn ℝ (cy_η M) (Ioo 0 (M * Real.pi)) := fun τ hτ =>
    (cy_hasDerivAt_η hM hτ).differentiableAt.differentiableWithinAt
  have hmaps : MapsTo (cy_η M) (Ioo 0 (M * Real.pi)) (Ioo 0 Real.pi) := fun τ hτ =>
    cy_η_mem_Ioo hM hτ
  have h1 : ContDiffOn ℝ 1 (cy_η M) (Ioo 0 (M * Real.pi)) := by
    rw [show (1 : WithTop ℕ∞) = 0 + 1 from rfl, contDiffOn_succ_iff_deriv_of_isOpen hI]
    refine ⟨hd, by simp, ?_⟩
    rw [contDiffOn_zero]
    exact ((cc_g_contDiffOn hM).continuousOn.comp hd.continuousOn hmaps).congr hder
  rw [show (2 : WithTop ℕ∞) = 1 + 1 from rfl, contDiffOn_succ_iff_deriv_of_isOpen hI]
  refine ⟨hd, by simp, ?_⟩
  exact (((cc_g_contDiffOn hM).of_le (by norm_num)).comp h1 hmaps).congr hder

/-- `S(τ) = s(η(τ))` -/
noncomputable def cc_S (M τ : ℝ) : ℝ := cc_s M (cy_η M τ)

lemma cc_s_contDiff (M : ℝ) : ContDiff ℝ 2 (cc_s M) := by
  unfold cc_s cy_r; fun_prop

lemma cc_S_contDiffOn (hM : 0 < M) : ContDiffOn ℝ 2 (cc_S M) (Ioo 0 (M * Real.pi)) :=
  (cc_s_contDiff M).comp_contDiffOn (cc_η_contDiffOn hM)

/-- `S′ = s′(η)·η′` -/
lemma cc_hasDerivAt_S (hM : 0 < M) {τ : ℝ} (hτ : τ ∈ Ioo 0 (M * Real.pi)) :
    HasDerivAt (cc_S M) (Real.exp (cy_r M (cy_η M τ) / (4 * M)) * Real.cos (cy_η M τ / 2) ^ 3 / 2 *
      (1 / (M * (1 + Real.cos (cy_η M τ))))) τ :=
  (cc_hasDerivAt_s hM _).comp τ (cy_hasDerivAt_η hM hτ)

/-- **The unit identity** `F(r)·S′² = 1` (`F = kr_φ`), i.e. `g(γ′, γ′) = −1`. -/
lemma cc_unit (hM : 0 < M) {τ : ℝ} (hτ : τ ∈ Ioo 0 (M * Real.pi)) :
    KRModel.kr_φ M (cy_r M (cy_η M τ)) * deriv (cc_S M) τ ^ 2 = 1 := by
  rw [(cc_hasDerivAt_S hM hτ).deriv]
  have hη := cy_η_mem_Ioo hM hτ
  set η := cy_η M τ
  have hc2 := cy_cos_half_sq η
  have hcpos : 0 < Real.cos (η / 2) :=
    Real.cos_pos_of_mem_Ioo ⟨by linarith [hη.1, Real.pi_pos], by linarith [hη.2]⟩
  have hrv : cy_r M η = 2 * M * Real.cos (η / 2) ^ 2 := by unfold cy_r; rw [← hc2]; ring
  have hG : Real.exp (-cy_r M η / (2 * M)) = (Real.exp (cy_r M η / (4 * M)) ^ 2)⁻¹ := by
    rw [cc_exp_neg, sq, ← Real.exp_add]; congr 2; field_simp; ring
  have hE := Real.exp_pos (cy_r M η / (4 * M))
  simp only [KRModel.kr_φ, hG]
  rw [show 1 + Real.cos η = 2 * Real.cos (η / 2) ^ 2 by linarith, hrv]
  field_simp; ring

/-- **The scalar geodesic identity** `F S″ + D S′² = 0`, `D = −F′(r) S / hK′(r)` (`= ∂_U F` at `U = V = S`):
from differentiating `F(r) S′² = 1` and `hK(r) = −S²`. -/
lemma cc_scalar (hM : 0 < M) {τ : ℝ} (hτ : τ ∈ Ioo 0 (M * Real.pi)) :
    KRModel.kr_φ M (cy_r M (cy_η M τ)) * deriv (deriv (cc_S M)) τ +
      (-(KRModel.kr_φ1 M (cy_r M (cy_η M τ))) * cc_S M τ / hK' M (cy_r M (cy_η M τ))) *
        deriv (cc_S M) τ ^ 2 = 0 := by
  have hI : IsOpen (Ioo 0 (M * Real.pi)) := isOpen_Ioo
  have hη := cy_η_mem_Ioo hM hτ
  have hr := cc_r_pos hM hη
  have hrd : HasDerivAt (fun σ => cy_r M (cy_η M σ))
      (-(Real.sin (cy_η M τ)) / (1 + Real.cos (cy_η M τ))) τ := (cy_radial hM hτ).1
  -- `S′` is differentiable at `τ`
  have hQ : DifferentiableAt ℝ (fun x => Real.exp (cy_r M x / (4 * M)) * Real.cos (x / 2) ^ 3 / 2 *
      (1 / (M * (1 + Real.cos x)))) (cy_η M τ) := by
    have hc := cy_cos_gt hη
    have hne : M * (1 + Real.cos (cy_η M τ)) ≠ 0 := by
      have : 0 < 1 + Real.cos (cy_η M τ) := by linarith
      positivity
    unfold cy_r
    exact (by fun_prop : DifferentiableAt ℝ (fun x => Real.exp (M * (1 + Real.cos x) / (4 * M)) *
      Real.cos (x / 2) ^ 3 / 2) _).mul ((differentiableAt_const _).div (by fun_prop) hne)
  have hL : deriv (cc_S M) =ᶠ[𝓝 τ] fun σ => Real.exp (cy_r M (cy_η M σ) / (4 * M)) *
      Real.cos (cy_η M σ / 2) ^ 3 / 2 * (1 / (M * (1 + Real.cos (cy_η M σ)))) := by
    filter_upwards [hI.mem_nhds hτ] with σ hσ using (cc_hasDerivAt_S hM hσ).deriv
  have hS1d : DifferentiableAt ℝ (deriv (cc_S M)) τ :=
    (hQ.comp τ (cy_hasDerivAt_η hM hτ).differentiableAt).congr_of_eventuallyEq hL
  have hSd : HasDerivAt (cc_S M) (deriv (cc_S M) τ) τ :=
    (cc_hasDerivAt_S hM hτ).differentiableAt.hasDerivAt
  -- (i) the unit identity, differentiated
  have hφ := (KRModel.kr_hasDerivAt_φ hM hr).comp τ hrd
  have hunit := hφ.mul (hS1d.hasDerivAt.mul hS1d.hasDerivAt)
  have hconst : (fun σ => (KRModel.kr_φ M ∘ fun σ => cy_r M (cy_η M σ)) σ *
      (deriv (cc_S M) σ * deriv (cc_S M) σ)) =ᶠ[𝓝 τ] fun _ => (1 : ℝ) := by
    filter_upwards [hI.mem_nhds hτ] with σ hσ
    have := cc_unit hM hσ
    simp only [Function.comp_apply]; rw [← this]; ring
  have h0 := hunit.unique ((hasDerivAt_const τ (1 : ℝ)).congr_of_eventuallyEq hconst)
  simp only [Function.comp_apply] at h0
  -- (ii) `hK(r) = −S²`, differentiated
  have hk1 := (hasDerivAt_hK hM (cy_r M (cy_η M τ))).comp τ hrd
  have hk2 := (hSd.mul hSd).neg
  have hkeq : (hK M ∘ fun σ => cy_r M (cy_η M σ)) = fun σ => -(cc_S M σ * cc_S M σ) := by
    funext σ; simp only [Function.comp_apply]; rw [cc_hK hM]; unfold cc_S; ring
  rw [hkeq] at hk1
  have h1 := hk1.unique hk2
  have hKp : hK' M (cy_r M (cy_η M τ)) ≠ 0 := (SRModel.sa_hK'_pos hM hr).ne'
  have hS1 : deriv (cc_S M) τ ≠ 0 := by
    intro h; have := cc_unit hM hτ; rw [h] at this; simp at this
  have hrp : -(Real.sin (cy_η M τ)) / (1 + Real.cos (cy_η M τ)) =
      -(2 * cc_S M τ * deriv (cc_S M) τ) / hK' M (cy_r M (cy_η M τ)) := by
    rw [eq_div_iff hKp, mul_comm]; linear_combination h1
  rw [hrp] at h0
  simp only [Pi.mul_apply] at h0
  have key : 2 * deriv (cc_S M) τ * (KRModel.kr_φ M (cy_r M (cy_η M τ)) * deriv (deriv (cc_S M)) τ +
      (-(KRModel.kr_φ1 M (cy_r M (cy_η M τ))) * cc_S M τ / hK' M (cy_r M (cy_η M τ))) *
        deriv (cc_S M) τ ^ 2) = 0 := by
    rw [← h0]; ring
  rcases mul_eq_zero.1 key with h | h
  · exact absurd h (mul_ne_zero two_ne_zero hS1)
  · exact h

/-- The chart curve `c(τ) = Φ(η(τ), t₀) = (S e^{−t₀/4M}, S e^{t₀/4M})`. -/
noncomputable def cc_c (M t₀ τ : ℝ) : P :=
  (cc_S M τ * Real.exp (-t₀ / (4 * M)), cc_S M τ * Real.exp (t₀ / (4 * M)))

lemma cc_c_eq (M t₀ τ : ℝ) : cc_c M t₀ τ = cc_Φ M (cy_η M τ) t₀ := rfl

/-- **The cycloid on Schwarzschild's manifold**: `γ(τ) = Φ(η(τ), t₀)` in `W` for `0 < τ < Mπ` (a junk point of
`W` outside). -/
noncomputable def cc_γ (hM : 0 < M) (t₀ τ : ℝ) : seW :=
  if h : τ ∈ Ioo 0 (M * Real.pi) then
    ⟨cc_c M t₀ τ, (cc_Φ_mem hM (cy_η_mem_Ioo hM h) t₀).1⟩
  else ⟨((0 : ℝ), (1 : ℝ)), ⟨one_pos, by norm_num⟩⟩

lemma cc_γ_val (hM : 0 < M) (t₀ : ℝ) {τ : ℝ} (hτ : τ ∈ Ioo 0 (M * Real.pi)) :
    (cc_γ hM t₀ τ : P) = cc_c M t₀ τ := by
  simp [cc_γ, hτ]

lemma cc_hasDerivAt_c (hM : 0 < M) (t₀ : ℝ) {τ : ℝ} (hτ : τ ∈ Ioo 0 (M * Real.pi)) :
    HasDerivAt (cc_c M t₀)
      (deriv (cc_S M) τ * Real.exp (-t₀ / (4 * M)), deriv (cc_S M) τ * Real.exp (t₀ / (4 * M))) τ := by
  have h := (cc_hasDerivAt_S hM hτ).differentiableAt.hasDerivAt
  exact (h.mul_const _).prodMk (h.mul_const _)

lemma cc_deriv_c (hM : 0 < M) (t₀ : ℝ) :
    ∀ τ ∈ Ioo 0 (M * Real.pi), deriv (cc_c M t₀) τ =
      (deriv (cc_S M) τ * Real.exp (-t₀ / (4 * M)), deriv (cc_S M) τ * Real.exp (t₀ / (4 * M))) :=
  fun _ hτ => (cc_hasDerivAt_c hM t₀ hτ).deriv

lemma cc_deriv2_c (hM : 0 < M) (t₀ : ℝ) {τ : ℝ} (hτ : τ ∈ Ioo 0 (M * Real.pi)) :
    deriv (deriv (cc_c M t₀)) τ =
      (deriv (deriv (cc_S M)) τ * Real.exp (-t₀ / (4 * M)),
        deriv (deriv (cc_S M)) τ * Real.exp (t₀ / (4 * M))) := by
  have hI : IsOpen (Ioo 0 (M * Real.pi)) := isOpen_Ioo
  have hev : deriv (cc_c M t₀) =ᶠ[𝓝 τ] fun σ =>
      (deriv (cc_S M) σ * Real.exp (-t₀ / (4 * M)), deriv (cc_S M) σ * Real.exp (t₀ / (4 * M))) := by
    filter_upwards [hI.mem_nhds hτ] with σ hσ using cc_deriv_c hM t₀ σ hσ
  rw [hev.deriv_eq]
  have hS2 : ContDiffAt ℝ 2 (cc_S M) τ := (cc_S_contDiffOn hM).contDiffAt (hI.mem_nhds hτ)
  have hd : DifferentiableAt ℝ (deriv (cc_S M)) τ := by
    have h1 : ContDiffAt ℝ 1 (deriv (cc_S M)) τ := by
      have := (cc_S_contDiffOn hM).deriv_of_isOpen hI (m := 1) (by norm_num)
      exact this.contDiffAt (hI.mem_nhds hτ)
    exact h1.differentiableAt (by norm_num)
  exact ((hd.hasDerivAt.mul_const _).prodMk (hd.hasDerivAt.mul_const _)).deriv

lemma cc_c_contDiffOn (hM : 0 < M) (t₀ : ℝ) : ContDiffOn ℝ 2 (cc_c M t₀) (Ioo 0 (M * Real.pi)) :=
  ((cc_S_contDiffOn hM).mul contDiffOn_const).prodMk ((cc_S_contDiffOn hM).mul contDiffOn_const)

/-- `∂_U F` and `∂_V F` at `y = (U, V) ∈ {UV < 1}`, from `F = kr_φ ∘ rK` and `kr_r_U`, `kr_r_V`. -/
lemma cc_dF (hM : 0 < M) {U V : ℝ} (hp : (U, V) ∈ sk_kM) (w : P) :
    fderiv ℝ (FS M) (U, V) w =
      KRModel.kr_φ1 M (rK M (U, V)) * (-V / hK' M (rK M (U, V))) * w.1 +
      KRModel.kr_φ1 M (rK M (U, V)) * (-U / hK' M (rK M (U, V))) * w.2 := by
  have hd := (st_FS_diff hM hp).hasFDerivAt
  have hφ := KRModel.kr_hasDerivAt_φ hM (KRModel.kr_r_pos hM hp)
  have hU : HasDerivAt (fun t => FS M (t, V)) (fderiv ℝ (FS M) (U, V) ((1 : ℝ), (0 : ℝ))) U :=
    hd.comp_hasDerivAt_of_eq U ((hasDerivAt_id U).prodMk (hasDerivAt_const U V)) rfl
  have hV : HasDerivAt (fun t => FS M (U, t)) (fderiv ℝ (FS M) (U, V) ((0 : ℝ), (1 : ℝ))) V :=
    hd.comp_hasDerivAt_of_eq V ((hasDerivAt_const V U).prodMk (hasDerivAt_id V)) rfl
  have eU := hU.unique (KRModel.kr_comp_U hM hp hφ)
  have eV := hV.unique (KRModel.kr_comp_V hM hp hφ)
  have hw : w = w.1 • ((1 : ℝ), (0 : ℝ)) + w.2 • ((0 : ℝ), (1 : ℝ)) := by
    ext <;> simp
  rw [hw, map_add, map_smul, map_smul, eU, eV, smul_eq_mul, smul_eq_mul]
  simp only [Prod.smul_mk, smul_eq_mul, Prod.mk_add_mk, mul_one, mul_zero, add_zero, zero_add]
  ring

/-- **2a-②-ii: the cycloid is a geodesic of Schwarzschild.** For every `t₀` and `[a, b] ⊂ (0, Mπ)`,
`γ(τ) = Φ(η(τ), t₀)` is `IsGeodesicOn (se_S hM)`: in `W`'s chart (the inclusion), `c″ = −Γ(c)(c′, c′)` in
Koszul form for `g = F·gM`. -/
theorem cc_isGeodesicOn (hM : 0 < M) (t₀ : ℝ) {a b : ℝ} (ha : 0 < a) (hb : b < M * Real.pi) :
    (se_S hM).IsGeodesicOn (cc_γ hM t₀) a b := by
  have hI : IsOpen (Ioo 0 (M * Real.pi)) := isOpen_Ioo
  intro t ht
  have htI : t ∈ Ioo 0 (M * Real.pi) := ⟨by linarith [ht.1], by linarith [ht.2]⟩
  set ε := min t (M * Real.pi - t) with hε_def
  have hε : 0 < ε := lt_min htI.1 (by linarith [htI.2])
  have hsub : Ioo (t - ε) (t + ε) ⊆ Ioo 0 (M * Real.pi) := fun s hs => by
    have h1 := min_le_left t (M * Real.pi - t); have h2 := min_le_right t (M * Real.pi - t)
    exact ⟨by linarith [hs.1], by linarith [hs.2]⟩
  set p := cc_γ hM t₀ t
  have hcEq : ∀ s ∈ Ioo 0 (M * Real.pi), ng_c P p (cc_γ hM t₀) s = cc_c M t₀ s :=
    fun s hs => cc_γ_val hM t₀ hs
  have hev : ∀ s ∈ Ioo 0 (M * Real.pi), ng_c P p (cc_γ hM t₀) =ᶠ[𝓝 s] cc_c M t₀ := fun s hs => by
    filter_upwards [hI.mem_nhds hs] with s' hs' using hcEq s' hs'
  refine ⟨ε, hε, fun s _ => se_src _ _, ?_, fun s hs w => ?_⟩
  · exact ((cc_c_contDiffOn hM t₀).mono hsub).congr fun s hs => hcEq s (hsub hs)
  · have hsI := hsub hs
    have hd1 : deriv (ng_c P p (cc_γ hM t₀)) s = deriv (cc_c M t₀) s := (hev s hsI).deriv_eq
    have hd2 : deriv (deriv (ng_c P p (cc_γ hM t₀))) s = deriv (deriv (cc_c M t₀)) s := by
      have : deriv (ng_c P p (cc_γ hM t₀)) =ᶠ[𝓝 s] deriv (cc_c M t₀) := (hev s hsI).deriv
      exact this.deriv_eq
    rw [hcEq s hsI, hd1, hd2, cc_deriv_c hM t₀ s hsI, cc_deriv2_c hM t₀ hsI]
    obtain ⟨hW, -, hk, hr⟩ := cc_Φ_mem hM (cy_η_mem_Ioo hM hsI) t₀
    rw [← cc_c_eq] at hW hk hr
    have hf : fderiv ℝ (hRep (se_S hM).g p) (cc_c M t₀ s) =
        fderiv ℝ (fun z => FS M z • gM) (cc_c M t₀ s) := (st_hRep_eventually hM p hW).fderiv_eq
    have hdiff := st_FS_diff hM hk
    rw [se_hRep hM p hW]
    simp only [ng_kos, hf, sq_smul_fderiv_apply gM hdiff, smul_apply, smul_eq_mul, gM_apply]
    unfold cc_c at hk hr ⊢
    simp only [cc_dF hM hk, hr]
    have hsc := cc_scalar hM hsI
    have hpair := cc_exp_pair M t₀
    have hFS : FS M (cc_S M s * Real.exp (-t₀ / (4 * M)), cc_S M s * Real.exp (t₀ / (4 * M))) =
        KRModel.kr_φ M (cy_r M (cy_η M s)) := by
      show 32 * M ^ 3 / rK M _ * Real.exp (-rK M _ / (2 * M)) = _
      rw [hr]; rfl
    rw [hFS]
    linear_combination (-(Real.exp (-t₀ / (4 * M)) * w.2 + Real.exp (t₀ / (4 * M)) * w.1) / 2) * hsc
      + (-(Real.exp (-t₀ / (4 * M)) * w.2 + Real.exp (t₀ / (4 * M)) * w.1) / 2 *
          (-(KRModel.kr_φ1 M (cy_r M (cy_η M s))) * cc_S M s / hK' M (cy_r M (cy_η M s))) *
          deriv (cc_S M) s ^ 2) * hpair

/-- **2a-③: on the manifold, the cycloid is unit timelike with Killing energy zero.** For `0 < τ < Mπ`,
`g(γ′, γ′) = −1`, and `g(γ′, χ) = 0` for the boost Killing field `χ = (−U/4M, V/4M)` (`sq_L`), which is `∂_t`
pushed forward by `Φ`: `E = −g(γ′, χ) = 0`. -/
theorem cc_unit_energy (hM : 0 < M) (t₀ : ℝ) (p : seW) {τ : ℝ} (hτ : τ ∈ Ioo 0 (M * Real.pi)) :
    hRep (se_S hM).g p (cc_c M t₀ τ) (deriv (cc_c M t₀) τ) (deriv (cc_c M t₀) τ) = -1 ∧
    hRep (se_S hM).g p (cc_c M t₀ τ) (deriv (cc_c M t₀) τ) (sq_L M (cc_c M t₀ τ)) = 0 := by
  obtain ⟨hW, -, hk, hr⟩ := cc_Φ_mem hM (cy_η_mem_Ioo hM hτ) t₀
  rw [← cc_c_eq] at hW hk hr
  rw [se_hRep hM p hW, cc_deriv_c hM t₀ τ hτ]
  simp only [smul_apply, smul_eq_mul, gM_apply, sq_L_apply]
  have hpair := cc_exp_pair M t₀
  have hu := cc_unit hM hτ
  have hFS : FS M (cc_c M t₀ τ) = KRModel.kr_φ M (cy_r M (cy_η M τ)) := by
    show 32 * M ^ 3 / rK M _ * Real.exp (-rK M _ / (2 * M)) = _
    rw [hr]; rfl
  rw [hFS]
  unfold cc_c
  constructor
  · linear_combination (-1 : ℝ) * hu + (-(KRModel.kr_φ M (cy_r M (cy_η M τ)) *
      deriv (cc_S M) τ ^ 2)) * hpair
  · ring

end CCModel


namespace CEModel
open Model SEModel Kruskal NModel STModel CCModel ContinuousLinearMap

variable {M : ℝ}

/-- `r(ρ) = M(1 + cosh ρ)` on Region I. -/
noncomputable def ce_r (M ρ : ℝ) : ℝ := M * (1 + Real.cosh ρ)

/-- `σ(ρ) = sinh(ρ/2)·e^{r/4M}`, so `σ² = hK(r) = (r/2M − 1) e^{r/2M}`. -/
noncomputable def ce_σ (M ρ : ℝ) : ℝ := Real.sinh (ρ / 2) * Real.exp (ce_r M ρ / (4 * M))

/-- **The Region I chart** `Ψ(ρ, t) = (−σ e^{−t/4M}, σ e^{t/4M})` into Kruskal's `(U, V)`. -/
noncomputable def ce_Ψ (M ρ t : ℝ) : P :=
  (-(ce_σ M ρ * Real.exp (-t / (4 * M))), ce_σ M ρ * Real.exp (t / (4 * M)))

lemma ce_cosh_half (ρ : ℝ) : 1 + Real.cosh ρ = 2 * Real.cosh (ρ / 2) ^ 2 ∧
    Real.cosh ρ - 1 = 2 * Real.sinh (ρ / 2) ^ 2 := by
  have hc : Real.cosh ρ = Real.cosh (ρ / 2) ^ 2 + Real.sinh (ρ / 2) ^ 2 := by
    rw [← Real.cosh_two_mul]; ring_nf
  have hcs := Real.cosh_sq (ρ / 2)
  constructor <;> linarith

lemma ce_hK (hM : 0 < M) (ρ : ℝ) : hK M (ce_r M ρ) = ce_σ M ρ ^ 2 := by
  obtain ⟨-, h⟩ := ce_cosh_half ρ
  have he : Real.exp (ce_r M ρ / (4 * M)) ^ 2 = Real.exp (ce_r M ρ / (2 * M)) := by
    rw [sq, ← Real.exp_add]; congr 1; field_simp; ring
  unfold hK ce_σ
  rw [mul_pow, he]
  have : ce_r M ρ / (2 * M) - 1 = Real.sinh (ρ / 2) ^ 2 := by
    unfold ce_r; field_simp; linarith
  rw [this]

lemma ce_prod (M ρ t : ℝ) : (ce_Ψ M ρ t).1 * (ce_Ψ M ρ t).2 = -(ce_σ M ρ ^ 2) := by
  show -(ce_σ M ρ * Real.exp (-t / (4 * M))) * (ce_σ M ρ * Real.exp (t / (4 * M))) = _
  have := cc_exp_pair M t
  calc _ = -(ce_σ M ρ ^ 2 * (Real.exp (-t / (4 * M)) * Real.exp (t / (4 * M)))) := by ring
    _ = _ := by rw [this, mul_one]

lemma ce_σ_pos {ρ : ℝ} (hρ : 0 < ρ) : 0 < ce_σ M ρ := by
  unfold ce_σ
  have : 0 < Real.sinh (ρ / 2) := Real.sinh_pos_iff.2 (by linarith)
  positivity

lemma ce_r_pos (hM : 0 < M) (ρ : ℝ) : 0 < ce_r M ρ := by
  unfold ce_r; have := Real.cosh_pos ρ; positivity

/-- **4b-①, the image**: for `ρ > 0`, `Ψ(ρ, t)` lies in `W = {V > 0, UV < 1}` with `U < 0` (Region I, the right
exterior), and `rK(Ψ(ρ, t)) = M(1 + cosh ρ)`. -/
theorem ce_Ψ_mem (hM : 0 < M) {ρ : ℝ} (hρ : 0 < ρ) (t : ℝ) :
    ce_Ψ M ρ t ∈ seWS ∧ (ce_Ψ M ρ t).1 < 0 ∧ ce_Ψ M ρ t ∈ sk_kM ∧
      rK M (ce_Ψ M ρ t) = ce_r M ρ := by
  have hs := ce_σ_pos (M := M) hρ
  have hr := ce_r_pos hM ρ
  have hk := ce_hK hM ρ
  have hp := ce_prod M ρ t
  have h1 : (ce_Ψ M ρ t).1 * (ce_Ψ M ρ t).2 < 1 := by
    rw [hp]; have := sq_nonneg (ce_σ M ρ); linarith
  refine ⟨⟨by show 0 < ce_σ M ρ * Real.exp (t / (4 * M)); positivity, h1⟩,
    by show -(ce_σ M ρ * Real.exp (-t / (4 * M))) < 0
       have : 0 < ce_σ M ρ * Real.exp (-t / (4 * M)) := by positivity
       linarith, h1, ?_⟩
  show rinv M (-((ce_Ψ M ρ t).1 * (ce_Ψ M ρ t).2)) = _
  rw [hp, neg_neg, ← hk, rinv_hK hM hr]

/-- **4b-①, injectivity**: `Ψ` is one-to-one on `(0, ∞) × ℝ`. -/
theorem ce_Ψ_inj (hM : 0 < M) {ρ ρ' t t' : ℝ} (hρ : 0 < ρ) (hρ' : 0 < ρ')
    (h : ce_Ψ M ρ t = ce_Ψ M ρ' t') : ρ = ρ' ∧ t = t' := by
  have hr := (ce_Ψ_mem hM hρ t).2.2.2
  have hr' := (ce_Ψ_mem hM hρ' t').2.2.2
  rw [h] at hr
  have hrr : ce_r M ρ = ce_r M ρ' := hr.symm.trans hr'
  have hc : Real.cosh ρ = Real.cosh ρ' := by
    unfold ce_r at hrr
    have := mul_left_cancel₀ hM.ne' hrr; linarith
  have h1 := Real.cosh_le_cosh.1 hc.le
  have h2 := Real.cosh_le_cosh.1 hc.ge
  rw [abs_of_pos hρ, abs_of_pos hρ'] at h1 h2
  have he : ρ = ρ' := le_antisymm h1 h2
  subst he
  refine ⟨rfl, ?_⟩
  have h2 := congrArg Prod.snd h
  simp only [ce_Ψ] at h2
  have := mul_left_cancel₀ (ce_σ_pos (M := M) hρ).ne' h2
  have := Real.exp_injective this
  have h4 : (0:ℝ) < 4 * M := by positivity
  field_simp at this; linarith

lemma ce_hasDerivAt_σ (hM : 0 < M) (ρ : ℝ) :
    HasDerivAt (ce_σ M) (Real.exp (ce_r M ρ / (4 * M)) * Real.cosh (ρ / 2) ^ 3 / 2) ρ := by
  have h1 : HasDerivAt (fun x => Real.sinh (x / 2)) (Real.cosh (ρ / 2) * (1 / 2)) ρ :=
    (Real.hasDerivAt_sinh _).comp ρ ((hasDerivAt_id ρ).div_const 2)
  have h2 : HasDerivAt (fun x => ce_r M x / (4 * M)) (M * Real.sinh ρ / (4 * M)) ρ := by
    have := ((hasDerivAt_const ρ (1:ℝ)).add (Real.hasDerivAt_cosh ρ)).const_mul M |>.div_const (4 * M)
    convert this using 1
    · funext x; rfl
    · ring
  have h3 := h1.mul ((Real.hasDerivAt_exp _).comp ρ h2)
  convert h3 using 1
  · funext x; rfl
  simp only [Function.comp_apply]
  have hs : Real.sinh ρ = 2 * Real.sinh (ρ / 2) * Real.cosh (ρ / 2) := by
    rw [← Real.sinh_two_mul]; ring_nf
  have hcs := Real.cosh_sq (ρ / 2)
  rw [hs]; field_simp
  linear_combination 4 * hcs

/-- `∂_ρΨ = σ′(ρ)·(−e^{−t/4M}, e^{t/4M})`, `σ′ = e^{r/4M} cosh³(ρ/2)/2`. -/
noncomputable def ce_a (M ρ t : ℝ) : P :=
  (-((Real.exp (ce_r M ρ / (4 * M)) * Real.cosh (ρ / 2) ^ 3 / 2) * Real.exp (-t / (4 * M))),
   (Real.exp (ce_r M ρ / (4 * M)) * Real.cosh (ρ / 2) ^ 3 / 2) * Real.exp (t / (4 * M)))

/-- `∂_tΨ = (σ/4M)·(e^{−t/4M}, e^{t/4M})`. -/
noncomputable def ce_b (M ρ t : ℝ) : P :=
  (-(ce_σ M ρ * (Real.exp (-t / (4 * M)) * (-1 / (4 * M)))),
   ce_σ M ρ * (Real.exp (t / (4 * M)) * (1 / (4 * M))))

lemma ce_dρ (hM : 0 < M) (ρ t : ℝ) : HasDerivAt (fun x => ce_Ψ M x t) (ce_a M ρ t) ρ :=
  ((ce_hasDerivAt_σ hM ρ).mul_const _).neg.prodMk ((ce_hasDerivAt_σ hM ρ).mul_const _)

lemma ce_dt (M ρ t : ℝ) : HasDerivAt (fun x => ce_Ψ M ρ x) (ce_b M ρ t) t := by
  refine HasDerivAt.prodMk ?_ ?_
  · have h := (((Real.hasDerivAt_exp _).comp t (((hasDerivAt_id t).neg).div_const (4 * M))).const_mul
      (ce_σ M ρ)).neg
    convert h using 1
    · funext x; simp [neg_div]
    · simp [neg_div]
  · have h := ((Real.hasDerivAt_exp _).comp t ((hasDerivAt_id t).div_const (4 * M))).const_mul
      (ce_σ M ρ)
    convert h using 1
    · simp
    · simp

/-- **4b-②, the pullback**: through `se_hRep`, `g(∂_ρΨ, ∂_ρΨ) = 4M²cosh⁴(ρ/2)`, `g(∂_tΨ, ∂_tΨ) = −tanh²(ρ/2)`,
`g(∂_ρΨ, ∂_tΨ) = 0`: `Ψ*g` is P2's `eq:Region_I_metric` (radial part), and `−tanh²(ρ/2) = −(1 − 2M/r)`
(`cy_regionI_schw`). -/
theorem ce_pullback (hM : 0 < M) (p : seW) {ρ : ℝ} (hρ : 0 < ρ) (t : ℝ) :
    hRep (se_S hM).g p (ce_Ψ M ρ t) (ce_a M ρ t) (ce_a M ρ t) = 4 * M ^ 2 * Real.cosh (ρ / 2) ^ 4 ∧
    hRep (se_S hM).g p (ce_Ψ M ρ t) (ce_b M ρ t) (ce_b M ρ t) = -(Real.tanh (ρ / 2) ^ 2) ∧
    hRep (se_S hM).g p (ce_Ψ M ρ t) (ce_a M ρ t) (ce_b M ρ t) = 0 := by
  obtain ⟨hW, -, hk, hr⟩ := ce_Ψ_mem hM hρ t
  obtain ⟨hc2, hs2⟩ := ce_cosh_half ρ
  have hcpos := Real.cosh_pos (ρ / 2)
  have hrv : ce_r M ρ = 2 * M * Real.cosh (ρ / 2) ^ 2 := by unfold ce_r; rw [hc2]; ring
  have hG : Real.exp (-ce_r M ρ / (2 * M)) = (Real.exp (ce_r M ρ / (4 * M)) ^ 2)⁻¹ := by
    rw [cc_exp_neg, sq, ← Real.exp_add]; congr 2; field_simp; ring
  rw [se_hRep hM p hW]
  simp only [smul_apply, smul_eq_mul, gM_apply, ce_a, ce_b, ce_σ, FS, hr, hG, cc_exp_neg t,
    Real.tanh_eq_sinh_div_cosh]
  have hE := Real.exp_pos (ce_r M ρ / (4 * M))
  have he := Real.exp_pos (t / (4 * M))
  refine ⟨?_, ?_, ?_⟩
  · rw [hrv]; field_simp; ring
  · rw [hrv]; field_simp; ring
  · ring

/-- **4b-③**: the second branch `z = −iρ` has the same `r` (`cy_patches`); it is the left exterior `{U > 0 > V}`,
outside `W`, reached by the reflection `(U, V) ↦ (−U, −V)`, which preserves `rK` and the metric coefficient-wise:
`F(−y)·gM(−a, −b) = F(y)·gM(a, b)`. -/
theorem ce_reflection (M : ℝ) (y a b : P) :
    rK M (-y) = rK M y ∧ FS M (-y) * gM (-a) (-b) = FS M y * gM a b := by
  have hr : rK M (-y) = rK M y := by
    show rinv M (-((-y).1 * (-y).2)) = rinv M (-(y.1 * y.2))
    simp
  refine ⟨hr, ?_⟩
  simp only [FS, hr, gM_apply, Prod.fst_neg, Prod.snd_neg]
  ring

end CEModel

#print axioms MSpacetime.me_futCauchy_of_cauchy_N
#print axioms MSpacetime.mk_isOpen_D
#print axioms MSpacetime.mk_pushup'
#print axioms MSpacetime.mk_curve_inext_D
#print axioms MSpacetime.ch_isCauchy_VN
#print axioms MSpacetime.mh_temporalD_chr
#print axioms MSpacetime.mh_future_step
#print axioms MSpacetime.mh_past_step
#print axioms MSpacetime.mh_hint
#print axioms MSpacetime.mh_hcl
#print axioms MSpacetime.mh_blowup
#print axioms MSpacetime.mh_sublevelProper
#print axioms MSpacetime.mh_slice_lower_limit
#print axioms MSpacetime.mh_slice_upper_limit
#print axioms MSpacetime.mh_slice_kuratowski
#print axioms MSpacetime.mh_causal_alignment_gh_N
#print axioms Model.hl_cauchy
#print axioms NModel.me_locallyOneChart
#print axioms NModel.me_charts_differ
#print axioms NModel.mh_witness_hypotheses
#print axioms NModel.mh_witness_headline_G
#print axioms NModel.mh_witness_headline

#print axioms TCF.tc_pointwise
#print axioms TCF.tc_tendsto
#print axioms TCF.tc_tendsto_limit
#print axioms mc_preconnected_inter_frontier
#print axioms MSpacetime.mc_lower_limit
#print axioms MSpacetime.mc_upper_limit
#print axioms MSpacetime.mc_cone_kuratowski_N
#print axioms mc_frameHyp_pullback
#print axioms MSpacetime.mc_frameHyp_toChart
#print axioms MSpacetime.mc_frameHyp_ofChart
#print axioms MSpacetime.mc_tangency_N
#print axioms MSpacetime.mc_tangency_limit_N
#print axioms MSpacetime.mc_tangency_at_N
#print axioms mc_covCh_change
#print axioms mc_chart_change
#print axioms mc_covCh_comp_chart
#print axioms Model.mc_frameHyp_gM
#print axioms NModel.mc_witness_frameHyp
#print axioms NModel.mc_witness_tangency_holds
#print axioms NModel.mc_witness_tangency_at
#print axioms NModel.mc_witness_tangency_fails
#print axioms NModel.mc_witness_cones
#print axioms mc_tendsto_limit_aux
#print axioms mc_tCC_eq
#print axioms NModel.tCC_neg_p₀

#print axioms mx_preimage_frontier
#print axioms mx_preimage_closure
#print axioms MSpacetime.mx_frontier_JpastSet
#print axioms MSpacetime.mx_range_subset_M
#print axioms MSpacetime.mx_H_eq_boundary
#print axioms MSpacetime.mx_prop_causal_alignment
#print axioms NModel.mx_ι_isOpenEmbedding
#print axioms NModel.mx_ι_contMDiff
#print axioms NModel.mx_dι_eq
#print axioms NModel.mx_witnessExt
#print axioms NModel.mx_mem_mink_D_JA
#print axioms NModel.mx_preimage_Ipast_scri
#print axioms NModel.mx_scri_subset_frontier
#print axioms NModel.mx_witness_boundary
#print axioms NModel.mx_witness_headline

#print axioms NModel.cz_locallyOneChart
#print axioms NModel.cz_oneChart
#print axioms NModel.cz_chartSp_eq
#print axioms NModel.cz_ι_isOpenEmbedding
#print axioms NModel.cz_ι_contMDiff
#print axioms NModel.cz_dι_eq
#print axioms NModel.cz_witnessExt
#print axioms NModel.cz_Ω_nonconst
#print axioms NModel.cz_closure_range
#print axioms NModel.cz_isCompact_closure
#print axioms NModel.cz_range_ne_univ
#print axioms NModel.cz_scri_subset_frontier
#print axioms NModel.cz_scri_nonempty
#print axioms NModel.cz_mem_Ipast_scri
#print axioms NModel.cz_preimage_Ipast_scri
#print axioms NModel.cz_witness_boundary
#print axioms NModel.cz_witness_headline
#print axioms MSpacetime.cz_scale_chr
#print axioms MSpacetime.cz_scale_isCauchyTemporalOn
#print axioms MSpacetime.cz_scale_locallyOneChart
#print axioms NModel.cz_minkF_locallyOneChart
#print axioms NModel.cz_witnessExtF
#print axioms NModel.cz_witness_headline_F
#print axioms NModel.cz_exp_nonvacuous

#print axioms NModel.ct_frameHyp_scaled
#print axioms NModel.ct_frameHyp
#print axioms NModel.ct_ratio
#print axioms NModel.ct_bound
#print axioms NModel.ct_dchartL_q
#print axioms NModel.ct_witness_tangency_F
#print axioms NModel.ct_witness_headline_F
#print axioms NModel.ct_exp
#print axioms NModel.ct_expV_differs


#print axioms Kruskal.sk_rinv_contDiffOn
#print axioms Kruskal.sk_rK_contDiffOn
#print axioms Kruskal.sk_rK_eq_two_iff
#print axioms Kruskal.sk_FS_contDiffOn
#print axioms Kruskal.sk_FS_nonconst
#print axioms MSpacetime.sk_scale_locallyOneChart
#print axioms Model.sk_K_D
#print axioms Model.sk_K_JpastSet
#print axioms Model.sk_K_H
#print axioms NModel.sk_hRep
#print axioms NModel.sk_hRep_apply
#print axioms NModel.sk_chartSp_eq
#print axioms NModel.sk_locallyOneChart
#print axioms NModel.sk_observer
#print axioms NModel.sk_static_observer
#print axioms NModel.sk_cor_EF_events
#print axioms NModel.sk_nonvacuous

#print axioms Spacetime.SeAgree.chr_iff
#print axioms Spacetime.SeAgree.D_eq
#print axioms Spacetime.SeAgree.H_eq
#print axioms Spacetime.SeAgree.isCauchyTemporal
#print axioms Model.se_temporal_RI
#print axioms Model.se_cauchy_RI
#print axioms Model.se_seg_mem
#print axioms Model.se_K_chr_iff
#print axioms Model.se_K_D
#print axioms Model.se_K_JpastSet
#print axioms Model.se_K_H
#print axioms SEModel.se_dchart
#print axioms SEModel.se_dchartInv
#print axioms SEModel.se_oneChart
#print axioms SEModel.se_flat_locallyOneChart
#print axioms SEModel.se_chartSp_agree
#print axioms SEModel.se_hRep
#print axioms SEModel.se_locallyOneChart
#print axioms SEModel.se_chr_iff_lt
#print axioms SEModel.se_foundation
#print axioms SEModel.se_cauchy
#print axioms SEModel.se_proper_time
#print axioms MSpacetime.cd_chr_of_mem_closure_Jpast
#print axioms MSpacetime.cd_mem_closure_sublevel
#print axioms MSpacetime.cd_closure_Jpast_subset_D
#print axioms MSpacetime.cd_closure_Jpast_inter_H
#print axioms MSpacetime.cd_cone_disjoint
#print axioms hs_pointwise
#print axioms hs_uniform_on_compact_pts
#print axioms hs_uniform_on_compact
#print axioms hs_unbounded
#print axioms MSpacetime.hs_stretch_N
#print axioms SEModel.se_O_mem_cone
#print axioms SEModel.se_headline
#print axioms SEModel.se_H_not_compact
#print axioms SEModel.se_stretch
#print axioms SEModel.se_nonvacuous

-- campaign 99 (new)
#print axioms SRModel.sr_seR_kM
#print axioms SRModel.sa_rK_hasFDerivAt
#print axioms SRModel.sa_uP_hasFDerivAt
#print axioms SRModel.sa_uP_contDiffOn
#print axioms SRModel.sa_hK'_pos
#print axioms SRModel.sa_uD_U
#print axioms SRModel.sa_uD_V
#print axioms SRModel.sr_futCausal_iff
#print axioms SRModel.sr_hasDerivAt
#print axioms SRModel.sr_dfun
#print axioms SRModel.sr_contMDiffOn
#print axioms SRModel.sr_split
#print axioms SRModel.sr_pos_of_causal
#print axioms SRModel.sr_Θ_eq
#print axioms SRModel.sr_D_eq
#print axioms SRModel.sr_k_eq
#print axioms SRModel.sr_q_pos
#print axioms SRModel.sr_dU_pos_iff
#print axioms SRModel.sr_temporal
#print axioms SRModel.sr_pt_mem
#print axioms SRModel.sr_pt_r
#print axioms SRModel.sr_not_temporal
#print axioms SRModel.sr_γ_memW
#print axioms SRModel.sr_γ_eq
#print axioms SRModel.sr_γ_vel
#print axioms SRModel.sr_curve_γ
#print axioms SRModel.sr_Θ_curve_gt
#print axioms SRModel.sr_not_cauchy
#print axioms SRModel.sr_not_isCauchy
#print axioms SRModel.sr_coord_mono
#print axioms SRModel.sr_future_diverges
#print axioms SRModel.sr_nonvacuous


-- campaign 100 (new)
#print axioms MSpacetime.cd_prop_causal_alignment
#print axioms SXModel.sx_ι_apply
#print axioms SXModel.sx_ι_isOpenEmbedding
#print axioms SXModel.sx_ι_contMDiff
#print axioms SXModel.sx_dι_eq
#print axioms SXModel.sx_F_pos
#print axioms SXModel.sx_Ω_pos
#print axioms SXModel.sx_Ω_sq
#print axioms SXModel.sx_ext_ι
#print axioms SXModel.sx_ext_Ω_sq
#print axioms SXModel.sx_dι_T
#print axioms SXModel.sx_hI
#print axioms SXModel.sx_prop_causal_alignment
#print axioms SXModel.sx_nonvacuous

-- campaign 96 (`KillingWhole.lean` kit, copied)
#print axioms ld_remainder_unif
#print axioms ld_local_flow
#print axioms ld_flow_bounded
#print axioms ld_linear_exists
#print axioms ld_gronwall_fwd
#print axioms ld_gronwall_symm
#print axioms ld_gronwallBound_le
#print axioms ld_flowData_exists
#print axioms FlowData.ld_Icc_mem
#print axioms FlowData.ld_alpha_continuousOn
#print axioms FlowData.ld_var_exists
#print axioms FlowData.ld_J_spec
#print axioms FlowData.ld_C_nonneg
#print axioms FlowData.ld_gb_le
#print axioms FlowData.ld_J_norm_le
#print axioms FlowData.ld_remainder_uniform
#print axioms FlowData.ld_J_uniform
#print axioms FlowData.ld_flow_hasFDerivAt
#print axioms FlowData.ld_J_continuousOn
#print axioms FlowData.ld_flow_contDiffOn
#print axioms FlowData.ld_U_open
#print axioms FlowData.ld_Dflow_apply
#print axioms FlowData.ld_J_continuousAt_joint
#print axioms FlowData.ld_flow_hasFDerivAt_joint
#print axioms FlowData.ld_flow_continuousOn_joint
#print axioms FlowData.ld_Dflow_continuousOn
#print axioms FlowData.ld_flow_contDiffOn_joint
#print axioms ld_flow_C1
#print axioms ld_complement_equiv
#print axioms FlowData.ld_flowBox
#print axioms ld_flowBox_exists
#print axioms ld_cutoff
#print axioms ld_flowData_small
#print axioms ld_agree
#print axioms FlowData.ld_x₀_mem
#print axioms FlowData.ld_transfer_J
#print axioms FlowData.ld_isFlowBox_mem
#print axioms FlowData.ld_transfer_isFlowBox
#print axioms ld_flowData_exists_of_contDiffOn
#print axioms ld_flowBox_exists_of_contDiffOn
#print axioms ld_flowBox_chart_of_contDiffOn
#print axioms ld_chartRep_inv
#print axioms ld_mdifferentiableAt_symm
#print axioms ld_manifold_flowBox
#print axioms FlowData.ld_flow_pushes_field_loc
#print axioms FlowData.ld_flow_pushes_field
#print axioms FlowData.ld_flow_isometry_loc
#print axioms FlowData.ld_flow_isometry
#print axioms FlowData.ld_flowBox_pullback_loc
#print axioms FlowData.ld_flowBox_pullback
#print axioms FlowData.ld_flowBox_killing
#print axioms FlowData.ld_transfer_isVar
#print axioms ld_flowBox_exists_of_contDiffOn_var
#print axioms ld_flowBox_killing_of_contDiffOn
#print axioms ld_isKilling_lie
#print axioms ld_flowBox_killing_of_isKilling
#print axioms ld_chartRep_eq_triv
#print axioms ld_chartRep_contDiffAt_of_triv
#print axioms ld_chartRep_contDiffAt_of_section
#print axioms ld_chartRep_ball_of_contDiffAt
#print axioms ld_chartRep_ball_of_section
#print axioms ld_chartRep_ne_zero
#print axioms ld_mfderiv_straightens
#print axioms ld_manifold_flowBox_of_contDiffAt
#print axioms ld_manifold_flowBox_section
#print axioms ld_chartRep_contDiffOn_of_section
#print axioms ld_manifold_flowBox_sectionOn
#print axioms LocalKillingChart.ld_lambda_indep
#print axioms ld_manifold_killingChart
#print axioms ld_manifold_killingChart_section
#print axioms ld_chartLie_core
#print axioms ld_hRep_apply
#print axioms ld_mfderiv_symm_chart
#print axioms ld_mfderiv_chart_symm
#print axioms ld_chartRep_apply_chart
#print axioms ld_h_eq_hRep
#print axioms ld_lieDerivForm_chart_of_bracket
#print axioms ld_mlieBracket_chart_self
#print axioms ld_constExt_self
#print axioms ld_chartRep_constExt
#print axioms ld_chartRep_constExt_contDiffAt
#print axioms ld_lieDerivForm_chart_self
#print axioms ld_lieDeriv_chart_self
#print axioms ld_lieDerivForm_eq_lieDeriv
#print axioms ld_mlieBracket_model
#print axioms ld_lieDerivForm_model
#print axioms ld_isKilling_of_chartLie
#print axioms ld_mlieBracket_chart
#print axioms ld_chartRep_contDiffAt_of_section_chart
#print axioms ld_constExt_section
#print axioms ld_lieDerivForm_chart
#print axioms ld_lieDeriv_chart
#print axioms ld_chartLie_zero_of_lieDeriv
#print axioms ld_isKilling_of_lieDeriv
#print axioms ld_manifold_killingChart_lieDeriv
#print axioms LocalKillingChart.ld_metric_N
#print axioms kl_psi_zero
#print axioms kl_velocity
#print axioms kl_psi_injOn
#print axioms kl_orbit_ne
#print axioms kl_exists_eps
#print axioms kl_uIcc_abs_lt
#print axioms kl_comps_eq_gH
#print axioms kl_lambda_indep_N
#print axioms kl_normSq_eq_comps
#print axioms kl_interval_orbit
#print axioms kl_forcing
#print axioms kl_normSq_orbit_const
#print axioms kl_null_along_orbit
#print axioms kl_lemma_killing_chart
#print axioms kl_lemma_killing_local
#print axioms kl_chartLie_const
#print axioms kl_psi_model
#print axioms kl_model_orbit
#print axioms kl_w_B_apply
#print axioms kl_w_lorentzian
#print axioms kl_w_mfderiv_chart
#print axioms kl_w_mfderiv_chart_symm
#print axioms kl_w_hRep
#print axioms kl_w_chartRep
#print axioms kl_w_lieDeriv
#print axioms kl_w_hX
#print axioms kl_w_hXp
#print axioms kl_w_null
#print axioms kl_witness
#print axioms kg_flowBox_killing_symm
#print axioms kg_restrict_source
#print axioms kg_restrict_symmC1
#print axioms kg_killingChart_symm
#print axioms kg_chi_psi
#print axioms kg_psi_mem_dom
#print axioms kg_psi_chi
#print axioms kg_chi_mem
#print axioms kg_dom_open
#print axioms kg_chi_mdiff
#print axioms kg_U_open
#print axioms kg_psi_mdiff
#print axioms kg_dpsi_dchi
#print axioms kg_add_mdiff
#print axioms kg_shift_hasMFDerivAt
#print axioms kg_shift_mdiff
#print axioms kg_mfderiv_shift
#print axioms kg_g_congr
#print axioms kg_shift_isometry
#print axioms kg_psi_mem_U
#print axioms kg_shift_psi
#print axioms kg_orbit_hasMFDerivAt
#print axioms kg_curve_eq_orbit
#print axioms kg_related_trans
#print axioms kg_box_along
#print axioms kg_related_box
#print axioms kg_normSq_box
#print axioms kg_lapse_null
#print axioms kg_deltaTau_zero
#print axioms kg_lemma_killing_generator
#print axioms kg_w_B_apply
#print axioms kg_w_lorentzian
#print axioms kg_w_L_apply
#print axioms kg_w_normSq
#print axioms kg_w_boost_generator
#print axioms kg_w_boost_isometry
#print axioms kg_w_hRep
#print axioms kg_w_chartRep
#print axioms kg_w_chartLie
#print axioms kg_w_lieDeriv
#print axioms kg_w_hX
#print axioms kg_w_X_γ
#print axioms kg_w_hXne
#print axioms kg_w_integral
#print axioms kg_w_null
#print axioms kg_w_injOn
#print axioms kg_witness
#print axioms «kw_dλ_exists»
#print axioms kw_AdaptedSplitting.kw_g_vel
#print axioms kw_eq_zero_of_integral_eq_zero
#print axioms kw_metric_singularity_along
#print axioms kw_dt_X
#print axioms kw_split
#print axioms kw_h_X
#print axioms kw_vel_eq
#print axioms kw_lemma_killing_whole
#print axioms kw_witness

-- campaign 106 (new, and the copied `sq_` lemmas)
#print axioms sq_smul_hasFDerivAt
#print axioms sq_smul_fderiv_apply
#print axioms sq_L_apply
#print axioms MSpacetime.st_null_of_isKillingHorizon
#print axioms st_cor_stationary
#print axioms STModel.st_g_apply
#print axioms STModel.st_chartRep
#print axioms STModel.st_chartRep_eventually
#print axioms STModel.st_hRep_eventually
#print axioms STModel.st_FS_diff
#print axioms STModel.st_gF_diff
#print axioms STModel.st_FS_boost
#print axioms STModel.st_chi_F
#print axioms STModel.st_chartLie
#print axioms STModel.st_chartLie_congr
#print axioms STModel.st_lieDeriv
#print axioms STModel.st_hX
#print axioms STModel.st_normSq
#print axioms STModel.st_γ_zero
#print axioms STModel.st_χ_γ
#print axioms STModel.st_integral
#print axioms STModel.st_mem_H
#print axioms STModel.st_isKillingHorizon
#print axioms STModel.st_witness


-- campaign 107 (new)
#print axioms ng_Γ_spec
#print axioms ng_Γ_unique
#print axioms ng_Γ_exists
#print axioms ng_geod_iff
#print axioms MSpacetime.ng_hRep_symm
#print axioms MSpacetime.ng_vel_chart
#print axioms MSpacetime.ng_chart_energy_deriv
#print axioms MSpacetime.ng_energy_hasDerivAt
#print axioms MSpacetime.ng_energy_const
#print axioms MSpacetime.ng_cor_threefold_iii
#print axioms NGModel.ng_γ_val
#print axioms NGModel.ng_γ_fst
#print axioms NGModel.ng_FS_dV
#print axioms NGModel.ng_kos_zero
#print axioms NGModel.ng_nondeg
#print axioms NGModel.ng_c_eq
#print axioms NGModel.ng_isGeodesicOn
#print axioms NGModel.ng_vel
#print axioms NGModel.ng_witness


-- campaign 110 (new)
#print axioms KRModel.kr_JpastSet
#print axioms KRModel.kr_BH_eq
#print axioms KRModel.kr_BH_val
#print axioms KRModel.kr_locus_BH
#print axioms KRModel.kr_Sig_closure_W
#print axioms KRModel.kr_slice_far
#print axioms KRModel.kr_toSig_neBot
#print axioms KRModel.kr_rinv_to_zero
#print axioms KRModel.kr_r_to_zero
#print axioms kr_pd_const
#print axioms kr_pd_congr
#print axioms kr_K_const
#print axioms kr_hasDerivAt_s2
#print axioms kr_deriv_s2
#print axioms kr_deriv_nsc
#print axioms kr_deriv_cot
#print axioms kr_sph_inv
#print axioms kr_sph_Γ
#print axioms kr_sph_D_open
#print axioms kr_sph_pdΓ
#print axioms kr_K_sphere
#print axioms kr_WD.dom_open
#print axioms kr_WD.d_mh_U
#print axioms kr_WD.d_mh_V
#print axioms kr_WD.d_sq_U
#print axioms kr_WD.d_sq_V
#print axioms kr_WD.d_q1_U
#print axioms kr_WD.d_q1_V
#print axioms kr_WD.d_q2_U
#print axioms kr_WD.d_q2_V
#print axioms kr_WD.d_q3_U
#print axioms kr_WD.d_q3_V
#print axioms kr_WD.d_q4_U
#print axioms kr_WD.d_q4_V
#print axioms kr_WD.d_q5_U
#print axioms kr_WD.d_q5_V
#print axioms kr_WD.d_q6_U
#print axioms kr_WD.d_q6_V
#print axioms kr_WD.gW_inv
#print axioms kr_WD.gW_pd
#print axioms kr_WD.Γ_eq
#print axioms kr_WD.pdΓ_eq
#print axioms kr_WD.Riem_eq
#print axioms kr_WD.gW_row
#print axioms kr_WD.giW_row
#print axioms kr_WD.kr_warped
#print axioms KRModel.kr_hasDerivAt_hK'
#print axioms KRModel.kr_hasDerivAt_φ
#print axioms KRModel.kr_hasDerivAt_φ1
#print axioms KRModel.kr_r_U
#print axioms KRModel.kr_r_V
#print axioms KRModel.kr_r_pos
#print axioms KRModel.kr_hp_ne
#print axioms KRModel.kr_comp_U
#print axioms KRModel.kr_comp_V
#print axioms KRModel.kr_SD_good
#print axioms KRModel.kr_schwarzschild
#print axioms KRModel.kr_KS_eq
#print axioms KRModel.kr_pow_blowup
#print axioms KRModel.kr_blowup
#print axioms KRModel.kr_nhds_le_toSig
#print axioms KRModel.kr_cor_densities_c

#print axioms ck_order_two
#print axioms ck_chain_rule
#print axioms ck_rC_deriv
#print axioms ck_rC_deriv2
#print axioms ck_rC_analytic
#print axioms ck_pole_pi
#print axioms ck_K_form
#print axioms ck_pole_pi'
#print axioms ck_order_zero
#print axioms ck_mislabel
#print axioms ck_r_deriv
#print axioms ck_r_deriv2
#print axioms ck_critical
#print axioms ck_critical_even
#print axioms ck_critical_odd
#print axioms ck_max_min
#print axioms ck_bounded_zero
#print axioms ck_value_zero
#print axioms ck_prop_critical
#print axioms KRModel.ck_horizon
#print axioms KRModel.ck_bifurcation
#print axioms KRModel.ck_interior
#print axioms KRModel.ck_interior_witness
#print axioms KRModel.ck_prop_Kretschmann
#print axioms KRModel.ck_cor_Kretschmann_at_z0

#print axioms cy_cos_half_sq
#print axioms cy_hasDerivAt_τ
#print axioms cy_continuous_τ
#print axioms cy_proper_time
#print axioms cy_Mpi
#print axioms cy_cos_gt
#print axioms cy_τ_strictMonoOn
#print axioms cy_τ_zero
#print axioms cy_τ_pi
#print axioms cy_τ_surj
#print axioms cy_η_spec
#print axioms cy_η_τ
#print axioms cy_η_strictMonoOn
#print axioms cy_η_image
#print axioms cy_η_zero
#print axioms cy_η_end
#print axioms cy_η_mem_Ioo
#print axioms cy_η_continuousAt
#print axioms cy_hasDerivAt_η
#print axioms cy_radial
#print axioms cy_η_tendsto_zero
#print axioms cy_η_tendsto_end
#print axioms cy_ends
#print axioms cy_pd0
#print axioms cy_pd1
#print axioms cy_pdz
#print axioms cy_diag_Γ
#print axioms cy_cos_lt
#print axioms cy_hasDerivAt_A
#print axioms cy_geodesic
#print axioms cy_interior_forms
#print axioms cy_regionI_coeffs
#print axioms cy_regionI_schw
#print axioms cy_backseam_coeffs
#print axioms cy_backseam_schw
#print axioms cy_patches
#print axioms KRModel.cy_backseam_not_kruskal

#print axioms CCModel.cc_exp_pair
#print axioms CCModel.cc_exp_sq
#print axioms CCModel.cc_sin_half_sq
#print axioms CCModel.cc_hK
#print axioms CCModel.cc_prod
#print axioms CCModel.cc_s_pos
#print axioms CCModel.cc_r_pos
#print axioms CCModel.cc_Φ_mem
#print axioms CCModel.cc_Φ_inj
#print axioms CCModel.cc_hasDerivAt_s
#print axioms CCModel.cc_dη
#print axioms CCModel.cc_dt
#print axioms CCModel.cc_exp_neg
#print axioms CCModel.cc_pullback
#print axioms CCModel.cc_g_contDiffOn
#print axioms CCModel.cc_η_contDiffOn
#print axioms CCModel.cc_s_contDiff
#print axioms CCModel.cc_S_contDiffOn
#print axioms CCModel.cc_hasDerivAt_S
#print axioms CCModel.cc_unit
#print axioms CCModel.cc_scalar
#print axioms CCModel.cc_c_eq
#print axioms CCModel.cc_γ_val
#print axioms CCModel.cc_hasDerivAt_c
#print axioms CCModel.cc_deriv_c
#print axioms CCModel.cc_deriv2_c
#print axioms CCModel.cc_c_contDiffOn
#print axioms CCModel.cc_dF
#print axioms CCModel.cc_isGeodesicOn
#print axioms CCModel.cc_unit_energy

#print axioms CEModel.ce_cosh_half
#print axioms CEModel.ce_hK
#print axioms CEModel.ce_prod
#print axioms CEModel.ce_σ_pos
#print axioms CEModel.ce_r_pos
#print axioms CEModel.ce_Ψ_mem
#print axioms CEModel.ce_Ψ_inj
#print axioms CEModel.ce_hasDerivAt_σ
#print axioms CEModel.ce_dρ
#print axioms CEModel.ce_dt
#print axioms CEModel.ce_pullback
#print axioms CEModel.ce_reflection

end ShadowProbe.CircleExteriorProbe

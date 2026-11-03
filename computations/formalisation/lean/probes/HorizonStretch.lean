import Mathlib

/-!
# Probe `r7665+71` (campaign 92), piece ①: the unbounded-stretch clause

Registration: `computations/formalisation/r7665_71_campaign92/PREDICTION.md`, piece ①. Nothing
imports this file, and it imports no other probe. It starts as a copy of campaign 91 ②'s
`probes/FourDWitness.lean` (namespace renamed `ShadowProbe.HorizonStretchProbe`, all old names and
all `#print axioms` lines kept); everything new has the prefix `hs_`. (Base: `FourDWitness` rather
than the registration's `ConeDisjoint`, because it carries the `ℝ⁴` witness, a metric space
natively; `ConeDisjoint`'s eighth conjunct is not used by ①.)

## NEW (campaign 92 ①)

**The stretch — BUILT.** On any metric space `X`, for `A : ℝ → Set X`, `H : Set X`:
`hs_stretch A H τ ε = {q ∈ H | infDist q (A τ) < ε}`.

**(S1) Uniform approach on compacts — BUILT; the registered expected stop (the uniformity step) was
not hit.** `hs_uniform_on_compact`: `H ⊆ KLi A → 0 < ε → K ⊆ H → IsCompact K →
∀ᶠ τ in atTop, K ⊆ hs_stretch A H τ ε`. Route: `hs_pointwise` (a ball is a neighbourhood, so
`KLi` gives a point of `A τ` within `ε/2`, eventually), a finite `ε/2`-ball cover of `K`
(`finite_cover_balls_of_compact`), `Set.Finite.eventually_all`, the triangle inequality.
`hs_uniform_on_compact_pts` is the stronger form with an actual point `a ∈ A τ`, `dist q a < ε`
(so an empty `A τ`, where `infDist = 0`, never carries the conclusion).

**(S2) Unboundedness — BUILT.** `hs_unbounded`: if also `H` lies in no compact set, then for every
compact `K`, eventually `¬ hs_stretch A H τ ε ⊆ K` (from (S1) on a singleton `{q}`, `q ∈ H \ K`).

**On `N` — BUILT.** `MSpacetime.hs_stretch_N`: under `mc_cone_kuratowski_N`'s hypotheses (`hL`,
`hOD`, `hmono`, `hJM`), for **any** `m : MetricSpace N` with
`hm : m.toUniformSpace.toTopologicalSpace = tN` (`tN` the manifold's topology), (S1) and (S2) for
`A = S.cone O`, `H = S.H J`. *The instance question:* the `MSpacetime` layer fixes
`[TopologicalSpace N]` as its own instance, so `[MetricSpace N]` on top would be a second, unrelated
topology (a diamond). The metric is therefore an explicit argument, the stretch is written
`@hs_stretch N m …`, and the proof `subst`s `hm` and applies the metric-space lemmas.

**The witness on `ℝ⁴` — BUILT.** `FourD.hs_topology_native` (`rfl`: on `N = E` the charted topology
is the norm topology). `FourD.hs_witness`: `𝓗⁺ = {U = 0}`; it lies in no compact set
(`hs_H_not_compact`, via the bounded `V`-coordinate `hs_V_bdd`); (S1) and (S2) via `hs_stretch_N`
with `m = inferInstance`, `hm = hs_topology_native`; **futureward**, `∀ ε > 0, ∀ T, ∀ᶠ τ,
∃ q ∈ stretch τ ε, q.V > T`; and for every `q ∈ 𝓗⁺`, `J⁺(q) ∩ 𝓗⁺ = {p | Cau q p} ∩ 𝓗⁺` lies in no
compact set, via the generator `hs_generator_subset : (U, V + s, y, z) ∈ J⁺(q) ∩ 𝓗⁺` for `s ≥ 0`
(`hs_cstep_V`: the straight null step along `∂_V`). `FourD.hs_origin` (non-vacuity): eventually a
point of `∂J⁻(O τ)` lies within `1` of the origin, which lies in the `1`-stretch.

**Not formalised (as registered):** the general theorem says the stretch is unbounded, not that it
runs futureward along generators (future inextendibility of generators is not formalised); the
"monotonically from outside" approach of P1's proof.

`#print axioms` at the end: every line reads `[propext, Classical.choice, Quot.sound]`.
-/

/-!
# (kept) Probe `r7663+71` (campaign 91), piece ②: a four-dimensional witness `N = ℝ⁴`,
`g = −dU dV + dy² + dz²`

Registration: `computations/formalisation/r7663_71_campaign91/PREDICTION.md`, piece ②. Nothing
imports this file, and it imports no other probe. It starts as a copy of campaign 90 (b)'s
`probes/CylinderWitness.lean` (namespace renamed `ShadowProbe.FourDWitnessProbe`, all old names
kept); everything new has the prefix `fd_` and lives in `namespace FourD`.

**Dropped from the copy** (compile time; nothing in ② uses it): campaign 90 (b)'s
`namespace Cylinder` (`cy_*`, the `ℝ² × S¹` witness) and its `#print axioms` lines. Its pattern is
adapted below; it stands in its own file. **Kept:** all the general theory (as listed in the kept
campaign 90 (b) header below, including `ConformalExtension`, `mx_prop_causal_alignment` and the
generic `cz_scale` section) and its `44` `#print axioms` lines.

## NEW (campaign 91 ②)

**`N` and its chart — BUILT.** `E = P × Q = (ℝ × ℝ) × (ℝ × ℝ)`, a point `((U, V), (y, z))`, and
`N = E`, the model space with its self chart (`fd_chart_univ`: the chart covers `N`; this witness
is about dimension, campaign 90 (b) is the multi-chart one). `fd_dim : finrank ℝ E = 4`.

**The spacetime — BUILT.** `fd_g x = fd_G = gM ∘ (fst, fst) + (dy² + dz²) ∘ (snd, snd)`, i.e.
`g = −dU dV + dy² + dz²`; `T = ∂_U + ∂_V`; `M = N`. `fd_locallyOneChart`: in the self chart
`hRep g p ≡ fd_G` (`fd_hRep`) and `chartRep T p ≡ ((1,1),0)`.

**Causal vectors and steps — BUILT.** `fd_futCausal_iff`: `v` future causal iff
`v_y² + v_z² ≤ v_U v_V` and `v_U + v_V > 0`; `fd_futCausal_proj`, `fd_futTimelike_proj` (to campaign
81's `mink`); `fd_futCausal_speed : a v_y + b v_z ≤ (v_U + v_V)/2` for `a² + b² ≤ 1`. Steps, `≪`,
`≤` project to the plane (`fd_tstep_proj`, `fd_cstep_proj`, `fd_chr_proj`, `fd_cau_proj`);
`fd_tstep_of`: the straight segment `a → b` is a timelike step when `ΔU, ΔV > 0` and
`Δy² + Δz² < ΔU ΔV`.

**The observer, `D`, `𝓗⁺` — BUILT.** `fd_O τ = (O' τ, 0)`, `O'` campaign 79's adapted
reparametrisation (`hl_adapted` for `−log`), `J = range fd_O`. `hOD` is `rfl`; `fd_hmono`; `fd_JM`;
`fd_D_eq : D = {U < 0}` (every `(y, z)`: a straight step to the observer); `fd_JpastSet_eq`;
`fd_H_eq : 𝓗⁺ = {U = 0}`, a null hyperplane; `fd_H_nonempty`; `fd_HM`.

**The Cauchy property on `N` — BUILT; the registered expected stop (non-compact fibre) was not
hit.** `fd_Θ x = Θ₀ x_{UV} = −log(−U) + V`; `fd_isTemporalOn` (`fd_dcov : dΘ(v) = dΘ₀(v_{UV})`).
`fd_mono`: a linear functional non-negative on the causal cone does not decrease along a causal
curve (campaign 79's `mono_brk`); applied to `W/2 ∓ y`, `W/2 ∓ z` (`W = U + V`) it gives `fd_lip :
|Δy|, |Δz| ≤ ΔW/2`. `fd_converge`: if the `(U, V)`-projection converges then `y`, `z` are Cauchy,
so converge (`ℝ` complete — simpler than the circle), and the curve converges in `N`. So
`fd_projCurve c` is an inextendible causal curve of `mink.Dsp (range O)`, and
`fd_isCauchyTemporalOn` is campaign 81's `hl_cauchy_Θ₀` read through it. `fd_adapt`.

**The witness headline — BUILT.** `fd_witness_headline`: `finrank = 4`, `LocallyOneChart`, `hOD`,
`hmono`, `J ⊆ M`, `D = {U < 0}`, `𝓗⁺ = {U = 0}` non-empty and `⊆ M`, the Cauchy property,
adaptation, and the conclusions of `mh_causal_alignment_gh_N` (properness, `KLi = KLs = 𝓗⁺` for the
slices) and `mc_cone_kuratowski_N` (`KLi = KLs = 𝓗⁺` for the past cones); every slice non-empty.
No hypothesis beyond the registration.

**Tangency — BUILT.** `fd_witness_tangency`: at every `q ∈ 𝓗⁺`, along `𝓝[D] q` (non-trivial), with
`ℓ = ∂_V`, `n = 2∂_U` (`fd_frameHyp`), `W = {ℓ, n}^⊥` the transverse plane `{v_U = v_V = 0}`
(`fd_W_transverse`, with `g|_W = dy² + dz²`, `fd_W_metric`), the rate `dΘ(ℓ)/dΘ(n) = −U/2 → 0`
(`fd_ratio`), and `mc_tangency_at_N` gives `(dΘ(n))⁻¹ dΘ → −g_q(ℓ, ·) = ½ dU`.
`fd_tangency_origin`: the same at the concrete point `((0,0),(0,0))` (non-vacuity).

**`∂J⁻(𝒥⁺)` / `ConformalExtension` — REPORTED, not exercised in four dimensions** (as registered:
`(arctan U, arctan V, y, z)` is not conformal for the product metric; the honest compactification
is Penrose's into the Einstein static universe, not attempted).

`#print axioms` at the end: every line reads `[propext, Classical.choice, Quot.sound]`.
-/

/-!
# (kept) Probe `r7661+71` (campaign 90), part (b): the cylinder witness `N = ℝ² × S¹`, no chart of whose
atlas covers it

Registration: `computations/formalisation/r7661_71_campaign90/PREDICTION.md`, part (b). Nothing
imports this file, and it imports no other probe. It starts as a copy of campaign 90 (a)'s
`probes/Compactification.lean` (namespace renamed `ShadowProbe.CylinderWitnessProbe`, all old names
kept); everything new has the prefix `cy_` and lives in `namespace Cylinder`.

**Dropped from the copy** (to keep compile time down; nothing in (b) uses them): every `NModel`
section of campaign 87 (the two-chart `Pt`, `minkN`, `me_locallyOneChart`, `mh_witness_*`),
campaign 88's witness sections (`Model.ellV`, `Model.nvec`, `Model.mc_frameHyp_gM`, `sm`, `xm`,
`NModel.mc_witness_*`), campaign 89's `NModel.mx_*` witness, campaign 90 (a)'s `NModel.cz_*`
witnesses (`cz_St`, `cz_ι`, `cz_witnessExt`, `cz_witness_headline`, `cz_minkF`,
`cz_witness_headline_F`), and the `#print axioms` lines for those. **Kept:** all the general theory
(`Spacetime`, the flat 2D `Model` through `hl_cauchy_Θ₀`, `TCF`, `MSpacetime` on any Mathlib
manifold `N` with model `E` and `IsManifold 𝓘(ℝ,E) 1 N`, `OneChart`, `LocallyOneChart`, the local
kit, `mh_causal_alignment_gh_N`, `mc_cone_kuratowski_N`, `mc_tangency_at_N`, `ConformalExtension`,
`mx_H_eq_boundary`, `mx_prop_causal_alignment`, the generic `cz_scale` section).

## NEW (campaign 90 (b))

**`N` and its atlas — BUILT.** `N = (ℝ × ℝ) × Circle` (Mathlib's `Circle ⊆ ℂ` with its stereographic
`ChartedSpace (EuclideanSpace ℝ (Fin 1))`), model `E = (ℝ × ℝ) × EuclideanSpace ℝ (Fin 1)`, the
product charted space (`cy_chartAt : chartAt E x = (chartAt P x.1).prod (chartAt E1 x.2)`), and
`IsManifold 𝓘(ℝ, E) ω N` from `IsManifold.prod` through `modelWithCornersSelf_prod`.
`cy_chart_ne_univ : ∀ x : N, (chartAt E x).source ≠ univ` (the stereographic chart at `y` misses
`−y`), so `cy_not_oneChart : ∀ p, ¬ cy_S.OneChart p`; `cy_dim : finrank ℝ E = 3`.

**The spacetime — BUILT.** Coordinates `(U, V)` null on the plane factor, `y` the circle angle.
`cy_g x v w = gM v_{UV} w_{UV} + ⟪dY_x v, dY_x w⟫` with `Y : N → ℂ` the circle coordinate
(`dY = mfderiv Y`), i.e. `g = −dU dV + dy²`, defined intrinsically (no chart formula);
`T = ∂_U + ∂_V`; `M = N`. `pos_on_perp` uses Mathlib's injectivity of `D(Circle ↪ ℂ)`.
`cy_locallyOneChart : cy_S.LocallyOneChart`: on each chart target, `hRep g p` is
`gM ∘ (D(fst ∘ φ⁻¹))² + ⟪D(Y ∘ φ⁻¹) ·, D(Y ∘ φ⁻¹) ·⟫` (`cy_hRep_eq`, chain rule), `C¹` because
`fst ∘ φ⁻¹`, `Y ∘ φ⁻¹` are analytic on the target; `chartRep T p = ((1,1), 0)` (`cy_chartRep_T`).
The registered stereographic formula `4 ds²/(1+s²)²` is never written: the intrinsic `g` makes it
unnecessary.

**Causal vectors and steps — BUILT.** `cy_futCausal_iff`: `v` future causal iff
`|v_y|² ≤ v_U v_V` and `v_U + v_V > 0` (`cy_futTimelike_iff` with `<`); `cy_futCausal_proj`,
`cy_futTimelike_proj` (to campaign 81's `mink`); `cy_futCausal_speed : |v_y| ≤ (v_U + v_V)/2`.
`cy_tstep_proj`, `cy_cstep_proj`, `cy_chr_proj`, `cy_cau_proj`: steps of `N` project to steps of the
plane. `cy_tstep_of`: the curve `r ↦ (a + r(b − a), z·e^{irθ})` is a timelike step when
`a < b` componentwise and `θ² < (b_U − a_U)(b_V − a_V)`.

**The observer, `D`, `𝓗⁺` — BUILT.** `cy_O τ = (O' τ, 1)`, `O'` campaign 79's adapted
reparametrisation of `(−e^{−σ}, e^{σ})` (`hl_adapted` for `−log`), `J = range cy_O`.
`hOD` is `rfl`; `cy_hmono`; `cy_JM`; `cy_D_eq : cy_S.D cy_J = {x | x.1.1 < 0}` (every angle: the
step winds round the circle); `cy_JpastSet_eq` (same set); `cy_H_eq : cy_S.H cy_J = {x | x.1.1 = 0}`,
the null cylinder `{U = 0} × S¹`; `cy_H_nonempty`; `cy_HM`.

**The Cauchy property on `N` — BUILT; the registered expected stop was not hit.**
`cy_Θ x = Θ₀ x_{UV} = −log(−U) + V`. `cy_isTemporalOn` (`dΘ(v) = dΘ₀(v_{UV})`, `cy_dcov`).
`cy_lip : ‖Y(γ t) − Y(γ s)‖ ≤ (W(γ t) − W(γ s))/2` for `s ≤ t` along any inextendible causal curve
(`W = U + V`; `W/2 − ⟪Y, e⟫` is monotone by campaign 79's `mono_brk`, `‖e‖ ≤ 1`).
`cy_converge`: if the `(U,V)`-projection converges then `Y` is Cauchy, so the curve converges in `N`
(`Circle` closed in `ℂ`). So the projection `cy_projCurve c` is an inextendible causal curve of
`mink.Dsp (range O)`, and `cy_isCauchyTemporalOn : cy_S.IsCauchyTemporalOn (cy_S.D cy_J) cy_Θ`
is campaign 81's `hl_cauchy_Θ₀` read through it. `cy_adapt : ∀ τ, cy_Θ (cy_O τ) = τ + 0`.

**The witness headline — BUILT.** `cy_witness_headline`: no chart covers `N`, `LocallyOneChart`,
`D = {U < 0}`, `𝓗⁺ = {U = 0}` non-empty, the Cauchy property, adaptation, and the conclusions of
`mh_causal_alignment_gh_N` (properness, `KLi = KLs = 𝓗⁺` for the slices) and
`mc_cone_kuratowski_N` (`KLi = KLs = 𝓗⁺` for the past cones). `cy_slice_nonempty`: every slice
is non-empty. No hypothesis beyond the registration.

**Tangency — BUILT (optional piece).** `cy_witness_tangency`: at every `q ∈ 𝓗⁺`, along
`𝓝[D] q` (non-trivial), with `ℓ = ∂_V`, `n = 2∂_U` (`cy_frameHyp`, the intrinsic frame hypotheses on
`D`), the rate `dΘ(ℓ)/dΘ(n) = −U/2 → 0` (`cy_ratio`), and `mc_tangency_at_N` gives
`(dΘ(n))⁻¹ dΘ^{e_q} → −g_q(ℓ, ·) = ½ dU` in the stereographic product chart at `q`.

**`ConformalExtension` / `mx_prop_causal_alignment` — REPORTED, not built.** The product map
`ι = (arctan U, arctan V, y)` is not conformal for `g = −dU dV + dy²` into a flat target: a
conformal `g̃ = h(u,v)(−du dv) + k(u,v) dy²` needs `k = Ω²` and `h = Ω² (1+U²)(1+V²)`, so either `k`
(the circle's size) vanishes at `𝒥⁺` (`h = 1`, `k = cos²u cos²v`) or `h` blows up there. Neither puts
`𝒥⁺` inside a Lorentzian `M̃`, so this was not cheap and is not instantiated.

`#print axioms` at the end: every line reads `[propext, Classical.choice, Quot.sound]`.
-/

/-!
# (kept) Probe `r7661+71` (campaign 90), part (a): a genuine compactification, `Ñ = P ≠ N = Pt`

*(Header kept from `probes/Compactification.lean`. In this file the `NModel` witnesses it describes
are dropped (see the campaign 90 (b) header above); the generic `cz_scale` section is kept.)*

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

namespace ShadowProbe.HorizonStretchProbe

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

/-! ## NEW (campaign 91 ②): the four-dimensional witness `N = ℝ⁴`, `g = −dU dV + dy² + dz²` -/

namespace FourD
open Manifold Model
open scoped ContDiff

/-- The transverse plane, coordinates `(y, z)`. -/
abbrev Q := ℝ × ℝ
/-- The model space `E = P × Q = ℝ⁴`, a point `((U, V), (y, z))`. -/
abbrev E := P × Q
/-- `N = E`, the model space with its self chart. -/
abbrev N := E

example : IsManifold 𝓘(ℝ, E) 1 N := inferInstance
example : IsManifold 𝓘(ℝ, E) ω N := inferInstance
example : T2Space N := inferInstance

/-- `N` is four-dimensional. -/
theorem fd_dim : Module.finrank ℝ E = 4 := by
  simp [Module.finrank_prod]

/-- One chart (the identity) covers `N`. -/
theorem fd_chart_univ (x : N) : (chartAt E x).source = univ := by
  rw [chartAt_self_eq]; rfl

theorem fd_extChart (p : N) : extChartAt 𝓘(ℝ, E) p = PartialEquiv.refl E :=
  extChartAt_model_space_eq_id ℝ p

/-- The flat transverse metric `dy² + dz²`. -/
noncomputable def fd_q : Q →L[ℝ] Q →L[ℝ] ℝ :=
  (ContinuousLinearMap.fst ℝ ℝ ℝ).smulRight (ContinuousLinearMap.fst ℝ ℝ ℝ) +
    (ContinuousLinearMap.snd ℝ ℝ ℝ).smulRight (ContinuousLinearMap.snd ℝ ℝ ℝ)

theorem fd_q_apply (a b : Q) : fd_q a b = a.1 * b.1 + a.2 * b.2 := by
  simp [fd_q]

/-- `g = −dU dV + dy² + dz²` as a constant bilinear form on `E`. -/
noncomputable def fd_G : E →L[ℝ] E →L[ℝ] ℝ :=
  gM.bilinearComp (ContinuousLinearMap.fst ℝ P Q) (ContinuousLinearMap.fst ℝ P Q) +
    fd_q.bilinearComp (ContinuousLinearMap.snd ℝ P Q) (ContinuousLinearMap.snd ℝ P Q)

theorem fd_G_apply (v w : E) : fd_G v w = gM v.1 w.1 + fd_q v.2 w.2 := by
  simp [fd_G]

theorem fd_G_self (v : E) : fd_G v v = -(v.1.1 * v.1.2) + (v.2.1 ^ 2 + v.2.2 ^ 2) := by
  rw [fd_G_apply, gM_apply, fd_q_apply]; ring

/-- The metric field `x ↦ g`. -/
noncomputable def fd_g (_ : N) : E →L[ℝ] E →L[ℝ] ℝ := fd_G

/-- `T = ∂_t = ∂_U + ∂_V`. -/
def fd_T (_ : N) : E := ((1, 1), 0)

theorem fd_G_T (v : E) : fd_G v ((1, 1), 0) = -(v.1.1 + v.1.2) / 2 := by
  rw [fd_G_apply, gM_apply, fd_q_apply]; simp

theorem fd_g_symm (x : N) (v w : E) : fd_g x v w = fd_g x w v := by
  show fd_G v w = fd_G w v
  rw [fd_G_apply, fd_G_apply, fd_q_apply, fd_q_apply, gM_apply, gM_apply]; ring

theorem fd_T_timelike (x : N) : fd_g x (fd_T x) (fd_T x) < 0 := by
  show fd_G ((1, 1), 0) ((1, 1), 0) < 0
  rw [fd_G_T]; norm_num

theorem fd_pos_on_perp (x : N) (v : E) (h : fd_g x v (fd_T x) = 0) (hv : v ≠ 0) :
    0 < fd_g x v v := by
  change fd_G v ((1, 1), 0) = 0 at h
  show 0 < fd_G v v
  rw [fd_G_T] at h
  rw [fd_G_self]
  have h2 : v.1.2 = -v.1.1 := by linarith
  rw [h2]
  by_contra hc; push Not at hc
  have a1 : v.1.1 = 0 := by nlinarith [sq_nonneg v.1.1, sq_nonneg v.2.1, sq_nonneg v.2.2]
  have a3 : v.2.1 = 0 := by nlinarith [sq_nonneg v.1.1, sq_nonneg v.2.1, sq_nonneg v.2.2]
  have a4 : v.2.2 = 0 := by nlinarith [sq_nonneg v.1.1, sq_nonneg v.2.1, sq_nonneg v.2.2]
  apply hv
  ext
  · exact a1
  · rw [h2, a1]; simp
  · exact a3
  · exact a4

/-- **The spacetime `ℝ^{3,1}`**, `M = N`, `g = −dU dV + dy² + dz²`, `T = ∂_U + ∂_V`. -/
noncomputable def fd_S : MSpacetime E N where
  M := univ
  isOpen_M := isOpen_univ
  g := fd_g
  symm := fd_g_symm
  T := fd_T
  T_timelike := fun x _ => fd_T_timelike x
  pos_on_perp := fun x _ v h hv => fd_pos_on_perp x v h hv

theorem fd_gE (x : N) (v w : E) : fd_S.gE x v w = gM v.1 w.1 + fd_q v.2 w.2 := fd_G_apply v w

theorem fd_gE_self (x : N) (v : E) :
    fd_S.gE x v v = -(v.1.1 * v.1.2) + (v.2.1 ^ 2 + v.2.2 ^ 2) := fd_G_self v

theorem fd_gE_T' (x : N) (v : E) : fd_S.gE x v (fd_S.T x) = -(v.1.1 + v.1.2) / 2 := fd_G_T v

/-! ### Causal vectors on `N` -/

theorem fd_futCausal_iff (x : N) (v : E) :
    fd_S.FutCausal x v ↔ v.2.1 ^ 2 + v.2.2 ^ 2 ≤ v.1.1 * v.1.2 ∧ 0 < v.1.1 + v.1.2 := by
  unfold MSpacetime.FutCausal
  rw [fd_gE_self, fd_gE_T']
  constructor
  · rintro ⟨h1, h2⟩; exact ⟨by linarith, by linarith⟩
  · rintro ⟨h1, h2⟩; exact ⟨by linarith, by linarith⟩

theorem fd_futTimelike_iff (x : N) (v : E) :
    fd_S.FutTimelike x v ↔ v.2.1 ^ 2 + v.2.2 ^ 2 < v.1.1 * v.1.2 ∧ 0 < v.1.1 + v.1.2 := by
  unfold MSpacetime.FutTimelike
  rw [fd_gE_self, fd_gE_T']
  constructor
  · rintro ⟨h1, h2⟩; exact ⟨by linarith, by linarith⟩
  · rintro ⟨h1, h2⟩; exact ⟨by linarith, by linarith⟩

/-- Causal vectors project to causal vectors of the `(U, V)` plane. -/
theorem fd_futCausal_proj {x : N} {v : E} (h : fd_S.FutCausal x v) : mink.FutCausal x.1 v.1 := by
  obtain ⟨h1, h2⟩ := (fd_futCausal_iff x v).1 h
  have h0 : 0 ≤ v.1.1 * v.1.2 := le_trans (by positivity) h1
  rw [futCausal_iff]
  refine ⟨?_, ?_, h2⟩ <;> by_contra hc <;> push Not at hc <;> nlinarith

theorem fd_futTimelike_proj {x : N} {v : E} (h : fd_S.FutTimelike x v) :
    mink.FutTimelike x.1 v.1 := by
  obtain ⟨h1, h2⟩ := (fd_futTimelike_iff x v).1 h
  have h0 : 0 < v.1.1 * v.1.2 := lt_of_le_of_lt (by positivity) h1
  rw [futTimelike_iff]
  refine ⟨?_, ?_⟩ <;> by_contra hc <;> push Not at hc <;> nlinarith

/-- The transverse speed of a causal vector in any unit direction `(a, b)` is at most
`(v_U + v_V)/2`. -/
theorem fd_futCausal_speed {x : N} {v : E} (h : fd_S.FutCausal x v) {a b : ℝ}
    (hab : a ^ 2 + b ^ 2 ≤ 1) : a * v.2.1 + b * v.2.2 ≤ (v.1.1 + v.1.2) / 2 := by
  obtain ⟨h1, h2⟩ := (fd_futCausal_iff x v).1 h
  have hS : 0 < (v.1.1 + v.1.2) / 2 := by linarith
  have hCS : (a * v.2.1 + b * v.2.2) ^ 2 ≤ (a ^ 2 + b ^ 2) * (v.2.1 ^ 2 + v.2.2 ^ 2) := by
    nlinarith [sq_nonneg (a * v.2.2 - b * v.2.1)]
  have hq : 0 ≤ v.2.1 ^ 2 + v.2.2 ^ 2 := by positivity
  have hX : (a * v.2.1 + b * v.2.2) ^ 2 ≤ ((v.1.1 + v.1.2) / 2) ^ 2 := by
    have : (a ^ 2 + b ^ 2) * (v.2.1 ^ 2 + v.2.2 ^ 2) ≤ v.2.1 ^ 2 + v.2.2 ^ 2 := by
      nlinarith
    nlinarith [sq_nonneg (v.1.1 - v.1.2)]
  by_contra hc; push Not at hc
  nlinarith

/-! ### Curves on `N` (the self chart: velocities are derivatives) -/

theorem fd_vel (γ : ℝ → N) (t : ℝ) : MSpacetime.vel (E := E) γ t = deriv γ t := by
  unfold MSpacetime.vel; rw [mfderiv_eq_fderiv]; rfl

theorem fd_hasDerivAt {γ : ℝ → N} {t : ℝ} (hγ : MDifferentiableAt 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ t) :
    HasDerivAt γ (MSpacetime.vel (E := E) γ t) t := by
  rw [fd_vel]; exact (mdifferentiableAt_iff_differentiableAt.1 hγ).hasDerivAt

theorem fd_hasDerivAt_fst {γ : ℝ → N} {t : ℝ} (hγ : MDifferentiableAt 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ t) :
    HasDerivAt (fun s => (γ s).1) (MSpacetime.vel (E := E) γ t).1 t :=
  (ContinuousLinearMap.fst ℝ P Q).hasFDerivAt.comp_hasDerivAt t (fd_hasDerivAt hγ)

theorem fd_proj_curve {γ : ℝ → N} (hγ : ContMDiff 𝓘(ℝ, ℝ) 𝓘(ℝ, E) 1 γ) :
    ContDiff ℝ 1 (fun s => (γ s).1) ∧
      ∀ t, deriv (fun s => (γ s).1) t = (MSpacetime.vel (E := E) γ t).1 := by
  refine ⟨contDiff_fst.comp (contMDiff_iff_contDiff.1 hγ),
    fun t => (fd_hasDerivAt_fst ((hγ t).mdifferentiableAt one_ne_zero)).deriv⟩

theorem fd_tstep_proj {x y : N} (h : fd_S.TStep x y) : mink.TStep x.1 y.1 := by
  obtain ⟨γ, hγ, h0, h1, ht⟩ := h
  obtain ⟨hc, hd⟩ := fd_proj_curve hγ
  refine ⟨fun s => (γ s).1, hc, congrArg Prod.fst h0, congrArg Prod.fst h1,
    fun t htI => ⟨mem_univ _, ?_⟩⟩
  rw [hd]; exact fd_futTimelike_proj (ht t htI).2

theorem fd_cstep_proj {x y : N} (h : fd_S.CStep x y) : mink.CStep x.1 y.1 := by
  obtain ⟨γ, hγ, h0, h1, ht⟩ := h
  obtain ⟨hc, hd⟩ := fd_proj_curve hγ
  refine ⟨fun s => (γ s).1, hc, congrArg Prod.fst h0, congrArg Prod.fst h1,
    fun t htI => ⟨mem_univ _, ?_⟩⟩
  rw [hd]; exact fd_futCausal_proj (ht t htI).2

theorem fd_chr_proj {x y : N} (h : fd_S.Chr x y) : mink.Chr x.1 y.1 := by
  induction h with
  | single h => exact Relation.TransGen.single (fd_tstep_proj h)
  | tail _ h ih => exact ih.tail (fd_tstep_proj h)

theorem fd_cau_proj {x y : N} (h : fd_S.Cau x y) : mink.Cau x.1 y.1 := by
  induction h with
  | refl => exact Relation.ReflTransGen.refl
  | tail _ h ih => exact ih.tail (fd_cstep_proj h)

/-- A straight timelike step: `a → b` with `ΔU, ΔV > 0` and `|Δ(y,z)|² < ΔU ΔV`. -/
theorem fd_tstep_of {a b : E} (h1 : a.1.1 < b.1.1) (h2 : a.1.2 < b.1.2)
    (h : (b.2.1 - a.2.1) ^ 2 + (b.2.2 - a.2.2) ^ 2 < (b.1.1 - a.1.1) * (b.1.2 - a.1.2)) :
    fd_S.TStep a b := by
  set γ : ℝ → N := fun r => a + r • (b - a) with hγdef
  have hα : ContDiff ℝ 1 γ := contDiff_const.add (contDiff_id.smul contDiff_const)
  refine ⟨γ, hα.contMDiff, by simp [γ], by simp [γ], fun t _ => ⟨mem_univ _, ?_⟩⟩
  have d1 : HasDerivAt γ (b - a) t := by
    have h := ((hasDerivAt_id' t).smul_const (b - a)).const_add a
    rw [one_smul] at h
    exact h
  rw [fd_vel, d1.deriv, fd_futTimelike_iff]
  simp only [Prod.fst_sub, Prod.snd_sub]
  exact ⟨h, by linarith⟩

/-! ### The observer, `D = {U < 0}` and `𝓗⁺ = {U = 0}` -/

/-- Campaign 79's adapted reparametrisation `O'` of the Rindler worldline (`Θ₀(O' τ) = τ`). -/
noncomputable def fd_O' : ℝ → P := Classical.choose goodG_log.hl_adapted

theorem fd_O'_spec : range fd_O' = range O ∧
    mink.IpastSet (range fd_O') = mink.D (range O) ∧
    (∀ s t : ℝ, s < t → mink.Chr (fd_O' s) (fd_O' t)) ∧
    ∀ τ, ThetaG (fun s => -Real.log s) (fd_O' τ) = τ + 0 :=
  Classical.choose_spec goodG_log.hl_adapted

/-- **The observer** `O(τ) = (O'(τ), 0)`: the Rindler worldline `UV = −1` at `y = z = 0`. -/
noncomputable def fd_O (τ : ℝ) : N := (fd_O' τ, 0)

/-- `J = range O`. -/
noncomputable def fd_J : Set N := range fd_O

theorem fd_O'_U (τ : ℝ) : (fd_O' τ).1 < 0 := by
  obtain ⟨σ, hσ⟩ : fd_O' τ ∈ range O := fd_O'_spec.1 ▸ mem_range_self τ
  rw [← hσ]; simp only [O]; exact neg_lt_zero.2 (Real.exp_pos _)

/-- **`hmono`**: the observer is future-directed. -/
theorem fd_hmono (s t : ℝ) (h : s < t) : fd_S.Chr (fd_O s) (fd_O t) := by
  obtain ⟨h1, h2⟩ := chr_lt (fd_O'_spec.2.2.1 s t h)
  refine Relation.TransGen.single (fd_tstep_of h1 h2 ?_)
  have := mul_pos (sub_pos.2 h1) (sub_pos.2 h2)
  simpa [fd_O] using this

theorem fd_JM : fd_J ⊆ fd_S.M := subset_univ _

/-- **`D = I⁻(J) = {U < 0}`** (every `(y, z)`). -/
theorem fd_D_eq : fd_S.D fd_J = {x : N | x.1.1 < 0} := by
  ext x
  simp only [MSpacetime.D, MSpacetime.IpastSet, mem_iUnion, MSpacetime.Ipast, mem_ofPred_eq,
    exists_prop, fd_J]
  constructor
  · rintro ⟨_, ⟨τ, rfl⟩, h⟩
    have h1 := (chr_lt (fd_chr_proj h)).1
    have h2 := fd_O'_U τ
    exact lt_trans h1 h2
  · intro hx
    set K := x.2.1 ^ 2 + x.2.2 ^ 2 with hK
    have hK0 : 0 ≤ K := by positivity
    set c := -x.1.1 / 2 with hc
    have hc0 : 0 < c := by rw [hc]; linarith
    have e1 : ∀ᶠ σ in atTop, Real.exp (-σ) < c :=
      (tendsto_order.1 Real.tendsto_exp_neg_atTop_nhds_zero).2 _ hc0
    have e2 : ∀ᶠ σ in atTop, x.1.2 + K / c + 1 < Real.exp σ :=
      Real.tendsto_exp_atTop.eventually_gt_atTop _
    obtain ⟨σ, h1, h2⟩ := (e1.and e2).exists
    obtain ⟨t, ht⟩ : O σ ∈ range fd_O' := fd_O'_spec.1.symm ▸ mem_range_self σ
    refine ⟨fd_O t, mem_range_self t, Relation.TransGen.single ?_⟩
    have hd1 : c < (O σ).1 - x.1.1 := by simp only [O]; rw [hc] at h1 ⊢; linarith
    have hd2 : K / c + 1 < (O σ).2 - x.1.2 := by simp only [O]; linarith
    have hq : K / c ≥ 0 := by positivity
    have k := fd_tstep_of (a := x) (b := fd_O t) (by simp only [fd_O]; rw [ht]; linarith)
      (by simp only [fd_O]; rw [ht]; linarith) (by
      have h3 : c * (K / c + 1) ≤ ((O σ).1 - x.1.1) * ((O σ).2 - x.1.2) := by
        apply mul_le_mul hd1.le hd2.le (by positivity) (by linarith)
      have h4 : c * (K / c + 1) = K + c := by field_simp
      simp only [fd_O, ht, Prod.fst_zero, Prod.snd_zero, zero_sub, neg_sq]
      linarith)
    exact k

theorem fd_D_iff (x : N) : x ∈ fd_S.D fd_J ↔ x.1.1 < 0 := by rw [fd_D_eq]; rfl

theorem fd_JpastSet_eq : fd_S.JpastSet fd_J = {x : N | x.1.1 < 0} := by
  apply Subset.antisymm
  · intro x hx
    simp only [MSpacetime.JpastSet, mem_iUnion, MSpacetime.Jpast, mem_ofPred_eq, exists_prop,
      fd_J] at hx
    obtain ⟨_, ⟨τ, rfl⟩, h⟩ := hx
    exact lt_of_le_of_lt (cau_le (fd_cau_proj h)).1 (fd_O'_U τ)
  · rw [← fd_D_eq]; exact fd_S.D_subset_JpastSet fd_J

/-- **`𝓗⁺ = {U = 0}`**, the null hyperplane. -/
theorem fd_H_eq : fd_S.H fd_J = {x : N | x.1.1 = 0} := by
  have ho : IsOpenMap (fun x : N => x.1.1) := isOpenMap_fst.comp isOpenMap_fst
  have hc : Continuous (fun x : N => x.1.1) := continuous_fst.comp continuous_fst
  have h := (ho.preimage_frontier_eq_frontier_preimage hc (Iio (0:ℝ))).symm
  rw [MSpacetime.H, fd_JpastSet_eq]
  have e : {x : N | x.1.1 < 0} = (fun x : N => x.1.1) ⁻¹' Iio 0 := rfl
  rw [e, h, frontier_Iio]
  rfl

theorem fd_H_nonempty : (fd_S.H fd_J).Nonempty := ⟨((0, 0), 0), by rw [fd_H_eq]; rfl⟩

theorem fd_HM : fd_S.H fd_J ⊆ fd_S.M := subset_univ _

/-! ### `LocallyOneChart` (the self chart: `g` and `T` are constant) -/

theorem fd_hRep (p : N) (y : E) : hRep fd_S.g p y = fd_G := by
  refine ContinuousLinearMap.ext fun v => ContinuousLinearMap.ext fun w => ?_
  rw [ld_hRep_apply, fd_extChart, PartialEquiv.refl_symm, PartialEquiv.refl_coe, mfderiv_id]
  rfl

theorem fd_chartRep_T (p : N) (y : E) : chartRep fd_S.T p y = ((1, 1), 0) := by
  unfold chartRep
  rw [fd_extChart, PartialEquiv.refl_coe, mfderiv_id]
  rfl

/-- **`LocallyOneChart`** on `ℝ⁴`. -/
theorem fd_locallyOneChart : fd_S.LocallyOneChart := by
  intro p _
  refine ⟨univ, isOpen_univ, mem_univ _, fun y _ => ⟨y, ⟨mem_univ _, ?_⟩, ?_⟩, ?_, ?_⟩
  · rw [fd_chart_univ]; exact mem_univ _
  · rw [fd_extChart]; rfl
  · exact contDiffOn_const.congr fun y _ => fd_hRep p y
  · exact continuousOn_const.congr fun y _ => fd_chartRep_T p y

/-! ### The Cauchy property on `N`, by projection to `(U, V)` with fibre `ℝ²` -/

/-- `Θ = −log(−U) + V`, read on `N`. -/
noncomputable def fd_Θ (x : N) : ℝ := Θ₀ x.1

/-- `W = U + V = 2t`. -/
def fd_W (x : N) : ℝ := x.1.1 + x.1.2

/-- `W/2 − (a y + b z)`, a linear functional on `E`. -/
noncomputable def fd_L (a b : ℝ) : E →L[ℝ] ℝ :=
  (1/2 : ℝ) • ((ContinuousLinearMap.fst ℝ ℝ ℝ).comp (ContinuousLinearMap.fst ℝ P Q) +
      (ContinuousLinearMap.snd ℝ ℝ ℝ).comp (ContinuousLinearMap.fst ℝ P Q)) -
    (a • (ContinuousLinearMap.fst ℝ ℝ ℝ).comp (ContinuousLinearMap.snd ℝ P Q) +
      b • (ContinuousLinearMap.snd ℝ ℝ ℝ).comp (ContinuousLinearMap.snd ℝ P Q))

theorem fd_L_apply (a b : ℝ) (x : E) :
    fd_L a b x = fd_W x / 2 - (a * x.2.1 + b * x.2.2) := by
  simp [fd_L, fd_W]; ring

theorem fd_L_nonneg {a b : ℝ} (hab : a ^ 2 + b ^ 2 ≤ 1) (x : N) (v : E)
    (h : fd_S.FutCausal x v) : 0 ≤ fd_L a b v := by
  rw [fd_L_apply, fd_W]
  have := fd_futCausal_speed h hab
  linarith

/-- A linear functional non-negative on the future causal cone does not decrease along a causal
curve. -/
theorem fd_mono {U : Set N} (c : fd_S.InextCausalCurveIn U) (L : E →L[ℝ] ℝ)
    (hL : ∀ x v, fd_S.FutCausal x v → 0 ≤ L v) {s t : ℝ} (hst : s ≤ t) :
    L (c.γ s) ≤ L (c.γ t) := by
  set F : ℝ → ℝ := fun r => L (c.γ r) with hF
  have hFc : Continuous F := L.continuous.comp c.cont
  have hFd : ∀ r ∉ c.brk, HasDerivAt F (L (MSpacetime.vel (E := E) c.γ r)) r := fun r hr =>
    L.hasFDerivAt.comp_hasDerivAt r (fd_hasDerivAt (c.causal r hr).1)
  have hFpos : ∀ r ∉ c.brk, 0 ≤ deriv F r := fun r hr => by
    rw [(hFd r hr).deriv]; exact hL _ _ (c.causal r hr).2
  set f : ℝ → ℝ := fun r => F (s + r) with hf
  set B : Set ℝ := {r | s + r ∈ c.brk} with hB
  have hBf : ∀ a b, (B ∩ Icc a b).Finite := fun a b => by
    have hfin := c.brk_fin (s + a) (s + b)
    refine (hfin.preimage (f := fun r => s + r) (add_right_injective s).injOn).subset ?_
    rintro r ⟨hr1, hr2, hr3⟩
    exact ⟨hr1, by linarith, by linarith⟩
  have hmono := mono_brk hBf (f := f) (hFc.comp (continuous_const.add continuous_id)).continuousOn
    (fun r _ hr => by
      have hd := (hFd (s + r) hr).comp r ((hasDerivAt_id r).const_add s)
      rw [mul_one] at hd
      refine ⟨hd.differentiableAt, ?_⟩
      have hd' : HasDerivAt f _ r := hd
      rw [hd'.deriv, ← (hFd (s + r) hr).deriv]
      exact hFpos _ hr)
  have := hmono (show (0:ℝ) ∈ Ici 0 from mem_Ici.2 le_rfl) (show t - s ∈ Ici 0 from sub_nonneg.2 hst)
    (sub_nonneg.2 hst)
  simp only [hf, add_zero, add_sub_cancel] at this
  exact this

/-- **The transverse length of a causal curve is at most `Δ(U + V)/2`**, in each of `y`, `z`. -/
theorem fd_lip {U : Set N} (c : fd_S.InextCausalCurveIn U) {s t : ℝ} (hst : s ≤ t) :
    |(c.γ t).2.1 - (c.γ s).2.1| ≤ (fd_W (c.γ t) - fd_W (c.γ s)) / 2 ∧
      |(c.γ t).2.2 - (c.γ s).2.2| ≤ (fd_W (c.γ t) - fd_W (c.γ s)) / 2 := by
  have m1 := fd_mono c (fd_L 1 0) (fd_L_nonneg (by norm_num)) hst
  have m2 := fd_mono c (fd_L (-1) 0) (fd_L_nonneg (by norm_num)) hst
  have m3 := fd_mono c (fd_L 0 1) (fd_L_nonneg (by norm_num)) hst
  have m4 := fd_mono c (fd_L 0 (-1)) (fd_L_nonneg (by norm_num)) hst
  simp only [fd_L_apply] at m1 m2 m3 m4
  exact ⟨abs_le.2 ⟨by linarith, by linarith⟩, abs_le.2 ⟨by linarith, by linarith⟩⟩

theorem fd_lip_abs {U : Set N} (c : fd_S.InextCausalCurveIn U) (s t : ℝ) :
    |(c.γ t).2.1 - (c.γ s).2.1| ≤ |fd_W (c.γ t) - fd_W (c.γ s)| / 2 ∧
      |(c.γ t).2.2 - (c.γ s).2.2| ≤ |fd_W (c.γ t) - fd_W (c.γ s)| / 2 := by
  rcases le_total s t with h | h
  · obtain ⟨h1, h2⟩ := fd_lip c h
    have k : fd_W (c.γ t) - fd_W (c.γ s) ≤ |fd_W (c.γ t) - fd_W (c.γ s)| := le_abs_self _
    exact ⟨h1.trans (by linarith), h2.trans (by linarith)⟩
  · obtain ⟨h1, h2⟩ := fd_lip c h
    rw [abs_sub_comm ((c.γ t).2.1), abs_sub_comm ((c.γ t).2.2), abs_sub_comm (fd_W (c.γ t))]
    have k : fd_W (c.γ s) - fd_W (c.γ t) ≤ |fd_W (c.γ s) - fd_W (c.γ t)| := le_abs_self _
    exact ⟨h1.trans (by linarith), h2.trans (by linarith)⟩

/-- A real function `1/2`-Lipschitz in a convergent one converges (`ℝ` is complete). -/
theorem fd_coord_conv {f w : ℝ → ℝ} {a : ℝ} (hlip : ∀ s t, |f t - f s| ≤ |w t - w s| / 2)
    (hw : Tendsto w atTop (𝓝 a)) : ∃ b, Tendsto f atTop (𝓝 b) := by
  have hWc := hw.cauchySeq
  have hYc : CauchySeq f := by
    rw [Metric.cauchySeq_iff'] at hWc ⊢
    intro ε hε
    obtain ⟨N0, hN⟩ := hWc (2 * ε) (by linarith)
    refine ⟨N0, fun n hn => ?_⟩
    have h1 := hN n hn
    rw [Real.dist_eq] at h1 ⊢
    have := hlip N0 n
    linarith
  exact cauchySeq_tendsto_of_complete hYc

/-- **Inextendibility descends**: if the `(U, V)`-projection of a curve with the transverse
Lipschitz bound converges, the curve converges in `N` (the fibre `ℝ²` is complete). -/
theorem fd_converge {γ : ℝ → N}
    (hlip : ∀ s t, |(γ t).2.1 - (γ s).2.1| ≤ |fd_W (γ t) - fd_W (γ s)| / 2 ∧
      |(γ t).2.2 - (γ s).2.2| ≤ |fd_W (γ t) - fd_W (γ s)| / 2) {p : P}
    (hp : Tendsto (fun t => (γ t).1) atTop (𝓝 p)) : ∃ q : Q, Tendsto γ atTop (𝓝 (p, q)) := by
  have hW : Tendsto (fun t => fd_W (γ t)) atTop (𝓝 (p.1 + p.2)) :=
    ((continuous_fst.add continuous_snd).tendsto p).comp hp
  obtain ⟨y, hy⟩ := fd_coord_conv (f := fun t => (γ t).2.1) (fun s t => (hlip s t).1) hW
  obtain ⟨z, hz⟩ := fd_coord_conv (f := fun t => (γ t).2.2) (fun s t => (hlip s t).2) hW
  exact ⟨(y, z), hp.prodMk_nhds (hy.prodMk_nhds hz)⟩

/-- `dΘ_x(v) = dΘ₀(v_{(U,V)})` on `D`. -/
theorem fd_dcov {x : N} (hx : x.1.1 < 0) (v : E) :
    dcov fd_Θ x v = dTh (fun s => -Real.log s) x.1 v.1 := by
  have hG := goodG_log
  have hd : HasFDerivAt Θ₀ (dTh (fun s => -Real.log s) x.1) x.1 := hG.hasFDerivAt hx
  have hc : HasFDerivAt fd_Θ ((dTh (fun s => -Real.log s) x.1).comp
      (ContinuousLinearMap.fst ℝ P Q)) x := hd.comp x hasFDerivAt_fst
  have e : fderiv ℝ fd_Θ x v = dTh (fun s => -Real.log s) x.1 v.1 := by rw [hc.fderiv]; rfl
  unfold dcov
  rw [mfderiv_eq_fderiv]
  exact e

/-- `Θ` is temporal on `D`. -/
theorem fd_isTemporalOn : fd_S.IsTemporalOn (fd_S.D fd_J) fd_Θ := by
  have hG := goodG_log
  have hset : fd_S.D fd_J = (fun x : N => x.1) ⁻¹' {p : P | p.1 < 0} := by
    rw [fd_D_eq]; rfl
  refine ⟨?_, ?_⟩
  · rw [hset]
    have h1 : ContMDiffOn 𝓘(ℝ, P) 𝓘(ℝ, ℝ) 1 Θ₀ {p : P | p.1 < 0} := hG.contDiffOn.contMDiffOn
    have h2 : ContMDiff 𝓘(ℝ, E) 𝓘(ℝ, P) 1 (fun x : N => x.1) := contDiff_fst.contMDiff
    exact h1.comp h2.contMDiffOn (fun x hx => hx)
  · intro x hx v hv
    rw [fd_D_iff] at hx
    have e : MSpacetime.dfun fd_Θ x v = dTh (fun s => -Real.log s) x.1 v.1 := fd_dcov hx v
    rw [e]
    exact hG.dTh_pos hx (fd_futCausal_proj hv)

/-- The `(U, V)`-projection of an inextendible causal curve in `D` is one of the plane's. -/
noncomputable def fd_projCurve (c : fd_S.InextCausalCurveIn (fd_S.D fd_J)) :
    (mink.Dsp (range O)).InextCausalCurve where
  γ := fun t => (c.γ t).1
  cont := continuous_fst.comp c.cont
  mem := fun t => by
    show (c.γ t).1 ∈ mink.D (range O)
    rw [hl_D_eq]; exact (fd_D_iff _).1 (c.mem t)
  brk := c.brk
  brk_fin := c.brk_fin
  causal := fun t ht => by
    have hd := fd_hasDerivAt_fst (c.causal t ht).1
    refine ⟨hd.differentiableAt, ?_⟩
    rw [hd.deriv]
    exact fd_futCausal_proj (c.causal t ht).2
  inext_future := by
    rintro ⟨p, hp, hlim⟩
    obtain ⟨z, hz⟩ := fd_converge (fd_lip_abs c) hlim
    apply c.inext_future
    refine ⟨(p, z), ?_, hz⟩
    rw [fd_D_iff]
    have : p ∈ mink.D (range O) := hp
    rw [hl_D_eq] at this; exact this
  inext_past := by
    rintro ⟨p, hp, hlim⟩
    have hlim' : Tendsto (fun t => (c.γ (-t)).1) atTop (𝓝 p) := hlim.comp tendsto_neg_atTop_atBot
    obtain ⟨z, hz⟩ := fd_converge (γ := fun t => c.γ (-t))
      (fun s t => fd_lip_abs c (-s) (-t)) hlim'
    apply c.inext_past
    refine ⟨(p, z), ?_, ?_⟩
    · rw [fd_D_iff]
      have : p ∈ mink.D (range O) := hp
      rw [hl_D_eq] at this; exact this
    · have := hz.comp tendsto_neg_atBot_atTop
      simpa [Function.comp_def] using this

/-- **The Cauchy property on `N` (BUILT; the registered expected stop was not hit).**
`Θ = −log(−U) + V` is a Cauchy temporal function on `D = {U < 0} ⊆ ℝ⁴`. -/
theorem fd_isCauchyTemporalOn : fd_S.IsCauchyTemporalOn (fd_S.D fd_J) fd_Θ :=
  ⟨fd_isTemporalOn, fun c a => hl_cauchy_Θ₀.2 (fd_projCurve c) a⟩

/-- **Adapted**: `Θ(O τ) = τ + 0`. -/
theorem fd_adapt (τ : ℝ) : fd_Θ (fd_O τ) = τ + 0 := fd_O'_spec.2.2.2 τ

/-! ### The witness headline -/

/-- Every slice is non-empty: `O τ ∈ S_τ`. -/
theorem fd_slice_nonempty (τ : ℝ) : (fd_S.slice fd_J fd_Θ τ).Nonempty :=
  ⟨fd_O τ, (fd_D_iff _).2 (fd_O'_U τ), by rw [fd_adapt, add_zero]⟩

/-- **The four-dimensional witness headline (BUILT).** On `N = ℝ⁴ = (ℝ × ℝ) × (ℝ × ℝ)` (the model
space, its self chart), `g = −dU dV + dy² + dz²`, `T = ∂_U + ∂_V`, `M = N`, the Rindler observer
`UV = −1` at `y = z = 0`, and `Θ = −log(−U) + V`: every hypothesis of `mh_causal_alignment_gh_N`
and `mc_cone_kuratowski_N` is proved, and their conclusions hold with `𝓗⁺ = {U = 0}` (a non-empty
null hyperplane); every slice is non-empty. -/
theorem fd_witness_headline :
    Module.finrank ℝ E = 4 ∧ fd_S.LocallyOneChart ∧
    fd_S.IpastSet (range fd_O) = fd_S.D fd_J ∧
    (∀ s t, s < t → fd_S.Chr (fd_O s) (fd_O t)) ∧ fd_J ⊆ fd_S.M ∧
    fd_S.D fd_J = {x : N | x.1.1 < 0} ∧
    fd_S.H fd_J = {x : N | x.1.1 = 0} ∧ (fd_S.H fd_J).Nonempty ∧ fd_S.H fd_J ⊆ fd_S.M ∧
    fd_S.IsCauchyTemporalOn (fd_S.D fd_J) fd_Θ ∧ (∀ τ, fd_Θ (fd_O τ) = τ + 0) ∧
    fd_S.SublevelProper fd_J fd_Θ ∧
    KLi (fd_S.slice fd_J fd_Θ) = {x : N | x.1.1 = 0} ∧
    KLs (fd_S.slice fd_J fd_Θ) = {x : N | x.1.1 = 0} ∧
    KLi (fd_S.cone fd_O) = {x : N | x.1.1 = 0} ∧
    KLs (fd_S.cone fd_O) = {x : N | x.1.1 = 0} ∧
    (∀ τ, (fd_S.slice fd_J fd_Θ τ).Nonempty) := by
  have hOD : fd_S.IpastSet (range fd_O) = fd_S.D fd_J := rfl
  obtain ⟨h1, h2, h3⟩ := fd_S.mh_causal_alignment_gh_N fd_locallyOneChart hOD fd_hmono fd_JM fd_HM
    fd_isCauchyTemporalOn fd_adapt
  obtain ⟨h4, h5⟩ := MSpacetime.mc_cone_kuratowski_N fd_locallyOneChart hOD fd_hmono fd_JM
  rw [fd_H_eq] at h2 h3 h4 h5
  exact ⟨fd_dim, fd_locallyOneChart, hOD, fd_hmono, fd_JM, fd_D_eq, fd_H_eq, fd_H_nonempty, fd_HM,
    fd_isCauchyTemporalOn, fd_adapt, h1, h2, h3, h4, h5, fd_slice_nonempty⟩

/-! ### Tangency at every horizon point -/

/-- The generator direction `ℓ = ∂_V` of `𝓗⁺`, and `n = 2 ∂_U` (`g(ℓ, n) = −1`), constant fields. -/
def fd_ℓ : E := ((0, 1), 0)
def fd_n : E := ((2, 0), 0)

/-- **`W = {ℓ, n}^⊥` is the transverse plane** `{v_U = v_V = 0}`, on which `g = dy² + dz²`. -/
theorem fd_W_transverse (x : N) (e : E) :
    (fd_S.gE x fd_ℓ e = 0 ∧ fd_S.gE x fd_n e = 0) ↔ e.1 = 0 := by
  rw [fd_gE, fd_gE, gM_apply, gM_apply, fd_q_apply, fd_q_apply]
  simp only [fd_ℓ, fd_n, Prod.fst_zero, Prod.snd_zero, zero_mul, add_zero]
  constructor
  · rintro ⟨h1, h2⟩; ext <;> simp <;> linarith
  · intro h
    have h1 : e.1.1 = 0 := by rw [h]; rfl
    have h2 : e.1.2 = 0 := by rw [h]; rfl
    rw [h1, h2]; norm_num

theorem fd_W_metric (x : N) (e : E) (he : e.1 = 0) : fd_S.gE x e e = e.2.1 ^ 2 + e.2.2 ^ 2 := by
  rw [fd_gE_self, he]; simp

theorem fd_frameHyp {x : N} (hx : x.1.1 < 0) :
    TCF.FrameHyp (fd_S.gE x) fd_ℓ fd_n (dcov fd_Θ x) := by
  refine ⟨⟨fun v w => fd_S.symm x v w, ?_, ?_, ?_, fun e he1 he2 => ?_⟩, fun v hv => ?_⟩
  · rw [TCF.bil_apply, fd_gE]; simp [gM_apply, fd_ℓ]
  · rw [TCF.bil_apply, fd_gE]; simp [gM_apply, fd_n]
  · rw [TCF.bil_apply, fd_gE]; simp [gM_apply, fd_ℓ, fd_n]
  · rw [TCF.bil_apply] at he1 he2
    rw [TCF.bil_apply, fd_W_metric x e ((fd_W_transverse x e).1 ⟨he1, he2⟩)]
    positivity
  · obtain ⟨hv1, hv2⟩ := hv
    simp only [TCF.bil_apply] at hv1 hv2
    rw [fd_gE_self] at hv1
    rw [fd_gE, gM_apply, fd_q_apply] at hv2
    simp only [fd_ℓ, fd_n, Prod.mk_add_mk] at hv2
    have hb : 0 ≤ v.2.1 ^ 2 + v.2.2 ^ 2 := by positivity
    have hp : 0 ≤ v.1.1 * v.1.2 := by linarith
    have hs : 0 < v.1.1 + 2 * v.1.2 := by norm_num at hv2; linarith
    have hv1' : 0 ≤ v.1.1 := by
      by_contra h; push Not at h
      have : v.1.2 ≤ 0 := by nlinarith
      nlinarith
    have hv2' : 0 ≤ v.1.2 := by
      by_contra h; push Not at h
      have : v.1.1 ≤ 0 := by nlinarith
      nlinarith
    rw [fd_dcov hx]
    exact goodG_log.dTh_pos hx ((futCausal_iff _ _).2 ⟨hv1', hv2', by
      rcases hv1'.eq_or_lt with h0 | h0
      · rw [← h0] at hs ⊢; linarith
      · linarith⟩)

theorem fd_ratio {x : N} (hx : x.1.1 < 0) :
    dcov fd_Θ x fd_ℓ / dcov fd_Θ x fd_n = -x.1.1 / 2 := by
  have hs : (0:ℝ) < -x.1.1 := by linarith
  rw [fd_dcov hx, fd_dcov hx, dTh_apply, dTh_apply]
  have hl : HasDerivAt (fun s => -Real.log s) (-(-x.1.1)⁻¹) (-x.1.1) :=
    (Real.hasDerivAt_log hs.ne').neg
  rw [hl.deriv]
  simp only [fd_ℓ, fd_n]
  have hne : x.1.1 ≠ 0 := hx.ne
  field_simp
  ring

theorem fd_dchartL (q x : N) (v : E) : dchartL q x v = v := by
  unfold dchartL
  rw [fd_extChart, PartialEquiv.refl_coe, mfderiv_id]
  rfl

/-- **Tangency at every horizon point (BUILT).** At each `q ∈ 𝓗⁺ = {U = 0}`, along `𝓝[D] q` (a
proper filter), with the null frame `ℓ = ∂_V`, `n = 2∂_U` (`W = {ℓ, n}^⊥` the transverse plane,
`fd_W_transverse`): the rate `dΘ(ℓ)/dΘ(n) = −U/2 → 0`, and `mc_tangency_at_N` gives
`(dΘ(n))⁻¹ dΘ → −g_q(ℓ, ·) = ½ dU`. -/
theorem fd_witness_tangency (q : N) (hq : q ∈ fd_S.H fd_J) :
    (𝓝[fd_S.D fd_J] q).NeBot ∧
    (∀ᶠ x in 𝓝[fd_S.D fd_J] q, TCF.FrameHyp (fd_S.gE x) fd_ℓ fd_n (dcov fd_Θ x)) ∧
    (∀ x : N, ∀ e : E, (fd_S.gE x fd_ℓ e = 0 ∧ fd_S.gE x fd_n e = 0) ↔ e.1 = 0) ∧
    Tendsto (fun x => dcov fd_Θ x fd_ℓ / dcov fd_Θ x fd_n) (𝓝[fd_S.D fd_J] q) (𝓝 0) ∧
    Tendsto (fun x => (dcov fd_Θ x fd_n)⁻¹ • covCh fd_Θ q x) (𝓝[fd_S.D fd_J] q)
      (𝓝 (-(fd_S.gE q fd_ℓ))) ∧
    ∀ w : E, -(fd_S.gE q fd_ℓ w) = w.1.1 / 2 := by
  have hne : (𝓝[fd_S.D fd_J] q).NeBot :=
    mem_closure_iff_nhdsWithin_neBot.1
      (fd_S.mh_hcl fd_locallyOneChart fd_JM (frontier_subset_closure hq))
  have hF : ∀ᶠ x in 𝓝[fd_S.D fd_J] q, TCF.FrameHyp (fd_S.gE x) fd_ℓ fd_n (dcov fd_Θ x) := by
    filter_upwards [self_mem_nhdsWithin] with x hx using fd_frameHyp ((fd_D_iff x).1 hx)
  have hq0 : q.1.1 = 0 := by rw [fd_H_eq] at hq; exact hq
  have hr : Tendsto (fun x => dcov fd_Θ x fd_ℓ / dcov fd_Θ x fd_n) (𝓝[fd_S.D fd_J] q) (𝓝 0) := by
    have hc : Tendsto (fun x : N => -x.1.1 / 2) (𝓝[fd_S.D fd_J] q) (𝓝 0) := by
      have := ((((continuous_fst.comp continuous_fst).neg.div_const (2:ℝ))).tendsto q).mono_left
        (nhdsWithin_le_nhds (s := fd_S.D fd_J))
      simpa [hq0] using this
    refine hc.congr' ?_
    filter_upwards [self_mem_nhdsWithin] with x hx using (fd_ratio ((fd_D_iff x).1 hx)).symm
  have hn : ∀ᶠ x in 𝓝[fd_S.D fd_J] q, ‖dchartL q x fd_n‖ ≤ ‖fd_n‖ :=
    Eventually.of_forall fun x => by rw [fd_dchartL]
  have hℓ : Tendsto (fun x => dchartL q x fd_ℓ) (𝓝[fd_S.D fd_J] q) (𝓝 fd_ℓ) := by
    exact tendsto_const_nhds.congr' (Eventually.of_forall fun x => (fd_dchartL q x fd_ℓ).symm)
  have h := fd_S.mc_tangency_at_N fd_locallyOneChart (mem_univ q) nhdsWithin_le_nhds hF hn hℓ hr
  refine ⟨hne, hF, fd_W_transverse, hr, h, fun w => ?_⟩
  rw [fd_gE]; simp [gM_apply, fd_ℓ]; ring

/-- **Non-vacuity**: the tangency conclusions at the concrete horizon point `((0, 0), (0, 0))`. -/
theorem fd_tangency_origin :
    Tendsto (fun x => (dcov fd_Θ x fd_n)⁻¹ • covCh fd_Θ ((0, 0), 0) x)
      (𝓝[fd_S.D fd_J] ((0, 0), 0)) (𝓝 (-(fd_S.gE ((0, 0), 0) fd_ℓ))) ∧
    (𝓝[fd_S.D fd_J] (((0, 0), 0) : N)).NeBot :=
  ⟨(fd_witness_tangency _ (by rw [fd_H_eq]; rfl)).2.2.2.2.1,
    (fd_witness_tangency _ (by rw [fd_H_eq]; rfl)).1⟩

end FourD

/-! ## NEW (campaign 92 ①): the unbounded-stretch clause

`hs_stretch A H τ ε = {q ∈ H | infDist q (A τ) < ε}`. (S1) `hs_uniform_on_compact`: if `H ⊆ KLi A`,
every compact `K ⊆ H` is eventually inside the `ε`-stretch, with an actual point of `A τ` within `ε`
of each `q ∈ K` (`hs_uniform_on_compact_pts`). (S2) `hs_unbounded`: if moreover `H` lies in no
compact set, the `ε`-stretch eventually leaves every compact set. -/

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

namespace FourD
open Manifold Model

/-! ### The witness: `𝓗⁺ = {U = 0}` on `ℝ⁴` (a normed space, so its metric is native) -/

/-- On `N = ℝ⁴` the charted topology *is* the norm topology: `hs_stretch_N` applies with `rfl`. -/
theorem hs_topology_native :
    (inferInstance : MetricSpace N).toUniformSpace.toTopologicalSpace =
      (inferInstance : TopologicalSpace N) := rfl

theorem hs_H_subset_KLi : fd_S.H fd_J ⊆ KLi (fd_S.cone fd_O) := by
  rw [fd_witness_headline.2.2.2.2.2.2.2.2.2.2.2.2.2.2.1, fd_H_eq]

/-- A compact set has bounded `V`-coordinate. -/
theorem hs_V_bdd {K : Set N} (hK : IsCompact K) : ∃ T : ℝ, ∀ x ∈ K, x.1.2 ≤ T := by
  obtain ⟨T, hT⟩ := (hK.image (continuous_snd.comp continuous_fst)).bddAbove
  exact ⟨T, fun x hx => hT ⟨x, hx, rfl⟩⟩

/-- `𝓗⁺ = {U = 0}` lies in no compact set. -/
theorem hs_H_not_compact (K : Set N) (hK : IsCompact K) : ¬ fd_S.H fd_J ⊆ K := by
  intro hsub
  obtain ⟨T, hT⟩ := hs_V_bdd hK
  have hmem : (((0 : ℝ), T + 1), (0 : Q)) ∈ fd_S.H fd_J := by rw [fd_H_eq]; rfl
  have h : T + 1 ≤ T := hT _ (hsub hmem)
  linarith

/-- A straight causal step along the generator direction `∂_V`. -/
theorem hs_cstep_V (q : N) {s : ℝ} (hs : 0 < s) :
    fd_S.CStep q ((q.1.1, q.1.2 + s), q.2) := by
  set b : N := ((q.1.1, q.1.2 + s), q.2)
  set γ : ℝ → N := fun r => q + r • (b - q) with hγdef
  have hα : ContDiff ℝ 1 γ := contDiff_const.add (contDiff_id.smul contDiff_const)
  refine ⟨γ, hα.contMDiff, by simp [γ], by simp [γ], fun t _ => ⟨mem_univ _, ?_⟩⟩
  have d1 : HasDerivAt γ (b - q) t := by
    have h := ((hasDerivAt_id' t).smul_const (b - q)).const_add q
    rw [one_smul] at h
    exact h
  rw [fd_vel, d1.deriv, fd_futCausal_iff]
  simp only [b, Prod.fst_sub, Prod.snd_sub, sub_self, Prod.fst_zero, Prod.snd_zero]
  constructor <;> nlinarith

/-- **The generator through `q ∈ 𝓗⁺`** `{(0, V + s, y, z) : s ≥ 0}` lies in `J⁺(q) ∩ 𝓗⁺`. -/
theorem hs_generator_subset (q : N) (hq : q ∈ fd_S.H fd_J) (s : ℝ) (hs : 0 ≤ s) :
    fd_S.Cau q ((q.1.1, q.1.2 + s), q.2) ∧ ((q.1.1, q.1.2 + s), q.2) ∈ fd_S.H fd_J := by
  rw [fd_H_eq] at hq ⊢
  refine ⟨?_, hq⟩
  rcases hs.lt_or_eq with hs | hs
  · exact Relation.ReflTransGen.single (hs_cstep_V q hs)
  · subst hs; simp only [add_zero]; exact Relation.ReflTransGen.refl

/-- **`J⁺(q) ∩ 𝓗⁺` lies in no compact set**, for every `q ∈ 𝓗⁺`. -/
theorem hs_Jfut_H_not_compact (q : N) (hq : q ∈ fd_S.H fd_J) (K : Set N) (hK : IsCompact K) :
    ¬ ({p | fd_S.Cau q p} ∩ fd_S.H fd_J) ⊆ K := by
  intro hsub
  obtain ⟨T, hT⟩ := hs_V_bdd hK
  set s := |T| + |q.1.2| + 1
  have hs : 0 ≤ s := by positivity
  have h := hT _ (hsub (hs_generator_subset q hq s hs))
  have : q.1.2 + s ≤ T := h
  have h1 := le_abs_self T; have h2 := neg_abs_le q.1.2
  linarith

/-- **The witness headline for ①.** On `ℝ⁴` with `𝓗⁺ = {U = 0}` and the cones `∂J⁻(O τ)`:
`𝓗⁺` lies in no compact set; (S1); (S2); futureward, for every `T` the `ε`-stretch eventually has a
point with `V > T`; and for every `q ∈ 𝓗⁺`, `J⁺(q) ∩ 𝓗⁺` lies in no compact set. -/
theorem hs_witness :
    fd_S.H fd_J = {x : N | x.1.1 = 0} ∧
    (∀ K : Set N, IsCompact K → ¬ fd_S.H fd_J ⊆ K) ∧
    (∀ ε > 0, ∀ K : Set N, K ⊆ fd_S.H fd_J → IsCompact K →
      ∀ᶠ τ in atTop, K ⊆ hs_stretch (fd_S.cone fd_O) (fd_S.H fd_J) τ ε) ∧
    (∀ ε > 0, ∀ K : Set N, IsCompact K →
      ∀ᶠ τ in atTop, ¬ hs_stretch (fd_S.cone fd_O) (fd_S.H fd_J) τ ε ⊆ K) ∧
    (∀ ε > 0, ∀ T : ℝ, ∀ᶠ τ in atTop,
      ∃ q ∈ hs_stretch (fd_S.cone fd_O) (fd_S.H fd_J) τ ε, q.1.2 > T) ∧
    (∀ q ∈ fd_S.H fd_J, ∀ K : Set N, IsCompact K → ¬ ({p | fd_S.Cau q p} ∩ fd_S.H fd_J) ⊆ K) := by
  have hOD : fd_S.IpastSet (range fd_O) = fd_S.D fd_J := rfl
  refine ⟨fd_H_eq, hs_H_not_compact, fun ε hε K hKH hK => ?_, fun ε hε K hK => ?_,
    fun ε hε T => ?_, hs_Jfut_H_not_compact⟩
  · exact (MSpacetime.hs_stretch_N fd_locallyOneChart hOD fd_hmono fd_JM inferInstance
      hs_topology_native hε).1 K hKH hK
  · exact (MSpacetime.hs_stretch_N fd_locallyOneChart hOD fd_hmono fd_JM inferInstance
      hs_topology_native hε).2 hs_H_not_compact K hK
  · have hmem : (((0 : ℝ), T + 1), (0 : Q)) ∈ fd_S.H fd_J := by rw [fd_H_eq]; rfl
    filter_upwards [hs_uniform_on_compact hs_H_subset_KLi hε (singleton_subset_iff.2 hmem)
      isCompact_singleton] with τ hτ
    exact ⟨_, hτ rfl, by show T + 1 > T; linarith⟩

/-- Non-vacuity: at the origin of `𝓗⁺`, for `ε = 1`, eventually a point of the cone `∂J⁻(O τ)`
is within distance `1` (so the cones are eventually non-empty near `𝓗⁺`), and the origin lies in
the `1`-stretch. -/
theorem hs_origin :
    ∀ᶠ τ in atTop, (∃ a ∈ fd_S.cone fd_O τ, dist (((0 : ℝ), (0 : ℝ)), (0 : Q)) a < 1) ∧
      (((0 : ℝ), (0 : ℝ)), (0 : Q)) ∈ hs_stretch (fd_S.cone fd_O) (fd_S.H fd_J) τ 1 := by
  have hmem : (((0 : ℝ), (0 : ℝ)), (0 : Q)) ∈ fd_S.H fd_J := by rw [fd_H_eq]; rfl
  filter_upwards [hs_uniform_on_compact_pts hs_H_subset_KLi one_pos
      (singleton_subset_iff.2 hmem) isCompact_singleton,
    hs_uniform_on_compact hs_H_subset_KLi one_pos (singleton_subset_iff.2 hmem)
      isCompact_singleton] with τ h1 h2
  exact ⟨h1 _ rfl, h2 rfl⟩

end FourD

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
#print axioms mc_tendsto_limit_aux
#print axioms mc_tCC_eq
#print axioms mx_preimage_frontier
#print axioms mx_preimage_closure
#print axioms MSpacetime.mx_frontier_JpastSet
#print axioms MSpacetime.mx_range_subset_M
#print axioms MSpacetime.mx_H_eq_boundary
#print axioms MSpacetime.mx_prop_causal_alignment
#print axioms MSpacetime.cz_scale_chr
#print axioms MSpacetime.cz_scale_isCauchyTemporalOn
#print axioms MSpacetime.cz_scale_locallyOneChart

#print axioms FourD.fd_dim
#print axioms FourD.fd_chart_univ
#print axioms FourD.fd_hRep
#print axioms FourD.fd_locallyOneChart
#print axioms FourD.fd_futCausal_proj
#print axioms FourD.fd_futCausal_speed
#print axioms FourD.fd_chr_proj
#print axioms FourD.fd_tstep_of
#print axioms FourD.fd_hmono
#print axioms FourD.fd_D_eq
#print axioms FourD.fd_JpastSet_eq
#print axioms FourD.fd_H_eq
#print axioms FourD.fd_H_nonempty
#print axioms FourD.fd_isTemporalOn
#print axioms FourD.fd_mono
#print axioms FourD.fd_lip
#print axioms FourD.fd_converge
#print axioms FourD.fd_isCauchyTemporalOn
#print axioms FourD.fd_adapt
#print axioms FourD.fd_slice_nonempty
#print axioms FourD.fd_witness_headline
#print axioms FourD.fd_dcov
#print axioms FourD.fd_W_transverse
#print axioms FourD.fd_frameHyp
#print axioms FourD.fd_ratio
#print axioms FourD.fd_witness_tangency
#print axioms FourD.fd_tangency_origin


#print axioms hs_pointwise
#print axioms hs_uniform_on_compact_pts
#print axioms hs_uniform_on_compact
#print axioms hs_unbounded
#print axioms MSpacetime.hs_stretch_N
#print axioms FourD.hs_H_not_compact
#print axioms FourD.hs_cstep_V
#print axioms FourD.hs_generator_subset
#print axioms FourD.hs_Jfut_H_not_compact
#print axioms FourD.hs_witness
#print axioms FourD.hs_origin

end ShadowProbe.HorizonStretchProbe

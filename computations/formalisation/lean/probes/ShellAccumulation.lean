import Mathlib

/-!
# Probe `r7693+71.1` (campaign 108): on the shell model the slices and the past cones accumulate on `𝓗⁺` alone

Registration: `computations/formalisation/r7693_71_campaign108/PREDICTION.md` (`r7693` ①, 8ii-e).
Nothing imports this file, and it imports only Mathlib. It starts as a copy of campaign 105's
`probes/ShellMatter.lean` (namespace renamed `ShadowProbe.ShellAccumulationProbe`, all old names
kept). Everything new has the prefix `sa2_`: the generic copy of campaign 91's cone disjointness
(`MSpacetime.sa2_cone_disjoint`, from `ConeDisjoint.lean`) in section `SA2Generic`, and the rest in
namespace `SA2Model`, just after campaign 105's `SMModel` and before the `#print axioms` block.

**① Flat ingredients — BUILT.** `sa2_flat_locallyOneChart`: `sh_flat = cz_St.restrictM M′` is
`LocallyOneChart` (`cz_locallyOneChart.restrict`). `sa2_S_chr/_D/_H/_slice/_cone/_sublevelProper`:
`sh_S = sh_flat.cz_scale Φ′` has `sh_flat`'s causal data. `sa2_flat_causal`: on `sh_flat`,
`D = {ũ < u_H}`, `𝓗⁺ = {ũ = u_H} ⊆ M′`, `O` chronological. `sa2_flat_cauchy`: `Θ_shell` is Cauchy
temporal on `sh_flat`'s `D` for `0 < a`, `0 < η ≤ 2`.

**② The adapted observer (the registered expected stop) — BUILT.** `sa2_curve`: `sv_O` is an
inextendible causal curve in `sh_flat`'s `D`. `g = Θ_shell ∘ sv_O` (`sa2_g`) is continuous,
strictly increasing (`mh_temporalD_chr`) and onto `ℝ` (Cauchy). `sa2_O = sv_O ∘ g⁻¹`
(`g⁻¹ = sa2_ginv`, a strictly increasing continuous bijection); `sa2_O_adapted`: `range O′ = range O`,
`O′` chronological on `sh_flat` and `sh_S`, continuous, and `Θ_shell(O′ τ) = τ` (`c = 0`).

**③ The accumulation — BUILT.** `sa2_flat` (`mh_causal_alignment_gh_N` on `sh_flat`, `J = range O′
= range O`): properness, `KLi(S_τ) = KLs(S_τ) = 𝓗⁺`. `sa2_flat_cones` (`mc_cone_kuratowski_N`):
the cones of `O′`, and of `O`, converge to `𝓗⁺`. `sa2_flat_cone_disjoint`: no cone meets `𝓗⁺`.
Headline `sa2_shell`: all of it on the `C⁰` shell `sh_S`, with `𝓗⁺ = {ũ = u_H}`, by
`cz_scale_*`; `Φ′` never enters. Tangency is not claimed on the shell. `sa2_nonvacuous`
(`M = 1`, `v₀ = 0`, `a = 1`, `η = 2`): `𝓗⁺ ≠ ∅`, and `(−4, −1) ∈ 𝓗⁺` (`v < v₀`, `Φ′ = 1`) lies in
`KLi` of the slices and of the cones.

`#print axioms` for every new theorem at the end: each reads `[propext, Classical.choice, Quot.sound]`.
-/

/-!
# Probe `r7687+71.2` (campaign 105): the collapsing matter on the shell model

Registration: `computations/formalisation/r7687_71_campaign105/PREDICTION.md` (`r7687` ②, 7d).
Nothing imports this file, and it imports only Mathlib. It starts as a copy of campaign 102's
`probes/SchwarzschildShellHorizon.lean` (namespace renamed `ShadowProbe.ShellAccumulationProbe`, all old
names kept). Everything new has the prefix `sm_` and sits in namespace `SMModel`, just after
campaign 102's `SHModel` and before the `#print axioms` block.

**The matter — a modelling choice.** `sm_matter M v₀ = {v = v₀} ∩ M′`: the thin shell, read off
where the metric changes form (`sh_flat_past` / `sh_vacuum`); the kit has no stress-energy. One
infalling element per point of the radial plane's shell.

**The shell ray — BUILT (the registered expected stop).** `sm_γ M v₀ s = (u_H − e^{−s}, v₀)`;
`sm_curve`: an `InextCausalCurveIn D` of `sh_S` (`C^∞`, no breaks, velocity `(e^{−s}, 0)`, future
null; `ũ → −∞` to the past; `γ → (u_H, v₀) ∉ D` to the future). `sm_matter_D`: `D ∩ 𝔐 = range γ`.
`sm_Θ_γ`: `Θ(γ(s)) = a(4Ms + (η/2 − 1)e^{−s} + const)`, strictly increasing (`η ≤ 2`).

**① — BUILT.** `sm_slice_meets_matter`: for `0 < a`, `0 < η ≤ 2` and every `τ`, `S_τ ∩ 𝔐` has
exactly one point, `γ(s_τ)` (`sh_cauchy_D` on `sm_curve`). `sm_outside_H`: `S_τ ∩ 𝔐 ∩ 𝓗⁺ = ∅`.

**② — BUILT.** `sm_finite`: at the slice point `r = (v₀ − ũ)/2 > 2M`, and `S_τ ∩ 𝔐` is a
singleton, hence compact.

**③ — BUILT.** `sm_approaches`: `γ → (u_H, v₀) ∈ 𝓗⁺` with `r = 2M` there; `Θ ∘ γ → ∞`; the slice
parameter `s_τ` (`sm_sτ`) is strictly increasing with `s_τ → ∞`; `ũ(γ(s_τ)) < u_H` on every slice,
and `γ(s_τ) → (u_H, v₀)` as `τ → ∞`. `sm_nonvacuous` (`M = 1`, `v₀ = 0`, `a = 1`, `η = 2`):
`S_0 ∩ 𝔐 = {(−8, 0)}`, `r = 4 > 2`.

`#print axioms` for every new declaration at the end: each reads
`[propext, Classical.choice, Quot.sound]`.
-/

/-!
# Probe `r7685+71.1` (campaign 102): the frontier of `D` on the shell model is `𝓗⁺` alone

Registration: `computations/formalisation/r7685_71_campaign102/PREDICTION.md` (`r7685` ①). Nothing
imports this file, and it imports only Mathlib. It starts as a copy of campaign 101's
`probes/SchwarzschildCollapse.lean` (namespace renamed `ShadowProbe.ShellAccumulationProbe`,
all old names kept). Everything new has the prefix `sh_` and sits in namespace `SHModel`, just
after campaign 101's `SVModel` and before the `#print axioms` block.

**① The extended model — BUILT.** `M′ = sh_MS M v₀ = {ũ < v₀} ∩ {U(ũ) V(v) < 1}` (open), with
campaign 101's smooth `U = sv_χU`, `V = sv_χV`. `Φ′ = sh_Φ = F_K(r) U′(ũ) V/4M` at `(ũ, max(v, v₀))`,
`r = r_K(UV)`, `1` off `M′`: positive (`sh_Φ_pos`), continuous on `M′` (`sh_Φ_continuousOn`).
`sh_S hM v₀ = (cz_St restricted to M′).cz_scale Φ′`, so `g = −Φ′ dũ dv` (`sh_hRep`).
* The identity checked in advance, `sh_UV_shell`: `−U(ũ) V(v₀) = h((v₀ − ũ)/2)` for every `ũ`, so
  `r = r_s = (v₀ − ũ)/2` on the shell (`sh_r_shell`) and `Φ′ = 1` for `v ≤ v₀` (`sh_flat_past`, on
  both sides of the horizon).
* `sh_vacuum`: for `v ≥ v₀`, `Φ′ = F_K(r) U′ V′` with `U′ = dU/dũ`, `V′ = V/4M`, `h(r) = −UV`:
  Kruskal's `−F_K dU dV` pulled back.
* `sh_agree`: `Φ′ = Φ` (campaign 101's `sv_Φ`) on `D = {ũ < u_H}`, i.e. `F_K dU dV = f du dv`.

**② Causal structure — BUILT.** `sh_seg_mem` (`M′` is null-convex: `U` increases on `ũ < v₀` and
`UV ≤ U_y V_y` where `U > 0`); `sh_chr`: `x ≪ y ⇔ ũ_x < ũ_y ∧ v_x < v_y` on `M′`; `sh_cau_le`: causal
curves raise both null coordinates. For campaign 101's observer `O(τ) = (u_H − e^{−τ}, τ)`
(`sh_O`: in `M′`, future timelike, `ũ → u_H⁻`, `v → ∞`): `sh_D`: `D = I⁻(O) = {ũ < u_H}`, and
`sh_Jpast`: `J⁻(O) = {ũ < u_H}` (the registered expected stop — not hit).

**③ The frontier — BUILT.** `sh_frontier`: `S.H (range O) = frontier_P J⁻(O) = {ũ = u_H}`, the
future horizon alone (no past component); `sh_H_sub`: `𝓗⁺ ⊆ M′` (`U(u_H) = 0`). On it, `r = 2M`
(`sh_H_r`; the vacuum side `v ≥ v₀`), and `Φ′ = 1` where `v ≤ v₀` (`sh_H_flat`): the horizon forms
inside the flat body before the shell arrives. `sh_cauchy_D`: the retarded slicing `sv_Θsh` is
Cauchy temporal on `D` for `0 < η ≤ 2` (campaign 101's `sv_cauchy_flat` carried to `sh_flat`, which
has the same `g` and `T`, then conformal invariance). Headline `sh_headline_D` collects them;
`sh_nonvacuous` (`M = 1`, `v₀ = 0`): `(−4, −1) ∈ 𝓗⁺` with `Φ′ = 1`, `(−4, 1) ∈ 𝓗⁺` with `r = 2`,
`(−3, 0) ∈ M′ ∖ D`, `Φ′(−5, 1) > 1`, Cauchy at `η = 2`.

As registered, the headline accumulation machinery does not run: `Φ′` has a kink at `v = v₀`, so
`LocallyOneChart` (`C¹` in the chart) fails and `mh_causal_alignment_gh_N` is not applied.

`#print axioms` for every new declaration at the end: each reads
`[propext, Classical.choice, Quot.sound]`.
-/

/-!
# Probe `r7683+71.1` (campaign 101): the collapse exterior, the retarded slicing is Cauchy

Registration: `computations/formalisation/r7683_71_campaign101/PREDICTION.md` (P1 `lem:alignment`
(ii)). Nothing imports this file, and it imports only Mathlib. It starts as a copy of campaign 100's
`probes/SchwarzschildConformal.lean` (namespace renamed `ShadowProbe.ShellAccumulationProbe`,
all old names kept). Everything new has the prefix `sv_`, and sits in namespace `SVModel` (two
generic lemmas, `sv_monotone_of_brk` and `MSpacetime.sv_cauchy_of_limits`, sit just before it),
just before the `#print axioms` block.

**The engine — BUILT.** `MSpacetime.sv_cauchy_of_limits`: on an open `U`, a temporal `Θ` with
`Θ → +∞` at the future end and `Θ → −∞` at the past end of every `InextCausalCurveIn U` is
`IsCauchyTemporalOn U` (continuity, strict monotonicity off the breaks via `strictMonoOn_of_brk`,
`Continuous.surjective`). `sv_monotone_of_brk`: `U`, `V` are monotone along causal curves on all
of `ℝ` (not only `[0, ∞)`).

**ⓐ The eternal core lemma — BUILT, including `η = 2`.** On campaign 99's region I,
`Θ_ψ = sv_Θψ M a η v₀ = sr_Θ + aη ψ(4M log V)`, `ψ(v) = −(v₀ − v) smoothTransition(v₀ − v)`
(`C^∞`, `0` for `v ≥ v₀`, monotone, `ψ ≤ 0`, `ψ(v) ≤ v − v₀ + 1`).
* `sv_eternal_cauchy`: `(se_S hM).IsCauchyTemporalOn D (sv_Θψ M a η v₀)` for `0 < η ≤ 2`;
  `sv_eternal_eq`: `Θ_ψ = Θ_ret` on `{4M log V ≥ v₀}`.
* Future end `sv_future_pure` (campaign 99's argument plus `ψ(v(t)) ≥ ψ(v(0))`).
* Past end `sv_past_pure`, the new part, stated for monotone paths in region I with no limit
  there. `V → 0`: `log V → −∞` in both regimes (`r < 4M`: `ψ(v) ≤ v − v₀ + 1`; `r ≥ 4M`: the exact
  identity with `η/2 − 1 ≤ 0`). `V → V_∞ > 0`, `U → −∞`: `r → ∞` and the exact identity
  `sv_r_identity`, `r = 2M(log(−U) + log V − log(r/2M − 1))`, gives
  `Θ_ψ ≤ C − 2Mηa log(r/2M − 1) → −∞` uniformly in `0 < η ≤ 2`. The registered expected stop
  (`η = 2`) was not hit; `sv_eta2_identity` states P1's form
  `−4M log(−U) + 2r = 4M log V − 4M log(r/2M − 1)`.

**ⓑ The thin-shell model — BUILT.** On `P` with coordinates `(ũ, v)`, `M = {ũ < u_H}`,
`u_H = v₀ − 4M`; `sv_S hM v₀ = (cz_St restricted to M).cz_scale Φ`, so `g = −Φ dũ dv` (`sv_hRep`).
`Φ = (1 − 2M/r(ũ, max(v, v₀))) F′(ũ)` on `M` (`1` off it), positive (`sv_Φ_pos`), continuous on `M`
(`sv_Φ_continuousOn`).
* `sv_flat_past`: `Φ = 1` for `v ≤ v₀`. `sv_vacuum`: for `v ≥ v₀`, `Φ = f(r) F′(ũ)` with
  `F′ = (sv_F)′` (`u = F(ũ) = ũ − 4M log((v₀ − ũ)/4M − 1)`) and `h(r) = e^{(v − u)/4M}`, i.e. `r` is
  Schwarzschild's areal radius at `(u, v)`. `sv_Φ_gt_one`: `Φ > 1` for `v > v₀`.
* `χ(ũ, v) = (−e^{−F(ũ)/4M}, e^{v/4M})` (`sv_χU_eq`), written as the smooth
  `U(ũ) = −((v₀ − ũ)/4M − 1) e^{−ũ/4M}`; it maps `M` into region I preserving both null orders.
* `sv_D`: `D = I⁻(O) = M` for the observer `O(τ) = (u_H − e^{−τ}, τ)` (in `M`, future timelike,
  `ũ → u_H`).
* `sv_cauchy`: `Θ_shell = Θ_ψ ∘ χ` is Cauchy temporal on `M` (and on `D`, `sv_cauchy_D`) for
  `0 < η ≤ 2`. Transported as in campaign 98, but through the curves: `χ ∘ γ` is a monotone path in
  region I with no limit there (`sv_shell_fut`, `sv_shell_past`), so ⓐ's two pure end lemmas
  apply; temporality by the chain rule (`Dχ = diag(U′, V/4M)`, `U′ > 0`); conformal invariance
  (`cz_scale_isCauchyTemporalOn`) removes `Φ`, whose kink at the shell never enters.
* `sv_retarded_eq`: on `v ≥ v₀`, `Θ_shell = a(F(ũ) + η r)`, i.e. `a(u + ηr)`.
* `sv_nonvacuous` (`M = 1`, `v₀ = 0`, `a = 1`): Cauchy at `η = 2` and `η = 1`, the eternal lemma
  at `η = 2`, `Φ(−5, 0) = 1 < Φ(−5, 1)`, `Θ_shell` not constant.

**ⓒ Stretch — not attempted** (the black-hole side inside `M`).

Limits (as registered): the radial plane only; the flat past is two-dimensional Minkowski with no
regular centre; the shell is thin (`Φ` is only `C⁰` across it); `Θ = a(u + ηr)` on the vacuum
exterior, a smooth continuation inside the body. The frontier of `D` is not computed.

`#print axioms` for every new declaration at the end: each reads
`[propext, Classical.choice, Quot.sound]`.

# Campaign 100's header, kept
-/

/-!
# Probe `r7681+71` (campaign 100): a `ConformalExtension` on Schwarzschild's `W`, so that `𝓗⁺ = ∂J⁻(𝒥⁺)`

Registration: `computations/formalisation/r7681_71_campaign100/PREDICTION.md`. Nothing imports this
file, and it imports only Mathlib. It starts as a copy of campaign 99's
`probes/SchwarzschildRetarded.lean` (namespace renamed `ShadowProbe.ShellAccumulationProbe`,
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
(namespace renamed `ShadowProbe.ShellAccumulationProbe`, all old names kept), with the `r_U`,
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

namespace ShadowProbe.ShellAccumulationProbe

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

/-! ## NEW (campaign 101): the collapse exterior, the retarded slicing continued through a thin shell -/

section SVGeneric
open Manifold
set_option linter.unusedSectionVars false

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
variable {N : Type*} [TopologicalSpace N] [ChartedSpace E N] [IsManifold 𝓘(ℝ, E) 1 N]

/-- A continuous `f` with `f′ ≥ 0` off a locally finite set is monotone on all of `ℝ` (`f + εt` is
strictly increasing by `strictMonoOn_of_brk`; let `ε → 0`). -/
theorem sv_monotone_of_brk {f : ℝ → ℝ} {B : Set ℝ} (hB : ∀ a b, (B ∩ Icc a b).Finite)
    (hf : Continuous f) (hd : ∀ t ∉ B, DifferentiableAt ℝ f t ∧ 0 ≤ deriv f t) :
    Monotone f := by
  intro s t hst
  rcases hst.lt_or_eq with h | h
  · refine le_of_forall_pos_lt_add fun δ hδ => ?_
    set ε := δ / (t - s) with hε
    have hεpos : 0 < ε := div_pos hδ (sub_pos.2 h)
    have hg : Continuous (fun x => f x + ε * x) := hf.add (continuous_const.mul continuous_id)
    have hd' : ∀ x ∉ B, 0 < deriv (fun x => f x + ε * x) x := by
      intro x hx
      obtain ⟨h1, h2⟩ := hd x hx
      have : HasDerivAt (fun x => f x + ε * x) (deriv f x + ε * 1) x :=
        h1.hasDerivAt.add ((hasDerivAt_id x).const_mul ε)
      rw [this.deriv]; linarith
    have hfin : (B ∩ Ioo s t).Finite :=
      (hB s t).subset (inter_subset_inter_right _ Ioo_subset_Icc_self)
    have key := Spacetime.strictMonoOn_of_brk hg hd' _ s t hfin le_rfl ⟨le_rfl, h.le⟩
      ⟨h.le, le_rfl⟩ h
    have e : ε * t - ε * s = δ := by rw [hε]; field_simp
    simp only at key
    linarith
  · rw [h]

namespace MSpacetime

/-- **The Cauchy criterion (BUILT, generic).** On an open `U`, a temporal `Θ` that tends to `+∞` at
the future end and to `−∞` at the past end of every inextendible causal curve of `U` is Cauchy
temporal: `Θ ∘ γ` is continuous and strictly increasing (`dΘ(γ′) > 0` off the breaks,
`strictMonoOn_of_brk`), so it takes every value exactly once (`Continuous.surjective`). -/
theorem sv_cauchy_of_limits {S : MSpacetime E N} {U : Set N} (hU : IsOpen U) {Θ : N → ℝ}
    (hΘ : S.IsTemporalOn U Θ)
    (hfut : ∀ c : S.InextCausalCurveIn U, Tendsto (fun t => Θ (c.γ t)) atTop atTop)
    (hpast : ∀ c : S.InextCausalCurveIn U, Tendsto (fun t => Θ (c.γ t)) atBot atBot) :
    S.IsCauchyTemporalOn U Θ := by
  refine ⟨hΘ, fun c a => ?_⟩
  have hf : Continuous (fun t => Θ (c.γ t)) :=
    hΘ.1.continuousOn.comp_continuous c.cont c.mem
  have hd : ∀ t ∉ c.brk, 0 < deriv (fun t => Θ (c.γ t)) t := by
    intro t ht
    obtain ⟨hγd, hft⟩ := c.causal t ht
    rw [(MSpacetime.me_temporal_hasDerivAt hU hΘ.1 hγd (c.mem t)).deriv]
    exact hΘ.2 _ (c.mem t) _ hft
  have hmono : StrictMono (fun t => Θ (c.γ t)) := by
    intro s t hst
    have hfin : (c.brk ∩ Ioo s t).Finite :=
      (c.brk_fin s t).subset (inter_subset_inter_right _ Ioo_subset_Icc_self)
    exact Spacetime.strictMonoOn_of_brk hf hd _ s t hfin le_rfl ⟨le_rfl, hst.le⟩
      ⟨hst.le, le_rfl⟩ hst
  obtain ⟨t, ht⟩ := hf.surjective (hfut c) (hpast c) a
  exact ⟨t, ht, fun s hs => hmono.injective (hs.trans ht.symm)⟩

end MSpacetime

end SVGeneric

namespace SVModel
open Model SEModel SRModel Kruskal Manifold ContinuousLinearMap TopologicalSpace

set_option synthInstance.maxHeartbeats 400000

/-! ### The profile `ψ` -/

/-- **`ψ(v) = −(v₀ − v) · smoothTransition(v₀ − v)`**: `C^∞`, `0` for `v ≥ v₀`, non-decreasing,
`→ −∞` at `−∞`. -/
noncomputable def sv_ψ (v₀ v : ℝ) : ℝ := -((v₀ - v) * Real.smoothTransition (v₀ - v))

lemma sv_ψ_contDiff (v₀ : ℝ) : ContDiff ℝ 1 (sv_ψ v₀) := by
  unfold sv_ψ
  have h : ContDiff ℝ 1 (fun v : ℝ => v₀ - v) := contDiff_const.sub contDiff_id
  exact (h.mul (Real.smoothTransition.contDiff.comp h)).neg

lemma sv_ψ_eq_zero {v₀ v : ℝ} (h : v₀ ≤ v) : sv_ψ v₀ v = 0 := by
  simp [sv_ψ, Real.smoothTransition.zero_of_nonpos (by linarith : v₀ - v ≤ 0)]

lemma sv_g_nonneg (w : ℝ) : 0 ≤ w * Real.smoothTransition w := by
  rcases le_or_gt w 0 with h | h
  · rw [Real.smoothTransition.zero_of_nonpos h, mul_zero]
  · exact mul_nonneg h.le (Real.smoothTransition.nonneg w)

lemma sv_ψ_nonpos (v₀ v : ℝ) : sv_ψ v₀ v ≤ 0 := by
  unfold sv_ψ; linarith [sv_g_nonneg (v₀ - v)]

lemma sv_ψ_le (v₀ v : ℝ) : sv_ψ v₀ v ≤ v - v₀ + 1 := by
  unfold sv_ψ
  rcases le_or_gt 1 (v₀ - v) with h | h
  · rw [Real.smoothTransition.one_of_one_le h]; linarith
  · nlinarith [sv_g_nonneg (v₀ - v)]

lemma sv_ψ_mono (v₀ : ℝ) : Monotone (sv_ψ v₀) := by
  intro x y hxy
  unfold sv_ψ
  have hw : v₀ - y ≤ v₀ - x := by linarith
  have key : (v₀ - y) * Real.smoothTransition (v₀ - y) ≤
      (v₀ - x) * Real.smoothTransition (v₀ - x) := by
    rcases le_or_gt (v₀ - y) 0 with h | h
    · rw [Real.smoothTransition.zero_of_nonpos h, mul_zero]; exact sv_g_nonneg _
    · exact mul_le_mul hw (Real.smoothTransition.monotone hw) (Real.smoothTransition.nonneg _)
        (by linarith)
  linarith

lemma sv_ψ_tendsto (v₀ : ℝ) : Tendsto (sv_ψ v₀) atBot atBot :=
  tendsto_atBot_atBot.2 fun b => ⟨b + v₀ - 1, fun v hv => by linarith [sv_ψ_le v₀ v]⟩

lemma sv_ψ_hasDerivAt (v₀ v : ℝ) : HasDerivAt (sv_ψ v₀) (deriv (sv_ψ v₀) v) v :=
  ((sv_ψ_contDiff v₀).differentiable one_ne_zero v).hasDerivAt

lemma sv_ψ_deriv_nonneg (v₀ v : ℝ) : 0 ≤ deriv (sv_ψ v₀) v := (sv_ψ_mono v₀).deriv_nonneg

/-! ### `Θ_ψ` on region I -/

variable {M : ℝ} (hM : 0 < M)

/-- `Θ_ψ` in the plane: `a(−4M log(−U) + η r) + aη ψ(4M log V)`. -/
noncomputable def sv_QP (M a η v₀ : ℝ) (y : P) : ℝ :=
  sa_uP M a η y + a * η * sv_ψ v₀ (4 * M * Real.log y.2)

/-- **`Θ_ψ = Θ_ret + aη ψ(4M log V)` on `W`** (`v = 4M log V` is the advanced time). -/
noncomputable def sv_Θψ (M a η v₀ : ℝ) (x : seW) : ℝ :=
  sr_Θ M a η x + a * η * sv_ψ v₀ (4 * M * Real.log x.1.2)

lemma sv_Θψ_eq (M a η v₀ : ℝ) : sv_Θψ M a η v₀ = fun x : seW => sv_QP M a η v₀ x.1 := by
  funext x
  show sr_Θ M a η x + _ = _
  rw [sr_Θ_eq]; rfl

/-- **`Θ_ψ = Θ_ret` on `{v ≥ v₀}` (BUILT).** -/
theorem sv_eternal_eq (M a η v₀ : ℝ) (x : seW) (hx : v₀ ≤ 4 * M * Real.log x.1.2) :
    sv_Θψ M a η v₀ x = sr_Θ M a η x := by
  rw [sv_Θψ, sv_ψ_eq_zero hx, mul_zero, add_zero]

/-- `dΘ_ψ = dΘ_ret + aη ψ′(4M log V) (4M/V) dV`. -/
noncomputable def sv_QD (M a η v₀ : ℝ) (y : P) : P →L[ℝ] ℝ :=
  sa_uD M a η y + (a * η * (deriv (sv_ψ v₀) (4 * M * Real.log y.2) * (4 * M / y.2))) •
    snd ℝ ℝ ℝ

lemma sv_ψV_hasFDerivAt (v₀ : ℝ) {y : P} (hy : 0 < y.2) :
    HasFDerivAt (fun y : P => sv_ψ v₀ (4 * M * Real.log y.2))
      ((deriv (sv_ψ v₀) (4 * M * Real.log y.2) * (4 * M / y.2)) • snd ℝ ℝ ℝ) y := by
  have h1 : HasFDerivAt (fun y : P => 4 * M * Real.log y.2) ((4 * M) • (y.2⁻¹ • snd ℝ ℝ ℝ)) y :=
    (hasFDerivAt_snd.log hy.ne').const_mul (4 * M)
  have h2 := (sv_ψ_hasDerivAt v₀ (4 * M * Real.log y.2)).comp_hasFDerivAt y h1
  refine h2.congr_fderiv ?_
  ext <;> simp [div_eq_mul_inv]

include hM in
lemma sv_QP_hasFDerivAt (a η v₀ : ℝ) {y : P} (hy : y ∈ seR) :
    HasFDerivAt (sv_QP M a η v₀) (sv_QD M a η v₀ y) y := by
  have h := (sv_ψV_hasFDerivAt (M := M) v₀ hy.2).const_mul (a * η)
  refine ((sa_uP_hasFDerivAt hM a η hy).add h).congr_fderiv ?_
  ext <;> simp [sv_QD]

include hM in
lemma sv_QP_contDiffOn (a η v₀ : ℝ) : ContDiffOn ℝ 1 (sv_QP M a η v₀) seR := by
  have hlog : ContDiffOn ℝ 1 (fun y : P => 4 * M * Real.log y.2) seR :=
    contDiffOn_const.mul (contDiff_snd.contDiffOn.log fun y hy => hy.2.ne')
  exact (sa_uP_contDiffOn hM a η).add
    (contDiffOn_const.mul ((sv_ψ_contDiff v₀).comp_contDiffOn hlog))

include hM in
/-- On region I, for `0 < η ≤ 2`: `∂_U Θ_ψ > 0` and `∂_V Θ_ψ > 0`. -/
lemma sv_QD_pos {a η : ℝ} (v₀ : ℝ) (ha : 0 < a) (hη : 0 < η) (hη2 : η ≤ 2) {y : P}
    (hy : y ∈ seR) : 0 < sv_QD M a η v₀ y (1, 0) ∧ 0 < sv_QD M a η v₀ y (0, 1) := by
  have hu : 0 < -y.1 := neg_pos.2 hy.1
  have hh := sa_hK'_pos hM (sk_rK_spec hM (sr_seR_kM hy)).1
  have hq := sr_q_pos hM hy
  have hk : 0 < sa_k M η y := by
    rw [sr_k_eq hM η (sr_seR_kM hy)]
    refine mul_pos (Real.exp_pos _) ?_
    nlinarith [mul_nonneg (show 0 ≤ 2 - η by linarith) hq.le]
  have hA : 0 < sa_uD M a η y (1, 0) := by
    rw [sa_uD_U a η hu hh]; exact div_pos (mul_pos ha hk) (mul_pos hu hh)
  have hB : 0 < sa_uD M a η y (0, 1) := by
    rw [sa_uD_V]; exact div_pos (mul_pos (mul_pos ha hη) hu) hh
  have hψ := sv_ψ_deriv_nonneg v₀ (4 * M * Real.log y.2)
  have hV : 0 ≤ 4 * M / y.2 := div_nonneg (by positivity) hy.2.le
  constructor
  · simp only [sv_QD, add_apply, smul_apply, coe_snd', smul_eq_mul, mul_zero, add_zero]
    exact hA
  · simp only [sv_QD, add_apply, smul_apply, coe_snd', smul_eq_mul, mul_one]
    have : 0 ≤ a * η * (deriv (sv_ψ v₀) (4 * M * Real.log y.2) * (4 * M / y.2)) :=
      mul_nonneg (mul_pos ha hη).le (mul_nonneg hψ hV)
    linarith

include hM in
/-- **The exact identity on region I:** `r = 2M (log(−U) + log V − log(r/2M − 1))`
(from `h(r) = (r/2M − 1) e^{r/2M} = −UV`). -/
theorem sv_r_identity {y : P} (hy : y ∈ seR) :
    rK M y = 2 * M * (Real.log (-y.1) + Real.log y.2 - Real.log (rK M y / (2 * M) - 1)) := by
  have hh := (sk_rK_spec hM (sr_seR_kM hy)).2
  have hq := sr_q_pos hM hy
  unfold hK at hh
  have hl := congrArg Real.log hh
  rw [Real.log_mul hq.ne' (Real.exp_pos _).ne', Real.log_exp,
    show -(y.1 * y.2) = (-y.1) * y.2 by ring,
    Real.log_mul (neg_pos.2 hy.1).ne' hy.2.ne'] at hl
  have e : rK M y / (2 * M) =
      Real.log (-y.1) + Real.log y.2 - Real.log (rK M y / (2 * M) - 1) := by linarith
  have hM' : (2 * M) ≠ 0 := by positivity
  calc rK M y = 2 * M * (rK M y / (2 * M)) := by field_simp
    _ = _ := by rw [← e]

include hM in
/-- **The `η = 2` identity (BUILT):** `−4M log(−U) + 2r = 4M log V − 4M log(r/2M − 1)`. -/
theorem sv_eta2_identity {y : P} (hy : y ∈ seR) :
    -4 * M * Real.log (-y.1) + 2 * rK M y =
      4 * M * Real.log y.2 - 4 * M * Real.log (rK M y / (2 * M) - 1) := by
  have := sv_r_identity hM hy
  linear_combination 2 * this

include hM in
/-- For `r ≥ 4M`: `Θ_ψ ≤ a((2Mη − 4M) log(−U) + 2Mη log V − 2Mη log(r/2M − 1))` (exact
identity, `ψ ≤ 0`). -/
lemma sv_Q_le_far {a η v₀ : ℝ} (ha : 0 < a) (hη : 0 < η) {y : P} (hy : y ∈ seR) :
    sv_QP M a η v₀ y ≤ a * ((2 * M * η - 4 * M) * Real.log (-y.1) + 2 * M * η * Real.log y.2 -
      2 * M * η * Real.log (rK M y / (2 * M) - 1)) := by
  have hid := sv_r_identity hM hy
  have hψ := sv_ψ_nonpos v₀ (4 * M * Real.log y.2)
  have e : sv_QP M a η v₀ y = a * (-(4 * M) * Real.log (-y.1) + η * rK M y) +
      a * η * sv_ψ v₀ (4 * M * Real.log y.2) := rfl
  rw [e]
  set q := Real.log (rK M y / (2 * M) - 1)
  rw [hid]
  nlinarith [mul_nonneg (mul_pos ha hη).le (neg_nonneg.2 hψ)]

/-! ### The two ends, as statements about monotone coordinate paths -/

include hM in
/-- **Future end (pure):** along any monotone `(U(t), V(t))` in region I with no limit in region I
at `+∞`, `Θ_ψ → +∞` (campaign 99's argument, `ψ(4M log V) ≥ ψ(4M log V(0))`). -/
theorem sv_future_pure {a η v₀ : ℝ} (ha : 0 < a) (hη : 0 < η) {U V : ℝ → ℝ}
    (hUm : Monotone U) (hVm : Monotone V) (hR : ∀ t, ((U t, V t) : P) ∈ seR)
    (hinext : ¬ ∃ p ∈ seR, Tendsto (fun t => ((U t, V t) : P)) atTop (𝓝 p)) :
    Tendsto (fun t => sv_QP M a η v₀ (U t, V t)) atTop atTop := by
  have hUneg : ∀ t, U t < 0 := fun t => (hR t).1
  have hVpos : ∀ t, 0 < V t := fun t => (hR t).2
  have hkM : ∀ t, ((U t, V t) : P) ∈ sk_kM := fun t => sr_seR_kM (hR t)
  have hrpos : ∀ t, 0 < rK M (U t, V t) := fun t => (sk_rK_spec hM (hkM t)).1
  have hQ : ∀ t, sv_QP M a η v₀ (U t, V t) =
      a * (-(4 * M) * Real.log (-U t) + η * rK M (U t, V t)) +
        a * η * sv_ψ v₀ (4 * M * Real.log (V t)) := fun t => rfl
  set c₀ := a * η * sv_ψ v₀ (4 * M * Real.log (V 0)) with hc₀
  have hψ : ∀ t, 0 ≤ t → c₀ ≤ a * η * sv_ψ v₀ (4 * M * Real.log (V t)) := fun t ht => by
    have h1 : 4 * M * Real.log (V 0) ≤ 4 * M * Real.log (V t) :=
      mul_le_mul_of_nonneg_left (Real.log_le_log (hVpos 0) (hVm ht)) (by positivity)
    exact mul_le_mul_of_nonneg_left (sv_ψ_mono v₀ h1) (mul_pos ha hη).le
  have hUbdd : BddAbove (range U) := ⟨0, by rintro _ ⟨t, rfl⟩; exact (hUneg t).le⟩
  set LU := ⨆ t, U t with hLUdef
  have hLU : Tendsto U atTop (𝓝 LU) := tendsto_atTop_ciSup hUm hUbdd
  have hLU0 : LU ≤ 0 := ciSup_le fun t => (hUneg t).le
  have hUle : ∀ t, U t ≤ LU := fun t => le_ciSup hUbdd t
  rcases hLU0.lt_or_eq with hLUn | hLU0'
  · by_cases hVb : BddAbove (range V)
    · exfalso
      have hLV : Tendsto V atTop (𝓝 (⨆ t, V t)) := tendsto_atTop_ciSup hVm hVb
      have hLVpos : 0 < ⨆ t, V t := lt_of_lt_of_le (hVpos 0) (le_ciSup hVb 0)
      exact hinext ⟨(LU, ⨆ t, V t), ⟨hLUn, hLVpos⟩, hLU.prodMk_nhds hLV⟩
    · have hVt : Tendsto V atTop atTop := tendsto_atTop_atTop_of_monotone hVm fun b => by
        by_contra h; push Not at h
        exact hVb ⟨b, by rintro _ ⟨t, rfl⟩; exact (h t).le⟩
      have hr : Tendsto (fun t => rK M (U t, V t)) atTop atTop := by
        rw [Filter.tendsto_atTop]
        intro R
        set R' := max R 1
        have hR' : 0 < R' := lt_of_lt_of_le one_pos (le_max_right _ _)
        have h1 : Tendsto (fun t => (-LU) * V t) atTop atTop :=
          hVt.const_mul_atTop (neg_pos.2 hLUn)
        filter_upwards [h1.eventually_gt_atTop (hK M R')] with t ht
        have hh : hK M (rK M (U t, V t)) = -(U t * V t) := (sk_rK_spec hM (hkM t)).2
        have hkey : hK M R' < hK M (rK M (U t, V t)) := by
          rw [hh]; nlinarith [hUle t, hVpos t]
        by_contra hlt; push Not at hlt
        have hle : rK M (U t, V t) ≤ R' := le_trans hlt.le (le_max_left R 1)
        have := (hK_strictMonoOn hM).monotoneOn (mem_Ici.2 (hrpos t).le) (mem_Ici.2 hR'.le) hle
        linarith
      have hlow : ∀ᶠ t in atTop, a * (-(4 * M) * Real.log (-U 0)) + c₀ +
          (a * η) * rK M (U t, V t) ≤ sv_QP M a η v₀ (U t, V t) := by
        filter_upwards [eventually_ge_atTop 0] with t ht0
        have hlog : Real.log (-U t) ≤ Real.log (-U 0) :=
          Real.log_le_log (neg_pos.2 (hUneg t)) (by linarith [hUm ht0])
        rw [hQ t]
        nlinarith [mul_nonneg (mul_pos ha hM).le (sub_nonneg.2 hlog), hψ t ht0]
      exact tendsto_atTop_mono' atTop hlow
        (tendsto_atTop_add_const_left _ _ (hr.const_mul_atTop (mul_pos ha hη)))
  · rw [hLU0'] at hLU
    have hneg : Tendsto (fun t => -U t) atTop (𝓝[>] 0) := by
      refine tendsto_nhdsWithin_iff.2 ⟨?_, Eventually.of_forall fun t => neg_pos.2 (hUneg t)⟩
      simpa using hLU.neg
    have hlog : Tendsto (fun t => -Real.log (-U t)) atTop atTop :=
      tendsto_neg_atBot_atTop.comp (Real.tendsto_log_nhdsGT_zero.comp hneg)
    have hlow : ∀ᶠ t in atTop, (a * (4 * M)) * (-Real.log (-U t)) + c₀ ≤
        sv_QP M a η v₀ (U t, V t) := by
      filter_upwards [eventually_ge_atTop 0] with t ht0
      rw [hQ t]; nlinarith [mul_pos ha (mul_pos hη (hrpos t)), hψ t ht0]
    exact tendsto_atTop_mono' atTop hlow
      (tendsto_atTop_add_const_right _ _ (hlog.const_mul_atTop (mul_pos ha (by positivity))))

include hM in
/-- **Past end (pure), the new part:** along any monotone `(U(t), V(t))` in region I with no limit
in region I at `−∞`, `Θ_ψ → −∞`, for `0 < η ≤ 2`. Either `V → 0`, where `log V → −∞` drives
both regimes (`r < 4M`: `ψ(v) ≤ v − v₀ + 1`; `r ≥ 4M`: the exact identity, `(η/2 − 1) ≤ 0`); or
`V → V_∞ > 0` and `U → −∞`, where `r → ∞` and the exact identity gives
`Θ_ψ ≤ C − 2Mηa log(r/2M − 1) → −∞` (this covers `η = 2`). -/
theorem sv_past_pure {a η v₀ : ℝ} (ha : 0 < a) (hη : 0 < η) (hη2 : η ≤ 2) {U V : ℝ → ℝ}
    (hUm : Monotone U) (hVm : Monotone V) (hR : ∀ t, ((U t, V t) : P) ∈ seR)
    (hinext : ¬ ∃ p ∈ seR, Tendsto (fun t => ((U t, V t) : P)) atBot (𝓝 p)) :
    Tendsto (fun t => sv_QP M a η v₀ (U t, V t)) atBot atBot := by
  have hUneg : ∀ t, U t < 0 := fun t => (hR t).1
  have hVpos : ∀ t, 0 < V t := fun t => (hR t).2
  have hkM : ∀ t, ((U t, V t) : P) ∈ sk_kM := fun t => sr_seR_kM (hR t)
  have hrpos : ∀ t, 0 < rK M (U t, V t) := fun t => (sk_rK_spec hM (hkM t)).1
  have hQ : ∀ t, sv_QP M a η v₀ (U t, V t) =
      a * (-(4 * M) * Real.log (-U t) + η * rK M (U t, V t)) +
        a * η * sv_ψ v₀ (4 * M * Real.log (V t)) := fun t => rfl
  set L₀ := Real.log (-U 0) with hL₀
  have hLU : ∀ t, t ≤ 0 → L₀ ≤ Real.log (-U t) := fun t ht =>
    Real.log_le_log (neg_pos.2 (hUneg 0)) (by linarith [hUm ht])
  have hLV : ∀ t, t ≤ 0 → Real.log (V t) ≤ Real.log (V 0) := fun t ht =>
    Real.log_le_log (hVpos t) (hVm ht)
  have hVbdd : BddBelow (range V) := ⟨0, by rintro _ ⟨t, rfl⟩; exact (hVpos t).le⟩
  set LV := ⨅ t, V t with hLVdef
  have hVlim : Tendsto V atBot (𝓝 LV) := tendsto_atBot_ciInf hVm hVbdd
  have hLV0 : 0 ≤ LV := le_ciInf fun t => (hVpos t).le
  have hVge : ∀ t, LV ≤ V t := fun t => ciInf_le hVbdd t
  have h2Mη : 2 * M * η - 4 * M ≤ 0 := by nlinarith
  rcases hLV0.lt_or_eq with hLVpos | hLV0'
  · -- `V → V_∞ > 0`
    by_cases hUb : BddBelow (range U)
    · exfalso
      have hUlim : Tendsto U atBot (𝓝 (⨅ t, U t)) := tendsto_atBot_ciInf hUm hUb
      have hneg : (⨅ t, U t) < 0 := lt_of_le_of_lt (ciInf_le hUb 0) (hUneg 0)
      exact hinext ⟨(⨅ t, U t, LV), ⟨hneg, hLVpos⟩, hUlim.prodMk_nhds hVlim⟩
    · have hUt : Tendsto U atBot atBot := tendsto_atBot_atBot_of_monotone hUm fun b => by
        by_contra h; push Not at h
        exact hUb ⟨b, by rintro _ ⟨t, rfl⟩; exact (h t).le⟩
      have hr : Tendsto (fun t => rK M (U t, V t)) atBot atTop := by
        rw [Filter.tendsto_atTop]
        intro R
        set R' := max R 1
        have hR' : 0 < R' := lt_of_lt_of_le one_pos (le_max_right _ _)
        have h1 : Tendsto (fun t => LV * (-U t)) atBot atTop :=
          (tendsto_neg_atBot_atTop.comp hUt).const_mul_atTop hLVpos
        filter_upwards [h1.eventually_gt_atTop (hK M R')] with t ht
        have hh : hK M (rK M (U t, V t)) = -(U t * V t) := (sk_rK_spec hM (hkM t)).2
        have hkey : hK M R' < hK M (rK M (U t, V t)) := by
          rw [hh]
          have : LV * (-U t) ≤ V t * (-U t) :=
            mul_le_mul_of_nonneg_right (hVge t) (neg_pos.2 (hUneg t)).le

          nlinarith
        by_contra hlt; push Not at hlt
        have hle : rK M (U t, V t) ≤ R' := le_trans hlt.le (le_max_left R 1)
        have := (hK_strictMonoOn hM).monotoneOn (mem_Ici.2 (hrpos t).le) (mem_Ici.2 hR'.le) hle
        linarith
      have hq : Tendsto (fun t => Real.log (rK M (U t, V t) / (2 * M) - 1)) atBot atTop := by
        refine Real.tendsto_log_atTop.comp ?_
        exact tendsto_atTop_add_const_right _ _ (hr.atTop_div_const (by positivity))
      set C := a * ((2 * M * η - 4 * M) * L₀ + 2 * M * η * Real.log (V 0)) with hC
      have hup : ∀ᶠ t in atBot, sv_QP M a η v₀ (U t, V t) ≤
          C + (-(a * (2 * M * η))) * Real.log (rK M (U t, V t) / (2 * M) - 1) := by
        filter_upwards [eventually_le_atBot 0] with t ht
        have h1 := sv_Q_le_far hM (v₀ := v₀) ha hη (hR t)
        have h3 : (2 * M * η - 4 * M) * Real.log (-U t) ≤ (2 * M * η - 4 * M) * L₀ :=
          mul_le_mul_of_nonpos_left (hLU t ht) h2Mη
        have h4 : 2 * M * η * Real.log (V t) ≤ 2 * M * η * Real.log (V 0) :=
          mul_le_mul_of_nonneg_left (hLV t ht) (by positivity)

        rw [hC]
        nlinarith
      exact tendsto_atBot_mono' atBot hup (tendsto_atBot_add_const_left _ _
        (hq.const_mul_atTop_of_neg (by have := mul_pos ha (mul_pos hM hη); linarith)))
  · -- `V → 0`: `log V → −∞`
    rw [← hLV0'] at hVlim
    have hV0 : Tendsto V atBot (𝓝[>] 0) :=
      tendsto_nhdsWithin_iff.2 ⟨hVlim, Eventually.of_forall hVpos⟩
    have hℓ : Tendsto (fun t => Real.log (V t)) atBot atBot :=
      Real.tendsto_log_nhdsGT_zero.comp hV0
    set C := max (-(4 * M) * L₀ + 4 * M * η + η * (1 - v₀)) ((2 * M * η - 4 * M) * L₀) with hC
    have hup : ∀ᶠ t in atBot, sv_QP M a η v₀ (U t, V t) ≤
        a * C + (a * (2 * M * η)) * Real.log (V t) := by
      filter_upwards [eventually_le_atBot 0, hℓ.eventually_le_atBot 0] with t ht hℓt
      have hC1 := le_max_left (-(4 * M) * L₀ + 4 * M * η + η * (1 - v₀))
        ((2 * M * η - 4 * M) * L₀)
      have hC2 := le_max_right (-(4 * M) * L₀ + 4 * M * η + η * (1 - v₀))
        ((2 * M * η - 4 * M) * L₀)
      rw [← hC] at hC1 hC2
      rcases lt_or_ge (rK M (U t, V t)) (4 * M) with hr4 | hr4
      · have hψ := sv_ψ_le v₀ (4 * M * Real.log (V t))
        have hL := hLU t ht
        rw [hQ t]
        have e1 : -(4 * M) * Real.log (-U t) ≤ -(4 * M) * L₀ := by nlinarith
        have e2 : η * rK M (U t, V t) ≤ 4 * M * η := by nlinarith
        have e3 : η * sv_ψ v₀ (4 * M * Real.log (V t)) ≤
            η * (4 * M * Real.log (V t) - v₀ + 1) := mul_le_mul_of_nonneg_left hψ hη.le
        have e4 : η * (4 * M * Real.log (V t)) ≤ 2 * M * η * Real.log (V t) := by
          nlinarith [mul_pos hM hη]
        have : -(4 * M) * Real.log (-U t) + η * rK M (U t, V t) +
            η * sv_ψ v₀ (4 * M * Real.log (V t)) ≤ C + 2 * M * η * Real.log (V t) := by
          nlinarith
        nlinarith
      · have h1 := sv_Q_le_far hM (v₀ := v₀) ha hη (hR t)
        have hq1 : 1 ≤ rK M (U t, V t) / (2 * M) - 1 := by
          rw [le_sub_iff_add_le, le_div_iff₀ (by positivity)]; linarith
        have hlq : 0 ≤ Real.log (rK M (U t, V t) / (2 * M) - 1) := Real.log_nonneg hq1
        have h3 : (2 * M * η - 4 * M) * Real.log (-U t) ≤ (2 * M * η - 4 * M) * L₀ :=
          mul_le_mul_of_nonpos_left (hLU t ht) h2Mη
        have : (2 * M * η - 4 * M) * Real.log (-U t) + 2 * M * η * Real.log (V t) -
            2 * M * η * Real.log (rK M (U t, V t) / (2 * M) - 1) ≤
              C + 2 * M * η * Real.log (V t) := by
          nlinarith [mul_nonneg (mul_pos hM hη).le hlq]

        nlinarith
    exact tendsto_atBot_mono' atBot hup
      (tendsto_atBot_add_const_left _ _ (hℓ.const_mul_atBot (by positivity)))

/-! ### ⓐ The eternal statement on campaign 99's region I -/

include hM in
/-- `U`, `V` are non-decreasing on **all of `ℝ`** along every causal curve of `W`. -/
lemma sv_coord_mono {U : Set seW} (c : (se_S hM).InextCausalCurveIn U) (φ : P →L[ℝ] ℝ)
    (hφ : ∀ v : P, 0 ≤ v.1 → 0 ≤ v.2 → 0 ≤ φ v) :
    Monotone (fun t => φ (c.γ t : P)) := by
  refine sv_monotone_of_brk c.brk_fin
    (φ.continuous.comp (continuous_subtype_val.comp c.cont)) fun t ht => ?_
  obtain ⟨hd, hfc⟩ := c.causal t ht
  have h : HasDerivAt (fun s => φ (c.γ s : P)) (φ (MSpacetime.vel c.γ t)) t :=
    φ.hasFDerivAt.comp_hasDerivAt t (sr_hasDerivAt hd)
  obtain ⟨h1, h2, -⟩ := (sr_futCausal_iff hM _ _).1 hfc
  exact ⟨h.differentiableAt, by rw [h.deriv]; exact hφ _ h1 h2⟩

/-- **`Θ_ψ` is temporal on region I for `0 < η ≤ 2` (BUILT):** `sr_temporal`'s `Θ_U, Θ_V > 0`, plus
the non-negative `aη ψ′ (4M/V) dV`. -/
theorem sv_eternal_temporal {r₀ : ℝ} (hr₀ : 2 * M < r₀) {a η : ℝ} (ha : 0 < a) (hη : 0 < η)
    (hη2 : η ≤ 2) (v₀ : ℝ) :
    (se_S hM).IsTemporalOn ((se_S hM).D (range (se_Ost hM hr₀))) (sv_Θψ M a η v₀) := by
  rw [sr_D_eq hM hr₀, sv_Θψ_eq]
  refine ⟨(sr_contMDiffOn seR_open (sv_QP_contDiffOn hM a η v₀)).mono fun x hx => ⟨hx, x.2.1⟩,
    fun x hx v hv => ?_⟩
  have hxR : x.1 ∈ seR := ⟨hx, x.2.1⟩
  rw [sr_dfun (sv_QP_hasFDerivAt hM a η v₀ hxR), sr_split]
  obtain ⟨h1, h2, h3⟩ := (sr_futCausal_iff hM x v).1 hv
  obtain ⟨hA, hB⟩ := sv_QD_pos hM v₀ ha hη hη2 hxR
  exact sr_pos_of_causal hA hB h1 h2 h3

lemma sv_D_open {r₀ : ℝ} (hr₀ : 2 * M < r₀) :
    IsOpen ((se_S hM).D (range (se_Ost hM hr₀))) := by
  rw [sr_D_eq hM hr₀]
  exact isOpen_lt (continuous_fst.comp continuous_subtype_val) continuous_const

lemma sv_curve_R {r₀ : ℝ} (hr₀ : 2 * M < r₀)
    (c : (se_S hM).InextCausalCurveIn ((se_S hM).D (range (se_Ost hM hr₀)))) (t : ℝ) :
    (((c.γ t : P).1, (c.γ t : P).2) : P) ∈ seR :=
  ⟨(Set.ext_iff.1 (sr_D_eq hM hr₀) (c.γ t)).1 (c.mem t), (c.γ t).2.1⟩

/-- **ⓐ The core lemma (BUILT): `Θ_ψ` is a Cauchy temporal function of region I `D` for
`0 < η ≤ 2`**, `Θ_ψ = a(−4M log(−U) + η r) + aη ψ(4M log V)`. Temporality is
`sv_eternal_temporal`; along every inextendible causal curve `U`, `V` are monotone on `ℝ`, so
`Θ_ψ → +∞` at the future end (`sv_future_pure`) and `Θ_ψ → −∞` at the past end
(`sv_past_pure`, the exact identity at `η = 2`); then `sv_cauchy_of_limits`. -/
theorem sv_eternal_cauchy {r₀ : ℝ} (hr₀ : 2 * M < r₀) {a η : ℝ} (ha : 0 < a) (hη : 0 < η)
    (hη2 : η ≤ 2) (v₀ : ℝ) :
    (se_S hM).IsCauchyTemporalOn ((se_S hM).D (range (se_Ost hM hr₀))) (sv_Θψ M a η v₀) := by
  refine MSpacetime.sv_cauchy_of_limits (sv_D_open hM hr₀)
    (sv_eternal_temporal hM hr₀ ha hη hη2 v₀) (fun c => ?_) (fun c => ?_)
  · have hU := sv_coord_mono hM c (fst ℝ ℝ ℝ) fun v h1 _ => h1
    have hV := sv_coord_mono hM c (snd ℝ ℝ ℝ) fun v _ h2 => h2
    rw [sv_Θψ_eq]
    refine sv_future_pure hM (v₀ := v₀) ha hη (U := fun t => (c.γ t : P).1)
      (V := fun t => (c.γ t : P).2) hU hV (sv_curve_R hM hr₀ c) ?_
    rintro ⟨p, hp, hlim⟩
    refine c.inext_future ⟨⟨p, seR_subset_WS hp⟩, ?_, ?_⟩
    · rw [sr_D_eq hM hr₀]; exact hp.1
    · rw [tendsto_subtype_rng]; exact hlim
  · have hU := sv_coord_mono hM c (fst ℝ ℝ ℝ) fun v h1 _ => h1
    have hV := sv_coord_mono hM c (snd ℝ ℝ ℝ) fun v _ h2 => h2
    rw [sv_Θψ_eq]
    refine sv_past_pure hM (v₀ := v₀) ha hη hη2 (U := fun t => (c.γ t : P).1)
      (V := fun t => (c.γ t : P).2) hU hV (sv_curve_R hM hr₀ c) ?_
    rintro ⟨p, hp, hlim⟩
    refine c.inext_past ⟨⟨p, seR_subset_WS hp⟩, ?_, ?_⟩
    · rw [sr_D_eq hM hr₀]; exact hp.1
    · rw [tendsto_subtype_rng]; exact hlim

/-! ### ⓑ The thin ingoing null shell: flat for `v ≤ v₀`, Schwarzschild for `v ≥ v₀` -/

/-- The flat retarded coordinate of the future horizon, `u_H = v₀ − 4M`. -/
noncomputable def sv_uH (M v₀ : ℝ) : ℝ := v₀ - 4 * M

/-- `M = {ũ < u_H}` in the plane `(ũ, v)`. -/
def sv_MS (M v₀ : ℝ) : Set P := {y | y.1 < sv_uH M v₀}

lemma sv_MS_open (M v₀ : ℝ) : IsOpen (sv_MS M v₀) := isOpen_lt continuous_fst continuous_const

/-- **The retarded time of the vacuum region**, `u = F(ũ) = ũ − 4M log((v₀ − ũ)/4M − 1)`. -/
noncomputable def sv_F (M v₀ ũ : ℝ) : ℝ := ũ - 4 * M * Real.log ((v₀ - ũ) / (4 * M) - 1)

/-- `F′(ũ) = 1 + 4M/(u_H − ũ)`. -/
noncomputable def sv_F' (M v₀ ũ : ℝ) : ℝ := 1 + 4 * M / (sv_uH M v₀ - ũ)

/-- Kruskal's `U` along the shell plane, `U(ũ) = −((v₀ − ũ)/4M − 1) e^{−ũ/4M}` (smooth on `ℝ`; it
equals `−e^{−F(ũ)/4M}` on `ũ < u_H`, `sv_χU_eq`). -/
noncomputable def sv_χU (M v₀ ũ : ℝ) : ℝ := -(((v₀ - ũ) / (4 * M) - 1) * Real.exp (-ũ / (4 * M)))

/-- Kruskal's `V = e^{v/4M}`. -/
noncomputable def sv_χV (M v : ℝ) : ℝ := Real.exp (v / (4 * M))

/-- **`χ(ũ, v) = (−e^{−F(ũ)/4M}, e^{v/4M})`**, from `M` onto region I. -/
noncomputable def sv_χ (M v₀ : ℝ) (y : P) : P := (sv_χU M v₀ y.1, sv_χV M y.2)

include hM in
lemma sv_q_pos {v₀ ũ : ℝ} (h : ũ < sv_uH M v₀) : 0 < (v₀ - ũ) / (4 * M) - 1 := by
  unfold sv_uH at h
  rw [sub_pos, one_lt_div (by positivity)]; linarith

include hM in
lemma sv_χU_eq {v₀ ũ : ℝ} (h : ũ < sv_uH M v₀) :
    sv_χU M v₀ ũ = -Real.exp (-sv_F M v₀ ũ / (4 * M)) := by
  have hq := sv_q_pos hM h
  have hM' : M ≠ 0 := hM.ne'
  unfold sv_χU sv_F
  have e : -(ũ - 4 * M * Real.log ((v₀ - ũ) / (4 * M) - 1)) / (4 * M) =
      Real.log ((v₀ - ũ) / (4 * M) - 1) + -ũ / (4 * M) := by field_simp; ring
  rw [e, Real.exp_add, Real.exp_log hq]

include hM in
lemma sv_χU_neg {v₀ ũ : ℝ} (h : ũ < sv_uH M v₀) : sv_χU M v₀ ũ < 0 := by
  rw [sv_χU_eq hM h]; exact neg_neg_of_pos (Real.exp_pos _)

include hM in
lemma sv_χU_uH (v₀ : ℝ) : sv_χU M v₀ (sv_uH M v₀) = 0 := by
  have hM' : M ≠ 0 := hM.ne'
  unfold sv_χU sv_uH
  have : (v₀ - (v₀ - 4 * M)) / (4 * M) - 1 = 0 := by field_simp; ring
  rw [this, zero_mul, neg_zero]

lemma sv_χV_pos (M v : ℝ) : 0 < sv_χV M v := Real.exp_pos _

include hM in
lemma sv_log_χV (v : ℝ) : 4 * M * Real.log (sv_χV M v) = v := by
  have hM' : M ≠ 0 := hM.ne'
  unfold sv_χV; rw [Real.log_exp]; field_simp

include hM in
/-- `−4M log(−U(ũ)) = F(ũ)`: the retarded time of `χ(ũ, v)` is `u = F(ũ)`. -/
lemma sv_F_eq {v₀ ũ : ℝ} (h : ũ < sv_uH M v₀) :
    -(4 * M) * Real.log (-sv_χU M v₀ ũ) = sv_F M v₀ ũ := by
  have hM' : M ≠ 0 := hM.ne'
  rw [sv_χU_eq hM h, neg_neg, Real.log_exp]; field_simp

include hM in
lemma sv_χ_mem {v₀ : ℝ} {y : P} (hy : y ∈ sv_MS M v₀) : sv_χ M v₀ y ∈ seR :=
  ⟨sv_χU_neg hM hy, sv_χV_pos M y.2⟩

/-- `U′(ũ) = e^{−ũ/4M} (v₀ − ũ)/16M²`. -/
noncomputable def sv_χU' (M v₀ ũ : ℝ) : ℝ := Real.exp (-ũ / (4 * M)) * (v₀ - ũ) / (16 * M ^ 2)

include hM in
lemma sv_χU_hasDerivAt (v₀ ũ : ℝ) : HasDerivAt (sv_χU M v₀) (sv_χU' M v₀ ũ) ũ := by
  have hM' : M ≠ 0 := hM.ne'
  have h1 : HasDerivAt (fun x : ℝ => (v₀ - x) / (4 * M) - 1) (-1 / (4 * M)) ũ :=
    (((hasDerivAt_id' ũ).const_sub v₀).div_const (4 * M)).sub_const 1
  have h2 : HasDerivAt (fun x : ℝ => Real.exp (-x / (4 * M)))
      (Real.exp (-ũ / (4 * M)) * (-1 / (4 * M))) ũ :=
    ((hasDerivAt_neg ũ).div_const (4 * M)).exp
  have h : HasDerivAt (sv_χU M v₀) _ ũ := (h1.mul h2).neg
  refine h.congr_deriv ?_
  unfold sv_χU'
  field_simp; ring

include hM in
lemma sv_χU'_pos {v₀ ũ : ℝ} (h : ũ < v₀) : 0 < sv_χU' M v₀ ũ := by
  unfold sv_χU'
  have : 0 < v₀ - ũ := by linarith
  positivity

lemma sv_χV_hasDerivAt (M v : ℝ) : HasDerivAt (sv_χV M) (sv_χV M v / (4 * M)) v := by
  have h : HasDerivAt (sv_χV M) _ v := ((hasDerivAt_id' v).div_const (4 * M)).exp
  refine h.congr_deriv ?_
  unfold sv_χV; ring

lemma sv_χU_continuous (M v₀ : ℝ) : Continuous (sv_χU M v₀) := by
  unfold sv_χU; fun_prop

include hM in
lemma sv_χU_strictMonoOn (v₀ : ℝ) : StrictMonoOn (sv_χU M v₀) (Iio v₀) := by
  refine strictMonoOn_of_deriv_pos (convex_Iio v₀) (sv_χU_continuous M v₀).continuousOn
    fun x hx => ?_
  rw [interior_Iio] at hx
  rw [(sv_χU_hasDerivAt hM v₀ x).deriv]; exact sv_χU'_pos hM hx

include hM in
lemma sv_χU_tendsto (v₀ : ℝ) : Tendsto (sv_χU M v₀) atBot atBot := by
  refine tendsto_atBot_atBot.2 fun b =>
    ⟨min (min 0 (v₀ - 8 * M)) (4 * M * (b - 1) + v₀), fun x hx => ?_⟩
  have hx0 : x ≤ 0 := le_trans hx (le_trans (min_le_left _ _) (min_le_left _ _))
  have hx1 : x ≤ v₀ - 8 * M := le_trans hx (le_trans (min_le_left _ _) (min_le_right _ _))
  have hx2 : x ≤ 4 * M * (b - 1) + v₀ := le_trans hx (min_le_right _ _)
  have he : 1 ≤ Real.exp (-x / (4 * M)) :=
    Real.one_le_exp (div_nonneg (by linarith) (by positivity))
  have hq : 1 ≤ (v₀ - x) / (4 * M) - 1 := by
    rw [le_sub_iff_add_le, le_div_iff₀ (by positivity)]; linarith
  have hqb : -(b - 1) ≤ (v₀ - x) / (4 * M) := by
    rw [le_div_iff₀ (by positivity)]; linarith
  unfold sv_χU
  nlinarith

lemma sv_χ_contDiff (M v₀ : ℝ) : ContDiff ℝ 1 (sv_χ M v₀) := by
  unfold sv_χ sv_χU sv_χV
  fun_prop

/-- `Dχ = diag(U′(ũ), V/4M)`. -/
noncomputable def sv_Dχ (M v₀ : ℝ) (y : P) : P →L[ℝ] P :=
  (sv_χU' M v₀ y.1 • fst ℝ ℝ ℝ).prod ((sv_χV M y.2 / (4 * M)) • snd ℝ ℝ ℝ)

include hM in
lemma sv_χ_hasFDerivAt (v₀ : ℝ) (y : P) : HasFDerivAt (sv_χ M v₀) (sv_Dχ M v₀ y) y :=
  ((sv_χU_hasDerivAt hM v₀ y.1).comp_hasFDerivAt y hasFDerivAt_fst).prodMk
    ((sv_χV_hasDerivAt M y.2).comp_hasFDerivAt y hasFDerivAt_snd)

lemma sv_Dχ_apply (M v₀ : ℝ) (y w : P) :
    sv_Dχ M v₀ y w = (sv_χU' M v₀ y.1 * w.1, sv_χV M y.2 / (4 * M) * w.2) := by
  simp [sv_Dχ]

/-! #### The spacetime -/

/-- **The flat plane with `M = {ũ < u_H}`**: `g = −dũ dv`, `T = (1, 1)` (campaign 90's `cz_St`
restricted). -/
noncomputable def sv_flat (M v₀ : ℝ) : MSpacetime P P :=
  NModel.cz_St.restrictM (sv_MS M v₀) (sv_MS_open M v₀) (subset_univ _)

/-- **The vacuum radial function**, `r(ũ, v) = r_S(χ(ũ, v))`: Schwarzschild's `r` at `(u, v) = (F(ũ), v)`, continued
over the whole model. It is the areal radius only on the vacuum side `v ≥ v₀` (`sv_vacuum`). On `v < v₀` it is the
vacuum continuation, not the flat interior's radius. -/
noncomputable def sv_r (M v₀ : ℝ) (y : P) : ℝ := rK M (sv_χ M v₀ y)

/-- **The conformal factor** `Φ(ũ, v) = (1 − 2M/r(ũ, max(v, v₀))) F′(ũ)` on `M` (`1` off `M`). A
single formula: it is `1` for `v ≤ v₀` (`sv_flat_past`) and `f(r) F′(ũ)` for `v ≥ v₀`
(`sv_vacuum`). -/
noncomputable def sv_Φ (M v₀ : ℝ) (y : P) : ℝ :=
  if y.1 < sv_uH M v₀ then (1 - 2 * M / sv_r M v₀ (y.1, max y.2 v₀)) * sv_F' M v₀ y.1 else 1

include hM in
lemma sv_r_gt {v₀ : ℝ} {y : P} (hy : y ∈ sv_MS M v₀) : 2 * M < sv_r M v₀ y := by
  have := sr_q_pos hM (sv_χ_mem hM hy)
  have h2 : 0 < 2 * M := by positivity
  unfold sv_r
  rw [sub_pos, one_lt_div h2] at this; exact this

include hM in
lemma sv_F'_pos {v₀ ũ : ℝ} (h : ũ < sv_uH M v₀) : 0 < sv_F' M v₀ ũ := by
  unfold sv_F'
  have : 0 < sv_uH M v₀ - ũ := by linarith
  positivity

include hM in
lemma sv_Φ_pos (v₀ : ℝ) (y : P) : 0 < sv_Φ M v₀ y := by
  unfold sv_Φ
  split_ifs with h
  · have hr := sv_r_gt hM (v₀ := v₀) (y := (y.1, max y.2 v₀)) h
    have : 0 < 1 - 2 * M / sv_r M v₀ (y.1, max y.2 v₀) := by
      rw [sub_pos, div_lt_one (by linarith)]; exact hr
    exact mul_pos this (sv_F'_pos hM h)
  · exact one_pos

/-- **The thin-shell spacetime** `sv_S`: on `P` with coordinates `(ũ, v)`, `M = {ũ < u_H}`,
`g = −Φ dũ dv`, `T = (1, 1)`; built as `cz_scale` of the flat `sv_flat`. -/
noncomputable def sv_S (v₀ : ℝ) : MSpacetime P P :=
  (sv_flat M v₀).cz_scale (sv_Φ M v₀) (sv_Φ_pos hM v₀)

lemma sv_S_M (v₀ : ℝ) : (sv_S hM v₀).M = sv_MS M v₀ := rfl

/-- **The metric (BUILT):** in the (identity) chart, `g = Φ · (−dũ dv)`. -/
theorem sv_hRep (v₀ : ℝ) (p y : P) : hRep (sv_S hM v₀).g p y = sv_Φ M v₀ y • gM := by
  rw [sv_S, MSpacetime.cz_hRep_scale, NModel.cz_extChart_symm_apply]
  have : hRep (sv_flat M v₀).g p y = gM := by
    have h := NModel.cz_hRep p
    exact congrFun h y
  rw [this]

include hM in
/-- **On the shell, `r = (v₀ − ũ)/2`** (the flat areal radius `(v − ũ)/2` at `v = v₀`). -/
lemma sv_r_shell {v₀ ũ : ℝ} (h : ũ < sv_uH M v₀) : sv_r M v₀ (ũ, v₀) = (v₀ - ũ) / 2 := by
  have hM' : M ≠ 0 := hM.ne'
  have hx : 0 < (v₀ - ũ) / 2 := by unfold sv_uH at h; linarith
  have e : -((sv_χ M v₀ (ũ, v₀)).1 * (sv_χ M v₀ (ũ, v₀)).2) = hK M ((v₀ - ũ) / 2) := by
    show -(sv_χU M v₀ ũ * sv_χV M v₀) = _
    unfold sv_χU sv_χV hK
    have e1 : Real.exp ((v₀ - ũ) / 2 / (2 * M)) =
        Real.exp (-ũ / (4 * M)) * Real.exp (v₀ / (4 * M)) := by
      rw [← Real.exp_add]; congr 1; field_simp; ring
    have e2 : (v₀ - ũ) / 2 / (2 * M) - 1 = (v₀ - ũ) / (4 * M) - 1 := by field_simp; ring
    rw [e1, e2]; ring
  show rinv M (-((sv_χ M v₀ (ũ, v₀)).1 * (sv_χ M v₀ (ũ, v₀)).2)) = _
  rw [e, rinv_hK hM hx]

include hM in
/-- **`sv_flat_past` (BUILT): `Φ = 1` for `v ≤ v₀`**, the flat past (`f(r) F′ = 1` on the shell). -/
theorem sv_flat_past {v₀ : ℝ} {y : P} (hy : y ∈ sv_MS M v₀) (hv : y.2 ≤ v₀) :
    sv_Φ M v₀ y = 1 := by
  have hy' : y.1 < sv_uH M v₀ := hy
  unfold sv_Φ
  rw [ite_eq_left_of_eq_true _ _ (eq_true hy'), max_eq_right hv, sv_r_shell hM hy']
  unfold sv_F'
  unfold sv_uH at hy' ⊢
  have h1 : v₀ - 4 * M - y.1 ≠ 0 := by linarith
  have h2 : v₀ - y.1 ≠ 0 := by linarith
  have e1 : 1 - 2 * M / ((v₀ - y.1) / 2) = (v₀ - 4 * M - y.1) / (v₀ - y.1) := by
    field_simp; ring
  have e2 : 1 + 4 * M / (v₀ - 4 * M - y.1) = (v₀ - y.1) / (v₀ - 4 * M - y.1) := by
    field_simp; ring
  rw [e1, e2]
  field_simp

include hM in
lemma sv_F_hasDerivAt {v₀ ũ : ℝ} (h : ũ < sv_uH M v₀) :
    HasDerivAt (sv_F M v₀) (sv_F' M v₀ ũ) ũ := by
  have hq := sv_q_pos hM h
  have hM' : M ≠ 0 := hM.ne'
  have h1 : HasDerivAt (fun x : ℝ => (v₀ - x) / (4 * M) - 1) (-1 / (4 * M)) ũ :=
    (((hasDerivAt_id' ũ).const_sub v₀).div_const (4 * M)).sub_const 1
  have h2 : HasDerivAt (sv_F M v₀) _ ũ :=
    (hasDerivAt_id' ũ).sub ((h1.log hq.ne').const_mul (4 * M))
  refine h2.congr_deriv ?_
  have hu : sv_uH M v₀ - ũ ≠ 0 := by linarith
  have e : (v₀ - ũ) / (4 * M) - 1 = (sv_uH M v₀ - ũ) / (4 * M) := by
    unfold sv_uH; field_simp; ring
  rw [e]
  unfold sv_F'
  field_simp
  ring

include hM in
/-- **`sv_vacuum` (BUILT): for `v ≥ v₀` the shell plane is Schwarzschild in null coordinates.**
`Φ = f(r) F′(ũ)` with `f = 1 − 2M/r`; `F′` is the derivative of `u = F(ũ)`, so
`Φ dũ dv = f(r) du dv`; and `r` is Schwarzschild's areal radius at `(u, v) = (F(ũ), v)`:
`h(r) = (r/2M − 1) e^{r/2M} = e^{(v − u)/4M}`. -/
theorem sv_vacuum {v₀ : ℝ} {y : P} (hy : y ∈ sv_MS M v₀) (hv : v₀ ≤ y.2) :
    sv_Φ M v₀ y = (1 - 2 * M / sv_r M v₀ y) * sv_F' M v₀ y.1 ∧
    HasDerivAt (sv_F M v₀) (sv_F' M v₀ y.1) y.1 ∧
    hK M (sv_r M v₀ y) = Real.exp ((y.2 - sv_F M v₀ y.1) / (4 * M)) := by
  have hy' : y.1 < sv_uH M v₀ := hy
  refine ⟨?_, sv_F_hasDerivAt hM hy', ?_⟩
  · unfold sv_Φ; rw [ite_eq_left_of_eq_true _ _ (eq_true hy'), max_eq_left hv]
  · have hh := (sk_rK_spec hM (sr_seR_kM (sv_χ_mem hM hy))).2
    unfold sv_r
    rw [hh]
    show -(sv_χU M v₀ y.1 * sv_χV M y.2) = _
    rw [sv_χU_eq hM hy']
    unfold sv_χV
    rw [neg_mul, neg_neg, ← Real.exp_add]
    congr 1; ring

include hM in
/-- **`Φ` is continuous on `M` (BUILT).** -/
theorem sv_Φ_continuousOn (v₀ : ℝ) : ContinuousOn (sv_Φ M v₀) (sv_MS M v₀) := by
  have hχ : Continuous (fun y : P => sv_χ M v₀ (y.1, max y.2 v₀)) := by
    unfold sv_χ sv_χU sv_χV; fun_prop
  have hr : ContinuousOn (fun y : P => sv_r M v₀ (y.1, max y.2 v₀)) (sv_MS M v₀) :=
    (sk_rK_contDiffOn hM).continuousOn.comp hχ.continuousOn fun y hy =>
      sr_seR_kM (sv_χ_mem hM (show (y.1, max y.2 v₀) ∈ sv_MS M v₀ from hy))
  have hf : ContinuousOn (fun y : P => (1 - 2 * M / sv_r M v₀ (y.1, max y.2 v₀)) *
      sv_F' M v₀ y.1) (sv_MS M v₀) := by
    refine (continuousOn_const.sub (continuousOn_const.div hr fun y hy => ?_)).mul ?_
    · exact (lt_trans (by positivity)
        (sv_r_gt hM (show (y.1, max y.2 v₀) ∈ sv_MS M v₀ from hy))).ne'
    · unfold sv_F'
      exact continuousOn_const.add (continuousOn_const.div
        (continuousOn_const.sub continuous_fst.continuousOn) fun y hy => (sub_pos.2 hy).ne')
  exact hf.congr fun y hy => by
    unfold sv_Φ; rw [ite_eq_left_of_eq_true _ _ (eq_true (show y.1 < sv_uH M v₀ from hy))]

include hM in
/-- `r` strictly increases with `v` at fixed `ũ`. -/
lemma sv_r_strictMono {v₀ ũ v v' : ℝ} (h : ũ < sv_uH M v₀) (hv : v < v') :
    sv_r M v₀ (ũ, v) < sv_r M v₀ (ũ, v') := by
  have hU := sv_χU_neg hM h
  have hV : sv_χV M v < sv_χV M v' := Real.exp_lt_exp.2 (div_lt_div_of_pos_right hv (by positivity))
  have hV0 := sv_χV_pos M v
  show rinv M (-(sv_χU M v₀ ũ * sv_χV M v)) < rinv M (-(sv_χU M v₀ ũ * sv_χV M v'))
  refine rinv_strictMonoOn hM ?_ ?_ ?_
  · show -1 < -(sv_χU M v₀ ũ * sv_χV M v); nlinarith
  · show -1 < -(sv_χU M v₀ ũ * sv_χV M v'); nlinarith
  · nlinarith

include hM in
/-- **`Φ > 1` strictly inside the vacuum region `v > v₀`**: so `Φ ≢ 1` and the metric is not
flat there. -/
theorem sv_Φ_gt_one {v₀ : ℝ} {y : P} (hy : y ∈ sv_MS M v₀) (hv : v₀ < y.2) : 1 < sv_Φ M v₀ y := by
  have hy' : y.1 < sv_uH M v₀ := hy
  have h1 := sv_flat_past hM (v₀ := v₀) (y := (y.1, v₀)) hy' le_rfl
  have hr := sv_r_strictMono hM hy' hv
  have hr0 := sv_r_gt hM (v₀ := v₀) (y := (y.1, v₀)) hy'
  have hF := sv_F'_pos hM hy'
  rw [(sv_vacuum hM hy hv.le).1]
  unfold sv_Φ at h1
  rw [ite_eq_left_of_eq_true _ _ (eq_true hy'), max_self] at h1
  have hlt : 2 * M / sv_r M v₀ y < 2 * M / sv_r M v₀ (y.1, v₀) :=
    div_lt_div_of_pos_left (by positivity) (by linarith) hr
  nlinarith

/-! #### The slicing `Θ_shell = Θ_ψ ∘ χ` and its Cauchy property -/

/-- **The shell slicing** `Θ_shell = Θ_ψ ∘ χ`. -/
noncomputable def sv_Θsh (M a η v₀ : ℝ) (y : P) : ℝ := sv_QP M a η v₀ (sv_χ M v₀ y)

include hM in
/-- On `M`: `Θ_shell = a(F(ũ) + η r) + aη ψ(v)`. -/
lemma sv_Θsh_eq {a η v₀ : ℝ} {y : P} (hy : y ∈ sv_MS M v₀) :
    sv_Θsh M a η v₀ y = a * (sv_F M v₀ y.1 + η * sv_r M v₀ y) + a * η * sv_ψ v₀ y.2 := by
  show a * (-(4 * M) * Real.log (-sv_χU M v₀ y.1) + η * rK M (sv_χ M v₀ y)) +
    a * η * sv_ψ v₀ (4 * M * Real.log (sv_χV M y.2)) = _
  rw [sv_F_eq hM hy, sv_log_χV hM]; rfl

include hM in
/-- **`sv_retarded_eq` (BUILT): on the vacuum exterior `v ≥ v₀`, `Θ_shell = a(u + η r)`**, with
`u = F(ũ)` the retarded time and `r` the areal radius. -/
theorem sv_retarded_eq {a η v₀ : ℝ} {y : P} (hy : y ∈ sv_MS M v₀) (hv : v₀ ≤ y.2) :
    sv_Θsh M a η v₀ y = a * (sv_F M v₀ y.1 + η * sv_r M v₀ y) := by
  rw [sv_Θsh_eq hM hy, sv_ψ_eq_zero hv, mul_zero, add_zero]

lemma sv_dfun {f : P → ℝ} {f' : P →L[ℝ] ℝ} {x : P} (hf : HasFDerivAt f f' x) (v : P) :
    MSpacetime.dfun f x v = f' v := by
  show mfderiv 𝓘(ℝ, P) 𝓘(ℝ, ℝ) f x v = f' v
  rw [mfderiv_eq_fderiv, hf.fderiv]; rfl

lemma sv_hasDerivAt {γ : ℝ → P} {t : ℝ} (hγ : MDifferentiableAt 𝓘(ℝ, ℝ) 𝓘(ℝ, P) γ t) :
    HasDerivAt γ (MSpacetime.vel γ t) t := by
  have hd := mdifferentiableAt_iff_differentiableAt.1 hγ
  have e : MSpacetime.vel γ t = deriv γ t := by
    show mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, P) γ t (1 : ℝ) = deriv γ t
    rw [mfderiv_eq_fderiv]; rfl
  rw [e]; exact hd.hasDerivAt

lemma sv_futCausal_iff (M v₀ : ℝ) (x v : P) :
    (sv_flat M v₀).FutCausal x v ↔ 0 ≤ v.1 ∧ 0 ≤ v.2 ∧ 0 < v.1 + v.2 :=
  futCausal_iff x v

/-- `ũ`, `v` are non-decreasing on `ℝ` along every causal curve of the shell plane. -/
lemma sv_coord_mono_P {M v₀ : ℝ} {U : Set P} (c : (sv_flat M v₀).InextCausalCurveIn U)
    (φ : P →L[ℝ] ℝ) (hφ : ∀ v : P, 0 ≤ v.1 → 0 ≤ v.2 → 0 ≤ φ v) :
    Monotone (fun t => φ (c.γ t)) := by
  refine sv_monotone_of_brk c.brk_fin (φ.continuous.comp c.cont) fun t ht => ?_
  obtain ⟨hd, hfc⟩ := c.causal t ht
  have h : HasDerivAt (fun s => φ (c.γ s)) (φ (MSpacetime.vel c.γ t)) t :=
    φ.hasFDerivAt.comp_hasDerivAt t (sv_hasDerivAt hd)
  obtain ⟨h1, h2, -⟩ := (sv_futCausal_iff M v₀ _ _).1 hfc
  exact ⟨h.differentiableAt, by rw [h.deriv]; exact hφ _ h1 h2⟩

include hM in
/-- **`Θ_shell` is temporal on `M` (BUILT)**: `dΘ_shell(w) = U′ w_ũ ∂_UΘ_ψ + (V/4M) w_v ∂_VΘ_ψ`,
with `U′, V > 0` and `∂_UΘ_ψ, ∂_VΘ_ψ > 0` (`sv_QD_pos`). -/
theorem sv_temporal {a η v₀ : ℝ} (ha : 0 < a) (hη : 0 < η) (hη2 : η ≤ 2) :
    (sv_flat M v₀).IsTemporalOn (sv_MS M v₀) (sv_Θsh M a η v₀) := by
  refine ⟨?_, fun y hy w hw => ?_⟩
  · rw [contMDiffOn_iff_contDiffOn]
    exact (sv_QP_contDiffOn hM a η v₀).comp (sv_χ_contDiff M v₀).contDiffOn
      fun y hy => sv_χ_mem hM hy
  · have h : HasFDerivAt (sv_Θsh M a η v₀) _ y :=
      (sv_QP_hasFDerivAt hM a η v₀ (sv_χ_mem hM hy)).comp y (sv_χ_hasFDerivAt hM v₀ y)
    rw [sv_dfun h, ContinuousLinearMap.comp_apply, sv_Dχ_apply, sr_split]
    obtain ⟨h1, h2, h3⟩ := (sv_futCausal_iff M v₀ y w).1 hw
    obtain ⟨hA, hB⟩ := sv_QD_pos hM v₀ ha hη hη2 (sv_χ_mem hM hy)
    have hU' := sv_χU'_pos hM (v₀ := v₀) (ũ := y.1) (by
      have : y.1 < sv_uH M v₀ := hy
      unfold sv_uH at this; linarith)
    have hV' : 0 < sv_χV M y.2 / (4 * M) := div_pos (sv_χV_pos M y.2) (by positivity)
    have := sr_pos_of_causal (mul_pos hU' hA) (mul_pos hV' hB) h1 h2 h3
    simp only at this ⊢
    linarith

include hM in
lemma sv_shell_UV {v₀ : ℝ} (c : (sv_flat M v₀).InextCausalCurveIn (sv_MS M v₀)) :
    Monotone (fun t => sv_χU M v₀ (c.γ t).1) ∧ Monotone (fun t => sv_χV M (c.γ t).2) ∧
      ∀ t, ((sv_χU M v₀ (c.γ t).1, sv_χV M (c.γ t).2) : P) ∈ seR := by
  have hu := sv_coord_mono_P c (fst ℝ ℝ ℝ) fun v h1 _ => h1
  have hv := sv_coord_mono_P c (snd ℝ ℝ ℝ) fun v _ h2 => h2
  have hlt : ∀ t, (c.γ t).1 < v₀ := fun t => by
    have : (c.γ t).1 < sv_uH M v₀ := c.mem t
    unfold sv_uH at this; linarith
  refine ⟨fun s t hst => (sv_χU_strictMonoOn hM v₀).monotoneOn (hlt s) (hlt t) (hu hst),
    fun s t hst => Real.exp_le_exp.2 (div_le_div_of_nonneg_right (hv hst) (by positivity)),
    fun t => sv_χ_mem hM (c.mem t)⟩

include hM in
/-- If `χ(γ(t))` had a limit in region I as `t → −∞` (or `+∞`), so would `γ` in `M`. -/
lemma sv_shell_v_lim {v₀ : ℝ} {γ : ℝ → P} {l : Filter ℝ} {p : P} (hp : 0 < p.2)
    (hlim : Tendsto (fun t => ((sv_χU M v₀ (γ t).1, sv_χV M (γ t).2) : P)) l (𝓝 p)) :
    Tendsto (fun t => (γ t).2) l (𝓝 (4 * M * Real.log p.2)) := by
  have h1 : Tendsto (fun t => sv_χV M (γ t).2) l (𝓝 p.2) := (continuous_snd.tendsto p).comp hlim
  have h2 := ((Real.continuousAt_log hp.ne').tendsto.comp h1).const_mul (4 * M)
  refine h2.congr fun t => ?_
  simp only [Function.comp]
  exact sv_log_χV hM _

include hM in
lemma sv_shell_fut {v₀ : ℝ} (c : (sv_flat M v₀).InextCausalCurveIn (sv_MS M v₀)) :
    ¬ ∃ p ∈ seR, Tendsto (fun t => ((sv_χU M v₀ (c.γ t).1, sv_χV M (c.γ t).2) : P)) atTop
      (𝓝 p) := by
  rintro ⟨p, hp, hlim⟩
  have hu := sv_coord_mono_P c (fst ℝ ℝ ℝ) fun v h1 _ => h1
  have hbdd : BddAbove (range fun t => (c.γ t).1) :=
    ⟨sv_uH M v₀, by rintro _ ⟨t, rfl⟩; exact (c.mem t).le⟩
  have hL : Tendsto (fun t => (c.γ t).1) atTop (𝓝 (⨆ t, (c.γ t).1)) :=
    tendsto_atTop_ciSup hu hbdd
  have hLle : (⨆ t, (c.γ t).1) ≤ sv_uH M v₀ := ciSup_le fun t => (c.mem t).le
  have h1 := ((sv_χU_continuous M v₀).tendsto _).comp hL
  have h2 : Tendsto (fun t => sv_χU M v₀ (c.γ t).1) atTop (𝓝 p.1) :=
    (continuous_fst.tendsto p).comp hlim
  have heq := tendsto_nhds_unique h1 h2
  have hLlt : (⨆ t, (c.γ t).1) < sv_uH M v₀ := by
    rcases hLle.lt_or_eq with h | h
    · exact h
    · exfalso; rw [h, sv_χU_uH hM] at heq; linarith [hp.1]
  exact c.inext_future ⟨(⨆ t, (c.γ t).1, 4 * M * Real.log p.2), hLlt,
    hL.prodMk_nhds (sv_shell_v_lim hM hp.2 hlim)⟩

include hM in
lemma sv_shell_past {v₀ : ℝ} (c : (sv_flat M v₀).InextCausalCurveIn (sv_MS M v₀)) :
    ¬ ∃ p ∈ seR, Tendsto (fun t => ((sv_χU M v₀ (c.γ t).1, sv_χV M (c.γ t).2) : P)) atBot
      (𝓝 p) := by
  rintro ⟨p, hp, hlim⟩
  have hu := sv_coord_mono_P c (fst ℝ ℝ ℝ) fun v h1 _ => h1
  have h2 : Tendsto (fun t => sv_χU M v₀ (c.γ t).1) atBot (𝓝 p.1) :=
    (continuous_fst.tendsto p).comp hlim
  by_cases hbdd : BddBelow (range fun t => (c.γ t).1)
  · have hL : Tendsto (fun t => (c.γ t).1) atBot (𝓝 (⨅ t, (c.γ t).1)) :=
      tendsto_atBot_ciInf hu hbdd
    have hLlt : (⨅ t, (c.γ t).1) < sv_uH M v₀ := lt_of_le_of_lt (ciInf_le hbdd 0) (c.mem 0)
    exact c.inext_past ⟨(⨅ t, (c.γ t).1, 4 * M * Real.log p.2), hLlt,
      hL.prodMk_nhds (sv_shell_v_lim hM hp.2 hlim)⟩
  · have hL : Tendsto (fun t => (c.γ t).1) atBot atBot :=
      tendsto_atBot_atBot_of_monotone hu fun b => by
        by_contra h; push Not at h
        exact hbdd ⟨b, by rintro _ ⟨t, rfl⟩; exact (h t).le⟩
    exact not_tendsto_nhds_of_tendsto_atBot ((sv_χU_tendsto hM v₀).comp hL) _ h2

include hM in
/-- **`Θ_shell` is Cauchy temporal on the flat plane `M` (BUILT).** Along a causal curve, `χ ∘ γ`
is a monotone path in region I (`sv_shell_UV`) with no limit in region I at either end
(`sv_shell_fut`, `sv_shell_past`: `U` has a continuous inverse on `M`'s range); then ⓐ's
`sv_future_pure`, `sv_past_pure` and `sv_cauchy_of_limits`. -/
theorem sv_cauchy_flat {a η v₀ : ℝ} (ha : 0 < a) (hη : 0 < η) (hη2 : η ≤ 2) :
    (sv_flat M v₀).IsCauchyTemporalOn (sv_MS M v₀) (sv_Θsh M a η v₀) := by
  refine MSpacetime.sv_cauchy_of_limits (sv_MS_open M v₀) (sv_temporal hM ha hη hη2)
    (fun c => ?_) (fun c => ?_)
  · obtain ⟨hU, hV, hR⟩ := sv_shell_UV hM c
    exact sv_future_pure hM ha hη hU hV hR (sv_shell_fut hM c)
  · obtain ⟨hU, hV, hR⟩ := sv_shell_UV hM c
    exact sv_past_pure hM ha hη hη2 hU hV hR (sv_shell_past hM c)

include hM in
/-- **ⓑ `sv_cauchy` (BUILT): on the thin-shell spacetime, `Θ_shell = Θ_ψ ∘ χ` is a Cauchy temporal
function of `M = {ũ < u_H}` for `0 < η ≤ 2`** (conformal invariance, `cz_scale_isCauchyTemporalOn`,
from `sv_cauchy_flat`). It equals `a(u + ηr)` on the vacuum exterior `v ≥ v₀`
(`sv_retarded_eq`). -/
theorem sv_cauchy {a η v₀ : ℝ} (ha : 0 < a) (hη : 0 < η) (hη2 : η ≤ 2) :
    (sv_S hM v₀).IsCauchyTemporalOn (sv_S hM v₀).M (sv_Θsh M a η v₀) :=
  (sv_flat M v₀).cz_scale_isCauchyTemporalOn (sv_Φ_pos hM v₀) (sv_cauchy_flat hM ha hη hη2)

/-! #### `D = I⁻(O) = M` -/

lemma sv_vel_eq (γ : ℝ → P) (t : ℝ) : MSpacetime.vel γ t = deriv γ t := by
  show mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, P) γ t (1 : ℝ) = deriv γ t
  rw [mfderiv_eq_fderiv]; rfl

lemma sv_futTimelike_iff (M v₀ : ℝ) (x v : P) :
    (sv_flat M v₀).FutTimelike x v ↔ 0 < v.1 ∧ 0 < v.2 :=
  futTimelike_iff x v

include hM in
/-- Straight segments with both null coordinates increasing are timelike steps inside `M`. -/
lemma sv_tstep {v₀ : ℝ} {x y : P} (hy : y ∈ sv_MS M v₀) (h1 : x.1 < y.1) (h2 : x.2 < y.2) :
    (sv_S hM v₀).TStep x y := by
  rw [sv_S, MSpacetime.cz_scale_tstep]
  have hd : deriv (fun t : ℝ => x + t • (y - x)) = fun _ => y - x := by
    funext t
    have h : HasDerivAt (fun t : ℝ => x + t • (y - x)) ((1:ℝ) • (y - x)) t :=
      ((hasDerivAt_id' t).smul_const (y - x)).const_add x
    rw [h.deriv, one_smul]
  refine ⟨fun t => x + t • (y - x), ?_, by simp, by simp, fun t ht => ⟨?_, ?_⟩⟩
  · rw [contMDiff_iff_contDiff]; exact contDiff_const.add (contDiff_id.smul contDiff_const)
  · show (x + t • (y - x)).1 < sv_uH M v₀
    have hy' : y.1 < sv_uH M v₀ := hy
    simp only [Prod.fst_add, Prod.smul_fst, Prod.fst_sub, smul_eq_mul]
    nlinarith [mul_le_mul_of_nonneg_right ht.2 (sub_pos.2 h1).le]
  · rw [sv_vel_eq, hd, sv_futTimelike_iff]
    simp only [Prod.fst_sub, Prod.snd_sub, sub_pos]
    exact ⟨h1, h2⟩

/-- **The observer** `O(τ) = (u_H − e^{−τ}, τ)`: inside `M`, with `ũ → u_H`. -/
noncomputable def sv_O (M v₀ τ : ℝ) : P := (sv_uH M v₀ - Real.exp (-τ), τ)

include hM in
/-- **`sv_D` (BUILT): `D = I⁻(O) = M = {ũ < u_H}`** for the observer `O(τ) = (u_H − e^{−τ}, τ)`,
which lies in `M`, is future timelike, and has `ũ → u_H`. -/
theorem sv_D (v₀ : ℝ) :
    (sv_S hM v₀).D (range (sv_O M v₀)) = (sv_S hM v₀).M ∧
    range (sv_O M v₀) ⊆ (sv_S hM v₀).M ∧
    (∀ s t : ℝ, s < t → (sv_S hM v₀).Chr (sv_O M v₀ s) (sv_O M v₀ t)) ∧
    Tendsto (fun τ => (sv_O M v₀ τ).1) atTop (𝓝 (sv_uH M v₀)) := by
  have hOM : ∀ τ, sv_O M v₀ τ ∈ sv_MS M v₀ := fun τ => by
    show sv_uH M v₀ - Real.exp (-τ) < sv_uH M v₀
    linarith [Real.exp_pos (-τ)]
  refine ⟨Subset.antisymm ((sv_S hM v₀).D_subset_M _) fun x hx => ?_,
    by rintro _ ⟨τ, rfl⟩; exact hOM τ, fun s t hst => ?_, ?_⟩
  · have hx' : x.1 < sv_uH M v₀ := hx
    have e1 : ∀ᶠ τ in atTop, Real.exp (-τ) < sv_uH M v₀ - x.1 :=
      (tendsto_order.1 Real.tendsto_exp_neg_atTop_nhds_zero).2 _ (by linarith)
    obtain ⟨τ, h1, h2⟩ := (e1.and (eventually_gt_atTop x.2)).exists
    exact mem_iUnion₂.2 ⟨sv_O M v₀ τ, mem_range_self τ, Relation.TransGen.single
      (sv_tstep hM (hOM τ) (by show x.1 < sv_uH M v₀ - Real.exp (-τ); linarith) h2)⟩
  · refine Relation.TransGen.single (sv_tstep hM (hOM t) ?_ hst)
    show sv_uH M v₀ - Real.exp (-s) < sv_uH M v₀ - Real.exp (-t)
    have := Real.exp_lt_exp.2 (show -t < -s by linarith)
    linarith
  · have h := (Real.tendsto_exp_neg_atTop_nhds_zero).const_sub (sv_uH M v₀)
    rw [sub_zero] at h
    exact h

include hM in
/-- **ⓑ `sv_cauchy` on `D`:** the same statement with `D = I⁻(O)`. -/
theorem sv_cauchy_D {a η v₀ : ℝ} (ha : 0 < a) (hη : 0 < η) (hη2 : η ≤ 2) :
    (sv_S hM v₀).IsCauchyTemporalOn ((sv_S hM v₀).D (range (sv_O M v₀))) (sv_Θsh M a η v₀) := by
  rw [(sv_D hM v₀).1]; exact sv_cauchy hM ha hη hη2

/-! ### Non-vacuity -/

lemma sv_mem5 : ((-5 : ℝ), (0 : ℝ)) ∈ sv_MS 1 0 := by
  show (-5 : ℝ) < sv_uH 1 0; unfold sv_uH; norm_num

lemma sv_mem5' : ((-5 : ℝ), (1 : ℝ)) ∈ sv_MS 1 0 := by
  show (-5 : ℝ) < sv_uH 1 0; unfold sv_uH; norm_num

/-- **Non-vacuity (BUILT)** at `M = 1`, `v₀ = 0` (`u_H = −4`), `a = 1`: `sv_cauchy` at the boundary
case `η = 2` and at `η = 1`; the eternal core lemma at `η = 2` (static observer at `r₀ = 4`);
`Φ ≢ 1` (`Φ(−5, 0) = 1 < Φ(−5, 1)`); `Θ_shell` is not constant (`Θ_shell(−5, 0) < Θ_shell(−5, 1)`)
and equals `u + 2r` at both points; `M` is non-empty. -/
theorem sv_nonvacuous :
    (sv_S one_pos 0).IsCauchyTemporalOn (sv_S one_pos 0).M (sv_Θsh 1 1 2 0) ∧
    (sv_S one_pos 0).IsCauchyTemporalOn (sv_S one_pos 0).M (sv_Θsh 1 1 1 0) ∧
    (se_S one_pos).IsCauchyTemporalOn
      ((se_S one_pos).D (range (se_Ost one_pos (r₀ := 4) (by norm_num)))) (sv_Θψ 1 1 2 0) ∧
    sv_Φ 1 0 ((-5 : ℝ), (0 : ℝ)) = 1 ∧ 1 < sv_Φ 1 0 ((-5 : ℝ), (1 : ℝ)) ∧
    sv_Θsh 1 1 2 0 ((-5 : ℝ), (0 : ℝ)) < sv_Θsh 1 1 2 0 ((-5 : ℝ), (1 : ℝ)) ∧
    sv_Θsh 1 1 2 0 ((-5 : ℝ), (1 : ℝ)) =
      1 * (sv_F 1 0 (-5) + 2 * sv_r 1 0 ((-5 : ℝ), (1 : ℝ))) ∧
    ((sv_S one_pos 0).M).Nonempty := by
  refine ⟨sv_cauchy one_pos one_pos (by norm_num) le_rfl,
    sv_cauchy one_pos one_pos one_pos (by norm_num),
    sv_eternal_cauchy one_pos (by norm_num) one_pos (by norm_num) le_rfl 0,
    sv_flat_past one_pos sv_mem5 le_rfl, sv_Φ_gt_one one_pos sv_mem5' one_pos, ?_,
    sv_retarded_eq one_pos sv_mem5' zero_le_one, ⟨_, sv_mem5⟩⟩
  rw [sv_retarded_eq one_pos sv_mem5 le_rfl, sv_retarded_eq one_pos sv_mem5' zero_le_one]
  have := sv_r_strictMono one_pos (v₀ := 0) (ũ := -5) (v := 0) (v' := 1) sv_mem5 one_pos
  simp only at this ⊢
  linarith
end SVModel

/-! ## NEW (campaign 102): the shell model extended across the horizon, `∂D = 𝓗⁺` -/

namespace SHModel
open Model SEModel SRModel SVModel Kruskal Manifold ContinuousLinearMap TopologicalSpace

set_option synthInstance.maxHeartbeats 400000

variable {M : ℝ} (hM : 0 < M)

/-! ### ① The extended model -/

/-- **The extended manifold** `M′ = {ũ < v₀} ∩ {U(ũ) V(v) < 1}`: across `𝓗⁺ = {ũ = u_H}` into the
black-hole side, up to (not including) `r = 0`. -/
def sh_MS (M v₀ : ℝ) : Set P := {y | y.1 < v₀ ∧ sv_χU M v₀ y.1 * sv_χV M y.2 < 1}

lemma sh_MS_open (M v₀ : ℝ) : IsOpen (sh_MS M v₀) :=
  (isOpen_lt continuous_fst continuous_const).inter
    (isOpen_lt (((sv_χU_continuous M v₀).comp continuous_fst).mul
      ((Real.continuous_exp.comp (continuous_snd.div_const _)))) continuous_const)

/-- The Kruskal image of a point of `M′` lies in `{UV < 1}`. -/
lemma sh_χ_mem {v₀ : ℝ} {y : P} (hy : y ∈ sh_MS M v₀) : sv_χ M v₀ y ∈ sk_kM := hy.2

include hM in
/-- **The identity checked in advance:** on the shell `v = v₀`, `−U(ũ) V(v₀) = h((v₀ − ũ)/2)`,
for every `ũ`. -/
lemma sh_UV_shell (v₀ ũ : ℝ) :
    -(sv_χU M v₀ ũ * sv_χV M v₀) = hK M ((v₀ - ũ) / 2) := by
  have hM' : M ≠ 0 := hM.ne'
  unfold sv_χU sv_χV hK
  have e1 : Real.exp ((v₀ - ũ) / 2 / (2 * M)) =
      Real.exp (-ũ / (4 * M)) * Real.exp (v₀ / (4 * M)) := by
    rw [← Real.exp_add]; congr 1; field_simp; ring
  have e2 : (v₀ - ũ) / 2 / (2 * M) - 1 = (v₀ - ũ) / (4 * M) - 1 := by field_simp; ring
  rw [e1, e2]; ring

include hM in
/-- The shell point `(ũ, v₀)` of a ray `ũ < v₀` lies in `M′`. -/
lemma sh_shell_mem {v₀ ũ : ℝ} (h : ũ < v₀) : ((ũ, v₀) : P) ∈ sh_MS M v₀ := by
  refine ⟨h, ?_⟩
  have h1 := hK_gt hM (x := (v₀ - ũ) / 2) (by linarith)
  have h2 := sh_UV_shell hM v₀ ũ
  show sv_χU M v₀ ũ * sv_χV M v₀ < 1
  linarith

include hM in
/-- `(ũ, max(v, v₀)) ∈ M′` for `(ũ, v) ∈ M′`. -/
lemma sh_max_mem {v₀ : ℝ} {y : P} (hy : y ∈ sh_MS M v₀) : ((y.1, max y.2 v₀) : P) ∈ sh_MS M v₀ := by
  rcases le_total y.2 v₀ with h | h
  · rw [max_eq_right h]; exact sh_shell_mem hM hy.1
  · rw [max_eq_left h]; exact hy

include hM in
/-- **On the shell, `r = r_s = (v₀ − ũ)/2`**, for every `ũ < v₀` (inside and behind the horizon). -/
lemma sh_r_shell {v₀ ũ : ℝ} (h : ũ < v₀) : sv_r M v₀ (ũ, v₀) = (v₀ - ũ) / 2 := by
  show rinv M (-(sv_χU M v₀ ũ * sv_χV M v₀)) = _
  rw [sh_UV_shell hM, rinv_hK hM (by linarith)]

open Classical in
/-- **The conformal factor** `Φ′(ũ, v) = F_K(r) U′(ũ) V/4M` at `(ũ, max(v, v₀))`, `r = r_K(UV)`
(Kruskal pulled back by `χ`); `1` off `M′`. -/
noncomputable def sh_Φ (M v₀ : ℝ) (y : P) : ℝ :=
  if y ∈ sh_MS M v₀ then
    FS M (sv_χ M v₀ (y.1, max y.2 v₀)) * sv_χU' M v₀ y.1 * (sv_χV M (max y.2 v₀) / (4 * M))
  else 1

lemma sh_Φ_of_mem {v₀ : ℝ} {y : P} (hy : y ∈ sh_MS M v₀) :
    sh_Φ M v₀ y =
      FS M (sv_χ M v₀ (y.1, max y.2 v₀)) * sv_χU' M v₀ y.1 * (sv_χV M (max y.2 v₀) / (4 * M)) := by
  unfold sh_Φ; rw [ite_eq_left_of_eq_true _ _ (eq_true hy)]

include hM in
/-- **`Φ′ > 0` (BUILT).** -/
theorem sh_Φ_pos (v₀ : ℝ) (y : P) : 0 < sh_Φ M v₀ y := by
  by_cases hy : y ∈ sh_MS M v₀
  · rw [sh_Φ_of_mem hy]
    have h1 := sk_FS_pos hM (sh_χ_mem (sh_max_mem hM hy))
    have h2 := sv_χU'_pos hM (v₀ := v₀) hy.1
    have h3 : 0 < sv_χV M (max y.2 v₀) / (4 * M) := div_pos (sv_χV_pos _ _) (by positivity)
    positivity
  · unfold sh_Φ; rw [ite_eq_right_of_eq_false _ _ (eq_false hy)]; exact one_pos

include hM in
/-- **`Φ′` is continuous on `M′` (BUILT)** (`C⁰` across the shell; the kink is at `v = v₀`). -/
theorem sh_Φ_continuousOn (v₀ : ℝ) : ContinuousOn (sh_Φ M v₀) (sh_MS M v₀) := by
  have hχ : Continuous (fun y : P => sv_χ M v₀ (y.1, max y.2 v₀)) := by
    unfold sv_χ sv_χU sv_χV; fun_prop
  have hF : ContinuousOn (fun y : P => FS M (sv_χ M v₀ (y.1, max y.2 v₀))) (sh_MS M v₀) :=
    (sk_FS_contDiffOn hM).continuousOn.comp hχ.continuousOn fun y hy =>
      sh_χ_mem (sh_max_mem hM hy)
  have hU : Continuous (fun y : P => sv_χU' M v₀ y.1) := by unfold sv_χU'; fun_prop
  have hV : Continuous (fun y : P => sv_χV M (max y.2 v₀) / (4 * M)) := by
    unfold sv_χV; fun_prop
  exact ((hF.mul hU.continuousOn).mul hV.continuousOn).congr fun y hy => sh_Φ_of_mem hy

/-- **The flat plane with `M = M′`** (`cz_St` restricted). -/
noncomputable def sh_flat (M v₀ : ℝ) : MSpacetime P P :=
  NModel.cz_St.restrictM (sh_MS M v₀) (sh_MS_open M v₀) (subset_univ _)

/-- **The extended shell spacetime** `sh_S`: on `P`, `M′ = {ũ < v₀, UV < 1}`, `g = −Φ′ dũ dv`,
`T = (1, 1)`. -/
noncomputable def sh_S (v₀ : ℝ) : MSpacetime P P :=
  (sh_flat M v₀).cz_scale (sh_Φ M v₀) (sh_Φ_pos hM v₀)

lemma sh_S_M (v₀ : ℝ) : (sh_S hM v₀).M = sh_MS M v₀ := rfl

/-- **The metric (BUILT):** `g = Φ′ · (−dũ dv)` in the identity chart. -/
theorem sh_hRep (v₀ : ℝ) (p y : P) : hRep (sh_S hM v₀).g p y = sh_Φ M v₀ y • gM := by
  rw [sh_S, MSpacetime.cz_hRep_scale, NModel.cz_extChart_symm_apply]
  have : hRep (sh_flat M v₀).g p y = gM := congrFun (NModel.cz_hRep p) y
  rw [this]

include hM in
/-- **`sh_flat_past` (BUILT): `Φ′ = 1` for `v ≤ v₀`**, on all of `M′` (both sides of `𝓗⁺`). -/
theorem sh_flat_past {v₀ : ℝ} {y : P} (hy : y ∈ sh_MS M v₀) (hv : y.2 ≤ v₀) :
    sh_Φ M v₀ y = 1 := by
  have hM' : M ≠ 0 := hM.ne'
  have hu : y.1 < v₀ := hy.1
  rw [sh_Φ_of_mem hy, max_eq_right hv]
  unfold FS
  rw [show rK M (sv_χ M v₀ (y.1, v₀)) = (v₀ - y.1) / 2 from sh_r_shell hM hu]
  unfold sv_χU' sv_χV
  have he : Real.exp (-((v₀ - y.1) / 2) / (2 * M)) * Real.exp (-y.1 / (4 * M)) *
      Real.exp (v₀ / (4 * M)) = 1 := by
    rw [← Real.exp_add, ← Real.exp_add, ← Real.exp_zero]; congr 1; field_simp; ring
  have h2 : v₀ - y.1 ≠ 0 := by linarith
  generalize Real.exp (-((v₀ - y.1) / 2) / (2 * M)) = A at *
  generalize Real.exp (-y.1 / (4 * M)) = B at *
  generalize Real.exp (v₀ / (4 * M)) = C at *
  field_simp
  linear_combination 64 * he

include hM in
/-- **`sh_vacuum` (BUILT): for `v ≥ v₀`, `−Φ′ dũ dv` is Kruskal's `−F_K(r) dU dV` pulled back by
`χ = (U(ũ), V(v))`**: `Φ′ = F_K(r) U′(ũ) V′(v)` with `U′ = dU/dũ`, `V′ = dV/dv = V/4M`, and
`r = r_K(UV)` with `h(r) = −UV`. -/
theorem sh_vacuum {v₀ : ℝ} {y : P} (hy : y ∈ sh_MS M v₀) (hv : v₀ ≤ y.2) :
    sh_Φ M v₀ y = FS M (sv_χ M v₀ y) * sv_χU' M v₀ y.1 * (sv_χV M y.2 / (4 * M)) ∧
    HasDerivAt (sv_χU M v₀) (sv_χU' M v₀ y.1) y.1 ∧
    HasDerivAt (sv_χV M) (sv_χV M y.2 / (4 * M)) y.2 ∧
    hK M (sv_r M v₀ y) = -(sv_χU M v₀ y.1 * sv_χV M y.2) := by
  refine ⟨?_, sv_χU_hasDerivAt hM v₀ y.1, sv_χV_hasDerivAt M y.2,
    (sk_rK_spec hM (sh_χ_mem hy)).2⟩
  rw [sh_Φ_of_mem hy, max_eq_left hv]

include hM in
/-- `D`'s side: `{ũ < u_H} ⊆ M′`. -/
lemma sh_sv_sub {v₀ : ℝ} {y : P} (hy : y ∈ sv_MS M v₀) : y ∈ sh_MS M v₀ := by
  have h1 : y.1 < sv_uH M v₀ := hy
  have hU := sv_χU_neg hM hy
  have hV := sv_χV_pos M y.2
  refine ⟨by unfold sv_uH at h1; linarith [hM], ?_⟩
  have : sv_χU M v₀ y.1 * sv_χV M y.2 < 0 := mul_neg_of_neg_of_pos hU hV
  linarith

include hM in
/-- `U′ = −U F′/4M` on `ũ < u_H`. -/
lemma sh_χU'_eq {v₀ ũ : ℝ} (h : ũ < sv_uH M v₀) :
    sv_χU' M v₀ ũ = -sv_χU M v₀ ũ * sv_F' M v₀ ũ / (4 * M) := by
  have hM' : M ≠ 0 := hM.ne'
  have hu : sv_uH M v₀ - ũ ≠ 0 := by linarith
  unfold sv_χU' sv_χU sv_F'
  unfold sv_uH at hu ⊢
  field_simp
  ring

include hM in
/-- **`sh_agree` (BUILT): `Φ′ = Φ` on `D = {ũ < u_H}`**, i.e. `F_K dU dV = f du dv`. -/
theorem sh_agree {v₀ : ℝ} {y : P} (hy : y ∈ sv_MS M v₀) : sh_Φ M v₀ y = sv_Φ M v₀ y := by
  have hM' : M ≠ 0 := hM.ne'
  have hy1 : y.1 < sv_uH M v₀ := hy
  have hy' := sh_sv_sub hM hy
  rw [sh_Φ_of_mem hy']
  unfold sv_Φ
  rw [ite_eq_left_of_eq_true _ _ (eq_true hy1)]
  have hp := sh_χ_mem (sh_max_mem hM hy')
  obtain ⟨hr, hh⟩ := sk_rK_spec hM hp
  set r := rK M (sv_χ M v₀ (y.1, max y.2 v₀)) with hr_def
  have hsr : sv_r M v₀ (y.1, max y.2 v₀) = r := rfl
  rw [hsr, sh_χU'_eq hM hy1]
  have hh' : -(sv_χU M v₀ y.1 * sv_χV M (max y.2 v₀)) = hK M r := hh.symm
  unfold FS
  rw [← hr_def]
  have he : Real.exp (-r / (2 * M)) * Real.exp (r / (2 * M)) = 1 := by
    rw [← Real.exp_add, neg_div, neg_add_cancel, Real.exp_zero]
  have hr0 : r ≠ 0 := hr.ne'
  unfold hK at hh'
  generalize Real.exp (-r / (2 * M)) = E' at *
  generalize Real.exp (r / (2 * M)) = E at *
  generalize sv_χU M v₀ y.1 = U at *
  generalize sv_χV M (max y.2 v₀) = V at *
  generalize sv_F' M v₀ y.1 = F at *
  have k : 32 * M ^ 3 / r * E' * (-U * F / (4 * M)) * (V / (4 * M)) =
      2 * M / r * F * (E' * (-(U * V))) := by
    field_simp; ring
  rw [k, hh']
  have k2 : E' * ((r / (2 * M) - 1) * E) = r / (2 * M) - 1 := by
    rw [show E' * ((r / (2 * M) - 1) * E) = (r / (2 * M) - 1) * (E' * E) by ring, he, mul_one]
  rw [k2]
  field_simp

/-! ### ② The causal structure of `M′` -/

include hM in
/-- **`sh_seg_mem` (BUILT): `M′` is null-convex.** A segment with `ũ`, `v` non-decreasing ending
in `M′` stays in `M′`: `U` increases on `ũ < v₀`, and where `U > 0`, `UV ≤ U(ũ_y) V(v_y) < 1`. -/
theorem sh_seg_mem {v₀ : ℝ} {x y : P} (hy : y ∈ sh_MS M v₀) (h1 : x.1 ≤ y.1) (h2 : x.2 ≤ y.2)
    {t : ℝ} (ht : t ∈ Icc (0:ℝ) 1) : x + t • (y - x) ∈ sh_MS M v₀ := by
  set z := x + t • (y - x) with hz
  have hz1 : z.1 ≤ y.1 := by
    simp only [hz, Prod.fst_add, Prod.smul_fst, Prod.fst_sub, smul_eq_mul]
    nlinarith [mul_le_mul_of_nonneg_right ht.2 (sub_nonneg.2 h1)]
  have hz2 : z.2 ≤ y.2 := by
    simp only [hz, Prod.snd_add, Prod.smul_snd, Prod.snd_sub, smul_eq_mul]
    nlinarith [mul_le_mul_of_nonneg_right ht.2 (sub_nonneg.2 h2)]
  have hzv : z.1 < v₀ := lt_of_le_of_lt hz1 hy.1
  refine ⟨hzv, ?_⟩
  have hU : sv_χU M v₀ z.1 ≤ sv_χU M v₀ y.1 :=
    (sv_χU_strictMonoOn hM v₀).monotoneOn hzv hy.1 hz1
  have hV : sv_χV M z.2 ≤ sv_χV M y.2 :=
    Real.exp_le_exp.2 (div_le_div_of_nonneg_right hz2 (by positivity))
  have hV0 := sv_χV_pos M z.2
  have hy2 : sv_χU M v₀ y.1 * sv_χV M y.2 < 1 := hy.2
  rcases le_or_gt (sv_χU M v₀ z.1) 0 with h | h
  · have : sv_χU M v₀ z.1 * sv_χV M z.2 ≤ 0 := mul_nonpos_of_nonpos_of_nonneg h hV0.le
    linarith
  · have : sv_χU M v₀ z.1 * sv_χV M z.2 ≤ sv_χU M v₀ y.1 * sv_χV M y.2 :=
      mul_le_mul hU hV hV0.le (by linarith)
    linarith

/-- A step of `sh_flat` is a step of campaign 81's `mink`. -/
lemma sh_tstep_mink {v₀ : ℝ} {x y : P} (h : (sh_flat M v₀).TStep x y) : mink.TStep x y := by
  obtain ⟨γ, hγ, h0, h1, ht⟩ := h
  refine ⟨γ, contMDiff_iff_contDiff.1 hγ, h0, h1, fun t htI => ⟨mem_univ _, ?_⟩⟩
  have := (ht t htI).2
  rw [sv_vel_eq] at this
  exact this

lemma sh_cstep_mink {v₀ : ℝ} {x y : P} (h : (sh_flat M v₀).CStep x y) : mink.CStep x y := by
  obtain ⟨γ, hγ, h0, h1, ht⟩ := h
  refine ⟨γ, contMDiff_iff_contDiff.1 hγ, h0, h1, fun t htI => ⟨mem_univ _, ?_⟩⟩
  have := (ht t htI).2
  rw [sv_vel_eq] at this
  exact this

lemma sh_chr_mink {v₀ : ℝ} {x y : P} (h : (sh_flat M v₀).Chr x y) : mink.Chr x y := by
  induction h with
  | single h => exact Relation.TransGen.single (sh_tstep_mink h)
  | tail _ h ih => exact ih.tail (sh_tstep_mink h)

lemma sh_cau_mink {v₀ : ℝ} {x y : P} (h : (sh_flat M v₀).Cau x y) : mink.Cau x y := by
  induction h with
  | refl => exact Relation.ReflTransGen.refl
  | tail _ h ih => exact ih.tail (sh_cstep_mink h)

include hM in
/-- The straight segment is a timelike step of `sh_flat` when both null coordinates increase. -/
lemma sh_tstep {v₀ : ℝ} {x y : P} (hy : y ∈ sh_MS M v₀) (h1 : x.1 < y.1) (h2 : x.2 < y.2) :
    (sh_flat M v₀).TStep x y := by
  refine ⟨fun t => x + t • (y - x), ?_, by simp, by simp,
    fun t ht => ⟨sh_seg_mem hM hy h1.le h2.le ht, ?_⟩⟩
  · rw [contMDiff_iff_contDiff]; exact contDiff_const.add (contDiff_id.smul contDiff_const)
  · rw [sv_vel_eq, sk_deriv_seg]
    show mink.FutTimelike (x + t • (y - x)) (y - x)
    rw [futTimelike_iff]
    simp only [Prod.fst_sub, Prod.snd_sub, sub_pos]
    exact ⟨h1, h2⟩

/-- A timelike step of `sh_flat` is a causal step. -/
lemma sh_tstep_cstep {v₀ : ℝ} {x y : P} (h : (sh_flat M v₀).TStep x y) :
    (sh_flat M v₀).CStep x y := by
  obtain ⟨γ, hγ, h0, h1, ht⟩ := h
  refine ⟨γ, hγ, h0, h1, fun t htI => ⟨(ht t htI).1, ?_⟩⟩
  have h := (ht t htI).2
  change mink.FutTimelike (γ t) (MSpacetime.vel γ t) at h
  change mink.FutCausal (γ t) (MSpacetime.vel γ t)
  rw [futTimelike_iff] at h
  rw [futCausal_iff]
  exact ⟨h.1.le, h.2.le, by linarith [h.1, h.2]⟩

include hM in
/-- **`sh_chr` (BUILT): `x ≪ y ⇔ ũ_x < ũ_y ∧ v_x < v_y` on `M′`.** -/
theorem sh_chr {v₀ : ℝ} {x y : P} (hx : x ∈ sh_MS M v₀) (hy : y ∈ sh_MS M v₀) :
    (sh_S hM v₀).Chr x y ↔ x.1 < y.1 ∧ x.2 < y.2 := by
  rw [sh_S, MSpacetime.cz_scale_chr]
  refine ⟨fun h => chr_lt (sh_chr_mink h), fun h => ?_⟩
  have _hx := hx
  exact Relation.TransGen.single (sh_tstep hM hy h.1 h.2)

include hM in
/-- **Causal curves raise both null coordinates:** `x ≤ y ⇒ ũ_x ≤ ũ_y ∧ v_x ≤ v_y`. -/
theorem sh_cau_le {v₀ : ℝ} {x y : P} (h : (sh_S hM v₀).Cau x y) : x.1 ≤ y.1 ∧ x.2 ≤ y.2 := by
  rw [sh_S, MSpacetime.cz_scale_cau] at h
  exact cau_le (sh_cau_mink h)

include hM in
/-- **The observer** (campaign 101's `sv_O`, `O(τ) = (u_H − e^{−τ}, τ)`) in `M′`: future
timelike, `ũ → u_H⁻`, `v → ∞`. -/
theorem sh_O (v₀ : ℝ) :
    range (sv_O M v₀) ⊆ (sh_S hM v₀).M ∧
    (∀ s t : ℝ, s < t → (sh_S hM v₀).Chr (sv_O M v₀ s) (sv_O M v₀ t)) ∧
    (∀ τ, (sv_O M v₀ τ).1 < sv_uH M v₀) ∧
    Tendsto (fun τ => (sv_O M v₀ τ).1) atTop (𝓝 (sv_uH M v₀)) ∧
    Tendsto (fun τ => (sv_O M v₀ τ).2) atTop atTop := by
  have hlt : ∀ τ, (sv_O M v₀ τ).1 < sv_uH M v₀ := fun τ => by
    show sv_uH M v₀ - Real.exp (-τ) < sv_uH M v₀
    linarith [Real.exp_pos (-τ)]
  have hOM : ∀ τ, sv_O M v₀ τ ∈ sh_MS M v₀ := fun τ => sh_sv_sub hM (hlt τ)
  refine ⟨by rintro _ ⟨τ, rfl⟩; exact hOM τ, fun s t hst => ?_, hlt, (sv_D hM v₀).2.2.2,
    tendsto_id⟩
  refine (sh_chr hM (hOM s) (hOM t)).2 ⟨?_, hst⟩
  show sv_uH M v₀ - Real.exp (-s) < sv_uH M v₀ - Real.exp (-t)
  have := Real.exp_lt_exp.2 (show -t < -s by linarith)
  linarith

include hM in
/-- Every point of `{ũ < u_H}` is in the chronological past of a late enough `O(τ)`. -/
lemma sh_chr_O {v₀ : ℝ} {x : P} (hx : x.1 < sv_uH M v₀) :
    ∃ τ, (sh_flat M v₀).TStep x (sv_O M v₀ τ) := by
  have e1 : ∀ᶠ τ in atTop, Real.exp (-τ) < sv_uH M v₀ - x.1 :=
    (tendsto_order.1 Real.tendsto_exp_neg_atTop_nhds_zero).2 _ (by linarith)
  obtain ⟨τ, h1, h2⟩ := (e1.and (eventually_gt_atTop x.2)).exists
  have hlt : (sv_O M v₀ τ).1 < sv_uH M v₀ := by
    show sv_uH M v₀ - Real.exp (-τ) < sv_uH M v₀
    linarith [Real.exp_pos (-τ)]
  exact ⟨τ, sh_tstep hM (sh_sv_sub hM hlt)
    (by show x.1 < sv_uH M v₀ - Real.exp (-τ); linarith) h2⟩

include hM in
/-- **`sh_D` (BUILT): `D = I⁻(O) = {ũ < u_H}`** on the extended `M′`. -/
theorem sh_D (v₀ : ℝ) :
    (sh_S hM v₀).D (range (sv_O M v₀)) = {y : P | y.1 < sv_uH M v₀} := by
  apply Subset.antisymm
  · intro p hp
    obtain ⟨_, ⟨τ, rfl⟩, h⟩ := mem_iUnion₂.1 hp
    have h' : (sh_flat M v₀).Chr p (sv_O M v₀ τ) := by
      have h0 : (sh_S hM v₀).Chr p (sv_O M v₀ τ) := h
      rw [sh_S, MSpacetime.cz_scale_chr] at h0; exact h0
    have h1 := (chr_lt (sh_chr_mink h')).1
    have := (sh_O hM v₀).2.2.1 τ
    show p.1 < sv_uH M v₀
    linarith
  · intro p hp
    obtain ⟨τ, h⟩ := sh_chr_O hM (show p.1 < sv_uH M v₀ from hp)
    refine mem_iUnion₂.2 ⟨sv_O M v₀ τ, mem_range_self τ, ?_⟩
    show (sh_S hM v₀).Chr p (sv_O M v₀ τ)
    rw [sh_S, MSpacetime.cz_scale_chr]
    exact Relation.TransGen.single h

include hM in
/-- **`sh_Jpast` (BUILT, the registered expected stop): `J⁻(O) = {ũ < u_H} = D`.** A causal
curve in `M′` raises both null coordinates (`sh_cau_le`), and `ũ_O(τ) < u_H`. -/
theorem sh_Jpast (v₀ : ℝ) :
    (sh_S hM v₀).JpastSet (range (sv_O M v₀)) = {y : P | y.1 < sv_uH M v₀} := by
  apply Subset.antisymm
  · intro p hp
    obtain ⟨_, ⟨τ, rfl⟩, h⟩ := mem_iUnion₂.1 hp
    have h1 := (sh_cau_le hM h).1
    have := (sh_O hM v₀).2.2.1 τ
    show p.1 < sv_uH M v₀
    linarith
  · intro p hp
    obtain ⟨τ, h⟩ := sh_chr_O hM (show p.1 < sv_uH M v₀ from hp)
    refine mem_iUnion₂.2 ⟨sv_O M v₀ τ, mem_range_self τ, ?_⟩
    show (sh_S hM v₀).Cau p (sv_O M v₀ τ)
    rw [sh_S, MSpacetime.cz_scale_cau]
    exact Relation.ReflTransGen.single (sh_tstep_cstep h)

/-! ### ③ The frontier: `∂D = 𝓗⁺ = {ũ = u_H}` -/

lemma sh_frontier_lt (c : ℝ) : frontier {y : P | y.1 < c} = {y : P | y.1 = c} := by
  have e : {y : P | y.1 < c} = Prod.fst ⁻¹' Iio c := rfl
  rw [e, ← isOpenMap_fst.preimage_frontier_eq_frontier_preimage continuous_fst, frontier_Iio]
  rfl

include hM in
/-- **`sh_frontier` (BUILT): `𝓗⁺ = ∂_P J⁻(O) = {ũ = u_H}`**, the future horizon alone. -/
theorem sh_frontier (v₀ : ℝ) :
    (sh_S hM v₀).H (range (sv_O M v₀)) = {y : P | y.1 = sv_uH M v₀} := by
  show frontier ((sh_S hM v₀).JpastSet (range (sv_O M v₀))) = _
  rw [sh_Jpast hM, sh_frontier_lt]

include hM in
/-- **`𝓗⁺ ⊆ M′`** (`U(u_H) = 0`, so `UV = 0 < 1`). -/
theorem sh_H_sub (v₀ : ℝ) : {y : P | y.1 = sv_uH M v₀} ⊆ sh_MS M v₀ := by
  intro y hy
  have hy' : y.1 = sv_uH M v₀ := hy
  refine ⟨by rw [hy']; unfold sv_uH; linarith, ?_⟩
  rw [hy', sv_χU_uH hM, zero_mul]; exact one_pos

include hM in
/-- **On `𝓗⁺`, `sv_r = 2M`, for every `v`.** `sv_r` is the Kruskal vacuum radius `rK ∘ χ`, continued over the whole
model. Only where `v ≥ v₀` (once the shell has passed, `sh_vacuum`) is it the areal radius of the spacetime. For
`v < v₀` the horizon lies in the flat body (`sh_H_flat`), and there `sv_r` is not the interior's areal radius. -/
theorem sh_H_r {v₀ : ℝ} {y : P} (hy : y.1 = sv_uH M v₀) : sv_r M v₀ y = 2 * M := by
  have hm : sv_χ M v₀ y ∈ sk_kM := sh_χ_mem (sh_H_sub hM v₀ hy)
  refine (sk_rK_eq_two_iff hM hm).2 ?_
  show sv_χU M v₀ y.1 * sv_χV M y.2 = 0
  rw [hy, sv_χU_uH hM, zero_mul]

include hM in
/-- **On `𝓗⁺` with `v < v₀`: `Φ′ = 1`**, the horizon forms in the flat body. -/
theorem sh_H_flat {v₀ : ℝ} {y : P} (hy : y.1 = sv_uH M v₀) (hv : y.2 ≤ v₀) : sh_Φ M v₀ y = 1 :=
  sh_flat_past hM (sh_H_sub hM v₀ hy) hv

/-- The Cauchy property passes from `sv_flat` to `sh_flat` (the same `g`, `T`). -/
lemma sh_cauchy_transfer {v₀ : ℝ} {U : Set P} {τ : P → ℝ}
    (h : (sv_flat M v₀).IsCauchyTemporalOn U τ) : (sh_flat M v₀).IsCauchyTemporalOn U τ := by
  obtain ⟨⟨h1, h2⟩, h3⟩ := h
  exact ⟨⟨h1, fun x hx v hv => h2 x hx v hv⟩, fun c a =>
    h3 ⟨c.γ, c.cont, c.mem, c.brk, c.brk_fin, c.causal, c.inext_future, c.inext_past⟩ a⟩

include hM in
/-- **The retarded slicing is Cauchy temporal on `D`** in the extended model, `0 < η ≤ 2`
(campaign 101's `sv_cauchy_flat`, transferred, then conformal invariance). -/
theorem sh_cauchy_D {a η v₀ : ℝ} (ha : 0 < a) (hη : 0 < η) (hη2 : η ≤ 2) :
    (sh_S hM v₀).IsCauchyTemporalOn ((sh_S hM v₀).D (range (sv_O M v₀))) (sv_Θsh M a η v₀) := by
  rw [sh_D hM]
  exact (sh_flat M v₀).cz_scale_isCauchyTemporalOn (sh_Φ_pos hM v₀)
    (sh_cauchy_transfer (sv_cauchy_flat hM ha hη hη2))

include hM in
/-- **Headline `sh_headline_D` (BUILT).** On the extended shell model: `D = I⁻(O) = {ũ < u_H}`,
`J⁻(O) = D`, `∂D = 𝓗⁺ = {ũ = u_H}` (the frontier in `P`), `𝓗⁺ ⊆ M′` and non-empty, and the
retarded slicing `Θ_shell` is Cauchy temporal on `D` for `0 < η ≤ 2`. -/
theorem sh_headline_D (v₀ : ℝ) :
    (sh_S hM v₀).D (range (sv_O M v₀)) = {y : P | y.1 < sv_uH M v₀} ∧
    (sh_S hM v₀).JpastSet (range (sv_O M v₀)) = (sh_S hM v₀).D (range (sv_O M v₀)) ∧
    (sh_S hM v₀).H (range (sv_O M v₀)) = {y : P | y.1 = sv_uH M v₀} ∧
    (sh_S hM v₀).H (range (sv_O M v₀)) ⊆ (sh_S hM v₀).M ∧
    ((sh_S hM v₀).H (range (sv_O M v₀))).Nonempty ∧
    ∀ a η : ℝ, 0 < a → 0 < η → η ≤ 2 →
      (sh_S hM v₀).IsCauchyTemporalOn ((sh_S hM v₀).D (range (sv_O M v₀))) (sv_Θsh M a η v₀) := by
  refine ⟨sh_D hM v₀, by rw [sh_Jpast hM, sh_D hM], sh_frontier hM v₀, ?_, ?_,
    fun a η ha hη hη2 => sh_cauchy_D hM ha hη hη2⟩
  · rw [sh_frontier hM]; exact sh_H_sub hM v₀
  · rw [sh_frontier hM]; exact ⟨(sv_uH M v₀, 0), rfl⟩

/-! ### Non-vacuity -/

/-- **Non-vacuity (BUILT)** at `M = 1`, `v₀ = 0` (`u_H = −4`): `(−4, −1) ∈ 𝓗⁺` with `Φ′ = 1`
(inside the flat body); `(−4, 1) ∈ 𝓗⁺` with `r = 2M`; `(−3, 0) ∈ M′ ∖ D` (the black-hole side);
`Φ′(−5, 1) > 1` (not flat); and Cauchy on `D` at `η = 2`. -/
theorem sh_nonvacuous :
    ((-4 : ℝ), (-1 : ℝ)) ∈ (sh_S one_pos 0).H (range (sv_O 1 0)) ∧
      sh_Φ 1 0 ((-4 : ℝ), (-1 : ℝ)) = 1 ∧
    ((-4 : ℝ), (1 : ℝ)) ∈ (sh_S one_pos 0).H (range (sv_O 1 0)) ∧
      sv_r 1 0 ((-4 : ℝ), (1 : ℝ)) = 2 * 1 ∧
    ((-3 : ℝ), (0 : ℝ)) ∈ (sh_S one_pos 0).M ∧
      ((-3 : ℝ), (0 : ℝ)) ∉ (sh_S one_pos 0).D (range (sv_O 1 0)) ∧
    1 < sh_Φ 1 0 ((-5 : ℝ), (1 : ℝ)) ∧
    (sh_S one_pos 0).IsCauchyTemporalOn ((sh_S one_pos 0).D (range (sv_O 1 0))) (sv_Θsh 1 1 2 0) := by
  have hH : ∀ v : ℝ, ((-4 : ℝ), v) ∈ (sh_S one_pos 0).H (range (sv_O 1 0)) := fun v => by
    rw [sh_frontier one_pos]; show (-4 : ℝ) = sv_uH 1 0; unfold sv_uH; norm_num
  have hu : ((-4 : ℝ), (-1 : ℝ)).1 = sv_uH 1 0 := by show (-4 : ℝ) = sv_uH 1 0; unfold sv_uH; norm_num
  have hu' : ((-4 : ℝ), (1 : ℝ)).1 = sv_uH 1 0 := by show (-4 : ℝ) = sv_uH 1 0; unfold sv_uH; norm_num
  refine ⟨hH _, sh_H_flat one_pos hu (by norm_num), hH _, sh_H_r one_pos hu',
    sh_shell_mem one_pos (v₀ := 0) (ũ := -3) (by norm_num), ?_, ?_,
    sh_cauchy_D one_pos one_pos (by norm_num) le_rfl⟩
  · rw [sh_D one_pos]; show ¬ (-3 : ℝ) < sv_uH 1 0; unfold sv_uH; norm_num
  · rw [sh_agree one_pos sv_mem5']; exact sv_Φ_gt_one one_pos sv_mem5' one_pos

end SHModel

/-! ## NEW (campaign 105): the collapsing matter on the shell model -/

namespace SMModel
open Model SEModel SRModel SVModel SHModel Kruskal Manifold ContinuousLinearMap TopologicalSpace

set_option synthInstance.maxHeartbeats 400000

variable {M : ℝ} (hM : 0 < M)

/-! ### The matter and the shell ray -/

/-- **The matter `𝔐 = {v = v₀} ∩ M′` — a modelling choice, not a derivation.** The kit has no
stress-energy tensor, so "the matter" is read off where the metric changes form (`sh_flat_past`
for `v ≤ v₀`, `sh_vacuum` for `v ≥ v₀`): the thin shell `v = v₀`. In the radial plane each point of
it is one infalling element (not a 2-sphere's worth). -/
def sm_matter (M v₀ : ℝ) : Set P := {y | y.2 = v₀} ∩ sh_MS M v₀

/-- **The shell ray** `γ(s) = (u_H − e^{−s}, v₀)`: the ingoing worldline of a shell element. -/
noncomputable def sm_γ (M v₀ s : ℝ) : P := (sv_uH M v₀ - Real.exp (-s), v₀)

/-- `γ` is smooth with velocity `(e^{−s}, 0)`. -/
lemma sm_γ_hasDerivAt (M v₀ s : ℝ) :
    HasDerivAt (sm_γ M v₀) ((Real.exp (-s), (0 : ℝ)) : P) s := by
  have h1 : HasDerivAt (fun s : ℝ => sv_uH M v₀ - Real.exp (-s)) (Real.exp (-s)) s := by
    have h := ((Real.hasDerivAt_exp (-s)).comp s (hasDerivAt_neg s)).const_sub (sv_uH M v₀)
    rw [show Real.exp (-s) = -(Real.exp (-s) * -1) by ring]; exact h
  exact h1.prodMk (hasDerivAt_const s v₀)

lemma sm_γ_contDiff (M v₀ : ℝ) : ContDiff ℝ ⊤ (sm_γ M v₀) := by
  unfold sm_γ; fun_prop

lemma sm_γ_lt (M v₀ s : ℝ) : (sm_γ M v₀ s).1 < sv_uH M v₀ := by
  show sv_uH M v₀ - Real.exp (-s) < sv_uH M v₀
  linarith [Real.exp_pos (-s)]

/-- The future end: `γ(s) → (u_H, v₀)`, the element's horizon event. -/
lemma sm_γ_tendsto (M v₀ : ℝ) :
    Tendsto (sm_γ M v₀) atTop (𝓝 ((sv_uH M v₀, v₀) : P)) := by
  have h := Real.tendsto_exp_neg_atTop_nhds_zero.const_sub (sv_uH M v₀)
  rw [sub_zero] at h
  exact h.prodMk_nhds tendsto_const_nhds

/-- The past end: `ũ → −∞`. -/
lemma sm_γ_atBot (M v₀ : ℝ) : Tendsto (fun s => (sm_γ M v₀ s).1) atBot atBot := by
  have h : Tendsto (fun s : ℝ => -Real.exp (-s)) atBot atBot :=
    tendsto_neg_atTop_atBot.comp (Real.tendsto_exp_atTop.comp tendsto_neg_atBot_atTop)
  exact (tendsto_atBot_add_const_left _ (sv_uH M v₀) h).congr fun s => by
    simp [sm_γ, sub_eq_add_neg]

lemma sm_futCausal_iff (M v₀ : ℝ) (x v : P) :
    (sh_flat M v₀).FutCausal x v ↔ 0 ≤ v.1 ∧ 0 ≤ v.2 ∧ 0 < v.1 + v.2 :=
  futCausal_iff x v

/-- **The shell ray as an inextendible causal curve in `D` (BUILT, the registered expected
stop).** `C^∞`, no breaks, velocity `(e^{−s}, 0)` (future null for `−Φ′ dũ dv`, `T = (1, 1)`),
inside `D = {ũ < u_H}`; no limit in `D` to the future (`γ → (u_H, v₀) ∉ D`) or to the past
(`ũ → −∞`). -/
noncomputable def sm_curve (v₀ : ℝ) :
    (sh_S hM v₀).InextCausalCurveIn ((sh_S hM v₀).D (range (sv_O M v₀))) where
  γ := sm_γ M v₀
  cont := (sm_γ_contDiff M v₀).continuous
  mem := fun t => by rw [sh_D hM]; exact sm_γ_lt M v₀ t
  brk := ∅
  brk_fin := fun _ _ => by simp
  causal := fun t _ => ⟨mdifferentiableAt_iff_differentiableAt.2
      (sm_γ_hasDerivAt M v₀ t).differentiableAt, by
    rw [sv_vel_eq, (sm_γ_hasDerivAt M v₀ t).deriv, sh_S, MSpacetime.cz_scale_futCausal,
      sm_futCausal_iff]
    exact ⟨(Real.exp_pos _).le, le_rfl, by simp [Real.exp_pos]⟩⟩
  inext_future := by
    rintro ⟨p, hp, hlim⟩
    have e := tendsto_nhds_unique hlim (sm_γ_tendsto M v₀)
    rw [sh_D hM, e] at hp
    exact lt_irrefl _ (show sv_uH M v₀ < sv_uH M v₀ from hp)
  inext_past := by
    rintro ⟨p, -, hlim⟩
    have h : Tendsto (fun t => (sm_γ M v₀ t).1) atBot (𝓝 p.1) :=
      (continuous_fst.tendsto p).comp hlim
    exact not_tendsto_nhds_of_tendsto_atBot (sm_γ_atBot M v₀) _ h

lemma sm_curve_γ (v₀ : ℝ) : (sm_curve hM v₀).γ = sm_γ M v₀ := rfl

include hM in
/-- **The matter in `D` is exactly the shell ray:** `𝔐 ∩ D = range γ`. -/
lemma sm_matter_D (v₀ : ℝ) :
    (sh_S hM v₀).D (range (sv_O M v₀)) ∩ sm_matter M v₀ = range (sm_γ M v₀) := by
  rw [sh_D hM]
  apply Subset.antisymm
  · rintro y ⟨h1, h2, -⟩
    have h1' : y.1 < sv_uH M v₀ := h1
    have hp : 0 < sv_uH M v₀ - y.1 := by linarith
    refine ⟨-Real.log (sv_uH M v₀ - y.1), ?_⟩
    show ((sv_uH M v₀ - Real.exp (- -Real.log (sv_uH M v₀ - y.1)), v₀) : P) = y
    rw [neg_neg, Real.exp_log hp]
    ext
    · show sv_uH M v₀ - (sv_uH M v₀ - y.1) = y.1; ring
    · exact h2.symm
  · rintro _ ⟨s, rfl⟩
    exact ⟨sm_γ_lt M v₀ s, rfl, sh_sv_sub hM (sm_γ_lt M v₀ s)⟩

include hM in
/-- **The slicing along the shell ray, explicitly:**
`Θ(γ(s)) = a(4M s + (η/2 − 1) e^{−s} + v₀ − 4M + 4M log 4M + 2Mη)`. -/
lemma sm_Θ_γ (a η v₀ s : ℝ) :
    sv_Θsh M a η v₀ (sm_γ M v₀ s) =
      a * (4 * M * s + (η / 2 - 1) * Real.exp (-s) +
        (v₀ - 4 * M + 4 * M * Real.log (4 * M) + 2 * M * η)) := by
  have hmem : sm_γ M v₀ s ∈ sv_MS M v₀ := sm_γ_lt M v₀ s
  rw [sv_retarded_eq hM hmem (le_refl v₀)]
  have hlt : (sm_γ M v₀ s).1 < v₀ := by
    have := sm_γ_lt M v₀ s; unfold sv_uH at this; linarith
  have hr : sv_r M v₀ (sm_γ M v₀ s) = (v₀ - (sm_γ M v₀ s).1) / 2 := sh_r_shell hM hlt
  rw [hr]
  have hM' : M ≠ 0 := hM.ne'
  have e1 : (v₀ - (sv_uH M v₀ - Real.exp (-s))) / (4 * M) - 1 = Real.exp (-s) / (4 * M) := by
    unfold sv_uH; field_simp; ring
  have e2 : Real.log (Real.exp (-s) / (4 * M)) = -s - Real.log (4 * M) := by
    rw [Real.log_div (Real.exp_pos _).ne' (by positivity), Real.log_exp]
  show a * (sv_F M v₀ (sv_uH M v₀ - Real.exp (-s)) +
    η * ((v₀ - (sv_uH M v₀ - Real.exp (-s))) / 2)) = _
  unfold sv_F
  rw [e1, e2]
  unfold sv_uH
  ring

include hM in
/-- **`Θ ∘ γ` is strictly increasing** (`0 < a`, `η ≤ 2`). -/
lemma sm_Θ_γ_strictMono {a η : ℝ} (ha : 0 < a) (hη2 : η ≤ 2) (v₀ : ℝ) :
    StrictMono (fun s => sv_Θsh M a η v₀ (sm_γ M v₀ s)) := by
  intro s t hst
  simp only [sm_Θ_γ hM]
  have h1 : Real.exp (-t) < Real.exp (-s) := Real.exp_lt_exp.2 (by linarith)
  have h2 : (η / 2 - 1) * Real.exp (-s) ≤ (η / 2 - 1) * Real.exp (-t) :=
    mul_le_mul_of_nonpos_left h1.le (by linarith)
  have h3 : 4 * M * s < 4 * M * t := by nlinarith
  exact mul_lt_mul_of_pos_left (by linarith) ha

/-- **The slice parameter** `s_τ`: the parameter of the shell ray on the slice `Θ = τ`. -/
noncomputable def sm_sτ (M a η v₀ τ : ℝ) : ℝ :=
  Classical.epsilon fun s => sv_Θsh M a η v₀ (sm_γ M v₀ s) = τ

include hM in
/-- **The shell ray meets each slice exactly once** (`sh_cauchy_D` on `sm_curve`). -/
theorem sm_param {a η : ℝ} (ha : 0 < a) (hη : 0 < η) (hη2 : η ≤ 2) (v₀ τ : ℝ) :
    ∃! s : ℝ, sv_Θsh M a η v₀ (sm_γ M v₀ s) = τ :=
  (sh_cauchy_D hM ha hη hη2).2 (sm_curve hM v₀) τ

include hM in
lemma sm_sτ_spec {a η : ℝ} (ha : 0 < a) (hη : 0 < η) (hη2 : η ≤ 2) (v₀ τ : ℝ) :
    sv_Θsh M a η v₀ (sm_γ M v₀ (sm_sτ M a η v₀ τ)) = τ :=
  Classical.epsilon_spec (sm_param hM ha hη hη2 v₀ τ).exists

include hM in
/-- **① `sm_slice_meets_matter` (BUILT):** for `0 < a`, `0 < η ≤ 2` and every `τ`, the slice
`S_τ` meets the matter in exactly one point, `γ(s_τ)`. -/
theorem sm_slice_meets_matter {a η : ℝ} (ha : 0 < a) (hη : 0 < η) (hη2 : η ≤ 2) (v₀ τ : ℝ) :
    (∃! y : P, y ∈ (sh_S hM v₀).slice (range (sv_O M v₀)) (sv_Θsh M a η v₀) τ ∩ sm_matter M v₀) ∧
    sm_γ M v₀ (sm_sτ M a η v₀ τ) ∈
      (sh_S hM v₀).slice (range (sv_O M v₀)) (sv_Θsh M a η v₀) τ ∩ sm_matter M v₀ ∧
    (sh_S hM v₀).D (range (sv_O M v₀)) ∩ sm_matter M v₀ = range (sm_γ M v₀) := by
  have hmem : sm_γ M v₀ (sm_sτ M a η v₀ τ) ∈
      (sh_S hM v₀).slice (range (sv_O M v₀)) (sv_Θsh M a η v₀) τ ∩ sm_matter M v₀ := by
    have h := (sm_matter_D hM v₀).symm ▸ mem_range_self (sm_sτ M a η v₀ τ)
    exact ⟨⟨h.1, sm_sτ_spec hM ha hη hη2 v₀ τ⟩, h.2⟩
  refine ⟨⟨_, hmem, fun y hy => ?_⟩, hmem, sm_matter_D hM v₀⟩
  obtain ⟨s, rfl⟩ : y ∈ range (sm_γ M v₀) := sm_matter_D hM v₀ ▸ ⟨hy.1.1, hy.2⟩
  rw [(sm_param hM ha hη hη2 v₀ τ).unique hy.1.2 (sm_sτ_spec hM ha hη hη2 v₀ τ)]

include hM in
/-- **`sm_outside_H` (BUILT):** `S_τ ∩ 𝔐 ∩ 𝓗⁺ = ∅` (slices lie in `D = {ũ < u_H}`,
`𝓗⁺ = {ũ = u_H}`). -/
theorem sm_outside_H (Θ : P → ℝ) (v₀ τ : ℝ) :
    (sh_S hM v₀).slice (range (sv_O M v₀)) Θ τ ∩ sm_matter M v₀ ∩
      (sh_S hM v₀).H (range (sv_O M v₀)) = ∅ := by
  ext y
  simp only [mem_inter_iff, mem_empty_iff_false, iff_false, not_and]
  intro hs hH
  have h1 := hs.1.1
  rw [sh_D hM] at h1
  rw [sh_frontier hM] at hH
  have h1' : y.1 < sv_uH M v₀ := h1
  have hH' : y.1 = sv_uH M v₀ := hH
  linarith

include hM in
/-- **② `sm_finite` (BUILT):** at the slice point `y = γ(s_τ)`, `r = (v₀ − ũ)/2` and `2M < r`;
`S_τ ∩ 𝔐 = {y}`, so it is compact. -/
theorem sm_finite {a η : ℝ} (ha : 0 < a) (hη : 0 < η) (hη2 : η ≤ 2) (v₀ τ : ℝ) :
    ∃ y : P, y = sm_γ M v₀ (sm_sτ M a η v₀ τ) ∧
      (sh_S hM v₀).slice (range (sv_O M v₀)) (sv_Θsh M a η v₀) τ ∩ sm_matter M v₀ = {y} ∧
      sv_r M v₀ y = (v₀ - y.1) / 2 ∧ 2 * M < sv_r M v₀ y ∧
      IsCompact ((sh_S hM v₀).slice (range (sv_O M v₀)) (sv_Θsh M a η v₀) τ ∩ sm_matter M v₀) := by
  obtain ⟨⟨y₀, hy₀, huniq⟩, hmem, -⟩ := sm_slice_meets_matter hM ha hη hη2 v₀ τ
  have hsing : (sh_S hM v₀).slice (range (sv_O M v₀)) (sv_Θsh M a η v₀) τ ∩ sm_matter M v₀ =
      {sm_γ M v₀ (sm_sτ M a η v₀ τ)} := by
    ext y
    refine ⟨fun hy => ?_, fun hy => by rw [mem_singleton_iff.1 hy]; exact hmem⟩
    rw [mem_singleton_iff, huniq y hy, huniq _ hmem]
  have hlt := sm_γ_lt M v₀ (sm_sτ M a η v₀ τ)
  have h2 : sv_uH M v₀ - Real.exp (-sm_sτ M a η v₀ τ) < v₀ := by
    have := Real.exp_pos (-sm_sτ M a η v₀ τ); unfold sv_uH; linarith
  exact ⟨_, rfl, hsing, sh_r_shell hM h2, sv_r_gt hM hlt, by rw [hsing]; exact isCompact_singleton⟩

include hM in
/-- **③ `sm_approaches` (BUILT):** `γ(s) → (u_H, v₀) ∈ 𝓗⁺`, where `r = 2M`; `Θ(γ(s)) → ∞`;
`s_τ` is strictly increasing in `τ` and `s_τ → ∞`; on every slice the element is short of its
horizon event (`ũ(γ(s_τ)) < u_H`), and `γ(s_τ) → (u_H, v₀)` only as `τ → ∞`. -/
theorem sm_approaches {a η : ℝ} (ha : 0 < a) (hη : 0 < η) (hη2 : η ≤ 2) (v₀ : ℝ) :
    Tendsto (sm_γ M v₀) atTop (𝓝 ((sv_uH M v₀, v₀) : P)) ∧
    ((sv_uH M v₀, v₀) : P) ∈ (sh_S hM v₀).H (range (sv_O M v₀)) ∧
    sv_r M v₀ ((sv_uH M v₀, v₀) : P) = 2 * M ∧
    Tendsto (fun s => sv_Θsh M a η v₀ (sm_γ M v₀ s)) atTop atTop ∧
    StrictMono (sm_sτ M a η v₀) ∧
    Tendsto (sm_sτ M a η v₀) atTop atTop ∧
    (∀ τ, (sm_γ M v₀ (sm_sτ M a η v₀ τ)).1 < sv_uH M v₀) ∧
    Tendsto (fun τ => sm_γ M v₀ (sm_sτ M a η v₀ τ)) atTop (𝓝 ((sv_uH M v₀, v₀) : P)) := by
  have hf := sm_Θ_γ_strictMono hM ha hη2 v₀
  have hspec := sm_sτ_spec hM ha hη hη2 v₀
  have hinv : ∀ s, sm_sτ M a η v₀ (sv_Θsh M a η v₀ (sm_γ M v₀ s)) = s := fun s =>
    hf.injective (hspec _)
  have hmono : StrictMono (sm_sτ M a η v₀) := fun τ τ' h => by
    rw [← hf.lt_iff_lt, hspec, hspec]; exact h
  have hsτ : Tendsto (sm_sτ M a η v₀) atTop atTop :=
    tendsto_atTop_atTop_of_monotone hmono.monotone fun b => ⟨_, (hinv b).ge⟩
  refine ⟨sm_γ_tendsto M v₀, ?_, sh_H_r hM rfl,
    tendsto_atTop_atTop_of_monotone hf.monotone fun b =>
      ⟨sm_sτ M a η v₀ b, (hspec b).ge⟩, hmono, hsτ, fun τ => sm_γ_lt M v₀ _,
    (sm_γ_tendsto M v₀).comp hsτ⟩
  rw [sh_frontier hM]; rfl

/-- **Non-vacuity (BUILT)** at `M = 1`, `v₀ = 0`, `a = 1`, `η = 2`: the matter on the slice
`τ = 0` is the single point `(−8, 0) = γ(−log 4)`, with `r = 4 > 2`. -/
theorem sm_nonvacuous :
    (sh_S one_pos 0).slice (range (sv_O 1 0)) (sv_Θsh 1 1 2 0) 0 ∩ sm_matter 1 0 =
      {((-8 : ℝ), (0 : ℝ))} ∧
    sv_r 1 0 ((-8 : ℝ), (0 : ℝ)) = 4 ∧ 2 * 1 < sv_r 1 0 ((-8 : ℝ), (0 : ℝ)) := by
  have hγ : sm_γ 1 0 (-Real.log 4) = ((-8 : ℝ), (0 : ℝ)) := by
    show ((sv_uH 1 0 - Real.exp (- -Real.log 4), 0) : P) = _
    rw [neg_neg, Real.exp_log (by norm_num)]; unfold sv_uH; norm_num
  have hΘ : sv_Θsh 1 1 2 0 (sm_γ 1 0 (-Real.log 4)) = 0 := by
    rw [sm_Θ_γ one_pos]; simp only [mul_one]; ring
  have hs : sm_sτ 1 1 2 0 0 = -Real.log 4 :=
    (sm_Θ_γ_strictMono one_pos one_pos le_rfl 0).injective
      ((sm_sτ_spec one_pos one_pos (by norm_num) le_rfl 0 0).trans hΘ.symm)
  obtain ⟨y, hy, hset, hr, hgt, -⟩ := sm_finite one_pos one_pos (by norm_num) le_rfl 0 0
  rw [hs, hγ] at hy
  subst hy
  refine ⟨hset, ?_, hgt⟩
  rw [hr]; norm_num

end SMModel

/-! ## NEW (campaign 108): the slices and the past cones accumulate on `𝓗⁺` alone, on the shell -/

section SA2Generic
open Manifold
set_option linter.unusedSectionVars false

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
variable {N : Type*} [TopologicalSpace N] [ChartedSpace E N] [IsManifold 𝓘(ℝ, E) 1 N]

namespace MSpacetime

/-! ### Campaign 91's `cd_cone_disjoint`, copied from `ConeDisjoint.lean` (renamed `sa2_`) -/

/-- (`cd_chr_of_mem_closure_Jpast`) `x ∈ closure J⁻(p)` and `y ≪ x` give `y ≪ p`. -/
theorem sa2_chr_of_mem_closure_Jpast {S : MSpacetime E N} (hL : S.LocallyOneChart) {p x y : N}
    (hx : x ∈ closure (S.Jpast p)) (hyx : S.Chr y x) : S.Chr y p := by
  obtain ⟨w, hyw, hwp⟩ := mem_closure_iff_nhds.1 hx _ ((S.mk_isOpen_Ifut hL y).mem_nhds hyx)
  exact S.mk_pushup' hL hyw hwp

/-- (`cd_mem_closure_sublevel`) `closure J⁻(p) ∩ M` lies in a sublevel closure. -/
theorem sa2_mem_closure_sublevel {S : MSpacetime E N} (hL : S.LocallyOneChart) {J : Set N}
    {Θ : N → ℝ} (hΘ : S.IsTemporalOn (S.D J) Θ) {p x : N} (hp : p ∈ S.D J) (hxM : x ∈ S.M)
    (hx : x ∈ closure (S.Jpast p)) : x ∈ closure {y | y ∈ S.D J ∧ Θ y ≤ Θ p} := by
  rw [mem_closure_iff_nhds]
  intro U hU
  obtain ⟨y, hyU, hyx⟩ := S.mh_past_step hL hxM hU
  have hyp := sa2_chr_of_mem_closure_Jpast hL hx hyx
  exact ⟨y, hyU, S.mh_D_of_chr hyp hp, (S.mh_temporalD_chr hL hΘ hyp hp).le⟩

/-- (`cd_closure_Jpast_subset_D`) `closure J⁻(p) ∩ M ⊆ D` for `p ∈ D`, from properness. -/
theorem sa2_closure_Jpast_subset_D {S : MSpacetime E N} (hL : S.LocallyOneChart) {J : Set N}
    {Θ : N → ℝ} (hΘ : S.IsTemporalOn (S.D J) Θ) (hP : S.SublevelProper J Θ) {p : N}
    (hp : p ∈ S.D J) : closure (S.Jpast p) ∩ S.M ⊆ S.D J := fun _ hx =>
  hP (Θ p) (sa2_mem_closure_sublevel hL hΘ hp hx.2 hx.1)

/-- (`cd_closure_Jpast_inter_H`) `closure J⁻(O τ) ∩ 𝓗⁺ = ∅`. -/
theorem sa2_closure_Jpast_inter_H {S : MSpacetime E N} (hL : S.LocallyOneChart) {J : Set N}
    {O : ℝ → N} (hOD : S.IpastSet (range O) = S.D J)
    (hmono : ∀ s t : ℝ, s < t → S.Chr (O s) (O t)) (hHM : S.H J ⊆ S.M) {Θ : N → ℝ}
    (hΘ : S.IsTemporalOn (S.D J) Θ) (hP : S.SublevelProper J Θ) (τ : ℝ) :
    closure (S.Jpast (O τ)) ∩ S.H J = ∅ := by
  refine eq_empty_iff_forall_notMem.2 fun x hx => S.mh_not_mem_D_of_H hL hx.2 ?_
  exact sa2_closure_Jpast_subset_D hL hΘ hP (mh_observer_mem_D hOD hmono τ) ⟨hx.1, hHM hx.2⟩

/-- (`cd_cone_disjoint`) **No past light cone meets `𝓗⁺`**: `S.cone O τ ∩ 𝓗⁺ = ∅`. -/
theorem sa2_cone_disjoint [T2Space N] {S : MSpacetime E N} (hL : S.LocallyOneChart) {J : Set N}
    {O : ℝ → N} (hOD : S.IpastSet (range O) = S.D J)
    (hmono : ∀ s t : ℝ, s < t → S.Chr (O s) (O t)) (hJM : J ⊆ S.M) (hHM : S.H J ⊆ S.M)
    {Θ : N → ℝ} (hΘ : S.IsCauchyTemporalOn (S.D J) Θ) :
    ∀ τ, S.cone O τ ∩ S.H J = ∅ := by
  have hF : S.FutCauchyTemporalOn (S.D J) Θ :=
    me_futCauchy_of_cauchy_N hL (S.mk_isOpen_D hL J) (S.D_subset_M J) hΘ
  have hP := S.mh_sublevelProper hL (S.mh_hint hL hJM) hHM hF
  intro τ
  exact subset_empty_iff.1 fun x hx =>
    (sa2_closure_Jpast_inter_H hL hOD hmono hHM hΘ.1 hP τ).subset
      ⟨frontier_subset_closure hx.1, hx.2⟩

end MSpacetime

end SA2Generic

namespace SA2Model
open Model SEModel SRModel SVModel SHModel Kruskal Manifold ContinuousLinearMap TopologicalSpace

set_option synthInstance.maxHeartbeats 400000

variable {M : ℝ} (hM : 0 < M)

/-! ### ① The flat ingredients -/

/-- **`sh_flat` is `LocallyOneChart`** (`cz_locallyOneChart`, restricted to `M′`). -/
theorem sa2_flat_locallyOneChart (M v₀ : ℝ) : (sh_flat M v₀).LocallyOneChart :=
  NModel.cz_locallyOneChart.restrict (sh_MS_open M v₀) (subset_univ _)

/-- `sh_S = sh_flat.cz_scale Φ′` has `sh_flat`'s causal data. -/
lemma sa2_S_chr (v₀ : ℝ) : (sh_S hM v₀).Chr = (sh_flat M v₀).Chr := by
  rw [sh_S, MSpacetime.cz_scale_chr]

lemma sa2_S_D (v₀ : ℝ) : (sh_S hM v₀).D = (sh_flat M v₀).D := by
  rw [sh_S, MSpacetime.cz_scale_D]

lemma sa2_S_H (v₀ : ℝ) : (sh_S hM v₀).H = (sh_flat M v₀).H := by
  rw [sh_S, MSpacetime.cz_scale_H]

lemma sa2_S_slice (v₀ : ℝ) : (sh_S hM v₀).slice = (sh_flat M v₀).slice := by
  rw [sh_S, MSpacetime.cz_scale_slice]

lemma sa2_S_cone (v₀ : ℝ) : (sh_S hM v₀).cone = (sh_flat M v₀).cone := by
  rw [sh_S, MSpacetime.cz_scale_cone]

lemma sa2_S_sublevelProper (v₀ : ℝ) :
    (sh_S hM v₀).SublevelProper = (sh_flat M v₀).SublevelProper := by
  rw [sh_S, MSpacetime.cz_scale_sublevelProper]

include hM in
/-- **The flat causal data are campaign 102's:** `D = J⁻(O) = {ũ < u_H}`, `𝓗⁺ = {ũ = u_H} ⊆ M′`,
and `O` is chronologically increasing, all on `sh_flat`. -/
theorem sa2_flat_causal (v₀ : ℝ) :
    (sh_flat M v₀).D (range (sv_O M v₀)) = {y : P | y.1 < sv_uH M v₀} ∧
    (sh_flat M v₀).H (range (sv_O M v₀)) = {y : P | y.1 = sv_uH M v₀} ∧
    (sh_flat M v₀).H (range (sv_O M v₀)) ⊆ (sh_flat M v₀).M ∧
    range (sv_O M v₀) ⊆ (sh_flat M v₀).M ∧
    ∀ s t : ℝ, s < t → (sh_flat M v₀).Chr (sv_O M v₀ s) (sv_O M v₀ t) := by
  have hD := sh_D hM v₀
  have hH := sh_frontier hM v₀
  rw [sa2_S_D hM] at hD
  rw [sa2_S_H hM] at hH
  refine ⟨hD, hH, by rw [hH]; exact sh_H_sub hM v₀, (sh_O hM v₀).1, fun s t hst => ?_⟩
  rw [← sa2_S_chr hM]; exact (sh_O hM v₀).2.1 s t hst

include hM in
/-- **Cauchy on the flat `D`:** `Θ_shell` is Cauchy temporal on `sh_flat`'s `D`, `0 < η ≤ 2`
(campaign 101's `sv_cauchy_flat`, through `sh_cauchy_transfer`). -/
theorem sa2_flat_cauchy {a η : ℝ} (ha : 0 < a) (hη : 0 < η) (hη2 : η ≤ 2) (v₀ : ℝ) :
    (sh_flat M v₀).IsCauchyTemporalOn ((sh_flat M v₀).D (range (sv_O M v₀)))
      (sv_Θsh M a η v₀) := by
  rw [(sa2_flat_causal hM v₀).1]
  exact sh_cauchy_transfer (sv_cauchy_flat hM ha hη hη2)

/-! ### ② The adapted observer -/

/-- `O(τ) = (u_H − e^{−τ}, τ)` has velocity `(e^{−τ}, 1)`. -/
lemma sa2_O_hasDerivAt (M v₀ τ : ℝ) :
    HasDerivAt (sv_O M v₀) ((Real.exp (-τ), (1 : ℝ)) : P) τ := by
  have h1 : HasDerivAt (fun s : ℝ => sv_uH M v₀ - Real.exp (-s)) (Real.exp (-τ)) τ := by
    have h := ((Real.hasDerivAt_exp (-τ)).comp τ (hasDerivAt_neg τ)).const_sub (sv_uH M v₀)
    rw [show Real.exp (-τ) = -(Real.exp (-τ) * -1) by ring]; exact h
  exact h1.prodMk (hasDerivAt_id τ)

lemma sa2_O_continuous (M v₀ : ℝ) : Continuous (sv_O M v₀) := by
  unfold sv_O; fun_prop

lemma sa2_O_lt (M v₀ τ : ℝ) : (sv_O M v₀ τ).1 < sv_uH M v₀ := by
  show sv_uH M v₀ - Real.exp (-τ) < sv_uH M v₀
  linarith [Real.exp_pos (-τ)]

lemma sa2_O_atBot (M v₀ : ℝ) : Tendsto (fun τ => (sv_O M v₀ τ).1) atBot atBot := by
  have h : Tendsto (fun s : ℝ => -Real.exp (-s)) atBot atBot :=
    tendsto_neg_atTop_atBot.comp (Real.tendsto_exp_atTop.comp tendsto_neg_atBot_atTop)
  exact (tendsto_atBot_add_const_left _ (sv_uH M v₀) h).congr fun s => by
    simp [sv_O, sub_eq_add_neg]

/-- **The observer as an inextendible causal curve in `sh_flat`'s `D`.** `C^∞`, no breaks,
velocity `(e^{−τ}, 1)` (future timelike); `v = τ → ∞` to the future and `ũ → −∞` to the past, so
no limit in `D` at either end. -/
noncomputable def sa2_curve (v₀ : ℝ) :
    (sh_flat M v₀).InextCausalCurveIn ((sh_flat M v₀).D (range (sv_O M v₀))) where
  γ := sv_O M v₀
  cont := sa2_O_continuous M v₀
  mem := fun t => by rw [(sa2_flat_causal hM v₀).1]; exact sa2_O_lt M v₀ t
  brk := ∅
  brk_fin := fun _ _ => by simp
  causal := fun t _ => ⟨mdifferentiableAt_iff_differentiableAt.2
      (sa2_O_hasDerivAt M v₀ t).differentiableAt, by
    rw [sv_vel_eq, (sa2_O_hasDerivAt M v₀ t).deriv]
    refine (futCausal_iff (sv_O M v₀ t) _).2 ⟨(Real.exp_pos _).le, zero_le_one, ?_⟩
    show 0 < Real.exp (-t) + 1
    linarith [Real.exp_pos (-t)]⟩
  inext_future := by
    rintro ⟨p, -, hlim⟩
    have h : Tendsto (fun t => (sv_O M v₀ t).2) atTop (𝓝 p.2) :=
      (continuous_snd.tendsto p).comp hlim
    exact not_tendsto_nhds_of_tendsto_atTop tendsto_id _ h
  inext_past := by
    rintro ⟨p, -, hlim⟩
    have h : Tendsto (fun t => (sv_O M v₀ t).1) atBot (𝓝 p.1) :=
      (continuous_fst.tendsto p).comp hlim
    exact not_tendsto_nhds_of_tendsto_atBot (sa2_O_atBot M v₀) _ h

/-- **The clock read along the observer**, `g(τ) = Θ_shell(O(τ))`. -/
noncomputable def sa2_g (M a η v₀ τ : ℝ) : ℝ := sv_Θsh M a η v₀ (sv_O M v₀ τ)

include hM in
/-- **`g` is strictly increasing** (`Θ_shell` is temporal on `D`, `O` chronological:
`mh_temporalD_chr`). -/
theorem sa2_g_strictMono {a η : ℝ} (ha : 0 < a) (hη : 0 < η) (hη2 : η ≤ 2) (v₀ : ℝ) :
    StrictMono (sa2_g M a η v₀) := fun s t hst =>
  (sh_flat M v₀).mh_temporalD_chr (sa2_flat_locallyOneChart M v₀)
    (sa2_flat_cauchy hM ha hη hη2 v₀).1 ((sa2_flat_causal hM v₀).2.2.2.2 s t hst)
    ((sa2_curve hM v₀).mem t)

include hM in
/-- **`g` is onto `ℝ`** (Cauchy: the inextendible `O` meets every level set). -/
theorem sa2_g_surjective {a η : ℝ} (ha : 0 < a) (hη : 0 < η) (hη2 : η ≤ 2) (v₀ : ℝ) :
    Function.Surjective (sa2_g M a η v₀) := fun τ =>
  ((sa2_flat_cauchy hM ha hη hη2 v₀).2 (sa2_curve hM v₀) τ).exists

include hM in
/-- **`g` is continuous** (`Θ_shell` is `C¹` on `M = {ũ < u_H}`). -/
theorem sa2_g_continuous {a η : ℝ} (ha : 0 < a) (hη : 0 < η) (hη2 : η ≤ 2) (v₀ : ℝ) :
    Continuous (sa2_g M a η v₀) :=
  (sv_temporal hM ha hη hη2).1.continuousOn.comp_continuous (sa2_O_continuous M v₀)
    fun τ => sa2_O_lt M v₀ τ

/-- **`g⁻¹`**, by choice. -/
noncomputable def sa2_ginv (M a η v₀ τ : ℝ) : ℝ :=
  Classical.epsilon fun s => sa2_g M a η v₀ s = τ

include hM in
lemma sa2_g_ginv {a η : ℝ} (ha : 0 < a) (hη : 0 < η) (hη2 : η ≤ 2) (v₀ τ : ℝ) :
    sa2_g M a η v₀ (sa2_ginv M a η v₀ τ) = τ :=
  Classical.epsilon_spec (sa2_g_surjective hM ha hη hη2 v₀ τ)

include hM in
lemma sa2_ginv_g {a η : ℝ} (ha : 0 < a) (hη : 0 < η) (hη2 : η ≤ 2) (v₀ s : ℝ) :
    sa2_ginv M a η v₀ (sa2_g M a η v₀ s) = s :=
  (sa2_g_strictMono hM ha hη hη2 v₀).injective (sa2_g_ginv hM ha hη hη2 v₀ _)

include hM in
/-- **`g⁻¹` is a strictly increasing homeomorphism of `ℝ`.** -/
theorem sa2_ginv_strictMono {a η : ℝ} (ha : 0 < a) (hη : 0 < η) (hη2 : η ≤ 2) (v₀ : ℝ) :
    StrictMono (sa2_ginv M a η v₀) ∧ Function.Surjective (sa2_ginv M a η v₀) ∧
    Continuous (sa2_ginv M a η v₀) := by
  have hmono : StrictMono (sa2_ginv M a η v₀) := by
    intro s t hst
    by_contra h
    have := (sa2_g_strictMono hM ha hη hη2 v₀).monotone (not_lt.1 h)
    rw [sa2_g_ginv hM ha hη hη2, sa2_g_ginv hM ha hη hη2] at this
    linarith
  have hsurj : Function.Surjective (sa2_ginv M a η v₀) := fun s =>
    ⟨_, sa2_ginv_g hM ha hη hη2 v₀ s⟩
  exact ⟨hmono, hsurj, hmono.monotone.continuous_of_surjective hsurj⟩

/-- **The adapted observer** `O′ = O ∘ g⁻¹`. -/
noncomputable def sa2_O (M a η v₀ τ : ℝ) : P := sv_O M v₀ (sa2_ginv M a η v₀ τ)

include hM in
/-- **② `sa2_O_adapted` (BUILT, the registered expected stop):** `O′ = O ∘ g⁻¹` has the same
range as `O`, is chronologically increasing (on `sh_flat`, hence on `sh_S`), continuous, and
adapted: `Θ_shell(O′ τ) = τ`. Here `g = Θ_shell ∘ O` is continuous, strictly increasing and onto
`ℝ`. -/
theorem sa2_O_adapted {a η : ℝ} (ha : 0 < a) (hη : 0 < η) (hη2 : η ≤ 2) (v₀ : ℝ) :
    Continuous (sa2_g M a η v₀) ∧ StrictMono (sa2_g M a η v₀) ∧
    Function.Surjective (sa2_g M a η v₀) ∧
    range (sa2_O M a η v₀) = range (sv_O M v₀) ∧
    (∀ s t : ℝ, s < t → (sh_flat M v₀).Chr (sa2_O M a η v₀ s) (sa2_O M a η v₀ t)) ∧
    (∀ s t : ℝ, s < t → (sh_S hM v₀).Chr (sa2_O M a η v₀ s) (sa2_O M a η v₀ t)) ∧
    Continuous (sa2_O M a η v₀) ∧
    ∀ τ, sv_Θsh M a η v₀ (sa2_O M a η v₀ τ) = τ := by
  obtain ⟨hm, hs, hc⟩ := sa2_ginv_strictMono hM ha hη hη2 v₀
  have hchr : ∀ s t : ℝ, s < t → (sh_flat M v₀).Chr (sa2_O M a η v₀ s) (sa2_O M a η v₀ t) :=
    fun s t hst => (sa2_flat_causal hM v₀).2.2.2.2 _ _ (hm hst)
  refine ⟨sa2_g_continuous hM ha hη hη2 v₀, sa2_g_strictMono hM ha hη hη2 v₀,
    sa2_g_surjective hM ha hη hη2 v₀, hs.range_comp _, hchr,
    fun s t hst => by rw [sa2_S_chr hM]; exact hchr s t hst,
    (sa2_O_continuous M v₀).comp hc, fun τ => sa2_g_ginv hM ha hη hη2 v₀ τ⟩

/-! ### ③ The accumulation on the flat restriction, then on the shell -/

include hM in
/-- **`sa2_flat` (BUILT):** `mh_causal_alignment_gh_N` on `sh_flat` with `O′`, `J = range O′ =
range O`: properness and `KLi(S_τ) = KLs(S_τ) = 𝓗⁺`. -/
theorem sa2_flat {a η : ℝ} (ha : 0 < a) (hη : 0 < η) (hη2 : η ≤ 2) (v₀ : ℝ) :
    (sh_flat M v₀).SublevelProper (range (sv_O M v₀)) (sv_Θsh M a η v₀) ∧
    KLi ((sh_flat M v₀).slice (range (sv_O M v₀)) (sv_Θsh M a η v₀)) =
      (sh_flat M v₀).H (range (sv_O M v₀)) ∧
    KLs ((sh_flat M v₀).slice (range (sv_O M v₀)) (sv_Θsh M a η v₀)) =
      (sh_flat M v₀).H (range (sv_O M v₀)) := by
  obtain ⟨-, -, -, hr, hchr, -, -, hΘ⟩ := sa2_O_adapted hM ha hη hη2 v₀
  obtain ⟨-, -, hHM, hJM, -⟩ := sa2_flat_causal hM v₀
  rw [← hr] at hHM hJM ⊢
  have hC := sa2_flat_cauchy hM ha hη hη2 v₀
  rw [← hr] at hC
  exact (sh_flat M v₀).mh_causal_alignment_gh_N (sa2_flat_locallyOneChart M v₀) rfl hchr hJM
    hHM hC (c := 0) fun τ => by rw [hΘ, add_zero]

include hM in
/-- **`sa2_flat_cones` (BUILT):** `mc_cone_kuratowski_N` on `sh_flat`: the past cones of `O′`
(and of `O` itself, which needs no clock) converge to `𝓗⁺`. -/
theorem sa2_flat_cones {a η : ℝ} (ha : 0 < a) (hη : 0 < η) (hη2 : η ≤ 2) (v₀ : ℝ) :
    KLi ((sh_flat M v₀).cone (sa2_O M a η v₀)) = (sh_flat M v₀).H (range (sv_O M v₀)) ∧
    KLs ((sh_flat M v₀).cone (sa2_O M a η v₀)) = (sh_flat M v₀).H (range (sv_O M v₀)) ∧
    KLi ((sh_flat M v₀).cone (sv_O M v₀)) = (sh_flat M v₀).H (range (sv_O M v₀)) ∧
    KLs ((sh_flat M v₀).cone (sv_O M v₀)) = (sh_flat M v₀).H (range (sv_O M v₀)) := by
  obtain ⟨-, -, -, hr, hchr, -, -, -⟩ := sa2_O_adapted hM ha hη hη2 v₀
  obtain ⟨-, -, -, hJM, hchrO⟩ := sa2_flat_causal hM v₀
  have h1 := MSpacetime.mc_cone_kuratowski_N (sa2_flat_locallyOneChart M v₀)
    (J := range (sv_O M v₀)) (O := sa2_O M a η v₀) (by rw [hr]; rfl) hchr hJM
  have h2 := MSpacetime.mc_cone_kuratowski_N (sa2_flat_locallyOneChart M v₀)
    (J := range (sv_O M v₀)) (O := sv_O M v₀) rfl hchrO hJM
  exact ⟨h1.1, h1.2, h2.1, h2.2⟩

include hM in
/-- **The cones miss `𝓗⁺`** on `sh_flat` (`sa2_cone_disjoint`, i.e. campaign 91's
`cd_cone_disjoint`), for `O′` and for `O`. -/
theorem sa2_flat_cone_disjoint {a η : ℝ} (ha : 0 < a) (hη : 0 < η) (hη2 : η ≤ 2) (v₀ : ℝ) :
    (∀ τ, (sh_flat M v₀).cone (sa2_O M a η v₀) τ ∩ (sh_flat M v₀).H (range (sv_O M v₀)) = ∅) ∧
    ∀ τ, (sh_flat M v₀).cone (sv_O M v₀) τ ∩ (sh_flat M v₀).H (range (sv_O M v₀)) = ∅ := by
  obtain ⟨-, -, -, hr, hchr, -, -, -⟩ := sa2_O_adapted hM ha hη hη2 v₀
  obtain ⟨-, -, hHM, hJM, hchrO⟩ := sa2_flat_causal hM v₀
  have hC := sa2_flat_cauchy hM ha hη hη2 v₀
  exact ⟨MSpacetime.sa2_cone_disjoint (sa2_flat_locallyOneChart M v₀) (by rw [hr]; rfl) hchr
      hJM hHM hC,
    MSpacetime.sa2_cone_disjoint (sa2_flat_locallyOneChart M v₀) rfl hchrO hJM hHM hC⟩

include hM in
/-- **Headline `sa2_shell` (BUILT): on the `C⁰` shell model `sh_S`, with `𝓗⁺ = {ũ = u_H}`.**
For `0 < a`, `0 < η ≤ 2`, the adapted observer `O′` (`range O′ = range O`, `Θ_shell(O′ τ) = τ`):
the retarded slicing is sublevel-proper; its slices accumulate on `𝓗⁺` and nowhere else
(`KLi = KLs = 𝓗⁺`); so do the past cones of `O′`; `𝓗⁺ = {ũ = u_H}`; and no cone meets `𝓗⁺`.
Proved on `sh_flat` and carried over by `cz_scale_*` — `Φ′` never enters. -/
theorem sa2_shell {a η : ℝ} (ha : 0 < a) (hη : 0 < η) (hη2 : η ≤ 2) (v₀ : ℝ) :
    range (sa2_O M a η v₀) = range (sv_O M v₀) ∧
    (∀ τ, sv_Θsh M a η v₀ (sa2_O M a η v₀ τ) = τ) ∧
    (sh_S hM v₀).SublevelProper (range (sv_O M v₀)) (sv_Θsh M a η v₀) ∧
    KLi ((sh_S hM v₀).slice (range (sv_O M v₀)) (sv_Θsh M a η v₀)) =
      {y : P | y.1 = sv_uH M v₀} ∧
    KLs ((sh_S hM v₀).slice (range (sv_O M v₀)) (sv_Θsh M a η v₀)) =
      {y : P | y.1 = sv_uH M v₀} ∧
    KLi ((sh_S hM v₀).cone (sa2_O M a η v₀)) = {y : P | y.1 = sv_uH M v₀} ∧
    KLs ((sh_S hM v₀).cone (sa2_O M a η v₀)) = {y : P | y.1 = sv_uH M v₀} ∧
    (sh_S hM v₀).H (range (sv_O M v₀)) = {y : P | y.1 = sv_uH M v₀} ∧
    ∀ τ, (sh_S hM v₀).cone (sa2_O M a η v₀) τ ∩ {y : P | y.1 = sv_uH M v₀} = ∅ := by
  obtain ⟨-, -, -, hr, -, -, -, hΘ⟩ := sa2_O_adapted hM ha hη hη2 v₀
  obtain ⟨h1, h2, h3⟩ := sa2_flat hM ha hη hη2 v₀
  obtain ⟨h4, h5, -, -⟩ := sa2_flat_cones hM ha hη hη2 v₀
  obtain ⟨h6, -⟩ := sa2_flat_cone_disjoint hM ha hη hη2 v₀
  have hH := (sa2_flat_causal hM v₀).2.1
  rw [hH] at h2 h3 h4 h5 h6
  rw [sa2_S_sublevelProper hM, sa2_S_slice hM, sa2_S_cone hM]
  exact ⟨hr, hΘ, h1, h2, h3, h4, h5, sh_frontier hM v₀, h6⟩

/-! ### Non-vacuity -/

/-- **Non-vacuity (BUILT)** at `M = 1`, `v₀ = 0`, `a = 1`, `η = 2` (`u_H = −4`): `𝓗⁺` is
non-empty; `(−4, −1) ∈ 𝓗⁺` has `v < v₀` (the flat body, `Φ′ = 1`) and is a Kuratowski limit of
the slices (and of the cones). -/
theorem sa2_nonvacuous :
    ((sh_S one_pos 0).H (range (sv_O 1 0))).Nonempty ∧
    ((-4 : ℝ), (-1 : ℝ)) ∈ (sh_S one_pos 0).H (range (sv_O 1 0)) ∧
    ((-4 : ℝ), (-1 : ℝ)).2 < 0 ∧ sh_Φ 1 0 ((-4 : ℝ), (-1 : ℝ)) = 1 ∧
    ((-4 : ℝ), (-1 : ℝ)) ∈ KLi ((sh_S one_pos 0).slice (range (sv_O 1 0)) (sv_Θsh 1 1 2 0)) ∧
    ((-4 : ℝ), (-1 : ℝ)) ∈ KLi ((sh_S one_pos 0).cone (sa2_O 1 1 2 0)) := by
  have hmem : ((-4 : ℝ), (-1 : ℝ)) ∈ {y : P | y.1 = sv_uH 1 0} := by
    show (-4 : ℝ) = sv_uH 1 0; unfold sv_uH; norm_num
  obtain ⟨-, -, -, h2, -, h4, -, hH, -⟩ :=
    sa2_shell one_pos one_pos (by norm_num : (0 : ℝ) < 2) le_rfl 0
  refine ⟨⟨_, hH ▸ hmem⟩, hH ▸ hmem, by norm_num, sh_H_flat one_pos hmem (by norm_num),
    h2 ▸ hmem, h4 ▸ hmem⟩

end SA2Model



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

-- campaign 101 (new)
#print axioms sv_monotone_of_brk
#print axioms MSpacetime.sv_cauchy_of_limits
#print axioms SVModel.sv_ψ_contDiff
#print axioms SVModel.sv_ψ_eq_zero
#print axioms SVModel.sv_g_nonneg
#print axioms SVModel.sv_ψ_nonpos
#print axioms SVModel.sv_ψ_le
#print axioms SVModel.sv_ψ_mono
#print axioms SVModel.sv_ψ_tendsto
#print axioms SVModel.sv_ψ_hasDerivAt
#print axioms SVModel.sv_ψ_deriv_nonneg
#print axioms SVModel.sv_Θψ_eq
#print axioms SVModel.sv_eternal_eq
#print axioms SVModel.sv_ψV_hasFDerivAt
#print axioms SVModel.sv_QP_hasFDerivAt
#print axioms SVModel.sv_QP_contDiffOn
#print axioms SVModel.sv_QD_pos
#print axioms SVModel.sv_r_identity
#print axioms SVModel.sv_eta2_identity
#print axioms SVModel.sv_Q_le_far
#print axioms SVModel.sv_future_pure
#print axioms SVModel.sv_past_pure
#print axioms SVModel.sv_coord_mono
#print axioms SVModel.sv_eternal_temporal
#print axioms SVModel.sv_D_open
#print axioms SVModel.sv_curve_R
#print axioms SVModel.sv_eternal_cauchy
#print axioms SVModel.sv_MS_open
#print axioms SVModel.sv_q_pos
#print axioms SVModel.sv_χU_eq
#print axioms SVModel.sv_χU_neg
#print axioms SVModel.sv_χU_uH
#print axioms SVModel.sv_χV_pos
#print axioms SVModel.sv_log_χV
#print axioms SVModel.sv_F_eq
#print axioms SVModel.sv_χ_mem
#print axioms SVModel.sv_χU_hasDerivAt
#print axioms SVModel.sv_χU'_pos
#print axioms SVModel.sv_χV_hasDerivAt
#print axioms SVModel.sv_χU_continuous
#print axioms SVModel.sv_χU_strictMonoOn
#print axioms SVModel.sv_χU_tendsto
#print axioms SVModel.sv_χ_contDiff
#print axioms SVModel.sv_χ_hasFDerivAt
#print axioms SVModel.sv_Dχ_apply
#print axioms SVModel.sv_r_gt
#print axioms SVModel.sv_F'_pos
#print axioms SVModel.sv_Φ_pos
#print axioms SVModel.sv_S_M
#print axioms SVModel.sv_hRep
#print axioms SVModel.sv_r_shell
#print axioms SVModel.sv_flat_past
#print axioms SVModel.sv_F_hasDerivAt
#print axioms SVModel.sv_vacuum
#print axioms SVModel.sv_Φ_continuousOn
#print axioms SVModel.sv_r_strictMono
#print axioms SVModel.sv_Φ_gt_one
#print axioms SVModel.sv_Θsh_eq
#print axioms SVModel.sv_retarded_eq
#print axioms SVModel.sv_dfun
#print axioms SVModel.sv_hasDerivAt
#print axioms SVModel.sv_futCausal_iff
#print axioms SVModel.sv_coord_mono_P
#print axioms SVModel.sv_temporal
#print axioms SVModel.sv_shell_UV
#print axioms SVModel.sv_shell_v_lim
#print axioms SVModel.sv_shell_fut
#print axioms SVModel.sv_shell_past
#print axioms SVModel.sv_cauchy_flat
#print axioms SVModel.sv_cauchy
#print axioms SVModel.sv_vel_eq
#print axioms SVModel.sv_futTimelike_iff
#print axioms SVModel.sv_tstep
#print axioms SVModel.sv_D
#print axioms SVModel.sv_cauchy_D
#print axioms SVModel.sv_mem5
#print axioms SVModel.sv_mem5'
#print axioms SVModel.sv_nonvacuous

-- campaign 102 (new)
#print axioms SHModel.sh_MS_open
#print axioms SHModel.sh_χ_mem
#print axioms SHModel.sh_UV_shell
#print axioms SHModel.sh_shell_mem
#print axioms SHModel.sh_max_mem
#print axioms SHModel.sh_r_shell
#print axioms SHModel.sh_Φ_of_mem
#print axioms SHModel.sh_Φ_pos
#print axioms SHModel.sh_Φ_continuousOn
#print axioms SHModel.sh_S_M
#print axioms SHModel.sh_hRep
#print axioms SHModel.sh_flat_past
#print axioms SHModel.sh_vacuum
#print axioms SHModel.sh_sv_sub
#print axioms SHModel.sh_χU'_eq
#print axioms SHModel.sh_agree
#print axioms SHModel.sh_seg_mem
#print axioms SHModel.sh_tstep_mink
#print axioms SHModel.sh_cstep_mink
#print axioms SHModel.sh_chr_mink
#print axioms SHModel.sh_cau_mink
#print axioms SHModel.sh_tstep
#print axioms SHModel.sh_tstep_cstep
#print axioms SHModel.sh_chr
#print axioms SHModel.sh_cau_le
#print axioms SHModel.sh_O
#print axioms SHModel.sh_chr_O
#print axioms SHModel.sh_D
#print axioms SHModel.sh_Jpast
#print axioms SHModel.sh_frontier_lt
#print axioms SHModel.sh_frontier
#print axioms SHModel.sh_H_sub
#print axioms SHModel.sh_H_r
#print axioms SHModel.sh_H_flat
#print axioms SHModel.sh_cauchy_transfer
#print axioms SHModel.sh_cauchy_D
#print axioms SHModel.sh_headline_D
#print axioms SHModel.sh_nonvacuous

-- campaign 105 (new)
#print axioms SMModel.sm_matter
#print axioms SMModel.sm_γ
#print axioms SMModel.sm_γ_hasDerivAt
#print axioms SMModel.sm_γ_contDiff
#print axioms SMModel.sm_γ_lt
#print axioms SMModel.sm_γ_tendsto
#print axioms SMModel.sm_γ_atBot
#print axioms SMModel.sm_futCausal_iff
#print axioms SMModel.sm_curve
#print axioms SMModel.sm_curve_γ
#print axioms SMModel.sm_matter_D
#print axioms SMModel.sm_Θ_γ
#print axioms SMModel.sm_Θ_γ_strictMono
#print axioms SMModel.sm_sτ
#print axioms SMModel.sm_param
#print axioms SMModel.sm_sτ_spec
#print axioms SMModel.sm_slice_meets_matter
#print axioms SMModel.sm_outside_H
#print axioms SMModel.sm_finite
#print axioms SMModel.sm_approaches
#print axioms SMModel.sm_nonvacuous

#print axioms MSpacetime.sa2_chr_of_mem_closure_Jpast
#print axioms MSpacetime.sa2_mem_closure_sublevel
#print axioms MSpacetime.sa2_closure_Jpast_subset_D
#print axioms MSpacetime.sa2_closure_Jpast_inter_H
#print axioms MSpacetime.sa2_cone_disjoint
#print axioms SA2Model.sa2_flat_locallyOneChart
#print axioms SA2Model.sa2_S_chr
#print axioms SA2Model.sa2_S_D
#print axioms SA2Model.sa2_S_H
#print axioms SA2Model.sa2_S_slice
#print axioms SA2Model.sa2_S_cone
#print axioms SA2Model.sa2_S_sublevelProper
#print axioms SA2Model.sa2_flat_causal
#print axioms SA2Model.sa2_flat_cauchy
#print axioms SA2Model.sa2_O_hasDerivAt
#print axioms SA2Model.sa2_O_continuous
#print axioms SA2Model.sa2_O_lt
#print axioms SA2Model.sa2_O_atBot
#print axioms SA2Model.sa2_g_strictMono
#print axioms SA2Model.sa2_g_surjective
#print axioms SA2Model.sa2_g_continuous
#print axioms SA2Model.sa2_g_ginv
#print axioms SA2Model.sa2_ginv_g
#print axioms SA2Model.sa2_ginv_strictMono
#print axioms SA2Model.sa2_O_adapted
#print axioms SA2Model.sa2_flat
#print axioms SA2Model.sa2_flat_cones
#print axioms SA2Model.sa2_flat_cone_disjoint
#print axioms SA2Model.sa2_shell
#print axioms SA2Model.sa2_nonvacuous

end ShadowProbe.ShellAccumulationProbe

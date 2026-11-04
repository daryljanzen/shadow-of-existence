import Mathlib.Analysis.ODE.ExistUnique
import Mathlib.Analysis.ODE.Gronwall
import Mathlib.Analysis.Calculus.MeanValue
import Mathlib.Analysis.Calculus.InverseFunctionTheorem.ContDiff
import Mathlib.Analysis.Calculus.BumpFunction.FiniteDimension
import Mathlib.Geometry.Manifold.VectorField.LieBracket
import Mathlib.Geometry.Manifold.VectorBundle.Tangent
import Mathlib.Geometry.Manifold.VectorBundle.Basic
import Mathlib.Geometry.Manifold.MFDeriv.Atlas
import Mathlib.Geometry.Manifold.IntegralCurve.ExistUnique

/-!
# Probe `r7675+71` (campaign 97 ②, `r7675`): Schwarzschild's Killing field `∂_t` in Kruskal's radial plane, and 3b

Registered target: `computations/formalisation/r7675_71_campaign97/PREDICTION.md`, piece ②. Base: campaign 96's
`probes/KillingWhole.lean`, copied unchanged into namespace `ShadowProbe.SchwarzschildKillingProbe` (probes cannot
import probes; every copied `ld_*`, `kl_*`, `kg_*`, `kw_*` name is kept, and the inherited headers below describe
them). Campaign 80's Kruskal radius (`probes/TangencyCondition.lean`, namespace `Kruskal`: `hK`, `hK'`, `rinv`,
`rK`, `FS`) is copied with the prefix `sq_` and adapted from region I to the whole of `M = {UV < 1}`.

**Status: BUILT.**
* **BUILT** the radius on `M = {UV < 1}` (`sq_Mset`, open): `r = sq_rK M (U, V) = h⁻¹(−UV)`,
  `h(x) = (x/2M − 1) e^{x/2M}`, with `r > 0` and `h(r) = −UV` (`sq_rK_spec`), **`C¹` on `M`**
  (`sq_rinv_contDiffAt`, `sq_rK_contDiffAt`: `r′ = 1/h′(r)` is continuous), and **`r = 2M` on `U = 0`**
  (`sq_rK_horizon`).
* **BUILT** `F = sq_FS M = (32M³/r) e^{−r/2M}`: `F > 0` on `M` (`sq_FS_pos`), `C¹` on `M` (`sq_FS_contDiffAt`),
  `F = 16M² e^{−1}` on `U = 0` (`sq_FS_horizon`), and **not constant** (`sq_FS_nonconst`: `r = 4M`,
  `F = 8M² e^{−2}` at `(−1, e²)`).
* **BUILT** the raw metric `g = sq_g M`, `g_x = F(x) • kg_w_B`, i.e. **`g_{(U,V)}(v, w) = −F(U, V)(v_U w_V + v_V w_U)/2`**
  (`sq_metric_formula`, stated with `F` written out through `sq_rinv`; this is the formula to match with ①'s
  `sk_S`). Lorentzian on `M` (`sq_lorentzian`).
* **BUILT** `χ = sq_X M = (1/4M)(V∂_V − U∂_U) = ∂_t` (`sq_L M = (1/4M) • kg_w_L`).
  **`L_χ g = 0` on `M`** through the registered `lieDeriv` (`sq_lieDeriv`, by `ld_lieDeriv_chart_self`):
  `χ(UV) = 0` (`sq_chi_UV`), so `χ(F) = 0` (`sq_chi_F`, `F = f ∘ (−UV)`), and the flat boost terms cancel
  (`sq_chartLie`). The registered expected stop was **not hit**. One detour: Mathlib's `HasFDerivAt.smul_const`
  fails here, because no `IsBoundedSMul ℝ (E →L E →L ℝ)` instance is found, so `y ↦ F(y) • B` is
  differentiated through the CLM `t ↦ t • B` (`sq_smul_hasFDerivAt`, `sq_smul_fderiv_apply`, generic `E`).
* **BUILT** `g(χ, χ) = F · UV/(16M²)` (`sq_normSq`). It is null on `U = 0` (`sq_null_horizon`), timelike where
  `UV < 0` (`sq_timelike`), and `χ ≠ 0` where `V ≠ 0` (`sq_X_ne`). The generator `γ s = (0, e^{s/4M})`
  (`sq_γ`) is an integral curve of `χ` itself, with the `1/4M` kept (`sq_integral`).
* **BUILT** 3b, **`sq_cor_EF_coincident`**: for `0 < V₁ < V₂`, `p = (0, V₁) = γ(4M log V₁)` and
  `q = (0, V₂) = γ(4M log V₂)` are distinct, and `kw_lemma_killing_whole` gives:
  - (a) `χ` and `γ′` are null on `[a, b]`;
  - (b) `kg_Related` holds both ways;
  - `kg_deltaTau = 0`;
  - for the horizon splitting, `Δx = 0` and `Δτ = 0`, with `∫ₐᵇ dλ(γ′) = b − a > 0`;
  - `r = 2M` at both.
* **BUILT** the summary `sq_killing`.

Non-vacuity: every hypothesis of `kw_lemma_killing_whole` is discharged for the actual Schwarzschild `F`, and
`F` is shown non-constant. The Killing parameter separates `p` and `q` (`b − a > 0`), and `p ≠ q`.

Not checked or used: `Ric = 0` (Schwarzschild is taken by definition of `F`, as in campaign 80); the `L_χ g = 0`
claim is on `M` only (off `M`, `sq_rinv` is a junk value).

Nothing imports this file.
-/

/-!
# Inherited header — probe `r7673+71` (campaign 96)

Registered target: `computations/formalisation/r7673_71_campaign96/PREDICTION.md`. Base: campaign 95's
`probes/KillingGenerator.lean`, copied unchanged into namespace `ShadowProbe.SchwarzschildKillingProbe` (probes cannot
import probes; every copied `ld_*`, `kl_*`, `kg_*` name is kept, and the campaign-95 header below describes
them). Campaign 94 ①'s `AdaptedSplitting`, `Δx`, `Δτ`, `g_vel`, `ac_eq_zero_of_integral_eq_zero` and
`ac_metric_singularity_along` (`probes/AlongConnection.lean`, stated there for an `MSpacetime` on `[0, 1]`)
are restated here for the raw section `g : Π x, T_xN →L T_xN →L ℝ` and `γ′ = mfderiv γ t 1` on `[a, b]`:
`kw_AdaptedSplitting`, `kw_AdaptedSplitting.Δx`, `.Δτ`, `.kw_g_vel`, `kw_eq_zero_of_integral_eq_zero`,
`kw_metric_singularity_along` (`a < b`).

**Status: BUILT.**
* **BUILT** `«kw_dλ_exists»`: in finite dimension every `v ≠ 0` has `φ : E →L[ℝ] ℝ` with `φ v = 1`.
* **BUILT** the horizon splitting `kw_horizonSplitting` along `γ` on `[a, b]`: lapse
  `n s = √(max 0 (−g(X, X)))` (`kw_n`), `dt s = dλ` chosen with `dλ(X (γ s)) = 1` (`kw_dt`, `kw_dt_X`),
  `h s = g_{γ s} + n² dt ⊗ dt` (`kw_h`); `g = h − n² dt ⊗ dt` (`kw_split`), and
  `h(X, X) = max(g(X, X), 0) ≥ 0` (`kw_h_X`), so `h(γ′, γ′) ≥ 0` once `γ′ = X`.
* **BUILT** `kw_lemma_killing_whole`: under `kg_lemma_killing_generator`'s hypotheses, all of stage 2's
  conclusions (velocity form, (a), (b), (c), `kg_deltaTau = 0`), and for the horizon splitting on the **whole**
  of `[a, b]`: `h s = g_{γ s}` and `h(γ′, γ′) = 0`, `Δx = ∫ₐᵇ √h(γ′, γ′) = 0`, and
  `Δτ = ∫ₐᵇ n |dt(γ′)| = 0` (from `kw_metric_singularity_along` when `a < b`; trivially when `a = b`).
* **BUILT** `kw_witness`: stage 2's Rindler generator `γ s = (0, eˢ)`, `s ∈ [0, 10]`: `Δx = 0`, `Δτ = 0`,
  `∫₀¹⁰ dλ(γ′) = 10` (the Killing parameter separates the endpoints), `γ 0 = (0, 1) ≠ (0, e¹⁰) = γ 10`,
  related both ways.

Stated as registered: `Δx` depends on the splitting, and this one is the horizon's own (lapse `|χ|`,
time `λ`). `h` equals `g` on `γ`; it is not positive semidefinite off `γ′`, and only `h(γ′, γ′) ≥ 0` is
asked. This is P1's reading: on a Killing horizon `ds² = |χ|² dλ²`, and the spatial leg along the
generator vanishes.

Nothing imports this file.
-/

/-!
# Inherited header — probe `r7671+71` (campaign 95, `r7671`): `lem:killing` stage 2, along a whole generator

Registered target: `computations/formalisation/r7671_71_campaign95/PREDICTION.md`. Base: campaign 94 ②'s
`probes/KillingLocal.lean`, copied unchanged into namespace `ShadowProbe.SchwarzschildKillingProbe` (probes cannot
import probes; one Mathlib import, `IntegralCurve.ExistUnique`, is added). The copied `ld_*` and `kl_*` names are
kept, so they still match their source, and that file's header describes them. Campaign 94 ①'s `gM`, boost flow,
`ac_boost_generator` and `ac_boost_isometry` (`probes/AlongConnection.lean`) are restated for the witness as
`kg_w_B`, `kg_w_Φ`, `kg_w_boost_generator`, `kg_w_boost_isometry`.

**Status.**
* **(a) BUILT.** `g(X, X) = 0` and `ds² = g(γ′, γ′) = 0` at every `γ t`, `t ∈ [a, b]`.
* **(b) BUILT**, for every pair `t₁, t₂ ∈ [a, b]` (not only one box): `kg_Related g γ t₁ t₂`.
* **(c) BUILT** (trivial, from injectivity).
* **(d) BUILT IN PART.** `Δτ = ∫ₐᵇ n |dλ(γ′)| = 0` for the adapted lapse `n = |X|` (`kg_deltaTau`), with
  `dλ(γ′) = 1` as `γ′ = X = ∂_λ`. `Δx = 0` holds box-wise only (in each window `γ s = ψ (s − t₁, 0)` sits on
  the transverse slice `h = 0`, `kg_box_along`); no global spatial splitting is built.
* **Witness BUILT**: the Rindler horizon generator, all hypotheses discharged, `γ 0 ≠ γ 10` related.
The registered expected stop (composing flow-box isometries along a chain) was not hit: the chain is
replaced by connectedness of `[a, b]` (`IsPreconnected.induction₂'`) applied to the transitive relation
`kg_Related`, which holds for every pair inside one box window.

New here (prefix `kg_`):
* `kg_flowBox_killing_symm`, `kg_killingChart_symm`: `ld_flowBox_killing_of_contDiffOn` and
  `ld_manifold_killingChart_lieDeriv` re-proved keeping the flow box's `C¹` inverse; `kg_restrict` shrinks a
  `LocalKillingChart` so that `Φ⁻¹` is `C¹` on its whole target (`kg_SymmC1`).
* The box translation `kg_shift K δ = ψ ∘ (· + (δ, 0)) ∘ ψ⁻¹` (`kg_chi = ψ⁻¹`, domain `kg_U K δ`, open):
  differentiable (`kg_shift_hasMFDerivAt`) and **an isometry** (`kg_shift_isometry`, from `kl_lambda_indep_N`).
* `kg_orbit_hasMFDerivAt` (the box orbit is an integral curve) and `kg_curve_eq_orbit`: Mathlib's
  `isMIntegralCurveAt_eventuallyEq_of_contMDiffAt_boundaryless` identifies `γ` with the box orbit near `t₁`.
* `kg_Related` (the registered (b)), `kg_related_trans` (composition on `U₁ ∩ F₁⁻¹ U₂`), `kg_box_along`,
  `kg_related_box`, `kg_normSq_box`; `kg_lapse`, `kg_deltaTau`, `kg_deltaTau_zero`.
* Headline **`kg_lemma_killing_generator`**, and the witness **`kg_witness`** (`kg_w_*`): `N = ℝ × ℝ`,
  `g = −dU dV`, `χ = V∂_V − U∂_U` (`L_χ g = 0` through the registered `lieDeriv`), `γ s = (0, eˢ)`,
  `s ∈ [0, 10]`.

**Hypotheses beyond the registration.** `γ` is an integral curve *at* every `t ∈ [a, b]`
(`IsMIntegralCurveAt`, i.e. on a neighbourhood of each parameter, so slightly past the endpoints); the
registered `mfderiv γ t 1 = X (γ t)` is then a conclusion. `X` is asked `C¹` only along `γ` (weaker than the
registered global `C¹`). `T2Space N` is not needed (only local uniqueness of integral curves is used), and
boundarylessness is automatic for the model `𝓘(ℝ, E)`.

Nothing imports this file.
-/

open Set Filter Topology Metric
open scoped NNReal

set_option linter.unusedSectionVars false

namespace ShadowProbe.SchwarzschildKillingProbe

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

/-- The chart representative of a vector field `X` in the chart at `p`: the pushforward of `X` by
`extChartAt p`, `y ↦ D(extChartAt p)_{φ⁻¹ y} (X (φ⁻¹ y))`. -/
noncomputable def chartRep (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N) (y : E) : E :=
  mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p) ((extChartAt 𝓘(ℝ, E) p).symm y)
    (X ((extChartAt 𝓘(ℝ, E) p).symm y))

/-- Pushing the chart representative back by `(extChartAt p).symm` returns `X`. -/
theorem ld_chartRep_inv (X : Π x : N, TangentSpace 𝓘(ℝ, E) x) (p : N) {y : E}
    (hy : y ∈ (extChartAt 𝓘(ℝ, E) p).target) :
    mfderiv 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p).symm y (chartRep (E := E) X p y) =
      X ((extChartAt 𝓘(ℝ, E) p).symm y) := by
  have h := mfderivWithin_extChartAt_symm_comp_mfderiv_extChartAt (I := 𝓘(ℝ, E)) (x := p) hy
  rw [ModelWithCorners.range_eq_univ, mfderivWithin_univ] at h
  exact DFunLike.congr_fun h (X ((extChartAt 𝓘(ℝ, E) p).symm y))

/-- `(extChartAt p).symm` is manifold-differentiable on the chart target. -/
theorem ld_mdifferentiableAt_symm (p : N) {y : E} (hy : y ∈ (extChartAt 𝓘(ℝ, E) p).target) :
    MDifferentiableAt 𝓘(ℝ, E) 𝓘(ℝ, E) (extChartAt 𝓘(ℝ, E) p).symm y := by
  have h := mdifferentiableWithinAt_extChartAt_symm (I := 𝓘(ℝ, E)) (x := p) hy
  rwa [ModelWithCorners.range_eq_univ, mdifferentiableWithinAt_univ] at h

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


/-! ## Campaign 97 ② (`r7675+71`): Schwarzschild in Kruskal's radial plane, `χ = ∂_t`, and 3b -/

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

section SQRadius

open Manifold ContinuousLinearMap

set_option synthInstance.maxHeartbeats 400000

/-! ### The areal radius `r(U, V)`: inverse of `h(x) = (x/2M − 1) e^{x/2M}` (campaign 80's `Kruskal`) -/

/-- `h(x) = (x/(2M) − 1) e^{x/(2M)}`; `r` solves `h(r) = −UV` (campaign 80's `hK`). -/
noncomputable def sq_hK (M x : ℝ) : ℝ := (x / (2 * M) - 1) * Real.exp (x / (2 * M))

/-- `h′(x) = x/(4M²) e^{x/(2M)}` (campaign 80's `hK'`). -/
noncomputable def sq_hK' (M x : ℝ) : ℝ := x / (4 * M ^ 2) * Real.exp (x / (2 * M))

section SQRadius1
variable {M : ℝ} (hM : 0 < M)
include hM

theorem sq_hasDerivAt_hK (x : ℝ) : HasDerivAt (sq_hK M) (sq_hK' M x) x := by
  have h1 : HasDerivAt (fun x : ℝ => x / (2 * M)) (1 / (2 * M)) x :=
    (hasDerivAt_id x).div_const _
  have h := (h1.sub_const 1).mul h1.exp
  refine h.congr_deriv ?_
  simp only [sq_hK']; field_simp; ring

omit hM in
theorem sq_continuous_hK : Continuous (sq_hK M) := by
  unfold sq_hK; fun_prop

theorem sq_hK_strictMonoOn : StrictMonoOn (sq_hK M) (Ici 0) := by
  refine strictMonoOn_of_deriv_pos (convex_Ici 0) sq_continuous_hK.continuousOn fun x hx => ?_
  rw [interior_Ici] at hx
  rw [(sq_hasDerivAt_hK hM x).deriv]
  have : 0 < x := hx
  unfold sq_hK'; positivity

omit hM in
theorem sq_hK_zero : sq_hK M 0 = -1 := by simp [sq_hK]

theorem sq_hK_two : sq_hK M (2 * M) = 0 := by
  simp only [sq_hK]; rw [div_self (by positivity)]; simp

theorem sq_hK_gt {x : ℝ} (hx : 0 < x) : -1 < sq_hK M x := by
  rw [← sq_hK_zero]
  exact sq_hK_strictMonoOn hM (mem_Ici.2 le_rfl) hx.le hx

theorem sq_hK_exists {y : ℝ} (hy : -1 < y) : ∃ x, 0 < x ∧ sq_hK M x = y := by
  set b := 2 * M * (|y| + 2)
  have hb : 0 ≤ b := by positivity
  have hyb : y ≤ sq_hK M b := by
    have h1 : 0 ≤ b / (2 * M) - 1 := by
      rw [show b / (2 * M) = |y| + 2 by simp only [b]; field_simp]
      linarith [abs_nonneg y]
    have h2 : b / (2 * M) - 1 ≤ sq_hK M b :=
      le_mul_of_one_le_right h1 (Real.one_le_exp (by positivity))
    have h3 : b / (2 * M) - 1 = |y| + 1 := by simp only [b]; field_simp; ring
    linarith [le_abs_self y]
  obtain ⟨x, hx, hxy⟩ := intermediate_value_Icc hb sq_continuous_hK.continuousOn
    ⟨by rw [sq_hK_zero]; exact hy.le, hyb⟩
  refine ⟨x, ?_, hxy⟩
  rcases hx.1.eq_or_lt with h | h
  · rw [← h, sq_hK_zero] at hxy; linarith
  · exact h

end SQRadius1

open Classical in
/-- The inverse of `h` on `(−1, ∞) → (0, ∞)` (junk value `0` elsewhere); campaign 80's `rinv`. -/
noncomputable def sq_rinv (M y : ℝ) : ℝ :=
  if h : ∃ x, 0 < x ∧ sq_hK M x = y then h.choose else 0

section SQRadius2
variable {M : ℝ} (hM : 0 < M)
include hM

theorem sq_rinv_spec {y : ℝ} (hy : -1 < y) : 0 < sq_rinv M y ∧ sq_hK M (sq_rinv M y) = y := by
  have h := sq_hK_exists hM hy
  simp only [sq_rinv, h, ↓reduceDIte]
  exact h.choose_spec

theorem sq_rinv_hK {x : ℝ} (hx : 0 < x) : sq_rinv M (sq_hK M x) = x := by
  obtain ⟨h1, h2⟩ := sq_rinv_spec hM (sq_hK_gt hM hx)
  exact (sq_hK_strictMonoOn hM).injOn (mem_Ici.2 h1.le) (mem_Ici.2 hx.le) h2

theorem sq_rinv_zero : sq_rinv M 0 = 2 * M := by
  rw [← sq_hK_two hM, sq_rinv_hK hM (by positivity)]

theorem sq_rinv_strictMonoOn : StrictMonoOn (sq_rinv M) (Ioi (-1)) := by
  intro y₁ hy₁ y₂ hy₂ hlt
  obtain ⟨a1, b1⟩ := sq_rinv_spec hM hy₁
  obtain ⟨a2, b2⟩ := sq_rinv_spec hM hy₂
  by_contra h; push Not at h
  have := (sq_hK_strictMonoOn hM).monotoneOn (mem_Ici.2 a2.le) (mem_Ici.2 a1.le) h
  rw [b1, b2] at this; linarith

theorem sq_rinv_continuousAt {a : ℝ} (ha : -1 < a) : ContinuousAt (sq_rinv M) a := by
  refine continuousAt_of_monotoneOn_of_image_mem_nhds (sq_rinv_strictMonoOn hM).monotoneOn
    (Ioi_mem_nhds ha) ?_
  refine mem_of_superset (Ioi_mem_nhds (sq_rinv_spec hM ha).1) fun x hx => ?_
  exact ⟨sq_hK M x, sq_hK_gt hM hx, sq_rinv_hK hM hx⟩

/-- **The derivative of the inverse** (inverse function theorem in one variable). -/
theorem sq_rinv_hasDerivAt {a : ℝ} (ha : -1 < a) :
    HasDerivAt (sq_rinv M) (sq_hK' M (sq_rinv M a))⁻¹ a := by
  refine HasDerivAt.of_local_left_inverse (sq_rinv_continuousAt hM ha) (sq_hasDerivAt_hK hM _) ?_ ?_
  · have := (sq_rinv_spec hM ha).1; unfold sq_hK'; positivity
  · filter_upwards [Ioi_mem_nhds ha] with y hy using (sq_rinv_spec hM hy).2

/-- **`r` is `C¹`** on `(−1, ∞)`: its derivative `1/h′(r)` is continuous there (new). -/
theorem sq_rinv_contDiffAt {a : ℝ} (ha : -1 < a) : ContDiffAt ℝ 1 (sq_rinv M) a := by
  rw [contDiffAt_one_iff]
  refine ⟨fun y => (sq_hK' M (sq_rinv M y))⁻¹ • (1 : ℝ →L[ℝ] ℝ), Ioi (-1), Ioi_mem_nhds ha, ?_, ?_⟩
  · refine ContinuousOn.smul (ContinuousOn.inv₀ (f := fun y => sq_hK' M (sq_rinv M y)) ?_ fun y hy => ?_)
      (continuousOn_const (c := (1 : ℝ →L[ℝ] ℝ)))
    · refine continuousOn_of_forall_continuousAt fun y hy => ?_
      have hc : Continuous (sq_hK' M) := by unfold sq_hK'; fun_prop
      exact hc.continuousAt.comp (sq_rinv_continuousAt hM hy)
    · have := (sq_rinv_spec hM hy).1; unfold sq_hK'; positivity
  · intro y hy
    refine (sq_rinv_hasDerivAt hM hy).hasFDerivAt.congr_fderiv ?_
    ext; simp

end SQRadius2

/-! ### The domain `M = {UV < 1}`, `r(U, V)` and `F = (32M³/r) e^{−r/2M}` on it -/

/-- The spacetime region `M = {UV < 1}` (`r > 0`) of the Kruskal plane. -/
def sq_Mset : Set (ℝ × ℝ) := {p | p.1 * p.2 < 1}

theorem sq_Mset_open : IsOpen sq_Mset :=
  isOpen_lt (continuous_fst.mul continuous_snd) continuous_const

/-- The horizon line `U = 0` lies in `M`. -/
theorem sq_horizon_mem {p : ℝ × ℝ} (hp : p.1 = 0) : p ∈ sq_Mset := by
  show p.1 * p.2 < 1
  rw [hp, zero_mul]; exact one_pos

/-- The areal radius in Kruskal coordinates: `r(U, V) = h⁻¹(−UV)` (campaign 80's `rK`). -/
noncomputable def sq_rK (M : ℝ) (p : ℝ × ℝ) : ℝ := sq_rinv M (-(p.1 * p.2))

/-- The Schwarzschild conformal factor as a function of `y = −UV`. -/
noncomputable def sq_fS (M y : ℝ) : ℝ := 32 * M ^ 3 / sq_rinv M y * Real.exp (-sq_rinv M y / (2 * M))

/-- `F = (32M³/r) e^{−r/2M}`, with `r = r(U, V)` (campaign 80's `FS`). -/
noncomputable def sq_FS (M : ℝ) (p : ℝ × ℝ) : ℝ :=
  32 * M ^ 3 / sq_rK M p * Real.exp (-sq_rK M p / (2 * M))

theorem sq_FS_comp (M : ℝ) : sq_FS M = sq_fS M ∘ fun p : ℝ × ℝ => -(p.1 * p.2) := rfl

section SQRadius3
variable {M : ℝ} (hM : 0 < M)
include hM

omit hM in
theorem sq_Mset_UV {p : ℝ × ℝ} (hp : p ∈ sq_Mset) : -1 < -(p.1 * p.2) := by
  have : p.1 * p.2 < 1 := hp; linarith

/-- On `M`: `r > 0` and `h(r) = −UV`. -/
theorem sq_rK_spec {p : ℝ × ℝ} (hp : p ∈ sq_Mset) :
    0 < sq_rK M p ∧ sq_hK M (sq_rK M p) = -(p.1 * p.2) :=
  sq_rinv_spec hM (sq_Mset_UV hp)

/-- **`r = 2M` on the horizon `U = 0`.** -/
theorem sq_rK_horizon {p : ℝ × ℝ} (hp : p.1 = 0) : sq_rK M p = 2 * M := by
  simp only [sq_rK, hp, zero_mul, neg_zero]; exact sq_rinv_zero hM

/-- **`r` is `C¹` on `M`.** -/
theorem sq_rK_contDiffAt {p : ℝ × ℝ} (hp : p ∈ sq_Mset) : ContDiffAt ℝ 1 (sq_rK M) p :=
  (sq_rinv_contDiffAt hM (sq_Mset_UV hp)).comp p (by fun_prop)

theorem sq_FS_pos {p : ℝ × ℝ} (hp : p ∈ sq_Mset) : 0 < sq_FS M p := by
  have := (sq_rK_spec hM hp).1; unfold sq_FS; positivity

theorem sq_fS_contDiffAt {y : ℝ} (hy : -1 < y) : ContDiffAt ℝ 1 (sq_fS M) y := by
  have hr := sq_rinv_contDiffAt hM hy
  have hne : sq_rinv M y ≠ 0 := (sq_rinv_spec hM hy).1.ne'
  unfold sq_fS
  exact (contDiffAt_const.div hr hne).mul ((hr.neg.div_const _).exp)

/-- **`F` is `C¹` on `M`.** -/
theorem sq_FS_contDiffAt {p : ℝ × ℝ} (hp : p ∈ sq_Mset) : ContDiffAt ℝ 1 (sq_FS M) p := by
  rw [sq_FS_comp]
  exact (sq_fS_contDiffAt hM (sq_Mset_UV hp)).comp p (by fun_prop)

/-- On the horizon, `F = 32M³/(2M) · e^{−1} = 16M² e^{−1}`. -/
theorem sq_FS_horizon {p : ℝ × ℝ} (hp : p.1 = 0) : sq_FS M p = 16 * M ^ 2 * Real.exp (-1) := by
  unfold sq_FS
  rw [sq_rK_horizon hM hp, show -(2 * M) / (2 * M) = -1 by field_simp]
  field_simp; ring

/-- **`F` is not constant** (non-vacuity of the `χ(F) = 0` step): at `(U, V) = (−1, e²)`, `r = 4M` and
`F = 8M² e^{−2} ≠ 16M² e^{−1}`, the horizon value. -/
theorem sq_FS_nonconst :
    sq_rK M (-1, Real.exp 2) = 4 * M ∧ sq_FS M (-1, Real.exp 2) = 8 * M ^ 2 * Real.exp (-2) ∧
    sq_FS M (-1, Real.exp 2) ≠ sq_FS M (0, 1) := by
  have h2 : 4 * M / (2 * M) = 2 := by rw [div_eq_iff (by positivity)]; ring
  have hr : sq_rK M (-1, Real.exp 2) = 4 * M := by
    have : -((-1 : ℝ) * Real.exp 2) = sq_hK M (4 * M) := by
      simp only [sq_hK, h2]; ring
    show sq_rinv M (-((-1 : ℝ) * Real.exp 2)) = _
    rw [this, sq_rinv_hK hM (by positivity)]
  have hF : sq_FS M (-1, Real.exp 2) = 8 * M ^ 2 * Real.exp (-2) := by
    unfold sq_FS
    rw [hr, show -(4 * M) / (2 * M) = -2 by rw [neg_div, h2]]
    field_simp; ring
  refine ⟨hr, hF, ?_⟩
  rw [hF, sq_FS_horizon hM (p := ((0 : ℝ), (1 : ℝ))) rfl]
  intro h
  have he : Real.exp (-2) < Real.exp (-1) := Real.exp_lt_exp.2 (by norm_num)
  have hM2 : 0 < M ^ 2 := by positivity
  nlinarith [Real.exp_pos (-2)]

end SQRadius3

/-! ### The metric `g = −F(r(U, V)) dU dV` on `ℝ × ℝ` -/

/-- `g_x = F(x) · gM`, `gM(a, b) = −(a₁ b₂ + a₂ b₁)/2` (`kg_w_B`, the convention of `kg_w_g`/`kw_witness`). -/
noncomputable def sq_gM (M : ℝ) (x : ℝ × ℝ) : (ℝ × ℝ) →L[ℝ] (ℝ × ℝ) →L[ℝ] ℝ := sq_FS M x • kg_w_B

theorem sq_gM_apply (M : ℝ) (x v w : ℝ × ℝ) :
    sq_gM M x v w = sq_FS M x * (-(v.1 * w.2 + v.2 * w.1) / 2) := by
  simp only [sq_gM, smul_apply, smul_eq_mul, kg_w_B_apply]

/-- The raw Schwarzschild metric field on `N = ℝ × ℝ` (Kruskal null coordinates `(U, V)`). -/
noncomputable def sq_g (M : ℝ) :
    Π x : ℝ × ℝ, TangentSpace 𝓘(ℝ, ℝ × ℝ) x →L[ℝ] TangentSpace 𝓘(ℝ, ℝ × ℝ) x →L[ℝ] ℝ :=
  fun x => sq_gM M x

/-- **The shared metric formula** (to be matched with ①'s `sk_S`):
`g_{(U,V)}(v, w) = −F(U, V) (v_U w_V + v_V w_U)/2`, `F = (32M³/r) e^{−r/2M}`, `r = h⁻¹(−UV)`,
`h(x) = (x/2M − 1) e^{x/2M}`. -/
theorem sq_metric_formula (M : ℝ) (x v w : ℝ × ℝ) :
    sq_g M x v w = -(32 * M ^ 3 / sq_rinv M (-(x.1 * x.2)) *
      Real.exp (-sq_rinv M (-(x.1 * x.2)) / (2 * M))) * (v.1 * w.2 + v.2 * w.1) / 2 := by
  show sq_gM M x v w = _
  rw [sq_gM_apply]; unfold sq_FS sq_rK; ring

/-- **`g` is Lorentzian on `M`:** symmetric, nondegenerate, `(1, 1)` timelike and `(1, −1)` spacelike. -/
theorem sq_lorentzian {M : ℝ} (hM : 0 < M) {x : ℝ × ℝ} (hx : x ∈ sq_Mset) :
    0 < sq_FS M x ∧
    (∀ v w : ℝ × ℝ, sq_g M x v w = sq_g M x w v) ∧
    (∀ v : ℝ × ℝ, (∀ w, sq_g M x v w = 0) → v = 0) ∧
    sq_g M x (1, 1) (1, 1) < 0 ∧ 0 < sq_g M x (1, -1) (1, -1) := by
  have hF := sq_FS_pos hM hx
  refine ⟨hF, fun v w => ?_, fun v hv => ?_, ?_, ?_⟩
  · show sq_gM M x v w = sq_gM M x w v
    simp only [sq_gM_apply]; ring
  · have h1 := hv (1, 0); have h2 := hv (0, 1)
    change sq_gM M x v (1, 0) = 0 at h1; change sq_gM M x v (0, 1) = 0 at h2
    simp only [sq_gM_apply] at h1 h2
    have e1 : v.2 = 0 := by
      have : sq_FS M x * v.2 = 0 := by linarith
      exact (mul_eq_zero.1 this).resolve_left hF.ne'
    have e2 : v.1 = 0 := by
      have : sq_FS M x * v.1 = 0 := by linarith
      exact (mul_eq_zero.1 this).resolve_left hF.ne'
    ext <;> simp [e1, e2]
  · show sq_gM M x (1, 1) (1, 1) < 0
    rw [sq_gM_apply]; norm_num; exact hF
  · show 0 < sq_gM M x (1, -1) (1, -1)
    rw [sq_gM_apply]; norm_num; exact hF

/-! ### The Killing field `χ = (1/4M)(V∂_V − U∂_U) = ∂_t` -/

/-- `χ` as a linear map: `(U, V) ↦ (1/4M)(−U, V)`. -/
noncomputable def sq_L (M : ℝ) : (ℝ × ℝ) →L[ℝ] (ℝ × ℝ) := (1 / (4 * M)) • kg_w_L

theorem sq_L_apply (M : ℝ) (x : ℝ × ℝ) : sq_L M x = (-x.1 / (4 * M), x.2 / (4 * M)) := by
  simp only [sq_L, smul_apply, kg_w_L_apply, Prod.smul_mk, smul_eq_mul]
  ext <;> simp only <;> ring

/-- The Schwarzschild time translation `χ = ∂_t` in Kruskal coordinates. -/
noncomputable def sq_X (M : ℝ) : Π x : ℝ × ℝ, TangentSpace 𝓘(ℝ, ℝ × ℝ) x := fun x => sq_L M x

/-- **`χ(UV) = 0`**: `χ` is tangent to the hyperbolae `UV = const`. -/
theorem sq_chi_UV (M : ℝ) (x : ℝ × ℝ) :
    fderiv ℝ (fun p : ℝ × ℝ => p.1 * p.2) x (sq_L M x) = 0 := by
  have h : HasFDerivAt (fun p : ℝ × ℝ => p.1 * p.2)
      (x.1 • snd ℝ ℝ ℝ + x.2 • fst ℝ ℝ ℝ) x :=
    (hasFDerivAt_fst (p := x)).mul (hasFDerivAt_snd (p := x))
  rw [h.fderiv]
  simp only [add_apply, smul_apply, coe_fst', coe_snd', smul_eq_mul, sq_L_apply]
  ring

section SQKilling
variable {M : ℝ} (hM : 0 < M)
include hM

/-- **`χ(F) = 0` on `M`**: `F` depends on `(U, V)` only through `UV`. -/
theorem sq_chi_F {x : ℝ × ℝ} (hx : x ∈ sq_Mset) : fderiv ℝ (sq_FS M) x (sq_L M x) = 0 := by
  have hq : HasFDerivAt (fun q : ℝ × ℝ => -(q.1 * q.2))
      (-(fderiv ℝ (fun p : ℝ × ℝ => p.1 * p.2) x)) x :=
    (((hasFDerivAt_fst (p := x)).mul (hasFDerivAt_snd (p := x))).differentiableAt.hasFDerivAt).neg
  have hf := ((sq_fS_contDiffAt hM (sq_Mset_UV hx)).differentiableAt one_ne_zero).hasFDerivAt
  rw [sq_FS_comp, (hf.comp x hq).fderiv, ContinuousLinearMap.comp_apply, neg_apply, sq_chi_UV,
    neg_zero, map_zero]

theorem sq_FS_diff {x : ℝ × ℝ} (hx : x ∈ sq_Mset) : DifferentiableAt ℝ (sq_FS M) x :=
  (sq_FS_contDiffAt hM hx).differentiableAt one_ne_zero

theorem sq_gM_diff {x : ℝ × ℝ} (hx : x ∈ sq_Mset) : DifferentiableAt ℝ (sq_gM M) x :=
  (sq_smul_hasFDerivAt kg_w_B (sq_FS_diff hM hx).hasFDerivAt).differentiableAt

omit hM in
theorem sq_hRep (p : ℝ × ℝ) : hRep (sq_g M) p = sq_gM M := by
  funext y
  show (sq_gM M ((extChartAt 𝓘(ℝ, ℝ × ℝ) p).symm y)).bilinearComp _ _ = sq_gM M y
  rw [kl_w_mfderiv_chart_symm, extChartAt_model_space_eq_id]
  exact ContinuousLinearMap.ext fun v => ContinuousLinearMap.ext fun w => rfl

omit hM in
theorem sq_chartRep (p : ℝ × ℝ) : chartRep (sq_X M) p = ⇑(sq_L M) := by
  funext y
  show mfderiv 𝓘(ℝ, ℝ × ℝ) 𝓘(ℝ, ℝ × ℝ) (extChartAt 𝓘(ℝ, ℝ × ℝ) p) _
    (sq_L M ((extChartAt 𝓘(ℝ, ℝ × ℝ) p).symm y)) = _
  rw [kl_w_mfderiv_chart, extChartAt_model_space_eq_id]
  rfl

/-- The chart Killing expression vanishes on `M`: `χ(F) gM + F (gM(χ a, b) + gM(a, χ b)) = 0`, the first
term by `χ(F) = 0`, the second by the flat boost cancellation. -/
theorem sq_chartLie {z : ℝ × ℝ} (hz : z ∈ sq_Mset) (a b : ℝ × ℝ) :
    chartLie (sq_gM M) ⇑(sq_L M) z a b = 0 := by
  unfold chartLie
  have e : fderiv ℝ (sq_gM M) z (sq_L M z) a b = fderiv ℝ (sq_FS M) z (sq_L M z) * kg_w_B a b :=
    sq_smul_fderiv_apply kg_w_B (sq_FS_diff hM hz) _ _ _
  rw [e, sq_chi_F hM hz, ContinuousLinearMap.fderiv, zero_mul, zero_add]
  rw [sq_gM_apply, sq_gM_apply, sq_L_apply, sq_L_apply]
  ring

/-- **`L_χ g = 0` on `M = {UV < 1}`**, through the registered `lieDeriv` (`ld_lieDeriv_chart_self`). -/
theorem sq_lieDeriv {x : ℝ × ℝ} (hx : x ∈ sq_Mset) (v w : ℝ × ℝ) :
    lieDeriv (sq_X M) (sq_g M) x v w = 0 := by
  rw [ld_lieDeriv_chart_self (sq_X M) (sq_g M) x v w (by
    rw [sq_hRep, extChartAt_model_space_eq_id]; exact sq_gM_diff hM hx)]
  rw [sq_hRep, sq_chartRep, extChartAt_model_space_eq_id]
  exact sq_chartLie hM hx _ _

/-- `L_χ g = 0` on a neighbourhood of every point of `M`. -/
theorem sq_lieDeriv_nhds {x : ℝ × ℝ} (hx : x ∈ sq_Mset) :
    ∀ᶠ y in 𝓝 x, ∀ v w, lieDeriv (sq_X M) (sq_g M) y v w = 0 := by
  filter_upwards [sq_Mset_open.mem_nhds hx] with y hy using sq_lieDeriv hM hy

theorem sq_hRep_nhds {x : ℝ × ℝ} (hx : x ∈ sq_Mset) (p : ℝ × ℝ) :
    ∀ᶠ y in 𝓝 x, DifferentiableAt ℝ (hRep (sq_g M) p) y := by
  filter_upwards [sq_Mset_open.mem_nhds hx] with y hy
  rw [sq_hRep]; exact sq_gM_diff hM hy

omit hM in
theorem sq_hX (p : ℝ × ℝ) : ContMDiffAt 𝓘(ℝ, ℝ × ℝ) 𝓘(ℝ, ℝ × ℝ).tangent 1
    (fun x ↦ (⟨x, sq_X M x⟩ : TangentBundle 𝓘(ℝ, ℝ × ℝ) (ℝ × ℝ))) p :=
  (contMDiffAt_vectorSpace_iff_contDiffAt (V := sq_X M)).2 (sq_L M).contDiff.contDiffAt

/-- `g(χ, χ) = F · UV/(16M²)`. -/
theorem sq_normSq (x : ℝ × ℝ) :
    sq_g M x (sq_X M x) (sq_X M x) = sq_FS M x * (x.1 * x.2) / (16 * M ^ 2) := by
  show sq_gM M x (sq_L M x) (sq_L M x) = _
  rw [sq_gM_apply, sq_L_apply]
  field_simp; ring

/-- **`χ` is null on `U = 0`.** -/
theorem sq_null_horizon {x : ℝ × ℝ} (hx : x.1 = 0) : sq_g M x (sq_X M x) (sq_X M x) = 0 := by
  rw [sq_normSq hM, hx]; simp

/-- **`χ ≠ 0` on `U = 0`, `V ≠ 0`** (away from the bifurcation point). -/
theorem sq_X_ne {x : ℝ × ℝ} (hV : x.2 ≠ 0) : sq_X M x ≠ 0 := by
  intro h
  have := congrArg Prod.snd h
  change (sq_L M x).2 = 0 at this
  rw [sq_L_apply] at this
  simp only at this
  rcases div_eq_zero_iff.1 this with h | h
  · exact hV h
  · have : (0 : ℝ) < 4 * M := by positivity
    linarith

/-- `χ` is timelike where `UV < 0` (regions I and III): `g(χ, χ) < 0`. -/
theorem sq_timelike {x : ℝ × ℝ} (hx : x ∈ sq_Mset) (hUV : x.1 * x.2 < 0) :
    sq_g M x (sq_X M x) (sq_X M x) < 0 := by
  rw [sq_normSq hM]
  have := sq_FS_pos hM hx
  exact div_neg_of_neg_of_pos (mul_neg_of_pos_of_neg this hUV) (by positivity)

/-! ### The generator `γ s = (0, e^{s/4M})` -/

omit hM in
/-- The future horizon generator `γ s = (0, e^{s/4M})`, `U = 0`, `V > 0`. -/
noncomputable def sq_γ (M : ℝ) (s : ℝ) : ℝ × ℝ := (0, Real.exp (s / (4 * M)))

omit hM in
theorem sq_γ_fst (s : ℝ) : (sq_γ M s).1 = 0 := rfl

theorem sq_X_γ (s : ℝ) :
    sq_X M (sq_γ M s) = ((0 : ℝ), Real.exp (s / (4 * M)) / (4 * M)) := by
  show sq_L M _ = _
  rw [sq_L_apply]; simp [sq_γ]

theorem sq_hXne (s : ℝ) : sq_X M (sq_γ M s) ≠ 0 :=
  sq_X_ne hM (x := sq_γ M s) (Real.exp_pos _).ne'

/-- `γ` is an integral curve of `χ` (everywhere). -/
theorem sq_integral (t : ℝ) : IsMIntegralCurveAt (sq_γ M) (sq_X M) t := by
  refine Filter.Eventually.of_forall fun s => ?_
  have he : HasDerivAt (fun s : ℝ => Real.exp (s / (4 * M))) (Real.exp (s / (4 * M)) / (4 * M)) s := by
    have := ((hasDerivAt_id s).div_const (4 * M)).exp
    refine this.congr_deriv ?_
    simp only [id]; ring
  have hd : HasDerivAt (sq_γ M) ((0 : ℝ), Real.exp (s / (4 * M)) / (4 * M)) s :=
    (hasDerivAt_const s (0:ℝ)).prodMk he
  have h := hd.hasFDerivAt.hasMFDerivAt
  rw [sq_X_γ hM]
  exact h

omit hM in
theorem sq_γ_injective (hM : 0 < M) : Function.Injective (sq_γ M) := fun s t h => by
  have := Real.exp_injective (congrArg Prod.snd h)
  field_simp at this; exact this

theorem sq_γ_log {V : ℝ} (hV : 0 < V) : sq_γ M (4 * M * Real.log V) = ((0 : ℝ), V) := by
  simp only [sq_γ]
  rw [mul_div_cancel_left₀ _ (by positivity : (4 * M : ℝ) ≠ 0), Real.exp_log hV]

theorem sq_γ_mem (s : ℝ) : sq_γ M s ∈ sq_Mset := sq_horizon_mem rfl

end SQKilling

/-! ### 3b, `sq_cor_EF_coincident` -/

set_option maxHeartbeats 800000 in
/-- **3b, `sq_cor_EF_coincident`.** Schwarzschild in Kruskal's radial plane (`g = −F(r(U, V)) dU dV`,
`F = (32M³/r) e^{−r/2M}`, Killing `χ = (1/4M)(V∂_V − U∂_U) = ∂_t`), along the future horizon generator
`γ s = (0, e^{s/4M})`: for `0 < V₁ < V₂`, `p = (0, V₁) = γ a` and `q = (0, V₂) = γ b`
(`a = 4M log V₁ < b = 4M log V₂`) are distinct and **metrically coincident** (`kw_lemma_killing_whole`):
(a) `χ` and `γ′` are null along `[a, b]`; (b) they are related both ways by local isometries carrying the
generator into itself (`kg_Related`); `Δτ = 0` (`kg_deltaTau`); for the horizon splitting
`Δx = 0`, `Δτ = 0`, while the Killing parameter separates them (`∫ₐᵇ dλ(γ′) = b − a > 0`); and `r = 2M` at
both. -/
theorem sq_cor_EF_coincident {M : ℝ} (hM : 0 < M) {V₁ V₂ : ℝ} (h₁ : 0 < V₁) (h₁₂ : V₁ < V₂) :
    sq_γ M (4 * M * Real.log V₁) = ((0 : ℝ), V₁) ∧ sq_γ M (4 * M * Real.log V₂) = ((0 : ℝ), V₂) ∧
    ((0 : ℝ), V₁) ≠ ((0 : ℝ), V₂) ∧
    4 * M * Real.log V₁ < 4 * M * Real.log V₂ ∧
    (∀ t ∈ Icc (4 * M * Real.log V₁) (4 * M * Real.log V₂),
      sq_g M (sq_γ M t) (sq_X M (sq_γ M t)) (sq_X M (sq_γ M t)) = 0 ∧
      sq_g M (sq_γ M t) (mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, ℝ × ℝ) (sq_γ M) t (1 : ℝ))
        (mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, ℝ × ℝ) (sq_γ M) t (1 : ℝ)) = 0) ∧
    kg_Related (sq_g M) (sq_γ M) (4 * M * Real.log V₁) (4 * M * Real.log V₂) ∧
    kg_Related (sq_g M) (sq_γ M) (4 * M * Real.log V₂) (4 * M * Real.log V₁) ∧
    kg_deltaTau (sq_g M) (sq_X M) (sq_γ M) (4 * M * Real.log V₁) (4 * M * Real.log V₂) = 0 ∧
    (∃ σ : kw_AdaptedSplitting (sq_g M) (sq_γ M) (4 * M * Real.log V₁) (4 * M * Real.log V₂),
      σ.n = kw_n (sq_g M) (sq_X M) (sq_γ M) ∧ σ.dt = kw_dt (sq_X M) (sq_γ M) ∧
      σ.h = kw_h (sq_g M) (sq_X M) (sq_γ M) ∧ σ.Δx = 0 ∧ σ.Δτ = 0 ∧
      (∫ s in (4 * M * Real.log V₁)..(4 * M * Real.log V₂), σ.dt s (kw_vel (sq_γ M) s)) =
        4 * M * Real.log V₂ - 4 * M * Real.log V₁) ∧
    sq_rK M ((0 : ℝ), V₁) = 2 * M ∧ sq_rK M ((0 : ℝ), V₂) = 2 * M := by
  set a := 4 * M * Real.log V₁ with ha
  set b := 4 * M * Real.log V₂ with hb
  have hab : a < b := by
    simp only [ha, hb]
    exact mul_lt_mul_of_pos_left (Real.log_lt_log h₁ h₁₂) (by positivity)
  have hI : a ∈ Icc a b := ⟨le_rfl, hab.le⟩
  have hI' : b ∈ Icc a b := ⟨hab.le, le_rfl⟩
  have hγ : ∀ t ∈ Icc a b, IsMIntegralCurveAt (sq_γ M) (sq_X M) t := fun t _ => sq_integral hM t
  have hXne : ∀ t ∈ Icc a b, sq_X M (sq_γ M t) ≠ 0 := fun t _ => sq_hXne hM t
  obtain ⟨-, hA, hB, -, hD, -, -, hΔx, -, hΔτ⟩ :=
    kw_lemma_killing_whole (sq_X M) (sq_g M) (sq_γ M) a b a hab.le
    (fun t _ => sq_hX _) hXne
    (fun t _ => sq_hRep_nhds hM (by rw [extChartAt_model_space_eq_id]; exact sq_γ_mem hM t) _)
    (fun t _ => sq_lieDeriv_nhds hM (sq_γ_mem hM t))
    hγ hI (sq_null_horizon hM (sq_γ_fst a))
  have hdt : (∫ s in a..b,
      (kw_horizonSplitting (sq_g M) (sq_X M) (sq_γ M) a b (kw_vel_eq hγ) hXne).dt s
        (kw_vel (sq_γ M) s)) = b - a := by
    rw [intervalIntegral.integral_congr (g := fun _ => (1 : ℝ)) fun s hs => by
      rw [uIcc_of_le hab.le] at hs
      show kw_dt (sq_X M) (sq_γ M) s (kw_vel (sq_γ M) s) = 1
      rw [kw_vel_eq hγ s hs]; exact kw_dt_X (hXne s hs)]
    simp
  have hne : ((0 : ℝ), V₁) ≠ ((0 : ℝ), V₂) := fun h => h₁₂.ne (congrArg Prod.snd h)
  exact ⟨sq_γ_log hM h₁, sq_γ_log hM (h₁.trans h₁₂), hne, hab, hA, hB a hI b hI', hB b hI' a hI, hD,
    ⟨_, rfl, rfl, rfl, hΔx, hΔτ, hdt⟩, sq_rK_horizon hM rfl, sq_rK_horizon hM rfl⟩

/-- **`χ` is Killing on `M`, null on the horizon, timelike in region I** (the headline for ②'s Killing field).
Non-vacuous: `F` is not constant (`sq_FS_nonconst`), and `χ ≠ 0` along the generator. -/
theorem sq_killing {M : ℝ} (hM : 0 < M) :
    (∀ x ∈ sq_Mset, ∀ v w : ℝ × ℝ, lieDeriv (sq_X M) (sq_g M) x v w = 0) ∧
    (∀ x : ℝ × ℝ, sq_g M x (sq_X M x) (sq_X M x) = sq_FS M x * (x.1 * x.2) / (16 * M ^ 2)) ∧
    (∀ x : ℝ × ℝ, x.1 = 0 → sq_g M x (sq_X M x) (sq_X M x) = 0 ∧ sq_rK M x = 2 * M) ∧
    (∀ x : ℝ × ℝ, x.1 = 0 → x.2 ≠ 0 → sq_X M x ≠ 0) ∧
    (∀ s, IsMIntegralCurveAt (sq_γ M) (sq_X M) s) ∧
    sq_FS M (-1, Real.exp 2) ≠ sq_FS M (0, 1) :=
  ⟨fun _ hx v w => sq_lieDeriv hM hx v w, sq_normSq hM,
    fun _ hx => ⟨sq_null_horizon hM hx, sq_rK_horizon hM hx⟩, fun _ _ hV => sq_X_ne hM hV,
    sq_integral hM, (sq_FS_nonconst hM).2.2⟩

end SQRadius

end ShadowProbe.SchwarzschildKillingProbe

#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_remainder_unif
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_local_flow
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_flow_bounded
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_linear_exists
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_gronwall_fwd
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_gronwall_symm
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_gronwallBound_le
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_flowData_exists
#print axioms ShadowProbe.SchwarzschildKillingProbe.FlowData.ld_Icc_mem
#print axioms ShadowProbe.SchwarzschildKillingProbe.FlowData.ld_alpha_continuousOn
#print axioms ShadowProbe.SchwarzschildKillingProbe.FlowData.ld_var_exists
#print axioms ShadowProbe.SchwarzschildKillingProbe.FlowData.ld_J_spec
#print axioms ShadowProbe.SchwarzschildKillingProbe.FlowData.ld_C_nonneg
#print axioms ShadowProbe.SchwarzschildKillingProbe.FlowData.ld_gb_le
#print axioms ShadowProbe.SchwarzschildKillingProbe.FlowData.ld_J_norm_le
#print axioms ShadowProbe.SchwarzschildKillingProbe.FlowData.ld_remainder_uniform
#print axioms ShadowProbe.SchwarzschildKillingProbe.FlowData.ld_J_uniform
#print axioms ShadowProbe.SchwarzschildKillingProbe.FlowData.ld_flow_hasFDerivAt
#print axioms ShadowProbe.SchwarzschildKillingProbe.FlowData.ld_J_continuousOn
#print axioms ShadowProbe.SchwarzschildKillingProbe.FlowData.ld_flow_contDiffOn
#print axioms ShadowProbe.SchwarzschildKillingProbe.FlowData.ld_U_open
#print axioms ShadowProbe.SchwarzschildKillingProbe.FlowData.ld_Dflow_apply
#print axioms ShadowProbe.SchwarzschildKillingProbe.FlowData.ld_J_continuousAt_joint
#print axioms ShadowProbe.SchwarzschildKillingProbe.FlowData.ld_flow_hasFDerivAt_joint
#print axioms ShadowProbe.SchwarzschildKillingProbe.FlowData.ld_flow_continuousOn_joint
#print axioms ShadowProbe.SchwarzschildKillingProbe.FlowData.ld_Dflow_continuousOn
#print axioms ShadowProbe.SchwarzschildKillingProbe.FlowData.ld_flow_contDiffOn_joint
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_flow_C1
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_complement_equiv
#print axioms ShadowProbe.SchwarzschildKillingProbe.FlowData.ld_flowBox
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_flowBox_exists
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_cutoff
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_flowData_small
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_agree
#print axioms ShadowProbe.SchwarzschildKillingProbe.FlowData.ld_x₀_mem
#print axioms ShadowProbe.SchwarzschildKillingProbe.FlowData.ld_transfer_J
#print axioms ShadowProbe.SchwarzschildKillingProbe.FlowData.ld_isFlowBox_mem
#print axioms ShadowProbe.SchwarzschildKillingProbe.FlowData.ld_transfer_isFlowBox
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_flowData_exists_of_contDiffOn
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_flowBox_exists_of_contDiffOn
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_flowBox_chart_of_contDiffOn
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_chartRep_inv
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_mdifferentiableAt_symm
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_manifold_flowBox
#print axioms ShadowProbe.SchwarzschildKillingProbe.FlowData.ld_flow_pushes_field_loc
#print axioms ShadowProbe.SchwarzschildKillingProbe.FlowData.ld_flow_pushes_field
#print axioms ShadowProbe.SchwarzschildKillingProbe.FlowData.ld_flow_isometry_loc
#print axioms ShadowProbe.SchwarzschildKillingProbe.FlowData.ld_flow_isometry
#print axioms ShadowProbe.SchwarzschildKillingProbe.FlowData.ld_flowBox_pullback_loc
#print axioms ShadowProbe.SchwarzschildKillingProbe.FlowData.ld_flowBox_pullback
#print axioms ShadowProbe.SchwarzschildKillingProbe.FlowData.ld_flowBox_killing
#print axioms ShadowProbe.SchwarzschildKillingProbe.FlowData.ld_transfer_isVar
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_flowBox_exists_of_contDiffOn_var
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_flowBox_killing_of_contDiffOn
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_isKilling_lie
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_flowBox_killing_of_isKilling
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_chartRep_eq_triv
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_chartRep_contDiffAt_of_triv
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_chartRep_contDiffAt_of_section
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_chartRep_ball_of_contDiffAt
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_chartRep_ball_of_section
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_chartRep_ne_zero
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_mfderiv_straightens
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_manifold_flowBox_of_contDiffAt
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_manifold_flowBox_section
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_chartRep_contDiffOn_of_section
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_manifold_flowBox_sectionOn
#print axioms ShadowProbe.SchwarzschildKillingProbe.LocalKillingChart.ld_lambda_indep
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_manifold_killingChart
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_manifold_killingChart_section
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_chartLie_core
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_hRep_apply
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_mfderiv_symm_chart
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_mfderiv_chart_symm
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_chartRep_apply_chart
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_h_eq_hRep
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_lieDerivForm_chart_of_bracket
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_mlieBracket_chart_self
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_constExt_self
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_chartRep_constExt
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_chartRep_constExt_contDiffAt
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_lieDerivForm_chart_self
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_lieDeriv_chart_self
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_lieDerivForm_eq_lieDeriv
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_mlieBracket_model
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_lieDerivForm_model
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_isKilling_of_chartLie
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_mlieBracket_chart
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_chartRep_contDiffAt_of_section_chart
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_constExt_section
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_lieDerivForm_chart
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_lieDeriv_chart
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_chartLie_zero_of_lieDeriv
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_isKilling_of_lieDeriv
#print axioms ShadowProbe.SchwarzschildKillingProbe.ld_manifold_killingChart_lieDeriv
#print axioms ShadowProbe.SchwarzschildKillingProbe.LocalKillingChart.ld_metric_N

-- new (campaign 94 ②)
#print axioms ShadowProbe.SchwarzschildKillingProbe.kl_psi_zero
#print axioms ShadowProbe.SchwarzschildKillingProbe.kl_velocity
#print axioms ShadowProbe.SchwarzschildKillingProbe.kl_psi_injOn
#print axioms ShadowProbe.SchwarzschildKillingProbe.kl_orbit_ne
#print axioms ShadowProbe.SchwarzschildKillingProbe.kl_exists_eps
#print axioms ShadowProbe.SchwarzschildKillingProbe.kl_uIcc_abs_lt
#print axioms ShadowProbe.SchwarzschildKillingProbe.kl_comps_eq_gH
#print axioms ShadowProbe.SchwarzschildKillingProbe.kl_lambda_indep_N
#print axioms ShadowProbe.SchwarzschildKillingProbe.kl_normSq_eq_comps
#print axioms ShadowProbe.SchwarzschildKillingProbe.kl_interval_orbit
#print axioms ShadowProbe.SchwarzschildKillingProbe.kl_forcing
#print axioms ShadowProbe.SchwarzschildKillingProbe.kl_normSq_orbit_const
#print axioms ShadowProbe.SchwarzschildKillingProbe.kl_null_along_orbit
#print axioms ShadowProbe.SchwarzschildKillingProbe.kl_lemma_killing_chart
#print axioms ShadowProbe.SchwarzschildKillingProbe.kl_lemma_killing_local
#print axioms ShadowProbe.SchwarzschildKillingProbe.kl_chartLie_const
#print axioms ShadowProbe.SchwarzschildKillingProbe.kl_psi_model
#print axioms ShadowProbe.SchwarzschildKillingProbe.kl_model_orbit
#print axioms ShadowProbe.SchwarzschildKillingProbe.kl_w_B_apply
#print axioms ShadowProbe.SchwarzschildKillingProbe.kl_w_lorentzian
#print axioms ShadowProbe.SchwarzschildKillingProbe.kl_w_mfderiv_chart
#print axioms ShadowProbe.SchwarzschildKillingProbe.kl_w_mfderiv_chart_symm
#print axioms ShadowProbe.SchwarzschildKillingProbe.kl_w_hRep
#print axioms ShadowProbe.SchwarzschildKillingProbe.kl_w_chartRep
#print axioms ShadowProbe.SchwarzschildKillingProbe.kl_w_lieDeriv
#print axioms ShadowProbe.SchwarzschildKillingProbe.kl_w_hX
#print axioms ShadowProbe.SchwarzschildKillingProbe.kl_w_hXp
#print axioms ShadowProbe.SchwarzschildKillingProbe.kl_w_null
#print axioms ShadowProbe.SchwarzschildKillingProbe.kl_witness

-- new (campaign 95, `r7671+71`)
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_flowBox_killing_symm
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_restrict_source
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_restrict_symmC1
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_killingChart_symm
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_chi_psi
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_psi_mem_dom
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_psi_chi
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_chi_mem
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_dom_open
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_chi_mdiff
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_U_open
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_psi_mdiff
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_dpsi_dchi
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_add_mdiff
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_shift_hasMFDerivAt
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_shift_mdiff
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_mfderiv_shift
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_g_congr
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_shift_isometry
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_psi_mem_U
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_shift_psi
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_orbit_hasMFDerivAt
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_curve_eq_orbit
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_related_trans
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_box_along
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_related_box
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_normSq_box
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_lapse_null
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_deltaTau_zero
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_lemma_killing_generator
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_w_B_apply
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_w_lorentzian
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_w_L_apply
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_w_normSq
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_w_boost_generator
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_w_boost_isometry
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_w_hRep
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_w_chartRep
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_w_chartLie
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_w_lieDeriv
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_w_hX
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_w_X_γ
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_w_hXne
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_w_integral
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_w_null
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_w_injOn
#print axioms ShadowProbe.SchwarzschildKillingProbe.kg_witness
#print axioms ShadowProbe.SchwarzschildKillingProbe.«kw_dλ_exists»
#print axioms ShadowProbe.SchwarzschildKillingProbe.kw_AdaptedSplitting.kw_g_vel
#print axioms ShadowProbe.SchwarzschildKillingProbe.kw_eq_zero_of_integral_eq_zero
#print axioms ShadowProbe.SchwarzschildKillingProbe.kw_metric_singularity_along
#print axioms ShadowProbe.SchwarzschildKillingProbe.kw_dt_X
#print axioms ShadowProbe.SchwarzschildKillingProbe.kw_split
#print axioms ShadowProbe.SchwarzschildKillingProbe.kw_h_X
#print axioms ShadowProbe.SchwarzschildKillingProbe.kw_vel_eq
#print axioms ShadowProbe.SchwarzschildKillingProbe.kw_lemma_killing_whole
#print axioms ShadowProbe.SchwarzschildKillingProbe.kw_witness

-- new (campaign 97 ②, `r7675+71`)
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_smul_hasFDerivAt
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_smul_fderiv_apply
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_hasDerivAt_hK
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_continuous_hK
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_hK_strictMonoOn
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_hK_zero
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_hK_two
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_hK_gt
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_hK_exists
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_rinv_spec
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_rinv_hK
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_rinv_zero
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_rinv_strictMonoOn
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_rinv_continuousAt
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_rinv_hasDerivAt
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_rinv_contDiffAt
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_Mset_open
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_horizon_mem
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_FS_comp
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_Mset_UV
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_rK_spec
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_rK_horizon
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_rK_contDiffAt
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_FS_pos
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_fS_contDiffAt
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_FS_contDiffAt
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_FS_horizon
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_FS_nonconst
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_gM_apply
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_metric_formula
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_lorentzian
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_L_apply
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_chi_UV
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_chi_F
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_FS_diff
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_gM_diff
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_hRep
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_chartRep
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_chartLie
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_lieDeriv
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_lieDeriv_nhds
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_hRep_nhds
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_hX
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_normSq
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_null_horizon
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_X_ne
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_timelike
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_γ_fst
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_X_γ
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_hXne
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_integral
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_γ_injective
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_γ_log
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_γ_mem
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_cor_EF_coincident
#print axioms ShadowProbe.SchwarzschildKillingProbe.sq_killing

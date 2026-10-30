import Mathlib

/-!
# Probe `r7641+71.2` (campaign 77, `r7641` ①): the causal-`P` bootstrap for a merely Lipschitz
# start, generators of `𝓗⁺` as null geodesics without the `C¹`-start hypotheses, and the tangent
# hyperplane of `𝓗⁺` at a generator point

Registration: `computations/formalisation/r7641_71_campaign77/PREDICTION.md`. Nothing imports this
file, and it imports no other probe.

## Copied (from campaign 76's `probes/ConoidBootstrap.lean`)

Campaign 76's probe, itself campaigns 62/70/71/61/73 plus campaign 76's new material, under the
namespace `ShadowProbe.LipschitzBootstrapProbe`, with every `cb_` ↦ `lb_`, `cbψ` ↦ `lbψ`,
`cbBump` ↦ `lbBump`: the `C¹` flow, the geodesic spray and `exp_p`, the Gauss lemma, the normal
chart `Φ`, `good`, `Q`, the position field `P`, `lb_grad_Q`, `lb_P_energy`, `CC`,
`lb_reverse_cs`, `lb_chr_of_Q_neg`, `lb_H_achronal`, the ray lemma, `lb_generator_null_geodesic`,
`lb_H_generator_radial_pregeodesic`, `lb_conoid_regular`, and from campaign 76: `lb_near_conoid`,
`lb_le_of_ae_deriv`, `lb_gronwall_step`, `lb_bootstrap`, `lb_orient`, `lb_orient_chart`,
`lb_Dexp_tendsto`, `lb_fderiv_symm_p`, `lb_exists_ball_small`, `lb_generator_Q_zero`.

**Trimmed:** campaign 76's `cb_small_t`, `cb_causal_in_conoid`, `cb_H_generator_null_geodesic`
and `cb_generator_conoid_tangent` (the `C¹`-start versions) are not copied; the new versions below
supersede them (same conclusions, strictly fewer hypotheses).

## New: ① the Lipschitz-start bootstrap — BUILT (no named hypothesis needed)

* `lb_cone_const` (BUILT): near `p ∈ M` there are `r, c > 0` with `−g_x(w, T x) ≥ c ‖w‖` for all
  `x ∈ closedBall p r`, `w ∈ CC x` (compactness).
* `lb_expansion` (BUILT): the uniform first-order expansion of `exp_p⁻¹` at `p`, the registered
  "reachable negative" item. For every `η > 0`, near `p`: `‖D(exp⁻¹)(x)‖ ≤ 2`,
  `‖g_p(T p, D(exp⁻¹)(x)·) − g_x(T x, ·)‖ ≤ η`, `‖g_x(T x, D exp(exp⁻¹x)·) − g_p(T p, ·)‖ ≤ η`.
  It follows from continuity of `D(exp⁻¹)` at `p` and of `D exp` at `0`, so it was *not* heavy and
  is **not** a named hypothesis.
* **`lb_small_t`** (BUILT): Lipschitz causal curve from `p` in the normal ball, avoiding `p` on
  `(0,1]` ⟹ `P(γ t) ∈ CC` on some `(0,ε]`. *Deviation from the registered route, same idea:*
  time is measured by the normal-coordinate time `a(t) = −g_p(exp_p⁻¹ γ(t), T p)` instead of the
  `T`-arclength `s(t) = ∫₀ᵗ −g(γ′,T)`. The two agree to first order (`a′ ≥ (29/30) s′` a.e.
  near `0`), and `a` needs no integral. The registered steps become: (1) `c ‖exp⁻¹ γ t‖ ≤ 3 a(t)`
  (compare the derivatives with the cone constant; Hahn–Banach for the norm); (2)
  `−g(P(γ t),T) ≥ (9/10) a(t)` (from `lb_expansion`; no causality of `P` used); (3)
  `lb_near_conoid` gives `(Q∘γ)′ ≤ (10/9)(30/29) a′ Q⁺/a` a.e.; (4) from `Q ≤ r a²` this gives
  `Q ≤ (3/5) r a²`, starting from `Q ≤ r₀ a²`; iterating, `Q ≤ 0`. The vertex issue "`s ≡ 0` near
  `0`" does not arise: `hne` (`γ ≠ p` on `(0,1]`) together with (1) gives `a > 0` on `(0,ε]`.
* **`lb_causal_in_conoid`** (BUILT): campaign 76's `cb_causal_in_conoid` with `u`, `hu`, `hd0`,
  `hC1` **removed**. Conclusion: `P(γ t) ∈ CC`, `g(P,T) < 0` on `(0,1]`, `Q ∘ γ ≤ 0` on `[0,1]`.
* **`lb_H_generator_null_geodesic`** (BUILT): campaign 76's `cb_H_generator_null_geodesic` with
  `u`, `hu`, `hd0`, `hC1` **removed**: a Lipschitz curve from `p` in `H = ∂J⁻(J)`, velocity a.e.
  in the closed future cone, in a small normal ball, avoiding `p` after `t = 0`, has `Q ∘ γ = 0`
  and reparametrises one `C²` radial null geodesic (null, pregeodesic on `(0,1)`).

## New: ② the tangent hyperplane of `𝓗⁺` — BUILT (the registered one-sided form)

* `lb_H_Q_nonneg_near` (BUILT): at `x ≠ p` with `Q x = 0`, `P x` future, `exp⁻¹ x` small, and
  `p ∈ H J`, every point of `H J` near `x` has `Q ≥ 0` (route as registered: `Q < 0` nearby ⟹
  future small `exp⁻¹` by continuity ⟹ `p ≪ y` by `lb_chr_of_Q_neg` ⟹ excluded by
  `lb_H_achronal`).
* **`lb_tangent_hyperplane`** (BUILT): every curve `c` with `c 0 = x`, `HasDerivAt c c′ 0` and
  `c t ∈ H J` for `t` near `0` has `DQ(x)(c′) = 0`, i.e. `g_x(P x, c′) = 0` (local minimum of
  `Q ∘ c`). Only differentiability at `0` is used (weaker than `C¹`).
* **`lb_generator_tangent_hyperplane`** (BUILT): along a generator as in
  `lb_H_generator_null_geodesic`, at every `t ∈ (0,1]`: `P(γ t)` is nonzero (`DQ ≠ 0`), future,
  null, and every such curve in `H J` through `γ t` has velocity in `P(γ t)^⊥ = ker DQ(γ t)`. So
  where `𝓗⁺` has a tangent hyperplane there, it is the null hyperplane of the generator.
* Not attempted, as registered: the reverse inclusion "`𝓗⁺` locally equals the conoid".

## Non-vacuity of the main theorems

* `lb_small_t` / `lb_causal_in_conoid`: **`lb_nonvacuous`** (BUILT) proves that in *every*
  `Spacetime` with `g ∈ C²`, for every geodesic-flow datum and normal chart at `p` (these exist
  for every `p ∈ M`: `lb_geoFlow_exists`, `lb_normalChart_exists`), the hypotheses `hB`, `hlip`,
  `hmem`, `h0`, `hne`, `hcausal` are jointly satisfied, by the short segment
  `γ t = p + (t δ) • T p`. So the conclusion is genuinely obtained, not vacuously.
* `lb_H_generator_null_geodesic`, `lb_generator_tangent_hyperplane`: on top of the above they need
  `hsmall` (satisfiable: `lb_exists_ball_small`) and `γ ⊆ H J`. These are consistent: in
  Minkowski space with `J = {q}`, `q = p + k`, `k` future null and small, `H J = ∂J⁻(q)` is the
  past null cone of `q`, which contains the straight null segment `γ t = p + t k`. That segment is
  Lipschitz, has null future velocity, starts at `p` and avoids `p` afterwards. The membership in
  `H J` is argued here, not proved in Lean (it needs `J⁻` of flat space).
* `lb_tangent_hyperplane`: its hypotheses are exactly what `lb_generator_tangent_hyperplane`
  derives at each generator point, so they are consistent whenever the generator hypotheses are
  (Minkowski example above). The curve hypothesis is satisfied at least by the constant curve
  `c ≡ x`, and in the example by the generator itself and by any curve in the past cone of `q`.
  The hypotheses do not force continuity at a point where something must blow up: everything is
  evaluated at `x ≠ p`, where `Q` is `C¹` and `DQ ≠ 0`.
-/

open Set Filter Topology Metric
open scoped NNReal

set_option linter.unusedSectionVars false

namespace ShadowProbe.LipschitzBootstrapProbe

section FlowCopy

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]

/-! ## Copied from campaign 62 (`probes/FlowC1.lean`, `fc_` ↦ `lb_`): the `C¹` local flow -/


/-- **1.** The first-order remainder of a `C¹` map is uniformly small on a closed ball. -/
theorem lb_remainder_unif (f : E → E) (hf : ContDiff ℝ 1 f) (x₀ : E) (R ε : ℝ) (hε : 0 < ε) :
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
theorem lb_local_flow (f : E → E) (hf : ContDiff ℝ 1 f) (x₀ : E) :
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
theorem lb_flow_bounded (f : E → E) (τ r : ℝ) (α : E → ℝ → E) (L : ℝ≥0) (x₀ : E)
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
theorem lb_linear_exists [CompleteSpace F] (A : ℝ → F →L[ℝ] F) (T M : ℝ) (hT : 0 ≤ T) (hM : 0 ≤ M)
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
theorem lb_gronwall_fwd (e e' : ℝ → F) (T δ K c : ℝ)
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
theorem lb_gronwall_symm (e e' : ℝ → F) (T δ K c : ℝ)
    (he : ∀ s ∈ Icc (-T) T, HasDerivWithinAt e (e' s) (Icc (-T) T) s) (h0 : ‖e 0‖ ≤ δ)
    (hb : ∀ s ∈ Icc (-T) T, ‖e' s‖ ≤ K * ‖e s‖ + c) :
    ∀ s ∈ Icc (-T) T, ‖e s‖ ≤ gronwallBound δ K c |s| := by
  intro s hs
  rcases le_total 0 s with h | h
  · rw [abs_of_nonneg h]; exact lb_gronwall_fwd e e' T δ K c he h0 hb s ⟨h, hs.2⟩
  · have hneg : ∀ u ∈ Icc (-T) T, -u ∈ Icc (-T) T := fun u hu => ⟨by linarith [hu.2], by linarith [hu.1]⟩
    have := lb_gronwall_fwd (fun u => e (-u)) (fun u => -e' (-u)) T δ K c
      (fun u hu => by
        have := (he (-u) (hneg u hu)).scomp u ((hasDerivAt_neg u).hasDerivWithinAt)
          (fun w hw => hneg w hw)
        simpa [Function.comp_def] using this)
      (by simpa using h0) (fun u hu => by simpa using hb (-u) (hneg u hu)) (-s)
      ⟨by linarith, by linarith [hs.1]⟩
    rw [abs_of_nonpos h]; simpa using this

end Linear

/-- The Grönwall bound with `δ = 0`, linear in `c`, uniformly on `[0, T]`. -/
theorem lb_gronwallBound_le (K c x T : ℝ) (hK : 0 < K) (hc : 0 ≤ c) (hxT : x ≤ T) :
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
theorem lb_flowData_exists (hf : ContDiff ℝ 1 f) (x₀ : E) : Nonempty (FlowData f x₀) := by
  obtain ⟨τ₀, hτ₀, r, hr, α, L, hα, hL⟩ := lb_local_flow f hf x₀
  obtain ⟨R, hR⟩ := lb_flow_bounded f τ₀ r α L x₀ hα hL
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

theorem lb_Icc_mem {t : ℝ} (ht : t ∈ Icc (-D.τ) D.τ) : |t| ≤ D.τ := abs_le.2 ht

theorem lb_alpha_continuousOn (x : E) (hx : x ∈ closedBall x₀ D.r) :
    ContinuousOn (D.α x) (Icc (-D.τ) D.τ) :=
  fun t ht => (D.deriv x hx t ht).continuousWithinAt

theorem lb_var_exists (hf : ContDiff ℝ 1 f) (x : E) (hx : x ∈ closedBall x₀ D.r) :
    ∃ W, D.IsVar x W := by
  obtain ⟨W, hW0, hW⟩ := lb_linear_exists
    (fun t => ContinuousLinearMap.compL ℝ E E E (fderiv ℝ f (D.α x t))) D.τ D.M D.τ_pos.le
    D.M_pos.le D.Mτ
    ((ContinuousLinearMap.compL ℝ E E E).continuous.comp_continuousOn
      ((hf.continuous_fderiv one_ne_zero).comp_continuousOn (D.lb_alpha_continuousOn x hx)))
    (fun t ht => ContinuousLinearMap.opNorm_le_bound _ D.M_pos.le fun W =>
      ((ContinuousLinearMap.opNorm_comp_le _ _).trans
        (mul_le_mul_of_nonneg_right (D.dbound _ (D.mem x hx t ht)) (norm_nonneg _))))
    (ContinuousLinearMap.id ℝ E)
  exact ⟨W, hW0, fun t ht => by simpa using hW t ht⟩

theorem lb_J_spec (hf : ContDiff ℝ 1 f) (x : E) (hx : x ∈ closedBall x₀ D.r) :
    D.IsVar x (D.J x) := by
  have h := D.lb_var_exists hf x hx
  unfold J; rw [dite_eq_left h]; exact h.choose_spec

/-- The constant of the Grönwall bound on `[-τ, τ]`. -/
noncomputable def C : ℝ := (Real.exp (D.M * D.τ) - 1) / D.M

theorem lb_C_nonneg : 0 ≤ D.C := by
  unfold C
  have : 1 ≤ Real.exp (D.M * D.τ) := Real.one_le_exp (by nlinarith [D.M_pos, D.τ_pos])
  exact div_nonneg (by linarith) D.M_pos.le

theorem lb_gb_le {c s : ℝ} (hc : 0 ≤ c) (hs : s ∈ Icc (-D.τ) D.τ) :
    gronwallBound 0 D.M c |s| ≤ c * D.C :=
  lb_gronwallBound_le _ _ _ _ D.M_pos hc (D.lb_Icc_mem hs)

/-- `‖J x s‖ ≤ exp (M τ)` on `[-τ, τ]`. -/
theorem lb_J_norm_le (hf : ContDiff ℝ 1 f) (x : E) (hx : x ∈ closedBall x₀ D.r)
    (s : ℝ) (hs : s ∈ Icc (-D.τ) D.τ) : ‖D.J x s‖ ≤ Real.exp (D.M * D.τ) := by
  obtain ⟨h0, hd⟩ := D.lb_J_spec hf x hx
  have := lb_gronwall_symm (D.J x) (fun t => (fderiv ℝ f (D.α x t)).comp (D.J x t)) D.τ 1 D.M 0 hd
    (by rw [h0]; exact ContinuousLinearMap.norm_id_le)
    (fun t ht => by
      rw [add_zero]
      exact (ContinuousLinearMap.opNorm_comp_le _ _).trans
        (mul_le_mul_of_nonneg_right (D.dbound _ (D.mem x hx t ht)) (norm_nonneg _))) s hs
  rw [gronwallBound_ε0, one_mul] at this
  exact this.trans (Real.exp_le_exp.2 (mul_le_mul_of_nonneg_left (D.lb_Icc_mem hs) D.M_pos.le))

/-- **Grönwall #1, uniform in time.** `‖α y s − α x s − J x s (y − x)‖ ≤ ε ‖y − x‖` for `y` near `x`,
for every `s ∈ [-τ, τ]` at once. -/
theorem lb_remainder_uniform (hf : ContDiff ℝ 1 f) (x : E) (hx : x ∈ closedBall x₀ D.r)
    (ε : ℝ) (hε : 0 < ε) :
    ∃ δ > 0, ∀ y ∈ closedBall x₀ D.r, ‖y - x‖ < δ → ∀ s ∈ Icc (-D.τ) D.τ,
      ‖D.α y s - D.α x s - D.J x s (y - x)‖ ≤ ε * ‖y - x‖ := by
  set ε' := ε / (((D.L : ℝ) + 1) * (D.C + 1)) with hε'
  have hC := D.lb_C_nonneg
  have hε'0 : 0 < ε' := by positivity
  obtain ⟨δ₀, hδ₀, hrem⟩ := lb_remainder_unif f hf x₀ D.R ε' hε'0
  refine ⟨δ₀ / ((D.L : ℝ) + 1), by positivity, fun y hy hyx s hs => ?_⟩
  obtain ⟨hJ0, hJd⟩ := D.lb_J_spec hf x hx
  have hlip : ∀ s ∈ Icc (-D.τ) D.τ, ‖D.α y s - D.α x s‖ ≤ D.L * ‖y - x‖ :=
    fun s hs => (D.lip s hs).norm_sub_le hy hx
  have hclose : ∀ s ∈ Icc (-D.τ) D.τ, ‖D.α y s - D.α x s‖ < δ₀ := fun s hs => by
    have h1 := hlip s hs
    have h2 : ((D.L : ℝ) + 1) * ‖y - x‖ < δ₀ := by
      rwa [lt_div_iff₀ (by positivity), mul_comm] at hyx
    nlinarith [norm_nonneg (y - x)]
  have key := lb_gronwall_symm (fun s => D.α y s - D.α x s - D.J x s (y - x))
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
  refine key.trans ((D.lb_gb_le (by positivity) hs).trans ?_)
  have : ε' * D.L * D.C ≤ ε := by
    rw [hε']
    rw [div_mul_eq_mul_div, div_mul_eq_mul_div, div_le_iff₀ (by positivity)]
    nlinarith [mul_le_mul (le_add_of_nonneg_right zero_le_one : (D.L : ℝ) ≤ D.L + 1)
      (le_add_of_nonneg_right zero_le_one : D.C ≤ D.C + 1) hC (by positivity)]
  nlinarith [norm_nonneg (y - x)]

/-- **Grönwall #2, uniform in time.** `‖J y s − J x s‖ ≤ ε` for `y` near `x`, every `s ∈ [-τ, τ]`. -/
theorem lb_J_uniform (hf : ContDiff ℝ 1 f) (x : E) (hx : x ∈ closedBall x₀ D.r)
    (ε : ℝ) (hε : 0 < ε) :
    ∃ δ > 0, ∀ y ∈ closedBall x₀ D.r, ‖y - x‖ < δ → ∀ s ∈ Icc (-D.τ) D.τ,
      ‖D.J y s - D.J x s‖ ≤ ε := by
  set B := Real.exp (D.M * D.τ) with hB
  have hB0 : 0 < B := Real.exp_pos _
  have hC := D.lb_C_nonneg
  set ε' := ε / (B * (D.C + 1)) with hε'
  have hε'0 : 0 < ε' := by positivity
  have hU : UniformContinuousOn (fderiv ℝ f) (closedBall x₀ D.R) :=
    (isCompact_closedBall x₀ D.R).uniformContinuousOn_of_continuous
      (hf.continuous_fderiv one_ne_zero).continuousOn
  obtain ⟨δ₀, hδ₀, hδ⟩ := Metric.uniformContinuousOn_iff.1 hU ε' hε'0
  refine ⟨δ₀ / ((D.L : ℝ) + 1), by positivity, fun y hy hyx s hs => ?_⟩
  obtain ⟨hJ0x, hJdx⟩ := D.lb_J_spec hf x hx
  obtain ⟨hJ0y, hJdy⟩ := D.lb_J_spec hf y hy
  have hDf : ∀ s ∈ Icc (-D.τ) D.τ, ‖fderiv ℝ f (D.α y s) - fderiv ℝ f (D.α x s)‖ ≤ ε' := by
    intro s hs
    have h1 := (D.lip s hs).norm_sub_le hy hx
    have h2 : ((D.L : ℝ) + 1) * ‖y - x‖ < δ₀ := by
      rwa [lt_div_iff₀ (by positivity), mul_comm] at hyx
    rw [← dist_eq_norm]
    refine (hδ _ (D.mem y hy s hs) _ (D.mem x hx s hs) ?_).le
    rw [dist_eq_norm]; nlinarith [norm_nonneg (y - x)]
  have key := lb_gronwall_symm (fun s => D.J y s - D.J x s)
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
      have h5 := D.lb_J_norm_le hf x hx s hs
      nlinarith [norm_nonneg (D.J y s - D.J x s), norm_nonneg (D.J x s),
        norm_nonneg (fderiv ℝ f (D.α y s) - fderiv ℝ f (D.α x s))])
    s hs
  refine key.trans ((D.lb_gb_le (by positivity) hs).trans ?_)
  rw [hε', div_mul_eq_mul_div, div_mul_eq_mul_div, div_le_iff₀ (by positivity)]
  nlinarith [mul_le_mul_of_nonneg_left (le_add_of_nonneg_right zero_le_one : D.C ≤ D.C + 1) hB0.le]

/-! ## ① The flow is differentiable, and `C¹`, in the initial point -/

/-- **① (a), T3b's stop.** `y ↦ α y t` has derivative `J x t` at every `x ∈ ball x₀ r`, `t ∈ [-τ, τ]`. -/
theorem lb_flow_hasFDerivAt (hf : ContDiff ℝ 1 f) (x : E) (hx : x ∈ ball x₀ D.r)
    (t : ℝ) (ht : t ∈ Icc (-D.τ) D.τ) : HasFDerivAt (fun y => D.α y t) (D.J x t) x := by
  rw [hasFDerivAt_iff_isLittleO]
  refine Asymptotics.IsLittleO.of_bound fun c hc => ?_
  obtain ⟨δ, hδ, h⟩ := D.lb_remainder_uniform hf x (ball_subset_closedBall hx) c hc
  filter_upwards [ball_mem_nhds x hδ, isOpen_ball.mem_nhds hx] with y hy1 hy2
  rw [mem_ball, dist_eq_norm] at hy1
  exact h y (ball_subset_closedBall hy2) hy1 t ht

/-- **① (b).** The derivative `x ↦ J x t` is continuous on `closedBall x₀ r`, uniformly in `t`. -/
theorem lb_J_continuousOn (hf : ContDiff ℝ 1 f) (t : ℝ) (ht : t ∈ Icc (-D.τ) D.τ) :
    ContinuousOn (fun x => D.J x t) (closedBall x₀ D.r) := by
  intro x hx
  rw [Metric.continuousWithinAt_iff]
  intro ε hε
  obtain ⟨δ, hδ, h⟩ := D.lb_J_uniform hf x hx (ε / 2) (half_pos hε)
  refine ⟨δ, hδ, fun y hy hyx => ?_⟩
  rw [dist_eq_norm] at hyx ⊢
  exact (h y hy hyx t ht).trans_lt (half_lt_self hε)

/-- **① (c).** For every `t ∈ [-τ, τ]`, `x ↦ α x t` is `C¹` on `ball x₀ r`. -/
theorem lb_flow_contDiffOn (hf : ContDiff ℝ 1 f) (t : ℝ) (ht : t ∈ Icc (-D.τ) D.τ) :
    ContDiffOn ℝ 1 (fun y => D.α y t) (ball x₀ D.r) := fun _x hx =>
  (contDiffAt_one_iff.2 ⟨fun y => D.J y t, ball x₀ D.r, isOpen_ball.mem_nhds hx,
    (D.lb_J_continuousOn hf t ht).mono ball_subset_closedBall,
    fun y hy => D.lb_flow_hasFDerivAt hf y hy t ht⟩).contDiffWithinAt


end FlowData

end FlowCopy

/-! ## New flow facts: uniqueness in the ball, fixed points, Lipschitz bound at a fixed point -/

section FlowExtra

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
variable {f : E → E} {x₀ : E}

namespace FlowData

variable (D : FlowData f x₀)

/-- The field is `M`-Lipschitz on `closedBall x₀ R`. -/
theorem lb_field_lip (hf : ContDiff ℝ 1 f) {y z : E} (hy : y ∈ closedBall x₀ D.R)
    (hz : z ∈ closedBall x₀ D.R) : ‖f y - f z‖ ≤ D.M * ‖y - z‖ :=
  (convex_closedBall x₀ D.R).norm_image_sub_le_of_norm_fderiv_le
    (fun w _ => hf.differentiable one_ne_zero w) D.dbound hz hy

/-- **Uniqueness** (Grönwall): a solution through `x` on `[-τ, τ]` that stays in
`closedBall x₀ R` is the flow line `α x`. -/
theorem lb_unique (hf : ContDiff ℝ 1 f) {x : E} (hx : x ∈ closedBall x₀ D.r) {β : ℝ → E}
    (hβ0 : β 0 = x)
    (hβ : ∀ t ∈ Icc (-D.τ) D.τ, HasDerivWithinAt β (f (β t)) (Icc (-D.τ) D.τ) t)
    (hmem : ∀ t ∈ Icc (-D.τ) D.τ, β t ∈ closedBall x₀ D.R) :
    ∀ t ∈ Icc (-D.τ) D.τ, β t = D.α x t := by
  intro t ht
  have := lb_gronwall_symm (fun s => β s - D.α x s) (fun s => f (β s) - f (D.α x s)) D.τ 0 D.M 0
    (fun s hs => (hβ s hs).sub (D.deriv x hx s hs)) (by simp [hβ0, D.init x hx])
    (fun s hs => by rw [add_zero]; exact D.lb_field_lip hf (hmem s hs) (D.mem x hx s hs)) t ht
  rw [gronwallBound_ε0_δ0] at this
  exact sub_eq_zero.1 (norm_le_zero_iff.1 this)

theorem lb_zero_mem : (0 : ℝ) ∈ Icc (-D.τ) D.τ := ⟨by linarith [D.τ_pos], D.τ_pos.le⟩

/-- A zero of the field at the centre is a fixed point of the flow. -/
theorem lb_fixed (hf : ContDiff ℝ 1 f) (h0 : f x₀ = 0) :
    ∀ t ∈ Icc (-D.τ) D.τ, D.α x₀ t = x₀ := by
  have hx₀ : x₀ ∈ closedBall x₀ D.r := mem_closedBall_self D.r_pos.le
  have hR : x₀ ∈ closedBall x₀ D.R :=
    mem_closedBall_self (dist_nonneg.trans (D.mem x₀ hx₀ 0 D.lb_zero_mem))
  intro t ht
  refine (D.lb_unique hf hx₀ (β := fun _ => x₀) rfl
    (fun s _ => by rw [h0]; exact hasDerivWithinAt_const _ _ _) (fun s _ => hR) t ht).symm

/-- Near a fixed centre the flow moves points by at most `L ‖y − x₀‖`. -/
theorem lb_lip_center (hf : ContDiff ℝ 1 f) (h0 : f x₀ = 0) {y : E}
    (hy : y ∈ closedBall x₀ D.r) {t : ℝ} (ht : t ∈ Icc (-D.τ) D.τ) :
    ‖D.α y t - x₀‖ ≤ D.L * ‖y - x₀‖ := by
  have := (D.lip t ht).norm_sub_le hy (mem_closedBall_self D.r_pos.le)
  rwa [D.lb_fixed hf h0 t ht] at this

/-- A function with constant derivative `a` on `[-τ, τ]` is affine there (Grönwall, `K = 0`). -/
theorem lb_affine_of_deriv {φ : ℝ → ℝ} {a : ℝ}
    (hd : ∀ s ∈ Icc (-D.τ) D.τ, HasDerivWithinAt φ a (Icc (-D.τ) D.τ) s) :
    ∀ s ∈ Icc (-D.τ) D.τ, φ s = φ 0 + s * a := by
  intro s hs
  have := lb_gronwall_symm (fun s => φ s - φ 0 - s * a) (fun _ => (0 : ℝ)) D.τ 0 0 0
    (fun s hs => by
      have h := ((hd s hs).sub_const (φ 0)).sub
        (((hasDerivAt_id s).mul_const a).hasDerivWithinAt (s := Icc (-D.τ) D.τ))
      convert h using 1
      · funext x; simp
      · ring)
    (by simp) (fun s _ => by simp) s hs
  rw [gronwallBound_ε0_δ0] at this
  have := norm_le_zero_iff.1 this
  linarith

end FlowData

end FlowExtra

/-! ## The metric, Christoffel symbols via `(g_x)⁻¹`, the geodesic spray -/

variable {V : Type*} [NormedAddCommGroup V] [NormedSpace ℝ V] [FiniteDimensional ℝ V]

/-- A time-oriented Lorentzian chart (copied from campaign 70 / campaign 60). -/
structure Spacetime (V : Type*) [NormedAddCommGroup V] [NormedSpace ℝ V] where
  M : Set V
  isOpen_M : IsOpen M
  g : V → V →L[ℝ] V →L[ℝ] ℝ
  cont_g : Continuous g
  symm : ∀ x v w, g x v w = g x w v
  T : V → V
  cont_T : Continuous T
  T_timelike : ∀ x ∈ M, g x (T x) (T x) < 0
  pos_on_perp : ∀ x ∈ M, ∀ v, g x v (T x) = 0 → v ≠ 0 → 0 < g x v v

namespace Spacetime
variable (S : Spacetime V)

/-- Future-directed timelike vector at `x`. -/
def FutTimelike (x v : V) : Prop := S.g x v v < 0 ∧ S.g x v (S.T x) < 0
/-- Future-directed causal vector at `x`. -/
def FutCausal (x v : V) : Prop := S.g x v v ≤ 0 ∧ S.g x v (S.T x) < 0

/-- `g_x` is nondegenerate on `M` (copied from campaign 70). -/
theorem lb_nondegenerate {x : V} (hx : x ∈ S.M) {z : V} (hz : ∀ w, S.g x z w = 0) : z = 0 := by
  by_contra hne
  have h := S.pos_on_perp x hx z (hz _) hne
  rw [hz z] at h
  exact lt_irrefl _ h

/-- `Dg x w u v = (Dg_x · w)(u, v)`. -/
noncomputable def Dg (x w u v : V) : ℝ := fderiv ℝ S.g x w u v

/-- The derivative of a symmetric metric is symmetric in its last two slots (copied). -/
theorem lb_Dg_symm (x w u v : V) : S.Dg x w u v = S.Dg x w v u := by
  by_cases hd : DifferentiableAt ℝ S.g x
  · have h1 := (hd.hasFDerivAt.clm_apply (hasFDerivAt_const u x)).clm_apply
      (hasFDerivAt_const v x)
    have h2 := (hd.hasFDerivAt.clm_apply (hasFDerivAt_const v x)).clm_apply
      (hasFDerivAt_const u x)
    have hfun : (fun y => S.g y u v) = fun y => S.g y v u := funext fun y => S.symm y u v
    rw [hfun] at h1
    have := congrArg (fun L => L w) (h1.unique h2)
    simpa [Dg] using this
  · simp [Dg, fderiv_zero_of_not_differentiableAt hd]

theorem lb_Dg_zero (x u v : V) : S.Dg x 0 u v = 0 := by simp [Dg]

/-- The Koszul covector `w ↦ ½(Dg(u)(v,w) + Dg(v)(u,w) − Dg(w)(u,v))`, as a continuous form. -/
noncomputable def kos (x u v : V) : V →L[ℝ] ℝ :=
  (1 / 2 : ℝ) • (fderiv ℝ S.g x u v + fderiv ℝ S.g x v u - ((fderiv ℝ S.g x).flip u).flip v)

theorem lb_kos_apply (x u v w : V) :
    S.kos x u v w = (S.Dg x u v w + S.Dg x v u w - S.Dg x w u v) / 2 := by
  simp [kos, Dg]; ring

/-- **Christoffel symbols** `Γ_x(u,v) = (g_x)⁻¹ (Koszul covector)`, through Mathlib's
`ContinuousLinearMap.inverse` (so that `C¹` dependence on `x` is available). -/
noncomputable def Γ (x u v : V) : V := ContinuousLinearMap.inverse (S.g x) (S.kos x u v)

/-- On `M`, `g_x : V → V*` is a continuous linear isomorphism. -/
theorem lb_g_equiv {x : V} (hx : x ∈ S.M) :
    ∃ e : V ≃L[ℝ] (V →L[ℝ] ℝ), (e : V →L[ℝ] V →L[ℝ] ℝ) = S.g x := by
  have hinj : Function.Injective ((S.g x : V →L[ℝ] V →L[ℝ] ℝ) : V →ₗ[ℝ] (V →L[ℝ] ℝ)) := by
    rw [← LinearMap.ker_eq_bot, LinearMap.ker_eq_bot']
    intro z hz
    exact S.lb_nondegenerate hx fun w => by
      have := congrArg (fun φ : V →L[ℝ] ℝ => φ w) hz; simpa using this
  have hdim : Module.finrank ℝ V = Module.finrank ℝ (V →L[ℝ] ℝ) := by
    rw [← (LinearMap.toContinuousLinearMap (𝕜 := ℝ) (E := V) (F' := ℝ)).finrank_eq]
    exact Subspace.dual_finrank_eq.symm
  refine ⟨(LinearMap.linearEquivOfInjective _ hinj hdim).toContinuousLinearEquiv, ?_⟩
  ext z w; rfl

theorem lb_g_Γ {x : V} (hx : x ∈ S.M) (u v : V) : S.g x (S.Γ x u v) = S.kos x u v := by
  obtain ⟨e, he⟩ := S.lb_g_equiv hx
  rw [Γ, ← he, ContinuousLinearMap.inverse_equiv]
  simp

/-- **Defining identity** `g(Γ(u,v), w) = ½(Dg(u)(v,w) + Dg(v)(u,w) − Dg(w)(u,v))`. -/
theorem lb_christoffel_koszul {x : V} (hx : x ∈ S.M) (u v w : V) :
    S.g x (S.Γ x u v) w = (S.Dg x u v w + S.Dg x v u w - S.Dg x w u v) / 2 := by
  rw [S.lb_g_Γ hx, lb_kos_apply]

theorem lb_christoffel_symm (x u v : V) : S.Γ x u v = S.Γ x v u := by
  have : S.kos x u v = S.kos x v u := by
    ext w; rw [lb_kos_apply, lb_kos_apply, S.lb_Dg_symm x w u v]; ring
  rw [Γ, Γ, this]

theorem lb_christoffel_quad (x u : V) (c : ℝ) : S.Γ x (c • u) (c • u) = (c ^ 2) • S.Γ x u u := by
  have : S.kos x (c • u) (c • u) = (c ^ 2) • S.kos x u u := by
    ext w
    rw [lb_kos_apply, smul_apply, lb_kos_apply]
    simp only [Dg, map_smul, smul_apply, smul_eq_mul]; ring
  rw [Γ, Γ, this, map_smul]

theorem lb_christoffel_zero (x : V) : S.Γ x 0 0 = 0 := by
  have : S.kos x 0 0 = 0 := by ext w; simp [lb_kos_apply, Dg]
  rw [Γ, this, map_zero]

/-- Product rule for `g` along curves (copied from campaign 70). -/
lemma lb_hasDerivAt_g {p u w : ℝ → V} {p' u' w' : V} {r : ℝ}
    (hg : DifferentiableAt ℝ S.g (p r)) (hp : HasDerivAt p p' r)
    (hu : HasDerivAt u u' r) (hw : HasDerivAt w w' r) :
    HasDerivAt (fun r => S.g (p r) (u r) (w r))
      (S.Dg (p r) p' (u r) (w r) + S.g (p r) u' (w r) + S.g (p r) (u r) w') r := by
  have h1 : HasDerivAt (fun r => S.g (p r)) (fderiv ℝ S.g (p r) p') r :=
    HasFDerivAt.comp_hasDerivAt (l := S.g) r hg.hasFDerivAt hp
  have := (h1.clm_apply hu).clm_apply hw
  simpa [Dg, add_assoc] using this

/-- Product rule for `g` along curves, within a set. -/
lemma lb_hasDerivWithinAt_g {s : Set ℝ} {p u w : ℝ → V} {p' u' w' : V} {r : ℝ}
    (hg : DifferentiableAt ℝ S.g (p r)) (hp : HasDerivWithinAt p p' s r)
    (hu : HasDerivWithinAt u u' s r) (hw : HasDerivWithinAt w w' s r) :
    HasDerivWithinAt (fun r => S.g (p r) (u r) (w r))
      (S.Dg (p r) p' (u r) (w r) + S.g (p r) u' (w r) + S.g (p r) (u r) w') s r := by
  have h1 : HasDerivWithinAt (fun r => S.g (p r)) (fderiv ℝ S.g (p r) p') s r :=
    HasFDerivAt.comp_hasDerivWithinAt (l := S.g) r hg.hasFDerivAt hp
  have := (h1.clm_apply hu).clm_apply hw
  simpa [Dg, add_assoc] using this

theorem lb_energy_contDiff (hg : ContDiff ℝ 2 S.g) :
    ContDiff ℝ 2 (fun y : V × V => S.g y.1 y.2 y.2) :=
  ((hg.comp contDiff_fst).clm_apply contDiff_snd).clm_apply contDiff_snd

/-- The energy `E(x, u) = g_x(u, u)` has derivative `(X, U) ↦ Dg_x(X)(u,u) + 2 g_x(u, U)`. -/
theorem lb_energy_hasFDerivAt (hg : ContDiff ℝ 2 S.g) (z : V × V) :
    ∃ L : V × V →L[ℝ] ℝ, HasFDerivAt (fun y : V × V => S.g y.1 y.2 y.2) L z ∧
      ∀ ξ : V × V, L ξ = S.Dg z.1 ξ.1 z.2 z.2 + 2 * S.g z.1 z.2 ξ.2 := by
  have hL := ((S.lb_energy_contDiff hg).differentiable (by norm_num) z).hasFDerivAt
  refine ⟨_, hL, fun ξ => ?_⟩
  have hd : DifferentiableAt ℝ S.g (z.1 + (0:ℝ) • ξ.1) := (hg.differentiable (by norm_num)) _
  have hline : HasDerivAt (fun s : ℝ => z + s • ξ) ξ 0 := by
    simpa using ((hasDerivAt_id (0:ℝ)).smul_const ξ).const_add z
  have h1 := hL.comp_hasDerivAt_of_eq (0:ℝ) hline (by simp)
  have hp : HasDerivAt (fun s : ℝ => z.1 + s • ξ.1) ξ.1 0 := by
    simpa using ((hasDerivAt_id (0:ℝ)).smul_const ξ.1).const_add z.1
  have hu : HasDerivAt (fun s : ℝ => z.2 + s • ξ.2) ξ.2 0 := by
    simpa using ((hasDerivAt_id (0:ℝ)).smul_const ξ.2).const_add z.2
  have h2 := S.lb_hasDerivAt_g hd hp hu hu
  have h3 : HasDerivAt ((fun y : V × V => S.g y.1 y.2 y.2) ∘ fun s : ℝ => z + s • ξ)
      (S.Dg (z.1 + (0:ℝ) • ξ.1) ξ.1 (z.2 + (0:ℝ) • ξ.2) (z.2 + (0:ℝ) • ξ.2) +
        S.g (z.1 + (0:ℝ) • ξ.1) ξ.2 (z.2 + (0:ℝ) • ξ.2) +
        S.g (z.1 + (0:ℝ) • ξ.1) (z.2 + (0:ℝ) • ξ.2) ξ.2) 0 := by
    convert h2 using 1
    funext r; simp [Function.comp]
  have := h1.unique h3
  simp only [zero_smul, add_zero] at this
  rw [this, S.symm z.1 ξ.2 z.2]; ring

/-- For `g ∈ C²`, `(x, u) ↦ Γ_x(u,u)` is `C¹` near every point of `M × V`. -/
theorem lb_christoffel_contDiffAt (hg : ContDiff ℝ 2 S.g) {x : V} (hx : x ∈ S.M) (u : V) :
    ContDiffAt ℝ 1 (fun z : V × V => S.Γ z.1 z.2 z.2) (x, u) := by
  obtain ⟨e, he⟩ := S.lb_g_equiv hx
  have h1 : ContDiffAt ℝ 1 (fun z : V × V => ContinuousLinearMap.inverse (S.g z.1)) (x, u) := by
    have := contDiffAt_map_inverse (𝕜 := ℝ) (n := 1) e
    rw [he] at this
    exact this.comp (x, u) ((hg.of_le (by norm_num)).contDiffAt.comp (x, u) contDiffAt_fst)
  have hE : ContDiff ℝ 2 (fun y : V × V => S.g y.1 y.2 y.2) :=
    ((hg.comp contDiff_fst).clm_apply contDiff_snd).clm_apply contDiff_snd
  have hT1 : ContDiff ℝ 1 (fun z : V × V => fderiv ℝ S.g z.1 z.2) :=
    ContDiff.fderiv_apply (f := fun _ : V × V => S.g) (by exact hg.comp contDiff_snd)
      contDiff_fst contDiff_snd (by norm_num)
  have hT3 : ContDiff ℝ 1 (fun z : V × V =>
      (fderiv ℝ (fun y : V × V => S.g y.1 y.2 y.2) z).comp (ContinuousLinearMap.inl ℝ V V)) :=
    (hE.fderiv_right (m := 1) (by norm_num)).clm_comp contDiff_const
  have hk : (fun z : V × V => S.kos z.1 z.2 z.2) = fun z => (1 / 2 : ℝ) •
      (fderiv ℝ S.g z.1 z.2 z.2 + fderiv ℝ S.g z.1 z.2 z.2 -
        (fderiv ℝ (fun y : V × V => S.g y.1 y.2 y.2) z).comp (ContinuousLinearMap.inl ℝ V V)) := by
    funext z; ext w
    obtain ⟨L, hL, hLv⟩ := S.lb_energy_hasFDerivAt hg z
    rw [lb_kos_apply, hL.fderiv]
    simp [hLv, Dg]; ring
  have h2 : ContDiff ℝ 1 (fun z : V × V => S.kos z.1 z.2 z.2) := by
    rw [hk]
    exact (contDiff_const (c := (1 / 2 : ℝ))).smul (((hT1.clm_apply contDiff_snd).add
      (hT1.clm_apply contDiff_snd)).sub hT3)
  exact h1.clm_apply h2.contDiffAt

/-- The geodesic spray `F(x, v) = (v, −Γ_x(v,v))` on `V × V`. -/
noncomputable def geoField (z : V × V) : V × V := (z.2, -S.Γ z.1 z.2 z.2)

theorem lb_geoField_contDiffAt (hg : ContDiff ℝ 2 S.g) {z : V × V} (hz : z.1 ∈ S.M) :
    ContDiffAt ℝ 1 S.geoField z := by
  obtain ⟨x, u⟩ := z
  exact contDiffAt_snd.prodMk (S.lb_christoffel_contDiffAt hg hz u).neg

/-- The spray cut off in `x` by a bump `χ` around `p`: `C¹` on all of `V × V`. -/
noncomputable def cutField {p : V} (χ : ContDiffBump p) (z : V × V) : V × V := χ z.1 • S.geoField z

theorem lb_cutField_contDiff (hg : ContDiff ℝ 2 S.g) {p : V} (χ : ContDiffBump p)
    (hχ : closedBall p χ.rOut ⊆ S.M) : ContDiff ℝ 1 (S.cutField χ) := by
  rw [contDiff_iff_contDiffAt]; intro z
  by_cases hz : z.1 ∈ closedBall p χ.rOut
  · exact ((χ.contDiff.comp contDiff_fst).contDiffAt).smul (S.lb_geoField_contDiffAt hg (hχ hz))
  · have hO : IsOpen {y : V × V | y.1 ∉ closedBall p χ.rOut} :=
      (isClosed_closedBall.preimage continuous_fst).isOpen_compl
    refine (contDiffAt_const (c := (0 : V × V))).congr_of_eventuallyEq ?_
    filter_upwards [hO.mem_nhds hz] with y hy
    have hy' : χ.rOut ≤ dist y.1 p := by
      simp only [mem_closedBall, not_le] at hy; exact hy.le
    simp [cutField, χ.zero_of_le_dist hy']

theorem lb_cutField_eq {p : V} (χ : ContDiffBump p) {z : V × V} (hz : z.1 ∈ closedBall p χ.rIn) :
    S.cutField χ z = S.geoField z := by
  simp [cutField, χ.one_of_mem_closedBall hz]

theorem lb_cutField_zero {p : V} (χ : ContDiffBump p) : S.cutField χ (p, 0) = 0 := by
  simp [cutField, geoField, lb_christoffel_zero]

/-- Inside `ball p rIn`, the first component of `D(cut spray)` is the projection `(X, U) ↦ U`. -/
theorem lb_fst_fderiv_cutField (hg : ContDiff ℝ 2 S.g) {p : V} (χ : ContDiffBump p)
    (hχ : closedBall p χ.rOut ⊆ S.M) {z : V × V} (hz : z.1 ∈ ball p χ.rIn) (ξ : V × V) :
    (fderiv ℝ (S.cutField χ) z ξ).1 = ξ.2 := by
  have hd := ((S.lb_cutField_contDiff hg χ hχ).differentiable one_ne_zero z).hasFDerivAt
  have h1 := (ContinuousLinearMap.fst ℝ V V).hasFDerivAt.comp z hd
  have hO : IsOpen {y : V × V | y.1 ∈ ball p χ.rIn} := isOpen_ball.preimage continuous_fst
  have heq : (fun y => (S.cutField χ y).1) =ᶠ[𝓝 z] Prod.snd := by
    filter_upwards [hO.mem_nhds hz] with y hy
    rw [S.lb_cutField_eq χ (ball_subset_closedBall hy)]; rfl
  have h2 : HasFDerivAt (fun y => (S.cutField χ y).1) (ContinuousLinearMap.snd ℝ V V) z :=
    (hasFDerivAt_snd).congr_of_eventuallyEq heq
  have := congrArg (fun L => L ξ) (h1.unique h2)
  simpa using this


theorem lb_norm_zero_prod (w : V) : ‖((0 : V), w)‖ = ‖w‖ := by
  rw [Prod.norm_def]; simp

/-- **Lorentzian algebra.** At `x ∈ M`, a causal vector `w` orthogonal to a nonzero null vector `P`
is a multiple of `P`. -/
theorem lb_causal_perp_null {x : V} (hx : x ∈ S.M) {P w : V} (hPP : S.g x P P = 0) (hP : P ≠ 0)
    (hww : S.g x w w ≤ 0) (hPw : S.g x P w = 0) : ∃ k : ℝ, w = k • P := by
  have hPT : S.g x P (S.T x) ≠ 0 := fun h => by
    have := S.pos_on_perp x hx P h hP; linarith
  refine ⟨S.g x w (S.T x) / S.g x P (S.T x), ?_⟩
  set k := S.g x w (S.T x) / S.g x P (S.T x) with hk
  have hzT : S.g x (w - k • P) (S.T x) = 0 := by
    simp only [map_sub, map_smul, sub_apply, FunLike.coe_smul,
      Pi.smul_apply, smul_eq_mul, hk]
    field_simp; ring
  have hzz : S.g x (w - k • P) (w - k • P) = S.g x w w := by
    have hwP : S.g x w P = 0 := by rw [S.symm]; exact hPw
    simp only [map_sub, map_smul, sub_apply, FunLike.coe_smul,
      Pi.smul_apply, smul_eq_mul, hPP, hwP, hPw]
    ring
  by_contra hne
  have := S.pos_on_perp x hx (w - k • P) hzT (sub_ne_zero.2 hne)
  linarith

/-- One `C¹` future-timelike piece from `x` to `y` on `[0,1]` (copied from campaign 70). -/
def TStep (x y : V) : Prop :=
  ∃ γ : ℝ → V, ContDiff ℝ 1 γ ∧ γ 0 = x ∧ γ 1 = y ∧
    ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ S.M ∧ S.FutTimelike (γ t) (deriv γ t)

/-- Chronological relation `x ≪ y` (copied from campaign 70). -/
def Chr (x y : V) : Prop := Relation.TransGen S.TStep x y

/-! ## ① Local geodesics: the flow of the cut-off spray near the zero section -/

/-- Local geodesic-flow data at `p ∈ M`: a bump `χ` around `p` with support in `M`, and campaign
62's flow data for the cut-off spray at `(p, 0)`. -/
structure GeoFlow (p : V) where
  χ : ContDiffBump p
  sub : closedBall p χ.rOut ⊆ S.M
  D : FlowData (S.cutField χ) ((p, 0) : V × V)

/-- Geodesic-flow data exist at every `p ∈ M` (for `g ∈ C²`). -/
theorem lb_geoFlow_exists (hg : ContDiff ℝ 2 S.g) {p : V} (hp : p ∈ S.M) :
    Nonempty (S.GeoFlow p) := by
  obtain ⟨ε, hε, hball⟩ := Metric.isOpen_iff.1 S.isOpen_M p hp
  let χ : ContDiffBump p := ⟨ε / 4, ε / 2, by positivity, by linarith⟩
  have hsub : closedBall p χ.rOut ⊆ S.M :=
    (closedBall_subset_ball (by show ε / 2 < ε; linarith)).trans hball
  exact ⟨⟨χ, hsub, (lb_flowData_exists (S.lb_cutField_contDiff hg χ hsub) (p, 0)).some⟩⟩

namespace GeoFlow

variable {S} {p : V} (G : S.GeoFlow p)

theorem lb_hf (hg : ContDiff ℝ 2 S.g) : ContDiff ℝ 1 (S.cutField G.χ) :=
  S.lb_cutField_contDiff hg G.χ G.sub

/-- The radius of initial data whose trajectories stay where `χ = 1`. -/
noncomputable def r₁ : ℝ := min G.D.r (G.χ.rIn / (2 * ((G.D.L : ℝ) + 1)))

theorem lb_r₁_pos : 0 < G.r₁ := lt_min G.D.r_pos (by have := G.χ.rIn_pos; positivity)

theorem lb_r₁_le : G.r₁ ≤ G.D.r := min_le_left _ _

theorem lb_mem_r {y : V × V} (hy : y ∈ closedBall ((p, 0) : V × V) G.r₁) :
    y ∈ closedBall ((p, 0) : V × V) G.D.r :=
  closedBall_subset_closedBall G.lb_r₁_le hy

theorem lb_ball_sub_M {x : V} (hx : x ∈ ball p G.χ.rIn) : x ∈ S.M :=
  G.sub (closedBall_subset_closedBall G.χ.rIn_lt_rOut.le (ball_subset_closedBall hx))

/-- Trajectories from `closedBall (p,0) r₁` stay over `ball p rIn`, where `χ = 1`. -/
theorem lb_traj_in (hg : ContDiff ℝ 2 S.g) {y : V × V}
    (hy : y ∈ closedBall ((p, 0) : V × V) G.r₁) {t : ℝ} (ht : t ∈ Icc (-G.D.τ) G.D.τ) :
    (G.D.α y t).1 ∈ ball p G.χ.rIn := by
  have h1 := G.D.lb_lip_center (G.lb_hf hg) (S.lb_cutField_zero G.χ) (G.lb_mem_r hy) ht
  have hy' : ‖y - (p, 0)‖ ≤ G.r₁ := by rwa [mem_closedBall, dist_eq_norm] at hy
  have hL : (0 : ℝ) ≤ G.D.L := G.D.L.2
  have hrin := G.χ.rIn_pos
  have hq : (G.D.L : ℝ) * G.r₁ < G.χ.rIn := by
    have h2 : G.r₁ ≤ G.χ.rIn / (2 * ((G.D.L : ℝ) + 1)) := min_le_right _ _
    have h3 : (G.D.L : ℝ) * (G.χ.rIn / (2 * ((G.D.L : ℝ) + 1))) < G.χ.rIn := by
      rw [mul_div_assoc', div_lt_iff₀ (by positivity)]; nlinarith
    calc _ ≤ (G.D.L : ℝ) * (G.χ.rIn / (2 * ((G.D.L : ℝ) + 1))) :=
          mul_le_mul_of_nonneg_left h2 hL
      _ < _ := h3
  rw [mem_ball, dist_eq_norm]
  calc ‖(G.D.α y t).1 - p‖ = ‖(G.D.α y t - (p, 0)).1‖ := rfl
    _ ≤ ‖G.D.α y t - (p, 0)‖ := norm_fst_le _
    _ ≤ G.D.L * ‖y - (p, 0)‖ := h1
    _ ≤ G.D.L * G.r₁ := mul_le_mul_of_nonneg_left hy' hL
    _ < _ := hq

/-- **Local geodesics.** For initial data in `closedBall (p,0) r₁` the flow solves the geodesic
spray `(x, u)′ = (u, −Γ_x(u,u))` on `[-τ, τ]`. -/
theorem lb_geodesic (hg : ContDiff ℝ 2 S.g) {y : V × V}
    (hy : y ∈ closedBall ((p, 0) : V × V) G.r₁) {t : ℝ} (ht : t ∈ Icc (-G.D.τ) G.D.τ) :
    HasDerivWithinAt (G.D.α y) (S.geoField (G.D.α y t)) (Icc (-G.D.τ) G.D.τ) t := by
  rw [← S.lb_cutField_eq G.χ (ball_subset_closedBall (G.lb_traj_in hg hy ht))]
  exact G.D.deriv y (G.lb_mem_r hy) t ht

theorem lb_geodesic_fst (hg : ContDiff ℝ 2 S.g) {y : V × V}
    (hy : y ∈ closedBall ((p, 0) : V × V) G.r₁) {t : ℝ} (ht : t ∈ Icc (-G.D.τ) G.D.τ) :
    HasDerivWithinAt (fun s => (G.D.α y s).1) (G.D.α y t).2 (Icc (-G.D.τ) G.D.τ) t := by
  have := (ContinuousLinearMap.fst ℝ V V).hasFDerivAt.comp_hasDerivWithinAt t
    (G.lb_geodesic hg hy ht)
  exact this.congr_deriv (by simp [geoField])

theorem lb_geodesic_snd (hg : ContDiff ℝ 2 S.g) {y : V × V}
    (hy : y ∈ closedBall ((p, 0) : V × V) G.r₁) {t : ℝ} (ht : t ∈ Icc (-G.D.τ) G.D.τ) :
    HasDerivWithinAt (fun s => (G.D.α y s).2)
      (-S.Γ (G.D.α y t).1 (G.D.α y t).2 (G.D.α y t).2) (Icc (-G.D.τ) G.D.τ) t := by
  have := (ContinuousLinearMap.snd ℝ V V).hasFDerivAt.comp_hasDerivWithinAt t
    (G.lb_geodesic hg hy ht)
  exact this.congr_deriv (by simp [geoField])

/-- **Scaling of geodesics.** `φ_t(p, λa) = (π₁ φ_{λt}(p, a), λ π₂ φ_{λt}(p, a))` for
`λ ∈ [0, 1]`: the geodesic with initial velocity `λa` is the one with velocity `a`, run at speed
`λ`. Proved by uniqueness (`lb_unique`). -/
theorem lb_scaling (hg : ContDiff ℝ 2 S.g) {a : V}
    (ha : ((p, a) : V × V) ∈ closedBall ((p, 0) : V × V) G.r₁) {l : ℝ} (hl : l ∈ Icc (0 : ℝ) 1)
    {t : ℝ} (ht : t ∈ Icc (-G.D.τ) G.D.τ) :
    G.D.α (p, l • a) t = ((G.D.α (p, a) (l * t)).1, l • (G.D.α (p, a) (l * t)).2) := by
  have hlt : ∀ s ∈ Icc (-G.D.τ) G.D.τ, l * s ∈ Icc (-G.D.τ) G.D.τ := fun s hs => by
    constructor <;> nlinarith [hs.1, hs.2, hl.1, hl.2, G.D.τ_pos]
  have hx : ((p, l • a) : V × V) ∈ closedBall ((p, 0) : V × V) G.D.r := by
    have ha' := G.lb_mem_r ha
    rw [mem_closedBall, dist_eq_norm] at ha' ⊢
    have e1 : ((p, l • a) : V × V) - (p, 0) = ((0 : V), l • a) := by simp
    have e2 : ((p, a) : V × V) - (p, 0) = ((0 : V), a) := by simp
    rw [e1, lb_norm_zero_prod, norm_smul, Real.norm_eq_abs, abs_of_nonneg hl.1]
    rw [e2, lb_norm_zero_prod] at ha'
    nlinarith [norm_nonneg a, hl.2]
  let Ll : V × V →L[ℝ] V × V :=
    (ContinuousLinearMap.fst ℝ V V).prod (l • ContinuousLinearMap.snd ℝ V V)
  have hβL : (fun s => ((G.D.α (p, a) (l * s)).1, l • (G.D.α (p, a) (l * s)).2)) =
      Ll ∘ G.D.α (p, a) ∘ fun s => l * s := by
    funext s; simp [Ll]
  refine (G.D.lb_unique (G.lb_hf hg) hx
    (β := fun s => ((G.D.α (p, a) (l * s)).1, l • (G.D.α (p, a) (l * s)).2)) ?_ ?_ ?_ t ht).symm
  · simp [G.D.init _ (G.lb_mem_r ha)]
  · intro s hs
    have h1 : HasDerivWithinAt (fun s => l * s) l (Icc (-G.D.τ) G.D.τ) s := by
      simpa using ((hasDerivAt_id s).const_mul l).hasDerivWithinAt
    have h2 := (G.lb_geodesic hg ha (hlt s hs)).scomp s h1 (fun s hs => hlt s hs)
    have h3 := Ll.hasFDerivAt.comp_hasDerivWithinAt s h2
    rw [← hβL] at h3
    convert h3 using 1
    have hin := G.lb_traj_in hg ha (hlt s hs)
    rw [S.lb_cutField_eq G.χ
      (z := ((G.D.α (p, a) (l * s)).1, l • (G.D.α (p, a) (l * s)).2)) (ball_subset_closedBall hin)]
    simp only [geoField, Ll, S.lb_christoffel_quad, ContinuousLinearMap.prod_apply,
      ContinuousLinearMap.coe_fst', ContinuousLinearMap.coe_snd', Prod.smul_mk,
      FunLike.coe_smul, Pi.smul_apply, smul_neg, smul_smul, pow_two]
  · intro s hs
    have := G.D.mem (p, a) (G.lb_mem_r ha) (l * s) (hlt s hs)
    rw [mem_closedBall, dist_eq_norm] at this ⊢
    refine le_trans ?_ this
    rw [Prod.norm_def, Prod.norm_def]
    refine max_le_max le_rfl ?_
    simp only [Prod.snd_sub, sub_zero, norm_smul, Real.norm_eq_abs, abs_of_nonneg hl.1]
    nlinarith [norm_nonneg (G.D.α (p, a) (l * s)).2, hl.2]

/-! ### The exponential map -/

/-- The time at which `exp` is read off. -/
noncomputable def s₀ : ℝ := G.D.τ / 2
/-- The velocity rescaling, `c s₀ = 1`. -/
noncomputable def c : ℝ := 2 / G.D.τ

theorem lb_c_s₀ : G.c * G.s₀ = 1 := by
  unfold c s₀; field_simp [G.D.τ_pos.ne']

theorem lb_s₀_pos : 0 < G.s₀ := by unfold s₀; linarith [G.D.τ_pos]
theorem lb_c_pos : 0 < G.c := by unfold c; have := G.D.τ_pos; positivity

theorem lb_s₀_mem : G.s₀ ∈ Icc (-G.D.τ) G.D.τ := by
  unfold s₀; constructor <;> linarith [G.D.τ_pos]

/-- `exp_p(v) = π₁ φ_{s₀}(p, c v)`; by `lb_expp_smul` this is `π₁ φ₁(p, v)` of the geodesic
spray, with the time rescaled to stay inside `[-τ, τ]`. -/
noncomputable def expp (v : V) : V := (G.D.α (p, G.c • v) G.s₀).1

/-- The velocity at `t = 1` of the radial geodesic `t ↦ exp_p(t v)`. -/
noncomputable def rad (v : V) : V := G.s₀ • (G.D.α (p, G.c • v) G.s₀).2

/-- The radius of the normal-coordinate domain `ball 0 ρ`. -/
noncomputable def ρ : ℝ := G.r₁ * G.s₀

theorem lb_ρ_pos : 0 < G.ρ := mul_pos G.lb_r₁_pos G.lb_s₀_pos

theorem lb_dom {v : V} (hv : v ∈ ball (0 : V) G.ρ) :
    ((p, G.c • v) : V × V) ∈ ball ((p, 0) : V × V) G.r₁ := by
  rw [mem_ball, dist_eq_norm]
  have e1 : ((p, G.c • v) : V × V) - (p, 0) = ((0 : V), G.c • v) := by simp
  rw [e1, lb_norm_zero_prod, norm_smul, Real.norm_eq_abs, abs_of_pos G.lb_c_pos]
  have h := mem_ball_zero_iff.1 hv
  have hcs := G.lb_c_s₀
  unfold ρ at h
  calc G.c * ‖v‖ < G.c * (G.r₁ * G.s₀) := mul_lt_mul_of_pos_left h G.lb_c_pos
    _ = G.r₁ * (G.c * G.s₀) := by ring
    _ = G.r₁ := by rw [hcs, mul_one]

theorem lb_dom_closed {v : V} (hv : v ∈ ball (0 : V) G.ρ) :
    ((p, G.c • v) : V × V) ∈ closedBall ((p, 0) : V × V) G.r₁ :=
  ball_subset_closedBall (G.lb_dom hv)

/-- The derivative `D exp_p(v) w = π₁ J_{s₀}(p, c v) (0, c w)` (variational equation). -/
noncomputable def Dexp (v : V) : V →L[ℝ] V :=
  (ContinuousLinearMap.fst ℝ V V).comp ((G.D.J (p, G.c • v) G.s₀).comp
    ((0 : V →L[ℝ] V).prod (G.c • ContinuousLinearMap.id ℝ V)))

theorem lb_Dexp_apply (v w : V) : G.Dexp v w = (G.D.J (p, G.c • v) G.s₀ (0, G.c • w)).1 := by
  simp [Dexp]

theorem lb_expp_hasFDerivAt (hg : ContDiff ℝ 2 S.g) {v : V} (hv : v ∈ ball (0 : V) G.ρ) :
    HasFDerivAt G.expp (G.Dexp v) v := by
  have h1 : HasFDerivAt (fun w : V => ((p, G.c • w) : V × V))
      ((0 : V →L[ℝ] V).prod (G.c • ContinuousLinearMap.id ℝ V)) v :=
    (hasFDerivAt_const p v).prodMk ((ContinuousLinearMap.id ℝ V).hasFDerivAt.const_smul G.c)
  have h2 := G.D.lb_flow_hasFDerivAt (G.lb_hf hg) (p, G.c • v)
    (ball_subset_ball G.lb_r₁_le (G.lb_dom hv)) G.s₀ G.lb_s₀_mem
  have h3 := h2.comp v h1
  have h4 := (ContinuousLinearMap.fst ℝ V V).hasFDerivAt.comp v h3
  exact h4

theorem lb_expp_contDiffAt (hg : ContDiff ℝ 2 S.g) {v : V} (hv : v ∈ ball (0 : V) G.ρ) :
    ContDiffAt ℝ 1 G.expp v := by
  have h1 : ContDiffAt ℝ 1 (fun y : V × V => G.D.α y G.s₀) (p, G.c • v) :=
    (G.D.lb_flow_contDiffOn (G.lb_hf hg) G.s₀ G.lb_s₀_mem).contDiffAt
      (isOpen_ball.mem_nhds (ball_subset_ball G.lb_r₁_le (G.lb_dom hv)))
  have h2 : ContDiffAt ℝ 1 (fun w : V => ((p, G.c • w) : V × V)) v :=
    contDiffAt_const.prodMk (contDiffAt_id.const_smul G.c)
  have h3 := h1.comp v h2
  have h4 := contDiffAt_fst.comp v h3
  exact h4

theorem lb_expp_zero (hg : ContDiff ℝ 2 S.g) : G.expp 0 = p := by
  simp [expp, G.D.lb_fixed (G.lb_hf hg) (S.lb_cutField_zero G.χ) G.s₀ G.lb_s₀_mem]

/-- **Radial geodesics.** `exp_p(λ v) = π₁ φ_{λ s₀}(p, c v)` for `λ ∈ [0, 1]`. -/
theorem lb_expp_smul (hg : ContDiff ℝ 2 S.g) {v : V} (hv : v ∈ ball (0 : V) G.ρ) {l : ℝ}
    (hl : l ∈ Icc (0 : ℝ) 1) : G.expp (l • v) = (G.D.α (p, G.c • v) (l * G.s₀)).1 := by
  rw [expp, smul_comm G.c l v, G.lb_scaling hg (G.lb_dom_closed hv) hl G.lb_s₀_mem]

theorem lb_mul_s₀_mem {l : ℝ} (hl : l ∈ Icc (0 : ℝ) 1) : l * G.s₀ ∈ Icc (-G.D.τ) G.D.τ := by
  have := G.lb_s₀_pos
  unfold s₀ at *
  constructor <;> nlinarith [hl.1, hl.2, G.D.τ_pos]

theorem lb_expp_radial_deriv (hg : ContDiff ℝ 2 S.g) {v : V} (hv : v ∈ ball (0 : V) G.ρ)
    {l : ℝ} (hl : l ∈ Icc (0 : ℝ) 1) :
    HasDerivWithinAt (fun m : ℝ => G.expp (m • v))
      (G.s₀ • (G.D.α (p, G.c • v) (l * G.s₀)).2) (Icc 0 1) l := by
  have hmaps : MapsTo (fun m : ℝ => m * G.s₀) (Icc (0 : ℝ) 1) (Icc (-G.D.τ) G.D.τ) :=
    fun m hm => G.lb_mul_s₀_mem hm
  have h1 : HasDerivWithinAt (fun m : ℝ => m * G.s₀) G.s₀ (Icc 0 1) l := by
    simpa using ((hasDerivAt_id l).mul_const G.s₀).hasDerivWithinAt
  have h2 := (G.lb_geodesic hg (G.lb_dom_closed hv) (hmaps hl)).scomp l h1 hmaps
  have h3 := (ContinuousLinearMap.fst ℝ V V).hasFDerivAt.comp_hasDerivWithinAt l h2
  refine (h3.congr (fun m hm => G.lb_expp_smul hg hv hm) (G.lb_expp_smul hg hv hl)).congr_deriv ?_
  simp [geoField]

/-- `D exp_p(λ v) v` is the velocity of the radial geodesic at `λ`. -/
theorem lb_Dexp_radial_at (hg : ContDiff ℝ 2 S.g) {v : V} (hv : v ∈ ball (0 : V) G.ρ) {l : ℝ}
    (hl : l ∈ Icc (0 : ℝ) 1) :
    G.Dexp (l • v) v = G.s₀ • (G.D.α (p, G.c • v) (l * G.s₀)).2 := by
  have hlv : l • v ∈ ball (0 : V) G.ρ := by
    rw [mem_ball_zero_iff, norm_smul, Real.norm_eq_abs, abs_of_nonneg hl.1]
    have := mem_ball_zero_iff.1 hv
    nlinarith [norm_nonneg v, hl.2]
  have h1 : HasDerivAt (fun m : ℝ => G.expp (m • v)) (G.Dexp (l • v) v) l := by
    have hline : HasDerivAt (fun m : ℝ => m • v) v l := by
      simpa using (hasDerivAt_id l).smul_const v
    exact (G.lb_expp_hasFDerivAt hg hlv).comp_hasDerivAt l hline
  exact (uniqueDiffOn_Icc_zero_one l hl).eq_deriv _ h1.hasDerivWithinAt
    (G.lb_expp_radial_deriv hg hv hl)

/-- `D exp_p(v) v = rad v`: the radial derivative is the geodesic velocity. -/
theorem lb_Dexp_radial (hg : ContDiff ℝ 2 S.g) {v : V} (hv : v ∈ ball (0 : V) G.ρ) :
    G.Dexp v v = G.rad v := by
  have := G.lb_Dexp_radial_at hg hv (l := 1) ⟨zero_le_one, le_rfl⟩
  rwa [one_smul, one_mul] at this

theorem lb_Dexp_zero_apply (hg : ContDiff ℝ 2 S.g) {v : V} (hv : v ∈ ball (0 : V) G.ρ) :
    G.Dexp 0 v = v := by
  have := G.lb_Dexp_radial_at hg hv (l := 0) ⟨le_rfl, zero_le_one⟩
  rw [zero_smul, zero_mul, G.D.init _ (G.lb_mem_r (G.lb_dom_closed hv)), smul_smul,
    mul_comm, G.lb_c_s₀, one_smul] at this
  exact this

/-- **`D exp_p(0) = id`.** -/
theorem lb_Dexp_zero (hg : ContDiff ℝ 2 S.g) : G.Dexp 0 = ContinuousLinearMap.id ℝ V := by
  ext v
  set ε : ℝ := G.ρ / (2 * (‖v‖ + 1)) with hε
  have hε0 : 0 < ε := by have := G.lb_ρ_pos; positivity
  have hεv : ε • v ∈ ball (0 : V) G.ρ := by
    rw [mem_ball_zero_iff, norm_smul, Real.norm_eq_abs, abs_of_pos hε0, hε]
    have := G.lb_ρ_pos
    rw [div_mul_eq_mul_div, div_lt_iff₀ (by positivity)]
    nlinarith [norm_nonneg v]
  have := G.lb_Dexp_zero_apply hg hεv
  rw [map_smul] at this
  simpa using smul_right_injective V hε0.ne' this

theorem lb_expp_fderiv_zero (hg : ContDiff ℝ 2 S.g) :
    HasFDerivAt G.expp (ContinuousLinearMap.id ℝ V) 0 := by
  rw [← G.lb_Dexp_zero hg]
  exact G.lb_expp_hasFDerivAt hg (mem_ball_self G.lb_ρ_pos)

/-- **`exp_p` is a local diffeomorphism at `0`** (inverse function theorem, as in campaign 62's flow
box): a `C¹` open partial homeomorphism `Φ` with `Φ = exp_p` on its source `∋ 0`, `Φ 0 = p`, and
a `C¹` inverse near `p`. -/
theorem lb_expp_localDiffeo (hg : ContDiff ℝ 2 S.g) :
    ∃ Φ : OpenPartialHomeomorph V V, (0 : V) ∈ Φ.source ∧ Φ.source ⊆ ball (0 : V) G.ρ ∧
      (∀ v ∈ Φ.source, Φ v = G.expp v) ∧ Φ 0 = p ∧ ContDiffOn ℝ 1 Φ Φ.source ∧
      ∀ᶠ x in 𝓝 p, ContDiffAt ℝ 1 Φ.symm x := by
  have hn : (1 : WithTop ℕ∞) ≠ 0 := by norm_num
  have h0 : (0 : V) ∈ ball (0 : V) G.ρ := mem_ball_self G.lb_ρ_pos
  have hd : HasFDerivAt G.expp ((ContinuousLinearEquiv.refl ℝ V : V ≃L[ℝ] V) : V →L[ℝ] V) 0 := by
    rw [ContinuousLinearEquiv.coe_refl]; exact G.lb_expp_fderiv_zero hg
  have hc := G.lb_expp_contDiffAt hg h0
  refine ⟨(hc.toOpenPartialHomeomorph G.expp hd hn).restrOpen (ball 0 G.ρ) isOpen_ball,
    ⟨hc.mem_toOpenPartialHomeomorph_source hd hn, h0⟩, inter_subset_right, fun v _ => rfl,
    G.lb_expp_zero hg, fun v hv => (G.lb_expp_contDiffAt hg hv.2).contDiffWithinAt, ?_⟩
  have := (hc.to_localInverse hd hn).eventually (by simp)
  rw [G.lb_expp_zero hg] at this
  exact this

/-! ## ② The Gauss lemma, through the variational (Jacobi) equation -/

/-- **Energy conservation** along local geodesics: `g_x(u, u)` is constant. -/
theorem lb_energy_cons (hg : ContDiff ℝ 2 S.g) {y : V × V}
    (hy : y ∈ closedBall ((p, 0) : V × V) G.r₁) {t : ℝ} (ht : t ∈ Icc (-G.D.τ) G.D.τ) :
    S.g (G.D.α y t).1 (G.D.α y t).2 (G.D.α y t).2 = S.g y.1 y.2 y.2 := by
  have hd : ∀ s ∈ Icc (-G.D.τ) G.D.τ, HasDerivWithinAt
      (fun s => S.g (G.D.α y s).1 (G.D.α y s).2 (G.D.α y s).2) 0 (Icc (-G.D.τ) G.D.τ) s := by
    intro s hs
    have h := S.lb_hasDerivWithinAt_g ((hg.differentiable (by norm_num)) _)
      (G.lb_geodesic_fst hg hy hs) (G.lb_geodesic_snd hg hy hs) (G.lb_geodesic_snd hg hy hs)
    convert h using 1
    have hx := G.lb_ball_sub_M (G.lb_traj_in hg hy hs)
    set x := (G.D.α y s).1
    set u := (G.D.α y s).2
    rw [map_neg, map_neg, neg_apply, S.symm x u (S.Γ x u u),
      S.lb_christoffel_koszul hx]
    ring
  have := G.D.lb_affine_of_deriv hd t ht
  rw [this, G.D.init y (G.lb_mem_r hy)]; ring

/-- The energy identity differentiated in the initial data:
`Dg_x(X)(u,u) + 2 g_x(u, U) = Dg_y(ξ₁)(y₂,y₂) + 2 g_y(y₂, ξ₂)` for `(X, U) = J ξ`. -/
theorem lb_energy_variation (hg : ContDiff ℝ 2 S.g) {y : V × V}
    (hy : y ∈ ball ((p, 0) : V × V) G.r₁) {t : ℝ} (ht : t ∈ Icc (-G.D.τ) G.D.τ) (ξ : V × V) :
    S.Dg (G.D.α y t).1 (G.D.J y t ξ).1 (G.D.α y t).2 (G.D.α y t).2 +
        2 * S.g (G.D.α y t).1 (G.D.α y t).2 (G.D.J y t ξ).2 =
      S.Dg y.1 ξ.1 y.2 y.2 + 2 * S.g y.1 y.2 ξ.2 := by
  obtain ⟨L₁, hL₁, hv₁⟩ := S.lb_energy_hasFDerivAt hg (G.D.α y t)
  obtain ⟨L₂, hL₂, hv₂⟩ := S.lb_energy_hasFDerivAt hg y
  have hJ := G.D.lb_flow_hasFDerivAt (G.lb_hf hg) y (ball_subset_ball G.lb_r₁_le hy) t ht
  have h1 := hL₁.comp y hJ
  have heq : ((fun z : V × V => S.g z.1 z.2 z.2) ∘ fun y' => G.D.α y' t) =ᶠ[𝓝 y]
      (fun y' : V × V => S.g y'.1 y'.2 y'.2) := by
    filter_upwards [isOpen_ball.mem_nhds hy] with y' hy'
    exact G.lb_energy_cons hg (ball_subset_closedBall hy') ht
  have h2 := hL₂.congr_of_eventuallyEq heq
  have := congrArg (fun L => L ξ) (h1.unique h2)
  simp only [ContinuousLinearMap.comp_apply, hv₁, hv₂] at this
  exact this

/-- **The Gauss lemma, flow form.** Along the geodesic `(x, u)(t) = φ_t(p, a)` and the Jacobi
field `(X, U)(t) = J_t(p, a)(0, b)`: `g_{x(t)}(u(t), X(t)) = t · g_p(a, b)`. -/
theorem lb_gauss_flow (hg : ContDiff ℝ 2 S.g) {a : V}
    (ha : ((p, a) : V × V) ∈ ball ((p, 0) : V × V) G.r₁) (b : V) {t : ℝ}
    (ht : t ∈ Icc (-G.D.τ) G.D.τ) :
    S.g (G.D.α (p, a) t).1 (G.D.α (p, a) t).2 (G.D.J (p, a) t (0, b)).1 = t * S.g p a b := by
  have hyc := ball_subset_closedBall ha
  have hJ := G.D.lb_J_spec (G.lb_hf hg) (p, a) (G.lb_mem_r hyc)
  have hd : ∀ s ∈ Icc (-G.D.τ) G.D.τ, HasDerivWithinAt (fun s =>
      S.g (G.D.α (p, a) s).1 (G.D.α (p, a) s).2 (G.D.J (p, a) s (0, b)).1) (S.g p a b)
      (Icc (-G.D.τ) G.D.τ) s := by
    intro s hs
    have hJs : HasDerivWithinAt (fun s => G.D.J (p, a) s (0, b))
        (fderiv ℝ (S.cutField G.χ) (G.D.α (p, a) s) (G.D.J (p, a) s (0, b)))
        (Icc (-G.D.τ) G.D.τ) s := by
      have := (hJ.2 s hs).clm_apply (hasDerivWithinAt_const s _ ((0 : V), b))
      simpa using this
    have hX : HasDerivWithinAt (fun s => (G.D.J (p, a) s (0, b)).1)
        (G.D.J (p, a) s (0, b)).2 (Icc (-G.D.τ) G.D.τ) s := by
      have := (ContinuousLinearMap.fst ℝ V V).hasFDerivAt.comp_hasDerivWithinAt s hJs
      have e := S.lb_fst_fderiv_cutField hg G.χ G.sub (G.lb_traj_in hg hyc hs)
        (G.D.J (p, a) s (0, b))
      exact this.congr_deriv (by simpa using e)
    have h := S.lb_hasDerivWithinAt_g ((hg.differentiable (by norm_num)) _)
      (G.lb_geodesic_fst hg hyc hs) (G.lb_geodesic_snd hg hyc hs) hX
    convert h using 1
    have hx := G.lb_ball_sub_M (G.lb_traj_in hg hyc hs)
    have hv := G.lb_energy_variation hg ha hs ((0 : V), b)
    simp only [S.lb_Dg_zero, zero_add] at hv
    rw [map_neg, neg_apply, S.lb_christoffel_koszul hx]
    linarith
  have := G.D.lb_affine_of_deriv hd t ht
  rw [this, hJ.1, G.D.init _ (G.lb_mem_r hyc)]
  simp

/-- **The Gauss lemma** (registered form): for `v` in the normal domain and every `w`,
`g_{exp_p v}(D exp_p(v) v, D exp_p(v) w) = g_p(v, w)`. -/
theorem lb_gauss (hg : ContDiff ℝ 2 S.g) {v : V} (hv : v ∈ ball (0 : V) G.ρ) (w : V) :
    S.g (G.expp v) (G.Dexp v v) (G.Dexp v w) = S.g p v w := by
  rw [G.lb_Dexp_radial hg hv, rad, lb_Dexp_apply, expp]
  have := G.lb_gauss_flow hg (G.lb_dom hv) (G.c • w) G.lb_s₀_mem
  simp only [map_smul, FunLike.coe_smul, Pi.smul_apply, smul_eq_mul] at this ⊢
  rw [this]
  have hcs := G.lb_c_s₀
  linear_combination (G.c * G.s₀ + 1) * S.g p v w * hcs

/-- The radial velocity has the energy of `v`: `g_{exp v}(rad v, rad v) = g_p(v, v)`. -/
theorem lb_rad_energy (hg : ContDiff ℝ 2 S.g) {v : V} (hv : v ∈ ball (0 : V) G.ρ) :
    S.g (G.expp v) (G.rad v) (G.rad v) = S.g p v v := by
  have := G.lb_energy_cons hg (G.lb_dom_closed hv) G.lb_s₀_mem
  rw [rad, expp]
  simp only [map_smul, FunLike.coe_smul, Pi.smul_apply, smul_eq_mul] at this ⊢
  rw [this]
  have hcs := G.lb_c_s₀
  linear_combination (G.c * G.s₀ + 1) * S.g p v v * hcs


/-! ## ③ Local maximality: the normal chart, `Q = g_p(exp⁻¹, exp⁻¹)`, the position field -/

/-- A normal chart at `p`: `exp_p` restricted to a neighbourhood of `0` on which it is a `C¹`
open partial homeomorphism (from `lb_expp_localDiffeo`). -/
structure NormalChart where
  Φ : OpenPartialHomeomorph V V
  zero_mem : (0 : V) ∈ Φ.source
  source_sub : Φ.source ⊆ ball (0 : V) G.ρ
  eq : ∀ v ∈ Φ.source, Φ v = G.expp v
  map_zero : Φ 0 = p
  symm_smooth : ∀ᶠ x in 𝓝 p, ContDiffAt ℝ 1 Φ.symm x

theorem lb_normalChart_exists (hg : ContDiff ℝ 2 S.g) : Nonempty G.NormalChart := by
  obtain ⟨Φ, h0, hs, he, hm, _, hsy⟩ := G.lb_expp_localDiffeo hg
  exact ⟨⟨Φ, h0, hs, he, hm, hsy⟩⟩

namespace NormalChart

variable {G} (N : G.NormalChart)

/-- `Q(x) = g_p(exp_p⁻¹ x, exp_p⁻¹ x)`. -/
noncomputable def Q (x : V) : ℝ := S.g p (N.Φ.symm x) (N.Φ.symm x)

/-- The position field `P(x) = (D exp_p)(v) v` at `x = exp_p v`: the velocity at time `1` of the
radial geodesic from `p` to `x`. -/
noncomputable def P (x : V) : V := G.rad (N.Φ.symm x)

/-- Points of the chart's target where the inverse is `C¹`; a neighbourhood of `p`. -/
def good : Set V := {x | x ∈ N.Φ.target ∧ ContDiffAt ℝ 1 N.Φ.symm x}

theorem lb_good_nhds : N.good ∈ 𝓝 p := by
  have hp : p ∈ N.Φ.target := by
    have := N.Φ.map_source N.zero_mem; rwa [N.map_zero] at this
  exact (N.Φ.open_target.eventually_mem hp).and N.symm_smooth

theorem lb_good_src {x : V} (hx : x ∈ N.good) : N.Φ.symm x ∈ N.Φ.source :=
  N.Φ.map_target hx.1

theorem lb_good_dom {x : V} (hx : x ∈ N.good) : N.Φ.symm x ∈ ball (0 : V) G.ρ :=
  N.source_sub (N.lb_good_src hx)

theorem lb_good_expp {x : V} (hx : x ∈ N.good) : G.expp (N.Φ.symm x) = x := by
  rw [← N.eq _ (N.lb_good_src hx)]; exact N.Φ.right_inv hx.1

theorem lb_good_mem_M (hg : ContDiff ℝ 2 S.g) {x : V} (hx : x ∈ N.good) : x ∈ S.M := by
  rw [← N.lb_good_expp hx]
  exact G.lb_ball_sub_M (G.lb_traj_in hg (G.lb_dom_closed (N.lb_good_dom hx)) G.lb_s₀_mem)

/-- **The gradient of `Q` is twice the position field:** `DQ_x(ξ) = 2 g_x(P(x), ξ)` (Gauss lemma). -/
theorem lb_grad_Q (hg : ContDiff ℝ 2 S.g) {x : V} (hx : x ∈ N.good) :
    HasFDerivAt N.Q ((2 : ℝ) • S.g x (N.P x)) x := by
  have hv := N.lb_good_dom hx
  have hxe := N.lb_good_expp hx
  have hL : HasFDerivAt N.Φ.symm (fderiv ℝ N.Φ.symm x) x :=
    (hx.2.differentiableAt one_ne_zero).hasFDerivAt
  have hcomp := (G.lb_expp_hasFDerivAt hg hv).comp x hL
  have hid : G.expp ∘ N.Φ.symm =ᶠ[𝓝 x] id := by
    filter_upwards [N.Φ.open_target.mem_nhds hx.1] with y hy
    show G.expp (N.Φ.symm y) = y
    rw [← N.eq _ (N.Φ.map_target hy)]; exact N.Φ.right_inv hy
  have hDL : (G.Dexp (N.Φ.symm x)).comp (fderiv ℝ N.Φ.symm x) = ContinuousLinearMap.id ℝ V :=
    hcomp.unique ((hasFDerivAt_id x).congr_of_eventuallyEq hid)
  obtain ⟨E', hE', hEv⟩ := S.lb_energy_hasFDerivAt hg (p, N.Φ.symm x)
  have hq : HasFDerivAt (fun w : V => ((p, w) : V × V))
      ((0 : V →L[ℝ] V).prod (ContinuousLinearMap.id ℝ V)) (N.Φ.symm x) :=
    (hasFDerivAt_const p _).prodMk (hasFDerivAt_id _)
  have h1 := hE'.comp (N.Φ.symm x) hq
  have hQ := h1.comp x hL
  refine hQ.congr_fderiv ?_
  ext ξ
  have hξ := congrArg (fun T => T ξ) hDL
  simp only [ContinuousLinearMap.comp_apply, ContinuousLinearMap.id_apply] at hξ
  simp only [ContinuousLinearMap.comp_apply, ContinuousLinearMap.prod_apply,
    zero_apply, ContinuousLinearMap.id_apply, hEv, S.lb_Dg_zero, zero_add,
    FunLike.coe_smul, Pi.smul_apply, smul_eq_mul, P]
  rw [← G.lb_gauss hg hv, G.lb_Dexp_radial hg hv, hxe, hξ]

/-- `g_x(P, P) = Q(x)`: the position field has the energy of `exp⁻¹ x`. -/
theorem lb_P_energy (hg : ContDiff ℝ 2 S.g) {x : V} (hx : x ∈ N.good) :
    S.g x (N.P x) (N.P x) = N.Q x := by
  have := G.lb_rad_energy hg (N.lb_good_dom hx)
  rw [N.lb_good_expp hx] at this
  exact this

/-- `P(x) ≠ 0` for `x ≠ p` (Gauss lemma and nondegeneracy at `p`). -/
theorem lb_P_ne_zero (hg : ContDiff ℝ 2 S.g) {x : V} (hx : x ∈ N.good) (hxp : x ≠ p) :
    N.P x ≠ 0 := by
  intro h0
  have hv := N.lb_good_dom hx
  have hpM : p ∈ S.M := G.lb_ball_sub_M (mem_ball_self G.χ.rIn_pos)
  have hz : N.Φ.symm x = 0 := S.lb_nondegenerate hpM fun w => by
    rw [← G.lb_gauss hg hv, G.lb_Dexp_radial hg hv]
    have : G.rad (N.Φ.symm x) = 0 := h0
    rw [this]; simp
  apply hxp
  rw [← N.Φ.right_inv hx.1, hz, N.map_zero]

/-- `D exp_p(v) ∘ D(exp_p⁻¹)(x) = id` at good points, `v = exp_p⁻¹ x`. -/
theorem lb_Dexp_comp_symm (hg : ContDiff ℝ 2 S.g) {x : V} (hx : x ∈ N.good) :
    (G.Dexp (N.Φ.symm x)).comp (fderiv ℝ N.Φ.symm x) = ContinuousLinearMap.id ℝ V := by
  have hL : HasFDerivAt N.Φ.symm (fderiv ℝ N.Φ.symm x) x :=
    (hx.2.differentiableAt one_ne_zero).hasFDerivAt
  have hcomp := (G.lb_expp_hasFDerivAt hg (N.lb_good_dom hx)).comp x hL
  have hid : G.expp ∘ N.Φ.symm =ᶠ[𝓝 x] id := by
    filter_upwards [N.Φ.open_target.mem_nhds hx.1] with y hy
    show G.expp (N.Φ.symm y) = y
    rw [← N.eq _ (N.Φ.map_target hy)]; exact N.Φ.right_inv hy
  exact hcomp.unique ((hasFDerivAt_id x).congr_of_eventuallyEq hid)

/-- **In normal coordinates the position field is the Euler field:** `D(exp_p⁻¹)(x) P(x) = exp_p⁻¹ x`.
So the radial geodesics from `p` are the integral curves of `P`. -/
theorem lb_P_euler (hg : ContDiff ℝ 2 S.g) {x : V} (hx : x ∈ N.good) :
    fderiv ℝ N.Φ.symm x (N.P x) = N.Φ.symm x := by
  have hv := N.lb_good_dom hx
  have hDL := N.lb_Dexp_comp_symm hg hx
  have hDL' : ∀ y, G.Dexp (N.Φ.symm x) (fderiv ℝ N.Φ.symm x y) = y := fun y => by
    have := congrArg (fun T => T y) hDL; simpa using this
  have hsurj : Function.Surjective (G.Dexp (N.Φ.symm x)) := fun y => ⟨_, hDL' y⟩
  have hinj : Function.Injective (G.Dexp (N.Φ.symm x)) := by
    have := (LinearMap.injective_iff_surjective
      (f := ((G.Dexp (N.Φ.symm x) : V →L[ℝ] V) : V →ₗ[ℝ] V))).2 hsurj
    exact this
  apply hinj
  rw [hDL', P, G.lb_Dexp_radial hg hv]

/-- **Local maximality, pointwise.** If a curve stays in the null conoid `{Q = 0}` near `t₀`, is
differentiable at `t₀` with causal velocity, and `γ t₀ ≠ p`, then `γ′(t₀) ∥ P(γ t₀)`, and `P` is a
nonzero null vector there. -/
theorem lb_null_tangent (hg : ContDiff ℝ 2 S.g) {γ : ℝ → V} {t₀ : ℝ} {γ' : V}
    (hγ : HasDerivAt γ γ' t₀) (hQ : ∀ᶠ s in 𝓝 t₀, N.Q (γ s) = 0) (hgood : γ t₀ ∈ N.good)
    (hne : γ t₀ ≠ p) (hc : S.g (γ t₀) γ' γ' ≤ 0) :
    (∃ k : ℝ, γ' = k • N.P (γ t₀)) ∧ S.g (γ t₀) (N.P (γ t₀)) (N.P (γ t₀)) = 0 ∧
      N.P (γ t₀) ≠ 0 := by
  have hD := (N.lb_grad_Q hg hgood).comp_hasDerivAt t₀ hγ
  have h0 : HasDerivAt (N.Q ∘ γ) 0 t₀ := (hasDerivAt_const t₀ (0 : ℝ)).congr_of_eventuallyEq hQ
  have hPw : S.g (γ t₀) (N.P (γ t₀)) γ' = 0 := by
    have := hD.unique h0
    simp only [FunLike.coe_smul, Pi.smul_apply, smul_eq_mul] at this
    linarith
  have hPP : S.g (γ t₀) (N.P (γ t₀)) (N.P (γ t₀)) = 0 := by
    rw [N.lb_P_energy hg hgood]; exact hQ.self_of_nhds
  have hP0 := N.lb_P_ne_zero hg hgood hne
  exact ⟨S.lb_causal_perp_null (N.lb_good_mem_M hg hgood) hPP hP0 hc hPw, hPP, hP0⟩

/-- **Local maximality, Lipschitz form.** A Lipschitz curve on `[0,1]` that stays in `{Q = 0}`
inside the chart, avoids `p` on `(0,1)`, and has causal velocity a.e., has velocity `∥ P` a.e. -/
theorem lb_ae_null_tangent (hg : ContDiff ℝ 2 S.g) {γ : ℝ → V} {K : ℝ≥0}
    (hlip : LipschitzOnWith K γ (Icc 0 1)) (hQ : ∀ s ∈ Icc (0 : ℝ) 1, N.Q (γ s) = 0)
    (hgood : ∀ s ∈ Ioo (0 : ℝ) 1, γ s ∈ N.good ∧ γ s ≠ p)
    (hc : ∀ᵐ t ∂(MeasureTheory.volume : MeasureTheory.Measure ℝ), t ∈ Ioo (0 : ℝ) 1 →
      DifferentiableAt ℝ γ t → S.g (γ t) (deriv γ t) (deriv γ t) ≤ 0) :
    ∀ᵐ t ∂(MeasureTheory.volume : MeasureTheory.Measure ℝ), t ∈ Ioo (0 : ℝ) 1 →
      ∃ k : ℝ, deriv γ t = k • N.P (γ t) := by
  filter_upwards [hlip.ae_differentiableWithinAt_of_mem (μ := MeasureTheory.volume), hc]
    with t ht1 ht2 htI
  have hd : DifferentiableAt ℝ γ t :=
    (ht1 (Ioo_subset_Icc_self htI)).differentiableAt (Icc_mem_nhds htI.1 htI.2)
  have hQ' : ∀ᶠ s in 𝓝 t, N.Q (γ s) = 0 := by
    filter_upwards [Ioo_mem_nhds htI.1 htI.2] with s hs
    exact hQ s (Ioo_subset_Icc_self hs)
  exact (N.lb_null_tangent hg hd.hasDerivAt hQ' (hgood t htI).1 (hgood t htI).2
    (ht2 htI hd)).1

end NormalChart

/-! ### The timelike side: `exp_p` of a future-timelike vector is in `I⁺(p)` -/

/-- **Timelike radial geodesics give `≪`.** If `v` is future-timelike at `p` and `‖v‖ < ρ/3`, then
`p ≪ exp_p v`: the radial geodesic `t ↦ exp_p(t v)`, reparametrised outside `[0,1]` by a bump so as
to be globally `C¹`, is one future-timelike step (energy conservation for `g(γ′,γ′) < 0`, the
intermediate value theorem for the time orientation). -/
theorem lb_chr_of_timelike (hg : ContDiff ℝ 2 S.g) {v : V} (hv : v ∈ ball (0 : V) (G.ρ / 3))
    (hvt : S.FutTimelike p v) : S.Chr p (G.expp v) := by
  have hρ := G.lb_ρ_pos
  have hv' : v ∈ ball (0 : V) G.ρ := ball_subset_ball (by linarith) hv
  have hvn := mem_ball_zero_iff.1 hv
  -- the reparametrisation `ψ`, the identity near `[0,1]` and bounded by `3`
  let b : ContDiffBump (1 / 2 : ℝ) := ⟨1, 2, one_pos, one_lt_two⟩
  let ψ : ℝ → ℝ := fun t => 1 / 2 + (t - 1 / 2) * b t
  have hψc : ContDiff ℝ 1 ψ := contDiff_const.add ((contDiff_id.sub contDiff_const).mul b.contDiff)
  have hψid : ∀ t ∈ Icc (0 : ℝ) 1, ψ =ᶠ[𝓝 t] id := by
    intro t ht
    have hb : t ∈ ball (1 / 2 : ℝ) b.rIn := by
      rw [mem_ball, Real.dist_eq, abs_lt]; show _ ∧ _; constructor <;> linarith [ht.1, ht.2]
    filter_upwards [b.eventuallyEq_one_of_mem_ball hb] with s hs
    simp only [ψ, id]; rw [hs]; simp
  have hψb : ∀ t, |ψ t| ≤ 3 := by
    intro t
    have h1 : |ψ t| ≤ 1 / 2 + |t - 1 / 2| * b t := by
      calc |ψ t| ≤ |(1 / 2 : ℝ)| + |(t - 1 / 2) * b t| := abs_add_le _ _
        _ = 1 / 2 + |t - 1 / 2| * b t := by rw [abs_mul, abs_of_nonneg b.nonneg]; norm_num
    by_cases h : |t - 1 / 2| < 2
    · nlinarith [(b.le_one : b t ≤ 1), (b.nonneg : 0 ≤ b t), abs_nonneg (t - 1 / 2)]
    · have : b t = 0 := b.zero_of_le_dist (by rw [Real.dist_eq]; show (2:ℝ) ≤ _; linarith [not_lt.1 h])
      rw [this, mul_zero] at h1; linarith
  have hmem : ∀ t, ψ t • v ∈ ball (0 : V) G.ρ := fun t => by
    rw [mem_ball_zero_iff, norm_smul, Real.norm_eq_abs]
    nlinarith [abs_nonneg (ψ t), norm_nonneg v, hψb t]
  -- the curve
  let γ : ℝ → V := fun t => G.expp (ψ t • v)
  have hγc : ContDiff ℝ 1 γ := contDiff_iff_contDiffAt.2 fun t => by
    have h1 : ContDiffAt ℝ 1 (fun s => ψ s • v) t := hψc.contDiffAt.smul contDiffAt_const
    have h2 := (G.lb_expp_contDiffAt hg (hmem t)).comp t h1
    exact h2
  have hψ0 : ψ 0 = 0 := by
    have : b 0 = 1 := b.one_of_mem_closedBall (by rw [mem_closedBall, Real.dist_eq]; norm_num)
    simp only [ψ, this]; norm_num
  have hψ1 : ψ 1 = 1 := by
    have : b 1 = 1 := b.one_of_mem_closedBall (by rw [mem_closedBall, Real.dist_eq]; norm_num)
    simp only [ψ, this]; norm_num
  -- on `[0,1]`: position and velocity of the radial geodesic
  have hpos : ∀ t ∈ Icc (0 : ℝ) 1, γ t = G.expp (t • v) := fun t ht => by
    simp only [γ]; rw [(hψid t ht).self_of_nhds]; rfl
  have hder : ∀ t ∈ Icc (0 : ℝ) 1, deriv γ t = G.Dexp (t • v) v := by
    intro t ht
    have htv : t • v ∈ ball (0 : V) G.ρ := by
      rw [mem_ball_zero_iff, norm_smul, Real.norm_eq_abs, abs_of_nonneg ht.1]
      nlinarith [norm_nonneg v, ht.2]
    have h1 : HasDerivAt (fun s : ℝ => G.expp (s • v)) (G.Dexp (t • v) v) t := by
      have hline : HasDerivAt (fun m : ℝ => m • v) v t := by
        simpa using (hasDerivAt_id t).smul_const v
      exact (G.lb_expp_hasFDerivAt hg htv).comp_hasDerivAt t hline
    have h2 : γ =ᶠ[𝓝 t] fun s : ℝ => G.expp (s • v) := by
      filter_upwards [hψid t ht] with s hs
      simp only [γ]; rw [hs]; rfl
    exact (h1.congr_of_eventuallyEq h2).deriv
  have hgeo : ∀ t ∈ Icc (0 : ℝ) 1, γ t = (G.D.α (p, G.c • v) (t * G.s₀)).1 ∧
      deriv γ t = G.s₀ • (G.D.α (p, G.c • v) (t * G.s₀)).2 := fun t ht =>
    ⟨(hpos t ht).trans (G.lb_expp_smul hg hv' ht), (hder t ht).trans (G.lb_Dexp_radial_at hg hv' ht)⟩
  have hM : ∀ t ∈ Icc (0 : ℝ) 1, γ t ∈ S.M := fun t ht => by
    rw [(hgeo t ht).1]
    exact G.lb_ball_sub_M (G.lb_traj_in hg (G.lb_dom_closed hv') (G.lb_mul_s₀_mem ht))
  have htl : ∀ t ∈ Icc (0 : ℝ) 1, S.g (γ t) (deriv γ t) (deriv γ t) < 0 := fun t ht => by
    rw [(hgeo t ht).1, (hgeo t ht).2]
    have hE := G.lb_energy_cons hg (G.lb_dom_closed hv') (G.lb_mul_s₀_mem ht)
    simp only [map_smul, FunLike.coe_smul, Pi.smul_apply, smul_eq_mul] at hE ⊢
    rw [hE]
    have hcs := G.lb_c_s₀
    have : G.s₀ * (G.s₀ * (G.c * (G.c * S.g p v v))) = S.g p v v := by
      linear_combination (G.c * G.s₀ + 1) * S.g p v v * hcs
    rw [this]; exact hvt.1
  -- the time orientation does not flip along `[0,1]`
  let h : ℝ → ℝ := fun t => S.g (γ t) (deriv γ t) (S.T (γ t))
  have hhc : Continuous h :=
    ((S.cont_g.comp hγc.continuous).clm_apply (hγc.continuous_deriv le_rfl)).clm_apply
      (S.cont_T.comp hγc.continuous)
  have hh0 : h 0 < 0 := by
    have e1 : γ 0 = p := by simp only [γ, hψ0, zero_smul]; exact G.lb_expp_zero hg
    have e2 : deriv γ 0 = v := by
      rw [hder 0 ⟨le_rfl, zero_le_one⟩, zero_smul, G.lb_Dexp_zero hg]; rfl
    simp only [h, e1, e2]; exact hvt.2
  have hne : ∀ t ∈ Icc (0 : ℝ) 1, h t ≠ 0 := fun t ht h0 => by
    have hd0 : deriv γ t ≠ 0 := fun hz => by have := htl t ht; rw [hz] at this; simp at this
    have := S.pos_on_perp (γ t) (hM t ht) (deriv γ t) h0 hd0
    linarith [htl t ht]
  have hfut : ∀ t ∈ Icc (0 : ℝ) 1, h t < 0 := by
    intro t ht
    by_contra hcon
    rw [not_lt] at hcon
    obtain ⟨s, hs, hs0⟩ := intermediate_value_Icc ht.1 hhc.continuousOn ⟨hh0.le, hcon⟩
    exact hne s ⟨hs.1, hs.2.trans ht.2⟩ hs0
  refine Relation.TransGen.single ⟨γ, hγc, ?_, ?_, fun t ht => ⟨hM t ht, htl t ht, hfut t ht⟩⟩
  · simp only [γ, hψ0, zero_smul]; exact G.lb_expp_zero hg
  · simp only [γ, hψ1, one_smul]

namespace NormalChart

variable {G} (N : G.NormalChart)

/-- **Inside the conoid is chronological.** A point `x` of the chart with `Q(x) < 0`, whose normal
coordinate `exp⁻¹ x` points to the future and is small, satisfies `p ≪ x`. -/
theorem lb_chr_of_Q_neg (hg : ContDiff ℝ 2 S.g) {x : V} (hx : x ∈ N.good) (hQ : N.Q x < 0)
    (hfut : S.g p (N.Φ.symm x) (S.T p) < 0) (hsmall : N.Φ.symm x ∈ ball (0 : V) (G.ρ / 3)) :
    S.Chr p x := by
  have := G.lb_chr_of_timelike hg hsmall ⟨hQ, hfut⟩
  rwa [N.lb_good_expp hx] at this

end NormalChart

end GeoFlow

end Spacetime

/-! ## Copied from campaign 70 (`probes/CornerCutting.lean`, `ct_` ↦ `lb_`): causal relations, the
horizon `H = ∂J⁻(J)`, pregeodesics, corner-cutting, and `lb_H_generator_null_pregeodesic`.

`Spacetime`, `FutTimelike`, `FutCausal`, `TStep`, `Chr`, `Dg`, nondegeneracy, the product rule and
`Γ` are the campaign-71 copies above. Campaign 70's `Γ` was `♭⁻¹` of the Koszul covector through a
`Classical.choose`; here it is campaign 71's `ContinuousLinearMap.inverse (g x)` form, and the only
property used, the Koszul identity `lb_christoffel_koszul`, holds for both. -/

namespace Spacetime
variable (S : Spacetime V)

/-- One `C¹` future-causal piece from `x` to `y`, parametrised by `[0,1]`. -/
def CStep (x y : V) : Prop :=
  ∃ γ : ℝ → V, ContDiff ℝ 1 γ ∧ γ 0 = x ∧ γ 1 = y ∧
    ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ S.M ∧ S.FutCausal (γ t) (deriv γ t)

/-- Causal relation `x ≤ y`. -/
def Cau (x y : V) : Prop := Relation.ReflTransGen S.CStep x y

/-- `I⁻(p)`. -/
def Ipast (p : V) : Set V := {q | S.Chr q p}
/-- `I⁺(p)`. -/
def Ifut (p : V) : Set V := {q | S.Chr p q}
/-- `J⁻(p)`. -/
def Jpast (p : V) : Set V := {q | S.Cau q p}
/-- `J⁻(A)`. -/
def JpastSet (A : Set V) : Set V := ⋃ p ∈ A, S.Jpast p
/-- The event horizon `𝓗⁺ = ∂J⁻(𝒥⁺)` for a hypothesis-supplied `𝒥⁺ = J`. -/
def H (J : Set V) : Set V := frontier (S.JpastSet J)

/-! ### Copied from campaign 60: openness of `I±`, `I ⊆ J` -/

lemma lb_cont_gvw {X : Type*} [TopologicalSpace X] {x v w : X → V} (hx : Continuous x)
    (hv : Continuous v) (hw : Continuous w) : Continuous fun a => S.g (x a) (v a) (w a) :=
  ((S.cont_g.comp hx).clm_apply hv).clm_apply hw

lemma lb_isOpen_timelikePairs :
    IsOpen {pv : V × V | pv.1 ∈ S.M ∧ S.FutTimelike pv.1 pv.2} := by
  refine (S.isOpen_M.preimage continuous_fst).inter (IsOpen.inter ?_ ?_)
  · exact isOpen_lt (S.lb_cont_gvw continuous_fst continuous_snd continuous_snd) continuous_const
  · exact isOpen_lt (S.lb_cont_gvw continuous_fst continuous_snd
      (S.cont_T.comp continuous_fst)) continuous_const

lemma lb_tube {P Q : V → ℝ → V} (hP : Continuous fun z : V × ℝ => P z.1 z.2)
    (hQ : Continuous fun z : V × ℝ => Q z.1 z.2)
    (h0 : ∀ t ∈ Icc (0:ℝ) 1, P 0 t ∈ S.M ∧ S.FutTimelike (P 0 t) (Q 0 t)) :
    ∀ᶠ w in 𝓝 (0:V), ∀ t ∈ Icc (0:ℝ) 1, P w t ∈ S.M ∧ S.FutTimelike (P w t) (Q w t) := by
  refine isCompact_Icc.eventually_forall_of_forall_eventually fun t ht => ?_
  have hO := S.lb_isOpen_timelikePairs.preimage (hP.prodMk hQ)
  exact hO.mem_nhds (h0 t ht)

lemma lb_hasDerivAt_of_contDiff {γ : ℝ → V} (hγ : ContDiff ℝ 1 γ) (t : ℝ) :
    HasDerivAt γ (deriv γ t) t :=
  ((hγ.differentiable one_ne_zero) t).hasDerivAt

lemma lb_tstep_end_eventually {y q : V} (h : S.TStep y q) : ∀ᶠ q' in 𝓝 q, S.TStep y q' := by
  obtain ⟨γ, hγ, h0, h1, hγt⟩ := h
  have hdc : Continuous (deriv γ) := hγ.continuous_deriv le_rfl
  have hT := S.lb_tube (P := fun w t => γ t + t • w) (Q := fun w t => deriv γ t + w)
    ((hγ.continuous.comp continuous_snd).add (continuous_snd.smul continuous_fst))
    ((hdc.comp continuous_snd).add continuous_fst) (by simpa using hγt)
  have hlim : Tendsto (fun q' => q' - q) (𝓝 q) (𝓝 0) := tendsto_sub_nhds_zero_iff.2 tendsto_id
  filter_upwards [hlim.eventually hT] with q' hq'
  refine ⟨fun t => γ t + t • (q' - q), hγ.add (contDiff_id.smul contDiff_const), by simp [h0],
    by simp [h1], fun t ht => ?_⟩
  have hd : deriv (fun t => γ t + t • (q' - q)) t = deriv γ t + (q' - q) := by
    have h : HasDerivAt (fun t => γ t + t • (q' - q)) (deriv γ t + (1:ℝ) • (q' - q)) t :=
      (lb_hasDerivAt_of_contDiff hγ t).add ((hasDerivAt_id' t).smul_const (q' - q))
    rw [h.deriv, one_smul]
  rw [hd]; exact hq' t ht

lemma lb_tstep_start_eventually {p y : V} (h : S.TStep p y) : ∀ᶠ p' in 𝓝 p, S.TStep p' y := by
  obtain ⟨γ, hγ, h0, h1, hγt⟩ := h
  have hdc : Continuous (deriv γ) := hγ.continuous_deriv le_rfl
  have hT := S.lb_tube (P := fun w t => γ t + (1 - t) • w) (Q := fun w t => deriv γ t - w)
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
      (lb_hasDerivAt_of_contDiff hγ t).add
        (((hasDerivAt_const t (1:ℝ)).sub (hasDerivAt_id' t)).smul_const (p' - p))
    rw [h.deriv, zero_sub, neg_one_smul, ← sub_eq_add_neg]
  rw [hd]; exact hp' t ht

theorem lb_isOpen_Ifut (p : V) : IsOpen (S.Ifut p) := by
  refine isOpen_iff_mem_nhds.2 fun q hq => ?_
  obtain ⟨y, hpy, hyq⟩ := Relation.TransGen.tail'_iff.1 hq
  filter_upwards [S.lb_tstep_end_eventually hyq] with q' hq'
  exact Relation.TransGen.tail' hpy hq'

theorem lb_isOpen_Ipast (p : V) : IsOpen (S.Ipast p) := by
  refine isOpen_iff_mem_nhds.2 fun q hq => ?_
  obtain ⟨y, hqy, hyp⟩ := Relation.TransGen.head'_iff.1 hq
  filter_upwards [S.lb_tstep_start_eventually hqy] with q' hq'
  exact Relation.TransGen.head' hq' hyp

lemma lb_tstep_to_cstep {x y : V} (h : S.TStep x y) : S.CStep x y := by
  obtain ⟨γ, hγ, h0, h1, hγt⟩ := h
  exact ⟨γ, hγ, h0, h1, fun t ht => ⟨(hγt t ht).1, (hγt t ht).2.1.le, (hγt t ht).2.2⟩⟩

theorem lb_chr_cau {x y : V} (h : S.Chr x y) : S.Cau x y := by
  induction h with
  | single h => exact Relation.ReflTransGen.single (S.lb_tstep_to_cstep h)
  | tail _ h ih => exact ih.tail (S.lb_tstep_to_cstep h)

lemma lb_Dg_smul (x w u v : V) (c : ℝ) : S.Dg x (c • w) u v = c * S.Dg x w u v := by
  simp [Dg]

lemma lb_cont_Dg {X : Type*} [TopologicalSpace X] (hg : ContDiff ℝ 1 S.g) {x w u v : X → V}
    (hx : Continuous x) (hw : Continuous w) (hu : Continuous u) (hv : Continuous v) :
    Continuous fun a => S.Dg (x a) (w a) (u a) (v a) :=
  ((((hg.continuous_fderiv one_ne_zero).comp hx).clm_apply hw).clm_apply hu).clm_apply hv

/-! ### Curves: acceleration, pregeodesics, metric compatibility -/

/-- The geodesic operator `∇_{γ'}γ' = γ'' + Γ(γ',γ')`. -/
noncomputable def acc (γ : ℝ → V) (t : ℝ) : V :=
  deriv (deriv γ) t + S.Γ (γ t) (deriv γ t) (deriv γ t)

/-- `γ` is a pregeodesic at `t`: `∇_{γ'}γ' ∥ γ'`. -/
def IsPregeodesicAt (γ : ℝ → V) (t : ℝ) : Prop := ∃ f : ℝ, S.acc γ t = f • deriv γ t

/-- `γ` is a pregeodesic on `I`: `∇_{γ'}γ' = f · γ'` there. -/
def IsPregeodesicOn (γ : ℝ → V) (I : Set ℝ) : Prop :=
  ∃ f : ℝ → ℝ, ∀ t ∈ I, S.acc γ t = f t • deriv γ t

theorem lb_pregeodesicOn_of_forall {γ : ℝ → V} {I : Set ℝ}
    (h : ∀ t ∈ I, S.IsPregeodesicAt γ t) : S.IsPregeodesicOn γ I := by
  classical
  refine ⟨fun t => if ht : t ∈ I then (h t ht).choose else 0, fun t ht => ?_⟩
  simp only [dif_pos ht]
  exact (h t ht).choose_spec

lemma lb_deriv_contDiff {γ : ℝ → V} (hγ : ContDiff ℝ 2 γ) : ContDiff ℝ 1 (deriv γ) :=
  (contDiff_succ_iff_deriv.1 hγ).2.2

/-- **Covariant product rule** along `γ`: `d/dt g(γ',W) = g(acc,W) + g(γ',W') + ½ Dg(W)(γ',γ')`. -/
theorem lb_deriv_g_vel_field (hg : Differentiable ℝ S.g) {γ W : ℝ → V}
    (hγ : ContDiff ℝ 2 γ) {W' : V} {t : ℝ} (hW : HasDerivAt W W' t) (ht : γ t ∈ S.M) :
    HasDerivAt (fun r => S.g (γ r) (deriv γ r) (W r))
      (S.g (γ t) (S.acc γ t) (W t) + S.g (γ t) (deriv γ t) W'
        + S.Dg (γ t) (W t) (deriv γ t) (deriv γ t) / 2) t := by
  have h := S.lb_hasDerivAt_g (hg (γ t))
    (lb_hasDerivAt_of_contDiff (hγ.of_le (by norm_num)) t)
    (lb_hasDerivAt_of_contDiff (lb_deriv_contDiff hγ) t) hW
  convert h using 1
  rw [acc, map_add, add_apply, S.lb_christoffel_koszul ht]
  ring

/-- **Metric compatibility along a curve:** `d/dt g(γ',γ') = 2 g(γ', acc)`. -/
theorem lb_metric_compat (hg : Differentiable ℝ S.g) {γ : ℝ → V}
    (hγ : ContDiff ℝ 2 γ) {t : ℝ} (ht : γ t ∈ S.M) :
    HasDerivAt (fun r => S.g (γ r) (deriv γ r) (deriv γ r))
      (2 * S.g (γ t) (deriv γ t) (S.acc γ t)) t := by
  have h := S.lb_deriv_g_vel_field hg hγ
    (lb_hasDerivAt_of_contDiff (lb_deriv_contDiff hγ) t) ht
  convert h using 1
  rw [S.symm (γ t) (deriv γ t) (S.acc γ t), acc, map_add, add_apply,
    S.lb_christoffel_koszul ht, S.symm (γ t) (deriv (deriv γ) t)]
  ring

lemma lb_hasDerivAt_line (p q : V) (e : ℝ) : HasDerivAt (fun e : ℝ => p + e • q) q e := by
  simpa using ((hasDerivAt_id' e).smul_const q).const_add p

/-- **First variation** of the quadratic form along `γ_ε = γ + εW` at a fixed parameter `t`:
`∂_ε|₀ g(γ_ε',γ_ε') = Dg(W)(γ',γ') + 2g(γ',W') = 2 d/dt g(γ',W) − 2 g(acc,W)`. -/
theorem lb_first_variation (hg : Differentiable ℝ S.g) {γ W : ℝ → V}
    (hγ : ContDiff ℝ 2 γ) {t : ℝ} (hW : HasDerivAt W (deriv W t) t) (ht : γ t ∈ S.M) :
    HasDerivAt (fun e : ℝ => S.g (γ t + e • W t) (deriv γ t + e • deriv W t)
        (deriv γ t + e • deriv W t))
      (S.Dg (γ t) (W t) (deriv γ t) (deriv γ t) + 2 * S.g (γ t) (deriv γ t) (deriv W t)) 0 ∧
    S.Dg (γ t) (W t) (deriv γ t) (deriv γ t) + 2 * S.g (γ t) (deriv γ t) (deriv W t)
      = 2 * deriv (fun r => S.g (γ r) (deriv γ r) (W r)) t - 2 * S.g (γ t) (S.acc γ t) (W t) := by
  constructor
  · have h := S.lb_hasDerivAt_g (hg _) (lb_hasDerivAt_line (γ t) (W t) 0)
      (lb_hasDerivAt_line (deriv γ t) (deriv W t) 0)
      (lb_hasDerivAt_line (deriv γ t) (deriv W t) 0)
    simp only [zero_smul, add_zero] at h
    convert h using 1
    rw [S.symm (γ t) (deriv W t)]; ring
  · rw [(S.lb_deriv_g_vel_field hg hγ hW ht).deriv]; ring

/-! ## ② The corner-cutting lemma -/

/-- Linear algebra: if `A ∉ ℝ·v` and `g(v,T) ≠ 0`, some `Z ⊥ v` has `g(A,Z) > 0`. -/
theorem lb_exists_transverse {x : V} (hx : x ∈ S.M) {v A : V} (hvT : S.g x v (S.T x) ≠ 0)
    (hA : ¬ ∃ f : ℝ, A = f • v) : ∃ Z, S.g x v Z = 0 ∧ 0 < S.g x A Z := by
  by_contra H
  push Not at H
  apply hA
  set τ := S.T x
  have hker : ∀ Z, S.g x v Z = 0 → S.g x A Z = 0 := fun Z hZ => by
    have h1 := H Z hZ
    have h2 := H (-Z) (by simp [hZ])
    simp only [map_neg] at h2
    linarith
  refine ⟨S.g x A τ / S.g x v τ, sub_eq_zero.1 (S.lb_nondegenerate hx fun w => ?_)⟩
  have hw := hker (w - (S.g x v w / S.g x v τ) • τ) (by
    simp only [map_sub, map_smul, smul_eq_mul]; field_simp; ring)
  simp only [map_sub, map_smul, smul_eq_mul, sub_apply,
    smul_apply] at hw ⊢
  field_simp at hw ⊢
  linarith

/-- An affine reparametrisation of a timelike `C¹` curve on `[s,t]` is a `TStep`. -/
theorem lb_tstep_of_curve {σ : ℝ → V} (hσ : ContDiff ℝ 1 σ) {s t : ℝ} (hst : s < t)
    (h : ∀ r ∈ Icc s t, σ r ∈ S.M ∧ S.FutTimelike (σ r) (deriv σ r)) :
    S.TStep (σ s) (σ t) := by
  have haff : ContDiff ℝ 1 fun x : ℝ => s + x * (t - s) :=
    contDiff_const.add (contDiff_id.mul contDiff_const)
  refine ⟨fun x => σ (s + x * (t - s)), hσ.comp haff, by simp, by simp, fun x hx => ?_⟩
  have hr : s + x * (t - s) ∈ Icc s t := by
    constructor <;> nlinarith [hx.1, hx.2]
  have hd : deriv (fun x => σ (s + x * (t - s))) x = (t - s) • deriv σ (s + x * (t - s)) := by
    have ha : HasDerivAt (fun x : ℝ => s + x * (t - s)) (t - s) x := by
      simpa using ((hasDerivAt_id' x).mul_const (t - s)).const_add s
    exact ((lb_hasDerivAt_of_contDiff hσ _).scomp x ha).deriv
  obtain ⟨hM, h1, h2⟩ := h _ hr
  refine ⟨hM, ?_, ?_⟩ <;> rw [hd]
  · simp only [map_smul, smul_apply, smul_eq_mul]
    have : 0 < t - s := sub_pos.2 hst
    nlinarith [mul_pos this this]
  · simp only [map_smul, smul_apply, smul_eq_mul]
    exact mul_neg_of_pos_of_neg (sub_pos.2 hst) h2

/-- **First variation ⟹ timelike.** If `γ` is a causal `C¹` curve on `[s,t]`, `W` a `C¹` field
vanishing at `s` and `t`, and the first variation `Dg(W)(γ',γ') + 2g(γ',W')` is negative on the
whole of `[s,t]`, then `γ(s) ≪ γ(t)` (realised by `γ + εW` for a small `ε > 0`). -/
theorem lb_variation_chr (hg : ContDiff ℝ 1 S.g) {γ W : ℝ → V} (hγ : ContDiff ℝ 1 γ)
    (hW : ContDiff ℝ 1 W) {s t : ℝ} (hst : s < t) (hWs : W s = 0) (hWt : W t = 0)
    (hγc : ∀ r ∈ Icc s t, γ r ∈ S.M ∧ S.FutCausal (γ r) (deriv γ r))
    (hneg : ∀ r ∈ Icc s t,
      S.Dg (γ r) (W r) (deriv γ r) (deriv γ r) + 2 * S.g (γ r) (deriv γ r) (deriv W r) < 0) :
    S.Chr (γ s) (γ t) := by
  have hγ'c : Continuous (deriv γ) := hγ.continuous_deriv le_rfl
  have hW'c : Continuous (deriv W) := hW.continuous_deriv le_rfl
  have hgd : Differentiable ℝ S.g := hg.differentiable one_ne_zero
  -- the curve, its velocity, and the `ε`-derivative of the quadratic form
  let σ : ℝ → ℝ → V := fun e r => γ r + e • W r
  let σ' : ℝ → ℝ → V := fun e r => deriv γ r + e • deriv W r
  let P : ℝ → ℝ → ℝ := fun e r => S.Dg (σ e r) (W r) (σ' e r) (σ' e r)
    + S.g (σ e r) (deriv W r) (σ' e r) + S.g (σ e r) (σ' e r) (deriv W r)
  have hσc : Continuous fun z : ℝ × ℝ => σ z.1 z.2 :=
    (hγ.continuous.comp continuous_snd).add (continuous_fst.smul (hW.continuous.comp continuous_snd))
  have hσ'c : Continuous fun z : ℝ × ℝ => σ' z.1 z.2 :=
    (hγ'c.comp continuous_snd).add (continuous_fst.smul (hW'c.comp continuous_snd))
  have hPc : Continuous fun z : ℝ × ℝ => P z.1 z.2 :=
    ((S.lb_cont_Dg hg hσc (hW.continuous.comp continuous_snd) hσ'c hσ'c).add
      (S.lb_cont_gvw hσc (hW'c.comp continuous_snd) hσ'c)).add
      (S.lb_cont_gvw hσc hσ'c (hW'c.comp continuous_snd))
  have hO : IsOpen {z : ℝ × ℝ | σ z.1 z.2 ∈ S.M ∧
      S.g (σ z.1 z.2) (σ' z.1 z.2) (S.T (σ z.1 z.2)) < 0 ∧ P z.1 z.2 < 0} :=
    (S.isOpen_M.preimage hσc).inter ((isOpen_lt (S.lb_cont_gvw hσc hσ'c (S.cont_T.comp hσc))
      continuous_const).inter (isOpen_lt hPc continuous_const))
  have hev : ∀ᶠ e in 𝓝 (0:ℝ), ∀ r ∈ Icc s t, σ e r ∈ S.M ∧
      S.g (σ e r) (σ' e r) (S.T (σ e r)) < 0 ∧ P e r < 0 := by
    refine isCompact_Icc.eventually_forall_of_forall_eventually fun r hr => hO.mem_nhds ?_
    obtain ⟨hM, -, hT⟩ := hγc r hr
    have hn := hneg r hr
    simp only [σ, σ', P, zero_smul, add_zero, Set.mem_ofPred_eq]
    refine ⟨hM, hT, ?_⟩
    rw [S.symm (γ r) (deriv W r)]; linarith
  obtain ⟨η, hη, hball⟩ := Metric.eventually_nhds_iff.1 hev
  set ε := η / 2 with hεdef
  have hε : 0 < ε := by positivity
  have hgood : ∀ e ∈ Icc (0:ℝ) ε, ∀ r ∈ Icc s t, σ e r ∈ S.M ∧
      S.g (σ e r) (σ' e r) (S.T (σ e r)) < 0 ∧ P e r < 0 := fun e he => hball (by
    rw [Real.dist_eq, sub_zero, abs_of_nonneg he.1]; linarith [he.2])
  -- the quadratic form decreases in `ε`
  have hQ : ∀ r ∈ Icc s t, S.g (σ ε r) (σ' ε r) (σ' ε r) < 0 := by
    intro r hr
    have hderiv : ∀ e, HasDerivAt (fun e => S.g (σ e r) (σ' e r) (σ' e r)) (P e r) e := by
      intro e
      have h := S.lb_hasDerivAt_g (hgd _) (lb_hasDerivAt_line (γ r) (W r) e)
        (lb_hasDerivAt_line (deriv γ r) (deriv W r) e)
        (lb_hasDerivAt_line (deriv γ r) (deriv W r) e)
      exact h
    obtain ⟨c, hc, hcq⟩ := exists_hasDerivAt_eq_slope
      (fun e => S.g (σ e r) (σ' e r) (σ' e r)) (fun e => P e r) hε
      (fun e _ => (hderiv e).continuousAt.continuousWithinAt) (fun e _ => hderiv e)
    have hPneg := (hgood c ⟨hc.1.le, hc.2.le⟩ r hr).2.2
    have h0 : S.g (σ 0 r) (σ' 0 r) (σ' 0 r) ≤ 0 := by
      simpa [σ, σ'] using (hγc r hr).2.1
    rw [hcq, sub_zero, div_lt_iff₀ hε, zero_mul] at hPneg
    linarith
  -- the timelike curve
  have hσC : ContDiff ℝ 1 (σ ε) := hγ.add (contDiff_const.smul hW)
  have hσd : ∀ r, deriv (σ ε) r = σ' ε r := fun r =>
    ((lb_hasDerivAt_of_contDiff hγ r).add
      ((lb_hasDerivAt_of_contDiff hW r).const_smul ε)).deriv
  have hstep := S.lb_tstep_of_curve hσC hst fun r hr => by
    rw [hσd]
    exact ⟨(hgood ε ⟨hε.le, le_rfl⟩ r hr).1, hQ r hr, (hgood ε ⟨hε.le, le_rfl⟩ r hr).2.1⟩
  have hs : σ ε s = γ s := by simp [σ, hWs]
  have ht : σ ε t = γ t := by simp [σ, hWt]
  rw [hs, ht] at hstep
  exact Relation.TransGen.single hstep

/-- **The corner-cutting lemma.** A `C²` future-causal (e.g. future-null) curve that fails to be
a pregeodesic at an interior parameter `t₀` has two chronologically related points
`γ(s) ≪ γ(t)`, `a < s < t₀ < t < b`. -/
theorem lb_corner_cutting (hg : ContDiff ℝ 1 S.g) {γ : ℝ → V}
    (hγ : ContDiff ℝ 2 γ) {a b t₀ : ℝ} (ht₀ : t₀ ∈ Ioo a b)
    (hcaus : ∀ r ∈ Icc a b, γ r ∈ S.M ∧ S.FutCausal (γ r) (deriv γ r))
    (hnp : ¬ S.IsPregeodesicAt γ t₀) :
    ∃ s t, a < s ∧ s < t₀ ∧ t₀ < t ∧ t < b ∧ S.Chr (γ s) (γ t) := by
  have hγ1 : ContDiff ℝ 1 γ := hγ.of_le (by norm_num)
  have hγ2 : ContDiff ℝ 1 (deriv γ) := lb_deriv_contDiff hγ
  have hgd : Differentiable ℝ S.g := hg.differentiable one_ne_zero
  have hγd : ∀ r, HasDerivAt γ (deriv γ r) r := lb_hasDerivAt_of_contDiff hγ1
  have hγ'd : ∀ r, HasDerivAt (deriv γ) (deriv (deriv γ) r) r := lb_hasDerivAt_of_contDiff hγ2
  have hγc : Continuous γ := hγ1.continuous
  have hγ'c : Continuous (deriv γ) := hγ2.continuous
  have hγ''c : Continuous (deriv (deriv γ)) := hγ2.continuous_deriv le_rfl
  obtain ⟨hx₀M, hv⟩ := hcaus t₀ (Ioo_subset_Icc_self ht₀)
  have hvτ : S.g (γ t₀) (deriv γ t₀) (S.T (γ t₀)) < 0 := hv.2
  obtain ⟨Z₀, hZ₀v, hc₀⟩ := S.lb_exists_transverse hx₀M hvτ.ne hnp
  set c₀ := S.g (γ t₀) (S.acc γ t₀) Z₀ with hc₀def
  set μ := (-c₀ / 2 - S.Dg (γ t₀) Z₀ (deriv γ t₀) (deriv γ t₀) / 2) /
    S.g (γ t₀) (deriv γ t₀) (S.T (γ t₀)) with hμdef
  set Y : V := μ • S.T (γ t₀) with hYdef
  set Z : ℝ → V := fun r => Z₀ + (r - t₀) • Y with hZdef
  have hZd : ∀ r, HasDerivAt Z Y r := fun r => by
    rw [hZdef]
    simpa using (((hasDerivAt_id' r).sub_const t₀).smul_const Y).const_add Z₀
  have hZc : Continuous Z := continuous_const.add ((continuous_id.sub continuous_const).smul
    continuous_const)
  -- `h = g(γ',Z)`, its derivative `hd`, and the error term `e`
  set h : ℝ → ℝ := fun r => S.g (γ r) (deriv γ r) (Z r) with hhdef
  set hd : ℝ → ℝ := fun r => S.Dg (γ r) (deriv γ r) (deriv γ r) (Z r)
    + S.g (γ r) (deriv (deriv γ) r) (Z r) + S.g (γ r) (deriv γ r) Y with hhddef
  set e : ℝ → ℝ := fun r => S.Dg (γ r) (Z r) (deriv γ r) (deriv γ r) / 2
    + S.g (γ r) (deriv γ r) Y with hedef
  have hhd : ∀ r, HasDerivAt h (hd r) r := fun r =>
    S.lb_hasDerivAt_g (hgd _) (hγd r) (hγ'd r) (hZd r)
  have hZt₀ : Z t₀ = Z₀ := by simp [hZdef]
  have hh0 : h t₀ = 0 := by simp only [hhdef, hZt₀]; exact hZ₀v
  have hgvY : S.g (γ t₀) (deriv γ t₀) Y = -c₀ / 2 - S.Dg (γ t₀) Z₀ (deriv γ t₀) (deriv γ t₀) / 2 := by
    have hne := hvτ.ne
    rw [hYdef, map_smul, smul_eq_mul, hμdef]; field_simp
  have he0 : e t₀ = -c₀ / 2 := by
    simp only [hedef, hZt₀, hgvY]; ring
  have hd0 : hd t₀ = c₀ / 2 := by
    have hk := S.lb_christoffel_koszul hx₀M (deriv γ t₀) (deriv γ t₀) Z₀
    have hc : c₀ = S.g (γ t₀) (deriv (deriv γ) t₀) Z₀
        + S.g (γ t₀) (S.Γ (γ t₀) (deriv γ t₀) (deriv γ t₀)) Z₀ := by
      rw [hc₀def, acc, map_add, add_apply]
    simp only [hhddef, hZt₀, hgvY]
    rw [hk] at hc
    linarith
  have hdc : Continuous hd :=
    ((S.lb_cont_Dg hg hγc hγ'c hγ'c hZc).add (S.lb_cont_gvw hγc hγ''c hZc)).add
      (S.lb_cont_gvw hγc hγ'c continuous_const)
  have hec : Continuous e :=
    ((S.lb_cont_Dg hg hγc hZc hγ'c hγ'c).div_const 2).add (S.lb_cont_gvw hγc hγ'c continuous_const)
  have hev : ∀ᶠ r in 𝓝 t₀, 0 < hd r ∧ e r < 0 :=
    (hdc.continuousAt.eventually (lt_mem_nhds (by rw [hd0]; linarith))).and
      (hec.continuousAt.eventually (gt_mem_nhds (by rw [he0]; linarith)))
  obtain ⟨ρ, hρ, hball⟩ := Metric.eventually_nhds_iff.1 hev
  set δ := min (ρ / 2) (min ((t₀ - a) / 2) ((b - t₀) / 2)) with hδdef
  have hδ : 0 < δ := lt_min (by positivity) (lt_min (by linarith [ht₀.1]) (by linarith [ht₀.2]))
  have hδρ : δ < ρ := lt_of_le_of_lt (min_le_left _ _) (by linarith)
  have hδa : δ < t₀ - a := lt_of_le_of_lt ((min_le_right _ _).trans (min_le_left _ _))
    (by linarith [ht₀.1])
  have hδb : δ < b - t₀ := lt_of_le_of_lt ((min_le_right _ _).trans (min_le_right _ _))
    (by linarith [ht₀.2])
  set s := t₀ - δ with hsdef
  set t := t₀ + δ with htdef
  have hst : s < t := by linarith
  have hloc : ∀ r ∈ Icc s t, 0 < hd r ∧ e r < 0 := fun r hr => hball (by
    rw [Real.dist_eq]
    exact (abs_le.2 ⟨by linarith [hr.1], by linarith [hr.2]⟩).trans_lt hδρ)
  -- `h` is strictly increasing on `[s,t]`
  have hmono : StrictMonoOn h (Icc s t) :=
    strictMonoOn_of_deriv_pos (convex_Icc s t)
      (fun r _ => (hhd r).continuousAt.continuousWithinAt) fun r hr => by
        rw [interior_Icc] at hr
        rw [(hhd r).deriv]; exact (hloc r (Ioo_subset_Icc_self hr)).1
  -- the variation field `W = φ Z`
  set φ : ℝ → ℝ := fun r => (r - s) * (t - r) with hφdef
  have hφd : ∀ r, HasDerivAt φ ((t - r) - (r - s)) r := fun r => by
    have := ((hasDerivAt_id' r).sub_const s).mul ((hasDerivAt_const r t).sub (hasDerivAt_id' r))
    rw [hφdef]
    convert this using 1; simp only [Pi.sub_apply]; ring
  set W : ℝ → V := fun r => φ r • Z r with hWdef
  have hWd : ∀ r, HasDerivAt W (φ r • Y + ((t - r) - (r - s)) • Z r) r := fun r =>
    (hφd r).smul (hZd r)
  have hWC : ContDiff ℝ 1 W :=
    (((contDiff_id.sub contDiff_const).mul (contDiff_const.sub contDiff_id))).smul
      (contDiff_const.add ((contDiff_id.sub contDiff_const).smul contDiff_const))
  refine ⟨s, t, by linarith, by linarith, by linarith, by linarith, ?_⟩
  refine S.lb_variation_chr hg hγ1 hWC hst (by simp [hWdef, hφdef]) (by simp [hWdef, hφdef])
    (fun r hr => hcaus r ⟨by linarith [hr.1], by linarith [hr.2]⟩) fun r hr => ?_
  rw [(hWd r).deriv]
  have hexp : S.Dg (γ r) (W r) (deriv γ r) (deriv γ r)
      + 2 * S.g (γ r) (deriv γ r) (φ r • Y + ((t - r) - (r - s)) • Z r)
      = 2 * (((t - r) - (r - s)) * h r + φ r * e r) := by
    simp only [hWdef, S.lb_Dg_smul, map_add, map_smul, smul_eq_mul, hhdef, hedef]
    ring
  rw [hexp]
  obtain ⟨-, her⟩ := hloc r hr
  have hφnn : 0 ≤ φ r := mul_nonneg (by linarith [hr.1]) (by linarith [hr.2])
  rcases lt_trichotomy r t₀ with hlt | heq | hgt
  · have hhr : h r < 0 := hh0 ▸ hmono hr ⟨by linarith, by linarith⟩ hlt
    have h1 : 0 < (t - r) - (r - s) := by linarith
    nlinarith [mul_neg_of_pos_of_neg h1 hhr, mul_nonpos_of_nonneg_of_nonpos hφnn her.le]
  · subst heq
    have hφp : 0 < φ r := by simp only [hφdef]; nlinarith
    nlinarith [mul_neg_of_pos_of_neg hφp her]
  · have hhr : 0 < h r := hh0 ▸ hmono ⟨by linarith, by linarith⟩ hr hgt
    have h1 : (t - r) - (r - s) < 0 := by linarith
    nlinarith [mul_neg_of_neg_of_pos h1 hhr, mul_nonpos_of_nonneg_of_nonpos hφnn her.le]

/-- Corollary in the registered form: a `C²` future-**null** curve that is not a pregeodesic
at an interior `t₀` has `γ(s) ≪ γ(t)` for some `s < t`. -/
theorem lb_corner_cutting_null (hg : ContDiff ℝ 1 S.g) {γ : ℝ → V}
    (hγ : ContDiff ℝ 2 γ) {a b t₀ : ℝ} (ht₀ : t₀ ∈ Ioo a b)
    (hnull : ∀ r ∈ Icc a b, γ r ∈ S.M ∧ S.g (γ r) (deriv γ r) (deriv γ r) = 0 ∧
      S.g (γ r) (deriv γ r) (S.T (γ r)) < 0)
    (hnp : ¬ S.IsPregeodesicAt γ t₀) :
    ∃ s t, s < t ∧ S.Chr (γ s) (γ t) := by
  obtain ⟨s, t, -, hs, ht, -, hc⟩ := S.lb_corner_cutting hg hγ ht₀
    (fun r hr => ⟨(hnull r hr).1, (hnull r hr).2.1.le, (hnull r hr).2.2⟩) hnp
  exact ⟨s, t, hs.trans ht, hc⟩

/-! ## ③ Stretch: the tangency clause (first half) -/

/-- The horizon `H = ∂J⁻(J)` is achronal. -/
theorem lb_H_achronal (J : Set V) {p q : V} (hp : p ∈ S.H J) (hq : q ∈ S.H J) :
    ¬ S.Chr p q := by
  intro hpq
  obtain ⟨q', hq'I, hq'J⟩ := mem_closure_iff.1 (frontier_subset_closure hq) (S.Ifut p)
    (S.lb_isOpen_Ifut p) hpq
  obtain ⟨j, hj, hq'j⟩ := mem_iUnion₂.1 hq'J
  have hsub : S.Ipast q' ⊆ S.JpastSet J := fun x hx =>
    mem_iUnion₂.2 ⟨j, hj, Relation.ReflTransGen.trans (S.lb_chr_cau hx) hq'j⟩
  have hint : p ∈ interior (S.JpastSet J) :=
    interior_maximal hsub (S.lb_isOpen_Ipast q') hq'I
  exact hp.2 hint

/-- An achronal `C¹` future-causal curve is null at every interior parameter. -/
theorem lb_achronal_null {γ : ℝ → V} (hγ : ContDiff ℝ 1 γ) {a b t₀ : ℝ} (ht₀ : t₀ ∈ Ioo a b)
    (hcaus : ∀ r ∈ Icc a b, γ r ∈ S.M ∧ S.FutCausal (γ r) (deriv γ r))
    (hach : ∀ s t, a < s → s < t → t < b → ¬ S.Chr (γ s) (γ t)) :
    S.g (γ t₀) (deriv γ t₀) (deriv γ t₀) = 0 := by
  obtain ⟨hM, hle, hT⟩ := hcaus t₀ (Ioo_subset_Icc_self ht₀)
  refine le_antisymm hle (not_lt.1 fun hlt => ?_)
  have hcont : Continuous fun r => (γ r, deriv γ r) :=
    hγ.continuous.prodMk (hγ.continuous_deriv le_rfl)
  have hev : ∀ᶠ r in 𝓝 t₀, γ r ∈ S.M ∧ S.FutTimelike (γ r) (deriv γ r) :=
    hcont.continuousAt.eventually (S.lb_isOpen_timelikePairs.mem_nhds ⟨hM, hlt, hT⟩)
  obtain ⟨ρ, hρ, hball⟩ := Metric.eventually_nhds_iff.1 hev
  set δ := min (ρ / 2) (min ((t₀ - a) / 2) ((b - t₀) / 2)) with hδdef
  have hδ : 0 < δ := lt_min (by positivity) (lt_min (by linarith [ht₀.1]) (by linarith [ht₀.2]))
  have hδρ : δ < ρ := lt_of_le_of_lt (min_le_left _ _) (by linarith)
  have hδa : δ < t₀ - a := lt_of_le_of_lt ((min_le_right _ _).trans (min_le_left _ _))
    (by linarith [ht₀.1])
  have hδb : δ < b - t₀ := lt_of_le_of_lt ((min_le_right _ _).trans (min_le_right _ _))
    (by linarith [ht₀.2])
  have hstep := S.lb_tstep_of_curve hγ (s := t₀ - δ) (t := t₀ + δ) (by linarith) fun r hr =>
    hball (by
      rw [Real.dist_eq]
      exact (abs_le.2 ⟨by linarith [hr.1], by linarith [hr.2]⟩).trans_lt hδρ)
  exact hach _ _ (by linarith) (by linarith) (by linarith) (Relation.TransGen.single hstep)

/-- An achronal `C²` future-causal curve is a pregeodesic at every interior parameter. -/
theorem lb_achronal_pregeodesic (hg : ContDiff ℝ 1 S.g) {γ : ℝ → V}
    (hγ : ContDiff ℝ 2 γ) {a b : ℝ}
    (hcaus : ∀ r ∈ Icc a b, γ r ∈ S.M ∧ S.FutCausal (γ r) (deriv γ r))
    (hach : ∀ s t, a < s → s < t → t < b → ¬ S.Chr (γ s) (γ t)) :
    S.IsPregeodesicOn γ (Ioo a b) := by
  refine S.lb_pregeodesicOn_of_forall fun t₀ ht₀ => not_not.1 fun hnp => ?_
  obtain ⟨s, t, has, hs, ht, htb, hc⟩ := S.lb_corner_cutting hg hγ ht₀ hcaus hnp
  exact hach s t has (hs.trans ht) htb hc

/-- **Tangency clause, first half:** a `C²` future-causal curve lying in the horizon
`H = ∂J⁻(J)` (a `C²` generator) is a null pregeodesic on the open parameter interval. -/
theorem lb_H_generator_null_pregeodesic (hg : ContDiff ℝ 1 S.g)
    (J : Set V) {γ : ℝ → V} (hγ : ContDiff ℝ 2 γ) {a b : ℝ}
    (hcaus : ∀ r ∈ Icc a b, γ r ∈ S.M ∧ S.FutCausal (γ r) (deriv γ r))
    (hH : ∀ r ∈ Icc a b, γ r ∈ S.H J) :
    (∀ t ∈ Ioo a b, S.g (γ t) (deriv γ t) (deriv γ t) = 0) ∧ S.IsPregeodesicOn γ (Ioo a b) := by
  have hach : ∀ s t, a < s → s < t → t < b → ¬ S.Chr (γ s) (γ t) := fun s t has hst htb =>
    S.lb_H_achronal J (hH s ⟨has.le, by linarith⟩) (hH t ⟨by linarith, htb.le⟩)
  exact ⟨fun t ht => S.lb_achronal_null (hγ.of_le (by norm_num)) ht hcaus hach,
    S.lb_achronal_pregeodesic hg hγ hcaus hach⟩


end Spacetime

/-! ## Copied from campaign 61 (`probes/LimitCurves.lean`, `lc_` ↦ `lb_`): the closed future cone
and reverse Cauchy–Schwarz -/

namespace Spacetime
variable (S : Spacetime V)

/-- The closed future cone at `x`: `C x = {v | g_x(v,v) ≤ 0 ∧ g_x(v,T x) ≤ 0}` (contains `0`). -/
def CC (x : V) : Set V := {v | S.g x v v ≤ 0 ∧ S.g x v (S.T x) ≤ 0}

lemma lb_perp_nonneg {x : V} (hx : x ∈ S.M) {u : V} (hu : S.g x u (S.T x) = 0) :
    0 ≤ S.g x u u := by
  by_cases h : u = 0
  · simp [h]
  · exact (S.pos_on_perp x hx u hu h).le

/-- Cauchy–Schwarz for `g_x` on the `g_x`-orthogonal complement of `T x`, where it is positive
semidefinite. -/
lemma lb_cs_perp {x : V} (hx : x ∈ S.M) {u w : V} (hu : S.g x u (S.T x) = 0)
    (hw : S.g x w (S.T x) = 0) : S.g x u w ^ 2 ≤ S.g x u u * S.g x w w := by
  have h : ∀ c : ℝ, 0 ≤ S.g x w w * (c * c) + (2 * S.g x u w) * c + S.g x u u := by
    intro c
    have h1 : S.g x (u + c • w) (S.T x) = 0 := by simp [hu, hw]
    have h2 := S.lb_perp_nonneg hx h1
    have hs := S.symm x w u
    simp only [map_add, map_smul, FunLike.coe_add, Pi.add_apply, FunLike.coe_smul,
      Pi.smul_apply, smul_eq_mul] at h2
    rw [hs] at h2
    linarith
  have := discrim_le_zero h
  unfold discrim at this
  nlinarith [this]

/-- **Reverse Cauchy–Schwarz.** For `u, w` in the closed future cone at `x ∈ M`,
`g_x(u,w) ≤ 0`; strictly if `u ≠ 0` and `w` is timelike. -/
theorem lb_reverse_cs {x : V} (hx : x ∈ S.M) {u w : V} (hu : u ∈ S.CC x) (hw : w ∈ S.CC x) :
    S.g x u w ≤ 0 := by
  obtain ⟨huu, huT⟩ := hu
  obtain ⟨hww, hwT⟩ := hw
  have ht : S.g x (S.T x) (S.T x) < 0 := S.T_timelike x hx
  obtain ⟨t, htd⟩ : ∃ t, S.g x (S.T x) (S.T x) = t := ⟨_, rfl⟩
  rw [htd] at ht
  obtain ⟨a, ha⟩ : ∃ a, S.g x u (S.T x) = a * t :=
    ⟨S.g x u (S.T x) / t, (div_mul_cancel₀ _ ht.ne).symm⟩
  obtain ⟨b, hb⟩ : ∃ b, S.g x w (S.T x) = b * t :=
    ⟨S.g x w (S.T x) / t, (div_mul_cancel₀ _ ht.ne).symm⟩
  have ha0 : 0 ≤ a := by nlinarith
  have hb0 : 0 ≤ b := by nlinarith
  have hTu : S.g x (S.T x) u = a * t := by rw [S.symm, ha]
  have hTw : S.g x (S.T x) w = b * t := by rw [S.symm, hb]
  have hwu : S.g x w u = S.g x u w := S.symm _ _ _
  have hu'T : S.g x (u - a • S.T x) (S.T x) = 0 := by simp [ha, htd]
  have hw'T : S.g x (w - b • S.T x) (S.T x) = 0 := by simp [hb, htd]
  have hu'u' : S.g x (u - a • S.T x) (u - a • S.T x) = S.g x u u - a ^ 2 * t := by
    simp [ha, hTu, htd]; ring
  have hw'w' : S.g x (w - b • S.T x) (w - b • S.T x) = S.g x w w - b ^ 2 * t := by
    simp [hb, hTw, htd]; ring
  have hu'w' : S.g x (u - a • S.T x) (w - b • S.T x) = S.g x u w - a * b * t := by
    simp [ha, hTw, htd]; ring
  have hA := S.lb_perp_nonneg hx hu'T
  have hB := S.lb_perp_nonneg hx hw'T
  have hcs := S.lb_cs_perp hx hu'T hw'T
  rw [hu'u'] at hA
  rw [hw'w'] at hB
  rw [hu'u', hw'w', hu'w'] at hcs
  have hab : 0 ≤ -(a * b * t) := by nlinarith [mul_nonneg ha0 hb0]
  have hAB : (S.g x u u - a ^ 2 * t) * (S.g x w w - b ^ 2 * t) ≤
      (-(a ^ 2 * t)) * (-(b ^ 2 * t)) :=
    mul_le_mul (by linarith) (by linarith) hB (by nlinarith [sq_nonneg a])
  have key : (S.g x u w - a * b * t) ^ 2 ≤ (-(a * b * t)) ^ 2 := by nlinarith
  have := (abs_le_of_sq_le_sq' key hab).2
  linarith

end Spacetime

open MeasureTheory

/-! ## ① The ray lemma -/



/-- `x ↦ x⁻¹` is `1/c²`-Lipschitz on `[c, ∞)`, composed with a Lipschitz function bounded below. -/
theorem lb_inv_lipschitzOn {f : ℝ → ℝ} {s : Set ℝ} {K : ℝ≥0} {c : ℝ} (hc : 0 < c)
    (hf : LipschitzOnWith K f s) (hfc : ∀ r ∈ s, c ≤ f r) :
    LipschitzOnWith (K * Real.toNNReal (1 / c ^ 2)) (fun r => (f r)⁻¹) s := by
  refine LipschitzOnWith.of_dist_le_mul fun x hx y hy => ?_
  have h1 := hf.dist_le_mul x hx y hy
  have hx' := hfc x hx
  have hy' := hfc y hy
  have hxp : 0 < f x := hc.trans_le hx'
  have hyp : 0 < f y := hc.trans_le hy'
  rw [Real.dist_eq, inv_sub_inv hxp.ne' hyp.ne', abs_div, abs_mul, abs_of_pos hxp, abs_of_pos hyp,
    ← Real.dist_eq, dist_comm]
  rw [NNReal.coe_mul, Real.coe_toNNReal _ (by positivity)]
  rw [div_le_iff₀ (by positivity)]
  have hcc : c ^ 2 ≤ f x * f y := by nlinarith
  have hd := dist_nonneg (x := x) (y := y)
  have hK : (0 : ℝ) ≤ K := K.2
  calc dist (f x) (f y) ≤ K * dist x y := h1
    _ = K * (1 / c ^ 2) * dist x y * c ^ 2 := by field_simp
    _ ≤ K * (1 / c ^ 2) * dist x y * (f x * f y) := by gcongr

/-- **The ray lemma, local form.** If `σ` is Lipschitz on `[a,b]`, `ℓ ∘ σ > 0` there for a
continuous functional `ℓ`, and `σ′ = k σ` a.e. on `(a,b)`, then `σ r = (ℓ σ r / ℓ σ b) σ b` on
`[a,b]`: the function `(ℓ ∘ σ)⁻¹ σ` is absolutely continuous with a.e. derivative `0`. -/
theorem lb_ray_local {σ : ℝ → V} {K : ℝ≥0} {a b : ℝ} (hab : a ≤ b)
    (hlip : LipschitzOnWith K σ (Icc a b)) (ℓ : V →L[ℝ] ℝ)
    (hpos : ∀ r ∈ Icc a b, 0 < ℓ (σ r)) {k : ℝ → ℝ}
    (hder : ∀ᵐ t ∂(volume : Measure ℝ), t ∈ Ioo a b → HasDerivAt σ (k t • σ t) t) :
    ∀ r ∈ Icc a b, σ r = (ℓ (σ r) / ℓ (σ b)) • σ b := by
  have hlσ : LipschitzOnWith (‖ℓ‖₊ * K) (fun r => ℓ (σ r)) (Icc a b) :=
    ℓ.lipschitzWith.comp_lipschitzOnWith hlip
  obtain ⟨m, hm, hmin⟩ := isCompact_Icc.exists_isMinOn (nonempty_Icc.2 hab)
    hlσ.continuousOn
  have hc := hpos m hm
  have hf := lb_inv_lipschitzOn hc hlσ fun r hr => hmin hr
  have hu : AbsolutelyContinuousOnInterval (fun r => (ℓ (σ r))⁻¹ • σ r) a b := by
    have h1 := (uIcc_of_le hab).symm ▸ hf
    have h2 := (uIcc_of_le hab).symm ▸ hlip
    exact h1.absolutelyContinuousOnInterval.fun_smul h2.absolutelyContinuousOnInterval
  have hzero : ∀ᵐ t ∂(volume : Measure ℝ), t ∈ uIcc a b →
      HasDerivAt (fun r => (ℓ (σ r))⁻¹ • σ r) 0 t := by
    filter_upwards [hder, Measure.ae_ne volume a, Measure.ae_ne volume b] with t ht hta htb htI
    rw [uIcc_of_le hab] at htI
    have htI' : t ∈ Ioo a b := ⟨lt_of_le_of_ne htI.1 (Ne.symm hta), lt_of_le_of_ne htI.2 htb⟩
    have hd := ht htI'
    have hpt := hpos t htI
    have hl : HasDerivAt (fun r => ℓ (σ r)) (ℓ (k t • σ t)) t := ℓ.hasFDerivAt.comp_hasDerivAt t hd
    have hi := hl.inv hpt.ne'
    have hs := hi.smul hd
    convert hs using 1
    simp only [Pi.inv_apply]
    rw [map_smul, smul_eq_mul, smul_smul, ← add_smul]
    have : (ℓ (σ t))⁻¹ * k t + -(k t * ℓ (σ t)) / ℓ (σ t) ^ 2 = 0 := by
      field_simp; ring
    rw [this, zero_smul]
  obtain ⟨C, hC⟩ := hu.const_of_ae_hasDerivAt_zero hzero
  intro r hr
  have hr' : r ∈ uIcc a b := (uIcc_of_le hab).symm ▸ hr
  have hb' : b ∈ uIcc a b := right_mem_uIcc
  have e := (hC r hr').trans (hC b hb').symm
  have hpr := (hpos r hr).ne'
  have hpb := (hpos b ⟨hab, le_rfl⟩).ne'
  have := congrArg (fun z => ℓ (σ r) • z) e
  simp only [smul_smul, mul_inv_cancel₀ hpr, one_smul] at this
  rw [div_eq_mul_inv]; exact this

/-- **The ray lemma.** Let `σ` be Lipschitz on `[0,1]`, nonvanishing on `(0,1]`, with
`σ′(t) = k(t) σ(t)` for a.e. `t ∈ (0,1)`. Then for every `t ∈ (0,1]`, `σ t = μ σ 1` with `μ > 0`.
No integrability or bound on `k` is assumed. -/
theorem lb_ray_lemma {σ : ℝ → V} {K : ℝ≥0} (hlip : LipschitzOnWith K σ (Icc 0 1))
    (hne : ∀ t ∈ Ioc (0 : ℝ) 1, σ t ≠ 0) {k : ℝ → ℝ}
    (hder : ∀ᵐ t ∂(volume : Measure ℝ), t ∈ Ioo (0 : ℝ) 1 → HasDerivAt σ (k t • σ t) t) :
    ∀ t ∈ Ioc (0 : ℝ) 1, ∃ μ > (0 : ℝ), σ t = μ • σ 1 := by
  have h1 : (1 : ℝ) ∈ Ioc (0 : ℝ) 1 := ⟨one_pos, le_rfl⟩
  obtain ⟨ℓ, -, hℓ⟩ := exists_dual_vector ℝ (σ 1) (norm_ne_zero_iff.2 (hne 1 h1))
  have hℓ1 : 0 < ℓ (σ 1) := by rw [hℓ]; exact norm_pos_iff.2 (hne 1 h1)
  intro t₀ ht₀
  have hsub : ∀ s ∈ Ioc (0 : ℝ) 1, Icc s 1 ⊆ Icc 0 1 := fun s hs => Icc_subset_Icc hs.1.le le_rfl
  have hder' : ∀ s ∈ Ioc (0 : ℝ) 1,
      ∀ᵐ t ∂(volume : Measure ℝ), t ∈ Ioo s 1 → HasDerivAt σ (k t • σ t) t := fun s hs => by
    filter_upwards [hder] with t ht htI using ht ⟨hs.1.trans htI.1, htI.2⟩
  have hcont : ContinuousOn (fun r => ℓ (σ r)) (Icc t₀ 1) :=
    ℓ.continuous.comp_continuousOn (hlip.continuousOn.mono (hsub t₀ ht₀))
  -- positivity of `ℓ ∘ σ` on `[t₀, 1]`
  have hposall : ∀ r ∈ Icc t₀ 1, 0 < ℓ (σ r) := by
    by_contra hcon
    push Not at hcon
    set A := Icc t₀ 1 ∩ (fun r => ℓ (σ r)) ⁻¹' Iic 0 with hA
    have hAc : IsClosed A := hcont.preimage_isClosed_of_isClosed isClosed_Icc isClosed_Iic
    obtain ⟨r₀, hr₀, hr₀'⟩ := hcon
    have hAne : A.Nonempty := ⟨r₀, hr₀, hr₀'⟩
    have hAb : BddAbove A := ⟨1, fun r hr => hr.1.2⟩
    set s := sSup A with hs
    have hsA : s ∈ A := hAc.csSup_mem hAne hAb
    have hs1 : s < 1 := by
      refine lt_of_le_of_ne hsA.1.2 fun h => ?_
      have := hsA.2; rw [h] at this; exact absurd (this : ℓ (σ 1) ≤ 0) (not_le.2 hℓ1)
    have hst₀ : t₀ ≤ s := hsA.1.1
    have hposr : ∀ r ∈ Ioc s 1, 0 < ℓ (σ r) := fun r hr => by
      by_contra h
      have : r ∈ A := ⟨⟨hst₀.trans hr.1.le, hr.2⟩, not_lt.1 h⟩
      exact absurd (le_csSup hAb this) (not_le.2 hr.1)
    have hray : ∀ r ∈ Ioc s 1, σ r = (ℓ (σ r) / ℓ (σ 1)) • σ 1 := fun r hr => by
      have hr0 : r ∈ Ioc (0 : ℝ) 1 := ⟨ht₀.1.trans_le (hst₀.trans hr.1.le), hr.2⟩
      exact lb_ray_local hr.2 (hlip.mono (hsub r hr0)) ℓ
        (fun q hq => hposr q ⟨hr.1.trans_le hq.1, hq.2⟩) (hder' r hr0) r ⟨le_rfl, hr.2⟩
    have hcl : s ∈ closure (Ioc s 1) := by rw [closure_Ioc hs1.ne]; exact ⟨le_rfl, hs1.le⟩
    have hIoc : Ioc s 1 ⊆ Icc t₀ 1 := fun r hr => ⟨hst₀.trans hr.1.le, hr.2⟩
    -- `ℓ σ s ≥ 0`
    have hY : IsClosed (Icc t₀ 1 ∩ (fun r => ℓ (σ r)) ⁻¹' Ici 0) :=
      hcont.preimage_isClosed_of_isClosed isClosed_Icc isClosed_Ici
    have hsY := hY.closure_subset_iff.2 (fun r hr => ⟨hIoc hr, (hposr r hr).le⟩) hcl
    have hℓs : ℓ (σ s) = 0 := le_antisymm hsA.2 hsY.2
    -- `σ s` is on the ray
    have hFc : ContinuousOn (fun r => σ r - (ℓ (σ r) / ℓ (σ 1)) • σ 1) (Icc t₀ 1) :=
      (hlip.continuousOn.mono (hsub t₀ ht₀)).sub ((hcont.div_const _).smul continuousOn_const)
    have hZ : IsClosed (Icc t₀ 1 ∩ (fun r => σ r - (ℓ (σ r) / ℓ (σ 1)) • σ 1) ⁻¹' {0}) :=
      hFc.preimage_isClosed_of_isClosed isClosed_Icc isClosed_singleton
    have hsZ := hZ.closure_subset_iff.2 (fun r hr => ⟨hIoc hr, by
      simp only [mem_preimage, mem_singleton_iff]; rw [← hray r hr, sub_self]⟩) hcl
    have hσs : σ s = 0 := by
      have := hsZ.2
      simp only [mem_preimage, mem_singleton_iff, hℓs, zero_div, zero_smul, sub_zero] at this
      exact this
    exact hne s ⟨ht₀.1.trans_le hst₀, hs1.le⟩ hσs
  refine ⟨ℓ (σ t₀) / ℓ (σ 1), div_pos (hposall t₀ ⟨le_rfl, ht₀.2⟩) hℓ1, ?_⟩
  exact lb_ray_local ht₀.2 (hlip.mono (hsub t₀ ht₀)) ℓ hposall (hder' t₀ ht₀) t₀ ⟨le_rfl, ht₀.2⟩


/-! ## The cutoff reparametrisation used to extend radial geodesics to `C²` curves on `ℝ` -/

/-- A bump at `1/2`, equal to `1` on `[-1/4, 5/4]` and `0` off `(-1/2, 3/2)`. -/
noncomputable def lbBump : ContDiffBump (1 / 2 : ℝ) := ⟨3 / 4, 1, by norm_num, by norm_num⟩

/-- `ψ t = 1/2 + (t − 1/2) χ(t)`: the identity near `[0,1]`, with values in `[-1/2, 3/2]`. -/
noncomputable def lbψ (t : ℝ) : ℝ := 1 / 2 + (t - 1 / 2) * lbBump t

theorem lb_psi_contDiff : ContDiff ℝ 2 lbψ :=
  contDiff_const.add ((contDiff_id.sub contDiff_const).mul lbBump.contDiff)

theorem lb_psi_bound (t : ℝ) : lbψ t ∈ Icc (-1 / 2 : ℝ) (3 / 2) := by
  have hb0 : 0 ≤ lbBump t := lbBump.nonneg
  have hb1 : lbBump t ≤ 1 := lbBump.le_one
  by_cases h : |t - 1 / 2| < 1
  · have h' := abs_lt.1 h
    unfold lbψ
    constructor <;> nlinarith [h'.1, h'.2]
  · have h0 : lbBump t = 0 := lbBump.zero_of_le_dist (by
      rw [Real.dist_eq]; exact not_lt.1 h)
    unfold lbψ; rw [h0]; constructor <;> norm_num

theorem lb_psi_id {t : ℝ} (ht : t ∈ Icc (0 : ℝ) 1) : lbψ =ᶠ[𝓝 t] id := by
  have hb : t ∈ ball (1 / 2 : ℝ) lbBump.rIn := by
    rw [mem_ball, Real.dist_eq, abs_lt]
    show _ ∧ _
    constructor <;> linarith [ht.1, ht.2, (show lbBump.rIn = 3 / 4 from rfl)]
  filter_upwards [lbBump.eventuallyEq_one_of_mem_ball hb] with s hs
  simp only [lbψ, id]; rw [hs, Pi.one_apply]; ring

theorem lb_psi_eq {t : ℝ} (ht : t ∈ Icc (0 : ℝ) 1) : lbψ t = t := (lb_psi_id ht).self_of_nhds

/-! ## ② Monotonicity of `Q`, ③ generators as null geodesics -/

namespace Spacetime

namespace GeoFlow

variable {S : Spacetime V} {p : V} (G : S.GeoFlow p)

/-- Flow trajectories are `C²` on the open time interval (the cut-off spray is `C¹`). -/
theorem lb_traj_contDiffOn (hg : ContDiff ℝ 2 S.g) {y : V × V}
    (hy : y ∈ closedBall ((p, 0) : V × V) G.D.r) :
    ContDiffOn ℝ 2 (G.D.α y) (Ioo (-G.D.τ) G.D.τ) := by
  have hF := G.lb_hf hg
  have hd : ∀ t ∈ Ioo (-G.D.τ) G.D.τ,
      HasDerivAt (G.D.α y) (S.cutField G.χ (G.D.α y t)) t := fun t ht =>
    (G.D.deriv y hy t (Ioo_subset_Icc_self ht)).hasDerivAt (Icc_mem_nhds ht.1 ht.2)
  have hdiff : DifferentiableOn ℝ (G.D.α y) (Ioo (-G.D.τ) G.D.τ) := fun t ht =>
    (hd t ht).differentiableAt.differentiableWithinAt
  have hderiv : EqOn (deriv (G.D.α y)) (fun t => S.cutField G.χ (G.D.α y t))
      (Ioo (-G.D.τ) G.D.τ) := fun t ht => (hd t ht).deriv
  have hC1 : ContDiffOn ℝ 1 (G.D.α y) (Ioo (-G.D.τ) G.D.τ) := by
    rw [show (1 : WithTop ℕ∞) = 0 + 1 by norm_num, contDiffOn_succ_iff_deriv_of_isOpen isOpen_Ioo]
    refine ⟨hdiff, by simp, ?_⟩
    exact (contDiffOn_zero.2 (hF.continuous.comp_continuousOn hdiff.continuousOn)).congr hderiv
  rw [show (2 : WithTop ℕ∞) = 1 + 1 by norm_num, contDiffOn_succ_iff_deriv_of_isOpen isOpen_Ioo]
  refine ⟨hdiff, by simp, ?_⟩
  exact (hF.comp_contDiffOn hC1).congr hderiv

/-- The radial geodesic through `v`, extended to a `C²` curve on `ℝ` through `lbψ`. -/
noncomputable def radC2 (v : V) (t : ℝ) : V := (G.D.α (p, G.c • v) (lbψ t * G.s₀)).1

theorem lb_psi_mem (t : ℝ) : lbψ t * G.s₀ ∈ Ioo (-G.D.τ) G.D.τ := by
  have h := lb_psi_bound t
  have hτ := G.D.τ_pos
  have hs : G.s₀ = G.D.τ / 2 := rfl
  rw [hs]; constructor <;> nlinarith [h.1, h.2]

/-- **The radial geodesic is `C²`.** -/
theorem lb_radC2_contDiff (hg : ContDiff ℝ 2 S.g) {v : V} (hv : v ∈ ball (0 : V) G.ρ) :
    ContDiff ℝ 2 (G.radC2 v) := by
  have h1 := contDiff_fst.comp_contDiffOn
    (G.lb_traj_contDiffOn hg (G.lb_mem_r (G.lb_dom_closed hv)))
  exact h1.comp_contDiff (lb_psi_contDiff.mul contDiff_const) G.lb_psi_mem

theorem lb_radC2_eq (hg : ContDiff ℝ 2 S.g) {v : V} (hv : v ∈ ball (0 : V) G.ρ) {r : ℝ}
    (hr : r ∈ Icc (0 : ℝ) 1) : G.radC2 v r = G.expp (r • v) := by
  rw [radC2, lb_psi_eq hr, G.lb_expp_smul hg hv hr]

theorem lb_radC2_deriv (hg : ContDiff ℝ 2 S.g) {v : V} (hv : v ∈ ball (0 : V) G.ρ) {r : ℝ}
    (hr : r ∈ Icc (0 : ℝ) 1) :
    HasDerivAt (G.radC2 v) (G.s₀ • (G.D.α (p, G.c • v) (r * G.s₀)).2) r := by
  have hy := G.lb_dom_closed hv
  have hrs : r * G.s₀ ∈ Ioo (-G.D.τ) G.D.τ := by
    have := G.lb_psi_mem r; rwa [lb_psi_eq hr] at this
  have hα : HasDerivAt (G.D.α (p, G.c • v)) (S.cutField G.χ (G.D.α (p, G.c • v) (r * G.s₀)))
      (r * G.s₀) :=
    (G.D.deriv _ (G.lb_mem_r hy) _ (Ioo_subset_Icc_self hrs)).hasDerivAt
      (Icc_mem_nhds hrs.1 hrs.2)
  have hlin : HasDerivAt (fun t : ℝ => t * G.s₀) G.s₀ r := by
    simpa using (hasDerivAt_id r).mul_const G.s₀
  have h2 := (ContinuousLinearMap.fst ℝ V V).hasFDerivAt.comp_hasDerivAt r (hα.scomp r hlin)
  have heq : G.radC2 v =ᶠ[𝓝 r] fun t => (G.D.α (p, G.c • v) (t * G.s₀)).1 := by
    filter_upwards [lb_psi_id hr] with t ht
    simp only [radC2, ht, id]
  refine (h2.congr_of_eventuallyEq heq).congr_deriv ?_
  have hin := G.lb_traj_in hg hy (Ioo_subset_Icc_self hrs)
  rw [S.lb_cutField_eq G.χ (ball_subset_closedBall hin)]
  simp [geoField]

/-- **The radial geodesic is future null.** If `v` is future-directed and null at `p`, the `C²`
radial geodesic is in `M` and future null on `[0,1]`. The time orientation cannot flip: a zero
of `g(β′, T)` would make the null `β′` vanish, and then the Gauss lemma (flow form) and
nondegeneracy at `p` force `v = 0`. -/
theorem lb_radC2_futNull (hg : ContDiff ℝ 2 S.g) {v : V} (hv : v ∈ ball (0 : V) G.ρ)
    (hnull : S.g p v v = 0) (hfut : S.g p v (S.T p) < 0) :
    ∀ r ∈ Icc (0 : ℝ) 1, G.radC2 v r ∈ S.M ∧ S.FutCausal (G.radC2 v r) (deriv (G.radC2 v) r) ∧
      S.g (G.radC2 v r) (deriv (G.radC2 v) r) (deriv (G.radC2 v) r) = 0 := by
  have hy := G.lb_dom_closed hv
  have hpos : ∀ r ∈ Icc (0 : ℝ) 1, G.radC2 v r = (G.D.α (p, G.c • v) (r * G.s₀)).1 := fun r hr => by
    rw [radC2, lb_psi_eq hr]
  have hder : ∀ r ∈ Icc (0 : ℝ) 1,
      deriv (G.radC2 v) r = G.s₀ • (G.D.α (p, G.c • v) (r * G.s₀)).2 := fun r hr =>
    (G.lb_radC2_deriv hg hv hr).deriv
  have hM : ∀ r ∈ Icc (0 : ℝ) 1, G.radC2 v r ∈ S.M := fun r hr => by
    rw [hpos r hr]; exact G.lb_ball_sub_M (G.lb_traj_in hg hy (G.lb_mul_s₀_mem hr))
  have hN : ∀ r ∈ Icc (0 : ℝ) 1,
      S.g (G.radC2 v r) (deriv (G.radC2 v) r) (deriv (G.radC2 v) r) = 0 := fun r hr => by
    rw [hpos r hr, hder r hr]
    have hE := G.lb_energy_cons hg hy (G.lb_mul_s₀_mem hr)
    simp only [map_smul, FunLike.coe_smul, Pi.smul_apply, smul_eq_mul] at hE ⊢
    rw [hE, hnull]; ring
  have hβ := G.lb_radC2_contDiff hg hv
  let h : ℝ → ℝ := fun t => S.g (G.radC2 v t) (deriv (G.radC2 v) t) (S.T (G.radC2 v t))
  have hhc : Continuous h :=
    ((S.cont_g.comp hβ.continuous).clm_apply (hβ.continuous_deriv (by norm_num))).clm_apply
      (S.cont_T.comp hβ.continuous)
  have h0mem : (0 : ℝ) ∈ Icc (0 : ℝ) 1 := ⟨le_rfl, zero_le_one⟩
  have hh0 : h 0 < 0 := by
    have e1 : G.radC2 v 0 = p := by
      rw [hpos 0 h0mem, zero_mul, G.D.init _ (G.lb_mem_r hy)]
    have e2 : deriv (G.radC2 v) 0 = v := by
      rw [hder 0 h0mem, zero_mul, G.D.init _ (G.lb_mem_r hy)]
      simp only [smul_smul, mul_comm G.s₀ G.c, G.lb_c_s₀, one_smul]
    simp only [h, e1, e2]; exact hfut
  have hpM : p ∈ S.M := G.lb_ball_sub_M (mem_ball_self G.χ.rIn_pos)
  have hne : ∀ t ∈ Icc (0 : ℝ) 1, h t ≠ 0 := fun t ht h0 => by
    have hd0 : deriv (G.radC2 v) t = 0 := by
      by_contra hd0
      have := S.pos_on_perp _ (hM t ht) _ h0 hd0
      rw [hN t ht] at this; exact lt_irrefl _ this
    have ht0 : t ≠ 0 := fun e => by rw [e] at h0; exact hh0.ne h0
    have hu0 : (G.D.α (p, G.c • v) (t * G.s₀)).2 = 0 := by
      rw [hder t ht] at hd0
      exact (smul_eq_zero.1 hd0).resolve_left G.lb_s₀_pos.ne'
    have hz : G.c • v = 0 := S.lb_nondegenerate hpM fun b => by
      have := G.lb_gauss_flow hg (G.lb_dom hv) b (G.lb_mul_s₀_mem ht)
      rw [hu0] at this
      simp only [map_zero, zero_apply] at this
      have hts : t * G.s₀ ≠ 0 := mul_ne_zero ht0 G.lb_s₀_pos.ne'
      exact (mul_eq_zero.1 this.symm).resolve_left hts
    have hv0 : v = 0 := (smul_eq_zero.1 hz).resolve_left G.lb_c_pos.ne'
    rw [hv0] at hfut; simp at hfut
  have hfutr : ∀ t ∈ Icc (0 : ℝ) 1, h t < 0 := by
    intro t ht
    by_contra hcon
    rw [not_lt] at hcon
    obtain ⟨s, hs, hs0⟩ := intermediate_value_Icc ht.1 hhc.continuousOn ⟨hh0.le, hcon⟩
    exact hne s ⟨hs.1, hs.2.trans ht.2⟩ hs0
  exact fun r hr => ⟨hM r hr, ⟨(hN r hr).le, hfutr r hr⟩, hN r hr⟩

namespace NormalChart

variable {G} (N : G.NormalChart)

theorem lb_good_isOpen : IsOpen N.good := by
  rw [isOpen_iff_mem_nhds]
  intro x hx
  filter_upwards [N.Φ.open_target.mem_nhds hx.1, hx.2.eventually (by simp)] with y h1 h2
  exact ⟨h1, h2⟩

theorem lb_symm_p : N.Φ.symm p = 0 := by
  have := N.Φ.left_inv N.zero_mem; rwa [N.map_zero] at this

theorem lb_Q_p : N.Q p = 0 := by simp [Q, N.lb_symm_p]

theorem lb_eq_p_of_symm {x : V} (hx : x ∈ N.good) (h : N.Φ.symm x = 0) : x = p := by
  rw [← N.Φ.right_inv hx.1, h, N.map_zero]

theorem lb_good_eq_expp {x : V} (hx : x ∈ N.good) : x = G.expp (N.Φ.symm x) :=
  (N.lb_good_expp hx).symm

/-- A closed ball around `p` inside the good set: the normal neighbourhood `U`. -/
theorem lb_exists_ball : ∃ R > (0 : ℝ), closedBall p R ⊆ N.good := by
  obtain ⟨ε, hε, h⟩ := Metric.mem_nhds_iff.1 N.lb_good_nhds
  exact ⟨ε / 2, by positivity, (closedBall_subset_ball (by linarith)).trans h⟩

theorem lb_Q_contDiffAt {x : V} (hx : x ∈ N.good) : ContDiffAt ℝ 1 N.Q x := by
  have h : ContDiff ℝ 1 (fun w : V => S.g p w w) :=
    (contDiff_const.clm_apply contDiff_id).clm_apply contDiff_id
  exact h.contDiffAt.comp x hx.2

theorem lb_Q_lipschitzOn {R : ℝ} (hB : closedBall p R ⊆ N.good) :
    ∃ K, LipschitzOnWith K N.Q (closedBall p R) :=
  ContDiffOn.exists_lipschitzOnWith (fun x hx => (N.lb_Q_contDiffAt (hB hx)).contDiffWithinAt)
    one_ne_zero (convex_closedBall p R) (isCompact_closedBall p R)

theorem lb_symm_lipschitzOn {R : ℝ} (hB : closedBall p R ⊆ N.good) :
    ∃ K, LipschitzOnWith K N.Φ.symm (closedBall p R) :=
  ContDiffOn.exists_lipschitzOnWith (fun x hx => (hB hx).2.contDiffWithinAt)
    one_ne_zero (convex_closedBall p R) (isCompact_closedBall p R)

/-- `(Q ∘ γ)′ = 2 g(P, γ′)` at differentiability points (`lb_grad_Q` and the chain rule). -/
theorem lb_Q_comp_hasDerivAt (hg : ContDiff ℝ 2 S.g) {γ : ℝ → V} {t : ℝ} {w : V}
    (hγ : HasDerivAt γ w t) (hx : γ t ∈ N.good) :
    HasDerivAt (fun s => N.Q (γ s)) (2 * S.g (γ t) (N.P (γ t)) w) t := by
  have h := (N.lb_grad_Q hg hx).comp_hasDerivAt t hγ
  have e : ((2 : ℝ) • S.g (γ t) (N.P (γ t))) w = 2 * S.g (γ t) (N.P (γ t)) w := by simp
  rw [e] at h; exact h

/-- **② Monotonicity of `Q`, analytic core.** Along a Lipschitz curve in the normal
neighbourhood `closedBall p R ⊆ good`, if `g(P, γ′) ≤ 0` a.e., then `Q ∘ γ` is non-increasing
on `[0,1]`. (`Q ∘ γ` is Lipschitz, hence absolutely continuous; FTC for absolutely continuous
functions.) -/
theorem lb_Q_antitone (hg : ContDiff ℝ 2 S.g) {γ : ℝ → V} {K : ℝ≥0} {R : ℝ}
    (hB : closedBall p R ⊆ N.good) (hlip : LipschitzOnWith K γ (Icc 0 1))
    (hmem : ∀ t ∈ Icc (0 : ℝ) 1, γ t ∈ closedBall p R)
    (hsign : ∀ᵐ t ∂(volume : Measure ℝ), t ∈ Ioo (0 : ℝ) 1 → DifferentiableAt ℝ γ t →
      S.g (γ t) (N.P (γ t)) (deriv γ t) ≤ 0) :
    AntitoneOn (fun t => N.Q (γ t)) (Icc 0 1) := by
  obtain ⟨KQ, hKQ⟩ := N.lb_Q_lipschitzOn hB
  have hQγ : LipschitzOnWith (KQ * K) (fun t => N.Q (γ t)) (Icc 0 1) :=
    hKQ.comp hlip (fun t ht => hmem t ht)
  intro s hs t ht hst
  have hsub : Icc s t ⊆ Icc 0 1 := Icc_subset_Icc hs.1 ht.2
  have hac : AbsolutelyContinuousOnInterval (fun t => N.Q (γ t)) s t := by
    have h := hQγ.mono hsub
    rw [← uIcc_of_le hst] at h
    exact h.absolutelyContinuousOnInterval
  have hint := hac.integral_deriv_eq_sub
  have hnn : 0 ≤ ∫ x in s..t, -deriv (fun t => N.Q (γ t)) x := by
    apply intervalIntegral.integral_nonneg_of_ae_restrict hst
    rw [Filter.EventuallyLE, ae_restrict_iff' measurableSet_Icc]
    filter_upwards [hsign, hlip.ae_differentiableWithinAt_of_mem (μ := volume),
      Measure.ae_ne volume s, Measure.ae_ne volume t] with x hx1 hx2 hxs hxt hxI
    have hxI' : x ∈ Ioo s t := ⟨lt_of_le_of_ne hxI.1 (Ne.symm hxs), lt_of_le_of_ne hxI.2 hxt⟩
    have hx01 : x ∈ Ioo (0 : ℝ) 1 := ⟨hs.1.trans_lt hxI'.1, hxI'.2.trans_le ht.2⟩
    have hd : DifferentiableAt ℝ γ x :=
      (hx2 (Ioo_subset_Icc_self hx01)).differentiableAt (Icc_mem_nhds hx01.1 hx01.2)
    have hQd := N.lb_Q_comp_hasDerivAt hg hd.hasDerivAt (hB (hmem x (Ioo_subset_Icc_self hx01)))
    simp only [Pi.zero_apply]
    rw [hQd.deriv]
    nlinarith [hx1 hx01 hd]
  rw [intervalIntegral.integral_neg, hint] at hnn
  linarith

/-- **② Monotonicity of `Q`, conditional on the bootstrap.** A Lipschitz curve from `p` in the
normal neighbourhood, with velocity a.e. in the closed future cone, along which the position field
`P` stays in the closed future cone, has `Q ∘ γ` non-increasing, hence `Q ≤ 0` along it: such
points of `J⁺(p) ∩ U` lie in `{Q ≤ 0}`. (Reverse Cauchy–Schwarz gives `g(P, γ′) ≤ 0`.) -/
theorem lb_Q_mono_of_cone (hg : ContDiff ℝ 2 S.g) {γ : ℝ → V} {K : ℝ≥0} {R : ℝ}
    (hB : closedBall p R ⊆ N.good) (hlip : LipschitzOnWith K γ (Icc 0 1))
    (hmem : ∀ t ∈ Icc (0 : ℝ) 1, γ t ∈ closedBall p R) (h0 : γ 0 = p)
    (hcausal : ∀ᵐ t ∂(volume : Measure ℝ), t ∈ Ioo (0 : ℝ) 1 → DifferentiableAt ℝ γ t →
      deriv γ t ∈ S.CC (γ t))
    (hboot : ∀ t ∈ Ioo (0 : ℝ) 1, N.P (γ t) ∈ S.CC (γ t)) :
    AntitoneOn (fun t => N.Q (γ t)) (Icc 0 1) ∧ ∀ t ∈ Icc (0 : ℝ) 1, N.Q (γ t) ≤ 0 := by
  have hanti := N.lb_Q_antitone hg hB hlip hmem (by
    filter_upwards [hcausal] with t ht htI hd
    exact S.lb_reverse_cs (N.lb_good_mem_M hg (hB (hmem t (Ioo_subset_Icc_self htI))))
      (hboot t htI) (ht htI hd))
  refine ⟨hanti, fun t ht => ?_⟩
  have := hanti ⟨le_rfl, zero_le_one⟩ ht ht.1
  simp only [h0, N.lb_Q_p] at this
  exact this

/-- `P` is in the closed future cone iff `Q ≤ 0` and `g(P, T) ≤ 0`: the bootstrap is exactly the
statement that the curve stays inside the (closed) future conoid. -/
theorem lb_P_mem_CC_iff (hg : ContDiff ℝ 2 S.g) {x : V} (hx : x ∈ N.good) :
    N.P x ∈ S.CC x ↔ N.Q x ≤ 0 ∧ S.g x (N.P x) (S.T x) ≤ 0 := by
  rw [Spacetime.CC, mem_setOf_eq, N.lb_P_energy hg hx]

/-- **③ (a) Curves in the null conoid are radial.** A Lipschitz curve in the normal neighbourhood
that stays in `{Q = 0}`, avoids `p` on `(0,1]`, and has causal velocity a.e., lies on one radial
null ray of `exp_p`: `exp_p⁻¹ γ(t) = μ exp_p⁻¹ γ(1)` with `μ > 0`. (`lb_ae_null_tangent` gives
`γ′ ∥ P` a.e.; by `lb_P_euler`, `σ = exp_p⁻¹ ∘ γ` then has `σ′ = k σ` a.e.; then the ray lemma.) -/
theorem lb_generator_ray (hg : ContDiff ℝ 2 S.g) {γ : ℝ → V} {K : ℝ≥0} {R : ℝ}
    (hB : closedBall p R ⊆ N.good) (hlip : LipschitzOnWith K γ (Icc 0 1))
    (hmem : ∀ t ∈ Icc (0 : ℝ) 1, γ t ∈ closedBall p R)
    (hQ : ∀ t ∈ Icc (0 : ℝ) 1, N.Q (γ t) = 0) (hne : ∀ t ∈ Ioc (0 : ℝ) 1, γ t ≠ p)
    (hc : ∀ᵐ t ∂(volume : Measure ℝ), t ∈ Ioo (0 : ℝ) 1 →
      DifferentiableAt ℝ γ t → S.g (γ t) (deriv γ t) (deriv γ t) ≤ 0) :
    S.g p (N.Φ.symm (γ 1)) (N.Φ.symm (γ 1)) = 0 ∧
    ∀ t ∈ Ioc (0 : ℝ) 1, ∃ μ > (0 : ℝ), N.Φ.symm (γ t) = μ • N.Φ.symm (γ 1) ∧
      γ t = G.expp (μ • N.Φ.symm (γ 1)) := by
  classical
  have hgood : ∀ t ∈ Icc (0 : ℝ) 1, γ t ∈ N.good := fun t ht => hB (hmem t ht)
  obtain ⟨Ks, hKs⟩ := N.lb_symm_lipschitzOn hB
  have hσ : LipschitzOnWith (Ks * K) (fun t => N.Φ.symm (γ t)) (Icc 0 1) :=
    hKs.comp hlip (fun t ht => hmem t ht)
  have hσne : ∀ t ∈ Ioc (0 : ℝ) 1, N.Φ.symm (γ t) ≠ 0 := fun t ht h =>
    hne t ht (N.lb_eq_p_of_symm (hgood t ⟨ht.1.le, ht.2⟩) h)
  have htan := N.lb_ae_null_tangent hg hlip hQ
    (fun s hs => ⟨hgood s (Ioo_subset_Icc_self hs), hne s ⟨hs.1, hs.2.le⟩⟩) hc
  let k : ℝ → ℝ := fun t => if h : ∃ k : ℝ, deriv γ t = k • N.P (γ t) then h.choose else 0
  have hder : ∀ᵐ t ∂(volume : Measure ℝ), t ∈ Ioo (0 : ℝ) 1 →
      HasDerivAt (fun t => N.Φ.symm (γ t)) (k t • N.Φ.symm (γ t)) t := by
    filter_upwards [htan, hlip.ae_differentiableWithinAt_of_mem (μ := volume)] with t h1 h2 htI
    have hd : DifferentiableAt ℝ γ t :=
      (h2 (Ioo_subset_Icc_self htI)).differentiableAt (Icc_mem_nhds htI.1 htI.2)
    have hk := h1 htI
    have hkt : deriv γ t = k t • N.P (γ t) := by
      simp only [k, dif_pos hk]; exact hk.choose_spec
    have hx := hgood t (Ioo_subset_Icc_self htI)
    have hc := ((hx.2.differentiableAt one_ne_zero).hasFDerivAt).comp_hasDerivAt t hd.hasDerivAt
    rw [hkt, map_smul, N.lb_P_euler hg hx] at hc
    exact hc
  have hray := lb_ray_lemma hσ hσne hder
  refine ⟨hQ 1 ⟨zero_le_one, le_rfl⟩, fun t ht => ?_⟩
  obtain ⟨μ, hμ, he⟩ := hray t ht
  refine ⟨μ, hμ, he, ?_⟩
  rw [← he]
  exact N.lb_good_eq_expp (hgood t ⟨ht.1.le, ht.2⟩)

/-- **③ Generators are null geodesics.** A Lipschitz curve from `p` in the normal neighbourhood,
inside the null conoid `{Q = 0}`, avoiding `p` on `(0,1]`, with causal velocity a.e., and with
future-directed endpoint direction, is a monotone-free reparametrisation of one `C²` radial null
geodesic `β = radC2 v` on `[0,1]` (`γ([0,1]) = β([0,1])`). If moreover it lies in the horizon
`H = ∂J⁻(J)`, campaign 70's `lb_H_generator_null_pregeodesic` applies to `β`: `β` is null and a
pregeodesic on `(0,1)`. -/
theorem lb_generator_null_geodesic (hg : ContDiff ℝ 2 S.g) {γ : ℝ → V} {K : ℝ≥0} {R : ℝ}
    (hB : closedBall p R ⊆ N.good) (hlip : LipschitzOnWith K γ (Icc 0 1))
    (hmem : ∀ t ∈ Icc (0 : ℝ) 1, γ t ∈ closedBall p R) (h0 : γ 0 = p)
    (hQ : ∀ t ∈ Icc (0 : ℝ) 1, N.Q (γ t) = 0) (hne : ∀ t ∈ Ioc (0 : ℝ) 1, γ t ≠ p)
    (hc : ∀ᵐ t ∂(volume : Measure ℝ), t ∈ Ioo (0 : ℝ) 1 →
      DifferentiableAt ℝ γ t → S.g (γ t) (deriv γ t) (deriv γ t) ≤ 0)
    (hfut : S.g p (N.Φ.symm (γ 1)) (S.T p) < 0) :
    ∃ v ∈ ball (0 : V) G.ρ, S.g p v v = 0 ∧ S.g p v (S.T p) < 0 ∧ ContDiff ℝ 2 (G.radC2 v) ∧
      (∀ t ∈ Icc (0 : ℝ) 1, ∃ r ∈ Icc (0 : ℝ) 1, γ t = G.radC2 v r) ∧
      (∀ r ∈ Icc (0 : ℝ) 1, ∃ t ∈ Icc (0 : ℝ) 1, G.radC2 v r = γ t) ∧
      (∀ r ∈ Icc (0 : ℝ) 1, G.radC2 v r ∈ S.M ∧
        S.FutCausal (G.radC2 v r) (deriv (G.radC2 v) r) ∧
        S.g (G.radC2 v r) (deriv (G.radC2 v) r) (deriv (G.radC2 v) r) = 0) := by
  obtain ⟨hnull1, hray⟩ := N.lb_generator_ray hg hB hlip hmem hQ hne hc
  have hgood : ∀ t ∈ Icc (0 : ℝ) 1, γ t ∈ N.good := fun t ht => hB (hmem t ht)
  set σ : ℝ → V := fun t => N.Φ.symm (γ t) with hσdef
  set v₁ := σ 1 with hv₁
  have h1 : (1 : ℝ) ∈ Ioc (0 : ℝ) 1 := ⟨one_pos, le_rfl⟩
  have hv₁0 : v₁ ≠ 0 := fun h =>
    hne 1 h1 (N.lb_eq_p_of_symm (hgood 1 ⟨zero_le_one, le_rfl⟩) h)
  obtain ⟨ℓ, -, hℓ⟩ := exists_dual_vector ℝ v₁ (norm_ne_zero_iff.2 hv₁0)
  have hℓ1 : 0 < ℓ v₁ := by rw [hℓ]; exact norm_pos_iff.2 hv₁0
  set μ : ℝ → ℝ := fun t => ℓ (σ t) / ℓ v₁ with hμdef
  have hσμ : ∀ t ∈ Icc (0 : ℝ) 1, σ t = μ t • v₁ := by
    intro t ht
    rcases ht.1.eq_or_lt with e | hlt
    · subst e
      simp [hσdef, hμdef, h0, N.lb_symm_p]
    · obtain ⟨m, -, hm, -⟩ := hray t ⟨hlt, ht.2⟩
      have : ℓ (σ t) = m * ℓ v₁ := by
        simp only [hσdef]; rw [hm, map_smul, smul_eq_mul]
      simp only [hμdef, this, mul_div_assoc, div_self hℓ1.ne', mul_one]
      exact hm
  have hμnn : ∀ t ∈ Icc (0 : ℝ) 1, 0 ≤ μ t := by
    intro t ht
    rcases ht.1.eq_or_lt with e | hlt
    · subst e; simp [hμdef, hσdef, h0, N.lb_symm_p]
    · obtain ⟨m, hm0, hm, -⟩ := hray t ⟨hlt, ht.2⟩
      have hmt : μ t = m := by
        simp only [hμdef, hσdef]; rw [hm, map_smul, smul_eq_mul, mul_div_assoc,
          div_self hℓ1.ne', mul_one]
      rw [hmt]; exact hm0.le
  obtain ⟨Ks, hKs⟩ := N.lb_symm_lipschitzOn hB
  have hσc : ContinuousOn σ (Icc 0 1) := (hKs.comp hlip (fun t ht => hmem t ht)).continuousOn
  have hμc : ContinuousOn μ (Icc 0 1) := (ℓ.continuous.comp_continuousOn hσc).div_const _
  obtain ⟨tm, htm, hmax⟩ := isCompact_Icc.exists_isMaxOn (nonempty_Icc.2 zero_le_one) hμc
  set m := μ tm with hmdef
  have hμ1 : μ 1 = 1 := by simp only [hμdef, ← hv₁, div_self hℓ1.ne']
  have hm1 : 1 ≤ m := hμ1 ▸ hmax ⟨zero_le_one, le_rfl⟩
  have hm0 : 0 < m := by linarith
  set v := m • v₁ with hvdef
  have hvσ : v = σ tm := (hσμ tm htm).symm
  have hvball : v ∈ ball (0 : V) G.ρ := by rw [hvσ]; exact N.lb_good_dom (hgood tm htm)
  have hvnull : S.g p v v = 0 := by
    simp only [hvdef, map_smul, smul_apply, smul_eq_mul]
    have : S.g p v₁ v₁ = 0 := hnull1
    rw [this]; ring
  have hvfut : S.g p v (S.T p) < 0 := by
    simp only [hvdef, map_smul, smul_apply, smul_eq_mul]
    exact mul_neg_of_pos_of_neg hm0 hfut
  -- every curve point is on the geodesic
  have hγr : ∀ t ∈ Icc (0 : ℝ) 1, μ t / m ∈ Icc (0 : ℝ) 1 ∧ γ t = G.radC2 v (μ t / m) := by
    intro t ht
    have hr : μ t / m ∈ Icc (0 : ℝ) 1 :=
      ⟨div_nonneg (hμnn t ht) hm0.le, (div_le_one hm0).2 (hmax ht)⟩
    refine ⟨hr, ?_⟩
    rw [G.lb_radC2_eq hg hvball hr, N.lb_good_eq_expp (hgood t ht)]
    congr 1
    show σ t = _
    rw [hσμ t ht, hvdef, smul_smul, div_mul_cancel₀ _ hm0.ne']
  refine ⟨v, hvball, hvnull, hvfut, G.lb_radC2_contDiff hg hvball,
    fun t ht => ⟨_, (hγr t ht).1, (hγr t ht).2⟩, fun r hr => ?_,
    G.lb_radC2_futNull hg hvball hvnull hvfut⟩
  -- every geodesic point is a curve point (intermediate value theorem on `[0, tm]`)
  have hsub : Icc 0 tm ⊆ Icc (0 : ℝ) 1 := Icc_subset_Icc le_rfl htm.2
  have hf : ContinuousOn (fun t => μ t / m) (Icc 0 tm) := (hμc.mono hsub).div_const _
  have h0' : μ 0 / m = 0 := by simp [hμdef, hσdef, h0, N.lb_symm_p]
  have htm' : μ tm / m = 1 := div_self hm0.ne'
  obtain ⟨t, ht, htr⟩ := intermediate_value_Icc htm.1 hf (by rw [h0', htm']; exact hr)
  refine ⟨t, hsub ht, ?_⟩
  rw [(hγr t (hsub ht)).2]
  simp only at htr
  rw [htr]

/-- **③ (b) Generators of `𝓗⁺` are null pregeodesics.** If, in addition, the curve lies in the
horizon `H = ∂J⁻(J)`, then the `C²` radial null geodesic `β` that it reparametrises lies in `H` on
`[0,1]`, so campaign 70's `lb_H_generator_null_pregeodesic` applies to `β`. -/
theorem lb_H_generator_radial_pregeodesic (hg : ContDiff ℝ 2 S.g) (J : Set V) {γ : ℝ → V}
    {K : ℝ≥0} {R : ℝ} (hB : closedBall p R ⊆ N.good) (hlip : LipschitzOnWith K γ (Icc 0 1))
    (hmem : ∀ t ∈ Icc (0 : ℝ) 1, γ t ∈ closedBall p R) (h0 : γ 0 = p)
    (hQ : ∀ t ∈ Icc (0 : ℝ) 1, N.Q (γ t) = 0) (hne : ∀ t ∈ Ioc (0 : ℝ) 1, γ t ≠ p)
    (hc : ∀ᵐ t ∂(volume : Measure ℝ), t ∈ Ioo (0 : ℝ) 1 →
      DifferentiableAt ℝ γ t → S.g (γ t) (deriv γ t) (deriv γ t) ≤ 0)
    (hfut : S.g p (N.Φ.symm (γ 1)) (S.T p) < 0) (hH : ∀ t ∈ Icc (0 : ℝ) 1, γ t ∈ S.H J) :
    ∃ v ∈ ball (0 : V) G.ρ, ContDiff ℝ 2 (G.radC2 v) ∧
      (∀ t ∈ Icc (0 : ℝ) 1, ∃ r ∈ Icc (0 : ℝ) 1, γ t = G.radC2 v r) ∧
      (∀ t ∈ Ioo (0 : ℝ) 1,
        S.g (G.radC2 v t) (deriv (G.radC2 v) t) (deriv (G.radC2 v) t) = 0) ∧
      S.IsPregeodesicOn (G.radC2 v) (Ioo 0 1) := by
  obtain ⟨v, hv, -, -, hC2, hto, hfrom, hcaus⟩ :=
    N.lb_generator_null_geodesic hg hB hlip hmem h0 hQ hne hc hfut
  have hHβ : ∀ r ∈ Icc (0 : ℝ) 1, G.radC2 v r ∈ S.H J := fun r hr => by
    obtain ⟨t, ht, e⟩ := hfrom r hr
    rw [e]; exact hH t ht
  have := S.lb_H_generator_null_pregeodesic (hg.of_le (by norm_num)) J hC2
    (fun r hr => ⟨(hcaus r hr).1, (hcaus r hr).2.1⟩) hHβ
  exact ⟨v, hv, hC2, hto, this.1, this.2⟩

/-- **④ (stretch, the part that is built): the generators are tangent to a regular conoid.** At a
point `x ≠ p` of the null conoid `{Q = 0}`, `DQ_x = 2 g_x(P x, ·) ≠ 0`, so `{Q = 0}` is a `C¹`
hypersurface near `x` (regular level set), and the generator direction `P x` lies in its tangent
space `ker DQ_x = (P x)^⊥`. -/
theorem lb_conoid_regular (hg : ContDiff ℝ 2 S.g) {x : V} (hx : x ∈ N.good) (hxp : x ≠ p)
    (hQ : N.Q x = 0) : fderiv ℝ N.Q x ≠ 0 ∧ fderiv ℝ N.Q x (N.P x) = 0 := by
  rw [(N.lb_grad_Q hg hx).fderiv]
  refine ⟨fun h => N.lb_P_ne_zero hg hx hxp (S.lb_nondegenerate (N.lb_good_mem_M hg hx) fun w => ?_), ?_⟩
  · have := congrArg (fun L : V →L[ℝ] ℝ => L w) h
    simp only [smul_apply, smul_eq_mul, zero_apply] at this
    linarith
  · simp only [smul_apply, smul_eq_mul, N.lb_P_energy hg hx, hQ, mul_zero]

end NormalChart

end GeoFlow

end Spacetime

/-! ## Copied from campaign 76 (`probes/ConoidBootstrap.lean`, `cb_` ↦ `lb_`): the near-conoid
estimate, the Grönwall step and the bootstrap away from `t = 0` -/

/-- Differences of real Lipschitz functions on a set are Lipschitz. -/
theorem lb_lip_sub {f g : ℝ → ℝ} {s : Set ℝ} {Kf Kg : ℝ≥0} (hf : LipschitzOnWith Kf f s)
    (hg : LipschitzOnWith Kg g s) : LipschitzOnWith (Kf + Kg) (fun t => f t - g t) s := by
  rw [lipschitzOnWith_iff_dist_le_mul] at *
  intro x hx y hy
  have h1 := hf x hx y hy
  have h2 := hg x hx y hy
  rw [Real.dist_eq] at *
  push_cast
  have : |f x - g x - (f y - g y)| ≤ |f x - f y| + |g x - g y| := by
    rw [show f x - g x - (f y - g y) = (f x - f y) - (g x - g y) by ring]; exact abs_sub _ _
  linarith

/-- **Comparison for Lipschitz functions.** If `F` is Lipschitz on `[a,b]` and `F′ ≤ ψ′` a.e. on
`(a,b)` for a `C¹` comparison function `ψ`, then `F t - F a ≤ ψ t - ψ a` on `[a,b]` (FTC for the
absolutely continuous `F - ψ`, as in `lb_Q_antitone`). -/
theorem lb_le_of_ae_deriv {F ψ : ℝ → ℝ} {a b : ℝ} {K : ℝ≥0}
    (hF : LipschitzOnWith K F (Icc a b)) (hψ : ContDiff ℝ 1 ψ)
    (hd : ∀ᵐ t ∂(volume : Measure ℝ), t ∈ Ioo a b → ∃ d, HasDerivAt F d t ∧ d ≤ deriv ψ t) :
    ∀ t ∈ Icc a b, F t - F a ≤ ψ t - ψ a := by
  obtain ⟨Kψ, hKψ⟩ := ContDiffOn.exists_lipschitzOnWith (s := Icc a b)
    (fun x _ => hψ.contDiffAt.contDiffWithinAt) one_ne_zero (convex_Icc a b) isCompact_Icc
  have hG := lb_lip_sub hF hKψ
  intro t ht
  have hat : a ≤ t := ht.1
  have hsub : Icc a t ⊆ Icc a b := Icc_subset_Icc le_rfl ht.2
  have hac : AbsolutelyContinuousOnInterval (fun s => F s - ψ s) a t := by
    have h := hG.mono hsub
    rw [← uIcc_of_le hat] at h
    exact h.absolutelyContinuousOnInterval
  have hint := hac.integral_deriv_eq_sub
  have hnn : 0 ≤ ∫ x in a..t, -deriv (fun s => F s - ψ s) x := by
    apply intervalIntegral.integral_nonneg_of_ae_restrict hat
    rw [Filter.EventuallyLE, ae_restrict_iff' measurableSet_Icc]
    filter_upwards [hd, Measure.ae_ne volume a, Measure.ae_ne volume t] with x hx hxa hxt hxI
    have hxI' : x ∈ Ioo a t := ⟨lt_of_le_of_ne hxI.1 (Ne.symm hxa), lt_of_le_of_ne hxI.2 hxt⟩
    obtain ⟨d, hdF, hdle⟩ := hx ⟨hxI'.1, hxI'.2.trans_le ht.2⟩
    have := (hdF.sub (hψ.differentiable one_ne_zero x).hasDerivAt).deriv
    simp only [Pi.zero_apply]
    rw [show (fun s => F s - ψ s) = F - ψ from rfl, this]; linarith
  rw [intervalIntegral.integral_neg, hint] at hnn
  linarith

namespace Spacetime
variable (S : Spacetime V)

/-- **① The near-conoid estimate, pointwise (reverse Cauchy–Schwarz with defect).** For any vector
`P` and any `w` in the closed future cone at `x ∈ M`,
`2 (−g(P,T)) g(P,w) ≤ (−g(w,T)) g(P,P)`.
(The vector `(−g(P,T)) w − (−g(w,T)) P` is `g`-orthogonal to `T`, so has `g ≥ 0`.) -/
theorem lb_near_conoid {x : V} (hx : x ∈ S.M) (P : V) {w : V} (hw : w ∈ S.CC x) :
    2 * (-S.g x P (S.T x)) * S.g x P w ≤ (-S.g x w (S.T x)) * S.g x P P := by
  have hsym : S.g x w P = S.g x P w := S.symm _ _ _
  have hz : S.g x ((-S.g x P (S.T x)) • w - (-S.g x w (S.T x)) • P) (S.T x) = 0 := by
    simp only [map_sub, map_smul, sub_apply, smul_apply,
      smul_eq_mul]
    ring
  have hzz := S.lb_perp_nonneg hx hz
  simp only [map_sub, map_smul, sub_apply, smul_apply,
    smul_eq_mul, hsym] at hzz
  have hB : 0 ≤ -S.g x w (S.T x) := by linarith [hw.2]
  rcases hB.eq_or_lt with h0 | hpos
  · have hw0 : w = 0 := by
      by_contra hne
      have := S.pos_on_perp x hx w (by linarith) hne
      linarith [hw.1]
    subst hw0
    simp
  · by_contra hcon
    rw [not_le] at hcon
    nlinarith [mul_nonpos_of_nonneg_of_nonpos (sq_nonneg (-S.g x P (S.T x))) hw.1,
      mul_pos hpos (sub_pos.2 hcon)]

/-- **① Near-conoid estimate, normed form.** If `g(P,T) < 0`, then for future-causal `w`,
`g(P,w) ≤ C · max(g(P,P), 0) · ‖w‖` with `C = ‖g_x‖ ‖T x‖ / (2 (−g(P,T)))`. The constant blows up
as `g(P,T) → 0`, in particular at the vertex, where `P = 0` (`lb_P_p`). -/
theorem lb_near_conoid_norm {x : V} (hx : x ∈ S.M) {P w : V} (hw : w ∈ S.CC x)
    (hPT : S.g x P (S.T x) < 0) :
    S.g x P w ≤ ‖S.g x‖ * ‖S.T x‖ / (2 * -S.g x P (S.T x)) * max (S.g x P P) 0 * ‖w‖ := by
  have h := S.lb_near_conoid hx P hw
  have hB0 : 0 ≤ -S.g x w (S.T x) := by linarith [hw.2]
  have hBn : -S.g x w (S.T x) ≤ ‖S.g x‖ * ‖S.T x‖ * ‖w‖ := by
    have h1 := (S.g x w).le_opNorm (S.T x)
    have h2 := (S.g x).le_opNorm w
    have h3 := neg_le_abs (S.g x w (S.T x))
    rw [← Real.norm_eq_abs] at h3
    calc _ ≤ _ := h3
      _ ≤ ‖S.g x w‖ * ‖S.T x‖ := h1
      _ ≤ ‖S.g x‖ * ‖w‖ * ‖S.T x‖ := by gcongr
      _ = _ := by ring
  have hQ : S.g x P P ≤ max (S.g x P P) 0 := le_max_left _ _
  have hQ0 : 0 ≤ max (S.g x P P) 0 := le_max_right _ _
  have hA : 0 < 2 * -S.g x P (S.T x) := by linarith
  rw [div_mul_eq_mul_div, div_mul_eq_mul_div, le_div_iff₀ hA]
  nlinarith [mul_le_mul_of_nonneg_left hQ hB0, mul_le_mul_of_nonneg_right hBn hQ0]

/-- Along a Lipschitz curve in a closed ball, `−g(γ′, T)` is bounded at differentiability points. -/
theorem lb_vel_T_bound {γ : ℝ → V} {K : ℝ≥0} {p : V} {R : ℝ}
    (hlip : LipschitzOnWith K γ (Icc 0 1)) (hmem : ∀ t ∈ Icc (0 : ℝ) 1, γ t ∈ closedBall p R) :
    ∃ L : ℝ, 0 ≤ L ∧ ∀ t ∈ Ioo (0 : ℝ) 1, DifferentiableAt ℝ γ t →
      -S.g (γ t) (deriv γ t) (S.T (γ t)) ≤ L := by
  obtain ⟨Cg, hCg⟩ :=
    (isCompact_closedBall p R).exists_bound_of_continuousOn (f := S.g) (by exact S.cont_g.continuousOn)
  obtain ⟨CT, hCT⟩ :=
    (isCompact_closedBall p R).exists_bound_of_continuousOn S.cont_T.continuousOn
  refine ⟨max Cg 0 * K * max CT 0,
    mul_nonneg (mul_nonneg (le_max_right _ _) K.2) (le_max_right _ _), fun t ht hd => ?_⟩
  have hx := hmem t (Ioo_subset_Icc_self ht)
  have hv : ‖deriv γ t‖ ≤ K := hd.hasDerivAt.le_of_lipschitzOn (Icc_mem_nhds ht.1 ht.2) hlip
  have h1 := (S.g (γ t) (deriv γ t)).le_opNorm (S.T (γ t))
  have h2 := (S.g (γ t)).le_opNorm (deriv γ t)
  have h3 := neg_le_abs (S.g (γ t) (deriv γ t) (S.T (γ t)))
  rw [← Real.norm_eq_abs] at h3
  have hg : ‖S.g (γ t)‖ ≤ max Cg 0 := (hCg _ hx).trans (le_max_left Cg 0)
  have hT : ‖S.T (γ t)‖ ≤ max CT 0 := (hCT _ hx).trans (le_max_left CT 0)
  calc _ ≤ _ := h3
    _ ≤ _ := h1
    _ ≤ ‖S.g (γ t)‖ * ‖deriv γ t‖ * ‖S.T (γ t)‖ := by gcongr
    _ ≤ max Cg 0 * K * max CT 0 := by gcongr

namespace GeoFlow

variable {S} {p : V} (G : S.GeoFlow p)

/-- `rad` is continuous on the normal-coordinate ball (the flow is Lipschitz in the initial point). -/
theorem lb_rad_continuousAt {v : V} (hv : v ∈ ball (0 : V) G.ρ) : ContinuousAt G.rad v := by
  have hy := ball_subset_ball G.lb_r₁_le (G.lb_dom hv)
  have h1 : ContinuousAt (fun y => G.D.α y G.s₀) (p, G.c • v) :=
    (G.D.lip G.s₀ G.lb_s₀_mem).continuousOn.continuousAt
      (mem_of_superset (isOpen_ball.mem_nhds hy) ball_subset_closedBall)
  have h2 : ContinuousAt (fun w : V => ((p, G.c • w) : V × V)) v :=
    continuousAt_const.prodMk (continuousAt_id.const_smul G.c)
  have h3 : ContinuousAt (fun w : V => G.D.α (p, G.c • w) G.s₀) v :=
    ContinuousAt.comp (g := fun y => G.D.α y G.s₀) (f := fun w : V => ((p, G.c • w) : V × V))
      h1 h2
  have h4 : ContinuousAt (fun w : V => (G.D.α (p, G.c • w) G.s₀).2) v :=
    ContinuousAt.comp (g := Prod.snd) (f := fun w : V => G.D.α (p, G.c • w) G.s₀)
      continuous_snd.continuousAt h3
  exact h4.const_smul G.s₀

/-- `D exp_p` is continuous at `0`, with value `id` (`exp_p` is `C¹`). -/
theorem lb_Dexp_tendsto (hg : ContDiff ℝ 2 S.g) :
    Tendsto G.Dexp (𝓝 0) (𝓝 (ContinuousLinearMap.id ℝ V)) := by
  have h1 := (G.lb_expp_contDiffAt hg (mem_ball_self G.lb_ρ_pos)).continuousAt_fderiv one_ne_zero
  have heq : fderiv ℝ G.expp =ᶠ[𝓝 0] G.Dexp := by
    filter_upwards [isOpen_ball.mem_nhds (mem_ball_self G.lb_ρ_pos)] with v hv
    exact (G.lb_expp_hasFDerivAt hg hv).fderiv
  have h2 : Tendsto (fderiv ℝ G.expp) (𝓝 0) (𝓝 (fderiv ℝ G.expp 0)) := h1
  rw [heq.eq_of_nhds, G.lb_Dexp_zero hg] at h2
  exact h2.congr' heq

/-- **Time orientation is transported along radial geodesics.** For a nonzero causal `v` at `p`,
`v` is future-directed iff the radial velocity `rad v` at `exp_p v` is (`g(β′, T)` cannot vanish
along the radial geodesic `β`: it is causal, and `β′ = 0` would force `v = 0`). -/
theorem lb_orient (hg : ContDiff ℝ 2 S.g) {v : V} (hv : v ∈ ball (0 : V) G.ρ)
    (hc : S.g p v v ≤ 0) (hv0 : v ≠ 0) :
    S.g p v (S.T p) < 0 ↔ S.g (G.expp v) (G.rad v) (S.T (G.expp v)) < 0 := by
  have hy := G.lb_dom_closed hv
  have hpos : ∀ r ∈ Icc (0 : ℝ) 1, G.radC2 v r = (G.D.α (p, G.c • v) (r * G.s₀)).1 :=
    fun r hr => by rw [radC2, lb_psi_eq hr]
  have hder : ∀ r ∈ Icc (0 : ℝ) 1,
      deriv (G.radC2 v) r = G.s₀ • (G.D.α (p, G.c • v) (r * G.s₀)).2 := fun r hr =>
    (G.lb_radC2_deriv hg hv hr).deriv
  have hM : ∀ r ∈ Icc (0 : ℝ) 1, G.radC2 v r ∈ S.M := fun r hr => by
    rw [hpos r hr]; exact G.lb_ball_sub_M (G.lb_traj_in hg hy (G.lb_mul_s₀_mem hr))
  have hN : ∀ r ∈ Icc (0 : ℝ) 1,
      S.g (G.radC2 v r) (deriv (G.radC2 v) r) (deriv (G.radC2 v) r) = S.g p v v := by
    intro r hr
    rw [hpos r hr, hder r hr]
    have hE := G.lb_energy_cons hg hy (G.lb_mul_s₀_mem hr)
    simp only [map_smul, smul_apply, smul_eq_mul] at hE ⊢
    rw [hE]
    have h := G.lb_c_s₀
    linear_combination (G.c * G.s₀ + 1) * S.g p v v * h
  have hβ := G.lb_radC2_contDiff hg hv
  let h : ℝ → ℝ := fun t => S.g (G.radC2 v t) (deriv (G.radC2 v) t) (S.T (G.radC2 v t))
  have hhc : Continuous h :=
    ((S.cont_g.comp hβ.continuous).clm_apply (hβ.continuous_deriv (by norm_num))).clm_apply
      (S.cont_T.comp hβ.continuous)
  have h0mem : (0 : ℝ) ∈ Icc (0 : ℝ) 1 := ⟨le_rfl, zero_le_one⟩
  have h1mem : (1 : ℝ) ∈ Icc (0 : ℝ) 1 := ⟨zero_le_one, le_rfl⟩
  have hpM : p ∈ S.M := G.lb_ball_sub_M (mem_ball_self G.χ.rIn_pos)
  have hh0 : h 0 = S.g p v (S.T p) := by
    have e1 : G.radC2 v 0 = p := by
      rw [hpos 0 h0mem, zero_mul, G.D.init _ (G.lb_mem_r hy)]
    have e2 : deriv (G.radC2 v) 0 = v := by
      rw [hder 0 h0mem, zero_mul, G.D.init _ (G.lb_mem_r hy)]
      simp only [smul_smul, mul_comm G.s₀ G.c, G.lb_c_s₀, one_smul]
    simp only [h, e1, e2]
  have hh1 : h 1 = S.g (G.expp v) (G.rad v) (S.T (G.expp v)) := by
    have e1 : G.radC2 v 1 = G.expp v := by rw [hpos 1 h1mem, one_mul]; rfl
    have e2 : deriv (G.radC2 v) 1 = G.rad v := by rw [hder 1 h1mem, one_mul]; rfl
    simp only [h, e1, e2]
  have hh0ne : h 0 ≠ 0 := by
    rw [hh0]; intro h0
    have := S.pos_on_perp p hpM v h0 hv0
    linarith
  have hne : ∀ t ∈ Icc (0 : ℝ) 1, h t ≠ 0 := fun t ht h0 => by
    have hd0 : deriv (G.radC2 v) t = 0 := by
      by_contra hd0
      have := S.pos_on_perp _ (hM t ht) _ h0 hd0
      rw [hN t ht] at this; linarith
    have ht0 : t ≠ 0 := fun e => by rw [e] at h0; exact hh0ne h0
    have hu0 : (G.D.α (p, G.c • v) (t * G.s₀)).2 = 0 := by
      rw [hder t ht] at hd0
      exact (smul_eq_zero.1 hd0).resolve_left G.lb_s₀_pos.ne'
    have hz : G.c • v = 0 := S.lb_nondegenerate hpM fun b => by
      have := G.lb_gauss_flow hg (G.lb_dom hv) b (G.lb_mul_s₀_mem ht)
      rw [hu0] at this
      simp only [map_zero, zero_apply] at this
      have hts : t * G.s₀ ≠ 0 := mul_ne_zero ht0 G.lb_s₀_pos.ne'
      exact (mul_eq_zero.1 this.symm).resolve_left hts
    exact hv0 ((smul_eq_zero.1 hz).resolve_left G.lb_c_pos.ne')
  rw [← hh0, ← hh1]
  constructor
  · intro hl
    by_contra hcon
    rw [not_lt] at hcon
    obtain ⟨s, hs, hs0⟩ := intermediate_value_Icc zero_le_one hhc.continuousOn ⟨hl.le, hcon⟩
    exact hne s hs hs0
  · intro hl
    by_contra hcon
    rw [not_lt] at hcon
    obtain ⟨s, hs, hs0⟩ := intermediate_value_Icc' zero_le_one hhc.continuousOn ⟨hl.le, hcon⟩
    exact hne s hs hs0

namespace NormalChart

variable {G} (N : G.NormalChart)

/-- `P` vanishes at the vertex: there the near-conoid constant of `lb_near_conoid_P` is not
available (no uniform `C` at `p`). -/
theorem lb_P_p (hg : ContDiff ℝ 2 S.g) : N.P p = 0 := by
  simp [P, rad, N.lb_symm_p, G.D.lb_fixed (G.lb_hf hg) (S.lb_cutField_zero G.χ) G.s₀ G.lb_s₀_mem]

theorem lb_P_continuousAt {x : V} (hx : x ∈ N.good) : ContinuousAt N.P x :=
  (G.lb_rad_continuousAt (N.lb_good_dom hx)).comp hx.2.continuousAt

/-- **① on the normal ball.** At a chart point where `P` is future-pointing (`g(P,T) < 0`), for
future-causal `w`: `g_x(P x, w) ≤ C(x) · max(Q x, 0) · ‖w‖`, `C(x) = ‖g_x‖‖T x‖ / (2(−g(P,T)))`. -/
theorem lb_near_conoid_P (hg : ContDiff ℝ 2 S.g) {x : V} (hx : x ∈ N.good) {w : V}
    (hw : w ∈ S.CC x) (hPT : S.g x (N.P x) (S.T x) < 0) :
    S.g x (N.P x) w ≤
      ‖S.g x‖ * ‖S.T x‖ / (2 * -S.g x (N.P x) (S.T x)) * max (N.Q x) 0 * ‖w‖ := by
  have := S.lb_near_conoid_norm (N.lb_good_mem_M hg hx) hw hPT
  rwa [N.lb_P_energy hg hx] at this

/-- Off the vertex, `P ∈ CC` forces `g(P, T) < 0` strictly. -/
theorem lb_P_T_neg (hg : ContDiff ℝ 2 S.g) {x : V} (hx : x ∈ N.good) (hxp : x ≠ p)
    (hP : N.P x ∈ S.CC x) : S.g x (N.P x) (S.T x) < 0 := by
  rcases hP.2.lt_or_eq with h | h
  · exact h
  · exfalso
    have := S.pos_on_perp x (N.lb_good_mem_M hg hx) _ h (N.lb_P_ne_zero hg hx hxp)
    linarith [hP.1]

/-- Orientation in the chart: for `x ≠ p` with `Q x ≤ 0`, `exp_p⁻¹ x` is future iff `P x` is. -/
theorem lb_orient_chart (hg : ContDiff ℝ 2 S.g) {x : V} (hx : x ∈ N.good) (hxp : x ≠ p)
    (hQ : N.Q x ≤ 0) :
    S.g p (N.Φ.symm x) (S.T p) < 0 ↔ S.g x (N.P x) (S.T x) < 0 := by
  have hv0 : N.Φ.symm x ≠ 0 := fun h => hxp (N.lb_eq_p_of_symm hx h)
  have := G.lb_orient hg (N.lb_good_dom hx) hQ hv0
  rwa [N.lb_good_expp hx] at this

/-- `D(exp_p⁻¹)(p) = id`. -/
theorem lb_fderiv_symm_p (hg : ContDiff ℝ 2 S.g) :
    fderiv ℝ N.Φ.symm p = ContinuousLinearMap.id ℝ V := by
  have hp : p ∈ N.good := mem_of_mem_nhds N.lb_good_nhds
  have h := N.lb_Dexp_comp_symm hg hp
  rwa [N.lb_symm_p, G.lb_Dexp_zero hg, ContinuousLinearMap.id_comp] at h

/-- A closed normal ball on which moreover `exp_p⁻¹` lands in `ball 0 (ρ/3)` (the smallness
needed by `lb_chr_of_Q_neg`). -/
theorem lb_exists_ball_small : ∃ R > (0 : ℝ), closedBall p R ⊆ N.good ∧
    ∀ x ∈ closedBall p R, N.Φ.symm x ∈ ball (0 : V) (G.ρ / 3) := by
  have hp : p ∈ N.good := mem_of_mem_nhds N.lb_good_nhds
  have hc : ContinuousAt N.Φ.symm p := hp.2.continuousAt
  have h1 : N.Φ.symm ⁻¹' ball (0 : V) (G.ρ / 3) ∈ 𝓝 p := hc.preimage_mem_nhds (by
    rw [N.lb_symm_p]; exact isOpen_ball.mem_nhds (mem_ball_self (by have := G.lb_ρ_pos; positivity)))
  obtain ⟨ε, hε, hsub⟩ := Metric.mem_nhds_iff.1 (inter_mem N.lb_good_nhds h1)
  exact ⟨ε / 2, by positivity, fun x hx => (hsub (closedBall_subset_ball (by linarith) hx)).1,
    fun x hx => (hsub (closedBall_subset_ball (by linarith) hx)).2⟩

/-- **② The Grönwall step (away from `t = 0`).** On `[a,b] ⊆ [0,1]` along a Lipschitz causal
curve in the normal ball, if `g(P,T) ≤ −δ` on `[a,b]`, `−g(γ′,T) ≤ L`, the interval is short
(`(b − a) L ≤ δ/2`) and `Q(γ a) ≤ 0`, then `Q ∘ γ ≤ 0` on `[a,b]`. By ①, `(Q∘γ)′ ≤ (L/δ) Q⁺`;
with `M = max Q⁺` on `[a,b]` this gives `Q⁺ ≤ M/2`, so `M = 0`. -/
theorem lb_gronwall_step (hg : ContDiff ℝ 2 S.g) {γ : ℝ → V} {K : ℝ≥0} {R : ℝ}
    (hB : closedBall p R ⊆ N.good) (hlip : LipschitzOnWith K γ (Icc 0 1))
    (hmem : ∀ t ∈ Icc (0 : ℝ) 1, γ t ∈ closedBall p R)
    (hcausal : ∀ᵐ t ∂(volume : Measure ℝ), t ∈ Ioo (0 : ℝ) 1 → DifferentiableAt ℝ γ t →
      deriv γ t ∈ S.CC (γ t))
    {L δ a b : ℝ} (hL0 : 0 ≤ L)
    (hL : ∀ t ∈ Ioo (0 : ℝ) 1, DifferentiableAt ℝ γ t → -S.g (γ t) (deriv γ t) (S.T (γ t)) ≤ L)
    (hδ : 0 < δ) (ha : 0 ≤ a) (hab : a ≤ b) (hb : b ≤ 1) (hlen : (b - a) * L ≤ δ / 2)
    (hA : ∀ t ∈ Icc a b, S.g (γ t) (N.P (γ t)) (S.T (γ t)) ≤ -δ) (hQa : N.Q (γ a) ≤ 0) :
    ∀ t ∈ Icc a b, N.Q (γ t) ≤ 0 := by
  have hsub : Icc a b ⊆ Icc (0 : ℝ) 1 := Icc_subset_Icc ha hb
  obtain ⟨KQ, hKQ⟩ := N.lb_Q_lipschitzOn hB
  have hQγ : LipschitzOnWith (KQ * K) (fun t => N.Q (γ t)) (Icc a b) :=
    (hKQ.comp hlip (fun t ht => hmem t ht)).mono hsub
  have hm : ContinuousOn (fun t => max (N.Q (γ t)) 0) (Icc a b) :=
    hQγ.continuousOn.sup continuousOn_const
  obtain ⟨ts, hts, hmax⟩ := isCompact_Icc.exists_isMaxOn (nonempty_Icc.2 hab) hm
  set M := max (N.Q (γ ts)) 0 with hMdef
  have hM0 : 0 ≤ M := le_max_right _ _
  have hmax' : ∀ t ∈ Icc a b, N.Q (γ t) ≤ M := fun t ht =>
    (le_max_left _ _).trans (hmax ht)
  have hcmp := lb_le_of_ae_deriv hQγ (ψ := fun t => L * M / δ * t)
    (contDiff_const.mul contDiff_id) (by
      filter_upwards [hcausal, hlip.ae_differentiableWithinAt_of_mem (μ := volume)]
        with t h1 h2 htI
      have ht01 : t ∈ Ioo (0 : ℝ) 1 := ⟨ha.trans_lt htI.1, htI.2.trans_le hb⟩
      have hd : DifferentiableAt ℝ γ t :=
        (h2 (Ioo_subset_Icc_self ht01)).differentiableAt (Icc_mem_nhds ht01.1 ht01.2)
      have hx := hB (hmem t (Ioo_subset_Icc_self ht01))
      refine ⟨_, N.lb_Q_comp_hasDerivAt hg hd.hasDerivAt hx, ?_⟩
      have hψ : deriv (fun t => L * M / δ * t) t = L * M / δ := by
        simp
      rw [hψ]
      have hw := h1 ht01 hd
      have hest := S.lb_near_conoid (N.lb_good_mem_M hg hx) (N.P (γ t)) hw
      rw [N.lb_P_energy hg hx] at hest
      have hAt := hA t (Ioo_subset_Icc_self htI)
      have hBt := hL t ht01 hd
      have hB0 : 0 ≤ -S.g (γ t) (deriv γ t) (S.T (γ t)) := by linarith [hw.2]
      have hQM := hmax' t (Ioo_subset_Icc_self htI)
      rw [le_div_iff₀ hδ]
      rcases le_or_gt (S.g (γ t) (N.P (γ t)) (deriv γ t)) 0 with hn | hp
      · nlinarith [mul_nonneg hL0 hM0]
      · nlinarith [mul_le_mul_of_nonneg_left (show δ ≤ -S.g (γ t) (N.P (γ t)) (S.T (γ t)) by
          linarith) (show (0 : ℝ) ≤ 2 * S.g (γ t) (N.P (γ t)) (deriv γ t) by linarith),
          mul_le_mul_of_nonneg_left hQM hB0, mul_le_mul_of_nonneg_right hBt hM0])
  have hbound : ∀ t ∈ Icc a b, N.Q (γ t) ≤ M / 2 := by
    intro t ht
    have h : N.Q (γ t) - N.Q (γ a) ≤ L * M / δ * t - L * M / δ * a := hcmp t ht
    have e : L * M / δ * t - L * M / δ * a = M * ((t - a) * L) / δ := by ring
    rw [e] at h
    have h2 : M * ((t - a) * L) / δ ≤ M / 2 := by
      rw [div_le_iff₀ hδ]
      have : (t - a) * L ≤ δ / 2 :=
        le_trans (mul_le_mul_of_nonneg_right (by linarith [ht.2]) hL0) hlen
      nlinarith
    linarith
  have hMle : M ≤ M / 2 := max_le (hbound ts hts) (by linarith)
  intro t ht
  linarith [hmax' t ht]

/-- **② The bootstrap (from any start time `t₀` with `P(γ t₀) ∈ CC`).** Along a Lipschitz
curve with velocity a.e. in the closed future cone, in the normal ball, avoiding `p` on `[t₀,1]`:
if `P(γ t₀)` is in the closed future cone, then so is `P(γ t)` for all `t ∈ [t₀,1]`, with
`g(P,T) < 0`; in particular `Q ≤ 0` there. (Continuous induction; each step is
`lb_gronwall_step`, launched with the strict `g(P,T) < 0` of `lb_P_T_neg`.) -/
theorem lb_bootstrap (hg : ContDiff ℝ 2 S.g) {γ : ℝ → V} {K : ℝ≥0} {R : ℝ}
    (hB : closedBall p R ⊆ N.good) (hlip : LipschitzOnWith K γ (Icc 0 1))
    (hmem : ∀ t ∈ Icc (0 : ℝ) 1, γ t ∈ closedBall p R)
    (hcausal : ∀ᵐ t ∂(volume : Measure ℝ), t ∈ Ioo (0 : ℝ) 1 → DifferentiableAt ℝ γ t →
      deriv γ t ∈ S.CC (γ t))
    {t₀ : ℝ} (ht₀ : t₀ ∈ Icc (0 : ℝ) 1) (hne : ∀ t ∈ Icc t₀ 1, γ t ≠ p)
    (hstart : N.P (γ t₀) ∈ S.CC (γ t₀)) :
    ∀ t ∈ Icc t₀ 1, N.P (γ t) ∈ S.CC (γ t) ∧ S.g (γ t) (N.P (γ t)) (S.T (γ t)) < 0 := by
  obtain ⟨L, hL0, hL⟩ := S.lb_vel_T_bound hlip hmem
  have hgood : ∀ t ∈ Icc (0 : ℝ) 1, γ t ∈ N.good := fun t ht => hB (hmem t ht)
  have hsub : Icc t₀ 1 ⊆ Icc (0 : ℝ) 1 := Icc_subset_Icc ht₀.1 le_rfl
  obtain ⟨KQ, hKQ⟩ := N.lb_Q_lipschitzOn hB
  have hQc : ContinuousOn (fun t => N.Q (γ t)) (Icc 0 1) :=
    (hKQ.comp hlip (fun t ht => hmem t ht)).continuousOn
  have hγc : ContinuousOn γ (Icc 0 1) := hlip.continuousOn
  let h : ℝ → ℝ := fun t => S.g (γ t) (N.P (γ t)) (S.T (γ t))
  have hhc : ContinuousOn h (Icc 0 1) := fun t ht =>
    ((S.cont_g.continuousAt.comp_continuousWithinAt (hγc t ht)).clm_apply
      ((N.lb_P_continuousAt (hgood t ht)).comp_continuousWithinAt (hγc t ht))).clm_apply
      (S.cont_T.continuousAt.comp_continuousWithinAt (hγc t ht))
  let s : Set ℝ := {t | N.Q (γ t) ≤ 0 ∧ h t ≤ 0}
  have hcl : IsClosed (s ∩ Icc t₀ 1) := by
    have := ((hQc.mono hsub).prodMk (hhc.mono hsub)).preimage_isClosed_of_isClosed isClosed_Icc
      ((isClosed_Iic (a := (0 : ℝ))).prod (isClosed_Iic (a := (0 : ℝ))))
    rw [inter_comm]; exact this
  have hstrict : ∀ t ∈ Icc t₀ 1, t ∈ s → h t < 0 := fun t ht hts =>
    N.lb_P_T_neg hg (hgood t (hsub ht)) (hne t ht)
      ((N.lb_P_mem_CC_iff hg (hgood t (hsub ht))).2 hts)
  have hIcc : Icc t₀ 1 ⊆ s := by
    refine hcl.Icc_subset_of_forall_mem_nhdsWithin
      ((N.lb_P_mem_CC_iff hg (hgood t₀ ht₀)).1 hstart) ?_
    rintro x ⟨hxs, hxI⟩
    have hx1 : x ∈ Icc t₀ 1 := Ico_subset_Icc_self hxI
    have hhx := hstrict x hx1 hxs
    set δ := -h x / 2 with hδ
    have hδ0 : 0 < δ := by linarith
    have hcw : ContinuousWithinAt h (Icc x 1) x :=
      (hhc x (hsub hx1)).mono (Icc_subset_Icc (ht₀.1.trans hxI.1) le_rfl)
    have hev : ∀ᶠ t in 𝓝[≥] x, h t < -δ :=
      (hcw.mono_of_mem_nhdsWithin (Icc_mem_nhdsGE hxI.2)).eventually
        (eventually_lt_nhds (show h x < -δ by linarith))
    obtain ⟨u, hu, hsubu⟩ := mem_nhdsGE_iff_exists_Icc_subset.1 hev
    have hq : 0 < δ / (2 * (L + 1)) := by positivity
    set b := min u (min 1 (x + δ / (2 * (L + 1)))) with hbdef
    have hxb : x < b := lt_min hu (lt_min hxI.2 (by linarith))
    have hb1 : b ≤ 1 := (min_le_right _ _).trans (min_le_left _ _)
    have hbu : b ≤ u := min_le_left _ _
    have hbl : b - x ≤ δ / (2 * (L + 1)) := by
      have : b ≤ x + δ / (2 * (L + 1)) := (min_le_right _ _).trans (min_le_right _ _)
      linarith
    have hkey : δ / (2 * (L + 1)) * L ≤ δ / 2 := by
      rw [div_mul_eq_mul_div, div_le_div_iff₀ (by positivity) (by norm_num)]
      nlinarith
    have hlen : (b - x) * L ≤ δ / 2 := (mul_le_mul_of_nonneg_right hbl hL0).trans hkey
    have hA : ∀ t ∈ Icc x b, S.g (γ t) (N.P (γ t)) (S.T (γ t)) ≤ -δ := fun t ht =>
      (hsubu ⟨ht.1, ht.2.trans hbu⟩).le
    have hQ := N.lb_gronwall_step hg hB hlip hmem hcausal hL0 hL hδ0 (ht₀.1.trans hxI.1) hxb.le
      hb1 hlen hA hxs.1
    rw [mem_nhdsGT_iff_exists_Ioo_subset]
    exact ⟨b, hxb, fun t ht => ⟨hQ t (Ioo_subset_Icc_self ht),
      (hA t (Ioo_subset_Icc_self ht)).trans (by linarith)⟩⟩
  intro t ht
  have hts := hIcc ht
  exact ⟨(N.lb_P_mem_CC_iff hg (hgood t (hsub ht))).2 hts, hstrict t ht hts⟩


/-- **② Discharging campaign 73's conoid hypothesis for achronal curves.** A curve from `p` in
the horizon `H = ∂J⁻(J)`, in a small normal ball, along which `P` stays in the closed future cone
on `(0,1]`, lies on the null conoid `{Q = 0}`: `Q < 0` would give `p ≪ γ t` (orientation transport
`lb_orient_chart`, then `lb_chr_of_Q_neg`), contradicting achronality of `H`. -/
theorem lb_generator_Q_zero (hg : ContDiff ℝ 2 S.g) (J : Set V) {γ : ℝ → V} {R : ℝ}
    (hB : closedBall p R ⊆ N.good)
    (hsmall : ∀ x ∈ closedBall p R, N.Φ.symm x ∈ ball (0 : V) (G.ρ / 3))
    (hmem : ∀ t ∈ Icc (0 : ℝ) 1, γ t ∈ closedBall p R) (h0 : γ 0 = p)
    (hne : ∀ t ∈ Ioc (0 : ℝ) 1, γ t ≠ p)
    (hcone : ∀ t ∈ Ioc (0 : ℝ) 1, N.P (γ t) ∈ S.CC (γ t))
    (hH : ∀ t ∈ Icc (0 : ℝ) 1, γ t ∈ S.H J) :
    ∀ t ∈ Icc (0 : ℝ) 1, N.Q (γ t) = 0 := by
  intro t ht
  rcases ht.1.eq_or_lt with e | hlt
  · rw [← e, h0, N.lb_Q_p]
  have ht' : t ∈ Ioc (0 : ℝ) 1 := ⟨hlt, ht.2⟩
  have hx := hB (hmem t ht)
  have hP := hcone t ht'
  have hQle := ((N.lb_P_mem_CC_iff hg hx).1 hP).1
  refine le_antisymm hQle (not_lt.1 fun hQ => ?_)
  have hPT := N.lb_P_T_neg hg hx (hne t ht') hP
  have hfut := (N.lb_orient_chart hg hx (hne t ht') hQle).2 hPT
  have hchr := N.lb_chr_of_Q_neg hg hx hQ hfut (hsmall _ (hmem t ht))
  have h0H := hH 0 ⟨le_rfl, zero_le_one⟩
  rw [h0] at h0H
  exact S.lb_H_achronal J h0H (hH t ht) hchr


end NormalChart

end GeoFlow

end Spacetime

/-! ## Campaign 77 (new): ① the Lipschitz-start bootstrap -/

/-- `F` Lipschitz on `[a,b]` with `F′ ≤ 0` a.e. ⟹ `F t ≤ F a` (`lb_le_of_ae_deriv`, `ψ = 0`). -/
theorem lb_le_start_of_ae_deriv {F : ℝ → ℝ} {a b : ℝ} {K : ℝ≥0}
    (hF : LipschitzOnWith K F (Icc a b))
    (hd : ∀ᵐ t ∂(volume : Measure ℝ), t ∈ Ioo a b → ∃ d, HasDerivAt F d t ∧ d ≤ 0) :
    ∀ t ∈ Icc a b, F t ≤ F a := by
  intro t ht
  have := lb_le_of_ae_deriv (ψ := fun _ => (0 : ℝ)) hF contDiff_const (by
    filter_upwards [hd] with s hs hsI
    obtain ⟨d, h1, h2⟩ := hs hsI
    exact ⟨d, h1, by simpa using h2⟩) t ht
  linarith

namespace Spacetime
variable (S : Spacetime V)

/-- **A uniform cone constant near a point of `M`.** There are `r, c > 0` with
`−g_x(w, T x) ≥ c ‖w‖` for every `x ∈ closedBall p r` and every `w` in the closed future cone at
`x`. (Compactness of `{(x,u) : x ∈ closedBall p r, ‖u‖ = 1, u ∈ CC x}`, on which `−g(u,T) > 0`
by `pos_on_perp`.) -/
theorem lb_cone_const {p : V} (hp : p ∈ S.M) :
    ∃ r > (0 : ℝ), ∃ c > (0 : ℝ), closedBall p r ⊆ S.M ∧
      ∀ x ∈ closedBall p r, ∀ w ∈ S.CC x, c * ‖w‖ ≤ -S.g x w (S.T x) := by
  obtain ⟨ε, hε, hball⟩ := Metric.isOpen_iff.1 S.isOpen_M p hp
  have hsubM : closedBall p (ε / 2) ⊆ S.M :=
    (closedBall_subset_ball (by linarith)).trans hball
  have hcg : Continuous fun z : V × V => S.g z.1 z.2 z.2 :=
    ((S.cont_g.comp continuous_fst).clm_apply continuous_snd).clm_apply continuous_snd
  have hcT : Continuous fun z : V × V => S.g z.1 z.2 (S.T z.1) :=
    ((S.cont_g.comp continuous_fst).clm_apply continuous_snd).clm_apply
      (S.cont_T.comp continuous_fst)
  set K : Set (V × V) := (closedBall p (ε / 2) ×ˢ sphere (0 : V) 1) ∩
    {z | S.g z.1 z.2 z.2 ≤ 0 ∧ S.g z.1 z.2 (S.T z.1) ≤ 0} with hKdef
  have hK : IsCompact K :=
    ((isCompact_closedBall p (ε / 2)).prod (isCompact_sphere 0 1)).inter_right
      ((isClosed_le hcg continuous_const).inter (isClosed_le hcT continuous_const))
  obtain ⟨c, hc0, hc⟩ := hK.exists_forall_le' (f := fun z : V × V => -S.g z.1 z.2 (S.T z.1))
    hcT.neg.continuousOn (a := 0) (by
      rintro ⟨x, u⟩ ⟨⟨hx, hu⟩, h1, h2⟩
      simp only at h1 h2 hx hu ⊢
      have hu0 : u ≠ 0 := by
        intro h; rw [h, mem_sphere_zero_iff_norm, norm_zero] at hu; norm_num at hu
      rcases h2.lt_or_eq with h | h
      · linarith
      · have := S.pos_on_perp x (hsubM hx) u h hu0; linarith)
  refine ⟨ε / 2, by positivity, c, hc0, hsubM, fun x hx w hw => ?_⟩
  rcases eq_or_ne w 0 with rfl | hw0
  · simp
  have hn : 0 < ‖w‖ := norm_pos_iff.2 hw0
  have hmem : ((x, ‖w‖⁻¹ • w) : V × V) ∈ K := by
    refine ⟨⟨hx, ?_⟩, ?_, ?_⟩
    · rw [mem_sphere_zero_iff_norm, norm_smul, norm_inv, norm_norm, inv_mul_cancel₀ hn.ne']
    · simp only [map_smul, smul_apply, smul_eq_mul]
      exact mul_nonpos_of_nonneg_of_nonpos (inv_nonneg.2 hn.le)
        (mul_nonpos_of_nonneg_of_nonpos (inv_nonneg.2 hn.le) hw.1)
    · simp only [map_smul, smul_apply, smul_eq_mul]
      exact mul_nonpos_of_nonneg_of_nonpos (inv_nonneg.2 hn.le) hw.2
  have h := hc _ hmem
  simp only [map_smul, smul_apply, smul_eq_mul] at h
  calc c * ‖w‖ ≤ -(‖w‖⁻¹ * S.g x w (S.T x)) * ‖w‖ := mul_le_mul_of_nonneg_right h hn.le
    _ = -S.g x w (S.T x) := by field_simp

namespace GeoFlow

variable {S} {p : V} (G : S.GeoFlow p)

namespace NormalChart

variable {G} (N : G.NormalChart)

/-- **The uniform first-order expansion of `exp_p⁻¹` at `p` (BUILT, not assumed).** For every
`η > 0`, near `p`: `‖D(exp⁻¹)(x)‖ ≤ 2`,
`‖g_p(T p, D(exp⁻¹)(x) ·) − g_x(T x, ·)‖ ≤ η` and `‖g_x(T x, D exp(exp⁻¹ x) ·) − g_p(T p, ·)‖ ≤ η`.
(Continuity of `D(exp⁻¹)` at `p` and of `D exp` at `0`, both `= id` there, `lb_fderiv_symm_p`,
`lb_Dexp_tendsto`.) -/
theorem lb_expansion (hg : ContDiff ℝ 2 S.g) {η : ℝ} (hη : 0 < η) :
    ∀ᶠ x in 𝓝 p, x ∈ N.good ∧ ‖fderiv ℝ N.Φ.symm x‖ ≤ 2 ∧
      ‖(S.g p (S.T p)).comp (fderiv ℝ N.Φ.symm x) - S.g x (S.T x)‖ ≤ η ∧
      ‖(S.g x (S.T x)).comp (G.Dexp (N.Φ.symm x)) - S.g p (S.T p)‖ ≤ η := by
  have hp : p ∈ N.good := mem_of_mem_nhds N.lb_good_nhds
  have hA : ContinuousAt (fderiv ℝ N.Φ.symm) p := hp.2.continuousAt_fderiv one_ne_zero
  have hgT : ContinuousAt (fun x => S.g x (S.T x)) p :=
    S.cont_g.continuousAt.clm_apply S.cont_T.continuousAt
  have hσ : Tendsto N.Φ.symm (𝓝 p) (𝓝 0) := by
    have := hp.2.continuousAt; rw [ContinuousAt, N.lb_symm_p] at this; exact this
  have hD : ContinuousAt (fun x => G.Dexp (N.Φ.symm x)) p := by
    show Tendsto _ _ (𝓝 (G.Dexp (N.Φ.symm p)))
    rw [N.lb_symm_p, G.lb_Dexp_zero hg]; exact (G.lb_Dexp_tendsto hg).comp hσ
  have h1 : Tendsto (fun x => (S.g p (S.T p)).comp (fderiv ℝ N.Φ.symm x) - S.g x (S.T x))
      (𝓝 p) (𝓝 0) := by
    have := (continuousAt_const (y := S.g p (S.T p))).clm_comp hA |>.sub hgT
    have e : (S.g p (S.T p)).comp (fderiv ℝ N.Φ.symm p) - S.g p (S.T p) = 0 := by
      rw [N.lb_fderiv_symm_p hg, ContinuousLinearMap.comp_id, sub_self]
    unfold ContinuousAt at this; simp only [Pi.sub_apply] at this
    rw [e] at this; exact this
  have h2 : Tendsto (fun x => (S.g x (S.T x)).comp (G.Dexp (N.Φ.symm x)) - S.g p (S.T p))
      (𝓝 p) (𝓝 0) := by
    have := (hgT.clm_comp hD).sub (continuousAt_const (y := S.g p (S.T p)))
    have e : (S.g p (S.T p)).comp (G.Dexp (N.Φ.symm p)) - S.g p (S.T p) = 0 := by
      rw [N.lb_symm_p, G.lb_Dexp_zero hg, ContinuousLinearMap.comp_id, sub_self]
    unfold ContinuousAt at this; simp only [Pi.sub_apply] at this
    rw [e] at this; exact this
  have h3 : ∀ᶠ x in 𝓝 p, ‖fderiv ℝ N.Φ.symm x - ContinuousLinearMap.id ℝ V‖ < 1 := by
    have := hA.tendsto; rw [N.lb_fderiv_symm_p hg] at this
    exact (tendsto_iff_norm_sub_tendsto_zero.1 this).eventually (eventually_lt_nhds one_pos)
  have hη' : ‖(0 : V →L[ℝ] ℝ)‖ < η := by rw [norm_zero]; exact hη
  filter_upwards [N.lb_good_nhds, h3, h1.norm.eventually (eventually_lt_nhds hη'),
    h2.norm.eventually (eventually_lt_nhds hη')] with x hx1 hx2 hx3 hx4
  refine ⟨hx1, ?_, hx3.le, hx4.le⟩
  calc ‖fderiv ℝ N.Φ.symm x‖
      = ‖(fderiv ℝ N.Φ.symm x - ContinuousLinearMap.id ℝ V) + ContinuousLinearMap.id ℝ V‖ := by
        rw [sub_add_cancel]
    _ ≤ ‖fderiv ℝ N.Φ.symm x - ContinuousLinearMap.id ℝ V‖ + ‖ContinuousLinearMap.id ℝ V‖ :=
        norm_add_le _ _
    _ ≤ 1 + 1 := add_le_add hx2.le ContinuousLinearMap.norm_id_le
    _ = 2 := by norm_num

/-- A function `C¹` on the good set, composed with a Lipschitz curve in the normal ball, is
Lipschitz on every `[0,b] ⊆ [0,1]`. -/
theorem lb_comp_lip {f : V → ℝ} (hf : ∀ x ∈ N.good, ContDiffAt ℝ 1 f x) {γ : ℝ → V}
    {K : ℝ≥0} {R : ℝ} (hB : closedBall p R ⊆ N.good) (hlip : LipschitzOnWith K γ (Icc 0 1))
    (hmem : ∀ t ∈ Icc (0 : ℝ) 1, γ t ∈ closedBall p R) {b : ℝ} (hb : b ≤ 1) :
    ∃ K', LipschitzOnWith K' (fun t => f (γ t)) (Icc 0 b) := by
  obtain ⟨Kf, hKf⟩ := ContDiffOn.exists_lipschitzOnWith
    (fun x hx => (hf x (hB hx)).contDiffWithinAt) one_ne_zero (convex_closedBall p R)
    (isCompact_closedBall p R)
  exact ⟨Kf * K, (hKf.comp hlip (fun t ht => hmem t ht)).mono (Icc_subset_Icc le_rfl hb)⟩

/-- **① The small-`t` argument for a merely Lipschitz start.** A Lipschitz curve from `p` in the
normal ball, with velocity a.e. in the closed future cone and avoiding `p` on `(0,1]`, has
`P(γ t) ∈ CC` on some `(0, ε]`. No initial direction is assumed.

Time is measured by the normal-coordinate time `a(t) = −g_p(exp_p⁻¹ γ(t), T p)` (it agrees with
the registered `T`-arclength `s(t)` to first order). With the cone constant `c`
(`lb_cone_const`) and the expansion of `exp⁻¹` at `p` to accuracy `c/30` (`lb_expansion`), on
`[0, ε]`: `a′ ≥ (29/30)(−g(γ′,T))` a.e.; `c ‖exp⁻¹ γ(t)‖ ≤ 3 a(t)` (so `a > 0` on `(0,ε]`);
`−g(P,T) ≥ (9/10) a`; `Q ≤ r₀ a²`. The near-conoid estimate then gives
`(Q∘γ)′ ≤ (6/5) r a a′` from `Q ≤ r a²`, so `Q ≤ (3/5) r a²`; iterating, `Q ≤ 0`. -/
theorem lb_small_t (hg : ContDiff ℝ 2 S.g) {γ : ℝ → V} {K : ℝ≥0} {R : ℝ}
    (hB : closedBall p R ⊆ N.good) (hlip : LipschitzOnWith K γ (Icc 0 1))
    (hmem : ∀ t ∈ Icc (0 : ℝ) 1, γ t ∈ closedBall p R) (h0 : γ 0 = p)
    (hne : ∀ t ∈ Ioc (0 : ℝ) 1, γ t ≠ p)
    (hcausal : ∀ᵐ t ∂(volume : Measure ℝ), t ∈ Ioo (0 : ℝ) 1 → DifferentiableAt ℝ γ t →
      deriv γ t ∈ S.CC (γ t)) :
    ∃ ε > (0 : ℝ), ε ≤ 1 ∧ ∀ t ∈ Ioc (0 : ℝ) ε, N.P (γ t) ∈ S.CC (γ t) := by
  have hp : p ∈ N.good := mem_of_mem_nhds N.lb_good_nhds
  have hpM : p ∈ S.M := N.lb_good_mem_M hg hp
  obtain ⟨rc, hrc, c, hc, -, hcone⟩ := S.lb_cone_const hpM
  have hgood : ∀ t ∈ Icc (0 : ℝ) 1, γ t ∈ N.good := fun t ht => hB (hmem t ht)
  have hU := (N.lb_expansion hg (η := c / 30) (by positivity)).and
    (show ∀ᶠ x in 𝓝 p, x ∈ closedBall p rc from closedBall_mem_nhds p hrc)
  obtain ⟨e, he, hUe⟩ := Metric.mem_nhds_iff.1 hU
  obtain ⟨δ, hδ, hγδ⟩ :=
    Metric.continuousWithinAt_iff.1 (hlip.continuousOn 0 ⟨le_rfl, zero_le_one⟩) e he
  set ε := min (δ / 2) 1 with hεdef
  have hε0 : 0 < ε := lt_min (by linarith) one_pos
  have hε1 : ε ≤ 1 := min_le_right _ _
  have hεI : ∀ t ∈ Icc (0 : ℝ) ε, t ∈ Icc (0 : ℝ) 1 := fun t ht => ⟨ht.1, ht.2.trans hε1⟩
  have hball : ∀ t ∈ Icc (0 : ℝ) ε, γ t ∈ ball p e := by
    intro t ht
    rw [mem_ball, ← h0]
    apply hγδ (hεI t ht)
    rw [Real.dist_eq, sub_zero, abs_of_nonneg ht.1]
    linarith [ht.2, min_le_left (δ / 2) 1]
  set L : V →L[ℝ] ℝ := S.g p (S.T p) with hLdef
  have hσ0 : N.Φ.symm (γ 0) = 0 := by rw [h0, N.lb_symm_p]
  -- differentiability bookkeeping
  have hdiff : ∀ᵐ t ∂(volume : Measure ℝ), t ∈ Ioo (0 : ℝ) ε →
      DifferentiableAt ℝ γ t ∧ deriv γ t ∈ S.CC (γ t) := by
    filter_upwards [hcausal, hlip.ae_differentiableWithinAt_of_mem (μ := volume)]
      with t h1 h2 ht
    have ht01 : t ∈ Ioo (0 : ℝ) 1 := ⟨ht.1, ht.2.trans_le hε1⟩
    have hd : DifferentiableAt ℝ γ t :=
      (h2 (Ioo_subset_Icc_self ht01)).differentiableAt (Icc_mem_nhds ht01.1 ht01.2)
    exact ⟨hd, h1 ht01 hd⟩
  have hσd : ∀ t ∈ Ioo (0 : ℝ) ε, DifferentiableAt ℝ γ t →
      HasDerivAt (fun s => N.Φ.symm (γ s)) (fderiv ℝ N.Φ.symm (γ t) (deriv γ t)) t :=
    fun t ht hd => ((hgood t (hεI t (Ioo_subset_Icc_self ht))).2.differentiableAt
      one_ne_zero).hasFDerivAt.comp_hasDerivAt t hd.hasDerivAt
  have had : ∀ t ∈ Ioo (0 : ℝ) ε, DifferentiableAt ℝ γ t →
      HasDerivAt (fun s => -L (N.Φ.symm (γ s))) (-L (fderiv ℝ N.Φ.symm (γ t) (deriv γ t))) t :=
    fun t ht hd => (L.hasFDerivAt.comp_hasDerivAt t (hσd t ht hd)).neg
  -- (K1) the pointwise estimates at differentiability points
  have hkey : ∀ t ∈ Ioo (0 : ℝ) ε, deriv γ t ∈ S.CC (γ t) →
      0 ≤ -S.g (γ t) (deriv γ t) (S.T (γ t)) ∧
      29 / 30 * (-S.g (γ t) (deriv γ t) (S.T (γ t))) ≤
        -L (fderiv ℝ N.Φ.symm (γ t) (deriv γ t)) ∧
      c * ‖fderiv ℝ N.Φ.symm (γ t) (deriv γ t)‖ ≤ 2 * (-S.g (γ t) (deriv γ t) (S.T (γ t))) := by
    intro t ht hw
    obtain ⟨⟨-, hA2, hl1, -⟩, hrc'⟩ := hUe (hball t (Ioo_subset_Icc_self ht))
    have hcw := hcone (γ t) hrc' (deriv γ t) hw
    have hwn := norm_nonneg (deriv γ t)
    have h1 : |L (fderiv ℝ N.Φ.symm (γ t) (deriv γ t)) - S.g (γ t) (S.T (γ t)) (deriv γ t)| ≤
        c / 30 * ‖deriv γ t‖ := by
      have := ((S.g p (S.T p)).comp (fderiv ℝ N.Φ.symm (γ t)) -
        S.g (γ t) (S.T (γ t))).le_opNorm (deriv γ t)
      rw [← Real.norm_eq_abs]
      calc _ = ‖((S.g p (S.T p)).comp (fderiv ℝ N.Φ.symm (γ t)) -
            S.g (γ t) (S.T (γ t))) (deriv γ t)‖ := by simp [hLdef]
        _ ≤ _ := this
        _ ≤ c / 30 * ‖deriv γ t‖ := by gcongr
    rw [S.symm (γ t) (S.T (γ t))] at h1
    have h2 : ‖fderiv ℝ N.Φ.symm (γ t) (deriv γ t)‖ ≤ 2 * ‖deriv γ t‖ :=
      ((fderiv ℝ N.Φ.symm (γ t)).le_opNorm _).trans (by gcongr)
    have h1' := (abs_le.1 h1).2
    refine ⟨by nlinarith [mul_nonneg hc.le hwn], by linarith, ?_⟩
    nlinarith [mul_le_mul_of_nonneg_left h2 hc.le]
  -- (K2) `c ‖exp⁻¹ γ t‖ ≤ 3 a(t)` on `[0, ε]`
  have hσa : ∀ t ∈ Icc (0 : ℝ) ε, c * ‖N.Φ.symm (γ t)‖ ≤ 3 * -L (N.Φ.symm (γ t)) := by
    intro t ht
    obtain ⟨ℓ, hℓ1, hℓ⟩ := exists_dual_vector'' ℝ (N.Φ.symm (γ t))
    have hf : ∀ x ∈ N.good, ContDiffAt ℝ 1 (fun y => c * ℓ (N.Φ.symm y) + 3 * L (N.Φ.symm y)) x :=
      fun x hx => (contDiffAt_const.mul (ℓ.contDiff.contDiffAt.comp x hx.2)).add
        (contDiffAt_const.mul (L.contDiff.contDiffAt.comp x hx.2))
    obtain ⟨K', hK'⟩ := N.lb_comp_lip hf hB hlip hmem hε1
    have hcmp := lb_le_start_of_ae_deriv hK' (by
      filter_upwards [hdiff] with s hs hsI
      obtain ⟨hd, hw⟩ := hs hsI
      obtain ⟨hb0, ha', hσ'⟩ := hkey s hsI hw
      refine ⟨_, ((ℓ.hasFDerivAt.comp_hasDerivAt s (hσd s hsI hd)).const_mul c).add
        ((L.hasFDerivAt.comp_hasDerivAt s (hσd s hsI hd)).const_mul 3), ?_⟩
      have hℓv : ℓ (fderiv ℝ N.Φ.symm (γ s) (deriv γ s)) ≤
          ‖fderiv ℝ N.Φ.symm (γ s) (deriv γ s)‖ := by
        have := ℓ.le_opNorm (fderiv ℝ N.Φ.symm (γ s) (deriv γ s))
        have h3 := le_abs_self (ℓ (fderiv ℝ N.Φ.symm (γ s) (deriv γ s)))
        rw [← Real.norm_eq_abs] at h3
        nlinarith [norm_nonneg (fderiv ℝ N.Φ.symm (γ s) (deriv γ s))]
      nlinarith [mul_le_mul_of_nonneg_left hℓv hc.le]) t ht
    have hℓ0 : ℓ 0 = 0 := _root_.map_zero ℓ
    have hL0 : L 0 = 0 := _root_.map_zero L
    simp only [hσ0, hℓ0, hL0, mul_zero, add_zero, hℓ, RCLike.ofReal_real_eq_id, id] at hcmp
    linarith
  -- (K3) `a > 0` on `(0, ε]`
  have hapos : ∀ t ∈ Ioc (0 : ℝ) ε, 0 < -L (N.Φ.symm (γ t)) := by
    intro t ht
    have hne' : N.Φ.symm (γ t) ≠ 0 := fun h =>
      hne t ⟨ht.1, ht.2.trans hε1⟩ (N.lb_eq_p_of_symm (hgood t ⟨ht.1.le, ht.2.trans hε1⟩) h)
    have := hσa t ⟨ht.1.le, ht.2⟩
    have := mul_pos hc (norm_pos_iff.2 hne')
    linarith
  -- (K4) `−g(P,T) ≥ (9/10) a`
  have hPT : ∀ t ∈ Icc (0 : ℝ) ε,
      9 / 10 * -L (N.Φ.symm (γ t)) ≤ -S.g (γ t) (N.P (γ t)) (S.T (γ t)) := by
    intro t ht
    obtain ⟨⟨hx, -, -, hl2⟩, -⟩ := hUe (hball t ht)
    have hsa := hσa t ht
    have hP : N.P (γ t) = G.Dexp (N.Φ.symm (γ t)) (N.Φ.symm (γ t)) :=
      (G.lb_Dexp_radial hg (N.lb_good_dom hx)).symm
    have h1 : |S.g (γ t) (S.T (γ t)) (N.P (γ t)) - L (N.Φ.symm (γ t))| ≤
        c / 30 * ‖N.Φ.symm (γ t)‖ := by
      have := ((S.g (γ t) (S.T (γ t))).comp (G.Dexp (N.Φ.symm (γ t))) -
        S.g p (S.T p)).le_opNorm (N.Φ.symm (γ t))
      rw [← Real.norm_eq_abs]
      calc _ = ‖((S.g (γ t) (S.T (γ t))).comp (G.Dexp (N.Φ.symm (γ t))) -
            S.g p (S.T p)) (N.Φ.symm (γ t))‖ := by simp [hLdef, hP]
        _ ≤ _ := this
        _ ≤ c / 30 * ‖N.Φ.symm (γ t)‖ := by gcongr
    rw [S.symm (γ t) (S.T (γ t))] at h1
    have h1' := (abs_le.1 h1).2
    nlinarith
  -- (K5) the base bound `Q ≤ r₀ a²`
  set r₀ := ‖S.g p‖ * (3 / c) ^ 2 with hr₀
  have hbase : ∀ t ∈ Icc (0 : ℝ) ε, N.Q (γ t) ≤ r₀ * (-L (N.Φ.symm (γ t)) * -L (N.Φ.symm (γ t))) := by
    intro t ht
    set σ := N.Φ.symm (γ t)
    have h2 : N.Q (γ t) ≤ ‖S.g p‖ * ‖σ‖ ^ 2 := by
      show S.g p σ σ ≤ _
      have a1 := (S.g p σ).le_opNorm σ
      have a2 := (S.g p).le_opNorm σ
      have a3 := le_abs_self (S.g p σ σ)
      rw [← Real.norm_eq_abs] at a3
      calc _ ≤ _ := a3
        _ ≤ _ := a1
        _ ≤ ‖S.g p‖ * ‖σ‖ * ‖σ‖ := by gcongr
        _ = _ := by ring
    have h3 : ‖σ‖ ≤ 3 / c * -L σ := by
      rw [div_mul_eq_mul_div, le_div_iff₀ hc]; linarith [hσa t ht]
    have h4 : ‖σ‖ ^ 2 ≤ (3 / c * -L σ) ^ 2 := pow_le_pow_left₀ (norm_nonneg _) h3 2
    calc _ ≤ _ := h2
      _ ≤ ‖S.g p‖ * (3 / c * -L σ) ^ 2 := by gcongr
      _ = _ := by rw [hr₀]; ring
  -- (K6) the improvement step `Q ≤ r a² ⟹ Q ≤ (3/5) r a²`
  have hstep : ∀ r : ℝ, 0 ≤ r →
      (∀ t ∈ Icc (0 : ℝ) ε, N.Q (γ t) ≤ r * (-L (N.Φ.symm (γ t)) * -L (N.Φ.symm (γ t)))) →
      ∀ t ∈ Icc (0 : ℝ) ε,
        N.Q (γ t) ≤ (3 / 5 * r) * (-L (N.Φ.symm (γ t)) * -L (N.Φ.symm (γ t))) := by
    intro r hr hQr t ht
    have hf : ∀ x ∈ N.good, ContDiffAt ℝ 1
        (fun y => N.Q y - 3 / 5 * r * (-L (N.Φ.symm y) * -L (N.Φ.symm y))) x := by
      intro x hx
      have hτ : ContDiffAt ℝ 1 (fun y => -L (N.Φ.symm y)) x :=
        (L.contDiff.contDiffAt.comp x hx.2).neg
      exact (N.lb_Q_contDiffAt hx).sub (contDiffAt_const.mul (hτ.mul hτ))
    obtain ⟨K', hK'⟩ := N.lb_comp_lip hf hB hlip hmem hε1
    have hcmp := lb_le_start_of_ae_deriv hK' (by
      filter_upwards [hdiff] with s hs hsI
      obtain ⟨hd, hw⟩ := hs hsI
      obtain ⟨hb0, ha', -⟩ := hkey s hsI hw
      have hsI' : s ∈ Icc (0 : ℝ) ε := Ioo_subset_Icc_self hsI
      have hx := hgood s (hεI s hsI')
      have hQd := N.lb_Q_comp_hasDerivAt hg hd.hasDerivAt hx
      refine ⟨_, hQd.sub (((had s hsI hd).mul (had s hsI hd)).const_mul (3 / 5 * r)), ?_⟩
      set a := -L (N.Φ.symm (γ s))
      set a' := -L (fderiv ℝ N.Φ.symm (γ s) (deriv γ s))
      set b := -S.g (γ s) (deriv γ s) (S.T (γ s))
      set Gw := S.g (γ s) (N.P (γ s)) (deriv γ s)
      set Nt := -S.g (γ s) (N.P (γ s)) (S.T (γ s))
      have ha := hapos s ⟨hsI.1, hsI.2.le⟩
      have hN := hPT s hsI'
      have hest := S.lb_near_conoid (N.lb_good_mem_M hg hx) (N.P (γ s)) hw
      rw [N.lb_P_energy hg hx] at hest
      have hQs := hQr s hsI'
      have ha'0 : 0 ≤ a' := by linarith
      have hra : 0 ≤ r * a * a' := by positivity
      rcases le_or_gt Gw 0 with hn | hpos
      · nlinarith
      · have i1 : 9 / 10 * a * (2 * Gw) ≤ Nt * (2 * Gw) :=
          mul_le_mul_of_nonneg_right hN (by linarith)
        have i3 : b * N.Q (γ s) ≤ b * (r * (a * a)) := mul_le_mul_of_nonneg_left hQs hb0
        have i4 : b * (r * (a * a)) ≤ 30 / 29 * a' * (r * (a * a)) :=
          mul_le_mul_of_nonneg_right (by linarith) (by positivity)
        have i5 : a * (9 / 5 * Gw) ≤ a * (30 / 29 * r * a * a') := by
          have : 2 * Nt * Gw = Nt * (2 * Gw) := by ring
          nlinarith
        have i6 := le_of_mul_le_mul_left i5 ha
        nlinarith) t ht
    have e0 : N.Q (γ 0) = 0 := by rw [h0, N.lb_Q_p]
    have hL0 : L 0 = 0 := _root_.map_zero L
    simp only [e0, hσ0, hL0, neg_zero, mul_zero, sub_zero] at hcmp
    linarith
  have hiter : ∀ n : ℕ, ∀ t ∈ Icc (0 : ℝ) ε,
      N.Q (γ t) ≤ (r₀ * (3 / 5) ^ n) * (-L (N.Φ.symm (γ t)) * -L (N.Φ.symm (γ t))) := by
    intro n
    induction n with
    | zero => intro t ht; simpa using hbase t ht
    | succ n ih =>
      intro t ht
      have := hstep _ (by positivity) ih t ht
      rw [pow_succ]; linarith
  have hQle : ∀ t ∈ Icc (0 : ℝ) ε, N.Q (γ t) ≤ 0 := by
    intro t ht
    have hlim : Tendsto (fun n : ℕ => r₀ * (3 / 5 : ℝ) ^ n *
        (-L (N.Φ.symm (γ t)) * -L (N.Φ.symm (γ t)))) atTop (𝓝 0) := by
      have := ((tendsto_pow_atTop_nhds_zero_of_lt_one (by norm_num : (0 : ℝ) ≤ 3 / 5)
        (by norm_num)).const_mul r₀).mul_const (-L (N.Φ.symm (γ t)) * -L (N.Φ.symm (γ t)))
      simpa using this
    exact ge_of_tendsto' hlim (fun n => hiter n t ht)
  refine ⟨ε, hε0, hε1, fun t ht => ?_⟩
  have hx := hgood t ⟨ht.1.le, ht.2.trans hε1⟩
  rw [N.lb_P_mem_CC_iff hg hx]
  have := hPT t ⟨ht.1.le, ht.2⟩
  have := hapos t ht
  exact ⟨hQle t ⟨ht.1.le, ht.2⟩, by linarith⟩

/-- **① Causal curves from `p` stay in the closed future conoid — Lipschitz start.** Campaign 76's
`cb_causal_in_conoid` with its `C¹`-start hypotheses (`u`, `hu`, `hd0`, `hC1`) **removed**: a
Lipschitz curve from `p` in the normal ball, with velocity a.e. in the closed future cone, avoiding
`p` on `(0,1]`, has `P(γ t) ∈ CC` and `g(P,T) < 0` on `(0,1]`, and `Q ∘ γ ≤ 0` on `[0,1]`.
(`lb_small_t` on `(0,ε]`, then `lb_bootstrap` from `ε`.) -/
theorem lb_causal_in_conoid (hg : ContDiff ℝ 2 S.g) {γ : ℝ → V} {K : ℝ≥0} {R : ℝ}
    (hB : closedBall p R ⊆ N.good) (hlip : LipschitzOnWith K γ (Icc 0 1))
    (hmem : ∀ t ∈ Icc (0 : ℝ) 1, γ t ∈ closedBall p R) (h0 : γ 0 = p)
    (hne : ∀ t ∈ Ioc (0 : ℝ) 1, γ t ≠ p)
    (hcausal : ∀ᵐ t ∂(volume : Measure ℝ), t ∈ Ioo (0 : ℝ) 1 → DifferentiableAt ℝ γ t →
      deriv γ t ∈ S.CC (γ t)) :
    (∀ t ∈ Ioc (0 : ℝ) 1, N.P (γ t) ∈ S.CC (γ t) ∧ S.g (γ t) (N.P (γ t)) (S.T (γ t)) < 0) ∧
      ∀ t ∈ Icc (0 : ℝ) 1, N.Q (γ t) ≤ 0 := by
  obtain ⟨ε, hε0, hε1, hsmall⟩ := N.lb_small_t hg hB hlip hmem h0 hne hcausal
  have hgood : ∀ t ∈ Icc (0 : ℝ) 1, γ t ∈ N.good := fun t ht => hB (hmem t ht)
  have h1 : ∀ t ∈ Ioc (0 : ℝ) 1,
      N.P (γ t) ∈ S.CC (γ t) ∧ S.g (γ t) (N.P (γ t)) (S.T (γ t)) < 0 := by
    intro t ht
    rcases le_or_gt t ε with hte | hte
    · have hP := hsmall t ⟨ht.1, hte⟩
      exact ⟨hP, N.lb_P_T_neg hg (hgood t ⟨ht.1.le, ht.2⟩) (hne t ht) hP⟩
    · exact N.lb_bootstrap hg hB hlip hmem hcausal ⟨hε0.le, hε1⟩
        (fun s hs => hne s ⟨hε0.trans_le hs.1, hs.2⟩) (hsmall ε ⟨hε0, le_rfl⟩) t ⟨hte.le, ht.2⟩
  refine ⟨h1, fun t ht => ?_⟩
  rcases ht.1.eq_or_lt with e | hlt
  · rw [← e, h0, N.lb_Q_p]
  · exact ((N.lb_P_mem_CC_iff hg (hgood t ht)).1 (h1 t ⟨hlt, ht.2⟩).1).1

/-- **① Generators of `𝓗⁺` from `p` are null geodesics — Lipschitz start.** Campaign 76's
`cb_H_generator_null_geodesic` with `u`, `hu`, `hd0`, `hC1` **removed**. Hypotheses: a Lipschitz
curve from `p` in a small normal ball, velocity a.e. in the closed future cone, avoiding `p` on
`(0,1]`, contained in `H = ∂J⁻(J)`. Conclusion: `Q ∘ γ = 0` and `γ` reparametrises one `C²`
radial null geodesic, null and pregeodesic on `(0,1)`. -/
theorem lb_H_generator_null_geodesic (hg : ContDiff ℝ 2 S.g) (J : Set V) {γ : ℝ → V}
    {K : ℝ≥0} {R : ℝ} (hB : closedBall p R ⊆ N.good)
    (hsmall : ∀ x ∈ closedBall p R, N.Φ.symm x ∈ ball (0 : V) (G.ρ / 3))
    (hlip : LipschitzOnWith K γ (Icc 0 1)) (hmem : ∀ t ∈ Icc (0 : ℝ) 1, γ t ∈ closedBall p R)
    (h0 : γ 0 = p) (hne : ∀ t ∈ Ioc (0 : ℝ) 1, γ t ≠ p)
    (hcausal : ∀ᵐ t ∂(volume : Measure ℝ), t ∈ Ioo (0 : ℝ) 1 → DifferentiableAt ℝ γ t →
      deriv γ t ∈ S.CC (γ t))
    (hH : ∀ t ∈ Icc (0 : ℝ) 1, γ t ∈ S.H J) :
    (∀ t ∈ Icc (0 : ℝ) 1, N.Q (γ t) = 0) ∧
    ∃ v ∈ ball (0 : V) G.ρ, ContDiff ℝ 2 (G.radC2 v) ∧
      (∀ t ∈ Icc (0 : ℝ) 1, ∃ r ∈ Icc (0 : ℝ) 1, γ t = G.radC2 v r) ∧
      (∀ t ∈ Ioo (0 : ℝ) 1,
        S.g (G.radC2 v t) (deriv (G.radC2 v) t) (deriv (G.radC2 v) t) = 0) ∧
      S.IsPregeodesicOn (G.radC2 v) (Ioo 0 1) := by
  obtain ⟨hcone, -⟩ := N.lb_causal_in_conoid hg hB hlip hmem h0 hne hcausal
  have hQ := N.lb_generator_Q_zero hg J hB hsmall hmem h0 hne (fun t ht => (hcone t ht).1) hH
  have h1 : (1 : ℝ) ∈ Ioc (0 : ℝ) 1 := ⟨one_pos, le_rfl⟩
  have h1' : (1 : ℝ) ∈ Icc (0 : ℝ) 1 := ⟨zero_le_one, le_rfl⟩
  have hx1 := hB (hmem 1 h1')
  have hfut := (N.lb_orient_chart hg hx1 (hne 1 h1) (hQ 1 h1').le).2 (hcone 1 h1).2
  refine ⟨hQ, N.lb_H_generator_radial_pregeodesic hg J hB hlip hmem h0 hQ hne ?_ hfut hH⟩
  filter_upwards [hcausal] with t ht htI hd
  exact (ht htI hd).1

/-! ## Campaign 77 (new): ② the tangent hyperplane of `𝓗⁺` at a generator point -/

/-- **② `𝓗⁺` lies on the outer side `{Q ≥ 0}` of the conoid near a generator point.** At
`x ≠ p` with `Q x = 0`, `P x` future, `exp⁻¹ x` small, and `p ∈ H J`: every point of `H J` near
`x` has `Q ≥ 0` (a point with `Q < 0` near `x` has future, small `exp⁻¹`, so lies in `I⁺(p)` by
`lb_chr_of_Q_neg`, which achronality `lb_H_achronal` forbids). -/
theorem lb_H_Q_nonneg_near (hg : ContDiff ℝ 2 S.g) (J : Set V) {x : V} (hx : x ∈ N.good)
    (hQ : N.Q x = 0) (hfut : S.g x (N.P x) (S.T x) < 0)
    (hsmall : N.Φ.symm x ∈ ball (0 : V) (G.ρ / 3)) (hp : p ∈ S.H J) :
    ∀ᶠ y in 𝓝 x, y ∈ S.H J → 0 ≤ N.Q y := by
  have hxp : x ≠ p := by
    intro h; rw [h, N.lb_P_p hg] at hfut; simp at hfut
  have hfut0 : S.g p (N.Φ.symm x) (S.T p) < 0 := (N.lb_orient_chart hg hx hxp hQ.le).2 hfut
  have hcont : ContinuousAt (fun y => S.g p (N.Φ.symm y) (S.T p)) x :=
    (continuousAt_const.clm_apply hx.2.continuousAt).clm_apply continuousAt_const
  filter_upwards [N.lb_good_isOpen.mem_nhds hx, hcont.eventually (eventually_lt_nhds hfut0),
    hx.2.continuousAt.preimage_mem_nhds (isOpen_ball.mem_nhds hsmall)] with y hy1 hy2 hy3 hyH
  by_contra hneg
  rw [not_le] at hneg
  exact S.lb_H_achronal J hp hyH (N.lb_chr_of_Q_neg hg hy1 hneg hy2 hy3)

/-- **② The tangent hyperplane (one-sided form).** Under the hypotheses of `lb_H_Q_nonneg_near`,
every curve `c` with `c 0 = x`, differentiable at `0` with velocity `c′`, and `c t ∈ H J` for `t`
near `0`, satisfies `DQ(x)(c′) = 0`, i.e. `g_x(P x, c′) = 0`: `c′` lies in the null hyperplane
`P(x)^⊥` (`P x` is future null, `lb_conoid_regular`). (`Q ∘ c` has a local minimum `0` at `0`.) -/
theorem lb_tangent_hyperplane (hg : ContDiff ℝ 2 S.g) (J : Set V) {x : V} (hx : x ∈ N.good)
    (hQ : N.Q x = 0) (hfut : S.g x (N.P x) (S.T x) < 0)
    (hsmall : N.Φ.symm x ∈ ball (0 : V) (G.ρ / 3)) (hp : p ∈ S.H J)
    {c : ℝ → V} {c' : V} (hc : HasDerivAt c c' 0) (hc0 : c 0 = x)
    (hcH : ∀ᶠ t in 𝓝 (0 : ℝ), c t ∈ S.H J) :
    fderiv ℝ N.Q x c' = 0 ∧ S.g x (N.P x) c' = 0 := by
  have hev := N.lb_H_Q_nonneg_near hg J hx hQ hfut hsmall hp
  have hcc : Tendsto c (𝓝 0) (𝓝 x) := by rw [← hc0]; exact hc.continuousAt
  have hmin : IsLocalMin (fun t => N.Q (c t)) 0 := by
    filter_upwards [hcc.eventually hev, hcH] with t h1 h2
    rw [hc0, hQ]; exact h1 h2
  have hx' : c 0 ∈ N.good := by rw [hc0]; exact hx
  have hD := N.lb_Q_comp_hasDerivAt hg hc hx'
  have h0 := hmin.hasDerivAt_eq_zero hD
  rw [hc0] at h0
  have h2 : S.g x (N.P x) c' = 0 := by linarith
  refine ⟨?_, h2⟩
  rw [(N.lb_grad_Q hg hx).fderiv]
  simp [h2]

/-- **② along a generator.** Under the hypotheses of `lb_H_generator_null_geodesic`, at every
`t ∈ (0,1]`: `P(γ t)` is a nonzero future null vector, and every curve in `H J` through `γ t`
(differentiable at the crossing) has velocity `g`-orthogonal to `P(γ t)`. So wherever `𝓗⁺` has a
tangent hyperplane at `γ t`, it is the null hyperplane `P(γ t)^⊥ = ker DQ(γ t)` of the generator. -/
theorem lb_generator_tangent_hyperplane (hg : ContDiff ℝ 2 S.g) (J : Set V) {γ : ℝ → V}
    {K : ℝ≥0} {R : ℝ} (hB : closedBall p R ⊆ N.good)
    (hsmall : ∀ x ∈ closedBall p R, N.Φ.symm x ∈ ball (0 : V) (G.ρ / 3))
    (hlip : LipschitzOnWith K γ (Icc 0 1)) (hmem : ∀ t ∈ Icc (0 : ℝ) 1, γ t ∈ closedBall p R)
    (h0 : γ 0 = p) (hne : ∀ t ∈ Ioc (0 : ℝ) 1, γ t ≠ p)
    (hcausal : ∀ᵐ t ∂(volume : Measure ℝ), t ∈ Ioo (0 : ℝ) 1 → DifferentiableAt ℝ γ t →
      deriv γ t ∈ S.CC (γ t))
    (hH : ∀ t ∈ Icc (0 : ℝ) 1, γ t ∈ S.H J) {t : ℝ} (ht : t ∈ Ioc (0 : ℝ) 1)
    {c : ℝ → V} {c' : V} (hc : HasDerivAt c c' 0) (hc0 : c 0 = γ t)
    (hcH : ∀ᶠ s in 𝓝 (0 : ℝ), c s ∈ S.H J) :
    S.g (γ t) (N.P (γ t)) c' = 0 ∧ fderiv ℝ N.Q (γ t) c' = 0 ∧ fderiv ℝ N.Q (γ t) ≠ 0 ∧
      S.g (γ t) (N.P (γ t)) (N.P (γ t)) = 0 ∧ S.g (γ t) (N.P (γ t)) (S.T (γ t)) < 0 := by
  obtain ⟨hcone, -⟩ := N.lb_causal_in_conoid hg hB hlip hmem h0 hne hcausal
  have hQ := N.lb_generator_Q_zero hg J hB hsmall hmem h0 hne (fun t ht => (hcone t ht).1) hH
  have htI : t ∈ Icc (0 : ℝ) 1 := ⟨ht.1.le, ht.2⟩
  have hx := hB (hmem t htI)
  have hp : p ∈ S.H J := by rw [← h0]; exact hH 0 ⟨le_rfl, zero_le_one⟩
  obtain ⟨h1, h2⟩ := N.lb_tangent_hyperplane hg J hx (hQ t htI) (hcone t ht).2
    (hsmall _ (hmem t htI)) hp hc hc0 hcH
  exact ⟨h2, h1, (N.lb_conoid_regular hg hx (hne t ht) (hQ t htI)).1,
    by rw [N.lb_P_energy hg hx]; exact hQ t htI, (hcone t ht).2⟩

/-! ## Campaign 77 (new): non-vacuity of the bootstrap hypotheses -/

/-- **Non-vacuity of `lb_causal_in_conoid` / `lb_small_t`.** In every spacetime chart, at every
`p ∈ M` with a normal chart, the hypotheses are jointly satisfied: a short segment
`γ t = p + (t δ) • T p` in the direction of the time orientation lies in a normal ball, is
Lipschitz, starts at `p`, avoids `p` for `t > 0`, and has velocity `δ • T p ∈ CC (γ t)`. -/
theorem lb_nonvacuous (hg : ContDiff ℝ 2 S.g) :
    ∃ R > (0 : ℝ), closedBall p R ⊆ N.good ∧ ∃ γ : ℝ → V, ∃ K : ℝ≥0,
      LipschitzOnWith K γ (Icc 0 1) ∧ (∀ t ∈ Icc (0 : ℝ) 1, γ t ∈ closedBall p R) ∧ γ 0 = p ∧
      (∀ t ∈ Ioc (0 : ℝ) 1, γ t ≠ p) ∧
      (∀ᵐ t ∂(volume : Measure ℝ), t ∈ Ioo (0 : ℝ) 1 → DifferentiableAt ℝ γ t →
        deriv γ t ∈ S.CC (γ t)) := by
  have hp : p ∈ N.good := mem_of_mem_nhds N.lb_good_nhds
  have hpM : p ∈ S.M := N.lb_good_mem_M hg hp
  have hgn : ∀ᶠ y in 𝓝 p, y ∈ N.good := N.lb_good_nhds
  have hTT := S.T_timelike p hpM
  have hc1 : ContinuousAt (fun y => S.g y (S.T p) (S.T p)) p :=
    S.cont_g.continuousAt.clm_apply continuousAt_const |>.clm_apply continuousAt_const
  have hc2 : ContinuousAt (fun y => S.g y (S.T p) (S.T y)) p :=
    S.cont_g.continuousAt.clm_apply continuousAt_const |>.clm_apply S.cont_T.continuousAt
  have hev := (hgn.and (hc1.eventually (eventually_lt_nhds hTT))).and
    (hc2.eventually (eventually_lt_nhds hTT))
  obtain ⟨e, he, hsub⟩ := Metric.mem_nhds_iff.1 hev
  have hT0 : S.T p ≠ 0 := fun h => by rw [h] at hTT; simp at hTT
  have hTn : 0 < ‖S.T p‖ := norm_pos_iff.2 hT0
  set R := e / 2 with hR
  have hR0 : 0 < R := by positivity
  set δ := R / ‖S.T p‖ with hδ
  have hδ0 : 0 < δ := by positivity
  have hδT : δ * ‖S.T p‖ = R := by rw [hδ]; field_simp
  let γ : ℝ → V := fun t => p + (t * δ) • S.T p
  have hγd : ∀ t, HasDerivAt γ (δ • S.T p) t := fun t => by
    have h1 : HasDerivAt (fun x : ℝ => x * δ) δ t := by
      simpa using (hasDerivAt_id t).mul_const δ
    exact (h1.smul_const (S.T p)).const_add p
  have hdist : ∀ t ∈ Icc (0 : ℝ) 1, γ t ∈ closedBall p R := by
    intro t ht
    rw [mem_closedBall, dist_eq_norm]
    simp only [γ, add_sub_cancel_left, norm_smul, Real.norm_eq_abs,
      abs_of_nonneg (mul_nonneg ht.1 hδ0.le)]
    nlinarith [ht.2, mul_le_mul_of_nonneg_right ht.2 (mul_nonneg hδ0.le hTn.le)]
  refine ⟨R, hR0, fun x hx => (hsub (closedBall_subset_ball (by linarith) hx)).1.1, γ,
    Real.toNNReal (δ * ‖S.T p‖), ?_, hdist, by simp [γ], ?_, ?_⟩
  · refine LipschitzWith.lipschitzOnWith (LipschitzWith.of_dist_le_mul fun s t => ?_)
    rw [dist_eq_norm, dist_eq_norm, Real.coe_toNNReal _ (by positivity)]
    simp only [γ, add_sub_add_left_eq_sub, ← sub_smul, norm_smul, Real.norm_eq_abs]
    rw [← sub_mul, abs_mul, abs_of_pos hδ0]; ring_nf; rfl
  · intro t ht h
    have : (t * δ) • S.T p = 0 := by
      have := congrArg (fun y => y - p) h; simpa [γ] using this
    rcases smul_eq_zero.1 this with h1 | h1
    · exact (mul_pos ht.1 hδ0).ne' h1
    · exact hT0 h1
  · refine Filter.Eventually.of_forall fun t ht _ => ?_
    rw [(hγd t).deriv]
    have hx := hsub (closedBall_subset_ball (by linarith) (hdist t (Ioo_subset_Icc_self ht)))
    refine ⟨?_, ?_⟩
    · simp only [map_smul, smul_apply, smul_eq_mul]
      nlinarith [hx.1.2, mul_pos hδ0 hδ0]
    · simp only [map_smul, smul_apply, smul_eq_mul]
      nlinarith [hx.2, hδ0]

end NormalChart

end GeoFlow

end Spacetime

/-! ## Axiom audit -/

-- copied machinery
#print axioms Spacetime.GeoFlow.lb_gauss
#print axioms Spacetime.GeoFlow.lb_expp_localDiffeo
#print axioms Spacetime.GeoFlow.NormalChart.lb_grad_Q
#print axioms Spacetime.GeoFlow.NormalChart.lb_chr_of_Q_neg
#print axioms Spacetime.lb_H_achronal
#print axioms Spacetime.lb_near_conoid
#print axioms Spacetime.GeoFlow.NormalChart.lb_bootstrap
#print axioms Spacetime.GeoFlow.NormalChart.lb_generator_Q_zero
#print axioms Spacetime.GeoFlow.NormalChart.lb_H_generator_radial_pregeodesic
#print axioms Spacetime.GeoFlow.NormalChart.lb_conoid_regular
-- campaign 77, ① Lipschitz-start bootstrap
#print axioms lb_le_start_of_ae_deriv
#print axioms Spacetime.lb_cone_const
#print axioms Spacetime.GeoFlow.NormalChart.lb_expansion
#print axioms Spacetime.GeoFlow.NormalChart.lb_comp_lip
#print axioms Spacetime.GeoFlow.NormalChart.lb_small_t
#print axioms Spacetime.GeoFlow.NormalChart.lb_causal_in_conoid
#print axioms Spacetime.GeoFlow.NormalChart.lb_H_generator_null_geodesic
-- campaign 77, ② tangent hyperplane
#print axioms Spacetime.GeoFlow.NormalChart.lb_H_Q_nonneg_near
#print axioms Spacetime.GeoFlow.NormalChart.lb_tangent_hyperplane
#print axioms Spacetime.GeoFlow.NormalChart.lb_generator_tangent_hyperplane
-- campaign 77, non-vacuity
#print axioms Spacetime.GeoFlow.NormalChart.lb_nonvacuous

end ShadowProbe.LipschitzBootstrapProbe

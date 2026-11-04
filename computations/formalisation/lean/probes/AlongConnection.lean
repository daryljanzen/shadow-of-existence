import Mathlib

/-!
# Probe `r7669+71` (campaign 94), piece ①: `thm:metric-singularity` 1b and `cor:threefold` 2iv-a on ruling 2

Registration: `computations/formalisation/r7669_71_campaign94/PREDICTION.md`, piece ①.
Ruling: `FOR_71.md`, `r7669` (69), ruling 2 — `Δτ` is the temporal leg of the frame adapted to (b)'s
foliation: along `γ`, `g = h − N² dt ⊗ dt` with the lapse `N ≥ 0` allowed to vanish,
`Δx := ∫₀¹ √(h(γ′, γ′))`, `Δτ := ∫₀¹ N |dt(γ′)|`.

This file imports no other probe. Its manifold layer is the `MSpacetime` structure (with `gE` and the
`mfderiv` velocity `vel`) copied from campaign 92's `HorizonStretch.lean`; everything else of that file
(the chart spacetimes, the `OneChart` kit, the causal relations, the horizon material) is trimmed.

* **BUILT** `ac_metric_singularity_along` — on any `MSpacetime` over any manifold, along any curve with an
  adapted splitting on `[0, 1]`: (a) `g(γ′, γ′) = 0` on `[0, 1]`, (b) `Δx = 0`, and continuity of
  `s ↦ h s (γ′ s) (γ′ s)` on `[0, 1]` give `Δτ = 0` and `n s · dt s (γ′ s) = 0` on `[0, 1]`.
  The registered expected stop (`Δx = 0 ⇒ h(γ′, γ′) = 0` pointwise) is passed with
  `intervalIntegral.integral_pos`, on the continuity hypothesis as registered.
* **BUILT** `ac_lapse_pos_forces_point` — with `n > 0` on `[0, 1]` and `h s` positive definite on
  `ker dt s`, (a) and (b) force `γ′ = 0` on `[0, 1]`, and (for `γ` manifold-differentiable on `[0, 1]`)
  `γ 1 = γ 0`, on the manifold itself (via `ac_const_of_vel_zero`: a chart-local mean-value bound and the
  connectedness of `[0, 1]`; no Hausdorff hypothesis on `N`).
* **BUILT** `ac_witness` — 2D Minkowski in null coordinates, `g = −dU dV`, on the model space; the Rindler
  horizon generator `γ s = (0, eˢ)`, `p = (0, 1) ≠ q = (0, e)`; the boost `χ = V∂_V − U∂_U` with
  `g(χ, χ) = UV`, `χ(γ s) = γ′ s` null and non-zero; the splitting `dt = dV/V`, `n = √(max 0 (−g(χ, χ))) = 0`
  on `γ`, `h = g`; (a), (b), `Δx = 0`, the conclusion `Δτ = 0`, and `∫₀¹ dt(γ′) = 1` (the Killing parameter
  `λ = log V` separates `p` from `q`). `χ` is Killing: its flow `Φ_t(U, V) = (e^{−t}U, e^{t}V)` is linear,
  has `χ` as its generator, and preserves `g` (`ac_boost_isometry`, `ac_boost_generator`).
  Companion corollary `ac_witness_no_positive_lapse`: no adapted splitting with positive lapse exists along
  the witness curve.
* Non-vacuity of the companion: `ac_lapse_pos_nonvacuous` — the standard `t`-splitting `n = 1`,
  `dt = (dU + dV)/2`, `h = dx²` on a constant curve satisfies every hypothesis.
-/

open Set Filter Topology Metric Manifold

noncomputable section

namespace ShadowProbe.AlongConnectionProbe

section Manifold
set_option linter.unusedSectionVars false

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
variable {N : Type*} [TopologicalSpace N] [ChartedSpace E N]

/-! ### The manifold spacetime (copied from `HorizonStretch.lean`) -/

variable (E N) in
/-- **A time-oriented Lorentzian region of a manifold** `N` (intrinsic): an open `M ⊆ N`, a section
`g` of `T*N ⊗ T*N`, symmetric, and a section `T` of `TN`, timelike on `M`, with `g` positive on
`T^⊥` at points of `M`. -/
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

/-- `g_x` read as a bilinear form on `E`. -/
def gE (x : N) : E →L[ℝ] E →L[ℝ] ℝ := S.g x

/-- The velocity `γ'(t) = mfderiv γ t 1 ∈ T_{γ t} N` of a curve `γ : ℝ → N`. -/
noncomputable def vel (γ : ℝ → N) (t : ℝ) : E := mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ t (1 : ℝ)

end MSpacetime

open MSpacetime

/-! ### The adapted splitting along `γ` (ruling 2) -/

/-- **The splitting adapted to (b)'s foliation, along `γ` on `[0, 1]`**: a spatial bilinear form `h s`,
a lapse `n s ≥ 0` (allowed to vanish), and a temporal one-form `dt s`, with
`g_{γ s} = h s − (n s)² dt s ⊗ dt s` and `h s (γ′ s, γ′ s) ≥ 0`. -/
structure AdaptedSplitting (S : MSpacetime E N) (γ : ℝ → N) where
  h : ℝ → E →L[ℝ] E →L[ℝ] ℝ
  n : ℝ → ℝ
  dt : ℝ → E →L[ℝ] ℝ
  n_nonneg : ∀ s ∈ Icc (0:ℝ) 1, 0 ≤ n s
  split : ∀ s ∈ Icc (0:ℝ) 1, S.gE (γ s) = h s - (n s) ^ 2 • (dt s).smulRight (dt s)
  h_nonneg : ∀ s ∈ Icc (0:ℝ) 1, 0 ≤ h s (vel γ s) (vel γ s)

namespace AdaptedSplitting
variable {S : MSpacetime E N} {γ : ℝ → N} (σ : AdaptedSplitting S γ)

/-- `Δx := ∫₀¹ √(h(γ′, γ′))`. -/
def Δx : ℝ := ∫ s in (0:ℝ)..1, √(σ.h s (vel γ s) (vel γ s))

/-- `Δτ := ∫₀¹ n |dt(γ′)|`. -/
def Δτ : ℝ := ∫ s in (0:ℝ)..1, σ.n s * |σ.dt s (vel γ s)|

/-- The line element along `γ`: `g(γ′, γ′) = h(γ′, γ′) − n² dt(γ′)²`. -/
lemma g_vel {s : ℝ} (hs : s ∈ Icc (0:ℝ) 1) :
    S.gE (γ s) (vel γ s) (vel γ s) =
      σ.h s (vel γ s) (vel γ s) - (σ.n s * σ.dt s (vel γ s)) ^ 2 := by
  rw [σ.split s hs]
  simp only [sub_apply, smul_apply,
    ContinuousLinearMap.smulRight_apply, smul_eq_mul]
  ring

end AdaptedSplitting

/-- A function continuous and non-negative on `[0, 1]` with zero integral vanishes on `[0, 1]`. -/
lemma ac_eq_zero_of_integral_eq_zero {f : ℝ → ℝ} (hc : ContinuousOn f (Icc 0 1))
    (hnn : ∀ s ∈ Icc (0:ℝ) 1, 0 ≤ f s) (h0 : ∫ s in (0:ℝ)..1, f s = 0) :
    ∀ s ∈ Icc (0:ℝ) 1, f s = 0 := by
  intro s hs
  by_contra hne
  have hpos : 0 < ∫ s in (0:ℝ)..1, f s :=
    intervalIntegral.integral_pos zero_lt_one hc (fun x hx => hnn x (Ioc_subset_Icc_self hx))
      ⟨s, hs, lt_of_le_of_ne (hnn s hs) (Ne.symm hne)⟩
  linarith

/-- **`thm:metric-singularity`, along-the-connection form, on ruling 2.** (a) `g(γ′, γ′) = 0` on `[0, 1]`,
(b) `Δx = 0`, and continuity of `s ↦ h s (γ′ s) (γ′ s)` on `[0, 1]` give `Δτ = 0`, and
`n s · dt s (γ′ s) = 0` on `[0, 1]` (and `h(γ′, γ′) = 0` there, which is (b) pointwise). -/
theorem ac_metric_singularity_along (S : MSpacetime E N) {γ : ℝ → N} (σ : AdaptedSplitting S γ)
    (ha : ∀ s ∈ Icc (0:ℝ) 1, S.gE (γ s) (vel γ s) (vel γ s) = 0)
    (hb : σ.Δx = 0)
    (hcont : ContinuousOn (fun s => σ.h s (vel γ s) (vel γ s)) (Icc 0 1)) :
    σ.Δτ = 0 ∧ (∀ s ∈ Icc (0:ℝ) 1, σ.n s * σ.dt s (vel γ s) = 0) ∧
      (∀ s ∈ Icc (0:ℝ) 1, σ.h s (vel γ s) (vel γ s) = 0) := by
  have hsq : ∀ s ∈ Icc (0:ℝ) 1, √(σ.h s (vel γ s) (vel γ s)) = 0 :=
    ac_eq_zero_of_integral_eq_zero (Real.continuous_sqrt.comp_continuousOn hcont)
      (fun s _ => Real.sqrt_nonneg _) hb
  have hh : ∀ s ∈ Icc (0:ℝ) 1, σ.h s (vel γ s) (vel γ s) = 0 := fun s hs =>
    le_antisymm (Real.sqrt_eq_zero'.mp (hsq s hs)) (σ.h_nonneg s hs)
  have hnd : ∀ s ∈ Icc (0:ℝ) 1, σ.n s * σ.dt s (vel γ s) = 0 := by
    intro s hs
    have h1 := σ.g_vel hs
    rw [ha s hs, hh s hs] at h1
    have : (σ.n s * σ.dt s (vel γ s)) ^ 2 = 0 := by linarith
    exact pow_eq_zero_iff two_ne_zero |>.mp this
  refine ⟨?_, hnd, hh⟩
  unfold AdaptedSplitting.Δτ
  have hz : ∫ s in (0:ℝ)..1, σ.n s * |σ.dt s (vel γ s)| = ∫ _ in (0:ℝ)..1, (0:ℝ) := by
    refine intervalIntegral.integral_congr fun s hs => ?_
    rw [uIcc_of_le zero_le_one] at hs
    show σ.n s * |σ.dt s (vel γ s)| = 0
    rcases mul_eq_zero.mp (hnd s hs) with h | h <;> simp [h]
  rw [hz]; simp

/-! ### Vanishing velocity on `[0, 1]` forces a constant curve (on the manifold) -/

variable [IsManifold 𝓘(ℝ, E) 1 N]

/-- Near a parameter `t`, in the chart at `γ t`, a curve with vanishing `mfderiv` velocity on `[0, 1]`
is constant on `[0, 1]`. -/
lemma ac_locally_const_of_vel_zero {γ : ℝ → N}
    (hd : ∀ t ∈ Icc (0:ℝ) 1, MDifferentiableAt 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ t)
    (h0 : ∀ t ∈ Icc (0:ℝ) 1, vel (E := E) γ t = 0) {t : ℝ} (ht : t ∈ Icc (0:ℝ) 1) :
    ∃ ε > 0, ∀ u ∈ Icc (0:ℝ) 1, dist u t < ε → γ u = γ t := by
  set φ := extChartAt 𝓘(ℝ, E) (γ t)
  have hev : ∀ᶠ u in 𝓝 t, γ u ∈ (chartAt E (γ t)).source :=
    (hd t ht).continuousAt.preimage_mem_nhds
      ((chartAt E (γ t)).open_source.mem_nhds (mem_chart_source E (γ t)))
  obtain ⟨ε, hε, hball⟩ := Metric.eventually_nhds_iff.mp hev
  refine ⟨ε, hε, fun u hu hut => ?_⟩
  set s := Icc (0:ℝ) 1 ∩ ball t ε
  have hsc : Convex ℝ s := (convex_Icc 0 1).inter (convex_ball t ε)
  have hderiv : ∀ x ∈ s, HasDerivWithinAt (φ ∘ γ) 0 s x := by
    intro x hx
    have hxs : γ x ∈ (chartAt E (γ t)).source := hball hx.2
    have hφ : MDifferentiableAt 𝓘(ℝ, E) 𝓘(ℝ, E) φ (γ x) :=
      mdifferentiableAt_extChartAt (I := 𝓘(ℝ, E)) hxs
    have hcomp : MDifferentiableAt 𝓘(ℝ, ℝ) 𝓘(ℝ, E) (φ ∘ γ) x := hφ.comp x (hd x hx.1)
    have hdiff : DifferentiableAt ℝ (φ ∘ γ) x := mdifferentiableAt_iff_differentiableAt.mp hcomp
    have hfd : fderiv ℝ (φ ∘ γ) x = 0 := by
      refine ContinuousLinearMap.ext_ring ?_
      have e : fderiv ℝ (φ ∘ γ) x 1 = mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, E) (φ ∘ γ) x 1 := by
        rw [mfderiv_eq_fderiv]; rfl
      rw [e, mfderiv_comp x hφ (hd x hx.1), ContinuousLinearMap.comp_apply]
      have : mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ x 1 = 0 := h0 x hx.1
      rw [this, map_zero]; rfl
    have := hdiff.hasFDerivAt
    rw [hfd] at this
    simpa using this.hasDerivAt.hasDerivWithinAt
  have hts : t ∈ s := ⟨ht, mem_ball_self hε⟩
  have hus : u ∈ s := ⟨hu, hut⟩
  have hle := hsc.norm_image_sub_le_of_norm_hasDerivWithin_le (C := 0) hderiv (fun _ _ => by simp) hts hus
  have heq : φ (γ u) = φ (γ t) := by
    have : ‖(φ ∘ γ) u - (φ ∘ γ) t‖ = 0 := le_antisymm (by simpa using hle) (norm_nonneg _)
    simpa [sub_eq_zero] using this
  exact (extChartAt 𝓘(ℝ, E) (γ t)).injOn (by rw [extChartAt_source]; exact hball hut)
    (by rw [extChartAt_source]; exact mem_chart_source E (γ t)) heq

/-- **A curve on a manifold with vanishing `mfderiv` velocity on `[0, 1]` is constant on `[0, 1]`.** -/
theorem ac_const_of_vel_zero {γ : ℝ → N}
    (hd : ∀ t ∈ Icc (0:ℝ) 1, MDifferentiableAt 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ t)
    (h0 : ∀ t ∈ Icc (0:ℝ) 1, vel (E := E) γ t = 0) : ∀ t ∈ Icc (0:ℝ) 1, γ t = γ 0 := by
  have : PreconnectedSpace (Icc (0:ℝ) 1) :=
    Subtype.preconnectedSpace isPreconnected_Icc
  let f : Icc (0:ℝ) 1 → N := fun u => γ u
  have hf : IsLocallyConstant f := by
    rw [IsLocallyConstant.iff_eventually_eq]
    rintro ⟨t, ht⟩
    obtain ⟨ε, hε, h⟩ := ac_locally_const_of_vel_zero hd h0 ht
    rw [Metric.eventually_nhds_iff]
    exact ⟨ε, hε, fun {y} hy => h y.1 y.2 hy⟩
  intro t ht
  exact hf.apply_eq_of_preconnectedSpace ⟨t, ht⟩ ⟨0, left_mem_Icc.mpr zero_le_one⟩

/-- **The companion (`N > 0`).** If the lapse is positive on `[0, 1]` and each `h s` is positive definite
on `ker dt s`, then (a) and (b) (with continuity of the `h`-integrand) force `γ′ = 0` on `[0, 1]`; for `γ`
manifold-differentiable on `[0, 1]`, `γ` is constant there and `γ 1 = γ 0`, so `p = q`. -/
theorem ac_lapse_pos_forces_point (S : MSpacetime E N) {γ : ℝ → N} (σ : AdaptedSplitting S γ)
    (ha : ∀ s ∈ Icc (0:ℝ) 1, S.gE (γ s) (vel γ s) (vel γ s) = 0)
    (hb : σ.Δx = 0)
    (hcont : ContinuousOn (fun s => σ.h s (vel γ s) (vel γ s)) (Icc 0 1))
    (hn : ∀ s ∈ Icc (0:ℝ) 1, 0 < σ.n s)
    (hpd : ∀ s ∈ Icc (0:ℝ) 1, ∀ v : E, v ≠ 0 → σ.dt s v = 0 → 0 < σ.h s v v) :
    (∀ s ∈ Icc (0:ℝ) 1, vel (E := E) γ s = 0) ∧
      ((∀ t ∈ Icc (0:ℝ) 1, MDifferentiableAt 𝓘(ℝ, ℝ) 𝓘(ℝ, E) γ t) → γ 1 = γ 0) := by
  obtain ⟨-, hnd, hh⟩ := ac_metric_singularity_along S σ ha hb hcont
  have hv : ∀ s ∈ Icc (0:ℝ) 1, vel (E := E) γ s = 0 := by
    intro s hs
    have hdt : σ.dt s (vel γ s) = 0 :=
      (mul_eq_zero.mp (hnd s hs)).resolve_left (hn s hs).ne'
    by_contra hne
    have := hpd s hs _ hne hdt
    rw [hh s hs] at this
    exact lt_irrefl _ this
  exact ⟨hv, fun hd => ac_const_of_vel_zero hd hv 1 (right_mem_Icc.mpr zero_le_one)⟩

end Manifold

/-! ### The Rindler-horizon witness: 2D Minkowski in null coordinates -/

namespace Model
open ContinuousLinearMap MSpacetime

set_option synthInstance.maxHeartbeats 400000

/-- Null coordinates `p = (U, V)`. -/
abbrev P := ℝ × ℝ

/-- `g = −dU dV` (symmetrised). -/
def gM : P →L[ℝ] P →L[ℝ] ℝ :=
  (-(1/2 : ℝ)) • ((fst ℝ ℝ ℝ).smulRight (snd ℝ ℝ ℝ) + (snd ℝ ℝ ℝ).smulRight (fst ℝ ℝ ℝ))

lemma gM_apply (v w : P) : gM v w = -(v.1 * w.2 + v.2 * w.1) / 2 := by
  simp [gM]; ring

/-- 2D Minkowski space on the model space `P`, `M = P`, `g = gM`, `T = ∂_t = (1, 1)`. -/
def mink : MSpacetime P P where
  M := univ
  isOpen_M := isOpen_univ
  g := fun _ => gM
  symm := fun _ v w => (by rw [gM_apply, gM_apply]; ring : gM v w = gM w v)
  T := fun _ => ((1 : ℝ), (1 : ℝ))
  T_timelike := fun _ _ => by
    show gM ((1 : ℝ), (1 : ℝ)) ((1 : ℝ), (1 : ℝ)) < 0
    rw [gM_apply]; norm_num
  pos_on_perp := fun _ _ v h hv => by
    change gM v ((1 : ℝ), (1 : ℝ)) = 0 at h
    show 0 < gM v v
    rw [gM_apply] at h ⊢
    have h2 : v.2 = -v.1 := by simp at h; linarith
    have h1 : v.1 ≠ 0 := by
      intro h1; apply hv; ext
      · exact h1
      · rw [h2, h1]; simp
    rw [h2]; nlinarith [sq_pos_of_ne_zero h1]

lemma mink_gE (x : P) : mink.gE x = gM := rfl

/-- On the model space, the `mfderiv` velocity is the ordinary derivative. -/
lemma vel_eq_of_hasDerivAt {γ : ℝ → P} {t : ℝ} {v : P} (h : HasDerivAt γ v t) : vel γ t = v := by
  unfold vel
  rw [mfderiv_eq_fderiv]
  show fderiv ℝ γ t 1 = v
  rw [h.hasFDerivAt.fderiv]
  simp

/-- The boost field `χ = V∂_V − U∂_U`. -/
def χ (x : P) : P := (-x.1, x.2)

/-- `g(χ, χ) = UV`. -/
lemma g_χ_χ (x : P) : gM (χ x) (χ x) = x.1 * x.2 := by
  rw [gM_apply]; simp [χ]; ring

/-- The boost flow `Φ_t(U, V) = (e^{−t}U, e^{t}V)`, linear in `x`. -/
def Φ (t : ℝ) (x : P) : P := (Real.exp (-t) * x.1, Real.exp t * x.2)

/-- `χ` is the generator of `Φ`: `d/dt Φ_t x |_{t=0} = χ x`. -/
theorem ac_boost_generator (x : P) : HasDerivAt (fun t => Φ t x) (χ x) 0 := by
  have h1 : HasDerivAt (fun t => Real.exp (-t) * x.1) (-x.1) 0 := by
    have := ((Real.hasDerivAt_exp (-0)).comp 0 (hasDerivAt_neg 0)).mul_const x.1
    simpa using this
  have h2 : HasDerivAt (fun t => Real.exp t * x.2) x.2 0 := by
    simpa using (Real.hasDerivAt_exp 0).mul_const x.2
  exact h1.prodMk h2

/-- `χ` is Killing: its (linear, so `DΦ_t = Φ_t`) flow preserves `g`. -/
theorem ac_boost_isometry (t : ℝ) (a b : P) : gM (Φ t a) (Φ t b) = gM a b := by
  rw [gM_apply, gM_apply]
  simp only [Φ]
  have he : Real.exp (-t) * Real.exp t = 1 := by rw [← Real.exp_add]; simp
  linear_combination (-(a.1 * b.2 + a.2 * b.1) / 2) * he

/-- The Rindler horizon generator `γ s = (0, eˢ)` on `U = 0`. -/
def γ (s : ℝ) : P := (0, Real.exp s)

lemma hasDerivAt_γ (s : ℝ) : HasDerivAt γ (0, Real.exp s) s :=
  (hasDerivAt_const s (0:ℝ)).prodMk (Real.hasDerivAt_exp s)

lemma vel_γ (s : ℝ) : vel (E := P) γ s = (0, Real.exp s) := vel_eq_of_hasDerivAt (hasDerivAt_γ s)

/-- The witness splitting: `h = g`, `n = √(max 0 (−g(χ, χ)))`, `dt = dV/V = dλ` with `λ = log V`. -/
def σ : AdaptedSplitting mink γ where
  h := fun _ => gM
  n := fun s => √(max 0 (-(gM (χ (γ s)) (χ (γ s)))))
  dt := fun s => (1 / Real.exp s) • snd ℝ ℝ ℝ
  n_nonneg := fun _ _ => Real.sqrt_nonneg _
  split := fun s _ => by
    have : √(max 0 (-(gM (χ (γ s)) (χ (γ s))))) = 0 := by
      rw [g_χ_χ]; simp [γ]
    refine ContinuousLinearMap.ext fun a => ContinuousLinearMap.ext fun b => ?_
    show gM a b = _
    simp [this]
  h_nonneg := fun s _ => by rw [vel_γ, gM_apply]; simp

lemma σ_n (s : ℝ) : σ.n s = 0 := by
  show √(max 0 (-(gM (χ (γ s)) (χ (γ s))))) = 0
  rw [g_χ_χ]; simp [γ]

lemma σ_dt (s : ℝ) : σ.dt s (vel γ s) = 1 := by
  show ((1 / Real.exp s) • snd ℝ ℝ ℝ) (vel γ s) = 1
  rw [vel_γ]; simp [Real.exp_ne_zero]

/-- **The Rindler-horizon witness.** On 2D Minkowski `g = −dU dV`, along `γ s = (0, eˢ)`: `χ(γ s) = γ′ s`,
null and non-zero, with `g(χ, χ) = UV` everywhere; the adapted splitting `σ` has lapse `0` on `γ`,
`dt(γ′) = 1` (so `∫₀¹ dt(γ′) = 1`, `λ = log V` separates the endpoints); (a) and (b) hold, the hypotheses of
`ac_metric_singularity_along` hold and its conclusion `Δτ = 0` holds; and `p = γ 0 ≠ q = γ 1`. -/
theorem ac_witness :
    (∀ x : P, gM (χ x) (χ x) = x.1 * x.2) ∧
    (∀ s, χ (γ s) = vel (E := P) γ s) ∧
    (∀ s, mink.gE (γ s) (vel γ s) (vel γ s) = 0 ∧ vel (E := P) γ s ≠ 0) ∧
    (∀ s, σ.n s = 0) ∧
    (∫ s in (0:ℝ)..1, σ.dt s (vel γ s)) = 1 ∧
    (∀ s ∈ Icc (0:ℝ) 1, mink.gE (γ s) (vel γ s) (vel γ s) = 0) ∧
    σ.Δx = 0 ∧
    ContinuousOn (fun s => σ.h s (vel γ s) (vel γ s)) (Icc 0 1) ∧
    σ.Δτ = 0 ∧
    γ 0 = ((0:ℝ), (1:ℝ)) ∧ γ 1 = ((0:ℝ), Real.exp 1) ∧ γ 0 ≠ γ 1 := by
  have hnull : ∀ s, mink.gE (γ s) (vel γ s) (vel γ s) = 0 := fun s => by
    rw [mink_gE, vel_γ, gM_apply]; simp
  have hhz : ∀ s, σ.h s (vel γ s) (vel γ s) = 0 := hnull
  have hΔx : σ.Δx = 0 := by
    unfold AdaptedSplitting.Δx
    simp only [hhz, Real.sqrt_zero, intervalIntegral.integral_zero]
  have hcont : ContinuousOn (fun s => σ.h s (vel γ s) (vel γ s)) (Icc 0 1) := by
    simp only [hhz]; exact continuousOn_const
  refine ⟨g_χ_χ, fun s => by rw [vel_γ]; simp [χ, γ], fun s => ⟨hnull s, ?_⟩, σ_n, ?_,
    fun s _ => hnull s, hΔx, hcont,
    (ac_metric_singularity_along mink σ (fun s _ => hnull s) hΔx hcont).1,
    by simp [γ], rfl, ?_⟩
  · rw [vel_γ]; intro h; exact Real.exp_ne_zero s (congrArg Prod.snd h)
  · simp only [σ_dt]; simp
  · intro h
    have := congrArg Prod.snd h
    simp only [γ, Real.exp_zero] at this
    exact (Real.exp_one_gt_d9.trans' (by norm_num)).ne this

/-- Along the witness curve, **no** adapted splitting with positive lapse (and `h` positive definite on
`ker dt`) satisfies (a), (b): by `ac_lapse_pos_forces_point` it would give `γ 1 = γ 0`. -/
theorem ac_witness_no_positive_lapse (τ : AdaptedSplitting mink γ)
    (hb : τ.Δx = 0)
    (hcont : ContinuousOn (fun s => τ.h s (vel γ s) (vel γ s)) (Icc 0 1))
    (hpd : ∀ s ∈ Icc (0:ℝ) 1, ∀ v : P, v ≠ 0 → τ.dt s v = 0 → 0 < τ.h s v v) :
    ¬ ∀ s ∈ Icc (0:ℝ) 1, 0 < τ.n s := by
  intro hn
  have hγ := ac_witness
  obtain ⟨-, -, -, -, -, ha, -, -, -, -, -, hpq⟩ := hγ
  have hd : ∀ t ∈ Icc (0:ℝ) 1, MDifferentiableAt 𝓘(ℝ, ℝ) 𝓘(ℝ, P) γ t := fun t _ =>
    mdifferentiableAt_iff_differentiableAt.mpr (hasDerivAt_γ t).differentiableAt
  exact hpq ((ac_lapse_pos_forces_point mink τ ha hb hcont hn hpd).2 hd).symm

/-! ### Non-vacuity of the companion: the standard `t`-splitting on a constant curve -/

/-- The constant curve at the origin. -/
def γ₀ (_ : ℝ) : P := (0, 0)

lemma vel_γ₀ (s : ℝ) : vel (E := P) γ₀ s = 0 := vel_eq_of_hasDerivAt (hasDerivAt_const s (0, 0))

/-- `dt = (dU + dV)/2`. -/
def dt₀ : P →L[ℝ] ℝ := (1/2 : ℝ) • (fst ℝ ℝ ℝ + snd ℝ ℝ ℝ)

/-- `−dU dV = −dt² + dx²`: the standard splitting `h = g + dt ⊗ dt`, `n = 1`. -/
def σ₀ : AdaptedSplitting mink γ₀ where
  h := fun _ => gM + dt₀.smulRight dt₀
  n := fun _ => 1
  dt := fun _ => dt₀
  n_nonneg := fun _ _ => zero_le_one
  split := fun _ _ => by
    refine ContinuousLinearMap.ext fun a => ContinuousLinearMap.ext fun b => ?_
    show gM a b = _
    simp
  h_nonneg := fun s _ => by rw [vel_γ₀]; simp

/-- **Non-vacuity of `ac_lapse_pos_forces_point`:** every hypothesis holds for `σ₀` (lapse `1`, `h = dx²`
positive definite on `ker dt`), on the constant curve `γ₀`. -/
theorem ac_lapse_pos_nonvacuous :
    (∀ s ∈ Icc (0:ℝ) 1, mink.gE (γ₀ s) (vel γ₀ s) (vel γ₀ s) = 0) ∧ σ₀.Δx = 0 ∧
    ContinuousOn (fun s => σ₀.h s (vel γ₀ s) (vel γ₀ s)) (Icc 0 1) ∧
    (∀ s ∈ Icc (0:ℝ) 1, 0 < σ₀.n s) ∧
    (∀ s ∈ Icc (0:ℝ) 1, ∀ v : P, v ≠ 0 → σ₀.dt s v = 0 → 0 < σ₀.h s v v) := by
  have hz : ∀ s, σ₀.h s (vel γ₀ s) (vel γ₀ s) = 0 := fun s => by rw [vel_γ₀]; simp
  refine ⟨fun s _ => by rw [vel_γ₀]; simp, ?_, ?_, fun _ _ => zero_lt_one, ?_⟩
  · unfold AdaptedSplitting.Δx; simp only [hz, Real.sqrt_zero, intervalIntegral.integral_zero]
  · simp only [hz]; exact continuousOn_const
  · intro s _ v hv hdt
    change dt₀ v = 0 at hdt
    show 0 < (gM + dt₀.smulRight dt₀) v v
    have edt : dt₀ v = (1/2) * (v.1 + v.2) := by simp [dt₀]; ring
    have eh : (gM + dt₀.smulRight dt₀) v v = gM v v + dt₀ v * dt₀ v := by simp
    rw [eh, hdt, gM_apply]
    have h2 : v.2 = -v.1 := by linarith
    have h1 : v.1 ≠ 0 := by
      intro h1; apply hv; ext
      · exact h1
      · rw [h2, h1]; simp
    rw [h2]; nlinarith [sq_pos_of_ne_zero h1]

end Model

end ShadowProbe.AlongConnectionProbe

#print axioms ShadowProbe.AlongConnectionProbe.ac_metric_singularity_along
#print axioms ShadowProbe.AlongConnectionProbe.ac_const_of_vel_zero
#print axioms ShadowProbe.AlongConnectionProbe.ac_lapse_pos_forces_point
#print axioms ShadowProbe.AlongConnectionProbe.Model.ac_boost_generator
#print axioms ShadowProbe.AlongConnectionProbe.Model.ac_boost_isometry
#print axioms ShadowProbe.AlongConnectionProbe.Model.ac_witness
#print axioms ShadowProbe.AlongConnectionProbe.Model.ac_witness_no_positive_lapse
#print axioms ShadowProbe.AlongConnectionProbe.Model.ac_lapse_pos_nonvacuous

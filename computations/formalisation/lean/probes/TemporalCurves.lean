import Mathlib

/-!
# P1's 6b-ii, phase 3: non-imprisonment under a temporal function, and the global limit curve

Registration: `computations/formalisation/r7811_71_6bii_p3/PREDICTION.md`; plan `../r7807_71_6bii/PLAN.md`.
Mathlib only; nothing imports this file. Verbatim copies, unchanged: `probes/GeneratorStretch.lean` l.499–534,
l.906–907 (`IsTemporal`) and l.1020–1030 (the chart `Spacetime`, `restrict`), l.627–636 (`futTimelike_smul`),
l.2363–2448 (campaign 84's `V`-side helpers and the squash) and l.2777–3278 (the manifold kit through `ch_cau_iff`);
`probes/ConeCurves.lean` l.519–545 (the 2D Minkowski chart `kc_mink`). Everything new has the prefix `tc3_`.

Chains are parametrised by the temporal function `Θ` itself. A **`Θ`-causal curve** on `[a, b]` (`tc3_Causal`) is
continuous, `Θ`-parametrised, in `M`, and on every cone set `B` (an open `B ⊆ M` with `c‖v‖ ≤ dΘ(v)` for causal `v`)
each segment inside `B` rises in `Θ` by at least `c` times its displacement.

* **T1 — BUILT.** `tc3_cone`: the temporal cone lemma.
* **T2 — BUILT.** `tc3_arc_bound`, `tc3_cstep_arc`, `tc3_cau_bound`.
* **T3 — BUILT.** `tc3_reparam`, `tc3_concat`, `tc3_chain`; and `tc3_arc_causal`, `tc3_causal_concat`,
  `tc3_chain_causal`: every chain from `x ∈ M` is a `Θ`-causal curve.
* **T4 — BUILT.** `tc3_AA` (Arzelà–Ascoli), `tc3_local_limit`, `tc3_causal_limit` (limits are `Θ`-causal).
* **T5 — BUILT.** `tc3_nonimprison_top`, `tc3_nonimprison`: non-imprisonment.
* **T6 — BUILT (the registered stop did not hold).** `tc3_step`, `tc3_global_limit`, `tc3_global_escape`: the
  global limit curve, by a diagonal over a compact exhaustion of `M`; it leaves every compact set.
* **T7 — BUILT.** `tc3_temporal_NV`, `tc3_manifold_escape`: on `N` under `OneChart p₀`.
* **T8 — BUILT.** `tc3_witness`: the 2D Minkowski chart with `Θ = fst`.
-/

open Set Filter Topology BoundedContinuousFunction Metric

namespace ShadowProbe.TemporalCurvesProbe

section Kit
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

def IsTemporal (τ : V → ℝ) : Prop :=
  ContDiffOn ℝ 1 τ S.M ∧ ∀ x ∈ S.M, ∀ v, S.FutCausal x v → 0 < fderiv ℝ τ x v

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

end Spacetime

end Kit

section TC3
variable {V : Type*} [NormedAddCommGroup V] [NormedSpace ℝ V]

/-! ## Curves bounded by `Θ`, `Θ`-parametrised -/

/-- `c‖η t − η s‖ ≤ Θ(η t) − Θ(η s)` for `a ≤ s ≤ t ≤ b`. -/
def tc3_Bound (Θ : V → ℝ) (c a b : ℝ) (η : ℝ → V) : Prop :=
  ∀ s t, a ≤ s → s ≤ t → t ≤ b → c * ‖η t - η s‖ ≤ Θ (η t) - Θ (η s)

/-- `Θ`-parametrised on `[a, b]`: `Θ(η s) = Θ(η a) + (s − a)`. -/
def tc3_Param (Θ : V → ℝ) (a b : ℝ) (η : ℝ → V) : Prop :=
  ∀ s ∈ Icc a b, Θ (η s) = Θ (η a) + (s - a)

omit [NormedSpace ℝ V] in
lemma tc3_lip {Θ : V → ℝ} {c a b : ℝ} (hc : 0 < c) {η : ℝ → V} (hB : tc3_Bound Θ c a b η)
    (hP : tc3_Param Θ a b η) {s t : ℝ} (hs : s ∈ Icc a b) (ht : t ∈ Icc a b) :
    ‖η t - η s‖ ≤ |t - s| / c := by
  rcases le_total s t with h | h
  · have := hB s t hs.1 h ht.2
    rw [hP t ht, hP s hs] at this
    rw [abs_of_nonneg (sub_nonneg.2 h), le_div_iff₀ hc]; linarith
  · have := hB t s ht.1 h hs.2
    rw [hP t ht, hP s hs] at this
    rw [norm_sub_rev, abs_of_nonpos (sub_nonpos.2 h), le_div_iff₀ hc]; linarith

omit [NormedSpace ℝ V] in
/-- Concatenation of two `Θ`-bounded, `Θ`-parametrised curves meeting at `b`. -/
theorem tc3_concat {Θ : V → ℝ} {c a b d : ℝ} (hc : 0 ≤ c) (hab : a ≤ b) {η₁ η₂ : ℝ → V}
    (h1 : tc3_Bound Θ c a b η₁) (h2 : tc3_Bound Θ c b d η₂) (P1 : tc3_Param Θ a b η₁)
    (P2 : tc3_Param Θ b d η₂) (heq : η₁ b = η₂ b) :
    tc3_Bound Θ c a d (fun s => if s ≤ b then η₁ s else η₂ s) ∧
      tc3_Param Θ a d (fun s => if s ≤ b then η₁ s else η₂ s) := by
  refine ⟨fun s t hs hst ht => ?_, fun s hs => ?_⟩
  · by_cases htb : t ≤ b
    · simp only [htb, hst.trans htb, ↓reduceIte]
      exact h1 s t hs hst htb
    · by_cases hsb : s ≤ b
      · simp only [htb, hsb, ↓reduceIte]
        have e : η₂ t - η₁ s = (η₂ t - η₂ b) + (η₁ b - η₁ s) := by rw [heq]; abel
        have hn := norm_add_le (η₂ t - η₂ b) (η₁ b - η₁ s)
        have i1 := h2 b t le_rfl (le_of_not_ge htb) ht
        have i2 := h1 s b hs hsb le_rfl
        have hΘe : Θ (η₂ b) = Θ (η₁ b) := by rw [heq]
        rw [e]
        nlinarith [mul_le_mul_of_nonneg_left hn hc]
      · simp only [htb, hsb, ↓reduceIte]
        exact h2 s t (le_of_not_ge hsb) hst ht
  · simp only [hab, ↓reduceIte]
    by_cases hsb : s ≤ b
    · simp only [hsb, ↓reduceIte]
      exact P1 s ⟨hs.1, hsb⟩
    · simp only [hsb, ↓reduceIte]
      rw [P2 s ⟨le_of_not_ge hsb, hs.2⟩, ← heq, P1 b ⟨hab, le_rfl⟩]
      ring

/-! ## Row T4 (first half): Arzelà–Ascoli for uniformly Lipschitz families in a ball -/

/-- **Row T4 (Arzelà–Ascoli).** In finite dimension, a sequence of maps on `[a, b]`, uniformly
`1/c`-Lipschitz there and valued in one closed ball, has a uniformly convergent subsequence. -/
theorem tc3_AA [FiniteDimensional ℝ V] {a b c R : ℝ} (hab : a ≤ b) (hc : 0 < c) {z : V}
    {fs : ℕ → ℝ → V} (hval : ∀ n, ∀ s ∈ Icc a b, fs n s ∈ closedBall z R)
    (hlip : ∀ n, ∀ s ∈ Icc a b, ∀ t ∈ Icc a b, ‖fs n t - fs n s‖ ≤ |t - s| / c) :
    ∃ (φ : ℕ → ℕ) (γ : ℝ → V), StrictMono φ ∧
      TendstoUniformlyOn (fun n => fs (φ n)) γ atTop (Icc a b) := by
  have : ProperSpace V := FiniteDimensional.proper_real V
  have hL : ∀ n (x y : Icc a b), dist (fs n x) (fs n y) ≤ 1 / c * dist x y := by
    intro n x y
    rw [dist_eq_norm, Subtype.dist_eq, Real.dist_eq, one_div_mul_eq_div]
    exact hlip n y y.2 x x.2
  have hcont : ∀ n, Continuous (fun x : Icc a b => fs n x) := by
    intro n
    refine Metric.continuous_iff.2 fun x ε hε => ⟨ε * c, by positivity, fun y hy => ?_⟩
    calc dist (fs n y) (fs n x) ≤ 1 / c * dist y x := hL n y x
      _ < 1 / c * (ε * c) := by gcongr
      _ = ε := by field_simp
  let f : ℕ → (Icc a b →ᵇ V) := fun n => BoundedContinuousFunction.mkOfCompact ⟨_, hcont n⟩
  have hball : ∀ n x, f n x ∈ closedBall z R := fun n x => hval n x x.2
  have hEq : Equicontinuous ((↑) : Set.range f → Icc a b → V) := by
    intro x₀
    refine Metric.equicontinuousAt_iff.2 fun ε hε => ⟨ε * c, by positivity, fun x hx i => ?_⟩
    obtain ⟨n, hn⟩ := i.2
    rw [← hn]
    calc dist (f n x₀) (f n x) ≤ 1 / c * dist x₀ x := hL n x₀ x
      _ < 1 / c * (ε * c) := by rw [dist_comm]; gcongr
      _ = ε := by field_simp
  have hA := BoundedContinuousFunction.arzela_ascoli (closedBall z R)
    (isCompact_closedBall _ _) (Set.range f) (by rintro g x ⟨n, rfl⟩; exact hball n x) hEq
  obtain ⟨F, -, φ, hφ, hFlim⟩ := hA.tendsto_subseq (fun n => subset_closure ⟨n, rfl⟩)
  set γ : ℝ → V := fun s => F (projIcc a b hab s)
  have hγF : ∀ s (hs : s ∈ Icc a b), γ s = F ⟨s, hs⟩ := fun s hs => by
    simp [γ, projIcc_of_mem hab hs]
  refine ⟨φ, γ, hφ, ?_⟩
  rw [Metric.tendstoUniformlyOn_iff]
  intro ε hε
  have := (Metric.tendsto_nhds.1 hFlim) ε hε
  filter_upwards [this] with n hn
  intro s hs
  rw [hγF s hs, dist_comm]
  calc dist (fs (φ n) s) (F ⟨s, hs⟩) = dist (f (φ n) ⟨s, hs⟩) (F ⟨s, hs⟩) := rfl
    _ ≤ dist (f (φ n)) F := BoundedContinuousFunction.dist_coe_le_dist _
    _ < ε := hn

namespace Spacetime
variable (S : Spacetime V)

lemma tc3_futCausal_smul {x u : V} {c : ℝ} (hc : 0 < c) (h : S.FutCausal x u) :
    S.FutCausal x (c • u) := by
  obtain ⟨h1, h2⟩ := h
  refine ⟨?_, ?_⟩
  · simp only [map_smul, FunLike.coe_smul, Pi.smul_apply, smul_eq_mul]
    nlinarith [mul_pos hc hc]
  · simp only [map_smul, FunLike.coe_smul, Pi.smul_apply, smul_eq_mul]
    nlinarith

lemma tc3_futCausal_ne {x u : V} (h : S.FutCausal x u) : u ≠ 0 := by
  rintro rfl; simp [FutCausal] at h

omit [NormedSpace ℝ V] in
lemma tc3_tendsto_clm {ι F G : Type*} [NormedAddCommGroup F] [NormedSpace ℝ F] [NormedAddCommGroup G]
    [NormedSpace ℝ G] {l : Filter ι} {f : ι → F →L[ℝ] G} {A : F →L[ℝ] G} {u : ι → F} {a : F}
    (hf : Tendsto f l (𝓝 A)) (hu : Tendsto u l (𝓝 a)) : Tendsto (fun i => f i (u i)) l (𝓝 (A a)) :=
  ((continuous_fst.clm_apply continuous_snd).tendsto (A, a)).comp (hf.prodMk_nhds hu)

lemma tc3_contAt {Θ : V → ℝ} (hΘ : S.IsTemporal Θ) {x : V} (hx : x ∈ S.M) : ContinuousAt Θ x :=
  hΘ.1.continuousOn.continuousAt (S.isOpen_M.mem_nhds hx)

/-! ## Row T1: the temporal cone lemma -/

/-- **Row T1.** Near `x₀ ∈ M`, every future-causal vector satisfies `c‖v‖ ≤ dΘ_x(v)`; the closed
ball lies in `M`. -/
theorem tc3_cone [FiniteDimensional ℝ V] {Θ : V → ℝ} (hΘ : S.IsTemporal Θ) {x₀ : V} (hx₀ : x₀ ∈ S.M) :
    ∃ r > 0, ∃ c > 0, closedBall x₀ r ⊆ S.M ∧
      ∀ x ∈ ball x₀ r, ∀ v, S.FutCausal x v → c * ‖v‖ ≤ fderiv ℝ Θ x v := by
  obtain ⟨r₀, hr₀, hr₀M⟩ := Metric.isOpen_iff.1 S.isOpen_M x₀ hx₀
  by_contra hcon
  push Not at hcon
  have key : ∀ n : ℕ, ∃ x ∈ ball x₀ (min (r₀ / 2) (1 / (n + 1))), ∃ v, S.FutCausal x v ∧ ‖v‖ = 1 ∧
      fderiv ℝ Θ x v < 1 / (n + 1) := by
    intro n
    have hr : 0 < min (r₀ / 2) (1 / ((n:ℝ) + 1)) := lt_min (half_pos hr₀) (by positivity)
    have hsub : closedBall x₀ (min (r₀ / 2) (1 / ((n:ℝ) + 1))) ⊆ S.M :=
      (closedBall_subset_ball (lt_of_le_of_lt (min_le_left _ _) (half_lt_self hr₀))).trans hr₀M
    obtain ⟨x, hx, v, hv, hvK⟩ := hcon _ hr (1 / ((n:ℝ) + 1)) (by positivity) hsub
    have hv0 : 0 < ‖v‖ := norm_pos_iff.2 (S.tc3_futCausal_ne hv)
    refine ⟨x, hx, ‖v‖⁻¹ • v, S.tc3_futCausal_smul (inv_pos.2 hv0) hv, ?_, ?_⟩
    · rw [norm_smul, norm_inv, norm_norm, inv_mul_cancel₀ hv0.ne']
    · rw [map_smul, smul_eq_mul]
      calc ‖v‖⁻¹ * fderiv ℝ Θ x v < ‖v‖⁻¹ * (1 / ((n:ℝ) + 1) * ‖v‖) :=
            mul_lt_mul_of_pos_left hvK (inv_pos.2 hv0)
        _ = 1 / ((n:ℝ) + 1) := by field_simp
  choose xs hxs vs hvs hv1 hvτ using key
  have hsph : ∀ n, vs n ∈ sphere (0:V) 1 := fun n => by simp [hv1 n]
  obtain ⟨u, hu, φ, hφ, hlim⟩ := (isCompact_sphere (0:V) 1).tendsto_subseq hsph
  have hu1 : ‖u‖ = 1 := by simpa using hu
  have hx : Tendsto xs atTop (𝓝 x₀) := by
    rw [Metric.tendsto_atTop]
    intro ε hε
    obtain ⟨N, hN⟩ := exists_nat_one_div_lt hε
    refine ⟨N, fun n hn => ?_⟩
    have h1 := mem_ball.1 (hxs n)
    calc dist (xs n) x₀ < min (r₀ / 2) (1 / ((n:ℝ) + 1)) := h1
      _ ≤ 1 / ((n:ℝ) + 1) := min_le_right _ _
      _ ≤ 1 / ((N:ℝ) + 1) := by gcongr
      _ < ε := hN
  have hxφ := hx.comp hφ.tendsto_atTop
  have hnhds : S.M ∈ 𝓝 x₀ := S.isOpen_M.mem_nhds hx₀
  have hgc : ContinuousAt S.g x₀ := S.cont_g.continuousAt hnhds
  have hTc : ContinuousAt S.T x₀ := S.cont_T.continuousAt hnhds
  have hdc : ContinuousAt (fderiv ℝ Θ) x₀ :=
    (hΘ.1.continuousOn_fderiv_of_isOpen S.isOpen_M le_rfl).continuousAt hnhds
  have hg : Tendsto (fun n => S.g (xs (φ n))) atTop (𝓝 (S.g x₀)) := hgc.tendsto.comp hxφ
  have hT : Tendsto (fun n => S.T (xs (φ n))) atTop (𝓝 (S.T x₀)) := hTc.tendsto.comp hxφ
  have h1 : Tendsto (fun n => S.g (xs (φ n)) (vs (φ n)) (vs (φ n))) atTop (𝓝 (S.g x₀ u u)) :=
    tc3_tendsto_clm (tc3_tendsto_clm hg hlim) hlim
  have h2 : Tendsto (fun n => S.g (xs (φ n)) (vs (φ n)) (S.T (xs (φ n)))) atTop
      (𝓝 (S.g x₀ u (S.T x₀))) := tc3_tendsto_clm (tc3_tendsto_clm hg hlim) hT
  have h3 : Tendsto (fun n => fderiv ℝ Θ (xs (φ n)) (vs (φ n))) atTop (𝓝 (fderiv ℝ Θ x₀ u)) :=
    tc3_tendsto_clm (hdc.tendsto.comp hxφ) hlim
  have hA : S.g x₀ u u ≤ 0 := le_of_tendsto' h1 fun n => (hvs (φ n)).1
  have hB : S.g x₀ u (S.T x₀) ≤ 0 := le_of_tendsto' h2 fun n => (hvs (φ n)).2.le
  have hC : fderiv ℝ Θ x₀ u ≤ 0 := by
    have h4 : Tendsto (fun n : ℕ => 1 / ((φ n : ℝ) + 1)) atTop (𝓝 0) :=
      tendsto_one_div_add_atTop_nhds_zero_nat.comp hφ.tendsto_atTop
    exact le_of_tendsto_of_tendsto' h3 h4 fun n => (hvτ (φ n)).le
  rcases hB.lt_or_eq with hlt | heq
  · have := hΘ.2 x₀ hx₀ u ⟨hA, hlt⟩
    linarith
  · have hpos := S.pos_on_perp x₀ hx₀ u heq (by rintro rfl; simp at hu1)
    linarith

/-! ## Row T2: arcs and chains rise in `Θ` by at least their displacement -/

/-- **Row T2 (arcs).** -/
theorem tc3_arc_bound {Θ : V → ℝ} (hΘ : S.IsTemporal Θ) {c : ℝ} (hc : 0 < c) {γ : ℝ → V}
    (hγ : ContDiff ℝ 1 γ) {a b : ℝ}
    (hd : ∀ t ∈ Icc a b, γ t ∈ S.M ∧ c * ‖deriv γ t‖ ≤ fderiv ℝ Θ (γ t) (deriv γ t)) :
    tc3_Bound Θ c a b γ := by
  intro s t hs hst ht
  have hdiff : Differentiable ℝ γ := hγ.differentiable one_ne_zero
  have hsub : ∀ u ∈ Icc s t, u ∈ Icc a b := fun u hu => ⟨hs.trans hu.1, hu.2.trans ht⟩
  have hΘd : ∀ u ∈ Icc s t, HasDerivAt (fun u => (Θ (γ u) - Θ (γ s)) / c)
      (fderiv ℝ Θ (γ u) (deriv γ u) / c) u := fun u hu =>
    (((((hΘ.1.contDiffAt (S.isOpen_M.mem_nhds (hd u (hsub u hu)).1)).differentiableAt
      one_ne_zero).hasFDerivAt).comp_hasDerivAt u (hdiff u).hasDerivAt).sub_const _).div_const c
  have key := image_norm_le_of_norm_deriv_right_le_deriv_boundary' (a := s) (b := t)
    (f := fun u => γ u - γ s) (f' := deriv γ)
    ((hγ.continuous.sub continuous_const).continuousOn)
    (fun u _ => ((hdiff u).hasDerivAt.sub_const _).hasDerivWithinAt)
    (B := fun u => (Θ (γ u) - Θ (γ s)) / c) (B' := fun u => fderiv ℝ Θ (γ u) (deriv γ u) / c)
    (by simp)
    (fun u hu => (hΘd u hu).continuousAt.continuousWithinAt)
    (fun u hu => (hΘd u (Ico_subset_Icc_self hu)).hasDerivWithinAt)
    (fun u hu => by
      rw [le_div_iff₀ hc, mul_comm]; exact (hd u (hsub u (Ico_subset_Icc_self hu))).2)
    ⟨hst, le_rfl⟩
  rw [mul_comm, ← le_div_iff₀ hc]; exact key

variable {S}

/-- **Row T2 (steps).** An arc of a step of the chart restricted to a set where the temporal cone
lemma holds is `Θ`-bounded on `[0, 1]`. -/
theorem tc3_cstep_arc {Θ : V → ℝ} (hΘ : S.IsTemporal Θ) {c : ℝ} (hc : 0 < c) {B : Set V}
    (hB : IsOpen B) (hBM : B ⊆ S.M)
    (hcone : ∀ x ∈ B, ∀ v, S.FutCausal x v → c * ‖v‖ ≤ fderiv ℝ Θ x v) {x y : V}
    (h : (S.restrict B hB hBM).CStep x y) :
    ∃ γ : ℝ → V, ContDiff ℝ 1 γ ∧ γ 0 = x ∧ γ 1 = y ∧
      (∀ t ∈ Icc (0:ℝ) 1, γ t ∈ B ∧ S.FutCausal (γ t) (deriv γ t)) ∧ tc3_Bound Θ c 0 1 γ := by
  obtain ⟨γ, hγ, h0, h1, ht⟩ := h
  have hd : ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ B ∧ S.FutCausal (γ t) (deriv γ t) := fun t htI =>
    ⟨(ht t htI).1, (ht t htI).2⟩
  exact ⟨γ, hγ, h0, h1, hd, S.tc3_arc_bound hΘ hc hγ fun t htI =>
    ⟨hBM (hd t htI).1, hcone _ (hd t htI).1 _ (hd t htI).2⟩⟩

/-- **Row T2 (chains).** `c‖y − x‖ ≤ Θ y − Θ x` along a chain of the restricted chart. -/
theorem tc3_cau_bound {Θ : V → ℝ} (hΘ : S.IsTemporal Θ) {c : ℝ} (hc : 0 < c) {B : Set V}
    (hB : IsOpen B) (hBM : B ⊆ S.M)
    (hcone : ∀ x ∈ B, ∀ v, S.FutCausal x v → c * ‖v‖ ≤ fderiv ℝ Θ x v) {x y : V}
    (h : (S.restrict B hB hBM).Cau x y) : c * ‖y - x‖ ≤ Θ y - Θ x := by
  induction h with
  | refl => simp
  | @tail y z _ hst ih =>
    obtain ⟨γ, -, h0, h1, -, hb⟩ := tc3_cstep_arc hΘ hc hB hBM hcone hst
    have := hb 0 1 le_rfl zero_le_one le_rfl
    rw [h0, h1] at this
    have e : z - x = (z - y) + (y - x) := by abel
    rw [e]
    nlinarith [mul_le_mul_of_nonneg_left (norm_add_le (z - y) (y - x)) hc.le]

/-! ## Row T3: `Θ`-parametrisation of chains -/

/-- One arc, reparametrised by the inverse of `Θ ∘ γ`. -/
theorem tc3_reparam {Θ : V → ℝ} (hΘ : S.IsTemporal Θ) {c : ℝ} {γ : ℝ → V} (hγ : ContDiff ℝ 1 γ)
    (hd : ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ S.M ∧ S.FutCausal (γ t) (deriv γ t))
    (hb : tc3_Bound Θ c 0 1 γ) :
    ∃ η : ℝ → V, tc3_Bound Θ c (Θ (γ 0)) (Θ (γ 1)) η ∧ tc3_Param Θ (Θ (γ 0)) (Θ (γ 1)) η ∧
      η (Θ (γ 0)) = γ 0 ∧ η (Θ (γ 1)) = γ 1 ∧ Θ (γ 0) < Θ (γ 1) ∧
      ∀ σ ∈ Icc (Θ (γ 0)) (Θ (γ 1)), ∃ u ∈ Icc (0:ℝ) 1, η σ = γ u := by
  set f : ℝ → ℝ := fun u => Θ (γ u) with hfdef
  have hdiff : Differentiable ℝ γ := hγ.differentiable one_ne_zero
  have hfd : ∀ u ∈ Icc (0:ℝ) 1, HasDerivAt f (fderiv ℝ Θ (γ u) (deriv γ u)) u := fun u hu =>
    (((hΘ.1.contDiffAt (S.isOpen_M.mem_nhds (hd u hu).1)).differentiableAt
      one_ne_zero).hasFDerivAt).comp_hasDerivAt u (hdiff u).hasDerivAt
  have hfc : ContinuousOn f (Icc 0 1) :=
    hΘ.1.continuousOn.comp hγ.continuous.continuousOn fun u hu => (hd u hu).1
  have hmono : StrictMonoOn f (Icc 0 1) := by
    refine strictMonoOn_of_deriv_pos (convex_Icc 0 1) hfc fun u hu => ?_
    rw [interior_Icc] at hu
    rw [(hfd u (Ioo_subset_Icc_self hu)).deriv]
    exact hΘ.2 _ (hd u (Ioo_subset_Icc_self hu)).1 _ (hd u (Ioo_subset_Icc_self hu)).2
  have h01 : f 0 < f 1 := hmono ⟨le_rfl, zero_le_one⟩ ⟨zero_le_one, le_rfl⟩ zero_lt_one
  have hex : ∀ σ ∈ Icc (f 0) (f 1), ∃ u ∈ Icc (0:ℝ) 1, f u = σ :=
    fun σ hσ => intermediate_value_Icc zero_le_one hfc hσ
  set θ := Function.invFunOn f (Icc (0:ℝ) 1) with hθdef
  have hθ : ∀ σ ∈ Icc (f 0) (f 1), θ σ ∈ Icc (0:ℝ) 1 ∧ f (θ σ) = σ :=
    fun σ hσ => Function.invFunOn_pos (hex σ hσ)
  have hθ0 : θ (f 0) = 0 := hmono.injOn (hθ _ ⟨le_rfl, h01.le⟩).1 ⟨le_rfl, zero_le_one⟩
    (hθ _ ⟨le_rfl, h01.le⟩).2
  have hθ1 : θ (f 1) = 1 := hmono.injOn (hθ _ ⟨h01.le, le_rfl⟩).1 ⟨zero_le_one, le_rfl⟩
    (hθ _ ⟨h01.le, le_rfl⟩).2
  refine ⟨fun σ => γ (θ σ), ?_, ?_, by show γ (θ (f 0)) = γ 0; rw [hθ0],
    by show γ (θ (f 1)) = γ 1; rw [hθ1], h01, fun σ hσ => ⟨θ σ, (hθ σ hσ).1, rfl⟩⟩
  · intro s t hs hst ht
    have hs' := hθ s ⟨hs, hst.trans ht⟩
    have ht' := hθ t ⟨hs.trans hst, ht⟩
    have hle : θ s ≤ θ t := by
      by_contra hlt
      push Not at hlt
      have := hmono ht'.1 hs'.1 hlt
      rw [hs'.2, ht'.2] at this
      linarith
    exact hb _ _ hs'.1.1 hle ht'.1.2
  · intro σ hσ
    show f (θ σ) = f (θ (f 0)) + (σ - f 0)
    rw [(hθ σ hσ).2, (hθ _ ⟨le_rfl, h01.le⟩).2]
    ring

/-- **Row T3.** A chain of the restricted chart from `x ∈ B` gives a `Θ`-bounded,
`Θ`-parametrised curve on `[Θ x, Θ y]` from `x` to `y`, with values in `B`. -/
theorem tc3_chain {Θ : V → ℝ} (hΘ : S.IsTemporal Θ) {c : ℝ} (hc : 0 < c) {B : Set V}
    (hB : IsOpen B) (hBM : B ⊆ S.M)
    (hcone : ∀ x ∈ B, ∀ v, S.FutCausal x v → c * ‖v‖ ≤ fderiv ℝ Θ x v) {x y : V} (hx : x ∈ B)
    (h : (S.restrict B hB hBM).Cau x y) :
    ∃ η : ℝ → V, tc3_Bound Θ c (Θ x) (Θ y) η ∧ tc3_Param Θ (Θ x) (Θ y) η ∧ η (Θ x) = x ∧
      η (Θ y) = y ∧ Θ x ≤ Θ y ∧ ∀ σ ∈ Icc (Θ x) (Θ y), η σ ∈ B := by
  induction h with
  | refl =>
    refine ⟨fun _ => x, fun s t _ _ _ => by simp, fun s hs => ?_, rfl, rfl, le_rfl, fun _ _ => hx⟩
    have : s = Θ x := le_antisymm hs.2 hs.1
    simp [this]
  | @tail y z _ hst ih =>
    obtain ⟨η₁, hK1, hP1, h1a, h1b, hle1, hB1⟩ := ih
    obtain ⟨γ, hγ, h0, h1, hd, hb⟩ := tc3_cstep_arc hΘ hc hB hBM hcone hst
    obtain ⟨η₂, hK2, hP2, h2a, h2b, hlt2, hB2⟩ :=
      tc3_reparam hΘ hγ (fun t ht => ⟨hBM (hd t ht).1, (hd t ht).2⟩) hb
    subst h0; subst h1
    obtain ⟨hKc, hPc⟩ := tc3_concat hc.le hle1 hK1 hK2 hP1 hP2 (by rw [h1b, h2a])
    refine ⟨_, hKc, hPc, ?_, ?_, hle1.trans hlt2.le, fun σ hσ => ?_⟩
    · simp only [hle1, ↓reduceIte]; exact h1a
    · simp only [not_le.2 hlt2, ↓reduceIte]; exact h2b
    · by_cases hσb : σ ≤ Θ (γ 0)
      · simp only [hσb, ↓reduceIte]; exact hB1 σ ⟨hσ.1, hσb⟩
      · simp only [hσb, ↓reduceIte]
        obtain ⟨u, hu, e⟩ := hB2 σ ⟨le_of_not_ge hσb, hσ.2⟩
        rw [e]; exact (hd u hu).1

/-! ## Row T4: the local limit for `Θ`-parametrised chains -/

/-- **Row T4.** Around `x₀ ∈ M` there are a ball `B` (with `closedBall ⊆ M`) and `c > 0` such that
chains of the chart restricted to `B` from `xₙ → p`, rising by at least `δ` in `Θ`, have
`Θ`-parametrisations on `[0, δ]` with a subsequence converging uniformly to a `Θ`-bounded,
`Θ`-parametrised curve from `p` in the closed ball. -/
theorem tc3_local_limit [FiniteDimensional ℝ V] {Θ : V → ℝ} (hΘ : S.IsTemporal Θ) {x₀ : V}
    (hx₀ : x₀ ∈ S.M) :
    ∃ r > 0, ∃ c > 0, ∃ hBM : ball x₀ r ⊆ S.M, closedBall x₀ r ⊆ S.M ∧
      ∀ (xs ys : ℕ → V) (p : V) (δ : ℝ), 0 < δ → (∀ n, xs n ∈ ball x₀ r) →
        (∀ n, (S.restrict (ball x₀ r) isOpen_ball hBM).Cau (xs n) (ys n)) →
        (∀ n, Θ (xs n) + δ ≤ Θ (ys n)) → Tendsto xs atTop (𝓝 p) →
        ∃ (ηs : ℕ → ℝ → V) (φ : ℕ → ℕ) (γ : ℝ → V),
          (∀ n, ηs n 0 = xs n ∧ ∀ s ∈ Icc (0:ℝ) δ, ηs n s ∈ ball x₀ r) ∧ StrictMono φ ∧
          TendstoUniformlyOn (fun n => ηs (φ n)) γ atTop (Icc 0 δ) ∧
          tc3_Bound Θ c 0 δ γ ∧ tc3_Param Θ 0 δ γ ∧ γ 0 = p ∧
          ∀ s ∈ Icc (0:ℝ) δ, γ s ∈ closedBall x₀ r := by
  obtain ⟨r, hr, c, hc, hcl, hcone⟩ := S.tc3_cone hΘ hx₀
  have hBM : ball x₀ r ⊆ S.M := ball_subset_closedBall.trans hcl
  refine ⟨r, hr, c, hc, hBM, hcl, fun xs ys p δ hδ hxB hcau hrise hp => ?_⟩
  have hch := fun n => tc3_chain hΘ hc isOpen_ball hBM hcone (hxB n) (hcau n)
  choose η hK hP ha hb hle hB using hch
  set ηs : ℕ → ℝ → V := fun n s => η n (Θ (xs n) + s) with hηs
  have hK' : ∀ n, tc3_Bound Θ c 0 δ (ηs n) := fun n s t hs hst ht =>
    hK n _ _ (by linarith) (by linarith) (by linarith [hrise n])
  have hP' : ∀ n, tc3_Param Θ 0 δ (ηs n) := fun n s hs => by
    simp only [hηs, add_zero]
    rw [hP n _ ⟨by linarith [hs.1], by linarith [hs.2, hrise n]⟩, ha n]
    ring
  have h0 : ∀ n, ηs n 0 = xs n := fun n => by simp only [hηs, add_zero]; exact ha n
  have hηB : ∀ n, ∀ s ∈ Icc (0:ℝ) δ, ηs n s ∈ ball x₀ r := fun n s hs =>
    hB n _ ⟨by linarith [hs.1], by linarith [hs.2, hrise n]⟩
  obtain ⟨φ, γ, hφ, hu⟩ := tc3_AA hδ.le hc (z := x₀) (R := r)
    (fun n s hs => ball_subset_closedBall (hηB n s hs))
    (fun n s hs t ht => tc3_lip hc (hK' n) (hP' n) hs ht)
  have hpt : ∀ s ∈ Icc (0:ℝ) δ, Tendsto (fun n => ηs (φ n) s) atTop (𝓝 (γ s)) :=
    fun s hs => hu.tendsto_at hs
  have hγB : ∀ s ∈ Icc (0:ℝ) δ, γ s ∈ closedBall x₀ r := fun s hs =>
    isClosed_closedBall.mem_of_tendsto (hpt s hs)
      (Eventually.of_forall fun n => ball_subset_closedBall (hηB (φ n) s hs))
  have hΘt : ∀ s ∈ Icc (0:ℝ) δ, Tendsto (fun n => Θ (ηs (φ n) s)) atTop (𝓝 (Θ (γ s))) :=
    fun s hs => (S.tc3_contAt hΘ (hcl (hγB s hs))).tendsto.comp (hpt s hs)
  have h0δ : (0:ℝ) ∈ Icc 0 δ := ⟨le_rfl, hδ.le⟩
  refine ⟨ηs, φ, γ, fun n => ⟨h0 n, hηB n⟩, hφ, hu, fun s t hs hst ht => ?_, fun s hs => ?_, ?_, hγB⟩
  · have hs' : s ∈ Icc 0 δ := ⟨hs, hst.trans ht⟩
    have ht' : t ∈ Icc 0 δ := ⟨hs.trans hst, ht⟩
    refine le_of_tendsto_of_tendsto' (((continuous_norm.tendsto _).comp
      ((hpt t ht').sub (hpt s hs'))).const_mul c) ((hΘt t ht').sub (hΘt s hs')) fun n => ?_
    exact hK' (φ n) s t hs hst ht
  · refine tendsto_nhds_unique (hΘt s hs) ?_
    have := (hΘt 0 h0δ).add_const (s - 0)
    refine this.congr fun n => ?_
    exact (hP' (φ n) s hs).symm
  · exact tendsto_nhds_unique (hpt 0 h0δ)
      ((hp.comp hφ.tendsto_atTop).congr fun n => (h0 (φ n)).symm)

variable (S) in
/-- Locally `Θ`-bounded on `[0, T)`: every `x₀ ∈ M` has a ball in `M` and `c > 0` such that
`c‖γ t − γ s‖ ≤ Θ(γ t) − Θ(γ s)` whenever `γ([s, t])` stays in the ball. -/
def tc3_LocBound (Θ : V → ℝ) (T : ℝ) (γ : ℝ → V) : Prop :=
  ∀ x₀ ∈ S.M, ∃ r > 0, ∃ c > 0, ball x₀ r ⊆ S.M ∧ ∀ s t, 0 ≤ s → s ≤ t → t < T →
    (∀ u ∈ Icc s t, γ u ∈ ball x₀ r) → c * ‖γ t - γ s‖ ≤ Θ (γ t) - Θ (γ s)

/-! ## Row T5: non-imprisonment -/

/-- **Row T5 (`T = ∞`).** A `Θ`-parametrised curve on `[0, ∞)` eventually leaves every compact
`K ⊆ M`: `Θ` is bounded on `K` and unbounded along the curve. -/
theorem tc3_nonimprison_top {Θ : V → ℝ} (hΘ : S.IsTemporal Θ) {γ : ℝ → V}
    (hP : ∀ t ≥ 0, Θ (γ t) = Θ (γ 0) + t) {K : Set V} (hK : IsCompact K) (hKM : K ⊆ S.M) :
    ∀ᶠ t in atTop, γ t ∉ K := by
  obtain ⟨B, hB⟩ := hK.bddAbove_image (hΘ.1.continuousOn.mono hKM)
  filter_upwards [eventually_gt_atTop (max 0 (B - Θ (γ 0)))] with t ht hmem
  have h1 := hB ⟨γ t, hmem, rfl⟩
  rw [hP t (le_max_left _ _ |>.trans ht.le)] at h1
  linarith [le_max_right 0 (B - Θ (γ 0))]

/-- **Row T5 (`T < ∞`).** A continuous, `Θ`-parametrised, locally `Θ`-bounded curve on `[0, T)` that
has no limit in `M` as `t → T⁻` eventually leaves every compact `K ⊆ M`. -/
theorem tc3_nonimprison [FiniteDimensional ℝ V] {Θ : V → ℝ} {T : ℝ} (hT : 0 < T) {γ : ℝ → V}
    (hcont : ContinuousOn γ (Ico 0 T)) (hP : ∀ t ∈ Ico 0 T, Θ (γ t) = Θ (γ 0) + t)
    (hL : S.tc3_LocBound Θ T γ) (hinext : ¬ ∃ p ∈ S.M, Tendsto γ (𝓝[<] T) (𝓝 p))
    {K : Set V} (hK : IsCompact K) (hKM : K ⊆ S.M) : ∀ᶠ t in 𝓝[<] T, γ t ∉ K := by
  have : CompleteSpace V := FiniteDimensional.complete ℝ V
  by_contra hcon
  rw [not_eventually] at hcon
  simp only [not_not] at hcon
  obtain ⟨ts, hts, hfr⟩ := frequently_iff_seq_frequently.1 hcon
  obtain ⟨ψ, hψ, hψK⟩ := extraction_of_frequently_atTop hfr
  obtain ⟨x, hxK, ψ', hψ', hlim⟩ := hK.tendsto_subseq hψK
  set tk : ℕ → ℝ := fun n => ts (ψ (ψ' n)) with htk
  have htk_lim : Tendsto tk atTop (𝓝[<] T) := hts.comp (hψ.comp hψ').tendsto_atTop
  obtain ⟨r, hr, c, hc, hBM, hLx⟩ := hL x (hKM hxK)
  -- choose `t₀ = tk k` close to `T` with `γ t₀` close to `x`
  have ev1 : ∀ᶠ n in atTop, tk n < T := (tendsto_nhdsWithin_iff.1 htk_lim).2
  have ev2 : ∀ᶠ n in atTop, T - c * (r / 3) < tk n ∧ 0 < tk n := by
    have h := (tendsto_nhdsWithin_iff.1 htk_lim).1
    have hpos : 0 < c * (r / 3) := by positivity
    exact (h.eventually (Ioi_mem_nhds (by linarith : T - c * (r / 3) < T))).and
      (h.eventually (Ioi_mem_nhds hT))
  have ev3 : ∀ᶠ n in atTop, dist (γ (tk n)) x < r / 3 :=
    (Metric.tendsto_nhds.1 hlim) _ (by positivity)
  obtain ⟨k, hk1, ⟨hk2, hk0⟩, hk3⟩ := (ev1.and (ev2.and ev3)).exists
  set t₀ := tk k
  -- the curve stays in `closedBall x (2r/3)` on `[t₀, T)`
  have hstay : ∀ t₁ ∈ Ico t₀ T, dist (γ t₁) x ≤ 2 * r / 3 := by
    intro t₁ ht₁
    by_contra hout
    push Not at hout
    set A := Icc t₀ t₁ ∩ γ ⁻¹' {y | 2 * r / 3 ≤ dist y x} with hAdef
    have hAc : IsClosed A := (hcont.mono fun u hu => ⟨hk0.le.trans hu.1, hu.2.trans_lt ht₁.2⟩
      ).preimage_isClosed_of_isClosed isClosed_Icc
      (isClosed_le continuous_const (continuous_id.dist continuous_const))
    have hA1 : t₁ ∈ A := ⟨⟨ht₁.1, le_rfl⟩, hout.le⟩
    have hAb : BddBelow A := ⟨t₀, fun u hu => hu.1.1⟩
    set ts' := sInf A with hts'
    have hmem : ts' ∈ A := hAc.csInf_mem ⟨t₁, hA1⟩ hAb
    have hlt0 : t₀ < ts' := by
      rcases hmem.1.1.lt_or_eq with h | h
      · exact h
      · exfalso; have := hmem.2; rw [← h] at this
        simp only [mem_preimage, mem_ofPred_eq] at this; linarith
    have hbefore : ∀ u ∈ Ico t₀ ts', dist (γ u) x < 2 * r / 3 := by
      intro u hu
      by_contra hu'
      push Not at hu'
      have : u ∈ A := ⟨⟨hu.1, hu.2.le.trans hmem.1.2⟩, hu'⟩
      exact absurd (csInf_le hAb this) (not_le.2 hu.2)
    have hsT : ts' < T := hmem.1.2.trans_lt ht₁.2
    have hcw : ContinuousWithinAt γ (Ico t₀ ts') ts' :=
      (hcont ts' ⟨hk0.le.trans hlt0.le, hsT⟩).mono fun u hu => ⟨hk0.le.trans hu.1, hu.2.trans hsT⟩
    have hcl : ts' ∈ closure (Ico t₀ ts') := by rw [closure_Ico hlt0.ne]; exact ⟨hlt0.le, le_rfl⟩
    have hγs : dist (γ ts') x ≤ 2 * r / 3 := by
      have h := hcw.mem_closure_image hcl
      have hsub : γ '' Ico t₀ ts' ⊆ closedBall x (2 * r / 3) := by
        rintro _ ⟨u, hu, rfl⟩; exact (hbefore u hu).le
      exact (closure_minimal hsub isClosed_closedBall) h
    have hin : ∀ u ∈ Icc t₀ ts', γ u ∈ ball x r := by
      intro u hu
      rcases hu.2.lt_or_eq with h | h
      · exact mem_ball.2 ((hbefore u ⟨hu.1, h⟩).trans (by linarith))
      · rw [h]; exact mem_ball.2 (hγs.trans_lt (by linarith))
    have hb := hLx t₀ ts' hk0.le hlt0.le hsT hin
    rw [hP ts' ⟨hk0.le.trans hlt0.le, hsT⟩, hP t₀ ⟨hk0.le, hk1⟩] at hb
    have hnorm : ‖γ ts' - γ t₀‖ < r / 3 := by
      have : c * ‖γ ts' - γ t₀‖ < c * (r / 3) := by linarith
      exact lt_of_mul_lt_mul_left this hc.le
    have := dist_triangle (γ ts') (γ t₀) x
    rw [dist_eq_norm (γ ts') (γ t₀)] at this
    have hmem2 := hmem.2
    simp only [mem_preimage, mem_ofPred_eq] at hmem2
    linarith
  -- the Lipschitz bound on `[t₀, T)` and the limit
  have hlip : ∀ s ∈ Ico t₀ T, ∀ t ∈ Ico t₀ T, s ≤ t → c * ‖γ t - γ s‖ ≤ t - s := by
    intro s hs t ht hst
    have hb := hLx s t (hk0.le.trans hs.1) hst ht.2 fun u hu =>
      mem_ball.2 ((hstay u ⟨hs.1.trans hu.1, hu.2.trans_lt ht.2⟩).trans_lt (by linarith))
    rw [hP t ⟨hk0.le.trans (hs.1.trans hst), ht.2⟩, hP s ⟨hk0.le.trans hs.1, hs.2⟩] at hb
    linarith
  have hcauchy : Cauchy (map γ (𝓝[<] T)) := by
    rw [Metric.cauchy_iff]
    refine ⟨inferInstance, fun ε hε => ?_⟩
    set a := max t₀ (T - c * ε / 2) with ha
    have haT : a < T := max_lt hk1 (by have : 0 < c * ε / 2 := by positivity
                                       linarith)
    refine ⟨γ '' Ioo a T, image_mem_map (Ioo_mem_nhdsLT haT), ?_⟩
    rintro _ ⟨s, hs, rfl⟩ _ ⟨t, ht, rfl⟩
    have hs' : s ∈ Ico t₀ T := ⟨(le_max_left _ _).trans hs.1.le, hs.2⟩
    have ht' : t ∈ Ico t₀ T := ⟨(le_max_left _ _).trans ht.1.le, ht.2⟩
    have hsa : T - c * ε / 2 < s := (le_max_right _ _).trans_lt hs.1
    have hta : T - c * ε / 2 < t := (le_max_right _ _).trans_lt ht.1
    rw [dist_eq_norm]
    have key : c * ‖γ s - γ t‖ < c * ε := by
      rcases le_total s t with h | h
      · rw [norm_sub_rev]; have := hlip s hs' t ht' h; linarith [ht.2, hs.2]
      · have := hlip t ht' s hs' h; linarith [ht.2, hs.2]
    exact lt_of_mul_lt_mul_left key hc.le
  obtain ⟨p, hp⟩ := cauchy_map_iff_exists_tendsto.1 hcauchy
  have hpB : p ∈ closedBall x (2 * r / 3) :=
    isClosed_closedBall.mem_of_tendsto hp (by
      filter_upwards [Ioo_mem_nhdsLT hk1] with t ht
      exact hstay t ⟨ht.1.le, ht.2⟩)
  exact hinext ⟨p, hBM (mem_ball.2 ((mem_closedBall.1 hpB).trans_lt (by linarith))), hp⟩

/-! ## Row T6 (groundwork): `Θ`-causal curves -/

variable (S) in
/-- An open `B ⊆ M` on which `c‖v‖ ≤ dΘ_x(v)` for every future-causal `v`. -/
def tc3_ConeSet (Θ : V → ℝ) (B : Set V) (c : ℝ) : Prop :=
  IsOpen B ∧ B ⊆ S.M ∧ ∀ x ∈ B, ∀ v, S.FutCausal x v → c * ‖v‖ ≤ fderiv ℝ Θ x v

variable (S) in
/-- **A `Θ`-causal curve on `[a, b]`**: continuous, `Θ`-parametrised, in `M`, and on every cone set
`B` (constant `c`) any segment inside `B` rises in `Θ` by at least `c` times its displacement. -/
def tc3_Causal (Θ : V → ℝ) (a b : ℝ) (η : ℝ → V) : Prop :=
  ContinuousOn η (Icc a b) ∧ tc3_Param Θ a b η ∧ (∀ s ∈ Icc a b, η s ∈ S.M) ∧
    ∀ B c, S.tc3_ConeSet Θ B c → ∀ s t, a ≤ s → s ≤ t → t ≤ b → (∀ u ∈ Icc s t, η u ∈ B) →
      c * ‖η t - η s‖ ≤ Θ (η t) - Θ (η s)

omit [NormedAddCommGroup V] [NormedSpace ℝ V] in
lemma tc3_Param_mono {Θ : V → ℝ} {a b : ℝ} {η : ℝ → V} (hP : tc3_Param Θ a b η) {s t : ℝ}
    (hs : s ∈ Icc a b) (ht : t ∈ Icc a b) : Θ (η t) - Θ (η s) = t - s := by
  rw [hP t ht, hP s hs]; ring

/-- One arc, `Θ`-reparametrised, is a `Θ`-causal curve. -/
theorem tc3_arc_causal {Θ : V → ℝ} (hΘ : S.IsTemporal Θ) {γ : ℝ → V} (hγ : ContDiff ℝ 1 γ)
    (hd : ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ S.M ∧ S.FutCausal (γ t) (deriv γ t)) :
    ∃ η : ℝ → V, S.tc3_Causal Θ (Θ (γ 0)) (Θ (γ 1)) η ∧ η (Θ (γ 0)) = γ 0 ∧
      η (Θ (γ 1)) = γ 1 ∧ Θ (γ 0) < Θ (γ 1) := by
  set f : ℝ → ℝ := fun u => Θ (γ u) with hfdef
  have hdiff : Differentiable ℝ γ := hγ.differentiable one_ne_zero
  have hfd : ∀ u ∈ Icc (0:ℝ) 1, HasDerivAt f (fderiv ℝ Θ (γ u) (deriv γ u)) u := fun u hu =>
    (((hΘ.1.contDiffAt (S.isOpen_M.mem_nhds (hd u hu).1)).differentiableAt
      one_ne_zero).hasFDerivAt).comp_hasDerivAt u (hdiff u).hasDerivAt
  have hfc : ContinuousOn f (Icc 0 1) :=
    hΘ.1.continuousOn.comp hγ.continuous.continuousOn fun u hu => (hd u hu).1
  have hmono : StrictMonoOn f (Icc 0 1) := by
    refine strictMonoOn_of_deriv_pos (convex_Icc 0 1) hfc fun u hu => ?_
    rw [interior_Icc] at hu
    rw [(hfd u (Ioo_subset_Icc_self hu)).deriv]
    exact hΘ.2 _ (hd u (Ioo_subset_Icc_self hu)).1 _ (hd u (Ioo_subset_Icc_self hu)).2
  have h01 : f 0 < f 1 := hmono ⟨le_rfl, zero_le_one⟩ ⟨zero_le_one, le_rfl⟩ zero_lt_one
  have hex : ∀ σ ∈ Icc (f 0) (f 1), ∃ u ∈ Icc (0:ℝ) 1, f u = σ :=
    fun σ hσ => intermediate_value_Icc zero_le_one hfc hσ
  set θ := Function.invFunOn f (Icc (0:ℝ) 1) with hθdef
  have hθ : ∀ σ ∈ Icc (f 0) (f 1), θ σ ∈ Icc (0:ℝ) 1 ∧ f (θ σ) = σ :=
    fun σ hσ => Function.invFunOn_pos (hex σ hσ)
  have hθf : ∀ u ∈ Icc (0:ℝ) 1, θ (f u) = u := fun u hu =>
    hmono.injOn (hθ _ ⟨hmono.monotoneOn ⟨le_rfl, zero_le_one⟩ hu hu.1,
      hmono.monotoneOn hu ⟨zero_le_one, le_rfl⟩ hu.2⟩).1 hu
      (hθ _ ⟨hmono.monotoneOn ⟨le_rfl, zero_le_one⟩ hu hu.1,
        hmono.monotoneOn hu ⟨zero_le_one, le_rfl⟩ hu.2⟩).2
  have hfI : ∀ u ∈ Icc (0:ℝ) 1, f u ∈ Icc (f 0) (f 1) := fun u hu =>
    ⟨hmono.monotoneOn ⟨le_rfl, zero_le_one⟩ hu hu.1, hmono.monotoneOn hu ⟨zero_le_one, le_rfl⟩ hu.2⟩
  -- continuity of `θ` from the closed embedding `f|[0,1]`
  have hθc : ContinuousOn θ (Icc (f 0) (f 1)) := by
    let F : Icc (0:ℝ) 1 → ℝ := fun u => f u
    have hFc : Continuous F := hfc.domRestrict
    have hFi : Function.Injective F := fun a b h => Subtype.ext (hmono.injOn a.2 b.2 h)
    have hemb := hFc.isClosedEmbedding hFi
    let θ' : Icc (f 0) (f 1) → Icc (0:ℝ) 1 := fun σ => ⟨θ σ, (hθ σ σ.2).1⟩
    have hθ' : Continuous θ' := hemb.isEmbedding.continuous_iff.2 (by
      have : F ∘ θ' = fun σ : Icc (f 0) (f 1) => (σ : ℝ) := funext fun σ => (hθ σ σ.2).2
      rw [this]; exact continuous_subtype_val)
    rw [continuousOn_iff_continuous_domRestrict]
    exact continuous_subtype_val.comp hθ'
  refine ⟨fun σ => γ (θ σ), ⟨?_, ?_, ?_, ?_⟩, by show γ (θ (f 0)) = γ 0; rw [hθf 0 ⟨le_rfl, zero_le_one⟩],
    by show γ (θ (f 1)) = γ 1; rw [hθf 1 ⟨zero_le_one, le_rfl⟩], h01⟩
  · exact hγ.continuous.comp_continuousOn hθc
  · intro σ hσ
    show f (θ σ) = f (θ (f 0)) + (σ - f 0)
    rw [(hθ σ hσ).2, (hθ _ ⟨le_rfl, h01.le⟩).2]
    ring
  · intro σ hσ; exact (hd _ (hθ σ hσ).1).1
  · intro B c hBc s t hs hst ht hin
    have hs' := hθ s ⟨hs, hst.trans ht⟩
    have ht' := hθ t ⟨hs.trans hst, ht⟩
    have hle : θ s ≤ θ t := by
      by_contra hlt
      push Not at hlt
      have := hmono ht'.1 hs'.1 hlt
      rw [hs'.2, ht'.2] at this
      linarith
    rcases le_or_gt c 0 with hc0 | hc0
    · have h1 : c * ‖γ (θ t) - γ (θ s)‖ ≤ 0 := mul_nonpos_of_nonpos_of_nonneg hc0 (norm_nonneg _)
      show c * ‖γ (θ t) - γ (θ s)‖ ≤ f (θ t) - f (θ s)
      rw [hs'.2, ht'.2]; linarith
    · have hb := S.tc3_arc_bound hΘ hc0 hγ (a := θ s) (b := θ t) fun u hu => by
        have hu01 : u ∈ Icc (0:ℝ) 1 := ⟨hs'.1.1.trans hu.1, hu.2.trans ht'.1.2⟩
        have hfu : f u ∈ Icc s t := by
          constructor
          · rw [← hs'.2]; exact hmono.monotoneOn hs'.1 hu01 hu.1
          · rw [← ht'.2]; exact hmono.monotoneOn hu01 ht'.1 hu.2
        have hmem : γ u ∈ B := by
          have := hin (f u) hfu
          simp only at this
          rwa [hθf u hu01] at this
        exact ⟨(hd u hu01).1, hBc.2.2 _ hmem _ (hd u hu01).2⟩
      exact hb _ _ le_rfl hle le_rfl

/-- Concatenation of `Θ`-causal curves. -/
theorem tc3_causal_concat {Θ : V → ℝ} {a b d : ℝ} (hab : a ≤ b) (hbd : b ≤ d) {η₁ η₂ : ℝ → V}
    (h1 : S.tc3_Causal Θ a b η₁) (h2 : S.tc3_Causal Θ b d η₂) (heq : η₁ b = η₂ b) :
    S.tc3_Causal Θ a d (fun s => if s ≤ b then η₁ s else η₂ s) := by
  obtain ⟨c1, P1, M1, B1⟩ := h1
  obtain ⟨c2, P2, M2, B2⟩ := h2
  have e1 : EqOn (fun s => if s ≤ b then η₁ s else η₂ s) η₁ (Icc a b) := fun s hs => by
    simp only [hs.2, ↓reduceIte]
  have e2 : EqOn (fun s => if s ≤ b then η₁ s else η₂ s) η₂ (Icc b d) := fun s hs => by
    by_cases h : s ≤ b
    · simp only [h, ↓reduceIte]; rw [le_antisymm h hs.1, heq]
    · simp only [h, ↓reduceIte]
  refine ⟨?_, fun s hs => ?_, fun s hs => ?_, fun B c hBc s t hs hst ht hin => ?_⟩
  · rw [← Icc_union_Icc_eq_Icc hab hbd]
    exact (c1.congr e1).union_of_isClosed (c2.congr e2) isClosed_Icc isClosed_Icc
  · simp only [hab, ↓reduceIte]
    by_cases hsb : s ≤ b
    · simp only [hsb, ↓reduceIte]; exact P1 s ⟨hs.1, hsb⟩
    · simp only [hsb, ↓reduceIte]
      rw [P2 s ⟨le_of_not_ge hsb, hs.2⟩, ← heq, P1 b ⟨hab, le_rfl⟩]; ring
  · by_cases hsb : s ≤ b
    · simp only [hsb, ↓reduceIte]; exact M1 s ⟨hs.1, hsb⟩
    · simp only [hsb, ↓reduceIte]; exact M2 s ⟨le_of_not_ge hsb, hs.2⟩
  · by_cases htb : t ≤ b
    · simp only [htb, hst.trans htb, ↓reduceIte]
      exact B1 B c hBc s t hs hst htb fun u hu => by
        have := hin u hu; simpa only [hu.2.trans htb, ↓reduceIte] using this
    · by_cases hsb : s ≤ b
      · simp only [htb, hsb, ↓reduceIte]
        have i1 := B2 B c hBc b t le_rfl (le_of_not_ge htb) ht fun u hu => by
          have := hin u ⟨hsb.trans hu.1, hu.2⟩
          rw [← e2 ⟨hu.1, hu.2.trans ht⟩]; exact this
        have i2 := B1 B c hBc s b hs hsb le_rfl fun u hu => by
          have := hin u ⟨hu.1, hu.2.trans (le_of_not_ge htb)⟩
          rw [← e1 ⟨hs.trans hu.1, hu.2⟩]; exact this
        have e : η₂ t - η₁ s = (η₂ t - η₂ b) + (η₁ b - η₁ s) := by rw [heq]; abel
        have hΘe : Θ (η₂ b) = Θ (η₁ b) := by rw [heq]
        have hBcpos : 0 ≤ c ∨ c < 0 := le_or_gt 0 c
        rw [e]
        rcases hBcpos with hc | hc
        · nlinarith [mul_le_mul_of_nonneg_left (norm_add_le (η₂ t - η₂ b) (η₁ b - η₁ s)) hc]
        · have : Θ (η₂ t) - Θ (η₁ s) ≥ 0 := by
            rw [P2 t ⟨(le_of_not_ge htb), ht⟩, ← heq, P1 b ⟨hab, le_rfl⟩, P1 s ⟨hs, hsb⟩]
            linarith [(le_of_not_ge htb)]
          nlinarith [norm_nonneg (η₂ t - η₂ b + (η₁ b - η₁ s))]
      · simp only [htb, hsb, ↓reduceIte]
        exact B2 B c hBc s t (le_of_not_ge hsb) hst ht fun u hu => by
          have := hin u hu
          rw [← e2 ⟨(le_of_not_ge hsb).trans hu.1, hu.2.trans ht⟩]; exact this

/-- **Chains are `Θ`-causal curves.** A chain of `S` from `x ∈ M` gives a `Θ`-causal curve on
`[Θ x, Θ y]` from `x` to `y`. -/
theorem tc3_chain_causal {Θ : V → ℝ} (hΘ : S.IsTemporal Θ) {x y : V} (hx : x ∈ S.M)
    (h : S.Cau x y) :
    ∃ η : ℝ → V, S.tc3_Causal Θ (Θ x) (Θ y) η ∧ η (Θ x) = x ∧ η (Θ y) = y ∧ Θ x ≤ Θ y := by
  induction h with
  | refl =>
    refine ⟨fun _ => x, ⟨continuousOn_const, fun s hs => ?_, fun _ _ => hx,
      fun B c _ s t hs hst ht _ => ?_⟩, rfl, rfl, le_rfl⟩
    · have : s = Θ x := le_antisymm hs.2 hs.1
      simp [this]
    · simp
  | @tail y z _ hst ih =>
    obtain ⟨η₁, h1, h1a, h1b, hle1⟩ := ih
    obtain ⟨γ, hγ, h0, h1', hd⟩ := hst
    obtain ⟨η₂, h2, h2a, h2b, hlt2⟩ := S.tc3_arc_causal hΘ hγ hd
    subst h0; subst h1'
    refine ⟨fun s => if s ≤ Θ (γ 0) then η₁ s else η₂ s,
      tc3_causal_concat hle1 hlt2.le h1 h2 (by rw [h1b, h2a]), ?_, ?_, hle1.trans hlt2.le⟩
    · simp only [hle1, ↓reduceIte]; exact h1a
    · simp only [not_le.2 hlt2, ↓reduceIte]; exact h2b

/-- Restriction of a `Θ`-causal curve to a sub-interval. -/
lemma tc3_causal_sub {Θ : V → ℝ} {a b a' b' : ℝ} {η : ℝ → V} (h : S.tc3_Causal Θ a b η)
    (ha : a ≤ a') (hb : b' ≤ b) (hab' : a' ≤ b') : S.tc3_Causal Θ a' b' η := by
  obtain ⟨hc, hP, hM, hB⟩ := h
  have hsub : Icc a' b' ⊆ Icc a b := Icc_subset_Icc ha hb
  refine ⟨hc.mono hsub, fun s hs => ?_, fun s hs => hM s (hsub hs),
    fun B c hBc s t hs hst ht hin => hB B c hBc s t (ha.trans hs) hst (ht.trans hb) hin⟩
  rw [hP s (hsub hs), hP a' (hsub ⟨le_rfl, hab'⟩)]; ring

/-- Shift of a `Θ`-causal curve to start at parameter `0`. -/
lemma tc3_causal_shift {Θ : V → ℝ} {a b : ℝ} {η : ℝ → V} (h : S.tc3_Causal Θ a b η) :
    S.tc3_Causal Θ 0 (b - a) (fun s => η (a + s)) := by
  obtain ⟨hc, hP, hM, hB⟩ := h
  have hmap : MapsTo (fun s => a + s) (Icc 0 (b - a)) (Icc a b) := fun s hs =>
    ⟨by linarith [hs.1], by linarith [hs.2]⟩
  refine ⟨hc.comp (continuous_const.add continuous_id).continuousOn hmap, fun s hs => ?_,
    fun s hs => hM _ (hmap hs), fun B c hBc s t hs hst ht hin => ?_⟩
  · simp only [add_zero]
    rw [hP _ (hmap hs), hP a ⟨le_rfl, by linarith [hs.1, hs.2]⟩]; ring
  · exact hB B c hBc (a + s) (a + t) (by linarith) (by linarith) (by linarith) fun u hu => by
      have := hin (u - a) ⟨by linarith [hu.1], by linarith [hu.2]⟩
      simpa using this

/-- **The stay lemma.** A `Θ`-causal curve starting within `ρ/3` of `q`, where `ball q ρ` is a cone
set with constant `c`, stays within `2ρ/3` of `q` for `Θ`-time `cρ/3`. -/
theorem tc3_stay {Θ : V → ℝ} {a b : ℝ} {η : ℝ → V} (hη : S.tc3_Causal Θ a b η) {q : V}
    {ρ c : ℝ} (hc : 0 < c) (hB : S.tc3_ConeSet Θ (ball q ρ) c) (h0 : dist (η a) q < ρ / 3) :
    ∀ t₁ ∈ Icc a b, t₁ ≤ a + c * (ρ / 3) → dist (η t₁) q ≤ 2 * ρ / 3 := by
  obtain ⟨hcont, hP, hM, hLB⟩ := hη
  have hρ : 0 < ρ := by have := dist_nonneg.trans_lt h0; linarith
  intro t₁ ht₁ ht₁a
  by_contra hout
  push Not at hout
  set A := Icc a t₁ ∩ η ⁻¹' {y | 2 * ρ / 3 ≤ dist y q} with hAdef
  have hAc : IsClosed A := (hcont.mono (Icc_subset_Icc le_rfl ht₁.2)).preimage_isClosed_of_isClosed
    isClosed_Icc (isClosed_le continuous_const (continuous_id.dist continuous_const))
  have hA1 : t₁ ∈ A := ⟨⟨ht₁.1, le_rfl⟩, hout.le⟩
  have hAb : BddBelow A := ⟨a, fun u hu => hu.1.1⟩
  set ts := sInf A with hts
  have hmem : ts ∈ A := hAc.csInf_mem ⟨t₁, hA1⟩ hAb
  have hmem2 : 2 * ρ / 3 ≤ dist (η ts) q := hmem.2
  have hlt0 : a < ts := by
    rcases hmem.1.1.lt_or_eq with h | h
    · exact h
    · exfalso; rw [← h] at hmem2; linarith
  have hbefore : ∀ u ∈ Ico a ts, dist (η u) q < 2 * ρ / 3 := by
    intro u hu
    by_contra hu'
    push Not at hu'
    have : u ∈ A := ⟨⟨hu.1, hu.2.le.trans hmem.1.2⟩, hu'⟩
    exact absurd (csInf_le hAb this) (not_le.2 hu.2)
  have htsb : ts ≤ b := hmem.1.2.trans ht₁.2
  have hcw : ContinuousWithinAt η (Ico a ts) ts :=
    (hcont ts ⟨hlt0.le, htsb⟩).mono fun u hu => ⟨hu.1, hu.2.le.trans htsb⟩
  have hcl : ts ∈ closure (Ico a ts) := by rw [closure_Ico hlt0.ne]; exact ⟨hlt0.le, le_rfl⟩
  have hγs : dist (η ts) q ≤ 2 * ρ / 3 := by
    have h := hcw.mem_closure_image hcl
    have hsub : η '' Ico a ts ⊆ closedBall q (2 * ρ / 3) := by
      rintro _ ⟨u, hu, rfl⟩; exact (hbefore u hu).le
    exact (closure_minimal hsub isClosed_closedBall) h
  have hin : ∀ u ∈ Icc a ts, η u ∈ ball q ρ := by
    intro u hu
    rcases hu.2.lt_or_eq with h | h
    · exact mem_ball.2 ((hbefore u ⟨hu.1, h⟩).trans (by linarith))
    · rw [h]; exact mem_ball.2 (hγs.trans_lt (by linarith))
  have hb := hLB _ _ hB a ts le_rfl hlt0.le htsb hin
  rw [tc3_Param_mono hP ⟨le_rfl, hlt0.le.trans htsb⟩ ⟨hlt0.le, htsb⟩] at hb
  have hnorm : ‖η ts - η a‖ ≤ ρ / 3 := by
    have : c * ‖η ts - η a‖ ≤ c * (ρ / 3) := by linarith [hmem.1.2]
    exact le_of_mul_le_mul_left this hc
  have := dist_triangle (η ts) (η a) q
  rw [dist_eq_norm (η ts) (η a)] at this
  linarith

/-- On the stay interval, a `Θ`-causal curve is `1/c`-Lipschitz. -/
theorem tc3_stay_lip {Θ : V → ℝ} {a b : ℝ} {η : ℝ → V} (hη : S.tc3_Causal Θ a b η) {q : V}
    {ρ c : ℝ} (hc : 0 < c) (hB : S.tc3_ConeSet Θ (ball q ρ) c) (h0 : dist (η a) q < ρ / 3)
    {s t : ℝ} (hs : s ∈ Icc a b) (ht : t ∈ Icc a b) (hsa : s ≤ a + c * (ρ / 3))
    (hta : t ≤ a + c * (ρ / 3)) : ‖η t - η s‖ ≤ |t - s| / c := by
  have hρ : 0 < ρ := by have := dist_nonneg.trans_lt h0; linarith
  have hst := S.tc3_stay hη hc hB h0
  have key : ∀ s t, s ∈ Icc a b → t ∈ Icc a b → s ≤ t → t ≤ a + c * (ρ / 3) →
      c * ‖η t - η s‖ ≤ t - s := fun s t hs ht h hta => by
    have hb := hη.2.2.2 _ _ hB s t hs.1 h ht.2 fun u hu =>
      mem_ball.2 ((hst u ⟨hs.1.trans hu.1, hu.2.trans ht.2⟩ (hu.2.trans hta)).trans_lt
        (by linarith))
    rwa [tc3_Param_mono hη.2.1 hs ht] at hb
  rcases le_total s t with h | h
  · rw [abs_of_nonneg (sub_nonneg.2 h), le_div_iff₀ hc, mul_comm]; exact key s t hs ht h hta
  · rw [norm_sub_rev, abs_of_nonpos (sub_nonpos.2 h), le_div_iff₀ hc, mul_comm]
    linarith [key t s ht hs h hsa]

/-- **Limits of `Θ`-causal curves are `Θ`-causal** (uniformly on `[a, b]`, limit values in `M`). -/
theorem tc3_causal_limit {Θ : V → ℝ} (hΘ : S.IsTemporal Θ) {a b : ℝ} {ηs : ℕ → ℝ → V}
    {γ : ℝ → V} (hη : ∀ n, S.tc3_Causal Θ a b (ηs n))
    (hu : TendstoUniformlyOn ηs γ atTop (Icc a b)) (hγM : ∀ s ∈ Icc a b, γ s ∈ S.M) :
    S.tc3_Causal Θ a b γ := by
  have hpt : ∀ s ∈ Icc a b, Tendsto (fun n => ηs n s) atTop (𝓝 (γ s)) :=
    fun s hs => hu.tendsto_at hs
  have hΘt : ∀ s ∈ Icc a b, Tendsto (fun n => Θ (ηs n s)) atTop (𝓝 (Θ (γ s))) :=
    fun s hs => (S.tc3_contAt hΘ (hγM s hs)).tendsto.comp (hpt s hs)
  have hcont : ContinuousOn γ (Icc a b) :=
    hu.continuousOn (Eventually.of_forall fun n => (hη n).1).frequently
  refine ⟨hcont, fun s hs => ?_, hγM, fun B c hBc s t hs hst ht hin => ?_⟩
  · have ha : a ∈ Icc a b := ⟨le_rfl, hs.1.trans hs.2⟩
    refine tendsto_nhds_unique (hΘt s hs) (((hΘt a ha).add_const (s - a)).congr fun n => ?_)
    exact ((hη n).2.1 s hs).symm
  · have hsub : Icc s t ⊆ Icc a b := Icc_subset_Icc hs ht
    have hKc : IsCompact (γ '' Icc s t) := isCompact_Icc.image_of_continuousOn (hcont.mono hsub)
    obtain ⟨ε, hε, hthick⟩ := hKc.exists_thickening_subset_open hBc.1
      (by rintro _ ⟨u, hu, rfl⟩; exact hin u hu)
    have hev := (Metric.tendstoUniformlyOn_iff.1 hu) ε hε
    have hs' : s ∈ Icc a b := ⟨hs, hst.trans ht⟩
    have ht' : t ∈ Icc a b := ⟨hs.trans hst, ht⟩
    refine le_of_tendsto_of_tendsto (((continuous_norm.tendsto _).comp
      ((hpt t ht').sub (hpt s hs'))).const_mul c) ((hΘt t ht').sub (hΘt s hs')) ?_
    filter_upwards [hev] with n hn
    refine (hη n).2.2.2 B c hBc s t hs hst ht fun u hu => hthick ?_
    exact Metric.mem_thickening_iff.2 ⟨γ u, ⟨u, hu, rfl⟩, by rw [dist_comm]; exact hn u (hsub hu)⟩

/-- **Uniform cone sets on a compact `K ⊆ M`.** -/
theorem tc3_uniform_cone [FiniteDimensional ℝ V] {Θ : V → ℝ} (hΘ : S.IsTemporal Θ) {K : Set V}
    (hK : IsCompact K) (hKM : K ⊆ S.M) :
    ∃ ρ > 0, ∃ c > 0, ∀ x ∈ K, S.tc3_ConeSet Θ (ball x ρ) c := by
  rcases K.eq_empty_or_nonempty with hKe | hKne
  · exact ⟨1, one_pos, 1, one_pos, by simp [hKe]⟩
  have hT1 := fun x : K => S.tc3_cone hΘ (hKM x.2)
  choose r hr c hc hcl hcone using hT1
  obtain ⟨t, ht⟩ := hK.elim_finite_subcover (fun x : K => ball (x : V) (r x / 2))
    (fun _ => isOpen_ball) (fun y hy => mem_iUnion.2 ⟨⟨y, hy⟩, mem_ball_self (half_pos (hr _))⟩)
  obtain ⟨y₀, hy₀⟩ := hKne
  have htne : t.Nonempty := by
    obtain ⟨i, hi, -⟩ := mem_iUnion₂.1 (ht hy₀)
    exact ⟨i, hi⟩
  refine ⟨t.inf' htne (fun i => r i / 2), (Finset.lt_inf'_iff htne).2 fun i _ => half_pos (hr i),
    t.inf' htne c, (Finset.lt_inf'_iff htne).2 fun i _ => hc i, fun x hx => ?_⟩
  obtain ⟨i, hi, hxi⟩ := mem_iUnion₂.1 (ht hx)
  have hρ : t.inf' htne (fun i => r i / 2) ≤ r i / 2 := Finset.inf'_le _ hi
  have hsub : ball x (t.inf' htne (fun i => r i / 2)) ⊆ ball (i : V) (r i) := by
    intro z hz
    rw [mem_ball] at hz hxi ⊢
    linarith [dist_triangle z x i]
  refine ⟨isOpen_ball, hsub.trans (ball_subset_closedBall.trans (hcl i)), fun z hz v hv => ?_⟩
  have := hcone i z (hsub hz) v hv
  have hcle : t.inf' htne c ≤ c i := Finset.inf'_le _ hi
  nlinarith [norm_nonneg v]

omit [NormedSpace ℝ V] in
/-- A subsequence of a uniformly convergent sequence converges uniformly. -/
lemma tc3_unif_subseq {F : ℕ → ℝ → V} {f : ℝ → V} {X : Set ℝ}
    (h : TendstoUniformlyOn F f atTop X) {χ : ℕ → ℕ} (hχ : StrictMono χ) :
    TendstoUniformlyOn (fun n => F (χ n)) f atTop X := by
  rw [Metric.tendstoUniformlyOn_iff] at h ⊢
  exact fun ε hε => hχ.tendsto_atTop.eventually (h ε hε)

omit [NormedSpace ℝ V] in
lemma tc3_unif_union {F : ℕ → ℝ → V} {f : ℝ → V} {X Y : Set ℝ}
    (h1 : TendstoUniformlyOn F f atTop X) (h2 : TendstoUniformlyOn F f atTop Y) :
    TendstoUniformlyOn F f atTop (X ∪ Y) := by
  rw [Metric.tendstoUniformlyOn_iff] at h1 h2 ⊢
  intro ε hε
  filter_upwards [h1 ε hε, h2 ε hε] with n hn1 hn2
  rintro x (hx | hx)
  · exact hn1 x hx
  · exact hn2 x hx

lemma tc3_causal_congr {Θ : V → ℝ} {a b : ℝ} {η η' : ℝ → V} (h : S.tc3_Causal Θ a b η)
    (he : EqOn η η' (Icc a b)) (hab : a ≤ b) : S.tc3_Causal Θ a b η' := by
  obtain ⟨hc, hP, hM, hB⟩ := h
  refine ⟨hc.congr fun x hx => (he hx).symm, fun s hs => ?_, fun s hs => he hs ▸ hM s hs,
    fun B c hBc s t hs hst ht hin => ?_⟩
  · rw [← he hs, ← he ⟨le_rfl, hab⟩]; exact hP s hs
  · have hs' : s ∈ Icc a b := ⟨hs, hst.trans ht⟩
    have ht' : t ∈ Icc a b := ⟨hs.trans hst, ht⟩
    rw [← he hs', ← he ht']
    exact hB B c hBc s t hs hst ht fun u hu => by
      rw [he ⟨hs.trans hu.1, hu.2.trans ht⟩]; exact hin u hu

/-- **Row T6 (one step).** A subsequence converging uniformly on `[0, T]` to a `Θ`-causal `γ`
extends, on a further subsequence, by `Θ`-time `c ρ/3` past `T`, where `ball (γ T) ρ` is a cone
set with constant `c`. -/
theorem tc3_step [FiniteDimensional ℝ V] {Θ : V → ℝ} (hΘ : S.IsTemporal Θ) {ηs : ℕ → ℝ → V}
    {Ls : ℕ → ℝ} (hη : ∀ n, S.tc3_Causal Θ 0 (Ls n) (ηs n)) (hLs : Tendsto Ls atTop atTop)
    {T : ℝ} (hT : 0 ≤ T) {ψ : ℕ → ℕ} (hψ : StrictMono ψ) {γ : ℝ → V}
    (hu : TendstoUniformlyOn (fun n => ηs (ψ n)) γ atTop (Icc 0 T)) (hγ : S.tc3_Causal Θ 0 T γ)
    {ρ c : ℝ} (hρ : 0 < ρ) (hc : 0 < c) (hB : S.tc3_ConeSet Θ (ball (γ T) ρ) c) :
    ∃ χ : ℕ → ℕ, StrictMono χ ∧ ∃ γ' : ℝ → V,
      TendstoUniformlyOn (fun n => ηs (ψ (χ n))) γ' atTop (Icc 0 (T + c * (ρ / 3))) ∧
      S.tc3_Causal Θ 0 (T + c * (ρ / 3)) γ' ∧ EqOn γ' γ (Icc 0 T) := by
  set q := γ T with hqdef
  set δ := c * (ρ / 3) with hδdef
  have hδ : 0 < δ := by positivity
  have hT' : T ∈ Icc 0 T := ⟨hT, le_rfl⟩
  have hq : Tendsto (fun n => ηs (ψ n) T) atTop (𝓝 q) := hu.tendsto_at hT'
  have ev : ∀ᶠ n in atTop, dist (ηs (ψ n) T) q < ρ / 3 ∧ T + δ ≤ Ls (ψ n) :=
    (Metric.tendsto_nhds.1 hq _ (by positivity)).and
      ((hLs.comp hψ.tendsto_atTop).eventually (eventually_ge_atTop _))
  obtain ⟨N, hN⟩ := eventually_atTop.1 ev
  have hNn : ∀ n, dist (ηs (ψ (n + N)) T) q < ρ / 3 ∧ T + δ ≤ Ls (ψ (n + N)) :=
    fun n => hN (n + N) (Nat.le_add_left N n)
  have hsub : ∀ n, S.tc3_Causal Θ T (Ls (ψ (n + N))) (ηs (ψ (n + N))) := fun n =>
    tc3_causal_sub (hη _) hT le_rfl (by linarith [(hNn n).2])
  have hsub' : ∀ n, S.tc3_Causal Θ T (T + δ) (ηs (ψ (n + N))) := fun n =>
    tc3_causal_sub (hη _) hT (hNn n).2 (by linarith)
  have hval : ∀ n, ∀ s ∈ Icc T (T + δ), ηs (ψ (n + N)) s ∈ closedBall q (2 * ρ / 3) :=
    fun n s hs => mem_closedBall.2 (S.tc3_stay (hsub n) hc hB (hNn n).1 s
      ⟨hs.1, hs.2.trans (hNn n).2⟩ hs.2)
  have hlip : ∀ n, ∀ s ∈ Icc T (T + δ), ∀ t ∈ Icc T (T + δ),
      ‖ηs (ψ (n + N)) t - ηs (ψ (n + N)) s‖ ≤ |t - s| / c := fun n s hs t ht =>
    S.tc3_stay_lip (hsub n) hc hB (hNn n).1 ⟨hs.1, hs.2.trans (hNn n).2⟩
      ⟨ht.1, ht.2.trans (hNn n).2⟩ hs.2 ht.2
  obtain ⟨χ₀, g, hχ₀, hg⟩ := tc3_AA (by linarith : T ≤ T + δ) hc hval hlip
  set χ : ℕ → ℕ := fun n => χ₀ n + N with hχdef
  have hχ : StrictMono χ := fun a b h => Nat.add_lt_add_right (hχ₀ h) N
  have hg' : TendstoUniformlyOn (fun n => ηs (ψ (χ n))) g atTop (Icc T (T + δ)) := hg
  have hTδ : T ∈ Icc T (T + δ) := ⟨le_rfl, by linarith⟩
  have hgT : g T = q := tendsto_nhds_unique (hg'.tendsto_at hTδ) (hq.comp hχ.tendsto_atTop)
  have hgM : ∀ s ∈ Icc T (T + δ), g s ∈ S.M := fun s hs =>
    hB.2.1 (closedBall_subset_ball (by linarith : 2 * ρ / 3 < ρ)
      (isClosed_closedBall.mem_of_tendsto (hg'.tendsto_at hs)
        (Eventually.of_forall fun n => hval (χ₀ n) s hs)))
  have hgc : S.tc3_Causal Θ T (T + δ) g :=
    S.tc3_causal_limit hΘ (fun n => hsub' (χ₀ n)) hg' hgM
  refine ⟨χ, hχ, fun s => if s ≤ T then γ s else g s, ?_,
    tc3_causal_concat hT (by linarith) hγ hgc hgT.symm, fun s hs => by simp only [hs.2, ↓reduceIte]⟩
  rw [← Icc_union_Icc_eq_Icc hT (by linarith : T ≤ T + δ)]
  refine tc3_unif_union ((tc3_unif_subseq hu hχ).congr_right fun s hs => ?_)
    (hg'.congr_right fun s hs => ?_)
  · simp only [hs.2, ↓reduceIte]
  · by_cases h : s ≤ T
    · simp only [h, ↓reduceIte]; rw [le_antisymm h hs.1, hgT]
    · simp only [h, ↓reduceIte]

/-- A positive lower bound for finitely many positive numbers. -/
lemma tc3_min_pos (f : ℕ → ℝ) (hf : ∀ m, 0 < f m) (M₀ : ℕ) : ∃ d > 0, ∀ m ≤ M₀, d ≤ f m := by
  induction M₀ with
  | zero => exact ⟨f 0, hf 0, fun m hm => by rw [Nat.le_zero.1 hm]⟩
  | succ k ih =>
    obtain ⟨d, hd, hdk⟩ := ih
    refine ⟨min d (f (k + 1)), lt_min hd (hf _), fun m hm => ?_⟩
    rcases Nat.lt_or_eq_of_le hm with h | h
    · exact (min_le_left _ _).trans (hdk m (Nat.lt_succ_iff.1 h))
    · rw [h]; exact min_le_right _ _

/-- **Row T6: the global limit curve.** In finite dimension, chains of `S` from `xₙ ∈ M`, `xₙ → p ∈ M`,
whose `Θ`-rise tends to `∞`, have `Θ`-causal parametrisations `ηₙ` on `[0, Lₙ]` and a subsequence
converging, uniformly on every `[0, Tⱼ]`, to one curve `γ` from `p` that is `Θ`-causal on every
`[0, Tⱼ]`, where `Tⱼ` is strictly increasing from `0`. Either `Tⱼ → ∞`, or `Tⱼ → T* < ∞` and `γ`
has no limit in `M` as `t → T*⁻`. -/
theorem tc3_global_limit [FiniteDimensional ℝ V] {Θ : V → ℝ} (hΘ : S.IsTemporal Θ)
    {xs ys : ℕ → V} {p : V} (hxM : ∀ n, xs n ∈ S.M) (hcau : ∀ n, S.Cau (xs n) (ys n))
    (hp : Tendsto xs atTop (𝓝 p)) (hpM : p ∈ S.M)
    (hL : Tendsto (fun n => Θ (ys n) - Θ (xs n)) atTop atTop) :
    ∃ (ηs : ℕ → ℝ → V) (φ : ℕ → ℕ) (γ : ℝ → V) (Ts : ℕ → ℝ),
      (∀ n, ηs n 0 = xs n ∧ S.tc3_Causal Θ 0 (Θ (ys n) - Θ (xs n)) (ηs n)) ∧ StrictMono φ ∧
      StrictMono Ts ∧ Ts 0 = 0 ∧ γ 0 = p ∧
      (∀ j, S.tc3_Causal Θ 0 (Ts j) γ ∧
        TendstoUniformlyOn (fun n => ηs (φ n)) γ atTop (Icc 0 (Ts j))) ∧
      (Tendsto Ts atTop atTop ∨ ∃ Tst : ℝ, Tendsto Ts atTop (𝓝 Tst) ∧ (∀ j, Ts j < Tst) ∧
        ¬ ∃ q ∈ S.M, Tendsto γ (𝓝[<] Tst) (𝓝 q)) := by
  classical
  -- the chain curves
  have hch := fun n => S.tc3_chain_causal hΘ (hxM n) (hcau n)
  choose η hηc hηa hηb hle using hch
  set Ls : ℕ → ℝ := fun n => Θ (ys n) - Θ (xs n) with hLsdef
  set ηs : ℕ → ℝ → V := fun n s => η n (Θ (xs n) + s) with hηsdef
  have hηs : ∀ n, S.tc3_Causal Θ 0 (Ls n) (ηs n) := fun n => tc3_causal_shift (hηc n)
  have hηs0 : ∀ n, ηs n 0 = xs n := fun n => by simp only [hηsdef, add_zero]; exact hηa n
  -- the exhaustion and its uniform cone constants
  have : ProperSpace V := FiniteDimensional.proper_real V
  have : LocallyCompactSpace S.M := S.isOpen_M.locallyCompactSpace
  have : SecondCountableTopology V := secondCountable_of_proper
  let Kx : CompactExhaustion S.M := CompactExhaustion.choice S.M
  have hcone : ∀ m, ∃ ρ > 0, ∃ c > 0, ∀ x ∈ (Subtype.val '' (Kx m) : Set V),
      S.tc3_ConeSet Θ (ball x ρ) c := fun m =>
    S.tc3_uniform_cone hΘ ((Kx.isCompact m).image continuous_subtype_val)
      (by rintro _ ⟨y, -, rfl⟩; exact y.2)
  choose ρ hρ c hc hcs using hcone
  let mi : V → ℕ := fun q => if hq : q ∈ S.M then Kx.find ⟨q, hq⟩ else 0
  have hmi : ∀ q (hq : q ∈ S.M), mi q = Kx.find ⟨q, hq⟩ := fun q hq => by simp [mi, hq]
  have hmiB : ∀ q (hq : q ∈ S.M), S.tc3_ConeSet Θ (ball q (ρ (mi q))) (c (mi q)) := fun q hq =>
    hcs _ q ⟨⟨q, hq⟩, by rw [hmi q hq]; exact Kx.mem_find _, rfl⟩
  set D : V → ℝ := fun q => c (mi q) * (ρ (mi q) / 3) with hDdef
  have hD : ∀ q, 0 < D q := fun q => by have := hc (mi q); have := hρ (mi q); positivity
  -- the state and the step
  let Inv : ℝ × (ℕ → ℕ) × (ℝ → V) → Prop := fun st =>
    0 ≤ st.1 ∧ StrictMono st.2.1 ∧
      TendstoUniformlyOn (fun n => ηs (st.2.1 n)) st.2.2 atTop (Icc 0 st.1) ∧
      S.tc3_Causal Θ 0 st.1 st.2.2 ∧ st.2.2 0 = p
  have stepEx : ∀ st : ℝ × (ℕ → ℕ) × (ℝ → V), Inv st → ∃ χ : ℕ → ℕ, StrictMono χ ∧
      ∃ γ' : ℝ → V, TendstoUniformlyOn (fun n => ηs (st.2.1 (χ n))) γ' atTop
        (Icc 0 (st.1 + D (st.2.2 st.1))) ∧ S.tc3_Causal Θ 0 (st.1 + D (st.2.2 st.1)) γ' ∧
        EqOn γ' st.2.2 (Icc 0 st.1) := fun st h =>
    S.tc3_step hΘ hηs hL h.1 h.2.1 h.2.2.1 h.2.2.2.1 (hρ _) (hc _)
      (hmiB _ (h.2.2.2.1.2.2.1 _ ⟨h.1, le_rfl⟩))
  choose! χf hχf γf hγf using stepEx
  let next : ℝ × (ℕ → ℕ) × (ℝ → V) → ℝ × (ℕ → ℕ) × (ℝ → V) := fun st =>
    (st.1 + D (st.2.2 st.1), st.2.1 ∘ χf st, γf st)
  let st0 : ℝ × (ℕ → ℕ) × (ℝ → V) := (0, id, fun _ => p)
  let seq : ℕ → ℝ × (ℕ → ℕ) × (ℝ → V) := fun j => next^[j] st0
  have hseq : ∀ j, seq (j + 1) = next (seq j) := fun j => Function.iterate_succ_apply' _ _ _
  have hInv0 : Inv st0 := by
    refine ⟨le_rfl, strictMono_id, ?_, ⟨continuousOn_const, fun s hs => ?_, fun _ _ => hpM,
      fun B c' _ s t hs hst ht _ => by show c' * ‖p - p‖ ≤ Θ p - Θ p; simp⟩, rfl⟩
    · show TendstoUniformlyOn (fun n => ηs n) (fun _ => p) atTop (Icc 0 0)
      rw [Icc_self, tendstoUniformlyOn_singleton_iff_tendsto]
      simpa [hηs0] using hp
    · have h0 : s = 0 := le_antisymm hs.2 hs.1
      subst h0; show Θ p = Θ p + (0 - 0); ring
  have hInv : ∀ j, Inv (seq j) := by
    intro j
    induction j with
    | zero => exact hInv0
    | succ k ih =>
      rw [hseq k]
      obtain ⟨h1, h2, h3⟩ := hγf _ ih
      exact ⟨by have := hD ((seq k).2.2 (seq k).1); linarith [ih.1], ih.2.1.comp (hχf _ ih), h1, h2,
        by show γf (seq k) 0 = p; rw [h3 ⟨le_rfl, ih.1⟩]; exact ih.2.2.2.2⟩
  set Ts : ℕ → ℝ := fun j => (seq j).1 with hTsdef
  set Ψ : ℕ → ℕ → ℕ := fun j => (seq j).2.1 with hΨdef
  set Γ : ℕ → ℝ → V := fun j => (seq j).2.2 with hΓdef
  have hTsucc : ∀ j, Ts (j + 1) = Ts j + D (Γ j (Ts j)) := fun j => by
    simp only [hTsdef, hΓdef, hseq j]; rfl
  have hΨsucc : ∀ j, Ψ (j + 1) = Ψ j ∘ χf (seq j) := fun j => by
    simp only [hΨdef, hseq j]; rfl
  have hΓsucc : ∀ j, EqOn (Γ (j + 1)) (Γ j) (Icc 0 (Ts j)) := fun j => by
    have := (hγf _ (hInv j)).2.2
    simp only [hΓdef, hTsdef, hseq j]; exact this
  have hTs : StrictMono Ts := strictMono_nat_of_lt_succ fun j => by
    rw [hTsucc j]; linarith [hD (Γ j (Ts j))]
  have hTs0 : Ts 0 = 0 := rfl
  have hagree : ∀ j k, j ≤ k → EqOn (Γ k) (Γ j) (Icc 0 (Ts j)) := by
    intro j k hjk
    induction k, hjk using Nat.le_induction with
    | base => exact fun _ _ => rfl
    | succ k hjk ih =>
      intro s hs
      rw [hΓsucc k ⟨hs.1, hs.2.trans (hTs.monotone hjk)⟩, ih hs]
  have hΨsub : ∀ j n, j ≤ n → ∀ m, ∃ k ≥ m, Ψ n m = Ψ j k := by
    intro j n hjn
    induction n, hjn using Nat.le_induction with
    | base => exact fun m => ⟨m, le_rfl, rfl⟩
    | succ n hjn ih =>
      intro m
      obtain ⟨k, hk, e⟩ := ih (χf (seq n) m)
      refine ⟨k, (hχf _ (hInv n)).id_le m |>.trans hk, ?_⟩
      rw [hΨsucc n]; exact e
  set φ : ℕ → ℕ := fun n => Ψ n n with hφdef
  have hφ : StrictMono φ := strictMono_nat_of_lt_succ fun n => by
    show Ψ (n + 1) (n + 1) > Ψ n n
    rw [hΨsucc n]
    exact (hInv n).2.1 (lt_of_lt_of_le (Nat.lt_succ_self n) ((hχf _ (hInv n)).id_le (n + 1)))
  -- the limit curve
  let γ : ℝ → V := fun s => if h : ∃ j, s ≤ Ts j then Γ (Nat.find h) s else p
  have hγΓ : ∀ j, EqOn γ (Γ j) (Icc 0 (Ts j)) := by
    intro j s hs
    have h : ∃ j, s ≤ Ts j := ⟨j, hs.2⟩
    simp only [γ, h, ↓reduceDIte]
    exact (hagree _ j (Nat.find_min' h hs.2) ⟨hs.1, Nat.find_spec h⟩).symm
  have hcaus : ∀ j, S.tc3_Causal Θ 0 (Ts j) γ := fun j =>
    tc3_causal_congr (hInv j).2.2.2.1 (fun s hs => (hγΓ j hs).symm) (hInv j).1
  have hunif : ∀ j, TendstoUniformlyOn (fun n => ηs (φ n)) γ atTop (Icc 0 (Ts j)) := by
    intro j
    refine TendstoUniformlyOn.congr_right ?_ (fun s hs => (hγΓ j hs).symm)
    have h := (hInv j).2.2.1
    rw [Metric.tendstoUniformlyOn_iff] at h ⊢
    intro ε hε
    obtain ⟨K, hK⟩ := eventually_atTop.1 (h ε hε)
    refine eventually_atTop.2 ⟨max j K, fun n hn => ?_⟩
    obtain ⟨k, hk, e⟩ := hΨsub j n (le_of_max_le_left hn) n
    show ∀ x ∈ Icc 0 (Ts j), dist (Γ j x) (ηs (Ψ n n) x) < ε
    rw [e]; exact hK k (le_trans (le_of_max_le_right hn) hk)
  have hγ0 : γ 0 = p := by
    rw [hγΓ 0 ⟨le_rfl, hTs0.symm.le⟩]; exact (hInv 0).2.2.2.2
  refine ⟨ηs, φ, γ, Ts, fun n => ⟨hηs0 n, hηs n⟩, hφ, hTs, hTs0, hγ0, fun j => ⟨hcaus j, hunif j⟩, ?_⟩
  -- the dichotomy
  by_cases hb : BddAbove (range Ts)
  · right
    set Tst := ⨆ j, Ts j with hTst
    have hlim : Tendsto Ts atTop (𝓝 Tst) := tendsto_atTop_ciSup hTs.monotone hb
    have hlt : ∀ j, Ts j < Tst := fun j => (hTs (Nat.lt_succ_self j)).trans_le (le_ciSup hb _)
    refine ⟨Tst, hlim, hlt, ?_⟩
    rintro ⟨q, hqM, hq⟩
    have hTsW : Tendsto Ts atTop (𝓝[<] Tst) :=
      tendsto_nhdsWithin_iff.2 ⟨hlim, Eventually.of_forall hlt⟩
    have hγM : ∀ j, γ (Ts j) ∈ S.M := fun j => (hcaus j).2.2.1 _ ⟨(hTs.monotone (Nat.zero_le j)).trans' hTs0.symm.le, le_rfl⟩
    have hsubt : Tendsto (fun j => (⟨γ (Ts j), hγM j⟩ : S.M)) atTop (𝓝 ⟨q, hqM⟩) :=
      tendsto_subtype_rng.2 (hq.comp hTsW)
    set m₀ := Kx.find ⟨q, hqM⟩
    have hnb : Kx (m₀ + 1) ∈ 𝓝 (⟨q, hqM⟩ : S.M) :=
      mem_interior_iff_mem_nhds.1 (Kx.subset_interior_succ _ (Kx.mem_find _))
    obtain ⟨d, hd, hdm⟩ := tc3_min_pos (fun m => c m * (ρ m / 3))
      (fun m => by have := hc m; have := hρ m; positivity) (m₀ + 1)
    have hev : ∀ᶠ j in atTop, d ≤ Ts (j + 1) - Ts j := by
      filter_upwards [hsubt.eventually hnb] with j hj
      have hm : mi (γ (Ts j)) ≤ m₀ + 1 := by
        rw [hmi _ (hγM j)]; exact Kx.mem_iff_find_le.1 hj
      rw [hTsucc j, ← hγΓ j ⟨(hTs.monotone (Nat.zero_le j)).trans' hTs0.symm.le, le_rfl⟩]
      have := hdm _ hm
      simp only [hDdef]; linarith
    obtain ⟨N, hN⟩ := eventually_atTop.1 hev
    have hgrow : ∀ k, Ts N + k * d ≤ Ts (N + k) := by
      intro k
      induction k with
      | zero => simp
      | succ k ih =>
        have := hN (N + k) (Nat.le_add_right N k)
        push_cast
        rw [← add_assoc]; linarith
    obtain ⟨B, hB⟩ := hb
    obtain ⟨k, hk⟩ := exists_nat_gt ((B - Ts N) / d)
    have h1 := hgrow k
    have h2 := hB ⟨N + k, rfl⟩
    rw [div_lt_iff₀ hd] at hk
    linarith
  · left
    rw [not_bddAbove_iff] at hb
    exact tendsto_atTop_atTop_of_monotone hTs.monotone fun b => by
      obtain ⟨_, ⟨j, rfl⟩, hj⟩ := hb b; exact ⟨j, hj.le⟩

/-- **Row T6 with T5: the global limit curve leaves every compact set.** Under `tc3_global_limit`'s
hypotheses the limit curve `γ` from `p` is defined (`Θ`-causal) on `[0, T*)` with `T* ≤ ∞`, and
eventually leaves every compact `K ⊆ M`: as `t → ∞` when `T* = ∞`, as `t → T*⁻` otherwise. -/
theorem tc3_global_escape [FiniteDimensional ℝ V] {Θ : V → ℝ} (hΘ : S.IsTemporal Θ)
    {xs ys : ℕ → V} {p : V} (hxM : ∀ n, xs n ∈ S.M) (hcau : ∀ n, S.Cau (xs n) (ys n))
    (hp : Tendsto xs atTop (𝓝 p)) (hpM : p ∈ S.M)
    (hL : Tendsto (fun n => Θ (ys n) - Θ (xs n)) atTop atTop) :
    ∃ (ηs : ℕ → ℝ → V) (φ : ℕ → ℕ) (γ : ℝ → V) (Ts : ℕ → ℝ),
      (∀ n, ηs n 0 = xs n ∧ S.tc3_Causal Θ 0 (Θ (ys n) - Θ (xs n)) (ηs n)) ∧ StrictMono φ ∧
      StrictMono Ts ∧ Ts 0 = 0 ∧ γ 0 = p ∧
      (∀ j, S.tc3_Causal Θ 0 (Ts j) γ ∧
        TendstoUniformlyOn (fun n => ηs (φ n)) γ atTop (Icc 0 (Ts j))) ∧
      ((Tendsto Ts atTop atTop ∧ ∀ K : Set V, IsCompact K → K ⊆ S.M → ∀ᶠ t in atTop, γ t ∉ K) ∨
        ∃ Tst : ℝ, Tendsto Ts atTop (𝓝 Tst) ∧ (∀ j, Ts j < Tst) ∧
          ∀ K : Set V, IsCompact K → K ⊆ S.M → ∀ᶠ t in 𝓝[<] Tst, γ t ∉ K) := by
  obtain ⟨ηs, φ, γ, Ts, h1, hφ, hTs, hTs0, hγ0, hj, hdich⟩ :=
    S.tc3_global_limit hΘ hxM hcau hp hpM hL
  refine ⟨ηs, φ, γ, Ts, h1, hφ, hTs, hTs0, hγ0, hj, ?_⟩
  rcases hdich with hinf | ⟨Tst, hlim, hlt, hinext⟩
  · refine Or.inl ⟨hinf, fun K hK hKM => S.tc3_nonimprison_top hΘ (fun t ht => ?_) hK hKM⟩
    obtain ⟨j, hjt⟩ := (hinf.eventually (eventually_ge_atTop t)).exists
    have := (hj j).1.2.1 t ⟨ht, hjt⟩
    rw [this]; ring
  · refine Or.inr ⟨Tst, hlim, hlt, fun K hK hKM => ?_⟩
    have hex : ∀ t < Tst, ∃ j, t < Ts j := fun t ht =>
      (hlim.eventually (lt_mem_nhds ht)).exists
    have hT : 0 < Tst := hTs0 ▸ hlt 0
    refine S.tc3_nonimprison (Θ := Θ) hT (fun t ht => ?_) (fun t ht => ?_) (fun x₀ hx₀ => ?_) hinext hK hKM
    · obtain ⟨j, hjt⟩ := hex t ht.2
      refine ((hj j).1.1 t ⟨ht.1, hjt.le⟩).mono_of_mem_nhdsWithin ?_
      exact mem_nhdsWithin.2 ⟨Iio (Ts j), isOpen_Iio, hjt, fun u hu => ⟨hu.2.1, hu.1.le⟩⟩
    · obtain ⟨j, hjt⟩ := hex t ht.2
      rw [(hj j).1.2.1 t ⟨ht.1, hjt.le⟩]; ring
    · obtain ⟨r, hr, c, hc, hcl, hcone⟩ := S.tc3_cone hΘ hx₀
      refine ⟨r, hr, c, hc, ball_subset_closedBall.trans hcl, fun s t hs hst ht hin => ?_⟩
      obtain ⟨j, hjt⟩ := hex t ht
      exact (hj j).1.2.2.2 _ _ ⟨isOpen_ball, ball_subset_closedBall.trans hcl, hcone⟩ s t hs hst
        hjt.le hin

end Spacetime

/-! ## Row T8: non-vacuity -/

section Witness

/-- `g(v, w) = −v₁w₁ + v₂w₂` on `ℝ × ℝ` (sup norm). -/
noncomputable def kc_g0 : ℝ × ℝ →L[ℝ] ℝ × ℝ →L[ℝ] ℝ :=
  -((ContinuousLinearMap.mul ℝ ℝ).bilinearComp (ContinuousLinearMap.fst ℝ ℝ ℝ)
    (ContinuousLinearMap.fst ℝ ℝ ℝ)) +
  (ContinuousLinearMap.mul ℝ ℝ).bilinearComp (ContinuousLinearMap.snd ℝ ℝ ℝ)
    (ContinuousLinearMap.snd ℝ ℝ ℝ)

lemma kc_g0_apply (v w : ℝ × ℝ) : kc_g0 v w = -(v.1 * w.1) + v.2 * w.2 := by
  simp [kc_g0]

/-- The 2D Minkowski chart: `M = ℝ²`, `g = diag(−1, 1)`, `T = (1, 0)`. -/
noncomputable def kc_mink : Spacetime (ℝ × ℝ) where
  M := univ
  isOpen_M := isOpen_univ
  g := fun _ => kc_g0
  cont_g := continuousOn_const
  symm := fun _ v w => by rw [kc_g0_apply, kc_g0_apply]; ring
  T := fun _ => (1, 0)
  cont_T := continuousOn_const
  T_timelike := fun _ _ => by rw [kc_g0_apply]; norm_num
  pos_on_perp := fun _ _ v hv hv0 => by
    rw [kc_g0_apply] at hv ⊢
    have h1 : v.1 = 0 := by simpa using hv
    have h2 : v.2 ≠ 0 := fun h2 => hv0 (Prod.ext h1 h2)
    rw [h1]; have := mul_self_pos.2 h2; linarith

lemma kc_mink_M (r : ℝ) : ball (0 : ℝ × ℝ) r ⊆ kc_mink.M := fun _ _ => mem_univ _

/-- `Θ(t, x) = t` is temporal for the 2D Minkowski chart. -/
theorem tc3_mink_temporal : kc_mink.IsTemporal (fun v : ℝ × ℝ => v.1) := by
  refine ⟨contDiff_fst.contDiffOn, fun x _ v hv => ?_⟩
  have h : fderiv ℝ (fun v : ℝ × ℝ => v.1) x = ContinuousLinearMap.fst ℝ ℝ ℝ :=
    (ContinuousLinearMap.fst ℝ ℝ ℝ).fderiv
  rw [h]
  have h2 := hv.2
  change kc_g0 v (1, 0) < 0 at h2
  rw [kc_g0_apply] at h2
  simp only [ContinuousLinearMap.coe_fst']
  linarith

/-- The straight chains `0 → (n + 1, 0)`. -/
lemma tc3_mink_cau (n : ℕ) : kc_mink.Cau 0 (((n:ℝ) + 1), 0) := by
  refine Relation.ReflTransGen.single ⟨fun t => t • (((n:ℝ) + 1), (0:ℝ)), contDiff_id.smul contDiff_const,
    by simp, by simp, fun t _ => ⟨mem_univ _, ?_⟩⟩
  have hd : deriv (fun t : ℝ => t • (((n:ℝ) + 1), (0:ℝ))) t = (((n:ℝ) + 1), 0) := by
    simpa using ((hasDerivAt_id t).smul_const (((n:ℝ) + 1), (0:ℝ))).deriv
  rw [hd]
  have hn : (0:ℝ) < (n:ℝ) + 1 := by positivity
  refine ⟨?_, ?_⟩
  · show kc_g0 _ _ ≤ 0; rw [kc_g0_apply]; simp only; nlinarith
  · show kc_g0 _ (1, 0) < 0; rw [kc_g0_apply]; simp only; linarith

/-- **Row T8.** T6–T5 are not vacuous: in the 2D Minkowski chart with `Θ = fst`, the chains
`0 → (n + 1, 0)` rise by `n + 1 → ∞`, so the global limit curve from `0` exists and eventually
leaves every compact set. -/
theorem tc3_witness :
    ∃ (γ : ℝ → ℝ × ℝ) (Ts : ℕ → ℝ), γ 0 = 0 ∧ StrictMono Ts ∧
      (∀ j, kc_mink.tc3_Causal (fun v : ℝ × ℝ => v.1) 0 (Ts j) γ) ∧
      ((Tendsto Ts atTop atTop ∧ ∀ K : Set (ℝ × ℝ), IsCompact K → K ⊆ kc_mink.M →
          ∀ᶠ t in atTop, γ t ∉ K) ∨
        ∃ Tst : ℝ, Tendsto Ts atTop (𝓝 Tst) ∧ ∀ K : Set (ℝ × ℝ), IsCompact K → K ⊆ kc_mink.M →
          ∀ᶠ t in 𝓝[<] Tst, γ t ∉ K) := by
  obtain ⟨_, _, γ, Ts, _, _, hTs, _, hγ0, hj, hd⟩ := kc_mink.tc3_global_escape tc3_mink_temporal
    (xs := fun _ => 0) (ys := fun n => (((n:ℝ) + 1), 0)) (p := 0) (fun _ => mem_univ _)
    tc3_mink_cau tendsto_const_nhds (mem_univ _) (by
      simp only [Prod.fst_zero, sub_zero]
      exact tendsto_natCast_atTop_atTop.atTop_add tendsto_const_nhds)
  refine ⟨γ, Ts, hγ0, hTs, fun j => (hj j).1, ?_⟩
  rcases hd with h | ⟨Tst, h1, -, h2⟩
  · exact Or.inl h
  · exact Or.inr ⟨Tst, h1, h2⟩

end Witness
end TC3

section KitB
variable {V : Type*} [NormedAddCommGroup V] [NormedSpace ℝ V]

namespace Spacetime
variable (S : Spacetime V)


/-- Positive rescaling preserves future-timelikeness. -/
lemma futTimelike_smul {x u : V} {c : ℝ} (hc : 0 < c) (h : S.FutTimelike x u) :
    S.FutTimelike x (c • u) := by
  obtain ⟨h1, h2⟩ := h
  refine ⟨?_, ?_⟩
  · simp only [map_smul, FunLike.coe_smul, Pi.smul_apply, smul_eq_mul]
    nlinarith [mul_pos hc hc]
  · simp only [map_smul, FunLike.coe_smul, Pi.smul_apply, smul_eq_mul]
    nlinarith

end Spacetime

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


end KitB

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

end MSpacetime

/-! ## Row T7: on `N` under `OneChart` -/

namespace MSpacetime
variable {S : MSpacetime E N} {p₀ : N}

lemma tc3_cau_mem {x y : N} (hx : x ∈ S.M) (h : S.Cau x y) : y ∈ S.M := by
  induction h with
  | refl => exact hx
  | tail _ hst _ => exact (S.cstep_mem hst).2

/-- **A temporal function on `M` is temporal in the chart** (the first half of the kit's
`ch_isCauchy_NV`, with `M` in place of `D J`). -/
theorem tc3_temporal_NV (hC : S.OneChart p₀) {Θ : N → ℝ} (hΘ : S.IsTemporalOn S.M Θ) :
    (chartSp hC).IsTemporal (Θ ∘ (extChartAt 𝓘(ℝ, E) p₀).symm) := by
  have hD : ∀ u ∈ (chartSp hC).M,
      u ∈ (extChartAt 𝓘(ℝ, E) p₀).target ∧ (extChartAt 𝓘(ℝ, E) p₀).symm u ∈ S.M := by
    rintro _ ⟨x, hx, rfl⟩
    exact ⟨ch_mem_target p₀ (hC.sub hx), by rw [ch_left_inv p₀ (hC.sub hx)]; exact hx⟩
  have hΘd : ∀ u ∈ (chartSp hC).M,
      ContMDiffAt 𝓘(ℝ, E) 𝓘(ℝ, ℝ) 1 (Θ ∘ (extChartAt 𝓘(ℝ, E) p₀).symm) u := fun u hu =>
    (hΘ.1.contMDiffAt (S.isOpen_M.mem_nhds (hD u hu).2)).comp u
      ((contMDiffOn_extChartAt_symm p₀).contMDiffAt
        ((isOpen_extChartAt_target p₀).mem_nhds (hD u hu).1))
  refine ⟨fun u hu => (contMDiffAt_iff_contDiffAt.1 (hΘd u hu)).contDiffWithinAt,
    fun u hu w hw => ?_⟩
  obtain ⟨hut, hxD⟩ := hD u hu
  have h1 := (hΘ.1.contMDiffAt (S.isOpen_M.mem_nhds hxD)).mdifferentiableAt one_ne_zero
  have h2 := ld_mdifferentiableAt_symm p₀ hut
  have e : fderiv ℝ (Θ ∘ (extChartAt 𝓘(ℝ, E) p₀).symm) u w =
      dfun Θ ((extChartAt 𝓘(ℝ, E) p₀).symm u) (dchartInv p₀ u w) := by
    have e1 : mfderiv 𝓘(ℝ, E) 𝓘(ℝ, ℝ) (Θ ∘ (extChartAt 𝓘(ℝ, E) p₀).symm) u w =
        fderiv ℝ (Θ ∘ (extChartAt 𝓘(ℝ, E) p₀).symm) u w := by rw [mfderiv_eq_fderiv]; rfl
    rw [← e1, mfderiv_comp u h1 h2]; rfl
  rw [e]
  exact hΘ.2 _ hxD _ ((futCausal_chart' hC hut w).1 hw)

/-- **Row T7.** Under `OneChart p₀` and a temporal `Θ` on `M`: chains of `N` from `xₙ ∈ M`,
`xₙ → p ∈ M`, with `Θ`-rise `→ ∞`, give a curve `c` in `M` from `p`, continuous and
`Θ`-parametrised (`Θ (c s) = Θ p + s`) on every `[0, Tⱼ]` (`Tⱼ` strictly increasing from `0`), the
pointwise limit in `N` of pulled-back chain parametrisations, which eventually leaves every compact
`K ⊆ M`: as `t → ∞` if `Tⱼ → ∞`, as `t → T*⁻` if `Tⱼ → T* < ∞`. -/
theorem tc3_manifold_escape [FiniteDimensional ℝ E] (hC : S.OneChart p₀) {Θ : N → ℝ}
    (hΘ : S.IsTemporalOn S.M Θ) {xs ys : ℕ → N} {p : N} (hxM : ∀ n, xs n ∈ S.M)
    (hcau : ∀ n, S.Cau (xs n) (ys n)) (hp : Tendsto xs atTop (𝓝 p)) (hpM : p ∈ S.M)
    (hL : Tendsto (fun n => Θ (ys n) - Θ (xs n)) atTop atTop) :
    ∃ (ηs : ℕ → ℝ → E) (ψ : ℕ → ℕ) (c : ℝ → N) (Ts : ℕ → ℝ), StrictMono ψ ∧
      (∀ n, ηs n 0 = extChartAt 𝓘(ℝ, E) p₀ (xs n)) ∧ c 0 = p ∧ StrictMono Ts ∧ Ts 0 = 0 ∧
      (∀ j, ContinuousOn c (Icc 0 (Ts j)) ∧ ∀ s ∈ Icc 0 (Ts j), c s ∈ S.M ∧ Θ (c s) = Θ p + s ∧
        Tendsto (fun n => (extChartAt 𝓘(ℝ, E) p₀).symm (ηs (ψ n) s)) atTop (𝓝 (c s))) ∧
      ((Tendsto Ts atTop atTop ∧ ∀ K : Set N, IsCompact K → K ⊆ S.M → ∀ᶠ t in atTop, c t ∉ K) ∨
        ∃ Tst : ℝ, Tendsto Ts atTop (𝓝 Tst) ∧
          ∀ K : Set N, IsCompact K → K ⊆ S.M → ∀ᶠ t in 𝓝[<] Tst, c t ∉ K) := by
  set φ := extChartAt 𝓘(ℝ, E) p₀ with hφ
  set Θ' : E → ℝ := Θ ∘ φ.symm with hΘ'
  have hT := tc3_temporal_NV hC hΘ
  have hMs : ∀ x ∈ S.M, x ∈ (chartAt E p₀).source := fun x hx => hC.sub hx
  have hΘφ : ∀ x ∈ S.M, Θ' (φ x) = Θ x := fun x hx => by
    simp only [hΘ', Function.comp]; rw [ch_left_inv p₀ (hMs x hx)]
  have hpull : ∀ y ∈ (chartSp hC).M, φ.symm y ∈ S.M ∧ φ (φ.symm y) = y := by
    rintro y ⟨z, hz, rfl⟩
    rw [ch_left_inv p₀ (hMs z hz)]; exact ⟨hz, rfl⟩
  have htgt : ∀ y ∈ (chartSp hC).M, y ∈ φ.target := by
    rintro y ⟨z, hz, rfl⟩; exact ch_mem_target p₀ (hMs z hz)
  have hsymmAt : ∀ y ∈ (chartSp hC).M, ContinuousAt φ.symm y := fun y hy =>
    (continuousOn_extChartAt_symm p₀).continuousAt
      ((isOpen_extChartAt_target p₀).mem_nhds (htgt y hy))
  have hyM : ∀ n, ys n ∈ S.M := fun n => tc3_cau_mem (hxM n) (hcau n)
  have hcau' : ∀ n, (chartSp hC).Cau (φ (xs n)) (φ (ys n)) := fun n =>
    Relation.ReflTransGen.lift _ (fun a b hab => ch_cstep_NV hC hab) _ _ (hcau n)
  have hL' : Tendsto (fun n => Θ' (φ (ys n)) - Θ' (φ (xs n))) atTop atTop := by
    refine hL.congr fun n => ?_
    rw [hΘφ _ (hyM n), hΘφ _ (hxM n)]
  have hp' : Tendsto (fun n => φ (xs n)) atTop (𝓝 (φ p)) :=
    (ch_contAt p₀ (hMs p hpM)).tendsto.comp hp
  obtain ⟨ηs, ψ, γ, Ts, h1, hψ, hTs, hTs0, hγ0, hj, hd⟩ :=
    (chartSp hC).tc3_global_escape hT (fun n => ⟨xs n, hxM n, rfl⟩) hcau' hp' ⟨p, hpM, rfl⟩ hL'
  have hγM : ∀ j, ∀ s ∈ Icc 0 (Ts j), γ s ∈ (chartSp hC).M := fun j s hs => (hj j).1.2.2.1 s hs
  have hcp : φ.symm (γ 0) = p := by rw [hγ0]; exact ch_left_inv p₀ (hMs p hpM)
  refine ⟨ηs, ψ, fun s => φ.symm (γ s), Ts, hψ, fun n => (h1 n).1, hcp, hTs, hTs0,
    fun j => ⟨fun s hs => ((hsymmAt _ (hγM j s hs)).comp_continuousWithinAt ((hj j).1.1 s hs)),
      fun s hs => ⟨(hpull _ (hγM j s hs)).1, ?_, (hsymmAt _ (hγM j s hs)).tendsto.comp
        ((hj j).2.tendsto_at hs)⟩⟩, ?_⟩
  · have := (hj j).1.2.1 s hs
    simp only [Function.comp] at this
    rw [this, hcp]; ring
  -- escape, pulled back
  have hpullK : ∀ K : Set N, IsCompact K → K ⊆ S.M →
      ∃ K' : Set E, IsCompact K' ∧ K' ⊆ (chartSp hC).M ∧
        ∀ y ∈ (chartSp hC).M, φ.symm y ∈ K → y ∈ K' := fun K hK hKM =>
    ⟨φ '' K, hK.image_of_continuousOn ((continuousOn_extChartAt p₀).mono fun x hx => by
        rw [extChartAt_source]; exact hMs x (hKM hx)),
      image_mono hKM, fun y hy hyK => ⟨_, hyK, (hpull y hy).2⟩⟩
  have hex : ∀ t ≥ (0:ℝ), (∃ j, t ≤ Ts j) → γ t ∈ (chartSp hC).M := fun t ht ⟨j, hj'⟩ =>
    hγM j t ⟨ht, hj'⟩
  rcases hd with ⟨hinf, hesc⟩ | ⟨Tst, hlim, hlt, hesc⟩
  · refine Or.inl ⟨hinf, fun K hK hKM => ?_⟩
    obtain ⟨K', hK'c, hK'M, hK'⟩ := hpullK K hK hKM
    filter_upwards [hesc K' hK'c hK'M, eventually_ge_atTop (0:ℝ)] with t ht ht0 hcK
    have hm := hex t ht0 ((hinf.eventually (eventually_ge_atTop t)).exists)
    exact ht (hK' _ hm hcK)
  · refine Or.inr ⟨Tst, hlim, fun K hK hKM => ?_⟩
    obtain ⟨K', hK'c, hK'M, hK'⟩ := hpullK K hK hKM
    have hT0 : 0 < Tst := hTs0 ▸ hlt 0
    filter_upwards [hesc K' hK'c hK'M, Ioo_mem_nhdsLT hT0] with t ht ht0 hcK
    have hm := hex t ht0.1.le ((hlim.eventually (lt_mem_nhds ht0.2)).exists.imp fun j h => h.le)
    exact ht (hK' _ hm hcK)

end MSpacetime

end Manifold

end ShadowProbe.TemporalCurvesProbe

#print axioms ShadowProbe.TemporalCurvesProbe.Spacetime.tc3_cone
#print axioms ShadowProbe.TemporalCurvesProbe.Spacetime.tc3_cau_bound
#print axioms ShadowProbe.TemporalCurvesProbe.Spacetime.tc3_chain
#print axioms ShadowProbe.TemporalCurvesProbe.Spacetime.tc3_chain_causal
#print axioms ShadowProbe.TemporalCurvesProbe.Spacetime.tc3_local_limit
#print axioms ShadowProbe.TemporalCurvesProbe.Spacetime.tc3_causal_limit
#print axioms ShadowProbe.TemporalCurvesProbe.Spacetime.tc3_nonimprison_top
#print axioms ShadowProbe.TemporalCurvesProbe.Spacetime.tc3_nonimprison
#print axioms ShadowProbe.TemporalCurvesProbe.Spacetime.tc3_global_limit
#print axioms ShadowProbe.TemporalCurvesProbe.Spacetime.tc3_global_escape
#print axioms ShadowProbe.TemporalCurvesProbe.MSpacetime.tc3_manifold_escape
#print axioms ShadowProbe.TemporalCurvesProbe.tc3_witness

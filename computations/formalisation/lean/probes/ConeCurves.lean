import Mathlib

/-!
# P1's 6b-ii, phase 2: the kit's causal arcs are locally cone curves; the limit-curve theorem for chains

Registration: `computations/formalisation/r7809_71_6bii_p2/PREDICTION.md`; plan `../r7807_71_6bii/PLAN.md`.
Mathlib only; nothing imports this file. Verbatim copies, unchanged: `probes/LimitCurve.lean` l.16–140 (phase 1,
rows L1–L3); `probes/GeneratorStretch.lean` l.499–534 and l.1020–1030 (the chart `Spacetime`, `restrict`),
l.627–636 (`futTimelike_smul`), l.2363–2448 (campaign 84's `V`-side helpers and the squash), l.2777–3278 (the
manifold kit through `ch_cau_iff`) and l.3543–3554 (`restrictM`). Everything new has the prefix `kc_`.

At `x₀ ∈ M` of a chart spacetime, `τ₀ v = −g_{x₀}(v, T x₀)` and `K(c) = {v : c‖v‖ ≤ τ₀ v}`.

* **K1 — BUILT.** `kc_cone`: near `x₀`, every future-causal vector lies in one constant cone `K(c)`.
* **K2 — BUILT.** `kc_KCurve_of_deriv`, `kc_cstep_arc`, `kc_cau_K`: arcs and chains are `K(c)`-curves.
* **K3 — BUILT.** `kc_reparam`, `kc_concat`, `kc_chain`: chains are `τ₀`-parametrised `K(c)`-curves.
* **K4 — BUILT.** `kc_local_limit`: the local limit-curve theorem for causal chains in a chart.
* **K5 — BUILT.** `kc_manifold_limit`: the same on `N` under `OneChart p₀`, with the limit pulled back to a
  continuous curve in `M` from `p`.
* **K6 — NOT BUILT (the registered stop).** The global limit-curve theorem on `N`, patching charts.
* **K7 — BUILT.** `kc_witness`: the 2D Minkowski chart with the arcs `(t r/2, r sin(m t)/(4m))`.
-/

open Set Filter Topology BoundedContinuousFunction Metric

namespace ShadowProbe.ConeCurvesProbe

section Phase1
variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]

/-- A `K`-curve on `[a, b]`: `γ t − γ s ∈ K` whenever `a ≤ s ≤ t ≤ b`. -/
def lc_KCurve (K : Set E) (a b : ℝ) (γ : ℝ → E) : Prop :=
  ∀ s t, a ≤ s → s ≤ t → t ≤ b → γ t - γ s ∈ K

/-- `γ` is `τ`-parametrised on `[a, b]`: `τ(γ s) = τ(γ a) + (s − a)`. -/
def lc_Param (τ : E →L[ℝ] ℝ) (a b : ℝ) (γ : ℝ → E) : Prop :=
  ∀ s ∈ Icc a b, τ (γ s) = τ (γ a) + (s - a)

/-! ## Row L1: the Lipschitz bound -/

/-- **Row L1.** Along a `K`-curve, `‖γ t − γ s‖ ≤ (τ(γ t) − τ(γ s))/c` for `s ≤ t`. -/
theorem lc_lipschitz_bound {K : Set E} {τ : E →L[ℝ] ℝ} {c a b : ℝ} (hc : 0 < c)
    (hK : ∀ v ∈ K, c * ‖v‖ ≤ τ v) {γ : ℝ → E} (hγ : lc_KCurve K a b γ) {s t : ℝ}
    (hs : a ≤ s) (hst : s ≤ t) (ht : t ≤ b) :
    ‖γ t - γ s‖ ≤ (τ (γ t) - τ (γ s)) / c := by
  rw [le_div_iff₀ hc, mul_comm, ← map_sub]
  exact hK _ (hγ s t hs hst ht)

/-- **Row L1.** A `τ`-parametrised `K`-curve is `1/c`-Lipschitz on `[a, b]`. -/
theorem lc_param_lipschitz {K : Set E} {τ : E →L[ℝ] ℝ} {c a b : ℝ} (hc : 0 < c)
    (hK : ∀ v ∈ K, c * ‖v‖ ≤ τ v) {γ : ℝ → E} (hγ : lc_KCurve K a b γ) (hp : lc_Param τ a b γ)
    {s t : ℝ} (hs : s ∈ Icc a b) (ht : t ∈ Icc a b) : ‖γ t - γ s‖ ≤ |t - s| / c := by
  rcases le_total s t with h | h
  · have := lc_lipschitz_bound hc hK hγ hs.1 h ht.2
    rw [hp t ht, hp s hs] at this
    rw [abs_of_nonneg (by linarith)]
    calc ‖γ t - γ s‖ ≤ _ := this
      _ = (t - s) / c := by ring
  · have := lc_lipschitz_bound hc hK hγ ht.1 h hs.2
    rw [hp t ht, hp s hs] at this
    rw [norm_sub_rev, abs_of_nonpos (by linarith)]
    calc ‖γ s - γ t‖ ≤ _ := this
      _ = -(t - s) / c := by ring

/-! ## Row L2: closedness under pointwise limits -/

/-- **Row L2.** A pointwise limit on `[a, b]` of `K`-curves is a `K`-curve (`K` closed), and of `τ`-parametrised curves
is `τ`-parametrised. -/
theorem lc_limit_closed {K : Set E} (hKc : IsClosed K) {τ : E →L[ℝ] ℝ} {a b : ℝ} {γs : ℕ → ℝ → E} {γ : ℝ → E}
    (hlim : ∀ s ∈ Icc a b, Tendsto (fun n => γs n s) atTop (𝓝 (γ s))) :
    ((∀ n, lc_KCurve K a b (γs n)) → lc_KCurve K a b γ) ∧
      ((∀ n, lc_Param τ a b (γs n)) → a ≤ b → lc_Param τ a b γ) := by
  constructor
  · intro hK s t hs hst ht
    have h1 := hlim t ⟨hs.trans hst, ht⟩
    have h2 := hlim s ⟨hs, hst.trans ht⟩
    exact hKc.mem_of_tendsto (h1.sub h2) (Eventually.of_forall fun n => hK n s t hs hst ht)
  · intro hP hab s hs
    have ha := (τ.continuous.tendsto _).comp (hlim a ⟨le_refl a, hab⟩)
    have hs' := (τ.continuous.tendsto _).comp (hlim s hs)
    have e : (fun n => τ (γs n s)) = fun n => τ (γs n a) + (s - a) := funext fun n => hP n s hs
    rw [Function.comp_def, e] at hs'
    exact tendsto_nhds_unique hs' ((ha.add_const (s - a)))

/-! ## Row L3: the local limit-curve theorem -/

/-- **Row L3.** In finite dimension: any sequence of `τ`-parametrised `K`-curves on `[a, b]` whose starting points
converge to `p` has a subsequence converging uniformly on `[a, b]` to a `τ`-parametrised `K`-curve starting at `p`. The
proof is Arzelà–Ascoli: the curves are uniformly `1/c`-Lipschitz (L1), their values lie in one closed ball (compact in
finite dimension), and the limit keeps the cone condition (L2). -/
theorem lc_limit_curve [FiniteDimensional ℝ E] {K : Set E} (hKc : IsClosed K) {τ : E →L[ℝ] ℝ} {c a b : ℝ}
    (hc : 0 < c) (hab : a ≤ b) (hK : ∀ v ∈ K, c * ‖v‖ ≤ τ v) {γs : ℕ → ℝ → E}
    (hγK : ∀ n, lc_KCurve K a b (γs n)) (hγP : ∀ n, lc_Param τ a b (γs n)) {p : E}
    (hp : Tendsto (fun n => γs n a) atTop (𝓝 p)) :
    ∃ (φ : ℕ → ℕ) (γ : ℝ → E), StrictMono φ ∧ TendstoUniformlyOn (fun n => γs (φ n)) γ atTop (Icc a b) ∧
      lc_KCurve K a b γ ∧ lc_Param τ a b γ ∧ γ a = p := by
  have : ProperSpace E := FiniteDimensional.proper_real E
  -- the uniform Lipschitz bound on `[a, b]`
  have hL : ∀ n (x y : Icc a b), dist (γs n x) (γs n y) ≤ 1 / c * dist x y := by
    intro n x y
    rw [dist_eq_norm, Subtype.dist_eq, Real.dist_eq, one_div_mul_eq_div]
    exact lc_param_lipschitz hc hK (hγK n) (hγP n) y.2 x.2
  have hcont : ∀ n, Continuous (fun x : Icc a b => γs n x) := by
    intro n
    refine Metric.continuous_iff.2 fun x ε hε => ⟨ε * c, by positivity, fun y hy => ?_⟩
    calc dist (γs n y) (γs n x) ≤ 1 / c * dist y x := hL n y x
      _ < 1 / c * (ε * c) := by gcongr
      _ = ε := by field_simp
  let f : ℕ → (Icc a b →ᵇ E) := fun n => BoundedContinuousFunction.mkOfCompact ⟨_, hcont n⟩
  have hf : ∀ n x, f n x = γs n x := fun n x => rfl
  -- all values lie in one closed ball about `p`
  obtain ⟨r, hr⟩ := (Metric.isBounded_range_of_tendsto _ hp).subset_closedBall p
  have hball : ∀ n x, f n x ∈ Metric.closedBall p (r + (b - a) / c) := by
    intro n x
    have h1 : dist (γs n a) p ≤ r := hr ⟨n, rfl⟩
    have h2 := hL n x ⟨a, le_refl a, hab⟩
    have h3 : dist x (⟨a, le_refl a, hab⟩ : Icc a b) ≤ b - a := by
      rw [Subtype.dist_eq, Real.dist_eq, abs_of_nonneg (by linarith [x.2.1])]; linarith [x.2.2]
    rw [Metric.mem_closedBall, hf]
    calc dist (γs n x) p ≤ dist (γs n x) (γs n a) + dist (γs n a) p := dist_triangle _ _ _
      _ ≤ 1 / c * (b - a) + r := by
          gcongr
          · exact h2.trans (by gcongr)
      _ = r + (b - a) / c := by ring
  -- equicontinuity of the family
  have hEq : Equicontinuous ((↑) : Set.range f → Icc a b → E) := by
    intro x₀
    refine Metric.equicontinuousAt_iff.2 fun ε hε => ⟨ε * c, by positivity, fun x hx i => ?_⟩
    obtain ⟨n, hn⟩ := i.2
    rw [← hn]
    calc dist (f n x₀) (f n x) ≤ 1 / c * dist x₀ x := hL n x₀ x
      _ < 1 / c * (ε * c) := by rw [dist_comm]; gcongr
      _ = ε := by field_simp
  have hA := BoundedContinuousFunction.arzela_ascoli (Metric.closedBall p (r + (b - a) / c))
    (isCompact_closedBall _ _) (Set.range f) (by rintro g x ⟨n, rfl⟩; exact hball n x) hEq
  obtain ⟨F, -, φ, hφ, hFlim⟩ := hA.tendsto_subseq (fun n => subset_closure ⟨n, rfl⟩)
  set γ : ℝ → E := fun s => F (projIcc a b hab s)
  have hγF : ∀ s (hs : s ∈ Icc a b), γ s = F ⟨s, hs⟩ := fun s hs => by simp [γ, projIcc_of_mem hab hs]
  have hunif : TendstoUniformlyOn (fun n => γs (φ n)) γ atTop (Icc a b) := by
    rw [Metric.tendstoUniformlyOn_iff]
    intro ε hε
    have := (Metric.tendsto_nhds.1 hFlim) ε hε
    filter_upwards [this] with n hn
    intro s hs
    rw [hγF s hs, dist_comm]
    calc dist (γs (φ n) s) (F ⟨s, hs⟩) = dist (f (φ n) ⟨s, hs⟩) (F ⟨s, hs⟩) := rfl
      _ ≤ dist (f (φ n)) F := BoundedContinuousFunction.dist_coe_le_dist _
      _ < ε := hn
  have hpt : ∀ s ∈ Icc a b, Tendsto (fun n => γs (φ n) s) atTop (𝓝 (γ s)) :=
    fun s hs => hunif.tendsto_at hs
  obtain ⟨hK2, hP2⟩ := lc_limit_closed (τ := τ) hKc hpt
  refine ⟨φ, γ, hφ, hunif, hK2 fun n => hγK (φ n), hP2 (fun n => hγP (φ n)) hab, ?_⟩
  exact tendsto_nhds_unique (hpt a ⟨le_refl a, hab⟩) (hp.comp hφ.tendsto_atTop)

end Phase1

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

section KC
variable {V : Type*} [NormedAddCommGroup V] [NormedSpace ℝ V]

namespace Spacetime
variable (S : Spacetime V)

/-- `τ₀ v = −g_{x₀}(v, T x₀)`. -/
noncomputable def kc_τ (x₀ : V) : V →L[ℝ] ℝ := -((S.g x₀).flip (S.T x₀))

lemma kc_τ_apply (x₀ v : V) : S.kc_τ x₀ v = -S.g x₀ v (S.T x₀) := rfl

/-- The constant cone `K(c) = {v : c‖v‖ ≤ τ₀ v}`. -/
def kc_K (x₀ : V) (c : ℝ) : Set V := {v | c * ‖v‖ ≤ S.kc_τ x₀ v}

lemma kc_futCausal_smul {x u : V} {c : ℝ} (hc : 0 < c) (h : S.FutCausal x u) :
    S.FutCausal x (c • u) := by
  obtain ⟨h1, h2⟩ := h
  refine ⟨?_, ?_⟩
  · simp only [map_smul, FunLike.coe_smul, Pi.smul_apply, smul_eq_mul]
    nlinarith [mul_pos hc hc]
  · simp only [map_smul, FunLike.coe_smul, Pi.smul_apply, smul_eq_mul]
    nlinarith

lemma kc_futCausal_ne {x u : V} (h : S.FutCausal x u) : u ≠ 0 := by
  rintro rfl; simp [FutCausal] at h

omit [NormedSpace ℝ V] in
lemma kc_tendsto_clm {ι F G : Type*} [NormedAddCommGroup F] [NormedSpace ℝ F] [NormedAddCommGroup G]
    [NormedSpace ℝ G] {l : Filter ι} {f : ι → F →L[ℝ] G} {A : F →L[ℝ] G} {u : ι → F} {a : F}
    (hf : Tendsto f l (𝓝 A)) (hu : Tendsto u l (𝓝 a)) : Tendsto (fun i => f i (u i)) l (𝓝 (A a)) :=
  ((continuous_fst.clm_apply continuous_snd).tendsto (A, a)).comp (hf.prodMk_nhds hu)

/-- **Row K1: the cone lemma.** -/
theorem kc_cone [FiniteDimensional ℝ V] {x₀ : V} (hx₀ : x₀ ∈ S.M) :
    ∃ r > 0, ∃ c > 0, ball x₀ r ⊆ S.M ∧
      ∀ x ∈ ball x₀ r, ∀ v, S.FutCausal x v → v ∈ S.kc_K x₀ c := by
  obtain ⟨r₀, hr₀, hr₀M⟩ := Metric.isOpen_iff.1 S.isOpen_M x₀ hx₀
  by_contra hcon
  push Not at hcon
  have key : ∀ n : ℕ, ∃ x ∈ ball x₀ (min r₀ (1 / (n + 1))), ∃ v, S.FutCausal x v ∧ ‖v‖ = 1 ∧
      S.kc_τ x₀ v < 1 / (n + 1) := by
    intro n
    have hr : 0 < min r₀ (1 / ((n:ℝ) + 1)) := lt_min hr₀ (by positivity)
    obtain ⟨x, hx, v, hv, hvK⟩ := hcon _ hr (1 / ((n:ℝ) + 1)) (by positivity)
      ((ball_subset_ball (min_le_left _ _)).trans hr₀M)
    have hv0 : 0 < ‖v‖ := norm_pos_iff.2 (S.kc_futCausal_ne hv)
    refine ⟨x, hx, ‖v‖⁻¹ • v, S.kc_futCausal_smul (inv_pos.2 hv0) hv, ?_, ?_⟩
    · rw [norm_smul, norm_inv, norm_norm, inv_mul_cancel₀ hv0.ne']
    · simp only [kc_K, mem_ofPred_eq, not_le] at hvK
      rw [map_smul, smul_eq_mul]
      calc ‖v‖⁻¹ * S.kc_τ x₀ v < ‖v‖⁻¹ * (1 / ((n:ℝ) + 1) * ‖v‖) :=
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
    calc dist (xs n) x₀ < min r₀ (1 / ((n:ℝ) + 1)) := h1
      _ ≤ 1 / ((n:ℝ) + 1) := min_le_right _ _
      _ ≤ 1 / ((N:ℝ) + 1) := by gcongr
      _ < ε := hN
  have hxφ := hx.comp hφ.tendsto_atTop
  have hgc : ContinuousAt S.g x₀ := S.cont_g.continuousAt (S.isOpen_M.mem_nhds hx₀)
  have hTc : ContinuousAt S.T x₀ := S.cont_T.continuousAt (S.isOpen_M.mem_nhds hx₀)
  have hg : Tendsto (fun n => S.g (xs (φ n))) atTop (𝓝 (S.g x₀)) := hgc.tendsto.comp hxφ
  have hT : Tendsto (fun n => S.T (xs (φ n))) atTop (𝓝 (S.T x₀)) := hTc.tendsto.comp hxφ
  have h1 : Tendsto (fun n => S.g (xs (φ n)) (vs (φ n)) (vs (φ n))) atTop (𝓝 (S.g x₀ u u)) :=
    kc_tendsto_clm (kc_tendsto_clm hg hlim) hlim
  have h2 : Tendsto (fun n => S.g (xs (φ n)) (vs (φ n)) (S.T (xs (φ n)))) atTop
      (𝓝 (S.g x₀ u (S.T x₀))) := kc_tendsto_clm (kc_tendsto_clm hg hlim) hT
  have h3 : Tendsto (fun n => S.kc_τ x₀ (vs (φ n))) atTop (𝓝 (S.kc_τ x₀ u)) :=
    ((S.kc_τ x₀).continuous.tendsto u).comp hlim
  have hA : S.g x₀ u u ≤ 0 := le_of_tendsto' h1 fun n => (hvs (φ n)).1
  have hB : S.g x₀ u (S.T x₀) ≤ 0 := le_of_tendsto' h2 fun n => (hvs (φ n)).2.le
  have hC : S.kc_τ x₀ u ≤ 0 := by
    have h4 : Tendsto (fun n : ℕ => 1 / ((φ n : ℝ) + 1)) atTop (𝓝 0) :=
      tendsto_one_div_add_atTop_nhds_zero_nat.comp hφ.tendsto_atTop
    exact le_of_tendsto_of_tendsto' h3 h4 fun n => (hvτ (φ n)).le
  rw [kc_τ_apply] at hC
  have h0 : S.g x₀ u (S.T x₀) = 0 := le_antisymm hB (by linarith)
  have hpos := S.pos_on_perp x₀ hx₀ u h0 (by rintro rfl; simp at hu1)
  linarith

/-! ## Row K2: arcs and chains are cone curves -/

/-- A `C¹` arc with velocity in `{c‖v‖ ≤ τ v}` on `[a, b]` is a cone curve there. -/
theorem kc_KCurve_of_deriv {τ : V →L[ℝ] ℝ} {c a b : ℝ} (hc : 0 < c) {γ : ℝ → V}
    (hγ : ContDiff ℝ 1 γ) (hd : ∀ t ∈ Icc a b, c * ‖deriv γ t‖ ≤ τ (deriv γ t)) :
    lc_KCurve {v | c * ‖v‖ ≤ τ v} a b γ := by
  intro s t hs hst ht
  have hdiff : Differentiable ℝ γ := hγ.differentiable one_ne_zero
  have hf : ∀ u, HasDerivAt (fun u => γ u - γ s) (deriv γ u) u :=
    fun u => (hdiff u).hasDerivAt.sub_const _
  have hB : ∀ u, HasDerivAt (fun u => (τ (γ u) - τ (γ s)) / c) (τ (deriv γ u) / c) u :=
    fun u => ((τ.hasFDerivAt.comp_hasDerivAt u (hdiff u).hasDerivAt).sub_const _).div_const c
  have key := image_norm_le_of_norm_deriv_right_le_deriv_boundary (a := s) (b := t)
    (f := fun u => γ u - γ s) (f' := deriv γ)
    ((hγ.continuous.sub continuous_const).continuousOn) (fun u _ => (hf u).hasDerivWithinAt)
    (B := fun u => (τ (γ u) - τ (γ s)) / c) (B' := fun u => τ (deriv γ u) / c)
    (by simp) hB
    (fun u hu => by
      rw [le_div_iff₀ hc, mul_comm]
      exact hd u ⟨hs.trans hu.1, hu.2.le.trans ht⟩)
    ⟨hst, le_rfl⟩
  show c * ‖γ t - γ s‖ ≤ τ (γ t - γ s)
  rw [map_sub, mul_comm, ← le_div_iff₀ hc]
  exact key

lemma kc_K_zero (x₀ : V) (c : ℝ) : (0 : V) ∈ S.kc_K x₀ c := by simp [kc_K]

lemma kc_K_add {x₀ : V} {c : ℝ} (hc : 0 ≤ c) {u v : V} (hu : u ∈ S.kc_K x₀ c)
    (hv : v ∈ S.kc_K x₀ c) : u + v ∈ S.kc_K x₀ c := by
  simp only [kc_K, mem_ofPred_eq, map_add] at *
  nlinarith [norm_add_le u v]

lemma kc_K_closed (x₀ : V) (c : ℝ) : IsClosed (S.kc_K x₀ c) :=
  isClosed_le (continuous_const.mul continuous_norm) (S.kc_τ x₀).continuous

variable {S}

/-- **Row K2 (arcs).** Every arc of a step of the chart restricted to a set where the cone lemma
holds is a `K(c)`-curve on `[0, 1]`, with nonzero velocity. -/
theorem kc_cstep_arc {x₀ : V} {c : ℝ} (hc : 0 < c) {B : Set V} (hB : IsOpen B) (hBM : B ⊆ S.M)
    (hcone : ∀ x ∈ B, ∀ v, S.FutCausal x v → v ∈ S.kc_K x₀ c) {x y : V}
    (h : (S.restrict B hB hBM).CStep x y) :
    ∃ γ : ℝ → V, ContDiff ℝ 1 γ ∧ γ 0 = x ∧ γ 1 = y ∧
      (∀ t ∈ Icc (0:ℝ) 1, γ t ∈ B ∧ deriv γ t ≠ 0 ∧ deriv γ t ∈ S.kc_K x₀ c) ∧
      lc_KCurve (S.kc_K x₀ c) 0 1 γ := by
  obtain ⟨γ, hγ, h0, h1, ht⟩ := h
  have hd : ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ B ∧ deriv γ t ≠ 0 ∧ deriv γ t ∈ S.kc_K x₀ c := fun t htI =>
    ⟨(ht t htI).1, S.kc_futCausal_ne (ht t htI).2, hcone _ (ht t htI).1 _ (ht t htI).2⟩
  exact ⟨γ, hγ, h0, h1, hd, kc_KCurve_of_deriv hc hγ fun t htI => (hd t htI).2.2⟩

/-- **Row K2 (chains).** A chain of the restricted chart has its displacement in `K(c)`. -/
theorem kc_cau_K {x₀ : V} {c : ℝ} (hc : 0 < c) {B : Set V} (hB : IsOpen B) (hBM : B ⊆ S.M)
    (hcone : ∀ x ∈ B, ∀ v, S.FutCausal x v → v ∈ S.kc_K x₀ c) {x y : V}
    (h : (S.restrict B hB hBM).Cau x y) : y - x ∈ S.kc_K x₀ c := by
  induction h with
  | refl => simpa using S.kc_K_zero x₀ c
  | tail _ hst ih =>
    obtain ⟨γ, -, h0, h1, -, hK⟩ := kc_cstep_arc hc hB hBM hcone hst
    have := hK 0 1 le_rfl zero_le_one le_rfl
    rw [h0, h1] at this
    have e := S.kc_K_add hc.le this ih
    rwa [sub_add_sub_cancel] at e

/-! ## Row K3: `τ₀`-parametrisation of chains -/

/-- One arc, reparametrised by the inverse of `τ ∘ γ`. -/
theorem kc_reparam {τ : V →L[ℝ] ℝ} {c : ℝ} (hc : 0 < c) {γ : ℝ → V} (hγ : ContDiff ℝ 1 γ)
    (hd : ∀ t ∈ Icc (0:ℝ) 1, deriv γ t ≠ 0 ∧ c * ‖deriv γ t‖ ≤ τ (deriv γ t)) :
    ∃ η : ℝ → V, lc_KCurve {v | c * ‖v‖ ≤ τ v} (τ (γ 0)) (τ (γ 1)) η ∧
      lc_Param τ (τ (γ 0)) (τ (γ 1)) η ∧ η (τ (γ 0)) = γ 0 ∧ η (τ (γ 1)) = γ 1 ∧
      τ (γ 0) < τ (γ 1) ∧ ∀ σ ∈ Icc (τ (γ 0)) (τ (γ 1)), ∃ u ∈ Icc (0:ℝ) 1, η σ = γ u := by
  set f : ℝ → ℝ := fun u => τ (γ u) with hfdef
  have hdiff : Differentiable ℝ γ := hγ.differentiable one_ne_zero
  have hfd : ∀ u, HasDerivAt f (τ (deriv γ u)) u :=
    fun u => τ.hasFDerivAt.comp_hasDerivAt u (hdiff u).hasDerivAt
  have hfc : ContinuousOn f (Icc 0 1) := (τ.continuous.comp hγ.continuous).continuousOn
  have hmono : StrictMonoOn f (Icc 0 1) := by
    refine strictMonoOn_of_deriv_pos (convex_Icc 0 1) hfc fun u hu => ?_
    rw [interior_Icc] at hu
    rw [(hfd u).deriv]
    have h := hd u (Ioo_subset_Icc_self hu)
    have : 0 < ‖deriv γ u‖ := norm_pos_iff.2 h.1
    nlinarith [h.2]
  have hKγ := kc_KCurve_of_deriv hc hγ fun t ht => (hd t ht).2
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
  refine ⟨fun σ => γ (θ σ), ?_, ?_, by show γ (θ (f 0)) = γ 0; rw [hθ0], by show γ (θ (f 1)) = γ 1; rw [hθ1], h01,
    fun σ hσ => ⟨θ σ, (hθ σ hσ).1, rfl⟩⟩
  · intro s t hs hst ht
    have hs' := hθ s ⟨hs, hst.trans ht⟩
    have ht' := hθ t ⟨hs.trans hst, ht⟩
    have hle : θ s ≤ θ t := by
      by_contra hlt
      push Not at hlt
      have := hmono ht'.1 hs'.1 hlt
      rw [hs'.2, ht'.2] at this
      linarith
    exact hKγ _ _ hs'.1.1 hle ht'.1.2
  · intro σ hσ
    show f (θ σ) = f (θ (f 0)) + (σ - f 0)
    rw [(hθ σ hσ).2, (hθ _ ⟨le_rfl, h01.le⟩).2]
    ring

/-- Concatenation of two parametrised cone curves meeting at `b`. -/
theorem kc_concat {K : Set V} (hKadd : ∀ u ∈ K, ∀ v ∈ K, u + v ∈ K) {τ : V →L[ℝ] ℝ}
    {a b d : ℝ} (hab : a ≤ b) {η₁ η₂ : ℝ → V} (h1 : lc_KCurve K a b η₁) (h2 : lc_KCurve K b d η₂)
    (P1 : lc_Param τ a b η₁) (P2 : lc_Param τ b d η₂) (heq : η₁ b = η₂ b) :
    lc_KCurve K a d (fun s => if s ≤ b then η₁ s else η₂ s) ∧
      lc_Param τ a d (fun s => if s ≤ b then η₁ s else η₂ s) := by
  refine ⟨fun s t hs hst ht => ?_, fun s hs => ?_⟩
  · by_cases htb : t ≤ b
    · simp only [htb, hst.trans htb, ↓reduceIte]
      exact h1 s t hs hst htb
    · by_cases hsb : s ≤ b
      · simp only [htb, hsb, ↓reduceIte]
        have e : η₂ t - η₁ s = (η₂ t - η₂ b) + (η₁ b - η₁ s) := by rw [heq]; abel
        rw [e]
        exact hKadd _ (h2 b t le_rfl (le_of_not_ge htb) ht) _ (h1 s b hs hsb le_rfl)
      · simp only [htb, hsb, ↓reduceIte]
        exact h2 s t (le_of_not_ge hsb) hst ht
  · simp only [hab, ↓reduceIte]
    by_cases hsb : s ≤ b
    · simp only [hsb, ↓reduceIte]
      exact P1 s ⟨hs.1, hsb⟩
    · simp only [hsb, ↓reduceIte]
      rw [P2 s ⟨le_of_not_ge hsb, hs.2⟩, ← heq, P1 b ⟨hab, le_rfl⟩]
      ring

/-- **Row K3.** A chain of the restricted chart from `x ∈ B` gives a `τ₀`-parametrised
`K(c)`-curve on `[τ₀ x, τ₀ y]` from `x` to `y`, with values in `B`. -/
theorem kc_chain {x₀ : V} {c : ℝ} (hc : 0 < c) {B : Set V} (hB : IsOpen B) (hBM : B ⊆ S.M)
    (hcone : ∀ x ∈ B, ∀ v, S.FutCausal x v → v ∈ S.kc_K x₀ c) {x y : V} (hx : x ∈ B)
    (h : (S.restrict B hB hBM).Cau x y) :
    ∃ η : ℝ → V, lc_KCurve (S.kc_K x₀ c) (S.kc_τ x₀ x) (S.kc_τ x₀ y) η ∧
      lc_Param (S.kc_τ x₀) (S.kc_τ x₀ x) (S.kc_τ x₀ y) η ∧ η (S.kc_τ x₀ x) = x ∧
      η (S.kc_τ x₀ y) = y ∧ S.kc_τ x₀ x ≤ S.kc_τ x₀ y ∧
      ∀ σ ∈ Icc (S.kc_τ x₀ x) (S.kc_τ x₀ y), η σ ∈ B := by
  induction h with
  | refl =>
    refine ⟨fun _ => x, fun s t _ _ _ => by simpa using S.kc_K_zero x₀ c, fun s hs => ?_, rfl, rfl,
      le_rfl, fun _ _ => hx⟩
    have : s = S.kc_τ x₀ x := le_antisymm hs.2 hs.1
    simp [this]
  | @tail y z _ hst ih =>
    obtain ⟨η₁, hK1, hP1, h1a, h1b, hle1, hB1⟩ := ih
    obtain ⟨γ, hγ, h0, h1, hd, -⟩ := kc_cstep_arc hc hB hBM hcone hst
    obtain ⟨η₂, hK2, hP2, h2a, h2b, hlt2, hB2⟩ :=
      kc_reparam (τ := S.kc_τ x₀) hc hγ fun t ht => ⟨(hd t ht).2.1, (hd t ht).2.2⟩
    subst h0; subst h1
    obtain ⟨hKc, hPc⟩ := kc_concat (fun u hu v hv => S.kc_K_add hc.le hu hv) hle1 hK1 hK2 hP1 hP2
      (by rw [h1b, h2a])
    refine ⟨_, hKc, hPc, ?_, ?_, hle1.trans hlt2.le, fun σ hσ => ?_⟩
    · simp only [hle1, ↓reduceIte]; exact h1a
    · simp only [not_le.2 hlt2, ↓reduceIte]; exact h2b
    · by_cases hσb : σ ≤ S.kc_τ x₀ (γ 0)
      · simp only [hσb, ↓reduceIte]; exact hB1 σ ⟨hσ.1, hσb⟩
      · simp only [hσb, ↓reduceIte]
        obtain ⟨u, hu, e⟩ := hB2 σ ⟨le_of_not_ge hσb, hσ.2⟩
        rw [e]; exact (hd u hu).1

/-! ## Row K4: the local limit-curve theorem for causal chains in a chart -/

/-- **Row K4.** Around `x₀ ∈ M` there is a ball `B` and a cone `K(c)` such that chains of the
chart restricted to `B`, starting at points `xₙ → p` and rising by at least `δ` in `τ₀`, have
parametrisations on `[0, δ]` of which a subsequence converges uniformly to a `τ₀`-parametrised
`K(c)`-curve from `p`. -/
theorem kc_local_limit [FiniteDimensional ℝ V] {x₀ : V} (hx₀ : x₀ ∈ S.M) :
    ∃ r > 0, ∃ c > 0, ∃ hBM : ball x₀ r ⊆ S.M, closedBall x₀ r ⊆ S.M ∧
      ∀ (xs ys : ℕ → V) (p : V) (δ : ℝ), 0 < δ → (∀ n, xs n ∈ ball x₀ r) →
        (∀ n, (S.restrict (ball x₀ r) isOpen_ball hBM).Cau (xs n) (ys n)) →
        (∀ n, S.kc_τ x₀ (xs n) + δ ≤ S.kc_τ x₀ (ys n)) → Tendsto xs atTop (𝓝 p) →
        ∃ (ηs : ℕ → ℝ → V) (φ : ℕ → ℕ) (γ : ℝ → V),
          (∀ n, ηs n 0 = xs n ∧ ∀ s ∈ Icc (0:ℝ) δ, ηs n s ∈ ball x₀ r) ∧ StrictMono φ ∧
          TendstoUniformlyOn (fun n => ηs (φ n)) γ atTop (Icc 0 δ) ∧
          lc_KCurve (S.kc_K x₀ c) 0 δ γ ∧ lc_Param (S.kc_τ x₀) 0 δ γ ∧ γ 0 = p ∧
          ∀ s ∈ Icc (0:ℝ) δ, γ s ∈ closedBall x₀ r := by
  obtain ⟨r₁, hr₁, c, hc, hBM₁, hcone₁⟩ := S.kc_cone hx₀
  set r := r₁ / 2 with hrdef
  have hr : 0 < r := half_pos hr₁
  have hsub : ball x₀ r ⊆ ball x₀ r₁ := ball_subset_ball (half_le_self hr₁.le)
  have hBM : ball x₀ r ⊆ S.M := hsub.trans hBM₁
  have hcone : ∀ x ∈ ball x₀ r, ∀ v, S.FutCausal x v → v ∈ S.kc_K x₀ c :=
    fun x hx => hcone₁ x (hsub hx)
  refine ⟨r, hr, c, hc, hBM, (closedBall_subset_ball (half_lt_self hr₁)).trans hBM₁,
    fun xs ys p δ hδ hxB hcau hrise hp => ?_⟩
  set τ := S.kc_τ x₀
  have hch := fun n => kc_chain hc isOpen_ball hBM hcone (hxB n) (hcau n)
  choose η hK hP ha hb hle hB using hch
  set ηs : ℕ → ℝ → V := fun n s => η n (τ (xs n) + s) with hηs
  have hK' : ∀ n, lc_KCurve (S.kc_K x₀ c) 0 δ (ηs n) := fun n s t hs hst ht =>
    hK n _ _ (by linarith) (by linarith) (by linarith [hrise n])
  have hP' : ∀ n, lc_Param τ 0 δ (ηs n) := fun n s hs => by
    simp only [hηs, add_zero]
    rw [hP n _ ⟨by linarith [hs.1], by linarith [hs.2, hrise n]⟩, ha n]
    ring
  have h0 : ∀ n, ηs n 0 = xs n := fun n => by simp only [hηs, add_zero]; exact ha n
  obtain ⟨φ, γ, hφ, hu, hKγ, hPγ, hγ0⟩ := lc_limit_curve (S.kc_K_closed x₀ c) hc hδ.le
    (fun v hv => hv) hK' hP' (by simpa [h0] using hp)
  have hηB : ∀ n, ∀ s ∈ Icc (0:ℝ) δ, ηs n s ∈ ball x₀ r := fun n s hs =>
    hB n _ ⟨by linarith [hs.1], by linarith [hs.2, hrise n]⟩
  refine ⟨ηs, φ, γ, fun n => ⟨h0 n, hηB n⟩, hφ, hu, hKγ, hPγ, hγ0, fun s hs => ?_⟩
  exact isClosed_closedBall.mem_of_tendsto (hu.tendsto_at hs)
    (Eventually.of_forall fun n => ball_subset_closedBall (hηB (φ n) s hs))

end Spacetime
end KC

/-! ## Row K7: non-vacuity -/

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

lemma kc_mink_τ (v : ℝ × ℝ) : kc_mink.kc_τ 0 v = v.1 := by
  rw [Spacetime.kc_τ_apply]; show -kc_g0 v (1, 0) = v.1; rw [kc_g0_apply]; ring

/-- The arcs `γₙ(t) = (t r/2, r sin(m t)/(4m))`, `m = n + 1`. -/
noncomputable def kc_arc (r : ℝ) (n : ℕ) (t : ℝ) : ℝ × ℝ :=
  (t * (r / 2), r / (4 * ((n:ℝ) + 1)) * Real.sin (((n:ℝ) + 1) * t))

lemma kc_arc_hasDerivAt (r : ℝ) (n : ℕ) (t : ℝ) :
    HasDerivAt (kc_arc r n) (r / 2, r / 4 * Real.cos (((n:ℝ) + 1) * t)) t := by
  have hm : ((n:ℝ) + 1) ≠ 0 := by positivity
  have h1 : HasDerivAt (fun t : ℝ => t * (r / 2)) (r / 2) t := by
    simpa using (hasDerivAt_id t).mul_const (r / 2)
  have h2 : HasDerivAt (fun t : ℝ => r / (4 * ((n:ℝ) + 1)) * Real.sin (((n:ℝ) + 1) * t))
      (r / 4 * Real.cos (((n:ℝ) + 1) * t)) t := by
    have := (((hasDerivAt_id t).const_mul ((n:ℝ) + 1)).sin).const_mul (r / (4 * ((n:ℝ) + 1)))
    simp only [id] at this
    convert this using 1
    field_simp
  exact h1.prodMk h2

/-- Each arc is a step of the chart restricted to `ball 0 r`, from `0`. -/
lemma kc_arc_cstep {r : ℝ} (hr : 0 < r) (n : ℕ) :
    (kc_mink.restrict (ball 0 r) isOpen_ball (kc_mink_M r)).CStep 0 (kc_arc r n 1) := by
  have hm : (0:ℝ) < (n:ℝ) + 1 := by positivity
  refine ⟨kc_arc r n, ?_, by simp [kc_arc], rfl, fun t ht => ⟨?_, ?_⟩⟩
  · exact (contDiff_id.mul contDiff_const).prodMk (contDiff_const.mul
      (Real.contDiff_sin.comp (contDiff_const.mul contDiff_id)))
  · show kc_arc r n t ∈ ball (0 : ℝ × ℝ) r
    rw [mem_ball_zero_iff, Prod.norm_def]
    refine max_lt ?_ ?_
    · simp only [kc_arc, Real.norm_eq_abs]
      rw [abs_of_nonneg (by nlinarith [ht.1])]
      nlinarith [ht.2]
    · simp only [kc_arc, Real.norm_eq_abs, abs_mul]
      have hs := Real.abs_sin_le_one (((n:ℝ) + 1) * t)
      rw [abs_of_pos (by positivity : 0 < r / (4 * ((n:ℝ) + 1)))]
      have : r / (4 * ((n:ℝ) + 1)) ≤ r / 4 := by
        apply div_le_div_of_nonneg_left hr.le (by norm_num); nlinarith
      nlinarith [abs_nonneg (Real.sin (((n:ℝ) + 1) * t))]
  · rw [(kc_arc_hasDerivAt r n t).deriv]
    refine ⟨?_, ?_⟩
    · show kc_g0 _ _ ≤ 0
      rw [kc_g0_apply]
      have := Real.cos_sq_le_one (((n:ℝ) + 1) * t)
      simp only
      nlinarith [sq_nonneg r]
    · show kc_g0 _ (1, 0) < 0
      rw [kc_g0_apply]; simp only; linarith

/-- **Row K7.** The setting of K4 is inhabited by a genuinely varying sequence: in the 2D
Minkowski chart at `0`, for K4's ball `ball 0 r`, the arcs `γₙ` are chains from `0` rising by
`r/2` in `τ₀ = fst`, so K4 produces a uniform limit `τ₀`-parametrised cone curve from `0`. -/
theorem kc_witness :
    ∃ r > 0, ∃ c > 0, (∀ v : ℝ × ℝ, kc_mink.kc_τ 0 v = v.1) ∧
      (∀ n, (kc_mink.restrict (ball 0 r) isOpen_ball (kc_mink_M r)).Cau 0 (kc_arc r n 1)) ∧
      ∃ (ηs : ℕ → ℝ → ℝ × ℝ) (φ : ℕ → ℕ) (γ : ℝ → ℝ × ℝ), (∀ n, ηs n 0 = 0) ∧ StrictMono φ ∧
        TendstoUniformlyOn (fun n => ηs (φ n)) γ atTop (Icc 0 (r / 2)) ∧
        lc_KCurve (kc_mink.kc_K 0 c) 0 (r / 2) γ ∧ lc_Param (kc_mink.kc_τ 0) 0 (r / 2) γ ∧
        γ 0 = 0 := by
  obtain ⟨r, hr, c, hc, hBM, -, H⟩ := kc_mink.kc_local_limit (x₀ := (0 : ℝ × ℝ)) (mem_univ _)
  have hcau : ∀ n, (kc_mink.restrict (ball 0 r) isOpen_ball hBM).Cau 0 (kc_arc r n 1) :=
    fun n => Relation.ReflTransGen.single (kc_arc_cstep hr n)
  obtain ⟨ηs, φ, γ, hη, hφ, hu, hK, hP, hγ0, -⟩ := H (fun _ => 0) (fun n => kc_arc r n 1) 0 (r / 2)
    (half_pos hr) (fun _ => mem_ball_self hr) hcau
    (fun n => by rw [kc_mink_τ, kc_mink_τ]; simp [kc_arc]) tendsto_const_nhds
  exact ⟨r, hr, c, hc, kc_mink_τ, hcau, ηs, φ, γ, fun n => (hη n).1, hφ, hu, hK, hP, hγ0⟩

end Witness

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

end MSpacetime

/-! ## Row K5: on `N` -/

namespace MSpacetime
variable {S : MSpacetime E N} {p₀ : N}

/-- `OneChart` passes to an open `U ⊆ M`. -/
lemma kc_oneChart_restrict (hC : S.OneChart p₀) {U : Set N} (hU : IsOpen U) (hUM : U ⊆ S.M) :
    (S.restrictM U hU hUM).OneChart p₀ where
  sub := hUM.trans hC.sub
  g_C1 := hC.g_C1.mono (image_mono hUM)
  T_cont := hC.T_cont.mono (image_mono hUM)

/-- Chains of `N` restricted to `U` are chains of the chart restricted to any open `B ⊇ φ(U)`. -/
lemma kc_cau_transfer (hC : S.OneChart p₀) {U : Set N} {hU : IsOpen U} {hUM : U ⊆ S.M}
    {B : Set E} (hB : IsOpen B) (hBM : B ⊆ (chartSp hC).M)
    (hUB : ∀ x ∈ U, extChartAt 𝓘(ℝ, E) p₀ x ∈ B) {x y : N} (h : (S.restrictM U hU hUM).Cau x y) :
    ((chartSp hC).restrict B hB hBM).Cau (extChartAt 𝓘(ℝ, E) p₀ x) (extChartAt 𝓘(ℝ, E) p₀ y) := by
  have hC' := kc_oneChart_restrict hC hU hUM
  refine Relation.ReflTransGen.lift _ (fun a b hab => ?_) _ _ h
  obtain ⟨γ, hγ, h0, h1, ht⟩ := ch_cstep_NV hC' hab
  refine ⟨γ, hγ, h0, h1, fun t htI => ⟨?_, (ht t htI).2⟩⟩
  obtain ⟨z, hz, e⟩ := (ht t htI).1
  rw [← e]; exact hUB z hz

/-- **Row K5.** Under `OneChart p₀`, every `x₀ ∈ M` has an open neighbourhood `U ⊆ M`, a linear
`τ` and a closed cone `K` uniformly timelike for it, such that chains of `N` restricted to `U`,
starting at `xₙ → p ∈ U` and rising by `δ` in `τ ∘ φ`, have chart parametrisations `ηₙ` on
`[0, δ]` (pulled back into `U`) of which a subsequence converges uniformly in the chart to a
`τ`-parametrised `K`-curve `γ`; its pull-back `φ⁻¹ ∘ γ` is a continuous curve in `M` from `p`,
and the pulled-back parametrisations converge to it pointwise in `N`. -/
theorem kc_manifold_limit [FiniteDimensional ℝ E] (hC : S.OneChart p₀) {x₀ : N} (hx₀ : x₀ ∈ S.M) :
    ∃ (U : Set N) (hU : IsOpen U) (hUM : U ⊆ S.M), x₀ ∈ U ∧
      ∃ (τ : E →L[ℝ] ℝ) (K : Set E) (c : ℝ), 0 < c ∧ IsClosed K ∧ (∀ v ∈ K, c * ‖v‖ ≤ τ v) ∧
      ∀ (xs ys : ℕ → N) (p : N) (δ : ℝ), 0 < δ → (∀ n, xs n ∈ U) → p ∈ U →
        (∀ n, (S.restrictM U hU hUM).Cau (xs n) (ys n)) →
        (∀ n, τ (extChartAt 𝓘(ℝ, E) p₀ (xs n)) + δ ≤ τ (extChartAt 𝓘(ℝ, E) p₀ (ys n))) →
        Tendsto xs atTop (𝓝 p) →
        ∃ (ηs : ℕ → ℝ → E) (ψ : ℕ → ℕ) (γ : ℝ → E), StrictMono ψ ∧
          (∀ n, ηs n 0 = extChartAt 𝓘(ℝ, E) p₀ (xs n) ∧
            ∀ s ∈ Icc (0:ℝ) δ, (extChartAt 𝓘(ℝ, E) p₀).symm (ηs n s) ∈ U) ∧
          TendstoUniformlyOn (fun n => ηs (ψ n)) γ atTop (Icc 0 δ) ∧
          lc_KCurve K 0 δ γ ∧ lc_Param τ 0 δ γ ∧
          ContinuousOn (fun s => (extChartAt 𝓘(ℝ, E) p₀).symm (γ s)) (Icc 0 δ) ∧
          (extChartAt 𝓘(ℝ, E) p₀).symm (γ 0) = p ∧
          (∀ s ∈ Icc (0:ℝ) δ, (extChartAt 𝓘(ℝ, E) p₀).symm (γ s) ∈ S.M) ∧
          ∀ s ∈ Icc (0:ℝ) δ, Tendsto (fun n => (extChartAt 𝓘(ℝ, E) p₀).symm (ηs (ψ n) s)) atTop
            (𝓝 ((extChartAt 𝓘(ℝ, E) p₀).symm (γ s))) := by
  set φ := extChartAt 𝓘(ℝ, E) p₀ with hφ
  have hx₀' : φ x₀ ∈ (chartSp hC).M := ⟨x₀, hx₀, rfl⟩
  obtain ⟨r, hr, c, hc, hBM, hcl, H⟩ := (chartSp hC).kc_local_limit hx₀'
  have hMs : ∀ x ∈ S.M, x ∈ (chartAt E p₀).source := fun x hx => hC.sub hx
  have hφc : ContinuousOn φ S.M := (continuousOn_extChartAt p₀).mono fun x hx => by
    rw [extChartAt_source]; exact hMs x hx
  set U := S.M ∩ φ ⁻¹' ball (φ x₀) r with hUdef
  have hU : IsOpen U := hφc.isOpen_inter_preimage S.isOpen_M isOpen_ball
  have hUM : U ⊆ S.M := inter_subset_left
  -- points of `φ(M)` pull back into `M`
  have hpull : ∀ y ∈ (chartSp hC).M, φ.symm y ∈ S.M ∧ φ (φ.symm y) = y := by
    rintro y ⟨z, hz, rfl⟩
    rw [ch_left_inv p₀ (hMs z hz)]; exact ⟨hz, rfl⟩
  have htgt : ∀ y ∈ (chartSp hC).M, y ∈ φ.target := by
    rintro y ⟨z, hz, rfl⟩; exact ch_mem_target p₀ (hMs z hz)
  refine ⟨U, hU, hUM, ⟨hx₀, mem_ball_self hr⟩, (chartSp hC).kc_τ (φ x₀),
    (chartSp hC).kc_K (φ x₀) c, c, hc, (chartSp hC).kc_K_closed _ _, fun v hv => hv,
    fun xs ys p δ hδ hxU hpU hcau hrise hp => ?_⟩
  have hcau' : ∀ n, ((chartSp hC).restrict (ball (φ x₀) r) isOpen_ball hBM).Cau (φ (xs n))
      (φ (ys n)) := fun n => kc_cau_transfer hC isOpen_ball hBM (fun x hx => hx.2) (hcau n)
  have hp' : Tendsto (fun n => φ (xs n)) atTop (𝓝 (φ p)) :=
    (ch_contAt p₀ (hMs p hpU.1)).tendsto.comp hp
  obtain ⟨ηs, ψ, γ, hη, hψ, hu, hK, hP, hγ0, hγB⟩ :=
    H (fun n => φ (xs n)) (fun n => φ (ys n)) (φ p) δ hδ (fun n => (hxU n).2) hcau' hrise hp'
  have hγM : ∀ s ∈ Icc (0:ℝ) δ, γ s ∈ (chartSp hC).M := fun s hs => hcl (hγB s hs)
  have hsymmAt : ∀ y ∈ (chartSp hC).M, ContinuousAt φ.symm y := fun y hy =>
    (continuousOn_extChartAt_symm p₀).continuousAt
      ((isOpen_extChartAt_target p₀).mem_nhds (htgt y hy))
  have hγc : ContinuousOn γ (Icc 0 δ) := by
    rw [Metric.continuousOn_iff]
    intro b hb ε hε
    refine ⟨c * ε, mul_pos hc hε, fun a ha hab => ?_⟩
    rw [dist_eq_norm]
    have h1 := lc_param_lipschitz hc (fun v hv => hv) hK hP hb ha
    rw [Real.dist_eq] at hab
    calc ‖γ a - γ b‖ ≤ |a - b| / c := h1
      _ < c * ε / c := by gcongr
      _ = ε := by field_simp
  refine ⟨ηs, ψ, γ, hψ, fun n => ⟨(hη n).1, fun s hs => ?_⟩, hu, hK, hP, ?_, ?_, fun s hs => ?_,
    fun s hs => ?_⟩
  · have hy := hBM ((hη n).2 s hs)
    exact ⟨(hpull _ hy).1, by simp only [mem_preimage]; rw [(hpull _ hy).2]; exact (hη n).2 s hs⟩
  · exact fun s hs => ((hsymmAt _ (hγM s hs)).comp_continuousWithinAt (hγc s hs))
  · rw [hγ0]; exact ch_left_inv p₀ (hMs p hpU.1)
  · exact (hpull _ (hγM s hs)).1
  · exact (hsymmAt _ (hγM s hs)).tendsto.comp (hu.tendsto_at hs)

end MSpacetime

end Manifold

end ShadowProbe.ConeCurvesProbe

#print axioms ShadowProbe.ConeCurvesProbe.Spacetime.kc_cone
#print axioms ShadowProbe.ConeCurvesProbe.Spacetime.kc_cau_K
#print axioms ShadowProbe.ConeCurvesProbe.Spacetime.kc_chain
#print axioms ShadowProbe.ConeCurvesProbe.Spacetime.kc_local_limit
#print axioms ShadowProbe.ConeCurvesProbe.MSpacetime.kc_manifold_limit
#print axioms ShadowProbe.ConeCurvesProbe.kc_witness

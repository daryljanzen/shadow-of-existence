import Mathlib

/-!
# P1's 6b-ii, phase 1: cone curves in a chart and the local limit-curve theorem

Registration: `computations/formalisation/r7807_71_6bii/PREDICTION.md`; plan `PLAN.md`. Mathlib only; nothing
imports this file. In a finite-dimensional normed space `E`, a closed convex cone `K` uniformly timelike for a linear
`τ` (`c‖v‖ ≤ τ v` on `K`) plays the light cone of a chart, widened to a constant cone. `K`-curves have their increments
in `K`.
-/

open Set Filter Topology BoundedContinuousFunction

namespace ShadowProbe.LimitCurveProbe

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

/-! ## Row L4: non-vacuity -/

/-- The 2D Minkowski cone `{(t, x) : |x| ≤ t}` in `ℝ × ℝ` (sup norm), with `τ(t, x) = t`. -/
def lc_K2 : Set (ℝ × ℝ) := {v | |v.2| ≤ v.1}

/-- The curves `γₙ(s) = (s, sin(ns)/n)`. -/
noncomputable def lc_γ (n : ℕ) (s : ℝ) : ℝ × ℝ := (s, Real.sin (n * s) / n)

/-- **Row L4.** The setting is inhabited: `lc_K2` is closed and uniformly timelike for `τ = fst` with `c = 1`; each
`γₙ` is a `τ`-parametrised `lc_K2`-curve on `[0, 1]` starting at the origin; so `lc_limit_curve` applies and yields a
uniformly convergent subsequence with a `τ`-parametrised `lc_K2`-curve limit through the origin. -/
theorem lc_witness :
    IsClosed lc_K2 ∧ (∀ v ∈ lc_K2, 1 * ‖v‖ ≤ ContinuousLinearMap.fst ℝ ℝ ℝ v) ∧
      (∀ n, lc_KCurve lc_K2 0 1 (lc_γ n)) ∧ (∀ n, lc_Param (ContinuousLinearMap.fst ℝ ℝ ℝ) 0 1 (lc_γ n)) ∧
      ∃ (φ : ℕ → ℕ) (γ : ℝ → ℝ × ℝ), StrictMono φ ∧
        TendstoUniformlyOn (fun n => lc_γ (φ n)) γ atTop (Icc 0 1) ∧ lc_KCurve lc_K2 0 1 γ ∧
        lc_Param (ContinuousLinearMap.fst ℝ ℝ ℝ) 0 1 γ ∧ γ 0 = 0 := by
  have hcl : IsClosed lc_K2 := isClosed_le continuous_snd.abs continuous_fst
  have hK : ∀ v ∈ lc_K2, 1 * ‖v‖ ≤ ContinuousLinearMap.fst ℝ ℝ ℝ v := by
    intro v hv
    simp only [lc_K2, mem_ofPred_eq] at hv
    have h0 : 0 ≤ v.1 := (abs_nonneg _).trans hv
    rw [one_mul, Prod.norm_def, Real.norm_eq_abs, Real.norm_eq_abs, abs_of_nonneg h0]
    simpa using hv
  have hKc : ∀ n, lc_KCurve lc_K2 0 1 (lc_γ n) := by
    intro n s t _ hst _
    simp only [lc_K2, lc_γ, mem_ofPred_eq, Prod.snd_sub, Prod.fst_sub]
    rcases Nat.eq_zero_or_pos n with rfl | hn
    · simp; linarith
    · have hn' : (0 : ℝ) < n := by exact_mod_cast hn
      rw [← sub_div, abs_div, abs_of_pos hn', div_le_iff₀ hn']
      calc |Real.sin (n * t) - Real.sin (n * s)| ≤ |n * t - n * s| := Real.abs_sin_sub_sin_le _ _
        _ = (t - s) * n := by rw [← mul_sub, abs_mul, abs_of_pos hn', abs_of_nonneg (by linarith)]; ring
  have hP : ∀ n, lc_Param (ContinuousLinearMap.fst ℝ ℝ ℝ) 0 1 (lc_γ n) := by
    intro n s _; simp [lc_γ]
  refine ⟨hcl, hK, hKc, hP, ?_⟩
  exact lc_limit_curve hcl one_pos zero_le_one hK hKc hP (p := 0) (by simp [lc_γ])

end ShadowProbe.LimitCurveProbe

#print axioms ShadowProbe.LimitCurveProbe.lc_lipschitz_bound
#print axioms ShadowProbe.LimitCurveProbe.lc_param_lipschitz
#print axioms ShadowProbe.LimitCurveProbe.lc_limit_closed
#print axioms ShadowProbe.LimitCurveProbe.lc_limit_curve
#print axioms ShadowProbe.LimitCurveProbe.lc_witness

import Mathlib

/-!
# Probe `r7637+71.2` (campaign 74, `r7637` ④): the slice lower limit `𝓗⁺ ⊆ KLi(S_τ)` and the
# Kuratowski convergence `S_τ → 𝓗⁺`

Registration: `computations/formalisation/r7637_71_campaign74/PREDICTION.md`. Nothing imports this
file, and it imports no other probe.

## Setting

Campaign 72's `probes/HorizonConvergence.lean` copied verbatim under this namespace with every
theorem renamed `hc_… ↦ sc_…`, plus campaign 60's `restrict`, `InextCausalCurve`,
`IsCauchyTemporal`, `GloballyHyperbolic`, `ExteriorGH` (`probes/CausalStructure.lean`).
`D = I⁻(𝒥⁺)`, `𝓗⁺ = H = frontier J⁻(𝒥⁺)`, `S_τ = slice J Θ τ = {x ∈ D | Θ x = τ}`.

## ① `Θ → ∞` at `𝓗⁺` — from a stated properness hypothesis

`SublevelProper J Θ : ∀ T, closure {x ∈ D | Θ x ≤ T} ⊆ D` — sublevel sets of `Θ` in `D` do not
accumulate on `∂D ⊇ 𝓗⁺`. For continuous `Θ` it is equivalent to every sublevel set
`{x ∈ D | Θ x ≤ T}` being closed in `V` (`sc_sublevelProper_iff`), and it is *equivalent* to the
blow-up `Θ x → ∞` as `x → p` in `D` at every `p ∉ D` (`sc_sublevelProper_iff_tendsto`).
The Cauchy property of `Θ` on `D` gives `Θ → ∞` along every causal curve of `D` running into `𝓗⁺`
(such a curve is future-inextendible in `D`, so it meets every level); passing from curves to
arbitrary approaches needs limit curves and is not attempted, so properness is taken.

## ② The slice lower limit

`LocConnAt J p : ∀ U ∈ 𝓝 p, ∃ W ∈ 𝓝 p, W ⊆ U ∧ IsPreconnected (W ∩ D)` — `D` is locally connected
at the horizon point `p`. With `p ∈ closure D` (campaign 72's `hcl`), continuity of `Θ` on `D`, and
① inside `W ∩ D`, the intermediate value theorem on `W ∩ D` hits every `τ ≥ Θ x₀`.

## ③ `KLi(S_τ) = KLs(S_τ) = 𝓗⁺`

Combines ② with campaign 72's slice upper limit. `sc_slice_kuratowski_temporalD` takes `Θ` temporal
on `D` only (the paper's setting): `sc_temporalD_chr` shows such a `Θ` increases along every `≪`
ending in `D`, since a timelike step ending in `D` runs inside `D`.
-/

open Set Filter Topology Metric

namespace ShadowProbe.SliceConvergenceProbe

variable {V : Type*} [NormedAddCommGroup V] [NormedSpace ℝ V]

/-- A time-oriented Lorentzian chart (campaign 60). -/
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

lemma cont_gvw {X : Type*} [TopologicalSpace X] {x v w : X → V} (hx : Continuous x)
    (hv : Continuous v) (hw : Continuous w) : Continuous fun a => S.g (x a) (v a) (w a) :=
  ((S.cont_g.comp hx).clm_apply hv).clm_apply hw

lemma isOpen_timelikePairs :
    IsOpen {pv : V × V | pv.1 ∈ S.M ∧ S.FutTimelike pv.1 pv.2} := by
  refine (S.isOpen_M.preimage continuous_fst).inter (IsOpen.inter ?_ ?_)
  · exact isOpen_lt (S.cont_gvw continuous_fst continuous_snd continuous_snd) continuous_const
  · exact isOpen_lt (S.cont_gvw continuous_fst continuous_snd
      (S.cont_T.comp continuous_fst)) continuous_const

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

/-- `I⁻(p)` is open (campaign 60's `cs_isOpen_Ipast`). -/
theorem sc_isOpen_Ipast (p : V) : IsOpen (S.Ipast p) := by
  refine isOpen_iff_mem_nhds.2 fun q hq => ?_
  obtain ⟨y, hqy, hyp⟩ := Relation.TransGen.head'_iff.1 hq
  filter_upwards [S.tstep_start_eventually hqy] with q' hq'
  exact Relation.TransGen.head' hq' hyp

lemma tstep_to_cstep {x y : V} (h : S.TStep x y) : S.CStep x y := by
  obtain ⟨γ, hγ, h0, h1, hγt⟩ := h
  exact ⟨γ, hγ, h0, h1, fun t ht => ⟨(hγt t ht).1, (hγt t ht).2.1.le, (hγt t ht).2.2⟩⟩

/-- `≪ ⊆ ≤`. -/
theorem sc_chr_cau {x y : V} (h : S.Chr x y) : S.Cau x y := by
  induction h with
  | single h => exact Relation.ReflTransGen.single (S.tstep_to_cstep h)
  | tail _ h ih => exact ih.tail (S.tstep_to_cstep h)

theorem sc_chr_trans {x y z : V} (h1 : S.Chr x y) (h2 : S.Chr y z) : S.Chr x z :=
  Relation.TransGen.trans h1 h2

theorem sc_cau_trans {x y z : V} (h1 : S.Cau x y) (h2 : S.Cau y z) : S.Cau x z :=
  Relation.ReflTransGen.trans h1 h2

theorem sc_Ipast_subset_Jpast (p : V) : S.Ipast p ⊆ S.Jpast p := fun _ h => S.sc_chr_cau h

/-- `I⁻(p) ⊆ int J⁻(p)`. -/
theorem sc_Ipast_subset_interior (p : V) : S.Ipast p ⊆ interior (S.Jpast p) :=
  interior_maximal (S.sc_Ipast_subset_Jpast p) (S.sc_isOpen_Ipast p)

/-! ### Temporal functions (campaign 60) -/

/-- A temporal function: `C¹`, with `dτ(v) > 0` for every future-causal `v` on `M`. -/
def IsTemporal (τ : V → ℝ) : Prop :=
  ContDiff ℝ 1 τ ∧ ∀ x ∈ S.M, ∀ v, S.FutCausal x v → 0 < fderiv ℝ τ x v

lemma temporal_tstep {τ : V → ℝ} (hτ : S.IsTemporal τ) {x y : V} (h : S.TStep x y) :
    τ x < τ y := by
  obtain ⟨γ, hγ, h0, h1, hγt⟩ := h
  have hc : ContDiff ℝ 1 (τ ∘ γ) := hτ.1.comp hγ
  have hmono : StrictMonoOn (τ ∘ γ) (Icc (0:ℝ) 1) := by
    refine strictMonoOn_of_deriv_pos (convex_Icc 0 1) hc.continuous.continuousOn fun t ht => ?_
    rw [interior_Icc] at ht
    have hti : t ∈ Icc (0:ℝ) 1 := Ioo_subset_Icc_self ht
    have hd : HasDerivAt (τ ∘ γ) (fderiv ℝ τ (γ t) (deriv γ t)) t :=
      ((hτ.1.differentiable one_ne_zero) (γ t)).hasFDerivAt.comp_hasDerivAt t
        (hasDerivAt_of_contDiff hγ t)
    rw [hd.deriv]
    obtain ⟨hm, h1, h2⟩ := hγt t hti
    exact hτ.2 _ hm _ ⟨h1.le, h2⟩
  have := hmono ⟨le_rfl, zero_le_one⟩ ⟨zero_le_one, le_rfl⟩ zero_lt_one
  simpa [h0, h1] using this

/-- A temporal function increases strictly along `≪` (campaign 60's `cs_temporal_chr`). -/
theorem sc_temporal_chr {τ : V → ℝ} (hτ : S.IsTemporal τ) {x y : V} (h : S.Chr x y) :
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

theorem sc_D_subset_JpastSet : S.D J ⊆ S.JpastSet J :=
  biUnion_mono subset_rfl fun p _ => S.sc_Ipast_subset_Jpast p

/-- `p ∈ D ⟹ J⁻(p) ⊆ J⁻(𝒥⁺)` (transitivity only). -/
theorem sc_Jpast_subset_JpastSet {p : V} (hp : p ∈ S.D J) : S.Jpast p ⊆ S.JpastSet J := by
  intro q hq
  simp only [D, IpastSet, JpastSet, mem_iUnion] at hp ⊢
  obtain ⟨z, hz, hpz⟩ := hp
  exact ⟨z, hz, S.sc_cau_trans hq (S.sc_chr_cau hpz)⟩

/-! ### Kuratowski limits as `τ → ∞` -/

end Spacetime

/-- Kuratowski lower limit of a family of sets as `τ → ∞`. -/
def KLi (A : ℝ → Set V) : Set V := {p | ∀ U ∈ 𝓝 p, ∀ᶠ τ in atTop, (A τ ∩ U).Nonempty}
/-- Kuratowski upper limit of a family of sets as `τ → ∞`. -/
def KLs (A : ℝ → Set V) : Set V := {p | ∀ U ∈ 𝓝 p, ∃ᶠ τ in atTop, (A τ ∩ U).Nonempty}

omit [NormedSpace ℝ V] in
/-- `Li ⊆ Ls`. -/
theorem sc_KLi_subset_KLs (A : ℝ → Set V) : KLi A ⊆ KLs A :=
  fun _ hp U hU => (hp U hU).frequently

omit [NormedSpace ℝ V] in
/-- A preconnected set that meets `A` at `a` and contains a point `p ∉ int A` meets `∂A`. -/
theorem sc_preconnected_inter_frontier {C A : Set V} (hC : IsPreconnected C) {a p : V}
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

omit [NormedSpace ℝ V] in
/-- Membership in `Ls` from a sequence: `yₙ ∈ A τₙ`, `τₙ → ∞`, `yₙ → y` give `y ∈ Ls A`. -/
theorem sc_mem_KLs_of_seq {A : ℝ → Set V} {τ : ℕ → ℝ} {y : ℕ → V} {y₀ : V}
    (hτ : Tendsto τ atTop atTop) (hy : Tendsto y atTop (𝓝 y₀)) (hA : ∀ n, y n ∈ A (τ n)) :
    y₀ ∈ KLs A := by
  intro U hU
  rw [frequently_atTop]
  intro T
  obtain ⟨n, hn1, hn2⟩ := ((hy.eventually hU).and (hτ.eventually_ge_atTop T)).exists
  exact ⟨τ n, hn2, y n, hA n, hn1⟩

namespace Spacetime
variable (S : Spacetime V) (J : Set V)

/-- The family of past light cones `∂J⁻(O τ)`. -/
def cone (O : ℝ → V) (τ : ℝ) : Set V := frontier (S.Jpast (O τ))

/-! ### The observer -/

section Observer
variable {S J} {O : ℝ → V} (hOD : S.IpastSet (range O) = S.D J)
  (hmono : ∀ s t : ℝ, s < t → S.Chr (O s) (O t))
include hOD hmono

omit hOD in
/-- `I⁻(O σ) ⊆ I⁻(O τ)` for `σ ≤ τ`. -/
theorem sc_Ipast_mono {σ τ : ℝ} (h : σ ≤ τ) : S.Ipast (O σ) ⊆ S.Ipast (O τ) := by
  rcases h.lt_or_eq with h | h
  · exact fun q hq => S.sc_chr_trans hq (hmono σ τ h)
  · rw [h]

/-- Each `O τ` lies in `D`. -/
theorem sc_observer_mem_D (τ : ℝ) : O τ ∈ S.D J := by
  rw [← hOD]
  exact mem_biUnion (mem_range_self (τ + 1)) (hmono τ (τ + 1) (by linarith))

/-- `x ∈ D ⟹ x ∈ I⁻(O τ)` for all large `τ`. -/
theorem sc_D_eventually {x : V} (hx : x ∈ S.D J) : ∀ᶠ τ in atTop, x ∈ S.Ipast (O τ) := by
  rw [← hOD] at hx
  simp only [IpastSet, mem_iUnion] at hx
  obtain ⟨_, ⟨σ, rfl⟩, hσ⟩ := hx
  filter_upwards [eventually_ge_atTop σ] with τ hτ
  exact S.sc_Ipast_mono hmono hτ hσ

/-- `J⁻(O τ) ⊆ J⁻(𝒥⁺)`, hence `int J⁻(O τ) ⊆ int J⁻(𝒥⁺)`. -/
theorem sc_interior_cone_subset (τ : ℝ) :
    interior (S.Jpast (O τ)) ⊆ interior (S.JpastSet J) :=
  interior_mono (S.sc_Jpast_subset_JpastSet J (S.sc_observer_mem_D hOD hmono τ))

/-! ### ① The lower limit -/

/-- **Lower limit** `𝓗⁺ ⊆ Li ∂J⁻(O τ)`: every horizon point `p` is approached, for *every* large
`τ`, by points of `∂J⁻(O τ)`. Hypothesis: `closure J⁻(𝒥⁺) ⊆ closure D`. -/
theorem sc_lower_limit (hcl : closure (S.JpastSet J) ⊆ closure (S.D J)) :
    S.H J ⊆ KLi (S.cone O) := by
  intro p hp U hU
  obtain ⟨ε, hε, hεU⟩ := Metric.mem_nhds_iff.1 hU
  have hpD : p ∈ closure (S.D J) := hcl (frontier_subset_closure hp)
  obtain ⟨x, hxD, hxb⟩ : ∃ x ∈ S.D J, x ∈ ball p ε := by
    obtain ⟨x, hx, hxb⟩ := Metric.mem_closure_iff.1 hpD ε hε
    exact ⟨x, hx, by rw [mem_ball, dist_comm]; exact hxb⟩
  filter_upwards [S.sc_D_eventually hOD hmono hxD] with τ hτ
  have hpi : p ∉ interior (S.Jpast (O τ)) :=
    fun h => hp.2 (S.sc_interior_cone_subset hOD hmono τ h)
  obtain ⟨y, hyb, hyf⟩ := sc_preconnected_inter_frontier isPreconnected_ball
    ⟨hxb, S.sc_Ipast_subset_Jpast _ hτ⟩ (mem_ball_self hε) hpi
  exact ⟨y, hyf, hεU hyb⟩

/-- The lower limit in the registered form: for every neighbourhood `U` of `p ∈ 𝓗⁺` and every `T`
there is `τ ≥ T` with `∂J⁻(O τ) ∩ U ≠ ∅`. -/
theorem sc_lower_limit_exists (hcl : closure (S.JpastSet J) ⊆ closure (S.D J)) {p : V}
    (hp : p ∈ S.H J) {U : Set V} (hU : U ∈ 𝓝 p) (T : ℝ) :
    ∃ τ ≥ T, (frontier (S.Jpast (O τ)) ∩ U).Nonempty :=
  ((S.sc_lower_limit hOD hmono hcl hp U hU).and (eventually_ge_atTop T)).exists.imp
    fun _ h => ⟨h.2, h.1⟩

/-- The lower limit with sequences: `p = lim yₙ`, `yₙ ∈ ∂J⁻(O τₙ)`, `τₙ → ∞`. -/
theorem sc_lower_limit_seq (hcl : closure (S.JpastSet J) ⊆ closure (S.D J)) {p : V}
    (hp : p ∈ S.H J) :
    ∃ τ : ℕ → ℝ, ∃ y : ℕ → V, Tendsto τ atTop atTop ∧ Tendsto y atTop (𝓝 p) ∧
      ∀ n, y n ∈ frontier (S.Jpast (O (τ n))) := by
  have h : ∀ n : ℕ, ∃ τ ≥ (n:ℝ), ∃ y ∈ frontier (S.Jpast (O τ)), y ∈ ball p (1 / ((n:ℝ) + 1)) :=
    fun n => S.sc_lower_limit_exists hOD hmono hcl hp (ball_mem_nhds p (by positivity)) n
  choose τ hτ y hy hyb using h
  refine ⟨τ, y, tendsto_atTop_mono hτ tendsto_natCast_atTop_atTop, ?_, hy⟩
  rw [tendsto_iff_dist_tendsto_zero]
  refine squeeze_zero (fun _ => dist_nonneg) (fun n => (mem_ball.1 (hyb n)).le)
    tendsto_one_div_add_atTop_nhds_zero_nat

/-! ### ② The upper limit -/

/-- **Upper limit, unconditional part** `Ls ∂J⁻(O τ) ⊆ closure J⁻(𝒥⁺) \ D`. -/
theorem sc_upper_limit_closure_diff :
    KLs (S.cone O) ⊆ closure (S.JpastSet J) \ S.D J := by
  intro y hy
  refine ⟨?_, fun hyD => ?_⟩
  · rw [mem_closure_iff_nhds]
    intro U hU
    obtain ⟨W, hWU, hWo, hyW⟩ := _root_.mem_nhds_iff.1 hU
    obtain ⟨τ, z, hzf, hzW⟩ := (hy W (hWo.mem_nhds hyW)).exists
    obtain ⟨w, hwW, hwJ⟩ := mem_closure_iff.1 (frontier_subset_closure hzf) W hWo hzW
    exact ⟨w, hWU hwW, S.sc_Jpast_subset_JpastSet J (S.sc_observer_mem_D hOD hmono τ) hwJ⟩
  · rw [← hOD] at hyD
    simp only [IpastSet, mem_iUnion] at hyD
    obtain ⟨_, ⟨σ, rfl⟩, hσ⟩ := hyD
    have hfr := hy _ ((S.sc_isOpen_Ipast (O σ)).mem_nhds hσ)
    obtain ⟨τ, hτσ, z, hzf, hzI⟩ := frequently_atTop.1 hfr σ
    exact hzf.2 (S.sc_Ipast_subset_interior _ (S.sc_Ipast_mono hmono hτσ hzI))

/-- **Upper limit** `Ls ∂J⁻(O τ) ⊆ 𝓗⁺`, given `int J⁻(𝒥⁺) ⊆ D`. -/
theorem sc_upper_limit (hint : interior (S.JpastSet J) ⊆ S.D J) :
    KLs (S.cone O) ⊆ S.H J := by
  intro y hy
  obtain ⟨h1, h2⟩ := S.sc_upper_limit_closure_diff hOD hmono hy
  exact ⟨h1, fun hi => h2 (hint hi)⟩

/-- **Upper limit with sequences**: `yₙ ∈ ∂J⁻(O τₙ)`, `τₙ → ∞`, `yₙ → y` give `y ∈ 𝓗⁺`. -/
theorem sc_upper_limit_seq (hint : interior (S.JpastSet J) ⊆ S.D J) {τ : ℕ → ℝ} {y : ℕ → V}
    {y₀ : V} (hτ : Tendsto τ atTop atTop) (hy : Tendsto y atTop (𝓝 y₀))
    (hA : ∀ n, y n ∈ frontier (S.Jpast (O (τ n)))) : y₀ ∈ S.H J :=
  S.sc_upper_limit hOD hmono hint (sc_mem_KLs_of_seq (A := S.cone O) hτ hy hA)

/-! ### ③ The clause in Kuratowski form -/

/-- **`∂J⁻(O τ) → 𝓗⁺` in the Kuratowski sense** as `τ → ∞`. -/
theorem sc_kuratowski (hcl : closure (S.JpastSet J) ⊆ closure (S.D J))
    (hint : interior (S.JpastSet J) ⊆ S.D J) :
    KLi (S.cone O) = S.H J ∧ KLs (S.cone O) = S.H J := by
  have h1 := S.sc_lower_limit hOD hmono hcl
  have h2 := S.sc_upper_limit hOD hmono hint
  have h3 := sc_KLi_subset_KLs (S.cone O)
  exact ⟨(h3.trans h2).antisymm h1, h2.antisymm (h1.trans h3)⟩

omit hOD hmono in
/-- Under the two hypotheses, `𝓗⁺ = closure D \ D`. -/
theorem sc_H_eq_closure_diff (hcl : closure (S.JpastSet J) ⊆ closure (S.D J))
    (hint : interior (S.JpastSet J) ⊆ S.D J) :
    S.H J = closure (S.D J) \ S.D J := by
  ext p
  constructor
  · intro hp
    refine ⟨hcl (frontier_subset_closure hp), fun hpD => hp.2 ?_⟩
    exact interior_maximal (S.sc_D_subset_JpastSet J)
      (isOpen_biUnion fun z _ => S.sc_isOpen_Ipast z) hpD
  · rintro ⟨h1, h2⟩
    exact ⟨closure_mono (S.sc_D_subset_JpastSet J) h1, fun hi => h2 (hint hi)⟩

/-! ### The slices `S_τ` accumulate on `𝓗⁺` -/

omit hmono in
/-- **Slices, upper limit.** Adapted `Θ`: `Θ (O τ) = τ + c`, and `Θ` increases along every `≪`
ending on the worldline. Then `Ls S_τ ⊆ closure J⁻(𝒥⁺) \ D`, and `⊆ 𝓗⁺` given `int J⁻(𝒥⁺) ⊆ D`. -/
theorem sc_slice_upper_limit {Θ : V → ℝ} {c : ℝ} (hadapt : ∀ τ, Θ (O τ) = τ + c)
    (hΘ : ∀ x σ, S.Chr x (O σ) → Θ x < Θ (O σ)) :
    KLs (S.slice J Θ) ⊆ closure (S.JpastSet J) \ S.D J ∧
    (interior (S.JpastSet J) ⊆ S.D J → KLs (S.slice J Θ) ⊆ S.H J) := by
  have key : KLs (S.slice J Θ) ⊆ closure (S.JpastSet J) \ S.D J := by
    intro y hy
    refine ⟨?_, fun hyD => ?_⟩
    · rw [mem_closure_iff_nhds]
      intro U hU
      obtain ⟨τ, z, hz, hzU⟩ := (hy U hU).exists
      exact ⟨z, hzU, S.sc_D_subset_JpastSet J hz.1⟩
    · rw [← hOD] at hyD
      simp only [IpastSet, mem_iUnion] at hyD
      obtain ⟨_, ⟨σ, rfl⟩, hσ⟩ := hyD
      have hfr := hy _ ((S.sc_isOpen_Ipast (O σ)).mem_nhds hσ)
      obtain ⟨τ, hτ, z, hz, hzI⟩ := frequently_atTop.1 hfr (σ + c)
      have := hΘ z σ hzI
      rw [hadapt, hz.2] at this
      linarith
  refine ⟨key, fun hint y hy => ?_⟩
  obtain ⟨h1, h2⟩ := key hy
  exact ⟨h1, fun hi => h2 (hint hi)⟩

omit hmono in
/-- Slices, upper limit, for a temporal `Θ` on `M` adapted to `O`. -/
theorem sc_slice_upper_limit_temporal (hint : interior (S.JpastSet J) ⊆ S.D J) {Θ : V → ℝ}
    {c : ℝ} (hΘ : S.IsTemporal Θ) (hadapt : ∀ τ, Θ (O τ) = τ + c) :
    KLs (S.slice J Θ) ⊆ S.H J :=
  (S.sc_slice_upper_limit hOD hadapt fun _ _ h => S.sc_temporal_chr hΘ h).2 hint

omit hmono in
/-- Slices with sequences: `xₙ ∈ S_{τₙ}`, `τₙ → ∞`, `xₙ → x` give `x ∈ 𝓗⁺`. -/
theorem sc_slice_upper_limit_seq (hint : interior (S.JpastSet J) ⊆ S.D J) {Θ : V → ℝ}
    {c : ℝ} (hadapt : ∀ τ, Θ (O τ) = τ + c) (hΘ : ∀ x σ, S.Chr x (O σ) → Θ x < Θ (O σ))
    {τ : ℕ → ℝ} {x : ℕ → V} {x₀ : V} (hτ : Tendsto τ atTop atTop)
    (hx : Tendsto x atTop (𝓝 x₀)) (hA : ∀ n, x n ∈ S.slice J Θ (τ n)) : x₀ ∈ S.H J :=
  (S.sc_slice_upper_limit hOD hadapt hΘ).2 hint (sc_mem_KLs_of_seq hτ hx hA)

end Observer

/-! ## Campaign 74: the slice lower limit

### Campaign 60's Cauchy-temporal definitions (copied) -/

/-- Points of `I⁻(z)` lie in `M` (campaign 60's `cs_Ipast_subset_M`). -/
theorem sc_Ipast_subset_M (z : V) : S.Ipast z ⊆ S.M := by
  intro q hq
  obtain ⟨b, ⟨γ, -, h0, -, hγ⟩, -⟩ := Relation.TransGen.head'_iff.1 hq
  rw [← h0]; exact (hγ 0 ⟨le_rfl, zero_le_one⟩).1

/-- `D` is open (campaign 60's `cs_D_open`). -/
theorem sc_D_open : IsOpen (S.D J) := isOpen_biUnion fun z _ => S.sc_isOpen_Ipast z

/-- `D ⊆ M` (campaign 60's `cs_D_subset_M`). -/
theorem sc_D_subset_M : S.D J ⊆ S.M := iUnion₂_subset fun z _ => S.sc_Ipast_subset_M z

/-- The same chart with `M` replaced by an open subset `U ⊆ M` (campaign 60). -/
def restrict (U : Set V) (hU : IsOpen U) (hUM : U ⊆ S.M) : Spacetime V where
  M := U
  isOpen_M := hU
  g := S.g
  cont_g := S.cont_g
  symm := S.symm
  T := S.T
  cont_T := S.cont_T
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

/-- Global hyperbolicity as the existence of a Cauchy temporal function (campaign 60). -/
def GloballyHyperbolic : Prop := ∃ τ : V → ℝ, S.IsCauchyTemporal τ

/-- The exterior `D` regarded as a spacetime in its own right. -/
def Dsp : Spacetime V := S.restrict (S.D J) (S.sc_D_open J) (S.sc_D_subset_M J)

/-- `prop:causal-alignment`'s hypothesis "`D` is globally hyperbolic" (campaign 60's
`ExteriorGH`). -/
def ExteriorGH : Prop := (S.Dsp J).GloballyHyperbolic

/-! ### `Θ` temporal on `D` only: increase along `≪` into `D`

This removes campaign 72's need for `Θ` temporal on all of `M`: a timelike step ending in `D` runs
inside `D`, so a function temporal on `D` (the paper's setting) increases along it. -/

/-- `≪` into `D` starts in `D`. -/
theorem sc_D_of_chr {x y : V} (h : S.Chr x y) (hy : y ∈ S.D J) : x ∈ S.D J := by
  simp only [D, IpastSet, mem_iUnion] at hy ⊢
  obtain ⟨z, hz, hyz⟩ := hy
  exact ⟨z, hz, S.sc_chr_trans h hyz⟩

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
  · exact S.sc_D_of_chr J (Relation.TransGen.single (S.tstep_tail hγ hγt ⟨ht.1, h⟩)) hy
  · rw [h]; exact hy

lemma temporalD_tstep {Θ : V → ℝ} (hΘ : (S.Dsp J).IsTemporal Θ) {x y : V} (h : S.TStep x y)
    (hy : y ∈ S.D J) : Θ x < Θ y := by
  obtain ⟨γ, hγ, h0, h1, hγt⟩ := h
  have hc : ContDiff ℝ 1 (Θ ∘ γ) := hΘ.1.comp hγ
  have hmono : StrictMonoOn (Θ ∘ γ) (Icc (0:ℝ) 1) := by
    refine strictMonoOn_of_deriv_pos (convex_Icc 0 1) hc.continuous.continuousOn fun t ht => ?_
    rw [interior_Icc] at ht
    have hti : t ∈ Icc (0:ℝ) 1 := Ioo_subset_Icc_self ht
    have hd : HasDerivAt (Θ ∘ γ) (fderiv ℝ Θ (γ t) (deriv γ t)) t :=
      ((hΘ.1.differentiable one_ne_zero) (γ t)).hasFDerivAt.comp_hasDerivAt t
        (hasDerivAt_of_contDiff hγ t)
    rw [hd.deriv]
    obtain ⟨-, h1', h2'⟩ := hγt t hti
    exact hΘ.2 _ (S.tstep_in_D J hγ hγt (h1 ▸ hy) hti) _ ⟨h1'.le, h2'⟩
  have := hmono ⟨le_rfl, zero_le_one⟩ ⟨zero_le_one, le_rfl⟩ zero_lt_one
  simpa [h0, h1] using this

/-- **A function temporal on `D` only increases along every `≪` ending in `D`.** -/
theorem sc_temporalD_chr {Θ : V → ℝ} (hΘ : (S.Dsp J).IsTemporal Θ) {x y : V} (h : S.Chr x y)
    (hy : y ∈ S.D J) : Θ x < Θ y := by
  induction h with
  | single h => exact S.temporalD_tstep J hΘ h hy
  | @tail b c hxb hbc ih =>
    have hb : b ∈ S.D J := S.sc_D_of_chr J (Relation.TransGen.single hbc) hy
    exact (ih hb).trans (S.temporalD_tstep J hΘ hbc hy)

/-! ### ① `Θ → ∞` at the horizon, from a properness hypothesis -/

/-- **Properness of `Θ` on `D`**: no sublevel set `{x ∈ D | Θ x ≤ T}` accumulates outside `D`
(equivalently, for continuous `Θ`, every sublevel set is closed in `V`: `sc_sublevelProper_iff`).
This is the content of "`Θ` is a Cauchy time function of `D` whose levels do not reach `∂D`". -/
def SublevelProper (Θ : V → ℝ) : Prop := ∀ T : ℝ, closure {x | x ∈ S.D J ∧ Θ x ≤ T} ⊆ S.D J

/-- For continuous `Θ`, properness is closedness of the sublevel sets `{x ∈ D | Θ x ≤ T}` in `V`. -/
theorem sc_sublevelProper_iff {Θ : V → ℝ} (hΘ : Continuous Θ) :
    S.SublevelProper J Θ ↔ ∀ T : ℝ, IsClosed {x | x ∈ S.D J ∧ Θ x ≤ T} := by
  constructor
  · intro h T
    refine isClosed_of_closure_subset fun x hx => ⟨h T hx, ?_⟩
    have : x ∈ closure (Θ ⁻¹' Iic T) := closure_mono (fun y hy => hy.2) hx
    rw [(isClosed_Iic.preimage hΘ).closure_eq] at this
    exact this
  · intro h T
    rw [(h T).closure_eq]
    exact fun x hx => hx.1

/-- `𝓗⁺ ∩ D = ∅`: a horizon point is not in `D`. -/
theorem sc_not_mem_D_of_H {p : V} (hp : p ∈ S.H J) : p ∉ S.D J := fun hpD =>
  hp.2 (interior_maximal (S.sc_D_subset_JpastSet J) (S.sc_D_open J) hpD)

/-- **`Θ → ∞` off `D`**: given properness, every `p ∉ D` and every `T` have a neighbourhood `U`
with `Θ > T` on `U ∩ D`. -/
theorem sc_blowup {Θ : V → ℝ} (hprop : S.SublevelProper J Θ) {p : V} (hp : p ∉ S.D J) (T : ℝ) :
    ∃ U ∈ 𝓝 p, ∀ x ∈ U ∩ S.D J, T < Θ x := by
  have hpc : p ∉ closure {x | x ∈ S.D J ∧ Θ x ≤ T} := fun h => hp (hprop T h)
  rw [mem_closure_iff_nhds] at hpc
  simp only [not_forall, not_nonempty_iff_eq_empty, exists_prop] at hpc
  obtain ⟨U, hU, hUe⟩ := hpc
  refine ⟨U, hU, fun x hx => lt_of_not_ge fun hle => ?_⟩
  have hmem : x ∈ U ∩ {x | x ∈ S.D J ∧ Θ x ≤ T} := ⟨hx.1, hx.2, hle⟩
  rw [hUe] at hmem
  exact hmem

/-- **① `Θ → ∞` at the horizon** (registered form): for `p ∈ 𝓗⁺` and every `T` there is a
neighbourhood `U` of `p` with `Θ > T` on `U ∩ D`. -/
theorem sc_blowup_H {Θ : V → ℝ} (hprop : S.SublevelProper J Θ) {p : V} (hp : p ∈ S.H J)
    (T : ℝ) : ∃ U ∈ 𝓝 p, ∀ x ∈ U ∩ S.D J, T < Θ x :=
  S.sc_blowup J hprop (S.sc_not_mem_D_of_H J hp) T

/-- ① in filter form: `Θ x → ∞` as `x → p` inside `D`, for every `p ∈ 𝓗⁺`. -/
theorem sc_tendsto_atTop_H {Θ : V → ℝ} (hprop : S.SublevelProper J Θ) {p : V}
    (hp : p ∈ S.H J) : Tendsto Θ (𝓝[S.D J] p) atTop := by
  rw [Filter.tendsto_atTop]
  intro T
  obtain ⟨U, hU, hUT⟩ := S.sc_blowup_H J hprop hp T
  rw [eventually_nhdsWithin_iff]
  filter_upwards [hU] with x hxU hxD
  exact (hUT x ⟨hxU, hxD⟩).le

/-- **Properness is exactly the blow-up**: `SublevelProper` holds iff `Θ x → ∞` as `x → p` inside
`D`, at every `p ∉ D`. So the hypothesis is not stronger than ① itself. -/
theorem sc_sublevelProper_iff_tendsto {Θ : V → ℝ} :
    S.SublevelProper J Θ ↔ ∀ p ∉ S.D J, Tendsto Θ (𝓝[S.D J] p) atTop := by
  constructor
  · intro hprop p hp
    rw [Filter.tendsto_atTop]
    intro T
    obtain ⟨U, hU, hUT⟩ := S.sc_blowup J hprop hp T
    rw [eventually_nhdsWithin_iff]
    filter_upwards [hU] with x hxU hxD
    exact (hUT x ⟨hxU, hxD⟩).le
  · intro h T q hq
    by_contra hqD
    have hev := (Filter.tendsto_atTop.1 (h q hqD)) (T + 1)
    rw [eventually_nhdsWithin_iff] at hev
    obtain ⟨x, hx, hxD, hxT⟩ := mem_closure_iff_nhds.1 hq _ hev
    linarith [hx hxD]

/-! ### ② The slice lower limit -/

/-- **Local connectedness of `D` at `p`**: arbitrarily small neighbourhoods `W` of `p` meet `D` in a
preconnected set (e.g. `D ∩ B` path-connected for small balls `B` around `p`). -/
def LocConnAt (p : V) : Prop := ∀ U ∈ 𝓝 p, ∃ W ∈ 𝓝 p, W ⊆ U ∧ IsPreconnected (W ∩ S.D J)

/-- **② Slice lower limit, pointwise.** If `p ∈ closure D \ D`, `D` is locally connected at `p`,
`Θ` is continuous on `D` and proper, then every neighbourhood of `p` meets `S_τ` for all large `τ`. -/
theorem sc_mem_KLi_slice {Θ : V → ℝ} (hcont : ContinuousOn Θ (S.D J))
    (hprop : S.SublevelProper J Θ) {p : V} (hpcl : p ∈ closure (S.D J)) (hpD : p ∉ S.D J)
    (hloc : S.LocConnAt J p) : p ∈ KLi (S.slice J Θ) := by
  intro U hU
  obtain ⟨W, hW, hWU, hWc⟩ := hloc U hU
  obtain ⟨x₀, hx₀W, hx₀D⟩ := mem_closure_iff_nhds.1 hpcl W hW
  filter_upwards [eventually_ge_atTop (Θ x₀)] with τ hτ
  obtain ⟨U', hU', hU'T⟩ := S.sc_blowup J hprop hpD τ
  obtain ⟨y, ⟨hyW, hyU'⟩, hyD⟩ := mem_closure_iff_nhds.1 hpcl _ (inter_mem hW hU')
  have hy : τ < Θ y := hU'T y ⟨hyU', hyD⟩
  obtain ⟨z, hz, hzτ⟩ := hWc.intermediate_value ⟨hx₀W, hx₀D⟩ ⟨hyW, hyD⟩
    (hcont.mono inter_subset_right) ⟨hτ, hy.le⟩
  exact ⟨z, ⟨hz.2, hzτ⟩, hWU hz.1⟩

/-- **② `𝓗⁺ ⊆ KLi(S_τ)`.** Hypotheses: `closure J⁻(𝒥⁺) ⊆ closure D` (campaign 72's `hcl`),
`Θ` continuous on `D`, `Θ` proper (`SublevelProper`), and `D` locally connected at every horizon
point. -/
theorem sc_slice_lower_limit (hcl : closure (S.JpastSet J) ⊆ closure (S.D J)) {Θ : V → ℝ}
    (hcont : ContinuousOn Θ (S.D J)) (hprop : S.SublevelProper J Θ)
    (hloc : ∀ p ∈ S.H J, S.LocConnAt J p) : S.H J ⊆ KLi (S.slice J Θ) := fun p hp =>
  S.sc_mem_KLi_slice J hcont hprop (hcl (frontier_subset_closure hp)) (S.sc_not_mem_D_of_H J hp)
    (hloc p hp)

/-- ② in the registered form: for `p ∈ 𝓗⁺`, a neighbourhood `U` and every `T` there is `τ ≥ T`
with `S_τ ∩ U ≠ ∅`. -/
theorem sc_slice_lower_limit_exists (hcl : closure (S.JpastSet J) ⊆ closure (S.D J))
    {Θ : V → ℝ} (hcont : ContinuousOn Θ (S.D J)) (hprop : S.SublevelProper J Θ)
    (hloc : ∀ p ∈ S.H J, S.LocConnAt J p) {p : V} (hp : p ∈ S.H J) {U : Set V} (hU : U ∈ 𝓝 p)
    (T : ℝ) : ∃ τ ≥ T, (S.slice J Θ τ ∩ U).Nonempty :=
  ((S.sc_slice_lower_limit J hcl hcont hprop hloc hp U hU).and (eventually_ge_atTop T)).exists.imp
    fun _ h => ⟨h.2, h.1⟩

/-- ② with sequences: `p = lim xₙ`, `xₙ ∈ S_{τₙ}`, `τₙ → ∞`. -/
theorem sc_slice_lower_limit_seq (hcl : closure (S.JpastSet J) ⊆ closure (S.D J))
    {Θ : V → ℝ} (hcont : ContinuousOn Θ (S.D J)) (hprop : S.SublevelProper J Θ)
    (hloc : ∀ p ∈ S.H J, S.LocConnAt J p) {p : V} (hp : p ∈ S.H J) :
    ∃ τ : ℕ → ℝ, ∃ x : ℕ → V, Tendsto τ atTop atTop ∧ Tendsto x atTop (𝓝 p) ∧
      ∀ n, x n ∈ S.slice J Θ (τ n) := by
  have h : ∀ n : ℕ, ∃ τ ≥ (n:ℝ), ∃ x ∈ S.slice J Θ τ, x ∈ ball p (1 / ((n:ℝ) + 1)) :=
    fun n => S.sc_slice_lower_limit_exists J hcl hcont hprop hloc hp
      (ball_mem_nhds p (by positivity)) n
  choose τ hτ x hx hxb using h
  refine ⟨τ, x, tendsto_atTop_mono hτ tendsto_natCast_atTop_atTop, ?_, hx⟩
  rw [tendsto_iff_dist_tendsto_zero]
  exact squeeze_zero (fun _ => dist_nonneg) (fun n => (mem_ball.1 (hxb n)).le)
    tendsto_one_div_add_atTop_nhds_zero_nat

/-! ### ③ The slices converge to `𝓗⁺` -/

section Slices
variable {S J} {O : ℝ → V} (hOD : S.IpastSet (range O) = S.D J)
include hOD

/-- **③ `KLi(S_τ) = KLs(S_τ) = 𝓗⁺`** for `Θ` adapted to the observer and increasing along `≪`
into the worldline (campaign 72's slice hypotheses), plus `hint`, `hcl`, continuity, properness
and local connectedness at `𝓗⁺`. -/
theorem sc_slice_kuratowski (hcl : closure (S.JpastSet J) ⊆ closure (S.D J))
    (hint : interior (S.JpastSet J) ⊆ S.D J) {Θ : V → ℝ} {c : ℝ}
    (hadapt : ∀ τ, Θ (O τ) = τ + c) (hΘ : ∀ x σ, S.Chr x (O σ) → Θ x < Θ (O σ))
    (hcont : ContinuousOn Θ (S.D J)) (hprop : S.SublevelProper J Θ)
    (hloc : ∀ p ∈ S.H J, S.LocConnAt J p) :
    KLi (S.slice J Θ) = S.H J ∧ KLs (S.slice J Θ) = S.H J := by
  have h1 := S.sc_slice_lower_limit J hcl hcont hprop hloc
  have h2 := (S.sc_slice_upper_limit hOD hadapt hΘ).2 hint
  have h3 := sc_KLi_subset_KLs (S.slice J Θ)
  exact ⟨(h3.trans h2).antisymm h1, h2.antisymm (h1.trans h3)⟩

/-- **③ in the paper's setting**: `Θ` temporal on `D` only (the restricted chart `Dsp`), adapted
to the observer along a future-directed worldline. The increase along `≪` is now derived (`sc_temporalD_chr`), not assumed. -/
theorem sc_slice_kuratowski_temporalD (hmono : ∀ s t : ℝ, s < t → S.Chr (O s) (O t))
    (hcl : closure (S.JpastSet J) ⊆ closure (S.D J))
    (hint : interior (S.JpastSet J) ⊆ S.D J) {Θ : V → ℝ} {c : ℝ}
    (hΘ : (S.Dsp J).IsTemporal Θ) (hadapt : ∀ τ, Θ (O τ) = τ + c)
    (hprop : S.SublevelProper J Θ) (hloc : ∀ p ∈ S.H J, S.LocConnAt J p) :
    KLi (S.slice J Θ) = S.H J ∧ KLs (S.slice J Θ) = S.H J := by
  exact S.sc_slice_kuratowski hOD hcl hint hadapt
    (fun x σ h => S.sc_temporalD_chr J hΘ h (S.sc_observer_mem_D hOD hmono σ))
    (hΘ.1.continuous.continuousOn) hprop hloc

end Slices


end Spacetime

#print axioms Spacetime.sc_isOpen_Ipast
#print axioms Spacetime.sc_chr_cau
#print axioms Spacetime.sc_chr_trans
#print axioms Spacetime.sc_cau_trans
#print axioms Spacetime.sc_Ipast_subset_Jpast
#print axioms Spacetime.sc_Ipast_subset_interior
#print axioms Spacetime.sc_temporal_chr
#print axioms Spacetime.sc_D_subset_JpastSet
#print axioms Spacetime.sc_Jpast_subset_JpastSet
#print axioms sc_KLi_subset_KLs
#print axioms sc_preconnected_inter_frontier
#print axioms Spacetime.sc_Ipast_mono
#print axioms Spacetime.sc_observer_mem_D
#print axioms Spacetime.sc_D_eventually
#print axioms Spacetime.sc_interior_cone_subset
#print axioms Spacetime.sc_lower_limit
#print axioms Spacetime.sc_lower_limit_exists
#print axioms Spacetime.sc_lower_limit_seq
#print axioms Spacetime.sc_upper_limit_closure_diff
#print axioms Spacetime.sc_upper_limit
#print axioms sc_mem_KLs_of_seq
#print axioms Spacetime.sc_upper_limit_seq
#print axioms Spacetime.sc_kuratowski
#print axioms Spacetime.sc_H_eq_closure_diff
#print axioms Spacetime.sc_slice_upper_limit
#print axioms Spacetime.sc_slice_upper_limit_temporal
#print axioms Spacetime.sc_slice_upper_limit_seq

#print axioms Spacetime.sc_Ipast_subset_M
#print axioms Spacetime.sc_D_open
#print axioms Spacetime.sc_D_subset_M
#print axioms Spacetime.sc_D_of_chr
#print axioms Spacetime.sc_temporalD_chr
#print axioms Spacetime.sc_sublevelProper_iff
#print axioms Spacetime.sc_not_mem_D_of_H
#print axioms Spacetime.sc_blowup
#print axioms Spacetime.sc_blowup_H
#print axioms Spacetime.sc_tendsto_atTop_H
#print axioms Spacetime.sc_sublevelProper_iff_tendsto
#print axioms Spacetime.sc_mem_KLi_slice
#print axioms Spacetime.sc_slice_lower_limit
#print axioms Spacetime.sc_slice_lower_limit_exists
#print axioms Spacetime.sc_slice_lower_limit_seq
#print axioms Spacetime.sc_slice_kuratowski
#print axioms Spacetime.sc_slice_kuratowski_temporalD

end ShadowProbe.SliceConvergenceProbe

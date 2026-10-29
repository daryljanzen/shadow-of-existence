import Mathlib

/-!
# Probe `r7635+71.2` (campaign 72, `r7635` ②): the convergence `∂J⁻(O(τ)) → 𝓗⁺` and the tangency
# clause of `prop:causal-alignment` in Kuratowski form

Source: `corpus/BH_causality_v2.tex`, `prop:causal-alignment` (lines 300–313).
Registration: `computations/formalisation/r7635_71_campaign72/PREDICTION.md`. Nothing imports this
file, and it imports no other probe.

## Setting

Campaign 60's single-chart `Spacetime V` (`probes/CausalStructure.lean`), copied verbatim under this
namespace with every theorem renamed `hc_…`: open `M`, continuous symmetric `g`, continuous time
orientation `T`; `≪` (`Chr`) is the transitive closure of `C¹` timelike steps, `≤` (`Cau`) the
reflexive-transitive closure of `C¹` causal steps. `𝒥⁺ = J` is an arbitrary set,
`D = I⁻(J)`, `𝓗⁺ = H = frontier J⁻(J)`.

The observer `O : ℝ → V` satisfies
* `hOD : I⁻(range O) = D` (the paper's `I⁻(O) = D`), and
* `hmono : s < t → O s ≪ O t` (future-directed worldline; taken, not derived).

## What is used, and what is not

* **No push-up and no Lipschitz hypothesis.** The lower limit only needs `p ∉ int J⁻(O τ)`, which
  follows from `J⁻(O τ) ⊆ J⁻(J)` (transitivity) and `p ∉ int J⁻(J)`; when `p ∈ J⁻(O τ)` the point
  `p` itself is on `∂J⁻(O τ)`.
* **No convexity of `M`.** The connected set joining `x ∈ D` to `p` is a ball of `V` around `p`; the
  frontier is taken in `V`, so the ball need not lie in `M`.
* Stated hypotheses:
  - `hcl : closure J⁻(J) ⊆ closure D` (the paper's `closure J⁻(𝒥⁺) = closure D`) — lower limit;
  - `hint : interior J⁻(J) ⊆ D` (`int J⁻ = I⁻`) — upper limit. For the Lipschitz relation this is
    campaign 63's `cr_interior_JpastL_subset`; for the `C¹`-chain relation used here it is stated.
    Without it the upper limit is proved into `closure J⁻(J) \ D`.

## Kuratowski limits (as `τ → ∞`)

* `KLi A = {p | ∀ U ∈ 𝓝 p, ∀ᶠ τ in atTop, (A τ ∩ U).Nonempty}` (lower limit),
* `KLs A = {p | ∀ U ∈ 𝓝 p, ∃ᶠ τ in atTop, (A τ ∩ U).Nonempty}` (upper limit).
`A` converges to `L` in the Kuratowski sense iff `KLi A = L = KLs A`.

## Scope of the tangency clause

What is proved is the set-convergence (Kuratowski) form of "`∂J⁻(O τ)` converges to `𝓗⁺`" and the
upper-limit form of "the slices `S_τ` accumulate on `𝓗⁺`". The differential form ("tangent hyperplanes
asymptotically tangent to the generators") needs the generators' regularity (campaign 71) and is not
attempted. The slice *lower* limit (`𝓗⁺ ⊆ KLi S_τ`) needs `Θ → ∞` on approach to `𝓗⁺` together with
an intermediate-value argument across levels, i.e. the Cauchy property of `Θ` on `D`; it is not
attempted.
-/

open Set Filter Topology Metric

namespace ShadowProbe.HorizonConvergenceProbe

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
theorem hc_isOpen_Ipast (p : V) : IsOpen (S.Ipast p) := by
  refine isOpen_iff_mem_nhds.2 fun q hq => ?_
  obtain ⟨y, hqy, hyp⟩ := Relation.TransGen.head'_iff.1 hq
  filter_upwards [S.tstep_start_eventually hqy] with q' hq'
  exact Relation.TransGen.head' hq' hyp

lemma tstep_to_cstep {x y : V} (h : S.TStep x y) : S.CStep x y := by
  obtain ⟨γ, hγ, h0, h1, hγt⟩ := h
  exact ⟨γ, hγ, h0, h1, fun t ht => ⟨(hγt t ht).1, (hγt t ht).2.1.le, (hγt t ht).2.2⟩⟩

/-- `≪ ⊆ ≤`. -/
theorem hc_chr_cau {x y : V} (h : S.Chr x y) : S.Cau x y := by
  induction h with
  | single h => exact Relation.ReflTransGen.single (S.tstep_to_cstep h)
  | tail _ h ih => exact ih.tail (S.tstep_to_cstep h)

theorem hc_chr_trans {x y z : V} (h1 : S.Chr x y) (h2 : S.Chr y z) : S.Chr x z :=
  Relation.TransGen.trans h1 h2

theorem hc_cau_trans {x y z : V} (h1 : S.Cau x y) (h2 : S.Cau y z) : S.Cau x z :=
  Relation.ReflTransGen.trans h1 h2

theorem hc_Ipast_subset_Jpast (p : V) : S.Ipast p ⊆ S.Jpast p := fun _ h => S.hc_chr_cau h

/-- `I⁻(p) ⊆ int J⁻(p)`. -/
theorem hc_Ipast_subset_interior (p : V) : S.Ipast p ⊆ interior (S.Jpast p) :=
  interior_maximal (S.hc_Ipast_subset_Jpast p) (S.hc_isOpen_Ipast p)

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
theorem hc_temporal_chr {τ : V → ℝ} (hτ : S.IsTemporal τ) {x y : V} (h : S.Chr x y) :
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

theorem hc_D_subset_JpastSet : S.D J ⊆ S.JpastSet J :=
  biUnion_mono subset_rfl fun p _ => S.hc_Ipast_subset_Jpast p

/-- `p ∈ D ⟹ J⁻(p) ⊆ J⁻(𝒥⁺)` (transitivity only). -/
theorem hc_Jpast_subset_JpastSet {p : V} (hp : p ∈ S.D J) : S.Jpast p ⊆ S.JpastSet J := by
  intro q hq
  simp only [D, IpastSet, JpastSet, mem_iUnion] at hp ⊢
  obtain ⟨z, hz, hpz⟩ := hp
  exact ⟨z, hz, S.hc_cau_trans hq (S.hc_chr_cau hpz)⟩

/-! ### Kuratowski limits as `τ → ∞` -/

end Spacetime

/-- Kuratowski lower limit of a family of sets as `τ → ∞`. -/
def KLi (A : ℝ → Set V) : Set V := {p | ∀ U ∈ 𝓝 p, ∀ᶠ τ in atTop, (A τ ∩ U).Nonempty}
/-- Kuratowski upper limit of a family of sets as `τ → ∞`. -/
def KLs (A : ℝ → Set V) : Set V := {p | ∀ U ∈ 𝓝 p, ∃ᶠ τ in atTop, (A τ ∩ U).Nonempty}

omit [NormedSpace ℝ V] in
/-- `Li ⊆ Ls`. -/
theorem hc_KLi_subset_KLs (A : ℝ → Set V) : KLi A ⊆ KLs A :=
  fun _ hp U hU => (hp U hU).frequently

omit [NormedSpace ℝ V] in
/-- A preconnected set that meets `A` at `a` and contains a point `p ∉ int A` meets `∂A`. -/
theorem hc_preconnected_inter_frontier {C A : Set V} (hC : IsPreconnected C) {a p : V}
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
theorem hc_mem_KLs_of_seq {A : ℝ → Set V} {τ : ℕ → ℝ} {y : ℕ → V} {y₀ : V}
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
theorem hc_Ipast_mono {σ τ : ℝ} (h : σ ≤ τ) : S.Ipast (O σ) ⊆ S.Ipast (O τ) := by
  rcases h.lt_or_eq with h | h
  · exact fun q hq => S.hc_chr_trans hq (hmono σ τ h)
  · rw [h]

/-- Each `O τ` lies in `D`. -/
theorem hc_observer_mem_D (τ : ℝ) : O τ ∈ S.D J := by
  rw [← hOD]
  exact mem_biUnion (mem_range_self (τ + 1)) (hmono τ (τ + 1) (by linarith))

/-- `x ∈ D ⟹ x ∈ I⁻(O τ)` for all large `τ`. -/
theorem hc_D_eventually {x : V} (hx : x ∈ S.D J) : ∀ᶠ τ in atTop, x ∈ S.Ipast (O τ) := by
  rw [← hOD] at hx
  simp only [IpastSet, mem_iUnion] at hx
  obtain ⟨_, ⟨σ, rfl⟩, hσ⟩ := hx
  filter_upwards [eventually_ge_atTop σ] with τ hτ
  exact S.hc_Ipast_mono hmono hτ hσ

/-- `J⁻(O τ) ⊆ J⁻(𝒥⁺)`, hence `int J⁻(O τ) ⊆ int J⁻(𝒥⁺)`. -/
theorem hc_interior_cone_subset (τ : ℝ) :
    interior (S.Jpast (O τ)) ⊆ interior (S.JpastSet J) :=
  interior_mono (S.hc_Jpast_subset_JpastSet J (S.hc_observer_mem_D hOD hmono τ))

/-! ### ① The lower limit -/

/-- **Lower limit** `𝓗⁺ ⊆ Li ∂J⁻(O τ)`: every horizon point `p` is approached, for *every* large
`τ`, by points of `∂J⁻(O τ)`. Hypothesis: `closure J⁻(𝒥⁺) ⊆ closure D`. -/
theorem hc_lower_limit (hcl : closure (S.JpastSet J) ⊆ closure (S.D J)) :
    S.H J ⊆ KLi (S.cone O) := by
  intro p hp U hU
  obtain ⟨ε, hε, hεU⟩ := Metric.mem_nhds_iff.1 hU
  have hpD : p ∈ closure (S.D J) := hcl (frontier_subset_closure hp)
  obtain ⟨x, hxD, hxb⟩ : ∃ x ∈ S.D J, x ∈ ball p ε := by
    obtain ⟨x, hx, hxb⟩ := Metric.mem_closure_iff.1 hpD ε hε
    exact ⟨x, hx, by rw [mem_ball, dist_comm]; exact hxb⟩
  filter_upwards [S.hc_D_eventually hOD hmono hxD] with τ hτ
  have hpi : p ∉ interior (S.Jpast (O τ)) :=
    fun h => hp.2 (S.hc_interior_cone_subset hOD hmono τ h)
  obtain ⟨y, hyb, hyf⟩ := hc_preconnected_inter_frontier isPreconnected_ball
    ⟨hxb, S.hc_Ipast_subset_Jpast _ hτ⟩ (mem_ball_self hε) hpi
  exact ⟨y, hyf, hεU hyb⟩

/-- The lower limit in the registered form: for every neighbourhood `U` of `p ∈ 𝓗⁺` and every `T`
there is `τ ≥ T` with `∂J⁻(O τ) ∩ U ≠ ∅`. -/
theorem hc_lower_limit_exists (hcl : closure (S.JpastSet J) ⊆ closure (S.D J)) {p : V}
    (hp : p ∈ S.H J) {U : Set V} (hU : U ∈ 𝓝 p) (T : ℝ) :
    ∃ τ ≥ T, (frontier (S.Jpast (O τ)) ∩ U).Nonempty :=
  ((S.hc_lower_limit hOD hmono hcl hp U hU).and (eventually_ge_atTop T)).exists.imp
    fun _ h => ⟨h.2, h.1⟩

/-- The lower limit with sequences: `p = lim yₙ`, `yₙ ∈ ∂J⁻(O τₙ)`, `τₙ → ∞`. -/
theorem hc_lower_limit_seq (hcl : closure (S.JpastSet J) ⊆ closure (S.D J)) {p : V}
    (hp : p ∈ S.H J) :
    ∃ τ : ℕ → ℝ, ∃ y : ℕ → V, Tendsto τ atTop atTop ∧ Tendsto y atTop (𝓝 p) ∧
      ∀ n, y n ∈ frontier (S.Jpast (O (τ n))) := by
  have h : ∀ n : ℕ, ∃ τ ≥ (n:ℝ), ∃ y ∈ frontier (S.Jpast (O τ)), y ∈ ball p (1 / ((n:ℝ) + 1)) :=
    fun n => S.hc_lower_limit_exists hOD hmono hcl hp (ball_mem_nhds p (by positivity)) n
  choose τ hτ y hy hyb using h
  refine ⟨τ, y, tendsto_atTop_mono hτ tendsto_natCast_atTop_atTop, ?_, hy⟩
  rw [tendsto_iff_dist_tendsto_zero]
  refine squeeze_zero (fun _ => dist_nonneg) (fun n => (mem_ball.1 (hyb n)).le)
    tendsto_one_div_add_atTop_nhds_zero_nat

/-! ### ② The upper limit -/

/-- **Upper limit, unconditional part** `Ls ∂J⁻(O τ) ⊆ closure J⁻(𝒥⁺) \ D`. -/
theorem hc_upper_limit_closure_diff :
    KLs (S.cone O) ⊆ closure (S.JpastSet J) \ S.D J := by
  intro y hy
  refine ⟨?_, fun hyD => ?_⟩
  · rw [mem_closure_iff_nhds]
    intro U hU
    obtain ⟨W, hWU, hWo, hyW⟩ := _root_.mem_nhds_iff.1 hU
    obtain ⟨τ, z, hzf, hzW⟩ := (hy W (hWo.mem_nhds hyW)).exists
    obtain ⟨w, hwW, hwJ⟩ := mem_closure_iff.1 (frontier_subset_closure hzf) W hWo hzW
    exact ⟨w, hWU hwW, S.hc_Jpast_subset_JpastSet J (S.hc_observer_mem_D hOD hmono τ) hwJ⟩
  · rw [← hOD] at hyD
    simp only [IpastSet, mem_iUnion] at hyD
    obtain ⟨_, ⟨σ, rfl⟩, hσ⟩ := hyD
    have hfr := hy _ ((S.hc_isOpen_Ipast (O σ)).mem_nhds hσ)
    obtain ⟨τ, hτσ, z, hzf, hzI⟩ := frequently_atTop.1 hfr σ
    exact hzf.2 (S.hc_Ipast_subset_interior _ (S.hc_Ipast_mono hmono hτσ hzI))

/-- **Upper limit** `Ls ∂J⁻(O τ) ⊆ 𝓗⁺`, given `int J⁻(𝒥⁺) ⊆ D`. -/
theorem hc_upper_limit (hint : interior (S.JpastSet J) ⊆ S.D J) :
    KLs (S.cone O) ⊆ S.H J := by
  intro y hy
  obtain ⟨h1, h2⟩ := S.hc_upper_limit_closure_diff hOD hmono hy
  exact ⟨h1, fun hi => h2 (hint hi)⟩

/-- **Upper limit with sequences**: `yₙ ∈ ∂J⁻(O τₙ)`, `τₙ → ∞`, `yₙ → y` give `y ∈ 𝓗⁺`. -/
theorem hc_upper_limit_seq (hint : interior (S.JpastSet J) ⊆ S.D J) {τ : ℕ → ℝ} {y : ℕ → V}
    {y₀ : V} (hτ : Tendsto τ atTop atTop) (hy : Tendsto y atTop (𝓝 y₀))
    (hA : ∀ n, y n ∈ frontier (S.Jpast (O (τ n)))) : y₀ ∈ S.H J :=
  S.hc_upper_limit hOD hmono hint (hc_mem_KLs_of_seq (A := S.cone O) hτ hy hA)

/-! ### ③ The clause in Kuratowski form -/

/-- **`∂J⁻(O τ) → 𝓗⁺` in the Kuratowski sense** as `τ → ∞`. -/
theorem hc_kuratowski (hcl : closure (S.JpastSet J) ⊆ closure (S.D J))
    (hint : interior (S.JpastSet J) ⊆ S.D J) :
    KLi (S.cone O) = S.H J ∧ KLs (S.cone O) = S.H J := by
  have h1 := S.hc_lower_limit hOD hmono hcl
  have h2 := S.hc_upper_limit hOD hmono hint
  have h3 := hc_KLi_subset_KLs (S.cone O)
  exact ⟨(h3.trans h2).antisymm h1, h2.antisymm (h1.trans h3)⟩

omit hOD hmono in
/-- Under the two hypotheses, `𝓗⁺ = closure D \ D`. -/
theorem hc_H_eq_closure_diff (hcl : closure (S.JpastSet J) ⊆ closure (S.D J))
    (hint : interior (S.JpastSet J) ⊆ S.D J) :
    S.H J = closure (S.D J) \ S.D J := by
  ext p
  constructor
  · intro hp
    refine ⟨hcl (frontier_subset_closure hp), fun hpD => hp.2 ?_⟩
    exact interior_maximal (S.hc_D_subset_JpastSet J)
      (isOpen_biUnion fun z _ => S.hc_isOpen_Ipast z) hpD
  · rintro ⟨h1, h2⟩
    exact ⟨closure_mono (S.hc_D_subset_JpastSet J) h1, fun hi => h2 (hint hi)⟩

/-! ### The slices `S_τ` accumulate on `𝓗⁺` -/

omit hmono in
/-- **Slices, upper limit.** Adapted `Θ`: `Θ (O τ) = τ + c`, and `Θ` increases along every `≪`
ending on the worldline. Then `Ls S_τ ⊆ closure J⁻(𝒥⁺) \ D`, and `⊆ 𝓗⁺` given `int J⁻(𝒥⁺) ⊆ D`. -/
theorem hc_slice_upper_limit {Θ : V → ℝ} {c : ℝ} (hadapt : ∀ τ, Θ (O τ) = τ + c)
    (hΘ : ∀ x σ, S.Chr x (O σ) → Θ x < Θ (O σ)) :
    KLs (S.slice J Θ) ⊆ closure (S.JpastSet J) \ S.D J ∧
    (interior (S.JpastSet J) ⊆ S.D J → KLs (S.slice J Θ) ⊆ S.H J) := by
  have key : KLs (S.slice J Θ) ⊆ closure (S.JpastSet J) \ S.D J := by
    intro y hy
    refine ⟨?_, fun hyD => ?_⟩
    · rw [mem_closure_iff_nhds]
      intro U hU
      obtain ⟨τ, z, hz, hzU⟩ := (hy U hU).exists
      exact ⟨z, hzU, S.hc_D_subset_JpastSet J hz.1⟩
    · rw [← hOD] at hyD
      simp only [IpastSet, mem_iUnion] at hyD
      obtain ⟨_, ⟨σ, rfl⟩, hσ⟩ := hyD
      have hfr := hy _ ((S.hc_isOpen_Ipast (O σ)).mem_nhds hσ)
      obtain ⟨τ, hτ, z, hz, hzI⟩ := frequently_atTop.1 hfr (σ + c)
      have := hΘ z σ hzI
      rw [hadapt, hz.2] at this
      linarith
  refine ⟨key, fun hint y hy => ?_⟩
  obtain ⟨h1, h2⟩ := key hy
  exact ⟨h1, fun hi => h2 (hint hi)⟩

omit hmono in
/-- Slices, upper limit, for a temporal `Θ` on `M` adapted to `O`. -/
theorem hc_slice_upper_limit_temporal (hint : interior (S.JpastSet J) ⊆ S.D J) {Θ : V → ℝ}
    {c : ℝ} (hΘ : S.IsTemporal Θ) (hadapt : ∀ τ, Θ (O τ) = τ + c) :
    KLs (S.slice J Θ) ⊆ S.H J :=
  (S.hc_slice_upper_limit hOD hadapt fun _ _ h => S.hc_temporal_chr hΘ h).2 hint

omit hmono in
/-- Slices with sequences: `xₙ ∈ S_{τₙ}`, `τₙ → ∞`, `xₙ → x` give `x ∈ 𝓗⁺`. -/
theorem hc_slice_upper_limit_seq (hint : interior (S.JpastSet J) ⊆ S.D J) {Θ : V → ℝ}
    {c : ℝ} (hadapt : ∀ τ, Θ (O τ) = τ + c) (hΘ : ∀ x σ, S.Chr x (O σ) → Θ x < Θ (O σ))
    {τ : ℕ → ℝ} {x : ℕ → V} {x₀ : V} (hτ : Tendsto τ atTop atTop)
    (hx : Tendsto x atTop (𝓝 x₀)) (hA : ∀ n, x n ∈ S.slice J Θ (τ n)) : x₀ ∈ S.H J :=
  (S.hc_slice_upper_limit hOD hadapt hΘ).2 hint (hc_mem_KLs_of_seq hτ hx hA)

end Observer

end Spacetime

#print axioms Spacetime.hc_isOpen_Ipast
#print axioms Spacetime.hc_chr_cau
#print axioms Spacetime.hc_chr_trans
#print axioms Spacetime.hc_cau_trans
#print axioms Spacetime.hc_Ipast_subset_Jpast
#print axioms Spacetime.hc_Ipast_subset_interior
#print axioms Spacetime.hc_temporal_chr
#print axioms Spacetime.hc_D_subset_JpastSet
#print axioms Spacetime.hc_Jpast_subset_JpastSet
#print axioms hc_KLi_subset_KLs
#print axioms hc_preconnected_inter_frontier
#print axioms Spacetime.hc_Ipast_mono
#print axioms Spacetime.hc_observer_mem_D
#print axioms Spacetime.hc_D_eventually
#print axioms Spacetime.hc_interior_cone_subset
#print axioms Spacetime.hc_lower_limit
#print axioms Spacetime.hc_lower_limit_exists
#print axioms Spacetime.hc_lower_limit_seq
#print axioms Spacetime.hc_upper_limit_closure_diff
#print axioms Spacetime.hc_upper_limit
#print axioms hc_mem_KLs_of_seq
#print axioms Spacetime.hc_upper_limit_seq
#print axioms Spacetime.hc_kuratowski
#print axioms Spacetime.hc_H_eq_closure_diff
#print axioms Spacetime.hc_slice_upper_limit
#print axioms Spacetime.hc_slice_upper_limit_temporal
#print axioms Spacetime.hc_slice_upper_limit_seq

end ShadowProbe.HorizonConvergenceProbe

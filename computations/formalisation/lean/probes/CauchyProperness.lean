import Mathlib

/-!
# Probe `r7639+71.1` (campaign 75, `r7639` ①): does `prop:causal-alignment` need properness?

Registration: `computations/formalisation/r7639_71_campaign75/PREDICTION.md`. Nothing imports this
file, and it imports no other probe.

## Copied

From campaign 74's `probes/SliceConvergence.lean`, renamed `sc_… ↦ cp_…`: the chart `Spacetime`,
`≪`/`≤`, `I⁻`, `J⁻`, openness of `I⁻(p)`, temporal functions, `D`, `𝓗⁺ = H`, `slice`, `KLi`,
`KLs`, the observer lemmas, the slice upper limit and `cp_H_eq_closure_diff` (campaign 72's
`HorizonConvergence.lean` through it), campaign 60's `restrict`, `InextCausalCurve`,
`IsCauchyTemporal`, `Dsp`, `ExteriorGH` (`CausalStructure.lean` through it), and campaign 74's
`cp_temporalD_chr`, `SublevelProper`, `cp_sublevelProper_iff(_tendsto)`, `cp_blowup(_H)`. Campaign
74's cone limits and its `LocConnAt`-based slice lower limit are not copied (superseded here).

## New (campaign 75)

1. `cp_isOpen_Ifut`: `I⁺(x)` is open. `cp_Ipast_subset_D`: `q ∈ closure D ⟹ I⁻(q) ⊆ D`.
2. `cp_curve`: for `q ∈ M ∩ closure D \ D`, `γ t = q - ε e^{-t} T(q)` (`t ≥ 0`) is a
   future-inextendible causal curve of `D` with `γ t → q`, `γ t ≪ q`, `γ t ≪ γ t'`.
3. **Cauchy form used: the future-inextendible form** `FutCauchyTemporal` (on `Dsp`): `Θ` temporal,
   and every future-inextendible piecewise-`C¹` causal curve `[0,∞) → D` attains every level
   `≥ Θ(γ 0)`. *This is a substitution* for campaign 60's two-sided `IsCauchyTemporal` (whose
   curves are on all of `ℝ` and inextendible in both directions; extending our curve into the past
   without a past endpoint in `D` was judged heavy, the registered "reachable negative"). The two
   are equivalent in the standard theory (a future-inextendible causal curve extends to an
   inextendible one); **that equivalence is not formalised**.
4. `cp_blowup_cauchy`, `cp_tendsto_atTop_H_cauchy`, `cp_sublevelProper`: properness is **derived**.
5. `cp_mem_KLi_slice`, `cp_slice_lower_limit(_seq)`: `𝓗⁺ ⊆ KLi(S_τ)` with no `SublevelProper` and
   no `LocConnAt` (the tail of the curve in `U` hits every large level, by the Cauchy property and
   monotonicity of `Θ` along `≪` — no intermediate value theorem is even needed).
6. `cp_slice_kuratowski`, `cp_causal_alignment`: `KLi(S_τ) = KLs(S_τ) = 𝓗⁺` (and properness).

One extra hypothesis appears: `hHM : 𝓗⁺ ⊆ M`. Frontiers are taken in the chart `V`, so a horizon
point could a priori lie on `∂M`, where `g` need not be Lorentzian; in the paper `𝓗⁺ ⊆ M`.

## Campaign 74's Schwarzschild example is withdrawn

Any spacetime containing the bifurcation sphere contains points of the white-hole region IV near
it; these lie in `D = I⁻(𝒥⁺)`, where Schwarzschild `t` is not temporal. So that example is outside
the proposition's hypotheses (no Lean for this remark).
-/
open Set Filter Topology Metric

namespace ShadowProbe.CauchyPropernessProbe

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
theorem cp_isOpen_Ipast (p : V) : IsOpen (S.Ipast p) := by
  refine isOpen_iff_mem_nhds.2 fun q hq => ?_
  obtain ⟨y, hqy, hyp⟩ := Relation.TransGen.head'_iff.1 hq
  filter_upwards [S.tstep_start_eventually hqy] with q' hq'
  exact Relation.TransGen.head' hq' hyp

lemma tstep_to_cstep {x y : V} (h : S.TStep x y) : S.CStep x y := by
  obtain ⟨γ, hγ, h0, h1, hγt⟩ := h
  exact ⟨γ, hγ, h0, h1, fun t ht => ⟨(hγt t ht).1, (hγt t ht).2.1.le, (hγt t ht).2.2⟩⟩

/-- `≪ ⊆ ≤`. -/
theorem cp_chr_cau {x y : V} (h : S.Chr x y) : S.Cau x y := by
  induction h with
  | single h => exact Relation.ReflTransGen.single (S.tstep_to_cstep h)
  | tail _ h ih => exact ih.tail (S.tstep_to_cstep h)

theorem cp_chr_trans {x y z : V} (h1 : S.Chr x y) (h2 : S.Chr y z) : S.Chr x z :=
  Relation.TransGen.trans h1 h2

theorem cp_cau_trans {x y z : V} (h1 : S.Cau x y) (h2 : S.Cau y z) : S.Cau x z :=
  Relation.ReflTransGen.trans h1 h2

theorem cp_Ipast_subset_Jpast (p : V) : S.Ipast p ⊆ S.Jpast p := fun _ h => S.cp_chr_cau h

/-- `I⁻(p) ⊆ int J⁻(p)`. -/
theorem cp_Ipast_subset_interior (p : V) : S.Ipast p ⊆ interior (S.Jpast p) :=
  interior_maximal (S.cp_Ipast_subset_Jpast p) (S.cp_isOpen_Ipast p)

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
theorem cp_temporal_chr {τ : V → ℝ} (hτ : S.IsTemporal τ) {x y : V} (h : S.Chr x y) :
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

theorem cp_D_subset_JpastSet : S.D J ⊆ S.JpastSet J :=
  biUnion_mono subset_rfl fun p _ => S.cp_Ipast_subset_Jpast p

/-- `p ∈ D ⟹ J⁻(p) ⊆ J⁻(𝒥⁺)` (transitivity only). -/
theorem cp_Jpast_subset_JpastSet {p : V} (hp : p ∈ S.D J) : S.Jpast p ⊆ S.JpastSet J := by
  intro q hq
  simp only [D, IpastSet, JpastSet, mem_iUnion] at hp ⊢
  obtain ⟨z, hz, hpz⟩ := hp
  exact ⟨z, hz, S.cp_cau_trans hq (S.cp_chr_cau hpz)⟩


end Spacetime

/-- Kuratowski lower limit of a family of sets as `τ → ∞`. -/
def KLi (A : ℝ → Set V) : Set V := {p | ∀ U ∈ 𝓝 p, ∀ᶠ τ in atTop, (A τ ∩ U).Nonempty}
/-- Kuratowski upper limit of a family of sets as `τ → ∞`. -/
def KLs (A : ℝ → Set V) : Set V := {p | ∀ U ∈ 𝓝 p, ∃ᶠ τ in atTop, (A τ ∩ U).Nonempty}

omit [NormedSpace ℝ V] in
/-- `Li ⊆ Ls`. -/
theorem cp_KLi_subset_KLs (A : ℝ → Set V) : KLi A ⊆ KLs A :=
  fun _ hp U hU => (hp U hU).frequently


omit [NormedSpace ℝ V] in
/-- Membership in `Ls` from a sequence: `yₙ ∈ A τₙ`, `τₙ → ∞`, `yₙ → y` give `y ∈ Ls A`. -/
theorem cp_mem_KLs_of_seq {A : ℝ → Set V} {τ : ℕ → ℝ} {y : ℕ → V} {y₀ : V}
    (hτ : Tendsto τ atTop atTop) (hy : Tendsto y atTop (𝓝 y₀)) (hA : ∀ n, y n ∈ A (τ n)) :
    y₀ ∈ KLs A := by
  intro U hU
  rw [frequently_atTop]
  intro T
  obtain ⟨n, hn1, hn2⟩ := ((hy.eventually hU).and (hτ.eventually_ge_atTop T)).exists
  exact ⟨τ n, hn2, y n, hA n, hn1⟩

namespace Spacetime
variable (S : Spacetime V) (J : Set V)

section Observer
variable {S J} {O : ℝ → V} (hOD : S.IpastSet (range O) = S.D J)
  (hmono : ∀ s t : ℝ, s < t → S.Chr (O s) (O t))
include hOD hmono

omit hOD in
/-- `I⁻(O σ) ⊆ I⁻(O τ)` for `σ ≤ τ`. -/
theorem cp_Ipast_mono {σ τ : ℝ} (h : σ ≤ τ) : S.Ipast (O σ) ⊆ S.Ipast (O τ) := by
  rcases h.lt_or_eq with h | h
  · exact fun q hq => S.cp_chr_trans hq (hmono σ τ h)
  · rw [h]

/-- Each `O τ` lies in `D`. -/
theorem cp_observer_mem_D (τ : ℝ) : O τ ∈ S.D J := by
  rw [← hOD]
  exact mem_biUnion (mem_range_self (τ + 1)) (hmono τ (τ + 1) (by linarith))

/-- `x ∈ D ⟹ x ∈ I⁻(O τ)` for all large `τ`. -/
theorem cp_D_eventually {x : V} (hx : x ∈ S.D J) : ∀ᶠ τ in atTop, x ∈ S.Ipast (O τ) := by
  rw [← hOD] at hx
  simp only [IpastSet, mem_iUnion] at hx
  obtain ⟨_, ⟨σ, rfl⟩, hσ⟩ := hx
  filter_upwards [eventually_ge_atTop σ] with τ hτ
  exact S.cp_Ipast_mono hmono hτ hσ

omit hOD hmono in
/-- Under the two hypotheses, `𝓗⁺ = closure D \ D`. -/
theorem cp_H_eq_closure_diff (hcl : closure (S.JpastSet J) ⊆ closure (S.D J))
    (hint : interior (S.JpastSet J) ⊆ S.D J) :
    S.H J = closure (S.D J) \ S.D J := by
  ext p
  constructor
  · intro hp
    refine ⟨hcl (frontier_subset_closure hp), fun hpD => hp.2 ?_⟩
    exact interior_maximal (S.cp_D_subset_JpastSet J)
      (isOpen_biUnion fun z _ => S.cp_isOpen_Ipast z) hpD
  · rintro ⟨h1, h2⟩
    exact ⟨closure_mono (S.cp_D_subset_JpastSet J) h1, fun hi => h2 (hint hi)⟩

/-! ### The slices `S_τ` accumulate on `𝓗⁺` -/

omit hmono in
/-- **Slices, upper limit.** Adapted `Θ`: `Θ (O τ) = τ + c`, and `Θ` increases along every `≪`
ending on the worldline. Then `Ls S_τ ⊆ closure J⁻(𝒥⁺) \ D`, and `⊆ 𝓗⁺` given `int J⁻(𝒥⁺) ⊆ D`. -/
theorem cp_slice_upper_limit {Θ : V → ℝ} {c : ℝ} (hadapt : ∀ τ, Θ (O τ) = τ + c)
    (hΘ : ∀ x σ, S.Chr x (O σ) → Θ x < Θ (O σ)) :
    KLs (S.slice J Θ) ⊆ closure (S.JpastSet J) \ S.D J ∧
    (interior (S.JpastSet J) ⊆ S.D J → KLs (S.slice J Θ) ⊆ S.H J) := by
  have key : KLs (S.slice J Θ) ⊆ closure (S.JpastSet J) \ S.D J := by
    intro y hy
    refine ⟨?_, fun hyD => ?_⟩
    · rw [mem_closure_iff_nhds]
      intro U hU
      obtain ⟨τ, z, hz, hzU⟩ := (hy U hU).exists
      exact ⟨z, hzU, S.cp_D_subset_JpastSet J hz.1⟩
    · rw [← hOD] at hyD
      simp only [IpastSet, mem_iUnion] at hyD
      obtain ⟨_, ⟨σ, rfl⟩, hσ⟩ := hyD
      have hfr := hy _ ((S.cp_isOpen_Ipast (O σ)).mem_nhds hσ)
      obtain ⟨τ, hτ, z, hz, hzI⟩ := frequently_atTop.1 hfr (σ + c)
      have := hΘ z σ hzI
      rw [hadapt, hz.2] at this
      linarith
  refine ⟨key, fun hint y hy => ?_⟩
  obtain ⟨h1, h2⟩ := key hy
  exact ⟨h1, fun hi => h2 (hint hi)⟩

omit hmono in
/-- Slices, upper limit, for a temporal `Θ` on `M` adapted to `O`. -/
theorem cp_slice_upper_limit_temporal (hint : interior (S.JpastSet J) ⊆ S.D J) {Θ : V → ℝ}
    {c : ℝ} (hΘ : S.IsTemporal Θ) (hadapt : ∀ τ, Θ (O τ) = τ + c) :
    KLs (S.slice J Θ) ⊆ S.H J :=
  (S.cp_slice_upper_limit hOD hadapt fun _ _ h => S.cp_temporal_chr hΘ h).2 hint

omit hmono in
/-- Slices with sequences: `xₙ ∈ S_{τₙ}`, `τₙ → ∞`, `xₙ → x` give `x ∈ 𝓗⁺`. -/
theorem cp_slice_upper_limit_seq (hint : interior (S.JpastSet J) ⊆ S.D J) {Θ : V → ℝ}
    {c : ℝ} (hadapt : ∀ τ, Θ (O τ) = τ + c) (hΘ : ∀ x σ, S.Chr x (O σ) → Θ x < Θ (O σ))
    {τ : ℕ → ℝ} {x : ℕ → V} {x₀ : V} (hτ : Tendsto τ atTop atTop)
    (hx : Tendsto x atTop (𝓝 x₀)) (hA : ∀ n, x n ∈ S.slice J Θ (τ n)) : x₀ ∈ S.H J :=
  (S.cp_slice_upper_limit hOD hadapt hΘ).2 hint (cp_mem_KLs_of_seq hτ hx hA)

end Observer

/-! ## Campaign 74: the slice lower limit

### Campaign 60's Cauchy-temporal definitions (copied) -/

/-- Points of `I⁻(z)` lie in `M` (campaign 60's `cs_Ipast_subset_M`). -/
theorem cp_Ipast_subset_M (z : V) : S.Ipast z ⊆ S.M := by
  intro q hq
  obtain ⟨b, ⟨γ, -, h0, -, hγ⟩, -⟩ := Relation.TransGen.head'_iff.1 hq
  rw [← h0]; exact (hγ 0 ⟨le_rfl, zero_le_one⟩).1

/-- `D` is open (campaign 60's `cs_D_open`). -/
theorem cp_D_open : IsOpen (S.D J) := isOpen_biUnion fun z _ => S.cp_isOpen_Ipast z

/-- `D ⊆ M` (campaign 60's `cs_D_subset_M`). -/
theorem cp_D_subset_M : S.D J ⊆ S.M := iUnion₂_subset fun z _ => S.cp_Ipast_subset_M z

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
def Dsp : Spacetime V := S.restrict (S.D J) (S.cp_D_open J) (S.cp_D_subset_M J)

/-- `prop:causal-alignment`'s hypothesis "`D` is globally hyperbolic" (campaign 60's
`ExteriorGH`). -/
def ExteriorGH : Prop := (S.Dsp J).GloballyHyperbolic

/-! ### `Θ` temporal on `D` only: increase along `≪` into `D`

This removes campaign 72's need for `Θ` temporal on all of `M`: a timelike step ending in `D` runs
inside `D`, so a function temporal on `D` (the paper's setting) increases along it. -/

/-- `≪` into `D` starts in `D`. -/
theorem cp_D_of_chr {x y : V} (h : S.Chr x y) (hy : y ∈ S.D J) : x ∈ S.D J := by
  simp only [D, IpastSet, mem_iUnion] at hy ⊢
  obtain ⟨z, hz, hyz⟩ := hy
  exact ⟨z, hz, S.cp_chr_trans h hyz⟩

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
  · exact S.cp_D_of_chr J (Relation.TransGen.single (S.tstep_tail hγ hγt ⟨ht.1, h⟩)) hy
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
theorem cp_temporalD_chr {Θ : V → ℝ} (hΘ : (S.Dsp J).IsTemporal Θ) {x y : V} (h : S.Chr x y)
    (hy : y ∈ S.D J) : Θ x < Θ y := by
  induction h with
  | single h => exact S.temporalD_tstep J hΘ h hy
  | @tail b c hxb hbc ih =>
    have hb : b ∈ S.D J := S.cp_D_of_chr J (Relation.TransGen.single hbc) hy
    exact (ih hb).trans (S.temporalD_tstep J hΘ hbc hy)

/-! ### ① `Θ → ∞` at the horizon, from a properness hypothesis -/

/-- **Properness of `Θ` on `D`**: no sublevel set `{x ∈ D | Θ x ≤ T}` accumulates outside `D`
(equivalently, for continuous `Θ`, every sublevel set is closed in `V`: `cp_sublevelProper_iff`).
This is the content of "`Θ` is a Cauchy time function of `D` whose levels do not reach `∂D`". -/
def SublevelProper (Θ : V → ℝ) : Prop := ∀ T : ℝ, closure {x | x ∈ S.D J ∧ Θ x ≤ T} ⊆ S.D J

/-- For continuous `Θ`, properness is closedness of the sublevel sets `{x ∈ D | Θ x ≤ T}` in `V`. -/
theorem cp_sublevelProper_iff {Θ : V → ℝ} (hΘ : Continuous Θ) :
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
theorem cp_not_mem_D_of_H {p : V} (hp : p ∈ S.H J) : p ∉ S.D J := fun hpD =>
  hp.2 (interior_maximal (S.cp_D_subset_JpastSet J) (S.cp_D_open J) hpD)

/-- **`Θ → ∞` off `D`**: given properness, every `p ∉ D` and every `T` have a neighbourhood `U`
with `Θ > T` on `U ∩ D`. -/
theorem cp_blowup {Θ : V → ℝ} (hprop : S.SublevelProper J Θ) {p : V} (hp : p ∉ S.D J) (T : ℝ) :
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
theorem cp_blowup_H {Θ : V → ℝ} (hprop : S.SublevelProper J Θ) {p : V} (hp : p ∈ S.H J)
    (T : ℝ) : ∃ U ∈ 𝓝 p, ∀ x ∈ U ∩ S.D J, T < Θ x :=
  S.cp_blowup J hprop (S.cp_not_mem_D_of_H J hp) T

/-- ① in filter form: `Θ x → ∞` as `x → p` inside `D`, for every `p ∈ 𝓗⁺`. -/
theorem cp_tendsto_atTop_H {Θ : V → ℝ} (hprop : S.SublevelProper J Θ) {p : V}
    (hp : p ∈ S.H J) : Tendsto Θ (𝓝[S.D J] p) atTop := by
  rw [Filter.tendsto_atTop]
  intro T
  obtain ⟨U, hU, hUT⟩ := S.cp_blowup_H J hprop hp T
  rw [eventually_nhdsWithin_iff]
  filter_upwards [hU] with x hxU hxD
  exact (hUT x ⟨hxU, hxD⟩).le

/-- **Properness is exactly the blow-up**: `SublevelProper` holds iff `Θ x → ∞` as `x → p` inside
`D`, at every `p ∉ D`. So the hypothesis is not stronger than ① itself. -/
theorem cp_sublevelProper_iff_tendsto {Θ : V → ℝ} :
    S.SublevelProper J Θ ↔ ∀ p ∉ S.D J, Tendsto Θ (𝓝[S.D J] p) atTop := by
  constructor
  · intro hprop p hp
    rw [Filter.tendsto_atTop]
    intro T
    obtain ⟨U, hU, hUT⟩ := S.cp_blowup J hprop hp T
    rw [eventually_nhdsWithin_iff]
    filter_upwards [hU] with x hxU hxD
    exact (hUT x ⟨hxU, hxD⟩).le
  · intro h T q hq
    by_contra hqD
    have hev := (Filter.tendsto_atTop.1 (h q hqD)) (T + 1)
    rw [eventually_nhdsWithin_iff] at hev
    obtain ⟨x, hx, hxD, hxT⟩ := mem_closure_iff_nhds.1 hq _ hev
    linarith [hx hxD]


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
theorem cp_isOpen_Ifut (x : V) : IsOpen {y | S.Chr x y} := by
  refine isOpen_iff_mem_nhds.2 fun q hq => ?_
  obtain ⟨y, hxy, hyq⟩ := Relation.TransGen.tail'_iff.1 hq
  filter_upwards [S.tstep_end_eventually hyq] with q' hq'
  exact Relation.TransGen.tail' hxy hq'

/-- **Step 1.** `q ∈ closure D ⟹ I⁻(q) ⊆ D`: if `x ≪ q`, the open set `I⁺(x)` meets `D` at some
`d`, and `x ≪ d ∈ D` gives `x ∈ D`. -/
theorem cp_Ipast_subset_D {q : V} (hq : q ∈ closure (S.D J)) : S.Ipast q ⊆ S.D J := by
  intro x hx
  obtain ⟨d, hd, hdD⟩ := mem_closure_iff_nhds.1 hq _ ((S.cp_isOpen_Ifut x).mem_nhds hx)
  exact S.cp_D_of_chr J hd hdD

/-- Step 1 at the horizon, under campaign 72's `hcl`. -/
theorem cp_Ipast_subset_D_of_H (hcl : closure (S.JpastSet J) ⊆ closure (S.D J)) {q : V}
    (hq : q ∈ S.H J) : S.Ipast q ⊆ S.D J :=
  S.cp_Ipast_subset_D J (hcl (frontier_subset_closure hq))

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
lemma seg_tstep {q : V} {ε : ℝ}
    (hε : ∀ r ∈ Icc (-ε) 0, S.seg q r ∈ S.M ∧ S.FutTimelike (S.seg q r) (S.T q))
    {s s' : ℝ} (hs : -ε ≤ s) (hss : s < s') (hs' : s' ≤ 0) :
    S.TStep (S.seg q s) (S.seg q s') := by
  have hc : 0 < s' - s := by linarith
  refine ⟨fun u => q + (s + u * (s' - s)) • S.T q, ?_, by simp [seg], by simp [seg], fun u hu => ?_⟩
  · exact contDiff_const.add
      ((contDiff_const.add (contDiff_id.mul contDiff_const)).smul contDiff_const)
  have hd : deriv (fun u => q + (s + u * (s' - s)) • S.T q) u = (s' - s) • S.T q := by
    have h : HasDerivAt (fun u => q + (s + u * (s' - s)) • S.T q) ((1 * (s' - s)) • S.T q) u :=
      ((((hasDerivAt_id u).mul_const (s' - s)).const_add s).smul_const (S.T q)).const_add q
    rw [h.deriv, one_mul]
  have hmem : s + u * (s' - s) ∈ Icc (-ε) 0 := by
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
from `γ 0` attains every level `a ≥ Θ (γ 0)`. Standard-equivalent to campaign 60's
`IsCauchyTemporal` (every future-inextendible causal curve extends to an inextendible one, whose
unique hit of level `a ≥ Θ(γ 0)` lies on the future part since `Θ` increases); that equivalence is
*not* formalised here. -/
def FutCauchyTemporal (Θ : V → ℝ) : Prop :=
  S.IsTemporal Θ ∧ ∀ c : S.FutInextCurve, ∀ a : ℝ, Θ (c.γ 0) ≤ a → ∃ t, 0 ≤ t ∧ Θ (c.γ t) = a

/-- **Step 2 + inextendibility.** For `q ∈ M ∩ closure D \ D` there is a future-inextendible
causal curve of `D` (a `FutInextCurve` of `Dsp`), `γ t = q - ε e^{-t} T(q)`, with `γ t → q`, every
`γ t ≪ q`, and `γ t ≪ γ t'` for `0 ≤ t < t'`. -/
theorem cp_curve {q : V} (hqM : q ∈ S.M) (hqcl : q ∈ closure (S.D J)) (hqD : q ∉ S.D J) :
    ∃ c : (S.Dsp J).FutInextCurve, Tendsto c.γ atTop (𝓝 q) ∧
      (∀ t, 0 ≤ t → S.Chr (c.γ t) q) ∧
      (∀ t t', 0 ≤ t → t < t' → S.Chr (c.γ t) (c.γ t')) := by
  obtain ⟨ε, hε0, hε⟩ := S.seg_timelike hqM
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
  have hchr_q : ∀ t, 0 ≤ t → S.Chr (S.seg q (r t)) q := by
    intro t ht
    have h := S.seg_tstep hε (hr_mem t ht).1 (hr_mem t ht).2 le_rfl
    rw [seg_zero] at h
    exact Relation.TransGen.single h
  have hchr : ∀ t t', 0 ≤ t → t < t' → S.Chr (S.seg q (r t)) (S.seg q (r t')) := by
    intro t t' ht htt
    exact Relation.TransGen.single
      (S.seg_tstep hε (hr_mem t ht).1 (hr_lt t t' htt) (hr_mem t' (by linarith)).2.le)
  have hmemD : ∀ t, 0 ≤ t → S.seg q (r t) ∈ S.D J := fun t ht =>
    S.cp_Ipast_subset_D J hqcl (hchr_q t ht)
  have hlim : Tendsto (fun t => S.seg q (r t)) atTop (𝓝 q) := by
    have h := ((tendsto_const_nhds (x := -ε)).mul Real.tendsto_exp_neg_atTop_nhds_zero).smul_const
      (S.T q) |>.const_add q
    simpa [seg, hr] using h
  have hderiv : ∀ t, HasDerivAt (fun t => S.seg q (r t)) ((ε * Real.exp (-t)) • S.T q) t := by
    intro t
    have h := ((((hasDerivAt_neg t).exp).const_mul (-ε)).smul_const (S.T q)).const_add q
    have e : ε * Real.exp (-t) = -ε * (Real.exp (-t) * -1) := by ring
    rw [e]; exact h
  have hcont : ContinuousOn (fun t => S.seg q (r t)) (Ici 0) :=
    (continuous_const.add
      ((continuous_const.mul (Real.continuous_exp.comp continuous_neg)).smul
        continuous_const)).continuousOn
  refine ⟨⟨fun t => S.seg q (r t), hcont, hmemD, ∅, fun a b => by simp, fun t ht _ => ?_, ?_⟩,
    hlim, hchr_q, hchr⟩
  · refine ⟨(hderiv t).differentiableAt, ?_⟩
    rw [(hderiv t).deriv]
    have hc : 0 < ε * Real.exp (-t) := mul_pos hε0 (Real.exp_pos _)
    obtain ⟨-, h1, h2⟩ := hε _ ⟨(hr_mem t ht.le).1, (hr_mem t ht.le).2.le⟩
    show S.g _ _ _ ≤ 0 ∧ S.g _ _ (S.T _) < 0
    simp only [map_smul, smul_apply, smul_eq_mul]
    refine ⟨?_, mul_neg_of_pos_of_neg hc h2⟩
    have : 0 < (ε * Real.exp (-t)) * (ε * Real.exp (-t)) := mul_pos hc hc
    nlinarith
  · rintro ⟨p, hp, hpl⟩
    exact hqD (tendsto_nhds_unique hlim hpl ▸ hp)

/-- `Θ` (temporal on `D`) increases strictly along the curve of `cp_curve`. -/
lemma curve_mono {Θ : V → ℝ} (hΘ : (S.Dsp J).IsTemporal Θ) (c : (S.Dsp J).FutInextCurve)
    (hc : ∀ t t', 0 ≤ t → t < t' → S.Chr (c.γ t) (c.γ t')) {t t' : ℝ} (ht : 0 ≤ t)
    (htt : t ≤ t') : Θ (c.γ t) ≤ Θ (c.γ t') := by
  rcases htt.lt_or_eq with h | h
  · exact (S.cp_temporalD_chr J hΘ (hc t t' ht h) (c.mem t' (by linarith))).le
  · rw [h]

/-! ### Step 4: properness from the Cauchy property -/

/-- **Step 4, `Θ → ∞` at `q`.** For `q ∈ M ∩ closure D \ D` and every `T'`, a neighbourhood `U` of
`q` has `Θ > T'` on `U ∩ D`: pick `r = γ t` with `Θ r = max (T'+1) (Θ (γ 0))`; `I⁺(r)` works. -/
theorem cp_blowup_cauchy {Θ : V → ℝ} (hΘ : (S.Dsp J).FutCauchyTemporal Θ) {q : V} (hqM : q ∈ S.M)
    (hqcl : q ∈ closure (S.D J)) (hqD : q ∉ S.D J) (T' : ℝ) :
    ∃ U ∈ 𝓝 q, ∀ x ∈ U ∩ S.D J, T' < Θ x := by
  obtain ⟨c, -, hchr_q, -⟩ := S.cp_curve J hqM hqcl hqD
  obtain ⟨t, ht, hta⟩ := hΘ.2 c (max (T' + 1) (Θ (c.γ 0))) (le_max_right _ _)
  refine ⟨{y | S.Chr (c.γ t) y}, (S.cp_isOpen_Ifut _).mem_nhds (hchr_q t ht), fun x hx => ?_⟩
  have h := S.cp_temporalD_chr J hΘ.1 hx.1 hx.2
  have := le_max_left (T' + 1) (Θ (c.γ 0))
  linarith

/-- Step 4 at a horizon point, in filter form: `Θ x → ∞` as `x → q` inside `D`. -/
theorem cp_tendsto_atTop_H_cauchy (hcl : closure (S.JpastSet J) ⊆ closure (S.D J))
    (hHM : S.H J ⊆ S.M) {Θ : V → ℝ} (hΘ : (S.Dsp J).FutCauchyTemporal Θ) {q : V}
    (hq : q ∈ S.H J) : Tendsto Θ (𝓝[S.D J] q) atTop := by
  rw [Filter.tendsto_atTop]
  intro T'
  obtain ⟨U, hU, hUT⟩ := S.cp_blowup_cauchy J hΘ (hHM hq) (hcl (frontier_subset_closure hq))
    (S.cp_not_mem_D_of_H J hq) T'
  rw [eventually_nhdsWithin_iff]
  filter_upwards [hU] with x hxU hxD
  exact (hUT x ⟨hxU, hxD⟩).le

/-- **Step 4, `SublevelProper` derived.** Campaign 74's properness hypothesis follows from the
future Cauchy property, `int J⁻(𝒥⁺) ⊆ D` (campaign 72's `hint`) and `𝓗⁺ ⊆ M`. -/
theorem cp_sublevelProper (hint : interior (S.JpastSet J) ⊆ S.D J) (hHM : S.H J ⊆ S.M)
    {Θ : V → ℝ} (hΘ : (S.Dsp J).FutCauchyTemporal Θ) : S.SublevelProper J Θ := by
  intro T' p hp
  by_contra hpD
  have hpcl : p ∈ closure (S.D J) := closure_mono (fun x hx => hx.1) hp
  have hpH : p ∈ S.H J :=
    ⟨closure_mono (S.cp_D_subset_JpastSet J) hpcl, fun hi => hpD (hint hi)⟩
  obtain ⟨U, hU, hUT⟩ := S.cp_blowup_cauchy J hΘ (hHM hpH) hpcl hpD T'
  obtain ⟨x, hxU, hxD, hxT⟩ := mem_closure_iff_nhds.1 hp U hU
  linarith [hUT x ⟨hxU, hxD⟩]

/-! ### Step 5: the slice lower limit, with no properness and no local connectedness -/

/-- **Step 5, pointwise.** `q ∈ M ∩ closure D \ D ⟹ q ∈ KLi(S_τ)`: the tail of the curve lies in
`U`, and the levels `τ ≥ Θ(γ t₀)` are hit on that tail (Cauchy property + monotonicity of `Θ`). -/
theorem cp_mem_KLi_slice {Θ : V → ℝ} (hΘ : (S.Dsp J).FutCauchyTemporal Θ) {q : V}
    (hqM : q ∈ S.M) (hqcl : q ∈ closure (S.D J)) (hqD : q ∉ S.D J) :
    q ∈ KLi (S.slice J Θ) := by
  intro U hU
  obtain ⟨c, hlim, -, hchr⟩ := S.cp_curve J hqM hqcl hqD
  obtain ⟨t₀, ht₀⟩ := eventually_atTop.1 ((hlim.eventually hU).and (eventually_ge_atTop 0))
  have ht₀0 : 0 ≤ t₀ := (ht₀ t₀ le_rfl).2
  filter_upwards [eventually_ge_atTop (Θ (c.γ t₀))] with τ hτ
  obtain ⟨t, ht0, htτ⟩ :=
    hΘ.2 c τ ((S.curve_mono J hΘ.1 c hchr le_rfl ht₀0).trans hτ)
  have htt : t₀ ≤ t := by
    by_contra h
    rw [not_le] at h
    have := S.cp_temporalD_chr J hΘ.1 (hchr t t₀ ht0 h) (c.mem t₀ ht₀0)
    linarith
  exact ⟨c.γ t, ⟨c.mem t ht0, htτ⟩, (ht₀ t htt).1⟩

/-- **Step 5, `𝓗⁺ ⊆ KLi(S_τ)`.** Hypotheses: campaign 72's `hcl`, `𝓗⁺ ⊆ M`, and `Θ` Cauchy temporal
on `D` (future form). No `SublevelProper`, no `LocConnAt`, no separate continuity hypothesis. -/
theorem cp_slice_lower_limit (hcl : closure (S.JpastSet J) ⊆ closure (S.D J))
    (hHM : S.H J ⊆ S.M) {Θ : V → ℝ} (hΘ : (S.Dsp J).FutCauchyTemporal Θ) :
    S.H J ⊆ KLi (S.slice J Θ) := fun _ hq =>
  S.cp_mem_KLi_slice J hΘ (hHM hq) (hcl (frontier_subset_closure hq)) (S.cp_not_mem_D_of_H J hq)

/-- Step 5 with sequences: `q = lim xₙ`, `xₙ ∈ S_{τₙ}`, `τₙ → ∞`. -/
theorem cp_slice_lower_limit_seq (hcl : closure (S.JpastSet J) ⊆ closure (S.D J))
    (hHM : S.H J ⊆ S.M) {Θ : V → ℝ} (hΘ : (S.Dsp J).FutCauchyTemporal Θ) {q : V}
    (hq : q ∈ S.H J) :
    ∃ τ : ℕ → ℝ, ∃ x : ℕ → V, Tendsto τ atTop atTop ∧ Tendsto x atTop (𝓝 q) ∧
      ∀ n, x n ∈ S.slice J Θ (τ n) := by
  have h : ∀ n : ℕ, ∃ τ ≥ (n:ℝ), ∃ x ∈ S.slice J Θ τ, x ∈ ball q (1 / ((n:ℝ) + 1)) := fun n =>
    ((S.cp_slice_lower_limit J hcl hHM hΘ hq _ (ball_mem_nhds q (by positivity))).and
      (eventually_ge_atTop (n:ℝ))).exists.imp fun _ h => ⟨h.2, h.1⟩
  choose τ hτ x hx hxb using h
  refine ⟨τ, x, tendsto_atTop_mono hτ tendsto_natCast_atTop_atTop, ?_, hx⟩
  rw [tendsto_iff_dist_tendsto_zero]
  exact squeeze_zero (fun _ => dist_nonneg) (fun n => (mem_ball.1 (hxb n)).le)
    tendsto_one_div_add_atTop_nhds_zero_nat

/-! ### Step 6: `KLi(S_τ) = KLs(S_τ) = 𝓗⁺` under the proposition's hypotheses -/

section Slices
variable {S J} {O : ℝ → V} (hOD : S.IpastSet (range O) = S.D J)
include hOD

/-- **Step 6.** For `Θ` Cauchy temporal on `D` (future form), adapted to a future-directed
observer worldline `O` with `I⁻(O) = D`, and campaign 72's `hcl`, `hint`, plus `𝓗⁺ ⊆ M`:
`KLi(S_τ) = KLs(S_τ) = 𝓗⁺`. No properness, no local connectedness, no continuity hypothesis. -/
theorem cp_slice_kuratowski (hmono : ∀ s t : ℝ, s < t → S.Chr (O s) (O t))
    (hcl : closure (S.JpastSet J) ⊆ closure (S.D J))
    (hint : interior (S.JpastSet J) ⊆ S.D J) (hHM : S.H J ⊆ S.M) {Θ : V → ℝ} {c : ℝ}
    (hΘ : (S.Dsp J).FutCauchyTemporal Θ) (hadapt : ∀ τ, Θ (O τ) = τ + c) :
    KLi (S.slice J Θ) = S.H J ∧ KLs (S.slice J Θ) = S.H J := by
  have h1 := S.cp_slice_lower_limit J hcl hHM hΘ
  have h2 := (S.cp_slice_upper_limit hOD hadapt
    (fun x σ h => S.cp_temporalD_chr J hΘ.1 h (S.cp_observer_mem_D hOD hmono σ))).2 hint
  have h3 := cp_KLi_subset_KLs (S.slice J Θ)
  exact ⟨(h3.trans h2).antisymm h1, h2.antisymm (h1.trans h3)⟩

/-- **`prop:causal-alignment`, both halves**: under the same hypotheses, properness holds (so
campaign 74's hypothesis is a consequence) and the slices converge to `𝓗⁺`. -/
theorem cp_causal_alignment (hmono : ∀ s t : ℝ, s < t → S.Chr (O s) (O t))
    (hcl : closure (S.JpastSet J) ⊆ closure (S.D J))
    (hint : interior (S.JpastSet J) ⊆ S.D J) (hHM : S.H J ⊆ S.M) {Θ : V → ℝ} {c : ℝ}
    (hΘ : (S.Dsp J).FutCauchyTemporal Θ) (hadapt : ∀ τ, Θ (O τ) = τ + c) :
    S.SublevelProper J Θ ∧ KLi (S.slice J Θ) = S.H J ∧ KLs (S.slice J Θ) = S.H J :=
  ⟨S.cp_sublevelProper J hint hHM hΘ, S.cp_slice_kuratowski hOD hmono hcl hint hHM hΘ hadapt⟩

end Slices

end Spacetime

#print axioms Spacetime.cp_isOpen_Ipast
#print axioms Spacetime.cp_temporalD_chr
#print axioms Spacetime.cp_slice_upper_limit
#print axioms Spacetime.cp_sublevelProper_iff_tendsto
#print axioms Spacetime.cp_isOpen_Ifut
#print axioms Spacetime.cp_Ipast_subset_D
#print axioms Spacetime.cp_Ipast_subset_D_of_H
#print axioms Spacetime.cp_curve
#print axioms Spacetime.cp_blowup_cauchy
#print axioms Spacetime.cp_tendsto_atTop_H_cauchy
#print axioms Spacetime.cp_sublevelProper
#print axioms Spacetime.cp_mem_KLi_slice
#print axioms Spacetime.cp_slice_lower_limit
#print axioms Spacetime.cp_slice_lower_limit_seq
#print axioms Spacetime.cp_slice_kuratowski
#print axioms Spacetime.cp_causal_alignment

end ShadowProbe.CauchyPropernessProbe

import Mathlib

/-!
# Probe `r7641+71.3` (campaign 78, `r7641` ②): the vacuity repair, a polygonal past extension, and
two-sided ⇒ future Cauchy

Registration: `computations/formalisation/r7641_71_campaign78/PREDICTION.md`. Finding answered:
`computations/formalisation/r7641_71_vacuity/FINDING.md` (`probes/VacuityCheck.lean` proves `False`
from campaign 75's hypotheses whenever `𝓗⁺ ≠ ∅`). Nothing imports this file, and it imports no
other probe.

## Copied

Campaign 75's `probes/CauchyProperness.lean`, whole, renamed `cp_… ↦ cr_…`, namespace
`ShadowProbe.CauchyRepairProbe` (its own header, items 1–6, is summarised here: `I⁺(x)` open,
`I⁻(q) ⊆ D` for `q ∈ closure D`, the curve `q - ε e^{-t} T(q)`, properness and the slice lower
limit from the future Cauchy property, `KLi(S_τ) = KLs(S_τ) = 𝓗⁺`).

## ⓪ The repair — BUILT

`IsTemporal τ := ContDiffOn ℝ 1 τ S.M ∧ ∀ x ∈ S.M, ∀ v, S.FutCausal x v → 0 < fderiv ℝ τ x v`
(was `ContDiff ℝ 1 τ ∧ …`). `M` is open, so `fderiv` at `x ∈ M` is the derivative of `τ|_M`. The old
global `ContDiff` made `Θ` continuous at every horizon point, while the Cauchy property forces
`Θ → ∞` along `𝓝[D] q` there: unsatisfiable when `𝓗⁺ ≠ ∅`.

* Only `temporal_tstep` (now via `temporal_curve`, using `ContDiffOn.contDiffAt` on the open `M`)
  and `temporalD_tstep` (now: a step into `D` is a `Dsp`-step, `tstep_Dsp`) changed. The rest of the
  chain — `cr_temporalD_chr`, `cr_curve`, `cr_blowup_cauchy`, `cr_tendsto_atTop_H_cauchy`,
  `cr_sublevelProper`, `cr_slice_lower_limit`, `cr_slice_kuratowski`, `cr_causal_alignment` —
  re-checks verbatim under the repaired definition.
* Sanity (no model): `cr_isTemporal_congr` (only `τ|_M` matters), `cr_isTemporal_update_H` (the
  value at a horizon point is free), `cr_no_blowup_of_continuousAt` (the old mechanism, now not
  triggered: `cr_temporalD_continuousOn` gives continuity on `D` only), `cr_blowup_consistent_toy`.
  No hypothesis anywhere in this file asserts continuity of `Θ` off `D`. The satisfiable model
  with `𝓗⁺ ≠ ∅` is campaign 79's, not here.

## ① Polygonal past extension — BUILT

`cr_past_extension`: from `x ∈ M`, a continuous `p` on `ℝ`, `p 0 = x`, with `p t ∈ M`, `p t ≪ x`
for `t < 0`, `C¹` and future-timelike off the integers, and no past limit in `M`. Vertices
`X (k+1) = X k - ℓ_k T(X k)`; `ℓ_k` is the **dyadic safe length** (`Nat.find` of the least `n` with
`[-2^{-n}, 0]` safe), the registered fallback for the "largest safe `ℓ`" supremum; the tube lemma
(`safe_uniform`) bounds it below near any `x* ∈ M`.

## ② Two-sided ⇒ future — BUILT

`cr_futCauchy_of_cauchy` (any spacetime), `cr_futCauchy_of_cauchy_D` (on `Dsp J`), and
`cr_causal_alignment_gh`: `prop:causal-alignment` under campaign 60's two-sided `IsCauchyTemporal`
(repaired), plus `cr_exteriorGH_of`.

## Stretch: two-sided ⇔ future ∧ past — BUILT

`cr_cauchy_iff`. The past form `cr_pastCauchy_of_cauchy` uses the time-reversed chart `rev`
(`T ↦ -T`), whose ① is a future extension of `S` (`cr_future_extension`). The converse uses
`cr_strictMono_curve` (`Θ` strictly increases along every inextendible causal curve; induction on
the finitely many breaks in `[a, b]`).

One extra hypothesis remains from campaign 75: `hHM : 𝓗⁺ ⊆ M`.
-/
open Set Filter Topology Metric

namespace ShadowProbe.CauchyRepairProbe

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
theorem cr_isOpen_Ipast (p : V) : IsOpen (S.Ipast p) := by
  refine isOpen_iff_mem_nhds.2 fun q hq => ?_
  obtain ⟨y, hqy, hyp⟩ := Relation.TransGen.head'_iff.1 hq
  filter_upwards [S.tstep_start_eventually hqy] with q' hq'
  exact Relation.TransGen.head' hq' hyp

lemma tstep_to_cstep {x y : V} (h : S.TStep x y) : S.CStep x y := by
  obtain ⟨γ, hγ, h0, h1, hγt⟩ := h
  exact ⟨γ, hγ, h0, h1, fun t ht => ⟨(hγt t ht).1, (hγt t ht).2.1.le, (hγt t ht).2.2⟩⟩

/-- `≪ ⊆ ≤`. -/
theorem cr_chr_cau {x y : V} (h : S.Chr x y) : S.Cau x y := by
  induction h with
  | single h => exact Relation.ReflTransGen.single (S.tstep_to_cstep h)
  | tail _ h ih => exact ih.tail (S.tstep_to_cstep h)

theorem cr_chr_trans {x y z : V} (h1 : S.Chr x y) (h2 : S.Chr y z) : S.Chr x z :=
  Relation.TransGen.trans h1 h2

theorem cr_cau_trans {x y z : V} (h1 : S.Cau x y) (h2 : S.Cau y z) : S.Cau x z :=
  Relation.ReflTransGen.trans h1 h2

theorem cr_Ipast_subset_Jpast (p : V) : S.Ipast p ⊆ S.Jpast p := fun _ h => S.cr_chr_cau h

/-- `I⁻(p) ⊆ int J⁻(p)`. -/
theorem cr_Ipast_subset_interior (p : V) : S.Ipast p ⊆ interior (S.Jpast p) :=
  interior_maximal (S.cr_Ipast_subset_Jpast p) (S.cr_isOpen_Ipast p)

/-! ### Temporal functions (campaign 60) -/

/-- **A temporal function, repaired (campaign 78, ⓪).** `τ` is `C¹` *on `M`* (not on the whole
chart `V`), with `dτ(v) > 0` for every future-causal `v` at points of `M`. Since `M` is open,
`fderiv ℝ τ x` at `x ∈ M` is the honest derivative of `τ|_M`.

*Change from campaigns 60/72/74/75:* those required `ContDiff ℝ 1 τ` on all of `V`. Applied to
`Dsp J` (whose `M` is `D`), that made `Θ` continuous at every horizon point, contradicting the
blow-up `Θ → ∞` along `𝓝[D] q`, `q ∈ 𝓗⁺`, that the Cauchy property forces (`r7641+71.1`,
`probes/VacuityCheck.lean`): the hypotheses were unsatisfiable whenever `𝓗⁺ ≠ ∅`. The repaired
definition constrains `τ` on `M` only (`cr_isTemporal_congr`), so no continuity across `∂M` is
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

/-- A temporal function increases strictly along `≪` (campaign 60's `cs_temporal_chr`). -/
theorem cr_temporal_chr {τ : V → ℝ} (hτ : S.IsTemporal τ) {x y : V} (h : S.Chr x y) :
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

theorem cr_D_subset_JpastSet : S.D J ⊆ S.JpastSet J :=
  biUnion_mono subset_rfl fun p _ => S.cr_Ipast_subset_Jpast p

/-- `p ∈ D ⟹ J⁻(p) ⊆ J⁻(𝒥⁺)` (transitivity only). -/
theorem cr_Jpast_subset_JpastSet {p : V} (hp : p ∈ S.D J) : S.Jpast p ⊆ S.JpastSet J := by
  intro q hq
  simp only [D, IpastSet, JpastSet, mem_iUnion] at hp ⊢
  obtain ⟨z, hz, hpz⟩ := hp
  exact ⟨z, hz, S.cr_cau_trans hq (S.cr_chr_cau hpz)⟩


end Spacetime

/-- Kuratowski lower limit of a family of sets as `τ → ∞`. -/
def KLi (A : ℝ → Set V) : Set V := {p | ∀ U ∈ 𝓝 p, ∀ᶠ τ in atTop, (A τ ∩ U).Nonempty}
/-- Kuratowski upper limit of a family of sets as `τ → ∞`. -/
def KLs (A : ℝ → Set V) : Set V := {p | ∀ U ∈ 𝓝 p, ∃ᶠ τ in atTop, (A τ ∩ U).Nonempty}

omit [NormedSpace ℝ V] in
/-- `Li ⊆ Ls`. -/
theorem cr_KLi_subset_KLs (A : ℝ → Set V) : KLi A ⊆ KLs A :=
  fun _ hp U hU => (hp U hU).frequently


omit [NormedSpace ℝ V] in
/-- Membership in `Ls` from a sequence: `yₙ ∈ A τₙ`, `τₙ → ∞`, `yₙ → y` give `y ∈ Ls A`. -/
theorem cr_mem_KLs_of_seq {A : ℝ → Set V} {τ : ℕ → ℝ} {y : ℕ → V} {y₀ : V}
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
theorem cr_Ipast_mono {σ τ : ℝ} (h : σ ≤ τ) : S.Ipast (O σ) ⊆ S.Ipast (O τ) := by
  rcases h.lt_or_eq with h | h
  · exact fun q hq => S.cr_chr_trans hq (hmono σ τ h)
  · rw [h]

/-- Each `O τ` lies in `D`. -/
theorem cr_observer_mem_D (τ : ℝ) : O τ ∈ S.D J := by
  rw [← hOD]
  exact mem_biUnion (mem_range_self (τ + 1)) (hmono τ (τ + 1) (by linarith))

/-- `x ∈ D ⟹ x ∈ I⁻(O τ)` for all large `τ`. -/
theorem cr_D_eventually {x : V} (hx : x ∈ S.D J) : ∀ᶠ τ in atTop, x ∈ S.Ipast (O τ) := by
  rw [← hOD] at hx
  simp only [IpastSet, mem_iUnion] at hx
  obtain ⟨_, ⟨σ, rfl⟩, hσ⟩ := hx
  filter_upwards [eventually_ge_atTop σ] with τ hτ
  exact S.cr_Ipast_mono hmono hτ hσ

omit hOD hmono in
/-- Under the two hypotheses, `𝓗⁺ = closure D \ D`. -/
theorem cr_H_eq_closure_diff (hcl : closure (S.JpastSet J) ⊆ closure (S.D J))
    (hint : interior (S.JpastSet J) ⊆ S.D J) :
    S.H J = closure (S.D J) \ S.D J := by
  ext p
  constructor
  · intro hp
    refine ⟨hcl (frontier_subset_closure hp), fun hpD => hp.2 ?_⟩
    exact interior_maximal (S.cr_D_subset_JpastSet J)
      (isOpen_biUnion fun z _ => S.cr_isOpen_Ipast z) hpD
  · rintro ⟨h1, h2⟩
    exact ⟨closure_mono (S.cr_D_subset_JpastSet J) h1, fun hi => h2 (hint hi)⟩

/-! ### The slices `S_τ` accumulate on `𝓗⁺` -/

omit hmono in
/-- **Slices, upper limit.** Adapted `Θ`: `Θ (O τ) = τ + c`, and `Θ` increases along every `≪`
ending on the worldline. Then `Ls S_τ ⊆ closure J⁻(𝒥⁺) \ D`, and `⊆ 𝓗⁺` given `int J⁻(𝒥⁺) ⊆ D`. -/
theorem cr_slice_upper_limit {Θ : V → ℝ} {c : ℝ} (hadapt : ∀ τ, Θ (O τ) = τ + c)
    (hΘ : ∀ x σ, S.Chr x (O σ) → Θ x < Θ (O σ)) :
    KLs (S.slice J Θ) ⊆ closure (S.JpastSet J) \ S.D J ∧
    (interior (S.JpastSet J) ⊆ S.D J → KLs (S.slice J Θ) ⊆ S.H J) := by
  have key : KLs (S.slice J Θ) ⊆ closure (S.JpastSet J) \ S.D J := by
    intro y hy
    refine ⟨?_, fun hyD => ?_⟩
    · rw [mem_closure_iff_nhds]
      intro U hU
      obtain ⟨τ, z, hz, hzU⟩ := (hy U hU).exists
      exact ⟨z, hzU, S.cr_D_subset_JpastSet J hz.1⟩
    · rw [← hOD] at hyD
      simp only [IpastSet, mem_iUnion] at hyD
      obtain ⟨_, ⟨σ, rfl⟩, hσ⟩ := hyD
      have hfr := hy _ ((S.cr_isOpen_Ipast (O σ)).mem_nhds hσ)
      obtain ⟨τ, hτ, z, hz, hzI⟩ := frequently_atTop.1 hfr (σ + c)
      have := hΘ z σ hzI
      rw [hadapt, hz.2] at this
      linarith
  refine ⟨key, fun hint y hy => ?_⟩
  obtain ⟨h1, h2⟩ := key hy
  exact ⟨h1, fun hi => h2 (hint hi)⟩

omit hmono in
/-- Slices, upper limit, for a temporal `Θ` on `M` adapted to `O`. -/
theorem cr_slice_upper_limit_temporal (hint : interior (S.JpastSet J) ⊆ S.D J) {Θ : V → ℝ}
    {c : ℝ} (hΘ : S.IsTemporal Θ) (hadapt : ∀ τ, Θ (O τ) = τ + c) :
    KLs (S.slice J Θ) ⊆ S.H J :=
  (S.cr_slice_upper_limit hOD hadapt fun _ _ h => S.cr_temporal_chr hΘ h).2 hint

omit hmono in
/-- Slices with sequences: `xₙ ∈ S_{τₙ}`, `τₙ → ∞`, `xₙ → x` give `x ∈ 𝓗⁺`. -/
theorem cr_slice_upper_limit_seq (hint : interior (S.JpastSet J) ⊆ S.D J) {Θ : V → ℝ}
    {c : ℝ} (hadapt : ∀ τ, Θ (O τ) = τ + c) (hΘ : ∀ x σ, S.Chr x (O σ) → Θ x < Θ (O σ))
    {τ : ℕ → ℝ} {x : ℕ → V} {x₀ : V} (hτ : Tendsto τ atTop atTop)
    (hx : Tendsto x atTop (𝓝 x₀)) (hA : ∀ n, x n ∈ S.slice J Θ (τ n)) : x₀ ∈ S.H J :=
  (S.cr_slice_upper_limit hOD hadapt hΘ).2 hint (cr_mem_KLs_of_seq hτ hx hA)

end Observer

/-! ## Campaign 74: the slice lower limit

### Campaign 60's Cauchy-temporal definitions (copied) -/

/-- Points of `I⁻(z)` lie in `M` (campaign 60's `cs_Ipast_subset_M`). -/
theorem cr_Ipast_subset_M (z : V) : S.Ipast z ⊆ S.M := by
  intro q hq
  obtain ⟨b, ⟨γ, -, h0, -, hγ⟩, -⟩ := Relation.TransGen.head'_iff.1 hq
  rw [← h0]; exact (hγ 0 ⟨le_rfl, zero_le_one⟩).1

/-- `D` is open (campaign 60's `cs_D_open`). -/
theorem cr_D_open : IsOpen (S.D J) := isOpen_biUnion fun z _ => S.cr_isOpen_Ipast z

/-- `D ⊆ M` (campaign 60's `cs_D_subset_M`). -/
theorem cr_D_subset_M : S.D J ⊆ S.M := iUnion₂_subset fun z _ => S.cr_Ipast_subset_M z

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
def Dsp : Spacetime V := S.restrict (S.D J) (S.cr_D_open J) (S.cr_D_subset_M J)

/-- `prop:causal-alignment`'s hypothesis "`D` is globally hyperbolic" (campaign 60's
`ExteriorGH`). -/
def ExteriorGH : Prop := (S.Dsp J).GloballyHyperbolic

/-! ### `Θ` temporal on `D` only: increase along `≪` into `D`

This removes campaign 72's need for `Θ` temporal on all of `M`: a timelike step ending in `D` runs
inside `D`, so a function temporal on `D` (the paper's setting) increases along it. -/

/-- `≪` into `D` starts in `D`. -/
theorem cr_D_of_chr {x y : V} (h : S.Chr x y) (hy : y ∈ S.D J) : x ∈ S.D J := by
  simp only [D, IpastSet, mem_iUnion] at hy ⊢
  obtain ⟨z, hz, hyz⟩ := hy
  exact ⟨z, hz, S.cr_chr_trans h hyz⟩

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
  · exact S.cr_D_of_chr J (Relation.TransGen.single (S.tstep_tail hγ hγt ⟨ht.1, h⟩)) hy
  · rw [h]; exact hy

/-- A timelike step of `S` ending in `D` is a timelike step of `Dsp J`. -/
lemma tstep_Dsp {x y : V} (h : S.TStep x y) (hy : y ∈ S.D J) : (S.Dsp J).TStep x y := by
  obtain ⟨γ, hγ, h0, h1, hγt⟩ := h
  exact ⟨γ, hγ, h0, h1, fun t ht => ⟨S.tstep_in_D J hγ hγt (h1 ▸ hy) ht, (hγt t ht).2⟩⟩

lemma temporalD_tstep {Θ : V → ℝ} (hΘ : (S.Dsp J).IsTemporal Θ) {x y : V} (h : S.TStep x y)
    (hy : y ∈ S.D J) : Θ x < Θ y :=
  (S.Dsp J).temporal_tstep hΘ (S.tstep_Dsp J h hy)

/-- **A function temporal on `D` only increases along every `≪` ending in `D`.** -/
theorem cr_temporalD_chr {Θ : V → ℝ} (hΘ : (S.Dsp J).IsTemporal Θ) {x y : V} (h : S.Chr x y)
    (hy : y ∈ S.D J) : Θ x < Θ y := by
  induction h with
  | single h => exact S.temporalD_tstep J hΘ h hy
  | @tail b c hxb hbc ih =>
    have hb : b ∈ S.D J := S.cr_D_of_chr J (Relation.TransGen.single hbc) hy
    exact (ih hb).trans (S.temporalD_tstep J hΘ hbc hy)

/-! ### ① `Θ → ∞` at the horizon, from a properness hypothesis -/

/-- **Properness of `Θ` on `D`**: no sublevel set `{x ∈ D | Θ x ≤ T}` accumulates outside `D`
(equivalently, for continuous `Θ`, every sublevel set is closed in `V`: `cr_sublevelProper_iff`).
This is the content of "`Θ` is a Cauchy time function of `D` whose levels do not reach `∂D`". -/
def SublevelProper (Θ : V → ℝ) : Prop := ∀ T : ℝ, closure {x | x ∈ S.D J ∧ Θ x ≤ T} ⊆ S.D J

/-- For continuous `Θ`, properness is closedness of the sublevel sets `{x ∈ D | Θ x ≤ T}` in `V`. -/
theorem cr_sublevelProper_iff {Θ : V → ℝ} (hΘ : Continuous Θ) :
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
theorem cr_not_mem_D_of_H {p : V} (hp : p ∈ S.H J) : p ∉ S.D J := fun hpD =>
  hp.2 (interior_maximal (S.cr_D_subset_JpastSet J) (S.cr_D_open J) hpD)

/-- **`Θ → ∞` off `D`**: given properness, every `p ∉ D` and every `T` have a neighbourhood `U`
with `Θ > T` on `U ∩ D`. -/
theorem cr_blowup {Θ : V → ℝ} (hprop : S.SublevelProper J Θ) {p : V} (hp : p ∉ S.D J) (T : ℝ) :
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
theorem cr_blowup_H {Θ : V → ℝ} (hprop : S.SublevelProper J Θ) {p : V} (hp : p ∈ S.H J)
    (T : ℝ) : ∃ U ∈ 𝓝 p, ∀ x ∈ U ∩ S.D J, T < Θ x :=
  S.cr_blowup J hprop (S.cr_not_mem_D_of_H J hp) T

/-- ① in filter form: `Θ x → ∞` as `x → p` inside `D`, for every `p ∈ 𝓗⁺`. -/
theorem cr_tendsto_atTop_H {Θ : V → ℝ} (hprop : S.SublevelProper J Θ) {p : V}
    (hp : p ∈ S.H J) : Tendsto Θ (𝓝[S.D J] p) atTop := by
  rw [Filter.tendsto_atTop]
  intro T
  obtain ⟨U, hU, hUT⟩ := S.cr_blowup_H J hprop hp T
  rw [eventually_nhdsWithin_iff]
  filter_upwards [hU] with x hxU hxD
  exact (hUT x ⟨hxU, hxD⟩).le

/-- **Properness is exactly the blow-up**: `SublevelProper` holds iff `Θ x → ∞` as `x → p` inside
`D`, at every `p ∉ D`. So the hypothesis is not stronger than ① itself. -/
theorem cr_sublevelProper_iff_tendsto {Θ : V → ℝ} :
    S.SublevelProper J Θ ↔ ∀ p ∉ S.D J, Tendsto Θ (𝓝[S.D J] p) atTop := by
  constructor
  · intro hprop p hp
    rw [Filter.tendsto_atTop]
    intro T
    obtain ⟨U, hU, hUT⟩ := S.cr_blowup J hprop hp T
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
theorem cr_isOpen_Ifut (x : V) : IsOpen {y | S.Chr x y} := by
  refine isOpen_iff_mem_nhds.2 fun q hq => ?_
  obtain ⟨y, hxy, hyq⟩ := Relation.TransGen.tail'_iff.1 hq
  filter_upwards [S.tstep_end_eventually hyq] with q' hq'
  exact Relation.TransGen.tail' hxy hq'

/-- **Step 1.** `q ∈ closure D ⟹ I⁻(q) ⊆ D`: if `x ≪ q`, the open set `I⁺(x)` meets `D` at some
`d`, and `x ≪ d ∈ D` gives `x ∈ D`. -/
theorem cr_Ipast_subset_D {q : V} (hq : q ∈ closure (S.D J)) : S.Ipast q ⊆ S.D J := by
  intro x hx
  obtain ⟨d, hd, hdD⟩ := mem_closure_iff_nhds.1 hq _ ((S.cr_isOpen_Ifut x).mem_nhds hx)
  exact S.cr_D_of_chr J hd hdD

/-- Step 1 at the horizon, under campaign 72's `hcl`. -/
theorem cr_Ipast_subset_D_of_H (hcl : closure (S.JpastSet J) ⊆ closure (S.D J)) {q : V}
    (hq : q ∈ S.H J) : S.Ipast q ⊆ S.D J :=
  S.cr_Ipast_subset_D J (hcl (frontier_subset_closure hq))

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
from `γ 0` attains every level `a ≥ Θ (γ 0)`. Campaign 78: implied by campaign 60's
`IsCauchyTemporal` (`cr_futCauchy_of_cauchy`, ②), and together with the past form equivalent to it
(`cr_cauchy_iff`). -/
def FutCauchyTemporal (Θ : V → ℝ) : Prop :=
  S.IsTemporal Θ ∧ ∀ c : S.FutInextCurve, ∀ a : ℝ, Θ (c.γ 0) ≤ a → ∃ t, 0 ≤ t ∧ Θ (c.γ t) = a

/-- **Step 2 + inextendibility.** For `q ∈ M ∩ closure D \ D` there is a future-inextendible
causal curve of `D` (a `FutInextCurve` of `Dsp`), `γ t = q - ε e^{-t} T(q)`, with `γ t → q`, every
`γ t ≪ q`, and `γ t ≪ γ t'` for `0 ≤ t < t'`. -/
theorem cr_curve {q : V} (hqM : q ∈ S.M) (hqcl : q ∈ closure (S.D J)) (hqD : q ∉ S.D J) :
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
    S.cr_Ipast_subset_D J hqcl (hchr_q t ht)
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

/-- `Θ` (temporal on `D`) increases strictly along the curve of `cr_curve`. -/
lemma curve_mono {Θ : V → ℝ} (hΘ : (S.Dsp J).IsTemporal Θ) (c : (S.Dsp J).FutInextCurve)
    (hc : ∀ t t', 0 ≤ t → t < t' → S.Chr (c.γ t) (c.γ t')) {t t' : ℝ} (ht : 0 ≤ t)
    (htt : t ≤ t') : Θ (c.γ t) ≤ Θ (c.γ t') := by
  rcases htt.lt_or_eq with h | h
  · exact (S.cr_temporalD_chr J hΘ (hc t t' ht h) (c.mem t' (by linarith))).le
  · rw [h]

/-! ### Step 4: properness from the Cauchy property -/

/-- **Step 4, `Θ → ∞` at `q`.** For `q ∈ M ∩ closure D \ D` and every `T'`, a neighbourhood `U` of
`q` has `Θ > T'` on `U ∩ D`: pick `r = γ t` with `Θ r = max (T'+1) (Θ (γ 0))`; `I⁺(r)` works. -/
theorem cr_blowup_cauchy {Θ : V → ℝ} (hΘ : (S.Dsp J).FutCauchyTemporal Θ) {q : V} (hqM : q ∈ S.M)
    (hqcl : q ∈ closure (S.D J)) (hqD : q ∉ S.D J) (T' : ℝ) :
    ∃ U ∈ 𝓝 q, ∀ x ∈ U ∩ S.D J, T' < Θ x := by
  obtain ⟨c, -, hchr_q, -⟩ := S.cr_curve J hqM hqcl hqD
  obtain ⟨t, ht, hta⟩ := hΘ.2 c (max (T' + 1) (Θ (c.γ 0))) (le_max_right _ _)
  refine ⟨{y | S.Chr (c.γ t) y}, (S.cr_isOpen_Ifut _).mem_nhds (hchr_q t ht), fun x hx => ?_⟩
  have h := S.cr_temporalD_chr J hΘ.1 hx.1 hx.2
  have := le_max_left (T' + 1) (Θ (c.γ 0))
  linarith

/-- Step 4 at a horizon point, in filter form: `Θ x → ∞` as `x → q` inside `D`. Campaign 78: this
is what made the old hypotheses vacuous (with global continuity of `Θ`); under the repaired
`IsTemporal` it is consistent, cf. `cr_blowup_consistent_toy`. -/
theorem cr_tendsto_atTop_H_cauchy (hcl : closure (S.JpastSet J) ⊆ closure (S.D J))
    (hHM : S.H J ⊆ S.M) {Θ : V → ℝ} (hΘ : (S.Dsp J).FutCauchyTemporal Θ) {q : V}
    (hq : q ∈ S.H J) : Tendsto Θ (𝓝[S.D J] q) atTop := by
  rw [Filter.tendsto_atTop]
  intro T'
  obtain ⟨U, hU, hUT⟩ := S.cr_blowup_cauchy J hΘ (hHM hq) (hcl (frontier_subset_closure hq))
    (S.cr_not_mem_D_of_H J hq) T'
  rw [eventually_nhdsWithin_iff]
  filter_upwards [hU] with x hxU hxD
  exact (hUT x ⟨hxU, hxD⟩).le

/-- **Step 4, `SublevelProper` derived.** Campaign 74's properness hypothesis follows from the
future Cauchy property, `int J⁻(𝒥⁺) ⊆ D` (campaign 72's `hint`) and `𝓗⁺ ⊆ M`. -/
theorem cr_sublevelProper (hint : interior (S.JpastSet J) ⊆ S.D J) (hHM : S.H J ⊆ S.M)
    {Θ : V → ℝ} (hΘ : (S.Dsp J).FutCauchyTemporal Θ) : S.SublevelProper J Θ := by
  intro T' p hp
  by_contra hpD
  have hpcl : p ∈ closure (S.D J) := closure_mono (fun x hx => hx.1) hp
  have hpH : p ∈ S.H J :=
    ⟨closure_mono (S.cr_D_subset_JpastSet J) hpcl, fun hi => hpD (hint hi)⟩
  obtain ⟨U, hU, hUT⟩ := S.cr_blowup_cauchy J hΘ (hHM hpH) hpcl hpD T'
  obtain ⟨x, hxU, hxD, hxT⟩ := mem_closure_iff_nhds.1 hp U hU
  linarith [hUT x ⟨hxU, hxD⟩]

/-! ### Step 5: the slice lower limit, with no properness and no local connectedness -/

/-- **Step 5, pointwise.** `q ∈ M ∩ closure D \ D ⟹ q ∈ KLi(S_τ)`: the tail of the curve lies in
`U`, and the levels `τ ≥ Θ(γ t₀)` are hit on that tail (Cauchy property + monotonicity of `Θ`). -/
theorem cr_mem_KLi_slice {Θ : V → ℝ} (hΘ : (S.Dsp J).FutCauchyTemporal Θ) {q : V}
    (hqM : q ∈ S.M) (hqcl : q ∈ closure (S.D J)) (hqD : q ∉ S.D J) :
    q ∈ KLi (S.slice J Θ) := by
  intro U hU
  obtain ⟨c, hlim, -, hchr⟩ := S.cr_curve J hqM hqcl hqD
  obtain ⟨t₀, ht₀⟩ := eventually_atTop.1 ((hlim.eventually hU).and (eventually_ge_atTop 0))
  have ht₀0 : 0 ≤ t₀ := (ht₀ t₀ le_rfl).2
  filter_upwards [eventually_ge_atTop (Θ (c.γ t₀))] with τ hτ
  obtain ⟨t, ht0, htτ⟩ :=
    hΘ.2 c τ ((S.curve_mono J hΘ.1 c hchr le_rfl ht₀0).trans hτ)
  have htt : t₀ ≤ t := by
    by_contra h
    rw [not_le] at h
    have := S.cr_temporalD_chr J hΘ.1 (hchr t t₀ ht0 h) (c.mem t₀ ht₀0)
    linarith
  exact ⟨c.γ t, ⟨c.mem t ht0, htτ⟩, (ht₀ t htt).1⟩

/-- **Step 5, `𝓗⁺ ⊆ KLi(S_τ)`.** Hypotheses: campaign 72's `hcl`, `𝓗⁺ ⊆ M`, and `Θ` Cauchy temporal
on `D` (future form). No `SublevelProper`, no `LocConnAt`, no separate continuity hypothesis.
Campaign 78: BUILT under the repaired `IsTemporal` (satisfiability: see `cr_slice_kuratowski`). -/
theorem cr_slice_lower_limit (hcl : closure (S.JpastSet J) ⊆ closure (S.D J))
    (hHM : S.H J ⊆ S.M) {Θ : V → ℝ} (hΘ : (S.Dsp J).FutCauchyTemporal Θ) :
    S.H J ⊆ KLi (S.slice J Θ) := fun _ hq =>
  S.cr_mem_KLi_slice J hΘ (hHM hq) (hcl (frontier_subset_closure hq)) (S.cr_not_mem_D_of_H J hq)

/-- Step 5 with sequences: `q = lim xₙ`, `xₙ ∈ S_{τₙ}`, `τₙ → ∞`. -/
theorem cr_slice_lower_limit_seq (hcl : closure (S.JpastSet J) ⊆ closure (S.D J))
    (hHM : S.H J ⊆ S.M) {Θ : V → ℝ} (hΘ : (S.Dsp J).FutCauchyTemporal Θ) {q : V}
    (hq : q ∈ S.H J) :
    ∃ τ : ℕ → ℝ, ∃ x : ℕ → V, Tendsto τ atTop atTop ∧ Tendsto x atTop (𝓝 q) ∧
      ∀ n, x n ∈ S.slice J Θ (τ n) := by
  have h : ∀ n : ℕ, ∃ τ ≥ (n:ℝ), ∃ x ∈ S.slice J Θ τ, x ∈ ball q (1 / ((n:ℝ) + 1)) := fun n =>
    ((S.cr_slice_lower_limit J hcl hHM hΘ hq _ (ball_mem_nhds q (by positivity))).and
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
`KLi(S_τ) = KLs(S_τ) = 𝓗⁺`. No properness, no local connectedness, no continuity hypothesis.

*Campaign 78:* re-derived under the repaired `IsTemporal` (BUILT). *Joint satisfiability:* `Θ` is
constrained on `D` only (`cr_isTemporal_congr`), so `r7641+71.1`'s contradiction (continuity of `Θ`
at `q ∈ 𝓗⁺` vs. `Θ → ∞` along `𝓝[D] q`, `cr_no_blowup_of_continuousAt`) is no longer derivable;
the concrete model with `𝓗⁺ ≠ ∅` is campaign 79's. -/
theorem cr_slice_kuratowski (hmono : ∀ s t : ℝ, s < t → S.Chr (O s) (O t))
    (hcl : closure (S.JpastSet J) ⊆ closure (S.D J))
    (hint : interior (S.JpastSet J) ⊆ S.D J) (hHM : S.H J ⊆ S.M) {Θ : V → ℝ} {c : ℝ}
    (hΘ : (S.Dsp J).FutCauchyTemporal Θ) (hadapt : ∀ τ, Θ (O τ) = τ + c) :
    KLi (S.slice J Θ) = S.H J ∧ KLs (S.slice J Θ) = S.H J := by
  have h1 := S.cr_slice_lower_limit J hcl hHM hΘ
  have h2 := (S.cr_slice_upper_limit hOD hadapt
    (fun x σ h => S.cr_temporalD_chr J hΘ.1 h (S.cr_observer_mem_D hOD hmono σ))).2 hint
  have h3 := cr_KLi_subset_KLs (S.slice J Θ)
  exact ⟨(h3.trans h2).antisymm h1, h2.antisymm (h1.trans h3)⟩

/-- **`prop:causal-alignment`, both halves**: under the same hypotheses, properness holds (so
campaign 74's hypothesis is a consequence) and the slices converge to `𝓗⁺`.

*Campaign 78:* re-derived under the repaired `IsTemporal` (BUILT); joint satisfiability as for
`cr_slice_kuratowski` (no continuity of `Θ` off `D` is assumed; model: campaign 79). -/
theorem cr_causal_alignment (hmono : ∀ s t : ℝ, s < t → S.Chr (O s) (O t))
    (hcl : closure (S.JpastSet J) ⊆ closure (S.D J))
    (hint : interior (S.JpastSet J) ⊆ S.D J) (hHM : S.H J ⊆ S.M) {Θ : V → ℝ} {c : ℝ}
    (hΘ : (S.Dsp J).FutCauchyTemporal Θ) (hadapt : ∀ τ, Θ (O τ) = τ + c) :
    S.SublevelProper J Θ ∧ KLi (S.slice J Θ) = S.H J ∧ KLs (S.slice J Θ) = S.H J :=
  ⟨S.cr_sublevelProper J hint hHM hΘ, S.cr_slice_kuratowski hOD hmono hcl hint hHM hΘ hadapt⟩

end Slices

/-! ## Campaign 78 ⓪: sanity of the repair

The repaired `IsTemporal` sees only `τ|_M` (`cr_isTemporal_congr`). Applied to `Dsp J`, it sees
only `Θ|_D`, and `𝓗⁺ ∩ D = ∅`. The vacuity of `r7641+71.1` came from continuity of `Θ` at a point of
`closure D` (`cr_no_blowup_of_continuousAt`); that continuity is no longer part of any
hypothesis. Toy consistency: `x ↦ x⁻¹` is `C¹` on the open `(0,∞)` and blows up at its boundary
point `0` (`cr_blowup_consistent_toy`). -/

/-- **The repaired temporality depends only on `τ|_M`.** -/
theorem cr_isTemporal_congr {τ τ' : V → ℝ} (h : ∀ x ∈ S.M, τ x = τ' x) :
    S.IsTemporal τ ↔ S.IsTemporal τ' := by
  have key : ∀ {τ τ' : V → ℝ}, (∀ x ∈ S.M, τ x = τ' x) → S.IsTemporal τ → S.IsTemporal τ' := by
    intro τ τ' h hτ
    refine ⟨hτ.1.congr fun x hx => (h x hx).symm, fun x hx v hv => ?_⟩
    have he : τ' =ᶠ[𝓝 x] τ := by
      filter_upwards [S.isOpen_M.mem_nhds hx] with y hy using (h y hy).symm
    rw [he.fderiv_eq]; exact hτ.2 x hx v hv
  exact ⟨key h, key fun x hx => (h x hx).symm⟩

open Classical in
/-- On `Dsp J`, a temporal `Θ` may be changed arbitrarily at a horizon point: its value (and its
continuity) there is not constrained. -/
theorem cr_isTemporal_update_H {Θ : V → ℝ} (hΘ : (S.Dsp J).IsTemporal Θ) {q : V}
    (hq : q ∈ S.H J) (b : ℝ) : (S.Dsp J).IsTemporal (Function.update Θ q b) := by
  refine ((S.Dsp J).cr_isTemporal_congr fun x hx => ?_).1 hΘ
  have hne : x ≠ q := fun h => S.cr_not_mem_D_of_H J hq (h ▸ hx)
  rw [Function.update_of_ne hne]

/-- **The vacuity mechanism** (`r7641+71.1`): a `Θ` continuous at `q ∈ closure D` cannot tend to
`∞` along `𝓝[D] q`. The old global `ContDiff` gave this continuity at every `q ∈ 𝓗⁺`; the repaired
definition gives continuity on `D` only (`cr_temporalD_continuousOn`). -/
theorem cr_no_blowup_of_continuousAt {Θ : V → ℝ} {q : V} (hq : q ∈ closure (S.D J))
    (hc : ContinuousAt Θ q) : ¬ Tendsto Θ (𝓝[S.D J] q) atTop := by
  have : (𝓝[S.D J] q).NeBot := mem_closure_iff_nhdsWithin_neBot.1 hq
  exact fun ht => not_tendsto_nhds_of_tendsto_atTop ht _ (hc.tendsto.mono_left nhdsWithin_le_nhds)

/-- What the repaired hypothesis gives: continuity on `D`, which contains no horizon point. -/
theorem cr_temporalD_continuousOn {Θ : V → ℝ} (hΘ : (S.Dsp J).IsTemporal Θ) :
    ContinuousOn Θ (S.D J) ∧ S.H J ∩ S.D J = ∅ :=
  ⟨hΘ.1.continuousOn, eq_empty_of_forall_notMem fun _ h => S.cr_not_mem_D_of_H J h.1 h.2⟩

/-- Toy consistency of "`C¹` on an open set, `→ ∞` at a boundary point": `x ⁻¹` on `(0, ∞)`. -/
theorem cr_blowup_consistent_toy :
    ContDiffOn ℝ 1 (fun x : ℝ => x⁻¹) (Ioi 0) ∧
      Tendsto (fun x : ℝ => x⁻¹) (𝓝[Ioi 0] 0) atTop ∧ (0:ℝ) ∈ closure (Ioi 0) \ Ioi 0 :=
  ⟨contDiffOn_inv ℝ |>.mono fun _ hx => ne_of_gt hx, tendsto_inv_nhdsGT_zero,
    by rw [closure_Ioi]; simp⟩

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
  have hc : Continuous fun z : V × ℝ => (S.seg z.1 z.2, S.T z.1) :=
    (continuous_fst.add (continuous_snd.smul (S.cont_T.comp continuous_fst))).prodMk
      (S.cont_T.comp continuous_fst)
  have hO := S.isOpen_timelikePairs.preimage hc
  exact isCompact_Icc.eventually_forall_of_forall_eventually
    (P := fun y r => S.seg y r ∈ S.M ∧ S.FutTimelike (S.seg y r) (S.T y))
    fun r hr => hO.mem_nhds (hε r hr)

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
theorem cr_past_extension {x : V} (hx : x ∈ S.M) :
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
      ((S.cont_T.tendsto q).comp hX).norm.eventually (lt_mem_nhds (by linarith))
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
theorem cr_futCauchy_of_cauchy {Θ : V → ℝ} (hΘ : S.IsCauchyTemporal Θ) : S.FutCauchyTemporal Θ := by
  refine ⟨hΘ.1, fun c a ha => ?_⟩
  obtain ⟨p, hpc, hp0, hpM, hpchr, hpd, hpinext⟩ := S.cr_past_extension (c.mem 0 le_rfl)
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
    have := S.cr_temporal_chr hΘ.1 (hpchr t h)
    linarith
  · exact ⟨t, h, by rw [← hγ0 t h]; exact ht⟩

/-- ② on the exterior: `(Dsp J).IsCauchyTemporal Θ → (Dsp J).FutCauchyTemporal Θ`. -/
theorem cr_futCauchy_of_cauchy_D {Θ : V → ℝ} (hΘ : (S.Dsp J).IsCauchyTemporal Θ) :
    (S.Dsp J).FutCauchyTemporal Θ :=
  (S.Dsp J).cr_futCauchy_of_cauchy hΘ

section SlicesGH
variable {S J} {O : ℝ → V} (hOD : S.IpastSet (range O) = S.D J)
include hOD

/-- **`prop:causal-alignment` under campaign 60's own definition** (`IsCauchyTemporal`, two-sided,
with the repaired `IsTemporal`): properness, and `KLi(S_τ) = KLs(S_τ) = 𝓗⁺`. BUILT, via ②.

*Joint satisfiability:* the hypotheses constrain `Θ` on `D` only (`cr_isTemporal_congr`), so the
vacuity mechanism of `r7641+71.1` (`cr_no_blowup_of_continuousAt`) no longer applies; a model with
`𝓗⁺ ≠ ∅` satisfying all of them is campaign 79's (not in this file). -/
theorem cr_causal_alignment_gh (hmono : ∀ s t : ℝ, s < t → S.Chr (O s) (O t))
    (hcl : closure (S.JpastSet J) ⊆ closure (S.D J))
    (hint : interior (S.JpastSet J) ⊆ S.D J) (hHM : S.H J ⊆ S.M) {Θ : V → ℝ} {c : ℝ}
    (hΘ : (S.Dsp J).IsCauchyTemporal Θ) (hadapt : ∀ τ, Θ (O τ) = τ + c) :
    S.SublevelProper J Θ ∧ KLi (S.slice J Θ) = S.H J ∧ KLs (S.slice J Θ) = S.H J :=
  S.cr_causal_alignment hOD hmono hcl hint hHM (S.cr_futCauchy_of_cauchy_D J hΘ) hadapt

end SlicesGH

/-- The two-sided hypothesis of `cr_causal_alignment_gh` gives campaign 60's `ExteriorGH`. -/
theorem cr_exteriorGH_of {Θ : V → ℝ} (hΘ : (S.Dsp J).IsCauchyTemporal Θ) : S.ExteriorGH J :=
  ⟨Θ, hΘ⟩



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

/-- The time-reversed chart: `T ↦ -T`. -/
def rev : Spacetime V where
  M := S.M
  isOpen_M := S.isOpen_M
  g := S.g
  cont_g := S.cont_g
  symm := S.symm
  T := fun x => -S.T x
  cont_T := S.cont_T.neg
  T_timelike x hx := by simpa using S.T_timelike x hx
  pos_on_perp x hx v hv hv0 := S.pos_on_perp x hx v (by simpa using hv) hv0

lemma rev_futTimelike {x v : V} (h : S.rev.FutTimelike x v) : S.FutTimelike x (-v) := by
  obtain ⟨h1, h2⟩ := h
  exact ⟨by simpa [rev] using h1, by simpa [rev] using h2⟩

/-- A timelike step of `rev`, run backwards, is a timelike step of `S`. -/
lemma rev_tstep {a b : V} (h : S.rev.TStep a b) : S.TStep b a := by
  obtain ⟨γ, hγ, h0, h1, hγt⟩ := h
  refine ⟨fun s => γ (1 - s), hγ.comp (contDiff_const.sub contDiff_id), by simp [h1],
    by simp [h0], fun s hs => ?_⟩
  have hd : deriv (fun s => γ (1 - s)) s = -deriv γ (1 - s) := by
    have h := (hasDerivAt_of_contDiff hγ (1 - s)).scomp s ((hasDerivAt_id s).const_sub 1)
    rw [show (fun s => γ (1 - s)) = γ ∘ HSub.hSub 1 from rfl, h.deriv]; simp
  obtain ⟨hm, hft⟩ := hγt (1 - s) ⟨by linarith [hs.2], by linarith [hs.1]⟩
  exact ⟨hm, hd ▸ S.rev_futTimelike hft⟩

lemma rev_chr {a b : V} (h : S.rev.Chr a b) : S.Chr b a := by
  induction h with
  | single h => exact Relation.TransGen.single (S.rev_tstep h)
  | tail _ h ih => exact Relation.TransGen.head (S.rev_tstep h) ih

/-- **Future polygonal extension** (① for `rev`, reversed): from `x ∈ M`, a continuous `p` with
`p 0 = x`, `x ≪ p t` for `t > 0`, future-timelike off the integers, no future limit in `M`. -/
theorem cr_future_extension {x : V} (hx : x ∈ S.M) :
    ∃ p : ℝ → V, Continuous p ∧ p 0 = x ∧ (∀ t, 0 ≤ t → p t ∈ S.M) ∧
      (∀ t, 0 < t → S.Chr x (p t)) ∧
      (∀ t, 0 < t → t ∉ range (Int.cast : ℤ → ℝ) →
        DifferentiableAt ℝ p t ∧ S.FutTimelike (p t) (deriv p t)) ∧
      ¬ ∃ q ∈ S.M, Tendsto p atTop (𝓝 q) := by
  obtain ⟨p, hpc, hp0, hpM, hpchr, hpd, hpinext⟩ := S.rev.cr_past_extension (x := x) hx
  refine ⟨fun t => p (-t), hpc.comp continuous_neg, by simp [hp0],
    fun t ht => hpM (-t) (by linarith), fun t ht => S.rev_chr (hpchr (-t) (by linarith)),
    fun t ht hb => ?_, ?_⟩
  · have hb' : -t ∉ range (Int.cast : ℤ → ℝ) := fun ⟨z, hz⟩ =>
      hb ⟨-z, by push_cast; rw [hz, neg_neg]⟩
    obtain ⟨hd, hft⟩ := hpd (-t) (by linarith) hb'
    have hD : HasDerivAt (fun t => p (-t)) (-deriv p (-t)) t := by
      have := hd.hasDerivAt.scomp t (hasDerivAt_neg t)
      simpa [Function.comp_def] using this
    exact ⟨hD.differentiableAt, hD.deriv ▸ S.rev_futTimelike hft⟩
  · rintro ⟨q, hq, hlim⟩
    exact hpinext ⟨q, hq, by simpa [Function.comp_def] using hlim.comp tendsto_neg_atBot_atTop⟩

/-- **Two-sided ⇒ past form** (mirror of ②, gluing the future extension at `0`). -/
theorem cr_pastCauchy_of_cauchy {Θ : V → ℝ} (hΘ : S.IsCauchyTemporal Θ) :
    S.PastCauchyTemporal Θ := by
  refine ⟨hΘ.1, fun c a ha => ?_⟩
  obtain ⟨p, hpc, hp0, hpM, hpchr, hpd, hpinext⟩ := S.cr_future_extension (c.mem 0 le_rfl)
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
    have := S.cr_temporal_chr hΘ.1 (hpchr t h)
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
theorem cr_strictMono_curve {Θ : V → ℝ} (hΘ : S.IsTemporal Θ) (c : S.InextCausalCurve) :
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
theorem cr_cauchy_iff {Θ : V → ℝ} :
    S.IsCauchyTemporal Θ ↔ S.FutCauchyTemporal Θ ∧ S.PastCauchyTemporal Θ := by
  refine ⟨fun h => ⟨S.cr_futCauchy_of_cauchy h, S.cr_pastCauchy_of_cauchy h⟩,
    fun ⟨hF, hP⟩ => ⟨hF.1, fun c a => ?_⟩⟩
  obtain ⟨t, ht⟩ : ∃ t, Θ (c.γ t) = a := by
    rcases le_total (Θ (c.γ 0)) a with h | h
    · obtain ⟨t, -, ht⟩ := hF.2 ⟨c.γ, c.cont.continuousOn, fun t _ => c.mem t, c.brk, c.brk_fin,
        fun t _ hb => c.causal t hb, c.inext_future⟩ a h
      exact ⟨t, ht⟩
    · obtain ⟨t, -, ht⟩ := hP.2 ⟨c.γ, c.cont.continuousOn, fun t _ => c.mem t, c.brk, c.brk_fin,
        fun t _ hb => c.causal t hb, c.inext_past⟩ a h
      exact ⟨t, ht⟩
  exact ⟨t, ht, fun s hs => (S.cr_strictMono_curve hF.1 c).injective (hs.trans ht.symm)⟩

end Spacetime

#print axioms Spacetime.cr_isOpen_Ipast
#print axioms Spacetime.cr_temporalD_chr
#print axioms Spacetime.cr_slice_upper_limit
#print axioms Spacetime.cr_sublevelProper_iff_tendsto
#print axioms Spacetime.cr_isOpen_Ifut
#print axioms Spacetime.cr_Ipast_subset_D
#print axioms Spacetime.cr_Ipast_subset_D_of_H
#print axioms Spacetime.cr_curve
#print axioms Spacetime.cr_blowup_cauchy
#print axioms Spacetime.cr_tendsto_atTop_H_cauchy
#print axioms Spacetime.cr_sublevelProper
#print axioms Spacetime.cr_mem_KLi_slice
#print axioms Spacetime.cr_slice_lower_limit
#print axioms Spacetime.cr_slice_lower_limit_seq
#print axioms Spacetime.cr_slice_kuratowski
#print axioms Spacetime.cr_causal_alignment
#print axioms Spacetime.temporal_curve
#print axioms Spacetime.cr_isTemporal_congr
#print axioms Spacetime.cr_isTemporal_update_H
#print axioms Spacetime.cr_no_blowup_of_continuousAt
#print axioms Spacetime.cr_temporalD_continuousOn
#print axioms Spacetime.cr_blowup_consistent_toy
#print axioms Spacetime.cr_past_extension
#print axioms Spacetime.cr_futCauchy_of_cauchy
#print axioms Spacetime.cr_futCauchy_of_cauchy_D
#print axioms Spacetime.cr_causal_alignment_gh
#print axioms Spacetime.cr_exteriorGH_of
#print axioms Spacetime.cr_future_extension
#print axioms Spacetime.cr_pastCauchy_of_cauchy
#print axioms Spacetime.cr_strictMono_curve
#print axioms Spacetime.cr_cauchy_iff

end ShadowProbe.CauchyRepairProbe

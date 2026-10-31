import Mathlib

/-!
# Probe `r7641+71.4` (campaign 79, `r7641` ③): slice tangency

Registration: `computations/formalisation/r7641_71_campaign79/PREDICTION.md`. Nothing imports this
file, and it imports no other probe.

## Copied

From campaign 75's `probes/CauchyProperness.lean`, renamed `cp_ ↦ st_`: `Spacetime`, `FutTimelike`,
`FutCausal`, `TStep`/`CStep`/`Chr`/`Cau`, `Ipast`/`Jpast`/`IpastSet`/`JpastSet`, the openness of
`I⁻(p)` (with `tube`, `tstep_start_eventually`), `st_chr_cau`, `D`, `H`, `slice`, `restrict`, `Dsp`,
`FutInextCurve`, `FutCauchyTemporal`, `KLi`, `KLs`. **`IsTemporal` is the repaired definition**
(`r7641+71.1`, campaign 78): `ContDiffOn ℝ 1 τ S.M ∧ ∀ x ∈ S.M, ∀ v, S.FutCausal x v → 0 < fderiv ℝ τ x v`.

## The model (used by every piece)

`P = ℝ × ℝ` in null coordinates `p = (U, V)`, `U = t − x`, `V = t + x`, so `−dt² + dx² = −dU dV`:
`g(a,b) = −(a_U b_V + a_V b_U)/2`, `T = ∂_t = (1,1)`, `M = ℝ²` (`Model.mink`). Future-causal means
`v_U, v_V ≥ 0`, not both `0` (`futCausal_iff`). `J = range O`, `O(σ) = (−e^{−σ}, e^{σ})` (the Rindler
hyperbola `U·V = −1`). Generator `ℓ = ∂_V = (0,1)`, transverse null `n = 2∂_U = (2,0)`,
`g(ℓ,ℓ) = g(n,n) = 0`, `g(ℓ,n) = −1` (`frame`).

## Results

**(1) The model — BUILT.**
- `st_model`: `D J = {U < 0}`, `𝓗⁺ = H J = {U = 0}`, `(0,0) ∈ 𝓗⁺`, `I⁻(range O) = D`, `O` future-
  timelike (`hmono`), `hcl`, `hint`, `𝓗⁺ ⊆ M`.
- `st_futCauchy`: for every profile `G` with `GoodG G` (`C¹` on `(0,∞)`, `G′ < 0`, `G → +∞` at `0⁺`,
  `G → −∞` at `+∞`), `Θ_G = G(−U) + V` is `FutCauchyTemporal` on `Dsp J` with the **repaired**
  `IsTemporal`. Proof as registered: `U`, `V` nondecreasing along a piecewise-`C¹` causal curve
  (`mono_brk`, induction on the number of break points), `Θ < a` forever ⟹ `U ≤ −δ < 0` and `V`
  bounded ⟹ monotone convergence to a point of `D`, contradicting inextendibility; then the IVT.
- `GoodG.st_adapted`: a reparametrisation `O' = O ∘ φ⁻¹` (`φ = Θ_G ∘ O`, a continuous strictly
  increasing surjection `ℝ → ℝ`) with `range O' = range O`, `I⁻(range O') = D`, `O'` future-timelike
  and `Θ_G(O' τ) = τ + 0`.
- `st_aligned`: `Θ₀ = −log(−U) + V` (`goodG_log`) is all of the above, and `dΘ₀(ℓ)/dΘ₀(n) = −U/2 → 0`
  at every horizon point, inside `D`.
So every hypothesis of campaign 75's `cp_causal_alignment` (`hOD`, `hmono`, `hcl`, `hint`, `hHM`,
`FutCauchyTemporal`, `hadapt`), with the repaired `IsTemporal`, holds here with `𝓗⁺ ≠ ∅`.
*Not done:* `cp_causal_alignment`'s conclusion is not re-proved in this file under the repaired
definition (that is campaign 78's file); only its hypotheses are shown satisfiable.

**(2) The failure — BUILT.** `st_tangency_fails`: `Θ = F(−U) + V`, `F(s) = −log s − sin(log s) − s`
(`goodG_Ffail`, `Θ_U = (1 + cos log s)/s + 1 ≥ 1`, `Θ_V = 1`) is future-Cauchy temporal on `D`,
adapted to a reparametrisation of `O`, and with `x_m = (−e^{−(2m+1)π}, 0) ∈ S_{Θ(x_m)}`:
`x_m → (0,0) ∈ 𝓗⁺`, `Θ(x_m) → ∞`, `dΘ(x_m) = dU + dV` for all `m`, `dΘ(x_m)(ℓ)/‖dΘ(x_m)‖ = 1/2`
(sup norm on `ℝ²`; the value is norm-dependent, its nonvanishing is not), so that ratio does not tend
to `0`; and `dΘ(ℓ)/dΘ(n)` does not tend to `0` as `x → (0,0)` within `D`.

**(3) The reduction — BUILT** (abstract linear algebra in null-frame components, `k` spatial
directions). `st_null_frame_bound`: if `ξ` (components `a = ξ(ℓ)`, `b = ξ(n)`, `c_i = ξ(e_i)`) is
positive on the future causal cone `{αℓ + βn + Σγ_i e_i | α, β ≥ 0, Σγ_i² ≤ 2αβ, (α,β) ≠ 0}`, then
`a, b > 0` and `Σ c_i² < 2ab`. `st_alignment_iff`: for a sequence of such covectors,
`(a_m/b_m → 0 ∧ ∀ i, c_{m,i}/b_m → 0) ↔ a_m/b_m → 0`. `st_frame_cone_model`: the cone hypothesis holds
(`k = 0`) for every `dΘ_G` at every point of `D` — so the reduction is not vacuous, and applies to
both `Θ₀` (ratio `→ 0`) and the failing `Θ` (ratio `1/2` along `x_m`).
*What the frame encoding assumes:* the covector is given by its frame components, and
`g(αℓ+βn+Σγe, ·) = −2αβ + Σγ²` is the definition of the cone; the frame itself is not built from a
general `g` (in the model it is `frame`).

## Why the hypotheses are satisfiable

All main theorems are about the explicit model, or (3a/3b) have hypotheses instantiated in the model
by `st_frame_cone_model`. `#print axioms` at the end: `[propext, Classical.choice, Quot.sound]`.
`set_option synthInstance.maxHeartbeats 400000` is used inside `Model` (the bilinear `g` on `ℝ²`).
-/
open Set Filter Topology Metric

namespace ShadowProbe.SliceTangencyProbe

/-! ## Copied from campaign 75 (`probes/CauchyProperness.lean`), `cp_ ↦ st_` -/

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

/-- `I⁻(p)` is open (campaign 75's `cp_isOpen_Ipast`). -/
theorem st_isOpen_Ipast (p : V) : IsOpen (S.Ipast p) := by
  refine isOpen_iff_mem_nhds.2 fun q hq => ?_
  obtain ⟨y, hqy, hyp⟩ := Relation.TransGen.head'_iff.1 hq
  filter_upwards [S.tstep_start_eventually hqy] with q' hq'
  exact Relation.TransGen.head' hq' hyp

lemma tstep_to_cstep {x y : V} (h : S.TStep x y) : S.CStep x y := by
  obtain ⟨γ, hγ, h0, h1, hγt⟩ := h
  exact ⟨γ, hγ, h0, h1, fun t ht => ⟨(hγt t ht).1, (hγt t ht).2.1.le, (hγt t ht).2.2⟩⟩

/-- `≪ ⊆ ≤`. -/
theorem st_chr_cau {x y : V} (h : S.Chr x y) : S.Cau x y := by
  induction h with
  | single h => exact Relation.ReflTransGen.single (S.tstep_to_cstep h)
  | tail _ h ih => exact ih.tail (S.tstep_to_cstep h)


/-- **Repaired** temporal function (campaign 78, `r7641+71.1`): `C¹` on `M` only, with
`dτ(v) > 0` for every future-causal `v` at points of `M`. -/
def IsTemporal (τ : V → ℝ) : Prop :=
  ContDiffOn ℝ 1 τ S.M ∧ ∀ x ∈ S.M, ∀ v, S.FutCausal x v → 0 < fderiv ℝ τ x v

variable (J : Set V)

/-- `D = I⁻(𝒥⁺)`. -/
def D : Set V := S.IpastSet J
/-- `𝓗⁺ = ∂J⁻(𝒥⁺)`. -/
def H : Set V := frontier (S.JpastSet J)
/-- A finite slice `S_τ = {x ∈ D | Θ x = τ}`. -/
def slice (Θ : V → ℝ) (τ : ℝ) : Set V := {x | x ∈ S.D J ∧ Θ x = τ}

/-- Points of `I⁻(z)` lie in `M`. -/
theorem st_Ipast_subset_M (z : V) : S.Ipast z ⊆ S.M := by
  intro q hq
  obtain ⟨b, ⟨γ, -, h0, -, hγ⟩, -⟩ := Relation.TransGen.head'_iff.1 hq
  rw [← h0]; exact (hγ 0 ⟨le_rfl, zero_le_one⟩).1

/-- `D` is open. -/
theorem st_D_open : IsOpen (S.D J) := isOpen_biUnion fun z _ => S.st_isOpen_Ipast z

/-- `D ⊆ M`. -/
theorem st_D_subset_M : S.D J ⊆ S.M := iUnion₂_subset fun z _ => S.st_Ipast_subset_M z

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

/-- The exterior `D` regarded as a spacetime in its own right. -/
def Dsp : Spacetime V := S.restrict (S.D J) (S.st_D_open J) (S.st_D_subset_M J)

/-- A future-directed piecewise-`C¹` causal curve on `[0, ∞)`, future-inextendible in `M`
(campaign 75). -/
structure FutInextCurve where
  γ : ℝ → V
  cont : ContinuousOn γ (Ici 0)
  mem : ∀ t, 0 ≤ t → γ t ∈ S.M
  brk : Set ℝ
  brk_fin : ∀ a b : ℝ, (brk ∩ Icc a b).Finite
  causal : ∀ t, 0 < t → t ∉ brk → DifferentiableAt ℝ γ t ∧ S.FutCausal (γ t) (deriv γ t)
  inext_future : ¬ ∃ p ∈ S.M, Tendsto γ atTop (𝓝 p)

/-- Cauchy temporal, future form (campaign 75), now with the repaired `IsTemporal`. -/
def FutCauchyTemporal (Θ : V → ℝ) : Prop :=
  S.IsTemporal Θ ∧ ∀ c : S.FutInextCurve, ∀ a : ℝ, Θ (c.γ 0) ≤ a → ∃ t, 0 ≤ t ∧ Θ (c.γ t) = a

end Spacetime

/-- Kuratowski lower limit of a family of sets as `τ → ∞`. -/
def KLi (A : ℝ → Set V) : Set V := {p | ∀ U ∈ 𝓝 p, ∀ᶠ τ in atTop, (A τ ∩ U).Nonempty}
/-- Kuratowski upper limit of a family of sets as `τ → ∞`. -/
def KLs (A : ℝ → Set V) : Set V := {p | ∀ U ∈ 𝓝 p, ∃ᶠ τ in atTop, (A τ ∩ U).Nonempty}

/-! ## (1) The model: 2D Minkowski in null coordinates, `J` the Rindler worldline

The chart is `P = ℝ × ℝ` with `p = (U, V)`, `U = t − x`, `V = t + x`. Then
`−dt² + dx² = −dU dV`, i.e. `g(a, b) = −(a_U b_V + a_V b_U)/2`, and `T = ∂_t = ∂_U + ∂_V = (1, 1)`.
`M` is the whole plane. -/

namespace Model
open ContinuousLinearMap

set_option synthInstance.maxHeartbeats 400000

/-- Null coordinates `p = (U, V)`. -/
abbrev P := ℝ × ℝ

/-- `g = −dU dV` (symmetrised). -/
noncomputable def gM : P →L[ℝ] P →L[ℝ] ℝ :=
  (-(1/2 : ℝ)) • ((fst ℝ ℝ ℝ).smulRight (snd ℝ ℝ ℝ) + (snd ℝ ℝ ℝ).smulRight (fst ℝ ℝ ℝ))

lemma gM_apply (v w : P) : gM v w = -(v.1 * w.2 + v.2 * w.1) / 2 := by
  simp [gM]; ring

/-- 2D Minkowski space, `M = ℝ²`, `T = ∂_t`. -/
noncomputable def mink : Spacetime P where
  M := univ
  isOpen_M := isOpen_univ
  g := fun _ => gM
  cont_g := continuous_const
  symm := fun _ v w => by rw [gM_apply, gM_apply]; ring
  T := fun _ => (1, 1)
  cont_T := continuous_const
  T_timelike := fun _ _ => by rw [gM_apply]; norm_num
  pos_on_perp := fun _ _ v h hv => by
    rw [gM_apply] at h ⊢
    have h2 : v.2 = -v.1 := by linarith
    have h1 : v.1 ≠ 0 := by
      intro h1; apply hv; ext
      · exact h1
      · rw [h2, h1]; simp
    rw [h2]; nlinarith [sq_pos_of_ne_zero h1]

/-- Future-causal in null coordinates: `v_U ≥ 0`, `v_V ≥ 0`, not both `0`. -/
lemma futCausal_iff (x v : P) : mink.FutCausal x v ↔ 0 ≤ v.1 ∧ 0 ≤ v.2 ∧ 0 < v.1 + v.2 := by
  show gM v v ≤ 0 ∧ gM v (1, 1) < 0 ↔ _
  rw [gM_apply, gM_apply]
  constructor
  · rintro ⟨h1, h2⟩
    have hs : 0 < v.1 + v.2 := by linarith
    have hp : 0 ≤ v.1 * v.2 := by linarith
    refine ⟨?_, ?_, hs⟩ <;> by_contra h <;> push Not at h <;> nlinarith
  · rintro ⟨h1, h2, h3⟩; constructor <;> nlinarith

/-- Future-timelike in null coordinates: `v_U > 0`, `v_V > 0`. -/
lemma futTimelike_iff (x v : P) : mink.FutTimelike x v ↔ 0 < v.1 ∧ 0 < v.2 := by
  show gM v v < 0 ∧ gM v (1, 1) < 0 ↔ _
  rw [gM_apply, gM_apply]
  constructor
  · rintro ⟨h1, h2⟩
    have hs : 0 < v.1 + v.2 := by linarith
    have hp : 0 < v.1 * v.2 := by linarith
    refine ⟨?_, ?_⟩ <;> by_contra h <;> push Not at h <;> nlinarith
  · rintro ⟨h1, h2⟩; constructor <;> nlinarith

lemma hasDerivAt_lin {γ : ℝ → P} (φ : P →L[ℝ] ℝ) {t : ℝ} (h : DifferentiableAt ℝ γ t) :
    HasDerivAt (fun t => φ (γ t)) (φ (deriv γ t)) t :=
  φ.hasFDerivAt.comp_hasDerivAt t h.hasDerivAt

lemma lin_le_of_step {γ : ℝ → P} (hγ : ContDiff ℝ 1 γ) (φ : P →L[ℝ] ℝ)
    (h : ∀ t ∈ Icc (0:ℝ) 1, 0 ≤ φ (deriv γ t)) : φ (γ 0) ≤ φ (γ 1) := by
  have hd : ∀ t, HasDerivAt (fun t => φ (γ t)) (φ (deriv γ t)) t := fun t =>
    hasDerivAt_lin φ ((hγ.differentiable one_ne_zero) t)
  have hm : MonotoneOn (fun t => φ (γ t)) (Icc (0:ℝ) 1) :=
    monotoneOn_of_deriv_nonneg (convex_Icc 0 1)
      (fun t _ => (hd t).continuousAt.continuousWithinAt)
      (fun t _ => (hd t).differentiableAt.differentiableWithinAt)
      (fun t ht => by
        rw [interior_Icc] at ht; rw [(hd t).deriv]; exact h t (Ioo_subset_Icc_self ht))
  exact hm ⟨le_rfl, zero_le_one⟩ ⟨zero_le_one, le_rfl⟩ zero_le_one

lemma lin_lt_of_step {γ : ℝ → P} (hγ : ContDiff ℝ 1 γ) (φ : P →L[ℝ] ℝ)
    (h : ∀ t ∈ Icc (0:ℝ) 1, 0 < φ (deriv γ t)) : φ (γ 0) < φ (γ 1) := by
  have hd : ∀ t, HasDerivAt (fun t => φ (γ t)) (φ (deriv γ t)) t := fun t =>
    hasDerivAt_lin φ ((hγ.differentiable one_ne_zero) t)
  have hm : StrictMonoOn (fun t => φ (γ t)) (Icc (0:ℝ) 1) :=
    strictMonoOn_of_deriv_pos (convex_Icc 0 1)
      (fun t _ => (hd t).continuousAt.continuousWithinAt)
      (fun t ht => by
        rw [interior_Icc] at ht; rw [(hd t).deriv]; exact h t (Ioo_subset_Icc_self ht))
  exact hm ⟨le_rfl, zero_le_one⟩ ⟨zero_le_one, le_rfl⟩ zero_lt_one

/-- `U` and `V` increase strictly along a timelike step. -/
lemma tstep_lt {x y : P} (h : mink.TStep x y) : x.1 < y.1 ∧ x.2 < y.2 := by
  obtain ⟨γ, hγ, h0, h1, hγt⟩ := h
  have k := fun t ht => (futTimelike_iff _ _).1 (hγt t ht).2
  subst h0 h1
  exact ⟨by simpa using lin_lt_of_step hγ (fst ℝ ℝ ℝ) (fun t ht => by simpa using (k t ht).1),
    by simpa using lin_lt_of_step hγ (snd ℝ ℝ ℝ) (fun t ht => by simpa using (k t ht).2)⟩

/-- `U` and `V` do not decrease along a causal step. -/
lemma cstep_le {x y : P} (h : mink.CStep x y) : x.1 ≤ y.1 ∧ x.2 ≤ y.2 := by
  obtain ⟨γ, hγ, h0, h1, hγt⟩ := h
  have k := fun t ht => (futCausal_iff _ _).1 (hγt t ht).2
  subst h0 h1
  exact ⟨by simpa using lin_le_of_step hγ (fst ℝ ℝ ℝ) (fun t ht => by simpa using (k t ht).1),
    by simpa using lin_le_of_step hγ (snd ℝ ℝ ℝ) (fun t ht => by simpa using (k t ht).2.1)⟩

lemma chr_lt {x y : P} (h : mink.Chr x y) : x.1 < y.1 ∧ x.2 < y.2 := by
  induction h with
  | single h => exact tstep_lt h
  | tail _ h ih => exact ⟨ih.1.trans (tstep_lt h).1, ih.2.trans (tstep_lt h).2⟩

lemma cau_le {x y : P} (h : mink.Cau x y) : x.1 ≤ y.1 ∧ x.2 ≤ y.2 := by
  induction h with
  | refl => exact ⟨le_rfl, le_rfl⟩
  | tail _ h ih => exact ⟨ih.1.trans (cstep_le h).1, ih.2.trans (cstep_le h).2⟩

/-- The straight segment is a timelike step when both null coordinates increase. -/
lemma tstep_of_lt {x y : P} (h1 : x.1 < y.1) (h2 : x.2 < y.2) : mink.TStep x y := by
  refine ⟨fun t => x + t • (y - x), contDiff_const.add (contDiff_id.smul contDiff_const),
    by simp, by simp, fun t _ => ⟨mem_univ _, ?_⟩⟩
  have hd : deriv (fun t : ℝ => x + t • (y - x)) t = y - x := by
    have h : HasDerivAt (fun t : ℝ => x + t • (y - x)) ((1:ℝ) • (y - x)) t :=
      ((hasDerivAt_id' t).smul_const (y - x)).const_add x
    rw [h.deriv, one_smul]
  rw [hd, futTimelike_iff]
  simp only [Prod.fst_sub, Prod.snd_sub, sub_pos]
  exact ⟨h1, h2⟩

/-- The Rindler worldline `O(σ) = (U, V) = (−e^{−σ}, e^{σ})`, on `U·V = −1`. -/
noncomputable def O (σ : ℝ) : P := (-Real.exp (-σ), Real.exp σ)

lemma O_UV (σ : ℝ) : (O σ).1 * (O σ).2 = -1 := by
  simp only [O, neg_mul, ← Real.exp_add, neg_add_cancel, Real.exp_zero]

/-- `O` is future-timelike: `O s ≪ O t` for `s < t`. -/
theorem st_O_mono (s t : ℝ) (h : s < t) : mink.Chr (O s) (O t) := by
  refine Relation.TransGen.single (tstep_of_lt ?_ ?_)
  · simp only [O, neg_lt_neg_iff, Real.exp_lt_exp]; linarith
  · simp only [O, Real.exp_lt_exp]; exact h

/-- **`D = {U < 0}`.** -/
theorem st_D_eq : mink.D (range O) = {p : P | p.1 < 0} := by
  ext p
  simp only [Spacetime.D, Spacetime.IpastSet, mem_iUnion, mem_ofPred_eq, Spacetime.Ipast,
    exists_prop]
  constructor
  · rintro ⟨_, ⟨σ, rfl⟩, h⟩
    have h1 := (chr_lt h).1
    have h2 : 0 < Real.exp (-σ) := Real.exp_pos _
    simp only [O] at h1; linarith
  · intro hp
    have e1 : ∀ᶠ σ in atTop, Real.exp (-σ) < -p.1 :=
      (tendsto_order.1 Real.tendsto_exp_neg_atTop_nhds_zero).2 _ (by linarith)
    have e2 : ∀ᶠ σ in atTop, p.2 < Real.exp σ := Real.tendsto_exp_atTop.eventually_gt_atTop p.2
    obtain ⟨σ, h1, h2⟩ := (e1.and e2).exists
    exact ⟨O σ, mem_range_self σ, Relation.TransGen.single
      (tstep_of_lt (by simp only [O]; linarith) h2)⟩

/-- `J⁻(𝒥⁺) = {U < 0}` too. -/
theorem st_JpastSet_eq : mink.JpastSet (range O) = {p : P | p.1 < 0} := by
  apply Subset.antisymm
  · intro p hp
    simp only [Spacetime.JpastSet, mem_iUnion, Spacetime.Jpast, mem_ofPred_eq, exists_prop] at hp
    obtain ⟨_, ⟨σ, rfl⟩, h⟩ := hp
    have h1 := (cau_le h).1
    have h2 : 0 < Real.exp (-σ) := Real.exp_pos _
    show p.1 < 0
    simp only [O] at h1; linarith
  · rw [← st_D_eq]
    intro p hp
    simp only [Spacetime.D, Spacetime.IpastSet, Spacetime.JpastSet, mem_iUnion] at hp ⊢
    obtain ⟨z, hz, h⟩ := hp
    exact ⟨z, hz, mink.st_chr_cau h⟩

/-- **`𝓗⁺ = {U = 0}`.** -/
theorem st_H_eq : mink.H (range O) = {p : P | p.1 = 0} := by
  have h := (IsOpenMap.preimage_frontier_eq_frontier_preimage (f := (Prod.fst : P → ℝ))
    isOpenMap_fst continuous_fst (Iio (0:ℝ))).symm
  rw [Spacetime.H, st_JpastSet_eq]
  have e : {p : P | p.1 < 0} = Prod.fst ⁻¹' Iio 0 := rfl
  rw [e, h, frontier_Iio]
  rfl

/-- **(1) The model meets the geometric hypotheses of `cp_causal_alignment`, with `𝓗⁺ ≠ ∅`.** -/
theorem st_model :
    mink.D (range O) = {p : P | p.1 < 0} ∧ mink.H (range O) = {p : P | p.1 = 0} ∧
    ((0, 0) : P) ∈ mink.H (range O) ∧
    mink.IpastSet (range O) = mink.D (range O) ∧
    (∀ s t : ℝ, s < t → mink.Chr (O s) (O t)) ∧
    closure (mink.JpastSet (range O)) ⊆ closure (mink.D (range O)) ∧
    interior (mink.JpastSet (range O)) ⊆ mink.D (range O) ∧
    mink.H (range O) ⊆ mink.M := by
  refine ⟨st_D_eq, st_H_eq, by rw [st_H_eq]; rfl, rfl, st_O_mono, ?_, ?_, subset_univ _⟩
  · rw [st_JpastSet_eq, st_D_eq]
  · rw [st_JpastSet_eq, st_D_eq]; exact interior_subset

/-! ## Temporal functions `Θ = G(−U) + V` on `D` and their future Cauchy property -/

/-- `Θ_G(U, V) = G(−U) + V`. -/
noncomputable def ThetaG (G : ℝ → ℝ) (p : P) : ℝ := G (-p.1) + p.2

/-- Conditions on the profile `G` (on `s = −U > 0`). -/
structure GoodG (G : ℝ → ℝ) : Prop where
  cdiff : ContDiffOn ℝ 1 G (Ioi 0)
  deriv_neg : ∀ s, 0 < s → deriv G s < 0
  tendsto_zero : Tendsto G (𝓝[>] 0) atTop
  tendsto_top : Tendsto G atTop atBot

/-- The derivative `dΘ_G = −G′(−U) dU + dV`. -/
noncomputable def dTh (G : ℝ → ℝ) (p : P) : P →L[ℝ] ℝ :=
  deriv G (-p.1) • (-(fst ℝ ℝ ℝ)) + snd ℝ ℝ ℝ

lemma dTh_apply (G : ℝ → ℝ) (p v : P) : dTh G p v = deriv G (-p.1) * (-v.1) + v.2 := by
  simp [dTh]

namespace GoodG
variable {G : ℝ → ℝ} (hG : GoodG G)
include hG

lemma hasDerivAt {s : ℝ} (hs : 0 < s) : HasDerivAt G (deriv G s) s :=
  ((hG.cdiff.differentiableOn one_ne_zero s hs).differentiableAt (Ioi_mem_nhds hs)).hasDerivAt

lemma hasFDerivAt {p : P} (hp : p.1 < 0) : HasFDerivAt (ThetaG G) (dTh G p) p := by
  have h1 : HasFDerivAt (fun p : P => -p.1) (-(fst ℝ ℝ ℝ)) p := hasFDerivAt_fst.neg
  have h2 := (hG.hasDerivAt (s := -p.1) (by linarith)).comp_hasFDerivAt p h1
  exact h2.add hasFDerivAt_snd

lemma fderiv_eq {p : P} (hp : p.1 < 0) : fderiv ℝ (ThetaG G) p = dTh G p :=
  (hG.hasFDerivAt hp).fderiv

lemma contDiffOn : ContDiffOn ℝ 1 (ThetaG G) {p : P | p.1 < 0} := by
  have h1 : ContDiffOn ℝ 1 (fun p : P => G (-p.1)) {p : P | p.1 < 0} :=
    hG.cdiff.comp (contDiff_fst.neg.contDiffOn) (fun p (hp : p.1 < 0) => by
      show 0 < -p.1; linarith)
  exact h1.add contDiff_snd.contDiffOn

lemma anti : StrictAntiOn G (Ioi 0) :=
  strictAntiOn_of_deriv_neg (convex_Ioi 0) hG.cdiff.continuousOn
    (fun x hx => by rw [interior_Ioi] at hx; exact hG.deriv_neg x hx)

/-- `G(s) ≤ K` forces `s ≥ δ > 0`. -/
lemma lower (K : ℝ) : ∃ δ > 0, ∀ s, 0 < s → G s ≤ K → δ ≤ s := by
  obtain ⟨u, hu, hsub⟩ :=
    (mem_nhdsGT_iff_exists_Ioo_subset).1 (hG.tendsto_zero.eventually_gt_atTop K)
  refine ⟨u, hu, fun s hs hK => le_of_not_gt fun hsu => ?_⟩
  have : K < G s := hsub ⟨hs, hsu⟩
  linarith

/-- `Θ_G` is temporal on `{U < 0}`: `dΘ_G(v) = (−G′) v_U + v_V > 0` for future-causal `v`. -/
lemma dTh_pos {p : P} (hp : p.1 < 0) {v : P} (hv : mink.FutCausal p v) : 0 < dTh G p v := by
  rw [dTh_apply]
  obtain ⟨h1, h2, h3⟩ := (futCausal_iff _ _).1 hv
  have hd := hG.deriv_neg (-p.1) (by linarith)
  rcases h1.eq_or_lt with h | h
  · rw [← h]; simp only [neg_zero, mul_zero, zero_add]; linarith
  · nlinarith

end GoodG

/-- Monotonicity of a function continuous on `[0, ∞)` with nonnegative derivative off a locally
finite set of break points. -/
lemma mono_brk {f : ℝ → ℝ} {B : Set ℝ} (hB : ∀ a b, (B ∩ Icc a b).Finite)
    (hf : ContinuousOn f (Ici 0))
    (hd : ∀ t, 0 < t → t ∉ B → DifferentiableAt ℝ f t ∧ 0 ≤ deriv f t) :
    MonotoneOn f (Ici 0) := by
  have hfin : ∀ a b, (B ∩ Ioo a b).Finite := fun a b =>
    (hB a b).subset (inter_subset_inter_right _ Ioo_subset_Icc_self)
  have base : ∀ a b, 0 ≤ a → a ≤ b → B ∩ Ioo a b = ∅ → f a ≤ f b := by
    intro a b ha hab he
    have hm : MonotoneOn f (Icc a b) := by
      refine monotoneOn_of_deriv_nonneg (convex_Icc a b)
        (hf.mono fun t ht => le_trans ha ht.1) (fun t ht => ?_) (fun t ht => ?_)
      all_goals
        rw [interior_Icc] at ht
        have htB : t ∉ B := fun h => (he ▸ (⟨h, ht⟩ : t ∈ B ∩ Ioo a b) : t ∈ (∅ : Set ℝ))
        have := hd t (by linarith [ht.1]) htB
      · exact this.1.differentiableWithinAt
      · exact this.2
    exact hm ⟨le_rfl, hab⟩ ⟨hab, le_rfl⟩ hab
  have key : ∀ n : ℕ, ∀ a b, 0 ≤ a → a ≤ b → (B ∩ Ioo a b).ncard ≤ n → f a ≤ f b := by
    intro n
    induction n with
    | zero =>
      intro a b ha hab hn
      exact base a b ha hab ((Set.ncard_eq_zero (hfin a b)).1 (Nat.le_zero.1 hn))
    | succ n ih =>
      intro a b ha hab hn
      by_cases he : B ∩ Ioo a b = ∅
      · exact base a b ha hab he
      obtain ⟨c, hcB, hc⟩ := nonempty_iff_ne_empty.2 he
      have h1 : (B ∩ Ioo a c).ncard ≤ n := by
        have : B ∩ Ioo a c ⊂ B ∩ Ioo a b :=
          (ssubset_iff_of_subset (inter_subset_inter_right _
            (Ioo_subset_Ioo_right hc.2.le))).2 ⟨c, ⟨hcB, hc⟩, fun h => lt_irrefl c h.2.2⟩
        have := Set.ncard_lt_ncard this (hfin a b)
        omega
      have h2 : (B ∩ Ioo c b).ncard ≤ n := by
        have : B ∩ Ioo c b ⊂ B ∩ Ioo a b :=
          (ssubset_iff_of_subset (inter_subset_inter_right _
            (Ioo_subset_Ioo_left hc.1.le))).2 ⟨c, ⟨hcB, hc⟩, fun h => lt_irrefl c h.2.1⟩
        have := Set.ncard_lt_ncard this (hfin a b)
        omega
      exact (ih a c ha hc.1.le h1).trans (ih c b (ha.trans hc.1.le) hc.2.le h2)
  intro a ha b hb hab
  exact key _ a b ha hab le_rfl

/-- **Future Cauchy property in the model.** For a good profile `G`, `Θ_G = G(−U) + V` is
`FutCauchyTemporal` on `D` (with the repaired `IsTemporal`). Along a future-inextendible causal
curve in `D`, `U` and `V` are nondecreasing; if `Θ` stayed below `a`, then `V` and `U` would be
bounded (`U ≤ −δ` by the blow-up of `G` at `0⁺`), so the curve would converge to a point with
`U < 0`, i.e. in `D`, contradicting inextendibility; so some `Θ(γ T) ≥ a`, and the IVT. -/
theorem st_futCauchy {G : ℝ → ℝ} (hG : GoodG G) :
    (mink.Dsp (range O)).FutCauchyTemporal (ThetaG G) := by
  have hM : (mink.Dsp (range O)).M = {p : P | p.1 < 0} := st_D_eq
  refine ⟨⟨hM ▸ hG.contDiffOn, fun x hx v hv => ?_⟩, fun c a ha => ?_⟩
  · rw [hM] at hx
    rw [hG.fderiv_eq hx]
    exact hG.dTh_pos hx hv
  have hmem : ∀ t, 0 ≤ t → (c.γ t).1 < 0 := fun t ht => by
    have := c.mem t ht; rw [hM] at this; exact this
  have hcaus : ∀ t, 0 < t → t ∉ c.brk →
      DifferentiableAt ℝ c.γ t ∧ 0 ≤ (deriv c.γ t).1 ∧ 0 ≤ (deriv c.γ t).2 := by
    intro t ht hb
    obtain ⟨hd, hc⟩ := c.causal t ht hb
    obtain ⟨h1, h2, -⟩ := (futCausal_iff (c.γ t) _).1 hc
    exact ⟨hd, h1, h2⟩
  have hU : MonotoneOn (fun t => (c.γ t).1) (Ici 0) := by
    refine mono_brk c.brk_fin (continuous_fst.comp_continuousOn c.cont) fun t ht hb => ?_
    obtain ⟨hd, h1, -⟩ := hcaus t ht hb
    have h := hasDerivAt_lin (fst ℝ ℝ ℝ) hd
    refine ⟨h.differentiableAt, ?_⟩
    change 0 ≤ deriv (fun t => (fst ℝ ℝ ℝ) (c.γ t)) t
    rw [h.deriv]; simpa using h1
  have hV : MonotoneOn (fun t => (c.γ t).2) (Ici 0) := by
    refine mono_brk c.brk_fin (continuous_snd.comp_continuousOn c.cont) fun t ht hb => ?_
    obtain ⟨hd, -, h2⟩ := hcaus t ht hb
    have h := hasDerivAt_lin (snd ℝ ℝ ℝ) hd
    refine ⟨h.differentiableAt, ?_⟩
    change 0 ≤ deriv (fun t => (snd ℝ ℝ ℝ) (c.γ t)) t
    rw [h.deriv]; simpa using h2
  have hcont : ContinuousOn (fun t => ThetaG G (c.γ t)) (Ici 0) :=
    hG.contDiffOn.continuousOn.comp c.cont (fun t ht => hmem t ht)
  suffices h : ∃ T, 0 ≤ T ∧ a ≤ ThetaG G (c.γ T) by
    obtain ⟨T, hT, haT⟩ := h
    obtain ⟨t, ht, hta⟩ := intermediate_value_Icc hT (hcont.mono Icc_subset_Ici_self) ⟨ha, haT⟩
    exact ⟨t, ht.1, hta⟩
  by_contra hno
  push Not at hno
  have h0 : (0:ℝ) ∈ Ici (0:ℝ) := mem_Ici.2 le_rfl
  obtain ⟨δ, hδ, hδs⟩ := hG.lower (a - (c.γ 0).2)
  have hUle : ∀ t, 0 ≤ t → (c.γ t).1 ≤ -δ := by
    intro t ht
    have h1 := hno t ht
    have h2 : (c.γ 0).2 ≤ (c.γ t).2 := hV h0 ht ht
    unfold ThetaG at h1
    have := hδs (-(c.γ t).1) (by linarith [hmem t ht]) (by linarith)
    linarith
  have hVle : ∀ t, 0 ≤ t → (c.γ t).2 ≤ a - G (-(c.γ 0).1) := by
    intro t ht
    have h1 := hno t ht
    have hU0 : (c.γ 0).1 ≤ (c.γ t).1 := hU h0 ht ht
    have hanti : G (-(c.γ 0).1) ≤ G (-(c.γ t).1) := by
      rcases hU0.eq_or_lt with h | h
      · rw [h]
      · exact (hG.anti (show (0:ℝ) < -(c.γ t).1 by linarith [hmem t ht])
          (show (0:ℝ) < -(c.γ 0).1 by linarith [hmem 0 le_rfl]) (by linarith)).le
    unfold ThetaG at h1
    linarith
  set u : ℝ → ℝ := fun t => (c.γ (max t 0)).1 with hu
  set w : ℝ → ℝ := fun t => (c.γ (max t 0)).2 with hw
  have hum : Monotone u := fun x y hxy =>
    hU (le_max_right x 0) (le_max_right y 0) (max_le_max hxy le_rfl)
  have hwm : Monotone w := fun x y hxy =>
    hV (le_max_right x 0) (le_max_right y 0) (max_le_max hxy le_rfl)
  have hub : BddAbove (range u) :=
    ⟨-δ, by rintro _ ⟨t, rfl⟩; exact hUle _ (le_max_right _ _)⟩
  have hwb : BddAbove (range w) :=
    ⟨a - G (-(c.γ 0).1), by rintro _ ⟨t, rfl⟩; exact hVle _ (le_max_right _ _)⟩
  have hlim : Tendsto c.γ atTop (𝓝 ((⨆ t, u t), (⨆ t, w t))) := by
    have h := (tendsto_atTop_ciSup hum hub).prodMk_nhds (tendsto_atTop_ciSup hwm hwb)
    refine h.congr' ?_
    filter_upwards [eventually_ge_atTop 0] with t ht
    simp [u, w, max_eq_left ht]
  apply c.inext_future
  refine ⟨_, ?_, hlim⟩
  rw [hM]
  show (⨆ t, u t) < 0
  exact lt_of_le_of_lt (ciSup_le fun t => hUle _ (le_max_right _ _)) (by linarith)

/-! ### Adaptation: reparametrise `O` so that `Θ(O' τ) = τ` -/

/-- `φ(σ) = Θ_G(O σ) = G(e^{−σ}) + e^{σ}`. -/
noncomputable def phiG (G : ℝ → ℝ) (σ : ℝ) : ℝ := ThetaG G (O σ)

lemma phiG_eq (G : ℝ → ℝ) (σ : ℝ) : phiG G σ = G (Real.exp (-σ)) + Real.exp σ := by
  simp [phiG, ThetaG, O]

namespace GoodG
variable {G : ℝ → ℝ} (hG : GoodG G)
include hG

lemma phiG_strictMono : StrictMono (phiG G) := by
  intro s t hst
  rw [phiG_eq, phiG_eq]
  have h1 : Real.exp (-t) < Real.exp (-s) := Real.exp_lt_exp.2 (by linarith)
  have h2 := hG.anti (Real.exp_pos (-t)) (Real.exp_pos (-s)) h1
  have h3 : Real.exp s < Real.exp t := Real.exp_lt_exp.2 hst
  linarith

lemma phiG_surjective : Function.Surjective (phiG G) := by
  have he : (phiG G) = fun σ => G (Real.exp (-σ)) + Real.exp σ := funext (phiG_eq G)
  rw [he]
  refine Continuous.surjective ?_ ?_ ?_
  · exact (hG.cdiff.continuousOn.comp_continuous (Real.continuous_exp.comp continuous_neg)
      (fun σ => Real.exp_pos _)).add Real.continuous_exp
  · have hexp0 : Tendsto (fun σ => Real.exp (-σ)) atTop (𝓝[>] 0) :=
      tendsto_nhdsWithin_iff.2 ⟨Real.tendsto_exp_neg_atTop_nhds_zero,
        Eventually.of_forall fun _ => Real.exp_pos _⟩
    exact (hG.tendsto_zero.comp hexp0).atTop_add_atTop Real.tendsto_exp_atTop
  · exact (hG.tendsto_top.comp (Real.tendsto_exp_atTop.comp tendsto_neg_atBot_atTop)).atBot_add
      Real.tendsto_exp_atBot

/-- **Adaptation.** A reparametrisation `O'` of the Rindler worldline, with the same range, still
future-timelike, along which `Θ_G(O' τ) = τ`. -/
theorem st_adapted : ∃ O' : ℝ → P, range O' = range O ∧
    mink.IpastSet (range O') = mink.D (range O) ∧
    (∀ s t : ℝ, s < t → mink.Chr (O' s) (O' t)) ∧ ∀ τ, ThetaG G (O' τ) = τ + 0 := by
  have hs := hG.phiG_surjective
  have hm := hG.phiG_strictMono
  set ψ := Function.surjInv hs
  have hψ : ∀ τ, phiG G (ψ τ) = τ := Function.surjInv_eq hs
  have hrange : range (fun τ => O (ψ τ)) = range O := by
    apply Subset.antisymm
    · rintro _ ⟨τ, rfl⟩; exact mem_range_self _
    · rintro _ ⟨σ, rfl⟩
      exact ⟨phiG G σ, by show O (ψ (phiG G σ)) = O σ; rw [hm.injective (hψ (phiG G σ))]⟩
  refine ⟨fun τ => O (ψ τ), hrange, by rw [hrange]; rfl, fun s t hst => st_O_mono _ _ ?_,
    fun τ => by rw [add_zero]; exact hψ τ⟩
  rw [← hm.lt_iff_lt, hψ, hψ]; exact hst

end GoodG

/-! ## The aligned `Θ₀ = −log(−U) + V` and the failing `Θ = F(−U) + V` -/

/-- `G₀(s) = −log s`. -/
lemma goodG_log : GoodG fun s => -Real.log s where
  cdiff := Real.contDiffOn_log.neg.mono fun s (hs : 0 < s) => by simpa using hs.ne'
  deriv_neg s hs := by
    have h : HasDerivAt (fun s => -Real.log s) (-s⁻¹) s := (Real.hasDerivAt_log hs.ne').neg
    rw [h.deriv]
    simpa using hs
  tendsto_zero := tendsto_neg_atBot_atTop.comp Real.tendsto_log_nhdsGT_zero
  tendsto_top := tendsto_neg_atTop_atBot.comp Real.tendsto_log_atTop

/-- The failing profile `F(s) = −log s − sin(log s) − s`. -/
noncomputable def Ffail (s : ℝ) : ℝ := -Real.log s - Real.sin (Real.log s) - s

lemma Ffail_hasDerivAt {s : ℝ} (hs : 0 < s) :
    HasDerivAt Ffail (-s⁻¹ - Real.cos (Real.log s) * s⁻¹ - 1) s := by
  have hl := Real.hasDerivAt_log hs.ne'
  exact (hl.neg.sub ((Real.hasDerivAt_sin (Real.log s)).comp s hl)).sub (hasDerivAt_id s)

lemma goodG_Ffail : GoodG Ffail where
  cdiff := fun s (hs : 0 < s) => by
    have hl := Real.contDiffAt_log (n := 1).2 hs.ne'
    exact ((hl.neg.sub (Real.contDiff_sin.contDiffAt.comp s hl)).sub
      contDiffAt_id).contDiffWithinAt
  deriv_neg s hs := by
    rw [(Ffail_hasDerivAt hs).deriv]
    have hi := inv_pos.2 hs
    nlinarith [Real.neg_one_le_cos (Real.log s)]
  tendsto_zero := by
    have h1 : Tendsto (fun s => -Real.log s + -2) (𝓝[>] 0) atTop :=
      tendsto_atTop_add_const_right _ (-2)
        (tendsto_neg_atBot_atTop.comp Real.tendsto_log_nhdsGT_zero)
    refine tendsto_atTop_mono' _ ?_ h1
    filter_upwards [Ioo_mem_nhdsGT (zero_lt_one' ℝ)] with s hs
    simp only [Ffail]
    nlinarith [Real.sin_le_one (Real.log s), hs.2]
  tendsto_top := by
    have h1 : Tendsto (fun s : ℝ => 1 + -s) atTop atBot :=
      tendsto_atBot_add_const_left _ 1 tendsto_neg_atTop_atBot
    refine tendsto_atBot_mono' _ ?_ h1
    filter_upwards [eventually_ge_atTop 1] with s hs
    simp only [Ffail]
    nlinarith [Real.neg_one_le_sin (Real.log s), Real.log_nonneg hs]

/-- The aligned slicing function `Θ₀ = −log(−U) + V`. -/
noncomputable def Θ₀ : P → ℝ := ThetaG fun s => -Real.log s
/-- The failing slicing function `Θ = F(−U) + V`. -/
noncomputable def Θf : P → ℝ := ThetaG Ffail

/-- The generator direction `ℓ = ∂_V` of `𝓗⁺ = {U = 0}`. -/
def ℓ : P := (0, 1)
/-- The transverse null vector `n = 2∂_U`, normalised by `g(ℓ, n) = −1`. -/
def nvec : P := (2, 0)

lemma frame : gM ℓ ℓ = 0 ∧ gM nvec nvec = 0 ∧ gM ℓ nvec = -1 := by
  simp only [gM_apply, ℓ, nvec]; norm_num

/-! ### The aligned `Θ₀` -/

/-- **`Θ₀` is non-vacuous and aligned.** It is future-Cauchy temporal on `D`, adapted to a
reparametrisation of `O`, and `dΘ₀(ℓ)/dΘ₀(n) = −U/2 → 0` at every horizon point. -/
theorem st_aligned :
    (mink.Dsp (range O)).FutCauchyTemporal Θ₀ ∧
    (∃ O' : ℝ → P, range O' = range O ∧ mink.IpastSet (range O') = mink.D (range O) ∧
      (∀ s t : ℝ, s < t → mink.Chr (O' s) (O' t)) ∧ ∀ τ, Θ₀ (O' τ) = τ + 0) ∧
    ∀ q ∈ mink.H (range O), Tendsto (fun p => fderiv ℝ Θ₀ p ℓ / fderiv ℝ Θ₀ p nvec)
      (𝓝[mink.D (range O)] q) (𝓝 0) := by
  refine ⟨st_futCauchy goodG_log, goodG_log.st_adapted, fun q hq => ?_⟩
  rw [st_H_eq] at hq
  have hq' : q.1 = 0 := hq
  have hc : Tendsto (fun p : P => -p.1 / 2) (𝓝[mink.D (range O)] q) (𝓝 0) := by
    have := ((continuous_fst.neg.div_const (2:ℝ)).tendsto q).mono_left
      (nhdsWithin_le_nhds (s := mink.D (range O)))
    simpa [hq'] using this
  refine hc.congr' ?_
  filter_upwards [self_mem_nhdsWithin] with p hp
  rw [st_D_eq] at hp
  have hp' : p.1 < 0 := hp
  have hs : (0:ℝ) < -p.1 := by linarith
  unfold Θ₀
  have hl : HasDerivAt (fun s => -Real.log s) (-(-p.1)⁻¹) (-p.1) :=
    (Real.hasDerivAt_log hs.ne').neg
  rw [goodG_log.fderiv_eq hp', dTh_apply, dTh_apply, hl.deriv]
  simp only [ℓ, nvec]
  have hne : p.1 ≠ 0 := hp'.ne
  field_simp
  ring

/-! ### (2) The failure -/

/-- `s_m = e^{−(2m+1)π}`. -/
noncomputable def sm (m : ℕ) : ℝ := Real.exp (-((2 * m + 1) * Real.pi))
/-- `x_m = (U, V) = (−s_m, 0)`. -/
noncomputable def xm (m : ℕ) : P := (-sm m, 0)

lemma log_sm (m : ℕ) : Real.log (sm m) = -((2 * m + 1) * Real.pi) := Real.log_exp _

lemma cos_log_sm (m : ℕ) : Real.cos (Real.log (sm m)) = -1 := by
  rw [log_sm, Real.cos_neg]
  have : (2 * (m:ℝ) + 1) * Real.pi = Real.pi + m * (2 * Real.pi) := by ring
  rw [this, Real.cos_add_nat_mul_two_pi, Real.cos_pi]

lemma sin_log_sm (m : ℕ) : Real.sin (Real.log (sm m)) = 0 := by
  rw [log_sm, Real.sin_neg]
  have : (2 * (m:ℝ) + 1) * Real.pi = Real.pi + m * (2 * Real.pi) := by ring
  rw [this, Real.sin_add_nat_mul_two_pi, Real.sin_pi, neg_zero]

lemma deriv_Ffail_sm (m : ℕ) : deriv Ffail (sm m) = -1 := by
  have hs : 0 < sm m := Real.exp_pos _
  rw [(Ffail_hasDerivAt hs).deriv, cos_log_sm]
  ring

lemma xm_mem (m : ℕ) : (xm m).1 < 0 := by
  simp only [xm, Left.neg_neg_iff]; exact Real.exp_pos _

/-- At `x_m`, `dΘ = dU + dV`. -/
lemma fderiv_xm (m : ℕ) : fderiv ℝ Θf (xm m) = fst ℝ ℝ ℝ + snd ℝ ℝ ℝ := by
  unfold Θf
  rw [goodG_Ffail.fderiv_eq (xm_mem m)]
  ext <;> simp [dTh_apply, xm, deriv_Ffail_sm]

lemma Θf_xm (m : ℕ) : Θf (xm m) = (2 * m + 1) * Real.pi - sm m := by
  simp only [Θf, ThetaG, xm, neg_neg, Ffail]
  rw [sin_log_sm, log_sm]
  ring

lemma norm_fst_add_snd : ‖fst ℝ ℝ ℝ + snd ℝ ℝ ℝ‖ = 2 := by
  apply le_antisymm
  · refine ContinuousLinearMap.opNorm_le_bound _ (by norm_num) fun v => ?_
    simp only [add_apply, coe_fst', coe_snd', Real.norm_eq_abs]
    have h1 := norm_fst_le v
    have h2 := norm_snd_le v
    rw [Real.norm_eq_abs] at h1 h2
    calc |v.1 + v.2| ≤ |v.1| + |v.2| := abs_add_le _ _
      _ ≤ 2 * ‖v‖ := by linarith
  · have h := (fst ℝ ℝ ℝ + snd ℝ ℝ ℝ).le_opNorm ((1, 1) : P)
    have hn : ‖((1, 1) : P)‖ = 1 := by simp [Prod.norm_def]
    rw [hn] at h
    simp only [add_apply, coe_fst', coe_snd', Real.norm_eq_abs] at h
    norm_num at h
    linarith

/-- **(2) The failure of tangency.** `Θ = F(−U) + V`, `F(s) = −log s − sin(log s) − s`, is future-
Cauchy temporal on `D` (repaired definition) and adapted to a reparametrisation of the Rindler
worldline; `(0,0) ∈ 𝓗⁺`; the points `x_m = (−e^{−(2m+1)π}, 0) ∈ D` lie on the slices
`S_{Θ(x_m)}` with `Θ(x_m) → ∞` and `x_m → (0,0)`; yet `dΘ(x_m) = dU + dV` for every `m`, so
`dΘ(ℓ)/‖dΘ‖ = 1/2` along the sequence (does not tend to `0`), and the frame ratio
`dΘ(ℓ)/dΘ(n)` does not tend to `0` as `x → (0,0)` in `D`. -/
theorem st_tangency_fails :
    (mink.Dsp (range O)).FutCauchyTemporal Θf ∧
    (∃ O' : ℝ → P, range O' = range O ∧ mink.IpastSet (range O') = mink.D (range O) ∧
      (∀ s t : ℝ, s < t → mink.Chr (O' s) (O' t)) ∧ ∀ τ, Θf (O' τ) = τ + 0) ∧
    ((0, 0) : P) ∈ mink.H (range O) ∧
    (∀ m, xm m ∈ mink.slice (range O) Θf (Θf (xm m))) ∧
    Tendsto xm atTop (𝓝 (0, 0)) ∧
    Tendsto (fun m => Θf (xm m)) atTop atTop ∧
    (∀ m, fderiv ℝ Θf (xm m) = fst ℝ ℝ ℝ + snd ℝ ℝ ℝ) ∧
    (∀ m, fderiv ℝ Θf (xm m) ℓ / ‖fderiv ℝ Θf (xm m)‖ = 1 / 2) ∧
    ¬ Tendsto (fun m => fderiv ℝ Θf (xm m) ℓ / ‖fderiv ℝ Θf (xm m)‖) atTop (𝓝 0) ∧
    ¬ Tendsto (fun p => fderiv ℝ Θf p ℓ / fderiv ℝ Θf p nvec)
      (𝓝[mink.D (range O)] (0, 0)) (𝓝 0) := by
  have hratio : ∀ m, fderiv ℝ Θf (xm m) ℓ / ‖fderiv ℝ Θf (xm m)‖ = 1 / 2 := fun m => by
    rw [fderiv_xm, norm_fst_add_snd]; simp [ℓ]
  have hmemD : ∀ m, xm m ∈ mink.D (range O) := fun m => by rw [st_D_eq]; exact xm_mem m
  have hsm : Tendsto sm atTop (𝓝 0) := by
    refine Real.tendsto_exp_atBot.comp ?_
    refine tendsto_neg_atTop_atBot.comp ?_
    refine Tendsto.atTop_mul_const Real.pi_pos ?_
    exact tendsto_atTop_add_const_right _ 1
      (Tendsto.const_mul_atTop two_pos tendsto_natCast_atTop_atTop)
  have hx : Tendsto xm atTop (𝓝 (0, 0)) := by
    have := (hsm.neg).prodMk_nhds (tendsto_const_nhds (x := (0:ℝ)))
    rw [neg_zero] at this
    exact this
  refine ⟨st_futCauchy goodG_Ffail, goodG_Ffail.st_adapted, by rw [st_H_eq]; rfl,
    fun m => ⟨hmemD m, rfl⟩, hx, ?_, fderiv_xm, hratio, ?_, ?_⟩
  · have hle : ∀ m : ℕ, (2 * m + 1) * Real.pi - 1 ≤ Θf (xm m) := fun m => by
      rw [Θf_xm]
      have : sm m ≤ 1 := Real.exp_le_one_iff.2 (by
        have := Real.pi_pos; have : (0:ℝ) ≤ m := m.cast_nonneg; nlinarith)
      linarith
    refine tendsto_atTop_mono hle ?_
    refine tendsto_atTop_add_const_right _ (-1) ?_
    refine Tendsto.atTop_mul_const Real.pi_pos ?_
    exact tendsto_atTop_add_const_right _ 1
      (Tendsto.const_mul_atTop two_pos tendsto_natCast_atTop_atTop)
  · intro h
    have := tendsto_nhds_unique h (by simp only [hratio]; exact tendsto_const_nhds)
    norm_num at this
  · intro h
    have hxD : Tendsto xm atTop (𝓝[mink.D (range O)] (0, 0)) :=
      tendsto_nhdsWithin_iff.2 ⟨hx, Eventually.of_forall hmemD⟩
    have h2 := h.comp hxD
    have hval : ∀ m, fderiv ℝ Θf (xm m) ℓ / fderiv ℝ Θf (xm m) nvec = 1 / 2 := fun m => by
      rw [fderiv_xm]; simp [ℓ, nvec]
    have := tendsto_nhds_unique h2 (by
      simp only [Function.comp_def, hval]; exact tendsto_const_nhds)
    norm_num at this

end Model

/-! ## (3) The null-frame reduction (linear algebra)

A covector `ξ` is recorded by its components in a null frame `ℓ, n` (`g(ℓ,ℓ) = g(n,n) = 0`,
`g(ℓ,n) = −1`, both future) and spatial orthonormal `e_i ⊥ ℓ, n` (`i : Fin k`):
`a = ξ(ℓ)`, `b = ξ(n)`, `c_i = ξ(e_i)`. A vector `v = αℓ + βn + Σ γ_i e_i` has
`g(v,v) = −2αβ + Σ γ_i²`, so the future causal cone is `{α, β ≥ 0, Σ γ_i² ≤ 2αβ, v ≠ 0}` (and
`v ≠ 0 ⟺ α ≠ 0 ∨ β ≠ 0` on it). "`ξ` temporal at the point" is positivity on that cone. -/

/-- **(3a)** Positivity of `ξ` on the future causal cone ⟹ `a, b > 0` and `Σ c_i² < 2ab`. -/
theorem st_null_frame_bound {k : ℕ} (a b : ℝ) (c : Fin k → ℝ)
    (h : ∀ α β : ℝ, ∀ γ : Fin k → ℝ, 0 ≤ α → 0 ≤ β → ∑ i, γ i ^ 2 ≤ 2 * α * β →
      (α ≠ 0 ∨ β ≠ 0) → 0 < α * a + β * b + ∑ i, γ i * c i) :
    0 < a ∧ 0 < b ∧ ∑ i, c i ^ 2 < 2 * a * b := by
  have ha : 0 < a := by simpa using h 1 0 0 zero_le_one le_rfl (by simp) (by simp)
  have hb : 0 < b := by simpa using h 0 1 0 le_rfl zero_le_one (by simp) (by simp)
  refine ⟨ha, hb, ?_⟩
  set C := ∑ i, c i ^ 2 with hC
  have hC0 : 0 ≤ C := Finset.sum_nonneg fun i _ => sq_nonneg _
  rcases hC0.eq_or_lt with h0 | h0
  · rw [← h0]; positivity
  have hsum : ∑ i, (-c i) ^ 2 = C := by simp [hC]
  have hsum2 : ∑ i, (-c i) * c i = -C := by
    simp [hC, Finset.sum_neg_distrib, sq]
  have key := h (C / (2 * a)) a (fun i => -c i) (by positivity) ha.le
    (by rw [hsum]; field_simp; rfl) (Or.inr ha.ne')
  rw [hsum2] at key
  have e : C / (2 * a) * a = C / 2 := by field_simp
  rw [e] at key
  linarith

/-- **(3b)** For a sequence of covectors each positive on the future causal cone,
alignment with the generator, i.e. `ξ_m / ξ_m(n) → (0, 1, 0) = −g(ℓ,·)` in frame components
(`a_m/b_m → 0` and every `c_{m,i}/b_m → 0`), holds **iff** `a_m/b_m → 0`. -/
theorem st_alignment_iff {k : ℕ} (a b : ℕ → ℝ) (c : ℕ → Fin k → ℝ)
    (h : ∀ m, ∀ α β : ℝ, ∀ γ : Fin k → ℝ, 0 ≤ α → 0 ≤ β → ∑ i, γ i ^ 2 ≤ 2 * α * β →
      (α ≠ 0 ∨ β ≠ 0) → 0 < α * a m + β * b m + ∑ i, γ i * c m i) :
    (Tendsto (fun m => a m / b m) atTop (𝓝 0) ∧
      ∀ i, Tendsto (fun m => c m i / b m) atTop (𝓝 0)) ↔
    Tendsto (fun m => a m / b m) atTop (𝓝 0) := by
  refine ⟨fun h' => h'.1, fun hab => ⟨hab, fun i => ?_⟩⟩
  have hbd : ∀ m, (c m i / b m) ^ 2 ≤ 2 * (a m / b m) := by
    intro m
    obtain ⟨ham, hbm, hC⟩ := st_null_frame_bound (a m) (b m) (c m) (h m)
    have hci : c m i ^ 2 ≤ ∑ j, c m j ^ 2 :=
      Finset.single_le_sum (f := fun j => c m j ^ 2) (fun j _ => sq_nonneg _)
        (Finset.mem_univ i)
    rw [div_pow, div_le_iff₀ (by positivity)]
    have : 2 * (a m / b m) * b m ^ 2 = 2 * a m * b m := by field_simp
    rw [this]; linarith
  have hsq : Tendsto (fun m => (c m i / b m) ^ 2) atTop (𝓝 0) := by
    have h2 : Tendsto (fun m => 2 * (a m / b m)) atTop (𝓝 0) := by
      simpa using hab.const_mul 2
    exact squeeze_zero (fun m => sq_nonneg _) hbd h2
  have habs : Tendsto (fun m => |c m i / b m|) atTop (𝓝 0) := by
    have := (Real.continuous_sqrt.tendsto 0).comp hsq
    simpa [Function.comp_def, Real.sqrt_sq_eq_abs] using this
  exact (tendsto_zero_iff_abs_tendsto_zero _).2 habs


/-- **(3c) The reduction's hypothesis holds in the model** (`k = 0`): for every good profile `G`
and every `p ∈ D = {U < 0}`, the frame components `a = dΘ_G(ℓ)`, `b = dΘ_G(n)` are positive on the
future causal cone. So (3a)/(3b) apply to `Θ₀` and to the failing `Θ` (where `a/b = 1/2` along
`x_m`). -/
theorem st_frame_cone_model {G : ℝ → ℝ} (hG : Model.GoodG G) {p : Model.P} (hp : p.1 < 0) :
    ∀ α β : ℝ, ∀ γ : Fin 0 → ℝ, 0 ≤ α → 0 ≤ β → ∑ i, γ i ^ 2 ≤ 2 * α * β → (α ≠ 0 ∨ β ≠ 0) →
      0 < α * Model.dTh G p Model.ℓ + β * Model.dTh G p Model.nvec +
        ∑ i, γ i * (fun _ : Fin 0 => (0:ℝ)) i := by
  intro α β γ hα hβ _ hne
  have hpos : 0 < 2 * β + α := by
    rcases hne with h | h
    · have := lt_of_le_of_ne hα (Ne.symm h); linarith
    · have := lt_of_le_of_ne hβ (Ne.symm h); linarith
  have hv := hG.dTh_pos hp (v := (2 * β, α))
    ((Model.futCausal_iff p _).2 ⟨by simp only; linarith, hα, by simp only; linarith⟩)
  rw [Model.dTh_apply] at hv
  simp only [Model.dTh_apply, Model.ℓ, Model.nvec, Finset.univ_eq_empty, Finset.sum_empty,
    add_zero] at hv ⊢
  linarith

#print axioms Model.st_model
#print axioms Model.st_futCauchy
#print axioms Model.GoodG.st_adapted
#print axioms Model.st_aligned
#print axioms Model.st_tangency_fails
#print axioms st_null_frame_bound
#print axioms st_alignment_iff
#print axioms st_frame_cone_model

end ShadowProbe.SliceTangencyProbe

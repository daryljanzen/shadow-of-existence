import Mathlib

/-!
# Probe `r7633+71.2` (campaign 70, `r7633` ②): Christoffel symbols, pregeodesics, and the
# corner-cutting lemma; the tangency clause of `prop:causal-alignment` (stretch)

Registration: `computations/formalisation/r7633_71_campaign70/PREDICTION.md`. Nothing imports this
file, and it imports no other probe. The `Spacetime` structure, the causal relations and the
openness lemmas for `I±` are copied from `probes/CausalStructure.lean` (campaign 60) under the
namespace `ShadowProbe.CornerCuttingProbe`; every theorem here carries the prefix `ct_`.

## Setting (single chart)

* `V` is a finite-dimensional real normed space and `M ⊆ V` is open.
* `g : V → (V →L[ℝ] V →L[ℝ] ℝ)` is symmetric and Lorentzian in the sense of campaign 60: a
  continuous time orientation `T` with `g(T,T) < 0` and `g` positive definite on `T^⊥`.
* Regularity: everything below needs only **`g ∈ C¹`** (hypothesis `ContDiff ℝ 1 S.g`), and the
  curves are `C²`. The registered `C²` metric is therefore more than is used.

## ① Christoffel symbols (BUILT)

* `ct_nondegenerate`: `g_x` is nondegenerate for `x ∈ M`. This is *proved* from the Lorentzian
  structure, not assumed. If `g(z,·) = 0` then `g(z,T) = 0` and `g(z,z) = 0`, so `z = 0`.
* `ct_flat_surjective`: in finite dimension the musical map `♭ : V → V*` is onto.
* `Γ x u v` is defined as `♭⁻¹` of the Koszul covector
  `w ↦ ½(Dg(u)(v,w) + Dg(v)(u,w) − Dg(w)(u,v))`, where `Dg x w u v = (Dg_x · w)(u,v)`.
  - Defining identity: `ct_christoffel_koszul`.
  - Uniqueness: `ct_christoffel_unique`.
  - Symmetry: `ct_christoffel_symm`.
* `acc γ t = γ'' t + Γ(γ t)(γ' t, γ' t)`, and `IsPregeodesicAt` / `IsPregeodesicOn` say
  `acc ∥ γ'`.
* Metric compatibility along a curve: `ct_metric_compat`, `d/dt g(γ',γ') = 2 g(γ', acc)`.
  The general form, for any vector field `W` along `γ`, is `ct_deriv_g_vel_field`:
  `d/dt g(γ',W) = g(acc,W) + g(γ',W') + ½ Dg(W)(γ',γ')`.
* First variation: `ct_first_variation`. For `γ_ε = γ + εW`,
  `∂_ε|₀ g(γ_ε',γ_ε') = Dg(W)(γ',γ') + 2 g(γ',W') = 2 d/dt g(γ',W) − 2 g(acc,W)`.

## ② The corner-cutting lemma (BUILT): `ct_corner_cutting`

If `γ` is `C²`, future causal on `[a,b]` (in particular future null), and `acc t₀ ∉ ℝ·γ' t₀` at an
interior `t₀`, then there are `a < s < t₀ < t < b` with `γ(s) ≪ γ(t)`. No push-up is needed: the
endpoints are kept fixed. The proof runs as follows.
1. `ct_exists_transverse`. Since `acc ∉ ℝγ'` and `g` is nondegenerate, there is `Z₀` with
   `g(γ',Z₀) = 0` and `c₀ := g(acc,Z₀) > 0`. This uses the `T`-component trick and does not need
   `γ'` to be null.
2. Take `Z(r) = Z₀ + (r−t₀)·μT`, with `μ` chosen so that `e(t₀) = −c₀/2`, where
   `e = ½Dg(Z)(γ',γ') + g(γ',Z')`. By Koszul, `h := g(γ',Z)` then has `h(t₀) = 0` and
   `h'(t₀) = c₀ + e(t₀) = c₀/2 > 0`.
3. On a small `[s,t] = [t₀−δ,t₀+δ]` we have `h' > 0` and `e < 0`. With `φ = (r−s)(t−r)` and
   `W = φZ`, the first variation is `2(φ'h + φe)`, which is `< 0` on all of `[s,t]`,
   **endpoints included**. At the endpoints `φ = 0`, but `φ'h < 0` because `h` changes sign at
   `t₀` together with `φ'`.
4. `ct_variation_chr`. If the first variation is `< 0` on the compact `[s,t]` and `γ` is causal
   there, then by a tube lemma and the mean value theorem in `ε` the curve `γ + εW` is
   future-timelike on `[s,t]` for one small `ε > 0`. It has the same endpoints, so after an
   affine reparametrisation to `[0,1]` it is a `TStep`.

## ③ Stretch: the tangency clause (BUILT IN PART)

* `ct_H_achronal`. The horizon `H = ∂J⁻(J)` is achronal. This needs no push-up, only openness of
  `I±` and `I ⊆ J`.
* `ct_achronal_null` and `ct_achronal_pregeodesic`. A `C²` future-causal curve with no two
  chronologically related points is null and a pregeodesic at every interior parameter.
* `ct_H_generator_null_pregeodesic`. Hence **a `C²` causal curve lying in `H` (a `C²`
  generator) is a null pregeodesic.** This is the first half of the tangency clause, given
  generator regularity.
* REPORTED, not built:
  - The *hypothesis* that generators are `C²`. Campaign 69 gives only Lipschitz generators. The
    first missing lemma is regularity of achronal-boundary generators: a Lipschitz causal curve
    in `∂J⁻(S) \ S` is, after reparametrisation, a `C²` null geodesic. Classically it is proved
    *through* the local corner-cutting for Lipschitz curves, i.e. a version of
    `ct_corner_cutting` for curves that are only a.e. differentiable. That needs the
    Lipschitz-curve re-founding of the causal relations named in campaign 60.
  - The accumulation `∂J⁻(O(τ)) → 𝓗⁺`, e.g. Hausdorff on compacts. The first missing lemma is
    the limit-curve theorem, the closedness of the causal-curve condition under uniform limits,
    as in campaign 60.
-/

open Set Filter Topology Metric

namespace ShadowProbe.CornerCuttingProbe

variable {V : Type*} [NormedAddCommGroup V] [NormedSpace ℝ V]

/-- A time-oriented Lorentzian chart (copied from campaign 60's `CausalStructure`). -/
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

/-- One `C¹` future-timelike piece from `x` to `y`, parametrised by `[0,1]`. -/
def TStep (x y : V) : Prop :=
  ∃ γ : ℝ → V, ContDiff ℝ 1 γ ∧ γ 0 = x ∧ γ 1 = y ∧
    ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ S.M ∧ S.FutTimelike (γ t) (deriv γ t)

/-- One `C¹` future-causal piece from `x` to `y`, parametrised by `[0,1]`. -/
def CStep (x y : V) : Prop :=
  ∃ γ : ℝ → V, ContDiff ℝ 1 γ ∧ γ 0 = x ∧ γ 1 = y ∧
    ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ S.M ∧ S.FutCausal (γ t) (deriv γ t)

/-- Chronological relation `x ≪ y`. -/
def Chr (x y : V) : Prop := Relation.TransGen S.TStep x y
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

lemma ct_cont_gvw {X : Type*} [TopologicalSpace X] {x v w : X → V} (hx : Continuous x)
    (hv : Continuous v) (hw : Continuous w) : Continuous fun a => S.g (x a) (v a) (w a) :=
  ((S.cont_g.comp hx).clm_apply hv).clm_apply hw

lemma ct_isOpen_timelikePairs :
    IsOpen {pv : V × V | pv.1 ∈ S.M ∧ S.FutTimelike pv.1 pv.2} := by
  refine (S.isOpen_M.preimage continuous_fst).inter (IsOpen.inter ?_ ?_)
  · exact isOpen_lt (S.ct_cont_gvw continuous_fst continuous_snd continuous_snd) continuous_const
  · exact isOpen_lt (S.ct_cont_gvw continuous_fst continuous_snd
      (S.cont_T.comp continuous_fst)) continuous_const

lemma ct_tube {P Q : V → ℝ → V} (hP : Continuous fun z : V × ℝ => P z.1 z.2)
    (hQ : Continuous fun z : V × ℝ => Q z.1 z.2)
    (h0 : ∀ t ∈ Icc (0:ℝ) 1, P 0 t ∈ S.M ∧ S.FutTimelike (P 0 t) (Q 0 t)) :
    ∀ᶠ w in 𝓝 (0:V), ∀ t ∈ Icc (0:ℝ) 1, P w t ∈ S.M ∧ S.FutTimelike (P w t) (Q w t) := by
  refine isCompact_Icc.eventually_forall_of_forall_eventually fun t ht => ?_
  have hO := S.ct_isOpen_timelikePairs.preimage (hP.prodMk hQ)
  exact hO.mem_nhds (h0 t ht)

lemma ct_hasDerivAt_of_contDiff {γ : ℝ → V} (hγ : ContDiff ℝ 1 γ) (t : ℝ) :
    HasDerivAt γ (deriv γ t) t :=
  ((hγ.differentiable one_ne_zero) t).hasDerivAt

lemma ct_tstep_end_eventually {y q : V} (h : S.TStep y q) : ∀ᶠ q' in 𝓝 q, S.TStep y q' := by
  obtain ⟨γ, hγ, h0, h1, hγt⟩ := h
  have hdc : Continuous (deriv γ) := hγ.continuous_deriv le_rfl
  have hT := S.ct_tube (P := fun w t => γ t + t • w) (Q := fun w t => deriv γ t + w)
    ((hγ.continuous.comp continuous_snd).add (continuous_snd.smul continuous_fst))
    ((hdc.comp continuous_snd).add continuous_fst) (by simpa using hγt)
  have hlim : Tendsto (fun q' => q' - q) (𝓝 q) (𝓝 0) := tendsto_sub_nhds_zero_iff.2 tendsto_id
  filter_upwards [hlim.eventually hT] with q' hq'
  refine ⟨fun t => γ t + t • (q' - q), hγ.add (contDiff_id.smul contDiff_const), by simp [h0],
    by simp [h1], fun t ht => ?_⟩
  have hd : deriv (fun t => γ t + t • (q' - q)) t = deriv γ t + (q' - q) := by
    have h : HasDerivAt (fun t => γ t + t • (q' - q)) (deriv γ t + (1:ℝ) • (q' - q)) t :=
      (ct_hasDerivAt_of_contDiff hγ t).add ((hasDerivAt_id' t).smul_const (q' - q))
    rw [h.deriv, one_smul]
  rw [hd]; exact hq' t ht

lemma ct_tstep_start_eventually {p y : V} (h : S.TStep p y) : ∀ᶠ p' in 𝓝 p, S.TStep p' y := by
  obtain ⟨γ, hγ, h0, h1, hγt⟩ := h
  have hdc : Continuous (deriv γ) := hγ.continuous_deriv le_rfl
  have hT := S.ct_tube (P := fun w t => γ t + (1 - t) • w) (Q := fun w t => deriv γ t - w)
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
      (ct_hasDerivAt_of_contDiff hγ t).add
        (((hasDerivAt_const t (1:ℝ)).sub (hasDerivAt_id' t)).smul_const (p' - p))
    rw [h.deriv, zero_sub, neg_one_smul, ← sub_eq_add_neg]
  rw [hd]; exact hp' t ht

theorem ct_isOpen_Ifut (p : V) : IsOpen (S.Ifut p) := by
  refine isOpen_iff_mem_nhds.2 fun q hq => ?_
  obtain ⟨y, hpy, hyq⟩ := Relation.TransGen.tail'_iff.1 hq
  filter_upwards [S.ct_tstep_end_eventually hyq] with q' hq'
  exact Relation.TransGen.tail' hpy hq'

theorem ct_isOpen_Ipast (p : V) : IsOpen (S.Ipast p) := by
  refine isOpen_iff_mem_nhds.2 fun q hq => ?_
  obtain ⟨y, hqy, hyp⟩ := Relation.TransGen.head'_iff.1 hq
  filter_upwards [S.ct_tstep_start_eventually hqy] with q' hq'
  exact Relation.TransGen.head' hq' hyp

lemma ct_tstep_to_cstep {x y : V} (h : S.TStep x y) : S.CStep x y := by
  obtain ⟨γ, hγ, h0, h1, hγt⟩ := h
  exact ⟨γ, hγ, h0, h1, fun t ht => ⟨(hγt t ht).1, (hγt t ht).2.1.le, (hγt t ht).2.2⟩⟩

theorem ct_chr_cau {x y : V} (h : S.Chr x y) : S.Cau x y := by
  induction h with
  | single h => exact Relation.ReflTransGen.single (S.ct_tstep_to_cstep h)
  | tail _ h ih => exact ih.tail (S.ct_tstep_to_cstep h)

/-! ## ① Nondegeneracy, the musical isomorphism, Christoffel symbols -/

/-- `g_x` is nondegenerate on `M`, proved from the Lorentzian structure. -/
theorem ct_nondegenerate {x : V} (hx : x ∈ S.M) {z : V} (hz : ∀ w, S.g x z w = 0) : z = 0 := by
  by_contra hne
  have h := S.pos_on_perp x hx z (hz _) hne
  rw [hz z] at h
  exact lt_irrefl _ h

/-- `Dg x w u v = (Dg_x · w)(u, v)`, the derivative of the metric in direction `w`. -/
noncomputable def Dg (x w u v : V) : ℝ := fderiv ℝ S.g x w u v

lemma ct_Dg_smul (x w u v : V) (c : ℝ) : S.Dg x (c • w) u v = c * S.Dg x w u v := by
  simp [Dg]

lemma ct_cont_Dg {X : Type*} [TopologicalSpace X] (hg : ContDiff ℝ 1 S.g) {x w u v : X → V}
    (hx : Continuous x) (hw : Continuous w) (hu : Continuous u) (hv : Continuous v) :
    Continuous fun a => S.Dg (x a) (w a) (u a) (v a) :=
  ((((hg.continuous_fderiv one_ne_zero).comp hx).clm_apply hw).clm_apply hu).clm_apply hv

/-- The derivative of a symmetric metric is symmetric in its last two slots. -/
theorem ct_Dg_symm (x w u v : V) : S.Dg x w u v = S.Dg x w v u := by
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

/-- The musical map `♭ : z ↦ g_x(z, ·)` into the algebraic dual. -/
noncomputable def flat (x : V) : V →ₗ[ℝ] Module.Dual ℝ V where
  toFun z := (S.g x z : V →ₗ[ℝ] ℝ)
  map_add' z₁ z₂ := by ext w; simp
  map_smul' c z := by ext w; simp

/-- In finite dimension, `♭` is onto at every point of `M`. -/
theorem ct_flat_surjective [FiniteDimensional ℝ V] {x : V} (hx : x ∈ S.M) :
    Function.Surjective (S.flat x) := by
  have hinj : Function.Injective (S.flat x) := by
    rw [← LinearMap.ker_eq_bot, LinearMap.ker_eq_bot']
    intro z hz
    exact S.ct_nondegenerate hx fun w => by simpa [flat] using LinearMap.congr_fun hz w
  exact (LinearMap.injective_iff_surjective_of_finrank_eq_finrank
    Subspace.dual_finrank_eq.symm).1 hinj

/-- The Koszul covector `w ↦ ½(Dg(u)(v,w) + Dg(v)(u,w) − Dg(w)(u,v))`. -/
noncomputable def koszul (x u v : V) : Module.Dual ℝ V where
  toFun w := (S.Dg x u v w + S.Dg x v u w - S.Dg x w u v) / 2
  map_add' w₁ w₂ := by simp only [Dg, map_add, add_apply]; ring
  map_smul' c w := by
    simp only [Dg, map_smul, smul_apply, smul_eq_mul, RingHom.id_apply]; ring

open Classical in
/-- **Christoffel symbols** `Γ(x)(u,v) = ♭⁻¹(Koszul covector)` (`0` off `M`). -/
noncomputable def Γ (x u v : V) : V :=
  if h : ∃ z, S.flat x z = S.koszul x u v then h.choose else 0

/-- **Defining identity:** `g(Γ(u,v), w) = ½(Dg(u)(v,w) + Dg(v)(u,w) − Dg(w)(u,v))`. -/
theorem ct_christoffel_koszul [FiniteDimensional ℝ V] {x : V} (hx : x ∈ S.M) (u v w : V) :
    S.g x (S.Γ x u v) w = (S.Dg x u v w + S.Dg x v u w - S.Dg x w u v) / 2 := by
  have h : ∃ z, S.flat x z = S.koszul x u v := S.ct_flat_surjective hx _
  rw [Γ, dif_pos h]
  exact LinearMap.congr_fun h.choose_spec w

/-- `Γ(u,v)` is the unique vector satisfying the Koszul identity. -/
theorem ct_christoffel_unique [FiniteDimensional ℝ V] {x : V} (hx : x ∈ S.M) {u v z : V}
    (hz : ∀ w, S.g x z w = (S.Dg x u v w + S.Dg x v u w - S.Dg x w u v) / 2) :
    z = S.Γ x u v := by
  have h0 : z - S.Γ x u v = 0 := S.ct_nondegenerate hx fun w => by
    rw [map_sub, sub_apply, hz, S.ct_christoffel_koszul hx]; ring
  exact sub_eq_zero.1 h0

/-- **Symmetry** `Γ(u,v) = Γ(v,u)`. -/
theorem ct_christoffel_symm (x u v : V) : S.Γ x u v = S.Γ x v u := by
  have hk : S.koszul x u v = S.koszul x v u := by
    ext w
    simp only [koszul, LinearMap.coe_mk, AddHom.coe_mk]
    rw [S.ct_Dg_symm x w u v]; ring
  unfold Γ
  rw [hk]

/-! ### Curves: acceleration, pregeodesics, metric compatibility -/

/-- The geodesic operator `∇_{γ'}γ' = γ'' + Γ(γ',γ')`. -/
noncomputable def acc (γ : ℝ → V) (t : ℝ) : V :=
  deriv (deriv γ) t + S.Γ (γ t) (deriv γ t) (deriv γ t)

/-- `γ` is a pregeodesic at `t`: `∇_{γ'}γ' ∥ γ'`. -/
def IsPregeodesicAt (γ : ℝ → V) (t : ℝ) : Prop := ∃ f : ℝ, S.acc γ t = f • deriv γ t

/-- `γ` is a pregeodesic on `I`: `∇_{γ'}γ' = f · γ'` there. -/
def IsPregeodesicOn (γ : ℝ → V) (I : Set ℝ) : Prop :=
  ∃ f : ℝ → ℝ, ∀ t ∈ I, S.acc γ t = f t • deriv γ t

theorem ct_pregeodesicOn_of_forall {γ : ℝ → V} {I : Set ℝ}
    (h : ∀ t ∈ I, S.IsPregeodesicAt γ t) : S.IsPregeodesicOn γ I := by
  classical
  refine ⟨fun t => if ht : t ∈ I then (h t ht).choose else 0, fun t ht => ?_⟩
  simp only [dif_pos ht]
  exact (h t ht).choose_spec

/-- Product rule for `g` along curves. -/
lemma ct_hasDerivAt_g {p u w : ℝ → V} {p' u' w' : V} {r : ℝ}
    (hg : DifferentiableAt ℝ S.g (p r)) (hp : HasDerivAt p p' r)
    (hu : HasDerivAt u u' r) (hw : HasDerivAt w w' r) :
    HasDerivAt (fun r => S.g (p r) (u r) (w r))
      (S.Dg (p r) p' (u r) (w r) + S.g (p r) u' (w r) + S.g (p r) (u r) w') r := by
  have h1 : HasDerivAt (fun r => S.g (p r)) (fderiv ℝ S.g (p r) p') r :=
    HasFDerivAt.comp_hasDerivAt (l := S.g) r hg.hasFDerivAt hp
  have := (h1.clm_apply hu).clm_apply hw
  simpa [Dg, add_assoc] using this

lemma ct_deriv_contDiff {γ : ℝ → V} (hγ : ContDiff ℝ 2 γ) : ContDiff ℝ 1 (deriv γ) :=
  (contDiff_succ_iff_deriv.1 hγ).2.2

/-- **Covariant product rule** along `γ`: `d/dt g(γ',W) = g(acc,W) + g(γ',W') + ½ Dg(W)(γ',γ')`. -/
theorem ct_deriv_g_vel_field [FiniteDimensional ℝ V] (hg : Differentiable ℝ S.g) {γ W : ℝ → V}
    (hγ : ContDiff ℝ 2 γ) {W' : V} {t : ℝ} (hW : HasDerivAt W W' t) (ht : γ t ∈ S.M) :
    HasDerivAt (fun r => S.g (γ r) (deriv γ r) (W r))
      (S.g (γ t) (S.acc γ t) (W t) + S.g (γ t) (deriv γ t) W'
        + S.Dg (γ t) (W t) (deriv γ t) (deriv γ t) / 2) t := by
  have h := S.ct_hasDerivAt_g (hg (γ t))
    (ct_hasDerivAt_of_contDiff (hγ.of_le (by norm_num)) t)
    (ct_hasDerivAt_of_contDiff (ct_deriv_contDiff hγ) t) hW
  convert h using 1
  rw [acc, map_add, add_apply, S.ct_christoffel_koszul ht]
  ring

/-- **Metric compatibility along a curve:** `d/dt g(γ',γ') = 2 g(γ', acc)`. -/
theorem ct_metric_compat [FiniteDimensional ℝ V] (hg : Differentiable ℝ S.g) {γ : ℝ → V}
    (hγ : ContDiff ℝ 2 γ) {t : ℝ} (ht : γ t ∈ S.M) :
    HasDerivAt (fun r => S.g (γ r) (deriv γ r) (deriv γ r))
      (2 * S.g (γ t) (deriv γ t) (S.acc γ t)) t := by
  have h := S.ct_deriv_g_vel_field hg hγ
    (ct_hasDerivAt_of_contDiff (ct_deriv_contDiff hγ) t) ht
  convert h using 1
  rw [S.symm (γ t) (deriv γ t) (S.acc γ t), acc, map_add, add_apply,
    S.ct_christoffel_koszul ht, S.symm (γ t) (deriv (deriv γ) t)]
  ring

lemma ct_hasDerivAt_line (p q : V) (e : ℝ) : HasDerivAt (fun e : ℝ => p + e • q) q e := by
  simpa using ((hasDerivAt_id' e).smul_const q).const_add p

/-- **First variation** of the quadratic form along `γ_ε = γ + εW` at a fixed parameter `t`:
`∂_ε|₀ g(γ_ε',γ_ε') = Dg(W)(γ',γ') + 2g(γ',W') = 2 d/dt g(γ',W) − 2 g(acc,W)`. -/
theorem ct_first_variation [FiniteDimensional ℝ V] (hg : Differentiable ℝ S.g) {γ W : ℝ → V}
    (hγ : ContDiff ℝ 2 γ) {t : ℝ} (hW : HasDerivAt W (deriv W t) t) (ht : γ t ∈ S.M) :
    HasDerivAt (fun e : ℝ => S.g (γ t + e • W t) (deriv γ t + e • deriv W t)
        (deriv γ t + e • deriv W t))
      (S.Dg (γ t) (W t) (deriv γ t) (deriv γ t) + 2 * S.g (γ t) (deriv γ t) (deriv W t)) 0 ∧
    S.Dg (γ t) (W t) (deriv γ t) (deriv γ t) + 2 * S.g (γ t) (deriv γ t) (deriv W t)
      = 2 * deriv (fun r => S.g (γ r) (deriv γ r) (W r)) t - 2 * S.g (γ t) (S.acc γ t) (W t) := by
  constructor
  · have h := S.ct_hasDerivAt_g (hg _) (ct_hasDerivAt_line (γ t) (W t) 0)
      (ct_hasDerivAt_line (deriv γ t) (deriv W t) 0)
      (ct_hasDerivAt_line (deriv γ t) (deriv W t) 0)
    simp only [zero_smul, add_zero] at h
    convert h using 1
    rw [S.symm (γ t) (deriv W t)]; ring
  · rw [(S.ct_deriv_g_vel_field hg hγ hW ht).deriv]; ring

/-! ## ② The corner-cutting lemma -/

/-- Linear algebra: if `A ∉ ℝ·v` and `g(v,T) ≠ 0`, some `Z ⊥ v` has `g(A,Z) > 0`. -/
theorem ct_exists_transverse {x : V} (hx : x ∈ S.M) {v A : V} (hvT : S.g x v (S.T x) ≠ 0)
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
  refine ⟨S.g x A τ / S.g x v τ, sub_eq_zero.1 (S.ct_nondegenerate hx fun w => ?_)⟩
  have hw := hker (w - (S.g x v w / S.g x v τ) • τ) (by
    simp only [map_sub, map_smul, smul_eq_mul]; field_simp; ring)
  simp only [map_sub, map_smul, smul_eq_mul, sub_apply,
    smul_apply] at hw ⊢
  field_simp at hw ⊢
  linarith

/-- An affine reparametrisation of a timelike `C¹` curve on `[s,t]` is a `TStep`. -/
theorem ct_tstep_of_curve {σ : ℝ → V} (hσ : ContDiff ℝ 1 σ) {s t : ℝ} (hst : s < t)
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
    exact ((ct_hasDerivAt_of_contDiff hσ _).scomp x ha).deriv
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
theorem ct_variation_chr (hg : ContDiff ℝ 1 S.g) {γ W : ℝ → V} (hγ : ContDiff ℝ 1 γ)
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
    ((S.ct_cont_Dg hg hσc (hW.continuous.comp continuous_snd) hσ'c hσ'c).add
      (S.ct_cont_gvw hσc (hW'c.comp continuous_snd) hσ'c)).add
      (S.ct_cont_gvw hσc hσ'c (hW'c.comp continuous_snd))
  have hO : IsOpen {z : ℝ × ℝ | σ z.1 z.2 ∈ S.M ∧
      S.g (σ z.1 z.2) (σ' z.1 z.2) (S.T (σ z.1 z.2)) < 0 ∧ P z.1 z.2 < 0} :=
    (S.isOpen_M.preimage hσc).inter ((isOpen_lt (S.ct_cont_gvw hσc hσ'c (S.cont_T.comp hσc))
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
      have h := S.ct_hasDerivAt_g (hgd _) (ct_hasDerivAt_line (γ r) (W r) e)
        (ct_hasDerivAt_line (deriv γ r) (deriv W r) e)
        (ct_hasDerivAt_line (deriv γ r) (deriv W r) e)
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
    ((ct_hasDerivAt_of_contDiff hγ r).add
      ((ct_hasDerivAt_of_contDiff hW r).const_smul ε)).deriv
  have hstep := S.ct_tstep_of_curve hσC hst fun r hr => by
    rw [hσd]
    exact ⟨(hgood ε ⟨hε.le, le_rfl⟩ r hr).1, hQ r hr, (hgood ε ⟨hε.le, le_rfl⟩ r hr).2.1⟩
  have hs : σ ε s = γ s := by simp [σ, hWs]
  have ht : σ ε t = γ t := by simp [σ, hWt]
  rw [hs, ht] at hstep
  exact Relation.TransGen.single hstep

/-- **The corner-cutting lemma.** A `C²` future-causal (e.g. future-null) curve that fails to be
a pregeodesic at an interior parameter `t₀` has two chronologically related points
`γ(s) ≪ γ(t)`, `a < s < t₀ < t < b`. -/
theorem ct_corner_cutting [FiniteDimensional ℝ V] (hg : ContDiff ℝ 1 S.g) {γ : ℝ → V}
    (hγ : ContDiff ℝ 2 γ) {a b t₀ : ℝ} (ht₀ : t₀ ∈ Ioo a b)
    (hcaus : ∀ r ∈ Icc a b, γ r ∈ S.M ∧ S.FutCausal (γ r) (deriv γ r))
    (hnp : ¬ S.IsPregeodesicAt γ t₀) :
    ∃ s t, a < s ∧ s < t₀ ∧ t₀ < t ∧ t < b ∧ S.Chr (γ s) (γ t) := by
  have hγ1 : ContDiff ℝ 1 γ := hγ.of_le (by norm_num)
  have hγ2 : ContDiff ℝ 1 (deriv γ) := ct_deriv_contDiff hγ
  have hgd : Differentiable ℝ S.g := hg.differentiable one_ne_zero
  have hγd : ∀ r, HasDerivAt γ (deriv γ r) r := ct_hasDerivAt_of_contDiff hγ1
  have hγ'd : ∀ r, HasDerivAt (deriv γ) (deriv (deriv γ) r) r := ct_hasDerivAt_of_contDiff hγ2
  have hγc : Continuous γ := hγ1.continuous
  have hγ'c : Continuous (deriv γ) := hγ2.continuous
  have hγ''c : Continuous (deriv (deriv γ)) := hγ2.continuous_deriv le_rfl
  obtain ⟨hx₀M, hv⟩ := hcaus t₀ (Ioo_subset_Icc_self ht₀)
  have hvτ : S.g (γ t₀) (deriv γ t₀) (S.T (γ t₀)) < 0 := hv.2
  obtain ⟨Z₀, hZ₀v, hc₀⟩ := S.ct_exists_transverse hx₀M hvτ.ne hnp
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
    S.ct_hasDerivAt_g (hgd _) (hγd r) (hγ'd r) (hZd r)
  have hZt₀ : Z t₀ = Z₀ := by simp [hZdef]
  have hh0 : h t₀ = 0 := by simp only [hhdef, hZt₀]; exact hZ₀v
  have hgvY : S.g (γ t₀) (deriv γ t₀) Y = -c₀ / 2 - S.Dg (γ t₀) Z₀ (deriv γ t₀) (deriv γ t₀) / 2 := by
    have hne := hvτ.ne
    rw [hYdef, map_smul, smul_eq_mul, hμdef]; field_simp
  have he0 : e t₀ = -c₀ / 2 := by
    simp only [hedef, hZt₀, hgvY]; ring
  have hd0 : hd t₀ = c₀ / 2 := by
    have hk := S.ct_christoffel_koszul hx₀M (deriv γ t₀) (deriv γ t₀) Z₀
    have hc : c₀ = S.g (γ t₀) (deriv (deriv γ) t₀) Z₀
        + S.g (γ t₀) (S.Γ (γ t₀) (deriv γ t₀) (deriv γ t₀)) Z₀ := by
      rw [hc₀def, acc, map_add, add_apply]
    simp only [hhddef, hZt₀, hgvY]
    rw [hk] at hc
    linarith
  have hdc : Continuous hd :=
    ((S.ct_cont_Dg hg hγc hγ'c hγ'c hZc).add (S.ct_cont_gvw hγc hγ''c hZc)).add
      (S.ct_cont_gvw hγc hγ'c continuous_const)
  have hec : Continuous e :=
    ((S.ct_cont_Dg hg hγc hZc hγ'c hγ'c).div_const 2).add (S.ct_cont_gvw hγc hγ'c continuous_const)
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
  refine S.ct_variation_chr hg hγ1 hWC hst (by simp [hWdef, hφdef]) (by simp [hWdef, hφdef])
    (fun r hr => hcaus r ⟨by linarith [hr.1], by linarith [hr.2]⟩) fun r hr => ?_
  rw [(hWd r).deriv]
  have hexp : S.Dg (γ r) (W r) (deriv γ r) (deriv γ r)
      + 2 * S.g (γ r) (deriv γ r) (φ r • Y + ((t - r) - (r - s)) • Z r)
      = 2 * (((t - r) - (r - s)) * h r + φ r * e r) := by
    simp only [hWdef, S.ct_Dg_smul, map_add, map_smul, smul_eq_mul, hhdef, hedef]
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
theorem ct_corner_cutting_null [FiniteDimensional ℝ V] (hg : ContDiff ℝ 1 S.g) {γ : ℝ → V}
    (hγ : ContDiff ℝ 2 γ) {a b t₀ : ℝ} (ht₀ : t₀ ∈ Ioo a b)
    (hnull : ∀ r ∈ Icc a b, γ r ∈ S.M ∧ S.g (γ r) (deriv γ r) (deriv γ r) = 0 ∧
      S.g (γ r) (deriv γ r) (S.T (γ r)) < 0)
    (hnp : ¬ S.IsPregeodesicAt γ t₀) :
    ∃ s t, s < t ∧ S.Chr (γ s) (γ t) := by
  obtain ⟨s, t, -, hs, ht, -, hc⟩ := S.ct_corner_cutting hg hγ ht₀
    (fun r hr => ⟨(hnull r hr).1, (hnull r hr).2.1.le, (hnull r hr).2.2⟩) hnp
  exact ⟨s, t, hs.trans ht, hc⟩

/-! ## ③ Stretch: the tangency clause (first half) -/

/-- The horizon `H = ∂J⁻(J)` is achronal. -/
theorem ct_H_achronal (J : Set V) {p q : V} (hp : p ∈ S.H J) (hq : q ∈ S.H J) :
    ¬ S.Chr p q := by
  intro hpq
  obtain ⟨q', hq'I, hq'J⟩ := mem_closure_iff.1 (frontier_subset_closure hq) (S.Ifut p)
    (S.ct_isOpen_Ifut p) hpq
  obtain ⟨j, hj, hq'j⟩ := mem_iUnion₂.1 hq'J
  have hsub : S.Ipast q' ⊆ S.JpastSet J := fun x hx =>
    mem_iUnion₂.2 ⟨j, hj, Relation.ReflTransGen.trans (S.ct_chr_cau hx) hq'j⟩
  have hint : p ∈ interior (S.JpastSet J) :=
    interior_maximal hsub (S.ct_isOpen_Ipast q') hq'I
  exact hp.2 hint

/-- An achronal `C¹` future-causal curve is null at every interior parameter. -/
theorem ct_achronal_null {γ : ℝ → V} (hγ : ContDiff ℝ 1 γ) {a b t₀ : ℝ} (ht₀ : t₀ ∈ Ioo a b)
    (hcaus : ∀ r ∈ Icc a b, γ r ∈ S.M ∧ S.FutCausal (γ r) (deriv γ r))
    (hach : ∀ s t, a < s → s < t → t < b → ¬ S.Chr (γ s) (γ t)) :
    S.g (γ t₀) (deriv γ t₀) (deriv γ t₀) = 0 := by
  obtain ⟨hM, hle, hT⟩ := hcaus t₀ (Ioo_subset_Icc_self ht₀)
  refine le_antisymm hle (not_lt.1 fun hlt => ?_)
  have hcont : Continuous fun r => (γ r, deriv γ r) :=
    hγ.continuous.prodMk (hγ.continuous_deriv le_rfl)
  have hev : ∀ᶠ r in 𝓝 t₀, γ r ∈ S.M ∧ S.FutTimelike (γ r) (deriv γ r) :=
    hcont.continuousAt.eventually (S.ct_isOpen_timelikePairs.mem_nhds ⟨hM, hlt, hT⟩)
  obtain ⟨ρ, hρ, hball⟩ := Metric.eventually_nhds_iff.1 hev
  set δ := min (ρ / 2) (min ((t₀ - a) / 2) ((b - t₀) / 2)) with hδdef
  have hδ : 0 < δ := lt_min (by positivity) (lt_min (by linarith [ht₀.1]) (by linarith [ht₀.2]))
  have hδρ : δ < ρ := lt_of_le_of_lt (min_le_left _ _) (by linarith)
  have hδa : δ < t₀ - a := lt_of_le_of_lt ((min_le_right _ _).trans (min_le_left _ _))
    (by linarith [ht₀.1])
  have hδb : δ < b - t₀ := lt_of_le_of_lt ((min_le_right _ _).trans (min_le_right _ _))
    (by linarith [ht₀.2])
  have hstep := S.ct_tstep_of_curve hγ (s := t₀ - δ) (t := t₀ + δ) (by linarith) fun r hr =>
    hball (by
      rw [Real.dist_eq]
      exact (abs_le.2 ⟨by linarith [hr.1], by linarith [hr.2]⟩).trans_lt hδρ)
  exact hach _ _ (by linarith) (by linarith) (by linarith) (Relation.TransGen.single hstep)

/-- An achronal `C²` future-causal curve is a pregeodesic at every interior parameter. -/
theorem ct_achronal_pregeodesic [FiniteDimensional ℝ V] (hg : ContDiff ℝ 1 S.g) {γ : ℝ → V}
    (hγ : ContDiff ℝ 2 γ) {a b : ℝ}
    (hcaus : ∀ r ∈ Icc a b, γ r ∈ S.M ∧ S.FutCausal (γ r) (deriv γ r))
    (hach : ∀ s t, a < s → s < t → t < b → ¬ S.Chr (γ s) (γ t)) :
    S.IsPregeodesicOn γ (Ioo a b) := by
  refine S.ct_pregeodesicOn_of_forall fun t₀ ht₀ => not_not.1 fun hnp => ?_
  obtain ⟨s, t, has, hs, ht, htb, hc⟩ := S.ct_corner_cutting hg hγ ht₀ hcaus hnp
  exact hach s t has (hs.trans ht) htb hc

/-- **Tangency clause, first half:** a `C²` future-causal curve lying in the horizon
`H = ∂J⁻(J)` (a `C²` generator) is a null pregeodesic on the open parameter interval. -/
theorem ct_H_generator_null_pregeodesic [FiniteDimensional ℝ V] (hg : ContDiff ℝ 1 S.g)
    (J : Set V) {γ : ℝ → V} (hγ : ContDiff ℝ 2 γ) {a b : ℝ}
    (hcaus : ∀ r ∈ Icc a b, γ r ∈ S.M ∧ S.FutCausal (γ r) (deriv γ r))
    (hH : ∀ r ∈ Icc a b, γ r ∈ S.H J) :
    (∀ t ∈ Ioo a b, S.g (γ t) (deriv γ t) (deriv γ t) = 0) ∧ S.IsPregeodesicOn γ (Ioo a b) := by
  have hach : ∀ s t, a < s → s < t → t < b → ¬ S.Chr (γ s) (γ t) := fun s t has hst htb =>
    S.ct_H_achronal J (hH s ⟨has.le, by linarith⟩) (hH t ⟨by linarith, htb.le⟩)
  exact ⟨fun t ht => S.ct_achronal_null (hγ.of_le (by norm_num)) ht hcaus hach,
    S.ct_achronal_pregeodesic hg hγ hcaus hach⟩

end Spacetime

#print axioms Spacetime.ct_nondegenerate
#print axioms Spacetime.ct_flat_surjective
#print axioms Spacetime.ct_Dg_symm
#print axioms Spacetime.ct_christoffel_koszul
#print axioms Spacetime.ct_christoffel_unique
#print axioms Spacetime.ct_christoffel_symm
#print axioms Spacetime.ct_deriv_g_vel_field
#print axioms Spacetime.ct_metric_compat
#print axioms Spacetime.ct_first_variation
#print axioms Spacetime.ct_exists_transverse
#print axioms Spacetime.ct_tstep_of_curve
#print axioms Spacetime.ct_variation_chr
#print axioms Spacetime.ct_corner_cutting
#print axioms Spacetime.ct_corner_cutting_null
#print axioms Spacetime.ct_H_achronal
#print axioms Spacetime.ct_achronal_null
#print axioms Spacetime.ct_achronal_pregeodesic
#print axioms Spacetime.ct_H_generator_null_pregeodesic

end ShadowProbe.CornerCuttingProbe

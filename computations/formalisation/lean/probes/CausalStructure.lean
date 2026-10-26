import Mathlib

/-!
# Probe `r7613+71.4` (campaign 60, `r7613` ③): the causal-structure layer, `prop:causal-alignment`'s
# elementary clauses, and `cor:densities`

Source: `corpus/BH_causality_v2.tex`, `prop:causal-alignment` and `cor:densities` (lines 300–328).
Registration: `computations/formalisation/r7613_71_campaign60/PREDICTION.md`. Nothing imports this
file, and it imports no other probe.

## Setting (single chart; no Mathlib-manifold version is attempted)

* `V` is any real normed space (for the paper, `EuclideanSpace ℝ (Fin (n+1))`); `M ⊆ V` is open.
* `g : V → (V →L[ℝ] V →L[ℝ] ℝ)` is continuous and symmetric. "Lorentzian of signature `(−,+,…,+)`"
  is encoded by the time orientation: `g x (T x) (T x) < 0` and `g x` is positive definite on the
  `g`-orthogonal complement of `T x`. This forces signature `(−,+,…,+)`.
* `T : V → V` is continuous: the time orientation.
* A vector `v` at `x` is *future timelike* if `g v v < 0 ∧ g v (T x) < 0`, and *future causal* if
  `g v v ≤ 0 ∧ g v (T x) < 0`. The second condition already forces `v ≠ 0`.

## Curves: the definition chosen

* A *timelike step* `TStep x y` is a `C¹` map `γ : ℝ → V` with `γ 0 = x` and `γ 1 = y`, such that
  for every `t ∈ [0,1]`, `γ t ∈ M` and `γ' t` is future timelike. `CStep` is the same with future
  causal.
* `x ≪ y` (`Chr`) is the transitive closure of `TStep`. `x ≤ y` (`Cau`) is the
  reflexive-transitive closure of `CStep`. So `I⁺/I⁻` are endpoints of finite chains of `C¹`
  timelike pieces, i.e. of piecewise-`C¹` timelike curves, and `J±(p)` contains `p`.
* Faithfulness caveats:
  - A piecewise-`C¹` curve on `[0,1]` is a finite concatenation of `C¹` pieces, and each piece,
    reparametrised affinely to `[0,1]`, extends to a `C¹` map on `ℝ`. The chain relation is
    therefore exactly the piecewise-`C¹` relation. The probe uses `C¹` on all of `ℝ` and does not
    prove that extension step.
  - At a corner the one-sided velocities need not agree. That is the standard piecewise-`C¹`
    convention.
  - `M` is only required to be open. Curves stay in `M` on `[0,1]`, endpoints included.

## Push-up and its hypothesis

Push-up (`J⁻(I⁻(z)) ⊆ I⁻(z)`, `cs_pushup`; dual `cs_pushup'`) is proved for **locally Lipschitz**
`g`. That hypothesis is genuine, not a convenience: for merely continuous metrics push-up can fail
(the "causal bubbles" of Chruściel–Grant 2012). Everything else needs only continuity. The proof
works as follows.
1. Local push-up. A causal piece `α` on `[s,t]` is tilted by `λ·(r−s)·T(α s)`. The tilt is
   strictly timelike for small `t−s` and `λ`. The Lipschitz bound controls the error from moving
   the base point, which is `O(λ(t−s))`, against the gain `λ·|g(α', T)|`.
2. Globally, take `sInf` of `{t | α t ∈ I⁻(z)}` and use openness of `I⁻(z)`.

## `𝒥⁺`, `D`, `𝓗⁺`, `B`

`𝒥⁺ = J` is any set (hypothesis-supplied; there is no conformal completion). Only points of
`J ∩ M` are endpoints of curves. To model a conformal boundary, read `(M, g)` as a chart of the
unphysical completion. Then:
* `D = I⁻(J)`,
* `H = frontier (J⁻(J))`,
* `BH = M \ J⁻(J)`,
* finite slices are `slice J Θ τ = {x ∈ D | Θ x = τ}`, with a subtype version for `Θ : D → ℝ`.

## Temporal functions and global hyperbolicity (definitions)

* `IsTemporal τ` asks that `τ` be `C¹` with `dτ(v) > 0` for all future-causal `v`. This is the
  dual form of "the gradient is past-directed timelike".
* `IsCauchyTemporal` asks that every inextendible piecewise-`C¹` causal curve meet each level set
  exactly once.
* `GloballyHyperbolic` is the *existence of a Cauchy temporal function*. This is the
  Bernal–Sánchez (2005) equivalent of the classical definition, **taken as the definition**; the
  equivalence is not proved.
* `ExteriorGH J` is that property for `D` regarded as a spacetime (`restrict`).
* Closedness of `J⁻(p)`, which follows from global hyperbolicity classically, is taken as an
  explicit hypothesis where it is used (`cs_lightcone_inter_H`).

## Not attempted: the tangency/convergence clause (the registered reachable negative)

It needs two pieces.
* The limit-curve theorem. Mathlib has Arzelà–Ascoli
  (`BoundedContinuousFunction.arzela_ascoli`, `ArzelaAscoli.isCompact_of_equicontinuous`),
  equicontinuity of Lipschitz families (`LipschitzWith.uniformEquicontinuous`) and Rademacher
  (`LipschitzWith.ae_differentiableAt`). It has no Lorentzian or causal-curve theory. The first
  missing lemma is *closedness of the causal-curve condition under uniform convergence*: a
  uniform limit of uniformly Lipschitz future-causal curves is a (Lipschitz) future-causal curve.
  It is missing for two reasons:
  - the `C¹` chain class used here is not closed under uniform limits, so causal curves must
    first be re-founded as Lipschitz/absolutely continuous curves with a.e. causal velocity;
  - the closed-convex-cone characterisation of their difference quotients is absent.
* The null-generator structure of achronal boundaries, `∂J⁻(S) \ S` ruled by past-inextendible
  null geodesics. This needs geodesics of `g`, achronality and the limit-curve theorem above.
-/

open Set Filter Topology Metric

namespace ShadowProbe.CausalStructure

variable {V : Type*} [NormedAddCommGroup V] [NormedSpace ℝ V]

/-- A time-oriented Lorentzian chart: open `M`, a continuous symmetric `g`, and a continuous
time orientation `T`. `T_timelike` and `pos_on_perp` together encode signature `(−,+,…,+)` on `M`. -/
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
/-- Future-directed causal vector at `x` (nonzero automatically). -/
def FutCausal (x v : V) : Prop := S.g x v v ≤ 0 ∧ S.g x v (S.T x) < 0

/-- One `C¹` future-timelike piece from `x` to `y`, parametrised by `[0,1]`. -/
def TStep (x y : V) : Prop :=
  ∃ γ : ℝ → V, ContDiff ℝ 1 γ ∧ γ 0 = x ∧ γ 1 = y ∧
    ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ S.M ∧ S.FutTimelike (γ t) (deriv γ t)

/-- One `C¹` future-causal piece from `x` to `y`, parametrised by `[0,1]`. -/
def CStep (x y : V) : Prop :=
  ∃ γ : ℝ → V, ContDiff ℝ 1 γ ∧ γ 0 = x ∧ γ 1 = y ∧
    ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ S.M ∧ S.FutCausal (γ t) (deriv γ t)

/-- Chronological relation `x ≪ y`: a finite chain of timelike pieces. -/
def Chr (x y : V) : Prop := Relation.TransGen S.TStep x y
/-- Causal relation `x ≤ y`: a finite (possibly empty) chain of causal pieces. -/
def Cau (x y : V) : Prop := Relation.ReflTransGen S.CStep x y

/-- Chronological past `I⁻(p)`. -/
def Ipast (p : V) : Set V := {q | S.Chr q p}

lemma cont_gvw {X : Type*} [TopologicalSpace X] {x v w : X → V} (hx : Continuous x)
    (hv : Continuous v) (hw : Continuous w) : Continuous fun a => S.g (x a) (v a) (w a) :=
  ((S.cont_g.comp hx).clm_apply hv).clm_apply hw

/-- The open set of (point, future timelike vector) pairs. -/
lemma isOpen_timelikePairs :
    IsOpen {pv : V × V | pv.1 ∈ S.M ∧ S.FutTimelike pv.1 pv.2} := by
  refine (S.isOpen_M.preimage continuous_fst).inter (IsOpen.inter ?_ ?_)
  · exact isOpen_lt (S.cont_gvw continuous_fst continuous_snd continuous_snd) continuous_const
  · exact isOpen_lt (S.cont_gvw continuous_fst continuous_snd
      (S.cont_T.comp continuous_fst)) continuous_const

/-- Tube lemma for perturbed curves. -/
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

/-- The end of a timelike step can be moved in an open set. -/
lemma tstep_end_eventually {y q : V} (h : S.TStep y q) : ∀ᶠ q' in 𝓝 q, S.TStep y q' := by
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

/-- Chronological future `I⁺(p)`. -/
def Ifut (p : V) : Set V := {q | S.Chr p q}
/-- Causal past `J⁻(p)` (contains `p`). -/
def Jpast (p : V) : Set V := {q | S.Cau q p}
/-- Causal future `J⁺(p)` (contains `p`). -/
def Jfut (p : V) : Set V := {q | S.Cau p q}
/-- `I⁻(A) = ⋃ p ∈ A, I⁻(p)`. -/
def IpastSet (A : Set V) : Set V := ⋃ p ∈ A, S.Ipast p
/-- `I⁺(A)`. -/
def IfutSet (A : Set V) : Set V := ⋃ p ∈ A, S.Ifut p
/-- `J⁻(A)`. -/
def JpastSet (A : Set V) : Set V := ⋃ p ∈ A, S.Jpast p
/-- `J⁺(A)`. -/
def JfutSet (A : Set V) : Set V := ⋃ p ∈ A, S.Jfut p

theorem cs_isOpen_Ifut (p : V) : IsOpen (S.Ifut p) := by
  refine isOpen_iff_mem_nhds.2 fun q hq => ?_
  obtain ⟨y, hpy, hyq⟩ := Relation.TransGen.tail'_iff.1 hq
  filter_upwards [S.tstep_end_eventually hyq] with q' hq'
  exact Relation.TransGen.tail' hpy hq'

theorem cs_isOpen_Ipast (p : V) : IsOpen (S.Ipast p) := by
  refine isOpen_iff_mem_nhds.2 fun q hq => ?_
  obtain ⟨y, hqy, hyp⟩ := Relation.TransGen.head'_iff.1 hq
  filter_upwards [S.tstep_start_eventually hqy] with q' hq'
  exact Relation.TransGen.head' hq' hyp

theorem cs_isOpen_IpastSet (A : Set V) : IsOpen (S.IpastSet A) :=
  isOpen_biUnion fun p _ => S.cs_isOpen_Ipast p

theorem cs_isOpen_IfutSet (A : Set V) : IsOpen (S.IfutSet A) :=
  isOpen_biUnion fun p _ => S.cs_isOpen_Ifut p

lemma tstep_to_cstep {x y : V} (h : S.TStep x y) : S.CStep x y := by
  obtain ⟨γ, hγ, h0, h1, hγt⟩ := h
  exact ⟨γ, hγ, h0, h1, fun t ht => ⟨(hγt t ht).1, (hγt t ht).2.1.le, (hγt t ht).2.2⟩⟩

/-- `I ⊆ J`. -/
theorem cs_chr_cau {x y : V} (h : S.Chr x y) : S.Cau x y := by
  induction h with
  | single h => exact Relation.ReflTransGen.single (S.tstep_to_cstep h)
  | tail _ h ih => exact ih.tail (S.tstep_to_cstep h)

/-- `I ∘ I ⊆ I`. -/
theorem cs_chr_trans {x y z : V} (h1 : S.Chr x y) (h2 : S.Chr y z) : S.Chr x z :=
  Relation.TransGen.trans h1 h2

/-- `J ∘ J ⊆ J`. -/
theorem cs_cau_trans {x y z : V} (h1 : S.Cau x y) (h2 : S.Cau y z) : S.Cau x z :=
  Relation.ReflTransGen.trans h1 h2

theorem cs_mem_Jpast_self (p : V) : p ∈ S.Jpast p := Relation.ReflTransGen.refl

theorem cs_Ipast_subset_Jpast (p : V) : S.Ipast p ⊆ S.Jpast p := fun _ h => S.cs_chr_cau h

theorem cs_IpastSet_subset_JpastSet (A : Set V) : S.IpastSet A ⊆ S.JpastSet A :=
  biUnion_mono subset_rfl fun p _ => S.cs_Ipast_subset_Jpast p

/-- Positive rescaling preserves future-timelikeness. -/
lemma futTimelike_smul {x u : V} {c : ℝ} (hc : 0 < c) (h : S.FutTimelike x u) :
    S.FutTimelike x (c • u) := by
  obtain ⟨h1, h2⟩ := h
  refine ⟨?_, ?_⟩
  · simp only [map_smul, FunLike.coe_smul, Pi.smul_apply, smul_eq_mul]
    nlinarith [mul_pos hc hc]
  · simp only [map_smul, FunLike.coe_smul, Pi.smul_apply, smul_eq_mul]
    nlinarith

/-- Lipschitz control of the quadratic form. -/
lemma quad_le {K : NNReal} {N : Set V} (hK : LipschitzOnWith K S.g N) {p q : V} (hp : p ∈ N)
    (hq : q ∈ N) (a : V) : S.g p a a ≤ S.g q a a + K * dist p q * (‖a‖ * ‖a‖) := by
  have h1 : |S.g p a a - S.g q a a| ≤ ‖S.g p - S.g q‖ * ‖a‖ * ‖a‖ := by
    have := (S.g p - S.g q).le_opNorm₂ a a
    simpa [Real.norm_eq_abs] using this
  have h2 : ‖S.g p - S.g q‖ ≤ K * dist p q := by
    have := hK.dist_le_mul p hp q hq
    rwa [dist_eq_norm] at this
  have h3 := (abs_le.1 h1).2
  have h4 : ‖S.g p - S.g q‖ * ‖a‖ * ‖a‖ ≤ K * dist p q * (‖a‖ * ‖a‖) := by
    rw [mul_assoc]; exact mul_le_mul_of_nonneg_right h2 (by positivity)
  linarith

/-- Local push-up. -/
lemma local_pushup (hL : LocallyLipschitz S.g) {α : ℝ → V} (hα : ContDiff ℝ 1 α)
    (hc : ∀ t ∈ Icc (0:ℝ) 1, α t ∈ S.M ∧ S.FutCausal (α t) (deriv α t))
    {s : ℝ} (hs : s ∈ Icc (0:ℝ) 1) :
    ∃ ε > 0, ∀ t ∈ Icc (0:ℝ) 1, s < t → t < s + ε → ∀ l : ℝ, 0 < l → l < ε →
      S.TStep (α s) (α t + (l * (t - s)) • S.T (α s)) := by
  obtain ⟨hx₀M, -, hb⟩ := hc s hs
  obtain ⟨K, N, hN, hK⟩ := hL (α s)
  have hvv : S.g (α s) (S.T (α s)) (S.T (α s)) < 0 := S.T_timelike _ hx₀M
  -- abbreviations
  have hdc : Continuous (deriv α) := hα.continuous_deriv le_rfl
  let v := S.T (α s)
  let u₀ := deriv α s
  let b := -(S.g (α s) u₀ v)
  have hbpos : 0 < b := by simp only [b]; linarith
  let P : V × V → Prop := fun pu => pu.1 ∈ S.M ∧ S.g pu.1 pu.2 v < -(b/2) ∧
    S.g pu.1 v v < 0 ∧ S.g pu.1 pu.2 (S.T pu.1) < 0 ∧ S.g pu.1 v (S.T pu.1) < 0 ∧
    pu.1 ∈ N ∧ ‖pu.2‖ < ‖u₀‖ + 1
  have hW : ∀ᶠ pu in 𝓝 (α s, u₀), P pu := by
    have e1 : ∀ᶠ pu : V × V in 𝓝 (α s, u₀), pu.1 ∈ S.M :=
      continuousAt_fst.eventually_mem (S.isOpen_M.mem_nhds hx₀M)
    have e2 : ∀ᶠ pu : V × V in 𝓝 (α s, u₀), S.g pu.1 pu.2 v < -(b/2) :=
      ((S.cont_gvw continuous_fst continuous_snd continuous_const).continuousAt).eventually_lt
        continuousAt_const (by simp only [b, u₀]; linarith)
    have e3 : ∀ᶠ pu : V × V in 𝓝 (α s, u₀), S.g pu.1 v v < 0 :=
      ((S.cont_gvw continuous_fst continuous_const continuous_const).continuousAt).eventually_lt
        continuousAt_const hvv
    have e4 : ∀ᶠ pu : V × V in 𝓝 (α s, u₀), S.g pu.1 pu.2 (S.T pu.1) < 0 :=
      ((S.cont_gvw continuous_fst continuous_snd
        (S.cont_T.comp continuous_fst)).continuousAt).eventually_lt continuousAt_const hb
    have e5 : ∀ᶠ pu : V × V in 𝓝 (α s, u₀), S.g pu.1 v (S.T pu.1) < 0 :=
      ((S.cont_gvw continuous_fst continuous_const
        (S.cont_T.comp continuous_fst)).continuousAt).eventually_lt continuousAt_const hvv
    have e6 : ∀ᶠ pu : V × V in 𝓝 (α s, u₀), pu.1 ∈ N := continuousAt_fst.eventually_mem hN
    have e7 : ∀ᶠ pu : V × V in 𝓝 (α s, u₀), ‖pu.2‖ < ‖u₀‖ + 1 :=
      (continuous_norm.comp continuous_snd).continuousAt.eventually_lt continuousAt_const
        (by simp)
    filter_upwards [e1, e2, e3, e4, e5, e6, e7] with pu h1 h2 h3 h4 h5 h6 h7
    exact ⟨h1, h2, h3, h4, h5, h6, h7⟩
  let Φ : ℝ × ℝ → V × V := fun z => (α z.1 + (z.2 * (z.1 - s)) • v, deriv α z.1)
  have hΦc : Continuous Φ := by
    refine Continuous.prodMk ?_ (hdc.comp continuous_fst)
    exact (hα.continuous.comp continuous_fst).add
      ((continuous_snd.mul (continuous_fst.sub continuous_const)).smul continuous_const)
  have hΦ : Tendsto Φ (𝓝 (s, 0)) (𝓝 (α s, u₀)) := by
    have := hΦc.tendsto (s, 0)
    simpa [Φ, u₀] using this
  have hαN : ∀ᶠ z : ℝ × ℝ in 𝓝 (s, 0), α z.1 ∈ N :=
    ((hα.continuous.comp continuous_fst).tendsto (s, 0)).eventually_mem (by simpa using hN)
  have hLip : ∀ᶠ z : ℝ × ℝ in 𝓝 (s, 0),
      (K:ℝ) * |z.1 - s| * ‖v‖ * (‖u₀‖ + 1) ^ 2 < b / 2 := by
    refine ContinuousAt.eventually_lt (by fun_prop) continuousAt_const ?_
    simp; linarith
  obtain ⟨ε, hε, hεP⟩ := Metric.eventually_nhds_iff.1 ((hΦ.eventually hW).and (hαN.and hLip))
  refine ⟨ε, hε, fun t ht hst htε l hl hlε => ?_⟩
  refine ⟨fun r => α (s + r * (t - s)) + (l * (r * (t - s))) • v,
    (hα.comp (contDiff_const.add (contDiff_id.mul contDiff_const))).add
      ((contDiff_const.mul (contDiff_id.mul contDiff_const)).smul contDiff_const),
    by simp, by simp [v], fun r hr => ?_⟩
  have hts : 0 < t - s := sub_pos.2 hst
  set s' := s + r * (t - s) with hs'
  have hs's : s' - s = r * (t - s) := by rw [hs']; ring
  have hs'0 : 0 ≤ s' - s := by rw [hs's]; exact mul_nonneg hr.1 hts.le
  have hs'1 : s' - s ≤ t - s := by rw [hs's]; nlinarith [hr.2]
  have hs'I : s' ∈ Icc (0:ℝ) 1 := ⟨by linarith [hs.1], by linarith [ht.2]⟩
  -- the derivative
  have hin : HasDerivAt (fun r => s + r * (t - s)) (t - s) r := by
    simpa using ((hasDerivAt_id r).mul_const (t - s)).const_add s
  have h1 : HasDerivAt (fun r => α (s + r * (t - s))) ((t - s) • deriv α s') r :=
    (hasDerivAt_of_contDiff hα _).scomp r hin
  have h2 : HasDerivAt (fun r => (l * (r * (t - s))) • v) ((l * (t - s)) • v) r := by
    simpa using (((hasDerivAt_id r).mul_const (t - s)).const_mul l).smul_const v
  have hd : deriv (fun r => α (s + r * (t - s)) + (l * (r * (t - s))) • v) r =
      (t - s) • (deriv α s' + l • v) := by
    have h3 : HasDerivAt (fun r => α (s + r * (t - s)) + (l * (r * (t - s))) • v)
        ((t - s) • deriv α s' + (l * (t - s)) • v) r := h1.add h2
    rw [h3.deriv, smul_add, smul_smul, mul_comm l]
  have hpt : α (s + r * (t - s)) + (l * (r * (t - s))) • v = α s' + (l * (s' - s)) • v := by
    rw [hs's]
  rw [hd]
  beta_reduce
  rw [hpt]
  -- the estimates at `(s', l)`
  have hdist : dist (s', l) (s, 0) < ε := by
    rw [Prod.dist_eq, max_lt_iff, Real.dist_eq, Real.dist_eq, sub_zero, abs_of_nonneg hs'0,
      abs_of_pos hl]
    exact ⟨by linarith, hlε⟩
  obtain ⟨⟨hpM, hav, hvv', haT, hvT, hpN, hna⟩, hαN', hLip'⟩ := hεP hdist
  simp only [Φ] at hpM hav hvv' haT hvT hpN hna hαN' hLip'
  set p := α s' + (l * (s' - s)) • v with hp
  set a := deriv α s' with ha
  have hcaus := (hc s' hs'I).2.1
  have hq := S.quad_le hK hpN hαN' a
  have hdp : dist p (α s') = l * (s' - s) * ‖v‖ := by
    rw [hp, dist_eq_norm, add_sub_cancel_left, norm_smul, Real.norm_eq_abs,
      abs_of_nonneg (mul_nonneg hl.le hs'0)]
  rw [hdp] at hq
  have hna0 : 0 ≤ ‖a‖ := norm_nonneg a
  have hasq : ‖a‖ * ‖a‖ ≤ (‖u₀‖ + 1) ^ 2 := by nlinarith
  have hQ0 : 0 ≤ (K:ℝ) * (s' - s) * ‖v‖ := by positivity
  have hLip'' : (K:ℝ) * (s' - s) * ‖v‖ * (‖u₀‖ + 1) ^ 2 < b / 2 := by
    rwa [abs_of_nonneg hs'0] at hLip'
  have hKa : (K:ℝ) * (l * (s' - s) * ‖v‖) * (‖a‖ * ‖a‖) ≤ l * (b / 2) := by
    have : (K:ℝ) * (s' - s) * ‖v‖ * (‖a‖ * ‖a‖) ≤ (K:ℝ) * (s' - s) * ‖v‖ * (‖u₀‖ + 1) ^ 2 :=
      mul_le_mul_of_nonneg_left hasq hQ0
    nlinarith
  have hgaa : S.g p a a ≤ l * (b / 2) := by linarith
  refine ⟨hpM, S.futTimelike_smul hts ⟨?_, ?_⟩⟩
  · simp only [map_add, map_smul, FunLike.coe_add, Pi.add_apply, FunLike.coe_smul, Pi.smul_apply,
      smul_eq_mul]
    rw [S.symm p v a]
    nlinarith [mul_pos hl hl]
  · simp only [map_add, map_smul, FunLike.coe_add, Pi.add_apply, FunLike.coe_smul, Pi.smul_apply,
      smul_eq_mul]
    nlinarith

/-- Push-up along one causal step: a causal step followed by a timelike chain is a timelike
chain. Needs `g` locally Lipschitz. -/
lemma pushup_cstep (hL : LocallyLipschitz S.g) {x y z : V} (hxy : S.CStep x y)
    (hyz : S.Chr y z) : S.Chr x z := by
  obtain ⟨α, hα, h0, h1, hc⟩ := hxy
  let A : Set ℝ := {t | t ∈ Icc (0:ℝ) 1 ∧ S.Chr (α t) z}
  have h1A : (1:ℝ) ∈ A := ⟨⟨zero_le_one, le_rfl⟩, by simp only [h1]; exact hyz⟩
  have hne : A.Nonempty := ⟨1, h1A⟩
  have hbdd : BddBelow A := ⟨0, fun t ht => ht.1.1⟩
  have hs0 : 0 ≤ sInf A := le_csInf hne fun t ht => ht.1.1
  have hs1 : sInf A ≤ 1 := csInf_le hbdd h1A
  have hαc := hα.continuous
  have hsA : S.Chr (α (sInf A)) z := by
    obtain ⟨ε, hε, hloc⟩ := S.local_pushup hL hα hc ⟨hs0, hs1⟩
    obtain ⟨t, htA, hts⟩ := exists_lt_of_csInf_lt hne (show sInf A < sInf A + ε by linarith)
    have hst : sInf A ≤ t := csInf_le hbdd htA
    rcases hst.lt_or_eq with hst | hst
    · have hcl : Continuous fun l : ℝ => α t + (l * (t - sInf A)) • S.T (α (sInf A)) := by
        fun_prop
      have hev : ∀ᶠ l in 𝓝 (0:ℝ), S.Chr (α t + (l * (t - sInf A)) • S.T (α (sInf A))) z := by
        have := hcl.tendsto 0
        simp only [zero_mul, zero_smul, add_zero] at this
        exact this.eventually ((S.cs_isOpen_Ipast z).mem_nhds htA.2)
      obtain ⟨l, hl, hlpos, hlε⟩ :=
        ((hev.filter_mono nhdsWithin_le_nhds).and (Ioo_mem_nhdsGT hε)).exists
      exact Relation.TransGen.head (hloc t htA.1 hst hts l hlpos hlε) hl
    · rw [hst]; exact htA.2
  have hs : sInf A = 0 := by
    by_contra hne0
    have hspos : 0 < sInf A := lt_of_le_of_ne hs0 (Ne.symm hne0)
    have hev : ∀ᶠ t in 𝓝 (sInf A), S.Chr (α t) z :=
      (hαc.tendsto _).eventually ((S.cs_isOpen_Ipast z).mem_nhds hsA)
    obtain ⟨δ, hδ, hδP⟩ := Metric.eventually_nhds_iff.1 hev
    have hm1 := min_le_left δ (sInf A)
    have hm2 := min_le_right δ (sInf A)
    have hm3 := lt_min hδ hspos
    have ht : sInf A - min δ (sInf A) / 2 ∈ A := by
      refine ⟨⟨by linarith, by linarith⟩, hδP ?_⟩
      rw [Real.dist_eq, abs_lt]; constructor <;> linarith
    have := csInf_le hbdd ht
    linarith
  rw [← h0, ← hs]; exact hsA

/-- **Push-up** `J⁻(I⁻(z)) ⊆ I⁻(z)`: `q ≤ p ≪ z ⟹ q ≪ z`, for locally Lipschitz `g`. -/
theorem cs_pushup (hL : LocallyLipschitz S.g) {q p z : V} (hqp : S.Cau q p) (hpz : S.Chr p z) :
    S.Chr q z := by
  induction hqp using Relation.ReflTransGen.head_induction_on with
  | refl => exact hpz
  | head h _ ih => exact S.pushup_cstep hL h ih

/-- Set form of push-up: `q ∈ J⁻(p)`, `p ∈ I⁻(A)` give `q ∈ I⁻(A)`. -/
theorem cs_pushup_set (hL : LocallyLipschitz S.g) {A : Set V} {q p : V} (hqp : q ∈ S.Jpast p)
    (hp : p ∈ S.IpastSet A) : q ∈ S.IpastSet A := by
  simp only [IpastSet, mem_iUnion] at hp ⊢
  obtain ⟨z, hz, hpz⟩ := hp
  exact ⟨z, hz, S.cs_pushup hL hqp hpz⟩

/-! ### Time reversal, and the dual push-up `I⁻ ∘ J⁻ ⊆ I⁻` -/

/-- The time-reversed chart: same `g`, orientation `-T`. -/
def rev : Spacetime V where
  M := S.M
  isOpen_M := S.isOpen_M
  g := S.g
  cont_g := S.cont_g
  symm := S.symm
  T x := -S.T x
  cont_T := S.cont_T.neg
  T_timelike x hx := by simpa using S.T_timelike x hx
  pos_on_perp x hx v hv := S.pos_on_perp x hx v (by simpa using hv)

lemma rev_futTimelike (x v : V) : S.rev.FutTimelike x v ↔ S.FutTimelike x (-v) := by
  simp [FutTimelike, rev]

lemma rev_futCausal (x v : V) : S.rev.FutCausal x v ↔ S.FutCausal x (-v) := by
  simp [FutCausal, rev]

lemma reverse_curve {γ : ℝ → V} (hγ : ContDiff ℝ 1 γ) :
    ContDiff ℝ 1 (fun t => γ (1 - t)) ∧ ∀ t, deriv (fun t => γ (1 - t)) t = -deriv γ (1 - t) := by
  refine ⟨hγ.comp (contDiff_const.sub contDiff_id), fun t => ?_⟩
  have hin : HasDerivAt (fun t : ℝ => 1 - t) (0 - 1) t :=
    (hasDerivAt_const t (1:ℝ)).sub (hasDerivAt_id' t)
  have h : HasDerivAt (fun t => γ (1 - t)) (((0:ℝ) - 1) • deriv γ (1 - t)) t :=
    (hasDerivAt_of_contDiff hγ (1 - t)).scomp t hin
  rw [h.deriv, zero_sub, neg_one_smul]

lemma rev_tstep_iff (x y : V) : S.rev.TStep x y ↔ S.TStep y x := by
  constructor
  · rintro ⟨γ, hγ, h0, h1, ht⟩
    obtain ⟨hc, hd⟩ := reverse_curve hγ
    refine ⟨fun t => γ (1 - t), hc, by simp [h1], by simp [h0], fun t htI => ?_⟩
    have hI : 1 - t ∈ Icc (0:ℝ) 1 := ⟨by linarith [htI.2], by linarith [htI.1]⟩
    obtain ⟨hm, hf⟩ := ht _ hI
    exact ⟨hm, by rw [hd]; exact (S.rev_futTimelike _ _).1 hf⟩
  · rintro ⟨γ, hγ, h0, h1, ht⟩
    obtain ⟨hc, hd⟩ := reverse_curve hγ
    refine ⟨fun t => γ (1 - t), hc, by simp [h1], by simp [h0], fun t htI => ?_⟩
    have hI : 1 - t ∈ Icc (0:ℝ) 1 := ⟨by linarith [htI.2], by linarith [htI.1]⟩
    obtain ⟨hm, hf⟩ := ht _ hI
    exact ⟨hm, by rw [hd, S.rev_futTimelike, neg_neg]; exact hf⟩

lemma rev_cstep_iff (x y : V) : S.rev.CStep x y ↔ S.CStep y x := by
  constructor
  · rintro ⟨γ, hγ, h0, h1, ht⟩
    obtain ⟨hc, hd⟩ := reverse_curve hγ
    refine ⟨fun t => γ (1 - t), hc, by simp [h1], by simp [h0], fun t htI => ?_⟩
    have hI : 1 - t ∈ Icc (0:ℝ) 1 := ⟨by linarith [htI.2], by linarith [htI.1]⟩
    obtain ⟨hm, hf⟩ := ht _ hI
    exact ⟨hm, by rw [hd]; exact (S.rev_futCausal _ _).1 hf⟩
  · rintro ⟨γ, hγ, h0, h1, ht⟩
    obtain ⟨hc, hd⟩ := reverse_curve hγ
    refine ⟨fun t => γ (1 - t), hc, by simp [h1], by simp [h0], fun t htI => ?_⟩
    have hI : 1 - t ∈ Icc (0:ℝ) 1 := ⟨by linarith [htI.2], by linarith [htI.1]⟩
    obtain ⟨hm, hf⟩ := ht _ hI
    exact ⟨hm, by rw [hd, S.rev_futCausal, neg_neg]; exact hf⟩

theorem cs_rev_chr (x y : V) : S.rev.Chr x y ↔ S.Chr y x := by
  have e : S.rev.TStep = Function.swap S.TStep := by
    funext x y; exact propext (S.rev_tstep_iff x y)
  unfold Chr; rw [e]; exact Relation.transGen_swap

theorem cs_rev_cau (x y : V) : S.rev.Cau x y ↔ S.Cau y x := by
  have e : S.rev.CStep = Function.swap S.CStep := by
    funext x y; exact propext (S.rev_cstep_iff x y)
  unfold Cau; rw [e]; exact Relation.reflTransGen_swap

/-- **Dual push-up** `q ≪ p ≤ z ⟹ q ≪ z`, by time reversal. -/
theorem cs_pushup' (hL : LocallyLipschitz S.g) {q p z : V} (hqp : S.Chr q p) (hpz : S.Cau p z) :
    S.Chr q z := by
  have h := S.rev.cs_pushup (z := q) hL ((S.cs_rev_cau z p).2 hpz) ((S.cs_rev_chr p q).2 hqp)
  exact (S.cs_rev_chr z q).1 h

/-- `I⁺(p)` is open (from openness of `I⁻` in the reversed chart, or directly). -/
theorem cs_Ifut_eq_rev (p : V) : S.Ifut p = S.rev.Ipast p := by
  ext q; exact (S.cs_rev_chr q p).symm

/-! ### Temporal functions and global hyperbolicity -/

/-- Points of `I⁻(z)` lie in `M`. -/
theorem cs_Ipast_subset_M (z : V) : S.Ipast z ⊆ S.M := by
  intro q hq
  obtain ⟨b, ⟨γ, -, h0, -, hγ⟩, -⟩ := Relation.TransGen.head'_iff.1 hq
  rw [← h0]; exact (hγ 0 ⟨le_rfl, zero_le_one⟩).1

theorem cs_IpastSet_subset_M (A : Set V) : S.IpastSet A ⊆ S.M :=
  iUnion₂_subset fun z _ => S.cs_Ipast_subset_M z

/-- The same chart with `M` replaced by an open subset `U ⊆ M` (e.g. the exterior `D`, regarded
as a spacetime in its own right). -/
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

/-- A future-directed, inextendible, piecewise-`C¹` causal curve, parametrised by `ℝ`: continuous,
in `M`, differentiable with future-causal velocity off a locally finite set of break points, and
with no endpoint in `M` in either direction. -/
structure InextCausalCurve where
  γ : ℝ → V
  cont : Continuous γ
  mem : ∀ t, γ t ∈ S.M
  brk : Set ℝ
  brk_fin : ∀ a b : ℝ, (brk ∩ Icc a b).Finite
  causal : ∀ t ∉ brk, DifferentiableAt ℝ γ t ∧ S.FutCausal (γ t) (deriv γ t)
  inext_future : ¬ ∃ p ∈ S.M, Tendsto γ atTop (𝓝 p)
  inext_past : ¬ ∃ p ∈ S.M, Tendsto γ atBot (𝓝 p)

/-- A temporal function: `C¹`, with `dτ(v) > 0` for every future-causal `v`. This is the dual
form of "`∇τ` is past-directed timelike". -/
def IsTemporal (τ : V → ℝ) : Prop :=
  ContDiff ℝ 1 τ ∧ ∀ x ∈ S.M, ∀ v, S.FutCausal x v → 0 < fderiv ℝ τ x v

/-- A Cauchy temporal function: temporal, and every inextendible causal curve meets every level
set exactly once (Bernal–Sánchez normalise `τ` onto `ℝ`). -/
def IsCauchyTemporal (τ : V → ℝ) : Prop :=
  S.IsTemporal τ ∧ ∀ c : S.InextCausalCurve, ∀ a : ℝ, ∃! t : ℝ, τ (c.γ t) = a

/-- **Global hyperbolicity**, defined as the existence of a Cauchy temporal function. By
Bernal–Sánchez (2005) this is equivalent to the classical definition (strong causality plus compact
causal diamonds); that equivalence is taken, not proved. -/
def GloballyHyperbolic : Prop := ∃ τ : V → ℝ, S.IsCauchyTemporal τ

/-- A temporal function increases strictly along every timelike step. -/
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

/-- A temporal function increases strictly along every timelike chain. -/
theorem cs_temporal_chr {τ : V → ℝ} (hτ : S.IsTemporal τ) {x y : V} (h : S.Chr x y) :
    τ x < τ y := by
  induction h with
  | single h => exact S.temporal_tstep hτ h
  | tail _ h ih => exact ih.trans (S.temporal_tstep hτ h)

/-- Global hyperbolicity implies chronology: no closed timelike chains. -/
theorem cs_GH_chronological (hGH : S.GloballyHyperbolic) (x : V) : ¬ S.Chr x x := by
  obtain ⟨τ, hτ, -⟩ := hGH
  exact fun h => lt_irrefl _ (S.cs_temporal_chr hτ h)

/-! ### Exterior, horizon, black-hole region (`𝒥⁺` hypothesis-supplied) -/

variable (J : Set V)

/-- The exterior `D = I⁻(𝒥⁺)`. -/
def D : Set V := S.IpastSet J
/-- The event horizon `𝓗⁺ = ∂J⁻(𝒥⁺)`. -/
def H : Set V := frontier (S.JpastSet J)
/-- The black-hole region `M \ J⁻(𝒥⁺)`. -/
def BH : Set V := S.M \ S.JpastSet J
/-- A finite slice `S_τ = {x ∈ D | Θ x = τ}`. -/
def slice (Θ : V → ℝ) (τ : ℝ) : Set V := {x | x ∈ S.D J ∧ Θ x = τ}

theorem cs_D_open : IsOpen (S.D J) := S.cs_isOpen_IpastSet J

theorem cs_D_subset_M : S.D J ⊆ S.M := S.cs_IpastSet_subset_M J

theorem cs_D_subset_interior : S.D J ⊆ interior (S.JpastSet J) :=
  interior_maximal (S.cs_IpastSet_subset_JpastSet J) (S.cs_D_open J)

/-- Every exterior event is off the horizon: `D ∩ 𝓗⁺ = ∅`. -/
theorem cs_D_inter_H : S.D J ∩ S.H J = ∅ := by
  ext x
  simp only [mem_inter_iff, mem_empty_iff_false, iff_false, not_and]
  intro hxD hxH
  exact hxH.2 (S.cs_D_subset_interior J hxD)

lemma disjoint_H_of_subset_D {A : Set V} (hA : A ⊆ S.D J) : A ∩ S.H J = ∅ :=
  subset_empty_iff.1 ((inter_subset_inter_left _ hA).trans (S.cs_D_inter_H J).subset)

/-- `p ∈ D ⟹ I⁻(p) ⊆ D`. -/
theorem cs_Ipast_subset_D {p : V} (hp : p ∈ S.D J) : S.Ipast p ⊆ S.D J := by
  intro q hq
  simp only [D, IpastSet, mem_iUnion] at hp ⊢
  obtain ⟨z, hz, hpz⟩ := hp
  exact ⟨z, hz, S.cs_chr_trans hq hpz⟩

/-- `p ∈ D ⟹ I⁻(p) ∩ 𝓗⁺ = ∅` (openness and transitivity only). -/
theorem cs_Ipast_inter_H {p : V} (hp : p ∈ S.D J) : S.Ipast p ∩ S.H J = ∅ :=
  S.disjoint_H_of_subset_D J (S.cs_Ipast_subset_D J hp)

/-- `p ∈ D ⟹ closure I⁻(p) ⊆ closure D`. -/
theorem cs_closure_Ipast_subset {p : V} (hp : p ∈ S.D J) :
    closure (S.Ipast p) ⊆ closure (S.D J) :=
  closure_mono (S.cs_Ipast_subset_D J hp)

/-- `p ∈ D ⟹ J⁻(p) ⊆ D` (push-up). -/
theorem cs_Jpast_subset_D (hL : LocallyLipschitz S.g) {p : V} (hp : p ∈ S.D J) :
    S.Jpast p ⊆ S.D J :=
  fun _ hq => S.cs_pushup_set hL hq hp

/-- `p ∈ D ⟹ J⁻(p) ∩ 𝓗⁺ = ∅` (push-up). -/
theorem cs_Jpast_inter_H (hL : LocallyLipschitz S.g) {p : V} (hp : p ∈ S.D J) :
    S.Jpast p ∩ S.H J = ∅ :=
  S.disjoint_H_of_subset_D J (S.cs_Jpast_subset_D J hL hp)

/-- The past light cone `∂J⁻(p)` of an exterior event misses `𝓗⁺`, given that `J⁻(p)` is closed
(which holds when the spacetime is globally hyperbolic; taken as a hypothesis). -/
theorem cs_lightcone_inter_H (hL : LocallyLipschitz S.g) {p : V} (hp : p ∈ S.D J)
    (hcl : IsClosed (S.Jpast p)) : frontier (S.Jpast p) ∩ S.H J = ∅ := by
  refine S.disjoint_H_of_subset_D J ?_
  exact (frontier_subset_closure.trans hcl.closure_subset).trans (S.cs_Jpast_subset_D J hL hp)

/-- A worldline in the exterior: no past cone of it meets `𝓗⁺`. -/
theorem cs_worldline_cones (hL : LocallyLipschitz S.g) (O : ℝ → V) (hO : ∀ τ, O τ ∈ S.D J)
    (τ : ℝ) : S.Ipast (O τ) ∩ S.H J = ∅ ∧ S.Jpast (O τ) ∩ S.H J = ∅ ∧
      (IsClosed (S.Jpast (O τ)) → frontier (S.Jpast (O τ)) ∩ S.H J = ∅) :=
  ⟨S.cs_Ipast_inter_H J (hO τ), S.cs_Jpast_inter_H J hL (hO τ),
    fun hcl => S.cs_lightcone_inter_H J hL (hO τ) hcl⟩

/-- If `I⁻(O) = D`, each `I⁻(O τ)` lies in `D`, hence misses `𝓗⁺`. -/
theorem cs_observer_Ipast (O : ℝ → V) (hOD : S.IpastSet (range O) = S.D J) (τ : ℝ) :
    S.Ipast (O τ) ⊆ S.D J ∧ S.Ipast (O τ) ∩ S.H J = ∅ := by
  have h : S.Ipast (O τ) ⊆ S.D J := by
    rw [← hOD]; exact subset_biUnion_of_mem (u := S.Ipast) (mem_range_self τ)
  exact ⟨h, S.disjoint_H_of_subset_D J h⟩

/-- Every finite slice lies in `D` and misses `𝓗⁺`. -/
theorem cs_slice_subset_D (Θ : V → ℝ) (τ : ℝ) :
    S.slice J Θ τ ⊆ S.D J ∧ S.slice J Θ τ ∩ S.H J = ∅ :=
  ⟨fun _ hx => hx.1, S.disjoint_H_of_subset_D J fun _ hx => hx.1⟩

/-- Subtype version: for `Θ : D → ℝ`, every level set, viewed in `V`, lies in `D` and misses
`𝓗⁺`. -/
theorem cs_slice_subtype (Θ : S.D J → ℝ) (τ : ℝ) :
    Subtype.val '' (Θ ⁻¹' {τ}) ⊆ S.D J ∧ (Subtype.val '' (Θ ⁻¹' {τ})) ∩ S.H J = ∅ := by
  have h : Subtype.val '' (Θ ⁻¹' {τ}) ⊆ S.D J := by
    rintro _ ⟨x, -, rfl⟩; exact x.2
  exact ⟨h, S.disjoint_H_of_subset_D J h⟩

/-- `cor:densities`: the black-hole region is disjoint from `D`. -/
theorem cs_BH_inter_D : S.BH J ∩ S.D J = ∅ := by
  ext x
  simp only [mem_inter_iff, mem_empty_iff_false, iff_false, not_and]
  intro hB hD
  exact hB.2 (S.cs_IpastSet_subset_JpastSet J hD)

/-- `cor:densities`: the black-hole region meets no finite slice. -/
theorem cs_BH_inter_slice (Θ : V → ℝ) (τ : ℝ) : S.BH J ∩ S.slice J Θ τ = ∅ :=
  subset_empty_iff.1 ((inter_subset_inter_right _ fun _ hx => hx.1).trans
    (S.cs_BH_inter_D J).subset)

/-- `cor:densities`, subtype form. -/
theorem cs_BH_inter_slice_subtype (Θ : S.D J → ℝ) (τ : ℝ) :
    S.BH J ∩ Subtype.val '' (Θ ⁻¹' {τ}) = ∅ :=
  subset_empty_iff.1 ((inter_subset_inter_right _ (S.cs_slice_subtype J Θ τ).1).trans
    (S.cs_BH_inter_D J).subset)

/-- The exterior is itself a spacetime chart; `prop:causal-alignment`'s hypothesis "`D` is globally
hyperbolic" is `S.ExteriorGH J`. -/
def ExteriorGH : Prop :=
  (S.restrict (S.D J) (S.cs_D_open J) (S.cs_D_subset_M J)).GloballyHyperbolic


end Spacetime

open Spacetime in
#print axioms cs_isOpen_Ipast
#print axioms Spacetime.cs_isOpen_Ifut
#print axioms Spacetime.cs_isOpen_IpastSet
#print axioms Spacetime.cs_chr_trans
#print axioms Spacetime.cs_chr_cau
#print axioms Spacetime.cs_cau_trans
#print axioms Spacetime.cs_pushup
#print axioms Spacetime.cs_pushup'
#print axioms Spacetime.cs_pushup_set
#print axioms Spacetime.cs_rev_chr
#print axioms Spacetime.cs_temporal_chr
#print axioms Spacetime.cs_GH_chronological
#print axioms Spacetime.cs_D_open
#print axioms Spacetime.cs_D_subset_interior
#print axioms Spacetime.cs_D_inter_H
#print axioms Spacetime.cs_Ipast_inter_H
#print axioms Spacetime.cs_Jpast_inter_H
#print axioms Spacetime.cs_lightcone_inter_H
#print axioms Spacetime.cs_worldline_cones
#print axioms Spacetime.cs_observer_Ipast
#print axioms Spacetime.cs_slice_subset_D
#print axioms Spacetime.cs_slice_subtype
#print axioms Spacetime.cs_BH_inter_D
#print axioms Spacetime.cs_BH_inter_slice
#print axioms Spacetime.cs_BH_inter_slice_subtype

end ShadowProbe.CausalStructure

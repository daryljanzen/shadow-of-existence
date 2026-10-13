import Mathlib.Geometry.Manifold.VectorBundle.CovariantDerivative.Basic
import Mathlib.Geometry.Manifold.VectorBundle.LocalFrame
import Mathlib.Geometry.Manifold.VectorBundle.Tangent
import Mathlib.Analysis.ODE.ExistUnique

/-!
# Probe T2 of `r7281+71.1`: local existence of geodesics, on a vector space

Classed THEORY at `r7277+71.5` (B7, geodesic existence), unprobed. **Scope, as pre-registered: `M = E`, a
finite-dimensional real vector space, its own model.** There the trivialisation of `TE` is the identity, so the
frame `covDerivAlong` uses is the same constant basis at every `t`, and the question is the ODE alone.

The connection is a hypothesis, as everywhere in these probes. Its Christoffel form is represented by a `C¹`
map `G : E → E →L E →L E` with `∇_w (const u) (x) = G x w u`. `vel`, `covDerivAlong` and `IsGeodesicAt` are
copied verbatim from `GeodesicProbe.lean`. Nothing imports this file.
-/

open Bundle Manifold Filter Set Topology
open scoped ContDiff

set_option linter.unusedSectionVars false

namespace ShadowProbe

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [CompleteSpace E]
  [FiniteDimensional ℝ E]
  {H : Type*} [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  {M : Type*} [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 2 M]

/-- The velocity of a curve, as a tangent vector. -/
noncomputable def vel (γ : ℝ → M) (t : ℝ) : TangentSpace I (γ t) :=
  mfderiv 𝓘(ℝ, ℝ) I γ t (show TangentSpace 𝓘(ℝ, ℝ) t from (1 : ℝ))

/-- **Q4 (B6).** The covariant derivative of a vector field along a curve. -/
noncomputable def covDerivAlong (cov : CovariantDerivative I E (TangentSpace I : M → Type _))
    (γ : ℝ → M) (V : Π t : ℝ, TangentSpace I (γ t)) (t : ℝ) : TangentSpace I (γ t) :=
  let e := trivializationAt E (TangentSpace I : M → Type _) (γ t)
  let b := Module.finBasis ℝ E
  ∑ i, ((deriv (fun s => e.localFrameCoeff I b i (γ s) (V s)) t) • e.localFrame b i (γ t)
    + (e.localFrameCoeff I b i (γ t) (V t)) • cov (e.localFrame b i) (γ t) (vel γ t))

/-- **B1.** `γ` is a geodesic of `cov` at `t`: `D/dt γ̇ = 0`. -/
def IsGeodesicAt (cov : CovariantDerivative I E (TangentSpace I : M → Type _)) (γ : ℝ → M)
    (t : ℝ) : Prop :=
  covDerivAlong cov γ (vel γ) t = 0


/-! ## On the model space -/

section Model

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [CompleteSpace E]
  [FiniteDimensional ℝ E]

set_option backward.isDefEq.respectTransparency false in
/-- On `E` as its own model, the frame of any trivialisation of `TE` is the basis, constant. -/
lemma model_localFrame (x₀ x : E) (i : Fin (Module.finrank ℝ E)) :
    (trivializationAt E (TangentSpace 𝓘(ℝ, E) : E → Type _) x₀).localFrame (Module.finBasis ℝ E) i x
      = Module.finBasis ℝ E i := by
  have hx : x ∈ (trivializationAt E (TangentSpace 𝓘(ℝ, E) : E → Type _) x₀).baseSet := by simp
  rw [Trivialization.localFrame_apply_of_mem_baseSet _ _ hx]
  simp only [Trivialization.basisAt, Module.Basis.map_apply]
  rw [Trivialization.linearEquivAt_symm_apply, ← Trivialization.symmL_apply (R := ℝ) _ hx,
    TangentBundle.symmL_model_space]
  rfl


set_option backward.isDefEq.respectTransparency false in
/-- On `E`, the frame coefficients of a vector are its coordinates in the basis. -/
lemma model_localFrameCoeff (x₀ x : E) (i : Fin (Module.finrank ℝ E)) (u : E) :
    (trivializationAt E (TangentSpace 𝓘(ℝ, E) : E → Type _) x₀).localFrameCoeff 𝓘(ℝ, E)
      (Module.finBasis ℝ E) i x u = (Module.finBasis ℝ E).repr u i := by
  have hx : x ∈ (trivializationAt E (TangentSpace 𝓘(ℝ, E) : E → Type _) x₀).baseSet := by simp
  rw [show u = (fun _ : E => u) x from rfl,
    Trivialization.localFrameCoeff_apply_of_mem_baseSet _ _ hx (fun _ : E => u) i]
  simp only [Trivialization.basisAt, Module.Basis.map_repr, LinearEquiv.trans_apply,
    LinearEquiv.symm_symm]
  rw [Trivialization.linearEquivAt_apply]
  simp

/-- On `E`: for a `cov` whose Christoffel form is `G`, `D/dt V = V′ + G(γ)(γ̇, V)`. -/
lemma covDerivAlong_model (cov : CovariantDerivative 𝓘(ℝ, E) E (TangentSpace 𝓘(ℝ, E) : E → Type _))
    (G : E → E →L[ℝ] E →L[ℝ] E) (hG : ∀ x w u, cov (fun _ => u) x w = G x w u)
    (γ : ℝ → E) (V : ℝ → E) (t : ℝ) (hV : DifferentiableAt ℝ V t) :
    covDerivAlong cov γ V t = deriv V t + G (γ t) (vel (I := 𝓘(ℝ, E)) γ t) (V t) := by
  unfold covDerivAlong
  have hfr : ∀ i, (trivializationAt E (TangentSpace 𝓘(ℝ, E)) (γ t)).localFrame
      (Module.finBasis ℝ E) i = fun _ => Module.finBasis ℝ E i :=
    fun i => funext fun x => model_localFrame _ _ _
  simp only [hfr, hG, model_localFrameCoeff]
  have hc : ∀ i, deriv (fun s => (Module.finBasis ℝ E).repr (V s) i) t
      = (Module.finBasis ℝ E).repr (deriv V t) i := by
    intro i
    have hL := (LinearMap.toContinuousLinearMap ((Module.finBasis ℝ E).coord i)).hasFDerivAt
      |>.comp_hasDerivAt t hV.hasDerivAt
    exact hL.deriv
  simp only [hc, Finset.sum_add_distrib]
  congr 1
  · exact (Module.finBasis ℝ E).sum_repr (deriv V t)
  · show ∑ x, ((Module.finBasis ℝ E).repr (V t)) x •
        (G (γ t) (show E from vel (I := 𝓘(ℝ, E)) γ t)) ((Module.finBasis ℝ E) x)
      = (G (γ t) (show E from vel (I := 𝓘(ℝ, E)) γ t)) (V t)
    generalize (G (γ t) (show E from vel (I := 𝓘(ℝ, E)) γ t)) = L
    conv_rhs => rw [← (Module.finBasis ℝ E).sum_repr (V t)]
    simp only [map_sum, map_smul]


/-- On `E`, the velocity is the derivative. -/
lemma vel_model (γ : ℝ → E) (t : ℝ) : vel (I := 𝓘(ℝ, E)) γ t = deriv γ t := by
  unfold vel
  rw [mfderiv_eq_fderiv, ← fderiv_apply_one_eq_deriv]
  rfl

set_option backward.isDefEq.respectTransparency false in
/-- **T2.** Local existence of geodesics on `E`, for a connection whose Christoffel form `G` is `C¹`:
through any `x` with any velocity `v` there is a curve, defined on `(-ε, ε)`, that is a geodesic of `cov`
at every time there. -/
theorem geodesic_exists (cov : CovariantDerivative 𝓘(ℝ, E) E (TangentSpace 𝓘(ℝ, E) : E → Type _))
    (G : E → E →L[ℝ] E →L[ℝ] E) (hG : ∀ x w u, cov (fun _ => u) x w = G x w u)
    (hGc : ContDiff ℝ 1 G) (x v : E) :
    ∃ ε > 0, ∃ γ : ℝ → E, γ 0 = x ∧ vel (I := 𝓘(ℝ, E)) γ 0 = v ∧
      ∀ t ∈ Ioo (-ε) ε, IsGeodesicAt cov γ t := by
  -- the first-order system `(x, v)′ = (v, −G(x)(v, v))` on `E × E`
  set f : E × E → E × E := fun p => (p.2, -(G p.1 p.2 p.2)) with hf
  have hfc : ContDiff ℝ 1 f := by
    refine contDiff_snd.prodMk ?_
    exact (((hGc.comp contDiff_fst).clm_apply contDiff_snd).clm_apply contDiff_snd).neg
  obtain ⟨α, hα0, ε, hε, hα⟩ :=
    ContDiffAt.exists_forall_mem_closedBall_exists_eq_forall_mem_Ioo_hasDerivAt₀ (hfc.contDiffAt (x := (x, v))) 0
  simp only [zero_sub, zero_add] at hα
  refine ⟨ε, hε, fun s => (α s).1, by simp [hα0], ?_, ?_⟩
  · have h0 := hα 0 (by constructor <;> linarith)
    rw [vel_model]
    show deriv (fun s => (α s).1) 0 = (v : E)
    have h1 : HasDerivAt (fun s => (α s).1) (f (α 0)).1 0 :=
      (hasFDerivAt_fst (𝕜 := ℝ) (p := α 0)).comp_hasDerivAt 0 h0
    rw [h1.deriv]
    simp [hf, hα0]
  · intro t ht
    -- on the interval, `γ′ = V` and `V′ = −G(γ)(V, V)`
    have hγ' : ∀ s ∈ Ioo (-ε) ε, HasDerivAt (fun s => (α s).1) (α s).2 s := fun s hs =>
      (hasFDerivAt_fst (𝕜 := ℝ) (p := α s)).comp_hasDerivAt s (hα s hs)
    have hV' : HasDerivAt (fun s => (α s).2) (-(G (α t).1 (α t).2 (α t).2)) t :=
      (hasFDerivAt_snd (𝕜 := ℝ) (p := α t)).comp_hasDerivAt t (hα t ht)
    have hvel : (fun s => vel (I := 𝓘(ℝ, E)) (fun s => (α s).1) s) =ᶠ[𝓝 t] fun s => (α s).2 := by
      filter_upwards [Ioo_mem_nhds ht.1 ht.2] with s hs
      rw [vel_model, (hγ' s hs).deriv]
    unfold IsGeodesicAt
    have hd : DifferentiableAt ℝ (fun s => vel (I := 𝓘(ℝ, E)) (fun s => (α s).1) s) t :=
      (hV'.congr_of_eventuallyEq hvel).differentiableAt
    rw [covDerivAlong_model cov G hG _ _ t hd, (hV'.congr_of_eventuallyEq hvel).deriv,
      hvel.eq_of_nhds]
    simp

end Model

end ShadowProbe

#print axioms ShadowProbe.geodesic_exists

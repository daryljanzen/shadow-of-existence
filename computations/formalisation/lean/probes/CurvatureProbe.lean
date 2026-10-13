import Mathlib.Geometry.Manifold.VectorBundle.CovariantDerivative.Basic
import Mathlib.Geometry.Manifold.VectorBundle.Hom
import Mathlib.Geometry.Manifold.VectorBundle.Tangent
import Mathlib.Geometry.Manifold.VectorField.LieBracket

/-!
# Probe K1 of `r7287+71.1`: the curvature tensor, the connection a hypothesis

`curv cov X Y Z = ∇_X ∇_Y Z − ∇_Y ∇_X Z − ∇_[X,Y] Z`, for a `CovariantDerivative` on `TM` taken as a hypothesis.
**The deferred smoothness is carried as `mathlib`'s own class** `ContMDiffCovariantDerivative cov ∞` — "∇ sends
`C^∞` sections to `C^∞` sections" — whose docstring says that a `C^(k+1)` connection being `C^k` "will be proved
in a later file". It is used in one place, `covApply_smooth`. Nothing imports this file.
-/

open Bundle Manifold Filter Set VectorField
open scoped ContDiff Manifold

set_option linter.unusedSectionVars false

namespace ShadowProbe

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  {H : Type*} [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  {M : Type*} [TopologicalSpace M] [ChartedSpace H M] [IsManifold I ∞ M]

local notation "TM" => fun x : M => TangentSpace I x

/-- **K-A.** The curvature of a connection on `TM`: `∇_X ∇_Y Z − ∇_Y ∇_X Z − ∇_[X,Y] Z`. -/
noncomputable def curv (cov : CovariantDerivative I E (TangentSpace I : M → Type _))
    (X Y Z : Π x : M, TangentSpace I x) (x : M) : TangentSpace I x :=
  cov (fun y => cov Z y (Y y)) x (X x) - cov (fun y => cov Z y (X y)) x (Y x)
    - cov Z x (mlieBracket I X Y x)

variable (cov : CovariantDerivative I E (TangentSpace I : M → Type _))

/-- The one use of the smoothness hypothesis: `∇_X Z` is a `C^∞` vector field when `X`, `Z` are. -/
lemma covApply_smooth [CovariantDerivative.ContMDiffCovariantDerivative cov (∞ : ℕ∞ω)] {X Z : Π x : M, TangentSpace I x}
    (hX : CMDiff ∞ (T% X)) (hZ : CMDiff ∞ (T% Z)) :
    CMDiff ∞ (T% (fun y => cov Z y (X y))) := by
  have h := (CovariantDerivative.ContMDiffCovariantDerivative.contMDiff (cov := cov) (k := (∞ : ℕ∞ω))).contMDiff
    (σ := Z) (by simpa using hZ.contMDiffOn)
  exact (contMDiffOn_univ.1 h).clm_bundle_apply hX

/-- `curv` is antisymmetric in `X, Y`. -/
lemma curv_swap (X Y Z : Π x : M, TangentSpace I x) (x : M) :
    curv cov X Y Z x = - curv cov Y X Z x := by
  unfold curv
  rw [mlieBracket_swap_apply, map_neg]
  abel

/-- **K-B, the `X` slot.** `R(f X, Y) Z = f R(X, Y) Z`. -/
theorem curv_smul_left [CovariantDerivative.ContMDiffCovariantDerivative cov (∞ : ℕ∞ω)] {f : M → ℝ} (hf : CMDiff ∞ f)
    {X Y Z : Π x : M, TangentSpace I x} (hX : CMDiff ∞ (T% X)) (hY : CMDiff ∞ (T% Y))
    (hZ : CMDiff ∞ (T% Z)) (x : M) :
    curv cov (f • X) Y Z x = f x • curv cov X Y Z x := by
  unfold curv
  have hfx : MDiffAt f x := (hf x).mdifferentiableAt (by simp)
  have hXx : MDiffAt (T% X) x := (hX x).mdifferentiableAt (by simp)
  have hW : MDiffAt (T% (fun y => cov Z y (X y))) x :=
    (covApply_smooth cov hX hZ x).mdifferentiableAt (by simp)
  have hsec : (fun y => cov Z y ((f • X) y)) = f • (fun y => cov Z y (X y)) := by
    funext y; simp [map_smul]
  rw [hsec, cov.isCovariantDerivativeOn.leibniz hW hfx, mlieBracket_smul_left hfx hXx]
  simp only [map_smul, map_add, ContinuousLinearMap.add_apply, ContinuousLinearMap.smul_apply,
    ContinuousLinearMap.smulRight_apply]
  rw [show (f • X) x = f x • X x from rfl, map_smul]
  module

/-- **K-B, the `Y` slot**, from the `X` slot and antisymmetry. -/
theorem curv_smul_middle [CovariantDerivative.ContMDiffCovariantDerivative cov (∞ : ℕ∞ω)] {f : M → ℝ} (hf : CMDiff ∞ f)
    {X Y Z : Π x : M, TangentSpace I x} (hX : CMDiff ∞ (T% X)) (hY : CMDiff ∞ (T% Y))
    (hZ : CMDiff ∞ (T% Z)) (x : M) :
    curv cov X (f • Y) Z x = f x • curv cov X Y Z x := by
  rw [curv_swap, curv_smul_left cov hf hY hX hZ, curv_swap cov Y X, smul_neg, neg_neg]

/-! ## Probe K2 — on `E` as its own model: the model formula, and the smoothness DISCHARGED -/

section Model

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]

/-- A vector field on `E`, read as a map `E → E`. -/
def vf (σ : Π x : E, TangentSpace 𝓘(ℝ, E) x) : E → E := fun y => show E from σ y

set_option backward.isDefEq.respectTransparency false in
/-- On `E`, a section of `TE` is differentiable iff it is, as a map `E → E`. -/
lemma mdiffAt_model {σ : Π x : E, TangentSpace 𝓘(ℝ, E) x} {x : E} :
    MDiffAt (T% σ) x ↔ DifferentiableAt ℝ (vf σ) x := by
  rw [mdifferentiableAt_section]
  simp only [trivializationAt_model_space_apply]
  exact mdifferentiableAt_iff_differentiableAt

set_option backward.isDefEq.respectTransparency false in
/-- The flat connection `σ ↦ Dσ` on `TE`. -/
lemma flat_isCov : IsCovariantDerivativeOn (I := 𝓘(ℝ, E)) (M := E) E
    (fun (σ : Π x : E, TangentSpace 𝓘(ℝ, E) x) x =>
      (show TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x from (fderiv ℝ (vf σ) x : E →L[ℝ] E))) := by
  refine ⟨fun {σ σ'} {x} hσ hσ' _ => ?_, fun {σ g} {x} hσ hg _ => ?_⟩
  · exact fderiv_add (mdiffAt_model.1 hσ) (mdiffAt_model.1 hσ')
  · rw [mdiffAt_model] at hσ
    rw [mdifferentiableAt_iff_differentiableAt] at hg
    show fderiv ℝ (g • vf σ) x = _
    rw [fderiv_smul hg hσ, mvfderiv_eq_fderiv]
    ext w
    simp only [ContinuousLinearMap.add_apply, ContinuousLinearMap.smul_apply,
      ContinuousLinearMap.smulRight_apply, ContinuousLinearMap.comp_apply]
    rfl

variable (cov : CovariantDerivative 𝓘(ℝ, E) E (TangentSpace 𝓘(ℝ, E) : E → Type _))
  (G : E → E →L[ℝ] E →L[ℝ] E) (hG : ∀ x w u, cov (fun _ => u) x w = G x w u)
include hG

set_option backward.isDefEq.respectTransparency false in
/-- **The model formula:** `∇_w σ = Dσ·w + G(w, σ)` for `σ` differentiable at `x`. -/
lemma cov_model {σ : Π x : E, TangentSpace 𝓘(ℝ, E) x} {x : E} (hσ : MDiffAt (T% σ) x)
    (w : TangentSpace 𝓘(ℝ, E) x) :
    cov σ x w = fderiv ℝ (vf σ) x (show E from w) + G x w (σ x) := by
  have hd := cov.isCovariantDerivativeOn.difference_apply flat_isCov (x := x) trivial hσ
  have hc := cov.isCovariantDerivativeOn.difference_apply flat_isCov (x := x) trivial
    (σ := fun _ => (σ x : E)) (mdiffAt_model.2 (differentiableAt_const (c := (σ x : E))))
  have h1 := DFunLike.congr_fun hd w
  have h2 := DFunLike.congr_fun hc w
  simp only [ContinuousLinearMap.sub_apply] at h1 h2
  have h3 : fderiv ℝ (vf fun _ => σ x) x = 0 := by
    show fderiv ℝ (fun _ : E => (show E from σ x)) x = 0
    exact fderiv_const_apply _
  rw [h3, ContinuousLinearMap.zero_apply, sub_zero, hG] at h2
  have h4 := h1.symm.trans h2
  rw [sub_eq_iff_eq_add] at h4
  show cov σ x w = fderiv ℝ (vf σ) x w + G x w (σ x)
  rw [h4, add_comm]; rfl

set_option backward.isDefEq.respectTransparency false in
/-- On `E`, the Lie bracket of two constant fields vanishes. -/
lemma mlieBracket_const (u v : E) (x : E) :
    mlieBracket 𝓘(ℝ, E) (fun _ => (u : E)) (fun _ => (v : E)) x = 0 := by
  rw [← mlieBracketWithin_univ, mlieBracketWithin_eq_lieBracketWithin, lieBracketWithin_univ,
    lieBracket_eq]
  simp

set_option backward.isDefEq.respectTransparency false in
/-- **K-C, the model formula for curvature**, on constant fields:
`R(u,v)w = (DG·u)(v,w) − (DG·v)(u,w) + G(u, G(v,w)) − G(v, G(u,w))`. -/
theorem curv_model (hGd : Differentiable ℝ G) (u v w x : E) :
    curv cov (fun _ => u) (fun _ => v) (fun _ => w) x
      = fderiv ℝ G x u v w - fderiv ℝ G x v u w + G x u (G x v w) - G x v (G x u w) := by
  have hA : ∀ a : E, (fun y => cov (fun _ => w) y a) = fun y => G y a w :=
    fun a => funext fun y => hG y a w
  have hd : ∀ a : E, MDiffAt (T% (fun y => cov (fun _ => w) y a)) x := fun a => by
    rw [mdiffAt_model, show vf (fun y => cov (fun _ => w) y a) = fun y => G y a w from hA a]
    exact ((hGd x).clm_apply (differentiableAt_const a)).clm_apply (differentiableAt_const w)
  have hD : ∀ a b : E, fderiv ℝ (vf (fun y => cov (fun _ => w) y a)) x b = fderiv ℝ G x b a w :=
    fun a b => by
      rw [show vf (fun y => cov (fun _ => w) y a) = fun y => G y a w from hA a]
      rw [fderiv_clm_apply ((hGd x).clm_apply (differentiableAt_const a))
        (differentiableAt_const w), fderiv_clm_apply (hGd x) (differentiableAt_const a)]
      simp
  unfold curv
  rw [cov_model cov G hG (hd v), cov_model cov G hG (hd u), mlieBracket_const cov G hG, map_zero, sub_zero,
    hD, hD, hG, hG]
  abel

set_option backward.isDefEq.respectTransparency false in
/-- **The smoothness, DISCHARGED on `E`**: if the Christoffel form `G` is `C^∞`, then `cov` is a `C^∞`
covariant derivative in `mathlib`'s sense — the hypothesis K1 carries is a lemma here. -/
theorem contMDiffCov_model (hGs : ContDiff ℝ ∞ G) :
    CovariantDerivative.ContMDiffCovariantDerivative cov (∞ : ℕ∞ω) := by
  refine ⟨⟨fun {σ} hσ => ?_⟩⟩
  have hσ' : ContDiff ℝ ∞ (vf σ) := by
    refine contDiff_iff_contDiffAt.2 fun x => ?_
    have := (contMDiffOn_univ.1 hσ x)
    rw [contMDiffAt_section] at this
    simp only [trivializationAt_model_space_apply] at this
    exact (contMDiffAt_iff_contDiffAt.1 this).of_le (by simp)
  have heq : ∀ x, (cov σ x : E →L[ℝ] E) = fderiv ℝ (vf σ) x + (G x).flip (vf σ x) := fun x => by
    ext w
    rw [cov_model cov G hG (mdiffAt_model.2 (hσ'.differentiable (by simp) x)) w]
    rfl
  refine contMDiffOn_univ.2 fun x => ?_
  rw [contMDiffAt_hom_bundle]
  refine ⟨contMDiffAt_id, ?_⟩
  simp only [inCoordinates_tangent_bundle_core_model_space, inTangentCoordinates_model_space]
  rw [contMDiffAt_iff_contDiffAt, show (fun x => (cov σ x : E →L[ℝ] E)) = fun x =>
    fderiv ℝ (vf σ) x + ContinuousLinearMap.flipₗᵢ ℝ E E E (G x) (vf σ x) from funext heq]
  exact ((hσ'.fderiv_right (by simp)).add
    (((ContinuousLinearMap.flipₗᵢ ℝ E E E).contDiff.comp hGs).clm_apply hσ')).contDiffAt

end Model

end ShadowProbe

#print axioms ShadowProbe.curv_smul_left
#print axioms ShadowProbe.curv_smul_middle
#print axioms ShadowProbe.cov_model
#print axioms ShadowProbe.curv_model
#print axioms ShadowProbe.contMDiffCov_model

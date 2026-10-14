import Mathlib.Analysis.Calculus.Deriv.Inv
import Mathlib.Analysis.SpecialFunctions.ExpDeriv
import Mathlib.Analysis.SpecialFunctions.Pow.Deriv
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Analysis.SpecialFunctions.Trigonometric.DerivHyp
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Deriv
import Mathlib.Analysis.SpecialFunctions.Trigonometric.ArctanDeriv
import Mathlib.Analysis.Calculus.ContDiff.Deriv
import Mathlib.Analysis.Calculus.TangentCone.Real
import Mathlib.Topology.Covering.AddCircle
import Mathlib.Data.ZMod.QuotientGroup
import Mathlib.Geometry.Manifold.MFDeriv.NormedSpace
import Mathlib.Geometry.Manifold.MFDeriv.SpecificFunctions
import Mathlib.Geometry.Manifold.Instances.Sphere
import Mathlib.Geometry.Manifold.VectorBundle.CovariantDerivative.Basic
import Mathlib.Geometry.Manifold.VectorBundle.CovariantDerivative.Torsion
import Mathlib.Geometry.Manifold.VectorBundle.Hom
import Mathlib.Geometry.Manifold.VectorBundle.Tensoriality
import Mathlib.Geometry.Manifold.ContMDiffMFDeriv
import Mathlib.Geometry.Manifold.VectorBundle.Tangent
import Mathlib.Geometry.Manifold.VectorField.LieBracket
import Mathlib.LinearAlgebra.Trace
import Mathlib.LinearAlgebra.BilinearForm.Properties
import Mathlib.Analysis.Calculus.ContDiff.FiniteDimension
import Mathlib.Analysis.Calculus.BumpFunction.FiniteDimension

/-!
# Probe K1 of `r7287+71.1`: the curvature tensor, the connection a hypothesis

`curv cov X Y Z = ∇_X ∇_Y Z − ∇_Y ∇_X Z − ∇_[X,Y] Z`, for a `CovariantDerivative` on `TM` taken as a hypothesis.
**The deferred smoothness is carried as `mathlib`'s own class** `ContMDiffCovariantDerivative cov ∞` — "∇ sends
`C^∞` sections to `C^∞` sections" — whose docstring says that a `C^(k+1)` connection being `C^k` "will be proved
in a later file". It is used in one place, `covApply_smooth`. Since `r7327+71.4` this file is the module `ShadowEngine`, imported by `probes/CurvatureInstances.lean`.
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

set_option backward.isDefEq.respectTransparency false in
/-- **(b)** `y ↦ df(y)(Y y)` is differentiable, from `ContMDiffAt.mfderiv_apply` by undoing its two
coordinate changes on the chart at `x₀`. -/
lemma mdiff_df_apply {f : M → ℝ} (hf : CMDiff ∞ f) {Y : Π x : M, TangentSpace I x}
    (hY : CMDiff ∞ (T% Y)) (x₀ : M) : MDiffAt (fun y => d% f y (Y y)) x₀ := by
  have hg₂ := (contMDiffAt_section (IB := I) (s := Y) x₀).1 (hY x₀)
  have h := ContMDiffAt.mfderiv_apply (I' := 𝓘(ℝ, ℝ)) (n := ∞) (m := 1) (fun _ : M => f) id id
    (fun y => (trivializationAt E (TangentSpace I) x₀ ⟨y, Y y⟩).2)
    ((hf x₀).comp _ contMDiffAt_snd) contMDiffAt_id contMDiffAt_id (hg₂.of_le (by simp)) (by simp)
  refine (h.mdifferentiableAt (by simp)).congr_of_eventuallyEq ?_
  filter_upwards [chart_source_mem_nhds H x₀] with y hy
  simp only [id]
  rw [inTangentCoordinates_eq _ _ _ hy (by simp)]
  simp only [id, tangentBundleCore_coordChange_model_space, ContinuousLinearMap.id_comp,
    ContinuousLinearMap.comp_apply]
  have hv : (trivializationAt E (TangentSpace I) x₀ ⟨y, Y y⟩).2
      = (tangentBundleCore I M).coordChange (achart H y) (achart H x₀) y (Y y) := rfl
  have hyy : y ∈ (tangentBundleCore I M).baseSet (achart H y) := mem_chart_source H y
  have hy0 : y ∈ (tangentBundleCore I M).baseSet (achart H x₀) := hy
  have hcc : (tangentBundleCore I M).coordChange (achart H x₀) (achart H y) y
      ((tangentBundleCore I M).coordChange (achart H y) (achart H x₀) y (Y y)) = Y y := by
    rw [(tangentBundleCore I M).coordChange_comp _ _ _ y ⟨⟨hyy, hy0⟩, hyy⟩,
      (tangentBundleCore I M).coordChange_self _ y hyy]
  rw [hv]
  exact Eq.trans rfl (congrArg (fun v => (mfderiv% f y) v) hcc.symm)

set_option backward.isDefEq.respectTransparency false in
/-- **(c), via Jacobi:** `(X(Yf) − Y(Xf) − [X,Y]f) · Z = 0` at `x`. Jacobi for `f • Z` minus `f` times
Jacobi for `Z`, each bracket expanded by `mlieBracket_smul_right`. -/
lemma jacobi_fun {f : M → ℝ} (hf : CMDiff ∞ f) {X Y Z : Π x : M, TangentSpace I x}
    (hX : CMDiff ∞ (T% X)) (hY : CMDiff ∞ (T% Y)) (hZ : CMDiff ∞ (T% Z)) (x : M) :
    (d% (fun y => d% f y (Y y)) x (X x) - d% (fun y => d% f y (X y)) x (Y x)
      - d% f x (mlieBracket I X Y x)) • Z x = 0 := by
  have : IsManifold I (minSmoothness ℝ 3) M := .of_le (n := ∞) (by simp)
  have : IsManifold I (minSmoothness ℝ 2) M := .of_le (n := ∞) (by simp)
  have : IsManifold I (((2 : ℕ∞) : ℕ∞ω) + 1) M := .of_le (n := ∞) (by simp)
  have md : ∀ {V : Π x : M, TangentSpace I x}, CMDiff ∞ (T% V) → ∀ y, MDiffAt (T% V) y :=
    fun hV y => (hV y).mdifferentiableAt (by simp)
  have mf : ∀ y, MDiffAt f y := fun y => (hf y).mdifferentiableAt (by simp)
  have br : ∀ {U V : Π x : M, TangentSpace I x}, CMDiff ∞ (T% U) → CMDiff ∞ (T% V) →
      MDiffAt (T% (mlieBracket I U V)) x := fun hU hV =>
    (((hU x).of_le (by simp)).mlieBracket_vectorField (m := 1) (n := 2) ((hV x).of_le (by simp))
      (by simp; rfl)).mdifferentiableAt (by simp)
  have hfZ : CMDiff ∞ (T% (f • Z)) := hf.smul_section hZ
  have exp : ∀ V : Π x : M, TangentSpace I x,
      mlieBracket I V (f • Z) = (fun y => d% f y (V y)) • Z + f • mlieBracket I V Z :=
    fun _ => funext fun y => mlieBracket_smul_right (mf y) (md hZ y)
  have j1 := leibniz_identity_mlieBracket_apply (x := x) ((hX x).of_le (by simp))
    ((hY x).of_le (by simp)) ((hfZ x).of_le (by simp))
  have j0 := leibniz_identity_mlieBracket_apply (x := x) ((hX x).of_le (by simp))
    ((hY x).of_le (by simp)) ((hZ x).of_le (by simp))
  rw [exp Y, exp X, exp (mlieBracket I X Y), mlieBracket_add_right ((mdiff_df_apply hf hY x).smul_section (md hZ x))
    ((mf x).smul_section (br hY hZ)), mlieBracket_add_right
    ((mdiff_df_apply hf hX x).smul_section (md hZ x)) ((mf x).smul_section (br hX hZ)),
    mlieBracket_smul_right (mdiff_df_apply hf hY x) (md hZ x), mlieBracket_smul_right (mf x) (br hY hZ),
    mlieBracket_smul_right (mdiff_df_apply hf hX x) (md hZ x), mlieBracket_smul_right (mf x) (br hX hZ),
    Pi.add_apply, Pi.smul_apply', Pi.smul_apply'] at j1
  rw [j0] at j1
  rw [sub_smul, sub_smul]
  linear_combination (norm := module) j1

set_option backward.isDefEq.respectTransparency false in
/-- **K-B, the `Z` slot.** `R(X, Y)(f Z) = f R(X, Y) Z`. -/
theorem curv_smul_right [CovariantDerivative.ContMDiffCovariantDerivative cov (∞ : ℕ∞ω)]
    {f : M → ℝ} (hf : CMDiff ∞ f) {X Y Z : Π x : M, TangentSpace I x} (hX : CMDiff ∞ (T% X))
    (hY : CMDiff ∞ (T% Y)) (hZ : CMDiff ∞ (T% Z)) (x : M) :
    curv cov X Y (f • Z) x = f x • curv cov X Y Z x := by
  have md : ∀ {V : Π x : M, TangentSpace I x}, CMDiff ∞ (T% V) → ∀ y, MDiffAt (T% V) y :=
    fun hV y => (hV y).mdifferentiableAt (by simp)
  have mf : ∀ y, MDiffAt f y := fun y => (hf y).mdifferentiableAt (by simp)
  have hc := cov.isCovariantDerivativeOn (s := univ)
  have s : ∀ V : Π x : M, TangentSpace I x, (fun y => cov (f • Z) y (V y))
      = f • (fun y => cov Z y (V y)) + (fun y => d% f y (V y)) • Z := fun V => funext fun y => by
    rw [hc.leibniz (md hZ y) (mf y)]; rfl
  have e : ∀ {V W : Π x : M, TangentSpace I x}, CMDiff ∞ (T% V) → CMDiff ∞ (T% W) →
      cov (f • (fun y => cov Z y (V y)) + (fun y => d% f y (V y)) • Z) x (W x)
        = f x • cov (fun y => cov Z y (V y)) x (W x) + d% f x (W x) • cov Z x (V x)
          + d% f x (V x) • cov Z x (W x) + d% (fun y => d% f y (V y)) x (W x) • Z x :=
    fun {V W} hV hW => by
      rw [hc.add ((mf x).smul_section (md (covApply_smooth cov hV hZ) x))
        ((mdiff_df_apply hf hV x).smul_section (md hZ x)),
        hc.leibniz (md (covApply_smooth cov hV hZ) x) (mf x),
        hc.leibniz (md hZ x) (mdiff_df_apply hf hV x)]
      simp only [ContinuousLinearMap.add_apply, ContinuousLinearMap.smul_apply,
        ContinuousLinearMap.smulRight_apply]
      abel
  unfold curv
  rw [s Y, s X, e hY hX, e hX hY, hc.leibniz (md hZ x) (mf x)]
  simp only [ContinuousLinearMap.add_apply, ContinuousLinearMap.smul_apply,
    ContinuousLinearMap.smulRight_apply]
  have j := jacobi_fun hf hX hY hZ x
  rw [sub_smul, sub_smul] at j
  linear_combination (norm := module) j

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

/-! ## Probe K3 — Ricci and scalar curvature over one fibre -/

section Fibre

variable {V : Type*} [AddCommGroup V] [Module ℝ V] [FiniteDimensional ℝ V]

/-- **K-D.** The Ricci form of a curvature-type map `R`: `Ric(u, v) = tr (w ↦ R(w, u) v)`. -/
noncomputable def ricci (R : V →ₗ[ℝ] V →ₗ[ℝ] V →ₗ[ℝ] V) : V →ₗ[ℝ] V →ₗ[ℝ] ℝ :=
  LinearMap.mk₂ ℝ (fun u v => LinearMap.trace ℝ V ((R.flip u).flip v))
    (fun u u' v => by
      rw [show (R.flip (u + u')).flip v = (R.flip u).flip v + (R.flip u').flip v by ext; simp,
        map_add])
    (fun c u v => by
      rw [show (R.flip (c • u)).flip v = c • (R.flip u).flip v by ext; simp, map_smul,
        smul_eq_mul])
    (fun u v v' => by simp [map_add, LinearMap.flip_apply])
    (fun c u v => by simp [map_smul, LinearMap.flip_apply])

lemma ricci_apply (R : V →ₗ[ℝ] V →ₗ[ℝ] V →ₗ[ℝ] V) (u v : V) :
    ricci R u v = LinearMap.trace ℝ V ((R.flip u).flip v) := rfl

/-- **K-E.** The scalar curvature: the trace of `g⁻¹ ∘ Ric`, through a nondegenerate form `g`. Basis-free. -/
noncomputable def scal (R : V →ₗ[ℝ] V →ₗ[ℝ] V →ₗ[ℝ] V) (g : LinearMap.BilinForm ℝ V)
    (hg : g.Nondegenerate) : ℝ :=
  LinearMap.trace ℝ V ((g.toDual hg).symm.toLinearMap ∘ₗ ricci R)

/-- What `scal` is, in any basis: `Σᵢ Ric(bᵢ*, bᵢ)`, with `b*` the `g`-dual basis. -/
theorem scal_eq_sum {ι : Type*} [Fintype ι] [DecidableEq ι] (R : V →ₗ[ℝ] V →ₗ[ℝ] V →ₗ[ℝ] V)
    (g : LinearMap.BilinForm ℝ V) (hg : g.Nondegenerate) (b : Module.Basis ι ℝ V) :
    scal R g hg = ∑ i, ricci R (g.dualBasis hg b i) (b i) := by
  rw [scal, LinearMap.trace_eq_matrix_trace ℝ (g.dualBasis hg b), Matrix.trace]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [Matrix.diag_apply, LinearMap.toMatrix_apply, LinearMap.BilinForm.dualBasis_repr_apply,
    LinearMap.comp_apply, LinearEquiv.coe_coe, LinearMap.BilinForm.apply_toDual_symm_apply]

end Fibre

/-! ## Probe K4 — the instance: the scalar curvature of `covConf a`, the programme's 2D conformal metric

R3's connection for `a(η)²(−dη² + dx²)` is copied verbatim from `ConformalLCProbe.lean`; the copied lines count
against K4's budget. -/

section Instance

/-- `−dη² + dx²`. Copied from `ConformalLCProbe.lean`. -/
noncomputable def minkForm : ℝ × ℝ →L[ℝ] ℝ × ℝ →L[ℝ] ℝ :=
  -((ContinuousLinearMap.mul ℝ ℝ).bilinearComp (ContinuousLinearMap.fst ℝ ℝ ℝ)
      (ContinuousLinearMap.fst ℝ ℝ ℝ))
    + (ContinuousLinearMap.mul ℝ ℝ).bilinearComp (ContinuousLinearMap.snd ℝ ℝ ℝ)
      (ContinuousLinearMap.snd ℝ ℝ ℝ)

lemma minkForm_apply (v w : ℝ × ℝ) : minkForm v w = -(v.1 * w.1) + v.2 * w.2 := by
  simp [minkForm]

/-- `φ′ = a′/a` at `p`. -/
noncomputable def phi' (a : ℝ → ℝ) (p : ℝ × ℝ) : ℝ := deriv a p.1 / a p.1

/-- `Γ_p(·, w)`. -/
noncomputable def Gam (a : ℝ → ℝ) (p w : ℝ × ℝ) : ℝ × ℝ →L[ℝ] ℝ × ℝ :=
  phi' a p • ((ContinuousLinearMap.fst ℝ ℝ ℝ).smulRight w + w.1 • ContinuousLinearMap.id ℝ (ℝ × ℝ)
    + (minkForm.flip w).smulRight ((1 : ℝ), (0 : ℝ)))

lemma Gam_apply (a : ℝ → ℝ) (p w v : ℝ × ℝ) :
    Gam a p w v = phi' a p • (v.1 • w + w.1 • v + minkForm v w • ((1 : ℝ), (0 : ℝ))) := by
  simp [Gam]

lemma Gam_symm (a : ℝ → ℝ) (p v w : ℝ × ℝ) : Gam a p w v = Gam a p v w := by
  rw [Gam_apply, Gam_apply, minkForm_apply, minkForm_apply]
  ext <;> simp <;> ring

lemma Gam_add (a : ℝ → ℝ) (p w w' : ℝ × ℝ) : Gam a p (w + w') = Gam a p w + Gam a p w' := by
  refine ContinuousLinearMap.ext fun v => ?_
  rw [ContinuousLinearMap.add_apply, Gam_apply, Gam_apply, Gam_apply]
  simp only [minkForm_apply]; ext <;> simp <;> ring

lemma Gam_smul (a : ℝ → ℝ) (p w : ℝ × ℝ) (c : ℝ) : Gam a p (c • w) = c • Gam a p w := by
  refine ContinuousLinearMap.ext fun v => ?_
  rw [ContinuousLinearMap.smul_apply, Gam_apply, Gam_apply]
  simp only [minkForm_apply]; ext <;> simp <;> ring

set_option backward.isDefEq.respectTransparency false in
/-- On `ℝ × ℝ` as a manifold, a section differentiable in the bundle sense is differentiable. -/
/- The models are written out: for `M = ℝ × ℝ` the `MDiffAt`/`T%` notation infers the PRODUCT model
`𝓘(ℝ, ℝ).prod 𝓘(ℝ, ℝ)`, while `CovariantDerivative 𝓘(ℝ, ℝ × ℝ) …` fixes `𝓘(ℝ, ℝ × ℝ)`. -/
lemma diff_of_mdiff {σ : Π p : ℝ × ℝ, TangentSpace 𝓘(ℝ, ℝ × ℝ) p} {x : ℝ × ℝ}
    (h : MDifferentiableAt 𝓘(ℝ, ℝ × ℝ) 𝓘(ℝ, ℝ × ℝ).tangent
      (fun y => (⟨y, σ y⟩ : TangentBundle 𝓘(ℝ, ℝ × ℝ) (ℝ × ℝ))) x) :
    DifferentiableAt ℝ (fun y => (σ y : ℝ × ℝ)) x := by
  rw [mdifferentiableAt_totalSpace] at h
  obtain ⟨-, h2⟩ := h
  have : (fun y => (trivializationAt (ℝ × ℝ) (TangentSpace 𝓘(ℝ, ℝ × ℝ)) x ⟨y, σ y⟩).2)
      = fun y => (σ y : ℝ × ℝ) := by
    funext y; simp
  rw [this] at h2
  exact mdifferentiableAt_iff_differentiableAt.mp h2

/-- The connection's underlying function: `∇_v Y (p) = DY(p) v + Γ_p(v, Y p)`. -/
noncomputable def covFun (a : ℝ → ℝ) (Y : Π p : ℝ × ℝ, TangentSpace 𝓘(ℝ, ℝ × ℝ) p) (p : ℝ × ℝ) :
    TangentSpace 𝓘(ℝ, ℝ × ℝ) p →L[ℝ] TangentSpace 𝓘(ℝ, ℝ × ℝ) p :=
  fderiv ℝ (Y : ℝ × ℝ → ℝ × ℝ) p + Gam a p (Y p)

set_option backward.isDefEq.respectTransparency false in
/-- **R3 (B8), part 1.** It is a covariant derivative. -/
noncomputable def covConf (a : ℝ → ℝ) :
    CovariantDerivative 𝓘(ℝ, ℝ × ℝ) (ℝ × ℝ) (TangentSpace 𝓘(ℝ, ℝ × ℝ) : ℝ × ℝ → Type _) where
  toFun := covFun a
  isCovariantDerivativeOnUniv :=
    { add := by
        intro σ σ' x hσ hσ' _
        simp only [covFun]
        rw [show ((σ + σ' : Π p : ℝ × ℝ, TangentSpace 𝓘(ℝ, ℝ × ℝ) p) : ℝ × ℝ → ℝ × ℝ)
          = (σ : ℝ × ℝ → ℝ × ℝ) + (σ' : ℝ × ℝ → ℝ × ℝ) from rfl,
          fderiv_add (diff_of_mdiff (σ := σ) (x := x) hσ) (diff_of_mdiff (σ := σ') (x := x) hσ')]
        rw [show (σ + σ') x = σ x + σ' x from rfl, Gam_add]
        abel
      leibniz := by
        intro σ g x hσ hg _
        simp only [covFun]
        have hgd : DifferentiableAt ℝ g x := mdifferentiableAt_iff_differentiableAt.mp hg
        rw [show ((g • σ : Π p : ℝ × ℝ, TangentSpace 𝓘(ℝ, ℝ × ℝ) p) : ℝ × ℝ → ℝ × ℝ)
          = fun y => g y • (σ : ℝ × ℝ → ℝ × ℝ) y from rfl,
          fderiv_fun_smul hgd (diff_of_mdiff (σ := σ) (x := x) hσ)]
        beta_reduce
        rw [Gam_smul]
        simp only [mvfderiv_eq_fderiv]
        refine ContinuousLinearMap.ext fun v => ?_
        simp only [ContinuousLinearMap.add_apply, ContinuousLinearMap.smul_apply,
          ContinuousLinearMap.smulRight_apply, ContinuousLinearMap.coe_comp',
          Function.comp_apply, smul_add]
        show g x • fderiv ℝ (fun y => (show ℝ × ℝ from σ y)) x v
            + fderiv ℝ g x v • (show ℝ × ℝ from σ x) + g x • Gam a x (σ x) v
          = g x • fderiv ℝ (fun y => (show ℝ × ℝ from σ y)) x v + g x • Gam a x (σ x) v
            + fderiv ℝ g x v • (show ℝ × ℝ from σ x)
        abel }

lemma covConf_apply (a : ℝ → ℝ) (Y : Π p : ℝ × ℝ, TangentSpace 𝓘(ℝ, ℝ × ℝ) p) (p v : ℝ × ℝ) :
    covConf a Y p v = fderiv ℝ (Y : ℝ × ℝ → ℝ × ℝ) p v + Gam a p (Y p) v := rfl

set_option backward.isDefEq.respectTransparency false in
lemma mlieBracket_const₂ (u v p : ℝ × ℝ) :
    mlieBracket 𝓘(ℝ, ℝ × ℝ) (fun _ => (u : ℝ × ℝ)) (fun _ => (v : ℝ × ℝ)) p = 0 := by
  rw [← mlieBracketWithin_univ, mlieBracketWithin_eq_lieBracketWithin, lieBracketWithin_univ,
    lieBracket_eq]
  simp

/-- `(log a)″` at `p`. -/
noncomputable def phi'' (a : ℝ → ℝ) (p : ℝ × ℝ) : ℝ := deriv (fun t => deriv a t / a t) p.1

set_option backward.isDefEq.respectTransparency false in
/-- **The curvature of `covConf a`**, on constant fields: `R(u,v)w = (log a)″ (u₁v₂ − u₂v₁) (w₂, w₁)`. -/
theorem curv_conf (a : ℝ → ℝ) (p u v w : ℝ × ℝ)
    (hd : DifferentiableAt ℝ (fun t => deriv a t / a t) p.1) :
    curv (covConf a) (fun _ => u) (fun _ => v) (fun _ => w) p
      = (phi'' a p * (u.1 * v.2 - u.2 * v.1)) • (w.2, w.1) := by
  have hphi : HasFDerivAt (phi' a) ((phi'' a p) • ContinuousLinearMap.fst ℝ ℝ ℝ) p :=
    hd.hasDerivAt.comp_hasFDerivAt p (hasFDerivAt_fst)
  have hD : ∀ K d : ℝ × ℝ, fderiv ℝ (fun y => phi' a y • K) p d = (phi'' a p * d.1) • K :=
    fun K d => by rw [(hphi.smul_const K).fderiv]; simp [mul_comm]
  have h0 : ∀ (y c : ℝ × ℝ), fderiv ℝ (fun _ : ℝ × ℝ => (w : ℝ × ℝ)) y c = 0 := by simp
  unfold curv
  simp only [covConf_apply, h0, zero_add, Gam_apply, minkForm_apply, hD, mlieBracket_const₂,
    map_zero, sub_zero]
  have fa : ∀ x y : TangentSpace 𝓘(ℝ, ℝ × ℝ) p, (x + y).1 = x.1 + y.1 ∧ (x + y).2 = x.2 + y.2 :=
    fun _ _ => ⟨rfl, rfl⟩
  have fs : ∀ x y : TangentSpace 𝓘(ℝ, ℝ × ℝ) p, (x - y).1 = x.1 - y.1 ∧ (x - y).2 = x.2 - y.2 :=
    fun _ _ => ⟨rfl, rfl⟩
  have fm : ∀ (c : ℝ) (x : TangentSpace 𝓘(ℝ, ℝ × ℝ) p), (c • x).1 = c * x.1 ∧ (c • x).2 = c * x.2 :=
    fun _ _ => ⟨rfl, rfl⟩
  refine Prod.ext ?_ ?_ <;>
    simp only [fun x y => (fa x y).1, fun x y => (fa x y).2, fun x y => (fs x y).1,
      fun x y => (fs x y).2, fun c x => (fm c x).1, fun c x => (fm c x).2, Prod.fst_add,
      Prod.snd_add, Prod.smul_fst, Prod.smul_snd, smul_eq_mul, Prod.fst_sub, Prod.snd_sub] <;> ring

/-- `det(u, v) = u₁v₂ − u₂v₁`. -/
noncomputable def det2 : (ℝ × ℝ) →ₗ[ℝ] (ℝ × ℝ) →ₗ[ℝ] ℝ :=
  LinearMap.mk₂ ℝ (fun u v => u.1 * v.2 - u.2 * v.1) (fun _ _ _ => by simp; ring)
    (fun _ _ _ => by simp; ring) (fun _ _ _ => by simp; ring) (fun _ _ _ => by simp; ring)

/-- The curvature of `covConf a` at `p`, as a trilinear map. -/
noncomputable def Rconf (a : ℝ → ℝ) (p : ℝ × ℝ) :
    (ℝ × ℝ) →ₗ[ℝ] (ℝ × ℝ) →ₗ[ℝ] (ℝ × ℝ) →ₗ[ℝ] (ℝ × ℝ) :=
  phi'' a p • det2.compr₂ (LinearMap.smulRight LinearMap.id
    ((LinearMap.snd ℝ ℝ ℝ).prod (LinearMap.fst ℝ ℝ ℝ)))

lemma Rconf_apply (a : ℝ → ℝ) (p u v w : ℝ × ℝ) :
    Rconf a p u v w = (phi'' a p * (u.1 * v.2 - u.2 * v.1)) • (w.2, w.1) := by
  simp [Rconf, det2, mul_smul]

/-- `Rconf` IS the curvature of `covConf a`, on constant fields. -/
theorem Rconf_eq_curv (a : ℝ → ℝ) (p u v w : ℝ × ℝ)
    (hd : DifferentiableAt ℝ (fun t => deriv a t / a t) p.1) :
    Rconf a p u v w = curv (covConf a) (fun _ => u) (fun _ => v) (fun _ => w) p := by
  rw [Rconf_apply, curv_conf a p u v w hd]

/-- `a(η)²(−dη² + dx²)` at `p`, as a bilinear form. -/
noncomputable def gB (a : ℝ → ℝ) (p : ℝ × ℝ) : LinearMap.BilinForm ℝ (ℝ × ℝ) :=
  LinearMap.mk₂ ℝ (fun v w => a p.1 ^ 2 * (-(v.1 * w.1) + v.2 * w.2)) (fun _ _ _ => by simp; ring)
    (fun _ _ _ => by simp; ring) (fun _ _ _ => by simp; ring) (fun _ _ _ => by simp; ring)

lemma gB_nondeg (a : ℝ → ℝ) (p : ℝ × ℝ) (ha : a p.1 ≠ 0) : (gB a p).Nondegenerate := by
  refine ⟨fun m hm => ?_, fun m hm => ?_⟩
  · have h1 := hm (1, 0); have h2 := hm (0, 1)
    simp [gB, ha] at h1 h2; exact Prod.ext h1 h2
  · have h1 := hm (1, 0); have h2 := hm (0, 1)
    simp [gB, ha] at h1 h2; exact Prod.ext h1 h2

lemma dual_conf (a : ℝ → ℝ) (p : ℝ × ℝ) (ha : a p.1 ≠ 0) (i : Fin 2) :
    (gB a p).dualBasis (gB_nondeg a p ha) (Module.Basis.finTwoProd ℝ) i
      = ![(-1 / a p.1 ^ 2, 0), (0, 1 / a p.1 ^ 2)] i := by
  refine ((gB a p).dualBasis (gB_nondeg a p ha) (Module.Basis.finTwoProd ℝ)).ext_elem fun j => ?_
  rw [Module.Basis.repr_self, LinearMap.BilinForm.dualBasis_repr_apply]
  fin_cases i <;> fin_cases j <;> simp [gB] <;> field_simp

/-- **The Ricci form of `covConf a`:** `Ric = (log a)″ (−dη² + dx²)`. -/
lemma ricci_conf (a : ℝ → ℝ) (p u v : ℝ × ℝ) :
    ricci (Rconf a p) u v = phi'' a p * (-(u.1 * v.1) + u.2 * v.2) := by
  rw [ricci_apply, LinearMap.trace_eq_matrix_trace ℝ (Module.Basis.finTwoProd ℝ), Matrix.trace_fin_two]
  simp [LinearMap.toMatrix_apply, Rconf_apply]
  ring

/-- **K-G. The scalar curvature of `a(η)²(−dη² + dx²)`, through its explicit connection `covConf a`:**
`R = 2 (log a)″ / a²`. -/
theorem scal_conf (a : ℝ → ℝ) (p : ℝ × ℝ) (ha : a p.1 ≠ 0) :
    scal (Rconf a p) (gB a p) (gB_nondeg a p ha) = 2 * phi'' a p / a p.1 ^ 2 := by
  rw [scal_eq_sum _ _ _ (Module.Basis.finTwoProd ℝ), Fin.sum_univ_two, dual_conf a p ha,
    dual_conf a p ha,
    ricci_conf, ricci_conf]
  simp
  field_simp
  ring

end Instance

/-! ## `r7289`, Probe F1 — the Einstein tensor and the field equations, over a fibre

The trace of a bilinear form against `g` generalises K3's `scal`. -/

section Fields

variable {V : Type*} [AddCommGroup V] [Module ℝ V] [FiniteDimensional ℝ V]

/-- The `g`-trace of a bilinear form: `tr (g⁻¹ ∘ H)`. -/
noncomputable def trG (H : V →ₗ[ℝ] V →ₗ[ℝ] ℝ) (g : LinearMap.BilinForm ℝ V) (hg : g.Nondegenerate) : ℝ :=
  LinearMap.trace ℝ V ((g.toDual hg).symm.toLinearMap ∘ₗ H)

theorem trG_eq_sum {ι : Type*} [Fintype ι] [DecidableEq ι] (H : V →ₗ[ℝ] V →ₗ[ℝ] ℝ)
    (g : LinearMap.BilinForm ℝ V) (hg : g.Nondegenerate) (b : Module.Basis ι ℝ V) :
    trG H g hg = ∑ i, H (g.dualBasis hg b i) (b i) := by
  rw [trG, LinearMap.trace_eq_matrix_trace ℝ (g.dualBasis hg b), Matrix.trace]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [Matrix.diag_apply, LinearMap.toMatrix_apply, LinearMap.BilinForm.dualBasis_repr_apply,
    LinearMap.comp_apply, LinearEquiv.coe_coe, LinearMap.BilinForm.apply_toDual_symm_apply]

/-- **G4a.** The Einstein tensor `Ein = Ric − ½ R g`. -/
noncomputable def einstein (R : V →ₗ[ℝ] V →ₗ[ℝ] V →ₗ[ℝ] V) (g : LinearMap.BilinForm ℝ V)
    (hg : g.Nondegenerate) : V →ₗ[ℝ] V →ₗ[ℝ] ℝ :=
  ricci R - ((1 / 2 : ℝ) * scal R g hg) • g

/-- **G4a.** Einstein's equations with `Λ`, coupling `κ` (`= 8πG`) and a source `T`: `Ein + Λ g = κ T`. -/
def FieldEq (R : V →ₗ[ℝ] V →ₗ[ℝ] V →ₗ[ℝ] V) (g : LinearMap.BilinForm ℝ V) (hg : g.Nondegenerate)
    (Λ κ : ℝ) (T : V →ₗ[ℝ] V →ₗ[ℝ] ℝ) : Prop :=
  einstein R g hg + Λ • g = κ • T

/-- **G4a.** A perfect fluid with density `ρ`, pressure `p` and velocity `U`: `(ρ + p) U♭ ⊗ U♭ + p g`. -/
noncomputable def perfectFluid (g : LinearMap.BilinForm ℝ V) (ρ p : ℝ) (U : V) :
    V →ₗ[ℝ] V →ₗ[ℝ] ℝ :=
  (ρ + p) • LinearMap.mk₂ ℝ (fun v w => g U v * g U w) (fun _ _ _ => by simp [add_mul])
    (fun _ _ _ => by simp [mul_assoc]) (fun _ _ _ => by simp [mul_add])
    (fun _ _ _ => by simp; ring) + p • g

end Fields

/-- **F1, the instance.** In two dimensions the Einstein tensor of `covConf a` vanishes identically. -/
theorem einstein_conf (a : ℝ → ℝ) (p : ℝ × ℝ) (ha : a p.1 ≠ 0) :
    einstein (Rconf a p) (gB a p) (gB_nondeg a p ha) = 0 := by
  refine LinearMap.ext₂ fun u v => ?_
  rw [einstein, scal_conf a p ha, LinearMap.sub_apply, LinearMap.sub_apply, ricci_conf]
  simp only [LinearMap.smul_apply, gB, LinearMap.mk₂_apply, smul_eq_mul, LinearMap.zero_apply]
  field_simp
  ring

/-! ## `r7289`, Probe F2 — the Hessian and the wave operator, the connection a hypothesis -/

section Wave

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  {H : Type*} [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  {M : Type*} [TopologicalSpace M] [ChartedSpace H M] [IsManifold I ∞ M]

/-- **G4b.** The Hessian of `f` for a connection `cov`: `Hess f (X, Y) = X(Y f) − (∇_X Y) f`. -/
noncomputable def hess (cov : CovariantDerivative I E (TangentSpace I : M → Type _)) (f : M → ℝ)
    (X Y : Π x : M, TangentSpace I x) (x : M) : ℝ :=
  d% (fun y => d% f y (Y y)) x (X x) - d% f x (cov Y x (X x))

lemma hess_smul_left (cov : CovariantDerivative I E (TangentSpace I : M → Type _)) (f g : M → ℝ)
    (X Y : Π x : M, TangentSpace I x) (x : M) : hess cov f (g • X) Y x = g x * hess cov f X Y x := by
  simp only [hess, Pi.smul_apply', map_smul, smul_eq_mul]
  ring

set_option backward.isDefEq.respectTransparency false in
/-- `Hess f` is `C^∞`-linear in its second slot too. -/
lemma hess_smul_right (cov : CovariantDerivative I E (TangentSpace I : M → Type _)) {f g : M → ℝ}
    (hf : CMDiff ∞ f) (hg : CMDiff ∞ g) {X Y : Π x : M, TangentSpace I x} (hY : CMDiff ∞ (T% Y))
    (x : M) : hess cov f X (g • Y) x = g x * hess cov f X Y x := by
  have mg : MDiffAt g x := (hg x).mdifferentiableAt (by simp)
  have mY : MDiffAt (T% Y) x := (hY x).mdifferentiableAt (by simp)
  have e : (fun y => d% f y ((g • Y) y)) = g * fun y => d% f y (Y y) := by
    funext y; simp [Pi.smul_apply', map_smul]
  rw [hess, e, mvfderiv_mul mg (mdiff_df_apply hf hY x),
    (cov.isCovariantDerivativeOn (s := univ)).leibniz mY mg, hess]
  simp only [ContinuousLinearMap.add_apply, ContinuousLinearMap.smul_apply,
    ContinuousLinearMap.smulRight_apply, map_add, map_smul, smul_eq_mul]
  ring

end Wave

/-- **G4b.** The wave operator over a fibre: the `g`-trace of a Hessian. -/
noncomputable abbrev box {V : Type*} [AddCommGroup V] [Module ℝ V] [FiniteDimensional ℝ V]
    (Hs : V →ₗ[ℝ] V →ₗ[ℝ] ℝ) (g : LinearMap.BilinForm ℝ V) (hg : g.Nondegenerate) : ℝ := trG Hs g hg

/-- The Hessian of `f` for `covConf a` at `p`, on constant fields, as a bilinear form. -/
noncomputable def hessConf (a : ℝ → ℝ) (f : ℝ × ℝ → ℝ) (p : ℝ × ℝ) :
    (ℝ × ℝ) →ₗ[ℝ] (ℝ × ℝ) →ₗ[ℝ] ℝ :=
  LinearMap.mk₂ ℝ (fun u v => fderiv ℝ (fderiv ℝ f) p u v - fderiv ℝ f p (Gam a p v u))
    (fun _ _ _ => by simp; ring) (fun _ _ _ => by simp; ring)
    (fun _ _ _ => by simp [Gam_add]; ring) (fun _ _ _ => by simp [Gam_smul]; ring)

set_option backward.isDefEq.respectTransparency false in
/-- `hessConf` IS the Hessian of `f` for `covConf a`, on constant fields. -/
theorem hessConf_eq (a : ℝ → ℝ) (f : ℝ × ℝ → ℝ) (p u v : ℝ × ℝ) (hf : ContDiff ℝ 2 f) :
    hessConf a f p u v = hess (covConf a) f (fun _ => u) (fun _ => v) p := by
  have h1 : DifferentiableAt ℝ (fderiv ℝ f) p :=
    (hf.fderiv_right (m := 1) (by norm_num)).differentiable (by norm_num) p
  simp only [hess, mvfderiv_eq_fderiv]
  show _ = fderiv ℝ (fun y => fderiv ℝ f y v) p u - fderiv ℝ f p (covConf a (fun _ => v) p u)
  rw [fderiv_clm_apply h1 (differentiableAt_const v), covConf_apply]
  simp [hessConf]

/-- **F2, the instance.** On `a(η)²(−dη² + dx²)`, `□ f = a⁻² (−f_ηη + f_xx)`: the connection terms cancel. -/
theorem box_conf (a : ℝ → ℝ) (f : ℝ × ℝ → ℝ) (p : ℝ × ℝ) (ha : a p.1 ≠ 0) :
    box (hessConf a f p) (gB a p) (gB_nondeg a p ha)
      = (-(fderiv ℝ (fderiv ℝ f) p (1, 0) (1, 0)) + fderiv ℝ (fderiv ℝ f) p (0, 1) (0, 1))
        / a p.1 ^ 2 := by
  rw [box, trG_eq_sum _ _ _ (Module.Basis.finTwoProd ℝ), Fin.sum_univ_two, dual_conf a p ha,
    dual_conf a p ha]
  simp only [hessConf, LinearMap.mk₂_apply, Matrix.cons_val_zero, Matrix.cons_val_one,
    Module.Basis.finTwoProd_zero, Module.Basis.finTwoProd_one, Gam_apply, minkForm_apply]
  have hm : ∀ (c : ℝ) (w : ℝ × ℝ), fderiv ℝ (fderiv ℝ f) p (c • w) = c • fderiv ℝ (fderiv ℝ f) p w :=
    fun c w => map_smul _ c w
  rw [show ((-1 / a p.1 ^ 2, 0) : ℝ × ℝ) = (-1 / a p.1 ^ 2) • ((1 : ℝ), (0 : ℝ)) by simp,
    show ((0, 1 / a p.1 ^ 2) : ℝ × ℝ) = (1 / a p.1 ^ 2) • ((0 : ℝ), (1 : ℝ)) by simp, hm, hm]
  have hl : ∀ c : ℝ, fderiv ℝ f p (c, 0) = c * fderiv ℝ f p (1, 0) := fun c => by
    rw [show ((c, 0) : ℝ × ℝ) = c • ((1 : ℝ), (0 : ℝ)) by simp, map_smul, smul_eq_mul]
  simp
  rw [hl (phi' a p * (-1 / a p.1 ^ 2)), hl (phi' a p * (a p.1 ^ 2)⁻¹)]
  field_simp
  ring

/-! ## `r7289`, Probe F3 — the covariant derivative of a `(0,2)` field, the connection a hypothesis -/

section Tensor2

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  {H : Type*} [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  {M : Type*} [TopologicalSpace M] [ChartedSpace H M] [IsManifold I ∞ M]
  (cov : CovariantDerivative I E (TangentSpace I : M → Type _))
  (T : Π x : M, TangentSpace I x →L[ℝ] TangentSpace I x →L[ℝ] ℝ)

/-- **G4a, G4b.** `∇T (X; Y, Z) = X(T(Y,Z)) − T(∇_X Y, Z) − T(Y, ∇_X Z)`. -/
noncomputable def covT (X Y Z : Π x : M, TangentSpace I x) (x : M) : ℝ :=
  d% (fun y => T y (Y y) (Z y)) x (X x) - T x (cov Y x (X x)) (Z x) - T x (Y x) (cov Z x (X x))

lemma covT_smul_X (g : M → ℝ) (X Y Z : Π x : M, TangentSpace I x) (x : M) :
    covT cov T (g • X) Y Z x = g x * covT cov T X Y Z x := by
  simp only [covT, Pi.smul_apply', map_smul, ContinuousLinearMap.smul_apply, smul_eq_mul]
  ring

set_option backward.isDefEq.respectTransparency false in
/-- `C^∞`-linear in `Y`, given that `T(Y, Z)` is differentiable at `x`. -/
lemma covT_smul_Y {g : M → ℝ} (hg : CMDiff ∞ g) {X Y Z : Π x : M, TangentSpace I x}
    (hY : CMDiff ∞ (T% Y)) (x : M) (hT : MDiffAt (fun y => T y (Y y) (Z y)) x) :
    covT cov T X (g • Y) Z x = g x * covT cov T X Y Z x := by
  have mg : MDiffAt g x := (hg x).mdifferentiableAt (by simp)
  have e : (fun y => T y ((g • Y) y) (Z y)) = g * fun y => T y (Y y) (Z y) := by
    funext y; simp [Pi.smul_apply', map_smul]
  rw [covT, e, mvfderiv_mul mg hT,
    (cov.isCovariantDerivativeOn (s := univ)).leibniz ((hY x).mdifferentiableAt (by simp)) mg, covT]
  simp only [ContinuousLinearMap.add_apply, ContinuousLinearMap.smul_apply,
    ContinuousLinearMap.smulRight_apply, Pi.smul_apply', map_add, map_smul, smul_eq_mul]
  ring

set_option backward.isDefEq.respectTransparency false in
/-- `C^∞`-linear in `Z`, given that `T(Y, Z)` is differentiable at `x`. -/
lemma covT_smul_Z {g : M → ℝ} (hg : CMDiff ∞ g) {X Y Z : Π x : M, TangentSpace I x}
    (hZ : CMDiff ∞ (T% Z)) (x : M) (hT : MDiffAt (fun y => T y (Y y) (Z y)) x) :
    covT cov T X Y (g • Z) x = g x * covT cov T X Y Z x := by
  have mg : MDiffAt g x := (hg x).mdifferentiableAt (by simp)
  have e : (fun y => T y (Y y) ((g • Z) y)) = g * fun y => T y (Y y) (Z y) := by
    funext y; simp [Pi.smul_apply', map_smul]
  rw [covT, e, mvfderiv_mul mg hT,
    (cov.isCovariantDerivativeOn (s := univ)).leibniz ((hZ x).mdifferentiableAt (by simp)) mg, covT]
  simp only [ContinuousLinearMap.add_apply, ContinuousLinearMap.smul_apply,
    ContinuousLinearMap.smulRight_apply, Pi.smul_apply', map_add, map_smul, smul_eq_mul]
  ring

end Tensor2

/-! ## `r7291`, Probe S2 — the second fundamental form, the connection and the metric hypotheses -/

section Sff

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  {H : Type*} [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  {M : Type*} [TopologicalSpace M] [ChartedSpace H M] [IsManifold I ∞ M]
  (cov : CovariantDerivative I E (TangentSpace I : M → Type _))
  (g : Π x : M, TangentSpace I x →L[ℝ] TangentSpace I x →L[ℝ] ℝ)

/-- **G3c.** The second fundamental form of a field `N`: `K(X, Y) = g(∇_X N, Y)`. -/
noncomputable def sff (N X Y : Π x : M, TangentSpace I x) (x : M) : ℝ := g x (cov N x (X x)) (Y x)

lemma sff_smul_X (N X Y : Π x : M, TangentSpace I x) (f : M → ℝ) (x : M) :
    sff cov g N (f • X) Y x = f x * sff cov g N X Y x := by
  simp [sff, Pi.smul_apply', map_smul]

lemma sff_smul_Y (N X Y : Π x : M, TangentSpace I x) (f : M → ℝ) (x : M) :
    sff cov g N X (f • Y) x = f x * sff cov g N X Y x := by
  simp [sff, Pi.smul_apply', map_smul]

/-- **G3c. `K` is symmetric** on fields tangent to the slice, for a torsion-free `cov` compatible with `g` along
`X` and `Y`, when `N` is everywhere `g`-normal to `X` and `Y` and `[X, Y]` is tangent at `x`. -/
theorem sff_symm (htor : cov.torsion = 0) {N X Y : Π x : M, TangentSpace I x}
    (hX : MDiffAt (T% X) x) (hY : MDiffAt (T% Y) x)
    (hNX : ∀ y, g y (N y) (X y) = 0) (hNY : ∀ y, g y (N y) (Y y) = 0)
    (hcX : d% (fun y => g y (N y) (Y y)) x (X x)
      = g x (cov N x (X x)) (Y x) + g x (N x) (cov Y x (X x)))
    (hcY : d% (fun y => g y (N y) (X y)) x (Y x)
      = g x (cov N x (Y x)) (X x) + g x (N x) (cov X x (Y x)))
    (hbr : g x (N x) (mlieBracket I X Y x) = 0) :
    sff cov g N X Y x = sff cov g N Y X x := by
  have z : ∀ {Z : Π x : M, TangentSpace I x}, (∀ y, g y (N y) (Z y) = 0) →
      d% (fun y => g y (N y) (Z y)) x = 0 := fun {Z} h => by
    rw [show (fun y => g y (N y) (Z y)) = fun _ => (0 : ℝ) from funext h]; exact mvfderiv_const _
  rw [z hNY, ContinuousLinearMap.zero_apply] at hcX
  rw [z hNX, ContinuousLinearMap.zero_apply] at hcY
  have ht := (CovariantDerivative.torsion_eq_zero_iff (cov := cov)).1 htor hX hY
  have hb : g x (N x) (cov Y x (X x)) - g x (N x) (cov X x (Y x)) = 0 := by
    rw [← map_sub, ht, hbr]
  simp only [sff]
  linarith

end Sff

/-! ## `r7291`, Probe S1 — the induced metric of a map, and the flat slicing of de Sitter -/

section Pull

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
  {H : Type*} [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  {M : Type*} [TopologicalSpace M] [ChartedSpace H M]
  {E' : Type*} [NormedAddCommGroup E'] [NormedSpace ℝ E']
  {H' : Type*} [TopologicalSpace H'] {I' : ModelWithCorners ℝ E' H'}
  {M' : Type*} [TopologicalSpace M'] [ChartedSpace H' M']
  {E'' : Type*} [NormedAddCommGroup E''] [NormedSpace ℝ E'']
  {H'' : Type*} [TopologicalSpace H''] {I'' : ModelWithCorners ℝ E'' H''}
  {M'' : Type*} [TopologicalSpace M''] [ChartedSpace H'' M'']

/-- **G3a.** The pullback of a metric along a map: `(φ*g)ₓ(u, v) = g_{φ x}(dφ u, dφ v)`. -/
noncomputable def pullG (φ : M → M') (g : Π y : M', LinearMap.BilinForm ℝ (TangentSpace I' y))
    (x : M) : LinearMap.BilinForm ℝ (TangentSpace I x) :=
  (g (φ x)).compl₁₂ (mfderiv I I' φ x : TangentSpace I x →ₗ[ℝ] _)
    (mfderiv I I' φ x : TangentSpace I x →ₗ[ℝ] _)

lemma pullG_apply (φ : M → M') (g : Π y : M', LinearMap.BilinForm ℝ (TangentSpace I' y))
    (x : M) (u v : TangentSpace I x) :
    pullG (I := I) (I' := I') φ g x u v = g (φ x) (mfderiv I I' φ x u) (mfderiv I I' φ x v) := rfl

/-- The pullback of a symmetric form is symmetric. -/
lemma pullG_symm (φ : M → M') (g : Π y : M', LinearMap.BilinForm ℝ (TangentSpace I' y))
    (hg : ∀ y u v, g y u v = g y v u) (x : M) (u v : TangentSpace I x) :
    pullG (I := I) (I' := I') φ g x u v = pullG (I := I) (I' := I') φ g x v u := hg _ _ _

/-- Pulling back twice is pulling back along the composite — so a slice of a slice is a slice. -/
lemma pullG_comp (ψ : M' → M'') (φ : M → M')
    (g : Π y : M'', LinearMap.BilinForm ℝ (TangentSpace I'' y)) {x : M}
    (hψ : MDifferentiableAt I' I'' ψ (φ x)) (hφ : MDifferentiableAt I I' φ x) (u v : TangentSpace I x) :
    pullG (I := I) (I' := I'') (ψ ∘ φ) g x u v
      = pullG (I := I) (I' := I') φ (pullG (I := I') (I' := I'') ψ g) x u v := by
  simp only [pullG_apply, mfderiv_comp x hψ hφ, ContinuousLinearMap.comp_apply, Function.comp_apply]

end Pull


section DeSitter

open Real

/-- The metric `−dX₀² + dX₁² + dX₂²` of `ℝ^{1,2}`. -/
noncomputable def mink : LinearMap.BilinForm ℝ (ℝ × ℝ × ℝ) :=
  LinearMap.mk₂ ℝ (fun a b => -a.1 * b.1 + a.2.1 * b.2.1 + a.2.2 * b.2.2)
    (fun _ _ _ => by simp only [Prod.fst_add, Prod.snd_add]; ring)
    (fun _ _ _ => by simp only [Prod.smul_fst, Prod.smul_snd, smul_eq_mul]; ring)
    (fun _ _ _ => by simp only [Prod.fst_add, Prod.snd_add]; ring)
    (fun _ _ _ => by simp only [Prod.smul_fst, Prod.smul_snd, smul_eq_mul]; ring)

/-- The flat slicing `(τ, x) ↦ X` of the de Sitter hyperboloid of radius `α`. -/
noncomputable def dsFlat (α : ℝ) (p : ℝ × ℝ) : ℝ × ℝ × ℝ :=
  (α / 2 * (exp (p.1 / α) - exp (-(p.1 / α))) + p.2 * p.2 * exp (p.1 / α) * (2 * α)⁻¹,
   α / 2 * (exp (p.1 / α) + exp (-(p.1 / α))) - p.2 * p.2 * exp (p.1 / α) * (2 * α)⁻¹,
   p.2 * exp (p.1 / α))

/-- **Receipt 50's embedding lies on the hyperboloid** `−X₀² + X₁² + X₂² = α²`. -/
theorem dsFlat_on {α : ℝ} (hα : α ≠ 0) (p : ℝ × ℝ) : mink (dsFlat α p) (dsFlat α p) = α ^ 2 := by
  have h : exp (p.1 / α) * exp (-(p.1 / α)) = 1 := by rw [← exp_add]; simp
  simp only [mink, LinearMap.mk₂_apply, dsFlat]
  field_simp
  linear_combination (α ^ 2 * 2 ^ 2 * α ^ 2) * h

theorem dsFlat_pull {α : ℝ} (hα : α ≠ 0) (p u v : ℝ × ℝ) :
    pullG (I := 𝓘(ℝ, ℝ × ℝ)) (I' := 𝓘(ℝ, ℝ × ℝ × ℝ)) (dsFlat α) (fun _ => mink) p u v
      = -u.1 * v.1 + exp (2 * p.1 / α) * u.2 * v.2 := by
  have ht : HasFDerivAt (fun q : ℝ × ℝ => q.1 / α) (α⁻¹ • ContinuousLinearMap.fst ℝ ℝ ℝ) p := by
    convert (hasFDerivAt_fst (p := p) (𝕜 := ℝ)).const_smul α⁻¹ using 1
    ext q; simp [div_eq_inv_mul]
  have he := ht.exp
  have hm := (ht.neg).exp
  have hx : HasFDerivAt (fun q : ℝ × ℝ => q.2) (ContinuousLinearMap.snd ℝ ℝ ℝ) p := hasFDerivAt_snd
  have h0 := ((he.sub hm).const_mul (α / 2)).add (((hx.mul hx).mul he).mul_const (2 * α)⁻¹)
  have h1 := ((he.add hm).const_mul (α / 2)).sub (((hx.mul hx).mul he).mul_const (2 * α)⁻¹)
  have h2 := hx.mul he
  have hφ : HasFDerivAt (dsFlat α) _ p := h0.prodMk (h1.prodMk h2)
  have hD : ∀ w, mfderiv 𝓘(ℝ, ℝ × ℝ) 𝓘(ℝ, ℝ × ℝ × ℝ) (dsFlat α) p w = fderiv ℝ (dsFlat α) p w :=
    fun w => by rw [mfderiv_eq_fderiv]; rfl
  have key : pullG (I := 𝓘(ℝ, ℝ × ℝ)) (I' := 𝓘(ℝ, ℝ × ℝ × ℝ)) (dsFlat α) (fun _ => mink) p u v
      = mink (fderiv ℝ (dsFlat α) p u) (fderiv ℝ (dsFlat α) p v) :=
    congrArg₂ (fun a b => mink a b) (hD u) (hD v)
  rw [key, hφ.fderiv]
  have h : exp (p.1 / α) * exp (-(p.1 / α)) = 1 := by rw [← exp_add]; simp
  have h2 : exp (2 * p.1 / α) = exp (p.1 / α) ^ 2 := by rw [← exp_nat_mul]; ring_nf
  simp only [mink, LinearMap.mk₂_apply, ContinuousLinearMap.prod_apply, ContinuousLinearMap.add_apply,
    ContinuousLinearMap.sub_apply, ContinuousLinearMap.neg_apply, FunLike.coe_smul, Pi.smul_apply,
    ContinuousLinearMap.coe_fst', ContinuousLinearMap.coe_snd', Pi.mul_apply, Pi.neg_apply, smul_eq_mul, h2]
  field_simp
  linear_combination (-(u.1 * v.1) * (2 * α) ^ 2 * α ^ 2) * h

end DeSitter

/-! ## `r7291`, Probe S3 — the extrinsic curvature of the slices `η = const` of `covConf a` -/

section SliceK

/-- The metric of `covConf a`: `a(η)² (−dη² + dx²)`. -/
noncomputable def gConf (a : ℝ → ℝ) (p : ℝ × ℝ) :
    TangentSpace 𝓘(ℝ, ℝ × ℝ) p →L[ℝ] TangentSpace 𝓘(ℝ, ℝ × ℝ) p →L[ℝ] ℝ :=
  a p.1 ^ 2 • minkForm

/-- The unit normal `a⁻¹ ∂_η` of the slices `η = const`. -/
noncomputable def nConf (a : ℝ → ℝ) : Π p : ℝ × ℝ, TangentSpace 𝓘(ℝ, ℝ × ℝ) p :=
  fun p => (((a p.1)⁻¹ : ℝ), (0 : ℝ))

/-- `∂_x`, tangent to every slice. -/
def dx : Π p : ℝ × ℝ, TangentSpace 𝓘(ℝ, ℝ × ℝ) p := fun _ => ((0 : ℝ), (1 : ℝ))

/-- `N` is a unit timelike normal: `g(N, N) = −1`, `g(N, ∂_x) = 0`. -/
lemma nConf_unit {a : ℝ → ℝ} {p : ℝ × ℝ} (ha : a p.1 ≠ 0) :
    gConf a p (nConf a p) (nConf a p) = -1 ∧ gConf a p (nConf a p) (dx p) = 0 := by
  show a p.1 ^ 2 * minkForm ((a p.1)⁻¹, 0) ((a p.1)⁻¹, 0) = -1
    ∧ a p.1 ^ 2 * minkForm ((a p.1)⁻¹, 0) (0, 1) = 0
  rw [minkForm_apply, minkForm_apply]
  constructor
  · field_simp; ring
  · ring

set_option backward.isDefEq.respectTransparency false in
/-- **S3.** The slices `η = const` of `a(η)²(−dη² + dx²)` have extrinsic curvature `K(∂_x, ∂_x) = a′(η)`. -/
theorem sff_conf {a : ℝ → ℝ} {p : ℝ × ℝ} (ha : a p.1 ≠ 0) (hd : DifferentiableAt ℝ a p.1) :
    sff (covConf a) (gConf a) (nConf a) dx dx p = deriv a p.1 := by
  have hN := HasFDerivAt.prodMk
    (HasDerivAt.comp_hasFDerivAt (f := Prod.fst) p (HasDerivAt.inv hd.hasDerivAt ha)
      (hasFDerivAt_fst : HasFDerivAt (Prod.fst : ℝ × ℝ → ℝ) (ContinuousLinearMap.fst ℝ ℝ ℝ) p))
    (hasFDerivAt_const (0 : ℝ) p)
  have hD' : fderiv ℝ (fun q : ℝ × ℝ => ((a⁻¹ ∘ Prod.fst) q, (0 : ℝ))) p (0, 1) = 0 := by
    rw [hN.fderiv]; simp
  have hD : fderiv ℝ (nConf a : ℝ × ℝ → ℝ × ℝ) p (0, 1) = 0 := hD'
  show a p.1 ^ 2 * minkForm (covConf a (nConf a) p (0, 1)) (0, 1) = deriv a p.1
  rw [covConf_apply, hD, zero_add, Gam_apply, minkForm_apply, minkForm_apply]
  simp only [nConf, phi', Prod.smul_fst, Prod.smul_snd, Prod.fst_add, Prod.snd_add, smul_eq_mul]
  field_simp
  ring

end SliceK

/-! ## `r7293`, Probe P1 — a metric on a product, and the round sphere as a pullback -/

section Product

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
  {H : Type*} [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  {M : Type*} [TopologicalSpace M] [ChartedSpace H M]
  {E' : Type*} [NormedAddCommGroup E'] [NormedSpace ℝ E']
  {H' : Type*} [TopologicalSpace H'] {I' : ModelWithCorners ℝ E' H'}
  {M' : Type*} [TopologicalSpace M'] [ChartedSpace H' M']

/-- **G5a.** The product metric `g₁ ⊕ g₂ = pr₁*g₁ + pr₂*g₂` on `M × M'`. -/
noncomputable def prodG (g₁ : Π x : M, LinearMap.BilinForm ℝ (TangentSpace I x))
    (g₂ : Π y : M', LinearMap.BilinForm ℝ (TangentSpace I' y)) (p : M × M') :
    LinearMap.BilinForm ℝ (TangentSpace (I.prod I') p) :=
  pullG (I := I.prod I') (I' := I) Prod.fst g₁ p + pullG (I := I.prod I') (I' := I') Prod.snd g₂ p

/-- In components: `(g₁ ⊕ g₂)((u, u′), (v, v′)) = g₁(u, v) + g₂(u′, v′)`. -/
lemma prodG_apply (g₁ : Π x : M, LinearMap.BilinForm ℝ (TangentSpace I x))
    (g₂ : Π y : M', LinearMap.BilinForm ℝ (TangentSpace I' y)) (p : M × M')
    (u v : TangentSpace (I.prod I') p) :
    prodG (I := I) (I' := I') g₁ g₂ p u v = g₁ p.1 u.1 v.1 + g₂ p.2 u.2 v.2 := by
  simp only [prodG, LinearMap.add_apply, pullG_apply, mfderiv_fst, mfderiv_snd]
  rfl

lemma prodG_symm (g₁ : Π x : M, LinearMap.BilinForm ℝ (TangentSpace I x))
    (g₂ : Π y : M', LinearMap.BilinForm ℝ (TangentSpace I' y))
    (h₁ : ∀ x u v, g₁ x u v = g₁ x v u) (h₂ : ∀ y u v, g₂ y u v = g₂ y v u) (p : M × M')
    (u v : TangentSpace (I.prod I') p) :
    prodG (I := I) (I' := I') g₁ g₂ p u v = prodG (I := I) (I' := I') g₁ g₂ p v u := by
  rw [prodG_apply, prodG_apply]
  exact congrArg₂ (· + ·) (h₁ _ _ _) (h₂ _ _ _)

end Product

section Sphere

open Metric Module

local notation "ℝ³" => EuclideanSpace ℝ (Fin 3)

instance fact_finrank_three : Fact (finrank ℝ ℝ³ = 2 + 1) := ⟨by simp⟩

/-- **G5a.** The round metric of the unit `S²`: the Euclidean inner product pulled back along `S² → ℝ³`. -/
noncomputable def roundG (x : sphere (0 : ℝ³) 1) : LinearMap.BilinForm ℝ (TangentSpace (𝓡 2) x) :=
  pullG (I := 𝓡 2) (I' := 𝓘(ℝ, ℝ³)) ((↑) : sphere (0 : ℝ³) 1 → ℝ³)
    (fun _ => (innerₗ ℝ³ : LinearMap.BilinForm ℝ ℝ³)) x

/-- **It is positive definite** on every tangent space — a Riemannian metric, from the inclusion's derivative
being injective. -/
theorem roundG_pos (x : sphere (0 : ℝ³) 1) (v : TangentSpace (𝓡 2) x) (hv : v ≠ 0) : 0 < roundG x v v := by
  have hD : mfderiv (𝓡 2) 𝓘(ℝ, ℝ³) ((↑) : sphere (0 : ℝ³) 1 → ℝ³) x v ≠ 0 := fun h0 =>
    hv ((mfderiv_coe_sphere_injective x) (h0.trans (map_zero _).symm))
  show 0 < @inner ℝ ℝ³ _ (mfderiv (𝓡 2) 𝓘(ℝ, ℝ³) ((↑) : sphere (0 : ℝ³) 1 → ℝ³) x v)
    (mfderiv (𝓡 2) 𝓘(ℝ, ℝ³) ((↑) : sphere (0 : ℝ³) 1 → ℝ³) x v)
  exact real_inner_self_pos.mpr hD

lemma roundG_symm (x : sphere (0 : ℝ³) 1) (u v : TangentSpace (𝓡 2) x) : roundG x u v = roundG x v u :=
  pullG_symm (I := 𝓡 2) (I' := 𝓘(ℝ, ℝ³)) _ (fun _ => (innerₗ ℝ³ : LinearMap.BilinForm ℝ ℝ³))
    (fun _ (a b : ℝ³) => real_inner_comm b a) x u v

end Sphere

/-! ## `r7293`, Probe P2 — a periodic identification: a covering, and a free cyclic deck action -/

section Period

variable {β : ℝ} [Fact (0 < β)]

/-- **G5b.** Identifying a coordinate mod its period `β` is a covering map. -/
theorem period_isCovering : IsCoveringMap ((↑) : ℝ → AddCircle β) := AddCircle.isCoveringMap_coe β

/-- The rotation by `β/n`. -/
noncomputable def rot (β : ℝ) (n : ℕ) : AddCircle β := ((β / n : ℝ) : AddCircle β)

/-- It generates a cyclic group of order `n`. -/
theorem rot_order {n : ℕ} (hn : 0 < n) : addOrderOf (rot β n) = n :=
  AddCircle.addOrderOf_period_div hn

theorem rot_card {n : ℕ} (hn : 0 < n) : Nat.card (AddSubgroup.zmultiples (rot β n)) = n := by
  rw [Nat.card_zmultiples, rot_order hn]

omit [Fact (0 < β)] in
/-- And it acts freely: no element but `0` fixes a point. -/
theorem rot_free (n : ℕ) (k : ℤ) (x : AddCircle β) (h : k • rot β n + x = x) : k • rot β n = 0 := by
  simpa using h

end Period

/-! ## `r7293`, Probe P3 — a continuation seam that is `C¹` and not `C²`, and the Wick map between quadrics -/

section Seam

open Real
open scoped Topology

/-- The warp factor across the seam: `cos` on the Riemannian side, `cosh` on the Lorentzian side. -/
noncomputable def wseam (s : ℝ) : ℝ := if s ≤ 0 then cos s else cosh s

noncomputable def wseam' (s : ℝ) : ℝ := if s ≤ 0 then -sin s else sinh s

lemma wseam_Iic : EqOn wseam cos (Iic 0) := fun s hs => by simp [wseam, show s ≤ 0 from hs]

lemma wseam_Ici : EqOn wseam cosh (Ici 0) := fun s hs => by
  rcases eq_or_lt_of_le (show (0:ℝ) ≤ s from hs) with h | h
  · subst h; simp [wseam]
  · simp [wseam, not_le.mpr h]

lemma wseam'_Iic : EqOn wseam' (fun s => -sin s) (Iic 0) := fun s hs => by
  simp [wseam', show s ≤ 0 from hs]

lemma wseam'_Ici : EqOn wseam' sinh (Ici 0) := fun s hs => by
  rcases eq_or_lt_of_le (show (0:ℝ) ≤ s from hs) with h | h
  · subst h; simp [wseam']
  · simp [wseam', not_le.mpr h]

lemma hasDerivAt_wseam (s : ℝ) : HasDerivAt wseam (wseam' s) s := by
  rcases lt_trichotomy s 0 with h | h | h
  · have e : wseam =ᶠ[𝓝 s] cos := Filter.eventually_of_mem (Iic_mem_nhds h) fun y hy => wseam_Iic hy
    rw [show wseam' s = -sin s from wseam'_Iic h.le]
    exact (hasDerivAt_cos s).congr_of_eventuallyEq e
  · subst h
    have h1 : HasDerivWithinAt wseam (wseam' 0) (Iic 0) 0 := by
      rw [show wseam' 0 = -sin 0 from wseam'_Iic (Set.mem_Iic.mpr le_rfl)]
      exact (hasDerivAt_cos 0).hasDerivWithinAt.congr wseam_Iic (wseam_Iic (Set.mem_Iic.mpr le_rfl))
    have h2 : HasDerivWithinAt wseam (wseam' 0) (Ici 0) 0 := by
      rw [show wseam' 0 = sinh 0 by simp [wseam']]
      exact (hasDerivAt_cosh 0).hasDerivWithinAt.congr wseam_Ici (wseam_Ici (Set.mem_Ici.mpr le_rfl))
    have := h1.union h2
    rwa [Iic_union_Ici, hasDerivWithinAt_univ] at this
  · have e : wseam =ᶠ[𝓝 s] cosh := Filter.eventually_of_mem (Ici_mem_nhds h) fun y hy => wseam_Ici hy
    rw [show wseam' s = sinh s from wseam'_Ici h.le]
    exact (hasDerivAt_cosh s).congr_of_eventuallyEq e

lemma deriv_wseam : deriv wseam = wseam' := funext fun s => (hasDerivAt_wseam s).deriv

/-- **G5c, receipt 37.** The join is `C¹`. -/
theorem wseam_C1 : ContDiff ℝ 1 wseam := by
  rw [contDiff_one_iff_deriv, deriv_wseam]
  refine ⟨fun s => (hasDerivAt_wseam s).differentiableAt, ?_⟩
  exact Continuous.if_le continuous_sin.neg continuous_sinh continuous_id continuous_const
    (fun s hs => by simp [hs])

/-- **G5c, receipt 37.** The join is NOT `C²` at the seam: the second derivative jumps from `−1` to `+1`. -/
theorem wseam_not_C2 : ¬ ContDiffAt ℝ 2 wseam 0 := by
  intro h
  obtain ⟨u, hu, hC⟩ := h.contDiffOn (m := 2) le_rfl (by simp)
  obtain ⟨t, htu, hto, h0⟩ := mem_nhds_iff.mp hu
  have h2 := ((contDiffOn_succ_iff_deriv_of_isOpen (n := 1) hto).mp (hC.mono htu)).2.2
  rw [deriv_wseam] at h2
  have hd : DifferentiableAt ℝ wseam' 0 :=
    (h2.differentiableOn (by simp) 0 h0).differentiableAt (hto.mem_nhds h0)
  have hL : HasDerivWithinAt wseam' (-cos 0) (Iic 0) 0 :=
    (hasDerivAt_sin 0).neg.hasDerivWithinAt.congr wseam'_Iic (wseam'_Iic (Set.mem_Iic.mpr le_rfl))
  have hR : HasDerivWithinAt wseam' (cosh 0) (Ici 0) 0 :=
    (hasDerivAt_sinh 0).hasDerivWithinAt.congr wseam'_Ici (wseam'_Ici (Set.mem_Ici.mpr le_rfl))
  have e1 := (uniqueDiffWithinAt_Iic 0).eq_deriv _ hd.hasDerivAt.hasDerivWithinAt hL
  have e2 := (uniqueDiffWithinAt_Ici 0).eq_deriv _ hd.hasDerivAt.hasDerivWithinAt hR
  simp at e1 e2
  linarith

end Seam

section Wick

open Complex

variable {n : ℕ}

/-- The de Sitter quadric `−X₀² + Σ Xᵢ² = α²` and the sphere quadric `X₀² + Σ Xᵢ² = α²`, over `ℂ`. -/
def quadDS (α : ℂ) : Set (ℂ × (Fin n → ℂ)) := {X | -X.1 ^ 2 + ∑ i, X.2 i ^ 2 = α ^ 2}
def quadS (α : ℂ) : Set (ℂ × (Fin n → ℂ)) := {X | X.1 ^ 2 + ∑ i, X.2 i ^ 2 = α ^ 2}

/-- The Wick rotation `X₀ ↦ i X₀`, as an equivalence. -/
def wick : (ℂ × (Fin n → ℂ)) ≃ (ℂ × (Fin n → ℂ)) where
  toFun X := (Complex.I * X.1, X.2)
  invFun X := (-Complex.I * X.1, X.2)
  left_inv X := by ext <;> simp [← mul_assoc]
  right_inv X := by ext <;> simp [← mul_assoc]

/-- **G5c, receipt 106.** The Wick rotation maps the de Sitter quadric onto the sphere quadric, bijectively. -/
theorem wick_bijOn (α : ℂ) : BijOn (wick (n := n)) (quadDS α) (quadS α) := by
  have key : ∀ X : ℂ × (Fin n → ℂ), wick X ∈ quadS α ↔ X ∈ quadDS α := fun X => by
    simp only [quadS, quadDS, mem_ofPred_eq, wick, Equiv.coe_fn_mk, mul_pow, I_sq]
    constructor <;> intro h <;> linear_combination h
  refine ⟨fun X hX => (key X).2 hX, wick.injective.injOn, fun Y hY => ⟨wick.symm Y, ?_, by simp⟩⟩
  rw [← key, Equiv.apply_symm_apply]; exact hY

end Wick

/-! ## `r7295`, the PORT, L1 — the Levi-Civita connection of a NONDEGENERATE metric is unique

`mathlib`'s `IsLeviCivitaConnection.uniqueness` (`CovariantDerivative/LeviCivita.lean`) is for a `RiemannianBundle`.
Its Koszul step survives with `g` symmetric. Its injectivity step uses `inner_self_eq_zero`, i.e. positivity, and is
replaced here by nondegeneracy, tested against `mathlib`'s `FiberBundle.extend`. -/

section LCUnique

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  {H : Type*} [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  {M : Type*} [TopologicalSpace M] [ChartedSpace H M] [IsManifold I ∞ M]

/-- Compatibility with `g` at `x`, for a metric of any signature — R3's `IsCompatible`, verbatim. -/
def IsCompatAt (g : Π x : M, TangentSpace I x →L[ℝ] TangentSpace I x →L[ℝ] ℝ)
    (cov : CovariantDerivative I E (TangentSpace I : M → Type _)) (x : M) : Prop :=
  ∀ X Y Z : Π x : M, TangentSpace I x, CMDiffAt 1 (T% X) x → CMDiffAt 1 (T% Y) x →
    CMDiffAt 1 (T% Z) x →
    (show ℝ from mfderiv I 𝓘(ℝ, ℝ) (fun y => g y (Y y) (Z y)) x (X x))
      = g x (cov Y x (X x)) (Z x) + g x (Y x) (cov Z x (X x))

variable {g : Π x : M, TangentSpace I x →L[ℝ] TangentSpace I x →L[ℝ] ℝ}
  {cov cov' : CovariantDerivative I E (TangentSpace I : M → Type _)}

/-- **The Koszul formula**, for a symmetric `g` of any signature: `g(∇_X Y, Z)` without `∇`. -/
theorem koszul {x : M} (hsym : ∀ u v, g x u v = g x v u) (htor : cov.torsion = 0)
    (hc : IsCompatAt g cov x) {X Y Z : Π x : M, TangentSpace I x}
    (hX : CMDiffAt 1 (T% X) x) (hY : CMDiffAt 1 (T% Y) x) (hZ : CMDiffAt 1 (T% Z) x) :
    g x (cov Y x (X x)) (Z x) =
      ((show ℝ from mfderiv I 𝓘(ℝ, ℝ) (fun y => g y (Y y) (Z y)) x (X x))
        + (show ℝ from mfderiv I 𝓘(ℝ, ℝ) (fun y => g y (Z y) (X y)) x (Y x))
        - (show ℝ from mfderiv I 𝓘(ℝ, ℝ) (fun y => g y (X y) (Y y)) x (Z x))
        - g x (Y x) (mlieBracket I X Z x) - g x (Z x) (mlieBracket I Y X x)
        + g x (X x) (mlieBracket I Z Y x)) / 2 := by
  have e1 := hc X Y Z hX hY hZ
  have e2 := hc Y Z X hY hZ hX
  have e3 := hc Z X Y hZ hX hY
  have tor : ∀ {A B : Π x : M, TangentSpace I x}, MDiffAt (T% A) x → MDiffAt (T% B) x →
      cov B x (A x) - cov A x (B x) = mlieBracket I A B x :=
    fun hA hB => (CovariantDerivative.torsion_eq_zero_iff (cov := cov)).1 htor hA hB
  have dX := hX.mdifferentiableAt one_ne_zero
  have dY := hY.mdifferentiableAt one_ne_zero
  have dZ := hZ.mdifferentiableAt one_ne_zero
  have t1 := congrArg (g x (Y x)) (tor dX dZ)
  have t2 := congrArg (g x (Z x)) (tor dY dX)
  have t3 := congrArg (g x (X x)) (tor dZ dY)
  simp only [map_sub] at t1 t2 t3
  have s1 := hsym (cov X x (Z x)) (Y x)
  have s2 := hsym (cov Y x (X x)) (Z x)
  have s3 := hsym (cov Z x (Y x)) (X x)
  rw [e1, e2, e3]
  linarith

/-- **L1. Uniqueness.** Two torsion-free connections compatible at `x` with a symmetric NONDEGENERATE `g` agree at
`x` on every field `C¹` at `x`. -/
theorem lc_unique {x : M} (hsym : ∀ u v, g x u v = g x v u)
    (hnd : ∀ u : TangentSpace I x, (∀ v, g x u v = 0) → u = 0)
    (htor : cov.torsion = 0) (htor' : cov'.torsion = 0)
    (hc : IsCompatAt g cov x) (hc' : IsCompatAt g cov' x)
    {Y : Π x : M, TangentSpace I x} (hY : CMDiffAt 1 (T% Y) x) (X₀ : TangentSpace I x) :
    cov Y x X₀ = cov' Y x X₀ := by
  have hX : CMDiffAt 1 (T% (FiberBundle.extend E X₀ : Π y : M, TangentSpace I y)) x :=
    FiberBundle.contMDiffAt_extend (k := 1) I E X₀
  have hXx : (FiberBundle.extend E X₀ : Π y : M, TangentSpace I y) x = X₀ :=
    FiberBundle.extend_apply_self E X₀
  refine sub_eq_zero.1 (hnd _ fun w => ?_)
  have hZ : CMDiffAt 1 (T% (FiberBundle.extend E w : Π y : M, TangentSpace I y)) x :=
    FiberBundle.contMDiffAt_extend (k := 1) I E w
  have hZx : (FiberBundle.extend E w : Π y : M, TangentSpace I y) x = w :=
    FiberBundle.extend_apply_self E w
  have k1 := koszul hsym htor hc hX hY hZ
  have k2 := koszul hsym htor' hc' hX hY hZ
  rw [hXx, hZx] at k1 k2
  rw [map_sub, sub_apply, k1, k2, sub_self]

end LCUnique

/-! ### L1's first discharge: `covConf a` is THE Levi-Civita connection of `a(η)²(−dη² + dx²)`

R3's torsion-freeness and compatibility, copied from `ConformalLCProbe.lean` (the copy counts against the
discharge, not L1). -/

section LCConf

lemma gConf_apply (a : ℝ → ℝ) (p v w : ℝ × ℝ) :
    gConf a p v w = a p.1 ^ 2 * (-(v.1 * w.1) + v.2 * w.2) := by
  show a p.1 ^ 2 * minkForm v w = _
  rw [minkForm_apply]

set_option backward.isDefEq.respectTransparency false in
/-- **R3 (B8), part 2.** It is torsion-free. -/
theorem covConf_torsion (a : ℝ → ℝ) : (covConf a).torsion = 0 := by
  rw [CovariantDerivative.torsion_eq_zero_iff]
  intro X Y x hX hY
  rw [covConf_apply, covConf_apply, Gam_symm a x (X x) (Y x)]
  rw [← mlieBracketWithin_univ, mlieBracketWithin_eq_lieBracketWithin]
  set X' : ℝ × ℝ → ℝ × ℝ := X
  set Y' : ℝ × ℝ → ℝ × ℝ := Y
  show _ = fderivWithin ℝ Y' Set.univ x (X' x) - fderivWithin ℝ X' Set.univ x (Y' x)
  rw [fderivWithin_univ, fderivWithin_univ]
  abel

/-- **R3 (B8), part 3.** It is compatible with `a(η)²(−dη² + dx²)` wherever `a` is differentiable and
nonzero. -/
theorem covConf_compatible (a : ℝ → ℝ) (p : ℝ × ℝ) (hd : DifferentiableAt ℝ a p.1)
    (ha : a p.1 ≠ 0) : IsCompatAt (gConf a) (covConf a) p := by
  intro X Y Z hX hY hZ
  rw [contMDiffAt_vectorSpace_iff_contDiffAt] at hY hZ
  obtain ⟨Y', rfl⟩ : ∃ Y' : ℝ × ℝ → ℝ × ℝ, Y' = Y := ⟨Y, rfl⟩
  obtain ⟨Z', rfl⟩ : ∃ Z' : ℝ × ℝ → ℝ × ℝ, Z' = Z := ⟨Z, rfl⟩
  obtain ⟨X', rfl⟩ : ∃ X' : ℝ × ℝ → ℝ × ℝ, X' = X := ⟨X, rfl⟩
  have hYd : DifferentiableAt ℝ Y' p := hY.differentiableAt (by norm_num)
  have hZd : DifferentiableAt ℝ Z' p := hZ.differentiableAt (by norm_num)
  have hA : HasFDerivAt (fun q : ℝ × ℝ => a q.1 ^ 2)
      ((2 * a p.1 * deriv a p.1) • ContinuousLinearMap.fst ℝ ℝ ℝ) p := by
    have h1 := (hd.hasDerivAt.pow 2).comp_hasFDerivAt p (hasFDerivAt_fst (𝕜 := ℝ) (p := p))
    convert h1 using 1
    congr 1
    norm_num
    try ring
  have hY1 := (hasFDerivAt_fst (𝕜 := ℝ) (p := Y' p)).comp p hYd.hasFDerivAt
  have hY2 := (hasFDerivAt_snd (𝕜 := ℝ) (p := Y' p)).comp p hYd.hasFDerivAt
  have hZ1 := (hasFDerivAt_fst (𝕜 := ℝ) (p := Z' p)).comp p hZd.hasFDerivAt
  have hZ2 := (hasFDerivAt_snd (𝕜 := ℝ) (p := Z' p)).comp p hZd.hasFDerivAt
  have hh := hA.mul (((hY1.mul hZ1).neg).add (hY2.mul hZ2))
  have hm : (show ℝ from mfderiv 𝓘(ℝ, ℝ × ℝ) 𝓘(ℝ, ℝ) (fun y => gConf a y (Y' y) (Z' y)) p (X' p))
      = fderiv ℝ ((fun q : ℝ × ℝ => a q.1 ^ 2) *
          (-(Prod.fst ∘ Y' * Prod.fst ∘ Z') + Prod.snd ∘ Y' * Prod.snd ∘ Z')) p (X' p) := by
    rw [mfderiv_eq_fderiv]
    have hfun : (fun y : ℝ × ℝ => gConf a y (Y' y) (Z' y)) =
        ((fun q : ℝ × ℝ => a q.1 ^ 2) *
          (-(Prod.fst ∘ Y' * Prod.fst ∘ Z') + Prod.snd ∘ Y' * Prod.snd ∘ Z')) := by
      funext q
      simp [gConf_apply]
    rw [hfun]
    rfl
  rw [hm, hh.fderiv]
  show _ = gConf a p (fderiv ℝ Y' p (X' p) + Gam a p (Y' p) (X' p)) (Z' p)
    + gConf a p (Y' p) (fderiv ℝ Z' p (X' p) + Gam a p (Z' p) (X' p))
  simp only [gConf_apply, Gam_apply, minkForm_apply, phi']
  simp [Function.comp_def]
  field_simp
  ring

lemma gConf_symm (a : ℝ → ℝ) (p u v : ℝ × ℝ) : gConf a p u v = gConf a p v u := by
  rw [gConf_apply, gConf_apply]; ring

lemma gConf_nondeg {a : ℝ → ℝ} {p : ℝ × ℝ} (ha : a p.1 ≠ 0) (u : ℝ × ℝ)
    (h : ∀ v : ℝ × ℝ, gConf a p u v = 0) : u = 0 := by
  have h1 := h ((1 : ℝ), (0 : ℝ)); have h2 := h ((0 : ℝ), (1 : ℝ))
  rw [gConf_apply] at h1 h2
  have ha2 : a p.1 ^ 2 ≠ 0 := pow_ne_zero 2 ha
  have e1 : u.1 = 0 := by
    have := (mul_eq_zero.1 h1).resolve_left ha2; simpa using this
  have e2 : u.2 = 0 := by
    have := (mul_eq_zero.1 h2).resolve_left ha2; simpa using this
  exact Prod.ext e1 e2

/-- **L1, discharged on the programme's metric.** Any torsion-free connection compatible at `p` with
`a(η)²(−dη² + dx²)` IS `covConf a` there, on fields `C¹` at `p`. So every `covConf` theorem in this file —
`curv_conf`, `scal_conf`, `einstein_conf`, `hessConf_eq`, `box_conf`, `sff_conf` — is about the METRIC. -/
theorem covConf_isLeviCivita {a : ℝ → ℝ} {p : ℝ × ℝ} (hd : DifferentiableAt ℝ a p.1) (ha : a p.1 ≠ 0)
    {cov' : CovariantDerivative 𝓘(ℝ, ℝ × ℝ) (ℝ × ℝ) (TangentSpace 𝓘(ℝ, ℝ × ℝ) : ℝ × ℝ → Type _)}
    (htor' : cov'.torsion = 0) (hc' : IsCompatAt (gConf a) cov' p)
    {Y : Π q : ℝ × ℝ, TangentSpace 𝓘(ℝ, ℝ × ℝ) q}
    (hY : ContMDiffAt 𝓘(ℝ, ℝ × ℝ) 𝓘(ℝ, ℝ × ℝ).tangent 1
      (fun q => (⟨q, Y q⟩ : TangentBundle 𝓘(ℝ, ℝ × ℝ) (ℝ × ℝ))) p)
    (v : TangentSpace 𝓘(ℝ, ℝ × ℝ) p) :
    cov' Y p v = covConf a Y p v :=
  lc_unique (fun u v => gConf_symm a p u v) (fun u h => gConf_nondeg ha u h) htor' (covConf_torsion a) hc'
    (covConf_compatible a p hd ha) hY v

end LCConf

/-! ## `r7295`, the PORT, L2 — EXISTENCE of the Levi-Civita connection for a nondegenerate metric

`mathlib`'s existence section of `LeviCivita.lean`, with `inner` replaced by `g`, `InnerProductSpace.toDual` by
`BilinForm.toDual` of a nondegenerate form, and the smoothness of `⟪Y, Z⟫` (the bundle API) by the field `mdiff` of
`NDMetric`. -/

section LCExist

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  {H : Type*} [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  {M : Type*} [TopologicalSpace M] [ChartedSpace H M] [IsManifold I ∞ M]

variable (I M) in
/-- **L2.** A metric of any signature on `TM`: symmetric, nondegenerate, and differentiable along differentiable
fields. -/
structure NDMetric where
  g : Π x : M, TangentSpace I x →L[ℝ] TangentSpace I x →L[ℝ] ℝ
  symm : ∀ x u v, g x u v = g x v u
  nondeg : ∀ x (u : TangentSpace I x), (∀ v, g x u v = 0) → u = 0
  mdiff : ∀ {Y Z : Π x : M, TangentSpace I x} {x : M}, MDiffAt (T% Y) x → MDiffAt (T% Z) x →
    MDiffAt (fun y => g y (Y y) (Z y)) x

variable (m : NDMetric I M)

/-- The Koszul form: what `g(∇_X Y, Z)` must be. -/
noncomputable def kosz (X Y Z : Π x : M, TangentSpace I x) (x : M) : ℝ :=
  (d% (fun y => m.g y (Y y) (Z y)) x (X x) + d% (fun y => m.g y (Z y) (X y)) x (Y x)
    - d% (fun y => m.g y (X y) (Y y)) x (Z x)
    - m.g x (Y x) (mlieBracket I X Z x) - m.g x (Z x) (mlieBracket I Y X x)
    + m.g x (X x) (mlieBracket I Z Y x)) / 2

theorem kosz_tensorial₁ {Y Z : Π x : M, TangentSpace I x} {x : M} (hY : MDiffAt (T% Y) x)
    (hZ : MDiffAt (T% Z) x) : TensorialAt I E (kosz m · Y Z x) x where
  smul {f X} hf hX := by
    have e1 : (fun y => m.g y (Z y) ((f • X) y)) = f * fun y => m.g y (Z y) (X y) := by
      funext y; simp
    have e2 : (fun y => m.g y ((f • X) y) (Y y)) = f * fun y => m.g y (X y) (Y y) := by
      funext y; simp
    simp only [kosz, e1, e2, mvfderiv_mul hf (m.mdiff hZ hX), mvfderiv_mul hf (m.mdiff hX hY),
      mlieBracket_smul_left hf hX, mlieBracket_smul_right hf hX]
    simp
    rw [m.symm x (Y x) (X x)]; ring
  add {X X'} hX hX' := by
    have e1 : (fun y => m.g y (Z y) ((X + X') y)) =
        (fun y => m.g y (Z y) (X y)) + fun y => m.g y (Z y) (X' y) := by
      funext y; simp
    have e2 : (fun y => m.g y ((X + X') y) (Y y)) =
        (fun y => m.g y (X y) (Y y)) + fun y => m.g y (X' y) (Y y) := by
      funext y; simp
    simp only [kosz, e1, e2, mvfderiv_add (m.mdiff hZ hX) (m.mdiff hZ hX'),
      mvfderiv_add (m.mdiff hX hY) (m.mdiff hX' hY), mlieBracket_add_left hX hX',
      mlieBracket_add_right hX hX']
    simp
    ring

theorem kosz_tensorial₃ {X Y : Π x : M, TangentSpace I x} {x : M} (hX : MDiffAt (T% X) x)
    (hY : MDiffAt (T% Y) x) : TensorialAt I E (kosz m X Y ·  x) x where
  smul {f Z} hf hZ := by
    have e1 : (fun y => m.g y (Y y) ((f • Z) y)) = f * fun y => m.g y (Y y) (Z y) := by
      funext y; simp
    have e2 : (fun y => m.g y ((f • Z) y) (X y)) = f * fun y => m.g y (Z y) (X y) := by
      funext y; simp
    simp only [kosz, e1, e2, mvfderiv_mul hf (m.mdiff hY hZ), mvfderiv_mul hf (m.mdiff hZ hX),
      mlieBracket_smul_left hf hZ, mlieBracket_smul_right hf hZ]
    simp
    rw [m.symm x (X x) (Z x)]; ring
  add {Z Z'} hZ hZ' := by
    have e1 : (fun y => m.g y (Y y) ((Z + Z') y)) =
        (fun y => m.g y (Y y) (Z y)) + fun y => m.g y (Y y) (Z' y) := by
      funext y; simp
    have e2 : (fun y => m.g y ((Z + Z') y) (X y)) =
        (fun y => m.g y (Z y) (X y)) + fun y => m.g y (Z' y) (X y) := by
      funext y; simp
    simp only [kosz, e1, e2, mvfderiv_add (m.mdiff hY hZ) (m.mdiff hY hZ'),
      mvfderiv_add (m.mdiff hZ hX) (m.mdiff hZ' hX), mlieBracket_add_left hZ hZ',
      mlieBracket_add_right hZ hZ']
    simp
    ring

/-- `kosz` at `x`, as a bilinear map in the values of `X` and `Z`. -/
noncomputable def koszHom {Y : Π x : M, TangentSpace I x} {x : M} (hY : MDiffAt (T% Y) x) :
    TangentSpace I x →L[ℝ] TangentSpace I x →L[ℝ] ℝ :=
  TensorialAt.mkHom₂ (fun X Z => kosz m X Y Z x) x (fun _ hZ => kosz_tensorial₁ m hY hZ)
    (fun _ hX => kosz_tensorial₃ m hX hY)

/-- `g x` as a bilinear form. -/
noncomputable def NDMetric.bil (x : M) : LinearMap.BilinForm ℝ (TangentSpace I x) := (m.g x).toLinearMap₁₂

lemma NDMetric.bil_nondeg (x : M) : (m.bil x).Nondegenerate :=
  ⟨fun u hu => m.nondeg x u hu, fun u hu => m.nondeg x u fun v => (m.symm x u v).trans (hu v)⟩

/-- The candidate `∇Y` at `x`: the `g`-dual of the Koszul form. **The musical isomorphism of a nondegenerate form
replaces `InnerProductSpace.toDual`.** -/
noncomputable def lcAuxOf {Y : Π x : M, TangentSpace I x} {x : M} (hY : MDiffAt (T% Y) x) :
    TangentSpace I x →L[ℝ] TangentSpace I x :=
  haveI : FiniteDimensional ℝ (TangentSpace I x) := inferInstanceAs (FiniteDimensional ℝ E)
  LinearMap.toContinuousLinearMap
    (((m.bil x).toDual (m.bil_nondeg x)).symm.toLinearMap ∘ₗ (ContinuousLinearMap.coeLM ℝ) ∘ₗ
      (koszHom m hY).toLinearMap)

lemma lcAuxOf_apply {Y : Π x : M, TangentSpace I x} {x : M} (hY : MDiffAt (T% Y) x)
    (X₀ Z₀ : TangentSpace I x) : m.g x (lcAuxOf m hY X₀) Z₀ = koszHom m hY X₀ Z₀ := by
  show m.bil x _ Z₀ = _
  simp [lcAuxOf]

open scoped Classical in
noncomputable def lcAux (Y : Π x : M, TangentSpace I x) (x : M) : TangentSpace I x →L[ℝ] TangentSpace I x :=
  if hY : MDiffAt (T% Y) x then lcAuxOf m hY else 0

lemma lcAux_apply {X Y Z : Π x : M, TangentSpace I x} {x : M} (hX : MDiffAt (T% X) x)
    (hY : MDiffAt (T% Y) x) (hZ : MDiffAt (T% Z) x) :
    m.g x (lcAux m Y x (X x)) (Z x) = kosz m X Y Z x := by
  rw [lcAux, dif_pos hY, lcAuxOf_apply, koszHom, TensorialAt.mkHom₂_apply _ _ hX hZ]

/-- A vector at `x` is determined by its `g`-products with differentiable fields — nondegeneracy in place of
`inner_self_eq_zero`. -/
lemma NDMetric.g_inj {x : M} {a b : TangentSpace I x}
    (h : ∀ Z : Π x : M, TangentSpace I x, MDiffAt (T% Z) x → m.g x a (Z x) = m.g x b (Z x)) : a = b := by
  refine sub_eq_zero.1 (m.nondeg x _ fun w => ?_)
  have := h (FiberBundle.extend E w) (FiberBundle.mdifferentiableAt_extend I E w)
  rw [FiberBundle.extend_apply_self] at this
  rw [map_sub, sub_apply, this, sub_self]

lemma kosz_add_Y {X Y Y' Z : Π x : M, TangentSpace I x} {x : M} (hX : MDiffAt (T% X) x)
    (hY : MDiffAt (T% Y) x) (hY' : MDiffAt (T% Y') x) (hZ : MDiffAt (T% Z) x) :
    kosz m X (Y + Y') Z x = kosz m X Y Z x + kosz m X Y' Z x := by
  have e1 : (fun y => m.g y ((Y + Y') y) (Z y)) =
      (fun y => m.g y (Y y) (Z y)) + fun y => m.g y (Y' y) (Z y) := by funext y; simp
  have e2 : (fun y => m.g y (X y) ((Y + Y') y)) =
      (fun y => m.g y (X y) (Y y)) + fun y => m.g y (X y) (Y' y) := by funext y; simp
  simp only [kosz, e1, e2, mvfderiv_add (m.mdiff hY hZ) (m.mdiff hY' hZ),
    mvfderiv_add (m.mdiff hX hY) (m.mdiff hX hY'), mlieBracket_add_left hY hY',
    mlieBracket_add_right hY hY']
  simp
  ring

lemma kosz_smul_Y {X Y Z : Π x : M, TangentSpace I x} {f : M → ℝ} {x : M} (hX : MDiffAt (T% X) x)
    (hY : MDiffAt (T% Y) x) (hZ : MDiffAt (T% Z) x) (hf : MDiffAt f x) :
    kosz m X (f • Y) Z x = f x * kosz m X Y Z x + d% f x (X x) * m.g x (Y x) (Z x) := by
  have e1 : (fun y => m.g y ((f • Y) y) (Z y)) = f * fun y => m.g y (Y y) (Z y) := by
    funext y; simp
  have e2 : (fun y => m.g y (X y) ((f • Y) y)) = f * fun y => m.g y (X y) (Y y) := by
    funext y; simp
  simp only [kosz, e1, e2, mvfderiv_mul hf (m.mdiff hY hZ), mvfderiv_mul hf (m.mdiff hX hY),
    mlieBracket_smul_left hf hY, mlieBracket_smul_right hf hY]
  simp
  rw [m.symm x (Z x) (Y x)]; ring

lemma isCovariantDerivativeOn_lcAux : IsCovariantDerivativeOn E (lcAux m) where
  add {Y Y' x} hY hY' _ := by
    apply injective_eval_mdifferentiableAt_vectorField (I := I) (TangentSpace I x) x
    funext X hX
    dsimp only
    refine m.g_inj fun Z hZ => ?_
    rw [lcAux_apply m hX (mdifferentiableAt_add_section hY hY') hZ, add_apply,
      map_add, add_apply, lcAux_apply m hX hY hZ, lcAux_apply m hX hY' hZ,
      kosz_add_Y m hX hY hY' hZ]
  leibniz {Y f x} hY hf _ := by
    apply injective_eval_mdifferentiableAt_vectorField (I := I) (TangentSpace I x) x
    funext X hX
    dsimp only
    refine m.g_inj fun Z hZ => ?_
    rw [lcAux_apply m hX (hf.smul_section hY) hZ, kosz_smul_Y m hX hY hZ hf]
    simp [lcAux_apply m hX hY hZ]

variable (M) in
/-- **L2. The Levi-Civita connection of a nondegenerate metric of any signature.** -/
noncomputable def lcConn : CovariantDerivative I E (TangentSpace I : M → Type _) where
  toFun := lcAux m
  isCovariantDerivativeOnUniv := isCovariantDerivativeOn_lcAux m

lemma lcConn_apply {X Y Z : Π x : M, TangentSpace I x} {x : M} (hX : MDiffAt (T% X) x)
    (hY : MDiffAt (T% Y) x) (hZ : MDiffAt (T% Z) x) :
    m.g x (lcConn M m Y x (X x)) (Z x) = kosz m X Y Z x :=
  lcAux_apply m hX hY hZ

lemma NDMetric.fun_symm (A B : Π x : M, TangentSpace I x) :
    (fun y => m.g y (A y) (B y)) = fun y => m.g y (B y) (A y) := funext fun y => m.symm y _ _

/-- **L2. It is torsion-free.** -/
theorem lcConn_torsion : (lcConn M m).torsion = 0 := by
  rw [CovariantDerivative.torsion_eq_zero_iff]
  intro X Y x hX hY
  refine m.g_inj fun Z hZ => ?_
  rw [map_sub, sub_apply, lcConn_apply m hX hY hZ, lcConn_apply m hY hX hZ]
  simp only [kosz, m.fun_symm X Z, m.fun_symm Z Y, m.fun_symm Y X,
    congrFun (mlieBracket_swap (V := Y) (W := X)) x, congrFun (mlieBracket_swap (V := Z) (W := Y)) x,
    congrFun (mlieBracket_swap (V := Z) (W := X)) x, Pi.neg_apply, map_neg]
  rw [m.symm x (Z x) (mlieBracket I X Y x)]
  ring

/-- **L2. It is compatible with `g`**, in L1's form (`IsCompatAt`). -/
theorem lcConn_compat (x : M) : IsCompatAt m.g (lcConn M m) x := by
  intro X Y Z hX hY hZ
  have dX := hX.mdifferentiableAt one_ne_zero
  have dY := hY.mdifferentiableAt one_ne_zero
  have dZ := hZ.mdifferentiableAt one_ne_zero
  rw [lcConn_apply m dX dY dZ, m.symm x (Y x) (lcConn M m Z x (X x)), lcConn_apply m dX dZ dY]
  simp only [kosz, m.fun_symm Y X, m.fun_symm Z Y, m.fun_symm X Z,
    congrFun (mlieBracket_swap (V := Z) (W := X)) x, congrFun (mlieBracket_swap (V := Y) (W := X)) x,
    congrFun (mlieBracket_swap (V := Z) (W := Y)) x, Pi.neg_apply, map_neg]
  show d% (fun y => m.g y (Y y) (Z y)) x (X x) = _
  ring

/-- **The PORT, L1 + L2: the Levi-Civita theorem for a metric of any signature.** `lcConn M m` is torsion-free and
compatible with `m.g`, and any connection that is, agrees with it at `x` on fields `C¹` at `x`. -/
theorem lcConn_unique {cov' : CovariantDerivative I E (TangentSpace I : M → Type _)}
    (htor' : cov'.torsion = 0) {x : M} (hc' : IsCompatAt m.g cov' x)
    {Y : Π x : M, TangentSpace I x} (hY : CMDiffAt 1 (T% Y) x) (X₀ : TangentSpace I x) :
    cov' Y x X₀ = lcConn M m Y x X₀ :=
  lc_unique (m.symm x) (m.nondeg x) htor' (lcConn_torsion m) hc' (lcConn_compat m x) hY X₀

end LCExist

/-! ## `r7297`, C1 — receipt 43: on a flat metric of any signature, the flat connection IS the Levi-Civita
connection, so the homothety `ξ(x) = x` has `∇ξ = id` for THE connection, and its charge is conserved exactly
along null geodesics -/

section FlatLC

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]

/-- The flat connection `σ ↦ Dσ`, from K2's `flat_isCov`. -/
noncomputable def flatCov : CovariantDerivative 𝓘(ℝ, E) E (TangentSpace 𝓘(ℝ, E) : E → Type _) where
  toFun σ x := show TangentSpace 𝓘(ℝ, E) x →L[ℝ] TangentSpace 𝓘(ℝ, E) x from (fderiv ℝ (vf σ) x : E →L[ℝ] E)
  isCovariantDerivativeOnUniv := flat_isCov

set_option backward.isDefEq.respectTransparency false in
theorem flatCov_torsion : (flatCov (E := E)).torsion = 0 := by
  rw [CovariantDerivative.torsion_eq_zero_iff]
  intro X Y x hX hY
  rw [← mlieBracketWithin_univ, mlieBracketWithin_eq_lieBracketWithin]
  show fderiv ℝ (vf Y) x (X x) - fderiv ℝ (vf X) x (Y x) = _
  rw [lieBracketWithin_univ]
  rfl

set_option backward.isDefEq.respectTransparency false in
/-- A constant form `η` is compatible with the flat connection. -/
theorem flatCov_compat (η : E →L[ℝ] E →L[ℝ] ℝ) (x : E) :
    IsCompatAt (fun _ => η) (flatCov (E := E)) x := by
  intro X Y Z hX hY hZ
  have dY : DifferentiableAt ℝ (vf Y) x :=
    mdiffAt_model.1 (hY.mdifferentiableAt one_ne_zero)
  have dZ : DifferentiableAt ℝ (vf Z) x :=
    mdiffAt_model.1 (hZ.mdifferentiableAt one_ne_zero)
  have hd : HasFDerivAt (fun y => η (vf Y y) (vf Z y)) _ x :=
    (η.hasFDerivAt.comp x dY.hasFDerivAt).clm_apply dZ.hasFDerivAt
  have : (show ℝ from mfderiv 𝓘(ℝ, E) 𝓘(ℝ, ℝ) (fun y => η (Y y) (Z y)) x (X x))
      = fderiv ℝ (fun y => η (vf Y y) (vf Z y)) x (X x) := by
    rw [mfderiv_eq_fderiv]; rfl
  exact this.trans (by rw [hd.fderiv, add_apply, add_comm]; rfl)

/-- **C1, the connection half.** For a symmetric nondegenerate constant `η` of ANY signature, every torsion-free
connection compatible with `η` at `x` IS the flat one there (L1). -/
theorem flat_isLeviCivita {η : E →L[ℝ] E →L[ℝ] ℝ} (hsym : ∀ u v, η u v = η v u)
    (hnd : ∀ u, (∀ v, η u v = 0) → u = 0)
    {cov' : CovariantDerivative 𝓘(ℝ, E) E (TangentSpace 𝓘(ℝ, E) : E → Type _)}
    (htor' : cov'.torsion = 0) {x : E} (hc' : IsCompatAt (fun _ => η) cov' x)
    {Y : Π y : E, TangentSpace 𝓘(ℝ, E) y} (hY : CMDiffAt 1 (T% Y) x) (w : TangentSpace 𝓘(ℝ, E) x) :
    cov' Y x w = fderiv ℝ (vf Y) x w :=
  lc_unique (g := fun _ => η) hsym hnd htor' flatCov_torsion hc' (flatCov_compat η x) hY w

/-- The homothety field `ξ(x) = x`. -/
def homo : Π y : E, TangentSpace 𝓘(ℝ, E) y := fun y => y

set_option backward.isDefEq.respectTransparency false in
/-- **C1, receipt 43.** For THE Levi-Civita connection of a flat metric of any signature, `∇ξ = id`: the dilation
is a homothety, `L_ξ η = 2η`. -/
theorem homothety_nabla {η : E →L[ℝ] E →L[ℝ] ℝ} (hsym : ∀ u v, η u v = η v u)
    (hnd : ∀ u, (∀ v, η u v = 0) → u = 0)
    {cov' : CovariantDerivative 𝓘(ℝ, E) E (TangentSpace 𝓘(ℝ, E) : E → Type _)}
    (htor' : cov'.torsion = 0) {x : E} (hc' : IsCompatAt (fun _ => η) cov' x)
    (w : TangentSpace 𝓘(ℝ, E) x) : cov' homo x w = w := by
  have hξ : CMDiffAt 1 (T% (homo (E := E))) x := by
    rw [contMDiffAt_section]; simp only [trivializationAt_model_space_apply]
    exact contMDiffAt_id
  rw [flat_isLeviCivita hsym hnd htor' hc' hξ w]
  show fderiv ℝ (fun y : E => y) x w = w
  rw [fderiv_fun_id]; rfl

/-- **C1, receipt 43.** Along a geodesic of the flat metric, `t ↦ p + t v`, the homothety charge `Q = η(ξ, γ̇)` has
`Q′ = η(v, v)`: it is conserved exactly when the geodesic is null. -/
theorem homothety_charge (η : E →L[ℝ] E →L[ℝ] ℝ) (p v : E) (t : ℝ) :
    HasDerivAt (fun s : ℝ => η (p + s • v) v) (η v v) t := by
  have e : (fun s : ℝ => η (p + s • v) v) = fun s => η p v + s * η v v := by
    funext s; simp [map_add, map_smul]
  rw [e]
  simpa using ((hasDerivAt_id t).mul_const (η v v)).const_add (η p v)

end FlatLC

/-! ## `r7297`, C2 — receipt 92: in a Painlevé–Gullstrand chart `g = −dτ² + (A(s) ds − w(s) dτ)²` with `A ≠ 0`,
nondegenerate everywhere, the rain field `V = ∂_τ + (w/A) ∂_s` is a GEODESIC field of THE Levi-Civita connection.
`A = 1`, `s = r` is the usual chart; `A = eˢ`, `r = eˢ` makes Schwarzschild–de Sitter's profile smooth on all of `ℝ`. -/

section RainPG

/-- `L_p = A ds − w dτ`. -/
noncomputable def pgL (A w : ℝ → ℝ) (p : ℝ × ℝ) : ℝ × ℝ →L[ℝ] ℝ :=
  A p.2 • ContinuousLinearMap.snd ℝ ℝ ℝ - w p.2 • ContinuousLinearMap.fst ℝ ℝ ℝ

/-- The 2D Painlevé–Gullstrand form `−dτ² + L²`. -/
noncomputable def pgForm (A w : ℝ → ℝ) (p : ℝ × ℝ) : ℝ × ℝ →L[ℝ] ℝ × ℝ →L[ℝ] ℝ :=
  -((ContinuousLinearMap.mul ℝ ℝ).bilinearComp (ContinuousLinearMap.fst ℝ ℝ ℝ)
      (ContinuousLinearMap.fst ℝ ℝ ℝ))
    + (ContinuousLinearMap.mul ℝ ℝ).bilinearComp (pgL A w p) (pgL A w p)

lemma pgForm_apply (A w : ℝ → ℝ) (p a b : ℝ × ℝ) :
    pgForm A w p a b = -(a.1 * b.1) + (A p.2 * a.2 - w p.2 * a.1) * (A p.2 * b.2 - w p.2 * b.1) := by
  simp [pgForm, pgL]; ring

lemma pgForm_symm (A w : ℝ → ℝ) (p a b : ℝ × ℝ) : pgForm A w p a b = pgForm A w p b a := by
  rw [pgForm_apply, pgForm_apply]; ring

lemma pgForm_nondeg {A : ℝ → ℝ} (w : ℝ → ℝ) {p : ℝ × ℝ} (hA : A p.2 ≠ 0) (u : ℝ × ℝ)
    (h : ∀ b : ℝ × ℝ, pgForm A w p u b = 0) : u = 0 := by
  have h1 := h ((1 : ℝ), (0 : ℝ)); have h2 := h ((0 : ℝ), (1 : ℝ))
  rw [pgForm_apply] at h1 h2
  simp only [mul_one, mul_zero, sub_zero, zero_sub, neg_zero, zero_add] at h1 h2
  have e0 : A p.2 * u.2 - w p.2 * u.1 = 0 := (mul_eq_zero.1 h2).resolve_right hA
  have e1 : u.1 = 0 := by linear_combination -h1 - w p.2 * e0
  have e2 : u.2 = 0 := by
    rw [e1, mul_zero, sub_zero] at e0; exact (mul_eq_zero.1 e0).resolve_left hA
  exact Prod.ext e1 e2

/-- The PG metric as an `NDMetric` on `ℝ²`. -/
noncomputable def pgMetric (A w : ℝ → ℝ) (hA : ∀ s, A s ≠ 0) (hAd : Differentiable ℝ A)
    (hw : Differentiable ℝ w) : NDMetric 𝓘(ℝ, ℝ × ℝ) (ℝ × ℝ) where
  g p := pgForm A w p
  symm p a b := pgForm_symm A w p a b
  nondeg p u h := pgForm_nondeg w (hA p.2) u h
  mdiff {Y Z x} hY hZ := by
    rw [mdiffAt_model] at hY hZ
    rw [mdifferentiableAt_iff_differentiableAt]
    have e : (fun y => pgForm A w y (Y y) (Z y)) = fun y =>
        -((vf Y y).1 * (vf Z y).1) + (A y.2 * (vf Y y).2 - w y.2 * (vf Y y).1)
          * (A y.2 * (vf Z y).2 - w y.2 * (vf Z y).1) := by
      funext y; exact pgForm_apply A w y (Y y) (Z y)
    show DifferentiableAt ℝ (fun y => pgForm A w y (Y y) (Z y)) x
    rw [e]
    have hw' : DifferentiableAt ℝ (fun y : ℝ × ℝ => w y.2) x := (hw _).comp x differentiableAt_snd
    have hA' : DifferentiableAt ℝ (fun y : ℝ × ℝ => A y.2) x := (hAd _).comp x differentiableAt_snd
    fun_prop

/-- The rain field `V = ∂_τ + (w/A) ∂_s`. -/
noncomputable def rain (A w : ℝ → ℝ) : Π p : ℝ × ℝ, TangentSpace 𝓘(ℝ, ℝ × ℝ) p :=
  fun p => ((1 : ℝ), w p.2 / A p.2)

lemma pg_rain_left {A : ℝ → ℝ} (w : ℝ → ℝ) {p : ℝ × ℝ} (hA : A p.2 ≠ 0) (b : ℝ × ℝ) :
    pgForm A w p ((1 : ℝ), w p.2 / A p.2) b = -b.1 := by
  rw [pgForm_apply]; field_simp; ring

set_option backward.isDefEq.respectTransparency false in
/-- **C2, receipt 92.** The rain field is a GEODESIC field of THE Levi-Civita connection of the PG metric:
`∇_V V = 0`. The E = 1 radial geodesics are its flow lines. -/
theorem rain_geodesic (A w : ℝ → ℝ) (hA : ∀ s, A s ≠ 0) (hAd : Differentiable ℝ A)
    (hw : Differentiable ℝ w) (p : ℝ × ℝ) :
    lcConn (ℝ × ℝ) (pgMetric A w hA hAd hw) (rain A w) p (rain A w p) = 0 := by
  set m := pgMetric A w hA hAd hw
  have hw' : DifferentiableAt ℝ (fun y : ℝ × ℝ => w y.2) p := (hw _).comp p differentiableAt_snd
  have hA' : DifferentiableAt ℝ (fun y : ℝ × ℝ => A y.2) p := (hAd _).comp p differentiableAt_snd
  have dq : DifferentiableAt ℝ (fun y : ℝ × ℝ => w y.2 / A y.2) p := by
    have := hA p.2; fun_prop (disch := assumption)
  have hVf : HasFDerivAt (fun y : ℝ × ℝ => ((1 : ℝ), w y.2 / A y.2))
      ((0 : ℝ × ℝ →L[ℝ] ℝ).prod (fderiv ℝ (fun y : ℝ × ℝ => w y.2 / A y.2) p)) p :=
    (hasFDerivAt_const (1 : ℝ) p).prodMk dq.hasFDerivAt
  have dV : DifferentiableAt ℝ (vf (rain A w)) p := hVf.differentiableAt
  have hV : MDifferentiableAt 𝓘(ℝ, ℝ × ℝ) 𝓘(ℝ, ℝ × ℝ).tangent
      (fun q => (⟨q, rain A w q⟩ : TangentBundle 𝓘(ℝ, ℝ × ℝ) (ℝ × ℝ))) p := mdiffAt_model.2 dV
  refine m.g_inj fun Z hZ => ?_
  have dZ := mdiffAt_model.1 hZ
  rw [lcConn_apply m hV hV hZ, map_zero, zero_apply]
  have f1 : (fun y => m.g y (rain A w y) (Z y)) = fun y => -(vf Z y).1 := by
    funext y; exact pg_rain_left w (hA y.2) (Z y)
  have f2 : (fun y => m.g y (Z y) (rain A w y)) = fun y => -(vf Z y).1 := by
    funext y; exact (pgForm_symm A w y (Z y) (rain A w y)).trans (pg_rain_left w (hA y.2) (Z y))
  have f3 : (fun y => m.g y (rain A w y) (rain A w y)) = fun _ => (-1 : ℝ) := by
    funext y; exact (pg_rain_left w (hA y.2) (rain A w y)).trans rfl
  have dfst : HasFDerivAt (fun y => -(vf Z y).1)
      (-((ContinuousLinearMap.fst ℝ ℝ ℝ).comp (fderiv ℝ (vf Z) p))) p :=
    (hasFDerivAt_fst.comp p dZ.hasFDerivAt).neg
  have hbr : ∀ A B : Π y : ℝ × ℝ, TangentSpace 𝓘(ℝ, ℝ × ℝ) y,
      mlieBracket 𝓘(ℝ, ℝ × ℝ) A B p = fderiv ℝ (vf B) p (A p) - fderiv ℝ (vf A) p (B p) :=
    fun A B => by
      rw [← mlieBracketWithin_univ, mlieBracketWithin_eq_lieBracketWithin, lieBracketWithin_univ]; rfl
  have hV1 : ∀ u, (fderiv ℝ (vf (rain A w)) p u).1 = 0 := fun u => by
    show (fderiv ℝ (fun y : ℝ × ℝ => ((1 : ℝ), w y.2 / A y.2)) p u).1 = 0
    rw [hVf.fderiv]; simp
  simp only [kosz, f1, f2, f3, mvfderiv_const, zero_apply, hbr, sub_self, map_zero]
  rw [mvfderiv_eq_fderiv, dfst.fderiv]
  set a : ℝ × ℝ := fderiv ℝ (vf Z) p (show ℝ × ℝ from rain A w p) with ha
  set b : ℝ × ℝ := fderiv ℝ (vf (rain A w)) p (show ℝ × ℝ from Z p) with hb
  have h1 : b.1 = 0 := hV1 (Z p)
  have k1 : m.g p (rain A w p) (a - b) = -(a.1 - b.1) := by
    rw [show m.g p (rain A w p) (a - b) = -(a - b).1 from pg_rain_left w (hA p.2) (a - b)]; simp
  have k2 : m.g p (rain A w p) (b - a) = -(b.1 - a.1) := by
    rw [show m.g p (rain A w p) (b - a) = -(b - a).1 from pg_rain_left w (hA p.2) (b - a)]; simp
  have k3 : (fderiv ℝ (vf Z) p (NormedSpace.fromTangentSpace p (rain A w p))).1 = a.1 := rfl
  simp only [neg_apply, ContinuousLinearMap.comp_apply, ContinuousLinearMap.coe_fst']
  linear_combination (norm := skip) -k3 - k1 / 2 + k2 / 2 - h1
  ring_nf
  first | rfl | simp | (congr 1)

/-- Schwarzschild–de Sitter's E = 1 profile in the chart `r = eˢ`: `w(s) = v(eˢ) = √(2M e⁻ˢ + e²ˢ/α²)`. -/
noncomputable def wSdS (M α : ℝ) (s : ℝ) : ℝ := Real.sqrt (2 * M * Real.exp (-s) + Real.exp (2 * s) / α ^ 2)

lemma wSdS_diff {M : ℝ} (hM : 0 < M) (α : ℝ) : Differentiable ℝ (wSdS M α) := fun s => by
  have hpos : 0 < 2 * M * Real.exp (-s) + Real.exp (2 * s) / α ^ 2 := by positivity
  have h0 := hpos.ne'
  unfold wSdS
  fun_prop (disch := assumption)

/-- **C2, receipt 92, on the named metric.** The rain field of Schwarzschild–de Sitter in the chart `r = eˢ`, where
the metric is smooth and nondegenerate on all of `ℝ²`, is a geodesic field of THE Levi-Civita connection. -/
theorem sds_rain_geodesic {M : ℝ} (hM : 0 < M) (α : ℝ) (p : ℝ × ℝ) :
    lcConn (ℝ × ℝ) (pgMetric Real.exp (wSdS M α) Real.exp_ne_zero Real.differentiable_exp (wSdS_diff hM α))
      (rain Real.exp (wSdS M α)) p (rain Real.exp (wSdS M α) p) = 0 :=
  rain_geodesic _ _ _ _ _ p

/-- **C2, receipt 92: the `sinh^{2/3}` law.** `r(τ) = (2Mα² sinh²(3τ/2α))^{1/3}` solves `ṙ = √(2M/r + r²/α²)`
for `τ > 0`: it is a flow line of the rain field, an E = 1 radial geodesic. -/
theorem sinh23_flow {M α τ : ℝ} (hM : 0 < M) (hα : 0 < α) (hτ : 0 < τ) :
    HasDerivAt (fun t => (2 * M * α ^ 2 * Real.sinh (3 / (2 * α) * t) ^ 2) ^ (1 / 3 : ℝ))
      (Real.sqrt (2 * M / (2 * M * α ^ 2 * Real.sinh (3 / (2 * α) * τ) ^ 2) ^ (1 / 3 : ℝ)
        + ((2 * M * α ^ 2 * Real.sinh (3 / (2 * α) * τ) ^ 2) ^ (1 / 3 : ℝ)) ^ 2 / α ^ 2)) τ := by
  set k := 3 / (2 * α) with hk
  set S := Real.sinh (k * τ)
  set C := Real.cosh (k * τ)
  have hS : 0 < S := Real.sinh_pos_iff.2 (by positivity)
  have hC : 0 < C := Real.cosh_pos _
  set F := 2 * M * α ^ 2 * S ^ 2
  have hF : 0 < F := by positivity
  set r := F ^ (1 / 3 : ℝ)
  have hr : 0 < r := Real.rpow_pos_of_pos hF _
  have hr3 : r ^ 3 = F := by
    rw [← Real.rpow_natCast, ← Real.rpow_mul hF.le]; norm_num
  have hFd : HasDerivAt (fun t => 2 * M * α ^ 2 * Real.sinh (k * t) ^ 2)
      (2 * M * α ^ 2 * (2 * S * (C * k))) τ := by
    have := (((Real.hasDerivAt_sinh (k * τ)).comp τ ((hasDerivAt_id τ).const_mul k)).pow 2).const_mul
      (2 * M * α ^ 2)
    convert this using 1
    · funext y; simp [Function.comp_apply]
    · rw [show (Real.sinh ∘ HMul.hMul k) τ = S from rfl]; push_cast; ring
  have hrd := HasDerivAt.rpow_const (p := 1 / 3) hFd (Or.inl hF.ne')
  convert hrd using 1
  have hFr : F ^ ((1 : ℝ) / 3 - 1) = r / F := by
    rw [Real.rpow_sub hF, Real.rpow_one]
  rw [hFr]
  have hcs : C ^ 2 = 1 + S ^ 2 := by rw [Real.cosh_sq]; ring
  rw [Real.sqrt_eq_iff_mul_self_eq_of_pos (by positivity)]
  field_simp
  rw [hk]; field_simp
  have hF' : F = 2 * M * α ^ 2 * S ^ 2 := rfl
  linear_combination (4 * M ^ 2 * α ^ 4 * S ^ 2 * C ^ 2 - F ^ 2) * hr3 + 4 * M ^ 2 * α ^ 4 * S ^ 2 * F * hcs
    - (2 * M * α ^ 2 * F + F * (F + 2 * M * α ^ 2 * S ^ 2)) * hF'

end RainPG

/-! ## `r7297`, C3 — receipt 41: in the PG chart with `A = 1`, `ξ = ∂_τ` satisfies `∇_ξ ξ = κ ξ` on the horizon
`w = −1`, with `κ = w′ = f′/2`, `f = 1 − w²` — the surface gravity, for THE Levi-Civita connection -/

section SurfGrav

lemma fts_apply (p : ℝ × ℝ) (v : TangentSpace 𝓘(ℝ, ℝ × ℝ) p) :
    ((NormedSpace.fromTangentSpace (𝕜 := ℝ) p : TangentSpace 𝓘(ℝ, ℝ × ℝ) p →L[ℝ] ℝ × ℝ) v) = v := rfl

/-- `ξ = ∂_τ`. -/
def xiT : Π p : ℝ × ℝ, TangentSpace 𝓘(ℝ, ℝ × ℝ) p := fun _ => ((1 : ℝ), (0 : ℝ))

set_option backward.isDefEq.respectTransparency false in
/-- **C3, receipt 41.** On the horizon `w(r) = −1`, `∇_ξ ξ = w′(r) ξ`: the surface gravity is `κ = w′ = f′/2`. -/
theorem surface_gravity (w : ℝ → ℝ) (hw : Differentiable ℝ w) (p : ℝ × ℝ) (hh : w p.2 = -1) :
    lcConn (ℝ × ℝ) (pgMetric (fun _ => 1) w (fun _ => one_ne_zero) (differentiable_const _) hw) xiT p (xiT p)
      = deriv w p.2 • xiT p := by
  set m := pgMetric (fun _ => 1) w (fun _ => one_ne_zero) (differentiable_const _) hw
  have hξd : HasFDerivAt (vf xiT) (0 : ℝ × ℝ →L[ℝ] ℝ × ℝ) p := hasFDerivAt_const _ _
  have hξ : MDifferentiableAt 𝓘(ℝ, ℝ × ℝ) 𝓘(ℝ, ℝ × ℝ).tangent
      (fun q => (⟨q, xiT q⟩ : TangentBundle 𝓘(ℝ, ℝ × ℝ) (ℝ × ℝ))) p :=
    mdiffAt_model.2 hξd.differentiableAt
  refine m.g_inj fun Z hZ => ?_
  have dZ := mdiffAt_model.1 hZ
  rw [lcConn_apply m hξ hξ hZ]
  -- the pieces of the Koszul form
  have hW : HasFDerivAt (fun y : ℝ × ℝ => w y.2) (deriv w p.2 • ContinuousLinearMap.snd ℝ ℝ ℝ) p := by
    exact (hw p.2).hasDerivAt.comp_hasFDerivAt p (hasFDerivAt_snd (p := p) (𝕜 := ℝ))
  have hZ1 : HasFDerivAt (fun y => (vf Z y).1) ((ContinuousLinearMap.fst ℝ ℝ ℝ).comp (fderiv ℝ (vf Z) p)) p :=
    hasFDerivAt_fst.comp p dZ.hasFDerivAt
  have hZ2 : HasFDerivAt (fun y => (vf Z y).2) ((ContinuousLinearMap.snd ℝ ℝ ℝ).comp (fderiv ℝ (vf Z) p)) p :=
    hasFDerivAt_snd.comp p dZ.hasFDerivAt
  have gl : ∀ y (b : ℝ × ℝ), m.g y (xiT y) b = -b.1 - w y.2 * (b.2 - w y.2 * b.1) := fun y b => by
    show pgForm (fun _ => 1) w y ((1 : ℝ), (0 : ℝ)) b = _
    rw [pgForm_apply]; ring
  have f1 : (fun y => m.g y (xiT y) (Z y)) =
      fun y => -(vf Z y).1 - w y.2 * ((vf Z y).2 - w y.2 * (vf Z y).1) := funext fun y => gl y (Z y)
  have f2 : (fun y => m.g y (Z y) (xiT y)) =
      fun y => -(vf Z y).1 - w y.2 * ((vf Z y).2 - w y.2 * (vf Z y).1) :=
    funext fun y => (pgForm_symm _ w y (Z y) (xiT y)).trans (gl y (Z y))
  have f3 : (fun y => m.g y (xiT y) (xiT y)) = fun y => -1 + w y.2 * w y.2 := funext fun y => by
    rw [gl]; show -(1 : ℝ) - w y.2 * (0 - w y.2 * 1) = _; ring
  have hT1 : HasFDerivAt (fun y => -(vf Z y).1 - w y.2 * ((vf Z y).2 - w y.2 * (vf Z y).1)) _ p :=
    (hZ1.neg).sub (hW.mul (hZ2.sub (hW.mul hZ1)))
  have hT3 : HasFDerivAt (fun y : ℝ × ℝ => -1 + w y.2 * w y.2) _ p :=
    (hasFDerivAt_const (-1 : ℝ) p).add (hW.mul hW)
  have hbr : ∀ A B : Π y : ℝ × ℝ, TangentSpace 𝓘(ℝ, ℝ × ℝ) y,
      mlieBracket 𝓘(ℝ, ℝ × ℝ) A B p = fderiv ℝ (vf B) p (A p) - fderiv ℝ (vf A) p (B p) :=
    fun A B => by
      rw [← mlieBracketWithin_univ, mlieBracketWithin_eq_lieBracketWithin, lieBracketWithin_univ]; rfl
  simp only [kosz, f1, f2, f3, hbr, hξd.fderiv, zero_apply, sub_zero, sub_self, map_zero]
  rw [mvfderiv_eq_fderiv, mvfderiv_eq_fderiv, hT1.fderiv, hT3.fderiv]
  simp only [ContinuousLinearMap.comp_apply, sub_apply, neg_apply, add_apply, smul_apply,
    ContinuousLinearMap.coe_fst', ContinuousLinearMap.coe_snd', smul_eq_mul, fts_apply, zero_apply]
  have hx2 : (xiT p : ℝ × ℝ).2 = 0 := rfl
  rw [map_smul, smul_apply, smul_eq_mul]
  simp only [gl, hx2, Prod.fst_sub, Prod.snd_sub, Prod.fst_zero, Prod.snd_zero, mul_zero, zero_add, add_zero]
  rw [hh]; ring

/-- **C3.** And `w′ = f′/2` there, with `f = 1 − w²`: the surface gravity is half the slope of the metric function. -/
lemma kappa_half_fprime (w : ℝ → ℝ) (r : ℝ) (hw : DifferentiableAt ℝ w r) (hh : w r = -1) :
    deriv (fun s => 1 - w s ^ 2) r / 2 = deriv w r := by
  have h : HasDerivAt (fun s => 1 - w s ^ 2) (-(2 * w r * deriv w r)) r := by
    convert (hw.hasDerivAt.pow 2).const_sub 1 using 1; simp
  rw [h.deriv, hh]; ring

end SurfGrav

/-! ## `r7297`, C4 — receipt 29: for a static 2D metric `g = −c(u)² du² + b(u) dt²` (`c, b ≠ 0`), the unit field
`U = c⁻¹ ∂_u` is a GEODESIC field of THE Levi-Civita connection. The Schwarzschild interior in the chart
`η = 2 arctan eᵘ` is `c = 4M eᵘ/(1+e²ᵘ)²`, `b = e²ᵘ`, and the cycloid `τ = M(η + sin η)` is its proper time. -/

section StaticDiag

noncomputable def dgForm (c b : ℝ → ℝ) (p : ℝ × ℝ) : ℝ × ℝ →L[ℝ] ℝ × ℝ →L[ℝ] ℝ :=
  -(c p.1 ^ 2 • (ContinuousLinearMap.mul ℝ ℝ).bilinearComp (ContinuousLinearMap.fst ℝ ℝ ℝ)
      (ContinuousLinearMap.fst ℝ ℝ ℝ))
    + b p.1 • (ContinuousLinearMap.mul ℝ ℝ).bilinearComp (ContinuousLinearMap.snd ℝ ℝ ℝ)
      (ContinuousLinearMap.snd ℝ ℝ ℝ)

lemma dgForm_apply (c b : ℝ → ℝ) (p x y : ℝ × ℝ) :
    dgForm c b p x y = -(c p.1 ^ 2 * (x.1 * y.1)) + b p.1 * (x.2 * y.2) := by
  simp [dgForm]

lemma dgForm_symm (c b : ℝ → ℝ) (p x y : ℝ × ℝ) : dgForm c b p x y = dgForm c b p y x := by
  rw [dgForm_apply, dgForm_apply]; ring

lemma dgForm_nondeg {c b : ℝ → ℝ} {p : ℝ × ℝ} (hc : c p.1 ≠ 0) (hb : b p.1 ≠ 0) (x : ℝ × ℝ)
    (h : ∀ y : ℝ × ℝ, dgForm c b p x y = 0) : x = 0 := by
  have h1 := h ((1 : ℝ), (0 : ℝ)); have h2 := h ((0 : ℝ), (1 : ℝ))
  rw [dgForm_apply] at h1 h2
  simp only [mul_one, mul_zero, add_zero, zero_add, neg_zero, neg_eq_zero] at h1 h2
  exact Prod.ext ((mul_eq_zero.1 h1).resolve_left (pow_ne_zero 2 hc))
    ((mul_eq_zero.1 h2).resolve_left hb)

noncomputable def dgMetric (c b : ℝ → ℝ) (hc : ∀ u, c u ≠ 0) (hb : ∀ u, b u ≠ 0)
    (hcd : Differentiable ℝ c) (hbd : Differentiable ℝ b) : NDMetric 𝓘(ℝ, ℝ × ℝ) (ℝ × ℝ) where
  g p := dgForm c b p
  symm p x y := dgForm_symm c b p x y
  nondeg p x h := dgForm_nondeg (hc p.1) (hb p.1) x h
  mdiff {Y Z x} hY hZ := by
    rw [mdiffAt_model] at hY hZ
    rw [mdifferentiableAt_iff_differentiableAt]
    have e : (fun y => dgForm c b y (Y y) (Z y)) = fun y =>
        -(c y.1 ^ 2 * ((vf Y y).1 * (vf Z y).1)) + b y.1 * ((vf Y y).2 * (vf Z y).2) := by
      funext y; exact dgForm_apply c b y (Y y) (Z y)
    show DifferentiableAt ℝ (fun y => dgForm c b y (Y y) (Z y)) x
    rw [e]
    have hc' : DifferentiableAt ℝ (fun y : ℝ × ℝ => c y.1) x := (hcd _).comp x differentiableAt_fst
    have hb' : DifferentiableAt ℝ (fun y : ℝ × ℝ => b y.1) x := (hbd _).comp x differentiableAt_fst
    fun_prop

/-- The unit field `U = c⁻¹ ∂_u`. -/
noncomputable def unitU (c : ℝ → ℝ) : Π p : ℝ × ℝ, TangentSpace 𝓘(ℝ, ℝ × ℝ) p :=
  fun p => ((c p.1)⁻¹, (0 : ℝ))

lemma dg_U_left {c : ℝ → ℝ} (b : ℝ → ℝ) {p : ℝ × ℝ} (hc : c p.1 ≠ 0) (y : ℝ × ℝ) :
    dgForm c b p ((c p.1)⁻¹, (0 : ℝ)) y = -(c p.1 * y.1) := by
  rw [dgForm_apply]; field_simp; ring

set_option backward.isDefEq.respectTransparency false in
/-- **C4.** `U = c⁻¹ ∂_u` is a geodesic field of THE Levi-Civita connection: `∇_U U = 0`. -/
theorem unitU_geodesic (c b : ℝ → ℝ) (hc : ∀ u, c u ≠ 0) (hb : ∀ u, b u ≠ 0)
    (hcd : Differentiable ℝ c) (hbd : Differentiable ℝ b) (p : ℝ × ℝ) :
    lcConn (ℝ × ℝ) (dgMetric c b hc hb hcd hbd) (unitU c) p (unitU c p) = 0 := by
  set m := dgMetric c b hc hb hcd hbd
  have hc1 : HasFDerivAt (fun y : ℝ × ℝ => c y.1) (deriv c p.1 • ContinuousLinearMap.fst ℝ ℝ ℝ) p := by
    exact (hcd p.1).hasDerivAt.comp_hasFDerivAt p (hasFDerivAt_fst (p := p) (𝕜 := ℝ))
  have hci : HasFDerivAt (fun y : ℝ × ℝ => (c y.1)⁻¹)
      (-(deriv c p.1 / c p.1 ^ 2) • ContinuousLinearMap.fst ℝ ℝ ℝ) p := by
    have := ((hcd p.1).hasDerivAt.inv (hc p.1)).comp_hasFDerivAt p (hasFDerivAt_fst (p := p) (𝕜 := ℝ))
    convert this using 1; ext v; simp; ring
  have hUf : HasFDerivAt (vf (unitU c)) ((-(deriv c p.1 / c p.1 ^ 2) • ContinuousLinearMap.fst ℝ ℝ ℝ).prod
      (0 : ℝ × ℝ →L[ℝ] ℝ)) p := hci.prodMk (hasFDerivAt_const (0 : ℝ) p)
  have hU : MDifferentiableAt 𝓘(ℝ, ℝ × ℝ) 𝓘(ℝ, ℝ × ℝ).tangent
      (fun q => (⟨q, unitU c q⟩ : TangentBundle 𝓘(ℝ, ℝ × ℝ) (ℝ × ℝ))) p :=
    mdiffAt_model.2 hUf.differentiableAt
  refine m.g_inj fun Z hZ => ?_
  have dZ := mdiffAt_model.1 hZ
  rw [lcConn_apply m hU hU hZ, map_zero, zero_apply]
  have gl : ∀ y (v : ℝ × ℝ), m.g y (unitU c y) v = -(c y.1 * v.1) := fun y v => dg_U_left b (hc y.1) v
  have f1 : (fun y => m.g y (unitU c y) (Z y)) = fun y => -(c y.1 * (vf Z y).1) :=
    funext fun y => gl y (Z y)
  have f2 : (fun y => m.g y (Z y) (unitU c y)) = fun y => -(c y.1 * (vf Z y).1) :=
    funext fun y => (dgForm_symm c b y (Z y) (unitU c y)).trans (gl y (Z y))
  have f3 : (fun y => m.g y (unitU c y) (unitU c y)) = fun _ => (-1 : ℝ) := funext fun y => by
    rw [gl]; show -(c y.1 * (c y.1)⁻¹) = -1; rw [mul_inv_cancel₀ (hc y.1)]
  have hZ1 : HasFDerivAt (fun y => (vf Z y).1) ((ContinuousLinearMap.fst ℝ ℝ ℝ).comp (fderiv ℝ (vf Z) p)) p :=
    hasFDerivAt_fst.comp p dZ.hasFDerivAt
  have hT : HasFDerivAt (fun y => -(c y.1 * (vf Z y).1)) _ p := (hc1.mul hZ1).neg
  have hbr : ∀ A B : Π y : ℝ × ℝ, TangentSpace 𝓘(ℝ, ℝ × ℝ) y,
      mlieBracket 𝓘(ℝ, ℝ × ℝ) A B p = fderiv ℝ (vf B) p (A p) - fderiv ℝ (vf A) p (B p) :=
    fun A B => by
      rw [← mlieBracketWithin_univ, mlieBracketWithin_eq_lieBracketWithin, lieBracketWithin_univ]; rfl
  simp only [kosz, f1, f2, f3, hbr, mvfderiv_const, zero_apply, sub_self, map_zero, hUf.fderiv]
  rw [mvfderiv_eq_fderiv, hT.fderiv]
  simp only [ContinuousLinearMap.comp_apply, sub_apply, neg_apply, add_apply, smul_apply,
    ContinuousLinearMap.coe_fst', ContinuousLinearMap.coe_snd', smul_eq_mul, fts_apply, zero_apply,
    ContinuousLinearMap.prod_apply, gl, Prod.fst_sub, Prod.snd_sub]
  have hu1 : (unitU c p : ℝ × ℝ).1 = (c p.1)⁻¹ := rfl
  have hvz : (vf Z p) = (Z p : ℝ × ℝ) := rfl
  simp only [hu1, hvz]
  have hcp := hc p.1
  field_simp
  ring

/-- The Schwarzschild interior in the chart `η = 2 arctan eᵘ`: `c(u) = 4M eᵘ/(1 + e²ᵘ)²`, `b(u) = e²ᵘ`. -/
noncomputable def cInt (M u : ℝ) : ℝ := 4 * M * Real.exp u / (1 + Real.exp (2 * u)) ^ 2

/-- The areal radius in that chart, `r(u) = 2M/(1 + e²ᵘ)`, in `(0, 2M)`. -/
noncomputable def rInt (M u : ℝ) : ℝ := 2 * M / (1 + Real.exp (2 * u))

/-- **C4, receipt 29 — the chart IS the Schwarzschild interior.** `b = e²ᵘ = 2M/r − 1` and `r′ = −c eᵘ`, so
`−c² du² + b dt² = −dr²/(2M/r − 1) + (2M/r − 1) dt²`. -/
lemma interior_chart {M : ℝ} (hM : M ≠ 0) (u : ℝ) :
    2 * M / rInt M u - 1 = Real.exp (2 * u) ∧ HasDerivAt (rInt M) (-(cInt M u * Real.exp u)) u := by
  have h1 : (0 : ℝ) < 1 + Real.exp (2 * u) := by positivity
  refine ⟨by unfold rInt; field_simp; ring, ?_⟩
  have hd := (((Real.hasDerivAt_exp (2 * u)).comp u ((hasDerivAt_id u).const_mul 2)).const_add 1).inv h1.ne'
  have := hd.const_mul (2 * M)
  unfold rInt cInt
  convert this using 1
  · funext s; simp [div_eq_mul_inv]
  · have he2 : Real.exp (2 * u) = Real.exp u ^ 2 := by rw [← Real.exp_nat_mul]; ring_nf
    simp only [Function.comp_apply, he2]
    field_simp; ring

/-- **C4, receipt 29 — the cycloid.** With `η = 2 arctan eᵘ`, the cycloid time `τ = M(η + sin η)` has `τ′ = c`: it is
the proper time along the geodesic field `U`, and `r = M(1 + cos η)`. -/
lemma cycloid_proper_time (M u : ℝ) :
    HasDerivAt (fun s => M * (2 * Real.arctan (Real.exp s) + Real.sin (2 * Real.arctan (Real.exp s))))
      (cInt M u) u ∧ rInt M u = M * (1 + Real.cos (2 * Real.arctan (Real.exp u))) := by
  have hx : (0 : ℝ) < 1 + Real.exp u ^ 2 := by positivity
  have hcos : Real.cos (2 * Real.arctan (Real.exp u)) = 2 / (1 + Real.exp u ^ 2) - 1 := by
    rw [Real.cos_two_mul, Real.cos_sq_arctan]; ring
  have he2 : Real.exp (2 * u) = Real.exp u ^ 2 := by rw [← Real.exp_nat_mul]; ring_nf
  have hη : HasDerivAt (fun s => 2 * Real.arctan (Real.exp s)) (2 * (Real.exp u / (1 + Real.exp u ^ 2))) u := by
    have := (Real.hasDerivAt_arctan (Real.exp u)).comp u (Real.hasDerivAt_exp u)
    convert this.const_mul 2 using 1
    · rfl
    · field_simp
  refine ⟨?_, ?_⟩
  · have := (hη.add (hη.sin)).const_mul M
    convert this using 1
    rw [hcos]; unfold cInt; rw [he2]; field_simp; ring
  · unfold rInt; rw [hcos, he2]; field_simp; ring

/-- **C4, receipt 29, on the named metric.** The radial infall field of the Schwarzschild interior, in the chart
where it is smooth and nondegenerate on all of `ℝ²`, is a geodesic field of THE Levi-Civita connection. -/
theorem interior_geodesic {M : ℝ} (hM : 0 < M) (p : ℝ × ℝ) :
    lcConn (ℝ × ℝ) (dgMetric (cInt M) (fun u => Real.exp (2 * u))
      (fun u => by unfold cInt; positivity) (fun u => (Real.exp_pos _).ne')
      (by unfold cInt; fun_prop (disch := intro u; positivity)) (by fun_prop))
      (unitU (cInt M)) p (unitU (cInt M) p) = 0 :=
  unitU_geodesic _ _ _ _ _ _ p

end StaticDiag

/-! ## `r7297`, C5 — receipt 77: if a metric on `E` is invariant under translation along `K`, then the constant
field `K` is a KILLING field of THE Levi-Civita connection, `g(∇_X K, Y) + g(X, ∇_Y K) = 0`. For every diagonal
metric on `ℝ⁴` whose coefficients depend on `(t, z)` only — the polarized Gowdy family — `∂_x` and `∂_y` are Killing. -/

section KillingTrans

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]

/-- The constant field `w`. -/
def constF (w : E) : Π y : E, TangentSpace 𝓘(ℝ, E) y := fun _ => w

lemma constF_mdiff (w x : E) : MDiffAt (T% (constF w)) x :=
  mdiffAt_model.2 (differentiableAt_const (c := w))

set_option backward.isDefEq.respectTransparency false in
lemma dirDeriv_invariant (m : NDMetric 𝓘(ℝ, E) E) {K : E} (hinv : ∀ y (t : ℝ), m.g (y + t • K) = m.g y)
    (u v x : E) : d% (fun y => m.g y (constF u y) (constF v y)) x K = 0 := by
  have hf : DifferentiableAt ℝ (fun y => m.g y (constF u y) (constF v y)) x :=
    mdifferentiableAt_iff_differentiableAt.1 (m.mdiff (constF_mdiff u x) (constF_mdiff v x))
  have hl : HasDerivAt (fun t : ℝ => x + t • K) K 0 := by
    simpa using ((hasDerivAt_id (0 : ℝ)).smul_const K).const_add x
  have h1 := HasFDerivAt.comp_hasDerivAt_of_eq (x := (0 : ℝ)) hf.hasFDerivAt hl (by simp)
  have h2 : HasDerivAt ((fun y => m.g y (constF u y) (constF v y)) ∘ fun t : ℝ => x + t • K) 0 0 := by
    have : ((fun y => m.g y (constF u y) (constF v y)) ∘ fun t : ℝ => x + t • K) =
        fun _ => m.g x u v := by
      funext t; simp only [Function.comp, constF, hinv]; rfl
    rw [this]; exact hasDerivAt_const _ _
  rw [mvfderiv_eq_fderiv]
  exact h1.unique h2

set_option backward.isDefEq.respectTransparency false in
/-- **C5.** Translation invariance along `K` makes `K` a Killing field of THE Levi-Civita connection. -/
theorem killing_of_invariant (m : NDMetric 𝓘(ℝ, E) E) {K : E} (hinv : ∀ y (t : ℝ), m.g (y + t • K) = m.g y)
    (x u v : E) :
    m.g x (lcConn E m (constF K) x u) v + m.g x u (lcConn E m (constF K) x v) = 0 := by
  rw [m.symm x u, show m.g x (lcConn E m (constF K) x u) v
      = m.g x (lcConn E m (constF K) x (constF u x)) (constF v x) from rfl,
    show m.g x (lcConn E m (constF K) x v) u
      = m.g x (lcConn E m (constF K) x (constF v x)) (constF u x) from rfl,
    lcConn_apply m (constF_mdiff u x) (constF_mdiff K x) (constF_mdiff v x),
    lcConn_apply m (constF_mdiff v x) (constF_mdiff K x) (constF_mdiff u x)]
  simp only [kosz]
  have hb : ∀ a b : E, mlieBracket 𝓘(ℝ, E) (constF a) (constF b) x = 0 := fun a b => by
    rw [← mlieBracketWithin_univ, mlieBracketWithin_eq_lieBracketWithin, lieBracketWithin_univ,
      lieBracket_eq]
    show fderiv ℝ (fun _ : E => b) x a - fderiv ℝ (fun _ : E => a) x b = 0
    simp
  simp only [hb, map_zero]
  rw [m.fun_symm (constF u) (constF K), m.fun_symm (constF K) (constF v), m.fun_symm (constF v) (constF u)]
  have h0 : d% (fun y => m.g y (constF u y) (constF v y)) x (constF K x) = 0 :=
    dirDeriv_invariant m hinv u v x
  linarith

/-- A diagonal form on `ℝ⁴`: `Σᵢ cᵢ(p) dxᵢ²`, any signature. -/
noncomputable def diag4 (c : Fin 4 → (Fin 4 → ℝ) → ℝ) (p : Fin 4 → ℝ) :
    (Fin 4 → ℝ) →L[ℝ] (Fin 4 → ℝ) →L[ℝ] ℝ :=
  ∑ i, c i p • (ContinuousLinearMap.mul ℝ ℝ).bilinearComp (ContinuousLinearMap.proj i)
    (ContinuousLinearMap.proj i)

lemma diag4_apply (c : Fin 4 → (Fin 4 → ℝ) → ℝ) (p u v : Fin 4 → ℝ) :
    diag4 c p u v = ∑ i, c i p * (u i * v i) := by
  simp [diag4]

lemma diag4_symm (c : Fin 4 → (Fin 4 → ℝ) → ℝ) (p u v : Fin 4 → ℝ) : diag4 c p u v = diag4 c p v u := by
  rw [diag4_apply, diag4_apply]; exact Finset.sum_congr rfl fun i _ => by ring

lemma diag4_nondeg {c : Fin 4 → (Fin 4 → ℝ) → ℝ} {p : Fin 4 → ℝ} (hc : ∀ i, c i p ≠ 0) (u : Fin 4 → ℝ)
    (h : ∀ v : Fin 4 → ℝ, diag4 c p u v = 0) : u = 0 := by
  funext j
  have hj := h (Pi.single j 1)
  rw [diag4_apply, Finset.sum_eq_single j (fun i _ hi => by simp [Pi.single_apply, hi])
    (by simp)] at hj
  simpa [hc j] using hj

/-- A diagonal metric with nonvanishing differentiable coefficients, as an `NDMetric` on `ℝ⁴`. -/
noncomputable def diag4Metric (c : Fin 4 → (Fin 4 → ℝ) → ℝ) (hc : ∀ i p, c i p ≠ 0)
    (hcd : ∀ i, Differentiable ℝ (c i)) : NDMetric 𝓘(ℝ, Fin 4 → ℝ) (Fin 4 → ℝ) where
  g p := diag4 c p
  symm p u v := diag4_symm c p u v
  nondeg p u h := diag4_nondeg (fun i => hc i p) u h
  mdiff {Y Z x} hY hZ := by
    rw [mdiffAt_model] at hY hZ
    rw [mdifferentiableAt_iff_differentiableAt]
    have e : (fun y => diag4 c y (Y y) (Z y)) = fun y => ∑ i, c i y * (vf Y y i * vf Z y i) := by
      funext y; exact diag4_apply c y (Y y) (Z y)
    show DifferentiableAt ℝ (fun y => diag4 c y (Y y) (Z y)) x
    rw [e]
    have hYi : ∀ i, DifferentiableAt ℝ (fun y => vf Y y i) x := fun i =>
      ((ContinuousLinearMap.proj (R := ℝ) (φ := fun _ : Fin 4 => ℝ) i).differentiableAt).comp x hY
    have hZi : ∀ i, DifferentiableAt ℝ (fun y => vf Z y i) x := fun i =>
      ((ContinuousLinearMap.proj (R := ℝ) (φ := fun _ : Fin 4 => ℝ) i).differentiableAt).comp x hZ
    exact DifferentiableAt.fun_sum fun i _ => ((hcd i x).mul ((hYi i).mul (hZi i)))

/-- **C5, receipt 77.** For EVERY diagonal metric on `ℝ⁴` (any signature) whose coefficients depend on the
coordinates `(t, z) = (x₀, x₁)` only — the polarized Gowdy family, for all profiles — `∂_x` and `∂_y` are Killing
fields of THE Levi-Civita connection. -/
theorem gowdy_killing (c : Fin 4 → (Fin 4 → ℝ) → ℝ) (hc : ∀ i p, c i p ≠ 0)
    (hcd : ∀ i, Differentiable ℝ (c i))
    (hdep : ∀ i (p q : Fin 4 → ℝ), p 0 = q 0 → p 1 = q 1 → c i p = c i q)
    (k : Fin 4) (hk : k = 2 ∨ k = 3) (x u v : Fin 4 → ℝ) :
    (diag4Metric c hc hcd).g x (lcConn (Fin 4 → ℝ) (diag4Metric c hc hcd) (constF (Pi.single k 1)) x u) v
      + (diag4Metric c hc hcd).g x u
          (lcConn (Fin 4 → ℝ) (diag4Metric c hc hcd) (constF (Pi.single k 1)) x v) = 0 := by
  refine killing_of_invariant _ (fun y t => ?_) x u v
  have h0 : (0 : Fin 4) ≠ k := by rcases hk with rfl | rfl <;> decide
  have h1 : (1 : Fin 4) ≠ k := by rcases hk with rfl | rfl <;> decide
  show diag4 c (y + t • Pi.single k 1) = diag4 c y
  have : ∀ i, c i (y + t • Pi.single k 1) = c i y := fun i =>
    hdep i _ _ (by simp [Pi.single_apply, h0]) (by simp [Pi.single_apply, h1])
  simp only [diag4, this]

end KillingTrans

/-! ## r7311 — item A: the smoothness class on THE connection, DISCHARGED on the model space -/

section SmoothLC

set_option synthInstance.maxHeartbeats 400000

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  (B : E → E →L[ℝ] E →L[ℝ] ℝ)

/-- The `NDMetric` of a differentiable, symmetric, nondegenerate field of forms on `E`. -/
noncomputable def ndOf (hs : ∀ x u v, B x u v = B x v u) (hn : ∀ x (u : E), (∀ v, B x u v = 0) → u = 0)
    (hB : Differentiable ℝ B) : NDMetric 𝓘(ℝ, E) E where
  g := B
  symm := hs
  nondeg := hn
  mdiff {Y Z x} hY hZ := by
    rw [mdiffAt_model] at hY hZ
    rw [mdifferentiableAt_iff_differentiableAt]
    exact ((hB x).clm_apply hY).clm_apply hZ

/-- **A2's key step: `♭ = B x` is invertible**, by nondegeneracy and equal finite dimension. -/
lemma flat_isInvertible (hn : ∀ x (u : E), (∀ v, B x u v = 0) → u = 0) (x : E) : (B x).IsInvertible := by
  have hinj : Function.Injective (B x) := fun a b h =>
    sub_eq_zero.1 (hn x _ fun v => by rw [map_sub, ContinuousLinearMap.sub_apply, h, sub_self])
  have H : Module.finrank ℝ E = Module.finrank ℝ (E →L[ℝ] ℝ) := by
    rw [← LinearEquiv.finrank_eq (LinearMap.toContinuousLinearMap (𝕜 := ℝ) (E := E) (F' := ℝ))]
    exact Subspace.dual_finrank_eq.symm
  have hsurj : Function.Surjective (B x) :=
    (LinearMap.injective_iff_surjective_of_finrank_eq_finrank H (f := (B x).toLinearMap)).1 hinj
  exact ⟨ContinuousLinearEquiv.ofBijective (B x) (LinearMap.ker_eq_bot.2 hinj)
    (LinearMap.range_eq_top.2 hsurj), rfl⟩

/-- The Koszul form on constant fields, as a bilinear map into the dual:
`K x a b v = ½[(DB·a)(b,v) + (DB·b)(v,a) − (DB·v)(a,b)]`. -/
noncomputable def koszK (x : E) : E →L[ℝ] E →L[ℝ] E →L[ℝ] ℝ :=
  let fl : (E →L[ℝ] E →L[ℝ] ℝ) →L[ℝ] (E →L[ℝ] E →L[ℝ] ℝ) :=
    (ContinuousLinearMap.flipₗᵢ ℝ E E ℝ).toContinuousLinearEquiv.toContinuousLinearMap
  (1 / 2 : ℝ) • (fderiv ℝ B x + (fl.comp (fderiv ℝ B x)).flip + (-1 : ℝ) • fl.comp (fderiv ℝ B x).flip)

lemma koszK_apply (x a b v : E) :
    koszK B x a b v = (fderiv ℝ B x a b v + fderiv ℝ B x b v a - fderiv ℝ B x v a b) / 2 := by
  simp [koszK]; ring

/-- **A1's object: the Christoffel form of `lcConn`**, `Γ x a b = ♭⁻¹(K x a b)`. -/
noncomputable def lcGam (x : E) : E →L[ℝ] E →L[ℝ] E :=
  (ContinuousLinearMap.compL ℝ E (E →L[ℝ] ℝ) E (B x).inverse).comp (koszK B x)

lemma lcGam_apply (x a b : E) : lcGam B x a b = (B x).inverse (koszK B x a b) := rfl

variable {B}

set_option backward.isDefEq.respectTransparency false in
/-- **A1. `lcConn` HAS the Christoffel form `lcGam`** on constant fields: `∇_a b = Γ(a, b)`. -/
theorem lcConn_const (hs : ∀ x u v, B x u v = B x v u) (hn : ∀ x (u : E), (∀ v, B x u v = 0) → u = 0)
    (hB : Differentiable ℝ B) (x a b : E) :
    lcConn E (ndOf B hs hn hB) (fun _ => b) x a = lcGam B x a b := by
  set m := ndOf B hs hn hB
  refine (flat_isInvertible B hn x).injective (ContinuousLinearMap.ext fun v => ?_)
  have h1 : m.g x (lcConn E m (constF b) x (constF a x)) (constF v x) = kosz m (constF a) (constF b) (constF v) x :=
    lcConn_apply m (constF_mdiff a x) (constF_mdiff b x) (constF_mdiff v x)
  have hb : ∀ p q : E, mlieBracket 𝓘(ℝ, E) (constF p) (constF q) x = 0 := fun p q => by
    rw [← mlieBracketWithin_univ, mlieBracketWithin_eq_lieBracketWithin, lieBracketWithin_univ,
      lieBracket_eq]
    show fderiv ℝ (fun _ : E => q) x p - fderiv ℝ (fun _ : E => p) x q = 0
    simp
  have hd : ∀ p q c : E, d% (fun y => m.g y (constF p y) (constF q y)) x c = fderiv ℝ B x c p q :=
    fun p q c => by
      rw [mvfderiv_eq_fderiv]
      have h := ((hB x).hasFDerivAt.clm_apply (hasFDerivAt_const p x)).clm_apply (hasFDerivAt_const q x)
      show fderiv ℝ (fun y => B y p q) x c = _
      rw [h.fderiv]
      simp
  simp only [kosz, hb, map_zero, sub_zero, add_zero, hd] at h1
  have h2 : m.g x (lcGam B x a b) v = koszK B x a b v := by
    show B x ((B x).inverse (koszK B x a b)) v = _
    rw [(flat_isInvertible B hn x).self_apply_inverse]
  show m.g x (lcConn E m (constF b) x (constF a x)) (constF v x) = m.g x (lcGam B x a b) v
  rw [h1, h2, koszK_apply]
  simp only [constF]

/-- **A2. `lcGam` is `C^∞` when `B` is**: inversion is smooth at an invertible map. -/
theorem lcGam_smooth (hn : ∀ x (u : E), (∀ v, B x u v = 0) → u = 0) (hB : ContDiff ℝ ∞ B) :
    ContDiff ℝ ∞ (lcGam B) := by
  have hinv : ContDiff ℝ ∞ fun x => (B x).inverse :=
    contDiff_iff_contDiffAt.2 fun x =>
      (flat_isInvertible B hn x).contDiffAt_map_inverse.comp x hB.contDiffAt
  have hD := hB.fderiv_right (m := ∞) (by simp)
  rw [contDiff_clm_apply_iff]; intro a
  rw [contDiff_clm_apply_iff]; intro b
  simp only [lcGam_apply]
  refine hinv.clm_apply ?_
  rw [contDiff_clm_apply_iff]; intro v
  simp only [koszK_apply]
  have e : ∀ p q r : E, ContDiff ℝ ∞ fun x => fderiv ℝ B x p q r := fun p q r =>
    ((hD.clm_apply contDiff_const).clm_apply contDiff_const).clm_apply contDiff_const
  exact (((e a b v).add (e b v a)).sub (e v a b)).div_const 2

/-- **A3. THE smoothness class on THE connection.** For a `C^∞` symmetric nondegenerate form field on `E`,
the Levi-Civita connection is a `C^∞` covariant derivative in `mathlib`'s sense — K1–K3 apply to it with no
class carried. -/
theorem lcConn_contMDiffCov (hs : ∀ x u v, B x u v = B x v u) (hn : ∀ x (u : E), (∀ v, B x u v = 0) → u = 0)
    (hB : ContDiff ℝ ∞ B) :
    CovariantDerivative.ContMDiffCovariantDerivative (lcConn E (ndOf B hs hn (hB.differentiable (by simp))))
      (∞ : ℕ∞ω) :=
  contMDiffCov_model _ (lcGam B) (fun x w u => lcConn_const hs hn _ x w u) (lcGam_smooth hn hB)

/-! ### A3 on the named metrics already in the tree, and A4 -/

/-- **A3 on C2/C3's Painlevé–Gullstrand metric**: with `C^∞` profiles, its Levi-Civita connection is `C^∞`. -/
theorem pg_contMDiffCov {A w : ℝ → ℝ} (hA : ∀ s, A s ≠ 0) (hAs : ContDiff ℝ ∞ A) (hws : ContDiff ℝ ∞ w)
    (hAd : Differentiable ℝ A) (hw : Differentiable ℝ w) :
    CovariantDerivative.ContMDiffCovariantDerivative (lcConn (ℝ × ℝ) (pgMetric A w hA hAd hw)) (∞ : ℕ∞ω) := by
  have hB : ContDiff ℝ ∞ (pgForm A w) := by
    rw [contDiff_clm_apply_iff]; intro a; rw [contDiff_clm_apply_iff]; intro b
    simp only [pgForm_apply]
    have h1 : ContDiff ℝ ∞ fun p : ℝ × ℝ => A p.2 := hAs.comp contDiff_snd
    have h2 : ContDiff ℝ ∞ fun p : ℝ × ℝ => w p.2 := hws.comp contDiff_snd
    fun_prop
  exact lcConn_contMDiffCov (B := pgForm A w) (fun p a b => pgForm_symm A w p a b)
    (fun p u h => pgForm_nondeg w (hA p.2) u h) hB

/-- **A3 on C4's static diagonal metric** `−c² du² + b dt²` (the Schwarzschild interior chart). -/
theorem dg_contMDiffCov {c b : ℝ → ℝ} (hc : ∀ u, c u ≠ 0) (hb : ∀ u, b u ≠ 0) (hcs : ContDiff ℝ ∞ c)
    (hbs : ContDiff ℝ ∞ b) (hcd : Differentiable ℝ c) (hbd : Differentiable ℝ b) :
    CovariantDerivative.ContMDiffCovariantDerivative (lcConn (ℝ × ℝ) (dgMetric c b hc hb hcd hbd))
      (∞ : ℕ∞ω) := by
  have hB : ContDiff ℝ ∞ (dgForm c b) := by
    rw [contDiff_clm_apply_iff]; intro x; rw [contDiff_clm_apply_iff]; intro y
    simp only [dgForm_apply]
    have h1 : ContDiff ℝ ∞ fun p : ℝ × ℝ => c p.1 := hcs.comp contDiff_fst
    have h2 : ContDiff ℝ ∞ fun p : ℝ × ℝ => b p.1 := hbs.comp contDiff_fst
    fun_prop
  exact lcConn_contMDiffCov (B := dgForm c b) (fun p x y => dgForm_symm c b p x y)
    (fun p x h => dgForm_nondeg (hc p.1) (hb p.1) x h) hB

/-- **A3 on C5's diagonal metric on `ℝ⁴`** (the polarized Gowdy family). -/
theorem diag4_contMDiffCov {c : Fin 4 → (Fin 4 → ℝ) → ℝ} (hc : ∀ i p, c i p ≠ 0)
    (hcs : ∀ i, ContDiff ℝ ∞ (c i)) (hcd : ∀ i, Differentiable ℝ (c i)) :
    CovariantDerivative.ContMDiffCovariantDerivative (lcConn (Fin 4 → ℝ) (diag4Metric c hc hcd))
      (∞ : ℕ∞ω) := by
  have hB : ContDiff ℝ ∞ (diag4 c) := by
    rw [contDiff_clm_apply_iff]; intro u; rw [contDiff_clm_apply_iff]; intro v
    simp only [diag4_apply]
    exact ContDiff.sum fun i _ => (hcs i).mul contDiff_const
  exact lcConn_contMDiffCov (B := diag4 c) (fun p u v => diag4_symm c p u v)
    (fun p u h => diag4_nondeg (fun i => hc i p) u h) hB

/-- **A4.** K1's `R(fX, Y)Z = f R(X, Y)Z` holds for THE Levi-Civita connection of the PG metric with NO class
hypothesis: A3 supplies it. The `C^∞` statements already built apply as they stand. -/
theorem pg_curv_smul_left {A w : ℝ → ℝ} (hA : ∀ s, A s ≠ 0) (hAs : ContDiff ℝ ∞ A) (hws : ContDiff ℝ ∞ w)
    (hAd : Differentiable ℝ A) (hw : Differentiable ℝ w) {f : ℝ × ℝ → ℝ}
    (hf : ContMDiff 𝓘(ℝ, ℝ × ℝ) 𝓘(ℝ, ℝ) ∞ f)
    {X Y Z : Π x : ℝ × ℝ, TangentSpace 𝓘(ℝ, ℝ × ℝ) x}
    (hX : ContMDiff 𝓘(ℝ, ℝ × ℝ) 𝓘(ℝ, ℝ × ℝ).tangent ∞ fun q => (⟨q, X q⟩ : TangentBundle 𝓘(ℝ, ℝ × ℝ) (ℝ × ℝ)))
    (hY : ContMDiff 𝓘(ℝ, ℝ × ℝ) 𝓘(ℝ, ℝ × ℝ).tangent ∞ fun q => (⟨q, Y q⟩ : TangentBundle 𝓘(ℝ, ℝ × ℝ) (ℝ × ℝ)))
    (hZ : ContMDiff 𝓘(ℝ, ℝ × ℝ) 𝓘(ℝ, ℝ × ℝ).tangent ∞ fun q => (⟨q, Z q⟩ : TangentBundle 𝓘(ℝ, ℝ × ℝ) (ℝ × ℝ)))
    (x : ℝ × ℝ) :
    curv (lcConn (ℝ × ℝ) (pgMetric A w hA hAd hw)) (f • X) Y Z x
      = f x • curv (lcConn (ℝ × ℝ) (pgMetric A w hA hAd hw)) X Y Z x := by
  haveI := pg_contMDiffCov hA hAs hws hAd hw
  exact curv_smul_left _ hf hX hY hZ x

end SmoothLC

/-! ## `r7315`, B1 — receipt 99: at the Nariai mass the SdS function `f = 1 − 2a/(3r) − r²/(3a²)` (`α = √3 a`) has
a double root at `r = a` and a simple root at `r = −2a`, and THE Levi-Civita connection's surface gravity is `0` at
the first and `3/(4a) = 3√3/(4α)` at the second -/

section SweepB1

/-- SdS at the Nariai mass, in the scale `a = α/√3`. -/
noncomputable def fNar (a r : ℝ) : ℝ := 1 - 2 * a / (3 * r) - r ^ 2 / (3 * a ^ 2)

lemma fNar_hasDerivAt {a : ℝ} (ha : a ≠ 0) {r : ℝ} (hr : r ≠ 0) :
    HasDerivAt (fNar a) (2 * a / (3 * r ^ 2) - 2 * r / (3 * a ^ 2)) r := by
  have e : fNar a = fun s => 1 - 2 * a / 3 * s⁻¹ - s ^ 2 / (3 * a ^ 2) := by
    funext s; simp only [fNar]; ring
  rw [e]
  refine HasDerivAt.congr_deriv (HasDerivAt.sub (HasDerivAt.sub (hasDerivAt_const r (1 : ℝ))
    ((hasDerivAt_inv hr).const_mul (2 * a / 3))) ((hasDerivAt_pow 2 r).div_const (3 * a ^ 2))) ?_
  field_simp; ring

/-- **B1, receipt 99.** Any PG profile `w` with `1 − w² = f` near each root and `w = −1` there: the surface
gravity `∇_ξ ξ = κ ξ` is `κ = 0` at the double root and `κ = 3/(4a)` at the simple root. -/
theorem two_surface_gravities (a : ℝ) (ha : a ≠ 0) (w : ℝ → ℝ) (hw : Differentiable ℝ w)
    (hf₁ : (fun s => 1 - w s ^ 2) =ᶠ[nhds a] fNar a) (hf₂ : (fun s => 1 - w s ^ 2) =ᶠ[nhds (-2 * a)] fNar a)
    (h₁ : w a = -1) (h₂ : w (-2 * a) = -1) (τ₁ τ₂ : ℝ) :
    lcConn (ℝ × ℝ) (pgMetric (fun _ => 1) w (fun _ => one_ne_zero) (differentiable_const _) hw)
        xiT (τ₁, a) (xiT (τ₁, a)) = 0
    ∧ lcConn (ℝ × ℝ) (pgMetric (fun _ => 1) w (fun _ => one_ne_zero) (differentiable_const _) hw)
        xiT (τ₂, -2 * a) (xiT (τ₂, -2 * a)) = (3 / (4 * a)) • xiT (τ₂, -2 * a) := by
  have k : ∀ r, w r = -1 → (fun s => 1 - w s ^ 2) =ᶠ[nhds r] fNar a → r ≠ 0 →
      deriv w r = (2 * a / (3 * r ^ 2) - 2 * r / (3 * a ^ 2)) / 2 := fun r h hf hr => by
    rw [← kappa_half_fprime w r (hw r) h, hf.deriv_eq, (fNar_hasDerivAt ha hr).deriv]
  refine ⟨?_, ?_⟩
  · rw [surface_gravity w hw _ h₁, k a h₁ hf₁ ha]
    have : (2 * a / (3 * a ^ 2) - 2 * a / (3 * a ^ 2)) / 2 = 0 := by ring
    rw [this, zero_smul]
  · rw [surface_gravity w hw _ h₂, k _ h₂ hf₂ (by simpa using ha)]
    congr 1; field_simp; ring

end SweepB1

/-! ## `r7315`, B2 — receipt 109: pure de Sitter `f = 1 − r²/α²` in PG form, `w = −r/α`. On `r > 0` the horizon
`w = −1` is `r = α` alone, and THE Levi-Civita connection gives it surface gravity `|κ| = |f′(α)|/2 = 1/α` -/

section SweepB2

/-- de Sitter's PG profile, with `1 − w² = 1 − r²/α²` identically. -/
noncomputable def wDS (α r : ℝ) : ℝ := -(r / α)

lemma wDS_diff (α : ℝ) : Differentiable ℝ (wDS α) := by unfold wDS; fun_prop

lemma ds_horizon_iff {α r : ℝ} (hα : 0 < α) : wDS α r = -1 ↔ r = α := by
  unfold wDS; constructor
  · intro h; field_simp at h; linarith
  · rintro rfl; field_simp

/-- **B2, receipt 109.** `∇_ξ ξ = −(1/α) ξ` on the de Sitter horizon, and `|f′(α)|/2 = 1/α`. -/
theorem ds_surface_gravity {α : ℝ} (hα : 0 < α) (τ : ℝ) :
    lcConn (ℝ × ℝ) (pgMetric (fun _ => 1) (wDS α) (fun _ => one_ne_zero) (differentiable_const _) (wDS_diff α))
      xiT (τ, α) (xiT (τ, α)) = -(1 / α) • xiT (τ, α)
    ∧ |deriv (fun s => 1 - s ^ 2 / α ^ 2) α / 2| = 1 / α := by
  have hd : HasDerivAt (wDS α) (-(1 / α)) α := HasDerivAt.neg ((hasDerivAt_id α).div_const α)
  have hh : wDS α (τ, α).2 = -1 := (ds_horizon_iff hα).2 rfl
  have hf : (fun s => 1 - s ^ 2 / α ^ 2) = fun s => 1 - wDS α s ^ 2 := by funext s; unfold wDS; ring
  refine ⟨by rw [surface_gravity _ (wDS_diff α) _ hh, hd.deriv], ?_⟩
  rw [hf, kappa_half_fprime _ α (wDS_diff α α) hh, hd.deriv, abs_neg, abs_of_pos (by positivity)]

end SweepB2

/-! ## `r7315`, B3 — receipt 11: the accelerated de Sitter temperature `T(a) = √(1/α² + a²)/2π` tends to `|κ|/2π`
as `a → 0`, where `κ` is THE Levi-Civita connection's surface gravity on the horizon (B2), and to the flat Unruh law
`T ~ a/2π` as `a → ∞`. The Nariai member's `κ = 0` is B1 -/

section SweepB3

open Filter Topology in
/-- **B3, receipt 11.** -/
theorem unruh_ds_limits {α : ℝ} (hα : 0 < α) (τ : ℝ) :
    ∃ κ : ℝ, lcConn (ℝ × ℝ) (pgMetric (fun _ => 1) (wDS α) (fun _ => one_ne_zero) (differentiable_const _)
        (wDS_diff α)) xiT (τ, α) (xiT (τ, α)) = κ • xiT (τ, α)
      ∧ Tendsto (fun a : ℝ => Real.sqrt ((1 / α) ^ 2 + a ^ 2) / (2 * Real.pi)) (𝓝 0) (𝓝 (|κ| / (2 * Real.pi)))
      ∧ Tendsto (fun a : ℝ => Real.sqrt ((1 / α) ^ 2 + a ^ 2) / (2 * Real.pi) / (a / (2 * Real.pi))) atTop (𝓝 1) := by
  refine ⟨-(1 / α), (ds_surface_gravity hα τ).1, ?_, ?_⟩
  · have hc : Continuous fun a : ℝ => Real.sqrt ((1 / α) ^ 2 + a ^ 2) / (2 * Real.pi) := by fun_prop
    convert hc.tendsto 0 using 2
    rw [abs_neg, abs_of_pos (by positivity)]
    simp; exact (Real.sqrt_sq hα.le).symm
  · have h0 : Tendsto (fun a : ℝ => (1 / α) ^ 2 / a ^ 2 + 1) atTop (𝓝 (0 + 1)) :=
      (tendsto_const_nhds.div_atTop (tendsto_pow_atTop two_ne_zero)).add tendsto_const_nhds
    have h1 := (Real.continuous_sqrt.tendsto _).comp h0
    rw [zero_add, Real.sqrt_one] at h1
    refine h1.congr' ?_
    filter_upwards [eventually_gt_atTop 0] with a ha
    simp only [Function.comp_apply]
    have hpi : (2 * Real.pi) ≠ 0 := by positivity
    have e : (1 / α) ^ 2 / a ^ 2 + 1 = ((1 / α) ^ 2 + a ^ 2) / a ^ 2 := by field_simp
    rw [div_div_div_cancel_right₀ hpi, e, Real.sqrt_div (by positivity), Real.sqrt_sq ha.le]

end SweepB3

/-! ## `r7315`, B4 — receipt 34: for a diagonal 2D metric `e(r) dr² + h(r) dφ²`, THE Levi-Civita connection's
curvature gives `g(R(∂_r, ∂_φ)∂_φ, ∂_r) = −h″/2 + e′h′/(4e) + h′²/(4h)`; on the slice `dr²/f + r² dφ²` the
Gaussian curvature is `K_G = −f′/(2r)` -/

section SweepB4

set_option synthInstance.maxHeartbeats 400000

/-- The diagonal form `e(r) dr² + h(r) dφ²` on `ℝ²`, in the chart `p = (r, φ)`. -/
noncomputable def diagF (e h : ℝ → ℝ) (p : ℝ × ℝ) : ℝ × ℝ →L[ℝ] ℝ × ℝ →L[ℝ] ℝ :=
  e p.1 • (ContinuousLinearMap.mul ℝ ℝ).bilinearComp (ContinuousLinearMap.fst ℝ ℝ ℝ) (ContinuousLinearMap.fst ℝ ℝ ℝ)
    + h p.1 • (ContinuousLinearMap.mul ℝ ℝ).bilinearComp (ContinuousLinearMap.snd ℝ ℝ ℝ)
      (ContinuousLinearMap.snd ℝ ℝ ℝ)

lemma diagF_apply (e h : ℝ → ℝ) (p a b : ℝ × ℝ) : diagF e h p a b = e p.1 * (a.1 * b.1) + h p.1 * (a.2 * b.2) := by
  simp [diagF]

lemma diagF_symm (e h : ℝ → ℝ) (p a b : ℝ × ℝ) : diagF e h p a b = diagF e h p b a := by
  rw [diagF_apply, diagF_apply]; ring

lemma diagF_nondeg {e h : ℝ → ℝ} (he : ∀ s, e s ≠ 0) (hh : ∀ s, h s ≠ 0) (p a : ℝ × ℝ)
    (H : ∀ b, diagF e h p a b = 0) : a = 0 := by
  have h1 := H ((1 : ℝ), (0 : ℝ)); have h2 := H ((0 : ℝ), (1 : ℝ))
  simp only [diagF_apply, mul_one, mul_zero, add_zero, zero_add] at h1 h2
  exact Prod.ext ((mul_eq_zero.1 h1).resolve_left (he _)) ((mul_eq_zero.1 h2).resolve_left (hh _))

lemma diagF_smooth {e h : ℝ → ℝ} (he : ContDiff ℝ ∞ e) (hh : ContDiff ℝ ∞ h) : ContDiff ℝ ∞ (diagF e h) := by
  rw [contDiff_clm_apply_iff]; intro a; rw [contDiff_clm_apply_iff]; intro b
  simp only [diagF_apply]
  have h1 : ContDiff ℝ ∞ fun p : ℝ × ℝ => e p.1 := he.comp contDiff_fst
  have h2 : ContDiff ℝ ∞ fun p : ℝ × ℝ => h p.1 := hh.comp contDiff_fst
  fun_prop

/-- A function of `r` alone, differentiated along `c`. -/
lemma fderiv_of_fst {F : Type*} [NormedAddCommGroup F] [NormedSpace ℝ F] {ψ : ℝ → F} {p : ℝ × ℝ}
    (hψ : DifferentiableAt ℝ ψ p.1) (c : ℝ × ℝ) : fderiv ℝ (fun y : ℝ × ℝ => ψ y.1) p c = c.1 • deriv ψ p.1 := by
  have H : HasFDerivAt (fun y : ℝ × ℝ => ψ y.1) ((fderiv ℝ ψ p.1).comp (ContinuousLinearMap.fst ℝ ℝ ℝ)) p :=
    hψ.hasFDerivAt.comp p hasFDerivAt_fst
  rw [H.fderiv]
  calc (fderiv ℝ ψ p.1).comp (ContinuousLinearMap.fst ℝ ℝ ℝ) c = fderiv ℝ ψ p.1 (c.1 • (1 : ℝ)) := by simp
    _ = c.1 • deriv ψ p.1 := by rw [map_smul]; rfl

/-- Two-slot evaluation of the derivative of a bilinear-map field. -/
lemma fderiv_apply₂ {F : Type*} [NormedAddCommGroup F] [NormedSpace ℝ F]
    {Φ : ℝ × ℝ → (ℝ × ℝ →L[ℝ] ℝ × ℝ →L[ℝ] F)} {p : ℝ × ℝ} (hΦ : DifferentiableAt ℝ Φ p) (c a b : ℝ × ℝ) :
    fderiv ℝ Φ p c a b = fderiv ℝ (fun y => Φ y a b) p c := by
  rw [fderiv_clm_apply (hΦ.clm_apply (differentiableAt_const a)) (differentiableAt_const b),
    fderiv_clm_apply hΦ (differentiableAt_const a)]
  simp

/-- The explicit Christoffel form of `e dr² + h dφ²`. -/
noncomputable def gD (e h : ℝ → ℝ) (s : ℝ) (a b : ℝ × ℝ) : ℝ × ℝ :=
  (deriv e s / (2 * e s) * (a.1 * b.1) - deriv h s / (2 * e s) * (a.2 * b.2),
   deriv h s / (2 * h s) * (a.1 * b.2 + a.2 * b.1))

variable {e h : ℝ → ℝ} (he : ∀ s, e s ≠ 0) (hh : ∀ s, h s ≠ 0) (hes : ContDiff ℝ ∞ e) (hhs : ContDiff ℝ ∞ h)
include he hh hes hhs

/-- **B4, the Christoffel form:** `lcGam` of `e dr² + h dφ²` is `gD`. -/
lemma lcGam_diag (p a b : ℝ × ℝ) : lcGam (diagF e h) p a b = gD e h p.1 a b := by
  have hn := diagF_nondeg he hh
  have inv := flat_isInvertible (diagF e h) hn p
  have hD : ∀ c a b : ℝ × ℝ, fderiv ℝ (diagF e h) p c a b
      = c.1 * (deriv e p.1 * (a.1 * b.1) + deriv h p.1 * (a.2 * b.2)) := fun c a b => by
    rw [fderiv_apply₂ ((diagF_smooth hes hhs).differentiable (by simp) p)]
    have : (fun y => diagF e h y a b) = fun y : ℝ × ℝ => e y.1 * (a.1 * b.1) + h y.1 * (a.2 * b.2) :=
      funext fun y => diagF_apply e h y a b
    rw [this, fderiv_of_fst (F := ℝ) (ψ := fun s => e s * (a.1 * b.1) + h s * (a.2 * b.2))
      ((((hes.differentiable (by simp)) _).mul_const _).add (((hhs.differentiable (by simp)) _).mul_const _))]
    have hd : HasDerivAt (fun s => e s * (a.1 * b.1) + h s * (a.2 * b.2))
        (deriv e p.1 * (a.1 * b.1) + deriv h p.1 * (a.2 * b.2)) p.1 :=
      HasDerivAt.add (((hes.differentiable (by simp)) p.1).hasDerivAt.mul_const (a.1 * b.1))
        (((hhs.differentiable (by simp)) p.1).hasDerivAt.mul_const (a.2 * b.2))
    rw [hd.deriv, smul_eq_mul]
  have hK : koszK (diagF e h) p a b = diagF e h p (gD e h p.1 a b) := by
    refine ContinuousLinearMap.ext fun v => ?_
    rw [koszK_apply, hD, hD, hD, diagF_apply]
    simp only [gD]
    have := he p.1; have := hh p.1
    field_simp; ring
  rw [lcGam_apply, hK, inv.inverse_apply_self]

/-- `gD` differentiated in `r`. -/
lemma gD_hasDerivAt (s : ℝ) (a b : ℝ × ℝ) : HasDerivAt (fun t => gD e h t a b)
    (((deriv (deriv e) s * (2 * e s) - deriv e s * (2 * deriv e s)) / (2 * e s) ^ 2 * (a.1 * b.1)
        - (deriv (deriv h) s * (2 * e s) - deriv h s * (2 * deriv e s)) / (2 * e s) ^ 2 * (a.2 * b.2),
      (deriv (deriv h) s * (2 * h s) - deriv h s * (2 * deriv h s)) / (2 * h s) ^ 2 * (a.1 * b.2 + a.2 * b.1))) s := by
  have hE := ((hes.differentiable (by simp)) s).hasDerivAt
  have hH := ((hhs.differentiable (by simp)) s).hasDerivAt
  have hE' := (((contDiff_infty_iff_deriv.1 hes).2.differentiable (by simp)) s).hasDerivAt
  have hH' := (((contDiff_infty_iff_deriv.1 hhs).2.differentiable (by simp)) s).hasDerivAt
  have e2 : 2 * e s ≠ 0 := mul_ne_zero two_ne_zero (he s)
  have h2 : 2 * h s ≠ 0 := mul_ne_zero two_ne_zero (hh s)
  exact HasDerivAt.prodMk
    (HasDerivAt.sub ((hE'.div (hE.const_mul 2) e2).mul_const _) ((hH'.div (hE.const_mul 2) e2).mul_const _))
    ((hH'.div (hH.const_mul 2) h2).mul_const _)

/-- **B4.** `g(R(∂_r, ∂_φ)∂_φ, ∂_r) = −h″/2 + e′h′/(4e) + h′²/(4h)` for THE Levi-Civita connection. -/
theorem diag_curv (p : ℝ × ℝ) :
    diagF e h p (curv (lcConn (ℝ × ℝ) (ndOf (diagF e h) (diagF_symm e h) (diagF_nondeg he hh)
        ((diagF_smooth hes hhs).differentiable (by simp))))
      (fun _ => ((1 : ℝ), (0 : ℝ))) (fun _ => ((0 : ℝ), (1 : ℝ))) (fun _ => ((0 : ℝ), (1 : ℝ))) p) ((1 : ℝ), (0 : ℝ))
      = -(deriv (deriv h) p.1) / 2 + deriv e p.1 * deriv h p.1 / (4 * e p.1)
        + deriv h p.1 ^ 2 / (4 * h p.1) := by
  have hn := diagF_nondeg he hh
  have hGd : Differentiable ℝ (lcGam (diagF e h)) := (lcGam_smooth hn (diagF_smooth hes hhs)).differentiable (by simp)
  have hfd : ∀ a b c : ℝ × ℝ, fderiv ℝ (fun y => lcGam (diagF e h) y a b) p c
      = c.1 • deriv (fun t => gD e h t a b) p.1 := fun a b c => by
    rw [show (fun y => lcGam (diagF e h) y a b) = fun y : ℝ × ℝ => gD e h y.1 a b from
      funext fun y => lcGam_diag he hh hes hhs y a b]
    exact fderiv_of_fst (gD_hasDerivAt he hh hes hhs p.1 a b).differentiableAt c
  rw [curv_model _ (lcGam (diagF e h)) (fun x w u => lcConn_const (diagF_symm e h) hn _ x w u) hGd,
    fderiv_apply₂ (hGd p), fderiv_apply₂ (hGd p), hfd, hfd, (gD_hasDerivAt he hh hes hhs _ _ _).deriv]
  simp only [lcGam_diag he hh hes hhs, gD, diagF_apply, zero_smul, one_smul, sub_zero, Prod.fst_add, Prod.fst_sub,
    Prod.snd_add, Prod.snd_sub]
  have := he p.1; have := hh p.1
  field_simp
  ring

open Filter Topology in
/-- **B4, receipt 34.** On the slice `dr²/f + r² dφ²` (profiles equal to `1/f`, `r²` near `r`), the Gaussian
curvature `K_G = g(R(∂_r, ∂_φ)∂_φ, ∂_r)/(g_rr g_φφ)` of THE Levi-Civita connection is `−f′(r)/(2r)`. -/
theorem slice_gauss {f : ℝ → ℝ} {p : ℝ × ℝ} (hr : p.1 ≠ 0) (hf : f p.1 ≠ 0) (hfd : DifferentiableAt ℝ f p.1)
    (he1 : e =ᶠ[𝓝 p.1] fun s => (f s)⁻¹) (hh1 : h =ᶠ[𝓝 p.1] fun s => s ^ 2) :
    diagF e h p (curv (lcConn (ℝ × ℝ) (ndOf (diagF e h) (diagF_symm e h) (diagF_nondeg he hh)
        ((diagF_smooth hes hhs).differentiable (by simp))))
      (fun _ => ((1 : ℝ), (0 : ℝ))) (fun _ => ((0 : ℝ), (1 : ℝ))) (fun _ => ((0 : ℝ), (1 : ℝ))) p) ((1 : ℝ), (0 : ℝ))
      / (e p.1 * h p.1) = -deriv f p.1 / (2 * p.1) := by
  have e1 : deriv e p.1 = -deriv f p.1 / f p.1 ^ 2 := by rw [he1.deriv_eq]; exact (hfd.hasDerivAt.inv hf).deriv
  have h1 : deriv h p.1 = 2 * p.1 := by rw [hh1.deriv_eq, (hasDerivAt_pow 2 p.1).deriv]; norm_num
  have h2 : deriv (deriv h) p.1 = 2 := by
    have : deriv (fun s : ℝ => s ^ 2) = fun s => 2 * s :=
      funext fun s => by rw [(hasDerivAt_pow 2 s).deriv]; norm_num
    rw [hh1.deriv.deriv_eq, this, ((hasDerivAt_id' p.1).const_mul 2).deriv, mul_one]
  rw [diag_curv he hh hes hhs, e1, h1, h2, he1.eq_of_nhds, hh1.eq_of_nhds]
  field_simp
  ring

end SweepB4

/-! ## `r7315`, B5 — receipt 36: on SdS, `f = 1 − 2M/r − r²/α²`, THE connection's slice curvature is
`K_G = 1/α² − M/r³`. On `K_G = 0` the mass leaves `f`, which becomes `1 − 3r²/α²`, and `K_G` and `f` vanish
together at some `r > 0` iff `27M² = α²`, the Nariai discriminant (there `r = 3M = α/√3`) -/

section SweepB5

noncomputable def fSdS (M α r : ℝ) : ℝ := 1 - 2 * M / r - r ^ 2 / α ^ 2

lemma fSdS_hasDerivAt (M α : ℝ) {r : ℝ} (hr : r ≠ 0) :
    HasDerivAt (fSdS M α) (2 * M / r ^ 2 - 2 * r / α ^ 2) r := by
  have e : fSdS M α = fun s => 1 - 2 * M * s⁻¹ - s ^ 2 / α ^ 2 := by funext s; simp only [fSdS]; ring
  rw [e]
  refine HasDerivAt.congr_deriv (HasDerivAt.sub (HasDerivAt.sub (hasDerivAt_const r (1 : ℝ))
    ((hasDerivAt_inv hr).const_mul (2 * M))) ((hasDerivAt_pow 2 r).div_const (α ^ 2))) ?_
  field_simp; ring

open Filter Topology in
/-- **B5.** THE connection's slice curvature on SdS is `1/α² − M/r³`. -/
theorem sds_slice_gauss {e h : ℝ → ℝ} (he : ∀ s, e s ≠ 0) (hh : ∀ s, h s ≠ 0) (hes : ContDiff ℝ ∞ e)
    (hhs : ContDiff ℝ ∞ h) {M α : ℝ} {p : ℝ × ℝ} (hr : p.1 ≠ 0) (hf : fSdS M α p.1 ≠ 0)
    (he1 : e =ᶠ[𝓝 p.1] fun s => (fSdS M α s)⁻¹) (hh1 : h =ᶠ[𝓝 p.1] fun s => s ^ 2) :
    diagF e h p (curv (lcConn (ℝ × ℝ) (ndOf (diagF e h) (diagF_symm e h) (diagF_nondeg he hh)
        ((diagF_smooth hes hhs).differentiable (by simp))))
      (fun _ => ((1 : ℝ), (0 : ℝ))) (fun _ => ((0 : ℝ), (1 : ℝ))) (fun _ => ((0 : ℝ), (1 : ℝ))) p) ((1 : ℝ), (0 : ℝ))
      / (e p.1 * h p.1) = 1 / α ^ 2 - M / p.1 ^ 3 := by
  rw [slice_gauss he hh hes hhs hr hf (fSdS_hasDerivAt M α hr).differentiableAt he1 hh1,
    (fSdS_hasDerivAt M α hr).deriv]
  field_simp; ring

/-- On `K_G = 0` the mass term is absorbed: `f = 1 − 3r²/α²`. -/
lemma sds_flat_locus {M α r : ℝ} (hα : α ≠ 0) (hr : r ≠ 0) (hK : 1 / α ^ 2 - M / r ^ 3 = 0) :
    fSdS M α r = 1 - 3 * r ^ 2 / α ^ 2 := by
  have hM : M = r ^ 3 / α ^ 2 := by field_simp at hK ⊢; linarith
  rw [fSdS, hM]; field_simp; ring

/-- **B5, receipt 36.** `K_G` and `f` vanish together at some `r > 0` iff `27M² = α²`. -/
theorem sds_nariai_iff {M α : ℝ} (hM : 0 < M) (hα : 0 < α) :
    (∃ r > 0, 1 / α ^ 2 - M / r ^ 3 = 0 ∧ fSdS M α r = 0) ↔ 27 * M ^ 2 = α ^ 2 := by
  constructor
  · rintro ⟨r, hr, hK, hf⟩
    rw [sds_flat_locus hα.ne' hr.ne' hK] at hf
    have hM' : M * α ^ 2 = r ^ 3 := by field_simp at hK; linarith
    have hα2 : α ^ 2 = 3 * r ^ 2 := by field_simp at hf; linarith
    have h9 : 9 * M ^ 2 * r ^ 4 = r ^ 2 * r ^ 4 := by
      linear_combination (M * α ^ 2 + r ^ 3) * hM' - M ^ 2 * (α ^ 2 + 3 * r ^ 2) * hα2
    have := mul_right_cancel₀ (pow_ne_zero 4 hr.ne') h9
    linear_combination 3 * this - hα2
  · intro h27
    refine ⟨3 * M, by positivity, ?_, ?_⟩
    · rw [← h27]; field_simp; ring
    · rw [fSdS, ← h27]; field_simp; ring

end SweepB5

/-! ## `r7315`, B6 — receipt 103: B5's slice curvature `K_G = 1/α² − M/r³` of THE connection vanishes on `r > 0`
exactly at `r_*³ = Mα²`, and the bead amplitude `A³ = 2Mα²` stands to it as `(A/r_*)³ = 2` -/

section SweepB6

/-- **B6, receipt 103.** -/
theorem sds_two_ranges {M α r A : ℝ} (hα : α ≠ 0) (hr : 0 < r) (hA : A ^ 3 = 2 * M * α ^ 2) :
    (1 / α ^ 2 - M / r ^ 3 = 0 ↔ r ^ 3 = M * α ^ 2)
    ∧ (r ^ 3 = M * α ^ 2 → (A / r) ^ 3 = 2) := by
  have hr3 : r ^ 3 ≠ 0 := pow_ne_zero 3 hr.ne'
  refine ⟨⟨fun h => ?_, fun h => ?_⟩, fun h => ?_⟩
  · field_simp at h; linarith
  · have hM : M ≠ 0 := fun h0 => hr3 (by rw [h, h0, zero_mul])
    rw [h]; field_simp; ring
  · have hM : M ≠ 0 := fun h0 => hr3 (by rw [h, h0, zero_mul])
    rw [div_pow, hA, h]; field_simp

end SweepB6

/-! ## `r7315`, B7 — receipt 32: on any member of the SdS energy family, `ṙ² = E² − f(r)`, the radial acceleration
is `r̈ = −f′/2 = r K_G`, with `K_G` THE connection's slice curvature from B5. `E` cancels -/

section SweepB7

open Filter Topology

/-- `ṙ² = E² − f(r)` near `t`, `ṙ ≠ 0` at `t`: then `r̈ = r(1/α² − M/r³)`. -/
lemma accel_rKG {r v : ℝ → ℝ} {E M α t a : ℝ} (hr : HasDerivAt r (v t) t) (hv : HasDerivAt v a t)
    (hrt : r t ≠ 0) (hvt : v t ≠ 0) (hE : ∀ᶠ s in 𝓝 t, v s ^ 2 = E ^ 2 - fSdS M α (r s)) :
    a = r t * (1 / α ^ 2 - M / r t ^ 3) := by
  have h1 : HasDerivAt (fun s => v s ^ 2) (2 * v t * a) t := by
    convert hv.pow 2 using 1; ring
  have h2 : HasDerivAt (fun s => E ^ 2 - fSdS M α (r s)) (-((2 * M / r t ^ 2 - 2 * r t / α ^ 2) * v t)) t := by
    exact HasDerivAt.congr_deriv (HasDerivAt.sub (hasDerivAt_const t (E ^ 2))
      ((fSdS_hasDerivAt M α hrt).comp t hr)) (by ring)
  have key := h1.unique (h2.congr_of_eventuallyEq hE)
  have hc : v t * (2 * a) = v t * (2 * (r t * (1 / α ^ 2 - M / r t ^ 3))) := by
    have e2 : 2 * (r t * (1 / α ^ 2 - M / r t ^ 3)) = -(2 * M / r t ^ 2 - 2 * r t / α ^ 2) := by
      field_simp; ring
    rw [e2]; linear_combination key
  linarith [mul_left_cancel₀ hvt hc]

/-- **B7, receipt 32.** `r̈ = r K_G`, with `K_G = g(R(∂_r,∂_φ)∂_φ,∂_r)/(g_rr g_φφ)` of THE Levi-Civita connection. -/
theorem sds_accel_is_rKG {e h : ℝ → ℝ} (he : ∀ s, e s ≠ 0) (hh : ∀ s, h s ≠ 0) (hes : ContDiff ℝ ∞ e)
    (hhs : ContDiff ℝ ∞ h) {r v : ℝ → ℝ} {E M α t a φ : ℝ} (hr : HasDerivAt r (v t) t) (hv : HasDerivAt v a t)
    (hrt : r t ≠ 0) (hvt : v t ≠ 0) (hE : ∀ᶠ s in 𝓝 t, v s ^ 2 = E ^ 2 - fSdS M α (r s))
    (hf : fSdS M α (r t) ≠ 0) (he1 : e =ᶠ[𝓝 (r t)] fun s => (fSdS M α s)⁻¹) (hh1 : h =ᶠ[𝓝 (r t)] fun s => s ^ 2) :
    a = r t * (diagF e h (r t, φ) (curv (lcConn (ℝ × ℝ) (ndOf (diagF e h) (diagF_symm e h) (diagF_nondeg he hh)
        ((diagF_smooth hes hhs).differentiable (by simp))))
      (fun _ => ((1 : ℝ), (0 : ℝ))) (fun _ => ((0 : ℝ), (1 : ℝ))) (fun _ => ((0 : ℝ), (1 : ℝ))) (r t, φ))
        ((1 : ℝ), (0 : ℝ)) / (e (r t) * h (r t))) := by
  rw [sds_slice_gauss he hh hes hhs (p := (r t, φ)) hrt hf he1 hh1]
  exact accel_rKG hr hv hrt hvt hE

end SweepB7

/-! ## `r7315`, B8 — receipt 38: on the energy family the radial acceleration vanishes exactly where THE
connection's slice curvature does, at the Hubble–Eddington radius `r³ = Mα²`: force balance IS the flat locus -/

section SweepB8

open Filter Topology in
/-- **B8, receipt 38.** `r̈ = 0 ↔ K_G = 0 ↔ r³ = Mα²`, for `r > 0` on any member of the family. -/
theorem sds_balance_is_flat {r v : ℝ → ℝ} {E M α t a : ℝ} (hα : α ≠ 0) (hr : HasDerivAt r (v t) t)
    (hv : HasDerivAt v a t) (hrt : 0 < r t) (hvt : v t ≠ 0)
    (hE : ∀ᶠ s in 𝓝 t, v s ^ 2 = E ^ 2 - fSdS M α (r s)) :
    (a = 0 ↔ 1 / α ^ 2 - M / r t ^ 3 = 0) ∧ (a = 0 ↔ r t ^ 3 = M * α ^ 2) := by
  have hacc := accel_rKG hr hv hrt.ne' hvt hE
  have h1 : a = 0 ↔ 1 / α ^ 2 - M / r t ^ 3 = 0 := by
    rw [hacc, mul_eq_zero, or_iff_right hrt.ne']
  refine ⟨h1, h1.trans ⟨fun h => ?_, fun h => ?_⟩⟩
  · field_simp at h; linarith
  · have hM : M ≠ 0 := fun h0 => (pow_ne_zero 3 hrt.ne') (by rw [h, h0, zero_mul])
    rw [h]; field_simp; ring

end SweepB8

/-! ## `r7315`, B9 — receipt 56: the plane wave `2 du dv + H du² + dx² + dy²`, `H = h₊(u)(x²−y²) + 2hₓ(u)xy`, in
Brinkmann coordinates on `ℝ⁴`. For THE Levi-Civita connection, `∂_v` and every `ξ_f = f^a(u)∂_a − (ḟ·x)∂_v` with
`f̈ = A f` are Killing (`∇ξ` antisymmetric); `[ξ_f, ξ_g] = W(f, g) ∂_v` with the Wronskian `W` constant; no
Killing field has a `∂_u` part, and `∂_v` is null and orthogonal to all of them: the orbits are null -/

section SweepB9

set_option synthInstance.maxHeartbeats 400000

set_option backward.isDefEq.respectTransparency false in
/-- **The Killing operator on a model space**: `g(∇_u ξ, v) + g(u, ∇_v ξ) = ξ(g(u,v)) + g(Dξ·u, v) + g(u, Dξ·v)`. -/
lemma killing_lie {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
    (m : NDMetric 𝓘(ℝ, E) E) {ξ : Π y : E, TangentSpace 𝓘(ℝ, E) y} {x : E} (hξ : DifferentiableAt ℝ (vf ξ) x)
    (u v : E) :
    m.g x (lcConn E m ξ x u) v + m.g x u (lcConn E m ξ x v)
      = fderiv ℝ (fun y => m.g y (constF u y) (constF v y)) x (vf ξ x) + m.g x (fderiv ℝ (vf ξ) x u) v
        + m.g x u (fderiv ℝ (vf ξ) x v) := by
  have hξm : MDiffAt (T% ξ) x := mdiffAt_model.2 hξ
  rw [m.symm x u, show m.g x (lcConn E m ξ x u) v = m.g x (lcConn E m ξ x (constF u x)) (constF v x) from rfl,
    show m.g x (lcConn E m ξ x v) u = m.g x (lcConn E m ξ x (constF v x)) (constF u x) from rfl,
    lcConn_apply m (constF_mdiff u x) hξm (constF_mdiff v x), lcConn_apply m (constF_mdiff v x) hξm (constF_mdiff u x)]
  have hbr : ∀ A B : Π y : E, TangentSpace 𝓘(ℝ, E) y,
      mlieBracket 𝓘(ℝ, E) A B x = fderiv ℝ (vf B) x (A x) - fderiv ℝ (vf A) x (B x) := fun A B => by
    rw [← mlieBracketWithin_univ, mlieBracketWithin_eq_lieBracketWithin, lieBracketWithin_univ]; rfl
  have hc : ∀ (a : E) (w : E), fderiv ℝ (vf (constF a)) x w = 0 := fun a w => by
    rw [show vf (constF a) = fun _ => a from rfl, fderiv_const_apply]; rfl
  have fts : ∀ w : TangentSpace 𝓘(ℝ, E) x, (NormedSpace.fromTangentSpace (𝕜 := ℝ) x : _ →L[ℝ] E) w = w :=
    fun _ => rfl
  simp only [kosz, hbr, hc, sub_zero, zero_sub, sub_self, map_zero, map_neg, mvfderiv_eq_fderiv,
    ContinuousLinearMap.comp_apply, fts]
  rw [m.fun_symm ξ (constF u), m.fun_symm ξ (constF v), m.fun_symm (constF v) (constF u)]
  have s1 := m.symm x (constF v x) (fderiv ℝ (vf ξ) x u)
  have s2 := m.symm x (constF u x) (fderiv ℝ (vf ξ) x v)
  simp only [constF] at s1 s2 ⊢
  rw [show vf ξ x = ξ x from rfl]
  linarith

/-- `H = h₊(u)(x² − y²) + 2hₓ(u)xy`, coordinates `(u, v, x, y) = (p 0, p 1, p 2, p 3)`. -/
noncomputable def Hpw (hp hx : ℝ → ℝ) (p : Fin 4 → ℝ) : ℝ :=
  hp (p 0) * (p 2 ^ 2 - p 3 ^ 2) + 2 * hx (p 0) * (p 2 * p 3)

/-- The Brinkmann form `2 du dv + H du² + dx² + dy²`. -/
noncomputable def pwF (hp hx : ℝ → ℝ) (p : Fin 4 → ℝ) : (Fin 4 → ℝ) →L[ℝ] (Fin 4 → ℝ) →L[ℝ] ℝ :=
  (ContinuousLinearMap.mul ℝ ℝ).bilinearComp (ContinuousLinearMap.proj 0) (ContinuousLinearMap.proj 1)
  + (ContinuousLinearMap.mul ℝ ℝ).bilinearComp (ContinuousLinearMap.proj 1) (ContinuousLinearMap.proj 0)
  + Hpw hp hx p • (ContinuousLinearMap.mul ℝ ℝ).bilinearComp (ContinuousLinearMap.proj 0) (ContinuousLinearMap.proj 0)
  + (ContinuousLinearMap.mul ℝ ℝ).bilinearComp (ContinuousLinearMap.proj 2) (ContinuousLinearMap.proj 2)
  + (ContinuousLinearMap.mul ℝ ℝ).bilinearComp (ContinuousLinearMap.proj 3) (ContinuousLinearMap.proj 3)

lemma pwF_apply (hp hx : ℝ → ℝ) (p a b : Fin 4 → ℝ) :
    pwF hp hx p a b = a 0 * b 1 + a 1 * b 0 + Hpw hp hx p * (a 0 * b 0) + a 2 * b 2 + a 3 * b 3 := by
  simp [pwF]

lemma pwF_symm (hp hx : ℝ → ℝ) (p a b : Fin 4 → ℝ) : pwF hp hx p a b = pwF hp hx p b a := by
  rw [pwF_apply, pwF_apply]; ring

lemma pwF_nondeg (hp hx : ℝ → ℝ) (p a : Fin 4 → ℝ) (h : ∀ b, pwF hp hx p a b = 0) : a = 0 := by
  have e0 := h (Pi.single 1 1); have e1 := h (Pi.single 0 1)
  have e2 := h (Pi.single 2 1); have e3 := h (Pi.single 3 1)
  simp [pwF_apply] at e0 e1 e2 e3
  funext i; fin_cases i <;> simp_all

lemma pwF_smooth {hp hx : ℝ → ℝ} (hps : ContDiff ℝ ∞ hp) (hxs : ContDiff ℝ ∞ hx) : ContDiff ℝ ∞ (pwF hp hx) := by
  rw [contDiff_clm_apply_iff]; intro a; rw [contDiff_clm_apply_iff]; intro b
  simp only [pwF_apply, Hpw]
  have h1 : ContDiff ℝ ∞ fun p : Fin 4 → ℝ => hp (p 0) := hps.comp (contDiff_apply ℝ ℝ 0)
  have h2 : ContDiff ℝ ∞ fun p : Fin 4 → ℝ => hx (p 0) := hxs.comp (contDiff_apply ℝ ℝ 0)
  have h3 : ∀ i : Fin 4, ContDiff ℝ ∞ fun p : Fin 4 → ℝ => p i := fun i => contDiff_apply ℝ ℝ i
  fun_prop

/-- The plane wave as an `NDMetric` on `ℝ⁴`. -/
noncomputable def pwM {hp hx : ℝ → ℝ} (hps : ContDiff ℝ ∞ hp) (hxs : ContDiff ℝ ∞ hx) :
    NDMetric 𝓘(ℝ, Fin 4 → ℝ) (Fin 4 → ℝ) :=
  ndOf (pwF hp hx) (pwF_symm hp hx) (pwF_nondeg hp hx) ((pwF_smooth hps hxs).differentiable (by simp))

/-- `ξ_f = f^a(u) ∂_a − (ḟ·x) ∂_v`. -/
noncomputable def xiPW (f1 f2 : ℝ → ℝ) : Π y : Fin 4 → ℝ, TangentSpace 𝓘(ℝ, Fin 4 → ℝ) y :=
  fun y => ![0, -(deriv f1 (y 0) * y 2 + deriv f2 (y 0) * y 3), f1 (y 0), f2 (y 0)]

lemma fd_coord {k : ℝ → ℝ} {x : Fin 4 → ℝ} (hk : DifferentiableAt ℝ k (x 0)) :
    HasFDerivAt (fun y : Fin 4 → ℝ => k (y 0)) (deriv k (x 0) • ContinuousLinearMap.proj (R := ℝ) (φ := fun _ : Fin 4 => ℝ) 0) x :=
  hk.hasDerivAt.comp_hasFDerivAt x (hasFDerivAt_apply (𝕜 := ℝ) (0 : Fin 4) x)

variable {f1 f2 : ℝ → ℝ} (h1s : ContDiff ℝ ∞ f1) (h2s : ContDiff ℝ ∞ f2)
include h1s h2s

/-- `ξ_f` is differentiable, with `Dξ·w = (0, −(f̈·x) w⁰ − ḟ·w^⊥, ḟ₁ w⁰, ḟ₂ w⁰)`. -/
lemma xiPW_deriv (x : Fin 4 → ℝ) : DifferentiableAt ℝ (vf (xiPW f1 f2)) x ∧ ∀ w : Fin 4 → ℝ,
    fderiv ℝ (vf (xiPW f1 f2)) x w = ![0, -((deriv (deriv f1) (x 0) * x 2 + deriv (deriv f2) (x 0) * x 3) * w 0
      + deriv f1 (x 0) * w 2 + deriv f2 (x 0) * w 3), deriv f1 (x 0) * w 0, deriv f2 (x 0) * w 0] := by
  have d1 := (contDiff_infty_iff_deriv.1 h1s).1; have d2 := (contDiff_infty_iff_deriv.1 h2s).1
  have d1' := ((contDiff_infty_iff_deriv.1 h1s).2).differentiable (by simp)
  have d2' := ((contDiff_infty_iff_deriv.1 h2s).2).differentiable (by simp)
  have k0 : HasFDerivAt (fun y => vf (xiPW f1 f2) y 0) (0 : (Fin 4 → ℝ) →L[ℝ] ℝ) x := hasFDerivAt_const (0 : ℝ) x
  have k1 : HasFDerivAt (fun y => vf (xiPW f1 f2) y 1) _ x :=
    (((fd_coord (d1' _)).mul (hasFDerivAt_apply (𝕜 := ℝ) (2 : Fin 4) x)).add ((fd_coord (d2' _)).mul (hasFDerivAt_apply (𝕜 := ℝ) (3 : Fin 4) x))).neg
  have k2 : HasFDerivAt (fun y => vf (xiPW f1 f2) y 2) _ x := fd_coord (d1 _)
  have k3 : HasFDerivAt (fun y => vf (xiPW f1 f2) y 3) _ x := fd_coord (d2 _)
  have hd : DifferentiableAt ℝ (vf (xiPW f1 f2)) x := by
    refine differentiableAt_pi.2 fun i => ?_
    fin_cases i
    exacts [k0.differentiableAt, k1.differentiableAt, k2.differentiableAt, k3.differentiableAt]
  refine ⟨hd, fun w => funext fun i => ?_⟩
  have D : ∀ j, fderiv ℝ (vf (xiPW f1 f2)) x w j = fderiv ℝ (fun y => vf (xiPW f1 f2) y j) x w := fun j => by
    rw [_root_.fderiv_apply hd j]; rfl
  have D0 : fderiv ℝ (vf (xiPW f1 f2)) x w 0 = 0 := by rw [D, k0.fderiv]; rfl
  have D1 : fderiv ℝ (vf (xiPW f1 f2)) x w 1 = -((deriv (deriv f1) (x 0) * x 2 + deriv (deriv f2) (x 0) * x 3) * w 0
      + deriv f1 (x 0) * w 2 + deriv f2 (x 0) * w 3) := by rw [D, k1.fderiv]; simp; ring
  have D2 : fderiv ℝ (vf (xiPW f1 f2)) x w 2 = deriv f1 (x 0) * w 0 := by rw [D, k2.fderiv]; simp
  have D3 : fderiv ℝ (vf (xiPW f1 f2)) x w 3 = deriv f2 (x 0) * w 0 := by rw [D, k3.fderiv]; simp
  fin_cases i
  exacts [D0, D1, D2, D3]

/-- **B9, receipt 56.** If `f̈ = A f`, `A = [[h₊, hₓ], [hₓ, −h₊]]`, then `ξ_f` is a Killing field of THE Levi-Civita
connection of the plane wave: `g(∇_u ξ, v) + g(u, ∇_v ξ) = 0`. -/
theorem pw_killing {hp hx : ℝ → ℝ} (hps : ContDiff ℝ ∞ hp) (hxs : ContDiff ℝ ∞ hx)
    (o1 : ∀ s, deriv (deriv f1) s = hp s * f1 s + hx s * f2 s)
    (o2 : ∀ s, deriv (deriv f2) s = hx s * f1 s - hp s * f2 s) (x u v : Fin 4 → ℝ) :
    (pwM hps hxs).g x (lcConn (Fin 4 → ℝ) (pwM hps hxs) (xiPW f1 f2) x u) v
      + (pwM hps hxs).g x u (lcConn (Fin 4 → ℝ) (pwM hps hxs) (xiPW f1 f2) x v) = 0 := by
  obtain ⟨hd, hD⟩ := xiPW_deriv h1s h2s x
  rw [killing_lie _ hd u v]
  have hG : (fun y => (pwM hps hxs).g y (constF u y) (constF v y))
      = fun y => u 0 * v 1 + u 1 * v 0 + Hpw hp hx y * (u 0 * v 0) + u 2 * v 2 + u 3 * v 3 :=
    funext fun y => pwF_apply hp hx y u v
  have dp := (hps.differentiable (by simp)) (x 0); have dx := (hxs.differentiable (by simp)) (x 0)
  have kH : HasFDerivAt (Hpw hp hx) _ x :=
    ((fd_coord dp).mul (((hasFDerivAt_apply (𝕜 := ℝ) (2 : Fin 4) x).pow 2).sub ((hasFDerivAt_apply (𝕜 := ℝ) (3 : Fin 4) x).pow 2))).add
      (((fd_coord dx).const_mul 2).mul ((hasFDerivAt_apply (𝕜 := ℝ) (2 : Fin 4) x).mul (hasFDerivAt_apply (𝕜 := ℝ) (3 : Fin 4) x)))
  have hGd := (((kH.mul_const (u 0 * v 0)).const_add (u 0 * v 1 + u 1 * v 0)).add_const (u 2 * v 2)).add_const
    (u 3 * v 3)
  rw [hG, hGd.fderiv]
  simp only [pwM, ndOf]
  erw [hD, hD, pwF_apply, pwF_apply]
  simp [xiPW, vf, o1, o2]
  ring

set_option backward.isDefEq.respectTransparency false in
/-- **B9. Heisenberg:** `[ξ_f, ξ_g] = W(f, g) ∂_v`, `W = ḟ·g − ġ·f`. -/
theorem pw_bracket {g1 g2 : ℝ → ℝ} (k1s : ContDiff ℝ ∞ g1) (k2s : ContDiff ℝ ∞ g2) (x : Fin 4 → ℝ) :
    mlieBracket 𝓘(ℝ, Fin 4 → ℝ) (xiPW f1 f2) (xiPW g1 g2) x = (deriv f1 (x 0) * g1 (x 0) + deriv f2 (x 0) * g2 (x 0)
      - deriv g1 (x 0) * f1 (x 0) - deriv g2 (x 0) * f2 (x 0)) • (Pi.single 1 1 : Fin 4 → ℝ) := by
  rw [← mlieBracketWithin_univ, mlieBracketWithin_eq_lieBracketWithin, lieBracketWithin_univ]
  show fderiv ℝ (vf (xiPW g1 g2)) x (xiPW f1 f2 x) - fderiv ℝ (vf (xiPW f1 f2)) x (xiPW g1 g2 x) = _
  rw [(xiPW_deriv k1s k2s x).2, (xiPW_deriv h1s h2s x).2]
  funext i; fin_cases i <;> simp [xiPW, Pi.single_apply] <;> ring

/-- **B9.** The Wronskian is constant when `f̈ = A f`, `g̈ = A g` with `A` symmetric. -/
theorem pw_wronskian_const {hp hx g1 g2 : ℝ → ℝ} (k1s : ContDiff ℝ ∞ g1) (k2s : ContDiff ℝ ∞ g2)
    (o1 : ∀ s, deriv (deriv f1) s = hp s * f1 s + hx s * f2 s) (o2 : ∀ s, deriv (deriv f2) s = hx s * f1 s - hp s * f2 s)
    (q1 : ∀ s, deriv (deriv g1) s = hp s * g1 s + hx s * g2 s) (q2 : ∀ s, deriv (deriv g2) s = hx s * g1 s - hp s * g2 s)
    (s : ℝ) : HasDerivAt (fun t => deriv f1 t * g1 t + deriv f2 t * g2 t - deriv g1 t * f1 t - deriv g2 t * f2 t) 0 s := by
  have D : ∀ {k : ℝ → ℝ}, ContDiff ℝ ∞ k → HasDerivAt k (deriv k s) s ∧ HasDerivAt (deriv k) (deriv (deriv k) s) s :=
    fun hk => ⟨((contDiff_infty_iff_deriv.1 hk).1 s).hasDerivAt,
      (((contDiff_infty_iff_deriv.1 hk).2.differentiable (by simp)) s).hasDerivAt⟩
  obtain ⟨a1, b1⟩ := D h1s; obtain ⟨a2, b2⟩ := D h2s; obtain ⟨c1, d1⟩ := D k1s; obtain ⟨c2, d2⟩ := D k2s
  refine HasDerivAt.congr_deriv (HasDerivAt.sub (HasDerivAt.sub (HasDerivAt.add (b1.mul c1) (b2.mul c2))
    (d1.mul a1)) (d2.mul a2)) ?_
  rw [o1, o2, q1, q2]; ring

omit h1s h2s in
/-- **B9, the `∂_v` generator and the null orbits.** `∂_v` is Killing; no `ξ_f` has a `∂_u` part; `∂_v` is null and
orthogonal to every `ξ_f`. -/
theorem pw_dv_null {hp hx : ℝ → ℝ} (hps : ContDiff ℝ ∞ hp) (hxs : ContDiff ℝ ∞ hx) (x u v : Fin 4 → ℝ) :
    ((pwM hps hxs).g x (lcConn (Fin 4 → ℝ) (pwM hps hxs) (constF (Pi.single 1 1)) x u) v
      + (pwM hps hxs).g x u (lcConn (Fin 4 → ℝ) (pwM hps hxs) (constF (Pi.single 1 1)) x v) = 0)
    ∧ (xiPW f1 f2 x : Fin 4 → ℝ) 0 = 0 ∧ (pwM hps hxs).g x (Pi.single 1 1) (Pi.single 1 1) = 0
    ∧ (pwM hps hxs).g x (Pi.single 1 1) (xiPW f1 f2 x) = 0 := by
  refine ⟨killing_of_invariant _ (fun y t => ?_) x u v, rfl, ?_, ?_⟩
  · show pwF hp hx (y + t • Pi.single 1 1) = pwF hp hx y
    simp [pwF, Hpw, Pi.single_apply]
  · show pwF hp hx x _ _ = 0; simp [pwF_apply]
  · show pwF hp hx x _ _ = 0; simp [pwF_apply, xiPW]

end SweepB9

/-! ## `r7315`, B10 — receipt 44: the equatorial chart `(t, r, φ)` on `ℝ³` with a diagonal metric `Σ cₖ(r) dxₖ²`.
THE connection's geodesic equation, radial part, on a null velocity of energy `E` and angular momentum `L` around
SdS (`c = (−f, 1/f, r²)`), is `r̈ = −(L²/2)(f/r²)′`. At the photon sphere `r = 3M` the Lyapunov exponent
`λ² = −(r²f/2)(f/r²)″` equals `Ω² = f/r²`: `λ = Ω_c` in four dimensions -/

section SweepB10

set_option synthInstance.maxHeartbeats 400000

/-- A diagonal form on `ℝ³` with coefficients depending on `r = p 1`. -/
noncomputable def diag3F (c : Fin 3 → ℝ → ℝ) (p : Fin 3 → ℝ) : (Fin 3 → ℝ) →L[ℝ] (Fin 3 → ℝ) →L[ℝ] ℝ :=
  ∑ i, c i (p 1) • (ContinuousLinearMap.mul ℝ ℝ).bilinearComp (ContinuousLinearMap.proj i) (ContinuousLinearMap.proj i)

lemma diag3F_apply (c : Fin 3 → ℝ → ℝ) (p a b : Fin 3 → ℝ) : diag3F c p a b = ∑ i, c i (p 1) * (a i * b i) := by
  simp [diag3F]

lemma diag3F_symm (c : Fin 3 → ℝ → ℝ) (p a b : Fin 3 → ℝ) : diag3F c p a b = diag3F c p b a := by
  rw [diag3F_apply, diag3F_apply]; exact Finset.sum_congr rfl fun i _ => by ring

lemma diag3F_nondeg {c : Fin 3 → ℝ → ℝ} (hc : ∀ i s, c i s ≠ 0) (p a : Fin 3 → ℝ) (h : ∀ b, diag3F c p a b = 0) :
    a = 0 := by
  funext j
  have hj := h (Pi.single j 1)
  rw [diag3F_apply, Finset.sum_eq_single j (fun i _ hi => by simp [Pi.single_apply, hi]) (by simp)] at hj
  simpa [hc j] using hj

/-- The explicit Christoffel form: `Γ(a,b)ₖ = (cₖ′(a_r bₖ + aₖ b_r) − δₖᵣ Σⱼ cⱼ′ aⱼ bⱼ) / (2cₖ)`. -/
noncomputable def gam3 (c : Fin 3 → ℝ → ℝ) (s : ℝ) (a b : Fin 3 → ℝ) : Fin 3 → ℝ := fun k =>
  (deriv (c k) s * (a 1 * b k + a k * b 1) - if k = 1 then ∑ j, deriv (c j) s * (a j * b j) else 0) / (2 * c k s)

/-- `fderiv_apply₂` on any domain. -/
lemma fderiv_apply₂' {E F : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F]
    {Φ : E → (E →L[ℝ] E →L[ℝ] F)} {p : E} (hΦ : DifferentiableAt ℝ Φ p) (e a b : E) :
    fderiv ℝ Φ p e a b = fderiv ℝ (fun y => Φ y a b) p e := by
  rw [fderiv_clm_apply (hΦ.clm_apply (differentiableAt_const a)) (differentiableAt_const b),
    fderiv_clm_apply hΦ (differentiableAt_const a)]
  simp

variable {c : Fin 3 → ℝ → ℝ} (hc : ∀ i s, c i s ≠ 0) (hcs : ∀ i, ContDiff ℝ ∞ (c i))
include hc hcs

lemma diag3F_smooth : ContDiff ℝ ∞ (diag3F c) := by
  rw [contDiff_clm_apply_iff]; intro a; rw [contDiff_clm_apply_iff]; intro b
  simp only [diag3F_apply]
  exact ContDiff.sum fun i _ => ((hcs i).comp (contDiff_apply ℝ ℝ 1)).mul contDiff_const

/-- **B10, the Christoffel form:** `lcGam` of `Σ cₖ(r) dxₖ²` is `gam3`. -/
lemma lcGam_diag3 (p a b : Fin 3 → ℝ) : lcGam (diag3F c) p a b = gam3 c (p 1) a b := by
  have inv := flat_isInvertible (diag3F c) (diag3F_nondeg hc) p
  have hd : ∀ i, DifferentiableAt ℝ (c i) (p 1) := fun i => ((hcs i).differentiable (by simp)) _
  have hD : ∀ e a b : Fin 3 → ℝ, fderiv ℝ (diag3F c) p e a b = e 1 * ∑ i, deriv (c i) (p 1) * (a i * b i) :=
    fun e a b => by
    rw [fderiv_apply₂' ((diag3F_smooth hc hcs).differentiable (by simp) p),
      show (fun y => diag3F c y a b) = fun y => ∑ i, c i (y 1) * (a i * b i) from funext fun y => diag3F_apply c y a b]
    have hF : HasFDerivAt (fun y : Fin 3 → ℝ => ∑ i, c i (y 1) * (a i * b i))
        (∑ i, (a i * b i) • deriv (c i) (p 1) • ContinuousLinearMap.proj (R := ℝ) (φ := fun _ : Fin 3 => ℝ) 1) p :=
      HasFDerivAt.fun_sum fun i _ => ((hd i).hasDerivAt.comp_hasFDerivAt p
        (hasFDerivAt_apply (𝕜 := ℝ) (1 : Fin 3) p)).mul_const (a i * b i)
    rw [hF.fderiv]; simp [Finset.mul_sum]; exact Finset.sum_congr rfl fun i _ => by ring
  have hK : koszK (diag3F c) p a b = diag3F c p (gam3 c (p 1) a b) := by
    refine ContinuousLinearMap.ext fun v => ?_
    rw [koszK_apply, hD, hD, hD, diag3F_apply]
    simp only [gam3, Fin.sum_univ_three]
    have := hc 0 (p 1); have := hc 1 (p 1); have := hc 2 (p 1)
    simp
    field_simp; ring
  rw [lcGam_apply, hK, inv.inverse_apply_self]

open Filter Topology in
/-- **B10.** THE connection's geodesic acceleration, radial part, on a null velocity `(E/f, ṙ, L/r²)` around SdS-type
profiles `c = (−f, 1/f, r²)`: `−Γ(γ̇, γ̇)_r = −(L²/2)(f/r²)′`. -/
theorem null_radial {f : ℝ → ℝ} {p : Fin 3 → ℝ} {E L rd : ℝ} (hr : p 1 ≠ 0) (hf : f (p 1) ≠ 0)
    (hfd : DifferentiableAt ℝ f (p 1)) (e0 : c 0 =ᶠ[𝓝 (p 1)] fun s => -f s) (e1 : c 1 =ᶠ[𝓝 (p 1)] fun s => (f s)⁻¹)
    (e2 : c 2 =ᶠ[𝓝 (p 1)] fun s => s ^ 2) (hnull : rd ^ 2 = E ^ 2 - f (p 1) * L ^ 2 / p 1 ^ 2) :
    -(lcConn (Fin 3 → ℝ) (ndOf (diag3F c) (diag3F_symm c) (diag3F_nondeg hc)
        ((diag3F_smooth hc hcs).differentiable (by simp))) (fun _ => ![E / f (p 1), rd, L / p 1 ^ 2]) p
        ![E / f (p 1), rd, L / p 1 ^ 2]) 1
      = -(L ^ 2 / 2) * (deriv f (p 1) / p 1 ^ 2 - 2 * f (p 1) / p 1 ^ 3) := by
  rw [lcConn_const (diag3F_symm c) (diag3F_nondeg hc), lcGam_diag3 hc hcs]
  have d0 : deriv (c 0) (p 1) = -deriv f (p 1) := by rw [e0.deriv_eq]; exact hfd.hasDerivAt.neg.deriv
  have d1 : deriv (c 1) (p 1) = -deriv f (p 1) / f (p 1) ^ 2 := by
    rw [e1.deriv_eq]; exact (hfd.hasDerivAt.inv hf).deriv
  have d2 : deriv (c 2) (p 1) = 2 * p 1 := by rw [e2.deriv_eq, (hasDerivAt_pow 2 _).deriv]; norm_num
  simp [gam3, Fin.sum_univ_three, d0, d1, d2, e1.eq_of_nhds]
  have hn' : rd ^ 2 * p 1 ^ 2 = E ^ 2 * p 1 ^ 2 - f (p 1) * L ^ 2 := by rw [hnull]; field_simp
  field_simp
  linear_combination (-(deriv f (p 1) * p 1)) * hn'

omit hc hcs

lemma sdsV_hasDerivAt {M α r : ℝ} (hr : r ≠ 0) :
    HasDerivAt (fun s => fSdS M α s / s ^ 2) (-2 / r ^ 3 + 6 * M / r ^ 4) r :=
  HasDerivAt.congr_deriv ((fSdS_hasDerivAt M α hr).div (hasDerivAt_pow 2 r) (pow_ne_zero 2 hr)) (by
    unfold fSdS; field_simp; ring)

lemma sdsW_hasDerivAt {M r : ℝ} (hr : r ≠ 0) :
    HasDerivAt (fun s => -2 / s ^ 3 + 6 * M / s ^ 4) (6 / r ^ 4 - 24 * M / r ^ 5) r :=
  HasDerivAt.congr_deriv (HasDerivAt.add ((hasDerivAt_const r (-2 : ℝ)).div (hasDerivAt_pow 3 r) (pow_ne_zero 3 hr))
    ((hasDerivAt_const r (6 * M)).div (hasDerivAt_pow 4 r) (pow_ne_zero 4 hr))) (by field_simp; ring)

open Filter Topology in
/-- **B10, receipt 44.** On SdS the radial potential `(f/r²)` is stationary at `r = 3M` (the photon sphere), and
there the Lyapunov exponent `λ² = −(r²f/2)(f/r²)″` equals `Ω² = f/r²`. -/
theorem sds_photon_lyapunov {M α : ℝ} (hM : M ≠ 0) :
    deriv (fun s => fSdS M α s / s ^ 2) (3 * M) = 0
    ∧ -((3 * M) ^ 2 * fSdS M α (3 * M) / 2) * deriv (deriv fun s => fSdS M α s / s ^ 2) (3 * M)
      = fSdS M α (3 * M) / (3 * M) ^ 2 := by
  have h3 : (3 * M) ≠ 0 := mul_ne_zero three_ne_zero hM
  have hev : deriv (fun s => fSdS M α s / s ^ 2) =ᶠ[𝓝 (3 * M)] fun s => -2 / s ^ 3 + 6 * M / s ^ 4 :=
    (eventually_ne_nhds h3).mono fun s hs => (sdsV_hasDerivAt hs).deriv
  refine ⟨by rw [(sdsV_hasDerivAt h3).deriv]; field_simp; ring, ?_⟩
  rw [hev.deriv_eq, (sdsW_hasDerivAt h3).deriv]
  field_simp; ring

end SweepB10

/-! ## `r7315`, B11 — receipt 78: the pp-wave `2 du dv + H du² + dx² + dy²` for ANY smooth `H(u, x, y)`. THE
connection's Ricci contraction is `Ric(a, b) = −½(H_xx + H_yy) a⁰ b⁰`; for `H = h₊(x²−y²) + 2hₓxy` it VANISHES
for any `h₊(u), hₓ(u)`, while `g(R(∂_u, ∂_x)∂_u, ∂_x) = ½H_xx = h₊ ≠ 0`; a trace part `h(x²+y²)` gives
`Ric(∂_u, ∂_u) = −2h ≠ 0` (the control) -/

section SweepB11

set_option synthInstance.maxHeartbeats 400000

/-- The pp-wave form, any profile `H`. -/
noncomputable def ppF (H : (Fin 4 → ℝ) → ℝ) (p : Fin 4 → ℝ) : (Fin 4 → ℝ) →L[ℝ] (Fin 4 → ℝ) →L[ℝ] ℝ :=
  (ContinuousLinearMap.mul ℝ ℝ).bilinearComp (ContinuousLinearMap.proj 0) (ContinuousLinearMap.proj 1)
  + (ContinuousLinearMap.mul ℝ ℝ).bilinearComp (ContinuousLinearMap.proj 1) (ContinuousLinearMap.proj 0)
  + H p • (ContinuousLinearMap.mul ℝ ℝ).bilinearComp (ContinuousLinearMap.proj 0) (ContinuousLinearMap.proj 0)
  + (ContinuousLinearMap.mul ℝ ℝ).bilinearComp (ContinuousLinearMap.proj 2) (ContinuousLinearMap.proj 2)
  + (ContinuousLinearMap.mul ℝ ℝ).bilinearComp (ContinuousLinearMap.proj 3) (ContinuousLinearMap.proj 3)

lemma pwF_eq_ppF (hp hx : ℝ → ℝ) : pwF hp hx = ppF (Hpw hp hx) := rfl

lemma ppF_apply (H : (Fin 4 → ℝ) → ℝ) (p a b : Fin 4 → ℝ) :
    ppF H p a b = a 0 * b 1 + a 1 * b 0 + H p * (a 0 * b 0) + a 2 * b 2 + a 3 * b 3 := by
  simp [ppF]

lemma ppF_symm (H : (Fin 4 → ℝ) → ℝ) (p a b : Fin 4 → ℝ) : ppF H p a b = ppF H p b a := by
  rw [ppF_apply, ppF_apply]; ring

lemma ppF_nondeg (H : (Fin 4 → ℝ) → ℝ) (p a : Fin 4 → ℝ) (h : ∀ b, ppF H p a b = 0) : a = 0 := by
  have e0 := h (Pi.single 1 1); have e1 := h (Pi.single 0 1)
  have e2 := h (Pi.single 2 1); have e3 := h (Pi.single 3 1)
  simp [ppF_apply] at e0 e1 e2 e3
  funext i; fin_cases i <;> simp_all

/-- `∂ⱼH` and `∂ᵢ∂ⱼH`. -/
noncomputable def dH (H : (Fin 4 → ℝ) → ℝ) (p : Fin 4 → ℝ) (j : Fin 4) : ℝ := fderiv ℝ H p (Pi.single j 1)
noncomputable def ddH (H : (Fin 4 → ℝ) → ℝ) (p : Fin 4 → ℝ) (i j : Fin 4) : ℝ :=
  fderiv ℝ (fderiv ℝ H) p (Pi.single i 1) (Pi.single j 1)

/-- The pp-wave Christoffel form. -/
noncomputable def gPP (H : (Fin 4 → ℝ) → ℝ) (p a b : Fin 4 → ℝ) : Fin 4 → ℝ :=
  ![0, (dH H p 0 * (a 0 * b 0) + dH H p 2 * (a 0 * b 2 + a 2 * b 0) + dH H p 3 * (a 0 * b 3 + a 3 * b 0)) / 2,
    -(dH H p 2 * (a 0 * b 0)) / 2, -(dH H p 3 * (a 0 * b 0)) / 2]

variable {H : (Fin 4 → ℝ) → ℝ} (hH : ContDiff ℝ ∞ H) (hv : ∀ p, dH H p 1 = 0)
include hH

lemma ppF_smooth : ContDiff ℝ ∞ (ppF H) := by
  rw [contDiff_clm_apply_iff]; intro a; rw [contDiff_clm_apply_iff]; intro b
  simp only [ppF_apply]; fun_prop

include hv

lemma dH_lin (p a : Fin 4 → ℝ) : fderiv ℝ H p a = a 0 * dH H p 0 + a 2 * dH H p 2 + a 3 * dH H p 3 := by
  have e : a = ∑ j, a j • (Pi.single j 1 : Fin 4 → ℝ) := by ext i; simp [Pi.single_apply]
  have h1 := hv p; simp only [dH] at h1 ⊢
  conv_lhs => rw [e]
  simp [Fin.sum_univ_four, h1]

/-- **B11, the Christoffel form:** `lcGam` of the pp-wave is `gPP`. -/
lemma lcGam_pp (p a b : Fin 4 → ℝ) : lcGam (ppF H) p a b = gPP H p a b := by
  have inv := flat_isInvertible (ppF H) (ppF_nondeg H) p
  have hD : ∀ e a b : Fin 4 → ℝ, fderiv ℝ (ppF H) p e a b = fderiv ℝ H p e * (a 0 * b 0) := fun e a b => by
    rw [fderiv_apply₂' ((ppF_smooth hH).differentiable (by simp) p),
      show (fun y => ppF H y a b) = fun y => a 0 * b 1 + a 1 * b 0 + H y * (a 0 * b 0) + a 2 * b 2 + a 3 * b 3 from
        funext fun y => ppF_apply H y a b]
    have h := ((((hH.differentiable (by simp)) p).hasFDerivAt.mul_const (a 0 * b 0)).const_add
      (a 0 * b 1 + a 1 * b 0)).add_const (a 2 * b 2) |>.add_const (a 3 * b 3)
    rw [h.fderiv]; simp; ring
  have hK : koszK (ppF H) p a b = ppF H p (gPP H p a b) := by
    refine ContinuousLinearMap.ext fun w => ?_
    rw [koszK_apply, hD, hD, hD, dH_lin hH hv, dH_lin hH hv, dH_lin hH hv, ppF_apply]
    simp [gPP]; ring
  rw [lcGam_apply, hK, inv.inverse_apply_self]

omit hv in
lemma dH_hasFDerivAt (p : Fin 4 → ℝ) (j : Fin 4) :
    HasFDerivAt (fun y => dH H y j) ((fderiv ℝ (fderiv ℝ H) p).flip (Pi.single j 1)) p := by
  have h2 := (hH.fderiv_right (m := ∞) (by simp)).differentiable (by simp) p
  exact (h2.hasFDerivAt.clm_apply (hasFDerivAt_const (Pi.single j 1 : Fin 4 → ℝ) p)).congr_fderiv (by ext; simp)

omit hv in
/-- `gPP` differentiated, with `Dⱼ e = ∂_e ∂ⱼ H`. -/
lemma gPP_deriv (p a b : Fin 4 → ℝ) : DifferentiableAt ℝ (fun y => gPP H y a b) p ∧ ∀ e : Fin 4 → ℝ,
    fderiv ℝ (fun y => gPP H y a b) p e = ![0, (fderiv ℝ (fderiv ℝ H) p e (Pi.single 0 1) * (a 0 * b 0)
      + fderiv ℝ (fderiv ℝ H) p e (Pi.single 2 1) * (a 0 * b 2 + a 2 * b 0)
      + fderiv ℝ (fderiv ℝ H) p e (Pi.single 3 1) * (a 0 * b 3 + a 3 * b 0)) / 2,
      -(fderiv ℝ (fderiv ℝ H) p e (Pi.single 2 1) * (a 0 * b 0)) / 2,
      -(fderiv ℝ (fderiv ℝ H) p e (Pi.single 3 1) * (a 0 * b 0)) / 2] := by
  have k0 : HasFDerivAt (fun y => gPP H y a b 0) (0 : (Fin 4 → ℝ) →L[ℝ] ℝ) p := hasFDerivAt_const (0 : ℝ) p
  have k1 : HasFDerivAt (fun y => gPP H y a b 1) _ p := HasFDerivAt.mul_const (HasFDerivAt.add (HasFDerivAt.add
    ((dH_hasFDerivAt hH p 0).mul_const (a 0 * b 0)) ((dH_hasFDerivAt hH p 2).mul_const (a 0 * b 2 + a 2 * b 0)))
    ((dH_hasFDerivAt hH p 3).mul_const (a 0 * b 3 + a 3 * b 0))) (2⁻¹ : ℝ)
  have k2 : HasFDerivAt (fun y => gPP H y a b 2) _ p :=
    HasFDerivAt.mul_const (HasFDerivAt.neg ((dH_hasFDerivAt hH p 2).mul_const (a 0 * b 0))) (2⁻¹ : ℝ)
  have k3 : HasFDerivAt (fun y => gPP H y a b 3) _ p :=
    HasFDerivAt.mul_const (HasFDerivAt.neg ((dH_hasFDerivAt hH p 3).mul_const (a 0 * b 0))) (2⁻¹ : ℝ)
  have hd : DifferentiableAt ℝ (fun y => gPP H y a b) p := by
    refine differentiableAt_pi.2 fun i => ?_
    fin_cases i
    exacts [k0.differentiableAt, k1.differentiableAt, k2.differentiableAt, k3.differentiableAt]
  refine ⟨hd, fun e => funext fun i => ?_⟩
  have D : ∀ j, fderiv ℝ (fun y => gPP H y a b) p e j = fderiv ℝ (fun y => gPP H y a b j) p e := fun j => by
    rw [_root_.fderiv_apply hd j]; rfl
  have D0 := (D 0).trans (by rw [k0.fderiv])
  have D1 := (D 1).trans (by rw [k1.fderiv])
  have D2 := (D 2).trans (by rw [k2.fderiv])
  have D3 := (D 3).trans (by rw [k3.fderiv])
  fin_cases i
  · exact D0
  · exact D1.trans (by simp; ring)
  · exact D2.trans (by simp; ring)
  · exact D3.trans (by simp; ring)

/-- **B11.** THE connection's Ricci contraction on the pp-wave: `Σᵢ (R(eᵢ, a)b)ⁱ = −½(H_xx + H_yy) a⁰ b⁰`. -/
theorem pp_ricci (p a b : Fin 4 → ℝ) :
    ∑ i, curv (lcConn (Fin 4 → ℝ) (ndOf (ppF H) (ppF_symm H) (ppF_nondeg H) ((ppF_smooth hH).differentiable (by simp))))
      (fun _ => (Pi.single i 1 : Fin 4 → ℝ)) (fun _ => a) (fun _ => b) p i
      = -(ddH H p 2 2 + ddH H p 3 3) / 2 * (a 0 * b 0) := by
  have hGd : Differentiable ℝ (lcGam (ppF H)) :=
    (lcGam_smooth (ppF_nondeg H) (ppF_smooth hH)).differentiable (by simp)
  have hF : ∀ e c d, fderiv ℝ (lcGam (ppF H)) p e c d = fderiv ℝ (fun y => gPP H y c d) p e := fun e c d => by
    rw [fderiv_apply₂' (hGd p), show (fun y => lcGam (ppF H) y c d) = fun y => gPP H y c d from
      funext fun y => lcGam_pp hH hv y c d]
  have hsym : ∀ j : Fin 4, fderiv ℝ (fderiv ℝ H) p (Pi.single 1 1) (Pi.single j 1) = 0 := fun j => by
    rw [(hH.contDiffAt.isSymmSndFDerivAt (by simp)) _ _]
    have h0 : HasFDerivAt (fun y => dH H y 1) (0 : (Fin 4 → ℝ) →L[ℝ] ℝ) p := by
      rw [show (fun y => dH H y 1) = fun _ => 0 from funext hv]; exact hasFDerivAt_const _ _
    simpa using congrArg (fun L => L (Pi.single j 1 : Fin 4 → ℝ)) ((dH_hasFDerivAt hH p 1).unique h0)
  simp only [Fin.sum_univ_four, curv_model _ _ (fun x w u => lcConn_const (ppF_symm H) (ppF_nondeg H) _ x w u) hGd,
    hF, (gPP_deriv hH _ _ _).2, lcGam_pp hH hv]
  simp [gPP, hsym, ddH]
  ring

omit hv in
/-- Second partials read off any explicit derivative of `∂ⱼH`. -/
lemma ddH_of {p : Fin 4 → ℝ} {j : Fin 4} {φ : (Fin 4 → ℝ) → ℝ} {L : (Fin 4 → ℝ) →L[ℝ] ℝ} (hφ : ∀ y, dH H y j = φ y)
    (hL : HasFDerivAt φ L p) (i : Fin 4) : ddH H p i j = L (Pi.single i 1) := by
  have := (dH_hasFDerivAt hH p j).unique (by rw [show (fun y => dH H y j) = φ from funext hφ]; exact hL)
  simpa [ddH] using congrArg (fun M => M (Pi.single i 1 : Fin 4 → ℝ)) this

end SweepB11

lemma Hpw_smooth {hp hx : ℝ → ℝ} (hps : ContDiff ℝ ∞ hp) (hxs : ContDiff ℝ ∞ hx) : ContDiff ℝ ∞ (Hpw hp hx) := by
  unfold Hpw; have := hps.comp (contDiff_apply ℝ ℝ (0 : Fin 4)); have := hxs.comp (contDiff_apply ℝ ℝ (0 : Fin 4))
  fun_prop

/-- **B11, receipt 78.** The polarized wave `H = h₊(u)(x²−y²) + 2hₓ(u)xy` is Ricci-flat for THE Levi-Civita
connection, for ANY smooth `h₊, hₓ`. -/
theorem pw_ricci_flat {hp hx : ℝ → ℝ} (hps : ContDiff ℝ ∞ hp) (hxs : ContDiff ℝ ∞ hx) (p a b : Fin 4 → ℝ) :
    ∑ i, curv (lcConn (Fin 4 → ℝ) (ndOf (ppF (Hpw hp hx)) (ppF_symm _) (ppF_nondeg _)
        ((ppF_smooth (Hpw_smooth hps hxs)).differentiable (by simp))))
      (fun _ => (Pi.single i 1 : Fin 4 → ℝ)) (fun _ => a) (fun _ => b) p i = 0 := by
  have hH := Hpw_smooth hps hxs
  have dp : ∀ y : Fin 4 → ℝ, DifferentiableAt ℝ hp (y 0) := fun y => (hps.differentiable (by simp)) _
  have dx : ∀ y : Fin 4 → ℝ, DifferentiableAt ℝ hx (y 0) := fun y => (hxs.differentiable (by simp)) _
  have c : ∀ (i : Fin 4) (y : Fin 4 → ℝ), HasFDerivAt (fun z : Fin 4 → ℝ => z i) _ y :=
    fun i y => hasFDerivAt_apply (𝕜 := ℝ) i y
  have kH : ∀ y, HasFDerivAt (Hpw hp hx) _ y := fun y =>
    ((fd_coord (dp y)).mul (((c 2 y).pow 2).sub ((c 3 y).pow 2))).add
      (((fd_coord (dx y)).const_mul 2).mul ((c 2 y).mul (c 3 y)))
  have d1 : ∀ y, dH (Hpw hp hx) y 1 = 0 := fun y => by rw [dH, (kH y).fderiv]; simp
  have d2 : ∀ y, dH (Hpw hp hx) y 2 = 2 * hp (y 0) * y 2 + 2 * hx (y 0) * y 3 := fun y => by
    rw [dH, (kH y).fderiv]; simp; ring
  have d3 : ∀ y, dH (Hpw hp hx) y 3 = -(2 * hp (y 0) * y 3) + 2 * hx (y 0) * y 2 := fun y => by
    rw [dH, (kH y).fderiv]; simp; ring
  rw [pp_ricci hH d1, ddH_of hH d2 ((((fd_coord (dp p)).const_mul 2).mul (c 2 p)).add
      (((fd_coord (dx p)).const_mul 2).mul (c 3 p))),
    ddH_of hH d3 ((((fd_coord (dp p)).const_mul 2).mul (c 3 p)).neg.add (((fd_coord (dx p)).const_mul 2).mul (c 2 p)))]
  simp



/-! ## `r7315`, B12 — receipt 55: on the pp-wave, THE connection is vacuum iff `H_xx + H_yy = 0`; its Riemann
form is `g(R(a,b)c, d) = P(a,b,c,d)` in closed form; `g(R(∂_u,∂_x)∂_u,∂_x) = ½H_xx` is nonzero for a nontrivial wave
while the Kretschmann contraction `R_abcd R^abcd` (raised through the `g`-dual basis) VANISHES: Petrov type N -/

section SweepB12

set_option synthInstance.maxHeartbeats 400000

variable {H : (Fin 4 → ℝ) → ℝ} (hH : ContDiff ℝ ∞ H) (hv : ∀ p, dH H p 1 = 0)
include hH hv

/-- The pp-wave as an `NDMetric`. -/
noncomputable abbrev ppM : NDMetric 𝓘(ℝ, Fin 4 → ℝ) (Fin 4 → ℝ) :=
  ndOf (ppF H) (ppF_symm H) (ppF_nondeg H) ((ppF_smooth hH).differentiable (by simp))

/-- **B12.** Vacuum iff harmonic. -/
theorem pp_vacuum_iff (p : Fin 4 → ℝ) :
    (∀ a b, ∑ i, curv (lcConn (Fin 4 → ℝ) (ppM hH)) (fun _ => (Pi.single i 1 : Fin 4 → ℝ)) (fun _ => a)
      (fun _ => b) p i = 0) ↔ ddH H p 2 2 + ddH H p 3 3 = 0 := by
  simp only [pp_ricci hH hv]
  refine ⟨fun h => ?_, fun h a b => by rw [h]; ring⟩
  have := h (Pi.single 0 1) (Pi.single 0 1); simp at this; linarith

/-- **B12, the Riemann form in closed form**, `Aⱼ = ∂_a∂ⱼH`, `Bⱼ = ∂_b∂ⱼH`. -/
theorem pp_riemann (p a b c d : Fin 4 → ℝ) :
    ppF H p (curv (lcConn (Fin 4 → ℝ) (ppM hH)) (fun _ => a) (fun _ => b) (fun _ => c) p) d
      = (fderiv ℝ (fderiv ℝ H) p a (Pi.single 0 1) * (b 0 * c 0)
          + fderiv ℝ (fderiv ℝ H) p a (Pi.single 2 1) * (b 0 * c 2 + b 2 * c 0)
          + fderiv ℝ (fderiv ℝ H) p a (Pi.single 3 1) * (b 0 * c 3 + b 3 * c 0)
          - fderiv ℝ (fderiv ℝ H) p b (Pi.single 0 1) * (a 0 * c 0)
          - fderiv ℝ (fderiv ℝ H) p b (Pi.single 2 1) * (a 0 * c 2 + a 2 * c 0)
          - fderiv ℝ (fderiv ℝ H) p b (Pi.single 3 1) * (a 0 * c 3 + a 3 * c 0)) / 2 * d 0
        - (fderiv ℝ (fderiv ℝ H) p a (Pi.single 2 1) * b 0 - fderiv ℝ (fderiv ℝ H) p b (Pi.single 2 1) * a 0)
          * c 0 / 2 * d 2
        - (fderiv ℝ (fderiv ℝ H) p a (Pi.single 3 1) * b 0 - fderiv ℝ (fderiv ℝ H) p b (Pi.single 3 1) * a 0)
          * c 0 / 2 * d 3 := by
  have hGd : Differentiable ℝ (lcGam (ppF H)) :=
    (lcGam_smooth (ppF_nondeg H) (ppF_smooth hH)).differentiable (by simp)
  have hF : ∀ e c d, fderiv ℝ (lcGam (ppF H)) p e c d = fderiv ℝ (fun y => gPP H y c d) p e := fun e c d => by
    rw [fderiv_apply₂' (hGd p), show (fun y => lcGam (ppF H) y c d) = fun y => gPP H y c d from
      funext fun y => lcGam_pp hH hv y c d]
  rw [curv_model _ _ (fun x w u => lcConn_const (ppF_symm H) (ppF_nondeg H) _ x w u) hGd, hF, hF,
    (gPP_deriv hH _ _ _).2, (gPP_deriv hH _ _ _).2, lcGam_pp hH hv, lcGam_pp hH hv, lcGam_pp hH hv, lcGam_pp hH hv,
    ppF_apply]
  simp [gPP]; ring

/-- **B12.** `g(R(∂_u, ∂_x)∂_u, ∂_x) = ½ H_xx`: nonzero Riemann (= Weyl in vacuum) when `H_xx ≠ 0`. -/
theorem pp_Ruxux (p : Fin 4 → ℝ) :
    ppF H p (curv (lcConn (Fin 4 → ℝ) (ppM hH)) (fun _ => (Pi.single 0 1 : Fin 4 → ℝ))
      (fun _ => (Pi.single 2 1 : Fin 4 → ℝ)) (fun _ => (Pi.single 0 1 : Fin 4 → ℝ)) p) (Pi.single 2 1)
      = ddH H p 2 2 / 2 := by
  rw [pp_riemann hH hv]; simp [ddH]; ring

/-- The `g`-dual basis: `ê₀ = ∂_v`, `ê₁ = ∂_u − H ∂_v`, `ê₂ = ∂_x`, `ê₃ = ∂_y`. -/
noncomputable def ppDual (H : (Fin 4 → ℝ) → ℝ) (p : Fin 4 → ℝ) (i : Fin 4) : Fin 4 → ℝ :=
  ![Pi.single 1 1, Pi.single 0 1 - H p • Pi.single 1 1, Pi.single 2 1, Pi.single 3 1] i

omit hH hv in
lemma ppDual_dual (H : (Fin 4 → ℝ) → ℝ) (p : Fin 4 → ℝ) (i j : Fin 4) :
    ppF H p (ppDual H p i) (Pi.single j 1) = if i = j then 1 else 0 := by
  fin_cases i <;> fin_cases j <;> simp [ppDual, ppF_apply]

/-- **B12, VSI.** The Kretschmann contraction `Σ R(eᵢ,eⱼ,eₖ,eₗ) R(êᵢ,êⱼ,êₖ,êₗ)` vanishes. -/
theorem pp_kretschmann (p : Fin 4 → ℝ) :
    ∑ i, ∑ j, ∑ k, ∑ l,
      ppF H p (curv (lcConn (Fin 4 → ℝ) (ppM hH)) (fun _ => (Pi.single i 1 : Fin 4 → ℝ))
        (fun _ => (Pi.single j 1 : Fin 4 → ℝ)) (fun _ => (Pi.single k 1 : Fin 4 → ℝ)) p) (Pi.single l 1)
      * ppF H p (curv (lcConn (Fin 4 → ℝ) (ppM hH)) (fun _ => ppDual H p i) (fun _ => ppDual H p j)
        (fun _ => ppDual H p k) p) (ppDual H p l) = 0 := by
  simp only [pp_riemann hH hv]
  simp [Fin.sum_univ_four, ppDual]

end SweepB12

/-! ## `r7315`, B13 — receipt 8: a 4D engine (THE connection's Christoffel form for ANY diagonal metric on `ℝ⁴`, and
`□φ` as the trace of its Hessian), then de Sitter in conformal time, `a(η)²(−dη² + dx²)`: the mode
`φ = h(η) cos(kx)` has `□φ = a⁻²(−h″ − 2(a′/a)h′ − k²h) cos(kx)`, and with `a = −1/(Hη)` the TT mode
`h = η cos kη − sin kη / k` (`u = ah ∝ cos kη − sin kη/(kη)`) solves `□φ = 0` -/

section SweepB13

set_option synthInstance.maxHeartbeats 400000

lemma diag4_smooth {c : Fin 4 → (Fin 4 → ℝ) → ℝ} (hcs : ∀ i, ContDiff ℝ ∞ (c i)) : ContDiff ℝ ∞ (diag4 c) := by
  rw [contDiff_clm_apply_iff]; intro a; rw [contDiff_clm_apply_iff]; intro b
  simp only [diag4_apply]
  exact ContDiff.sum fun i _ => (hcs i).mul contDiff_const

/-- The Christoffel form of `Σ cᵢ(p) dxᵢ²`: `Γ(a,b)ₖ = (Dcₖ·a bₖ + Dcₖ·b aₖ − Σⱼ ∂ₖcⱼ aⱼbⱼ)/(2cₖ)`. -/
noncomputable def gamD (c : Fin 4 → (Fin 4 → ℝ) → ℝ) (p a b : Fin 4 → ℝ) : Fin 4 → ℝ := fun k =>
  (fderiv ℝ (c k) p a * b k + fderiv ℝ (c k) p b * a k - ∑ j, fderiv ℝ (c j) p (Pi.single k 1) * (a j * b j))
    / (2 * c k p)

variable {c : Fin 4 → (Fin 4 → ℝ) → ℝ} (hc : ∀ i p, c i p ≠ 0) (hcs : ∀ i, ContDiff ℝ ∞ (c i))
include hc hcs

/-- **The engine:** `lcGam` of any diagonal metric on `ℝ⁴` is `gamD`. -/
lemma lcGam_diag4 (p a b : Fin 4 → ℝ) : lcGam (diag4 c) p a b = gamD c p a b := by
  have inv := flat_isInvertible (diag4 c) (fun p u h => diag4_nondeg (fun i => hc i p) u h) p
  have hD : ∀ e a b : Fin 4 → ℝ, fderiv ℝ (diag4 c) p e a b = ∑ i, fderiv ℝ (c i) p e * (a i * b i) :=
    fun e a b => by
    rw [fderiv_apply₂' ((diag4_smooth hcs).differentiable (by simp) p),
      show (fun y => diag4 c y a b) = fun y => ∑ i, c i y * (a i * b i) from funext fun y => diag4_apply c y a b]
    rw [(HasFDerivAt.fun_sum fun i _ => (((hcs i).differentiable (by simp) p).hasFDerivAt.mul_const
      (a i * b i))).fderiv]
    simp; exact Finset.sum_congr rfl fun i _ => by ring
  have hK : koszK (diag4 c) p a b = diag4 c p (gamD c p a b) := by
    refine ContinuousLinearMap.ext fun v => ?_
    have hv : v = ∑ k, v k • (Pi.single k 1 : Fin 4 → ℝ) := by ext i; simp [Pi.single_apply]
    rw [koszK_apply, hD, hD, hD, diag4_apply]
    simp only [gamD, Fin.sum_univ_four]
    have := hc 0 p; have := hc 1 p; have := hc 2 p; have := hc 3 p
    conv_lhs => rw [hv]
    simp [Fin.sum_univ_four]
    field_simp; ring
  rw [lcGam_apply, hK, inv.inverse_apply_self]

omit hc hcs

/-- THE connection's wave operator for a diagonal metric `Σ cᵢ dxᵢ²`: `□φ = Σᵢ cᵢ⁻¹ (∂ᵢ∂ᵢφ − (∇_{eᵢ} eᵢ)φ)`. -/
noncomputable def boxD (m : NDMetric 𝓘(ℝ, Fin 4 → ℝ) (Fin 4 → ℝ)) (c : Fin 4 → (Fin 4 → ℝ) → ℝ)
    (φ : (Fin 4 → ℝ) → ℝ) (p : Fin 4 → ℝ) : ℝ :=
  ∑ i, (c i p)⁻¹ * (fderiv ℝ (fun y => fderiv ℝ φ y (Pi.single i 1)) p (Pi.single i 1)
    - fderiv ℝ φ p (lcConn (Fin 4 → ℝ) m (fun _ => (Pi.single i 1 : Fin 4 → ℝ)) p (Pi.single i 1)))

/-- The conformally flat metric `a(η)²(−dη² + dx² + dy² + dz²)`. -/
noncomputable def cConf (a : ℝ → ℝ) : Fin 4 → (Fin 4 → ℝ) → ℝ :=
  ![fun p => -a (p 0) ^ 2, fun p => a (p 0) ^ 2, fun p => a (p 0) ^ 2, fun p => a (p 0) ^ 2]

variable {a h : ℝ → ℝ} (ha : ∀ s, a s ≠ 0) (has : ContDiff ℝ ∞ a) (hhs : ContDiff ℝ ∞ h)

include ha in
lemma cConf_ne (i : Fin 4) (p : Fin 4 → ℝ) : cConf a i p ≠ 0 := by
  fin_cases i <;> simp [cConf, ha]

include has in
lemma cConf_smooth (i : Fin 4) : ContDiff ℝ ∞ (cConf a i) := by
  have := has.comp (contDiff_apply ℝ ℝ (0 : Fin 4))
  fin_cases i <;> simp [cConf] <;> fun_prop

include ha has hhs in
/-- **B13.** `□(h(η) cos kx) = a⁻²(−h″ − 2(a′/a)h′ − k²h) cos kx` for THE Levi-Civita connection. -/
theorem conf_box (k : ℝ) (p : Fin 4 → ℝ) :
    boxD (ndOf (diag4 (cConf a)) (diag4_symm _) (fun p u h => diag4_nondeg (fun i => cConf_ne ha i p) u h)
      ((diag4_smooth (cConf_smooth has)).differentiable (by simp))) (cConf a) (fun y => h (y 0) * Real.cos (k * y 1)) p
      = (a (p 0) ^ 2)⁻¹ * (-deriv (deriv h) (p 0) - 2 * (deriv a (p 0) / a (p 0)) * deriv h (p 0)
          - k ^ 2 * h (p 0)) * Real.cos (k * p 1) := by
  have da : ∀ s, DifferentiableAt ℝ a s := fun s => (has.differentiable (by simp)) s
  have dh : ∀ s, DifferentiableAt ℝ h s := fun s => (hhs.differentiable (by simp)) s
  have dh' : ∀ s, DifferentiableAt ℝ (deriv h) s :=
    fun s => ((contDiff_infty_iff_deriv.1 hhs).2.differentiable (by simp)) s
  have pr : ∀ (i : Fin 4) (y : Fin 4 → ℝ), HasFDerivAt (fun z : Fin 4 → ℝ => z i) _ y :=
    fun i y => hasFDerivAt_apply (𝕜 := ℝ) i y
  have cosk : ∀ (y : Fin 4 → ℝ), HasFDerivAt (fun z : Fin 4 → ℝ => Real.cos (k * z 1)) _ y :=
    fun y => (Real.hasDerivAt_cos _).comp_hasFDerivAt y ((pr 1 y).const_mul k)
  have sink : ∀ (y : Fin 4 → ℝ), HasFDerivAt (fun z : Fin 4 → ℝ => Real.sin (k * z 1)) _ y :=
    fun y => (Real.hasDerivAt_sin _).comp_hasFDerivAt y ((pr 1 y).const_mul k)
  have hφ : ∀ y, HasFDerivAt (fun z : Fin 4 → ℝ => h (z 0) * Real.cos (k * z 1)) _ y :=
    fun y => (fd_coord (dh _)).mul (cosk y)
  have e0 : (fun y => fderiv ℝ (fun z : Fin 4 → ℝ => h (z 0) * Real.cos (k * z 1)) y (Pi.single 0 1))
      = fun y => deriv h (y 0) * Real.cos (k * y 1) := funext fun y => by rw [(hφ y).fderiv]; simp; ring
  have e1 : (fun y => fderiv ℝ (fun z : Fin 4 → ℝ => h (z 0) * Real.cos (k * z 1)) y (Pi.single 1 1))
      = fun y => -(k * (h (y 0) * Real.sin (k * y 1))) := funext fun y => by rw [(hφ y).fderiv]; simp; ring
  have e2 : ∀ j : Fin 4, j = 2 ∨ j = 3 →
      (fun y => fderiv ℝ (fun z : Fin 4 → ℝ => h (z 0) * Real.cos (k * z 1)) y (Pi.single j 1)) = fun _ => 0 :=
    fun j hj => funext fun y => by rcases hj with rfl | rfl <;> (rw [(hφ y).fderiv]; simp)
  have hsq := (fd_coord (x := p) (da (p 0))).pow 2
  have hq : ∀ v, fderiv ℝ (fun p : Fin 4 → ℝ => a (p 0) ^ 2) p v = 2 * a (p 0) * deriv a (p 0) * v 0 :=
    fun v => by rw [hsq.fderiv]; simp; ring
  have g0 : HasFDerivAt (fun y : Fin 4 → ℝ => deriv h (y 0) * Real.cos (k * y 1)) _ p :=
    (fd_coord (dh' _)).mul (cosk p)
  have g1 : HasFDerivAt (fun y : Fin 4 → ℝ => -(k * (h (y 0) * Real.sin (k * y 1)))) _ p :=
    (((fd_coord (dh _)).mul (sink p)).const_mul k).neg
  simp only [boxD, Fin.sum_univ_four, lcConn_const, lcGam_diag4 (cConf_ne ha) (cConf_smooth has), e0, e1,
    e2 2 (Or.inl rfl), e2 3 (Or.inr rfl), (hφ p).fderiv]
  rw [g0.fderiv, g1.fderiv]
  simp [gamD, Fin.sum_univ_four, cConf, hq]
  have := ha (p 0)
  field_simp; ring

/-- The de Sitter TT mode, `h = η cos kη − sin kη / k` (so `a h ∝ cos kη − sin kη/(kη)`). -/
noncomputable def hTT (k s : ℝ) : ℝ := s * Real.cos (k * s) - Real.sin (k * s) / k

open Filter Topology in
include ha has in
/-- **B13, receipt 8.** On de Sitter in conformal time (`a = −1/(Hη)` near `η`), the TT mode `h(η) cos kx` solves
THE connection's wave equation `□φ = 0`. -/
theorem ds_tt_mode {H k η : ℝ} (hH : H ≠ 0) (hk : k ≠ 0) (hη : η ≠ 0) (haη : a =ᶠ[𝓝 η] fun s => -(H * s)⁻¹)
    (p : Fin 4 → ℝ) (hp : p 0 = η) :
    boxD (ndOf (diag4 (cConf a)) (diag4_symm _) (fun p u h => diag4_nondeg (fun i => cConf_ne ha i p) u h)
      ((diag4_smooth (cConf_smooth has)).differentiable (by simp))) (cConf a)
      (fun y => hTT k (y 0) * Real.cos (k * y 1)) p = 0 := by
  have hs : ContDiff ℝ ∞ (hTT k) := by unfold hTT; fun_prop
  have d1 : ∀ s, HasDerivAt (hTT k) (-(k * s * Real.sin (k * s))) s := fun s => by
    have hc := (Real.hasDerivAt_cos (k * s)).comp s ((hasDerivAt_id s).const_mul k)
    have hn := (Real.hasDerivAt_sin (k * s)).comp s ((hasDerivAt_id s).const_mul k)
    refine HasDerivAt.congr_deriv (HasDerivAt.sub ((hasDerivAt_id s).mul hc) (hn.div_const k)) ?_
    simp; field_simp; ring
  have d2 : HasDerivAt (fun s => -(k * s * Real.sin (k * s))) (-(k * Real.sin (k * η) + k * η * (Real.cos (k * η) * k))) η :=
    by
    have hn := (Real.hasDerivAt_sin (k * η)).comp η ((hasDerivAt_id η).const_mul k)
    refine HasDerivAt.congr_deriv ((((hasDerivAt_id η).const_mul k).mul hn).neg) ?_
    simp
  have dd : deriv (hTT k) = fun s => -(k * s * Real.sin (k * s)) := funext fun s => (d1 s).deriv
  have da : deriv a η = 1 / (H * η ^ 2) := by
    rw [haη.deriv_eq]
    exact (((hasDerivAt_id η).const_mul H).inv (mul_ne_zero hH hη)).neg.deriv.trans (by simp only [id_eq]; field_simp)
  rw [conf_box ha has hs, hp, dd, d2.deriv, haη.eq_of_nhds, da]
  unfold hTT
  field_simp; ring

end SweepB13

/-! ## `r7315`, B14 — receipt 76: the Mukhanov variable. For THE connection on `a(η)²(−dη² + dx²)`, the field mode
`φ = h(η) cos kx` has `(□ − m²)φ = −a⁻³ (W″ + (k² + m²a² − a″/a) W) cos kx` with `W = a h`; on de Sitter
`a = −1/(Hη)`, `a″/a = 2/η²`, so the massless mode obeys `W″ + (k² − 2/η²) W = 0` -/

section SweepB14

variable {a h : ℝ → ℝ} (ha : ∀ s, a s ≠ 0) (has : ContDiff ℝ ∞ a) (hhs : ContDiff ℝ ∞ h)
include ha has hhs

/-- **B14, receipt 76.** -/
theorem mukhanov (k m : ℝ) (p : Fin 4 → ℝ) :
    boxD (ndOf (diag4 (cConf a)) (diag4_symm _) (fun p u h => diag4_nondeg (fun i => cConf_ne ha i p) u h)
      ((diag4_smooth (cConf_smooth has)).differentiable (by simp))) (cConf a) (fun y => h (y 0) * Real.cos (k * y 1)) p
      - m ^ 2 * (h (p 0) * Real.cos (k * p 1))
      = -(a (p 0) ^ 3)⁻¹ * (deriv (deriv fun s => a s * h s) (p 0)
          + (k ^ 2 + m ^ 2 * a (p 0) ^ 2 - deriv (deriv a) (p 0) / a (p 0)) * (a (p 0) * h (p 0)))
        * Real.cos (k * p 1) := by
  have D : ∀ {f : ℝ → ℝ}, ContDiff ℝ ∞ f → ∀ s, HasDerivAt f (deriv f s) s ∧ HasDerivAt (deriv f) (deriv (deriv f) s) s :=
    fun hf s => ⟨((contDiff_infty_iff_deriv.1 hf).1 s).hasDerivAt,
      (((contDiff_infty_iff_deriv.1 hf).2.differentiable (by simp)) s).hasDerivAt⟩
  have d1 : deriv (fun s => a s * h s) = fun s => deriv a s * h s + a s * deriv h s :=
    funext fun s => ((D has s).1.mul (D hhs s).1).deriv
  have d2 : deriv (fun s => deriv a s * h s + a s * deriv h s) (p 0) = deriv (deriv a) (p 0) * h (p 0)
      + deriv a (p 0) * deriv h (p 0) + (deriv a (p 0) * deriv h (p 0) + a (p 0) * deriv (deriv h) (p 0)) :=
    (HasDerivAt.add ((D has (p 0)).2.mul (D hhs (p 0)).1) ((D has (p 0)).1.mul (D hhs (p 0)).2)).deriv
  rw [conf_box ha has hhs, d1, d2]
  have := ha (p 0)
  field_simp; ring

omit has hhs ha

open Filter Topology in
/-- On de Sitter, `a = −1/(Hη)`: `a″/a = 2/η²`. -/
lemma ds_app {H η : ℝ} (hH : H ≠ 0) (hη : η ≠ 0) (haη : a =ᶠ[𝓝 η] fun s => -(H * s)⁻¹) :
    deriv (deriv a) η / a η = 2 / η ^ 2 := by
  have hd : ∀ s ≠ 0, HasDerivAt (fun s => -(H * s)⁻¹) ((H * s ^ 2)⁻¹) s := fun s hs =>
    (((hasDerivAt_id s).const_mul H).inv (mul_ne_zero hH hs)).neg.congr_deriv (by simp only [id_eq]; field_simp)
  have e1 : deriv a =ᶠ[𝓝 η] fun s => (H * s ^ 2)⁻¹ :=
    haη.deriv.trans ((eventually_ne_nhds hη).mono fun s hs => (hd s hs).deriv)
  have h2 : HasDerivAt (fun s => (H * s ^ 2)⁻¹) (-(H * (2 * η)) / (H * η ^ 2) ^ 2) η := by
    have := ((hasDerivAt_pow 2 η).const_mul H).inv (mul_ne_zero hH (pow_ne_zero 2 hη))
    convert this using 1; simp
  rw [e1.deriv_eq, h2.deriv, haη.eq_of_nhds]
  field_simp

end SweepB14

/-! ## `r7315`, B15 — receipt 22: a second engine, for time-dependent diagonal metrics `Σ qᵢ(t) dxᵢ²` on `ℝ⁴` (THE
connection's Christoffel form `GT`, its `t`-derivative `DGT`, and its curvature on constant fields in closed form);
then de Sitter in the flat slicing, `−dt² + e^{2Ht} dx²`: `R = 12H²`, `Ric² = 36H⁴`, `Riem² = 24H⁴`, so
`Weyl² = 0` and `GB = 24H⁴` — with `α = 1/H` these are `144, 36, 24 /α⁴` squared and contracted -/

section SweepB15

set_option synthInstance.maxHeartbeats 400000

/-- `Σ qᵢ(t) dxᵢ²`, with `t = p 0`. -/
def cT (q : Fin 4 → ℝ → ℝ) : Fin 4 → (Fin 4 → ℝ) → ℝ := fun i p => q i (p 0)

noncomputable def GT (q : Fin 4 → ℝ → ℝ) (s : ℝ) (a b : Fin 4 → ℝ) : Fin 4 → ℝ := fun k =>
  (deriv (q k) s * (a 0 * b k + b 0 * a k) - if k = 0 then ∑ j, deriv (q j) s * (a j * b j) else 0) / (2 * q k s)

noncomputable def DGT (q : Fin 4 → ℝ → ℝ) (s : ℝ) (a b : Fin 4 → ℝ) : Fin 4 → ℝ := fun k =>
  ((deriv (deriv (q k)) s * (a 0 * b k + b 0 * a k)
      - if k = 0 then ∑ j, deriv (deriv (q j)) s * (a j * b j) else 0) * (2 * q k s)
    - (deriv (q k) s * (a 0 * b k + b 0 * a k) - if k = 0 then ∑ j, deriv (q j) s * (a j * b j) else 0)
      * (2 * deriv (q k) s)) / (2 * q k s) ^ 2

/-- The curvature, in closed form: `R(u,v)w = u⁰ DGT(v,w) − v⁰ DGT(u,w) + Γ(u,Γ(v,w)) − Γ(v,Γ(u,w))`. -/
noncomputable def curvT (q : Fin 4 → ℝ → ℝ) (s : ℝ) (u v w : Fin 4 → ℝ) : Fin 4 → ℝ :=
  u 0 • DGT q s v w - v 0 • DGT q s u w + GT q s u (GT q s v w) - GT q s v (GT q s u w)

variable {q : Fin 4 → ℝ → ℝ} (hq : ∀ i s, q i s ≠ 0) (hqs : ∀ i, ContDiff ℝ ∞ (q i))
include hq hqs

lemma cT_ne (i : Fin 4) (p : Fin 4 → ℝ) : cT q i p ≠ 0 := hq i _
lemma cT_smooth (i : Fin 4) : ContDiff ℝ ∞ (cT q i) := (hqs i).comp (contDiff_apply ℝ ℝ (0 : Fin 4))

lemma GT_hasDerivAt (s : ℝ) (a b : Fin 4 → ℝ) : HasDerivAt (fun t => GT q t a b) (DGT q s a b) s := by
  have d1 : ∀ i, HasDerivAt (deriv (q i)) (deriv (deriv (q i)) s) s := fun i =>
    (((contDiff_infty_iff_deriv.1 (hqs i)).2.differentiable (by simp)) s).hasDerivAt
  have d0 : ∀ i, HasDerivAt (q i) (deriv (q i) s) s := fun i => (((hqs i).differentiable (by simp)) s).hasDerivAt
  refine hasDerivAt_pi.2 fun k => ?_
  have hS : HasDerivAt (fun t => ∑ j, deriv (q j) t * (a j * b j)) (∑ j, deriv (deriv (q j)) s * (a j * b j)) s :=
    HasDerivAt.fun_sum fun j _ => (d1 j).mul_const _
  have hN : HasDerivAt (fun t => deriv (q k) t * (a 0 * b k + b 0 * a k)
      - if k = 0 then ∑ j, deriv (q j) t * (a j * b j) else 0)
      (deriv (deriv (q k)) s * (a 0 * b k + b 0 * a k)
        - if k = 0 then ∑ j, deriv (deriv (q j)) s * (a j * b j) else 0) s := by
    split_ifs
    · exact HasDerivAt.sub ((d1 k).mul_const _) hS
    · exact HasDerivAt.sub ((d1 k).mul_const _) (hasDerivAt_const s 0)
  exact (hN.div ((d0 k).const_mul 2) (mul_ne_zero two_ne_zero (hq k s))).congr_deriv (by simp [DGT])

lemma lcGam_T (p a b : Fin 4 → ℝ) : lcGam (diag4 (cT q)) p a b = GT q (p 0) a b := by
  rw [lcGam_diag4 (cT_ne hq hqs) (cT_smooth hq hqs)]
  have hf : ∀ i v, fderiv ℝ (cT q i) p v = deriv (q i) (p 0) * v 0 := fun i v => by
    show fderiv ℝ (fun y : Fin 4 → ℝ => q i (y 0)) p v = _
    rw [(fd_coord (x := p) (((hqs i).differentiable (by simp)) (p 0))).fderiv]; simp [mul_comm]
  funext k
  fin_cases k <;> simp [gamD, GT, hf, cT, Fin.sum_univ_four] <;> ring

lemma fderiv_lcGam_T (p u a b : Fin 4 → ℝ) :
    fderiv ℝ (lcGam (diag4 (cT q))) p u a b = u 0 • DGT q (p 0) a b := by
  have hGd : Differentiable ℝ (lcGam (diag4 (cT q))) :=
    (lcGam_smooth (fun p u h => diag4_nondeg (fun i => cT_ne hq hqs i p) u h)
      (diag4_smooth (cT_smooth hq hqs))).differentiable (by simp)
  rw [fderiv_apply₂' (hGd p), show (fun y => lcGam (diag4 (cT q)) y a b) = fun y => GT q (y 0) a b from
    funext fun y => lcGam_T hq hqs y a b]
  have H := (GT_hasDerivAt hq hqs (p 0) a b).hasFDerivAt.comp p (hasFDerivAt_apply (𝕜 := ℝ) (0 : Fin 4) p)
  rw [show (fun y : Fin 4 → ℝ => GT q (y 0) a b) = (fun t => GT q t a b) ∘ fun y => y 0 from rfl, H.fderiv]
  simp

/-- **B15, the engine.** THE connection's curvature of `Σ qᵢ(t) dxᵢ²` on constant fields is `curvT`. -/
theorem curv_T (p u v w : Fin 4 → ℝ) :
    curv (lcConn (Fin 4 → ℝ) (ndOf (diag4 (cT q)) (diag4_symm _)
      (fun p u h => diag4_nondeg (fun i => cT_ne hq hqs i p) u h) ((diag4_smooth (cT_smooth hq hqs)).differentiable
        (by simp)))) (fun _ => u) (fun _ => v) (fun _ => w) p = curvT q (p 0) u v w := by
  have hGd : Differentiable ℝ (lcGam (diag4 (cT q))) :=
    (lcGam_smooth (fun p u h => diag4_nondeg (fun i => cT_ne hq hqs i p) u h)
      (diag4_smooth (cT_smooth hq hqs))).differentiable (by simp)
  rw [curv_model _ _ (fun x w u => lcConn_const (diag4_symm _) _ _ x w u) hGd, fderiv_lcGam_T hq hqs,
    fderiv_lcGam_T hq hqs, lcGam_T hq hqs, lcGam_T hq hqs, lcGam_T hq hqs, lcGam_T hq hqs]
  rfl

omit hq hqs

/-- Contractions of a Riemann array `Rf i j k = R(eᵢ,eⱼ)eₖ` through a diagonal metric `g`. -/
noncomputable def ricC (Rf : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ) (j k : Fin 4) : ℝ := ∑ i, Rf i j k i
noncomputable def scalC (g : Fin 4 → ℝ) (Rf : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ) : ℝ := ∑ j, ricC Rf j j / g j
noncomputable def ric2C (g : Fin 4 → ℝ) (Rf : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ) : ℝ :=
  ∑ j, ∑ k, ricC Rf j k ^ 2 / (g j * g k)
noncomputable def riem2C (g : Fin 4 → ℝ) (Rf : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ) : ℝ :=
  ∑ i, ∑ j, ∑ k, ∑ l, (g l * Rf i j k l) ^ 2 / (g i * g j * g k * g l)

/-- de Sitter in the flat slicing: `−dt² + e^{2Ht}(dx² + dy² + dz²)`. -/
noncomputable def qDS (H : ℝ) : Fin 4 → ℝ → ℝ :=
  ![fun _ => -1, fun s => Real.exp (2 * H * s), fun s => Real.exp (2 * H * s), fun s => Real.exp (2 * H * s)]

lemma qDS_ne (H : ℝ) (i : Fin 4) (s : ℝ) : qDS H i s ≠ 0 := by fin_cases i <;> simp [qDS, Real.exp_ne_zero]
lemma qDS_smooth (H : ℝ) (i : Fin 4) : ContDiff ℝ ∞ (qDS H i) := by fin_cases i <;> simp [qDS] <;> fun_prop

/-- **B15, receipt 22.** THE connection's invariants on de Sitter: `R = 12H²`, `Ric² = 36H⁴`, `Riem² = 24H⁴`;
hence `Weyl² = Riem² − 2Ric² + R²/3 = 0` and `GB = Riem² − 4Ric² + R² = 24H⁴`. -/
theorem ds_invariants (H : ℝ) (p : Fin 4 → ℝ) :
    let Rf := fun i j k => curv (lcConn (Fin 4 → ℝ) (ndOf (diag4 (cT (qDS H))) (diag4_symm _)
      (fun p u h => diag4_nondeg (fun i => cT_ne (qDS_ne H) (qDS_smooth H) i p) u h)
      ((diag4_smooth (cT_smooth (qDS_ne H) (qDS_smooth H))).differentiable (by simp))))
      (fun _ => (Pi.single i 1 : Fin 4 → ℝ)) (fun _ => (Pi.single j 1 : Fin 4 → ℝ))
      (fun _ => (Pi.single k 1 : Fin 4 → ℝ)) p
    let g := fun i => qDS H i (p 0)
    scalC g Rf = 12 * H ^ 2 ∧ ric2C g Rf = 36 * H ^ 4 ∧ riem2C g Rf = 24 * H ^ 4
      ∧ riem2C g Rf - 2 * ric2C g Rf + scalC g Rf ^ 2 / 3 = 0
      ∧ riem2C g Rf - 4 * ric2C g Rf + scalC g Rf ^ 2 = 24 * H ^ 4 := by
  intro Rf g
  have h1 : ∀ s, HasDerivAt (fun s => Real.exp (2 * H * s)) (2 * H * Real.exp (2 * H * s)) s := fun s =>
    HasDerivAt.congr_deriv (((hasDerivAt_id' s).const_mul (2 * H)).exp) (by ring)
  have e1 : deriv (fun s => Real.exp (2 * H * s)) = fun s => 2 * H * Real.exp (2 * H * s) :=
    funext fun s => (h1 s).deriv
  have e2 : deriv (fun s => 2 * H * Real.exp (2 * H * s)) = fun s => 4 * H ^ 2 * Real.exp (2 * H * s) :=
    funext fun s => (HasDerivAt.congr_deriv ((h1 s).const_mul (2 * H)) (by ring)).deriv
  have hR : ∀ i j k, Rf i j k = curvT (qDS H) (p 0) (Pi.single i 1) (Pi.single j 1) (Pi.single k 1) :=
    fun i j k => curv_T (qDS_ne H) (qDS_smooth H) p _ _ _
  have hS : scalC g Rf = 12 * H ^ 2 := by
    simp only [scalC, ricC, hR, g]
    simp [Fin.sum_univ_four, curvT, GT, DGT, qDS, e1, e2]
    field_simp; ring
  have hC : ric2C g Rf = 36 * H ^ 4 := by
    simp only [ric2C, ricC, hR, g]
    simp [Fin.sum_univ_four, curvT, GT, DGT, qDS, e1, e2]
    field_simp; ring
  have hM : riem2C g Rf = 24 * H ^ 4 := by
    simp only [riem2C, hR, g]
    simp [Fin.sum_univ_four, curvT, GT, DGT, qDS, e1, e2]
    field_simp; ring
  refine ⟨hS, hC, hM, ?_, ?_⟩ <;> rw [hS, hC, hM] <;> ring

end SweepB15

/-! ## `r7315`, B16 — receipt 4 (its chartable half): flat FRW `−dt² + a(t)² dx²` under THE connection has
`R = 6(ä/a + ȧ²/a²)`, and on P15's layer `a = sinh^{2/3}(3Ht/2)` that is `R = 12H² + 3H²/sinh²(3Ht/2)`: it RUNS.
*P10's closed slicing `a = α cosh(T/α)` on `S³` fails the chart clause and is not attempted.* -/

section SweepB16

set_option synthInstance.maxHeartbeats 400000

/-- Flat FRW: `q = (−1, a², a², a²)`. -/
noncomputable def qFRW (a : ℝ → ℝ) : Fin 4 → ℝ → ℝ :=
  ![fun _ => -1, fun s => a s ^ 2, fun s => a s ^ 2, fun s => a s ^ 2]

variable {a : ℝ → ℝ} (ha : ∀ s, a s ≠ 0) (has : ContDiff ℝ ∞ a)

include ha in
lemma qFRW_ne (i : Fin 4) (s : ℝ) : qFRW a i s ≠ 0 := by fin_cases i <;> simp [qFRW, ha]
include has in
lemma qFRW_smooth (i : Fin 4) : ContDiff ℝ ∞ (qFRW a i) := by fin_cases i <;> simp [qFRW] <;> fun_prop

include ha has in
/-- **B16.** THE connection's scalar curvature of flat FRW. -/
theorem frw_scal (p : Fin 4 → ℝ) :
    scalC (fun i => qFRW a i (p 0)) (fun i j k => curv (lcConn (Fin 4 → ℝ) (ndOf (diag4 (cT (qFRW a)))
      (diag4_symm _) (fun p u h => diag4_nondeg (fun i => cT_ne (qFRW_ne ha) (qFRW_smooth has) i p) u h)
      ((diag4_smooth (cT_smooth (qFRW_ne ha) (qFRW_smooth has))).differentiable (by simp))))
      (fun _ => (Pi.single i 1 : Fin 4 → ℝ)) (fun _ => (Pi.single j 1 : Fin 4 → ℝ))
      (fun _ => (Pi.single k 1 : Fin 4 → ℝ)) p)
      = 6 * (deriv (deriv a) (p 0) / a (p 0) + (deriv a (p 0) / a (p 0)) ^ 2) := by
  have d0 : ∀ s, HasDerivAt a (deriv a s) s := fun s => ((has.differentiable (by simp)) s).hasDerivAt
  have d1 : ∀ s, HasDerivAt (deriv a) (deriv (deriv a) s) s := fun s =>
    (((contDiff_infty_iff_deriv.1 has).2.differentiable (by simp)) s).hasDerivAt
  have e1 : deriv (fun s => a s ^ 2) = fun s => 2 * a s * deriv a s :=
    funext fun s => ((d0 s).pow 2).deriv.trans (by simp)
  have e2 : deriv (fun s => 2 * a s * deriv a s) = fun s => 2 * deriv a s ^ 2 + 2 * a s * deriv (deriv a) s :=
    funext fun s => (((d0 s).const_mul 2).mul (d1 s)).deriv.trans (by ring)
  simp only [scalC, ricC, curv_T (qFRW_ne ha) (qFRW_smooth has)]
  simp [Fin.sum_univ_four, curvT, GT, DGT, qFRW, e1, e2]
  have := ha (p 0)
  field_simp; ring

omit ha has in
open Filter Topology in
/-- **B16, receipt 4.** On P15's layer, `a = sinh^{2/3}(3Ht/2)` near `t > 0`, the flat-FRW curvature
`6(ä/a + ȧ²/a²)` is `12H² + 3H²/sinh²(3Ht/2)`: it runs, divergent early and `12H²` late. -/
theorem layer_scal {H t : ℝ} (hH : 0 < H) (ht : 0 < t)
    (hat : a =ᶠ[𝓝 t] fun s => Real.sinh (3 * H / 2 * s) ^ (2 / 3 : ℝ)) :
    6 * (deriv (deriv a) t / a t + (deriv a t / a t) ^ 2)
      = 12 * H ^ 2 + 3 * H ^ 2 / Real.sinh (3 * H / 2 * t) ^ 2 := by
  set k := 3 * H / 2 with hk
  have hk0 : 0 < k := by positivity
  have hsk : ∀ s, HasDerivAt (fun s => Real.sinh (k * s)) (Real.cosh (k * s) * k) s := fun s => by
    exact (((hasDerivAt_id' s).const_mul k).sinh).congr_deriv (by ring)
  have hck : ∀ s, HasDerivAt (fun s => Real.cosh (k * s)) (Real.sinh (k * s) * k) s := fun s => by
    exact (((hasDerivAt_id' s).const_mul k).cosh).congr_deriv (by ring)
  have hA : ∀ s, 0 < Real.sinh (k * s) → HasDerivAt (fun s => Real.sinh (k * s) ^ (2 / 3 : ℝ))
      (2 / 3 * k * Real.cosh (k * s) * (Real.sinh (k * s) ^ (2 / 3 : ℝ) / Real.sinh (k * s))) s := fun s hs =>
    ((hsk s).rpow_const (p := 2 / 3) (Or.inl hs.ne')).congr_deriv (by
      rw [show (2 / 3 : ℝ) - 1 = 2 / 3 - 1 from rfl, Real.rpow_sub_one hs.ne']; ring)
  have hpos : ∀ᶠ s in 𝓝 t, 0 < Real.sinh (k * s) :=
    ((Real.continuous_sinh.comp (continuous_const.mul continuous_id)).continuousAt (x := t)).eventually
      (lt_mem_nhds (Real.sinh_pos_iff.2 (mul_pos hk0 ht)))
  have hS := hpos.self_of_nhds
  have hd : deriv a =ᶠ[𝓝 t] fun s =>
      2 / 3 * k * Real.cosh (k * s) * (Real.sinh (k * s) ^ (2 / 3 : ℝ) / Real.sinh (k * s)) :=
    hat.deriv.trans (hpos.mono fun s hs => (hA s hs).deriv)
  have h2 : HasDerivAt (fun s => 2 / 3 * k * Real.cosh (k * s)
      * (Real.sinh (k * s) ^ (2 / 3 : ℝ) / Real.sinh (k * s))) _ t :=
    HasDerivAt.mul ((hck t).const_mul (2 / 3 * k)) (HasDerivAt.div (hA t hS) (hsk t) hS.ne')
  rw [hd.deriv_eq, h2.deriv, hd.eq_of_nhds, hat.eq_of_nhds]
  have hApos : 0 < Real.sinh (k * t) ^ (2 / 3 : ℝ) := Real.rpow_pos_of_pos hS _
  have hc := Real.cosh_sq (k * t)
  field_simp
  rw [hc, hk]; ring

end SweepB16

/-! ## `r7315`, B17 — receipt 5 (its chartable half): the layer's THE-connection curvature from B16,
`12H² + 3H²/sinh²(3Ht/2)`, tends to `12H²` as `t → ∞` — de Sitter's value from B15 -/

open Filter Topology in
/-- **B17, receipt 5.** -/
theorem layer_late {H : ℝ} (hH : 0 < H) :
    Tendsto (fun t => 12 * H ^ 2 + 3 * H ^ 2 / Real.sinh (3 * H / 2 * t) ^ 2) atTop (𝓝 (12 * H ^ 2)) := by
  have h1 : Tendsto (fun t => Real.sinh (3 * H / 2 * t)) atTop atTop :=
    tendsto_atTop_mono' _ ((eventually_ge_atTop 0).mono fun t ht =>
      Real.self_le_sinh_iff.2 (by positivity)) (tendsto_id.const_mul_atTop (by positivity))
  have h2 := (tendsto_const_nhds (x := 3 * H ^ 2)).div_atTop ((tendsto_pow_atTop two_ne_zero).comp h1)
  simpa using (tendsto_const_nhds (x := 12 * H ^ 2)).add h2

/-! ## `r7315`, B18 — receipt 2: on flat FRW `−dt² + a(t)² dx²`, for a FREE `a`, THE connection's
`Weyl² = Riem² − 2Ric² + R²/3 = 0` -/

section SweepB18

set_option synthInstance.maxHeartbeats 400000

variable {a : ℝ → ℝ} (ha : ∀ s, a s ≠ 0) (has : ContDiff ℝ ∞ a)
include ha has

/-- **B18, receipt 2 (k = 0).** -/
theorem frw_weyl (p : Fin 4 → ℝ) :
    let Rf := fun i j k => curv (lcConn (Fin 4 → ℝ) (ndOf (diag4 (cT (qFRW a))) (diag4_symm _)
      (fun p u h => diag4_nondeg (fun i => cT_ne (qFRW_ne ha) (qFRW_smooth has) i p) u h)
      ((diag4_smooth (cT_smooth (qFRW_ne ha) (qFRW_smooth has))).differentiable (by simp))))
      (fun _ => (Pi.single i 1 : Fin 4 → ℝ)) (fun _ => (Pi.single j 1 : Fin 4 → ℝ))
      (fun _ => (Pi.single k 1 : Fin 4 → ℝ)) p
    let g := fun i => qFRW a i (p 0)
    riem2C g Rf - 2 * ric2C g Rf + scalC g Rf ^ 2 / 3 = 0 := by
  intro Rf g
  have d0 : ∀ s, HasDerivAt a (deriv a s) s := fun s => ((has.differentiable (by simp)) s).hasDerivAt
  have d1 : ∀ s, HasDerivAt (deriv a) (deriv (deriv a) s) s := fun s =>
    (((contDiff_infty_iff_deriv.1 has).2.differentiable (by simp)) s).hasDerivAt
  have e1 : deriv (fun s => a s ^ 2) = fun s => 2 * a s * deriv a s :=
    funext fun s => ((d0 s).pow 2).deriv.trans (by simp)
  have e2 : deriv (fun s => 2 * a s * deriv a s) = fun s => 2 * deriv a s ^ 2 + 2 * a s * deriv (deriv a) s :=
    funext fun s => (((d0 s).const_mul 2).mul (d1 s)).deriv.trans (by ring)
  have hR : ∀ i j k, Rf i j k = curvT (qFRW a) (p 0) (Pi.single i 1) (Pi.single j 1) (Pi.single k 1) :=
    fun i j k => curv_T (qFRW_ne ha) (qFRW_smooth has) p _ _ _
  simp only [riem2C, ric2C, scalC, ricC, hR, g]
  simp [Fin.sum_univ_four, curvT, GT, DGT, qFRW, e1, e2]
  have := ha (p 0)
  field_simp; ring

end SweepB18

/-! ## `r7319`, the `4D` engine (pre-registered at `r7317+71.6`) — E1: THE connection's curvature on constant fields
for ANY diagonal metric `Σ cₖ(p) dxₖ²` on `ℝ⁴`, in closed form in `cₖ`, `∂cₖ` and `∂∂cₖ` at the point.
***The interface is `curvD_eq`; nothing downstream needs `lcConn`, `kosz`, `curv_model` or `lcGam`.*** -/

section Engine4D

set_option synthInstance.maxHeartbeats 400000

/-- First and second partials of a coefficient: `∂_v cₖ` and `∂_u ∂_v cₖ` at `p`. -/
noncomputable def dC1 (c : Fin 4 → (Fin 4 → ℝ) → ℝ) (p : Fin 4 → ℝ) (k : Fin 4) (v : Fin 4 → ℝ) : ℝ :=
  fderiv ℝ (c k) p v
noncomputable def dC2 (c : Fin 4 → (Fin 4 → ℝ) → ℝ) (p : Fin 4 → ℝ) (k : Fin 4) (u v : Fin 4 → ℝ) : ℝ :=
  fderiv ℝ (fderiv ℝ (c k)) p u v

/-- `∂_u` of the Christoffel form `gamD`, componentwise. -/
noncomputable def DGD (c : Fin 4 → (Fin 4 → ℝ) → ℝ) (p u a b : Fin 4 → ℝ) : Fin 4 → ℝ := fun k =>
  ((dC2 c p k u a * b k + dC2 c p k u b * a k - ∑ j, dC2 c p j u (Pi.single k 1) * (a j * b j)) * (2 * c k p)
    - (dC1 c p k a * b k + dC1 c p k b * a k - ∑ j, dC1 c p j (Pi.single k 1) * (a j * b j)) * (2 * dC1 c p k u))
    / (2 * c k p) ^ 2

/-- **The engine's closed form**: `R(u,v)w = ∂_u Γ(v,w) − ∂_v Γ(u,w) + Γ(u,Γ(v,w)) − Γ(v,Γ(u,w))`. -/
noncomputable def curvD (c : Fin 4 → (Fin 4 → ℝ) → ℝ) (p u v w : Fin 4 → ℝ) : Fin 4 → ℝ :=
  DGD c p u v w - DGD c p v u w + gamD c p u (gamD c p v w) - gamD c p v (gamD c p u w)

variable {c : Fin 4 → (Fin 4 → ℝ) → ℝ} (hc : ∀ i p, c i p ≠ 0) (hcs : ∀ i, ContDiff ℝ ∞ (c i))
include hc hcs

omit hc in
lemma dC1_hasFDerivAt (p : Fin 4 → ℝ) (k : Fin 4) (v : Fin 4 → ℝ) :
    HasFDerivAt (fun y => fderiv ℝ (c k) y v) ((fderiv ℝ (fderiv ℝ (c k)) p).flip v) p := by
  have h2 := ((hcs k).fderiv_right (m := ∞) (by simp)).differentiable (by simp) p
  exact (h2.hasFDerivAt.clm_apply (hasFDerivAt_const v p)).congr_fderiv (by ext; simp)

lemma gamD_comp_hasFDerivAt (p a b : Fin 4 → ℝ) (k : Fin 4) :
    ∃ L : (Fin 4 → ℝ) →L[ℝ] ℝ, HasFDerivAt (fun y => gamD c y a b k) L p ∧ ∀ u, L u = DGD c p u a b k := by
  have hN : HasFDerivAt (fun y => fderiv ℝ (c k) y a * b k + fderiv ℝ (c k) y b * a k
      - ∑ j, fderiv ℝ (c j) y (Pi.single k 1) * (a j * b j)) _ p :=
    HasFDerivAt.sub (HasFDerivAt.add ((dC1_hasFDerivAt hcs p k a).mul_const _) ((dC1_hasFDerivAt hcs p k b).mul_const _))
      (HasFDerivAt.fun_sum fun j _ => (dC1_hasFDerivAt hcs p j _).mul_const _)
  have hD : HasFDerivAt (fun y => 2 * c k y) _ p :=
    (((hcs k).differentiable (by simp) p).hasFDerivAt).const_mul 2
  have hq := HasFDerivAt.mul hN ((hasDerivAt_inv (mul_ne_zero two_ne_zero (hc k p))).comp_hasFDerivAt p hD)
  refine ⟨_, hq, fun u => ?_⟩
  simp only [DGD, dC1, dC2]
  have := hc k p
  simp
  field_simp
  rw [Finset.sum_congr rfl fun x _ => (by ring : a x * b x * fderiv ℝ (fderiv ℝ (c x)) p u (Pi.single k 1)
    = fderiv ℝ (fderiv ℝ (c x)) p u (Pi.single k 1) * a x * b x)]
  ring

/-- `∂_u` of `gamD` as a vector. -/
lemma fderiv_gamD (p u a b : Fin 4 → ℝ) : fderiv ℝ (fun y => gamD c y a b) p u = DGD c p u a b := by
  choose L hL hLu using fun k => gamD_comp_hasFDerivAt hc hcs p a b k
  have hd : DifferentiableAt ℝ (fun y => gamD c y a b) p := differentiableAt_pi.2 fun k => (hL k).differentiableAt
  funext k
  rw [show fderiv ℝ (fun y => gamD c y a b) p u k = fderiv ℝ (fun y => gamD c y a b k) p u by
    rw [_root_.fderiv_apply hd k]; rfl, (hL k).fderiv, hLu]

/-- **E1, the engine.** THE connection's curvature of `Σ cₖ dxₖ²` on constant fields is `curvD`. -/
theorem curvD_eq (p u v w : Fin 4 → ℝ) :
    curv (lcConn (Fin 4 → ℝ) (ndOf (diag4 c) (diag4_symm _) (fun p u h => diag4_nondeg (fun i => hc i p) u h)
      ((diag4_smooth hcs).differentiable (by simp)))) (fun _ => u) (fun _ => v) (fun _ => w) p = curvD c p u v w := by
  have hGd : Differentiable ℝ (lcGam (diag4 c)) :=
    (lcGam_smooth (fun p u h => diag4_nondeg (fun i => hc i p) u h) (diag4_smooth hcs)).differentiable (by simp)
  have hF : ∀ e a b, fderiv ℝ (lcGam (diag4 c)) p e a b = DGD c p e a b := fun e a b => by
    rw [fderiv_apply₂' (hGd p), show (fun y => lcGam (diag4 c) y a b) = fun y => gamD c y a b from
      funext fun y => lcGam_diag4 hc hcs y a b, fderiv_gamD hc hcs]
  rw [curv_model _ _ (fun x w u => lcConn_const (diag4_symm _) _ _ x w u) hGd, hF, hF,
    lcGam_diag4 hc hcs, lcGam_diag4 hc hcs, lcGam_diag4 hc hcs, lcGam_diag4 hc hcs]
  rfl

end Engine4D

/-! ### E2 — the remaining contractions, and the recipe for separable coefficients `cₖ = Fₖ(t) Gₖ(w)` -/

section Engine4D_E2

set_option synthInstance.maxHeartbeats 400000

noncomputable def weyl2C (g : Fin 4 → ℝ) (Rf : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ) : ℝ :=
  riem2C g Rf - 2 * ric2C g Rf + scalC g Rf ^ 2 / 3
noncomputable def gbC (g : Fin 4 → ℝ) (Rf : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ) : ℝ :=
  riem2C g Rf - 4 * ric2C g Rf + scalC g Rf ^ 2
noncomputable def einsteinC (g : Fin 4 → ℝ) (Rf : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ) (j k : Fin 4) : ℝ :=
  ricC Rf j k - (if j = k then scalC g Rf * g j / 2 else 0)

/-- A separable diagonal metric: `cₖ(p) = Fₖ(p⁰) Gₖ(p¹)`. -/
def cS (F G : Fin 4 → ℝ → ℝ) : Fin 4 → (Fin 4 → ℝ) → ℝ := fun k y => F k (y 0) * G k (y 1)

lemma fd_coord_i {k : ℝ → ℝ} {x : Fin 4 → ℝ} (i : Fin 4) (hk : DifferentiableAt ℝ k (x i)) :
    HasFDerivAt (fun y : Fin 4 → ℝ => k (y i)) (deriv k (x i) • ContinuousLinearMap.proj (R := ℝ)
      (φ := fun _ : Fin 4 => ℝ) i) x :=
  hk.hasDerivAt.comp_hasFDerivAt x (hasFDerivAt_apply (𝕜 := ℝ) i x)

variable {F G : Fin 4 → ℝ → ℝ} (hF : ∀ k, ContDiff ℝ ∞ (F k)) (hG : ∀ k, ContDiff ℝ ∞ (G k))
include hF hG

lemma cS_smooth (k : Fin 4) : ContDiff ℝ ∞ (cS F G k) :=
  ((hF k).comp (contDiff_apply ℝ ℝ (0 : Fin 4))).mul ((hG k).comp (contDiff_apply ℝ ℝ (1 : Fin 4)))

lemma cS_hasFDerivAt (k : Fin 4) (y : Fin 4 → ℝ) : HasFDerivAt (cS F G k)
    (F k (y 0) • deriv (G k) (y 1) • ContinuousLinearMap.proj (R := ℝ) (φ := fun _ : Fin 4 => ℝ) 1
      + G k (y 1) • deriv (F k) (y 0) • ContinuousLinearMap.proj (R := ℝ) (φ := fun _ : Fin 4 => ℝ) 0) y :=
  (fd_coord_i 0 (((hF k).differentiable (by simp)) _)).mul (fd_coord_i 1 (((hG k).differentiable (by simp)) _))

/-- **The recipe, first partials.** -/
lemma dC1_cS (p : Fin 4 → ℝ) (k : Fin 4) (v : Fin 4 → ℝ) :
    dC1 (cS F G) p k v = deriv (F k) (p 0) * G k (p 1) * v 0 + F k (p 0) * deriv (G k) (p 1) * v 1 := by
  rw [dC1, (cS_hasFDerivAt hF hG k p).fderiv]; simp; ring

/-- **The recipe, second partials.** -/
lemma dC2_cS (p : Fin 4 → ℝ) (k : Fin 4) (u v : Fin 4 → ℝ) :
    dC2 (cS F G) p k u v = deriv (deriv (F k)) (p 0) * G k (p 1) * u 0 * v 0
      + deriv (F k) (p 0) * deriv (G k) (p 1) * (u 0 * v 1 + u 1 * v 0)
      + F k (p 0) * deriv (deriv (G k)) (p 1) * u 1 * v 1 := by
  have dF := fun s => (((contDiff_infty_iff_deriv.1 (hF k)).2).differentiable (by simp)) s
  have dG := fun s => (((contDiff_infty_iff_deriv.1 (hG k)).2).differentiable (by simp)) s
  have F0 := fun s => ((hF k).differentiable (by simp)) s
  have G0 := fun s => ((hG k).differentiable (by simp)) s
  have hφ : ∀ y, fderiv ℝ (cS F G k) y v
      = deriv (F k) (y 0) * G k (y 1) * v 0 + F k (y 0) * deriv (G k) (y 1) * v 1 := fun y => by
    rw [(cS_hasFDerivAt hF hG k y).fderiv]; simp; ring
  have hL : HasFDerivAt (fun y : Fin 4 → ℝ => deriv (F k) (y 0) * G k (y 1) * v 0
      + F k (y 0) * deriv (G k) (y 1) * v 1) _ p :=
    (((fd_coord_i 0 (dF _)).mul (fd_coord_i 1 (G0 _))).mul_const _).add
      (((fd_coord_i 0 (F0 _)).mul (fd_coord_i 1 (dG _))).mul_const _)
  have := (dC1_hasFDerivAt (c := cS F G) (cS_smooth hF hG) p k v).unique
    (by rw [show (fun y => fderiv ℝ (cS F G k) y v) = _ from funext hφ]; exact hL)
  rw [dC2, show fderiv ℝ (fderiv ℝ (cS F G k)) p u v = ((fderiv ℝ (fderiv ℝ (cS F G k)) p).flip v) u from rfl, this]
  simp; ring

end Engine4D_E2









/-! ### `r7323` E5 — the two-variable recipe: coefficients that depend on several coordinates and are NOT
separable products. A second partial is read off ANY `HasFDerivAt` of the first partial, and independence
from a coordinate kills every second partial with that slot. -/

section Engine4D_E5

set_option synthInstance.maxHeartbeats 400000

lemma fdA_hasFDerivAt {f : (Fin 4 → ℝ) → ℝ} (hf : ContDiff ℝ ∞ f) (p v : Fin 4 → ℝ) :
    HasFDerivAt (fun y => fderiv ℝ f y v) ((fderiv ℝ (fderiv ℝ f) p).flip v) p := by
  have h2 := (hf.fderiv_right (m := ∞) (by simp)).differentiable (by simp) p
  exact (h2.hasFDerivAt.clm_apply (hasFDerivAt_const v p)).congr_fderiv (by ext; simp)

/-- **E5.** The second partial `∂_u∂_v F` is `L u` for any derivative `L` of the first partial `∂_v F`. -/
lemma d2_of {F φ : (Fin 4 → ℝ) → ℝ} (hF : ContDiff ℝ ∞ F) {p v : Fin 4 → ℝ}
    (hφ : ∀ y, fderiv ℝ F y v = φ y) {L : (Fin 4 → ℝ) →L[ℝ] ℝ} (hL : HasFDerivAt φ L p) (u : Fin 4 → ℝ) :
    fderiv ℝ (fderiv ℝ F) p u v = L u := by
  have := (fdA_hasFDerivAt hF p v).unique (by rw [show (fun y => fderiv ℝ F y v) = φ from funext hφ]; exact hL)
  rw [show fderiv ℝ (fderiv ℝ F) p u v = ((fderiv ℝ (fderiv ℝ F) p).flip v) u from rfl, this]

/-- **E5.** No dependence on coordinate `i` ⇒ every second partial with an `i` slot vanishes. -/
lemma d2_indep {f : (Fin 4 → ℝ) → ℝ} (hf : ContDiff ℝ ∞ f) {i : Fin 4}
    (h0 : ∀ y, fderiv ℝ f y (Pi.single i 1) = 0) (p u : Fin 4 → ℝ) :
    fderiv ℝ (fderiv ℝ f) p u (Pi.single i 1) = 0 ∧ fderiv ℝ (fderiv ℝ f) p (Pi.single i 1) u = 0 := by
  have h1 : fderiv ℝ (fderiv ℝ f) p u (Pi.single i 1) = 0 := by
    rw [d2_of hf (φ := fun _ => 0) h0 (hasFDerivAt_const (0 : ℝ) p)]; simp
  exact ⟨h1, by rw [(hf.contDiffAt.isSymmSndFDerivAt (by simp)) _ _]; exact h1⟩

end Engine4D_E5



/-! ### `r7327` — the cutoff lemma: B's near-the-point convention, proved once. A profile smooth near `p` and
nonzero at `p` is equal near `p` to a profile that is smooth and nonzero EVERYWHERE, so every instance stated
"for profiles equal to the named ones near the point" is about profiles that exist. -/

section Cutoff

open Metric Filter Topology

/-- **The cutoff lemma.** `g = φf + (1 − φ)·f(p)`, `φ` a bump inside a ball where `f` keeps the sign of `f(p)`. -/
theorem exists_global_profile {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
    {f : E → ℝ} {p : E} {R : ℝ} (hR : 0 < R) (hf : ContDiffOn ℝ ∞ f (ball p R)) (hp : f p ≠ 0) :
    ∃ g : E → ℝ, ContDiff ℝ ∞ g ∧ (∀ x, g x ≠ 0) ∧ g =ᶠ[𝓝 p] f := by
  have hc : ContinuousAt f p := hf.continuousOn.continuousAt (ball_mem_nhds p hR)
  have hsq : 0 < f p * f p := mul_self_pos.2 hp
  obtain ⟨δ, hδ, hs⟩ := Metric.eventually_nhds_iff_ball.1
    ((hc.mul continuousAt_const).eventually (lt_mem_nhds hsq) |>.mono fun _ h => h)
  set r := min δ R with hr
  have hr0 : 0 < r := lt_min hδ hR
  let φ : ContDiffBump p := ⟨r / 4, r / 2, by positivity, by linarith⟩
  have hout : ∀ x, x ∉ ball p r → φ x = 0 := fun x hx =>
    φ.zero_of_le_dist (by simp only [mem_ball, not_lt] at hx; show r / 2 ≤ _; linarith)
  refine ⟨fun x => φ x * f x + (1 - φ x) * f p, ?_, fun x => ?_, ?_⟩
  · refine ContDiff.add (contDiff_iff_contDiffAt.2 fun x => ?_) ((contDiff_const.sub φ.contDiff).mul contDiff_const)
    by_cases hx : x ∈ ball p r
    · exact φ.contDiffAt.mul (hf.contDiffAt (isOpen_ball.mem_nhds
        (ball_subset_ball (min_le_right δ R) hx)))
    · have hz : (fun x => φ x * f x) =ᶠ[𝓝 x] fun _ => 0 := by
        have hU : {y | r / 2 < dist y p} ∈ 𝓝 x :=
          (isOpen_lt continuous_const (continuous_id.dist continuous_const)).mem_nhds
            (by simp only [mem_ball, not_lt] at hx; show r / 2 < dist x p; linarith)
        exact Filter.mem_of_superset hU fun y hy => by
          simp [φ.zero_of_le_dist (le_of_lt (show (r / 2 : ℝ) < dist y p from hy))]
      exact contDiffAt_const.congr_of_eventuallyEq hz
  · show φ x * f x + (1 - φ x) * f p ≠ 0
    by_cases hx : x ∈ ball p r
    · have hfx : 0 < f x * f p := by simpa using hs x (ball_subset_ball (min_le_left δ R) hx)
      have h0 := φ.nonneg (x := x); have h1 := φ.le_one (x := x)
      intro h
      have : (φ x * f x + (1 - φ x) * f p) * f p = 0 := by rw [h]; ring
      have hpos : 0 < (φ x * f x + (1 - φ x) * f p) * f p := by
        rcases h0.lt_or_eq with h0 | h0
        · nlinarith
        · rw [← h0]; nlinarith
      linarith
    · simp [hout x hx, hp]
  · filter_upwards [φ.eventuallyEq_one] with x hx
    simp [hx]

/-- **The cutoff lemma, in the shape the instances use**: a coefficient family smooth near `p` and nonzero at `p`
is equal near `p` to a family that is smooth and nowhere zero, so `diag4`'s hypotheses are met. -/
theorem exists_global_family {c : Fin 4 → (Fin 4 → ℝ) → ℝ} {p : Fin 4 → ℝ} {R : ℝ} (hR : 0 < R)
    (hc : ∀ i, ContDiffOn ℝ ∞ (c i) (Metric.ball p R)) (hp : ∀ i, c i p ≠ 0) :
    ∃ c' : Fin 4 → (Fin 4 → ℝ) → ℝ, (∀ i, ContDiff ℝ ∞ (c' i)) ∧ (∀ i x, c' i x ≠ 0)
      ∧ ∀ i, c' i =ᶠ[𝓝 p] c i := by
  choose c' h1 h2 h3 using fun i => exists_global_profile hR (hc i) (hp i)
  exact ⟨c', h1, h2, h3⟩

end Cutoff


/-! ### `r7327` — the coordinate recipe: first and second partials of a profile in ONE coordinate, and of a product
of profiles in two. This is what an `S²` metric's coefficients are made of, and it is the template the reopened rows
use. -/

section CoordRecipe

set_option synthInstance.maxHeartbeats 400000

variable {k m : ℝ → ℝ} (hk : ContDiff ℝ ∞ k) (hm : ContDiff ℝ ∞ m)

include hk in
lemma co_d1 (i : Fin 4) (y v : Fin 4 → ℝ) : fderiv ℝ (fun y : Fin 4 → ℝ => k (y i)) y v = deriv k (y i) * v i := by
  rw [(fd_coord_i i ((hk.differentiable (by simp)) _)).fderiv]; simp

include hk in
lemma co_d2 (i : Fin 4) (p u v : Fin 4 → ℝ) :
    fderiv ℝ (fderiv ℝ (fun y : Fin 4 → ℝ => k (y i))) p u v = deriv (deriv k) (p i) * u i * v i := by
  rw [d2_of (F := fun y : Fin 4 → ℝ => k (y i)) (hk.comp (contDiff_apply ℝ ℝ i)) (fun y => co_d1 hk i y v)
    ((fd_coord_i i (((contDiff_infty_iff_deriv.1 hk).2.differentiable (by simp)) _)).mul_const (v i))]
  simp; ring

include hk hm in
lemma pr_d1 (i j : Fin 4) (y v : Fin 4 → ℝ) : fderiv ℝ (fun y : Fin 4 → ℝ => k (y i) * m (y j)) y v
    = deriv k (y i) * v i * m (y j) + k (y i) * (deriv m (y j) * v j) := by
  rw [(show HasFDerivAt (fun y : Fin 4 → ℝ => k (y i) * m (y j)) _ y from
    (fd_coord_i i ((hk.differentiable (by simp)) _)).mul (fd_coord_i j ((hm.differentiable (by simp)) _))).fderiv]
  simp; ring

include hk hm in
lemma pr_d2 (i j : Fin 4) (p u v : Fin 4 → ℝ) :
    fderiv ℝ (fderiv ℝ (fun y : Fin 4 → ℝ => k (y i) * m (y j))) p u v
      = deriv (deriv k) (p i) * u i * v i * m (p j) + deriv k (p i) * v i * (deriv m (p j) * u j)
        + deriv k (p i) * u i * (deriv m (p j) * v j) + k (p i) * (deriv (deriv m) (p j) * u j * v j) := by
  have dk := fun s => ((contDiff_infty_iff_deriv.1 hk).2.differentiable (by simp)) s
  have dm := fun s => ((contDiff_infty_iff_deriv.1 hm).2.differentiable (by simp)) s
  rw [d2_of (F := fun y : Fin 4 → ℝ => k (y i) * m (y j))
    ((hk.comp (contDiff_apply ℝ ℝ i)).mul (hm.comp (contDiff_apply ℝ ℝ j))) (fun y => pr_d1 hk hm i j y v)
    (HasFDerivAt.add (((fd_coord_i i (dk _)).mul_const (v i)).mul (fd_coord_i j ((hm.differentiable (by simp)) _)))
      ((fd_coord_i i ((hk.differentiable (by simp)) _)).mul ((fd_coord_i j (dm _)).mul_const (v j))))]
  simp; ring

end CoordRecipe

/-! ### `r7335` — the two-variable recipe, from `70`'s (`r7333+70.5`, row 13), stated for ANY coordinate pair
`i ≠ j` and any third coordinate `l`: first and second partials of `y ↦ h(yⁱ, yʲ)` and of `y ↦ h(yⁱ, yʲ) k(yˡ)`.
`70`'s copy at `(0, 1)` and `2` stays in its instance file under its own names. -/

section TwoVarRecipe

/-- `y ↦ (yⁱ, yʲ)`. -/
noncomputable def prP (i j : Fin 4) : (Fin 4 → ℝ) →L[ℝ] ℝ × ℝ :=
  (ContinuousLinearMap.proj (R := ℝ) (φ := fun _ : Fin 4 => ℝ) i).prod (ContinuousLinearMap.proj j)

lemma prP_apply (i j : Fin 4) (y : Fin 4 → ℝ) : prP i j y = (y i, y j) := rfl

lemma prP_split (i j : Fin 4) (y : Fin 4 → ℝ) :
    prP i j y = y i • ((1 : ℝ), (0 : ℝ)) + y j • ((0 : ℝ), (1 : ℝ)) := by
  simp [prP_apply]

/-- The two-variable partials of `h` at `q`: `∂ₐh` and `∂ₐ∂_bh`, `a, b ∈ {0, 1}` naming `h`'s two slots. -/
noncomputable def eTV : Fin 2 → ℝ × ℝ := ![(1, 0), (0, 1)]
noncomputable def d1H (h : ℝ × ℝ → ℝ) (q : ℝ × ℝ) (a : Fin 2) : ℝ := fderiv ℝ h q (eTV a)
noncomputable def d2H (h : ℝ × ℝ → ℝ) (q : ℝ × ℝ) (a b : Fin 2) : ℝ := fderiv ℝ (fderiv ℝ h) q (eTV a) (eTV b)

variable {h : ℝ × ℝ → ℝ} (hh : ContDiff ℝ ∞ h) (i j : Fin 4)

include hh in
lemma tw_has (y : Fin 4 → ℝ) :
    HasFDerivAt (fun y : Fin 4 → ℝ => h (y i, y j)) ((fderiv ℝ h (prP i j y)).comp (prP i j)) y :=
  ((hh.differentiable (by simp)) _).hasFDerivAt.comp y (prP i j).hasFDerivAt

include hh in
lemma tw_d1 (y v : Fin 4 → ℝ) :
    fderiv ℝ (fun y : Fin 4 → ℝ => h (y i, y j)) y v = v i * d1H h (y i, y j) 0 + v j * d1H h (y i, y j) 1 := by
  rw [(tw_has hh i j y).fderiv, ContinuousLinearMap.comp_apply, prP_split i j v, map_add, map_smul, map_smul]
  simp [d1H, eTV, prP_apply]

include hh in
lemma tw_line (w q : ℝ × ℝ) : HasFDerivAt (fun x => fderiv ℝ h x w) ((fderiv ℝ (fderiv ℝ h) q).flip w) q := by
  have hd := ((hh.fderiv_right (m := ∞) (by simp)).differentiable (by simp)) q
  exact hd.hasFDerivAt.clm_apply (hasFDerivAt_const w q) |>.congr_fderiv
    (by rw [ContinuousLinearMap.comp_zero, zero_add])

include hh in
lemma tw_d2 (p u v : Fin 4 → ℝ) :
    fderiv ℝ (fderiv ℝ (fun y : Fin 4 → ℝ => h (y i, y j))) p u v
      = u i * v i * d2H h (p i, p j) 0 0 + (u i * v j + u j * v i) * d2H h (p i, p j) 0 1
        + u j * v j * d2H h (p i, p j) 1 1 := by
  have hs := (hh.contDiffAt (x := (p i, p j))).isSymmSndFDerivAt (by simp)
  have L0 := (tw_line hh ((1 : ℝ), (0 : ℝ)) (prP i j p)).comp p (prP i j).hasFDerivAt
  have L1 := (tw_line hh ((0 : ℝ), (1 : ℝ)) (prP i j p)).comp p (prP i j).hasFDerivAt
  rw [d2_of (F := fun y : Fin 4 → ℝ => h (y i, y j)) (hh.comp (prP i j).contDiff) (fun y => tw_d1 hh i j y v)
    (((L0.const_mul (v i)).add (L1.const_mul (v j))).congr_of_eventuallyEq
      (Eventually.of_forall fun y => by simp [d1H, eTV, prP_apply]))]
  simp only [add_apply, smul_apply, ContinuousLinearMap.comp_apply,
    ContinuousLinearMap.flip_apply, smul_eq_mul]
  rw [prP_split i j u]
  simp only [map_add, map_smul, add_apply, smul_apply, smul_eq_mul]
  simp only [d2H, eTV, prP_apply, Matrix.cons_val_zero, Matrix.cons_val_one]
  rw [hs ((0 : ℝ), (1 : ℝ)) ((1 : ℝ), (0 : ℝ))]
  ring

variable {k : ℝ → ℝ} (hk : ContDiff ℝ ∞ k) (l : Fin 4)

include hh hk in
lemma twp_d1 (y v : Fin 4 → ℝ) :
    fderiv ℝ (fun y : Fin 4 → ℝ => h (y i, y j) * k (y l)) y v
      = (v i * d1H h (y i, y j) 0 + v j * d1H h (y i, y j) 1) * k (y l) + h (y i, y j) * (deriv k (y l) * v l) := by
  have H : HasFDerivAt (fun y : Fin 4 → ℝ => h (y i, y j) * k (y l)) _ y :=
    (tw_has hh i j y).mul (fd_coord_i l ((hk.differentiable (by simp)) _))
  rw [H.fderiv]
  simp only [add_apply, smul_apply, ContinuousLinearMap.comp_apply,
    smul_eq_mul, ContinuousLinearMap.proj_apply]
  rw [prP_split i j v, map_add, map_smul, map_smul]
  simp [d1H, eTV, prP_apply]; ring

include hh hk in
lemma twp_d2 (p u v : Fin 4 → ℝ) :
    fderiv ℝ (fderiv ℝ (fun y : Fin 4 → ℝ => h (y i, y j) * k (y l))) p u v
      = (u i * v i * d2H h (p i, p j) 0 0 + (u i * v j + u j * v i) * d2H h (p i, p j) 0 1
          + u j * v j * d2H h (p i, p j) 1 1) * k (p l)
        + (v i * d1H h (p i, p j) 0 + v j * d1H h (p i, p j) 1) * (deriv k (p l) * u l)
        + (u i * d1H h (p i, p j) 0 + u j * d1H h (p i, p j) 1) * (deriv k (p l) * v l)
        + h (p i, p j) * (deriv (deriv k) (p l) * u l * v l) := by
  have hs := (hh.contDiffAt (x := (p i, p j))).isSymmSndFDerivAt (by simp)
  have L0 := (tw_line hh ((1 : ℝ), (0 : ℝ)) (prP i j p)).comp p (prP i j).hasFDerivAt
  have L1 := (tw_line hh ((0 : ℝ), (1 : ℝ)) (prP i j p)).comp p (prP i j).hasFDerivAt
  have K0 := fd_coord_i (x := p) l ((hk.differentiable (by simp)) (p l))
  have K1 := fd_coord_i (x := p) l (((contDiff_infty_iff_deriv.1 hk).2.differentiable (by simp)) (p l))
  have H := tw_has hh i j p
  rw [d2_of (F := fun y : Fin 4 → ℝ => h (y i, y j) * k (y l))
    ((hh.comp (prP i j).contDiff).mul (hk.comp (contDiff_apply ℝ ℝ l))) (fun y => twp_d1 hh i j hk l y v)
    (((((L0.const_mul (v i)).add (L1.const_mul (v j))).mul K0).add (H.mul (K1.mul_const (v l)))).congr_of_eventuallyEq
      (Eventually.of_forall fun y => by simp [d1H, eTV, prP_apply]))]
  simp only [add_apply, smul_apply, ContinuousLinearMap.comp_apply,
    ContinuousLinearMap.flip_apply, smul_eq_mul, ContinuousLinearMap.proj_apply, Pi.add_apply,
    Function.comp_apply]
  rw [prP_split i j u]
  simp only [map_add, map_smul, add_apply, smul_apply, smul_eq_mul]
  simp only [d1H, d2H, eTV, prP_apply, Matrix.cons_val_zero, Matrix.cons_val_one]
  rw [hs ((0 : ℝ), (1 : ℝ)) ((1 : ℝ), (0 : ℝ))]
  ring

end TwoVarRecipe


end ShadowProbe

#print axioms ShadowProbe.curv_smul_left
#print axioms ShadowProbe.curv_smul_middle
#print axioms ShadowProbe.curv_smul_right
#print axioms ShadowProbe.cov_model
#print axioms ShadowProbe.curv_model
#print axioms ShadowProbe.contMDiffCov_model
#print axioms ShadowProbe.scal_eq_sum
#print axioms ShadowProbe.curv_conf
#print axioms ShadowProbe.Rconf_eq_curv
#print axioms ShadowProbe.scal_conf
#print axioms ShadowProbe.trG_eq_sum
#print axioms ShadowProbe.einstein_conf
#print axioms ShadowProbe.hess_smul_left
#print axioms ShadowProbe.hess_smul_right
#print axioms ShadowProbe.hessConf_eq
#print axioms ShadowProbe.box_conf
#print axioms ShadowProbe.covT_smul_X
#print axioms ShadowProbe.covT_smul_Y
#print axioms ShadowProbe.covT_smul_Z
#print axioms ShadowProbe.sff_smul_X
#print axioms ShadowProbe.sff_smul_Y
#print axioms ShadowProbe.sff_symm
#print axioms ShadowProbe.pullG_symm
#print axioms ShadowProbe.pullG_comp
#print axioms ShadowProbe.dsFlat_on
#print axioms ShadowProbe.dsFlat_pull
#print axioms ShadowProbe.nConf_unit
#print axioms ShadowProbe.sff_conf
#print axioms ShadowProbe.prodG_apply
#print axioms ShadowProbe.prodG_symm
#print axioms ShadowProbe.roundG_pos
#print axioms ShadowProbe.roundG_symm
#print axioms ShadowProbe.period_isCovering
#print axioms ShadowProbe.rot_card
#print axioms ShadowProbe.rot_free
#print axioms ShadowProbe.wseam_C1
#print axioms ShadowProbe.wseam_not_C2
#print axioms ShadowProbe.wick_bijOn
#print axioms ShadowProbe.koszul
#print axioms ShadowProbe.lc_unique
#print axioms ShadowProbe.covConf_torsion
#print axioms ShadowProbe.covConf_compatible
#print axioms ShadowProbe.covConf_isLeviCivita
#print axioms ShadowProbe.kosz_tensorial₁
#print axioms ShadowProbe.kosz_tensorial₃
#print axioms ShadowProbe.lcAux_apply
#print axioms ShadowProbe.lcConn_torsion
#print axioms ShadowProbe.lcConn_compat
#print axioms ShadowProbe.lcConn_unique
#print axioms ShadowProbe.flatCov_torsion
#print axioms ShadowProbe.flatCov_compat
#print axioms ShadowProbe.flat_isLeviCivita
#print axioms ShadowProbe.homothety_nabla
#print axioms ShadowProbe.homothety_charge
#print axioms ShadowProbe.rain_geodesic
#print axioms ShadowProbe.sds_rain_geodesic
#print axioms ShadowProbe.sinh23_flow
#print axioms ShadowProbe.surface_gravity
#print axioms ShadowProbe.kappa_half_fprime
#print axioms ShadowProbe.unitU_geodesic
#print axioms ShadowProbe.interior_chart
#print axioms ShadowProbe.cycloid_proper_time
#print axioms ShadowProbe.interior_geodesic
#print axioms ShadowProbe.killing_of_invariant
#print axioms ShadowProbe.gowdy_killing
#print axioms ShadowProbe.lcConn_const
#print axioms ShadowProbe.lcGam_smooth
#print axioms ShadowProbe.lcConn_contMDiffCov
#print axioms ShadowProbe.pg_contMDiffCov
#print axioms ShadowProbe.dg_contMDiffCov
#print axioms ShadowProbe.diag4_contMDiffCov
#print axioms ShadowProbe.pg_curv_smul_left
#print axioms ShadowProbe.fNar_hasDerivAt
#print axioms ShadowProbe.two_surface_gravities
#print axioms ShadowProbe.ds_horizon_iff
#print axioms ShadowProbe.ds_surface_gravity
#print axioms ShadowProbe.unruh_ds_limits
#print axioms ShadowProbe.lcGam_diag
#print axioms ShadowProbe.diag_curv
#print axioms ShadowProbe.slice_gauss
#print axioms ShadowProbe.sds_slice_gauss
#print axioms ShadowProbe.sds_flat_locus
#print axioms ShadowProbe.sds_nariai_iff
#print axioms ShadowProbe.sds_two_ranges
#print axioms ShadowProbe.accel_rKG
#print axioms ShadowProbe.sds_accel_is_rKG
#print axioms ShadowProbe.sds_balance_is_flat
#print axioms ShadowProbe.killing_lie
#print axioms ShadowProbe.xiPW_deriv
#print axioms ShadowProbe.pw_killing
#print axioms ShadowProbe.pw_bracket
#print axioms ShadowProbe.pw_wronskian_const
#print axioms ShadowProbe.pw_dv_null
#print axioms ShadowProbe.lcGam_diag3
#print axioms ShadowProbe.null_radial
#print axioms ShadowProbe.sds_photon_lyapunov
#print axioms ShadowProbe.lcGam_pp
#print axioms ShadowProbe.pp_ricci
#print axioms ShadowProbe.pw_ricci_flat
#print axioms ShadowProbe.pp_vacuum_iff
#print axioms ShadowProbe.pp_riemann
#print axioms ShadowProbe.pp_Ruxux
#print axioms ShadowProbe.pp_kretschmann
#print axioms ShadowProbe.lcGam_diag4
#print axioms ShadowProbe.conf_box
#print axioms ShadowProbe.ds_tt_mode
#print axioms ShadowProbe.mukhanov
#print axioms ShadowProbe.ds_app
#print axioms ShadowProbe.curv_T
#print axioms ShadowProbe.ds_invariants
#print axioms ShadowProbe.frw_scal
#print axioms ShadowProbe.layer_scal
#print axioms ShadowProbe.layer_late
#print axioms ShadowProbe.frw_weyl
#print axioms ShadowProbe.curvD_eq
#print axioms ShadowProbe.dC2_cS
#print axioms ShadowProbe.d2_of
#print axioms ShadowProbe.d2_indep
#print axioms ShadowProbe.exists_global_profile
#print axioms ShadowProbe.exists_global_family
#print axioms ShadowProbe.pr_d2
#print axioms ShadowProbe.tw_d1
#print axioms ShadowProbe.tw_d2
#print axioms ShadowProbe.twp_d1
#print axioms ShadowProbe.twp_d2

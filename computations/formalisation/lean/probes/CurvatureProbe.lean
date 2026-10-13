import Mathlib.Geometry.Manifold.VectorBundle.CovariantDerivative.Basic
import Mathlib.Geometry.Manifold.VectorBundle.Hom
import Mathlib.Geometry.Manifold.VectorBundle.Tangent
import Mathlib.Geometry.Manifold.VectorField.LieBracket
import Mathlib.LinearAlgebra.Trace
import Mathlib.LinearAlgebra.BilinearForm.Properties

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

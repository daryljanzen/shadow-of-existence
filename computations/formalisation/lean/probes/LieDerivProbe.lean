import Mathlib.Geometry.Manifold.VectorField.LieBracket
import Mathlib.Geometry.Manifold.VectorBundle.Tangent

/-!
# Probes P1–P3 of `r7269+71.1`: the Lie derivative of a metric, Killing and conformal-Killing fields, and I20's instance

**A measurement, not the start of the layer, and not the Levi-Civita port.** Nothing imports this file.

* **P1 (B1)** `lieDerivForm g X Y Z x = X(g(Y,Z)) − g([X,Y],Z) − g(Y,[X,Z])` at `x`, for a field of
  bilinear forms `g` on the tangent bundle. *The test fields enter through the formula and not through a
  tensor, so tensoriality (B2) is not needed to state it.*
* **P2 (B4, B5)** Killing and conformal-Killing, quantified over `C¹` test fields. The `C¹` choice is
  forced: `mathlib` has the model-space bridge for `ContMDiff` sections
  (`contMDiffAt_vectorSpace_iff_contDiffAt`) and not for `MDifferentiable` ones.
* **P3 (B8)** on `ℝ × ℝ`, with `g = a(η)² (−dη² + dx²)`, `ξ = ∂_η` is conformal Killing with
  `σ = a′/a`, at every point where `a` is differentiable and nonzero.
-/

open Manifold VectorField
open scoped ContDiff

namespace ShadowProbe

section General

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
  {H : Type*} [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  {M : Type*} [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 1 M]

/-- **P1 (B1).** The Lie derivative of a field of bilinear forms, evaluated on test fields. -/
noncomputable def lieDerivForm (g : Π x : M, TangentSpace I x →L[ℝ] TangentSpace I x →L[ℝ] ℝ)
    (X Y Z : Π x : M, TangentSpace I x) (x : M) : ℝ :=
  (show ℝ from mfderiv I 𝓘(ℝ, ℝ) (fun y => g y (Y y) (Z y)) x (X x))
    - g x (mlieBracket I X Y x) (Z x) - g x (Y x) (mlieBracket I X Z x)

/-- **P2 (B5).** `X` is conformal Killing for `g` with factor `σ`. -/
def IsConformalKilling (g : Π x : M, TangentSpace I x →L[ℝ] TangentSpace I x →L[ℝ] ℝ)
    (X : Π x : M, TangentSpace I x) (σ : M → ℝ) (x : M) : Prop :=
  ∀ Y Z : Π x : M, TangentSpace I x, CMDiffAt 1 (T% Y) x → CMDiffAt 1 (T% Z) x →
    lieDerivForm g X Y Z x = 2 * σ x * g x (Y x) (Z x)

/-- **P2 (B4).** `X` is Killing for `g`: conformal Killing with factor `0`. -/
def IsKilling (g : Π x : M, TangentSpace I x →L[ℝ] TangentSpace I x →L[ℝ] ℝ)
    (X : Π x : M, TangentSpace I x) (x : M) : Prop :=
  IsConformalKilling g X 0 x

theorem isKilling_iff (g : Π x : M, TangentSpace I x →L[ℝ] TangentSpace I x →L[ℝ] ℝ)
    (X : Π x : M, TangentSpace I x) (x : M) :
    IsKilling g X x ↔ ∀ Y Z : Π x : M, TangentSpace I x, CMDiffAt 1 (T% Y) x →
      CMDiffAt 1 (T% Z) x → lieDerivForm g X Y Z x = 0 := by
  simp [IsKilling, IsConformalKilling]

end General

section Instance

/-- `−dη² + dx²` on `ℝ × ℝ`, as a continuous bilinear form. -/
noncomputable def minkForm : ℝ × ℝ →L[ℝ] ℝ × ℝ →L[ℝ] ℝ :=
  -((ContinuousLinearMap.mul ℝ ℝ).bilinearComp (ContinuousLinearMap.fst ℝ ℝ ℝ)
      (ContinuousLinearMap.fst ℝ ℝ ℝ))
    + (ContinuousLinearMap.mul ℝ ℝ).bilinearComp (ContinuousLinearMap.snd ℝ ℝ ℝ)
      (ContinuousLinearMap.snd ℝ ℝ ℝ)

lemma minkForm_apply (v w : ℝ × ℝ) : minkForm v w = -(v.1 * w.1) + v.2 * w.2 := by
  simp [minkForm]

/-- I20's metric `a(η)² (−dη² + dx²)` on `ℝ × ℝ`, `η` the first coordinate. -/
noncomputable def gConf (a : ℝ → ℝ) :
    Π p : ℝ × ℝ, TangentSpace 𝓘(ℝ, ℝ × ℝ) p →L[ℝ] TangentSpace 𝓘(ℝ, ℝ × ℝ) p →L[ℝ] ℝ :=
  fun p => (a p.1 ^ 2) • minkForm

/-- `ξ = ∂_η`. -/
def xi : Π p : ℝ × ℝ, TangentSpace 𝓘(ℝ, ℝ × ℝ) p := fun _ => ((1 : ℝ), (0 : ℝ))

/-- **P3 (B8).** `∂_η` is conformal Killing for `a(η)² (−dη² + dx²)` with `σ = a′/a`, at every point
where `a` is differentiable and nonzero. -/
lemma gConf_apply (a : ℝ → ℝ) (p v w : ℝ × ℝ) :
    gConf a p v w = a p.1 ^ 2 * (-(v.1 * w.1) + v.2 * w.2) := by
  simp only [gConf, ContinuousLinearMap.smul_apply, smul_eq_mul, minkForm_apply]
  rfl

theorem xi_isConformalKilling (a : ℝ → ℝ) (p : ℝ × ℝ) (hd : DifferentiableAt ℝ a p.1)
    (ha : a p.1 ≠ 0) :
    IsConformalKilling (gConf a) xi (fun q => deriv a q.1 / a q.1) p := by
  intro Y Z hY hZ
  rw [contMDiffAt_vectorSpace_iff_contDiffAt] at hY hZ
  -- on the model space a vector field is a function `E → E`; name it as one throughout
  obtain ⟨Y', rfl⟩ : ∃ Y' : ℝ × ℝ → ℝ × ℝ, Y' = Y := ⟨Y, rfl⟩
  obtain ⟨Z', rfl⟩ : ∃ Z' : ℝ × ℝ → ℝ × ℝ, Z' = Z := ⟨Z, rfl⟩
  have hYd : DifferentiableAt ℝ Y' p := hY.differentiableAt (by norm_num)
  have hZd : DifferentiableAt ℝ Z' p := hZ.differentiableAt (by norm_num)
  -- the bracket on the model space is the vector-space bracket, and `ξ` is constant
  have hxi : fderiv ℝ (xi : ℝ × ℝ → ℝ × ℝ) p = 0 := by
    show fderiv ℝ (fun _ : ℝ × ℝ => ((1 : ℝ), (0 : ℝ))) p = 0
    simp
  have hbr : ∀ W : Π q : ℝ × ℝ, TangentSpace 𝓘(ℝ, ℝ × ℝ) q,
      mlieBracket 𝓘(ℝ, ℝ × ℝ) xi W p = fderiv ℝ (W : ℝ × ℝ → ℝ × ℝ) p ((1 : ℝ), (0 : ℝ)) := by
    intro W
    rw [← mlieBracketWithin_univ, mlieBracketWithin_eq_lieBracketWithin]
    set W' : ℝ × ℝ → ℝ × ℝ := W
    set xi' : ℝ × ℝ → ℝ × ℝ := xi
    show fderivWithin ℝ W' Set.univ p (xi' p) - fderivWithin ℝ xi' Set.univ p (W' p) = _
    rw [fderivWithin_univ, fderivWithin_univ, hxi]
    simp [xi', xi]
  -- the derivative of `g(Y,Z)` along `ξ`
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
  have hm : (show ℝ from mfderiv 𝓘(ℝ, ℝ × ℝ) 𝓘(ℝ, ℝ) (fun y => gConf a y (Y' y) (Z' y)) p (xi p))
      = fderiv ℝ ((fun q : ℝ × ℝ => a q.1 ^ 2) *
          (-(Prod.fst ∘ Y' * Prod.fst ∘ Z') + Prod.snd ∘ Y' * Prod.snd ∘ Z')) p
          ((1 : ℝ), (0 : ℝ)) := by
    rw [mfderiv_eq_fderiv]
    have hfun : (fun y : ℝ × ℝ => gConf a y (Y' y) (Z' y)) =
        ((fun q : ℝ × ℝ => a q.1 ^ 2) *
          (-(Prod.fst ∘ Y' * Prod.fst ∘ Z') + Prod.snd ∘ Y' * Prod.snd ∘ Z')) := by
      funext q
      simp [gConf_apply]
    rw [hfun]
    rfl
  unfold lieDerivForm
  rw [hm, hbr Y', hbr Z', hh.fderiv]
  simp only [gConf_apply]
  simp [Function.comp_def]
  field_simp
  ring

end Instance

end ShadowProbe

#print axioms ShadowProbe.isKilling_iff
#print axioms ShadowProbe.xi_isConformalKilling

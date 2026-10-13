import Mathlib.Geometry.Manifold.VectorField.LieBracket
import Mathlib.Geometry.Manifold.VectorBundle.Tangent
import Mathlib.Geometry.Manifold.VectorBundle.CovariantDerivative.Torsion

/-!
# Probes Q1–Q3 of `r7273+71.1`: compatibility, and the `∇` form of the Lie derivative of a metric

**A measurement, not the Levi-Civita port.** Nothing imports this file. Nothing here touches
`LeviCivita.lean`, `Metric.lean` or the layer-1 probe. **The connection is a HYPOTHESIS**: any bundled
`CovariantDerivative` on `TM` that is torsion-free and compatible with `g`. So no existence is used.

`lieDerivForm` and `IsConformalKilling` are copied verbatim from `LieDerivProbe.lean` (`r7269+71.2`),
because probes are not a library and do not import each other.

* **Q1 (B1)** `IsCompatible g cov x`: `X(g(Y,Z)) = g(∇_X Y, Z) + g(Y, ∇_X Z)` at `x`, over `C¹` fields.
* **Q2 (B4)** for torsion-free compatible `cov`: `(𝓛_X g)(Y,Z) = g(∇_Y X, Z) + g(Y, ∇_Z X)`.
* **Q3 (B5)** hence `ξ` conformal Killing gives `g(∇_Y ξ, Z) + g(Y, ∇_Z ξ) = 2σ g(Y,Z)`.

`mathlib` writes `cov σ x (X x)` for `∇_X σ` at `x`.
-/

open Manifold VectorField
open scoped ContDiff

namespace ShadowProbe

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [CompleteSpace E]
  [FiniteDimensional ℝ E]
  {H : Type*} [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  {M : Type*} [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 2 M]

/-- Copied from `LieDerivProbe.lean`. -/
noncomputable def lieDerivForm (g : Π x : M, TangentSpace I x →L[ℝ] TangentSpace I x →L[ℝ] ℝ)
    (X Y Z : Π x : M, TangentSpace I x) (x : M) : ℝ :=
  (show ℝ from mfderiv I 𝓘(ℝ, ℝ) (fun y => g y (Y y) (Z y)) x (X x))
    - g x (mlieBracket I X Y x) (Z x) - g x (Y x) (mlieBracket I X Z x)

/-- Copied from `LieDerivProbe.lean`. -/
def IsConformalKilling (g : Π x : M, TangentSpace I x →L[ℝ] TangentSpace I x →L[ℝ] ℝ)
    (X : Π x : M, TangentSpace I x) (σ : M → ℝ) (x : M) : Prop :=
  ∀ Y Z : Π x : M, TangentSpace I x, CMDiffAt 1 (T% Y) x → CMDiffAt 1 (T% Z) x →
    lieDerivForm g X Y Z x = 2 * σ x * g x (Y x) (Z x)

/-- **Q1 (B1).** `cov` is compatible with the field of forms `g` at `x`. -/
def IsCompatible (g : Π x : M, TangentSpace I x →L[ℝ] TangentSpace I x →L[ℝ] ℝ)
    (cov : CovariantDerivative I E (TangentSpace I : M → Type _)) (x : M) : Prop :=
  ∀ X Y Z : Π x : M, TangentSpace I x, CMDiffAt 1 (T% X) x → CMDiffAt 1 (T% Y) x →
    CMDiffAt 1 (T% Z) x →
    (show ℝ from mfderiv I 𝓘(ℝ, ℝ) (fun y => g y (Y y) (Z y)) x (X x))
      = g x (cov Y x (X x)) (Z x) + g x (Y x) (cov Z x (X x))

/-- **Q2 (B4).** For a torsion-free connection compatible with `g`,
`(𝓛_X g)(Y,Z) = g(∇_Y X, Z) + g(Y, ∇_Z X)`. -/
theorem lieDerivForm_eq_cov (g : Π x : M, TangentSpace I x →L[ℝ] TangentSpace I x →L[ℝ] ℝ)
    (cov : CovariantDerivative I E (TangentSpace I : M → Type _)) (htor : cov.torsion = 0)
    {x : M} (hcomp : IsCompatible g cov x)
    {X Y Z : Π x : M, TangentSpace I x} (hX : CMDiffAt 1 (T% X) x) (hY : CMDiffAt 1 (T% Y) x)
    (hZ : CMDiffAt 1 (T% Z) x) :
    lieDerivForm g X Y Z x = g x (cov X x (Y x)) (Z x) + g x (Y x) (cov X x (Z x)) := by
  have hXd : MDiffAt (T% X) x := hX.mdifferentiableAt (by norm_num)
  have hYd : MDiffAt (T% Y) x := hY.mdifferentiableAt (by norm_num)
  have hZd : MDiffAt (T% Z) x := hZ.mdifferentiableAt (by norm_num)
  -- torsion-free: `[X,Y] = ∇_X Y − ∇_Y X`
  have hXY : mlieBracket I X Y x = cov Y x (X x) - cov X x (Y x) := by
    have h := cov.torsion_apply hXd hYd
    rw [htor] at h
    simp only [Pi.zero_apply, ContinuousLinearMap.zero_apply] at h
    first
      | exact (sub_eq_zero.mp h).symm
      | exact (sub_eq_zero.mp h.symm).symm
  have hXZ : mlieBracket I X Z x = cov Z x (X x) - cov X x (Z x) := by
    have h := cov.torsion_apply hXd hZd
    rw [htor] at h
    simp only [Pi.zero_apply, ContinuousLinearMap.zero_apply] at h
    first
      | exact (sub_eq_zero.mp h).symm
      | exact (sub_eq_zero.mp h.symm).symm
  unfold lieDerivForm
  rw [hcomp X Y Z hX hY hZ, hXY, hXZ]
  simp only [map_sub, ContinuousLinearMap.sub_apply]
  ring

/-- **Q3 (B5).** A conformal Killing field, in `∇` form. -/
theorem conformalKilling_cov (g : Π x : M, TangentSpace I x →L[ℝ] TangentSpace I x →L[ℝ] ℝ)
    (cov : CovariantDerivative I E (TangentSpace I : M → Type _)) (htor : cov.torsion = 0)
    {x : M} (hcomp : IsCompatible g cov x) {ξ : Π x : M, TangentSpace I x} {σ : M → ℝ}
    (hξ : CMDiffAt 1 (T% ξ) x) (hck : IsConformalKilling g ξ σ x)
    {Y Z : Π x : M, TangentSpace I x} (hY : CMDiffAt 1 (T% Y) x) (hZ : CMDiffAt 1 (T% Z) x) :
    g x (cov ξ x (Y x)) (Z x) + g x (Y x) (cov ξ x (Z x)) = 2 * σ x * g x (Y x) (Z x) := by
  rw [← lieDerivForm_eq_cov g cov htor hcomp hξ hY hZ]
  exact hck Y Z hY hZ

end ShadowProbe

#print axioms ShadowProbe.lieDerivForm_eq_cov
#print axioms ShadowProbe.conformalKilling_cov

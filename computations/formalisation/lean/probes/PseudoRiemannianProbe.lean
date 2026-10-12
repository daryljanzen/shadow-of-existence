import Mathlib.Geometry.Manifold.VectorBundle.Riemannian

/-!
# Probe — B1 of `r7267+71.1`: a pseudo-Riemannian metric structure, against `mathlib` `4e6064a4`

**A measurement, not the start of the Lorentzian layer.** Nothing imports this file, and
`ShadowFormal` does not build on it. It answers one question of the pre-registration: is B1 writable
as a `structure` over machinery `mathlib` already has, with its one proof obligation discharged by
existing lemmas? It is `ContMDiffRiemannianMetric` with `pos` and `isVonNBounded` replaced by
nondegeneracy. `isVonNBounded` exists only to make the inner product's norm agree with the fibre
topology, and an indefinite form defines no norm.
-/

open Bundle Manifold
open scoped ContDiff

namespace ShadowProbe

variable
  {EB : Type*} [NormedAddCommGroup EB] [NormedSpace ℝ EB]
  {HB : Type*} [TopologicalSpace HB] (IB : ModelWithCorners ℝ EB HB) (n : ℕ∞ω)
  {B : Type*} [TopologicalSpace B] [ChartedSpace HB B]
  (F : Type*) [NormedAddCommGroup F] [NormedSpace ℝ F]
  (E : B → Type*) [TopologicalSpace (TotalSpace F E)]
  [∀ b, TopologicalSpace (E b)] [∀ b, AddCommGroup (E b)] [∀ b, Module ℝ (E b)]
  [∀ b, IsTopologicalAddGroup (E b)] [∀ b, ContinuousConstSMul ℝ (E b)]
  [FiberBundle F E] [VectorBundle ℝ F E]

/-- B1: a smooth, fibrewise symmetric, nondegenerate bilinear form on a vector bundle. -/
structure ContMDiffPseudoRiemannianMetric where
  inner (b : B) : E b →L[ℝ] E b →L[ℝ] ℝ
  symm (b : B) (v w : E b) : inner b v w = inner b w v
  nondegenerate (b : B) (v : E b) (hv : ∀ w, inner b v w = 0) : v = 0
  contMDiff : ContMDiff IB (IB.prod 𝓘(ℝ, F →L[ℝ] F →L[ℝ] ℝ)) n
    (fun b ↦ TotalSpace.mk' (F →L[ℝ] F →L[ℝ] ℝ) b (inner b))

variable {IB n F E}

/-- The one proof obligation: every smooth Riemannian metric is a pseudo-Riemannian one.
Nondegeneracy comes from `pos` applied to `v` itself. -/
def ofRiemannian (g : ContMDiffRiemannianMetric IB n F E) :
    ContMDiffPseudoRiemannianMetric IB n F E where
  inner := g.inner
  symm := g.symm
  nondegenerate b v hv := by
    by_contra h
    exact (g.pos b v h).ne' (hv v)
  contMDiff := g.contMDiff

/-- A theorem about the probe, so `#print axioms` has something to read. -/
theorem ofRiemannian_inner (g : ContMDiffRiemannianMetric IB n F E) (b : B) :
    (ofRiemannian g).inner b = g.inner b := rfl

end ShadowProbe

#print axioms ShadowProbe.ofRiemannian
#print axioms ShadowProbe.ofRiemannian_inner

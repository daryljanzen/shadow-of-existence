import Mathlib.Geometry.Manifold.IntegralCurve.ExistUnique
import Mathlib.Geometry.Manifold.IntegralCurve.Transform

/-!
# Probe T3a of `r7281+71.1`: the local flow of a `C¹` vector field, and its group law

Classed THEORY at `r7269+71.2` (A5, "a flow with a group law"), unprobed. This probe splits off the group
law. Smooth dependence on the initial point is T3b and is not here.

`flow hv t x` is the chosen local integral curve through `x`, from `mathlib`'s existence theorem, read at
time `t`. The group law is local: for each `x`, for `s` near `0`, for `t` near `0`,
`flow (s + t) x = flow t (flow s x)`. The proof is `mathlib`'s local uniqueness of integral curves
applied to two integral curves through `flow s x`. Nothing imports this file.
-/

open Manifold Filter Topology

namespace ShadowProbe

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [CompleteSpace E]
  {H : Type*} [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  {M : Type*} [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 1 M] [BoundarylessManifold I M]
  {v : (x : M) → TangentSpace I x}

/-- The chosen local integral curve through `x`, at time `0`. -/
noncomputable def flowCurve (hv : ∀ x, CMDiffAt 1 (fun x ↦ (⟨x, v x⟩ : TangentBundle I M)) x)
    (x : M) : ℝ → M :=
  Classical.choose (exists_isMIntegralCurveAt_of_contMDiffAt_boundaryless 0 (hv x))

lemma flowCurve_spec (hv : ∀ x, CMDiffAt 1 (fun x ↦ (⟨x, v x⟩ : TangentBundle I M)) x) (x : M) :
    flowCurve hv x 0 = x ∧ IsMIntegralCurveAt (flowCurve hv x) v 0 :=
  Classical.choose_spec (exists_isMIntegralCurveAt_of_contMDiffAt_boundaryless 0 (hv x))

/-- **T3a.** The local flow. -/
noncomputable def flow (hv : ∀ x, CMDiffAt 1 (fun x ↦ (⟨x, v x⟩ : TangentBundle I M)) x)
    (t : ℝ) (x : M) : M :=
  flowCurve hv x t

/-- **T3a.** The local group law: `flow (s + t) x = flow t (flow s x)` for `s` and `t` near `0`. -/
theorem flow_add (hv : ∀ x, CMDiffAt 1 (fun x ↦ (⟨x, v x⟩ : TangentBundle I M)) x) (x : M) :
    ∀ᶠ s in 𝓝 (0 : ℝ), ∀ᶠ t in 𝓝 (0 : ℝ), flow hv (s + t) x = flow hv t (flow hv s x) := by
  have h := (flowCurve_spec hv x).2
  filter_upwards [Filter.Eventually.eventually_nhds h] with s hs
  -- `t ↦ γ (t + s)` is an integral curve through `γ s` at time `0`
  have hshift : IsMIntegralCurveAt (flowCurve hv x ∘ (· + s)) v 0 := by
    simpa using (show IsMIntegralCurveAt (flowCurve hv x) v s from hs).comp_add s
  set y := flowCurve hv x s
  have hδ := flowCurve_spec hv y
  have heq := isMIntegralCurveAt_eventuallyEq_of_contMDiffAt_boundaryless
    (hv (flowCurve hv y 0)) hδ.2 hshift (by simp [hδ.1, y])
  filter_upwards [heq] with t ht
  simp only [flow, Function.comp_apply] at ht ⊢
  rw [ht, add_comm]

end ShadowProbe

#print axioms ShadowProbe.flow_add

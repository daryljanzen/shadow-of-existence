import Mathlib.Geometry.Manifold.VectorField.LieBracket
import Mathlib.Geometry.Manifold.VectorBundle.CovariantDerivative.Torsion
import Mathlib.Geometry.Manifold.VectorBundle.Tangent

/-!
# Probe R3 of `r7277+71.1`: a torsion-free connection compatible with `a(η)²(−dη² + dx²)` on `ℝ × ℝ`

**One connection for one metric, constructed from a formula. Not the general existence theorem, and not
the Levi-Civita port.** Nothing imports this file; nothing touches `LeviCivita.lean` or `Metric.lean`.

With `φ′ = a′/a` (the derivative of `log a`, a function of `η` alone), the Christoffel form of the
conformally flat metric `a² η` is

    Γ(v, w) = φ′ · (v₁ w + w₁ v + η(v, w) e₁),        e₁ = ∂_η,

and `∇_v Y = DY(v) + Γ(v, Y)`. It is symmetric, so torsion-free; compatibility is the identity
`η(Γ(X,Y),Z) + η(Y,Γ(X,Z)) = 2 φ′ X₁ η(Y,Z)`.

Hypotheses, where used: `a` differentiable everywhere and nonzero everywhere (for the connection to be
one object), and differentiable at the point for compatibility.
-/

open Manifold VectorField Bundle
open scoped ContDiff

namespace ShadowProbe

/-- `−dη² + dx²`. Copied from `LieDerivProbe.lean`. -/
noncomputable def minkForm : ℝ × ℝ →L[ℝ] ℝ × ℝ →L[ℝ] ℝ :=
  -((ContinuousLinearMap.mul ℝ ℝ).bilinearComp (ContinuousLinearMap.fst ℝ ℝ ℝ)
      (ContinuousLinearMap.fst ℝ ℝ ℝ))
    + (ContinuousLinearMap.mul ℝ ℝ).bilinearComp (ContinuousLinearMap.snd ℝ ℝ ℝ)
      (ContinuousLinearMap.snd ℝ ℝ ℝ)

lemma minkForm_apply (v w : ℝ × ℝ) : minkForm v w = -(v.1 * w.1) + v.2 * w.2 := by
  simp [minkForm]

/-- `a(η)² (−dη² + dx²)`. Copied from `LieDerivProbe.lean`. -/
noncomputable def gConf (a : ℝ → ℝ) :
    Π p : ℝ × ℝ, TangentSpace 𝓘(ℝ, ℝ × ℝ) p →L[ℝ] TangentSpace 𝓘(ℝ, ℝ × ℝ) p →L[ℝ] ℝ :=
  fun p => (a p.1 ^ 2) • minkForm

lemma gConf_apply (a : ℝ → ℝ) (p v w : ℝ × ℝ) :
    gConf a p v w = a p.1 ^ 2 * (-(v.1 * w.1) + v.2 * w.2) := by
  simp only [gConf, ContinuousLinearMap.smul_apply, smul_eq_mul, minkForm_apply]
  rfl

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

section General

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [CompleteSpace E]
  [FiniteDimensional ℝ E]
  {H : Type*} [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  {M : Type*} [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 2 M]

/-- Copied from `ConnectionProbe.lean`: `cov` is compatible with the field of forms `g` at `x`. -/
def IsCompatible (g : Π x : M, TangentSpace I x →L[ℝ] TangentSpace I x →L[ℝ] ℝ)
    (cov : CovariantDerivative I E (TangentSpace I : M → Type _)) (x : M) : Prop :=
  ∀ X Y Z : Π x : M, TangentSpace I x, CMDiffAt 1 (T% X) x → CMDiffAt 1 (T% Y) x →
    CMDiffAt 1 (T% Z) x →
    (show ℝ from mfderiv I 𝓘(ℝ, ℝ) (fun y => g y (Y y) (Z y)) x (X x))
      = g x (cov Y x (X x)) (Z x) + g x (Y x) (cov Z x (X x))

end General

/-- **R3 (B8), part 3.** It is compatible with `a(η)²(−dη² + dx²)` wherever `a` is differentiable and
nonzero. -/
theorem covConf_compatible (a : ℝ → ℝ) (p : ℝ × ℝ) (hd : DifferentiableAt ℝ a p.1)
    (ha : a p.1 ≠ 0) : IsCompatible (gConf a) (covConf a) p := by
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

end ShadowProbe

#print axioms ShadowProbe.covConf
#print axioms ShadowProbe.covConf_torsion
#print axioms ShadowProbe.covConf_compatible

import Mathlib.Geometry.Manifold.VectorBundle.CovariantDerivative.Basic
import Mathlib.Geometry.Manifold.VectorBundle.LocalFrame
import Mathlib.Geometry.Manifold.VectorBundle.Tangent
import Mathlib.Analysis.Calculus.Deriv.Add
import Mathlib.Analysis.Calculus.Deriv.Mul

/-!
# Probes Q4–Q5 of `r7273+71.1`: the covariant derivative along a curve

**A measurement, not the Levi-Civita port.** Nothing imports this file. `cov` is any bundled
covariant derivative on `TM`; no metric and no existence theorem is used.

* **Q4 (B6)** `covDerivAlong cov γ V t`: expand `V` in the local frame of the trivialisation at `γ t`
  and differentiate the coefficients along `γ`:
  `D/dt V = ∑ᵢ (cᵢ ∘ γ)′ sᵢ + cᵢ ∇_γ̇ sᵢ`.
* **Q5 (B8)** for a `C¹` vector field `X` near `γ t`: `D/dt (X ∘ γ) = ∇_γ̇ X`.
-/

open Bundle Manifold Filter Set FiberBundle
open scoped ContDiff

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

/-- `cov` is additive over a finite sum of differentiable sections. -/
lemma cov_sum (cov : CovariantDerivative I E (TangentSpace I : M → Type _)) {ι : Type*}
    (s : Finset ι) (σ : ι → Π x : M, TangentSpace I x) {x : M}
    (h : ∀ i ∈ s, MDiffAt (T% (σ i)) x) :
    cov (∑ i ∈ s, σ i) x = ∑ i ∈ s, cov (σ i) x := by
  classical
  induction s using Finset.induction_on with
  | empty => simp
  | insert j s hj ih =>
    have hrest : MDiffAt (T% (∑ i ∈ s, σ i)) x := by
      have := MDifferentiableAt.sum_section (fun i hi => h i (Finset.mem_insert_of_mem hi))
      convert this using 3 with y
      simp [Finset.sum_apply]
    rw [Finset.sum_insert hj, Finset.sum_insert hj,
      cov.isCovariantDerivativeOn.add (h j (Finset.mem_insert_self j s)) hrest,
      ih (fun i hi => h i (Finset.mem_insert_of_mem hi))]

set_option backward.isDefEq.respectTransparency false in
/-- **Q5 (B8).** Along a curve, `D/dt (X ∘ γ) = ∇_γ̇ X`. -/
theorem covDerivAlong_comp (cov : CovariantDerivative I E (TangentSpace I : M → Type _))
    (γ : ℝ → M) (t : ℝ) (hγ : MDifferentiableAt 𝓘(ℝ, ℝ) I γ t)
    (X : Π x : M, TangentSpace I x) (hX : CMDiffAt 1 (T% X) (γ t)) :
    covDerivAlong cov γ (fun s => X (γ s)) t = cov X (γ t) (vel γ t) := by
  set e := trivializationAt E (TangentSpace I : M → Type _) (γ t) with he
  set b := Module.finBasis ℝ E with hb
  have hx : γ t ∈ e.baseSet := FiberBundle.mem_baseSet_trivializationAt' (γ t)
  set c : Fin (Module.finrank ℝ E) → M → ℝ :=
    fun i x => e.localFrameCoeff I b i x (X x) with hcdef
  have hc : ∀ i, MDiffAt (c i) (γ t) := fun i =>
    (contMDiffAt_localFrameCoeff (k := 1) b hx hX i).mdifferentiableAt (by norm_num)
  have hs : ∀ i, MDiffAt (T% (e.localFrame b i)) (γ t) := fun i =>
    (contMDiffAt_localFrame_of_mem (n := 1) (e := e) (b := b) i hx).mdifferentiableAt
      (by norm_num)
  have hterm : ∀ i ∈ (Finset.univ : Finset (Fin (Module.finrank ℝ E))),
      MDiffAt (T% (c i • e.localFrame b i)) (γ t) := fun i _ =>
    (hc i).smul_section (hs i)
  have hsum : MDiffAt (T% (∑ i, c i • e.localFrame b i)) (γ t) := by
    have := MDifferentiableAt.sum_section hterm
    convert this using 3 with y
    simp [Finset.sum_apply]
  have hev : ∀ᶠ y in nhds (γ t), X y = (∑ i, c i • e.localFrame b i) y := by
    filter_upwards [e.open_baseSet.mem_nhds hx] with y hy
    rw [Finset.sum_apply]
    exact e.eq_sum_localFrameCoeff_smul hy
  -- the derivative of each coefficient along `γ`
  have hderiv : ∀ i, deriv (fun s => c i (γ s)) t = mfderiv I 𝓘(ℝ, ℝ) (c i) (γ t) (vel γ t) := by
    intro i
    have h1 := (hc i).hasMFDerivAt.comp t hγ.hasMFDerivAt
    calc deriv (fun s => c i (γ s)) t
        = mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, ℝ) (c i ∘ γ) t (show TangentSpace 𝓘(ℝ, ℝ) t from (1 : ℝ)) := by
          rw [mfderiv_eq_fderiv, ← fderiv_apply_one_eq_deriv]
          rfl
      _ = mfderiv I 𝓘(ℝ, ℝ) (c i) (γ t) (vel γ t) := by
          rw [h1.mfderiv]
          rfl
  -- the right-hand side, expanded in the frame
  rw [cov.isCovariantDerivativeOn.congr_of_eventuallyEq (hX.mdifferentiableAt (by norm_num)) (σ' := ∑ i, c i •
      e.localFrame b i) hsum univ_mem hev, cov_sum cov _ _ hterm]
  simp only [ContinuousLinearMap.sum_apply]
  unfold covDerivAlong
  apply Finset.sum_congr rfl
  intro i _
  rw [cov.isCovariantDerivativeOn.leibniz (hs i) (hc i)]
  simp only [ContinuousLinearMap.add_apply, ContinuousLinearMap.smul_apply,
    ContinuousLinearMap.smulRight_apply]
  rw [add_comm]
  congr 1
  congr 1
  exact hderiv i


/-- Copied from `ConnectionProbe.lean`: `cov` is compatible with the field of forms `g` at `x`. -/
def IsCompatible (g : Π x : M, TangentSpace I x →L[ℝ] TangentSpace I x →L[ℝ] ℝ)
    (cov : CovariantDerivative I E (TangentSpace I : M → Type _)) (x : M) : Prop :=
  ∀ X Y Z : Π x : M, TangentSpace I x, CMDiffAt 1 (T% X) x → CMDiffAt 1 (T% Y) x →
    CMDiffAt 1 (T% Z) x →
    (show ℝ from mfderiv I 𝓘(ℝ, ℝ) (fun y => g y (Y y) (Z y)) x (X x))
      = g x (cov Y x (X x)) (Z x) + g x (Y x) (cov Z x (X x))

/-- A tangent vector at a point of the trivialisation's base set is the sum of its frame components. -/
lemma vec_expand {x₀ x : M}
    (hx : x ∈ (trivializationAt E (TangentSpace I : M → Type _) x₀).baseSet)
    (v : TangentSpace I x) :
    v = ∑ i, (trivializationAt E (TangentSpace I : M → Type _) x₀).localFrameCoeff I
      (Module.finBasis ℝ E) i x v •
      (trivializationAt E (TangentSpace I : M → Type _) x₀).localFrame (Module.finBasis ℝ E) i x := by
  have := (trivializationAt E (TangentSpace I : M → Type _) x₀).eq_sum_localFrameCoeff_smul
    (I := I) (b := Module.finBasis ℝ E) (s := extend E v) hx
  simpa using this

set_option backward.isDefEq.respectTransparency false in
/-- **Q5 (B7).** Compatibility along a curve: `d/dt g(V,W) = g(DV/dt, W) + g(V, DW/dt)`. -/
theorem covDerivAlong_compat (g : Π x : M, TangentSpace I x →L[ℝ] TangentSpace I x →L[ℝ] ℝ)
    (cov : CovariantDerivative I E (TangentSpace I : M → Type _))
    (γ : ℝ → M) (t : ℝ) (hγ : MDifferentiableAt 𝓘(ℝ, ℝ) I γ t) (hcomp : IsCompatible g cov (γ t))
    (hg : ∀ Y Z : Π x : M, TangentSpace I x, CMDiffAt 1 (T% Y) (γ t) → CMDiffAt 1 (T% Z) (γ t) →
      MDiffAt (fun y => g y (Y y) (Z y)) (γ t))
    (V W : Π s : ℝ, TangentSpace I (γ s))
    (hV : ∀ i, DifferentiableAt ℝ (fun s => (trivializationAt E (TangentSpace I : M → Type _)
      (γ t)).localFrameCoeff I (Module.finBasis ℝ E) i (γ s) (V s)) t)
    (hW : ∀ i, DifferentiableAt ℝ (fun s => (trivializationAt E (TangentSpace I : M → Type _)
      (γ t)).localFrameCoeff I (Module.finBasis ℝ E) i (γ s) (W s)) t) :
    deriv (fun s => g (γ s) (V s) (W s)) t
      = g (γ t) (covDerivAlong cov γ V t) (W t) + g (γ t) (V t) (covDerivAlong cov γ W t) := by
  set e := trivializationAt E (TangentSpace I : M → Type _) (γ t) with he
  set b := Module.finBasis ℝ E with hb
  have hx : γ t ∈ e.baseSet := FiberBundle.mem_baseSet_trivializationAt' (γ t)
  set v : Fin (Module.finrank ℝ E) → ℝ → ℝ := fun i s => e.localFrameCoeff I b i (γ s) (V s)
  set w : Fin (Module.finrank ℝ E) → ℝ → ℝ := fun i s => e.localFrameCoeff I b i (γ s) (W s)
  set G : Fin (Module.finrank ℝ E) → Fin (Module.finrank ℝ E) → M → ℝ :=
    fun i j x => g x (e.localFrame b i x) (e.localFrame b j x)
  have hs : ∀ i, CMDiffAt 1 (T% (e.localFrame b i)) (γ t) := fun i =>
    contMDiffAt_localFrame_of_mem (n := 1) (e := e) (b := b) i hx
  -- the bilinear form on two frame expansions
  have hbil : ∀ (x : M) (a c : Fin (Module.finrank ℝ E) → ℝ),
      g x (∑ i, a i • e.localFrame b i x) (∑ j, c j • e.localFrame b j x)
        = ∑ i, ∑ j, a i * c j * G i j x := by
    intro x a c
    simp only [map_sum, map_smul, ContinuousLinearMap.sum_apply, ContinuousLinearMap.smul_apply,
      smul_eq_mul, G, Finset.mul_sum]
    rw [Finset.sum_comm]
    apply Finset.sum_congr rfl; intro i _; apply Finset.sum_congr rfl; intro j _; ring
  -- near `t`, the function is a finite sum of products
  have hnear : ∀ᶠ s in nhds t, γ s ∈ e.baseSet :=
    hγ.continuousAt.preimage_mem_nhds (e.open_baseSet.mem_nhds hx)
  have hexp : (fun s => g (γ s) (V s) (W s)) =ᶠ[nhds t]
      fun s => ∑ i, ∑ j, v i s * w j s * G i j (γ s) := by
    filter_upwards [hnear] with s hs'
    rw [← hbil, ← vec_expand hs' (V s), ← vec_expand hs' (W s)]
  -- each `G i j ∘ γ` has the derivative compatibility gives it
  have hGd : ∀ i j, HasDerivAt (fun s => G i j (γ s))
      (g (γ t) (cov (e.localFrame b i) (γ t) (vel γ t)) (e.localFrame b j (γ t))
        + g (γ t) (e.localFrame b i (γ t)) (cov (e.localFrame b j) (γ t) (vel γ t))) t := by
    intro i j
    have hGm : MDiffAt (G i j) (γ t) := hg _ _ (hs i) (hs j)
    have h1 := hGm.hasMFDerivAt.comp t hγ.hasMFDerivAt
    have hd : DifferentiableAt ℝ (fun s => G i j (γ s)) t :=
      mdifferentiableAt_iff_differentiableAt.mp (hGm.comp t hγ)
    have hval : deriv (fun s => G i j (γ s)) t = mfderiv I 𝓘(ℝ, ℝ) (G i j) (γ t) (vel γ t) := by
      calc deriv (fun s => G i j (γ s)) t
          = mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, ℝ) (G i j ∘ γ) t (show TangentSpace 𝓘(ℝ, ℝ) t from (1 : ℝ)) := by
            rw [mfderiv_eq_fderiv, ← fderiv_apply_one_eq_deriv]
            rfl
        _ = _ := by rw [h1.mfderiv]; rfl
    have hc := hcomp (extend E (vel γ t)) (e.localFrame b i) (e.localFrame b j)
      (contMDiffAt_extend I E (vel γ t)) (hs i) (hs j)
    simp only [extend_apply_self] at hc
    have := hd.hasDerivAt
    rw [hval] at this
    convert this using 1
    exact hc.symm
  have hsum := HasDerivAt.fun_sum (u := Finset.univ) (fun i _ => HasDerivAt.fun_sum
    (u := Finset.univ) (fun j _ => (((hV i).hasDerivAt.fun_mul (hW j).hasDerivAt).fun_mul (hGd i j))))
  -- the right-hand side, expanded in the frame (only there: `V t` also sits inside `v i t`)
  conv_rhs => rw [vec_expand hx (W t), vec_expand hx (V t)]
  rw [hexp.deriv_eq, hsum.deriv]
  unfold covDerivAlong
  simp only [← he, ← hb]
  simp only [map_sum, map_add, map_smul, ContinuousLinearMap.sum_apply,
    ContinuousLinearMap.add_apply, ContinuousLinearMap.smul_apply, smul_eq_mul]
  simp only [← Finset.sum_add_distrib, Finset.mul_sum]
  conv_rhs => rw [Finset.sum_comm]
  apply Finset.sum_congr rfl; intro i _; apply Finset.sum_congr rfl; intro j _
  simp only [← he, v, w, G]
  ring

end ShadowProbe

#print axioms ShadowProbe.covDerivAlong_comp
#print axioms ShadowProbe.covDerivAlong_compat

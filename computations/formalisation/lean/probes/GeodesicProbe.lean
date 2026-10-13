import Mathlib.Geometry.Manifold.VectorField.LieBracket
import Mathlib.Geometry.Manifold.VectorBundle.CovariantDerivative.Torsion
import Mathlib.Geometry.Manifold.VectorBundle.LocalFrame
import Mathlib.Geometry.Manifold.VectorBundle.Tangent
import Mathlib.Analysis.Calculus.Deriv.Add
import Mathlib.Analysis.Calculus.Deriv.Mul
import Mathlib.Analysis.Calculus.MeanValue

/-!
# Probes R1–R2 of `r7277+71.1`: the geodesic, the charge, and its conservation on null geodesics

**A measurement, not the Levi-Civita port.** Nothing imports this file. **The connection is a
HYPOTHESIS** throughout: any `CovariantDerivative` `cov` on `TM` with `cov.torsion = 0` and
`IsCompatible g cov`. No existence theorem for any connection or geodesic is used.

The layer-3 probes are copied in verbatim (`ConnectionProbe.lean`, `AlongCurveProbe.lean`), because probes
are not a library. One change: B7 is restated as a `HasDerivAt` (`covDerivAlong_compat_hasDerivAt`) rather
than a `deriv` equation, because conservation needs differentiability, not only the value. Its proof is
unchanged apart from the first and last steps.

* **R1 (B1–B3)** `IsGeodesicAt`, `IsNullAt`, `charge`.
* **R2 (B4)** `charge_hasDerivAt`: along a geodesic, `Q′(t) = σ(γ t) · g(γ̇, γ̇)`.
  **(B5)** `charge_const`: `Q` is constant along a null geodesic.
  **(B6)** `charge_deriv_ne_zero`: `Q′(t) ≠ 0` where `σ ≠ 0` and `γ̇` is not null.
-/

open Bundle Manifold VectorField Filter Set FiberBundle
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
theorem covDerivAlong_compat_hasDerivAt (g : Π x : M, TangentSpace I x →L[ℝ] TangentSpace I x →L[ℝ] ℝ)
    (cov : CovariantDerivative I E (TangentSpace I : M → Type _))
    (γ : ℝ → M) (t : ℝ) (hγ : MDifferentiableAt 𝓘(ℝ, ℝ) I γ t) (hcomp : IsCompatible g cov (γ t))
    (hg : ∀ Y Z : Π x : M, TangentSpace I x, CMDiffAt 1 (T% Y) (γ t) → CMDiffAt 1 (T% Z) (γ t) →
      MDiffAt (fun y => g y (Y y) (Z y)) (γ t))
    (V W : Π s : ℝ, TangentSpace I (γ s))
    (hV : ∀ i, DifferentiableAt ℝ (fun s => (trivializationAt E (TangentSpace I : M → Type _)
      (γ t)).localFrameCoeff I (Module.finBasis ℝ E) i (γ s) (V s)) t)
    (hW : ∀ i, DifferentiableAt ℝ (fun s => (trivializationAt E (TangentSpace I : M → Type _)
      (γ t)).localFrameCoeff I (Module.finBasis ℝ E) i (γ s) (W s)) t) :
    HasDerivAt (fun s => g (γ s) (V s) (W s))
      (g (γ t) (covDerivAlong cov γ V t) (W t) + g (γ t) (V t) (covDerivAlong cov γ W t)) t := by
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
  refine (hsum.congr_of_eventuallyEq hexp).congr_deriv ?_
  conv_rhs => rw [vec_expand hx (W t), vec_expand hx (V t)]
  unfold covDerivAlong
  simp only [← he, ← hb]
  simp only [map_sum, map_add, map_smul, ContinuousLinearMap.sum_apply,
    ContinuousLinearMap.add_apply, ContinuousLinearMap.smul_apply, smul_eq_mul]
  simp only [← Finset.sum_add_distrib, Finset.mul_sum]
  conv_rhs => rw [Finset.sum_comm]
  apply Finset.sum_congr rfl; intro i _; apply Finset.sum_congr rfl; intro j _
  simp only [← he, v, w, G]
  ring


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


/-! ## R1 (B1–B3) -/

/-- **B1.** `γ` is a geodesic of `cov` at `t`: `D/dt γ̇ = 0`. -/
def IsGeodesicAt (cov : CovariantDerivative I E (TangentSpace I : M → Type _)) (γ : ℝ → M)
    (t : ℝ) : Prop :=
  covDerivAlong cov γ (vel γ) t = 0

/-- **B2.** `γ̇` is null for `g` at `t`. -/
def IsNullAt (g : Π x : M, TangentSpace I x →L[ℝ] TangentSpace I x →L[ℝ] ℝ) (γ : ℝ → M)
    (t : ℝ) : Prop :=
  g (γ t) (vel (I := I) γ t) (vel (I := I) γ t) = 0

/-- **B3.** The charge `Q(t) = g(ξ, γ̇)`. -/
noncomputable def charge (g : Π x : M, TangentSpace I x →L[ℝ] TangentSpace I x →L[ℝ] ℝ)
    (ξ : Π x : M, TangentSpace I x) (γ : ℝ → M) (t : ℝ) : ℝ :=
  g (γ t) (ξ (γ t)) (vel (I := I) γ t)

/-! ## R2 (B4–B6) -/

/-- The frame coefficients of a field along `γ`, in the frame of the trivialisation at `γ t`, are
differentiable at `t`. This is the hypothesis B7 uses, named once. -/
def CoeffDiffAt (γ : ℝ → M) (V : Π s : ℝ, TangentSpace I (γ s)) (t : ℝ) : Prop :=
  ∀ i, DifferentiableAt ℝ (fun s => (trivializationAt E (TangentSpace I : M → Type _)
    (γ t)).localFrameCoeff I (Module.finBasis ℝ E) i (γ s) (V s)) t

set_option backward.isDefEq.respectTransparency false in
/-- **R2 (B4).** Along a geodesic of a torsion-free `g`-compatible connection, for a conformal Killing
field `ξ` with factor `σ` and a symmetric `g`, `Q′(t) = σ(γ t) · g(γ̇, γ̇)`. -/
theorem charge_hasDerivAt (g : Π x : M, TangentSpace I x →L[ℝ] TangentSpace I x →L[ℝ] ℝ)
    (hsymm : ∀ x (v w : TangentSpace I x), g x v w = g x w v)
    (cov : CovariantDerivative I E (TangentSpace I : M → Type _)) (htor : cov.torsion = 0)
    (γ : ℝ → M) (t : ℝ) (hγ : MDifferentiableAt 𝓘(ℝ, ℝ) I γ t)
    (hcomp : IsCompatible g cov (γ t))
    (hg : ∀ Y Z : Π x : M, TangentSpace I x, CMDiffAt 1 (T% Y) (γ t) → CMDiffAt 1 (T% Z) (γ t) →
      MDiffAt (fun y => g y (Y y) (Z y)) (γ t))
    (ξ : Π x : M, TangentSpace I x) (hξ : CMDiffAt 1 (T% ξ) (γ t)) (σ : M → ℝ)
    (hck : IsConformalKilling g ξ σ (γ t))
    (hξc : CoeffDiffAt γ (fun s => ξ (γ s)) t) (hvc : CoeffDiffAt γ (vel (I := I) γ) t)
    (hgeo : IsGeodesicAt cov γ t) :
    HasDerivAt (charge g ξ γ) (σ (γ t) * g (γ t) (vel γ t) (vel γ t)) t := by
  have h := covDerivAlong_compat_hasDerivAt g cov γ t hγ hcomp hg (fun s => ξ (γ s)) (vel γ)
    hξc hvc
  rw [covDerivAlong_comp cov γ t hγ ξ hξ, show covDerivAlong cov γ (vel γ) t = 0 from hgeo,
    map_zero, add_zero] at h
  refine h.congr_deriv ?_
  -- conformal Killing in `∇` form, on an extension of `γ̇`
  have hk := conformalKilling_cov g cov htor hcomp hξ hck (contMDiffAt_extend I E (vel γ t))
    (contMDiffAt_extend I E (vel γ t))
  simp only [extend_apply_self] at hk
  rw [hsymm (γ t) (vel γ t) (cov ξ (γ t) (vel γ t))] at hk
  linarith

/-- **R2 (B5).** Along a null geodesic defined for all `t`, the charge is constant. -/
theorem charge_const (g : Π x : M, TangentSpace I x →L[ℝ] TangentSpace I x →L[ℝ] ℝ)
    (hsymm : ∀ x (v w : TangentSpace I x), g x v w = g x w v)
    (cov : CovariantDerivative I E (TangentSpace I : M → Type _)) (htor : cov.torsion = 0)
    (γ : ℝ → M) (hγ : ∀ t, MDifferentiableAt 𝓘(ℝ, ℝ) I γ t)
    (hcomp : ∀ t, IsCompatible g cov (γ t))
    (hg : ∀ t, ∀ Y Z : Π x : M, TangentSpace I x, CMDiffAt 1 (T% Y) (γ t) →
      CMDiffAt 1 (T% Z) (γ t) → MDiffAt (fun y => g y (Y y) (Z y)) (γ t))
    (ξ : Π x : M, TangentSpace I x) (hξ : ∀ t, CMDiffAt 1 (T% ξ) (γ t)) (σ : M → ℝ)
    (hck : ∀ t, IsConformalKilling g ξ σ (γ t))
    (hξc : ∀ t, CoeffDiffAt γ (fun s => ξ (γ s)) t) (hvc : ∀ t, CoeffDiffAt γ (vel (I := I) γ) t)
    (hgeo : ∀ t, IsGeodesicAt cov γ t) (hnull : ∀ t, IsNullAt g γ t) (s t : ℝ) :
    charge g ξ γ s = charge g ξ γ t := by
  have hd : ∀ u, HasDerivAt (charge g ξ γ) 0 u := by
    intro u
    have := charge_hasDerivAt g hsymm cov htor γ u (hγ u) (hcomp u) (hg u) ξ (hξ u) σ (hck u)
      (hξc u) (hvc u) (hgeo u)
    rwa [show g (γ u) (vel γ u) (vel γ u) = 0 from hnull u, mul_zero] at this
  exact is_const_of_deriv_eq_zero (fun u => (hd u).differentiableAt) (fun u => (hd u).deriv) s t

/-- **R2 (B6).** "And along no other": where `σ ≠ 0` and `γ̇` is not null, `Q′(t) ≠ 0`. -/
theorem charge_deriv_ne_zero {σ0 n : ℝ} {Q : ℝ → ℝ} {t : ℝ} (h : HasDerivAt Q (σ0 * n) t)
    (hσ : σ0 ≠ 0) (hn : n ≠ 0) : deriv Q t ≠ 0 := by
  rw [h.deriv]
  exact mul_ne_zero hσ hn

end ShadowProbe

#print axioms ShadowProbe.charge_hasDerivAt
#print axioms ShadowProbe.charge_const
#print axioms ShadowProbe.charge_deriv_ne_zero

import Mathlib.Geometry.Manifold.VectorField.LieBracket
import Mathlib.Geometry.Manifold.VectorBundle.CovariantDerivative.Torsion
import Mathlib.Geometry.Manifold.VectorBundle.LocalFrame
import Mathlib.Geometry.Manifold.VectorBundle.Tangent
import Mathlib.Analysis.Calculus.Deriv.Add
import Mathlib.Analysis.Calculus.Deriv.Mul
import Mathlib.Analysis.Calculus.MeanValue

/-!
# Probe R4 of `r7277+71.1`: I20's instance — `a·ω` constant along a null geodesic, and `1 + z = a_obs/a_em`

Assembled from the probes it needs, because probes are not a library and do not import each other:
`GeodesicProbe.lean` (R1–R2, with the layer-3 probes it copies), `ConformalLCProbe.lean` (R3, without its
duplicate `IsCompatible`), and `xi`/`xi_isConformalKilling` from `LieDerivProbe.lean` (`r7269`'s P3),
reusing R3's `minkForm`/`gConf`, which are the same definitions. Everything copied is copied verbatim.
**The connection is the explicit one of R3, for this one metric — no general existence theorem is used.**
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

/-- `ξ = ∂_η`. -/
def xi : Π p : ℝ × ℝ, TangentSpace 𝓘(ℝ, ℝ × ℝ) p := fun _ => ((1 : ℝ), (0 : ℝ))

/-- **P3 (B8).** `∂_η` is conformal Killing for `a(η)² (−dη² + dx²)` with `σ = a′/a`, at every point
where `a` is differentiable and nonzero. -/
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

/-! ## R4 (B9, B10) -/

/-- The comoving frequency of a curve: `ω = a(η) · η̇`, i.e. `−g(u, γ̇)` for `u = ∂_η / a`. -/
noncomputable def omega (a : ℝ → ℝ) (γ : ℝ → ℝ × ℝ) (t : ℝ) : ℝ :=
  a (γ t).1 * (show ℝ × ℝ from vel (I := 𝓘(ℝ, ℝ × ℝ)) γ t).1

lemma gConf_symm (a : ℝ → ℝ) (x : ℝ × ℝ) (v w : TangentSpace 𝓘(ℝ, ℝ × ℝ) x) :
    gConf a x v w = gConf a x w v := by
  have h1 := gConf_apply a x v w
  have h2 := gConf_apply a x w v
  linarith

lemma charge_eq (a : ℝ → ℝ) (γ : ℝ → ℝ × ℝ) (t : ℝ) :
    charge (gConf a) xi γ t = -(a (γ t).1 * omega a γ t) := by
  have h := gConf_apply a (γ t) ((1 : ℝ), (0 : ℝ)) (vel (I := 𝓘(ℝ, ℝ × ℝ)) γ t)
  simp only [charge, omega, xi]
  linear_combination h

set_option backward.isDefEq.respectTransparency false in
/-- **R4 (B9).** Along a null geodesic of the explicit connection, `a · ω` is constant. -/
theorem a_omega_const (a : ℝ → ℝ) (hd : Differentiable ℝ a) (ha : ∀ η, a η ≠ 0)
    (γ : ℝ → ℝ × ℝ) (hγ : ∀ t, MDifferentiableAt 𝓘(ℝ, ℝ) 𝓘(ℝ, ℝ × ℝ) γ t)
    (hξc : ∀ t, CoeffDiffAt γ (fun s => xi (γ s)) t)
    (hvc : ∀ t, CoeffDiffAt γ (vel (I := 𝓘(ℝ, ℝ × ℝ)) γ) t)
    (hgeo : ∀ t, IsGeodesicAt (covConf a) γ t) (hnull : ∀ t, IsNullAt (gConf a) γ t) (s t : ℝ) :
    a (γ s).1 * omega a γ s = a (γ t).1 * omega a γ t := by
  have hg : ∀ t, ∀ Y Z : Π x : ℝ × ℝ, TangentSpace 𝓘(ℝ, ℝ × ℝ) x,
      ContMDiffAt 𝓘(ℝ, ℝ × ℝ) 𝓘(ℝ, ℝ × ℝ).tangent 1
        (fun x => (⟨x, Y x⟩ : TangentBundle 𝓘(ℝ, ℝ × ℝ) (ℝ × ℝ))) (γ t) →
      ContMDiffAt 𝓘(ℝ, ℝ × ℝ) 𝓘(ℝ, ℝ × ℝ).tangent 1
        (fun x => (⟨x, Z x⟩ : TangentBundle 𝓘(ℝ, ℝ × ℝ) (ℝ × ℝ))) (γ t) →
      MDifferentiableAt 𝓘(ℝ, ℝ × ℝ) 𝓘(ℝ, ℝ) (fun y => gConf a y (Y y) (Z y)) (γ t) := by
    intro t Y Z hY hZ
    rw [contMDiffAt_vectorSpace_iff_contDiffAt] at hY hZ
    obtain ⟨Y', rfl⟩ : ∃ Y' : ℝ × ℝ → ℝ × ℝ, Y' = Y := ⟨Y, rfl⟩
    obtain ⟨Z', rfl⟩ : ∃ Z' : ℝ × ℝ → ℝ × ℝ, Z' = Z := ⟨Z, rfl⟩
    have hYd : DifferentiableAt ℝ Y' (γ t) := hY.differentiableAt (by norm_num)
    have hZd : DifferentiableAt ℝ Z' (γ t) := hZ.differentiableAt (by norm_num)
    rw [mdifferentiableAt_iff_differentiableAt]
    have : (fun y : ℝ × ℝ => gConf a y (Y' y) (Z' y))
        = fun q => a q.1 ^ 2 * (-((Y' q).1 * (Z' q).1) + (Y' q).2 * (Z' q).2) := by
      funext q; rw [gConf_apply]
    rw [this]
    have ha1 : DifferentiableAt ℝ (fun q : ℝ × ℝ => a q.1) (γ t) :=
      (hd _).comp _ differentiableAt_fst
    fun_prop
  have hξ : ∀ t, ContMDiffAt 𝓘(ℝ, ℝ × ℝ) 𝓘(ℝ, ℝ × ℝ).tangent 1
      (fun x => (⟨x, xi x⟩ : TangentBundle 𝓘(ℝ, ℝ × ℝ) (ℝ × ℝ))) (γ t) := by
    intro t
    rw [contMDiffAt_vectorSpace_iff_contDiffAt]
    exact contDiffAt_const
  have h := charge_const (gConf a) (gConf_symm a) (covConf a) (covConf_torsion a) γ hγ
    (fun t => covConf_compatible a (γ t) (hd _) (ha _)) hg xi hξ (fun q => deriv a q.1 / a q.1)
    (fun t => xi_isConformalKilling a (γ t) (hd _) (ha _)) hξc hvc hgeo hnull s t
  rw [charge_eq, charge_eq] at h
  linarith

/-- **R4 (B10).** `1 + z = ω_em/ω_obs = a_obs/a_em`. -/
theorem one_plus_z (a : ℝ → ℝ) (γ : ℝ → ℝ × ℝ) {s t : ℝ}
    (h : a (γ s).1 * omega a γ s = a (γ t).1 * omega a γ t)
    (hs : a (γ s).1 ≠ 0) (hω : omega a γ t ≠ 0) :
    omega a γ s / omega a γ t = a (γ t).1 / a (γ s).1 := by
  field_simp
  linarith

end ShadowProbe

#print axioms ShadowProbe.a_omega_const
#print axioms ShadowProbe.one_plus_z

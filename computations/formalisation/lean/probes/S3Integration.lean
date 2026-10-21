import Mathlib.MeasureTheory.Constructions.HaarToSphere
import Mathlib.MeasureTheory.Measure.Haar.InnerProductSpace
import Mathlib.MeasureTheory.Function.LocallyIntegrable
import Mathlib.MeasureTheory.Integral.Bochner.ContinuousLinearMap
import Mathlib.Analysis.Quaternion
import Mathlib.Analysis.Calculus.ParametricIntegral
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Deriv
import Mathlib.Algebra.MvPolynomial.Derivation

/-! # Campaign 52, stage P1: integration on `S³` and the symmetry of `∇²`

`σ = volume.toSphere` on the unit sphere of `ℝ⁴ = EuclideanSpace ℝ (Fin 4)`, identified with `ℍ` by
`Quaternion.linearIsometryEquivTuple`. Every linear isometry preserves `σ` (`sph_preserving`), in particular the
right and left translations by unit quaternions. The frame field `E_a(q) = q·u_a` (campaign 51's `dval`) acts on
functions `f : ℝ⁴ → ℂ` by `Ea a f x = Df(x)(x·u_a)`; differentiating `t ↦ ∫ f(q·(cos t + sin t·u_a)) dσ` under the
integral sign gives `∫ E_a f dσ = 0` (`integral_Ea`). Hence integration by parts (`ibp`), the skew-adjointness of
`∇_a` with campaign 51's connection `∇_{E_a}E_b = ε_abc E_c` (`nab_skew`), the symmetry of `∇² = Σ ∇_a∇_a`
(`lap_symm`) and `∫⟨−∇²h, h⟩ = Σ_a ∫|∇_a h|² ≥ 0` (`neg_lap_nonneg`). On polynomials `E_a` is `D a`
(`Ea_poly`), and campaign 51's `nab`/`lap` are `nabA`/`lapA` (`evT_nab`, `evT_lap`, `lapP_symm`). -/

open MeasureTheory Metric Set Quaternion
open scoped Quaternion ComplexConjugate Pointwise

namespace ShadowProbe.S3Integration

/-! ## 1. The sphere measure -/

abbrev E := EuclideanSpace ℝ (Fin 4)
abbrev S3 := sphere (0 : E) 1

/-- The surface measure on the unit `S³ ⊂ ℝ⁴`. -/
noncomputable def σ : Measure S3 := (volume : Measure E).toSphere

instance : IsFiniteMeasure σ := by unfold σ; infer_instance

theorem σ_ne_zero : σ ≠ 0 := Measure.toSphere_ne_zero _

theorem σ_univ : σ univ = 4 * volume (ball (0 : E) 1) := by
  simp [σ, finrank_euclideanSpace]

theorem σ_finite_nonzero : σ univ < ⊤ ∧ σ univ ≠ 0 :=
  ⟨measure_lt_top _ _, fun h => σ_ne_zero (Measure.measure_univ_eq_zero.1 h)⟩

/-! ## 2. Invariance under linear isometries -/

lemma mem_S3 (L : E ≃ₗᵢ[ℝ] E) (x : S3) : L x ∈ S3 := by
  have := x.2; simp only [mem_sphere_zero_iff_norm] at this ⊢; rw [L.norm_map, this]

/-- A linear isometry of `ℝ⁴`, restricted to the unit sphere. -/
noncomputable def sph (L : E ≃ₗᵢ[ℝ] E) : S3 ≃ᵐ S3 where
  toFun x := ⟨L x, mem_S3 L x⟩
  invFun x := ⟨L.symm x, mem_S3 L.symm x⟩
  left_inv x := Subtype.ext (by simp)
  right_inv x := Subtype.ext (by simp)
  measurable_toFun := ((L.continuous.comp continuous_subtype_val).subtype_mk _).measurable
  measurable_invFun := ((L.symm.continuous.comp continuous_subtype_val).subtype_mk _).measurable

@[simp] lemma sph_val (L : E ≃ₗᵢ[ℝ] E) (x : S3) : ((sph L x : S3) : E) = L x := rfl

/-- **Every linear isometry of `ℝ⁴` preserves `σ`.** -/
theorem sph_preserving (L : E ≃ₗᵢ[ℝ] E) : MeasurePreserving (sph L) σ σ := by
  refine ⟨(sph L).measurable, ?_⟩
  ext s hs
  rw [Measure.map_apply (sph L).measurable hs, σ, Measure.toSphere_apply' _ hs,
    Measure.toSphere_apply' _ ((sph L).measurable hs)]
  congr 1
  have : Ioo (0 : ℝ) 1 • ((↑) '' (sph L ⁻¹' s) : Set E) = L ⁻¹' (Ioo (0 : ℝ) 1 • ((↑) '' s)) := by
    ext z
    simp only [Set.mem_smul, Set.mem_preimage, Set.mem_image]
    constructor
    · rintro ⟨r, hr, _, ⟨y, hy, rfl⟩, rfl⟩
      exact ⟨r, hr, _, ⟨sph L y, hy, rfl⟩, by simp⟩
    · rintro ⟨r, hr, _, ⟨y, hy, rfl⟩, hz⟩
      refine ⟨r, hr, _, ⟨(sph L).symm y, by simpa using hy, rfl⟩, ?_⟩
      apply L.injective
      rw [L.map_smul, ← hz]
      congr 1
      exact congrArg Subtype.val ((sph L).apply_symm_apply y)
  rw [this]
  exact ((L.measurePreserving).measure_preimage_emb L.toHomeomorph.measurableEmbedding _)

/-- Integrals over `S³` are invariant under every linear isometry. -/
theorem integral_sph {F : Type*} [NormedAddCommGroup F] [NormedSpace ℝ F]
    (L : E ≃ₗᵢ[ℝ] E) (f : E → F) : ∫ x : S3, f (L x) ∂σ = ∫ x : S3, f x ∂σ :=
  (sph_preserving L).integral_comp' (fun y : S3 => f y)

/-! ### Quaternion translations -/

lemma ne_zero_of_norm {g : ℍ} (hg : ‖g‖ = 1) : g ≠ 0 := by rintro rfl; simp at hg

/-- Right translation `q ↦ q·g` by a unit quaternion. -/
noncomputable def rmulH (g : ℍ) (hg : ‖g‖ = 1) : ℍ ≃ₗᵢ[ℝ] ℍ where
  toFun q := q * g
  invFun q := q * g⁻¹
  map_add' a b := add_mul a b g
  map_smul' c q := smul_mul_assoc c q g
  left_inv q := by simp [ne_zero_of_norm hg]
  right_inv q := by simp [ne_zero_of_norm hg]
  norm_map' q := by simp [norm_mul, hg]

/-- Left translation `q ↦ g·q` by a unit quaternion. -/
noncomputable def lmulH (g : ℍ) (hg : ‖g‖ = 1) : ℍ ≃ₗᵢ[ℝ] ℍ where
  toFun q := g * q
  invFun q := g⁻¹ * q
  map_add' a b := mul_add g a b
  map_smul' c q := mul_smul_comm c g q
  left_inv q := by simp [ne_zero_of_norm hg]
  right_inv q := by simp [ne_zero_of_norm hg]
  norm_map' q := by simp [norm_mul, hg]

/-- `q ↦ q·g` on `ℝ⁴` (coordinates `x = x₀ + x₁i + x₂j + x₃k`). -/
noncomputable def rmul (g : ℍ) (hg : ‖g‖ = 1) : E ≃ₗᵢ[ℝ] E :=
  (linearIsometryEquivTuple.symm.trans (rmulH g hg)).trans linearIsometryEquivTuple
/-- `q ↦ g·q` on `ℝ⁴`. -/
noncomputable def lmul (g : ℍ) (hg : ‖g‖ = 1) : E ≃ₗᵢ[ℝ] E :=
  (linearIsometryEquivTuple.symm.trans (lmulH g hg)).trans linearIsometryEquivTuple

lemma rmul_apply (g : ℍ) (hg : ‖g‖ = 1) (x : E) :
    rmul g hg x = linearIsometryEquivTuple (linearIsometryEquivTuple.symm x * g) := rfl
lemma lmul_apply (g : ℍ) (hg : ‖g‖ = 1) (x : E) :
    lmul g hg x = linearIsometryEquivTuple (g * linearIsometryEquivTuple.symm x) := rfl

/-- **Right invariance of `σ`.** -/
theorem right_invariant (g : ℍ) (hg : ‖g‖ = 1) : MeasurePreserving (sph (rmul g hg)) σ σ :=
  sph_preserving _
/-- **Left invariance of `σ`.** -/
theorem left_invariant (g : ℍ) (hg : ‖g‖ = 1) : MeasurePreserving (sph (lmul g hg)) σ σ :=
  sph_preserving _


/-! ## 3. The frame and its one-parameter rotations -/

lemma norm_one_of_normSq {g : ℍ} (h : normSq g = 1) : ‖g‖ = 1 := by
  have h2 : ‖g‖ * ‖g‖ = 1 := by rw [← normSq_eq_norm_mul_self, h]
  nlinarith [norm_nonneg g]

/-- The imaginary units `u = (i, j, k)`. -/
def u : Fin 3 → ℍ := ![⟨0, 1, 0, 0⟩, ⟨0, 0, 1, 0⟩, ⟨0, 0, 0, 1⟩]

lemma u_norm (a : Fin 3) : ‖u a‖ = 1 :=
  norm_one_of_normSq (by fin_cases a <;> simp [u, normSq_def'])

/-- **The left-invariant frame field** `E_a(q) = q·u_a` (campaign 51's `dval`/`dR`), a linear map of `ℝ⁴`. -/
noncomputable def vR (a : Fin 3) : E →L[ℝ] E := ((rmul (u a) (u_norm a)).toContinuousLinearEquiv : E →L[ℝ] E)

lemma vR_apply (a : Fin 3) (x : E) : vR a x = rmul (u a) (u_norm a) x := rfl

/-- The components of `E_a`, as in campaign 51's `dval`/`dR`. -/
def dR : Fin 3 → E → Fin 4 → ℝ
  | 0 => fun x => ![-x 1, x 0, x 3, -x 2]
  | 1 => fun x => ![-x 2, -x 3, x 0, x 1]
  | 2 => fun x => ![-x 3, x 2, -x 1, x 0]

lemma vR_coord (a : Fin 3) (x : E) (i : Fin 4) : vR a x i = dR a x i := by
  fin_cases a <;> fin_cases i <;> simp [vR_apply, rmul_apply, u, dR]

/-- `exp(t u_a) = cos t + sin t·u_a`. -/
noncomputable def gexp (a : Fin 3) (t : ℝ) : ℍ := (Real.cos t : ℍ) + Real.sin t • u a

lemma gexp_norm (a : Fin 3) (t : ℝ) : ‖gexp a t‖ = 1 :=
  norm_one_of_normSq (by
    fin_cases a <;> simp [gexp, u, normSq_def'])

/-- The rotation `q ↦ q·exp(t u_a)`, a linear isometry of `ℝ⁴`. -/
noncomputable def rot (a : Fin 3) (t : ℝ) : E ≃ₗᵢ[ℝ] E := rmul (gexp a t) (gexp_norm a t)

lemma rot_apply (a : Fin 3) (t : ℝ) (x : E) : rot a t x = Real.cos t • x + Real.sin t • vR a x := by
  simp only [rot, rmul_apply, gexp, mul_add, mul_smul_comm, Quaternion.mul_coe_eq_smul, map_add,
    map_smul, LinearIsometryEquiv.apply_symm_apply, vR_apply]

/-! ## 4. The frame derivation integrates to zero -/

/-- **The frame derivation** `E_a f (x) = Df(x)·(x·u_a) = d/dt f(x·exp(t u_a))|₀`. -/
noncomputable def Ea (a : Fin 3) (f : E → ℂ) (x : E) : ℂ := fderiv ℝ f x (vR a x)

lemma integrable_of_cont {g : S3 → ℂ} (hg : Continuous g) : Integrable g σ :=
  hg.integrable_of_hasCompactSupport (HasCompactSupport.of_compactSpace g)

lemma Ea_cont (a : Fin 3) {f : E → ℂ} (hf : ContDiff ℝ 1 f) : Continuous (Ea a f) :=
  (hf.continuous_fderiv one_ne_zero).clm_apply (vR a).continuous

lemma Ea_contDiff (a : Fin 3) {m n : WithTop ℕ∞} {f : E → ℂ} (hf : ContDiff ℝ n f) (hmn : m + 1 ≤ n) :
    ContDiff ℝ m (Ea a f) :=
  (hf.fderiv_right hmn).clm_apply (vR a).contDiff

lemma rot_zero (a : Fin 3) (x : E) : rot a 0 x = x := by simp [rot_apply]

/-- `d/dt f(x·exp(t u_a))`. -/
lemma hasDerivAt_rot (a : Fin 3) {f : E → ℂ} (hf : Differentiable ℝ f) (x : E) (t : ℝ) :
    HasDerivAt (fun t => f (rot a t x))
      (fderiv ℝ f (rot a t x) (-Real.sin t • x + Real.cos t • vR a x)) t := by
  have hγ : HasDerivAt (fun t => Real.cos t • x + Real.sin t • vR a x)
      (-Real.sin t • x + Real.cos t • vR a x) t :=
    ((Real.hasDerivAt_cos t).smul_const _).add ((Real.hasDerivAt_sin t).smul_const _)
  have e : (fun t => f (rot a t x)) = f ∘ (fun t => Real.cos t • x + Real.sin t • vR a x) := by
    funext t; simp [rot_apply]
  rw [e]
  have h := (hf (Real.cos t • x + Real.sin t • vR a x)).hasFDerivAt.comp_hasDerivAt t hγ
  rw [← rot_apply] at h; exact h

/-- **Item 3. `∫_{S³} E_a f dσ = 0`** for every `C¹` function `f : ℝ⁴ → ℂ`. -/
theorem integral_Ea (a : Fin 3) {f : E → ℂ} (hf : ContDiff ℝ 1 f) :
    ∫ x : S3, Ea a f x ∂σ = 0 := by
  have hd : Differentiable ℝ f := hf.differentiable one_ne_zero
  obtain ⟨M, hM⟩ := (isCompact_sphere (0 : E) 1).exists_bound_of_continuousOn
    (hf.continuous_fderiv one_ne_zero).continuousOn
  let F : ℝ → S3 → ℂ := fun t x => f (rot a t x)
  let F' : ℝ → S3 → ℂ := fun t x => fderiv ℝ f (rot a t x) (-Real.sin t • (x : E) + Real.cos t • vR a x)
  have cF : ∀ t, Continuous (F t) := fun t =>
    hf.continuous.comp ((rot a t).continuous.comp continuous_subtype_val)
  have cF' : ∀ t, Continuous (F' t) := fun t =>
    ((hf.continuous_fderiv one_ne_zero).comp ((rot a t).continuous.comp continuous_subtype_val)).clm_apply
      (by fun_prop : Continuous fun x : S3 => -Real.sin t • (x : E) + Real.cos t • vR a x)
  have hbound : ∀ (x : S3) (t : ℝ), ‖F' t x‖ ≤ M * 2 := by
    intro x t
    have hx : ‖(x : E)‖ = 1 := by simp
    have hvx : ‖vR a x‖ = 1 := by rw [vR_apply, LinearIsometryEquiv.norm_map, hx]
    have hv : ‖-Real.sin t • (x : E) + Real.cos t • vR a x‖ ≤ 2 := by
      calc _ ≤ ‖-Real.sin t • (x : E)‖ + ‖Real.cos t • vR a x‖ := norm_add_le _ _
        _ = |Real.sin t| + |Real.cos t| := by rw [norm_smul, norm_smul, hx, hvx]; simp
        _ ≤ 2 := by linarith [Real.abs_sin_le_one t, Real.abs_cos_le_one t]
    have hmem : rot a t x ∈ sphere (0 : E) 1 := mem_S3 (rot a t) x
    calc ‖F' t x‖ ≤ ‖fderiv ℝ f (rot a t x)‖ * ‖-Real.sin t • (x : E) + Real.cos t • vR a x‖ :=
          ContinuousLinearMap.le_opNorm _ _
      _ ≤ M * 2 := mul_le_mul (hM _ hmem) hv (norm_nonneg _) ((norm_nonneg _).trans (hM _ hmem))
  have key := hasDerivAt_integral_of_dominated_loc_of_deriv_le (μ := σ) (F := F) (F' := F') (x₀ := 0)
    (bound := fun _ => M * 2) Filter.univ_mem
    (Filter.Eventually.of_forall fun t => (cF t).aestronglyMeasurable)
    (integrable_of_cont (cF 0)) (cF' 0).aestronglyMeasurable
    (ae_of_all _ fun x t _ => hbound x t) (integrable_const _)
    (ae_of_all _ fun x t _ => hasDerivAt_rot a hd x t)
  have hconst : (fun t => ∫ x, F t x ∂σ) = fun _ => ∫ x : S3, f x ∂σ :=
    funext fun t => integral_sph (rot a t) f
  have h2 : HasDerivAt (fun t => ∫ x, F t x ∂σ) 0 0 := by
    rw [hconst]; exact hasDerivAt_const _ _
  have e : (fun x : S3 => F' 0 x) = fun x : S3 => Ea a f x := by
    funext x; simp [F', Ea, rot_zero]
  have := key.2.unique h2
  rw [e] at this; exact this


/-! ## 5. Integration by parts for functions -/

lemma Ea_mul (a : Fin 3) {f g : E → ℂ} (hf : Differentiable ℝ f) (hg : Differentiable ℝ g) (x : E) :
    Ea a (fun y => f y * g y) x = Ea a f x * g x + f x * Ea a g x := by
  simp only [Ea]; rw [fderiv_fun_mul (hf x) (hg x)]
  simp only [FunLike.coe_add, FunLike.coe_smul, Pi.add_apply, Pi.smul_apply,
    smul_eq_mul]; ring

lemma Ea_conj (a : Fin 3) (f : E → ℂ) (x : E) :
    Ea a (fun y => conj (f y)) x = conj (Ea a f x) := by
  have h := Complex.conjCLE.comp_fderiv (f := f) (x := x)
  simp only [Ea]
  have e : (fun y => conj (f y)) = ⇑Complex.conjCLE ∘ f := by funext y; simp
  rw [e, h]; simp

lemma Ea_sum (a : Fin 3) {ι : Type*} (s : Finset ι) {A : ι → E → ℂ}
    (hA : ∀ i ∈ s, Differentiable ℝ (A i)) (x : E) :
    Ea a (fun y => ∑ i ∈ s, A i y) x = ∑ i ∈ s, Ea a (A i) x := by
  simp only [Ea]; rw [fderiv_fun_sum fun i hi => hA i hi x]; simp

lemma contDiff_conj {n : WithTop ℕ∞} {f : E → ℂ} (hf : ContDiff ℝ n f) :
    ContDiff ℝ n (fun y => conj (f y)) := by
  have := Complex.conjCLE.contDiff.comp hf
  exact this

/-- **Integration by parts.** `∫ (E_a f) g dσ = −∫ f (E_a g) dσ` for `C¹` functions. -/
theorem ibp (a : Fin 3) {f g : E → ℂ} (hf : ContDiff ℝ 1 f) (hg : ContDiff ℝ 1 g) :
    ∫ x : S3, Ea a f x * g x ∂σ = -∫ x : S3, f x * Ea a g x ∂σ := by
  have h0 := integral_Ea a (hf.mul hg)
  have e : (fun x : S3 => Ea a (fun y => f y * g y) x) =
      fun x : S3 => Ea a f x * g x + f x * Ea a g x :=
    funext fun x => Ea_mul a (hf.differentiable one_ne_zero) (hg.differentiable one_ne_zero) x
  rw [e, integral_add] at h0
  · linear_combination h0
  · exact integrable_of_cont (((Ea_cont a hf).mul hg.continuous).comp continuous_subtype_val)
  · exact integrable_of_cont ((hf.continuous.mul (Ea_cont a hg)).comp continuous_subtype_val)

/-! ## 6. Tensor fields: the connection, `∇²`, and its symmetry -/

/-- The Levi-Civita symbol (campaign 51's `eps`). -/
def eps : Fin 3 → Fin 3 → Fin 3 → ℂ :=
  ![![![0, 0, 0], ![0, 0, 1], ![0, -1, 0]],
    ![![0, 0, -1], ![0, 0, 0], ![1, 0, 0]],
    ![![0, 1, 0], ![-1, 0, 0], ![0, 0, 0]]]

/-- Frame components of a 2-tensor field on (a neighbourhood of) `S³`. -/
abbrev TenA := Fin 3 → Fin 3 → E → ℂ

/-- The connection term `(L_a H)_bc = −ε_abd H_dc − ε_acd H_bd` (campaign 51's `Lt`), pointwise. -/
def Lc (a : Fin 3) (H : Fin 3 → Fin 3 → ℂ) (b c : Fin 3) : ℂ :=
  -(∑ d, eps a b d * H d c) - ∑ d, eps a c d * H b d

/-- **The covariant derivative** `(∇_a h)_bc = E_a h_bc − ε_abd h_dc − ε_acd h_bd` (`∇_{E_a}E_b = ε_abc E_c`). -/
noncomputable def nabA (a : Fin 3) (h : TenA) : TenA :=
  fun b c x => Ea a (h b c) x + Lc a (fun i j => h i j x) b c

/-- **The rough Laplacian** `∇² = Σ_a ∇_a ∇_a`. -/
noncomputable def lapA (h : TenA) : TenA := fun b c x => ∑ a, nabA a (nabA a h) b c x

/-- The pointwise Hermitian product `⟨h, k⟩ = Σ_bc conj(h_bc) k_bc`. -/
noncomputable def ip (h k : TenA) (x : E) : ℂ := ∑ b, ∑ c, conj (h b c x) * k b c x

/-- All frame components are `Cⁿ`. -/
def CD (n : WithTop ℕ∞) (h : TenA) : Prop := ∀ b c, ContDiff ℝ n (h b c)

lemma Lc_contDiff (a : Fin 3) {n : WithTop ℕ∞} {h : TenA} (hh : CD n h) (b c : Fin 3) :
    ContDiff ℝ n (fun x => Lc a (fun i j => h i j x) b c) := by
  simp only [Lc]
  exact ((ContDiff.sum fun d _ => contDiff_const.mul (hh d c)).neg).sub
    (ContDiff.sum fun d _ => contDiff_const.mul (hh b d))

lemma nabA_CD (a : Fin 3) {m n : WithTop ℕ∞} {h : TenA} (hh : CD n h) (hmn : m + 1 ≤ n) :
    CD m (nabA a h) := fun b c =>
  (Ea_contDiff a (hh b c) hmn).add (Lc_contDiff a (fun i j => (hh i j).of_le (le_self_add.trans hmn)) b c)

lemma ip_contDiff {n : WithTop ℕ∞} {h k : TenA} (hh : CD n h) (hk : CD n k) : ContDiff ℝ n (ip h k) := by
  unfold ip
  exact ContDiff.sum fun b _ => ContDiff.sum fun c _ => (contDiff_conj (hh b c)).mul (hk b c)

lemma ip_cont {h k : TenA} (hh : CD 0 h) (hk : CD 0 k) : Continuous (ip h k) :=
  (ip_contDiff hh hk).continuous

lemma integrable_ip {h k : TenA} (hh : CD 0 h) (hk : CD 0 k) : Integrable (fun x : S3 => ip h k x) σ :=
  integrable_of_cont ((ip_cont hh hk).comp continuous_subtype_val)

lemma Ea_ip (a : Fin 3) {h k : TenA} (hh : CD 1 h) (hk : CD 1 k) (x : E) :
    Ea a (ip h k) x = ∑ b, ∑ c, (conj (Ea a (h b c) x) * k b c x + conj (h b c x) * Ea a (k b c) x) := by
  have dh : ∀ b c, Differentiable ℝ (h b c) := fun b c => (hh b c).differentiable one_ne_zero
  have dk : ∀ b c, Differentiable ℝ (k b c) := fun b c => (hk b c).differentiable one_ne_zero
  have dc : ∀ b c, Differentiable ℝ (fun y => conj (h b c y)) := fun b c =>
    (contDiff_conj (hh b c)).differentiable one_ne_zero
  unfold ip
  rw [Ea_sum a Finset.univ (A := fun b y => ∑ c, conj (h b c y) * k b c y)
    (fun b _ => Differentiable.fun_sum fun c _ => (dc b c).mul (dk b c))]
  refine Finset.sum_congr rfl fun b _ => ?_
  rw [Ea_sum a Finset.univ (A := fun c y => conj (h b c y) * k b c y) (fun c _ => (dc b c).mul (dk b c))]
  refine Finset.sum_congr rfl fun c _ => ?_
  rw [Ea_mul a (dc b c) (dk b c), Ea_conj]

/-- The connection terms are skew: the antisymmetry of `ε`. -/
lemma Lc_skew (a : Fin 3) (H K : Fin 3 → Fin 3 → ℂ) :
    ∑ b, ∑ c, (conj (Lc a H b c) * K b c + conj (H b c) * Lc a K b c) = 0 := by
  fin_cases a <;> simp [Lc, eps, Fin.sum_univ_three] <;> ring

/-- `⟨∇_a h, k⟩ + ⟨h, ∇_a k⟩ = E_a ⟨h, k⟩` pointwise (metric compatibility). -/
lemma ip_nab (a : Fin 3) {h k : TenA} (hh : CD 1 h) (hk : CD 1 k) (x : E) :
    ip (nabA a h) k x + ip h (nabA a k) x = Ea a (ip h k) x := by
  rw [Ea_ip a hh hk]
  have := Lc_skew a (fun i j => h i j x) (fun i j => k i j x)
  simp only [ip, nabA, map_add, Fin.sum_univ_three] at this ⊢
  linear_combination this

/-- **`∇_a` is skew-adjoint on `L²(σ)`.** `∫⟨∇_a h, k⟩ = −∫⟨h, ∇_a k⟩` for `C¹` tensor fields. -/
theorem nab_skew (a : Fin 3) {h k : TenA} (hh : CD 1 h) (hk : CD 1 k) :
    ∫ x : S3, ip (nabA a h) k x ∂σ = -∫ x : S3, ip h (nabA a k) x ∂σ := by
  have h0 := integral_Ea a (ip_contDiff hh hk)
  have e : (fun x : S3 => Ea a (ip h k) x) = fun x : S3 => ip (nabA a h) k x + ip h (nabA a k) x :=
    funext fun x => (ip_nab a hh hk x).symm
  have h1 : CD 0 h := fun b c => (hh b c).of_le (by norm_num)
  have k1 : CD 0 k := fun b c => (hk b c).of_le (by norm_num)
  rw [e, integral_add (integrable_ip (nabA_CD a hh (by norm_num)) k1)
    (integrable_ip h1 (nabA_CD a hk (by norm_num)))] at h0
  linear_combination h0

lemma ip_sum_left (X : Fin 3 → TenA) (k : TenA) (x : E) :
    ip (fun b c y => ∑ a, X a b c y) k x = ∑ a, ip (X a) k x := by
  simp only [ip, Fin.sum_univ_three, map_add]; ring

lemma ip_sum_right (h : TenA) (X : Fin 3 → TenA) (x : E) :
    ip h (fun b c y => ∑ a, X a b c y) x = ∑ a, ip h (X a) x := by
  simp only [ip, Fin.sum_univ_three]; ring

lemma CD_mono {m n : WithTop ℕ∞} {h : TenA} (hh : CD n h) (hmn : m ≤ n) : CD m h :=
  fun b c => (hh b c).of_le hmn

/-- `∫⟨∇²h, k⟩ = −Σ_a ∫⟨∇_a h, ∇_a k⟩`. -/
theorem lap_ip (h k : TenA) (hh : CD 2 h) (hk : CD 1 k) :
    ∫ x : S3, ip (lapA h) k x ∂σ = -∑ a, ∫ x : S3, ip (nabA a h) (nabA a k) x ∂σ := by
  have e : (fun x : S3 => ip (lapA h) k x) = fun x : S3 => ∑ a, ip (nabA a (nabA a h)) k x :=
    funext fun x => ip_sum_left (fun a => nabA a (nabA a h)) k x
  rw [e, integral_finsetSum _ fun a _ => integrable_ip
    (nabA_CD (m := 0) a (nabA_CD (m := 1) a hh (by norm_num)) (by norm_num)) (CD_mono hk (by norm_num)),
    ← Finset.sum_neg_distrib]
  exact Finset.sum_congr rfl fun a _ => nab_skew a (nabA_CD a hh (by norm_num)) hk

/-- **`∇²` is symmetric on `L²(σ)`**: `∫⟨∇²h, k⟩ = ∫⟨h, ∇²k⟩` for `C²` tensor fields. -/
theorem lap_symm (h k : TenA) (hh : CD 2 h) (hk : CD 2 k) :
    ∫ x : S3, ip (lapA h) k x ∂σ = ∫ x : S3, ip h (lapA k) x ∂σ := by
  rw [lap_ip h k hh (CD_mono hk (by norm_num))]
  have e : (fun x : S3 => ip h (lapA k) x) = fun x : S3 => ∑ a, ip h (nabA a (nabA a k)) x :=
    funext fun x => ip_sum_right h (fun a => nabA a (nabA a k)) x
  rw [e, integral_finsetSum _ fun a _ => integrable_ip (CD_mono hh (by norm_num))
    (nabA_CD (m := 0) a (nabA_CD (m := 1) a hk (by norm_num)) (by norm_num)), ← Finset.sum_neg_distrib]
  refine Finset.sum_congr rfl fun a _ => ?_
  rw [nab_skew a (CD_mono hh (by norm_num)) (nabA_CD a hk (by norm_num)), neg_neg]

lemma ip_self (h : TenA) (x : E) : ip h h x = ((∑ b, ∑ c, ‖h b c x‖ ^ 2 : ℝ) : ℂ) := by
  simp [ip, Complex.conj_mul']

lemma ip_neg_left (h k : TenA) (x : E) : ip (fun b c y => -h b c y) k x = -ip h k x := by
  simp [ip, Finset.sum_neg_distrib]

/-- **`−∇² ≥ 0`.** `∫⟨−∇²h, h⟩ = Σ_a ∫ |∇_a h|²`, a non-negative real. -/
theorem neg_lap_nonneg (h : TenA) (hh : CD 2 h) :
    ∫ x : S3, ip (fun b c y => -lapA h b c y) h x ∂σ =
      ((∑ a, ∫ x : S3, ∑ b, ∑ c, ‖nabA a h b c x‖ ^ 2 ∂σ : ℝ) : ℂ) ∧
    0 ≤ ∑ a, ∫ x : S3, ∑ b, ∑ c, ‖nabA a h b c x‖ ^ 2 ∂σ := by
  refine ⟨?_, Finset.sum_nonneg fun a _ => integral_nonneg fun x => by positivity⟩
  simp only [ip_neg_left, integral_neg]
  rw [lap_ip h h hh (CD_mono hh (by norm_num)), neg_neg, Complex.ofReal_sum]
  refine Finset.sum_congr rfl fun a _ => ?_
  simp only [ip_self]; exact integral_ofReal


/-! ## 7. Sanity: on polynomials, `E_a` is campaign 51's derivation `D a` -/

section Poly
open MvPolynomial

abbrev P := MvPolynomial (Fin 4) ℂ

/-- `D_a (X i)`: campaign 51's `dval`. -/
noncomputable def dval : Fin 3 → Fin 4 → P
  | 0 => ![-X 1, X 0, X 3, -X 2]
  | 1 => ![-X 2, -X 3, X 0, X 1]
  | 2 => ![-X 3, X 2, -X 1, X 0]

/-- Campaign 51's frame derivations. -/
noncomputable def D (a : Fin 3) : Derivation ℂ P P := mkDerivation ℂ (dval a)

@[simp] lemma D_X (a : Fin 3) (i : Fin 4) : D a (X i) = dval a i := mkDerivation_X _ _ _

/-- A complex polynomial as a function on `ℝ⁴` (campaign 51's `ev`). -/
noncomputable def evE (p : P) (x : E) : ℂ := eval (fun i => ((x i : ℝ) : ℂ)) p

@[simp] lemma evE_zero (x : E) : evE 0 x = 0 := by simp [evE]
@[simp] lemma evE_add (p q : P) (x : E) : evE (p + q) x = evE p x + evE q x := by simp [evE]
@[simp] lemma evE_sub (p q : P) (x : E) : evE (p - q) x = evE p x - evE q x := by simp [evE]
@[simp] lemma evE_neg (p : P) (x : E) : evE (-p) x = -evE p x := by simp [evE]
@[simp] lemma evE_mul (p q : P) (x : E) : evE (p * q) x = evE p x * evE q x := by simp [evE]
@[simp] lemma evE_C (c : ℂ) (x : E) : evE (C c) x = c := by simp [evE]
@[simp] lemma evE_X (i : Fin 4) (x : E) : evE (X i) x = ((x i : ℝ) : ℂ) := by simp [evE]
@[simp] lemma evE_sum {ι : Type*} (s : Finset ι) (p : ι → P) (x : E) :
    evE (∑ i ∈ s, p i) x = ∑ i ∈ s, evE (p i) x := by simp [evE, map_sum]

lemma coord_hasFDerivAt (i : Fin 4) (x : E) :
    HasFDerivAt (fun y : E => ((y i : ℝ) : ℂ)) (Complex.ofRealCLM.comp (EuclideanSpace.proj i)) x :=
  (Complex.ofRealCLM.comp (EuclideanSpace.proj i : E →L[ℝ] ℝ)).hasFDerivAt

lemma coord_contDiff (i : Fin 4) {n : WithTop ℕ∞} : ContDiff ℝ n (fun y : E => ((y i : ℝ) : ℂ)) :=
  (Complex.ofRealCLM.comp (EuclideanSpace.proj i : E →L[ℝ] ℝ)).contDiff

lemma evE_contDiff (p : P) {n : WithTop ℕ∞} : ContDiff ℝ n (evE p) := by
  induction p using MvPolynomial.induction_on with
  | C c =>
    have : evE (C c) = fun _ => c := funext fun _ => evE_C c _
    rw [this]; exact contDiff_const
  | add p q hp hq =>
    have : evE (p + q) = fun x => evE p x + evE q x := funext fun x => evE_add p q x
    rw [this]; exact hp.add hq
  | mul_X p i hp =>
    have : evE (p * X i) = fun x => evE p x * ((x i : ℝ) : ℂ) := funext fun x => by simp
    rw [this]; exact hp.mul (coord_contDiff i)

lemma evE_diff (p : P) : Differentiable ℝ (evE p) := (evE_contDiff p (n := 1)).differentiable one_ne_zero

lemma Ea_add (a : Fin 3) {f g : E → ℂ} (hf : Differentiable ℝ f) (hg : Differentiable ℝ g) (x : E) :
    Ea a (fun y => f y + g y) x = Ea a f x + Ea a g x := by
  simp only [Ea]; rw [fderiv_fun_add (hf x) (hg x)]; rfl

lemma Ea_const (a : Fin 3) (c : ℂ) (x : E) : Ea a (fun _ => c) x = 0 := by simp [Ea]

lemma Ea_coord (a : Fin 3) (i : Fin 4) (x : E) :
    Ea a (fun y : E => ((y i : ℝ) : ℂ)) x = ((dR a x i : ℝ) : ℂ) := by
  simp only [Ea, (coord_hasFDerivAt i x).fderiv]; simp [vR_coord]

lemma evE_dval (a : Fin 3) (i : Fin 4) (x : E) : evE (dval a i) x = ((dR a x i : ℝ) : ℂ) := by
  fin_cases a <;> fin_cases i <;> simp [dval, dR]

/-- **Item 5.** On polynomials the analytic frame derivation is campaign 51's `D a`:
`E_a (p|_{ℝ⁴}) = (D a p)|_{ℝ⁴}`. -/
theorem Ea_poly (a : Fin 3) (p : P) (x : E) : Ea a (evE p) x = evE (D a p) x := by
  induction p using MvPolynomial.induction_on with
  | C c =>
    have : evE (C c) = fun _ => c := funext fun _ => evE_C c _
    rw [this, Ea_const]; simp
  | add p q hp hq =>
    have : evE (p + q) = fun x => evE p x + evE q x := funext fun x => evE_add p q x
    rw [this, Ea_add a (evE_diff p) (evE_diff q), hp, hq, map_add, evE_add]
  | mul_X p i hp =>
    have : evE (p * X i) = fun x => evE p x * ((x i : ℝ) : ℂ) := funext fun x => by simp
    rw [this, Ea_mul a (evE_diff p) ((coord_contDiff i (n := 1)).differentiable one_ne_zero), hp,
      Ea_coord, Derivation.leibniz, D_X]
    simp only [smul_eq_mul, evE_add, evE_mul, evE_X, evE_dval]; ring

/-- Item 3 for polynomials: `∫_{S³} (D a p) dσ = 0`. -/
theorem integral_D_poly (a : Fin 3) (p : P) : ∫ x : S3, evE (D a p) x ∂σ = 0 := by
  have e : (fun x : S3 => evE (D a p) x) = fun x : S3 => Ea a (evE p) x :=
    funext fun x => (Ea_poly a p x).symm
  rw [e]; exact integral_Ea a (evE_contDiff p)

/-! ### Polynomial tensor fields: campaign 51's `nab`/`lap` are `nabA`/`lapA` -/

/-- Campaign 51's tensor fields. -/
abbrev Ten := Fin 3 → Fin 3 → P

/-- Campaign 51's `nab a` written out (`nab a T b c = D a (T b c) + Lt a T b c`, `Lt_apply`). -/
noncomputable def nabP (a : Fin 3) (T : Ten) : Ten :=
  fun b c => D a (T b c) + (-(∑ d, C (eps a b d) * T d c) - ∑ d, C (eps a c d) * T b d)

/-- Campaign 51's `lap = Σ_a nab a * nab a`, written out. -/
noncomputable def lapP (T : Ten) : Ten := fun b c => ∑ a, nabP a (nabP a T) b c

/-- A polynomial tensor field as an analytic one. -/
noncomputable def evT (T : Ten) : TenA := fun b c => evE (T b c)

lemma evT_CD (T : Ten) (n : WithTop ℕ∞) : CD n (evT T) := fun b c => evE_contDiff (T b c)

theorem evT_nab (a : Fin 3) (T : Ten) : nabA a (evT T) = evT (nabP a T) := by
  funext b c x; simp [nabA, nabP, evT, Ea_poly, Lc]

theorem evT_lap (T : Ten) : lapA (evT T) = evT (lapP T) := by
  funext b c x; simp only [lapA, evT_nab]; simp [lapP, evT]

/-- **The symmetry of campaign 51's `∇²` on `L²(σ)`**, for polynomial tensor fields. -/
theorem lapP_symm (T U : Ten) :
    ∫ x : S3, ip (evT (lapP T)) (evT U) x ∂σ = ∫ x : S3, ip (evT T) (evT (lapP U)) x ∂σ := by
  rw [← evT_lap, ← evT_lap]; exact lap_symm _ _ (evT_CD T 2) (evT_CD U 2)

end Poly

end ShadowProbe.S3Integration

#print axioms ShadowProbe.S3Integration.σ_finite_nonzero
#print axioms ShadowProbe.S3Integration.right_invariant
#print axioms ShadowProbe.S3Integration.left_invariant
#print axioms ShadowProbe.S3Integration.integral_Ea
#print axioms ShadowProbe.S3Integration.ibp
#print axioms ShadowProbe.S3Integration.nab_skew
#print axioms ShadowProbe.S3Integration.lap_symm
#print axioms ShadowProbe.S3Integration.neg_lap_nonneg
#print axioms ShadowProbe.S3Integration.Ea_poly
#print axioms ShadowProbe.S3Integration.integral_D_poly
#print axioms ShadowProbe.S3Integration.lapP_symm

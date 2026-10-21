import Mathlib.Algebra.MvPolynomial.Derivation
import Mathlib.RingTheory.Derivation.Lie
import Mathlib.Algebra.Lie.Sl2
import Mathlib.Algebra.Lie.OfAssociative
import Mathlib.LinearAlgebra.Eigenspace.Basic
import Mathlib.Analysis.Complex.RealDeriv
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Deriv

/-! # Campaign 51, piece T: the TT spectrum of the round `S³`, lower half

The unit `S³ ⊂ ℝ⁴ = ℍ`. Its left-invariant frame `E_a(q) = q·u_a` (`u = i, j, k`) has `[E_a, E_b] = 2ε_abc E_c`, the
corpus's convention (`probes/S3Frame.lean`: `strC`, `nabF`, `s3_tt_eigen`). We let the frame fields act as
derivations `D a` of the complex polynomial functions `P = ℂ[x₀,x₁,x₂,x₃]`; they are tangent to every sphere
(`tangent_D`), so they act on functions restricted to `S³`. A symmetric 2-tensor is its frame components
`h : Fin 3 → Fin 3 → P`. The Levi-Civita connection is `∇_{E_a}E_b = ε_abc E_c`:
`(∇_a h)_bc = E_a h_bc − ε_abd h_dc − ε_acd h_bd` (`nab`, = `S3Frame.nabF` plus the derivative term), the rough
Laplacian is `∇² = Σ_a ∇_a∇_a` (`lap`), and TT means symmetric, `h_aa = 0`, `∇^a h_ab = 0`.

The corpus convention (rows 60, 63, 68, 70, 73): level `m ≥ 3`, `−∇²h = (m² − 3) h`, `deg = 2(m² − 4)`.

**Built.** For every `N` (level `m = N + 3`), a family of `2(m² − 4)` TT tensor fields with `−∇²h = (m²−3)h`
whose restrictions to `S³` are linearly independent (`tt_level_multiplicity`). They are
`f_Y^q f_K^p (w^N v⊗v)` and `f_Y^q f_K^p (w^N p⊗p)`, two `sl₂ × sl₂` (SO(4)) multiplets, built from Mathlib's
`IsSl2Triple` primitive-vector theory. Completeness (that these are all) is not built: see the report. -/

open MvPolynomial

namespace ShadowProbe.S3TTSpectrum

/-! ## 1. The frame on `ℝ⁴ = ℍ` -/

abbrev P := MvPolynomial (Fin 4) ℂ

/-- `D_a (X i)`: the left-invariant field `q ↦ q·u_a`, `u = (i, j, k)`. -/
noncomputable def dval : Fin 3 → Fin 4 → P
  | 0 => ![-X 1, X 0, X 3, -X 2]
  | 1 => ![-X 2, -X 3, X 0, X 1]
  | 2 => ![-X 3, X 2, -X 1, X 0]

/-- `Y_a (X i)`: the right-invariant field `q ↦ u_a·q`. -/
noncomputable def yval : Fin 3 → Fin 4 → P
  | 0 => ![-X 1, X 0, -X 3, X 2]
  | 1 => ![-X 2, X 3, X 0, -X 1]
  | 2 => ![-X 3, -X 2, X 1, X 0]

/-- The left-invariant frame fields, as derivations. -/
noncomputable def D (a : Fin 3) : Derivation ℂ P P := mkDerivation ℂ (dval a)
/-- The right-invariant fields (they generate left translations, which preserve the left frame). -/
noncomputable def Y (a : Fin 3) : Derivation ℂ P P := mkDerivation ℂ (yval a)

@[simp] lemma D_X (a : Fin 3) (i : Fin 4) : D a (X i) = dval a i := mkDerivation_X _ _ _
@[simp] lemma Y_X (a : Fin 3) (i : Fin 4) : Y a (X i) = yval a i := mkDerivation_X _ _ _
@[simp] lemma C_two : (C 2 : P) = 2 := map_ofNat C 2

/-- The Levi-Civita symbol (as in `S3Frame.eps3`), complex-valued. -/
def eps : Fin 3 → Fin 3 → Fin 3 → ℂ :=
  ![![![0, 0, 0], ![0, 0, 1], ![0, -1, 0]],
    ![![0, 0, -1], ![0, 0, 0], ![1, 0, 0]],
    ![![0, 1, 0], ![-1, 0, 0], ![0, 0, 0]]]

/-- **The frame structure constants**: `[E_a, E_b] = 2 ε_abc E_c`. -/
theorem frame_bracket (a b : Fin 3) : ⁅D a, D b⁆ = ∑ c, (2 * eps a b c) • D c := by
  fin_cases a <;> fin_cases b <;>
  · apply derivation_ext; intro i
    fin_cases i <;> simp [Derivation.commutator_apply, dval, Fin.sum_univ_three, eps, smul_eq_C_mul] <;> ring

/-- The right-invariant fields: `[Y_a, Y_b] = −2 ε_abc Y_c`. -/
theorem right_bracket (a b : Fin 3) : ⁅Y a, Y b⁆ = ∑ c, (-2 * eps a b c) • Y c := by
  fin_cases a <;> fin_cases b <;>
  · apply derivation_ext; intro i
    fin_cases i <;> simp [Derivation.commutator_apply, yval, Fin.sum_univ_three, eps, smul_eq_C_mul] <;> ring

/-- Left- and right-invariant fields commute. -/
theorem left_right_commute (a b : Fin 3) : ⁅D a, Y b⁆ = 0 := by
  fin_cases a <;> fin_cases b <;>
  · apply derivation_ext; intro i
    fin_cases i <;> simp [Derivation.commutator_apply, dval, yval] <;> ring

/-- `ρ = |x|²`. -/
noncomputable def rho : P := ∑ i, X i ^ 2

/-- Both families are tangent to the spheres `ρ = const` (algebraic form). -/
theorem D_rho (a : Fin 3) : D a rho = 0 ∧ Y a rho = 0 := by
  fin_cases a <;> constructor <;> simp [rho, Fin.sum_univ_four, dval, yval, Derivation.leibniz_pow] <;> ring

/-! ## 2. Tensor fields and the frame operators -/

/-- Frame components of a 2-tensor field. -/
abbrev Ten := Fin 3 → Fin 3 → P
/-- Frame components of a vector field. -/
abbrev Vec := Fin 3 → P

/-- A derivation acting componentwise, as a linear map in the derivation. -/
noncomputable def DtL : Derivation ℂ P P →ₗ[ℂ] Module.End ℂ Ten where
  toFun δ :=
    { toFun := fun h b c => δ (h b c)
      map_add' := fun h k => by funext b c; simp
      map_smul' := fun r h => by funext b c; simp }
  map_add' δ₁ δ₂ := by refine LinearMap.ext fun h => ?_; funext b c; simp
  map_smul' r δ := by refine LinearMap.ext fun h => ?_; funext b c; simp

@[simp] lemma DtL_apply (δ : Derivation ℂ P P) (h : Ten) (b c : Fin 3) : DtL δ h b c = δ (h b c) := rfl

/-- The connection term `(L_a h)_bc = −ε_abd h_dc − ε_acd h_bd` (`∇_{E_a}E_b = ε_abc E_c`). -/
noncomputable def Lt (a : Fin 3) : Module.End ℂ Ten where
  toFun h := fun b c => -(∑ d, C (eps a b d) * h d c) - ∑ d, C (eps a c d) * h b d
  map_add' h k := by funext b c; simp [mul_add, Finset.sum_add_distrib]; ring
  map_smul' r h := by
    funext b c
    simp only [Pi.smul_apply, smul_eq_C_mul, RingHom.id_apply]
    rw [mul_sub, mul_neg, Finset.mul_sum, Finset.mul_sum]; simp only [mul_left_comm]

@[simp] lemma Lt_apply (a : Fin 3) (h : Ten) (b c : Fin 3) :
    Lt a h b c = -(∑ d, C (eps a b d) * h d c) - ∑ d, C (eps a c d) * h b d := rfl

/-- The covariant derivative `∇_a`. -/
noncomputable def nab (a : Fin 3) : Module.End ℂ Ten := DtL (D a) + Lt a
/-- The rough Laplacian `∇² = Σ_a ∇_a ∇_a` (the first-slot connection term vanishes, `ε_aad = 0`). -/
noncomputable def lap : Module.End ℂ Ten := ∑ a, nab a * nab a
/-- The Lie derivative along `E_a`: `(£_{E_a} h)_bc = E_a h_bc − 2ε_abd h_dc − 2ε_acd h_bd`
(`[K_a, K_b] = 2ε_abc K_c`). -/
noncomputable def K (a : Fin 3) : Module.End ℂ Ten := DtL (D a) + (2 : ℂ) • Lt a
/-- Signs making the right-invariant fields a copy of the same bracket: `Yk = (−Y₀, Y₁, Y₂)`. -/
def sY : Fin 3 → ℂ := ![-1, 1, 1]
/-- The right-invariant fields on tensors (`[Yk_a, Yk_b] = 2ε_abc Yk_c`). -/
noncomputable def Yk (a : Fin 3) : Module.End ℂ Ten := sY a • DtL (Y a)
/-- The Casimir of the frame action on components, `S_J = Σ_a E_a E_a` (componentwise). -/
noncomputable def SJ : Module.End ℂ Ten := ∑ a, DtL (D a) * DtL (D a)

lemma DtL_comm (δ₁ δ₂ : Derivation ℂ P P) :
    DtL δ₁ * DtL δ₂ - DtL δ₂ * DtL δ₁ = DtL ⁅δ₁, δ₂⁆ := by
  refine LinearMap.ext fun h => ?_; funext b c; simp [Derivation.commutator_apply]

lemma DtL_Lt (δ : Derivation ℂ P P) (a : Fin 3) : DtL δ * Lt a = Lt a * DtL δ := by
  refine LinearMap.ext fun h => ?_; funext b c; simp [map_sum, Derivation.leibniz, derivation_C]

set_option maxHeartbeats 1000000 in
lemma Lt_bracket (a b : Fin 3) : Lt a * Lt b - Lt b * Lt a = ∑ c, eps a b c • Lt c := by
  refine LinearMap.ext fun h => ?_; funext i j
  simp only [LinearMap.sub_apply, Module.End.mul_apply, LinearMap.sum_apply, Finset.sum_apply,
      LinearMap.smul_apply, Pi.sub_apply, Pi.smul_apply, Lt_apply, Fin.sum_univ_three, smul_eq_C_mul]
  fin_cases a <;> fin_cases b <;> fin_cases i <;> fin_cases j <;> simp [eps, Fin.sum_univ_three] <;> ring

lemma DtL_D_bracket (a b : Fin 3) :
    DtL (D a) * DtL (D b) - DtL (D b) * DtL (D a) = ∑ c, (2 * eps a b c) • DtL (D c) := by
  rw [DtL_comm, frame_bracket, map_sum]; simp only [map_smul]

lemma DtL_Y_bracket (a b : Fin 3) :
    DtL (Y a) * DtL (Y b) - DtL (Y b) * DtL (Y a) = ∑ c, (-2 * eps a b c) • DtL (Y c) := by
  rw [DtL_comm, right_bracket, map_sum]; simp only [map_smul]

lemma DtL_DY (a b : Fin 3) : DtL (D a) * DtL (Y b) = DtL (Y b) * DtL (D a) := by
  have := DtL_comm (D a) (Y b); rw [left_right_commute, map_zero, sub_eq_zero] at this; exact this

/-- `[∇_b, K_a] = 2ε_bac ∇_c`. -/
lemma nab_K (b a : Fin 3) : nab b * K a - K a * nab b = ∑ c, (2 * eps b a c) • nab c := by
  have h1 := DtL_D_bracket b a
  have h2 := Lt_bracket b a
  have c1 := DtL_Lt (D b) a
  have c2 := DtL_Lt (D a) b
  have : nab b * K a - K a * nab b = (DtL (D b) * DtL (D a) - DtL (D a) * DtL (D b))
      + (2 : ℂ) • (Lt b * Lt a - Lt a * Lt b) := by
    simp only [nab, K, add_mul, mul_add, smul_mul_assoc, mul_smul_comm, c1, c2]; module
  rw [this, h1, h2]; simp only [nab, Fin.sum_univ_three, smul_add]; module

/-- `[E_b, K_a] = 2ε_bac E_c` (componentwise). -/
lemma D_K (b a : Fin 3) : DtL (D b) * K a - K a * DtL (D b) = ∑ c, (2 * eps b a c) • DtL (D c) := by
  have h1 := DtL_D_bracket b a
  have c1 := DtL_Lt (D b) a
  have : DtL (D b) * K a - K a * DtL (D b) =
      (DtL (D b) * DtL (D a) - DtL (D a) * DtL (D b)) := by
    simp only [K, add_mul, mul_add, smul_mul_assoc, mul_smul_comm, c1]; module
  rw [this, h1]

/-- `[K_a, K_b] = 2ε_abc K_c`. -/
lemma K_bracket (a b : Fin 3) : K a * K b - K b * K a = ∑ c, (2 * eps a b c) • K c := by
  have h1 := DtL_D_bracket a b
  have h2 := Lt_bracket a b
  have c1 := DtL_Lt (D a) b
  have c2 := DtL_Lt (D b) a
  have : K a * K b - K b * K a = (DtL (D a) * DtL (D b) - DtL (D b) * DtL (D a))
      + (4 : ℂ) • (Lt a * Lt b - Lt b * Lt a) := by
    simp only [K, add_mul, mul_add, smul_mul_assoc, mul_smul_comm, smul_smul, c1, c2]; module
  rw [this, h1, h2]; simp only [K, Fin.sum_univ_three, smul_add]; module

/-- `[Yk_a, Yk_b] = 2ε_abc Yk_c`. -/
lemma Yk_bracket (a b : Fin 3) : Yk a * Yk b - Yk b * Yk a = ∑ c, (2 * eps a b c) • Yk c := by
  have h1 := DtL_Y_bracket a b
  have : Yk a * Yk b - Yk b * Yk a = (sY a * sY b) • (DtL (Y a) * DtL (Y b) - DtL (Y b) * DtL (Y a)) := by
    simp only [Yk, smul_mul_assoc, mul_smul_comm, smul_smul, smul_sub]; ring_nf
  rw [this, h1]
  fin_cases a <;> fin_cases b <;> simp [Yk, sY, eps, Fin.sum_univ_three] <;> module

lemma Yt_Lt (a b : Fin 3) : DtL (Y a) * Lt b = Lt b * DtL (Y a) := DtL_Lt _ _
lemma Yt_K (a b : Fin 3) : Yk a * K b = K b * Yk a := by
  simp only [Yk, K, mul_add, add_mul, smul_mul_assoc, mul_smul_comm, Yt_Lt, DtL_DY]; module
lemma Yt_nab (a b : Fin 3) : DtL (Y a) * nab b = nab b * DtL (Y a) := by
  simp only [nab, mul_add, add_mul, Yt_Lt, DtL_DY]

/-- In any ring: `[x², k] = x[x,k] + [x,k]x`. -/
lemma comm_sq {A : Type*} [Ring A] (x k y : A) (h : x * k - k * x = y) :
    x * x * k - k * (x * x) = x * y + y * x := by
  rw [← h]; noncomm_ring

/-- A Casimir `Σ_b x_b²` commutes with `k` whenever `[x_b, k] = 2ε_bac x_c`. -/
lemma casimir_comm (x : Fin 3 → Module.End ℂ Ten) (k : Module.End ℂ Ten) (a : Fin 3)
    (hx : ∀ b, x b * k - k * x b = ∑ c, (2 * eps b a c) • x c) :
    (∑ b, x b * x b) * k = k * ∑ b, x b * x b := by
  rw [← sub_eq_zero, Finset.sum_mul, Finset.mul_sum, ← Finset.sum_sub_distrib]
  simp only [fun b => comm_sq _ _ _ (hx b)]
  fin_cases a <;> simp [Fin.sum_univ_three, eps, mul_add, add_mul, smul_mul_assoc, mul_smul_comm] <;> module

/-- **The rough Laplacian commutes with the Lie derivative along every frame field** (isometries). -/
theorem lap_K (a : Fin 3) : lap * K a = K a * lap := casimir_comm nab (K a) a (fun b => nab_K b a)
theorem SJ_K (a : Fin 3) : SJ * K a = K a * SJ := casimir_comm _ (K a) a (fun b => D_K b a)
lemma lap_Y (a : Fin 3) : lap * DtL (Y a) = DtL (Y a) * lap := by
  simp only [lap, Finset.sum_mul, Finset.mul_sum]
  exact Finset.sum_congr rfl fun b _ => by rw [mul_assoc, ← Yt_nab, ← mul_assoc, ← Yt_nab, mul_assoc]
lemma SJ_Y (a : Fin 3) : SJ * DtL (Y a) = DtL (Y a) * SJ := by
  simp only [SJ, Finset.sum_mul, Finset.mul_sum]
  exact Finset.sum_congr rfl fun b _ => by rw [mul_assoc, DtL_DY, ← mul_assoc, DtL_DY, mul_assoc]
theorem lap_Yk (a : Fin 3) : lap * Yk a = Yk a * lap := by
  simp only [Yk, smul_mul_assoc, mul_smul_comm, lap_Y]
theorem SJ_Yk (a : Fin 3) : SJ * Yk a = Yk a * SJ := by
  simp only [Yk, smul_mul_assoc, mul_smul_comm, SJ_Y]


/-! ## 3. The TT conditions and their invariance under the isometries -/

/-- Symmetric. -/
def IsSym (h : Ten) : Prop := ∀ b c, h b c = h c b

/-- The trace `h_aa`. -/
noncomputable def trL : Ten →ₗ[ℂ] P := ∑ a, LinearMap.proj a ∘ₗ LinearMap.proj a
/-- The divergence `(div h)_c = Σ_b (∇_b h)_bc` (`∇_bE_b = 0`, so this is the full `∇^b h_bc`). -/
noncomputable def dvL : Ten →ₗ[ℂ] Vec := ∑ b, LinearMap.proj b ∘ₗ nab b

@[simp] lemma trL_apply (h : Ten) : trL h = ∑ a, h a a := by simp [trL]
@[simp] lemma dvL_apply (h : Ten) (c : Fin 3) : dvL h c = ∑ b, nab b h b c := by simp [dvL]

/-- **The TT eigenspace** of `−∇²` with eigenvalue `lam`: symmetric, traceless, divergence-free, `∇²h = −lam h`. -/
noncomputable def TT (lam : ℂ) : Submodule ℂ Ten where
  carrier := {h | IsSym h ∧ trL h = 0 ∧ dvL h = 0 ∧ lap h = (-lam) • h}
  zero_mem' := ⟨fun _ _ => rfl, map_zero _, map_zero _, by simp⟩
  add_mem' := by
    rintro h k ⟨hs, ht, hd, hl⟩ ⟨ks, kt, kd, kl⟩
    refine ⟨fun b c => by simp [hs b c, ks b c], by rw [map_add, ht, kt, add_zero],
      by rw [map_add, hd, kd, add_zero], ?_⟩
    show lap (h + k) = (-lam) • (h + k); rw [map_add, hl, kl, smul_add]
  smul_mem' := by
    rintro r h ⟨hs, ht, hd, hl⟩
    refine ⟨fun b c => by simp [hs b c], by rw [map_smul, ht, smul_zero], by rw [map_smul, hd, smul_zero], ?_⟩
    show lap (r • h) = (-lam) • (r • h); rw [map_smul, hl, smul_comm]

/-- The Lie derivative along `E_a` on vector fields: `(£v)_c = E_a v_c − 2ε_acd v_d`. -/
noncomputable def KV (a : Fin 3) : Module.End ℂ Vec :=
  LinearMap.pi fun c => (D a).toLinearMap ∘ₗ LinearMap.proj c -
    (2 : ℂ) • ∑ d, LinearMap.mulLeft ℂ (C (eps a c d)) ∘ₗ LinearMap.proj d

lemma KV_apply (a : Fin 3) (v : Vec) (c : Fin 3) :
    KV a v c = D a (v c) - 2 * ∑ d, C (eps a c d) * v d := by
  simp [KV, smul_eq_C_mul, LinearMap.sum_apply]

lemma K_apply (a : Fin 3) (h : Ten) (b c : Fin 3) :
    K a h b c = D a (h b c) - 2 * (∑ d, C (eps a b d) * h d c) - 2 * ∑ d, C (eps a c d) * h b d := by
  simp [K, smul_eq_C_mul]; ring

lemma nab_K_apply (b a : Fin 3) (h : Ten) :
    nab b (K a h) = K a (nab b h) + ∑ e, (2 * eps b a e) • nab e h := by
  have := LinearMap.congr_fun (nab_K b a) h
  simp only [LinearMap.sub_apply, Module.End.mul_apply, LinearMap.sum_apply, LinearMap.smul_apply] at this
  rw [← this]; abel

set_option maxHeartbeats 1000000 in
lemma K_sym (a : Fin 3) {h : Ten} (hs : IsSym h) : IsSym (K a h) := by
  intro b c
  have s01 := hs 0 1; have s02 := hs 0 2; have s12 := hs 1 2
  fin_cases a <;> fin_cases b <;> fin_cases c <;> simp [K_apply, Fin.sum_univ_three, eps, s01, s02, s12] <;> ring

lemma K_tr (a : Fin 3) (h : Ten) : trL (K a h) = D a (trL h) := by
  fin_cases a <;> simp [K_apply, Fin.sum_univ_three, eps] <;> ring

lemma K_dv (a : Fin 3) (h : Ten) : dvL (K a h) = KV a (dvL h) := by
  funext c
  simp only [dvL_apply, nab_K_apply, LinearMap.add_apply, Pi.add_apply]
  fin_cases a <;> fin_cases c <;>
  simp [K_apply, KV_apply, Fin.sum_univ_three, eps, smul_eq_C_mul, Finset.sum_apply] <;> ring

/-- `K_a` preserves every TT eigenspace. -/
theorem K_TT (a : Fin 3) {lam : ℂ} {h : Ten} (hh : h ∈ TT lam) : K a h ∈ TT lam := by
  obtain ⟨hs, ht, hd, hl⟩ := hh
  refine ⟨K_sym a hs, by rw [K_tr, ht]; simp, by rw [K_dv, hd, map_zero], ?_⟩
  have := LinearMap.congr_fun (lap_K a) h
  simp only [Module.End.mul_apply] at this
  rw [this, hl, map_smul]

/-- The right-invariant fields preserve every TT eigenspace. -/
theorem Y_TT (a : Fin 3) {lam : ℂ} {h : Ten} (hh : h ∈ TT lam) : DtL (Y a) h ∈ TT lam := by
  obtain ⟨hs, ht, hd, hl⟩ := hh
  refine ⟨fun b c => by simp [hs b c], ?_, ?_, ?_⟩
  · simp only [trL_apply] at ht ⊢; simp [← map_sum, ht]
  · funext c
    have e : ∀ b, nab b (DtL (Y a) h) = DtL (Y a) (nab b h) := fun b => by
      have := LinearMap.congr_fun (Yt_nab a b) h; simpa using this.symm
    have := congrFun hd c
    simp only [dvL_apply, Pi.zero_apply] at this ⊢
    simp only [e, DtL_apply, ← map_sum, this, map_zero]
  · have := LinearMap.congr_fun (lap_Y a) h
    simp only [Module.End.mul_apply] at this
    rw [this, hl, map_smul]

lemma Yk_TT (a : Fin 3) {lam : ℂ} {h : Ten} (hh : h ∈ TT lam) : Yk a h ∈ TT lam :=
  (TT lam).smul_mem _ (Y_TT a hh)

/-- Operators preserving every TT eigenspace. -/
def Stab (O : Module.End ℂ Ten) : Prop := ∀ lam h, h ∈ TT lam → O h ∈ TT lam

lemma Stab.add {O O' : Module.End ℂ Ten} (h1 : Stab O) (h2 : Stab O') : Stab (O + O') :=
  fun lam h hh => (TT lam).add_mem (h1 lam h hh) (h2 lam h hh)
lemma Stab.smul {O : Module.End ℂ Ten} (r : ℂ) (h1 : Stab O) : Stab (r • O) :=
  fun lam h hh => (TT lam).smul_mem r (h1 lam h hh)
lemma Stab.neg {O : Module.End ℂ Ten} (h1 : Stab O) : Stab (-O) :=
  fun lam h hh => by simpa using (TT lam).neg_mem (h1 lam h hh)
lemma Stab.sub {O O' : Module.End ℂ Ten} (h1 : Stab O) (h2 : Stab O') : Stab (O - O') :=
  fun lam h hh => (TT lam).sub_mem (h1 lam h hh) (h2 lam h hh)
lemma Stab.mul {O O' : Module.End ℂ Ten} (h1 : Stab O) (h2 : Stab O') : Stab (O * O') :=
  fun lam h hh => h1 lam _ (h2 lam h hh)
lemma Stab.pow {O : Module.End ℂ Ten} (h1 : Stab O) (n : ℕ) : Stab (O ^ n) := by
  induction n with
  | zero => intro lam h hh; simpa using hh
  | succ n ih => rw [pow_succ]; exact ih.mul h1

/-! ## 4. Products with functions, and the two seeds -/

/-- `f · T`. -/
noncomputable def smulT (f : P) (T : Ten) : Ten := fun b c => f * T b c

lemma nab_smulT (a : Fin 3) (f : P) (T : Ten) :
    nab a (smulT f T) = smulT (D a f) T + smulT f (nab a T) := by
  funext b c; simp [nab, smulT, Derivation.leibniz, Fin.sum_univ_three]; ring

lemma lap_smulT (f : P) (T : Ten) (b c : Fin 3) :
    lap (smulT f T) b c = (∑ a, D a (D a f)) * T b c + 2 * ∑ a, D a f * nab a T b c + f * lap T b c := by
  simp only [lap, LinearMap.sum_apply, Finset.sum_apply, Module.End.mul_apply, nab_smulT, map_add]
  simp [smulT, Fin.sum_univ_three]; ring

lemma SJ_smulT (f : P) (T : Ten) (b c : Fin 3) :
    SJ (smulT f T) b c = (∑ a, D a (D a f)) * T b c + 2 * ∑ a, D a f * D a (T b c)
      + f * ∑ a, D a (D a (T b c)) := by
  simp [SJ, smulT, Fin.sum_univ_three, Derivation.leibniz]; ring

lemma dv_smulT (f : P) (T : Ten) (c : Fin 3) :
    dvL (smulT f T) c = ∑ a, D a f * T a c + f * dvL T c := by
  simp only [dvL_apply, nab_smulT]; simp [smulT, Fin.sum_univ_three]; ring

lemma K_smulT (a : Fin 3) (f : P) (T : Ten) :
    K a (smulT f T) = smulT (D a f) T + smulT f (K a T) := by
  funext b c; simp [K_apply, smulT, Derivation.leibniz, Fin.sum_univ_three, smul_eq_C_mul]; ring

lemma Yk_smulT (a : Fin 3) (f : P) (T : Ten) :
    Yk a (smulT f T) = smulT (sY a • Y a f) T + smulT f (Yk a T) := by
  funext b c; simp [Yk, smulT, Derivation.leibniz, smul_eq_C_mul]; ring

/-! The holomorphic coordinates `w = x₀ + i x₃`, `u = x₁ + i x₂`: the frame acts on them as spin `½`. -/

noncomputable def ii : P := C Complex.I
lemma ii_sq : ii ^ 2 = -1 := by simp [ii, ← map_pow]
lemma ii_three : ii ^ 3 = -ii := by rw [pow_succ, ii_sq]; ring
lemma ii_four : ii ^ 4 = 1 := by
  have : ii ^ 4 = (ii ^ 2) ^ 2 := by ring
  rw [this, ii_sq]; ring
@[simp] lemma D_ii (a : Fin 3) : D a ii = 0 := derivation_C _ _
@[simp] lemma Y_ii (a : Fin 3) : Y a ii = 0 := derivation_C _ _
@[simp] lemma C_I : (C Complex.I : P) = ii := rfl

/-- Normalise, then reduce powers of `i`. -/
lemma ii_five : ii ^ 5 = ii := by rw [pow_succ, ii_four, one_mul]
lemma ii_six : ii ^ 6 = -1 := by rw [pow_succ, ii_five, ← sq, ii_sq]
lemma ii_seven : ii ^ 7 = -ii := by rw [pow_succ, ii_six]; ring
lemma ii_eight : ii ^ 8 = 1 := by rw [pow_succ, ii_seven, neg_mul, ← sq, ii_sq, neg_neg]
@[simp] lemma C_3 : (C 3 : P) = 3 := map_ofNat C 3
@[simp] lemma C_4 : (C 4 : P) = 4 := map_ofNat C 4
@[simp] lemma C_6 : (C 6 : P) = 6 := map_ofNat C 6
@[simp] lemma D_two (a : Fin 3) : D a (2 : P) = 0 := by
  rw [show (2 : P) = C 2 from (map_ofNat C 2).symm]; exact derivation_C _ _
@[simp] lemma Y_two (a : Fin 3) : Y a (2 : P) = 0 := by
  rw [show (2 : P) = C 2 from (map_ofNat C 2).symm]; exact derivation_C _ _

macro "iring" : tactic => `(tactic| (ring_nf <;>
  (try simp only [ii_sq, ii_three, ii_four, ii_five, ii_six, ii_seven, ii_eight]) <;> (try ring_nf)))

noncomputable def w : P := X 0 + ii * X 3
noncomputable def u : P := X 1 + ii * X 2

@[simp] lemma D0w : D 0 w = -u := by simp [w, u, dval]; iring
@[simp] lemma D1w : D 1 w = ii * u := by simp [w, u, dval]; iring
@[simp] lemma D2w : D 2 w = ii * w := by simp [w, dval]; iring
@[simp] lemma D0u : D 0 u = w := by simp [w, u, dval]
@[simp] lemma D1u : D 1 u = ii * w := by simp [w, u, dval]; iring
@[simp] lemma D2u : D 2 u = -(ii * u) := by simp [u, dval]; iring
@[simp] lemma Y2w : Y 2 w = ii * w := by simp [w, yval]; iring
@[simp] lemma Y2u : Y 2 u = ii * u := by simp [u, yval]; iring
lemma Y01w : Y 0 w + ii * Y 1 w = 0 := by simp [w, yval]; iring
lemma Y01u : Y 0 u + ii * Y 1 u = 0 := by simp [u, yval]; iring

/-- `Σ_a δ_a(w^N) Φ_a = N c w^N Ψ` whenever `Σ_a δ_a(w) Φ_a = c w Ψ`. -/
lemma wpow_contract (δ : Fin 3 → Derivation ℂ P P) (N : ℕ) (Φ : Fin 3 → P) (c Ψ : P)
    (h : ∑ a, δ a w * Φ a = c * w * Ψ) : ∑ a, δ a (w ^ N) * Φ a = N * c * w ^ N * Ψ := by
  cases N with
  | zero => simp
  | succ n =>
    simp only [Derivation.leibniz_pow, smul_eq_mul, nsmul_eq_mul, Nat.add_sub_cancel]
    have : ∑ a, ↑(n + 1) * (w ^ n * δ a w) * Φ a = ↑(n + 1) * w ^ n * ∑ a, δ a w * Φ a := by
      rw [Finset.mul_sum]; exact Finset.sum_congr rfl fun a _ => by ring
    rw [this, h]; push_cast; ring

lemma Bww : ∑ a, D a w * D a w = -1 * w * w := by simp [Fin.sum_univ_three]; iring

/-- `Σ_a E_aE_a w^N = −N(N+2) w^N`: `w^N` has spin `N/2`. -/
lemma S_wpow (N : ℕ) : ∑ a, D a (D a (w ^ N)) = -((N : P) * (N + 2)) * w ^ N := by
  induction N with
  | zero => simp
  | succ n ih =>
    have hG := wpow_contract D n (fun a => D a w) (-1) w Bww
    have hS : ∑ a, D a (D a w) = -3 * w := by simp [Fin.sum_univ_three]; iring
    have : ∑ a, D a (D a (w ^ (n + 1))) =
        (∑ a, D a (D a (w ^ n))) * w + 2 * ∑ a, D a (w ^ n) * D a w + w ^ n * ∑ a, D a (D a w) := by
      simp only [pow_succ, Derivation.leibniz, smul_eq_mul, map_add, Fin.sum_univ_three]; ring
    rw [this, ih, hG, hS]; push_cast; ring

/-- **Level raising.** If `T` is a level-3 TT tensor (`−∇²T = 6T`) with the two contraction conditions against
`dw`, then `w^N T` is TT at level `m = N + 3`, eigenvalue `m² − 3`. -/
theorem seed_TT (T : Ten) (N : ℕ) (hs : IsSym T) (ht : trL T = 0) (hd : dvL T = 0)
    (hl : lap T = (-6 : ℂ) • T) (hx : ∀ b c, ∑ a, D a w * nab a T b c = -2 * w * T b c)
    (hg : ∀ c, ∑ a, D a w * T a c = 0 * w * 0) :
    smulT (w ^ N) T ∈ TT (((N : ℂ) + 3) ^ 2 - 3) := by
  refine ⟨fun b c => by simp [smulT, hs b c], ?_, ?_, ?_⟩
  · simp only [trL_apply] at ht ⊢; simp only [smulT, ← Finset.mul_sum, ht, mul_zero]
  · funext c; rw [dv_smulT, wpow_contract D N _ 0 0 (hg c), hd]; simp
  · funext b c
    rw [lap_smulT, S_wpow, wpow_contract D N _ (-2) _ (hx b c), hl]
    simp [smulT, smul_eq_C_mul]; ring


/-! ## 5. The two level-3 seeds

`TU = v⊗v`, `v = (1, −i, 0)`: frame-constant (a left-invariant tensor), the top of `V₀ ⊗ V₂` (spin `k = j + 2`).
`TL = p⊗p`, `p = (i(w²+u²), u²−w², 2uw)`: `K`-invariant (a right-invariant tensor), components of spin `j = 2`
(`k = j − 2`). Both are null (`v·v = p·p = 0`). -/

noncomputable def vC : Fin 3 → P := ![1, -ii, 0]
noncomputable def pR : Fin 3 → P := ![ii * (w ^ 2 + u ^ 2), u ^ 2 - w ^ 2, u * w + u * w]
noncomputable def outer (v : Fin 3 → P) : Ten := fun b c => v b * v c
noncomputable def TU : Ten := outer vC
noncomputable def TL : Ten := outer pR

lemma outer_sym (v : Fin 3 → P) : IsSym (outer v) := fun b c => mul_comm _ _

@[simp] lemma D_vC (a : Fin 3) (b : Fin 3) : D a (vC b) = 0 := by fin_cases b <;> simp [vC]
@[simp] lemma Y_vC (a : Fin 3) (b : Fin 3) : Y a (vC b) = 0 := by fin_cases b <;> simp [vC]
lemma D_TU (a b c : Fin 3) : D a (TU b c) = 0 := by simp [TU, outer, Derivation.leibniz]
lemma nab_TU (a : Fin 3) : nab a TU = Lt a TU := by
  funext b c; simp [nab, D_TU]
lemma D_LtTU (a e b c : Fin 3) : D a (Lt e TU b c) = 0 := by
  simp only [Lt_apply, map_sub, map_neg, Fin.sum_univ_three, map_add, Derivation.leibniz, D_TU,
    derivation_C, smul_zero, add_zero, neg_zero, sub_zero]

theorem TU_tr : trL TU = 0 := by simp [TU, outer, vC, Fin.sum_univ_three]; iring
theorem TU_dv : dvL TU = 0 := by
  funext c; simp only [dvL_apply, nab_TU]
  fin_cases c <;> simp [TU, outer, vC, Fin.sum_univ_three, eps] <;> iring
/-- **Level 3, frame-constant seed** (= `S3Frame.s3_tt_eigen` on this tensor): `−∇²TU = 6 TU`. -/
theorem TU_lap : lap TU = (-6 : ℂ) • TU := by
  funext b c
  have e : ∀ a, nab a (nab a TU) = Lt a (Lt a TU) := fun a => by
    rw [nab_TU, nab, LinearMap.add_apply]; funext b c
    simp only [Pi.add_apply, DtL_apply, D_LtTU, zero_add]
  simp only [lap, LinearMap.sum_apply, Finset.sum_apply, Module.End.mul_apply, e]
  fin_cases b <;> fin_cases c <;> simp [TU, outer, vC, Fin.sum_univ_three, eps, smul_eq_C_mul] <;> iring
theorem TU_hx (b c : Fin 3) : ∑ a, D a w * nab a TU b c = -2 * w * TU b c := by
  simp only [nab_TU]
  fin_cases b <;> fin_cases c <;> simp [TU, outer, vC, Fin.sum_univ_three, eps] <;> iring
theorem TU_hg (c : Fin 3) : ∑ a, D a w * TU a c = 0 * w * 0 := by
  fin_cases c <;> simp [TU, outer, vC, Fin.sum_univ_three] <;> iring


theorem TL_tr : trL TL = 0 := by simp [TL, outer, pR, Fin.sum_univ_three]; iring
theorem TL_K (a : Fin 3) : K a TL = 0 := by
  funext b c
  fin_cases a <;> fin_cases b <;> fin_cases c <;>
  simp [K_apply, TL, outer, pR, Fin.sum_univ_three, eps, Derivation.leibniz, Derivation.leibniz_pow,
    -mul_eq_zero] <;> iring
/-- For a `K`-invariant tensor, `E_a T = −2 L_a T` and `∇_a T = −L_a T`: no derivatives remain. -/
lemma Kinv_D {T : Ten} (hT : ∀ a, K a T = 0) (a : Fin 3) : DtL (D a) T = (-2 : ℂ) • Lt a T := by
  have := hT a; simp only [K, LinearMap.add_apply, LinearMap.smul_apply] at this
  rw [eq_neg_of_add_eq_zero_left this, neg_smul]
lemma Kinv_nab {T : Ten} (hT : ∀ a, K a T = 0) (a : Fin 3) : nab a T = (-1 : ℂ) • Lt a T := by
  rw [nab, LinearMap.add_apply, Kinv_D hT]; module
lemma Kinv_lap {T : Ten} (hT : ∀ a, K a T = 0) : lap T = ∑ a, Lt a (Lt a T) := by
  simp only [lap, LinearMap.sum_apply, Module.End.mul_apply]
  refine Finset.sum_congr rfl fun a _ => ?_
  rw [Kinv_nab hT, map_smul, nab, LinearMap.add_apply, ← Module.End.mul_apply (DtL (D a)),
    DtL_Lt, Module.End.mul_apply, Kinv_D hT, map_smul]; module
lemma Kinv_SJ {T : Ten} (hT : ∀ a, K a T = 0) : SJ T = (4 : ℂ) • ∑ a, Lt a (Lt a T) := by
  simp only [SJ, LinearMap.sum_apply, Module.End.mul_apply, Finset.smul_sum]
  refine Finset.sum_congr rfl fun a _ => ?_
  rw [Kinv_D hT, map_smul, ← Module.End.mul_apply (DtL (D a)), DtL_Lt, Module.End.mul_apply,
    Kinv_D hT, map_smul, smul_smul]; norm_num

lemma TL_L (a b c : Fin 3) : Lt a TL b c = -(∑ d, C (eps a b d) * TL d c) - ∑ d, C (eps a c d) * TL b d := rfl

theorem TL_dv : dvL TL = 0 := by
  funext c; simp only [dvL_apply, Kinv_nab TL_K]
  fin_cases c <;> simp [TL, outer, pR, Fin.sum_univ_three, eps, smul_eq_C_mul] <;> iring
theorem TL_hx (b c : Fin 3) : ∑ a, D a w * nab a TL b c = -2 * w * TL b c := by
  simp only [Kinv_nab TL_K]
  fin_cases b <;> fin_cases c <;> simp [TL, outer, pR, Fin.sum_univ_three, eps, smul_eq_C_mul] <;> iring
theorem TL_hg (c : Fin 3) : ∑ a, D a w * TL a c = 0 * w * 0 := by
  fin_cases c <;> simp [TL, outer, pR, Fin.sum_univ_three] <;> iring
theorem TL_B (b c : Fin 3) : ∑ a, D a w * D a (TL b c) = -4 * w * TL b c := by
  have e : ∀ a, D a (TL b c) = (-2 : ℂ) • Lt a TL b c := fun a => by
    rw [← DtL_apply, Kinv_D TL_K]; rfl
  simp only [e]
  fin_cases b <;> fin_cases c <;> simp [TL, outer, pR, Fin.sum_univ_three, eps, smul_eq_C_mul] <;> iring
/-- `Σ_a L_aL_a TL = −6 TL` (spin 2 on the indices); purely algebraic. -/
lemma TL_LL : ∑ a, Lt a (Lt a TL) = (-6 : ℂ) • TL := by
  funext b c
  fin_cases b <;> fin_cases c <;>
  simp [TL, outer, pR, Fin.sum_univ_three, eps, smul_eq_C_mul, Finset.sum_apply] <;> iring
theorem TL_S (b c : Fin 3) : ∑ a, D a (D a (TL b c)) = -24 * TL b c := by
  have := congrFun (congrFun (Kinv_SJ TL_K) b) c
  rw [TL_LL] at this; simp [SJ, Finset.sum_apply, smul_eq_C_mul] at this; rw [this]; ring
/-- **Level 3, the right-invariant seed**: `−∇²TL = 6 TL`. -/
theorem TL_lap : lap TL = (-6 : ℂ) • TL := by rw [Kinv_lap TL_K, TL_LL]

/-- The upper seed at level `m = N + 3`: `w^N TU` (spins `j = N/2`, `k = N/2 + 2`). -/
noncomputable def sU (N : ℕ) : Ten := smulT (w ^ N) TU
/-- The lower seed at level `m = N + 3`: `w^N TL` (spins `j = N/2 + 2`, `k = N/2`). -/
noncomputable def sL (N : ℕ) : Ten := smulT (w ^ N) TL

/-- **Lower half, one tensor of each branch at every level `m = N + 3 ≥ 3`**: TT with `−∇²h = (m² − 3) h`. -/
theorem sU_TT (N : ℕ) : sU N ∈ TT (((N : ℂ) + 3) ^ 2 - 3) :=
  seed_TT TU N (outer_sym _) TU_tr TU_dv TU_lap TU_hx TU_hg
theorem sL_TT (N : ℕ) : sL N ∈ TT (((N : ℂ) + 3) ^ 2 - 3) :=
  seed_TT TL N (outer_sym _) TL_tr TL_dv TL_lap TL_hx TL_hg

/-! ## 6. The two `sl₂` triples (SO(4) = SU(2)_K × SU(2)_Y) -/

open Complex in
/-- In any complex algebra, `[k_a, k_b] = 2ε_abc k_c` gives the `sl₂` relations for
`h = −i k₂`, `e = k₀ − i k₁`, `f = −¼(k₀ + i k₁)`. -/
lemma sl2_rel_alg {A : Type*} [Ring A] [Algebra ℂ A] (k0 k1 k2 : A)
    (r01 : k0 * k1 = k1 * k0 + (2 : ℂ) • k2) (r20 : k2 * k0 = k0 * k2 + (2 : ℂ) • k1)
    (r12 : k1 * k2 = k2 * k1 + (2 : ℂ) • k0) :
    ⁅-I • k2, k0 - I • k1⁆ = 2 • (k0 - I • k1) ∧
    ⁅-I • k2, -((1 / 4 : ℂ) • (k0 + I • k1))⁆ = -(2 • -((1 / 4 : ℂ) • (k0 + I • k1))) ∧
    ⁅k0 - I • k1, -((1 / 4 : ℂ) • (k0 + I • k1))⁆ = -I • k2 := by
  refine ⟨?_, ?_, ?_⟩ <;>
  · simp only [Ring.lie_def, mul_sub, sub_mul, mul_add, add_mul, mul_neg, neg_mul, smul_mul_assoc,
      mul_smul_comm, smul_smul, r01, r20, r12, two_nsmul, smul_add, smul_neg, neg_smul]
    match_scalars <;> (try ring_nf) <;> (try simp only [I_sq]) <;> (try ring_nf)

open Complex in
lemma sl2_rel (k : Fin 3 → Module.End ℂ Ten)
    (hk : ∀ a b, k a * k b - k b * k a = ∑ c, (2 * eps a b c) • k c) :
    ⁅-I • k 2, k 0 - I • k 1⁆ = 2 • (k 0 - I • k 1) ∧
    ⁅-I • k 2, -((1 / 4 : ℂ) • (k 0 + I • k 1))⁆ = -(2 • -((1 / 4 : ℂ) • (k 0 + I • k 1))) ∧
    ⁅k 0 - I • k 1, -((1 / 4 : ℂ) • (k 0 + I • k 1))⁆ = -I • k 2 := by
  refine sl2_rel_alg (k 0) (k 1) (k 2) ?_ ?_ ?_
  · have := hk 0 1; simp [Fin.sum_univ_three, eps] at this; rw [← this]; abel
  · have := hk 2 0; simp [Fin.sum_univ_three, eps] at this; rw [← this]; abel
  · have := hk 1 2; simp [Fin.sum_univ_three, eps] at this; rw [← this]; abel

open Complex in
noncomputable def hK : Module.End ℂ Ten := -I • K 2
open Complex in
noncomputable def eK : Module.End ℂ Ten := K 0 - I • K 1
open Complex in
noncomputable def fK : Module.End ℂ Ten := -((1 / 4 : ℂ) • (K 0 + I • K 1))
open Complex in
noncomputable def hY : Module.End ℂ Ten := -I • Yk 2
open Complex in
noncomputable def eY : Module.End ℂ Ten := Yk 0 - I • Yk 1
open Complex in
noncomputable def fY : Module.End ℂ Ten := -((1 / 4 : ℂ) • (Yk 0 + I • Yk 1))

lemma relK : ⁅hK, eK⁆ = 2 • eK ∧ ⁅hK, fK⁆ = -(2 • fK) ∧ ⁅eK, fK⁆ = hK := sl2_rel K K_bracket
lemma relY : ⁅hY, eY⁆ = 2 • eY ∧ ⁅hY, fY⁆ = -(2 • fY) ∧ ⁅eY, fY⁆ = hY := sl2_rel Yk Yk_bracket

lemma comm_comb (x y : Fin 3 → Module.End ℂ Ten) (h : ∀ a b, Commute (x a) (y b)) (α β : Fin 3 → ℂ) :
    Commute (∑ a, α a • x a) (∑ b, β b • y b) :=
  Commute.sum_left _ _ _ fun a _ => Commute.sum_right _ _ _ fun b _ => ((h a b).smul_left _).smul_right _

open Complex in
lemma combs : hK = ∑ a, ![0, 0, -I] a • K a ∧ eK = ∑ a, ![1, -I, 0] a • K a ∧
    fK = ∑ a, ![-1 / 4, -I / 4, 0] a • K a ∧ hY = ∑ a, ![0, 0, -I] a • Yk a ∧
    eY = ∑ a, ![1, -I, 0] a • Yk a ∧ fY = ∑ a, ![-1 / 4, -I / 4, 0] a • Yk a := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩ <;> simp [Fin.sum_univ_three, hK, eK, fK, hY, eY, fY] <;> module

lemma comm_KY {A B : Module.End ℂ Ten} (hA : ∃ α : Fin 3 → ℂ, A = ∑ a, α a • K a)
    (hB : ∃ β : Fin 3 → ℂ, B = ∑ b, β b • Yk b) : Commute A B := by
  obtain ⟨α, rfl⟩ := hA; obtain ⟨β, rfl⟩ := hB
  exact comm_comb K Yk (fun a b => (Yt_K b a).symm) α β

lemma comm_SJ_K {A : Module.End ℂ Ten} (hA : ∃ α : Fin 3 → ℂ, A = ∑ a, α a • K a) : Commute SJ A := by
  obtain ⟨α, rfl⟩ := hA
  exact Commute.sum_right _ _ _ fun a _ => (show Commute SJ (K a) from SJ_K a).smul_right _
lemma comm_SJ_Y {A : Module.End ℂ Ten} (hA : ∃ α : Fin 3 → ℂ, A = ∑ a, α a • Yk a) : Commute SJ A := by
  obtain ⟨α, rfl⟩ := hA
  exact Commute.sum_right _ _ _ fun a _ => (show Commute SJ (Yk a) from SJ_Yk a).smul_right _

/-! The seeds are highest-weight vectors. -/

lemma eK_smulT (f : P) (T : Ten) :
    eK (smulT f T) = smulT (D 0 f - ii * D 1 f) T + smulT f (eK T) := by
  funext b c; simp [eK, K_smulT, smulT, smul_eq_C_mul]; ring
lemma hK_smulT (f : P) (T : Ten) : hK (smulT f T) = smulT (-ii * D 2 f) T + smulT f (hK T) := by
  funext b c; simp [hK, K_smulT, smulT, smul_eq_C_mul]; ring
lemma eY_smulT (f : P) (T : Ten) :
    eY (smulT f T) = smulT (-(Y 0 f + ii * Y 1 f)) T + smulT f (eY T) := by
  funext b c; simp [eY, Yk_smulT, smulT, smul_eq_C_mul, sY]; ring
lemma hY_smulT (f : P) (T : Ten) : hY (smulT f T) = smulT (-ii * Y 2 f) T + smulT f (hY T) := by
  funext b c; simp [hY, Yk_smulT, smulT, smul_eq_C_mul, sY]; ring

lemma eJ_wpow (N : ℕ) : D 0 (w ^ N) - ii * D 1 (w ^ N) = 0 := by
  have := wpow_contract D N ![1, -ii, 0] 0 0 (by simp [Fin.sum_univ_three]; iring)
  simp only [Fin.sum_univ_three, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two,
    Matrix.head_cons, Matrix.tail_cons] at this; linear_combination this
lemma hJ_wpow (N : ℕ) : -ii * D 2 (w ^ N) = N * w ^ N := by
  have := wpow_contract D N ![0, 0, -ii] 1 1 (by simp [Fin.sum_univ_three]; iring)
  simp only [Fin.sum_univ_three, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two,
    Matrix.head_cons, Matrix.tail_cons] at this; linear_combination this
lemma eYw_wpow (N : ℕ) : Y 0 (w ^ N) + ii * Y 1 (w ^ N) = 0 := by
  have := wpow_contract Y N ![1, ii, 0] 0 0 (by simp [Fin.sum_univ_three]; linear_combination Y01w)
  simp only [Fin.sum_univ_three, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two,
    Matrix.head_cons, Matrix.tail_cons] at this; linear_combination this
lemma hYw_wpow (N : ℕ) : -ii * Y 2 (w ^ N) = N * w ^ N := by
  have := wpow_contract Y N ![0, 0, -ii] 1 1 (by simp [Fin.sum_univ_three]; iring)
  simp only [Fin.sum_univ_three, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two,
    Matrix.head_cons, Matrix.tail_cons] at this; linear_combination this

/-- `eY` on components is minus the derivation `Y₀ + iY₁`, which kills `w` and `u`. -/
noncomputable def eYd : Derivation ℂ P P := Y 0 + Complex.I • Y 1
@[simp] lemma eYd_w : eYd w = 0 := by simp [eYd, smul_eq_C_mul]; linear_combination Y01w
@[simp] lemma eYd_u : eYd u = 0 := by simp [eYd, smul_eq_C_mul]; linear_combination Y01u
@[simp] lemma eYd_ii : eYd ii = 0 := derivation_C _ _
@[simp] lemma eYd_two : eYd (2 : P) = 0 := by
  rw [show (2 : P) = C 2 from (map_ofNat C 2).symm]; exact derivation_C _ _
lemma eY_apply (T : Ten) (b c : Fin 3) : eY T b c = -eYd (T b c) := by
  simp [eY, Yk, eYd, sY, smul_eq_C_mul]; ring
lemma hY_apply (T : Ten) (b c : Fin 3) : hY T b c = -ii * Y 2 (T b c) := by
  simp [hY, Yk, sY, smul_eq_C_mul]

lemma TU_Y (a : Fin 3) (b c : Fin 3) : Y a (TU b c) = 0 := by simp [TU, outer, Derivation.leibniz]
lemma eK_TU : eK TU = 0 := by
  funext b c; fin_cases b <;> fin_cases c <;>
  simp [eK, K_apply, D_TU, TU, outer, vC, Fin.sum_univ_three, eps, smul_eq_C_mul] <;> iring
lemma hK_TU : hK TU = (4 : ℂ) • TU := by
  funext b c; fin_cases b <;> fin_cases c <;>
  simp [hK, K_apply, D_TU, TU, outer, vC, Fin.sum_univ_three, eps, smul_eq_C_mul] <;> iring
lemma eY_TU : eY TU = 0 := by funext b c; simp [eY, Yk, TU_Y]
lemma hY_TU : hY TU = (0 : ℂ) • TU := by funext b c; simp [hY, Yk, TU_Y]
lemma eK_TL : eK TL = 0 := by simp [eK, TL_K]
lemma hK_TL : hK TL = (0 : ℂ) • TL := by simp [hK, TL_K]
lemma eY_TL : eY TL = 0 := by
  funext b c; rw [eY_apply]
  fin_cases b <;> fin_cases c <;> simp [TL, outer, pR, Derivation.leibniz, Derivation.leibniz_pow]
lemma hY_TL : hY TL = (4 : ℂ) • TL := by
  funext b c; rw [hY_apply]
  fin_cases b <;> fin_cases c <;>
  simp [TL, outer, pR, Derivation.leibniz, Derivation.leibniz_pow, smul_eq_C_mul] <;> iring

/-- `w^N T` inherits the weights of `T`, shifted by `N` (`w` is a highest weight of both triples). -/
lemma seed_weights (N : ℕ) (T : Ten) (μK μY : ℂ) (h1 : eK T = 0) (h2 : hK T = μK • T)
    (h3 : eY T = 0) (h4 : hY T = μY • T) :
    eK (smulT (w ^ N) T) = 0 ∧ hK (smulT (w ^ N) T) = ((N : ℂ) + μK) • smulT (w ^ N) T ∧
    eY (smulT (w ^ N) T) = 0 ∧ hY (smulT (w ^ N) T) = ((N : ℂ) + μY) • smulT (w ^ N) T := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · rw [eK_smulT, eJ_wpow, h1]; funext b c; simp [smulT]
  · rw [hK_smulT, hJ_wpow, h2]; funext b c; simp [smulT, smul_eq_C_mul]; ring
  · rw [eY_smulT, eYw_wpow, h3]; funext b c; simp [smulT]
  · rw [hY_smulT, hYw_wpow, h4]; funext b c; simp [smulT, smul_eq_C_mul]; ring

lemma sU_weights (N : ℕ) : eK (sU N) = 0 ∧ hK (sU N) = ((N : ℂ) + 4) • sU N ∧
    eY (sU N) = 0 ∧ hY (sU N) = ((N : ℂ) + 0) • sU N :=
  seed_weights N TU 4 0 eK_TU hK_TU eY_TU hY_TU
lemma sL_weights (N : ℕ) : eK (sL N) = 0 ∧ hK (sL N) = ((N : ℂ) + 0) • sL N ∧
    eY (sL N) = 0 ∧ hY (sL N) = ((N : ℂ) + 4) • sL N :=
  seed_weights N TL 0 4 eK_TL hK_TL eY_TL hY_TL

/-- The frame Casimir separates the branches: `j = N/2` versus `j = N/2 + 2`. -/
lemma sU_SJ (N : ℕ) : SJ (sU N) = (-((N : ℂ) * (N + 2))) • sU N := by
  funext b c
  rw [sU, SJ_smulT, S_wpow]; simp [smulT, D_TU, smul_eq_C_mul]; ring
lemma sL_SJ (N : ℕ) : SJ (sL N) = (-(((N : ℂ) + 4) * (N + 6))) • sL N := by
  funext b c
  rw [sL, SJ_smulT, S_wpow, wpow_contract D N _ (-4) _ (TL_B b c), TL_S]
  simp [smulT, smul_eq_C_mul]; ring

/-! ## 7. Restriction to `S³`

`Z` is the tensor fields whose components vanish on the real unit sphere. Every frame field is tangent to `S³`
(`tangent`), so all the operators above descend to `Ten ⧸ Z`, the tensor fields restricted to `S³`. Linear
independence is proved there, i.e. for the restricted fields on `S³`. -/

/-- The unit sphere `S³ ⊂ ℝ⁴`. -/
def S3 : Set (Fin 4 → ℝ) := {x | ∑ i, x i ^ 2 = 1}
/-- Evaluation of a complex polynomial at a real point. -/
noncomputable def ev (x : Fin 4 → ℝ) : P →+* ℂ := eval fun i => (x i : ℂ)

/-- **Tangency.** A derivation that is a linear vector field `x ↦ y(x)` with `y ⊥ x`, `|y| = |x|` maps polynomials
vanishing on `S³` to polynomials vanishing on `S³` (differentiate along the great circle `cos t·x + sin t·y`). -/
theorem tangent (δ : Derivation ℂ P P) (yv : (Fin 4 → ℝ) → Fin 4 → ℝ)
    (hy : ∀ x i, ev x (δ (X i)) = (yv x i : ℂ)) (horth : ∀ x, ∑ i, x i * yv x i = 0)
    (hnorm : ∀ x, ∑ i, yv x i ^ 2 = ∑ i, x i ^ 2)
    (p : P) (hp : ∀ x ∈ S3, ev x p = 0) (x : Fin 4 → ℝ) (hx : x ∈ S3) : ev x (δ p) = 0 := by
  let c : ℝ → Fin 4 → ℝ := fun t i => Real.cos t * x i + Real.sin t * yv x i
  have hc : ∀ t, c t ∈ S3 := by
    intro t
    have h1 := horth x; have h2 := hnorm x
    simp only [S3, Set.mem_setOf_eq, c, Fin.sum_univ_four] at hx h1 h2 ⊢
    linear_combination (Real.cos t ^ 2 + Real.sin t ^ 2) * hx + 2 * Real.cos t * Real.sin t * h1
      + Real.sin t ^ 2 * h2 + Real.sin_sq_add_cos_sq t
  have hc0 : c 0 = x := by funext i; simp [c]
  have hder : ∀ q : P, HasDerivAt (fun t => ev (c t) q) (ev x (δ q)) 0 := by
    intro q
    induction q using MvPolynomial.induction_on with
    | C a => simpa [ev] using hasDerivAt_const (0 : ℝ) a
    | add p q hp hq =>
      convert hp.add hq using 1
      · funext t; simp
      · simp
    | mul_X p i hp =>
      have hi : HasDerivAt (fun t => ((c t i : ℝ) : ℂ)) (yv x i : ℂ) 0 := by
        have : HasDerivAt (fun t => Real.cos t * x i + Real.sin t * yv x i)
            (-Real.sin 0 * x i + Real.cos 0 * yv x i) 0 :=
          ((Real.hasDerivAt_cos 0).mul_const _).add ((Real.hasDerivAt_sin 0).mul_const _)
        convert this.ofReal_comp using 1; simp
      have := hp.mul hi
      convert this using 1
      · funext t; simp [ev]
      · rw [Derivation.leibniz]; simp only [smul_eq_mul, map_add, map_mul, hy]
        rw [show ev x (X i) = (x i : ℂ) by simp [ev], show (c 0 i : ℂ) = x i by rw [hc0]]
        rw [show ev (c 0) p = ev x p by rw [hc0]]; ring
  have hz : (fun t => ev (c t) p) = fun _ => 0 := funext fun t => hp _ (hc t)
  have := hder p; rw [hz] at this
  exact this.unique (hasDerivAt_const 0 0)

/-- The left frame fields as vector fields on `ℝ⁴` (real form of `dval`). -/
def dR : Fin 3 → (Fin 4 → ℝ) → Fin 4 → ℝ
  | 0 => fun x => ![-x 1, x 0, x 3, -x 2]
  | 1 => fun x => ![-x 2, -x 3, x 0, x 1]
  | 2 => fun x => ![-x 3, x 2, -x 1, x 0]
def yR : Fin 3 → (Fin 4 → ℝ) → Fin 4 → ℝ
  | 0 => fun x => ![-x 1, x 0, -x 3, x 2]
  | 1 => fun x => ![-x 2, x 3, x 0, -x 1]
  | 2 => fun x => ![-x 3, -x 2, x 1, x 0]

theorem tangent_D (a : Fin 3) (p : P) (hp : ∀ x ∈ S3, ev x p = 0) : ∀ x ∈ S3, ev x (D a p) = 0 :=
  tangent (D a) (dR a)
    (fun x i => by fin_cases a <;> fin_cases i <;> simp [ev, dval, dR])
    (fun x => by fin_cases a <;> simp [dR, Fin.sum_univ_four] <;> ring)
    (fun x => by fin_cases a <;> simp [dR, Fin.sum_univ_four] <;> ring) p hp
theorem tangent_Y (a : Fin 3) (p : P) (hp : ∀ x ∈ S3, ev x p = 0) : ∀ x ∈ S3, ev x (Y a p) = 0 :=
  tangent (Y a) (yR a)
    (fun x i => by fin_cases a <;> fin_cases i <;> simp [ev, yval, yR])
    (fun x => by fin_cases a <;> simp [yR, Fin.sum_univ_four] <;> ring)
    (fun x => by fin_cases a <;> simp [yR, Fin.sum_univ_four] <;> ring) p hp

/-- Tensor fields vanishing on `S³`. -/
noncomputable def Z : Submodule ℂ Ten where
  carrier := {h | ∀ b c, ∀ x ∈ S3, ev x (h b c) = 0}
  zero_mem' := by intro b c x _; simp
  add_mem' := by intro h k hh hk b c x hx; simp [hh b c x hx, hk b c x hx]
  smul_mem' := by
    intro r h hh b c x hx
    have := hh b c x hx; simp only [ev] at this; simp [smul_eq_C_mul, ev, this]

/-- Operators preserving `Z`. -/
def Pres (O : Module.End ℂ Ten) : Prop := ∀ h ∈ Z, O h ∈ Z

lemma Pres.add {O O' : Module.End ℂ Ten} (h1 : Pres O) (h2 : Pres O') : Pres (O + O') :=
  fun h hh => Z.add_mem (h1 h hh) (h2 h hh)
lemma Pres.sub {O O' : Module.End ℂ Ten} (h1 : Pres O) (h2 : Pres O') : Pres (O - O') :=
  fun h hh => Z.sub_mem (h1 h hh) (h2 h hh)
lemma Pres.smul {O : Module.End ℂ Ten} (r : ℂ) (h1 : Pres O) : Pres (r • O) :=
  fun h hh => Z.smul_mem r (h1 h hh)
lemma Pres.neg {O : Module.End ℂ Ten} (h1 : Pres O) : Pres (-O) :=
  fun h hh => by simpa using Z.neg_mem (h1 h hh)
lemma Pres.mul {O O' : Module.End ℂ Ten} (h1 : Pres O) (h2 : Pres O') : Pres (O * O') :=
  fun h hh => h1 _ (h2 h hh)
lemma Pres.one : Pres 1 := fun h hh => hh
lemma Pres.pow {O : Module.End ℂ Ten} (h1 : Pres O) (n : ℕ) : Pres (O ^ n) := by
  induction n with
  | zero => exact Pres.one
  | succ n ih => rw [pow_succ]; exact ih.mul h1
lemma Pres.sum {O : Fin 3 → Module.End ℂ Ten} (h : ∀ a, Pres (O a)) : Pres (∑ a, O a) := by
  simp only [Fin.sum_univ_three]; exact ((h 0).add (h 1)).add (h 2)

lemma pres_D (a : Fin 3) : Pres (DtL (D a)) := fun h hh b c x hx => tangent_D a _ (hh b c) x hx
lemma pres_Y (a : Fin 3) : Pres (DtL (Y a)) := fun h hh b c x hx => tangent_Y a _ (hh b c) x hx
lemma pres_L (a : Fin 3) : Pres (Lt a) := fun h hh b c x hx => by
  have e := fun d f => hh d f x hx
  simp only [Lt_apply, map_sub, map_neg, map_sum, map_mul, e, mul_zero, Finset.sum_const_zero,
    neg_zero, sub_zero]
lemma pres_K (a : Fin 3) : Pres (K a) := (pres_D a).add ((pres_L a).smul _)
lemma pres_Yk (a : Fin 3) : Pres (Yk a) := (pres_Y a).smul _
lemma pres_SJ : Pres SJ := Pres.sum fun a => (pres_D a).mul (pres_D a)
lemma pres_combK (α : Fin 3 → ℂ) : Pres (∑ a, α a • K a) := Pres.sum fun a => (pres_K a).smul _
lemma pres_combY (α : Fin 3 → ℂ) : Pres (∑ a, α a • Yk a) := Pres.sum fun a => (pres_Yk a).smul _

/-- Tensor fields on `S³`. -/
abbrev Q := Ten ⧸ Z

/-- Operators on `S³` tensor fields, as a Lie algebra under the commutator. -/
noncomputable instance : LieRing (Module.End ℂ Q) := LieRing.ofAssociativeRing
noncomputable instance : LieAlgebra ℂ (Module.End ℂ Q) := LieAlgebra.ofAssociativeAlgebra

open Classical in
/-- An operator descended to `S³` (zero if it does not preserve `Z`). -/
noncomputable def desc (O : Module.End ℂ Ten) : Module.End ℂ Q :=
  if h : Pres O then Z.mapQ Z O (fun x hx => h x hx) else 0

lemma desc_mk {O : Module.End ℂ Ten} (hO : Pres O) (h : Ten) :
    desc O (Submodule.Quotient.mk h) = Submodule.Quotient.mk (O h) := by
  simp [desc, hO]

lemma desc_mul {O O' : Module.End ℂ Ten} (h1 : Pres O) (h2 : Pres O') : desc (O * O') = desc O * desc O' := by
  refine LinearMap.ext fun x => ?_
  induction x using Submodule.Quotient.induction_on with
  | H h => simp [desc_mk (h1.mul h2), desc_mk h1, desc_mk h2]
lemma desc_sub {O O' : Module.End ℂ Ten} (h1 : Pres O) (h2 : Pres O') : desc (O - O') = desc O - desc O' := by
  refine LinearMap.ext fun x => ?_
  induction x using Submodule.Quotient.induction_on with
  | H h => simp [desc_mk (h1.sub h2), desc_mk h1, desc_mk h2]
lemma desc_add {O O' : Module.End ℂ Ten} (h1 : Pres O) (h2 : Pres O') : desc (O + O') = desc O + desc O' := by
  refine LinearMap.ext fun x => ?_
  induction x using Submodule.Quotient.induction_on with
  | H h => simp [desc_mk (h1.add h2), desc_mk h1, desc_mk h2]
lemma desc_smul {O : Module.End ℂ Ten} (r : ℂ) (h1 : Pres O) : desc (r • O) = r • desc O := by
  refine LinearMap.ext fun x => ?_
  induction x using Submodule.Quotient.induction_on with
  | H h => simp [desc_mk (h1.smul r), desc_mk h1]
lemma desc_neg {O : Module.End ℂ Ten} (h1 : Pres O) : desc (-O) = -desc O := by
  refine LinearMap.ext fun x => ?_
  induction x using Submodule.Quotient.induction_on with
  | H h => simp [desc_mk h1.neg, desc_mk h1]
lemma desc_pow {O : Module.End ℂ Ten} (h1 : Pres O) (n : ℕ) : desc (O ^ n) = desc O ^ n := by
  induction n with
  | zero =>
    refine LinearMap.ext fun x => ?_
    induction x using Submodule.Quotient.induction_on with
    | H h => simp [desc_mk Pres.one]
  | succ n ih => rw [pow_succ, desc_mul (h1.pow n) h1, ih, pow_succ]
lemma desc_comm {O O' : Module.End ℂ Ten} (h1 : Pres O) (h2 : Pres O') (hc : Commute O O') :
    Commute (desc O) (desc O') := by
  unfold Commute SemiconjBy; rw [← desc_mul h1 h2, ← desc_mul h2 h1, hc.eq]

/-- A class is nonzero if one component is nonzero at one point of `S³`. -/
lemma mk_ne_zero (h : Ten) (b c : Fin 3) (x : Fin 4 → ℝ) (hx : x ∈ S3) (hne : ev x (h b c) ≠ 0) :
    (Submodule.Quotient.mk h : Q) ≠ 0 := by
  rw [Ne, Submodule.Quotient.mk_eq_zero]; intro hz; exact hne (hz b c x hx)

def pt : Fin 4 → ℝ := ![1, 0, 0, 0]
lemma pt_S3 : pt ∈ S3 := by simp [S3, pt, Fin.sum_univ_four]
@[simp] lemma ev_w : ev pt w = 1 := by simp [ev, w, pt, ii, -C_I]
@[simp] lemma ev_u : ev pt u = 0 := by simp [ev, u, pt, ii, -C_I]
@[simp] lemma ev_ii : ev pt ii = Complex.I := by simp [ev, ii, -C_I]

lemma sU_ne (N : ℕ) : (Submodule.Quotient.mk (sU N) : Q) ≠ 0 :=
  mk_ne_zero _ 0 0 pt pt_S3 (by simp [sU, smulT, TU, outer, vC])
lemma sL_ne (N : ℕ) : (Submodule.Quotient.mk (sL N) : Q) ≠ 0 :=
  mk_ne_zero _ 0 0 pt pt_S3 (by simp [sL, smulT, TL, outer, pR])

/-! ## 8. The two multiplets on `S³` and their independence -/

lemma pres_hK : Pres hK := by rw [combs.1]; exact pres_combK _
lemma pres_eK : Pres eK := by rw [combs.2.1]; exact pres_combK _
lemma pres_fK : Pres fK := by rw [combs.2.2.1]; exact pres_combK _
lemma pres_hY : Pres hY := by rw [combs.2.2.2.1]; exact pres_combY _
lemma pres_eY : Pres eY := by rw [combs.2.2.2.2.1]; exact pres_combY _
lemma pres_fY : Pres fY := by rw [combs.2.2.2.2.2]; exact pres_combY _

/-- An `sl₂` triple on `Ten` that preserves `Z` descends to an `sl₂` triple on `S³`. -/
lemma desc_triple {h e f : Module.End ℂ Ten} (ph : Pres h) (pe : Pres e) (pf : Pres f)
    (r1 : ⁅h, e⁆ = 2 • e) (r2 : ⁅h, f⁆ = -(2 • f)) (r3 : ⁅e, f⁆ = h) (hne : desc h ≠ 0) :
    IsSl2Triple (desc h) (desc e) (desc f) where
  h_ne_zero := hne
  lie_e_f := by rw [Ring.lie_def, ← desc_mul pe pf, ← desc_mul pf pe, ← desc_sub (pe.mul pf) (pf.mul pe),
    ← Ring.lie_def, r3]
  lie_h_e_nsmul := by
    rw [Ring.lie_def, ← desc_mul ph pe, ← desc_mul pe ph, ← desc_sub (ph.mul pe) (pe.mul ph),
      ← Ring.lie_def, r1, two_nsmul, two_nsmul, desc_add pe pe]
  lie_h_f_nsmul := by
    rw [Ring.lie_def, ← desc_mul ph pf, ← desc_mul pf ph, ← desc_sub (ph.mul pf) (pf.mul ph),
      ← Ring.lie_def, r2, two_nsmul, two_nsmul, desc_neg (pf.add pf), desc_add pf pf]

lemma desc_ne_of_eigen {O : Module.End ℂ Ten} (hO : Pres O) (s : Ten) (μ : ℂ) (hμ : μ ≠ 0)
    (hs : O s = μ • s) (hne : (Submodule.Quotient.mk s : Q) ≠ 0) : desc O ≠ 0 := by
  intro h0
  have := desc_mk hO s; rw [h0, hs, LinearMap.zero_apply, Submodule.Quotient.mk_smul] at this
  exact hne ((smul_eq_zero.mp this.symm).resolve_left hμ)

/-- **The `K` triple on `S³`** (`SU(2)` generated by the left-invariant Killing fields). -/
lemma tK : IsSl2Triple (desc hK) (desc eK) (desc fK) := by
  obtain ⟨r1, r2, r3⟩ := sl2_rel K K_bracket
  refine desc_triple pres_hK pres_eK pres_fK r1 r2 r3 ?_
  refine desc_ne_of_eigen pres_hK (sU 0) 4 (by norm_num) ?_ (sU_ne 0)
  simpa using (sU_weights 0).2.1
/-- **The `Y` triple on `S³`** (`SU(2)` generated by the right-invariant fields). -/
lemma tY : IsSl2Triple (desc hY) (desc eY) (desc fY) := by
  obtain ⟨r1, r2, r3⟩ := relY
  refine desc_triple pres_hY pres_eY pres_fY r1 r2 r3 ?_
  refine desc_ne_of_eigen pres_hY (sL 0) 4 (by norm_num) ?_ (sL_ne 0)
  simpa using (sL_weights 0).2.2.2

lemma toEnd_self (F : Module.End ℂ Q) : LieModule.toEnd ℂ (Module.End ℂ Q) Q F = F := by
  ext x; simp

/-- A highest-weight seed. -/
structure Seed (s : Ten) (nK nY : ℕ) (σ : ℂ) : Prop where
  ne : (Submodule.Quotient.mk s : Q) ≠ 0
  eK0 : eK s = 0
  hKs : hK s = (nK : ℂ) • s
  eY0 : eY s = 0
  hYs : hY s = (nY : ℂ) • s
  SJs : SJ s = σ • s

lemma sU_seed (N : ℕ) : Seed (sU N) (N + 4) N (-((N : ℂ) * (N + 2))) := by
  obtain ⟨a, b, c, d⟩ := sU_weights N
  exact ⟨sU_ne N, a, by rw [b]; push_cast; rfl, c, by rw [d]; simp, sU_SJ N⟩
lemma sL_seed (N : ℕ) : Seed (sL N) N (N + 4) (-(((N : ℂ) + 4) * (N + 6))) := by
  obtain ⟨a, b, c, d⟩ := sL_weights N
  exact ⟨sL_ne N, a, by rw [b]; simp, c, by rw [d]; push_cast; rfl, sL_SJ N⟩

/-- The multiplet member `f_Y^q f_K^p s`, on `ℝ⁴` and on `S³`. -/
noncomputable def mem (s : Ten) (p q : ℕ) : Ten := (fY ^ q) ((fK ^ p) s)

lemma mem_mk (s : Ten) (p q : ℕ) :
    (Submodule.Quotient.mk (mem s p q) : Q) = (desc fY ^ q) ((desc fK ^ p) (Submodule.Quotient.mk s)) := by
  rw [mem, ← desc_pow pres_fY, ← desc_pow pres_fK, desc_mk (pres_fK.pow p), desc_mk (pres_fY.pow q)]

set_option maxHeartbeats 1000000 in
/-- **The weights of a multiplet member, and that it is nonzero on `S³`.** -/
theorem mem_spec {s : Ten} {nK nY : ℕ} {σ : ℂ} (S : Seed s nK nY σ) {p q : ℕ} (hp : p ≤ nK) (hq : q ≤ nY) :
    let v : Q := Submodule.Quotient.mk (mem s p q)
    v ≠ 0 ∧ desc hK v = ((nK : ℂ) - 2 * p) • v ∧ desc hY v = ((nY : ℂ) - 2 * q) • v ∧ desc SJ v = σ • v := by
  intro v
  let m : Q := Submodule.Quotient.mk s
  have PK : tK.HasPrimitiveVectorWith m (nK : ℂ) :=
    ⟨S.ne, by simp [m, desc_mk pres_hK, S.hKs, Submodule.Quotient.mk_smul],
      by simp [m, desc_mk pres_eK, S.eK0]⟩
  let x : Q := (desc fK ^ p) m
  have hx : x = (LieModule.toEnd ℂ (Module.End ℂ Q) Q (desc fK) ^ p) m := by rw [toEnd_self]
  have xne : x ≠ 0 := by rw [hx]; exact PK.pow_toEnd_f_ne_zero_of_eq_nat rfl hp
  have xK : desc hK x = ((nK : ℂ) - 2 * p) • x := by
    have := PK.lie_h_pow_toEnd_f p; rw [toEnd_self] at this; simpa [x] using this
  have cKY : ∀ {A B : Module.End ℂ Ten}, (∃ α : Fin 3 → ℂ, A = ∑ a, α a • K a) →
      (∃ β : Fin 3 → ℂ, B = ∑ b, β b • Yk b) → Pres A → Pres B →
      Commute (desc A) (desc B) := fun hA hB pA pB => desc_comm pA pB (comm_KY hA hB)
  have ehK : ∃ α : Fin 3 → ℂ, hK = ∑ a, α a • K a := ⟨_, combs.1⟩
  have efK : ∃ α : Fin 3 → ℂ, fK = ∑ a, α a • K a := ⟨_, combs.2.2.1⟩
  have ehY : ∃ α : Fin 3 → ℂ, hY = ∑ a, α a • Yk a := ⟨_, combs.2.2.2.1⟩
  have eeY : ∃ α : Fin 3 → ℂ, eY = ∑ a, α a • Yk a := ⟨_, combs.2.2.2.2.1⟩
  have efY : ∃ α : Fin 3 → ℂ, fY = ∑ a, α a • Yk a := ⟨_, combs.2.2.2.2.2⟩
  have PY : tY.HasPrimitiveVectorWith x (nY : ℂ) := by
    refine ⟨xne, ?_, ?_⟩
    · rw [Module.End.lie_apply]
      show desc hY ((desc fK ^ p) m) = (nY : ℂ) • ((desc fK ^ p) m)
      rw [← Module.End.mul_apply, ← ((cKY efK ehY pres_fK pres_hY).pow_left p).eq, Module.End.mul_apply]
      simp [m, desc_mk pres_hY, S.hYs, Submodule.Quotient.mk_smul]
    · rw [Module.End.lie_apply]
      show desc eY ((desc fK ^ p) m) = 0
      rw [← Module.End.mul_apply, ← ((cKY efK eeY pres_fK pres_eY).pow_left p).eq, Module.End.mul_apply]
      simp [m, desc_mk pres_eY, S.eY0]
  have hv : v = (LieModule.toEnd ℂ (Module.End ℂ Q) Q (desc fY) ^ q) x := by
    show (Submodule.Quotient.mk (mem s p q) : Q) = _; rw [toEnd_self, mem_mk]
  refine ⟨by rw [hv]; exact PY.pow_toEnd_f_ne_zero_of_eq_nat rfl hq, ?_, ?_, ?_⟩
  · rw [show v = (desc fY ^ q) x from mem_mk s p q]
    rw [← Module.End.mul_apply, ((cKY ehK efY pres_hK pres_fY).pow_right q).eq, Module.End.mul_apply, xK,
      map_smul]
  · have := PY.lie_h_pow_toEnd_f q; rw [toEnd_self] at this; rw [hv, toEnd_self]; simpa using this
  · have c1 : Commute (desc SJ) (desc fK) := desc_comm pres_SJ pres_fK (comm_SJ_K efK)
    have c2 : Commute (desc SJ) (desc fY) := desc_comm pres_SJ pres_fY (comm_SJ_Y efY)
    rw [show v = (desc fY ^ q) ((desc fK ^ p) m) from mem_mk s p q]
    rw [← Module.End.mul_apply, (c2.pow_right q).eq, Module.End.mul_apply,
      ← Module.End.mul_apply (desc SJ), (c1.pow_right p).eq, Module.End.mul_apply]
    simp [m, desc_mk pres_SJ, S.SJs, Submodule.Quotient.mk_smul]

lemma mem_TT {s : Ten} {lam : ℂ} (hs : s ∈ TT lam) (p q : ℕ) : mem s p q ∈ TT lam := by
  have sK : Stab fK := by
    rw [combs.2.2.1]; intro l h hh
    rw [LinearMap.sum_apply]; exact Submodule.sum_mem _ fun a _ => (TT l).smul_mem _ (K_TT a hh)
  have sY : Stab fY := by
    rw [combs.2.2.2.2.2]; intro l h hh
    rw [LinearMap.sum_apply]; exact Submodule.sum_mem _ fun a _ => (TT l).smul_mem _ (Yk_TT a hh)
  exact sY.pow q _ _ (sK.pow p _ _ hs)

/-- The index set at level `m = N + 3`: the upper multiplet `(N+5) × (N+1)`, the lower one `(N+1) × (N+5)`. -/
abbrev Idx (N : ℕ) := (Fin (N + 5) × Fin (N + 1)) ⊕ (Fin (N + 1) × Fin (N + 5))

/-- The family at level `m = N + 3`. -/
noncomputable def fam (N : ℕ) : Idx N → Ten
  | .inl (p, q) => mem (sU N) p q
  | .inr (p, q) => mem (sL N) p q

lemma card_Idx (N : ℕ) : Fintype.card (Idx N) = 2 * ((N + 3) ^ 2 - 4) := by
  simp only [Fintype.card_sum, Fintype.card_prod, Fintype.card_fin]
  rw [show (N + 3) ^ 2 = (N + 5) * (N + 1) + 4 by ring, Nat.add_sub_cancel]; ring

open Complex in
/-- **Multiplicity at every level.** At level `m = N + 3`, the `2(m² − 4)` fields `fam N` are TT eigen-tensors
with `−∇²h = (m² − 3) h`, and their restrictions to `S³` are linearly independent over `ℂ`. -/
theorem tt_level_multiplicity_N (N : ℕ) :
    (∀ i, fam N i ∈ TT (((N : ℂ) + 3) ^ 2 - 3)) ∧
    LinearIndependent ℂ (fun i => (Submodule.Quotient.mk (fam N i) : Q)) ∧
    Fintype.card (Idx N) = 2 * ((N + 3) ^ 2 - 4) := by
  refine ⟨?_, ?_, card_Idx N⟩
  · rintro (⟨p, q⟩ | ⟨p, q⟩)
    · exact mem_TT (sU_TT N) p q
    · exact mem_TT (sL_TT N) p q
  let c : ℂ := 1 / (16 * ((N : ℂ) + 3))
  let Θ : Module.End ℂ Q := desc hK + I • desc hY + c • (desc SJ + ((N : ℂ) * (N + 2)) • 1)
  let μ : Idx N → ℂ
    | .inl (p, q) => ((N : ℂ) + 4 - 2 * (p : ℕ)) + I * ((N : ℂ) - 2 * (q : ℕ))
    | .inr (p, q) => ((N : ℂ) - 2 * (p : ℕ)) + I * ((N : ℂ) + 4 - 2 * (q : ℕ)) - 1 / 2
  have hN3 : (N : ℂ) + 3 ≠ 0 := by
    have : (0 : ℝ) < N + 3 := by positivity
    exact_mod_cast this.ne'
  have hN : (16 * ((N : ℂ) + 3)) ≠ 0 := by
    have : (0 : ℝ) < 16 * (N + 3) := by positivity
    exact_mod_cast this.ne'
  refine Module.End.eigenvectors_linearIndependent' Θ μ ?_ _ ?_
  · rintro (⟨p, q⟩ | ⟨p, q⟩) (⟨p', q'⟩ | ⟨p', q'⟩) h <;>
      simp [μ, Complex.ext_iff] at h <;> obtain ⟨h1, h2⟩ := h
    · have e1 : p = p' := Fin.ext (by exact_mod_cast h1)
      have e2 : q = q' := Fin.ext (by exact_mod_cast h2)
      rw [e1, e2]
    · exfalso
      have : ((4 * (p : ℕ) : ℕ) : ℝ) = ((4 * (p' : ℕ) + 9 : ℕ) : ℝ) := by push_cast; linarith
      have := Nat.cast_injective this; omega
    · exfalso
      have : ((4 * (p' : ℕ) : ℕ) : ℝ) = ((4 * (p : ℕ) + 9 : ℕ) : ℝ) := by push_cast; linarith
      have := Nat.cast_injective this; omega
    · have e1 : p = p' := Fin.ext (by exact_mod_cast h1)
      have e2 : q = q' := Fin.ext (by exact_mod_cast h2)
      rw [e1, e2]
  · have key : ∀ {s nK nY σ} (S : Seed s nK nY σ) (p q : ℕ) (hp : p ≤ nK) (hq : q ≤ nY),
        Θ (Submodule.Quotient.mk (mem s p q)) =
          (((nK : ℂ) - 2 * p) + I * ((nY : ℂ) - 2 * q) + c * (σ + N * (N + 2))) •
            (Submodule.Quotient.mk (mem s p q) : Q) := by
      intro s nK nY σ S p q hp hq
      obtain ⟨_, h1, h2, h3⟩ := mem_spec S hp hq
      simp only [Θ, LinearMap.add_apply, LinearMap.smul_apply, h1, h2, h3, Module.End.one_apply]
      simp only [smul_smul, ← add_smul]
    rintro (⟨p, q⟩ | ⟨p, q⟩)
    · refine ⟨?_, (mem_spec (sU_seed N) (by omega) (by omega)).1⟩
      rw [Module.End.mem_eigenspace_iff]
      simp only [fam]
      rw [key (sU_seed N) p q (by omega) (by omega)]; congr 1; simp only [μ, c]; push_cast; field_simp; ring
    · refine ⟨?_, (mem_spec (sL_seed N) (by omega) (by omega)).1⟩
      rw [Module.End.mem_eigenspace_iff]
      simp only [fam]
      rw [key (sL_seed N) p q (by omega) (by omega)]; congr 1; simp only [μ, c]; push_cast; field_simp; ring

/-- **The lower half of the TT spectrum of `S³`, at every level.** For every `m ≥ 3` there are `2(m² − 4)`
transverse-traceless symmetric tensor fields with `−∇²h = (m² − 3) h` whose restrictions to `S³` are linearly
independent: the TT eigenspace at level `m` has (complex) dimension `≥ 2(m² − 4)`. -/
theorem tt_level_multiplicity (m : ℕ) (hm : 3 ≤ m) :
    ∃ (ι : Type) (_ : Fintype ι) (v : ι → Ten), Fintype.card ι = 2 * (m ^ 2 - 4) ∧
      (∀ i, v i ∈ TT ((m : ℂ) ^ 2 - 3)) ∧ LinearIndependent ℂ (fun i => (Submodule.Quotient.mk (v i) : Q)) := by
  obtain ⟨N, rfl⟩ : ∃ N, m = N + 3 := ⟨m - 3, by omega⟩
  obtain ⟨h1, h2, h3⟩ := tt_level_multiplicity_N N
  exact ⟨Idx N, inferInstance, fam N, h3, by simpa using h1, h2⟩

/-- The corpus's first three degeneracies, `10, 24, 42`, reached. -/
theorem tt_m345 : Fintype.card (Idx 0) = 10 ∧ Fintype.card (Idx 1) = 24 ∧ Fintype.card (Idx 2) = 42 := by
  simp

end ShadowProbe.S3TTSpectrum

#print axioms ShadowProbe.S3TTSpectrum.frame_bracket
#print axioms ShadowProbe.S3TTSpectrum.lap_K
#print axioms ShadowProbe.S3TTSpectrum.K_TT
#print axioms ShadowProbe.S3TTSpectrum.TU_lap
#print axioms ShadowProbe.S3TTSpectrum.TL_lap
#print axioms ShadowProbe.S3TTSpectrum.seed_TT
#print axioms ShadowProbe.S3TTSpectrum.sU_TT
#print axioms ShadowProbe.S3TTSpectrum.sL_TT
#print axioms ShadowProbe.S3TTSpectrum.tangent
#print axioms ShadowProbe.S3TTSpectrum.mem_spec
#print axioms ShadowProbe.S3TTSpectrum.tt_level_multiplicity_N
#print axioms ShadowProbe.S3TTSpectrum.tt_level_multiplicity
#print axioms ShadowProbe.S3TTSpectrum.tt_m345

import Mathlib.Algebra.MvPolynomial.Derivation
import Mathlib.RingTheory.Derivation.Lie
import Mathlib.Algebra.Lie.Sl2
import Mathlib.Algebra.Lie.OfAssociative
import Mathlib.LinearAlgebra.Eigenspace.Basic
import Mathlib.Analysis.Complex.RealDeriv
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Deriv
import Mathlib.Algebra.MvPolynomial.CommRing
import Mathlib.LinearAlgebra.Complex.FiniteDimensional

/-! # Campaign 53 (programme stage P2): the polynomial spectrum of `∇²` on symmetric traceless tensor fields on `S³`

Sections 1–8 are campaign 51's `probes/S3TTSpectrum.lean`, copied wholesale (the frame `D a` on `ℂ[x₀..x₃]`,
`nab`, `lap`, the TT eigenspaces, the restriction `Q = Ten ⧸ Z` to `S³`, the two `sl₂` triples, the seeds,
`mem_spec`, and the lower bound `tt_level_multiplicity`). Its original header follows.

Sections 9–15 are new (campaign 53). `Pd = Sd d`: the symmetric traceless tensor fields with polynomial
components of degree `≤ d`, on `S³`.
* **Item 1.** `Sd_fd`, `Sd_finrank_le`, `Sd_finrank` (`dim Pd = 5 Σ_{N≤d} (N+1)²`), `Sd_invariant`
  (`∇²`, both `sl₂` triples preserve `Pd`; the divergence does not raise degree).
* **Item 2.** `lap_casimir` (`∇² = ½(S_J + C_K) − Σ L_a²`, exact), `SJ_eq_CY` (frame Casimir = right-invariant
  Casimir), `neg_lap_casimir` (`−∇² = −6 − ½(C_Y + C_K)` on symmetric traceless fields), `lap_spectrum`
  (an eigenbasis of `Pd`, eigenvalues `λ(N,t) = ½(N(N+2) + μ(μ+2)) − 6`, `μ = N + 4 − 2t`).
* **Item 3.** `degree_bound`: an eigenvector at `λ` lies in `P_{D(λ)}`, `D(λ) = ⌈|λ|⌉ + 6`, uniformly.
* **Item 4.** `tt_spectrum` (TT eigenvalues are `m² − 3`, `m ≥ 3`), `tt_count` (for `d ≥ m + 1` the TT
  eigenspace at `m² − 3` is the span of campaign 51's eigen-tensors and has complex dimension exactly
  `2(m² − 4)`, uniformly in `m`), `tt_count_real` (real dimension `2(m² − 4)` for real-coefficient fields).

Route: an explicit eigenbasis of `Pd` (highest-weight seeds `w^(N−t) T_t` and their `sl₂ × sl₂` multiplets),
independent by distinct joint eigenvalues, whose number matches a spanning family of reduced monomials
(`x₀² = 1 − x₁² − x₂² − x₃²` on `S³`). The TT part is cut out by `O = Ł ∘ div` (`Ł` the conformal Killing
operator), which acts on the seed `(N, t)` by a scalar nonzero exactly for the non-TT seeds `t = 1, 2, 3`. -/


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

namespace ShadowProbe.S3PolySpectrum

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


/-! ## 9. Degree

`DL n p`: the total degree of `p` is at most `n`. It is a structure (not a bare `≤`) so the structural degree
tactic `deg` below cannot unify it with the arithmetic side goals. -/

structure DL (n : ℕ) (p : P) : Prop where
  le : p.totalDegree ≤ n

lemma DL.mono {i j : ℕ} {p : P} (hp : DL i p) (h : i ≤ j) : DL j p := ⟨hp.le.trans h⟩
lemma DL.add {n : ℕ} {p q : P} (hp : DL n p) (hq : DL n q) : DL n (p + q) :=
  ⟨(totalDegree_add p q).trans (max_le hp.le hq.le)⟩
lemma DL.add' {i j : ℕ} {p q : P} (hp : DL i p) (hq : DL j q) : DL (max i j) (p + q) :=
  (hp.mono (le_max_left i j)).add (hq.mono (le_max_right i j))
lemma DL.neg {n : ℕ} {p : P} (hp : DL n p) : DL n (-p) := ⟨by rw [totalDegree_neg]; exact hp.le⟩
lemma DL.sub {n : ℕ} {p q : P} (hp : DL n p) (hq : DL n q) : DL n (p - q) := by
  rw [sub_eq_add_neg]; exact hp.add hq.neg
lemma DL.sub' {i j : ℕ} {p q : P} (hp : DL i p) (hq : DL j q) : DL (max i j) (p - q) :=
  (hp.mono (le_max_left i j)).sub (hq.mono (le_max_right i j))
lemma DL.mul {i j : ℕ} {p q : P} (hp : DL i p) (hq : DL j q) : DL (i + j) (p * q) :=
  ⟨(totalDegree_mul p q).trans (add_le_add hp.le hq.le)⟩
lemma DL.pow {i : ℕ} {p : P} (hp : DL i p) (k : ℕ) : DL (k * i) (p ^ k) :=
  ⟨(totalDegree_pow p k).trans (Nat.mul_le_mul_left k hp.le)⟩
lemma DL.const (c : ℂ) : DL 0 (C c : P) := ⟨by rw [totalDegree_C]⟩
lemma DL.zero : DL 0 (0 : P) := ⟨by rw [totalDegree_zero]⟩
lemma DL.zero' (n : ℕ) : DL n (0 : P) := DL.zero.mono (Nat.zero_le n)
lemma DL.one : DL 0 (1 : P) := ⟨by rw [totalDegree_one]⟩
lemma DL.ofNat (k : ℕ) [k.AtLeastTwo] : DL 0 (OfNat.ofNat k : P) := by
  rw [← map_ofNat C]; exact DL.const _
lemma DL.var (i : Fin 4) : DL 1 (X i : P) := ⟨by rw [totalDegree_X]⟩
lemma DL.iI : DL 0 ii := DL.const _
lemma DL.smul {n : ℕ} (c : ℂ) {p : P} (hp : DL n p) : DL n (c • p) := ⟨(totalDegree_smul_le c p).trans hp.le⟩
lemma DL.Cmul {n : ℕ} (c : ℂ) {p : P} (hp : DL n p) : DL n (C c * p) := by
  rw [← smul_eq_C_mul]; exact hp.smul c
lemma DL.sum {n : ℕ} {ι : Type*} (s : Finset ι) (f : ι → P) (h : ∀ a, DL n (f a)) : DL n (∑ a ∈ s, f a) :=
  ⟨totalDegree_finsetSum_le fun a _ => (h a).le⟩

/-- Structural degree bound for explicit polynomials. -/
macro "deg" : tactic => `(tactic| (
  apply DL.mono
  repeat' first
    | exact DL.var _
    | exact DL.iI
    | exact DL.one
    | exact DL.zero
    | exact DL.ofNat _
    | exact DL.const _
    | apply DL.add'
    | apply DL.sub'
    | apply DL.neg
    | apply DL.mul
    | apply DL.pow
  all_goals omega))

lemma DL_w : DL 1 w := by unfold w ii; deg
lemma DL_u : DL 1 u := by unfold u ii; deg

/-! ### Polynomials of bounded degree, monomial by monomial -/

/-- The monomial `x₀^a x₁^b x₂^c x₃^e`. -/
noncomputable def mono (a b c e : ℕ) : P := X 0 ^ a * X 1 ^ b * X 2 ^ c * X 3 ^ e

/-- **Induction on the monomials of a polynomial of degree `≤ n`.** -/
lemma deg_induction {n : ℕ} (M : P → Prop) (h0 : M 0) (hadd : ∀ p q, M p → M q → M (p + q))
    (hsmul : ∀ (c : ℂ) p, M p → M (c • p)) (hmono : ∀ a b c e, a + b + c + e ≤ n → M (mono a b c e))
    (p : P) (hp : DL n p) : M p := by
  rw [as_sum p]
  refine Finset.sum_induction _ M hadd h0 fun s hs => ?_
  have hd := (le_totalDegree hs).trans hp.le
  rw [Finsupp.sum_fintype _ _ (fun _ => rfl), Fin.sum_univ_four] at hd
  have : monomial s (p.coeff s) = p.coeff s • mono (s 0) (s 1) (s 2) (s 3) := by
    rw [monomial_eq, Finsupp.prod_fintype _ _ (fun _ => pow_zero _), Fin.prod_univ_four, smul_eq_C_mul, mono]
  rw [this]; exact hsmul _ _ (hmono _ _ _ _ hd)

/-- A derivation sending each `X i` to a polynomial of degree `≤ 1` does not raise degree. -/
lemma deriv_DL (δ : Derivation ℂ P P) (hδ : ∀ i, DL 1 (δ (X i))) {n : ℕ} {p : P} (hp : DL n p) :
    DL n (δ p) := by
  -- `G k f`: `f` and `δ f` both have degree `≤ k`
  have Gmul : ∀ {i j f g}, DL i f ∧ DL i (δ f) → DL j g ∧ DL j (δ g) →
      DL (i + j) (f * g) ∧ DL (i + j) (δ (f * g)) := by
    intro i j f g ⟨hf, hf'⟩ ⟨hg, hg'⟩
    refine ⟨hf.mul hg, ?_⟩
    rw [Derivation.leibniz, smul_eq_mul, smul_eq_mul]
    exact (hf.mul hg').add ((hg.mul hf').mono (by omega))
  have Gpow : ∀ (i : Fin 4) (k : ℕ), DL k (X i ^ k) ∧ DL k (δ (X i ^ k)) := by
    intro i k
    induction k with
    | zero => exact ⟨by simpa using DL.one, by simpa using DL.zero⟩
    | succ k ih => rw [pow_succ]; exact Gmul ih ⟨DL.var i, hδ i⟩
  refine deg_induction (fun q => DL n (δ q)) (by simpa using DL.zero' n)
    (fun p q hp hq => by rw [map_add]; exact hp.add hq) (fun c p hp => by rw [Derivation.map_smul]; exact hp.smul c)
    (fun a b c e h => ?_) p hp
  have := Gmul (Gmul (Gmul (Gpow 0 a) (Gpow 1 b)) (Gpow 2 c)) (Gpow 3 e)
  exact this.2.mono h

lemma D_DL (a : Fin 3) {n : ℕ} {p : P} (hp : DL n p) : DL n (D a p) :=
  deriv_DL (D a) (fun i => by rw [D_X]; fin_cases a <;> fin_cases i <;> simp [dval] <;> deg) hp
lemma Y_DL (a : Fin 3) {n : ℕ} {p : P} (hp : DL n p) : DL n (Y a p) :=
  deriv_DL (Y a) (fun i => by rw [Y_X]; fin_cases a <;> fin_cases i <;> simp [yval] <;> deg) hp

/-! ### Degree of tensor and vector fields, and the operators that preserve it -/

/-- All components of `h` have degree `≤ n`. -/
def DegLe (n : ℕ) (h : Ten) : Prop := ∀ b c, DL n (h b c)
/-- All components of `v` have degree `≤ n`. -/
def DegLeV (n : ℕ) (v : Vec) : Prop := ∀ c, DL n (v c)

/-- Operators not raising degree. -/
def DegPres (O : Module.End ℂ Ten) : Prop := ∀ n h, DegLe n h → DegLe n (O h)

lemma DegPres.add {O O' : Module.End ℂ Ten} (h1 : DegPres O) (h2 : DegPres O') : DegPres (O + O') :=
  fun n h hh b c => (h1 n h hh b c).add (h2 n h hh b c)
lemma DegPres.sub {O O' : Module.End ℂ Ten} (h1 : DegPres O) (h2 : DegPres O') : DegPres (O - O') :=
  fun n h hh b c => (h1 n h hh b c).sub (h2 n h hh b c)
lemma DegPres.smul {O : Module.End ℂ Ten} (r : ℂ) (h1 : DegPres O) : DegPres (r • O) :=
  fun n h hh b c => (h1 n h hh b c).smul r
lemma DegPres.neg {O : Module.End ℂ Ten} (h1 : DegPres O) : DegPres (-O) :=
  fun n h hh b c => (h1 n h hh b c).neg
lemma DegPres.mul {O O' : Module.End ℂ Ten} (h1 : DegPres O) (h2 : DegPres O') : DegPres (O * O') :=
  fun n h hh => h1 n _ (h2 n h hh)
lemma DegPres.one : DegPres 1 := fun _ _ hh => hh
lemma DegPres.pow {O : Module.End ℂ Ten} (h1 : DegPres O) (k : ℕ) : DegPres (O ^ k) := by
  induction k with
  | zero => exact DegPres.one
  | succ k ih => rw [pow_succ]; exact ih.mul h1
lemma DegPres.sum {O : Fin 3 → Module.End ℂ Ten} (h : ∀ a, DegPres (O a)) : DegPres (∑ a, O a) := by
  simp only [Fin.sum_univ_three]; exact ((h 0).add (h 1)).add (h 2)

lemma degP_D (a : Fin 3) : DegPres (DtL (D a)) := fun _ _ hh b c => D_DL a (hh b c)
lemma degP_Y (a : Fin 3) : DegPres (DtL (Y a)) := fun _ _ hh b c => Y_DL a (hh b c)
lemma degP_L (a : Fin 3) : DegPres (Lt a) := fun n h hh b c => by
  rw [Lt_apply]
  exact (DL.sum _ _ fun d => (hh d c).Cmul _).neg.sub (DL.sum _ _ fun d => (hh b d).Cmul _)
lemma degP_K (a : Fin 3) : DegPres (K a) := (degP_D a).add ((degP_L a).smul _)
lemma degP_Yk (a : Fin 3) : DegPres (Yk a) := (degP_Y a).smul _
lemma degP_nab (a : Fin 3) : DegPres (nab a) := (degP_D a).add (degP_L a)
lemma degP_lap : DegPres lap := DegPres.sum fun a => (degP_nab a).mul (degP_nab a)
lemma degP_SJ : DegPres SJ := DegPres.sum fun a => (degP_D a).mul (degP_D a)
lemma degP_combK (α : Fin 3 → ℂ) : DegPres (∑ a, α a • K a) := DegPres.sum fun a => (degP_K a).smul _
lemma degP_combY (α : Fin 3 → ℂ) : DegPres (∑ a, α a • Yk a) := DegPres.sum fun a => (degP_Yk a).smul _
lemma degP_hK : DegPres hK := by rw [combs.1]; exact degP_combK _
lemma degP_eK : DegPres eK := by rw [combs.2.1]; exact degP_combK _
lemma degP_fK : DegPres fK := by rw [combs.2.2.1]; exact degP_combK _
lemma degP_hY : DegPres hY := by rw [combs.2.2.2.1]; exact degP_combY _
lemma degP_eY : DegPres eY := by rw [combs.2.2.2.2.1]; exact degP_combY _
lemma degP_fY : DegPres fY := by rw [combs.2.2.2.2.2]; exact degP_combY _

/-- The divergence does not raise degree. -/
lemma dv_DegLe {n : ℕ} {h : Ten} (hh : DegLe n h) : DegLeV n (dvL h) := fun c => by
  rw [dvL_apply]; exact DL.sum _ _ fun b => degP_nab b n h hh b c

/-! ### Symmetric traceless tensors, and the operators preserving them -/

/-- Symmetric traceless tensor fields with components of degree `≤ d` (on `ℝ⁴`). -/
noncomputable def SymTL (d : ℕ) : Submodule ℂ Ten where
  carrier := {h | IsSym h ∧ trL h = 0 ∧ DegLe d h}
  zero_mem' := ⟨fun _ _ => rfl, map_zero _, fun _ _ => DL.zero' d⟩
  add_mem' := by
    rintro h k ⟨hs, ht, hd⟩ ⟨ks, kt, kd⟩
    exact ⟨fun b c => by simp [hs b c, ks b c], by rw [map_add, ht, kt, add_zero],
      fun b c => (hd b c).add (kd b c)⟩
  smul_mem' := by
    rintro r h ⟨hs, ht, hd⟩
    exact ⟨fun b c => by simp [hs b c], by rw [map_smul, ht, smul_zero], fun b c => (hd b c).smul r⟩

/-- **`Pd`**: the symmetric traceless tensor fields with polynomial components of degree `≤ d`, on `S³`. -/
noncomputable def Sd (d : ℕ) : Submodule ℂ Q := (SymTL d).map Z.mkQ

lemma Sd_mono {d e : ℕ} (h : d ≤ e) : Sd d ≤ Sd e := by
  apply Submodule.map_mono
  rintro x ⟨hs, ht, hd⟩; exact ⟨hs, ht, fun b c => (hd b c).mono h⟩

/-- Operators preserving symmetry and tracelessness. -/
def STPres (O : Module.End ℂ Ten) : Prop := ∀ h, IsSym h → trL h = 0 → IsSym (O h) ∧ trL (O h) = 0

lemma STPres.add {O O' : Module.End ℂ Ten} (h1 : STPres O) (h2 : STPres O') : STPres (O + O') :=
  fun h hs ht => ⟨fun b c => by simp [(h1 h hs ht).1 b c, (h2 h hs ht).1 b c],
    by show trL (O h + O' h) = 0; rw [map_add, (h1 h hs ht).2, (h2 h hs ht).2, add_zero]⟩
lemma STPres.smul {O : Module.End ℂ Ten} (r : ℂ) (h1 : STPres O) : STPres (r • O) :=
  fun h hs ht => ⟨fun b c => by simp [(h1 h hs ht).1 b c],
    by show trL (r • O h) = 0; rw [map_smul, (h1 h hs ht).2, smul_zero]⟩
lemma STPres.mul {O O' : Module.End ℂ Ten} (h1 : STPres O) (h2 : STPres O') : STPres (O * O') :=
  fun h hs ht => h1 _ (h2 h hs ht).1 (h2 h hs ht).2
lemma STPres.sum {O : Fin 3 → Module.End ℂ Ten} (h : ∀ a, STPres (O a)) : STPres (∑ a, O a) := by
  simp only [Fin.sum_univ_three]; exact ((h 0).add (h 1)).add (h 2)

lemma stP_K (a : Fin 3) : STPres (K a) := fun h hs ht => ⟨K_sym a hs, by rw [K_tr, ht]; simp⟩
lemma stP_Yk (a : Fin 3) : STPres (Yk a) := fun h hs ht => by
  refine ⟨fun b c => by simp [Yk, hs b c], ?_⟩
  simp only [trL_apply] at ht ⊢; simp [Yk, ← Finset.smul_sum, ← map_sum, ht]

set_option maxHeartbeats 1000000 in
lemma stP_nab (a : Fin 3) : STPres (nab a) := fun h hs ht => by
  have s01 := hs 0 1; have s02 := hs 0 2; have s12 := hs 1 2
  have t := ht; simp only [trL_apply, Fin.sum_univ_three] at t
  refine ⟨fun b c => ?_, ?_⟩
  · fin_cases a <;> fin_cases b <;> fin_cases c <;>
      simp [nab, Fin.sum_univ_three, eps, s01, s02, s12] <;> ring
  · have e : h 2 2 = -h 0 0 - h 1 1 := by linear_combination t
    fin_cases a <;> simp [nab, Fin.sum_univ_three, eps, e] <;> ring

lemma stP_lap : STPres lap := STPres.sum fun a => (stP_nab a).mul (stP_nab a)
lemma stP_combK (α : Fin 3 → ℂ) : STPres (∑ a, α a • K a) := STPres.sum fun a => (stP_K a).smul _
lemma stP_combY (α : Fin 3 → ℂ) : STPres (∑ a, α a • Yk a) := STPres.sum fun a => (stP_Yk a).smul _

/-- Operators that preserve `Z`, symmetry, tracelessness and degree. -/
structure Good (O : Module.End ℂ Ten) : Prop where
  pres : Pres O
  st : STPres O
  deg : DegPres O

lemma Good.symTL {O : Module.End ℂ Ten} (hO : Good O) {d : ℕ} {h : Ten} (hh : h ∈ SymTL d) : O h ∈ SymTL d :=
  ⟨(hO.st h hh.1 hh.2.1).1, (hO.st h hh.1 hh.2.1).2, hO.deg d h hh.2.2⟩

/-- A good operator, descended to `S³`, preserves `Pd`. -/
lemma Good.Sd {O : Module.End ℂ Ten} (hO : Good O) {d : ℕ} {v : Q} (hv : v ∈ Sd d) : desc O v ∈ Sd d := by
  obtain ⟨h, hh, rfl⟩ := hv
  exact ⟨O h, hO.symTL hh, by simp [desc_mk hO.pres]⟩

lemma good_K (a : Fin 3) : Good (K a) := ⟨pres_K a, stP_K a, degP_K a⟩
lemma good_Yk (a : Fin 3) : Good (Yk a) := ⟨pres_Yk a, stP_Yk a, degP_Yk a⟩
lemma good_lap : Good lap :=
  ⟨Pres.sum fun a => ((pres_D a).add (pres_L a)).mul ((pres_D a).add (pres_L a)), stP_lap, degP_lap⟩
lemma good_combK (α : Fin 3 → ℂ) : Good (∑ a, α a • K a) := ⟨pres_combK α, stP_combK α, degP_combK α⟩
lemma good_combY (α : Fin 3 → ℂ) : Good (∑ a, α a • Yk a) := ⟨pres_combY α, stP_combY α, degP_combY α⟩
lemma good_hK : Good hK := by rw [combs.1]; exact good_combK _
lemma good_eK : Good eK := by rw [combs.2.1]; exact good_combK _
lemma good_fK : Good fK := by rw [combs.2.2.1]; exact good_combK _
lemma good_hY : Good hY := by rw [combs.2.2.2.1]; exact good_combY _
lemma good_eY : Good eY := by rw [combs.2.2.2.2.1]; exact good_combY _
lemma good_fY : Good fY := by rw [combs.2.2.2.2.2]; exact good_combY _

/-- **Item 1, invariance.** `∇²`, and both `sl₂` triples, descended to `S³`, preserve `Pd`; the divergence maps
the degree-`≤ d` symmetric traceless fields to degree-`≤ d` vector fields. -/
theorem Sd_invariant (d : ℕ) :
    (∀ v ∈ Sd d, desc lap v ∈ Sd d) ∧
    (∀ v ∈ Sd d, desc hK v ∈ Sd d ∧ desc eK v ∈ Sd d ∧ desc fK v ∈ Sd d) ∧
    (∀ v ∈ Sd d, desc hY v ∈ Sd d ∧ desc eY v ∈ Sd d ∧ desc fY v ∈ Sd d) ∧
    (∀ h ∈ SymTL d, DegLeV d (dvL h)) :=
  ⟨fun _ hv => good_lap.Sd hv, fun _ hv => ⟨good_hK.Sd hv, good_eK.Sd hv, good_fK.Sd hv⟩,
    fun _ hv => ⟨good_hY.Sd hv, good_eY.Sd hv, good_fY.Sd hv⟩, fun _ hh => dv_DegLe hh.2.2⟩

/-! ### Reduction modulo `|x|² = 1`, and a spanning family for `Pd`

Every monomial is congruent on `S³` to a combination of monomials of no larger degree with `x₀`-exponent
`≤ 1` (`x₀² = 1 − x₁² − x₂² − x₃²`). In degree `N` these are indexed by `(p, q) ∈ [0, N]²`:
`x₁^p x₂^q x₃^(N−p−q)` if `p + q ≤ N`, and `x₀ x₁^(N−p) x₂^(N−q) x₃^(p+q−N−1)` otherwise. -/

/-- Polynomials vanishing on `S³`. -/
noncomputable def Zs : Submodule ℂ P where
  carrier := {p | ∀ x ∈ S3, ev x p = 0}
  zero_mem' := by intro x _; simp
  add_mem' := by intro p q hp hq x hx; simp [hp x hx, hq x hx]
  smul_mem' := by
    intro r p hp x hx; have := hp x hx; simp only [ev] at this; simp [smul_eq_C_mul, ev, this]

/-- The reduced monomials of degree `N`, indexed by `[0, N]²`. -/
noncomputable def rmon (N p q : ℕ) : P :=
  if p + q ≤ N then mono 0 p q (N - p - q) else mono 1 (N - p) (N - q) (p + q - N - 1)

/-- The index set of the reduced monomials of degree `≤ d`. -/
abbrev RIdx (d : ℕ) := Σ N : Fin (d + 1), Fin (N + 1) × Fin (N + 1)

/-- The reduced monomials of degree `≤ d`, plus everything vanishing on `S³`. -/
noncomputable def Red (d : ℕ) : Submodule ℂ P :=
  Submodule.span ℂ (Set.range fun i : RIdx d => rmon i.1 i.2.1 i.2.2) ⊔ Zs

lemma rmon_mem {d N p q : ℕ} (hN : N ≤ d) (hp : p ≤ N) (hq : q ≤ N) : rmon N p q ∈ Red d :=
  Submodule.mem_sup_left (Submodule.subset_span
    ⟨⟨⟨N, by omega⟩, ⟨p, by show p < N + 1; omega⟩, ⟨q, by show q < N + 1; omega⟩⟩, rfl⟩)

lemma mono_red {d : ℕ} : ∀ a b c e, a + b + c + e ≤ d → mono a b c e ∈ Red d := by
  intro a
  induction a using Nat.strong_induction_on with
  | _ a ih =>
    intro b c e h
    rcases a with _ | _ | a
    · have := rmon_mem (d := d) (N := b + c + e) (p := b) (q := c) (by omega) (by omega) (by omega)
      rwa [rmon, if_pos (by omega), show b + c + e - b - c = e by omega] at this
    · have := rmon_mem (d := d) (N := 1 + b + c + e) (p := 1 + c + e) (q := 1 + b + e)
        (by omega) (by omega) (by omega)
      rwa [rmon, if_neg (by omega), show 1 + b + c + e - (1 + c + e) = b by omega,
        show 1 + b + c + e - (1 + b + e) = c by omega,
        show 1 + c + e + (1 + b + e) - (1 + b + c + e) - 1 = e by omega] at this
    · have key : mono (a + 2) b c e = mono a b c e - mono a (b + 2) c e - mono a b (c + 2) e
          - mono a b c (e + 2) + mono a b c e * (rho - 1) := by
        simp only [mono, rho, Fin.sum_univ_four]; ring
      have hz : mono a b c e * (rho - 1) ∈ Red d := Submodule.mem_sup_right (by
        intro x hx
        have : ∑ i, x i ^ 2 = 1 := hx
        simp only [map_mul, map_sub, map_one, rho, map_sum, map_pow, ev, eval_X]
        rw [show ∑ i, ((x i : ℂ)) ^ 2 = ((∑ i, x i ^ 2 : ℝ) : ℂ) by push_cast; rfl, this]; simp)
      rw [key]
      refine Submodule.add_mem _ (Submodule.sub_mem _ (Submodule.sub_mem _ (Submodule.sub_mem _ ?_ ?_) ?_) ?_) hz
      · exact ih a (by omega) b c e (by omega)
      · exact ih a (by omega) _ c e (by omega)
      · exact ih a (by omega) b _ e (by omega)
      · exact ih a (by omega) b c _ (by omega)

/-- Every polynomial of degree `≤ d` is, on `S³`, a combination of the reduced monomials of degree `≤ d`. -/
lemma DL_red {d : ℕ} {p : P} (hp : DL d p) : p ∈ Red d :=
  deg_induction (· ∈ Red d) (Submodule.zero_mem _) (fun _ _ => Submodule.add_mem _)
    (fun c _ => Submodule.smul_mem _ c) (fun a b c e h => mono_red a b c e h) p hp

/-- The five constant symmetric traceless tensors. -/
noncomputable def Eb : Fin 5 → Ten
  | 0 => ![![1, 0, 0], ![0, 0, 0], ![0, 0, -1]]
  | 1 => ![![0, 0, 0], ![0, 1, 0], ![0, 0, -1]]
  | 2 => ![![0, 1, 0], ![1, 0, 0], ![0, 0, 0]]
  | 3 => ![![0, 0, 1], ![0, 0, 0], ![1, 0, 0]]
  | 4 => ![![0, 0, 0], ![0, 0, 1], ![0, 1, 0]]

/-- The coordinates of a symmetric traceless tensor in the basis `Eb`. -/
def coefT (h : Ten) : Fin 5 → P := ![h 0 0, h 1 1, h 0 1, h 0 2, h 1 2]

lemma symTL_decomp {h : Ten} (hs : IsSym h) (ht : trL h = 0) : h = ∑ r, smulT (coefT h r) (Eb r) := by
  have t := ht; simp only [trL_apply, Fin.sum_univ_three] at t
  have e : h 2 2 = -h 0 0 - h 1 1 := by linear_combination t
  funext b c
  fin_cases b <;> fin_cases c <;>
    simp [Fin.sum_univ_five, smulT, Eb, coefT, e, hs 1 0, hs 2 0, hs 2 1] <;> ring

/-- `f ↦ f · T`, as a linear map. -/
noncomputable def smulTL (T : Ten) : P →ₗ[ℂ] Ten where
  toFun f := smulT f T
  map_add' f g := by funext b c; simp [smulT, add_mul]
  map_smul' r f := by funext b c; simp [smulT, smul_eq_C_mul, mul_assoc]

/-- The spanning family of `Pd`: reduced monomials times the five constant tensors. -/
abbrev GIdx (d : ℕ) := RIdx d × Fin 5

noncomputable def Gv (d : ℕ) (i : GIdx d) : Q :=
  Submodule.Quotient.mk (smulT (rmon i.1.1 i.1.2.1 i.1.2.2) (Eb i.2))

lemma Sd_le_span (d : ℕ) : Sd d ≤ Submodule.span ℂ (Set.range (Gv d)) := by
  rintro _ ⟨h, ⟨hs, ht, hd⟩, rfl⟩
  have hdec := symTL_decomp hs ht
  rw [hdec, map_sum]
  refine Submodule.sum_mem _ fun r _ => ?_
  let ι : P →ₗ[ℂ] Q := Z.mkQ ∘ₗ smulTL (Eb r)
  have hle : Red d ≤ (Submodule.span ℂ (Set.range (Gv d))).comap ι := by
    refine sup_le (Submodule.span_le.mpr ?_) ?_
    · rintro _ ⟨i, rfl⟩
      exact Submodule.subset_span ⟨(i, r), rfl⟩
    · intro z hz
      rw [Submodule.mem_comap]
      have : ι z = 0 := by
        simp only [ι, LinearMap.comp_apply, Submodule.mkQ_apply, Submodule.Quotient.mk_eq_zero]
        intro b c x hx
        simp [smulTL, smulT, hz x hx]
      rw [this]; exact Submodule.zero_mem _
  have hc : DL d (coefT h r) := by fin_cases r <;> exact hd _ _
  exact hle (DL_red hc)

instance Sd_fd (d : ℕ) : FiniteDimensional ℂ (Sd d) :=
  have : FiniteDimensional ℂ (Submodule.span ℂ (Set.range (Gv d))) :=
    FiniteDimensional.span_of_finite ℂ (Set.finite_range _)
  Submodule.finiteDimensional_of_le (Sd_le_span d)

lemma card_GIdx (d : ℕ) : Fintype.card (GIdx d) = ∑ N : Fin (d + 1), ((N : ℕ) + 1) * ((N : ℕ) + 1) * 5 := by
  simp [Fintype.card_sigma, Finset.sum_mul]

/-- **Item 1, finiteness.** `Pd` is finite-dimensional, of dimension at most `5 Σ_{N ≤ d} (N+1)²`. -/
theorem Sd_finrank_le (d : ℕ) :
    Module.finrank ℂ (Sd d) ≤ ∑ N : Fin (d + 1), ((N : ℕ) + 1) * ((N : ℕ) + 1) * 5 := by
  haveI : FiniteDimensional ℂ (Submodule.span ℂ (Set.range (Gv d))) :=
    FiniteDimensional.span_of_finite ℂ (Set.finite_range _)
  rw [← card_GIdx]
  exact (Submodule.finrank_mono (Sd_le_span d)).trans (finrank_range_le_card _)

/-- `deg`, also knowing `w` and `u`. -/
macro "degw" : tactic => `(tactic| (
  apply DL.mono
  repeat' first
    | exact DL_w
    | exact DL_u
    | exact DL.var _
    | exact DL.iI
    | exact DL.one
    | exact DL.zero
    | exact DL.ofNat _
    | exact DL.const _
    | apply DL.add'
    | apply DL.sub'
    | apply DL.neg
    | apply DL.mul
    | apply DL.pow
  all_goals omega))

/-! ## 10. The five highest-weight seeds

In `V_{N/2} ⊗ V₂` (components homogeneous of degree `N` in `w, u`, the spin-2 index space) there is one
`K`-highest-weight line of each weight `N + 4 − 2t`, `0 ≤ t ≤ min 4 N`. It is spanned by `w^(N−t) T_t`, with
`T_t` of degree `t`: `T₀ = TU`, `T₄ = TL` (campaign 51), and `T₁, T₂, T₃` below. -/

@[simp] lemma D_three (a : Fin 3) : D a (3 : P) = 0 := by
  rw [show (3 : P) = C 3 from (map_ofNat C 3).symm]; exact derivation_C _ _
@[simp] lemma D_four (a : Fin 3) : D a (4 : P) = 0 := by
  rw [show (4 : P) = C 4 from (map_ofNat C 4).symm]; exact derivation_C _ _
@[simp] lemma Y_three (a : Fin 3) : Y a (3 : P) = 0 := by
  rw [show (3 : P) = C 3 from (map_ofNat C 3).symm]; exact derivation_C _ _
@[simp] lemma Y_four (a : Fin 3) : Y a (4 : P) = 0 := by
  rw [show (4 : P) = C 4 from (map_ofNat C 4).symm]; exact derivation_C _ _
@[simp] lemma eYd_three : eYd (3 : P) = 0 := by
  rw [show (3 : P) = C 3 from (map_ofNat C 3).symm]; exact derivation_C _ _
@[simp] lemma eYd_four : eYd (4 : P) = 0 := by
  rw [show (4 : P) = C 4 from (map_ofNat C 4).symm]; exact derivation_C _ _
@[simp] lemma ev_two (x : Fin 4 → ℝ) : ev x (2 : P) = 2 := map_ofNat _ 2

noncomputable def T1 : Ten := ![![-2 * u, 2 * ii * u, ii * w], ![2 * ii * u, 2 * u, w], ![ii * w, w, 0]]
noncomputable def T2 : Ten :=
  ![![-(3 * u ^ 2 + w ^ 2), 3 * ii * u ^ 2, 3 * ii * u * w], ![3 * ii * u ^ 2, 3 * u ^ 2 - w ^ 2, 3 * u * w],
    ![3 * ii * u * w, 3 * u * w, 2 * w ^ 2]]
noncomputable def T3 : Ten :=
  ![![-2 * u * (u ^ 2 + w ^ 2), 2 * ii * u ^ 3, ii * w * (3 * u ^ 2 + w ^ 2)],
    ![2 * ii * u ^ 3, 2 * u * (u ^ 2 - w ^ 2), w * (3 * u ^ 2 - w ^ 2)],
    ![ii * w * (3 * u ^ 2 + w ^ 2), w * (3 * u ^ 2 - w ^ 2), 4 * u * w ^ 2]]

/-- The properties of a degree-`t` seed tensor. -/
structure TP (T : Ten) (t : ℕ) : Prop where
  sym : IsSym T
  tr : trL T = 0
  eK0 : eK T = 0
  hKw : hK T = ((4 : ℂ) - t) • T
  eY0 : eY T = 0
  hYw : hY T = (t : ℂ) • T
  ctr : ∀ b c, ∑ a, D a w * D a (T b c) = -(t : P) * w * T b c
  sj : ∀ b c, ∑ a, D a (D a (T b c)) = -((t : P) * (t + 2)) * T b c
  deg : DegLe t T

macro "tcomp" : tactic => `(tactic| (funext b c; fin_cases b <;> fin_cases c <;>
  simp [eK, hK, K_apply, Fin.sum_univ_three, eps, smul_eq_C_mul, Derivation.leibniz,
    Derivation.leibniz_pow, -mul_eq_zero] <;> iring))

set_option maxHeartbeats 4000000 in
lemma TP_T1 : TP T1 1 where
  sym b c := by fin_cases b <;> fin_cases c <;> rfl
  tr := by simp [T1, Fin.sum_univ_three]
  eK0 := by unfold T1; tcomp
  hKw := by unfold T1; norm_num; tcomp
  eY0 := by
    funext b c; rw [eY_apply]
    fin_cases b <;> fin_cases c <;> simp [T1, Derivation.leibniz]
  hYw := by
    funext b c; rw [hY_apply]
    fin_cases b <;> fin_cases c <;> simp [T1, Derivation.leibniz, smul_eq_C_mul] <;> iring
  ctr b c := by
    fin_cases b <;> fin_cases c <;> simp [T1, Fin.sum_univ_three, Derivation.leibniz] <;> iring
  sj b c := by
    fin_cases b <;> fin_cases c <;> simp [T1, Fin.sum_univ_three, Derivation.leibniz] <;> iring
  deg b c := by fin_cases b <;> fin_cases c <;> simp only [T1] <;> simp <;> degw

set_option maxHeartbeats 4000000 in
lemma TP_T2 : TP T2 2 where
  sym b c := by fin_cases b <;> fin_cases c <;> rfl
  tr := by simp [T2, Fin.sum_univ_three]; ring
  eK0 := by unfold T2; tcomp
  hKw := by unfold T2; norm_num; tcomp
  eY0 := by
    funext b c; rw [eY_apply]
    fin_cases b <;> fin_cases c <;> simp [T2, Derivation.leibniz, Derivation.leibniz_pow]
  hYw := by
    funext b c; rw [hY_apply]
    fin_cases b <;> fin_cases c <;> simp [T2, Derivation.leibniz, Derivation.leibniz_pow, smul_eq_C_mul] <;> iring
  ctr b c := by
    fin_cases b <;> fin_cases c <;> simp [T2, Fin.sum_univ_three, Derivation.leibniz, Derivation.leibniz_pow] <;>
      iring
  sj b c := by
    fin_cases b <;> fin_cases c <;> simp [T2, Fin.sum_univ_three, Derivation.leibniz, Derivation.leibniz_pow] <;>
      iring
  deg b c := by fin_cases b <;> fin_cases c <;> simp only [T2] <;> simp <;> degw

set_option maxHeartbeats 8000000 in
lemma TP_T3 : TP T3 3 where
  sym b c := by fin_cases b <;> fin_cases c <;> rfl
  tr := by simp [T3, Fin.sum_univ_three]; ring
  eK0 := by unfold T3; tcomp
  hKw := by unfold T3; norm_num; tcomp
  eY0 := by
    funext b c; rw [eY_apply]
    fin_cases b <;> fin_cases c <;> simp [T3, Derivation.leibniz, Derivation.leibniz_pow]
  hYw := by
    funext b c; rw [hY_apply]
    fin_cases b <;> fin_cases c <;> simp [T3, Derivation.leibniz, Derivation.leibniz_pow, smul_eq_C_mul] <;> iring
  ctr b c := by
    fin_cases b <;> fin_cases c <;> simp [T3, Fin.sum_univ_three, Derivation.leibniz, Derivation.leibniz_pow] <;>
      iring
  sj b c := by
    fin_cases b <;> fin_cases c <;> simp [T3, Fin.sum_univ_three, Derivation.leibniz, Derivation.leibniz_pow] <;>
      iring
  deg b c := by fin_cases b <;> fin_cases c <;> simp only [T3] <;> simp <;> degw

lemma TP_TU : TP TU 0 where
  sym := outer_sym _
  tr := TU_tr
  eK0 := eK_TU
  hKw := by simpa using hK_TU
  eY0 := eY_TU
  hYw := by simpa using hY_TU
  ctr b c := by simp [D_TU]
  sj b c := by simp [D_TU]
  deg b c := by fin_cases b <;> fin_cases c <;> simp [TU, outer, vC] <;> degw

lemma TP_TL : TP TL 4 where
  sym := outer_sym _
  tr := TL_tr
  eK0 := eK_TL
  hKw := by simpa using hK_TL
  eY0 := eY_TL
  hYw := by simpa using hY_TL
  ctr b c := by rw [TL_B]; norm_num
  sj b c := by rw [TL_S]; norm_num
  deg b c := by
    have hp : ∀ b, DL 2 (pR b) := fun b => by fin_cases b <;> simp [pR] <;> degw
    exact (hp b).mul (hp c)

/-- The seed tensors `T_t`, `t = 0, …, 4`. -/
noncomputable def Tt : ℕ → Ten
  | 0 => TU
  | 1 => T1
  | 2 => T2
  | 3 => T3
  | _ => TL

lemma TP_Tt {t : ℕ} (ht : t ≤ 4) : TP (Tt t) t := by
  interval_cases t
  exacts [TP_TU, TP_T1, TP_T2, TP_T3, TP_TL]

/-- **The seeds**: `w^(N−t) T_t`, highest weight `(N + 4 − 2t, N)` for `(hK, hY)`, frame Casimir `−N(N+2)`. -/
noncomputable def seed (N t : ℕ) : Ten := smulT (w ^ (N - t)) (Tt t)

lemma seed_zero (N : ℕ) : seed N 0 = sU N := rfl
lemma seed_four (N : ℕ) : seed N 4 = sL (N - 4) := rfl

/-! ## 11. Casimirs, and `∇²` through them -/

/-- The Casimir of the Lie derivatives `K_a` (the right-invariant `SU(2)` acting on tensor fields). -/
noncomputable def CK : Module.End ℂ Ten := ∑ a, K a * K a
/-- The Casimir of the right-invariant fields, componentwise. -/
noncomputable def CY : Module.End ℂ Ten := ∑ a, Yk a * Yk a
/-- The index Casimir `Σ_a L_a L_a` (spin of the index pair). -/
noncomputable def LL : Module.End ℂ Ten := ∑ a, Lt a * Lt a

/-- **`∇²` through Casimirs** (exact, on `ℝ⁴`): `∇² = ½(S_J + C_K) − Σ_a L_a²`. -/
theorem lap_casimir : lap = (1 / 2 : ℂ) • (SJ + CK) - LL := by
  simp only [lap, CK, SJ, LL, nab, K, Fin.sum_univ_three, add_mul, mul_add, smul_mul_assoc, mul_smul_comm,
    smul_add, smul_smul]
  module

set_option maxHeartbeats 2000000 in
/-- On symmetric traceless tensors the index pair has spin 2: `Σ_a L_a² = −6`. -/
lemma LL_symTL {h : Ten} (hs : IsSym h) (ht : trL h = 0) : LL h = (-6 : ℂ) • h := by
  have s01 := hs 0 1; have s02 := hs 0 2; have s12 := hs 1 2
  have t := ht; simp only [trL_apply, Fin.sum_univ_three] at t
  have e : h 2 2 = -h 0 0 - h 1 1 := by linear_combination t
  funext b c
  simp only [LL, LinearMap.sum_apply, Finset.sum_apply, Module.End.mul_apply, Fin.sum_univ_three]
  fin_cases b <;> fin_cases c <;> simp [Fin.sum_univ_three, eps, smul_eq_C_mul, s01, s02, s12, e] <;> ring

open Complex in
/-- On a `K`-primitive tensor of weight `μ`, `C_K = −μ(μ + 2)` (pointwise: `K₀s = iK₁s`, `K₂s = iμs`,
`[K₀, K₁] = 2K₂`). -/
lemma CK_prim {s : Ten} {μ : ℂ} (he : eK s = 0) (hh : hK s = μ • s) : CK s = (-(μ * (μ + 2))) • s := by
  have e0 : K 0 s = I • K 1 s := by
    have := he; simp only [eK, LinearMap.sub_apply, LinearMap.smul_apply] at this; exact sub_eq_zero.mp this
  have e2 : K 2 s = (I * μ) • s := by
    have h2 : -I • K 2 s = μ • s := by simpa [hK] using hh
    calc K 2 s = (I * -I) • K 2 s := by rw [show I * -I = 1 by rw [mul_neg, I_mul_I, neg_neg], one_smul]
      _ = I • (-I • K 2 s) := by rw [smul_smul]
      _ = I • (μ • s) := by rw [h2]
      _ = (I * μ) • s := by rw [smul_smul]
  have r01 : K 0 (K 1 s) = K 1 (K 0 s) + (2 : ℂ) • K 2 s := by
    have := LinearMap.congr_fun (K_bracket 0 1) s
    simp only [Fin.sum_univ_three, eps, LinearMap.sub_apply, Module.End.mul_apply, LinearMap.add_apply,
      LinearMap.smul_apply] at this
    norm_num at this
    rw [← this]; abel
  simp only [CK, Fin.sum_univ_three, LinearMap.add_apply, Module.End.mul_apply]
  rw [e0, map_smul, r01, e0, map_smul, e2, map_smul, e2]
  simp only [smul_add, smul_smul]
  match_scalars <;> ring_nf <;> simp only [I_sq] <;> ring_nf

/-- `Σ_a δ_a δ_a (pq)`, by Leibniz. -/
lemma lap_mul (δ : Fin 3 → Derivation ℂ P P) (p q : P) :
    ∑ a, δ a (δ a (p * q)) = (∑ a, δ a (δ a p)) * q + 2 * (∑ a, δ a p * δ a q) + p * ∑ a, δ a (δ a q) := by
  simp only [Derivation.leibniz, smul_eq_mul, map_add, Fin.sum_univ_three]; ring
lemma bil_mul (δ : Fin 3 → Derivation ℂ P P) (p q r : P) :
    ∑ a, δ a (p * q) * δ a r = (∑ a, δ a p * δ a r) * q + p * ∑ a, δ a q * δ a r := by
  simp only [Derivation.leibniz, smul_eq_mul, Fin.sum_univ_three]; ring

/-- **The two Casimirs on functions agree**: `Σ_a E_a² = Σ_a Y_a²` on `ℂ[x₀..x₃]` (both are
`|x|²Δ − E(E + 2)`, `E` the Euler field). -/
theorem SJ_eq_CY_fun (p : P) : ∑ a, D a (D a p) = ∑ a, Y a (Y a p) := by
  have hX : ∀ j : Fin 4, ∑ a, D a (D a (X j)) = ∑ a, Y a (Y a (X j)) := by
    intro j; fin_cases j <;> simp [Fin.sum_univ_three, dval, yval]
  have hB : ∀ i j : Fin 4, ∑ a, D a (X j) * D a (X i) = ∑ a, Y a (X j) * Y a (X i) := by
    intro i j; fin_cases i <;> fin_cases j <;> simp [Fin.sum_univ_three, dval, yval] <;> ring
  suffices H : ∑ a, D a (D a p) = ∑ a, Y a (Y a p) ∧
      ∀ i, ∑ a, D a p * D a (X i) = ∑ a, Y a p * Y a (X i) from H.1
  induction p using MvPolynomial.induction_on with
  | C c => simp [derivation_C]
  | add p q hp hq =>
    refine ⟨by simp [Finset.sum_add_distrib, hp.1, hq.1], fun i => ?_⟩
    simp only [map_add, add_mul, Finset.sum_add_distrib, hp.2 i, hq.2 i]
  | mul_X p j hp =>
    refine ⟨?_, fun i => ?_⟩
    · rw [lap_mul D, lap_mul Y, hp.1, hp.2 j, hX j]
    · rw [bil_mul D, bil_mul Y, hp.2 i, hB i j]

/-- `S_J = C_Y` on tensor fields (exactly). -/
theorem SJ_eq_CY : SJ = CY := by
  refine LinearMap.ext fun h => ?_; funext b c
  have e := SJ_eq_CY_fun (h b c)
  simp only [SJ, CY, Yk, LinearMap.sum_apply, Finset.sum_apply, Module.End.mul_apply, LinearMap.smul_apply,
    Pi.smul_apply, DtL_apply, map_smul, smul_smul] at e ⊢
  rw [e]; refine Finset.sum_congr rfl fun a _ => ?_
  fin_cases a <;> simp [sY]

/-- **Item 2.** On symmetric traceless tensor fields, `−∇² = −6 − ½(C_Y + C_K)`: the right-invariant Casimir
(= the frame Casimir on components) and the Casimir of the Lie derivatives `K_a`. -/
theorem neg_lap_casimir {h : Ten} (hs : IsSym h) (ht : trL h = 0) :
    -lap h = (-6 : ℂ) • h - (1 / 2 : ℂ) • (CY h + CK h) := by
  rw [lap_casimir, ← SJ_eq_CY]
  simp only [LinearMap.sub_apply, LinearMap.smul_apply, LinearMap.add_apply, LL_symTL hs ht]
  module

/-! ### The Casimirs commute with both `sl₂` actions -/

lemma CK_K (a : Fin 3) : CK * K a = K a * CK := casimir_comm K (K a) a (fun b => K_bracket b a)
lemma CK_Yk (a : Fin 3) : CK * Yk a = Yk a * CK := by
  simp only [CK, Finset.sum_mul, Finset.mul_sum]
  refine Finset.sum_congr rfl fun b _ => ?_
  have c : Commute (K b) (Yk a) := (Yt_K a b).symm
  exact (c.mul_left c).eq

/-- An operator commuting with all `K_a` and `Yk_a` commutes with the multiplet maps. -/
lemma mem_comm {O : Module.End ℂ Ten} (hK : ∀ a, O * K a = K a * O) (hY : ∀ a, O * Yk a = Yk a * O)
    (s : Ten) (p q : ℕ) : O (mem s p q) = mem (O s) p q := by
  have cK : Commute O fK := by
    rw [combs.2.2.1]
    exact Commute.sum_right _ _ _ fun a _ => (show Commute O (K a) from hK a).smul_right _
  have cY : Commute O fY := by
    rw [combs.2.2.2.2.2]
    exact Commute.sum_right _ _ _ fun a _ => (show Commute O (Yk a) from hY a).smul_right _
  simp only [mem]
  rw [← Module.End.mul_apply, (cY.pow_right q).eq, Module.End.mul_apply, ← Module.End.mul_apply O,
    (cK.pow_right p).eq, Module.End.mul_apply]

/-! ### The seeds' properties -/

/-- The weight `μ = N + 4 − 2t` of the seed `(N, t)` under `hK`, and the eigenvalue of `−∇²` there. -/
def muK (N t : ℕ) : ℕ := N + 4 - 2 * t
noncomputable def lamNt (N t : ℕ) : ℂ := ((N : ℂ) * (N + 2) + (muK N t : ℂ) * (muK N t + 2)) / 2 - 6

lemma seed_SJ (N t : ℕ) (ht : t ≤ N) (htt : t ≤ 4) : SJ (seed N t) = (-((N : ℂ) * (N + 2))) • seed N t := by
  obtain ⟨n, rfl⟩ : ∃ n, N = n + t := ⟨N - t, by omega⟩
  have T := TP_Tt htt
  funext b c
  rw [seed, show n + t - t = n by omega, SJ_smulT, S_wpow, wpow_contract D n _ (-(t : P)) _ (T.ctr b c),
    T.sj b c]
  simp [smulT, smul_eq_C_mul]; ring

lemma seed_weights' (N t : ℕ) (ht : t ≤ N) (htt : t ≤ 4) :
    eK (seed N t) = 0 ∧ hK (seed N t) = ((muK N t : ℕ) : ℂ) • seed N t ∧
    eY (seed N t) = 0 ∧ hY (seed N t) = ((N : ℕ) : ℂ) • seed N t := by
  obtain ⟨n, rfl⟩ : ∃ n, N = n + t := ⟨N - t, by omega⟩
  have T := TP_Tt htt
  obtain ⟨a, b, c, d⟩ := seed_weights n (Tt t) _ _ T.eK0 T.hKw T.eY0 T.hYw
  have e : n + t - t = n := by omega
  refine ⟨by rw [seed, e]; exact a, ?_, by rw [seed, e]; exact c, ?_⟩
  · rw [seed, e, b, muK, show n + t + 4 - 2 * t = n + (4 - t) by omega]
    push_cast [Nat.cast_sub htt]; ring_nf
  · rw [seed, e, d]; push_cast; ring_nf

lemma seed_symTL (N t : ℕ) (ht : t ≤ N) (htt : t ≤ 4) : seed N t ∈ SymTL N := by
  obtain ⟨n, rfl⟩ : ∃ n, N = n + t := ⟨N - t, by omega⟩
  have T := TP_Tt htt
  rw [seed, show n + t - t = n by omega]
  refine ⟨fun b c => by simp [smulT, T.sym b c], ?_, fun b c => ?_⟩
  · simp only [trL_apply] at T ⊢; have := T.tr; simp only [trL_apply] at this
    simp only [smulT, ← Finset.mul_sum, this, mul_zero]
  · exact ((DL_w.pow n).mul (T.deg b c)).mono (by omega)

/-- The point `(1,0,0,0)` sees every seed. -/
lemma seed_ne (N t : ℕ) (htt : t ≤ 4) : (Submodule.Quotient.mk (seed N t) : Q) ≠ 0 := by
  interval_cases t
  · exact mk_ne_zero _ 0 0 pt pt_S3 (by simp [seed, Tt, smulT, TU, outer, vC])
  · exact mk_ne_zero _ 0 2 pt pt_S3 (by simp [seed, Tt, smulT, T1])
  · exact mk_ne_zero _ 2 2 pt pt_S3 (by simp [seed, Tt, smulT, T2])
  · exact mk_ne_zero _ 0 2 pt pt_S3 (by simp [seed, Tt, smulT, T3])
  · exact mk_ne_zero _ 0 0 pt pt_S3 (by simp [seed, Tt, smulT, TL, outer, pR])

lemma seed_Seed (N t : ℕ) (ht : t ≤ N) (htt : t ≤ 4) :
    Seed (seed N t) (muK N t) N (-((N : ℂ) * (N + 2))) := by
  obtain ⟨a, b, c, d⟩ := seed_weights' N t ht htt
  exact ⟨seed_ne N t htt, a, b, c, d, seed_SJ N t ht htt⟩

lemma seed_CK (N t : ℕ) (ht : t ≤ N) (htt : t ≤ 4) :
    CK (seed N t) = (-((muK N t : ℂ) * (muK N t + 2))) • seed N t := by
  obtain ⟨a, b, -, -⟩ := seed_weights' N t ht htt
  exact CK_prim a b

/-- **The eigenvalue of `−∇²` on the seed `(N, t)`**: `½(N(N+2) + μ(μ+2)) − 6`, `μ = N + 4 − 2t`. -/
lemma seed_lap (N t : ℕ) (ht : t ≤ N) (htt : t ≤ 4) : lap (seed N t) = (-lamNt N t) • seed N t := by
  have hs := seed_symTL N t ht htt
  rw [lap_casimir]
  simp only [LinearMap.sub_apply, LinearMap.smul_apply, LinearMap.add_apply, LL_symTL hs.1 hs.2.1,
    seed_SJ N t ht htt, seed_CK N t ht htt, lamNt]
  module

/-! ## 12. The operator `O = Ł ∘ div`, which sees exactly the non-TT seeds

`Ł` is (6×) the conformal Killing operator, `(Łv)_bc = 3(E_b v_c + E_c v_b) − 2δ_bc E_a v_a` (the connection
terms of `∇_b v_c` are antisymmetric and drop out). `O = Ł ∘ div` commutes with both `sl₂` actions, kills
every divergence-free field, and acts on the seed `(N, t)` by the scalar `κ(N, t)`, which is nonzero exactly for
`t = 1, 2, 3`. -/

/-- The (scaled) conformal Killing operator. -/
noncomputable def ckL : Vec →ₗ[ℂ] Ten where
  toFun v := fun b c => 3 * (D b (v c) + D c (v b)) - (if b = c then 2 * ∑ a, D a (v a) else 0)
  map_add' v v' := by
    funext b c; simp only [Pi.add_apply, map_add]
    split_ifs <;> simp [Finset.sum_add_distrib] <;> ring
  map_smul' r v := by
    funext b c; simp only [Pi.smul_apply, Derivation.map_smul, smul_eq_C_mul, RingHom.id_apply]
    split_ifs <;> simp [Fin.sum_univ_three] <;> ring

lemma ckL_apply (v : Vec) (b c : Fin 3) :
    ckL v b c = 3 * (D b (v c) + D c (v b)) - (if b = c then 2 * ∑ a, D a (v a) else 0) := rfl

/-- `O = Ł ∘ div`. -/
noncomputable def Oop : Module.End ℂ Ten := ckL ∘ₗ dvL

lemma Oop_apply (h : Ten) : Oop h = ckL (dvL h) := rfl

/-! ### Equivariance -/

lemma D_comm_10 (p : P) : D 1 (D 0 p) = D 0 (D 1 p) - 2 * D 2 p := by
  have := congrArg (fun δ : Derivation ℂ P P => δ p) (frame_bracket 0 1)
  simp [Derivation.commutator_apply, Fin.sum_univ_three, eps, smul_eq_C_mul] at this
  linear_combination -this
lemma D_comm_20 (p : P) : D 2 (D 0 p) = D 0 (D 2 p) + 2 * D 1 p := by
  have := congrArg (fun δ : Derivation ℂ P P => δ p) (frame_bracket 2 0)
  simp [Derivation.commutator_apply, Fin.sum_univ_three, eps, smul_eq_C_mul] at this
  linear_combination this
lemma D_comm_21 (p : P) : D 2 (D 1 p) = D 1 (D 2 p) - 2 * D 0 p := by
  have := congrArg (fun δ : Derivation ℂ P P => δ p) (frame_bracket 1 2)
  simp [Derivation.commutator_apply, Fin.sum_univ_three, eps, smul_eq_C_mul] at this
  linear_combination -this

lemma DY_comm (a b : Fin 3) (p : P) : D b (Y a p) = Y a (D b p) := by
  have := congrArg (fun δ : Derivation ℂ P P => δ p) (left_right_commute b a)
  simp only [Derivation.commutator_apply, Derivation.zero_apply] at this
  exact sub_eq_zero.mp this

set_option maxHeartbeats 4000000 in
/-- `Ł` intertwines the Lie derivatives on vector fields and on tensor fields. -/
lemma ckL_KV (a : Fin 3) (v : Vec) : ckL (KV a v) = K a (ckL v) := by
  funext b c
  fin_cases a <;> fin_cases b <;> fin_cases c <;>
  simp [ckL_apply, KV_apply, K_apply, Fin.sum_univ_three, eps, Derivation.leibniz, D_comm_10, D_comm_20,
    D_comm_21] <;> ring

/-- The right-invariant fields on vector fields, componentwise. -/
lemma dv_Y (a : Fin 3) (h : Ten) : dvL (DtL (Y a) h) = fun c => Y a (dvL h c) := by
  funext c
  have e : ∀ b, nab b (DtL (Y a) h) = DtL (Y a) (nab b h) := fun b => by
    have := LinearMap.congr_fun (Yt_nab a b) h; simpa using this.symm
  simp only [dvL_apply, e, DtL_apply, ← map_sum]

lemma ckL_Y (a : Fin 3) (v : Vec) : ckL (fun c => Y a (v c)) = DtL (Y a) (ckL v) := by
  funext b c
  simp only [ckL_apply, DtL_apply, DY_comm, map_sub, map_add, map_mul]
  split_ifs <;> simp [map_sum, Derivation.leibniz, DY_comm]

lemma Oop_K (a : Fin 3) : Oop * K a = K a * Oop := by
  refine LinearMap.ext fun h => ?_
  simp only [Module.End.mul_apply, Oop_apply, K_dv, ckL_KV]

lemma Oop_Yk (a : Fin 3) : Oop * Yk a = Yk a * Oop := by
  refine LinearMap.ext fun h => ?_
  simp only [Module.End.mul_apply, Oop_apply, Yk, LinearMap.smul_apply, map_smul, dv_Y, ckL_Y]

/-! ### `O` on `S³` -/

lemma ckL_Z {v : Vec} (hv : ∀ c, ∀ x ∈ S3, ev x (v c) = 0) : ckL v ∈ Z := by
  intro b c x hx
  have h1 := tangent_D b _ (hv c) x hx
  have h2 := tangent_D c _ (hv b) x hx
  have h3 : ∀ a, ev x (D a (v a)) = 0 := fun a => tangent_D a _ (hv a) x hx
  rw [ckL_apply]
  split_ifs <;> simp [h1, h2, map_sum, h3]

lemma dv_Z {h : Ten} (hh : h ∈ Z) : ∀ c, ∀ x ∈ S3, ev x (dvL h c) = 0 := by
  intro c x hx
  rw [dvL_apply, map_sum]
  refine Finset.sum_eq_zero fun b _ => ?_
  exact (show Pres (nab b) from (pres_D b).add (pres_L b)) h hh b c x hx

lemma pres_O : Pres Oop := fun h hh => ckL_Z (dv_Z hh)

/-- A field whose divergence vanishes on `S³` is killed by `O` on `S³`. -/
lemma Oop_of_dv {h : Ten} (hd : ∀ c, ∀ x ∈ S3, ev x (dvL h c) = 0) :
    desc Oop (Submodule.Quotient.mk h) = 0 := by
  rw [desc_mk pres_O, Submodule.Quotient.mk_eq_zero]; exact ckL_Z hd

/-! ### `O` on the seeds

`O(wⁿ T) = (n(n−1)α + nβ + γ) wⁿ T` as soon as three contractions of `T` against `dw` are proportional
to `T`. -/

/-- The contraction `(ι T)_c = Σ_a E_a(w) T_ac`. -/
noncomputable def iota (T : Ten) : Vec := fun c => ∑ a, D a w * T a c
/-- `sym-tl(dw ⊗ U)` (scaled as `Ł`). -/
noncomputable def symW (U : Vec) : Ten :=
  fun b c => 3 * (D b w * U c + D c w * U b) - (if b = c then 2 * ∑ a, D a w * U a else 0)

lemma ckL_mul (f g : P) (hf : ∀ b, D b f = g * D b w) (U : Vec) (b c : Fin 3) :
    ckL (fun c => f * U c) b c = g * symW U b c + f * ckL U b c := by
  simp only [ckL_apply, symW, Derivation.leibniz, smul_eq_mul, hf]
  split_ifs <;> (try simp only [Fin.sum_univ_three]) <;> ring

lemma D_wpow (k : ℕ) (b : Fin 3) : D b (w ^ k) = ((k : P) * w ^ (k - 1)) * D b w := by
  rw [Derivation.leibniz_pow, smul_eq_mul, nsmul_eq_mul]; ring

lemma dv_wpow (n : ℕ) (T : Ten) :
    dvL (smulT (w ^ n) T) = fun c => ((n : P) * w ^ (n - 1)) * iota T c + w ^ n * dvL T c := by
  funext c
  rw [dv_smulT, iota, Finset.mul_sum]; simp only [D_wpow, mul_assoc]

lemma hw1 (n : ℕ) : (n : P) * w ^ (n - 1) * w = (n : P) * w ^ n := by
  rcases n with _ | n
  · simp
  · rw [show n + 1 - 1 = n by omega, pow_succ]; ring
lemma hw2 (n : ℕ) : (n : P) * ((n - 1 : ℕ) : P) * w ^ (n - 2) * w ^ 2 = (n : P) * ((n : P) - 1) * w ^ n := by
  rcases n with _ | _ | m
  · simp
  · simp
  · rw [show m + 2 - 1 = m + 1 by omega, show m + 2 - 2 = m by omega]; push_cast; ring

/-- **`O` on `wⁿ T`.** -/
theorem Oop_wpow (T : Ten) (α β γ : ℂ) (hA : ∀ b c, symW (iota T) b c = C α * w ^ 2 * T b c)
    (hB : ∀ b c, ckL (iota T) b c + symW (dvL T) b c = C β * w * T b c)
    (hC : ∀ b c, ckL (dvL T) b c = C γ * T b c) (n : ℕ) :
    Oop (smulT (w ^ n) T) = ((n : ℂ) * ((n : ℂ) - 1) * α + n * β + γ) • smulT (w ^ n) T := by
  funext b c
  rw [Oop_apply, dv_wpow]
  have split : (fun c => ((n : P) * w ^ (n - 1)) * iota T c + w ^ n * dvL T c) =
      (fun c => ((n : P) * w ^ (n - 1)) * iota T c) + (fun c => w ^ n * dvL T c) := rfl
  have e1 : ∀ b, D b ((n : P) * w ^ (n - 1)) = ((n : P) * ((n - 1 : ℕ) : P) * w ^ (n - 1 - 1)) * D b w :=
    fun b => by rw [Derivation.leibniz, D_wpow]; simp [smul_eq_mul]; ring
  rw [split, map_add, Pi.add_apply, Pi.add_apply, ckL_mul _ _ e1, ckL_mul _ _ (fun b => D_wpow n b), hA, hC,
    show n - 1 - 1 = n - 2 by omega]
  simp only [Pi.smul_apply, smulT, smul_eq_C_mul, map_add, map_mul, map_sub, map_natCast, map_one]
  linear_combination ((n : P) * w ^ (n - 1)) * hB b c + (C α * T b c) * hw2 n + (C β * T b c) * hw1 n

/-! The three non-TT seeds. -/

lemma iota_T1 : iota T1 = ![-w ^ 2, ii * w ^ 2, 0] := by
  funext c; fin_cases c <;> simp [iota, T1, Fin.sum_univ_three] <;> iring
lemma dv_T1 : dvL T1 = ![-5 * w, 5 * ii * w, 0] := by
  funext c; fin_cases c <;> simp [dvL_apply, nab, T1, Fin.sum_univ_three, eps, Derivation.leibniz] <;> iring
lemma iota_T2 : iota T2 = ![-2 * u * w ^ 2, 2 * ii * u * w ^ 2, 2 * ii * w ^ 3] := by
  funext c; fin_cases c <;> simp [iota, T2, Fin.sum_univ_three] <;> iring
lemma dv_T2 : dvL T2 = ![-10 * u * w, 10 * ii * u * w, 10 * ii * w ^ 2] := by
  funext c; fin_cases c <;>
    simp [dvL_apply, nab, T2, Fin.sum_univ_three, eps, Derivation.leibniz, Derivation.leibniz_pow] <;> iring
lemma iota_T3 : iota T3 = ![-(u ^ 2 * w ^ 2) - w ^ 4, ii * u ^ 2 * w ^ 2 - ii * w ^ 4, 2 * ii * u * w ^ 3] := by
  funext c; fin_cases c <;> simp [iota, T3, Fin.sum_univ_three] <;> iring
lemma dv_T3 : dvL T3 = ![-5 * u ^ 2 * w - 5 * w ^ 3, 5 * ii * u ^ 2 * w - 5 * ii * w ^ 3, 10 * ii * u * w ^ 2] := by
  funext c; fin_cases c <;>
    simp [dvL_apply, nab, T3, Fin.sum_univ_three, eps, Derivation.leibniz, Derivation.leibniz_pow] <;> iring

@[simp] lemma C_5 : (C 5 : P) = 5 := map_ofNat C 5
@[simp] lemma C_21 : (C 21 : P) = 21 := map_ofNat C 21
@[simp] lemma C_15 : (C 15 : P) = 15 := map_ofNat C 15
@[simp] lemma C_28 : (C 28 : P) = 28 := map_ofNat C 28
@[simp] lemma C_20 : (C 20 : P) = 20 := map_ofNat C 20
@[simp] lemma D_five (a : Fin 3) : D a (5 : P) = 0 := by
  rw [show (5 : P) = C 5 from (map_ofNat C 5).symm]; exact derivation_C _ _
@[simp] lemma D_ten (a : Fin 3) : D a (10 : P) = 0 := by
  rw [show (10 : P) = C 10 from (map_ofNat C 10).symm]; exact derivation_C _ _

macro "ocomp" : tactic => `(tactic| (intro b c; fin_cases b <;> fin_cases c <;>
  simp [symW, ckL_apply, T1, T2, T3, Fin.sum_univ_three, Derivation.leibniz, Derivation.leibniz_pow,
    -mul_eq_zero] <;> iring))

set_option maxHeartbeats 8000000 in
lemma O_T1 (n : ℕ) : Oop (smulT (w ^ n) T1) = ((n : ℂ) * ((n : ℂ) - 1) * (-3) + n * (-21) + (-15)) • smulT (w ^ n) T1 :=
  Oop_wpow T1 (-3) (-21) (-15) (by rw [iota_T1]; ocomp) (by rw [iota_T1, dv_T1]; ocomp)
    (by rw [dv_T1]; ocomp) n
set_option maxHeartbeats 8000000 in
lemma O_T2 (n : ℕ) : Oop (smulT (w ^ n) T2) = ((n : ℂ) * ((n : ℂ) - 1) * (-4) + n * (-28) + (-20)) • smulT (w ^ n) T2 :=
  Oop_wpow T2 (-4) (-28) (-20) (by rw [iota_T2]; ocomp) (by rw [iota_T2, dv_T2]; ocomp)
    (by rw [dv_T2]; ocomp) n
set_option maxHeartbeats 8000000 in
lemma O_T3 (n : ℕ) : Oop (smulT (w ^ n) T3) = ((n : ℂ) * ((n : ℂ) - 1) * (-3) + n * (-21) + (-15)) • smulT (w ^ n) T3 :=
  Oop_wpow T3 (-3) (-21) (-15) (by rw [iota_T3]; ocomp) (by rw [iota_T3, dv_T3]; ocomp)
    (by rw [dv_T3]; ocomp) n

/-- The scalar by which `O` acts on the seed `(N, t)`: `−3(n+1)(n+5)`, `−4(n+1)(n+5)`, `−3(n+1)(n+5)` for
`t = 1, 2, 3` (`n = N − t`), and `0` on the TT seeds `t = 0, 4`. -/
noncomputable def kap (N t : ℕ) : ℂ :=
  (if t = 2 then -4 else if t = 1 ∨ t = 3 then -3 else 0) * (((N - t : ℕ) : ℂ) + 1) * (((N - t : ℕ) : ℂ) + 5)

lemma Oop_seed (N t : ℕ) (htt : t ≤ 4) : Oop (seed N t) = kap N t • seed N t := by
  interval_cases t
  · have := (sU_TT N).2.2.1
    rw [seed_zero, Oop_apply, this, map_zero]; simp [kap]
  · rw [seed, show Tt 1 = T1 from rfl, O_T1]; congr 1; simp [kap]; ring
  · rw [seed, show Tt 2 = T2 from rfl, O_T2]; congr 1; simp [kap]; ring
  · rw [seed, show Tt 3 = T3 from rfl, O_T3]; congr 1; simp [kap]; ring
  · have := (sL_TT (N - 4)).2.2.1
    rw [seed_four, Oop_apply, this, map_zero]; simp [kap]

lemma kap_ne (N t : ℕ) (h1 : 1 ≤ t) (h3 : t ≤ 3) : kap N t ≠ 0 := by
  have e1 : ((N - t : ℕ) : ℂ) + 1 ≠ 0 := by norm_cast
  have e5 : ((N - t : ℕ) : ℂ) + 5 ≠ 0 := by norm_cast
  have : (if t = 2 then (-4 : ℂ) else if t = 1 ∨ t = 3 then -3 else 0) ≠ 0 := by
    interval_cases t <;> norm_num
  exact mul_ne_zero (mul_ne_zero this e1) e5

/-! ## 13. An eigenbasis of `Pd`

For `N ≤ d`, `t ≤ min 4 N`, `p ≤ N + 4 − 2t`, `q ≤ N`: the multiplet members `f_Y^q f_K^p (w^(N−t) T_t)`.
That is `Σ_N (N + 1) Σ_t (N + 5 − 2t) = Σ_N 5 (N + 1)²` vectors (Clebsch–Gordan for `V_{N/2} ⊗ V₂`, by
counting), linearly independent on `S³` (distinct joint eigenvalues), lying in `Pd`, whose dimension is at most
the same number (the reduced monomials). So they are a basis of `Pd`, made of eigenvectors of `∇²`, of `O`,
of both Casimirs and both Cartan elements. -/

/-- The index set of the eigenbasis of `Pd`. -/
abbrev EIdx (d : ℕ) := Σ N : Fin (d + 1), (Σ t : Fin (min 4 (N : ℕ) + 1), Fin (muK N t + 1)) × Fin (N + 1)

def iN {d : ℕ} (i : EIdx d) : ℕ := i.1
def it {d : ℕ} (i : EIdx d) : ℕ := i.2.1.1
def ip {d : ℕ} (i : EIdx d) : ℕ := i.2.1.2
def iq {d : ℕ} (i : EIdx d) : ℕ := i.2.2

lemma iN_le {d : ℕ} (i : EIdx d) : iN i ≤ d := by have := i.1.2; simp only [iN]; omega
lemma it_le {d : ℕ} (i : EIdx d) : it i ≤ 4 ∧ it i ≤ iN i := by
  have := i.2.1.1.2; simp only [it, iN]; omega
lemma ip_le {d : ℕ} (i : EIdx d) : ip i ≤ muK (iN i) (it i) := by have := i.2.1.2.2; simp only [ip, iN, it]; omega
lemma iq_le {d : ℕ} (i : EIdx d) : iq i ≤ iN i := by have := i.2.2.2; simp only [iq, iN]; omega

/-- The basis vectors, on `ℝ⁴` and on `S³`. -/
noncomputable def Et {d : ℕ} (i : EIdx d) : Ten := mem (seed (iN i) (it i)) (ip i) (iq i)
noncomputable def Ev {d : ℕ} (i : EIdx d) : Q := Submodule.Quotient.mk (Et i)

lemma pow_mem_of {O : Module.End ℂ Ten} {S : Submodule ℂ Ten} (h : ∀ x ∈ S, O x ∈ S) (k : ℕ) :
    ∀ x ∈ S, (O ^ k) x ∈ S := by
  induction k with
  | zero => intro x hx; simpa using hx
  | succ k ih => intro x hx; rw [pow_succ', Module.End.mul_apply]; exact h _ (ih x hx)

lemma mem_symTL {s : Ten} {d : ℕ} (hs : s ∈ SymTL d) (p q : ℕ) : mem s p q ∈ SymTL d :=
  pow_mem_of (fun _ hx => good_fY.symTL hx) q _ (pow_mem_of (fun _ hx => good_fK.symTL hx) p _ hs)

lemma Et_symTL {d : ℕ} (i : EIdx d) : Et i ∈ SymTL (iN i) :=
  mem_symTL (seed_symTL _ _ (it_le i).2 (it_le i).1) _ _
lemma Ev_Sd {d : ℕ} (i : EIdx d) : Ev i ∈ Sd (iN i) := ⟨Et i, Et_symTL i, rfl⟩

/-- `∇²` on the basis: `−∇² = λ(N, t)`. -/
lemma lap_Et {d : ℕ} (i : EIdx d) : lap (Et i) = (-lamNt (iN i) (it i)) • Et i := by
  rw [Et, mem_comm lap_K lap_Yk, seed_lap _ _ (it_le i).2 (it_le i).1]
  simp only [mem, map_smul]
lemma CK_Et {d : ℕ} (i : EIdx d) :
    CK (Et i) = (-((muK (iN i) (it i) : ℂ) * (muK (iN i) (it i) + 2))) • Et i := by
  rw [Et, mem_comm CK_K CK_Yk, seed_CK _ _ (it_le i).2 (it_le i).1]
  simp only [mem, map_smul]
lemma O_Et {d : ℕ} (i : EIdx d) : Oop (Et i) = kap (iN i) (it i) • Et i := by
  rw [Et, mem_comm Oop_K Oop_Yk, Oop_seed _ _ (it_le i).1]
  simp only [mem, map_smul]

lemma desc_Ev {O : Module.End ℂ Ten} (hO : Pres O) {d : ℕ} (i : EIdx d) {c : ℂ} (h : O (Et i) = c • Et i) :
    desc O (Ev i) = c • Ev i := by
  rw [Ev, desc_mk hO, h, Submodule.Quotient.mk_smul]

lemma pres_lap : Pres lap := good_lap.pres
lemma pres_CK : Pres CK := Pres.sum fun a => (pres_K a).mul (pres_K a)

lemma Ev_spec {d : ℕ} (i : EIdx d) :
    Ev i ≠ 0 ∧ desc hK (Ev i) = ((muK (iN i) (it i) : ℂ) - 2 * (ip i)) • Ev i ∧
      desc hY (Ev i) = ((iN i : ℂ) - 2 * (iq i)) • Ev i ∧
      desc SJ (Ev i) = (-((iN i : ℂ) * (iN i + 2))) • Ev i :=
  mem_spec (seed_Seed _ _ (it_le i).2 (it_le i).1) (ip_le i) (iq_le i)

/-! ### Independence -/

lemma digit {x x' y y' M : ℤ} (hx : |x - x'| < M) (h : x + M * y = x' + M * y') : y = y' ∧ x = x' := by
  have hM : 0 < M := lt_of_le_of_lt (abs_nonneg _) hx
  have e : M * (y - y') = x' - x := by linarith
  have hy : y = y' := by
    by_contra hne
    rcases lt_or_gt_of_ne hne with hl | hl
    · have : M * (y - y') ≤ -M := by nlinarith
      have := abs_lt.mp hx; linarith
    · have : M * (y - y') ≥ M := by nlinarith
      have := abs_lt.mp hx; linarith
  subst hy; exact ⟨rfl, by linarith⟩

lemma sq2_inj {a b : ℕ} (h : a * (a + 2) = b * (b + 2)) : a = b := by
  rcases lt_trichotomy a b with hl | hl | hl
  · have : a * (a + 2) < b * (b + 2) := Nat.mul_lt_mul'' hl (by omega)
    omega
  · exact hl
  · have : b * (b + 2) < a * (a + 2) := Nat.mul_lt_mul'' hl (by omega)
    omega

open Complex in
/-- The joint eigenvalue used to separate the basis. -/
noncomputable def theta (d N t p q : ℕ) : ℂ :=
  ((muK N t : ℂ) - 2 * p + (2 * d + 10) * (N * (N + 2))) +
    I * ((N : ℂ) - 2 * q + (2 * d + 10) * ((muK N t : ℂ) * (muK N t + 2)))

lemma theta_inj {d N t p q N' t' p' q' : ℕ} (hN : N ≤ d) (hN' : N' ≤ d) (ht : t ≤ 4) (ht' : t' ≤ 4)
    (htN : t ≤ N) (htN' : t' ≤ N') (hp : p ≤ muK N t) (hp' : p' ≤ muK N' t') (hq : q ≤ N) (hq' : q' ≤ N')
    (h : theta d N t p q = theta d N' t' p' q') : N = N' ∧ t = t' ∧ p = p' ∧ q = q' := by
  have hre := congrArg Complex.re h
  have him := congrArg Complex.im h
  simp only [theta, Complex.add_re, Complex.sub_re, Complex.mul_re, Complex.I_re, Complex.I_im,
    Complex.add_im, Complex.sub_im, Complex.mul_im, Complex.natCast_re, Complex.natCast_im, Complex.re_ofNat,
    Complex.im_ofNat] at hre him
  norm_num at hre him
  have hμ : muK N t ≤ d + 4 := by unfold muK; omega
  have hμ' : muK N' t' ≤ d + 4 := by unfold muK; omega
  have r1 : ((muK N t : ℤ) - 2 * p) + (2 * d + 10) * (N * (N + 2)) =
      ((muK N' t' : ℤ) - 2 * p') + (2 * d + 10) * (N' * (N' + 2)) := by
    have : (((muK N t : ℤ) - 2 * p + (2 * d + 10) * (N * (N + 2)) : ℤ) : ℝ) =
        (((muK N' t' : ℤ) - 2 * p' + (2 * d + 10) * (N' * (N' + 2)) : ℤ) : ℝ) := by push_cast; linarith
    exact_mod_cast this
  have r2 : ((N : ℤ) - 2 * q) + (2 * d + 10) * (muK N t * (muK N t + 2)) =
      ((N' : ℤ) - 2 * q') + (2 * d + 10) * (muK N' t' * (muK N' t' + 2)) := by
    have : (((N : ℤ) - 2 * q + (2 * d + 10) * (muK N t * (muK N t + 2)) : ℤ) : ℝ) =
        (((N' : ℤ) - 2 * q' + (2 * d + 10) * (muK N' t' * (muK N' t' + 2)) : ℤ) : ℝ) := by
      push_cast; linarith
    exact_mod_cast this
  obtain ⟨e1, e2⟩ := digit (by rw [abs_lt]; constructor <;> omega) r1
  obtain ⟨e3, e4⟩ := digit (by rw [abs_lt]; constructor <;> omega) r2
  have eN : N = N' := sq2_inj (by exact_mod_cast e1)
  have eμ : muK N t = muK N' t' := sq2_inj (by exact_mod_cast e3)
  subst eN
  have et : t = t' := by unfold muK at eμ; omega
  subst et
  refine ⟨rfl, rfl, by omega, by omega⟩

open Complex in
/-- **The basis vectors are linearly independent on `S³`.** -/
theorem Ev_linIndep (d : ℕ) : LinearIndependent ℂ (fun i : EIdx d => Ev i) := by
  let M : ℂ := 2 * d + 10
  let Θ : Module.End ℂ Q := desc hK - M • desc SJ + I • (desc hY - M • desc CK)
  refine Module.End.eigenvectors_linearIndependent' Θ
    (fun i : EIdx d => theta d (iN i) (it i) (ip i) (iq i)) ?_ _ ?_
  · rintro ⟨⟨N, hN⟩, ⟨⟨t, ht⟩, ⟨p, hp⟩⟩, ⟨q, hq⟩⟩ ⟨⟨N', hN'⟩, ⟨⟨t', ht'⟩, ⟨p', hp'⟩⟩, ⟨q', hq'⟩⟩ h
    simp only [iN, it, ip, iq] at h hp hp' hq hq' ht ht'
    obtain ⟨rfl, rfl, rfl, rfl⟩ := theta_inj (by omega) (by omega) (by omega) (by omega) (by omega) (by omega)
      (by omega) (by omega) (by omega) (by omega) h
    rfl
  · intro i
    obtain ⟨hne, h1, h2, h3⟩ := Ev_spec i
    have h4 := desc_Ev pres_CK i (CK_Et i)
    refine ⟨?_, hne⟩
    rw [Module.End.mem_eigenspace_iff]
    simp only [Θ, LinearMap.add_apply, LinearMap.sub_apply, LinearMap.smul_apply, h1, h2, h3, h4, smul_smul,
      ← sub_smul, ← add_smul, ← smul_add]
    congr 1; simp only [theta, M]; ring

/-! ### Counting -/

lemma card_t (N : ℕ) : Fintype.card (Σ t : Fin (min 4 N + 1), Fin (muK N t + 1)) = 5 * (N + 1) := by
  rw [Fintype.card_sigma]
  simp only [Fintype.card_fin]
  rw [Fin.sum_univ_eq_sum_range (fun t => muK N t + 1) (min 4 N + 1)]
  rcases N with _ | _ | _ | _ | N
  · simp [muK]
  · simp [Finset.sum_range_succ, muK]
  · simp [Finset.sum_range_succ, muK]
  · simp [Finset.sum_range_succ, muK]
  · rw [show min 4 (N + 4) = 4 by omega]
    simp only [Finset.sum_range_succ, Finset.sum_range_zero, muK]; omega

lemma card_EIdx (d : ℕ) : Fintype.card (EIdx d) = Fintype.card (GIdx d) := by
  rw [card_GIdx, Fintype.card_sigma]
  refine Finset.sum_congr rfl fun N _ => ?_
  rw [Fintype.card_prod, card_t, Fintype.card_fin]; ring

/-- **`Pd` is spanned by the eigenbasis.** -/
theorem Sd_eq_span (d : ℕ) : Sd d = Submodule.span ℂ (Set.range (fun i : EIdx d => Ev i)) := by
  have hle : Submodule.span ℂ (Set.range (fun i : EIdx d => Ev i)) ≤ Sd d :=
    Submodule.span_le.mpr (by rintro _ ⟨i, rfl⟩; exact Sd_mono (iN_le i) (Ev_Sd i))
  refine (Submodule.eq_of_le_of_finrank_le hle ?_).symm
  rw [finrank_span_eq_card (Ev_linIndep d), card_EIdx]
  haveI : FiniteDimensional ℂ (Submodule.span ℂ (Set.range (Gv d))) :=
    FiniteDimensional.span_of_finite ℂ (Set.finite_range _)
  exact (Submodule.finrank_mono (Sd_le_span d)).trans (finrank_range_le_card _)

/-- **Item 1, exact dimension** (the harmonic decomposition, counted): `dim Pd = 5 Σ_{N ≤ d} (N + 1)²`. -/
theorem Sd_finrank (d : ℕ) :
    Module.finrank ℂ (Sd d) = ∑ N : Fin (d + 1), ((N : ℕ) + 1) * ((N : ℕ) + 1) * 5 := by
  rw [Sd_eq_span, finrank_span_eq_card (Ev_linIndep d), card_EIdx, card_GIdx]

/-! ### Coefficients in the eigenbasis -/

lemma coeffs_of_eigen {d : ℕ} (F : Module.End ℂ Q) (c : EIdx d → ℂ) (hF : ∀ i, F (Ev i) = c i • Ev i)
    (a : EIdx d → ℂ) (lam : ℂ) (h : F (∑ i, a i • Ev i) = lam • ∑ i, a i • Ev i) :
    ∀ i, a i * (c i - lam) = 0 := by
  have hz : ∑ i, (a i * (c i - lam)) • Ev i = 0 := by
    simp only [map_sum, map_smul, hF, Finset.smul_sum, smul_smul] at h
    simp only [mul_sub, sub_smul, Finset.sum_sub_distrib, h]
    simp only [mul_comm, sub_self]
  exact (Fintype.linearIndependent_iff.mp (Ev_linIndep d)) _ hz

lemma lamNt_re (N t : ℕ) : (lamNt N t).im = 0 ∧ (N : ℝ) - 6 ≤ (lamNt N t).re := by
  simp only [lamNt]
  constructor
  · simp
  · simp only [Complex.sub_re, Complex.div_re, Complex.add_re, Complex.mul_re, Complex.natCast_re,
      Complex.natCast_im, Complex.re_ofNat, Complex.im_ofNat]
    norm_num
    have h1 : (0 : ℝ) ≤ (muK N t : ℝ) * ((muK N t : ℝ) + 2) := by positivity
    have h2 : (N : ℝ) * 2 ≤ (N : ℝ) * ((N : ℝ) + 2) := by nlinarith [(Nat.cast_nonneg N : (0 : ℝ) ≤ N)]
    have : ((N : ℝ) * (N + 2) + (muK N t : ℝ) * (muK N t + 2)) / 2 ≥ N := by linarith
    norm_num at this ⊢; linarith

/-- The explicit degree bound. -/
noncomputable def Dlam (lam : ℂ) : ℕ := ⌈‖lam‖⌉₊ + 6

/-! ### Item 2: the spectrum of `−∇²` on `Pd` -/

/-- **Item 2.** `Pd` has a basis of `−∇²`-eigenvectors, the basis vector `(N, t, p, q)` having eigenvalue
`λ(N, t) = ½(N(N+2) + μ(μ+2)) − 6`, `μ = N + 4 − 2t`; so every eigenvalue of `−∇²` on `Pd` is one of these. -/
theorem lap_spectrum (d : ℕ) :
    LinearIndependent ℂ (fun i : EIdx d => Ev i) ∧
    Sd d = Submodule.span ℂ (Set.range (fun i : EIdx d => Ev i)) ∧
    (∀ i : EIdx d, desc lap (Ev i) = (-lamNt (iN i) (it i)) • Ev i) ∧
    (∀ (lam : ℂ) (v : Q), v ∈ Sd d → v ≠ 0 → desc lap v = (-lam) • v →
      ∃ N t, N ≤ d ∧ t ≤ min 4 N ∧ lam = lamNt N t) := by
  refine ⟨Ev_linIndep d, Sd_eq_span d, fun i => desc_Ev pres_lap i (lap_Et i), ?_⟩
  intro lam v hv hne hl
  rw [Sd_eq_span, Submodule.mem_span_range_iff_exists_fun] at hv
  obtain ⟨a, rfl⟩ := hv
  have hc := coeffs_of_eigen (desc lap) _ (fun i => desc_Ev pres_lap i (lap_Et i)) a (-lam) hl
  by_contra hno
  push_neg at hno
  apply hne
  refine Finset.sum_eq_zero fun i _ => ?_
  have : a i = 0 := by
    rcases mul_eq_zero.mp (hc i) with h | h
    · exact h
    · exfalso
      exact hno (iN i) (it i) (iN_le i) (by have := it_le i; omega) (by linear_combination h)
  rw [this, zero_smul]

/-! ### Item 3: the degree bound -/

/-- **Item 3, the degree bound.** A `−∇²`-eigenvector on `S³` at eigenvalue `λ` which is a symmetric traceless
tensor field with polynomial components (of any degree) already lies in `P_{D(λ)}`, `D(λ) = ⌈|λ|⌉ + 6`:
uniformly in `λ` and in the starting degree `d`. -/
theorem degree_bound (d : ℕ) (lam : ℂ) (v : Q) (hv : v ∈ Sd d) (hl : desc lap v = (-lam) • v) :
    v ∈ Sd (Dlam lam) := by
  rw [Sd_eq_span, Submodule.mem_span_range_iff_exists_fun] at hv
  obtain ⟨a, rfl⟩ := hv
  have hc := coeffs_of_eigen (desc lap) _ (fun i => desc_Ev pres_lap i (lap_Et i)) a (-lam) hl
  refine Submodule.sum_mem _ fun i _ => ?_
  rcases mul_eq_zero.mp (hc i) with h | h
  · rw [h, zero_smul]; exact Submodule.zero_mem _
  · refine Submodule.smul_mem _ _ (Sd_mono ?_ (Ev_Sd i))
    have e : lam = lamNt (iN i) (it i) := by linear_combination h
    obtain ⟨-, hre⟩ := lamNt_re (iN i) (it i)
    have h1 : (lamNt (iN i) (it i)).re ≤ ‖lam‖ := by rw [← e]; exact Complex.re_le_norm lam
    have h2 : ‖lam‖ ≤ (⌈‖lam‖⌉₊ : ℝ) := Nat.le_ceil _
    have : (iN i : ℝ) ≤ (⌈‖lam‖⌉₊ : ℝ) + 6 := by linarith
    unfold Dlam; exact_mod_cast this

/-! ## 14. The TT spectrum, exactly -/

/-- **The TT eigenspace in `Pd`**: classes on `S³` of symmetric traceless tensor fields with components of degree
`≤ d`, whose divergence vanishes on `S³`, with `−∇² = λ` on `S³`. -/
noncomputable def TTQ (d : ℕ) (lam : ℂ) : Submodule ℂ Q where
  carrier := {v | ∃ h ∈ SymTL d, (∀ c, ∀ x ∈ S3, ev x (dvL h c) = 0) ∧
    Submodule.Quotient.mk h = v ∧ desc lap v = (-lam) • v}
  zero_mem' := ⟨0, Submodule.zero_mem _, by simp, by simp, by simp⟩
  add_mem' := by
    rintro _ _ ⟨h, hh, hd, rfl, hl⟩ ⟨k, hk, kd, rfl, kl⟩
    refine ⟨h + k, Submodule.add_mem _ hh hk, fun c x hx => ?_, by simp, ?_⟩
    · rw [map_add, Pi.add_apply, map_add, hd c x hx, kd c x hx, add_zero]
    · rw [map_add, hl, kl, smul_add]
  smul_mem' := by
    rintro r _ ⟨h, hh, hd, rfl, hl⟩
    refine ⟨r • h, Submodule.smul_mem _ r hh, fun c x hx => ?_, by simp, ?_⟩
    · rw [map_smul, Pi.smul_apply, smul_eq_C_mul, map_mul, hd c x hx, mul_zero]
    · rw [map_smul, hl, smul_comm]

lemma TTQ_le (d : ℕ) (lam : ℂ) : TTQ d lam ≤ Sd d := by
  rintro _ ⟨h, hh, -, rfl, -⟩; exact ⟨h, hh, rfl⟩

/-- In the eigenbasis, a TT eigenvector only uses the TT seeds `t ∈ {0, 4}` at eigenvalue `λ`. -/
lemma TTQ_coeffs {d : ℕ} {lam : ℂ} (a : EIdx d → ℂ) (hv : ∑ i, a i • Ev i ∈ TTQ d lam) (i : EIdx d)
    (hi : a i ≠ 0) : (it i = 0 ∨ it i = 4) ∧ lamNt (iN i) (it i) = lam := by
  obtain ⟨h, -, hd, hmk, hl⟩ := hv
  have hO : desc Oop (∑ i, a i • Ev i) = (0 : ℂ) • ∑ i, a i • Ev i := by
    rw [← hmk, Oop_of_dv hd, zero_smul]
  have c1 := coeffs_of_eigen (desc Oop) _ (fun i => desc_Ev pres_O i (O_Et i)) a 0 hO i
  have c2 := coeffs_of_eigen (desc lap) _ (fun i => desc_Ev pres_lap i (lap_Et i)) a (-lam) hl i
  have k0 : kap (iN i) (it i) = 0 := by
    rcases mul_eq_zero.mp c1 with h | h
    · exact absurd h hi
    · simpa using h
  refine ⟨?_, ?_⟩
  · by_contra hne
    have := it_le i
    exact kap_ne (iN i) (it i) (by omega) (by omega) k0
  · rcases mul_eq_zero.mp c2 with h | h
    · exact absurd h hi
    · linear_combination -h

lemma lamNt_zero (N : ℕ) : lamNt N 0 = ((N : ℂ) + 3) ^ 2 - 3 := by
  simp only [lamNt, muK]; push_cast; ring
lemma lamNt_four (N : ℕ) (hN : 4 ≤ N) : lamNt N 4 = ((N : ℂ) - 1) ^ 2 - 3 := by
  simp only [lamNt, muK]
  rw [show N + 4 - 2 * 4 = N - 4 by omega]; push_cast [Nat.cast_sub hN]; ring

lemma sq_cast_inj {a b : ℕ} (h : ((a : ℂ)) ^ 2 - 3 = (b : ℂ) ^ 2 - 3) : a = b := by
  have : ((a ^ 2 : ℕ) : ℂ) = ((b ^ 2 : ℕ) : ℂ) := by push_cast; linear_combination h
  exact Nat.pow_left_injective (by norm_num) (Nat.cast_injective this)

/-- **The TT eigenvalues on `Pd` are exactly the `m² − 3`, `m ≥ 3`** (one direction; the other is
`tt_count`). -/
theorem tt_spectrum (d : ℕ) (lam : ℂ) (hne : TTQ d lam ≠ ⊥) : ∃ m : ℕ, 3 ≤ m ∧ lam = (m : ℂ) ^ 2 - 3 := by
  obtain ⟨v, hv, hv0⟩ := Submodule.exists_mem_ne_zero_of_ne_bot hne
  have hS := TTQ_le d lam hv
  rw [Sd_eq_span, Submodule.mem_span_range_iff_exists_fun] at hS
  obtain ⟨a, rfl⟩ := hS
  obtain ⟨i, hi⟩ : ∃ i, a i ≠ 0 := by
    by_contra hno; push_neg at hno; apply hv0; simp [hno]
  obtain ⟨ht, hl⟩ := TTQ_coeffs a hv i hi
  rcases ht with ht | ht
  · rw [ht, lamNt_zero] at hl
    exact ⟨iN i + 3, by omega, by rw [← hl]; push_cast; ring⟩
  · have h4 : 4 ≤ iN i := by have := it_le i; omega
    rw [ht, lamNt_four _ h4] at hl
    exact ⟨iN i - 1, by omega, by rw [← hl]; push_cast [Nat.cast_sub (by omega : 1 ≤ iN i)]; ring⟩

/-- Campaign 51's eigen-tensors at level `m`, on `S³`. -/
noncomputable def famQ (m : ℕ) (i : Idx (m - 3)) : Q := Submodule.Quotient.mk (fam (m - 3) i)

lemma fam_symTL (N : ℕ) (i : Idx N) : fam N i ∈ SymTL (N + 4) := by
  rcases i with ⟨p, q⟩ | ⟨p, q⟩
  · have := mem_symTL (seed_symTL N 0 (by omega) (by omega)) p q
    exact (show SymTL N ≤ SymTL (N + 4) from fun x ⟨a, b, c⟩ => ⟨a, b, fun i j => (c i j).mono (by omega)⟩) this
  · have := mem_symTL (seed_symTL (N + 4) 4 (by omega) (by omega)) p q
    rw [seed_four, show N + 4 - 4 = N by omega] at this; exact this

lemma famQ_mem (m d : ℕ) (hm : 3 ≤ m) (hd : m + 1 ≤ d) (i : Idx (m - 3)) :
    famQ m i ∈ TTQ d ((m : ℂ) ^ 2 - 3) := by
  have hT := (tt_level_multiplicity_N (m - 3)).1 i
  have e : ((m - 3 : ℕ) : ℂ) + 3 = m := by push_cast [Nat.cast_sub hm]; ring
  rw [e] at hT
  obtain ⟨-, -, hdv, hl⟩ := hT
  have hs := fam_symTL (m - 3) i
  refine ⟨fam (m - 3) i, ⟨hs.1, hs.2.1, fun b c => (hs.2.2 b c).mono (by omega)⟩, ?_, rfl, ?_⟩
  · intro c x _; rw [hdv]; simp
  · rw [famQ, desc_mk pres_lap, hl, Submodule.Quotient.mk_smul]

/-- **Item 4, the exact count.** For `m ≥ 3` and `d ≥ m + 1`, the TT eigenspace of `−∇²` at `m² − 3` in `Pd`
is spanned by campaign 51's eigen-tensors, and has complex dimension exactly `2(m² − 4)`. Uniform in `m`. -/
theorem tt_count (m d : ℕ) (hm : 3 ≤ m) (hd : m + 1 ≤ d) :
    TTQ d ((m : ℂ) ^ 2 - 3) = Submodule.span ℂ (Set.range (famQ m)) ∧
    Module.finrank ℂ (TTQ d ((m : ℂ) ^ 2 - 3)) = 2 * (m ^ 2 - 4) := by
  have hspan : TTQ d ((m : ℂ) ^ 2 - 3) = Submodule.span ℂ (Set.range (famQ m)) := by
    refine le_antisymm ?_ (Submodule.span_le.mpr (by rintro _ ⟨i, rfl⟩; exact famQ_mem m d hm hd i))
    intro v hv
    have hS := TTQ_le _ _ hv
    rw [Sd_eq_span, Submodule.mem_span_range_iff_exists_fun] at hS
    obtain ⟨a, rfl⟩ := hS
    refine Submodule.sum_mem _ fun i _ => ?_
    by_cases hi : a i = 0
    · rw [hi, zero_smul]; exact Submodule.zero_mem _
    refine Submodule.smul_mem _ _ ?_
    obtain ⟨ht, hl⟩ := TTQ_coeffs a hv i hi
    have hp := ip_le i; have hq := iq_le i
    rcases ht with ht | ht
    · rw [ht, lamNt_zero] at hl
      have eN : iN i + 3 = m := sq_cast_inj (by rw [← hl]; push_cast; ring)
      refine Submodule.subset_span ⟨.inl (⟨ip i, by rw [ht] at hp; simp only [muK] at hp; omega⟩,
        ⟨iq i, by omega⟩), ?_⟩
      show Submodule.Quotient.mk (mem (sU (m - 3)) (ip i) (iq i)) =
        Submodule.Quotient.mk (mem (seed (iN i) (it i)) (ip i) (iq i))
      rw [ht, seed_zero, show m - 3 = iN i by omega]
    · have h4 : 4 ≤ iN i := by have := it_le i; omega
      rw [ht, lamNt_four _ h4] at hl
      have eN : iN i - 1 = m := sq_cast_inj (by rw [← hl]; push_cast [Nat.cast_sub (by omega : 1 ≤ iN i)]; ring)
      refine Submodule.subset_span ⟨.inr (⟨ip i, by rw [ht] at hp; simp only [muK] at hp; omega⟩,
        ⟨iq i, by omega⟩), ?_⟩
      show Submodule.Quotient.mk (mem (sL (m - 3)) (ip i) (iq i)) =
        Submodule.Quotient.mk (mem (seed (iN i) (it i)) (ip i) (iq i))
      rw [ht, seed_four, show m - 3 = iN i - 4 by omega]
  refine ⟨hspan, ?_⟩
  have li : LinearIndependent ℂ (famQ m) := (tt_level_multiplicity_N (m - 3)).2.1
  rw [hspan, finrank_span_eq_card li, card_Idx, show m - 3 + 3 = m by omega]

/-! ## 15. Real tensors

Complex conjugation of coefficients, `h ↦ h̄`. It fixes the frame, the connection and every point of `S³`, so it
commutes with `∇²` and the divergence and descends to `S³`. The real tensor fields are its fixed points; the TT
eigenspace is conjugation-stable, so it is the complexification of its real part, and the real dimension is the
complex one. -/

/-- Conjugation of coefficients. -/
noncomputable def cP : P →+* P := MvPolynomial.map (starRingEnd ℂ)

lemma cP_C (c : ℂ) : cP (C c) = C (starRingEnd ℂ c) := map_C _ _
lemma cP_X (i : Fin 4) : cP (X i) = X i := map_X _ _
lemma cP_cP (p : P) : cP (cP p) = p := by
  simp only [cP, MvPolynomial.map_map]
  have : (starRingEnd ℂ).comp (starRingEnd ℂ) = RingHom.id ℂ := by ext z <;> simp
  rw [this, map_id]

lemma ev_cP (x : Fin 4 → ℝ) (p : P) : ev x (cP p) = starRingEnd ℂ (ev x p) := by
  induction p using MvPolynomial.induction_on with
  | C c => simp [cP, ev]
  | add p q hp hq => simp [hp, hq]
  | mul_X p i hp =>
    rw [map_mul, map_mul, map_mul, hp, cP_X, map_mul]; simp [ev]

lemma cP_dval (a : Fin 3) (i : Fin 4) : cP (dval a i) = dval a i := by
  fin_cases a <;> fin_cases i <;> simp [dval, cP_X]

lemma cP_D (a : Fin 3) (p : P) : cP (D a p) = D a (cP p) := by
  induction p using MvPolynomial.induction_on with
  | C c => simp [cP_C, derivation_C]
  | add p q hp hq => simp [hp, hq]
  | mul_X p i hp =>
    simp only [Derivation.leibniz, smul_eq_mul, map_add, map_mul, D_X, cP_X, cP_dval, hp]

lemma conj_eps (a b c : Fin 3) : starRingEnd ℂ (eps a b c) = eps a b c := by
  fin_cases a <;> fin_cases b <;> fin_cases c <;> simp [eps]

/-- Conjugation on tensor fields, as a conjugate-linear map. -/
noncomputable def cT : Ten →ₛₗ[starRingEnd ℂ] Ten where
  toFun h := fun b c => cP (h b c)
  map_add' h k := by funext b c; simp
  map_smul' r h := by funext b c; simp [smul_eq_C_mul, cP_C]

lemma cT_apply (h : Ten) (b c : Fin 3) : cT h b c = cP (h b c) := rfl

@[simp] lemma conj_two : starRingEnd ℂ 2 = 2 := map_ofNat _ 2
@[simp] lemma conj_three : starRingEnd ℂ 3 = 3 := map_ofNat _ 3

/-- Operators commuting with conjugation. -/
def CR (O : Module.End ℂ Ten) : Prop := ∀ h, cT (O h) = O (cT h)

lemma CR.add {O O' : Module.End ℂ Ten} (h1 : CR O) (h2 : CR O') : CR (O + O') :=
  fun h => by simp [h1 h, h2 h]
lemma CR.mul {O O' : Module.End ℂ Ten} (h1 : CR O) (h2 : CR O') : CR (O * O') :=
  fun h => by simp only [Module.End.mul_apply]; rw [h1, h2]
lemma CR.sum {O : Fin 3 → Module.End ℂ Ten} (h : ∀ a, CR (O a)) : CR (∑ a, O a) := by
  simp only [Fin.sum_univ_three]; exact ((h 0).add (h 1)).add (h 2)

lemma cr_D (a : Fin 3) : CR (DtL (D a)) := fun h => by funext b c; simp [cT_apply, cP_D]
lemma cr_L (a : Fin 3) : CR (Lt a) := fun h => by
  funext b c; simp [cT_apply, Lt_apply, map_sum, cP_C, conj_eps]
lemma cr_nab (a : Fin 3) : CR (nab a) := (cr_D a).add (cr_L a)
lemma cr_lap : CR lap := CR.sum fun a => (cr_nab a).mul (cr_nab a)

lemma cT_dv (h : Ten) (c : Fin 3) : cP (dvL h c) = dvL (cT h) c := by
  simp only [dvL_apply, map_sum]
  refine Finset.sum_congr rfl fun b _ => ?_
  rw [← cT_apply, cr_nab]

lemma cT_symTL {d : ℕ} {h : Ten} (hh : h ∈ SymTL d) : cT h ∈ SymTL d := by
  obtain ⟨hs, ht, hd⟩ := hh
  refine ⟨fun b c => by simp [cT_apply, hs b c], ?_, fun b c => ⟨?_⟩⟩
  · simp only [trL_apply] at ht ⊢; simp only [cT_apply, ← map_sum, ht, map_zero]
  · exact (Finset.sup_mono (support_map_subset _ _)).trans (hd b c).le

lemma cT_Z {h : Ten} (hh : h ∈ Z) : cT h ∈ Z := fun b c x hx => by
  rw [cT_apply, ev_cP, hh b c x hx, map_zero]

/-- Conjugation on `S³` tensor fields. -/
noncomputable def cQ : Q →ₛₗ[starRingEnd ℂ] Q := Z.mapQ Z cT (fun _ hh => cT_Z hh)

lemma cQ_mk (h : Ten) : cQ (Submodule.Quotient.mk h) = Submodule.Quotient.mk (cT h) := rfl

lemma cQ_cQ (v : Q) : cQ (cQ v) = v := by
  induction v using Submodule.Quotient.induction_on with
  | H h => rw [cQ_mk, cQ_mk]; congr 1; funext b c; simp [cT_apply, cP_cP]

lemma cQ_lap (v : Q) : cQ (desc lap v) = desc lap (cQ v) := by
  induction v using Submodule.Quotient.induction_on with
  | H h => rw [desc_mk pres_lap, cQ_mk, cQ_mk, desc_mk pres_lap, cr_lap]

/-- For real `λ`, the TT eigenspace is conjugation-stable. -/
lemma cQ_TTQ {d : ℕ} {lam : ℂ} (hlam : starRingEnd ℂ lam = lam) {v : Q} (hv : v ∈ TTQ d lam) :
    cQ v ∈ TTQ d lam := by
  obtain ⟨h, hh, hd, rfl, hl⟩ := hv
  refine ⟨cT h, cT_symTL hh, fun c x hx => ?_, rfl, ?_⟩
  · rw [← cT_dv, ev_cP, hd c x hx, map_zero]
  · rw [← cQ_lap, hl, map_smulₛₗ, map_neg, hlam]

/-- **The real TT eigenspace**: the conjugation-fixed (real-coefficient) part of the TT eigenspace, as a real
vector space. -/
noncomputable def TTR (d : ℕ) (lam : ℂ) : Submodule ℝ Q where
  carrier := {v | v ∈ TTQ d lam ∧ cQ v = v}
  zero_mem' := ⟨Submodule.zero_mem _, map_zero _⟩
  add_mem' := by
    rintro v v' ⟨h1, h2⟩ ⟨h1', h2'⟩; exact ⟨Submodule.add_mem _ h1 h1', by rw [map_add, h2, h2']⟩
  smul_mem' := by
    rintro r v ⟨h1, h2⟩
    refine ⟨?_, ?_⟩
    · rw [← Complex.coe_smul]; exact Submodule.smul_mem _ _ h1
    · rw [← Complex.coe_smul, map_smulₛₗ, h2, Complex.conj_ofReal]

/-- A real TT class has a real-coefficient representative. -/
lemma TTR_real_rep {d : ℕ} {lam : ℂ} {v : Q} (hv : v ∈ TTR d lam) :
    ∃ h : Ten, cT h = h ∧ (Submodule.Quotient.mk h : Q) = v := by
  obtain ⟨⟨h, -, -, rfl, -⟩, hc⟩ := hv
  refine ⟨(1 / 2 : ℂ) • (h + cT h), ?_, ?_⟩
  · rw [map_smulₛₗ, map_add]
    funext b c; simp [cT_apply, cP_cP, add_comm]
  · rw [Submodule.Quotient.mk_smul, Submodule.Quotient.mk_add, ← cQ_mk, hc]
    rw [← two_smul ℂ (Submodule.Quotient.mk h : Q), smul_smul]; norm_num

open Complex in
/-- **The real dimension equals the complex one**, for real `λ`. -/
theorem finrank_TTR {d : ℕ} {lam : ℂ} (hlam : starRingEnd ℂ lam = lam) :
    Module.finrank ℝ (TTR d lam) = Module.finrank ℂ (TTQ d lam) := by
  let W := TTQ d lam
  let Φ : (TTR d lam × TTR d lam) →ₗ[ℝ] W :=
    { toFun := fun x => ⟨x.1.1 + I • x.2.1, Submodule.add_mem _ x.1.2.1 (Submodule.smul_mem _ _ x.2.2.1)⟩
      map_add' := fun x y => by
        ext; simp only [Prod.fst_add, Prod.snd_add, Submodule.coe_add, smul_add]; abel
      map_smul' := fun r x => by
        apply Subtype.ext
        show (r • x.1 : TTR d lam).1 + I • (r • x.2 : TTR d lam).1 = r • (x.1.1 + I • x.2.1)
        simp only [SetLike.val_smul, smul_add]
        rw [← Complex.coe_smul, ← Complex.coe_smul, ← Complex.coe_smul, smul_smul, smul_smul, mul_comm] }
  have hinj : Function.Injective Φ := by
    rw [← LinearMap.ker_eq_bot, LinearMap.ker_eq_bot']
    rintro ⟨⟨a, ha⟩, ⟨b, hb⟩⟩ h0
    have h1 : a + I • b = 0 := congrArg Subtype.val h0
    have h2 : a - I • b = 0 := by
      have := congrArg cQ h1
      rw [map_add, map_smulₛₗ, ha.2, hb.2, Complex.conj_I, map_zero, neg_smul] at this
      rw [sub_eq_add_neg]; exact this
    have ea : (2 : ℂ) • a = 0 := by
      rw [two_smul]
      calc a + a = (a + I • b) + (a - I • b) := by abel
        _ = 0 := by rw [h1, h2, add_zero]
    have eb : (2 * I) • b = 0 := by
      rw [mul_smul, two_smul]
      calc I • b + I • b = (a + I • b) - (a - I • b) := by abel
        _ = 0 := by rw [h1, h2, sub_zero]
    have a0 : a = 0 := (smul_eq_zero.mp ea).resolve_left two_ne_zero
    have b0 : b = 0 := (smul_eq_zero.mp eb).resolve_left (mul_ne_zero two_ne_zero I_ne_zero)
    simp [a0, b0]
  have hsurj : Function.Surjective Φ := by
    rintro ⟨v, hv⟩
    have hcv := cQ_TTQ hlam hv
    refine ⟨(⟨(1 / 2 : ℂ) • (v + cQ v), Submodule.smul_mem _ _ (Submodule.add_mem _ hv hcv), ?_⟩,
      ⟨(-I / 2) • (v - cQ v), Submodule.smul_mem _ _ (Submodule.sub_mem _ hv hcv), ?_⟩), ?_⟩
    · rw [map_smulₛₗ, map_add, cQ_cQ]; simp [add_comm]
    · rw [map_smulₛₗ, map_sub, cQ_cQ]
      simp only [map_div₀, map_neg, Complex.conj_I, map_ofNat]
      rw [show (-(-I) / 2 : ℂ) = -(-I / 2) by ring, neg_smul, ← smul_neg, neg_sub]
    · ext
      simp only [Φ, LinearMap.coe_mk, AddHom.coe_mk, smul_smul, smul_sub, smul_add]
      rw [show I * (-I / 2) = (1 / 2 : ℂ) by rw [mul_div_assoc', mul_neg, I_mul_I]; norm_num]
      rw [← sub_eq_zero]
      have : (1 / 2 : ℂ) • v + (1 / 2 : ℂ) • cQ v + ((1 / 2 : ℂ) • v - (1 / 2 : ℂ) • cQ v) - v
          = ((1 / 2 : ℂ) + 1 / 2 - 1) • v := by module
      rw [this]; norm_num
  let e := LinearEquiv.ofBijective Φ ⟨hinj, hsurj⟩
  haveI : FiniteDimensional ℂ W := Submodule.finiteDimensional_of_le (TTQ_le d lam)
  haveI : Module.Finite ℝ W := FiniteDimensional.complexToReal W
  haveI : Module.Finite ℝ (TTR d lam × TTR d lam) := Module.Finite.equiv e.symm
  haveI : Module.Finite ℝ (TTR d lam) :=
    Module.Finite.of_surjective (LinearMap.fst ℝ (TTR d lam) (TTR d lam)) LinearMap.fst_surjective
  have h1 := e.finrank_eq
  rw [Module.finrank_prod] at h1
  have h2 := finrank_real_of_complex W
  change _ = Module.finrank ℂ W
  omega

/-- **Item 4, over `ℝ`.** For `m ≥ 3` and `d ≥ m + 1`, the real TT eigenspace at `m² − 3` (real-coefficient
symmetric traceless fields on `S³`) has real dimension exactly `2(m² − 4)`. -/
theorem tt_count_real (m d : ℕ) (hm : 3 ≤ m) (hd : m + 1 ≤ d) :
    Module.finrank ℝ (TTR d ((m : ℂ) ^ 2 - 3)) = 2 * (m ^ 2 - 4) := by
  rw [finrank_TTR (by simp [map_sub, map_pow, map_natCast]), (tt_count m d hm hd).2]

end ShadowProbe.S3PolySpectrum

#print axioms ShadowProbe.S3PolySpectrum.frame_bracket
#print axioms ShadowProbe.S3PolySpectrum.lap_K
#print axioms ShadowProbe.S3PolySpectrum.K_TT
#print axioms ShadowProbe.S3PolySpectrum.TU_lap
#print axioms ShadowProbe.S3PolySpectrum.TL_lap
#print axioms ShadowProbe.S3PolySpectrum.seed_TT
#print axioms ShadowProbe.S3PolySpectrum.sU_TT
#print axioms ShadowProbe.S3PolySpectrum.sL_TT
#print axioms ShadowProbe.S3PolySpectrum.tangent
#print axioms ShadowProbe.S3PolySpectrum.mem_spec
#print axioms ShadowProbe.S3PolySpectrum.tt_level_multiplicity_N
#print axioms ShadowProbe.S3PolySpectrum.tt_level_multiplicity
#print axioms ShadowProbe.S3PolySpectrum.tt_m345
#print axioms ShadowProbe.S3PolySpectrum.Sd_invariant
#print axioms ShadowProbe.S3PolySpectrum.Sd_finrank_le
#print axioms ShadowProbe.S3PolySpectrum.Sd_finrank
#print axioms ShadowProbe.S3PolySpectrum.lap_casimir
#print axioms ShadowProbe.S3PolySpectrum.SJ_eq_CY
#print axioms ShadowProbe.S3PolySpectrum.neg_lap_casimir
#print axioms ShadowProbe.S3PolySpectrum.CK_prim
#print axioms ShadowProbe.S3PolySpectrum.Oop_wpow
#print axioms ShadowProbe.S3PolySpectrum.Oop_seed
#print axioms ShadowProbe.S3PolySpectrum.Ev_linIndep
#print axioms ShadowProbe.S3PolySpectrum.Sd_eq_span
#print axioms ShadowProbe.S3PolySpectrum.lap_spectrum
#print axioms ShadowProbe.S3PolySpectrum.degree_bound
#print axioms ShadowProbe.S3PolySpectrum.tt_spectrum
#print axioms ShadowProbe.S3PolySpectrum.tt_count
#print axioms ShadowProbe.S3PolySpectrum.finrank_TTR
#print axioms ShadowProbe.S3PolySpectrum.tt_count_real

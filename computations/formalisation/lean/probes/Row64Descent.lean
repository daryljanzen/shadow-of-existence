import ShadowEngine
import Mathlib.NumberTheory.Harmonic.EulerMascheroni
import Mathlib.LinearAlgebra.Matrix.Rank

/-! # Campaign 35 (`r7443+71.15`): row 64, the descent is free at the order the section works at

The receipt is `P10_the_descent_is_free_at_the_order_the_section_works_at_and_the_kernel_rotates_rather_than_failing.py`.
Its computed checks are sections A–D; each is built here as the receipt computes it. Ranks are `Matrix.rank`, proved by
an exhibited factorisation `V = E * C` through `k` columns (rank `≤ k`) and an exhibited nonzero `k × k` minor (rank
`≥ k`), see `rank_eq_of_factor`. Kernels are exhibited as one-parameter families, `x ∈ ker ↔ ∃ t, x = t • v`. Limits
are `Filter.Tendsto`.

**Imported, not derived (labelled again at each declaration):**
- the forms of the three convention directions `f₁ = q₆(64Λ³ + 48εΛ²ν/a⁴)`, `f₂ = q₄Λ²`, `f₃ = L/a⁴` (`fs`);
- the TT label weights `d(m) = 2(m² − 4)`, `μ(m) = √(m² − 1)` (`wTT`);
- the closed-FRW (`k = 1`) curvature formulas in the receipt's typed form, in terms of `ä/a`, `H²` and `a`:
  `R = 6(ä/a + H² + 1/a²)`, `λ₀ = 3ä/a`, `λ₁ = ä/a + 2H² + 2/a²`, `Ric² = λ₀² + 3λ₁²`,
  `Riem² = 12((ä/a)² + (H² + 1/a²)²)`, `tr Ric³ = λ₀³ + 3λ₁³` (`frwR` … `frwRic3`). They are NOT tied to the engine's
  connection here; the derivatives they are fed (of `α cosh(T/α)`, and the Friedmann `ä/a = aF′/2 + F` with `F′`)
  ARE derived, by `HasDerivAt`.
- the deformation `F = H² = Λ/3 + εu/3 − 1/a²`, `u = (1 + ν log a)/a⁴` itself (the receipt's model of the anomaly).

The receipt's paper-text check (`pf.inline R=(4\Lambda)`) is not formalised; the value `4Λ` it parses is proved here. -/

namespace ShadowProbe

namespace R64Descent

open Matrix Filter Topology

/-! ### The rank tool -/

/-- A matrix that factors through `k` columns and has a nonzero `k × k` minor has rank exactly `k`. -/
theorem rank_eq_of_factor {m n k : ℕ} (V : Matrix (Fin m) (Fin n) ℝ) (E : Matrix (Fin m) (Fin k) ℝ)
    (C : Matrix (Fin k) (Fin n) ℝ) (hVEC : V = E * C) (r : Fin k → Fin m) (c : Fin k → Fin n)
    (hminor : (V.submatrix r c).det ≠ 0) : V.rank = k := by
  apply le_antisymm
  · rw [hVEC]; exact (Matrix.rank_mul_le_right E C).trans (Matrix.rank_le_height C)
  · have h := Matrix.rank_of_det_ne_zero hminor
    rw [Fintype.card_fin] at h
    rw [← h]; exact Matrix.rank_submatrix_le V r c

/-! ### A. One object, not three -/

section A

variable (q6 q4 Λ ε ν L : ℝ)

/-- **Imported:** the three convention directions, first order in the back-reaction. -/
noncomputable def fs : Fin 3 → ℝ → ℝ :=
  ![fun a => q6 * (64 * Λ ^ 3 + 48 * ε * Λ ^ 2 * ν / a ^ 4), fun _ => q4 * Λ ^ 2, fun a => L / a ^ 4]

/-- the coefficient matrix of `fs` in the basis `(1, a⁻⁴)` (the receipt's `Mk` / `ns_fun` matrix) -/
noncomputable def Mk : Matrix (Fin 2) (Fin 3) ℝ :=
  !![64 * q6 * Λ ^ 3, q4 * Λ ^ 2, 0; 48 * ε * Λ ^ 2 * ν * q6, 0, L]

theorem fs_decomp (j : Fin 3) (a : ℝ) :
    fs q6 q4 Λ ε ν L j a = Mk q6 q4 Λ ε ν L 0 j + Mk q6 q4 Λ ε ν L 1 j * (a ^ 4)⁻¹ := by
  fin_cases j <;> simp [fs, Mk] <;> ring

/-- the four-point and the one-point spectrum -/
noncomputable def spec4 : Fin 4 → ℝ := ![1, 3 / 2, 2, 5 / 2]
noncomputable def spec1 : Fin 1 → ℝ := ![2]

/-- a function of one operator IS the diagonal matrix of its values on the spectrum: the value matrix -/
noncomputable def Vmat {n : ℕ} (spec : Fin n → ℝ) : Matrix (Fin n) (Fin 3) ℝ :=
  Matrix.of fun i j => fs q6 q4 Λ ε ν L j (spec i)

/-- the evaluation of the basis `(1, a⁻⁴)` on a spectrum -/
noncomputable def Emat {n : ℕ} (spec : Fin n → ℝ) : Matrix (Fin n) (Fin 2) ℝ :=
  Matrix.of fun i k => ![1, (spec i ^ 4)⁻¹] k

theorem Vmat_factor {n : ℕ} (spec : Fin n → ℝ) :
    Vmat q6 q4 Λ ε ν L spec = Emat spec * Mk q6 q4 Λ ε ν L := by
  ext i j
  rw [Matrix.mul_apply, Fin.sum_univ_two]
  simp only [Vmat, Emat, Matrix.of_apply, fs_decomp]
  simp; ring

/-- the kernel vector, normalised to third entry `1` -/
noncomputable def kv : Fin 3 → ℝ :=
  ![-L / (48 * Λ ^ 2 * ε * ν * q6), 4 * L / (3 * Λ * ε * ν * q4), 1]

variable {q6 q4 Λ ε ν L}
variable (hq6 : 0 < q6) (hq4 : 0 < q4) (hΛ : 0 < Λ) (hε : 0 < ε) (hν : 0 < ν) (hL : 0 < L)

include hq6 hq4 hΛ hε hν hL

omit hq6 hε hν in
/-- ⛭ **`rank_A`.** The three directions have rank `2` on the four-point spectrum and `1` on the one-point one. -/
theorem rank_A : (Vmat q6 q4 Λ ε ν L spec4).rank = 2 ∧ (Vmat q6 q4 Λ ε ν L spec1).rank = 1 := by
  constructor
  · refine rank_eq_of_factor _ _ _ (Vmat_factor q6 q4 Λ ε ν L spec4) ![0, 2] ![1, 2] ?_
    rw [Matrix.det_fin_two]
    simp [Vmat, fs, spec4]
    intro h
    have : q4 * Λ ^ 2 * L * (15 / 16) = 0 := by linarith
    have : q4 * Λ ^ 2 * L * (15 / 16) ≠ 0 := by positivity
    contradiction
  · refine rank_eq_of_factor _ 1 _ (Matrix.one_mul _).symm id ![1] ?_
    simp [Vmat, fs, spec1]
    exact ⟨hq4.ne', hΛ.ne'⟩

/-- ⛭ **`kernel_A`.** The coefficient kernel (`ns_fun`) is exactly the line through `kv`, the value kernel on the
four-point spectrum (`ns_many`) is the same line — the operator reading and the value reading are one object — and
`kv`'s third entry is nonzero. -/
theorem kernel_A :
    (∀ x : Fin 3 → ℝ, Mk q6 q4 Λ ε ν L *ᵥ x = 0 ↔ ∃ t : ℝ, x = t • kv q6 q4 Λ ε ν L) ∧
    (∀ x : Fin 3 → ℝ, Vmat q6 q4 Λ ε ν L spec4 *ᵥ x = 0 ↔ Mk q6 q4 Λ ε ν L *ᵥ x = 0) ∧
    kv q6 q4 Λ ε ν L 2 ≠ 0 := by
  refine ⟨fun x => ?_, fun x => ?_, by simp [kv]⟩
  · constructor
    · intro h
      have h0 := congrFun h 0
      have h1 := congrFun h 1
      simp [Mk, Matrix.mulVec, dotProduct, Fin.sum_univ_three] at h0 h1
      refine ⟨x 2, ?_⟩
      funext i
      fin_cases i
      · simp [kv]; field_simp; linear_combination h1
      · have hk : (3 * Λ * ε * ν * q4) * (4 * L / (3 * Λ * ε * ν * q4)) = 4 * L := by field_simp
        have hc : (3 * Λ ^ 2 * ε * ν * q4) ≠ 0 := by positivity
        simp only [kv]
        simp
        apply mul_left_cancel₀ hc
        linear_combination 3 * ε * ν * h0 - 4 * Λ * h1 - Λ * x 2 * hk
      · simp [kv]
    · rintro ⟨t, rfl⟩
      funext i
      fin_cases i <;> simp [Mk, kv, Matrix.mulVec, dotProduct, Fin.sum_univ_three] <;> field_simp <;> ring
  · rw [Vmat_factor, ← Matrix.mulVec_mulVec]
    generalize Mk q6 q4 Λ ε ν L *ᵥ x = y
    constructor
    · intro h
      have h0 := congrFun h 0
      have h2 := congrFun h 2
      simp [Emat, spec4, Matrix.mulVec, dotProduct, Fin.sum_univ_two] at h0 h2
      norm_num at h2
      funext k
      fin_cases k
      · simp; linarith
      · simp; linarith
    · intro h; rw [h]; simp

end A

/-! ### A(b). The expectation of a function of the operator sees no phase; a non-commuting control does -/

/-- `ψ = (c₁, c₂ e^{iθ})` -/
noncomputable def psi (c1 c2 θ : ℝ) : Fin 2 → ℂ := ![(c1 : ℂ), (c2 : ℂ) * Complex.exp (θ * Complex.I)]

/-- `⟨ψ|A|ψ⟩` -/
noncomputable def expect (A : Matrix (Fin 2) (Fin 2) ℂ) (v : Fin 2 → ℂ) : ℂ := star v ⬝ᵥ (A *ᵥ v)

theorem psi_one (c2 θ : ℝ) : (c2 : ℂ) * Complex.exp (θ * Complex.I) = ⟨c2 * Real.cos θ, c2 * Real.sin θ⟩ := by
  apply Complex.ext <;> simp [Complex.exp_ofReal_mul_I_re, Complex.exp_ofReal_mul_I_im]

/-- ⛭ **`phase_A`.** `⟨ψ|diag(1,4)|ψ⟩ = c₁² + 4c₂²` for every phase (so its phase derivative is `0`), while
`⟨ψ|σₓ|ψ⟩ = 2c₁c₂ cos θ`, whose phase derivative `−2c₁c₂ sin θ` is nonzero at `θ = π/2` when `c₁c₂ ≠ 0`. -/
theorem phase_A (c1 c2 : ℝ) :
    (∀ θ : ℝ, expect (Matrix.diagonal ![1, 4]) (psi c1 c2 θ) = (c1 ^ 2 + 4 * c2 ^ 2 : ℝ)) ∧
    (∀ θ : ℝ, HasDerivAt (fun θ => expect (Matrix.diagonal ![1, 4]) (psi c1 c2 θ)) 0 θ) ∧
    (∀ θ : ℝ, expect !![0, 1; 1, 0] (psi c1 c2 θ) = (2 * c1 * c2 * Real.cos θ : ℝ)) ∧
    (∀ θ : ℝ, HasDerivAt (fun θ => (expect !![0, 1; 1, 0] (psi c1 c2 θ)).re) (-(2 * c1 * c2 * Real.sin θ)) θ) ∧
    (c1 * c2 ≠ 0 → -(2 * c1 * c2 * Real.sin (Real.pi / 2)) ≠ 0) := by
  have hA : ∀ θ : ℝ, expect (Matrix.diagonal ![1, 4]) (psi c1 c2 θ) = (c1 ^ 2 + 4 * c2 ^ 2 : ℝ) := by
    intro θ
    simp only [expect, psi, psi_one]
    apply Complex.ext <;>
      simp [dotProduct, Matrix.mulVec, Fin.sum_univ_two, Matrix.diagonal, sq] <;>
      first | ring1 | linear_combination (4 * c2 ^ 2) * Real.sin_sq_add_cos_sq θ
  have hB : ∀ θ : ℝ, expect !![0, 1; 1, 0] (psi c1 c2 θ) = (2 * c1 * c2 * Real.cos θ : ℝ) := by
    intro θ
    simp only [expect, psi, psi_one]
    apply Complex.ext <;> simp [dotProduct, Matrix.mulVec, Fin.sum_univ_two, Complex.cos_ofReal_re] <;> ring
  refine ⟨hA, fun θ => ?_, hB, fun θ => ?_, fun h => ?_⟩
  · have : (fun θ => expect (Matrix.diagonal ![1, 4]) (psi c1 c2 θ)) = fun _ => ((c1 ^ 2 + 4 * c2 ^ 2 : ℝ) : ℂ) :=
      funext hA
    rw [this]; exact hasDerivAt_const _ _
  · have : (fun θ => (expect !![0, 1; 1, 0] (psi c1 c2 θ)).re) = fun θ => 2 * c1 * c2 * Real.cos θ := by
      funext θ; rw [hB]; simp [Complex.cos_ofReal_re]
    rw [this]
    simpa using (Real.hasDerivAt_cos θ).const_mul (2 * c1 * c2)
  · simp only [Real.sin_pi_div_two, mul_one, neg_ne_zero]
    intro h2; apply h; linarith

/-! ### B. The descent on the deformation the theory makes -/

section B

/-- **Imported (the receipt's typed closed-FRW formulas)**, in terms of `add = ä/a`, `H2 = H²` and the scale factor. -/
noncomputable def frwR (add H2 a : ℝ) : ℝ := 6 * (add + H2 + 1 / a ^ 2)
noncomputable def frwL0 (add : ℝ) : ℝ := 3 * add
noncomputable def frwL1 (add H2 a : ℝ) : ℝ := add + 2 * H2 + 2 / a ^ 2
noncomputable def frwRic2 (add H2 a : ℝ) : ℝ := frwL0 add ^ 2 + 3 * frwL1 add H2 a ^ 2
noncomputable def frwRiem2 (add H2 a : ℝ) : ℝ := 12 * (add ^ 2 + (H2 + 1 / a ^ 2) ^ 2)
noncomputable def frwRic3 (add H2 a : ℝ) : ℝ := frwL0 add ^ 3 + 3 * frwL1 add H2 a ^ 3

/-- the four dimension-six invariants `R³, R·Ric², R·Riem², tr Ric³` -/
noncomputable def inv6 (add H2 a : ℝ) : Fin 4 → ℝ :=
  ![frwR add H2 a ^ 3, frwR add H2 a * frwRic2 add H2 a, frwR add H2 a * frwRiem2 add H2 a, frwRic3 add H2 a]

/-- the substrate member `a(T) = α cosh(T/α)`, with `ä/a` and `H²` built from its DERIVED derivatives -/
noncomputable def aCosh (α T : ℝ) : ℝ := α * Real.cosh (T / α)
noncomputable def addM (α T : ℝ) : ℝ := Real.cosh (T / α) / α / aCosh α T
noncomputable def H2M (α T : ℝ) : ℝ := (Real.sinh (T / α) / aCosh α T) ^ 2

/-- ⛭ **`substrate`.** `ȧ = sinh(T/α)`, `ä = cosh(T/α)/α`, and fed into the typed formulas they give, with
`Λ = 3/α²`: `R = 4Λ`, `Ric² = 4Λ²`, `Riem² = 8Λ²/3`, `λ₀ = λ₁ = Λ`. -/
theorem substrate (α : ℝ) (hα : 0 < α) (T : ℝ) :
    HasDerivAt (aCosh α) (Real.sinh (T / α)) T ∧
    HasDerivAt (fun T => Real.sinh (T / α)) (Real.cosh (T / α) / α) T ∧
    frwR (addM α T) (H2M α T) (aCosh α T) = 4 * (3 / α ^ 2) ∧
    frwRic2 (addM α T) (H2M α T) (aCosh α T) = 4 * (3 / α ^ 2) ^ 2 ∧
    frwRiem2 (addM α T) (H2M α T) (aCosh α T) = 8 * (3 / α ^ 2) ^ 2 / 3 ∧
    frwL0 (addM α T) = 3 / α ^ 2 ∧ frwL1 (addM α T) (H2M α T) (aCosh α T) = 3 / α ^ 2 := by
  have hd : HasDerivAt (fun T : ℝ => T / α) (1 / α) T := (hasDerivAt_id T).div_const α
  have hc := Real.cosh_pos (T / α)
  have hadd : addM α T = 1 / α ^ 2 := by
    simp only [addM, aCosh]; field_simp
  have hH2 : H2M α T = 1 / α ^ 2 - 1 / aCosh α T ^ 2 := by
    simp only [H2M, aCosh]; field_simp; linear_combination (-1) * Real.cosh_sq (T / α)
  refine ⟨?_, ?_, ?_⟩
  · have := ((Real.hasDerivAt_cosh (T / α)).comp T hd).const_mul α
    convert this using 1
    · funext y; simp [aCosh]
    · field_simp
  · have := (Real.hasDerivAt_sinh (T / α)).comp T hd
    convert this using 1
    · rfl
    · ring
  · simp only [frwR, frwRic2, frwRiem2, frwL0, frwL1, hadd, hH2]
    refine ⟨by ring, by ring, by ring, by ring, by ring⟩

/-- **Imported (the receipt's model):** the deformation `F = H² = Λ/3 + εu/3 − 1/a²`, `u = (1 + ν log a)/a⁴`. -/
noncomputable def Fd (Λ ε ν a : ℝ) : ℝ := Λ / 3 + ε * ((1 + ν * Real.log a) / a ^ 4) / 3 - 1 / a ^ 2
noncomputable def Fd' (ε ν a : ℝ) : ℝ := ε * (ν - 4 - 4 * ν * Real.log a) / (3 * a ^ 5) + 2 / a ^ 3

theorem Fd_deriv (Λ ε ν : ℝ) {a : ℝ} (ha : 0 < a) : HasDerivAt (Fd Λ ε ν) (Fd' ε ν a) a := by
  have h := (((((((Real.hasDerivAt_log ha.ne').const_mul ν).const_add 1).div (hasDerivAt_pow 4 a)
    (by positivity)).const_mul ε).div_const 3).const_add (Λ / 3)).sub ((hasDerivAt_pow 2 a).inv (by positivity))
  convert h using 1
  · funext x; simp only [Fd, Pi.sub_apply, Pi.div_apply, Pi.inv_apply]; ring
  · simp only [Fd']; norm_num; field_simp; ring

/-- `ä/a = aF′/2 + F` (the receipt's `add`), with `F′` the derived derivative -/
noncomputable def addD (Λ ε ν a : ℝ) : ℝ := a * Fd' ε ν a / 2 + Fd Λ ε ν a
noncomputable def Sa (ν a : ℝ) : ℝ := ν / (6 * a ^ 4)
noncomputable def Aa (ν a : ℝ) : ℝ := (ν - 2 - 2 * ν * Real.log a) / (6 * a ^ 4)

theorem addD_eq (Λ ε ν : ℝ) {a : ℝ} (ha : 0 < a) : addD Λ ε ν a = Λ / 3 + ε * Aa ν a := by
  simp only [addD, Fd, Fd', Aa]; field_simp; ring

theorem Fd_eq (Λ ε ν : ℝ) {a : ℝ} (ha : 0 < a) : Fd Λ ε ν a = Λ / 3 + ε * (Sa ν a - Aa ν a) - 1 / a ^ 2 := by
  simp only [Fd, Sa, Aa]; field_simp; ring

/-- the invariants on the deformation -/
noncomputable def invD (Λ ε ν a : ℝ) : Fin 4 → ℝ := inv6 (addD Λ ε ν a) (Fd Λ ε ν a) a

/-- ⛭ **`R_deformed`.** `R = 4Λ + εν/a⁴` exactly; at `ν = 0` (pure radiation) `R = 4Λ`. -/
theorem R_deformed (Λ ε ν : ℝ) {a : ℝ} (ha : 0 < a) :
    frwR (addD Λ ε ν a) (Fd Λ ε ν a) a = 4 * Λ + ε * ν / a ^ 4 := by
  rw [addD_eq Λ ε ν ha, Fd_eq Λ ε ν ha]; simp only [frwR, Sa, Aa]; field_simp; ring

/-- the order-0 … order-3 coefficients, `S = Sa`, `A = Aa`, `Q = A² − SA + S²` -/
noncomputable def c0 (Λ : ℝ) : Fin 4 → ℝ := ![64 * Λ ^ 3, 16 * Λ ^ 3, 32 / 3 * Λ ^ 3, 4 * Λ ^ 3]
noncomputable def c1 (Λ ν a : ℝ) : Fin 4 → ℝ :=
  ![48 * Λ ^ 2 * ν / a ^ 4, 12 * Λ ^ 2 * ν / a ^ 4, 8 * Λ ^ 2 * ν / a ^ 4, 3 * Λ ^ 2 * ν / a ^ 4]
noncomputable def Qa (ν a : ℝ) : ℝ := Aa ν a ^ 2 - Sa ν a * Aa ν a + Sa ν a ^ 2
noncomputable def c2 (Λ ν a : ℝ) : Fin 4 → ℝ :=
  ![432 * Λ * Sa ν a ^ 2, Λ * (48 * Qa ν a + 72 * Sa ν a ^ 2), 96 * Λ * Qa ν a, 36 * Λ * Qa ν a]
noncomputable def c3 (ν a : ℝ) : Fin 4 → ℝ :=
  ![216 * Sa ν a ^ 3, 72 * Sa ν a * Qa ν a, 72 * Sa ν a * (2 * Aa ν a ^ 2 - 2 * Sa ν a * Aa ν a + Sa ν a ^ 2),
    27 * Aa ν a ^ 3 + 3 * (2 * Sa ν a - Aa ν a) ^ 3]

/-- ⛭ **`inv_poly`.** Each invariant is EXACTLY the cubic `c₀ + c₁ε + c₂ε² + c₃ε³` in the back-reaction. -/
theorem inv_poly (Λ ε ν : ℝ) {a : ℝ} (ha : 0 < a) (k : Fin 4) :
    invD Λ ε ν a k = c0 Λ k + c1 Λ ν a k * ε + c2 Λ ν a k * ε ^ 2 + c3 ν a k * ε ^ 3 := by
  have hS : ν / a ^ 4 = 6 * Sa ν a := by simp only [Sa]; field_simp
  simp only [invD, addD_eq Λ ε ν ha, Fd_eq Λ ε ν ha]
  fin_cases k <;>
    simp [inv6, frwR, frwRic2, frwRiem2, frwRic3, frwL0, frwL1, c0, c1, c2, c3, Qa, mul_div_assoc, hS] <;>
    ring

/-- ⛭ **`orders`.** Order `0` is `(64, 16, 32/3, 4)Λ³`; the order-`1` coefficient is the `ε`-derivative at `0` and
equals `(48, 12, 8, 3)Λ²ν/a⁴`, each EXACTLY `(3/4)(ν/a⁴)` times its own order `0` over `Λ`. -/
theorem orders (Λ ν : ℝ) (hΛ : 0 < Λ) {a : ℝ} (ha : 0 < a) (k : Fin 4) :
    invD Λ 0 ν a k = c0 Λ k ∧
    HasDerivAt (fun ε => invD Λ ε ν a k) (c1 Λ ν a k) 0 ∧
    c1 Λ ν a k / (c0 Λ k / Λ) = 3 / 4 * (ν / a ^ 4) := by
  refine ⟨by simp [inv_poly Λ 0 ν ha], ?_, ?_⟩
  · have h := (((hasDerivAt_const (0 : ℝ) (c0 Λ k)).add ((hasDerivAt_id (0 : ℝ)).const_mul (c1 Λ ν a k))).add
      ((hasDerivAt_pow 2 (0 : ℝ)).const_mul (c2 Λ ν a k))).add ((hasDerivAt_pow 3 (0 : ℝ)).const_mul (c3 ν a k))
    convert h using 1
    · funext e; simp [inv_poly Λ e ν ha]
    · simp
  · fin_cases k <;> simp [c0, c1] <;> field_simp <;> ring

/-- `P(ν, ℓ) = t² − νt + ν²`, `t = ν − 2 − 2νℓ`: `36 a⁸ Q = P(ν, log a)` -/
noncomputable def Pq (ν ℓ : ℝ) : ℝ := (ν - 2 - 2 * ν * ℓ) ^ 2 - ν * (ν - 2 - 2 * ν * ℓ) + ν ^ 2

/-- ⛭ **`log_structure`.** First order is log-free: `a⁴ c₁` is the same at every `a`. Second order is not:
`a⁸ c₂ = Λ(4P/3 + 2ν²), 8ΛP/3, ΛP` for `R·Ric², R·Riem², tr Ric³` with `P = P(ν, log a)`, and these differ between
`a = 1` and `a = e`. -/
theorem log_structure (Λ ν : ℝ) (hΛ : 0 < Λ) (hν : 0 < ν) :
    (∀ a b : ℝ, 0 < a → 0 < b → ∀ k, a ^ 4 * c1 Λ ν a k = b ^ 4 * c1 Λ ν b k) ∧
    (∀ a : ℝ, 0 < a →
      a ^ 8 * c2 Λ ν a 1 = Λ * (4 / 3 * Pq ν (Real.log a) + 2 * ν ^ 2) ∧
      a ^ 8 * c2 Λ ν a 2 = 8 / 3 * Λ * Pq ν (Real.log a) ∧ a ^ 8 * c2 Λ ν a 3 = Λ * Pq ν (Real.log a)) ∧
    (∀ k : Fin 4, k ≠ 0 → (1 : ℝ) ^ 8 * c2 Λ ν 1 k ≠ Real.exp 1 ^ 8 * c2 Λ ν (Real.exp 1) k) := by
  have hcl : ∀ a : ℝ, 0 < a →
      a ^ 8 * c2 Λ ν a 1 = Λ * (4 / 3 * Pq ν (Real.log a) + 2 * ν ^ 2) ∧
      a ^ 8 * c2 Λ ν a 2 = 8 / 3 * Λ * Pq ν (Real.log a) ∧ a ^ 8 * c2 Λ ν a 3 = Λ * Pq ν (Real.log a) := by
    intro a ha
    refine ⟨?_, ?_, ?_⟩ <;> simp [c2, Qa, Sa, Aa, Pq] <;> field_simp <;> ring
  refine ⟨fun a b ha hb k => ?_, hcl, fun k hk => ?_⟩
  · fin_cases k <;> simp [c1] <;> field_simp
  · have hp : 0 < Λ * (2 * ν ^ 2 + 8 * ν) := by positivity
    obtain ⟨h1, h2, h3⟩ := hcl 1 one_pos
    obtain ⟨e1, e2, e3⟩ := hcl (Real.exp 1) (Real.exp_pos 1)
    rw [Real.log_one] at h1 h2 h3
    rw [Real.log_exp] at e1 e2 e3
    fin_cases k
    · exact absurd rfl hk
    · simp only [Fin.mk_one] at *
      rw [h1, e1]; intro h; simp only [Pq] at h; nlinarith
    · simp only [Fin.reduceFinMk] at *
      rw [h2, e2]; intro h; simp only [Pq] at h; nlinarith
    · simp only [Fin.reduceFinMk] at *
      rw [h3, e3]; intro h; simp only [Pq] at h; nlinarith

/-- the order matrices on the four-point spectrum at `ν = 1`, `Λ = 3`, as the receipt samples them -/
noncomputable def M0 : Matrix (Fin 4) (Fin 4) ℝ := Matrix.of fun i j => invD 3 0 1 (spec4 i) j
noncomputable def M1 : Matrix (Fin 4) (Fin 4) ℝ := Matrix.of fun i j => c1 3 1 (spec4 i) j
noncomputable def M2 : Matrix (Fin 4) (Fin 4) ℝ := Matrix.of fun i j => c2 3 1 (spec4 i) j
/-- the control: an `a⁻⁶` put into ONE invariant (`tr Ric³`) at first order -/
noncomputable def M1ctl : Matrix (Fin 4) (Fin 4) ℝ :=
  Matrix.of fun i j => c1 3 1 (spec4 i) j + if j = 3 then 1 / spec4 i ^ 6 else 0

theorem spec4_pos (i : Fin 4) : 0 < spec4 i := by fin_cases i <;> norm_num [spec4]

/-- ⛭ **`ranks_by_order`.** The ranks are `1, 1, 2` at orders `0, 1, 2`, and the `a⁻⁶` control has rank `2` at
order `1`. -/
theorem ranks_by_order : M0.rank = 1 ∧ M1.rank = 1 ∧ M2.rank = 2 ∧ M1ctl.rank = 2 := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · refine rank_eq_of_factor M0 (Matrix.of fun _ _ => 1) (Matrix.of fun _ j => c0 3 j) ?_ ![0] ![0] ?_
    · ext i j; simp [M0, Matrix.mul_apply, inv_poly 3 0 1 (spec4_pos i)]
    · rw [Matrix.det_unique]; simp [M0, inv_poly 3 0 1 (spec4_pos 0), c0]
  · refine rank_eq_of_factor M1 (Matrix.of fun i _ => 1 / spec4 i ^ 4) (Matrix.of fun _ j => ![432, 108, 72, 27] j)
      ?_ ![0] ![0] ?_
    · ext i j; simp only [M1, Matrix.mul_apply, Matrix.of_apply, Fin.sum_univ_one]
      fin_cases j <;> simp [c1] <;> ring
    · rw [Matrix.det_unique]; simp [M1, c1, spec4]
  · refine rank_eq_of_factor M2 (Matrix.of fun i => ![3 * Sa 1 (spec4 i) ^ 2, 3 * Qa 1 (spec4 i)])
      !![432, 72, 0, 0; 0, 48, 96, 36] ?_ ![0, 2] ![0, 3] ?_
    · ext i j; simp only [M2, Matrix.mul_apply, Matrix.of_apply, Fin.sum_univ_two]
      fin_cases j <;> simp [c2] <;> ring
    · have hl := Real.log_pos (by norm_num : (1 : ℝ) < 2)
      rw [Matrix.det_fin_two]
      simp [M2, c2, Qa, Sa, Aa, spec4]
      nlinarith [mul_pos hl hl]
  · refine rank_eq_of_factor M1ctl (Matrix.of fun i => ![1 / spec4 i ^ 4, 1 / spec4 i ^ 6])
      !![432, 108, 72, 27; 0, 0, 0, 1] ?_ ![0, 2] ![0, 3] ?_
    · ext i j; simp only [M1ctl, Matrix.mul_apply, Matrix.of_apply, Fin.sum_univ_two]
      fin_cases j <;> simp [c1] <;> ring
    · rw [Matrix.det_fin_two]
      simp [M1ctl, c1, spec4]
      norm_num

end B

/-! ### C. Item by item: the rate, the counts, the kernel -/

section C

/-- **Imported:** the TT label weights `d(m)μ(m) = 2(m² − 4)√(m² − 1)`, a function of the label `m` alone. -/
noncomputable def wTT (m : ℝ) : ℝ := 2 * (m ^ 2 - 4) * Real.sqrt (m ^ 2 - 1)

/-- ⛭ **`L_coeff`.** `d(m)μ(m) = 2m³ − 9m + L/m + o(1/m)` with `L = 15/4`, as a limit; behind it the exact identity
`m(dμ − 2m³ + 9m) = 8r − r²`, `r = m/(m + √(m² − 1)) → 1/2`, for `m ≥ 1`. -/
theorem L_coeff : Tendsto (fun m : ℝ => m * (wTT m - (2 * m ^ 3 - 9 * m))) atTop (𝓝 (15 / 4)) := by
  have key : ∀ m : ℝ, 1 ≤ m → m * (wTT m - (2 * m ^ 3 - 9 * m)) =
      8 * (m / (m + Real.sqrt (m ^ 2 - 1))) - (m / (m + Real.sqrt (m ^ 2 - 1))) ^ 2 := by
    intro m hm
    have hs : Real.sqrt (m ^ 2 - 1) ^ 2 = m ^ 2 - 1 := Real.sq_sqrt (by nlinarith)
    have hs0 := Real.sqrt_nonneg (m ^ 2 - 1)
    have hp : 0 < m + Real.sqrt (m ^ 2 - 1) := by linarith
    simp only [wTT]
    field_simp
    linear_combination (-(2 * m ^ 4 - 7 * m ^ 2 + Real.sqrt (m ^ 2 - 1) * (2 * m ^ 3 - 8 * m))) * hs
  have hr : Tendsto (fun m : ℝ => m / (m + Real.sqrt (m ^ 2 - 1))) atTop (𝓝 (1 / 2)) := by
    have h1 : Tendsto (fun m : ℝ => Real.sqrt (1 - (m⁻¹) ^ 2)) atTop (𝓝 1) := by
      simpa using ((tendsto_inv_atTop_zero.pow 2).const_sub (1 : ℝ)).sqrt
    have h2 := (h1.const_add 1).inv₀ (by norm_num)
    norm_num at h2
    refine h2.congr' ?_
    filter_upwards [eventually_ge_atTop 1] with m hm
    have hm0 : 0 < m := by linarith
    have : Real.sqrt (m ^ 2 - 1) = m * Real.sqrt (1 - (m⁻¹) ^ 2) := by
      rw [show m ^ 2 - 1 = m ^ 2 * (1 - (m⁻¹) ^ 2) by field_simp, Real.sqrt_mul (sq_nonneg m),
        Real.sqrt_sq hm0.le]
    rw [this]
    have := Real.sqrt_nonneg (1 - (m⁻¹) ^ 2)
    field_simp
  have h3 := (hr.const_mul 8).sub (hr.pow 2)
  norm_num at h3
  refine h3.congr' ?_
  filter_upwards [eventually_ge_atTop 1] with m hm
  rw [key m hm]

/-- ⛭ **`rate_factor`.** The density of a label sum `W` is `W/a⁴`: times `a⁴` it is constant in `a`, while the
density itself has the nonzero derivative `−4W/a⁵`. -/
theorem rate_factor (W : ℝ) (hW : 0 < W) {a : ℝ} (ha : 0 < a) :
    HasDerivAt (fun a : ℝ => W / a ^ 4 * a ^ 4) 0 a ∧ HasDerivAt (fun a : ℝ => W / a ^ 4) (-4 * W / a ^ 5) a ∧
    -4 * W / a ^ 5 ≠ 0 := by
  refine ⟨?_, ?_, by positivity⟩
  · have : (fun a : ℝ => W / a ^ 4 * a ^ 4) =ᶠ[𝓝 a] fun _ => W := by
      filter_upwards [lt_mem_nhds ha] with x hx
      field_simp
    exact (hasDerivAt_const a W).congr_of_eventuallyEq this
  · have := ((hasDerivAt_pow 4 a).inv (by positivity)).const_mul W
    convert this using 1
    · funext x; ring
    · norm_num; field_simp

/-- the asymptotic weight `2m³ − 9m + L/m`, `L = 15/4`, and its partial sums from `m = 3` to `M + 2` -/
noncomputable def wSum (m : ℝ) : ℝ := 2 * m ^ 3 - 9 * m + 15 / 4 / m
noncomputable def Ssum (M : ℕ) : ℝ := ∑ i ∈ Finset.range M, wSum ((i : ℝ) + 3)
noncomputable def Ppoly (N : ℝ) : ℝ := N ^ 2 * (N + 1) ^ 2 / 2 - 9 * N * (N + 1) / 2 + 9

theorem Ssum_closed (M : ℕ) : Ssum M = Ppoly ((M : ℝ) + 2) + 15 / 4 * ((harmonic (M + 2) : ℝ) - 3 / 2) := by
  induction M with
  | zero => simp [Ssum, Ppoly, harmonic, Finset.sum_range_succ]; norm_num
  | succ M ih =>
    rw [Ssum, Finset.sum_range_succ, ← Ssum, ih, show M + 1 + 2 = (M + 2) + 1 by ring, harmonic_succ]
    push_cast
    simp only [wSum, Ppoly]
    have : (0 : ℝ) < M + 3 := by positivity
    field_simp
    ring

/-- ⛭ **`log_coeff`.** For ANY state moment `g`, the partial sum times `g` is `g·P(M+2) + gL·log(M+2)` plus a term
tending to `gL(γ − 3/2)`: the logarithm's coefficient relative to the sum is exactly `L`. -/
theorem log_coeff (g : ℝ) :
    Tendsto (fun M : ℕ => g * Ssum M - g * Ppoly ((M : ℝ) + 2) - g * (15 / 4) * Real.log ((M : ℝ) + 2)) atTop
      (𝓝 (g * (15 / 4) * (eulerMascheroniConstant - 3 / 2))) := by
  have h := (Real.tendsto_harmonic_sub_log.comp (tendsto_add_atTop_nat 2)).sub_const (3 / 2 : ℝ)
  refine (h.const_mul (g * (15 / 4))).congr fun M => ?_
  simp only [Function.comp, Ssum_closed]
  push_cast
  ring

/-- the control: a weight made scale-factor-dependent, `w + m/a` -/
noncomputable def SsumBad (M : ℕ) (a : ℝ) : ℝ := ∑ i ∈ Finset.range M, (wSum ((i : ℝ) + 3) + ((i : ℝ) + 3) / a)

/-- ⛭ **`control_weight`.** That control puts `M(M+5)/(2a)` into the partial sum itself: it depends on `a`. -/
theorem control_weight (M : ℕ) (a : ℝ) (ha : 0 < a) :
    SsumBad M a = Ssum M + (M : ℝ) * (M + 5) / (2 * a) ∧
    (1 ≤ M → SsumBad M 1 - Ssum M ≠ SsumBad M 2 - Ssum M) := by
  have hc : ∀ (M : ℕ) (a : ℝ), 0 < a → SsumBad M a = Ssum M + (M : ℝ) * (M + 5) / (2 * a) := by
    intro M a ha
    induction M with
    | zero => simp [SsumBad, Ssum]
    | succ M ih =>
      rw [SsumBad, Finset.sum_range_succ, ← SsumBad, ih, Ssum, Finset.sum_range_succ, ← Ssum]
      push_cast; field_simp; ring
  refine ⟨hc M a ha, fun hM => ?_⟩
  rw [hc M 1 one_pos, hc M 2 two_pos]
  have : (1 : ℝ) ≤ M := by exact_mod_cast hM
  intro h
  nlinarith

/-- ⛭ **`conventions_three`.** With the state's moment `g > 0` in front, dropping any one of the three structures
`AM⁶`, `BM⁴`, `L log M` from `D = AM⁶ + BM⁴ + L log M + F` leaves an infinite limit; dropping all three leaves `gF`. -/
theorem conventions_three (g A B L Fp : ℝ) (hg : 0 < g) (hA : 0 < A) (hB : 0 < B) (hL : 0 < L) :
    Tendsto (fun M : ℝ => g * ((A * M ^ 6 + B * M ^ 4 + L * Real.log M + Fp) - (B * M ^ 4 + L * Real.log M)))
      atTop atTop ∧
    Tendsto (fun M : ℝ => g * ((A * M ^ 6 + B * M ^ 4 + L * Real.log M + Fp) - (A * M ^ 6 + L * Real.log M)))
      atTop atTop ∧
    Tendsto (fun M : ℝ => g * ((A * M ^ 6 + B * M ^ 4 + L * Real.log M + Fp) - (A * M ^ 6 + B * M ^ 4)))
      atTop atTop ∧
    Tendsto (fun M : ℝ => g * ((A * M ^ 6 + B * M ^ 4 + L * Real.log M + Fp) -
      (A * M ^ 6 + B * M ^ 4 + L * Real.log M))) atTop (𝓝 (g * Fp)) := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · refine ((tendsto_atTop_add_const_right _ Fp ((tendsto_pow_atTop (by norm_num : (6 : ℕ) ≠ 0)).const_mul_atTop
      hA)).const_mul_atTop hg).congr fun M => ?_
    ring
  · refine ((tendsto_atTop_add_const_right _ Fp ((tendsto_pow_atTop (by norm_num : (4 : ℕ) ≠ 0)).const_mul_atTop
      hB)).const_mul_atTop hg).congr fun M => ?_
    ring
  · refine ((tendsto_atTop_add_const_right _ Fp (Real.tendsto_log_atTop.const_mul_atTop hL)).const_mul_atTop
      hg).congr fun M => ?_
    ring
  · refine tendsto_const_nhds.congr fun M => ?_
    ring

variable {q6 q4 Λ ε ν L : ℝ}
variable (hq6 : 0 < q6) (hq4 : 0 < q4) (hΛ : 0 < Λ) (hν : 0 < ν) (hL : 0 < L)

include hq6 hq4 hΛ hν hL

/-- ⛭ **`kernel_rotates`.** The three conventions span `2` directions (`Mk.rank = 2`; with `kernel_A`, a
one-dimensional kernel). With the anomaly OFF (`ε = 0`) every kernel vector has third entry `0`, and the kernel is
nontrivial; with it ON the kernel's ratio is `kv₀/kv₂ = −L/(48Λ²ενq₆)`, which runs to `−∞` as `ε → 0⁺`, while the
rescaled kernel vector `ε·kv` tends to a vector of the classical kernel. -/
theorem kernel_rotates :
    (Mk q6 q4 Λ ε ν L).rank = 2 ∧
    (∀ x : Fin 3 → ℝ, Mk q6 q4 Λ 0 ν L *ᵥ x = 0 → x 2 = 0) ∧
    Mk q6 q4 Λ 0 ν L *ᵥ ![q4, -64 * q6 * Λ, 0] = 0 ∧
    (∀ ε, kv q6 q4 Λ ε ν L 0 / kv q6 q4 Λ ε ν L 2 = -L / (48 * Λ ^ 2 * ε * ν * q6)) ∧
    Tendsto (fun ε => kv q6 q4 Λ ε ν L 0 / kv q6 q4 Λ ε ν L 2) (𝓝[>] 0) atBot ∧
    Tendsto (fun ε => ε • kv q6 q4 Λ ε ν L) (𝓝[>] 0)
      (𝓝 ![-L / (48 * Λ ^ 2 * ν * q6), 4 * L / (3 * Λ * ν * q4), 0]) ∧
    Mk q6 q4 Λ 0 ν L *ᵥ ![-L / (48 * Λ ^ 2 * ν * q6), 4 * L / (3 * Λ * ν * q4), 0] = 0 := by
  have hratio : ∀ ε, kv q6 q4 Λ ε ν L 0 / kv q6 q4 Λ ε ν L 2 = -L / (48 * Λ ^ 2 * ε * ν * q6) := by
    intro ε; simp [kv]
  refine ⟨?_, fun x hx => ?_, ?_, hratio, ?_, ?_, ?_⟩
  · refine rank_eq_of_factor _ 1 _ (Matrix.one_mul _).symm id ![1, 2] ?_
    rw [Matrix.det_fin_two]
    simp [Mk]
    exact ⟨⟨hq4.ne', hΛ.ne'⟩, hL.ne'⟩
  · have h1 := congrFun hx 1
    simp [Mk, Matrix.mulVec, dotProduct, Fin.sum_univ_three] at h1
    exact h1.resolve_left hL.ne'
  · funext i; fin_cases i <;> simp [Mk, Matrix.mulVec, dotProduct, Fin.sum_univ_three]; ring
  · have hneg : -L / (48 * Λ ^ 2 * ν * q6) < 0 := by
      have : 0 < L / (48 * Λ ^ 2 * ν * q6) := by positivity
      rw [neg_div]; linarith
    refine (tendsto_inv_nhdsGT_zero.const_mul_atTop_of_neg hneg).congr fun ε => ?_
    rw [hratio]; ring
  · have hev : (fun ε => ε • kv q6 q4 Λ ε ν L) =ᶠ[𝓝[>] 0]
        fun ε => ![-L / (48 * Λ ^ 2 * ν * q6), 4 * L / (3 * Λ * ν * q4), ε] := by
      filter_upwards [self_mem_nhdsWithin] with ε (hε : 0 < ε)
      funext i; fin_cases i <;> simp [kv] <;> field_simp
    refine Tendsto.congr' hev.symm (tendsto_pi_nhds.2 fun i => ?_)
    fin_cases i
    · exact tendsto_const_nhds
    · exact tendsto_const_nhds
    · exact (continuous_id.tendsto 0).mono_left nhdsWithin_le_nhds
  · funext i; fin_cases i <;> simp [Mk, Matrix.mulVec, dotProduct, Fin.sum_univ_three] <;> field_simp <;> ring

end C

/-! ### D. The one number a fourth time, and the unknown factor on the dimension-six direction -/

section D

variable {q6 q4 Λ ε ν L : ℝ}
variable (hq6 : 0 < q6) (hq4 : 0 < q4) (hΛ : 0 < Λ) (hε : 0 < ε) (hν : 0 < ν) (hL : 0 < L)

include hq6 hΛ hε hν in
/-- ⛭ **`one_number`.** The rotation's size moves with `L` (nonzero `L`-derivative); the curvature's `a⁻⁴` moves with
`ν` and vanishes at `ν = 0`; the first-order `R³` shift is exactly `48Λ²ν/a⁴`. -/
theorem one_number (a : ℝ) (ha : 0 < a) :
    HasDerivAt (fun L => kv q6 q4 Λ ε ν L 0 / kv q6 q4 Λ ε ν L 2) (-1 / (48 * Λ ^ 2 * ε * ν * q6)) L ∧
    -1 / (48 * Λ ^ 2 * ε * ν * q6) ≠ 0 ∧
    HasDerivAt (fun ν => frwR (addD Λ ε ν a) (Fd Λ ε ν a) a - 4 * Λ) (ε / a ^ 4) ν ∧ ε / a ^ 4 ≠ 0 ∧
    frwR (addD Λ ε 0 a) (Fd Λ ε 0 a) a - 4 * Λ = 0 ∧
    c1 Λ ν a 0 / (48 * Λ ^ 2 * ν / a ^ 4) = 1 := by
  refine ⟨?_, by positivity, ?_, by positivity, ?_, ?_⟩
  · have := (hasDerivAt_id L).const_mul (-1 / (48 * Λ ^ 2 * ε * ν * q6))
    convert this using 1
    · funext L; simp [kv]; ring
    · simp
  · have := (hasDerivAt_id ν).const_mul (ε / a ^ 4)
    convert this using 1
    · funext ν; rw [R_deformed Λ ε ν ha]; simp; ring
    · simp
  · rw [R_deformed Λ ε 0 ha]; ring
  · simp [c1]; field_simp

include hq6 hq4 hΛ hε hν hL in
/-- ⛭ **`A6_factor`.** Carry an unknown factor `A₆ > 0` on the dimension-six direction (`f₁ ↦ A₆f₁`): the rank on the
four-point spectrum is still `2 = rank Mk`, and the value kernel is still a line whose third entry is nonzero. -/
theorem A6_factor (A6 : ℝ) (hA6 : 0 < A6) :
    (∀ a, fs (A6 * q6) q4 Λ ε ν L 0 a = A6 * fs q6 q4 Λ ε ν L 0 a) ∧
    (Vmat (A6 * q6) q4 Λ ε ν L spec4).rank = 2 ∧ (Mk (A6 * q6) q4 Λ ε ν L).rank = 2 ∧
    (∀ x : Fin 3 → ℝ, Vmat (A6 * q6) q4 Λ ε ν L spec4 *ᵥ x = 0 ↔ ∃ t : ℝ, x = t • kv (A6 * q6) q4 Λ ε ν L) ∧
    kv (A6 * q6) q4 Λ ε ν L 2 ≠ 0 := by
  have hq := mul_pos hA6 hq6
  obtain ⟨k1, k2, k3⟩ := kernel_A hq hq4 hΛ hε hν hL
  refine ⟨fun a => by simp [fs]; ring, (rank_A hq hq4 hΛ hε hν hL).1,
    (kernel_rotates hq hq4 hΛ hν hL).1, fun x => (k2 x).trans (k1 x), k3⟩

end D

end R64Descent

end ShadowProbe

#print axioms ShadowProbe.R64Descent.rank_A
#print axioms ShadowProbe.R64Descent.kernel_A
#print axioms ShadowProbe.R64Descent.phase_A
#print axioms ShadowProbe.R64Descent.substrate
#print axioms ShadowProbe.R64Descent.R_deformed
#print axioms ShadowProbe.R64Descent.inv_poly
#print axioms ShadowProbe.R64Descent.orders
#print axioms ShadowProbe.R64Descent.log_structure
#print axioms ShadowProbe.R64Descent.ranks_by_order
#print axioms ShadowProbe.R64Descent.L_coeff
#print axioms ShadowProbe.R64Descent.rate_factor
#print axioms ShadowProbe.R64Descent.log_coeff
#print axioms ShadowProbe.R64Descent.control_weight
#print axioms ShadowProbe.R64Descent.conventions_three
#print axioms ShadowProbe.R64Descent.kernel_rotates
#print axioms ShadowProbe.R64Descent.one_number
#print axioms ShadowProbe.R64Descent.A6_factor

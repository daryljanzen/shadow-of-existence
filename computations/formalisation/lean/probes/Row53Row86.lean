import ShadowEngine

/-! # Campaign 32 (`r7443+71`): step 3, the computable parts of structure rows 53 and 86

Both rows stay `ROW: A DIFFERENT KIND` (`r7421`). Their own objects are an essential image (53) and a `Z₃` action on
loci of the quadric (86). What their receipts compute beside those objects is built here.

- ***Row 53*** (`K7_range_is_essential_image.py`): the fibre counts.
  - `sds_kernel`: the SdS kernel is exactly a one-parameter family, as a classification.
  - `typeD_four`: the Type-D quartic pair has exactly four parameters.
  - `skew_finrank`: the stratum arithmetic `n(n−1)/2`, as the dimension of the skew-symmetric matrices.
- ***Row 86*** (`P14_is_there_a_singlet_for_the_axis_pair.py`): `branch_count`, one branch exactly on the throat. -/

namespace ShadowProbe

namespace R53R86

open Matrix

/-! ### Row 53 -/

/-- the SdS kernel `f = 1 − 2M/r − Λr²/3` -/
noncomputable def fSdS (M Λ r : ℝ) : ℝ := 1 - 2 * M / r - Λ * r ^ 2 / 3

/-- ⛭ **`sds_kernel`.** On `r > 0`, every `fSdS M` solves `r f' + f − 1 + Λr² = 0`; and EVERY differentiable solution
is `fSdS M` for exactly one `M`. The receipt's "`1` for SdS" is a classification, not a symbol count. -/
theorem sds_kernel (Λ : ℝ) :
    (∀ M r : ℝ, 0 < r → HasDerivAt (fSdS M Λ) (2 * M / r ^ 2 - 2 * Λ * r / 3) r ∧
        r * (2 * M / r ^ 2 - 2 * Λ * r / 3) + fSdS M Λ r - 1 + Λ * r ^ 2 = 0) ∧
      ∀ f f' : ℝ → ℝ, (∀ r, 0 < r → HasDerivAt f (f' r) r) →
        (∀ r, 0 < r → r * f' r + f r - 1 + Λ * r ^ 2 = 0) →
        ∃! M : ℝ, ∀ r, 0 < r → f r = fSdS M Λ r := by
  refine ⟨fun M r hr => ⟨?_, ?_⟩, fun f f' hf hode => ?_⟩
  · have h1 : HasDerivAt (fun x : ℝ => x⁻¹) (-(r ^ 2)⁻¹) r := hasDerivAt_inv hr.ne'
    have h2 : HasDerivAt (fun x : ℝ => x ^ 2) (2 * r) r := by simpa using hasDerivAt_pow 2 r
    have := ((h1.const_mul (2 * M)).const_sub 1).sub (h2.const_mul (Λ / 3))
    convert this using 1
    · funext x; simp [fSdS]; ring
    · field_simp
  · simp only [fSdS]; field_simp; ring
  · -- g = r f − r + Λ r³/3 has derivative zero on (0, ∞), so it is constant there
    set g : ℝ → ℝ := fun r => r * f r - r + Λ * r ^ 3 / 3 with hg
    have hgd : ∀ r, 0 < r → HasDerivAt g 0 r := by
      intro r hr
      have h3 : HasDerivAt (fun x : ℝ => x ^ 3) (3 * r ^ 2) r := by simpa using hasDerivAt_pow 3 r
      have := (((hasDerivAt_id r).mul (hf r hr)).sub (hasDerivAt_id r)).add (h3.const_mul (Λ / 3))
      convert this using 1
      · funext x; simp [hg]; ring
      · simp; linarith [hode r hr]
    have hconst : ∀ r, 0 < r → g r = g 1 := by
      intro r hr
      have hdiff : DifferentiableOn ℝ g (Set.Ioi 0) := fun x hx => (hgd x hx).differentiableAt.differentiableWithinAt
      have hder : Set.EqOn (deriv g) 0 (Set.Ioi 0) := fun x hx => (hgd x hx).deriv
      exact isOpen_Ioi.is_const_of_deriv_eq_zero (convex_Ioi 0).isPreconnected hdiff hder hr (by norm_num : (0:ℝ) < 1)
    refine ⟨-(g 1) / 2, fun r hr => ?_, fun M hM => ?_⟩
    · have := hconst r hr
      simp only [hg, fSdS] at this ⊢
      field_simp
      linarith
    · have h1 := hM 1 one_pos
      simp only [hg, fSdS] at h1 ⊢
      linarith

/-- the Type-D quartic pair: leading `−Λ/3` in both, OPPOSITE `c₂`, SHARED `c₀` -/
noncomputable def Dr (Λ c2 c1 c0 r : ℝ) : ℝ := -Λ / 3 * r ^ 4 + c2 * r ^ 2 + c1 * r + c0
noncomputable def Dp (Λ c2 d1 c0 p : ℝ) : ℝ := -Λ / 3 * p ^ 4 - c2 * p ^ 2 + d1 * p + c0

/-- ⛭ **`typeD_four`.** `(c₂, c₁, c₀, d₁) ↦ (D_r, D_p)` is injective: the family has exactly FOUR parameters, not six,
because `c₀` is shared and `c₂` enters both with opposite signs -/
theorem typeD_four (Λ c2 c1 c0 d1 c2' c1' c0' d1' : ℝ)
    (hr : ∀ r, Dr Λ c2 c1 c0 r = Dr Λ c2' c1' c0' r) (hp : ∀ p, Dp Λ c2 d1 c0 p = Dp Λ c2' d1' c0' p) :
    c2 = c2' ∧ c1 = c1' ∧ c0 = c0' ∧ d1 = d1' := by
  have a0 := hr 0; have a1 := hr 1; have a2 := hr (-1); have b1 := hp 1; have b2 := hp (-1)
  simp only [Dr, Dp] at a0 a1 a2 b1 b2
  refine ⟨?_, ?_, ?_, ?_⟩ <;> nlinarith

/-- the skew-symmetric `n × n` real matrices -/
def skew (n : ℕ) : Submodule ℝ (Matrix (Fin n) (Fin n) ℝ) where
  carrier := {A | Aᵀ = -A}
  add_mem' := by intro A B hA hB; simp only [Set.mem_ofPred_eq] at *; rw [Matrix.transpose_add, hA, hB]; abel
  zero_mem' := by simp
  smul_mem' := by intro c A hA; simp only [Set.mem_ofPred_eq] at *; rw [Matrix.transpose_smul, hA, smul_neg]

/-- the strictly upper entries -/
abbrev Up (n : ℕ) := {p : Fin n × Fin n // p.1 < p.2}

/-- a skew matrix is its strictly upper entries -/
noncomputable def skewEquiv (n : ℕ) : skew n ≃ₗ[ℝ] (Up n → ℝ) where
  toFun A := fun p => (A : Matrix (Fin n) (Fin n) ℝ) p.1.1 p.1.2
  map_add' A B := by ext p; simp
  map_smul' c A := by ext p; simp
  invFun f := ⟨Matrix.of fun i j => if h : i < j then f ⟨(i, j), h⟩ else if h' : j < i then -f ⟨(j, i), h'⟩ else 0, by
    ext i j
    simp only [Matrix.transpose_apply, Matrix.of_apply, Matrix.neg_apply]
    rcases lt_trichotomy i j with h | h | h
    · simp [h, not_lt.mpr h.le]
    · subst h; simp
    · simp [h, not_lt.mpr h.le]⟩
  left_inv A := by
    have hA : (A : Matrix (Fin n) (Fin n) ℝ)ᵀ = -A := A.2
    ext i j
    simp only [Matrix.of_apply]
    rcases lt_trichotomy i j with h | h | h
    · simp [h]
    · subst h
      have := congrFun (congrFun hA i) i
      simp [Matrix.transpose_apply] at this ⊢; linarith
    · have := congrFun (congrFun hA i) j
      simp [Matrix.transpose_apply] at this
      simp [h, not_lt.mpr h.le, this]
  right_inv f := by ext p; simp [p.2]

/-- ⛭ **`skew_finrank`.** `dim so(n) = n(n − 1)/2` at the receipt's `n = 3, 5, 6`: `3, 10, 15`. So the receipt's
`SO(4,1)` is `10`, `SO(2,1) × SO(3)` is `3 + 3 = 6`, `ℝ_t × SO(3)` is `1 + 3 = 4`, inside `so(5,1)`'s `15`. -/
theorem skew_finrank :
    Module.finrank ℝ (skew 3) = 3 ∧ Module.finrank ℝ (skew 5) = 10 ∧ Module.finrank ℝ (skew 6) = 15 ∧
      3 * (3 - 1) / 2 = 3 ∧ 5 * (5 - 1) / 2 = 10 ∧ 6 * (6 - 1) / 2 = 15 := by
  refine ⟨?_, ?_, ?_, by norm_num, by norm_num, by norm_num⟩ <;>
    rw [(skewEquiv _).finrank_eq, Module.finrank_fintype_fun_eq_card] <;> decide

/-! ### Row 86 -/

/-- ⛭ **`branch_count`.** Over `ℂ`, the height `z² = X² − α²` has ONE root exactly when `X² = α²` (the throat), and
two DISTINCT roots otherwise. That includes the axis `X = 0`, where the pair is imaginary and not absent. -/
theorem branch_count (X α : ℂ) :
    (X ^ 2 = α ^ 2 → ∀ z : ℂ, z ^ 2 = X ^ 2 - α ^ 2 ↔ z = 0) ∧
      (X ^ 2 ≠ α ^ 2 → ∃ z₁ z₂ : ℂ, z₁ ≠ z₂ ∧ ∀ z : ℂ, z ^ 2 = X ^ 2 - α ^ 2 ↔ z = z₁ ∨ z = z₂) := by
  refine ⟨fun h z => ?_, fun h => ?_⟩
  · rw [h, sub_self]; exact pow_eq_zero_iff two_ne_zero
  · set s : ℂ := (X ^ 2 - α ^ 2) ^ ((2 : ℕ) : ℂ)⁻¹ with hsdef
    have hs : s ^ 2 = X ^ 2 - α ^ 2 := Complex.cpow_nat_inv_pow _ two_ne_zero
    have hs0 : s ≠ 0 := by
      intro h0; apply h; rw [← sub_eq_zero, ← hs, h0]; ring
    refine ⟨s, -s, ?_, fun z => ?_⟩
    · intro e; apply hs0; linear_combination e / 2
    · rw [← hs]; exact sq_eq_sq_iff_eq_or_eq_neg

end R53R86

end ShadowProbe

#print axioms ShadowProbe.R53R86.sds_kernel
#print axioms ShadowProbe.R53R86.typeD_four
#print axioms ShadowProbe.R53R86.skew_finrank
#print axioms ShadowProbe.R53R86.branch_count

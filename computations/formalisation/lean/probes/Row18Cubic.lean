import ShadowEngine

/-! # Campaign 26 (`r7427+71`): row 18's computable residue, from `P7`'s `order3_bridge`

The horizon cubic family `r³ + (E² − 1)r + 2M` is depressed: `r³ + pr + q`, with roots `x, y, z`, `x + y + z = 0`,
`p = xy + yz + zx`, `q = −xyz`. Everything here is an identity over a commutative ring, so it holds over ℂ, where
the roots of every member live. -/

namespace ShadowProbe

section Row18Cubic

/-- **(a) The discriminant is the squared product of root differences**, so it vanishes exactly when two roots
collide. -/
theorem cubic_disc_roots {R : Type*} [CommRing R] (x y z : R) (h : x + y + z = 0) :
    -4 * (x * y + y * z + z * x) ^ 3 - 27 * (-(x * y * z)) ^ 2 = ((x - y) * (y - z) * (z - x)) ^ 2 := by
  have hz : z = -x - y := by linear_combination h
  subst hz; ring

lemma disc_zero_iff {R : Type*} [CommRing R] [IsDomain R] (x y z : R) (h : x + y + z = 0) :
    -4 * (x * y + y * z + z * x) ^ 3 - 27 * (-(x * y * z)) ^ 2 = 0 ↔ x = y ∨ y = z ∨ z = x := by
  rw [cubic_disc_roots x y z h, pow_eq_zero_iff two_ne_zero, mul_eq_zero, mul_eq_zero, sub_eq_zero, sub_eq_zero,
    sub_eq_zero, or_assoc]

/-- **(b) The family's discriminant**, `4((1 − E²)³ − 27M²)` (the receipt's assert), and the horizon member's branch
points: at `E = 0` it vanishes exactly at `27M² = 1`, the Nariai masses. -/
theorem family_disc (E M : ℝ) :
    -4 * (E ^ 2 - 1) ^ 3 - 27 * (2 * M) ^ 2 = 4 * ((1 - E ^ 2) ^ 3 - 27 * M ^ 2) ∧
      (-4 * ((0 : ℝ) ^ 2 - 1) ^ 3 - 27 * (2 * M) ^ 2 = 0 ↔ 27 * M ^ 2 = 1) := by
  refine ⟨by ring, ?_⟩
  constructor <;> intro h <;> linarith

/-- **(c) Square in `M` exactly when `p = 0`:** over ℂ, `−4p³ − 108M²` is the square of a linear polynomial in `M`
iff `p = 0`. (The receipt's "√Δ rational in `M`"; that a square in `ℂ(M)` of this quadratic is a polynomial
square is not re-proved here.) -/
theorem disc_square_iff (p : ℂ) :
    (∃ a b : ℂ, ∀ M : ℂ, (a + b * M) ^ 2 = -4 * p ^ 3 - 27 * (2 * M) ^ 2) ↔ p = 0 := by
  constructor
  · rintro ⟨a, b, h⟩
    have h0 := h 0
    have h1 := h 1
    have h2 := h (-1)
    simp only [mul_zero, add_zero, mul_one, mul_neg] at h0 h1 h2
    have hab : a * b = 0 := by linear_combination (h1 - h2) / 4
    have hb : b ^ 2 = -108 := by linear_combination (h1 + h2) / 2 - h0
    have hb0 : b ≠ 0 := fun hb0 => by rw [hb0] at hb; norm_num at hb
    have ha : a = 0 := by
      rcases mul_eq_zero.1 hab with ha | ha
      · exact ha
      · exact absurd ha hb0
    rw [ha] at h0
    have : p ^ 3 = 0 := by linear_combination h0 / 4
    exact pow_eq_zero_iff (by norm_num) |>.1 this
  · rintro rfl
    have hs : ((-108 : ℂ) ^ ((2 : ℕ)⁻¹ : ℂ)) ^ 2 = -108 := Complex.cpow_nat_inv_pow _ two_ne_zero
    exact ⟨0, (-108 : ℂ) ^ ((2 : ℕ)⁻¹ : ℂ), fun M => by rw [zero_add, mul_pow, hs]; ring⟩

/-- **(d) Equilateral exactly when `p = 0`:** with `ω² + ω + 1 = 0`, the roots satisfy `x + ωy + ω²z = 0` or
`x + ω²y + ωz = 0` (an equilateral triangle, either orientation) iff `p = 0`, because the product of the two is
`x² + y² + z² − (xy + yz + zx) = −3p` when `x + y + z = 0`. -/
theorem equilateral_iff {R : Type*} [CommRing R] [IsDomain R] [CharZero R] (ω x y z : R)
    (hω : ω ^ 2 + ω + 1 = 0) (h : x + y + z = 0) :
    (x + ω * y + ω ^ 2 * z = 0 ∨ x + ω ^ 2 * y + ω * z = 0) ↔ x * y + y * z + z * x = 0 := by
  have key : (x + ω * y + ω ^ 2 * z) * (x + ω ^ 2 * y + ω * z) = -3 * (x * y + y * z + z * x) := by
    have hz : z = -x - y := by linear_combination h
    subst hz
    linear_combination (-ω ^ 2 * x * y - ω ^ 2 * y ^ 2 + ω * x ^ 2 + 3 * ω * x * y + 3 * ω * y ^ 2 - 2 * x ^ 2
      - 3 * x * y - 3 * y ^ 2) * hω
  rw [← mul_eq_zero, key, mul_eq_zero]
  constructor
  · rintro (h3 | hp)
    · exact absurd h3 (by norm_num)
    · exact hp
  · exact Or.inr

/-- **(e) Simple branching:** with `p ≠ 0` there is no triple root, so every collision is of exactly two roots and
the local monodromy at a branch point is a transposition. -/
theorem no_triple_root {R : Type*} [CommRing R] [IsDomain R] [CharZero R] (x y z : R) (h : x + y + z = 0)
    (hp : x * y + y * z + z * x ≠ 0) : ¬ (x = y ∧ y = z) := by
  rintro ⟨rfl, rfl⟩
  have : (3 : R) * x = 0 := by linear_combination h
  have hx : x = 0 := by
    rcases mul_eq_zero.1 this with h3 | h3
    · exact absurd h3 (by norm_num)
    · exact h3
  exact hp (by rw [hx]; ring)

end Row18Cubic

end ShadowProbe

#print axioms ShadowProbe.cubic_disc_roots
#print axioms ShadowProbe.disc_zero_iff
#print axioms ShadowProbe.family_disc
#print axioms ShadowProbe.disc_square_iff
#print axioms ShadowProbe.equilateral_iff
#print axioms ShadowProbe.no_triple_root

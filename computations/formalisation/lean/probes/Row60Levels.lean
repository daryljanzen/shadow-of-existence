import Mathlib.Tactic
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Analysis.SpecialFunctions.Integrals.Basic
import Mathlib.MeasureTheory.Integral.IntervalIntegral.Periodic

/-! # Campaign 45 (`r7443+71.34`): row 60, the assembly gives both level sums, with the spectrum imported

The receipt is `P10_the_assembly_gives_both_level_sums_in_the_towers_own_variables_and_the_sign_needs_no_bitensor.py`
(`r7034`). This probe formalises its computed checks A–E.

- ***(A)*** An explicit basis built from `δ` and `ε`: `P` at rank 4, `B0` at rank 5, `C1, C2` at rank 6. Every
  symmetry, tracelessness, transversality and pair-exchange condition is verified componentwise over `Fin 3`
  (`decide +kernel`). The trace relation `Σ_a C_{aij,akl} = (λ·deg/5) P_{ijkl}` fixes exactly one of `C`'s two
  numbers, and the full trace is `λ·deg` for every value of the other.
  - **Rank certificate, within the candidate span.** Every rational combination of the receipt's candidate
    structures (all `δ`-matchings, or one `ε` with `δ`'s) that satisfies the conditions is a multiple of the
    exhibited basis (`cert4`, `cert5`, `cert6`). The basis is nonzero, and `C1, C2` have a nonzero `2 × 2` minor.
    The four kernel relations among the ten rank-5 candidates are exhibited (`ker5_*`). So the dimensions are
    `(1, 1, 2)` *within the span*. Completeness of the `δ/ε` span (the first fundamental theorem for `SO(3)`) is
    **not** claimed.
- ***(B)*** The `ε²` coefficient `scT2` of the frame-Koszul scalar of `exp(εH)` on `S³` (row 62's `jet_series`,
  copied below and restricted to orders `0..2`). On the transverse-traceless constraint variety it equals
  `−¼ ∇_a h_bc ∇_a h_bc + 0 · ∇_a h_bc ∇_b h_ac − ½ h_ab h_ab`. This is an identity on the variety, proved by an
  explicit `linear_combination` of the twelve linear constraints, not fitted on samples. The three coefficients
  are the only ones that work (`B_unique`), so the mixed coefficient is `0`.
  - Controls: `−2 tr h²` at a frame-constant `h`; and on row 59's `H4` the identity's right side is exactly row
    59's `R₂` integrand, whose Euler-box integral is `−16π²` (row 59's `section_e_integrals`, copied).
- ***(C)*** The seven level values, from the `3⁵`-index sums (`decide +kernel` on the integer sums), as polynomials
  in `(c_C, c_B, λ, deg)`. The combination with the seven coefficients is `(49/48) c_C deg − (13/480) λ deg² − 45 c_B²`.
  With the imports it gives `−¼·deg·μ²` (second order) and `−(1/120) deg² (5μ² + 4)` (fourth order). Both vanish at
  `m = 2` and are negative for every real `m ≥ 3`, proved by positivity.
- ***(D)*** The cross-level double sum factorises as `(49/48 c_C − 13/480 λ deg)(m) · deg(m′) − 45 c_B(m) c_B(m′)`,
  and its diagonal is C's object. The Faulhaber sums are closed polynomials of degrees 5 and 7, with leading
  coefficients `−1/10` and `−1/42`.
- ***(E)*** The sign algebra for `2c₄ − g²/μ²` against the rearranged `μ² − g²/(2c₄)`.

***Imports, stated as imports*** (section `Imports`, each a named definition or hypothesis whose docstring says
so): the TT spectrum `λ = m² − 3`, `deg = 2(m² − 4)`, `μ² = m² − 1`; the value `c_C = −(m²−4)(m²+5)/35`; the parity
`c_B = 0` (a hypothesis `hB`); the seven rational coefficients and their seven contractions (`r7032`, row 62); and
the Wick-tensor ansatz, that level sums of harmonic products are the invariant tensors `A, B, C` (`levelValue`). No
theorem derives any of them.
-/

-- Some uniform tactic steps are idle on some cases; these linters report that idleness, not a gap.
set_option linter.unusedTactic false
set_option linter.unnecessarySeqFocus false
set_option linter.unusedSimpArgs false
set_option linter.unusedSectionVars false
set_option linter.unusedVariables false
set_option linter.unreachableTactic false
set_option linter.style.longLine false
set_option linter.constructorNameAsVariable false
set_option linter.style.setOption false
set_option linter.flexible false
set_option maxHeartbeats 400000000
set_option maxRecDepth 200000
-- elaborate declarations one at a time, to keep the peak memory down
set_option Elab.async false

namespace ShadowProbe

namespace R60Levels

open Finset

noncomputable section

/-! ## Imports (stated as imports; nothing below derives them) -/

section Imports

/-- **IMPORTED** (the TT spectrum on `S³`): the eigenvalue at level `m`, `λ = m² − 3`. -/
def lamSpec (m : ℝ) : ℝ := m ^ (2:ℕ) - 3

/-- **IMPORTED** (the TT spectrum on `S³`): the degeneracy at level `m`, `deg = 2(m² − 4)`. -/
def degSpec (m : ℝ) : ℝ := 2 * (m ^ (2:ℕ) - 4)

/-- **IMPORTED** (the tower's frequency, part of the spectrum import): `μ² = m² − 1`. -/
def mu2 (m : ℝ) : ℝ := m ^ (2:ℕ) - 1

/-- **IMPORTED** (the receipt's value for `C`'s free number, carried from `r7018`; its provenance is not checked
here): `c_C = −(m² − 4)(m² + 5)/35`. -/
def cCval (m : ℝ) : ℝ := -(m ^ (2:ℕ) - 4) * (m ^ (2:ℕ) + 5) / 35

/-- **IMPORTED** (`r7032`, row 62): the seven rational coefficients
`−5/48, 1/8, 1/24, 19/192, 7/48, −53/192, 1/8`. -/
def ACO : Fin 7 → ℝ := ![-5/48, 1/8, 1/24, 19/192, 7/48, -53/192, 1/8]

/-- **IMPORTED** (`r7032`, row 62): the seven contractions those coefficients multiply, transcribed from the receipt
as entries `0, 2, 24, 62, 72, 84, 194` of its enumeration of the 372 admissible quartic contractions. The ten slots
are `∇_a h_bc` (slots 0–2), `∇_d h_ef` (3–5), `h` (6–7), `h` (8–9). Entry `s` gives the summed index that slot `s`
carries. -/
def pat : Fin 7 → Fin 10 → Fin 5 :=
  ![![0, 1, 2, 0, 1, 2, 3, 4, 3, 4], ![0, 1, 2, 0, 1, 3, 2, 4, 3, 4], ![0, 1, 2, 0, 3, 4, 1, 2, 3, 4],
    ![0, 1, 2, 1, 0, 3, 2, 4, 3, 4], ![0, 1, 2, 3, 0, 1, 2, 4, 3, 4], ![0, 1, 2, 3, 0, 4, 1, 2, 3, 4],
    ![0, 1, 2, 3, 1, 4, 0, 2, 3, 4]]

end Imports

/-! ## (A) the invariant basis, its conditions, and the rank certificate within the candidate span -/

/-- `δ_ij` -/
def dl (i j : Fin 3) : ℤ := if i = j then 1 else 0

/-- `ε_ijk` -/
def ee (i j k : Fin 3) : ℤ :=
  if (i = 0 ∧ j = 1 ∧ k = 2) ∨ (i = 1 ∧ j = 2 ∧ k = 0) ∨ (i = 2 ∧ j = 0 ∧ k = 1) then 1
  else if (i = 0 ∧ j = 2 ∧ k = 1) ∨ (i = 2 ∧ j = 1 ∧ k = 0) ∨ (i = 1 ∧ j = 0 ∧ k = 2) then -1 else 0

/-- a sum over one index in `Fin 3`, written out -/
def S3 {R : Type*} [Add R] (f : Fin 3 → R) : R := f 0 + f 1 + f 2

/-- the conditions on `A_{ij,kl}` (the receipt's `condsA`): symmetric in each pair, traceless in each pair, and
pair exchange -/
def CondA {R : Type*} [CommRing R] (T : Fin 3 → Fin 3 → Fin 3 → Fin 3 → R) : Prop :=
  (∀ i j k l, T i j k l = T j i k l) ∧ (∀ i j k l, T i j k l = T i j l k) ∧
  (∀ i j, S3 (fun k => T k k i j) = 0) ∧ (∀ i j, S3 (fun k => T i j k k) = 0) ∧
  (∀ i j k l, T i j k l = T k l i j)

/-- the conditions on `B_{a ij, kl}` (the receipt's `condsB`): symmetric in `ij` and in `kl`, traceless in both,
and transverse (`Σ_k B_{k kj, il} = 0`) -/
def CondB {R : Type*} [CommRing R] (T : Fin 3 → Fin 3 → Fin 3 → Fin 3 → Fin 3 → R) : Prop :=
  (∀ a i j k l, T a i j k l = T a j i k l) ∧ (∀ a i j k l, T a i j k l = T a i j l k) ∧
  (∀ a i j, S3 (fun k => T a k k i j) = 0) ∧ (∀ a i j, S3 (fun k => T a i j k k) = 0) ∧
  (∀ j i l, S3 (fun k => T k k j i l) = 0)

/-- the conditions on `C_{a ij, b kl}` (the receipt's `condsC`): symmetric in `ij` and in `kl`, traceless in both,
pair exchange `(a ij) ↔ (b kl)`, and transverse -/
def CondC {R : Type*} [CommRing R] (T : Fin 3 → Fin 3 → Fin 3 → Fin 3 → Fin 3 → Fin 3 → R) : Prop :=
  (∀ a i j b k l, T a i j b k l = T a j i b k l) ∧ (∀ a i j b k l, T a i j b k l = T a i j b l k) ∧
  (∀ a b i j, S3 (fun k => T a k k b i j) = 0) ∧ (∀ a i j b, S3 (fun k => T a i j b k k) = 0) ∧
  (∀ a i j b k l, T a i j b k l = T b k l a i j) ∧ (∀ j b l n, S3 (fun k => T k k j b l n) = 0)

/-- the rank-4 candidate structures, in the receipt's own order: products of `δ`'s (3 of them) -/
def S4 (n : Fin 3) (i j k l : Fin 3) : ℤ :=
  match n with
  | 0 => dl i j * dl k l
  | 1 => dl i k * dl j l
  | 2 => dl i l * dl j k

/-- a general element of the rank-4 candidate span, with rational coefficients `z` -/
def T4 (z : Fin 3 → ℚ) (i j k l : Fin 3) : ℚ :=
  z 0 * S4 0 i j k l + z 1 * S4 1 i j k l + z 2 * S4 2 i j k l
/-- the rank-5 candidate structures, in the receipt's own order: one `ε` and one `δ` (10 of them) -/
def S5 (n : Fin 10) (i j k l m : Fin 3) : ℤ :=
  match n with
  | 0 => ee i j k * dl l m
  | 1 => ee i j l * dl k m
  | 2 => ee i j m * dl k l
  | 3 => ee i k l * dl j m
  | 4 => ee i k m * dl j l
  | 5 => ee i l m * dl j k
  | 6 => ee j k l * dl i m
  | 7 => ee j k m * dl i l
  | 8 => ee j l m * dl i k
  | 9 => ee k l m * dl i j

/-- a general element of the rank-5 candidate span, with rational coefficients `z` -/
def T5 (z : Fin 10 → ℚ) (i j k l m : Fin 3) : ℚ :=
  z 0 * S5 0 i j k l m + z 1 * S5 1 i j k l m + z 2 * S5 2 i j k l m + z 3 * S5 3 i j k l m + z 4 * S5 4 i j k l m + z 5 * S5 5 i j k l m + z 6 * S5 6 i j k l m + z 7 * S5 7 i j k l m + z 8 * S5 8 i j k l m + z 9 * S5 9 i j k l m
/-- the rank-6 candidate structures, in the receipt's own order: products of `δ`'s (15 of them) -/
def S6 (n : Fin 15) (i j k l m q : Fin 3) : ℤ :=
  match n with
  | 0 => dl i j * dl k l * dl m q
  | 1 => dl i j * dl k m * dl l q
  | 2 => dl i j * dl k q * dl l m
  | 3 => dl i k * dl j l * dl m q
  | 4 => dl i k * dl j m * dl l q
  | 5 => dl i k * dl j q * dl l m
  | 6 => dl i l * dl j k * dl m q
  | 7 => dl i l * dl j m * dl k q
  | 8 => dl i l * dl j q * dl k m
  | 9 => dl i m * dl j k * dl l q
  | 10 => dl i m * dl j l * dl k q
  | 11 => dl i m * dl j q * dl k l
  | 12 => dl i q * dl j k * dl l m
  | 13 => dl i q * dl j l * dl k m
  | 14 => dl i q * dl j m * dl k l

/-- a general element of the rank-6 candidate span, with rational coefficients `z` -/
def T6 (z : Fin 15 → ℚ) (i j k l m q : Fin 3) : ℚ :=
  z 0 * S6 0 i j k l m q + z 1 * S6 1 i j k l m q + z 2 * S6 2 i j k l m q + z 3 * S6 3 i j k l m q + z 4 * S6 4 i j k l m q + z 5 * S6 5 i j k l m q + z 6 * S6 6 i j k l m q + z 7 * S6 7 i j k l m q + z 8 * S6 8 i j k l m q + z 9 * S6 9 i j k l m q + z 10 * S6 10 i j k l m q + z 11 * S6 11 i j k l m q + z 12 * S6 12 i j k l m q + z 13 * S6 13 i j k l m q + z 14 * S6 14 i j k l m q

/-- the projector, scaled: `P6 = 6 P`, `P_ijkl = ½(δ_ik δ_jl + δ_il δ_jk) − ⅓ δ_ij δ_kl` -/
def P6 (i j k l : Fin 3) : ℤ := -2 * S4 0 i j k l + 3 * S4 1 i j k l + 3 * S4 2 i j k l

/-- the rank-5 basis tensor `B0`: the receipt's `TB / c_B`, an integer combination of the `εδ` structures -/
def B0 (i j k l m : Fin 3) : ℤ := S5 1 i j k l m + S5 2 i j k l m + S5 3 i j k l m + S5 4 i j k l m

/-- the receipt's `C`-tensor's `c_C` direction, scaled by `8` -/
def C1i (i j k l m q : Fin 3) : ℤ := -6 * S6 0 i j k l m q + S6 1 i j k l m q + S6 2 i j k l m q - 6 * S6 3 i j k l m q + S6 4 i j k l m q + S6 5 i j k l m q + 8 * S6 6 i j k l m q - 6 * S6 7 i j k l m q - 6 * S6 8 i j k l m q - 6 * S6 9 i j k l m q + 8 * S6 10 i j k l m q + 8 * S6 11 i j k l m q - 6 * S6 12 i j k l m q + 8 * S6 13 i j k l m q + 8 * S6 14 i j k l m q

/-- the receipt's `C`-tensor's `λ·deg` direction, scaled by `240` -/
def C2i (i j k l m q : Fin 3) : ℤ := 2 * S6 0 i j k l m q - 3 * S6 1 i j k l m q - 3 * S6 2 i j k l m q + 2 * S6 3 i j k l m q - 3 * S6 4 i j k l m q - 3 * S6 5 i j k l m q - 8 * S6 6 i j k l m q + 10 * S6 7 i j k l m q + 10 * S6 8 i j k l m q + 2 * S6 9 i j k l m q + 2 * S6 12 i j k l m q

/-- a kernel relation among the ten `εδ` candidates (exhibited; there are four, so the span is 6-dimensional) -/
theorem ker5_6 : ∀ i j k l m : Fin 3, -S5 0 i j k l m + S5 1 i j k l m - S5 3 i j k l m + S5 6 i j k l m = 0 := by decide +kernel

/-- a kernel relation among the ten `εδ` candidates (exhibited; there are four, so the span is 6-dimensional) -/
theorem ker5_7 : ∀ i j k l m : Fin 3, -S5 0 i j k l m + S5 2 i j k l m - S5 4 i j k l m + S5 7 i j k l m = 0 := by decide +kernel

/-- a kernel relation among the ten `εδ` candidates (exhibited; there are four, so the span is 6-dimensional) -/
theorem ker5_8 : ∀ i j k l m : Fin 3, -S5 1 i j k l m + S5 2 i j k l m - S5 5 i j k l m + S5 8 i j k l m = 0 := by decide +kernel

/-- a kernel relation among the ten `εδ` candidates (exhibited; there are four, so the span is 6-dimensional) -/
theorem ker5_9 : ∀ i j k l m : Fin 3, -S5 3 i j k l m + S5 4 i j k l m - S5 5 i j k l m + S5 9 i j k l m = 0 := by decide +kernel

/-- ⛭ **(A1) rank 4, within the candidate span.** Every rational combination of the three `δδ` candidates that
satisfies the five conditions is a multiple of `P6`: the solution space is spanned by `P`. -/
theorem cert4 (z : Fin 3 → ℚ) (h : CondA (T4 z)) :
    ∀ i j k l : Fin 3, T4 z i j k l = z 2 / 3 * (P6 i j k l : ℚ) := by
  obtain ⟨h1, h2, h3, h4, h5⟩ := h
  have e0 := h1 0 1 0 1
  have e1 := h3 0 0
  simp [T4, S4, dl, ee, S3] at e0 e1
  have hz0 : z 0 = -2*z 2/3 := by linarith
  have hz1 : z 1 = z 2 := by linarith
  intro i j k l
  simp only [T4, hz0, hz1]; push_cast [P6]; ring

/-- ⛭ **(A2) rank 5, within the candidate span.** The ten `εδ` candidates span only six dimensions (the four
kernel relations above). Every combination satisfying the five conditions equals `z₄ · B0`: the solution space is spanned by `B0`. -/
theorem cert5 (z : Fin 10 → ℚ) (h : CondB (T5 z)) :
    ∀ i j k l m : Fin 3, T5 z i j k l m = (z 4 + z 7 - z 9) * (B0 i j k l m : ℚ) := by
  obtain ⟨h1, h2, h3, h4, h5⟩ := h
  have e0 := h1 0 0 1 0 2
  have e1 := h1 0 0 1 2 0
  have e2 := h1 0 1 2 0 0
  have e3 := h2 0 0 0 1 2
  have e4 := h2 0 0 1 0 2
  simp [T5, S5, dl, ee, S3] at e0 e1 e2 e3 e4
  have hz0 : z 0 = -z 6 - z 7 := by linarith
  have hz1 : z 1 = z 4 + z 6 + z 7 - z 8 - z 9 := by linarith
  have hz2 : z 2 = z 4 + 2*z 7 + z 8 - z 9 := by linarith
  have hz3 : z 3 = z 4 - z 6 + z 7 - 2*z 9 := by linarith
  have hz5 : z 5 = -z 8 - z 9 := by linarith
  intro i j k l m
  have k6 := congrArg (Int.cast : ℤ → ℚ) (ker5_6 i j k l m); push_cast at k6
  have k7 := congrArg (Int.cast : ℤ → ℚ) (ker5_7 i j k l m); push_cast at k7
  have k8 := congrArg (Int.cast : ℤ → ℚ) (ker5_8 i j k l m); push_cast at k8
  have k9 := congrArg (Int.cast : ℤ → ℚ) (ker5_9 i j k l m); push_cast at k9
  simp only [T5, B0, hz0, hz1, hz2, hz3, hz5]; push_cast
  linear_combination z 6 * k6 + z 7 * k7 + z 8 * k8 + z 9 * k9

/-- ⛭ **(A3) rank 6, within the candidate span.** Every combination of the fifteen `δδδ` candidates satisfying
the six conditions is `x · C1i + y · C2i`: the solution space is spanned by the two. -/
theorem cert6 (z : Fin 15 → ℚ) (h : CondC (T6 z)) :
    ∀ i j k l m q : Fin 3, T6 z i j k l m q = z 14 / 8 * (C1i i j k l m q : ℚ) + (z 12 / 2 + 3 * z 14 / 8) * (C2i i j k l m q : ℚ) := by
  obtain ⟨h1, h2, h3, h4, h5, h6⟩ := h
  have e0 := h1 0 0 1 0 0 1
  have e1 := h1 0 0 1 0 1 0
  have e2 := h1 0 0 1 1 0 0
  have e3 := h1 0 0 1 1 2 2
  have e4 := h1 0 0 1 2 1 2
  have e5 := h1 0 1 2 0 1 2
  have e6 := h2 0 0 0 1 0 1
  have e7 := h2 0 0 1 0 0 1
  have e8 := h2 0 0 1 2 1 2
  have e9 := h3 0 0 0 0
  have e10 := h3 0 0 1 1
  have e11 := h4 0 0 0 0
  have e12 := h6 0 0 0 0
  simp [T6, S6, dl, ee, S3] at e0 e1 e2 e3 e4 e5 e6 e7 e8 e9 e10 e11 e12
  have hz0 : z 0 = z 12 := by linarith
  have hz1 : z 1 = -3*z 12/2 - z 14 := by linarith
  have hz2 : z 2 = -3*z 12/2 - z 14 := by linarith
  have hz3 : z 3 = z 12 := by linarith
  have hz4 : z 4 = -3*z 12/2 - z 14 := by linarith
  have hz5 : z 5 = -3*z 12/2 - z 14 := by linarith
  have hz6 : z 6 = -4*z 12 - 2*z 14 := by linarith
  have hz7 : z 7 = 5*z 12 + 3*z 14 := by linarith
  have hz8 : z 8 = 5*z 12 + 3*z 14 := by linarith
  have hz9 : z 9 = z 12 := by linarith
  have hz10 : z 10 = z 14 := by linarith
  have hz11 : z 11 = z 14 := by linarith
  have hz13 : z 13 = z 14 := by linarith
  intro i j k l m q
  simp only [T6, hz0, hz1, hz2, hz3, hz4, hz5, hz6, hz7, hz8, hz9, hz10, hz11, hz13]; push_cast [C1i, C2i]; ring

/-- the nonzero `2 × 2` minor: `C1i` and `C2i` are linearly independent -/
theorem C_minor : C1i 0 0 0 0 0 0 * C2i 0 0 1 0 0 1 - C1i 0 0 1 0 0 1 * C2i 0 0 0 0 0 0 ≠ 0 := by decide +kernel

/-! ### sufficiency: the basis satisfies every condition, componentwise -/

theorem P6_cond : CondA P6 := by unfold CondA; decide +kernel
theorem B0_cond : CondB B0 := by unfold CondB; decide +kernel
theorem C1i_cond : CondC C1i := by unfold CondC; decide +kernel
theorem C2i_cond : CondC C2i := by unfold CondC; decide +kernel

/-- `tr P = 5`, i.e. `Σ P6_ijij = 30` -/
theorem P6_trace : S3 (fun i => S3 (fun j => P6 i j i j)) = 30 := by decide +kernel
/-- the trace relation's integer content: `Σ_a C1i_{aij,akl} = 0`, `Σ_a C2i_{aij,akl} = 8 P6_ijkl` -/
theorem C1i_tr : ∀ i j k l, S3 (fun a => C1i a i j a k l) = 0 := by decide +kernel
theorem C2i_tr : ∀ i j k l, S3 (fun a => C2i a i j a k l) = 8 * P6 i j k l := by decide +kernel
/-- the full traces: `Σ C1i_{aij,aij} = 0`, `Σ C2i_{aij,aij} = 240` -/
theorem C1i_full : S3 (fun a => S3 (fun i => S3 (fun j => C1i a i j a i j))) = 0 := by decide +kernel
theorem C2i_full : S3 (fun a => S3 (fun i => S3 (fun j => C2i a i j a i j))) = 240 := by decide +kernel
theorem nonzero_P_B : P6 0 0 0 0 = 4 ∧ B0 0 0 1 0 2 = 1 := by decide +kernel

/-! ### the level tensors, with the receipt's normalisations -/

/-- `P_ijkl` over `ℝ` -/
def Pr (i j k l : Fin 3) : ℝ := (P6 i j k l : ℝ) / 6

/-- the rank-4 level tensor `A = (deg/5) P` -/
def Aten (deg : ℝ) (i j k l : Fin 3) : ℝ := deg / 30 * (P6 i j k l : ℝ)

/-- the rank-5 level tensor `B = c_B · B0` -/
def Bten (cB : ℝ) (i j k l m : Fin 3) : ℝ := cB * (B0 i j k l m : ℝ)

/-- the rank-6 level tensor `C = c_C C1 + λ·deg C2`, with `C1 = C1i/8` and `C2 = C2i/240` -/
def Cten (cC lam deg : ℝ) (i j k l m q : Fin 3) : ℝ :=
  cC / 8 * (C1i i j k l m q : ℝ) + lam * deg / 240 * (C2i i j k l m q : ℝ)

theorem S3_real {f : Fin 3 → ℤ} : S3 (fun i => (f i : ℝ)) = ((S3 f : ℤ) : ℝ) := by
  simp only [S3]; push_cast; ring

/-- ⛭ **(A4) THE TRACE RELATION FIXES EXACTLY ONE OF C'S TWO NUMBERS.** On the solution family `x·C1 + y·C2`,
`Σ_a C_{aij,akl} = (L/5) P_ijkl` holds for every `ijkl` if and only if `y = L`. -/
theorem trace_relation_fixes (x y L : ℝ) :
    (∀ i j k l, S3 (fun a => x / 8 * (C1i a i j a k l : ℝ) + y / 240 * (C2i a i j a k l : ℝ)) = L / 5 * Pr i j k l)
      ↔ y = L := by
  have key : ∀ i j k l, S3 (fun a => x / 8 * (C1i a i j a k l : ℝ) + y / 240 * (C2i a i j a k l : ℝ))
      = y / 30 * (P6 i j k l : ℝ) := by
    intro i j k l
    have h1 := congrArg (Int.cast : ℤ → ℝ) (C1i_tr i j k l)
    have h2 := congrArg (Int.cast : ℤ → ℝ) (C2i_tr i j k l)
    simp only [S3] at h1 h2 ⊢; push_cast at h1 h2
    linear_combination x / 8 * h1 + y / 240 * h2
  constructor
  · intro h
    have e := h 0 0 0 0
    rw [key] at e
    have hp : (P6 0 0 0 0 : ℝ) = 4 := by exact_mod_cast nonzero_P_B.1
    simp only [Pr, hp] at e
    linarith
  · rintro rfl i j k l
    rw [key]; simp only [Pr]; ring

/-- the full traces of the level tensors: `tr C = λ·deg` for **every** `c_C`, and `tr A = deg` -/
theorem full_traces (cC lam deg : ℝ) :
    S3 (fun a => S3 (fun i => S3 (fun j => Cten cC lam deg a i j a i j))) = lam * deg ∧
      S3 (fun i => S3 (fun j => Aten deg i j i j)) = deg ∧
      S3 (fun i => S3 (fun j => Pr i j i j)) = 5 := by
  have h1 := congrArg (Int.cast : ℤ → ℝ) C1i_full
  have h2 := congrArg (Int.cast : ℤ → ℝ) C2i_full
  have h3 := congrArg (Int.cast : ℤ → ℝ) P6_trace
  simp only [S3] at h1 h2 h3; push_cast at h1 h2 h3
  refine ⟨?_, ?_, ?_⟩ <;> simp only [Cten, Aten, Pr, S3]
  · linear_combination cC / 8 * h1 + lam * deg / 240 * h2
  · linear_combination deg / 30 * h3
  · linear_combination h3 / 6

/-- the level tensors satisfy their conditions for all values of the numbers (linearity) -/
theorem level_tensors_cond (cC cB lam deg : ℝ) :
    CondA (Aten deg) ∧ CondB (Bten cB) ∧ CondC (Cten cC lam deg) := by
  obtain ⟨a1, a2, a3, a4, a5⟩ := P6_cond
  obtain ⟨b1, b2, b3, b4, b5⟩ := B0_cond
  obtain ⟨c1, c2, c3, c4, c5, c6⟩ := C1i_cond
  obtain ⟨d1, d2, d3, d4, d5, d6⟩ := C2i_cond
  refine ⟨⟨?_, ?_, ?_, ?_, ?_⟩, ⟨?_, ?_, ?_, ?_, ?_⟩, ⟨?_, ?_, ?_, ?_, ?_, ?_⟩⟩
  · intro i j k l; simp only [Aten, a1 i j k l]
  · intro i j k l; simp only [Aten, a2 i j k l]
  · intro i j; have := congrArg (Int.cast : ℤ → ℝ) (a3 i j); simp only [S3, Aten] at this ⊢; push_cast at this
    linear_combination deg / 30 * this
  · intro i j; have := congrArg (Int.cast : ℤ → ℝ) (a4 i j); simp only [S3, Aten] at this ⊢; push_cast at this
    linear_combination deg / 30 * this
  · intro i j k l; simp only [Aten, a5 i j k l]
  · intro a i j k l; simp only [Bten, b1 a i j k l]
  · intro a i j k l; simp only [Bten, b2 a i j k l]
  · intro a i j; have := congrArg (Int.cast : ℤ → ℝ) (b3 a i j); simp only [S3, Bten] at this ⊢
    push_cast at this; linear_combination cB * this
  · intro a i j; have := congrArg (Int.cast : ℤ → ℝ) (b4 a i j); simp only [S3, Bten] at this ⊢
    push_cast at this; linear_combination cB * this
  · intro a i j; have := congrArg (Int.cast : ℤ → ℝ) (b5 a i j); simp only [S3, Bten] at this ⊢
    push_cast at this; linear_combination cB * this
  · intro a i j b k l; simp only [Cten, c1 a i j b k l, d1 a i j b k l]
  · intro a i j b k l; simp only [Cten, c2 a i j b k l, d2 a i j b k l]
  · intro a b i j
    have h1 := congrArg (Int.cast : ℤ → ℝ) (c3 a b i j); have h2 := congrArg (Int.cast : ℤ → ℝ) (d3 a b i j)
    simp only [S3, Cten] at h1 h2 ⊢; push_cast at h1 h2
    linear_combination cC / 8 * h1 + lam * deg / 240 * h2
  · intro a i j b
    have h1 := congrArg (Int.cast : ℤ → ℝ) (c4 a i j b); have h2 := congrArg (Int.cast : ℤ → ℝ) (d4 a i j b)
    simp only [S3, Cten] at h1 h2 ⊢; push_cast at h1 h2
    linear_combination cC / 8 * h1 + lam * deg / 240 * h2
  · intro a i j b k l; simp only [Cten, c5 a i j b k l, d5 a i j b k l]
  · intro j b l n
    have h1 := congrArg (Int.cast : ℤ → ℝ) (c6 j b l n); have h2 := congrArg (Int.cast : ℤ → ℝ) (d6 j b l n)
    simp only [S3, Cten] at h1 h2 ⊢; push_cast at h1 h2
    linear_combination cC / 8 * h1 + lam * deg / 240 * h2

/-- ⛭ **(A) THE INVARIANT BASIS AND ITS DIMENSIONS `(1, 1, 2)`, WITHIN THE CANDIDATE SPAN.**
- *Sufficiency:* `P`, `B0`, `C1`, `C2` (built from `δ` and `ε`) satisfy every condition, componentwise.
- *Rank certificate:* every rational combination of the candidates that satisfies the conditions is a multiple of
  `P` (rank 4) or of `B0` (rank 5), or a combination of `C1, C2` (rank 6). The basis is nonzero, and `C1, C2` have a
  nonzero minor.
- *Trace relation:* it fixes exactly one of `C`'s two numbers; `tr C = λ·deg` for every value of the other; and
  `A = (deg/5)P` with `tr P = 5`.

Completeness of the `δ/ε` candidate span is not claimed. -/
theorem invariant_basis :
    (CondA P6 ∧ CondB B0 ∧ CondC C1i ∧ CondC C2i) ∧
    (∀ z, CondA (T4 z) → ∀ i j k l, T4 z i j k l = z 2 / 3 * (P6 i j k l : ℚ)) ∧
    (∀ z, CondB (T5 z) → ∀ i j k l m, T5 z i j k l m = (z 4 + z 7 - z 9) * (B0 i j k l m : ℚ)) ∧
    (∀ z, CondC (T6 z) → ∀ i j k l m q,
      T6 z i j k l m q = z 14 / 8 * (C1i i j k l m q : ℚ) + (z 12 / 2 + 3 * z 14 / 8) * (C2i i j k l m q : ℚ)) ∧
    (P6 0 0 0 0 ≠ 0 ∧ B0 0 0 1 0 2 ≠ 0 ∧
      C1i 0 0 0 0 0 0 * C2i 0 0 1 0 0 1 - C1i 0 0 1 0 0 1 * C2i 0 0 0 0 0 0 ≠ 0) ∧
    (∀ x y L : ℝ, (∀ i j k l, S3 (fun a => x / 8 * (C1i a i j a k l : ℝ) + y / 240 * (C2i a i j a k l : ℝ))
      = L / 5 * Pr i j k l) ↔ y = L) ∧
    (∀ cC lam deg : ℝ, S3 (fun a => S3 (fun i => S3 (fun j => Cten cC lam deg a i j a i j))) = lam * deg) ∧
    (∀ deg : ℝ, S3 (fun i => S3 (fun j => Aten deg i j i j)) = deg) ∧
    S3 (fun i => S3 (fun j => Pr i j i j)) = 5 :=
  ⟨⟨P6_cond, B0_cond, C1i_cond, C2i_cond⟩, cert4, cert5, cert6,
    ⟨by rw [nonzero_P_B.1]; norm_num, by rw [nonzero_P_B.2]; norm_num, C_minor⟩,
    trace_relation_fixes, fun cC lam deg => (full_traces cC lam deg).1,
    fun deg => (full_traces 0 0 deg).2.1, (full_traces 0 0 0).2.2⟩

#print axioms invariant_basis

/-! ## (B) the second-order identity on the TT variety

### row 62's frame-jet machine, copied verbatim from `probes/Row62Jet.lean` (orders `0..2` only)

The definitions, the order-`0..2` tables and their layer lemmas are copied unchanged. The only edits: the simp
lists of `Gam_k`/`Ric_k` no longer name the order-3 lemmas (not copied), and `jet_series` is restated as
`jet_series_le2` for orders `0..2`, which is all Part B needs. -/

namespace Jet

/-- three derivations on a characteristic-zero field: additive, Leibniz, and killing the rationals -/
structure FD (K : Type*) [Field K] where
  D : Fin 3 → K → K
  add : ∀ a x y, D a (x + y) = D a x + D a y
  mul : ∀ a x y, D a (x * y) = D a x * y + x * D a y
  rat : ∀ a (q : ℚ), D a (q : K) = 0

variable {K : Type*} [Field K] [CharZero K] (F : FD K)

theorem FD.zero (a) : F.D a 0 = 0 := by simpa using F.rat a 0
theorem FD.neg (a x) : F.D a (-x) = -F.D a x := by
  have := F.add a x (-x); simp [F.zero] at this; linear_combination -this
theorem FD.sub (a x y) : F.D a (x - y) = F.D a x - F.D a y := by
  rw [sub_eq_add_neg, F.add, F.neg, ← sub_eq_add_neg]
theorem FD.ofNat (a) (n : ℕ) [n.AtLeastTwo] : F.D a (OfNat.ofNat n : K) = 0 := by
  simpa using F.rat a (OfNat.ofNat n)
theorem FD.one (a) : F.D a (1 : K) = 0 := by simpa using F.rat a 1
theorem FD.inv_ofNat (a) (n : ℕ) [n.AtLeastTwo] : F.D a ((OfNat.ofNat n : K)⁻¹) = 0 := by
  simpa [Rat.cast_inv] using F.rat a ((OfNat.ofNat n : ℚ))⁻¹
theorem FD.div_ofNat (a x) (n : ℕ) [n.AtLeastTwo] :
    F.D a (x / (OfNat.ofNat n : K)) = F.D a x / (OfNat.ofNat n : K) := by
  rw [div_eq_mul_inv, F.mul, F.inv_ofNat]; ring
theorem FD.div_one' (a x) : F.D a (x / (1 : K)) = F.D a x := by simp
theorem FD.sq (a x) : F.D a (x ^ 2) = 2 * x * F.D a x := by rw [pow_two, F.mul]; ring
theorem FD.cube (a x) : F.D a (x ^ 3) = 3 * x ^ 2 * F.D a x := by
  rw [pow_succ, F.mul, FD.sq]; ring
theorem FD.quart (a x) : F.D a (x ^ 4) = 4 * x ^ 3 * F.D a x := by
  rw [pow_succ, F.mul, FD.cube]; ring
theorem FD.pow (a x) : ∀ n : ℕ, F.D a (x ^ (n + 1)) = (n + 1) * x ^ n * F.D a x
  | 0 => by simp
  | n + 1 => by rw [pow_succ, F.mul, FD.pow a x n]; push_cast; ring

/-- the structure constants `[X_a, X_b] = c^m_ab X_m`, `c^m_ab = 2 ε_abm` -/
def cst (m a b : Fin 3) : K := 2 * (Matrix.of ![![![0, 0, 0], ![0, 0, 1], ![0, -1, 0]],
  ![![0, 0, -1], ![0, 0, 0], ![1, 0, 0]], ![![0, 1, 0], ![-1, 0, 0], ![0, 0, 0]]] a b m : K)

/-- `(L_a)_kj = −2 ε_akj` : `D_a u_j = Σ_k u_k (L_a)_kj` -/
def Lm (a k j : Fin 3) : K := -2 * (Matrix.of ![![![0, 0, 0], ![0, 0, 1], ![0, -1, 0]],
  ![![0, 0, -1], ![0, 0, 0], ![1, 0, 0]], ![![0, 1, 0], ![-1, 0, 0], ![0, 0, 0]]] a k j : K)


/-- the symmetric traceless matrix of five coordinates -/
def Hm (v : Fin 5 → K) : Matrix (Fin 3) (Fin 3) K := !![v 0, v 2, v 3; v 2, v 1, v 4; v 3, v 4, -v 0 - v 1]

/-- the coordinates of `D_a D_c H`: the symmetric part `s`, and the antisymmetric part `ε_acm D_m H` the frame
commutator fixes -/
def DDt (d : Fin 3 → Fin 5 → K) (s : Fin 3 → Fin 3 → Fin 5 → K) : Fin 3 → Fin 3 → Fin 5 → K :=
  ![![fun i => s 0 0 i, fun i => s 0 1 i + d 2 i, fun i => s 0 2 i - d 1 i],
    ![fun i => s 0 1 i - d 2 i, fun i => s 1 1 i, fun i => s 1 2 i + d 0 i],
    ![fun i => s 0 2 i + d 1 i, fun i => s 1 2 i - d 0 i, fun i => s 2 2 i]]

/-- `Hᵏ` -/
def Pw (h : Fin 5 → K) : ℕ → Matrix (Fin 3) (Fin 3) K
  | 0 => 1
  | k + 1 => Pw h k * Hm h

def Gk (h : Fin 5 → K) (k : ℕ) (a b : Fin 3) : K := Pw h k a b / k.factorial
def Gik (h : Fin 5 → K) (k : ℕ) (a b : Fin 3) : K := (-1) ^ k * Pw h k a b / k.factorial

def Gl (h : Fin 5 → K) (k : ℕ) (a b c : Fin 3) : K :=
  (F.D a (Gk h k b c) + F.D b (Gk h k a c) - F.D c (Gk h k a b)
    + ∑ m, (cst m a b * Gk h k m c - cst m b c * Gk h k m a + cst m c a * Gk h k m b)) / 2

def Gam (h : Fin 5 → K) (k : ℕ) (d a b : Fin 3) : K :=
  ∑ i ∈ range (k + 1), ∑ c, Gik h i d c * Gl F h (k - i) a b c

def Rm (h : Fin 5 → K) (k : ℕ) (d a b c : Fin 3) : K :=
  F.D a (Gam F h k d b c) - F.D b (Gam F h k d a c)
    + ∑ i ∈ range (k + 1), ∑ e, (Gam F h i e b c * Gam F h (k - i) d a e
        - Gam F h i e a c * Gam F h (k - i) d b e)
    - ∑ m, cst m a b * Gam F h k d m c

def Ric (h : Fin 5 → K) (k : ℕ) (b c : Fin 3) : K := ∑ a, Rm F h k a a b c

def Scal (h : Fin 5 → K) (k : ℕ) : K :=
  ∑ i ∈ range (k + 1), ∑ b, ∑ c, Gik h i b c * Ric F h (k - i) b c

/-! ### the tables (sympy-generated; each proved below from the layer under it) -/


def gkT0 (h : Fin 5 → K) : Fin 3 → Fin 3 → K :=
  ![![(1), 0, 0],
    ![0, (1), 0],
    ![0, 0, (1)]]

def gikT0 (h : Fin 5 → K) : Fin 3 → Fin 3 → K :=
  ![![(1), 0, 0],
    ![0, (1), 0],
    ![0, 0, (1)]]

def glT0 (h : Fin 5 → K) (d : Fin 3 → Fin 5 → K) : Fin 3 → Fin 3 → Fin 3 → K :=
  ![![![0, 0, 0],
    ![0, 0, (1)],
    ![0, (-1), 0]],
   ![![0, 0, (-1)],
    ![0, 0, 0],
    ![(1), 0, 0]],
   ![![0, (1), 0],
    ![(-1), 0, 0],
    ![0, 0, 0]]]

def gamT0 (h : Fin 5 → K) (d : Fin 3 → Fin 5 → K) : Fin 3 → Fin 3 → Fin 3 → K :=
  ![![![0, 0, 0],
    ![0, 0, (1)],
    ![0, (-1), 0]],
   ![![0, 0, (-1)],
    ![0, 0, 0],
    ![(1), 0, 0]],
   ![![0, (1), 0],
    ![(-1), 0, 0],
    ![0, 0, 0]]]

def ricT0 (h : Fin 5 → K) (d : Fin 3 → Fin 5 → K) (s : Fin 3 → Fin 3 → Fin 5 → K) : Fin 3 → Fin 3 → K :=
  ![![(2), 0, 0],
    ![0, (2), 0],
    ![0, 0, (2)]]

def gkT1 (h : Fin 5 → K) : Fin 3 → Fin 3 → K :=
  ![![(h 0), (h 2), (h 3)],
    ![(h 2), (h 1), (h 4)],
    ![(h 3), (h 4), (-h 0 - h 1)]]

def gikT1 (h : Fin 5 → K) : Fin 3 → Fin 3 → K :=
  ![![(-h 0), (-h 2), (-h 3)],
    ![(-h 2), (-h 1), (-h 4)],
    ![(-h 3), (-h 4), (h 0 + h 1)]]

def glT1 (h : Fin 5 → K) (d : Fin 3 → Fin 5 → K) : Fin 3 → Fin 3 → Fin 3 → K :=
  ![![![((1/2) * d 0 0), (d 0 2 - 2 * h 3 - (1/2) * d 1 0), (d 0 3 + 2 * h 2 - (1/2) * d 2 0)],
    ![((1/2) * d 1 0 + 2 * h 3), ((1/2) * d 0 1), ((1/2) * d 0 4 + (1/2) * d 1 3 - 2 * h 0 - (1/2) * d 2 2)],
    ![((1/2) * d 2 0 - 2 * h 2), ((1/2) * d 0 4 + (1/2) * d 2 2 + 2 * h 0 - (1/2) * d 1 3), (-(1/2) * d 0 0 - (1/2) * d 0 1)]],
   ![![((1/2) * d 1 0), ((1/2) * d 0 1 - 2 * h 4), ((1/2) * d 0 4 + (1/2) * d 1 3 + 2 * h 1 - (1/2) * d 2 2)],
    ![(d 1 2 + 2 * h 4 - (1/2) * d 0 1), ((1/2) * d 1 1), (d 1 4 - 2 * h 2 - (1/2) * d 2 1)],
    ![((1/2) * d 1 3 + (1/2) * d 2 2 - 2 * h 1 - (1/2) * d 0 4), ((1/2) * d 2 1 + 2 * h 2), (-(1/2) * d 1 0 - (1/2) * d 1 1)]],
   ![![((1/2) * d 2 0), ((1/2) * d 0 4 + (1/2) * d 2 2 + 2 * h 0 + 2 * h 1 - (1/2) * d 1 3), (2 * h 4 - (1/2) * d 0 0 - (1/2) * d 0 1)],
    ![((1/2) * d 1 3 + (1/2) * d 2 2 - 2 * h 0 - 2 * h 1 - (1/2) * d 0 4), ((1/2) * d 2 1), (-2 * h 3 - (1/2) * d 1 0 - (1/2) * d 1 1)],
    ![(d 2 3 + (1/2) * d 0 0 + (1/2) * d 0 1 - 2 * h 4), (d 2 4 + (1/2) * d 1 0 + (1/2) * d 1 1 + 2 * h 3), (-(1/2) * d 2 0 - (1/2) * d 2 1)]]]

def gamT1 (h : Fin 5 → K) (d : Fin 3 → Fin 5 → K) : Fin 3 → Fin 3 → Fin 3 → K :=
  ![![![((1/2) * d 0 0), (h 3 + (1/2) * d 1 0), ((1/2) * d 2 0 - h 2)],
    ![(h 3 + (1/2) * d 1 0), (d 1 2 + 2 * h 4 - (1/2) * d 0 1), ((1/2) * d 1 3 + (1/2) * d 2 2 - h 0 - 2 * h 1 - (1/2) * d 0 4)],
    ![((1/2) * d 2 0 - h 2), ((1/2) * d 1 3 + (1/2) * d 2 2 - h 0 - 2 * h 1 - (1/2) * d 0 4), (d 2 3 + (1/2) * d 0 0 + (1/2) * d 0 1 - 2 * h 4)]],
   ![![(d 0 2 - 2 * h 3 - (1/2) * d 1 0), ((1/2) * d 0 1 - h 4), (h 1 + (1/2) * d 0 4 + (1/2) * d 2 2 + 2 * h 0 - (1/2) * d 1 3)],
    ![((1/2) * d 0 1 - h 4), ((1/2) * d 1 1), (h 2 + (1/2) * d 2 1)],
    ![(h 1 + (1/2) * d 0 4 + (1/2) * d 2 2 + 2 * h 0 - (1/2) * d 1 3), (h 2 + (1/2) * d 2 1), (d 2 4 + (1/2) * d 1 0 + (1/2) * d 1 1 + 2 * h 3)]],
   ![![(d 0 3 + 2 * h 2 - (1/2) * d 2 0), (h 1 + (1/2) * d 0 4 + (1/2) * d 1 3 - h 0 - (1/2) * d 2 2), (h 4 - (1/2) * d 0 0 - (1/2) * d 0 1)],
    ![(h 1 + (1/2) * d 0 4 + (1/2) * d 1 3 - h 0 - (1/2) * d 2 2), (d 1 4 - 2 * h 2 - (1/2) * d 2 1), (-h 3 - (1/2) * d 1 0 - (1/2) * d 1 1)],
    ![(h 4 - (1/2) * d 0 0 - (1/2) * d 0 1), (-h 3 - (1/2) * d 1 0 - (1/2) * d 1 1), (-(1/2) * d 2 0 - (1/2) * d 2 1)]]]

def ricT1 (h : Fin 5 → K) (d : Fin 3 → Fin 5 → K) (s : Fin 3 → Fin 3 → Fin 5 → K) : Fin 3 → Fin 3 → K :=
  ![![(s 0 1 2 + s 0 2 3 + (1/2) * s 0 0 0 - 3 * d 1 3 + 3 * d 2 2 + 6 * h 0 - (1/2) * s 1 1 0 - (1/2) * s 2 2 0), ((1/2) * s 0 1 0 + (1/2) * s 0 1 1 + (1/2) * s 0 2 4 + (1/2) * s 1 2 3 + 6 * h 2 - (3/2) * d 1 4 - (3/2) * d 2 0 - (1/2) * s 2 2 2 + (3/2) * d 0 3 + (3/2) * d 2 1), ((1/2) * s 0 1 4 + (1/2) * s 1 2 2 + 3 * d 1 0 + 6 * h 3 - (3/2) * d 0 2 - (1/2) * s 0 2 1 - (1/2) * s 1 1 3 + (3/2) * d 1 1 + (3/2) * d 2 4)],
    ![((1/2) * s 0 1 0 + (1/2) * s 0 1 1 + (1/2) * s 0 2 4 + (1/2) * s 1 2 3 + 6 * h 2 - (3/2) * d 1 4 - (3/2) * d 2 0 - (1/2) * s 2 2 2 + (3/2) * d 0 3 + (3/2) * d 2 1), (s 0 1 2 + s 1 2 4 + (1/2) * s 1 1 1 - 3 * d 2 2 + 3 * d 0 4 + 6 * h 1 - (1/2) * s 0 0 1 - (1/2) * s 2 2 1), ((1/2) * s 0 1 3 + (1/2) * s 0 2 2 - 3 * d 0 1 + 6 * h 4 - (3/2) * d 0 0 - (3/2) * d 2 3 - (1/2) * s 0 0 4 - (1/2) * s 1 2 0 + (3/2) * d 1 2)],
    ![((1/2) * s 0 1 4 + (1/2) * s 1 2 2 + 3 * d 1 0 + 6 * h 3 - (3/2) * d 0 2 - (1/2) * s 0 2 1 - (1/2) * s 1 1 3 + (3/2) * d 1 1 + (3/2) * d 2 4), ((1/2) * s 0 1 3 + (1/2) * s 0 2 2 - 3 * d 0 1 + 6 * h 4 - (3/2) * d 0 0 - (3/2) * d 2 3 - (1/2) * s 0 0 4 - (1/2) * s 1 2 0 + (3/2) * d 1 2), (s 0 2 3 + s 1 2 4 + (1/2) * s 0 0 0 + (1/2) * s 0 0 1 + (1/2) * s 1 1 0 + (1/2) * s 1 1 1 - 6 * h 0 - 6 * h 1 - 3 * d 0 4 + 3 * d 1 3 - (1/2) * s 2 2 0 - (1/2) * s 2 2 1)]]

def gkT2 (h : Fin 5 → K) : Fin 3 → Fin 3 → K :=
  ![![((1/2) * (h 0) ^ (2:ℕ) + (1/2) * (h 2) ^ (2:ℕ) + (1/2) * (h 3) ^ (2:ℕ)), ((1/2) * h 0 * h 2 + (1/2) * h 1 * h 2 + (1/2) * h 3 * h 4), ((1/2) * h 2 * h 4 - (1/2) * h 1 * h 3)],
    ![((1/2) * h 0 * h 2 + (1/2) * h 1 * h 2 + (1/2) * h 3 * h 4), ((1/2) * (h 1) ^ (2:ℕ) + (1/2) * (h 2) ^ (2:ℕ) + (1/2) * (h 4) ^ (2:ℕ)), ((1/2) * h 2 * h 3 - (1/2) * h 0 * h 4)],
    ![((1/2) * h 2 * h 4 - (1/2) * h 1 * h 3), ((1/2) * h 2 * h 3 - (1/2) * h 0 * h 4), ((1/2) * (h 0) ^ (2:ℕ) + (1/2) * (h 1) ^ (2:ℕ) + (1/2) * (h 3) ^ (2:ℕ) + (1/2) * (h 4) ^ (2:ℕ) + h 0 * h 1)]]

def gikT2 (h : Fin 5 → K) : Fin 3 → Fin 3 → K :=
  ![![((1/2) * (h 0) ^ (2:ℕ) + (1/2) * (h 2) ^ (2:ℕ) + (1/2) * (h 3) ^ (2:ℕ)), ((1/2) * h 0 * h 2 + (1/2) * h 1 * h 2 + (1/2) * h 3 * h 4), ((1/2) * h 2 * h 4 - (1/2) * h 1 * h 3)],
    ![((1/2) * h 0 * h 2 + (1/2) * h 1 * h 2 + (1/2) * h 3 * h 4), ((1/2) * (h 1) ^ (2:ℕ) + (1/2) * (h 2) ^ (2:ℕ) + (1/2) * (h 4) ^ (2:ℕ)), ((1/2) * h 2 * h 3 - (1/2) * h 0 * h 4)],
    ![((1/2) * h 2 * h 4 - (1/2) * h 1 * h 3), ((1/2) * h 2 * h 3 - (1/2) * h 0 * h 4), ((1/2) * (h 0) ^ (2:ℕ) + (1/2) * (h 1) ^ (2:ℕ) + (1/2) * (h 3) ^ (2:ℕ) + (1/2) * (h 4) ^ (2:ℕ) + h 0 * h 1)]]

def glT2 (h : Fin 5 → K) (d : Fin 3 → Fin 5 → K) : Fin 3 → Fin 3 → Fin 3 → K :=
  ![![![((1/2) * d 0 0 * h 0 + (1/2) * d 0 2 * h 2 + (1/2) * d 0 3 * h 3), (h 1 * h 3 + (1/2) * d 0 0 * h 2 + (1/2) * d 0 1 * h 2 + (1/2) * d 0 2 * h 0 + (1/2) * d 0 2 * h 1 + (1/2) * d 0 3 * h 4 + (1/2) * d 0 4 * h 3 - h 2 * h 4 - (1/2) * d 1 0 * h 0 - (1/2) * d 1 2 * h 2 - (1/2) * d 1 3 * h 3), (h 0 * h 2 + h 1 * h 2 + h 3 * h 4 + (1/2) * d 0 2 * h 4 + (1/2) * d 0 4 * h 2 - (1/2) * d 0 1 * h 3 - (1/2) * d 0 3 * h 1 - (1/2) * d 2 0 * h 0 - (1/2) * d 2 2 * h 2 - (1/2) * d 2 3 * h 3)],
    ![(h 2 * h 4 + (1/2) * d 1 0 * h 0 + (1/2) * d 1 2 * h 2 + (1/2) * d 1 3 * h 3 - h 1 * h 3), ((1/2) * d 0 1 * h 1 + (1/2) * d 0 2 * h 2 + (1/2) * d 0 4 * h 4), ((h 1) ^ (2:ℕ) + (h 4) ^ (2:ℕ) + h 0 * h 1 - (1/4) * d 0 0 * h 4 - (1/4) * d 0 4 * h 0 - (1/4) * d 1 1 * h 3 - (1/4) * d 1 3 * h 1 - (1/4) * d 2 0 * h 2 - (1/4) * d 2 1 * h 2 - (1/4) * d 2 2 * h 0 - (1/4) * d 2 2 * h 1 - (1/4) * d 2 3 * h 4 - (1/4) * d 2 4 * h 3 + (1/4) * d 0 2 * h 3 + (1/4) * d 0 3 * h 2 + (1/4) * d 1 2 * h 4 + (1/4) * d 1 4 * h 2)],
    ![((1/2) * d 2 0 * h 0 + (1/2) * d 2 2 * h 2 + (1/2) * d 2 3 * h 3 - h 0 * h 2 - h 1 * h 2 - h 3 * h 4), (-(h 1) ^ (2:ℕ) - (h 4) ^ (2:ℕ) - h 0 * h 1 - (1/4) * d 0 0 * h 4 - (1/4) * d 0 4 * h 0 - (1/4) * d 1 2 * h 4 - (1/4) * d 1 4 * h 2 + (1/4) * d 0 2 * h 3 + (1/4) * d 0 3 * h 2 + (1/4) * d 1 1 * h 3 + (1/4) * d 1 3 * h 1 + (1/4) * d 2 0 * h 2 + (1/4) * d 2 1 * h 2 + (1/4) * d 2 2 * h 0 + (1/4) * d 2 2 * h 1 + (1/4) * d 2 3 * h 4 + (1/4) * d 2 4 * h 3), ((1/2) * d 0 0 * h 0 + (1/2) * d 0 0 * h 1 + (1/2) * d 0 1 * h 0 + (1/2) * d 0 1 * h 1 + (1/2) * d 0 3 * h 3 + (1/2) * d 0 4 * h 4)]],
   ![![((1/2) * d 1 0 * h 0 + (1/2) * d 1 2 * h 2 + (1/2) * d 1 3 * h 3), (h 0 * h 4 + (1/2) * d 0 1 * h 1 + (1/2) * d 0 2 * h 2 + (1/2) * d 0 4 * h 4 - h 2 * h 3), (-(h 0) ^ (2:ℕ) - (h 3) ^ (2:ℕ) - h 0 * h 1 - (1/4) * d 0 0 * h 4 - (1/4) * d 0 4 * h 0 - (1/4) * d 1 1 * h 3 - (1/4) * d 1 3 * h 1 - (1/4) * d 2 0 * h 2 - (1/4) * d 2 1 * h 2 - (1/4) * d 2 2 * h 0 - (1/4) * d 2 2 * h 1 - (1/4) * d 2 3 * h 4 - (1/4) * d 2 4 * h 3 + (1/4) * d 0 2 * h 3 + (1/4) * d 0 3 * h 2 + (1/4) * d 1 2 * h 4 + (1/4) * d 1 4 * h 2)],
    ![(h 2 * h 3 + (1/2) * d 1 0 * h 2 + (1/2) * d 1 1 * h 2 + (1/2) * d 1 2 * h 0 + (1/2) * d 1 2 * h 1 + (1/2) * d 1 3 * h 4 + (1/2) * d 1 4 * h 3 - h 0 * h 4 - (1/2) * d 0 1 * h 1 - (1/2) * d 0 2 * h 2 - (1/2) * d 0 4 * h 4), ((1/2) * d 1 1 * h 1 + (1/2) * d 1 2 * h 2 + (1/2) * d 1 4 * h 4), ((1/2) * d 1 2 * h 3 + (1/2) * d 1 3 * h 2 - h 0 * h 2 - h 1 * h 2 - h 3 * h 4 - (1/2) * d 1 0 * h 4 - (1/2) * d 1 4 * h 0 - (1/2) * d 2 1 * h 1 - (1/2) * d 2 2 * h 2 - (1/2) * d 2 4 * h 4)],
    ![((h 0) ^ (2:ℕ) + (h 3) ^ (2:ℕ) + h 0 * h 1 - (1/4) * d 0 2 * h 3 - (1/4) * d 0 3 * h 2 - (1/4) * d 1 1 * h 3 - (1/4) * d 1 3 * h 1 + (1/4) * d 0 0 * h 4 + (1/4) * d 0 4 * h 0 + (1/4) * d 1 2 * h 4 + (1/4) * d 1 4 * h 2 + (1/4) * d 2 0 * h 2 + (1/4) * d 2 1 * h 2 + (1/4) * d 2 2 * h 0 + (1/4) * d 2 2 * h 1 + (1/4) * d 2 3 * h 4 + (1/4) * d 2 4 * h 3), (h 0 * h 2 + h 1 * h 2 + h 3 * h 4 + (1/2) * d 2 1 * h 1 + (1/2) * d 2 2 * h 2 + (1/2) * d 2 4 * h 4), ((1/2) * d 1 0 * h 0 + (1/2) * d 1 0 * h 1 + (1/2) * d 1 1 * h 0 + (1/2) * d 1 1 * h 1 + (1/2) * d 1 3 * h 3 + (1/2) * d 1 4 * h 4)]],
   ![![((1/2) * d 2 0 * h 0 + (1/2) * d 2 2 * h 2 + (1/2) * d 2 3 * h 3), ((h 2) ^ (2:ℕ) - h 0 * h 1 - (1/4) * d 0 0 * h 4 - (1/4) * d 0 4 * h 0 - (1/4) * d 1 2 * h 4 - (1/4) * d 1 4 * h 2 + (1/4) * d 0 2 * h 3 + (1/4) * d 0 3 * h 2 + (1/4) * d 1 1 * h 3 + (1/4) * d 1 3 * h 1 + (1/4) * d 2 0 * h 2 + (1/4) * d 2 1 * h 2 + (1/4) * d 2 2 * h 0 + (1/4) * d 2 2 * h 1 + (1/4) * d 2 3 * h 4 + (1/4) * d 2 4 * h 3), (h 2 * h 3 + (1/2) * d 0 0 * h 0 + (1/2) * d 0 0 * h 1 + (1/2) * d 0 1 * h 0 + (1/2) * d 0 1 * h 1 + (1/2) * d 0 3 * h 3 + (1/2) * d 0 4 * h 4 - h 0 * h 4)],
    ![(-(h 2) ^ (2:ℕ) + h 0 * h 1 - (1/4) * d 0 2 * h 3 - (1/4) * d 0 3 * h 2 - (1/4) * d 1 1 * h 3 - (1/4) * d 1 3 * h 1 + (1/4) * d 0 0 * h 4 + (1/4) * d 0 4 * h 0 + (1/4) * d 1 2 * h 4 + (1/4) * d 1 4 * h 2 + (1/4) * d 2 0 * h 2 + (1/4) * d 2 1 * h 2 + (1/4) * d 2 2 * h 0 + (1/4) * d 2 2 * h 1 + (1/4) * d 2 3 * h 4 + (1/4) * d 2 4 * h 3), ((1/2) * d 2 1 * h 1 + (1/2) * d 2 2 * h 2 + (1/2) * d 2 4 * h 4), (h 1 * h 3 + (1/2) * d 1 0 * h 0 + (1/2) * d 1 0 * h 1 + (1/2) * d 1 1 * h 0 + (1/2) * d 1 1 * h 1 + (1/2) * d 1 3 * h 3 + (1/2) * d 1 4 * h 4 - h 2 * h 4)],
    ![(h 0 * h 4 + (1/2) * d 2 2 * h 4 + (1/2) * d 2 4 * h 2 - h 2 * h 3 - (1/2) * d 0 0 * h 0 - (1/2) * d 0 0 * h 1 - (1/2) * d 0 1 * h 0 - (1/2) * d 0 1 * h 1 - (1/2) * d 0 3 * h 3 - (1/2) * d 0 4 * h 4 - (1/2) * d 2 1 * h 3 - (1/2) * d 2 3 * h 1), (h 2 * h 4 + (1/2) * d 2 2 * h 3 + (1/2) * d 2 3 * h 2 - h 1 * h 3 - (1/2) * d 1 0 * h 0 - (1/2) * d 1 0 * h 1 - (1/2) * d 1 1 * h 0 - (1/2) * d 1 1 * h 1 - (1/2) * d 1 3 * h 3 - (1/2) * d 1 4 * h 4 - (1/2) * d 2 0 * h 4 - (1/2) * d 2 4 * h 0), ((1/2) * d 2 0 * h 0 + (1/2) * d 2 0 * h 1 + (1/2) * d 2 1 * h 0 + (1/2) * d 2 1 * h 1 + (1/2) * d 2 3 * h 3 + (1/2) * d 2 4 * h 4)]]]

def gamT2 (h : Fin 5 → K) (d : Fin 3 → Fin 5 → K) : Fin 3 → Fin 3 → Fin 3 → K :=
  ![![![((1/2) * d 1 0 * h 2 + (1/2) * d 2 0 * h 3 - (1/2) * d 0 2 * h 2 - (1/2) * d 0 3 * h 3), ((1/2) * d 1 2 * h 2 + (1/2) * d 2 2 * h 3 - (3/2) * h 1 * h 3 - (1/2) * d 0 1 * h 2 - (1/2) * d 0 4 * h 3 + (3/2) * h 2 * h 4), ((1/2) * d 0 0 * h 3 + (1/2) * d 0 1 * h 3 + (1/2) * d 1 3 * h 2 + (1/2) * d 2 3 * h 3 - (3/2) * h 0 * h 2 - (3/2) * h 1 * h 2 - (3/2) * h 3 * h 4 - (1/2) * d 0 4 * h 2)],
    ![((1/2) * d 1 2 * h 2 + (1/2) * d 2 2 * h 3 - (3/2) * h 1 * h 3 - (1/2) * d 0 1 * h 2 - (1/2) * d 0 4 * h 3 + (3/2) * h 2 * h 4), ((1/2) * d 0 1 * h 0 + (1/2) * d 1 0 * h 2 + (1/2) * d 1 2 * h 1 + (1/2) * d 1 3 * h 4 + (1/2) * d 2 1 * h 3 - 3 * h 0 * h 4 + 3 * h 2 * h 3 - (1/2) * d 0 1 * h 1 - (1/2) * d 0 2 * h 2 - (1/2) * d 0 4 * h 4 - (1/2) * d 1 2 * h 0 - (1/2) * d 1 4 * h 3), (-(3/2) * (h 2) ^ (2:ℕ) + (3/2) * (h 0) ^ (2:ℕ) + (3/2) * (h 3) ^ (2:ℕ) + (1/2) * d 1 0 * h 3 + 3 * h 0 * h 1 - (1/2) * d 1 3 * h 0 - (1/4) * d 0 2 * h 3 - (1/4) * d 0 3 * h 2 - (1/4) * d 1 3 * h 1 - (1/4) * d 2 1 * h 2 - (1/4) * d 2 2 * h 0 + (1/4) * d 0 0 * h 4 + (1/4) * d 1 1 * h 3 + (1/4) * d 1 2 * h 4 + (1/4) * d 1 4 * h 2 + (1/4) * d 2 0 * h 2 + (1/4) * d 2 2 * h 1 + (1/4) * d 2 3 * h 4 + (1/4) * d 2 4 * h 3 + (3/4) * d 0 4 * h 0)],
    ![((1/2) * d 0 0 * h 3 + (1/2) * d 0 1 * h 3 + (1/2) * d 1 3 * h 2 + (1/2) * d 2 3 * h 3 - (3/2) * h 0 * h 2 - (3/2) * h 1 * h 2 - (3/2) * h 3 * h 4 - (1/2) * d 0 4 * h 2), (-(3/2) * (h 2) ^ (2:ℕ) + (3/2) * (h 0) ^ (2:ℕ) + (3/2) * (h 3) ^ (2:ℕ) + (1/2) * d 1 0 * h 3 + 3 * h 0 * h 1 - (1/2) * d 1 3 * h 0 - (1/4) * d 0 2 * h 3 - (1/4) * d 0 3 * h 2 - (1/4) * d 1 3 * h 1 - (1/4) * d 2 1 * h 2 - (1/4) * d 2 2 * h 0 + (1/4) * d 0 0 * h 4 + (1/4) * d 1 1 * h 3 + (1/4) * d 1 2 * h 4 + (1/4) * d 1 4 * h 2 + (1/4) * d 2 0 * h 2 + (1/4) * d 2 2 * h 1 + (1/4) * d 2 3 * h 4 + (1/4) * d 2 4 * h 3 + (3/4) * d 0 4 * h 0), ((1/2) * d 2 0 * h 3 + (1/2) * d 2 2 * h 4 - d 0 0 * h 0 - d 0 1 * h 0 - d 2 3 * h 0 - 3 * h 2 * h 3 + 3 * h 0 * h 4 - (1/2) * d 0 0 * h 1 - (1/2) * d 0 1 * h 1 - (1/2) * d 0 3 * h 3 - (1/2) * d 0 4 * h 4 - (1/2) * d 1 0 * h 2 - (1/2) * d 1 1 * h 2 - (1/2) * d 2 3 * h 1 - (1/2) * d 2 4 * h 2)]],
   ![![((1/2) * d 0 1 * h 2 + (1/2) * d 0 2 * h 0 + (1/2) * d 0 4 * h 3 + (1/2) * d 1 0 * h 1 + (1/2) * d 2 0 * h 4 - 3 * h 2 * h 4 + 3 * h 1 * h 3 - (1/2) * d 0 2 * h 1 - (1/2) * d 0 3 * h 4 - (1/2) * d 1 0 * h 0 - (1/2) * d 1 2 * h 2 - (1/2) * d 1 3 * h 3), ((1/2) * d 0 2 * h 2 + (1/2) * d 2 2 * h 4 - (3/2) * h 2 * h 3 - (1/2) * d 1 0 * h 2 - (1/2) * d 1 3 * h 4 + (3/2) * h 0 * h 4), (-(3/2) * (h 1) ^ (2:ℕ) - (3/2) * (h 4) ^ (2:ℕ) + (3/2) * (h 2) ^ (2:ℕ) + (1/2) * d 0 1 * h 4 - 3 * h 0 * h 1 - (1/2) * d 0 4 * h 1 - (1/4) * d 0 4 * h 0 - (1/4) * d 1 2 * h 4 - (1/4) * d 1 4 * h 2 - (1/4) * d 2 0 * h 2 - (1/4) * d 2 2 * h 1 + (1/4) * d 0 0 * h 4 + (1/4) * d 0 2 * h 3 + (1/4) * d 0 3 * h 2 + (1/4) * d 1 1 * h 3 + (1/4) * d 2 1 * h 2 + (1/4) * d 2 2 * h 0 + (1/4) * d 2 3 * h 4 + (1/4) * d 2 4 * h 3 + (3/4) * d 1 3 * h 1)],
    ![((1/2) * d 0 2 * h 2 + (1/2) * d 2 2 * h 4 - (3/2) * h 2 * h 3 - (1/2) * d 1 0 * h 2 - (1/2) * d 1 3 * h 4 + (3/2) * h 0 * h 4), ((1/2) * d 0 1 * h 2 + (1/2) * d 2 1 * h 4 - (1/2) * d 1 2 * h 2 - (1/2) * d 1 4 * h 4), ((1/2) * d 0 4 * h 2 + (1/2) * d 1 0 * h 4 + (1/2) * d 1 1 * h 4 + (1/2) * d 2 4 * h 4 - (1/2) * d 1 3 * h 2 + (3/2) * h 0 * h 2 + (3/2) * h 1 * h 2 + (3/2) * h 3 * h 4)],
    ![(-(3/2) * (h 1) ^ (2:ℕ) - (3/2) * (h 4) ^ (2:ℕ) + (3/2) * (h 2) ^ (2:ℕ) + (1/2) * d 0 1 * h 4 - 3 * h 0 * h 1 - (1/2) * d 0 4 * h 1 - (1/4) * d 0 4 * h 0 - (1/4) * d 1 2 * h 4 - (1/4) * d 1 4 * h 2 - (1/4) * d 2 0 * h 2 - (1/4) * d 2 2 * h 1 + (1/4) * d 0 0 * h 4 + (1/4) * d 0 2 * h 3 + (1/4) * d 0 3 * h 2 + (1/4) * d 1 1 * h 3 + (1/4) * d 2 1 * h 2 + (1/4) * d 2 2 * h 0 + (1/4) * d 2 3 * h 4 + (1/4) * d 2 4 * h 3 + (3/4) * d 1 3 * h 1), ((1/2) * d 0 4 * h 2 + (1/2) * d 1 0 * h 4 + (1/2) * d 1 1 * h 4 + (1/2) * d 2 4 * h 4 - (1/2) * d 1 3 * h 2 + (3/2) * h 0 * h 2 + (3/2) * h 1 * h 2 + (3/2) * h 3 * h 4), ((1/2) * d 2 1 * h 4 + (1/2) * d 2 2 * h 3 - d 1 0 * h 1 - d 1 1 * h 1 - d 2 4 * h 1 - 3 * h 1 * h 3 + 3 * h 2 * h 4 - (1/2) * d 0 0 * h 2 - (1/2) * d 0 1 * h 2 - (1/2) * d 1 0 * h 0 - (1/2) * d 1 1 * h 0 - (1/2) * d 1 3 * h 3 - (1/2) * d 1 4 * h 4 - (1/2) * d 2 3 * h 2 - (1/2) * d 2 4 * h 0)]],
   ![![(d 0 3 * h 0 + (1/2) * d 0 3 * h 1 + (1/2) * d 0 4 * h 2 + (1/2) * d 1 0 * h 4 - d 2 0 * h 0 + 3 * h 0 * h 2 + 3 * h 1 * h 2 + 3 * h 3 * h 4 - (1/2) * d 0 0 * h 3 - (1/2) * d 0 1 * h 3 - (1/2) * d 0 2 * h 4 - (1/2) * d 2 0 * h 1 - (1/2) * d 2 2 * h 2 - (1/2) * d 2 3 * h 3), (-(3/2) * (h 0) ^ (2:ℕ) - (3/2) * (h 3) ^ (2:ℕ) + (3/2) * (h 1) ^ (2:ℕ) + (3/2) * (h 4) ^ (2:ℕ) + (1/2) * d 0 4 * h 1 + (1/2) * d 1 3 * h 0 - (3/4) * d 2 2 * h 0 - (3/4) * d 2 2 * h 1 - (1/2) * d 0 1 * h 4 - (1/2) * d 1 0 * h 3 - (1/4) * d 0 0 * h 4 - (1/4) * d 1 1 * h 3 - (1/4) * d 2 0 * h 2 - (1/4) * d 2 1 * h 2 - (1/4) * d 2 3 * h 4 - (1/4) * d 2 4 * h 3 + (1/4) * d 0 2 * h 3 + (1/4) * d 0 3 * h 2 + (1/4) * d 0 4 * h 0 + (1/4) * d 1 2 * h 4 + (1/4) * d 1 3 * h 1 + (1/4) * d 1 4 * h 2), ((1/2) * d 0 3 * h 3 + (1/2) * d 1 3 * h 4 - (3/2) * h 0 * h 4 - (1/2) * d 2 0 * h 3 - (1/2) * d 2 2 * h 4 + (3/2) * h 2 * h 3)],
    ![(-(3/2) * (h 0) ^ (2:ℕ) - (3/2) * (h 3) ^ (2:ℕ) + (3/2) * (h 1) ^ (2:ℕ) + (3/2) * (h 4) ^ (2:ℕ) + (1/2) * d 0 4 * h 1 + (1/2) * d 1 3 * h 0 - (3/4) * d 2 2 * h 0 - (3/4) * d 2 2 * h 1 - (1/2) * d 0 1 * h 4 - (1/2) * d 1 0 * h 3 - (1/4) * d 0 0 * h 4 - (1/4) * d 1 1 * h 3 - (1/4) * d 2 0 * h 2 - (1/4) * d 2 1 * h 2 - (1/4) * d 2 3 * h 4 - (1/4) * d 2 4 * h 3 + (1/4) * d 0 2 * h 3 + (1/4) * d 0 3 * h 2 + (1/4) * d 0 4 * h 0 + (1/4) * d 1 2 * h 4 + (1/4) * d 1 3 * h 1 + (1/4) * d 1 4 * h 2), (d 1 4 * h 1 + (1/2) * d 0 1 * h 3 + (1/2) * d 1 3 * h 2 + (1/2) * d 1 4 * h 0 - d 2 1 * h 1 - 3 * h 0 * h 2 - 3 * h 1 * h 2 - 3 * h 3 * h 4 - (1/2) * d 1 0 * h 4 - (1/2) * d 1 1 * h 4 - (1/2) * d 1 2 * h 3 - (1/2) * d 2 1 * h 0 - (1/2) * d 2 2 * h 2 - (1/2) * d 2 4 * h 4), ((1/2) * d 0 4 * h 3 + (1/2) * d 1 4 * h 4 - (3/2) * h 2 * h 4 - (1/2) * d 2 1 * h 4 - (1/2) * d 2 2 * h 3 + (3/2) * h 1 * h 3)],
    ![((1/2) * d 0 3 * h 3 + (1/2) * d 1 3 * h 4 - (3/2) * h 0 * h 4 - (1/2) * d 2 0 * h 3 - (1/2) * d 2 2 * h 4 + (3/2) * h 2 * h 3), ((1/2) * d 0 4 * h 3 + (1/2) * d 1 4 * h 4 - (3/2) * h 2 * h 4 - (1/2) * d 2 1 * h 4 - (1/2) * d 2 2 * h 3 + (3/2) * h 1 * h 3), (-(1/2) * d 0 0 * h 3 - (1/2) * d 0 1 * h 3 - (1/2) * d 1 0 * h 4 - (1/2) * d 1 1 * h 4 - (1/2) * d 2 3 * h 3 - (1/2) * d 2 4 * h 4)]]]

def ricT2 (h : Fin 5 → K) (d : Fin 3 → Fin 5 → K) (s : Fin 3 → Fin 3 → Fin 5 → K) : Fin 3 → Fin 3 → K :=
  ![![(-8 * (h 1) ^ (2:ℕ) - 8 * (h 4) ^ (2:ℕ) + 7 * (h 0) ^ (2:ℕ) + 7 * (h 2) ^ (2:ℕ) + 7 * (h 3) ^ (2:ℕ) - (1/2) * (d 0 0) ^ (2:ℕ) - (1/2) * (d 0 1) ^ (2:ℕ) - (1/2) * (d 0 2) ^ (2:ℕ) - (1/2) * (d 0 3) ^ (2:ℕ) - (1/2) * (d 0 4) ^ (2:ℕ) - (1/2) * (d 1 2) ^ (2:ℕ) - (1/2) * (d 2 0) ^ (2:ℕ) - (1/2) * (d 2 3) ^ (2:ℕ) + h 0 * s 0 2 3 + h 4 * s 1 2 0 + (1/2) * d 0 1 * d 1 2 + (1/2) * d 0 3 * d 2 0 + (1/2) * d 0 3 * d 2 1 + (1/2) * d 0 4 * d 1 3 + (1/2) * d 0 4 * d 2 2 + (1/2) * d 1 0 * d 1 1 + (1/2) * d 1 0 * d 2 4 + (1/2) * d 1 4 * d 2 0 + (1/2) * d 2 0 * h 2 + (1/2) * h 0 * s 0 1 2 + (1/2) * h 1 * s 0 2 3 + (1/2) * h 1 * s 1 1 0 + (1/2) * h 2 * s 0 1 0 + (1/2) * h 2 * s 0 1 1 + (1/2) * h 2 * s 0 2 4 + (1/2) * h 3 * s 0 1 4 - d 1 3 * d 2 2 - h 0 * s 2 2 0 - 8 * h 0 * h 1 - 4 * d 0 4 * h 1 - 3 * d 1 3 * h 0 - 2 * d 0 2 * h 3 - 2 * d 0 4 * h 0 + 2 * d 0 0 * h 4 + 2 * d 0 3 * h 2 + 3 * d 1 0 * h 3 + 4 * d 0 1 * h 4 - (9/2) * d 1 2 * h 4 - (7/2) * d 1 4 * h 2 - (1/2) * d 0 0 * d 0 1 - (1/2) * d 0 0 * d 2 3 - (1/2) * d 0 1 * d 2 3 - (1/2) * d 0 2 * d 1 1 - (1/2) * d 0 2 * d 2 4 - (1/2) * d 0 3 * d 1 4 - (1/2) * d 2 0 * d 2 1 - (1/2) * h 0 * s 1 1 0 - (1/2) * h 1 * s 0 1 2 - (1/2) * h 1 * s 2 2 0 - (1/2) * h 2 * s 0 0 2 - (1/2) * h 2 * s 1 1 2 - (1/2) * h 2 * s 2 2 2 - (1/2) * h 3 * s 0 0 3 - (1/2) * h 3 * s 0 2 1 - (1/2) * h 3 * s 1 1 3 - (1/2) * h 3 * s 2 2 3 - (1/2) * h 4 * s 0 1 3 - (1/2) * h 4 * s 0 2 2 + (7/2) * d 1 1 * h 3 + (7/2) * d 2 1 * h 2 + (7/2) * d 2 4 * h 3 + (9/2) * d 1 3 * h 1 + (9/2) * d 2 2 * h 1 + (9/2) * d 2 3 * h 4 + (15/2) * d 2 2 * h 0), (h 2 * s 0 1 2 + (1/2) * d 0 4 * d 2 1 + (1/2) * d 1 3 * d 2 0 + (1/2) * h 0 * s 1 2 3 + (1/2) * h 1 * s 0 2 4 - 4 * d 2 0 * h 0 - 4 * d 2 3 * h 3 - 2 * d 2 0 * h 1 + 2 * d 2 1 * h 0 + 4 * d 2 1 * h 1 + 4 * d 2 4 * h 4 + 15 * h 0 * h 2 + 15 * h 1 * h 2 + 15 * h 3 * h 4 - (19/4) * d 0 1 * h 3 - (19/4) * d 1 3 * h 2 - (3/2) * d 0 0 * h 3 - (3/2) * d 1 4 * h 1 - (3/4) * d 0 1 * d 1 0 - (3/4) * d 0 2 * h 4 - (3/4) * d 1 4 * h 0 - (3/4) * h 0 * s 2 2 2 - (3/4) * h 1 * s 2 2 2 - (1/2) * d 0 0 * d 1 0 - (1/2) * d 0 1 * d 1 1 - (1/2) * d 0 1 * d 2 4 - (1/2) * d 0 3 * d 1 3 - (1/2) * d 0 4 * d 1 4 - (1/2) * d 1 0 * d 2 3 - (1/2) * d 2 0 * d 2 2 - (1/2) * d 2 1 * d 2 2 - (1/2) * d 2 3 * d 2 4 - (1/2) * h 2 * s 0 0 1 - (1/2) * h 2 * s 1 1 0 - (1/2) * h 3 * s 0 0 4 - (1/2) * h 3 * s 1 2 0 - (1/2) * h 4 * s 0 2 1 - (1/2) * h 4 * s 1 1 3 - (1/4) * d 0 0 * d 1 1 - (1/4) * d 0 0 * d 2 4 - (1/4) * d 0 4 * d 2 0 - (1/4) * d 1 1 * d 2 3 - (1/4) * d 1 3 * d 2 1 - (1/4) * h 2 * s 2 2 0 - (1/4) * h 2 * s 2 2 1 - (1/4) * h 3 * s 1 2 1 - (1/4) * h 3 * s 2 2 4 - (1/4) * h 4 * s 0 2 0 - (1/4) * h 4 * s 2 2 3 + (1/4) * d 0 2 * d 2 3 + (1/4) * d 0 3 * d 2 2 + (1/4) * d 1 2 * d 2 4 + (1/4) * d 1 4 * d 2 2 + (1/4) * h 0 * s 0 2 4 + (1/4) * h 1 * s 1 2 3 + (1/4) * h 2 * s 0 2 3 + (1/4) * h 2 * s 1 2 4 + (3/2) * d 0 3 * h 0 + (3/2) * d 1 1 * h 4 + (3/4) * d 0 3 * h 1 + (3/4) * d 1 2 * h 3 + (3/4) * h 3 * s 0 2 2 + (3/4) * h 4 * s 1 2 2 + (19/4) * d 0 4 * h 2 + (19/4) * d 1 0 * h 4), (h 3 * s 0 2 3 + (1/2) * d 0 1 * d 1 4 + (1/2) * d 1 1 * d 1 3 + (1/2) * h 3 * s 0 0 0 + (1/2) * h 3 * s 0 0 1 + (1/2) * h 4 * s 0 1 1 - 15 * h 1 * h 3 - 6 * d 1 0 * h 1 - 4 * d 1 1 * h 1 - 4 * d 1 4 * h 4 - 2 * d 1 1 * h 0 + 4 * d 1 2 * h 2 + 15 * h 2 * h 4 - (19/4) * d 0 1 * h 2 - (19/4) * d 0 4 * h 3 - (13/4) * d 0 0 * h 2 - (13/4) * d 2 0 * h 4 - (3/2) * d 2 4 * h 1 - (3/4) * d 0 2 * h 0 - (3/4) * d 0 4 * d 1 0 - (3/4) * d 2 3 * h 2 - (3/4) * d 2 4 * h 0 - (1/2) * d 0 1 * d 2 1 - (1/2) * d 0 2 * d 2 2 - (1/2) * d 0 4 * d 1 1 - (1/2) * d 0 4 * d 2 4 - (1/2) * d 1 2 * d 1 4 - (1/2) * h 1 * s 0 1 4 - (1/2) * h 2 * s 0 0 4 - (1/2) * h 3 * s 2 2 0 - (1/2) * h 4 * s 2 2 2 - (1/4) * d 0 0 * d 2 1 - (1/4) * d 1 2 * d 2 0 - (1/4) * h 0 * s 0 1 4 - (1/4) * h 1 * s 1 2 2 - (1/4) * h 2 * s 1 1 4 - (1/4) * h 2 * s 1 2 0 - (1/4) * h 4 * s 1 1 2 + (1/4) * d 0 0 * d 1 4 + (1/4) * d 0 1 * d 2 0 + (1/4) * d 0 2 * d 1 3 + (1/4) * d 0 3 * d 1 2 + (1/4) * d 1 1 * d 2 2 + (1/4) * d 1 2 * d 2 1 + (1/4) * d 1 3 * d 2 4 + (1/4) * d 1 4 * d 2 3 + (1/4) * h 0 * s 1 2 2 + (1/4) * h 2 * s 1 2 1 + (1/4) * h 3 * s 0 1 2 + (1/4) * h 3 * s 1 1 1 + (1/4) * h 3 * s 1 2 4 + (1/4) * h 4 * s 0 1 0 + (3/2) * d 2 1 * h 4 + (3/4) * d 0 2 * h 1 + (3/4) * d 0 3 * h 4 + (3/4) * d 1 0 * d 2 2 + (3/4) * h 1 * s 1 1 3 + (3/4) * h 2 * s 0 1 3 + (3/4) * h 4 * s 1 2 3 + (19/4) * d 2 2 * h 3)],
    ![(h 2 * s 0 1 2 + (1/2) * d 0 4 * d 2 1 + (1/2) * d 1 3 * d 2 0 + (1/2) * h 0 * s 1 2 3 + (1/2) * h 1 * s 0 2 4 - 4 * d 2 0 * h 0 - 4 * d 2 3 * h 3 - 2 * d 2 0 * h 1 + 2 * d 2 1 * h 0 + 4 * d 2 1 * h 1 + 4 * d 2 4 * h 4 + 15 * h 0 * h 2 + 15 * h 1 * h 2 + 15 * h 3 * h 4 - (19/4) * d 0 1 * h 3 - (19/4) * d 1 3 * h 2 - (3/2) * d 0 0 * h 3 - (3/2) * d 1 4 * h 1 - (3/4) * d 0 1 * d 1 0 - (3/4) * d 0 2 * h 4 - (3/4) * d 1 4 * h 0 - (3/4) * h 0 * s 2 2 2 - (3/4) * h 1 * s 2 2 2 - (1/2) * d 0 0 * d 1 0 - (1/2) * d 0 1 * d 1 1 - (1/2) * d 0 1 * d 2 4 - (1/2) * d 0 3 * d 1 3 - (1/2) * d 0 4 * d 1 4 - (1/2) * d 1 0 * d 2 3 - (1/2) * d 2 0 * d 2 2 - (1/2) * d 2 1 * d 2 2 - (1/2) * d 2 3 * d 2 4 - (1/2) * h 2 * s 0 0 1 - (1/2) * h 2 * s 1 1 0 - (1/2) * h 3 * s 0 0 4 - (1/2) * h 3 * s 1 2 0 - (1/2) * h 4 * s 0 2 1 - (1/2) * h 4 * s 1 1 3 - (1/4) * d 0 0 * d 1 1 - (1/4) * d 0 0 * d 2 4 - (1/4) * d 0 4 * d 2 0 - (1/4) * d 1 1 * d 2 3 - (1/4) * d 1 3 * d 2 1 - (1/4) * h 2 * s 2 2 0 - (1/4) * h 2 * s 2 2 1 - (1/4) * h 3 * s 1 2 1 - (1/4) * h 3 * s 2 2 4 - (1/4) * h 4 * s 0 2 0 - (1/4) * h 4 * s 2 2 3 + (1/4) * d 0 2 * d 2 3 + (1/4) * d 0 3 * d 2 2 + (1/4) * d 1 2 * d 2 4 + (1/4) * d 1 4 * d 2 2 + (1/4) * h 0 * s 0 2 4 + (1/4) * h 1 * s 1 2 3 + (1/4) * h 2 * s 0 2 3 + (1/4) * h 2 * s 1 2 4 + (3/2) * d 0 3 * h 0 + (3/2) * d 1 1 * h 4 + (3/4) * d 0 3 * h 1 + (3/4) * d 1 2 * h 3 + (3/4) * h 3 * s 0 2 2 + (3/4) * h 4 * s 1 2 2 + (19/4) * d 0 4 * h 2 + (19/4) * d 1 0 * h 4), (-8 * (h 0) ^ (2:ℕ) - 8 * (h 3) ^ (2:ℕ) + 7 * (h 1) ^ (2:ℕ) + 7 * (h 2) ^ (2:ℕ) + 7 * (h 4) ^ (2:ℕ) - (1/2) * (d 0 2) ^ (2:ℕ) - (1/2) * (d 1 0) ^ (2:ℕ) - (1/2) * (d 1 1) ^ (2:ℕ) - (1/2) * (d 1 2) ^ (2:ℕ) - (1/2) * (d 1 3) ^ (2:ℕ) - (1/2) * (d 1 4) ^ (2:ℕ) - (1/2) * (d 2 1) ^ (2:ℕ) - (1/2) * (d 2 4) ^ (2:ℕ) + h 1 * s 1 2 4 + h 3 * s 0 2 1 + (1/2) * d 0 0 * d 0 1 + (1/2) * d 0 1 * d 2 3 + (1/2) * d 0 2 * d 1 0 + (1/2) * d 0 3 * d 2 1 + (1/2) * d 0 4 * d 1 3 + (1/2) * d 1 3 * d 2 2 + (1/2) * d 1 4 * d 2 0 + (1/2) * d 1 4 * d 2 1 + (1/2) * h 0 * s 0 0 1 + (1/2) * h 0 * s 1 2 4 + (1/2) * h 1 * s 0 1 2 + (1/2) * h 2 * s 0 1 0 + (1/2) * h 2 * s 0 1 1 + (1/2) * h 2 * s 1 2 3 + (1/2) * h 4 * s 0 1 3 - d 0 4 * d 2 2 - h 1 * s 2 2 1 - 8 * h 0 * h 1 - 4 * d 1 0 * h 3 - 3 * d 0 1 * h 4 - 2 * d 1 1 * h 3 - 2 * d 1 4 * h 2 + 2 * d 1 2 * h 4 + 2 * d 1 3 * h 1 + 3 * d 0 4 * h 1 + 4 * d 1 3 * h 0 - (15/2) * d 2 2 * h 1 - (9/2) * d 0 4 * h 0 - (9/2) * d 2 2 * h 0 - (9/2) * d 2 4 * h 3 - (7/2) * d 0 0 * h 4 - (7/2) * d 2 0 * h 2 - (7/2) * d 2 3 * h 4 - (1/2) * d 0 0 * d 1 2 - (1/2) * d 0 3 * d 1 4 - (1/2) * d 1 0 * d 1 1 - (1/2) * d 1 0 * d 2 4 - (1/2) * d 1 1 * d 2 4 - (1/2) * d 1 2 * d 2 3 - (1/2) * d 2 0 * d 2 1 - (1/2) * d 2 1 * h 2 - (1/2) * h 0 * s 0 1 2 - (1/2) * h 0 * s 2 2 1 - (1/2) * h 1 * s 0 0 1 - (1/2) * h 2 * s 0 0 2 - (1/2) * h 2 * s 1 1 2 - (1/2) * h 2 * s 2 2 2 - (1/2) * h 3 * s 0 1 4 - (1/2) * h 3 * s 1 2 2 - (1/2) * h 4 * s 0 0 4 - (1/2) * h 4 * s 1 1 4 - (1/2) * h 4 * s 1 2 0 - (1/2) * h 4 * s 2 2 4 + (7/2) * d 0 3 * h 2 + (9/2) * d 0 2 * h 3), (h 4 * s 1 2 4 + (1/2) * d 0 0 * d 0 4 + (1/2) * d 0 3 * d 1 0 + (1/2) * h 3 * s 0 1 0 + (1/2) * h 4 * s 1 1 0 + (1/2) * h 4 * s 1 1 1 - 15 * h 0 * h 4 - 4 * d 0 2 * h 2 + 2 * d 0 0 * h 1 + 4 * d 0 0 * h 0 + 4 * d 0 3 * h 3 + 6 * d 0 1 * h 0 + 15 * h 2 * h 3 - (19/4) * d 2 2 * h 4 - (3/2) * d 2 0 * h 3 - (3/4) * d 0 1 * d 1 3 - (3/4) * d 1 2 * h 0 - (3/4) * d 1 4 * h 3 - (1/2) * d 0 0 * d 1 3 - (1/2) * d 0 2 * d 0 3 - (1/2) * d 1 0 * d 2 0 - (1/2) * d 1 2 * d 2 2 - (1/2) * d 1 3 * d 2 3 - (1/2) * h 0 * s 0 1 3 - (1/2) * h 2 * s 1 1 3 - (1/2) * h 3 * s 2 2 2 - (1/2) * h 4 * s 2 2 1 - (1/4) * d 0 2 * d 2 1 - (1/4) * d 1 1 * d 2 0 - (1/4) * h 0 * s 0 2 2 - (1/4) * h 1 * s 0 1 3 - (1/4) * h 2 * s 0 0 3 - (1/4) * h 2 * s 0 2 1 - (1/4) * h 3 * s 0 0 2 + (1/4) * d 0 0 * d 2 2 + (1/4) * d 0 2 * d 1 4 + (1/4) * d 0 2 * d 2 0 + (1/4) * d 0 3 * d 1 1 + (1/4) * d 0 3 * d 2 4 + (1/4) * d 0 4 * d 1 2 + (1/4) * d 0 4 * d 2 3 + (1/4) * d 1 0 * d 2 1 + (1/4) * h 1 * s 0 2 2 + (1/4) * h 2 * s 0 2 0 + (1/4) * h 3 * s 0 1 1 + (1/4) * h 4 * s 0 0 0 + (1/4) * h 4 * s 0 1 2 + (1/4) * h 4 * s 0 2 3 + (3/2) * d 2 3 * h 0 + (3/4) * d 0 1 * d 2 2 + (3/4) * d 1 2 * h 1 + (3/4) * d 2 3 * h 1 + (3/4) * d 2 4 * h 2 + (3/4) * h 0 * s 0 0 4 + (3/4) * h 2 * s 0 1 4 + (3/4) * h 3 * s 0 2 4 + (13/4) * d 1 1 * h 2 + (13/4) * d 2 1 * h 3 + (19/4) * d 1 0 * h 2 + (19/4) * d 1 3 * h 4)],
    ![(h 3 * s 0 2 3 + (1/2) * d 0 1 * d 1 4 + (1/2) * d 1 1 * d 1 3 + (1/2) * h 3 * s 0 0 0 + (1/2) * h 3 * s 0 0 1 + (1/2) * h 4 * s 0 1 1 - 15 * h 1 * h 3 - 6 * d 1 0 * h 1 - 4 * d 1 1 * h 1 - 4 * d 1 4 * h 4 - 2 * d 1 1 * h 0 + 4 * d 1 2 * h 2 + 15 * h 2 * h 4 - (19/4) * d 0 1 * h 2 - (19/4) * d 0 4 * h 3 - (13/4) * d 0 0 * h 2 - (13/4) * d 2 0 * h 4 - (3/2) * d 2 4 * h 1 - (3/4) * d 0 2 * h 0 - (3/4) * d 0 4 * d 1 0 - (3/4) * d 2 3 * h 2 - (3/4) * d 2 4 * h 0 - (1/2) * d 0 1 * d 2 1 - (1/2) * d 0 2 * d 2 2 - (1/2) * d 0 4 * d 1 1 - (1/2) * d 0 4 * d 2 4 - (1/2) * d 1 2 * d 1 4 - (1/2) * h 1 * s 0 1 4 - (1/2) * h 2 * s 0 0 4 - (1/2) * h 3 * s 2 2 0 - (1/2) * h 4 * s 2 2 2 - (1/4) * d 0 0 * d 2 1 - (1/4) * d 1 2 * d 2 0 - (1/4) * h 0 * s 0 1 4 - (1/4) * h 1 * s 1 2 2 - (1/4) * h 2 * s 1 1 4 - (1/4) * h 2 * s 1 2 0 - (1/4) * h 4 * s 1 1 2 + (1/4) * d 0 0 * d 1 4 + (1/4) * d 0 1 * d 2 0 + (1/4) * d 0 2 * d 1 3 + (1/4) * d 0 3 * d 1 2 + (1/4) * d 1 1 * d 2 2 + (1/4) * d 1 2 * d 2 1 + (1/4) * d 1 3 * d 2 4 + (1/4) * d 1 4 * d 2 3 + (1/4) * h 0 * s 1 2 2 + (1/4) * h 2 * s 1 2 1 + (1/4) * h 3 * s 0 1 2 + (1/4) * h 3 * s 1 1 1 + (1/4) * h 3 * s 1 2 4 + (1/4) * h 4 * s 0 1 0 + (3/2) * d 2 1 * h 4 + (3/4) * d 0 2 * h 1 + (3/4) * d 0 3 * h 4 + (3/4) * d 1 0 * d 2 2 + (3/4) * h 1 * s 1 1 3 + (3/4) * h 2 * s 0 1 3 + (3/4) * h 4 * s 1 2 3 + (19/4) * d 2 2 * h 3), (h 4 * s 1 2 4 + (1/2) * d 0 0 * d 0 4 + (1/2) * d 0 3 * d 1 0 + (1/2) * h 3 * s 0 1 0 + (1/2) * h 4 * s 1 1 0 + (1/2) * h 4 * s 1 1 1 - 15 * h 0 * h 4 - 4 * d 0 2 * h 2 + 2 * d 0 0 * h 1 + 4 * d 0 0 * h 0 + 4 * d 0 3 * h 3 + 6 * d 0 1 * h 0 + 15 * h 2 * h 3 - (19/4) * d 2 2 * h 4 - (3/2) * d 2 0 * h 3 - (3/4) * d 0 1 * d 1 3 - (3/4) * d 1 2 * h 0 - (3/4) * d 1 4 * h 3 - (1/2) * d 0 0 * d 1 3 - (1/2) * d 0 2 * d 0 3 - (1/2) * d 1 0 * d 2 0 - (1/2) * d 1 2 * d 2 2 - (1/2) * d 1 3 * d 2 3 - (1/2) * h 0 * s 0 1 3 - (1/2) * h 2 * s 1 1 3 - (1/2) * h 3 * s 2 2 2 - (1/2) * h 4 * s 2 2 1 - (1/4) * d 0 2 * d 2 1 - (1/4) * d 1 1 * d 2 0 - (1/4) * h 0 * s 0 2 2 - (1/4) * h 1 * s 0 1 3 - (1/4) * h 2 * s 0 0 3 - (1/4) * h 2 * s 0 2 1 - (1/4) * h 3 * s 0 0 2 + (1/4) * d 0 0 * d 2 2 + (1/4) * d 0 2 * d 1 4 + (1/4) * d 0 2 * d 2 0 + (1/4) * d 0 3 * d 1 1 + (1/4) * d 0 3 * d 2 4 + (1/4) * d 0 4 * d 1 2 + (1/4) * d 0 4 * d 2 3 + (1/4) * d 1 0 * d 2 1 + (1/4) * h 1 * s 0 2 2 + (1/4) * h 2 * s 0 2 0 + (1/4) * h 3 * s 0 1 1 + (1/4) * h 4 * s 0 0 0 + (1/4) * h 4 * s 0 1 2 + (1/4) * h 4 * s 0 2 3 + (3/2) * d 2 3 * h 0 + (3/4) * d 0 1 * d 2 2 + (3/4) * d 1 2 * h 1 + (3/4) * d 2 3 * h 1 + (3/4) * d 2 4 * h 2 + (3/4) * h 0 * s 0 0 4 + (3/4) * h 2 * s 0 1 4 + (3/4) * h 3 * s 0 2 4 + (13/4) * d 1 1 * h 2 + (13/4) * d 2 1 * h 3 + (19/4) * d 1 0 * h 2 + (19/4) * d 1 3 * h 4), (-8 * (h 2) ^ (2:ℕ) + 7 * (h 0) ^ (2:ℕ) + 7 * (h 1) ^ (2:ℕ) + 7 * (h 3) ^ (2:ℕ) + 7 * (h 4) ^ (2:ℕ) - (1/2) * (d 0 0) ^ (2:ℕ) - (1/2) * (d 0 3) ^ (2:ℕ) - (1/2) * (d 1 1) ^ (2:ℕ) - (1/2) * (d 1 4) ^ (2:ℕ) - (1/2) * (d 2 0) ^ (2:ℕ) - (1/2) * (d 2 1) ^ (2:ℕ) - (1/2) * (d 2 2) ^ (2:ℕ) - (1/2) * (d 2 3) ^ (2:ℕ) - (1/2) * (d 2 4) ^ (2:ℕ) + (1/2) * d 0 0 * h 4 + (1/2) * d 0 3 * d 2 0 + (1/2) * d 0 4 * d 2 2 + (1/2) * d 1 3 * d 2 2 + (1/2) * d 1 4 * d 2 1 + (1/2) * h 3 * s 1 2 2 + (1/2) * h 4 * s 0 2 2 - d 0 4 * d 1 3 - h 0 * s 0 0 0 - h 0 * s 0 0 1 - h 0 * s 0 2 3 - h 1 * s 1 1 0 - h 1 * s 1 1 1 - h 1 * s 1 2 4 - h 2 * s 0 1 0 - h 2 * s 0 1 1 - 3 * d 0 1 * h 4 - 3 * d 1 3 * h 0 - 2 * d 2 1 * h 2 - 2 * d 2 2 * h 0 - 2 * d 2 3 * h 4 + 2 * d 2 0 * h 2 + 2 * d 2 2 * h 1 + 2 * d 2 4 * h 3 + 3 * d 0 4 * h 1 + 3 * d 1 0 * h 3 + 22 * h 0 * h 1 - (15/2) * d 1 3 * h 1 - (9/2) * d 0 3 * h 2 - (7/2) * d 0 2 * h 3 - (1/2) * d 0 0 * d 0 1 - (1/2) * d 0 0 * d 1 2 - (1/2) * d 0 0 * d 2 3 - (1/2) * d 0 1 * d 1 2 - (1/2) * d 0 2 * d 1 0 - (1/2) * d 0 2 * d 1 1 - (1/2) * d 0 2 * d 2 4 - (1/2) * d 1 0 * d 1 1 - (1/2) * d 1 1 * d 2 4 - (1/2) * d 1 1 * h 3 - (1/2) * d 1 2 * d 2 3 - (1/2) * d 2 0 * d 2 1 - (1/2) * h 0 * s 1 1 0 - (1/2) * h 0 * s 1 1 1 - (1/2) * h 0 * s 1 2 4 - (1/2) * h 1 * s 0 0 0 - (1/2) * h 1 * s 0 0 1 - (1/2) * h 1 * s 0 2 3 - (1/2) * h 2 * s 0 2 4 - (1/2) * h 2 * s 1 2 3 - (1/2) * h 3 * s 0 0 3 - (1/2) * h 3 * s 0 2 1 - (1/2) * h 3 * s 1 1 3 - (1/2) * h 3 * s 2 2 3 - (1/2) * h 4 * s 0 0 4 - (1/2) * h 4 * s 1 1 4 - (1/2) * h 4 * s 1 2 0 - (1/2) * h 4 * s 2 2 4 + (7/2) * d 1 2 * h 4 + (9/2) * d 1 4 * h 2 + (15/2) * d 0 4 * h 0)]]

/-- the scalar series' coefficient of `ε^0`, in the fifty jet coordinates -/
def scT0 (h : Fin 5 → K) (d : Fin 3 → Fin 5 → K) (s : Fin 3 → Fin 3 → Fin 5 → K) : K :=
  (6)

/-- the scalar series' coefficient of `ε^1`, in the fifty jet coordinates -/
def scT1 (h : Fin 5 → K) (d : Fin 3 → Fin 5 → K) (s : Fin 3 → Fin 3 → Fin 5 → K) : K :=
  (s 0 0 0 + s 1 1 1 - s 2 2 0 - s 2 2 1 + 2 * s 0 1 2 + 2 * s 0 2 3 + 2 * s 1 2 4)

/-- the scalar series' coefficient of `ε^2`, in the fifty jet coordinates -/
def scT2 (h : Fin 5 → K) (d : Fin 3 → Fin 5 → K) (s : Fin 3 → Fin 3 → Fin 5 → K) : K :=
  (-(d 0 0) ^ (2:ℕ) - (d 0 2) ^ (2:ℕ) - (d 0 3) ^ (2:ℕ) - (d 1 1) ^ (2:ℕ) - (d 1 2) ^ (2:ℕ) - (d 1 4) ^ (2:ℕ) - (d 2 0) ^ (2:ℕ) - (d 2 1) ^ (2:ℕ) - (d 2 3) ^ (2:ℕ) - (d 2 4) ^ (2:ℕ) - 4 * (h 0) ^ (2:ℕ) - 4 * (h 1) ^ (2:ℕ) - 4 * (h 2) ^ (2:ℕ) - 4 * (h 3) ^ (2:ℕ) - 4 * (h 4) ^ (2:ℕ) - (1/2) * (d 0 1) ^ (2:ℕ) - (1/2) * (d 0 4) ^ (2:ℕ) - (1/2) * (d 1 0) ^ (2:ℕ) - (1/2) * (d 1 3) ^ (2:ℕ) - (1/2) * (d 2 2) ^ (2:ℕ) + d 0 3 * d 2 0 + d 0 3 * d 2 1 + d 1 4 * d 2 0 + d 1 4 * d 2 1 + h 0 * s 1 2 4 + h 1 * s 0 2 3 + h 3 * s 0 2 1 + h 4 * s 1 2 0 - d 0 0 * d 1 2 - d 0 0 * d 2 3 - d 0 2 * d 1 1 - d 0 2 * d 2 4 - d 0 3 * d 1 4 - d 1 1 * d 2 4 - d 1 2 * d 2 3 - h 0 * s 0 0 0 - h 0 * s 0 1 2 - h 0 * s 2 2 0 - h 0 * s 2 2 1 - h 1 * s 0 1 2 - h 1 * s 1 1 1 - h 1 * s 2 2 0 - h 1 * s 2 2 1 - h 2 * s 0 0 2 - h 2 * s 0 1 0 - h 2 * s 0 1 1 - h 2 * s 0 2 4 - h 2 * s 1 1 2 - h 2 * s 1 2 3 - h 3 * s 0 0 3 - h 3 * s 0 1 4 - h 3 * s 1 2 2 - h 3 * s 2 2 3 - h 4 * s 0 1 3 - h 4 * s 0 2 2 - h 4 * s 1 1 4 - h 4 * s 2 2 4 - 4 * d 0 4 * h 1 - 4 * d 1 0 * h 3 - 4 * h 0 * h 1 - 2 * d 0 3 * h 2 - 2 * d 0 4 * h 0 - 2 * d 1 1 * h 3 - 2 * d 1 2 * h 4 - 2 * d 2 1 * h 2 - 2 * d 2 2 * h 0 - 2 * d 2 4 * h 3 + 2 * d 0 0 * h 4 + 2 * d 0 2 * h 3 + 2 * d 1 3 * h 1 + 2 * d 1 4 * h 2 + 2 * d 2 0 * h 2 + 2 * d 2 2 * h 1 + 2 * d 2 3 * h 4 + 4 * d 0 1 * h 4 + 4 * d 1 3 * h 0 - (3/2) * d 2 0 * d 2 1 - (1/2) * d 0 0 * d 0 1 - (1/2) * d 1 0 * d 1 1)

variable (h : Fin 5 → K) (d : Fin 3 → Fin 5 → K) (s : Fin 3 → Fin 3 → Fin 5 → K)

theorem Gk_0 : ∀ a b, Gk h 0 a b = gkT0 h a b := by
  intro a b; fin_cases a <;> fin_cases b <;> simp [Gk, Pw, Hm, gkT0, Matrix.mul_apply, Fin.sum_univ_three, Nat.factorial] <;> ring
theorem Gik_0 : ∀ a b, Gik h 0 a b = gikT0 h a b := by
  intro a b; fin_cases a <;> fin_cases b <;> simp [Gik, Pw, Hm, gikT0, Matrix.mul_apply, Fin.sum_univ_three, Nat.factorial] <;> ring

theorem Gk_1 : ∀ a b, Gk h 1 a b = gkT1 h a b := by
  intro a b; fin_cases a <;> fin_cases b <;> simp [Gk, Pw, Hm, gkT1, Matrix.mul_apply, Fin.sum_univ_three, Nat.factorial] <;> ring
theorem Gik_1 : ∀ a b, Gik h 1 a b = gikT1 h a b := by
  intro a b; fin_cases a <;> fin_cases b <;> simp [Gik, Pw, Hm, gikT1, Matrix.mul_apply, Fin.sum_univ_three, Nat.factorial] <;> ring

theorem Gk_2 : ∀ a b, Gk h 2 a b = gkT2 h a b := by
  intro a b; fin_cases a <;> fin_cases b <;> simp [Gk, Pw, Hm, gkT2, Matrix.mul_apply, Fin.sum_univ_three, Nat.factorial] <;> ring
theorem Gik_2 : ∀ a b, Gik h 2 a b = gikT2 h a b := by
  intro a b; fin_cases a <;> fin_cases b <;> simp [Gik, Pw, Hm, gikT2, Matrix.mul_apply, Fin.sum_univ_three, Nat.factorial] <;> ring

theorem Gl_0 (hd : ∀ a i, F.D a (h i) = d a i) (hs : ∀ a c i, F.D a (d c i) = DDt d s a c i) : ∀ a b c, Gl F h 0 a b c = glT0 h d a b c := by
  intro a b c; fin_cases a <;> fin_cases b <;> fin_cases c <;>
    simp [Gl, Gk_0, gkT0, glT0, Fin.sum_univ_three, F.add, F.mul, F.sub, F.neg, F.zero, F.one, F.ofNat, F.inv_ofNat, F.div_ofNat, F.sq, F.cube, F.quart, hd, hs, DDt, cst] <;> ring

theorem Gl_1 (hd : ∀ a i, F.D a (h i) = d a i) (hs : ∀ a c i, F.D a (d c i) = DDt d s a c i) : ∀ a b c, Gl F h 1 a b c = glT1 h d a b c := by
  intro a b c; fin_cases a <;> fin_cases b <;> fin_cases c <;>
    simp [Gl, Gk_1, gkT1, glT1, Fin.sum_univ_three, F.add, F.mul, F.sub, F.neg, F.zero, F.one, F.ofNat, F.inv_ofNat, F.div_ofNat, F.sq, F.cube, F.quart, hd, hs, DDt, cst] <;> ring

theorem Gl_2 (hd : ∀ a i, F.D a (h i) = d a i) (hs : ∀ a c i, F.D a (d c i) = DDt d s a c i) : ∀ a b c, Gl F h 2 a b c = glT2 h d a b c := by
  intro a b c; fin_cases a <;> fin_cases b <;> fin_cases c <;>
    simp [Gl, Gk_2, gkT2, glT2, Fin.sum_univ_three, F.add, F.mul, F.sub, F.neg, F.zero, F.one, F.ofNat, F.inv_ofNat, F.div_ofNat, F.sq, F.cube, F.quart, hd, hs, DDt, cst] <;> ring

theorem Gam_0 (hd : ∀ a i, F.D a (h i) = d a i) (hs : ∀ a c i, F.D a (d c i) = DDt d s a c i) : ∀ e a b, Gam F h 0 e a b = gamT0 h d e a b := by
  intro e a b; fin_cases e <;> fin_cases a <;> fin_cases b <;>
    simp [Gam, Finset.sum_range_succ, Gik_0, Gik_1, Gik_2, Gl_0 F h d s hd hs, Gl_1 F h d s hd hs, Gl_2 F h d s hd hs, gikT0, glT0, gamT0, Fin.sum_univ_three] <;> ring

theorem Gam_1 (hd : ∀ a i, F.D a (h i) = d a i) (hs : ∀ a c i, F.D a (d c i) = DDt d s a c i) : ∀ e a b, Gam F h 1 e a b = gamT1 h d e a b := by
  intro e a b; fin_cases e <;> fin_cases a <;> fin_cases b <;>
    simp [Gam, Finset.sum_range_succ, Gik_0, Gik_1, Gik_2, Gl_0 F h d s hd hs, Gl_1 F h d s hd hs, Gl_2 F h d s hd hs, gikT0, gikT1, glT0, glT1, gamT1, Fin.sum_univ_three] <;> ring

theorem Gam_2 (hd : ∀ a i, F.D a (h i) = d a i) (hs : ∀ a c i, F.D a (d c i) = DDt d s a c i) : ∀ e a b, Gam F h 2 e a b = gamT2 h d e a b := by
  intro e a b; fin_cases e <;> fin_cases a <;> fin_cases b <;>
    simp [Gam, Finset.sum_range_succ, Gik_0, Gik_1, Gik_2, Gl_0 F h d s hd hs, Gl_1 F h d s hd hs, Gl_2 F h d s hd hs, gikT0, gikT1, gikT2, glT0, glT1, glT2, gamT2, Fin.sum_univ_three] <;> ring

theorem Ric_0 (hd : ∀ a i, F.D a (h i) = d a i) (hs : ∀ a c i, F.D a (d c i) = DDt d s a c i) : ∀ b c, Ric F h 0 b c = ricT0 h d s b c := by
  intro b c; fin_cases b <;> fin_cases c <;>
    simp [Ric, Rm, Finset.sum_range_succ, Gam_0 F h d s hd hs, Gam_1 F h d s hd hs, Gam_2 F h d s hd hs, gamT0, ricT0, Fin.sum_univ_three, F.add, F.mul, F.sub, F.neg, F.zero, F.one, F.ofNat, F.inv_ofNat, F.div_ofNat, F.sq, F.cube, F.quart, hd, hs, DDt, cst] <;> ring

theorem Ric_1 (hd : ∀ a i, F.D a (h i) = d a i) (hs : ∀ a c i, F.D a (d c i) = DDt d s a c i) : ∀ b c, Ric F h 1 b c = ricT1 h d s b c := by
  intro b c; fin_cases b <;> fin_cases c <;>
    simp [Ric, Rm, Finset.sum_range_succ, Gam_0 F h d s hd hs, Gam_1 F h d s hd hs, Gam_2 F h d s hd hs, gamT0, gamT1, ricT1, Fin.sum_univ_three, F.add, F.mul, F.sub, F.neg, F.zero, F.one, F.ofNat, F.inv_ofNat, F.div_ofNat, F.sq, F.cube, F.quart, hd, hs, DDt, cst] <;> ring

theorem Ric_2 (hd : ∀ a i, F.D a (h i) = d a i) (hs : ∀ a c i, F.D a (d c i) = DDt d s a c i) : ∀ b c, Ric F h 2 b c = ricT2 h d s b c := by
  intro b c; fin_cases b <;> fin_cases c <;>
    simp [Ric, Rm, Finset.sum_range_succ, Gam_0 F h d s hd hs, Gam_1 F h d s hd hs, Gam_2 F h d s hd hs, gamT0, gamT1, gamT2, ricT2, Fin.sum_univ_three, F.add, F.mul, F.sub, F.neg, F.zero, F.one, F.ofNat, F.inv_ofNat, F.div_ofNat, F.sq, F.cube, F.quart, hd, hs, DDt, cst] <;> ring

/-- ⛭ **(J1, orders 0–2)** row 62's `jet_series`, restricted to the orders Part B needs: for any three derivations
with `D_a h = d_a` and `D_a d_c = DDt d s a c`, the frame-Koszul scalar of `exp(εH)` has coefficients `scT0, scT1,
scT2`. -/
theorem jet_series_le2 (hd : ∀ a i, F.D a (h i) = d a i) (hs : ∀ a c i, F.D a (d c i) = DDt d s a c i) :
    Scal F h 0 = scT0 h d s ∧ Scal F h 1 = scT1 h d s ∧ Scal F h 2 = scT2 h d s := by
  refine ⟨?_, ?_, ?_⟩ <;>
    simp [Scal, Finset.sum_range_succ, Gik_0, Gik_1, Gik_2, Ric_0 F h d s hd hs, Ric_1 F h d s hd hs, Ric_2 F h d s hd hs, gikT0, ricT0, gikT1, ricT1, gikT2, ricT2, scT0, scT1, scT2, Fin.sum_univ_three] <;> ring


end Jet

/-! ### the TT variety, the contractions, and the identity on the variety -/

section SecondOrder

open Jet

variable {K : Type*} [Field K] [CharZero K]

/-- `ε_abc` over `K` (the literal of row 62's `cst`, without its factor 2) -/
def epsK (a b c : Fin 3) : K := (Matrix.of ![![![0, 0, 0], ![0, 0, 1], ![0, -1, 0]],
  ![![0, 0, -1], ![0, 0, 0], ![1, 0, 0]], ![![0, 1, 0], ![-1, 0, 0], ![0, 0, 0]]] a b c : K)

/-- the transverse-traceless constraint variety in row 62's jet coordinates. Tracelessness is built into `Hm`.
Transversality is `Σ_a (D_a H)_ab = 0`, and its frame derivative is `Σ_a (D_c D_a H)_ab = 0`. The commutator
constraint is built into `DDt`. (Checked in sympy, not here: the receipt's covariant TT jets map into this variety
under its `to_frame`, and both have dimension 38.) -/
def TT (h : Fin 5 → K) (d : Fin 3 → Fin 5 → K) (s : Fin 3 → Fin 3 → Fin 5 → K) : Prop :=
  (∀ b, ∑ a, Hm (d a) a b = 0) ∧ (∀ c b, ∑ a, Hm (DDt d s c a) a b = 0)

/-- the covariant derivative `∇_c h_ab = (D_c H)_ab − ε_cax h_xb − ε_cbx h_ax` (the receipt's `Dframe`) -/
def nab (h : Fin 5 → K) (d : Fin 3 → Fin 5 → K) (c a b : Fin 3) : K :=
  Hm (d c) a b - ∑ x, (epsK c a x * Hm h x b + epsK c b x * Hm h a x)

/-- `∇_a h_bc ∇_a h_bc` -/
def G1 (h : Fin 5 → K) (d : Fin 3 → Fin 5 → K) : K := ∑ a, ∑ b, ∑ c, nab h d a b c ^ 2
/-- the mixed contraction `∇_a h_bc ∇_b h_ac` -/
def Gm (h : Fin 5 → K) (d : Fin 3 → Fin 5 → K) : K := ∑ a, ∑ b, ∑ c, nab h d a b c * nab h d b a c
/-- `h_ab h_ab` -/
def H1 (h : Fin 5 → K) : K := ∑ a, ∑ b, Hm h a b ^ 2

theorem G1_eq (h : Fin 5 → K) (d : Fin 3 → Fin 5 → K) : G1 h d = (2 * (d 0 0) ^ (2:ℕ) + 2 * (d 0 1) ^ (2:ℕ) + 2 * (d 0 2) ^ (2:ℕ) + 2 * (d 0 3) ^ (2:ℕ) + 2 * (d 0 4) ^ (2:ℕ) + 2 * (d 1 0) ^ (2:ℕ) + 2 * (d 1 1) ^ (2:ℕ) + 2 * (d 1 2) ^ (2:ℕ) + 2 * (d 1 3) ^ (2:ℕ) + 2 * (d 1 4) ^ (2:ℕ) + 2 * (d 2 0) ^ (2:ℕ) + 2 * (d 2 1) ^ (2:ℕ) + 2 * (d 2 2) ^ (2:ℕ) + 2 * (d 2 3) ^ (2:ℕ) + 2 * (d 2 4) ^ (2:ℕ) + 12 * (h 0) ^ (2:ℕ) + 12 * (h 1) ^ (2:ℕ) + 12 * (h 2) ^ (2:ℕ) + 12 * (h 3) ^ (2:ℕ) + 12 * (h 4) ^ (2:ℕ) - 8 * d 0 1 * h 4 - 8 * d 1 3 * h 0 - 4 * d 0 0 * h 4 - 4 * d 0 2 * h 3 - 4 * d 1 3 * h 1 - 4 * d 1 4 * h 2 - 4 * d 2 0 * h 2 - 4 * d 2 2 * h 1 - 4 * d 2 3 * h 4 + 2 * d 0 0 * d 0 1 + 2 * d 1 0 * d 1 1 + 2 * d 2 0 * d 2 1 + 4 * d 0 3 * h 2 + 4 * d 0 4 * h 0 + 4 * d 1 1 * h 3 + 4 * d 1 2 * h 4 + 4 * d 2 1 * h 2 + 4 * d 2 2 * h 0 + 4 * d 2 4 * h 3 + 8 * d 0 4 * h 1 + 8 * d 1 0 * h 3 + 12 * h 0 * h 1) := by
  simp [G1, nab, epsK, Hm, Fin.sum_univ_three] <;> ring
theorem Gm_eq (h : Fin 5 → K) (d : Fin 3 → Fin 5 → K) : Gm h d = ((d 0 0) ^ (2:ℕ) + (d 0 2) ^ (2:ℕ) + (d 0 3) ^ (2:ℕ) + (d 1 1) ^ (2:ℕ) + (d 1 2) ^ (2:ℕ) + (d 1 4) ^ (2:ℕ) + (d 2 0) ^ (2:ℕ) + (d 2 1) ^ (2:ℕ) + (d 2 3) ^ (2:ℕ) + (d 2 4) ^ (2:ℕ) - 6 * (h 0) ^ (2:ℕ) - 6 * (h 1) ^ (2:ℕ) - 6 * (h 2) ^ (2:ℕ) - 6 * (h 3) ^ (2:ℕ) - 6 * (h 4) ^ (2:ℕ) - 6 * h 0 * h 1 - 4 * d 0 4 * h 1 - 4 * d 1 0 * h 3 - 2 * d 0 0 * d 2 3 - 2 * d 0 1 * d 2 3 - 2 * d 0 3 * h 2 - 2 * d 0 4 * h 0 - 2 * d 1 0 * d 2 4 - 2 * d 1 1 * d 2 4 - 2 * d 1 1 * h 3 - 2 * d 1 2 * h 4 - 2 * d 2 1 * h 2 - 2 * d 2 2 * h 0 - 2 * d 2 4 * h 3 + 2 * d 0 0 * h 4 + 2 * d 0 1 * d 1 2 + 2 * d 0 2 * d 1 0 + 2 * d 0 2 * h 3 + 2 * d 0 3 * d 2 0 + 2 * d 0 4 * d 1 3 + 2 * d 0 4 * d 2 2 + 2 * d 1 3 * d 2 2 + 2 * d 1 3 * h 1 + 2 * d 1 4 * d 2 1 + 2 * d 1 4 * h 2 + 2 * d 2 0 * d 2 1 + 2 * d 2 0 * h 2 + 2 * d 2 2 * h 1 + 2 * d 2 3 * h 4 + 4 * d 0 1 * h 4 + 4 * d 1 3 * h 0) := by
  simp [Gm, nab, epsK, Hm, Fin.sum_univ_three] <;> ring
theorem H1_eq (h : Fin 5 → K) : H1 h = (2 * (h 0) ^ (2:ℕ) + 2 * (h 1) ^ (2:ℕ) + 2 * (h 2) ^ (2:ℕ) + 2 * (h 3) ^ (2:ℕ) + 2 * (h 4) ^ (2:ℕ) + 2 * h 0 * h 1) := by
  simp [H1, Hm, Fin.sum_univ_three] <;> ring

/-- ⛭ **(B1) THE SECOND-ORDER IDENTITY, ON THE VARIETY.** On every transverse-traceless jet,
`[ε²] R = −¼ ∇_a h_bc ∇_a h_bc − ½ h_ab h_ab`. The proof is an explicit combination of the twelve linear
constraints (polynomial multipliers generated by sympy and checked here by `ring`), so it is not a fit. -/
theorem second_order_identity (h : Fin 5 → K) (d : Fin 3 → Fin 5 → K) (s : Fin 3 → Fin 3 → Fin 5 → K)
    (hT : TT h d s) : scT2 h d s = -(1/4) * G1 h d + 0 * Gm h d - (1/2) * H1 h := by
  have t0 : d 0 0 + d 1 2 + d 2 3 = 0 := by
    have e := hT.1 0
    simp [Hm, DDt, Fin.sum_univ_three] at e
    first | linear_combination e | linear_combination -e
  have t1 : d 0 2 + d 1 1 + d 2 4 = 0 := by
    have e := hT.1 1
    simp [Hm, DDt, Fin.sum_univ_three] at e
    first | linear_combination e | linear_combination -e
  have t2 : d 0 3 + d 1 4 - d 2 0 - d 2 1 = 0 := by
    have e := hT.1 2
    simp [Hm, DDt, Fin.sum_univ_three] at e
    first | linear_combination e | linear_combination -e
  have u00 : d 2 2 + s 0 0 0 + s 0 1 2 + s 0 2 3 - d 1 3 = 0 := by
    have e := hT.2 0 0
    simp [Hm, DDt, Fin.sum_univ_three] at e
    first | linear_combination e | linear_combination -e
  have u01 : d 2 1 + s 0 0 2 + s 0 1 1 + s 0 2 4 - d 1 4 = 0 := by
    have e := hT.2 0 1
    simp [Hm, DDt, Fin.sum_univ_three] at e
    first | linear_combination e | linear_combination -e
  have u02 : d 1 0 + d 1 1 + d 2 4 + s 0 0 3 + s 0 1 4 - s 0 2 0 - s 0 2 1 = 0 := by
    have e := hT.2 0 2
    simp [Hm, DDt, Fin.sum_univ_three] at e
    first | linear_combination e | linear_combination -e
  have u10 : d 0 3 + s 0 1 0 + s 1 1 2 + s 1 2 3 - d 2 0 = 0 := by
    have e := hT.2 1 0
    simp [Hm, DDt, Fin.sum_univ_three] at e
    first | linear_combination e | linear_combination -e
  have u11 : d 0 4 + s 0 1 2 + s 1 1 1 + s 1 2 4 - d 2 2 = 0 := by
    have e := hT.2 1 1
    simp [Hm, DDt, Fin.sum_univ_three] at e
    first | linear_combination e | linear_combination -e
  have u12 : s 0 1 3 + s 1 1 4 - d 0 0 - d 0 1 - d 2 3 - s 1 2 0 - s 1 2 1 = 0 := by
    have e := hT.2 1 2
    simp [Hm, DDt, Fin.sum_univ_three] at e
    first | linear_combination e | linear_combination -e
  have u20 : d 1 0 + s 0 2 0 + s 1 2 2 + s 2 2 3 - d 0 2 = 0 := by
    have e := hT.2 2 0
    simp [Hm, DDt, Fin.sum_univ_three] at e
    first | linear_combination e | linear_combination -e
  have u21 : d 1 2 + s 0 2 2 + s 1 2 1 + s 2 2 4 - d 0 1 = 0 := by
    have e := hT.2 2 1
    simp [Hm, DDt, Fin.sum_univ_three] at e
    first | linear_combination e | linear_combination -e
  have u22 : d 1 3 + s 0 2 3 + s 1 2 4 - d 0 4 - s 2 2 0 - s 2 2 1 = 0 := by
    have e := hT.2 2 2
    simp [Hm, DDt, Fin.sum_univ_three] at e
    first | linear_combination e | linear_combination -e
  rw [G1_eq, H1_eq]; unfold scT2
  linear_combination (-(1/2) * d 0 0 - (1/2) * d 1 2 - (1/2) * d 2 3) * t0 + (-(1/2) * d 0 2 - (1/2) * d 1 1 - (1/2) * d 2 4) * t1 + ((1/2) * d 2 1 + (1/2) * s 0 1 0 + (1/2) * s 1 1 2 + (1/2) * s 1 2 3 - (1/2) * d 1 4) * t2 + (-h 0) * u00 + (-h 2) * u01 + (-h 3) * u02 + ((1/2) * d 2 0 + (1/2) * d 2 1 - h 2 - (1/2) * d 0 3 - (1/2) * d 1 4) * u10 + (-h 1) * u11 + (-h 4) * u12 + (-h 3) * u20 + (-h 4) * u21 + (h 0 + h 1) * u22


/-- ⛭ **(B2) THE COEFFICIENTS ARE FORCED: THE MIXED ONE IS `0`.** If `scT2 = α G1 + β Gm + γ H1` on the whole TT
variety, then `(α, β, γ) = (−¼, 0, −½)`. Three rational TT jets give a nonsingular system (determinant `−191472`). -/
theorem B_unique (α β γ : ℚ)
    (H : ∀ (h : Fin 5 → ℚ) d s, TT h d s → scT2 h d s = α * G1 h d + β * Gm h d + γ * H1 h) :
    α = -1/4 ∧ β = 0 ∧ γ = -1/2 := by
  have e0 := H ![2, 0, 0, 2, -2]
    ![![1, 0, -2, -1, -1], ![2, 1, -1, -2, -2], ![-2, -1, -2, 0, 1]]
    ![![![-2, -1, 2, -6, 1], ![2, -2, 2, 2, -1], ![-2, -1, 1, 0, -1]], ![![0, 0, 0, 0, 0], ![1, -1, -2, -1, 2], ![2, 1, -1, -1, -2]], ![![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![-2, -1, -1, -1, -1]]] (by
      refine ⟨fun b => ?_, fun c b => ?_⟩ <;> (try fin_cases c) <;> fin_cases b <;>
        simp [Hm, DDt, Fin.sum_univ_three] <;> norm_num)
  have e1 := H ![0, 0, -1, 2, -1]
    ![![1, -3, 0, 0, -1], ![-3, -1, -1, -4, 1], ![1, 0, -2, 0, 1]]
    ![![![-4, -1, 3, 7, -1], ![0, -2, 0, -4, 0], ![2, 2, -2, 2, 0]], ![![0, 0, 0, 0, 0], ![-2, 0, 0, 0, 1], ![0, -1, 1, 1, -1]], ![![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![-2, 0, -2, 0, 1]]] (by
      refine ⟨fun b => ?_, fun c b => ?_⟩ <;> (try fin_cases c) <;> fin_cases b <;>
        simp [Hm, DDt, Fin.sum_univ_three] <;> norm_num)
  have e2 := H ![-2, 2, 1, 0, 1]
    ![![0, -3, -1, 0, -3], ![-7, 2, -2, -2, -1], ![1, -2, -1, 2, -1]]
    ![![![-1, -2, -1, 8, -1], ![1, 0, 2, 0, 0], ![2, 0, 1, -2, 2]], ![![0, 0, 0, 0, 0], ![0, 0, -2, 1, -2], ![-1, 0, 2, 2, 0]], ![![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![-1, 0, 0, 2, -2]]] (by
      refine ⟨fun b => ?_, fun c b => ?_⟩ <;> (try fin_cases c) <;> fin_cases b <;>
        simp [Hm, DDt, Fin.sum_univ_three] <;> norm_num)
  simp [scT2, G1_eq, Gm_eq, H1_eq] at e0 e1 e2
  norm_num at e0 e1 e2
  refine ⟨by linarith, by linarith, by linarith⟩

/-- the identity for the scalar curvature itself: with any derivations realising the jet (`D_a h = d_a`,
`D_a d_c = DDt d s a c`), the `ε²` coefficient `Scal F h 2` of the frame-Koszul scalar of `exp(εH)` satisfies it -/
theorem scal_second_order (F : FD K) (h : Fin 5 → K) (d : Fin 3 → Fin 5 → K) (s : Fin 3 → Fin 3 → Fin 5 → K)
    (hd : ∀ a i, F.D a (h i) = d a i) (hs : ∀ a c i, F.D a (d c i) = DDt d s a c i) (hT : TT h d s) :
    Scal F h 2 = -(1/4) * G1 h d + 0 * Gm h d - (1/2) * H1 h := by
  rw [(jet_series_le2 F h d s hd hs).2.2]; exact second_order_identity h d s hT

/-- ⛭ **(B3) CONTROL: THE FRAME-CONSTANT VALUE.** A frame-constant `h` (`d = s = 0`) lies on the variety. There
both `scT2` and the identity's right side equal `−2 tr h²`. -/
theorem control_frame_constant (h : Fin 5 → K) :
    TT h 0 0 ∧ scT2 h 0 0 = -2 * (Hm h ^ 2).trace ∧
      -(1/4) * G1 h 0 + 0 * Gm h 0 - (1/2) * H1 h = -2 * (Hm h ^ 2).trace := by
  refine ⟨⟨fun b => ?_, fun c b => ?_⟩, ?_, ?_⟩
  · fin_cases b <;> simp [Hm, Fin.sum_univ_three]
  · fin_cases c <;> fin_cases b <;> simp [Hm, DDt, Fin.sum_univ_three]
  · simp [scT2, Hm, pow_succ, Matrix.trace, Fin.sum_univ_three, Matrix.mul_apply]; ring
  · rw [G1_eq, Gm_eq, H1_eq]; simp [Hm, pow_succ, Matrix.trace, Fin.sum_univ_three, Matrix.mul_apply]; ring

#print axioms second_order_identity
#print axioms B_unique
#print axioms scal_second_order
#print axioms control_frame_constant

end SecondOrder

/-! ### the Euler-box control, with row 59's integrals copied verbatim from `probes/Row59Series.lean`

`uR`, `box`, `sin_four_pi`, `i_phi`, `i_theta` and `row_unit` are copied unchanged. `box_R2` is the `−16π²`
component of row 59's `section_e_integrals`, with its proof copied unchanged. -/

namespace Box

open Real intervalIntegral

/-- `Rad`'s first row on the Euler chart (campaign 24's `Rad ψ θ φ 0 ·`) -/
noncomputable def uR (ψ θ φ : ℝ) : Fin 3 → ℝ :=
  ![cos φ * cos ψ - sin φ * sin ψ * cos θ, -(sin φ * cos ψ * cos θ) - sin ψ * cos φ, sin φ * sin θ]

/-- the box integral with the round volume `sin θ / 8`, over `[0, 2π] × [0, π] × [0, 4π]` -/
noncomputable def box (P : (Fin 3 → ℝ) → ℝ) : ℝ :=
  ∫ ψ in (0 : ℝ)..2 * π, ∫ θ in (0 : ℝ)..π, ∫ φ in (0 : ℝ)..4 * π, P (uR ψ θ φ) * (sin θ / 8)

theorem sin_four_pi : sin (4 * π) = 0 := by
  rw [show (4 : ℝ) * π = ((4 : ℕ) : ℝ) * π by norm_num]; exact sin_nat_mul_pi 4

theorem i_phi (A B C : ℝ) :
    ∫ φ in (0 : ℝ)..4 * π, (A + B * sin φ ^ 2 + C * sin φ ^ 4) = 4 * π * A + 2 * π * B + 3 * π / 2 * C := by
  have h2 : ∫ φ in (0 : ℝ)..4 * π, sin φ ^ 2 = 2 * π := by
    rw [integral_sin_sq, sin_four_pi]; simp; ring
  have h4 : ∫ φ in (0 : ℝ)..4 * π, sin φ ^ 4 = 3 * π / 2 := by
    have := @integral_sin_pow 0 (4 * π) 2
    norm_num at this; rw [this, sin_four_pi]; ring
  rw [integral_add, integral_add, integral_const_mul, integral_const_mul, h2, h4]
  all_goals first | (simp; ring1) | (apply Continuous.intervalIntegrable; fun_prop)

theorem i_theta (A B C : ℝ) :
    ∫ θ in (0 : ℝ)..π, (A * sin θ + B * sin θ ^ 3 + C * sin θ ^ 5) = 2 * A + 4 / 3 * B + 16 / 15 * C := by
  have h1 : ∫ θ in (0 : ℝ)..π, sin θ = 2 := by rw [integral_sin]; norm_num
  have h3 : ∫ θ in (0 : ℝ)..π, sin θ ^ 3 = 4 / 3 := by
    have := @integral_sin_pow 0 π 1; norm_num at this ⊢
  have h5 : ∫ θ in (0 : ℝ)..π, sin θ ^ 5 = 16 / 15 := by
    have := @integral_sin_pow 0 π 3; norm_num at this ⊢; exact this
  rw [integral_add, integral_add, integral_const_mul, integral_const_mul, integral_const_mul, h1, h3, h5]
  all_goals first | ring1 | (apply Continuous.intervalIntegrable; fun_prop)
theorem row_unit (ψ θ φ : ℝ) : uR ψ θ φ 0 ^ 2 + uR ψ θ φ 1 ^ 2 = 1 - sin φ ^ 2 * sin θ ^ 2 := by
  simp [uR]
  linear_combination (cos φ ^ 2 + sin φ ^ 2 * cos θ ^ 2) * sin_sq_add_cos_sq ψ + sin φ ^ 2 * sin_sq_add_cos_sq θ
    + sin_sq_add_cos_sq φ

/-- row 59's `section_e_integrals`, third component (proof copied verbatim): the `ε²` coefficient `R₂` of the
frame scalar on `H4`, integrated over the Euler box, is `−16π²` -/
theorem box_R2 : box (fun u => -10 * u 0 ^ 2 - 10 * u 1 ^ 2 - 4 * u 2 ^ 2) = -16 * π ^ 2 := by
  · have hp : ∀ ψ θ φ : ℝ, (-10 * uR ψ θ φ 0 ^ 2 - 10 * uR ψ θ φ 1 ^ 2 - 4 * uR ψ θ φ 2 ^ 2) * (sin θ / 8)
        = (-(5 / 4) * sin θ + 3 / 4 * sin θ ^ 3 * sin φ ^ 2 + 0 * sin φ ^ 4) := fun ψ θ φ => by
      have := row_unit ψ θ φ; simp only [uR] at this ⊢; simp at this ⊢
      linear_combination (-10 / 8 * sin θ) * this
    simp only [box, hp, i_phi]
    have hq : ∀ θ : ℝ, 4 * π * (-(5 / 4) * sin θ) + 2 * π * (3 / 4 * sin θ ^ 3) + 3 * π / 2 * 0
        = (-5 * π) * sin θ + (3 / 2 * π) * sin θ ^ 3 + 0 * sin θ ^ 5 := fun θ => by ring
    simp only [hq, i_theta, integral_const]; simp; ring

/-- row 59's `H4` in row 62's jet coordinates: `H4 = [[−u₀, u₁, 0], [u₁, u₀, 0], [0, 0, 0]]` -/
def h4 {K : Type*} [Field K] (u : Fin 3 → K) : Fin 5 → K := ![-u 0, u 0, u 1, 0, 0]

/-- its frame derivatives: `D_a H4 = H4(u L_a)`, since row 59's chart link is `X_a u = u L_a` -/
def d4 {K : Type*} [Field K] (u : Fin 3 → K) (a : Fin 3) : Fin 5 → K :=
  h4 (fun j => ∑ m, u m * Jet.Lm a m j)

/-- `H4`'s first-order jet is transverse: `Σ_a (D_a H4)_ab = 0` -/
theorem h4_transverse {K : Type*} [Field K] [CharZero K] (u : Fin 3 → K) :
    ∀ b, ∑ a, Jet.Hm (d4 u a) a b = 0 := by
  intro b; fin_cases b <;> simp [d4, h4, Jet.Hm, Jet.Lm, Fin.sum_univ_three] <;> ring

/-- on `H4` the identity's right side is, pointwise, row 59's `R₂` integrand `−10u₀² − 10u₁² − 4u₂²` -/
theorem h4_formula {K : Type*} [Field K] [CharZero K] (u : Fin 3 → K) :
    -(1/4) * G1 (h4 u) (d4 u) + 0 * Gm (h4 u) (d4 u) - (1/2) * H1 (h4 u)
      = -10 * u 0 ^ 2 - 10 * u 1 ^ 2 - 4 * u 2 ^ 2 := by
  rw [G1_eq, Gm_eq, H1_eq]; simp [d4, h4, Jet.Lm, Fin.sum_univ_three]; ring

/-- ⛭ **(B4) CONTROL: THE EULER-BOX ANCHOR.** On row 59's position-dependent harmonic `H4`, the second-order
identity's right side integrates over the Euler box to `−16π²`, row 59's value for the scalar's `ε²` coefficient. -/
theorem control_euler_box :
    box (fun u => -(1/4) * G1 (h4 u) (d4 u) + 0 * Gm (h4 u) (d4 u) - (1/2) * H1 (h4 u)) = -16 * π ^ 2 := by
  have e : (fun u : Fin 3 → ℝ => -(1/4) * G1 (h4 u) (d4 u) + 0 * Gm (h4 u) (d4 u) - (1/2) * H1 (h4 u))
      = fun u => -10 * u 0 ^ 2 - 10 * u 1 ^ 2 - 4 * u 2 ^ 2 := funext h4_formula
  rw [e]; exact box_R2

#print axioms control_euler_box

end Box

/-- ⛭ **(B) THE SECOND-ORDER IDENTITY, WITH ITS CONTROLS.** On the TT variety, `[ε²] R = −¼|∇h|² + 0·mixed − ½|h|²`
(for the scalar itself, via row 62's jet series). These coefficients are the only ones that work. The frame-constant
control gives `−2 tr h²`, and the Euler-box control on `H4` gives `−16π²`. -/
theorem part_B :
    (∀ (h : Fin 5 → ℝ) d s, TT h d s → Jet.scT2 h d s = -(1/4) * G1 h d + 0 * Gm h d - (1/2) * H1 h) ∧
    (∀ α β γ : ℚ, (∀ (h : Fin 5 → ℚ) d s, TT h d s → Jet.scT2 h d s = α * G1 h d + β * Gm h d + γ * H1 h) →
      α = -1/4 ∧ β = 0 ∧ γ = -1/2) ∧
    (∀ h : Fin 5 → ℝ, -(1/4) * G1 h 0 + 0 * Gm h 0 - (1/2) * H1 h = -2 * (Jet.Hm h ^ 2).trace) ∧
    Box.box (fun u => -(1/4) * G1 (Box.h4 u) (Box.d4 u) + 0 * Gm (Box.h4 u) (Box.d4 u) - (1/2) * H1 (Box.h4 u))
      = -16 * Real.pi ^ 2 :=
  ⟨fun h d s hT => second_order_identity h d s hT, B_unique, fun h => (control_frame_constant h).2.2,
    Box.control_euler_box⟩

#print axioms part_B

/-! ## (C) the seven level values, from the `3⁵`-index sums -/

section Levels

/-- the `C ⊗ A` Wick pairing of a contraction `p`: both derivatives on one level's harmonic, both bare `h`'s on
another's. A sum over the `3⁵` assignments of the five summed indices. -/
def NC {R : Type*} [CommRing R] (p : Fin 10 → Fin 5) (C : Fin 3 → Fin 3 → Fin 3 → Fin 3 → Fin 3 → Fin 3 → R)
    (A : Fin 3 → Fin 3 → Fin 3 → Fin 3 → R) : R :=
  S3 fun x0 => S3 fun x1 => S3 fun x2 => S3 fun x3 => S3 fun x4 =>
    C (![x0, x1, x2, x3, x4] (p 0)) (![x0, x1, x2, x3, x4] (p 1)) (![x0, x1, x2, x3, x4] (p 2))
      (![x0, x1, x2, x3, x4] (p 3)) (![x0, x1, x2, x3, x4] (p 4)) (![x0, x1, x2, x3, x4] (p 5)) *
    A (![x0, x1, x2, x3, x4] (p 6)) (![x0, x1, x2, x3, x4] (p 7)) (![x0, x1, x2, x3, x4] (p 8))
      (![x0, x1, x2, x3, x4] (p 9))

/-- the two `B ⊗ B` Wick pairings of a contraction `p`, each differentiated harmonic paired with a bare one
(`B` on the first level, `B'` on the second) -/
def NB {R : Type*} [CommRing R] (p : Fin 10 → Fin 5) (B B' : Fin 3 → Fin 3 → Fin 3 → Fin 3 → Fin 3 → R) : R :=
  S3 fun x0 => S3 fun x1 => S3 fun x2 => S3 fun x3 => S3 fun x4 =>
    B (![x0, x1, x2, x3, x4] (p 0)) (![x0, x1, x2, x3, x4] (p 1)) (![x0, x1, x2, x3, x4] (p 2))
      (![x0, x1, x2, x3, x4] (p 6)) (![x0, x1, x2, x3, x4] (p 7)) *
    B' (![x0, x1, x2, x3, x4] (p 3)) (![x0, x1, x2, x3, x4] (p 4)) (![x0, x1, x2, x3, x4] (p 5))
      (![x0, x1, x2, x3, x4] (p 8)) (![x0, x1, x2, x3, x4] (p 9)) +
    B (![x0, x1, x2, x3, x4] (p 0)) (![x0, x1, x2, x3, x4] (p 1)) (![x0, x1, x2, x3, x4] (p 2))
      (![x0, x1, x2, x3, x4] (p 8)) (![x0, x1, x2, x3, x4] (p 9)) *
    B' (![x0, x1, x2, x3, x4] (p 3)) (![x0, x1, x2, x3, x4] (p 4)) (![x0, x1, x2, x3, x4] (p 5))
      (![x0, x1, x2, x3, x4] (p 6)) (![x0, x1, x2, x3, x4] (p 7))

/-- **IMPORTED: the Wick-tensor ansatz.** The level sum of a quartic contraction is its three Wick pairings, with
the level sums of harmonic products taken to be the invariant tensors of Part A, carrying the receipt's numbers:
`A = (deg/5)P`, `B = c_B B0`, `C = c_C C1 + λ·deg C2`. That level sums *are* these tensors (homogeneity, Schur) is
not proved here. -/
def levelValue (p : Fin 10 → Fin 5) (cC cB lam deg : ℝ) : ℝ :=
  NC p (Cten cC lam deg) (Aten deg) + NB p (Bten cB) (Bten cB)

/-- **IMPORTED (the same ansatz, across two levels):** the `(m, m′)` term of the tower double sum. The
differentiated pair comes from level `m` and the bare pair from level `m′`. -/
def crossValue (p : Fin 10 → Fin 5) (cC cB lam deg cB' deg' : ℝ) : ℝ :=
  NC p (Cten cC lam deg) (Aten deg') + NB p (Bten cB) (Bten cB')

theorem S3_lin (a b : ℝ) (f g : Fin 3 → ℝ) : S3 (fun x => a * f x + b * g x) = a * S3 f + b * S3 g := by
  simp only [S3]; ring
theorem S3_smul (a : ℝ) (f : Fin 3 → ℝ) : S3 (fun x => a * f x) = a * S3 f := by
  simp only [S3]; ring
theorem S3_cast (f : Fin 3 → ℤ) : S3 (fun x => (f x : ℝ)) = ((S3 f : ℤ) : ℝ) := by
  simp only [S3]; push_cast; ring

theorem NC_lin (p : Fin 10 → Fin 5) (C C' : Fin 3 → Fin 3 → Fin 3 → Fin 3 → Fin 3 → Fin 3 → ℤ)
    (A : Fin 3 → Fin 3 → Fin 3 → Fin 3 → ℤ) (x y w : ℝ) :
    NC p (fun i j k l m q => x * (C i j k l m q : ℝ) + y * (C' i j k l m q : ℝ)) (fun i j k l => w * (A i j k l : ℝ))
      = x * w * ((NC p C A : ℤ) : ℝ) + y * w * ((NC p C' A : ℤ) : ℝ) := by
  have hpt : ∀ c c' a : ℝ, (x * c + y * c') * (w * a) = (x * w) * (c * a) + (y * w) * (c' * a) := by
    intros; ring
  simp only [NC, hpt, ← Int.cast_mul, S3_lin, S3_cast]

theorem NB_lin (p : Fin 10 → Fin 5) (B : Fin 3 → Fin 3 → Fin 3 → Fin 3 → Fin 3 → ℤ) (x y : ℝ) :
    NB p (fun i j k l m => x * (B i j k l m : ℝ)) (fun i j k l m => y * (B i j k l m : ℝ))
      = x * y * ((NB p B B : ℤ) : ℝ) := by
  have hpt : ∀ b1 b2 b3 b4 : ℝ, x * b1 * (y * b2) + x * b3 * (y * b4) = (x * y) * (b1 * b2 + b3 * b4) := by
    intros; ring
  simp only [NB, hpt, ← Int.cast_mul, ← Int.cast_add, S3_smul, S3_cast]

/-- the integer `3⁵`-sums, by kernel evaluation, one pattern at a time: `Σ C1i ⊗ P6`, `Σ C2i ⊗ P6`,
`Σ (B0 ⊗ B0 + B0 ⊗ B0)` -/
theorem sC1_0 : NC (pat 0) C1i P6 = 0 := by decide +kernel
theorem sC2_0 : NC (pat 0) C2i P6 = 7200 := by decide +kernel
theorem sB_0 : NB (pat 0) B0 B0 = 240 := by decide +kernel
theorem sC1_1 : NC (pat 1) C1i P6 = 0 := by decide +kernel
theorem sC2_1 : NC (pat 1) C2i P6 = 2400 := by decide +kernel
theorem sB_1 : NB (pat 1) B0 B0 = 150 := by decide +kernel
theorem sC1_2 : NC (pat 2) C1i P6 = 0 := by decide +kernel
theorem sC2_2 : NC (pat 2) C2i P6 = 1440 := by decide +kernel
theorem sB_2 : NB (pat 2) B0 B0 = -120 := by decide +kernel
theorem sC1_3 : NC (pat 3) C1i P6 = 2100 := by decide +kernel
theorem sC2_3 : NC (pat 3) C2i P6 = 900 := by decide +kernel
theorem sB_3 : NB (pat 3) B0 B0 = -180 := by decide +kernel
theorem sC1_4 : NC (pat 4) C1i P6 = 2100 := by decide +kernel
theorem sC2_4 : NC (pat 4) C2i P6 = 900 := by decide +kernel
theorem sB_4 : NB (pat 4) B0 B0 = 30 := by decide +kernel
theorem sC1_5 : NC (pat 5) C1i P6 = 1260 := by decide +kernel
theorem sC2_5 : NC (pat 5) C2i P6 = 540 := by decide +kernel
theorem sB_5 : NB (pat 5) B0 B0 = 60 := by decide +kernel
theorem sC1_6 : NC (pat 6) C1i P6 = 630 := by decide +kernel
theorem sC2_6 : NC (pat 6) C2i P6 = 990 := by decide +kernel
theorem sB_6 : NB (pat 6) B0 B0 = -30 := by decide +kernel
theorem sums_C1 : ∀ c : Fin 7, NC (pat c) C1i P6 = ![0, 0, 0, 2100, 2100, 1260, 630] c := by
  intro c; fin_cases c
  exacts [sC1_0, sC1_1, sC1_2, sC1_3, sC1_4, sC1_5, sC1_6]
theorem sums_C2 : ∀ c : Fin 7, NC (pat c) C2i P6 = ![7200, 2400, 1440, 900, 900, 540, 990] c := by
  intro c; fin_cases c
  exacts [sC2_0, sC2_1, sC2_2, sC2_3, sC2_4, sC2_5, sC2_6]
theorem sums_B : ∀ c : Fin 7, NB (pat c) B0 B0 = ![240, 150, -120, -180, 30, 60, -30] c := by
  intro c; fin_cases c
  exacts [sB_0, sB_1, sB_2, sB_3, sB_4, sB_5, sB_6]

theorem levelValue_eq (c : Fin 7) (cC cB lam deg : ℝ) :
    levelValue (pat c) cC cB lam deg
      = cC * deg * (((![0, 0, 0, 2100, 2100, 1260, 630] c : ℤ) : ℝ) / 240)
        + lam * deg ^ 2 * (((![7200, 2400, 1440, 900, 900, 540, 990] c : ℤ) : ℝ) / 7200)
        + cB ^ 2 * ((![240, 150, -120, -180, 30, 60, -30] c : ℤ) : ℝ) := by
  have e1 : Cten cC lam deg = fun i j k l m q => cC / 8 * (C1i i j k l m q : ℝ) + lam * deg / 240 * (C2i i j k l m q : ℝ) := rfl
  have e2 : Aten deg = fun i j k l => deg / 30 * (P6 i j k l : ℝ) := rfl
  have e3 : Bten cB = fun i j k l m => cB * (B0 i j k l m : ℝ) := rfl
  rw [levelValue, e1, e2, e3, NC_lin, NB_lin, sums_C1, sums_C2, sums_B]; ring

/-- ⛭ **(C1) THE SEVEN LEVEL VALUES** as polynomial identities in `(c_C, c_B, λ, deg)`. Each lies in the three
structures `c_C·deg`, `λ·deg²` and `c_B²`. -/
theorem seven_level_values (cC cB lam deg : ℝ) :
    levelValue (pat 0) cC cB lam deg = lam * deg ^ 2 + 240 * cB ^ 2 ∧
    levelValue (pat 1) cC cB lam deg = 1/3 * lam * deg ^ 2 + 150 * cB ^ 2 ∧
    levelValue (pat 2) cC cB lam deg = 1/5 * lam * deg ^ 2 - 120 * cB ^ 2 ∧
    levelValue (pat 3) cC cB lam deg = 35/4 * cC * deg + 1/8 * lam * deg ^ 2 - 180 * cB ^ 2 ∧
    levelValue (pat 4) cC cB lam deg = 35/4 * cC * deg + 1/8 * lam * deg ^ 2 + 30 * cB ^ 2 ∧
    levelValue (pat 5) cC cB lam deg = 21/4 * cC * deg + 3/40 * lam * deg ^ 2 + 60 * cB ^ 2 ∧
    levelValue (pat 6) cC cB lam deg = 21/8 * cC * deg + 11/80 * lam * deg ^ 2 - 30 * cB ^ 2 := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;> rw [levelValue_eq] <;> norm_num <;> ring

/-- the level object: the seven values weighted by the seven imported coefficients -/
def levelObject (cC cB lam deg : ℝ) : ℝ := ∑ c : Fin 7, ACO c * levelValue (pat c) cC cB lam deg

/-- ⛭ **(C2) THE COMBINATION:** `(49/48) c_C deg − (13/480) λ deg² − 45 c_B²`. All three weights are nonzero. In
particular the `c_B²` weight is `−45`, so the imported parity is load-bearing. -/
theorem level_object_eq (cC cB lam deg : ℝ) :
    levelObject cC cB lam deg = 49/48 * cC * deg - 13/480 * lam * deg ^ 2 - 45 * cB ^ 2 := by
  obtain ⟨h0, h1, h2, h3, h4, h5, h6⟩ := seven_level_values cC cB lam deg
  rw [levelObject, Fin.sum_univ_seven, h0, h1, h2, h3, h4, h5, h6]
  norm_num [ACO] <;> ring

theorem weights_nonzero :
    levelObject 0 1 0 0 = -45 ∧ levelObject 1 0 0 1 = 49/48 ∧ levelObject 0 0 1 1 = -13/480 ∧
      (-45 : ℝ) ≠ 0 ∧ (49/48 : ℝ) ≠ 0 ∧ (-13/480 : ℝ) ≠ 0 := by
  refine ⟨?_, ?_, ?_, by norm_num, by norm_num, by norm_num⟩ <;> rw [level_object_eq] <;> norm_num

/-- the second-order level sum: the identity's coefficients `(−¼, 0, −½)` (Part B) against the contractions
`tr C`, the mixed `Σ C_{abc,bac}`, and `tr A` -/
def secondOrderLevel (cC lam deg : ℝ) : ℝ :=
  -(1/4) * S3 (fun a => S3 (fun i => S3 (fun j => Cten cC lam deg a i j a i j)))
    + 0 * S3 (fun a => S3 (fun i => S3 (fun j => Cten cC lam deg a i j i a j)))
    - (1/2) * S3 (fun i => S3 (fun j => Aten deg i j i j))

/-- ⛭ **(C3) BOTH LEVEL SUMS IN THE TOWER'S OWN VARIABLES.** With the imports (the spectrum, `c_C`, and the parity
`c_B = 0` as hypothesis `hB`): the second-order level sum is `−¼·deg·μ²` and the fourth-order one is
`−(1/120)·deg²·(5μ² + 4)`. -/
theorem level_sums_in_tower_variables (m cB : ℝ) (hB : cB = 0) :
    secondOrderLevel (cCval m) (lamSpec m) (degSpec m) = -(1/4) * degSpec m * mu2 m ∧
      levelObject (cCval m) cB (lamSpec m) (degSpec m) = -(1/120) * degSpec m ^ 2 * (5 * mu2 m + 4) := by
  constructor
  · simp only [secondOrderLevel]
    rw [(full_traces _ _ _).1, (full_traces 0 0 _).2.1]
    simp only [lamSpec, degSpec, mu2]; ring
  · rw [level_object_eq, hB]; simp only [cCval, lamSpec, degSpec, mu2]; ring

/-- ⛭ **(C4) BOTH VANISH AT `m = 2` AND ARE NEGATIVE FOR EVERY `m ≥ 3`** (every real `m ≥ 3`, so every level of
the tower). This is proved by positivity, not sampled. -/
theorem level_sums_sign (cB : ℝ) (hB : cB = 0) :
    (secondOrderLevel (cCval 2) (lamSpec 2) (degSpec 2) = 0 ∧ levelObject (cCval 2) cB (lamSpec 2) (degSpec 2) = 0) ∧
    ∀ m : ℝ, 3 ≤ m → secondOrderLevel (cCval m) (lamSpec m) (degSpec m) < 0 ∧
      levelObject (cCval m) cB (lamSpec m) (degSpec m) < 0 := by
  refine ⟨?_, fun m hm => ?_⟩
  · obtain ⟨h1, h2⟩ := level_sums_in_tower_variables 2 cB hB
    rw [h1, h2]; simp only [degSpec, mu2]; norm_num
  · obtain ⟨h1, h2⟩ := level_sums_in_tower_variables m cB hB
    rw [h1, h2]
    have hd : 0 < degSpec m := by simp only [degSpec]; nlinarith
    have hμ : 0 < mu2 m := by simp only [mu2]; nlinarith
    constructor
    · have := mul_pos hd hμ; linarith
    · have := mul_pos (pow_pos hd 2) (by linarith : (0:ℝ) < 5 * mu2 m + 4); linarith

/-- the same, for every natural level `m ≥ 3` -/
theorem level_sums_sign_nat (cB : ℝ) (hB : cB = 0) (m : ℕ) (hm : 3 ≤ m) :
    secondOrderLevel (cCval m) (lamSpec m) (degSpec m) < 0 ∧
      levelObject (cCval m) cB (lamSpec m) (degSpec m) < 0 :=
  (level_sums_sign cB hB).2 m (by exact_mod_cast hm)

/-- ⛭ **(C) THE LEVEL SUMS.** These are the seven values, their combination with nonzero weights, both sums in the
tower's variables, and their signs. -/
theorem part_C :
    (∀ cC cB lam deg, levelObject cC cB lam deg = 49/48 * cC * deg - 13/480 * lam * deg ^ 2 - 45 * cB ^ 2) ∧
    (∀ m cB, cB = 0 → secondOrderLevel (cCval m) (lamSpec m) (degSpec m) = -(1/4) * degSpec m * mu2 m ∧
      levelObject (cCval m) cB (lamSpec m) (degSpec m) = -(1/120) * degSpec m ^ 2 * (5 * mu2 m + 4)) ∧
    (∀ cB, cB = 0 → ∀ m : ℝ, 3 ≤ m → secondOrderLevel (cCval m) (lamSpec m) (degSpec m) < 0 ∧
      levelObject (cCval m) cB (lamSpec m) (degSpec m) < 0) :=
  ⟨level_object_eq, level_sums_in_tower_variables, fun cB hB => (level_sums_sign cB hB).2⟩

#print axioms seven_level_values
#print axioms weights_nonzero
#print axioms level_sums_sign
#print axioms part_C

/-! ## (D) the cross-level double sum, and the Faulhaber sums -/

/-- ⛭ **(D1) THE DOUBLE SUM FACTORISES.** The `(m, m′)` term of the weighted double sum is
`(49/48 c_C − 13/480 λ deg)(m) · deg(m′) − 45 c_B(m) c_B(m′)`. Every term is a level-`m` quantity times a level-`m′`
quantity. On the diagonal it is C's level object. -/
theorem cross_factorises (cC cB lam deg cB' deg' : ℝ) :
    ∑ c : Fin 7, ACO c * crossValue (pat c) cC cB lam deg cB' deg'
      = (49/48 * cC - 13/480 * lam * deg) * deg' - 45 * cB * cB' ∧
    ∑ c : Fin 7, ACO c * crossValue (pat c) cC cB lam deg cB deg = levelObject cC cB lam deg := by
  have key : ∀ c : Fin 7, crossValue (pat c) cC cB lam deg cB' deg'
      = cC * deg' * (((![0, 0, 0, 2100, 2100, 1260, 630] c : ℤ) : ℝ) / 240)
        + lam * deg * deg' * (((![7200, 2400, 1440, 900, 900, 540, 990] c : ℤ) : ℝ) / 7200)
        + cB * cB' * ((![240, 150, -120, -180, 30, 60, -30] c : ℤ) : ℝ) := by
    intro c
    have e1 : Cten cC lam deg = fun i j k l m q => cC / 8 * (C1i i j k l m q : ℝ) + lam * deg / 240 * (C2i i j k l m q : ℝ) := rfl
    have e2 : Aten deg' = fun i j k l => deg' / 30 * (P6 i j k l : ℝ) := rfl
    have e3 : ∀ x, Bten x = fun i j k l m => x * (B0 i j k l m : ℝ) := fun x => rfl
    rw [crossValue, e1, e2, e3, e3, NC_lin, NB_lin, sums_C1, sums_C2, sums_B]; ring
  refine ⟨?_, rfl⟩
  rw [Fin.sum_univ_seven]; simp only [key]
  norm_num [ACO] <;> ring

#print axioms cross_factorises

/-- the second-order level sum at level `k`, in the tower's variables -/
def q2m (k : ℝ) : ℝ := -(1/4) * degSpec k * mu2 k
/-- the fourth-order level sum at level `k`, in the tower's variables -/
def q4m (k : ℝ) : ℝ := -(1/120) * degSpec k ^ 2 * (5 * mu2 k + 4)

/-- ⛭ **(D2) THE FAULHABER SUMS.** The unweighted tower sums to a cutoff `M` are polynomials of degree 5 and 7, with
leading coefficients `−1/10` and `−1/42`, both negative. -/
theorem faulhaber (M : ℕ) (hM : 2 ≤ M) :
    ∑ k ∈ Finset.Icc 3 M, q2m k
      = -(1/10) * (M:ℝ) ^ 5 - 1/4 * (M:ℝ) ^ 4 + 2/3 * (M:ℝ) ^ 3 + 5/4 * (M:ℝ) ^ 2 - 47/30 * (M:ℝ) ∧
    ∑ k ∈ Finset.Icc 3 M, q4m k
      = -(1/42) * (M:ℝ) ^ 7 - 1/12 * (M:ℝ) ^ 6 + 19/100 * (M:ℝ) ^ 5 + 41/60 * (M:ℝ) ^ 4 - 89/180 * (M:ℝ) ^ 3
        - 22/15 * (M:ℝ) ^ 2 - 8/1575 * (M:ℝ) + 6/5 := by
  induction M, hM using Nat.le_induction with
  | base => constructor <;> simp [q2m, q4m, degSpec, mu2] <;> norm_num
  | succ n hn ih =>
    rw [Finset.sum_Icc_succ_top (show 3 ≤ n + 1 by omega), Finset.sum_Icc_succ_top (show 3 ≤ n + 1 by omega), ih.1, ih.2]
    constructor <;> simp only [q2m, q4m, degSpec, mu2] <;> push_cast <;> ring

theorem faulhaber_leading : (-(1/10) : ℝ) < 0 ∧ (-(1/42) : ℝ) < 0 := by norm_num

#print axioms faulhaber

end Levels

/-! ## (E) the sign algebra for `2c₄ − g²/μ²` -/

section Sign

/-- the receipt's honest form -/
def honest (c4 g2 μ2 : ℝ) : ℝ := 2 * c4 - g2 / μ2
/-- the banked (rearranged) form `μ² − g²/(2c₄)` -/
def banked (c4 g2 μ2 : ℝ) : ℝ := μ2 - g2 / (2 * c4)

/-- ⛭ **(E) THE SIGN NEEDS NO `g²`.**
- The banked form is the honest one rearranged across a division by `c₄`: they differ by the factor `2c₄/μ²`.
- So they agree in sign for `c₄ > 0` and can disagree for `c₄ < 0` (`c₄ = −1, g² = 1, μ² = 8`: `−17/8` against
  `17/2`; the receipt's text prints `−9/8` for the first).
- For `c₄ < 0` the honest form is negative for every `g² ≥ 0` and every `μ² > 0`, in particular at every tower level
  `m ≥ 3`, where `μ² = m² − 1 ≥ 8`. -/
theorem sign_algebra :
    (∀ c4 g2 μ2 : ℝ, c4 ≠ 0 → μ2 ≠ 0 → honest c4 g2 μ2 = banked c4 g2 μ2 * (2 * c4 / μ2)) ∧
    (∀ c4 g2 μ2 : ℝ, 0 < c4 → 0 < μ2 → (0 < honest c4 g2 μ2 ↔ 0 < banked c4 g2 μ2)) ∧
    (honest (-1) 1 8 = -17/8 ∧ banked (-1) 1 8 = 17/2) ∧
    (∀ c4 g μ2 : ℝ, c4 < 0 → 0 < μ2 → honest c4 (g ^ 2) μ2 < 0) ∧
    (∀ m : ℝ, 3 ≤ m → 8 ≤ mu2 m ∧ ∀ c4 g : ℝ, c4 < 0 → honest c4 (g ^ 2) (mu2 m) < 0) := by
  have neg : ∀ c4 g μ2 : ℝ, c4 < 0 → 0 < μ2 → honest c4 (g ^ 2) μ2 < 0 := by
    intro c4 g μ2 hc hμ
    have : 0 ≤ g ^ 2 / μ2 := div_nonneg (sq_nonneg g) hμ.le
    simp only [honest]; linarith
  refine ⟨?_, ?_, ?_, neg, ?_⟩
  · intro c4 g2 μ2 hc hμ; simp only [honest, banked]; field_simp
  · intro c4 g2 μ2 hc hμ
    have e : honest c4 g2 μ2 = banked c4 g2 μ2 * (2 * c4 / μ2) := by
      simp only [honest, banked]; field_simp
    have hf : 0 < 2 * c4 / μ2 := by positivity
    rw [e]; constructor
    · intro h; nlinarith
    · intro h; exact mul_pos h hf
  · simp only [honest, banked]; norm_num
  · intro m hm
    have h8 : 8 ≤ mu2 m := by simp only [mu2]; nlinarith
    exact ⟨h8, fun c4 g hc => neg c4 g (mu2 m) hc (by linarith)⟩

#print axioms sign_algebra

end Sign

end

end R60Levels

end ShadowProbe

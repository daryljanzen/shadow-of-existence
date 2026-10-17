import ShadowEngine
import Mathlib.NumberTheory.Harmonic.EulerMascheroni
import Mathlib.LinearAlgebra.Matrix.Rank

/-! # Campaign 37 (`r7443+71.18`): library-gap row 73, the vertex numbers are exact at the level this row owns

The receipt is
`P10_the_vertex_numbers_are_exact_at_the_level_this_row_owns_and_the_whole_scheme_is_one_series_pole_data.py`.
Its COMPUTED checks, sections A–E, are built here. Its paper-text check (the `pf.inline` parse of the
`K_ijK^ij − K²` formula from `canonical_time.tex`) is not formalised; the expression it parses is proved (`misner`).

- ***A.*** `misner` (`KK − K² = −6H² + 6(β̇₊² + β̇₋²)`, `Σβ̇ᵢ = 0`, isotropic limit `−6H²`, not vacuous);
  `unimodular` (`Πλᵢ = 1`); `R3_round` (`R₃ = 6` at `β = 0`); `R3_milnor` (the typed closed form equals the Koszul
  scalar curvature of `diag(e^{2bᵢ})`, via Milnor's formula, COPIED with its proof from `S3Frame.milnor_scalar`
  since probes cannot import probes); `taylor` (for every direction and `n ≤ 4`,
  `dⁿ/dtⁿ R₃(tβ₊, tβ₋)|₀ = n!·qₙ` with `q₀ … q₄ = 6, 0, −48(β₊² + β₋²), 160(β₊³ − 3β₊β₋²), −336(β₊² + β₋²)²`);
  `shapes` (cubic `= 160 Re(β₊ + iβ₋)³`, quartic a function of `β₊² + β₋²`); `calibration` (`48/6 = 8 = 3² − 1`,
  `2(3² − 4) = 10`, `√8 = 2√2`, `8 > 200/63`).
- ***B.*** `kinetic_linear` (`6ḣ²(1 − 4h + 12h²) + h³ḣ²r(h)`, explicit remainder), `kinetic_exponential` (every field
  derivative of `6β̇²` vanishes), `unit_jacobian` (`β(0) = 0`, `β′(0) = 1`).
- ***C.*** A two-mode ladder algebra on coefficient functions of `|n₊ n₋⟩` (adapted from `Row68Overlap`), the
  truncation a parameter `ok`: `quartic_vev` (`⟨V₄⟩ = 8c₄s²`), `cubic_three_quanta` (`V₃|0⟩` lives on exactly
  `|3 0⟩, |1 2⟩`), `one_quantum_cancels`, `cubic_shift` (`−8g²s³/ħω`), `fock_receipt` (the receipt's `NF = 7` and the
  untruncated ladder), `normalisation` (`c₄ = 14κ/3V`, `g² = 800κ/27V`), `total_shift`
  (`4κħ²(63μ² − 200)/(27Va³μ⁴)`), `at_level_three` (`19κħ²/(27Va³) > 0`), `threshold` (`200/63`), `density_a6`.
- ***D.*** `linear_solves` (one unknown fixed vs a one-parameter family), `rank_two` (Jacobian rank `2`, `Σbᵢ = 0`,
  `R₃` depends on both anisotropies).
- ***E.*** `dmu_residues` (`2, −9, 15/4`), `dovmu_residues` (`2, −7`), `faulhaber` (residue over location, and the
  `M²` mixing), `log_coeff` (the log coefficient is `15/4`), `residue_product` (`½`).

***Imported, not derived (labelled again at each declaration):***
- the identification of the frame-constant sector with the left-invariant metrics `diag(e^{2bᵢ})` and the typed
  closed form `R₃` (here tied to the Koszul curvature by `R3_milnor`);
- the TT spectrum beyond `m = 3`, `d(m) = 2(m² − 4)`, `μ(m) = √(m² − 1)` (`wDmu`, `wDovmu`);
- the formal Rayleigh–Schrödinger second-order formula (`rs2`), a formula and not an eigenvalue statement;
- the receipt's typed action normalisation `V/(2κ)`, `φ = √(6V/κ)β` (`pre`, `cv`) and scale-factor bookkeeping
  `s = ħ/(2a²μ)`, `ħω = ħμ/a`, the factors `a`, `a²` (`sv`, `hwv`, `total`). -/

namespace ShadowProbe

namespace R73Vertex

open Finset Real Filter Topology

/-! ### A. The exact reduction and the vertex numbers -/

section A

/-- the Misner velocities `β̇ᵢ = (β̇₊ + √3β̇₋, β̇₊ − √3β̇₋, −2β̇₊)` -/
noncomputable def dv (bdp bdm : ℝ) : Fin 3 → ℝ := ![bdp + √3 * bdm, bdp - √3 * bdm, -2 * bdp]

/-- `K_ij K^ij − K²` from `K^i_j = diag(H + β̇ᵢ)` -/
noncomputable def KK (H bdp bdm : ℝ) : ℝ := ∑ i, (H + dv bdp bdm i) ^ 2 - (3 * H + ∑ i, dv bdp bdm i) ^ 2

theorem sqrt3_sq : √3 ^ 2 = 3 := Real.sq_sqrt (by norm_num)

/-- ⛭ **`misner`.** the velocities sum to zero and `K_ijK^ij − K² = −6H² + 6(β̇₊² + β̇₋²)` exactly (no cross
term); its isotropic limit is `−6H²`, and the limit is not vacuous -/
theorem misner (H bdp bdm : ℝ) :
    ∑ i, dv bdp bdm i = 0 ∧ KK H bdp bdm = -6 * H ^ 2 + 6 * (bdp ^ 2 + bdm ^ 2) ∧
    KK H 0 0 = -6 * H ^ 2 ∧ KK H 1 0 ≠ KK H 0 0 := by
  have hs := sqrt3_sq
  have key : ∀ x y, KK H x y = -6 * H ^ 2 + 6 * (x ^ 2 + y ^ 2) := by
    intro x y
    simp only [KK, dv, Fin.sum_univ_three, Matrix.cons_val_zero, Matrix.cons_val_one,
      Matrix.cons_val_two, Matrix.head_cons, Matrix.tail_cons]
    linear_combination (2 * y ^ 2) * hs
  refine ⟨?_, key _ _, ?_, ?_⟩
  · simp [dv, Fin.sum_univ_three]; ring
  · rw [key]; ring
  · rw [key, key]; norm_num

/-- the anisotropy exponents `bᵢ = (β₊ + √3β₋, β₊ − √3β₋, −2β₊)` -/
noncomputable def bv (bp bm : ℝ) : Fin 3 → ℝ := ![bp + √3 * bm, bp - √3 * bm, -2 * bp]

/-- the eigenvalues `λᵢ = e^{2bᵢ}` of the frame-constant metric -/
noncomputable def lam (bp bm : ℝ) (i : Fin 3) : ℝ := Real.exp (2 * bv bp bm i)

/-- ⛭ **`unimodular`.** `λ₀λ₁λ₂ = 1` -/
theorem unimodular (bp bm : ℝ) : lam bp bm 0 * lam bp bm 1 * lam bp bm 2 = 1 := by
  simp only [lam, ← Real.exp_add]
  rw [show 2 * bv bp bm 0 + 2 * bv bp bm 1 + 2 * bv bp bm 2 = 0 by simp [bv]; ring, Real.exp_zero]

/-- the receipt's typed closed form `R₃ = 2(2Σλᵢλⱼ − Σλᵢ²)` (Milnor's formula at `λ₀λ₁λ₂ = 1`; derived below) -/
noncomputable def R3 (bp bm : ℝ) : ℝ :=
  2 * (2 * (lam bp bm 0 * lam bp bm 1 + lam bp bm 1 * lam bp bm 2 + lam bp bm 2 * lam bp bm 0)
    - (lam bp bm 0 ^ 2 + lam bp bm 1 ^ 2 + lam bp bm 2 ^ 2))

/-- ⛭ **`R3_round`.** `R₃ = 6` on the round metric -/
theorem R3_round : R3 0 0 = 6 := by
  simp [R3, lam, bv]; norm_num

/-! #### The link to Milnor's formula, by copying `S3Frame`'s Koszul machinery (probes cannot import probes) -/

/-- (copied from `S3Frame.lean`) the Levi-Civita symbol on `Fin 3` -/
def eps3 (a b c : Fin 3) : ℝ :=
  if (a, b, c) = (0, 1, 2) ∨ (a, b, c) = (1, 2, 0) ∨ (a, b, c) = (2, 0, 1) then 1
  else if (a, b, c) = (0, 2, 1) ∨ (a, b, c) = (2, 1, 0) ∨ (a, b, c) = (1, 0, 2) then -1 else 0

/-- (copied) su(2) in the left-invariant frame of the unit `S³`: `[E_a, E_b] = 2 ε_abc E_c` -/
def strC (a b c : Fin 3) : ℝ := 2 * eps3 a b c

/-- (copied) the Koszul formula for the left-invariant metric `diag λ`: `Γ_abc = g(∇_{E_a}E_b, E_c)` -/
noncomputable def kosL (l : Fin 3 → ℝ) (a b c : Fin 3) : ℝ :=
  (strC a b c * l c - strC b c a * l a + strC c a b * l b) / 2

/-- (copied) `∇_{E_a}E_b = Σ_d kosU a b d E_d` -/
noncomputable def kosU (l : Fin 3 → ℝ) (a b d : Fin 3) : ℝ := kosL l a b d / l d

/-- (copied) `g(R(E_a, E_b)E_c, E_d)` -/
noncomputable def riemF (l : Fin 3 → ℝ) (a b c d : Fin 3) : ℝ :=
  ∑ e, (kosU l b c e * kosL l a e d - kosU l a c e * kosL l b e d) - ∑ f, strC a b f * kosL l f c d

/-- (copied) the scalar curvature `Σ_{ab} R_abba / (λ_a λ_b)` -/
noncomputable def scalF (l : Fin 3 → ℝ) : ℝ := ∑ a, ∑ b, riemF l a b b a / (l a * l b)

/-- (copied, with its proof, from `S3Frame.milnor_scalar`) `R(diag λ) = 2(4e₂ − e₁²)/e₃` -/
theorem milnor_scalar (l : Fin 3 → ℝ) (h0 : l 0 ≠ 0) (h1 : l 1 ≠ 0) (h2 : l 2 ≠ 0) :
    scalF l = 2 * (4 * (l 0 * l 1 + l 0 * l 2 + l 1 * l 2) - (l 0 + l 1 + l 2) ^ 2) / (l 0 * l 1 * l 2) := by
  simp only [scalF, riemF, kosU, kosL, strC, eps3, Fin.sum_univ_three]
  simp
  field_simp
  ring

/-- ⛭ **`R3_milnor`.** the typed closed form IS the Koszul scalar curvature of the left-invariant metric
`diag(e^{2bᵢ})` on `S³`: Milnor's formula with `e₃ = 1` -/
theorem R3_milnor (bp bm : ℝ) : scalF (lam bp bm) = R3 bp bm := by
  have hu := unimodular bp bm
  have hpos : ∀ i, lam bp bm i ≠ 0 := fun i => (Real.exp_pos _).ne'
  rw [milnor_scalar _ (hpos 0) (hpos 1) (hpos 2), hu, div_one, R3]
  ring

/-! #### The Taylor coefficients, as iterated derivatives along every ray -/

/-- a sum of six exponentials `Σ cₖ e^{aₖ t}` -/
noncomputable def expsum (c a : Fin 6 → ℝ) (t : ℝ) : ℝ := ∑ k, c k * Real.exp (a k * t)

theorem expsum_deriv (c a : Fin 6 → ℝ) : deriv (expsum c a) = expsum (fun k => c k * a k) a := by
  funext t
  apply HasDerivAt.deriv
  have h : ∀ k ∈ (Finset.univ : Finset (Fin 6)),
      HasDerivAt (fun t => c k * Real.exp (a k * t)) (c k * a k * Real.exp (a k * t)) t := by
    intro k _
    have := (((hasDerivAt_id t).const_mul (a k)).exp).const_mul (c k)
    convert this using 1
    · simp only [id]
    · simp only [id]; ring
  have := HasDerivAt.sum h
  have e1 : (∑ i, fun t => c i * Real.exp (a i * t)) = expsum c a := by
    funext x; simp [expsum, Finset.sum_apply]
  rw [e1] at this
  convert this using 1
  simp only [expsum]

theorem expsum_iter (n : ℕ) : ∀ c a : Fin 6 → ℝ,
    iteratedDeriv n (expsum c a) = expsum (fun k => c k * a k ^ n) a := by
  induction n with
  | zero => intro c a; simp
  | succ n ih =>
    intro c a
    rw [iteratedDeriv_succ', expsum_deriv, ih]
    congr 1; funext k; ring

/-- the six coefficients and exponents of `R₃` along the ray `t ↦ (tβ₊, tβ₋)` -/
def cR : Fin 6 → ℝ := ![4, 4, 4, -2, -2, -2]
noncomputable def aR (bp bm : ℝ) : Fin 6 → ℝ :=
  ![4 * bp, -2 * bp - 2 * √3 * bm, -2 * bp + 2 * √3 * bm, 4 * bp + 4 * √3 * bm, 4 * bp - 4 * √3 * bm, -8 * bp]

theorem expsum_six (c a : Fin 6 → ℝ) (t : ℝ) : expsum c a t = c 0 * Real.exp (a 0 * t) +
    c 1 * Real.exp (a 1 * t) + c 2 * Real.exp (a 2 * t) + c 3 * Real.exp (a 3 * t) +
    c 4 * Real.exp (a 4 * t) + c 5 * Real.exp (a 5 * t) := by
  simp only [expsum, Fin.sum_univ_six]

theorem cR_vals : cR 0 = 4 ∧ cR 1 = 4 ∧ cR 2 = 4 ∧ cR 3 = -2 ∧ cR 4 = -2 ∧ cR 5 = -2 :=
  ⟨rfl, rfl, rfl, rfl, rfl, rfl⟩

theorem aR_vals (bp bm : ℝ) : aR bp bm 0 = 4 * bp ∧ aR bp bm 1 = -2 * bp - 2 * √3 * bm ∧
    aR bp bm 2 = -2 * bp + 2 * √3 * bm ∧ aR bp bm 3 = 4 * bp + 4 * √3 * bm ∧
    aR bp bm 4 = 4 * bp - 4 * √3 * bm ∧ aR bp bm 5 = -8 * bp :=
  ⟨rfl, rfl, rfl, rfl, rfl, rfl⟩

theorem R3_ray (bp bm : ℝ) : (fun t => R3 (t * bp) (t * bm)) = expsum cR (aR bp bm) := by
  funext t
  obtain ⟨c0, c1, c2, c3, c4, c5⟩ := cR_vals
  obtain ⟨a0, a1, a2, a3, a4, a5⟩ := aR_vals bp bm
  rw [expsum_six, c0, c1, c2, c3, c4, c5, a0, a1, a2, a3, a4, a5]
  simp only [R3, lam, bv, Matrix.cons_val_zero, Matrix.cons_val_one,
    Matrix.cons_val_two, Matrix.head_cons, Matrix.tail_cons, sq, ← Real.exp_add]
  have h1 : Real.exp (2 * (t * bp + √3 * (t * bm)) + 2 * (t * bp - √3 * (t * bm))) = Real.exp (4 * bp * t) := by
    congr 1; ring
  have h2 : Real.exp (2 * (t * bp - √3 * (t * bm)) + 2 * (-2 * (t * bp))) =
      Real.exp ((-2 * bp - 2 * √3 * bm) * t) := by congr 1; ring
  have h3 : Real.exp (2 * (-2 * (t * bp)) + 2 * (t * bp + √3 * (t * bm))) =
      Real.exp ((-2 * bp + 2 * √3 * bm) * t) := by congr 1; ring
  have h4 : Real.exp (2 * (t * bp + √3 * (t * bm)) + 2 * (t * bp + √3 * (t * bm))) =
      Real.exp ((4 * bp + 4 * √3 * bm) * t) := by congr 1; ring
  have h5 : Real.exp (2 * (t * bp - √3 * (t * bm)) + 2 * (t * bp - √3 * (t * bm))) =
      Real.exp ((4 * bp - 4 * √3 * bm) * t) := by congr 1; ring
  have h6 : Real.exp (2 * (-2 * (t * bp)) + 2 * (-2 * (t * bp))) = Real.exp (-8 * bp * t) := by
    congr 1; ring
  rw [h1, h2, h3, h4, h5, h6]
  ring

/-- the receipt's homogeneous Taylor polynomials `q₀ … q₄` -/
noncomputable def qT (bp bm : ℝ) : Fin 5 → ℝ :=
  ![6, 0, -48 * (bp ^ 2 + bm ^ 2), 160 * (bp ^ 3 - 3 * bp * bm ^ 2), -336 * (bp ^ 2 + bm ^ 2) ^ 2]

/-- ⛭ **`taylor`.** for every direction `(β₊, β₋)` and `n ≤ 4`, the `n`-th derivative at `0` of
`t ↦ R₃(tβ₊, tβ₋)` is `n! · qₙ(β₊, β₋)`: the order-`n` Taylor term of `R₃` at the round metric is `qₙ`, i.e.
`R₃ = 6 − 48(β₊² + β₋²) + 160(β₊³ − 3β₊β₋²) − 336(β₊² + β₋²)² + O(|β|⁵)` -/
theorem taylor (bp bm : ℝ) (n : Fin 5) :
    iteratedDeriv n (fun t => R3 (t * bp) (t * bm)) 0 = (n : ℕ).factorial * qT bp bm n := by
  have hs := sqrt3_sq
  obtain ⟨c0, c1, c2, c3, c4, c5⟩ := cR_vals
  obtain ⟨a0, a1, a2, a3, a4, a5⟩ := aR_vals bp bm
  rw [R3_ray, expsum_iter, expsum_six]
  simp only [c0, c1, c2, c3, c4, c5, a0, a1, a2, a3, a4, a5, mul_zero, Real.exp_zero, mul_one]
  fin_cases n <;> simp [qT, Nat.factorial]
  · norm_num
  · ring
  · linear_combination (-32 * bm ^ 2) * hs
  · linear_combination (-960 * bm ^ 2 * bp) * hs
  · linear_combination (-896 * bm ^ 2 * (bm ^ 2 * √3 ^ 2 + 3 * bm ^ 2 + 6 * bp ^ 2)) * hs

/-- ⛭ **`shapes`.** the cubic is `160 Re(β₊ + iβ₋)³` (hexagonal) and the quartic is a function of
`β₊² + β₋²` alone (isotropic) -/
theorem shapes (bp bm : ℝ) :
    qT bp bm 3 = 160 * (((bp : ℂ) + bm * Complex.I) ^ 3).re ∧
    ∃ f : ℝ → ℝ, ∀ x y, qT x y 4 = f (x ^ 2 + y ^ 2) := by
  refine ⟨?_, ⟨fun r => -336 * r ^ 2, fun x y => by simp [qT]⟩⟩
  simp [qT, pow_succ, Complex.mul_re, Complex.mul_im]
  ring

/-- ⛭ **`calibration`.** the ratio of the first two Taylor coefficients is `48/6 = 8 = m² − 1` at `m = 3`, `2(m² − 4) = 10`, `√8 = 2√2`, and `8 > 200/63` -/
theorem calibration : -(qT 1 0 2) / R3 0 0 = 8 ∧ (48 / 6 : ℝ) = 8 ∧ (3 : ℝ) ^ 2 - 1 = 8 ∧ 2 * ((3 : ℝ) ^ 2 - 4) = 10 ∧
    √(48 / 6 : ℝ) = 2 * √2 ∧ (200 / 63 : ℝ) < 48 / 6 := by
  refine ⟨by rw [R3_round]; norm_num [qT], by norm_num, by norm_num, by norm_num, ?_, by norm_num⟩
  rw [show (48 / 6 : ℝ) = 2 ^ 2 * 2 by norm_num, Real.sqrt_mul (by norm_num), Real.sqrt_sq (by norm_num)]

end A

/-! ### B. The kinetic sector in the two parameterisations -/

section B

/-- the linear variable: `λ = 1 + 2h`, `β = ½ log λ` -/
noncomputable def betaH (h : ℝ) : ℝ := Real.log (1 + 2 * h) / 2

theorem betaH_deriv {h : ℝ} (hh : 0 < 1 + 2 * h) : HasDerivAt betaH (1 / (1 + 2 * h)) h := by
  have := (((hasDerivAt_id h).const_mul 2).const_add 1).log hh.ne'
  convert this.div_const 2 using 1
  · funext x; simp [betaH]
  · simp only [id]; field_simp

/-- the kinetic term `6β̇²` (A's `K_ijK^ij − K²` anisotropy part) written in the linear variable,
`β̇ = β′(h) ḣ` -/
noncomputable def kinH (h hdot : ℝ) : ℝ := 6 * (deriv betaH h * hdot) ^ 2

/-- ⛭ **`kinetic_linear`.** in the linear variable the kinetic term is
`6ḣ² − 24hḣ² + 72h²ḣ² + h³ḣ² r(h)`, with the explicit remainder `r(h) = −(192 + 288h)/(1 + 2h)²` regular at
`h = 0`: a cubic AND a quartic vertex, both non-zero -/
theorem kinetic_linear {h : ℝ} (hh : 0 < 1 + 2 * h) (hdot : ℝ) :
    kinH h hdot = 6 * hdot ^ 2 - 24 * h * hdot ^ 2 + 72 * h ^ 2 * hdot ^ 2 +
      h ^ 3 * hdot ^ 2 * (-(192 + 288 * h) / (1 + 2 * h) ^ 2) ∧ (-24 : ℝ) ≠ 0 ∧ (72 : ℝ) ≠ 0 := by
  refine ⟨?_, by norm_num, by norm_num⟩
  rw [kinH, (betaH_deriv hh).deriv]
  field_simp
  ring

/-- the kinetic term in the exponential variable, as a function of the field: `6β̇²`, field-independent -/
noncomputable def kinE (bdot : ℝ) (_β : ℝ) : ℝ := 6 * bdot ^ 2

/-- ⛭ **`kinetic_exponential`.** in the exponential variable every field derivative of the kinetic term
vanishes, at every order and every field value: no `π²φ²` vertex at any order -/
theorem kinetic_exponential (bdot β₀ : ℝ) (n : ℕ) : iteratedDeriv (n + 1) (kinE bdot) β₀ = 0 := by
  have : kinE bdot = fun _ => 6 * bdot ^ 2 := rfl
  rw [this, iteratedDeriv_const]; simp

/-- ⛭ **`unit_jacobian`.** `β(0) = 0` and `β′(0) = 1`: the map is a point transformation agreeing at linear order -/
theorem unit_jacobian : betaH 0 = 0 ∧ deriv betaH 0 = 1 := by
  refine ⟨by simp [betaH], ?_⟩
  rw [(betaH_deriv (by norm_num)).deriv]; norm_num

end B

/-! ### C. The second-order shift, in a two-mode Fock space -/

section C

/-- a state of the two modes: its coefficient on each number vector `|n₊ n₋⟩` -/
abbrev St := ℕ × ℕ → ℝ

/-- the number vector `|p q⟩` -/
def ket (p q : ℕ) : St := fun n => if n = (p, q) then 1 else 0

/-- the vacuum `|0 0⟩` -/
def vac : St := ket 0 0

variable (ok : ℕ → Prop) [DecidablePred ok]

/-- `a₊`: `(a₊ψ)(n) = √(n₊+1) ψ(n + e₊)`, on kept levels (`ok k ↔ k < 7` is the receipt's `NF = 7`) -/
noncomputable def lowP : St →ₗ[ℝ] St where
  toFun ψ n := if ok n.1 ∧ ok n.2 ∧ ok (n.1 + 1) then √((n.1 : ℝ) + 1) * ψ (n.1 + 1, n.2) else 0
  map_add' ψ φ := by funext n; simp only [Pi.add_apply]; split_ifs <;> ring
  map_smul' c ψ := by funext n; simp only [Pi.smul_apply, smul_eq_mul, RingHom.id_apply]; split_ifs <;> ring

/-- `a₊†`: `(a₊†ψ)(n) = √n₊ ψ(n − e₊)` for `n₊ ≥ 1`, on kept levels -/
noncomputable def raiP : St →ₗ[ℝ] St where
  toFun ψ n := if ok n.1 ∧ ok n.2 ∧ 0 < n.1 then √(n.1 : ℝ) * ψ (n.1 - 1, n.2) else 0
  map_add' ψ φ := by funext n; simp only [Pi.add_apply]; split_ifs <;> ring
  map_smul' c ψ := by funext n; simp only [Pi.smul_apply, smul_eq_mul, RingHom.id_apply]; split_ifs <;> ring

/-- `a₋` -/
noncomputable def lowM : St →ₗ[ℝ] St where
  toFun ψ n := if ok n.1 ∧ ok n.2 ∧ ok (n.2 + 1) then √((n.2 : ℝ) + 1) * ψ (n.1, n.2 + 1) else 0
  map_add' ψ φ := by funext n; simp only [Pi.add_apply]; split_ifs <;> ring
  map_smul' c ψ := by funext n; simp only [Pi.smul_apply, smul_eq_mul, RingHom.id_apply]; split_ifs <;> ring

/-- `a₋†` -/
noncomputable def raiM : St →ₗ[ℝ] St where
  toFun ψ n := if ok n.1 ∧ ok n.2 ∧ 0 < n.2 then √(n.2 : ℝ) * ψ (n.1, n.2 - 1) else 0
  map_add' ψ φ := by funext n; simp only [Pi.add_apply]; split_ifs <;> ring
  map_smul' c ψ := by funext n; simp only [Pi.smul_apply, smul_eq_mul, RingHom.id_apply]; split_ifs <;> ring

theorem lowP_ket (p q : ℕ) : lowP ok (ket p q) =
    (if 0 < p ∧ ok (p - 1) ∧ ok q ∧ ok p then √(p : ℝ) else 0) • ket (p - 1) q := by
  funext ⟨a, b⟩
  simp only [lowP, LinearMap.coe_mk, AddHom.coe_mk, ket, Pi.smul_apply, smul_eq_mul, Prod.mk.injEq]
  by_cases hab : a + 1 = p ∧ b = q
  · obtain ⟨rfl, rfl⟩ := hab
    simp
  · rcases Nat.eq_zero_or_pos p with hp | hp
    · simp [hp]
    · have : ¬ (a = p - 1 ∧ b = q) := fun h => hab ⟨by omega, h.2⟩
      simp [hab, this]

theorem raiP_ket (p q : ℕ) : raiP ok (ket p q) = (if ok (p + 1) ∧ ok q then √((p : ℝ) + 1) else 0) •
    ket (p + 1) q := by
  funext ⟨a, b⟩
  simp only [raiP, LinearMap.coe_mk, AddHom.coe_mk, ket, Pi.smul_apply, smul_eq_mul, Prod.mk.injEq]
  by_cases hab : a = p + 1 ∧ b = q
  · obtain ⟨rfl, rfl⟩ := hab
    simp
  · have : ¬ (0 < a ∧ a - 1 = p ∧ b = q) := fun h => hab ⟨by omega, h.2.2⟩
    by_cases h0 : 0 < a
    · simp [hab, show ¬ (a - 1 = p ∧ b = q) from fun h => this ⟨h0, h⟩]
    · simp [hab, h0]

theorem lowM_ket (p q : ℕ) : lowM ok (ket p q) =
    (if 0 < q ∧ ok p ∧ ok (q - 1) ∧ ok q then √(q : ℝ) else 0) • ket p (q - 1) := by
  funext ⟨a, b⟩
  simp only [lowM, LinearMap.coe_mk, AddHom.coe_mk, ket, Pi.smul_apply, smul_eq_mul, Prod.mk.injEq]
  by_cases hab : a = p ∧ b + 1 = q
  · obtain ⟨rfl, rfl⟩ := hab
    simp
  · rcases Nat.eq_zero_or_pos q with hq | hq
    · simp [hq]
    · have : ¬ (a = p ∧ b = q - 1) := fun h => hab ⟨h.1, by omega⟩
      simp [hab, this]

theorem raiM_ket (p q : ℕ) : raiM ok (ket p q) = (if ok p ∧ ok (q + 1) then √((q : ℝ) + 1) else 0) •
    ket p (q + 1) := by
  funext ⟨a, b⟩
  simp only [raiM, LinearMap.coe_mk, AddHom.coe_mk, ket, Pi.smul_apply, smul_eq_mul, Prod.mk.injEq]
  by_cases hab : a = p ∧ b = q + 1
  · obtain ⟨rfl, rfl⟩ := hab
    simp
  · by_cases h0 : 0 < b
    · simp [hab, h0, show ¬ (a = p ∧ b - 1 = q) from fun h => hab ⟨h.1, by omega⟩]
    · simp [hab, h0]

/-- `x₊ = √s (a₊ + a₊†)`, so that `⟨x₊²⟩ = s` -/
noncomputable def XP (s : ℝ) : Module.End ℝ St := √s • (lowP ok + raiP ok)
/-- `x₋ = √s (a₋ + a₋†)` -/
noncomputable def XM (s : ℝ) : Module.End ℝ St := √s • (lowM ok + raiM ok)

/-- the quartic `V₄ = c₄(x₊² + x₋²)²` -/
noncomputable def V4 (c4 s : ℝ) : Module.End ℝ St :=
  c4 • ((XP ok s * XP ok s + XM ok s * XM ok s) * (XP ok s * XP ok s + XM ok s * XM ok s))

/-- the cubic `V₃ = −g(x₊³ − 3x₊x₋²)` -/
noncomputable def V3 (g s : ℝ) : Module.End ℝ St :=
  -g • (XP ok s * XP ok s * XP ok s - (3 : ℝ) • (XP ok s * XM ok s * XM ok s))

/-- ⛭ the cubic on the vacuum, as a combination of number vectors -/
theorem V3_vac_kets (h0 : ok 0) (h1 : ok 1) (h2 : ok 2) (h3 : ok 3) (g s : ℝ) :
    V3 ok g s vac = (-g * √s ^ 3 * √2 * √3) • ket 3 0 + (3 * g * √s ^ 3 * √2) • ket 1 2 := by
  simp only [V3, XP, XM, vac, Module.End.mul_apply, LinearMap.smul_apply, LinearMap.add_apply, LinearMap.sub_apply,
    map_add, map_smul, lowP_ket, raiP_ket, lowM_ket, raiM_ket]
  simp [h0, h1, h2, h3]
  funext n
  simp only [Pi.add_apply, Pi.sub_apply, Pi.neg_apply, Pi.smul_apply, smul_eq_mul, ket]
  norm_num
  split_ifs <;> simp_all
  all_goals first
    | ring1
    | (right; linear_combination (√s * (√s * √s)) * (Real.mul_self_sqrt (show (0:ℝ) ≤ 2 by norm_num)))

/-- ⛭ **`cubic_three_quanta`.** for `g ≠ 0`, `s > 0`: `V₃|0⟩` has non-zero amplitude on exactly the two
states `|3 0⟩`, `|1 2⟩`, both of three quanta (any truncation keeping levels `0 … 3`) -/
theorem cubic_three_quanta (h0 : ok 0) (h1 : ok 1) (h2 : ok 2) (h3 : ok 3) {g s : ℝ} (hg : g ≠ 0)
    (hs : 0 < s) (n : ℕ × ℕ) :
    (V3 ok g s vac n ≠ 0 ↔ n = (3, 0) ∨ n = (1, 2)) ∧ (V3 ok g s vac n ≠ 0 → n.1 + n.2 = 3) := by
  have hss : 0 < √s := Real.sqrt_pos.2 hs
  have h2' : 0 < √(2 : ℝ) := by positivity
  have h3' : 0 < √(3 : ℝ) := by positivity
  have key : V3 ok g s vac n ≠ 0 ↔ n = (3, 0) ∨ n = (1, 2) := by
    rw [V3_vac_kets ok h0 h1 h2 h3]
    simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul, ket]
    by_cases ha : n = (3, 0)
    · subst ha; simp [hg, hss.ne', h2'.ne', h3'.ne']
    · by_cases hb : n = (1, 2)
      · subst hb; simp [hg, hss.ne', h2'.ne']
      · simp [ha, hb]
  refine ⟨key, fun h => ?_⟩
  rcases key.1 h with rfl | rfl <;> rfl

/-- ⛭ **`one_quantum_cancels`.** the one-quantum amplitude of `V₃|0⟩` is `0`, its two channels `x₊³` and
`3x₊x₋²` each contributing `3s^{3/2}`, equal and opposite -/
theorem one_quantum_cancels (h0 : ok 0) (h1 : ok 1) (h2 : ok 2) (h3 : ok 3) (g s : ℝ) :
    V3 ok g s vac (1, 0) = 0 ∧ (XP ok s * XP ok s * XP ok s) vac (1, 0) = 3 * √s ^ 3 ∧
    ((3 : ℝ) • (XP ok s * XM ok s * XM ok s)) vac (1, 0) = 3 * √s ^ 3 := by
  refine ⟨?_, ?_, ?_⟩
  · rw [V3_vac_kets ok h0 h1 h2 h3]; simp [ket]
  · simp only [XP, vac, Module.End.mul_apply, LinearMap.smul_apply, LinearMap.add_apply,
      map_add, map_smul, lowP_ket, raiP_ket]
    simp [h0, h1, h2, h3, ket]
    norm_num
    linear_combination (√s ^ 3) * (Real.sq_sqrt (show (0:ℝ) ≤ 2 by norm_num))
  · simp only [XP, XM, vac, Module.End.mul_apply, LinearMap.smul_apply, LinearMap.add_apply,
      map_add, map_smul, lowP_ket, raiP_ket, lowM_ket, raiM_ket]
    simp [h0, h1, h2, ket]
    ring

/-- ⛭ **`quartic_vev`.** `⟨0|V₄|0⟩ = 8c₄s²` (any truncation keeping levels `0, 1, 2`) -/
theorem quartic_vev (h0 : ok 0) (h1 : ok 1) (h2 : ok 2) (c4 : ℝ) {s : ℝ} (hs : 0 ≤ s) :
    V4 ok c4 s vac (0, 0) = 8 * c4 * s ^ 2 := by
  have q : √s * √s = s := Real.mul_self_sqrt hs
  simp only [V4, XP, XM, vac, Module.End.mul_apply, LinearMap.smul_apply, LinearMap.add_apply,
    map_add, map_smul, lowP_ket, raiP_ket, lowM_ket, raiM_ket]
  simp [h0, h1, h2, ket, ite_apply]
  norm_num
  linear_combination (8 * c4 * (√s * √s + s)) * q +
    (2 * c4 * (√s * √s) ^ 2) * (Real.mul_self_sqrt (show (0:ℝ) ≤ 2 by norm_num))

/-- the excited states of the `N`-level box (`N = 7`: the receipt's `49 − 1`) -/
def box (N : ℕ) : Finset (ℕ × ℕ) := (Finset.range N ×ˢ Finset.range N).erase (0, 0)

/-- **IMPORTED (the formal Rayleigh–Schrödinger formula, labelled):** the second-order shift
`−Σ_{n≠0} |⟨n|V|0⟩|²/(E_n − E_0)`, with the free two-mode spectrum `E_n − E_0 = (n₊ + n₋)ħω`. It is a formula, not an
eigenvalue statement: the cubic oscillator is unbounded below. -/
noncomputable def rs2 (N : ℕ) (V : Module.End ℝ St) (hw : ℝ) : ℝ :=
  -∑ n ∈ box N, (V vac n) ^ 2 / (((n.1 + n.2 : ℕ) : ℝ) * hw)

/-- ⛭ **`cubic_shift`.** the cubic's second-order shift is `−8g²s³/ħω`, for every box of `N ≥ 4` levels kept by
`ok` (the receipt's `N = 7`) -/
theorem cubic_shift (h0 : ok 0) (h1 : ok 1) (h2 : ok 2) (h3 : ok 3) {N : ℕ} (hN : 4 ≤ N) (g : ℝ) {s : ℝ}
    (hs : 0 ≤ s) (hw : ℝ) (hhw : hw ≠ 0) :
    rs2 N (V3 ok g s) hw = -8 * g ^ 2 * s ^ 3 / hw := by
  have hsub : ({(3, 0), (1, 2)} : Finset (ℕ × ℕ)) ⊆ box N := by
    intro n hn
    simp only [Finset.mem_insert, Finset.mem_singleton] at hn
    simp only [box, Finset.mem_erase, Finset.mem_product, Finset.mem_range]
    rcases hn with rfl | rfl <;> refine ⟨by decide, ?_, ?_⟩ <;> simp <;> omega
  rw [rs2, ← Finset.sum_subset hsub, Finset.sum_pair (by decide)]
  · rw [V3_vac_kets ok h0 h1 h2 h3]
    simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul, ket]
    norm_num
    have e2 := Real.sq_sqrt (show (0:ℝ) ≤ 2 by norm_num)
    have e3 := Real.sq_sqrt (show (0:ℝ) ≤ 3 by norm_num)
    have es : √s ^ 6 = s ^ 3 := by rw [show 6 = 2 * 3 by rfl, pow_mul, Real.sq_sqrt hs]
    field_simp
    rw [es, e2, e3]
    ring
  · intro n _ hn
    rw [V3_vac_kets ok h0 h1 h2 h3]
    simp only [Finset.mem_insert, Finset.mem_singleton, not_or] at hn
    simp [ket, hn.1, hn.2]

/-- the quartic's first-order shift `⟨0|V₄|0⟩` -/
noncomputable def e4 (ok : ℕ → Prop) [DecidablePred ok] (c4 s : ℝ) : ℝ := V4 ok c4 s vac (0, 0)

/-- the receipt's truncation `NF = 7` -/
def trunc7 (k : ℕ) : Prop := k < 7

instance : DecidablePred trunc7 := fun k => by unfold trunc7; infer_instance

/-- ⛭ **`fock_receipt`.** the receipt's computation itself (`NF = 7`, `49` states) and the untruncated ladder:
`⟨V₄⟩ = 8c₄s²`, `V₃|0⟩` supported on the two three-quantum states, and the shift `−8g²s³/ħω` -/
theorem fock_receipt (c4 g : ℝ) (hg : g ≠ 0) {s : ℝ} (hs : 0 < s) (hw : ℝ) (hhw : hw ≠ 0) :
    e4 trunc7 c4 s = 8 * c4 * s ^ 2 ∧ (∀ n, V3 trunc7 g s vac n ≠ 0 ↔ n = (3, 0) ∨ n = (1, 2)) ∧
    rs2 7 (V3 trunc7 g s) hw = -8 * g ^ 2 * s ^ 3 / hw ∧
    e4 (fun _ => True) c4 s = 8 * c4 * s ^ 2 ∧
    (∀ n, V3 (fun _ => True) g s vac n ≠ 0 ↔ n = (3, 0) ∨ n = (1, 2)) := by
  have t : ∀ k, k < 4 → trunc7 k := fun k hk => by unfold trunc7; omega
  refine ⟨quartic_vev _ (t 0 (by norm_num)) (t 1 (by norm_num)) (t 2 (by norm_num)) c4 hs.le,
    fun n => (cubic_three_quanta _ (t 0 (by norm_num)) (t 1 (by norm_num)) (t 2 (by norm_num))
      (t 3 (by norm_num)) hg hs n).1,
    cubic_shift _ (t 0 (by norm_num)) (t 1 (by norm_num)) (t 2 (by norm_num)) (t 3 (by norm_num))
      (by norm_num) g hs.le hw hhw,
    quartic_vev _ trivial trivial trivial c4 hs.le,
    fun n => (cubic_three_quanta _ trivial trivial trivial trivial hg hs n).1⟩

/-! #### The canonical normalisation and the total -/

/-- **IMPORTED (the receipt's action normalisation, typed):** the prefactor `V/(2κ)` and the canonical field
`φ = √(6V/κ) β`, i.e. `β = √(κ/(6V)) φ` -/
noncomputable def pre (κ V : ℝ) : ℝ := V / (2 * κ)
noncomputable def cv (κ V : ℝ) : ℝ := √(κ / (6 * V))

/-- `c₄ = 336 · (V/2κ) · (κ/6V)²`, from A's quartic `−336(β₊² + β₋²)²` -/
noncomputable def c4v (κ V : ℝ) : ℝ := 336 * pre κ V * cv κ V ^ 4
/-- `g = 160 · (V/2κ) · (κ/6V)^{3/2}`, from A's cubic `160(β₊³ − 3β₊β₋²)` -/
noncomputable def gv (κ V : ℝ) : ℝ := 160 * pre κ V * cv κ V ^ 3

/-- ⛭ **`normalisation`.** the kinetic term `(V/2κ)·6β̇²` becomes `½φ̇²`, and `c₄ = 14κ/(3V)`,
`g² = 800κ/(27V)` -/
theorem normalisation {κ V : ℝ} (hκ : 0 < κ) (hV : 0 < V) :
    pre κ V * 6 * cv κ V ^ 2 = 1 / 2 ∧ c4v κ V = 14 * κ / (3 * V) ∧ gv κ V ^ 2 = 800 * κ / (27 * V) := by
  have h : cv κ V ^ 2 = κ / (6 * V) := Real.sq_sqrt (by positivity)
  refine ⟨?_, ?_, ?_⟩
  · rw [h, pre]; field_simp
  · rw [c4v, show cv κ V ^ 4 = (cv κ V ^ 2) ^ 2 by ring, h, pre]; field_simp; ring
  · rw [gv, show (160 * pre κ V * cv κ V ^ 3) ^ 2 = 160 ^ 2 * pre κ V ^ 2 * (cv κ V ^ 2) ^ 3 by ring, h, pre]
    field_simp; ring

/-- **IMPORTED (the receipt's typed scale-factor bookkeeping):** the mode variance `s = ħ/(2a²μ)`, the quantum
`ħω = ħμ/a`, and the factors `a` (first order) and `a²` (second order) multiplying the vertex terms -/
noncomputable def sv (a ħ μ : ℝ) : ℝ := ħ / (2 * a ^ 2 * μ)
noncomputable def hwv (a ħ μ : ℝ) : ℝ := ħ * μ / a

/-- the total second-order vacuum shift, assembled from the Fock-space quantities on the receipt's box -/
noncomputable def total (κ V a ħ μ : ℝ) : ℝ :=
  a * e4 trunc7 (c4v κ V) (sv a ħ μ) + a ^ 2 * rs2 7 (V3 trunc7 (gv κ V) (sv a ħ μ)) (hwv a ħ μ)

/-- ⛭ **`total_shift`.** `ΔE⁽²⁾ = 4κħ²(63μ² − 200)/(27Va³μ⁴)` -/
theorem total_shift {κ V a ħ μ : ℝ} (hκ : 0 < κ) (hV : 0 < V) (ha : 0 < a) (hħ : 0 < ħ) (hμ : 0 < μ) :
    total κ V a ħ μ = 4 * κ * ħ ^ 2 * (63 * μ ^ 2 - 200) / (27 * V * a ^ 3 * μ ^ 4) := by
  have hs : 0 < sv a ħ μ := by unfold sv; positivity
  have hw : hwv a ħ μ ≠ 0 := by unfold hwv; positivity
  have t : ∀ k, k < 4 → trunc7 k := fun k hk => by unfold trunc7; omega
  obtain ⟨_, hc4, hg2⟩ := normalisation hκ hV
  rw [total, e4, quartic_vev _ (t 0 (by norm_num)) (t 1 (by norm_num)) (t 2 (by norm_num)) _ hs.le,
    cubic_shift _ (t 0 (by norm_num)) (t 1 (by norm_num)) (t 2 (by norm_num)) (t 3 (by norm_num))
      (by norm_num) _ hs.le _ hw, hc4, hg2, sv, hwv]
  field_simp
  ring

/-- ⛭ **`at_level_three`.** at `μ = 2√2` the shift is `19κħ²/(27Va³) > 0` -/
theorem at_level_three {κ V a ħ : ℝ} (hκ : 0 < κ) (hV : 0 < V) (ha : 0 < a) (hħ : 0 < ħ) :
    total κ V a ħ (2 * √2) = 19 * κ * ħ ^ 2 / (27 * V * a ^ 3) ∧ 0 < total κ V a ħ (2 * √2) := by
  have h2 : √2 ^ 2 = 2 := Real.sq_sqrt (by norm_num)
  have e : total κ V a ħ (2 * √2) = 19 * κ * ħ ^ 2 / (27 * V * a ^ 3) := by
    rw [total_shift hκ hV ha hħ (by positivity)]
    rw [show (2 * √2) ^ 2 = 8 by rw [mul_pow, h2]; norm_num,
      show (2 * √2) ^ 4 = 64 by rw [show 4 = 2 * 2 by rfl, pow_mul, mul_pow, h2]; norm_num]
    field_simp; ring
  exact ⟨e, by rw [e]; positivity⟩

/-- ⛭ **`threshold`.** the sign flips exactly at `μ² = 200/63`: the shift is positive iff `μ² > 200/63`, zero iff
`μ² = 200/63`; and `8 > 200/63` -/
theorem threshold {κ V a ħ μ : ℝ} (hκ : 0 < κ) (hV : 0 < V) (ha : 0 < a) (hħ : 0 < ħ) (hμ : 0 < μ) :
    (0 < total κ V a ħ μ ↔ 200 / 63 < μ ^ 2) ∧ (total κ V a ħ μ = 0 ↔ μ ^ 2 = 200 / 63) ∧
    (200 / 63 : ℝ) < 8 := by
  rw [total_shift hκ hV ha hħ hμ]
  have hd : 0 < 27 * V * a ^ 3 * μ ^ 4 := by positivity
  have hn : 0 < 4 * κ * ħ ^ 2 := by positivity
  refine ⟨?_, ?_, by norm_num⟩
  · rw [div_pos_iff_of_pos_right hd]
    constructor
    · intro h; nlinarith [pos_of_mul_pos_right h hn.le]
    · intro h; exact mul_pos hn (by linarith)
  · rw [div_eq_zero_iff, mul_eq_zero]
    constructor
    · rintro ((h | h) | h)
      · exact absurd h hn.ne'
      · linarith
      · exact absurd h hd.ne'
    · intro h; left; right; linarith

/-- the energy density at this level, `ΔE⁽²⁾/(Va³)` -/
noncomputable def dens (κ V ħ a : ℝ) : ℝ := 19 * κ * ħ ^ 2 / (27 * V * a ^ 3) / (V * a ^ 3)

/-- ⛭ **`density_a6`.** the density is `19κħ²/(27V²a⁶)` and `a · d log(dens)/da = −6`, i.e.
`dens′ = −6 dens / a` -/
theorem density_a6 {κ V ħ a : ℝ} (hV : 0 < V) (ha : 0 < a) :
    dens κ V ħ a = 19 * κ * ħ ^ 2 / (27 * V ^ 2 * a ^ 6) ∧
    HasDerivAt (dens κ V ħ) (-6 * dens κ V ħ a / a) a := by
  constructor
  · unfold dens; field_simp
  · have hf : dens κ V ħ = fun x => 19 * κ * ħ ^ 2 / (27 * V ^ 2) * (x ^ 6)⁻¹ := by
      funext x; unfold dens; field_simp
    rw [hf]
    have := ((hasDerivAt_pow 6 a).inv (by positivity)).const_mul (19 * κ * ħ ^ 2 / (27 * V ^ 2))
    convert this using 1
    field_simp; ring

end C

/-! ### D. The second-order rank from above: an order not reached -/

section D

/-- ⛭ **`linear_solves`.** first order closes: `c₁δa₁ = src₁` has exactly one solution; second order, whose source
needs the state's own correction, `c₁δa₂ + c₂δψ = src₂`, has the one-parameter FAMILY
`δa₂ = (src₂ − c₂δψ)/c₁` with `δψ` free, no unique solution, and `δa₂` genuinely depending on `δψ` -/
theorem linear_solves (c1 c2 src1 src2 : ℝ) (hc1 : c1 ≠ 0) (hc2 : c2 ≠ 0) :
    (∃! da1 : ℝ, c1 * da1 = src1) ∧
    (∀ da2 dpsi : ℝ, c1 * da2 + c2 * dpsi = src2 ↔ da2 = (src2 - c2 * dpsi) / c1) ∧
    ¬ (∃! p : ℝ × ℝ, c1 * p.1 + c2 * p.2 = src2) ∧
    (src2 - c2 * 0) / c1 ≠ (src2 - c2 * 1) / c1 := by
  refine ⟨⟨src1 / c1, by field_simp, fun y hy => by field_simp; linarith⟩, fun da2 dpsi => ?_, ?_, ?_⟩
  · rw [eq_div_iff hc1]; constructor <;> intro h <;> linarith
  · rintro ⟨p, hp, huniq⟩
    have h1 := huniq ((src2 - c2 * (p.2 + 1)) / c1, p.2 + 1) (by simp only; field_simp; ring)
    have := congrArg Prod.snd h1
    simp at this
  · intro h
    rw [div_left_inj' hc1] at h
    apply hc2; linarith

/-- the Jacobian `∂bᵢ/∂(β₊, β₋)` of the three eigenvalue logarithms -/
noncomputable def jac (bp bm : ℝ) : Matrix (Fin 3) (Fin 2) ℝ :=
  Matrix.of fun i j => if j = 0 then deriv (fun x => bv x bm i) bp else deriv (fun y => bv bp y i) bm

theorem jac_eq (bp bm : ℝ) : jac bp bm = !![1, √3; 1, -√3; -2, 0] := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [jac, bv]

/-- ⛭ **`rank_two`.** the Jacobian has rank `2` at every point, the logarithms satisfy the one relation
`Σbᵢ = 0`, and `R₃` genuinely depends on both anisotropies (neither partial derivative vanishes identically) -/
theorem rank_two (bp bm : ℝ) :
    (jac bp bm).rank = 2 ∧ ∑ i, bv bp bm i = 0 ∧
    ¬ (∀ x, deriv (fun t => R3 t 0) x = 0) ∧ ¬ (∀ y, deriv (fun t => R3 0 t) y = 0) := by
  refine ⟨?_, by simp [bv, Fin.sum_univ_three]; ring, ?_, ?_⟩
  · apply le_antisymm (by simpa using Matrix.rank_le_width (jac bp bm))
    have hm : ((jac bp bm).submatrix ![0, 1] ![0, 1]).det ≠ 0 := by
      rw [jac_eq, Matrix.det_fin_two]
      simp
      have := Real.sqrt_pos.2 (show (0:ℝ) < 3 by norm_num)
      intro h; linarith
    have h := Matrix.rank_of_det_ne_zero hm
    rw [Fintype.card_fin] at h
    exact (le_of_eq h.symm).trans (Matrix.rank_submatrix_le _ _ _)
  · intro h
    have hd : deriv (fun t => R3 t 0) = fun _ => 0 := funext h
    have t2 := taylor 1 0 2
    rw [show ((2 : Fin 5) : ℕ) = 1 + 1 from rfl, iteratedDeriv_succ, iteratedDeriv_one] at t2
    simp only [mul_one, mul_zero] at t2
    rw [hd] at t2
    simp [qT] at t2
  · intro h
    have hd : deriv (fun t => R3 0 t) = fun _ => 0 := funext h
    have t2 := taylor 0 1 2
    rw [show ((2 : Fin 5) : ℕ) = 1 + 1 from rfl, iteratedDeriv_succ, iteratedDeriv_one] at t2
    simp only [mul_one, mul_zero] at t2
    rw [hd] at t2
    simp [qT] at t2

end D

/-! ### E. The pole data of the tower's spectral series -/

section E

/-- **IMPORTED (the TT spectrum beyond `m = 3`):** `d(m)μ(m) = 2(m² − 4)√(m² − 1)` -/
noncomputable def wDmu (m : ℝ) : ℝ := 2 * (m ^ 2 - 4) * √(m ^ 2 - 1)
/-- **IMPORTED:** `d(m)/μ(m) = 2(m² − 4)/√(m² − 1)` -/
noncomputable def wDovmu (m : ℝ) : ℝ := 2 * (m ^ 2 - 4) / √(m ^ 2 - 1)

/-- (copied from `Row64Descent.L_coeff`) `m(dμ − 2m³ + 9m) → 15/4` -/
theorem dmu_L : Tendsto (fun m : ℝ => m * (wDmu m - (2 * m ^ 3 - 9 * m))) atTop (𝓝 (15 / 4)) := by
  have key : ∀ m : ℝ, 1 ≤ m → m * (wDmu m - (2 * m ^ 3 - 9 * m)) =
      8 * (m / (m + Real.sqrt (m ^ 2 - 1))) - (m / (m + Real.sqrt (m ^ 2 - 1))) ^ 2 := by
    intro m hm
    have hs : Real.sqrt (m ^ 2 - 1) ^ 2 = m ^ 2 - 1 := Real.sq_sqrt (by nlinarith)
    have hs0 := Real.sqrt_nonneg (m ^ 2 - 1)
    have hp : 0 < m + Real.sqrt (m ^ 2 - 1) := by linarith
    rw [show 8 * (m / (m + Real.sqrt (m ^ 2 - 1))) - (m / (m + Real.sqrt (m ^ 2 - 1))) ^ 2
        = (8 * m * (m + Real.sqrt (m ^ 2 - 1)) - m ^ 2) / (m + Real.sqrt (m ^ 2 - 1)) ^ 2 by
          field_simp, eq_div_iff (by positivity)]
    simp only [wDmu]
    linear_combination (2 * m ^ 4 - 7 * m ^ 2 + Real.sqrt (m ^ 2 - 1) * (2 * m ^ 3 - 8 * m)) * hs
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

/-- ⛭ **`dmu_residues`.** `d(m)μ(m) = 2m³ − 9m + (15/4)/m + o(1/m)`: the three coefficients `2, −9, 15/4`
(the residues of `Σ dμ m^{−s}` at `s = 4, 2, 0`) -/
theorem dmu_residues :
    Tendsto (fun m : ℝ => wDmu m / m ^ 3) atTop (𝓝 2) ∧
    Tendsto (fun m : ℝ => (wDmu m - 2 * m ^ 3) / m) atTop (𝓝 (-9)) ∧
    Tendsto (fun m : ℝ => m * (wDmu m - (2 * m ^ 3 - 9 * m))) atTop (𝓝 (15 / 4)) := by
  have i0 : Tendsto (fun m : ℝ => m⁻¹) atTop (𝓝 0) := tendsto_inv_atTop_zero
  have i2 : Tendsto (fun m : ℝ => (m⁻¹) ^ 2) atTop (𝓝 0) := by
    convert i0.pow 2 using 2; norm_num
  have i4 : Tendsto (fun m : ℝ => (m⁻¹) ^ 4) atTop (𝓝 0) := by
    convert i0.pow 4 using 2; norm_num
  refine ⟨?_, ?_, dmu_L⟩
  · have h := ((i2.const_mul (-9)).const_add 2).add (dmu_L.mul i4)
    norm_num at h
    refine h.congr' ?_
    filter_upwards [eventually_gt_atTop 0] with m hm
    field_simp; ring
  · have h := (dmu_L.mul i2).const_add (-9)
    norm_num at h
    refine h.congr' ?_
    filter_upwards [eventually_gt_atTop 0] with m hm
    field_simp; ring

/-- the exact identity behind `d/μ`: for `m ≥ 2`, with `v = √(1 − m⁻²)`,
`m(d/μ − 2m) = 2(16m⁻² − 7)/(v(1 − 4m⁻² + v))` -/
theorem dovmu_key {m : ℝ} (hm : 2 ≤ m) :
    m * (wDovmu m - 2 * m) = 2 * (16 * (m⁻¹) ^ 2 - 7) /
      (√(1 - (m⁻¹) ^ 2) * (1 - 4 * (m⁻¹) ^ 2 + √(1 - (m⁻¹) ^ 2))) := by
  have hm0 : 0 < m := by linarith
  have hx : (m⁻¹) ^ 2 ≤ 1 / 4 := by
    rw [inv_pow, ← one_div, div_le_div_iff₀ (by positivity) (by norm_num)]; nlinarith
  set v := √(1 - (m⁻¹) ^ 2) with hvdef
  have hv2 : v ^ 2 = 1 - (m⁻¹) ^ 2 := Real.sq_sqrt (by linarith)
  have hv : 0 < v := Real.sqrt_pos.2 (by linarith)
  have hu : √(m ^ 2 - 1) = m * v := by
    rw [hvdef, show m ^ 2 - 1 = m ^ 2 * (1 - (m⁻¹) ^ 2) by field_simp, Real.sqrt_mul (sq_nonneg m),
      Real.sqrt_sq hm0.le]
  have hB : 0 < 1 - 4 * (m⁻¹) ^ 2 + v := by linarith
  rw [wDovmu, hu, eq_div_iff (by positivity)]
  have hv2' : m ^ 2 * v ^ 2 = m ^ 2 - 1 := by rw [hv2]; field_simp
  field_simp
  linear_combination (-m ^ 2) * hv2'

/-- ⛭ **`dovmu_residues`.** `d(m)/μ(m) = 2m − 7/m + o(1/m)`: the coefficients `2, −7` (the residues of
`Σ (d/μ) m^{−s}` at `s = 2, 0`) -/
theorem dovmu_residues :
    Tendsto (fun m : ℝ => wDovmu m / m) atTop (𝓝 2) ∧
    Tendsto (fun m : ℝ => m * (wDovmu m - 2 * m)) atTop (𝓝 (-7)) := by
  have i0 : Tendsto (fun m : ℝ => m⁻¹) atTop (𝓝 0) := tendsto_inv_atTop_zero
  have i2 : Tendsto (fun m : ℝ => (m⁻¹) ^ 2) atTop (𝓝 0) := by
    convert i0.pow 2 using 2; norm_num
  have hv : Tendsto (fun m : ℝ => √(1 - (m⁻¹) ^ 2)) atTop (𝓝 1) := by
    simpa using (i2.const_sub (1 : ℝ)).sqrt
  have hL : Tendsto (fun m : ℝ => m * (wDovmu m - 2 * m)) atTop (𝓝 (-7)) := by
    have h := ((i2.const_mul 16).sub_const 7).const_mul 2 |>.div
      (hv.mul ((((i2.const_mul 4).const_sub 1)).add hv)) (by norm_num)
    norm_num at h
    refine h.congr' ?_
    filter_upwards [eventually_ge_atTop 2] with m hm
    rw [dovmu_key hm]; simp only [Pi.div_apply, inv_pow]
  refine ⟨?_, hL⟩
  have h := (hL.mul i2).const_add 2
  norm_num at h
  refine h.congr' ?_
  filter_upwards [eventually_gt_atTop 0] with m hm
  field_simp; ring

/-- ⛭ **`faulhaber`.** each pole contributes its residue over its location to the matching power of the cutoff:
`Σ_{m=3}^{M} 2m³ = ½M⁴ + M³ + ½M² − 18` (leading `2/4`), `Σ −9m = −(9/2)M² − (9/2)M + 27` (leading `−9/2`),
`Σ 2m = M² + M − 6` (leading `2/2`); and the first already carries an `M²` (`½ ≠ 0`): Faulhaber's mixing -/
theorem faulhaber (M : ℕ) (hM : 2 ≤ M) :
    ∑ m ∈ Finset.Icc 3 M, (2 * (m : ℝ) ^ 3) = (2 / 4) * (M : ℝ) ^ 4 + M ^ 3 + 1 / 2 * M ^ 2 - 18 ∧
    ∑ m ∈ Finset.Icc 3 M, (-9 * (m : ℝ)) = (-9 / 2) * (M : ℝ) ^ 2 - 9 / 2 * M + 27 ∧
    ∑ m ∈ Finset.Icc 3 M, (2 * (m : ℝ)) = (2 / 2) * (M : ℝ) ^ 2 + M - 6 ∧ (1 / 2 : ℝ) ≠ 0 := by
  refine ⟨?_, ?_, ?_, by norm_num⟩
  all_goals
    induction M, hM using Nat.le_induction with
    | base => simp; norm_num
    | succ n hn ih =>
      rw [Finset.sum_Icc_succ_top (by omega), ih]
      push_cast; ring

/-- `Σ_{m=3}^{M} (15/4)/m = (15/4)(H_M − 3/2)` -/
theorem log_sum (M : ℕ) (hM : 2 ≤ M) :
    ∑ m ∈ Finset.Icc 3 M, (15 / 4 / (m : ℝ)) = 15 / 4 * ((harmonic M : ℝ) - 3 / 2) := by
  induction M, hM using Nat.le_induction with
  | base => simp [harmonic, Finset.sum_range_succ]; norm_num
  | succ n hn ih =>
    rw [Finset.sum_Icc_succ_top (by omega), ih, harmonic_succ]
    push_cast; ring

/-- ⛭ **`log_coeff`.** the logarithmic coefficient is the `s = 0` residue exactly:
`Σ_{m=3}^{M} (15/4)/m − (15/4) log M → (15/4)(γ − 3/2)` -/
theorem log_coeff :
    Tendsto (fun M : ℕ => ∑ m ∈ Finset.Icc 3 M, (15 / 4 / (m : ℝ)) - 15 / 4 * Real.log M) atTop
      (𝓝 (15 / 4 * (Real.eulerMascheroniConstant - 3 / 2))) := by
  have h := (Real.tendsto_harmonic_sub_log.sub_const (3 / 2 : ℝ)).const_mul (15 / 4 : ℝ)
  refine h.congr' ?_
  filter_upwards [eventually_ge_atTop 2] with M hM
  rw [log_sum M hM]; ring

/-- ⛭ **`residue_product`.** the second-order sum's leading coefficient `½` is the product of two residues over
their locations, `(2/4)(2/2)`, and it is the `M⁴` coefficient of `Σ 2m³` -/
theorem residue_product : (2 / 4 : ℝ) * (2 / 2) = 1 / 2 ∧ (2 / 4 : ℝ) = 1 / 2 := by norm_num

end E

end R73Vertex

end ShadowProbe

#print axioms ShadowProbe.R73Vertex.misner
#print axioms ShadowProbe.R73Vertex.unimodular
#print axioms ShadowProbe.R73Vertex.R3_round
#print axioms ShadowProbe.R73Vertex.R3_milnor
#print axioms ShadowProbe.R73Vertex.taylor
#print axioms ShadowProbe.R73Vertex.shapes
#print axioms ShadowProbe.R73Vertex.calibration
#print axioms ShadowProbe.R73Vertex.kinetic_linear
#print axioms ShadowProbe.R73Vertex.kinetic_exponential
#print axioms ShadowProbe.R73Vertex.unit_jacobian
#print axioms ShadowProbe.R73Vertex.quartic_vev
#print axioms ShadowProbe.R73Vertex.cubic_three_quanta
#print axioms ShadowProbe.R73Vertex.one_quantum_cancels
#print axioms ShadowProbe.R73Vertex.cubic_shift
#print axioms ShadowProbe.R73Vertex.fock_receipt
#print axioms ShadowProbe.R73Vertex.normalisation
#print axioms ShadowProbe.R73Vertex.total_shift
#print axioms ShadowProbe.R73Vertex.at_level_three
#print axioms ShadowProbe.R73Vertex.threshold
#print axioms ShadowProbe.R73Vertex.density_a6
#print axioms ShadowProbe.R73Vertex.linear_solves
#print axioms ShadowProbe.R73Vertex.rank_two
#print axioms ShadowProbe.R73Vertex.dmu_residues
#print axioms ShadowProbe.R73Vertex.dovmu_residues
#print axioms ShadowProbe.R73Vertex.faulhaber
#print axioms ShadowProbe.R73Vertex.log_coeff
#print axioms ShadowProbe.R73Vertex.residue_product

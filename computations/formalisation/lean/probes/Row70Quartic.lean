import ShadowEngine
import Mathlib.NumberTheory.Harmonic.EulerMascheroni
import Mathlib.LinearAlgebra.Matrix.Rank
import Mathlib.LinearAlgebra.Matrix.Hermitian

/-! # Campaign 41 (`r7443+71.26`): library-gap row 70, the second-order term is the quartic's deviation from the
cubic's own completion, and the counterterm collapses to `Λ³`

The receipt is
`P10_the_second_order_term_is_the_quartics_deviation_from_the_cubics_own_completion_and_the_counterterm_collapses_to_lambda_cubed.py`.
Its COMPUTED checks A–F are built here; its paper-text content is not formalised.

***The second-order energy is the receipt's FORMAL formula on finite matrix elements*** (`dE2`), NOT an eigenvalue
statement: the cubic oscillator is unbounded below. Matrices are `(N + 4) × (N + 4)` truncations, for EVERY `N`
(the receipt's sizes `8, 12, 16, 18` are `N = 4, 8, 12, 14`); `ħ = 1`.

- ***A.*** `dE2_closed` (`(6g₄w² − 11g₃²)/(8w⁴)` on every truncation), `dE2_receipt_sizes`; `conj_zero` (general
  Hermitian `A`), `conj_q3` (`27/(8w²)`), `conj_q3qpq` (`27/(8w²) + 19/8`).
- ***B.*** `gen_solves`, `fake_vev`, `fake_zero`, `deviation` (general, non-resonant Hermitian `H₃`); `cubic_nonres`,
  `fake_receipt`, `locus`.
- ***C.*** `no_cancellation`, `pure_cubic_even`, `g3_derivs`, `trace_cube`, `trace_cube_cases`.
- ***D.*** `bookkeeping`; `closed_dS` (THE Levi-Civita curvature of closed de Sitter, all `256` components maximally
  symmetric, `R = 12/α²`); `frame_values`, `frame_weyl`, `eight_homogeneous`; the control: `RlT_bi` (Riemann from the
  Christoffel engine at `T = 1`), `bianchi_connection` (the same for THE connection), `control` (`C² = 28/3`, cubic
  Weyl `40/9`, `20/9`), `bi_scal`/`bi_gradient` (`R = 38/T²`, `R′(1) = −76`), `ratios_distinct`.
- ***E.*** `derivative_test`, `gauge_ratio`, `combo_homogeneous`, `eight_homogeneous`.
- ***F.*** `ranks` (`1`, `2`), `residue_scheme`, `cited_bound`, `any_target`.

***Imported, not built:*** the `r6990` bound `3/10¹²²` and the shear's `1/60` (cited constants, `cited_bound`,
`derivative_test`); the TT spectrum `m² − 1`, `2(m² − 4)` and the overlap `6π² det h` (data in E only). The closed
slicing's profiles `S₁ = sin²χ`, `S₂ = sin²θ` are hypotheses near the point, nowhere-zero globally (as in `FRWk.lean`).
Copied (probes do not import probes): `cF`, `fRk`, `frw_tab_k`, `prof_sin2` from `FRWk.lean` (restricted to `i < j`),
`rank_eq_of_factor` from `Row64Descent.lean`. The control's eight scalars `ctl` were computed with the receipt's
definitions; the receipt prints only their ratio count. -/

namespace ShadowProbe
namespace R70Quartic

open Matrix Complex Finset

section RS

variable {ι : Type*} [Fintype ι] [DecidableEq ι]

/-- the cubic channel `Σ_{s≠v} |⟨s|H₃|v⟩|²/(E_s − E_v)` (Lean's `x/0 = 0` drops degenerate `s`, whose numerators
vanish for a non-resonant `H₃` anyway) -/
noncomputable def cubicCh (E : ι → ℝ) (v : ι) (H3 : Matrix ι ι ℂ) : ℂ :=
  ∑ s ∈ univ.erase v, ((Complex.normSq (H3 s v) / (E s - E v) : ℝ) : ℂ)

/-- **The receipt's FORMAL Rayleigh–Schrödinger second-order energy** `⟨v|H₄|v⟩ − Σ_{s≠v}|⟨s|H₃|v⟩|²/(E_s − E_v)`, a
function of finitely many matrix elements. It is **not** asserted to be the `λ²` coefficient of any eigenvalue: the
cubic oscillator `H₀ + λg₃q³` is unbounded below and has no ground state, and nothing here says otherwise. -/
noncomputable def dE2 (E : ι → ℝ) (v : ι) (H3 H4 : Matrix ι ι ℂ) : ℂ := H4 v v - cubicCh E v H3

noncomputable def H0m (E : ι → ℝ) : Matrix ι ι ℂ := diagonal fun i => (E i : ℂ)

omit [Fintype ι] [DecidableEq ι] in
lemma herm_mul_conj {A : Matrix ι ι ℂ} (hA : Matrix.IsHermitian A) (s v : ι) :
    A v s * A s v = (Complex.normSq (A s v) : ℂ) := by
  have : A v s = star (A s v) := (hA.apply v s).symm
  rw [this, Complex.normSq_eq_conj_mul_self]; rfl

lemma comm_entry (E : ι → ℝ) (A : Matrix ι ι ℂ) (s t : ι) :
    (A * H0m E - H0m E * A) s t = A s t * ((E t : ℂ) - E s) := by
  simp only [Matrix.sub_apply, H0m, mul_diagonal, diagonal_mul]; ring

/-- sum over all `s` of a summand vanishing at `v` is the sum over `s ≠ v` -/
lemma sum_erase_of (f : ι → ℂ) (v : ι) (h : f v = 0) : ∑ s, f s = ∑ s ∈ univ.erase v, f s := by
  rw [← Finset.add_sum_erase _ _ (mem_univ v), h, zero_add]

theorem conj_channels (E : ι → ℝ) (v : ι) (A : Matrix ι ι ℂ) (hA : Matrix.IsHermitian A) :
    (-(1 / 2 : ℂ) • (A * (A * H0m E - H0m E * A) - (A * H0m E - H0m E * A) * A)) v v
      = ∑ s ∈ univ.erase v, ((Complex.normSq (A s v) * (E s - E v) : ℝ) : ℂ) ∧
    cubicCh E v (I • (A * H0m E - H0m E * A))
      = ∑ s ∈ univ.erase v, ((Complex.normSq (A s v) * (E s - E v) : ℝ) : ℂ) := by
  constructor
  · simp only [Matrix.smul_apply, Matrix.sub_apply, smul_eq_mul]
    rw [Matrix.mul_apply, Matrix.mul_apply]
    simp only [comm_entry]
    rw [← Finset.sum_sub_distrib, Finset.mul_sum, sum_erase_of _ v (by ring)]
    refine Finset.sum_congr rfl fun s _ => ?_
    have h1 := herm_mul_conj hA s v
    push_cast
    linear_combination (-(E v : ℂ) + E s) * h1
  · unfold cubicCh
    refine Finset.sum_congr rfl fun s _ => ?_
    congr 1
    simp only [Matrix.smul_apply, comm_entry, smul_eq_mul]
    rw [Complex.normSq_mul, Complex.normSq_mul, Complex.normSq_I, ← Complex.ofReal_sub, Complex.normSq_ofReal]
    by_cases h : E s - E v = 0
    · rw [h]; simp [show E v - E s = 0 by linarith]
    · field_simp; ring

/-- ⛭ the discriminating zero, in general: for ANY Hermitian `A`, the order-`λ²` pair of
`e^{iλA} H₀ e^{−iλA}` has `dE₂ = 0`, its two channels both equal to `Σ_{s≠v} |A_{sv}|² (E_s − E_v)` -/
theorem conj_zero (E : ι → ℝ) (v : ι) (A : Matrix ι ι ℂ) (hA : Matrix.IsHermitian A) :
    dE2 E v (I • (A * H0m E - H0m E * A))
      (-(1 / 2 : ℂ) • (A * (A * H0m E - H0m E * A) - (A * H0m E - H0m E * A) * A)) = 0 := by
  rw [dE2, (conj_channels E v A hA).1, (conj_channels E v A hA).2, sub_self]

/-- the receipt's elementwise generator: `A_{mn} = H₃_{mn} / (i(E_n − E_m))` off resonance -/
noncomputable def gen (E : ι → ℝ) (H3 : Matrix ι ι ℂ) : Matrix ι ι ℂ :=
  Matrix.of fun m n => if E n ≠ E m then H3 m n / (I * ((E n : ℂ) - E m)) else 0

/-- non-resonance: no energy-diagonal matrix element -/
def NonRes (E : ι → ℝ) (H3 : Matrix ι ι ℂ) : Prop := ∀ m n, E m = E n → H3 m n = 0

theorem gen_solves (E : ι → ℝ) (H3 : Matrix ι ι ℂ) (hN : NonRes E H3) :
    I • (gen E H3 * H0m E - H0m E * gen E H3) = H3 := by
  ext m n
  rw [Matrix.smul_apply, comm_entry, smul_eq_mul]
  simp only [gen, Matrix.of_apply]
  split_ifs with h
  · have : (E n : ℂ) - E m ≠ 0 := by rw [← Complex.ofReal_sub]; exact_mod_cast sub_ne_zero.2 h
    field_simp
  · push Not at h; rw [hN m n h.symm]; ring

/-- `⟨v|H₄fake|v⟩` is the cubic channel itself -/
theorem fake_vev (E : ι → ℝ) (v : ι) (H3 : Matrix ι ι ℂ) (hH : Matrix.IsHermitian H3) (hN : NonRes E H3) :
    ((I / 2) • (gen E H3 * H3 - H3 * gen E H3)) v v = cubicCh E v H3 := by
  simp only [Matrix.smul_apply, Matrix.sub_apply, Matrix.mul_apply, smul_eq_mul, cubicCh]
  rw [← Finset.sum_sub_distrib, Finset.mul_sum, sum_erase_of _ v (by simp [gen])]
  refine Finset.sum_congr rfl fun s _ => ?_
  have h1 := herm_mul_conj hH s v
  simp only [gen, Matrix.of_apply]
  by_cases h : E s = E v
  · simp [h, hN s v h, hN v s h.symm]
  · simp only [ne_eq, Ne.symm h, h, not_false_eq_true, ite_true]
    have hs : (E s : ℂ) - E v ≠ 0 := by rw [← Complex.ofReal_sub]; exact_mod_cast sub_ne_zero.2 h
    have hs' : (E v : ℂ) - E s ≠ 0 := by rw [← Complex.ofReal_sub]; exact_mod_cast sub_ne_zero.2 (Ne.symm h)
    push_cast
    field_simp
    linear_combination (2 * ((E v : ℂ) - E s)) * h1

theorem fake_zero (E : ι → ℝ) (v : ι) (H3 : Matrix ι ι ℂ) (hH : Matrix.IsHermitian H3) (hN : NonRes E H3) :
    dE2 E v H3 ((I / 2) • (gen E H3 * H3 - H3 * gen E H3)) = 0 := by
  rw [dE2, fake_vev E v H3 hH hN, sub_self]

theorem deviation (E : ι → ℝ) (v : ι) (H3 H4 : Matrix ι ι ℂ) (hH : Matrix.IsHermitian H3) (hN : NonRes E H3) :
    dE2 E v H3 H4 = H4 v v - ((I / 2) • (gen E H3 * H3 - H3 * gen E H3)) v v := by
  rw [dE2, fake_vev E v H3 hH hN]

end RS


section ladder

variable (N : ℕ)

/-- `|n⟩` in the space of the lowest `N + 4` levels -/
def ket (n : ℕ) : Fin (N + 4) → ℂ := fun i => if (i : ℕ) = n then 1 else 0

/-- `a`, truncated: `a_{n−1,n} = √n` -/
noncomputable def lowM : Matrix (Fin (N + 4)) (Fin (N + 4)) ℂ :=
  Matrix.of fun i j => if (j : ℕ) = i + 1 then (Real.sqrt j : ℂ) else 0

/-- `a†`, truncated -/
noncomputable def raiseM : Matrix (Fin (N + 4)) (Fin (N + 4)) ℂ :=
  Matrix.of fun i j => if (i : ℕ) = j + 1 then (Real.sqrt i : ℂ) else 0

lemma low_ket (n : ℕ) (h : n + 1 < N + 4) :
    lowM N *ᵥ ket N (n + 1) = (Real.sqrt (n + 1) : ℂ) • ket N n := by
  funext i
  simp only [mulVec, dotProduct, lowM, ket, Matrix.of_apply, Pi.smul_apply, smul_eq_mul, mul_ite, mul_one,
    mul_zero]
  rw [Finset.sum_eq_single ⟨n + 1, h⟩]
  · by_cases hi : (i : ℕ) = n
    · simp [hi]
    · simp [hi]; omega
  · intro j _ hj
    have : (j : ℕ) ≠ n + 1 := fun e => hj (Fin.ext e)
    simp [this]
  · simp

lemma low_ket0 : lowM N *ᵥ ket N 0 = 0 := by
  funext i
  simp only [mulVec, dotProduct, lowM, ket, Matrix.of_apply, mul_ite, mul_one, mul_zero, Pi.zero_apply]
  refine Finset.sum_eq_zero fun j _ => ?_
  split_ifs with h1 h2 <;> first | rfl | omega

lemma raise_ket (n : ℕ) (h : n + 1 < N + 4) :
    raiseM N *ᵥ ket N n = (Real.sqrt (n + 1) : ℂ) • ket N (n + 1) := by
  funext i
  simp only [mulVec, dotProduct, raiseM, ket, Matrix.of_apply, Pi.smul_apply, smul_eq_mul, mul_ite, mul_one,
    mul_zero]
  rw [Finset.sum_eq_single ⟨n, by omega⟩]
  · by_cases hi : (i : ℕ) = n + 1
    · simp [hi]
    · simp [hi]
  · intro j _ hj
    have : (j : ℕ) ≠ n := fun e => hj (Fin.ext e)
    simp [this]
  · simp


/-- the three kets the vacuum column reaches, as functions -/
lemma ket_apply (n : ℕ) (i : Fin (N + 4)) : ket N n i = if (i : ℕ) = n then 1 else 0 := rfl

variable (w : ℝ)

/-- `1/√(2w)` -/
noncomputable def cq : ℝ := (Real.sqrt (2 * w))⁻¹
/-- `√(w/2)` -/
noncomputable def kq : ℝ := Real.sqrt (w / 2)

/-- `q = (a + a†)/√(2w)` -/
noncomputable def qM : Matrix (Fin (N + 4)) (Fin (N + 4)) ℂ := (cq w : ℂ) • (lowM N + raiseM N)
/-- `p = i√(w/2)(a† − a)` -/
noncomputable def pM : Matrix (Fin (N + 4)) (Fin (N + 4)) ℂ := (I * (kq w : ℂ)) • (raiseM N - lowM N)
/-- `E_n = w(n + ½)` (`ħ = 1`) -/
noncomputable def En : Fin (N + 4) → ℝ := fun n => w * ((n : ℝ) + 1 / 2)

lemma qv0 : qM N w *ᵥ ket N 0 = (cq w : ℂ) • ket N 1 := by
  rw [qM, smul_mulVec, add_mulVec, low_ket0, raise_ket N 0 (by omega)]; simp

lemma qv1 : qM N w *ᵥ ket N 1 = (cq w : ℂ) • (ket N 0 + (Real.sqrt 2 : ℂ) • ket N 2) := by
  rw [qM, smul_mulVec, add_mulVec, low_ket N 0 (by omega), raise_ket N 1 (by omega)]; norm_num

lemma qv2 : qM N w *ᵥ ket N 2 = (cq w : ℂ) • ((Real.sqrt 2 : ℂ) • ket N 1 + (Real.sqrt 3 : ℂ) • ket N 3) := by
  rw [qM, smul_mulVec, add_mulVec, low_ket N 1 (by omega), raise_ket N 2 (by omega)]; norm_num

lemma pv1 : pM N w *ᵥ ket N 1 = (I * (kq w : ℂ)) • ((Real.sqrt 2 : ℂ) • ket N 2 - ket N 0) := by
  rw [pM, smul_mulVec, sub_mulVec, low_ket N 0 (by omega), raise_ket N 1 (by omega)]; norm_num

/-- row `0` of `q`: `(qψ)₀ = ψ₁/√(2w)` -/
lemma q_row0 (ψ : Fin (N + 4) → ℂ) : (qM N w *ᵥ ψ) 0 = (cq w : ℂ) * ψ 1 := by
  simp only [qM, smul_mulVec, Pi.smul_apply, smul_eq_mul, add_mulVec, Pi.add_apply]
  congr 1
  simp only [mulVec, dotProduct, lowM, raiseM, Matrix.of_apply]
  rw [Finset.sum_eq_single 1]
  · simp
  · intro j _ hj
    have : (j : ℕ) ≠ 1 := fun e => hj (Fin.ext (by simp [e]))
    simp [this]
  · simp

lemma s22 : (Real.sqrt 2 : ℂ) * (Real.sqrt 2 : ℂ) = 2 := by
  rw [← Complex.ofReal_mul, Real.mul_self_sqrt (by norm_num)]; norm_num
lemma s23 : (Real.sqrt 2 : ℂ) * (Real.sqrt 3 : ℂ) = (Real.sqrt 6 : ℂ) := by
  rw [← Complex.ofReal_mul, ← Real.sqrt_mul (by norm_num)]; norm_num

/-- `q³|0⟩ = (3|1⟩ + √6|3⟩)/(2w)^{3/2}` -/
lemma q3v : (qM N w * qM N w * qM N w) *ᵥ ket N 0
    = (cq w : ℂ) ^ 3 • ((3 : ℂ) • ket N 1 + (Real.sqrt 6 : ℂ) • ket N 3) := by
  rw [← mulVec_mulVec, ← mulVec_mulVec]
  simp only [qv0, qv1, qv2, mulVec_smul, mulVec_add]
  funext i
  simp only [Pi.smul_apply, Pi.add_apply, smul_eq_mul]
  linear_combination (cq w : ℂ) ^ 3 * ket N 1 i * s22 + (cq w : ℂ) ^ 3 * ket N 3 i * s23

/-- `qpq|0⟩ = i√(w/2)(|1⟩ + √6|3⟩)/(2w)` -/
lemma qpqv : (qM N w * pM N w * qM N w) *ᵥ ket N 0
    = (I * (kq w : ℂ) * (cq w : ℂ) ^ 2) • (ket N 1 + (Real.sqrt 6 : ℂ) • ket N 3) := by
  rw [← mulVec_mulVec, ← mulVec_mulVec]
  simp only [qv0, pv1, qv2, mulVec_smul, mulVec_sub]
  funext i
  simp only [Pi.smul_apply, Pi.add_apply, Pi.sub_apply, smul_eq_mul]
  linear_combination I * (kq w : ℂ) * (cq w : ℂ) ^ 2 * ket N 1 i * s22
    + I * (kq w : ℂ) * (cq w : ℂ) ^ 2 * ket N 3 i * s23

/-- `(M ψ)` at `s`, against the vacuum column: `M_{s0} = (M|0⟩)_s` -/
lemma col0 (M : Matrix (Fin (N + 4)) (Fin (N + 4)) ℂ) (s : Fin (N + 4)) : M s 0 = (M *ᵥ ket N 0) s := by
  simp only [mulVec, dotProduct, ket]
  rw [Finset.sum_eq_single 0]
  · simp
  · intro j _ hj; have : (j : ℕ) ≠ 0 := fun e => hj (Fin.ext (by simp [e])); simp [this]
  · simp

/-- `⟨0|q⁴|0⟩ = 3/(4w²)`, as `3 c⁴` -/
lemma q4vev : (qM N w * qM N w * qM N w * qM N w) 0 0 = 3 * (cq w : ℂ) ^ 4 := by
  rw [col0 N (qM N w * qM N w * qM N w * qM N w) 0,
    show qM N w * qM N w * qM N w * qM N w = qM N w * (qM N w * qM N w * qM N w) by simp only [mul_assoc],
    ← mulVec_mulVec, q3v, q_row0]
  simp [ket]; ring


lemma low_ct : (lowM N)ᴴ = raiseM N := by
  ext i j
  simp only [conjTranspose_apply, lowM, raiseM, Matrix.of_apply]
  split_ifs <;> simp

lemma raise_ct : (raiseM N)ᴴ = lowM N := by rw [← low_ct, conjTranspose_conjTranspose]

lemma qM_herm : (qM N w)ᴴ = qM N w := by
  rw [qM, conjTranspose_smul, conjTranspose_add, low_ct, raise_ct, add_comm (raiseM N)]
  simp

lemma pM_herm : (pM N w)ᴴ = pM N w := by
  rw [pM, conjTranspose_smul, conjTranspose_sub, low_ct, raise_ct]
  rw [show star (I * (kq w : ℂ)) = -(I * (kq w : ℂ)) by simp]
  rw [neg_smul, ← smul_neg, neg_sub]

lemma pal_herm {A B : Matrix (Fin (N + 4)) (Fin (N + 4)) ℂ} (hA : Aᴴ = A) (hB : Bᴴ = B) :
    Matrix.IsHermitian (A * B * A) := by
  unfold Matrix.IsHermitian
  rw [conjTranspose_mul, conjTranspose_mul, hA, hB, mul_assoc]

/-- odd/even parity of a matrix in the level label -/
def OddM (M : Matrix (Fin (N + 4)) (Fin (N + 4)) ℂ) : Prop := ∀ i j : Fin (N + 4), ((i : ℕ) + j) % 2 = 0 → M i j = 0
def EvenM (M : Matrix (Fin (N + 4)) (Fin (N + 4)) ℂ) : Prop := ∀ i j : Fin (N + 4), ((i : ℕ) + j) % 2 = 1 → M i j = 0

lemma qM_odd : OddM N (qM N w) := by
  intro i j h
  simp only [qM, Matrix.smul_apply, Matrix.add_apply, lowM, raiseM, Matrix.of_apply, smul_eq_mul]
  simp only [show ¬ ((j : ℕ) = i + 1) by omega, show ¬ ((i : ℕ) = j + 1) by omega, ite_false]; simp

lemma odd_odd {A B : Matrix (Fin (N + 4)) (Fin (N + 4)) ℂ} (hA : OddM N A) (hB : OddM N B) : EvenM N (A * B) := by
  intro i j h
  rw [Matrix.mul_apply]
  refine Finset.sum_eq_zero fun k _ => ?_
  rcases Nat.mod_two_eq_zero_or_one ((i : ℕ) + k) with h1 | h1
  · rw [hA i k h1, zero_mul]
  · rw [hB k j (by omega), mul_zero]

lemma even_odd {A B : Matrix (Fin (N + 4)) (Fin (N + 4)) ℂ} (hA : EvenM N A) (hB : OddM N B) : OddM N (A * B) := by
  intro i j h
  rw [Matrix.mul_apply]
  refine Finset.sum_eq_zero fun k _ => ?_
  rcases Nat.mod_two_eq_zero_or_one ((i : ℕ) + k) with h1 | h1
  · rw [hB k j (by omega), mul_zero]
  · rw [hA i k h1, zero_mul]

lemma En_inj (hw : w ≠ 0) {m n : Fin (N + 4)} (h : En N w m = En N w n) : m = n := by
  simp only [En] at h
  have : (m : ℝ) = n := by
    have := mul_left_cancel₀ hw h; linarith
  exact Fin.ext (by exact_mod_cast this)

/-- ⛭ **non-resonance**: every matrix element of `g₃q³` between equal energies vanishes (parity) -/
theorem cubic_nonres (hw : w ≠ 0) (g3 : ℝ) : NonRes (En N w) ((g3 : ℂ) • (qM N w * qM N w * qM N w)) := by
  intro m n h
  have := En_inj N w hw h; subst this
  rw [Matrix.smul_apply, even_odd N (odd_odd N (qM_odd N w) (qM_odd N w)) (qM_odd N w) m m (by omega),
    smul_zero]

lemma cubic_herm (g3 : ℝ) : Matrix.IsHermitian ((g3 : ℂ) • (qM N w * qM N w * qM N w)) := by
  unfold Matrix.IsHermitian
  rw [conjTranspose_smul, (pal_herm N (qM_herm N w) (qM_herm N w)).eq]; simp

lemma fv1 : ((1 : Fin (N + 4)) : ℕ) = 1 := by simp
lemma fv3 : ((3 : Fin (N + 4)) : ℕ) = 3 := by simp

/-- a vacuum-column sum over `s ≠ 0` supported on `s ∈ {1, 3}` -/
lemma sum13 (f : Fin (N + 4) → ℂ) (h : ∀ s : Fin (N + 4), (s : ℕ) ≠ 1 → (s : ℕ) ≠ 3 → f s = 0) :
    ∑ s ∈ univ.erase 0, f s = f 1 + f 3 := by
  have h1 := fv1 N
  have h3 := fv3 N
  rw [← Finset.sum_subset (s₁ := {1, 3})]
  · rw [Finset.sum_pair]; intro e; have := congrArg Fin.val e; omega
  · intro x hx
    simp only [Finset.mem_insert, Finset.mem_singleton] at hx
    rcases hx with rfl | rfl <;> simp only [Finset.mem_erase, ne_eq, Finset.mem_univ, and_true] <;>
      intro e <;> have := congrArg Fin.val e <;> simp only [h1, h3, Fin.val_zero] at this <;> omega
  · intro x _ hx
    simp only [Finset.mem_insert, Finset.mem_singleton, not_or] at hx
    exact h x (fun e => hx.1 (Fin.ext (by rw [e, h1]))) (fun e => hx.2 (Fin.ext (by rw [e, h3])))

lemma ket1_1 : ket N 1 1 = 1 := by simp only [ket, fv1]; simp
lemma ket3_1 : ket N 3 1 = 0 := by simp only [ket, fv1]; simp
lemma ket1_3 : ket N 1 3 = 0 := by simp only [ket, fv3]; simp
lemma ket3_3 : ket N 3 3 = 1 := by simp only [ket, fv3]; simp

lemma ket13_zero (s : Fin (N + 4)) (h1 : (s : ℕ) ≠ 1) (h3 : (s : ℕ) ≠ 3) : ket N 1 s = 0 ∧ ket N 3 s = 0 := by
  simp [ket, h1, h3]

lemma En_1 : En N w 1 - En N w 0 = w := by simp only [En, fv1, Fin.val_zero]; push_cast; ring
lemma En_3 : En N w 3 - En N w 0 = 3 * w := by simp only [En, fv3, Fin.val_zero]; push_cast; ring

lemma cq_sq (hw : 0 < w) : cq w ^ 2 = 1 / (2 * w) := by
  rw [cq, inv_pow, Real.sq_sqrt (by positivity), one_div]
lemma kq_sq (hw : 0 < w) : kq w ^ 2 = w / 2 := by
  rw [kq, Real.sq_sqrt (by positivity)]

/-- the column `α|1⟩ + β|3⟩`: its cubic channel is `|α|²/w + |β|²/3w` -/
lemma cubic_of_col (H : Matrix (Fin (N + 4)) (Fin (N + 4)) ℂ) (α β : ℂ)
    (hH : ∀ s, H s 0 = α * ket N 1 s + β * ket N 3 s) :
    cubicCh (En N w) 0 H = ((Complex.normSq α / w + Complex.normSq β / (3 * w) : ℝ) : ℂ) := by
  unfold cubicCh
  rw [sum13 N]
  · rw [hH, hH, ket1_1, ket3_1, ket1_3, ket3_3, En_1, En_3]; push_cast; ring_nf
  · intro s h1 h3
    obtain ⟨e1, e3⟩ := ket13_zero N s h1 h3
    rw [hH, e1, e3]; simp

/-- and its conjugation channel `Σ|α_s|²(E_s − E_0)` is `|α|²w + 3|β|²w` -/
lemma conj_of_col (A : Matrix (Fin (N + 4)) (Fin (N + 4)) ℂ) (α β : ℂ)
    (hA : ∀ s, A s 0 = α * ket N 1 s + β * ket N 3 s) :
    ∑ s ∈ univ.erase 0, ((Complex.normSq (A s 0) * (En N w s - En N w 0) : ℝ) : ℂ)
      = ((Complex.normSq α * w + Complex.normSq β * (3 * w) : ℝ) : ℂ) := by
  rw [sum13 N]
  · rw [hA, hA, ket1_1, ket3_1, ket1_3, ket3_3, En_1, En_3]; push_cast; ring_nf
  · intro s h1 h3
    obtain ⟨e1, e3⟩ := ket13_zero N s h1 h3
    rw [hA, e1, e3]; simp

lemma q3col (s : Fin (N + 4)) :
    (qM N w * qM N w * qM N w) s 0 = (3 * (cq w : ℂ) ^ 3) * ket N 1 s + (Real.sqrt 6 * (cq w : ℂ) ^ 3) * ket N 3 s := by
  rw [col0 N (qM N w * qM N w * qM N w) s, q3v]; simp only [Pi.smul_apply, Pi.add_apply, smul_eq_mul]; ring

lemma qpqcol (s : Fin (N + 4)) :
    (qM N w * pM N w * qM N w) s 0 = (I * (kq w : ℂ) * (cq w : ℂ) ^ 2) * ket N 1 s
      + (I * (kq w : ℂ) * (cq w : ℂ) ^ 2 * Real.sqrt 6) * ket N 3 s := by
  rw [col0 N (qM N w * pM N w * qM N w) s, qpqv]; simp only [Pi.smul_apply, Pi.add_apply, smul_eq_mul]; ring

/-- the term of the cubic channel at `s` -/
noncomputable def cterm (H3 : Matrix (Fin (N + 4)) (Fin (N + 4)) ℂ) (s : Fin (N + 4)) : ℝ :=
  Complex.normSq (H3 s 0) / (En N w s - En N w 0)

end ladder


section main

variable (N : ℕ) {w : ℝ} (hw : 0 < w)
include hw

/-- the receipt's closed form `(6g₄w² − 11g₃²)/(8w⁴)` -/
noncomputable def closedE (w g3 g4 : ℝ) : ℝ := (6 * g4 * w ^ 2 - 11 * g3 ^ 2) / (8 * w ^ 4)

omit hw in
lemma s66 : Real.sqrt 6 * Real.sqrt 6 = 6 := Real.mul_self_sqrt (by norm_num)

lemma c6 : cq w ^ 6 = 1 / (8 * w ^ 3) := by
  rw [show cq w ^ 6 = (cq w ^ 2) ^ 3 by ring, cq_sq w hw]; field_simp; ring

omit hw in
lemma q3col_real (g3 : ℝ) (s : Fin (N + 4)) : ((g3 : ℂ) • (qM N w * qM N w * qM N w)) s 0
    = ((g3 * 3 * cq w ^ 3 : ℝ) : ℂ) * ket N 1 s + ((g3 * Real.sqrt 6 * cq w ^ 3 : ℝ) : ℂ) * ket N 3 s := by
  rw [Matrix.smul_apply, q3col, smul_eq_mul]; push_cast; ring

/-- the cubic channel of `g₃q³` is `11g₃²/(8w⁴)` -/
theorem cubic_channel (g3 : ℝ) :
    cubicCh (En N w) 0 ((g3 : ℂ) • (qM N w * qM N w * qM N w)) = ((11 * g3 ^ 2 / (8 * w ^ 4) : ℝ) : ℂ) := by
  rw [cubic_of_col N w _ _ _ (q3col_real N g3)]
  congr 1
  simp only [Complex.normSq_ofReal]
  rw [show g3 * 3 * cq w ^ 3 * (g3 * 3 * cq w ^ 3) = 9 * g3 ^ 2 * cq w ^ 6 by ring,
    show g3 * Real.sqrt 6 * cq w ^ 3 * (g3 * Real.sqrt 6 * cq w ^ 3)
      = (Real.sqrt 6 * Real.sqrt 6) * g3 ^ 2 * cq w ^ 6 by ring, s66, c6 hw]
  field_simp; ring

/-- ⛭ **`dE2_closed` (A).** On EVERY truncation keeping at least four levels (`N + 4`), the formal
second-order vacuum energy of `(g₃q³, g₄q⁴)` is exactly `(6g₄w² − 11g₃²)/(8w⁴)`. -/
theorem dE2_closed (g3 g4 : ℝ) :
    dE2 (En N w) 0 ((g3 : ℂ) • (qM N w * qM N w * qM N w)) ((g4 : ℂ) • (qM N w * qM N w * qM N w * qM N w))
      = (closedE w g3 g4 : ℂ) := by
  rw [dE2, Matrix.smul_apply, q4vev, cubic_channel N hw, smul_eq_mul, closedE]
  have h4 : (cq w : ℂ) ^ 4 = ((1 / (4 * w ^ 2) : ℝ) : ℂ) := by
    rw [← Complex.ofReal_pow, show cq w ^ 4 = (cq w ^ 2) ^ 2 by ring, cq_sq w hw]; congr 1; field_simp; ring
  rw [h4]; push_cast
  have : (w : ℂ) ≠ 0 := by exact_mod_cast hw.ne'
  field_simp; ring

/-- the receipt's own sizes, `8` and `12`: the two values agree because both are the closed form -/
theorem dE2_receipt_sizes (g3 g4 : ℝ) :
    dE2 (En 4 w) 0 ((g3 : ℂ) • (qM 4 w * qM 4 w * qM 4 w)) ((g4 : ℂ) • (qM 4 w * qM 4 w * qM 4 w * qM 4 w))
      = dE2 (En 8 w) 0 ((g3 : ℂ) • (qM 8 w * qM 8 w * qM 8 w)) ((g4 : ℂ) • (qM 8 w * qM 8 w * qM 8 w * qM 8 w)) ∧
    dE2 (En 4 w) 0 ((g3 : ℂ) • (qM 4 w * qM 4 w * qM 4 w)) ((g4 : ℂ) • (qM 4 w * qM 4 w * qM 4 w * qM 4 w))
      = (closedE w g3 g4 : ℂ) := by
  rw [dE2_closed 4 hw, dE2_closed 8 hw]; exact ⟨rfl, rfl⟩

omit hw in
lemma q_herm' : Matrix.IsHermitian (qM N w * qM N w * qM N w) := pal_herm N (qM_herm N w) (qM_herm N w)
omit hw in
lemma qpq_herm : Matrix.IsHermitian (qM N w * pM N w * qM N w) := pal_herm N (qM_herm N w) (pM_herm N w)

/-- ⛭ **`conj_q3` (A, the discriminating zero, `A = q³`).** `H₃ = i[A,H₀]`, `H₄ = −[A,[A,H₀]]/2`: `dE₂ = 0`, both
channels equal `27/(8w²) ≠ 0`, and `H₃` connects the vacuum to something. -/
theorem conj_q3 :
    let A := qM N w * qM N w * qM N w
    let H3u := I • (A * H0m (En N w) - H0m (En N w) * A)
    let H4u := -(1 / 2 : ℂ) • (A * (A * H0m (En N w) - H0m (En N w) * A) - (A * H0m (En N w) - H0m (En N w) * A) * A)
    dE2 (En N w) 0 H3u H4u = 0 ∧ H4u 0 0 = ((27 / (8 * w ^ 2) : ℝ) : ℂ) ∧
      cubicCh (En N w) 0 H3u = ((27 / (8 * w ^ 2) : ℝ) : ℂ) ∧ (27 / (8 * w ^ 2) : ℝ) ≠ 0 ∧ ∃ s, H3u s 0 ≠ 0 := by
  intro A H3u H4u
  have hA := q_herm' N (w := w)
  have hcol : ∀ s, A s 0 = ((3 * cq w ^ 3 : ℝ) : ℂ) * ket N 1 s + ((Real.sqrt 6 * cq w ^ 3 : ℝ) : ℂ) * ket N 3 s :=
    fun s => by simp only [A]; rw [q3col]; push_cast; ring
  have hv : ((Complex.normSq ((3 * cq w ^ 3 : ℝ) : ℂ) * w + Complex.normSq ((Real.sqrt 6 * cq w ^ 3 : ℝ) : ℂ)
      * (3 * w) : ℝ) : ℂ) = ((27 / (8 * w ^ 2) : ℝ) : ℂ) := by
    congr 1
    simp only [Complex.normSq_ofReal]
    rw [show 3 * cq w ^ 3 * (3 * cq w ^ 3) = 9 * cq w ^ 6 by ring,
      show Real.sqrt 6 * cq w ^ 3 * (Real.sqrt 6 * cq w ^ 3) = (Real.sqrt 6 * Real.sqrt 6) * cq w ^ 6 by ring,
      s66, c6 hw]
    field_simp; ring
  have h1 := (conj_channels (En N w) 0 A hA).1
  have h2 := (conj_channels (En N w) 0 A hA).2
  rw [conj_of_col N w A _ _ hcol, hv] at h1 h2
  have hne : (27 / (8 * w ^ 2) : ℝ) ≠ 0 := by positivity
  refine ⟨conj_zero _ _ A hA, h1, h2, hne, ?_⟩
  by_contra hall
  push Not at hall
  have : cubicCh (En N w) 0 H3u = 0 := Finset.sum_eq_zero fun s _ => by simp [hall s]
  rw [h2] at this; exact hne (by exact_mod_cast this)

/-- ⛭ **`conj_q3qpq` (A, `A = q³ + qpq`).** The same zero, with both channels `27/(8w²) + 19/8`. -/
theorem conj_q3qpq :
    let A := qM N w * qM N w * qM N w + qM N w * pM N w * qM N w
    let H3u := I • (A * H0m (En N w) - H0m (En N w) * A)
    let H4u := -(1 / 2 : ℂ) • (A * (A * H0m (En N w) - H0m (En N w) * A) - (A * H0m (En N w) - H0m (En N w) * A) * A)
    dE2 (En N w) 0 H3u H4u = 0 ∧ H4u 0 0 = ((27 / (8 * w ^ 2) + 19 / 8 : ℝ) : ℂ) ∧
      cubicCh (En N w) 0 H3u = ((27 / (8 * w ^ 2) + 19 / 8 : ℝ) : ℂ) ∧ (27 / (8 * w ^ 2) + 19 / 8 : ℝ) ≠ 0 ∧
      ∃ s, H3u s 0 ≠ 0 := by
  intro A H3u H4u
  have hA : Matrix.IsHermitian A := (q_herm' N).add (qpq_herm N)
  have hcol : ∀ s, A s 0 = (((3 * cq w ^ 3 : ℝ) : ℂ) + ((kq w * cq w ^ 2 : ℝ) : ℂ) * I) * ket N 1 s
      + (((Real.sqrt 6 * cq w ^ 3 : ℝ) : ℂ) + ((Real.sqrt 6 * kq w * cq w ^ 2 : ℝ) : ℂ) * I) * ket N 3 s :=
    fun s => by simp only [A]; rw [Matrix.add_apply, q3col, qpqcol]; push_cast; ring
  have hv : ((Complex.normSq (((3 * cq w ^ 3 : ℝ) : ℂ) + ((kq w * cq w ^ 2 : ℝ) : ℂ) * I) * w
      + Complex.normSq (((Real.sqrt 6 * cq w ^ 3 : ℝ) : ℂ) + ((Real.sqrt 6 * kq w * cq w ^ 2 : ℝ) : ℂ) * I)
      * (3 * w) : ℝ) : ℂ) = ((27 / (8 * w ^ 2) + 19 / 8 : ℝ) : ℂ) := by
    congr 1
    simp only [Complex.normSq_add_mul_I]
    have hk := kq_sq w hw
    rw [show (3 * cq w ^ 3) ^ 2 = 9 * cq w ^ 6 by ring,
      show (kq w * cq w ^ 2) ^ 2 = kq w ^ 2 * (cq w ^ 2) ^ 2 by ring,
      show (Real.sqrt 6 * cq w ^ 3) ^ 2 = (Real.sqrt 6 * Real.sqrt 6) * cq w ^ 6 by ring,
      show (Real.sqrt 6 * kq w * cq w ^ 2) ^ 2 = (Real.sqrt 6 * Real.sqrt 6) * kq w ^ 2 * (cq w ^ 2) ^ 2 by ring,
      s66, c6 hw, hk, cq_sq w hw]
    field_simp; ring
  have h1 := (conj_channels (En N w) 0 A hA).1
  have h2 := (conj_channels (En N w) 0 A hA).2
  rw [conj_of_col N w A _ _ hcol, hv] at h1 h2
  have hne : (27 / (8 * w ^ 2) + 19 / 8 : ℝ) ≠ 0 := by positivity
  refine ⟨conj_zero _ _ A hA, h1, h2, hne, ?_⟩
  by_contra hall
  push Not at hall
  have : cubicCh (En N w) 0 H3u = 0 := Finset.sum_eq_zero fun s _ => by simp [hall s]
  rw [h2] at this; exact hne (by exact_mod_cast this)

/-- ⛭ **`fake_receipt` (B).** For `H₃ = g₃q³` on every truncation: non-resonant; the generator solves
`i[A,H₀] = H₃`; `H₄fake = i[A,H₃]/2` has `⟨H₄fake⟩ = 11g₃²/(8w⁴)` and `dE₂(H₃, H₄fake) = 0`; and for every quartic
`dE₂(H₃, g₄q⁴) = ⟨g₄q⁴ − H₄fake⟩`. -/
theorem fake_receipt (g3 : ℝ) :
    let H3 := (g3 : ℂ) • (qM N w * qM N w * qM N w)
    let A := gen (En N w) H3
    let H4f := (I / 2) • (A * H3 - H3 * A)
    NonRes (En N w) H3 ∧ I • (A * H0m (En N w) - H0m (En N w) * A) = H3 ∧ dE2 (En N w) 0 H3 H4f = 0 ∧
      H4f 0 0 = ((11 * g3 ^ 2 / (8 * w ^ 4) : ℝ) : ℂ) ∧ (g3 ≠ 0 → H4f 0 0 ≠ 0) ∧
      ∀ g4 : ℝ, dE2 (En N w) 0 H3 ((g4 : ℂ) • (qM N w * qM N w * qM N w * qM N w))
        = ((g4 : ℂ) • (qM N w * qM N w * qM N w * qM N w)) 0 0 - H4f 0 0 := by
  intro H3 A H4f
  have hN := cubic_nonres N w hw.ne' g3
  have hH := cubic_herm N w g3
  have hv : H4f 0 0 = ((11 * g3 ^ 2 / (8 * w ^ 4) : ℝ) : ℂ) :=
    (fake_vev _ _ _ hH hN).trans (cubic_channel N hw g3)
  refine ⟨hN, gen_solves _ _ hN, fake_zero _ _ _ hH hN, hv, fun hg => ?_, fun g4 => deviation _ _ _ _ hH hN⟩
  rw [hv]; exact_mod_cast (by positivity : (11 * g3 ^ 2 / (8 * w ^ 4) : ℝ) ≠ 0)

/-- ⛭ **`locus` (B).** `dE₂ = 0` on exactly one quartic, `g₄ = 11g₃²/(6w²)`, and `∂dE₂/∂g₄ = 3/(4w²) ≠ 0`. -/
theorem locus (g3 : ℝ) :
    (∀ g4 : ℝ, dE2 (En N w) 0 ((g3 : ℂ) • (qM N w * qM N w * qM N w))
        ((g4 : ℂ) • (qM N w * qM N w * qM N w * qM N w)) = 0 ↔ g4 = 11 * g3 ^ 2 / (6 * w ^ 2)) ∧
    (∀ g4 : ℝ, HasDerivAt (fun g => closedE w g3 g) (3 / (4 * w ^ 2)) g4) ∧ (3 / (4 * w ^ 2) : ℝ) ≠ 0 := by
  refine ⟨fun g4 => ?_, fun g4 => ?_, by positivity⟩
  · rw [dE2_closed N hw, Complex.ofReal_eq_zero, closedE, div_eq_zero_iff]
    have : (8 * w ^ 4 : ℝ) ≠ 0 := by positivity
    constructor
    · rintro (h | h)
      · field_simp; linarith
      · exact absurd h this
    · intro h; left; rw [h]; field_simp; ring
  · have := ((((hasDerivAt_id g4).const_mul (6 * w ^ 2)).sub_const (11 * g3 ^ 2)).div_const (8 * w ^ 4))
    convert this using 1
    · funext g; simp [closedE]; ring
    · field_simp; ring


/-- ⛭ **`no_cancellation` (C).** Every term of the cubic channel is a non-negative numerator over a positive
denominator, for ANY `H₃`; for `g₃q³` with `g₃ ≠ 0` exactly two are non-zero (`s = 1, 3`), both positive. -/
theorem no_cancellation (g3 : ℝ) (hg : g3 ≠ 0) :
    (∀ H3 : Matrix (Fin (N + 4)) (Fin (N + 4)) ℂ, ∀ s ∈ univ.erase (0 : Fin (N + 4)),
      0 < En N w s - En N w 0 ∧ 0 ≤ cterm N w H3 s) ∧
    (∀ s : Fin (N + 4), cterm N w ((g3 : ℂ) • (qM N w * qM N w * qM N w)) s ≠ 0 ↔ s = 1 ∨ s = 3) ∧
    cterm N w ((g3 : ℂ) • (qM N w * qM N w * qM N w)) 1 = 9 * g3 ^ 2 / (8 * w ^ 4) ∧
    cterm N w ((g3 : ℂ) • (qM N w * qM N w * qM N w)) 3 = 2 * g3 ^ 2 / (8 * w ^ 4) ∧
    0 < 9 * g3 ^ 2 / (8 * w ^ 4) ∧ 0 < 2 * g3 ^ 2 / (8 * w ^ 4) := by
  have hd : ∀ s ∈ univ.erase (0 : Fin (N + 4)), 0 < En N w s - En N w 0 := fun s hs => by
    have : (s : ℕ) ≠ 0 := fun e => (Finset.mem_erase.1 hs).1 (Fin.ext (by simp [e]))
    have : (1 : ℝ) ≤ (s : ℕ) := by exact_mod_cast Nat.one_le_iff_ne_zero.2 this
    simp only [En, Fin.val_zero]; push_cast; nlinarith
  have t1 : cterm N w ((g3 : ℂ) • (qM N w * qM N w * qM N w)) 1 = 9 * g3 ^ 2 / (8 * w ^ 4) := by
    rw [cterm, q3col_real N, ket1_1, ket3_1, En_1]
    simp only [mul_one, mul_zero, add_zero, Complex.normSq_ofReal]
    rw [show g3 * 3 * cq w ^ 3 * (g3 * 3 * cq w ^ 3) = 9 * g3 ^ 2 * cq w ^ 6 by ring, c6 hw]
    field_simp
  have t3 : cterm N w ((g3 : ℂ) • (qM N w * qM N w * qM N w)) 3 = 2 * g3 ^ 2 / (8 * w ^ 4) := by
    rw [cterm, q3col_real N, ket1_3, ket3_3, En_3]
    simp only [mul_one, mul_zero, zero_add, Complex.normSq_ofReal]
    rw [show g3 * Real.sqrt 6 * cq w ^ 3 * (g3 * Real.sqrt 6 * cq w ^ 3)
      = (Real.sqrt 6 * Real.sqrt 6) * g3 ^ 2 * cq w ^ 6 by ring, s66, c6 hw]
    field_simp; ring
  have p1 : 0 < 9 * g3 ^ 2 / (8 * w ^ 4) := by positivity
  have p3 : 0 < 2 * g3 ^ 2 / (8 * w ^ 4) := by positivity
  refine ⟨fun H3 s hs => ⟨hd s hs, div_nonneg (Complex.normSq_nonneg _) (hd s hs).le⟩, fun s => ?_, t1, t3, p1, p3⟩
  constructor
  · intro h
    by_contra hc
    push Not at hc
    apply h
    have h1 : (s : ℕ) ≠ 1 := fun e => hc.1 (Fin.ext (by rw [e, fv1]))
    have h3 : (s : ℕ) ≠ 3 := fun e => hc.2 (Fin.ext (by rw [e, fv3]))
    obtain ⟨e1, e3⟩ := ket13_zero N s h1 h3
    rw [cterm, q3col_real N, e1, e3]; simp
  · rintro (rfl | rfl)
    · rw [t1]; exact p1.ne'
    · rw [t3]; exact p3.ne'

/-- ⛭ **`pure_cubic` and `even` (C).** No quartic at all: `dE₂ = −11g₃²/(8w⁴) ≠ 0`; and `dE₂` is even in `g₃`. -/
theorem pure_cubic_even (g3 g4 : ℝ) :
    dE2 (En N w) 0 ((g3 : ℂ) • (qM N w * qM N w * qM N w)) 0 = ((-11 * g3 ^ 2 / (8 * w ^ 4) : ℝ) : ℂ) ∧
    (g3 ≠ 0 → (-11 * g3 ^ 2 / (8 * w ^ 4) : ℝ) ≠ 0) ∧
    dE2 (En N w) 0 ((g3 : ℂ) • (qM N w * qM N w * qM N w)) ((g4 : ℂ) • (qM N w * qM N w * qM N w * qM N w))
      = dE2 (En N w) 0 (((-g3 : ℝ) : ℂ) • (qM N w * qM N w * qM N w))
          ((g4 : ℂ) • (qM N w * qM N w * qM N w * qM N w)) := by
  refine ⟨?_, fun hg => ?_, ?_⟩
  · rw [dE2, cubic_channel N hw]; simp only [Matrix.zero_apply, zero_sub]; push_cast; ring
  · have : 0 < g3 ^ 2 := by positivity
    have : 0 < w ^ 4 := by positivity
    intro h; field_simp at h; linarith
  · rw [dE2_closed N hw, dE2_closed N hw, closedE, closedE]; ring_nf

/-- the derivatives in `g₃` (C): `∂ = −11g₃/(4w⁴)`, `∂² = −11/(4w⁴) ≠ 0` -/
theorem g3_derivs (g3 g4 : ℝ) :
    HasDerivAt (fun g => closedE w g g4) (-11 * g3 / (4 * w ^ 4)) g3 ∧
    HasDerivAt (fun g => -11 * g / (4 * w ^ 4)) (-11 / (4 * w ^ 4)) g3 ∧ (-11 / (4 * w ^ 4) : ℝ) ≠ 0 ∧
    (-11 * 1 / (4 * w ^ 4) : ℝ) ≠ 0 := by
  have hw4 : (0 : ℝ) < w ^ 4 := by positivity
  refine ⟨?_, ?_, by positivity, by positivity⟩
  · have := (((hasDerivAt_pow 2 g3).const_mul (11 : ℝ)).const_sub (6 * g4 * w ^ 2)).div_const (8 * w ^ 4)
    convert this using 1
    · funext g; simp [closedE]
    · field_simp; ring
  · have := ((hasDerivAt_id g3).const_mul (-11 : ℝ)).div_const (4 * w ^ 4)
    convert this using 1
    · funext g; simp
    · simp

end main

/-- ⛭ **`trace_cube` (C).** For every traceless `3 × 3` matrix, `tr h³ = 3 det h`. -/
theorem trace_cube {R : Type*} [CommRing R] (h : Matrix (Fin 3) (Fin 3) R) (h0 : Matrix.trace h = 0) :
    Matrix.trace (h * h * h) = 3 * Matrix.det h := by
  rw [Matrix.trace_fin_three] at h0
  have e : h 2 2 = -h 0 0 - h 1 1 := by linear_combination h0
  simp only [Matrix.trace_fin_three, Matrix.det_fin_three, Matrix.mul_apply, Fin.sum_univ_three]
  rw [e]; ring

/-- `diag(2, −1, −1)` and `diag(1, 1, −2)`: traceless, `tr h³ = 3 det h`, `det = 2` and `−2` -/
theorem trace_cube_cases :
    Matrix.trace (Matrix.diagonal ![(2 : ℚ), -1, -1]) = 0 ∧
    Matrix.trace (Matrix.diagonal ![(2 : ℚ), -1, -1] ^ 3) = 3 * Matrix.det (Matrix.diagonal ![(2 : ℚ), -1, -1]) ∧
    Matrix.det (Matrix.diagonal ![(2 : ℚ), -1, -1]) = 2 ∧
    Matrix.trace (Matrix.diagonal ![(1 : ℚ), 1, -2]) = 0 ∧
    Matrix.trace (Matrix.diagonal ![(1 : ℚ), 1, -2] ^ 3) = 3 * Matrix.det (Matrix.diagonal ![(1 : ℚ), 1, -2]) ∧
    Matrix.det (Matrix.diagonal ![(1 : ℚ), 1, -2]) = -2 := by
  simp [Matrix.diagonal_pow, Fin.sum_univ_three, Fin.prod_univ_three]
  norm_num


/-! ### D. The bookkeeping -/

/-- the trace formula's bracket `(1 − n)L^m + m L^{m−1}` -/
noncomputable def bracket (n m L : ℝ) : ℝ := (1 - n) * L ^ m + m * L ^ (m - 1)

/-- **`bookkeeping` (D).** `j = 2k − 4`: `j = 2` admits `k = 3` and nothing else; the bracket is `1` at `(n, m) = (1, 1)`
(the `m` term) and `−2` at `(3, 0)` (the `(1 − n)` term). -/
theorem bookkeeping (L : ℝ) : (∀ k : ℝ, 2 * k - 4 = 2 ↔ k = 3) ∧ bracket 1 1 L = 1 ∧ bracket 3 0 L = -2 := by
  refine ⟨fun k => ⟨fun h => by linarith, fun h => by rw [h]; norm_num⟩, ?_, ?_⟩
  · simp [bracket]
  · simp [bracket]; norm_num


section inv
variable {F : Type*} [Field F]

abbrev T4 (F : Type*) := Fin 4 → Fin 4 → Fin 4 → Fin 4 → F

/-- `g_{ab}` from its diagonal -/
def gd (g : Fin 4 → F) (a b : Fin 4) : F := if a = b then g a else 0
def Ric (Rl : T4 F) (g : Fin 4 → F) (b d : Fin 4) : F := ∑ a, Rl a b a d / g a
def Rs (Rl : T4 F) (g : Fin 4 → F) : F := ∑ i, Ric Rl g i i / g i
def Ru (Rl : T4 F) (g : Fin 4 → F) (i j : Fin 4) : F := Ric Rl g i j / (g i * g j)
def Riem2 (Rl : T4 F) (g : Fin 4 → F) : F := ∑ a, ∑ b, ∑ c, ∑ d, Rl a b c d ^ 2 / (g a * g b * g c * g d)
def RicRic (Rl : T4 F) (g : Fin 4 → F) : F := ∑ i, ∑ j, Ric Rl g i j * Ru Rl g i j
def I3 (Rl : T4 F) (g : Fin 4 → F) : F :=
  ∑ a, ∑ b, ∑ c, (Ric Rl g a b / g a) * (Ric Rl g b c / g b) * (Ric Rl g c a / g c)
def I5 (Rl : T4 F) (g : Fin 4 → F) : F :=
  ∑ i, ∑ j, ∑ k, ∑ l, Ru Rl g i j * Ru Rl g k l * Rl i k j l
def I6 (Rl : T4 F) (g : Fin 4 → F) : F :=
  ∑ a, ∑ b, ∑ c, ∑ d, ∑ e, Ru Rl g a b / (g c * g d * g e) * Rl a c d e * Rl b c d e
def cubA (C : T4 F) (g : Fin 4 → F) : F :=
  ∑ a, ∑ b, ∑ c, ∑ d, ∑ e, ∑ f, C a b c d / (g a * g b) * (C c d e f / (g c * g d)) * (C e f a b / (g e * g f))
def cubB (C : T4 F) (g : Fin 4 → F) : F :=
  ∑ a, ∑ b, ∑ c, ∑ d, ∑ e, ∑ f, C a b c d * (C a e c f / (g a * g e * g c * g f)) * (C b e d f / (g b * g d))
def weyl (Rl : T4 F) (g : Fin 4 → F) : T4 F := fun a b c d =>
  Rl a b c d - (gd g a c * Ric Rl g b d - gd g a d * Ric Rl g b c - gd g b c * Ric Rl g a d + gd g b d * Ric Rl g a c) / 2
    + Rs Rl g * (gd g a c * gd g b d - gd g a d * gd g b c) / 6
def sq2 (C : T4 F) (g : Fin 4 → F) : F := Riem2 C g


/-- the eight algebraic dimension-six scalars, in the receipt's order -/
def eight (Rl : T4 F) (g : Fin 4 → F) : Fin 8 → F :=
  ![Rs Rl g * Rs Rl g * Rs Rl g, Rs Rl g * RicRic Rl g, I3 Rl g, Rs Rl g * Riem2 Rl g, I5 Rl g, I6 Rl g, cubA Rl g, cubB Rl g]

section scale
variable (K : F) (Rl : T4 F) (g : Fin 4 → F)
def sc : T4 F := fun a b c d => K * Rl a b c d

lemma Ric_sc (b d : Fin 4) : Ric (sc K Rl) g b d = K * Ric Rl g b d := by
  simp only [Ric, sc, Finset.mul_sum]; ring_nf
lemma Rs_sc : Rs (sc K Rl) g = K * Rs Rl g := by
  simp only [Rs, Ric_sc, Finset.mul_sum]; ring_nf
lemma Ru_sc (i j : Fin 4) : Ru (sc K Rl) g i j = K * Ru Rl g i j := by
  simp only [Ru, Ric_sc]; ring
lemma Riem2_sc : Riem2 (sc K Rl) g = K ^ 2 * Riem2 Rl g := by
  simp only [Riem2, sc, Finset.mul_sum]; ring_nf
lemma RicRic_sc : RicRic (sc K Rl) g = K ^ 2 * RicRic Rl g := by
  simp only [RicRic, Ric_sc, Ru_sc, Finset.mul_sum]; ring_nf
lemma I3_sc : I3 (sc K Rl) g = K ^ 3 * I3 Rl g := by
  simp only [I3, Ric_sc, Finset.mul_sum]; ring_nf
lemma I5_sc : I5 (sc K Rl) g = K ^ 3 * I5 Rl g := by
  simp only [I5, Ru_sc, sc, Finset.mul_sum]; ring_nf
lemma I6_sc : I6 (sc K Rl) g = K ^ 3 * I6 Rl g := by
  simp only [I6, Ru_sc, sc, Finset.mul_sum]; ring_nf
lemma cubA_sc : cubA (sc K Rl) g = K ^ 3 * cubA Rl g := by
  simp only [cubA, sc, Finset.mul_sum]; ring_nf
lemma cubB_sc : cubB (sc K Rl) g = K ^ 3 * cubB Rl g := by
  simp only [cubB, sc, Finset.mul_sum]; ring_nf
lemma weyl_sc : weyl (sc K Rl) g = sc K (weyl Rl g) := by
  funext a b c d; simp only [weyl, sc, Ric_sc, Rs_sc]; ring
lemma eight_sc (i : Fin 8) : eight (sc K Rl) g i = K ^ 3 * eight Rl g i := by
  fin_cases i <;> simp [eight, Rs_sc, RicRic_sc, Riem2_sc, I3_sc, I5_sc, I6_sc, cubA_sc, cubB_sc] <;> ring
end scale

section map
variable {F' : Type*} [Field F'] (φ : F →+* F') (Rl : T4 F) (g : Fin 4 → F)
def mp : T4 F' := fun a b c d => φ (Rl a b c d)
lemma gd_map (a b : Fin 4) : gd (fun i => φ (g i)) a b = φ (gd g a b) := by
  unfold gd; split_ifs <;> simp
lemma Ric_map (b d : Fin 4) : Ric (mp φ Rl) (fun i => φ (g i)) b d = φ (Ric Rl g b d) := by
  simp [Ric, mp, map_sum, map_div₀]
lemma Rs_map : Rs (mp φ Rl) (fun i => φ (g i)) = φ (Rs Rl g) := by simp [Rs, Ric_map, map_sum, map_div₀]
lemma Ru_map (i j : Fin 4) : Ru (mp φ Rl) (fun i => φ (g i)) i j = φ (Ru Rl g i j) := by
  simp [Ru, Ric_map, map_div₀]
lemma weyl_map : weyl (mp φ Rl) (fun i => φ (g i)) = mp φ (weyl Rl g) := by
  funext a b c d; simp [weyl, mp, Ric_map, Rs_map, gd_map, map_div₀, map_ofNat]
lemma Riem2_map : Riem2 (mp φ Rl) (fun i => φ (g i)) = φ (Riem2 Rl g) := by simp [Riem2, mp, map_sum, map_div₀]
lemma cubA_map : cubA (mp φ Rl) (fun i => φ (g i)) = φ (cubA Rl g) := by simp [cubA, mp, map_sum, map_div₀]
lemma cubB_map : cubB (mp φ Rl) (fun i => φ (g i)) = φ (cubB Rl g) := by simp [cubB, mp, map_sum, map_div₀]
lemma RicRic_map : RicRic (mp φ Rl) (fun i => φ (g i)) = φ (RicRic Rl g) := by
  simp [RicRic, Ric_map, Ru_map, map_sum]
lemma I3_map : I3 (mp φ Rl) (fun i => φ (g i)) = φ (I3 Rl g) := by simp [I3, Ric_map, map_sum, map_div₀]
lemma I5_map : I5 (mp φ Rl) (fun i => φ (g i)) = φ (I5 Rl g) := by simp [I5, Ru_map, mp, map_sum]
lemma I6_map : I6 (mp φ Rl) (fun i => φ (g i)) = φ (I6 Rl g) := by simp [I6, Ru_map, mp, map_sum, map_div₀]
lemma eight_map (i : Fin 8) : eight (mp φ Rl) (fun i => φ (g i)) i = φ (eight Rl g i) := by
  fin_cases i <;> simp [eight, Rs_map, RicRic_map, Riem2_map, I3_map, I5_map, I6_map, cubA_map, cubB_map]
end map

end inv


section FRWcopy
open Bundle Manifold Filter Set VectorField
open scoped ContDiff Manifold Topology
set_option synthInstance.maxHeartbeats 400000
variable {k m n : ℝ → ℝ} (hk : ContDiff ℝ ∞ k) (hm : ContDiff ℝ ∞ m) (hn : ContDiff ℝ ∞ n)

include hk hm hn in
lemma pr3_d1 (i j l : Fin 4) (y v : Fin 4 → ℝ) :
    fderiv ℝ (fun y : Fin 4 → ℝ => k (y i) * m (y j) * n (y l)) y v
      = deriv k (y i) * v i * m (y j) * n (y l) + k (y i) * (deriv m (y j) * v j) * n (y l)
        + k (y i) * m (y j) * (deriv n (y l) * v l) := by
  have H : HasFDerivAt (fun y : Fin 4 → ℝ => k (y i) * m (y j) * n (y l)) _ y :=
    ((fd_coord_i i ((hk.differentiable (by simp)) _)).mul (fd_coord_i j ((hm.differentiable (by simp)) _))).mul
      (fd_coord_i l ((hn.differentiable (by simp)) _))
  rw [H.fderiv]; simp; ring

include hk hm hn in
lemma pr3_d2 (i j l : Fin 4) (p u v : Fin 4 → ℝ) :
    fderiv ℝ (fderiv ℝ (fun y : Fin 4 → ℝ => k (y i) * m (y j) * n (y l))) p u v
      = deriv (deriv k) (p i) * u i * v i * m (p j) * n (p l)
        + deriv k (p i) * v i * (deriv m (p j) * u j) * n (p l)
        + deriv k (p i) * v i * m (p j) * (deriv n (p l) * u l)
        + deriv k (p i) * u i * (deriv m (p j) * v j) * n (p l)
        + k (p i) * (deriv (deriv m) (p j) * u j * v j) * n (p l)
        + k (p i) * (deriv m (p j) * v j) * (deriv n (p l) * u l)
        + deriv k (p i) * u i * m (p j) * (deriv n (p l) * v l)
        + k (p i) * (deriv m (p j) * u j) * (deriv n (p l) * v l)
        + k (p i) * m (p j) * (deriv (deriv n) (p l) * u l * v l) := by
  have D := fun {f : ℝ → ℝ} (hf : ContDiff ℝ ∞ f) (q : Fin 4) =>
    fd_coord_i (x := p) q ((hf.differentiable (by simp)) (p q))
  have D' := fun {f : ℝ → ℝ} (hf : ContDiff ℝ ∞ f) (q : Fin 4) =>
    fd_coord_i (x := p) q (((contDiff_infty_iff_deriv.1 hf).2.differentiable (by simp)) (p q))
  rw [d2_of (F := fun y : Fin 4 → ℝ => k (y i) * m (y j) * n (y l))
    (((hk.comp (contDiff_apply ℝ ℝ i)).mul (hm.comp (contDiff_apply ℝ ℝ j))).mul (hn.comp (contDiff_apply ℝ ℝ l)))
    (fun y => pr3_d1 hk hm hn i j l y v)
    (((((D' hk i).mul_const (v i)).mul (D hm j)).mul (D hn l)).add
      (((D hk i).mul ((D' hm j).mul_const (v j))).mul (D hn l)) |>.add
      (((D hk i).mul (D hm j)).mul ((D' hn l).mul_const (v l))))]
  simp; ring

noncomputable def cF (a S₁ S₂ : ℝ → ℝ) : Fin 4 → (Fin 4 → ℝ) → ℝ :=
  ![fun _ => -1, fun y => a (y 0) ^ 2, fun y => a (y 0) ^ 2 * S₁ (y 1), fun y => a (y 0) ^ 2 * S₁ (y 1) * S₂ (y 2)]

omit hk hm hn in
lemma cF_smooth {a S₁ S₂ : ℝ → ℝ} (ha : ContDiff ℝ ∞ a) (h1 : ContDiff ℝ ∞ S₁) (h2 : ContDiff ℝ ∞ S₂)
    (j : Fin 4) : ContDiff ℝ ∞ (cF a S₁ S₂ j) := by
  fin_cases j
  · exact contDiff_const
  · exact (ha.comp (contDiff_apply ℝ ℝ 0)).pow 2
  · exact ((ha.comp (contDiff_apply ℝ ℝ 0)).pow 2).mul (h1.comp (contDiff_apply ℝ ℝ 1))
  · exact (((ha.comp (contDiff_apply ℝ ℝ 0)).pow 2).mul (h1.comp (contDiff_apply ℝ ℝ 1))).mul
      (h2.comp (contDiff_apply ℝ ℝ 2))
omit hk hm hn in
lemma cF_ne {a S₁ S₂ : ℝ → ℝ} (ha0 : ∀ s, a s ≠ 0) (h10 : ∀ s, S₁ s ≠ 0) (h20 : ∀ s, S₂ s ≠ 0)
    (j : Fin 4) (p : Fin 4 → ℝ) : cF a S₁ S₂ j p ≠ 0 := by
  fin_cases j <;> simp [cF, ha0, h10, h20]


/-- THE connection's Riemann table on `cF`, symbolic in the profile data at the point: `A = a`, `A1 = a′`,
`A2 = a″`, `s = S`, `d = S′`, `d2 = S″`, `s2 = S₂`, `e = S₂′`, `e2 = S₂″`. Generated by sympy and checked case by case
below. -/
noncomputable def fRk (A A1 A2 s d d2 s2 e e2 : ℝ) : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ := ![![![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, (A2/A), 0, 0], ![(A*A2), 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, 0, (A2/A), 0], ![0, 0, 0, 0], ![(A*A2*s), 0, 0, 0], ![0, 0, 0, 0]], ![![0, 0, 0, (A2/A)], ![0, 0, 0, 0], ![0, 0, 0, 0], ![(A*A2*s*s2), 0, 0, 0]]], ![![![0, (-A2/A), 0, 0], ![(-A*A2), 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, 0, 0, 0], ![0, 0, (-(4*A1^2*s^2 + d^2 - 2*d2*s)/(4*s^2)), 0], ![0, ((4*A1^2*s^2 + d^2 - 2*d2*s)/(4*s)), 0, 0], ![0, 0, 0, 0]], ![![0, 0, 0, 0], ![0, 0, 0, (-(4*A1^2*s^2 + d^2 - 2*d2*s)/(4*s^2))], ![0, 0, 0, 0], ![0, (s2*(4*A1^2*s^2 + d^2 - 2*d2*s)/(4*s)), 0, 0]]], ![![![0, 0, (-A2/A), 0], ![0, 0, 0, 0], ![(-A*A2*s), 0, 0, 0], ![0, 0, 0, 0]], ![![0, 0, 0, 0], ![0, 0, ((4*A1^2*s^2 + d^2 - 2*d2*s)/(4*s^2)), 0], ![0, (-(4*A1^2*s^2 + d^2 - 2*d2*s)/(4*s)), 0, 0], ![0, 0, 0, 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, (-(4*A1^2*s^2*s2^2 - d^2*s2^2 + e^2*s - 2*e2*s*s2)/(4*s*s2^2))], ![0, 0, ((4*A1^2*s^2*s2^2 - d^2*s2^2 + e^2*s - 2*e2*s*s2)/(4*s*s2)), 0]]], ![![![0, 0, 0, (-A2/A)], ![0, 0, 0, 0], ![0, 0, 0, 0], ![(-A*A2*s*s2), 0, 0, 0]], ![![0, 0, 0, 0], ![0, 0, 0, ((4*A1^2*s^2 + d^2 - 2*d2*s)/(4*s^2))], ![0, 0, 0, 0], ![0, (-s2*(4*A1^2*s^2 + d^2 - 2*d2*s)/(4*s)), 0, 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, ((4*A1^2*s^2*s2^2 - d^2*s2^2 + e^2*s - 2*e2*s*s2)/(4*s*s2^2))], ![0, 0, (-(4*A1^2*s^2*s2^2 - d^2*s2^2 + e^2*s - 2*e2*s*s2)/(4*s*s2)), 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]]]]

omit hk hm hn in
set_option maxHeartbeats 0 in
/-- THE table, proved once: `R(eᵢ, eⱼ)eₖ` of the general-`k` FRW metric at `p`, in the point values of `a`,
`S₁`, `S₂` and their first two derivatives. -/
lemma frw_tab_k {a S₁ S₂ : ℝ → ℝ} (ha : ContDiff ℝ ∞ a) (h1 : ContDiff ℝ ∞ S₁) (h2 : ContDiff ℝ ∞ S₂)
    (ha0 : ∀ s, a s ≠ 0) (h10 : ∀ s, S₁ s ≠ 0) (h20 : ∀ s, S₂ s ≠ 0) (p : Fin 4 → ℝ) :
    ∀ i j k l, i < j → curvD (cF a S₁ S₂) p (Pi.single i 1) (Pi.single j 1) (Pi.single k 1) l
      = fRk (a (p 0)) (deriv a (p 0)) (deriv (deriv a) (p 0)) (S₁ (p 1)) (deriv S₁ (p 1)) (deriv (deriv S₁) (p 1))
          (S₂ (p 2)) (deriv S₂ (p 2)) (deriv (deriv S₂) (p 2)) i j k l := by
  have d0 : ∀ s, HasDerivAt a (deriv a s) s := fun s => ((ha.differentiable (by simp)) s).hasDerivAt
  have d1 : ∀ s, HasDerivAt (deriv a) (deriv (deriv a) s) s := fun s =>
    (((contDiff_infty_iff_deriv.1 ha).2.differentiable (by simp)) s).hasDerivAt
  have q1 : deriv (fun s => a s ^ 2) = fun s => 2 * a s * deriv a s :=
    funext fun s => ((d0 s).pow 2).deriv.trans (by simp)
  have q2 : deriv (deriv (fun s => a s ^ 2)) (p 0) = 2 * deriv a (p 0) ^ 2 + 2 * a (p 0) * deriv (deriv a) (p 0) := by
    rw [q1]
    have := (show HasDerivAt (fun s => 2 * a s * deriv a s) _ (p 0) from ((d0 (p 0)).const_mul 2).mul (d1 (p 0)))
    rw [this.deriv]; ring
  have hq : ContDiff ℝ ∞ (fun s => a s ^ 2) := ha.pow 2
  have hD1 : ∀ j v, fderiv ℝ (cF a S₁ S₂ j) p v = (![0, 2 * a (p 0) * deriv a (p 0) * v 0,
      2 * a (p 0) * deriv a (p 0) * v 0 * S₁ (p 1) + a (p 0) ^ 2 * (deriv S₁ (p 1) * v 1),
      2 * a (p 0) * deriv a (p 0) * v 0 * S₁ (p 1) * S₂ (p 2) + a (p 0) ^ 2 * (deriv S₁ (p 1) * v 1) * S₂ (p 2)
        + a (p 0) ^ 2 * S₁ (p 1) * (deriv S₂ (p 2) * v 2)] : Fin 4 → ℝ) j := fun j v => by
    fin_cases j
    · simp [cF]
    · show fderiv ℝ (fun y => (fun s => a s ^ 2) (y 0)) p v = _
      rw [co_d1 hq]; simp [q1]
    · show fderiv ℝ (fun y => (fun s => a s ^ 2) (y 0) * S₁ (y 1)) p v = _
      rw [pr_d1 hq h1]; simp [q1]
    · show fderiv ℝ (fun y => (fun s => a s ^ 2) (y 0) * S₁ (y 1) * S₂ (y 2)) p v = _
      rw [pr3_d1 hq h1 h2]; simp [q1]
  have hD2 : ∀ j u v, fderiv ℝ (fderiv ℝ (cF a S₁ S₂ j)) p u v = (![0,
      (2 * deriv a (p 0) ^ 2 + 2 * a (p 0) * deriv (deriv a) (p 0)) * u 0 * v 0,
      (2 * deriv a (p 0) ^ 2 + 2 * a (p 0) * deriv (deriv a) (p 0)) * u 0 * v 0 * S₁ (p 1)
        + 2 * a (p 0) * deriv a (p 0) * v 0 * (deriv S₁ (p 1) * u 1)
        + 2 * a (p 0) * deriv a (p 0) * u 0 * (deriv S₁ (p 1) * v 1)
        + a (p 0) ^ 2 * (deriv (deriv S₁) (p 1) * u 1 * v 1),
      (2 * deriv a (p 0) ^ 2 + 2 * a (p 0) * deriv (deriv a) (p 0)) * u 0 * v 0 * S₁ (p 1) * S₂ (p 2)
        + 2 * a (p 0) * deriv a (p 0) * v 0 * (deriv S₁ (p 1) * u 1) * S₂ (p 2)
        + 2 * a (p 0) * deriv a (p 0) * v 0 * S₁ (p 1) * (deriv S₂ (p 2) * u 2)
        + 2 * a (p 0) * deriv a (p 0) * u 0 * (deriv S₁ (p 1) * v 1) * S₂ (p 2)
        + a (p 0) ^ 2 * (deriv (deriv S₁) (p 1) * u 1 * v 1) * S₂ (p 2)
        + a (p 0) ^ 2 * (deriv S₁ (p 1) * v 1) * (deriv S₂ (p 2) * u 2)
        + 2 * a (p 0) * deriv a (p 0) * u 0 * S₁ (p 1) * (deriv S₂ (p 2) * v 2)
        + a (p 0) ^ 2 * (deriv S₁ (p 1) * u 1) * (deriv S₂ (p 2) * v 2)
        + a (p 0) ^ 2 * S₁ (p 1) * (deriv (deriv S₂) (p 2) * u 2 * v 2)] : Fin 4 → ℝ) j := fun j u v => by
    fin_cases j
    · simp [cF]
    · show fderiv ℝ (fderiv ℝ (fun y => (fun s => a s ^ 2) (y 0))) p u v = _
      rw [co_d2 hq]; simp [q2]
    · show fderiv ℝ (fderiv ℝ (fun y => (fun s => a s ^ 2) (y 0) * S₁ (y 1))) p u v = _
      rw [pr_d2 hq h1, q2]; simp [q1]
    · show fderiv ℝ (fderiv ℝ (fun y => (fun s => a s ^ 2) (y 0) * S₁ (y 1) * S₂ (y 2))) p u v = _
      rw [pr3_d2 hq h1 h2, q2]; simp [q1]
  have hA := ha0 (p 0); have hS1 := h10 (p 1); have hS2 := h20 (p 2)
  have hT : ∀ i j k l, i < j → curvD (cF a S₁ S₂) p (Pi.single i 1) (Pi.single j 1) (Pi.single k 1) l
      = fRk (a (p 0)) (deriv a (p 0)) (deriv (deriv a) (p 0)) (S₁ (p 1)) (deriv S₁ (p 1)) (deriv (deriv S₁) (p 1))
          (S₂ (p 2)) (deriv S₂ (p 2)) (deriv (deriv S₂) (p 2)) i j k l := by
    intro i j k l hij
    fin_cases i <;> fin_cases j <;> (try exact absurd hij (by decide)) <;> fin_cases k <;> fin_cases l <;>
      (simp only [curvD, Pi.sub_apply, Pi.add_apply, DGD, gamD, dC1, dC2, hD1, hD2]
       simp [cF, fRk, Fin.sum_univ_four]
       try field_simp
       try ring)
  exact hT

/-- Profile data at a point, for `S = sin²`, `χ²` and `sinh²` near it. -/
lemma prof_sin2 {S : ℝ → ℝ} {θ : ℝ} (eS : S =ᶠ[𝓝 θ] fun s => Real.sin s ^ 2) :
    deriv S θ ^ 2 = 4 * S θ * (1 - S θ) ∧ deriv (deriv S) θ = 2 - 4 * S θ := by
  have sd : ∀ s, HasDerivAt (fun s => Real.sin s ^ 2) (2 * Real.sin s * Real.cos s) s := fun s =>
    ((Real.hasDerivAt_sin s).pow 2).congr_deriv (by ring)
  have e3 : deriv S =ᶠ[𝓝 θ] fun s => 2 * Real.sin s * Real.cos s :=
    eS.deriv.trans (Eventually.of_forall fun s => (sd s).deriv)
  have h2 : HasDerivAt (fun s => 2 * Real.sin s * Real.cos s) _ θ :=
    ((Real.hasDerivAt_sin θ).const_mul 2).mul (Real.hasDerivAt_cos θ)
  rw [eS.deriv_eq, (sd θ).deriv, e3.deriv_eq, h2.deriv, eS.eq_of_nhds]
  have hc := Real.sin_sq_add_cos_sq θ
  constructor <;> nlinarith [hc]



set_option maxHeartbeats 0 in
/-- the algebra of maximal symmetry on the table, for `i < j`: with `a = αc`, `a′ = sh`, `a″ = c/α`,
`sh² = c² − 1` and the `sin²` profile relations, `g_l R(e_i,e_j)e_k^l = α⁻²(g_li g_kj − g_lj g_ki)` -/
lemma fRk_maxsym {α c sh s d d2 s2 e e2 : ℝ} (hα : α ≠ 0) (hc : c ≠ 0) (hs : s ≠ 0) (hs2 : s2 ≠ 0)
    (hsh : sh ^ 2 = c ^ 2 - 1) (hd : d ^ 2 = 4 * s * (1 - s)) (hd2 : d2 = 2 - 4 * s)
    (he : e ^ 2 = 4 * s2 * (1 - s2)) (he2 : e2 = 2 - 4 * s2) (i j k l : Fin 4) (hij : i < j) :
    (![-1, (α * c) ^ 2, (α * c) ^ 2 * s, (α * c) ^ 2 * s * s2] : Fin 4 → ℝ) l
        * fRk (α * c) sh (c / α) s d d2 s2 e e2 i j k l
      = 1 / α ^ 2 * (gd ![-1, (α * c) ^ 2, (α * c) ^ 2 * s, (α * c) ^ 2 * s * s2] l i
          * gd ![-1, (α * c) ^ 2, (α * c) ^ 2 * s, (α * c) ^ 2 * s * s2] k j
        - gd ![-1, (α * c) ^ 2, (α * c) ^ 2 * s, (α * c) ^ 2 * s * s2] l j
          * gd ![-1, (α * c) ^ 2, (α * c) ^ 2 * s, (α * c) ^ 2 * s * s2] k i) := by
  subst hd2 he2
  fin_cases i <;> fin_cases j <;> (try exact absurd hij (by decide)) <;> fin_cases k <;> fin_cases l <;>
    (simp [fRk, gd, hsh, hd, he]
     try field_simp
     try ring)

/-- `curvD` is antisymmetric in its first two slots -/
lemma curvD_anti (c : Fin 4 → (Fin 4 → ℝ) → ℝ) (p u v w : Fin 4 → ℝ) : curvD c p v u w = -curvD c p u v w := by
  funext k; simp only [curvD, Pi.add_apply, Pi.sub_apply, Pi.neg_apply]; ring

/-- `a = α cosh(T/α)`: `a′ = sinh(T/α)`, `a″ = cosh(T/α)/α` -/
lemma cosh_derivs {α : ℝ} (hα : α ≠ 0) (T : ℝ) :
    deriv (fun T => α * Real.cosh (T / α)) T = Real.sinh (T / α) ∧
    deriv (deriv fun T => α * Real.cosh (T / α)) T = Real.cosh (T / α) / α := by
  have d1 : ∀ T, HasDerivAt (fun T => α * Real.cosh (T / α)) (Real.sinh (T / α)) T := fun T => by
    have := ((Real.hasDerivAt_cosh (T / α)).comp T ((hasDerivAt_id T).div_const α)).const_mul α
    exact this.congr_deriv (by simp; field_simp)
  have e1 : deriv (fun T => α * Real.cosh (T / α)) = fun T => Real.sinh (T / α) := funext fun T => (d1 T).deriv
  have d2 : HasDerivAt (fun T => Real.sinh (T / α)) (Real.cosh (T / α) / α) T := by
    have := (Real.hasDerivAt_sinh (T / α)).comp T ((hasDerivAt_id T).div_const α)
    exact this.congr_deriv (by simp [div_eq_mul_inv])
  exact ⟨(d1 T).deriv, by rw [e1, d2.deriv]⟩

set_option maxHeartbeats 1000000 in
/-- ⛭ **`closed_dS` (D).** The closed de Sitter metric `−dT² + a²(dχ² + S₁ dθ² + S₁S₂ dφ²)`, `a = α cosh(T/α)`, with
`S₁ = sin²χ`, `S₂ = sin²θ` near the point (the chart's profiles taken nowhere-zero, as in `FRWk`): THE Levi-Civita
connection's curvature, computed from its Christoffel form (engine `curvD_eq`), is maximally symmetric in ALL `256`
components, `R_{lkij} = α⁻²(g_li g_kj − g_lj g_ki)`, and `R = 12/α²`. -/
theorem closed_dS {S₁ S₂ : ℝ → ℝ} {α : ℝ} (hα : α ≠ 0) (h1 : ContDiff ℝ ∞ S₁) (h2 : ContDiff ℝ ∞ S₂)
    (h10 : ∀ s, S₁ s ≠ 0) (h20 : ∀ s, S₂ s ≠ 0) (p : Fin 4 → ℝ)
    (e1 : S₁ =ᶠ[𝓝 (p 1)] fun s => Real.sin s ^ 2) (e2 : S₂ =ᶠ[𝓝 (p 2)] fun s => Real.sin s ^ 2) :
    let a := fun T => α * Real.cosh (T / α)
    have ha : ContDiff ℝ ∞ a := by fun_prop
    have ha0 : ∀ s, a s ≠ 0 := fun s => mul_ne_zero hα (Real.cosh_pos _).ne'
    let g := fun i => cF a S₁ S₂ i p
    let Rf := fun i j k => curv (lcConn (Fin 4 → ℝ) (ndOf (diag4 (cF a S₁ S₂)) (diag4_symm _)
      (fun p u h => diag4_nondeg (fun i => cF_ne ha0 h10 h20 i p) u h)
      ((diag4_smooth (cF_smooth ha h1 h2)).differentiable (by simp))))
      (fun _ => (Pi.single i 1 : Fin 4 → ℝ)) (fun _ => (Pi.single j 1 : Fin 4 → ℝ))
      (fun _ => (Pi.single k 1 : Fin 4 → ℝ)) p
    (∀ i j k l, g l * Rf i j k l = 1 / α ^ 2 * (gd g l i * gd g k j - gd g l j * gd g k i)) ∧
      scalC g Rf = 12 / α ^ 2 := by
  intro a ha ha0 g Rf
  obtain ⟨da, dda⟩ := cosh_derivs hα (p 0)
  obtain ⟨hd, hd2⟩ := prof_sin2 e1
  obtain ⟨he, he2⟩ := prof_sin2 e2
  have hc0 : Real.cosh (p 0 / α) ≠ 0 := (Real.cosh_pos _).ne'
  have hsh : Real.sinh (p 0 / α) ^ 2 = Real.cosh (p 0 / α) ^ 2 - 1 := by rw [Real.cosh_sq]; ring
  have hG : g = ![-1, (α * Real.cosh (p 0 / α)) ^ 2, (α * Real.cosh (p 0 / α)) ^ 2 * S₁ (p 1),
      (α * Real.cosh (p 0 / α)) ^ 2 * S₁ (p 1) * S₂ (p 2)] := by
    funext i; fin_cases i <;> rfl
  have hRf : ∀ i j k, Rf i j k = curvD (cF a S₁ S₂) p (Pi.single i 1) (Pi.single j 1) (Pi.single k 1) :=
    fun i j k => curvD_eq (cF_ne ha0 h10 h20) (cF_smooth ha h1 h2) p _ _ _
  have hlt : ∀ i j k l, i < j →
      g l * Rf i j k l = 1 / α ^ 2 * (gd g l i * gd g k j - gd g l j * gd g k i) := by
    intro i j k l hij
    rw [hRf, frw_tab_k ha h1 h2 ha0 h10 h20 p i j k l hij, da, dda, hG]
    exact fRk_maxsym hα hc0 (h10 _) (h20 _) hsh hd hd2 he he2 i j k l hij
  have hms : ∀ i j k l, g l * Rf i j k l = 1 / α ^ 2 * (gd g l i * gd g k j - gd g l j * gd g k i) := by
    intro i j k l
    rcases lt_trichotomy i j with h | rfl | h
    · exact hlt i j k l h
    · have hz : Rf i i k l = 0 := by
        have e := congrFun (curvD_anti (cF a S₁ S₂) p (Pi.single i 1) (Pi.single i 1) (Pi.single k 1)) l
        rw [Pi.neg_apply] at e
        rw [hRf]; linarith
      rw [hz]; ring
    · have := hlt j i k l h
      have e := congrFun (curvD_anti (cF a S₁ S₂) p (Pi.single j 1) (Pi.single i 1) (Pi.single k 1)) l
      rw [Pi.neg_apply] at e
      rw [hRf, e, ← hRf]
      linear_combination -this
  refine ⟨hms, ?_⟩
  have hgn : ∀ l, g l ≠ 0 := fun l => cF_ne ha0 h10 h20 l p
  have hv : ∀ i j k l, Rf i j k l = 1 / α ^ 2 * (gd g l i * gd g k j - gd g l j * gd g k i) / g l :=
    fun i j k l => by rw [← hms]; field_simp [hgn l]
  simp only [scalC, ricC, hv]
  rw [hG]
  have := h10 (p 1); have := h20 (p 2)
  simp [Fin.sum_univ_four, gd]
  field_simp; ring

end FRWcopy

section BI
open Filter Topology
open scoped ContDiff

/-- `Γ(a, b)ₖ` is linear in `b` -/
lemma GT_lin (q : Fin 4 → ℝ → ℝ) (s : ℝ) (a b : Fin 4 → ℝ) (k : Fin 4) :
    GT q s a b k = ∑ x, b x * GT q s a (Pi.single x 1) k := by
  fin_cases k <;> simp [GT, Fin.sum_univ_four, Pi.single_apply] <;> ring

/-- the components of `curvT`: `R^a_{bcd} = ∂_cΓ^a_{db} − ∂_dΓ^a_{cb} + Γ^x_{db}Γ^a_{cx} − Γ^x_{cb}Γ^a_{dx}`, with
`∂_c = δ_c⁰ d/dt` -/
lemma curvT_comp (q : Fin 4 → ℝ → ℝ) (s : ℝ) (a b c d : Fin 4) :
    curvT q s (Pi.single c 1) (Pi.single d 1) (Pi.single b 1) a
      = (if c = 0 then DGT q s (Pi.single d 1) (Pi.single b 1) a else 0)
        - (if d = 0 then DGT q s (Pi.single c 1) (Pi.single b 1) a else 0)
        + ∑ x, GT q s (Pi.single d 1) (Pi.single b 1) x * GT q s (Pi.single c 1) (Pi.single x 1) a
        - ∑ x, GT q s (Pi.single c 1) (Pi.single b 1) x * GT q s (Pi.single d 1) (Pi.single x 1) a := by
  simp only [curvT, Pi.add_apply, Pi.sub_apply, Pi.smul_apply, smul_eq_mul]
  rw [GT_lin q s (Pi.single c 1) (GT q s _ _), GT_lin q s (Pi.single d 1) (GT q s (Pi.single c 1) _)]
  by_cases hc : c = 0 <;> by_cases hd : d = 0 <;> simp [hc, hd]

/-- Bianchi I `diag(−1, T², T⁴, T⁶)` as time profiles -/
noncomputable def qBI : Fin 4 → ℝ → ℝ := ![fun _ => -1, fun s => s ^ 2, fun s => s ^ 4, fun s => s ^ 6]

lemma dqBI : deriv (qBI 0) = (fun _ => 0) ∧ deriv (qBI 1) = (fun s => 2 * s) ∧ deriv (qBI 2) = (fun s => 4 * s ^ 3) ∧
    deriv (qBI 3) = (fun s => 6 * s ^ 5) := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;> funext s <;> simp [qBI]

lemma ddqBI (s : ℝ) : deriv (deriv (qBI 0)) s = 0 ∧ deriv (deriv (qBI 1)) s = 2 ∧
    deriv (deriv (qBI 2)) s = 12 * s ^ 2 ∧ deriv (deriv (qBI 3)) s = 30 * s ^ 4 := by
  obtain ⟨h0, h1, h2, h3⟩ := dqBI
  rw [h0, h1, h2, h3]
  refine ⟨by simp, ?_, ?_, ?_⟩
  · simp
  · rw [deriv_const_mul _ (by fun_prop)]; simp; ring
  · rw [deriv_const_mul _ (by fun_prop)]; simp; ring

/-- `Γ^a_{bc}` of the control at `T = 1` -/
def GamQ (a b c : Fin 4) : ℚ :=
  match a.val, b.val, c.val with
  | 0, 1, 1 => 1 | 0, 2, 2 => 2 | 0, 3, 3 => 3
  | 1, 0, 1 => 1 | 1, 1, 0 => 1 | 2, 0, 2 => 2 | 2, 2, 0 => 2 | 3, 0, 3 => 3 | 3, 3, 0 => 3
  | _, _, _ => 0
/-- `∂_T Γ^a_{bc}` of the control at `T = 1` -/
def dGamQ (a b c : Fin 4) : ℚ :=
  match a.val, b.val, c.val with
  | 0, 1, 1 => 1 | 0, 2, 2 => 6 | 0, 3, 3 => 15
  | 1, 0, 1 => -1 | 1, 1, 0 => -1 | 2, 0, 2 => -2 | 2, 2, 0 => -2 | 3, 0, 3 => -3 | 3, 3, 0 => -3
  | _, _, _ => 0

set_option maxHeartbeats 1000000 in
lemma GT_bi (a b c : Fin 4) : GT qBI 1 (Pi.single b 1) (Pi.single c 1) a = (GamQ a b c : ℝ) := by
  fin_cases a <;> fin_cases b <;> fin_cases c <;>
    simp [GT, Fin.sum_univ_four, qBI, GamQ] <;> norm_num

set_option maxHeartbeats 1000000 in
lemma DGT_bi (a b c : Fin 4) : DGT qBI 1 (Pi.single b 1) (Pi.single c 1) a = (dGamQ a b c : ℝ) := by
  have e2 : deriv (fun s : ℝ => s ^ 2) = fun s => 2 * s := by funext s; simp
  have e4 : deriv (fun s : ℝ => s ^ 4) = fun s => 4 * s ^ 3 := by funext s; simp
  have e6 : deriv (fun s : ℝ => s ^ 6) = fun s => 6 * s ^ 5 := by funext s; simp
  fin_cases a <;> fin_cases b <;> fin_cases c <;>
    simp [DGT, e2, e4, e6, Fin.sum_univ_four, qBI, dGamQ] <;> norm_num

def gBQ : Fin 4 → ℚ := ![-1, 1, 1, 1]

/-- the Riemann tensor of the control at `T = 1` from the Christoffel tables, `R_{abcd} = g_aa R^a_{bcd}` -/
def RiemQ (a b c d : Fin 4) : ℚ :=
  gBQ a * ((if c = 0 then dGamQ a d b else 0) - (if d = 0 then dGamQ a c b else 0)
    + ∑ x, GamQ x d b * GamQ a c x - ∑ x, GamQ x c b * GamQ a d x)

def biQ (a b c d : Fin 4) : ℚ :=
  match a.val, b.val, c.val, d.val with
  | 0, 2, 0, 2 => -2 | 0, 2, 2, 0 => 2 | 0, 3, 0, 3 => -6 | 0, 3, 3, 0 => 6
  | 1, 2, 1, 2 => 2 | 1, 2, 2, 1 => -2 | 1, 3, 1, 3 => 3 | 1, 3, 3, 1 => -3
  | 2, 0, 0, 2 => 2 | 2, 0, 2, 0 => -2 | 2, 1, 1, 2 => -2 | 2, 1, 2, 1 => 2
  | 2, 3, 2, 3 => 6 | 2, 3, 3, 2 => -6 | 3, 0, 0, 3 => 6 | 3, 0, 3, 0 => -6
  | 3, 1, 1, 3 => -3 | 3, 1, 3, 1 => 3 | 3, 2, 2, 3 => -6 | 3, 2, 3, 2 => 6
  | _, _, _, _ => 0

theorem RiemQ_eq : ∀ a b c d, RiemQ a b c d = biQ a b c d := by decide +kernel

/-- the lowered Riemann tensor from the Christoffel engine: `R_{abcd} = g_aa (R(e_c, e_d)e_b)^a` -/
noncomputable def RlT (q : Fin 4 → ℝ → ℝ) (s : ℝ) (a b c d : Fin 4) : ℝ :=
  q a s * curvT q s (Pi.single c 1) (Pi.single d 1) (Pi.single b 1) a

theorem RlT_bi (a b c d : Fin 4) : RlT qBI 1 a b c d = (biQ a b c d : ℝ) := by
  rw [← RiemQ_eq, RlT, curvT_comp]
  simp only [GT_bi, DGT_bi]
  have hg : qBI a 1 = (gBQ a : ℝ) := by fin_cases a <;> simp [qBI, gBQ]
  rw [hg, RiemQ]
  split_ifs <;> push_cast <;> ring


set_option maxHeartbeats 1000000 in
/-- the control's scalar curvature at every `T ≠ 0`: `R = 38/T²` -/
theorem bi_scal (T : ℝ) (hT : T ≠ 0) :
    scalC (fun i => qBI i T) (fun i j k => curvT qBI T (Pi.single i 1) (Pi.single j 1) (Pi.single k 1)) = 38 / T ^ 2 := by
  have e2 : deriv (fun s : ℝ => s ^ 2) = fun s => 2 * s := by funext s; simp
  have e4 : deriv (fun s : ℝ => s ^ 4) = fun s => 4 * s ^ 3 := by funext s; simp
  have e6 : deriv (fun s : ℝ => s ^ 6) = fun s => 6 * s ^ 5 := by funext s; simp
  simp only [scalC, ricC, curvT_comp]
  simp [Fin.sum_univ_four, GT, DGT, qBI, e2, e4, e6]
  field_simp; ring

/-- ⛭ **`bi_gradient` (D).** On the control `R = 38/T²` near `T = 1`, so `dR/dT = −76 ≠ 0` there. -/
theorem bi_gradient :
    HasDerivAt (fun T => scalC (fun i => qBI i T)
      (fun i j k => curvT qBI T (Pi.single i 1) (Pi.single j 1) (Pi.single k 1))) (-76) 1 := by
  have h : HasDerivAt (fun T : ℝ => 38 / T ^ 2) (-76) 1 := by
    have := ((hasDerivAt_pow 2 (1 : ℝ)).inv (by norm_num)).const_mul (38 : ℝ)
    convert this using 1
    · funext T; simp [div_eq_mul_inv]
    · norm_num
  refine h.congr_of_eventuallyEq ?_
  filter_upwards [eventually_ne_nhds (one_ne_zero : (1 : ℝ) ≠ 0)] with T hT
  exact bi_scal T hT

/-- the control, made globally non-degenerate away from `T = 1` so that the engine's THE-connection theorem
`curv_T` applies: `T^{2k} + smoothTransition(1/2 − T)`, equal to `T^{2k}` for `T ≥ 1/2` -/
noncomputable def qBIt : Fin 4 → ℝ → ℝ :=
  ![fun _ => -1, fun s => s ^ 2 + Real.smoothTransition (1 / 2 - s), fun s => s ^ 4 + Real.smoothTransition (1 / 2 - s),
    fun s => s ^ 6 + Real.smoothTransition (1 / 2 - s)]

lemma pow_st_pos (n : ℕ) (hn : Even n) (s : ℝ) : 0 < s ^ n + Real.smoothTransition (1 / 2 - s) := by
  rcases le_or_gt (1 / 2) s with h | h
  · have : 0 < s ^ n := pow_pos (by linarith) n
    linarith [Real.smoothTransition.nonneg (1 / 2 - s)]
  · have := Real.smoothTransition.pos_of_pos (show 0 < 1 / 2 - s by linarith)
    linarith [hn.pow_nonneg s]

lemma qBIt_ne (i : Fin 4) (s : ℝ) : qBIt i s ≠ 0 := by
  fin_cases i
  · simp [qBIt]
  · exact (pow_st_pos 2 (by decide) s).ne'
  · exact (pow_st_pos 4 (by decide) s).ne'
  · exact (pow_st_pos 6 (by decide) s).ne'

lemma qBIt_smooth (i : Fin 4) : ContDiff ℝ ∞ (qBIt i) := by
  have := (Real.smoothTransition.contDiff (n := ⊤)).comp (contDiff_const.sub contDiff_id : ContDiff ℝ ∞ fun s : ℝ => 1 / 2 - s)
  fin_cases i
  · exact contDiff_const
  · exact (contDiff_id.pow 2).add this
  · exact (contDiff_id.pow 4).add this
  · exact (contDiff_id.pow 6).add this

lemma qBIt_near (i : Fin 4) : qBIt i =ᶠ[𝓝 1] qBI i := by
  filter_upwards [lt_mem_nhds (show (1 / 2 : ℝ) < 1 by norm_num)] with s hs
  fin_cases i <;> simp [qBIt, qBI] <;> linarith

lemma curvT_bit (u v w : Fin 4 → ℝ) : curvT qBIt 1 u v w = curvT qBI 1 u v w := by
  have h0 : ∀ k, qBIt k 1 = qBI k 1 := fun k => (qBIt_near k).eq_of_nhds
  have h1 : ∀ k, deriv (qBIt k) 1 = deriv (qBI k) 1 := fun k => (qBIt_near k).deriv_eq
  have h2 : ∀ k, deriv (deriv (qBIt k)) 1 = deriv (deriv (qBI k)) 1 := fun k => (qBIt_near k).deriv.deriv_eq
  have hG : GT qBIt 1 = GT qBI 1 := by funext a b k; simp only [GT, h0, h1]
  have hD : DGT qBIt 1 = DGT qBI 1 := by funext a b k; simp only [DGT, h0, h1, h2]
  simp only [curvT, hG, hD]

/-- ⛭ **`bianchi_connection` (D).** At any point with `T = 1`, THE Levi-Civita connection's curvature of the control
(engine theorem `curv_T`), lowered, is the rational table `biQ` — the input of `control`. -/
theorem bianchi_connection (p : Fin 4 → ℝ) (hp : p 0 = 1) (a b c d : Fin 4) :
    qBIt a (p 0) * curv (lcConn (Fin 4 → ℝ) (ndOf (diag4 (cT qBIt)) (diag4_symm _)
      (fun p u h => diag4_nondeg (fun i => cT_ne qBIt_ne qBIt_smooth i p) u h)
      ((diag4_smooth (cT_smooth qBIt_ne qBIt_smooth)).differentiable (by simp))))
      (fun _ => (Pi.single c 1 : Fin 4 → ℝ)) (fun _ => (Pi.single d 1 : Fin 4 → ℝ))
      (fun _ => (Pi.single b 1 : Fin 4 → ℝ)) p a = (biQ a b c d : ℝ) := by
  rw [curv_T qBIt_ne qBIt_smooth, hp, curvT_bit, (qBIt_near a).eq_of_nhds]
  exact RlT_bi a b c d


end BI

/-! ### D. The frame form and the control, evaluated -/

def etaQ : Fin 4 → ℚ := ![-1, 1, 1, 1]
/-- `R_{abcd} = η_ac η_bd − η_ad η_bc` (the maximally symmetric form at `K = 1`) -/
def msQ : T4 ℚ := fun a b c d => gd etaQ a c * gd etaQ b d - gd etaQ a d * gd etaQ b c

set_option maxRecDepth 100000 in
theorem ms_q : Rs msQ etaQ = 12 ∧ Riem2 msQ etaQ = 24 ∧ RicRic msQ etaQ = 36 ∧
    eight msQ etaQ = ![1728, 432, 108, 288, 108, 72, 48, 24] ∧ (∀ a b c d, weyl msQ etaQ a b c d = 0) := by
  decide +kernel

/-- the frame metric `η` and the frame form `K(η_ac η_bd − η_ad η_bc)` over `ℝ` -/
noncomputable def etaR : Fin 4 → ℝ := fun i => (Rat.castHom ℝ) (etaQ i)
lemma etaR_def : etaR = fun i => (Rat.castHom ℝ) (etaQ i) := rfl
noncomputable def msR (K : ℝ) : T4 ℝ := sc K (mp (Rat.castHom ℝ) msQ)

theorem msR_eq (K : ℝ) (a b c d : Fin 4) :
    msR K a b c d = K * (gd etaR a c * gd etaR b d - gd etaR a d * gd etaR b c) := by
  simp only [msR, sc, mp, msQ, map_sub, map_mul, etaR_def, gd_map]

/-- the receipt's ratios to `Λ³` -/
def want : Fin 8 → ℚ := ![64, 16, 4, 32 / 3, 4, 8 / 3, 16 / 9, 8 / 9]

/-- ⛭ **`frame_values` (D).** On the frame form at `K = Λ/3`: `R = 12K`, `Riem² = 24K²`, `Ric² = 36K²`, and the eight
dimension-six scalars are `(64, 16, 4, 32/3, 4, 8/3, 16/9, 8/9)Λ³`. -/
theorem frame_values (Λ K : ℝ) :
    Rs (msR K) etaR = 12 * K ∧ Riem2 (msR K) etaR = 24 * K ^ 2 ∧ RicRic (msR K) etaR = 36 * K ^ 2 ∧
    ∀ i, eight (msR (Λ / 3)) etaR i = (want i : ℝ) * Λ ^ 3 := by
  obtain ⟨h1, h2, h3, h4, -⟩ := ms_q
  refine ⟨?_, ?_, ?_, fun i => ?_⟩
  · rw [msR, Rs_sc, etaR_def, Rs_map, h1]; simp; ring
  · rw [msR, Riem2_sc, etaR_def, Riem2_map, h2]; simp; ring
  · rw [msR, RicRic_sc, etaR_def, RicRic_map, h3]; simp; ring
  · rw [msR, eight_sc, etaR_def, eight_map, h4]
    fin_cases i <;> simp [want] <;> ring

/-- ⛭ **`frame_weyl` (D).** On the frame form, for every `K`, every Weyl component vanishes, so `C² = 0` and both cubic
Weyl contractions `C_abcd C^ab_ef C^cdef` and `C_abcd C^aecf C^b_e^d_f` are `0`. -/
theorem frame_weyl (K : ℝ) :
    (∀ a b c d, weyl (msR K) etaR a b c d = 0) ∧ Riem2 (weyl (msR K) etaR) etaR = 0 ∧
    cubA (weyl (msR K) etaR) etaR = 0 ∧ cubB (weyl (msR K) etaR) etaR = 0 := by
  have hz : weyl (msR K) etaR = fun _ _ _ _ => 0 := by
    funext a b c d
    rw [msR, weyl_sc, etaR_def, weyl_map]; simp [sc, mp, ms_q.2.2.2.2 a b c d]
  rw [hz]; simp [Riem2, cubA, cubB]

/-- ⛭ **`eight_homogeneous` (D, E).** Each of the eight, as a function of `Λ`, has `Λ f′(Λ) = 3 f(Λ)`. -/
theorem eight_homogeneous (Λ : ℝ) (i : Fin 8) :
    HasDerivAt (fun L => eight (msR (L / 3)) etaR i) ((want i : ℝ) * (3 * Λ ^ 2)) Λ ∧
    (want i : ℝ) * (3 * Λ ^ 2) * Λ = 3 * eight (msR (Λ / 3)) etaR i := by
  simp only [(frame_values Λ 0).2.2.2, fun L => (frame_values L 0).2.2.2 i]
  refine ⟨?_, by ring⟩
  simpa using (hasDerivAt_pow 3 Λ).const_mul (want i : ℝ)

/-- the control's Riemann tensor at `T = 1`, as computed from the Christoffel tables (`RlT_bi`) -/
noncomputable def biR : T4 ℝ := mp (Rat.castHom ℝ) biQ

/-- the control's eight values -/
def ctl : Fin 8 → ℚ := ![54872, 15732, 5012, 13528, 4210, 4080, 3800, 648]

set_option maxRecDepth 100000 in
theorem bi_q : Rs biQ etaQ = 38 ∧ Riem2 (weyl biQ etaQ) etaQ = 28 / 3 ∧ cubA (weyl biQ etaQ) etaQ = 40 / 9 ∧
    cubB (weyl biQ etaQ) etaQ = 20 / 9 ∧ eight biQ etaQ = ctl := by
  decide +kernel

set_option maxRecDepth 100000 in
/-- the eight ratios `ctl/want` are pairwise distinct: eight directions, not one -/
theorem ratios_distinct : (List.ofFn fun i => ctl i / want i).Nodup := by decide +kernel

/-- ⛭ **`control` (D).** Bianchi I `diag(−1, T², T⁴, T⁶)` at `T = 1`, its Riemann tensor from the Christoffel engine
(`RlT_bi`): `C² = 28/3`, `C_abcd C^ab_ef C^cdef = 40/9 ≠ 0`, `C_abcd C^aecf C^b_e^d_f = 20/9 ≠ 0`, `R = 38`, and the eight
scalars `ctl`, not in the ratios `want`. -/
theorem control :
    let Rl := RlT qBI 1
    let g := fun i => qBI i 1
    Riem2 (weyl Rl g) g = 28 / 3 ∧ cubA (weyl Rl g) g = 40 / 9 ∧ cubB (weyl Rl g) g = 20 / 9 ∧
    (40 / 9 : ℝ) ≠ 0 ∧ (20 / 9 : ℝ) ≠ 0 ∧ Rs Rl g = 38 ∧ (∀ i, eight Rl g i = (ctl i : ℝ)) ∧
    (ctl 0 / want 0 ≠ ctl 1 / want 1) := by
  intro Rl g
  have hR : Rl = biR := funext fun a => funext fun b => funext fun c => funext fun d => RlT_bi a b c d
  have hg : g = etaR := by funext i; fin_cases i <;> simp [g, qBI, etaR, etaQ]
  obtain ⟨h1, h2, h3, h4, h5⟩ := bi_q
  rw [hR, hg, biR, etaR_def, weyl_map, Riem2_map, cubA_map, cubB_map, Rs_map, h1, h2, h3, h4]
  refine ⟨by simp, by simp, by simp, by norm_num, by norm_num, by simp, fun i => ?_, by simp [ctl, want]; norm_num⟩
  rw [eight_map, h5]; rfl

/-! ### E. Computed or fitted -/

/-- ⛭ **`derivative_test` (E).** Every ingredient — the eight ratios, `m² − 1`, `2(m² − 4)`, `6π² det h` (`= 12π²`
at `diag(2,−1,−1)`), `11/6`, and the cited `1/60` — is a constant function of the measured inputs `(Λ, ħ, G, c)`, so its
derivative in each is `0`; the affirmative control `Λ` has `∂Λ/∂Λ = 1`, `0` in the others. -/
theorem derivative_test (m : ℝ) (x : Fin 4 → ℝ) :
    (∀ v ∈ ([((want 0 : ℚ) : ℝ), ((want 1 : ℚ) : ℝ), ((want 2 : ℚ) : ℝ), ((want 3 : ℚ) : ℝ), ((want 4 : ℚ) : ℝ),
        ((want 5 : ℚ) : ℝ), ((want 6 : ℚ) : ℝ), ((want 7 : ℚ) : ℝ), m ^ 2 - 1, 2 * (m ^ 2 - 4),
        6 * Real.pi ^ 2 * 2, 11 / 6, 1 / 60] : List ℝ),
      HasFDerivAt (fun _ : Fin 4 → ℝ => v) (0 : (Fin 4 → ℝ) →L[ℝ] ℝ) x) ∧
    HasFDerivAt (fun y : Fin 4 → ℝ => y 0) (ContinuousLinearMap.proj (R := ℝ) (φ := fun _ : Fin 4 => ℝ) 0) x ∧
    (ContinuousLinearMap.proj (R := ℝ) (φ := fun _ : Fin 4 => ℝ) 0) (Pi.single 0 1) = 1 ∧
    (∀ j : Fin 4, j ≠ 0 → (ContinuousLinearMap.proj (R := ℝ) (φ := fun _ : Fin 4 => ℝ) 0) (Pi.single j 1) = 0) ∧
    (1 / 60 : ℝ) ≠ 0 := by
  refine ⟨fun v _ => hasFDerivAt_const v x, hasFDerivAt_apply 0 x, by simp, fun j hj => by simp [hj.symm],
    by norm_num⟩

/-- the second control: the gauge ratio `α/ℓ_P = √(3/Λ)/√(ħG/c³)` has non-zero `Λ`-derivative -/
theorem gauge_ratio (Λ P : ℝ) (hΛ : 0 < Λ) (hP : 0 < P) :
    HasDerivAt (fun L => Real.sqrt (3 / L) / Real.sqrt P) (-(Real.sqrt (3 / Λ) / (2 * Λ)) / Real.sqrt P) Λ ∧
    -(Real.sqrt (3 / Λ) / (2 * Λ)) / Real.sqrt P ≠ 0 := by
  have h3 : (0 : ℝ) < 3 / Λ := by positivity
  have hd : HasDerivAt (fun L => 3 / L) (-(3 / Λ ^ 2)) Λ := by
    simpa [div_eq_mul_inv] using (hasDerivAt_inv hΛ.ne').const_mul (3 : ℝ)
  refine ⟨((hd.sqrt h3.ne').div_const _).congr_deriv ?_, ?_⟩
  · have hs : Real.sqrt (3 / Λ) ≠ 0 := (Real.sqrt_pos.2 h3).ne'
    have hsq : Real.sqrt (3 / Λ) ^ 2 = 3 / Λ := Real.sq_sqrt h3.le
    rw [show (3 : ℝ) / Λ ^ 2 = Real.sqrt (3 / Λ) ^ 2 / Λ by rw [hsq]; field_simp]
    field_simp
  · have : 0 < Real.sqrt (3 / Λ) := Real.sqrt_pos.2 h3
    have : 0 < Real.sqrt P := Real.sqrt_pos.2 hP
    have : 0 < Real.sqrt (3 / Λ) / (2 * Λ) / Real.sqrt P := by positivity
    intro h; rw [neg_div] at h; linarith

/-- ⛭ **`combo_homogeneous` (E).** Any rational combination of the eight is `(Σ cᵢ wantᵢ)Λ³` and satisfies
`Λ f′ = 3f`; ħ, G, c do not enter. -/
theorem combo_homogeneous (cs : Fin 8 → ℚ) (Λ : ℝ) :
    ∑ i, (cs i : ℝ) * eight (msR (Λ / 3)) etaR i = ((∑ i, cs i * want i : ℚ) : ℝ) * Λ ^ 3 ∧
    HasDerivAt (fun L => ∑ i, (cs i : ℝ) * eight (msR (L / 3)) etaR i)
      (((∑ i, cs i * want i : ℚ) : ℝ) * (3 * Λ ^ 2)) Λ := by
  have hv : ∀ L : ℝ, ∑ i, (cs i : ℝ) * eight (msR (L / 3)) etaR i = ((∑ i, cs i * want i : ℚ) : ℝ) * L ^ 3 := by
    intro L; simp only [(frame_values L 0).2.2.2]; push_cast; rw [Finset.sum_mul]
    exact Finset.sum_congr rfl fun i _ => by ring
  refine ⟨hv Λ, ?_⟩
  simp only [hv]
  simpa using (hasDerivAt_pow 3 Λ).const_mul ((∑ i, cs i * want i : ℚ) : ℝ)

/-! ### F. The scope -/

/-- A matrix that factors through `k` columns and has a nonzero `k × k` minor has rank exactly `k`
(copied from `Row64Descent.lean`). -/
theorem rank_eq_of_factor {m n k : ℕ} (V : Matrix (Fin m) (Fin n) ℝ) (E : Matrix (Fin m) (Fin k) ℝ)
    (C : Matrix (Fin k) (Fin n) ℝ) (hVEC : V = E * C) (r : Fin k → Fin m) (c : Fin k → Fin n)
    (hminor : (V.submatrix r c).det ≠ 0) : V.rank = k := by
  apply le_antisymm
  · rw [hVEC]; exact (Matrix.rank_mul_le_right E C).trans (Matrix.rank_le_height C)
  · have h := Matrix.rank_of_det_ne_zero hminor
    rw [Fintype.card_fin] at h
    rw [← h]; exact Matrix.rank_submatrix_le V r c

/-- ⛭ **`ranks` (F).** The eight values on the background have rank `1`; adjoining the control's raises it to `2`. -/
theorem ranks :
    (Matrix.of fun (_ : Fin 1) j => (want j : ℝ)).rank = 1 ∧
    (Matrix.of ![fun j => (want j : ℝ), fun j => (ctl j : ℝ)]).rank = 2 := by
  constructor
  · refine rank_eq_of_factor _ 1 _ (Matrix.one_mul _).symm id ![0] ?_
    simp [want]
  · refine rank_eq_of_factor _ 1 _ (Matrix.one_mul _).symm id ![0, 1] ?_
    rw [Matrix.det_fin_two]; simp [want, ctl]; norm_num

open Filter Topology in
/-- ⛭ **`residue_scheme` (F).** `H_M − log M → γ` and `H_M − log 2M → γ − log 2`: one log coefficient, finite parts
differing by `log 2 ≠ 0`, a cutoff-independent constant. -/
theorem residue_scheme :
    Tendsto (fun M : ℕ => (harmonic M : ℝ) - Real.log M) atTop (𝓝 Real.eulerMascheroniConstant) ∧
    Tendsto (fun M : ℕ => (harmonic M : ℝ) - Real.log (2 * M)) atTop
      (𝓝 (Real.eulerMascheroniConstant - Real.log 2)) ∧
    Real.eulerMascheroniConstant - (Real.eulerMascheroniConstant - Real.log 2) = Real.log 2 ∧ Real.log 2 ≠ 0 := by
  refine ⟨Real.tendsto_harmonic_sub_log, ?_, by ring, (Real.log_pos (by norm_num)).ne'⟩
  refine (Real.tendsto_harmonic_sub_log.sub_const (Real.log 2)).congr' ?_
  filter_upwards [eventually_ge_atTop 1] with M hM
  have : (M : ℝ) ≠ 0 := by exact_mod_cast (show M ≠ 0 by omega)
  rw [Real.log_mul (by norm_num) this]; ring

/-- the cited `r6990` bound, carried exactly: `(3/10¹²²)/3 = 10⁻¹²² < 10⁻¹²¹` -/
theorem cited_bound : (3 / 10 ^ 122 : ℚ) / 3 = 1 / 10 ^ 122 ∧ (1 / 10 ^ 122 : ℚ) < 1 / 10 ^ 121 := by
  norm_num

/-- ⛭ **`any_target` (F).** For every target there is exactly one quartic returning it,
`g₄ = (11g₃² + 8w⁴·target)/(6w²)`, moving with the target: the identity constrains the size not at all. -/
theorem any_target {w : ℝ} (hw : 0 < w) (g3 t : ℝ) :
    (∀ g4, closedE w g3 g4 = t ↔ g4 = (11 * g3 ^ 2 + 8 * w ^ 4 * t) / (6 * w ^ 2)) ∧
    HasDerivAt (fun t => (11 * g3 ^ 2 + 8 * w ^ 4 * t) / (6 * w ^ 2)) (8 * w ^ 4 / (6 * w ^ 2)) t ∧
    (8 * w ^ 4 / (6 * w ^ 2) : ℝ) ≠ 0 := by
  have hw2 : (0 : ℝ) < w ^ 2 := by positivity
  refine ⟨fun g4 => ?_, ?_, by positivity⟩
  · rw [closedE]
    constructor
    · intro h; field_simp at h ⊢; linarith
    · intro h; rw [h]; field_simp; ring
  · have := (((hasDerivAt_id t).const_mul (8 * w ^ 4)).const_add (11 * g3 ^ 2)).div_const (6 * w ^ 2)
    simpa using this

end R70Quartic
end ShadowProbe

#print axioms ShadowProbe.R70Quartic.conj_zero
#print axioms ShadowProbe.R70Quartic.gen_solves
#print axioms ShadowProbe.R70Quartic.fake_vev
#print axioms ShadowProbe.R70Quartic.fake_zero
#print axioms ShadowProbe.R70Quartic.deviation
#print axioms ShadowProbe.R70Quartic.cubic_nonres
#print axioms ShadowProbe.R70Quartic.cubic_channel
#print axioms ShadowProbe.R70Quartic.dE2_closed
#print axioms ShadowProbe.R70Quartic.dE2_receipt_sizes
#print axioms ShadowProbe.R70Quartic.conj_q3
#print axioms ShadowProbe.R70Quartic.conj_q3qpq
#print axioms ShadowProbe.R70Quartic.fake_receipt
#print axioms ShadowProbe.R70Quartic.locus
#print axioms ShadowProbe.R70Quartic.no_cancellation
#print axioms ShadowProbe.R70Quartic.pure_cubic_even
#print axioms ShadowProbe.R70Quartic.g3_derivs
#print axioms ShadowProbe.R70Quartic.trace_cube
#print axioms ShadowProbe.R70Quartic.trace_cube_cases
#print axioms ShadowProbe.R70Quartic.bookkeeping
#print axioms ShadowProbe.R70Quartic.frw_tab_k
#print axioms ShadowProbe.R70Quartic.fRk_maxsym
#print axioms ShadowProbe.R70Quartic.closed_dS
#print axioms ShadowProbe.R70Quartic.ms_q
#print axioms ShadowProbe.R70Quartic.frame_values
#print axioms ShadowProbe.R70Quartic.frame_weyl
#print axioms ShadowProbe.R70Quartic.eight_homogeneous
#print axioms ShadowProbe.R70Quartic.RiemQ_eq
#print axioms ShadowProbe.R70Quartic.RlT_bi
#print axioms ShadowProbe.R70Quartic.bianchi_connection
#print axioms ShadowProbe.R70Quartic.bi_scal
#print axioms ShadowProbe.R70Quartic.bi_gradient
#print axioms ShadowProbe.R70Quartic.bi_q
#print axioms ShadowProbe.R70Quartic.control
#print axioms ShadowProbe.R70Quartic.ratios_distinct
#print axioms ShadowProbe.R70Quartic.derivative_test
#print axioms ShadowProbe.R70Quartic.gauge_ratio
#print axioms ShadowProbe.R70Quartic.combo_homogeneous
#print axioms ShadowProbe.R70Quartic.ranks
#print axioms ShadowProbe.R70Quartic.residue_scheme
#print axioms ShadowProbe.R70Quartic.cited_bound
#print axioms ShadowProbe.R70Quartic.any_target

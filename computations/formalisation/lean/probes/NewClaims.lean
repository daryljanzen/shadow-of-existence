import Mathlib

/-!
# Campaign 144: the claims the papers have gained since the closing table (C1–C14)

Registration: `computations/formalisation/r7827_71_campaign144/PREDICTION.md` (order 69's `r7827`). Mathlib only;
nothing imports this file, and it imports no other probe. Every name has the prefix `nc_`. No option is set.

* C1  `nc_sixteen` — P14 l.892 (Y2): `3·2·2 + 1·2·2 = 16 = dim(4,2,1) + dim(4̄,1,2)`.
* C2  `nc_LambdaYM_lt` — P14 l.368 (Y1): `μ e^{−1/2b₀g²} < μ` for every `g² > 0`.
* C3  `nc_f_parity`, `nc_f_diff` — P14 l.896 (Y4): `f(−r;M) = f(r;−M)` and `f(−r;M) − f(r;M) = 4M/r`.
* C4  `nc_r2_signs` — P15 l.594–595: `r² − 1` at `0.9918` and `1.0926`, their signs, values and ratio.
* C5  `nc_characters` — P14 l.896 (Y4): `(t, r) ↦ (t, −r)` keeps the four characters, not the SM's.
* C6  `nc_signature_scale`, `nc_signature_number` — P15 l.580–582: only `ℓ_D/√α` enters; `1951.9/√1.7 ≈ 1497.04`.
* C7  `nc_charges` — P14 l.892 (Y2), SYN l.3077 (Y8): the `B−L` charge table.
* C8  `nc_anomalies` — P14 l.607/610, SYN l.2802: the six anomaly sums vanish; `ν^c` adds nothing.
* C9  `nc_nariai_max` — P14 l.898 (Y7): `max_{x>0} x(1 − x²) = 2/(3√3)`, only at `x = 1/√3`.
* C10 `nc_dirac` — P14 l.894 (Y4): `γ¹γ²γ³` flips a scalar mass and keeps a pseudoscalar; `γ⁵γ¹γ²γ³ = i γ⁰`.
* C11 `nc_reflections` — P14 l.368: `det P = det T = −1`, `det R = det PT = 1`.
* C12 `nc_selfdual_swap` — P14 l.894 (Y3): the layer's reflection exchanges self-dual and anti-self-dual.
* C13 `nc_det_real` — P14 l.894/898 (Y3, Y6): the zero-block quark mass determinant is real.
* C14 `nc_four` — SYN l.2804: a closed set containing a left doublet has at least four states, and four suffice.
-/

open Matrix Real

namespace ShadowProbe.NewClaimsProbe

/-! ## C1: the sixteen -/

/-- **C1.** A generation as `3×2×2` coloured and `1×2×2` colourless states is sixteen, which is also
`dim (4,2,1) + dim (4̄,1,2)`. -/
theorem nc_sixteen : 3 * 2 * 2 + 1 * 2 * 2 = 16 ∧ 4 * 2 * 1 + 4 * 1 * 2 = 16 := by norm_num

/-! ## C2: the one-loop scale lies below `μ` -/

/-- **C2.** For `μ, b₀ > 0` and every `g² > 0`, `Λ = μ e^{−1/(2 b₀ g²)} < μ`. -/
theorem nc_LambdaYM_lt {μ b₀ g2 : ℝ} (hμ : 0 < μ) (hb : 0 < b₀) (hg : 0 < g2) :
    μ * Real.exp (-1 / (2 * b₀ * g2)) < μ := by
  have h1 : -1 / (2 * b₀ * g2) < 0 := div_neg_of_neg_of_pos (by norm_num) (by positivity)
  have h2 : Real.exp (-1 / (2 * b₀ * g2)) < 1 := Real.exp_lt_one_iff.2 h1
  nlinarith

/-! ## C3: the parity on the slicing function -/

/-- The slicing function `f(r; M) = 1 − 2M/r − r²/α²`. -/
noncomputable def nc_f (α M r : ℝ) : ℝ := 1 - 2 * M / r - r ^ 2 / α ^ 2

/-- **C3.** `f(−r; M) = f(r; −M)`. -/
theorem nc_f_parity (α M r : ℝ) : nc_f α M (-r) = nc_f α (-M) r := by
  unfold nc_f; rw [div_neg]; ring

/-- **C3.** `f(−r; M) − f(r; M) = 4M/r`, which vanishes only on the de Sitter member `M = 0`. -/
theorem nc_f_diff (α M r : ℝ) (hr : r ≠ 0) :
    nc_f α M (-r) - nc_f α M r = 4 * M / r ∧ (nc_f α M (-r) = nc_f α M r ↔ M = 0) := by
  have h : nc_f α M (-r) - nc_f α M r = 4 * M / r := by
    unfold nc_f; field_simp; ring
  refine ⟨h, ⟨fun he => ?_, fun hM => ?_⟩⟩
  · have : 4 * M / r = 0 := by rw [← h, he, sub_self]
    rcases div_eq_zero_iff.1 this with h' | h'
    · linarith
    · exact absurd h' hr
  · rw [hM] at h ⊢
    have := h; simp at this; linarith

/-! ## C4: `r² − 1` at the two endpoints -/

/-- **C4.** At the adjudicated endpoint `r = 0.9918`, `r² − 1 = −0.01633276`; at `1.0926`, `0.19377476`.
They have opposite signs, they print as `−0.0163` and `+0.1938`, and the second is one part in `11.9`
of the first in size. -/
theorem nc_r2_signs :
    (0.9918 : ℝ) ^ 2 - 1 = -0.01633276 ∧ (1.0926 : ℝ) ^ 2 - 1 = 0.19377476 ∧
    (0.9918 : ℝ) ^ 2 - 1 < 0 ∧ 0 < (1.0926 : ℝ) ^ 2 - 1 ∧
    |((0.9918 : ℝ) ^ 2 - 1) - (-0.0163)| < 0.00005 ∧ |((1.0926 : ℝ) ^ 2 - 1) - 0.1938| < 0.00005 ∧
    11.85 < ((1.0926 : ℝ) ^ 2 - 1) / (1 - (0.9918 : ℝ) ^ 2) ∧
    ((1.0926 : ℝ) ^ 2 - 1) / (1 - (0.9918 : ℝ) ^ 2) < 11.95 := by
  refine ⟨by norm_num, by norm_num, by norm_num, by norm_num, ?_, ?_, ?_, ?_⟩
  · rw [abs_lt]; constructor <;> norm_num
  · rw [abs_lt]; constructor <;> norm_num
  · rw [lt_div_iff₀ (by norm_num)]; norm_num
  · rw [div_lt_iff₀ (by norm_num)]; norm_num

/-! ## C5: the `(T, R)` characters under `P` -/

/-- `P` on a `(T, R)` character. -/
def nc_P (c : ℤ × ℤ) : ℤ × ℤ := (c.1, -c.2)

/-- The four characters. -/
def nc_all : Finset (ℤ × ℤ) := {(1, 1), (1, -1), (-1, 1), (-1, -1)}

/-- The Standard Model's colourless occupation: `T ∈ {+1, −1}` on one chirality (`R = +1`) and
`T ∈ {+1, +1}` on the other (`R = −1`). -/
def nc_SM : Finset (ℤ × ℤ) := {(1, 1), (-1, 1), (1, -1)}

/-- **C5.** `P` carries the four characters onto themselves, and sends the Standard Model's to a
character it lacks. -/
theorem nc_characters :
    nc_all.image nc_P = nc_all ∧ (-1, -1) ∈ nc_SM.image nc_P ∧ (-1, -1) ∉ nc_SM := by
  refine ⟨by decide, by decide, by decide⟩

/-! ## C6: the damping signature's one scale -/

/-- **C6.** `α` and `ℓ_D` enter `exp[−α (ℓ/ℓ_D)² (r² − 1)]` only through `ℓ_D/√α`. -/
theorem nc_signature_scale {α ℓD : ℝ} (hα : 0 < α) (hℓ : 0 < ℓD) (ℓ r : ℝ) :
    Real.exp (-α * (ℓ / ℓD) ^ 2 * (r ^ 2 - 1)) =
      Real.exp (-(ℓ / (ℓD / Real.sqrt α)) ^ 2 * (r ^ 2 - 1)) := by
  congr 1
  have hs : Real.sqrt α ^ 2 = α := Real.sq_sqrt hα.le
  have hs0 : Real.sqrt α ≠ 0 := (Real.sqrt_pos.2 hα).ne'
  rw [div_div_eq_mul_div, div_pow, div_pow, mul_pow, hs]
  field_simp

/-- **C6.** `ℓ_D = 1951.9` at `α = 1.70` is the exponent-one form at `ℓ_D = 1497.04`, to `0.005`. -/
theorem nc_signature_number : |1951.9 / Real.sqrt 1.7 - 1497.04| < 0.005 := by
  have hlo : (1.30384 : ℝ) < Real.sqrt 1.7 := by
    rw [Real.lt_sqrt (by norm_num)]; norm_num
  have hhi : Real.sqrt 1.7 < 1.303841 := by
    rw [Real.sqrt_lt' (by norm_num)]; norm_num
  have hpos : (0 : ℝ) < Real.sqrt 1.7 := by linarith
  rw [abs_lt]
  constructor
  · rw [lt_sub_iff_add_lt, lt_div_iff₀ hpos]; nlinarith
  · rw [sub_lt_iff_lt_add, div_lt_iff₀ hpos]; nlinarith

/-! ## C7: the charge table -/

/-- A Weyl state of a generation: `T` (the entry of `diag(1,1,1,−3)`: `1` for a quark, `−3` for a
lepton), `I₃L`, `I₃R`, and the Standard Model charge `Q` and hypercharge `Y` (with `Q = I₃L + Y/2`). -/
structure St where
  T : ℚ
  I3L : ℚ
  I3R : ℚ
  Q : ℚ
  Y : ℚ

/-- The sixteen states: `u_L, d_L` (three colours each), `ν_L, e_L`, `u_R, d_R` (three colours each),
`ν_R, e_R`. -/
def nc_gen : List St :=
  List.replicate 3 ⟨1, 1/2, 0, 2/3, 1/3⟩ ++ List.replicate 3 ⟨1, -1/2, 0, -1/3, 1/3⟩ ++
  [⟨-3, 1/2, 0, 0, -1⟩, ⟨-3, -1/2, 0, -1, -1⟩] ++
  List.replicate 3 ⟨1, 0, 1/2, 2/3, 4/3⟩ ++ List.replicate 3 ⟨1, 0, -1/2, -1/3, -2/3⟩ ++
  [⟨-3, 0, 1/2, 0, 0⟩, ⟨-3, 0, -1/2, -1, -2⟩]

/-- `B − L = T/3`. -/
def St.BL (s : St) : ℚ := s.T / 3

/-- **C7.** The generation has sixteen states; `diag(1,1,1,−3)` is traceless on each `SU(4)` multiplet;
with `B − L = T/3` and `c = 1/2`, `Q = I₃L + I₃R + (B−L)/2` returns every Standard Model charge; with the
right-handed doublet split by `I₃R`, `Y = 2(I₃R + (B−L)/2)` returns every hypercharge; and `ν_R` has
`Q = Y = 0` but `B − L = −1` and `I₃R = 1/2`, so it couples to the right-handed `W`. -/
theorem nc_charges :
    nc_gen.length = 16 ∧ (1 + 1 + 1 + (-3) : ℚ) = 0 ∧
    (∀ s ∈ nc_gen, s.Q = s.I3L + s.I3R + s.BL / 2) ∧
    (∀ s ∈ nc_gen, s.Y = 2 * (s.I3R + s.BL / 2)) ∧
    (∀ s ∈ nc_gen, s.Q = s.I3L + s.Y / 2) ∧
    (⟨-3, 0, 1/2, 0, 0⟩ : St) ∈ nc_gen ∧ (⟨-3, 0, 1/2, 0, 0⟩ : St).BL = -1 := by
  refine ⟨rfl, by norm_num, ?_, ?_, ?_, by simp [nc_gen], by norm_num [St.BL]⟩ <;>
  · intro s hs
    simp only [nc_gen, List.mem_append, List.mem_replicate, List.mem_cons, List.mem_nil_iff,
      or_false] at hs
    rcases hs with ((((⟨-, rfl⟩ | ⟨-, rfl⟩) | (rfl | rfl)) | ⟨-, rfl⟩) | ⟨-, rfl⟩) | (rfl | rfl) <;>
      norm_num [St.BL]

/-! ## C8: the anomaly sums -/

/-- A left-handed Weyl multiplet: colour (`1` triplet, `−1` antitriplet, `0` singlet), colour dimension,
`SU(2)` dimension, hypercharge (`Q = I₃ + Y`). -/
structure Wm where
  col : ℤ
  dc : ℚ
  d2 : ℚ
  Y : ℚ

/-- One generation as left-handed multiplets: `Q (3,2,1/6)`, `u^c (3̄,1,−2/3)`, `d^c (3̄,1,1/3)`,
`L (1,2,−1/2)`, `e^c (1,1,1)`. -/
def nc_SMgen : List Wm := [⟨1, 3, 2, 1/6⟩, ⟨-1, 3, 1, -2/3⟩, ⟨-1, 3, 1, 1/3⟩, ⟨0, 1, 2, -1/2⟩, ⟨0, 1, 1, 1⟩]

/-- The right-handed neutrino's conjugate `ν^c (1,1,0)`. -/
def nc_nuc : Wm := ⟨0, 1, 1, 0⟩

/-- `SU(3)²Y`, `SU(2)²Y`, gravitational `Y`, `Y³`, `SU(3)³`, and the number of `SU(2)` doublets. -/
def nc_A33Y (g : List Wm) : ℚ := (g.filter (fun w => w.col ≠ 0)).foldr (fun w a => w.d2 * w.Y + a) 0
def nc_A22Y (g : List Wm) : ℚ := (g.filter (fun w => w.d2 = 2)).foldr (fun w a => w.dc * w.Y + a) 0
def nc_AgY (g : List Wm) : ℚ := g.foldr (fun w a => w.dc * w.d2 * w.Y + a) 0
def nc_AY3 (g : List Wm) : ℚ := g.foldr (fun w a => w.dc * w.d2 * w.Y ^ 3 + a) 0
def nc_A333 (g : List Wm) : ℚ := g.foldr (fun w a => (w.col : ℚ) * w.d2 + a) 0
def nc_Ndoub (g : List Wm) : ℚ := (g.filter (fun w => w.d2 = 2)).foldr (fun w a => w.dc + a) 0

/-- **C8.** Every per-generation anomaly sum of the Standard Model vanishes, the number of doublets is
even (no Witten anomaly), and adding the singlet `ν^c` changes none of them. -/
theorem nc_anomalies :
    nc_A33Y nc_SMgen = 0 ∧ nc_A22Y nc_SMgen = 0 ∧ nc_AgY nc_SMgen = 0 ∧ nc_AY3 nc_SMgen = 0 ∧
    nc_A333 nc_SMgen = 0 ∧ nc_Ndoub nc_SMgen = 4 ∧
    nc_A33Y (nc_SMgen ++ [nc_nuc]) = 0 ∧ nc_A22Y (nc_SMgen ++ [nc_nuc]) = 0 ∧
    nc_AgY (nc_SMgen ++ [nc_nuc]) = 0 ∧ nc_AY3 (nc_SMgen ++ [nc_nuc]) = 0 ∧
    nc_A333 (nc_SMgen ++ [nc_nuc]) = 0 ∧ nc_Ndoub (nc_SMgen ++ [nc_nuc]) = 4 := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;>
    norm_num [nc_A33Y, nc_A22Y, nc_AgY, nc_AY3, nc_A333, nc_Ndoub, nc_SMgen, nc_nuc,
      List.filter_cons]

/-! ## C9: the largest value of the order parameter -/

/-- **C9.** For `x > 0`, `x(1 − x²) ≤ 2/(3√3)`, with equality only at `x = 1/√3`. -/
theorem nc_nariai_max :
    (∀ x : ℝ, 0 < x → x * (1 - x ^ 2) ≤ 2 / (3 * Real.sqrt 3)) ∧
    (1 / Real.sqrt 3) * (1 - (1 / Real.sqrt 3) ^ 2) = 2 / (3 * Real.sqrt 3) ∧
    (∀ x : ℝ, 0 < x → x * (1 - x ^ 2) = 2 / (3 * Real.sqrt 3) → x = 1 / Real.sqrt 3) := by
  set s := Real.sqrt 3 with hsdef
  have hs : s ^ 2 = 3 := Real.sq_sqrt (by norm_num)
  have hs0 : 0 < s := Real.sqrt_pos.2 (by norm_num)
  have e1 : 2 / (3 * s) = 2 * s / 9 := by field_simp; nlinarith
  have e2 : 1 / s = s / 3 := by field_simp; nlinarith
  have key : ∀ x : ℝ, 2 * s / 9 - x * (1 - x ^ 2) = (x - s / 3) ^ 2 * (x + 2 * s / 3) := by
    intro x; linear_combination (x / 3 - 2 * s / 27) * hs
  refine ⟨fun x hx => ?_, ?_, fun x hx he => ?_⟩
  · rw [e1]
    have := key x
    have : 0 ≤ (x - s / 3) ^ 2 * (x + 2 * s / 3) := by positivity
    linarith
  · rw [e1, e2]
    have := key (s / 3); simp at this; linarith
  · rw [e1] at he
    rw [e2]
    have h0 : (x - s / 3) ^ 2 * (x + 2 * s / 3) = 0 := by rw [← key x, he, sub_self]
    rcases mul_eq_zero.1 h0 with h | h
    · nlinarith [pow_eq_zero_iff (n := 2) (two_ne_zero) |>.1 h]
    · nlinarith

/-! ## C10: the Dirac parities -/

section Dirac
open Complex

/-- Dirac basis over `ℂ`: `γ⁰ = diag(1,1,−1,−1)`, `γᵏ = [[0, σₖ], [−σₖ, 0]]`; `Gam` is `Γ = γ¹γ²γ³` written
out, and `g5` is `γ⁵ = iγ⁰γ¹γ²γ³` written out (each identified with its product below). -/
def g0 : Matrix (Fin 4) (Fin 4) ℂ := !![1, 0, 0, 0; 0, 1, 0, 0; 0, 0, -1, 0; 0, 0, 0, -1]
def g1 : Matrix (Fin 4) (Fin 4) ℂ := !![0, 0, 0, 1; 0, 0, 1, 0; 0, -1, 0, 0; -1, 0, 0, 0]
def g2 : Matrix (Fin 4) (Fin 4) ℂ := !![0, 0, 0, -I; 0, 0, I, 0; 0, I, 0, 0; -I, 0, 0, 0]
def g3 : Matrix (Fin 4) (Fin 4) ℂ := !![0, 0, 1, 0; 0, 0, 0, -1; -1, 0, 0, 0; 0, 1, 0, 0]
def Gam : Matrix (Fin 4) (Fin 4) ℂ := !![0, 0, -I, 0; 0, 0, 0, -I; I, 0, 0, 0; 0, I, 0, 0]
def g5 : Matrix (Fin 4) (Fin 4) ℂ := !![0, 0, 1, 0; 0, 0, 0, 1; 1, 0, 0, 0; 0, 1, 0, 0]
theorem nc_dirac_0 : g1 * g2 * g3 = Gam := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [g1, g2, g3, Gam, Matrix.mul_apply, Fin.sum_univ_four]
theorem nc_dirac_1 : I • (g0 * g1 * g2 * g3) = g5 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [g0, g1, g2, g3, g5]
theorem nc_dirac_2 : g0 * g0 = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [g0, Matrix.mul_apply, Fin.sum_univ_four]
theorem nc_dirac_3 : g1 * g1 = -1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [g1, Matrix.mul_apply, Fin.sum_univ_four]
theorem nc_dirac_4 : g2 * g2 = -1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [g2, Matrix.mul_apply, Fin.sum_univ_four]
theorem nc_dirac_5 : g3 * g3 = -1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [g3, Matrix.mul_apply, Fin.sum_univ_four]
theorem nc_dirac_6 : g0 * g1 = -(g1 * g0) := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [g0, g1, Matrix.mul_apply, Fin.sum_univ_four]
theorem nc_dirac_7 : g0 * g2 = -(g2 * g0) := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [g0, g2, Matrix.mul_apply, Fin.sum_univ_four]
theorem nc_dirac_8 : g0 * g3 = -(g3 * g0) := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [g0, g3, Matrix.mul_apply, Fin.sum_univ_four]
theorem nc_dirac_9 : g1 * g2 = -(g2 * g1) := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [g1, g2, Matrix.mul_apply, Fin.sum_univ_four]
theorem nc_dirac_10 : g1 * g3 = -(g3 * g1) := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [g1, g3, Matrix.mul_apply, Fin.sum_univ_four]
theorem nc_dirac_11 : g2 * g3 = -(g3 * g2) := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [g2, g3, Matrix.mul_apply, Fin.sum_univ_four]
theorem nc_dirac_12 : Gamᴴ = Gam := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Gam, Matrix.conjTranspose_apply]
theorem nc_dirac_13 : Gam * Gam = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Gam, Matrix.mul_apply, Fin.sum_univ_four]
theorem nc_dirac_14 : Gamᴴ * g0 * Gam = -g0 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [g0, Gam, Matrix.mul_apply, Fin.sum_univ_four, Matrix.conjTranspose_apply]
theorem nc_dirac_15 : Gamᴴ * (g0 * g5) * Gam = g0 * g5 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [g0, g5, Gam, Matrix.mul_apply, Fin.sum_univ_four, Matrix.conjTranspose_apply]
theorem nc_dirac_16 : g5 * Gam = I • g0 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [g0, g5, Gam, Matrix.mul_apply, Fin.sum_univ_four]
theorem nc_dirac_17 : g0ᴴ * g0 * g0 = g0 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [g0, Matrix.mul_apply, Fin.sum_univ_four, Matrix.conjTranspose_apply]
theorem nc_dirac_18 : g0ᴴ * (g0 * g5) * g0 = -(g0 * g5) := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [g0, g5, Matrix.mul_apply, Fin.sum_univ_four, Matrix.conjTranspose_apply]

/-- **C10.** `Γ = γ¹γ²γ³` and `γ⁵ = iγ⁰γ¹γ²γ³`, with the Clifford relations (`γ⁰² = 1`, `γᵏ² = −1`,
anticommuting). `Γ` is Hermitian and squares to `1`; it reverses a scalar mass, `Γᴴγ⁰Γ = −γ⁰`, and keeps a
pseudoscalar one, `Γᴴ(γ⁰γ⁵)Γ = γ⁰γ⁵`; its composite with `R = γ⁵` is `i γ⁰`, the conventional parity,
which keeps the scalar mass and reverses the pseudoscalar. -/
theorem nc_dirac :
    g1 * g2 * g3 = Gam ∧ I • (g0 * g1 * g2 * g3) = g5 ∧
    g0 * g0 = 1 ∧
    g1 * g1 = -1 ∧
    g2 * g2 = -1 ∧
    g3 * g3 = -1 ∧
    g0 * g1 = -(g1 * g0) ∧
    g0 * g2 = -(g2 * g0) ∧
    g0 * g3 = -(g3 * g0) ∧
    g1 * g2 = -(g2 * g1) ∧
    g1 * g3 = -(g3 * g1) ∧
    g2 * g3 = -(g3 * g2) ∧
    Gamᴴ = Gam ∧
    Gam * Gam = 1 ∧
    Gamᴴ * g0 * Gam = -g0 ∧
    Gamᴴ * (g0 * g5) * Gam = g0 * g5 ∧
    g5 * Gam = I • g0 ∧
    g0ᴴ * g0 * g0 = g0 ∧
    g0ᴴ * (g0 * g5) * g0 = -(g0 * g5) :=
  ⟨nc_dirac_0, nc_dirac_1, nc_dirac_2, nc_dirac_3, nc_dirac_4, nc_dirac_5, nc_dirac_6, nc_dirac_7, nc_dirac_8, nc_dirac_9, nc_dirac_10, nc_dirac_11, nc_dirac_12, nc_dirac_13, nc_dirac_14, nc_dirac_15, nc_dirac_16, nc_dirac_17, nc_dirac_18⟩

end Dirac

/-! ## C11: the three reflections -/

/-- The cut's reflections on `(t, x¹, x², x³)`: `P` flips three legs, `T` flips one, `R` fixes all four
(it acts by `γ⁵`, which reverses the radius and keeps the cut). -/
def nc_Pm : Matrix (Fin 4) (Fin 4) ℤ := Matrix.diagonal ![1, -1, -1, -1]
def nc_Tm : Matrix (Fin 4) (Fin 4) ℤ := Matrix.diagonal ![-1, 1, 1, 1]
def nc_Rm : Matrix (Fin 4) (Fin 4) ℤ := 1

/-- **C11.** `P` and `T` reverse the cut's orientation, `R` and `PT` do not. -/
theorem nc_reflections :
    nc_Pm.det = -1 ∧ nc_Tm.det = -1 ∧ nc_Rm.det = 1 ∧ (nc_Pm * nc_Tm).det = 1 := by
  refine ⟨?_, ?_, by simp [nc_Rm], ?_⟩
  · simp [nc_Pm, Matrix.det_diagonal, Fin.prod_univ_four]
  · simp [nc_Tm, Matrix.det_diagonal, Fin.prod_univ_four]
  · rw [Matrix.det_mul]; simp [nc_Pm, nc_Tm, Matrix.det_diagonal, Fin.prod_univ_four]

/-! ## C12: the layer's reflection exchanges self-dual and anti-self-dual -/

/-- `e_{ij} = E_{ij} − E_{ji}`, a generator of `so(4)`. -/
def nc_e (i j : Fin 4) : Matrix (Fin 4) (Fin 4) ℤ := Matrix.single i j 1 - Matrix.single j i 1

/-- The self-dual and anti-self-dual bases. -/
def nc_sd : Fin 3 → Matrix (Fin 4) (Fin 4) ℤ :=
  ![nc_e 0 1 + nc_e 2 3, nc_e 0 2 - nc_e 1 3, nc_e 0 3 + nc_e 1 2]
def nc_asd : Fin 3 → Matrix (Fin 4) (Fin 4) ℤ :=
  ![nc_e 0 1 - nc_e 2 3, nc_e 0 2 + nc_e 1 3, nc_e 0 3 - nc_e 1 2]

/-- The rotation `diag(1, 1, −1, −1)`. -/
def nc_rot : Matrix (Fin 4) (Fin 4) ℤ := Matrix.diagonal ![1, 1, -1, -1]

/-- **C12.** The reflection `p = diag(1, −1, −1, −1)` reversing three directions through a point lies in
`O(4)` with determinant `−1`, and conjugation by it carries each self-dual generator onto (minus) the
matching anti-self-dual one, and back; the rotation `diag(1, 1, −1, −1)` (determinant `1`) carries each
self-dual generator onto (plus or minus) itself. -/
theorem nc_selfdual_swap :
    nc_Pmᵀ * nc_Pm = 1 ∧ nc_Pm.det = -1 ∧
    (∀ k, nc_Pm * nc_sd k * nc_Pm = -nc_asd k) ∧ (∀ k, nc_Pm * nc_asd k * nc_Pm = -nc_sd k) ∧
    nc_rot.det = 1 ∧ (∀ k, nc_rot * nc_sd k * nc_rot = nc_sd k ∨ nc_rot * nc_sd k * nc_rot = -nc_sd k) := by
  refine ⟨by decide, nc_reflections.1, by decide, by decide, ?_, by decide⟩
  simp [nc_rot, Matrix.det_diagonal, Fin.prod_univ_four]

/-! ## C13: the quark mass determinant is real -/

section Block
variable {n : ℕ}

open Matrix in
/-- The block swap `[[0, I], [I, 0]]` has determinant `(−1)ⁿ`: it is `diag(−I, I) · L · U · L` with
`L = [[I, 0], [I, I]]` and `U = [[I, −I], [0, I]]`. -/
theorem nc_det_swap :
    (fromBlocks (0 : Matrix (Fin n) (Fin n) ℂ) (1 : Matrix (Fin n) (Fin n) ℂ) (1 : Matrix (Fin n) (Fin n) ℂ)
      (0 : Matrix (Fin n) (Fin n) ℂ)).det = (-1) ^ n := by
  have h : fromBlocks (0 : Matrix (Fin n) (Fin n) ℂ) (1 : Matrix (Fin n) (Fin n) ℂ)
      (1 : Matrix (Fin n) (Fin n) ℂ) (0 : Matrix (Fin n) (Fin n) ℂ) =
      fromBlocks (-1 : Matrix (Fin n) (Fin n) ℂ) 0 0 1 *
        (fromBlocks (1 : Matrix (Fin n) (Fin n) ℂ) 0 1 1 *
          (fromBlocks (1 : Matrix (Fin n) (Fin n) ℂ) (-1) 0 1 *
            fromBlocks (1 : Matrix (Fin n) (Fin n) ℂ) 0 1 1)) := by
    simp [fromBlocks_multiply]
  rw [h]
  simp [det_neg, Fintype.card_fin]

open Matrix in
/-- `det [[0, B], [C, D]] = (−1)ⁿ det B det C` for square blocks of size `n`. -/
theorem nc_det_zero11 (B C D : Matrix (Fin n) (Fin n) ℂ) :
    (fromBlocks 0 B C D).det = (-1) ^ n * B.det * C.det := by
  have h : fromBlocks 0 B C D = fromBlocks B 0 D C *
      fromBlocks (0 : Matrix (Fin n) (Fin n) ℂ) (1 : Matrix (Fin n) (Fin n) ℂ) 1 0 := by
    simp [fromBlocks_multiply]
  rw [h, det_mul, det_fromBlocks_zero₁₂, nc_det_swap]; ring

open Matrix in
/-- **C13.** With the couplings tied by the parity (the right-handed block the Hermitian conjugate of the
left-handed one, `v_L, v_R` real) and any singlet mass block `C`, the quark mass determinant is
`(−1)ⁿ v_Lⁿ v_Rⁿ |det A|²`: real, so its phase is `0` or `π`, whatever `C` and the complex couplings `A`. -/
theorem nc_det_real (A C : Matrix (Fin n) (Fin n) ℂ) (vL vR : ℝ) :
    (fromBlocks 0 ((vL : ℂ) • A) ((vR : ℂ) • Aᴴ) C).det =
      ((-1) ^ n * vL ^ n * vR ^ n * Complex.normSq A.det : ℝ) ∧
    ((fromBlocks 0 ((vL : ℂ) • A) ((vR : ℂ) • Aᴴ) C).det).im = 0 := by
  have h : (fromBlocks 0 ((vL : ℂ) • A) ((vR : ℂ) • Aᴴ) C).det =
      ((-1) ^ n * vL ^ n * vR ^ n * Complex.normSq A.det : ℝ) := by
    rw [nc_det_zero11, det_smul, det_smul, det_conjTranspose, Fintype.card_fin]
    push_cast
    rw [Complex.normSq_eq_conj_mul_self]
    simp only [Complex.star_def]
    ring
  exact ⟨h, by rw [h]; exact Complex.ofReal_im _⟩

end Block

/-- **C13, non-vacuity.** At `n = 1`, `A = (i)`, `C = (5)`, `v_L = 2`, `v_R = 3`: the determinant is `−6`. -/
theorem nc_det_witness :
    (Matrix.fromBlocks (0 : Matrix (Fin 1) (Fin 1) ℂ) (((2 : ℝ) : ℂ) • !![Complex.I])
      (((3 : ℝ) : ℂ) • (!![Complex.I])ᴴ) !![5]).det = -6 := by
  rw [(nc_det_real !![Complex.I] !![5] 2 3).1]
  simp [Complex.normSq_I]
  norm_num

/-! ## C14: the closure of four -/

/-- **C14.** Let `P` be an involution on states that sends every left state to a right state. A set
that contains a two-element set of left states and that `P` carries into itself has at least four
elements; and the four states `L ∪ P(L)` already form such a set. -/
theorem nc_four {S : Type*} [DecidableEq S] (P : S → S) (hP : ∀ x, P (P x) = x)
    (left : S → Prop) (hLR : ∀ x, left x → ¬ left (P x)) (L : Finset S) (hL : L.card = 2)
    (hLl : ∀ x ∈ L, left x) :
    (∀ X : Finset S, L ⊆ X → (∀ x ∈ X, P x ∈ X) → 4 ≤ X.card) ∧
    ((L ∪ L.image P).card = 4 ∧ ∀ x ∈ L ∪ L.image P, P x ∈ L ∪ L.image P) := by
  have hinj : Function.Injective P := fun a b h => by rw [← hP a, h, hP b]
  have hdisj : Disjoint L (L.image P) := by
    rw [Finset.disjoint_left]
    intro x hx hxP
    obtain ⟨y, hy, rfl⟩ := Finset.mem_image.1 hxP
    exact hLR y (hLl y hy) (hLl _ hx)
  have hcard : (L ∪ L.image P).card = 4 := by
    rw [Finset.card_union_of_disjoint hdisj, Finset.card_image_of_injective _ hinj, hL]
  refine ⟨fun X hLX hX => ?_, hcard, fun x hx => ?_⟩
  · have hsub : L ∪ L.image P ⊆ X := Finset.union_subset hLX (fun y hy => by
      obtain ⟨z, hz, rfl⟩ := Finset.mem_image.1 hy; exact hX z (hLX hz))
    rw [← hcard]; exact Finset.card_le_card hsub
  · rcases Finset.mem_union.1 hx with h | h
    · exact Finset.mem_union_right _ (Finset.mem_image_of_mem P h)
    · obtain ⟨z, hz, rfl⟩ := Finset.mem_image.1 h
      rw [hP]; exact Finset.mem_union_left _ hz

/-- **C14, non-vacuity.** On four states `{νL, eL, νR, eR}` with `P` exchanging `νL ↔ νR`, `eL ↔ eR`, the
left doublet `{νL, eL}` meets every hypothesis. -/
theorem nc_four_witness :
    let P : Fin 4 → Fin 4 := ![2, 3, 0, 1]
    (∀ x, P (P x) = x) ∧ (∀ x : Fin 4, x.val < 2 → ¬ (P x).val < 2) ∧
    ({0, 1} : Finset (Fin 4)).card = 2 := by
  refine ⟨by decide, by decide, by decide⟩

end ShadowProbe.NewClaimsProbe

#print axioms ShadowProbe.NewClaimsProbe.nc_LambdaYM_lt
#print axioms ShadowProbe.NewClaimsProbe.nc_f_diff
#print axioms ShadowProbe.NewClaimsProbe.nc_r2_signs
#print axioms ShadowProbe.NewClaimsProbe.nc_characters
#print axioms ShadowProbe.NewClaimsProbe.nc_signature_scale
#print axioms ShadowProbe.NewClaimsProbe.nc_signature_number
#print axioms ShadowProbe.NewClaimsProbe.nc_charges
#print axioms ShadowProbe.NewClaimsProbe.nc_anomalies
#print axioms ShadowProbe.NewClaimsProbe.nc_nariai_max
#print axioms ShadowProbe.NewClaimsProbe.nc_dirac
#print axioms ShadowProbe.NewClaimsProbe.nc_reflections
#print axioms ShadowProbe.NewClaimsProbe.nc_selfdual_swap
#print axioms ShadowProbe.NewClaimsProbe.nc_det_real
#print axioms ShadowProbe.NewClaimsProbe.nc_det_witness
#print axioms ShadowProbe.NewClaimsProbe.nc_four
#print axioms ShadowProbe.NewClaimsProbe.nc_four_witness

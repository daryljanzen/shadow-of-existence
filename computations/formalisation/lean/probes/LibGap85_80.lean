import ShadowEngine

/-! # Campaign 34 (`r7443+71`): library-gap rows 85 (the SdS tetrad and its superpotential) and 80 (the Killing form on the dS₅ coset)

`r7443_71_pricing/PRICING.md`: neither row needs the library its gap names.
- ***Row 85*** (`P14_B3_spinor_vielbein.py`): the tetrad identity and the superpotential's values. The Dirac
  operator's separation (`λ = j + ½`, superpotential `λ ω²₁`) is imported, the spinor library's. At the throat
  `f < 0`, so the receipt's `|√f/r|` there is a complex modulus, and it is stated as one (`throat_check`).
- ***Row 80*** (`P12_coset_metric.py`): `B = tr(ad ad)` on `so(5,1)`, computed over `ℤ` from the generators and
  restricted to the coset. The quotient manifold and its invariant metric are the receipt's reading, imported. -/

namespace ShadowProbe

namespace LibGap85_80

open Real Matrix

/-! ### Row 85 -/

/-- SdS: `f = 1 − 2M/r − r²/α²` -/
noncomputable def fS (M α r : ℝ) : ℝ := 1 - 2 * M / r - r ^ 2 / α ^ 2

/-- the orthonormal tetrad `(√f dt, dr/√f, r dθ, r sinθ dφ)`, as the matrix `e^a_μ` -/
noncomputable def tet (f r θ : ℝ) : Matrix (Fin 4) (Fin 4) ℝ :=
  !![Real.sqrt f, 0, 0, 0; 0, 1 / Real.sqrt f, 0, 0; 0, 0, r, 0; 0, 0, 0, r * Real.sin θ]

/-- ⛭ **`tetrad_metric`.** Where `f > 0`, `η_ab e^a_μ e^b_ν = diag(−f, 1/f, r², r² sin²θ)` -/
theorem tetrad_metric (f r θ : ℝ) (hf : 0 < f) :
    (tet f r θ)ᵀ * Matrix.diagonal ![-1, 1, 1, 1] * tet f r θ =
      Matrix.diagonal ![-f, 1 / f, r ^ 2, r ^ 2 * Real.sin θ ^ 2] := by
  have hs : Real.sqrt f ^ 2 = f := Real.sq_sqrt hf.le
  have hs0 : Real.sqrt f ≠ 0 := (Real.sqrt_pos.mpr hf).ne'
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [tet, Matrix.mul_apply, Fin.sum_univ_four, Matrix.diagonal] <;> field_simp <;> nlinarith [hs]

/-- ⛭ **`superpotential_values`.** At the receipt's `M = 0.12`, `α = 1`, `λ = 1`, with `W = √f/r`:
- `W(1/2)` agrees with `1.0392305` to `10⁻⁶`;
- `W(−1/2)` agrees with `−2.2181073` to `10⁻⁶`, and is negative;
- `|f| < 10⁻⁹` at the two decimal horizon roots. -/
theorem superpotential_values :
    |Real.sqrt (fS 0.12 1 (1 / 2)) / (1 / 2) - 1.0392305| < 1e-6 ∧
      |Real.sqrt (fS 0.12 1 (-1 / 2)) / (-1 / 2) - (-2.2181073)| < 1e-6 ∧
      Real.sqrt (fS 0.12 1 (-1 / 2)) / (-1 / 2) < 0 ∧
      |fS 0.12 1 0.2569683156| < 1e-9 ∧ |fS 0.12 1 0.8464391538| < 1e-9 := by
  have e1 : fS 0.12 1 (1 / 2) = 0.27 := by norm_num [fS]
  have e2 : fS 0.12 1 (-1 / 2) = 1.23 := by norm_num [fS]
  rw [e1, e2]
  have a1 : 0.51961475 < Real.sqrt 0.27 := Real.lt_sqrt (by norm_num) |>.mpr (by norm_num)
  have b1 : Real.sqrt 0.27 < 0.51961575 := (Real.sqrt_lt' (by norm_num)).mpr (by norm_num)
  have a2 : 1.10905315 < Real.sqrt 1.23 := Real.lt_sqrt (by norm_num) |>.mpr (by norm_num)
  have b2 : Real.sqrt 1.23 < 1.10905415 := (Real.sqrt_lt' (by norm_num)).mpr (by norm_num)
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · rw [abs_lt]; constructor <;> linarith
  · rw [abs_lt]; constructor <;> linarith
  · linarith
  · rw [abs_lt]; norm_num [fS]
  · rw [abs_lt]; norm_num [fS]

/-- ⛭ **`horizon_W`.** And `|W| < 10⁻⁴` at both horizon roots, with `|W| = √|f|/r`, the complex modulus, which is the
receipt's `abs(complex(…))` whatever the sign of the tiny `f` -/
theorem horizon_W :
    Real.sqrt |fS 0.12 1 0.2569683156| / 0.2569683156 < 1e-4 ∧
      Real.sqrt |fS 0.12 1 0.8464391538| / 0.8464391538 < 1e-4 := by
  have k : ∀ x : ℝ, |x| < 1e-10 → Real.sqrt |x| < 1e-4 * 0.25 := fun x hx =>
    (Real.sqrt_lt' (by norm_num)).mpr (by nlinarith [abs_nonneg x])
  have h1 : |fS 0.12 1 0.2569683156| < 1e-10 := by rw [abs_lt]; norm_num [fS]
  have h2 : |fS 0.12 1 0.8464391538| < 1e-10 := by rw [abs_lt]; norm_num [fS]
  constructor
  · rw [div_lt_iff₀ (by norm_num)]; linarith [k _ h1]
  · rw [div_lt_iff₀ (by norm_num)]; linarith [k _ h2]

/-- ⛭ **`throat_check`, stated as what it is.** At `r = 1/1000`, `f < 0`, so the tetrad is NOT real there and the
receipt's `|√f/r|` is a complex modulus. That modulus `√|f|/r` exceeds `10³`. (A literal `Real.sqrt` port reads `0`
here.) -/
theorem throat_check :
    fS 0.12 1 (1 / 1000) < 0 ∧ Real.sqrt |fS 0.12 1 (1 / 1000)| / (1 / 1000) > 1e3 := by
  have e : fS 0.12 1 (1 / 1000) = -239.000001 := by norm_num [fS]
  rw [e]; refine ⟨by norm_num, ?_⟩
  have : 1 < Real.sqrt |(-239.000001 : ℝ)| := Real.lt_sqrt (by norm_num) |>.mpr (by norm_num [abs_of_neg])
  rw [gt_iff_lt, lt_div_iff₀ (by norm_num)]; linarith

/-! ### Row 80 -/

/-- `η = diag(−1, 1, 1, 1, 1, 1)` -/
def eta : Fin 6 → ℤ := ![-1, 1, 1, 1, 1, 1]

/-- the fifteen index pairs `μ < ν` -/
def keys : Fin 15 → Fin 6 × Fin 6 :=
  ![(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5),
    (4, 5)]

/-- `(M_μν)_ρσ = δ_ρμ η_νσ − δ_ρν η_μσ` -/
def gen (k : Fin 15) (ρ σ : Fin 6) : ℤ :=
  (if ρ = (keys k).1 ∧ σ = (keys k).2 then eta (keys k).2 else 0) -
    (if ρ = (keys k).2 ∧ σ = (keys k).1 then eta (keys k).1 else 0)

def br (A B : Fin 6 → Fin 6 → ℤ) (ρ σ : Fin 6) : ℤ := ∑ τ, (A ρ τ * B τ σ - B ρ τ * A τ σ)

/-- the coordinate of `M_k` in an element of the span: its `(μ, ν)` entry divided by `η_νν = ±1` -/
def coord (A : Fin 6 → Fin 6 → ℤ) (k : Fin 15) : ℤ := A (keys k).1 (keys k).2 * eta (keys k).2

/-- `ad_i`, as a `15 × 15` matrix: `(ad_i)_kj` is the `M_k` coordinate of `[M_i, M_j]` -/
def adm (i k j : Fin 15) : ℤ := coord (br (gen i) (gen j)) k

/-- the Killing form `B_ij = tr(ad_i ad_j)` -/
def Bk (i j : Fin 15) : ℤ := ∑ k, ∑ l, adm i k l * adm j l k

/-- the coset `m = span{M_a5}`: generator indices `4, 8, 11, 13, 14` -/
def mIdx : Fin 5 → Fin 15 := ![4, 8, 11, 13, 14]

set_option maxHeartbeats 0 in
/-- ⛭ **`killing_on_coset`.**
- The bracket closes on the span: every `[M_i, M_j]` is the combination its coordinates name (`closure`).
- `B|_m = diag(8, −8, −8, −8, −8)` = `−8 η_ab`: Lorentzian, signature `(1, 4)`. -/
theorem killing_on_coset :
    (∀ i j : Fin 15, ∀ ρ σ : Fin 6, br (gen i) (gen j) ρ σ = ∑ k, adm i k j * gen k ρ σ) ∧
      (fun a b : Fin 5 => Bk (mIdx a) (mIdx b)) = ![![8, 0, 0, 0, 0], ![0, -8, 0, 0, 0], ![0, 0, -8, 0, 0],
        ![0, 0, 0, -8, 0], ![0, 0, 0, 0, -8]] := by
  refine ⟨by decide +kernel, by decide +kernel⟩

end LibGap85_80

end ShadowProbe

#print axioms ShadowProbe.LibGap85_80.tetrad_metric
#print axioms ShadowProbe.LibGap85_80.superpotential_values
#print axioms ShadowProbe.LibGap85_80.horizon_W
#print axioms ShadowProbe.LibGap85_80.throat_check
#print axioms ShadowProbe.LibGap85_80.killing_on_coset

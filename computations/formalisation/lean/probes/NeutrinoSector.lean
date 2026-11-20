import Mathlib

/-!
# Campaign 145: 72's L550 Y10–Y17 at their formal cores (`r7835`)

The rows of `computations/formalisation/r7835_71_campaign145/PREDICTION.md`:
- E1 the seesaw relation;
- E2 the dimension counts of the Pati–Salam channels;
- E3 sixteen slots filled by sixteen states;
- E4 the `ΔN_eff` floor and bound;
- E5 the decoupling temperature;
- E6 the scale arithmetic and the strong-CP caps;
- E7 the gravitational Majorana splitting against the solar bound;
- E8 the neutral mass matrix's rank bound (at least `6 − n` zeros).
-/

namespace ShadowProbe.NeutrinoSectorProbe

open Matrix

/-! ## E1: the seesaw relation -/

theorem ns_seesaw {vL vR M : ℝ} (hM : M ≠ 0) (hR : vR ≠ 0) :
    (vL / vR) ^ 2 = (vL ^ 2 / M) / (vR ^ 2 / M) ∧
      (vL * vR / M) ^ 2 = (vL ^ 2 / M) * (vR ^ 2 / M) := by
  constructor
  · field_simp
  · field_simp

/-! ## E2: the dimension counts -/

theorem ns_dims : 4 * 4 = 1 + 15 ∧ 4 * 4 = 6 + 10 ∧ 2 * 2 = 1 + 3 := by norm_num

/-! ## E3: sixteen slots, sixteen states -/

theorem ns_slots {S : Type*} [Fintype S] (hS : Fintype.card S = 16)
    (f : S → Fin 4 × Fin 2 × Fin 2) (hf : Function.Injective f) :
    Function.Bijective f ∧
      (Finset.univ.filter (fun s : Fin 4 × Fin 2 × Fin 2 => s.1 = 3)).card = 4 ∧
      ∀ s, ∃! x, f x = s := by
  have hb : Function.Bijective f :=
    (Fintype.bijective_iff_injective_and_card f).2 ⟨hf, by simp [hS]⟩
  exact ⟨hb, by decide, fun s => hb.existsUnique s⟩

theorem ns_slots_witness :
    Function.Bijective (id : Fin 4 × Fin 2 × Fin 2 → Fin 4 × Fin 2 × Fin 2) :=
  (ns_slots (by simp) id Function.injective_id).1

/-! ## E4, E5: the `4/3` powers, by cubing -/

lemma ns_cube {x a b : ℝ} (hx : 0 < x) (hb : 0 ≤ b)
    (h1 : a ^ 3 < x ^ 4) (h2 : x ^ 4 < b ^ 3) :
    a < x ^ ((4 : ℝ) / 3) ∧ x ^ ((4 : ℝ) / 3) < b := by
  have hy0 : 0 ≤ x ^ ((4 : ℝ) / 3) := Real.rpow_nonneg hx.le _
  have hy : (x ^ ((4 : ℝ) / 3)) ^ 3 = x ^ 4 := by
    rw [← Real.rpow_natCast, ← Real.rpow_mul hx.le]
    norm_num
  constructor
  · by_contra h
    have := pow_le_pow_left₀ hy0 (not_lt.mp h) 3
    linarith
  · by_contra h
    have := pow_le_pow_left₀ hb (not_lt.mp h) 3
    linarith

theorem ns_neff :
    (0.285 : ℝ) < 3 * (10.75 / 61.75 : ℝ) ^ ((4 : ℝ) / 3) ∧
      3 * (10.75 / 61.75 : ℝ) ^ ((4 : ℝ) / 3) < 0.295 ∧
      (0.140 : ℝ) < 3 * (10.75 / 106.75 : ℝ) ^ ((4 : ℝ) / 3) ∧
      3 * (10.75 / 106.75 : ℝ) ^ ((4 : ℝ) / 3) < 0.142 := by
  obtain ⟨a1, b1⟩ := ns_cube (x := 10.75 / 61.75) (a := 0.0951) (b := 0.0983)
    (by norm_num) (by norm_num) (by norm_num) (by norm_num)
  obtain ⟨a2, b2⟩ := ns_cube (x := 10.75 / 106.75) (a := 0.0467) (b := 0.0473)
    (by norm_num) (by norm_num) (by norm_num) (by norm_num)
  refine ⟨by linarith, by linarith, by linarith, by linarith⟩

theorem ns_tdec :
    (335 : ℝ) < (6400 / 80.38 : ℝ) ^ ((4 : ℝ) / 3) ∧
      (6400 / 80.38 : ℝ) ^ ((4 : ℝ) / 3) < 345 :=
  ns_cube (by norm_num) (by norm_num) (by norm_num) (by norm_num)

/-! ## E6: the scale arithmetic -/

theorem ns_scales :
    |(246.22 : ℝ) ^ 2 / 2.435e18 * 1e9 - 2.5e-5| < 0.05e-5 ∧
      (1900 : ℝ) < 0.05 / ((246.22 : ℝ) ^ 2 / 2.435e18 * 1e9) ∧
      0.05 / ((246.22 : ℝ) ^ 2 / 2.435e18 * 1e9) < 2100 ∧
      |(246.22 : ℝ) ^ 2 / 0.05e-9 - 1.2e15| < 0.02e15 ∧
      (0.95 : ℝ) < (3.5e7 : ℝ) ^ 2 / ((246.22 : ℝ) ^ 2 / 0.05e-9) ∧
      (3.5e7 : ℝ) ^ 2 / ((246.22 : ℝ) ^ 2 / 0.05e-9) < 1.05 ∧
      (0.5e-11 : ℝ) < 246.22 / 2.4e13 ∧ (246.22 : ℝ) / 2.4e13 < 2e-11 ∧
      (5e-6 : ℝ) < 246.22 / 3.5e7 ∧ (246.22 : ℝ) / 3.5e7 < 1e-5 ∧
      |(2.435e18 : ℝ) / 1e5 - 2.4e13| < 0.05e13 ∧
      |(246.22 : ℝ) ^ 2 / 0.05e-9 / 1e5 - 1.2e10| < 0.05e10 := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;>
    norm_num [abs_lt]

/-- The cap: `v_R² / Λ² < 10⁻¹⁰` exactly when `v_R < Λ / 10⁵`. -/
theorem ns_cap {vR Λ : ℝ} (hv : 0 < vR) (hΛ : 0 < Λ) :
    vR ^ 2 / Λ ^ 2 < 1e-10 ↔ vR < Λ / 1e5 := by
  rw [div_lt_iff₀ (by positivity)]
  constructor
  · intro h
    by_contra h'
    have := pow_le_pow_left₀ (by positivity) (not_lt.mp h') 2
    nlinarith
  · intro h
    have := pow_lt_pow_left₀ h hv.le (by norm_num : (2 : ℕ) ≠ 0)
    nlinarith

/-! ## E7: the gravitational Majorana splitting -/

theorem ns_splitting :
    (0.155 : ℝ) < (2 * 6400 / 0.65 : ℝ) ^ 2 / 2.435e18 * 1e9 ∧
      (2 * 6400 / 0.65 : ℝ) ^ 2 / 2.435e18 * 1e9 < 0.165 ∧
      (1e8 : ℝ) < (2 * 6400 / 0.65 : ℝ) ^ 2 / 2.435e18 * 1e9 /
        (2e-11 / (2 * Real.sqrt 7.42e-5)) ∧
      (2 * 6400 / 0.65 : ℝ) ^ 2 / 2.435e18 * 1e9 /
        (2e-11 / (2 * Real.sqrt 7.42e-5)) < 2e8 := by
  have hs1 : (0.0086 : ℝ) < Real.sqrt 7.42e-5 := by
    rw [Real.lt_sqrt (by norm_num)]; norm_num
  have hs2 : Real.sqrt 7.42e-5 < 0.0087 := by
    rw [Real.sqrt_lt' (by norm_num)]; norm_num
  have hs0 : 0 < Real.sqrt 7.42e-5 := by linarith
  have key : ∀ μ : ℝ, μ / (2e-11 / (2 * Real.sqrt 7.42e-5)) = μ * Real.sqrt 7.42e-5 * 1e11 := by
    intro μ; field_simp; ring
  rw [key]
  refine ⟨by norm_num, by norm_num, ?_, ?_⟩ <;> nlinarith

/-! ## E8: the neutral mass matrix has at least `6 − n` zeros -/

section Rank
variable {n : ℕ}

lemma ns_rank_add_le {m k : Type*} [Fintype m] [Fintype k] [DecidableEq k]
    (A B : Matrix m k ℂ) : (A + B).rank ≤ A.rank + B.rank := by
  unfold Matrix.rank
  rw [Matrix.mulVecLin_add]
  calc Module.finrank ℂ (LinearMap.range (A.mulVecLin + B.mulVecLin))
      ≤ Module.finrank ℂ
          (LinearMap.range A.mulVecLin ⊔ LinearMap.range B.mulVecLin : Submodule ℂ (m → ℂ)) :=
        Submodule.finrank_mono (LinearMap.range_add_le _ _)
    _ ≤ _ := Submodule.finrank_add_le_finrank_add_finrank _ _

lemma ns_split (D : Matrix (Fin 6) (Fin n) ℂ) (MS : Matrix (Fin n) (Fin n) ℂ) :
    fromBlocks 0 D Dᵀ MS =
      fromRows D 0 * fromCols (0 : Matrix (Fin n) (Fin 6) ℂ) 1 +
        fromRows (0 : Matrix (Fin 6) (Fin n) ℂ) 1 * fromCols Dᵀ MS := by
  rw [fromRows_mul_fromCols, fromRows_mul_fromCols, fromBlocks_add]
  simp

/-- **E8.** For any `6 × n` Yukawa-times-vev block `D` and any singlet mass matrix `M_S`, the neutral
mass matrix `[[0, D], [Dᵀ, M_S]]` has rank at most `2n`, so its kernel has dimension at least `6 − n`. -/
theorem ns_zeros (D : Matrix (Fin 6) (Fin n) ℂ) (MS : Matrix (Fin n) (Fin n) ℂ) :
    (fromBlocks 0 D Dᵀ MS).rank ≤ 2 * n ∧
      6 + n ≤ 2 * n + Module.finrank ℂ (LinearMap.ker (fromBlocks 0 D Dᵀ MS).mulVecLin) := by
  have hr : (fromBlocks 0 D Dᵀ MS).rank ≤ 2 * n := by
    rw [ns_split]
    refine (ns_rank_add_le _ _).trans ?_
    have h1 := (Matrix.rank_mul_le_left (fromRows D (0 : Matrix (Fin n) (Fin n) ℂ))
      (fromCols (0 : Matrix (Fin n) (Fin 6) ℂ) (1 : Matrix (Fin n) (Fin n) ℂ))).trans
      (Matrix.rank_le_card_width _)
    have h2 := (Matrix.rank_mul_le_left
      (fromRows (0 : Matrix (Fin 6) (Fin n) ℂ) (1 : Matrix (Fin n) (Fin n) ℂ))
      (fromCols Dᵀ MS)).trans (Matrix.rank_le_card_width _)
    simp only [Fintype.card_fin] at h1 h2
    omega
  refine ⟨hr, ?_⟩
  have hrn := LinearMap.finrank_range_add_finrank_ker (fromBlocks 0 D Dᵀ MS).mulVecLin
  rw [Module.finrank_fintype_fun_eq_card, Fintype.card_sum, Fintype.card_fin,
    Fintype.card_fin] at hrn
  unfold Matrix.rank at hr
  omega

theorem ns_need_five (D : Matrix (Fin 6) (Fin n) ℂ) (MS : Matrix (Fin n) (Fin n) ℂ)
    (hn : n ≤ 4) :
    2 ≤ Module.finrank ℂ (LinearMap.ker (fromBlocks 0 D Dᵀ MS).mulVecLin) := by
  have := (ns_zeros D MS).2
  omega

theorem ns_three_singlets (D : Matrix (Fin 6) (Fin 3) ℂ) (MS : Matrix (Fin 3) (Fin 3) ℂ) :
    3 ≤ Module.finrank ℂ (LinearMap.ker (fromBlocks 0 D Dᵀ MS).mulVecLin) := by
  have := (ns_zeros D MS).2
  omega

end Rank

end ShadowProbe.NeutrinoSectorProbe

#print axioms ShadowProbe.NeutrinoSectorProbe.ns_seesaw
#print axioms ShadowProbe.NeutrinoSectorProbe.ns_dims
#print axioms ShadowProbe.NeutrinoSectorProbe.ns_slots
#print axioms ShadowProbe.NeutrinoSectorProbe.ns_slots_witness
#print axioms ShadowProbe.NeutrinoSectorProbe.ns_neff
#print axioms ShadowProbe.NeutrinoSectorProbe.ns_tdec
#print axioms ShadowProbe.NeutrinoSectorProbe.ns_scales
#print axioms ShadowProbe.NeutrinoSectorProbe.ns_cap
#print axioms ShadowProbe.NeutrinoSectorProbe.ns_splitting
#print axioms ShadowProbe.NeutrinoSectorProbe.ns_zeros
#print axioms ShadowProbe.NeutrinoSectorProbe.ns_need_five
#print axioms ShadowProbe.NeutrinoSectorProbe.ns_three_singlets

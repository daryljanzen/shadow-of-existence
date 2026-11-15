import Mathlib

/-!
# P12 (`algebroid_paper`): the symmetric-space grading `so(5,1) = so(4,1) ⊕ 𝔪` (`prop:closure`)

Campaign 141 (`r7797`). Conventions as in the receipt `P12_bracket_closure.py`: `η = diag(−1, 1, 1, 1, 1, 1)`,
`(M_μν)^ρ_σ = δ^ρ_μ η_νσ − δ^ρ_ν η_μσ`, `𝔥 = so(4,1)` (row and column `5` zero), `𝔪` the boosts `M_a5`.
-/

open Matrix

namespace ShadowProbe.AlgebroidProbe

/-- The signature `η = diag(−1, 1, 1, 1, 1, 1)`. -/
def al_s : Fin 6 → ℝ := ![-1, 1, 1, 1, 1, 1]

lemma al_s_sq (i : Fin 6) : al_s i * al_s i = 1 := by fin_cases i <;> simp [al_s]

lemma al_s_ne (i : Fin 6) : al_s i ≠ 0 := fun h => by simpa [h] using al_s_sq i

lemma al_s5 : al_s 5 = 1 := rfl

/-- `Aᵀη + ηA = 0`, entrywise. -/
def al_skew (A : Matrix (Fin 6) (Fin 6) ℝ) : Prop := ∀ i j, al_s j * A j i + al_s i * A i j = 0

lemma al_skew_iff (A : Matrix (Fin 6) (Fin 6) ℝ) :
    Aᵀ * diagonal al_s + diagonal al_s * A = 0 ↔ al_skew A := by
  constructor
  · intro h i j
    have := congrFun (congrFun h i) j
    simp only [Matrix.add_apply, mul_diagonal, diagonal_mul, transpose_apply, Matrix.zero_apply] at this
    linarith
  · intro h
    ext i j
    simp only [Matrix.add_apply, mul_diagonal, diagonal_mul, transpose_apply, Matrix.zero_apply]
    linarith [h i j]

lemma al_skew_diag {A : Matrix (Fin 6) (Fin 6) ℝ} (h : al_skew A) (i : Fin 6) : A i i = 0 := by
  have := h i i
  have : al_s i * A i i = 0 := by linarith
  exact (mul_eq_zero.1 this).resolve_left (al_s_ne i)

lemma al_skew_swap {A : Matrix (Fin 6) (Fin 6) ℝ} (h : al_skew A) (i j : Fin 6) :
    A j i = -(al_s i * al_s j * A i j) := by
  have e := h i j
  have := al_s_sq j
  linear_combination al_s j * e - A j i * this

/-- The subspace of `so(5,1)` whose above-diagonal entries vanish off a pattern `P`. -/
def al_S (P : Fin 6 → Fin 6 → Prop) : Submodule ℝ (Matrix (Fin 6) (Fin 6) ℝ) where
  carrier := {A | al_skew A ∧ ∀ i j, i < j → ¬ P i j → A i j = 0}
  add_mem' := by
    rintro A B ⟨hA, hA'⟩ ⟨hB, hB'⟩
    refine ⟨fun i j => ?_, fun i j hij hP => ?_⟩
    · simp only [Matrix.add_apply]; linarith [hA i j, hB i j]
    · simp [hA' i j hij hP, hB' i j hij hP]
  zero_mem' := ⟨fun i j => by simp, fun i j _ _ => rfl⟩
  smul_mem' := by
    rintro c A ⟨hA, hA'⟩
    refine ⟨fun i j => ?_, fun i j hij hP => ?_⟩
    · simp only [Matrix.smul_apply, smul_eq_mul]; linear_combination c * hA i j
    · simp [hA' i j hij hP]

/-- `so(5,1)`. -/
def al_so : Submodule ℝ (Matrix (Fin 6) (Fin 6) ℝ) := al_S fun _ _ => True
/-- `𝔥 = so(4,1)`: the generators `M_ab`, `a, b ≤ 4`. -/
def al_h : Submodule ℝ (Matrix (Fin 6) (Fin 6) ℝ) := al_S fun _ j => j ≠ 5
/-- `𝔪`: the boosts `M_a5`. -/
def al_m : Submodule ℝ (Matrix (Fin 6) (Fin 6) ℝ) := al_S fun _ j => j = 5

lemma al_mem_so {A : Matrix (Fin 6) (Fin 6) ℝ} : A ∈ al_so ↔ Aᵀ * diagonal al_s + diagonal al_s * A = 0 := by
  rw [al_skew_iff]
  exact ⟨fun h => h.1, fun h => ⟨h, fun _ _ _ hP => absurd trivial hP⟩⟩

/-- `𝔥` is the part of `so(5,1)` with row and column `5` zero. -/
lemma al_mem_h {A : Matrix (Fin 6) (Fin 6) ℝ} : A ∈ al_h ↔ al_skew A ∧ ∀ i, A i 5 = 0 ∧ A 5 i = 0 := by
  constructor
  · rintro ⟨h, h'⟩
    have hc : ∀ i, A i 5 = 0 := fun i => by
      by_cases hi : i = 5
      · subst hi; exact al_skew_diag h 5
      · exact h' i 5 (lt_of_le_of_ne (Fin.le_last i) hi) (by simp)
    exact ⟨h, fun i => ⟨hc i, by rw [al_skew_swap h i 5, hc i]; ring⟩⟩
  · rintro ⟨h, h'⟩
    refine ⟨h, fun i j _ hP => ?_⟩
    have : j = 5 := by simpa using hP
    subst this; exact (h' i).1

/-- `𝔪` is the part of `so(5,1)` vanishing off row and column `5`. -/
lemma al_mem_m {A : Matrix (Fin 6) (Fin 6) ℝ} :
    A ∈ al_m ↔ al_skew A ∧ ∀ i j, i ≠ 5 → j ≠ 5 → A i j = 0 := by
  constructor
  · rintro ⟨h, h'⟩
    refine ⟨h, fun i j hi hj => ?_⟩
    rcases lt_trichotomy i j with hij | rfl | hij
    · exact h' i j hij hj
    · exact al_skew_diag h i
    · rw [al_skew_swap h j i, h' j i hij hi]; ring
  · rintro ⟨h, h'⟩
    exact ⟨h, fun i j hij hP => h' i j (fun hi => by subst hi; exact absurd hij (not_lt.2 (Fin.le_last j))) hP⟩

/-! ## Row C0: the setting -/

/-- **Row C0.** `so(5,1)` is closed under the commutator. -/
theorem al_so_bracket {A B : Matrix (Fin 6) (Fin 6) ℝ} (hA : A ∈ al_so) (hB : B ∈ al_so) :
    A * B - B * A ∈ al_so := by
  rw [al_mem_so] at *
  have hA' : Aᵀ * diagonal al_s = -(diagonal al_s * A) := eq_neg_of_add_eq_zero_left hA
  have hB' : Bᵀ * diagonal al_s = -(diagonal al_s * B) := eq_neg_of_add_eq_zero_left hB
  rw [transpose_sub, transpose_mul, transpose_mul, Matrix.sub_mul, Matrix.mul_assoc, Matrix.mul_assoc, hA', hB',
    Matrix.mul_neg, Matrix.mul_neg, ← Matrix.mul_assoc, ← Matrix.mul_assoc, hA', hB']
  noncomm_ring

/-- **Row C0.** `𝔥, 𝔪 ⊂ so(5,1)`, `𝔥 ∩ 𝔪 = 0`, and every element of `so(5,1)` is a sum of one from each. -/
theorem al_direct_sum :
    al_h ≤ al_so ∧ al_m ≤ al_so ∧ al_h ⊓ al_m = ⊥ ∧ al_h ⊔ al_m = al_so := by
  have hh : al_h ≤ al_so := fun A hA => ⟨hA.1, fun _ _ _ hP => absurd trivial hP⟩
  have hm : al_m ≤ al_so := fun A hA => ⟨hA.1, fun _ _ _ hP => absurd trivial hP⟩
  refine ⟨hh, hm, ?_, le_antisymm (sup_le hh hm) ?_⟩
  · rw [eq_bot_iff]
    rintro A ⟨h1, h2⟩
    rw [Submodule.mem_bot]
    obtain ⟨-, h1⟩ := al_mem_h.1 h1
    obtain ⟨-, h2⟩ := al_mem_m.1 h2
    ext i j
    by_cases hi : i = 5
    · subst hi; exact (h1 j).2
    · by_cases hj : j = 5
      · subst hj; exact (h1 i).1
      · exact h2 i j hi hj
  · rintro A ⟨hA, -⟩
    -- the `𝔥` part masks row and column `5`; the `𝔪` part keeps only them
    let Ah : Matrix (Fin 6) (Fin 6) ℝ := of fun i j => if i = 5 ∨ j = 5 then 0 else A i j
    let Am : Matrix (Fin 6) (Fin 6) ℝ := of fun i j => if i = 5 ∨ j = 5 then A i j else 0
    have hAh : Ah ∈ al_h := by
      refine al_mem_h.2 ⟨fun i j => ?_, fun i => ⟨by simp [Ah], by simp [Ah]⟩⟩
      simp only [Ah, of_apply, or_comm (a := j = 5)]
      split_ifs
      · ring
      · exact hA i j
    have hAm : Am ∈ al_m := by
      refine al_mem_m.2 ⟨fun i j => ?_, fun i j hi hj => by simp [Am, hi, hj]⟩
      simp only [Am, of_apply, or_comm (a := j = 5)]
      split_ifs
      · exact hA i j
      · ring
    have : A = Ah + Am := by
      ext i j; simp only [Ah, Am, Matrix.add_apply, of_apply]; split_ifs <;> simp
    rw [this]
    exact Submodule.add_mem_sup hAh hAm

/-! ## Rows C1–C3: the grading -/

/-- **Row C1.** `[𝔥, 𝔥] ⊂ 𝔥`. -/
theorem al_hh {A B : Matrix (Fin 6) (Fin 6) ℝ} (hA : A ∈ al_h) (hB : B ∈ al_h) : A * B - B * A ∈ al_h := by
  have hs := (al_so_bracket (al_direct_sum.1 hA) (al_direct_sum.1 hB)).1
  obtain ⟨-, hA⟩ := al_mem_h.1 hA
  obtain ⟨-, hB⟩ := al_mem_h.1 hB
  refine al_mem_h.2 ⟨hs, fun i => ⟨?_, ?_⟩⟩ <;>
    simp [Matrix.sub_apply, Matrix.mul_apply, (hA _).1, (hA _).2, (hB _).1, (hB _).2]

/-- **Row C2.** `[𝔥, 𝔪] ⊂ 𝔪`. -/
theorem al_hm {A B : Matrix (Fin 6) (Fin 6) ℝ} (hA : A ∈ al_h) (hB : B ∈ al_m) : A * B - B * A ∈ al_m := by
  have hs := (al_so_bracket (al_direct_sum.1 hA) (al_direct_sum.2.1 hB)).1
  obtain ⟨-, hA⟩ := al_mem_h.1 hA
  obtain ⟨-, hB⟩ := al_mem_m.1 hB
  refine al_mem_m.2 ⟨hs, fun i j hi hj => ?_⟩
  rw [Matrix.sub_apply, Matrix.mul_apply, Matrix.mul_apply, ← Finset.sum_sub_distrib]
  refine Finset.sum_eq_zero fun k _ => ?_
  by_cases hk : k = 5
  · subst hk; rw [(hA i).1, (hA j).2]; ring
  · rw [hB k j hk hj, hB i k hi hk]; ring

/-- **Row C3.** `[𝔪, 𝔪] ⊂ 𝔥`: two boosts bracket into the isotropy. -/
theorem al_mm {A B : Matrix (Fin 6) (Fin 6) ℝ} (hA : A ∈ al_m) (hB : B ∈ al_m) : A * B - B * A ∈ al_h := by
  have hs := (al_so_bracket (al_direct_sum.2.1 hA) (al_direct_sum.2.1 hB)).1
  obtain ⟨hAs, hA⟩ := al_mem_m.1 hA
  obtain ⟨hBs, hB⟩ := al_mem_m.1 hB
  have hA5 := al_skew_diag hAs 5
  have hB5 := al_skew_diag hBs 5
  have key : ∀ i, (A * B - B * A) i 5 = 0 := by
    intro i
    rw [Matrix.sub_apply, Matrix.mul_apply, Matrix.mul_apply, ← Finset.sum_sub_distrib]
    refine Finset.sum_eq_zero fun k _ => ?_
    by_cases hi : i = 5
    · subst hi
      by_cases hk : k = 5
      · subst hk; rw [hA5, hB5]; ring
      · rw [al_skew_swap hAs 5 k, al_skew_swap hBs 5 k, al_s5]; ring
    · by_cases hk : k = 5
      · subst hk; rw [hA5, hB5]; ring
      · rw [hA i k hi hk, hB i k hi hk]; ring
  refine al_mem_h.2 ⟨hs, fun i => ⟨key i, ?_⟩⟩
  rw [al_skew_swap hs i 5, key i]; ring

/-! ## Row C4: `𝔪` is not a subalgebra -/

/-- The generators `(M_μν)^ρ_σ = δ^ρ_μ η_νσ − δ^ρ_ν η_μσ`. -/
def al_M (μ ν : Fin 6) : Matrix (Fin 6) (Fin 6) ℝ :=
  of fun ρ σ => (if ρ = μ ∧ σ = ν then al_s ν else 0) - (if ρ = ν ∧ σ = μ then al_s μ else 0)

lemma al_M_skew (μ ν : Fin 6) : al_skew (al_M μ ν) := by
  intro i j
  simp only [al_M, of_apply, and_comm (a := j = μ), and_comm (a := j = ν)]
  by_cases hP : i = ν ∧ j = μ <;> by_cases hQ : i = μ ∧ j = ν
  · simp only [eq_true hP, eq_true hQ, ↓reduceIte]
    obtain ⟨rfl, rfl⟩ := hP; obtain ⟨rfl, -⟩ := hQ; ring
  · simp only [eq_true hP, eq_false hQ, ↓reduceIte]
    obtain ⟨rfl, rfl⟩ := hP; ring
  · simp only [eq_false hP, eq_true hQ, ↓reduceIte]
    obtain ⟨rfl, rfl⟩ := hQ; ring
  · simp only [eq_false hP, eq_false hQ, ↓reduceIte]; ring

lemma al_M_mem_h {μ ν : Fin 6} (hμ : μ ≠ 5) (hν : ν ≠ 5) : al_M μ ν ∈ al_h :=
  al_mem_h.2 ⟨al_M_skew μ ν, fun i => ⟨by simp [al_M, Ne.symm hμ, Ne.symm hν], by simp [al_M, Ne.symm hμ, Ne.symm hν]⟩⟩

lemma al_M_mem_m (a : Fin 6) : al_M a 5 ∈ al_m :=
  al_mem_m.2 ⟨al_M_skew a 5, fun i j hi hj => by simp [al_M, hi, hj]⟩

/-- **Row C4.** `𝔪` is not a subalgebra: `M₀₅, M₁₅ ∈ 𝔪` and `[M₀₅, M₁₅] = −M₀₁`, a nonzero element of `𝔥`, so not
of `𝔪`. -/
theorem al_m_not_closed :
    al_M 0 5 ∈ al_m ∧ al_M 1 5 ∈ al_m ∧ al_M 0 5 * al_M 1 5 - al_M 1 5 * al_M 0 5 = -al_M 0 1 ∧
      al_M 0 1 ∈ al_h ∧ al_M 0 1 ≠ 0 ∧ al_M 0 5 * al_M 1 5 - al_M 1 5 * al_M 0 5 ∉ al_m := by
  have hbr : al_M 0 5 * al_M 1 5 - al_M 1 5 * al_M 0 5 = -al_M 0 1 := by
    ext i j
    fin_cases i <;> fin_cases j <;> simp [al_M, al_s, Matrix.mul_apply]
  have h01 : al_M 0 1 0 1 = 1 := by simp [al_M, al_s]
  refine ⟨al_M_mem_m 0, al_M_mem_m 1, hbr, al_M_mem_h (by decide) (by decide),
    fun h => by simp [h] at h01, fun h => ?_⟩
  have := (al_mem_m.1 h).2 0 1 (by decide) (by decide)
  rw [hbr, Matrix.neg_apply, h01] at this
  norm_num at this

/-! ## Row C5: the count `10 + 5 = 15` -/

/-- The above-diagonal index pairs allowed by a pattern `P`. -/
abbrev al_idx (P : Fin 6 → Fin 6 → Prop) [∀ i j, Decidable (P i j)] := {p : Fin 6 × Fin 6 // p.1 < p.2 ∧ P p.1 p.2}

/-- The matrix with prescribed above-diagonal entries on the pattern, extended to an element of `so(5,1)`. -/
def al_fill (P : Fin 6 → Fin 6 → Prop) [∀ i j, Decidable (P i j)] (c : al_idx P → ℝ) :
    Matrix (Fin 6) (Fin 6) ℝ :=
  of fun i j => if h : i < j ∧ P i j then c ⟨(i, j), h⟩
    else if h' : j < i ∧ P j i then -(al_s i * al_s j * c ⟨(j, i), h'⟩) else 0

lemma al_fill_mem (P : Fin 6 → Fin 6 → Prop) [∀ i j, Decidable (P i j)] (c : al_idx P → ℝ) :
    al_fill P c ∈ al_S P := by
  refine ⟨fun i j => ?_, fun i j hij hP => ?_⟩
  · simp only [al_fill, of_apply]
    rcases lt_trichotomy i j with hij | rfl | hij
    · have n1 : ¬ j < i := not_lt_of_gt hij
      by_cases hP : P i j
      · simp only [n1, hP, hij, and_self, false_and, ↓reduceDIte]
        linear_combination (-(al_s i * c ⟨(i, j), ⟨hij, hP⟩⟩)) * al_s_sq j
      · simp [n1, hP]
    · simp
    · have n1 : ¬ i < j := not_lt_of_gt hij
      by_cases hP : P j i
      · simp only [n1, hP, hij, and_self, false_and, ↓reduceDIte]
        linear_combination (-(al_s j * c ⟨(j, i), ⟨hij, hP⟩⟩)) * al_s_sq i
      · simp [n1, hP]
  · simp [al_fill, hP, not_lt_of_gt hij]

/-- The coordinates of the pattern subspace are its allowed above-diagonal entries. -/
def al_coord (P : Fin 6 → Fin 6 → Prop) [∀ i j, Decidable (P i j)] : al_S P ≃ₗ[ℝ] (al_idx P → ℝ) where
  toFun A p := (A : Matrix (Fin 6) (Fin 6) ℝ) p.1.1 p.1.2
  map_add' A B := rfl
  map_smul' c A := rfl
  invFun c := ⟨al_fill P c, al_fill_mem P c⟩
  left_inv := by
    rintro ⟨A, hA, hA'⟩
    ext i j
    simp only [al_fill, of_apply]
    rcases lt_trichotomy i j with hij | rfl | hij
    · by_cases hP : P i j
      · simp [hij, hP]
      · simp [hP, not_lt_of_gt hij, hA' i j hij hP]
    · simp [al_skew_diag hA i]
    · have n1 : ¬ i < j := not_lt_of_gt hij
      by_cases hP : P j i
      · simp only [n1, hP, hij, and_self, false_and, ↓reduceDIte]
        rw [al_skew_swap hA j i]; ring
      · simp only [n1, hP, false_and, and_false, ↓reduceDIte]
        rw [al_skew_swap hA j i, hA' j i hij hP]; ring
  right_inv c := by
    funext p
    simp [al_fill, p.2]

/-- **Row C5.** `dim so(5,1) = 15`, `dim 𝔥 = 10`, `dim 𝔪 = 5`: the symmetric-space split is `10 + 5 = 15`. -/
theorem al_dims :
    Module.finrank ℝ al_so = 15 ∧ Module.finrank ℝ al_h = 10 ∧ Module.finrank ℝ al_m = 5 := by
  refine ⟨?_, ?_, ?_⟩
  · rw [al_so, LinearEquiv.finrank_eq (al_coord _), Module.finrank_fintype_fun_eq_card]; decide
  · rw [al_h, LinearEquiv.finrank_eq (al_coord _), Module.finrank_fintype_fun_eq_card]; decide
  · rw [al_m, LinearEquiv.finrank_eq (al_coord _), Module.finrank_fintype_fun_eq_card]; decide

/-! ## Non-vacuity -/

/-- **Witnesses.** The generators place as the paper says: `M_ab` (`a, b ≤ 4`) in `𝔥`, `M_a5` in `𝔪`, each nonzero for
`a ≠ b` (here `M₀₁`, `M₀₅`); and the C4 bracket is a nonzero element of `𝔥`. -/
theorem al_witness :
    al_M 0 1 ∈ al_h ∧ al_M 0 1 ≠ 0 ∧ al_M 0 5 ∈ al_m ∧ al_M 0 5 ≠ 0 ∧
      al_M 0 5 * al_M 1 5 - al_M 1 5 * al_M 0 5 ∈ al_h ∧ al_M 0 5 * al_M 1 5 - al_M 1 5 * al_M 0 5 ≠ 0 := by
  obtain ⟨h05, h15, hbr, h01, hne, -⟩ := al_m_not_closed
  refine ⟨h01, hne, h05, fun h => ?_, al_mm h05 h15, by rw [hbr]; exact neg_ne_zero.2 hne⟩
  have := congrFun (congrFun h 0) 5
  simp [al_M, al_s] at this

end ShadowProbe.AlgebroidProbe

#print axioms ShadowProbe.AlgebroidProbe.al_skew_iff
#print axioms ShadowProbe.AlgebroidProbe.al_mem_h
#print axioms ShadowProbe.AlgebroidProbe.al_mem_m
#print axioms ShadowProbe.AlgebroidProbe.al_so_bracket
#print axioms ShadowProbe.AlgebroidProbe.al_direct_sum
#print axioms ShadowProbe.AlgebroidProbe.al_hh
#print axioms ShadowProbe.AlgebroidProbe.al_hm
#print axioms ShadowProbe.AlgebroidProbe.al_mm
#print axioms ShadowProbe.AlgebroidProbe.al_M_skew
#print axioms ShadowProbe.AlgebroidProbe.al_M_mem_h
#print axioms ShadowProbe.AlgebroidProbe.al_M_mem_m
#print axioms ShadowProbe.AlgebroidProbe.al_m_not_closed
#print axioms ShadowProbe.AlgebroidProbe.al_dims
#print axioms ShadowProbe.AlgebroidProbe.al_witness

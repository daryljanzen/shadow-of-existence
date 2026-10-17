import ShadowEngine

/-! # Campaign 28 (`r7443+71`): row 59's rank 8, the derivative sector's pointwise dimension

The receipt (`P10_the_algebraic_quartic_is_settled_by_…_eight.py`, section D) counts the independent pointwise
invariants of the form `∇h ∇h h h` on the three-sphere's transverse-traceless jets. It finds ***eight***, taken as the
rank of a value matrix on random jets.

- `h` is a symmetric traceless `3 × 3` matrix, parametrised by `a : Fin 5 → ℚ`.
- `∇h` is `G p r s`: symmetric and traceless in `r s`, and divergence-free (`Σ_p G p p s = 0`), parametrised by its
  `12` free entries `v : Fin 12 → ℚ`. The other six are solved from the conditions.
- `gp_admissible` and `gp_onto` show this is exactly the admissible jet space, so a statement on `(a, v)` is a
  statement on the jets.
- The receipt's `372` matchings give `13` distinct polynomials (sympy bookkeeping, registered as not built here).
  `I0`–`I12` are one matching from each class, written as the index sum it is.
- `sector_rank_eight`: their `ℚ`-span, as functions of the jet, has `finrank` exactly `8`.
  - Lower bound: classes `0, 1, 2, 4, 5, 6, 7, 10` are linearly independent, by evaluation at eight jets.
  - Upper bound: the other five are rational combinations of those eight (`rel3`, …, `rel12`). -/

namespace ShadowProbe

namespace R59Rank

open Finset

/-- the symmetric traceless `h`, in five coordinates -/
def hp (a : Fin 5 → ℚ) : Fin 3 → Fin 3 → ℚ :=
  ![![a 0, a 2, a 3], ![a 2, a 1, a 4], ![a 3, a 4, -a 0 - a 1]]

/-- the admissible one-jet `G p r s`, in its twelve free entries (the receipt's nullspace, solved) -/
def gp (v : Fin 12 → ℚ) : Fin 3 → Fin 3 → Fin 3 → ℚ :=
  ![![![(-v 8 - v 2), (-v 10 - v 4), (-v 5 - v 11)], ![(-v 10 - v 4), (v 8 + v 2 - v 1), (v 0)], ![(-v 5 - v 11), (v 0), (v 1)]], ![![(-v 6 - v 4), (v 2), (v 3)], ![(v 2), (v 4), (v 5)], ![(v 3), (v 5), (v 6)]], ![![(-v 9 - v 11), (v 7), (v 8)], ![(v 7), (v 9), (v 10)], ![(v 8), (v 10), (v 11)]]]

/-- the twelve free entries of a jet -/
def gfree (G : Fin 3 → Fin 3 → Fin 3 → ℚ) : Fin 12 → ℚ :=
  ![G 0 1 2, G 0 2 2, G 1 0 1, G 1 0 2, G 1 1 1, G 1 1 2, G 1 2 2, G 2 0 1, G 2 0 2, G 2 1 1, G 2 1 2, G 2 2 2]

/-- the parametrised `h` is symmetric and traceless -/
theorem hp_admissible (a : Fin 5 → ℚ) :
    (∀ r s, hp a r s = hp a s r) ∧ ∑ k, hp a k k = 0 := by
  refine ⟨fun r s => ?_, ?_⟩
  · fin_cases r <;> fin_cases s <;> simp [hp]
  · simp [hp, Fin.sum_univ_three]

/-- and every symmetric traceless `h` is one of them -/
theorem hp_onto (H : Fin 3 → Fin 3 → ℚ) (hs : ∀ r s, H r s = H s r) (ht : ∑ k, H k k = 0) :
    H = hp ![H 0 0, H 1 1, H 0 1, H 0 2, H 1 2] := by
  simp only [Fin.sum_univ_three] at ht
  funext r s
  have := hs 0 1; have := hs 0 2; have := hs 1 2
  fin_cases r <;> fin_cases s <;> simp [hp] <;> linarith

/-- the parametrised jet is symmetric and traceless in its last two slots, and divergence-free -/
theorem gp_admissible (v : Fin 12 → ℚ) :
    (∀ p r s, gp v p r s = gp v p s r) ∧ (∀ p, ∑ k, gp v p k k = 0) ∧ (∀ s, ∑ p, gp v p p s = 0) := by
  refine ⟨fun p r s => ?_, fun p => ?_, fun s => ?_⟩
  · fin_cases p <;> fin_cases r <;> fin_cases s <;> simp [gp]
  · fin_cases p <;> simp [gp, Fin.sum_univ_three] <;> ring
  · fin_cases s <;> simp [gp, Fin.sum_univ_three]
    ring

/-- ⛭ and every admissible jet is the parametrisation of its own free entries -/
theorem gp_onto (G : Fin 3 → Fin 3 → Fin 3 → ℚ) (hs : ∀ p r s, G p r s = G p s r)
    (ht : ∀ p, ∑ k, G p k k = 0) (hd : ∀ s, ∑ p, G p p s = 0) : G = gp (gfree G) := by
  have t0 := ht 0; have t1 := ht 1; have t2 := ht 2
  have d0 := hd 0; have d1 := hd 1; have d2 := hd 2
  simp only [Fin.sum_univ_three] at t0 t1 t2 d0 d1 d2
  have := hs 0 0 1; have := hs 0 0 2; have := hs 0 1 2; have := hs 1 0 1; have := hs 1 0 2
  have := hs 1 1 2; have := hs 2 0 1; have := hs 2 0 2; have := hs 2 1 2
  funext p r s
  fin_cases p <;> fin_cases r <;> fin_cases s <;> simp [gp, gfree] <;> linarith

/-- class 0: matching [(0, 3), (1, 4), (2, 5), (6, 8), (7, 9)] -/
def I0 (a : Fin 5 → ℚ) (v : Fin 12 → ℚ) : ℚ :=
  ∑ i, ∑ j, ∑ k, ∑ l, ∑ m, gp v i j k * gp v i j k * hp a l m * hp a l m

/-- class 1: matching [(0, 3), (1, 4), (2, 6), (5, 8), (7, 9)] -/
def I1 (a : Fin 5 → ℚ) (v : Fin 12 → ℚ) : ℚ :=
  ∑ i, ∑ j, ∑ k, ∑ l, ∑ m, gp v i j k * gp v i j l * hp a k m * hp a l m

/-- class 2: matching [(0, 3), (1, 6), (2, 7), (4, 8), (5, 9)] -/
def I2 (a : Fin 5 → ℚ) (v : Fin 12 → ℚ) : ℚ :=
  ∑ i, ∑ j, ∑ k, ∑ l, ∑ m, gp v i j k * gp v i l m * hp a j k * hp a l m

/-- class 3: matching [(0, 3), (1, 6), (2, 8), (4, 7), (5, 9)] -/
def I3 (a : Fin 5 → ℚ) (v : Fin 12 → ℚ) : ℚ :=
  ∑ i, ∑ j, ∑ k, ∑ l, ∑ m, gp v i j k * gp v i l m * hp a j l * hp a k m

/-- class 4: matching [(0, 4), (1, 3), (2, 5), (6, 8), (7, 9)] -/
def I4 (a : Fin 5 → ℚ) (v : Fin 12 → ℚ) : ℚ :=
  ∑ i, ∑ j, ∑ k, ∑ l, ∑ m, gp v i j k * gp v j i k * hp a l m * hp a l m

/-- class 5: matching [(0, 4), (1, 3), (2, 6), (5, 8), (7, 9)] -/
def I5 (a : Fin 5 → ℚ) (v : Fin 12 → ℚ) : ℚ :=
  ∑ i, ∑ j, ∑ k, ∑ l, ∑ m, gp v i j k * gp v j i l * hp a k m * hp a l m

/-- class 6: matching [(0, 4), (1, 5), (2, 6), (3, 8), (7, 9)] -/
def I6 (a : Fin 5 → ℚ) (v : Fin 12 → ℚ) : ℚ :=
  ∑ i, ∑ j, ∑ k, ∑ l, ∑ m, gp v i j k * gp v l i j * hp a k m * hp a l m

/-- class 7: matching [(0, 4), (1, 6), (2, 7), (3, 8), (5, 9)] -/
def I7 (a : Fin 5 → ℚ) (v : Fin 12 → ℚ) : ℚ :=
  ∑ i, ∑ j, ∑ k, ∑ l, ∑ m, gp v i j k * gp v l i m * hp a j k * hp a l m

/-- class 8: matching [(0, 4), (1, 6), (2, 8), (3, 7), (5, 9)] -/
def I8 (a : Fin 5 → ℚ) (v : Fin 12 → ℚ) : ℚ :=
  ∑ i, ∑ j, ∑ k, ∑ l, ∑ m, gp v i j k * gp v l i m * hp a j l * hp a k m

/-- class 9: matching [(0, 6), (1, 4), (2, 5), (3, 8), (7, 9)] -/
def I9 (a : Fin 5 → ℚ) (v : Fin 12 → ℚ) : ℚ :=
  ∑ i, ∑ j, ∑ k, ∑ l, ∑ m, gp v i j k * gp v l j k * hp a i m * hp a l m

/-- class 10: matching [(0, 6), (1, 4), (2, 7), (3, 8), (5, 9)] -/
def I10 (a : Fin 5 → ℚ) (v : Fin 12 → ℚ) : ℚ :=
  ∑ i, ∑ j, ∑ k, ∑ l, ∑ m, gp v i j k * gp v l j m * hp a i k * hp a l m

/-- class 11: matching [(0, 6), (1, 4), (2, 8), (3, 7), (5, 9)] -/
def I11 (a : Fin 5 → ℚ) (v : Fin 12 → ℚ) : ℚ :=
  ∑ i, ∑ j, ∑ k, ∑ l, ∑ m, gp v i j k * gp v l j m * hp a i l * hp a k m

/-- class 12: matching [(0, 6), (1, 4), (2, 8), (3, 9), (5, 7)] -/
def I12 (a : Fin 5 → ℚ) (v : Fin 12 → ℚ) : ℚ :=
  ∑ i, ∑ j, ∑ k, ∑ l, ∑ m, gp v i j k * gp v l j m * hp a i m * hp a k l

/-- the expansion every identity below runs on -/
macro "expand" : tactic => `(tactic| simp only [I0, I1, I2, I3, I4, I5, I6, I7, I8, I9, I10, I11, I12,
  Fin.sum_univ_three, hp, gp, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two,
  Matrix.head_cons, Matrix.tail_cons])

set_option maxHeartbeats 8000000

theorem rel3 (a : Fin 5 → ℚ) (v : Fin 12 → ℚ) : I3 a v = 1/2 * I0 a v - 2 * I1 a v + I2 a v := by
  expand; ring

theorem rel8 (a : Fin 5 → ℚ) (v : Fin 12 → ℚ) :
    I8 a v = 1/2 * I4 a v - I5 a v - I6 a v + I7 a v := by
  expand; ring

theorem rel9 (a : Fin 5 → ℚ) (v : Fin 12 → ℚ) :
    I9 a v = I0 a v - 2 * I1 a v - I4 a v + I5 a v + 2 * I6 a v := by
  expand; ring

theorem rel11 (a : Fin 5 → ℚ) (v : Fin 12 → ℚ) :
    I11 a v = -1/2 * I0 a v + I1 a v + I4 a v - I5 a v - 2 * I6 a v + I10 a v := by
  expand; ring

theorem rel12 (a : Fin 5 → ℚ) (v : Fin 12 → ℚ) :
    I12 a v = 1/2 * I4 a v - 2 * I6 a v + I10 a v := by
  expand; ring

/-- the thirteen classes, as functions of the jet -/
def sector : Fin 13 → ((Fin 5 → ℚ) × (Fin 12 → ℚ) → ℚ) :=
  ![fun x => I0 x.1 x.2, fun x => I1 x.1 x.2, fun x => I2 x.1 x.2, fun x => I3 x.1 x.2,
    fun x => I4 x.1 x.2, fun x => I5 x.1 x.2, fun x => I6 x.1 x.2, fun x => I7 x.1 x.2,
    fun x => I8 x.1 x.2, fun x => I9 x.1 x.2, fun x => I10 x.1 x.2, fun x => I11 x.1 x.2,
    fun x => I12 x.1 x.2]

/-- the eight that carry the sector -/
def bidx : Fin 8 → Fin 13 := ![0, 1, 2, 4, 5, 6, 7, 10]

/-- ⛭ the lower bound: the eight are linearly independent, read off eight jets with entries in `{-1, 0, 1}`.
The `8 × 8` value matrix (rows the jets, columns the classes `0 1 2 4 5 6 7 10`) is non-singular:
  jet 0: [24, 8, 4, -8, -2, -3, -2, 2]
  jet 1: [16, 6, 0, 8, 4, 2, 0, 1]
  jet 2: [24, 9, 5, 0, 2, -1, -1, 2]
  jet 3: [24, 7, 0, 8, 2, 2, 0, 3]
  jet 4: [24, 8, 4, 8, 2, 3, 0, 2]
  jet 5: [24, 8, 8, 8, 2, 3, 2, 2]
  jet 6: [24, 8, 0, 0, 2, 0, 0, 6]
  jet 7: [20, 10, 12, 16, 8, 8, 8, 8] -/
theorem basis_independent : LinearIndependent ℚ (fun i => sector (bidx i)) := by
  rw [Fintype.linearIndependent_iff]
  intro c hc
  have e : ∀ x, ∑ i, c i * sector (bidx i) x = 0 := fun x => by
    simpa using congrFun hc x
  have e0 := e (![0, 0, 1, -1, 0], ![-1, 0, 0, 0, 0, 0, 0, 1, 0, -1, 0, 0])
  have e1 := e (![1, -1, 0, 0, 0], ![0, 0, 0, -1, 0, 0, 0, -1, 0, 0, -1, 0])
  have e2 := e (![0, -1, -1, 0, 0], ![-1, -1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0])
  have e3 := e (![0, 0, -1, 0, -1], ![0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, -1])
  have e4 := e (![-1, 0, 0, 0, -1], ![0, 0, 1, 0, 0, 0, 1, 0, -1, 0, 0, 0])
  have e5 := e (![0, 0, 1, -1, 0], ![0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 1])
  have e6 := e (![0, 0, -1, -1, 0], ![0, -1, 0, 0, 0, 0, -1, 0, 0, -1, 0, 0])
  have e7 := e (![1, -1, 0, 0, 0], ![0, 0, -1, 0, 1, 0, 0, 0, 0, -1, 0, 0])
  norm_num [Fin.sum_univ_eight, sector, bidx, I0, I1, I2, I4, I5, I6, I7, I10, Fin.sum_univ_three, hp, gp]
    at e0 e1 e2 e3 e4 e5 e6 e7
  intro i
  fin_cases i <;> simp <;> linarith

/-- ⛭⛭ THE RANK: the span of the thirteen classes has dimension exactly eight -/
theorem sector_rank_eight : Module.finrank ℚ (Submodule.span ℚ (Set.range sector)) = 8 := by
  have hspan : Submodule.span ℚ (Set.range sector) = Submodule.span ℚ (Set.range (sector ∘ bidx)) := by
    apply le_antisymm
    · rw [Submodule.span_le]
      rintro _ ⟨j, rfl⟩
      have hb : ∀ i, sector (bidx i) ∈ Submodule.span ℚ (Set.range (sector ∘ bidx)) :=
        fun i => Submodule.subset_span ⟨i, rfl⟩
      have comb : ∀ (c : Fin 8 → ℚ) (f : (Fin 5 → ℚ) × (Fin 12 → ℚ) → ℚ),
          (∀ x, f x = ∑ i, c i * sector (bidx i) x) →
          f ∈ Submodule.span ℚ (Set.range (sector ∘ bidx)) := by
        intro c f hf
        rw [Submodule.mem_span_range_iff_exists_fun]
        exact ⟨c, funext fun x => by simp [hf]⟩
      fin_cases j
      · exact hb 0
      · exact hb 1
      · exact hb 2
      · exact comb ![1/2, -2, 1, 0, 0, 0, 0, 0] _ fun x => by
          simp [Fin.sum_univ_eight, sector, bidx, rel3]; ring
      · exact hb 3
      · exact hb 4
      · exact hb 5
      · exact hb 6
      · exact comb ![0, 0, 0, 1/2, -1, -1, 1, 0] _ fun x => by
          simp [Fin.sum_univ_eight, sector, bidx, rel8]; ring
      · exact comb ![1, -2, 0, -1, 1, 2, 0, 0] _ fun x => by
          simp [Fin.sum_univ_eight, sector, bidx, rel9]; ring
      · exact hb 7
      · exact comb ![-1/2, 1, 0, 1, -1, -2, 0, 1] _ fun x => by
          simp [Fin.sum_univ_eight, sector, bidx, rel11]; ring
      · exact comb ![0, 0, 0, 1/2, 0, -2, 0, 1] _ fun x => by
          simp [Fin.sum_univ_eight, sector, bidx, rel12]; ring
    · exact Submodule.span_mono (Set.range_comp_subset_range _ _)
  rw [hspan, show Set.range (sector ∘ bidx) = Set.range (fun i => sector (bidx i)) from rfl,
    finrank_span_eq_card basis_independent]
  simp

end R59Rank

end ShadowProbe

#print axioms ShadowProbe.R59Rank.gp_onto
#print axioms ShadowProbe.R59Rank.hp_onto
#print axioms ShadowProbe.R59Rank.basis_independent
#print axioms ShadowProbe.R59Rank.sector_rank_eight

import ShadowEngine
import Mathlib.RingTheory.RootsOfUnity.Complex
import Mathlib.Tactic.ComputeDegree
import Mathlib.FieldTheory.IsAlgClosed.Basic
import Mathlib.Analysis.Complex.Polynomial.Basic
import Mathlib.LinearAlgebra.Matrix.Rank

/-! # Campaign 46 (`r7443+71.37`), the quadric/flow group of LIMIT rows: 9, 10, 106, 91, 97, 26, 40

Each row is built to the COMPUTED checks of its receipt (ROWS.tsv column 6); text pins and symbol-occurrence checks
are excepted, as for every DONE row. Imported from `ShadowEngine`: `sinh23_flow`, `unruh_ds_limits`,
`ds_surface_gravity`, `ds_horizon_iff` (through it), `fNar`. Copied (probes cannot import probes):
`section_quadric` (`HigherDim.lean`), `sds_kretschmann` with `cK`, `kR` (`CurvatureInstances.lean`), `cL3` and
`sin2_at'` (`Row79Leaf.lean`).

- **9** (`E50`): the orthogonal split for every `D ≥ 1`, instances `D = 5..8`; the rank-1 Jacobian of
  `α_eff = √(α_top² − c₂²)` and its fibre; the slicing cubic `u − u³ = m` of degree 3 with 3 roots over `ℂ`.
- **10** (`E52`): the spacelike, timelike and null sections of `−X₀² + ΣXᵢ²` for every `D`, with the receipt's
  coefficient reads as coefficients of one-variable polynomials; instances `D = 5, 6`.
- **106** (`P17`): `X₀ ↦ iX₀` over `ℂ`; the invariants and `d ln v/d ln α ∈ {−2, −4, −4}`; and (beyond the receipt,
  which types the invariants in) the invariants derived from the constant-curvature array that
  `dS5_constant_curvature` proves.
- **91** (`I11/I1`): from `sinh23_flow`; `V_eff = 1 ⇔ M = −r³/(2α²)`; the turnaround root; I1's two derivatives.
- **26** (`P1`): the four-row table is the receipt's DEFINITION; `κ`, `T(a)` and its limits from the imported
  theorems; the Nariai `κ = 0`.
- **40** (`P03`): the marginal first integral for EVERY `D ≥ 3` (instances `D = 4..8`), generalising `sinh23_flow`;
  the deck shift over `ℂ`; the primitive 7th root at `D = 8`; the degree-5 numerator at `D = 6`. The deck group
  `Z_{D−1}` is NOT claimed.
- **97** (`P15`): §A the layer identity; §B Ricci of `ℝ × S²` and `S³` under THE connection; §C the Kretschmann
  closed form, its `r_s`-free excess and limit, and the six receipt points as instances. ⚠ §C's Kretschmann is THE
  connection's in SdS's STATIC chart (`sds_kretschmann`), evaluated on the worldline; the receipt computes it in
  the reassigned (proper-frame) chart. That the two charts carry the same scalar is not built here. -/

open Real Filter Topology Bundle Manifold Set VectorField
open scoped ContDiff Manifold

namespace ShadowProbe.LimitQuadricFlow

/-! ## Row 9 -/


section Row9

/-- `section_quadric` (row 108, `HigherDim.lean`), copied: the split identity under any symmetric `η`. -/
theorem split_identity {E : Type*} [AddCommGroup E] [Module ℝ E] (η : E →ₗ[ℝ] E →ₗ[ℝ] ℝ)
    (hs : ∀ x y, η x y = η y x) (n Y : E) (hn : η n n = 1) (hY : η n Y = 0) (c : ℝ) :
    η (c • n + Y) (c • n + Y) - η Y Y - c ^ 2 = 0 := by
  simp only [map_add, map_smul, LinearMap.add_apply, LinearMap.smul_apply, smul_eq_mul, hn, hY, hs Y n]
  ring

/-- `section_quadric` (row 108), copied. -/
theorem section_quadric {E : Type*} [AddCommGroup E] [Module ℝ E] (η : E →ₗ[ℝ] E →ₗ[ℝ] ℝ)
    (hs : ∀ x y, η x y = η y x) (n Y : E) (hn : η n n = 1) (hY : η n Y = 0) (c α : ℝ) :
    η (c • n + Y) (c • n + Y) = α ^ 2 ↔ η Y Y = α ^ 2 - c ^ 2 := by
  have := split_identity η hs n Y hn hY c
  constructor <;> intro h <;> linarith

/-- The Minkowski signs of `ℝ^{1,D}`. -/
def sgn {D : ℕ} (i : Fin (D + 1)) : ℝ := if i = 0 then -1 else 1

/-- `η = −dX₀² + dX₁² + … + dX_D²` on `ℝ^{D+1}`. -/
noncomputable def eta (D : ℕ) : (Fin (D + 1) → ℝ) →ₗ[ℝ] (Fin (D + 1) → ℝ) →ₗ[ℝ] ℝ :=
  LinearMap.mk₂ ℝ (fun x y => ∑ i, sgn i * x i * y i)
    (fun x x' y => by
      simp only [Pi.add_apply, ← Finset.sum_add_distrib]; exact Finset.sum_congr rfl fun i _ => by ring)
    (fun c x y => by
      simp only [Pi.smul_apply, smul_eq_mul, Finset.mul_sum]; exact Finset.sum_congr rfl fun i _ => by ring)
    (fun x y y' => by
      simp only [Pi.add_apply, ← Finset.sum_add_distrib]; exact Finset.sum_congr rfl fun i _ => by ring)
    (fun c x y => by
      simp only [Pi.smul_apply, smul_eq_mul, Finset.mul_sum]; exact Finset.sum_congr rfl fun i _ => by ring)

lemma eta_apply {D : ℕ} (x y : Fin (D + 1) → ℝ) : eta D x y = ∑ i, sgn i * x i * y i := rfl

/-- **Row 9, the orthogonal split at every `D ≥ 1`.** With `n = e_D` (spacelike, `η(n,n) = 1`) and `Y ⟂ n`,
`η(cn + Y, cn + Y) − η(Y,Y) − c² = 0`, so the section is `η(Y,Y) = α² − c²`. -/
theorem eta_split (D : ℕ) (hD : 1 ≤ D) (Y : Fin (D + 1) → ℝ) (hY : Y (Fin.last D) = 0) (c α : ℝ) :
    eta D (Pi.single (Fin.last D) 1) (Pi.single (Fin.last D) 1) = 1
    ∧ eta D (c • Pi.single (Fin.last D) 1 + Y) (c • Pi.single (Fin.last D) 1 + Y) - eta D Y Y - c ^ 2 = 0
    ∧ (eta D (c • Pi.single (Fin.last D) 1 + Y) (c • Pi.single (Fin.last D) 1 + Y) = α ^ 2
        ↔ eta D Y Y = α ^ 2 - c ^ 2) := by
  have hl : Fin.last D ≠ 0 := by rw [Ne, Fin.ext_iff]; simp; omega
  have hn : eta D (Pi.single (Fin.last D) 1) (Pi.single (Fin.last D) 1) = 1 := by
    rw [eta_apply, Finset.sum_eq_single (Fin.last D) (fun i _ hi => by simp [hi]) (by simp)]
    simp [sgn, hl]
  have hnY : eta D (Pi.single (Fin.last D) 1) Y = 0 := by
    rw [eta_apply, Finset.sum_eq_single (Fin.last D) (fun i _ hi => by simp [hi]) (by simp)]
    simp [hY]
  have hs : ∀ x y, eta D x y = eta D y x := fun x y => by
    simp only [eta_apply]; exact Finset.sum_congr rfl fun i _ => by ring
  exact ⟨hn, split_identity _ hs _ _ hn hnY c, section_quadric _ hs _ _ hn hnY c α⟩

/-- The rank-1 Jacobian: a nonzero `1 × 2` row has rank 1. -/
theorem rank_row {a b : ℝ} (h : a ≠ 0) : (!![a, b] : Matrix (Fin 1) (Fin 2) ℝ).rank = 1 := by
  apply le_antisymm
  · exact (Matrix.rank_le_card_height _).trans (by simp)
  · rw [Nat.one_le_iff_ne_zero]
    intro h0
    rw [Matrix.rank, Submodule.finrank_eq_zero] at h0
    have hm : (!![a, b] : Matrix (Fin 1) (Fin 2) ℝ).mulVecLin (Pi.single 0 1) ∈
        LinearMap.range (!![a, b] : Matrix (Fin 1) (Fin 2) ℝ).mulVecLin := LinearMap.mem_range_self _ _
    rw [h0, Submodule.mem_bot] at hm
    have := congrFun hm 0
    simp [Matrix.mulVec, dotProduct, Fin.sum_univ_two] at this
    exact h this

/-- `α_eff = √(α_top² − c₂²)`: its two partials. -/
theorem aeff_partials {aT c : ℝ} (h : 0 < aT ^ 2 - c ^ 2) :
    HasDerivAt (fun x => Real.sqrt (x ^ 2 - c ^ 2)) (aT / Real.sqrt (aT ^ 2 - c ^ 2)) aT
    ∧ HasDerivAt (fun y => Real.sqrt (aT ^ 2 - y ^ 2)) (-c / Real.sqrt (aT ^ 2 - c ^ 2)) c := by
  constructor
  · have := ((hasDerivAt_pow 2 aT).sub_const (c ^ 2)).sqrt h.ne'
    convert this using 1; field_simp; ring
  · have := ((hasDerivAt_pow 2 c).const_sub (aT ^ 2)).sqrt h.ne'
    convert this using 1; field_simp; ring

/-- The one-parameter fibre: for `c₂ > 0`, `√(α_top² − c₂²) = a_e` iff `c₂ = √(α_top² − a_e²)`. -/
theorem aeff_fibre {aT ae c : ℝ} (hae : 0 < ae) (hc : 0 < c) :
    Real.sqrt (aT ^ 2 - c ^ 2) = ae ↔ c = Real.sqrt (aT ^ 2 - ae ^ 2) := by
  constructor
  · intro h
    have hp : 0 < aT ^ 2 - c ^ 2 := by
      by_contra hn; rw [not_lt] at hn; rw [Real.sqrt_eq_zero'.2 hn] at h; linarith
    have := Real.sq_sqrt hp.le; rw [h] at this
    rw [eq_comm, Real.sqrt_eq_iff_mul_self_eq_of_pos hc]; linarith
  · intro h
    have hp : 0 < aT ^ 2 - ae ^ 2 := by
      by_contra hn; rw [not_lt] at hn; rw [Real.sqrt_eq_zero'.2 hn] at h; linarith
    have := Real.sq_sqrt hp.le; rw [← h] at this
    rw [Real.sqrt_eq_iff_mul_self_eq_of_pos hae]; linarith

open Polynomial in
/-- The slicing cubic `u − u³ = m`: degree 3, and three roots over `ℂ` for every `m`. -/
theorem slicing_cubic (m : ℂ) :
    (X - X ^ 3 - C m : ℂ[X]).natDegree = 3 ∧ (X - X ^ 3 - C m : ℂ[X]).roots.card = 3 := by
  have hd : (X - X ^ 3 - C m : ℂ[X]).natDegree = 3 := by compute_degree!
  exact ⟨hd, by rw [IsAlgClosed.card_roots_eq_natDegree, hd]⟩

/-- **Row 9, headline.** The split at `D = 5..8`; the Jacobian of `α_eff` has rank 1, with a one-parameter fibre;
the slicing cubic has degree 3 and three roots. -/
theorem row9_checks {aT c2 : ℝ} (h : 0 < aT ^ 2 - c2 ^ 2) (hat : 0 < aT) :
    (∀ D ∈ Finset.Icc 5 8, ∀ (Y : Fin (D + 1) → ℝ), Y (Fin.last D) = 0 → ∀ c : ℝ,
      eta D (c • Pi.single (Fin.last D) 1 + Y) (c • Pi.single (Fin.last D) 1 + Y) - eta D Y Y - c ^ 2 = 0)
    ∧ (!![aT / Real.sqrt (aT ^ 2 - c2 ^ 2), -c2 / Real.sqrt (aT ^ 2 - c2 ^ 2)] : Matrix (Fin 1) (Fin 2) ℝ).rank = 1
    ∧ (∀ ae c : ℝ, 0 < ae → 0 < c → (Real.sqrt (aT ^ 2 - c ^ 2) = ae ↔ c = Real.sqrt (aT ^ 2 - ae ^ 2)))
    ∧ (∀ m : ℂ, (Polynomial.X - Polynomial.X ^ 3 - Polynomial.C m : Polynomial ℂ).natDegree = 3
        ∧ (Polynomial.X - Polynomial.X ^ 3 - Polynomial.C m : Polynomial ℂ).roots.card = 3) :=
  ⟨fun D hD Y hY c => (eta_split D (by simp at hD; omega) Y hY c 0).2.1,
    rank_row (div_ne_zero hat.ne' (Real.sqrt_pos.2 h).ne'), fun _ _ ha hc => aeff_fibre ha hc, slicing_cubic⟩

end Row9

#print axioms row9_checks

/-! ## Row 10 -/

section Row10

/-- The ambient quadric `−X₀² + X₁² + … + X_D²`. -/
noncomputable def base {D : ℕ} (X : Fin (D + 1) → ℝ) : ℝ := -X 0 ^ 2 + ∑ i ∈ Finset.univ.erase 0, X i ^ 2

lemma sum_update {D : ℕ} (s : Finset (Fin (D + 1))) {j : Fin (D + 1)} (hj : j ∈ s) (X : Fin (D + 1) → ℝ) (v : ℝ) :
    ∑ i ∈ s, Function.update X j v i ^ 2 = v ^ 2 + ∑ i ∈ s.erase j, X i ^ 2 := by
  rw [← Finset.add_sum_erase s _ hj, Function.update_self]
  congr 1
  exact Finset.sum_congr rfl fun i hi => by rw [Function.update_of_ne (Finset.ne_of_mem_erase hi)]

lemma pq_neg (q t : ℝ) : (-Polynomial.X ^ 2 + Polynomial.C q : Polynomial ℝ).eval t = -t ^ 2 + q ∧
    (-Polynomial.X ^ 2 + Polynomial.C q : Polynomial ℝ).coeff 2 = -1 := by
  constructor <;> simp

lemma pq_pos (q t : ℝ) : (Polynomial.X ^ 2 + Polynomial.C q : Polynomial ℝ).eval t = t ^ 2 + q ∧
    (Polynomial.X ^ 2 + Polynomial.C q : Polynomial ℝ).coeff 2 = 1 := by
  constructor <;> simp

lemma pq_lin (b q t : ℝ) : (Polynomial.C b * Polynomial.X + Polynomial.C q : Polynomial ℝ).eval t = b * t + q ∧
    (Polynomial.C b * Polynomial.X + Polynomial.C q : Polynomial ℝ).coeff 1 = b ∧
    (Polynomial.C b * Polynomial.X + Polynomial.C q : Polynomial ℝ).coeff 2 = 0 := by
  refine ⟨by simp, ?_, ?_⟩ <;> simp [Polynomial.coeff_C]

lemma last_ne {D : ℕ} (hD : 1 ≤ D) : Fin.last D ≠ 0 := by rw [Ne, Fin.ext_iff]; simp; omega

/-- **Spacelike** (`X_D = c`): `−X₀² + X₁² + … + X_{D−1}² + c²`; as a polynomial in `X₀` its `X₀²` coefficient
is `−1`: the signature survives. -/
theorem spacelike_section (D : ℕ) (hD : 1 ≤ D) (X : Fin (D + 1) → ℝ) (c : ℝ) :
    base (Function.update X (Fin.last D) c)
      = -X 0 ^ 2 + ∑ i ∈ (Finset.univ.erase 0).erase (Fin.last D), X i ^ 2 + c ^ 2
    ∧ ∃ q : ℝ, (∀ t, base (Function.update (Function.update X 0 t) (Fin.last D) c)
        = (-Polynomial.X ^ 2 + Polynomial.C q : Polynomial ℝ).eval t)
      ∧ (-Polynomial.X ^ 2 + Polynomial.C q : Polynomial ℝ).coeff 2 = -1 := by
  have hl := last_ne hD
  have hm : Fin.last D ∈ Finset.univ.erase (0 : Fin (D + 1)) := Finset.mem_erase.2 ⟨hl, Finset.mem_univ _⟩
  have key : ∀ Z : Fin (D + 1) → ℝ, base (Function.update Z (Fin.last D) c)
      = -Z 0 ^ 2 + ∑ i ∈ (Finset.univ.erase 0).erase (Fin.last D), Z i ^ 2 + c ^ 2 := fun Z => by
    unfold base; rw [sum_update _ hm, Function.update_of_ne hl.symm]; ring
  refine ⟨key X, ∑ i ∈ (Finset.univ.erase 0).erase (Fin.last D), X i ^ 2 + c ^ 2, fun t => ?_, ?_⟩
  · rw [key]
    have : ∑ i ∈ (Finset.univ.erase 0).erase (Fin.last D), Function.update X 0 t i ^ 2
        = ∑ i ∈ (Finset.univ.erase 0).erase (Fin.last D), X i ^ 2 :=
      Finset.sum_congr rfl fun i hi => by
        rw [Function.update_of_ne (Finset.ne_of_mem_erase (Finset.mem_of_mem_erase hi))]
    rw [this, (pq_neg _ t).1, Function.update_self]; ring
  · exact (pq_neg _ 0).2

/-- **Timelike** (`X₀ = c`): `X₁² + … + X_D² − c²`, a sphere: in each `X_i`, `i ≠ 0`, the `X_i²` coefficient
is `+1`, and nothing depends on `X₀`. -/
theorem timelike_section (D : ℕ) (X : Fin (D + 1) → ℝ) (c : ℝ) :
    base (Function.update X 0 c) = ∑ i ∈ Finset.univ.erase 0, X i ^ 2 - c ^ 2
    ∧ ∀ i : Fin (D + 1), i ≠ 0 → ∃ q : ℝ, (∀ t, base (Function.update (Function.update X i t) 0 c)
        = (Polynomial.X ^ 2 + Polynomial.C q : Polynomial ℝ).eval t)
      ∧ (Polynomial.X ^ 2 + Polynomial.C q : Polynomial ℝ).coeff 2 = 1 := by
  have key : ∀ Z : Fin (D + 1) → ℝ, base (Function.update Z 0 c) = ∑ i ∈ Finset.univ.erase 0, Z i ^ 2 - c ^ 2 :=
    fun Z => by
      unfold base; rw [Function.update_self]
      rw [Finset.sum_congr rfl fun i hi => by rw [Function.update_of_ne (Finset.ne_of_mem_erase hi)]]; ring
  refine ⟨key X, fun i hi => ⟨∑ j ∈ (Finset.univ.erase 0).erase i, X j ^ 2 - c ^ 2, fun t => ?_, ?_⟩⟩
  · rw [key, sum_update _ (Finset.mem_erase.2 ⟨hi, Finset.mem_univ _⟩), (pq_pos _ t).1]; ring
  · exact (pq_pos _ 0).2

/-- **Null** (`X_D = X₀ − c`): `−2cX₀ + X₁² + … + X_{D−1}² + c²`: as a polynomial in `X₀` it has the LINEAR
coefficient `−2c` and no `X₀²` term, so it is not a quadric of the same form. -/
theorem null_section (D : ℕ) (hD : 1 ≤ D) (X : Fin (D + 1) → ℝ) (c : ℝ) :
    base (Function.update X (Fin.last D) (X 0 - c))
      = -2 * c * X 0 + ∑ i ∈ (Finset.univ.erase 0).erase (Fin.last D), X i ^ 2 + c ^ 2
    ∧ ∃ q : ℝ, (∀ t, base (Function.update (Function.update X 0 t) (Fin.last D) (t - c))
        = (Polynomial.C (-2 * c) * Polynomial.X + Polynomial.C q : Polynomial ℝ).eval t)
      ∧ (Polynomial.C (-2 * c) * Polynomial.X + Polynomial.C q : Polynomial ℝ).coeff 1 = -2 * c
      ∧ (Polynomial.C (-2 * c) * Polynomial.X + Polynomial.C q : Polynomial ℝ).coeff 2 = 0 := by
  have hl := last_ne hD
  have hm : Fin.last D ∈ Finset.univ.erase (0 : Fin (D + 1)) := Finset.mem_erase.2 ⟨hl, Finset.mem_univ _⟩
  have key : ∀ Z : Fin (D + 1) → ℝ, base (Function.update Z (Fin.last D) (Z 0 - c))
      = -2 * c * Z 0 + ∑ i ∈ (Finset.univ.erase 0).erase (Fin.last D), Z i ^ 2 + c ^ 2 := fun Z => by
    unfold base; rw [sum_update _ hm, Function.update_of_ne hl.symm]; ring
  refine ⟨key X, ∑ i ∈ (Finset.univ.erase 0).erase (Fin.last D), X i ^ 2 + c ^ 2, fun t => ?_, ?_, ?_⟩
  · have := key (Function.update X 0 t)
    simp only [Function.update_self] at this
    rw [this]
    have : ∑ i ∈ (Finset.univ.erase 0).erase (Fin.last D), Function.update X 0 t i ^ 2
        = ∑ i ∈ (Finset.univ.erase 0).erase (Fin.last D), X i ^ 2 :=
      Finset.sum_congr rfl fun i hi => by
        rw [Function.update_of_ne (Finset.ne_of_mem_erase (Finset.mem_of_mem_erase hi))]
    rw [this, (pq_lin _ _ t).1]; ring
  · exact (pq_lin _ _ 0).2.1
  · exact (pq_lin _ _ 0).2.2

/-- **Row 10, headline**, at `D = 5, 6`. -/
theorem row10_checks (c : ℝ) (hc : c ≠ 0) :
    ∀ D ∈ ({5, 6} : Finset ℕ), ∀ X : Fin (D + 1) → ℝ,
      (base (Function.update X (Fin.last D) c)
          = -X 0 ^ 2 + ∑ i ∈ (Finset.univ.erase 0).erase (Fin.last D), X i ^ 2 + c ^ 2
        ∧ ∃ q : ℝ, (∀ t, base (Function.update (Function.update X 0 t) (Fin.last D) c)
            = (-Polynomial.X ^ 2 + Polynomial.C q : Polynomial ℝ).eval t)
          ∧ (-Polynomial.X ^ 2 + Polynomial.C q : Polynomial ℝ).coeff 2 = -1)
      ∧ (∀ i : Fin (D + 1), i ≠ 0 → ∃ q : ℝ, (∀ t, base (Function.update (Function.update X i t) 0 c)
            = (Polynomial.X ^ 2 + Polynomial.C q : Polynomial ℝ).eval t)
          ∧ (Polynomial.X ^ 2 + Polynomial.C q : Polynomial ℝ).coeff 2 = 1)
      ∧ (∃ q : ℝ, (∀ t, base (Function.update (Function.update X 0 t) (Fin.last D) (t - c))
            = (Polynomial.C (-2 * c) * Polynomial.X + Polynomial.C q : Polynomial ℝ).eval t)
          ∧ (Polynomial.C (-2 * c) * Polynomial.X + Polynomial.C q : Polynomial ℝ).coeff 1 ≠ 0) := by
  intro D hD X
  have hD1 : 1 ≤ D := by simp at hD; omega
  obtain ⟨q, hq, h1, -⟩ := (null_section D hD1 X c).2
  exact ⟨spacelike_section D hD1 X c, (timelike_section D X c).2, q, hq, by rw [h1]; simpa using hc⟩

end Row10

#print axioms row10_checks

/-! ## Row 106 -/

section Row106

/-- **The Wick substitution** `X₀ ↦ iX₀` over `ℂ`: `−(iX₀)² + ΣXᵢ² = ΣXᵢ²`, in every dimension. -/
theorem wick {D : ℕ} (X : Fin (D + 1) → ℂ) :
    -(Complex.I * X 0) ^ 2 + ∑ i ∈ Finset.univ.erase 0, X i ^ 2 = ∑ i, X i ^ 2 := by
  rw [← Finset.add_sum_erase _ _ (Finset.mem_univ (0 : Fin (D + 1))), mul_pow, Complex.I_sq]; ring

/-- `d ln v/d ln α = −k` for `v = c/α^k`. -/
theorem loglog (c : ℝ) (hc : c ≠ 0) (k : ℕ) {α : ℝ} (hα : 0 < α) :
    HasDerivAt (fun a => c / a ^ (k + 1)) (-(c * ((k + 1 : ℕ) * α ^ k)) / (α ^ (k + 1)) ^ 2) α
    ∧ α * (-(c * ((k + 1 : ℕ) * α ^ k)) / (α ^ (k + 1)) ^ 2) / (c / α ^ (k + 1)) = -((k + 1 : ℕ) : ℝ) := by
  constructor
  · have := ((hasDerivAt_pow (k + 1) α).inv (pow_ne_zero _ hα.ne')).const_mul c
    convert this using 1
    · funext a; simp [div_eq_mul_inv]
    · simp only [Nat.add_sub_cancel]; ring
  · have := hα.ne'; field_simp; ring

/-- **Row 106, headline.** The Wick map carries the `dS₅` quadric to `S⁵` of the same radius; the invariants
`R = n(n−1)/α²`, `Ric² = n(n−1)²/α⁴`, `K = 2n(n−1)/α⁴` at `n = 5` are `20/α²`, `80/α⁴`, `40/α⁴`, with
`d ln v/d ln α = −2, −4, −4`, integers. -/
theorem row106_checks {α : ℝ} (hα : 0 < α) :
    (∀ X : Fin 6 → ℂ, -(Complex.I * X 0) ^ 2 + ∑ i ∈ Finset.univ.erase 0, X i ^ 2 = ∑ i, X i ^ 2)
    ∧ ((5 : ℝ) * (5 - 1) * (1 / α ^ 2) = 20 / α ^ 2 ∧ (5 : ℝ) * ((5 - 1) * (1 / α ^ 2)) ^ 2 = 80 / α ^ 4
        ∧ 2 * (5 : ℝ) * (5 - 1) * (1 / α ^ 2) ^ 2 = 40 / α ^ 4)
    ∧ (∃ v', HasDerivAt (fun a => 20 / a ^ 2) v' α ∧ α * v' / (20 / α ^ 2) = -2)
    ∧ (∃ v', HasDerivAt (fun a => 80 / a ^ 4) v' α ∧ α * v' / (80 / α ^ 4) = -4)
    ∧ (∃ v', HasDerivAt (fun a => 40 / a ^ 4) v' α ∧ α * v' / (40 / α ^ 4) = -4) := by
  refine ⟨wick, ⟨?_, ?_, ?_⟩, ⟨_, (loglog 20 (by norm_num) 1 hα).1, by simpa using (loglog 20 (by norm_num) 1 hα).2⟩,
    ⟨_, (loglog 80 (by norm_num) 3 hα).1, by simpa using (loglog 80 (by norm_num) 3 hα).2⟩,
    ⟨_, (loglog 40 (by norm_num) 3 hα).1, by simpa using (loglog 40 (by norm_num) 3 hα).2⟩⟩ <;>
    (have := hα.ne'; field_simp; ring)

end Row106

#print axioms row106_checks

/-- The constant-curvature array `R(eᵢ,eⱼ)eₖ = K(g_jk eᵢ − g_ik eⱼ)` over a diagonal `g`: the form
`dS5_constant_curvature` (row 108, `HigherDim.lean`) proves for `dS₅` with `K = H²`. -/
noncomputable def ccR {n : ℕ} (K : ℝ) (g : Fin n → ℝ) (i j k l : Fin n) : ℝ :=
  K * ((if j = k then g j else 0) * (if i = l then 1 else 0) - (if i = k then g i else 0) * (if j = l then 1 else 0))

set_option maxHeartbeats 4000000 in
/-- **Row 106, the invariants on `dS₅`.** For ANY nonzero diagonal `g` on `Fin 5`, the constant-curvature array has
`R = 20K`, `Ric² = 80K²`, `Riem² = 40K²`: `n(n−1)K`, `n(n−1)²K²`, `2n(n−1)K²` at `n = 5`. -/
theorem cc_invariants (K : ℝ) (g : Fin 5 → ℝ) (hg : ∀ i, g i ≠ 0) :
    scalCN g (ccR K g) = 20 * K ∧ ric2CN g (ccR K g) = 80 * K ^ 2 ∧ riem2CN g (ccR K g) = 40 * K ^ 2 := by
  have h0 := hg 0; have h1 := hg 1; have h2 := hg 2; have h3 := hg 3; have h4 := hg 4
  refine ⟨?_, ?_, ?_⟩
  · simp [scalCN, ricCN, ccR, Fin.sum_univ_five]; field_simp; ring
  · simp [ric2CN, ricCN, ccR, Fin.sum_univ_five]; field_simp; ring
  · simp [riem2CN, ccR, Fin.sum_univ_five]; field_simp; ring

#print axioms cc_invariants

/-! ## Row 91 -/

section Row91

lemma law_pos {M α τ : ℝ} (hM : 0 < M) (hα : 0 < α) (hτ : 0 < τ) :
    0 < (2 * M * α ^ 2 * Real.sinh (3 / (2 * α) * τ) ^ 2) ^ (1 / 3 : ℝ) := by
  have : 0 < Real.sinh (3 / (2 * α) * τ) := Real.sinh_pos_iff.2 (by positivity)
  exact Real.rpow_pos_of_pos (by positivity) _

/-- The squared first integral, from `sinh23_flow`. -/
theorem flow_sq {M α τ : ℝ} (hM : 0 < M) (hα : 0 < α) (hτ : 0 < τ) :
    deriv (fun t => (2 * M * α ^ 2 * Real.sinh (3 / (2 * α) * t) ^ 2) ^ (1 / 3 : ℝ)) τ ^ 2
      = 2 * M / (2 * M * α ^ 2 * Real.sinh (3 / (2 * α) * τ) ^ 2) ^ (1 / 3 : ℝ)
        + ((2 * M * α ^ 2 * Real.sinh (3 / (2 * α) * τ) ^ 2) ^ (1 / 3 : ℝ)) ^ 2 / α ^ 2 := by
  rw [(sinh23_flow hM hα hτ).deriv, Real.sq_sqrt]
  have := law_pos hM hα hτ
  positivity

/-- `V_eff = 1` at `J = 0` is `M = −r³/(2α²)`. -/
theorem veff_one {α r M : ℝ} (hα : α ≠ 0) (hr : r ≠ 0) :
    1 - 2 * M / r - r ^ 2 / α ^ 2 = 1 ↔ M = -r ^ 3 / (2 * α ^ 2) := by
  constructor
  · intro h; field_simp at h ⊢; linarith
  · intro h; subst h; field_simp; ring

/-- The comoving turnaround `r = −(2Mα²)^{1/3}` is a real root of `r³ = −2Mα²`. -/
theorem turnaround_root {M α : ℝ} (hM : 0 < M) (hα : 0 < α) :
    (-(2 * M * α ^ 2) ^ (1 / 3 : ℝ)) ^ 3 + 2 * M * α ^ 2 = 0 := by
  have h : ((2 * M * α ^ 2) ^ (1 / 3 : ℝ)) ^ 3 = 2 * M * α ^ 2 := by
    rw [← Real.rpow_natCast, ← Real.rpow_mul (by positivity)]; norm_num
  rw [neg_pow, h]; ring

/-- `∂_p ∂_r (r² + p²) = 0` and `∂_r(r² + p²) = 2r`. -/
lemma sigma_partials (r p : ℝ) :
    deriv (fun r => r ^ 2 + p ^ 2) r = 2 * r ∧ deriv (fun p => deriv (fun r => r ^ 2 + p ^ 2) r) p = 0 := by
  have h : ∀ p, deriv (fun r => r ^ 2 + p ^ 2) r = 2 * r := fun p => by
    rw [((hasDerivAt_pow 2 r).add_const (p ^ 2)).deriv]; norm_num
  refine ⟨h p, ?_⟩
  rw [show (fun p => deriv (fun r => r ^ 2 + p ^ 2) r) = fun _ => 2 * r from funext h]
  simp

/-- **Row 91, headline.** `E = 1` is `k = 0`; the `sinh^{2/3}` law solves `r′² = 2M/r + r²/α²` and leaves
residual exactly `+k` against the `k ≠ 0` law; `V_eff = 1` is `M = −r³/(2α²)`, negative at `r = 1`; the turnaround
`−(2Mα²)^{1/3}` is its real root; and I1's computed checks. -/
theorem row91_checks {M α τ : ℝ} (hM : 0 < M) (hα : 0 < α) (hτ : 0 < τ) :
    (1 - (1 : ℝ) ^ 2 = 0)
    ∧ deriv (fun t => (2 * M * α ^ 2 * Real.sinh (3 / (2 * α) * t) ^ 2) ^ (1 / 3 : ℝ)) τ ^ 2
      = 2 * M / (2 * M * α ^ 2 * Real.sinh (3 / (2 * α) * τ) ^ 2) ^ (1 / 3 : ℝ)
        + ((2 * M * α ^ 2 * Real.sinh (3 / (2 * α) * τ) ^ 2) ^ (1 / 3 : ℝ)) ^ 2 / α ^ 2
    ∧ (∀ k : ℝ, deriv (fun t => (2 * M * α ^ 2 * Real.sinh (3 / (2 * α) * t) ^ 2) ^ (1 / 3 : ℝ)) τ ^ 2
        - (2 * M / (2 * M * α ^ 2 * Real.sinh (3 / (2 * α) * τ) ^ 2) ^ (1 / 3 : ℝ)
          + ((2 * M * α ^ 2 * Real.sinh (3 / (2 * α) * τ) ^ 2) ^ (1 / 3 : ℝ)) ^ 2 / α ^ 2 - k) = k)
    ∧ (∀ r M' : ℝ, r ≠ 0 → (1 - 2 * M' / r - r ^ 2 / α ^ 2 = 1 ↔ M' = -r ^ 3 / (2 * α ^ 2)))
    ∧ -(1 : ℝ) ^ 3 / (2 * α ^ 2) < 0
    ∧ (-(2 * M * α ^ 2) ^ (1 / 3 : ℝ)) ^ 3 + 2 * M * α ^ 2 = 0
    ∧ (∀ r p : ℝ, deriv (fun r => r ^ 2 + p ^ 2) r = 2 * r ∧ deriv (fun p => deriv (fun r => r ^ 2 + p ^ 2) r) p = 0)
    ∧ ((3 : ℝ) ^ 3 - 27 * 1 ^ 2 = 0) := by
  refine ⟨by norm_num, flow_sq hM hα hτ, fun k => by rw [flow_sq hM hα hτ]; ring,
    fun r M' hr => veff_one hα.ne' hr, by have := hα.ne'; apply div_neg_of_neg_of_pos <;> [norm_num; positivity],
    turnaround_root hM hα, sigma_partials, by norm_num⟩

end Row91

#print axioms row91_checks

/-! ## Row 26 -/

section Row26

/-- The receipt's hard-coded table: `(complete, observer-dependent, thermal)` for Rindler, the substrate's
cosmological horizon, eternal Schwarzschild, astrophysical collapse. A DEFINITION, as the receipt has it. -/
def horizonTable : List (Bool × Option Bool × Bool) :=
  [(true, some true, true), (true, some true, true), (true, some false, true), (false, none, false)]

/-- Completion predicts thermality on every row; observer-dependence does not (on the rows where it is defined). -/
theorem table_sorts : horizonTable.all (fun x => x.1 == x.2.2) = true
    ∧ horizonTable.all (fun x => match x.2.1 with | some o => o == x.2.2 | none => true) = false := by
  decide

/-- The Nariai member `M = α/(3√3)` has the double root `r = α/√3`: `f = f′ = 0` there. -/
theorem nariai_double {α : ℝ} (hα : 0 < α) :
    (1 - 2 * (α / (3 * √3)) / (α / √3) - (α / √3) ^ 2 / α ^ 2 = 0)
    ∧ HasDerivAt (fun r => 1 - 2 * (α / (3 * √3)) / r - r ^ 2 / α ^ 2) 0 (α / √3)
    ∧ (∀ r, fNar (α / √3) r = 1 - 2 * (α / (3 * √3)) / r - r ^ 2 / α ^ 2) := by
  have h3 : √3 ^ 2 = 3 := Real.sq_sqrt (by norm_num)
  have hs : 0 < √3 := by positivity
  have hr : α / √3 ≠ 0 := by positivity
  refine ⟨?_, ?_, fun r => ?_⟩
  · field_simp; linear_combination h3
  · have := ((hasDerivAt_inv hr).const_mul (2 * (α / (3 * √3)))).neg.add
      ((hasDerivAt_pow 2 (α / √3)).div_const (α ^ 2)).neg
    convert (this.const_add 1) using 1
    · funext r; simp [div_eq_mul_inv]; ring
    · have e1 : (α / √3) ^ 2 = α ^ 2 / 3 := by rw [div_pow, h3]
      rw [e1]; norm_num; field_simp; ring
  · unfold fNar; field_simp; linear_combination (-(√3 * r ^ 2)) * h3

/-- **Row 26, headline.** The table sorts by completion and not by observer-dependence; pure de Sitter's horizon is
`r = α` and THE connection's surface gravity there is `κ = −1/α`, `|f′(α)|/2 = 1/α`; `T(0) = κ/2π ≠ 0`; `T(a)/(a/2π)
→ 1`; at the Nariai double root `f = f′ = 0`, so `κ = 0`. Carried by `ds_horizon_iff`, `ds_surface_gravity`,
`unruh_ds_limits` (imported) and `fNar` of `two_surface_gravities`. -/
theorem row26_checks {α : ℝ} (hα : 0 < α) :
    (horizonTable.all (fun x => x.1 == x.2.2) = true
      ∧ horizonTable.all (fun x => match x.2.1 with | some o => o == x.2.2 | none => true) = false)
    ∧ (∀ r, 0 < r → (1 - r ^ 2 / α ^ 2 = 0 ↔ r = α))
    ∧ lcConn (ℝ × ℝ) (pgMetric (fun _ => 1) (wDS α) (fun _ => one_ne_zero) (differentiable_const _) (wDS_diff α))
        xiT (0, α) (xiT (0, α)) = -(1 / α) • xiT (0, α)
    ∧ |deriv (fun s => 1 - s ^ 2 / α ^ 2) α / 2| = 1 / α
    ∧ Real.sqrt (1 / α ^ 2 + 0 ^ 2) / (2 * π) = (1 / α) / (2 * π)
    ∧ Real.sqrt (1 / α ^ 2 + 0 ^ 2) / (2 * π) ≠ 0
    ∧ Tendsto (fun a : ℝ => Real.sqrt (1 / α ^ 2 + a ^ 2) / (2 * π) / (a / (2 * π))) atTop (𝓝 1)
    ∧ (1 - 2 * (α / (3 * √3)) / (α / √3) - (α / √3) ^ 2 / α ^ 2 = 0)
    ∧ |deriv (fun r => 1 - 2 * (α / (3 * √3)) / r - r ^ 2 / α ^ 2) (α / √3) / 2| = 0 := by
  obtain ⟨κ, -, -, hinf⟩ := unruh_ds_limits hα 0
  simp only [one_div_pow] at hinf
  have hN := nariai_double hα
  refine ⟨table_sorts, fun r hr => ?_, (ds_surface_gravity hα 0).1, (ds_surface_gravity hα 0).2, ?_, ?_, hinf,
    hN.1, by rw [hN.2.1.deriv]; simp⟩
  · constructor
    · intro h
      have : r ^ 2 = α ^ 2 := by field_simp at h; linarith
      nlinarith [sq_nonneg (r - α), sq_nonneg (r + α)]
    · rintro rfl; field_simp; ring
  · rw [zero_pow two_ne_zero, add_zero, Real.sqrt_div' 1 (by positivity), Real.sqrt_one, Real.sqrt_sq hα.le]
  · rw [zero_pow two_ne_zero, add_zero]
    have : 0 < Real.sqrt (1 / α ^ 2) := Real.sqrt_pos.2 (by positivity)
    positivity

end Row26

#print axioms row26_checks

/-! ## Row 97, §A and the closed form of §C -/

section Row97A

/-- The `E = 1` Nariai worldline `r(τ̃) = (r_s α² sinh²(3τ̃/2α))^{1/3}`, i.e. `A sinh^{2/3}` with `A = (r_sα²)^{1/3}`. -/
noncomputable def rW (rs α u : ℝ) : ℝ := (rs * α ^ 2 * Real.sinh (3 / (2 * α) * u) ^ 2) ^ (1 / 3 : ℝ)

lemma rW_A {rs α u : ℝ} (hrs : 0 < rs) (hα : 0 < α) (hu : 0 < u) :
    rW rs α u = (rs * α ^ 2) ^ (1 / 3 : ℝ) * Real.sinh (3 / (2 * α) * u) ^ (2 / 3 : ℝ) := by
  have hS : 0 < Real.sinh (3 / (2 * α) * u) := Real.sinh_pos_iff.2 (by positivity)
  rw [rW, Real.mul_rpow (by positivity) (by positivity), ← Real.rpow_natCast (Real.sinh _) 2, ← Real.rpow_mul hS.le]
  norm_num

lemma rW_cube {rs α u : ℝ} (hrs : 0 < rs) (hα : 0 < α) (hu : 0 < u) :
    rW rs α u ^ 3 = rs * α ^ 2 * Real.sinh (3 / (2 * α) * u) ^ 2 := by
  have hS : 0 < Real.sinh (3 / (2 * α) * u) := Real.sinh_pos_iff.2 (by positivity)
  rw [rW, ← Real.rpow_natCast, ← Real.rpow_mul (by positivity)]; norm_num

/-- **§A.** On the reassigned chart, `r = r(τ + χ)`, and `(∂_χ r)² − 1 = −f(r)` identically, `f = 1 − r_s/r − r²/α²`. -/
theorem layer_identity {rs α τ χ : ℝ} (hrs : 0 < rs) (hα : 0 < α) (hu : 0 < τ + χ) :
    ∃ v, HasDerivAt (fun x => rW rs α (τ + x)) v χ
      ∧ v ^ 2 - 1 = -(1 - rs / rW rs α (τ + χ) - rW rs α (τ + χ) ^ 2 / α ^ 2) := by
  have h := sinh23_flow (M := rs / 2) (by positivity) hα hu
  rw [show 2 * (rs / 2) = rs by ring] at h
  refine ⟨_, h.comp χ ((hasDerivAt_id χ).const_add τ), ?_⟩
  have hp : 0 < rW rs α (τ + χ) := by
    have : 0 < Real.sinh (3 / (2 * α) * (τ + χ)) := Real.sinh_pos_iff.2 (by positivity)
    exact Real.rpow_pos_of_pos (by positivity) _
  rw [mul_one, Real.sq_sqrt (by unfold rW at hp; positivity)]
  unfold rW; ring

/-- **§C, the closed form.** SdS's Kretschmann `48M²/r⁶ + 8Λ²/3` at `Λ = 3/α²`, `r_s = 2M`, is
`24/α⁴ + 12r_s²/r⁶`, and the two spellings agree, `12(2M)² = 48M²`. On the `E = 1` worldline the excess is
`12/(α⁴ sinh⁴(3τ̃/2α))`, free of `r_s`, and it tends to `0`. -/
theorem kretschmann_closed_form {M α r : ℝ} :
    48 * M ^ 2 / r ^ 6 + 8 * (3 / α ^ 2) ^ 2 / 3 = 24 / α ^ 4 + 12 * (2 * M) ^ 2 / r ^ 6
    ∧ 12 * (2 * M) ^ 2 = 48 * M ^ 2 := by
  constructor
  · rcases eq_or_ne α 0 with h | h
    · subst h; simp; ring
    · field_simp; ring
  · ring

theorem excess_on_worldline {rs α u : ℝ} (hrs : 0 < rs) (hα : 0 < α) (hu : 0 < u) :
    12 * rs ^ 2 / rW rs α u ^ 6 = 12 / (α ^ 4 * Real.sinh (3 / (2 * α) * u) ^ 4) := by
  have hS : 0 < Real.sinh (3 / (2 * α) * u) := Real.sinh_pos_iff.2 (by positivity)
  rw [show rW rs α u ^ 6 = (rW rs α u ^ 3) ^ 2 by ring, rW_cube hrs hα hu]
  field_simp

theorem excess_tendsto {α : ℝ} (hα : 0 < α) :
    Tendsto (fun u => 12 / (α ^ 4 * Real.sinh (3 / (2 * α) * u) ^ 4)) atTop (𝓝 0) := by
  have hk : 0 < 3 / (2 * α) := by positivity
  have h1 : Tendsto (fun u => Real.sinh (3 / (2 * α) * u)) atTop atTop :=
    tendsto_atTop_mono' atTop ((eventually_ge_atTop 0).mono fun u hu =>
      Real.self_le_sinh_iff.2 (by positivity)) (tendsto_id.const_mul_atTop hk)
  have h2 : Tendsto (fun u => α ^ 4 * Real.sinh (3 / (2 * α) * u) ^ 4) atTop atTop :=
    (tendsto_pow_atTop (by norm_num : (4 : ℕ) ≠ 0)).comp h1 |>.const_mul_atTop (by positivity)
  exact tendsto_const_nhds.div_atTop h2

end Row97A

/-! ## Row 40 -/

section Row40

/-- **Row 40, the marginal-geodesic first integral at every `D = m + 3`.** With `n = D − 1 = m + 2`, the law
`r = (2Mα² sinh²(n τ/2α))^{1/n}` has `dr/dτ = √(2M/r^{D−3} + r²/α²)`. At `m = 1` this is `sinh23_flow`. -/
theorem marginal_flow (m : ℕ) {M α τ : ℝ} (hM : 0 < M) (hα : 0 < α) (hτ : 0 < τ) :
    HasDerivAt (fun t => (2 * M * α ^ 2 * Real.sinh ((m + 2 : ℝ) / (2 * α) * t) ^ 2) ^ (1 / (m + 2 : ℝ)))
      (Real.sqrt (2 * M / ((2 * M * α ^ 2 * Real.sinh ((m + 2 : ℝ) / (2 * α) * τ) ^ 2) ^ (1 / (m + 2 : ℝ))) ^ m
        + ((2 * M * α ^ 2 * Real.sinh ((m + 2 : ℝ) / (2 * α) * τ) ^ 2) ^ (1 / (m + 2 : ℝ))) ^ 2 / α ^ 2)) τ := by
  set n : ℝ := (m + 2 : ℝ) with hn
  have hn0 : 0 < n := by positivity
  set k := n / (2 * α) with hk
  set S := Real.sinh (k * τ)
  set C := Real.cosh (k * τ)
  have hS : 0 < S := Real.sinh_pos_iff.2 (by positivity)
  have hC : 0 < C := Real.cosh_pos _
  set F := 2 * M * α ^ 2 * S ^ 2 with hF'
  have hF : 0 < F := by positivity
  set r := F ^ (1 / n)
  have hr : 0 < r := Real.rpow_pos_of_pos hF _
  have hrn : r ^ m * r ^ 2 = F := by
    rw [← pow_add, ← Real.rpow_natCast, ← Real.rpow_mul hF.le]
    rw [show (1 / n * ((m + 2 : ℕ) : ℝ)) = 1 by rw [hn]; push_cast; field_simp, Real.rpow_one]
  have hFd : HasDerivAt (fun t => 2 * M * α ^ 2 * Real.sinh (k * t) ^ 2)
      (2 * M * α ^ 2 * (2 * S * (C * k))) τ := by
    have := (((Real.hasDerivAt_sinh (k * τ)).comp τ ((hasDerivAt_id τ).const_mul k)).pow 2).const_mul
      (2 * M * α ^ 2)
    convert this using 1
    · funext y; simp [Function.comp_apply]
    · rw [show (Real.sinh ∘ HMul.hMul k) τ = S from rfl]; push_cast; ring
  have hrd := HasDerivAt.rpow_const (p := 1 / n) hFd (Or.inl hF.ne')
  convert hrd using 1
  have hFr : F ^ ((1 : ℝ) / n - 1) = r / F := by
    rw [Real.rpow_sub hF, Real.rpow_one]
  rw [hFr]
  have hcs : C ^ 2 = 1 + S ^ 2 := by rw [Real.cosh_sq]; ring
  rw [Real.sqrt_eq_iff_mul_self_eq_of_pos (by positivity)]
  have hrm : 0 < r ^ m := pow_pos hr m
  have e1 : 2 * M / r ^ m = 2 * M * r ^ 2 / F := by
    rw [← hrn]; field_simp
  rw [e1, hk]
  field_simp
  rw [hF']
  linear_combination (4 * M ^ 2 * α ^ 4 * S ^ 2) * hcs

/-- Row 40 in `D`: for `D ≥ 3`, `(dr/dτ)² = 2M/r^{D−3} + r²/α²` on `r^{D−1} = 2Mα² sinh²((D−1)τ/2α)`. -/
theorem marginal_flow_D (D : ℕ) (hD : 3 ≤ D) {M α τ : ℝ} (hM : 0 < M) (hα : 0 < α) (hτ : 0 < τ) :
    HasDerivAt (fun t => (2 * M * α ^ 2 * Real.sinh (((D : ℝ) - 1) / (2 * α) * t) ^ 2) ^ (1 / ((D : ℝ) - 1)))
      (Real.sqrt (2 * M / ((2 * M * α ^ 2 * Real.sinh (((D : ℝ) - 1) / (2 * α) * τ) ^ 2) ^ (1 / ((D : ℝ) - 1)))
          ^ (D - 3)
        + ((2 * M * α ^ 2 * Real.sinh (((D : ℝ) - 1) / (2 * α) * τ) ^ 2) ^ (1 / ((D : ℝ) - 1))) ^ 2 / α ^ 2)) τ := by
  obtain ⟨m, rfl⟩ : ∃ m, D = m + 3 := ⟨D - 3, by omega⟩
  have e : ((m + 3 : ℕ) : ℝ) - 1 = (m + 2 : ℝ) := by push_cast; ring
  rw [e, show m + 3 - 3 = m by omega]
  exact marginal_flow m hM hα hτ

/-- The squared form at `D`, as the receipt states it. -/
theorem marginal_sq (D : ℕ) (hD : 3 ≤ D) {M α τ : ℝ} (hM : 0 < M) (hα : 0 < α) (hτ : 0 < τ) :
    deriv (fun t => (2 * M * α ^ 2 * Real.sinh (((D : ℝ) - 1) / (2 * α) * t) ^ 2) ^ (1 / ((D : ℝ) - 1))) τ ^ 2
      = 2 * M / ((2 * M * α ^ 2 * Real.sinh (((D : ℝ) - 1) / (2 * α) * τ) ^ 2) ^ (1 / ((D : ℝ) - 1))) ^ (D - 3)
        + ((2 * M * α ^ 2 * Real.sinh (((D : ℝ) - 1) / (2 * α) * τ) ^ 2) ^ (1 / ((D : ℝ) - 1))) ^ 2 / α ^ 2 := by
  rw [(marginal_flow_D D hD hM hα hτ).deriv, Real.sq_sqrt]
  have : 0 < 2 * M * α ^ 2 * Real.sinh (((D : ℝ) - 1) / (2 * α) * τ) ^ 2 := by
    have : (3 : ℝ) ≤ D := by exact_mod_cast hD
    have : 0 < Real.sinh (((D : ℝ) - 1) / (2 * α) * τ) := Real.sinh_pos_iff.2 (by
      apply mul_pos (div_pos (by linarith) (by positivity)) hτ)
    positivity
  positivity

/-- The deck shift: over `ℂ`, `τ ↦ τ + 2πiα/n` leaves `sinh²(nτ/2α)` invariant, for every `n ≠ 0`. -/
theorem deck_shift (n : ℕ) (hn : n ≠ 0) {α : ℂ} (hα : α ≠ 0) (τ : ℂ) :
    Complex.sinh (n * (τ + 2 * π * Complex.I * α / n) / (2 * α)) ^ 2 = Complex.sinh (n * τ / (2 * α)) ^ 2 := by
  have hn' : (n : ℂ) ≠ 0 := by exact_mod_cast hn
  have e : n * (τ + 2 * π * Complex.I * α / n) / (2 * α) = n * τ / (2 * α) + π * Complex.I := by
    field_simp
  rw [e, Complex.sinh_add, Complex.sinh_mul_I, Complex.cosh_mul_I, ← Complex.ofReal_cos, ← Complex.ofReal_sin,
    Real.cos_pi, Real.sin_pi]
  push_cast; ring

/-- The cleared horizon numerator `α² r^{D−3} − 2Mα² − r^{D−1}`, `D = 4, 5, 6`. -/
theorem numerator_D (M α r : ℝ) (hα : α ≠ 0) (hr : r ≠ 0) :
    (1 - 2 * M / r - r ^ 2 / α ^ 2) * r * α ^ 2 = α ^ 2 * r - 2 * M * α ^ 2 - r ^ 3
    ∧ (1 - 2 * M / r ^ 2 - r ^ 2 / α ^ 2) * r ^ 2 * α ^ 2 = α ^ 2 * r ^ 2 - 2 * M * α ^ 2 - r ^ 4
    ∧ (1 - 2 * M / r ^ 3 - r ^ 2 / α ^ 2) * r ^ 3 * α ^ 2 = α ^ 2 * r ^ 3 - 2 * M * α ^ 2 - r ^ 5 := by
  refine ⟨?_, ?_, ?_⟩ <;> field_simp

open Polynomial in
/-- … of degree `D − 1`: `3, 4, 5`. -/
theorem numerator_degree (M α : ℝ) :
    (C (α ^ 2) * X - C (2 * M * α ^ 2) - X ^ 3 : ℝ[X]).natDegree = 3
    ∧ (C (α ^ 2) * X ^ 2 - C (2 * M * α ^ 2) - X ^ 4 : ℝ[X]).natDegree = 4
    ∧ (C (α ^ 2) * X ^ 3 - C (2 * M * α ^ 2) - X ^ 5 : ℝ[X]).natDegree = 5 := by
  refine ⟨?_, ?_, ?_⟩ <;> compute_degree!

/-- **Row 40, headline.** The first integral at `D = 4..8`; the deck shift leaves `r^{D−1}` fixed at `D = 4..8`;
at `D = 8` the period is `2πiα/7` and `e^{2πi/7}` is a primitive 7th root of unity; at `D = 6` the cleared
numerator is `α²r³ − 2Mα² − r⁵`, of degree 5. The deck group `Z_{D−1}` is NOT claimed. -/
theorem row40_checks {M α τ : ℝ} (hM : 0 < M) (hα : 0 < α) (hτ : 0 < τ) :
    (∀ D : ℕ, D ∈ Finset.Icc 4 8 →
      deriv (fun t => (2 * M * α ^ 2 * Real.sinh (((D : ℝ) - 1) / (2 * α) * t) ^ 2) ^ (1 / ((D : ℝ) - 1))) τ ^ 2
        = 2 * M / ((2 * M * α ^ 2 * Real.sinh (((D : ℝ) - 1) / (2 * α) * τ) ^ 2) ^ (1 / ((D : ℝ) - 1)))
            ^ (D - 3)
          + ((2 * M * α ^ 2 * Real.sinh (((D : ℝ) - 1) / (2 * α) * τ) ^ 2) ^ (1 / ((D : ℝ) - 1))) ^ 2 / α ^ 2)
    ∧ (∀ D : ℕ, D ∈ Finset.Icc 4 8 → ∀ z : ℂ,
      Complex.sinh (((D - 1 : ℕ) : ℂ) * (z + 2 * π * Complex.I * α / ((D - 1 : ℕ) : ℂ)) / (2 * α)) ^ 2
        = Complex.sinh (((D - 1 : ℕ) : ℂ) * z / (2 * α)) ^ 2)
    ∧ IsPrimitiveRoot (Complex.exp (2 * π * Complex.I / (7 : ℕ))) 7
    ∧ Complex.exp (2 * π * Complex.I / (7 : ℕ)) ^ 7 = 1 ∧ Complex.exp (2 * π * Complex.I / (7 : ℕ)) ≠ 1
    ∧ (∀ r : ℝ, r ≠ 0 →
      (1 - 2 * M / r ^ 3 - r ^ 2 / α ^ 2) * r ^ 3 * α ^ 2 = α ^ 2 * r ^ 3 - 2 * M * α ^ 2 - r ^ 5)
    ∧ (Polynomial.C (α ^ 2) * Polynomial.X ^ 3 - Polynomial.C (2 * M * α ^ 2) - Polynomial.X ^ 5
        : Polynomial ℝ).natDegree = 5 := by
  have hp := Complex.isPrimitiveRoot_exp 7 (by norm_num)
  refine ⟨fun D hD => marginal_sq D (by simp at hD; omega) hM hα hτ, fun D hD z => ?_, hp, hp.pow_eq_one,
    hp.ne_one (by norm_num), fun r hr => (numerator_D M α r hα.ne' hr).2.2, (numerator_degree M α).2.2⟩
  have : D - 1 ≠ 0 := by simp at hD; omega
  exact deck_shift (D - 1) this (by exact_mod_cast hα.ne') z

end Row40

#print axioms row40_checks

/-! ## Row 97, §B: Ricci of `ℝ × S²` and of `S³` under THE connection, on the engine's diagonal case over `Fin 3` -/

section Row97B

set_option synthInstance.maxHeartbeats 400000

/-- `dx₀²/F + P(dx₁² + S dx₂²)` on `ℝ³` (`cL3` of `Row79Leaf.lean`, copied). -/
noncomputable def cL3 (F P S : ℝ → ℝ) : Fin 3 → (Fin 3 → ℝ) → ℝ :=
  ![fun y => (F (y 0))⁻¹, fun y => P (y 0), fun y => P (y 0) * S (y 1)]

variable {F P S : ℝ → ℝ} (hF : ContDiff ℝ ∞ F) (hP : ContDiff ℝ ∞ P) (hS : ContDiff ℝ ∞ S)
  (hF0 : ∀ s, F s ≠ 0) (hP0 : ∀ s, P s ≠ 0) (hS0 : ∀ s, S s ≠ 0)

include hF hP hS hF0 in
lemma cL3_smooth (j : Fin 3) : ContDiff ℝ ∞ (cL3 F P S j) := by
  fin_cases j
  · exact (hF.comp (contDiff_apply ℝ ℝ 0)).inv fun y => hF0 _
  · exact hP.comp (contDiff_apply ℝ ℝ 0)
  · exact (hP.comp (contDiff_apply ℝ ℝ 0)).mul (hS.comp (contDiff_apply ℝ ℝ 1))
include hF0 hP0 hS0 in
lemma cL3_ne (j : Fin 3) (p : Fin 3 → ℝ) : cL3 F P S j p ≠ 0 := by
  fin_cases j <;> simp [cL3, hF0, hP0, hS0]

/-- `sin²` and its two derivatives at `θ` (`Row79Leaf.lean`, copied). -/
lemma sin2_at' {S : ℝ → ℝ} {θ : ℝ} (eS : S =ᶠ[𝓝 θ] fun s => Real.sin s ^ 2) :
    S θ = Real.sin θ ^ 2 ∧ deriv S θ = 2 * Real.sin θ * Real.cos θ ∧
      deriv (deriv S) θ = 2 * Real.cos θ ^ 2 - 2 * Real.sin θ ^ 2 := by
  have sd : ∀ s, HasDerivAt (fun s => Real.sin s ^ 2) (2 * Real.sin s * Real.cos s) s := fun s =>
    (show HasDerivAt (fun s => Real.sin s ^ 2) _ s from (Real.hasDerivAt_sin s).pow 2).congr_deriv (by norm_num)
  refine ⟨eS.eq_of_nhds, by rw [eS.deriv_eq, (sd _).deriv], ?_⟩
  rw [(eS.deriv.trans (Eventually.of_forall fun s => (sd s).deriv) :
    deriv S =ᶠ[𝓝 θ] fun s => 2 * Real.sin s * Real.cos s).deriv_eq,
    (show HasDerivAt (fun s => 2 * Real.sin s * Real.cos s) _ θ from
      ((Real.hasDerivAt_sin θ).const_mul 2).mul (Real.hasDerivAt_cos θ)).deriv]
  ring

include hF hP hS hF0 in
/-- The recipe's first partials of `cL3`. -/
lemma cL3_d1 (p : Fin 3 → ℝ) (j : Fin 3) (v : Fin 3 → ℝ) : fderiv ℝ (cL3 F P S j) p v =
    (![-(deriv F (p 0)) / F (p 0) ^ 2 * v 0, deriv P (p 0) * v 0,
      deriv P (p 0) * v 0 * S (p 1) + P (p 0) * (deriv S (p 1) * v 1)] : Fin 3 → ℝ) j := by
  have dF := fun s => ((hF.differentiable (by simp)) s).hasDerivAt
  have iv1 : deriv (fun s => (F s)⁻¹) = fun s => -(deriv F s) / F s ^ 2 :=
    funext fun s => ((dF s).inv (hF0 s)).deriv.trans (by ring)
  have hinv : ContDiff ℝ ∞ (fun s => (F s)⁻¹) := hF.inv hF0
  fin_cases j
  · show fderiv ℝ (fun y => (fun s => (F s)⁻¹) (y 0)) p v = _
    rw [co_d1 hinv]; simp [iv1]
  · show fderiv ℝ (fun y => P (y 0)) p v = _
    rw [co_d1 hP]; simp
  · show fderiv ℝ (fun y => P (y 0) * S (y 1)) p v = _
    rw [pr_d1 hP hS]; simp

include hF hP hS hF0 in
/-- … and second partials. -/
lemma cL3_d2 (p : Fin 3 → ℝ) (j : Fin 3) (u v : Fin 3 → ℝ) : fderiv ℝ (fderiv ℝ (cL3 F P S j)) p u v = (![
    (2 * deriv F (p 0) ^ 2 - F (p 0) * deriv (deriv F) (p 0)) / F (p 0) ^ 3 * u 0 * v 0,
    deriv (deriv P) (p 0) * u 0 * v 0,
    deriv (deriv P) (p 0) * u 0 * v 0 * S (p 1) + deriv P (p 0) * v 0 * (deriv S (p 1) * u 1)
      + deriv P (p 0) * u 0 * (deriv S (p 1) * v 1) + P (p 0) * (deriv (deriv S) (p 1) * u 1 * v 1)]
    : Fin 3 → ℝ) j := by
  have dF := fun s => ((hF.differentiable (by simp)) s).hasDerivAt
  have dF' := fun s => (((contDiff_infty_iff_deriv.1 hF).2.differentiable (by simp)) s).hasDerivAt
  have iv1 : deriv (fun s => (F s)⁻¹) = fun s => -(deriv F s) / F s ^ 2 :=
    funext fun s => ((dF s).inv (hF0 s)).deriv.trans (by ring)
  have iv2 : deriv (deriv (fun s => (F s)⁻¹)) (p 0)
      = (2 * deriv F (p 0) ^ 2 - F (p 0) * deriv (deriv F) (p 0)) / F (p 0) ^ 3 := by
    rw [iv1, (show HasDerivAt (fun s => -deriv F s / F s ^ 2) _ (p 0) from
      (dF' (p 0)).neg.div ((dF (p 0)).pow 2) (pow_ne_zero 2 (hF0 (p 0)))).deriv]
    have := hF0 (p 0); simp only [Pi.neg_apply]; field_simp; ring
  have hinv : ContDiff ℝ ∞ (fun s => (F s)⁻¹) := hF.inv hF0
  fin_cases j
  · show fderiv ℝ (fderiv ℝ (fun y => (fun s => (F s)⁻¹) (y 0))) p u v = _
    rw [co_d2 hinv]; simp [iv2]
  · show fderiv ℝ (fderiv ℝ (fun y => P (y 0))) p u v = _
    rw [co_d2 hP]; simp
  · show fderiv ℝ (fderiv ℝ (fun y => P (y 0) * S (y 1))) p u v = _
    rw [pr_d2 hP hS]; simp

/-- THE connection's Riemann array of `cL3 F P S` at `p`. -/
noncomputable def RL (p : Fin 3 → ℝ) (i j k : Fin 3) : Fin 3 → ℝ :=
  curv (lcConn (Fin 3 → ℝ) (ndOf (diagN (cL3 F P S)) (diagN_symm _)
    (fun p u h => diagN_nondeg (fun i => cL3_ne hF0 hP0 hS0 i p) u h)
    ((diagN_smooth (cL3_smooth hF hP hS hF0)).differentiable (by simp))))
    (fun _ => (Pi.single i 1 : Fin 3 → ℝ)) (fun _ => (Pi.single j 1 : Fin 3 → ℝ))
    (fun _ => (Pi.single k 1 : Fin 3 → ℝ)) p

set_option maxHeartbeats 16000000 in
include hF hP hS hF0 hP0 hS0 in
/-- **§B, the layer.** `dχ² + r_c²(dθ² + sin²θ dφ²)` (`F ≡ 1`, `P ≡ r_c²`): the mixed Ricci diagonal is
`(0, 1/r_c², 1/r_c²)`, a flat line times a round `S²`. -/
theorem layer_ricci {rc : ℝ} (eF : ∀ s, F s = 1) (eP : ∀ s, P s = rc ^ 2) (p : Fin 3 → ℝ)
    (eS : S =ᶠ[𝓝 (p 1)] fun s => Real.sin s ^ 2) :
    ricCN (RL hF hP hS hF0 hP0 hS0 p) 0 0 / cL3 F P S 0 p = 0
    ∧ ricCN (RL hF hP hS hF0 hP0 hS0 p) 1 1 / cL3 F P S 1 p = 1 / rc ^ 2
    ∧ ricCN (RL hF hP hS hF0 hP0 hS0 p) 2 2 / cL3 F P S 2 p = 1 / rc ^ 2 := by
  have hFf : F = fun _ => 1 := funext eF
  have hPf : P = fun _ => rc ^ 2 := funext eP
  have F1 : ∀ s, deriv F s = 0 := fun s => by rw [hFf]; simp
  have F2 : ∀ s, deriv (deriv F) s = 0 := fun s => by rw [hFf]; simp
  have P1 : ∀ s, deriv P s = 0 := fun s => by rw [hPf]; simp
  have P2 : ∀ s, deriv (deriv P) s = 0 := fun s => by rw [hPf]; simp
  obtain ⟨hSv, hS1, hS2⟩ := sin2_at' eS
  have hsa : Real.sin (p 1) ≠ 0 := fun h => hS0 (p 1) (by rw [hSv, h]; simp)
  have hrc : rc ≠ 0 := fun h => hP0 0 (by rw [eP, h]; simp)
  have hR : ∀ i j, RL hF hP hS hF0 hP0 hS0 p i j j i
      = curvDN (cL3 F P S) p (Pi.single i 1) (Pi.single j 1) (Pi.single j 1) i :=
    fun i j => by simp only [RL, curvDN_eq (cL3_ne hF0 hP0 hS0) (cL3_smooth hF hP hS hF0)]
  refine ⟨?_, ?_, ?_⟩ <;>
  (simp only [ricCN, Fin.sum_univ_three, hR]
   simp only [curvDN, Pi.sub_apply, Pi.add_apply, DGDN, gamDN, dC1N, dC2N, cL3_d1 hF hP hS hF0,
    cL3_d2 hF hP hS hF0]
   simp [cL3, Fin.sum_univ_three, eF, eP, F1, F2, P1, P2, hSv, hS1, hS2] <;> field_simp <;> ring1)

set_option maxHeartbeats 16000000 in
include hF hP hS hF0 hP0 hS0 in
/-- **§B, the comparison.** The round `S³` of radius `a`, `a²(dψ² + sin²ψ(dθ² + sin²θ dφ²))` (`F ≡ 1/a²`,
`P = a² sin²ψ` and `S = sin²θ` near the point): all three mixed Ricci entries are `2/a²`, so no radius gives a zero. -/
theorem s3_ricci {a : ℝ} (ha : a ≠ 0) (eF : ∀ s, F s = (a ^ 2)⁻¹) (p : Fin 3 → ℝ)
    (eP : P =ᶠ[𝓝 (p 0)] fun s => a ^ 2 * Real.sin s ^ 2) (eS : S =ᶠ[𝓝 (p 1)] fun s => Real.sin s ^ 2) :
    ricCN (RL hF hP hS hF0 hP0 hS0 p) 0 0 / cL3 F P S 0 p = 2 / a ^ 2
    ∧ ricCN (RL hF hP hS hF0 hP0 hS0 p) 1 1 / cL3 F P S 1 p = 2 / a ^ 2
    ∧ ricCN (RL hF hP hS hF0 hP0 hS0 p) 2 2 / cL3 F P S 2 p = 2 / a ^ 2 := by
  have hFf : F = fun _ => (a ^ 2)⁻¹ := funext eF
  have F1 : ∀ s, deriv F s = 0 := fun s => by rw [hFf]; simp
  have F2 : ∀ s, deriv (deriv F) s = 0 := fun s => by rw [hFf]; simp
  obtain ⟨hSv, hS1, hS2⟩ := sin2_at' eS
  have sP := sin2_at' (S := fun s => P s / a ^ 2) (θ := p 0)
    (eP.mono fun s hs => by simp only [hs]; field_simp)
  have hPv : P (p 0) = a ^ 2 * Real.sin (p 0) ^ 2 := eP.eq_of_nhds
  have dP : ∀ s, HasDerivAt P (deriv P s) s := fun s => ((hP.differentiable (by simp)) s).hasDerivAt
  have dP' : ∀ s, HasDerivAt (deriv P) (deriv (deriv P) s) s := fun s =>
    (((contDiff_infty_iff_deriv.1 hP).2.differentiable (by simp)) s).hasDerivAt
  have P1 : deriv P (p 0) = a ^ 2 * (2 * Real.sin (p 0) * Real.cos (p 0)) := by
    have := sP.2.1; rw [((dP (p 0)).div_const (a ^ 2)).deriv] at this; field_simp at this ⊢; linarith
  have P2 : deriv (deriv P) (p 0) = a ^ 2 * (2 * Real.cos (p 0) ^ 2 - 2 * Real.sin (p 0) ^ 2) := by
    have := sP.2.2
    have e : deriv (fun s => P s / a ^ 2) = fun s => deriv P s / a ^ 2 :=
      funext fun s => ((dP s).div_const (a ^ 2)).deriv
    rw [e, ((dP' (p 0)).div_const (a ^ 2)).deriv] at this; field_simp at this ⊢; linarith
  have hsa : Real.sin (p 1) ≠ 0 := fun h => hS0 (p 1) (by rw [hSv, h]; simp)
  have hsp : Real.sin (p 0) ≠ 0 := fun h => hP0 (p 0) (by rw [hPv, h]; simp)
  have hR : ∀ i j, RL hF hP hS hF0 hP0 hS0 p i j j i
      = curvDN (cL3 F P S) p (Pi.single i 1) (Pi.single j 1) (Pi.single j 1) i :=
    fun i j => by simp only [RL, curvDN_eq (cL3_ne hF0 hP0 hS0) (cL3_smooth hF hP hS hF0)]
  simp only [ricCN, Fin.sum_univ_three, hR]
  simp only [curvDN, Pi.sub_apply, Pi.add_apply, DGDN, gamDN, dC1N, dC2N, cL3_d1 hF hP hS hF0,
    cL3_d2 hF hP hS hF0]
  simp [cL3, Fin.sum_univ_three, eF, F1, F2, hPv, P1, P2, hSv, hS1, hS2]
  refine ⟨?_, ?_, ?_⟩ <;> (field_simp; first | ring1 | linear_combination (-(Real.sin (p 1)) ^ 2) * Real.sin_sq_add_cos_sq (p 0))

end Row97B

/-! ## Row 97, §C: `sds_kretschmann` (row 45), copied, on the worldline -/

/-- On the worldline, `48M²/r⁶ + 8Λ²/3` at `M = r_s/2`, `Λ = 3/α²` is `24/α⁴ + 12/(α⁴ sinh⁴(3τ̃/2α))`. -/
theorem kret_worldline {rs α u : ℝ} (hrs : 0 < rs) (hα : 0 < α) (hu : 0 < u) :
    48 * (rs / 2) ^ 2 / rW rs α u ^ 6 + 8 * (3 / α ^ 2) ^ 2 / 3
      = 24 / α ^ 4 + 12 / (α ^ 4 * Real.sinh (3 / (2 * α) * u) ^ 4) := by
  have hS : 0 < Real.sinh (3 / (2 * α) * u) := Real.sinh_pos_iff.2 (by positivity)
  rw [show rW rs α u ^ 6 = (rW rs α u ^ 3) ^ 2 by ring, rW_cube hrs hα hu]
  field_simp; ring

section Inst_R45

set_option synthInstance.maxHeartbeats 400000

noncomputable def cK (F P S : ℝ → ℝ) : Fin 4 → (Fin 4 → ℝ) → ℝ :=
  ![fun y => -F (y 1), fun y => (F (y 1))⁻¹, fun y => P (y 1), fun y => P (y 1) * S (y 2)]

/-- The static-spherical Riemann table `R(eᵢ,eⱼ)eₖ` component `l`, in `F₀, F₁, F₂` (the radial profile and its
derivatives), `r`, and `S₀, S₁, S₂` (the angular profile); the angular part enters only through `Q`. -/
noncomputable def kR (f0 f1 f2 r s0 s1 s2 : ℝ) (i j k l : Fin 4) : ℝ :=
  let Q := (4 * f0 * s0 ^ 2 + 2 * s0 * s2 - s1 ^ 2) / (4 * s0 ^ 2)
  if (i, j, k, l) = (0, 1, 0, 1) then -(f0 * f2 / 2) else if (i, j, k, l) = (0, 1, 1, 0) then -(f2 / (2 * f0))
  else if (i, j, k, l) = (0, 2, 0, 2) then -(f0 * f1 / (2 * r)) else if (i, j, k, l) = (0, 2, 2, 0) then -(f1 * r / 2)
  else if (i, j, k, l) = (0, 3, 0, 3) then -(f0 * f1 / (2 * r)) else if (i, j, k, l) = (0, 3, 3, 0) then -(f1 * r * s0 / 2)
  else if (i, j, k, l) = (1, 0, 0, 1) then f0 * f2 / 2 else if (i, j, k, l) = (1, 0, 1, 0) then f2 / (2 * f0)
  else if (i, j, k, l) = (1, 2, 1, 2) then f1 / (2 * f0 * r) else if (i, j, k, l) = (1, 2, 2, 1) then -(f1 * r / 2)
  else if (i, j, k, l) = (1, 3, 1, 3) then f1 / (2 * f0 * r) else if (i, j, k, l) = (1, 3, 3, 1) then -(f1 * r * s0 / 2)
  else if (i, j, k, l) = (2, 0, 0, 2) then f0 * f1 / (2 * r) else if (i, j, k, l) = (2, 0, 2, 0) then f1 * r / 2
  else if (i, j, k, l) = (2, 1, 1, 2) then -(f1 / (2 * f0 * r)) else if (i, j, k, l) = (2, 1, 2, 1) then f1 * r / 2
  else if (i, j, k, l) = (2, 3, 2, 3) then Q else if (i, j, k, l) = (2, 3, 3, 2) then -(Q * s0)
  else if (i, j, k, l) = (3, 0, 0, 3) then f0 * f1 / (2 * r) else if (i, j, k, l) = (3, 0, 3, 0) then f1 * r * s0 / 2
  else if (i, j, k, l) = (3, 1, 1, 3) then -(f1 / (2 * f0 * r)) else if (i, j, k, l) = (3, 1, 3, 1) then f1 * r * s0 / 2
  else if (i, j, k, l) = (3, 2, 2, 3) then -Q else if (i, j, k, l) = (3, 2, 3, 2) then Q * s0
  else 0

variable {F P S : ℝ → ℝ} (hF : ContDiff ℝ ∞ F) (hP : ContDiff ℝ ∞ P) (hS : ContDiff ℝ ∞ S)
  (hF0 : ∀ s, F s ≠ 0) (hP0 : ∀ s, P s ≠ 0) (hS0 : ∀ s, S s ≠ 0)

include hF hP hS hF0 in
lemma cK_smooth (k : Fin 4) : ContDiff ℝ ∞ (cK F P S k) := by
  fin_cases k
  · exact (hF.comp (contDiff_apply ℝ ℝ 1)).neg
  · exact (hF.comp (contDiff_apply ℝ ℝ 1)).inv fun y => hF0 _
  · exact hP.comp (contDiff_apply ℝ ℝ 1)
  · exact (hP.comp (contDiff_apply ℝ ℝ 1)).mul (hS.comp (contDiff_apply ℝ ℝ 2))
include hF0 hP0 hS0 in
lemma cK_ne (k : Fin 4) (p : Fin 4 → ℝ) : cK F P S k p ≠ 0 := by
  fin_cases k <;> simp [cK, hF0, hP0, hS0]

open Filter Topology in
set_option maxHeartbeats 8000000 in
include hF hP hS hF0 hP0 hS0 in
/-- **Row 45, the `S²` pilot.** -/
theorem sds_kretschmann (M Λ : ℝ) (p : Fin 4 → ℝ)
    (eF : F =ᶠ[𝓝 (p 1)] fun s => 1 - 2 * M * s⁻¹ - Λ / 3 * s ^ 2) (eP : P =ᶠ[𝓝 (p 1)] fun s => s ^ 2)
    (eS : S =ᶠ[𝓝 (p 2)] fun s => Real.sin s ^ 2) :
    riem2C (fun i => cK F P S i p) (fun i j k => curv (lcConn (Fin 4 → ℝ) (ndOf (diag4 (cK F P S)) (diag4_symm _)
      (fun p u h => diag4_nondeg (fun i => cK_ne hF0 hP0 hS0 i p) u h)
      ((diag4_smooth (cK_smooth hF hP hS hF0)).differentiable (by simp))))
      (fun _ => (Pi.single i 1 : Fin 4 → ℝ)) (fun _ => (Pi.single j 1 : Fin 4 → ℝ))
      (fun _ => (Pi.single k 1 : Fin 4 → ℝ)) p) = 48 * M ^ 2 / p 1 ^ 6 + 8 * Λ ^ 2 / 3 := by
  set r := p 1 with hr_def
  have hr : r ≠ 0 := fun h => hP0 r (by rw [eP.eq_of_nhds, h]; simp)
  -- the radial profile: `f`, `f′`, `f″` at `r`
  have hf1 : ∀ s, s ≠ 0 → HasDerivAt (fun s => 1 - 2 * M * s⁻¹ - Λ / 3 * s ^ 2)
      (2 * M * (s ^ 2)⁻¹ - 2 * Λ / 3 * s) s := fun s hs =>
    (show HasDerivAt (fun s => 1 - 2 * M * s⁻¹ - Λ / 3 * s ^ 2) _ s from
      ((hasDerivAt_const s (1 : ℝ)).sub ((hasDerivAt_inv hs).const_mul (2 * M))).sub
        ((hasDerivAt_pow 2 s).const_mul (Λ / 3))).congr_deriv (by norm_num; ring)
  have ed : deriv (fun s => 1 - 2 * M * s⁻¹ - Λ / 3 * s ^ 2) =ᶠ[𝓝 r]
      fun s => 2 * M * (s ^ 2)⁻¹ - 2 * Λ / 3 * s :=
    Filter.eventually_of_mem (isOpen_ne.mem_nhds hr) fun s hs => (hf1 s hs).deriv
  have hF0v : F r = 1 - 2 * M * r⁻¹ - Λ / 3 * r ^ 2 := eF.eq_of_nhds
  have hF1v : deriv F r = 2 * M * (r ^ 2)⁻¹ - 2 * Λ / 3 * r := by rw [eF.deriv_eq, (hf1 r hr).deriv]
  have hF2v : deriv (deriv F) r = -(4 * M / r ^ 3) - 2 * Λ / 3 := by
    rw [(eF.deriv.trans ed).deriv_eq]
    have := (show HasDerivAt (fun s => 2 * M * (s ^ 2)⁻¹ - 2 * Λ / 3 * s) _ r from
      (((hasDerivAt_pow 2 r).inv (pow_ne_zero 2 hr)).const_mul (2 * M)).sub ((hasDerivAt_id r).const_mul (2 * Λ / 3)))
    rw [this.deriv]; field_simp; ring
  -- the inverse profile `1/F`
  have dF := fun s => ((hF.differentiable (by simp)) s).hasDerivAt
  have dF' := fun s => (((contDiff_infty_iff_deriv.1 hF).2.differentiable (by simp)) s).hasDerivAt
  have iv1 : deriv (fun s => (F s)⁻¹) = fun s => -(deriv F s) / F s ^ 2 :=
    funext fun s => ((dF s).inv (hF0 s)).deriv.trans (by ring)
  have iv2 : deriv (deriv (fun s => (F s)⁻¹)) r = (2 * deriv F r ^ 2 - F r * deriv (deriv F) r) / F r ^ 3 := by
    rw [iv1, (show HasDerivAt (fun s => -deriv F s / F s ^ 2) _ r from
      (dF' r).neg.div ((dF r).pow 2) (pow_ne_zero 2 (hF0 r))).deriv]
    have := hF0 r; simp only [Pi.neg_apply]; field_simp; ring
  have ng1 : deriv (fun s => -F s) = fun s => -deriv F s := funext fun s => deriv.neg
  have hneg : ContDiff ℝ ∞ (fun s => -F s) := hF.neg
  have hinv : ContDiff ℝ ∞ (fun s => (F s)⁻¹) := hF.inv hF0
  -- `r²` and `sin²θ`
  have hPv : P r = r ^ 2 := eP.eq_of_nhds
  have hP1 : deriv P r = 2 * r := by rw [eP.deriv_eq]; simp
  have e2 : deriv P =ᶠ[𝓝 r] fun s => 2 * s := eP.deriv.trans (Eventually.of_forall fun s => by simp)
  have hP2 : deriv (deriv P) r = 2 := by rw [e2.deriv_eq]; simp
  have sd : ∀ s, HasDerivAt (fun s => Real.sin s ^ 2) (2 * Real.sin s * Real.cos s) s := fun s =>
    (show HasDerivAt (fun s => Real.sin s ^ 2) _ s from (Real.hasDerivAt_sin s).pow 2).congr_deriv (by norm_num <;> ring)
  have hSv : S (p 2) = Real.sin (p 2) ^ 2 := eS.eq_of_nhds
  have hS1 : deriv S (p 2) = 2 * Real.sin (p 2) * Real.cos (p 2) := by rw [eS.deriv_eq, (sd _).deriv]
  have hS2 : deriv (deriv S) (p 2) = 2 * Real.cos (p 2) ^ 2 - 2 * Real.sin (p 2) ^ 2 := by
    have e3 : deriv S =ᶠ[𝓝 (p 2)] fun s => 2 * Real.sin s * Real.cos s :=
      eS.deriv.trans (Eventually.of_forall fun s => (sd s).deriv)
    rw [e3.deriv_eq]
    have := (show HasDerivAt (fun s => 2 * Real.sin s * Real.cos s) _ (p 2) from
      ((Real.hasDerivAt_sin (p 2)).const_mul 2).mul (Real.hasDerivAt_cos (p 2)))
    rw [this.deriv]; ring
  -- the recipe's facts
  have hD1 : ∀ k v, fderiv ℝ (cK F P S k) p v = (![-(deriv F r * v 1), -(deriv F r) / F r ^ 2 * v 1,
      2 * r * v 1, 2 * r * v 1 * S (p 2) + r ^ 2 * (deriv S (p 2) * v 2)] : Fin 4 → ℝ) k := fun k v => by
    fin_cases k
    · show fderiv ℝ (fun y => (fun s => -F s) (y 1)) p v = _
      rw [co_d1 hneg]; simp [← hr_def, ng1]
    · show fderiv ℝ (fun y => (fun s => (F s)⁻¹) (y 1)) p v = _
      rw [co_d1 hinv]; simp [← hr_def, iv1]
    · show fderiv ℝ (fun y => P (y 1)) p v = _
      rw [co_d1 hP]; simp [← hr_def, hP1]
    · show fderiv ℝ (fun y => P (y 1) * S (y 2)) p v = _
      rw [pr_d1 hP hS]; simp [← hr_def, hP1, hPv]
  have hD2 : ∀ k u v, fderiv ℝ (fderiv ℝ (cK F P S k)) p u v = (![-(deriv (deriv F) r * u 1 * v 1),
      (2 * deriv F r ^ 2 - F r * deriv (deriv F) r) / F r ^ 3 * u 1 * v 1, 2 * u 1 * v 1,
      2 * u 1 * v 1 * S (p 2) + 2 * r * v 1 * (deriv S (p 2) * u 2) + 2 * r * u 1 * (deriv S (p 2) * v 2)
        + r ^ 2 * (deriv (deriv S) (p 2) * u 2 * v 2)] : Fin 4 → ℝ) k := fun k u v => by
    fin_cases k
    · show fderiv ℝ (fderiv ℝ (fun y => (fun s => -F s) (y 1))) p u v = _
      rw [co_d2 hneg]; simp [← hr_def, ng1, deriv.neg]
    · show fderiv ℝ (fderiv ℝ (fun y => (fun s => (F s)⁻¹) (y 1))) p u v = _
      rw [co_d2 hinv]; simp [← hr_def, iv2]
    · show fderiv ℝ (fderiv ℝ (fun y => P (y 1))) p u v = _
      rw [co_d2 hP]; simp [← hr_def, hP2]
    · show fderiv ℝ (fderiv ℝ (fun y => P (y 1) * S (y 2))) p u v = _
      rw [pr_d2 hP hS]; simp [← hr_def, hP1, hP2, hPv]
  -- the table, component by component
  have hT : ∀ i j k l, curvD (cK F P S) p (Pi.single i 1) (Pi.single j 1) (Pi.single k 1) l
      = kR (F r) (deriv F r) (deriv (deriv F) r) r (S (p 2)) (deriv S (p 2)) (deriv (deriv S) (p 2)) i j k l := by
    have := hF0 r; have := hS0 (p 2)
    intro i j k l
    fin_cases i <;> fin_cases j <;> fin_cases k <;> fin_cases l <;>
      (simp only [curvD, Pi.sub_apply, Pi.add_apply, DGD, gamD, dC1, dC2, hD1, hD2]
       simp [cK, kR, Fin.sum_univ_four, ← hr_def, hPv]
       try (field_simp; try ring))
  simp only [riem2C, curvD_eq (cK_ne hF0 hP0 hS0) (cK_smooth hF hP hS hF0), hT]
  have hs : Real.sin (p 2) ≠ 0 := fun h => hS0 (p 2) (by rw [hSv, h]; simp)
  have hf := hF0 r
  rw [show (48 * M ^ 2 / r ^ 6 + 8 * Λ ^ 2 / 3 : ℝ)
      = deriv (deriv F) r ^ 2 + 4 * deriv F r ^ 2 / r ^ 2 + 4 * (F r - 1) ^ 2 / r ^ 4 by
    rw [hF0v, hF1v, hF2v]; field_simp; ring]
  simp [Fin.sum_univ_four, kR, cK, ← hr_def, hPv, hSv, hS1, hS2]
  field_simp
  ring


open Filter Topology in
include hF hP hS hF0 hP0 hS0 in
/-- **§C under THE connection.** At a point on the worldline, the static-chart Kretschmann of SdS with
`M = r_s/2`, `Λ = 3/α²` is `24/α⁴ + 12/(α⁴ sinh⁴(3τ̃/2α))`. -/
theorem kretschmann_on_worldline {rs α u : ℝ} (hrs : 0 < rs) (hα : 0 < α) (hu : 0 < u) (p : Fin 4 → ℝ)
    (hp : p 1 = rW rs α u)
    (eF : F =ᶠ[𝓝 (p 1)] fun s => 1 - 2 * (rs / 2) * s⁻¹ - (3 / α ^ 2) / 3 * s ^ 2) (eP : P =ᶠ[𝓝 (p 1)] fun s => s ^ 2)
    (eS : S =ᶠ[𝓝 (p 2)] fun s => Real.sin s ^ 2) :
    riem2C (fun i => cK F P S i p) (fun i j k => curv (lcConn (Fin 4 → ℝ) (ndOf (diag4 (cK F P S)) (diag4_symm _)
      (fun p u h => diag4_nondeg (fun i => cK_ne hF0 hP0 hS0 i p) u h)
      ((diag4_smooth (cK_smooth hF hP hS hF0)).differentiable (by simp))))
      (fun _ => (Pi.single i 1 : Fin 4 → ℝ)) (fun _ => (Pi.single j 1 : Fin 4 → ℝ))
      (fun _ => (Pi.single k 1 : Fin 4 → ℝ)) p) = 24 / α ^ 4 + 12 / (α ^ 4 * Real.sinh (3 / (2 * α) * u) ^ 4) := by
  rw [sds_kretschmann hF hP hS hF0 hP0 hS0 _ _ p eF eP eS, hp, kret_worldline hrs hα hu]

end Inst_R45


/-- The receipt's points: `τ = 2αu/3`, `χ = 0`, so the argument `3τ/2α` is `u`. -/
theorem kret_point {rs α u : ℝ} (hrs : 0 < rs) (hα : 0 < α) (hu : 0 < u) :
    48 * (rs / 2) ^ 2 / rW rs α (2 * α * u / 3) ^ 6 + 8 * (3 / α ^ 2) ^ 2 / 3
      = 24 / α ^ 4 + 12 / (α ^ 4 * Real.sinh u ^ 4) := by
  have := kret_worldline hrs hα (u := 2 * α * u / 3) (by positivity)
  rwa [show 3 / (2 * α) * (2 * α * u / 3) = u by field_simp] at this

/-- **Row 97, headline** (with `layer_ricci`, `s3_ricci`, `kretschmann_on_worldline` below for the engine parts).
§A the layer identity; §C the closed form, the spellings, the `r_s`-free excess, its late-time limit, and the six
receipt points `(u, r_s, α)` as instances of the closed form. -/
theorem row97_checks :
    (∀ rs α τ χ : ℝ, 0 < rs → 0 < α → 0 < τ + χ → ∃ v, HasDerivAt (fun x => rW rs α (τ + x)) v χ
      ∧ v ^ 2 - 1 = -(1 - rs / rW rs α (τ + χ) - rW rs α (τ + χ) ^ 2 / α ^ 2))
    ∧ (∀ M α r : ℝ, 48 * M ^ 2 / r ^ 6 + 8 * (3 / α ^ 2) ^ 2 / 3 = 24 / α ^ 4 + 12 * (2 * M) ^ 2 / r ^ 6
      ∧ 12 * (2 * M) ^ 2 = 48 * M ^ 2)
    ∧ (∀ rs α u : ℝ, 0 < rs → 0 < α → 0 < u →
      12 * rs ^ 2 / rW rs α u ^ 6 = 12 / (α ^ 4 * Real.sinh (3 / (2 * α) * u) ^ 4))
    ∧ (∀ α : ℝ, 0 < α → Tendsto (fun u => 12 / (α ^ 4 * Real.sinh (3 / (2 * α) * u) ^ 4)) atTop (𝓝 0))
    ∧ (∀ q ∈ ([(1 / 2, 1, 1), (3 / 2, 1, 1), (3, 1, 1), (7 / 10, 2, 3), (2, 1 / 3, 5), (9 / 4, 7, 2)] :
        List (ℝ × ℝ × ℝ)),
      48 * (q.2.1 / 2) ^ 2 / rW q.2.1 q.2.2 (2 * q.2.2 * q.1 / 3) ^ 6 + 8 * (3 / q.2.2 ^ 2) ^ 2 / 3
        = 24 / q.2.2 ^ 4 + 12 / (q.2.2 ^ 4 * Real.sinh q.1 ^ 4)) := by
  refine ⟨fun rs α τ χ h1 h2 h3 => layer_identity h1 h2 h3, fun M α r => kretschmann_closed_form,
    fun rs α u h1 h2 h3 => excess_on_worldline h1 h2 h3, fun α h => excess_tendsto h, fun q hq => ?_⟩
  simp only [List.mem_cons, List.not_mem_nil, or_false] at hq
  rcases hq with rfl | rfl | rfl | rfl | rfl | rfl <;> exact kret_point (by norm_num) (by norm_num) (by norm_num)

#print axioms row97_checks
#print axioms layer_ricci
#print axioms s3_ricci
#print axioms kretschmann_on_worldline

end ShadowProbe.LimitQuadricFlow

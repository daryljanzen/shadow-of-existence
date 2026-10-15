import ShadowEngine

/-! # Campaign 12 (`r7353+71.16`): row 19's last half, the running-layer comparison

`L818_po6_running_layer/S1`: on the running FRW layer the one-loop quadratic-curvature counterterm
`a₁Riem² + a₂Ric² + a₃R²` reduces to {Gauss–Bonnet, `Λ²`, `ΛR`, field-equation-proportional} with remainder ZERO,
for arbitrary coefficients. Its item 1 (`Weyl² = 0`, `R` runs, `R → 12H²`) is the engine's `frw_weyl`,
`frw_scal`, `layer_scal` and `layer_late`. This file builds items 3 to 5.
- A. `frw_invariants`: the mixed Ricci, `Riem²`, `Ric²` and `R` of flat FRW for a free `a`, under THE connection.
- B. `tv_identity`: `(7/20)Ric² + (1/120)R² = E·f` for ANY `4 × 4` mixed Ricci (item 3).
- C. `ledger_general`: the reduction for ANY curvature data, remainder zero (item 4, background-independent).
- D. `ledger_layer`: the receipt's reduction on flat FRW, under THE connection (item 4, as stated).
- E. `ledger_ds_point`: at `Ḣ = 0`, `H² = Λ/3`, `R = 4Λ` and `tr E = 0` (item 5). -/

open Bundle Manifold Filter Set VectorField
open scoped ContDiff Manifold Topology

namespace ShadowProbe

section RunningLayer

set_option synthInstance.maxHeartbeats 400000

/-- B. **Item 3, background-independent.** For any mixed Ricci `M` in dimension `4`, with `R = tr M`,
`E = M − ½R` and `f = (7/20)M − (11/60)R`: `(7/20)tr M² + (1/120)R² = tr(E f)`. -/
theorem tv_identity (M : Matrix (Fin 4) (Fin 4) ℝ) :
    7 / 20 * (M * M).trace + 1 / 120 * M.trace ^ 2 =
      ((M - (M.trace / 2) • 1) * ((7 / 20 : ℝ) • M - (11 / 60 * M.trace) • 1)).trace := by
  simp only [Matrix.sub_mul, Matrix.mul_sub, Matrix.smul_mul, Matrix.mul_smul, Matrix.one_mul, Matrix.mul_one,
    Matrix.trace_sub, Matrix.trace_smul, Matrix.trace_one, Fintype.card_fin, smul_eq_mul, smul_smul]
  push_cast; ring

/-- C. **Item 4, background-independent and coefficient-independent.** For any `a₁, a₂, a₃`, `Λ`, `Riem²` and mixed
Ricci `M` in dimension `4`, with `E = M + (Λ − R/2)`, the counterterm is `a₁E_GB` plus a `Λ²`, a `ΛR` and an
`E`-proportional part. The remainder is zero. -/
theorem ledger_general (a₁ a₂ a₃ Λ Riem2 : ℝ) (M : Matrix (Fin 4) (Fin 4) ℝ) :
    let R := M.trace
    let E := M + (Λ - R / 2) • (1 : Matrix (Fin 4) (Fin 4) ℝ)
    a₁ * Riem2 + a₂ * (M * M).trace + a₃ * R ^ 2 =
      a₁ * (Riem2 - 4 * (M * M).trace + R ^ 2) + (a₂ + 4 * a₁) * ((E * E).trace + 2 * Λ * R - 4 * Λ ^ 2)
        + (a₃ - a₁) * (E.trace ^ 2 + 8 * Λ * R - 16 * Λ ^ 2) := by
  intro R E
  simp only [E, Matrix.add_mul, Matrix.mul_add, Matrix.smul_mul, Matrix.mul_smul, Matrix.one_mul, Matrix.mul_one,
    Matrix.trace_add, Matrix.trace_smul, Matrix.trace_one, Fintype.card_fin, smul_eq_mul, smul_smul]
  push_cast; ring

variable {a : ℝ → ℝ} (ha : ∀ s, a s ≠ 0) (has : ContDiff ℝ ∞ a)

/-- THE connection's curvature table of flat FRW at `p`. -/
noncomputable def RfL (p : Fin 4 → ℝ) (i j k : Fin 4) : Fin 4 → ℝ :=
  curv (lcConn (Fin 4 → ℝ) (ndOf (diag4 (cT (qFRW a))) (diag4_symm _)
      (fun p u h => diag4_nondeg (fun i => cT_ne (qFRW_ne ha) (qFRW_smooth has) i p) u h)
      ((diag4_smooth (cT_smooth (qFRW_ne ha) (qFRW_smooth has))).differentiable (by simp))))
    (fun _ => (Pi.single i 1 : Fin 4 → ℝ)) (fun _ => (Pi.single j 1 : Fin 4 → ℝ))
    (fun _ => (Pi.single k 1 : Fin 4 → ℝ)) p

include ha has

omit ha has in
/-- The derivative facts every invariant below uses. -/
lemma frw_e12 {a : ℝ → ℝ} (has : ContDiff ℝ ∞ a) :
    deriv (fun s => a s ^ 2) = (fun s => 2 * a s * deriv a s) ∧
    deriv (fun s => 2 * a s * deriv a s) = fun s => 2 * deriv a s ^ 2 + 2 * a s * deriv (deriv a) s := by
  have d0 : ∀ s, HasDerivAt a (deriv a s) s := fun s => ((has.differentiable (by simp)) s).hasDerivAt
  have d1 : ∀ s, HasDerivAt (deriv a) (deriv (deriv a) s) s := fun s =>
    (((contDiff_infty_iff_deriv.1 has).2.differentiable (by simp)) s).hasDerivAt
  exact ⟨funext fun s => ((d0 s).pow 2).deriv.trans (by simp),
    funext fun s => (((d0 s).const_mul 2).mul (d1 s)).deriv.trans (by ring)⟩

lemma RfL_T (p : Fin 4 → ℝ) (i j k : Fin 4) :
    RfL ha has p i j k = curvT (qFRW a) (p 0) (Pi.single i 1) (Pi.single j 1) (Pi.single k 1) :=
  curv_T (qFRW_ne ha) (qFRW_smooth has) p _ _ _

lemma frw_ric_off (p : Fin 4 → ℝ) (j k : Fin 4) (hjk : j ≠ k) : ricC (RfL ha has p) j k = 0 := by
  obtain ⟨e1, e2⟩ := frw_e12 has
  fin_cases j <;> fin_cases k <;> simp at hjk <;>
    (simp only [ricC, RfL_T ha has]; simp [Fin.sum_univ_four, curvT, GT, DGT, qFRW, e1, e2])

lemma frw_ric_diag (p : Fin 4 → ℝ) (j : Fin 4) :
    ricC (RfL ha has p) j j / qFRW a j (p 0) = if j = 0 then 3 * deriv (deriv a) (p 0) / a (p 0)
      else deriv (deriv a) (p 0) / a (p 0) + 2 * (deriv a (p 0) / a (p 0)) ^ 2 := by
  obtain ⟨e1, e2⟩ := frw_e12 has
  have hA := ha (p 0)
  fin_cases j <;>
    (simp only [ricC, RfL_T ha has]; simp [Fin.sum_univ_four, curvT, GT, DGT, qFRW, e1, e2]; field_simp; ring)

set_option maxHeartbeats 1600000 in
lemma frw_riem2 (p : Fin 4 → ℝ) :
    riem2C (fun i => qFRW a i (p 0)) (RfL ha has p) = 12 * (deriv (deriv a) (p 0) / a (p 0)) ^ 2
      + 12 * (deriv a (p 0) / a (p 0)) ^ 4 := by
  obtain ⟨e1, e2⟩ := frw_e12 has
  have hA := ha (p 0)
  simp only [riem2C, RfL_T ha has]
  simp [Fin.sum_univ_four, curvT, GT, DGT, qFRW, e1, e2]
  field_simp; ring

/-- A. **The invariants of flat FRW under THE connection**, for a free `a`, with `H = ȧ/a` and `Ḣ = ä/a − H²`:
the mixed Ricci is `diag(3(Ḣ + H²), Ḣ + 3H², Ḣ + 3H², Ḣ + 3H²)`, and `Riem²`, `Ric²` and `R` are
`24H⁴ + 24H²Ḣ + 12Ḣ²`, `36H⁴ + 36H²Ḣ + 12Ḣ²` and `12H² + 6Ḣ`. `Ric²` and `R` are read off the mixed Ricci. -/
theorem frw_invariants (p : Fin 4 → ℝ) :
    let Rf := RfL ha has p
    let g := fun i => qFRW a i (p 0)
    let H := deriv a (p 0) / a (p 0)
    let Hd := deriv (deriv a) (p 0) / a (p 0) - H ^ 2
    (∀ j k, j ≠ k → ricC Rf j k = 0) ∧ ricC Rf 0 0 / g 0 = 3 * (Hd + H ^ 2) ∧
      (∀ j, j ≠ 0 → ricC Rf j j / g j = Hd + 3 * H ^ 2) ∧
      riem2C g Rf = 24 * H ^ 4 + 24 * H ^ 2 * Hd + 12 * Hd ^ 2 ∧
      ric2C g Rf = 36 * H ^ 4 + 36 * H ^ 2 * Hd + 12 * Hd ^ 2 ∧ scalC g Rf = 12 * H ^ 2 + 6 * Hd := by
  intro Rf g H Hd
  have hd : ∀ j, ricC Rf j j / g j = _ := frw_ric_diag ha has p
  have hg : ∀ j, g j ≠ 0 := fun j => qFRW_ne ha j (p 0)
  have hsq : ∀ j k, ricC Rf j k ^ 2 / (g j * g k) = if j = k then (ricC Rf j j / g j) ^ 2 else 0 := by
    intro j k
    split_ifs with h
    · subst h; field_simp
    · rw [frw_ric_off ha has p j k h]; simp
  refine ⟨frw_ric_off ha has p, ?_, fun j hj => ?_, ?_, ?_, ?_⟩
  · rw [hd]; simp only [H, Hd]; simp; ring
  · rw [hd]; simp only [H, Hd, hj, ite_false]; ring
  · rw [frw_riem2 ha has p]; ring
  · simp only [ric2C, hsq, Finset.sum_ite_eq, Finset.mem_univ, ite_true, Fin.sum_univ_four, hd]; norm_num; ring
  · simp only [scalC, Fin.sum_univ_four, hd]; norm_num; ring

/-- The mixed `E^j_j = R^j_j − R/2 + Λ` of flat FRW. -/
noncomputable def EL (Λ : ℝ) (p : Fin 4 → ℝ) (j : Fin 4) : ℝ :=
  ricC (RfL ha has p) j j / qFRW a j (p 0) - scalC (fun i => qFRW a i (p 0)) (RfL ha has p) / 2 + Λ

/-- D. **Item 4 as the receipt states it, under THE connection.** On flat FRW, for any `a(T)` and any
`a₁, a₂, a₃, Λ`, with `s = a₁ + a₂ + 3a₃`:
`a₁Riem² + a₂Ric² + a₃R² = ((3a₃ − a₁)/2)·GB − 4sΛ² + 2sΛR + s·Σⱼ(E^j_j)²`. The `GB` coefficient is not `a₁`,
because the layer is conformally flat. -/
theorem ledger_layer (a₁ a₂ a₃ Λ : ℝ) (p : Fin 4 → ℝ) :
    let Rf := RfL ha has p
    let g := fun i => qFRW a i (p 0)
    let s := a₁ + a₂ + 3 * a₃
    a₁ * riem2C g Rf + a₂ * ric2C g Rf + a₃ * scalC g Rf ^ 2 =
      (3 * a₃ - a₁) / 2 * gbC g Rf - 4 * s * Λ ^ 2 + 2 * s * Λ * scalC g Rf
        + s * ∑ j, EL ha has Λ p j ^ 2 := by
  intro Rf g s
  obtain ⟨-, h0, hj, hM, hC, hS⟩ := frw_invariants ha has p
  simp only [EL, gbC, Fin.sum_univ_four]
  rw [h0, hj 1 (by decide), hj 2 (by decide), hj 3 (by decide)]
  simp only [Rf, g] at hM hC hS ⊢
  rw [hM, hC, hS]
  ring

/-- E. **Item 5.** At the vacuum de Sitter point, `Ḣ = 0` and `H² = Λ/3`: `R = 4Λ`, and the trace of `E` vanishes,
so the reduction collapses to Gauss–Bonnet plus the `Λ, G` renormalisations. -/
theorem ledger_ds_point (Λ : ℝ) (p : Fin 4 → ℝ)
    (hHd : deriv (deriv a) (p 0) / a (p 0) - (deriv a (p 0) / a (p 0)) ^ 2 = 0)
    (hH : (deriv a (p 0) / a (p 0)) ^ 2 = Λ / 3) :
    scalC (fun i => qFRW a i (p 0)) (RfL ha has p) = 4 * Λ ∧ ∑ j, EL ha has Λ p j = 0 := by
  obtain ⟨-, h0, hj, -, -, hS⟩ := frw_invariants ha has p
  simp only [hHd] at h0 hj hS
  refine ⟨by rw [hS, hH]; ring, ?_⟩
  simp only [EL, Fin.sum_univ_four]
  rw [h0, hj 1 (by decide), hj 2 (by decide), hj 3 (by decide), hS, hH]
  ring

end RunningLayer

end ShadowProbe
#print axioms ShadowProbe.tv_identity
#print axioms ShadowProbe.ledger_general
#print axioms ShadowProbe.frw_invariants
#print axioms ShadowProbe.ledger_layer
#print axioms ShadowProbe.ledger_ds_point

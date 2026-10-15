import ShadowEngine

/-! # Campaign 6, stage A (`r7351+71`): the contraction identities

- Row 71, `P10_the_shear_breaks_conformal_flatness_but_not_the_gauss_bonnet_degeneracy…`, ⓵: in four dimensions
  `C² = E₄ + 2(Ric² − R²/3)` with `E₄ = Riem² − 4Ric² + R²`, an algebraic identity between the contractions,
  for every metric the engine contracts. Its non-vacuous instance on SdS (where `C² = 48M²/r⁶ ≠ 0`) is
  `row71_sds` in `CurvatureInstances.lean`.
- Row 19, `Q1_the_degeneracy_is_conformal_flatness…`, ⓷: on closed FRW, `√g·E₄ = d/dT[24(a′³/3 + a′)]` for every
  `a`. `70`'s `frw_closed` (`SecondSeatFRW.lean`) proves `a³·E₄ = 24a″(a′² + 1)` under THE connection. What is added
  here is that `24(a′³/3 + a′)` has exactly that derivative, so the Gauss–Bonnet density is a total `T`-derivative. -/

open Bundle Manifold Filter Set VectorField
open scoped ContDiff Manifold

namespace ShadowProbe

/-- **Row 71.** `C² = E₄ + 2(Ric² − R²/3)` for every diagonal metric and every curvature array. -/
theorem weyl2_gb_identity (g : Fin 4 → ℝ) (Rf : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ) :
    weyl2C g Rf = gbC g Rf + 2 * (ric2C g Rf - scalC g Rf ^ 2 / 3) := by
  simp only [weyl2C, gbC]; ring

/-- **Row 19's total derivative.** For any smooth scale factor, `d/dT[24(a′³/3 + a′)] = 24a″(a′² + 1)`, the right side
of `70`'s `frw_closed`. -/
theorem gb_total_derivative {a : ℝ → ℝ} (ha : ContDiff ℝ ∞ a) (T : ℝ) :
    HasDerivAt (fun s => 24 * (deriv a s ^ 3 / 3 + deriv a s))
      (24 * deriv (deriv a) T * (deriv a T ^ 2 + 1)) T := by
  have d1 : HasDerivAt (deriv a) (deriv (deriv a) T) T :=
    (((contDiff_infty_iff_deriv.1 ha).2.differentiable (by simp)) T).hasDerivAt
  exact ((((d1.pow 3).div_const 3).add d1).const_mul 24).congr_deriv (by ring)

/-- **Row 7** (`I3_the_identification_is_general…`, ⓵): split the extrinsic curvature, with the index raised, as
`A = (θ/3)·1 + S` with `tr S = 0`. Then `(tr A)² − tr(A²) = (2/3)θ² − tr(S²)`, the ADM identity
`K² − K_ijK^ij = (2/3)θ² − σ_ijσ^ij`, for any leaf and any `3 × 3` matrix. No symmetry and no connection enter. -/
theorem adm_trace_split (θ : ℝ) (S : Matrix (Fin 3) (Fin 3) ℝ) (hS : Matrix.trace S = 0) :
    Matrix.trace ((θ / 3) • (1 : Matrix (Fin 3) (Fin 3) ℝ) + S) ^ 2
      - Matrix.trace (((θ / 3) • (1 : Matrix (Fin 3) (Fin 3) ℝ) + S) ^ 2)
      = 2 / 3 * θ ^ 2 - Matrix.trace (S ^ 2) := by
  simp only [Matrix.trace, Fin.sum_univ_three, Matrix.diag, sq, Matrix.mul_apply, Fin.sum_univ_three,
    Matrix.add_apply, Matrix.smul_apply, Matrix.one_apply, smul_eq_mul] at hS ⊢
  simp
  have h22 : S 2 2 = -S 0 0 - S 1 1 := by linarith
  rw [h22]; ring

end ShadowProbe

#print axioms ShadowProbe.weyl2_gb_identity
#print axioms ShadowProbe.gb_total_derivative
#print axioms ShadowProbe.adm_trace_split

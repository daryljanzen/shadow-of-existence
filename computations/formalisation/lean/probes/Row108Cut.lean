import ShadowEngine

/-! # Campaign 18 (`r7371+71.7`): row 108's half, the receipt's (4)–(5)

`P17_geometric_core_paper/P17_the_cut_is_planar_only_at_M_zero.py`. Its (1)–(3) are `section_quadric`,
`dS5_constant_curvature` and `sds_K_radial` (`HigherDim.lean`, `r7341+71.5`). Its (4)–(5) work INSIDE one ansatz,
`X = (F sinh κt, F cosh κt, G, r n)` in `ℝ^{5,1}`, with SdS's `f = 1 − 2M/r − r²/α²`:
- `boost_pullback`: the boost block pulls back to `F′²dr² − κ²F²dt²`, so `F² = f/κ²` is forced;
- `cut_defect`: on the substrate, `G² = α² − r² − f/κ²`, and the two determinations of `G′²` differ by
  `−4M·q(r)/r⁴`, with `q = −Mα² + 9Mr² + 2α²κ²r³ − 2r³`: an overall factor of `M`;
- `cut_closure_iff`: they agree at `r` iff `M·q(r) = 0`;
- `cut_closes_only_at_M_zero`: they agree on an open interval only at `M = 0`;
- `cut_control`: at `M = 0` the defect vanishes, and at `κ = 1/α` the cut is the hyperplane `X₂ = 0`.

Not claimed: nonexistence over ALL hypersurfaces of `dS₅`. The receipt does not compute that either. -/

namespace ShadowProbe

section Row108Cut

open Polynomial

/-- (i) The boost block: `X₀ = F sinh κt`, `X₁ = F cosh κt` pull `−dX₀² + dX₁²` back to `F′²dr² − κ²F²dt²`.
The differentials at `(t, r)`, applied to `(dt, dr)`, are written out. -/
theorem boost_pullback (F F' κ t dt dr : ℝ) :
    let dX0 := F' * Real.sinh (κ * t) * dr + F * κ * Real.cosh (κ * t) * dt
    let dX1 := F' * Real.cosh (κ * t) * dr + F * κ * Real.sinh (κ * t) * dt
    (-dX0 ^ 2 + dX1 ^ 2) = F' ^ 2 * dr ^ 2 - κ ^ 2 * F ^ 2 * dt ^ 2 := by
  intro dX0 dX1
  have h := Real.cosh_sq_sub_sinh_sq (κ * t)
  simp only [dX0, dX1]
  linear_combination (F' ^ 2 * dr ^ 2 - κ ^ 2 * F ^ 2 * dt ^ 2) * h

variable (M α κ : ℝ)

/-- SdS's lapse, `f = 1 − 2M/r − r²/α²`. -/
noncomputable def fS (s : ℝ) : ℝ := 1 - 2 * M / s - s ^ 2 / α ^ 2
/-- (A), on the substrate with `F² = f/κ²`: `G² = α² − r² − f/κ²`. -/
noncomputable def G2 (s : ℝ) : ℝ := α ^ 2 - s ^ 2 - fS M α s / κ ^ 2

lemma fS_hasDerivAt {r : ℝ} (hr : r ≠ 0) : HasDerivAt (fS M α) (2 * M / r ^ 2 - 2 * r / α ^ 2) r := by
  have h := ((hasDerivAt_const r (1 : ℝ)).sub ((hasDerivAt_inv hr).const_mul (2 * M))).sub
    ((hasDerivAt_pow 2 r).div_const (α ^ 2))
  refine (h.congr_of_eventuallyEq (Filter.Eventually.of_forall fun s => by simp [fS, div_eq_mul_inv])).congr_deriv ?_
  simp; ring

lemma G2_hasDerivAt {r : ℝ} (hr : r ≠ 0) :
    HasDerivAt (G2 M α κ) (-(2 * r) - (2 * M / r ^ 2 - 2 * r / α ^ 2) / κ ^ 2) r := by
  have h := ((hasDerivAt_const r (α ^ 2)).sub (hasDerivAt_pow 2 r)).sub ((fS_hasDerivAt M α hr).div_const (κ ^ 2))
  exact (h.congr_of_eventuallyEq (Filter.Eventually.of_forall fun s => rfl)).congr_deriv (by simp)

/-- The receipt's closure polynomial, `q(r) = −Mα² + 9Mr² + 2α²κ²r³ − 2r³`. -/
noncomputable def qC (r : ℝ) : ℝ := -M * α ^ 2 + 9 * M * r ^ 2 + 2 * α ^ 2 * κ ^ 2 * r ^ 3 - 2 * r ^ 3

/-- (ii) **The defect.** `κ²f·(G²)′² − G²·(4κ²(1 − f) − f′²) = −4M·q(r)/r⁴`: an overall factor `M`. -/
theorem cut_defect {r : ℝ} (hr : r ≠ 0) (hα : α ≠ 0) (hκ : κ ≠ 0) :
    κ ^ 2 * fS M α r * deriv (G2 M α κ) r ^ 2
      - G2 M α κ r * (4 * κ ^ 2 * (1 - fS M α r) - deriv (fS M α) r ^ 2)
      = -4 * M * qC M α κ r / r ^ 4 := by
  rw [(G2_hasDerivAt M α κ hr).deriv, (fS_hasDerivAt M α hr).deriv]
  simp only [G2, fS, qC]
  field_simp
  ring

/-- (iii) **Closure ⇔ `M·q(r) = 0`.** The receipt's two determinations of `G′²` (from (A), `(G²)′²/(4G²)`; from the
induced `dr²` coefficient (B), `(1 − f)/f − F′²` with `F′² = f′²/(4fκ²)`) agree at `r` iff `M·q(r) = 0`. -/
theorem cut_closure_iff {r : ℝ} (hr : r ≠ 0) (hα : α ≠ 0) (hκ : κ ≠ 0) (hf : fS M α r ≠ 0)
    (hG : G2 M α κ r ≠ 0) :
    deriv (G2 M α κ) r ^ 2 / (4 * G2 M α κ r)
        = (1 - fS M α r) / fS M α r - deriv (fS M α) r ^ 2 / (4 * fS M α r * κ ^ 2)
      ↔ M * qC M α κ r = 0 := by
  have key : deriv (G2 M α κ) r ^ 2 / (4 * G2 M α κ r)
        - ((1 - fS M α r) / fS M α r - deriv (fS M α) r ^ 2 / (4 * fS M α r * κ ^ 2))
      = (κ ^ 2 * fS M α r * deriv (G2 M α κ) r ^ 2
          - G2 M α κ r * (4 * κ ^ 2 * (1 - fS M α r) - deriv (fS M α) r ^ 2)) / (4 * κ ^ 2 * fS M α r * G2 M α κ r) := by
    field_simp
  rw [cut_defect M α κ hr hα hκ] at key
  rw [← sub_eq_zero, key]
  have h4 : r ^ 4 ≠ 0 := pow_ne_zero 4 hr
  have hd : 4 * κ ^ 2 * fS M α r * G2 M α κ r ≠ 0 := by
    have := pow_ne_zero 2 hκ; positivity
  constructor
  · intro h
    rcases div_eq_zero_iff.1 h with h | h
    · rcases div_eq_zero_iff.1 h with h | h
      · linear_combination (-1 / 4 : ℝ) * h
      · exact absurd h h4
    · exact absurd h hd
  · intro h
    have : -4 * M * qC M α κ r = 0 := by linear_combination (-4 : ℝ) * h
    rw [this]; simp

/-- (iv) **The result, inside the ansatz.** If the two determinations agree on an open interval of `r`, then
`M = 0`: no constant `κ` closes the bent cut at `M ≠ 0`. -/
theorem cut_closes_only_at_M_zero {a b : ℝ} (hab : a < b) (hα : α ≠ 0) (hκ : κ ≠ 0)
    (hnd : ∀ r ∈ Set.Ioo a b, r ≠ 0 ∧ fS M α r ≠ 0 ∧ G2 M α κ r ≠ 0)
    (hcl : ∀ r ∈ Set.Ioo a b, deriv (G2 M α κ) r ^ 2 / (4 * G2 M α κ r)
        = (1 - fS M α r) / fS M α r - deriv (fS M α) r ^ 2 / (4 * fS M α r * κ ^ 2)) :
    M = 0 := by
  by_contra hM
  set p : ℝ[X] := C (-M * α ^ 2) + C (9 * M) * X ^ 2 + C (2 * α ^ 2 * κ ^ 2 - 2) * X ^ 3 with hp
  have hev : ∀ r, p.eval r = qC M α κ r := fun r => by simp [hp, qC]; ring
  have hp0 : p ≠ 0 := by
    intro h
    have := hev 0
    rw [h, eval_zero] at this
    simp [qC] at this
    exact this.elim hM hα
  apply hp0
  refine Polynomial.eq_zero_of_infinite_isRoot p ((Set.Ioo_infinite hab).mono fun r hr => ?_)
  obtain ⟨h0, hf, hG⟩ := hnd r hr
  have := (cut_closure_iff M α κ h0 hα hκ hf hG).1 (hcl r hr)
  show p.IsRoot r
  rw [IsRoot, hev]
  exact (mul_eq_zero.1 this).resolve_left hM

/-- (v) **The control.** At `M = 0` the defect vanishes at every `r`; and at `κ = 1/α` also `G² ≡ 0`, so the cut is
the hyperplane `X₂ = 0`. -/
theorem cut_control (hα : α ≠ 0) :
    (∀ κ r, r ≠ 0 → κ ≠ 0 → κ ^ 2 * fS 0 α r * deriv (G2 0 α κ) r ^ 2
      - G2 0 α κ r * (4 * κ ^ 2 * (1 - fS 0 α r) - deriv (fS 0 α) r ^ 2) = 0) ∧
    ∀ s, G2 0 α (1 / α) s = 0 := by
  refine ⟨fun κ r hr hκ => by rw [cut_defect 0 α κ hr hα hκ]; simp, fun s => ?_⟩
  simp only [G2, fS]
  field_simp
  ring

end Row108Cut

end ShadowProbe

#print axioms ShadowProbe.boost_pullback
#print axioms ShadowProbe.cut_defect
#print axioms ShadowProbe.cut_closure_iff
#print axioms ShadowProbe.cut_closes_only_at_M_zero
#print axioms ShadowProbe.cut_control

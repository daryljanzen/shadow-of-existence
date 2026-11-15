import Mathlib

/-!
# P17 (`geometric_core_paper`): the intrinsic metric and its one eigenvalue; the tangent to the throat is null

Campaign 140 (`r7783`). Rows U1–U4 (`prop:unique`, `eq:sphere3`, `eq:eigen`) and T1–T4 (`prop:tangentnull`,
`eq:power`, `eq:powerisheight`). `prop:unique`'s uniqueness (U5) is not formalised.
-/

open Real Filter Topology Set Matrix

namespace ShadowProbe.GeometricCoreProbe

/-! ## `prop:unique`: the intrinsic metric `eq:sphere3` and its eigenvalue `eq:eigen` -/

/-- **Row U1.** On `x₀² + |x|² = α²` with `x₀ ≠ 0`, the constraint's differential `x₀ dx₀ + x·dx = 0` turns the flat
`dx₀² + |dx|²` into the intrinsic line element `|dx|² + (x·dx)²/(α² − |x|²)` (`eq:sphere3`). -/
theorem gc_line_element {α2 x0 dx0 : ℝ} {x dx : Fin 4 → ℝ} (h : x0 ^ 2 + x ⬝ᵥ x = α2) (hx0 : x0 ≠ 0)
    (hd : x0 * dx0 + x ⬝ᵥ dx = 0) :
    dx0 ^ 2 + dx ⬝ᵥ dx = dx ⬝ᵥ dx + (x ⬝ᵥ dx) ^ 2 / (α2 - x ⬝ᵥ x) := by
  have h1 : α2 - x ⬝ᵥ x = x0 ^ 2 := by linarith
  have h2 : x ⬝ᵥ dx = -(x0 * dx0) := by linarith
  rw [h1, h2]
  field_simp
  ring

/-- The intrinsic metric `g = I + x xᵀ/(α² − |x|²)`. -/
noncomputable def gc_g (α2 : ℝ) (x : Fin 4 → ℝ) : Matrix (Fin 4) (Fin 4) ℝ :=
  1 + (1 / (α2 - x ⬝ᵥ x)) • vecMulVec x x

/-- Its fourth eigenvalue `λ = α²/(α² − |x|²)`. -/
noncomputable def gc_lam (α2 : ℝ) (x : Fin 4 → ℝ) : ℝ := α2 / (α2 - x ⬝ᵥ x)

/-- **Row U2.** `g` is the paper's case formula `eq:eigen`, entry by entry. -/
theorem gc_g_entry {α2 : ℝ} {x : Fin 4 → ℝ} (hα : α2 ≠ x ⬝ᵥ x) (i j : Fin 4) :
    gc_g α2 x i j = if i = j then (α2 - (x ⬝ᵥ x - x i ^ 2)) / (α2 - x ⬝ᵥ x)
      else x i * x j / (α2 - x ⬝ᵥ x) := by
  have hs : α2 - x ⬝ᵥ x ≠ 0 := sub_ne_zero.2 hα
  by_cases h : i = j
  · subst h
    simp only [gc_g, Matrix.add_apply, Matrix.one_apply_eq, Matrix.smul_apply, vecMulVec_apply, smul_eq_mul,
      ↓reduceIte]
    field_simp
    ring
  · simp only [gc_g, Matrix.add_apply, Matrix.one_apply_ne h, Matrix.smul_apply, vecMulVec_apply, smul_eq_mul, h,
      ↓reduceIte]
    field_simp
    ring

/-- `g v = v + ((x·v)/(α² − |x|²)) x`. -/
theorem gc_g_mulVec (α2 : ℝ) (x v : Fin 4 → ℝ) :
    gc_g α2 x *ᵥ v = v + ((x ⬝ᵥ v) / (α2 - x ⬝ᵥ x)) • x := by
  unfold gc_g
  rw [Matrix.add_mulVec, Matrix.one_mulVec]
  congr 1
  ext i
  simp only [Matrix.mulVec, dotProduct, Matrix.smul_apply, vecMulVec_apply, smul_eq_mul, Pi.smul_apply,
    Finset.sum_div, Finset.sum_mul]
  refine Finset.sum_congr rfl fun j _ => ?_
  ring

/-- **Row U2.** `x` is an eigenvector with eigenvalue `λ`; every `v ⊥ x` is fixed; and `det g = λ`. -/
theorem gc_eigen {α2 : ℝ} {x : Fin 4 → ℝ} (hα : α2 ≠ x ⬝ᵥ x) :
    gc_g α2 x *ᵥ x = gc_lam α2 x • x ∧ (∀ v, x ⬝ᵥ v = 0 → gc_g α2 x *ᵥ v = v) ∧
      (gc_g α2 x).det = gc_lam α2 x := by
  have hs : α2 - x ⬝ᵥ x ≠ 0 := sub_ne_zero.2 hα
  refine ⟨?_, fun v hv => by rw [gc_g_mulVec, hv, zero_div, zero_smul, add_zero], ?_⟩
  · rw [gc_g_mulVec]
    ext i
    simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul, gc_lam]
    field_simp
    ring
  · have e : gc_g α2 x = 1 + replicateCol Unit ((1 / (α2 - x ⬝ᵥ x)) • x) * replicateRow Unit x := by
      rw [← vecMulVec_eq]
      unfold gc_g
      congr 1
      ext i j
      simp [vecMulVec_apply, mul_assoc]
    rw [e, det_one_add_replicateCol_mul_replicateRow, dotProduct_smul, smul_eq_mul, gc_lam]
    field_simp
    ring

/-- **Row U3.** The sign of `λ` for `x ≠ 0` (`s = |x|² > 0`): positive exactly for `α² < 0` or `α² > s`, zero exactly
at `α² = 0`, negative exactly for `s > α² > 0`. Within the family, Lorentzian points occur only for `α² > 0`. -/
theorem gc_sign {α2 s : ℝ} (hs : 0 < s) :
    (0 < α2 / (α2 - s) ↔ α2 < 0 ∨ s < α2) ∧ (α2 / (α2 - s) = 0 ↔ α2 = 0 ∨ α2 = s) ∧
      (α2 / (α2 - s) < 0 ↔ 0 < α2 ∧ α2 < s) := by
  refine ⟨?_, ?_, ?_⟩
  · rw [div_pos_iff]
    constructor
    · rintro (⟨h1, h2⟩ | ⟨h1, h2⟩)
      · right; linarith
      · left; exact h1
    · rintro (h | h)
      · right; constructor <;> linarith
      · left; constructor <;> linarith
  · rw [div_eq_zero_iff, sub_eq_zero]
  · rw [div_neg_iff]
    constructor
    · rintro (⟨h1, h2⟩ | ⟨h1, h2⟩)
      · exact ⟨h1, by linarith⟩
      · exact absurd h2 (by linarith)
    · rintro ⟨h1, h2⟩
      left; constructor <;> linarith

/-- **Row U4.** A pole, not a zero: at fixed `α² > 0`, `λ → +∞` as `s → α²⁻` and `λ → −∞` as `s → α²⁺`. -/
theorem gc_pole {α2 : ℝ} (hα : 0 < α2) :
    Tendsto (fun s => α2 / (α2 - s)) (𝓝[<] α2) atTop ∧ Tendsto (fun s => α2 / (α2 - s)) (𝓝[>] α2) atBot := by
  have hc : Tendsto (fun s : ℝ => α2 - s) (𝓝 α2) (𝓝 0) := by
    have := (tendsto_const_nhds (x := α2)).sub (tendsto_id (x := 𝓝 α2))
    simpa using this
  constructor
  · have h0 : Tendsto (fun s : ℝ => α2 - s) (𝓝[<] α2) (𝓝[>] 0) :=
      tendsto_nhdsWithin_iff.2 ⟨hc.mono_left nhdsWithin_le_nhds,
        eventually_nhdsWithin_of_forall fun s (hs : s < α2) => sub_pos.2 hs⟩
    have := (h0.inv_tendsto_nhdsGT_zero).const_mul_atTop hα
    simpa [div_eq_mul_inv] using this
  · have h0 : Tendsto (fun s : ℝ => α2 - s) (𝓝[>] α2) (𝓝[<] 0) :=
      tendsto_nhdsWithin_iff.2 ⟨hc.mono_left nhdsWithin_le_nhds,
        eventually_nhdsWithin_of_forall fun s (hs : α2 < s) => sub_neg.2 hs⟩
    have := (h0.inv_tendsto_nhdsLT_zero).const_mul_atBot hα
    simpa [div_eq_mul_inv] using this

/-- **Row U4.** `det g = λ` never vanishes where `g` is defined, for `α² ≠ 0`; and the `Λ = 0` member is the limit
`λ → 1` as `α² → ±∞`. -/
theorem gc_det_ne_zero_limit {α2 : ℝ} {x : Fin 4 → ℝ} (h0 : α2 ≠ 0) (hα : α2 ≠ x ⬝ᵥ x) :
    (gc_g α2 x).det ≠ 0 ∧ Tendsto (fun a => gc_lam a x) atTop (𝓝 1) ∧
      Tendsto (fun a => gc_lam a x) atBot (𝓝 1) := by
  refine ⟨?_, ?_, ?_⟩
  · rw [(gc_eigen hα).2.2, gc_lam]
    exact div_ne_zero h0 (sub_ne_zero.2 hα)
  · have h1 : Tendsto (fun a : ℝ => 1 + x ⬝ᵥ x / (a - x ⬝ᵥ x)) atTop (𝓝 (1 + 0)) :=
      tendsto_const_nhds.add ((tendsto_atTop_add_const_right _ (-(x ⬝ᵥ x)) tendsto_id).const_div_atTop (x ⬝ᵥ x)
        |>.congr fun a => by simp [sub_eq_add_neg])
    rw [add_zero] at h1
    refine h1.congr' ?_
    filter_upwards [eventually_gt_atTop (x ⬝ᵥ x)] with a ha
    have : a - x ⬝ᵥ x ≠ 0 := sub_ne_zero.2 (ne_of_gt ha)
    simp only [gc_lam]
    field_simp
    ring
  · have h1 : Tendsto (fun a : ℝ => 1 + x ⬝ᵥ x / (a - x ⬝ᵥ x)) atBot (𝓝 (1 + 0)) :=
      tendsto_const_nhds.add ((tendsto_atBot_add_const_right _ (-(x ⬝ᵥ x)) tendsto_id).const_div_atBot (x ⬝ᵥ x)
        |>.congr fun a => by simp [sub_eq_add_neg])
    rw [add_zero] at h1
    refine h1.congr' ?_
    filter_upwards [eventually_lt_atBot (x ⬝ᵥ x)] with a ha
    have : a - x ⬝ᵥ x ≠ 0 := sub_ne_zero.2 (ne_of_lt ha)
    simp only [gc_lam]
    field_simp
    ring

/-! ## `prop:tangentnull`: the tangent to the throat is a null line -/

section Tangent

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- **Row T1.** Euclid III.36 through Pythagoras: if `T` is on the throat `|T| = α` and the radius is perpendicular to
the tangent, `⟪T, P − T⟫ = 0`, then the tangent length satisfies `|P − T|² = |P|² − α² = pow(P)` (`eq:power`). -/
theorem gc_tangent_sq {α : ℝ} {P T : E} (hT : ‖T‖ = α) (hperp : inner ℝ T (P - T) = 0) :
    ‖P - T‖ ^ 2 = ‖P‖ ^ 2 - α ^ 2 := by
  have h := norm_add_sq_real T (P - T)
  rw [add_sub_cancel, hperp, hT] at h
  linarith

/-- **Row T3.** The tangent is null. If `(x₀, X)` is on the substrate `−x₀² + |X|² = α²` (so `x₀² = pow(X)`,
`eq:powerisheight`) and `T` is a point of tangency from `X`, then `(0, T)` is on the substrate and the displacement
`(x₀, X − T)` from it to `(x₀, X)` is null. The in-plane restriction of `η` is positive definite, so no displacement
within the plane is null: the null vector is the lifted one. -/
theorem gc_tangent_null {α x0 : ℝ} {X T : E} (hX : -x0 ^ 2 + ‖X‖ ^ 2 = α ^ 2) (hT : ‖T‖ = α)
    (hperp : inner ℝ T (X - T) = 0) :
    (-(0 : ℝ) ^ 2 + ‖T‖ ^ 2 = α ^ 2) ∧ (-x0 ^ 2 + ‖X - T‖ ^ 2 = 0) ∧
      ∀ v : E, v ≠ 0 → 0 < -(0 : ℝ) ^ 2 + ‖v‖ ^ 2 := by
  refine ⟨by rw [hT]; ring, ?_, fun v hv => by have := norm_pos_iff.2 hv; nlinarith⟩
  rw [gc_tangent_sq hT hperp]
  linarith

/-- **Row T4.** The line `P + t u` (`|u| = 1`) meets the throat exactly at the roots of
`t² + 2⟪P, u⟫ t + pow(P) = 0`. -/
theorem gc_meet {α : ℝ} {P u : E} (hu : ‖u‖ = 1) (t : ℝ) :
    ‖P + t • u‖ ^ 2 = α ^ 2 ↔ t ^ 2 + 2 * inner ℝ P u * t + (‖P‖ ^ 2 - α ^ 2) = 0 := by
  have h := norm_add_sq_real P (t • u)
  rw [inner_smul_right, norm_smul, Real.norm_eq_abs, hu, mul_one, sq_abs] at h
  rw [h]
  constructor <;> intro h' <;> linarith

/-- **Row T4.** The power of a point: the two meeting points of a secant have parameters with product `pow(P)`. -/
theorem gc_power {α t1 t2 : ℝ} {P u : E} (hu : ‖u‖ = 1) (h1 : ‖P + t1 • u‖ ^ 2 = α ^ 2)
    (h2 : ‖P + t2 • u‖ ^ 2 = α ^ 2) (hne : t1 ≠ t2) :
    t1 * t2 = ‖P‖ ^ 2 - α ^ 2 ∧ t1 + t2 = -(2 * inner ℝ P u) := by
  rw [gc_meet hu] at h1 h2
  have hs : t1 + t2 = -(2 * inner ℝ P u) := by
    have : (t1 - t2) * (t1 + t2 + 2 * inner ℝ P u) = 0 := by linear_combination h1 - h2
    rcases mul_eq_zero.1 this with h | h
    · exact absurd (sub_eq_zero.1 h) hne
    · linarith
  refine ⟨?_, hs⟩
  have : t2 = -(2 * inner ℝ P u) - t1 := by linarith
  subst this
  linear_combination -h1

/-- **Row T4.** Touch and cut. Lift an outside point `P` (`pow(P) > 0`) to its height, `x₀² = pow(P)`. The
displacement from `(x₀, P)` to the meeting point `(0, P + t u)` has `η = −x₀² + t²`. For a secant (two distinct
meeting points) neither displacement is null; for a tangent (a single, double, meeting point) the displacement is
null. -/
theorem gc_touch_cut {α x0 : ℝ} {P u : E} (hu : ‖u‖ = 1) (hpow : 0 < ‖P‖ ^ 2 - α ^ 2)
    (hx0 : x0 ^ 2 = ‖P‖ ^ 2 - α ^ 2) :
    (∀ t1 t2 : ℝ, ‖P + t1 • u‖ ^ 2 = α ^ 2 → ‖P + t2 • u‖ ^ 2 = α ^ 2 → t1 ≠ t2 →
        -x0 ^ 2 + ‖(P + t1 • u) - P‖ ^ 2 ≠ 0) ∧
      (∀ t : ℝ, ‖P + t • u‖ ^ 2 = α ^ 2 → (∀ t', ‖P + t' • u‖ ^ 2 = α ^ 2 → t' = t) →
        -x0 ^ 2 + ‖(P + t • u) - P‖ ^ 2 = 0) := by
  have hd : ∀ t : ℝ, ‖(P + t • u) - P‖ ^ 2 = t ^ 2 := fun t => by
    rw [add_sub_cancel_left, norm_smul, Real.norm_eq_abs, hu, mul_one, sq_abs]
  constructor
  · intro t1 t2 h1 h2 hne
    obtain ⟨hp, -⟩ := gc_power hu h1 h2 hne
    rw [hd, hx0, ← hp]
    have ht1 : t1 ≠ 0 := by rintro rfl; rw [zero_mul] at hp; linarith
    intro h
    have : t1 * (t1 - t2) = 0 := by linear_combination h
    rcases mul_eq_zero.1 this with h' | h'
    · exact ht1 h'
    · exact hne (sub_eq_zero.1 h')
  · intro t ht huniq
    -- the other root `−2⟪P, u⟫ − t` is also a meeting point, so it equals `t`
    have hq := (gc_meet hu t).1 ht
    have ho : ‖P + (-(2 * inner ℝ P u) - t) • u‖ ^ 2 = α ^ 2 := by
      rw [gc_meet hu]
      linear_combination hq
    have he := huniq _ ho
    rw [hd, hx0]
    have hb : inner ℝ P u = -t := by linarith
    rw [hb] at hq
    linear_combination -hq

end Tangent

/-- **Row T2.** The two tangency points from `P = (p₁, p₂)` outside the throat (`|P|² = q > α² > 0`):
`T± = (α²/q) P ± (α√(q − α²)/q) P^⊥`, with `ε = ±1`. -/
noncomputable def gc_tan (α p1 p2 ε : ℝ) : ℝ × ℝ :=
  let q := p1 ^ 2 + p2 ^ 2
  let k := α ^ 2 / q
  let m := ε * α * Real.sqrt (q - α ^ 2) / q
  (k * p1 - m * p2, k * p2 + m * p1)

/-- **Row T2.** Each `T±` lies on the throat, is a point of tangency (`⟪T, P − T⟫ = 0`), and the tangent length is
`√pow`; the two are distinct. -/
theorem gc_tangents {α p1 p2 ε : ℝ} (hα : 0 < α) (hq : α ^ 2 < p1 ^ 2 + p2 ^ 2) (hε : ε ^ 2 = 1) :
    (gc_tan α p1 p2 ε).1 ^ 2 + (gc_tan α p1 p2 ε).2 ^ 2 = α ^ 2 ∧
      (gc_tan α p1 p2 ε).1 * (p1 - (gc_tan α p1 p2 ε).1) + (gc_tan α p1 p2 ε).2 * (p2 - (gc_tan α p1 p2 ε).2) = 0 ∧
      (p1 - (gc_tan α p1 p2 ε).1) ^ 2 + (p2 - (gc_tan α p1 p2 ε).2) ^ 2 = p1 ^ 2 + p2 ^ 2 - α ^ 2 ∧
      gc_tan α p1 p2 1 ≠ gc_tan α p1 p2 (-1) := by
  have hq0 : 0 < p1 ^ 2 + p2 ^ 2 := lt_trans (by positivity) hq
  have hqne : p1 ^ 2 + p2 ^ 2 ≠ 0 := hq0.ne'
  have hr : Real.sqrt (p1 ^ 2 + p2 ^ 2 - α ^ 2) ^ 2 = p1 ^ 2 + p2 ^ 2 - α ^ 2 := Real.sq_sqrt (by linarith)
  have hrpos : 0 < Real.sqrt (p1 ^ 2 + p2 ^ 2 - α ^ 2) := Real.sqrt_pos.2 (by linarith)
  set r := Real.sqrt (p1 ^ 2 + p2 ^ 2 - α ^ 2) with hr_def
  set q := p1 ^ 2 + p2 ^ 2 with hq_def
  have hnorm : (gc_tan α p1 p2 ε).1 ^ 2 + (gc_tan α p1 p2 ε).2 ^ 2 = α ^ 2 := by
    simp only [gc_tan]
    rw [← hq_def, ← hr_def]
    field_simp
    linear_combination (α ^ 2 * ε ^ 2) * hq_def + (α ^ 2 * q) * hε + (α ^ 2 * ε ^ 2) * hr +
      (-α ^ 2 * r ^ 2 - α ^ 4 + r ^ 2 * (p1 ^ 2 + p2 ^ 2)) * hε + (p1 ^ 2 + p2 ^ 2 - α ^ 2) * hr +
      (p1 ^ 2 + p2 ^ 2 - α ^ 2) * hq_def
  have hdot : (gc_tan α p1 p2 ε).1 * p1 + (gc_tan α p1 p2 ε).2 * p2 = α ^ 2 := by
    simp only [gc_tan]
    rw [← hq_def, ← hr_def]
    field_simp
    linear_combination α ^ 2 * hq_def
  refine ⟨hnorm, by linear_combination hdot - hnorm, by linear_combination hnorm - 2 * hdot, ?_⟩
  intro h
  have h1 := congrArg Prod.fst h
  have h2 := congrArg Prod.snd h
  simp only [gc_tan] at h1 h2
  rw [← hq_def, ← hr_def] at h1 h2
  have e1 : α * r / q * p2 = 0 := by linear_combination -(h1 / 2)
  have e2 : α * r / q * p1 = 0 := by linear_combination h2 / 2
  have hc : α * r / q ≠ 0 := by positivity
  have := mul_eq_zero.1 e1
  have := mul_eq_zero.1 e2
  have hp1 : p1 = 0 := by tauto
  have hp2 : p2 = 0 := by tauto
  have : q = 0 := by rw [hq_def, hp1, hp2]; ring
  exact hqne this

/-! ## Non-vacuity -/

/-- **Witnesses.** A Lorentzian point (`α² = 1`, `x = (2, 0, 0, 0)`, `λ = −1/3`) with its eigenvector, and a Riemannian
one (`α² = 4`, `x = (1, 0, 0, 0)`, `λ = 4/3`); the tangency point `T = (1/2, √3/2)` from `P = (2, 0)` to the unit
throat, with the lifted tangent null at height `x₀ = √3`; and the secant through `P = 2` along `u = −1` on the line
`ℝ`, meeting the throat at `t = 1, 3`, with product `3 = pow(P)` and its meeting points not null. -/
theorem gc_witness :
    gc_lam 1 ![2, 0, 0, 0] = -(1 / 3) ∧ gc_lam 4 ![1, 0, 0, 0] = 4 / 3 ∧
      gc_g 1 ![2, 0, 0, 0] *ᵥ ![2, 0, 0, 0] = (-(1 / 3) : ℝ) • ![2, 0, 0, 0] ∧
      gc_tan 1 2 0 1 = (1 / 2, Real.sqrt 3 / 2) ∧
      -(Real.sqrt 3) ^ 2 + (2 - (gc_tan 1 2 0 1).1) ^ 2 + (0 - (gc_tan 1 2 0 1).2) ^ 2 = 0 ∧
      (1 : ℝ) * 3 = ‖(2 : ℝ)‖ ^ 2 - 1 ^ 2 ∧
      -(Real.sqrt 3) ^ 2 + ‖((2 : ℝ) + (1 : ℝ) • (-1 : ℝ)) - 2‖ ^ 2 ≠ 0 := by
  have hl : gc_lam 1 ![2, 0, 0, 0] = -(1 / 3) := by
    simp [gc_lam, dotProduct, Fin.sum_univ_four]; norm_num
  have hs3 : Real.sqrt 3 ^ 2 = 3 := Real.sq_sqrt (by norm_num)
  have hu : ‖(-1 : ℝ)‖ = 1 := by norm_num
  have m1 : ‖(2 : ℝ) + (1 : ℝ) • (-1 : ℝ)‖ ^ 2 = 1 ^ 2 := by norm_num
  have m3 : ‖(2 : ℝ) + (3 : ℝ) • (-1 : ℝ)‖ ^ 2 = 1 ^ 2 := by norm_num
  refine ⟨hl, by simp [gc_lam, dotProduct, Fin.sum_univ_four]; norm_num, ?_, ?_, ?_,
    (gc_power hu m1 m3 (by norm_num)).1,
    (gc_touch_cut (α := 1) (x0 := Real.sqrt 3) hu (by norm_num) (by rw [hs3]; norm_num)).1 1 3 m1 m3
      (by norm_num)⟩
  · rw [(gc_eigen (by simp [dotProduct, Fin.sum_univ_four]; norm_num)).1, hl]
  · refine Prod.ext (by simp [gc_tan]; norm_num) (by simp [gc_tan]; norm_num; ring)
  · have := (gc_tangents (α := 1) (p1 := 2) (p2 := 0) (ε := 1) one_pos (by norm_num) (by norm_num)).2.2.1
    rw [hs3]
    linarith

end ShadowProbe.GeometricCoreProbe

#print axioms ShadowProbe.GeometricCoreProbe.gc_line_element
#print axioms ShadowProbe.GeometricCoreProbe.gc_g_entry
#print axioms ShadowProbe.GeometricCoreProbe.gc_g_mulVec
#print axioms ShadowProbe.GeometricCoreProbe.gc_eigen
#print axioms ShadowProbe.GeometricCoreProbe.gc_sign
#print axioms ShadowProbe.GeometricCoreProbe.gc_pole
#print axioms ShadowProbe.GeometricCoreProbe.gc_det_ne_zero_limit
#print axioms ShadowProbe.GeometricCoreProbe.gc_tangent_sq
#print axioms ShadowProbe.GeometricCoreProbe.gc_tangent_null
#print axioms ShadowProbe.GeometricCoreProbe.gc_meet
#print axioms ShadowProbe.GeometricCoreProbe.gc_power
#print axioms ShadowProbe.GeometricCoreProbe.gc_touch_cut
#print axioms ShadowProbe.GeometricCoreProbe.gc_tangents
#print axioms ShadowProbe.GeometricCoreProbe.gc_witness

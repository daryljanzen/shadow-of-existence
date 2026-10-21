import ShadowEngine
import Mathlib.Analysis.SpecialFunctions.NonIntegrable
import Mathlib.Analysis.SpecialFunctions.Integrals.Basic
import Mathlib.Analysis.SpecialFunctions.Arsinh
import Mathlib.Analysis.Complex.ExponentialBounds

/-! # Campaign 46, the Nariai group of LIMIT rows: 12, 21, 100, 101, 105

Each row's receipt's COMPUTED checks, built (text pins and symbol-occurrence checks excepted). Copied, not
imported, from `probes/CurvatureInstances.lean`: the `sin²` facts and the SdS radial derivatives; everything
else is the engine (`import ShadowEngine`: `fSdS`, `diag_curv`, `curvD_eq`, `cS` and its recipe). -/

open Real Filter Topology Set MeasureTheory
open scoped ContDiff

/-- `field_simp`, then `ring` if anything is left. -/
macro "fsr" : tactic => `(tactic| (field_simp; try ring))

namespace ShadowProbe.LimitNariai


/-! ## Common: the Nariai member of `f = 1 − 2M/r − r²/α²` (the engine's `fSdS`), `ρ = α/√3`, `M = α/(3√3)` -/

lemma s3 : √3 ^ 2 = 3 := Real.sq_sqrt (by norm_num)
lemma s3pos : 0 < √3 := by positivity

lemma rho_sq (α : ℝ) : (α / √3) ^ 2 = α ^ 2 / 3 := by rw [div_pow, s3]

lemma MN_eq (α : ℝ) : α / (3 * √3) = α / √3 / 3 := by rw [div_div, mul_comm]

lemma d1 (M α : ℝ) {r : ℝ} (hr : r ≠ 0) : deriv (fSdS M α) r = 2 * M / r ^ 2 - 2 * r / α ^ 2 :=
  (fSdS_hasDerivAt M α hr).deriv

lemma d2 (M α : ℝ) {r : ℝ} (hr : r ≠ 0) : deriv (deriv (fSdS M α)) r = -(4 * M / r ^ 3) - 2 / α ^ 2 := by
  have e : deriv (fSdS M α) =ᶠ[𝓝 r] fun s => 2 * M * (s ^ 2)⁻¹ - 2 * s / α ^ 2 :=
    eventually_of_mem (isOpen_ne.mem_nhds hr) fun s hs => (d1 M α hs).trans (by ring)
  rw [e.deriv_eq, (show HasDerivAt (fun s => 2 * M * (s ^ 2)⁻¹ - 2 * s / α ^ 2) _ r from
    (((hasDerivAt_pow 2 r).inv (pow_ne_zero 2 hr)).const_mul (2 * M)).sub
    (((hasDerivAt_id' r).const_mul 2).div_const (α ^ 2))).deriv]
  fsr

/-- `−α² r f = (r − ρ)²(r + 2ρ)` at the Nariai mass. -/
lemma factor {α ρ r : ℝ} (hα : α ≠ 0) (hr : r ≠ 0) (h2 : α ^ 2 = 3 * ρ ^ 2) :
    α ^ 2 * r * fSdS (ρ / 3) α r = -((r - ρ) ^ 2 * (r + 2 * ρ)) := by
  have : α ^ 2 * r * fSdS (ρ / 3) α r = α ^ 2 * r - 2 * ρ * α ^ 2 / 3 - r ^ 3 := by
    unfold fSdS; field_simp
  rw [this]; linear_combination (r - 2 * ρ / 3) * h2

lemma f_eq {α ρ r : ℝ} (hα : α ≠ 0) (hr : r ≠ 0) (h2 : α ^ 2 = 3 * ρ ^ 2) :
    fSdS (ρ / 3) α r = -((r - ρ) ^ 2 * (r + 2 * ρ)) / (α ^ 2 * r) := by
  rw [← factor hα hr h2]; field_simp

lemma f_nonpos {α ρ r : ℝ} (hα : α ≠ 0) (hρ : 0 < ρ) (hr : 0 < r) (h2 : α ^ 2 = 3 * ρ ^ 2) :
    fSdS (ρ / 3) α r ≤ 0 := by
  rw [f_eq hα hr.ne' h2]
  exact div_nonpos_of_nonpos_of_nonneg (neg_nonpos.2 (by positivity)) (by positivity)

lemma f_neg {α ρ r : ℝ} (hα : α ≠ 0) (hρ : 0 < ρ) (hr : 0 < r) (hne : r ≠ ρ) (h2 : α ^ 2 = 3 * ρ ^ 2) :
    fSdS (ρ / 3) α r < 0 := by
  rw [f_eq hα hr.ne' h2]
  have : 0 < (r - ρ) ^ 2 := by have := sub_ne_zero.2 hne; positivity
  exact div_neg_of_neg_of_pos (neg_neg_of_pos (by positivity)) (by positivity)

/-- The Nariai data in `α`: `ρ = α/√3`, `α² = 3ρ²`, `M_N = ρ/3`. -/
lemma nar (α : ℝ) : α ^ 2 = 3 * (α / √3) ^ 2 ∧ α / (3 * √3) = α / √3 / 3 :=
  ⟨by rw [rho_sq]; ring, MN_eq α⟩

/-- The three Nariai values `f(ρ) = f′(ρ) = 0`, `f″(ρ) = −6/α²`. -/
lemma nariai_vals {α : ℝ} (hα : 0 < α) :
    fSdS (α / (3 * √3)) α (α / √3) = 0 ∧ deriv (fSdS (α / (3 * √3)) α) (α / √3) = 0 ∧
      deriv (deriv (fSdS (α / (3 * √3)) α)) (α / √3) = -6 / α ^ 2 := by
  obtain ⟨h2, hM⟩ := nar α
  have hρ : α / √3 ≠ 0 := by positivity
  rw [hM, d1 _ _ hρ, d2 _ _ hρ]
  refine ⟨?_, ?_, ?_⟩
  · have h := factor hα.ne' hρ h2
    have hne : α ^ 2 * (α / √3) ≠ 0 := by positivity
    exact (mul_eq_zero.1 (by rw [h]; ring)).resolve_left hne
  · rw [h2]; fsr
  · rw [h2]; fsr

/-! ## Row 105 — `P16_nariai_welds.py` -/

/-- The turnover: on `r > 0`, `f′(r) = 0 ⇔ r³ = Mα²` (the receipt's `tp = (Mα²)^{1/3}`). -/
lemma turnover (M : ℝ) {α r : ℝ} (hα : α ≠ 0) (hr : 0 < r) :
    deriv (fSdS M α) r = 0 ↔ r ^ 3 = M * α ^ 2 := by
  rw [d1 M α hr.ne']
  constructor
  · intro h; field_simp at h; linarith
  · intro h; field_simp; linarith

lemma cube_root {α : ℝ} (hα : 0 < α) : (α / (3 * √3) * α ^ 2) ^ (1 / 3 : ℝ) = α / √3 := by
  have : α / (3 * √3) * α ^ 2 = (α / √3) ^ 3 := by
    have h3 : √3 ^ 3 = 3 * √3 := by rw [pow_succ, s3]
    rw [div_pow, h3]; ring
  rw [this, show (1 / 3 : ℝ) = ((3 : ℕ) : ℝ)⁻¹ by norm_num]
  exact pow_rpow_inv_natCast (by positivity) (by norm_num)

/-- **Row 105.** At `M_N = α/(3√3)`: `f(ρ) = f′(ρ) = 0`, `f″(ρ) = −6/α²`; the turnover `(M_Nα²)^{1/3}` is `ρ`
and is the only zero of `f′` on `r > 0`; `−α² r f = (r − ρ)²(r + 2ρ)`, so `f ≤ 0` on ALL of `r > 0` with
equality only at `ρ` (the receipt's eight samples are instances); and `(dr/dτ)² = 1 − f = 1` at `ρ`. -/
theorem row105_checks {α : ℝ} (hα : 0 < α) :
    fSdS (α / (3 * √3)) α (α / √3) = 0 ∧ deriv (fSdS (α / (3 * √3)) α) (α / √3) = 0 ∧
      deriv (deriv (fSdS (α / (3 * √3)) α)) (α / √3) = -6 / α ^ 2 ∧
      (α / (3 * √3) * α ^ 2) ^ (1 / 3 : ℝ) = α / √3 ∧
      (∀ r > 0, deriv (fSdS (α / (3 * √3)) α) r = 0 ↔ r = α / √3) ∧
      (∀ r ≠ 0, -(α ^ 2 * r * fSdS (α / (3 * √3)) α r) = (r - α / √3) ^ 2 * (r + 2 * (α / √3))) ∧
      (∀ r > 0, fSdS (α / (3 * √3)) α r ≤ 0) ∧ (∀ r > 0, fSdS (α / (3 * √3)) α r = 0 → r = α / √3) ∧
      (∀ x ∈ [0.1, 0.3, 0.5, 0.577, 0.7, 1, 2, 5], fSdS (1 / (3 * √3)) 1 x ≤ 0) ∧
      1 - fSdS (α / (3 * √3)) α (α / √3) = 1 := by
  obtain ⟨h2, hM⟩ := nar α
  have hρ : 0 < α / √3 := by positivity
  obtain ⟨v0, v1, v2⟩ := nariai_vals hα
  refine ⟨v0, v1, v2, cube_root hα, fun r hr => ?_, fun r hr => ?_, fun r hr => ?_, fun r hr h0 => ?_,
    fun x hx => ?_, by rw [v0]; ring⟩
  · rw [turnover _ hα.ne' hr]
    have hc : α / (3 * √3) * α ^ 2 = (α / √3) ^ 3 := by
      have := cube_root hα
      rw [← this, show (1 / 3 : ℝ) = ((3 : ℕ) : ℝ)⁻¹ by norm_num,
        rpow_inv_natCast_pow (by positivity) (by norm_num)]
    rw [hc]
    exact ⟨fun h => (pow_left_inj₀ hr.le hρ.le (by norm_num : (3 : ℕ) ≠ 0)).1 h, fun h => by rw [h]⟩
  · rw [hM, factor hα.ne' hr h2]; ring
  · rw [hM]; exact f_nonpos hα.ne' hρ hr h2
  · by_contra hne; rw [hM] at h0; exact (f_neg hα.ne' hρ hr hne h2).ne h0
  · have h1 := nar (1 : ℝ)
    rw [show (1 : ℝ) / (3 * √3) = 1 / √3 / 3 from h1.2]
    refine f_nonpos one_ne_zero (by positivity) ?_ h1.1
    simp only [List.mem_cons, List.not_mem_nil, or_false] at hx
    rcases hx with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl <;> norm_num

/-! ## Row 12 — `P6_the_nariai_frame_does_not_exist…` -/

/-- **Row 12, ⓵.** The double root, `f″(r_n) = −6/α² < 0`; `f < 0` on `r > 0` off `r_n` (the receipt's four
samples at `α = 1` are instances), so no `r > 0` has `f > 0`: the static region is the single point `r_n`. -/
theorem row12_checks {α : ℝ} (hα : 0 < α) :
    fSdS (α / (3 * √3)) α (α / √3) = 0 ∧ deriv (fSdS (α / (3 * √3)) α) (α / √3) = 0 ∧
      deriv (deriv (fSdS (α / (3 * √3)) α)) (α / √3) = -6 / α ^ 2 ∧
      deriv (deriv (fSdS (α / (3 * √3)) α)) (α / √3) < 0 ∧
      (∀ r > 0, r ≠ α / √3 → fSdS (α / (3 * √3)) α r < 0) ∧
      (∀ x ∈ [0.40, 0.50, 0.60, 0.70], fSdS (1 / (3 * √3)) 1 x < 0) ∧
      ¬ ∃ r > 0, 0 < fSdS (α / (3 * √3)) α r := by
  obtain ⟨h2, hM⟩ := nar α
  have hρ : 0 < α / √3 := by positivity
  obtain ⟨v0, v1, v2⟩ := nariai_vals hα
  refine ⟨v0, v1, v2, by rw [v2]; exact div_neg_of_neg_of_pos (by norm_num) (by positivity),
    fun r hr hne => ?_, fun x hx => ?_, fun ⟨r, hr, hp⟩ => ?_⟩
  · rw [hM]; exact f_neg hα.ne' hρ hr hne h2
  · have h1 := nar (1 : ℝ)
    rw [show (1 : ℝ) / (3 * √3) = 1 / √3 / 3 from h1.2]
    have hs : ∀ x : ℝ, x ^ 2 * 3 ≠ 1 → x ≠ 1 / √3 := fun x hx h => hx (by
      rw [h, div_pow, s3]; norm_num)
    simp only [List.mem_cons, List.not_mem_nil, or_false] at hx
    rcases hx with rfl | rfl | rfl | rfl <;>
      exact f_neg one_ne_zero (by positivity) (by norm_num) (hs _ (by norm_num)) h1.1
  · rw [hM] at hp; exact absurd (f_nonpos hα.ne' hρ hr h2) (not_le.2 hp)

/-- **Row 12, ⓶.** The blueshift `1/√(2κδ)`: `·√δ → 1/√(2κ)` (so it goes as `δ^{-1/2}`), it is finite and positive
at every `δ > 0` (at `κ = δ = 1` it is `√2/2`), and it diverges only as `δ → 0⁺`. -/
theorem row12_blueshift {κ : ℝ} (hκ : 0 < κ) :
    Tendsto (fun δ => 1 / √(2 * κ * δ) * √δ) (𝓝[>] 0) (𝓝 (1 / √(2 * κ))) ∧
      (∀ δ > 0, 0 < 1 / √(2 * κ * δ)) ∧ 1 / √(2 * 1 * 1) = √2 / 2 ∧
      Tendsto (fun δ => 1 / √(2 * κ * δ)) (𝓝[>] 0) atTop := by
  refine ⟨?_, fun δ hδ => by positivity, ?_, ?_⟩
  · refine tendsto_const_nhds.congr' (eventually_nhdsWithin_of_forall fun δ (hδ : 0 < δ) => ?_)
    show 1 / √(2 * κ) = 1 / √(2 * κ * δ) * √δ
    rw [sqrt_mul (by positivity : (0 : ℝ) ≤ 2 * κ) δ]; have := sqrt_pos.2 hδ; field_simp
  · rw [mul_one, mul_one, div_eq_div_iff (by positivity) (by norm_num), ← sq, Real.sq_sqrt (by norm_num)]; ring
  · have h0 : Tendsto (fun δ => √(2 * κ * δ)) (𝓝[>] 0) (𝓝[>] 0) := by
      refine tendsto_nhdsWithin_iff.2 ⟨?_, eventually_nhdsWithin_of_forall fun δ (hδ : 0 < δ) => by
        show 0 < √(2 * κ * δ); positivity⟩
      have : Continuous fun δ : ℝ => √(2 * κ * δ) := by fun_prop
      simpa using (this.tendsto 0).mono_left nhdsWithin_le_nhds
    simp only [one_div]; exact tendsto_inv_nhdsGT_zero.comp h0

/-! ## Row 21 — `S1_the_nariai_closed_form_extends…` -/

/-- **Row 21.** `f′ = 0 ⇔ M = r³/α²`; with that `M`, `f(r_n) = 0` at `r_n = α/√3 = 1/√Λ`; `M_N = α/(3√3)`;
`f″(r_n) = −6/α²`; the throat's `L² = 2/|f″(r_n)| = α²/3 = r_n²`; and the receipt's LEADING-ORDER truncation
`½f″(r_n)dr² + ∂_M f(r_n)·(−δM) = 0`, with `∂_M f(r_n) = −2/r_n`, is `dr² = (2/r_n)/(3/α²)·δM`: `dr² ∝ δM`
with an `α`-only coefficient, vanishing at `δM = 0`. -/
theorem row21_checks {α : ℝ} (hα : 0 < α) :
    (∀ M r, r ≠ 0 → (deriv (fSdS M α) r = 0 ↔ M = r ^ 3 / α ^ 2)) ∧
      fSdS ((α / √3) ^ 3 / α ^ 2) α (α / √3) = 0 ∧
      (∀ Λ > 0, α = √(3 / Λ) → α / √3 = 1 / √Λ) ∧
      (α / √3) ^ 3 / α ^ 2 = α / (3 * √3) ∧
      deriv (deriv (fSdS (α / (3 * √3)) α)) (α / √3) = -6 / α ^ 2 ∧
      2 / -deriv (deriv (fSdS (α / (3 * √3)) α)) (α / √3) = (α / √3) ^ 2 ∧
      2 / -deriv (deriv (fSdS (α / (3 * √3)) α)) (α / √3) = α ^ 2 / 3 ∧
      HasDerivAt (fun m => fSdS m α (α / √3)) (-2 / (α / √3)) (α / (3 * √3)) ∧
      (∀ dr δM, 1 / 2 * deriv (deriv (fSdS (α / (3 * √3)) α)) (α / √3) * dr ^ 2 + -2 / (α / √3) * -δM = 0
        ↔ dr ^ 2 = (-(-2 / (α / √3))) / (-(1 / 2 * deriv (deriv (fSdS (α / (3 * √3)) α)) (α / √3))) * δM) ∧
      (-(-2 / (α / √3))) / (-(1 / 2 * deriv (deriv (fSdS (α / (3 * √3)) α)) (α / √3)))
        = 2 * √3 * α / 3 := by
  obtain ⟨h2, hM⟩ := nar α
  have hρ : 0 < α / √3 := by positivity
  obtain ⟨v0, v1, v2⟩ := nariai_vals hα
  have hMr : (α / √3) ^ 3 / α ^ 2 = α / (3 * √3) := by
    rw [hM, h2]; field_simp
  have s3n := s3pos.ne'
  refine ⟨fun M r hr => ?_, by rw [hMr]; exact v0, fun Λ hΛ he => ?_, hMr, v2, ?_, ?_, ?_, fun dr δM => ?_, ?_⟩
  · rw [d1 M α hr]; constructor
    · intro h; field_simp at h ⊢; linarith
    · intro h; rw [h]; fsr
  · rw [he, div_eq_div_iff s3n (by positivity), one_mul, ← sqrt_mul (by positivity)]
    rw [show 3 / Λ * Λ = 3 by field_simp]
  · rw [v2, rho_sq]; field_simp; norm_num
  · rw [v2]; field_simp; norm_num
  · have : HasDerivAt (fun m => fSdS m α (α / √3)) (-(2 * 1 / (α / √3))) (α / (3 * √3)) := by
      unfold fSdS
      exact ((((hasDerivAt_id _).const_mul 2).div_const _).const_sub 1).sub_const _
    convert this using 1; ring
  · rw [v2]; constructor <;> intro h
    · field_simp at h ⊢; linarith
    · rw [h]; fsr
  · rw [v2]; field_simp; norm_num




/-! ## Row 100 — the normal-time integral `∫dr/√(−f)` at the Nariai member -/

/-- The integrand of the normal proper time, `1/√(−f)`. -/
noncomputable def Fint (α ρ r : ℝ) : ℝ := 1 / √(-fSdS (ρ / 3) α r)

/-- `q(s) = 3ρ²(ρ+s)/(3ρ+s)`, so that `−f(ρ+s) = s²/q(s)` and `1/√(−f(ρ+s)) = √q(s)/s`. -/
noncomputable def q (ρ s : ℝ) : ℝ := 3 * ρ ^ 2 * (ρ + s) / (3 * ρ + s)

section Div

variable {α ρ : ℝ} (hρ : 0 < ρ) (h2 : α ^ 2 = 3 * ρ ^ 2)
include hρ

lemma q_pos {s : ℝ} (hs : 0 ≤ s) : 0 < q ρ s := by unfold q; positivity

lemma q_sub {s : ℝ} (hs : 0 ≤ s) : q ρ s - ρ ^ 2 = 2 * ρ ^ 2 * s / (3 * ρ + s) := by
  unfold q; fsr

lemma sqrt_q_ge {s : ℝ} (hs : 0 ≤ s) : ρ ≤ √(q ρ s) := by
  have h1 := q_sub hρ hs
  have h3 : 0 ≤ 2 * ρ ^ 2 * s / (3 * ρ + s) := by positivity
  exact (le_sqrt hρ.le (q_pos hρ hs).le).2 (by linarith)

lemma sqrt_q_gt {s : ℝ} (hs : 0 < s) : ρ < √(q ρ s) := by
  have h1 := q_sub hρ hs.le
  have h3 : 0 < 2 * ρ ^ 2 * s / (3 * ρ + s) := by positivity
  exact (lt_sqrt hρ.le).2 (by linarith)

lemma sqrt_q_le {s : ℝ} (hs : 0 ≤ s) : √(q ρ s) ≤ ρ + s / 3 := by
  refine (sqrt_le_sqrt ?_).trans_eq (sqrt_sq (by positivity))
  unfold q; rw [div_le_iff₀ (by positivity)]; nlinarith [sq_nonneg s, mul_nonneg hρ.le hs]

lemma q_lt {s t : ℝ} (hs : 0 ≤ s) (hst : s < t) : q ρ s < q ρ t := by
  unfold q; rw [div_lt_div_iff₀ (by positivity) (by linarith)]; nlinarith [mul_pos (pow_pos hρ 2) hρ]

include h2

lemma negf_shift {s : ℝ} (hs : 0 < s) : -fSdS (ρ / 3) α (ρ + s) = s ^ 2 / q ρ s := by
  have hα : α ≠ 0 := fun h => by rw [h] at h2; nlinarith [pow_pos hρ 2]
  rw [f_eq hα (by positivity) h2, h2]; unfold q; fsr

lemma Fint_shift {s : ℝ} (hs : 0 < s) : Fint α ρ (ρ + s) = √(q ρ s) / s := by
  unfold Fint
  rw [negf_shift hρ h2 hs, sqrt_div (sq_nonneg s), sqrt_sq hs.le]
  have := (sqrt_pos.2 (q_pos hρ hs.le)).ne'; field_simp

omit h2 in
lemma cont_G {a b : ℝ} (ha : 0 < a) (c : ℝ) (hc : 0 < c) :
    ContinuousOn (fun s => √(q ρ (s / c)) / s) (Icc a b) := by
  refine ContinuousOn.div ?_ continuousOn_id fun x hx => (ha.trans_le hx.1).ne'
  refine Real.continuous_sqrt.comp_continuousOn ?_
  unfold q
  refine ContinuousOn.div (by fun_prop) (by fun_prop) fun x hx => ?_
  have := ha.trans_le hx.1; positivity

lemma int_shift {a b : ℝ} (ha : 0 < a) (hab : a ≤ b) :
    ∫ r in ρ + a..ρ + b, Fint α ρ r = ∫ s in a..b, √(q ρ s) / s := by
  rw [← intervalIntegral.integral_comp_add_left]
  refine intervalIntegral.integral_congr fun s hs => ?_
  rw [uIcc_of_le hab] at hs
  exact Fint_shift hρ h2 (ha.trans_le hs.1)

omit hρ h2 in
lemma int_inv {a b : ℝ} (ha : 0 < a) (hb : 0 < b) (c : ℝ) : ∫ s in a..b, c / s = c * log (b / a) := by
  simp_rw [div_eq_mul_inv c]; rw [intervalIntegral.integral_const_mul, integral_inv_of_pos ha hb]

/-- The two-sided log bound on `0 < a < b`: `ρ log(b/a) < ∫_{ρ+a}^{ρ+b} dr/√(−f) ≤ (ρ + b/3) log(b/a)`. -/
lemma log_bounds {a b : ℝ} (ha : 0 < a) (hab : a < b) :
    ρ * log (b / a) < ∫ r in ρ + a..ρ + b, Fint α ρ r ∧
      ∫ r in ρ + a..ρ + b, Fint α ρ r ≤ (ρ + b / 3) * log (b / a) := by
  have hb : 0 < b := ha.trans hab
  rw [int_shift hρ h2 ha hab.le, ← int_inv ha hb, ← int_inv ha hb]
  have cG := cont_G hρ ha (b := b) 1 one_pos
  simp only [div_one] at cG
  have cI : ∀ c : ℝ, ContinuousOn (fun s => c / s) (Icc a b) := fun c =>
    continuousOn_const.div continuousOn_id fun x hx => (ha.trans_le hx.1).ne'
  refine ⟨intervalIntegral.integral_lt_integral_of_continuousOn_of_le_of_exists_lt hab (cI ρ) cG
    (fun x hx => div_le_div_of_nonneg_right (sqrt_q_ge hρ (ha.trans hx.1).le) (ha.trans hx.1).le)
    ⟨b, right_mem_Icc.2 hab.le, div_lt_div_of_pos_right (sqrt_q_gt hρ hb) hb⟩, ?_⟩
  refine intervalIntegral.integral_mono_on hab.le (cG.intervalIntegrable_of_Icc hab.le)
    ((cI _).intervalIntegrable_of_Icc hab.le) fun x hx => ?_
  have hx0 : 0 < x := ha.trans_le hx.1
  refine div_le_div_of_nonneg_right ((sqrt_q_le hρ hx0.le).trans ?_) hx0.le
  linarith [hx.2]

/-- **The log divergence, analytically.** `∫_{ρ+ε}^{ρ+1} dr/√(−f) > ρ log(1/ε) → ∞` as `ε → 0⁺`. -/
lemma log_divergence :
    (∀ ε, 0 < ε → ε < 1 → ρ * log (1 / ε) < ∫ r in ρ + ε..ρ + 1, Fint α ρ r) ∧
      Tendsto (fun ε => ∫ r in ρ + ε..ρ + 1, Fint α ρ r) (𝓝[>] 0) atTop := by
  refine ⟨fun ε h0 h1 => (log_bounds hρ h2 h0 h1).1, ?_⟩
  have hl : Tendsto (fun ε => ρ * log (1 / ε)) (𝓝[>] 0) atTop := by
    simp_rw [one_div, log_inv]
    exact (tendsto_neg_atBot_atTop.comp tendsto_log_nhdsGT_zero).const_mul_atTop hρ
  refine tendsto_atTop_mono' _ ?_ hl
  filter_upwards [Ioo_mem_nhdsGT one_pos] with ε hε
  exact (log_bounds hρ h2 hε.1 hε.2).1.le

/-- **Non-integrability** on any interval containing `ρ`: `(r − ρ)⁻¹ = O(1/√(−f))` near `ρ`. -/
lemma not_integrable {a b : ℝ} (hne : a ≠ b) (hc : ρ ∈ uIcc a b) :
    ¬ IntervalIntegrable (Fint α ρ) volume a b := by
  have hα : α ≠ 0 := fun h => by rw [h] at h2; nlinarith [pow_pos hρ 2]
  refine not_intervalIntegrable_of_sub_inv_isBigO_punctured (Asymptotics.IsBigO.of_bound (3 / |α|) ?_) hne hc
  filter_upwards [nhdsWithin_le_nhds (Ioo_mem_nhds (by linarith : ρ / 2 < ρ) (by linarith : ρ < 2 * ρ)),
    self_mem_nhdsWithin] with x hx hne'
  have hx0 : 0 < x := by linarith [hx.1]
  have hD : 0 < |x - ρ| := abs_pos.2 (sub_ne_zero.2 hne')
  have hfe := f_eq hα hx0.ne' h2
  have hnf : -fSdS (ρ / 3) α x = (x - ρ) ^ 2 * (x + 2 * ρ) / (α ^ 2 * x) := by rw [hfe]; ring
  have hpos : 0 < -fSdS (ρ / 3) α x := by
    have hne2 : x - ρ ≠ 0 := sub_ne_zero.2 hne'
    rw [hnf]; have : 0 < (x - ρ) ^ 2 := by positivity
    positivity
  have hle : -fSdS (ρ / 3) α x ≤ (3 * |x - ρ| / |α|) ^ 2 := by
    rw [hnf, div_pow, mul_pow, sq_abs, sq_abs, div_le_div_iff₀ (by positivity) (by positivity)]
    nlinarith [mul_nonneg (mul_nonneg (sq_nonneg α) (sq_nonneg (x - ρ))) (by linarith [hx.1] : 0 ≤ 8 * x - 2 * ρ)]
  have hS : √(-fSdS (ρ / 3) α x) ≤ 3 * |x - ρ| / |α| :=
    (sqrt_le_sqrt hle).trans (sqrt_sq (by positivity)).le
  have hSp := sqrt_pos.2 hpos
  rw [Real.norm_eq_abs, Real.norm_eq_abs, abs_inv, Fint, abs_of_pos (show 0 < 1 / √(-fSdS (ρ / 3) α x) by positivity)]
  rw [show 3 / |α| * (1 / √(-fSdS (ρ / 3) α x)) = 1 / (|α| * √(-fSdS (ρ / 3) α x) / 3) by
    field_simp, ← one_div]
  refine one_div_le_one_div_of_le (by positivity) ?_
  rw [le_div_iff₀ (by positivity)] at hS
  have := abs_pos.2 hα
  nlinarith

/-- The increment of normal time over one decade of approach, `∫_{ρ+h/10}^{ρ+h} dr/√(−f)`. -/
noncomputable def incr (α ρ h : ℝ) : ℝ := ∫ r in ρ + h / 10..ρ + h, Fint α ρ r

lemma incr_bounds {h : ℝ} (hh : 0 < h) :
    ρ * log 10 < incr α ρ h ∧ incr α ρ h ≤ (ρ + h / 3) * log 10 := by
  have := log_bounds hρ h2 (a := h / 10) (b := h) (by positivity) (by linarith)
  rwa [show h / (h / 10) = 10 by field_simp] at this

lemma incr_anti {h : ℝ} (hh : 0 < h) : incr α ρ (h / 10) < incr α ρ h := by
  unfold incr
  rw [int_shift hρ h2 (by positivity) (by linarith), int_shift hρ h2 (by positivity) (by linarith)]
  have hcv := intervalIntegral.integral_comp_div (a := h / 10) (b := h) (fun s => √(q ρ s) / s)
    (by norm_num : (10 : ℝ) ≠ 0)
  have e : ∫ s in h / 10 / 10..h / 10, √(q ρ s) / s = ∫ s in h / 10..h, √(q ρ (s / 10)) / s := by
    have : ∫ s in h / 10..h, √(q ρ (s / 10)) / s
        = (1 / 10) * ∫ s in h / 10..h, (fun s => √(q ρ s) / s) (s / 10) := by
      rw [← intervalIntegral.integral_const_mul]; congr 1; funext s; beta_reduce; rw [div_div_eq_mul_div]; ring
    rw [this, hcv, smul_eq_mul]; ring
  rw [e]
  have c1 := cont_G hρ (a := h / 10) (b := h) (by positivity) 1 one_pos
  simp only [div_one] at c1
  refine intervalIntegral.integral_lt_integral_of_continuousOn_of_le_of_exists_lt (by linarith)
    (cont_G hρ (by positivity) 10 (by norm_num)) c1 (fun x hx => ?_) ⟨h, right_mem_Icc.2 (by linarith), ?_⟩
  · have hx0 : 0 < x := by linarith [hx.1]
    exact div_le_div_of_nonneg_right (sqrt_le_sqrt (q_lt hρ (by positivity) (by linarith)).le) hx0.le
  · exact div_lt_div_of_pos_right (sqrt_lt_sqrt (q_pos hρ (by positivity)).le
      (q_lt hρ (by positivity) (by linarith))) hh

lemma incr_tendsto : Tendsto (fun d : ℕ => incr α ρ ((1 / 10) ^ d)) atTop (𝓝 (ρ * log 10)) := by
  have hu : Tendsto (fun d : ℕ => (ρ + (1 / 10 : ℝ) ^ d / 3) * log 10) atTop (𝓝 ((ρ + 0 / 3) * log 10)) :=
    ((tendsto_const_nhds.add ((tendsto_pow_atTop_nhds_zero_of_lt_one (by norm_num) (by norm_num)).div_const 3)).mul_const _)
  rw [zero_div, add_zero] at hu
  exact tendsto_of_tendsto_of_tendsto_of_le_of_le tendsto_const_nhds hu
    (fun d => (incr_bounds hρ h2 (by positivity)).1.le) (fun d => (incr_bounds hρ h2 (by positivity)).2)

/-- On `t ∈ (0, 1]`, at the SIMPLE root `−2ρ`: `1/√(−f(−2ρ − t)) ≤ √((2ρ+1)/3)/√t`. -/
lemma simple_bd {t : ℝ} (ht0 : 0 < t) (ht1 : t ≤ 1) :
    Fint α ρ (-2 * ρ - t) ≤ √((2 * ρ + 1) / 3) / √t := by
  have hα : α ≠ 0 := fun h => by rw [h] at h2; nlinarith [pow_pos hρ 2]
  have hr : (-2 * ρ - t) ≠ 0 := by linarith
  have hnf : -fSdS (ρ / 3) α (-2 * ρ - t) = (3 * ρ + t) ^ 2 * t / (3 * ρ ^ 2 * (2 * ρ + t)) := by
    have hp : 0 < 2 * ρ + t := by positivity
    rw [f_eq hα hr h2, h2, show -2 * ρ - t - ρ = -(3 * ρ + t) by ring, show -2 * ρ - t + 2 * ρ = -t by ring,
      show -2 * ρ - t = -(2 * ρ + t) by ring]
    fsr
  have key : t ≤ (2 * ρ + 1) / 3 * -fSdS (ρ / 3) α (-2 * ρ - t) := by
    rw [hnf, ← mul_div_assoc, le_div_iff₀ (by positivity)]
    have h9 : 9 * ρ ^ 2 ≤ (3 * ρ + t) ^ 2 := by nlinarith
    nlinarith [mul_le_mul (by linarith : 2 * ρ + t ≤ 2 * ρ + 1) h9 (by positivity) (by positivity)]
  have hpos : 0 < -fSdS (ρ / 3) α (-2 * ρ - t) := by rw [hnf]; positivity
  unfold Fint
  rw [div_le_div_iff₀ (sqrt_pos.2 hpos) (sqrt_pos.2 ht0), one_mul, ← sqrt_mul (by positivity)]
  exact sqrt_le_sqrt key

/-- The dominating function `√((2ρ+1)/3)·(−2ρ − r)^{−1/2}` on `[−2ρ − 1, −2ρ]`. -/
lemma simple_dom {r : ℝ} (hr : r ∈ Icc (-2 * ρ - 1) (-2 * ρ)) :
    Fint α ρ r ≤ √((2 * ρ + 1) / 3) * (-2 * ρ - r) ^ (-(1 / 2) : ℝ) := by
  have hα : α ≠ 0 := fun h => by rw [h] at h2; nlinarith [pow_pos hρ 2]
  rcases eq_or_lt_of_le hr.2 with h | h
  · subst h
    have : fSdS (ρ / 3) α (-2 * ρ) = 0 := by rw [f_eq hα (by linarith) h2]; ring
    unfold Fint; rw [this]; simp [Real.zero_rpow (by norm_num : (-(1 / 2) : ℝ) ≠ 0)]
  · set t := -2 * ρ - r with ht
    have ht0 : 0 < t := by linarith
    have := simple_bd hρ h2 ht0 (by linarith [hr.1])
    rw [show -2 * ρ - t = r by ring] at this
    rwa [rpow_neg ht0.le, ← sqrt_eq_rpow, ← div_eq_mul_inv]

omit h2 in
lemma simple_dom_int :
    IntervalIntegrable (fun r => √((2 * ρ + 1) / 3) * (-2 * ρ - r) ^ (-(1 / 2) : ℝ)) volume (-2 * ρ - 1) (-2 * ρ) ∧
      ∫ r in -2 * ρ - 1..-2 * ρ, √((2 * ρ + 1) / 3) * (-2 * ρ - r) ^ (-(1 / 2) : ℝ) = 2 * √((2 * ρ + 1) / 3) := by
  have hi := (intervalIntegral.intervalIntegrable_rpow' (a := 1) (b := 0) (by norm_num : (-1 : ℝ) < -(1 / 2))).comp_sub_left (-2 * ρ)
  rw [sub_zero] at hi
  refine ⟨hi.const_mul _, ?_⟩
  rw [intervalIntegral.integral_const_mul, intervalIntegral.integral_comp_sub_left (fun x => x ^ (-(1 / 2) : ℝ)),
    show -2 * ρ - -2 * ρ = 0 by ring, show -2 * ρ - (-2 * ρ - 1) = 1 by ring,
    integral_rpow (Or.inl (by norm_num))]
  norm_num [zero_rpow]
  ring

/-- **At the simple root the same integral converges**: integrable on `[−2ρ − 1, −2ρ]`, value in
`[0, 2√((2ρ+1)/3)]`. -/
lemma simple_converges :
    IntervalIntegrable (Fint α ρ) volume (-2 * ρ - 1) (-2 * ρ) ∧
      0 ≤ ∫ r in -2 * ρ - 1..-2 * ρ, Fint α ρ r ∧
      ∫ r in -2 * ρ - 1..-2 * ρ, Fint α ρ r ≤ 2 * √((2 * ρ + 1) / 3) := by
  obtain ⟨hg, hgv⟩ := simple_dom_int hρ
  have hab : -2 * ρ - 1 ≤ -2 * ρ := by linarith
  have hnn : ∀ r, 0 ≤ Fint α ρ r := fun r => by unfold Fint; positivity
  have hm : Measurable (Fint α ρ) := by unfold Fint fSdS; fun_prop
  have hF : IntervalIntegrable (Fint α ρ) volume (-2 * ρ - 1) (-2 * ρ) := by
    refine hg.mono_fun hm.aestronglyMeasurable ?_
    refine (ae_restrict_mem measurableSet_uIoc).mono fun x hx => ?_
    rw [uIoc_of_le hab] at hx
    beta_reduce
    rw [Real.norm_eq_abs, Real.norm_eq_abs, abs_of_nonneg (hnn x)]
    exact (simple_dom hρ h2 ⟨hx.1.le, hx.2⟩).trans (le_abs_self _)
  refine ⟨hF, intervalIntegral.integral_nonneg hab fun r _ => hnn r, ?_⟩
  rw [← hgv]
  exact intervalIntegral.integral_mono_on hab hF hg fun x hx => simple_dom hρ h2 hx

end Div


/-! ### Row 100: the exact form, the flow, the approach rates, and the 2D `χ` block -/

section Flow

/-- The `χ`-block two-metric `−dT² + a(T)²dχ²`, `a = √Λ C e^{−√Λ T}`, as `e dT² + h dχ²`. -/
noncomputable def eT : ℝ → ℝ := fun _ => -1
noncomputable def hT (Λ C : ℝ) : ℝ → ℝ := fun T => (√Λ * C * Real.exp (-(√Λ * T))) ^ 2

lemma eT_ne (s : ℝ) : eT s ≠ 0 := by simp [eT]
lemma eT_smooth : ContDiff ℝ ∞ eT := contDiff_const
lemma hT_ne {Λ C : ℝ} (hΛ : 0 < Λ) (hC : C ≠ 0) (s : ℝ) : hT Λ C s ≠ 0 := by
  unfold hT; have := sqrt_pos.2 hΛ; have := Real.exp_pos (-(√Λ * s)); positivity
lemma hT_smooth (Λ C : ℝ) : ContDiff ℝ ∞ (hT Λ C) := by unfold hT; fun_prop

lemma hT_d (Λ C : ℝ) : deriv (hT Λ C) = fun T => -(2 * √Λ) * hT Λ C T := funext fun T => by
  have := (((Real.hasDerivAt_exp _).comp T ((hasDerivAt_id T).const_mul √Λ).neg).const_mul (√Λ * C)).pow 2
  unfold hT
  exact (show HasDerivAt (fun T => (√Λ * C * Real.exp (-(√Λ * T))) ^ 2) _ T from this).deriv.trans
    (by simp only [Function.comp_apply, Pi.neg_apply, id]; norm_num; ring)

lemma hT_dd (Λ C : ℝ) (hΛ : 0 ≤ Λ) : deriv (deriv (hT Λ C)) = fun T => 4 * Λ * hT Λ C T := funext fun T => by
  rw [hT_d]
  have h1 : HasDerivAt (hT Λ C) (-(2 * √Λ) * hT Λ C T) T := by
    rw [← congrFun (hT_d Λ C) T]; exact ((hT_smooth Λ C).differentiable (by simp) T).hasDerivAt
  rw [(h1.const_mul (-(2 * √Λ))).deriv]
  linear_combination (4 * hT Λ C T) * sq_sqrt hΛ

/-- **Row 100, Ⓒ③.** THE connection's Gaussian curvature `g(R(∂_T,∂_χ)∂_χ,∂_T)/(g_TT g_χχ)` of
`−dT² + (√Λ C e^{−√Λ T})² dχ²` is `Λ`, so its scalar curvature is `R₂ = 2K = 2Λ`: `dS₂` of radius `1/√Λ`. -/
theorem chi_block_gauss {Λ C : ℝ} (hΛ : 0 < Λ) (hC : C ≠ 0) (p : ℝ × ℝ) :
    diagF eT (hT Λ C) p (curv (lcConn (ℝ × ℝ) (ndOf (diagF eT (hT Λ C)) (diagF_symm _ _)
        (diagF_nondeg eT_ne (hT_ne hΛ hC)) ((diagF_smooth eT_smooth (hT_smooth Λ C)).differentiable (by simp))))
      (fun _ => ((1 : ℝ), (0 : ℝ))) (fun _ => ((0 : ℝ), (1 : ℝ))) (fun _ => ((0 : ℝ), (1 : ℝ))) p) ((1 : ℝ), (0 : ℝ))
      / (eT p.1 * hT Λ C p.1) = Λ := by
  rw [diag_curv eT_ne (hT_ne hΛ hC) eT_smooth (hT_smooth Λ C) p, hT_dd Λ C hΛ.le, hT_d]
  have hv := hT_ne hΛ hC p.1
  have key : (-(2 * √Λ) * hT Λ C p.1) ^ 2 = 4 * Λ * hT Λ C p.1 ^ 2 := by
    linear_combination (4 * hT Λ C p.1 ^ 2) * sq_sqrt hΛ.le
  have hde : deriv eT p.1 = 0 := by show deriv (fun _ : ℝ => (-1 : ℝ)) p.1 = 0; simp
  simp only [eT, hde, key]
  fsr

end Flow

/-- **Row 100, Ⓐ①–④: the exact diagonal form.** `(∂_χ r)² = 2M/r + r²/α² = 1 − f`; the `(τ̃,χ)` block
`[[−1,1],[1,F]]` has determinant `−(1+F)`, `1 + F = (∂_χ r)²` at `F = −f`; with `N² = (1+F)/F` and
`dχ̂ = dχ + dτ̃/F` the diagonal form re-derives `eq:proper-frame` exactly; and `dT = N dτ̃ = dr/√F`. -/
theorem row100_exact :
    (∀ M α r : ℝ, 2 * M / r + r ^ 2 / α ^ 2 = 1 - fSdS M α r) ∧
      (∀ F : ℝ, Matrix.det !![(-1 : ℝ), 1; 1, F] = -(1 + F)) ∧
      (∀ M α r : ℝ, 1 + -fSdS M α r = 2 * M / r + r ^ 2 / α ^ 2) ∧
      (∀ F : ℝ, F ≠ 0 → ∀ dτ dχ : ℝ,
        -((1 + F) / F) * dτ ^ 2 + F * (dχ + dτ / F) ^ 2 = -dτ ^ 2 + 2 * dτ * dχ + F * dχ ^ 2) ∧
      (∀ F : ℝ, 0 < F → √((1 + F) / F) / √(1 + F) = 1 / √F) := by
  refine ⟨fun M α r => by unfold fSdS; ring, fun F => by simp [Matrix.det_fin_two]; ring,
    fun M α r => by unfold fSdS; ring, fun F hF dτ dχ => by fsr, fun F hF => ?_⟩
  rw [sqrt_div (by linarith)]
  have := sqrt_pos.2 (show 0 < 1 + F by linarith); have := sqrt_pos.2 hF
  field_simp

/-- **Row 100, Ⓒ①②④: the flow.** `u = Ce^{−√Λ T}` solves `u̇ = −√Λ u`, `√(Λu²) = √Λ u`; the `χ` scale factor
`a = √Λ u` has `−ȧ/a = √Λ` exactly; and `C = 1/√Λ` gives `a² = e^{−2√Λ T}`. -/
theorem row100_flow {Λ : ℝ} (hΛ : 0 < Λ) :
    (∀ C T : ℝ, HasDerivAt (fun T => C * Real.exp (-(√Λ * T))) (-√Λ * (C * Real.exp (-(√Λ * T)))) T) ∧
      (∀ u : ℝ, 0 ≤ u → √(Λ * u ^ 2) = √Λ * u) ∧
      (∀ C T : ℝ, 0 < C → -deriv (fun T => √Λ * (C * Real.exp (-(√Λ * T)))) T
        / (√Λ * (C * Real.exp (-(√Λ * T)))) = √Λ) ∧
      (∀ T : ℝ, (√Λ * (1 / √Λ) * Real.exp (-(√Λ * T))) ^ 2 = Real.exp (-(2 * √Λ * T))) := by
  have hd : ∀ C T : ℝ, HasDerivAt (fun T => C * Real.exp (-(√Λ * T))) (-√Λ * (C * Real.exp (-(√Λ * T)))) T :=
    fun C T => by
      have := ((Real.hasDerivAt_exp _).comp T (((hasDerivAt_id' T).const_mul √Λ).neg)).const_mul C
      exact (show HasDerivAt (fun T => C * Real.exp (-(√Λ * T))) _ T from this).congr_deriv
        (by simp only [Pi.neg_apply]; ring)
  have hs := sqrt_pos.2 hΛ
  refine ⟨hd, fun u hu => by rw [sqrt_mul hΛ.le, sqrt_sq hu], fun C T hC => ?_, fun T => ?_⟩
  · rw [((hd C T).const_mul √Λ).deriv]
    have := Real.exp_pos (-(√Λ * T)); field_simp
  · rw [mul_one_div_cancel hs.ne', one_mul, sq, ← Real.exp_add]; congr 1; ring

/-- A limit along `u → 0⁺` read off a function continuous at `0` that agrees with it on `u > 0`. -/
lemma tend_of {φ g : ℝ → ℝ} {L : ℝ} (hg : ContinuousAt g 0) (hL : g 0 = L) (he : ∀ u > 0, φ u = g u) :
    Tendsto φ (𝓝[>] 0) (𝓝 L) := by
  rw [← hL]
  exact (hg.tendsto.mono_left nhdsWithin_le_nhds).congr' (eventually_nhdsWithin_of_forall fun u hu => (he u hu).symm)

section Rates

variable {α ρ : ℝ} (hρ : 0 < ρ) (h2 : α ^ 2 = 3 * ρ ^ 2)
include hρ h2

/-- **Row 100, Ⓑ③, Ⓓ②, Ⓕ②: the approach rates.** `−f/u² → Λ = 1/ρ²`; the angular deviation
`(r²/r_N² − 1)/u → 2/r_N`; the `χ`-block deviation `((−f)/Λu² − 1)/u → −2/(3r_N)`; and the squashing
`ε = a/r` over `u` tends to `√Λ/r_N`, so `ε ∝ u ∝ e^{−√Λ T}`. -/
theorem row100_rates :
    Tendsto (fun u => -fSdS (ρ / 3) α (ρ + u) / u ^ 2) (𝓝[>] 0) (𝓝 (1 / ρ ^ 2)) ∧
      Tendsto (fun u => ((ρ + u) ^ 2 / ρ ^ 2 - 1) / u) (𝓝[>] 0) (𝓝 (2 / ρ)) ∧
      Tendsto (fun u => (-fSdS (ρ / 3) α (ρ + u) / (1 / ρ ^ 2 * u ^ 2) - 1) / u) (𝓝[>] 0) (𝓝 (-2 / (3 * ρ))) ∧
      Tendsto (fun u => √(1 / ρ ^ 2) * u / (ρ + u) / u) (𝓝[>] 0) (𝓝 (√(1 / ρ ^ 2) / ρ)) := by
  refine ⟨tend_of (g := fun u => (3 * ρ + u) / (3 * ρ ^ 2 * (ρ + u))) (ContinuousAt.div (by fun_prop) (by fun_prop)
      (by simp; positivity)) (by fsr) fun u hu => ?_,
    tend_of (g := fun u => (2 * ρ + u) / ρ ^ 2) (by fun_prop) (by simp only [add_zero]; fsr) fun u hu => ?_,
    tend_of (g := fun u => -2 / (3 * (ρ + u))) (ContinuousAt.div (by fun_prop) (by fun_prop) (by simp; positivity))
      (by simp) fun u hu => ?_,
    tend_of (g := fun u => √(1 / ρ ^ 2) / (ρ + u)) (ContinuousAt.div (by fun_prop) (by fun_prop) (by simp; positivity))
      (by simp) fun u hu => ?_⟩
  · rw [negf_shift hρ h2 hu]; unfold q; field_simp
  · fsr
  · rw [negf_shift hρ h2 hu]; unfold q; fsr
  · field_simp

end Rates

/-- **Row 100, Ⓓ③ at `α = 1`, `u = 10⁻⁶`.** Both relative deviations match their rates `2u/r_N` and
`−2u/(3r_N)` to `10⁻¹¹`, in closed form: the residuals are `u²/r_N² = 3u²` and `2u²/(3r_N(r_N+u)) ≤ 2u²`. -/
theorem row100_deviation_instance :
    |((1 / √3 + 1e-6) / (1 / √3)) ^ 2 - 1 - 2 * 1e-6 / (1 / √3)| < 1e-11 ∧
      |-fSdS (1 / √3 / 3) 1 (1 / √3 + 1e-6) / (3 * (1e-6) ^ 2) - 1 + 2 * 1e-6 / (3 * (1 / √3))| < 1e-11 := by
  have hρ : (0 : ℝ) < 1 / √3 := by positivity
  have h2 : (1 : ℝ) ^ 2 = 3 * (1 / √3) ^ 2 := by rw [div_pow, s3]; norm_num
  have hr2 : (1 / √3 : ℝ) ^ 2 = 1 / 3 := by rw [div_pow, s3]; norm_num
  set ρ := (1 / √3 : ℝ)
  constructor
  · rw [show ((ρ + 1e-6) / ρ) ^ 2 - 1 - 2 * 1e-6 / ρ = (1e-6) ^ 2 / ρ ^ 2 by fsr, hr2]; norm_num
  · rw [negf_shift hρ h2 (by norm_num : (0 : ℝ) < 1e-6)]
    have e : (1e-6 : ℝ) ^ 2 / q ρ 1e-6 / (3 * (1e-6) ^ 2) - 1 + 2 * 1e-6 / (3 * ρ)
        = 2 * (1e-6) ^ 2 / (3 * ρ * (ρ + 1e-6)) := by
      unfold q; rw [show (3 : ℝ) * ρ ^ 2 = 1 by rw [hr2]; norm_num]; fsr
    rw [e, abs_of_pos (by positivity)]
    calc 2 * (1e-6 : ℝ) ^ 2 / (3 * ρ * (ρ + 1e-6)) ≤ 2 * (1e-6) ^ 2 / (3 * ρ ^ 2) :=
          div_le_div_of_nonneg_left (by positivity) (by positivity) (by nlinarith)
      _ < 1e-11 := by rw [hr2]; norm_num

/-- **Row 100, Ⓔ③ (the evaluation).** SdS's Kretschmann closed form `48M²/r⁶ + 8Λ²/3` at the Nariai mass
`M = ρ/3`, `Λ = 1/ρ²`, evaluated at `r = ρ`, is `8Λ²`, the limit metric's; and it tends to `8Λ²` as `r → ρ`
(the static chart itself degenerates at `ρ`, where `f = 0`). -/
theorem row100_kretschmann_at_rN {ρ : ℝ} (hρ : ρ ≠ 0) :
    48 * (ρ / 3) ^ 2 / ρ ^ 6 + 8 * (1 / ρ ^ 2) ^ 2 / 3 = 8 * (1 / ρ ^ 2) ^ 2 ∧
      Tendsto (fun r => 48 * (ρ / 3) ^ 2 / r ^ 6 + 8 * (1 / ρ ^ 2) ^ 2 / 3) (𝓝 ρ) (𝓝 (8 * (1 / ρ ^ 2) ^ 2)) := by
  have e : 48 * (ρ / 3) ^ 2 / ρ ^ 6 + 8 * (1 / ρ ^ 2) ^ 2 / 3 = 8 * (1 / ρ ^ 2) ^ 2 := by fsr
  refine ⟨e, ?_⟩
  have hc : ContinuousAt (fun r : ℝ => 48 * (ρ / 3) ^ 2 / r ^ 6 + 8 * (1 / ρ ^ 2) ^ 2 / 3) ρ :=
    ((continuousAt_const.div (continuousAt_id.pow 6) (pow_ne_zero 6 hρ)).add continuousAt_const)
  have := hc.tendsto; rwa [e] at this

/-- **Row 100, the analytic core** (Ⓑ, Ⓓ①, Ⓒ③'s radius), at `α > 0`, `r_N = α/√3`, `Λ = 3/α²`:
the double root and `α² r f = −(r − r_N)²(r + 2r_N)`, `f″(r_N) = −2Λ`, the simple root `−2r_N`;
`r_N = 1/√Λ`, `r_N² = 1/Λ`, `2/r_N² = 2Λ`, `√(−2/f″(r_N)) = 1/√Λ`; the normal time `∫dr/√(−f)` is NOT
integrable across `r_N` and its truncation exceeds `r_N log(1/ε) → ∞`; its decade increments lie in
`(r_N ln10, (r_N + h/3) ln10]`, decrease strictly, and tend to `r_N ln10 = ln10/√Λ`; and at the simple root it
converges, to at most `2√((2r_N+1)/3)`. -/
theorem row100_checks {α : ℝ} (hα : 0 < α) :
    fSdS (α / (3 * √3)) α (α / √3) = 0 ∧ deriv (fSdS (α / (3 * √3)) α) (α / √3) = 0 ∧
      deriv (deriv (fSdS (α / (3 * √3)) α)) (α / √3) = -2 * (3 / α ^ 2) ∧
      (∀ r ≠ 0, α ^ 2 * r * fSdS (α / (3 * √3)) α r = -((r - α / √3) ^ 2 * (r + 2 * (α / √3)))) ∧
      fSdS (α / (3 * √3)) α (-2 * (α / √3)) = 0 ∧
      α / √3 = 1 / √(3 / α ^ 2) ∧ (α / √3) ^ 2 = 1 / (3 / α ^ 2) ∧ 2 / (α / √3) ^ 2 = 2 * (3 / α ^ 2) ∧
      √(-2 / deriv (deriv (fSdS (α / (3 * √3)) α)) (α / √3)) = 1 / √(3 / α ^ 2) ∧
      ¬ IntervalIntegrable (Fint α (α / √3)) MeasureTheory.volume (α / √3) (α / √3 + 1) ∧
      (∀ ε, 0 < ε → ε < 1 → α / √3 * log (1 / ε) < ∫ r in α / √3 + ε..α / √3 + 1, Fint α (α / √3) r) ∧
      Tendsto (fun ε => ∫ r in α / √3 + ε..α / √3 + 1, Fint α (α / √3) r) (𝓝[>] 0) atTop ∧
      (∀ h > 0, α / √3 * log 10 < incr α (α / √3) h ∧ incr α (α / √3) h ≤ (α / √3 + h / 3) * log 10) ∧
      (∀ h > 0, incr α (α / √3) (h / 10) < incr α (α / √3) h) ∧
      Tendsto (fun d : ℕ => incr α (α / √3) ((1 / 10) ^ d)) atTop (𝓝 (log 10 / √(3 / α ^ 2))) ∧
      IntervalIntegrable (Fint α (α / √3)) MeasureTheory.volume (-2 * (α / √3) - 1) (-2 * (α / √3)) ∧
      0 ≤ ∫ r in -2 * (α / √3) - 1..-2 * (α / √3), Fint α (α / √3) r ∧
      ∫ r in -2 * (α / √3) - 1..-2 * (α / √3), Fint α (α / √3) r ≤ 2 * √((2 * (α / √3) + 1) / 3) := by
  obtain ⟨h2, hM⟩ := nar α
  have hρ : 0 < α / √3 := by positivity
  obtain ⟨v0, v1, v2⟩ := nariai_vals hα
  have hL : 1 / √(3 / α ^ 2) = α / √3 := by
    rw [sqrt_div (by norm_num), sqrt_sq hα.le]; field_simp
  obtain ⟨c1, c2, c3⟩ := simple_converges hρ h2
  refine ⟨v0, v1, by rw [v2]; ring, fun r hr => by rw [hM]; exact factor hα.ne' hr h2, ?_, hL.symm,
    by rw [rho_sq]; field_simp, by rw [rho_sq]; fsr, ?_, not_integrable hρ h2 (by linarith)
      (by rw [uIcc_of_le (by linarith)]; exact ⟨le_rfl, by linarith⟩),
    (log_divergence hρ h2).1, (log_divergence hρ h2).2, fun h hh => incr_bounds hρ h2 hh,
    fun h hh => incr_anti hρ h2 hh, ?_, c1, c2, c3⟩
  · rw [hM, f_eq hα.ne' (by positivity) h2]; ring
  · rw [v2, hL, show -2 / (-6 / α ^ 2) = (α / √3) ^ 2 by rw [rho_sq]; fsr, sqrt_sq hρ.le]
  · rw [show log 10 / √(3 / α ^ 2) = α / √3 * log 10 by rw [div_eq_mul_one_div, hL]; ring]
    exact incr_tendsto hρ h2

/-- **Row 100, Ⓑ⑥ at `α = 1`**: the simple-root integral is finite and below `10`. -/
theorem row100_simple_instance :
    IntervalIntegrable (Fint 1 (1 / √3)) MeasureTheory.volume (-2 * (1 / √3) - 1) (-2 * (1 / √3)) ∧
      |∫ r in -2 * (1 / √3) - 1..-2 * (1 / √3), Fint 1 (1 / √3) r| < 10 := by
  have hρ : (0 : ℝ) < 1 / √3 := by positivity
  have h2 : (1 : ℝ) ^ 2 = 3 * (1 / √3) ^ 2 := by rw [div_pow, s3]; norm_num
  obtain ⟨c1, c2, c3⟩ := simple_converges hρ h2
  have hle : 1 / √3 ≤ 1 := by rw [div_le_one s3pos]; exact (lt_sqrt (by norm_num)).2 (by norm_num) |>.le
  have : √((2 * (1 / √3) + 1) / 3) ≤ 1 := sqrt_le_one.mpr (by linarith)
  refine ⟨c1, ?_⟩
  rw [abs_of_nonneg c2]; linarith




/-! ## Row 101 — `P15_the_seam_sec_envelope_means…`: the bead's legs `r(s)` and the turning-point quartic -/

/-- `√3` to ten digits. -/
lemma s3_bounds : 1.7320508075 < √3 ∧ √3 < 1.7320508076 :=
  ⟨(lt_sqrt (by norm_num)).2 (by norm_num), (sqrt_lt' (by norm_num)).2 (by norm_num)⟩

/-- Cube-root bookkeeping: with `u = x^{1/3}`, `x^{n/3} = uⁿ` and `x^{-n/3} = u⁻ⁿ`. -/
lemma cbp {x : ℝ} (hx : 0 < x) (n : ℕ) : (x ^ (1 / 3 : ℝ)) ^ n = x ^ ((n : ℝ) / 3) := by
  rw [← rpow_natCast, ← rpow_mul hx.le]; ring_nf

lemma cbn {x : ℝ} (hx : 0 < x) (n : ℕ) : x ^ (-((n : ℝ) / 3)) = ((x ^ (1 / 3 : ℝ)) ^ n)⁻¹ := by
  rw [rpow_neg hx.le, cbp hx]

lemma cb3 {x : ℝ} (hx : 0 < x) : (x ^ (1 / 3 : ℝ)) ^ 3 = x := by
  rw [cbp hx]; norm_num

/-- `k = 3/(2α)`, the amplitude `A = 2^{1/3}α/√3`, and the two legs `−A cosh^{2/3}(ks)`, `A sinh^{2/3}(ks)`. -/
noncomputable def kk (α : ℝ) : ℝ := 3 / (2 * α)
noncomputable def AA (α : ℝ) : ℝ := (2 : ℝ) ^ (1 / 3 : ℝ) * α / √3
noncomputable def rColl (α s : ℝ) : ℝ := -AA α * cosh (kk α * s) ^ (2 / 3 : ℝ)
noncomputable def rExp (α s : ℝ) : ℝ := AA α * sinh (kk α * s) ^ (2 / 3 : ℝ)

/-- The collapse leg's first two derivatives. -/
noncomputable def d1C (α s : ℝ) : ℝ := -AA α * (2 / 3) * kk α * sinh (kk α * s) * cosh (kk α * s) ^ (-(1 / 3) : ℝ)
noncomputable def d2C (α s : ℝ) : ℝ := -AA α * (2 / 3) * kk α ^ 2 *
  (cosh (kk α * s) * cosh (kk α * s) ^ (-(1 / 3) : ℝ) - 1 / 3 * sinh (kk α * s) ^ 2 * cosh (kk α * s) ^ (-(4 / 3) : ℝ))
/-- The expansion leg's first three derivatives (on `s > 0`). -/
noncomputable def d1E (α s : ℝ) : ℝ := AA α * (2 / 3) * kk α * cosh (kk α * s) * sinh (kk α * s) ^ (-(1 / 3) : ℝ)
noncomputable def d2E (α s : ℝ) : ℝ := AA α * (2 / 3) * kk α ^ 2 *
  (sinh (kk α * s) * sinh (kk α * s) ^ (-(1 / 3) : ℝ) - 1 / 3 * cosh (kk α * s) ^ 2 * sinh (kk α * s) ^ (-(4 / 3) : ℝ))
noncomputable def d3E (α s : ℝ) : ℝ := AA α * (2 / 3) * kk α ^ 3 * (4 / 9) * cosh (kk α * s) ^ 3 *
  sinh (kk α * s) ^ (-(7 / 3) : ℝ)

/-- `HasDerivAt` of `g(ks)^p` for a positive `g`. -/
lemma hd_pow {g g' : ℝ → ℝ} {s k p : ℝ} (hg : HasDerivAt g (g' (k * s)) (k * s)) (hpos : 0 < g (k * s)) :
    HasDerivAt (fun s => g (k * s) ^ p) (k * g' (k * s) * p * g (k * s) ^ (p - 1)) s := by
  have := (hg.comp s ((hasDerivAt_id' s).const_mul k)).rpow_const (p := p) (Or.inl hpos.ne')
  exact (show HasDerivAt (fun s => g (k * s) ^ p) _ s from this).congr_deriv
    (by simp only [Function.comp_apply]; ring)

lemma hd_lin {f f' : ℝ → ℝ} (k s : ℝ) (hf : HasDerivAt f (f' (k * s)) (k * s)) :
    HasDerivAt (fun s => f (k * s)) (k * f' (k * s)) s :=
  (show HasDerivAt (fun s => f (k * s)) _ s from hf.comp s ((hasDerivAt_id' s).const_mul k)).congr_deriv
    (by ring)

lemma coll_d1 (α s : ℝ) : HasDerivAt (rColl α) (d1C α s) s := by
  have h : HasDerivAt (rColl α) _ s :=
    (hd_pow (p := 2 / 3) (Real.hasDerivAt_cosh (kk α * s)) (cosh_pos _) (s := s)).const_mul (-AA α)
  exact h.congr_deriv (by unfold d1C; rw [show (2 / 3 : ℝ) - 1 = -(1 / 3) by norm_num]; ring)

lemma coll_d2 (α s : ℝ) : HasDerivAt (d1C α) (d2C α s) s := by
  have e : d1C α = fun y => (-AA α * (2 / 3) * kk α) * (sinh (kk α * y) * cosh (kk α * y) ^ (-(1 / 3) : ℝ)) := by
    funext y; unfold d1C; ring
  rw [e]
  exact (((hd_lin (kk α) s (Real.hasDerivAt_sinh _)).mul
    (hd_pow (p := -(1 / 3)) (Real.hasDerivAt_cosh (kk α * s)) (cosh_pos _) (s := s))).const_mul _).congr_deriv
    (by unfold d2C; rw [show (-(1 / 3) : ℝ) - 1 = -(4 / 3) by norm_num]; ring)

lemma exp_d1 (α : ℝ) {s : ℝ} (hs : 0 < sinh (kk α * s)) : HasDerivAt (rExp α) (d1E α s) s := by
  have h : HasDerivAt (rExp α) _ s :=
    (hd_pow (p := 2 / 3) (Real.hasDerivAt_sinh (kk α * s)) hs (s := s)).const_mul (AA α)
  exact h.congr_deriv (by unfold d1E; rw [show (2 / 3 : ℝ) - 1 = -(1 / 3) by norm_num]; ring)

lemma exp_d2 (α : ℝ) {s : ℝ} (hs : 0 < sinh (kk α * s)) : HasDerivAt (d1E α) (d2E α s) s := by
  have e : d1E α = fun y => (AA α * (2 / 3) * kk α) * (cosh (kk α * y) * sinh (kk α * y) ^ (-(1 / 3) : ℝ)) := by
    funext y; unfold d1E; ring
  rw [e]
  exact (((hd_lin (kk α) s (Real.hasDerivAt_cosh _)).mul
    (hd_pow (p := -(1 / 3)) (Real.hasDerivAt_sinh (kk α * s)) hs (s := s))).const_mul _).congr_deriv
    (by unfold d2E; rw [show (-(1 / 3) : ℝ) - 1 = -(4 / 3) by norm_num]; ring)

lemma exp_d3 (α : ℝ) {s : ℝ} (hs : 0 < sinh (kk α * s)) : HasDerivAt (d2E α) (d3E α s) s := by
  have e : d2E α = fun y => (AA α * (2 / 3) * kk α ^ 2) * (sinh (kk α * y) * sinh (kk α * y) ^ (-(1 / 3) : ℝ)
      - (1 / 3 * cosh (kk α * y) ^ 2) * sinh (kk α * y) ^ (-(4 / 3) : ℝ)) := by
    funext y; unfold d2E; ring
  rw [e]
  have hc2 : HasDerivAt (fun y => 1 / 3 * cosh (kk α * y) ^ 2) (1 / 3 * (2 * cosh (kk α * s) * (kk α * sinh (kk α * s)))) s :=
    (show HasDerivAt (fun y => 1 / 3 * cosh (kk α * y) ^ 2) _ s from
      ((hd_lin (kk α) s (Real.hasDerivAt_cosh _)).pow 2).const_mul (1 / 3)).congr_deriv (by push_cast; ring)
  refine ((((hd_lin (kk α) s (Real.hasDerivAt_sinh _)).mul
    (hd_pow (p := -(1 / 3)) (Real.hasDerivAt_sinh (kk α * s)) hs (s := s))).sub
    (hc2.mul (hd_pow (p := -(4 / 3)) (Real.hasDerivAt_sinh (kk α * s)) hs (s := s)))).const_mul _).congr_deriv ?_
  unfold d3E
  have hS := cb3 hs
  rw [show (-(1 / 3 : ℝ) - 1) = -(((4 : ℕ) : ℝ) / 3) by norm_num, show (-(1 / 3 : ℝ)) = -(((1 : ℕ) : ℝ) / 3) by norm_num,
    show (-(4 / 3 : ℝ) - 1) = -(((7 : ℕ) : ℝ) / 3) by norm_num, show (-(4 / 3 : ℝ)) = -(((4 : ℕ) : ℝ) / 3) by norm_num,
    show (-(7 / 3 : ℝ)) = -(((7 : ℕ) : ℝ) / 3) by norm_num, cbn hs, cbn hs, cbn hs]
  have hu : 0 < sinh (kk α * s) ^ (1 / 3 : ℝ) := rpow_pos_of_pos hs _
  set u := sinh (kk α * s) ^ (1 / 3 : ℝ)
  rw [← hS]; field_simp; ring

/-- `log(1 − x)` from the series, six terms, for `0 ≤ x < 1`. -/
lemma log_series {x : ℝ} (hx0 : 0 ≤ x) (hx1 : x < 1) :
    -(∑ i ∈ Finset.range 6, x ^ (i + 1) / (i + 1)) - x ^ 7 / (1 - x) ≤ log (1 - x) ∧
      log (1 - x) ≤ -(∑ i ∈ Finset.range 6, x ^ (i + 1) / (i + 1)) + x ^ 7 / (1 - x) := by
  have h := abs_log_sub_add_sum_range_le (show |x| < 1 by rw [abs_of_nonneg hx0]; exact hx1) 6
  rw [abs_of_nonneg hx0, abs_le] at h
  constructor <;> linarith [h.1, h.2]

/-- `log(2 + √3) = arcosh 2` to seven digits. -/
lemma log_2s3 : 1.3169578 < log (2 + √3) ∧ log (2 + √3) < 1.31695791 := by
  obtain ⟨a, b⟩ := s3_bounds
  have l2a := log_two_gt_d9; have l2b := log_two_lt_d9
  have hq : ∀ q : ℝ, 0 < q → log q = 2 * log 2 + log (1 - (1 - q / 4)) := fun q hq => by
    rw [show (1 : ℝ) - (1 - q / 4) = q / 4 by ring, log_div hq.ne' (by norm_num),
      show (4 : ℝ) = 2 ^ 2 by norm_num, log_pow]; push_cast; ring
  have lo := log_series (x := 1 - 3.7320508075 / 4) (by norm_num) (by norm_num)
  have hi := log_series (x := 1 - 3.7320508076 / 4) (by norm_num) (by norm_num)
  norm_num [Finset.sum_range_succ] at lo hi
  constructor
  · calc (1.3169578 : ℝ) < log 3.7320508075 := by rw [hq _ (by norm_num)]; norm_num; linarith [lo.1]
      _ < log (2 + √3) := log_lt_log (by norm_num) (by linarith)
  · calc log (2 + √3) < log 3.7320508076 := log_lt_log (by positivity) (by linarith)
      _ < 1.31695791 := by rw [hq _ (by norm_num)]; norm_num; linarith [hi.2]

/-- `log 10` to four digits. -/
lemma log_10 : 2.30256 < log 10 ∧ log 10 < 2.30260 := by
  have l2a := log_two_gt_d9; have l2b := log_two_lt_d9
  have e : log 10 = 3 * log 2 - log (1 - 1 / 5) := by
    rw [show (1 : ℝ) - 1 / 5 = 2 ^ 3 / 10 by norm_num, log_div (by norm_num) (by norm_num), log_pow]; push_cast; ring
  have h := log_series (x := 1 / 5) (by norm_num) (by norm_num)
  norm_num [Finset.sum_range_succ] at h
  rw [e]; constructor <;> linarith [h.1, h.2]

variable {α : ℝ} (hα : 0 < α)
include hα

lemma kk_pos : 0 < kk α := by unfold kk; positivity
lemma t3 : ((2 : ℝ) ^ (1 / 3 : ℝ)) ^ 3 = 2 := cb3 (by norm_num)

/-- **Row 101, Ⓒ①: the back seam.** At `cosh(ks) = 2`, i.e. `s_b = log(2+√3)/k`: `r = −2α/√3`, `dr/ds = −1`,
`d²r/ds² = −9/(4√3α) = −3√3/(4α)`. -/
lemma back_seam :
    cosh (kk α * (log (2 + √3) / kk α)) = 2 ∧ sinh (kk α * (log (2 + √3) / kk α)) = √3 ∧
      rColl α (log (2 + √3) / kk α) = -2 * α / √3 ∧ d1C α (log (2 + √3) / kk α) = -1 ∧
      d2C α (log (2 + √3) / kk α) = -(3 * √3) / (4 * α) := by
  have hk := (kk_pos hα).ne'
  have hy : (0 : ℝ) < 2 + √3 := by positivity
  have hinv : (2 + √3)⁻¹ = 2 - √3 := by
    exact inv_eq_of_mul_eq_one_right (by linear_combination (-1 : ℝ) * s3)
  have e : kk α * (log (2 + √3) / kk α) = log (2 + √3) := by field_simp
  have hc : cosh (kk α * (log (2 + √3) / kk α)) = 2 := by rw [e, cosh_log hy, hinv]; ring
  have hs : sinh (kk α * (log (2 + √3) / kk α)) = √3 := by rw [e, sinh_log hy, hinv]; ring
  have tpos : (0 : ℝ) < 2 ^ (1 / 3 : ℝ) := by positivity
  have ht := t3 hα
  have := s3pos
  refine ⟨hc, hs, ?_, ?_, ?_⟩
  · unfold rColl; rw [hc]; unfold AA
    rw [show -((2 : ℝ) ^ (1 / 3 : ℝ) * α / √3) * (2 : ℝ) ^ (2 / 3 : ℝ)
      = -((2 : ℝ) ^ (1 / 3 : ℝ) * 2 ^ (2 / 3 : ℝ)) * α / √3 by ring, ← rpow_add (by norm_num)]
    norm_num; try ring
  · unfold d1C; rw [hc, hs]; unfold AA kk
    rw [show (-(1 / 3) : ℝ) = -(((1 : ℕ) : ℝ) / 3) by norm_num, cbn (by norm_num : (0 : ℝ) < 2)]
    simp only [Nat.cast_one, pow_one]
    fsr
  · unfold d2C; rw [hc, hs]; unfold AA kk
    rw [show (-(1 / 3) : ℝ) = -(((1 : ℕ) : ℝ) / 3) by norm_num,
      show (-(4 / 3) : ℝ) = -(((4 : ℕ) : ℝ) / 3) by norm_num, cbn (by norm_num : (0 : ℝ) < 2),
      cbn (by norm_num : (0 : ℝ) < 2)]
    have h4 : ((2 : ℝ) ^ (1 / 3 : ℝ)) ^ 4 = 2 * 2 ^ (1 / 3 : ℝ) := by rw [pow_succ, ht]
    simp only [Nat.cast_one, pow_one, Nat.cast_ofNat]
    rw [h4, s3]
    have : (-(3 * √3) / (4 * α) : ℝ) = -9 / (4 * √3 * α) := by
      rw [div_eq_div_iff (by positivity) (by positivity)]; linear_combination (-12 * α) * s3
    rw [this]; fsr

/-- **Row 101, Ⓒ②: the turnaround** `s = 0`: `r = −A`, `dr/ds = 0`, `d²r/ds² = −3A/(2α²)`, with `A = (2Mα²)^{1/3}`
at `M = α/(3√3)`; and the limits `s → 0` of both derivatives are those values. -/
lemma turnaround :
    rColl α 0 = -AA α ∧ d1C α 0 = 0 ∧ d2C α 0 = -(3 * AA α) / (2 * α ^ 2) ∧
      AA α = (2 * (α / (3 * √3)) * α ^ 2) ^ (1 / 3 : ℝ) ∧
      Tendsto (d1C α) (𝓝 0) (𝓝 0) ∧ Tendsto (d2C α) (𝓝 0) (𝓝 (-(3 * AA α) / (2 * α ^ 2))) := by
  have h0 : d1C α 0 = 0 := by simp [d1C]
  have h2 : d2C α 0 = -(3 * AA α) / (2 * α ^ 2) := by simp [d2C, kk]; fsr
  refine ⟨by simp [rColl], h0, h2, ?_, ?_, ?_⟩
  · have : 2 * (α / (3 * √3)) * α ^ 2 = 2 * (α / √3) ^ 3 := by
      have h3 : √3 ^ 3 = 3 * √3 := by rw [pow_succ, s3]
      rw [div_pow, h3]; ring
    rw [this, mul_rpow (by norm_num) (by positivity), show (1 / 3 : ℝ) = ((3 : ℕ) : ℝ)⁻¹ by norm_num,
      pow_rpow_inv_natCast (by positivity) (by norm_num), AA]; ring
  · simpa [h0] using (coll_d2 α 0).continuousAt.tendsto
  · rw [← h2]
    have hc : Continuous fun s => cosh (kk α * s) := by fun_prop
    have h1 := hc.rpow_const (p := -(1 / 3)) fun x => Or.inl (cosh_pos _).ne'
    have h4 := hc.rpow_const (p := -(4 / 3)) fun x => Or.inl (cosh_pos _).ne'
    have : Continuous (d2C α) := by unfold d2C; fun_prop
    exact this.tendsto 0

/-- **Row 101, Ⓒ③: the front seam.** At `sinh(ks) = 1/√2` (`tanh² = 1/3`): `r = α/√3`, `dr/ds = 1`,
`d²r/ds² = 0`, `d³r/ds³ > 0` — a minimum of the speed, of exactly `1`. -/
lemma front_seam :
    sinh (kk α * (arsinh (1 / √2) / kk α)) = 1 / √2 ∧ rExp α (arsinh (1 / √2) / kk α) = α / √3 ∧
      d1E α (arsinh (1 / √2) / kk α) = 1 ∧ d2E α (arsinh (1 / √2) / kk α) = 0 ∧
      0 < d3E α (arsinh (1 / √2) / kk α) := by
  have hk := (kk_pos hα).ne'
  have e : kk α * (arsinh (1 / √2) / kk α) = arsinh (1 / √2) := by field_simp
  have hs : sinh (kk α * (arsinh (1 / √2) / kk α)) = 1 / √2 := by rw [e, sinh_arsinh]
  have s2 : √2 ^ 2 = 2 := sq_sqrt (by norm_num)
  have hc : cosh (kk α * (arsinh (1 / √2) / kk α)) = √3 / √2 := by
    rw [e, cosh_arsinh, div_pow, s2, show (1 : ℝ) + 1 ^ 2 / 2 = 3 / 2 by norm_num, sqrt_div (by norm_num)]
  have hS0 : (0 : ℝ) < 1 / √2 := by positivity
  set v := (1 / √2 : ℝ) ^ (1 / 3 : ℝ) with hv
  have hv0 : 0 < v := rpow_pos_of_pos hS0 _
  have hv3 : v ^ 3 = 1 / √2 := cb3 hS0
  set t := (2 : ℝ) ^ (1 / 3 : ℝ) with htd
  have ht0 : 0 < t := by positivity
  have ht3 : t ^ 3 = 2 := t3 hα
  have htv : t * v ^ 2 = 1 := by
    have h6 : (t * v ^ 2) ^ 3 = 1 := by
      rw [mul_pow, ht3, ← pow_mul, show 2 * 3 = 3 * 2 by rfl, pow_mul, hv3, div_pow, s2]; norm_num
    exact (pow_left_inj₀ (by positivity) zero_le_one (by norm_num : (3 : ℕ) ≠ 0)).1 (h6.trans (one_pow 3).symm)
  have s2p : (0 : ℝ) < √2 := by positivity
  refine ⟨hs, ?_, ?_, ?_, ?_⟩
  · unfold rExp AA
    rw [hs, show (2 / 3 : ℝ) = ((2 : ℕ) : ℝ) / 3 by norm_num, ← cbp hS0, ← hv, ← htd]
    rw [show t * α / √3 * v ^ 2 = (t * v ^ 2) * α / √3 by ring, htv, one_mul]
  · unfold d1E; rw [hs, hc]; unfold AA kk
    rw [show (-(1 / 3) : ℝ) = -(((1 : ℕ) : ℝ) / 3) by norm_num, cbn hS0, ← hv, ← htd]
    simp only [Nat.cast_one, pow_one]
    have h' : √2 * v ^ 3 = 1 := by rw [hv3]; field_simp
    have key : t = √2 * v := by linear_combination (-t) * h' + (√2 * v) * htv
    rw [key]; fsr
  · unfold d2E; rw [hs, hc]
    rw [show (-(1 / 3) : ℝ) = -(((1 : ℕ) : ℝ) / 3) by norm_num,
      show (-(4 / 3) : ℝ) = -(((4 : ℕ) : ℝ) / 3) by norm_num, cbn hS0, cbn hS0, ← hv]
    simp only [Nat.cast_one, pow_one, Nat.cast_ofNat]
    have h32 : (√3 / √2) ^ 2 = 3 * (v ^ 3) ^ 2 := by
      rw [hv3, div_pow, div_pow, s2, sq_sqrt (by norm_num : (0 : ℝ) ≤ 3)]; norm_num
    rw [h32, ← hv3, mul_eq_zero]; right; fsr
  · unfold d3E
    have hA : 0 < AA α := by unfold AA; positivity
    have := kk_pos hα
    rw [hc, hs]; positivity

/-- On the legs `r` is monotone: `dr/ds > 0` on the collapse leg `s < 0` and on the expansion leg `s > 0`. -/
lemma legs_monotone : (∀ s < 0, 0 < d1C α s) ∧ (∀ s > 0, 0 < d1E α s) := by
  have hA : 0 < AA α := by unfold AA; positivity
  have hk := kk_pos hα
  refine ⟨fun s hs => ?_, fun s hs => ?_⟩
  · have h1 : sinh (kk α * s) < 0 := sinh_neg_iff.2 (by nlinarith)
    have := rpow_pos_of_pos (cosh_pos (kk α * s)) (-(1 / 3))
    rw [show d1C α s = (AA α * (2 / 3) * kk α * cosh (kk α * s) ^ (-(1 / 3) : ℝ)) * -sinh (kk α * s) by
      unfold d1C; ring]
    exact mul_pos (by positivity) (neg_pos.2 h1)
  · have : 0 < sinh (kk α * s) := sinh_pos_iff.2 (by positivity)
    unfold d1E; have := rpow_pos_of_pos this (-(1 / 3)); have := cosh_pos (kk α * s); positivity

omit hα

/-- The quartic `x⁴ − x − 4` has exactly one positive root, and it lies in `(1.5333, 1.5343)`. -/
lemma quartic_root : (∃! x : ℝ, 0 < x ∧ x ^ 4 - x - 4 = 0) ∧
    ∀ x : ℝ, 0 < x → x ^ 4 - x - 4 = 0 → 1.5333 < x ∧ x < 1.5343 := by
  have big : ∀ x : ℝ, 0 < x → x ^ 4 - x - 4 = 0 → 1 < x := fun x hx h => by
    by_contra hc; push_neg at hc
    nlinarith [pow_le_one₀ hx.le hc (n := 4)]
  have mono : ∀ x y : ℝ, 1 ≤ x → x < y → x ^ 4 - x - 4 < y ^ 4 - y - 4 := fun x y hx hxy => by
    nlinarith [mul_pos (by linarith : (0 : ℝ) < y - x) (by nlinarith : (0 : ℝ) < y ^ 3 + y ^ 2 * x + y * x ^ 2 + x ^ 3 - 1)]
  have brk : ∀ x : ℝ, 0 < x → x ^ 4 - x - 4 = 0 → 1.5333 < x ∧ x < 1.5343 := fun x hx h => by
    have h1 := big x hx h
    constructor
    · by_contra hc; push_neg at hc
      rcases eq_or_lt_of_le hc with e | e
      · rw [e] at h; norm_num at h
      · have := mono x 1.5333 h1.le e; norm_num at this; linarith
    · by_contra hc; push_neg at hc
      rcases eq_or_lt_of_le hc with e | e
      · rw [← e] at h; norm_num at h
      · have := mono 1.5343 x (by norm_num) e; norm_num at this; linarith
  refine ⟨?_, brk⟩
  obtain ⟨x, hx, hx0⟩ : ∃ x ∈ Icc (1.5333 : ℝ) 1.5343, x ^ 4 - x - 4 = 0 :=
    intermediate_value_Icc (by norm_num) (by fun_prop) ⟨by norm_num, by norm_num⟩
  refine ⟨x, ⟨by linarith [hx.1], hx0⟩, fun y ⟨hy, hy0⟩ => ?_⟩
  rcases lt_trichotomy y x with e | e | e
  · have := mono y x (big y hy hy0).le e; linarith
  · exact e
  · have := mono x y (by linarith [hx.1]) e; linarith

/-- The Euclidean-null cubic `r³ + r + 2M`, `2M = 2/(3√3)` (`f = 2` at `α = 1`, times `−r`), has exactly one
real root, and it lies within `10⁻⁷` of `−0.34414212`. -/
lemma null_root : (∃! r : ℝ, r ^ 3 + r + 2 * (1 / (3 * √3)) = 0) ∧
    ∀ r : ℝ, r ^ 3 + r + 2 * (1 / (3 * √3)) = 0 → |r + 0.34414212| < 1e-7 := by
  obtain ⟨a, b⟩ := s3_bounds
  have e : 2 * (1 / (3 * √3)) = 2 * √3 / 9 := by
    field_simp; rw [s3]; ring
  rw [e]
  have mono : ∀ x y : ℝ, x < y → x ^ 3 + x + 2 * √3 / 9 < y ^ 3 + y + 2 * √3 / 9 := fun x y h => by
    nlinarith [mul_pos (by linarith : (0 : ℝ) < y - x) (by nlinarith [sq_nonneg (x + y)] :
      (0 : ℝ) < x ^ 2 + x * y + y ^ 2 + 1)]
  have lo : (-0.34414222 : ℝ) ^ 3 + -0.34414222 + 2 * √3 / 9 < 0 := by nlinarith
  have hi : 0 < (-0.34414202 : ℝ) ^ 3 + -0.34414202 + 2 * √3 / 9 := by nlinarith
  have brk : ∀ r : ℝ, r ^ 3 + r + 2 * √3 / 9 = 0 → |r + 0.34414212| < 1e-7 := fun r h => by
    rw [abs_lt]; constructor
    · by_contra hc; push_neg at hc
      rcases (show r ≤ -0.34414222 by linarith).lt_or_eq with h' | h'
      · have := mono r (-0.34414222) h'; linarith
      · rw [h'] at h; linarith
    · by_contra hc; push_neg at hc
      rcases (show -0.34414202 ≤ r by linarith).lt_or_eq with h' | h'
      · have := mono (-0.34414202) r h'; linarith
      · rw [← h'] at h; linarith
  refine ⟨?_, brk⟩
  obtain ⟨x, -, hx0⟩ : ∃ x ∈ Icc (-0.34414222 : ℝ) (-0.34414202), x ^ 3 + x + 2 * √3 / 9 = 0 :=
    intermediate_value_Icc (by norm_num) (by fun_prop) ⟨lo.le, hi.le⟩
  refine ⟨x, hx0, fun y hy => ?_⟩
  rcases lt_trichotomy y x with e | e | e
  · have := mono y x e; linarith
  · exact e
  · have := mono x y e; linarith

/-- **Row 100, Ⓑ④ at the receipt's `α = 1`.** The four decade increments decrease strictly, stay above
`ln10/√3`, and the fourth is within `10⁻⁴` of it; `r7155`'s `2.659` is twice the limit to `5·10⁻⁴` (Ⓑ⑤). -/
theorem row100_decades :
    incr 1 (1 / √3) (1 / 100) < incr 1 (1 / √3) (1 / 10) ∧ incr 1 (1 / √3) (1 / 1000) < incr 1 (1 / √3) (1 / 100) ∧
      incr 1 (1 / √3) (1 / 10000) < incr 1 (1 / √3) (1 / 1000) ∧ log 10 / √3 < incr 1 (1 / √3) (1 / 10000) ∧
      |incr 1 (1 / √3) (1 / 10000) - log 10 / √3| < 1e-4 ∧ |(2.659 : ℝ) - 2 * (log 10 / √3)| < 5e-4 := by
  have hρ : (0 : ℝ) < 1 / √3 := by positivity
  have h2 : (1 : ℝ) ^ 2 = 3 * (1 / √3) ^ 2 := by rw [div_pow, s3]; norm_num
  have e : (1 / √3) * log 10 = log 10 / √3 := by ring
  have a1 := incr_anti hρ h2 (h := 1 / 10) (by norm_num)
  have a2 := incr_anti hρ h2 (h := 1 / 100) (by norm_num)
  have a3 := incr_anti hρ h2 (h := 1 / 1000) (by norm_num)
  rw [show (1 : ℝ) / 10 / 10 = 1 / 100 by norm_num] at a1
  rw [show (1 : ℝ) / 100 / 10 = 1 / 1000 by norm_num] at a2
  rw [show (1 : ℝ) / 1000 / 10 = 1 / 10000 by norm_num] at a3
  obtain ⟨b1, b2⟩ := incr_bounds hρ h2 (h := 1 / 10000) (by norm_num)
  rw [e] at b1
  obtain ⟨l1, l2⟩ := log_10
  obtain ⟨sa, sb⟩ := s3_bounds
  refine ⟨a1, a2, a3, b1, ?_, ?_⟩
  · rw [abs_lt]; constructor
    · linarith
    · have : (1 / √3 + 1 / 10000 / 3) * log 10 = log 10 / √3 + log 10 / 30000 := by ring
      linarith
  · have hl : 2.6585 * √3 < 2 * log 10 := by nlinarith
    have hu : 2 * log 10 < 2.6595 * √3 := by nlinarith
    have h1 : 2 * (log 10 / √3) < 2.6595 := by
      rw [show 2 * (log 10 / √3) = 2 * log 10 / √3 by ring, div_lt_iff₀ s3pos]; linarith
    have h2' : 2.6585 < 2 * (log 10 / √3) := by
      rw [show 2 * (log 10 / √3) = 2 * log 10 / √3 by ring, lt_div_iff₀ s3pos]; linarith
    rw [abs_lt]; constructor <;> linarith

/-- `sec:envelope`'s turnaround function `(rH)² = A_r/r² + 2M/r + r²/α²` and its `r`-derivative. -/
noncomputable def rH2 (α Ar r : ℝ) : ℝ := Ar / r ^ 2 + 2 * (α / (3 * √3)) / r + r ^ 2 / α ^ 2
noncomputable def drH2 (α Ar r : ℝ) : ℝ := -(2 * Ar / r ^ 3) - 2 * (α / (3 * √3)) / r ^ 2 + 2 * r / α ^ 2

lemma rH2_deriv (α Ar : ℝ) {r : ℝ} (hr : r ≠ 0) : HasDerivAt (rH2 α Ar) (drH2 α Ar r) r := by
  have h := (((hasDerivAt_pow 2 r).inv (pow_ne_zero 2 hr)).const_mul Ar).add
    (((hasDerivAt_id r).inv hr).const_mul (2 * (α / (3 * √3)))) |>.add ((hasDerivAt_pow 2 r).div_const (α ^ 2))
  convert h using 1
  · funext s; simp [rH2, div_eq_mul_inv]
  · simp [drH2]; fsr

/-- **Row 101.** The computed checks of the receipt, at the Nariai member (`2M = 2α/(3√3)`), `A = 2^{1/3}α/√3`,
`k = 3/(2α)`. ⓑ the vacuum turning point `(Mα²)^{1/3} = α/√3` and `f′ = 0` there; with `A_r = 4Mr_seam = 4α²/9`
(radiation/matter `= 2` at the seam) the turning point of `(rH)²` is the unique positive root of
`x⁴ − x − 4` in `x = r/(α/√3)`, `|x − 1.5338| < 5·10⁻⁴`, and against the back seam `|x/2 − 0.7669| < 5·10⁻⁴`,
`|x/2 − 1.53| > 0.5`. ⓒ the back seam (`r = −2α/√3`, `dr/ds = −1`, `r̈ = −3√3/(4α)`, at `α = 1` within `10⁻⁶`
of `−1.299038`), the turnaround (`r = −A`, `ṙ = 0`, `r̈ = −3A/(2α²) = −(3/2)(2Mα²)^{1/3}` at `α = 1`, with the
limits), the front seam (`r = α/√3`, `ṙ = 1`, `r̈ = 0`, `r⃛ > 0`), and the unique real root of `f = 2` at `α = 1`
within `10⁻⁷` of `−0.34414212`. ⓓ `A/r_N = 2^{1/3}`, `r_N < A`; the speeds `1, 1, 0`; `2α/√3 = 2^{2/3}A` and the
remaining contour `log(2+√3)/k` within `10⁻⁷` of `0.8779719` at `α = 1`. ⓔ `r` is monotone on both legs; the
phase gaps `4π/3` and `2π`. NOT built: ⓔ③/ⓔ④'s `23.254` per cent (a Beta-type ratio by quadrature). -/
theorem row101_checks {α : ℝ} (hα : 0 < α) :
    -- ⓑ①
    (α / (3 * √3) * α ^ 2) ^ (1 / 3 : ℝ) = α / √3 ∧ deriv (fSdS (α / (3 * √3)) α) (α / √3) = 0 ∧
    -- ⓑ②③
    4 * (α / (3 * √3)) * (α / √3) = 4 * α ^ 2 / 9 ∧
      (4 * (α / (3 * √3)) * (α / √3) / (α / √3) ^ 2) / (2 * (α / (3 * √3)) / (α / √3)) = 2 ∧
      (∀ r > 0, drH2 α (4 * (α / (3 * √3)) * (α / √3)) r = 0 ↔ (r / (α / √3)) ^ 4 - r / (α / √3) - 4 = 0) ∧
      (∃! r : ℝ, 0 < r ∧ drH2 α (4 * (α / (3 * √3)) * (α / √3)) r = 0) ∧
      (∀ r > 0, drH2 α (4 * (α / (3 * √3)) * (α / √3)) r = 0 →
        |r / (α / √3) - 1.5338| < 0.0005 ∧ |r / (2 * α / √3) - 0.7669| < 0.0005 ∧
          0.5 < |r / (2 * α / √3) - 1.53|) ∧
    -- ⓒ①
      rColl α (log (2 + √3) / kk α) = -2 * α / √3 ∧ d1C α (log (2 + √3) / kk α) = -1 ∧
      d1C α (-(log (2 + √3) / kk α)) = 1 ∧
      d2C α (log (2 + √3) / kk α) = -(3 * √3) / (4 * α) ∧ |d2C 1 (log (2 + √3) / kk 1) + 1.299038| < 1e-6 ∧
    -- ⓒ②
      rColl α 0 = -AA α ∧ d1C α 0 = 0 ∧ d2C α 0 = -(3 * AA α) / (2 * α ^ 2) ∧
      d2C 1 0 = -(3 / 2) * (2 * (1 / (3 * √3)) * 1 ^ 2) ^ (1 / 3 : ℝ) ∧
      Tendsto (d1C α) (𝓝 0) (𝓝 0) ∧ Tendsto (d2C α) (𝓝 0) (𝓝 (-(3 * AA α) / (2 * α ^ 2))) ∧
    -- ⓒ③
      rExp α (arsinh (1 / √2) / kk α) = α / √3 ∧ d1E α (arsinh (1 / √2) / kk α) = 1 ∧
      d2E α (arsinh (1 / √2) / kk α) = 0 ∧ 0 < d3E α (arsinh (1 / √2) / kk α) ∧
    -- ⓒ④
      (∀ r ≠ 0, fSdS (1 / (3 * √3)) 1 r = 2 ↔ r ^ 3 + r + 2 * (1 / (3 * √3)) = 0) ∧
      (∃! r : ℝ, r ^ 3 + r + 2 * (1 / (3 * √3)) = 0) ∧
      (∀ r : ℝ, r ^ 3 + r + 2 * (1 / (3 * √3)) = 0 → |r + 0.34414212| < 1e-7) ∧
    -- ⓓ
      AA α / (α / √3) = (2 : ℝ) ^ (1 / 3 : ℝ) ∧ 1 / √3 < AA 1 ∧
      |d1C α (log (2 + √3) / kk α)| = 1 ∧ |d1E α (arsinh (1 / √2) / kk α)| = 1 ∧ |d1C α 0| = 0 ∧
      2 * α / √3 = (2 : ℝ) ^ (2 / 3 : ℝ) * AA α ∧ |log (2 + √3) / kk 1 - 0.8779719| < 1e-7 ∧
    -- ⓔ①②④
      (∀ s < 0, 0 < d1C α s) ∧ (∀ s > 0, 0 < d1E α s) ∧
      2 * π * (α / √3) / (√3 * α) - 2 * π * (-(α / √3)) / (√3 * α) = 4 * π / 3 ∧
      2 * π * (α / √3) / (√3 * α) - 2 * π * (-2 * α / √3) / (√3 * α) = 2 * π ∧
      AA α = (2 : ℝ) ^ (1 / 3 : ℝ) * (α / √3) := by
  have hρ : 0 < α / √3 := by positivity
  have h3 : √3 ^ 3 = 3 * √3 := by rw [pow_succ, s3]
  have hMa : α / (3 * √3) * α ^ 2 = (α / √3) ^ 3 := by rw [div_pow, h3]; ring
  have ha2 : α ^ 2 = 3 * (α / √3) ^ 2 := by rw [div_pow, s3]; field_simp
  have hAr : 4 * (α / (3 * √3)) * (α / √3) = 4 * (α / √3) ^ 4 / α ^ 2 := by
    rw [ha2]; field_simp; try (rw [h3]; ring)
  -- the quartic in `x = r/ρ`
  have hq : ∀ r > 0, drH2 α (4 * (α / (3 * √3)) * (α / √3)) r = 0 ↔
      (r / (α / √3)) ^ 4 - r / (α / √3) - 4 = 0 := fun r hr => by
    have e : drH2 α (4 * (α / (3 * √3)) * (α / √3)) r
        = 2 * (α / √3) ^ 4 / (α ^ 2 * r ^ 3) * ((r / (α / √3)) ^ 4 - r / (α / √3) - 4) := by
      unfold drH2
      rw [hAr, show 2 * (α / (3 * √3)) / r ^ 2 = 2 * (α / (3 * √3) * α ^ 2) / (α ^ 2 * r ^ 2) by
        field_simp, hMa]
      fsr
    rw [e, mul_eq_zero, or_iff_right (by positivity)]
  obtain ⟨⟨x, ⟨hx0, hx⟩, hxu⟩, hbr⟩ := quartic_root
  obtain ⟨b1, b2, b3, b4, b5⟩ := back_seam hα
  obtain ⟨t1, t2, t3', t4, t5, t6⟩ := turnaround hα
  obtain ⟨-, f2, f3, f4, f5⟩ := front_seam hα
  obtain ⟨n1, n2⟩ := null_root
  obtain ⟨sa, sb⟩ := s3_bounds
  obtain ⟨la, lb⟩ := log_2s3
  refine ⟨?_, ?_, ?_, ?_, hq, ?_, fun r hr h => ?_, b3, b4, ?_, b5, ?_, t1, t2, t3', ?_, t5, t6, f2, f3, f4, f5,
    fun r hr => ?_, n1, n2, ?_, ?_, by rw [b4]; norm_num, by rw [f3]; norm_num, by rw [t2]; norm_num, ?_, ?_,
    (legs_monotone hα).1, (legs_monotone hα).2, ?_, ?_, by unfold AA; ring⟩
  · rw [hMa, show (1 / 3 : ℝ) = ((3 : ℕ) : ℝ)⁻¹ by norm_num]
    exact pow_rpow_inv_natCast hρ.le (by norm_num)
  · rw [(fSdS_hasDerivAt _ α hρ.ne').deriv, ha2]; fsr
  · field_simp; rw [s3]; ring
  · fsr
  · refine ⟨x * (α / √3), ⟨by positivity, (hq _ (by positivity)).2 (by rwa [mul_div_assoc, div_self hρ.ne', mul_one])⟩,
      fun y ⟨hy, hy0⟩ => ?_⟩
    have := hxu (y / (α / √3)) ⟨by positivity, (hq y hy).1 hy0⟩
    rw [← this]; field_simp
  · obtain ⟨c1, c2⟩ := hbr _ (by positivity) ((hq r hr).1 h)
    have e : r / (2 * α / √3) = r / (α / √3) / 2 := by field_simp
    rw [e]
    refine ⟨by rw [abs_lt]; constructor <;> linarith, by rw [abs_lt]; constructor <;> linarith, ?_⟩
    rw [lt_abs]; right; linarith
  · rw [show -(log (2 + √3) / kk α) = -1 * (log (2 + √3) / kk α) by ring]
    have : d1C α (-1 * (log (2 + √3) / kk α)) = -d1C α (log (2 + √3) / kk α) := by
      unfold d1C; rw [show kk α * (-1 * (log (2 + √3) / kk α)) = -(kk α * (log (2 + √3) / kk α)) by ring,
        sinh_neg, cosh_neg]; ring
    rw [this, b4]; norm_num
  · rw [(back_seam one_pos).2.2.2.2, abs_lt]; constructor <;> nlinarith
  · rw [(turnaround one_pos).2.2.1, (turnaround one_pos).2.2.2.1]; ring
  · rw [← sub_eq_zero, show fSdS (1 / (3 * √3)) 1 r - 2 = -(r ^ 3 + r + 2 * (1 / (3 * √3))) / r by
      unfold fSdS; fsr, div_eq_zero_iff, neg_eq_zero, or_iff_left hr]
  · unfold AA; field_simp
  · unfold AA
    have : (1 : ℝ) < 2 ^ (1 / 3 : ℝ) := one_lt_rpow (by norm_num) (by norm_num)
    rw [mul_one]; exact div_lt_div_of_pos_right this s3pos
  · unfold AA
    rw [show 2 ^ (2 / 3 : ℝ) * (2 ^ (1 / 3 : ℝ) * α / √3) = 2 ^ (2 / 3 : ℝ) * 2 ^ (1 / 3 : ℝ) * α / √3 by ring,
      ← rpow_add (by norm_num)]; norm_num
  · rw [show kk 1 = 3 / 2 by norm_num [kk], abs_lt]; constructor <;> linarith
  · field_simp; rw [s3]; ring
  · field_simp; rw [s3]; ring

/-! ## The warped table: `diag(F₀(x), F₁(x), F₂(x), F₃(x)·S(y))` in `(x, y, z, w)`, THE connection

One table carries both 4D metrics row 100 computes: the limit metric in its planar patch and SdS in its static
chart. Generated (sympy) and then proved, component by component, from the engine's `curvD_eq`. -/

section Warped

set_option synthInstance.maxHeartbeats 400000

/-- The warped table `R(eᵢ,eⱼ)eₖ` component `l`. -/
noncomputable def tW (f00 f01 f02 f10 f11 f12 f20 f21 f22 f30 f31 f32 s0 s1 s2 : ℝ) (i j k l : Fin 4) : ℝ :=
  if (i, j, k, l) = (0, 1, 0, 1) then (2*f00*f10*f12 - f00*f11^2 - f01*f10*f11)/(4*f00*f10^2) else
  if (i, j, k, l) = (0, 1, 1, 0) then -(2*f00*f10*f12 - f00*f11^2 - f01*f10*f11)/(4*f00^2*f10) else
  if (i, j, k, l) = (0, 2, 0, 2) then (2*f00*f20*f22 - f00*f21^2 - f01*f20*f21)/(4*f00*f20^2) else
  if (i, j, k, l) = (0, 2, 2, 0) then -(2*f00*f20*f22 - f00*f21^2 - f01*f20*f21)/(4*f00^2*f20) else
  if (i, j, k, l) = (0, 3, 0, 3) then (2*f00*f30*f32 - f00*f31^2 - f01*f30*f31)/(4*f00*f30^2) else
  if (i, j, k, l) = (0, 3, 1, 3) then s1*(f10*f31 - f11*f30)/(4*f10*f30*s0) else
  if (i, j, k, l) = (0, 3, 3, 0) then -s0*(2*f00*f30*f32 - f00*f31^2 - f01*f30*f31)/(4*f00^2*f30) else
  if (i, j, k, l) = (0, 3, 3, 1) then -s1*(f10*f31 - f11*f30)/(4*f10^2) else
  if (i, j, k, l) = (1, 0, 0, 1) then -(2*f00*f10*f12 - f00*f11^2 - f01*f10*f11)/(4*f00*f10^2) else
  if (i, j, k, l) = (1, 0, 1, 0) then (2*f00*f10*f12 - f00*f11^2 - f01*f10*f11)/(4*f00^2*f10) else
  if (i, j, k, l) = (1, 2, 1, 2) then f11*f21/(4*f00*f20) else
  if (i, j, k, l) = (1, 2, 2, 1) then -f11*f21/(4*f00*f10) else
  if (i, j, k, l) = (1, 3, 0, 3) then s1*(f10*f31 - f11*f30)/(4*f10*f30*s0) else
  if (i, j, k, l) = (1, 3, 1, 3) then (2*f00*f30*s0*s2 - f00*f30*s1^2 + f11*f31*s0^2)/(4*f00*f30*s0^2) else
  if (i, j, k, l) = (1, 3, 3, 0) then -s1*(f10*f31 - f11*f30)/(4*f00*f10) else
  if (i, j, k, l) = (1, 3, 3, 1) then -(2*f00*f30*s0*s2 - f00*f30*s1^2 + f11*f31*s0^2)/(4*f00*f10*s0) else
  if (i, j, k, l) = (2, 0, 0, 2) then -(2*f00*f20*f22 - f00*f21^2 - f01*f20*f21)/(4*f00*f20^2) else
  if (i, j, k, l) = (2, 0, 2, 0) then (2*f00*f20*f22 - f00*f21^2 - f01*f20*f21)/(4*f00^2*f20) else
  if (i, j, k, l) = (2, 1, 1, 2) then -f11*f21/(4*f00*f20) else
  if (i, j, k, l) = (2, 1, 2, 1) then f11*f21/(4*f00*f10) else
  if (i, j, k, l) = (2, 3, 2, 3) then f21*f31/(4*f00*f30) else
  if (i, j, k, l) = (2, 3, 3, 2) then -f21*f31*s0/(4*f00*f20) else
  if (i, j, k, l) = (3, 0, 0, 3) then -(2*f00*f30*f32 - f00*f31^2 - f01*f30*f31)/(4*f00*f30^2) else
  if (i, j, k, l) = (3, 0, 1, 3) then -s1*(f10*f31 - f11*f30)/(4*f10*f30*s0) else
  if (i, j, k, l) = (3, 0, 3, 0) then s0*(2*f00*f30*f32 - f00*f31^2 - f01*f30*f31)/(4*f00^2*f30) else
  if (i, j, k, l) = (3, 0, 3, 1) then s1*(f10*f31 - f11*f30)/(4*f10^2) else
  if (i, j, k, l) = (3, 1, 0, 3) then -s1*(f10*f31 - f11*f30)/(4*f10*f30*s0) else
  if (i, j, k, l) = (3, 1, 1, 3) then -(2*f00*f30*s0*s2 - f00*f30*s1^2 + f11*f31*s0^2)/(4*f00*f30*s0^2) else
  if (i, j, k, l) = (3, 1, 3, 0) then s1*(f10*f31 - f11*f30)/(4*f00*f10) else
  if (i, j, k, l) = (3, 1, 3, 1) then (2*f00*f30*s0*s2 - f00*f30*s1^2 + f11*f31*s0^2)/(4*f00*f10*s0) else
  if (i, j, k, l) = (3, 2, 2, 3) then -f21*f31/(4*f00*f30) else
  if (i, j, k, l) = (3, 2, 3, 2) then f21*f31*s0/(4*f00*f20) else
  0

/-- The angular factor `G = (1, 1, 1, S)`. -/
noncomputable def GW (S : ℝ → ℝ) : Fin 4 → ℝ → ℝ := ![fun _ => 1, fun _ => 1, fun _ => 1, S]

variable {F : Fin 4 → ℝ → ℝ} {S : ℝ → ℝ} (hF : ∀ k, ContDiff ℝ ∞ (F k)) (hS : ContDiff ℝ ∞ S)
  (hF0 : ∀ k s, F k s ≠ 0) (hS0 : ∀ s, S s ≠ 0)

include hS in
lemma GW_smooth (k : Fin 4) : ContDiff ℝ ∞ (GW S k) := by
  fin_cases k <;> simp [GW] <;> first | exact hS | exact contDiff_const

include hF0 hS0 in
lemma W_ne (i : Fin 4) (p : Fin 4 → ℝ) : cS F (GW S) i p ≠ 0 := by
  fin_cases i <;> simp [cS, GW, hF0, hS0]

/-- THE connection's curvature on basis fields at `p`, for `diag(F₀, F₁, F₂, F₃S)`. -/
noncomputable def RW (p : Fin 4 → ℝ) (i j k : Fin 4) : Fin 4 → ℝ :=
  curv (lcConn (Fin 4 → ℝ) (ndOf (diag4 (cS F (GW S))) (diag4_symm _)
    (fun p u h => diag4_nondeg (fun i => W_ne hF0 hS0 i p) u h)
    ((diag4_smooth (cS_smooth hF (GW_smooth hS))).differentiable (by simp))))
    (fun _ => (Pi.single i 1 : Fin 4 → ℝ)) (fun _ => (Pi.single j 1 : Fin 4 → ℝ))
    (fun _ => (Pi.single k 1 : Fin 4 → ℝ)) p

set_option maxHeartbeats 8000000 in
/-- **The warped table**, for any `F₀..F₃` and `S`. -/
theorem warped_table (p : Fin 4 → ℝ) (i j k l : Fin 4) :
    RW hF hS hF0 hS0 p i j k l = tW (F 0 (p 0)) (deriv (F 0) (p 0)) (deriv (deriv (F 0)) (p 0))
      (F 1 (p 0)) (deriv (F 1) (p 0)) (deriv (deriv (F 1)) (p 0))
      (F 2 (p 0)) (deriv (F 2) (p 0)) (deriv (deriv (F 2)) (p 0))
      (F 3 (p 0)) (deriv (F 3) (p 0)) (deriv (deriv (F 3)) (p 0))
      (S (p 1)) (deriv S (p 1)) (deriv (deriv S) (p 1)) i j k l := by
  rw [RW, curvD_eq (W_ne hF0 hS0) (cS_smooth hF (GW_smooth hS))]
  have h1 := fun k v => dC1_cS hF (GW_smooth hS) p k v
  have h2 := fun k u v => dC2_cS hF (GW_smooth hS) p k u v
  have h1' : ∀ k v, fderiv ℝ (cS F (GW S) k) p v = _ := fun k v => h1 k v
  have hGv : ∀ k, GW S k (p 1) = (![1, 1, 1, S (p 1)] : Fin 4 → ℝ) k := fun k => by fin_cases k <;> rfl
  have hDG : ∀ k, deriv (GW S k) (p 1) = (![0, 0, 0, deriv S (p 1)] : Fin 4 → ℝ) k := fun k => by
    fin_cases k <;> simp [GW]
  have hDDG : ∀ k, deriv (deriv (GW S k)) (p 1) = (![0, 0, 0, deriv (deriv S) (p 1)] : Fin 4 → ℝ) k :=
    fun k => by fin_cases k <;> simp [GW]
  have := hF0 0 (p 0); have := hF0 1 (p 0); have := hF0 2 (p 0); have := hF0 3 (p 0); have := hS0 (p 1)
  fin_cases i <;> fin_cases j <;> fin_cases k <;> fin_cases l <;>
    (simp only [curvD, Pi.sub_apply, Pi.add_apply, DGD, gamD, h1', h1, h2, hGv, hDG, hDDG]
     simp [cS, tW, Fin.sum_univ_four, hGv]
     try (field_simp; ring))

/-- `sin²θ` and its two derivatives at `θ`. (Copied from `CurvatureInstances.lean`.) -/
lemma sin2_facts {S : ℝ → ℝ} {θ : ℝ} (eS : S =ᶠ[𝓝 θ] fun s => Real.sin s ^ 2) :
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

end Warped

/-! ### The limit metric in its planar patch: `−dT² + e^{−2HT}dχ² + H⁻²(dθ² + sin²θ dφ²)`, `H = √Λ`,
in the coordinate order `(T, θ, χ, φ)` -/

section Planar

set_option synthInstance.maxHeartbeats 400000

noncomputable def FP (H : ℝ) : Fin 4 → ℝ → ℝ :=
  ![fun _ => -1, fun _ => 1 / H ^ 2, fun s => Real.exp (-(2 * H * s)), fun _ => 1 / H ^ 2]

lemma FP_smooth (H : ℝ) (k : Fin 4) : ContDiff ℝ ∞ (FP H k) := by fin_cases k <;> simp [FP] <;> fun_prop

lemma FP_ne {H : ℝ} (hH : H ≠ 0) (k : Fin 4) (s : ℝ) : FP H k s ≠ 0 := by
  fin_cases k <;> simp [FP, hH, Real.exp_ne_zero]

variable {S : ℝ → ℝ} (hS : ContDiff ℝ ∞ S) (hS0 : ∀ s, S s ≠ 0)

open Filter Topology in
include hS hS0 in
/-- **Row 100, Ⓔ①②.** THE connection on the limit metric: `Ric = Λg` (Einstein, the vacuum equation of SdS),
`R = 4Λ`, and `Riem² = 8Λ²`, with `Λ = H²`, identically in `H`. -/
theorem planar_invariants {H : ℝ} (hH : H ≠ 0) (p : Fin 4 → ℝ) (eS : S =ᶠ[𝓝 (p 1)] fun s => Real.sin s ^ 2) :
    (∀ j k, ricC (RW (FP_smooth H) hS (FP_ne hH) hS0 p) j k = H ^ 2 * if j = k then cS (FP H) (GW S) j p else 0) ∧
      scalC (fun i => cS (FP H) (GW S) i p) (RW (FP_smooth H) hS (FP_ne hH) hS0 p) = 4 * H ^ 2 ∧
      riem2C (fun i => cS (FP H) (GW S) i p) (RW (FP_smooth H) hS (FP_ne hH) hS0 p) = 8 * (H ^ 2) ^ 2 := by
  obtain ⟨hSv, hS1, hS2⟩ := sin2_facts eS
  have hs : Real.sin (p 1) ≠ 0 := fun h => hS0 (p 1) (by rw [hSv, h]; simp)
  have x1 : ∀ s, HasDerivAt (fun s => Real.exp (-(2 * H * s))) (-(2 * H) * Real.exp (-(2 * H * s))) s := fun s =>
    HasDerivAt.congr_deriv (((hasDerivAt_id' s).const_mul (2 * H)).neg.exp) (by simp only [Pi.neg_apply]; ring)
  have f1 : deriv (fun s => Real.exp (-(2 * H * s))) = fun s => -(2 * H) * Real.exp (-(2 * H * s)) :=
    funext fun s => (x1 s).deriv
  have f2 : deriv (fun s => -(2 * H) * Real.exp (-(2 * H * s))) = fun s => 4 * H ^ 2 * Real.exp (-(2 * H * s)) :=
    funext fun s => (((x1 s).const_mul (-(2 * H)))).deriv.trans (by ring)
  have hd : ∀ k, deriv (FP H k) (p 0) = (![0, 0, -(2 * H) * Real.exp (-(2 * H * p 0)), 0] : Fin 4 → ℝ) k :=
    fun k => by fin_cases k <;> simp [FP, f1]
  have hdd : ∀ k, deriv (deriv (FP H k)) (p 0) = (![0, 0, 4 * H ^ 2 * Real.exp (-(2 * H * p 0)), 0] : Fin 4 → ℝ) k :=
    fun k => by fin_cases k <;> simp [FP, f1] <;> ring
  have he := Real.exp_ne_zero (-(2 * H * p 0))
  have hR : ∀ j k, ricC (RW (FP_smooth H) hS (FP_ne hH) hS0 p) j k = H ^ 2 * if j = k then cS (FP H) (GW S) j p else 0 := by
    intro j k
    simp only [ricC, Fin.sum_univ_four, warped_table, hd, hdd]
    fin_cases j <;> fin_cases k <;> simp [tW, FP, GW, cS, hSv, hS1, hS2] <;> field_simp <;> ring
  refine ⟨hR, ?_, ?_⟩
  · simp only [scalC, Fin.sum_univ_four, hR]; simp [FP, GW, cS, hSv]; field_simp; ring
  · simp only [riem2C, Fin.sum_univ_four, warped_table, hd, hdd]
    simp [tW, FP, GW, cS, hSv, hS1, hS2]
    field_simp; ring

end Planar

/-! ### SdS in its static chart, coordinate order `(r, θ, t, φ)`: `diag(1/f, P, −f, P sin²θ)`; the profiles `Fr`, `P`
equal `f = 1 − 2M/r − Λr²/3` and `r²` near the point -/

section SdS

set_option synthInstance.maxHeartbeats 400000

noncomputable def FS (Fr P : ℝ → ℝ) : Fin 4 → ℝ → ℝ := ![fun s => (Fr s)⁻¹, P, fun s => -Fr s, P]

variable {Fr P S : ℝ → ℝ} (hFr : ContDiff ℝ ∞ Fr) (hP : ContDiff ℝ ∞ P) (hS : ContDiff ℝ ∞ S)
  (hFr0 : ∀ s, Fr s ≠ 0) (hP0 : ∀ s, P s ≠ 0) (hS0 : ∀ s, S s ≠ 0)

include hFr hP hFr0 in
lemma FS_smooth (k : Fin 4) : ContDiff ℝ ∞ (FS Fr P k) := by
  fin_cases k
  exacts [hFr.inv hFr0, hP, hFr.neg, hP]

include hFr0 hP0 in
lemma FS_ne (k : Fin 4) (s : ℝ) : FS Fr P k s ≠ 0 := by
  fin_cases k <;> simp [FS, hFr0, hP0]

/-- The SdS radial profile's two derivatives at `r ≠ 0`. (As `sds_derivs` in `CurvatureInstances.lean`.) -/
lemma sds_derivs (M Λ r : ℝ) (hr : r ≠ 0) :
    deriv (fun s => 1 - 2 * M * s⁻¹ - Λ / 3 * s ^ 2) r = 2 * M * (r ^ 2)⁻¹ - 2 * Λ / 3 * r ∧
      deriv (deriv (fun s => 1 - 2 * M * s⁻¹ - Λ / 3 * s ^ 2)) r = -(4 * M / r ^ 3) - 2 * Λ / 3 := by
  have hf1 : ∀ s, s ≠ 0 → HasDerivAt (fun s => 1 - 2 * M * s⁻¹ - Λ / 3 * s ^ 2)
      (2 * M * (s ^ 2)⁻¹ - 2 * Λ / 3 * s) s := fun s hs =>
    (show HasDerivAt (fun s => 1 - 2 * M * s⁻¹ - Λ / 3 * s ^ 2) _ s from
      ((hasDerivAt_const s (1 : ℝ)).sub ((hasDerivAt_inv hs).const_mul (2 * M))).sub
        ((hasDerivAt_pow 2 s).const_mul (Λ / 3))).congr_deriv (by norm_num; ring)
  have ed : deriv (fun s => 1 - 2 * M * s⁻¹ - Λ / 3 * s ^ 2) =ᶠ[𝓝 r]
      fun s => 2 * M * (s ^ 2)⁻¹ - 2 * Λ / 3 * s :=
    Filter.eventually_of_mem (isOpen_ne.mem_nhds hr) fun s hs => (hf1 s hs).deriv
  refine ⟨(hf1 r hr).deriv, ?_⟩
  rw [ed.deriv_eq, (show HasDerivAt (fun s => 2 * M * (s ^ 2)⁻¹ - 2 * Λ / 3 * s) _ r from
      (((hasDerivAt_pow 2 r).inv (pow_ne_zero 2 hr)).const_mul (2 * M)).sub
        ((hasDerivAt_id r).const_mul (2 * Λ / 3))).deriv]
  field_simp; ring

open Filter Topology in
include hFr hP hS hFr0 hP0 hS0 in
/-- **Row 100, Ⓔ③ (the SdS side).** THE connection's Kretschmann scalar of SdS at any point of the static chart
(`f(r) ≠ 0`) is `48M²/r⁶ + 8Λ²/3`, from the warped table. -/
theorem sds_kretschmann_W (M Λ : ℝ) (p : Fin 4 → ℝ)
    (eF : Fr =ᶠ[𝓝 (p 0)] fun s => 1 - 2 * M * s⁻¹ - Λ / 3 * s ^ 2) (eP : P =ᶠ[𝓝 (p 0)] fun s => s ^ 2)
    (eS : S =ᶠ[𝓝 (p 1)] fun s => Real.sin s ^ 2) :
    riem2C (fun i => cS (FS Fr P) (GW S) i p) (RW (FS_smooth hFr hP hFr0) hS (FS_ne hFr0 hP0) hS0 p)
      = 48 * M ^ 2 / p 0 ^ 6 + 8 * Λ ^ 2 / 3 := by
  set r := p 0 with hr_def
  have hr : r ≠ 0 := fun h => hP0 r (by rw [eP.eq_of_nhds, h]; simp)
  obtain ⟨d1, d2⟩ := sds_derivs M Λ r hr
  have hF0v : Fr r = 1 - 2 * M * r⁻¹ - Λ / 3 * r ^ 2 := eF.eq_of_nhds
  have hF1v : deriv Fr r = _ := eF.deriv_eq.trans d1
  have hF2v : deriv (deriv Fr) r = _ := eF.deriv.deriv_eq.trans d2
  have hPv : P r = r ^ 2 := eP.eq_of_nhds
  have hP1 : deriv P r = 2 * r := by rw [eP.deriv_eq]; simp
  have hP2 : deriv (deriv P) r = 2 := by
    rw [(eP.deriv.trans (Eventually.of_forall fun s => by simp) : deriv P =ᶠ[𝓝 r] fun s => 2 * s).deriv_eq]; simp
  obtain ⟨hSv, hS1, hS2⟩ := sin2_facts eS
  have hs : Real.sin (p 1) ≠ 0 := fun h => hS0 (p 1) (by rw [hSv, h]; simp)
  have dF := fun s => ((hFr.differentiable (by simp)) s).hasDerivAt
  have dF' := fun s => (((contDiff_infty_iff_deriv.1 hFr).2.differentiable (by simp)) s).hasDerivAt
  have iv1 : deriv (fun s => (Fr s)⁻¹) = fun s => -(deriv Fr s) / Fr s ^ 2 :=
    funext fun s => ((dF s).inv (hFr0 s)).deriv.trans (by ring)
  have iv2 : deriv (deriv (fun s => (Fr s)⁻¹)) r = (2 * deriv Fr r ^ 2 - Fr r * deriv (deriv Fr) r) / Fr r ^ 3 := by
    rw [iv1, (show HasDerivAt (fun s => -deriv Fr s / Fr s ^ 2) _ r from
      (dF' r).neg.div ((dF r).pow 2) (pow_ne_zero 2 (hFr0 r))).deriv]
    have := hFr0 r; simp only [Pi.neg_apply]; field_simp; ring
  have ng1 : deriv (fun s => -Fr s) = fun s => -deriv Fr s := funext fun s => deriv.neg
  have hd : ∀ k, deriv (FS Fr P k) r = (![-(deriv Fr r) / Fr r ^ 2, deriv P r, -deriv Fr r, deriv P r] : Fin 4 → ℝ) k :=
    fun k => by fin_cases k <;> simp [FS, iv1, ng1]
  have hdd : ∀ k, deriv (deriv (FS Fr P k)) r = (![(2 * deriv Fr r ^ 2 - Fr r * deriv (deriv Fr) r) / Fr r ^ 3,
      deriv (deriv P) r, -deriv (deriv Fr) r, deriv (deriv P) r] : Fin 4 → ℝ) k :=
    fun k => by fin_cases k <;> simp [FS, iv2, ng1]
  have hf := hFr0 r
  simp only [riem2C, Fin.sum_univ_four, warped_table, ← hr_def, hd, hdd]
  rw [show (48 * M ^ 2 / r ^ 6 + 8 * Λ ^ 2 / 3 : ℝ)
      = deriv (deriv Fr) r ^ 2 + 4 * deriv Fr r ^ 2 / r ^ 2 + 4 * (Fr r - 1) ^ 2 / r ^ 4 by
    rw [hF0v, hF1v, hF2v]; field_simp; ring]
  simp [tW, FS, GW, cS, ← hr_def, hPv, hP1, hP2, hSv, hS1, hS2]
  field_simp
  ring

end SdS


end ShadowProbe.LimitNariai


#print axioms ShadowProbe.LimitNariai.row105_checks
#print axioms ShadowProbe.LimitNariai.row12_checks
#print axioms ShadowProbe.LimitNariai.row12_blueshift
#print axioms ShadowProbe.LimitNariai.row21_checks



#print axioms ShadowProbe.LimitNariai.row101_checks
#print axioms ShadowProbe.LimitNariai.row100_checks
#print axioms ShadowProbe.LimitNariai.row100_exact
#print axioms ShadowProbe.LimitNariai.row100_flow
#print axioms ShadowProbe.LimitNariai.row100_rates
#print axioms ShadowProbe.LimitNariai.row100_decades
#print axioms ShadowProbe.LimitNariai.row100_deviation_instance
#print axioms ShadowProbe.LimitNariai.row100_simple_instance
#print axioms ShadowProbe.LimitNariai.chi_block_gauss
#print axioms ShadowProbe.LimitNariai.warped_table
#print axioms ShadowProbe.LimitNariai.planar_invariants
#print axioms ShadowProbe.LimitNariai.sds_kretschmann_W
#print axioms ShadowProbe.LimitNariai.row100_kretschmann_at_rN

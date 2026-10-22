/-
Campaign 56, piece F — the full-sky F law.

For real `ν₁, ν₂ > 0`, if `X ~ χ²_{ν₁}` and `Y ~ χ²_{ν₂}` are independent (χ²_ν = Gamma(ν/2, rate 1/2),
Mathlib's `gammaMeasure (ν/2) (1/2)`), then the law of `(X/ν₁)/(Y/ν₂)` is the F(ν₁, ν₂) law with density
  f(r) = (ν₁/ν₂)^{ν₁/2} r^{ν₁/2-1} (1 + ν₁ r/ν₂)^{-(ν₁+ν₂)/2} / B(ν₁/2, ν₂/2)   on r > 0.
`B` is Mathlib's `ProbabilityTheory.beta α β = Γ α Γ β / Γ (α+β)`, which equals the real part of
`Complex.betaIntegral α β` (`ProbabilityTheory.beta_eq_betaIntegralReal`).

Stated as an equality of measures: the pushforward of the product measure is `volume.withDensity f`.
-/
import Mathlib

open MeasureTheory ProbabilityTheory Set
open scoped ENNReal

namespace ShadowProbe.FLaw

/-- χ²_ν as the Gamma law with shape `ν/2` and rate `1/2`. -/
noncomputable def chiSq (ν : ℝ) : Measure ℝ := gammaMeasure (ν / 2) (1 / 2)

/-- The F(ν₁, ν₂) density, real-valued, zero off `r > 0`. -/
noncomputable def fPDFReal (ν₁ ν₂ r : ℝ) : ℝ :=
  if 0 < r then
    (ν₁ / ν₂) ^ (ν₁ / 2) * r ^ (ν₁ / 2 - 1) * (1 + ν₁ * r / ν₂) ^ (-((ν₁ + ν₂) / 2))
      / ProbabilityTheory.beta (ν₁ / 2) (ν₂ / 2)
  else 0

/-- The F(ν₁, ν₂) density, `ℝ≥0∞`-valued. -/
noncomputable def fPDF (ν₁ ν₂ r : ℝ) : ℝ≥0∞ := ENNReal.ofReal (fPDFReal ν₁ ν₂ r)

/-- The F(ν₁, ν₂) law. -/
noncomputable def fMeasure (ν₁ ν₂ : ℝ) : Measure ℝ := volume.withDensity (fPDF ν₁ ν₂)

/-- The ratio statistic `(x/ν₁)/(y/ν₂)`. -/
noncomputable def ratio (ν₁ ν₂ : ℝ) (p : ℝ × ℝ) : ℝ := (p.1 / ν₁) / (p.2 / ν₂)

/-! ### Measurability -/

@[fun_prop]
lemma measurable_gammaPDF (a l : ℝ) : Measurable (gammaPDF a l) :=
  (measurable_gammaPDFReal a l).ennreal_ofReal

lemma measurable_fPDFReal (ν₁ ν₂ : ℝ) : Measurable (fPDFReal ν₁ ν₂) := by
  unfold fPDFReal
  refine Measurable.ite measurableSet_Ioi ?_ measurable_const
  fun_prop

@[fun_prop]
lemma measurable_fPDF (ν₁ ν₂ : ℝ) : Measurable (fPDF ν₁ ν₂) :=
  (measurable_fPDFReal ν₁ ν₂).ennreal_ofReal

@[fun_prop]
lemma measurable_ratio (ν₁ ν₂ : ℝ) : Measurable (ratio ν₁ ν₂) := by
  unfold ratio; fun_prop

/-! ### Two integration lemmas -/

/-- A function vanishing on `(-∞,0)` has its Lebesgue integral carried by `(0,∞)`. -/
lemma lintegral_eq_setLIntegral_Ioi {F : ℝ → ℝ≥0∞} (h : ∀ y < 0, F y = 0) :
    ∫⁻ y, F y = ∫⁻ y in Ioi 0, F y := by
  rw [← lintegral_add_compl F (measurableSet_Ioi (a := (0 : ℝ))), compl_Ioi,
    setLIntegral_congr (Iio_ae_eq_Iic (a := (0 : ℝ))).symm,
    setLIntegral_congr_fun measurableSet_Iio (g := fun _ => 0) (fun y hy => h y hy),
    lintegral_zero, add_zero]

/-- Linear substitution `x = a r`, `a > 0`, for the Lebesgue integral on `ℝ`. -/
lemma lintegral_comp_mul_pos {F : ℝ → ℝ≥0∞} (hF : Measurable F) {a : ℝ} (ha : 0 < a) :
    ∫⁻ x, F x = ENNReal.ofReal a * ∫⁻ r, F (a * r) := by
  have h1 : ∫⁻ r, F (a * r) = ∫⁻ x, F x ∂(Measure.map (a * ·) volume) :=
    (lintegral_map hF (measurable_const_mul a)).symm
  rw [h1, Real.map_volume_mul_left ha.ne', lintegral_smul_measure, smul_eq_mul, ← mul_assoc,
    ← ENNReal.ofReal_mul ha.le, abs_of_pos (inv_pos.2 ha), mul_inv_cancel₀ ha.ne',
    ENNReal.ofReal_one, one_mul]

lemma setLIntegral_gammaPDF_Ioi {a l : ℝ} (ha : 0 < a) (hl : 0 < l) :
    ∫⁻ y in Ioi 0, gammaPDF a l y = 1 := by
  rw [← lintegral_eq_setLIntegral_Ioi (fun y hy => gammaPDF_of_neg hy)]
  exact lintegral_gammaPDF_eq_one ha hl

/-! ### The pointwise Gamma–Beta identity -/

/-- After the substitution `x = c y r`, the joint density times the Jacobian `c y` factors as
the F density at `r` times a Gamma(α+β, (1+cr)/2) density in `y`. -/
lemma core_real {α β c r y : ℝ} (hα : 0 < α) (hβ : 0 < β) (hc : 0 < c) (hr : 0 < r)
    (hy : 0 < y) :
    gammaPDFReal β (1 / 2) y * (c * y * gammaPDFReal α (1 / 2) (c * y * r)) =
      c ^ α * r ^ (α - 1) * (1 + c * r) ^ (-(α + β)) / ProbabilityTheory.beta α β *
        gammaPDFReal (α + β) ((1 + c * r) / 2) y := by
  have hq : 0 < 1 + c * r := by positivity
  unfold gammaPDFReal ProbabilityTheory.beta
  have hcyr : 0 ≤ c * y * r := by positivity
  simp only [hy.le, hcyr, ↓reduceIte]
  have hGa := Real.Gamma_pos_of_pos hα
  have hGb := Real.Gamma_pos_of_pos hβ
  have hGab := Real.Gamma_pos_of_pos (add_pos hα hβ)
  rw [Real.mul_rpow (by positivity) hr.le, Real.mul_rpow hc.le hy.le,
    show c ^ α = c ^ (α - 1) * c by rw [← Real.rpow_add_one hc.ne', sub_add_cancel],
    show α + β - 1 = (β - 1) + (α - 1) + 1 by ring, Real.rpow_add_one hy.ne',
    Real.rpow_add hy, Real.div_rpow hq.le zero_le_two, Real.rpow_add zero_lt_two,
    Real.div_rpow zero_le_one zero_le_two, Real.div_rpow zero_le_one zero_le_two,
    Real.one_rpow, Real.one_rpow, Real.rpow_neg hq.le,
    show Real.exp (-((1 + c * r) / 2 * y)) =
      Real.exp (-(1 / 2 * y)) * Real.exp (-(1 / 2 * (c * y * r))) by
        rw [← Real.exp_add]; ring_nf]
  have h1 : 0 < (2 : ℝ) ^ α := by positivity
  have h2 : 0 < (2 : ℝ) ^ β := by positivity
  have h3 : 0 < (1 + c * r) ^ (α + β) := by positivity
  field_simp

/-- The same identity in `ℝ≥0∞`, with the parameters of the χ² laws and `c = ν₁/ν₂`. -/
lemma core_ennreal {ν₁ ν₂ r y : ℝ} (h₁ : 0 < ν₁) (h₂ : 0 < ν₂) (hr : 0 < r) (hy : 0 < y) :
    gammaPDF (ν₂ / 2) (1 / 2) y *
        (ENNReal.ofReal (ν₁ / ν₂ * y) * gammaPDF (ν₁ / 2) (1 / 2) (ν₁ / ν₂ * y * r)) =
      fPDF ν₁ ν₂ r * gammaPDF (ν₁ / 2 + ν₂ / 2) ((1 + ν₁ / ν₂ * r) / 2) y := by
  have hc : 0 < ν₁ / ν₂ := div_pos h₁ h₂
  have hα : 0 < ν₁ / 2 := by positivity
  have hβ : 0 < ν₂ / 2 := by positivity
  have key := core_real hα hβ hc hr hy
  have hf : fPDFReal ν₁ ν₂ r = (ν₁ / ν₂) ^ (ν₁ / 2) * r ^ (ν₁ / 2 - 1) *
      (1 + ν₁ / ν₂ * r) ^ (-(ν₁ / 2 + ν₂ / 2)) / ProbabilityTheory.beta (ν₁ / 2) (ν₂ / 2) := by
    rw [fPDFReal, ite_eq_left_of_eq_true _ _ (eq_true hr), show 1 + ν₁ * r / ν₂ = 1 + ν₁ / ν₂ * r by ring,
      show -((ν₁ + ν₂) / 2) = -(ν₁ / 2 + ν₂ / 2) by ring]
  have hfn : 0 ≤ fPDFReal ν₁ ν₂ r := by
    rw [hf]; have := ProbabilityTheory.beta_pos hα hβ; positivity
  unfold fPDF gammaPDF
  rw [← ENNReal.ofReal_mul (by positivity), ← ENNReal.ofReal_mul (gammaPDFReal_nonneg hβ
    one_half_pos _), ← ENNReal.ofReal_mul hfn, hf, key]

/-! ### The F law -/

/-- The headline identity in integral form: for every measurable test function `φ`,
`∫ φ d(law of (X/ν₁)/(Y/ν₂)) = ∫ φ(r) f(r) dr`. -/
theorem lintegral_map_ratio {ν₁ ν₂ : ℝ} (h₁ : 0 < ν₁) (h₂ : 0 < ν₂) {φ : ℝ → ℝ≥0∞}
    (hφ : Measurable φ) :
    ∫⁻ t, φ t ∂((chiSq ν₁).prod (chiSq ν₂)).map (ratio ν₁ ν₂) =
      ∫⁻ r, fPDF ν₁ ν₂ r * φ r := by
  have hc : 0 < ν₁ / ν₂ := div_pos h₁ h₂
  have hα : 0 < ν₁ / 2 := by positivity
  have hβ : 0 < ν₂ / 2 := by positivity
  -- push forward, then write the product law with its product density
  rw [lintegral_map hφ (measurable_ratio ν₁ ν₂), chiSq, chiSq, gammaMeasure, gammaMeasure,
    prod_withDensity (measurable_gammaPDF _ _) (measurable_gammaPDF _ _),
    lintegral_withDensity_eq_lintegral_mul _ (by fun_prop) (by fun_prop)]
  simp only [Pi.mul_apply]
  -- Tonelli, `y` outside
  rw [lintegral_prod_symm _ (by fun_prop)]
  -- only `y > 0` contributes
  rw [lintegral_eq_setLIntegral_Ioi (fun y hy => by
    simp [gammaPDF_of_neg hy])]
  -- substitute `x = (ν₁/ν₂) y r` in the inner integral
  have hsub : ∀ y ∈ Ioi (0 : ℝ),
      ∫⁻ x, gammaPDF (ν₁ / 2) (1 / 2) x * gammaPDF (ν₂ / 2) (1 / 2) y * φ (ratio ν₁ ν₂ (x, y)) =
        ∫⁻ r, gammaPDF (ν₂ / 2) (1 / 2) y * (ENNReal.ofReal (ν₁ / ν₂ * y) *
          gammaPDF (ν₁ / 2) (1 / 2) (ν₁ / ν₂ * y * r)) * φ r := by
    intro y (hy : 0 < y)
    rw [lintegral_comp_mul_pos (by fun_prop) (mul_pos hc hy),
      ← lintegral_const_mul' _ _ ENNReal.ofReal_ne_top]
    refine lintegral_congr fun r => ?_
    have : ratio ν₁ ν₂ (ν₁ / ν₂ * y * r, y) = r := by
      simp only [ratio]; field_simp
    simp only [this]
    ring
  rw [setLIntegral_congr_fun measurableSet_Ioi hsub]
  -- Tonelli again, `r` outside
  rw [lintegral_lintegral_swap (by fun_prop)]
  refine lintegral_congr_ae ?_
  have hne : ∀ᵐ r ∂(volume : Measure ℝ), r ≠ 0 := by
    simp [ae_iff, measure_singleton]
  filter_upwards [hne] with r hr0
  rcases lt_or_gt_of_ne hr0 with hr | hr
  · -- `r < 0`: both sides vanish
    have h0 : fPDF ν₁ ν₂ r = 0 := by simp [fPDF, fPDFReal, not_lt.2 hr.le]
    rw [h0, zero_mul]
    refine setLIntegral_eq_zero measurableSet_Ioi (fun y (hy : 0 < y) => ?_)
    have : ν₁ / ν₂ * y * r < 0 := mul_neg_of_pos_of_neg (mul_pos hc hy) hr
    simp [gammaPDF_of_neg this]
  · -- `r > 0`: the `y`-integral is the F density times a Gamma(α+β) total mass
    rw [setLIntegral_congr_fun measurableSet_Ioi
      (g := fun y => (fPDF ν₁ ν₂ r * φ r) * gammaPDF (ν₁ / 2 + ν₂ / 2) ((1 + ν₁ / ν₂ * r) / 2) y)
      (fun y (hy : 0 < y) => by simp only; rw [core_ennreal h₁ h₂ hr hy]; ring),
      lintegral_const_mul _ (measurable_gammaPDF _ _),
      setLIntegral_gammaPDF_Ioi (add_pos hα hβ) (by positivity), mul_one]

#print axioms lintegral_map_ratio

/-- **The F law (measure form).** For `ν₁, ν₂ > 0`, the pushforward of `χ²_{ν₁} ⊗ χ²_{ν₂}` under
`(x, y) ↦ (x/ν₁)/(y/ν₂)` is the F(ν₁, ν₂) law `volume.withDensity f`. -/
theorem map_ratio_chiSq_eq_fMeasure {ν₁ ν₂ : ℝ} (h₁ : 0 < ν₁) (h₂ : 0 < ν₂) :
    ((chiSq ν₁).prod (chiSq ν₂)).map (fun p => (p.1 / ν₁) / (p.2 / ν₂)) = fMeasure ν₁ ν₂ := by
  ext s hs
  have h := lintegral_map_ratio h₁ h₂ (measurable_one.indicator hs : Measurable (s.indicator 1))
  rw [lintegral_indicator_one hs] at h
  rw [show (fun p : ℝ × ℝ => (p.1 / ν₁) / (p.2 / ν₂)) = ratio ν₁ ν₂ from rfl, h, fMeasure,
    withDensity_apply _ hs, ← lintegral_indicator hs]
  refine lintegral_congr fun r => ?_
  by_cases hr : r ∈ s <;> simp [hr]

#print axioms map_ratio_chiSq_eq_fMeasure

lemma map_ratio_eq {ν₁ ν₂ : ℝ} (h₁ : 0 < ν₁) (h₂ : 0 < ν₂) :
    ((chiSq ν₁).prod (chiSq ν₂)).map (ratio ν₁ ν₂) = fMeasure ν₁ ν₂ :=
  map_ratio_chiSq_eq_fMeasure h₁ h₂

/-- The F(ν₁, ν₂) density integrates to one: `fMeasure` is a probability measure. -/
theorem isProbabilityMeasure_fMeasure {ν₁ ν₂ : ℝ} (h₁ : 0 < ν₁) (h₂ : 0 < ν₂) :
    IsProbabilityMeasure (fMeasure ν₁ ν₂) := by
  have := isProbabilityMeasure_gammaMeasure (a := ν₁ / 2) (r := 1 / 2) (by positivity)
    one_half_pos
  have := isProbabilityMeasure_gammaMeasure (a := ν₂ / 2) (r := 1 / 2) (by positivity)
    one_half_pos
  have : IsProbabilityMeasure ((chiSq ν₁).prod (chiSq ν₂)) := by
    unfold chiSq; infer_instance
  rw [← map_ratio_chiSq_eq_fMeasure h₁ h₂]
  infer_instance

#print axioms isProbabilityMeasure_fMeasure

/-- **The F law (random-variable form).** If `X ~ χ²_{ν₁}` and `Y ~ χ²_{ν₂}` are independent on a
probability space, then `(X/ν₁)/(Y/ν₂) ~ F(ν₁, ν₂)`. -/
theorem law_ratio_of_indep {Ω : Type*} [MeasurableSpace Ω] {P : Measure Ω}
    [IsProbabilityMeasure P] {X Y : Ω → ℝ} {ν₁ ν₂ : ℝ} (h₁ : 0 < ν₁) (h₂ : 0 < ν₂)
    (hX : AEMeasurable X P) (hY : AEMeasurable Y P) (hXY : IndepFun X Y P)
    (hXlaw : P.map X = chiSq ν₁) (hYlaw : P.map Y = chiSq ν₂) :
    P.map (fun ω => (X ω / ν₁) / (Y ω / ν₂)) = fMeasure ν₁ ν₂ := by
  have hjoint : P.map (fun ω => (X ω, Y ω)) = (chiSq ν₁).prod (chiSq ν₂) := by
    rw [(indepFun_iff_map_prod_eq_prod_map_map hX hY).1 hXY, hXlaw, hYlaw]
  rw [← map_ratio_eq h₁ h₂, ← hjoint,
    AEMeasurable.map_map_of_aemeasurable (measurable_ratio ν₁ ν₂).aemeasurable
      (hX.prodMk hY)]
  rfl

#print axioms law_ratio_of_indep

/-- **The F law (CDF form).** `P((X/ν₁)/(Y/ν₂) ≤ t) = ∫_{(-∞,t]} f`. -/
theorem cdf_ratio_chiSq {ν₁ ν₂ : ℝ} (h₁ : 0 < ν₁) (h₂ : 0 < ν₂) (t : ℝ) :
    ((chiSq ν₁).prod (chiSq ν₂)) {p | (p.1 / ν₁) / (p.2 / ν₂) ≤ t} =
      ∫⁻ r in Iic t, fPDF ν₁ ν₂ r := by
  rw [← withDensity_apply _ measurableSet_Iic]
  change _ = fMeasure ν₁ ν₂ (Iic t)
  rw [← map_ratio_eq h₁ h₂, Measure.map_apply (measurable_ratio ν₁ ν₂) measurableSet_Iic]
  rfl

#print axioms cdf_ratio_chiSq

/-! ### The receipt's scaled form at ν = (5, 7)

The receipt draws `R = (d₂ · χ²₅/5) / (d₃ · χ²₇/7)` and evaluates `P(R ≤ r)` as
`stats.f.cdf(r / (d₂/d₃), 5, 7)`. -/

/-- `R / (d₂/d₃) ~ F(5, 7)` exactly. -/
theorem receipt_scaled_ratio_F57 {d₂ d₃ : ℝ} (h₂ : d₂ ≠ 0) (h₃ : d₃ ≠ 0) :
    ((chiSq 5).prod (chiSq 7)).map
        (fun p => ((d₂ * (p.1 / 5)) / (d₃ * (p.2 / 7))) / (d₂ / d₃)) = fMeasure 5 7 := by
  have hk : d₂ / d₃ ≠ 0 := div_ne_zero h₂ h₃
  have hfun : (fun p : ℝ × ℝ => ((d₂ * (p.1 / 5)) / (d₃ * (p.2 / 7))) / (d₂ / d₃)) =
      fun p => (p.1 / 5) / (p.2 / 7) := by
    funext p
    rw [show (d₂ * (p.1 / 5)) / (d₃ * (p.2 / 7)) = d₂ / d₃ * ((p.1 / 5) / (p.2 / 7)) by ring,
      mul_div_cancel_left₀ _ hk]
  rw [hfun]
  exact map_ratio_chiSq_eq_fMeasure (by norm_num) (by norm_num)

#print axioms receipt_scaled_ratio_F57

/-- The law of `R` itself is the F(5,7) law scaled by `d₂/d₃`. -/
theorem receipt_law_R {d₂ d₃ : ℝ} :
    ((chiSq 5).prod (chiSq 7)).map (fun p => (d₂ * (p.1 / 5)) / (d₃ * (p.2 / 7))) =
      (fMeasure 5 7).map (fun r => d₂ / d₃ * r) := by
  rw [← map_ratio_eq (by norm_num) (by norm_num),
    Measure.map_map (measurable_const_mul _) (measurable_ratio 5 7)]
  congr 1
  funext p
  simp only [Function.comp, ratio]
  ring

#print axioms receipt_law_R

/-- The receipt's `p_exact` at `fsky = 1`: for `d₂/d₃ > 0`,
`P(R ≤ r) = F₅,₇-CDF(r / (d₂/d₃))`. -/
theorem receipt_p_exact {d₂ d₃ : ℝ} (hk : 0 < d₂ / d₃) (r : ℝ) :
    ((chiSq 5).prod (chiSq 7)) {p | (d₂ * (p.1 / 5)) / (d₃ * (p.2 / 7)) ≤ r} =
      fMeasure 5 7 (Iic (r / (d₂ / d₃))) := by
  have hpre : {p : ℝ × ℝ | (d₂ * (p.1 / 5)) / (d₃ * (p.2 / 7)) ≤ r} =
      (fun p => (d₂ * (p.1 / 5)) / (d₃ * (p.2 / 7))) ⁻¹' Iic r := rfl
  rw [hpre, ← Measure.map_apply (by fun_prop) measurableSet_Iic, receipt_law_R,
    Measure.map_apply (measurable_const_mul _) measurableSet_Iic]
  congr 1
  ext x
  simp only [mem_preimage, mem_Iic]
  rw [le_div_iff₀ hk, mul_comm]

#print axioms receipt_p_exact

end ShadowProbe.FLaw

import Mathlib

/-!
# Probe `r7741+71.2` (campaign 131): P15's horizon rows

Registration: `computations/formalisation/r7741_71_campaign131/PREDICTION.md`; inventory
`computations/formalisation/r7741_71_survey/SURVEY.md`. Nothing imports this file, and it imports only Mathlib. It is a
new standalone probe, prefix `cm_`, and later P15 campaigns append to it, so it is P15's citable file
(`corpus/CR_cosmology.tex`). `f(r) = 1 − 2M/r − r²/α²`, `Λ = 3/α²`, `G = c = 1`.

* **Row 1 — BUILT.** `cm_aH_diverges`, `cm_horizon_exit`.
* **Row 4 — BUILT.** `cm_throat`, `cm_throat_root`, `cm_throat_radii`.
* **Row 6 — BUILT.** `cm_tortoise_linear`, `cm_tortoise_double`.
* **Row 7 — BUILT.** `cm_tortoise_finite`.
* **Non-vacuity.** `cm_witness`.
-/

open Real Filter Topology Set

namespace ShadowProbe.CosmologyProbe

/-- The SdS metric function `f(r) = 1 − 2M/r − r²/α²`. -/
noncomputable def cm_f (M α r : ℝ) : ℝ := 1 - 2 * M / r - r ^ 2 / α ^ 2
/-- `f′(r) = 2M/r² − 2r/α²`. -/
noncomputable def cm_f1 (M α r : ℝ) : ℝ := 2 * M / r ^ 2 - 2 * r / α ^ 2
/-- `f″(r) = −4M/r³ − 2/α²`. -/
noncomputable def cm_f2 (M α r : ℝ) : ℝ := -4 * M / r ^ 3 - 2 / α ^ 2

lemma cm_s3 : Real.sqrt 3 ^ 2 = 3 := Real.sq_sqrt (by norm_num)

lemma cm_hasDeriv_f (M α : ℝ) {r : ℝ} (hr : r ≠ 0) : HasDerivAt (cm_f M α) (cm_f1 M α r) r := by
  have h1 : HasDerivAt (fun r : ℝ => 2 * M / r) (-(2 * M) / r ^ 2) r := by
    have := (hasDerivAt_inv hr).const_mul (2 * M)
    convert this using 1
    · funext x; ring
    · ring
  have h2 : HasDerivAt (fun r : ℝ => r ^ 2 / α ^ 2) (2 * r / α ^ 2) r := by
    convert (hasDerivAt_pow 2 r).div_const (α ^ 2) using 1; ring
  have h : HasDerivAt (fun r : ℝ => 1 - 2 * M / r - r ^ 2 / α ^ 2) (0 - -(2 * M) / r ^ 2 - 2 * r / α ^ 2) r :=
    ((hasDerivAt_const r (1 : ℝ)).sub h1).sub h2
  exact h.congr_deriv (by unfold cm_f1; ring)

lemma cm_hasDeriv_f1 (M α : ℝ) {r : ℝ} (hr : r ≠ 0) : HasDerivAt (cm_f1 M α) (cm_f2 M α r) r := by
  have h1 : HasDerivAt (fun r : ℝ => 2 * M / r ^ 2) (-(4 * M) / r ^ 3) r := by
    have := ((hasDerivAt_pow 2 r).inv (pow_ne_zero 2 hr)).const_mul (2 * M)
    convert this using 1
    · funext x; simp [div_eq_mul_inv]
    · field_simp; ring
  have h2 : HasDerivAt (fun r : ℝ => 2 * r / α ^ 2) (2 * 1 / α ^ 2) r :=
    ((hasDerivAt_id' r).const_mul 2).div_const (α ^ 2)
  have h : HasDerivAt (fun r : ℝ => 2 * M / r ^ 2 - 2 * r / α ^ 2) (-(4 * M) / r ^ 3 - 2 * 1 / α ^ 2) r :=
    h1.sub h2
  exact h.congr_deriv (by unfold cm_f2; ring)

/-! ## Row 1: the comoving Hubble scale at the branch point -/

/-- **Row 1a.** On the `E = 1` leg (`a = r`, `ṙ² = 2M/r + r²/α²`), the comoving Hubble scale `aH = ṙ` grows
without bound as `r → 0⁺`, for `M > 0`. -/
theorem cm_aH_diverges {M α : ℝ} (hM : 0 < M) :
    Tendsto (fun r : ℝ => Real.sqrt (2 * M / r + r ^ 2 / α ^ 2)) (𝓝[>] 0) atTop := by
  have h1 : Tendsto (fun r : ℝ => 2 * M / r) (𝓝[>] 0) atTop := by
    simpa [div_eq_mul_inv] using tendsto_inv_nhdsGT_zero.const_mul_atTop (by positivity : (0 : ℝ) < 2 * M)
  have h2 : Tendsto (fun r : ℝ => 2 * M / r + r ^ 2 / α ^ 2) (𝓝[>] 0) atTop :=
    tendsto_atTop_mono (fun r => le_add_of_nonneg_right (by positivity)) h1
  exact Real.tendsto_sqrt_atTop.comp h2

/-- **Row 1b.** Hence the comoving horizon `1/(aH)` closes: `k/(aH) → 0` for every wavenumber `k`. -/
theorem cm_horizon_exit {M α : ℝ} (hM : 0 < M) (k : ℝ) :
    Tendsto (fun r : ℝ => k / Real.sqrt (2 * M / r + r ^ 2 / α ^ 2)) (𝓝[>] 0) (𝓝 0) :=
  tendsto_const_nhds.div_atTop (cm_aH_diverges hM)

/-! ## Row 4: the Nariai throat -/

/-- **Row 4a.** At the Nariai mass `M = α/(3√3)` (`ΛM² = 1/9`), the radius `r_N = α/√3` has `f = f′ = 0` and
`f″ = −2Λ`, with `Λ = 3/α²`. -/
theorem cm_throat {α : ℝ} (hα : 0 < α) :
    cm_f (α / (3 * Real.sqrt 3)) α (α / Real.sqrt 3) = 0 ∧
      cm_f1 (α / (3 * Real.sqrt 3)) α (α / Real.sqrt 3) = 0 ∧
      cm_f2 (α / (3 * Real.sqrt 3)) α (α / Real.sqrt 3) = -2 * (3 / α ^ 2) ∧
      3 / α ^ 2 * (α / (3 * Real.sqrt 3)) ^ 2 = 1 / 9 := by
  have hs : 0 < Real.sqrt 3 := by positivity
  have hs3 := cm_s3
  refine ⟨?_, ?_, ?_, ?_⟩
  · unfold cm_f; field_simp; rw [hs3]; ring
  · unfold cm_f1; field_simp; ring_nf; linarith [hs3]
  · unfold cm_f2; field_simp; ring_nf; linarith [hs3]
  · field_simp; rw [hs3]; ring

/-- **Row 4a.** At the Nariai mass `f(r) = −(r − r_N)²(r + 2r_N)/(α² r)`: the two positive horizons merge at `r_N`,
which is the only positive root. -/
theorem cm_throat_root {α : ℝ} (hα : 0 < α) :
    (∀ r : ℝ, r ≠ 0 → cm_f (α / (3 * Real.sqrt 3)) α r =
        -((r - α / Real.sqrt 3) ^ 2 * (r + 2 * (α / Real.sqrt 3))) / (α ^ 2 * r)) ∧
      ∀ r : ℝ, 0 < r → cm_f (α / (3 * Real.sqrt 3)) α r = 0 → r = α / Real.sqrt 3 := by
  have hs : 0 < Real.sqrt 3 := by positivity
  have hs3 := cm_s3
  have hfac : ∀ r : ℝ, r ≠ 0 → cm_f (α / (3 * Real.sqrt 3)) α r =
      -((r - α / Real.sqrt 3) ^ 2 * (r + 2 * (α / Real.sqrt 3))) / (α ^ 2 * r) := by
    intro r hr
    unfold cm_f; field_simp
    ring_nf; rw [show Real.sqrt 3 ^ 3 = Real.sqrt 3 ^ 2 * Real.sqrt 3 by ring, hs3]; ring
  refine ⟨hfac, fun r hr h0 => ?_⟩
  rw [hfac r hr.ne'] at h0
  have hpos : 0 < r + 2 * (α / Real.sqrt 3) := by positivity
  have : (r - α / Real.sqrt 3) ^ 2 * (r + 2 * (α / Real.sqrt 3)) = 0 := by
    have hd : α ^ 2 * r ≠ 0 := by positivity
    rcases div_eq_zero_iff.1 h0 with h | h
    · exact neg_eq_zero.1 h
    · exact absurd h hd
  rcases mul_eq_zero.1 this with h | h
  · nlinarith [pow_eq_zero_iff (n := 2) (two_ne_zero) |>.1 h]
  · linarith

/-- **Row 4b.** The throat's two radii are equal: the `S²` two-Ricci is `2/r_N² = 2Λ` and the `dS₂` radius² is
`−2/f″(r_N) = 1/Λ`. -/
theorem cm_throat_radii {α : ℝ} (hα : 0 < α) :
    2 / (α / Real.sqrt 3) ^ 2 = 2 * (3 / α ^ 2) ∧
      -2 / cm_f2 (α / (3 * Real.sqrt 3)) α (α / Real.sqrt 3) = 1 / (3 / α ^ 2) ∧
      (α / Real.sqrt 3) ^ 2 = 1 / (3 / α ^ 2) := by
  have hs : 0 < Real.sqrt 3 := by positivity
  refine ⟨?_, ?_, ?_⟩
  · field_simp; rw [cm_s3]
  · rw [(cm_throat hα).2.2.1]; field_simp
  · field_simp; rw [cm_s3]

/-! ## Row 6: the tortoise dichotomy -/

/-- **Row 6a, `p = 1`.** Near a non-degenerate horizon, `f = 2κ(x − x_h)` with `κ > 0`: the tortoise coordinate
`r* = ln(x − x_h)/(2κ)` has `dr*/dx = 1/f`, the approach is exponential, `x − x_h = e^{2κ r*}`, and `r* → −∞` as
`x → x_h⁺` (logarithmically). -/
theorem cm_tortoise_linear {κ xh : ℝ} (hκ : 0 < κ) :
    (∀ x, xh < x → HasDerivAt (fun x => Real.log (x - xh) / (2 * κ)) (1 / (2 * κ * (x - xh))) x) ∧
      (∀ x, xh < x → x - xh = Real.exp (2 * κ * (Real.log (x - xh) / (2 * κ)))) ∧
      Tendsto (fun x => Real.log (x - xh) / (2 * κ)) (𝓝[>] xh) atBot := by
  refine ⟨fun x hx => ?_, fun x hx => ?_, ?_⟩
  · have h : HasDerivAt (fun y => Real.log (y - xh)) (1 / (x - xh)) x :=
      ((hasDerivAt_id' x).sub_const xh).log (sub_pos.2 hx).ne'
    exact (h.div_const (2 * κ)).congr_deriv (by field_simp)
  · rw [mul_div_cancel₀ _ (by positivity), Real.exp_log (sub_pos.2 hx)]
  · have h0 : Tendsto (fun x => x - xh) (𝓝[>] xh) (𝓝[>] 0) := by
      refine tendsto_nhdsWithin_of_tendsto_nhds_of_eventually_within _ ?_ ?_
      · have hc : Continuous (fun x : ℝ => x - xh) := by fun_prop
        simpa using (hc.tendsto xh).mono_left (nhdsWithin_le_nhds (s := Ioi xh))
      · filter_upwards [self_mem_nhdsWithin] with x (hx : xh < x) using sub_pos.2 hx
    exact (Real.tendsto_log_nhdsGT_zero.comp h0).atBot_div_const (by positivity)

/-- **Row 6b, `p = 2`.** At the degenerate Nariai double root, `f = −Λ(x − x_N)²`: the tortoise coordinate
`r* = 1/(Λ(x − x_N))` has `dr*/dx = 1/f`, the approach is a power law, `x − x_N = 1/(Λ r*)`, and `r* → +∞` as
`x → x_N⁺` (as a power, not a logarithm). -/
theorem cm_tortoise_double {Λ xN : ℝ} (hΛ : 0 < Λ) :
    (∀ x, x ≠ xN → HasDerivAt (fun x => 1 / (Λ * (x - xN))) (1 / (-Λ * (x - xN) ^ 2)) x) ∧
      (∀ x, x ≠ xN → x - xN = 1 / (Λ * (1 / (Λ * (x - xN))))) ∧
      Tendsto (fun x => 1 / (Λ * (x - xN))) (𝓝[>] xN) atTop := by
  refine ⟨fun x hx => ?_, fun x hx => ?_, ?_⟩
  · have hx' : x - xN ≠ 0 := sub_ne_zero.2 hx
    have h := (((hasDerivAt_id x).sub_const xN).const_mul Λ).inv (mul_ne_zero hΛ.ne' hx')
    convert h using 1
    · funext y; simp [one_div]
    · simp; field_simp
  · have hx' : x - xN ≠ 0 := sub_ne_zero.2 hx
    field_simp
  · have h0 : Tendsto (fun x => Λ * (x - xN)) (𝓝[>] xN) (𝓝[>] 0) := by
      refine tendsto_nhdsWithin_of_tendsto_nhds_of_eventually_within _ ?_ ?_
      · have hc : Continuous (fun x : ℝ => Λ * (x - xN)) := by fun_prop
        simpa using (hc.tendsto xN).mono_left (nhdsWithin_le_nhds (s := Ioi xN))
      · filter_upwards [self_mem_nhdsWithin] with x (hx : xN < x) using mul_pos hΛ (sub_pos.2 hx)
    refine (tendsto_inv_nhdsGT_zero.comp h0).congr fun x => ?_
    simp [one_div]

/-! ## Row 7: the finite tortoise length at the branch point -/

/-- `1/f` near the branch point, written without `1/r`: `g(r) = r/(r − 2M − r³/α²)`. -/
noncomputable def cm_g (M α r : ℝ) : ℝ := r / (r - 2 * M - r ^ 3 / α ^ 2)

lemma cm_den_neg {M α r : ℝ} (h0 : 0 ≤ r) (hr : r ≤ M) :
    r - 2 * M - r ^ 3 / α ^ 2 ≤ -M := by
  have : 0 ≤ r ^ 3 / α ^ 2 := by positivity
  linarith

lemma cm_inv_f_eq {M α r : ℝ} (hM : 0 < M) (h0 : 0 < r) (hr : r ≤ M) (hα : α ≠ 0) :
    1 / cm_f M α r = cm_g M α r := by
  have hd := cm_den_neg (α := α) h0.le hr
  have hd' : r - 2 * M - r ^ 3 / α ^ 2 ≠ 0 := by linarith
  unfold cm_f cm_g
  rw [show 1 - 2 * M / r - r ^ 2 / α ^ 2 = (r - 2 * M - r ^ 3 / α ^ 2) / r by field_simp]
  rw [one_div_div]

/-- **Row 7.** At the branch point `f ~ −2M/r` diverges, so `1/f → 0` as `r → 0⁺`; on `(0, ε]` with `ε ≤ M` it is
bounded by `ε/M` and agrees with the continuous `r/(r − 2M − r³/α²)`, so it is integrable on `[0, ε]`: the tortoise
length `r* = ∫₀^ε dr/f` is finite. -/
theorem cm_tortoise_finite {M α ε : ℝ} (hM : 0 < M) (hα : α ≠ 0) (hε : 0 < ε) (hεM : ε ≤ M) :
    Tendsto (fun r => 1 / cm_f M α r) (𝓝[>] 0) (𝓝 0) ∧
      (∀ r ∈ Ioc 0 ε, |1 / cm_f M α r| ≤ ε / M) ∧
      IntervalIntegrable (fun r => 1 / cm_f M α r) MeasureTheory.volume 0 ε := by
  have hcont : ContinuousOn (cm_g M α) (Icc 0 ε) := by
    refine ContinuousOn.div continuousOn_id (by fun_prop) fun r hr => ?_
    have := cm_den_neg (α := α) hr.1 (hr.2.trans hεM); linarith
  refine ⟨?_, ?_, ?_⟩
  · have hg : Tendsto (cm_g M α) (𝓝 0) (𝓝 (cm_g M α 0)) := by
      refine ContinuousAt.tendsto ?_
      refine ContinuousAt.div continuousAt_id (by fun_prop) ?_
      simp; exact hM.ne'
    have hg0 : cm_g M α 0 = 0 := by simp [cm_g]
    rw [hg0] at hg
    refine (hg.mono_left nhdsWithin_le_nhds).congr' ?_
    filter_upwards [Ioo_mem_nhdsGT hM] with r hr
    exact (cm_inv_f_eq hM hr.1 hr.2.le hα).symm
  · intro r hr
    rw [cm_inv_f_eq hM hr.1 (hr.2.trans hεM) hα, cm_g, abs_div, abs_of_pos hr.1]
    have hd := cm_den_neg (α := α) hr.1.le (hr.2.trans hεM)
    rw [abs_of_neg (by linarith), div_le_div_iff₀ (by linarith) hM]
    nlinarith [hr.2]
  · have hI : IntervalIntegrable (cm_g M α) MeasureTheory.volume 0 ε :=
      hcont.intervalIntegrable_of_Icc hε.le
    rw [intervalIntegrable_iff_integrableOn_Ioc_of_le hε.le] at hI ⊢
    refine hI.congr_fun (fun r hr => ?_) measurableSet_Ioc
    exact (cm_inv_f_eq hM hr.1 (hr.2.trans hεM) hα).symm

/-- **Non-vacuity.** The throat at `α = 3` (`r_N = √3`, `M = 1/√3`), the two tortoise laws at `κ = Λ = 1`, and the
finite tortoise length at `M = 1`, `α = 3`, `ε = 1`. -/
theorem cm_witness :
    cm_f (3 / (3 * Real.sqrt 3)) 3 (3 / Real.sqrt 3) = 0 ∧
      Real.exp (2 * 1 * (Real.log (2 - 1) / (2 * 1))) = 2 - 1 ∧
      IntervalIntegrable (fun r => 1 / cm_f 1 3 r) MeasureTheory.volume 0 1 := by
  refine ⟨(cm_throat (by norm_num)).1, ?_, (cm_tortoise_finite one_pos (by norm_num) one_pos le_rfl).2.2⟩
  norm_num

end ShadowProbe.CosmologyProbe

#print axioms ShadowProbe.CosmologyProbe.cm_hasDeriv_f
#print axioms ShadowProbe.CosmologyProbe.cm_hasDeriv_f1
#print axioms ShadowProbe.CosmologyProbe.cm_aH_diverges
#print axioms ShadowProbe.CosmologyProbe.cm_horizon_exit
#print axioms ShadowProbe.CosmologyProbe.cm_throat
#print axioms ShadowProbe.CosmologyProbe.cm_throat_root
#print axioms ShadowProbe.CosmologyProbe.cm_throat_radii
#print axioms ShadowProbe.CosmologyProbe.cm_tortoise_linear
#print axioms ShadowProbe.CosmologyProbe.cm_tortoise_double
#print axioms ShadowProbe.CosmologyProbe.cm_tortoise_finite
#print axioms ShadowProbe.CosmologyProbe.cm_witness

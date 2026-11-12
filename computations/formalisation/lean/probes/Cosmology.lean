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

**Campaign 132 (`r7743+71.2`), in this same file.** Registration:
`computations/formalisation/r7743_71_campaign132/PREDICTION.md`. `StaticEinstein.lean`'s `KrCurvature` and `LfLeaves`
are copied verbatim below (namespace `ShadowProbe.StaticEinsteinProbe`, names kept).
* **Row 2 — BUILT.** `cm_substrate_ratio`.
* **Row 3 — BUILT.** `cm_mass_cap`, `cm_progenitor_arith`.
* **Row 5 — BUILT.** `cm_flat_slice` (with the copied `lf_curv`), `cm_flat_witness`.
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

/-! ## Campaign 132: rows 2, 3 and 5

`StaticEinstein.lean`'s sections `KrCurvature` and `LfLeaves` are copied verbatim below (namespace
`ShadowProbe.StaticEinsteinProbe`, every name kept), so P15's names stay in one file. -/

section LfCopy
open Set Filter Topology
namespace ShadowProbe.StaticEinsteinProbe

section KrCurvature

variable {n : ℕ}

/-- The classical partial derivative `∂_c f(x)`: the derivative of `f` along the `c`-th coordinate line. -/
noncomputable def kr_pd (f : (Fin n → ℝ) → ℝ) (x : Fin n → ℝ) (c : Fin n) : ℝ :=
  deriv (fun t => f (Function.update x c t)) (x c)

/-- Christoffel symbols `Γ^a_{bc} = ½ g^{ad}(∂_b g_{dc} + ∂_c g_{db} − ∂_d g_{bc})`. -/
noncomputable def kr_Γ (g : (Fin n → ℝ) → Matrix (Fin n) (Fin n) ℝ) (x : Fin n → ℝ)
    (a b c : Fin n) : ℝ :=
  (1 / 2 : ℝ) * ∑ d, (g x)⁻¹ a d *
    (kr_pd (fun y => g y d c) x b + kr_pd (fun y => g y d b) x c - kr_pd (fun y => g y b c) x d)

/-- Riemann `R^a_{bcd} = ∂_c Γ^a_{db} − ∂_d Γ^a_{cb} + Γ^a_{ce}Γ^e_{db} − Γ^a_{de}Γ^e_{cb}`. -/
noncomputable def kr_Riem (g : (Fin n → ℝ) → Matrix (Fin n) (Fin n) ℝ) (x : Fin n → ℝ)
    (a b c d : Fin n) : ℝ :=
  kr_pd (fun y => kr_Γ g y a d b) x c - kr_pd (fun y => kr_Γ g y a c b) x d +
    ∑ e, (kr_Γ g x a c e * kr_Γ g x e d b - kr_Γ g x a d e * kr_Γ g x e c b)

/-- `R_{abcd} = g_{ae} R^e_{bcd}`. -/
noncomputable def kr_Rlow (g : (Fin n → ℝ) → Matrix (Fin n) (Fin n) ℝ) (x : Fin n → ℝ)
    (a b c d : Fin n) : ℝ :=
  ∑ e, g x a e * kr_Riem g x e b c d

/-- `R^{abcd} = g^{bb'} g^{cc'} g^{dd'} R^a_{b'c'd'}`. -/
noncomputable def kr_Rup (g : (Fin n → ℝ) → Matrix (Fin n) (Fin n) ℝ) (x : Fin n → ℝ)
    (a b c d : Fin n) : ℝ :=
  ∑ b', (g x)⁻¹ b b' * ∑ c', (g x)⁻¹ c c' * ∑ d', (g x)⁻¹ d d' * kr_Riem g x a b' c' d'

/-- **The Kretschmann scalar** `K = R_{abcd} R^{abcd}`. -/
noncomputable def kr_K (g : (Fin n → ℝ) → Matrix (Fin n) (Fin n) ℝ) (x : Fin n → ℝ) : ℝ :=
  ∑ a, ∑ b, ∑ c, ∑ d, kr_Rlow g x a b c d * kr_Rup g x a b c d

lemma kr_pd_const (C : ℝ) (x : Fin n → ℝ) (c : Fin n) : kr_pd (fun _ => C) x c = 0 := by
  simp [kr_pd]

lemma kr_pd_congr {f f' : (Fin n → ℝ) → ℝ} {x : Fin n → ℝ} {c : Fin n}
    (h : ∀ᶠ y in 𝓝 x, f y = f' y) : kr_pd f x c = kr_pd f' x c := by
  unfold kr_pd
  refine Filter.EventuallyEq.deriv_eq ?_
  have hc : ContinuousAt (fun t => Function.update x c t) (x c) :=
    (continuous_const.update c continuous_id).continuousAt
  have h' : ∀ᶠ y in 𝓝 (Function.update x c (x c)), f y = f' y := by
    rwa [Function.update_eq_self]
  exact hc.eventually h'

/-- **Sanity ①: a constant metric is flat**, `K = 0`. -/
theorem kr_K_const (G : Matrix (Fin n) (Fin n) ℝ) (x : Fin n → ℝ) : kr_K (fun _ => G) x = 0 := by
  have hΓ : ∀ y a b c, kr_Γ (fun _ => G) y a b c = 0 := by
    intro y a b c; simp [kr_Γ, kr_pd_const]
  have hR : ∀ a b c d, kr_Riem (fun _ => G) x a b c d = 0 := by
    intro a b c d; simp [kr_Riem, hΓ, kr_pd_const]
  simp [kr_K, kr_Rlow, hR]

section KrTrig

/-- `sin² θ`. -/
noncomputable def kr_s2 (t : ℝ) : ℝ := Real.sin t ^ 2
/-- `−sin θ cos θ`. -/
noncomputable def kr_nsc (t : ℝ) : ℝ := -(Real.sin t * Real.cos t)
/-- `cot θ = cos θ / sin θ`. -/
noncomputable def kr_cot (t : ℝ) : ℝ := Real.cos t / Real.sin t

lemma kr_hasDerivAt_s2 (t : ℝ) :
    HasDerivAt kr_s2 (2 * Real.sin t * Real.cos t) t := by
  have h := (Real.hasDerivAt_sin t).pow 2
  unfold kr_s2
  convert h using 1; push_cast; ring

lemma kr_deriv_s2 (t : ℝ) : deriv kr_s2 t = 2 * Real.sin t * Real.cos t :=
  (kr_hasDerivAt_s2 t).deriv

lemma kr_deriv_nsc (t : ℝ) :
    deriv kr_nsc t = Real.sin t ^ 2 - Real.cos t ^ 2 := by
  have h := ((Real.hasDerivAt_sin t).mul (Real.hasDerivAt_cos t)).neg
  refine (h.congr_deriv ?_).deriv
  ring

lemma kr_deriv_cot {t : ℝ} (ht : Real.sin t ≠ 0) :
    deriv kr_cot t = -(1 / Real.sin t ^ 2) := by
  have h := (Real.hasDerivAt_cos t).div (Real.hasDerivAt_sin t) ht
  refine (h.congr_deriv ?_).deriv
  field_simp
  have := Real.sin_sq_add_cos_sq t
  linear_combination (-1 : ℝ) * this

end KrTrig

end KrCurvature

section LfLeaves
open Real

/-- The warped metric `R²(dχ² + S(χ)²(dθ² + sin²θ dφ²))` on `(χ, θ, φ)`. -/
noncomputable def lf_g (R : ℝ) (S : ℝ → ℝ) (y : Fin 3 → ℝ) : Matrix (Fin 3) (Fin 3) ℝ :=
  Matrix.diagonal ![R ^ 2, R ^ 2 * S (y 0) ^ 2, R ^ 2 * S (y 0) ^ 2 * kr_s2 (y 1)]

noncomputable def lf_c1 (S D : ℝ → ℝ) (t : ℝ) : ℝ := -(S t * D t)
noncomputable def lf_c2 (S D : ℝ → ℝ) (t : ℝ) : ℝ := D t / S t

/-- The Christoffel table of `lf_g`. -/
noncomputable def lf_T (S D : ℝ → ℝ) (y : Fin 3 → ℝ) : Fin 3 → Fin 3 → Fin 3 → ℝ :=
  ![![![0, 0, 0], ![0, lf_c1 S D (y 0), 0], ![0, 0, lf_c1 S D (y 0) * kr_s2 (y 1)]],
    ![![0, lf_c2 S D (y 0), 0], ![lf_c2 S D (y 0), 0, 0], ![0, 0, kr_nsc (y 1)]],
    ![![0, 0, lf_c2 S D (y 0)], ![0, 0, kr_cot (y 1)], ![lf_c2 S D (y 0), kr_cot (y 1), 0]]]

variable {R k : ℝ} {S D : ℝ → ℝ}

lemma lf_g_inv {y : Fin 3 → ℝ} (hR : R ≠ 0) (hS : S (y 0) ≠ 0) (hs : Real.sin (y 1) ≠ 0) :
    (lf_g R S y)⁻¹ = Matrix.diagonal ![(R ^ 2)⁻¹, (R ^ 2 * S (y 0) ^ 2)⁻¹,
      (R ^ 2 * S (y 0) ^ 2 * kr_s2 (y 1))⁻¹] := by
  refine Matrix.inv_eq_left_inv ?_
  rw [lf_g, Matrix.diagonal_mul_diagonal, ← Matrix.diagonal_one]
  congr 1; ext i; fin_cases i <;> simp [kr_s2] <;> field_simp

lemma lf_Γ (hSd : ∀ t, HasDerivAt S (D t) t) {y : Fin 3 → ℝ} (hR : R ≠ 0) (hS : S (y 0) ≠ 0)
    (hs : Real.sin (y 1) ≠ 0) (a b c : Fin 3) :
    kr_Γ (lf_g R S) y a b c = lf_T S D y a b c := by
  have h0 : HasDerivAt (fun t => S t ^ 2) (2 * S (y 0) * D (y 0)) (y 0) := by
    have h' : HasDerivAt (fun t => S t * S t) (D (y 0) * S (y 0) + S (y 0) * D (y 0)) (y 0) :=
      (hSd (y 0)).mul (hSd (y 0))
    convert h' using 1
    · funext t; ring
    · ring
  have d1 : deriv (fun t => R ^ 2 * S t ^ 2) (y 0) = R ^ 2 * (2 * S (y 0) * D (y 0)) :=
    (h0.const_mul (R ^ 2)).deriv
  have d2 : deriv (fun t => R ^ 2 * S t ^ 2 * kr_s2 (y 1)) (y 0) =
      R ^ 2 * (2 * S (y 0) * D (y 0)) * kr_s2 (y 1) :=
    ((h0.const_mul (R ^ 2)).mul_const (kr_s2 (y 1))).deriv
  have d3 : deriv (fun t => R ^ 2 * S (y 0) ^ 2 * kr_s2 t) (y 1) =
      R ^ 2 * S (y 0) ^ 2 * (2 * Real.sin (y 1) * Real.cos (y 1)) :=
    ((kr_hasDerivAt_s2 (y 1)).const_mul _).deriv
  have d0 := h0.deriv
  simp only [kr_Γ, lf_g_inv hR hS hs]
  fin_cases a <;> fin_cases b <;> fin_cases c <;>
    simp [kr_pd, lf_g, lf_T, Function.update_apply, Matrix.diagonal_apply, d0, d1, d2, d3,
      lf_c1, lf_c2, kr_nsc, kr_cot]
  all_goals (try simp only [kr_s2])
  all_goals field_simp

/-- The data at the point: `S′ = D`, `D′ = −kS` everywhere, `S′² + kS² = 1`, `R ≠ 0`, `S(χ) ≠ 0`, `sin θ ≠ 0`. -/
structure lf_Hyp (R k : ℝ) (S D : ℝ → ℝ) (x : Fin 3 → ℝ) : Prop where
  hSd : ∀ t, HasDerivAt S (D t) t
  hDd : ∀ t, HasDerivAt D (-(k * S t)) t
  hid : D (x 0) ^ 2 + k * S (x 0) ^ 2 = 1
  hR : R ≠ 0
  hS : S (x 0) ≠ 0
  hs : Real.sin (x 1) ≠ 0

variable {x : Fin 3 → ℝ}

lemma lf_Hyp.U (h : lf_Hyp R k S D x) : ∀ᶠ y in 𝓝 x, S (y 0) ≠ 0 ∧ Real.sin (y 1) ≠ 0 := by
  have c0 : ContinuousAt (fun y : Fin 3 → ℝ => y 0) x := (continuous_apply 0).continuousAt
  have c1 : ContinuousAt (fun y : Fin 3 → ℝ => y 1) x := (continuous_apply 1).continuousAt
  filter_upwards [(ContinuousAt.comp (f := fun y : Fin 3 → ℝ => y 0)
      (h.hSd (x 0)).continuousAt c0).eventually_ne h.hS,
    (ContinuousAt.comp (f := fun y : Fin 3 → ℝ => y 1) Real.continuous_sin.continuousAt c1).eventually_ne h.hs]
    with y h1 h2
  exact ⟨h1, h2⟩

lemma lf_pd (h : lf_Hyp R k S D x) (a b c d : Fin 3) :
    kr_pd (fun y => kr_Γ (lf_g R S) y a b c) x d = kr_pd (fun y => lf_T S D y a b c) x d :=
  kr_pd_congr (h.U.mono fun _ hy => lf_Γ h.hSd h.hR hy.1 hy.2 a b c)

/-- **Constant curvature `k/R²`.** `R_{abcd} = (k/R²)(g_ac g_bd − g_ad g_bc)` for the warped metric
`R²(dχ² + S(χ)² dΩ²)` whenever `S″ = −kS` and `S′² + kS² = 1`. -/
theorem lf_curv (h : lf_Hyp R k S D x) (a b c d : Fin 3) :
    kr_Rlow (lf_g R S) x a b c d = k / R ^ 2 *
      (lf_g R S x a c * lf_g R S x b d - lf_g R S x a d * lf_g R S x b c) := by
  have hΓ := lf_Γ (D := D) h.hSd h.hR h.hS h.hs
  have hR := h.hR; have hS := h.hS; have hs := h.hs
  have e1 : deriv (lf_c1 S D) (x 0) = -(D (x 0) ^ 2 - k * S (x 0) ^ 2) := by
    have h' : HasDerivAt (fun t => -(S t * D t)) (-(D (x 0) * D (x 0) + S (x 0) * -(k * S (x 0)))) (x 0) :=
      ((h.hSd (x 0)).mul (h.hDd (x 0))).neg
    rw [show lf_c1 S D = fun t => -(S t * D t) from rfl, h'.deriv]; ring
  have e1s : deriv (fun t => lf_c1 S D t * kr_s2 (x 1)) (x 0) =
      -(D (x 0) ^ 2 - k * S (x 0) ^ 2) * kr_s2 (x 1) := by
    have h' : HasDerivAt (fun t => -(S t * D t) * kr_s2 (x 1))
        (-(D (x 0) * D (x 0) + S (x 0) * -(k * S (x 0))) * kr_s2 (x 1)) (x 0) :=
      (((h.hSd (x 0)).mul (h.hDd (x 0))).neg).mul_const (kr_s2 (x 1))
    rw [show (fun t => lf_c1 S D t * kr_s2 (x 1)) = fun t => -(S t * D t) * kr_s2 (x 1) from rfl, h'.deriv]
    ring
  have e1t : deriv (fun t => lf_c1 S D (x 0) * kr_s2 t) (x 1) =
      lf_c1 S D (x 0) * (2 * Real.sin (x 1) * Real.cos (x 1)) :=
    ((kr_hasDerivAt_s2 (x 1)).const_mul _).deriv
  have e2 : deriv (lf_c2 S D) (x 0) = (-(k * S (x 0)) * S (x 0) - D (x 0) * D (x 0)) / S (x 0) ^ 2 := by
    have h' : HasDerivAt (fun t => D t / S t)
        ((-(k * S (x 0)) * S (x 0) - D (x 0) * D (x 0)) / S (x 0) ^ 2) (x 0) :=
      (h.hDd (x 0)).div (h.hSd (x 0)) hS
    rw [show lf_c2 S D = fun t => D t / S t from rfl, h'.deriv]
  have en := kr_deriv_nsc (x 1)
  have ec := kr_deriv_cot hs
  have hk : k = (1 - D (x 0) ^ 2) / S (x 0) ^ 2 := by
    field_simp; linear_combination h.hid
  unfold kr_Rlow kr_Riem
  simp only [Fin.sum_univ_three, lf_pd h, hΓ]
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases d <;>
  · simp [lf_T, lf_g, kr_pd, e1, e1s, e1t, e2, en, ec]
    all_goals (try simp only [lf_c1, lf_c2, kr_nsc, kr_cot, kr_s2])
    all_goals (try rw [hk])
    all_goals (try field_simp)
    all_goals (try simp only [Real.cos_sq'])
    all_goals (try ring1)
    all_goals (try simp)
    all_goals (try norm_num)

/-- The substrate's quadratic form `η(X, X) = −X₀² + X₁² + X₂² + X₃² + X₄²`. -/
def lf_η (X : Fin 5 → ℝ) : ℝ := -X 0 ^ 2 + X 1 ^ 2 + X 2 ^ 2 + X 3 ^ 2 + X 4 ^ 2

/-- The signature `ε = (−1, 1, 1, 1, 1)`. -/
def lf_ε : Fin 5 → ℝ := ![-1, 1, 1, 1, 1]

/-- The induced metric `g_ij = Σ_A ε_A ∂_iΦ^A ∂_jΦ^A` of a chart `Φ`. -/
noncomputable def lf_pull (Φ : (Fin 3 → ℝ) → Fin 5 → ℝ) (x : Fin 3 → ℝ) : Matrix (Fin 3) (Fin 3) ℝ :=
  Matrix.of fun i j => ∑ A, lf_ε A * kr_pd (fun y => Φ y A) x i * kr_pd (fun y => Φ y A) x j

lemma lf_pd3 {F G H : ℝ → ℝ} {F' G' H' : ℝ} {x : Fin 3 → ℝ} (hF : HasDerivAt F F' (x 0))
    (hG : HasDerivAt G G' (x 1)) (hH : HasDerivAt H H' (x 2)) (c : Fin 3) :
    kr_pd (fun y => F (y 0) * G (y 1) * H (y 2)) x c =
      ![F' * G (x 1) * H (x 2), F (x 0) * G' * H (x 2), F (x 0) * G (x 1) * H'] c := by
  fin_cases c <;> simp [kr_pd]
  · exact Or.inl (Or.inl hF.deriv)
  · exact Or.inl (Or.inl hG.deriv)
  · exact Or.inl hH.deriv

/-- The chart `(U₀(χ), U₁(χ), R S(χ) n̂(θ, φ))`. -/
noncomputable def lf_Φ (U0 U1 : ℝ → ℝ) (R : ℝ) (S : ℝ → ℝ) (y : Fin 3 → ℝ) : Fin 5 → ℝ :=
  ![U0 (y 0), U1 (y 0), R * S (y 0) * Real.cos (y 1), R * S (y 0) * Real.sin (y 1) * Real.cos (y 2),
    R * S (y 0) * Real.sin (y 1) * Real.sin (y 2)]

/-- **The induced metric of the chart** is `diag(−U₀′² + U₁′² + R²S′², R²S², R²S² sin²θ)`. -/
theorem lf_pull_eq {U0 U1 S V0 V1 D : ℝ → ℝ} {R : ℝ} (h0 : ∀ t, HasDerivAt U0 (V0 t) t)
    (h1 : ∀ t, HasDerivAt U1 (V1 t) t) (hS : ∀ t, HasDerivAt S (D t) t) (x : Fin 3 → ℝ) :
    lf_pull (lf_Φ U0 U1 R S) x = Matrix.diagonal ![-V0 (x 0) ^ 2 + V1 (x 0) ^ 2 + R ^ 2 * D (x 0) ^ 2,
      R ^ 2 * S (x 0) ^ 2, R ^ 2 * S (x 0) ^ 2 * kr_s2 (x 1)] := by
  have one : ∀ t : ℝ, HasDerivAt (fun _ : ℝ => (1 : ℝ)) 0 t := fun t => hasDerivAt_const t 1
  have hRS : HasDerivAt (fun t => R * S t) (R * D (x 0)) (x 0) := (hS (x 0)).const_mul R
  have p0 : ∀ c, kr_pd (fun y => lf_Φ U0 U1 R S y 0) x c = ![V0 (x 0), 0, 0] c := fun c => by
    have := lf_pd3 (x := x) (h0 (x 0)) (one (x 1)) (one (x 2)) c
    simp only [mul_one, mul_zero] at this; simpa [lf_Φ] using this
  have p1 : ∀ c, kr_pd (fun y => lf_Φ U0 U1 R S y 1) x c = ![V1 (x 0), 0, 0] c := fun c => by
    have := lf_pd3 (x := x) (h1 (x 0)) (one (x 1)) (one (x 2)) c
    simp only [mul_one, mul_zero] at this; simpa [lf_Φ] using this
  have p2 : ∀ c, kr_pd (fun y => lf_Φ U0 U1 R S y 2) x c =
      ![R * D (x 0) * Real.cos (x 1), -(R * S (x 0) * Real.sin (x 1)), 0] c := fun c => by
    have := lf_pd3 (x := x) hRS (Real.hasDerivAt_cos (x 1)) (one (x 2)) c
    simp only [mul_one, mul_zero] at this; simpa [lf_Φ] using this
  have p3 : ∀ c, kr_pd (fun y => lf_Φ U0 U1 R S y 3) x c =
      ![R * D (x 0) * Real.sin (x 1) * Real.cos (x 2), R * S (x 0) * Real.cos (x 1) * Real.cos (x 2),
        R * S (x 0) * Real.sin (x 1) * -Real.sin (x 2)] c := fun c => by
    have := lf_pd3 (x := x) hRS (Real.hasDerivAt_sin (x 1)) (Real.hasDerivAt_cos (x 2)) c
    simpa [lf_Φ] using this
  have p4 : ∀ c, kr_pd (fun y => lf_Φ U0 U1 R S y 4) x c =
      ![R * D (x 0) * Real.sin (x 1) * Real.sin (x 2), R * S (x 0) * Real.cos (x 1) * Real.sin (x 2),
        R * S (x 0) * Real.sin (x 1) * Real.cos (x 2)] c := fun c => by
    have := lf_pd3 (x := x) hRS (Real.hasDerivAt_sin (x 1)) (Real.hasDerivAt_sin (x 2)) c
    simpa [lf_Φ] using this
  ext i j
  simp only [lf_pull, Matrix.of_apply, Fin.sum_univ_five, p0, p1, p2, p3, p4]
  fin_cases i <;> fin_cases j <;> simp [lf_ε, kr_s2]
  all_goals (try ring_nf)
  all_goals (try simp only [Real.cos_sq'])
  all_goals ring1

/-! #### The three leaves -/

/-- **Row 5a, the set.** On the hyperboloid, `X₀ = c` is the sphere `X₁² + … + X₄² = α² + c²`. -/
theorem lf_closed_set (α c : ℝ) (X : Fin 5 → ℝ) :
    (lf_η X = α ^ 2 ∧ X 0 = c) ↔ (X 0 = c ∧ X 1 ^ 2 + X 2 ^ 2 + X 3 ^ 2 + X 4 ^ 2 = α ^ 2 + c ^ 2) := by
  unfold lf_η
  constructor
  · rintro ⟨h, rfl⟩; exact ⟨rfl, by linarith⟩
  · rintro ⟨rfl, h⟩; exact ⟨by linarith, rfl⟩

/-- The closed chart `(c, R cos χ, R sin χ n̂(θ, φ))`. -/
noncomputable def lf_S3 (c R : ℝ) : (Fin 3 → ℝ) → Fin 5 → ℝ :=
  lf_Φ (fun _ => c) (fun t => R * Real.cos t) R Real.sin

theorem lf_S3_on {α c R : ℝ} (hR : R ^ 2 = α ^ 2 + c ^ 2) (y : Fin 3 → ℝ) :
    lf_η (lf_S3 c R y) = α ^ 2 ∧ lf_S3 c R y 0 = c := by
  refine ⟨?_, by simp [lf_S3, lf_Φ]⟩
  simp [lf_η, lf_S3, lf_Φ]
  ring_nf; simp only [Real.cos_sq']; linear_combination hR

theorem lf_S3_pull (c R : ℝ) : lf_pull (lf_S3 c R) = lf_g R Real.sin := by
  funext y
  rw [lf_S3, lf_pull_eq (V0 := fun _ => 0) (V1 := fun t => R * -Real.sin t) (D := Real.cos)
    (fun t => hasDerivAt_const t c) (fun t => (Real.hasDerivAt_cos t).const_mul R) Real.hasDerivAt_sin y, lf_g]
  congr 1; ext i; fin_cases i <;> simp
  ring_nf; simp only [Real.cos_sq']; ring

/-- **Row 5a.** The closed leaf `X₀ = c` is a round `S³` of curvature `+1/(α² + c²)`: its induced metric has
`R_{abcd} = (1/(α² + c²))(g_ac g_bd − g_ad g_bc)`. -/
theorem lf_closed {α c R : ℝ} (hR0 : R ≠ 0) (hR : R ^ 2 = α ^ 2 + c ^ 2) {x : Fin 3 → ℝ}
    (h0 : Real.sin (x 0) ≠ 0) (h1 : Real.sin (x 1) ≠ 0) (i j k l : Fin 3) :
    kr_Rlow (lf_pull (lf_S3 c R)) x i j k l = 1 / (α ^ 2 + c ^ 2) *
      (lf_pull (lf_S3 c R) x i k * lf_pull (lf_S3 c R) x j l -
        lf_pull (lf_S3 c R) x i l * lf_pull (lf_S3 c R) x j k) := by
  rw [lf_S3_pull, ← hR, show (1 : ℝ) / R ^ 2 = 1 / R ^ 2 from rfl]
  have := lf_curv (R := R) (k := 1) (S := Real.sin) (D := Real.cos) (x := x)
    ⟨Real.hasDerivAt_sin, fun t => by simpa using Real.hasDerivAt_cos t,
      by rw [one_mul]; exact Real.cos_sq_add_sin_sq _, hR0, h0, h1⟩ i j k l
  exact this

/-- **Row 5c, the set.** On the hyperboloid, `X₁ = b` gives `X₀² − (X₂² + X₃² + X₄²) = b² − α²`; beyond the
throat (`0 ≤ α < b`) every point has `X₀ ≠ 0`, so the section has two sheets, `X₀ > 0` and `X₀ < 0`. -/
theorem lf_open_set {α b : ℝ} {X : Fin 5 → ℝ} (h : lf_η X = α ^ 2) (hb : X 1 = b) :
    X 0 ^ 2 - (X 2 ^ 2 + X 3 ^ 2 + X 4 ^ 2) = b ^ 2 - α ^ 2 ∧ (0 ≤ α → α < b → X 0 ≠ 0) := by
  unfold lf_η at h; subst hb
  refine ⟨by linarith, fun hα hαb h0 => ?_⟩
  rw [h0] at h
  nlinarith [sq_nonneg (X 2), sq_nonneg (X 3), sq_nonneg (X 4)]

/-- The open chart `(A cosh ρ, b, A sinh ρ n̂(θ, φ))`. -/
noncomputable def lf_H3 (b A : ℝ) : (Fin 3 → ℝ) → Fin 5 → ℝ :=
  lf_Φ (fun t => A * Real.cosh t) (fun _ => b) A Real.sinh

theorem lf_H3_on {α b A : ℝ} (hA : A ^ 2 = b ^ 2 - α ^ 2) (y : Fin 3 → ℝ) :
    lf_η (lf_H3 b A y) = α ^ 2 ∧ lf_H3 b A y 1 = b := by
  refine ⟨?_, by simp [lf_H3, lf_Φ]⟩
  simp [lf_η, lf_H3, lf_Φ]
  ring_nf; simp only [Real.cos_sq', Real.cosh_sq]; linear_combination -hA

theorem lf_H3_pull (b A : ℝ) : lf_pull (lf_H3 b A) = lf_g A Real.sinh := by
  funext y
  rw [lf_H3, lf_pull_eq (V0 := fun t => A * Real.sinh t) (V1 := fun _ => 0) (D := Real.cosh)
    (fun t => (Real.hasDerivAt_cosh t).const_mul A) (fun t => hasDerivAt_const t b) Real.hasDerivAt_sinh y, lf_g]
  congr 1; ext i; fin_cases i <;> simp
  ring_nf; simp only [Real.cosh_sq]; ring

/-- **Row 5c.** The open leaf `X₁ = b > α` is `H³` of curvature `−1/(b² − α²)`: its induced metric has
`R_{abcd} = (−1/(b² − α²))(g_ac g_bd − g_ad g_bc)`. -/
theorem lf_open {α b A : ℝ} (hA0 : A ≠ 0) (hA : A ^ 2 = b ^ 2 - α ^ 2) {x : Fin 3 → ℝ}
    (h0 : Real.sinh (x 0) ≠ 0) (h1 : Real.sin (x 1) ≠ 0) (i j k l : Fin 3) :
    kr_Rlow (lf_pull (lf_H3 b A)) x i j k l = -1 / (b ^ 2 - α ^ 2) *
      (lf_pull (lf_H3 b A) x i k * lf_pull (lf_H3 b A) x j l -
        lf_pull (lf_H3 b A) x i l * lf_pull (lf_H3 b A) x j k) := by
  rw [lf_H3_pull, ← hA]
  exact lf_curv (R := A) (k := -1) (S := Real.sinh) (D := Real.cosh) (x := x)
    ⟨Real.hasDerivAt_sinh, fun t => by simpa using Real.hasDerivAt_cosh t,
      by rw [Real.cosh_sq]; ring, hA0, h0, h1⟩ i j k l

/-- The null direction `B = (1, 1, 0, 0, 0)` and the bilinear form `η(X, Y)`. -/
def lf_B : Fin 5 → ℝ := ![1, 1, 0, 0, 0]
def lf_ηb (X Y : Fin 5 → ℝ) : ℝ := -X 0 * Y 0 + X 1 * Y 1 + X 2 * Y 2 + X 3 * Y 3 + X 4 * Y 4

lemma lf_B_null : lf_ηb lf_B lf_B = 0 ∧ lf_B ≠ 0 := by
  refine ⟨by simp [lf_ηb, lf_B], fun h => ?_⟩
  have := congrFun h 0; simp [lf_B] at this

/-- The height `X₀` of the flat chart: `X₁ − X₀ = s` and `X₁ + X₀ = (α² − |y|²)/s`. -/
noncomputable def lf_h (α s : ℝ) (y : Fin 3 → ℝ) : ℝ := ((α ^ 2 - (y 0 ^ 2 + y 1 ^ 2 + y 2 ^ 2)) / s - s) / 2

/-- The flat chart `y ↦ (X₀(y), X₀(y) + s, y)`. -/
noncomputable def lf_horo (α s : ℝ) (y : Fin 3 → ℝ) : Fin 5 → ℝ := ![lf_h α s y, lf_h α s y + s, y 0, y 1, y 2]

/-- **Row 5b, the set.** For `s ≠ 0`, the flat chart is a bijection from `ℝ³` onto the horosphere
`{η(X, X) = α², η(X, B) = s}` of the null `B`. -/
theorem lf_horo_leaf (α : ℝ) {s : ℝ} (hs : s ≠ 0) :
    (∀ y, lf_η (lf_horo α s y) = α ^ 2 ∧ lf_ηb (lf_horo α s y) lf_B = s) ∧
      (∀ X, lf_η X = α ^ 2 → lf_ηb X lf_B = s → X = lf_horo α s ![X 2, X 3, X 4]) ∧
      Function.Injective (lf_horo α s) := by
  refine ⟨fun y => ⟨?_, ?_⟩, fun X hX hB => ?_, fun y z h => ?_⟩
  · simp [lf_η, lf_horo, lf_h]; field_simp; ring
  · simp [lf_ηb, lf_horo, lf_B]
  · simp [lf_ηb, lf_B] at hB
    simp [lf_η] at hX
    have h0 : X 0 = lf_h α s ![X 2, X 3, X 4] := by
      simp [lf_h]; field_simp
      have : X 1 = X 0 + s := by linarith
      rw [this] at hX; linear_combination hX
    ext i; fin_cases i <;> simp [lf_horo, h0]
    · simp [lf_h] at h0 ⊢; linarith
  · ext i; fin_cases i
    · exact congrFun h 2
    · exact congrFun h 3
    · exact congrFun h 4

lemma lf_pd_add_const (f : (Fin 3 → ℝ) → ℝ) (s : ℝ) (x : Fin 3 → ℝ) (c : Fin 3) :
    kr_pd (fun y => f y + s) x c = kr_pd f x c := by
  simp [kr_pd]

lemma lf_pd_coord (j : Fin 3) (x : Fin 3 → ℝ) (c : Fin 3) :
    kr_pd (fun y => y j) x c = if c = j then 1 else 0 := by
  fin_cases c <;> fin_cases j <;> simp [kr_pd]

/-- **The induced metric of the flat chart is `δ_ij`.** -/
theorem lf_horo_pull (α s : ℝ) : lf_pull (lf_horo α s) = fun _ => 1 := by
  funext x; ext i j
  have e1 : kr_pd (fun y => lf_horo α s y 1) x = kr_pd (fun y => lf_horo α s y 0) x := by
    funext c; exact lf_pd_add_const (lf_h α s) s x c
  have e2 : kr_pd (fun y => lf_horo α s y 2) x = kr_pd (fun y => y 0) x := rfl
  have e3 : kr_pd (fun y => lf_horo α s y 3) x = kr_pd (fun y => y 1) x := rfl
  have e4 : kr_pd (fun y => lf_horo α s y 4) x = kr_pd (fun y => y 2) x := rfl
  simp only [lf_pull, Matrix.of_apply, Fin.sum_univ_five, e1, e2, e3, e4, lf_pd_coord]
  fin_cases i <;> fin_cases j <;> simp [lf_ε]

/-- **Row 5b.** The flat leaf has curvature `0`: every `R^a_{bcd}` of its induced metric vanishes. -/
theorem lf_flat (α s : ℝ) (x : Fin 3 → ℝ) (a b c d : Fin 3) :
    kr_Riem (lf_pull (lf_horo α s)) x a b c d = 0 := by
  rw [lf_horo_pull]
  have hΓ : ∀ y a b c, kr_Γ (fun _ => (1 : Matrix (Fin 3) (Fin 3) ℝ)) y a b c = 0 := by
    intro y a b c; simp [kr_Γ, kr_pd_const]
  simp [kr_Riem, hΓ, kr_pd_const]

/-- **Non-vacuity, in one sense: each leaf's curvature takes a stated value at a concrete point of a non-empty
chart.** At `χ = θ = π/2` the closed leaf of `α = 1`, `c = 0` has `R_{0101} = 1`; at `ρ = 1`, `θ = π/2` the open
leaf of `α = 1`, `b = √2` has `R_{0101} = −sinh²1 ≠ 0`; the flat leaf's value is `0` at every point (`lf_flat`),
and the flat chart of `α = s = 1` puts the origin on its leaf, so that chart is non-empty. -/
theorem lf_witness :
    kr_Rlow (lf_pull (lf_S3 0 1)) ![π / 2, π / 2, 0] 0 1 0 1 = 1 ∧
      kr_Rlow (lf_pull (lf_H3 (Real.sqrt 2) 1)) ![1, π / 2, 0] 0 1 0 1 = -Real.sinh 1 ^ 2 ∧
      Real.sinh 1 ≠ 0 ∧
      lf_η (lf_horo 1 1 0) = 1 ^ 2 ∧ lf_ηb (lf_horo 1 1 0) lf_B = 1 := by
  have hs1 : Real.sinh 1 ≠ 0 := (Real.sinh_pos_iff.2 one_pos).ne'
  refine ⟨?_, ?_, hs1, (lf_horo_leaf 1 one_ne_zero).1 0⟩
  · rw [lf_closed (α := 1) one_ne_zero (by norm_num) (by simp) (by simp), lf_S3_pull]
    simp [lf_g, kr_s2]
  · rw [lf_open (α := 1) one_ne_zero (by norm_num) (by simp) (by simp), lf_H3_pull]
    simp [lf_g, kr_s2]; norm_num

end LfLeaves

end ShadowProbe.StaticEinsteinProbe
end LfCopy

namespace ShadowProbe.CosmologyProbe

open ShadowProbe.StaticEinsteinProbe

/-- **Row 5.** The constant-`τ` slice's induced metric `dr² + r²dΩ²` is `lf_g 1 id`, and its Riemann tensor vanishes
identically: `lf_curv` with `R = 1`, `S = id`, `S′ = 1`, `k = 0`. -/
theorem cm_flat_slice (x : Fin 3 → ℝ) (hr : x 0 ≠ 0) (hs : Real.sin (x 1) ≠ 0) :
    lf_g 1 id x = Matrix.diagonal ![1, x 0 ^ 2, x 0 ^ 2 * Real.sin (x 1) ^ 2] ∧
      ∀ a b c d, kr_Rlow (lf_g 1 id) x a b c d = 0 := by
  refine ⟨by simp [lf_g, kr_s2], fun a b c d => ?_⟩
  have := lf_curv (R := 1) (k := 0) (S := id) (D := fun _ => 1) (x := x)
    ⟨fun t => hasDerivAt_id t, fun t => by simpa using hasDerivAt_const t (1 : ℝ), by simp, one_ne_zero,
      hr, hs⟩ a b c d
  simpa using this

/-- **Row 2.** The substrate vacuum power `Λℓ_P² ≈ 3×10⁻¹²²` lies below `A_s ≈ 2×10⁻⁹` by a factor between `10¹¹²`
and `10¹¹³`. -/
theorem cm_substrate_ratio :
    (10 : ℝ) ^ 112 < (2 / 10 ^ 9) / (3 / 10 ^ 122) ∧ (2 / 10 ^ 9 : ℝ) / (3 / 10 ^ 122) < 10 ^ 113 := by
  constructor <;> norm_num

/-- **Row 3a.** The recollapse cap `M ≤ α/(3√3)` gives `(ℓ_P/M)² ≥ 27(ℓ_P/α)²`. -/
theorem cm_mass_cap {M α ℓ : ℝ} (hM : 0 < M) (hα : 0 < α) (h : M ≤ α / (3 * Real.sqrt 3)) :
    27 * (ℓ / α) ^ 2 ≤ (ℓ / M) ^ 2 := by
  have hs : 0 < Real.sqrt 3 := by positivity
  have h2 : M ^ 2 ≤ α ^ 2 / 27 := by
    have := pow_le_pow_left₀ hM.le h 2
    rw [div_pow, mul_pow, cm_s3] at this; linarith
  rw [div_pow, div_pow, ← mul_div_assoc, div_le_div_iff₀ (by positivity) (by positivity)]
  nlinarith [sq_nonneg ℓ]

/-- **Row 3b.** The transfer law on vacuum data at the cap, `9 × 2.6×10⁻¹²¹ × ρ⁻⁶`, is between `10⁻¹¹³` and
`10⁻¹¹²` at `ρ = 5.45×10⁻²`; it reaches the observed `2×10⁻⁹` only for `ρ` between `3×10⁻¹⁹` and `3.5×10⁻¹⁹`; and
the tensor floor `144π × 2.6×10⁻¹²¹ × ρ⁻⁶` is below `10⁻¹¹⁰`. -/
theorem cm_progenitor_arith :
    (1 / 10 ^ 113 : ℝ) < 9 * (26 / 10 ^ 122) / (545 / 10 ^ 4) ^ 6 ∧
      9 * (26 / 10 ^ 122) / (545 / 10 ^ 4) ^ 6 < (1 / 10 ^ 112 : ℝ) ∧
      (2 / 10 ^ 9 : ℝ) < 9 * (26 / 10 ^ 122) / (3 / 10 ^ 19) ^ 6 ∧
      9 * (26 / 10 ^ 122) / (35 / 10 ^ 20) ^ 6 < (2 / 10 ^ 9 : ℝ) ∧
      144 * π * (26 / 10 ^ 122) / (545 / 10 ^ 4) ^ 6 < (1 / 10 ^ 110 : ℝ) := by
  refine ⟨by norm_num, by norm_num, by norm_num, by norm_num, ?_⟩
  have hπ := Real.pi_lt_d2
  have hc : (0 : ℝ) < (26 / 10 ^ 122) / (545 / 10 ^ 4) ^ 6 := by positivity
  calc 144 * π * (26 / 10 ^ 122) / (545 / 10 ^ 4) ^ 6 = 144 * π * ((26 / 10 ^ 122) / (545 / 10 ^ 4) ^ 6) := by ring
    _ < 144 * 3.15 * ((26 / 10 ^ 122) / (545 / 10 ^ 4) ^ 6) := by gcongr
    _ < 1 / 10 ^ 110 := by norm_num

/-- **Non-vacuity.** The flat slice at `r = 1`, `θ = π/2`. -/
theorem cm_flat_witness : ∀ a b c d, kr_Rlow (lf_g 1 id) ![1, π / 2, 0] a b c d = 0 :=
  (cm_flat_slice _ (by simp) (by simp)).2

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
#print axioms ShadowProbe.StaticEinsteinProbe.lf_curv
#print axioms ShadowProbe.CosmologyProbe.cm_flat_slice
#print axioms ShadowProbe.CosmologyProbe.cm_substrate_ratio
#print axioms ShadowProbe.CosmologyProbe.cm_mass_cap
#print axioms ShadowProbe.CosmologyProbe.cm_progenitor_arith
#print axioms ShadowProbe.CosmologyProbe.cm_flat_witness

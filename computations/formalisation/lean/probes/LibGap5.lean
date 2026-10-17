import ShadowEngine

/-! # Campaign 33 (`r7443+71`): step 4's cheapest library-gap rows, 24, 82, 84 and 46 (and 23, cited)

`r7443_71_pricing/PRICING.md` read each receipt for what it computes. None of these needs the library its gap
named. Each takes one piece of data as imported, and that piece stays imported here, labelled:
- the one-loop `b₄` coefficients (24);
- the Dirac spectrum on round spheres and the Friedrich bound (82, 84);
- the area formula `4πr²` and `S = A/4` (46);
- the physical constants (84).

Row 23's receipt is the one row 19's campaign 12 formalised (`probes/RunningLayer.lean`), so it is cited there and
not rebuilt. -/

namespace ShadowProbe

namespace LibGap5

open Real

/-! ### Row 24 -/

/-- ⛭ **`b4_rewrite`.** In four dimensions, with `W = Riem² − 2Ric² + R²/3` and `GB = Riem² − 4Ric² + R²`:
- `Ric² = ½W − ½GB + ⅓R²`;
- the graviton `b₄ = (53/90)GB + (7/20)Ric² + (1/120)R²` (imported coefficients) is
  `(7/40)W + (149/360)GB + (1/8)R²`. -/
theorem b4_rewrite (Riem2 Ric2 R2 : ℝ) :
    let W := Riem2 - 2 * Ric2 + R2 / 3
    let GB := Riem2 - 4 * Ric2 + R2
    Ric2 = W / 2 - GB / 2 + R2 / 3 ∧
      53 / 90 * GB + 7 / 20 * Ric2 + 1 / 120 * R2 = 7 / 40 * W + 149 / 360 * GB + 1 / 8 * R2 := by
  intro W GB; constructor <;> simp only [W, GB] <;> ring

/-- **`trace_relation`.** `4ΛR − R·E_tr − R² = 0` at `E_tr = −R + 4Λ`: `R²` reduces to `{G-renorm, EOM}` -/
theorem trace_relation (Λ R : ℝ) : 4 * Λ * R - R * (-R + 4 * Λ) - R ^ 2 = 0 := by ring

/-- ⛭ **`shear_onset`.** The receipt's Weyl² on its shear family is `12σ²(H − 2σ)²`. `BianchiI.lean`'s `row1_shear`
proves that under the engine's connection, and it is cited. This Weyl² vanishes at `σ = 0`, has NO linear term,
and has `σ²` coefficient `12H²`, which is nonzero for `H ≠ 0`. -/
theorem shear_onset (H : ℝ) (hH : H ≠ 0) :
    (fun σ : ℝ => 12 * σ ^ 2 * (H - 2 * σ) ^ 2) 0 = 0 ∧
      (∀ σ, 12 * σ ^ 2 * (H - 2 * σ) ^ 2 = 0 + 0 * σ + 12 * H ^ 2 * σ ^ 2 - 48 * H * σ ^ 3 + 48 * σ ^ 4) ∧
      12 * H ^ 2 ≠ 0 := by
  refine ⟨by simp, fun σ => by ring, by positivity⟩

/-! ### Row 82 -/

/-- the round `Sⁿ` of radius `a`: `R = n(n−1)/a²` -/
noncomputable def Rs (n : ℕ) (a : ℝ) : ℝ := n * (n - 1) / a ^ 2
/-- IMPORTED, as the receipt types it: the Dirac spectrum on round `Sⁿ`, `±(n/2 + k)/a`, `k ≥ 0` -/
noncomputable def lamD (n k : ℕ) (a : ℝ) : ℝ := ((n : ℝ) / 2 + k) / a

/-- ⛭ **`friedrich_saturation`.** The lowest eigenvalue saturates the Friedrich bound `nR/(4(n−1))` at `n = 4` and
`n = 5`. And `λ_min(5) = 5/(2a) > 0`, with no `k ≥ 0` giving zero, and `R(5)/4 = 5/a²`. -/
theorem friedrich_saturation (a : ℝ) (ha : 0 < a) :
    lamD 4 0 a ^ 2 = 4 * Rs 4 a / (4 * (4 - 1)) ∧ lamD 5 0 a ^ 2 = 5 * Rs 5 a / (4 * (5 - 1)) ∧
      lamD 5 0 a = 5 / (2 * a) ∧ 0 < lamD 5 0 a ∧ (∀ k : ℕ, ((5 : ℝ) / 2 + k) ≠ 0) ∧ Rs 5 a / 4 = 5 / a ^ 2 := by
  have ha' : a ≠ 0 := ha.ne'
  refine ⟨?_, ?_, ?_, ?_, fun k => by positivity, ?_⟩
  · simp [lamD, Rs]; field_simp; ring
  · simp [lamD, Rs]; field_simp; ring
  · simp [lamD]; field_simp
  · simp [lamD]; positivity
  · simp [Rs]; field_simp; ring

/-! ### Row 84 -/

/-- ⛭ **`one_scale`.** With `α = √(3/Λ)`, the receipt's only scale: `R(S⁵) = 20Λ/3` and
`λ_min = (5/2)/α = (5/2)√Λ/√3` -/
theorem one_scale (Λ : ℝ) (hΛ : 0 < Λ) :
    let α := Real.sqrt (3 / Λ)
    5 * 4 / α ^ 2 = 20 * Λ / 3 ∧ (5 / 2) / α = 5 / 2 * Real.sqrt Λ / Real.sqrt 3 := by
  intro α
  have h3 : (0 : ℝ) < 3 / Λ := by positivity
  have hα2 : α ^ 2 = 3 / Λ := Real.sq_sqrt h3.le
  refine ⟨?_, ?_⟩
  · rw [hα2]; field_simp; norm_num
  · simp only [α]; rw [Real.sqrt_div (by norm_num : (0:ℝ) ≤ 3)]
    have : 0 < Real.sqrt 3 := by positivity
    have : 0 < Real.sqrt Λ := Real.sqrt_pos.mpr hΛ
    field_simp

/-- the receipt's constants (SI and eV, as it types them) and `m_min = 2.5 ħc H₀ √Ω_Λ / c` -/
noncomputable def mMin : ℝ :=
  2.5 * 1.973269804e-7 * (73.0 * 1e3 / 3.0856775814913673e22 * Real.sqrt 0.7) / 2.99792458e8

/-- ⛭ **`mass_bounds`.** `m_min < 10⁻³⁰ eV` and `m_e/m_min > 10³⁰`, as exact inequalities: only `0 < √0.7 < 1` is
needed -/
theorem mass_bounds : mMin < 1e-30 ∧ 5.10998950e5 / mMin > 1e30 := by
  have hs0 : 0 < Real.sqrt 0.7 := Real.sqrt_pos.mpr (by norm_num)
  have hs1 : Real.sqrt 0.7 < 1 := by
    rw [show (1 : ℝ) = Real.sqrt 1 by simp]; exact Real.sqrt_lt_sqrt (by norm_num) (by norm_num)
  have hpos : 0 < mMin := by unfold mMin; positivity
  have hlt : mMin < 4e-33 := by unfold mMin; nlinarith
  refine ⟨by linarith, ?_⟩
  rw [gt_iff_lt, lt_div_iff₀ hpos]; nlinarith

/-! ### Row 46 -/

/-- SdS with `α² = 3/Λ`: `f = 1 − 2M/r − r²/α²` -/
noncomputable def fS (M α r : ℝ) : ℝ := 1 - 2 * M / r - r ^ 2 / α ^ 2

/-- ⛭ **`photon_sphere`.** `d/dr(f/r²) = (6M − 2r)/r⁴`, which contains no `α`. On `r > 0` it vanishes exactly at
`r = 3M`. -/
theorem photon_sphere (M α r : ℝ) (hr : 0 < r) :
    HasDerivAt (fun x => fS M α x / x ^ 2) ((6 * M - 2 * r) / r ^ 4) r ∧
      ((6 * M - 2 * r) / r ^ 4 = 0 ↔ r = 3 * M) := by
  have hr' : r ≠ 0 := hr.ne'
  refine ⟨?_, ?_⟩
  · have e : (fun x => fS M α x / x ^ 2) =ᶠ[nhds r] fun x => (x ^ 2)⁻¹ - 2 * M * (x ^ 3)⁻¹ - 1 / α ^ 2 :=
      Filter.eventually_of_mem (isOpen_ne.mem_nhds hr') fun x (hx : x ≠ 0) => by
        simp only [fS]; field_simp
    refine HasDerivAt.congr_of_eventuallyEq ?_ e
    have h2 : HasDerivAt (fun x : ℝ => x ^ 2) (2 * r) r := by simpa using hasDerivAt_pow 2 r
    have h3 : HasDerivAt (fun x : ℝ => x ^ 3) (3 * r ^ 2) r := by simpa using hasDerivAt_pow 3 r
    have := ((h2.inv (pow_ne_zero 2 hr')).sub ((h3.inv (pow_ne_zero 3 hr')).const_mul (2 * M))).sub_const (1 / α ^ 2)
    convert this using 1; field_simp; ring
  · rw [div_eq_zero_iff]; constructor
    · rintro (h | h)
      · linarith
      · exact absurd h (pow_ne_zero 4 hr')
    · intro h; left; linarith

/-- ⛭ **`nariai_seam`.** At the Nariai mass `M_N = √3α/9`, `r_N = α/√3`:
- `3M_N = r_N`, so the photon sphere sits on the horizon;
- `f(r_N) = 0` and `f′(r_N) = 0`, the double root;
- the Lyapunov combination `f(2f − r²f″)/(2r²)` vanishes there. -/
theorem nariai_seam (α : ℝ) (hα : 0 < α) :
    let MN := Real.sqrt 3 * α / 9
    let rN := α / Real.sqrt 3
    3 * MN = rN ∧ fS MN α rN = 0 ∧ 2 * MN / rN ^ 2 - 2 * rN / α ^ 2 = 0 ∧
      fS MN α rN * (2 * fS MN α rN - rN ^ 2 * (-4 * MN / rN ^ 3 - 2 / α ^ 2)) / (2 * rN ^ 2) = 0 := by
  intro MN rN
  have h3 : Real.sqrt 3 ^ 2 = 3 := Real.sq_sqrt (by norm_num)
  have hs : 0 < Real.sqrt 3 := by positivity
  have hf : fS MN α rN = 0 := by
    simp only [fS, MN, rN]; field_simp; nlinarith [h3]
  refine ⟨?_, hf, ?_, by rw [hf]; simp⟩
  · simp only [MN, rN]; field_simp; nlinarith [h3]
  · simp only [MN, rN]; field_simp; nlinarith [h3]

/-- ⛭ **`areas_entropies`.** The area formula `4πr²` and `S = A/4ℓ_P²` are imported, with `α = √(3/Λ)`:
- the two readings' areas `16πM²` and `4πα²` agree only at `M = α/2`, which is not `M_N`;
- the seam area is `4πα²/3`, a third of `4πα²`;
- the entropies are `3π/(Λℓ²)` (substrate) and `π/(Λℓ²)` (seam), at `3/8` and `1/8` of `8π/(Λℓ²)`. -/
theorem areas_entropies (α M Λ ℓ : ℝ) (hα : 0 < α) (hM : 0 < M) (hΛ : 0 < Λ) (hℓ : 0 < ℓ)
    (hαΛ : α = Real.sqrt (3 / Λ)) :
    (16 * π * M ^ 2 = 4 * π * α ^ 2 ↔ M = α / 2) ∧ α / 2 ≠ Real.sqrt 3 * α / 9 ∧
      4 * π * (α / Real.sqrt 3) ^ 2 = 4 * π * α ^ 2 / 3 ∧
      4 * π * α ^ 2 / (4 * ℓ ^ 2) = 3 * π / (Λ * ℓ ^ 2) ∧
      4 * π * (α / Real.sqrt 3) ^ 2 / (4 * ℓ ^ 2) = π / (Λ * ℓ ^ 2) ∧
      (3 * π / (Λ * ℓ ^ 2)) / (8 * π / (Λ * ℓ ^ 2)) = 3 / 8 ∧
      (π / (Λ * ℓ ^ 2)) / (8 * π / (Λ * ℓ ^ 2)) = 1 / 8 := by
  have h3 : Real.sqrt 3 ^ 2 = 3 := Real.sq_sqrt (by norm_num)
  have hs : 0 < Real.sqrt 3 := by positivity
  have hα2 : α ^ 2 = 3 / Λ := by rw [hαΛ]; exact Real.sq_sqrt (by positivity)
  have hπ : 0 < π := Real.pi_pos
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_⟩
  · constructor
    · intro h
      have : M ^ 2 = (α / 2) ^ 2 := by nlinarith
      nlinarith [sq_nonneg (M - α / 2), sq_nonneg (M + α / 2)]
    · intro h; rw [h]; ring
  · intro h
    have : Real.sqrt 3 = 9 / 2 := by field_simp at h; nlinarith
    nlinarith [h3]
  · field_simp; rw [h3]
  · rw [hα2]; field_simp
  · field_simp; rw [h3, hα2]; field_simp
  · field_simp
  · field_simp

end LibGap5

end ShadowProbe

#print axioms ShadowProbe.LibGap5.b4_rewrite
#print axioms ShadowProbe.LibGap5.shear_onset
#print axioms ShadowProbe.LibGap5.friedrich_saturation
#print axioms ShadowProbe.LibGap5.one_scale
#print axioms ShadowProbe.LibGap5.mass_bounds
#print axioms ShadowProbe.LibGap5.photon_sphere
#print axioms ShadowProbe.LibGap5.nariai_seam
#print axioms ShadowProbe.LibGap5.areas_entropies

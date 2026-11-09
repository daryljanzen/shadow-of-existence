import Mathlib

/-!
# Probe `r7725+71.2` (campaign 123): P8's vacuum kernel

Registration: `computations/formalisation/r7725_71_campaign123/PREDICTION.md`. Nothing imports this file, and it
imports only Mathlib. It is a new standalone probe: these rows need nothing from the probe chain, so it copies no
earlier probe. Everything new has the prefix `ok_`. It backs P8 (`corpus/slicing_operator.tex`): `thm:kernel` and
`prop:bend`. `8πT^t_t` is read through eq. `Ttt`, `(rf′ + f − 1)/r² + Λ`, and `8πT^θ_θ` as `f″/2 + f′/r + Λ`.

* **Row 1b — BUILT.** `ok_vacuum_iff_ode`.
* **Row 1c — BUILT.** `ok_general_solution`, `ok_sds_solves`.
* **Row 1d — BUILT.** `ok_L_bound`, `ok_kernel`, `ok_onto`, `ok_index_one`.
* **Row 1e — BUILT.** `ok_matter_onto`.
* **Row 2 — BUILT.** `ok_bend`.
-/

open Set Filter Topology

namespace ShadowProbe.OperatorKernelProbe

/-- `8πT^t_t = 8πT^r_r` in the construction gauge (eq. `Ttt`). -/
noncomputable def ok_Tt (Λ : ℝ) (f : ℝ → ℝ) (r : ℝ) : ℝ := (r * deriv f r + f r - 1) / r ^ 2 + Λ

/-- `8πT^θ_θ = 8πT^φ_φ` in the construction gauge. -/
noncomputable def ok_Tθ (Λ : ℝ) (f : ℝ → ℝ) (r : ℝ) : ℝ := deriv (deriv f) r / 2 + deriv f r / r + Λ

/-- The vacuum ODE's left side, `rf′ + f − 1 + Λr²` (eq. `vacode`). -/
noncomputable def ok_ode (Λ : ℝ) (f : ℝ → ℝ) (r : ℝ) : ℝ := r * deriv f r + f r - 1 + Λ * r ^ 2

/-- The SdS profile `1 − 2M/r − Λr²/3` (eq. `sds`). -/
noncomputable def ok_sds (Λ M : ℝ) (r : ℝ) : ℝ := 1 - 2 * M / r - Λ * r ^ 2 / 3

/-- **Row 1b.** On an open interval in `(0, ∞)`, with `f` twice differentiable there, `T = 0` (all components)
⟺ the vacuum ODE. The angular equation is the radial one's derivative over `2r`. -/
theorem ok_vacuum_iff_ode {Λ a b : ℝ} (ha : 0 ≤ a) {f : ℝ → ℝ}
    (hf : ∀ r ∈ Ioo a b, DifferentiableAt ℝ f r) (hf' : ∀ r ∈ Ioo a b, DifferentiableAt ℝ (deriv f) r) :
    (∀ r ∈ Ioo a b, ok_Tt Λ f r = 0 ∧ ok_Tθ Λ f r = 0) ↔ ∀ r ∈ Ioo a b, ok_ode Λ f r = 0 := by
  have hr0 : ∀ r ∈ Ioo a b, r ≠ 0 := fun r hr => (ha.trans_lt hr.1).ne'
  have tt : ∀ r ∈ Ioo a b, ok_Tt Λ f r = ok_ode Λ f r / r ^ 2 := by
    intro r hr; have := hr0 r hr; unfold ok_Tt ok_ode; field_simp
  constructor
  · intro h r hr
    have h1 := (h r hr).1; rw [tt r hr] at h1
    exact (div_eq_zero_iff.mp h1).resolve_right (pow_ne_zero 2 (hr0 r hr))
  · intro h r hr
    refine ⟨by rw [tt r hr, h r hr, zero_div], ?_⟩
    have hd : HasDerivAt (ok_ode Λ f)
        (r * deriv (deriv f) r + 2 * deriv f r + 2 * Λ * r) r := by
      have h1 := ((hasDerivAt_id r).mul (hf' r hr).hasDerivAt).add (hf r hr).hasDerivAt
      have h2 := (h1.sub_const 1).add ((hasDerivAt_pow 2 r).const_mul Λ)
      refine h2.congr_deriv ?_
      simp; ring
    have hev : ok_ode Λ f =ᶠ[𝓝 r] fun _ => (0 : ℝ) := by
      filter_upwards [isOpen_Ioo.mem_nhds hr] with s hs using h s hs
    have hz : r * deriv (deriv f) r + 2 * deriv f r + 2 * Λ * r = 0 := by
      rw [← hd.deriv, hev.deriv_eq]; simp
    have := hr0 r hr
    unfold ok_Tθ
    field_simp
    linear_combination hz

/-- `rf′ + f − 1 + Λr² = (r f − r + Λr³/3)′`. -/
lemma ok_ode_deriv {Λ : ℝ} {f : ℝ → ℝ} {r : ℝ} (hf : DifferentiableAt ℝ f r) :
    HasDerivAt (fun s => s * f s - s + Λ * s ^ 3 / 3) (ok_ode Λ f r) r := by
  have h := ((((hasDerivAt_id r).mul hf.hasDerivAt).sub (hasDerivAt_id r)).add
    (((hasDerivAt_pow 3 r).const_mul Λ).div_const 3))
  refine h.congr_deriv ?_
  unfold ok_ode; simp; ring

/-- **Row 1c.** On an open interval in `(0, ∞)`, with `f` differentiable there: `f` solves the vacuum ODE iff it is
the SdS profile for a single constant `M`, the constant of integration. -/
theorem ok_general_solution {Λ a b : ℝ} (ha : 0 ≤ a) {f : ℝ → ℝ} (hf : DifferentiableOn ℝ f (Ioo a b)) :
    (∀ r ∈ Ioo a b, ok_ode Λ f r = 0) ↔ ∃ M, ∀ r ∈ Ioo a b, f r = ok_sds Λ M r := by
  have hr0 : ∀ r ∈ Ioo a b, r ≠ 0 := fun r hr => (ha.trans_lt hr.1).ne'
  have hdiff : ∀ r ∈ Ioo a b, DifferentiableAt ℝ f r :=
    fun r hr => hf.differentiableAt (isOpen_Ioo.mem_nhds hr)
  constructor
  · intro h
    obtain ⟨C, hC⟩ := isOpen_Ioo.exists_is_const_of_deriv_eq_zero isPreconnected_Ioo
      (f := fun s => s * f s - s + Λ * s ^ 3 / 3)
      (fun r hr => (ok_ode_deriv (hdiff r hr)).differentiableAt.differentiableWithinAt)
      (fun r hr => by rw [(ok_ode_deriv (Λ := Λ) (hdiff r hr)).deriv, h r hr]; rfl)
    refine ⟨-C / 2, fun r hr => ?_⟩
    have e := hC r hr
    have := hr0 r hr
    unfold ok_sds; field_simp
    linear_combination 3 * e
  · rintro ⟨M, hM⟩ r hr
    have := hr0 r hr
    have hev : f =ᶠ[𝓝 r] ok_sds Λ M := by
      filter_upwards [isOpen_Ioo.mem_nhds hr] with s hs using hM s hs
    have hd : HasDerivAt (ok_sds Λ M) (2 * M / r ^ 2 - 2 * Λ * r / 3) r := by
      have e : ok_sds Λ M = fun s => 1 - 2 * M * s⁻¹ - Λ * s ^ 2 / 3 := by
        funext s; simp only [ok_sds]; ring
      rw [e]
      refine HasDerivAt.congr_deriv ((((hasDerivAt_const r (1 : ℝ)).sub
        ((hasDerivAt_inv this).const_mul (2 * M))).sub (((hasDerivAt_pow 2 r).const_mul Λ).div_const 3))) ?_
      field_simp; ring
    unfold ok_ode
    rw [hev.deriv_eq, hd.deriv, hM r hr]
    unfold ok_sds; field_simp; ring

/-- **Row 1c, non-vacuity.** The SdS profile solves the vacuum ODE on all of `(0, ∞)`, for every `M`. -/
theorem ok_sds_solves (Λ M : ℝ) {r : ℝ} (hr : 0 < r) : ok_ode Λ (ok_sds Λ M) r = 0 := by
  have h := (ok_general_solution (Λ := Λ) (a := 0) (b := r + 1) le_rfl (f := ok_sds Λ M) ?_).2
    ⟨M, fun _ _ => rfl⟩ r ⟨hr, by linarith⟩
  · exact h
  · intro s hs
    have hs0 : s ≠ 0 := hs.1.ne'
    unfold ok_sds
    exact ((((differentiableAt_const _).sub ((differentiableAt_const _).div differentiableAt_id hs0)).sub
      (((differentiableAt_id.pow 2).const_mul Λ).div_const 3))).differentiableWithinAt

/-- The operator `L f = (r f)′`. -/
noncomputable def ok_L (f : ℝ → ℝ) (r : ℝ) : ℝ := deriv (fun s => s * f s) r

lemma ok_L_eq {f : ℝ → ℝ} {r : ℝ} (hf : DifferentiableAt ℝ f r) : ok_L f r = f r + r * deriv f r := by
  unfold ok_L
  have h : HasDerivAt (fun s => s * f s) (1 * f r + r * deriv f r) r := (hasDerivAt_id r).mul hf.hasDerivAt
  rw [h.deriv]; ring

/-- **Row 1d, bounded.** On `[r₁, r₂]`, `|Lf| ≤ |f| + r₂ |f′|`: `L` is bounded from `C¹` to `C⁰`. -/
theorem ok_L_bound {r₁ r₂ : ℝ} (h1 : 0 < r₁) {f : ℝ → ℝ} {r : ℝ} (hr : r ∈ Icc r₁ r₂)
    (hf : DifferentiableAt ℝ f r) : |ok_L f r| ≤ |f r| + r₂ * |deriv f r| := by
  rw [ok_L_eq hf]
  have hr0 : 0 ≤ r := h1.le.trans hr.1
  calc |f r + r * deriv f r| ≤ |f r| + |r * deriv f r| := abs_add_le _ _
    _ = |f r| + r * |deriv f r| := by rw [abs_mul, abs_of_nonneg hr0]
    _ ≤ |f r| + r₂ * |deriv f r| := by gcongr; exact hr.2

/-- **Row 1d, the kernel.** On `(r₁, r₂) ⊂ (0, ∞)`, `Lf = 0` iff `f = c/r`: `ker L = span{1/r}`. -/
theorem ok_kernel {r₁ r₂ : ℝ} (h1 : 0 ≤ r₁) {f : ℝ → ℝ} (hf : DifferentiableOn ℝ f (Ioo r₁ r₂)) :
    (∀ r ∈ Ioo r₁ r₂, ok_L f r = 0) ↔ ∃ c, ∀ r ∈ Ioo r₁ r₂, f r = c / r := by
  have hr0 : ∀ r ∈ Ioo r₁ r₂, r ≠ 0 := fun r hr => (h1.trans_lt hr.1).ne'
  have hdiff : ∀ r ∈ Ioo r₁ r₂, DifferentiableAt ℝ f r :=
    fun r hr => hf.differentiableAt (isOpen_Ioo.mem_nhds hr)
  constructor
  · intro h
    obtain ⟨c, hc⟩ := isOpen_Ioo.exists_is_const_of_deriv_eq_zero isPreconnected_Ioo
      (f := fun s => s * f s)
      (fun r hr => (differentiableAt_id.mul (hdiff r hr)).differentiableWithinAt)
      (fun r hr => h r hr)
    refine ⟨c, fun r hr => ?_⟩
    have := hr0 r hr
    rw [eq_div_iff this, mul_comm]; exact hc r hr
  · rintro ⟨c, hc⟩ r hr
    have hev : (fun s => s * f s) =ᶠ[𝓝 r] fun _ => c := by
      filter_upwards [isOpen_Ioo.mem_nhds hr] with s hs
      rw [hc s hs]; field_simp [hr0 s hs]
    unfold ok_L; rw [hev.deriv_eq]; simp

/-- **Row 1d, onto.** For every continuous `g`, `f = (1/r) ∫_{r₁}^r g` has `Lf = g` at every `r > 0`, in
particular on all of `[r₁, r₂]`, endpoints included. -/
theorem ok_onto {g : ℝ → ℝ} (hg : Continuous g) (r₁ : ℝ) {r : ℝ} (hr : 0 < r) :
    ok_L (fun s => (∫ x in r₁..s, g x) / s) r = g r := by
  have hev : (fun s => s * ((∫ x in r₁..s, g x) / s)) =ᶠ[𝓝 r] fun s => ∫ x in r₁..s, g x := by
    filter_upwards [Ioi_mem_nhds hr] with s (hs : 0 < s)
    field_simp
  unfold ok_L
  rw [hev.deriv_eq]
  exact (intervalIntegral.integral_hasDerivAt_right (hg.intervalIntegrable _ _)
    hg.aestronglyMeasurable.stronglyMeasurableAtFilter hg.continuousAt).deriv

/-- **Row 1d, index 1.** On `(r₁, r₂)`: `1/r` spans the kernel and is non-zero, and `L` is onto the continuous
functions. One-dimensional kernel, zero cokernel. -/
theorem ok_index_one {r₁ r₂ : ℝ} (h1 : 0 < r₁) (h12 : r₁ < r₂) :
    (∀ r ∈ Ioo r₁ r₂, ok_L (fun s => 1 / s) r = 0) ∧ (∃ r ∈ Ioo r₁ r₂, (fun s : ℝ => 1 / s) r ≠ 0) ∧
      (∀ f : ℝ → ℝ, DifferentiableOn ℝ f (Ioo r₁ r₂) → (∀ r ∈ Ioo r₁ r₂, ok_L f r = 0) →
        ∃ c, ∀ r ∈ Ioo r₁ r₂, f r = c * (1 / r)) ∧
      (∀ g : ℝ → ℝ, Continuous g → ∃ f : ℝ → ℝ, ∀ r ∈ Icc r₁ r₂, ok_L f r = g r) := by
  refine ⟨?_, ⟨(r₁ + r₂) / 2, ⟨by linarith, by linarith⟩, by
      have : 0 < (r₁ + r₂) / 2 := by linarith
      positivity⟩, ?_, ?_⟩
  · have hd : DifferentiableOn ℝ (fun s : ℝ => 1 / s) (Ioo r₁ r₂) := fun s hs =>
      ((differentiableAt_const _).div differentiableAt_id (h1.trans hs.1).ne').differentiableWithinAt
    exact (ok_kernel h1.le hd).2 ⟨1, fun _ _ => rfl⟩
  · intro f hf h
    obtain ⟨c, hc⟩ := (ok_kernel h1.le hf).1 h
    exact ⟨c, fun r hr => by rw [hc r hr]; ring⟩
  · intro g hg
    exact ⟨fun s => (∫ x in r₁..s, g x) / s, fun r hr => ok_onto hg r₁ (h1.trans_le hr.1)⟩

/-- **Row 2, `prop:bend`.** With `f = 1 − 2m(r)/r − Λr²/3` and `m` differentiable at `r ≠ 0`:
`8πT^t_t = (rf′ + f − 1)/r² + Λ = −2m′/r²`, i.e. `ρ = −T^t_t = m′/4πr²`. -/
theorem ok_bend {Λ : ℝ} {m : ℝ → ℝ} {r : ℝ} (hr : r ≠ 0) (hm : DifferentiableAt ℝ m r) :
    ok_Tt Λ (fun s => 1 - 2 * m s / s - Λ * s ^ 2 / 3) r = -(2 * deriv m r / r ^ 2) := by
  have hd : HasDerivAt (fun s => 1 - 2 * m s / s - Λ * s ^ 2 / 3)
      (-(2 * (deriv m r * r - m r) / r ^ 2) - 2 * Λ * r / 3) r := by
    have h := (((hasDerivAt_const r (1 : ℝ)).sub
      ((hm.hasDerivAt.const_mul 2).div (hasDerivAt_id r) hr)).sub
      (((hasDerivAt_pow 2 r).const_mul Λ).div_const 3))
    refine h.congr_deriv ?_
    simp; ring
  unfold ok_Tt
  rw [hd.deriv]
  field_simp; ring

/-- **Row 1e, the matter functional is onto.** For every continuous `ρ`, the mass `m(r) = ∫_{r₁}^r 4πs²ρ` gives a
cut `f = 1 − 2m/r − Λr²/3` whose `8πT^t_t` is `−8πρ` at every `r > 0`: the density `ρ` is realised. -/
theorem ok_matter_onto {ρ : ℝ → ℝ} (hρ : Continuous ρ) (Λ r₁ : ℝ) {r : ℝ} (hr : 0 < r) :
    ok_Tt Λ (fun s => 1 - 2 * (∫ x in r₁..s, 4 * Real.pi * x ^ 2 * ρ x) / s - Λ * s ^ 2 / 3) r =
      -(8 * Real.pi * ρ r) := by
  have hc : Continuous fun x => 4 * Real.pi * x ^ 2 * ρ x := by fun_prop
  have hD := intervalIntegral.integral_hasDerivAt_right (hc.intervalIntegrable r₁ r)
    hc.aestronglyMeasurable.stronglyMeasurableAtFilter hc.continuousAt
  rw [ok_bend (m := fun s => ∫ x in r₁..s, 4 * Real.pi * x ^ 2 * ρ x) hr.ne' hD.differentiableAt, hD.deriv]
  field_simp
  ring

end ShadowProbe.OperatorKernelProbe

#print axioms ShadowProbe.OperatorKernelProbe.ok_vacuum_iff_ode
#print axioms ShadowProbe.OperatorKernelProbe.ok_ode_deriv
#print axioms ShadowProbe.OperatorKernelProbe.ok_general_solution
#print axioms ShadowProbe.OperatorKernelProbe.ok_sds_solves
#print axioms ShadowProbe.OperatorKernelProbe.ok_L_eq
#print axioms ShadowProbe.OperatorKernelProbe.ok_L_bound
#print axioms ShadowProbe.OperatorKernelProbe.ok_kernel
#print axioms ShadowProbe.OperatorKernelProbe.ok_onto
#print axioms ShadowProbe.OperatorKernelProbe.ok_index_one
#print axioms ShadowProbe.OperatorKernelProbe.ok_bend
#print axioms ShadowProbe.OperatorKernelProbe.ok_matter_onto

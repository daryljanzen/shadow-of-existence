import Mathlib

/-!
# Probe `r7727+71.2` (campaign 124): P8's static Einstein tensor from the coordinate Riemann tensor

Registration: `computations/formalisation/r7727_71_campaign124/PREDICTION.md`. Nothing imports this file, and it
imports only Mathlib. It is campaign 123's `probes/OperatorKernel.lean` (namespace renamed
`ShadowProbe.StaticEinsteinProbe`, all old names kept; its header below is kept verbatim), plus campaign 110's
coordinate-curvature sections `KrCurvature` and `KrTrig` copied verbatim from `probes/SlicingCurvature.lean`, plus a
new `section EsStatic` (prefix `es_`), all before the `#print axioms` block. P8's names stay in one file.

* **Row 1a — BUILT.** `es_Γ`, `es_Ric_diag`, `es_einstein`; the construction gauge `es_construction_gauge`
  (P8 eq. `Ttt`, `Ttheta`).
* **Rows 3a–3c — BUILT.** `es_lapse` (eq. `rho-B`, `prho`, the lock).
* **Non-vacuity — BUILT.** `es_sds_vacuum`, `es_sds_witness`: SdS is vacuum from the Riemann tensor itself.
-/

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

namespace ShadowProbe.StaticEinsteinProbe

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

section EsStatic
open Real

/-- The static spherical metric `diag(−A(r), 1/F(r), r², r² sin²θ)` on `(t, r, θ, φ)`. -/
noncomputable def es_g (A F : ℝ → ℝ) (y : Fin 4 → ℝ) : Matrix (Fin 4) (Fin 4) ℝ :=
  Matrix.diagonal ![-A (y 1), (F (y 1))⁻¹, y 1 ^ 2, y 1 ^ 2 * kr_s2 (y 2)]

/-- Ricci `R_{bd} = R^a_{bad}`. -/
noncomputable def es_Ric (g : (Fin 4 → ℝ) → Matrix (Fin 4) (Fin 4) ℝ) (x : Fin 4 → ℝ) (b d : Fin 4) : ℝ :=
  ∑ a, kr_Riem g x a b a d

/-- The scalar curvature `R = g^{bd} R_{db}`. -/
noncomputable def es_scal (g : (Fin 4 → ℝ) → Matrix (Fin 4) (Fin 4) ℝ) (x : Fin 4 → ℝ) : ℝ :=
  ∑ b, ∑ d, (g x)⁻¹ b d * es_Ric g x d b

/-- The mixed Einstein tensor `G^b_c = g^{bd} R_{dc} − ½ δ^b_c R`. -/
noncomputable def es_G (g : (Fin 4 → ℝ) → Matrix (Fin 4) (Fin 4) ℝ) (x : Fin 4 → ℝ) (b c : Fin 4) : ℝ :=
  ∑ d, (g x)⁻¹ b d * es_Ric g x d c - (if b = c then es_scal g x / 2 else 0)

/-- The Christoffel entries, each a function of one variable. -/
noncomputable def es_c1 (A : ℝ → ℝ) (t : ℝ) : ℝ := deriv A t / (2 * A t)
noncomputable def es_c2 (A F : ℝ → ℝ) (t : ℝ) : ℝ := F t * deriv A t / 2
noncomputable def es_c3 (F : ℝ → ℝ) (t : ℝ) : ℝ := -(deriv F t) / (2 * F t)
noncomputable def es_c4 (F : ℝ → ℝ) (t : ℝ) : ℝ := -(t * F t)
noncomputable def es_c5 (t : ℝ) : ℝ := t⁻¹

/-- The Christoffel table of `es_g`. -/
noncomputable def es_T (A F : ℝ → ℝ) (y : Fin 4 → ℝ) : Fin 4 → Fin 4 → Fin 4 → ℝ :=
  ![![![0, es_c1 A (y 1), 0, 0], ![es_c1 A (y 1), 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]],
    ![![es_c2 A F (y 1), 0, 0, 0], ![0, es_c3 F (y 1), 0, 0], ![0, 0, es_c4 F (y 1), 0],
      ![0, 0, 0, es_c4 F (y 1) * kr_s2 (y 2)]],
    ![![0, 0, 0, 0], ![0, 0, es_c5 (y 1), 0], ![0, es_c5 (y 1), 0, 0], ![0, 0, 0, kr_nsc (y 2)]],
    ![![0, 0, 0, 0], ![0, 0, 0, es_c5 (y 1)], ![0, 0, 0, kr_cot (y 2)], ![0, es_c5 (y 1), kr_cot (y 2), 0]]]

variable {A F : ℝ → ℝ}

lemma es_g_inv {y : Fin 4 → ℝ} (hA : A (y 1) ≠ 0) (hF : F (y 1) ≠ 0) (hr : y 1 ≠ 0)
    (hs : Real.sin (y 2) ≠ 0) :
    (es_g A F y)⁻¹ = Matrix.diagonal ![-(A (y 1))⁻¹, F (y 1), (y 1 ^ 2)⁻¹, (y 1 ^ 2 * kr_s2 (y 2))⁻¹] := by
  refine Matrix.inv_eq_left_inv ?_
  rw [es_g, Matrix.diagonal_mul_diagonal, ← Matrix.diagonal_one]
  congr 1; ext i; fin_cases i <;> simp [kr_s2] <;> field_simp

lemma es_Γ {y : Fin 4 → ℝ} (hFd : DifferentiableAt ℝ F (y 1))
    (hA : A (y 1) ≠ 0) (hF : F (y 1) ≠ 0) (hr : y 1 ≠ 0) (hs : Real.sin (y 2) ≠ 0) (a b c : Fin 4) :
    kr_Γ (es_g A F) y a b c = es_T A F y a b c := by
  have d0 : deriv (fun t => -A t) (y 1) = -deriv A (y 1) := deriv.neg
  have d1 : deriv (fun t => (F t)⁻¹) (y 1) = -deriv F (y 1) / F (y 1) ^ 2 :=
    (hFd.hasDerivAt.inv hF).deriv
  have d2 : deriv (fun t : ℝ => t ^ 2) (y 1) = 2 * y 1 := by simp
  have d3 : deriv (fun t : ℝ => t ^ 2 * kr_s2 (y 2)) (y 1) = 2 * y 1 * kr_s2 (y 2) := by
    rw [((hasDerivAt_pow 2 (y 1)).mul_const (kr_s2 (y 2))).deriv]; ring
  have d4 : deriv (fun t => y 1 ^ 2 * kr_s2 t) (y 2) = y 1 ^ 2 * (2 * Real.sin (y 2) * Real.cos (y 2)) :=
    ((kr_hasDerivAt_s2 (y 2)).const_mul _).deriv
  simp only [kr_Γ, es_g_inv hA hF hr hs]
  fin_cases a <;> fin_cases b <;> fin_cases c <;>
    simp [kr_pd, es_g, es_T, Function.update_apply, Matrix.diagonal_apply, d0, d1, d2, d3, d4,
      es_c1, es_c2, es_c3, es_c4, es_c5, kr_nsc, kr_cot]
  all_goals (try simp only [kr_s2])
  all_goals field_simp

/-- The data at the point: `A, F` nonzero and `F` differentiable near `r`, `A′` differentiable at `r` with
derivative `A2`, `r ≠ 0`, `sin θ ≠ 0`. -/
structure es_Hyp (A F : ℝ → ℝ) (x : Fin 4 → ℝ) (A2 : ℝ) : Prop where
  hA : A (x 1) ≠ 0
  hF : F (x 1) ≠ 0
  hr : x 1 ≠ 0
  hs : Real.sin (x 2) ≠ 0
  hAd : DifferentiableAt ℝ A (x 1)
  hFd : ∀ᶠ t in 𝓝 (x 1), DifferentiableAt ℝ F t
  hA2 : HasDerivAt (deriv A) A2 (x 1)

variable {x : Fin 4 → ℝ} {A2 : ℝ}

lemma es_Hyp.U (h : es_Hyp A F x A2) : ∀ᶠ y in 𝓝 x, DifferentiableAt ℝ F (y 1) ∧ A (y 1) ≠ 0 ∧
    F (y 1) ≠ 0 ∧ y 1 ≠ 0 ∧ Real.sin (y 2) ≠ 0 := by
  have c1 : ContinuousAt (fun y : Fin 4 → ℝ => y 1) x := (continuous_apply 1).continuousAt
  have c2 : ContinuousAt (fun y : Fin 4 → ℝ => y 2) x := (continuous_apply 2).continuousAt
  have hFc : ContinuousAt F (x 1) := h.hFd.self_of_nhds.continuousAt
  filter_upwards [c1.eventually h.hFd,
    (ContinuousAt.comp (f := fun y : Fin 4 → ℝ => y 1) h.hAd.continuousAt c1).eventually_ne h.hA,
    (ContinuousAt.comp (f := fun y : Fin 4 → ℝ => y 1) hFc c1).eventually_ne h.hF, c1.eventually_ne h.hr,
    (ContinuousAt.comp (f := fun y : Fin 4 → ℝ => y 2) Real.continuous_sin.continuousAt c2).eventually_ne h.hs]
    with y h1 h2 h3 h4 h5
  exact ⟨h1, h2, h3, h4, h5⟩

lemma es_pd (h : es_Hyp A F x A2) (a b c d : Fin 4) :
    kr_pd (fun y => kr_Γ (es_g A F) y a b c) x d = kr_pd (fun y => es_T A F y a b c) x d :=
  kr_pd_congr (h.U.mono fun _ hy => es_Γ hy.1 hy.2.1 hy.2.2.1 hy.2.2.2.1 hy.2.2.2.2 a b c)

/-- **The Ricci diagonal of `es_g`.** -/
theorem es_Ric_diag (h : es_Hyp A F x A2) :
    es_Ric (es_g A F) x 0 0 = F (x 1) * A2 / 2 - F (x 1) * deriv A (x 1) ^ 2 / (4 * A (x 1))
        + deriv F (x 1) * deriv A (x 1) / 4 + F (x 1) * deriv A (x 1) / x 1 ∧
      es_Ric (es_g A F) x 1 1 = -(A2 / (2 * A (x 1))) + deriv A (x 1) ^ 2 / (4 * A (x 1) ^ 2)
        - deriv A (x 1) * deriv F (x 1) / (4 * A (x 1) * F (x 1)) - deriv F (x 1) / (x 1 * F (x 1)) ∧
      es_Ric (es_g A F) x 2 2 = 1 - F (x 1) - x 1 * F (x 1) * deriv A (x 1) / (2 * A (x 1))
        - x 1 * deriv F (x 1) / 2 ∧
      es_Ric (es_g A F) x 3 3 = kr_s2 (x 2) * (1 - F (x 1) - x 1 * F (x 1) * deriv A (x 1) / (2 * A (x 1))
        - x 1 * deriv F (x 1) / 2) := by
  have hΓ := es_Γ h.hFd.self_of_nhds h.hA h.hF h.hr h.hs
  have hFd := h.hFd.self_of_nhds
  have hA := h.hA; have hF := h.hF; have hr := h.hr; have hs := h.hs
  have e1 : deriv (es_c1 A) (x 1) = (A2 * A (x 1) - deriv A (x 1) ^ 2) / (2 * A (x 1) ^ 2) := by
    have h' : HasDerivAt (fun t => deriv A t / (2 * A t))
        ((A2 * (2 * A (x 1)) - deriv A (x 1) * (2 * deriv A (x 1))) / (2 * A (x 1)) ^ 2) (x 1) :=
      h.hA2.div (h.hAd.hasDerivAt.const_mul 2) (mul_ne_zero two_ne_zero hA)
    rw [show es_c1 A = fun t => deriv A t / (2 * A t) from rfl, h'.deriv]; field_simp
  have e2 : deriv (es_c2 A F) (x 1) = (deriv F (x 1) * deriv A (x 1) + F (x 1) * A2) / 2 := by
    have h' : HasDerivAt (fun t => F t * deriv A t / 2)
        ((deriv F (x 1) * deriv A (x 1) + F (x 1) * A2) / 2) (x 1) := (hFd.hasDerivAt.mul h.hA2).div_const 2
    rw [show es_c2 A F = fun t => F t * deriv A t / 2 from rfl, h'.deriv]
  have e4 : deriv (es_c4 F) (x 1) = -(F (x 1) + x 1 * deriv F (x 1)) := by
    have h' : HasDerivAt (fun t => -(t * F t)) (-(1 * F (x 1) + x 1 * deriv F (x 1))) (x 1) :=
      ((hasDerivAt_id (x 1)).mul hFd.hasDerivAt).neg
    rw [show es_c4 F = fun t => -(t * F t) from rfl, h'.deriv]; ring
  have e4s : deriv (fun t => es_c4 F t * kr_s2 (x 2)) (x 1) = -(F (x 1) + x 1 * deriv F (x 1)) * kr_s2 (x 2) := by
    have h' : HasDerivAt (fun t => -(t * F t) * kr_s2 (x 2))
        (-(1 * F (x 1) + x 1 * deriv F (x 1)) * kr_s2 (x 2)) (x 1) :=
      (((hasDerivAt_id (x 1)).mul hFd.hasDerivAt).neg).mul_const (kr_s2 (x 2))
    rw [show (fun t => es_c4 F t * kr_s2 (x 2)) = fun t => -(t * F t) * kr_s2 (x 2) from rfl, h'.deriv]; ring
  have e5 : deriv es_c5 (x 1) = -(x 1 ^ 2)⁻¹ := by
    rw [show es_c5 = fun t => t⁻¹ from rfl, deriv_inv]
  have en := kr_deriv_nsc (x 2)
  have ec := kr_deriv_cot hs
  refine ⟨?_, ?_, ?_, ?_⟩ <;>
  · unfold es_Ric kr_Riem
    simp only [Fin.sum_univ_four, es_pd h, hΓ]
    simp [es_T, kr_pd, e1, e2, e4, e4s, e5, en, ec]
    all_goals (try simp only [es_c1, es_c2, es_c3, es_c4, es_c5, kr_nsc, kr_cot, kr_s2])
    all_goals field_simp
    all_goals (try simp only [Real.cos_sq'])
    all_goals ring

/-- **Row 1a.** The mixed Einstein tensor of `diag(−A, 1/F, r², r² sin²θ)` from the coordinate Riemann tensor:
`G^t_t = (rF′ + F − 1)/r²` (no `A` in it), `G^r_r = (rFA′/A + F − 1)/r²`, and
`G^θ_θ = G^φ_φ = FA″/2A − FA′²/4A² + F′A′/4A + FA′/2rA + F′/2r`. -/
theorem es_einstein (h : es_Hyp A F x A2) :
    es_G (es_g A F) x 0 0 = (x 1 * deriv F (x 1) + F (x 1) - 1) / x 1 ^ 2 ∧
      es_G (es_g A F) x 1 1 = (x 1 * F (x 1) * deriv A (x 1) / A (x 1) + F (x 1) - 1) / x 1 ^ 2 ∧
      es_G (es_g A F) x 2 2 = F (x 1) * A2 / (2 * A (x 1)) - F (x 1) * deriv A (x 1) ^ 2 / (4 * A (x 1) ^ 2)
        + deriv F (x 1) * deriv A (x 1) / (4 * A (x 1)) + F (x 1) * deriv A (x 1) / (2 * x 1 * A (x 1))
        + deriv F (x 1) / (2 * x 1) ∧
      es_G (es_g A F) x 3 3 = es_G (es_g A F) x 2 2 := by
  obtain ⟨r0, r1, r2, r3⟩ := es_Ric_diag h
  have hA := h.hA; have hF := h.hF; have hr := h.hr
  have hs2 : kr_s2 (x 2) ≠ 0 := pow_ne_zero 2 h.hs
  have hinv := es_g_inv h.hA h.hF h.hr h.hs
  have G : ∀ b, es_G (es_g A F) x b b = (es_g A F x)⁻¹ b b * es_Ric (es_g A F) x b b - es_scal (es_g A F) x / 2 := by
    intro b
    simp only [es_G, hinv, Matrix.diagonal_apply, Fin.sum_univ_four]
    fin_cases b <;> simp
  have S : es_scal (es_g A F) x = -(A (x 1))⁻¹ * es_Ric (es_g A F) x 0 0 + F (x 1) * es_Ric (es_g A F) x 1 1
      + (x 1 ^ 2)⁻¹ * es_Ric (es_g A F) x 2 2 + (x 1 ^ 2 * kr_s2 (x 2))⁻¹ * es_Ric (es_g A F) x 3 3 := by
    simp only [es_scal, hinv, Matrix.diagonal_apply, Fin.sum_univ_four]
    simp
  refine ⟨?_, ?_, ?_, ?_⟩
  · rw [G, S, hinv, r0, r1, r2, r3]; simp; field_simp; ring
  · rw [G, S, hinv, r0, r1, r2, r3]; simp; field_simp; ring
  · rw [G, S, hinv, r0, r1, r2, r3]; simp; field_simp; ring
  · rw [G, G, S, hinv, r2, r3]; simp; field_simp

/-- **Row 1a, the construction gauge `A = F = f` (P8 eq. `Ttt`, `Ttheta`).** `G^t_t = G^r_r = (rf′ + f − 1)/r²` and
`G^θ_θ = G^φ_φ = f″/2 + f′/r`; with `+Λ` these are `8πT^t_t = 8πT^r_r` and `8πT^θ_θ = 8πT^φ_φ`. -/
theorem es_construction_gauge {f : ℝ → ℝ} {f2 : ℝ} (h : es_Hyp f f x f2) :
    es_G (es_g f f) x 0 0 = (x 1 * deriv f (x 1) + f (x 1) - 1) / x 1 ^ 2 ∧
      es_G (es_g f f) x 1 1 = es_G (es_g f f) x 0 0 ∧
      es_G (es_g f f) x 2 2 = f2 / 2 + deriv f (x 1) / x 1 ∧
      es_G (es_g f f) x 3 3 = es_G (es_g f f) x 2 2 := by
  obtain ⟨g0, g1, g2, g3⟩ := es_einstein h
  have := h.hA; have := h.hr
  refine ⟨g0, ?_, ?_, g3⟩
  · rw [g1, g0]; field_simp
  · rw [g2]; field_simp; ring

/-- **Rows 3a–3c, `prop:lapse`.** `G^t_t` has no `A` in it (eq. `rho-B`); `G^r_r − G^t_t = (F/r)(A′/A − F′/F)`
(eq. `prho`), which is `(F/r)(ln(A/F))′` where `A/F > 0`; and the lock `A = F` gives `G^r_r = G^t_t`, i.e.
`p_r + ρ = 0`. -/
theorem es_lapse (h : es_Hyp A F x A2) :
    (∀ A' : ℝ → ℝ, ∀ A2' : ℝ, es_Hyp A' F x A2' → es_G (es_g A' F) x 0 0 = es_G (es_g A F) x 0 0) ∧
      es_G (es_g A F) x 1 1 - es_G (es_g A F) x 0 0 =
        F (x 1) / x 1 * (deriv A (x 1) / A (x 1) - deriv F (x 1) / F (x 1)) ∧
      (0 < A (x 1) / F (x 1) →
        deriv (fun t => Real.log (A t / F t)) (x 1) = deriv A (x 1) / A (x 1) - deriv F (x 1) / F (x 1)) ∧
      (A = F → es_G (es_g A F) x 1 1 = es_G (es_g A F) x 0 0) := by
  obtain ⟨g0, g1, -, -⟩ := es_einstein h
  have hA := h.hA; have hF := h.hF; have hr := h.hr
  refine ⟨fun A' A2' h' => by rw [(es_einstein h').1, g0], by rw [g1, g0]; field_simp; ring, fun hpos => ?_, ?_⟩
  · have hd : HasDerivAt (fun t => Real.log (A t / F t))
        ((deriv A (x 1) * F (x 1) - A (x 1) * deriv F (x 1)) / F (x 1) ^ 2 / (A (x 1) / F (x 1))) (x 1) :=
      (h.hAd.hasDerivAt.div h.hFd.self_of_nhds.hasDerivAt hF).log hpos.ne'
    rw [hd.deriv]; field_simp
  · rintro rfl; rw [g1, g0]; field_simp

/-- The SdS profile's derivative off `r = 0`. -/
lemma es_sds_hasDeriv (Λ M : ℝ) {t : ℝ} (ht : t ≠ 0) :
    HasDerivAt (ok_sds Λ M) (2 * M / t ^ 2 - 2 * Λ * t / 3) t := by
  have e : ok_sds Λ M = fun s => 1 - 2 * M * s⁻¹ - Λ * s ^ 2 / 3 := by funext s; simp only [ok_sds]; ring
  rw [e]
  refine HasDerivAt.congr_deriv ((((hasDerivAt_const t (1 : ℝ)).sub
    ((hasDerivAt_inv ht).const_mul (2 * M))).sub (((hasDerivAt_pow 2 t).const_mul Λ).div_const 3))) ?_
  field_simp; ring

/-- **Non-vacuity, and the vacuum from the metric.** SdS, `A = F = 1 − 2M/r − Λr²/3`, at any point with `r > 0`,
`f ≠ 0` and `sin θ ≠ 0`, meets the hypotheses, and `G^μ_μ + Λ = 0` for every diagonal component: P8's vacuum,
computed from the coordinate Riemann tensor. -/
theorem es_sds_vacuum (Λ M : ℝ) {x : Fin 4 → ℝ} (hr : 0 < x 1) (hf : ok_sds Λ M (x 1) ≠ 0)
    (hs : Real.sin (x 2) ≠ 0) :
    es_Hyp (ok_sds Λ M) (ok_sds Λ M) x (-(4 * M / x 1 ^ 3) - 2 * Λ / 3) ∧
      es_G (es_g (ok_sds Λ M) (ok_sds Λ M)) x 0 0 + Λ = 0 ∧ es_G (es_g (ok_sds Λ M) (ok_sds Λ M)) x 1 1 + Λ = 0 ∧
      es_G (es_g (ok_sds Λ M) (ok_sds Λ M)) x 2 2 + Λ = 0 ∧ es_G (es_g (ok_sds Λ M) (ok_sds Λ M)) x 3 3 + Λ = 0 := by
  have hr0 := hr.ne'
  have hev : deriv (ok_sds Λ M) =ᶠ[𝓝 (x 1)] fun t => 2 * M / t ^ 2 - 2 * Λ * t / 3 := by
    filter_upwards [Ioi_mem_nhds hr] with t (ht : 0 < t) using (es_sds_hasDeriv Λ M ht.ne').deriv
  have h2 : HasDerivAt (deriv (ok_sds Λ M)) (-(4 * M / x 1 ^ 3) - 2 * Λ / 3) (x 1) := by
    refine HasDerivAt.congr_of_eventuallyEq ?_ hev
    have := (((hasDerivAt_pow 2 (x 1)).inv (pow_ne_zero 2 hr0)).const_mul (2 * M)).sub
      (((hasDerivAt_id (x 1)).const_mul (2 * Λ)).div_const 3)
    refine (this.congr_deriv ?_).congr_of_eventuallyEq ?_
    · field_simp; ring
    · filter_upwards with t; simp [div_eq_mul_inv]
  have H : es_Hyp (ok_sds Λ M) (ok_sds Λ M) x (-(4 * M / x 1 ^ 3) - 2 * Λ / 3) :=
    { hA := hf, hF := hf, hr := hr0, hs := hs, hAd := (es_sds_hasDeriv Λ M hr0).differentiableAt,
      hFd := by
        filter_upwards [Ioi_mem_nhds hr] with t (ht : 0 < t)
        exact (es_sds_hasDeriv Λ M ht.ne').differentiableAt,
      hA2 := h2 }
  obtain ⟨g0, g1, g2, g3⟩ := es_construction_gauge H
  have d1 := (es_sds_hasDeriv Λ M hr0).deriv
  have v0 : es_G (es_g (ok_sds Λ M) (ok_sds Λ M)) x 0 0 + Λ = 0 := by
    rw [g0, d1]; unfold ok_sds; field_simp; ring
  have v2 : es_G (es_g (ok_sds Λ M) (ok_sds Λ M)) x 2 2 + Λ = 0 := by
    rw [g2, d1]; field_simp; ring
  exact ⟨H, v0, by rw [g1]; exact v0, v2, by rw [g3]; exact v2⟩

/-- **A concrete point.** `M = 1`, `Λ = 3/100`, `r = 4`, `θ = π/2`: `f(4) = 17/50 ≠ 0`, so `es_sds_vacuum` applies. -/
theorem es_sds_witness :
    es_G (es_g (ok_sds (3 / 100) 1) (ok_sds (3 / 100) 1)) ![0, 4, π / 2, 0] 0 0 + 3 / 100 = 0 ∧
      es_G (es_g (ok_sds (3 / 100) 1) (ok_sds (3 / 100) 1)) ![0, 4, π / 2, 0] 2 2 + 3 / 100 = 0 := by
  have h := es_sds_vacuum (3 / 100) 1 (x := ![0, 4, π / 2, 0]) (by norm_num)
    (by simp [ok_sds]; norm_num) (by simp)
  exact ⟨h.2.1, h.2.2.2.1⟩

end EsStatic

end ShadowProbe.StaticEinsteinProbe

#print axioms ShadowProbe.StaticEinsteinProbe.ok_vacuum_iff_ode
#print axioms ShadowProbe.StaticEinsteinProbe.ok_ode_deriv
#print axioms ShadowProbe.StaticEinsteinProbe.ok_general_solution
#print axioms ShadowProbe.StaticEinsteinProbe.ok_sds_solves
#print axioms ShadowProbe.StaticEinsteinProbe.ok_L_eq
#print axioms ShadowProbe.StaticEinsteinProbe.ok_L_bound
#print axioms ShadowProbe.StaticEinsteinProbe.ok_kernel
#print axioms ShadowProbe.StaticEinsteinProbe.ok_onto
#print axioms ShadowProbe.StaticEinsteinProbe.ok_index_one
#print axioms ShadowProbe.StaticEinsteinProbe.ok_bend
#print axioms ShadowProbe.StaticEinsteinProbe.ok_matter_onto
#print axioms ShadowProbe.StaticEinsteinProbe.es_g_inv
#print axioms ShadowProbe.StaticEinsteinProbe.es_Γ
#print axioms ShadowProbe.StaticEinsteinProbe.es_pd
#print axioms ShadowProbe.StaticEinsteinProbe.es_Ric_diag
#print axioms ShadowProbe.StaticEinsteinProbe.es_einstein
#print axioms ShadowProbe.StaticEinsteinProbe.es_construction_gauge
#print axioms ShadowProbe.StaticEinsteinProbe.es_lapse
#print axioms ShadowProbe.StaticEinsteinProbe.es_sds_hasDeriv
#print axioms ShadowProbe.StaticEinsteinProbe.es_sds_vacuum
#print axioms ShadowProbe.StaticEinsteinProbe.es_sds_witness

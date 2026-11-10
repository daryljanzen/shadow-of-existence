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

**Campaign 125 (`r7729+71.2`), in this same file so P8's citations stay exact.** Registration:
`computations/formalisation/r7729_71_campaign125/PREDICTION.md`.
* **60's `r7730` ⓶ repairs.** `ok_vacuum_iff_ode` without the redundant second-derivative hypothesis;
  `ok_L_bound` as the operator (supremum) bound; `ok_index_one` as the integer index `dim ker − codim range = 1` of
  the linear map `ok_Lmap : C¹[r₁, r₂] → C⁰[r₁, r₂]` on the closed interval.
* **Off-diagonal components.** `es_Ric_offdiag`, `es_G_offdiag`; `es_sds_vacuum_full`: `T_{μν} = 0` whole for SdS.
* **Rows 4a–4c — BUILT.** `rg_cosmo` (with `rg_Γ`, `rg_witness`), `rg_sinh23`, `rg_sinh23_radial`, `rg_tau23`.
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

/-- The SdS profile's derivative off `r = 0`. -/
lemma ok_sds_hasDeriv (Λ M : ℝ) {t : ℝ} (ht : t ≠ 0) :
    HasDerivAt (ok_sds Λ M) (2 * M / t ^ 2 - 2 * Λ * t / 3) t := by
  have e : ok_sds Λ M = fun s => 1 - 2 * M * s⁻¹ - Λ * s ^ 2 / 3 := by funext s; simp only [ok_sds]; ring
  rw [e]
  refine HasDerivAt.congr_deriv ((((hasDerivAt_const t (1 : ℝ)).sub
    ((hasDerivAt_inv ht).const_mul (2 * M))).sub (((hasDerivAt_pow 2 t).const_mul Λ).div_const 3))) ?_
  field_simp; ring

/-- **Row 1b.** On an open interval in `(0, ∞)`, with `f` differentiable there, `T = 0` (all diagonal components)
⟺ the vacuum ODE. No second derivative is assumed: in the reverse direction the ODE makes `f` the SdS profile
(`ok_general_solution`), on which the angular component vanishes identically. -/
theorem ok_vacuum_iff_ode {Λ a b : ℝ} (ha : 0 ≤ a) {f : ℝ → ℝ}
    (hf : ∀ r ∈ Ioo a b, DifferentiableAt ℝ f r) :
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
    obtain ⟨M, hM⟩ := (ok_general_solution ha fun s hs => (hf s hs).differentiableWithinAt).1 h
    have hrpos : 0 < r := ha.trans_lt hr.1
    have hev : f =ᶠ[𝓝 r] ok_sds Λ M := by
      filter_upwards [isOpen_Ioo.mem_nhds hr] with s hs using hM s hs
    have hd : deriv (ok_sds Λ M) =ᶠ[𝓝 r] fun t => 2 * M / t ^ 2 - 2 * Λ * t / 3 := by
      filter_upwards [Ioi_mem_nhds hrpos] with t (ht : 0 < t) using (ok_sds_hasDeriv Λ M ht.ne').deriv
    have h2 : HasDerivAt (fun t : ℝ => 2 * M / t ^ 2 - 2 * Λ * t / 3) (-(4 * M / r ^ 3) - 2 * Λ / 3) r := by
      have := (((hasDerivAt_pow 2 r).inv (pow_ne_zero 2 hrpos.ne')).const_mul (2 * M)).sub
        (((hasDerivAt_id r).const_mul (2 * Λ)).div_const 3)
      refine (this.congr_deriv ?_).congr_of_eventuallyEq ?_
      · field_simp; ring
      · filter_upwards with t; simp [div_eq_mul_inv]
    have e1 : deriv f r = 2 * M / r ^ 2 - 2 * Λ * r / 3 := by
      rw [hev.deriv_eq, (ok_sds_hasDeriv Λ M hrpos.ne').deriv]
    have e2 : deriv (deriv f) r = -(4 * M / r ^ 3) - 2 * Λ / 3 := by
      rw [hev.deriv.deriv_eq, hd.deriv_eq, h2.deriv]
    unfold ok_Tθ; rw [e1, e2]; field_simp; ring

/-- The operator `L f = (r f)′`. -/
noncomputable def ok_L (f : ℝ → ℝ) (r : ℝ) : ℝ := deriv (fun s => s * f s) r

lemma ok_L_eq {f : ℝ → ℝ} {r : ℝ} (hf : DifferentiableAt ℝ f r) : ok_L f r = f r + r * deriv f r := by
  unfold ok_L
  have h : HasDerivAt (fun s => s * f s) (1 * f r + r * deriv f r) r := (hasDerivAt_id r).mul hf.hasDerivAt
  rw [h.deriv]; ring

/-- **Row 1d, bounded.** On `[r₁, r₂]`, for `f` differentiable there with `f′` continuous: pointwise
`|Lf| ≤ |f| + r₂|f′|`, and the operator bound `sup |Lf| ≤ max(1, r₂)(sup |f| + sup |f′|)`: `L` is bounded from
`C¹` to `C⁰`. -/
theorem ok_L_bound {r₁ r₂ : ℝ} (h1 : 0 < r₁) (h12 : r₁ ≤ r₂) {f : ℝ → ℝ}
    (hf : ∀ r ∈ Icc r₁ r₂, DifferentiableAt ℝ f r) (hc : ContinuousOn (deriv f) (Icc r₁ r₂)) :
    (∀ r ∈ Icc r₁ r₂, |ok_L f r| ≤ |f r| + r₂ * |deriv f r|) ∧
      sSup ((fun r => |ok_L f r|) '' Icc r₁ r₂) ≤
        max 1 r₂ * (sSup ((fun r => |f r|) '' Icc r₁ r₂) + sSup ((fun r => |deriv f r|) '' Icc r₁ r₂)) := by
  have pw : ∀ r ∈ Icc r₁ r₂, |ok_L f r| ≤ |f r| + r₂ * |deriv f r| := by
    intro r hr
    rw [ok_L_eq (hf r hr)]
    have hr0 : 0 ≤ r := h1.le.trans hr.1
    calc |f r + r * deriv f r| ≤ |f r| + |r * deriv f r| := abs_add_le _ _
      _ = |f r| + r * |deriv f r| := by rw [abs_mul, abs_of_nonneg hr0]
      _ ≤ |f r| + r₂ * |deriv f r| := by gcongr; exact hr.2
  refine ⟨pw, ?_⟩
  have hne : (Icc r₁ r₂).Nonempty := nonempty_Icc.mpr h12
  have hfc : ContinuousOn f (Icc r₁ r₂) := fun r hr => (hf r hr).continuousAt.continuousWithinAt
  have b0 : BddAbove ((fun r => |f r|) '' Icc r₁ r₂) :=
    (isCompact_Icc.image_of_continuousOn hfc.abs).bddAbove
  have b1 : BddAbove ((fun r => |deriv f r|) '' Icc r₁ r₂) :=
    (isCompact_Icc.image_of_continuousOn hc.abs).bddAbove
  have s0 : 0 ≤ sSup ((fun r => |f r|) '' Icc r₁ r₂) :=
    (abs_nonneg _).trans (le_csSup b0 ⟨r₁, ⟨le_rfl, h12⟩, rfl⟩)
  have s1 : 0 ≤ sSup ((fun r => |deriv f r|) '' Icc r₁ r₂) :=
    (abs_nonneg _).trans (le_csSup b1 ⟨r₁, ⟨le_rfl, h12⟩, rfl⟩)
  refine csSup_le (hne.image _) ?_
  rintro _ ⟨r, hr, rfl⟩
  have a0 : |f r| ≤ sSup ((fun r => |f r|) '' Icc r₁ r₂) := le_csSup b0 ⟨r, hr, rfl⟩
  have a1 : |deriv f r| ≤ sSup ((fun r => |deriv f r|) '' Icc r₁ r₂) := le_csSup b1 ⟨r, hr, rfl⟩
  have m1 : (1 : ℝ) ≤ max 1 r₂ := le_max_left _ _
  have m2 : r₂ ≤ max 1 r₂ := le_max_right _ _
  have hr2 : 0 ≤ r₂ := h1.le.trans (h12.trans le_rfl) |>.trans le_rfl
  calc |ok_L f r| ≤ |f r| + r₂ * |deriv f r| := pw r hr
    _ ≤ sSup ((fun r => |f r|) '' Icc r₁ r₂) + r₂ * sSup ((fun r => |deriv f r|) '' Icc r₁ r₂) := by
        gcongr
    _ ≤ _ := by nlinarith

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

/-- `C¹[r₁, r₂]`, as functions differentiable on `[r₁, r₂]` (one-sided at the ends) with continuous derivative there,
vanishing off it. -/
def ok_D (r₁ r₂ : ℝ) : Submodule ℝ (ℝ → ℝ) where
  carrier := {f | DifferentiableOn ℝ f (Icc r₁ r₂) ∧ ContinuousOn (derivWithin f (Icc r₁ r₂)) (Icc r₁ r₂) ∧
    ∀ r ∉ Icc r₁ r₂, f r = 0}
  add_mem' := by
    rintro f g ⟨hf1, hf2, hf3⟩ ⟨hg1, hg2, hg3⟩
    exact ⟨hf1.add hg1, (hf2.add hg2).congr fun r hr => derivWithin_add (hf1 r hr) (hg1 r hr),
      fun r hr => by simp [hf3 r hr, hg3 r hr]⟩
  zero_mem' := ⟨differentiableOn_const 0, (continuousOn_const (c := (0 : ℝ))).congr fun r _ => by simp,
    fun _ _ => rfl⟩
  smul_mem' := by
    rintro c f ⟨hf1, hf2, hf3⟩
    exact ⟨hf1.const_smul c, (hf2.const_smul c).congr fun r hr => derivWithin_const_smul c (hf1 r hr),
      fun r hr => by simp [hf3 r hr]⟩

lemma ok_D_iff {r₁ r₂ : ℝ} {f : ℝ → ℝ} : f ∈ ok_D r₁ r₂ ↔ (DifferentiableOn ℝ f (Icc r₁ r₂) ∧
    ContinuousOn (derivWithin f (Icc r₁ r₂)) (Icc r₁ r₂) ∧ ∀ r ∉ Icc r₁ r₂, f r = 0) := Iff.rfl

/-- `C⁰[r₁, r₂]`, as functions continuous on `[r₁, r₂]`, vanishing off it. -/
def ok_C0 (r₁ r₂ : ℝ) : Submodule ℝ (ℝ → ℝ) where
  carrier := {g | ContinuousOn g (Icc r₁ r₂) ∧ ∀ r ∉ Icc r₁ r₂, g r = 0}
  add_mem' := by
    rintro f g ⟨hf1, hf3⟩ ⟨hg1, hg3⟩
    exact ⟨hf1.add hg1, fun r hr => by simp [hf3 r hr, hg3 r hr]⟩
  zero_mem' := ⟨continuousOn_const, fun _ _ => rfl⟩
  smul_mem' := by
    rintro c f ⟨hf1, hf3⟩
    exact ⟨hf1.const_smul c, fun r hr => by simp [hf3 r hr]⟩

lemma ok_C0_iff {r₁ r₂ : ℝ} {g : ℝ → ℝ} : g ∈ ok_C0 r₁ r₂ ↔ (ContinuousOn g (Icc r₁ r₂) ∧
    ∀ r ∉ Icc r₁ r₂, g r = 0) := Iff.rfl

/-- `L f = f + r f′` on `[r₁, r₂]` (one-sided at the ends), zero off it. -/
noncomputable def ok_Lfun (r₁ r₂ : ℝ) (f : ℝ → ℝ) : ℝ → ℝ :=
  (Icc r₁ r₂).indicator fun r => f r + r * derivWithin f (Icc r₁ r₂) r

lemma ok_Lfun_mem {r₁ r₂ : ℝ} {f : ℝ → ℝ} (hf : f ∈ ok_D r₁ r₂) : ok_Lfun r₁ r₂ f ∈ ok_C0 r₁ r₂ :=
  ok_C0_iff.mpr ⟨((ok_D_iff.mp hf).1.continuousOn.add (continuousOn_id.mul (ok_D_iff.mp hf).2.1)).congr fun r hr => by
      simp [ok_Lfun, Set.indicator_of_mem hr],
    fun r hr => by simp [ok_Lfun, Set.indicator_of_notMem hr]⟩

/-- **The operator `L : C¹[r₁, r₂] → C⁰[r₁, r₂]`, `f ↦ (rf)′`,** as a linear map. -/
noncomputable def ok_Lmap (r₁ r₂ : ℝ) : ok_D r₁ r₂ →ₗ[ℝ] ok_C0 r₁ r₂ where
  toFun f := ⟨ok_Lfun r₁ r₂ f, ok_Lfun_mem f.2⟩
  map_add' f g := by
    refine Subtype.ext (funext fun r => ?_)
    by_cases hr : r ∈ Icc r₁ r₂
    · simp only [ok_Lfun, Submodule.coe_add, Pi.add_apply, Set.indicator_of_mem hr]
      rw [derivWithin_add ((ok_D_iff.mp f.2).1 r hr) ((ok_D_iff.mp g.2).1 r hr)]; ring
    · simp [ok_Lfun, Set.indicator_of_notMem hr]
  map_smul' c f := by
    refine Subtype.ext (funext fun r => ?_)
    by_cases hr : r ∈ Icc r₁ r₂
    · simp only [ok_Lfun, Submodule.coe_smul, Pi.smul_apply, smul_eq_mul, Set.indicator_of_mem hr,
        RingHom.id_apply]
      rw [derivWithin_const_smul c ((ok_D_iff.mp f.2).1 r hr)]; simp; ring
    · simp [ok_Lfun, Set.indicator_of_notMem hr]

/-- On `[r₁, r₂]`, `L f = (rf)′`, the derivative within `[r₁, r₂]`. -/
lemma ok_Lfun_eq {r₁ r₂ : ℝ} (h12 : r₁ < r₂) {f : ℝ → ℝ} {r : ℝ} (hr : r ∈ Icc r₁ r₂)
    (hf : DifferentiableWithinAt ℝ f (Icc r₁ r₂) r) :
    derivWithin (fun s => s * f s) (Icc r₁ r₂) r = f r + r * derivWithin f (Icc r₁ r₂) r := by
  have hid : derivWithin (fun s : ℝ => s) (Icc r₁ r₂) r = 1 := by
    exact (hasDerivWithinAt_id r (Icc r₁ r₂)).derivWithin (uniqueDiffOn_Icc h12 r hr)
  rw [derivWithin_fun_mul (c := fun s : ℝ => s) differentiableWithinAt_id hf, hid]; ring

/-- `1/r` on `[r₁, r₂]`, zero off it: the kernel's generator. -/
noncomputable def ok_invFun (r₁ r₂ : ℝ) : ℝ → ℝ := (Icc r₁ r₂).indicator fun r => r⁻¹

lemma ok_invFun_deriv {r₁ r₂ : ℝ} (h1 : 0 < r₁) (h12 : r₁ < r₂) {r : ℝ} (hr : r ∈ Icc r₁ r₂) :
    derivWithin (ok_invFun r₁ r₂) (Icc r₁ r₂) r = -(r ^ 2)⁻¹ := by
  have hr0 : r ≠ 0 := (h1.trans_le hr.1).ne'
  rw [derivWithin_congr (f := fun r : ℝ => r⁻¹) (fun s hs => by simp [ok_invFun, Set.indicator_of_mem hs])
    (by simp [ok_invFun, Set.indicator_of_mem hr]),
    (hasDerivAt_inv hr0).hasDerivWithinAt.derivWithin (uniqueDiffOn_Icc h12 r hr)]

lemma ok_invFun_mem {r₁ r₂ : ℝ} (h1 : 0 < r₁) (h12 : r₁ < r₂) : ok_invFun r₁ r₂ ∈ ok_D r₁ r₂ := by
  refine ok_D_iff.mpr ⟨fun r hr => ?_, ?_, fun r hr => by simp [ok_invFun, Set.indicator_of_notMem hr]⟩
  · have hr0 : r ≠ 0 := (h1.trans_le hr.1).ne'
    exact ((hasDerivAt_inv hr0).differentiableAt.differentiableWithinAt).congr
      (fun s hs => by simp [ok_invFun, Set.indicator_of_mem hs]) (by simp [ok_invFun, Set.indicator_of_mem hr])
  · refine (continuousOn_id.pow 2 |>.inv₀ fun r hr => pow_ne_zero 2 (h1.trans_le hr.1).ne').neg.congr ?_
    intro r hr; rw [ok_invFun_deriv h1 h12 hr]; rfl

/-- The kernel's generator as an element of `C¹[r₁, r₂]`. -/
noncomputable def ok_inv {r₁ r₂ : ℝ} (h1 : 0 < r₁) (h12 : r₁ < r₂) : ok_D r₁ r₂ :=
  ⟨ok_invFun r₁ r₂, ok_invFun_mem h1 h12⟩

/-- **Row 1d, index 1, on `[r₁, r₂]` as P8 states it.** For `L : C¹[r₁, r₂] → C⁰[r₁, r₂]`, `f ↦ (rf)′`:
`ker L = span{1/r}`, `dim ker L = 1`, `L` is onto, and the index `dim ker L − codim range L` is `1`. -/
theorem ok_index_one {r₁ r₂ : ℝ} (h1 : 0 < r₁) (h12 : r₁ < r₂) :
    LinearMap.ker (ok_Lmap r₁ r₂) = ℝ ∙ ok_inv h1 h12 ∧
      Module.finrank ℝ (LinearMap.ker (ok_Lmap r₁ r₂)) = 1 ∧
      LinearMap.range (ok_Lmap r₁ r₂) = ⊤ ∧
      (Module.finrank ℝ (LinearMap.ker (ok_Lmap r₁ r₂)) : ℤ) -
        Module.finrank ℝ (ok_C0 r₁ r₂ ⧸ LinearMap.range (ok_Lmap r₁ r₂)) = 1 := by
  have hI : ∀ {r}, r ∈ Icc r₁ r₂ → r ≠ 0 := fun hr => (h1.trans_le hr.1).ne'
  -- the kernel
  have hker : LinearMap.ker (ok_Lmap r₁ r₂) = ℝ ∙ ok_inv h1 h12 := by
    ext f
    rw [LinearMap.mem_ker, Submodule.mem_span_singleton]
    constructor
    · intro hf
      have hz : ∀ r ∈ Icc r₁ r₂, (f : ℝ → ℝ) r + r * derivWithin f (Icc r₁ r₂) r = 0 := by
        intro r hr
        have := congrFun (congrArg Subtype.val hf) r
        simpa [ok_Lmap, ok_Lfun, Set.indicator_of_mem hr] using this
      have hc := constant_of_derivWithin_zero (f := fun s => s * (f : ℝ → ℝ) s)
        (differentiableOn_id.mul (ok_D_iff.mp f.2).1) (fun x hx => by
          rw [ok_Lfun_eq h12 (Ico_subset_Icc_self hx) ((ok_D_iff.mp f.2).1 x (Ico_subset_Icc_self hx))]
          exact hz x (Ico_subset_Icc_self hx))
      refine ⟨r₁ * (f : ℝ → ℝ) r₁, Subtype.ext (funext fun r => ?_)⟩
      by_cases hr : r ∈ Icc r₁ r₂
      · have e := hc r hr
        simp only [Submodule.coe_smul, Pi.smul_apply, smul_eq_mul, ok_inv, ok_invFun,
          Set.indicator_of_mem hr]
        have := hI hr
        field_simp; linarith
      · simp [ok_inv, ok_invFun, Set.indicator_of_notMem hr, (ok_D_iff.mp f.2).2.2 r hr]
    · rintro ⟨a, rfl⟩
      rw [map_smul]
      have : ok_Lmap r₁ r₂ (ok_inv h1 h12) = 0 := by
        refine Subtype.ext (funext fun r => ?_)
        by_cases hr : r ∈ Icc r₁ r₂
        · simp only [ok_Lmap, LinearMap.coe_mk, AddHom.coe_mk, ok_Lfun, Set.indicator_of_mem hr, ok_inv,
            ZeroMemClass.coe_zero, Pi.zero_apply]
          rw [ok_invFun_deriv h1 h12 hr]
          simp only [ok_invFun, Set.indicator_of_mem hr]
          have := hI hr; field_simp; ring
        · simp [ok_Lmap, ok_Lfun, Set.indicator_of_notMem hr]
      rw [this, smul_zero]
  have hne : ok_inv h1 h12 ≠ 0 := by
    intro h
    have := congrFun (congrArg Subtype.val h) r₁
    have hm : r₁ ∈ Icc r₁ r₂ := ⟨le_rfl, h12.le⟩
    simp [ok_inv, ok_invFun, Set.indicator_of_mem hm, h1.ne'] at this
  have hdim : Module.finrank ℝ (LinearMap.ker (ok_Lmap r₁ r₂)) = 1 := by
    rw [hker]; exact finrank_span_singleton hne
  -- onto
  have hrange : LinearMap.range (ok_Lmap r₁ r₂) = ⊤ := by
    refine LinearMap.range_eq_top.mpr fun g => ?_
    set c : ℝ → ℝ := fun x => max r₁ (min r₂ x) with hcdef
    have hcI : ∀ x, c x ∈ Icc r₁ r₂ := fun x => ⟨le_max_left _ _, max_le h12.le (min_le_left _ _)⟩
    have hcid : ∀ x ∈ Icc r₁ r₂, c x = x := fun x hx => by
      simp only [hcdef, min_eq_right hx.2, max_eq_right hx.1]
    have hG : Continuous fun x => (g : ℝ → ℝ) (c x) :=
      (ok_C0_iff.mp g.2).1.comp_continuous (by fun_prop) hcI
    set G : ℝ → ℝ := fun x => (g : ℝ → ℝ) (c x) with hGdef
    have hInt : ∀ r, HasDerivAt (fun u => ∫ x in r₁..u, G x) (G r) r := fun r =>
      intervalIntegral.integral_hasDerivAt_right (hG.intervalIntegrable _ _)
        hG.aestronglyMeasurable.stronglyMeasurableAtFilter hG.continuousAt
    set Φ : ℝ → ℝ := fun r => (∫ x in r₁..r, G x) / r with hΦ
    have hΦd : ∀ r, r ≠ 0 → HasDerivAt Φ
        ((G r * r - (∫ x in r₁..r, G x) * 1) / r ^ 2) r := fun r hr => (hInt r).div (hasDerivAt_id r) hr
    set F : ℝ → ℝ := (Icc r₁ r₂).indicator Φ with hFdef
    have hFΦ : EqOn F Φ (Icc r₁ r₂) := fun s hs => by simp [hFdef, Set.indicator_of_mem hs]
    have hFd : ∀ r ∈ Icc r₁ r₂, derivWithin F (Icc r₁ r₂) r =
        (G r * r - (∫ x in r₁..r, G x) * 1) / r ^ 2 := fun r hr => by
      rw [derivWithin_congr hFΦ (hFΦ hr), (hΦd r (hI hr)).hasDerivWithinAt.derivWithin
        (uniqueDiffOn_Icc h12 r hr)]
    have hFmem : F ∈ ok_D r₁ r₂ := by
      refine ok_D_iff.mpr ⟨fun r hr => ((hΦd r (hI hr)).differentiableAt.differentiableWithinAt).congr hFΦ (hFΦ hr),
        ?_, fun r hr => by simp [hFdef, Set.indicator_of_notMem hr]⟩
      have hcInt : Continuous fun r => ∫ x in r₁..r, G x :=
        continuous_iff_continuousAt.mpr fun r => (hInt r).continuousAt
      refine (((hG.mul continuous_id).sub (hcInt.mul continuous_const)).continuousOn.div
        (continuous_id.pow 2).continuousOn fun r hr => pow_ne_zero 2 (hI hr)).congr fun r hr => hFd r hr
    refine ⟨⟨F, hFmem⟩, Subtype.ext (funext fun r => ?_)⟩
    by_cases hr : r ∈ Icc r₁ r₂
    · simp only [ok_Lmap, LinearMap.coe_mk, AddHom.coe_mk, ok_Lfun, Set.indicator_of_mem hr]
      rw [hFd r hr, hFΦ hr]
      simp only [hΦ, hGdef, hcid r hr]
      have := hI hr; field_simp; ring
    · simp [ok_Lmap, ok_Lfun, Set.indicator_of_notMem hr, (ok_C0_iff.mp g.2).2 r hr]
  refine ⟨hker, hdim, hrange, ?_⟩
  rw [hdim, hrange]
  have : Subsingleton (ok_C0 r₁ r₂ ⧸ (⊤ : Submodule ℝ (ok_C0 r₁ r₂))) :=
    Submodule.Quotient.subsingleton_iff.mpr rfl
  rw [Module.finrank_zero_of_subsingleton]; norm_num

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

/-- **The off-diagonal Ricci components vanish:** `R_{bc} = 0` for `b ≠ c`. -/
theorem es_Ric_offdiag (h : es_Hyp A F x A2) (b c : Fin 4) (hbc : b ≠ c) : es_Ric (es_g A F) x b c = 0 := by
  have hΓ := es_Γ h.hFd.self_of_nhds h.hA h.hF h.hr h.hs
  have hA := h.hA; have hF := h.hF; have hr := h.hr; have hs := h.hs
  fin_cases b <;> fin_cases c <;> (try exact absurd rfl hbc) <;>
  · unfold es_Ric kr_Riem
    simp only [Fin.sum_univ_four, es_pd h, hΓ]
    simp [es_T, kr_pd]
    all_goals (try simp only [es_c5, kr_cot])
    all_goals (try field_simp)
    all_goals (try ring)

/-- **The off-diagonal Einstein components vanish:** `G^b_c = 0` for `b ≠ c`. -/
theorem es_G_offdiag (h : es_Hyp A F x A2) (b c : Fin 4) (hbc : b ≠ c) : es_G (es_g A F) x b c = 0 := by
  have hinv := es_g_inv h.hA h.hF h.hr h.hs
  have hR := es_Ric_offdiag h b c hbc
  simp only [es_G, hbc, ↓reduceIte, sub_zero, hinv, Matrix.diagonal_apply, ite_mul, zero_mul,
    Finset.sum_ite_eq, Finset.mem_univ, hR, mul_zero]

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

/-- **`T_{μν} = 0` whole, for SdS:** `G^b_c + Λδ^b_c = 0` for all sixteen `(b, c)`, from the Riemann tensor. -/
theorem es_sds_vacuum_full (Λ M : ℝ) {x : Fin 4 → ℝ} (hr : 0 < x 1) (hf : ok_sds Λ M (x 1) ≠ 0)
    (hs : Real.sin (x 2) ≠ 0) (b c : Fin 4) :
    es_G (es_g (ok_sds Λ M) (ok_sds Λ M)) x b c + (if b = c then Λ else 0) = 0 := by
  obtain ⟨H, v0, v1, v2, v3⟩ := es_sds_vacuum Λ M hr hf hs
  by_cases hbc : b = c
  · subst hbc; simp only [↓reduceIte]
    rcases (show b = 0 ∨ b = 1 ∨ b = 2 ∨ b = 3 by fin_cases b <;> simp) with rfl | rfl | rfl | rfl
    exacts [v0, v1, v2, v3]
  · simp only [hbc, ↓reduceIte, add_zero, es_G_offdiag H b c hbc]

/-- **A concrete point.** `M = 1`, `Λ = 3/100`, `r = 4`, `θ = π/2`: `f(4) = 17/50 ≠ 0`, so `es_sds_vacuum` applies. -/
theorem es_sds_witness :
    es_G (es_g (ok_sds (3 / 100) 1) (ok_sds (3 / 100) 1)) ![0, 4, π / 2, 0] 0 0 + 3 / 100 = 0 ∧
      es_G (es_g (ok_sds (3 / 100) 1) (ok_sds (3 / 100) 1)) ![0, 4, π / 2, 0] 2 2 + 3 / 100 = 0 := by
  have h := es_sds_vacuum (3 / 100) 1 (x := ![0, 4, π / 2, 0]) (by norm_num)
    (by simp [ok_sds]; norm_num) (by simp)
  exact ⟨h.2.1, h.2.2.2.1⟩

end EsStatic

section RgRadial
open Real

/-- The radial plane `diag(−f(r), 1/f(r))` on `(t, r)`. -/
noncomputable def rg_g (f : ℝ → ℝ) (y : Fin 2 → ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  !![-f (y 1), 0; 0, (f (y 1))⁻¹]

/-- Its Christoffel symbols: `Γ⁰₀₁ = Γ⁰₁₀ = f′/2f`, `Γ¹₀₀ = ff′/2`, `Γ¹₁₁ = −f′/2f`, the rest zero. -/
noncomputable def rg_T (f : ℝ → ℝ) (y : Fin 2 → ℝ) : Fin 2 → Fin 2 → Fin 2 → ℝ :=
  ![![![0, deriv f (y 1) / (2 * f (y 1))], ![deriv f (y 1) / (2 * f (y 1)), 0]],
    ![![f (y 1) * deriv f (y 1) / 2, 0], ![0, -(deriv f (y 1)) / (2 * f (y 1))]]]

lemma rg_Γ {f : ℝ → ℝ} {y : Fin 2 → ℝ} (hfd : DifferentiableAt ℝ f (y 1)) (hf : f (y 1) ≠ 0)
    (a b c : Fin 2) : kr_Γ (rg_g f) y a b c = rg_T f y a b c := by
  have hinv : (rg_g f y)⁻¹ = !![-(f (y 1))⁻¹, 0; 0, f (y 1)] := by
    refine Matrix.inv_eq_left_inv ?_
    ext i j; fin_cases i <;> fin_cases j <;> simp [Matrix.mul_apply, rg_g] <;> field_simp
  have d0 : deriv (fun t => -f t) (y 1) = -deriv f (y 1) := deriv.neg
  have d1 : deriv (fun t => (f t)⁻¹) (y 1) = -deriv f (y 1) / f (y 1) ^ 2 := (hfd.hasDerivAt.inv hf).deriv
  simp only [kr_Γ, hinv]
  fin_cases a <;> fin_cases b <;> fin_cases c <;>
    simp [kr_pd, rg_g, rg_T, Function.update_apply, d0, d1]
  all_goals field_simp

/-- A curve `τ ↦ (T(τ), R(τ))` with velocities `T′, R′` and accelerations `T″, R″` is a geodesic of `rg_g f`:
`ẍ^a + Γ^a_{bc} ẋ^b ẋ^c = 0`. -/
def rg_geodesic (f T R T' R' T'' R'' : ℝ → ℝ) : Prop :=
  (∀ τ, HasDerivAt T (T' τ) τ) ∧ (∀ τ, HasDerivAt R (R' τ) τ) ∧ (∀ τ, HasDerivAt T' (T'' τ) τ) ∧
    (∀ τ, HasDerivAt R' (R'' τ) τ) ∧
    ∀ τ, ∀ a, ![T'' τ, R'' τ] a + ∑ b, ∑ c, kr_Γ (rg_g f) ![T τ, R τ] a b c * ![T' τ, R' τ] b *
      ![T' τ, R' τ] c = 0

/-- **Row 4a.** Along a geodesic of the radial plane (with `f` differentiable and non-zero along it), the energy
`E = f(r) ṫ` is conserved; if the geodesic is unit timelike, `−fṫ² + ṙ²/f = −1`, then `ṙ² = E² − f`. -/
theorem rg_cosmo {f T R T' R' T'' R'' : ℝ → ℝ} (hg : rg_geodesic f T R T' R' T'' R'')
    (hfd : ∀ τ, DifferentiableAt ℝ f (R τ)) (hf : ∀ τ, f (R τ) ≠ 0) :
    (∀ τ, HasDerivAt (fun s => f (R s) * T' s) 0 τ) ∧
      (∃ E, ∀ τ, f (R τ) * T' τ = E) ∧
      ((∀ τ, -f (R τ) * T' τ ^ 2 + R' τ ^ 2 / f (R τ) = -1) →
        ∃ E, ∀ τ, R' τ ^ 2 = E ^ 2 - f (R τ)) := by
  obtain ⟨hT, hR, hT', hR', hgeo⟩ := hg
  have hE : ∀ τ, HasDerivAt (fun s => f (R s) * T' s) 0 τ := by
    intro τ
    have h0 := hgeo τ 0
    have hy : (![T τ, R τ] : Fin 2 → ℝ) 1 = R τ := rfl
    simp only [Fin.sum_univ_two, rg_Γ (y := ![T τ, R τ]) (hfd τ) (hf τ)] at h0
    simp [rg_T] at h0
    have hd := ((hfd τ).hasDerivAt.comp τ (hR τ)).mul (hT' τ)
    refine hd.congr_deriv ?_
    have := hf τ
    simp only [Function.comp_apply]
    field_simp at h0
    linear_combination h0 / 2
  have hconst : ∃ E, ∀ τ, f (R τ) * T' τ = E :=
    ⟨f (R 0) * T' 0, fun τ => is_const_of_deriv_eq_zero
      (fun s => (hE s).differentiableAt) (fun s => (hE s).deriv) τ 0⟩
  refine ⟨hE, hconst, fun hu => ?_⟩
  obtain ⟨E, hEc⟩ := hconst
  refine ⟨E, fun τ => ?_⟩
  have h1 := hu τ
  have h2 := hEc τ
  have := hf τ
  field_simp at h1
  rw [← h2]
  linear_combination h1

/-- **Row 4a, non-vacuity.** In Minkowski (`f ≡ 1`) the curve `t = τ`, `r = 1` is a unit timelike geodesic with
`E = 1`. -/
theorem rg_witness :
    rg_geodesic (fun _ => 1) id (fun _ => 1) (fun _ => 1) (fun _ => 0) (fun _ => 0) (fun _ => 0) ∧
      ∀ τ, -(fun _ : ℝ => (1 : ℝ)) ((fun _ : ℝ => (1 : ℝ)) τ) * (fun _ : ℝ => (1 : ℝ)) τ ^ 2 +
        (fun _ : ℝ => (0 : ℝ)) τ ^ 2 / (fun _ : ℝ => (1 : ℝ)) ((fun _ : ℝ => (1 : ℝ)) τ) = -1 := by
  refine ⟨⟨fun τ => hasDerivAt_id τ, fun τ => hasDerivAt_const τ _, fun τ => hasDerivAt_const τ _,
    fun τ => hasDerivAt_const τ _, fun τ a => ?_⟩, fun τ => by norm_num⟩
  fin_cases a <;> simp [kr_Γ, kr_pd, rg_g]

/-- **Row 4b, `E = 1`.** `r(τ) = (2Mα²)^{1/3} sinh^{2/3}(3τ/2α)` has `ṙ = √(2M/r + r²/α²)` for `τ > 0`, i.e.
`ṙ² = E² − f` with `E = 1` and `f = 1 − 2M/r − r²/α²`. -/
theorem rg_sinh23 {M α τ : ℝ} (hM : 0 < M) (hα : 0 < α) (hτ : 0 < τ) :
    HasDerivAt (fun t => (2 * M * α ^ 2 * Real.sinh (3 / (2 * α) * t) ^ 2) ^ (1 / 3 : ℝ))
      (Real.sqrt (2 * M / (2 * M * α ^ 2 * Real.sinh (3 / (2 * α) * τ) ^ 2) ^ (1 / 3 : ℝ)
        + ((2 * M * α ^ 2 * Real.sinh (3 / (2 * α) * τ) ^ 2) ^ (1 / 3 : ℝ)) ^ 2 / α ^ 2)) τ := by
  set k := 3 / (2 * α) with hk
  set S := Real.sinh (k * τ)
  set C := Real.cosh (k * τ)
  have hS : 0 < S := Real.sinh_pos_iff.2 (by positivity)
  have hC : 0 < C := Real.cosh_pos _
  set F := 2 * M * α ^ 2 * S ^ 2
  have hF : 0 < F := by positivity
  set r := F ^ (1 / 3 : ℝ)
  have hr : 0 < r := Real.rpow_pos_of_pos hF _
  have hr3 : r ^ 3 = F := by
    rw [← Real.rpow_natCast, ← Real.rpow_mul hF.le]; norm_num
  have hFd : HasDerivAt (fun t => 2 * M * α ^ 2 * Real.sinh (k * t) ^ 2)
      (2 * M * α ^ 2 * (2 * S * (C * k))) τ := by
    have := (((Real.hasDerivAt_sinh (k * τ)).comp τ ((hasDerivAt_id τ).const_mul k)).pow 2).const_mul
      (2 * M * α ^ 2)
    convert this using 1
    · funext y; simp [Function.comp_apply]
    · rw [show (Real.sinh ∘ HMul.hMul k) τ = S from rfl]; push_cast; ring
  have hrd := HasDerivAt.rpow_const (p := 1 / 3) hFd (Or.inl hF.ne')
  convert hrd using 1
  have hFr : F ^ ((1 : ℝ) / 3 - 1) = r / F := by
    rw [Real.rpow_sub hF, Real.rpow_one]
  rw [hFr]
  have hcs : C ^ 2 = 1 + S ^ 2 := by rw [Real.cosh_sq]; ring
  rw [Real.sqrt_eq_iff_mul_self_eq_of_pos (by positivity)]
  field_simp
  rw [hk]; field_simp
  have hF' : F = 2 * M * α ^ 2 * S ^ 2 := rfl
  linear_combination (4 * M ^ 2 * α ^ 4 * S ^ 2 * C ^ 2 - F ^ 2) * hr3 + 4 * M ^ 2 * α ^ 4 * S ^ 2 * F * hcs
    - (2 * M * α ^ 2 * F + F * (F + 2 * M * α ^ 2 * S ^ 2)) * hF'

/-- **Row 4b, as the radial equation.** For that `r`, `ṙ² = 1 − f(r)` with `f = 1 − 2M/r − r²/α²`. -/
theorem rg_sinh23_radial {M α τ : ℝ} (hM : 0 < M) (hα : 0 < α) (hτ : 0 < τ) :
    let r := (2 * M * α ^ 2 * Real.sinh (3 / (2 * α) * τ) ^ 2) ^ (1 / 3 : ℝ)
    deriv (fun t => (2 * M * α ^ 2 * Real.sinh (3 / (2 * α) * t) ^ 2) ^ (1 / 3 : ℝ)) τ ^ 2 =
      1 ^ 2 - (1 - 2 * M / r - r ^ 2 / α ^ 2) := by
  intro r
  have hS : 0 < Real.sinh (3 / (2 * α) * τ) := Real.sinh_pos_iff.2 (by positivity)
  have hr : 0 < r := Real.rpow_pos_of_pos (by positivity) _
  rw [(rg_sinh23 hM hα hτ).deriv, Real.sq_sqrt (by positivity)]
  ring

/-- **Row 4c, `Λ = 0`.** `r(τ) = (9Mτ²/2)^{1/3} = (9M/2)^{1/3} τ^{2/3}` has `ṙ = √(2M/r)` for `τ > 0`. -/
theorem rg_tau23 {M τ : ℝ} (hM : 0 < M) (hτ : 0 < τ) :
    HasDerivAt (fun t => (9 * M / 2 * t ^ 2) ^ (1 / 3 : ℝ))
      (Real.sqrt (2 * M / (9 * M / 2 * τ ^ 2) ^ (1 / 3 : ℝ))) τ := by
  set F := 9 * M / 2 * τ ^ 2
  have hF : 0 < F := by positivity
  set r := F ^ (1 / 3 : ℝ)
  have hr : 0 < r := Real.rpow_pos_of_pos hF _
  have hr3 : r ^ 3 = F := by
    rw [← Real.rpow_natCast, ← Real.rpow_mul hF.le]; norm_num
  have hFd : HasDerivAt (fun t => 9 * M / 2 * t ^ 2) (9 * M / 2 * (2 * τ)) τ := by
    simpa using (hasDerivAt_pow 2 τ).const_mul (9 * M / 2)
  have hrd := HasDerivAt.rpow_const (p := 1 / 3) hFd (Or.inl hF.ne')
  convert hrd using 1
  have hFr : F ^ ((1 : ℝ) / 3 - 1) = r / F := by
    rw [Real.rpow_sub hF, Real.rpow_one]
  rw [hFr]
  rw [Real.sqrt_eq_iff_mul_self_eq_of_pos (by positivity)]
  have hF' : F = 9 * M / 2 * τ ^ 2 := rfl
  field_simp
  linear_combination (81 * M * τ ^ 2) * hr3
end RgRadial

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
#print axioms ShadowProbe.StaticEinsteinProbe.ok_sds_hasDeriv
#print axioms ShadowProbe.StaticEinsteinProbe.ok_D_iff
#print axioms ShadowProbe.StaticEinsteinProbe.ok_C0_iff
#print axioms ShadowProbe.StaticEinsteinProbe.ok_Lfun_mem
#print axioms ShadowProbe.StaticEinsteinProbe.ok_Lfun_eq
#print axioms ShadowProbe.StaticEinsteinProbe.ok_invFun_deriv
#print axioms ShadowProbe.StaticEinsteinProbe.ok_invFun_mem
#print axioms ShadowProbe.StaticEinsteinProbe.es_Ric_offdiag
#print axioms ShadowProbe.StaticEinsteinProbe.es_G_offdiag
#print axioms ShadowProbe.StaticEinsteinProbe.es_sds_vacuum_full
#print axioms ShadowProbe.StaticEinsteinProbe.rg_Γ
#print axioms ShadowProbe.StaticEinsteinProbe.rg_cosmo
#print axioms ShadowProbe.StaticEinsteinProbe.rg_witness
#print axioms ShadowProbe.StaticEinsteinProbe.rg_sinh23
#print axioms ShadowProbe.StaticEinsteinProbe.rg_sinh23_radial
#print axioms ShadowProbe.StaticEinsteinProbe.rg_tau23

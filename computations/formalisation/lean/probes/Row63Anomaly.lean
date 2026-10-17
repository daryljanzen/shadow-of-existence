import ShadowEngine
import Mathlib.NumberTheory.LSeries.RiemannZeta
import Mathlib.LinearAlgebra.Matrix.Rank

/-! # Campaign 38 (`r7443+71.18`): row 63, the degeneracy needs `R` constant, not the cosh

The receipt is
`P10_the_degeneracy_needs_r_constant_not_the_cosh_so_the_anomaly_is_what_makes_its_own_constant_observable.py`.
Its sections A1, A2, A3, B, C and D (the latter in the receipt's FORMAL sense) are built here.

**Imported, not derived (labelled again at each declaration):**
- the residue `r = 15/4` and `ζ₀ = 10`, "banked" in the receipt. `r` enters only as a parameter (C is proved for every
  `r > 0`, and the instance `15/4`); `10` is *derived* here by the formal rule (`zeta_free_tower`), not assumed;
- the semiclassical renormalised energy `E = (1/a)[C + r log(aμ)]` (`rhoRen`);
- the TT spectrum `λ = m² − 1` and degeneracy `d(m) = 2(m² − 4)`, `m ≥ 3` (`dTT`, `Dtt`, `uFree`);
- the closed-FRW scalar curvature in the receipt's typed form `R = 6(ä/a + ȧ²/a² + 1/a²)` (`frwR`). The derivatives
  fed into it are derived by `HasDerivAt`, and `ä = F′(a)/2` from `ȧ² = F(a)` is proved (`addot_of_constraint`).

**Not formalised:** the paper-text parses (`pf.inline` of `12/\alpha^{2}` and `R=(4\Lambda)` from `canonical_time.tex`);
the values they parse, `12/α²` and `4Λ`, are proved (`A1_cosh`, `A3_radiation`). The genuine `ζ_Δ` (meromorphic
continuation of `Σ d(m)λ(m)^{−s}`) is not built: D is the receipt's formal rule, made an explicit definition
(`zetaRule`) and shown to be the termwise `s → 0` limit of the continued summands (`rule_is_limit`). In C the
receipt's *numbers* (the SVD ratios `s₂/s₁`, `s₃/s₁`, the floor `10⁻⁴³`, and the `r²` calibration
`(s₃/s₁)/r² ≈ 1.0179 × 10⁻⁹`) are not built; the *ranks* they measure are proved exactly.

**Receipt-internal discrepancies noticed (Lean follows the receipt's executed code and checks):**
- the docstring quotes `s₃/s₁ = 9.06 × 10⁻⁸` for the tower; the run prints `1.394 × 10⁻⁸`;
- the docstring's ⓶ gives `δ = cm ⇒ Δζ(0) = c − c³/3`; the check (at the corrected base `λ = m² − 1`) is
  `3c − c³/3`, which is what `zeta_odd` proves;
- the free-tower print label says `lam = m^2 - 3`; the code (and `uFree`) uses `λ = m² − 1`.

**The pieces, by receipt section:**
- ***A1.*** `A1_cosh`: `R = 12/α²` on `α cosh(t/α)`.
- ***A2.*** `A2_variance` (`I₂I₀ − I₁² = I₀²Var`), `A2_const` (zero on constant `F`, every weight), `A2_sign`
  (Cauchy–Schwarz sign), `A2_sample` (gap `6 > 0`).
- ***A3.*** `A3_radiation` (`R = 4Λ`), `A3_flat` (`dR/da = 0`).
- ***B.*** `B1_bare` (`ρ ∝ a⁻⁴`, `p = ρ/3`, `Θ = 0`); `B2_trace` (`Θ = r/(2π²a⁴)`, free of `μ` and `C`);
  `B3_R` (`R = 4Λ + 8πGΘ = 4Λ + 4Gr/(πa⁴)`); `B3_slope`, `B3_iff` (`dR/da ≠ 0 ↔ r ≠ 0`).
- ***C.*** BUILT, both halves. `rank_one_of_const`, `C_controls`: rank `1` when `r = 0` (both null controls).
  `moment_det_neg`, `C_tower`: rank `3` for every `r > 0`. The structural argument: the rows are moments of a
  positive weight against `1, R, R²` over three consecutive intervals, and `R = 4Λ + κ/a⁴` is strictly decreasing
  when `κ > 0`; expanding the determinant one row at a time leaves a Vandermonde `(z − y)(x − y)(x − z)` of three
  ordered values, so the determinant is strictly negative. No numerical integration is needed. `C_receipt`: the
  receipt's three instances. `adot_sq`, `Rtow_eq` tie the receipt's `ad` and `Rf` to the constraint of B3.
- ***D.*** `zetaRule` (the rule), `zeta_rule_eq` (`ζ_Δ(0) = 10 + ½B₃′(0)` for every shift, `M ≥ 3`, `J ≥ 4`),
  `Bj_zero` (`B_j(0) = 2δ_{j0} − 8δ_{j2}`), `B3_zero`; `zeta_free_tower` (`10`); `zeta_protected` (`+δ`, `×L`,
  `+b/m²`, `+b/m⁴` leave `10`); `zeta_odd` (`+cm ↦ 10 + 3c − c³/3`, `+c/m ↦ 10 − c`); `series_inputs`;
  `rule_is_limit` and `pole_term` (the pole term through `riemannZeta_residue_one`). Uses Mathlib's
  `riemannZeta_zero` (`ζ(0) = −1/2`) and `riemannZeta_neg_two_mul_nat_add_one` (`ζ(−2) = 0`). -/

namespace ShadowProbe

namespace R63Anomaly

/-! ### A. The degeneracy's exact criterion -/

section A

open Real

/-! #### A1. Closed FRW, and the cosh -/

/-- **Imported (typed, as the receipt types it in A1):** closed-FRW (`k = 1`) scalar curvature in proper time,
`R = 6(ä/a + ȧ²/a² + 1/a²)`. Not tied to the engine's connection here. -/
noncomputable def frwR (a : ℝ → ℝ) (t : ℝ) : ℝ :=
  6 * (deriv (deriv a) t / a t + deriv a t ^ 2 / a t ^ 2 + 1 / a t ^ 2)

/-- **A1.** On `a = α cosh(t/α)`, `R = 12/α²` (the value `pf.inline` parses from the paper). Derivatives by `HasDerivAt`. -/
theorem A1_cosh {α : ℝ} (hα : α ≠ 0) (t : ℝ) : frwR (fun t => α * cosh (t / α)) t = 12 / α ^ 2 := by
  have hd : ∀ t, HasDerivAt (fun t => α * cosh (t / α)) (sinh (t / α)) t := by
    intro t
    have := ((Real.hasDerivAt_cosh (t / α)).comp t ((hasDerivAt_id t).div_const α)).const_mul α
    exact this.congr_deriv (by simp; field_simp)
  have hd2 : ∀ t, HasDerivAt (fun t => sinh (t / α)) (cosh (t / α) / α) t := by
    intro t
    have := (Real.hasDerivAt_sinh (t / α)).comp t ((hasDerivAt_id t).div_const α)
    exact this.congr_deriv (by simp; ring)
  have e1 : deriv (fun t => α * cosh (t / α)) = fun t => sinh (t / α) := funext fun t => (hd t).deriv
  unfold frwR
  rw [e1, (hd2 t).deriv]
  have hc : cosh (t / α) ≠ 0 := (Real.cosh_pos _).ne'
  have hcs := Real.cosh_sq (t / α)
  field_simp
  linear_combination (-6) * hcs

/-- `ä = F′(a)/2` from the constraint `ȧ² = F(a)` -/
theorem addot_of_constraint {a F : ℝ → ℝ} {t a'' F' : ℝ} (ha : HasDerivAt a (deriv a t) t)
    (ha' : HasDerivAt (deriv a) a'' t) (hF : HasDerivAt F F' (a t))
    (hc : ∀ τ, deriv a τ ^ 2 = F (a τ)) (hne : deriv a t ≠ 0) : a'' = F' / 2 := by
  have h1 : HasDerivAt (fun τ => deriv a τ ^ 2) (2 * deriv a t * a'') t := by
    have := ha'.pow 2; convert this using 1; ring
  have h2 : HasDerivAt (fun τ => deriv a τ ^ 2) (F' * deriv a t) t := by
    have := hF.comp t ha
    rw [show (fun τ => deriv a τ ^ 2) = F ∘ a from funext hc]; exact this
  have := h1.unique h2
  field_simp
  have : deriv a t * (2 * a'' - F') = 0 := by linear_combination this
  rcases mul_eq_zero.1 this with h | h
  · exact absurd h hne
  · linarith

/-- `R` as a function of `a` on a history obeying `ȧ² = F(a)`: `ä = F′/2` (by `addot_of_constraint`) in `frwR`. -/
noncomputable def Rconstr (F : ℝ → ℝ) (a : ℝ) : ℝ := 6 * (deriv F a / 2 / a + F a / a ^ 2 + 1 / a ^ 2)

/-! #### A2. The degeneracy is `R` constant: the variance identity -/

theorem A2_variance {ι : Type*} (s : Finset ι) (w F : ι → ℝ) (h : ∑ i ∈ s, w i ≠ 0) :
    let I0 := ∑ i ∈ s, w i
    let I1 := ∑ i ∈ s, w i * F i
    let I2 := ∑ i ∈ s, w i * F i ^ 2
    I2 * I0 - I1 ^ 2 = I0 ^ 2 * ((∑ i ∈ s, w i * (F i - I1 / I0) ^ 2) / I0) := by
  intro I0 I1 I2
  have h' : I0 ≠ 0 := h
  have e : ∑ i ∈ s, w i * (F i - I1 / I0) ^ 2
      = I2 - 2 * (I1 / I0) * I1 + (I1 / I0) ^ 2 * I0 := by
    simp only [I0, I1, I2, Finset.mul_sum, ← Finset.sum_sub_distrib, ← Finset.sum_add_distrib]
    apply Finset.sum_congr rfl; intro i _; ring
  rw [e]; field_simp; ring

/-- **A2.** On constant `F` the variance vanishes, and `I₂I₀ = I₁²` for every weight. -/
theorem A2_const {ι : Type*} (s : Finset ι) (w : ι → ℝ) (F0 : ℝ) (h : ∑ i ∈ s, w i ≠ 0) :
    ∑ i ∈ s, w i * (F0 - (∑ i ∈ s, w i * F0) / ∑ i ∈ s, w i) ^ 2 = 0 ∧
    (∑ i ∈ s, w i * F0 ^ 2) * (∑ i ∈ s, w i) - (∑ i ∈ s, w i * F0) ^ 2 = 0 := by
  simp only [← Finset.sum_mul]
  constructor
  · rw [mul_div_cancel_left₀ _ h]; simp
  · ring

/-- **A2.** The gap is signed: `I₂I₀ ≥ I₁²` for nonnegative weights (Cauchy–Schwarz, via the identity). -/
theorem A2_sign {ι : Type*} (s : Finset ι) (w F : ι → ℝ) (hw : ∀ i ∈ s, 0 ≤ w i) :
    0 ≤ (∑ i ∈ s, w i * F i ^ 2) * (∑ i ∈ s, w i) - (∑ i ∈ s, w i * F i) ^ 2 := by
  rcases eq_or_lt_of_le (Finset.sum_nonneg hw) with h0 | hpos
  · rw [← h0]
    have : ∀ i ∈ s, w i = 0 := (Finset.sum_eq_zero_iff_of_nonneg hw).1 h0.symm
    have h1 : ∑ i ∈ s, w i * F i ^ 2 = 0 := Finset.sum_eq_zero (fun i hi => by rw [this i hi, zero_mul])
    have h2 : ∑ i ∈ s, w i * F i = 0 := Finset.sum_eq_zero (fun i hi => by rw [this i hi, zero_mul])
    rw [h1, h2]; simp
  · have := A2_variance s w F hpos.ne'
    simp only at this
    rw [this]
    apply mul_nonneg (sq_nonneg _)
    apply div_nonneg _ hpos.le
    exact Finset.sum_nonneg fun i hi => mul_nonneg (hw i hi) (sq_nonneg _)

/-- **A2.** The receipt's sample gap: `w = (1,1,1)`, `F = (0,1,2)` gives `6 > 0`. -/
theorem A2_sample :
    let w : Fin 3 → ℝ := ![1, 1, 1]
    let F : Fin 3 → ℝ := ![0, 1, 2]
    (∑ i, w i * F i ^ 2) * (∑ i, w i) - (∑ i, w i * F i) ^ 2 = 6 := by
  simp [Fin.sum_univ_three]; norm_num

/-! #### A3. `Λ` + radiation: `R = 4Λ` off the cosh -/

noncomputable def Frad (Λ C : ℝ) (a : ℝ) : ℝ := Λ * a ^ 2 / 3 + C / a ^ 2 - 1

theorem hasDerivAt_Frad (Λ C : ℝ) {a : ℝ} (ha : a ≠ 0) :
    HasDerivAt (Frad Λ C) (2 * Λ * a / 3 - 2 * C / a ^ 3) a := by
  have h1 := ((hasDerivAt_pow 2 a).const_mul Λ).div_const 3
  have h2 := (hasDerivAt_pow 2 a).inv (pow_ne_zero 2 ha) |>.const_mul C
  have := (h1.add h2).sub_const 1
  unfold Frad
  convert this using 1
  · funext x; simp [div_eq_mul_inv]
  · field_simp; ring

/-- **A3.** `Λ` + radiation gives `R = 4Λ` exactly, though `a` is not the cosh. -/
theorem A3_radiation (Λ C : ℝ) {a : ℝ} (ha : 0 < a) : Rconstr (Frad Λ C) a = 4 * Λ := by
  unfold Rconstr; rw [(hasDerivAt_Frad Λ C ha.ne').deriv]; unfold Frad
  field_simp; ring

/-- **A3.** `dR/da = 0`: the degeneracy survives off the cosh. -/
theorem A3_flat (Λ C : ℝ) {a : ℝ} (ha : 0 < a) : deriv (Rconstr (Frad Λ C)) a = 0 := by
  have : Rconstr (Frad Λ C) =ᶠ[nhds a] fun _ => 4 * Λ := by
    filter_upwards [Ioi_mem_nhds ha] with x hx using A3_radiation Λ C hx
  rw [this.deriv_eq]; simp

end A

/-! ### B. The tower's own trace -/

section B

open Real

/-- `p = −(a/3)ρ′ − ρ` (energy conservation `ρ + p = −(a/3)dρ/da`) -/
noncomputable def pressure (ρ : ℝ → ℝ) (a : ℝ) : ℝ := -(a / 3) * deriv ρ a - ρ a
/-- `Θ = ρ − 3p` -/
noncomputable def trace (ρ : ℝ → ℝ) (a : ℝ) : ℝ := ρ a - 3 * pressure ρ a

/-- the bare tower: `E = S/a` with `S` free of `a`, over `V = 2π²a³` -/
noncomputable def rhoBare (S : ℝ) (a : ℝ) : ℝ := S / a / (2 * π ^ 2 * a ^ 3)
/-- **Imported (semiclassical):** the renormalised energy `E = (1/a)[C + r log(aμ)]`, over `V = 2π²a³`. -/
noncomputable def rhoRen (C r μ : ℝ) (a : ℝ) : ℝ := (C + r * log (a * μ)) / a / (2 * π ^ 2 * a ^ 3)

theorem hasDerivAt_rhoBare (S : ℝ) {a : ℝ} (ha : a ≠ 0) :
    HasDerivAt (rhoBare S) (-4 * S / (2 * π ^ 2 * a ^ 5)) a := by
  have hπ : π ≠ 0 := pi_ne_zero
  have h := ((hasDerivAt_pow 4 a).inv (pow_ne_zero 4 ha)).const_mul (S / (2 * π ^ 2))
  unfold rhoBare
  convert h using 1
  · funext x
    simp only [Pi.inv_apply]
    by_cases hx : x = 0
    · simp [hx]
    · field_simp
  · field_simp; ring

/-- **B1.** The bare tower: `aρ′ = −4ρ` (`ρ ∝ a⁻⁴`), `p = ρ/3`, `Θ = 0` identically. -/
theorem B1_bare (S : ℝ) {a : ℝ} (ha : 0 < a) :
    a * deriv (rhoBare S) a = -4 * rhoBare S a ∧ pressure (rhoBare S) a = rhoBare S a / 3 ∧
    trace (rhoBare S) a = 0 := by
  have hd := (hasDerivAt_rhoBare S ha.ne').deriv
  have hπ : π ≠ 0 := pi_ne_zero
  have ha' := ha.ne'
  refine ⟨?_, ?_, ?_⟩
  · rw [hd]; unfold rhoBare; field_simp
  · unfold pressure; rw [hd]; unfold rhoBare; field_simp; ring
  · unfold trace pressure; rw [hd]; unfold rhoBare; field_simp; ring

theorem hasDerivAt_rhoRen (C r : ℝ) {μ a : ℝ} (hμ : 0 < μ) (ha : 0 < a) :
    HasDerivAt (rhoRen C r μ)
      (r / a / (2 * π ^ 2 * a ^ 4) - 4 * (C + r * log (a * μ)) / (2 * π ^ 2 * a ^ 5)) a := by
  have hπ : π ≠ 0 := pi_ne_zero
  have hlog : HasDerivAt (fun x => C + r * log (x * μ)) (r * (μ / (a * μ))) a := by
    have := ((hasDerivAt_id a).mul_const μ).log (by simpa using (mul_pos ha hμ).ne')
    simpa using (this.const_mul r).const_add C
  have hinv := (hasDerivAt_pow 4 a).inv (pow_ne_zero 4 ha.ne')
  have h := (hlog.mul hinv).div_const (2 * π ^ 2)
  simp only [Pi.inv_apply, Pi.mul_apply] at h
  unfold rhoRen
  convert h using 1
  · funext x
    by_cases hx : x = 0
    · simp [hx]
    · field_simp
  · field_simp; ring

/-- **B2.** `Θ = r/(2π²a⁴)` for every `C` and `μ > 0`: independent of `μ` and `C`, and `0` at `r = 0`. -/
theorem B2_trace (C r : ℝ) {μ a : ℝ} (hμ : 0 < μ) (ha : 0 < a) :
    trace (rhoRen C r μ) a = r / (2 * π ^ 2 * a ^ 4) := by
  unfold trace pressure; rw [(hasDerivAt_rhoRen C r hμ ha).deriv]; unfold rhoRen
  have hπ : π ≠ 0 := pi_ne_zero
  have ha' := ha.ne'
  field_simp; ring

/-- the constraint with the tower: `ȧ² = Λa²/3 − 1 + (8πG/3)ρ_ren a²` -/
noncomputable def Ftow (Λ G C r μ : ℝ) (a : ℝ) : ℝ :=
  Λ * a ^ 2 / 3 - 1 + (8 * π * G / 3) * rhoRen C r μ a * a ^ 2

/-- **B3.** `R` from the constraint equals `4Λ + 8πGΘ`, and is `4Λ + 4Gr/(πa⁴)` (no `μ`). -/
theorem B3_R (Λ G C r : ℝ) {μ a : ℝ} (hμ : 0 < μ) (ha : 0 < a) :
    Rconstr (Ftow Λ G C r μ) a = 4 * Λ + 8 * π * G * trace (rhoRen C r μ) a ∧
    Rconstr (Ftow Λ G C r μ) a = 4 * Λ + 4 * G * r / (π * a ^ 4) := by
  have hπ : π ≠ 0 := pi_ne_zero
  have ha' := ha.ne'
  have hd : HasDerivAt (Ftow Λ G C r μ)
      (2 * Λ * a / 3 + (8 * π * G / 3) * ((r / a / (2 * π ^ 2 * a ^ 4)
        - 4 * (C + r * log (a * μ)) / (2 * π ^ 2 * a ^ 5)) * a ^ 2 + rhoRen C r μ a * (2 * a))) a := by
    have h1 := ((hasDerivAt_pow 2 a).const_mul Λ).div_const 3
    have h2 := (((hasDerivAt_rhoRen C r hμ ha).mul (hasDerivAt_pow 2 a)).const_mul (8 * π * G / 3))
    have := (h1.sub_const 1).add h2
    have e : Ftow Λ G C r μ = (fun x => Λ * x ^ 2 / 3 - 1) +
        fun y => 8 * π * G / 3 * ((rhoRen C r μ * fun x : ℝ => x ^ 2 : ℝ → ℝ) y) := by
      funext x; simp only [Ftow, Pi.add_apply, Pi.mul_apply]; ring
    rw [e]
    refine this.congr_deriv ?_
    norm_num
    ring
  have hval : Rconstr (Ftow Λ G C r μ) a = 4 * Λ + 4 * G * r / (π * a ^ 4) := by
    unfold Rconstr; rw [hd.deriv]; unfold Ftow rhoRen
    field_simp; ring
  refine ⟨?_, hval⟩
  rw [hval, B2_trace C r hμ ha]; field_simp; ring

/-- **B3.** `dR/da = −16Gr/(πa⁵)`. -/
theorem B3_slope (Λ G C r : ℝ) {μ a : ℝ} (hμ : 0 < μ) (ha : 0 < a) :
    deriv (Rconstr (Ftow Λ G C r μ)) a = -16 * G * r / (π * a ^ 5) := by
  have hπ : π ≠ 0 := pi_ne_zero
  have : Rconstr (Ftow Λ G C r μ) =ᶠ[nhds a] fun x => 4 * Λ + 4 * G * r / π * (x ^ 4)⁻¹ := by
    filter_upwards [Ioi_mem_nhds ha] with x hx
    rw [(B3_R Λ G C r hμ hx).2]; field_simp
  rw [this.deriv_eq]
  have h := (((hasDerivAt_pow 4 a).inv (pow_ne_zero 4 ha.ne')).const_mul (4 * G * r / π)).const_add (4 * Λ)
  simp only [Pi.inv_apply] at h
  rw [h.deriv]; field_simp; ring

/-- **B3.** `dR/da ≠ 0 ↔ r ≠ 0` (for `G ≠ 0`, `a > 0`). -/
theorem B3_iff (Λ G C r : ℝ) {μ a : ℝ} (hG : G ≠ 0) (hμ : 0 < μ) (ha : 0 < a) :
    deriv (Rconstr (Ftow Λ G C r μ)) a ≠ 0 ↔ r ≠ 0 := by
  rw [B3_slope Λ G C r hμ ha]
  have hπ : π ≠ 0 := pi_ne_zero
  have ha' : a ^ 5 ≠ 0 := pow_ne_zero 5 ha.ne'
  constructor
  · intro h hr; apply h; simp [hr]
  · intro hr h
    rw [div_eq_zero_iff] at h
    rcases h with h | h
    · have : G * r = 0 := by linear_combination h / (-16)
      rcases mul_eq_zero.1 this with h | h
      · exact hG h
      · exact hr h
    · exact mul_ne_zero hπ ha' h

end B

/-! ### C. The rank -/

section C

open Real MeasureTheory intervalIntegral Set


/-- Rank tool (copied from `Row64Descent`): a factorisation through `k` columns plus a nonzero `k × k` minor. -/
theorem rank_eq_of_factor {m n k : ℕ} (V : Matrix (Fin m) (Fin n) ℝ) (E : Matrix (Fin m) (Fin k) ℝ)
    (C : Matrix (Fin k) (Fin n) ℝ) (hVEC : V = E * C) (r : Fin k → Fin m) (c : Fin k → Fin n)
    (hminor : (V.submatrix r c).det ≠ 0) : V.rank = k := by
  apply le_antisymm
  · rw [hVEC]; exact (Matrix.rank_mul_le_right E C).trans (Matrix.rank_le_height C)
  · have h := Matrix.rank_of_det_ne_zero hminor
    rw [Fintype.card_fin] at h
    rw [← h]; exact Matrix.rank_submatrix_le V r c

/-- the moment matrix `M i k = ∫_{I_i} w R^k` over three consecutive intervals -/
noncomputable def momentMatrix (w R : ℝ → ℝ) (x0 x1 x2 x3 : ℝ) : Matrix (Fin 3) (Fin 3) ℝ :=
  Matrix.of fun i k => ∫ a in (![x0, x1, x2] i)..(![x1, x2, x3] i), w a * R a ^ (k : ℕ)

/-- rank 1 when `R` is constant -/
theorem rank_one_of_const {w R : ℝ → ℝ} {x0 x1 x2 x3 R0 : ℝ} (hR : ∀ a, R a = R0)
    (hV : ∫ a in x0..x1, w a ≠ 0) : (momentMatrix w R x0 x1 x2 x3).rank = 1 := by
  refine rank_eq_of_factor _ (Matrix.of fun i _ => ∫ a in (![x0, x1, x2] i)..(![x1, x2, x3] i), w a)
    (Matrix.of fun _ k => R0 ^ (k : ℕ)) ?_ (fun _ => 0) (fun _ => 0) ?_
  · ext i k
    simp only [momentMatrix, Matrix.of_apply, Matrix.mul_apply, Fin.sum_univ_one, hR]
    rw [intervalIntegral.integral_mul_const]
  · simpa [Matrix.det_unique, momentMatrix] using hV

/-- linearity: `Σ c_k ∫ w R^k = ∫ w (c₀ + c₁R + c₂R²)` -/
theorem lin3 {w R : ℝ → ℝ} {p q : ℝ} (c0 c1 c2 : ℝ)
    (h0 : IntervalIntegrable (fun a => w a * R a ^ 0) volume p q)
    (h1 : IntervalIntegrable (fun a => w a * R a ^ 1) volume p q)
    (h2 : IntervalIntegrable (fun a => w a * R a ^ 2) volume p q) :
    c0 * (∫ a in p..q, w a * R a ^ 0) + c1 * (∫ a in p..q, w a * R a ^ 1) + c2 * (∫ a in p..q, w a * R a ^ 2)
      = ∫ a in p..q, w a * (c0 + c1 * R a + c2 * R a ^ 2) := by
  rw [← intervalIntegral.integral_const_mul, ← intervalIntegral.integral_const_mul,
    ← intervalIntegral.integral_const_mul,
    ← intervalIntegral.integral_add (h0.const_mul c0) (h1.const_mul c1),
    ← intervalIntegral.integral_add ((h0.const_mul c0).add (h1.const_mul c1)) (h2.const_mul c2)]
  congr 1; funext a; ring

/-- a quadratic in `R`, negative against a weight on the open interval, integrates to a negative number -/
theorem quad_neg {w R : ℝ → ℝ} {p q : ℝ} (hpq : p < q) (c0 c1 c2 : ℝ)
    (h0 : IntervalIntegrable (fun a => w a * R a ^ 0) volume p q)
    (h1 : IntervalIntegrable (fun a => w a * R a ^ 1) volume p q)
    (h2 : IntervalIntegrable (fun a => w a * R a ^ 2) volume p q)
    (hneg : ∀ a ∈ Ioo p q, w a * (c0 + c1 * R a + c2 * R a ^ 2) < 0) :
    c0 * (∫ a in p..q, w a * R a ^ 0) + c1 * (∫ a in p..q, w a * R a ^ 1)
      + c2 * (∫ a in p..q, w a * R a ^ 2) < 0 := by
  rw [lin3 c0 c1 c2 h0 h1 h2]
  have hi : IntervalIntegrable (fun a => -(w a * (c0 + c1 * R a + c2 * R a ^ 2))) volume p q := by
    have := (((h0.const_mul c0).add (h1.const_mul c1)).add (h2.const_mul c2)).neg
    refine this.congr fun a _ => ?_
    simp only [Pi.neg_apply]; ring
  have := intervalIntegral_pos_of_pos_on hi (fun a ha => neg_pos.2 (hneg a ha)) hpq
  rw [intervalIntegral.integral_neg] at this
  linarith

/-- **Rank 3, structurally.** For a weight positive on the open intervals and `R` strictly decreasing, the moment
determinant over three consecutive intervals is strictly negative. -/
theorem moment_det_neg {w R : ℝ → ℝ} {x0 x1 x2 x3 : ℝ} (h01 : x0 < x1) (h12 : x1 < x2) (h23 : x2 < x3)
    (hw : ∀ a ∈ Ioo x0 x3, 0 < w a) (hR : StrictAntiOn R (Icc x0 x3))
    (hint : ∀ k : ℕ, k ≤ 2 → IntervalIntegrable (fun a => w a * R a ^ k) volume x0 x3) :
    (momentMatrix w R x0 x1 x2 x3).det < 0 := by
  have sub : ∀ {p q : ℝ}, x0 ≤ p → p ≤ q → q ≤ x3 → ∀ k : ℕ, k ≤ 2 →
      IntervalIntegrable (fun a => w a * R a ^ k) volume p q := by
    intro p q hp hpq hq k hk
    refine (hint k hk).mono_set ?_
    rw [uIcc_of_le hpq, uIcc_of_le (by linarith)]
    exact Icc_subset_Icc hp hq
  have it := fun k hk => sub le_rfl h01.le (by linarith) k hk
  have iv := fun k hk => sub h01.le h12.le (by linarith) k hk
  have iu := fun k hk => sub (by linarith) h23.le le_rfl k hk
  have hwI : ∀ {p q : ℝ}, x0 ≤ p → q ≤ x3 → ∀ a ∈ Ioo p q, 0 < w a :=
    fun hp hq a ha => hw a ⟨by linarith [ha.1], by linarith [ha.2]⟩
  have hRlt : ∀ {a b : ℝ}, x0 ≤ a → a < b → b ≤ x3 → R b < R a :=
    fun ha hab hb => hR ⟨ha, by linarith⟩ ⟨by linarith, hb⟩ hab
  set u : ℕ → ℝ := fun k => ∫ a in x2..x3, w a * R a ^ k with hu
  set v : ℕ → ℝ := fun k => ∫ a in x1..x2, w a * R a ^ k with hv
  set t : ℕ → ℝ := fun k => ∫ a in x0..x1, w a * R a ^ k with ht
  -- row 3: the Vandermonde in `(y, z, R c)`
  have hQ : ∀ y z, R x2 ≤ z → z < y →
      (y * z ^ 2 - y ^ 2 * z) * u 0 + (y ^ 2 - z ^ 2) * u 1 + (z - y) * u 2 < 0 := by
    intro y z hz hzy
    refine quad_neg h23 _ _ _ (iu 0 (by norm_num)) (iu 1 (by norm_num)) (iu 2 (by norm_num)) ?_
    intro c hc
    have hRc : R c < R x2 := hRlt (by linarith) hc.1 (by linarith [hc.2])
    have e : (y * z ^ 2 - y ^ 2 * z) + (y ^ 2 - z ^ 2) * R c + (z - y) * R c ^ 2
        = (z - y) * (R c - y) * (R c - z) := by ring
    rw [e]
    refine mul_neg_of_pos_of_neg (hwI (by linarith) le_rfl c hc) ?_
    exact mul_neg_of_pos_of_neg (mul_pos_of_neg_of_neg (by linarith) (by linarith)) (by linarith)
  -- row 2
  have hP : ∀ y, R x1 ≤ y →
      (u 1 * y ^ 2 - u 2 * y) * v 0 + (u 2 - u 0 * y ^ 2) * v 1 + (u 0 * y - u 1) * v 2 < 0 := by
    intro y hy
    refine quad_neg h12 _ _ _ (iv 0 (by norm_num)) (iv 1 (by norm_num)) (iv 2 (by norm_num)) ?_
    intro b hb
    have h1 : R b < R x1 := hRlt h01.le hb.1 (by linarith [hb.2])
    have h2 : R x2 < R b := hRlt (by linarith [hb.1]) hb.2 h23.le
    have := hQ y (R b) h2.le (by linarith)
    refine mul_neg_of_pos_of_neg (hwI h01.le (by linarith) b hb) ?_
    linarith
  -- row 1
  have hD : (v 1 * u 2 - v 2 * u 1) * t 0 + (v 2 * u 0 - v 0 * u 2) * t 1 + (v 0 * u 1 - v 1 * u 0) * t 2 < 0 := by
    refine quad_neg h01 _ _ _ (it 0 (by norm_num)) (it 1 (by norm_num)) (it 2 (by norm_num)) ?_
    intro a ha
    have h1 : R x1 < R a := hRlt (by linarith [ha.1]) ha.2 (by linarith)
    have := hP (R a) h1.le
    refine mul_neg_of_pos_of_neg (hwI le_rfl (by linarith) a ha) ?_
    linarith
  have hdet : (momentMatrix w R x0 x1 x2 x3).det
      = (v 1 * u 2 - v 2 * u 1) * t 0 + (v 2 * u 0 - v 0 * u 2) * t 1 + (v 0 * u 1 - v 1 * u 0) * t 2 := by
    simp only [momentMatrix, Matrix.det_fin_three, Matrix.of_apply, hu, hv, ht]
    simp
    ring
  rw [hdet]; exact hD

/-- `ȧ(a)` on the semiclassical history (the receipt's `ad`) -/
noncomputable def adot (Λ G r C0 μ a : ℝ) : ℝ :=
  √(Λ * a ^ 2 / 3 - 1 + (4 * G / (3 * π)) * (C0 + r * log (a * μ)) / a ^ 2)

/-- `R = 4Λ + κ/a⁴`, `κ = 4Gr/π` (the receipt's `Rf`) -/
noncomputable def Rtow (Λ G r a : ℝ) : ℝ := 4 * Λ + (4 * G * r / π) / a ^ 4

/-- **B ↔ C.** `ȧ² = Ftow`: the receipt's `ad` is the square root of the constraint of B3. -/
theorem adot_sq (Λ G C0 r μ : ℝ) {a : ℝ} (ha : a ≠ 0) (hpos : 0 ≤ Ftow Λ G C0 r μ a) :
    adot Λ G r C0 μ a ^ 2 = Ftow Λ G C0 r μ a := by
  have e : Ftow Λ G C0 r μ a = Λ * a ^ 2 / 3 - 1 + (4 * G / (3 * π)) * (C0 + r * log (a * μ)) / a ^ 2 := by
    have hπ : π ≠ 0 := pi_ne_zero
    unfold Ftow rhoRen; field_simp; ring
  unfold adot; rw [← e, Real.sq_sqrt hpos]

/-- **B ↔ C.** The receipt's `Rf` is `R` computed from the constraint (B3). -/
theorem Rtow_eq (Λ G C0 r : ℝ) {μ a : ℝ} (hμ : 0 < μ) (ha : 0 < a) :
    Rtow Λ G r a = Rconstr (Ftow Λ G C0 r μ) a := by
  rw [(B3_R Λ G C0 r hμ ha).2]; unfold Rtow
  have hπ : π ≠ 0 := pi_ne_zero
  have := ha.ne'
  field_simp

/-- the receipt's `triples`: rows are the regions `[2,3], [3,5], [5,9]`, columns `k = 0, 1, 2` -/
noncomputable def triples (Λ G r C0 μ : ℝ) : Matrix (Fin 3) (Fin 3) ℝ :=
  Matrix.of fun i k => 2 * π ^ 2 *
    ∫ a in (![2, 3, 5] i : ℝ)..(![3, 5, 9] i : ℝ), a ^ 3 * Rtow Λ G r a ^ (k : ℕ) / adot Λ G r C0 μ a

theorem triples_eq (Λ G r C0 μ : ℝ) :
    triples Λ G r C0 μ = momentMatrix (fun a => 2 * π ^ 2 * a ^ 3 / adot Λ G r C0 μ a) (Rtow Λ G r) 2 3 5 9 := by
  ext i k
  simp only [triples, momentMatrix, Matrix.of_apply]
  rw [← intervalIntegral.integral_const_mul]
  congr 1; funext a; ring

section receipt
variable {r C0 μ : ℝ}

theorem inner_pos (hr : 0 ≤ r) (hC0 : 0 ≤ C0) (hμ : 1 ≤ μ) {a : ℝ} (ha : 2 ≤ a) :
    0 < 3 * a ^ 2 / 3 - 1 + (4 * 1 / (3 * π)) * (C0 + r * log (a * μ)) / a ^ 2 := by
  have hl : 0 ≤ log (a * μ) := Real.log_nonneg (by nlinarith)
  have : 0 ≤ (4 * 1 / (3 * π)) * (C0 + r * log (a * μ)) / a ^ 2 := by
    have := pi_pos; positivity
  nlinarith

theorem weight_cont (hr : 0 ≤ r) (hC0 : 0 ≤ C0) (hμ : 1 ≤ μ) (k : ℕ) :
    ContinuousOn (fun a => 2 * π ^ 2 * a ^ 3 / adot 3 1 r C0 μ a * Rtow 3 1 r a ^ k) (Icc 2 9) := by
  have hin : ContinuousOn (fun a : ℝ => 3 * a ^ 2 / 3 - 1 + (4 * 1 / (3 * π)) * (C0 + r * log (a * μ)) / a ^ 2)
      (Icc 2 9) := by
    apply ContinuousOn.add (by fun_prop)
    apply ContinuousOn.div _ (by fun_prop) (fun x hx => by have := hx.1; positivity)
    apply ContinuousOn.mul continuousOn_const
    apply ContinuousOn.add continuousOn_const
    apply ContinuousOn.mul continuousOn_const
    exact ContinuousOn.log (by fun_prop) (fun x hx => by have := hx.1; positivity)
  have had : ContinuousOn (adot 3 1 r C0 μ) (Icc 2 9) := Real.continuous_sqrt.comp_continuousOn hin
  apply ContinuousOn.mul
  · apply ContinuousOn.div (by fun_prop) had
    intro x hx
    exact (Real.sqrt_pos.2 (inner_pos hr hC0 hμ hx.1)).ne'
  · apply ContinuousOn.pow
    unfold Rtow
    apply ContinuousOn.add continuousOn_const
    exact ContinuousOn.div continuousOn_const (by fun_prop) (fun x hx => by have := hx.1; positivity)

theorem weight_pos (hr : 0 ≤ r) (hC0 : 0 ≤ C0) (hμ : 1 ≤ μ) {a : ℝ} (ha : 2 ≤ a) :
    0 < 2 * π ^ 2 * a ^ 3 / adot 3 1 r C0 μ a := by
  have := Real.sqrt_pos.2 (inner_pos hr hC0 hμ ha)
  have := pi_pos
  unfold adot; positivity

theorem weight_int (hr : 0 ≤ r) (hC0 : 0 ≤ C0) (hμ : 1 ≤ μ) (k : ℕ) {p q : ℝ} (hp : 2 ≤ p) (hpq : p ≤ q)
    (hq : q ≤ 9) :
    IntervalIntegrable (fun a => 2 * π ^ 2 * a ^ 3 / adot 3 1 r C0 μ a * Rtow 3 1 r a ^ k) volume p q := by
  apply ContinuousOn.intervalIntegrable
  rw [uIcc_of_le hpq]
  exact (weight_cont hr hC0 hμ k).mono (Icc_subset_Icc hp hq)

/-- **C, the null controls**: with `r = 0` (pure `Λ`, `C₀ = 0`; `Λ` + radiation, `C₀ = 1`) the triples are
parallel, rank exactly `1`. -/
theorem C_controls (hC0 : 0 ≤ C0) (hμ : 1 ≤ μ) : (triples 3 1 0 C0 μ).rank = 1 := by
  rw [triples_eq]
  refine rank_one_of_const (R0 := 12) (fun a => by simp [Rtow]; norm_num) ?_
  apply ne_of_gt
  have := intervalIntegral_pos_of_pos_on
    (weight_int le_rfl hC0 hμ 0 le_rfl (by norm_num) (by norm_num) : IntervalIntegrable _ volume 2 3)
    (fun a ha => by
      have := weight_pos le_rfl hC0 hμ (a := a) ha.1.le
      simpa using this) (by norm_num)
  simpa using this

/-- **C, the tower**: any positive anomaly coefficient makes the moment determinant strictly negative, hence
rank `3`. -/
theorem C_tower (hr : 0 < r) (hC0 : 0 ≤ C0) (hμ : 1 ≤ μ) :
    (triples 3 1 r C0 μ).det < 0 ∧ (triples 3 1 r C0 μ).rank = 3 := by
  have hdet : (triples 3 1 r C0 μ).det < 0 := by
    rw [triples_eq]
    apply moment_det_neg (by norm_num) (by norm_num) (by norm_num)
    · intro a ha; exact weight_pos hr.le hC0 hμ ha.1.le
    · intro a ha b hb hab
      have hk : 0 < 4 * 1 * r / π := by have := pi_pos; positivity
      have ha0 : 0 < a := by linarith [ha.1]
      unfold Rtow
      have : a ^ 4 < b ^ 4 := by gcongr
      have := div_lt_div_of_pos_left hk (by positivity) this
      linarith
    · intro k _
      exact weight_int hr.le hC0 hμ k le_rfl (by norm_num) le_rfl
  refine ⟨hdet, ?_⟩
  have := Matrix.rank_of_det_ne_zero hdet.ne
  simpa using this

/-- the receipt's instances: controls at `μ = 1`, `C₀ ∈ {0, 1}`; the tower at `r = 15/4`, `C₀ = 1`, `μ = 1` -/
theorem C_receipt :
    (triples 3 1 0 0 1).rank = 1 ∧ (triples 3 1 0 1 1).rank = 1 ∧ (triples 3 1 (15 / 4) 1 1).rank = 3 :=
  ⟨C_controls le_rfl le_rfl, C_controls zero_le_one le_rfl, (C_tower (by norm_num) zero_le_one le_rfl).2⟩

end receipt

end C

/-! ### D. What a shift can do to `ζ(0)`: the receipt's formal rule -/

section D

open Filter Topology


/-- the generalised binomial coefficient `(z choose k)`, by its recursion -/
noncomputable def gbinom (z : ℂ) : ℕ → ℂ
  | 0 => 1
  | k + 1 => gbinom z k * (z - k) / (k + 1)

/-- a formal power series in `x = 1/m`, as its coefficient function -/
abbrev PS := ℕ → ℂ

/-- Cauchy product -/
def psMul (f g : PS) : PS := fun n => ∑ i ∈ Finset.range (n + 1), f i * g (n - i)

/-- powers -/
def psPow (f : PS) : ℕ → PS
  | 0 => fun n => if n = 0 then 1 else 0
  | k + 1 => psMul (psPow f k) f

/-- coefficient of `x^j` in `(1 + u(x))^{−s}` (the binomial series; correct when `u 0 = 0`) -/
noncomputable def binomSer (u : PS) (s : ℂ) (j : ℕ) : ℂ :=
  ∑ k ∈ Finset.range (j + 1), gbinom (-s) k * psPow u k j

/-- `B_j(s)`: coefficient of `x^j` in `pref(s) · D(x) · (1 + u(x))^{−s}`, where `D(x) = x² d(1/x)` and
`λ(m)/m² = (prefactor) · (1 + u(1/m))`. The summand is `d(m)λ(m)^{−s} = Σ_j B_j(s) m^{2−2s−j}`. -/
noncomputable def Bcoef (pref : ℂ → ℂ) (D u : PS) (s : ℂ) (j : ℕ) : ℂ :=
  pref s * ∑ i ∈ Finset.range (j + 1), D i * binomSer u s (j - i)

/-- **Imported (the TT degeneracy):** `d(m) = 2(m² − 4)`, so `x² d(1/x) = 2 − 8x²`. -/
def Dtt : PS := fun n => if n = 0 then 2 else if n = 2 then -8 else 0

/-- **Imported:** the TT degeneracy `d(m) = 2(m² − 4)`, `m ≥ 3`. -/
def dTT (m : ℕ) : ℂ := 2 * ((m : ℂ) ^ 2 - 4)

/-- The `j`-th term of the receipt's rule: `B_j(0)(ζ(j − 2) − Σ_{m<M} m^{2−j})` for `j ≠ 3`, and the pole term
`B₃′(0)/2` at `j = 3` (`ζ(2s + 1) ∼ 1/(2s)`). `rule_is_limit` proves each is the `s → 0` limit of the summand. -/
noncomputable def ruleTerm (M : ℕ) (B : ℂ → ℕ → ℂ) (j : ℕ) : ℂ :=
  if j = 3 then deriv (fun s => B s 3) 0 / 2
  else B 0 j * (riemannZeta ((j : ℂ) - 2) - ∑ m ∈ Finset.Ico 1 M, (m : ℂ) ^ ((2 : ℤ) - j))

/-- **D, the receipt's formal rule** (`zeta_delta_at_zero`): `ζ_Δ(0) = Σ_{3≤m<M} d(m) + Σ_{j<J} ruleTerm j`. -/
noncomputable def zetaRule (M J : ℕ) (B : ℂ → ℕ → ℂ) : ℂ :=
  (∑ m ∈ Finset.Ico 3 M, dTT m) + ∑ j ∈ Finset.range J, ruleTerm M B j

/-- `d/ds (−s choose k)` at `s = 0` -/
noncomputable def dk (k : ℕ) : ℂ := if k = 0 then 0 else (-1) ^ k / k

theorem gbinom_zero_arg (k : ℕ) : gbinom 0 k = if k = 0 then 1 else 0 := by
  induction k with
  | zero => simp [gbinom]
  | succ k ih =>
    simp only [gbinom, ih]
    split_ifs with h <;> simp_all

theorem hasDerivAt_gbinom (k : ℕ) : HasDerivAt (fun s => gbinom (-s) k) (dk k) 0 := by
  induction k with
  | zero => simpa [gbinom, dk] using hasDerivAt_const (0 : ℂ) (1 : ℂ)
  | succ k ih =>
    have h1 : HasDerivAt (fun s : ℂ => (-s - k) / (k + 1)) (-1 / (k + 1)) 0 := by
      have := ((hasDerivAt_id (0 : ℂ)).neg.sub_const (k : ℂ)).div_const ((k : ℂ) + 1)
      simpa using this
    have := ih.mul h1
    simp only [gbinom]
    convert this using 1
    · funext s; simp only [Pi.mul_apply]; ring
    · rw [neg_zero, gbinom_zero_arg]
      have hk : (k : ℂ) + 1 ≠ 0 := by exact_mod_cast Nat.succ_ne_zero k
      rcases Nat.eq_zero_or_pos k with rfl | hpos
      · simp [dk]
      · have hk0 : (k : ℂ) ≠ 0 := by exact_mod_cast hpos.ne'
        simp only [dk, hpos.ne', Nat.succ_ne_zero, ite_false, Nat.cast_succ]
        field_simp
        ring

theorem psPow_zero_apply (u : PS) (j : ℕ) : psPow u 0 j = if j = 0 then 1 else 0 := rfl

theorem binomSer_zero (u : PS) (j : ℕ) : binomSer u 0 j = if j = 0 then 1 else 0 := by
  unfold binomSer
  rw [Finset.sum_eq_single 0]
  · simp [gbinom, psPow_zero_apply]
  · intro k _ hk; simp [gbinom_zero_arg, hk]
  · intro h; simp at h

theorem Bcoef_zero (pref : ℂ → ℂ) (D u : PS) (j : ℕ) : Bcoef pref D u 0 j = pref 0 * D j := by
  unfold Bcoef
  congr 1
  rw [Finset.sum_eq_single j]
  · simp [binomSer_zero]
  · intro i hi hij
    have : j - i ≠ 0 := by
      have := Finset.mem_range.1 hi; omega
    simp [binomSer_zero, this]
  · intro h; simp at h

noncomputable def ell (u : PS) (j : ℕ) : ℂ := ∑ k ∈ Finset.range (j + 1), dk k * psPow u k j

theorem hasDerivAt_binomSer (u : PS) (j : ℕ) :
    HasDerivAt (fun s => binomSer u s j) (ell u j) 0 := by
  unfold binomSer ell
  have := HasDerivAt.fun_sum (u := Finset.range (j + 1))
    (A := fun k s => gbinom (-s) k * psPow u k j) (A' := fun k => dk k * psPow u k j) (x := 0)
    (fun k _ => (hasDerivAt_gbinom k).mul_const _)
  simpa using this

theorem hasDerivAt_Bcoef {pref : ℂ → ℂ} {p' : ℂ} (hp : HasDerivAt pref p' 0) (D u : PS) (j : ℕ) :
    HasDerivAt (fun s => Bcoef pref D u s j)
      (p' * D j + pref 0 * ∑ i ∈ Finset.range (j + 1), D i * ell u (j - i)) 0 := by
  have hs : HasDerivAt (fun s => ∑ i ∈ Finset.range (j + 1), D i * binomSer u s (j - i))
      (∑ i ∈ Finset.range (j + 1), D i * ell u (j - i)) 0 :=
    HasDerivAt.fun_sum (fun i _ => (hasDerivAt_binomSer u (j - i)).const_mul (D i))
  have := hp.mul hs
  unfold Bcoef
  convert this using 1
  have h0 := Bcoef_zero pref D u j
  unfold Bcoef at h0
  rw [show (∑ i ∈ Finset.range (j + 1), D i * binomSer u 0 (j - i)) = D j by
    rw [Finset.sum_eq_single j]
    · simp [binomSer_zero]
    · intro i hi hij
      have : j - i ≠ 0 := by
        have := Finset.mem_range.1 hi; omega
      simp [binomSer_zero, this]
    · intro h; simp at h]

theorem split_point (M : ℕ) (hM : 3 ≤ M) :
    (∑ m ∈ Finset.Ico 3 M, dTT m) + 2 * (riemannZeta (-2) - ∑ m ∈ Finset.Ico 1 M, (m : ℂ) ^ 2)
      - 8 * (riemannZeta 0 - ∑ _m ∈ Finset.Ico 1 M, (1 : ℂ)) = 10 := by
  have h2 : riemannZeta (-2) = 0 := by
    have := riemannZeta_neg_two_mul_nat_add_one 0; norm_num at this; exact this
  rw [h2, riemannZeta_zero]
  induction M, hM using Nat.le_induction with
  | base => simp [Finset.sum_Ico_succ_top, dTT]; norm_num
  | succ n hn ih =>
    rw [Finset.sum_Ico_succ_top hn, Finset.sum_Ico_succ_top (by omega : 1 ≤ n),
      Finset.sum_Ico_succ_top (by omega : 1 ≤ n)]
    rw [← ih]; simp only [dTT]; ring


/-- **D, the theorem.** `ζ_Δ(0) = 10 + ½B₃′(0)` exactly, for every shift `u`, split `M ≥ 3` and truncation `J ≥ 4`;
`B₃′(0) = 2ℓ₃ − 8ℓ₁` with `ℓ_j` the `x^j` coefficient of `−log(1 + u)`. -/
theorem zeta_rule_eq {pref : ℂ → ℂ} {p' : ℂ} (hp : HasDerivAt pref p' 0) (h1 : pref 0 = 1) (u : PS)
    {M J : ℕ} (hM : 3 ≤ M) (hJ : 4 ≤ J) :
    zetaRule M J (Bcoef pref Dtt u) = 10 + (2 * ell u 3 - 8 * ell u 1) / 2 := by
  have hderiv : deriv (fun s => Bcoef pref Dtt u s 3) 0 = 2 * ell u 3 - 8 * ell u 1 := by
    rw [(hasDerivAt_Bcoef hp Dtt u 3).deriv, h1]
    simp [Dtt, Finset.sum_range_succ]; ring
  have hc : ∑ _m ∈ Finset.Ico 1 M, (1 : ℂ) = ((M - 1 : ℕ) : ℂ) := by simp
  unfold zetaRule ruleTerm
  have hsub : ({0, 2, 3} : Finset ℕ) ⊆ Finset.range J := by
    intro j hj; simp at hj; simp; omega
  rw [← Finset.sum_subset hsub]
  · simp [Bcoef_zero, h1, Dtt, hderiv]
    linear_combination split_point M hM - 8 * hc
  · intro j _ hj
    simp at hj
    simp [hj.2.2, Bcoef_zero, h1, Dtt, hj.1, hj.2.1]

/-- `B₃(0) = 0` for every shift: the receipt's guard against a pole at `s = 0`. -/
theorem B3_zero (pref : ℂ → ℂ) (u : PS) : Bcoef pref Dtt u 0 3 = 0 := by
  simp [Bcoef_zero, Dtt]

/-- `B_j(0) = 2δ_{j0} − 8δ_{j2}` whatever the shift. -/
theorem Bj_zero (pref : ℂ → ℂ) (h1 : pref 0 = 1) (u : PS) (j : ℕ) :
    Bcoef pref Dtt u 0 j = if j = 0 then 2 else if j = 2 then -8 else 0 := by
  simp [Bcoef_zero, h1, Dtt]

/-- the pole term -/
theorem pole_term {f : ℂ → ℂ} {f' : ℂ} (hf : HasDerivAt f f' 0) (h0 : f 0 = 0) :
    Tendsto (fun s => f s * riemannZeta (2 * s + 1)) (𝓝[≠] 0) (𝓝 (f' / 2)) := by
  have hslope := hf.tendsto_slope_zero
  simp only [zero_add, h0, sub_zero, smul_eq_mul] at hslope
  have hg : Tendsto (fun s : ℂ => 2 * s + 1) (𝓝[≠] 0) (𝓝[≠] 1) := by
    apply tendsto_nhdsWithin_of_tendsto_nhds_of_eventually_within
    · have : Tendsto (fun s : ℂ => 2 * s + 1) (𝓝 0) (𝓝 (2 * 0 + 1)) :=
        ((continuous_const.mul continuous_id).add continuous_const).tendsto 0
      simpa using this.mono_left nhdsWithin_le_nhds
    · filter_upwards [self_mem_nhdsWithin] with s hs
      simp only [Set.mem_compl_iff, Set.mem_singleton_iff] at hs ⊢
      intro h; apply hs; linear_combination h / 2
  have hres := riemannZeta_residue_one.comp hg
  have := (hslope.mul hres).div_const 2
  rw [mul_one] at this
  refine this.congr' ?_
  filter_upwards [self_mem_nhdsWithin] with s hs
  simp only [Set.mem_compl_iff, Set.mem_singleton_iff] at hs
  simp only [Function.comp_apply]
  field_simp
  ring

/-- the free tower: `λ/m² = 1 − x²` -/
def uFree : PS := fun n => if n = 2 then -1 else 0
/-- `λ = m² − 1 + δ` -/
def uDelta (δ : ℂ) : PS := fun n => if n = 2 then δ - 1 else 0
/-- `λ = m² − 1 + b/m²` -/
def uB2 (b : ℂ) : PS := fun n => if n = 2 then -1 else if n = 4 then b else 0
/-- `λ = m² − 1 + b/m⁴` -/
def uB4 (b : ℂ) : PS := fun n => if n = 2 then -1 else if n = 6 then b else 0
/-- `λ = m² − 1 + cm` -/
def uCm (c : ℂ) : PS := fun n => if n = 1 then c else if n = 2 then -1 else 0
/-- `λ = m² − 1 + c/m` -/
def uCinv (c : ℂ) : PS := fun n => if n = 2 then -1 else if n = 3 then c else 0

/-- the trivial prefactor -/
noncomputable def prefOne : ℂ → ℂ := fun _ => 1
/-- the rescaling `λ → Lλ`: `(Lλ/m²)^{−s} = L^{−s}(λ/m²)^{−s}` -/
noncomputable def prefL (L : ℂ) : ℂ → ℂ := fun s => L ^ (-s)

theorem hasDerivAt_one : HasDerivAt prefOne 0 0 := hasDerivAt_const _ _

theorem hasDerivAt_prefL {L : ℂ} (hL : L ≠ 0) : HasDerivAt (prefL L) (L ^ (-(0:ℂ)) * Complex.log L * (-1)) 0 :=
  (hasDerivAt_neg (0 : ℂ)).const_cpow (Or.inl hL)

theorem prefL_zero (L : ℂ) : prefL L 0 = 1 := by simp [prefL]

theorem ell_free : 2 * ell uFree 3 - 8 * ell uFree 1 = 0 := by
  simp [ell, dk, psPow, psMul, Finset.sum_range_succ, uFree]

theorem ell_cm (c : ℂ) : 2 * ell (uCm c) 3 - 8 * ell (uCm c) 1 = 6 * c - 2 * c ^ 3 / 3 := by
  simp [ell, dk, psPow, psMul, Finset.sum_range_succ, uCm]; ring1

theorem ell_cinv (c : ℂ) : 2 * ell (uCinv c) 3 - 8 * ell (uCinv c) 1 = -2 * c := by
  simp [ell, dk, psPow, psMul, Finset.sum_range_succ, uCinv]

theorem ell_delta (δ : ℂ) : 2 * ell (uDelta δ) 3 - 8 * ell (uDelta δ) 1 = 0 := by
  simp [ell, dk, psPow, psMul, Finset.sum_range_succ, uDelta]

theorem ell_b2 (b : ℂ) : 2 * ell (uB2 b) 3 - 8 * ell (uB2 b) 1 = 0 := by
  simp [ell, dk, psPow, psMul, Finset.sum_range_succ, uB2]

theorem ell_b4 (b : ℂ) : 2 * ell (uB4 b) 3 - 8 * ell (uB4 b) 1 = 0 := by
  simp [ell, dk, psPow, psMul, Finset.sum_range_succ, uB4]

/-- **D.** The free tower gives `10` (the banked `ζ₀`). -/
theorem zeta_free_tower {M J : ℕ} (hM : 3 ≤ M) (hJ : 4 ≤ J) : zetaRule M J (Bcoef prefOne Dtt uFree) = 10 := by
  rw [zeta_rule_eq hasDerivAt_one rfl uFree hM hJ, ell_free]; ring

/-- **D1.** The shifts `+δ`, `×L`, `+b/m²`, `+b/m⁴` leave `10`, for every `M ≥ 3`, `J ≥ 4`. -/
theorem zeta_protected {M J : ℕ} (hM : 3 ≤ M) (hJ : 4 ≤ J) (δ L b : ℂ) (hL : L ≠ 0) :
    zetaRule M J (Bcoef prefOne Dtt (uDelta δ)) = 10 ∧ zetaRule M J (Bcoef (prefL L) Dtt uFree) = 10 ∧
    zetaRule M J (Bcoef prefOne Dtt (uB2 b)) = 10 ∧ zetaRule M J (Bcoef prefOne Dtt (uB4 b)) = 10 := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · rw [zeta_rule_eq hasDerivAt_one rfl _ hM hJ, ell_delta]; ring
  · rw [zeta_rule_eq (hasDerivAt_prefL hL) (prefL_zero L) _ hM hJ, ell_free]; ring
  · rw [zeta_rule_eq hasDerivAt_one rfl _ hM hJ, ell_b2]; ring
  · rw [zeta_rule_eq hasDerivAt_one rfl _ hM hJ, ell_b4]; ring

/-- **D2.** `+cm` gives `10 + 3c − c³/3`; `+c/m` gives `10 − c`, for every `M ≥ 3`, `J ≥ 4`. -/
theorem zeta_odd {M J : ℕ} (hM : 3 ≤ M) (hJ : 4 ≤ J) (c : ℂ) :
    zetaRule M J (Bcoef prefOne Dtt (uCm c)) = 10 + 3 * c - c ^ 3 / 3 ∧
    zetaRule M J (Bcoef prefOne Dtt (uCinv c)) = 10 - c := by
  constructor
  · rw [zeta_rule_eq hasDerivAt_one rfl _ hM hJ, ell_cm]; ring
  · rw [zeta_rule_eq hasDerivAt_one rfl _ hM hJ, ell_cinv]; ring

/-- the series inputs are the receipt's: `x² d(1/x) = 2 − 8x²` and `λ(m)/m² = 1 + u(1/m)` -/
noncomputable def psEval (u : PS) (x : ℂ) : ℂ := ∑ n ∈ Finset.range 7, u n * x ^ n

/-- the series inputs are the receipt's: `x² d(1/x) = D(x)` and `λ(m)/m² = 1 + u(1/m)` for each family -/
theorem series_inputs (m : ℕ) (hm : m ≠ 0) (δ L b c : ℂ) :
    let x : ℂ := 1 / m
    x ^ 2 * dTT m = psEval Dtt x ∧
    ((m : ℂ) ^ 2 - 1) / m ^ 2 = 1 + psEval uFree x ∧
    ((m : ℂ) ^ 2 - 1 + δ) / m ^ 2 = 1 + psEval (uDelta δ) x ∧
    L * ((m : ℂ) ^ 2 - 1) / m ^ 2 = L * (1 + psEval uFree x) ∧
    ((m : ℂ) ^ 2 - 1 + b / m ^ 2) / m ^ 2 = 1 + psEval (uB2 b) x ∧
    ((m : ℂ) ^ 2 - 1 + b / m ^ 4) / m ^ 2 = 1 + psEval (uB4 b) x ∧
    ((m : ℂ) ^ 2 - 1 + c * m) / m ^ 2 = 1 + psEval (uCm c) x ∧
    ((m : ℂ) ^ 2 - 1 + c / m) / m ^ 2 = 1 + psEval (uCinv c) x := by
  have hm' : (m : ℂ) ≠ 0 := by exact_mod_cast hm
  intro x
  simp only [x, psEval, Finset.sum_range_succ, Finset.sum_range_zero, Dtt, uFree, uDelta, uB2, uB4, uCm,
    uCinv, dTT]
  norm_num
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;> field_simp <;> ring

/-- the `j`-th summand of the termwise-continued sum at `s` -/
noncomputable def termS (B : ℂ → ℕ → ℂ) (M j : ℕ) (s : ℂ) : ℂ :=
  B s j * (riemannZeta (2 * s + j - 2) - ∑ m ∈ Finset.Ico 1 M, (m : ℂ) ^ ((2 : ℂ) - 2 * s - j))

theorem continuousAt_psum (M j : ℕ) :
    ContinuousAt (fun s : ℂ => ∑ m ∈ Finset.Ico 1 M, (m : ℂ) ^ ((2 : ℂ) - 2 * s - j)) 0 := by
  refine (continuous_finsetSum _ fun m hm => ?_).continuousAt
  have hm0 : (m : ℂ) ≠ 0 := by
    have := (Finset.mem_Ico.1 hm).1; exact_mod_cast (by omega : m ≠ 0)
  exact ((continuous_const.sub (continuous_const.mul continuous_id)).sub
    continuous_const).const_cpow (Or.inl hm0)

theorem psum_at_zero (M j : ℕ) :
    ∑ m ∈ Finset.Ico 1 M, (m : ℂ) ^ ((2 : ℂ) - 2 * 0 - j) = ∑ m ∈ Finset.Ico 1 M, (m : ℂ) ^ ((2 : ℤ) - j) := by
  apply Finset.sum_congr rfl
  intro m _
  rw [← Complex.cpow_intCast]; push_cast; ring_nf

theorem termS_regular {B : ℂ → ℕ → ℂ} (M : ℕ) {j : ℕ} (hj : j ≠ 3) (hB : ContinuousAt (fun s => B s j) 0) :
    Tendsto (termS B M j) (𝓝[≠] 0) (𝓝 (ruleTerm M B j)) := by
  have hne : (2 * 0 + (j : ℂ) - 2) ≠ 1 := by
    intro h; apply hj
    have : (j : ℂ) = 3 := by linear_combination h
    exact_mod_cast this
  have hg : ContinuousAt (fun s : ℂ => 2 * s + j - 2) 0 := by fun_prop
  have hz : ContinuousAt (fun s : ℂ => riemannZeta (2 * s + j - 2)) 0 :=
    ContinuousAt.comp (g := riemannZeta) (f := fun s : ℂ => 2 * s + j - 2)
      (differentiableAt_riemannZeta hne).continuousAt hg
  have h : ContinuousAt (termS B M j) 0 := hB.mul (hz.sub (continuousAt_psum M j))
  have hval : ruleTerm M B j = termS B M j 0 := by
    simp only [termS, ruleTerm, hj, ite_false]
    rw [psum_at_zero, mul_zero, zero_add]
  rw [hval]
  exact h.tendsto.mono_left nhdsWithin_le_nhds

theorem termS_pole {B : ℂ → ℕ → ℂ} (M : ℕ) {b' : ℂ} (hB : HasDerivAt (fun s => B s 3) b' 0)
    (h0 : B 0 3 = 0) : Tendsto (termS B M 3) (𝓝[≠] 0) (𝓝 (ruleTerm M B 3)) := by
  have h1 := pole_term hB h0
  have h2 : Tendsto (fun s => B s 3 * ∑ m ∈ Finset.Ico 1 M, (m : ℂ) ^ ((2 : ℂ) - 2 * s - (3 : ℕ)))
      (𝓝[≠] 0) (𝓝 (B 0 3 * ∑ m ∈ Finset.Ico 1 M, (m : ℂ) ^ ((2 : ℂ) - 2 * 0 - (3 : ℕ)))) :=
    (hB.continuousAt.mul (continuousAt_psum M 3)).tendsto.mono_left nhdsWithin_le_nhds
  have := h1.sub h2
  rw [h0, zero_mul, sub_zero] at this
  have hval : ruleTerm M B 3 = b' / 2 := by simp [ruleTerm, hB.deriv]
  rw [hval]
  refine this.congr' (Eventually.of_forall fun s => ?_)
  simp only [termS]; push_cast; ring_nf

/-- **The rule is the termwise `s → 0` limit**: every summand of `zetaRule` is the limit of the continued summand. -/
theorem rule_is_limit {pref : ℂ → ℂ} {p' : ℂ} (hp : HasDerivAt pref p' 0) (D u : PS) (hD : D 3 = 0) (M j : ℕ) :
    Tendsto (termS (Bcoef pref D u) M j) (𝓝[≠] 0) (𝓝 (ruleTerm M (Bcoef pref D u) j)) := by
  by_cases hj : j = 3
  · subst hj
    exact termS_pole M (hasDerivAt_Bcoef hp D u 3) (by simp [Bcoef_zero, hD])
  · exact termS_regular M hj (hasDerivAt_Bcoef hp D u j).continuousAt

end D

end R63Anomaly

end ShadowProbe

#print axioms ShadowProbe.R63Anomaly.A1_cosh
#print axioms ShadowProbe.R63Anomaly.A2_variance
#print axioms ShadowProbe.R63Anomaly.A2_const
#print axioms ShadowProbe.R63Anomaly.A2_sign
#print axioms ShadowProbe.R63Anomaly.A2_sample
#print axioms ShadowProbe.R63Anomaly.A3_radiation
#print axioms ShadowProbe.R63Anomaly.A3_flat
#print axioms ShadowProbe.R63Anomaly.B1_bare
#print axioms ShadowProbe.R63Anomaly.B2_trace
#print axioms ShadowProbe.R63Anomaly.B3_R
#print axioms ShadowProbe.R63Anomaly.B3_slope
#print axioms ShadowProbe.R63Anomaly.B3_iff
#print axioms ShadowProbe.R63Anomaly.rank_one_of_const
#print axioms ShadowProbe.R63Anomaly.moment_det_neg
#print axioms ShadowProbe.R63Anomaly.C_controls
#print axioms ShadowProbe.R63Anomaly.C_tower
#print axioms ShadowProbe.R63Anomaly.C_receipt
#print axioms ShadowProbe.R63Anomaly.adot_sq
#print axioms ShadowProbe.R63Anomaly.Rtow_eq
#print axioms ShadowProbe.R63Anomaly.zeta_rule_eq
#print axioms ShadowProbe.R63Anomaly.Bj_zero
#print axioms ShadowProbe.R63Anomaly.B3_zero
#print axioms ShadowProbe.R63Anomaly.zeta_free_tower
#print axioms ShadowProbe.R63Anomaly.zeta_protected
#print axioms ShadowProbe.R63Anomaly.zeta_odd
#print axioms ShadowProbe.R63Anomaly.series_inputs
#print axioms ShadowProbe.R63Anomaly.rule_is_limit

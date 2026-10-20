import ShadowEngine
import Mathlib.NumberTheory.Harmonic.EulerMascheroni
import Mathlib.NumberTheory.Harmonic.ZetaAsymp
import Mathlib.LinearAlgebra.Matrix.Rank
import Mathlib.Analysis.SpecialFunctions.Log.Base

/-! # Campaign 39 (`r7443+71.22`): row 57, second order is an order the construction does not reach

The receipt is
`P10_second_order_is_an_order_the_construction_does_not_reach_and_the_one_new_direction_carries_no_new_convention.py`.
Its computed checks (A1–A3, B1, B2, the asymptotics, the harmonic sum, C and D) are built here as the receipt
computes them. Ranks are `Matrix.rank`, proved by an exhibited factorisation `V = E * C` through `k` columns (rank
`≤ k`) and an exhibited nonzero `k × k` minor (rank `≥ k`), see `rank_eq_of_factor`. The receipt's truncated
`ε`-series coefficients are `Exp3` data — `f ε = c₀ + c₁ε + c₂ε² + ε³g(ε)` with `g` continuous — and they are
unique (`Exp3.unique`), so "the order-`k` coefficient" is a well-defined object here, not a formal substitution.
Decimal `mpmath` claims are exact rational inequalities; the `ζ` probe is the genuine limit
`L·h·ζ(1 + h) → L` (from Mathlib's `riemannZeta_residue_one`), with its linear error decay as the genuine limit
`(L·h·ζ(1 + h) − L)/h → Lγ` (from `tendsto_riemannZeta_sub_one_div`). Limits are `Filter.Tendsto`.

**Imported, not derived (labelled again at each declaration):**
- the TT label weights `d(m) = 2(m² − 4)`, `μ(m) = √(m² − 1)` (`wTT`), and the control `μ² = m²` (`wCtl`);
- the FRW sectional-curvature invariant formulas in `K₁`, `K₂` as the receipt types them: `R = 6(K₁ + K₂)`,
  `λ₀ = 3K₁`, `λ₁ = K₁ + 2K₂`, `Ric² = λ₀² + 3λ₁²`, `Riem² = 12(K₁² + K₂²)`, `tr Ric³ = λ₀³ + 3λ₁³`,
  `tr Rm³ = 3K₁³ + 3K₂³`, `tr Rm⁴ = 3K₁⁴ + 3K₂⁴` (`inv6`, `inv8`), and the sectional curvatures of `H² = F(a)` as
  `K₁ = aF′/2 + F`, `K₂ = F + 1/a²` (`K1`, `K2`; `F′` itself IS derived, by `HasDerivAt`);
- the receipt's model `F = Λ/3 + εu/3 + σε²/a⁸ − 1/a²`, `u = (1 + ν log a)/a⁴` (`Fs`), and the trace's typed
  pressure `p = −ρ − aρ′/3` (`pres`, with `ρ′` derived);
- the measured `Λ = 1.1056·10⁻⁵² m⁻²` and `ℓ_P² = 2.6121·10⁻⁷⁰ m²` (`LamObs`, `ell2Obs`).

The receipt's paper-text content is not formalised. The meromorphic continuation of `Σ d(m)μ(m)m⁻ˢ` is not built
(the receipt does not do it either): face one is the `ζ`-residue statement the receipt probes numerically.

**The pieces, by receipt check:**
- ***A1.*** `turnover_unique` (one stationary point `T = 0`, second derivative `1/α > 0`, `ℓ²/a² ≤ ℓ²/α²` with equality
  only there, `= ℓ²Λ/3` at `α = √(3/Λ)`).
- ***A2.*** `eps_size` (`ε < 10⁻¹²²`, `10⁻²⁴⁶ < ε² < 10⁻²⁴⁴`, `log₁₀ ε² = 2 log₁₀ ε`).
- ***A3.*** `source_moves` (a source `σε²/a⁸` moves every `ε²` coefficient by `−2g_kΛ²σ/(9a⁸) ≠ 0`, `R³`'s by
  `−576Λ²σ/a⁸`, and no `ε¹` coefficient).
- ***B1.*** `gradient_six`, `gradient_eight` (`∂P/∂K₁ = ∂P/∂K₂ ≠ 0` at `K₁ = K₂`); `realizable_cubics` (the
  condition is `3c₀ + c₁ − c₂ − 3c₃ = 0`, it is exactly the five invariants' span, rank `3`, `K₂³` raises it to `4`).
- ***B2.*** `dK_split` (`δK₁ + δK₂ = ν/6a⁴` log-free, `δK₁ − δK₂` not); `sector_orders`; `ranks_by_order`
  (`1, 1, 2` on the six sample points); `second_direction` (the `5 × 3` log-coefficient matrix, rank `2`, spanned by
  `a⁻⁸` and `(3 + 6 log a + 4 log² a)a⁻⁸`, `R³` giving `36a⁻⁸`); `no_fourth_convention`.
- ***Asymptotics.*** `L_coeff` (`L = 15/4`).
- ***Harmonic sum.*** `harmonic_closed`, `log_coeff` (log coefficient `gL′` for any `L′`, quartic polynomial part,
  no `M⁵`).
- ***C.*** `zeta_face`; `trace_face`; `curvature_face`; `control_weight`; `faces_together`.
- ***D.*** `two_halves`; `vertex_scaled`. -/

namespace ShadowProbe

namespace R57Second

open Matrix Filter Topology

/-! ### Tools: the rank tool and unique truncated expansions -/

/-- A matrix that factors through `k` columns and has a nonzero `k × k` minor has rank exactly `k`. -/
theorem rank_eq_of_factor {m n k : ℕ} (V : Matrix (Fin m) (Fin n) ℝ) (E : Matrix (Fin m) (Fin k) ℝ)
    (C : Matrix (Fin k) (Fin n) ℝ) (hVEC : V = E * C) (r : Fin k → Fin m) (c : Fin k → Fin n)
    (hminor : (V.submatrix r c).det ≠ 0) : V.rank = k := by
  apply le_antisymm
  · rw [hVEC]; exact (Matrix.rank_mul_le_right E C).trans (Matrix.rank_le_height C)
  · have h := Matrix.rank_of_det_ne_zero hminor
    rw [Fintype.card_fin] at h
    rw [← h]; exact Matrix.rank_submatrix_le V r c

/-- `f ε = c₀ + c₁ε + c₂ε² + ε³ g(ε)` with `g` continuous: the receipt's `series(·, ε, 0, 3)` data. -/
def Exp3 (f : ℝ → ℝ) (c0 c1 c2 : ℝ) : Prop :=
  ∃ g : ℝ → ℝ, Continuous g ∧ ∀ e, f e = c0 + c1 * e + c2 * e ^ 2 + e ^ 3 * g e

theorem zero_of_continuous {φ : ℝ → ℝ} (hφ : Continuous φ) (h : ∀ e, e ≠ 0 → φ e = 0) : φ 0 = 0 := by
  have h1 : Tendsto φ (𝓝[≠] 0) (𝓝 (φ 0)) := hφ.continuousAt.tendsto.mono_left nhdsWithin_le_nhds
  have h2 : Tendsto φ (𝓝[≠] 0) (𝓝 0) := tendsto_const_nhds.congr' (by
    filter_upwards [self_mem_nhdsWithin] with e he using (h e he).symm)
  exact tendsto_nhds_unique h1 h2

/-- ⛭ **`Exp3.unique`.** The order-`0`, `1`, `2` coefficients of a truncated expansion are unique. -/
theorem Exp3.unique {f : ℝ → ℝ} {a0 a1 a2 b0 b1 b2 : ℝ} (ha : Exp3 f a0 a1 a2) (hb : Exp3 f b0 b1 b2) :
    a0 = b0 ∧ a1 = b1 ∧ a2 = b2 := by
  obtain ⟨g, hg, hfg⟩ := ha
  obtain ⟨g', hg', hfg'⟩ := hb
  have hd : ∀ e, (a0 - b0) + (a1 - b1) * e + (a2 - b2) * e ^ 2 + e ^ 3 * (g e - g' e) = 0 := by
    intro e; linear_combination hfg' e - hfg e
  have h0 : a0 = b0 := by have := hd 0; simp at this; linarith
  have h1 : a1 = b1 := by
    have := zero_of_continuous (φ := fun e => (a1 - b1) + (a2 - b2) * e + e ^ 2 * (g e - g' e))
      (by fun_prop) (fun e he => by
        have h := hd e
        have h' : e * ((a1 - b1) + (a2 - b2) * e + e ^ 2 * (g e - g' e)) = 0 := by
          rw [h0] at h; linear_combination h
        exact (mul_eq_zero.mp h').resolve_left he)
    simp at this; linarith
  have h2 : a2 = b2 := by
    have := zero_of_continuous (φ := fun e => (a2 - b2) + e * (g e - g' e))
      (by fun_prop) (fun e he => by
        have h := hd e
        have h' : e ^ 2 * ((a2 - b2) + e * (g e - g' e)) = 0 := by
          rw [h0, h1] at h; linear_combination h
        exact (mul_eq_zero.mp h').resolve_left (pow_ne_zero 2 he))
    simp at this; linarith
  exact ⟨h0, h1, h2⟩

theorem Exp3.quad (x0 x1 x2 : ℝ) : Exp3 (fun e => x0 + x1 * e + x2 * e ^ 2) x0 x1 x2 :=
  ⟨fun _ => 0, continuous_const, fun e => by ring⟩

theorem Exp3.congr {f f' : ℝ → ℝ} {a0 a1 a2 b0 b1 b2 : ℝ} (hf : Exp3 f a0 a1 a2) (h : ∀ e, f e = f' e)
    (h0 : a0 = b0) (h1 : a1 = b1) (h2 : a2 = b2) : Exp3 f' b0 b1 b2 := by
  obtain ⟨g, hg, hfg⟩ := hf
  exact ⟨g, hg, fun e => by rw [← h e, hfg e, h0, h1, h2]⟩

theorem Exp3.add {f g : ℝ → ℝ} {a0 a1 a2 b0 b1 b2 : ℝ} (hf : Exp3 f a0 a1 a2) (hg : Exp3 g b0 b1 b2) :
    Exp3 (fun e => f e + g e) (a0 + b0) (a1 + b1) (a2 + b2) := by
  obtain ⟨F, hF, hfF⟩ := hf
  obtain ⟨G, hG, hgG⟩ := hg
  exact ⟨fun e => F e + G e, hF.add hG, fun e => by beta_reduce; rw [hfF e, hgG e]; ring⟩

theorem Exp3.const_mul {f : ℝ → ℝ} {a0 a1 a2 : ℝ} (c : ℝ) (hf : Exp3 f a0 a1 a2) :
    Exp3 (fun e => c * f e) (c * a0) (c * a1) (c * a2) := by
  obtain ⟨F, hF, hfF⟩ := hf
  exact ⟨fun e => c * F e, continuous_const.mul hF, fun e => by beta_reduce; rw [hfF e]; ring⟩

theorem Exp3.mul {f g : ℝ → ℝ} {a0 a1 a2 b0 b1 b2 : ℝ} (hf : Exp3 f a0 a1 a2) (hg : Exp3 g b0 b1 b2) :
    Exp3 (fun e => f e * g e) (a0 * b0) (a0 * b1 + a1 * b0) (a0 * b2 + a1 * b1 + a2 * b0) := by
  obtain ⟨F, hF, hfF⟩ := hf
  obtain ⟨G, hG, hgG⟩ := hg
  refine ⟨fun e => a1 * b2 + a2 * b1 + a2 * b2 * e + F e * (b0 + b1 * e + b2 * e ^ 2) +
    G e * (a0 + a1 * e + a2 * e ^ 2) + e ^ 3 * F e * G e, by fun_prop, fun e => ?_⟩
  beta_reduce; rw [hfF e, hgG e]; ring

/-! ### Cubic and quartic forms in the two sectional curvatures -/

/-- the cubic form with coefficient vector `c` on `(K₁³, K₁²K₂, K₁K₂², K₂³)` -/
def cub (c : Fin 4 → ℝ) (x y : ℝ) : ℝ := c 0 * x ^ 3 + c 1 * x ^ 2 * y + c 2 * x * y ^ 2 + c 3 * y ^ 3
/-- its two partial derivatives -/
def d1c (c : Fin 4 → ℝ) (x y : ℝ) : ℝ := 3 * c 0 * x ^ 2 + 2 * c 1 * x * y + c 2 * y ^ 2
def d2c (c : Fin 4 → ℝ) (x y : ℝ) : ℝ := c 1 * x ^ 2 + 2 * c 2 * x * y + 3 * c 3 * y ^ 2
/-- the order-`2` coefficient of `cub c (x₀ + x₁ε + x₂ε² …) (y₀ + y₁ε + y₂ε² …)` -/
def o2c (c : Fin 4 → ℝ) (x0 y0 x1 y1 x2 y2 : ℝ) : ℝ :=
  d1c c x0 y0 * x2 + d2c c x0 y0 * y2 + (3 * c 0 * x0 + c 1 * y0) * x1 ^ 2 +
    (2 * c 1 * x0 + 2 * c 2 * y0) * x1 * y1 + (c 2 * x0 + 3 * c 3 * y0) * y1 ^ 2

/-- the quartic form on `(K₁⁴, K₁³K₂, K₁²K₂², K₁K₂³, K₂⁴)` and its partials -/
def qrt (c : Fin 5 → ℝ) (x y : ℝ) : ℝ :=
  c 0 * x ^ 4 + c 1 * x ^ 3 * y + c 2 * x ^ 2 * y ^ 2 + c 3 * x * y ^ 3 + c 4 * y ^ 4
def d1q (c : Fin 5 → ℝ) (x y : ℝ) : ℝ := 4 * c 0 * x ^ 3 + 3 * c 1 * x ^ 2 * y + 2 * c 2 * x * y ^ 2 + c 3 * y ^ 3
def d2q (c : Fin 5 → ℝ) (x y : ℝ) : ℝ := c 1 * x ^ 3 + 2 * c 2 * x ^ 2 * y + 3 * c 3 * x * y ^ 2 + 4 * c 4 * y ^ 3

/-- ⛭ **`Exp3.cubic`.** A cubic form of two expansions expands with the gradient at order `1` and the gradient
plus half the Hessian at order `2`. -/
theorem Exp3.cubic {x y : ℝ → ℝ} {x0 x1 x2 y0 y1 y2 : ℝ} (c : Fin 4 → ℝ) (hx : Exp3 x x0 x1 x2)
    (hy : Exp3 y y0 y1 y2) :
    Exp3 (fun e => cub c (x e) (y e)) (cub c x0 y0) (d1c c x0 y0 * x1 + d2c c x0 y0 * y1)
      (o2c c x0 y0 x1 y1 x2 y2) := by
  have h := (((((hx.mul hx).mul hx).const_mul (c 0)).add (((hx.mul hx).mul hy).const_mul (c 1))).add
    (((hx.mul hy).mul hy).const_mul (c 2))).add (((hy.mul hy).mul hy).const_mul (c 3))
  refine h.congr (fun e => by simp only [cub]; ring) (by simp only [cub]; ring)
    (by simp only [d1c, d2c]; ring) (by simp only [o2c, d1c, d2c]; ring)

theorem cub_d1 (c : Fin 4 → ℝ) (x y : ℝ) : HasDerivAt (fun x => cub c x y) (d1c c x y) x := by
  have h := ((((hasDerivAt_pow 3 x).const_mul (c 0)).add ((hasDerivAt_pow 2 x).const_mul (c 1 * y))).add
    ((hasDerivAt_id x).const_mul (c 2 * y ^ 2))).add_const (c 3 * y ^ 3)
  convert h using 1
  · funext x; simp only [cub, id, Pi.add_apply]; ring
  · simp only [d1c]; norm_num; ring

theorem cub_d2 (c : Fin 4 → ℝ) (x y : ℝ) : HasDerivAt (fun y => cub c x y) (d2c c x y) y := by
  have h := ((((hasDerivAt_pow 3 y).const_mul (c 3)).add ((hasDerivAt_pow 2 y).const_mul (c 2 * x))).add
    ((hasDerivAt_id y).const_mul (c 1 * x ^ 2))).add_const (c 0 * x ^ 3)
  convert h using 1
  · funext y; simp only [cub, id, Pi.add_apply]; ring
  · simp only [d2c]; norm_num; ring

theorem qrt_d1 (c : Fin 5 → ℝ) (x y : ℝ) : HasDerivAt (fun x => qrt c x y) (d1q c x y) x := by
  have h := (((((hasDerivAt_pow 4 x).const_mul (c 0)).add ((hasDerivAt_pow 3 x).const_mul (c 1 * y))).add
    ((hasDerivAt_pow 2 x).const_mul (c 2 * y ^ 2))).add ((hasDerivAt_id x).const_mul (c 3 * y ^ 3))).add_const
    (c 4 * y ^ 4)
  convert h using 1
  · funext x; simp only [qrt, id, Pi.add_apply]; ring
  · simp only [d1q]; norm_num; ring

theorem qrt_d2 (c : Fin 5 → ℝ) (x y : ℝ) : HasDerivAt (fun y => qrt c x y) (d2q c x y) y := by
  have h := (((((hasDerivAt_pow 4 y).const_mul (c 4)).add ((hasDerivAt_pow 3 y).const_mul (c 3 * x))).add
    ((hasDerivAt_pow 2 y).const_mul (c 2 * x ^ 2))).add ((hasDerivAt_id y).const_mul (c 1 * x ^ 3))).add_const
    (c 0 * x ^ 4)
  convert h using 1
  · funext y; simp only [qrt, id, Pi.add_apply]; ring
  · simp only [d2q]; norm_num; ring


/-! ### A. Is second order in the back-reaction reached at all? -/

section A

/-- the substrate member `a(T) = α cosh(T/α)` -/
noncomputable def aCosh (α T : ℝ) : ℝ := α * Real.cosh (T / α)

theorem aCosh_deriv (α : ℝ) (hα : 0 < α) (T : ℝ) : HasDerivAt (aCosh α) (Real.sinh (T / α)) T := by
  have hd : HasDerivAt (fun T : ℝ => T / α) (1 / α) T := (hasDerivAt_id T).div_const α
  have := ((Real.hasDerivAt_cosh (T / α)).comp T hd).const_mul α
  convert this using 1
  · funext y; simp [aCosh]
  · field_simp

/-- ⛭ **`turnover_unique`** (A1). `α cosh(T/α)` has exactly ONE stationary point, `T = 0`, with second derivative
`1/α > 0` there; the expansion parameter `ℓ²/a²` is at most `ℓ²/α²`, with equality exactly at `T = 0`; and with
`α = √(3/Λ)` that maximum is `ℓ²Λ/3`. -/
theorem turnover_unique (α ℓ : ℝ) (hα : 0 < α) (hℓ : ℓ ≠ 0) :
    deriv (aCosh α) = (fun T => Real.sinh (T / α)) ∧
    {T | deriv (aCosh α) T = 0} = {0} ∧
    HasDerivAt (deriv (aCosh α)) (1 / α) 0 ∧ 0 < 1 / α ∧
    (∀ T, ℓ ^ 2 / aCosh α T ^ 2 ≤ ℓ ^ 2 / α ^ 2) ∧
    (∀ T, ℓ ^ 2 / aCosh α T ^ 2 = ℓ ^ 2 / α ^ 2 ↔ T = 0) ∧
    (∀ Λ : ℝ, 0 < Λ → α = Real.sqrt (3 / Λ) → ℓ ^ 2 / α ^ 2 = ℓ ^ 2 * Λ / 3) := by
  have hder : deriv (aCosh α) = (fun T => Real.sinh (T / α)) := funext fun T => (aCosh_deriv α hα T).deriv
  have hge : ∀ T, α ≤ aCosh α T := fun T => by
    have := Real.one_le_cosh (T / α); simp only [aCosh]; nlinarith
  refine ⟨hder, ?_, ?_, by positivity, fun T => ?_, fun T => ?_, fun Λ hΛ hαΛ => ?_⟩
  · ext T; simp [hder, hα.ne']
  · rw [hder]
    have hd : HasDerivAt (fun T : ℝ => T / α) (1 / α) 0 := (hasDerivAt_id (0 : ℝ)).div_const α
    have := (Real.hasDerivAt_sinh (0 / α)).comp 0 hd
    convert this using 1 <;> simp [Function.comp_def]
  · have h1 := hge T
    apply div_le_div_of_nonneg_left (sq_nonneg ℓ) (by positivity)
    nlinarith
  · have hl : 0 < ℓ ^ 2 := by positivity
    have hA : 0 < aCosh α T := lt_of_lt_of_le hα (hge T)
    constructor
    · intro h
      have h2 : aCosh α T ^ 2 = α ^ 2 := by
        field_simp at h; nlinarith
      have h3 : Real.cosh (T / α) = 1 := by
        simp only [aCosh] at h2
        have hc := Real.cosh_pos (T / α)
        have : (Real.cosh (T / α) - 1) * (Real.cosh (T / α) + 1) * α ^ 2 = 0 := by linear_combination h2
        rcases mul_eq_zero.mp this with h | h
        · rcases mul_eq_zero.mp h with h | h
          · linarith
          · linarith
        · exact absurd h (by positivity)
      by_contra hT
      have := Real.one_lt_cosh.mpr (div_ne_zero hT hα.ne')
      linarith
    · rintro rfl; simp [aCosh]
  · rw [hαΛ, Real.sq_sqrt (by positivity)]; field_simp

/-- **Imported (measured):** `Λ = 1.1056·10⁻⁵² m⁻²` and `ℓ_P² = 2.6121·10⁻⁷⁰ m²`, as exact rationals. -/
noncomputable def LamObs : ℝ := 11056 / 10 ^ 56
noncomputable def ell2Obs : ℝ := 26121 / 10 ^ 74
/-- the parameter's maximum `ε_max = Λℓ²/3` on the measured inputs -/
noncomputable def epsMax : ℝ := LamObs * ell2Obs / 3

/-- ⛭ **`eps_size`** (A2). `10⁻¹²³ < ε_max < 10⁻¹²²`, `10⁻²⁴⁶ < ε_max² < 10⁻²⁴⁴`, and `log₁₀ ε_max² = 2 log₁₀ ε_max`
exactly (the receipt's "square of the first to machine precision"). -/
theorem eps_size :
    1 / 10 ^ 123 < epsMax ∧ epsMax < 1 / 10 ^ 122 ∧ 1 / 10 ^ 246 < epsMax ^ 2 ∧ epsMax ^ 2 < 1 / 10 ^ 244 ∧
    Real.logb 10 (epsMax ^ 2) = 2 * Real.logb 10 epsMax := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · norm_num [epsMax, LamObs, ell2Obs]
  · norm_num [epsMax, LamObs, ell2Obs]
  · norm_num [epsMax, LamObs, ell2Obs]
  · norm_num [epsMax, LamObs, ell2Obs]
  · rw [Real.logb_pow]; push_cast; ring

/-- **Imported (the receipt's model):** `F = Λ/3 + εu/3 + σε²/a⁸ − 1/a²`, `u = (1 + ν log a)/a⁴`; `σ` is the
independent second-order source (`σ = 0` is the construction's own). -/
noncomputable def Fs (Λ ε ν σ a : ℝ) : ℝ :=
  Λ / 3 + ε * ((1 + ν * Real.log a) / a ^ 4) / 3 + σ * ε ^ 2 / a ^ 8 - 1 / a ^ 2
noncomputable def Fs' (ε ν σ a : ℝ) : ℝ :=
  ε * (ν - 4 - 4 * ν * Real.log a) / (3 * a ^ 5) - 8 * σ * ε ^ 2 / a ^ 9 + 2 / a ^ 3

theorem Fs_deriv (Λ ε ν σ : ℝ) {a : ℝ} (ha : 0 < a) : HasDerivAt (Fs Λ ε ν σ) (Fs' ε ν σ a) a := by
  have h1 := (((((Real.hasDerivAt_log ha.ne').const_mul ν).const_add 1).div (hasDerivAt_pow 4 a)
    (by positivity)).const_mul ε).div_const 3
  have h2 := ((hasDerivAt_pow 8 a).inv (by positivity)).const_mul (σ * ε ^ 2)
  have h3 := (hasDerivAt_pow 2 a).inv (by positivity)
  have h := ((h1.const_add (Λ / 3)).add h2).sub h3
  convert h using 1
  · funext x; simp only [Fs, Pi.sub_apply, Pi.add_apply, Pi.div_apply, Pi.inv_apply]; ring
  · simp only [Fs']; norm_num; field_simp; ring

/-- **Imported (typed):** the two sectional curvatures of `H² = F(a)`, `K₁ = aF′/2 + F` and `K₂ = F + 1/a²`, with
`F′` the DERIVED derivative (`Fs_deriv`) -/
noncomputable def K1 (Λ ε ν σ a : ℝ) : ℝ := a * Fs' ε ν σ a / 2 + Fs Λ ε ν σ a
noncomputable def K2 (Λ ε ν σ a : ℝ) : ℝ := Fs Λ ε ν σ a + 1 / a ^ 2
noncomputable def Sa (ν a : ℝ) : ℝ := ν / (6 * a ^ 4)
noncomputable def Aa (ν a : ℝ) : ℝ := (ν - 2 - 2 * ν * Real.log a) / (6 * a ^ 4)
noncomputable def Qa (ν a : ℝ) : ℝ := Aa ν a ^ 2 - Sa ν a * Aa ν a + Sa ν a ^ 2

theorem K1_eq (Λ ε ν σ : ℝ) {a : ℝ} (ha : 0 < a) :
    K1 Λ ε ν σ a = Λ / 3 + Aa ν a * ε + (-3 * σ / a ^ 8) * ε ^ 2 := by
  simp only [K1, Fs, Fs', Aa]; field_simp; ring

theorem K2_eq (Λ ε ν σ : ℝ) {a : ℝ} (ha : 0 < a) :
    K2 Λ ε ν σ a = Λ / 3 + (Sa ν a - Aa ν a) * ε + (σ / a ^ 8) * ε ^ 2 := by
  simp only [K2, Fs, Sa, Aa]; field_simp; ring

theorem K1_exp (Λ ν σ : ℝ) {a : ℝ} (ha : 0 < a) :
    Exp3 (fun ε => K1 Λ ε ν σ a) (Λ / 3) (Aa ν a) (-3 * σ / a ^ 8) :=
  (Exp3.quad _ _ _).congr (fun e => (K1_eq Λ e ν σ ha).symm) rfl rfl rfl

theorem K2_exp (Λ ν σ : ℝ) {a : ℝ} (ha : 0 < a) :
    Exp3 (fun ε => K2 Λ ε ν σ a) (Λ / 3) (Sa ν a - Aa ν a) (σ / a ^ 8) :=
  (Exp3.quad _ _ _).congr (fun e => (K2_eq Λ e ν σ ha).symm) rfl rfl rfl

/-- **Imported (the receipt's typed invariant formulas in `K₁`, `K₂`)** -/
def Rs (x y : ℝ) : ℝ := 6 * (x + y)
def lam0 (x : ℝ) : ℝ := 3 * x
def lam1 (x y : ℝ) : ℝ := x + 2 * y
def Ric2 (x y : ℝ) : ℝ := lam0 x ^ 2 + 3 * lam1 x y ^ 2
def Riem2 (x y : ℝ) : ℝ := 12 * (x ^ 2 + y ^ 2)
/-- the five dimension-six invariants `R³, R·Ric², R·Riem², tr Ric³, tr Rm³` -/
def inv6 (x y : ℝ) : Fin 5 → ℝ :=
  ![Rs x y ^ 3, Rs x y * Ric2 x y, Rs x y * Riem2 x y, lam0 x ^ 3 + 3 * lam1 x y ^ 3, 3 * x ^ 3 + 3 * y ^ 3]
/-- the four dimension-eight invariants `R⁴, R²·Ric², (Ric²)², tr Rm⁴` -/
def inv8 (x y : ℝ) : Fin 4 → ℝ :=
  ![Rs x y ^ 4, Rs x y ^ 2 * Ric2 x y, Ric2 x y ^ 2, 3 * x ^ 4 + 3 * y ^ 4]

/-- their coefficient vectors (the receipt's `Msix` rows) -/
def row6 : Fin 5 → Fin 4 → ℝ :=
  ![![216, 648, 648, 216], ![72, 144, 144, 72], ![72, 72, 72, 72], ![30, 18, 36, 24], ![3, 0, 0, 3]]
def row8 : Fin 4 → Fin 5 → ℝ :=
  ![![1296, 5184, 7776, 5184, 1296], ![432, 1296, 1728, 1296, 432], ![144, 288, 432, 288, 144], ![3, 0, 0, 0, 3]]

theorem inv6_cub (x y : ℝ) (k : Fin 5) : inv6 x y k = cub (row6 k) x y := by
  fin_cases k <;> simp [inv6, cub, row6, Rs, Ric2, Riem2, lam0, lam1] <;> ring

theorem inv8_qrt (x y : ℝ) (k : Fin 4) : inv8 x y k = qrt (row8 k) x y := by
  fin_cases k <;> simp [inv8, qrt, row8, Rs, Ric2, lam0, lam1] <;> ring

/-- the invariants on the receipt's geometry, with source `σ` -/
noncomputable def invG (Λ ε ν σ a : ℝ) (k : Fin 5) : ℝ := inv6 (K1 Λ ε ν σ a) (K2 Λ ε ν σ a) k

/-- the common gradient `∂P/∂K₁ = ∂P/∂K₂` at the symmetric point `(K, K)`, over `K²` -/
def g6 : Fin 5 → ℝ := ![2592, 648, 432, 162, 9]
def g8 : Fin 4 → ℝ := ![41472, 10368, 2592, 12]

/-- the order coefficients of the construction's own invariants (`σ = 0`) and the source's shift -/
noncomputable def P0 (Λ : ℝ) (k : Fin 5) : ℝ := cub (row6 k) (Λ / 3) (Λ / 3)
noncomputable def P1 (Λ ν a : ℝ) (k : Fin 5) : ℝ :=
  d1c (row6 k) (Λ / 3) (Λ / 3) * Aa ν a + d2c (row6 k) (Λ / 3) (Λ / 3) * (Sa ν a - Aa ν a)
noncomputable def P2 (Λ ν a : ℝ) (k : Fin 5) : ℝ := o2c (row6 k) (Λ / 3) (Λ / 3) (Aa ν a) (Sa ν a - Aa ν a) 0 0

/-- ⛭ **`inv_exp`.** Each invariant on the geometry expands as `P₀ + P₁ε + (P₂ − 2g_kΛ²σ/(9a⁸))ε² + O(ε³)`. -/
theorem inv_exp (Λ ν σ : ℝ) {a : ℝ} (ha : 0 < a) (k : Fin 5) :
    Exp3 (fun ε => invG Λ ε ν σ a k) (P0 Λ k) (P1 Λ ν a k) (P2 Λ ν a k - 2 * g6 k * Λ ^ 2 * σ / (9 * a ^ 8)) :=
  (Exp3.cubic (row6 k) (K1_exp Λ ν σ ha) (K2_exp Λ ν σ ha)).congr
    (fun e => (inv6_cub _ _ k).symm) rfl rfl
    (by fin_cases k <;> simp [o2c, P2, d1c, d2c, row6, g6] <;> field_simp <;> ring)

/-- ⛭ **`source_moves`** (A3). Whatever coefficients one reads off, an independent second-order source `σε²/a⁸`
leaves orders `0` and `1` of every invariant untouched and moves every order-`2` coefficient by
`−2g_kΛ²σ/(9a⁸)`, nonzero for `σ, Λ ≠ 0` — `R³`'s by `−576Λ²σ/a⁸`. -/
theorem source_moves (Λ ν σ : ℝ) {a : ℝ} (ha : 0 < a) (k : Fin 5) :
    (∀ c0 c1 c2 d0 d1 d2 : ℝ, Exp3 (fun ε => invG Λ ε ν σ a k) c0 c1 c2 →
      Exp3 (fun ε => invG Λ ε ν 0 a k) d0 d1 d2 →
      c0 = d0 ∧ c1 = d1 ∧ c2 - d2 = -2 * g6 k * Λ ^ 2 * σ / (9 * a ^ 8)) ∧
    (σ ≠ 0 → Λ ≠ 0 → -2 * g6 k * Λ ^ 2 * σ / (9 * a ^ 8) ≠ 0) ∧
    -2 * g6 0 * Λ ^ 2 * σ / (9 * a ^ 8) = -576 * Λ ^ 2 * σ / a ^ 8 := by
  refine ⟨fun c0 c1 c2 d0 d1 d2 hc hd => ?_, fun hσ hΛ => ?_, ?_⟩
  · obtain ⟨u0, u1, u2⟩ := Exp3.unique hc (inv_exp Λ ν σ ha k)
    obtain ⟨v0, v1, v2⟩ := Exp3.unique hd (inv_exp Λ ν 0 ha k)
    refine ⟨u0.trans v0.symm, u1.trans v1.symm, ?_⟩
    rw [u2, v2]; ring
  · have : g6 k ≠ 0 := by fin_cases k <;> norm_num [g6]
    have : 0 < a ^ 8 := by positivity
    field_simp
    simp [*, ha.ne']
  · simp [g6]; field_simp; ring

end A

/-! ### B1. The gradient condition and the realizable cubics -/

section B1

/-- ⛭ **`gradient_six`** (B1). At `K₁ = K₂ = K` every dimension-six invariant has `∂P/∂K₁ = ∂P/∂K₂ = g_k K²`
with `g_k ≠ 0`: a degeneracy of the gradient, not a vanishing of it. -/
theorem gradient_six (k : Fin 5) (K : ℝ) :
    HasDerivAt (fun x => inv6 x K k) (g6 k * K ^ 2) K ∧ HasDerivAt (fun y => inv6 K y k) (g6 k * K ^ 2) K ∧
    g6 k ≠ 0 := by
  have e1 : (fun x => inv6 x K k) = fun x => cub (row6 k) x K := funext fun x => inv6_cub x K k
  have e2 : (fun y => inv6 K y k) = fun y => cub (row6 k) K y := funext fun y => inv6_cub K y k
  refine ⟨?_, ?_, by fin_cases k <;> norm_num [g6]⟩
  · rw [e1]; convert cub_d1 (row6 k) K K using 1; simp only [d1c]; fin_cases k <;> norm_num [row6, g6] <;> ring
  · rw [e2]; convert cub_d2 (row6 k) K K using 1; simp only [d2c]; fin_cases k <;> norm_num [row6, g6] <;> ring

/-- ⛭ **`gradient_eight`** (B1). The same at dimension eight: `∂P/∂K₁ = ∂P/∂K₂ = g_k K³`, `g_k ≠ 0`. -/
theorem gradient_eight (k : Fin 4) (K : ℝ) :
    HasDerivAt (fun x => inv8 x K k) (g8 k * K ^ 3) K ∧ HasDerivAt (fun y => inv8 K y k) (g8 k * K ^ 3) K ∧
    g8 k ≠ 0 := by
  have e1 : (fun x => inv8 x K k) = fun x => qrt (row8 k) x K := funext fun x => inv8_qrt x K k
  have e2 : (fun y => inv8 K y k) = fun y => qrt (row8 k) K y := funext fun y => inv8_qrt K y k
  refine ⟨?_, ?_, by fin_cases k <;> norm_num [g8]⟩
  · rw [e1]; convert qrt_d1 (row8 k) K K using 1; simp only [d1q]; fin_cases k <;> norm_num [row8, g8] <;> ring
  · rw [e2]; convert qrt_d2 (row8 k) K K using 1; simp only [d2q]; fin_cases k <;> norm_num [row8, g8] <;> ring

/-- the gradient condition on a cubic, `3c₀ + c₁ − c₂ − 3c₃` -/
def cond (c : Fin 4 → ℝ) : ℝ := 3 * c 0 + c 1 - c 2 - 3 * c 3

/-- the `5 × 4` coefficient matrix, and with the control `K₂³` adjoined -/
def Msix : Matrix (Fin 5) (Fin 4) ℝ := Matrix.of row6
def Maug : Matrix (Fin 6) (Fin 4) ℝ := Matrix.of ![row6 0, row6 1, row6 2, row6 3, row6 4, ![0, 0, 0, 1]]

/-- ⛭ **`realizable_cubics`** (B1). For a general cubic `∂₁P − ∂₂P = K² (3c₀ + c₁ − c₂ − 3c₃)` at `(K, K)`, so the
gradient condition is exactly that hyperplane; the five invariants satisfy it and SPAN it (every cubic satisfying
it is a combination of their rows); their matrix has rank `3`; `K₂³` violates it and adjoining it raises the rank
to `4`. -/
theorem realizable_cubics :
    (∀ c : Fin 4 → ℝ, ∀ K : ℝ, d1c c K K - d2c c K K = K ^ 2 * cond c) ∧
    (∀ c : Fin 4 → ℝ, (∀ K : ℝ, d1c c K K = d2c c K K) ↔ cond c = 0) ∧
    (∀ k, cond (row6 k) = 0) ∧
    (∀ c : Fin 4 → ℝ, cond c = 0 ↔ ∃ w : Fin 5 → ℝ, c = Matrix.vecMul w Msix) ∧
    Msix.rank = 3 ∧ cond ![0, 0, 0, 1] ≠ 0 ∧ Maug.rank = Msix.rank + 1 := by
  have hid : ∀ c : Fin 4 → ℝ, ∀ K : ℝ, d1c c K K - d2c c K K = K ^ 2 * cond c := by
    intro c K; simp only [d1c, d2c, cond]; ring
  have hrank : Msix.rank = 3 := by
    refine rank_eq_of_factor Msix (Matrix.of fun k => ![row6 k 0, row6 k 2, row6 k 3])
      !![1, -3, 0, 0; 0, 1, 1, 0; 0, 3, 0, 1] ?_ ![2, 3, 4] ![0, 2, 3] ?_
    · ext k j; simp only [Msix, Matrix.mul_apply, Matrix.of_apply, Fin.sum_univ_three]
      fin_cases k <;> fin_cases j <;> norm_num [row6]
    · rw [Matrix.det_fin_three]; simp [Msix, row6]; norm_num
  refine ⟨hid, fun c => ⟨fun h => ?_, fun h K => ?_⟩, ?_, fun c => ⟨fun h => ?_, ?_⟩, hrank, ?_, ?_⟩
  · have := hid c 1; rw [h 1] at this; linarith
  · have := hid c K; rw [h] at this; linarith
  · intro k; fin_cases k <;> norm_num [cond, row6]
  · refine ⟨![0, 0, (c 2 - 6 * (c 0 - c 3)) / 72, (c 0 - c 3) / 6, (2 * c 0 - c 2 - c 3) / 3], ?_⟩
    simp only [cond] at h
    funext j; fin_cases j <;> simp [Matrix.vecMul, dotProduct, Fin.sum_univ_five, Msix, row6] <;> linarith
  · rintro ⟨w, rfl⟩
    simp [cond, Matrix.vecMul, dotProduct, Fin.sum_univ_five, Msix, row6]; ring
  · simp [cond]
  · rw [hrank]
    refine rank_eq_of_factor Maug Maug 1 (Matrix.mul_one _).symm ![2, 3, 4, 5] id ?_
    have hsub : Maug.submatrix ![2, 3, 4, 5] id = !![72, 72, 72, 72; 30, 18, 36, 24; 3, 0, 0, 3; 0, 0, 0, 1] := by
      ext i j; fin_cases i <;> fin_cases j <;> simp [Maug, row6]
    rw [hsub, Matrix.det_succ_row_zero]
    simp [Fin.sum_univ_succ, Matrix.det_fin_three, Matrix.submatrix_apply, Fin.succAbove]
    norm_num

end B1


/-! ### B2. What the first order can do, and what the second adds -/

section B2

/-- ⛭ **`dK_split`** (B2). Whatever first-order coefficients `δK₁`, `δK₂` one reads off, `δK₁ + δK₂ = ν/6a⁴`
carries NO logarithm, while `δK₁ − δK₂ = (ν − 4 − 4ν log a)/6a⁴` does: `a⁴(δK₁ − δK₂)` differs between `a = 1` and
`a = e` whenever `ν ≠ 0`. -/
theorem dK_split (Λ ν σ : ℝ) {a : ℝ} (ha : 0 < a) :
    (∀ c0 c1 c2 d0 d1 d2 : ℝ, Exp3 (fun ε => K1 Λ ε ν σ a) c0 c1 c2 → Exp3 (fun ε => K2 Λ ε ν σ a) d0 d1 d2 →
      c1 + d1 = ν / (6 * a ^ 4) ∧ c1 - d1 = (ν - 4 - 4 * ν * Real.log a) / (6 * a ^ 4)) ∧
    (ν ≠ 0 → (1 : ℝ) ^ 4 * ((ν - 4 - 4 * ν * Real.log 1) / (6 * 1 ^ 4)) ≠
      Real.exp 1 ^ 4 * ((ν - 4 - 4 * ν * Real.log (Real.exp 1)) / (6 * Real.exp 1 ^ 4))) := by
  refine ⟨fun c0 c1 c2 d0 d1 d2 hc hd => ?_, fun hν => ?_⟩
  · obtain ⟨-, u1, -⟩ := Exp3.unique hc (K1_exp Λ ν σ ha)
    obtain ⟨-, v1, -⟩ := Exp3.unique hd (K2_exp Λ ν σ ha)
    rw [u1, v1]; simp only [Sa, Aa]
    constructor <;> field_simp <;> ring
  · rw [Real.log_one, Real.log_exp]
    have he : Real.exp 1 ^ 4 * ((ν - 4 - 4 * ν * 1) / (6 * Real.exp 1 ^ 4)) = (ν - 4 - 4 * ν) / 6 := by
      have := Real.exp_pos 1
      field_simp
    rw [he]; intro h; apply hν; linarith

/-- ⛭ **`sector_orders`** (B2, the mechanism). For EVERY realizable cubic (`3c₀ + c₁ − c₂ − 3c₃ = 0`) at the
symmetric point `K = Λ/3`, the order-`1` coefficient is a multiple of `S = δK₁ + δK₂` alone, and the order-`2`
coefficient lies in the span of `S²` and `Q = A² − SA + S²`. -/
theorem sector_orders (c : Fin 4 → ℝ) (hc : cond c = 0) (Λ S A : ℝ) :
    d1c c (Λ / 3) (Λ / 3) * A + d2c c (Λ / 3) (Λ / 3) * (S - A) = (3 * c 0 + 2 * c 1 + c 2) * (Λ / 3) ^ 2 * S ∧
    o2c c (Λ / 3) (Λ / 3) A (S - A) 0 0 = Λ / 3 * (-3 * c 0 + c 1 + 2 * c 2) * S ^ 2 +
      Λ / 3 * (3 * c 0 - c 1 - c 2 + 3 * c 3) * (A ^ 2 - S * A + S ^ 2) := by
  simp only [cond] at hc
  constructor
  · simp only [d1c, d2c]; linear_combination ((Λ / 3) ^ 2 * (A - S)) * hc
  · simp only [o2c, d1c, d2c]; linear_combination (A * (Λ / 3) * S) * hc

/-- the `S²` and `Q` amplitudes of the five invariants' order-`2` coefficients, over `Λ` -/
def al : Fin 5 → ℝ := ![432, 72, 0, 0, -3]
def be : Fin 5 → ℝ := ![0, 48, 96, 36, 6]

theorem P_closed (Λ ν a : ℝ) (k : Fin 5) :
    P1 Λ ν a k = g6 k * Λ ^ 2 / 9 * Sa ν a ∧ P2 Λ ν a k = al k * Λ * Sa ν a ^ 2 + be k * Λ * Qa ν a := by
  have hk := realizable_cubics.2.2.1 k
  obtain ⟨h1, h2⟩ := sector_orders (row6 k) hk Λ (Sa ν a) (Aa ν a)
  constructor
  · have e1 : 3 * row6 k 0 + 2 * row6 k 1 + row6 k 2 = g6 k := by fin_cases k <;> norm_num [row6, g6]
    simp only [P1]; rw [h1, e1]; ring
  · have ea : -3 * row6 k 0 + row6 k 1 + 2 * row6 k 2 = 3 * al k := by fin_cases k <;> norm_num [row6, al]
    have eb : 3 * row6 k 0 - row6 k 1 - row6 k 2 + 3 * row6 k 3 = 3 * be k := by
      fin_cases k <;> norm_num [row6, be]
    simp only [P2, Qa]; rw [h2, ea, eb]; ring

/-- the receipt's six sample points `a = 1, 3/2, …, 7/2` -/
noncomputable def pts : Fin 6 → ℝ := ![1, 3 / 2, 2, 5 / 2, 3, 7 / 2]

/-- the order-`0`, `1`, `2` value matrices at `ν = 1`, `Λ = 3`, as the receipt samples them -/
noncomputable def Mo0 : Matrix (Fin 6) (Fin 5) ℝ := Matrix.of fun _ k => P0 3 k
noncomputable def Mo1 : Matrix (Fin 6) (Fin 5) ℝ := Matrix.of fun i k => P1 3 1 (pts i) k
noncomputable def Mo2 : Matrix (Fin 6) (Fin 5) ℝ := Matrix.of fun i k => P2 3 1 (pts i) k

/-- ⛭ **`ranks_by_order`** (B2). The value ranks over the five invariants at the six points are `1, 1, 2` at
orders `0, 1, 2`. -/
theorem ranks_by_order : Mo0.rank = 1 ∧ Mo1.rank = 1 ∧ Mo2.rank = 2 := by
  refine ⟨?_, ?_, ?_⟩
  · refine rank_eq_of_factor Mo0 (Matrix.of fun _ _ => 1) (Matrix.of fun _ k => P0 3 k) ?_ ![0] ![0] ?_
    · ext i k; simp [Mo0, Matrix.mul_apply]
    · rw [Matrix.det_unique]; simp [Mo0, P0, cub, row6]; norm_num
  · refine rank_eq_of_factor Mo1 (Matrix.of fun i _ => Sa 1 (pts i)) (Matrix.of fun _ k => g6 k) ?_ ![0] ![0] ?_
    · ext i k; simp [Mo1, Matrix.mul_apply, (P_closed 3 1 (pts i) k).1]; ring
    · rw [Matrix.det_unique]; simp [Mo1, (P_closed 3 1 _ _).1, g6, Sa, pts]
  · refine rank_eq_of_factor Mo2 (Matrix.of fun i => ![Sa 1 (pts i) ^ 2, Qa 1 (pts i)])
      !![1296, 216, 0, 0, -9; 0, 144, 288, 108, 18] ?_ ![0, 2] ![0, 2] ?_
    · ext i k; simp only [Mo2, Matrix.mul_apply, Matrix.of_apply, Fin.sum_univ_two, (P_closed 3 1 _ _).2]
      fin_cases k <;> simp [al, be] <;> ring
    · have hl := Real.log_pos (by norm_num : (1 : ℝ) < 2)
      rw [Matrix.det_fin_two]
      simp [Mo2, (P_closed 3 1 _ _).2, al, be, Qa, Sa, Aa, pts]
      nlinarith [mul_pos hl hl]

/-- the receipt's `Mf`: the coefficients of `1, log a, log² a` in `a⁸ ×` each order-`2` value (`ν = 1`, `Λ = 3`) -/
noncomputable def Mf : Matrix (Fin 5) (Fin 3) ℝ :=
  Matrix.of ![![36, 0, 0], ![18, 24, 16], ![24, 48, 32], ![9, 18, 12], ![5 / 4, 3, 2]]
/-- the two spanning vectors: the plain `a⁻⁸` and the squared-logarithm combination `(3 + 6 log a + 4 log² a)a⁻⁸` -/
def Espan : Matrix (Fin 2) (Fin 3) ℝ := !![1, 0, 0; 3, 6, 4]

/-- ⛭ **`second_direction`** (B2). `a⁸ × order 2 = Mf₀ + Mf₁ log a + Mf₂ log² a` for every invariant and every
`a > 0`; `Mf` factors as `(al/12, be/12) · Espan` — every value decomposes into the plain `a⁻⁸` and the single
combination `3 + 6 log a + 4 log² a` — `Mf` and `Espan` both have rank `2`, and `R³` gives `36 a⁻⁸` with no
logarithm. ⇒ exactly ONE new direction. -/
theorem second_direction :
    (∀ a : ℝ, 0 < a → ∀ k, a ^ 8 * P2 3 1 a k = Mf k 0 + Mf k 1 * Real.log a + Mf k 2 * Real.log a ^ 2) ∧
    Mf = (Matrix.of fun k => ![al k / 12, be k / 12]) * Espan ∧
    Mf.rank = 2 ∧ Espan.rank = 2 ∧ (∀ j, Mf 0 j = 36 * ![1, 0, 0] j) := by
  have hfac : Mf = (Matrix.of fun k => ![al k / 12, be k / 12]) * Espan := by
    ext k j; simp only [Matrix.mul_apply, Matrix.of_apply, Fin.sum_univ_two]
    fin_cases k <;> fin_cases j <;> simp [Mf, Espan, al, be] <;> norm_num
  refine ⟨fun a ha k => ?_, hfac, ?_, ?_, fun j => ?_⟩
  · rw [(P_closed 3 1 a k).2]
    simp only [Sa, Qa, Aa]
    fin_cases k <;> simp [Mf, al, be] <;> field_simp <;> ring
  · refine rank_eq_of_factor Mf _ _ hfac ![0, 1] ![0, 1] ?_
    rw [Matrix.det_fin_two]; simp [Mf]
  · refine rank_eq_of_factor Espan 1 Espan (Matrix.one_mul _).symm ![0, 1] ![0, 1] ?_
    rw [Matrix.det_fin_two]; simp [Espan]
  · fin_cases j <;> simp [Mf]

end B2

/-! ### C. The banked number: one object with four faces -/

section C

/-- **Imported:** the TT label weights `d(m)μ(m) = 2(m² − 4)√(m² − 1)`, a function of the label `m` alone (no scale
factor enters). -/
noncomputable def wTT (m : ℝ) : ℝ := 2 * (m ^ 2 - 4) * Real.sqrt (m ^ 2 - 1)

/-- ⛭ **`L_coeff`** (asymptotics). `d(m)μ(m) = 2m³ − 9m + L/m + o(1/m)` with `L = 15/4`, as a limit; behind it the
exact identity `m(dμ − 2m³ + 9m) = 8r − r²`, `r = m/(m + √(m² − 1)) → 1/2`, for `m ≥ 1`. -/
theorem L_coeff : Tendsto (fun m : ℝ => m * (wTT m - (2 * m ^ 3 - 9 * m))) atTop (𝓝 (15 / 4)) := by
  have key : ∀ m : ℝ, 1 ≤ m → m * (wTT m - (2 * m ^ 3 - 9 * m)) =
      8 * (m / (m + Real.sqrt (m ^ 2 - 1))) - (m / (m + Real.sqrt (m ^ 2 - 1))) ^ 2 := by
    intro m hm
    have hs : Real.sqrt (m ^ 2 - 1) ^ 2 = m ^ 2 - 1 := Real.sq_sqrt (by nlinarith)
    have hs0 := Real.sqrt_nonneg (m ^ 2 - 1)
    have hp : 0 < m + Real.sqrt (m ^ 2 - 1) := by linarith
    rw [show 8 * (m / (m + Real.sqrt (m ^ 2 - 1))) - (m / (m + Real.sqrt (m ^ 2 - 1))) ^ 2
        = (8 * m * (m + Real.sqrt (m ^ 2 - 1)) - m ^ 2) / (m + Real.sqrt (m ^ 2 - 1)) ^ 2 by
          field_simp, eq_div_iff (by positivity)]
    simp only [wTT]
    linear_combination (2 * m ^ 4 - 7 * m ^ 2 + Real.sqrt (m ^ 2 - 1) * (2 * m ^ 3 - 8 * m)) * hs
  have hr : Tendsto (fun m : ℝ => m / (m + Real.sqrt (m ^ 2 - 1))) atTop (𝓝 (1 / 2)) := by
    have h1 : Tendsto (fun m : ℝ => Real.sqrt (1 - (m⁻¹) ^ 2)) atTop (𝓝 1) := by
      simpa using ((tendsto_inv_atTop_zero.pow 2).const_sub (1 : ℝ)).sqrt
    have h2 := (h1.const_add 1).inv₀ (by norm_num)
    norm_num at h2
    refine h2.congr' ?_
    filter_upwards [eventually_ge_atTop 1] with m hm
    have hm0 : 0 < m := by linarith
    have : Real.sqrt (m ^ 2 - 1) = m * Real.sqrt (1 - (m⁻¹) ^ 2) := by
      rw [show m ^ 2 - 1 = m ^ 2 * (1 - (m⁻¹) ^ 2) by field_simp, Real.sqrt_mul (sq_nonneg m),
        Real.sqrt_sq hm0.le]
    rw [this]
    have := Real.sqrt_nonneg (1 - (m⁻¹) ^ 2)
    field_simp
  have h3 := (hr.const_mul 8).sub (hr.pow 2)
  norm_num at h3
  refine h3.congr' ?_
  filter_upwards [eventually_ge_atTop 1] with m hm
  rw [key m hm]

/-- the partial sum `Σ_{m=3}^{M} (2m³ − 9m + L′/m)` with a general `1/m` term `L′`, and its quartic part -/
noncomputable def SsumL (Lp : ℝ) (M : ℕ) : ℝ := ∑ m ∈ Finset.Icc 3 M, (2 * (m : ℝ) ^ 3 - 9 * m + Lp / m)
noncomputable def Ppoly (M : ℝ) : ℝ := M ^ 4 / 2 + M ^ 3 - 4 * M ^ 2 - 9 * M / 2 + 9

/-- ⛭ **`harmonic_closed`** (harmonic sum). `Σ_{m=3}^{M}(2m³ − 9m + L′/m) = P(M) + L′(H_M − 3/2)` exactly, with
`P(M) = M⁴/2 + M³ − 4M² − 9M/2 + 9` a quartic: NO `M⁵` term. -/
theorem harmonic_closed (Lp : ℝ) (M : ℕ) (hM : 2 ≤ M) :
    SsumL Lp M = Ppoly M + Lp * ((harmonic M : ℝ) - 3 / 2) := by
  induction M, hM using Nat.le_induction with
  | base => simp [SsumL, Ppoly, harmonic, Finset.sum_range_succ]; norm_num
  | succ n hn ih =>
    rw [SsumL, Finset.sum_Icc_succ_top (by omega), ← SsumL, ih, harmonic_succ]
    have : (0 : ℝ) < n + 1 := by positivity
    simp only [Ppoly]; push_cast; field_simp; ring

/-- ⛭ **`log_coeff`** (harmonic sum, `H_M → log M + γ` as a genuine limit). For ANY moment `g` and any `1/m`
term `L′`, `g·S_M − g·P(M) − gL′ log M → gL′(γ − 3/2)`: the logarithm's coefficient is exactly `gL′`. -/
theorem log_coeff (g Lp : ℝ) :
    Tendsto (fun M : ℕ => g * SsumL Lp M - g * Ppoly M - g * Lp * Real.log M) atTop
      (𝓝 (g * Lp * (Real.eulerMascheroniConstant - 3 / 2))) := by
  have h := (Real.tendsto_harmonic_sub_log.sub_const (3 / 2 : ℝ)).const_mul (g * Lp)
  refine h.congr' ?_
  filter_upwards [eventually_ge_atTop 2] with M hM
  rw [harmonic_closed Lp M hM]; ring

/-- ⛭ **`no_fourth_convention`** (B2's last check). The weight is a function of the label alone; with any moment
`g` in front the sum's divergent structures are the quartic `g·P(M)` (no `M⁵`) and `gL log M` with `L = 15/4`, and
the first-order value rank is `1`. -/
theorem no_fourth_convention (g : ℝ) :
    (∀ M : ℕ, 2 ≤ M → g * SsumL (15 / 4) M = g * Ppoly M + g * (15 / 4) * ((harmonic M : ℝ) - 3 / 2)) ∧
    Tendsto (fun M : ℕ => g * SsumL (15 / 4) M - g * Ppoly M - g * (15 / 4) * Real.log M) atTop
      (𝓝 (g * (15 / 4) * (Real.eulerMascheroniConstant - 3 / 2))) ∧
    Mo1.rank = 1 := by
  refine ⟨fun M hM => by rw [harmonic_closed _ M hM]; ring, log_coeff g _, ranks_by_order.2.1⟩

/-- ⛭ **`zeta_face`** (C, face one; replaces the receipt's `mpmath` probe). For any residue `c`,
`c·h·ζ(1 + h) → c` as `h → 0`, and the error falls linearly: `(c·h·ζ(1 + h) − c)/h → cγ`. The receipt's two
readings are `c = 15/4` (the `s = 0` pole) and `c = 2` (the `s = 4` pole). -/
theorem zeta_face (c : ℂ) :
    Tendsto (fun h : ℂ => c * h * riemannZeta (1 + h)) (𝓝[≠] 0) (𝓝 c) ∧
    Tendsto (fun h : ℂ => (c * h * riemannZeta (1 + h) - c) / h) (𝓝[≠] 0)
      (𝓝 (c * Real.eulerMascheroniConstant)) := by
  have hmap : Tendsto (fun h : ℂ => 1 + h) (𝓝[≠] 0) (𝓝[≠] 1) := by
    apply tendsto_nhdsWithin_of_tendsto_nhds_of_eventually_within
    · have : Tendsto (fun h : ℂ => 1 + h) (𝓝 0) (𝓝 (1 + 0)) := tendsto_const_nhds.add tendsto_id
      rw [add_zero] at this
      exact this.mono_left nhdsWithin_le_nhds
    · filter_upwards [self_mem_nhdsWithin] with h hh
      simpa using hh
  refine ⟨?_, ?_⟩
  · have h1 := (riemannZeta_residue_one.comp hmap).const_mul c
    rw [mul_one] at h1
    refine h1.congr fun h => ?_
    simp only [Function.comp_apply, add_sub_cancel_left]; ring
  · have h2 := (tendsto_riemannZeta_sub_one_div.comp hmap).const_mul c
    refine h2.congr' ?_
    filter_upwards [self_mem_nhdsWithin] with h (hh : h ≠ 0)
    simp only [Function.comp_apply, add_sub_cancel_left]
    field_simp

/-- the anomaly's energy density `ρ = L′ log a/a⁴` and its derived derivative -/
noncomputable def rhoL (Lp a : ℝ) : ℝ := Lp * Real.log a / a ^ 4
noncomputable def rhoL' (Lp a : ℝ) : ℝ := Lp * (1 - 4 * Real.log a) / a ^ 5
/-- **Imported (typed):** the pressure `p = −ρ − aρ′/3` (the receipt's `trace`) -/
noncomputable def pres (rho rho' a : ℝ) : ℝ := -rho - a * rho' / 3

/-- ⛭ **`trace_face`** (C, face three). `ρ′ = L′(1 − 4 log a)/a⁵` and the trace `ρ − 3p = L′/a⁴`. -/
theorem trace_face (Lp : ℝ) {a : ℝ} (ha : 0 < a) :
    HasDerivAt (rhoL Lp) (rhoL' Lp a) a ∧ rhoL Lp a - 3 * pres (rhoL Lp a) (rhoL' Lp a) a = Lp / a ^ 4 := by
  refine ⟨?_, ?_⟩
  · have h := ((Real.hasDerivAt_log ha.ne').const_mul Lp).div (hasDerivAt_pow 4 a) (by positivity)
    convert h using 1
    · funext x; simp [rhoL]
    · simp only [rhoL']; norm_num; field_simp
  · simp only [rhoL, rhoL', pres]; field_simp; ring

/-- ⛭ **`curvature_face`** (C, face four). On the construction's geometry `R = 6(K₁ + K₂) = 4Λ + εν/a⁴`; with the
amplitude off (`ν = 0`) `R = 4Λ` exactly; with `ν = L′` the `a⁻⁴` coefficient of `(R − 4Λ)/ε` is `L′`. -/
theorem curvature_face (Λ ε ν Lp : ℝ) {a : ℝ} (ha : 0 < a) :
    Rs (K1 Λ ε ν 0 a) (K2 Λ ε ν 0 a) = 4 * Λ + ε * ν / a ^ 4 ∧
    Rs (K1 Λ ε 0 0 a) (K2 Λ ε 0 0 a) = 4 * Λ ∧
    (ε ≠ 0 → (Rs (K1 Λ ε Lp 0 a) (K2 Λ ε Lp 0 a) - 4 * Λ) / ε * a ^ 4 = Lp) := by
  have hR : ∀ ν, Rs (K1 Λ ε ν 0 a) (K2 Λ ε ν 0 a) = 4 * Λ + ε * ν / a ^ 4 := by
    intro ν; rw [K1_eq Λ ε ν 0 ha, K2_eq Λ ε ν 0 ha]; simp only [Rs, Sa]; field_simp; ring
  refine ⟨hR ν, by rw [hR 0]; ring, fun hε => ?_⟩
  rw [hR Lp]; field_simp; ring

/-- **Imported (control):** the weight at `μ² = m²`, `2(m² − 4)√(m²)` -/
noncomputable def wCtl (m : ℝ) : ℝ := 2 * (m ^ 2 - 4) * Real.sqrt (m ^ 2)

/-- ⛭ **`control_weight`** (C). The control has NO `1/m` term (`m(w − 2m³ + 8m) → 0`, indeed `= 0` for `m ≥ 0`), its
sum is the polynomial `M⁴/2 + M³ − 7M²/2 − 4M + 6` — no harmonic number, no logarithm — and with `L′ = 0` there is
no anomaly. -/
theorem control_weight :
    (∀ m : ℝ, 0 ≤ m → wCtl m = 2 * m ^ 3 - 8 * m) ∧
    Tendsto (fun m : ℝ => m * (wCtl m - (2 * m ^ 3 - 8 * m))) atTop (𝓝 0) ∧
    (∀ M : ℕ, 2 ≤ M → ∑ m ∈ Finset.Icc 3 M, wCtl m = (M : ℝ) ^ 4 / 2 + M ^ 3 - 7 * M ^ 2 / 2 - 4 * M + 6) ∧
    (∀ a : ℝ, rhoL 0 a - 3 * pres (rhoL 0 a) (rhoL' 0 a) a = 0) := by
  have hw : ∀ m : ℝ, 0 ≤ m → wCtl m = 2 * m ^ 3 - 8 * m := by
    intro m hm; simp only [wCtl, Real.sqrt_sq hm]; ring
  refine ⟨hw, ?_, fun M hM => ?_, fun a => by simp [rhoL, rhoL', pres]⟩
  · refine tendsto_const_nhds.congr' ?_
    filter_upwards [eventually_ge_atTop 0] with m hm
    rw [hw m hm]; ring
  · induction M, hM using Nat.le_induction with
    | base => norm_num
    | succ n hn ih =>
      rw [Finset.sum_Icc_succ_top (by omega), ih, hw _ (by positivity)]
      push_cast; ring

/-- ⛭ **`faces_together`** (C). Change the weight's `1/m` term to an arbitrary `L′`: the partial sum's logarithm,
the trace's `a⁻⁴` and the curvature scalar's `a⁻⁴` all carry `L′`; at the TT weight's own `L = 15/4` (`L_coeff`)
all three are `15/4` — one rational, named once. -/
theorem faces_together (Lp : ℝ) :
    Tendsto (fun M : ℕ => SsumL Lp M - Ppoly M - Lp * Real.log M) atTop
      (𝓝 (Lp * (Real.eulerMascheroniConstant - 3 / 2))) ∧
    (∀ a : ℝ, 0 < a → (rhoL Lp a - 3 * pres (rhoL Lp a) (rhoL' Lp a) a) * a ^ 4 = Lp) ∧
    (∀ Λ ε a : ℝ, 0 < a → ε ≠ 0 → (Rs (K1 Λ ε Lp 0 a) (K2 Λ ε Lp 0 a) - 4 * Λ) / ε * a ^ 4 = Lp) ∧
    Tendsto (fun m : ℝ => m * (wTT m - (2 * m ^ 3 - 9 * m))) atTop (𝓝 (15 / 4)) := by
  refine ⟨by simpa using log_coeff 1 Lp, fun a ha => ?_, fun Λ ε a ha hε => (curvature_face Λ ε Lp Lp ha).2.2 hε,
    L_coeff⟩
  rw [(trace_face Lp ha).2]; field_simp

end C

/-! ### D. What this leaves -/

section D

/-- ⛭ **`two_halves`** (D). The order-dependence is real as arithmetic (rank `1 → 2`) and sits at a relative size
below `10⁻²⁴⁴`. -/
theorem two_halves : Mo1.rank < Mo2.rank ∧ epsMax ^ 2 < 1 / 10 ^ 244 := by
  rw [ranks_by_order.2.1, ranks_by_order.2.2]
  exact ⟨by norm_num, eps_size.2.2.2.1⟩

/-- ⛭ **`vertex_scaled`** (D). Carry an unknown vertex factor `A₆ ≠ 0`: every order coefficient is `A₆` times the
old one, both value ranks are unchanged (`1` and `2`), and the logarithm's coefficient is `A₆L`. -/
theorem vertex_scaled (A6 : ℝ) (hA6 : A6 ≠ 0) (Λ ν σ : ℝ) {a : ℝ} (ha : 0 < a) (k : Fin 5) :
    Exp3 (fun ε => A6 * invG Λ ε ν σ a k) (A6 * P0 Λ k) (A6 * P1 Λ ν a k)
      (A6 * (P2 Λ ν a k - 2 * g6 k * Λ ^ 2 * σ / (9 * a ^ 8))) ∧
    (A6 • Mo1).rank = 1 ∧ (A6 • Mo2).rank = 2 ∧
    Tendsto (fun M : ℕ => A6 * SsumL (15 / 4) M - A6 * Ppoly M - A6 * (15 / 4) * Real.log M) atTop
      (𝓝 (A6 * (15 / 4) * (Real.eulerMascheroniConstant - 3 / 2))) := by
  have hc : A6 ∈ nonZeroDivisors ℝ := mem_nonZeroDivisors_of_ne_zero hA6
  refine ⟨(inv_exp Λ ν σ ha k).const_mul A6, ?_, ?_, log_coeff A6 _⟩
  · rw [Matrix.rank_smul_of_mem_nonZeroDivisors _ hc]; exact ranks_by_order.2.1
  · rw [Matrix.rank_smul_of_mem_nonZeroDivisors _ hc]; exact ranks_by_order.2.2

end D

end R57Second

end ShadowProbe

#print axioms ShadowProbe.R57Second.rank_eq_of_factor
#print axioms ShadowProbe.R57Second.Exp3.unique
#print axioms ShadowProbe.R57Second.Exp3.cubic
#print axioms ShadowProbe.R57Second.turnover_unique
#print axioms ShadowProbe.R57Second.eps_size
#print axioms ShadowProbe.R57Second.inv_exp
#print axioms ShadowProbe.R57Second.source_moves
#print axioms ShadowProbe.R57Second.gradient_six
#print axioms ShadowProbe.R57Second.gradient_eight
#print axioms ShadowProbe.R57Second.realizable_cubics
#print axioms ShadowProbe.R57Second.dK_split
#print axioms ShadowProbe.R57Second.sector_orders
#print axioms ShadowProbe.R57Second.P_closed
#print axioms ShadowProbe.R57Second.ranks_by_order
#print axioms ShadowProbe.R57Second.second_direction
#print axioms ShadowProbe.R57Second.L_coeff
#print axioms ShadowProbe.R57Second.harmonic_closed
#print axioms ShadowProbe.R57Second.log_coeff
#print axioms ShadowProbe.R57Second.no_fourth_convention
#print axioms ShadowProbe.R57Second.zeta_face
#print axioms ShadowProbe.R57Second.trace_face
#print axioms ShadowProbe.R57Second.curvature_face
#print axioms ShadowProbe.R57Second.control_weight
#print axioms ShadowProbe.R57Second.faces_together
#print axioms ShadowProbe.R57Second.two_halves
#print axioms ShadowProbe.R57Second.vertex_scaled

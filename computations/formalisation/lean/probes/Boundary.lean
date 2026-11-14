import Mathlib

/-!
# Probe `r7765+71.2` (campaign 139): P13's conjugation parity, conjugation closure and residue

Registration: `computations/formalisation/r7765_71_campaign139/PREDICTION.md`; inventory
`computations/formalisation/r7763_71_survey/SURVEY.md`. Nothing imports this file, and it imports only Mathlib. It is
a new probe, prefix `bd_`, so it is P13's citable file (`corpus/boundary_paper.tex`). P7's row-7c section of
`Framework.lean` (`fw_y`, `fw_τ` and their lemmas through `fw_τ_cont`) is copied verbatim below, names kept.

`f(r) = 1 − 2M/r + Q²/r² − Λr²/3`; `R: (r, M) ↦ (−r, −M)`; `K: z ↦ z̄`.

* **Row 2a — BUILT.** `bd_parity`.
* **Row 2b — BUILT.** `bd_charge_even`.
* **Row 3a — BUILT.** `bd_R_isometry`, `bd_Q_blind`.
* **Row 3b — BUILT.** `bd_K_bead`, `bd_K_antilinear`.
* **Row 3c — BUILT.** `bd_K_wings`.
* **Row 3d — BUILT.** `bd_RK`.
* **Row 4i — BUILT.** `bd_conj_rep`, `bd_neg_one_not_weyl`.
* **Row 4iii — BUILT.** `bd_null_swap`.
* **Row 4iv — BUILT.** `bd_R_fixed`.
* **Row 1 (`prop:boundary`'s non-embedding) — NOT BEGUN**, priced as beyond.
-/

open Real Filter Topology Set

namespace ShadowProbe.FrameworkProbe

/-! ## Row 7c: the turnaround is bounded along the whole lap -/

/-- `y(r) = (|r|/r₀)^{3/2}` on `r ≤ 0`, written `a√a` with `a = −r/r₀`. -/
noncomputable def fw_y (r₀ r : ℝ) : ℝ := (-r / r₀) * Real.sqrt (-r / r₀)

/-- The complex cosmic time along the conjugate branch: `−(2α/3) i arcsin y` on the lap `[−r₀, 0]`, and
`(2α/3)(arcosh y − iπ/2)` beyond the turnaround. -/
noncomputable def fw_τ (α r₀ r : ℝ) : ℂ :=
  if -r₀ ≤ r then -((2 * α / 3 : ℝ) : ℂ) * Complex.I * (Real.arcsin (fw_y r₀ r) : ℂ)
  else ((2 * α / 3 : ℝ) : ℂ) * ((Real.arcosh (fw_y r₀ r) : ℂ) - ((π / 2 : ℝ) : ℂ) * Complex.I)

lemma fw_y_sq {r₀ r : ℝ} (h0 : 0 < r₀) (hr : r ≤ 0) : fw_y r₀ r ^ 2 = (-r / r₀) ^ 3 := by
  have ha : 0 ≤ -r / r₀ := div_nonneg (by linarith) h0.le
  simp only [fw_y]; rw [mul_pow, Real.sq_sqrt ha]; ring

lemma fw_y_nonneg {r₀ r : ℝ} (h0 : 0 < r₀) (hr : r ≤ 0) : 0 ≤ fw_y r₀ r :=
  mul_nonneg (div_nonneg (by linarith) h0.le) (Real.sqrt_nonneg _)

lemma fw_y_le_one {r₀ r : ℝ} (h0 : 0 < r₀) (hr : -r₀ ≤ r) (hr0 : r ≤ 0) : fw_y r₀ r ≤ 1 := by
  have ha : -r / r₀ ≤ 1 := by rw [div_le_one h0]; linarith
  have ha0 : 0 ≤ -r / r₀ := div_nonneg (by linarith) h0.le
  simp only [fw_y]
  have : Real.sqrt (-r / r₀) ≤ 1 := Real.sqrt_le_one.mpr ha
  nlinarith [Real.sqrt_nonneg (-r / r₀)]

lemma fw_one_le_y {r₀ r : ℝ} (h0 : 0 < r₀) (hr : r ≤ -r₀) : 1 ≤ fw_y r₀ r := by
  have ha : 1 ≤ -r / r₀ := by rw [le_div_iff₀ h0]; linarith
  simp only [fw_y]
  have : 1 ≤ Real.sqrt (-r / r₀) := by rw [Real.le_sqrt (by norm_num) (by linarith)]; linarith
  nlinarith

lemma fw_y_cont (r₀ : ℝ) : Continuous (fw_y r₀) := by unfold fw_y; fun_prop

/-- **Row 7c (the bead).** On the whole conjugate branch `r ≤ 0`, `τ̃(r)` solves `r³ = 2Mα² sinh²(3τ̃/2α)`. -/
theorem fw_τ_bead {M α r₀ r : ℝ} (hα : 0 < α) (h0 : 0 < r₀) (h3 : r₀ ^ 3 = 2 * M * α ^ 2) (hr : r ≤ 0) :
    (r : ℂ) ^ 3 = 2 * M * α ^ 2 * Complex.sinh (3 * fw_τ α r₀ r / (2 * α)) ^ 2 := by
  have hαc : (α : ℂ) ≠ 0 := Complex.ofReal_ne_zero.2 hα.ne'
  have hy2 := fw_y_sq h0 hr
  have key : (2 * M * α ^ 2 : ℝ) * (-(fw_y r₀ r ^ 2)) = r ^ 3 := by
    rw [hy2, ← h3]; field_simp
  unfold fw_τ
  split_ifs with hc
  · have harg : (3 * (-((2 * α / 3 : ℝ) : ℂ) * Complex.I * (Real.arcsin (fw_y r₀ r) : ℂ)) / (2 * α) : ℂ) =
        ((-Real.arcsin (fw_y r₀ r) : ℝ) : ℂ) * Complex.I := by
      push_cast; field_simp
    rw [harg, Complex.sinh_mul_I, ← Complex.ofReal_sin, Real.sin_neg,
      Real.sin_arcsin (by linarith [fw_y_nonneg h0 hr]) (fw_y_le_one h0 hc hr)]
    have := congrArg (fun z : ℝ => (z : ℂ)) key
    push_cast at this ⊢
    linear_combination (-1 : ℂ) * this + (-(2 * (M : ℂ) * α ^ 2 * (fw_y r₀ r : ℂ) ^ 2)) * Complex.I_sq
  · simp only [not_le] at hc
    have hy1 := fw_one_le_y h0 hc.le
    have harg : (3 * (((2 * α / 3 : ℝ) : ℂ) * ((Real.arcosh (fw_y r₀ r) : ℂ) - ((π / 2 : ℝ) : ℂ) * Complex.I)) /
        (2 * α) : ℂ) = (Real.arcosh (fw_y r₀ r) : ℂ) - ((π / 2 : ℝ) : ℂ) * Complex.I := by
      push_cast; field_simp
    rw [harg, Complex.sinh_sub, Complex.sinh_mul_I, Complex.cosh_mul_I, ← Complex.ofReal_sin,
      ← Complex.ofReal_cos, Real.sin_pi_div_two, Real.cos_pi_div_two, ← Complex.ofReal_cosh,
      Real.cosh_arcosh hy1]
    have := congrArg (fun z : ℝ => (z : ℂ)) key
    push_cast at this ⊢
    linear_combination (-1 : ℂ) * this + (-(2 * (M : ℂ) * α ^ 2 * (fw_y r₀ r : ℂ) ^ 2)) * Complex.I_sq

/-- **Row 7c (the bound).** Along the whole branch, `|Im τ̃| ≤ πα/3`, with equality exactly beyond the turnaround,
`r ≤ −r₀`. -/
theorem fw_τ_bound {α r₀ r : ℝ} (hα : 0 < α) (h0 : 0 < r₀) (hr : r ≤ 0) :
    |(fw_τ α r₀ r).im| ≤ π * α / 3 ∧ (|(fw_τ α r₀ r).im| = π * α / 3 ↔ r ≤ -r₀) := by
  unfold fw_τ
  split_ifs with hc
  · have hy0 := fw_y_nonneg h0 hr
    have hy1 := fw_y_le_one h0 hc hr
    have ha0 : 0 ≤ Real.arcsin (fw_y r₀ r) := Real.arcsin_nonneg.2 hy0
    have ha1 : Real.arcsin (fw_y r₀ r) ≤ π / 2 := Real.arcsin_le_pi_div_two _
    have him : (-((2 * α / 3 : ℝ) : ℂ) * Complex.I * (Real.arcsin (fw_y r₀ r) : ℂ)).im =
        -(2 * α / 3 * Real.arcsin (fw_y r₀ r)) := by simp
    rw [him, abs_neg, abs_of_nonneg (by positivity)]
    refine ⟨by nlinarith, ⟨fun h => ?_, fun h => ?_⟩⟩
    · have ha : Real.arcsin (fw_y r₀ r) = π / 2 := by
        have : 2 * α / 3 * Real.arcsin (fw_y r₀ r) = 2 * α / 3 * (π / 2) := by rw [h]; ring
        exact mul_left_cancel₀ (by positivity) this
      have hy : fw_y r₀ r = 1 := by
        have := congrArg Real.sin ha
        rwa [Real.sin_arcsin (by linarith) hy1, Real.sin_pi_div_two] at this
      have hy2 := fw_y_sq h0 hr
      rw [hy, one_pow] at hy2
      have ha3 : -r / r₀ = 1 := by
        have hpos : 0 ≤ -r / r₀ := div_nonneg (by linarith) h0.le
        nlinarith [sq_nonneg (-r / r₀ - 1), sq_nonneg (-r / r₀)]
      rw [div_eq_one_iff_eq h0.ne'] at ha3
      linarith
    · have hrr : r = -r₀ := le_antisymm h hc
      have hy : fw_y r₀ r = 1 := by
        simp only [fw_y, hrr, neg_neg, div_self h0.ne', Real.sqrt_one, mul_one]
      rw [hy, Real.arcsin_one]; ring
  · simp only [not_le] at hc
    have him : (((2 * α / 3 : ℝ) : ℂ) * ((Real.arcosh (fw_y r₀ r) : ℂ) - ((π / 2 : ℝ) : ℂ) * Complex.I)).im =
        -(π * α / 3) := by simp; ring
    rw [him, abs_neg, abs_of_pos (by positivity)]
    exact ⟨le_rfl, ⟨fun _ => hc.le, fun _ => rfl⟩⟩

/-- **Row 7c (continuity).** `τ̃` is continuous on the whole conjugate branch `(−∞, 0]`: each piece is continuous,
and they agree at the turnaround `r = −r₀`, where both give `−iπα/3`. -/
theorem fw_τ_cont {α r₀ : ℝ} (h0 : 0 < r₀) : ContinuousOn (fw_τ α r₀) (Iic 0) := by
  have c1 : Continuous fun r => -((2 * α / 3 : ℝ) : ℂ) * Complex.I * (Real.arcsin (fw_y r₀ r) : ℂ) := by
    have := (Real.continuous_arcsin.comp (fw_y_cont r₀))
    fun_prop
  have c2 : ContinuousOn (fun r => ((2 * α / 3 : ℝ) : ℂ) *
      ((Real.arcosh (fw_y r₀ r) : ℂ) - ((π / 2 : ℝ) : ℂ) * Complex.I)) (Iic (-r₀)) := by
    have ca : ContinuousOn (fun r => Real.arcosh (fw_y r₀ r)) (Iic (-r₀)) :=
      Real.continuousOn_arcosh.comp (fw_y_cont r₀).continuousOn fun r hr => fw_one_le_y h0 hr
    exact continuousOn_const.mul ((Complex.continuous_ofReal.comp_continuousOn ca).sub continuousOn_const)
  have hsplit : Iic (0 : ℝ) = Icc (-r₀) 0 ∪ Iic (-r₀) := by
    ext r; simp only [mem_Iic, mem_Icc, mem_union]; constructor
    · intro h; by_cases h' : -r₀ ≤ r
      · exact Or.inl ⟨h', h⟩
      · exact Or.inr (by linarith)
    · rintro (⟨-, h⟩ | h) <;> linarith
  rw [hsplit]
  refine ContinuousOn.union_of_isClosed ?_ ?_ isClosed_Icc isClosed_Iic
  · refine c1.continuousOn.congr fun r hr => ?_
    simp only [fw_τ, hr.1, ↓reduceIte]
  · refine c2.congr fun r hr => ?_
    by_cases h : -r₀ ≤ r
    · have hrr : r = -r₀ := le_antisymm hr h
      have hy : fw_y r₀ r = 1 := by
        simp only [fw_y, hrr, neg_neg, div_self h0.ne', Real.sqrt_one, mul_one]
      simp only [fw_τ, h, ↓reduceIte, hy, Real.arcsin_one, Real.arcosh_zero]
      push_cast; ring
    · simp only [fw_τ, h, ↓reduceIte]

end ShadowProbe.FrameworkProbe

namespace ShadowProbe.BoundaryProbe

open ShadowProbe.FrameworkProbe

/-! ## Row 2: `prop:conjugation-parity` -/

/-- The charged structure function `f(r) = 1 − 2M/r + Q²/r² − Λr²/3`. -/
noncomputable def bd_f (M Q L r : ℝ) : ℝ := 1 - 2 * M / r + Q ^ 2 / r ^ 2 - L * r ^ 2 / 3

/-- **Row 2a.** `f = f_even + f_odd`, with `f_even = 1 + Q²/r² − Λr²/3` even and `f_odd = −2M/r` odd in `r`. So the mass
is the `R`-odd datum, and `f(−r; −M) = f(r; M)`. -/
theorem bd_parity (M Q L r : ℝ) :
    bd_f M Q L r = (1 + Q ^ 2 / r ^ 2 - L * r ^ 2 / 3) + (-2 * M / r) ∧
      (1 + Q ^ 2 / (-r) ^ 2 - L * (-r) ^ 2 / 3) = (1 + Q ^ 2 / r ^ 2 - L * r ^ 2 / 3) ∧
      -2 * M / (-r) = -(-2 * M / r) ∧ bd_f (-M) Q L (-r) = bd_f M Q L r := by
  refine ⟨by simp only [bd_f]; ring, by ring, by rw [div_neg], ?_⟩
  simp only [bd_f, neg_sq, div_neg]; ring

/-- **Row 2b.** The metric sees the charge only through `Q²` (`f(Q) = f(−Q)`), while the Maxwell potential
`A_t = −Q/r` is odd in `Q`: the charge sign lives in `A` alone. -/
theorem bd_charge_even (M Q L r : ℝ) :
    bd_f M (-Q) L r = bd_f M Q L r ∧ -(-Q) / r = -(-Q / r) := by
  refine ⟨by simp only [bd_f, neg_sq], by ring⟩

/-! ## Row 3: `prop:conjugation-closure` -/

/-- The charged spherical metric `diag(−f, 1/f, r², r² sin²θ)` on `(t, r, θ, φ)`. -/
noncomputable def bd_g (M Q L : ℝ) (y : Fin 4 → ℝ) : Matrix (Fin 4) (Fin 4) ℝ :=
  Matrix.diagonal ![-bd_f M Q L (y 1), 1 / bd_f M Q L (y 1), y 1 ^ 2, y 1 ^ 2 * Real.sin (y 2) ^ 2]

/-- `R` on coordinates: `(t, r, θ, φ) ↦ (t, −r, θ, φ)`, with Jacobian `diag(1, −1, 1, 1)`. -/
def bd_ρ (y : Fin 4 → ℝ) : Fin 4 → ℝ := ![y 0, -y 1, y 2, y 3]
def bd_J : Matrix (Fin 4) (Fin 4) ℝ := Matrix.diagonal ![1, -1, 1, 1]

/-- **Row 3a.** `R` is a linear isometry of the charged metric: pulling `g_{−M}` back along `ρ` gives `g_M`. -/
theorem bd_R_isometry (M Q L : ℝ) (y : Fin 4 → ℝ) :
    Matrix.transpose bd_J * bd_g (-M) Q L (bd_ρ y) * bd_J = bd_g M Q L y := by
  have hf : bd_f (-M) Q L (-y 1) = bd_f M Q L (y 1) := (bd_parity M Q L (y 1)).2.2.2
  simp only [bd_J, bd_g, bd_ρ, Matrix.diagonal_transpose, Matrix.diagonal_mul_diagonal]
  congr 1
  ext i; fin_cases i <;> simp [hf]

/-- **Row 3a.** `R` is blind to `Q`: the metric is the same for `Q` and `−Q`. -/
theorem bd_Q_blind (M Q L : ℝ) (y : Fin 4 → ℝ) : bd_g M (-Q) L y = bd_g M Q L y := by
  simp only [bd_g, (bd_charge_even M Q L (y 1)).1]

/-- The bead `r³ = 2Mα² sinh²(3τ̃/2α)`, with `r, τ̃ ∈ ℂ`. -/
def bd_bead (M α : ℝ) (r τ : ℂ) : Prop := r ^ 3 = 2 * M * α ^ 2 * Complex.sinh (3 * τ / (2 * α)) ^ 2

/-- **Row 3b.** The reality involution `K` maps bead solutions to bead solutions. -/
theorem bd_K_bead {M α : ℝ} {r τ : ℂ} (h : bd_bead M α r τ) :
    bd_bead M α ((starRingEnd ℂ) r) ((starRingEnd ℂ) τ) := by
  unfold bd_bead at h ⊢
  have := congrArg (starRingEnd ℂ) h
  simpa [map_pow, map_mul, map_div₀, map_ofNat, Complex.conj_ofReal, ← Complex.sinh_conj] using this

/-- **Row 3b.** `K` is antilinear (`K(iz) = −iK(z)`) and an involution. -/
theorem bd_K_antilinear (z : ℂ) :
    (starRingEnd ℂ) (Complex.I * z) = -Complex.I * (starRingEnd ℂ) z ∧
      (starRingEnd ℂ) ((starRingEnd ℂ) z) = z := by
  constructor
  · simp [map_mul]
  · simp

/-- **Row 3c.** `K` fixes the real (photon) axis and swaps the two `r < 0` wings: beyond the turnaround `τ̃ = fw_τ(r)`
has `Im τ̃ = −πα/3`, while `K τ̃` has `Im = +πα/3` and solves the bead at the same `r`. -/
theorem bd_K_wings {M α r₀ r : ℝ} (hα : 0 < α) (h0 : 0 < r₀) (h3 : r₀ ^ 3 = 2 * M * α ^ 2) (hr : r < -r₀) :
    (∀ x : ℝ, (starRingEnd ℂ) (x : ℂ) = x) ∧
      (fw_τ α r₀ r).im = -(π * α / 3) ∧ ((starRingEnd ℂ) (fw_τ α r₀ r)).im = π * α / 3 ∧
      bd_bead M α (r : ℂ) (fw_τ α r₀ r) ∧ bd_bead M α (r : ℂ) ((starRingEnd ℂ) (fw_τ α r₀ r)) := by
  have hb : bd_bead M α (r : ℂ) (fw_τ α r₀ r) := fw_τ_bead hα h0 h3 (by linarith)
  have him : (fw_τ α r₀ r).im = -(π * α / 3) := by
    have hn : ¬ (-r₀ ≤ r) := by linarith
    simp only [fw_τ, hn, ↓reduceIte]
    simp; ring
  refine ⟨fun x => Complex.conj_ofReal x, him, by rw [Complex.conj_im, him]; ring, hb, ?_⟩
  have := bd_K_bead hb
  rwa [Complex.conj_ofReal] at this

/-- **Row 3d.** `R` (`z ↦ −z`) and `K` commute, and `R ∘ K` is an involution. -/
theorem bd_RK (z : ℂ) :
    -((starRingEnd ℂ) z) = (starRingEnd ℂ) (-z) ∧ -((starRingEnd ℂ) (-((starRingEnd ℂ) z))) = z := by
  constructor <;> simp

/-! ## Row 4: `prop:residue-is-the-bead` -/

/-- The weights of `𝟑` in fundamental-weight coordinates: `ω₁`, `ω₂ − ω₁`, `−ω₂`. -/
def bd_three : Set (Fin 2 → ℤ) := {![1, 0], ![-1, 1], ![0, -1]}

/-- The diagram automorphism of `A₂`, `ω₁ ↔ ω₂`. -/
def bd_σ (v : Fin 2 → ℤ) : Fin 2 → ℤ := ![v 1, v 0]

/-- **Row 4i.** `𝟑̄ = R(𝟑)`: the diagram automorphism maps the weights of `𝟑` onto their negatives, the weights of
`𝟑̄`. -/
theorem bd_conj_rep : bd_σ '' bd_three = (fun v => -v) '' bd_three := by
  ext w
  simp only [bd_three, bd_σ, Set.image_insert_eq, Set.image_singleton, Set.mem_insert_iff,
    Set.mem_singleton_iff]
  constructor <;> rintro (h | h | h) <;> subst h <;> simp

/-- The simple reflections of `A₂` on weight coordinates. -/
def bd_s1 : Matrix (Fin 2) (Fin 2) ℤ := !![-1, 0; 1, 1]
def bd_s2 : Matrix (Fin 2) (Fin 2) ℤ := !![1, 1; 0, -1]

/-- **Row 4i.** `−1 ∉ W(A₂)`: every element of the monoid generated by the simple reflections permutes the weights of
`𝟑`, and `−1` does not. So `R` is the diagram automorphism and not a Weyl element. -/
theorem bd_neg_one_not_weyl : (-1 : Matrix (Fin 2) (Fin 2) ℤ) ∉ Submonoid.closure {bd_s1, bd_s2} := by
  have pres : ∀ A ∈ Submonoid.closure ({bd_s1, bd_s2} : Set (Matrix (Fin 2) (Fin 2) ℤ)),
      ∀ v ∈ bd_three, A.mulVec v ∈ bd_three := by
    intro A hA
    induction hA using Submonoid.closure_induction with
    | mem B hB =>
      intro v hv
      simp only [Set.mem_insert_iff, Set.mem_singleton_iff] at hB
      simp only [bd_three, Set.mem_insert_iff, Set.mem_singleton_iff] at hv ⊢
      rcases hB with rfl | rfl <;> rcases hv with rfl | rfl | rfl <;> decide
    | one => intro v hv; simpa using hv
    | mul B C _ _ hB hC =>
      intro v hv; rw [← Matrix.mulVec_mulVec]; exact hB _ (hC v hv)
  intro h
  have := pres _ h ![1, 0] (by simp [bd_three])
  simp [bd_three] at this

/-- **Row 4iii.** Every orientation-reversing linear isometry of `ℝ^{1,1}` (`η = diag(−1, 1)`) swaps the two null lines:
`(1, 1)` goes into the span of `(1, −1)` and `(1, −1)` into the span of `(1, 1)`. -/
theorem bd_null_swap {a b c d : ℝ} (h1 : -a ^ 2 + c ^ 2 = -1) (h2 : -b ^ 2 + d ^ 2 = 1) (h3 : -a * b + c * d = 0)
    (hdet : a * d - b * c = -1) : c + d = -(a + b) ∧ c - d = a - b := by
  -- with x = a − c, y = a + c, z = d − b, w = d + b: xy = 1, zw = 1, xw = yz = −1
  have hxy : (a - c) * (a + c) = 1 := by nlinarith
  have hzw : (d - b) * (d + b) = 1 := by nlinarith
  have hxw : (a - c) * (d + b) = -1 := by nlinarith
  have hyz : (a + c) * (d - b) = -1 := by nlinarith
  have hx : a - c ≠ 0 := fun h => by rw [h, zero_mul] at hxy; exact zero_ne_one hxy
  have hy : a + c ≠ 0 := fun h => by rw [h, mul_zero] at hxy; exact zero_ne_one hxy
  have e1 : d + b = -(a + c) := by
    have : (a - c) * ((d + b) + (a + c)) = 0 := by linarith
    rcases mul_eq_zero.1 this with h | h
    · exact absurd h hx
    · linarith
  have e2 : d - b = -(a - c) := by
    have : (a + c) * ((d - b) + (a - c)) = 0 := by linarith
    rcases mul_eq_zero.1 this with h | h
    · exact absurd h hy
    · linarith
  constructor <;> linarith

/-- **Row 4iv.** `R` fixes exactly the branch point `r = 0` and exchanges the two signed-radius regions. -/
theorem bd_R_fixed (r : ℝ) : (-r = r ↔ r = 0) ∧ (0 < r ↔ -r < 0) := by
  constructor
  · constructor <;> intro h <;> linarith
  · constructor <;> intro h <;> linarith

/-! ## Non-vacuity -/

/-- **Witnesses.** The parity at `M = Q = 1`, `Λ = 3`, `r = 2`; the isometry at a point; the wing swap at `α = r₀ = 1`,
`r = −2`; the null swap for `A = diag(1, −1)`. -/
theorem bd_witness :
    bd_f (-1) 1 3 (-2) = bd_f 1 1 3 2 ∧ bd_f 1 1 3 2 = -(15 / 4) ∧
      Matrix.transpose bd_J * bd_g (-1) 1 3 (bd_ρ ![0, 2, 1, 0]) * bd_J = bd_g 1 1 3 ![0, 2, 1, 0] ∧
      ((starRingEnd ℂ) (fw_τ 1 1 (-2))).im = π * 1 / 3 ∧
      ((0 : ℝ) + -1 = -(1 + 0) ∧ (0 : ℝ) - -1 = 1 - 0) := by
  refine ⟨(bd_parity 1 1 3 2).2.2.2, by norm_num [bd_f], bd_R_isometry 1 1 3 _,
    (bd_K_wings (M := 1 / 2) one_pos one_pos (by norm_num) (by norm_num)).2.2.1,
    bd_null_swap (by norm_num) (by norm_num) (by norm_num) (by norm_num)⟩

end ShadowProbe.BoundaryProbe

#print axioms ShadowProbe.FrameworkProbe.fw_τ_bead
#print axioms ShadowProbe.FrameworkProbe.fw_τ_bound
#print axioms ShadowProbe.FrameworkProbe.fw_τ_cont
#print axioms ShadowProbe.BoundaryProbe.bd_parity
#print axioms ShadowProbe.BoundaryProbe.bd_charge_even
#print axioms ShadowProbe.BoundaryProbe.bd_R_isometry
#print axioms ShadowProbe.BoundaryProbe.bd_Q_blind
#print axioms ShadowProbe.BoundaryProbe.bd_K_bead
#print axioms ShadowProbe.BoundaryProbe.bd_K_antilinear
#print axioms ShadowProbe.BoundaryProbe.bd_K_wings
#print axioms ShadowProbe.BoundaryProbe.bd_RK
#print axioms ShadowProbe.BoundaryProbe.bd_conj_rep
#print axioms ShadowProbe.BoundaryProbe.bd_neg_one_not_weyl
#print axioms ShadowProbe.BoundaryProbe.bd_null_swap
#print axioms ShadowProbe.BoundaryProbe.bd_R_fixed
#print axioms ShadowProbe.BoundaryProbe.bd_witness

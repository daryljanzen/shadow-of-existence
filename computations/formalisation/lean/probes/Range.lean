import Mathlib

/-!
# Probe `r7745+71.2` (campaign 133): P9's Kantowski–Sachs kernel and the pp-wave's Ricci

Registration: `computations/formalisation/r7745_71_campaign133/PREDICTION.md`; inventory
`computations/formalisation/r7745_71_survey/SURVEY.md`. Nothing imports this file, and it imports only Mathlib. It is a
new probe, prefix `rn_`, and later P9 campaigns append to it, so it is P9's citable file (`corpus/range_paper.tex`).
`StaticEinstein.lean`'s `KrCurvature` section (with `KrTrig`) is copied verbatim below, names kept.

* **Row 3a — BUILT.** `rn_ks_Γ`, `rn_ks_Ric_diag`, `rn_ks_einstein`, `rn_ks_G_offdiag`.
* **Row 3b — BUILT.** `rn_ks_sds_vacuum`, `rn_ks_witness`.
* **Row 3c — BUILT.** `rn_ks_nariai`.
* **Row 8a — BUILT.** `rn_pp_Ric`, `rn_pp_vacuum_iff`, `rn_pp_witness`.
-/

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

end ShadowProbe.StaticEinsteinProbe

namespace ShadowProbe.RangeProbe

open ShadowProbe.StaticEinsteinProbe Real

/-- Ricci `R_{bd} = R^a_{bad}`. -/
noncomputable def rn_Ric (g : (Fin 4 → ℝ) → Matrix (Fin 4) (Fin 4) ℝ) (x : Fin 4 → ℝ) (b d : Fin 4) : ℝ :=
  ∑ a, kr_Riem g x a b a d

/-- The scalar curvature `R = g^{bd} R_{db}`. -/
noncomputable def rn_scal (g : (Fin 4 → ℝ) → Matrix (Fin 4) (Fin 4) ℝ) (x : Fin 4 → ℝ) : ℝ :=
  ∑ b, ∑ d, (g x)⁻¹ b d * rn_Ric g x d b

/-- The mixed Einstein tensor `G^b_c = g^{bd} R_{dc} − ½ δ^b_c R`. -/
noncomputable def rn_G (g : (Fin 4 → ℝ) → Matrix (Fin 4) (Fin 4) ℝ) (x : Fin 4 → ℝ) (b c : Fin 4) : ℝ :=
  ∑ d, (g x)⁻¹ b d * rn_Ric g x d c - (if b = c then rn_scal g x / 2 else 0)

/-! ## Row 3: the Kantowski–Sachs cut -/

/-- The KS metric `−dτ² + X(τ)²dχ² + Y(τ)²(dθ² + sin²θ dφ²)` on `(τ, χ, θ, φ)`. -/
noncomputable def rn_ks (X Y : ℝ → ℝ) (y : Fin 4 → ℝ) : Matrix (Fin 4) (Fin 4) ℝ :=
  Matrix.diagonal ![-1, X (y 0) ^ 2, Y (y 0) ^ 2, Y (y 0) ^ 2 * kr_s2 (y 2)]

/-- The data: `X′ = X1`, `X1′ = X2`, `Y′ = Y1`, `Y1′ = Y2` everywhere; `X, Y, sin θ ≠ 0` at the point. -/
structure rn_Hyp (X X1 X2 Y Y1 Y2 : ℝ → ℝ) (x : Fin 4 → ℝ) : Prop where
  hX : ∀ t, HasDerivAt X (X1 t) t
  hX1 : ∀ t, HasDerivAt X1 (X2 t) t
  hY : ∀ t, HasDerivAt Y (Y1 t) t
  hY1 : ∀ t, HasDerivAt Y1 (Y2 t) t
  hX0 : X (x 0) ≠ 0
  hY0 : Y (x 0) ≠ 0
  hs : Real.sin (x 2) ≠ 0

noncomputable def rn_c1 (X X1 : ℝ → ℝ) (t : ℝ) : ℝ := X t * X1 t
noncomputable def rn_c2 (Y Y1 : ℝ → ℝ) (t : ℝ) : ℝ := Y t * Y1 t
noncomputable def rn_c3 (X X1 : ℝ → ℝ) (t : ℝ) : ℝ := X1 t / X t
noncomputable def rn_c4 (Y Y1 : ℝ → ℝ) (t : ℝ) : ℝ := Y1 t / Y t

/-- The Christoffel table of `rn_ks`. -/
noncomputable def rn_T (X X1 Y Y1 : ℝ → ℝ) (y : Fin 4 → ℝ) : Fin 4 → Fin 4 → Fin 4 → ℝ :=
  ![![![0, 0, 0, 0], ![0, rn_c1 X X1 (y 0), 0, 0], ![0, 0, rn_c2 Y Y1 (y 0), 0],
      ![0, 0, 0, rn_c2 Y Y1 (y 0) * kr_s2 (y 2)]],
    ![![0, rn_c3 X X1 (y 0), 0, 0], ![rn_c3 X X1 (y 0), 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]],
    ![![0, 0, rn_c4 Y Y1 (y 0), 0], ![0, 0, 0, 0], ![rn_c4 Y Y1 (y 0), 0, 0, 0], ![0, 0, 0, kr_nsc (y 2)]],
    ![![0, 0, 0, rn_c4 Y Y1 (y 0)], ![0, 0, 0, 0], ![0, 0, 0, kr_cot (y 2)],
      ![rn_c4 Y Y1 (y 0), 0, kr_cot (y 2), 0]]]

variable {X X1 X2 Y Y1 Y2 : ℝ → ℝ}

lemma rn_ks_inv {y : Fin 4 → ℝ} (hX : X (y 0) ≠ 0) (hY : Y (y 0) ≠ 0) (hs : Real.sin (y 2) ≠ 0) :
    (rn_ks X Y y)⁻¹ = Matrix.diagonal ![-1, (X (y 0) ^ 2)⁻¹, (Y (y 0) ^ 2)⁻¹, (Y (y 0) ^ 2 * kr_s2 (y 2))⁻¹] := by
  refine Matrix.inv_eq_left_inv ?_
  rw [rn_ks, Matrix.diagonal_mul_diagonal, ← Matrix.diagonal_one]
  congr 1; ext i; fin_cases i <;> simp [kr_s2] <;> field_simp

lemma rn_ks_Γ (hXd : ∀ t, HasDerivAt X (X1 t) t) (hYd : ∀ t, HasDerivAt Y (Y1 t) t) {y : Fin 4 → ℝ}
    (hX : X (y 0) ≠ 0) (hY : Y (y 0) ≠ 0) (hs : Real.sin (y 2) ≠ 0) (a b c : Fin 4) :
    kr_Γ (rn_ks X Y) y a b c = rn_T X X1 Y Y1 y a b c := by
  have hX2' : HasDerivAt (fun t => X t ^ 2) ((2 : ℕ) * X (y 0) ^ (2 - 1) * X1 (y 0)) (y 0) := (hXd (y 0)).pow 2
  have hY2' : HasDerivAt (fun t => Y t ^ 2) ((2 : ℕ) * Y (y 0) ^ (2 - 1) * Y1 (y 0)) (y 0) := (hYd (y 0)).pow 2
  have hX2 : HasDerivAt (fun t => X t ^ 2) (2 * X (y 0) * X1 (y 0)) (y 0) := hX2'.congr_deriv (by push_cast; ring)
  have hY2 : HasDerivAt (fun t => Y t ^ 2) (2 * Y (y 0) * Y1 (y 0)) (y 0) := hY2'.congr_deriv (by push_cast; ring)
  have d1 : deriv (fun t => X t ^ 2) (y 0) = 2 * X (y 0) * X1 (y 0) := hX2.deriv
  have d2 : deriv (fun t => Y t ^ 2) (y 0) = 2 * Y (y 0) * Y1 (y 0) := hY2.deriv
  have d3 : deriv (fun t => Y t ^ 2 * kr_s2 (y 2)) (y 0) = 2 * Y (y 0) * Y1 (y 0) * kr_s2 (y 2) :=
    (hY2.mul_const _).deriv
  have d4 : deriv (fun t => Y (y 0) ^ 2 * kr_s2 t) (y 2) = Y (y 0) ^ 2 * (2 * Real.sin (y 2) * Real.cos (y 2)) :=
    ((kr_hasDerivAt_s2 (y 2)).const_mul _).deriv
  simp only [kr_Γ, rn_ks_inv hX hY hs]
  fin_cases a <;> fin_cases b <;> fin_cases c <;>
    simp [kr_pd, rn_ks, rn_T, Function.update_apply, Matrix.diagonal_apply, d1, d2, d3, d4,
      rn_c1, rn_c2, rn_c3, rn_c4, kr_nsc, kr_cot]
  all_goals (try simp only [kr_s2])
  all_goals field_simp

variable {x : Fin 4 → ℝ}

lemma rn_Hyp.U (h : rn_Hyp X X1 X2 Y Y1 Y2 x) :
    ∀ᶠ y in 𝓝 x, X (y 0) ≠ 0 ∧ Y (y 0) ≠ 0 ∧ Real.sin (y 2) ≠ 0 := by
  have c0 : ContinuousAt (fun y : Fin 4 → ℝ => y 0) x := (continuous_apply 0).continuousAt
  have c2 : ContinuousAt (fun y : Fin 4 → ℝ => y 2) x := (continuous_apply 2).continuousAt
  filter_upwards [(ContinuousAt.comp (f := fun y : Fin 4 → ℝ => y 0) (h.hX (x 0)).continuousAt c0).eventually_ne h.hX0,
    (ContinuousAt.comp (f := fun y : Fin 4 → ℝ => y 0) (h.hY (x 0)).continuousAt c0).eventually_ne h.hY0,
    (ContinuousAt.comp (f := fun y : Fin 4 → ℝ => y 2) Real.continuous_sin.continuousAt c2).eventually_ne h.hs]
    with y h1 h2 h3
  exact ⟨h1, h2, h3⟩

lemma rn_pd (h : rn_Hyp X X1 X2 Y Y1 Y2 x) (a b c d : Fin 4) :
    kr_pd (fun y => kr_Γ (rn_ks X Y) y a b c) x d = kr_pd (fun y => rn_T X X1 Y Y1 y a b c) x d :=
  kr_pd_congr (h.U.mono fun _ hy => rn_ks_Γ h.hX h.hY hy.1 hy.2.1 hy.2.2 a b c)

/-- **The Ricci diagonal of the KS cut.** -/
theorem rn_ks_Ric_diag (h : rn_Hyp X X1 X2 Y Y1 Y2 x) :
    rn_Ric (rn_ks X Y) x 0 0 = -(X2 (x 0) / X (x 0)) - 2 * (Y2 (x 0) / Y (x 0)) ∧
      rn_Ric (rn_ks X Y) x 1 1 = X (x 0) * X2 (x 0) + 2 * X (x 0) * X1 (x 0) * Y1 (x 0) / Y (x 0) ∧
      rn_Ric (rn_ks X Y) x 2 2 = Y (x 0) * Y2 (x 0) + Y1 (x 0) ^ 2 + Y (x 0) * Y1 (x 0) * X1 (x 0) / X (x 0) + 1 ∧
      rn_Ric (rn_ks X Y) x 3 3 = kr_s2 (x 2) * (Y (x 0) * Y2 (x 0) + Y1 (x 0) ^ 2 +
        Y (x 0) * Y1 (x 0) * X1 (x 0) / X (x 0) + 1) := by
  have hΓ := rn_ks_Γ h.hX h.hY h.hX0 h.hY0 h.hs
  have hX := h.hX0; have hY := h.hY0; have hs := h.hs
  have e1 : deriv (rn_c1 X X1) (x 0) = X1 (x 0) * X1 (x 0) + X (x 0) * X2 (x 0) :=
    ((h.hX (x 0)).mul (h.hX1 (x 0))).deriv
  have e2 : deriv (rn_c2 Y Y1) (x 0) = Y1 (x 0) * Y1 (x 0) + Y (x 0) * Y2 (x 0) :=
    ((h.hY (x 0)).mul (h.hY1 (x 0))).deriv
  have e2s : deriv (fun t => rn_c2 Y Y1 t * kr_s2 (x 2)) (x 0) =
      (Y1 (x 0) * Y1 (x 0) + Y (x 0) * Y2 (x 0)) * kr_s2 (x 2) :=
    (((h.hY (x 0)).mul (h.hY1 (x 0))).mul_const (kr_s2 (x 2))).deriv
  have e3 : deriv (rn_c3 X X1) (x 0) = (X2 (x 0) * X (x 0) - X1 (x 0) * X1 (x 0)) / X (x 0) ^ 2 :=
    ((h.hX1 (x 0)).div (h.hX (x 0)) hX).deriv
  have e4 : deriv (rn_c4 Y Y1) (x 0) = (Y2 (x 0) * Y (x 0) - Y1 (x 0) * Y1 (x 0)) / Y (x 0) ^ 2 :=
    ((h.hY1 (x 0)).div (h.hY (x 0)) hY).deriv
  have en := kr_deriv_nsc (x 2)
  have ec := kr_deriv_cot hs
  refine ⟨?_, ?_, ?_, ?_⟩ <;>
  · unfold rn_Ric kr_Riem
    simp only [Fin.sum_univ_four, rn_pd h, hΓ]
    simp [rn_T, kr_pd, e1, e2, e2s, e3, e4, en, ec]
    all_goals (try simp only [rn_c1, rn_c2, rn_c3, rn_c4, kr_nsc, kr_cot, kr_s2])
    all_goals field_simp
    all_goals (try simp only [Real.cos_sq'])
    all_goals ring

/-- **The off-diagonal Ricci components vanish.** -/
theorem rn_ks_Ric_offdiag (h : rn_Hyp X X1 X2 Y Y1 Y2 x) (b c : Fin 4) (hbc : b ≠ c) :
    rn_Ric (rn_ks X Y) x b c = 0 := by
  have hΓ := rn_ks_Γ h.hX h.hY h.hX0 h.hY0 h.hs
  have hX := h.hX0; have hY := h.hY0; have hs := h.hs
  fin_cases b <;> fin_cases c <;> (try exact absurd rfl hbc) <;>
  · unfold rn_Ric kr_Riem
    simp only [Fin.sum_univ_four, rn_pd h, hΓ]
    simp [rn_T, kr_pd]
    all_goals (try simp only [rn_c4, kr_cot])
    all_goals (try field_simp)
    all_goals (try ring)

theorem rn_ks_G_offdiag (h : rn_Hyp X X1 X2 Y Y1 Y2 x) (b c : Fin 4) (hbc : b ≠ c) :
    rn_G (rn_ks X Y) x b c = 0 := by
  have hinv := rn_ks_inv h.hX0 h.hY0 h.hs
  have hR := rn_ks_Ric_offdiag h b c hbc
  simp only [rn_G, hbc, ↓reduceIte, sub_zero, hinv, Matrix.diagonal_apply, ite_mul, zero_mul,
    Finset.sum_ite_eq, Finset.mem_univ, hR, mul_zero]

/-- **Row 3a.** The KS Einstein tensor, P9 eq. `ksrho` and partners (with `8πT = G + Λ`):
`−G^τ_τ = (Y′/Y)² + 1/Y² + 2X′Y′/(XY)`, `G^χ_χ = −2Y″/Y − (Y′/Y)² − 1/Y²`,
`G^θ_θ = G^φ_φ = −Y″/Y − X″/X − X′Y′/(XY)`. -/
theorem rn_ks_einstein (h : rn_Hyp X X1 X2 Y Y1 Y2 x) :
    -rn_G (rn_ks X Y) x 0 0 = (Y1 (x 0) / Y (x 0)) ^ 2 + 1 / Y (x 0) ^ 2 +
        2 * (X1 (x 0) / X (x 0)) * (Y1 (x 0) / Y (x 0)) ∧
      rn_G (rn_ks X Y) x 1 1 = -2 * (Y2 (x 0) / Y (x 0)) - (Y1 (x 0) / Y (x 0)) ^ 2 - 1 / Y (x 0) ^ 2 ∧
      rn_G (rn_ks X Y) x 2 2 = -(Y2 (x 0) / Y (x 0)) - X2 (x 0) / X (x 0) -
        (X1 (x 0) / X (x 0)) * (Y1 (x 0) / Y (x 0)) ∧
      rn_G (rn_ks X Y) x 3 3 = rn_G (rn_ks X Y) x 2 2 := by
  obtain ⟨r0, r1, r2, r3⟩ := rn_ks_Ric_diag h
  have hX := h.hX0; have hY := h.hY0
  have hs2 : kr_s2 (x 2) ≠ 0 := pow_ne_zero 2 h.hs
  have hinv := rn_ks_inv h.hX0 h.hY0 h.hs
  have G : ∀ b, rn_G (rn_ks X Y) x b b = (rn_ks X Y x)⁻¹ b b * rn_Ric (rn_ks X Y) x b b - rn_scal (rn_ks X Y) x / 2 := by
    intro b
    simp only [rn_G, hinv, Matrix.diagonal_apply, Fin.sum_univ_four]
    fin_cases b <;> simp
  have S : rn_scal (rn_ks X Y) x = -rn_Ric (rn_ks X Y) x 0 0 + (X (x 0) ^ 2)⁻¹ * rn_Ric (rn_ks X Y) x 1 1
      + (Y (x 0) ^ 2)⁻¹ * rn_Ric (rn_ks X Y) x 2 2 + (Y (x 0) ^ 2 * kr_s2 (x 2))⁻¹ * rn_Ric (rn_ks X Y) x 3 3 := by
    simp only [rn_scal, hinv, Matrix.diagonal_apply, Fin.sum_univ_four]
    simp
  refine ⟨?_, ?_, ?_, ?_⟩
  · rw [G, S, hinv, r0, r1, r2, r3]; simp; field_simp; ring
  · rw [G, S, hinv, r0, r1, r2, r3]; simp; field_simp; ring
  · rw [G, S, hinv, r0, r1, r2, r3]; simp; field_simp; ring
  · rw [G, G, S, hinv, r2, r3]; simp; field_simp

/-- **Row 3b.** The SdS interior is vacuum: if `Y′ = X`, `X′ = −f′(Y)/2`, `X″ = −f″(Y)X/2` and `X² = −f(Y)` for
`f = 1 − 2M/Y − ΛY²/3`, then `G^μ_ν + Λδ^μ_ν = 0` for all sixteen components. -/
theorem rn_ks_sds_vacuum {Λ M : ℝ} (h : rn_Hyp X X1 X2 Y Y1 Y2 x)
    (hY1 : Y1 (x 0) = X (x 0)) (hX1 : X1 (x 0) = -(2 * M / Y (x 0) ^ 2 - 2 * Λ * Y (x 0) / 3) / 2)
    (hY2 : Y2 (x 0) = X1 (x 0)) (hX2 : X2 (x 0) = -(-4 * M / Y (x 0) ^ 3 - 2 * Λ / 3) * X (x 0) / 2)
    (hf : X (x 0) ^ 2 = -(1 - 2 * M / Y (x 0) - Λ * Y (x 0) ^ 2 / 3)) (μ ν : Fin 4) :
    rn_G (rn_ks X Y) x μ ν + (if μ = ν then Λ else 0) = 0 := by
  obtain ⟨g0, g1, g2, g3⟩ := rn_ks_einstein h
  have hX := h.hX0; have hY := h.hY0
  have hM : M = (3 * Y (x 0) * X (x 0) ^ 2 + 3 * Y (x 0) - Λ * Y (x 0) ^ 3) / 6 := by
    have h' := hf; field_simp at h'; linarith
  rw [hM] at hX1 hX2
  by_cases hμν : μ = ν
  · subst hμν; simp only [↓reduceIte]
    rcases (show μ = 0 ∨ μ = 1 ∨ μ = 2 ∨ μ = 3 by fin_cases μ <;> simp) with rfl | rfl | rfl | rfl
    · have : rn_G (rn_ks X Y) x 0 0 = -((Y1 (x 0) / Y (x 0)) ^ 2 + 1 / Y (x 0) ^ 2 +
          2 * (X1 (x 0) / X (x 0)) * (Y1 (x 0) / Y (x 0))) := by linarith
      rw [this, hY1, hX1]; field_simp; ring
    · rw [g1, hY2, hY1, hX1]; field_simp; ring
    · rw [g2, hY2, hX2, hY1, hX1]; field_simp; ring
    · rw [g3, g2, hY2, hX2, hY1, hX1]; field_simp; ring
  · simp only [hμν, ↓reduceIte, add_zero, rn_ks_G_offdiag h μ ν hμν]

/-- **Row 3c.** The Nariai member `Y = 1/√Λ`, `X = e^{√Λτ}` is vacuum: `G^μ_ν + Λδ^μ_ν = 0` for all sixteen. -/
theorem rn_ks_nariai {Λ : ℝ} (hΛ : 0 < Λ) {x : Fin 4 → ℝ} (hs : Real.sin (x 2) ≠ 0) (μ ν : Fin 4) :
    rn_G (rn_ks (fun t => Real.exp (Real.sqrt Λ * t)) (fun _ => 1 / Real.sqrt Λ)) x μ ν +
      (if μ = ν then Λ else 0) = 0 := by
  have hq : 0 < Real.sqrt Λ := Real.sqrt_pos.2 hΛ
  have hq2 : Real.sqrt Λ ^ 2 = Λ := Real.sq_sqrt hΛ.le
  have hX : ∀ t, HasDerivAt (fun t => Real.exp (Real.sqrt Λ * t)) (Real.sqrt Λ * Real.exp (Real.sqrt Λ * t)) t :=
    fun t => (((hasDerivAt_id t).const_mul (Real.sqrt Λ)).exp).congr_deriv (by simp; ring)
  have hX1 : ∀ t, HasDerivAt (fun t => Real.sqrt Λ * Real.exp (Real.sqrt Λ * t))
      (Real.sqrt Λ * (Real.sqrt Λ * Real.exp (Real.sqrt Λ * t))) t := fun t => (hX t).const_mul _
  have h : rn_Hyp (fun t => Real.exp (Real.sqrt Λ * t)) (fun t => Real.sqrt Λ * Real.exp (Real.sqrt Λ * t))
      (fun t => Real.sqrt Λ * (Real.sqrt Λ * Real.exp (Real.sqrt Λ * t))) (fun _ => 1 / Real.sqrt Λ) (fun _ => 0)
      (fun _ => 0) x :=
    ⟨hX, hX1, fun t => hasDerivAt_const t _, fun t => hasDerivAt_const t _, (Real.exp_pos _).ne',
      by positivity, hs⟩
  obtain ⟨g0, g1, g2, g3⟩ := rn_ks_einstein h
  by_cases hμν : μ = ν
  · subst hμν; simp only [↓reduceIte]
    rcases (show μ = 0 ∨ μ = 1 ∨ μ = 2 ∨ μ = 3 by fin_cases μ <;> simp) with rfl | rfl | rfl | rfl
    · have e : rn_G (rn_ks (fun t => Real.exp (Real.sqrt Λ * t)) (fun _ => 1 / Real.sqrt Λ)) x 0 0 =
          -((0 / (1 / Real.sqrt Λ)) ^ 2 + 1 / (1 / Real.sqrt Λ) ^ 2 +
            2 * (Real.sqrt Λ * Real.exp (Real.sqrt Λ * x 0) / Real.exp (Real.sqrt Λ * x 0)) * (0 / (1 / Real.sqrt Λ))) := by
        linarith
      rw [e]; field_simp; ring_nf; linarith [hq2]
    · rw [g1]; field_simp; ring_nf; linarith [hq2]
    · rw [g2]; field_simp; ring_nf; linarith [hq2]
    · rw [g3, g2]; field_simp; ring_nf; linarith [hq2]
  · simp only [hμν, ↓reduceIte, add_zero, rn_ks_G_offdiag h μ ν hμν]

/-- **Row 3b, non-vacuity.** `M = 0`, `Λ = 3`: `Y = cosh τ`, `X = sinh τ` solves `Y′² = −f(Y)` with `X = Y′`, and the
cut is vacuum at `τ = 1`, `θ = π/2`. -/
theorem rn_ks_witness (μ ν : Fin 4) :
    rn_G (rn_ks Real.sinh Real.cosh) ![1, 0, π / 2, 0] μ ν + (if μ = ν then (3 : ℝ) else 0) = 0 := by
  have h : rn_Hyp Real.sinh Real.cosh Real.sinh Real.cosh Real.sinh Real.cosh ![1, 0, π / 2, 0] :=
    ⟨Real.hasDerivAt_sinh, Real.hasDerivAt_cosh, Real.hasDerivAt_cosh, Real.hasDerivAt_sinh,
      by simp, by simpa using (Real.cosh_pos 1).ne', by simp⟩
  refine rn_ks_sds_vacuum (M := 0) h rfl ?_ rfl ?_ ?_ μ ν
  · simp; field_simp
  · simp
  · simp; rw [Real.cosh_sq]; ring

/-! ## Row 8a: the pp-wave -/

/-- The profile `H(u, x, y)`, independent of `v`. -/
def rn_H (h : ℝ → ℝ → ℝ → ℝ) (y : Fin 4 → ℝ) : ℝ := h (y 0) (y 2) (y 3)

/-- The pp-wave `H du² − 2 du dv + dx² + dy²` on `(u, v, x, y)`. -/
def rn_pp (h : ℝ → ℝ → ℝ → ℝ) (y : Fin 4 → ℝ) : Matrix (Fin 4) (Fin 4) ℝ :=
  !![rn_H h y, -1, 0, 0; -1, 0, 0, 0; 0, 0, 1, 0; 0, 0, 0, 1]

lemma rn_pp_inv (h : ℝ → ℝ → ℝ → ℝ) (y : Fin 4 → ℝ) :
    (rn_pp h y)⁻¹ = !![0, -1, 0, 0; -1, -rn_H h y, 0, 0; 0, 0, 1, 0; 0, 0, 0, 1] := by
  refine Matrix.inv_eq_left_inv ?_
  ext i j; fin_cases i <;> fin_cases j <;> simp [rn_pp, Matrix.mul_apply, Fin.sum_univ_four]

lemma rn_pd_v (h : ℝ → ℝ → ℝ → ℝ) (x : Fin 4 → ℝ) : kr_pd (rn_H h) x 1 = 0 := by
  simp [kr_pd, rn_H]

lemma rn_pd_v2 (h : ℝ → ℝ → ℝ → ℝ) (x : Fin 4 → ℝ) (c : Fin 4) :
    kr_pd (fun y => kr_pd (rn_H h) y c) x 1 = 0 := by
  fin_cases c <;> simp [kr_pd, rn_H]

/-- The pp-wave's Christoffel table: `Γ^v_uu = −½∂_uH`, `Γ^v_ux = −½∂_xH`, `Γ^v_uy = −½∂_yH`, `Γ^x_uu = −½∂_xH`,
`Γ^y_uu = −½∂_yH`, all others zero. -/
noncomputable def rn_ppT (h : ℝ → ℝ → ℝ → ℝ) (y : Fin 4 → ℝ) : Fin 4 → Fin 4 → Fin 4 → ℝ :=
  ![![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]],
    ![![-(kr_pd (rn_H h) y 0) / 2, 0, -(kr_pd (rn_H h) y 2) / 2, -(kr_pd (rn_H h) y 3) / 2], ![0, 0, 0, 0],
      ![-(kr_pd (rn_H h) y 2) / 2, 0, 0, 0], ![-(kr_pd (rn_H h) y 3) / 2, 0, 0, 0]],
    ![![-(kr_pd (rn_H h) y 2) / 2, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]],
    ![![-(kr_pd (rn_H h) y 3) / 2, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]]]

lemma rn_pp_Γ (h : ℝ → ℝ → ℝ → ℝ) (y : Fin 4 → ℝ) (a b c : Fin 4) :
    kr_Γ (rn_pp h) y a b c = rn_ppT h y a b c := by
  have hv := rn_pd_v h y
  simp only [kr_Γ, rn_pp_inv]
  fin_cases a <;> fin_cases b <;> fin_cases c <;>
    simp [Fin.sum_univ_four, rn_pp, rn_ppT, kr_pd_const, hv] <;> ring

lemma rn_pd_negHalf (f : (Fin 4 → ℝ) → ℝ) (x : Fin 4 → ℝ) (d : Fin 4) :
    kr_pd (fun y => -f y / 2) x d = -kr_pd f x d / 2 := by
  unfold kr_pd; rw [deriv_div_const, deriv.fun_neg]

lemma rn_pp_pd (h : ℝ → ℝ → ℝ → ℝ) (x : Fin 4 → ℝ) (a b c d : Fin 4) :
    kr_pd (fun y => kr_Γ (rn_pp h) y a b c) x d = kr_pd (fun y => rn_ppT h y a b c) x d := by
  simp only [rn_pp_Γ]

/-- **Row 8a.** The pp-wave's Ricci tensor: `R_uu = −½(∂²_x H + ∂²_y H)` and every other component vanishes. -/
theorem rn_pp_Ric (h : ℝ → ℝ → ℝ → ℝ) (x : Fin 4 → ℝ) :
    rn_Ric (rn_pp h) x 0 0 =
        -(kr_pd (fun y => kr_pd (rn_H h) y 2) x 2 + kr_pd (fun y => kr_pd (rn_H h) y 3) x 3) / 2 ∧
      ∀ b d : Fin 4, ¬(b = 0 ∧ d = 0) → rn_Ric (rn_pp h) x b d = 0 := by
  have v2 := rn_pd_v2 h x
  have hΓ := rn_pp_Γ h x
  refine ⟨?_, fun b d hbd => ?_⟩
  · unfold rn_Ric kr_Riem
    simp only [Fin.sum_univ_four, rn_pp_pd, hΓ]
    simp [rn_ppT, kr_pd_const, v2, rn_pd_negHalf]
    ring
  · fin_cases b <;> fin_cases d <;> simp at hbd <;>
    · unfold rn_Ric kr_Riem
      simp only [Fin.sum_univ_four, rn_pp_pd, hΓ]
      simp [rn_ppT, kr_pd_const, v2, rn_pd_negHalf]

/-- **Row 8a.** The pp-wave is vacuum iff `H` is harmonic in `(x, y)`: all sixteen `R_μν = 0` ⟺
`∂²_x H + ∂²_y H = 0`. -/
theorem rn_pp_vacuum_iff (h : ℝ → ℝ → ℝ → ℝ) (x : Fin 4 → ℝ) :
    (∀ b d, rn_Ric (rn_pp h) x b d = 0) ↔
      kr_pd (fun y => kr_pd (rn_H h) y 2) x 2 + kr_pd (fun y => kr_pd (rn_H h) y 3) x 3 = 0 := by
  obtain ⟨h0, hoff⟩ := rn_pp_Ric h x
  constructor
  · intro hv; have := hv 0 0; rw [h0] at this; linarith
  · intro hs b d
    by_cases hbd : b = 0 ∧ d = 0
    · obtain ⟨rfl, rfl⟩ := hbd; rw [h0, hs]; ring
    · exact hoff b d hbd

/-- **Row 8a, non-vacuity.** `H = x² − y²` is harmonic, so its pp-wave is vacuum at every point. -/
theorem rn_pp_witness (x : Fin 4 → ℝ) :
    ∀ b d, rn_Ric (rn_pp fun _ X Y => X ^ 2 - Y ^ 2) x b d = 0 := by
  have i2 : ∀ y : Fin 4 → ℝ, kr_pd (rn_H fun _ X Y => X ^ 2 - Y ^ 2) y 2 = 2 * y 2 := fun y => by
    simp [kr_pd, rn_H]
  have i3 : ∀ y : Fin 4 → ℝ, kr_pd (rn_H fun _ X Y => X ^ 2 - Y ^ 2) y 3 = -(2 * y 3) := fun y => by
    simp [kr_pd, rn_H]
  rw [rn_pp_vacuum_iff]
  simp only [i2, i3]
  simp [kr_pd]

end ShadowProbe.RangeProbe

#print axioms ShadowProbe.RangeProbe.rn_ks_inv
#print axioms ShadowProbe.RangeProbe.rn_ks_Γ
#print axioms ShadowProbe.RangeProbe.rn_ks_Ric_diag
#print axioms ShadowProbe.RangeProbe.rn_ks_Ric_offdiag
#print axioms ShadowProbe.RangeProbe.rn_ks_G_offdiag
#print axioms ShadowProbe.RangeProbe.rn_ks_einstein
#print axioms ShadowProbe.RangeProbe.rn_ks_sds_vacuum
#print axioms ShadowProbe.RangeProbe.rn_ks_nariai
#print axioms ShadowProbe.RangeProbe.rn_ks_witness
#print axioms ShadowProbe.RangeProbe.rn_pp_inv
#print axioms ShadowProbe.RangeProbe.rn_pp_Γ
#print axioms ShadowProbe.RangeProbe.rn_pp_Ric
#print axioms ShadowProbe.RangeProbe.rn_pp_vacuum_iff
#print axioms ShadowProbe.RangeProbe.rn_pp_witness

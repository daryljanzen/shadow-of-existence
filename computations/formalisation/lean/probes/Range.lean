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

Campaign 134 (`r7747+71.1`, `computations/formalisation/r7747_71_campaign134/PREDICTION.md`) appends Kerr–de Sitter,
`kds_`, in the chart `(t, r, x = cos θ, φ)`. The transfer of 4a and 4c back to the θ chart is not formalised.
* **Row 4a — BUILT (chart `x = cos θ`).** `kds_vacuum`: `R_μν = Λg_μν`, all sixteen; witness `kds_witness`.
* **Row 4b — BUILT.** `kds_sds` (`a = 0`), `kds_desitter` (`a = M = 0`).
* **Row 4c — BUILT (chart `x = cos θ`).** `kds_const_curv`: at `M = 0`, `R_{abcd} = (Λ/3)(g_ac g_bd − g_ad g_bc)`.
* **Row 4d — BUILT.** `kds_deltadecomp`.
* **Row 4e — BUILT.** `kds_J`.
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


/-! ## Row 4: Kerr–de Sitter in the chart `(t, r, x = cos θ, φ)` -/

/-- `ρ² = r² + a²x²`. -/
noncomputable def kds_P (a r x : ℝ) : ℝ := r ^ 2 + a ^ 2 * x ^ 2
/-- `Δ_r = (r² + a²)(1 − Λr²/3) − 2Mr`. -/
noncomputable def kds_D (a M L r : ℝ) : ℝ := (r ^ 2 + a ^ 2) * (1 - L * r ^ 2 / 3) - 2 * M * r
/-- `Δ_x = 1 + Λa²x²/3`, i.e. `Δ_θ` at `x = cos θ`. -/
noncomputable def kds_Q (a L x : ℝ) : ℝ := 1 + L * a ^ 2 * x ^ 2 / 3
/-- `1 − x² = sin²θ`. -/
noncomputable def kds_S (x : ℝ) : ℝ := 1 - x ^ 2
/-- `Ξ = 1 + Λa²/3`. -/
noncomputable def kds_X (a L : ℝ) : ℝ := 1 + L * a ^ 2 / 3

lemma kds_P_dr (a r x : ℝ) : HasDerivAt (fun t => kds_P a t x) (2 * r) r := by
  have h := ((hasDerivAt_id' r).pow 2).add (hasDerivAt_const r (a ^ 2 * x ^ 2))
  exact h.congr_deriv (by simp)
lemma kds_P_dx (a r x : ℝ) : HasDerivAt (fun t => kds_P a r t) (2 * a ^ 2 * x) x := by
  have h := (hasDerivAt_const x (r ^ 2)).add (((hasDerivAt_id' x).pow 2).const_mul (a ^ 2))
  exact h.congr_deriv (by simp; ring)
lemma kds_D_dr (a M L r : ℝ) :
    HasDerivAt (fun t => kds_D a M L t) (((-2:ℝ) * M) + (2 * r * (1 + (((-1:ℝ) * L * (r ^ 2)) / 3))) + (((-2:ℝ) * L * r * ((a ^ 2) + (r ^ 2))) / 3)) r := by
  have h := ((((hasDerivAt_id' r).pow 2).add (hasDerivAt_const r (a ^ 2))).mul
    ((hasDerivAt_const r (1 : ℝ)).sub ((((hasDerivAt_id' r).pow 2).const_mul L).div_const 3))).sub
    ((hasDerivAt_id' r).const_mul (2 * M))
  exact h.congr_deriv (by simp; ring)
lemma kds_Q_dx (a L x : ℝ) : HasDerivAt (fun t => kds_Q a L t) (2 * L * a ^ 2 * x / 3) x := by
  have h := (hasDerivAt_const x (1 : ℝ)).add ((((hasDerivAt_id' x).pow 2).const_mul (L * a ^ 2)).div_const 3)
  exact h.congr_deriv (by simp; ring)
lemma kds_S_dx (x : ℝ) : HasDerivAt (fun t => kds_S t) (-2 * x) x := by
  have h := (hasDerivAt_const x (1 : ℝ)).sub ((hasDerivAt_id' x).pow 2)
  exact h.congr_deriv (by simp)


/-! Generated (campaign 134): the derivative lemmas below are emitted by
`computations/formalisation/r7747_71_campaign134/generator/`, each closed by `congr_deriv`. -/

noncomputable def kds_g00 (a M L r x : ℝ) : ℝ :=
  ((((-1:ℝ) * kds_D a M L r) + (kds_Q a L x * kds_S x * (a ^ 2))) / (kds_P a r x * (kds_X a L ^ 2)))

noncomputable def kds_g03 (a M L r x : ℝ) : ℝ :=
  (((kds_S x * a) * (kds_D a M L r + (((-1:ℝ) * kds_Q a L x) * ((a ^ 2) + (r ^ 2))))) / (kds_P a r x * (kds_X a L ^ 2)))

noncomputable def kds_g33 (a M L r x : ℝ) : ℝ :=
  ((kds_S x * ((kds_Q a L x * (((a ^ 2) + (r ^ 2)) ^ 2)) + ((((-1:ℝ) * kds_D a M L r) * kds_S x) * (a ^ 2)))) / (kds_P a r x * (kds_X a L ^ 2)))

noncomputable def kds_g11 (a M L r x : ℝ) : ℝ :=
  (kds_P a r x / kds_D a M L r)

noncomputable def kds_g22 (a L r x : ℝ) : ℝ :=
  (kds_P a r x / (kds_Q a L x * kds_S x))

lemma kds_g00_dr (a M L r x : ℝ) (hP : kds_P a r x ≠ 0) (hX : kds_X a L ≠ 0) :
    HasDerivAt (fun t => (kds_g00 a M L t x)) ((((2 * M) + ((-2:ℝ) * r * (1 + (((-1:ℝ) * L * (r ^ 2)) / 3))) + ((2 * L * r * ((a ^ 2) + (r ^ 2))) / 3)) / (kds_P a r x * (kds_X a L ^ 2))) + (((-2:ℝ) * r * (((-1:ℝ) * kds_D a M L r) + (kds_Q a L x * kds_S x * (a ^ 2)))) / ((kds_P a r x ^ 2) * (kds_X a L ^ 2)))) r := by
  have h := ((((hasDerivAt_const r ((-1:ℝ) : ℝ)).fun_mul (kds_D_dr a M L r)).fun_add (hasDerivAt_const r ((kds_Q a L x * kds_S x * (a ^ 2)) : ℝ))).fun_div ((kds_P_dr a r x).fun_mul (hasDerivAt_const r ((kds_X a L ^ 2) : ℝ))) (mul_ne_zero hP (pow_ne_zero 2 hX)))
  exact h.congr_deriv (by field_simp; ring)

lemma kds_g00_dx (a M L r x : ℝ) (hP : kds_P a r x ≠ 0) (hX : kds_X a L ≠ 0) :
    HasDerivAt (fun t => (kds_g00 a M L r t)) ((((-2:ℝ) * kds_Q a L x * x * (a ^ 2)) / (kds_P a r x * (kds_X a L ^ 2))) + (((-2:ℝ) * x * (a ^ 2) * (((-1:ℝ) * kds_D a M L r) + (kds_Q a L x * kds_S x * (a ^ 2)))) / ((kds_P a r x ^ 2) * (kds_X a L ^ 2))) + ((2 * L * kds_S x * x * (a ^ 4)) / (3 * kds_P a r x * (kds_X a L ^ 2)))) x := by
  have h := (((hasDerivAt_const x (((-1:ℝ) * kds_D a M L r) : ℝ)).fun_add (((kds_Q_dx a L x).fun_mul (kds_S_dx x)).fun_mul (hasDerivAt_const x ((a ^ 2) : ℝ)))).fun_div ((kds_P_dx a r x).fun_mul (hasDerivAt_const x ((kds_X a L ^ 2) : ℝ))) (mul_ne_zero hP (pow_ne_zero 2 hX)))
  exact h.congr_deriv (by field_simp; ring)

lemma kds_g03_dr (a M L r x : ℝ) (hP : kds_P a r x ≠ 0) (hX : kds_X a L ≠ 0) :
    HasDerivAt (fun t => (kds_g03 a M L t x)) (((kds_S x * a * (((-2:ℝ) * M) + (2 * r * (1 + (((-1:ℝ) * L * (r ^ 2)) / 3))) + (((-2:ℝ) * L * r * ((a ^ 2) + (r ^ 2))) / 3))) / (kds_P a r x * (kds_X a L ^ 2))) + (((-2:ℝ) * kds_Q a L x * kds_S x * a * r) / (kds_P a r x * (kds_X a L ^ 2))) + (((-2:ℝ) * kds_S x * a * r * (kds_D a M L r + ((-1:ℝ) * kds_Q a L x * ((a ^ 2) + (r ^ 2))))) / ((kds_P a r x ^ 2) * (kds_X a L ^ 2)))) r := by
  have h := ((((hasDerivAt_const r (kds_S x : ℝ)).fun_mul (hasDerivAt_const r (a : ℝ))).fun_mul ((kds_D_dr a M L r).fun_add (((hasDerivAt_const r ((-1:ℝ) : ℝ)).fun_mul (hasDerivAt_const r (kds_Q a L x : ℝ))).fun_mul ((hasDerivAt_const r ((a ^ 2) : ℝ)).fun_add ((hasDerivAt_id' r).fun_pow 2))))).fun_div ((kds_P_dr a r x).fun_mul (hasDerivAt_const r ((kds_X a L ^ 2) : ℝ))) (mul_ne_zero hP (pow_ne_zero 2 hX)))
  exact h.congr_deriv (by simp only [Nat.cast_ofNat]; field_simp; ring)

lemma kds_g03_dx (a M L r x : ℝ) (hP : kds_P a r x ≠ 0) (hX : kds_X a L ≠ 0) :
    HasDerivAt (fun t => (kds_g03 a M L r t)) ((((-2:ℝ) * a * x * (kds_D a M L r + ((-1:ℝ) * kds_Q a L x * ((a ^ 2) + (r ^ 2))))) / (kds_P a r x * (kds_X a L ^ 2))) + (((-2:ℝ) * kds_S x * x * (a ^ 3) * (kds_D a M L r + ((-1:ℝ) * kds_Q a L x * ((a ^ 2) + (r ^ 2))))) / ((kds_P a r x ^ 2) * (kds_X a L ^ 2))) + ((2 * L * kds_S x * x * (a ^ 3) * (((-1:ℝ) * (a ^ 2)) + ((-1:ℝ) * (r ^ 2)))) / (3 * kds_P a r x * (kds_X a L ^ 2)))) x := by
  have h := ((((kds_S_dx x).fun_mul (hasDerivAt_const x (a : ℝ))).fun_mul ((hasDerivAt_const x (kds_D a M L r : ℝ)).fun_add (((hasDerivAt_const x ((-1:ℝ) : ℝ)).fun_mul (kds_Q_dx a L x)).fun_mul (hasDerivAt_const x (((a ^ 2) + (r ^ 2)) : ℝ))))).fun_div ((kds_P_dx a r x).fun_mul (hasDerivAt_const x ((kds_X a L ^ 2) : ℝ))) (mul_ne_zero hP (pow_ne_zero 2 hX)))
  exact h.congr_deriv (by field_simp; ring)

lemma kds_g33_dr (a M L r x : ℝ) (hP : kds_P a r x ≠ 0) (hX : kds_X a L ≠ 0) :
    HasDerivAt (fun t => (kds_g33 a M L t x)) ((((-1:ℝ) * (kds_S x ^ 2) * (a ^ 2) * (((-2:ℝ) * M) + (2 * r * (1 + (((-1:ℝ) * L * (r ^ 2)) / 3))) + (((-2:ℝ) * L * r * ((a ^ 2) + (r ^ 2))) / 3))) / (kds_P a r x * (kds_X a L ^ 2))) + (((-2:ℝ) * kds_S x * r * ((kds_Q a L x * (((a ^ 2) + (r ^ 2)) ^ 2)) + ((-1:ℝ) * kds_D a M L r * kds_S x * (a ^ 2)))) / ((kds_P a r x ^ 2) * (kds_X a L ^ 2))) + ((4 * kds_Q a L x * kds_S x * r * ((a ^ 2) + (r ^ 2))) / (kds_P a r x * (kds_X a L ^ 2)))) r := by
  have h := (((hasDerivAt_const r (kds_S x : ℝ)).fun_mul (((hasDerivAt_const r (kds_Q a L x : ℝ)).fun_mul (((hasDerivAt_const r ((a ^ 2) : ℝ)).fun_add ((hasDerivAt_id' r).fun_pow 2)).fun_pow 2)).fun_add ((((hasDerivAt_const r ((-1:ℝ) : ℝ)).fun_mul (kds_D_dr a M L r)).fun_mul (hasDerivAt_const r (kds_S x : ℝ))).fun_mul (hasDerivAt_const r ((a ^ 2) : ℝ))))).fun_div ((kds_P_dr a r x).fun_mul (hasDerivAt_const r ((kds_X a L ^ 2) : ℝ))) (mul_ne_zero hP (pow_ne_zero 2 hX)))
  exact h.congr_deriv (by simp only [Nat.cast_ofNat]; field_simp; ring)

lemma kds_g33_dx (a M L r x : ℝ) (hP : kds_P a r x ≠ 0) (hX : kds_X a L ≠ 0) :
    HasDerivAt (fun t => (kds_g33 a M L r t)) (((-2:ℝ) * x * ((((kds_Q a L x * (((a ^ 2) + (r ^ 2)) ^ 2)) + ((-1:ℝ) * kds_D a M L r * kds_S x * (a ^ 2))) / (kds_P a r x * (kds_X a L ^ 2))) + (((-1:ℝ) * kds_D a M L r * kds_S x * (a ^ 2)) / (kds_P a r x * (kds_X a L ^ 2))))) + (((-2:ℝ) * kds_S x * x * (a ^ 2) * ((kds_Q a L x * (((a ^ 2) + (r ^ 2)) ^ 2)) + ((-1:ℝ) * kds_D a M L r * kds_S x * (a ^ 2)))) / ((kds_P a r x ^ 2) * (kds_X a L ^ 2))) + ((2 * L * kds_S x * x * (a ^ 2) * (((a ^ 2) + (r ^ 2)) ^ 2)) / (3 * kds_P a r x * (kds_X a L ^ 2)))) x := by
  have h := (((kds_S_dx x).fun_mul (((kds_Q_dx a L x).fun_mul (hasDerivAt_const x ((((a ^ 2) + (r ^ 2)) ^ 2) : ℝ))).fun_add ((((hasDerivAt_const x ((-1:ℝ) : ℝ)).fun_mul (hasDerivAt_const x (kds_D a M L r : ℝ))).fun_mul (kds_S_dx x)).fun_mul (hasDerivAt_const x ((a ^ 2) : ℝ))))).fun_div ((kds_P_dx a r x).fun_mul (hasDerivAt_const x ((kds_X a L ^ 2) : ℝ))) (mul_ne_zero hP (pow_ne_zero 2 hX)))
  exact h.congr_deriv (by field_simp; ring)

lemma kds_g11_dr (a M L r x : ℝ) (hD : kds_D a M L r ≠ 0) :
    HasDerivAt (fun t => (kds_g11 a M L t x)) (((2 * r) / kds_D a M L r) + (((-1:ℝ) * kds_P a r x * (((-2:ℝ) * M) + (2 * r * (1 + (((-1:ℝ) * L * (r ^ 2)) / 3))) + (((-2:ℝ) * L * r * ((a ^ 2) + (r ^ 2))) / 3))) / (kds_D a M L r ^ 2))) r := by
  have h := ((kds_P_dr a r x).fun_div (kds_D_dr a M L r) hD)
  exact h.congr_deriv (by field_simp; ring)

lemma kds_g11_dx (a M L r x : ℝ) (hD : kds_D a M L r ≠ 0) :
    HasDerivAt (fun t => (kds_g11 a M L r t)) ((2 * x * (a ^ 2)) / kds_D a M L r) x := by
  have h := ((kds_P_dx a r x).fun_div (hasDerivAt_const x (kds_D a M L r : ℝ)) hD)
  exact h.congr_deriv (by field_simp; ring)

lemma kds_g22_dr (a L r x : ℝ) (hQ : kds_Q a L x ≠ 0) (hS : kds_S x ≠ 0) :
    HasDerivAt (fun t => (kds_g22 a L t x)) ((2 * r) / (kds_Q a L x * kds_S x)) r := by
  have h := ((kds_P_dr a r x).fun_div (hasDerivAt_const r ((kds_Q a L x * kds_S x) : ℝ)) (mul_ne_zero hQ hS))
  exact h.congr_deriv (by field_simp; ring)

lemma kds_g22_dx (a L r x : ℝ) (hQ : kds_Q a L x ≠ 0) (hS : kds_S x ≠ 0) :
    HasDerivAt (fun t => (kds_g22 a L r t)) (((2 * kds_P a r x * x) / (kds_Q a L x * (kds_S x ^ 2))) + ((2 * x * (a ^ 2)) / (kds_Q a L x * kds_S x)) + (((-2:ℝ) * L * kds_P a r x * x * (a ^ 2)) / (3 * kds_S x * (kds_Q a L x ^ 2)))) x := by
  have h := ((kds_P_dx a r x).fun_div ((kds_Q_dx a L x).fun_mul (kds_S_dx x)) (mul_ne_zero hQ hS))
  exact h.congr_deriv (by field_simp; ring)

noncomputable def kds_i00 (a M L r x : ℝ) : ℝ :=
  ((((-1:ℝ) * (kds_X a L ^ 2)) * ((((((((((3 * (r ^ 4)) + ((3 * (a ^ 2)) * (r ^ 2))) + (3 * (a ^ 4) * (x ^ 2))) + ((L * (a ^ 2)) * (r ^ 4))) + ((L * (a ^ 4)) * (r ^ 2))) + (L * (a ^ 6) * (x ^ 2))) + (((3 * (a ^ 2)) * (r ^ 2)) * (x ^ 2))) + (((6 * M) * r) * (a ^ 2))) + (((L * (a ^ 4)) * (r ^ 2)) * (x ^ 2))) + (((((-6:ℝ) * M) * r) * (a ^ 2)) * (x ^ 2)))) / (((3 * kds_D a M L r) * kds_P a r x) * kds_Q a L x))

noncomputable def kds_i03 (a M L r x : ℝ) : ℝ :=
  (((((-1:ℝ) * a) * (kds_X a L ^ 2)) * (((((L * (r ^ 4)) + ((6 * M) * r)) + ((L * (a ^ 2)) * (r ^ 2))) + (L * (a ^ 4) * (x ^ 2))) + (((L * (a ^ 2)) * (r ^ 2)) * (x ^ 2)))) / (((3 * kds_D a M L r) * kds_P a r x) * kds_Q a L x))

noncomputable def kds_i33 (a M L r x : ℝ) : ℝ :=
  (((kds_X a L ^ 2) * (((((((3 * (r ^ 2)) + (((-1:ℝ) * L) * (r ^ 4))) + (((-6:ℝ) * M) * r)) + (3 * (a ^ 2) * (x ^ 2))) + (L * (a ^ 4) * (x ^ 4))) + ((((-1:ℝ) * L) * (a ^ 2)) * (r ^ 2))) + ((-1:ℝ) * L * (a ^ 4) * (x ^ 2)))) / ((((3 * kds_D a M L r) * kds_P a r x) * kds_Q a L x) * kds_S x))

noncomputable def kds_i11 (a M L r x : ℝ) : ℝ :=
  (kds_D a M L r / kds_P a r x)

noncomputable def kds_i22 (a L r x : ℝ) : ℝ :=
  ((kds_Q a L x * kds_S x) / kds_P a r x)

noncomputable def kds_G001 (a M L r x : ℝ) : ℝ :=
  ((((((-1:ℝ) * (a ^ 2)) / 3) + (((-1:ℝ) * (r ^ 2)) / 3)) * (((((L * (r ^ 5)) + (((-3:ℝ) * M) * (r ^ 2))) + (3 * M * (a ^ 2) * (x ^ 2))) + (((L * r) * (a ^ 4)) * (x ^ 4))) + ((((2 * L) * (a ^ 2)) * (r ^ 3)) * (x ^ 2)))) / (kds_D a M L r * (kds_P a r x ^ 2)))

noncomputable def kds_G002 (a M L r x : ℝ) : ℝ :=
  (((x * (a ^ 2)) * ((((L * (r ^ 4)) + ((6 * M) * r)) + (L * (a ^ 4) * (x ^ 4))) + ((((2 * L) * (a ^ 2)) * (r ^ 2)) * (x ^ 2)))) / ((3 * kds_Q a L x) * (kds_P a r x ^ 2)))

noncomputable def kds_G013 (a M L r x : ℝ) : ℝ :=
  ((((((-1:ℝ) * M) * kds_S x) * a) * ((((3 * (r ^ 4)) + ((a ^ 2) * (r ^ 2))) + ((-1:ℝ) * (a ^ 4) * (x ^ 2))) + (((a ^ 2) * (r ^ 2)) * (x ^ 2)))) / (kds_D a M L r * (kds_P a r x ^ 2)))

noncomputable def kds_G023 (a M L r x : ℝ) : ℝ :=
  (((((((-2:ℝ) * M) * kds_S x) * r) * x) * (a ^ 3)) / (kds_Q a L x * (kds_P a r x ^ 2)))

noncomputable def kds_G100 (a M L r x : ℝ) : ℝ :=
  ((((-1:ℝ) * kds_D a M L r) * (((((L * (r ^ 5)) + (((-3:ℝ) * M) * (r ^ 2))) + (3 * M * (a ^ 2) * (x ^ 2))) + (((L * r) * (a ^ 4)) * (x ^ 4))) + ((((2 * L) * (a ^ 2)) * (r ^ 3)) * (x ^ 2)))) / ((3 * (kds_P a r x ^ 3)) * (kds_X a L ^ 2)))

noncomputable def kds_G103 (a M L r x : ℝ) : ℝ :=
  ((((kds_D a M L r * kds_S x) * a) * (((((L * (r ^ 5)) + (((-3:ℝ) * M) * (r ^ 2))) + (3 * M * (a ^ 2) * (x ^ 2))) + (((L * r) * (a ^ 4)) * (x ^ 4))) + ((((2 * L) * (a ^ 2)) * (r ^ 3)) * (x ^ 2)))) / ((3 * (kds_P a r x ^ 3)) * (kds_X a L ^ 2)))

noncomputable def kds_G111 (a M L r x : ℝ) : ℝ :=
  ((((((((r * (a ^ 2)) + (((-1:ℝ) * M) * (r ^ 2))) + ((L * (r ^ 5)) / 3)) + (M * (a ^ 2) * (x ^ 2))) + ((((-1:ℝ) * r) * (a ^ 2)) * (x ^ 2))) + ((((L * r) * (a ^ 4)) * (x ^ 2)) / 3)) + (((((2 * L) * (a ^ 2)) * (r ^ 3)) * (x ^ 2)) / 3)) / (kds_D a M L r * kds_P a r x))

noncomputable def kds_G112 (a r x : ℝ) : ℝ :=
  ((x * (a ^ 2)) / kds_P a r x)

noncomputable def kds_G122 (a M L r x : ℝ) : ℝ :=
  ((((-1:ℝ) * kds_D a M L r) * r) / ((kds_P a r x * kds_Q a L x) * kds_S x))

noncomputable def kds_G133 (a M L r x : ℝ) : ℝ :=
  (((((-1:ℝ) * kds_D a M L r) * kds_S x) * ((((((((((3 * (r ^ 5)) + ((L * (a ^ 2)) * (r ^ 5))) + ((((-3:ℝ) * M) * (a ^ 2)) * (r ^ 2))) + ((-3:ℝ) * M * (a ^ 4) * (x ^ 4))) + (3 * M * (a ^ 4) * (x ^ 2))) + (((3 * r) * (a ^ 4)) * (x ^ 4))) + (((6 * (a ^ 2)) * (r ^ 3)) * (x ^ 2))) + (((L * r) * (a ^ 6)) * (x ^ 4))) + ((((2 * L) * (a ^ 4)) * (r ^ 3)) * (x ^ 2))) + ((((3 * M) * (a ^ 2)) * (r ^ 2)) * (x ^ 2)))) / ((3 * (kds_P a r x ^ 3)) * (kds_X a L ^ 2)))

noncomputable def kds_G200 (a M L r x : ℝ) : ℝ :=
  (((((kds_Q a L x * kds_S x) * x) * (a ^ 2)) * ((((L * (r ^ 4)) + ((6 * M) * r)) + (L * (a ^ 4) * (x ^ 4))) + ((((2 * L) * (a ^ 2)) * (r ^ 2)) * (x ^ 2)))) / ((3 * (kds_P a r x ^ 3)) * (kds_X a L ^ 2)))

noncomputable def kds_G203 (a M L r x : ℝ) : ℝ :=
  ((((((((-1:ℝ) * kds_Q a L x) * kds_S x) * a) * x) * ((a ^ 2) + (r ^ 2))) * ((((L * (r ^ 4)) + ((6 * M) * r)) + (L * (a ^ 4) * (x ^ 4))) + ((((2 * L) * (a ^ 2)) * (r ^ 2)) * (x ^ 2)))) / ((3 * (kds_P a r x ^ 3)) * (kds_X a L ^ 2)))

noncomputable def kds_G211 (a M L r x : ℝ) : ℝ :=
  (((-1:ℝ) * kds_Q a L x * kds_S x * x * (a ^ 2)) / (kds_D a M L r * kds_P a r x))

noncomputable def kds_G212 (a r x : ℝ) : ℝ :=
  (r / kds_P a r x)

noncomputable def kds_G222 (a L r x : ℝ) : ℝ :=
  ((x * (((((3 * (a ^ 2)) + (3 * (r ^ 2))) + (L * (a ^ 4) * (x ^ 4))) + ((((-1:ℝ) * L) * (a ^ 2)) * (r ^ 2))) + ((((2 * L) * (a ^ 2)) * (r ^ 2)) * (x ^ 2)))) / (((3 * kds_P a r x) * kds_Q a L x) * kds_S x))

noncomputable def kds_G233 (a M L r x : ℝ) : ℝ :=
  ((((kds_Q a L x * kds_S x) * x) * ((((((((((((((((3 * (r ^ 6)) + ((3 * (a ^ 2)) * (r ^ 4))) + (3 * (a ^ 6) * (x ^ 4))) + ((L * (a ^ 2)) * (r ^ 6))) + ((L * (a ^ 4)) * (r ^ 4))) + (L * (a ^ 8) * (x ^ 4))) + (((3 * (a ^ 4)) * (r ^ 2)) * (x ^ 4))) + (((6 * M) * r) * (a ^ 4))) + (((6 * (a ^ 2)) * (r ^ 4)) * (x ^ 2))) + (((6 * (a ^ 4)) * (r ^ 2)) * (x ^ 2))) + (((12 * M) * (a ^ 2)) * (r ^ 3))) + (((L * (a ^ 6)) * (r ^ 2)) * (x ^ 4))) + (((((-12:ℝ) * M) * (a ^ 2)) * (r ^ 3)) * (x ^ 2))) + (((((-6:ℝ) * M) * r) * (a ^ 4)) * (x ^ 4))) + ((((2 * L) * (a ^ 4)) * (r ^ 4)) * (x ^ 2))) + ((((2 * L) * (a ^ 6)) * (r ^ 2)) * (x ^ 2)))) / ((3 * (kds_P a r x ^ 3)) * (kds_X a L ^ 2)))

noncomputable def kds_G301 (a M L r x : ℝ) : ℝ :=
  ((((-1:ℝ) * a) * (((((L * (r ^ 5)) + (((-3:ℝ) * M) * (r ^ 2))) + (3 * M * (a ^ 2) * (x ^ 2))) + (((L * r) * (a ^ 4)) * (x ^ 4))) + ((((2 * L) * (a ^ 2)) * (r ^ 3)) * (x ^ 2)))) / ((3 * kds_D a M L r) * (kds_P a r x ^ 2)))

noncomputable def kds_G302 (a M L r x : ℝ) : ℝ :=
  (((a * x) * ((((L * (r ^ 4)) + ((6 * M) * r)) + (L * (a ^ 4) * (x ^ 4))) + ((((2 * L) * (a ^ 2)) * (r ^ 2)) * (x ^ 2)))) / (((3 * kds_Q a L x) * kds_S x) * (kds_P a r x ^ 2)))

noncomputable def kds_G313 (a M L r x : ℝ) : ℝ :=
  ((((((((((((r ^ 5) + (((-2:ℝ) * M) * (r ^ 4))) + ((((-1:ℝ) * L) * (r ^ 7)) / 3)) + (M * (a ^ 4) * (x ^ 2))) + ((r * (a ^ 4)) * (x ^ 4))) + ((((-1:ℝ) * M) * (a ^ 2)) * (r ^ 2))) + ((-1:ℝ) * M * (a ^ 4) * (x ^ 4))) + (((2 * (a ^ 2)) * (r ^ 3)) * (x ^ 2))) + (((((-1:ℝ) * M) * (a ^ 2)) * (r ^ 2)) * (x ^ 2))) + ((((((-2:ℝ) * L) * (a ^ 2)) * (r ^ 5)) * (x ^ 2)) / 3)) + ((((((-1:ℝ) * L) * (a ^ 4)) * (r ^ 3)) * (x ^ 4)) / 3)) / (kds_D a M L r * (kds_P a r x ^ 2)))

noncomputable def kds_G323 (a M L r x : ℝ) : ℝ :=
  ((((-1:ℝ) * x) * ((((((((3 * (r ^ 4)) + (3 * (a ^ 4) * (x ^ 4))) + (L * (a ^ 6) * (x ^ 6))) + (((6 * M) * r) * (a ^ 2))) + (((6 * (a ^ 2)) * (r ^ 2)) * (x ^ 2))) + (((L * (a ^ 2)) * (r ^ 4)) * (x ^ 2))) + (((((-6:ℝ) * M) * r) * (a ^ 2)) * (x ^ 2))) + ((((2 * L) * (a ^ 4)) * (r ^ 2)) * (x ^ 4)))) / (((3 * kds_Q a L x) * kds_S x) * (kds_P a r x ^ 2)))

lemma kds_G001_dr (a M L r x : ℝ) (hP : kds_P a r x ≠ 0) (hD : kds_D a M L r ≠ 0) :
    HasDerivAt (fun t => (kds_G001 a M L t x)) ((((-2:ℝ) * M * (r ^ 7)) + (2 * (M ^ 2) * (r ^ 6)) + (((-1:ℝ) * L * (r ^ 10)) / 3) + (((-1:ℝ) * (L ^ 2) * (r ^ 12)) / 9) + ((-4:ℝ) * M * (a ^ 2) * (r ^ 5)) + ((-2:ℝ) * M * (a ^ 4) * (r ^ 3)) + ((-2:ℝ) * (M ^ 2) * (a ^ 6) * (x ^ 4)) + (6 * (M ^ 2) * (a ^ 2) * (r ^ 4)) + (((-2:ℝ) * L * (a ^ 2) * (r ^ 8)) / 3) + (((-2:ℝ) * (L ^ 2) * (a ^ 2) * (r ^ 10)) / 9) + (((-1:ℝ) * L * (a ^ 4) * (r ^ 6)) / 3) + (((-1:ℝ) * L * (a ^ 10) * (x ^ 6)) / 3) + (((-1:ℝ) * (L ^ 2) * (a ^ 4) * (r ^ 8)) / 9) + ((8 * L * M * (r ^ 9)) / 3) + ((-1:ℝ) * L * (a ^ 2) * (r ^ 8) * (x ^ 2)) + ((-1:ℝ) * L * (a ^ 4) * (r ^ 6) * (x ^ 4)) + ((-1:ℝ) * L * (a ^ 6) * (r ^ 4) * (x ^ 2)) + ((-1:ℝ) * L * (a ^ 8) * (r ^ 2) * (x ^ 4)) + ((-12:ℝ) * (M ^ 2) * (a ^ 2) * (r ^ 4) * (x ^ 2)) + ((-12:ℝ) * (M ^ 2) * (a ^ 4) * (r ^ 2) * (x ^ 2)) + ((-2:ℝ) * L * (a ^ 4) * (r ^ 6) * (x ^ 2)) + ((-2:ℝ) * L * (a ^ 6) * (r ^ 4) * (x ^ 4)) + (2 * (M ^ 2) * (a ^ 4) * (r ^ 2) * (x ^ 4)) + (6 * M * r * (a ^ 6) * (x ^ 2)) + (6 * M * (a ^ 2) * (r ^ 5) * (x ^ 2)) + (12 * M * (a ^ 4) * (r ^ 3) * (x ^ 2)) + (((-2:ℝ) * L * (a ^ 8) * (r ^ 2) * (x ^ 6)) / 3) + (((-2:ℝ) * (L ^ 2) * (a ^ 4) * (r ^ 8) * (x ^ 2)) / 3) + (((-2:ℝ) * (L ^ 2) * (a ^ 6) * (r ^ 6) * (x ^ 4)) / 3) + (((-2:ℝ) * (L ^ 2) * (a ^ 8) * (r ^ 4) * (x ^ 6)) / 9) + (((-1:ℝ) * L * (a ^ 6) * (r ^ 4) * (x ^ 6)) / 3) + (((-1:ℝ) * (L ^ 2) * (a ^ 2) * (r ^ 10) * (x ^ 2)) / 3) + (((-1:ℝ) * (L ^ 2) * (a ^ 4) * (r ^ 8) * (x ^ 4)) / 3) + (((-1:ℝ) * (L ^ 2) * (a ^ 6) * (r ^ 6) * (x ^ 2)) / 3) + (((-1:ℝ) * (L ^ 2) * (a ^ 8) * (r ^ 4) * (x ^ 4)) / 3) + (((-1:ℝ) * (L ^ 2) * (a ^ 6) * (r ^ 6) * (x ^ 6)) / 9) + (((-1:ℝ) * (L ^ 2) * (a ^ 10) * (r ^ 2) * (x ^ 6)) / 9) + ((4 * L * M * (a ^ 4) * (r ^ 5)) / 3) + ((8 * L * M * (a ^ 2) * (r ^ 7)) / 3) + ((-4:ℝ) * L * M * (a ^ 4) * (r ^ 5) * (x ^ 2)) + ((-2:ℝ) * L * M * (a ^ 6) * (r ^ 3) * (x ^ 2)) + (2 * L * M * (a ^ 2) * (r ^ 7) * (x ^ 2)) + (((-4:ℝ) * L * M * (a ^ 6) * (r ^ 3) * (x ^ 4)) / 3) + (((-2:ℝ) * L * M * r * (a ^ 8) * (x ^ 4)) / 3) + ((4 * L * M * (a ^ 6) * (r ^ 3) * (x ^ 6)) / 3) + ((10 * L * M * (a ^ 4) * (r ^ 5) * (x ^ 4)) / 3)) / ((kds_D a M L r ^ 2) * (kds_P a r x ^ 3))) r := by
  have h := ((((hasDerivAt_const r ((((-1:ℝ) * (a ^ 2)) / 3) : ℝ)).fun_add (((hasDerivAt_const r ((-1:ℝ) : ℝ)).fun_mul ((hasDerivAt_id' r).fun_pow 2)).fun_div (hasDerivAt_const r (3 : ℝ)) (by norm_num))).fun_mul ((((((hasDerivAt_const r (L : ℝ)).fun_mul ((hasDerivAt_id' r).fun_pow 5)).fun_add (((hasDerivAt_const r ((-3:ℝ) : ℝ)).fun_mul (hasDerivAt_const r (M : ℝ))).fun_mul ((hasDerivAt_id' r).fun_pow 2))).fun_add (hasDerivAt_const r ((3 * M * (a ^ 2) * (x ^ 2)) : ℝ))).fun_add ((((hasDerivAt_const r (L : ℝ)).fun_mul (hasDerivAt_id' r)).fun_mul (hasDerivAt_const r ((a ^ 4) : ℝ))).fun_mul (hasDerivAt_const r ((x ^ 4) : ℝ)))).fun_add (((((hasDerivAt_const r (2 : ℝ)).fun_mul (hasDerivAt_const r (L : ℝ))).fun_mul (hasDerivAt_const r ((a ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' r).fun_pow 3)).fun_mul (hasDerivAt_const r ((x ^ 2) : ℝ))))).fun_div ((kds_D_dr a M L r).fun_mul ((kds_P_dr a r x).fun_pow 2)) (mul_ne_zero hD (pow_ne_zero 2 hP)))
  exact h.congr_deriv (by simp only [Nat.cast_ofNat]; field_simp; simp only [kds_P, kds_D]; ring)

lemma kds_G001_dx (a M L r x : ℝ) (hP : kds_P a r x ≠ 0) (hD : kds_D a M L r ≠ 0) :
    HasDerivAt (fun t => (kds_G001 a M L r t)) ((M * x * (a ^ 2) * (((-3:ℝ) * (r ^ 2)) + ((a ^ 2) * (x ^ 2))) * ((2 * (a ^ 2)) + (2 * (r ^ 2)))) / (kds_D a M L r * (kds_P a r x ^ 3))) x := by
  have h := (((hasDerivAt_const x (((((-1:ℝ) * (a ^ 2)) / 3) + (((-1:ℝ) * (r ^ 2)) / 3)) : ℝ)).fun_mul (((((hasDerivAt_const x ((L * (r ^ 5)) : ℝ)).fun_add (hasDerivAt_const x (((-3:ℝ) * M * (r ^ 2)) : ℝ))).fun_add ((((hasDerivAt_const x (3 : ℝ)).fun_mul (hasDerivAt_const x (M : ℝ))).fun_mul (hasDerivAt_const x ((a ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 2))).fun_add ((((hasDerivAt_const x (L : ℝ)).fun_mul (hasDerivAt_const x (r : ℝ))).fun_mul (hasDerivAt_const x ((a ^ 4) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 4))).fun_add (((((hasDerivAt_const x (2 : ℝ)).fun_mul (hasDerivAt_const x (L : ℝ))).fun_mul (hasDerivAt_const x ((a ^ 2) : ℝ))).fun_mul (hasDerivAt_const x ((r ^ 3) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 2)))).fun_div ((hasDerivAt_const x (kds_D a M L r : ℝ)).fun_mul ((kds_P_dx a r x).fun_pow 2)) (mul_ne_zero hD (pow_ne_zero 2 hP)))
  exact h.congr_deriv (by simp only [Nat.cast_ofNat]; field_simp; simp only [kds_P, kds_D]; ring)

lemma kds_G002_dr (a M L r x : ℝ) (hP : kds_P a r x ≠ 0) (hQ : kds_Q a L x ≠ 0) :
    HasDerivAt (fun t => (kds_G002 a M L t x)) ((2 * M * x * (a ^ 2) * (((-3:ℝ) * (r ^ 2)) + ((a ^ 2) * (x ^ 2)))) / (kds_Q a L x * (kds_P a r x ^ 3))) r := by
  have h := ((((hasDerivAt_const r (x : ℝ)).fun_mul (hasDerivAt_const r ((a ^ 2) : ℝ))).fun_mul (((((hasDerivAt_const r (L : ℝ)).fun_mul ((hasDerivAt_id' r).fun_pow 4)).fun_add (((hasDerivAt_const r (6 : ℝ)).fun_mul (hasDerivAt_const r (M : ℝ))).fun_mul (hasDerivAt_id' r))).fun_add (hasDerivAt_const r ((L * (a ^ 4) * (x ^ 4)) : ℝ))).fun_add (((((hasDerivAt_const r (2 : ℝ)).fun_mul (hasDerivAt_const r (L : ℝ))).fun_mul (hasDerivAt_const r ((a ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' r).fun_pow 2)).fun_mul (hasDerivAt_const r ((x ^ 2) : ℝ))))).fun_div (((hasDerivAt_const r (3 : ℝ)).fun_mul (hasDerivAt_const r (kds_Q a L x : ℝ))).fun_mul ((kds_P_dr a r x).fun_pow 2)) (mul_ne_zero (mul_ne_zero (by norm_num) hQ) (pow_ne_zero 2 hP)))
  exact h.congr_deriv (by simp only [Nat.cast_ofNat]; field_simp; simp only [kds_P, kds_Q]; ring)

lemma kds_G002_dx (a M L r x : ℝ) (hP : kds_P a r x ≠ 0) (hQ : kds_Q a L x ≠ 0) :
    HasDerivAt (fun t => (kds_G002 a M L r t)) (((-1:ℝ) * (a ^ 2) * (((-18:ℝ) * M * (r ^ 3)) + ((-3:ℝ) * L * (r ^ 6)) + ((L ^ 2) * (a ^ 8) * (x ^ 8)) + ((-3:ℝ) * L * (a ^ 6) * (x ^ 6)) + ((L ^ 2) * (a ^ 2) * (r ^ 6) * (x ^ 2)) + ((-9:ℝ) * L * (a ^ 2) * (r ^ 4) * (x ^ 2)) + ((-9:ℝ) * L * (a ^ 4) * (r ^ 2) * (x ^ 4)) + (3 * (L ^ 2) * (a ^ 4) * (r ^ 4) * (x ^ 4)) + (3 * (L ^ 2) * (a ^ 6) * (r ^ 2) * (x ^ 6)) + (54 * M * r * (a ^ 2) * (x ^ 2)) + (6 * L * M * (a ^ 2) * (r ^ 3) * (x ^ 2)) + (30 * L * M * r * (a ^ 4) * (x ^ 4)))) / (9 * (kds_P a r x ^ 3) * (kds_Q a L x ^ 2))) x := by
  have h := ((((hasDerivAt_id' x).fun_mul (hasDerivAt_const x ((a ^ 2) : ℝ))).fun_mul ((((hasDerivAt_const x ((L * (r ^ 4)) : ℝ)).fun_add (hasDerivAt_const x ((6 * M * r) : ℝ))).fun_add (((hasDerivAt_const x (L : ℝ)).fun_mul (hasDerivAt_const x ((a ^ 4) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 4))).fun_add (((((hasDerivAt_const x (2 : ℝ)).fun_mul (hasDerivAt_const x (L : ℝ))).fun_mul (hasDerivAt_const x ((a ^ 2) : ℝ))).fun_mul (hasDerivAt_const x ((r ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 2)))).fun_div (((hasDerivAt_const x (3 : ℝ)).fun_mul (kds_Q_dx a L x)).fun_mul ((kds_P_dx a r x).fun_pow 2)) (mul_ne_zero (mul_ne_zero (by norm_num) hQ) (pow_ne_zero 2 hP)))
  exact h.congr_deriv (by simp only [Nat.cast_ofNat]; field_simp; simp only [kds_P, kds_Q]; ring)

lemma kds_G013_dr (a M L r x : ℝ) (hP : kds_P a r x ≠ 0) (hD : kds_D a M L r ≠ 0) :
    HasDerivAt (fun t => (kds_G013 a M L t x)) (((-2:ℝ) * M * kds_S x * a * (((-9:ℝ) * (r ^ 7)) + ((-6:ℝ) * (a ^ 2) * (r ^ 5)) + ((-3:ℝ) * (a ^ 4) * (r ^ 3)) + (6 * L * (r ^ 9)) + (9 * M * (r ^ 6)) + ((-3:ℝ) * M * (a ^ 6) * (x ^ 4)) + (2 * L * (a ^ 4) * (r ^ 5)) + (3 * (a ^ 2) * (r ^ 5) * (x ^ 2)) + (6 * L * (a ^ 2) * (r ^ 7)) + (6 * r * (a ^ 6) * (x ^ 4)) + (9 * M * (a ^ 2) * (r ^ 4)) + (9 * r * (a ^ 6) * (x ^ 2)) + (24 * (a ^ 4) * (r ^ 3) * (x ^ 2)) + (L * (a ^ 4) * (r ^ 5) * (x ^ 4)) + ((-1:ℝ) * L * r * (a ^ 8) * (x ^ 4)) + ((-18:ℝ) * M * (a ^ 2) * (r ^ 4) * (x ^ 2)) + ((-18:ℝ) * M * (a ^ 4) * (r ^ 2) * (x ^ 2)) + ((-4:ℝ) * L * (a ^ 4) * (r ^ 5) * (x ^ 2)) + ((-3:ℝ) * L * (a ^ 6) * (r ^ 3) * (x ^ 2)) + ((-3:ℝ) * M * (a ^ 4) * (r ^ 2) * (x ^ 4)) + ((-2:ℝ) * L * (a ^ 6) * (r ^ 3) * (x ^ 4)) + (3 * L * (a ^ 2) * (r ^ 7) * (x ^ 2)))) / (3 * (kds_D a M L r ^ 2) * (kds_P a r x ^ 3))) r := by
  have h := ((((((hasDerivAt_const r ((-1:ℝ) : ℝ)).fun_mul (hasDerivAt_const r (M : ℝ))).fun_mul (hasDerivAt_const r (kds_S x : ℝ))).fun_mul (hasDerivAt_const r (a : ℝ))).fun_mul (((((hasDerivAt_const r (3 : ℝ)).fun_mul ((hasDerivAt_id' r).fun_pow 4)).fun_add ((hasDerivAt_const r ((a ^ 2) : ℝ)).fun_mul ((hasDerivAt_id' r).fun_pow 2))).fun_add (hasDerivAt_const r (((-1:ℝ) * (a ^ 4) * (x ^ 2)) : ℝ))).fun_add (((hasDerivAt_const r ((a ^ 2) : ℝ)).fun_mul ((hasDerivAt_id' r).fun_pow 2)).fun_mul (hasDerivAt_const r ((x ^ 2) : ℝ))))).fun_div ((kds_D_dr a M L r).fun_mul ((kds_P_dr a r x).fun_pow 2)) (mul_ne_zero hD (pow_ne_zero 2 hP)))
  exact h.congr_deriv (by simp only [Nat.cast_ofNat]; field_simp; simp only [kds_P, kds_D, kds_S]; ring)

lemma kds_G013_dx (a M L r x : ℝ) (hP : kds_P a r x ≠ 0) (hD : kds_D a M L r ≠ 0) :
    HasDerivAt (fun t => (kds_G013 a M L r t)) (((-2:ℝ) * M * a * x * (((a ^ 2) + (r ^ 2)) ^ 2) * (((-3:ℝ) * (r ^ 2)) + ((a ^ 2) * (x ^ 2)))) / (kds_D a M L r * (kds_P a r x ^ 3))) x := by
  have h := ((((((hasDerivAt_const x ((-1:ℝ) : ℝ)).fun_mul (hasDerivAt_const x (M : ℝ))).fun_mul (kds_S_dx x)).fun_mul (hasDerivAt_const x (a : ℝ))).fun_mul ((((hasDerivAt_const x ((3 * (r ^ 4)) : ℝ)).fun_add (hasDerivAt_const x (((a ^ 2) * (r ^ 2)) : ℝ))).fun_add (((hasDerivAt_const x ((-1:ℝ) : ℝ)).fun_mul (hasDerivAt_const x ((a ^ 4) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 2))).fun_add (((hasDerivAt_const x ((a ^ 2) : ℝ)).fun_mul (hasDerivAt_const x ((r ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 2)))).fun_div ((hasDerivAt_const x (kds_D a M L r : ℝ)).fun_mul ((kds_P_dx a r x).fun_pow 2)) (mul_ne_zero hD (pow_ne_zero 2 hP)))
  exact h.congr_deriv (by simp only [Nat.cast_ofNat]; field_simp; simp only [kds_P, kds_D, kds_S]; ring)

lemma kds_G023_dr (a M L r x : ℝ) (hP : kds_P a r x ≠ 0) (hQ : kds_Q a L x ≠ 0) :
    HasDerivAt (fun t => (kds_G023 a M L t x)) (((-2:ℝ) * M * kds_S x * x * (a ^ 3) * (((-3:ℝ) * (r ^ 2)) + ((a ^ 2) * (x ^ 2)))) / (kds_Q a L x * (kds_P a r x ^ 3))) r := by
  have h := (((((((hasDerivAt_const r ((-2:ℝ) : ℝ)).fun_mul (hasDerivAt_const r (M : ℝ))).fun_mul (hasDerivAt_const r (kds_S x : ℝ))).fun_mul (hasDerivAt_id' r)).fun_mul (hasDerivAt_const r (x : ℝ))).fun_mul (hasDerivAt_const r ((a ^ 3) : ℝ))).fun_div ((hasDerivAt_const r (kds_Q a L x : ℝ)).fun_mul ((kds_P_dr a r x).fun_pow 2)) (mul_ne_zero hQ (pow_ne_zero 2 hP)))
  exact h.congr_deriv (by simp only [Nat.cast_ofNat]; field_simp; simp only [kds_P, kds_Q, kds_S]; ring)

lemma kds_G023_dx (a M L r x : ℝ) (hP : kds_P a r x ≠ 0) (hQ : kds_Q a L x ≠ 0) :
    HasDerivAt (fun t => (kds_G023 a M L r t)) (((-2:ℝ) * M * r * (a ^ 3) * ((3 * (r ^ 2)) + ((-9:ℝ) * (a ^ 2) * (x ^ 2)) + ((-9:ℝ) * (r ^ 2) * (x ^ 2)) + (3 * (a ^ 2) * (x ^ 4)) + ((-5:ℝ) * L * (a ^ 4) * (x ^ 4)) + (3 * L * (a ^ 4) * (x ^ 6)) + ((-1:ℝ) * L * (a ^ 2) * (r ^ 2) * (x ^ 2)) + ((-1:ℝ) * L * (a ^ 2) * (r ^ 2) * (x ^ 4)))) / (3 * (kds_P a r x ^ 3) * (kds_Q a L x ^ 2))) x := by
  have h := (((((((hasDerivAt_const x ((-2:ℝ) : ℝ)).fun_mul (hasDerivAt_const x (M : ℝ))).fun_mul (kds_S_dx x)).fun_mul (hasDerivAt_const x (r : ℝ))).fun_mul (hasDerivAt_id' x)).fun_mul (hasDerivAt_const x ((a ^ 3) : ℝ))).fun_div ((kds_Q_dx a L x).fun_mul ((kds_P_dx a r x).fun_pow 2)) (mul_ne_zero hQ (pow_ne_zero 2 hP)))
  exact h.congr_deriv (by simp only [Nat.cast_ofNat]; field_simp; simp only [kds_P, kds_Q, kds_S]; ring)

lemma kds_G100_dr (a M L r x : ℝ) (hP : kds_P a r x ≠ 0) (hX : kds_X a L ≠ 0) :
    HasDerivAt (fun t => (kds_G100 a M L t x)) ((((-2:ℝ) * M * (r ^ 5)) + (6 * (M ^ 2) * (r ^ 4)) + (((-1:ℝ) * L * (r ^ 8)) / 3) + (((L ^ 2) * (r ^ 10)) / 3) + ((-4:ℝ) * M * (a ^ 2) * (r ^ 3)) + (2 * (M ^ 2) * (a ^ 4) * (x ^ 4)) + (((-1:ℝ) * L * (a ^ 8) * (x ^ 6)) / 3) + ((L * (a ^ 2) * (r ^ 6)) / 3) + (((L ^ 2) * (a ^ 2) * (r ^ 8)) / 9) + ((-1:ℝ) * L * (a ^ 6) * (r ^ 2) * (x ^ 6)) + ((-16:ℝ) * (M ^ 2) * (a ^ 2) * (r ^ 2) * (x ^ 2)) + ((-2:ℝ) * M * r * (a ^ 4) * (x ^ 4)) + (8 * M * r * (a ^ 4) * (x ^ 2)) + (8 * M * (a ^ 2) * (r ^ 3) * (x ^ 2)) + (((-7:ℝ) * L * (a ^ 4) * (r ^ 4) * (x ^ 4)) / 3) + (((-5:ℝ) * L * (a ^ 2) * (r ^ 6) * (x ^ 2)) / 3) + (((-1:ℝ) * L * (a ^ 6) * (r ^ 2) * (x ^ 4)) / 3) + ((L * (a ^ 4) * (r ^ 4) * (x ^ 2)) / 3) + (((L ^ 2) * (a ^ 8) * (r ^ 2) * (x ^ 6)) / 3) + ((2 * L * M * (a ^ 2) * (r ^ 5)) / 3) + ((5 * (L ^ 2) * (a ^ 4) * (r ^ 6) * (x ^ 2)) / 9) + ((5 * (L ^ 2) * (a ^ 6) * (r ^ 4) * (x ^ 6)) / 9) + ((7 * (L ^ 2) * (a ^ 6) * (r ^ 4) * (x ^ 4)) / 9) + ((11 * (L ^ 2) * (a ^ 2) * (r ^ 8) * (x ^ 2)) / 9) + ((13 * (L ^ 2) * (a ^ 4) * (r ^ 6) * (x ^ 4)) / 9) + (4 * L * M * (a ^ 4) * (r ^ 3) * (x ^ 4)) + (((-8:ℝ) * L * M * (a ^ 4) * (r ^ 3) * (x ^ 2)) / 3) + (((-4:ℝ) * L * M * (a ^ 2) * (r ^ 5) * (x ^ 2)) / 3) + ((2 * L * M * r * (a ^ 6) * (x ^ 4)) / 3) + ((4 * L * M * r * (a ^ 6) * (x ^ 6)) / 3)) / ((kds_P a r x ^ 4) * (kds_X a L ^ 2))) r := by
  have h := ((((hasDerivAt_const r ((-1:ℝ) : ℝ)).fun_mul (kds_D_dr a M L r)).fun_mul ((((((hasDerivAt_const r (L : ℝ)).fun_mul ((hasDerivAt_id' r).fun_pow 5)).fun_add (((hasDerivAt_const r ((-3:ℝ) : ℝ)).fun_mul (hasDerivAt_const r (M : ℝ))).fun_mul ((hasDerivAt_id' r).fun_pow 2))).fun_add (hasDerivAt_const r ((3 * M * (a ^ 2) * (x ^ 2)) : ℝ))).fun_add ((((hasDerivAt_const r (L : ℝ)).fun_mul (hasDerivAt_id' r)).fun_mul (hasDerivAt_const r ((a ^ 4) : ℝ))).fun_mul (hasDerivAt_const r ((x ^ 4) : ℝ)))).fun_add (((((hasDerivAt_const r (2 : ℝ)).fun_mul (hasDerivAt_const r (L : ℝ))).fun_mul (hasDerivAt_const r ((a ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' r).fun_pow 3)).fun_mul (hasDerivAt_const r ((x ^ 2) : ℝ))))).fun_div (((hasDerivAt_const r (3 : ℝ)).fun_mul ((kds_P_dr a r x).fun_pow 3)).fun_mul (hasDerivAt_const r ((kds_X a L ^ 2) : ℝ))) (mul_ne_zero (mul_ne_zero (by norm_num) (pow_ne_zero 3 hP)) (pow_ne_zero 2 hX)))
  exact h.congr_deriv (by simp only [Nat.cast_ofNat]; field_simp; simp only [kds_P, kds_D, kds_X]; ring)

lemma kds_G100_dx (a M L r x : ℝ) (hP : kds_P a r x ≠ 0) (hX : kds_X a L ≠ 0) :
    HasDerivAt (fun t => (kds_G100 a M L r t)) ((2 * kds_D a M L r * x * (a ^ 2) * ((L * (r ^ 5)) + ((-12:ℝ) * M * (r ^ 2)) + (6 * M * (a ^ 2) * (x ^ 2)) + (L * r * (a ^ 4) * (x ^ 4)) + (2 * L * (a ^ 2) * (r ^ 3) * (x ^ 2)))) / (3 * (kds_P a r x ^ 4) * (kds_X a L ^ 2))) x := by
  have h := ((((hasDerivAt_const x ((-1:ℝ) : ℝ)).fun_mul (hasDerivAt_const x (kds_D a M L r : ℝ))).fun_mul (((((hasDerivAt_const x ((L * (r ^ 5)) : ℝ)).fun_add (hasDerivAt_const x (((-3:ℝ) * M * (r ^ 2)) : ℝ))).fun_add ((((hasDerivAt_const x (3 : ℝ)).fun_mul (hasDerivAt_const x (M : ℝ))).fun_mul (hasDerivAt_const x ((a ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 2))).fun_add ((((hasDerivAt_const x (L : ℝ)).fun_mul (hasDerivAt_const x (r : ℝ))).fun_mul (hasDerivAt_const x ((a ^ 4) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 4))).fun_add (((((hasDerivAt_const x (2 : ℝ)).fun_mul (hasDerivAt_const x (L : ℝ))).fun_mul (hasDerivAt_const x ((a ^ 2) : ℝ))).fun_mul (hasDerivAt_const x ((r ^ 3) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 2)))).fun_div (((hasDerivAt_const x (3 : ℝ)).fun_mul ((kds_P_dx a r x).fun_pow 3)).fun_mul (hasDerivAt_const x ((kds_X a L ^ 2) : ℝ))) (mul_ne_zero (mul_ne_zero (by norm_num) (pow_ne_zero 3 hP)) (pow_ne_zero 2 hX)))
  exact h.congr_deriv (by simp only [Nat.cast_ofNat]; field_simp; simp only [kds_P, kds_D, kds_X]; ring)

lemma kds_G103_dr (a M L r x : ℝ) (hP : kds_P a r x ≠ 0) (hX : kds_X a L ≠ 0) :
    HasDerivAt (fun t => (kds_G103 a M L t x)) (((-1:ℝ) * kds_S x * a * (((-18:ℝ) * M * (r ^ 5)) + ((-3:ℝ) * L * (r ^ 8)) + (3 * (L ^ 2) * (r ^ 10)) + (54 * (M ^ 2) * (r ^ 4)) + ((L ^ 2) * (a ^ 2) * (r ^ 8)) + ((-36:ℝ) * M * (a ^ 2) * (r ^ 3)) + ((-3:ℝ) * L * (a ^ 8) * (x ^ 6)) + (3 * L * (a ^ 2) * (r ^ 6)) + (18 * (M ^ 2) * (a ^ 4) * (x ^ 4)) + ((-144:ℝ) * (M ^ 2) * (a ^ 2) * (r ^ 2) * (x ^ 2)) + ((-21:ℝ) * L * (a ^ 4) * (r ^ 4) * (x ^ 4)) + ((-18:ℝ) * M * r * (a ^ 4) * (x ^ 4)) + ((-15:ℝ) * L * (a ^ 2) * (r ^ 6) * (x ^ 2)) + ((-9:ℝ) * L * (a ^ 6) * (r ^ 2) * (x ^ 6)) + ((-3:ℝ) * L * (a ^ 6) * (r ^ 2) * (x ^ 4)) + (3 * L * (a ^ 4) * (r ^ 4) * (x ^ 2)) + (3 * (L ^ 2) * (a ^ 8) * (r ^ 2) * (x ^ 6)) + (5 * (L ^ 2) * (a ^ 4) * (r ^ 6) * (x ^ 2)) + (5 * (L ^ 2) * (a ^ 6) * (r ^ 4) * (x ^ 6)) + (6 * L * M * (a ^ 2) * (r ^ 5)) + (7 * (L ^ 2) * (a ^ 6) * (r ^ 4) * (x ^ 4)) + (11 * (L ^ 2) * (a ^ 2) * (r ^ 8) * (x ^ 2)) + (13 * (L ^ 2) * (a ^ 4) * (r ^ 6) * (x ^ 4)) + (72 * M * r * (a ^ 4) * (x ^ 2)) + (72 * M * (a ^ 2) * (r ^ 3) * (x ^ 2)) + ((-24:ℝ) * L * M * (a ^ 4) * (r ^ 3) * (x ^ 2)) + ((-12:ℝ) * L * M * (a ^ 2) * (r ^ 5) * (x ^ 2)) + (6 * L * M * r * (a ^ 6) * (x ^ 4)) + (12 * L * M * r * (a ^ 6) * (x ^ 6)) + (36 * L * M * (a ^ 4) * (r ^ 3) * (x ^ 4)))) / (9 * (kds_P a r x ^ 4) * (kds_X a L ^ 2))) r := by
  have h := (((((kds_D_dr a M L r).fun_mul (hasDerivAt_const r (kds_S x : ℝ))).fun_mul (hasDerivAt_const r (a : ℝ))).fun_mul ((((((hasDerivAt_const r (L : ℝ)).fun_mul ((hasDerivAt_id' r).fun_pow 5)).fun_add (((hasDerivAt_const r ((-3:ℝ) : ℝ)).fun_mul (hasDerivAt_const r (M : ℝ))).fun_mul ((hasDerivAt_id' r).fun_pow 2))).fun_add (hasDerivAt_const r ((3 * M * (a ^ 2) * (x ^ 2)) : ℝ))).fun_add ((((hasDerivAt_const r (L : ℝ)).fun_mul (hasDerivAt_id' r)).fun_mul (hasDerivAt_const r ((a ^ 4) : ℝ))).fun_mul (hasDerivAt_const r ((x ^ 4) : ℝ)))).fun_add (((((hasDerivAt_const r (2 : ℝ)).fun_mul (hasDerivAt_const r (L : ℝ))).fun_mul (hasDerivAt_const r ((a ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' r).fun_pow 3)).fun_mul (hasDerivAt_const r ((x ^ 2) : ℝ))))).fun_div (((hasDerivAt_const r (3 : ℝ)).fun_mul ((kds_P_dr a r x).fun_pow 3)).fun_mul (hasDerivAt_const r ((kds_X a L ^ 2) : ℝ))) (mul_ne_zero (mul_ne_zero (by norm_num) (pow_ne_zero 3 hP)) (pow_ne_zero 2 hX)))
  exact h.congr_deriv (by simp only [Nat.cast_ofNat]; field_simp; simp only [kds_P, kds_D, kds_S, kds_X]; ring)

lemma kds_G103_dx (a M L r x : ℝ) (hP : kds_P a r x ≠ 0) (hX : kds_X a L ≠ 0) :
    HasDerivAt (fun t => (kds_G103 a M L r t)) (((-2:ℝ) * kds_D a M L r * a * x * ((L * (r ^ 7)) + ((-3:ℝ) * M * (r ^ 4)) + (L * (a ^ 2) * (r ^ 5)) + ((-12:ℝ) * M * (a ^ 2) * (r ^ 2)) + ((-3:ℝ) * M * (a ^ 4) * (x ^ 4)) + (6 * M * (a ^ 4) * (x ^ 2)) + (L * r * (a ^ 6) * (x ^ 4)) + (L * (a ^ 4) * (r ^ 3) * (x ^ 4)) + (2 * L * (a ^ 2) * (r ^ 5) * (x ^ 2)) + (2 * L * (a ^ 4) * (r ^ 3) * (x ^ 2)) + (12 * M * (a ^ 2) * (r ^ 2) * (x ^ 2)))) / (3 * (kds_P a r x ^ 4) * (kds_X a L ^ 2))) x := by
  have h := (((((hasDerivAt_const x (kds_D a M L r : ℝ)).fun_mul (kds_S_dx x)).fun_mul (hasDerivAt_const x (a : ℝ))).fun_mul (((((hasDerivAt_const x ((L * (r ^ 5)) : ℝ)).fun_add (hasDerivAt_const x (((-3:ℝ) * M * (r ^ 2)) : ℝ))).fun_add ((((hasDerivAt_const x (3 : ℝ)).fun_mul (hasDerivAt_const x (M : ℝ))).fun_mul (hasDerivAt_const x ((a ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 2))).fun_add ((((hasDerivAt_const x (L : ℝ)).fun_mul (hasDerivAt_const x (r : ℝ))).fun_mul (hasDerivAt_const x ((a ^ 4) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 4))).fun_add (((((hasDerivAt_const x (2 : ℝ)).fun_mul (hasDerivAt_const x (L : ℝ))).fun_mul (hasDerivAt_const x ((a ^ 2) : ℝ))).fun_mul (hasDerivAt_const x ((r ^ 3) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 2)))).fun_div (((hasDerivAt_const x (3 : ℝ)).fun_mul ((kds_P_dx a r x).fun_pow 3)).fun_mul (hasDerivAt_const x ((kds_X a L ^ 2) : ℝ))) (mul_ne_zero (mul_ne_zero (by norm_num) (pow_ne_zero 3 hP)) (pow_ne_zero 2 hX)))
  exact h.congr_deriv (by simp only [Nat.cast_ofNat]; field_simp; simp only [kds_P, kds_D, kds_S, kds_X]; ring)

lemma kds_G111_dr (a M L r x : ℝ) (hP : kds_P a r x ≠ 0) (hD : kds_D a M L r ≠ 0) :
    HasDerivAt (fun t => (kds_G111 a M L t x)) ((((a ^ 6) * (x ^ 2)) + ((-1:ℝ) * (a ^ 4) * (r ^ 2)) + ((-1:ℝ) * (a ^ 6) * (x ^ 4)) + ((-3:ℝ) * (a ^ 2) * (r ^ 4)) + ((-2:ℝ) * (M ^ 2) * (r ^ 4)) + (2 * M * (r ^ 5)) + ((L * (r ^ 8)) / 3) + (((L ^ 2) * (r ^ 10)) / 9) + (L * (a ^ 4) * (r ^ 4)) + ((a ^ 4) * (r ^ 2) * (x ^ 4)) + (2 * (M ^ 2) * (a ^ 4) * (x ^ 4)) + (3 * (a ^ 2) * (r ^ 4) * (x ^ 2)) + (4 * M * (a ^ 2) * (r ^ 3)) + (((-8:ℝ) * L * M * (r ^ 7)) / 3) + (((-1:ℝ) * (L ^ 2) * (a ^ 2) * (r ^ 8)) / 9) + ((L * (a ^ 8) * (x ^ 4)) / 3) + ((8 * L * (a ^ 2) * (r ^ 6)) / 3) + ((-8:ℝ) * M * (a ^ 2) * (r ^ 3) * (x ^ 2)) + ((-4:ℝ) * M * r * (a ^ 4) * (x ^ 2)) + ((-2:ℝ) * M * r * (a ^ 4) * (x ^ 4)) + (8 * (M ^ 2) * (a ^ 2) * (r ^ 2) * (x ^ 2)) + (((-4:ℝ) * L * (a ^ 2) * (r ^ 6) * (x ^ 2)) / 3) + (((-2:ℝ) * L * M * (a ^ 2) * (r ^ 5)) / 3) + (((-1:ℝ) * L * (a ^ 4) * (r ^ 4) * (x ^ 4)) / 3) + (((L ^ 2) * (a ^ 6) * (r ^ 4) * (x ^ 2)) / 3) + (((L ^ 2) * (a ^ 6) * (r ^ 4) * (x ^ 4)) / 9) + (((L ^ 2) * (a ^ 8) * (r ^ 2) * (x ^ 4)) / 9) + ((2 * (L ^ 2) * (a ^ 4) * (r ^ 6) * (x ^ 4)) / 9) + ((4 * L * (a ^ 4) * (r ^ 4) * (x ^ 2)) / 3) + ((4 * L * (a ^ 6) * (r ^ 2) * (x ^ 4)) / 3) + ((4 * (L ^ 2) * (a ^ 4) * (r ^ 6) * (x ^ 2)) / 9) + ((5 * (L ^ 2) * (a ^ 2) * (r ^ 8) * (x ^ 2)) / 9) + (((-4:ℝ) * L * M * (a ^ 2) * (r ^ 5) * (x ^ 2)) / 3) + (((-4:ℝ) * L * M * (a ^ 4) * (r ^ 3) * (x ^ 4)) / 3) + ((2 * L * M * r * (a ^ 6) * (x ^ 4)) / 3) + ((8 * L * M * (a ^ 4) * (r ^ 3) * (x ^ 2)) / 3)) / ((kds_D a M L r ^ 2) * (kds_P a r x ^ 2))) r := by
  have h := (((((((((hasDerivAt_id' r).fun_mul (hasDerivAt_const r ((a ^ 2) : ℝ))).fun_add (((hasDerivAt_const r ((-1:ℝ) : ℝ)).fun_mul (hasDerivAt_const r (M : ℝ))).fun_mul ((hasDerivAt_id' r).fun_pow 2))).fun_add (((hasDerivAt_const r (L : ℝ)).fun_mul ((hasDerivAt_id' r).fun_pow 5)).fun_div (hasDerivAt_const r (3 : ℝ)) (by norm_num))).fun_add (hasDerivAt_const r ((M * (a ^ 2) * (x ^ 2)) : ℝ))).fun_add ((((hasDerivAt_const r ((-1:ℝ) : ℝ)).fun_mul (hasDerivAt_id' r)).fun_mul (hasDerivAt_const r ((a ^ 2) : ℝ))).fun_mul (hasDerivAt_const r ((x ^ 2) : ℝ)))).fun_add (((((hasDerivAt_const r (L : ℝ)).fun_mul (hasDerivAt_id' r)).fun_mul (hasDerivAt_const r ((a ^ 4) : ℝ))).fun_mul (hasDerivAt_const r ((x ^ 2) : ℝ))).fun_div (hasDerivAt_const r (3 : ℝ)) (by norm_num))).fun_add ((((((hasDerivAt_const r (2 : ℝ)).fun_mul (hasDerivAt_const r (L : ℝ))).fun_mul (hasDerivAt_const r ((a ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' r).fun_pow 3)).fun_mul (hasDerivAt_const r ((x ^ 2) : ℝ))).fun_div (hasDerivAt_const r (3 : ℝ)) (by norm_num))).fun_div ((kds_D_dr a M L r).fun_mul (kds_P_dr a r x)) (mul_ne_zero hD hP))
  exact h.congr_deriv (by simp only [Nat.cast_ofNat]; field_simp; simp only [kds_P, kds_D]; ring)

lemma kds_G111_dx (a M L r x : ℝ) (hP : kds_P a r x ≠ 0) (hD : kds_D a M L r ≠ 0) :
    HasDerivAt (fun t => (kds_G111 a M L r t)) (((-2:ℝ) * r * x * (a ^ 2)) / (kds_P a r x ^ 2)) x := by
  have h := ((((((((hasDerivAt_const x ((r * (a ^ 2)) : ℝ)).fun_add (hasDerivAt_const x (((-1:ℝ) * M * (r ^ 2)) : ℝ))).fun_add (hasDerivAt_const x (((L * (r ^ 5)) / 3) : ℝ))).fun_add (((hasDerivAt_const x (M : ℝ)).fun_mul (hasDerivAt_const x ((a ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 2))).fun_add ((((hasDerivAt_const x ((-1:ℝ) : ℝ)).fun_mul (hasDerivAt_const x (r : ℝ))).fun_mul (hasDerivAt_const x ((a ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 2))).fun_add (((((hasDerivAt_const x (L : ℝ)).fun_mul (hasDerivAt_const x (r : ℝ))).fun_mul (hasDerivAt_const x ((a ^ 4) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 2)).fun_div (hasDerivAt_const x (3 : ℝ)) (by norm_num))).fun_add ((((((hasDerivAt_const x (2 : ℝ)).fun_mul (hasDerivAt_const x (L : ℝ))).fun_mul (hasDerivAt_const x ((a ^ 2) : ℝ))).fun_mul (hasDerivAt_const x ((r ^ 3) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 2)).fun_div (hasDerivAt_const x (3 : ℝ)) (by norm_num))).fun_div ((hasDerivAt_const x (kds_D a M L r : ℝ)).fun_mul (kds_P_dx a r x)) (mul_ne_zero hD hP))
  exact h.congr_deriv (by simp only [Nat.cast_ofNat]; field_simp; simp only [kds_P, kds_D]; ring)

lemma kds_G112_dr (a r x : ℝ) (hP : kds_P a r x ≠ 0) :
    HasDerivAt (fun t => (kds_G112 a t x)) (((-2:ℝ) * r * x * (a ^ 2)) / (kds_P a r x ^ 2)) r := by
  have h := ((hasDerivAt_const r ((x * (a ^ 2)) : ℝ)).fun_div (kds_P_dr a r x) hP)
  exact h.congr_deriv (by field_simp; simp only [kds_P]; ring)

lemma kds_G112_dx (a r x : ℝ) (hP : kds_P a r x ≠ 0) :
    HasDerivAt (fun t => (kds_G112 a r t)) (((-1:ℝ) * (a ^ 2) * (r + (a * x)) * (((-1:ℝ) * r) + (a * x))) / (kds_P a r x ^ 2)) x := by
  have h := (((hasDerivAt_id' x).fun_mul (hasDerivAt_const x ((a ^ 2) : ℝ))).fun_div (kds_P_dx a r x) hP)
  exact h.congr_deriv (by field_simp; simp only [kds_P]; ring)

lemma kds_G122_dr (a M L r x : ℝ) (hP : kds_P a r x ≠ 0) (hQ : kds_Q a L x ≠ 0) (hS : kds_S x ≠ 0) :
    HasDerivAt (fun t => (kds_G122 a M L t x)) ((((-1:ℝ) * (r ^ 4)) + (L * (r ^ 6)) + ((a ^ 2) * (r ^ 2)) + ((-1:ℝ) * (a ^ 4) * (x ^ 2)) + ((-3:ℝ) * (a ^ 2) * (r ^ 2) * (x ^ 2)) + ((L * (a ^ 2) * (r ^ 4)) / 3) + (L * (a ^ 4) * (r ^ 2) * (x ^ 2)) + (4 * M * r * (a ^ 2) * (x ^ 2)) + ((5 * L * (a ^ 2) * (r ^ 4) * (x ^ 2)) / 3)) / (kds_Q a L x * kds_S x * (kds_P a r x ^ 2))) r := by
  have h := ((((hasDerivAt_const r ((-1:ℝ) : ℝ)).fun_mul (kds_D_dr a M L r)).fun_mul (hasDerivAt_id' r)).fun_div (((kds_P_dr a r x).fun_mul (hasDerivAt_const r (kds_Q a L x : ℝ))).fun_mul (hasDerivAt_const r (kds_S x : ℝ))) (mul_ne_zero (mul_ne_zero hP hQ) hS))
  exact h.congr_deriv (by field_simp; simp only [kds_P, kds_D, kds_Q, kds_S]; ring)

lemma kds_G122_dx (a M L r x : ℝ) (hP : kds_P a r x ≠ 0) (hQ : kds_Q a L x ≠ 0) (hS : kds_S x ≠ 0) :
    HasDerivAt (fun t => (kds_G122 a M L r t)) (((-2:ℝ) * kds_D a M L r * r * x * (((-3:ℝ) * (a ^ 2)) + (3 * (r ^ 2)) + (6 * (a ^ 2) * (x ^ 2)) + ((-1:ℝ) * L * (a ^ 2) * (r ^ 2)) + ((-2:ℝ) * L * (a ^ 4) * (x ^ 2)) + (3 * L * (a ^ 4) * (x ^ 4)) + (2 * L * (a ^ 2) * (r ^ 2) * (x ^ 2)))) / (3 * (kds_P a r x ^ 2) * (kds_Q a L x ^ 2) * (kds_S x ^ 2))) x := by
  have h := ((hasDerivAt_const x (((-1:ℝ) * kds_D a M L r * r) : ℝ)).fun_div (((kds_P_dx a r x).fun_mul (kds_Q_dx a L x)).fun_mul (kds_S_dx x)) (mul_ne_zero (mul_ne_zero hP hQ) hS))
  exact h.congr_deriv (by field_simp; simp only [kds_P, kds_D, kds_Q, kds_S]; ring)

lemma kds_G133_dr (a M L r x : ℝ) (hP : kds_P a r x ≠ 0) (hX : kds_X a L ≠ 0) :
    HasDerivAt (fun t => (kds_G133 a M L t x)) ((kds_S x * (((-9:ℝ) * (r ^ 8)) + ((-9:ℝ) * (a ^ 8) * (x ^ 6)) + (9 * L * (r ^ 10)) + (9 * (a ^ 2) * (r ^ 6)) + ((L ^ 2) * (a ^ 4) * (r ^ 8)) + ((-63:ℝ) * (a ^ 4) * (r ^ 4) * (x ^ 4)) + ((-45:ℝ) * (a ^ 2) * (r ^ 6) * (x ^ 2)) + ((-36:ℝ) * M * (a ^ 4) * (r ^ 3)) + ((-27:ℝ) * (a ^ 6) * (r ^ 2) * (x ^ 6)) + ((-18:ℝ) * M * (a ^ 2) * (r ^ 5)) + ((-18:ℝ) * (M ^ 2) * (a ^ 6) * (x ^ 6)) + ((-9:ℝ) * (a ^ 6) * (r ^ 2) * (x ^ 4)) + ((-3:ℝ) * L * (a ^ 10) * (x ^ 6)) + (3 * L * (a ^ 4) * (r ^ 6)) + (3 * (L ^ 2) * (a ^ 2) * (r ^ 10)) + (9 * (a ^ 4) * (r ^ 4) * (x ^ 2)) + (18 * (M ^ 2) * (a ^ 6) * (x ^ 4)) + (54 * (M ^ 2) * (a ^ 2) * (r ^ 4)) + ((-144:ℝ) * (M ^ 2) * (a ^ 4) * (r ^ 2) * (x ^ 2)) + ((-90:ℝ) * M * r * (a ^ 6) * (x ^ 4)) + ((-54:ℝ) * (M ^ 2) * (a ^ 2) * (r ^ 4) * (x ^ 2)) + ((-3:ℝ) * L * (a ^ 8) * (r ^ 2) * (x ^ 4)) + (3 * L * (a ^ 6) * (r ^ 4) * (x ^ 2)) + (3 * (L ^ 2) * (a ^ 10) * (r ^ 2) * (x ^ 6)) + (5 * (L ^ 2) * (a ^ 6) * (r ^ 6) * (x ^ 2)) + (5 * (L ^ 2) * (a ^ 8) * (r ^ 4) * (x ^ 6)) + (6 * L * M * (a ^ 4) * (r ^ 5)) + (7 * (L ^ 2) * (a ^ 8) * (r ^ 4) * (x ^ 4)) + (11 * (L ^ 2) * (a ^ 4) * (r ^ 8) * (x ^ 2)) + (13 * (L ^ 2) * (a ^ 6) * (r ^ 6) * (x ^ 4)) + (15 * L * (a ^ 6) * (r ^ 4) * (x ^ 6)) + (33 * L * (a ^ 2) * (r ^ 8) * (x ^ 2)) + (39 * L * (a ^ 4) * (r ^ 6) * (x ^ 4)) + (54 * M * r * (a ^ 6) * (x ^ 6)) + (54 * M * (a ^ 2) * (r ^ 5) * (x ^ 2)) + (72 * M * r * (a ^ 6) * (x ^ 2)) + (108 * M * (a ^ 4) * (r ^ 3) * (x ^ 2)) + (144 * (M ^ 2) * (a ^ 4) * (r ^ 2) * (x ^ 4)) + ((-24:ℝ) * L * M * (a ^ 6) * (r ^ 3) * (x ^ 2)) + ((-18:ℝ) * L * M * (a ^ 4) * (r ^ 5) * (x ^ 2)) + ((-12:ℝ) * L * M * (a ^ 6) * (r ^ 3) * (x ^ 6)) + (6 * L * M * r * (a ^ 8) * (x ^ 4)) + (6 * L * M * r * (a ^ 8) * (x ^ 6)) + (24 * L * M * (a ^ 4) * (r ^ 5) * (x ^ 4)) + (60 * L * M * (a ^ 6) * (r ^ 3) * (x ^ 4)))) / (9 * (kds_P a r x ^ 4) * (kds_X a L ^ 2))) r := by
  have h := (((((hasDerivAt_const r ((-1:ℝ) : ℝ)).fun_mul (kds_D_dr a M L r)).fun_mul (hasDerivAt_const r (kds_S x : ℝ))).fun_mul (((((((((((hasDerivAt_const r (3 : ℝ)).fun_mul ((hasDerivAt_id' r).fun_pow 5)).fun_add (((hasDerivAt_const r (L : ℝ)).fun_mul (hasDerivAt_const r ((a ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' r).fun_pow 5))).fun_add ((((hasDerivAt_const r ((-3:ℝ) : ℝ)).fun_mul (hasDerivAt_const r (M : ℝ))).fun_mul (hasDerivAt_const r ((a ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' r).fun_pow 2))).fun_add (hasDerivAt_const r (((-3:ℝ) * M * (a ^ 4) * (x ^ 4)) : ℝ))).fun_add (hasDerivAt_const r ((3 * M * (a ^ 4) * (x ^ 2)) : ℝ))).fun_add ((((hasDerivAt_const r (3 : ℝ)).fun_mul (hasDerivAt_id' r)).fun_mul (hasDerivAt_const r ((a ^ 4) : ℝ))).fun_mul (hasDerivAt_const r ((x ^ 4) : ℝ)))).fun_add ((((hasDerivAt_const r (6 : ℝ)).fun_mul (hasDerivAt_const r ((a ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' r).fun_pow 3)).fun_mul (hasDerivAt_const r ((x ^ 2) : ℝ)))).fun_add ((((hasDerivAt_const r (L : ℝ)).fun_mul (hasDerivAt_id' r)).fun_mul (hasDerivAt_const r ((a ^ 6) : ℝ))).fun_mul (hasDerivAt_const r ((x ^ 4) : ℝ)))).fun_add (((((hasDerivAt_const r (2 : ℝ)).fun_mul (hasDerivAt_const r (L : ℝ))).fun_mul (hasDerivAt_const r ((a ^ 4) : ℝ))).fun_mul ((hasDerivAt_id' r).fun_pow 3)).fun_mul (hasDerivAt_const r ((x ^ 2) : ℝ)))).fun_add (((((hasDerivAt_const r (3 : ℝ)).fun_mul (hasDerivAt_const r (M : ℝ))).fun_mul (hasDerivAt_const r ((a ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' r).fun_pow 2)).fun_mul (hasDerivAt_const r ((x ^ 2) : ℝ))))).fun_div (((hasDerivAt_const r (3 : ℝ)).fun_mul ((kds_P_dr a r x).fun_pow 3)).fun_mul (hasDerivAt_const r ((kds_X a L ^ 2) : ℝ))) (mul_ne_zero (mul_ne_zero (by norm_num) (pow_ne_zero 3 hP)) (pow_ne_zero 2 hX)))
  exact h.congr_deriv (by simp only [Nat.cast_ofNat]; field_simp; simp only [kds_P, kds_D, kds_S, kds_X]; ring)

lemma kds_G133_dx (a M L r x : ℝ) (hP : kds_P a r x ≠ 0) (hX : kds_X a L ≠ 0) :
    HasDerivAt (fun t => (kds_G133 a M L r t)) ((2 * kds_D a M L r * x * ((3 * (r ^ 7)) + (3 * (a ^ 2) * (r ^ 5)) + (L * (a ^ 2) * (r ^ 7)) + (L * (a ^ 4) * (r ^ 5)) + ((-12:ℝ) * M * (a ^ 4) * (r ^ 2)) + ((-6:ℝ) * M * (a ^ 2) * (r ^ 4)) + ((-6:ℝ) * M * (a ^ 6) * (x ^ 4)) + (3 * r * (a ^ 6) * (x ^ 4)) + (3 * (a ^ 4) * (r ^ 3) * (x ^ 4)) + (6 * M * (a ^ 6) * (x ^ 2)) + (6 * (a ^ 2) * (r ^ 5) * (x ^ 2)) + (6 * (a ^ 4) * (r ^ 3) * (x ^ 2)) + (L * r * (a ^ 8) * (x ^ 4)) + (L * (a ^ 6) * (r ^ 3) * (x ^ 4)) + ((-12:ℝ) * M * (a ^ 4) * (r ^ 2) * (x ^ 4)) + (2 * L * (a ^ 4) * (r ^ 5) * (x ^ 2)) + (2 * L * (a ^ 6) * (r ^ 3) * (x ^ 2)) + (6 * M * (a ^ 2) * (r ^ 4) * (x ^ 2)) + (24 * M * (a ^ 4) * (r ^ 2) * (x ^ 2)))) / (3 * (kds_P a r x ^ 4) * (kds_X a L ^ 2))) x := by
  have h := (((((hasDerivAt_const x ((-1:ℝ) : ℝ)).fun_mul (hasDerivAt_const x (kds_D a M L r : ℝ))).fun_mul (kds_S_dx x)).fun_mul ((((((((((hasDerivAt_const x ((3 * (r ^ 5)) : ℝ)).fun_add (hasDerivAt_const x ((L * (a ^ 2) * (r ^ 5)) : ℝ))).fun_add (hasDerivAt_const x (((-3:ℝ) * M * (a ^ 2) * (r ^ 2)) : ℝ))).fun_add ((((hasDerivAt_const x ((-3:ℝ) : ℝ)).fun_mul (hasDerivAt_const x (M : ℝ))).fun_mul (hasDerivAt_const x ((a ^ 4) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 4))).fun_add ((((hasDerivAt_const x (3 : ℝ)).fun_mul (hasDerivAt_const x (M : ℝ))).fun_mul (hasDerivAt_const x ((a ^ 4) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 2))).fun_add ((((hasDerivAt_const x (3 : ℝ)).fun_mul (hasDerivAt_const x (r : ℝ))).fun_mul (hasDerivAt_const x ((a ^ 4) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 4))).fun_add ((((hasDerivAt_const x (6 : ℝ)).fun_mul (hasDerivAt_const x ((a ^ 2) : ℝ))).fun_mul (hasDerivAt_const x ((r ^ 3) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 2))).fun_add ((((hasDerivAt_const x (L : ℝ)).fun_mul (hasDerivAt_const x (r : ℝ))).fun_mul (hasDerivAt_const x ((a ^ 6) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 4))).fun_add (((((hasDerivAt_const x (2 : ℝ)).fun_mul (hasDerivAt_const x (L : ℝ))).fun_mul (hasDerivAt_const x ((a ^ 4) : ℝ))).fun_mul (hasDerivAt_const x ((r ^ 3) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 2))).fun_add (((((hasDerivAt_const x (3 : ℝ)).fun_mul (hasDerivAt_const x (M : ℝ))).fun_mul (hasDerivAt_const x ((a ^ 2) : ℝ))).fun_mul (hasDerivAt_const x ((r ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 2)))).fun_div (((hasDerivAt_const x (3 : ℝ)).fun_mul ((kds_P_dx a r x).fun_pow 3)).fun_mul (hasDerivAt_const x ((kds_X a L ^ 2) : ℝ))) (mul_ne_zero (mul_ne_zero (by norm_num) (pow_ne_zero 3 hP)) (pow_ne_zero 2 hX)))
  exact h.congr_deriv (by simp only [Nat.cast_ofNat]; field_simp; simp only [kds_P, kds_D, kds_S, kds_X]; ring)

lemma kds_G200_dr (a M L r x : ℝ) (hP : kds_P a r x ≠ 0) (hX : kds_X a L ≠ 0) :
    HasDerivAt (fun t => (kds_G200 a M L t x)) (((-2:ℝ) * kds_Q a L x * kds_S x * x * (a ^ 2) * ((L * (r ^ 5)) + (15 * M * (r ^ 2)) + ((-3:ℝ) * M * (a ^ 2) * (x ^ 2)) + (L * r * (a ^ 4) * (x ^ 4)) + (2 * L * (a ^ 2) * (r ^ 3) * (x ^ 2)))) / (3 * (kds_P a r x ^ 4) * (kds_X a L ^ 2))) r := by
  have h := ((((((hasDerivAt_const r (kds_Q a L x : ℝ)).fun_mul (hasDerivAt_const r (kds_S x : ℝ))).fun_mul (hasDerivAt_const r (x : ℝ))).fun_mul (hasDerivAt_const r ((a ^ 2) : ℝ))).fun_mul (((((hasDerivAt_const r (L : ℝ)).fun_mul ((hasDerivAt_id' r).fun_pow 4)).fun_add (((hasDerivAt_const r (6 : ℝ)).fun_mul (hasDerivAt_const r (M : ℝ))).fun_mul (hasDerivAt_id' r))).fun_add (hasDerivAt_const r ((L * (a ^ 4) * (x ^ 4)) : ℝ))).fun_add (((((hasDerivAt_const r (2 : ℝ)).fun_mul (hasDerivAt_const r (L : ℝ))).fun_mul (hasDerivAt_const r ((a ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' r).fun_pow 2)).fun_mul (hasDerivAt_const r ((x ^ 2) : ℝ))))).fun_div (((hasDerivAt_const r (3 : ℝ)).fun_mul ((kds_P_dr a r x).fun_pow 3)).fun_mul (hasDerivAt_const r ((kds_X a L ^ 2) : ℝ))) (mul_ne_zero (mul_ne_zero (by norm_num) (pow_ne_zero 3 hP)) (pow_ne_zero 2 hX)))
  exact h.congr_deriv (by simp only [Nat.cast_ofNat]; field_simp; simp only [kds_P, kds_Q, kds_S, kds_X]; ring)

lemma kds_G200_dx (a M L r x : ℝ) (hP : kds_P a r x ≠ 0) (hX : kds_X a L ≠ 0) :
    HasDerivAt (fun t => (kds_G200 a M L r t)) (((-1:ℝ) * (a ^ 2) * (((-18:ℝ) * M * (r ^ 3)) + ((-3:ℝ) * L * (r ^ 6)) + ((-1:ℝ) * (L ^ 2) * (a ^ 8) * (x ^ 8)) + (3 * L * (a ^ 6) * (x ^ 6)) + (3 * L * (a ^ 6) * (x ^ 8)) + (3 * (L ^ 2) * (a ^ 8) * (x ^ 10)) + (9 * L * (r ^ 6) * (x ^ 2)) + (54 * M * (r ^ 3) * (x ^ 2)) + ((-54:ℝ) * M * r * (a ^ 2) * (x ^ 4)) + ((-7:ℝ) * (L ^ 2) * (a ^ 4) * (r ^ 4) * (x ^ 4)) + ((-5:ℝ) * (L ^ 2) * (a ^ 6) * (r ^ 2) * (x ^ 6)) + ((-3:ℝ) * L * (a ^ 2) * (r ^ 4) * (x ^ 2)) + ((-3:ℝ) * (L ^ 2) * (a ^ 2) * (r ^ 6) * (x ^ 2)) + (3 * L * (a ^ 4) * (r ^ 2) * (x ^ 4)) + (5 * (L ^ 2) * (a ^ 2) * (r ^ 6) * (x ^ 4)) + (11 * (L ^ 2) * (a ^ 6) * (r ^ 2) * (x ^ 8)) + (13 * (L ^ 2) * (a ^ 4) * (r ^ 4) * (x ^ 6)) + (15 * L * (a ^ 4) * (r ^ 2) * (x ^ 6)) + (21 * L * (a ^ 2) * (r ^ 4) * (x ^ 4)) + (90 * M * r * (a ^ 2) * (x ^ 2)) + ((-18:ℝ) * L * M * (a ^ 2) * (r ^ 3) * (x ^ 2)) + ((-6:ℝ) * L * M * r * (a ^ 4) * (x ^ 6)) + (18 * L * M * r * (a ^ 4) * (x ^ 4)) + (30 * L * M * (a ^ 2) * (r ^ 3) * (x ^ 4)))) / (9 * (kds_P a r x ^ 4) * (kds_X a L ^ 2))) x := by
  have h := ((((((kds_Q_dx a L x).fun_mul (kds_S_dx x)).fun_mul (hasDerivAt_id' x)).fun_mul (hasDerivAt_const x ((a ^ 2) : ℝ))).fun_mul ((((hasDerivAt_const x ((L * (r ^ 4)) : ℝ)).fun_add (hasDerivAt_const x ((6 * M * r) : ℝ))).fun_add (((hasDerivAt_const x (L : ℝ)).fun_mul (hasDerivAt_const x ((a ^ 4) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 4))).fun_add (((((hasDerivAt_const x (2 : ℝ)).fun_mul (hasDerivAt_const x (L : ℝ))).fun_mul (hasDerivAt_const x ((a ^ 2) : ℝ))).fun_mul (hasDerivAt_const x ((r ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 2)))).fun_div (((hasDerivAt_const x (3 : ℝ)).fun_mul ((kds_P_dx a r x).fun_pow 3)).fun_mul (hasDerivAt_const x ((kds_X a L ^ 2) : ℝ))) (mul_ne_zero (mul_ne_zero (by norm_num) (pow_ne_zero 3 hP)) (pow_ne_zero 2 hX)))
  exact h.congr_deriv (by simp only [Nat.cast_ofNat]; field_simp; simp only [kds_P, kds_Q, kds_S, kds_X]; ring)

lemma kds_G203_dr (a M L r x : ℝ) (hP : kds_P a r x ≠ 0) (hX : kds_X a L ≠ 0) :
    HasDerivAt (fun t => (kds_G203 a M L t x)) (((-2:ℝ) * kds_Q a L x * kds_S x * a * x * (((-9:ℝ) * M * (r ^ 4)) + ((-1:ℝ) * L * (a ^ 2) * (r ^ 5)) + ((-15:ℝ) * M * (a ^ 2) * (r ^ 2)) + (3 * M * (a ^ 4) * (x ^ 2)) + (L * r * (a ^ 6) * (x ^ 6)) + (L * (a ^ 2) * (r ^ 5) * (x ^ 2)) + ((-1:ℝ) * L * r * (a ^ 6) * (x ^ 4)) + ((-2:ℝ) * L * (a ^ 4) * (r ^ 3) * (x ^ 2)) + (2 * L * (a ^ 4) * (r ^ 3) * (x ^ 4)) + (9 * M * (a ^ 2) * (r ^ 2) * (x ^ 2)))) / (3 * (kds_P a r x ^ 4) * (kds_X a L ^ 2))) r := by
  have h := ((((((((hasDerivAt_const r ((-1:ℝ) : ℝ)).fun_mul (hasDerivAt_const r (kds_Q a L x : ℝ))).fun_mul (hasDerivAt_const r (kds_S x : ℝ))).fun_mul (hasDerivAt_const r (a : ℝ))).fun_mul (hasDerivAt_const r (x : ℝ))).fun_mul ((hasDerivAt_const r ((a ^ 2) : ℝ)).fun_add ((hasDerivAt_id' r).fun_pow 2))).fun_mul (((((hasDerivAt_const r (L : ℝ)).fun_mul ((hasDerivAt_id' r).fun_pow 4)).fun_add (((hasDerivAt_const r (6 : ℝ)).fun_mul (hasDerivAt_const r (M : ℝ))).fun_mul (hasDerivAt_id' r))).fun_add (hasDerivAt_const r ((L * (a ^ 4) * (x ^ 4)) : ℝ))).fun_add (((((hasDerivAt_const r (2 : ℝ)).fun_mul (hasDerivAt_const r (L : ℝ))).fun_mul (hasDerivAt_const r ((a ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' r).fun_pow 2)).fun_mul (hasDerivAt_const r ((x ^ 2) : ℝ))))).fun_div (((hasDerivAt_const r (3 : ℝ)).fun_mul ((kds_P_dr a r x).fun_pow 3)).fun_mul (hasDerivAt_const r ((kds_X a L ^ 2) : ℝ))) (mul_ne_zero (mul_ne_zero (by norm_num) (pow_ne_zero 3 hP)) (pow_ne_zero 2 hX)))
  exact h.congr_deriv (by simp only [Nat.cast_ofNat]; field_simp; simp only [kds_P, kds_Q, kds_S, kds_X]; ring)

lemma kds_G203_dx (a M L r x : ℝ) (hP : kds_P a r x ≠ 0) (hX : kds_X a L ≠ 0) :
    HasDerivAt (fun t => (kds_G203 a M L r t)) ((a * (((a ^ 2) / 9) + ((r ^ 2) / 9)) * (((-18:ℝ) * M * (r ^ 3)) + ((-3:ℝ) * L * (r ^ 6)) + ((-1:ℝ) * (L ^ 2) * (a ^ 8) * (x ^ 8)) + (3 * L * (a ^ 6) * (x ^ 6)) + (3 * L * (a ^ 6) * (x ^ 8)) + (3 * (L ^ 2) * (a ^ 8) * (x ^ 10)) + (9 * L * (r ^ 6) * (x ^ 2)) + (54 * M * (r ^ 3) * (x ^ 2)) + ((-54:ℝ) * M * r * (a ^ 2) * (x ^ 4)) + ((-7:ℝ) * (L ^ 2) * (a ^ 4) * (r ^ 4) * (x ^ 4)) + ((-5:ℝ) * (L ^ 2) * (a ^ 6) * (r ^ 2) * (x ^ 6)) + ((-3:ℝ) * L * (a ^ 2) * (r ^ 4) * (x ^ 2)) + ((-3:ℝ) * (L ^ 2) * (a ^ 2) * (r ^ 6) * (x ^ 2)) + (3 * L * (a ^ 4) * (r ^ 2) * (x ^ 4)) + (5 * (L ^ 2) * (a ^ 2) * (r ^ 6) * (x ^ 4)) + (11 * (L ^ 2) * (a ^ 6) * (r ^ 2) * (x ^ 8)) + (13 * (L ^ 2) * (a ^ 4) * (r ^ 4) * (x ^ 6)) + (15 * L * (a ^ 4) * (r ^ 2) * (x ^ 6)) + (21 * L * (a ^ 2) * (r ^ 4) * (x ^ 4)) + (90 * M * r * (a ^ 2) * (x ^ 2)) + ((-18:ℝ) * L * M * (a ^ 2) * (r ^ 3) * (x ^ 2)) + ((-6:ℝ) * L * M * r * (a ^ 4) * (x ^ 6)) + (18 * L * M * r * (a ^ 4) * (x ^ 4)) + (30 * L * M * (a ^ 2) * (r ^ 3) * (x ^ 4)))) / ((kds_P a r x ^ 4) * (kds_X a L ^ 2))) x := by
  have h := ((((((((hasDerivAt_const x ((-1:ℝ) : ℝ)).fun_mul (kds_Q_dx a L x)).fun_mul (kds_S_dx x)).fun_mul (hasDerivAt_const x (a : ℝ))).fun_mul (hasDerivAt_id' x)).fun_mul (hasDerivAt_const x (((a ^ 2) + (r ^ 2)) : ℝ))).fun_mul ((((hasDerivAt_const x ((L * (r ^ 4)) : ℝ)).fun_add (hasDerivAt_const x ((6 * M * r) : ℝ))).fun_add (((hasDerivAt_const x (L : ℝ)).fun_mul (hasDerivAt_const x ((a ^ 4) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 4))).fun_add (((((hasDerivAt_const x (2 : ℝ)).fun_mul (hasDerivAt_const x (L : ℝ))).fun_mul (hasDerivAt_const x ((a ^ 2) : ℝ))).fun_mul (hasDerivAt_const x ((r ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 2)))).fun_div (((hasDerivAt_const x (3 : ℝ)).fun_mul ((kds_P_dx a r x).fun_pow 3)).fun_mul (hasDerivAt_const x ((kds_X a L ^ 2) : ℝ))) (mul_ne_zero (mul_ne_zero (by norm_num) (pow_ne_zero 3 hP)) (pow_ne_zero 2 hX)))
  exact h.congr_deriv (by simp only [Nat.cast_ofNat]; field_simp; simp only [kds_P, kds_Q, kds_S, kds_X]; ring)

lemma kds_G211_dr (a M L r x : ℝ) (hP : kds_P a r x ≠ 0) (hD : kds_D a M L r ≠ 0) :
    HasDerivAt (fun t => (kds_G211 a M L t x)) (((-2:ℝ) * kds_Q a L x * kds_S x * x * (a ^ 2) * (((-6:ℝ) * (r ^ 3)) + ((-3:ℝ) * r * (a ^ 2)) + (3 * L * (r ^ 5)) + (9 * M * (r ^ 2)) + ((-3:ℝ) * r * (a ^ 2) * (x ^ 2)) + (2 * L * (a ^ 2) * (r ^ 3)) + (3 * M * (a ^ 2) * (x ^ 2)) + (L * r * (a ^ 4) * (x ^ 2)) + (2 * L * (a ^ 2) * (r ^ 3) * (x ^ 2)))) / (3 * (kds_D a M L r ^ 2) * (kds_P a r x ^ 2))) r := by
  have h := ((hasDerivAt_const r (((-1:ℝ) * kds_Q a L x * kds_S x * x * (a ^ 2)) : ℝ)).fun_div ((kds_D_dr a M L r).fun_mul (kds_P_dr a r x)) (mul_ne_zero hD hP))
  exact h.congr_deriv (by field_simp; simp only [kds_P, kds_D, kds_Q, kds_S]; ring)

lemma kds_G211_dx (a M L r x : ℝ) (hP : kds_P a r x ≠ 0) (hD : kds_D a M L r ≠ 0) :
    HasDerivAt (fun t => (kds_G211 a M L r t)) (((a ^ 2) * (((-3:ℝ) * (r ^ 2)) + (3 * (a ^ 2) * (x ^ 2)) + (3 * (a ^ 2) * (x ^ 4)) + (9 * (r ^ 2) * (x ^ 2)) + ((-1:ℝ) * L * (a ^ 4) * (x ^ 4)) + (3 * L * (a ^ 4) * (x ^ 6)) + ((-3:ℝ) * L * (a ^ 2) * (r ^ 2) * (x ^ 2)) + (5 * L * (a ^ 2) * (r ^ 2) * (x ^ 4)))) / (3 * kds_D a M L r * (kds_P a r x ^ 2))) x := by
  have h := ((((((hasDerivAt_const x ((-1:ℝ) : ℝ)).fun_mul (kds_Q_dx a L x)).fun_mul (kds_S_dx x)).fun_mul (hasDerivAt_id' x)).fun_mul (hasDerivAt_const x ((a ^ 2) : ℝ))).fun_div ((hasDerivAt_const x (kds_D a M L r : ℝ)).fun_mul (kds_P_dx a r x)) (mul_ne_zero hD hP))
  exact h.congr_deriv (by field_simp; simp only [kds_P, kds_D, kds_Q, kds_S]; ring)

lemma kds_G212_dr (a r x : ℝ) (hP : kds_P a r x ≠ 0) :
    HasDerivAt (fun t => (kds_G212 a t x)) (((r + (a * x)) * (((-1:ℝ) * r) + (a * x))) / (kds_P a r x ^ 2)) r := by
  have h := ((hasDerivAt_id' r).fun_div (kds_P_dr a r x) hP)
  exact h.congr_deriv (by field_simp; simp only [kds_P]; ring)

lemma kds_G212_dx (a r x : ℝ) (hP : kds_P a r x ≠ 0) :
    HasDerivAt (fun t => (kds_G212 a r t)) (((-2:ℝ) * r * x * (a ^ 2)) / (kds_P a r x ^ 2)) x := by
  have h := ((hasDerivAt_const x (r : ℝ)).fun_div (kds_P_dx a r x) hP)
  exact h.congr_deriv (by field_simp; simp only [kds_P]; ring)

lemma kds_G222_dr (a L r x : ℝ) (hP : kds_P a r x ≠ 0) (hQ : kds_Q a L x ≠ 0) (hS : kds_S x ≠ 0) :
    HasDerivAt (fun t => (kds_G222 a L t x)) (((-2:ℝ) * r * x * (a ^ 2)) / (kds_P a r x ^ 2)) r := by
  have h := (((hasDerivAt_const r (x : ℝ)).fun_mul (((((hasDerivAt_const r ((3 * (a ^ 2)) : ℝ)).fun_add ((hasDerivAt_const r (3 : ℝ)).fun_mul ((hasDerivAt_id' r).fun_pow 2))).fun_add (hasDerivAt_const r ((L * (a ^ 4) * (x ^ 4)) : ℝ))).fun_add ((((hasDerivAt_const r ((-1:ℝ) : ℝ)).fun_mul (hasDerivAt_const r (L : ℝ))).fun_mul (hasDerivAt_const r ((a ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' r).fun_pow 2))).fun_add (((((hasDerivAt_const r (2 : ℝ)).fun_mul (hasDerivAt_const r (L : ℝ))).fun_mul (hasDerivAt_const r ((a ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' r).fun_pow 2)).fun_mul (hasDerivAt_const r ((x ^ 2) : ℝ))))).fun_div ((((hasDerivAt_const r (3 : ℝ)).fun_mul (kds_P_dr a r x)).fun_mul (hasDerivAt_const r (kds_Q a L x : ℝ))).fun_mul (hasDerivAt_const r (kds_S x : ℝ))) (mul_ne_zero (mul_ne_zero (mul_ne_zero (by norm_num) hP) hQ) hS))
  exact h.congr_deriv (by simp only [Nat.cast_ofNat]; field_simp; simp only [kds_P, kds_Q, kds_S]; ring)

lemma kds_G222_dx (a L r x : ℝ) (hP : kds_P a r x ≠ 0) (hQ : kds_Q a L x ≠ 0) (hS : kds_S x ≠ 0) :
    HasDerivAt (fun t => (kds_G222 a L r t)) (((r ^ 4) + ((a ^ 2) * (r ^ 2)) + ((r ^ 4) * (x ^ 2)) + ((-1:ℝ) * (a ^ 4) * (x ^ 2)) + (3 * (a ^ 4) * (x ^ 4)) + ((-1:ℝ) * L * (a ^ 6) * (x ^ 4)) + (3 * (a ^ 2) * (r ^ 2) * (x ^ 4)) + (((-1:ℝ) * L * (a ^ 2) * (r ^ 4)) / 3) + (((-1:ℝ) * L * (a ^ 6) * (x ^ 8)) / 3) + (((L ^ 2) * (a ^ 8) * (x ^ 8)) / 9) + (((L ^ 2) * (a ^ 8) * (x ^ 10)) / 9) + ((8 * L * (a ^ 6) * (x ^ 6)) / 3) + (((-4:ℝ) * (L ^ 2) * (a ^ 6) * (r ^ 2) * (x ^ 6)) / 9) + (((-1:ℝ) * (L ^ 2) * (a ^ 4) * (r ^ 4) * (x ^ 4)) / 9) + ((L * (a ^ 2) * (r ^ 4) * (x ^ 4)) / 3) + (((L ^ 2) * (a ^ 6) * (r ^ 2) * (x ^ 4)) / 3) + (((L ^ 2) * (a ^ 4) * (r ^ 4) * (x ^ 2)) / 9) + ((2 * (L ^ 2) * (a ^ 4) * (r ^ 4) * (x ^ 6)) / 9) + ((4 * L * (a ^ 2) * (r ^ 4) * (x ^ 2)) / 3) + ((4 * L * (a ^ 4) * (r ^ 2) * (x ^ 4)) / 3) + ((4 * L * (a ^ 4) * (r ^ 2) * (x ^ 6)) / 3) + ((5 * (L ^ 2) * (a ^ 6) * (r ^ 2) * (x ^ 8)) / 9)) / ((kds_P a r x ^ 2) * (kds_Q a L x ^ 2) * (kds_S x ^ 2))) x := by
  have h := (((hasDerivAt_id' x).fun_mul (((((hasDerivAt_const x ((3 * (a ^ 2)) : ℝ)).fun_add (hasDerivAt_const x ((3 * (r ^ 2)) : ℝ))).fun_add (((hasDerivAt_const x (L : ℝ)).fun_mul (hasDerivAt_const x ((a ^ 4) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 4))).fun_add (hasDerivAt_const x (((-1:ℝ) * L * (a ^ 2) * (r ^ 2)) : ℝ))).fun_add (((((hasDerivAt_const x (2 : ℝ)).fun_mul (hasDerivAt_const x (L : ℝ))).fun_mul (hasDerivAt_const x ((a ^ 2) : ℝ))).fun_mul (hasDerivAt_const x ((r ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 2)))).fun_div ((((hasDerivAt_const x (3 : ℝ)).fun_mul (kds_P_dx a r x)).fun_mul (kds_Q_dx a L x)).fun_mul (kds_S_dx x)) (mul_ne_zero (mul_ne_zero (mul_ne_zero (by norm_num) hP) hQ) hS))
  exact h.congr_deriv (by simp only [Nat.cast_ofNat]; field_simp; simp only [kds_P, kds_Q, kds_S]; ring)

lemma kds_G233_dr (a M L r x : ℝ) (hP : kds_P a r x ≠ 0) (hX : kds_X a L ≠ 0) :
    HasDerivAt (fun t => (kds_G233 a M L t x)) (((-2:ℝ) * kds_Q a L x * x * (kds_S x ^ 2) * (a ^ 2) * ((3 * (r ^ 5)) + (18 * M * (r ^ 4)) + (L * (a ^ 2) * (r ^ 5)) + ((-3:ℝ) * M * (a ^ 4) * (x ^ 2)) + ((-3:ℝ) * M * (a ^ 4) * (x ^ 4)) + (3 * r * (a ^ 4) * (x ^ 4)) + (6 * (a ^ 2) * (r ^ 3) * (x ^ 2)) + (15 * M * (a ^ 2) * (r ^ 2)) + (L * r * (a ^ 6) * (x ^ 4)) + ((-3:ℝ) * M * (a ^ 2) * (r ^ 2) * (x ^ 2)) + (2 * L * (a ^ 4) * (r ^ 3) * (x ^ 2)))) / (3 * (kds_P a r x ^ 4) * (kds_X a L ^ 2))) r := by
  have h := (((((hasDerivAt_const r (kds_Q a L x : ℝ)).fun_mul (hasDerivAt_const r (kds_S x : ℝ))).fun_mul (hasDerivAt_const r (x : ℝ))).fun_mul (((((((((((((((((hasDerivAt_const r (3 : ℝ)).fun_mul ((hasDerivAt_id' r).fun_pow 6)).fun_add (((hasDerivAt_const r (3 : ℝ)).fun_mul (hasDerivAt_const r ((a ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' r).fun_pow 4))).fun_add (hasDerivAt_const r ((3 * (a ^ 6) * (x ^ 4)) : ℝ))).fun_add (((hasDerivAt_const r (L : ℝ)).fun_mul (hasDerivAt_const r ((a ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' r).fun_pow 6))).fun_add (((hasDerivAt_const r (L : ℝ)).fun_mul (hasDerivAt_const r ((a ^ 4) : ℝ))).fun_mul ((hasDerivAt_id' r).fun_pow 4))).fun_add (hasDerivAt_const r ((L * (a ^ 8) * (x ^ 4)) : ℝ))).fun_add ((((hasDerivAt_const r (3 : ℝ)).fun_mul (hasDerivAt_const r ((a ^ 4) : ℝ))).fun_mul ((hasDerivAt_id' r).fun_pow 2)).fun_mul (hasDerivAt_const r ((x ^ 4) : ℝ)))).fun_add ((((hasDerivAt_const r (6 : ℝ)).fun_mul (hasDerivAt_const r (M : ℝ))).fun_mul (hasDerivAt_id' r)).fun_mul (hasDerivAt_const r ((a ^ 4) : ℝ)))).fun_add ((((hasDerivAt_const r (6 : ℝ)).fun_mul (hasDerivAt_const r ((a ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' r).fun_pow 4)).fun_mul (hasDerivAt_const r ((x ^ 2) : ℝ)))).fun_add ((((hasDerivAt_const r (6 : ℝ)).fun_mul (hasDerivAt_const r ((a ^ 4) : ℝ))).fun_mul ((hasDerivAt_id' r).fun_pow 2)).fun_mul (hasDerivAt_const r ((x ^ 2) : ℝ)))).fun_add ((((hasDerivAt_const r (12 : ℝ)).fun_mul (hasDerivAt_const r (M : ℝ))).fun_mul (hasDerivAt_const r ((a ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' r).fun_pow 3))).fun_add ((((hasDerivAt_const r (L : ℝ)).fun_mul (hasDerivAt_const r ((a ^ 6) : ℝ))).fun_mul ((hasDerivAt_id' r).fun_pow 2)).fun_mul (hasDerivAt_const r ((x ^ 4) : ℝ)))).fun_add (((((hasDerivAt_const r ((-12:ℝ) : ℝ)).fun_mul (hasDerivAt_const r (M : ℝ))).fun_mul (hasDerivAt_const r ((a ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' r).fun_pow 3)).fun_mul (hasDerivAt_const r ((x ^ 2) : ℝ)))).fun_add (((((hasDerivAt_const r ((-6:ℝ) : ℝ)).fun_mul (hasDerivAt_const r (M : ℝ))).fun_mul (hasDerivAt_id' r)).fun_mul (hasDerivAt_const r ((a ^ 4) : ℝ))).fun_mul (hasDerivAt_const r ((x ^ 4) : ℝ)))).fun_add (((((hasDerivAt_const r (2 : ℝ)).fun_mul (hasDerivAt_const r (L : ℝ))).fun_mul (hasDerivAt_const r ((a ^ 4) : ℝ))).fun_mul ((hasDerivAt_id' r).fun_pow 4)).fun_mul (hasDerivAt_const r ((x ^ 2) : ℝ)))).fun_add (((((hasDerivAt_const r (2 : ℝ)).fun_mul (hasDerivAt_const r (L : ℝ))).fun_mul (hasDerivAt_const r ((a ^ 6) : ℝ))).fun_mul ((hasDerivAt_id' r).fun_pow 2)).fun_mul (hasDerivAt_const r ((x ^ 2) : ℝ))))).fun_div (((hasDerivAt_const r (3 : ℝ)).fun_mul ((kds_P_dr a r x).fun_pow 3)).fun_mul (hasDerivAt_const r ((kds_X a L ^ 2) : ℝ))) (mul_ne_zero (mul_ne_zero (by norm_num) (pow_ne_zero 3 hP)) (pow_ne_zero 2 hX)))
  exact h.congr_deriv (by simp only [Nat.cast_ofNat]; field_simp; simp only [kds_P, kds_Q, kds_S, kds_X]; ring)

set_option maxHeartbeats 1000000 in
lemma kds_G233_dx (a M L r x : ℝ) (hP : kds_P a r x ≠ 0) (hX : kds_X a L ≠ 0) :
    HasDerivAt (fun t => (kds_G233 a M L r t)) (((r ^ 8) + ((a ^ 2) * (r ^ 6)) + ((-1:ℝ) * (a ^ 8) * (x ^ 6)) + ((-1:ℝ) * (a ^ 8) * (x ^ 8)) + ((-3:ℝ) * (r ^ 8) * (x ^ 2)) + ((a ^ 4) * (r ^ 4) * (x ^ 2)) + ((-1:ℝ) * L * (a ^ 10) * (x ^ 10)) + ((-1:ℝ) * (a ^ 6) * (r ^ 2) * (x ^ 4)) + ((-1:ℝ) * (a ^ 6) * (r ^ 2) * (x ^ 8)) + ((-8:ℝ) * (a ^ 4) * (r ^ 4) * (x ^ 4)) + ((-7:ℝ) * (a ^ 2) * (r ^ 6) * (x ^ 4)) + ((-6:ℝ) * (a ^ 6) * (r ^ 2) * (x ^ 6)) + ((-5:ℝ) * (a ^ 4) * (r ^ 4) * (x ^ 6)) + ((-2:ℝ) * (a ^ 2) * (r ^ 6) * (x ^ 2)) + (2 * M * (a ^ 4) * (r ^ 3)) + (4 * M * (a ^ 2) * (r ^ 5)) + (((-1:ℝ) * L * (a ^ 10) * (x ^ 6)) / 3) + (((-1:ℝ) * (L ^ 2) * (a ^ 12) * (x ^ 10)) / 3) + ((L * (a ^ 2) * (r ^ 8)) / 3) + ((L * (a ^ 4) * (r ^ 6)) / 3) + (((L ^ 2) * (a ^ 12) * (x ^ 8)) / 9) + ((-1:ℝ) * L * (a ^ 8) * (r ^ 2) * (x ^ 10)) + ((-26:ℝ) * M * (a ^ 4) * (r ^ 3) * (x ^ 2)) + ((-24:ℝ) * M * (a ^ 2) * (r ^ 5) * (x ^ 2)) + ((-10:ℝ) * M * r * (a ^ 6) * (x ^ 2)) + (2 * M * r * (a ^ 6) * (x ^ 6)) + (2 * M * r * (a ^ 6) * (x ^ 8)) + (6 * M * r * (a ^ 6) * (x ^ 4)) + (10 * M * (a ^ 4) * (r ^ 3) * (x ^ 6)) + (14 * M * (a ^ 4) * (r ^ 3) * (x ^ 4)) + (20 * M * (a ^ 2) * (r ^ 5) * (x ^ 4)) + (((-13:ℝ) * L * (a ^ 4) * (r ^ 6) * (x ^ 6)) / 3) + (((-13:ℝ) * L * (a ^ 6) * (r ^ 4) * (x ^ 6)) / 3) + (((-13:ℝ) * (L ^ 2) * (a ^ 6) * (r ^ 6) * (x ^ 6)) / 9) + (((-11:ℝ) * L * (a ^ 6) * (r ^ 4) * (x ^ 8)) / 3) + (((-11:ℝ) * L * (a ^ 8) * (r ^ 2) * (x ^ 8)) / 3) + (((-11:ℝ) * (L ^ 2) * (a ^ 8) * (r ^ 4) * (x ^ 8)) / 9) + (((-10:ℝ) * (L ^ 2) * (a ^ 10) * (r ^ 2) * (x ^ 8)) / 9) + (((-8:ℝ) * (L ^ 2) * (a ^ 8) * (r ^ 4) * (x ^ 6)) / 9) + (((-5:ℝ) * L * (a ^ 2) * (r ^ 8) * (x ^ 4)) / 3) + (((-5:ℝ) * L * (a ^ 4) * (r ^ 6) * (x ^ 4)) / 3) + (((-5:ℝ) * (L ^ 2) * (a ^ 4) * (r ^ 8) * (x ^ 4)) / 9) + (((-1:ℝ) * L * (a ^ 6) * (r ^ 4) * (x ^ 4)) / 3) + (((-1:ℝ) * L * (a ^ 8) * (r ^ 2) * (x ^ 4)) / 3) + (((-1:ℝ) * L * (a ^ 8) * (r ^ 2) * (x ^ 6)) / 3) + (((-1:ℝ) * (L ^ 2) * (a ^ 10) * (r ^ 2) * (x ^ 10)) / 3) + ((L * (a ^ 4) * (r ^ 6) * (x ^ 2)) / 3) + ((L * (a ^ 6) * (r ^ 4) * (x ^ 2)) / 3) + (((L ^ 2) * (a ^ 4) * (r ^ 8) * (x ^ 2)) / 3) + (((L ^ 2) * (a ^ 6) * (r ^ 6) * (x ^ 2)) / 3) + ((2 * (L ^ 2) * (a ^ 6) * (r ^ 6) * (x ^ 4)) / 9) + ((5 * (L ^ 2) * (a ^ 10) * (r ^ 2) * (x ^ 6)) / 9) + ((7 * (L ^ 2) * (a ^ 8) * (r ^ 4) * (x ^ 4)) / 9) + ((-2:ℝ) * L * M * r * (a ^ 8) * (x ^ 4)) + ((-2:ℝ) * L * M * (a ^ 6) * (r ^ 3) * (x ^ 6)) + (2 * L * M * r * (a ^ 8) * (x ^ 10)) + (2 * L * M * (a ^ 6) * (r ^ 3) * (x ^ 2)) + (4 * L * M * (a ^ 4) * (r ^ 5) * (x ^ 2)) + (((-40:ℝ) * L * M * (a ^ 4) * (r ^ 5) * (x ^ 4)) / 3) + (((-22:ℝ) * L * M * (a ^ 6) * (r ^ 3) * (x ^ 4)) / 3) + (((-2:ℝ) * L * M * r * (a ^ 8) * (x ^ 8)) / 3) + ((2 * L * M * r * (a ^ 8) * (x ^ 6)) / 3) + ((22 * L * M * (a ^ 6) * (r ^ 3) * (x ^ 8)) / 3) + ((28 * L * M * (a ^ 4) * (r ^ 5) * (x ^ 6)) / 3)) / ((kds_P a r x ^ 4) * (kds_X a L ^ 2))) x := by
  have h := (((((kds_Q_dx a L x).fun_mul (kds_S_dx x)).fun_mul (hasDerivAt_id' x)).fun_mul ((((((((((((((((hasDerivAt_const x ((3 * (r ^ 6)) : ℝ)).fun_add (hasDerivAt_const x ((3 * (a ^ 2) * (r ^ 4)) : ℝ))).fun_add (((hasDerivAt_const x (3 : ℝ)).fun_mul (hasDerivAt_const x ((a ^ 6) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 4))).fun_add (hasDerivAt_const x ((L * (a ^ 2) * (r ^ 6)) : ℝ))).fun_add (hasDerivAt_const x ((L * (a ^ 4) * (r ^ 4)) : ℝ))).fun_add (((hasDerivAt_const x (L : ℝ)).fun_mul (hasDerivAt_const x ((a ^ 8) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 4))).fun_add ((((hasDerivAt_const x (3 : ℝ)).fun_mul (hasDerivAt_const x ((a ^ 4) : ℝ))).fun_mul (hasDerivAt_const x ((r ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 4))).fun_add (hasDerivAt_const x ((6 * M * r * (a ^ 4)) : ℝ))).fun_add ((((hasDerivAt_const x (6 : ℝ)).fun_mul (hasDerivAt_const x ((a ^ 2) : ℝ))).fun_mul (hasDerivAt_const x ((r ^ 4) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 2))).fun_add ((((hasDerivAt_const x (6 : ℝ)).fun_mul (hasDerivAt_const x ((a ^ 4) : ℝ))).fun_mul (hasDerivAt_const x ((r ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 2))).fun_add (hasDerivAt_const x ((12 * M * (a ^ 2) * (r ^ 3)) : ℝ))).fun_add ((((hasDerivAt_const x (L : ℝ)).fun_mul (hasDerivAt_const x ((a ^ 6) : ℝ))).fun_mul (hasDerivAt_const x ((r ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 4))).fun_add (((((hasDerivAt_const x ((-12:ℝ) : ℝ)).fun_mul (hasDerivAt_const x (M : ℝ))).fun_mul (hasDerivAt_const x ((a ^ 2) : ℝ))).fun_mul (hasDerivAt_const x ((r ^ 3) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 2))).fun_add (((((hasDerivAt_const x ((-6:ℝ) : ℝ)).fun_mul (hasDerivAt_const x (M : ℝ))).fun_mul (hasDerivAt_const x (r : ℝ))).fun_mul (hasDerivAt_const x ((a ^ 4) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 4))).fun_add (((((hasDerivAt_const x (2 : ℝ)).fun_mul (hasDerivAt_const x (L : ℝ))).fun_mul (hasDerivAt_const x ((a ^ 4) : ℝ))).fun_mul (hasDerivAt_const x ((r ^ 4) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 2))).fun_add (((((hasDerivAt_const x (2 : ℝ)).fun_mul (hasDerivAt_const x (L : ℝ))).fun_mul (hasDerivAt_const x ((a ^ 6) : ℝ))).fun_mul (hasDerivAt_const x ((r ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 2)))).fun_div (((hasDerivAt_const x (3 : ℝ)).fun_mul ((kds_P_dx a r x).fun_pow 3)).fun_mul (hasDerivAt_const x ((kds_X a L ^ 2) : ℝ))) (mul_ne_zero (mul_ne_zero (by norm_num) (pow_ne_zero 3 hP)) (pow_ne_zero 2 hX)))
  exact h.congr_deriv (by simp only [Nat.cast_ofNat]; field_simp; simp only [kds_P, kds_Q, kds_S, kds_X]; ring)

lemma kds_G301_dr (a M L r x : ℝ) (hP : kds_P a r x ≠ 0) (hD : kds_D a M L r ≠ 0) :
    HasDerivAt (fun t => (kds_G301 a M L t x)) (((-1:ℝ) * a * (((-54:ℝ) * (M ^ 2) * (r ^ 4)) + ((-3:ℝ) * L * (r ^ 8)) + (3 * (L ^ 2) * (r ^ 10)) + (36 * M * (r ^ 5)) + ((L ^ 2) * (a ^ 2) * (r ^ 8)) + ((-18:ℝ) * L * M * (r ^ 7)) + (3 * L * (a ^ 2) * (r ^ 6)) + (3 * L * (a ^ 8) * (x ^ 6)) + (18 * M * (a ^ 2) * (r ^ 3)) + (18 * (M ^ 2) * (a ^ 4) * (x ^ 4)) + ((L ^ 2) * (a ^ 8) * (r ^ 2) * (x ^ 6)) + ((-54:ℝ) * M * r * (a ^ 4) * (x ^ 2)) + ((-54:ℝ) * M * (a ^ 2) * (r ^ 3) * (x ^ 2)) + ((-18:ℝ) * M * r * (a ^ 4) * (x ^ 4)) + ((-12:ℝ) * L * M * (a ^ 2) * (r ^ 5)) + ((-9:ℝ) * L * (a ^ 2) * (r ^ 6) * (x ^ 2)) + ((-9:ℝ) * L * (a ^ 4) * (r ^ 4) * (x ^ 4)) + ((-3:ℝ) * L * (a ^ 6) * (r ^ 2) * (x ^ 6)) + (3 * (L ^ 2) * (a ^ 4) * (r ^ 6) * (x ^ 2)) + (3 * (L ^ 2) * (a ^ 6) * (r ^ 4) * (x ^ 4)) + (3 * (L ^ 2) * (a ^ 6) * (r ^ 4) * (x ^ 6)) + (9 * L * (a ^ 4) * (r ^ 4) * (x ^ 2)) + (9 * L * (a ^ 6) * (r ^ 2) * (x ^ 4)) + (9 * (L ^ 2) * (a ^ 2) * (r ^ 8) * (x ^ 2)) + (9 * (L ^ 2) * (a ^ 4) * (r ^ 6) * (x ^ 4)) + (108 * (M ^ 2) * (a ^ 2) * (r ^ 2) * (x ^ 2)) + (6 * L * M * r * (a ^ 6) * (x ^ 4)) + (12 * L * M * (a ^ 4) * (r ^ 3) * (x ^ 4)) + (18 * L * M * (a ^ 2) * (r ^ 5) * (x ^ 2)) + (18 * L * M * (a ^ 4) * (r ^ 3) * (x ^ 2)))) / (9 * (kds_D a M L r ^ 2) * (kds_P a r x ^ 3))) r := by
  have h := ((((hasDerivAt_const r ((-1:ℝ) : ℝ)).fun_mul (hasDerivAt_const r (a : ℝ))).fun_mul ((((((hasDerivAt_const r (L : ℝ)).fun_mul ((hasDerivAt_id' r).fun_pow 5)).fun_add (((hasDerivAt_const r ((-3:ℝ) : ℝ)).fun_mul (hasDerivAt_const r (M : ℝ))).fun_mul ((hasDerivAt_id' r).fun_pow 2))).fun_add (hasDerivAt_const r ((3 * M * (a ^ 2) * (x ^ 2)) : ℝ))).fun_add ((((hasDerivAt_const r (L : ℝ)).fun_mul (hasDerivAt_id' r)).fun_mul (hasDerivAt_const r ((a ^ 4) : ℝ))).fun_mul (hasDerivAt_const r ((x ^ 4) : ℝ)))).fun_add (((((hasDerivAt_const r (2 : ℝ)).fun_mul (hasDerivAt_const r (L : ℝ))).fun_mul (hasDerivAt_const r ((a ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' r).fun_pow 3)).fun_mul (hasDerivAt_const r ((x ^ 2) : ℝ))))).fun_div (((hasDerivAt_const r (3 : ℝ)).fun_mul (kds_D_dr a M L r)).fun_mul ((kds_P_dr a r x).fun_pow 2)) (mul_ne_zero (mul_ne_zero (by norm_num) hD) (pow_ne_zero 2 hP)))
  exact h.congr_deriv (by simp only [Nat.cast_ofNat]; field_simp; simp only [kds_P, kds_D]; ring)

lemma kds_G301_dx (a M L r x : ℝ) (hP : kds_P a r x ≠ 0) (hD : kds_D a M L r ≠ 0) :
    HasDerivAt (fun t => (kds_G301 a M L r t)) ((2 * M * x * (a ^ 3) * (((-3:ℝ) * (r ^ 2)) + ((a ^ 2) * (x ^ 2)))) / (kds_D a M L r * (kds_P a r x ^ 3))) x := by
  have h := ((((hasDerivAt_const x ((-1:ℝ) : ℝ)).fun_mul (hasDerivAt_const x (a : ℝ))).fun_mul (((((hasDerivAt_const x ((L * (r ^ 5)) : ℝ)).fun_add (hasDerivAt_const x (((-3:ℝ) * M * (r ^ 2)) : ℝ))).fun_add ((((hasDerivAt_const x (3 : ℝ)).fun_mul (hasDerivAt_const x (M : ℝ))).fun_mul (hasDerivAt_const x ((a ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 2))).fun_add ((((hasDerivAt_const x (L : ℝ)).fun_mul (hasDerivAt_const x (r : ℝ))).fun_mul (hasDerivAt_const x ((a ^ 4) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 4))).fun_add (((((hasDerivAt_const x (2 : ℝ)).fun_mul (hasDerivAt_const x (L : ℝ))).fun_mul (hasDerivAt_const x ((a ^ 2) : ℝ))).fun_mul (hasDerivAt_const x ((r ^ 3) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 2)))).fun_div (((hasDerivAt_const x (3 : ℝ)).fun_mul (hasDerivAt_const x (kds_D a M L r : ℝ))).fun_mul ((kds_P_dx a r x).fun_pow 2)) (mul_ne_zero (mul_ne_zero (by norm_num) hD) (pow_ne_zero 2 hP)))
  exact h.congr_deriv (by simp only [Nat.cast_ofNat]; field_simp; simp only [kds_P, kds_D]; ring)

lemma kds_G302_dr (a M L r x : ℝ) (hP : kds_P a r x ≠ 0) (hQ : kds_Q a L x ≠ 0) (hS : kds_S x ≠ 0) :
    HasDerivAt (fun t => (kds_G302 a M L t x)) ((2 * M * a * x * (((-3:ℝ) * (r ^ 2)) + ((a ^ 2) * (x ^ 2)))) / (kds_Q a L x * kds_S x * (kds_P a r x ^ 3))) r := by
  have h := ((((hasDerivAt_const r (a : ℝ)).fun_mul (hasDerivAt_const r (x : ℝ))).fun_mul (((((hasDerivAt_const r (L : ℝ)).fun_mul ((hasDerivAt_id' r).fun_pow 4)).fun_add (((hasDerivAt_const r (6 : ℝ)).fun_mul (hasDerivAt_const r (M : ℝ))).fun_mul (hasDerivAt_id' r))).fun_add (hasDerivAt_const r ((L * (a ^ 4) * (x ^ 4)) : ℝ))).fun_add (((((hasDerivAt_const r (2 : ℝ)).fun_mul (hasDerivAt_const r (L : ℝ))).fun_mul (hasDerivAt_const r ((a ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' r).fun_pow 2)).fun_mul (hasDerivAt_const r ((x ^ 2) : ℝ))))).fun_div ((((hasDerivAt_const r (3 : ℝ)).fun_mul (hasDerivAt_const r (kds_Q a L x : ℝ))).fun_mul (hasDerivAt_const r (kds_S x : ℝ))).fun_mul ((kds_P_dr a r x).fun_pow 2)) (mul_ne_zero (mul_ne_zero (mul_ne_zero (by norm_num) hQ) hS) (pow_ne_zero 2 hP)))
  exact h.congr_deriv (by simp only [Nat.cast_ofNat]; field_simp; simp only [kds_P, kds_Q, kds_S]; ring)

lemma kds_G302_dx (a M L r x : ℝ) (hP : kds_P a r x ≠ 0) (hQ : kds_Q a L x ≠ 0) (hS : kds_S x ≠ 0) :
    HasDerivAt (fun t => (kds_G302 a M L r t)) ((a * ((3 * L * (r ^ 6)) + (18 * M * (r ^ 3)) + ((-1:ℝ) * (L ^ 2) * (a ^ 8) * (x ^ 8)) + (3 * L * (a ^ 6) * (x ^ 6)) + (3 * L * (a ^ 6) * (x ^ 8)) + (3 * L * (r ^ 6) * (x ^ 2)) + (3 * (L ^ 2) * (a ^ 8) * (x ^ 10)) + (18 * M * (r ^ 3) * (x ^ 2)) + ((-1:ℝ) * (L ^ 2) * (a ^ 2) * (r ^ 6) * (x ^ 2)) + ((-54:ℝ) * M * r * (a ^ 2) * (x ^ 2)) + ((-3:ℝ) * (L ^ 2) * (a ^ 4) * (r ^ 4) * (x ^ 4)) + ((-3:ℝ) * (L ^ 2) * (a ^ 6) * (r ^ 2) * (x ^ 6)) + (3 * (L ^ 2) * (a ^ 2) * (r ^ 6) * (x ^ 4)) + (9 * L * (a ^ 2) * (r ^ 4) * (x ^ 2)) + (9 * L * (a ^ 2) * (r ^ 4) * (x ^ 4)) + (9 * L * (a ^ 4) * (r ^ 2) * (x ^ 4)) + (9 * L * (a ^ 4) * (r ^ 2) * (x ^ 6)) + (9 * (L ^ 2) * (a ^ 4) * (r ^ 4) * (x ^ 6)) + (9 * (L ^ 2) * (a ^ 6) * (r ^ 2) * (x ^ 8)) + (90 * M * r * (a ^ 2) * (x ^ 4)) + ((-30:ℝ) * L * M * r * (a ^ 4) * (x ^ 4)) + ((-6:ℝ) * L * M * (a ^ 2) * (r ^ 3) * (x ^ 2)) + (18 * L * M * (a ^ 2) * (r ^ 3) * (x ^ 4)) + (42 * L * M * r * (a ^ 4) * (x ^ 6)))) / (9 * (kds_P a r x ^ 3) * (kds_Q a L x ^ 2) * (kds_S x ^ 2))) x := by
  have h := ((((hasDerivAt_const x (a : ℝ)).fun_mul (hasDerivAt_id' x)).fun_mul ((((hasDerivAt_const x ((L * (r ^ 4)) : ℝ)).fun_add (hasDerivAt_const x ((6 * M * r) : ℝ))).fun_add (((hasDerivAt_const x (L : ℝ)).fun_mul (hasDerivAt_const x ((a ^ 4) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 4))).fun_add (((((hasDerivAt_const x (2 : ℝ)).fun_mul (hasDerivAt_const x (L : ℝ))).fun_mul (hasDerivAt_const x ((a ^ 2) : ℝ))).fun_mul (hasDerivAt_const x ((r ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 2)))).fun_div ((((hasDerivAt_const x (3 : ℝ)).fun_mul (kds_Q_dx a L x)).fun_mul (kds_S_dx x)).fun_mul ((kds_P_dx a r x).fun_pow 2)) (mul_ne_zero (mul_ne_zero (mul_ne_zero (by norm_num) hQ) hS) (pow_ne_zero 2 hP)))
  exact h.congr_deriv (by simp only [Nat.cast_ofNat]; field_simp; simp only [kds_P, kds_Q, kds_S]; ring)

lemma kds_G313_dr (a M L r x : ℝ) (hP : kds_P a r x ≠ 0) (hD : kds_D a M L r ≠ 0) :
    HasDerivAt (fun t => (kds_G313 a M L t x)) ((((-1:ℝ) * (r ^ 8)) + ((a ^ 2) * (r ^ 6)) + ((a ^ 8) * (x ^ 6)) + ((-4:ℝ) * (M ^ 2) * (r ^ 6)) + (4 * M * (r ^ 7)) + (((-1:ℝ) * (L ^ 2) * (r ^ 12)) / 9) + ((2 * L * (r ^ 10)) / 3) + ((-1:ℝ) * (a ^ 6) * (r ^ 2) * (x ^ 6)) + ((-6:ℝ) * (M ^ 2) * (a ^ 2) * (r ^ 4)) + ((-3:ℝ) * (a ^ 2) * (r ^ 6) * (x ^ 2)) + ((-3:ℝ) * (a ^ 4) * (r ^ 4) * (x ^ 4)) + ((-2:ℝ) * (M ^ 2) * (a ^ 6) * (x ^ 6)) + (2 * M * (a ^ 4) * (r ^ 3)) + (2 * (M ^ 2) * (a ^ 6) * (x ^ 4)) + (3 * (a ^ 4) * (r ^ 4) * (x ^ 2)) + (3 * (a ^ 6) * (r ^ 2) * (x ^ 4)) + (4 * M * (a ^ 2) * (r ^ 5)) + (((-4:ℝ) * L * M * (r ^ 9)) / 3) + (((-2:ℝ) * L * (a ^ 2) * (r ^ 8)) / 3) + (((L ^ 2) * (a ^ 2) * (r ^ 10)) / 9) + ((-12:ℝ) * M * (a ^ 4) * (r ^ 3) * (x ^ 2)) + ((-8:ℝ) * (M ^ 2) * (a ^ 4) * (r ^ 2) * (x ^ 4)) + ((-6:ℝ) * M * r * (a ^ 6) * (x ^ 2)) + ((-2:ℝ) * L * (a ^ 4) * (r ^ 6) * (x ^ 2)) + ((-2:ℝ) * L * (a ^ 6) * (r ^ 4) * (x ^ 4)) + (2 * L * (a ^ 2) * (r ^ 8) * (x ^ 2)) + (2 * L * (a ^ 4) * (r ^ 6) * (x ^ 4)) + (2 * M * r * (a ^ 6) * (x ^ 6)) + (6 * M * (a ^ 4) * (r ^ 3) * (x ^ 4)) + (6 * (M ^ 2) * (a ^ 2) * (r ^ 4) * (x ^ 2)) + (12 * (M ^ 2) * (a ^ 4) * (r ^ 2) * (x ^ 2)) + (((-10:ℝ) * L * M * (a ^ 2) * (r ^ 7)) / 3) + (((-4:ℝ) * L * M * (a ^ 4) * (r ^ 5)) / 3) + (((-2:ℝ) * L * (a ^ 8) * (r ^ 2) * (x ^ 6)) / 3) + (((-1:ℝ) * (L ^ 2) * (a ^ 2) * (r ^ 10) * (x ^ 2)) / 3) + (((-1:ℝ) * (L ^ 2) * (a ^ 4) * (r ^ 8) * (x ^ 4)) / 3) + (((-1:ℝ) * (L ^ 2) * (a ^ 6) * (r ^ 6) * (x ^ 6)) / 9) + (((L ^ 2) * (a ^ 4) * (r ^ 8) * (x ^ 2)) / 3) + (((L ^ 2) * (a ^ 6) * (r ^ 6) * (x ^ 4)) / 3) + (((L ^ 2) * (a ^ 8) * (r ^ 4) * (x ^ 6)) / 9) + ((2 * L * (a ^ 6) * (r ^ 4) * (x ^ 6)) / 3) + (2 * L * M * (a ^ 2) * (r ^ 7) * (x ^ 2)) + (2 * L * M * (a ^ 4) * (r ^ 5) * (x ^ 2)) + (2 * L * M * (a ^ 6) * (r ^ 3) * (x ^ 2)) + (((-2:ℝ) * L * M * r * (a ^ 8) * (x ^ 6)) / 3) + (((-2:ℝ) * L * M * (a ^ 6) * (r ^ 3) * (x ^ 4)) / 3) + ((2 * L * M * r * (a ^ 8) * (x ^ 4)) / 3) + ((2 * L * M * (a ^ 4) * (r ^ 5) * (x ^ 4)) / 3)) / ((kds_D a M L r ^ 2) * (kds_P a r x ^ 3))) r := by
  have h := (((((((((((((hasDerivAt_id' r).fun_pow 5).fun_add (((hasDerivAt_const r ((-2:ℝ) : ℝ)).fun_mul (hasDerivAt_const r (M : ℝ))).fun_mul ((hasDerivAt_id' r).fun_pow 4))).fun_add ((((hasDerivAt_const r ((-1:ℝ) : ℝ)).fun_mul (hasDerivAt_const r (L : ℝ))).fun_mul ((hasDerivAt_id' r).fun_pow 7)).fun_div (hasDerivAt_const r (3 : ℝ)) (by norm_num))).fun_add (hasDerivAt_const r ((M * (a ^ 4) * (x ^ 2)) : ℝ))).fun_add (((hasDerivAt_id' r).fun_mul (hasDerivAt_const r ((a ^ 4) : ℝ))).fun_mul (hasDerivAt_const r ((x ^ 4) : ℝ)))).fun_add ((((hasDerivAt_const r ((-1:ℝ) : ℝ)).fun_mul (hasDerivAt_const r (M : ℝ))).fun_mul (hasDerivAt_const r ((a ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' r).fun_pow 2))).fun_add (hasDerivAt_const r (((-1:ℝ) * M * (a ^ 4) * (x ^ 4)) : ℝ))).fun_add ((((hasDerivAt_const r (2 : ℝ)).fun_mul (hasDerivAt_const r ((a ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' r).fun_pow 3)).fun_mul (hasDerivAt_const r ((x ^ 2) : ℝ)))).fun_add (((((hasDerivAt_const r ((-1:ℝ) : ℝ)).fun_mul (hasDerivAt_const r (M : ℝ))).fun_mul (hasDerivAt_const r ((a ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' r).fun_pow 2)).fun_mul (hasDerivAt_const r ((x ^ 2) : ℝ)))).fun_add ((((((hasDerivAt_const r ((-2:ℝ) : ℝ)).fun_mul (hasDerivAt_const r (L : ℝ))).fun_mul (hasDerivAt_const r ((a ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' r).fun_pow 5)).fun_mul (hasDerivAt_const r ((x ^ 2) : ℝ))).fun_div (hasDerivAt_const r (3 : ℝ)) (by norm_num))).fun_add ((((((hasDerivAt_const r ((-1:ℝ) : ℝ)).fun_mul (hasDerivAt_const r (L : ℝ))).fun_mul (hasDerivAt_const r ((a ^ 4) : ℝ))).fun_mul ((hasDerivAt_id' r).fun_pow 3)).fun_mul (hasDerivAt_const r ((x ^ 4) : ℝ))).fun_div (hasDerivAt_const r (3 : ℝ)) (by norm_num))).fun_div ((kds_D_dr a M L r).fun_mul ((kds_P_dr a r x).fun_pow 2)) (mul_ne_zero hD (pow_ne_zero 2 hP)))
  exact h.congr_deriv (by simp only [Nat.cast_ofNat]; field_simp; simp only [kds_P, kds_D]; ring)

lemma kds_G313_dx (a M L r x : ℝ) (hP : kds_P a r x ≠ 0) (hD : kds_D a M L r ≠ 0) :
    HasDerivAt (fun t => (kds_G313 a M L r t)) ((M * x * (a ^ 2) * (((-3:ℝ) * (r ^ 2)) + ((a ^ 2) * (x ^ 2))) * (((-2:ℝ) * (a ^ 2)) + ((-2:ℝ) * (r ^ 2)))) / (kds_D a M L r * (kds_P a r x ^ 3))) x := by
  have h := ((((((((((((hasDerivAt_const x ((r ^ 5) : ℝ)).fun_add (hasDerivAt_const x (((-2:ℝ) * M * (r ^ 4)) : ℝ))).fun_add (hasDerivAt_const x ((((-1:ℝ) * L * (r ^ 7)) / 3) : ℝ))).fun_add (((hasDerivAt_const x (M : ℝ)).fun_mul (hasDerivAt_const x ((a ^ 4) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 2))).fun_add (((hasDerivAt_const x (r : ℝ)).fun_mul (hasDerivAt_const x ((a ^ 4) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 4))).fun_add (hasDerivAt_const x (((-1:ℝ) * M * (a ^ 2) * (r ^ 2)) : ℝ))).fun_add ((((hasDerivAt_const x ((-1:ℝ) : ℝ)).fun_mul (hasDerivAt_const x (M : ℝ))).fun_mul (hasDerivAt_const x ((a ^ 4) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 4))).fun_add ((((hasDerivAt_const x (2 : ℝ)).fun_mul (hasDerivAt_const x ((a ^ 2) : ℝ))).fun_mul (hasDerivAt_const x ((r ^ 3) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 2))).fun_add (((((hasDerivAt_const x ((-1:ℝ) : ℝ)).fun_mul (hasDerivAt_const x (M : ℝ))).fun_mul (hasDerivAt_const x ((a ^ 2) : ℝ))).fun_mul (hasDerivAt_const x ((r ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 2))).fun_add ((((((hasDerivAt_const x ((-2:ℝ) : ℝ)).fun_mul (hasDerivAt_const x (L : ℝ))).fun_mul (hasDerivAt_const x ((a ^ 2) : ℝ))).fun_mul (hasDerivAt_const x ((r ^ 5) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 2)).fun_div (hasDerivAt_const x (3 : ℝ)) (by norm_num))).fun_add ((((((hasDerivAt_const x ((-1:ℝ) : ℝ)).fun_mul (hasDerivAt_const x (L : ℝ))).fun_mul (hasDerivAt_const x ((a ^ 4) : ℝ))).fun_mul (hasDerivAt_const x ((r ^ 3) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 4)).fun_div (hasDerivAt_const x (3 : ℝ)) (by norm_num))).fun_div ((hasDerivAt_const x (kds_D a M L r : ℝ)).fun_mul ((kds_P_dx a r x).fun_pow 2)) (mul_ne_zero hD (pow_ne_zero 2 hP)))
  exact h.congr_deriv (by simp only [Nat.cast_ofNat]; field_simp; simp only [kds_P, kds_D]; ring)

lemma kds_G323_dr (a M L r x : ℝ) (hP : kds_P a r x ≠ 0) (hQ : kds_Q a L x ≠ 0) (hS : kds_S x ≠ 0) :
    HasDerivAt (fun t => (kds_G323 a M L t x)) (((-2:ℝ) * M * x * (a ^ 2) * (((-3:ℝ) * (r ^ 2)) + ((a ^ 2) * (x ^ 2)))) / (kds_Q a L x * (kds_P a r x ^ 3))) r := by
  have h := ((((hasDerivAt_const r ((-1:ℝ) : ℝ)).fun_mul (hasDerivAt_const r (x : ℝ))).fun_mul (((((((((hasDerivAt_const r (3 : ℝ)).fun_mul ((hasDerivAt_id' r).fun_pow 4)).fun_add (hasDerivAt_const r ((3 * (a ^ 4) * (x ^ 4)) : ℝ))).fun_add (hasDerivAt_const r ((L * (a ^ 6) * (x ^ 6)) : ℝ))).fun_add ((((hasDerivAt_const r (6 : ℝ)).fun_mul (hasDerivAt_const r (M : ℝ))).fun_mul (hasDerivAt_id' r)).fun_mul (hasDerivAt_const r ((a ^ 2) : ℝ)))).fun_add ((((hasDerivAt_const r (6 : ℝ)).fun_mul (hasDerivAt_const r ((a ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' r).fun_pow 2)).fun_mul (hasDerivAt_const r ((x ^ 2) : ℝ)))).fun_add ((((hasDerivAt_const r (L : ℝ)).fun_mul (hasDerivAt_const r ((a ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' r).fun_pow 4)).fun_mul (hasDerivAt_const r ((x ^ 2) : ℝ)))).fun_add (((((hasDerivAt_const r ((-6:ℝ) : ℝ)).fun_mul (hasDerivAt_const r (M : ℝ))).fun_mul (hasDerivAt_id' r)).fun_mul (hasDerivAt_const r ((a ^ 2) : ℝ))).fun_mul (hasDerivAt_const r ((x ^ 2) : ℝ)))).fun_add (((((hasDerivAt_const r (2 : ℝ)).fun_mul (hasDerivAt_const r (L : ℝ))).fun_mul (hasDerivAt_const r ((a ^ 4) : ℝ))).fun_mul ((hasDerivAt_id' r).fun_pow 2)).fun_mul (hasDerivAt_const r ((x ^ 4) : ℝ))))).fun_div ((((hasDerivAt_const r (3 : ℝ)).fun_mul (hasDerivAt_const r (kds_Q a L x : ℝ))).fun_mul (hasDerivAt_const r (kds_S x : ℝ))).fun_mul ((kds_P_dr a r x).fun_pow 2)) (mul_ne_zero (mul_ne_zero (mul_ne_zero (by norm_num) hQ) hS) (pow_ne_zero 2 hP)))
  exact h.congr_deriv (by simp only [Nat.cast_ofNat]; field_simp; simp only [kds_P, kds_Q, kds_S]; ring)

lemma kds_G323_dx (a M L r x : ℝ) (hP : kds_P a r x ≠ 0) (hQ : kds_Q a L x ≠ 0) (hS : kds_S x ≠ 0) :
    HasDerivAt (fun t => (kds_G323 a M L r t)) ((((-1:ℝ) * (r ^ 6)) + ((-1:ℝ) * (a ^ 6) * (x ^ 6)) + ((-1:ℝ) * (a ^ 6) * (x ^ 8)) + ((-1:ℝ) * (r ^ 6) * (x ^ 2)) + ((-3:ℝ) * (a ^ 2) * (r ^ 4) * (x ^ 2)) + ((-3:ℝ) * (a ^ 2) * (r ^ 4) * (x ^ 4)) + ((-3:ℝ) * (a ^ 4) * (r ^ 2) * (x ^ 4)) + ((-3:ℝ) * (a ^ 4) * (r ^ 2) * (x ^ 6)) + ((-2:ℝ) * M * (a ^ 2) * (r ^ 3)) + (((-2:ℝ) * L * (a ^ 8) * (x ^ 8)) / 3) + (((-2:ℝ) * L * (a ^ 8) * (x ^ 10)) / 3) + (((-1:ℝ) * (L ^ 2) * (a ^ 10) * (x ^ 10)) / 9) + (((-1:ℝ) * (L ^ 2) * (a ^ 10) * (x ^ 12)) / 9) + ((-12:ℝ) * M * r * (a ^ 4) * (x ^ 4)) + ((-2:ℝ) * L * (a ^ 4) * (r ^ 4) * (x ^ 4)) + ((-2:ℝ) * L * (a ^ 4) * (r ^ 4) * (x ^ 6)) + ((-2:ℝ) * L * (a ^ 6) * (r ^ 2) * (x ^ 6)) + ((-2:ℝ) * L * (a ^ 6) * (r ^ 2) * (x ^ 8)) + ((-2:ℝ) * M * (a ^ 2) * (r ^ 3) * (x ^ 4)) + (4 * M * (a ^ 2) * (r ^ 3) * (x ^ 2)) + (6 * M * r * (a ^ 4) * (x ^ 2)) + (6 * M * r * (a ^ 4) * (x ^ 6)) + (((-2:ℝ) * L * (a ^ 2) * (r ^ 6) * (x ^ 2)) / 3) + (((-2:ℝ) * L * (a ^ 2) * (r ^ 6) * (x ^ 4)) / 3) + (((-1:ℝ) * (L ^ 2) * (a ^ 6) * (r ^ 4) * (x ^ 6)) / 3) + (((-1:ℝ) * (L ^ 2) * (a ^ 6) * (r ^ 4) * (x ^ 8)) / 3) + (((-1:ℝ) * (L ^ 2) * (a ^ 8) * (r ^ 2) * (x ^ 8)) / 3) + (((-1:ℝ) * (L ^ 2) * (a ^ 8) * (r ^ 2) * (x ^ 10)) / 3) + (((-1:ℝ) * (L ^ 2) * (a ^ 4) * (r ^ 6) * (x ^ 4)) / 9) + (((-1:ℝ) * (L ^ 2) * (a ^ 4) * (r ^ 6) * (x ^ 6)) / 9) + (((-20:ℝ) * L * M * r * (a ^ 6) * (x ^ 6)) / 3) + (((-4:ℝ) * L * M * (a ^ 4) * (r ^ 3) * (x ^ 4)) / 3) + ((2 * L * M * (a ^ 4) * (r ^ 3) * (x ^ 2)) / 3) + ((2 * L * M * (a ^ 4) * (r ^ 3) * (x ^ 6)) / 3) + ((10 * L * M * r * (a ^ 6) * (x ^ 4)) / 3) + ((10 * L * M * r * (a ^ 6) * (x ^ 8)) / 3)) / ((kds_P a r x ^ 3) * (kds_Q a L x ^ 2) * (kds_S x ^ 2))) x := by
  have h := ((((hasDerivAt_const x ((-1:ℝ) : ℝ)).fun_mul (hasDerivAt_id' x)).fun_mul ((((((((hasDerivAt_const x ((3 * (r ^ 4)) : ℝ)).fun_add (((hasDerivAt_const x (3 : ℝ)).fun_mul (hasDerivAt_const x ((a ^ 4) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 4))).fun_add (((hasDerivAt_const x (L : ℝ)).fun_mul (hasDerivAt_const x ((a ^ 6) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 6))).fun_add (hasDerivAt_const x ((6 * M * r * (a ^ 2)) : ℝ))).fun_add ((((hasDerivAt_const x (6 : ℝ)).fun_mul (hasDerivAt_const x ((a ^ 2) : ℝ))).fun_mul (hasDerivAt_const x ((r ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 2))).fun_add ((((hasDerivAt_const x (L : ℝ)).fun_mul (hasDerivAt_const x ((a ^ 2) : ℝ))).fun_mul (hasDerivAt_const x ((r ^ 4) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 2))).fun_add (((((hasDerivAt_const x ((-6:ℝ) : ℝ)).fun_mul (hasDerivAt_const x (M : ℝ))).fun_mul (hasDerivAt_const x (r : ℝ))).fun_mul (hasDerivAt_const x ((a ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 2))).fun_add (((((hasDerivAt_const x (2 : ℝ)).fun_mul (hasDerivAt_const x (L : ℝ))).fun_mul (hasDerivAt_const x ((a ^ 4) : ℝ))).fun_mul (hasDerivAt_const x ((r ^ 2) : ℝ))).fun_mul ((hasDerivAt_id' x).fun_pow 4)))).fun_div ((((hasDerivAt_const x (3 : ℝ)).fun_mul (kds_Q_dx a L x)).fun_mul (kds_S_dx x)).fun_mul ((kds_P_dx a r x).fun_pow 2)) (mul_ne_zero (mul_ne_zero (mul_ne_zero (by norm_num) hQ) hS) (pow_ne_zero 2 hP)))
  exact h.congr_deriv (by simp only [Nat.cast_ofNat]; field_simp; simp only [kds_P, kds_Q, kds_S]; ring)

/-- **Kerr–de Sitter** in Boyer–Lindquist form with `x = cos θ`, on `(t, r, x, φ)`:
`g = −(Δ_r/ρ²Ξ²)(dt − a(1−x²)dφ)² + (Δ_x(1−x²)/ρ²Ξ²)(a dt − (r²+a²)dφ)² + (ρ²/Δ_r)dr² + ρ²/(Δ_x(1−x²)) dx²`. -/
noncomputable def rn_kds (a M L : ℝ) (y : Fin 4 → ℝ) : Matrix (Fin 4) (Fin 4) ℝ :=
  !![(kds_g00 a M L (y 1) (y 2)), 0, 0, (kds_g03 a M L (y 1) (y 2));
    0, (kds_g11 a M L (y 1) (y 2)), 0, 0;
    0, 0, (kds_g22 a L (y 1) (y 2)), 0;
    (kds_g03 a M L (y 1) (y 2)), 0, 0, (kds_g33 a M L (y 1) (y 2))]

lemma kds_inv {a M L : ℝ} {y : Fin 4 → ℝ} (hP : kds_P a (y 1) (y 2) ≠ 0) (hD : kds_D a M L (y 1) ≠ 0) (hQ : kds_Q a L (y 2) ≠ 0)
    (hS : kds_S (y 2) ≠ 0) (hX : kds_X a L ≠ 0) :
    (rn_kds a M L y)⁻¹ = !![(kds_i00 a M L (y 1) (y 2)), 0, 0, (kds_i03 a M L (y 1) (y 2));
      0, (kds_i11 a M L (y 1) (y 2)), 0, 0;
      0, 0, (kds_i22 a L (y 1) (y 2)), 0;
      (kds_i03 a M L (y 1) (y 2)), 0, 0, (kds_i33 a M L (y 1) (y 2))] := by
  refine Matrix.inv_eq_left_inv ?_
  ext i j
  fin_cases i <;> fin_cases j <;> simp [rn_kds, Matrix.mul_apply, Fin.sum_univ_four]
  all_goals simp only [kds_i00, kds_i03, kds_i33, kds_i11, kds_i22, kds_g00, kds_g03, kds_g33, kds_g11, kds_g22]
  all_goals field_simp
  all_goals simp only [kds_P, kds_D, kds_Q, kds_S]
  all_goals ring

/-- The Christoffel table of `rn_kds`: twenty independent non-zero entries. -/
noncomputable def kds_T (a M L : ℝ) (y : Fin 4 → ℝ) : Fin 4 → Fin 4 → Fin 4 → ℝ :=
  ![![![0, (kds_G001 a M L (y 1) (y 2)), (kds_G002 a M L (y 1) (y 2)), 0], ![(kds_G001 a M L (y 1) (y 2)), 0, 0, (kds_G013 a M L (y 1) (y 2))], ![(kds_G002 a M L (y 1) (y 2)), 0, 0, (kds_G023 a M L (y 1) (y 2))], ![0, (kds_G013 a M L (y 1) (y 2)), (kds_G023 a M L (y 1) (y 2)), 0]],
    ![![(kds_G100 a M L (y 1) (y 2)), 0, 0, (kds_G103 a M L (y 1) (y 2))], ![0, (kds_G111 a M L (y 1) (y 2)), (kds_G112 a (y 1) (y 2)), 0], ![0, (kds_G112 a (y 1) (y 2)), (kds_G122 a M L (y 1) (y 2)), 0], ![(kds_G103 a M L (y 1) (y 2)), 0, 0, (kds_G133 a M L (y 1) (y 2))]],
    ![![(kds_G200 a M L (y 1) (y 2)), 0, 0, (kds_G203 a M L (y 1) (y 2))], ![0, (kds_G211 a M L (y 1) (y 2)), (kds_G212 a (y 1) (y 2)), 0], ![0, (kds_G212 a (y 1) (y 2)), (kds_G222 a L (y 1) (y 2)), 0], ![(kds_G203 a M L (y 1) (y 2)), 0, 0, (kds_G233 a M L (y 1) (y 2))]],
    ![![0, (kds_G301 a M L (y 1) (y 2)), (kds_G302 a M L (y 1) (y 2)), 0], ![(kds_G301 a M L (y 1) (y 2)), 0, 0, (kds_G313 a M L (y 1) (y 2))], ![(kds_G302 a M L (y 1) (y 2)), 0, 0, (kds_G323 a M L (y 1) (y 2))], ![0, (kds_G313 a M L (y 1) (y 2)), (kds_G323 a M L (y 1) (y 2)), 0]]]

set_option maxHeartbeats 0 in
set_option linter.unusedSimpArgs false in
lemma kds_Γ {a M L : ℝ} {y : Fin 4 → ℝ} (hP : kds_P a (y 1) (y 2) ≠ 0) (hD : kds_D a M L (y 1) ≠ 0) (hQ : kds_Q a L (y 2) ≠ 0)
    (hS : kds_S (y 2) ≠ 0) (hX : kds_X a L ≠ 0) (A B C : Fin 4) :
    kr_Γ (rn_kds a M L) y A B C = kds_T a M L y A B C := by
  have e0 := (kds_g00_dr a M L (y 1) (y 2) hP hX).deriv
  have e1 := (kds_g00_dx a M L (y 1) (y 2) hP hX).deriv
  have e2 := (kds_g03_dr a M L (y 1) (y 2) hP hX).deriv
  have e3 := (kds_g03_dx a M L (y 1) (y 2) hP hX).deriv
  have e4 := (kds_g33_dr a M L (y 1) (y 2) hP hX).deriv
  have e5 := (kds_g33_dx a M L (y 1) (y 2) hP hX).deriv
  have e6 := (kds_g11_dr a M L (y 1) (y 2) hD).deriv
  have e7 := (kds_g11_dx a M L (y 1) (y 2) hD).deriv
  have e8 := (kds_g22_dr a L (y 1) (y 2) hQ hS).deriv
  have e9 := (kds_g22_dx a L (y 1) (y 2) hQ hS).deriv
  simp only [kr_Γ, kds_inv hP hD hQ hS hX]
  fin_cases A <;> fin_cases B <;> fin_cases C <;>
    simp [kr_pd, rn_kds, kds_T, Function.update_apply, Fin.sum_univ_four, e0, e1, e2, e3, e4, e5, e6, e7, e8, e9]
  all_goals (try simp only [kds_i00, kds_i03, kds_i33, kds_i11, kds_i22, kds_g00, kds_g03, kds_g33, kds_g11, kds_g22, kds_G001, kds_G002, kds_G013, kds_G023, kds_G100, kds_G103, kds_G111, kds_G112, kds_G122, kds_G133, kds_G200, kds_G203, kds_G211, kds_G212, kds_G222, kds_G233, kds_G301, kds_G302, kds_G313, kds_G323])
  all_goals field_simp
  all_goals simp only [kds_P, kds_D, kds_Q, kds_S, kds_X]
  all_goals ring

/-- The data at a point: `ρ², Δ_r, Δ_x, 1 − x², Ξ ≠ 0`. -/
structure kds_Hyp (a M L : ℝ) (x : Fin 4 → ℝ) : Prop where
  hP : kds_P a (x 1) (x 2) ≠ 0
  hD : kds_D a M L (x 1) ≠ 0
  hQ : kds_Q a L (x 2) ≠ 0
  hS : kds_S (x 2) ≠ 0
  hX : kds_X a L ≠ 0

lemma kds_Hyp.U {a M L : ℝ} {x : Fin 4 → ℝ} (h : kds_Hyp a M L x) : ∀ᶠ y in 𝓝 x, kds_Hyp a M L y := by
  have cP : Continuous fun y : Fin 4 → ℝ => kds_P a (y 1) (y 2) := by unfold kds_P; fun_prop
  have cD : Continuous fun y : Fin 4 → ℝ => kds_D a M L (y 1) := by unfold kds_D; fun_prop
  have cQ : Continuous fun y : Fin 4 → ℝ => kds_Q a L (y 2) := by unfold kds_Q; fun_prop
  have cS : Continuous fun y : Fin 4 → ℝ => kds_S (y 2) := by unfold kds_S; fun_prop
  filter_upwards [cP.continuousAt.eventually_ne h.hP, cD.continuousAt.eventually_ne h.hD,
    cQ.continuousAt.eventually_ne h.hQ, cS.continuousAt.eventually_ne h.hS] with y h1 h2 h3 h4
  exact ⟨h1, h2, h3, h4, h.hX⟩

lemma kds_pd {a M L : ℝ} {x : Fin 4 → ℝ} (h : kds_Hyp a M L x) (A B C d : Fin 4) :
    kr_pd (fun y => kr_Γ (rn_kds a M L) y A B C) x d = kr_pd (fun y => kds_T a M L y A B C) x d :=
  kr_pd_congr (h.U.mono fun _ hy => kds_Γ hy.hP hy.hD hy.hQ hy.hS hy.hX A B C)

set_option maxHeartbeats 0 in
set_option linter.unusedSimpArgs false in
/-- **Row 4a.** Kerr–de Sitter is vacuum-`Λ`: `R_μν = Λ g_μν`, all sixteen components. -/
theorem kds_vacuum {a M L : ℝ} {x : Fin 4 → ℝ} (h : kds_Hyp a M L x) (μ ν : Fin 4) :
    rn_Ric (rn_kds a M L) x μ ν = L * rn_kds a M L x μ ν := by
  have hP := h.hP; have hD := h.hD; have hQ := h.hQ; have hS := h.hS; have hX := h.hX
  have hΓ := kds_Γ hP hD hQ hS hX
  have f0 := (kds_G001_dr a M L (x 1) (x 2) hP hD).deriv
  have f1 := (kds_G001_dx a M L (x 1) (x 2) hP hD).deriv
  have f2 := (kds_G002_dr a M L (x 1) (x 2) hP hQ).deriv
  have f3 := (kds_G002_dx a M L (x 1) (x 2) hP hQ).deriv
  have f4 := (kds_G013_dr a M L (x 1) (x 2) hP hD).deriv
  have f5 := (kds_G013_dx a M L (x 1) (x 2) hP hD).deriv
  have f6 := (kds_G023_dr a M L (x 1) (x 2) hP hQ).deriv
  have f7 := (kds_G023_dx a M L (x 1) (x 2) hP hQ).deriv
  have f8 := (kds_G100_dr a M L (x 1) (x 2) hP hX).deriv
  have f9 := (kds_G100_dx a M L (x 1) (x 2) hP hX).deriv
  have f10 := (kds_G103_dr a M L (x 1) (x 2) hP hX).deriv
  have f11 := (kds_G103_dx a M L (x 1) (x 2) hP hX).deriv
  have f12 := (kds_G111_dr a M L (x 1) (x 2) hP hD).deriv
  have f13 := (kds_G111_dx a M L (x 1) (x 2) hP hD).deriv
  have f14 := (kds_G112_dr a (x 1) (x 2) hP).deriv
  have f15 := (kds_G112_dx a (x 1) (x 2) hP).deriv
  have f16 := (kds_G122_dr a M L (x 1) (x 2) hP hQ hS).deriv
  have f17 := (kds_G122_dx a M L (x 1) (x 2) hP hQ hS).deriv
  have f18 := (kds_G133_dr a M L (x 1) (x 2) hP hX).deriv
  have f19 := (kds_G133_dx a M L (x 1) (x 2) hP hX).deriv
  have f20 := (kds_G200_dr a M L (x 1) (x 2) hP hX).deriv
  have f21 := (kds_G200_dx a M L (x 1) (x 2) hP hX).deriv
  have f22 := (kds_G203_dr a M L (x 1) (x 2) hP hX).deriv
  have f23 := (kds_G203_dx a M L (x 1) (x 2) hP hX).deriv
  have f24 := (kds_G211_dr a M L (x 1) (x 2) hP hD).deriv
  have f25 := (kds_G211_dx a M L (x 1) (x 2) hP hD).deriv
  have f26 := (kds_G212_dr a (x 1) (x 2) hP).deriv
  have f27 := (kds_G212_dx a (x 1) (x 2) hP).deriv
  have f28 := (kds_G222_dr a L (x 1) (x 2) hP hQ hS).deriv
  have f29 := (kds_G222_dx a L (x 1) (x 2) hP hQ hS).deriv
  have f30 := (kds_G233_dr a M L (x 1) (x 2) hP hX).deriv
  have f31 := (kds_G233_dx a M L (x 1) (x 2) hP hX).deriv
  have f32 := (kds_G301_dr a M L (x 1) (x 2) hP hD).deriv
  have f33 := (kds_G301_dx a M L (x 1) (x 2) hP hD).deriv
  have f34 := (kds_G302_dr a M L (x 1) (x 2) hP hQ hS).deriv
  have f35 := (kds_G302_dx a M L (x 1) (x 2) hP hQ hS).deriv
  have f36 := (kds_G313_dr a M L (x 1) (x 2) hP hD).deriv
  have f37 := (kds_G313_dx a M L (x 1) (x 2) hP hD).deriv
  have f38 := (kds_G323_dr a M L (x 1) (x 2) hP hQ hS).deriv
  have f39 := (kds_G323_dx a M L (x 1) (x 2) hP hQ hS).deriv
  fin_cases μ <;> fin_cases ν <;>
  · unfold rn_Ric kr_Riem
    simp only [Fin.sum_univ_four, kds_pd h, hΓ]
    simp [kds_T, kr_pd, Function.update_apply, rn_kds, f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23, f24, f25, f26, f27, f28, f29, f30, f31, f32, f33, f34, f35, f36, f37, f38, f39]
    all_goals (try simp only [kds_i00, kds_i03, kds_i33, kds_i11, kds_i22, kds_g00, kds_g03, kds_g33, kds_g11, kds_g22, kds_G001, kds_G002, kds_G013, kds_G023, kds_G100, kds_G103, kds_G111, kds_G112, kds_G122, kds_G133, kds_G200, kds_G203, kds_G211, kds_G212, kds_G222, kds_G233, kds_G301, kds_G302, kds_G313, kds_G323])
    all_goals field_simp
    all_goals simp only [kds_P, kds_D, kds_Q, kds_S, kds_X]
    all_goals ring

set_option maxHeartbeats 0 in
set_option linter.unusedSimpArgs false in
lemma kds_const_curv_aux {a M L : ℝ} {x : Fin 4 → ℝ} (h : kds_Hyp a M L x) (hM : M = 0) (A B C D : Fin 4) :
    kr_Rlow (rn_kds a M L) x A B C D =
      L / 3 * (rn_kds a M L x A C * rn_kds a M L x B D - rn_kds a M L x A D * rn_kds a M L x B C) := by
  have hP := h.hP; have hD := h.hD; have hQ := h.hQ; have hS := h.hS; have hX := h.hX
  have hΓ := kds_Γ hP hD hQ hS hX
  have f0 := (kds_G001_dr a M L (x 1) (x 2) hP hD).deriv
  have f1 := (kds_G001_dx a M L (x 1) (x 2) hP hD).deriv
  have f2 := (kds_G002_dr a M L (x 1) (x 2) hP hQ).deriv
  have f3 := (kds_G002_dx a M L (x 1) (x 2) hP hQ).deriv
  have f4 := (kds_G013_dr a M L (x 1) (x 2) hP hD).deriv
  have f5 := (kds_G013_dx a M L (x 1) (x 2) hP hD).deriv
  have f6 := (kds_G023_dr a M L (x 1) (x 2) hP hQ).deriv
  have f7 := (kds_G023_dx a M L (x 1) (x 2) hP hQ).deriv
  have f8 := (kds_G100_dr a M L (x 1) (x 2) hP hX).deriv
  have f9 := (kds_G100_dx a M L (x 1) (x 2) hP hX).deriv
  have f10 := (kds_G103_dr a M L (x 1) (x 2) hP hX).deriv
  have f11 := (kds_G103_dx a M L (x 1) (x 2) hP hX).deriv
  have f12 := (kds_G111_dr a M L (x 1) (x 2) hP hD).deriv
  have f13 := (kds_G111_dx a M L (x 1) (x 2) hP hD).deriv
  have f14 := (kds_G112_dr a (x 1) (x 2) hP).deriv
  have f15 := (kds_G112_dx a (x 1) (x 2) hP).deriv
  have f16 := (kds_G122_dr a M L (x 1) (x 2) hP hQ hS).deriv
  have f17 := (kds_G122_dx a M L (x 1) (x 2) hP hQ hS).deriv
  have f18 := (kds_G133_dr a M L (x 1) (x 2) hP hX).deriv
  have f19 := (kds_G133_dx a M L (x 1) (x 2) hP hX).deriv
  have f20 := (kds_G200_dr a M L (x 1) (x 2) hP hX).deriv
  have f21 := (kds_G200_dx a M L (x 1) (x 2) hP hX).deriv
  have f22 := (kds_G203_dr a M L (x 1) (x 2) hP hX).deriv
  have f23 := (kds_G203_dx a M L (x 1) (x 2) hP hX).deriv
  have f24 := (kds_G211_dr a M L (x 1) (x 2) hP hD).deriv
  have f25 := (kds_G211_dx a M L (x 1) (x 2) hP hD).deriv
  have f26 := (kds_G212_dr a (x 1) (x 2) hP).deriv
  have f27 := (kds_G212_dx a (x 1) (x 2) hP).deriv
  have f28 := (kds_G222_dr a L (x 1) (x 2) hP hQ hS).deriv
  have f29 := (kds_G222_dx a L (x 1) (x 2) hP hQ hS).deriv
  have f30 := (kds_G233_dr a M L (x 1) (x 2) hP hX).deriv
  have f31 := (kds_G233_dx a M L (x 1) (x 2) hP hX).deriv
  have f32 := (kds_G301_dr a M L (x 1) (x 2) hP hD).deriv
  have f33 := (kds_G301_dx a M L (x 1) (x 2) hP hD).deriv
  have f34 := (kds_G302_dr a M L (x 1) (x 2) hP hQ hS).deriv
  have f35 := (kds_G302_dx a M L (x 1) (x 2) hP hQ hS).deriv
  have f36 := (kds_G313_dr a M L (x 1) (x 2) hP hD).deriv
  have f37 := (kds_G313_dx a M L (x 1) (x 2) hP hD).deriv
  have f38 := (kds_G323_dr a M L (x 1) (x 2) hP hQ hS).deriv
  have f39 := (kds_G323_dx a M L (x 1) (x 2) hP hQ hS).deriv
  have hpd := kds_pd h
  subst hM
  fin_cases A <;> fin_cases B <;> fin_cases C <;> fin_cases D <;>
  · unfold kr_Rlow kr_Riem
    simp only [Fin.sum_univ_four, hpd, hΓ]
    simp [kds_T, kr_pd, Function.update_apply, rn_kds, f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23, f24, f25, f26, f27, f28, f29, f30, f31, f32, f33, f34, f35, f36, f37, f38, f39]
    all_goals (try simp only [kds_i00, kds_i03, kds_i33, kds_i11, kds_i22, kds_g00, kds_g03, kds_g33, kds_g11, kds_g22, kds_G001, kds_G002, kds_G013, kds_G023, kds_G100, kds_G103, kds_G111, kds_G112, kds_G122, kds_G133, kds_G200, kds_G203, kds_G211, kds_G212, kds_G222, kds_G233, kds_G301, kds_G302, kds_G313, kds_G323])
    all_goals field_simp
    all_goals simp only [kds_P, kds_D, kds_Q, kds_S, kds_X]
    all_goals ring_nf
    all_goals simp

/-- **Row 4c.** The mass-free, rotation-only member (`M = 0`, any `a`) is maximally symmetric:
`R_{abcd} = (Λ/3)(g_ac g_bd − g_ad g_bc)`, all 256 components. -/
theorem kds_const_curv {a L : ℝ} {x : Fin 4 → ℝ} (h : kds_Hyp a 0 L x) (A B C D : Fin 4) :
    kr_Rlow (rn_kds a 0 L) x A B C D =
      L / 3 * (rn_kds a 0 L x A C * rn_kds a 0 L x B D - rn_kds a 0 L x A D * rn_kds a 0 L x B C) :=
  kds_const_curv_aux h rfl A B C D

/-- **Row 4b, `a → 0`.** At `a = 0` Kerr–de Sitter is Schwarzschild–de Sitter, component by component:
`diag(−f, 1/f, r²/(1−x²), r²(1−x²))` with `f = 1 − 2M/r − Λr²/3` (in `x = cos θ`, `dθ² = dx²/(1−x²)`). -/
theorem kds_sds (M L : ℝ) (y : Fin 4 → ℝ) (hr : y 1 ≠ 0) :
    rn_kds 0 M L y = !![-(1 - 2 * M / y 1 - L * y 1 ^ 2 / 3), 0, 0, 0;
      0, 1 / (1 - 2 * M / y 1 - L * y 1 ^ 2 / 3), 0, 0;
      0, 0, y 1 ^ 2 / (1 - y 2 ^ 2), 0;
      0, 0, 0, y 1 ^ 2 * (1 - y 2 ^ 2)] := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [rn_kds, kds_g00, kds_g03, kds_g33, kds_g11, kds_g22, kds_P, kds_D, kds_Q, kds_S, kds_X]
  all_goals field_simp
  all_goals ring

/-- **Row 4b, `M → 0` with `a = 0`.** The static de Sitter patch, `f = 1 − Λr²/3`. (`M = 0` with `a ≠ 0` is de Sitter in
rotating coordinates: that is row 4c.) -/
theorem kds_desitter (L : ℝ) (y : Fin 4 → ℝ) (hr : y 1 ≠ 0) :
    rn_kds 0 0 L y = !![-(1 - L * y 1 ^ 2 / 3), 0, 0, 0;
      0, 1 / (1 - L * y 1 ^ 2 / 3), 0, 0;
      0, 0, y 1 ^ 2 / (1 - y 2 ^ 2), 0;
      0, 0, 0, y 1 ^ 2 * (1 - y 2 ^ 2)] := by
  rw [kds_sds 0 L y hr]; simp

/-- **Row 4d.** The structure functions are the substrate-scale deformations of P9 eq. `deltadecomp`: with
`Λ = 3/α²`, `Δ_r = r²f_SdS + a²f_dS`, `Δ_θ = 1 + (a/α)²cos²θ`, `Ξ = 1 + (a/α)²`, where `f_SdS = 1 − 2M/r − r²/α²` and
`f_dS = 1 − r²/α²`. -/
theorem kds_deltadecomp (a M α r θ : ℝ) (hr : r ≠ 0) (hα : α ≠ 0) :
    kds_D a M (3 / α ^ 2) r = r ^ 2 * (1 - 2 * M / r - r ^ 2 / α ^ 2) + a ^ 2 * (1 - r ^ 2 / α ^ 2) ∧
      kds_Q a (3 / α ^ 2) (Real.cos θ) = 1 + (a / α) ^ 2 * Real.cos θ ^ 2 ∧
      kds_X a (3 / α ^ 2) = 1 + (a / α) ^ 2 := by
  refine ⟨?_, ?_, ?_⟩
  · simp only [kds_D]; field_simp; ring
  · simp only [kds_Q]; field_simp
  · simp only [kds_X]; field_simp

/-- **Row 4e.** The angular momentum `J = Ma/Ξ²` vanishes iff the offset or the twist is absent. -/
theorem kds_J (a M L : ℝ) (hX : kds_X a L ≠ 0) : M * a / kds_X a L ^ 2 = 0 ↔ M = 0 ∨ a = 0 := by
  simp [hX]

/-- **Row 4a, non-vacuity.** `a = M = 1`, `Λ = 3` at `r = 2`, `x = 0`: the hypotheses hold, the cross term
`g_tφ = −3/2` is non-zero, and `R_μν = Λg_μν` in all sixteen components. -/
theorem kds_witness :
    rn_kds 1 1 3 ![0, 2, 0, 0] 0 3 = -3 / 2 ∧
      ∀ μ ν, rn_Ric (rn_kds 1 1 3) ![0, 2, 0, 0] μ ν = 3 * rn_kds 1 1 3 ![0, 2, 0, 0] μ ν := by
  have h : kds_Hyp 1 1 3 ![0, 2, 0, 0] :=
    ⟨by norm_num [kds_P], by norm_num [kds_D], by norm_num [kds_Q], by norm_num [kds_S], by norm_num [kds_X]⟩
  refine ⟨?_, kds_vacuum h⟩
  norm_num [rn_kds, kds_g03, kds_P, kds_D, kds_Q, kds_S, kds_X]

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
#print axioms ShadowProbe.RangeProbe.kds_inv
#print axioms ShadowProbe.RangeProbe.kds_Γ
#print axioms ShadowProbe.RangeProbe.kds_vacuum
#print axioms ShadowProbe.RangeProbe.kds_const_curv
#print axioms ShadowProbe.RangeProbe.kds_sds
#print axioms ShadowProbe.RangeProbe.kds_desitter
#print axioms ShadowProbe.RangeProbe.kds_deltadecomp
#print axioms ShadowProbe.RangeProbe.kds_J
#print axioms ShadowProbe.RangeProbe.kds_witness

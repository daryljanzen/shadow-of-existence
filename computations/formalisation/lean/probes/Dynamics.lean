import Mathlib

/-!
# P11 (`dynamics_paper`): the de Sitter cut's admissible dynamics, the two Killing vectors, the regular wall

Campaign 142 (`r7799`). Registration: `computations/formalisation/r7799_71_campaign142/PREDICTION.md`. Mathlib only;
nothing imports this file. For the wall rows, `Range.lean`'s `KrCurvature` section, `rn_Ric`, `rn_scal`, `rn_Weyl`,
its Row 8a and Row 8b pp-wave blocks and its `ij_` definitions with `pw_IJ` are copied verbatim below, names and
namespaces kept. The new rows are in `ShadowProbe.DynamicsProbe` (`dy_`).
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


/-- The 4-D Weyl tensor `C_abcd = R_abcd − ½(g_ac R_bd − g_ad R_bc − g_bc R_ad + g_bd R_ac) + (R/6)(g_ac g_bd − g_ad g_bc)`. -/
noncomputable def rn_Weyl (g : (Fin 4 → ℝ) → Matrix (Fin 4) (Fin 4) ℝ) (x : Fin 4 → ℝ) (a b c d : Fin 4) : ℝ :=
  kr_Rlow g x a b c d - (1 / 2) * (g x a c * rn_Ric g x b d - g x a d * rn_Ric g x b c -
    g x b c * rn_Ric g x a d + g x b d * rn_Ric g x a c) +
    rn_scal g x / 6 * (g x a c * g x b d - g x a d * g x b c)


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


/-! ## Row 8b: the pp-wave's Weyl tensor is non-zero and nilpotent -/

set_option maxHeartbeats 0 in
/-- Every lowered Riemann component of the pp-wave carrying a `v` index vanishes, as does every one whose first or
second pair contains no `u` (given that the mixed partials of `H` commute at the point). -/
lemma pw_Rlow_vanish (h : ℝ → ℝ → ℝ → ℝ) (x : Fin 4 → ℝ)
    (hsym : kr_pd (fun y => kr_pd (rn_H h) y 2) x 3 = kr_pd (fun y => kr_pd (rn_H h) y 3) x 2) (a b c d : Fin 4)
    (hv : a = 1 ∨ b = 1 ∨ c = 1 ∨ d = 1 ∨ (a ≠ 0 ∧ b ≠ 0) ∨ (c ≠ 0 ∧ d ≠ 0)) :
    kr_Rlow (rn_pp h) x a b c d = 0 := by
  have v2 := rn_pd_v2 h x
  have hΓ := rn_pp_Γ h x
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases d <;> simp at hv <;>
  · unfold kr_Rlow kr_Riem
    simp only [Fin.sum_univ_four, rn_pp_pd, hΓ]
    simp [rn_ppT, rn_pp, kr_pd_const, v2, rn_pd_negHalf, hsym]

/-- The Weyl tensor of a vacuum pp-wave (`H` harmonic at the point) is its Riemann tensor. -/
lemma pw_Weyl_eq (h : ℝ → ℝ → ℝ → ℝ) (x : Fin 4 → ℝ)
    (hH : kr_pd (fun y => kr_pd (rn_H h) y 2) x 2 + kr_pd (fun y => kr_pd (rn_H h) y 3) x 3 = 0)
    (a b c d : Fin 4) : rn_Weyl (rn_pp h) x a b c d = kr_Rlow (rn_pp h) x a b c d := by
  have hR := (rn_pp_vacuum_iff h x).2 hH
  have hS : rn_scal (rn_pp h) x = 0 := by simp [rn_scal, hR]
  simp [rn_Weyl, hR, hS]

/-- The Weyl bivector operator `W^{ab}{}_{cd} = g^{aa′}g^{bb′}C_{a′b′cd}`. -/
noncomputable def pw_W (g : (Fin 4 → ℝ) → Matrix (Fin 4) (Fin 4) ℝ) (x : Fin 4 → ℝ) (a b c d : Fin 4) : ℝ :=
  ∑ a', ∑ b', (g x)⁻¹ a a' * (g x)⁻¹ b b' * rn_Weyl g x a' b' c d

lemma pw_W_up (h : ℝ → ℝ → ℝ → ℝ) (x : Fin 4 → ℝ)
    (hsym : kr_pd (fun y => kr_pd (rn_H h) y 2) x 3 = kr_pd (fun y => kr_pd (rn_H h) y 3) x 2)
    (hH : kr_pd (fun y => kr_pd (rn_H h) y 2) x 2 + kr_pd (fun y => kr_pd (rn_H h) y 3) x 3 = 0)
    (a b c d : Fin 4) (hab : a = 0 ∨ b = 0) : pw_W (rn_pp h) x a b c d = 0 := by
  have z : ∀ a' b' : Fin 4, rn_Weyl (rn_pp h) x a' b' c d = if a' = 1 ∨ b' = 1 ∨ (a' ≠ 0 ∧ b' ≠ 0) then 0
      else rn_Weyl (rn_pp h) x a' b' c d := by
    intro a' b'; split_ifs with hc
    · rw [pw_Weyl_eq h x hH]; exact pw_Rlow_vanish h x hsym a' b' c d (by tauto)
    · rfl
  rcases hab with rfl | rfl <;>
  · simp only [pw_W, rn_pp_inv, Fin.sum_univ_four]
    rw [z 0 0, z 0 1, z 0 2, z 0 3, z 1 0, z 1 1, z 1 2, z 1 3, z 2 0, z 2 1, z 2 2, z 2 3, z 3 0, z 3 1,
      z 3 2, z 3 3]
    simp

lemma pw_W_low (h : ℝ → ℝ → ℝ → ℝ) (x : Fin 4 → ℝ)
    (hsym : kr_pd (fun y => kr_pd (rn_H h) y 2) x 3 = kr_pd (fun y => kr_pd (rn_H h) y 3) x 2)
    (hH : kr_pd (fun y => kr_pd (rn_H h) y 2) x 2 + kr_pd (fun y => kr_pd (rn_H h) y 3) x 3 = 0)
    (a b c d : Fin 4) (hcd : c ≠ 0 ∧ d ≠ 0) : pw_W (rn_pp h) x a b c d = 0 := by
  simp only [pw_W, pw_Weyl_eq h x hH, pw_Rlow_vanish h x hsym _ _ c d (Or.inr (Or.inr (Or.inr (Or.inr (Or.inr hcd))))),
    mul_zero, Finset.sum_const_zero]

/-- **Row 8b (built part).** The Weyl bivector operator of a vacuum pp-wave squares to zero:
`W^{ab}{}_{cd} W^{cd}{}_{ef} = 0` for all 256 `(a, b, e, f)`. So every trace of a product of Weyl operators, and so
every contraction from which `I` and `J` are built, vanishes. -/
theorem pw_nilpotent (h : ℝ → ℝ → ℝ → ℝ) (x : Fin 4 → ℝ)
    (hsym : kr_pd (fun y => kr_pd (rn_H h) y 2) x 3 = kr_pd (fun y => kr_pd (rn_H h) y 3) x 2)
    (hH : kr_pd (fun y => kr_pd (rn_H h) y 2) x 2 + kr_pd (fun y => kr_pd (rn_H h) y 3) x 3 = 0)
    (a b e f : Fin 4) : ∑ c, ∑ d, pw_W (rn_pp h) x a b c d * pw_W (rn_pp h) x c d e f = 0 := by
  refine Finset.sum_eq_zero fun c _ => Finset.sum_eq_zero fun d _ => ?_
  by_cases hcd : c = 0 ∨ d = 0
  · rw [pw_W_up h x hsym hH c d e f hcd, mul_zero]
  · rw [pw_W_low h x hsym hH a b c d (by tauto), zero_mul]

/-- **Row 8b (built part).** The quadratic and cubic Weyl invariants of a vacuum pp-wave vanish:
`C_{ab}{}^{cd}C_{cd}{}^{ab} = 0` and `C_{ab}{}^{cd}C_{cd}{}^{ef}C_{ef}{}^{ab} = 0` (as traces of the bivector operator). -/
theorem pw_invariants (h : ℝ → ℝ → ℝ → ℝ) (x : Fin 4 → ℝ)
    (hsym : kr_pd (fun y => kr_pd (rn_H h) y 2) x 3 = kr_pd (fun y => kr_pd (rn_H h) y 3) x 2)
    (hH : kr_pd (fun y => kr_pd (rn_H h) y 2) x 2 + kr_pd (fun y => kr_pd (rn_H h) y 3) x 3 = 0) :
    ∑ a, ∑ b, ∑ c, ∑ d, pw_W (rn_pp h) x a b c d * pw_W (rn_pp h) x c d a b = 0 ∧
      ∑ a, ∑ b, ∑ c, ∑ d, ∑ e, ∑ f,
        pw_W (rn_pp h) x a b c d * pw_W (rn_pp h) x c d e f * pw_W (rn_pp h) x e f a b = 0 := by
  constructor
  · exact Finset.sum_eq_zero fun a _ => Finset.sum_eq_zero fun b _ => pw_nilpotent h x hsym hH a b a b
  · refine Finset.sum_eq_zero fun a _ => Finset.sum_eq_zero fun b _ => ?_
    have e : ∀ c d, ∑ e, ∑ f, pw_W (rn_pp h) x a b c d * pw_W (rn_pp h) x c d e f * pw_W (rn_pp h) x e f a b =
        pw_W (rn_pp h) x a b c d * ∑ e, ∑ f, pw_W (rn_pp h) x c d e f * pw_W (rn_pp h) x e f a b := by
      intro c d; simp only [Finset.mul_sum, mul_assoc]
    simp only [e, pw_nilpotent h x hsym hH, mul_zero, Finset.sum_const_zero]

/-- **Row 8b, non-vacuity.** For `H = x² − y²` the Weyl tensor is non-zero: `C_{uxux} = −1`. -/
theorem pw_witness (x : Fin 4 → ℝ) : rn_Weyl (rn_pp fun _ X Y => X ^ 2 - Y ^ 2) x 0 2 0 2 = -1 := by
  have i2 : ∀ y : Fin 4 → ℝ, kr_pd (rn_H fun _ X Y => X ^ 2 - Y ^ 2) y 2 = 2 * y 2 := fun y => by
    simp [kr_pd, rn_H]
  have i3 : ∀ y : Fin 4 → ℝ, kr_pd (rn_H fun _ X Y => X ^ 2 - Y ^ 2) y 3 = -(2 * y 3) := fun y => by
    simp [kr_pd, rn_H]
  have hH : kr_pd (fun y => kr_pd (rn_H fun _ X Y => X ^ 2 - Y ^ 2) y 2) x 2 +
      kr_pd (fun y => kr_pd (rn_H fun _ X Y => X ^ 2 - Y ^ 2) y 3) x 3 = 0 := by
    simp only [i2, i3]; simp [kr_pd]
  rw [pw_Weyl_eq _ x hH]
  unfold kr_Rlow kr_Riem
  simp only [Fin.sum_univ_four, rn_pp_Γ]
  simp [rn_ppT, rn_pp, kr_pd_const, rn_pd_negHalf, i2, i3]
  simp [kr_pd]


/-! ## Rows 7b and 8b closed: the invariants `I` and `J` -/

/-- The Levi-Civita symbol `Π_{i<j}(x_j − x_i)/12`: the sign of `(a, b, c, d)` as a permutation of `(0, 1, 2, 3)`,
and zero on a repeated index. -/
noncomputable def ij_lc (a b c d : Fin 4) : ℝ :=
  (((b : ℕ) : ℝ) - (a : ℕ)) * (((c : ℕ) : ℝ) - (a : ℕ)) * (((d : ℕ) : ℝ) - (a : ℕ)) *
    (((c : ℕ) : ℝ) - (b : ℕ)) * (((d : ℕ) : ℝ) - (b : ℕ)) * (((d : ℕ) : ℝ) - (c : ℕ)) / 12

lemma ij_lc_values : ij_lc 0 1 2 3 = 1 ∧ ij_lc 1 0 2 3 = -1 ∧ ij_lc 0 0 2 3 = 0 := by
  refine ⟨?_, ?_, ?_⟩ <;> norm_num [ij_lc]

/-- The Weyl bivector operator `W^{ab}{}_{cd}` as a matrix on ordered index pairs. -/
noncomputable def ij_W (g : (Fin 4 → ℝ) → Matrix (Fin 4) (Fin 4) ℝ) (x : Fin 4 → ℝ) :
    Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ :=
  Matrix.of fun p q => pw_W g x p.1 p.2 q.1 q.2

/-- The Hodge dual on bivectors, `½ ε^{ab}{}_{ef}`, with `ε_{abcd} = √|det g| · ij_lc a b c d`. -/
noncomputable def ij_E (g : (Fin 4 → ℝ) → Matrix (Fin 4) (Fin 4) ℝ) (x : Fin 4 → ℝ) :
    Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ :=
  Matrix.of fun p q => (1 / 2) * ∑ a', ∑ b', (g x)⁻¹ p.1 a' * (g x)⁻¹ p.2 b' *
    (Real.sqrt |(g x).det| * ij_lc a' b' q.1 q.2)

/-- `I = (K₁ − iK₂)/16` with `K₁ = C_{abcd}C^{abcd} = tr W²` and `K₂ = C_{abcd}*C^{abcd} = tr(W ∘ *W)`. -/
noncomputable def ij_I (g : (Fin 4 → ℝ) → Matrix (Fin 4) (Fin 4) ℝ) (x : Fin 4 → ℝ) : ℂ :=
  ⟨(ij_W g x * ij_W g x).trace / 16, -((ij_W g x * (ij_E g x * ij_W g x)).trace / 16)⟩

/-- `J = (K₃ − iK₄)/96` with `K₃ = C_{ab}{}^{cd}C_{cd}{}^{ef}C_{ef}{}^{ab} = tr W³` and `K₄ = tr(W² ∘ *W)`. -/
noncomputable def ij_J (g : (Fin 4 → ℝ) → Matrix (Fin 4) (Fin 4) ℝ) (x : Fin 4 → ℝ) : ℂ :=
  ⟨(ij_W g x * ij_W g x * ij_W g x).trace / 96, -((ij_W g x * ij_W g x * (ij_E g x * ij_W g x)).trace / 96)⟩

/-- **Row 8b.** A vacuum pp-wave (harmonic `H`, mixed partials commuting) has `I = J = 0`. With `pw_witness`
(Weyl ≠ 0 for `H = x² − y²`) it is type N. -/
theorem pw_IJ (h : ℝ → ℝ → ℝ → ℝ) (x : Fin 4 → ℝ)
    (hsym : kr_pd (fun y => kr_pd (rn_H h) y 2) x 3 = kr_pd (fun y => kr_pd (rn_H h) y 3) x 2)
    (hH : kr_pd (fun y => kr_pd (rn_H h) y 2) x 2 + kr_pd (fun y => kr_pd (rn_H h) y 3) x 3 = 0) :
    ij_I (rn_pp h) x = 0 ∧ ij_J (rn_pp h) x = 0 := by
  have sq : ij_W (rn_pp h) x * ij_W (rn_pp h) x = 0 := by
    ext p q
    simp only [ij_W, Matrix.mul_apply, Matrix.of_apply, Matrix.zero_apply, Fintype.sum_prod_type]
    exact pw_nilpotent h x hsym hH p.1 p.2 q.1 q.2
  have k2 : (ij_W (rn_pp h) x * (ij_E (rn_pp h) x * ij_W (rn_pp h) x)).trace = 0 := by
    rw [Matrix.trace_mul_comm, Matrix.mul_assoc, sq, Matrix.mul_zero, Matrix.trace_zero]
  refine ⟨Complex.ext ?_ ?_, Complex.ext ?_ ?_⟩
  · simp [ij_I, sq]
  · simp [ij_I, k2]
  · simp [ij_J, sq]
  · simp [ij_J, sq]

end ShadowProbe.RangeProbe

namespace ShadowProbe.DynamicsProbe

open ShadowProbe.StaticEinsteinProbe ShadowProbe.RangeProbe Real

/-! ## `prop:radiative-wall` -/

/-- **Row W1.** The wall's metric is non-degenerate: `det g = −1` for every `H`, both in the paper's form
`2 du dv + H du² + dx² + dy²` and in P9's `H du² − 2 du dv + dx² + dy²` (`v ↦ −v`). -/
theorem dy_wall_det (H : ℝ) (h : ℝ → ℝ → ℝ → ℝ) (y : Fin 4 → ℝ) :
    (!![H, 1, 0, 0; 1, 0, 0, 0; 0, 0, 1, 0; 0, 0, 0, 1] : Matrix (Fin 4) (Fin 4) ℝ).det = -1 ∧
      (rn_pp h y).det = -1 := by
  constructor
  · simp [Matrix.det_succ_row_zero, Fin.sum_univ_succ]; rfl
  · simp [rn_pp, Matrix.det_succ_row_zero, Fin.sum_univ_succ]; rfl

/-- The two-polarization profile `H = h₊(u)(x² − y²) + 2h×(u)xy`. -/
def dy_H (hp hx : ℝ → ℝ) : ℝ → ℝ → ℝ → ℝ := fun u X Y => hp u * (X ^ 2 - Y ^ 2) + 2 * hx u * X * Y

lemma dy_H_x (hp hx : ℝ → ℝ) (y : Fin 4 → ℝ) :
    kr_pd (rn_H (dy_H hp hx)) y 2 = 2 * hp (y 0) * y 2 + 2 * hx (y 0) * y 3 := by
  unfold kr_pd rn_H dy_H
  simp only [Function.update_self, Function.update_of_ne (show (0 : Fin 4) ≠ 2 by decide),
    Function.update_of_ne (show (3 : Fin 4) ≠ 2 by decide)]
  have h := (((hasDerivAt_pow 2 (y 2)).sub_const (y 3 ^ 2)).const_mul (hp (y 0))).add
    (((hasDerivAt_id (y 2)).const_mul (2 * hx (y 0))).mul_const (y 3))
  exact h.deriv.trans (by simp; ring)

lemma dy_H_y (hp hx : ℝ → ℝ) (y : Fin 4 → ℝ) :
    kr_pd (rn_H (dy_H hp hx)) y 3 = -(2 * hp (y 0) * y 3) + 2 * hx (y 0) * y 2 := by
  unfold kr_pd rn_H dy_H
  simp only [Function.update_self, Function.update_of_ne (show (0 : Fin 4) ≠ 3 by decide),
    Function.update_of_ne (show (2 : Fin 4) ≠ 3 by decide)]
  have h := ((((hasDerivAt_pow 2 (y 3)).const_sub (y 2 ^ 2))).const_mul (hp (y 0))).add
    ((hasDerivAt_id (y 3)).const_mul (2 * hx (y 0) * y 2))
  exact h.deriv.trans (by simp; ring)

lemma dy_H_second (hp hx : ℝ → ℝ) (x : Fin 4 → ℝ) :
    kr_pd (fun y => kr_pd (rn_H (dy_H hp hx)) y 2) x 2 + kr_pd (fun y => kr_pd (rn_H (dy_H hp hx)) y 3) x 3 = 0 ∧
      kr_pd (fun y => kr_pd (rn_H (dy_H hp hx)) y 2) x 3 = kr_pd (fun y => kr_pd (rn_H (dy_H hp hx)) y 3) x 2 := by
  simp only [dy_H_x, dy_H_y]
  constructor <;> simp [kr_pd]

/-- **Row W2.** The two-polarization wall is vacuum: all sixteen `R_μν = 0`, for any `h₊(u)`, `h×(u)`. -/
theorem dy_wall_vacuum (hp hx : ℝ → ℝ) (x : Fin 4 → ℝ) (b d : Fin 4) : rn_Ric (rn_pp (dy_H hp hx)) x b d = 0 :=
  (rn_pp_vacuum_iff _ x).2 (dy_H_second hp hx x).1 b d

/-- **Row W3.** The wall is curvature-regular: its scalar curvature vanishes, its Weyl bivector operator squares to
zero, and `I = J = 0`. -/
theorem dy_wall_regular (hp hx : ℝ → ℝ) (x : Fin 4 → ℝ) :
    rn_scal (rn_pp (dy_H hp hx)) x = 0 ∧
      (∀ a b e f, ∑ c, ∑ d, pw_W (rn_pp (dy_H hp hx)) x a b c d * pw_W (rn_pp (dy_H hp hx)) x c d e f = 0) ∧
      ij_I (rn_pp (dy_H hp hx)) x = 0 ∧ ij_J (rn_pp (dy_H hp hx)) x = 0 := by
  obtain ⟨hH, hsym⟩ := dy_H_second hp hx x
  refine ⟨by simp [rn_scal, dy_wall_vacuum], pw_nilpotent _ x hsym hH, (pw_IJ _ x hsym hH).1, (pw_IJ _ x hsym hH).2⟩

/-- **Row W3.** With `h₊ = 1`, `h× = 0` the Weyl tensor is nonzero (`C_uxux = −1`), so with `I = J = 0` the wall is
type N. -/
theorem dy_wall_typeN (x : Fin 4 → ℝ) : rn_Weyl (rn_pp (dy_H (fun _ => 1) (fun _ => 0))) x 0 2 0 2 = -1 := by
  have e : dy_H (fun _ => 1) (fun _ => 0) = fun _ X Y => X ^ 2 - Y ^ 2 := by
    funext u X Y; simp [dy_H]
  rw [e]; exact pw_witness x

/-! ## `prop:twoKV` -/

/-- The polarized Gowdy–de Sitter metric `eq:metric` on `(t, z, x, y)`. -/
noncomputable def dy_g (ψ γ R : ℝ → ℝ → ℝ) (y : Fin 4 → ℝ) : Matrix (Fin 4) (Fin 4) ℝ :=
  Matrix.diagonal ![-Real.exp (2 * (γ (y 0) (y 1) - ψ (y 0) (y 1))), Real.exp (2 * (γ (y 0) (y 1) - ψ (y 0) (y 1))),
    Real.exp (2 * ψ (y 0) (y 1)), R (y 0) (y 1) ^ 2 * Real.exp (-(2 * ψ (y 0) (y 1)))]

/-- The Lie derivative `(L_ξ g)_ab = ξ^c ∂_c g_ab + g_cb ∂_a ξ^c + g_ac ∂_b ξ^c`. -/
noncomputable def dy_lie (g : (Fin 4 → ℝ) → Matrix (Fin 4) (Fin 4) ℝ) (ξ : (Fin 4 → ℝ) → Fin 4 → ℝ)
    (x : Fin 4 → ℝ) (a b : Fin 4) : ℝ :=
  ∑ c, ξ x c * kr_pd (fun y => g y a b) x c + ∑ c, g x c b * kr_pd (fun y => ξ y c) x a +
    ∑ c, g x a c * kr_pd (fun y => ξ y c) x b

/-- A function of `(t, z)` alone has no `x` or `y` derivative. -/
lemma dy_pd_tz (F : ℝ → ℝ → ℝ) (x : Fin 4 → ℝ) {c : Fin 4} (hc : c = 2 ∨ c = 3) :
    kr_pd (fun y => F (y 0) (y 1)) x c = 0 := by
  unfold kr_pd
  rcases hc with rfl | rfl <;>
    simp only [Function.update_of_ne (show (0 : Fin 4) ≠ 2 by decide), Function.update_of_ne (show (1 : Fin 4) ≠ 2 by decide),
      Function.update_of_ne (show (0 : Fin 4) ≠ 3 by decide), Function.update_of_ne (show (1 : Fin 4) ≠ 3 by decide),
      deriv_const]

lemma dy_g_pd (ψ γ R : ℝ → ℝ → ℝ) (x : Fin 4 → ℝ) (a b : Fin 4) {c : Fin 4} (hc : c = 2 ∨ c = 3) :
    kr_pd (fun y => dy_g ψ γ R y a b) x c = 0 := by
  fin_cases a <;> fin_cases b <;> simp [dy_g] <;>
    first
    | exact dy_pd_tz (fun t z => -Real.exp (2 * (γ t z - ψ t z))) x hc
    | exact dy_pd_tz (fun t z => Real.exp (2 * (γ t z - ψ t z))) x hc
    | exact dy_pd_tz (fun t z => Real.exp (2 * ψ t z)) x hc
    | exact dy_pd_tz (fun t z => R t z ^ 2 * Real.exp (-(2 * ψ t z))) x hc
    | exact kr_pd_const 0 x c

/-- **Row K1.** `∂_x` and `∂_y` are Killing vectors of `eq:metric` for every `ψ, γ, R`. -/
theorem dy_killing_xy (ψ γ R : ℝ → ℝ → ℝ) (x : Fin 4 → ℝ) (a b : Fin 4) :
    dy_lie (dy_g ψ γ R) (fun _ => Pi.single 2 1) x a b = 0 ∧ dy_lie (dy_g ψ γ R) (fun _ => Pi.single 3 1) x a b = 0 := by
  constructor <;>
  · simp only [dy_lie, kr_pd_const, mul_zero, Finset.sum_const_zero, add_zero]
    refine Finset.sum_eq_zero fun c _ => ?_
    by_cases h2 : c = 2
    · subst h2; simp [dy_g_pd ψ γ R x a b (Or.inl rfl)]
    · by_cases h3 : c = 3
      · subst h3; simp [dy_g_pd ψ γ R x a b (Or.inr rfl)]
      · simp [h2, h3]

/-- The test profile `ψ = sin t cos z`. -/
noncomputable def dy_ψ : ℝ → ℝ → ℝ := fun t z => Real.sin t * Real.cos z

lemma dy_pd_t (γ R : ℝ → ℝ → ℝ) (x : Fin 4 → ℝ) :
    kr_pd (fun y => dy_g dy_ψ γ R y 2 2) x 0 =
      2 * (Real.cos (x 0) * Real.cos (x 1)) * Real.exp (2 * (Real.sin (x 0) * Real.cos (x 1))) := by
  unfold kr_pd
  simp only [dy_g, dy_ψ, Matrix.diagonal_apply_eq, Matrix.cons_val, Function.update_self,
    Function.update_of_ne (show (1 : Fin 4) ≠ 0 by decide)]
  have h := (((Real.hasDerivAt_sin (x 0)).mul_const (Real.cos (x 1))).const_mul 2).exp
  exact h.deriv.trans (by ring)

lemma dy_pd_z (γ R : ℝ → ℝ → ℝ) (x : Fin 4 → ℝ) :
    kr_pd (fun y => dy_g dy_ψ γ R y 2 2) x 1 =
      -(2 * (Real.sin (x 0) * Real.sin (x 1))) * Real.exp (2 * (Real.sin (x 0) * Real.cos (x 1))) := by
  unfold kr_pd
  simp only [dy_g, dy_ψ, Matrix.diagonal_apply_eq, Matrix.cons_val, Function.update_self,
    Function.update_of_ne (show (0 : Fin 4) ≠ 1 by decide)]
  have h := (((Real.hasDerivAt_cos (x 1)).const_mul (Real.sin (x 0))).const_mul 2).exp
  exact h.deriv.trans (by ring)

/-- **Row K2.** For `ψ = sin t cos z` and any `γ, R`, none of `∂_t`, `∂_z`, the boost `z∂_t + t∂_z` is Killing:
`(L_ξ g)_xx` is `2` at `(t, z) = (0, 0)`, `−2` at `(π/2, π/2)`, and `2 cos 1 ≠ 0` at `(0, 1)`. -/
theorem dy_not_killing (γ R : ℝ → ℝ → ℝ) :
    dy_lie (dy_g dy_ψ γ R) (fun _ => Pi.single 0 1) ![0, 0, 0, 0] 2 2 = 2 ∧
      dy_lie (dy_g dy_ψ γ R) (fun _ => Pi.single 1 1) ![π / 2, π / 2, 0, 0] 2 2 = -2 ∧
      dy_lie (dy_g dy_ψ γ R) (fun y => ![y 1, y 0, 0, 0]) ![0, 1, 0, 0] 2 2 = 2 * Real.cos 1 ∧ Real.cos 1 ≠ 0 := by
  have hb : ∀ x : Fin 4 → ℝ, kr_pd (fun y => (![y 1, y 0, 0, 0] : Fin 4 → ℝ) 2) x 2 = 0 := fun x => by
    simpa using kr_pd_const (0 : ℝ) x 2
  refine ⟨?_, ?_, ?_, (Real.cos_pos_of_mem_Ioo ⟨by linarith [Real.pi_gt_three], by linarith [Real.pi_gt_three]⟩).ne'⟩
  · simp only [dy_lie, Fin.sum_univ_four, kr_pd_const, dy_pd_t]
    simp [dy_g]
  · simp only [dy_lie, Fin.sum_univ_four, kr_pd_const, dy_pd_z]
    simp [dy_g]
  · simp only [dy_lie, Fin.sum_univ_four, dy_pd_t, dy_pd_z, hb]
    simp [dy_g]

/-! ## P11's first proposition: the de Sitter cut's admissible dynamics -/

/-- The isotropic background `ψ(t) = −log(c − kt)`. -/
noncomputable def dy_bg (c k t : ℝ) : ℝ := -Real.log (c - k * t)

/-- Cosmic time `τ(t) = −(1/k) log(c − kt)`, `dτ = e^ψ dt`. -/
noncomputable def dy_τ (c k t : ℝ) : ℝ := -(Real.log (c - k * t) / k)

/-- **Row A1.** On `c − kt > 0`, `ψ = −log(c − kt)` has `ψ_t = k e^ψ` and `ψ_tt = ψ_t²` (ENERGY); with `k² = Λ/3`,
`3ψ_t² = Λe^{2ψ}` (AREA). Cosmic time has `dτ/dt = e^ψ`, and the scale factor `a = e^ψ` is `e^{kτ}`: exact de Sitter
with `H = k`, `H² = Λ/3`. -/
theorem dy_desitter {c k Λ t : ℝ} (hk : k ≠ 0) (hpos : 0 < c - k * t) (hΛ : k ^ 2 = Λ / 3) :
    HasDerivAt (dy_bg c k) (k * Real.exp (dy_bg c k t)) t ∧
      HasDerivAt (fun s => k * Real.exp (dy_bg c k s)) ((k * Real.exp (dy_bg c k t)) ^ 2) t ∧
      3 * (k * Real.exp (dy_bg c k t)) ^ 2 = Λ * Real.exp (2 * dy_bg c k t) ∧
      HasDerivAt (dy_τ c k) (Real.exp (dy_bg c k t)) t ∧ Real.exp (dy_bg c k t) = Real.exp (k * dy_τ c k t) := by
  have hne : c - k * t ≠ 0 := hpos.ne'
  have he : ∀ s, 0 < c - k * s → Real.exp (dy_bg c k s) = 1 / (c - k * s) := fun s hs => by
    rw [dy_bg, Real.exp_neg, Real.exp_log hs, one_div]
  have hlin : HasDerivAt (fun s => c - k * s) (-k) t := by
    simpa using (hasDerivAt_id t).const_mul k |>.const_sub c
  have hlog : HasDerivAt (fun s => Real.log (c - k * s)) (-k / (c - k * t)) t := hlin.log hne
  have h1 : HasDerivAt (dy_bg c k) (k * Real.exp (dy_bg c k t)) t := by
    rw [he t hpos]
    convert hlog.neg using 1
    · funext s; simp [dy_bg]
    · rw [neg_div, neg_neg]; ring
  refine ⟨h1, ?_, ?_, ?_, ?_⟩
  · -- `k e^ψ = k/(c − kt)` near `t`
    have hev : (fun s => k * Real.exp (dy_bg c k s)) =ᶠ[𝓝 t] fun s => k / (c - k * s) := by
      filter_upwards [(continuous_const.sub (continuous_const.mul continuous_id)).continuousAt.eventually
        (lt_mem_nhds hpos)] with s hs
      rw [he s hs]; ring
    refine HasDerivAt.congr_of_eventuallyEq ?_ hev
    rw [he t hpos]
    convert (hasDerivAt_const t k).div hlin hne using 1
    field_simp
    ring
  · rw [show 2 * dy_bg c k t = dy_bg c k t + dy_bg c k t by ring, Real.exp_add, he t hpos,
      show Λ = 3 * k ^ 2 by linarith]
    ring
  · rw [he t hpos]
    convert (hlog.div_const k).neg using 1
    · funext s; simp [dy_τ]
    · field_simp
  · congr 1
    rw [dy_τ, dy_bg]
    field_simp

/-- **Row A2.** The shear charge. If WAVE `(Rψ_t)_t = ΛRe^{2(γ−ψ)}` and AREA `R_tt = 2ΛRe^{2(γ−ψ)}` hold on a homogeneous
cut (`R₁ = R_t`, `ψ₁ = ψ_t`), then `C₀ = R_t − 2Rψ_t` is constant (AREA − 2·WAVE cancels the `Λ` source); and the
shear shape `s = ψ − ½ log R` has `2R s_t = −C₀`. -/
theorem dy_shear {R R1 ψ ψ1 γ : ℝ → ℝ} {Λ : ℝ}
    (hwave : ∀ t, HasDerivAt (fun s => R s * ψ1 s) (Λ * R t * Real.exp (2 * (γ t - ψ t))) t)
    (harea : ∀ t, HasDerivAt R1 (2 * Λ * R t * Real.exp (2 * (γ t - ψ t))) t) :
    (∀ t, R1 t - 2 * (R t * ψ1 t) = R1 0 - 2 * (R 0 * ψ1 0)) ∧
      ∀ t, HasDerivAt R (R1 t) t → HasDerivAt ψ (ψ1 t) t → 0 < R t →
        HasDerivAt (fun s => ψ s - Real.log (R s) / 2) (-(R1 t - 2 * (R t * ψ1 t)) / (2 * R t)) t := by
  have hC : ∀ t, HasDerivAt (fun s => R1 s - 2 * (R s * ψ1 s)) 0 t := fun t => by
    convert (harea t).sub ((hwave t).const_mul 2) using 1; ring
  refine ⟨fun t => is_const_of_deriv_eq_zero (fun s => (hC s).differentiableAt) (fun s => (hC s).deriv) t 0,
    fun t hR hψ hpos => ?_⟩
  convert hψ.sub ((hR.log hpos.ne').div_const 2) using 1
  field_simp
  ring

/-- The two Mukhanov modes `W₁ = cos kη − sin kη/(kη)`, `W₂ = −sin kη − cos kη/(kη)`. -/
noncomputable def dy_W1 (k η : ℝ) : ℝ := Real.cos (k * η) - Real.sin (k * η) / (k * η)
noncomputable def dy_W2 (k η : ℝ) : ℝ := -Real.sin (k * η) - Real.cos (k * η) / (k * η)

lemma dy_hs (k η : ℝ) : HasDerivAt (fun η => Real.sin (k * η)) (k * Real.cos (k * η)) η := by
  have := (Real.hasDerivAt_sin (k * η)).comp η ((hasDerivAt_id η).const_mul k)
  convert this using 1
  · rfl
  · ring

lemma dy_hc (k η : ℝ) : HasDerivAt (fun η => Real.cos (k * η)) (-(k * Real.sin (k * η))) η := by
  have := (Real.hasDerivAt_cos (k * η)).comp η ((hasDerivAt_id η).const_mul k)
  convert this using 1
  · rfl
  · ring

lemma dy_hp (k η : ℝ) (n : ℕ) : HasDerivAt (fun η => k * η ^ n) (k * (n * η ^ (n - 1))) η :=
  (hasDerivAt_pow n η).const_mul k

/-- **Row A3.** `W₁` solves the Mukhanov equation `W″ + (k² − 2/η²)W = 0` (`eq:mukhanov`) at every `η ≠ 0`. -/
theorem dy_W1_mukhanov {k η : ℝ} (hk : k ≠ 0) (hη : η ≠ 0) :
    HasDerivAt (dy_W1 k) (-(k * Real.sin (k * η)) - Real.cos (k * η) / η + Real.sin (k * η) / (k * η ^ 2)) η ∧
      HasDerivAt (fun η => -(k * Real.sin (k * η)) - Real.cos (k * η) / η + Real.sin (k * η) / (k * η ^ 2))
        (-(k ^ 2 * Real.cos (k * η)) + k * Real.sin (k * η) / η + 2 * Real.cos (k * η) / η ^ 2 -
          2 * Real.sin (k * η) / (k * η ^ 3)) η ∧
      (-(k ^ 2 * Real.cos (k * η)) + k * Real.sin (k * η) / η + 2 * Real.cos (k * η) / η ^ 2 -
          2 * Real.sin (k * η) / (k * η ^ 3)) + (k ^ 2 - 2 / η ^ 2) * dy_W1 k η = 0 := by
  have hk1 : k * η ^ 1 ≠ 0 := by simp [hk, hη]
  have hk2 : k * η ^ 2 ≠ 0 := by simp [hk, hη]
  have h1 : (1 : ℝ) * η ^ 1 ≠ 0 := by simp [hη]
  refine ⟨?_, ?_, ?_⟩
  · have := (dy_hc k η).sub ((dy_hs k η).div (dy_hp k η 1) hk1)
    convert this using 1
    · funext s; simp [dy_W1]
    · field_simp; ring
  · have := (((dy_hs k η).const_mul k).neg.sub ((dy_hc k η).div (dy_hp 1 η 1) h1)).add
      ((dy_hs k η).div (dy_hp k η 2) hk2)
    convert this using 1
    · funext s; simp only [Pi.add_apply, Pi.sub_apply, Pi.neg_apply, Pi.div_apply, one_mul, pow_one]
    · field_simp; ring
  · simp only [dy_W1]; field_simp; ring

/-- **Row A3.** `W₂` solves the Mukhanov equation at every `η ≠ 0`. -/
theorem dy_W2_mukhanov {k η : ℝ} (hk : k ≠ 0) (hη : η ≠ 0) :
    HasDerivAt (dy_W2 k) (-(k * Real.cos (k * η)) + Real.sin (k * η) / η + Real.cos (k * η) / (k * η ^ 2)) η ∧
      HasDerivAt (fun η => -(k * Real.cos (k * η)) + Real.sin (k * η) / η + Real.cos (k * η) / (k * η ^ 2))
        (k ^ 2 * Real.sin (k * η) + k * Real.cos (k * η) / η - 2 * Real.sin (k * η) / η ^ 2 -
          2 * Real.cos (k * η) / (k * η ^ 3)) η ∧
      (k ^ 2 * Real.sin (k * η) + k * Real.cos (k * η) / η - 2 * Real.sin (k * η) / η ^ 2 -
          2 * Real.cos (k * η) / (k * η ^ 3)) + (k ^ 2 - 2 / η ^ 2) * dy_W2 k η = 0 := by
  have hk1 : k * η ^ 1 ≠ 0 := by simp [hk, hη]
  have hk2 : k * η ^ 2 ≠ 0 := by simp [hk, hη]
  have h1 : (1 : ℝ) * η ^ 1 ≠ 0 := by simp [hη]
  refine ⟨?_, ?_, ?_⟩
  · have := (dy_hs k η).neg.sub ((dy_hc k η).div (dy_hp k η 1) hk1)
    convert this using 1
    · funext s; simp [dy_W2]
    · field_simp; ring
  · have := (((dy_hc k η).const_mul k).neg.add ((dy_hs k η).div (dy_hp 1 η 1) h1)).add
      ((dy_hc k η).div (dy_hp k η 2) hk2)
    convert this using 1
    · funext s; simp only [Pi.add_apply, Pi.neg_apply, Pi.div_apply, one_mul, pow_one]
    · field_simp; ring
  · simp only [dy_W2]; field_simp; ring

/-- **Row A3.** `Q = W/a` with `a = −1/(Hη)` is bounded as `η → 0⁻`: the branch from `W₂` tends to the constant
`H/k` (the frozen mode), and the branch from `W₁` is `O(η³)` (`∝ a⁻³`): `|Q₁| ≤ |H| k² |η|³` for `|kη| ≤ 1`. -/
theorem dy_Q_bounded {k H : ℝ} (hk : k ≠ 0) :
    Tendsto (fun η => -(H * η) * dy_W2 k η) (𝓝[<] 0) (𝓝 (H / k)) ∧
      ∀ η, η ≠ 0 → |k * η| ≤ 1 → |-(H * η) * dy_W1 k η| ≤ |H| * k ^ 2 * |η| ^ 3 := by
  constructor
  · have hc : Continuous fun η => H * η * Real.sin (k * η) + H * Real.cos (k * η) / k := by fun_prop
    have h0 := hc.tendsto 0
    simp only [mul_zero, Real.sin_zero, Real.cos_zero, mul_one, zero_add] at h0
    refine (h0.mono_left nhdsWithin_le_nhds).congr' ?_
    filter_upwards [self_mem_nhdsWithin] with η (hη : η < 0)
    have hη0 : η ≠ 0 := hη.ne
    simp only [dy_W2]
    field_simp
    ring
  · intro η hη hu
    set u := k * η with hu_def
    have hu0 : u ≠ 0 := by simp [hu_def, hk, hη]
    have hcb := Real.cos_bound hu
    have hsb := Real.sin_bound hu
    -- `W₁ = (cos u − (1 − u²/2)) − (sin u − (u − u³/6))/u − u²/3`
    have hW : dy_W1 k η = (Real.cos u - (1 - u ^ 2 / 2)) - (Real.sin u - (u - u ^ 3 / 6)) / u - u ^ 2 / 3 := by
      simp only [dy_W1, ← hu_def]; field_simp; ring
    have hau : |u| ≤ 1 := hu
    have hW' : |dy_W1 k η| ≤ u ^ 2 := by
      rw [hW]
      have e1 : |(Real.sin u - (u - u ^ 3 / 6)) / u| ≤ |u| ^ 4 / 100 := by
        rw [abs_div, div_le_iff₀ (abs_pos.2 hu0)]
        calc |Real.sin u - (u - u ^ 3 / 6)| ≤ |u| ^ 5 / 100 := hsb
          _ = |u| ^ 4 / 100 * |u| := by ring
      have hu4 : |u| ^ 4 ≤ u ^ 2 := by
        rw [show |u| ^ 4 = u ^ 2 * |u| ^ 2 by rw [← sq_abs u]; ring]
        exact mul_le_of_le_one_right (sq_nonneg u) (pow_le_one₀ (abs_nonneg u) hau)
      calc |(Real.cos u - (1 - u ^ 2 / 2)) - (Real.sin u - (u - u ^ 3 / 6)) / u - u ^ 2 / 3|
          ≤ |Real.cos u - (1 - u ^ 2 / 2)| + |(Real.sin u - (u - u ^ 3 / 6)) / u| + |u ^ 2 / 3| := by
            have := abs_sub (Real.cos u - (1 - u ^ 2 / 2) - (Real.sin u - (u - u ^ 3 / 6)) / u) (u ^ 2 / 3)
            have := abs_sub (Real.cos u - (1 - u ^ 2 / 2)) ((Real.sin u - (u - u ^ 3 / 6)) / u)
            linarith
        _ ≤ |u| ^ 4 * (5 / 96) + |u| ^ 4 / 100 + u ^ 2 / 3 := by
            have h3 : |u ^ 2 / 3| = u ^ 2 / 3 := abs_of_nonneg (by positivity)
            rw [h3]
            linarith
        _ ≤ u ^ 2 := by nlinarith
    calc |-(H * η) * dy_W1 k η| = |H| * |η| * |dy_W1 k η| := by rw [abs_mul, abs_neg, abs_mul]
      _ ≤ |H| * |η| * u ^ 2 := by gcongr
      _ = |H| * k ^ 2 * |η| ^ 3 := by rw [hu_def, mul_pow, ← sq_abs η]; ring

/-! ## Non-vacuity -/

/-- **Witnesses.** The de Sitter background at `Λ = 3`, `c = k = 1`, `t = 0`; the Mukhanov modes at `k = 1`,
`η = −1`; the wall at `h₊ = 1`, `h× = 0` (vacuum, with `C_uxux = −1`). K2's points are explicit in `dy_not_killing`. -/
theorem dy_witness (x : Fin 4 → ℝ) :
    HasDerivAt (dy_bg 1 1) (1 * Real.exp (dy_bg 1 1 0)) 0 ∧
      3 * (1 * Real.exp (dy_bg 1 1 0)) ^ 2 = 3 * Real.exp (2 * dy_bg 1 1 0) ∧
      HasDerivAt (dy_W1 1) (-(1 * Real.sin (1 * -1)) - Real.cos (1 * -1) / -1 + Real.sin (1 * -1) / (1 * (-1) ^ 2))
        (-1) ∧
      HasDerivAt (dy_W2 1) (-(1 * Real.cos (1 * -1)) + Real.sin (1 * -1) / -1 + Real.cos (1 * -1) / (1 * (-1) ^ 2))
        (-1) ∧
      (∀ b d, rn_Ric (rn_pp (dy_H (fun _ => 1) (fun _ => 0))) x b d = 0) ∧
      rn_Weyl (rn_pp (dy_H (fun _ => 1) (fun _ => 0))) x 0 2 0 2 = -1 := by
  have hA := dy_desitter (c := 1) (k := 1) (Λ := 3) (t := 0) one_ne_zero (by norm_num) (by norm_num)
  exact ⟨hA.1, hA.2.2.1, (dy_W1_mukhanov one_ne_zero (by norm_num)).1, (dy_W2_mukhanov one_ne_zero (by norm_num)).1,
    dy_wall_vacuum _ _ x, dy_wall_typeN x⟩

end ShadowProbe.DynamicsProbe


namespace ShadowProbe.RangeProbe

/-- The bivector table `W^{ab}{}_{cd} = U_ab(δ_ac δ_bd − δ_ad δ_bc)` for `a ≠ b`. -/
def ij_tbl (u : Matrix (Fin 4) (Fin 4) ℝ) : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ :=
  Matrix.of fun p q => if p.1 = q.1 ∧ p.2 = q.2 ∧ p.1 ≠ p.2 then u p.1 p.2
    else if p.1 = q.2 ∧ p.2 = q.1 ∧ p.1 ≠ p.2 then -u p.1 p.2 else 0

/-- Supported on pair blocks: `X p q = 0` unless `q = p` or `q = p.swap`. -/
def ij_blk (X : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ) : Prop :=
  ∀ p q : Fin 4 × Fin 4, q ≠ p → q ≠ p.swap → X p q = 0

lemma ij_tbl_blk (u : Matrix (Fin 4) (Fin 4) ℝ) : ij_blk (ij_tbl u) := by
  intro p q h1 h2
  simp only [ij_tbl, Matrix.of_apply]
  split_ifs with c1 c2
  · exact absurd (Prod.ext c1.1.symm c1.2.1.symm) h1
  · exact absurd (Prod.ext c2.2.1.symm c2.1.symm) h2
  · rfl

lemma ij_blk_mul {X Y : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ} (hX : ij_blk X) (hY : ij_blk Y) :
    ij_blk (X * Y) := by
  intro p q h1 h2
  simp only [Matrix.mul_apply]
  refine Finset.sum_eq_zero fun r _ => ?_
  by_cases hr1 : r = p
  · subst hr1; rw [hY r q h1 h2, mul_zero]
  by_cases hr2 : r = p.swap
  · subst hr2; rw [hY _ q h2 (by rwa [Prod.swap_swap]), mul_zero]
  · rw [hX p r hr1 hr2, zero_mul]

/-- A dual trace vanishes on block-supported operators: `tr(X ∘ E ∘ Y) = 0` when `E` kills each block. -/
lemma ij_tr_dual {X Y E : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ} (hX : ij_blk X) (hY : ij_blk Y)
    (hE : ∀ q r : Fin 4 × Fin 4, (r = q ∨ r = q.swap) → E q r = 0) : (X * (E * Y)).trace = 0 := by
  simp only [Matrix.trace, Matrix.diag, Matrix.mul_apply, Finset.mul_sum]
  refine Finset.sum_eq_zero fun p _ => Finset.sum_eq_zero fun q _ => Finset.sum_eq_zero fun r _ => ?_
  by_cases hq : q = p ∨ q = p.swap
  · by_cases hr : r = p ∨ r = p.swap
    · rw [hE q r ?_, zero_mul, mul_zero]
      rcases hq with rfl | rfl <;> rcases hr with rfl | rfl <;> simp
    · simp only [not_or] at hr
      rw [hY r p (Ne.symm hr.1) (fun e => hr.2 (by rw [e, Prod.swap_swap])), mul_zero, mul_zero]
  · simp only [not_or] at hq
    rw [hX p q hq.1 hq.2, zero_mul]

lemma ij_tr2 (u : Matrix (Fin 4) (Fin 4) ℝ) : (ij_tbl u * ij_tbl u).trace =
    ∑ a, ∑ b, if a = b then 0 else (u a b ^ 2 + u a b * u b a) := by
  simp [Matrix.trace, Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_four, ij_tbl]
  ring

set_option maxHeartbeats 0 in
lemma ij_tr3 (u : Matrix (Fin 4) (Fin 4) ℝ) : (ij_tbl u * ij_tbl u * ij_tbl u).trace =
    ∑ a, ∑ b, if a = b then 0 else (u a b + u b a) ^ 3 / 2 := by
  simp [Matrix.trace, Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_four, ij_tbl]
  ring

end ShadowProbe.RangeProbe

namespace ShadowProbe.DynamicsProbe

open ShadowProbe.StaticEinsteinProbe ShadowProbe.RangeProbe Real

/-! ## K4: a vacuum-Λ point of the Gowdy–de Sitter form at which the Weyl tensor is Petrov type I -/

/-- `B(t, z) = 1 + 2t + 5t² + z²` and `C(t, z) = 1 + 2z − t² − 3z²`. -/
def dy_Bf (t z : ℝ) : ℝ := 1 + 2 * t + 5 * t ^ 2 + z ^ 2
def dy_Cf (t z : ℝ) : ℝ := 1 + 2 * z - t ^ 2 - 3 * z ^ 2
def dy_B (y : Fin 4 → ℝ) : ℝ := dy_Bf (y 0) (y 1)
def dy_C (y : Fin 4 → ℝ) : ℝ := dy_Cf (y 0) (y 1)

/-- The metric `diag(−1, 1, B, C)` on `(t, z, x, y)`. -/
def dy_gk (y : Fin 4 → ℝ) : Matrix (Fin 4) (Fin 4) ℝ := Matrix.diagonal ![-1, 1, dy_B y, dy_C y]

lemma dy_B_pos (y : Fin 4 → ℝ) : 0 < dy_B y := by
  unfold dy_B dy_Bf; nlinarith [sq_nonneg (5 * y 0 + 1), sq_nonneg (y 1)]

/-- **K4, the form.** Where `C > 0`, `diag(−1, 1, B, C)` is `eq:metric` with `γ = ψ = ½ log B`, `R = √(BC)`. -/
theorem dy_gk_form (y : Fin 4 → ℝ) (hC : 0 < dy_C y) :
    dy_gk y = dy_g (fun t z => Real.log (dy_Bf t z) / 2) (fun t z => Real.log (dy_Bf t z) / 2)
      (fun t z => Real.sqrt (dy_Bf t z * dy_Cf t z)) y := by
  have hB := dy_B_pos y
  unfold dy_B at hB; unfold dy_C at hC
  have e1 : Real.exp (2 * (Real.log (dy_Bf (y 0) (y 1)) / 2)) = dy_Bf (y 0) (y 1) := by
    rw [show 2 * (Real.log (dy_Bf (y 0) (y 1)) / 2) = Real.log (dy_Bf (y 0) (y 1)) by ring, Real.exp_log hB]
  have e2 : Real.exp (-(2 * (Real.log (dy_Bf (y 0) (y 1)) / 2))) = (dy_Bf (y 0) (y 1))⁻¹ := by
    rw [Real.exp_neg, e1]
  have e3 : Real.sqrt (dy_Bf (y 0) (y 1) * dy_Cf (y 0) (y 1)) ^ 2 = dy_Bf (y 0) (y 1) * dy_Cf (y 0) (y 1) :=
    Real.sq_sqrt (by positivity)
  unfold dy_gk dy_g dy_B dy_C
  congr 1
  ext i; fin_cases i <;> simp [e1, e2, e3]
  field_simp

/-! ### The Christoffel table -/

/-- A partial derivative read off a derivative along the coordinate line. -/
lemma dy_pd_of {F : (Fin 4 → ℝ) → ℝ} {y : Fin 4 → ℝ} {c : Fin 4} (φ : ℝ → ℝ) {v : ℝ}
    (hφ : ∀ s, F (Function.update y c s) = φ s) (h : HasDerivAt φ v (y c)) : kr_pd F y c = v := by
  unfold kr_pd; rw [show (fun t => F (Function.update y c t)) = φ from funext hφ]; exact h.deriv

lemma dy_quad (a b c x : ℝ) : HasDerivAt (fun s => a + b * s + c * s ^ 2) (b + 2 * c * x) x := by
  have := (((hasDerivAt_id' x).const_mul b).const_add a).fun_add ((hasDerivAt_pow 2 x).const_mul c)
  convert this using 1; push_cast; ring

lemma dy_rat0 (a b q0 q1 q2 : ℝ) (hq : q0 ≠ 0) :
    HasDerivAt (fun s => (a + b * s) / (q0 + q1 * s + q2 * s ^ 2)) ((b * q0 - a * q1) / q0 ^ 2) 0 := by
  have h1 := (dy_quad a b 0 0)
  have h2 := (dy_quad q0 q1 q2 0)
  have := h1.div h2 (by simpa using hq)
  convert this using 1
  · funext s; simp
  · simp

lemma dy_B_pd0 (y : Fin 4 → ℝ) : kr_pd dy_B y 0 = 2 + 10 * y 0 :=
  dy_pd_of (fun s => (1 + y 1 ^ 2) + 2 * s + 5 * s ^ 2) (fun s => by simp [dy_B, dy_Bf]; ring)
    (by convert dy_quad (1 + y 1 ^ 2) 2 5 (y 0) using 1; ring)
lemma dy_B_pd1 (y : Fin 4 → ℝ) : kr_pd dy_B y 1 = 2 * y 1 :=
  dy_pd_of (fun s => (1 + 2 * y 0 + 5 * y 0 ^ 2) + 0 * s + 1 * s ^ 2) (fun s => by simp [dy_B, dy_Bf])
    (by convert dy_quad (1 + 2 * y 0 + 5 * y 0 ^ 2) 0 1 (y 1) using 1; ring)
lemma dy_C_pd0 (y : Fin 4 → ℝ) : kr_pd dy_C y 0 = -(2 * y 0) :=
  dy_pd_of (fun s => (1 + 2 * y 1 - 3 * y 1 ^ 2) + 0 * s + (-1) * s ^ 2) (fun s => by simp [dy_C, dy_Cf]; ring)
    (by convert dy_quad (1 + 2 * y 1 - 3 * y 1 ^ 2) 0 (-1) (y 0) using 1; ring)
lemma dy_C_pd1 (y : Fin 4 → ℝ) : kr_pd dy_C y 1 = 2 - 6 * y 1 :=
  dy_pd_of (fun s => (1 - y 0 ^ 2) + 2 * s + (-3) * s ^ 2) (fun s => by simp [dy_C, dy_Cf]; ring)
    (by convert dy_quad (1 - y 0 ^ 2) 2 (-3) (y 1) using 1; ring)

/-- A function of `(t, z)` alone has no `x` or `y` partial. -/
lemma dy_pd23 (F : ℝ → ℝ → ℝ) (y : Fin 4 → ℝ) : kr_pd (fun y => F (y 0) (y 1)) y 2 = 0 ∧
    kr_pd (fun y => F (y 0) (y 1)) y 3 = 0 :=
  ⟨dy_pd_of (fun _ => F (y 0) (y 1)) (fun s => by simp) (hasDerivAt_const _ _),
    dy_pd_of (fun _ => F (y 0) (y 1)) (fun s => by simp) (hasDerivAt_const _ _)⟩

lemma dy_B_pd (y : Fin 4 → ℝ) (c : Fin 4) : kr_pd dy_B y c = ![2 + 10 * y 0, 2 * y 1, 0, 0] c := by
  fin_cases c
  · simpa using dy_B_pd0 y
  · simpa using dy_B_pd1 y
  · show kr_pd dy_B y 2 = 0; exact (dy_pd23 dy_Bf y).1
  · show kr_pd dy_B y 3 = 0; exact (dy_pd23 dy_Bf y).2

lemma dy_C_pd (y : Fin 4 → ℝ) (c : Fin 4) : kr_pd dy_C y c = ![-(2 * y 0), 2 - 6 * y 1, 0, 0] c := by
  fin_cases c
  · simpa using dy_C_pd0 y
  · simpa using dy_C_pd1 y
  · show kr_pd dy_C y 2 = 0; exact (dy_pd23 dy_Cf y).1
  · show kr_pd dy_C y 3 = 0; exact (dy_pd23 dy_Cf y).2

/-- The eight Christoffel functions. -/
def dy_k1 (y : Fin 4 → ℝ) : ℝ := 1 + 5 * y 0
def dy_k2 (y : Fin 4 → ℝ) : ℝ := -y 0
def dy_k3 (y : Fin 4 → ℝ) : ℝ := -y 1
def dy_k4 (y : Fin 4 → ℝ) : ℝ := 3 * y 1 - 1
noncomputable def dy_k5 (y : Fin 4 → ℝ) : ℝ := (1 + 5 * y 0) / dy_B y
noncomputable def dy_k6 (y : Fin 4 → ℝ) : ℝ := y 1 / dy_B y
noncomputable def dy_k7 (y : Fin 4 → ℝ) : ℝ := -y 0 / dy_C y
noncomputable def dy_k8 (y : Fin 4 → ℝ) : ℝ := (1 - 3 * y 1) / dy_C y

/-- The Christoffel table `Γ^a_{bc}` of `diag(−1, 1, B, C)`. -/
noncomputable def dy_Tk (y : Fin 4 → ℝ) : Fin 4 → Fin 4 → Fin 4 → ℝ :=
  ![![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, dy_k1 y, 0], ![0, 0, 0, dy_k2 y]],
    ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, dy_k3 y, 0], ![0, 0, 0, dy_k4 y]],
    ![![0, 0, dy_k5 y, 0], ![0, 0, dy_k6 y, 0], ![dy_k5 y, dy_k6 y, 0, 0], ![0, 0, 0, 0]],
    ![![0, 0, 0, dy_k7 y], ![0, 0, 0, dy_k8 y], ![0, 0, 0, 0], ![dy_k7 y, dy_k8 y, 0, 0]]]

lemma dy_gk_inv (y : Fin 4 → ℝ) (hC : dy_C y ≠ 0) :
    (dy_gk y)⁻¹ = Matrix.diagonal ![-1, 1, (dy_B y)⁻¹, (dy_C y)⁻¹] := by
  have hB := (dy_B_pos y).ne'
  refine Matrix.inv_eq_left_inv ?_
  rw [dy_gk, Matrix.diagonal_mul_diagonal, ← Matrix.diagonal_one]
  congr 1; ext i; fin_cases i <;> simp [hB, hC]

lemma dy_Γk (y : Fin 4 → ℝ) (hC : dy_C y ≠ 0) (a b c : Fin 4) : kr_Γ dy_gk y a b c = dy_Tk y a b c := by
  have hB := (dy_B_pos y).ne'
  simp only [kr_Γ, dy_gk_inv y hC]
  fin_cases a <;> fin_cases b <;> fin_cases c <;>
    simp [Fin.sum_univ_four, dy_gk, dy_Tk, dy_B_pd, dy_C_pd, kr_pd_const, dy_k1, dy_k2, dy_k3, dy_k4, dy_k5, dy_k6,
      dy_k7, dy_k8] <;> field_simp <;> ring


/-! ### The Riemann table at the origin -/

lemma dy_C_cont : Continuous dy_C := by unfold dy_C dy_Cf; fun_prop

lemma dy_k1_pd (c : Fin 4) : kr_pd dy_k1 0 c = ![5, 0, 0, 0] c := by
  fin_cases c
  · exact dy_pd_of (fun s => 1 + 5 * s + 0 * s ^ 2) (fun s => by simp [dy_k1]) (by simpa using dy_quad 1 5 0 0)
  · exact dy_pd_of (fun _ => 1) (fun s => by simp [dy_k1]) (hasDerivAt_const _ _)
  · show kr_pd dy_k1 0 2 = 0; exact (dy_pd23 (fun t _ => 1 + 5 * t) 0).1
  · show kr_pd dy_k1 0 3 = 0; exact (dy_pd23 (fun t _ => 1 + 5 * t) 0).2
lemma dy_k2_pd (c : Fin 4) : kr_pd dy_k2 0 c = ![-1, 0, 0, 0] c := by
  fin_cases c
  · exact dy_pd_of (fun s => 0 + (-1) * s + 0 * s ^ 2) (fun s => by simp [dy_k2]) (by simpa using dy_quad 0 (-1) 0 0)
  · exact dy_pd_of (fun _ => 0) (fun s => by simp [dy_k2]) (hasDerivAt_const _ _)
  · show kr_pd dy_k2 0 2 = 0; exact (dy_pd23 (fun t _ => -t) 0).1
  · show kr_pd dy_k2 0 3 = 0; exact (dy_pd23 (fun t _ => -t) 0).2
lemma dy_k3_pd (c : Fin 4) : kr_pd dy_k3 0 c = ![0, -1, 0, 0] c := by
  fin_cases c
  · exact dy_pd_of (fun _ => 0) (fun s => by simp [dy_k3]) (hasDerivAt_const _ _)
  · exact dy_pd_of (fun s => 0 + (-1) * s + 0 * s ^ 2) (fun s => by simp [dy_k3]) (by simpa using dy_quad 0 (-1) 0 0)
  · show kr_pd dy_k3 0 2 = 0; exact (dy_pd23 (fun _ z => -z) 0).1
  · show kr_pd dy_k3 0 3 = 0; exact (dy_pd23 (fun _ z => -z) 0).2
lemma dy_k4_pd (c : Fin 4) : kr_pd dy_k4 0 c = ![0, 3, 0, 0] c := by
  fin_cases c
  · exact dy_pd_of (fun _ => (-1)) (fun s => by simp [dy_k4]) (hasDerivAt_const _ _)
  · exact dy_pd_of (fun s => (-1) + 3 * s + 0 * s ^ 2) (fun s => by simp [dy_k4]; ring) (by simpa using dy_quad (-1) 3 0 0)
  · show kr_pd dy_k4 0 2 = 0; exact (dy_pd23 (fun _ z => 3 * z - 1) 0).1
  · show kr_pd dy_k4 0 3 = 0; exact (dy_pd23 (fun _ z => 3 * z - 1) 0).2
lemma dy_k5_pd (c : Fin 4) : kr_pd dy_k5 0 c = ![3, 0, 0, 0] c := by
  fin_cases c
  · exact dy_pd_of (fun s => (1 + 5 * s) / (1 + 2 * s + 5 * s ^ 2))
      (fun s => by simp [dy_k5, dy_B, dy_Bf]) (by have h := dy_rat0 1 5 1 2 5 one_ne_zero; norm_num at h ⊢; exact h)
  · exact dy_pd_of (fun s => (1 + 0 * s) / (1 + 0 * s + 1 * s ^ 2))
      (fun s => by simp [dy_k5, dy_B, dy_Bf]) (by have h := dy_rat0 1 0 1 0 1 one_ne_zero; norm_num at h ⊢; exact h)
  · show kr_pd dy_k5 0 2 = 0; exact (dy_pd23 (fun t z => (1 + 5 * t) / dy_Bf t z) 0).1
  · show kr_pd dy_k5 0 3 = 0; exact (dy_pd23 (fun t z => (1 + 5 * t) / dy_Bf t z) 0).2
lemma dy_k6_pd (c : Fin 4) : kr_pd dy_k6 0 c = ![0, 1, 0, 0] c := by
  fin_cases c
  · exact dy_pd_of (fun s => (0 + 0 * s) / (1 + 2 * s + 5 * s ^ 2))
      (fun s => by simp [dy_k6, dy_B, dy_Bf]) (by have h := dy_rat0 0 0 1 2 5 one_ne_zero; norm_num at h ⊢; exact h)
  · exact dy_pd_of (fun s => (0 + 1 * s) / (1 + 0 * s + 1 * s ^ 2))
      (fun s => by simp [dy_k6, dy_B, dy_Bf]) (by have h := dy_rat0 0 1 1 0 1 one_ne_zero; norm_num at h ⊢; exact h)
  · show kr_pd dy_k6 0 2 = 0; exact (dy_pd23 (fun t z => z / dy_Bf t z) 0).1
  · show kr_pd dy_k6 0 3 = 0; exact (dy_pd23 (fun t z => z / dy_Bf t z) 0).2
lemma dy_k7_pd (c : Fin 4) : kr_pd dy_k7 0 c = ![-1, 0, 0, 0] c := by
  fin_cases c
  · exact dy_pd_of (fun s => (0 + (-1) * s) / (1 + 0 * s + (-1) * s ^ 2))
      (fun s => by simp [dy_k7, dy_C, dy_Cf]; ring) (by simpa using dy_rat0 0 (-1) 1 0 (-1) one_ne_zero)
  · exact dy_pd_of (fun s => (0 + 0 * s) / (1 + 2 * s + (-3) * s ^ 2))
      (fun s => by simp [dy_k7, dy_C, dy_Cf]) (by simpa using dy_rat0 0 0 1 2 (-3) one_ne_zero)
  · show kr_pd dy_k7 0 2 = 0; exact (dy_pd23 (fun t z => -t / dy_Cf t z) 0).1
  · show kr_pd dy_k7 0 3 = 0; exact (dy_pd23 (fun t z => -t / dy_Cf t z) 0).2
lemma dy_k8_pd (c : Fin 4) : kr_pd dy_k8 0 c = ![0, -5, 0, 0] c := by
  fin_cases c
  · exact dy_pd_of (fun s => (1 + 0 * s) / (1 + 0 * s + (-1) * s ^ 2))
      (fun s => by simp [dy_k8, dy_C, dy_Cf]; ring) (by simpa using dy_rat0 1 0 1 0 (-1) one_ne_zero)
  · exact dy_pd_of (fun s => (1 + (-3) * s) / (1 + 2 * s + (-3) * s ^ 2))
      (fun s => by simp [dy_k8, dy_C, dy_Cf]; ring) (by have h := dy_rat0 1 (-3) 1 2 (-3) one_ne_zero; norm_num at h ⊢; exact h)
  · show kr_pd dy_k8 0 2 = 0; exact (dy_pd23 (fun t z => (1 - 3 * z) / dy_Cf t z) 0).1
  · show kr_pd dy_k8 0 3 = 0; exact (dy_pd23 (fun t z => (1 - 3 * z) / dy_Cf t z) 0).2


/-- The sectional values `R^a{}_{bab}` at the origin. -/
def dy_V : Matrix (Fin 4) (Fin 4) ℝ := !![0, 0, 4, -1; 0, 0, -1, 4; -4, -1, 0, 0; 1, 4, 0, 0]

/-- The Riemann table at the origin: `R^a{}_{bcd} = V_ab(δ_ac δ_bd − δ_ad δ_bc)` for `a ≠ b`, zero otherwise. -/
def dy_RT (a b c d : Fin 4) : ℝ :=
  if c = a ∧ d = b ∧ a ≠ b then dy_V a b else if c = b ∧ d = a ∧ a ≠ b then -dy_V a b else 0

set_option maxHeartbeats 0 in
/-- **Row K4a.** The full Riemann tensor of `diag(−1, 1, B, C)` at the origin. -/
lemma dy_Riem0 (a b c d : Fin 4) : kr_Riem dy_gk 0 a b c d = dy_RT a b c d := by
  have hev : ∀ᶠ y in 𝓝 (0 : Fin 4 → ℝ), dy_C y ≠ 0 :=
    dy_C_cont.continuousAt.eventually_ne (by simp [dy_C, dy_Cf])
  have hpd : ∀ a b c d, kr_pd (fun y => kr_Γ dy_gk y a b c) 0 d = kr_pd (fun y => dy_Tk y a b c) 0 d :=
    fun a b c d => kr_pd_congr (hev.mono fun y hy => dy_Γk y hy a b c)
  have h0 : ∀ a b c, kr_Γ dy_gk 0 a b c = dy_Tk 0 a b c := dy_Γk 0 (by simp [dy_C, dy_Cf])
  unfold kr_Riem
  simp only [hpd, h0]
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases d <;>
    simp [dy_Tk, Fin.sum_univ_four, dy_k1_pd, dy_k2_pd, dy_k3_pd, dy_k4_pd, dy_k5_pd, dy_k6_pd, dy_k7_pd,
      dy_k8_pd, kr_pd_const] <;>
    simp [dy_RT, dy_V, dy_k1, dy_k2, dy_k3, dy_k4, dy_k5, dy_k6, dy_k7, dy_k8, dy_B, dy_Bf, dy_C, dy_Cf] <;>
    norm_num


lemma dy_g0 : dy_gk 0 = Matrix.diagonal ![-1, 1, 1, 1] := by
  unfold dy_gk; congr 1; ext i; fin_cases i <;> simp [dy_B, dy_Bf, dy_C, dy_Cf]

lemma dy_g0_inv : (Matrix.diagonal ![(-1 : ℝ), 1, 1, 1])⁻¹ = Matrix.diagonal ![-1, 1, 1, 1] := by
  refine Matrix.inv_eq_left_inv ?_
  rw [Matrix.diagonal_mul_diagonal, ← Matrix.diagonal_one]; congr 1; ext i; fin_cases i <;> simp

/-- **Row K4a.** At the origin the Einstein–Λ equations hold with `Λ = 3`: `R_ab = 3g_ab`, and `R = 12`. -/
theorem dy_vacuum0 : (∀ b d, rn_Ric dy_gk 0 b d = 3 * dy_gk 0 b d) ∧ rn_scal dy_gk 0 = 12 := by
  have hR : ∀ b d, rn_Ric dy_gk 0 b d = 3 * dy_gk 0 b d := by
    intro b d
    rw [dy_g0]
    fin_cases b <;> fin_cases d <;> simp [rn_Ric, dy_Riem0, Fin.sum_univ_four, dy_RT, dy_V] <;> norm_num
  refine ⟨hR, ?_⟩
  simp only [rn_scal, hR, dy_g0, dy_g0_inv]
  simp [Fin.sum_univ_four, Matrix.diagonal_apply]
  norm_num

/-- The Weyl pair table at the origin. -/
def dy_U : Matrix (Fin 4) (Fin 4) ℝ := !![0, -1, 3, -2; -1, 0, -2, 3; 3, -2, 0, -1; -2, 3, -1, 0]

set_option maxHeartbeats 0 in
set_option linter.unusedSimpArgs false in
/-- **Row K4b.** At the origin the Weyl bivector operator is `ij_tbl U`. -/
lemma dy_W0 : ij_W dy_gk 0 = ij_tbl dy_U := by
  obtain ⟨hR, hS⟩ := dy_vacuum0
  have hC : ∀ a b c d, rn_Weyl dy_gk 0 a b c d =
      kr_Rlow dy_gk 0 a b c d - (dy_gk 0 a c * dy_gk 0 b d - dy_gk 0 a d * dy_gk 0 b c) := by
    intro a b c d; simp only [rn_Weyl, hR, hS]; ring
  have hRl : ∀ a b c d, kr_Rlow dy_gk 0 a b c d = dy_gk 0 a a * dy_RT a b c d := by
    intro a b c d
    simp only [kr_Rlow, dy_Riem0, dy_g0]
    fin_cases a <;> simp [Fin.sum_univ_four, Matrix.diagonal_apply]
  ext ⟨a, b⟩ ⟨c, d⟩
  simp only [ij_W, ij_tbl, Matrix.of_apply, pw_W, dy_g0_inv, hC, hRl, dy_g0]
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases d <;>
    simp [Fin.sum_univ_four, Matrix.diagonal_apply, dy_RT, dy_V, dy_U] <;> norm_num

/-- **Row K4.** The Gowdy–de Sitter-form metric `diag(−1, 1, B, C)` (`B = 1 + 2t + 5t² + z²`,
`C = 1 + 2z − t² − 3z²`) is, at the origin, a vacuum-Λ point (`R_ab = 3g_ab`), depends on `z` (`∂_z C = 2`), and has
Weyl invariants `I = 7`, `J = 3`, so `I³ = 343 ≠ 243 = 27J²`: **Petrov type I**. -/
theorem dy_typeI :
    (∀ b d, rn_Ric dy_gk 0 b d = 3 * dy_gk 0 b d) ∧ kr_pd dy_C 0 1 = 2 ∧
      ij_I dy_gk 0 = 7 ∧ ij_J dy_gk 0 = 3 ∧ ij_I dy_gk 0 ^ 3 ≠ 27 * ij_J dy_gk 0 ^ 2 := by
  have hW := dy_W0
  have hE : ∀ q r : Fin 4 × Fin 4, (r = q ∨ r = q.swap) → ij_E dy_gk 0 q r = 0 := by
    rintro ⟨q1, q2⟩ r hr
    rcases hr with rfl | rfl <;> fin_cases q1 <;> fin_cases q2 <;>
      simp [ij_E, dy_g0, dy_g0_inv, Matrix.diagonal_apply, ij_lc]
  have bW := ij_tbl_blk dy_U
  have hK2 : (ij_W dy_gk 0 * (ij_E dy_gk 0 * ij_W dy_gk 0)).trace = 0 := by
    rw [hW]; exact ij_tr_dual bW bW hE
  have hK4 : (ij_W dy_gk 0 * ij_W dy_gk 0 * (ij_E dy_gk 0 * ij_W dy_gk 0)).trace = 0 := by
    rw [hW]; exact ij_tr_dual (ij_blk_mul bW bW) bW hE
  have hI : ij_I dy_gk 0 = 7 := by
    apply Complex.ext
    · simp only [ij_I, hW, ij_tr2]; simp [Fin.sum_univ_four, dy_U]; norm_num
    · simp [ij_I, hK2]
  have hJ : ij_J dy_gk 0 = 3 := by
    apply Complex.ext
    · simp only [ij_J, hW, ij_tr3]; simp [Fin.sum_univ_four, dy_U]; norm_num
    · simp [ij_J, hK4]
  refine ⟨dy_vacuum0.1, by simpa using dy_C_pd1 0, hI, hJ, ?_⟩
  rw [hI, hJ]; norm_num

end ShadowProbe.DynamicsProbe

#print axioms ShadowProbe.RangeProbe.rn_pp_vacuum_iff
#print axioms ShadowProbe.RangeProbe.pw_nilpotent
#print axioms ShadowProbe.RangeProbe.pw_IJ
#print axioms ShadowProbe.RangeProbe.pw_witness
#print axioms ShadowProbe.DynamicsProbe.dy_wall_det
#print axioms ShadowProbe.DynamicsProbe.dy_wall_vacuum
#print axioms ShadowProbe.DynamicsProbe.dy_wall_regular
#print axioms ShadowProbe.DynamicsProbe.dy_wall_typeN
#print axioms ShadowProbe.DynamicsProbe.dy_killing_xy
#print axioms ShadowProbe.DynamicsProbe.dy_not_killing
#print axioms ShadowProbe.DynamicsProbe.dy_desitter
#print axioms ShadowProbe.DynamicsProbe.dy_shear
#print axioms ShadowProbe.DynamicsProbe.dy_W1_mukhanov
#print axioms ShadowProbe.DynamicsProbe.dy_W2_mukhanov
#print axioms ShadowProbe.DynamicsProbe.dy_Q_bounded
#print axioms ShadowProbe.DynamicsProbe.dy_witness
#print axioms ShadowProbe.DynamicsProbe.dy_gk_form
#print axioms ShadowProbe.DynamicsProbe.dy_Γk
#print axioms ShadowProbe.DynamicsProbe.dy_Riem0
#print axioms ShadowProbe.DynamicsProbe.dy_vacuum0
#print axioms ShadowProbe.DynamicsProbe.dy_W0
#print axioms ShadowProbe.DynamicsProbe.dy_typeI

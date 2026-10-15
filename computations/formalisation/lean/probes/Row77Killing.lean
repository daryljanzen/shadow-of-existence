import ShadowEngine

/-! # Campaign 19 (`r7371+71.9`): row 77's half, the receipt's three failing candidates under THE connection

`P11_dynamics_paper/P11_twoKV.py`: "exactly two" is computed as three failures. `∂_z` and `∂_t` fail where
`ψ_z`, `ψ_t ≠ 0`; the `x ↔ y` rotation fails where `g_xx ≠ g_yy`. That `∂_x`, `∂_y` ARE Killing is `gowdy_killing`
(engine, `r7297` C5).
- `killF_model`: for ANY differentiable field `ξ` and any diagonal metric on `ℝ⁴`, THE connection's Killing form is
  `g(Dξ·u + Γ(u, ξ), v) + g(u, Dξ·v + Γ(v, ξ))` (the engine's `cov_model`, `lcConn_const`, `lcGam_diag4`);
- `killF_coord`, `coord_not_killing`, `gowdy_coord_not_killing`: `∂_k`'s Killing form on `(∂ᵢ, ∂ᵢ)` is `∂_k cᵢ`,
  so with `g_xx = e^{2ψ}`, `∂_k` fails wherever `∂_kψ ≠ 0`;
- `rot_killF`, `gowdy_rot_not_killing`: the rotation's Killing form on `(∂_x, ∂_y)` is `c_y − c_x`, so for the
  Gowdy family it fails wherever `g_xx ≠ g_yy`.

Not claimed: that NO third Killing field exists, of any form. The receipt does not compute that either. -/

open Bundle Manifold Filter Set VectorField
open scoped ContDiff Manifold

namespace ShadowProbe

section Row77Killing

variable {c : Fin 4 → (Fin 4 → ℝ) → ℝ} (hc : ∀ i p, c i p ≠ 0) (hcs : ∀ i, ContDiff ℝ ∞ (c i))

/-- THE Levi-Civita connection of `Σ cᵢ dxᵢ²` on `ℝ⁴`. -/
noncomputable abbrev gw (hc : ∀ i p, c i p ≠ 0) (hcs : ∀ i, ContDiff ℝ ∞ (c i)) :=
  ndOf (diag4 c) (diag4_symm c) (fun p u h => diag4_nondeg (fun i => hc i p) u h)
    ((diag4_smooth hcs).differentiable (by simp))

/-- The Killing form `g(∇_uξ, v) + g(u, ∇_vξ)` of a field `ξ` under THE connection. -/
noncomputable def killF (ξ : (Fin 4 → ℝ) → (Fin 4 → ℝ)) (p u v : Fin 4 → ℝ) : ℝ :=
  diag4 c p (lcConn (Fin 4 → ℝ) (gw hc hcs) (fun y => ξ y) p u) v
    + diag4 c p u (lcConn (Fin 4 → ℝ) (gw hc hcs) (fun y => ξ y) p v)

include hc hcs in
/-- (a) **The Killing form, in closed form:** `∇_wξ = Dξ·w + Γ(w, ξ)` with `Γ = gamD`. -/
theorem killF_model {ξ : (Fin 4 → ℝ) → (Fin 4 → ℝ)} {p : Fin 4 → ℝ} (hξ : DifferentiableAt ℝ ξ p) (u v : Fin 4 → ℝ) :
    killF hc hcs ξ p u v = diag4 c p (fderiv ℝ ξ p u + gamD c p u (ξ p)) v
      + diag4 c p u (fderiv ℝ ξ p v + gamD c p v (ξ p)) := by
  have hG : ∀ x w b, lcConn (Fin 4 → ℝ) (gw hc hcs) (fun _ => b) x w = lcGam (diag4 c) x w b :=
    fun x w b => lcConn_const _ _ _ x w b
  let σ : Π x : Fin 4 → ℝ, TangentSpace 𝓘(ℝ, Fin 4 → ℝ) x := fun y => ξ y
  have hσ := (mdiffAt_model (σ := σ) (x := p)).2 hξ
  have hm := fun w => cov_model (lcConn (Fin 4 → ℝ) (gw hc hcs)) (lcGam (diag4 c)) hG hσ w
  have e : ∀ w : Fin 4 → ℝ, lcConn (Fin 4 → ℝ) (gw hc hcs) (fun y => ξ y) p w
      = fderiv ℝ ξ p w + gamD c p w (ξ p) := fun w => by
    rw [← lcGam_diag4 hc hcs]; exact hm w
  simp only [killF, e]

include hc hcs in
/-- (b) **The coordinate candidates.** For the constant field `∂_k`, the Killing form on `(∂ᵢ, ∂ᵢ)` is `∂_k cᵢ`. -/
theorem killF_coord (k i : Fin 4) (p : Fin 4 → ℝ) :
    killF hc hcs (fun _ => Pi.single k 1) p (Pi.single i 1) (Pi.single i 1) = fderiv ℝ (c i) p (Pi.single k 1) := by
  rw [killF_model hc hcs (differentiableAt_const _)]
  have h0 := hc 0 p; have h1 := hc 1 p; have h2 := hc 2 p; have h3 := hc 3 p
  simp only [diag4_apply]
  fin_cases i <;> fin_cases k <;> simp [gamD, Fin.sum_univ_four] <;> field_simp <;> ring

include hc hcs in
/-- `∂_k` is not Killing at `p` wherever some `∂_k cᵢ(p) ≠ 0`. -/
theorem coord_not_killing (k i : Fin 4) (p : Fin 4 → ℝ) (h : fderiv ℝ (c i) p (Pi.single k 1) ≠ 0) :
    ¬ ∀ u v, killF hc hcs (fun _ => Pi.single k 1) p u v = 0 :=
  fun hK => h (by rw [← killF_coord hc hcs k i p]; exact hK _ _)

include hc hcs in
/-- **Gowdy's `∂_z` and `∂_t`.** With `g_xx = e^{2ψ}`, `∂_k` (`k = z` or `t`) fails the Killing equation at every
point where `∂_kψ ≠ 0`. -/
theorem gowdy_coord_not_killing {ψ : (Fin 4 → ℝ) → ℝ} (hc2 : c 2 = fun q => Real.exp (2 * ψ q)) (k : Fin 4)
    {p : Fin 4 → ℝ} (hψ : DifferentiableAt ℝ ψ p) (hψk : fderiv ℝ ψ p (Pi.single k 1) ≠ 0) :
    ¬ ∀ u v, killF hc hcs (fun _ => Pi.single k 1) p u v = 0 := by
  refine coord_not_killing hc hcs k 2 p ?_
  rw [hc2, ((hψ.hasFDerivAt.const_mul 2).exp).fderiv]
  simp only [ContinuousLinearMap.smul_apply, smul_eq_mul]
  exact mul_ne_zero (Real.exp_pos _).ne' (mul_ne_zero two_ne_zero hψk)

/-- The `x ↔ y` rotation, `ξ = −y ∂_x + x ∂_y` (coordinates `(t, z, x, y) = (0, 1, 2, 3)`). -/
noncomputable def rotXY (y : Fin 4 → ℝ) : Fin 4 → ℝ := (-y 3) • Pi.single 2 1 + y 2 • Pi.single 3 1

lemma rotXY_hasFDerivAt (p : Fin 4 → ℝ) : HasFDerivAt rotXY
    ((-ContinuousLinearMap.proj (R := ℝ) (φ := fun _ : Fin 4 => ℝ) 3).smulRight (Pi.single 2 1 : Fin 4 → ℝ)
      + (ContinuousLinearMap.proj (R := ℝ) (φ := fun _ : Fin 4 => ℝ) 2).smulRight (Pi.single 3 1 : Fin 4 → ℝ)) p :=
  ((hasFDerivAt_apply 3 p).neg.smul_const _).add ((hasFDerivAt_apply 2 p).smul_const _)

include hc hcs in
/-- (c) **The rotation.** If the coefficients do not depend on `x, y` at `p`, the rotation's Killing form on
`(∂_x, ∂_y)` is `c_y − c_x`: the rotation is Killing at `p` only if `g_xx(p) = g_yy(p)`. -/
theorem rot_killF (p : Fin 4 → ℝ) (hxy : ∀ i, fderiv ℝ (c i) p (Pi.single 2 1) = 0 ∧ fderiv ℝ (c i) p (Pi.single 3 1) = 0) :
    killF hc hcs rotXY p (Pi.single 2 1) (Pi.single 3 1) = c 3 p - c 2 p := by
  rw [killF_model hc hcs (rotXY_hasFDerivAt p).differentiableAt, (rotXY_hasFDerivAt p).fderiv]
  have h2 := hc 2 p; have h3 := hc 3 p
  simp [diag4_apply, gamD, rotXY, Fin.sum_univ_four, (hxy _).1, (hxy _).2]
  ring

include hc hcs in
/-- For the Gowdy family, coefficients depending on `(t, z)` only, the rotation is Killing at `p` only if
`g_xx(p) = g_yy(p)`. -/
theorem gowdy_rot_not_killing (hdep : ∀ i (p q : Fin 4 → ℝ), p 0 = q 0 → p 1 = q 1 → c i p = c i q)
    (p : Fin 4 → ℝ) (hne : c 2 p ≠ c 3 p) : ¬ ∀ u v, killF hc hcs rotXY p u v = 0 := by
  have hz : ∀ i (k : Fin 4), k ≠ 0 → k ≠ 1 → fderiv ℝ (c i) p (Pi.single k 1) = 0 := fun i k h0 h1 => by
    have hl : HasDerivAt (fun s : ℝ => p + s • (Pi.single k 1 : Fin 4 → ℝ)) (Pi.single k 1) 0 := by
      simpa using ((hasDerivAt_id (0 : ℝ)).smul_const (Pi.single k 1 : Fin 4 → ℝ)).const_add p
    have h1' := HasFDerivAt.comp_hasDerivAt_of_eq (x := (0 : ℝ))
      (((hcs i).differentiable (by simp)) p).hasFDerivAt hl (by simp)
    have h2' : HasDerivAt (c i ∘ fun s : ℝ => p + s • (Pi.single k 1 : Fin 4 → ℝ)) 0 0 := by
      have : (c i ∘ fun s : ℝ => p + s • (Pi.single k 1 : Fin 4 → ℝ)) = fun _ => c i p := funext fun s =>
        hdep i _ _ (by simp [Ne.symm h0]) (by simp [Ne.symm h1])
      rw [this]; exact hasDerivAt_const _ _
    exact h1'.unique h2'
  intro hK
  have := rot_killF hc hcs p fun i => ⟨hz i 2 (by decide) (by decide), hz i 3 (by decide) (by decide)⟩
  rw [hK] at this
  exact hne (by linarith)

end Row77Killing

end ShadowProbe

#print axioms ShadowProbe.killF_model
#print axioms ShadowProbe.killF_coord
#print axioms ShadowProbe.coord_not_killing
#print axioms ShadowProbe.gowdy_coord_not_killing
#print axioms ShadowProbe.rot_killF
#print axioms ShadowProbe.gowdy_rot_not_killing

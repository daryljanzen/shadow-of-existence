import ShadowEngine

/-! # The second seat's closed-FRW row (`r7335+70`): 72

`−dT² + a(T)²(dχ² + sin²χ dθ² + sin²χ sin²θ dφ²)` in `(T, χ, θ, φ)` with `a` free, smooth and nowhere zero, and the
angular profiles `S₁ = sin²χ`, `S₂ = sin²θ` near the point (the convention, `exists_global_family`). `g_φφ` is a
product of THREE one-coordinate profiles, so this file adds the three-factor recipe from `d2_of`. -/

open Bundle Manifold Filter Set VectorField
open scoped ContDiff Manifold

namespace ShadowProbe

/-! ### `r7335` instance, row 72: `R = 6(aä + ȧ² + 1)/a²`, `Weyl² = 0` for every `a`, and Gauss–Bonnet as an exact
total derivative, `a³·GB = 24 d/dT(ȧ³/3 + ȧ) = 24ä(ȧ² + 1)` -/

section Inst_R72

set_option synthInstance.maxHeartbeats 400000

variable {k m n : ℝ → ℝ} (hk : ContDiff ℝ ∞ k) (hm : ContDiff ℝ ∞ m) (hn : ContDiff ℝ ∞ n)

include hk hm hn in
lemma pr3_d1 (i j l : Fin 4) (y v : Fin 4 → ℝ) :
    fderiv ℝ (fun y : Fin 4 → ℝ => k (y i) * m (y j) * n (y l)) y v
      = deriv k (y i) * v i * m (y j) * n (y l) + k (y i) * (deriv m (y j) * v j) * n (y l)
        + k (y i) * m (y j) * (deriv n (y l) * v l) := by
  have H : HasFDerivAt (fun y : Fin 4 → ℝ => k (y i) * m (y j) * n (y l)) _ y :=
    ((fd_coord_i i ((hk.differentiable (by simp)) _)).mul (fd_coord_i j ((hm.differentiable (by simp)) _))).mul
      (fd_coord_i l ((hn.differentiable (by simp)) _))
  rw [H.fderiv]; simp; ring

include hk hm hn in
lemma pr3_d2 (i j l : Fin 4) (p u v : Fin 4 → ℝ) :
    fderiv ℝ (fderiv ℝ (fun y : Fin 4 → ℝ => k (y i) * m (y j) * n (y l))) p u v
      = deriv (deriv k) (p i) * u i * v i * m (p j) * n (p l)
        + deriv k (p i) * v i * (deriv m (p j) * u j) * n (p l)
        + deriv k (p i) * v i * m (p j) * (deriv n (p l) * u l)
        + deriv k (p i) * u i * (deriv m (p j) * v j) * n (p l)
        + k (p i) * (deriv (deriv m) (p j) * u j * v j) * n (p l)
        + k (p i) * (deriv m (p j) * v j) * (deriv n (p l) * u l)
        + deriv k (p i) * u i * m (p j) * (deriv n (p l) * v l)
        + k (p i) * (deriv m (p j) * u j) * (deriv n (p l) * v l)
        + k (p i) * m (p j) * (deriv (deriv n) (p l) * u l * v l) := by
  have D := fun {f : ℝ → ℝ} (hf : ContDiff ℝ ∞ f) (q : Fin 4) =>
    fd_coord_i (x := p) q ((hf.differentiable (by simp)) (p q))
  have D' := fun {f : ℝ → ℝ} (hf : ContDiff ℝ ∞ f) (q : Fin 4) =>
    fd_coord_i (x := p) q (((contDiff_infty_iff_deriv.1 hf).2.differentiable (by simp)) (p q))
  rw [d2_of (F := fun y : Fin 4 → ℝ => k (y i) * m (y j) * n (y l))
    (((hk.comp (contDiff_apply ℝ ℝ i)).mul (hm.comp (contDiff_apply ℝ ℝ j))).mul (hn.comp (contDiff_apply ℝ ℝ l)))
    (fun y => pr3_d1 hk hm hn i j l y v)
    (((((D' hk i).mul_const (v i)).mul (D hm j)).mul (D hn l)).add
      (((D hk i).mul ((D' hm j).mul_const (v j))).mul (D hn l)) |>.add
      (((D hk i).mul (D hm j)).mul ((D' hn l).mul_const (v l))))]
  simp; ring

/-- The closed-FRW Riemann table `R(eᵢ,eⱼ)eₖ` component `l`: `K(g_jk δ_il − g_ik δ_jl)`, with `K = ä/a` when one
of `i, j` is time and `K = (1 + ȧ²)/a²` when both are spatial. -/
noncomputable def fR (A A1 A2 s1 s2 : ℝ) (i j k l : Fin 4) : ℝ :=
  let g : Fin 4 → ℝ := ![-1, A ^ 2, A ^ 2 * s1, A ^ 2 * s1 * s2]
  let K : ℝ := if i = 0 ∨ j = 0 then A2 / A else (1 + A1 ^ 2) / A ^ 2
  K * ((if j = k ∧ i = l then g j else 0) - (if i = k ∧ j = l then g i else 0))

noncomputable def cF (a S₁ S₂ : ℝ → ℝ) : Fin 4 → (Fin 4 → ℝ) → ℝ :=
  ![fun _ => -1, fun y => a (y 0) ^ 2, fun y => a (y 0) ^ 2 * S₁ (y 1), fun y => a (y 0) ^ 2 * S₁ (y 1) * S₂ (y 2)]

omit hk hm hn in
lemma cF_smooth {a S₁ S₂ : ℝ → ℝ} (ha : ContDiff ℝ ∞ a) (h1 : ContDiff ℝ ∞ S₁) (h2 : ContDiff ℝ ∞ S₂)
    (j : Fin 4) : ContDiff ℝ ∞ (cF a S₁ S₂ j) := by
  fin_cases j
  · exact contDiff_const
  · exact (ha.comp (contDiff_apply ℝ ℝ 0)).pow 2
  · exact ((ha.comp (contDiff_apply ℝ ℝ 0)).pow 2).mul (h1.comp (contDiff_apply ℝ ℝ 1))
  · exact (((ha.comp (contDiff_apply ℝ ℝ 0)).pow 2).mul (h1.comp (contDiff_apply ℝ ℝ 1))).mul
      (h2.comp (contDiff_apply ℝ ℝ 2))
omit hk hm hn in
lemma cF_ne {a S₁ S₂ : ℝ → ℝ} (ha0 : ∀ s, a s ≠ 0) (h10 : ∀ s, S₁ s ≠ 0) (h20 : ∀ s, S₂ s ≠ 0)
    (j : Fin 4) (p : Fin 4 → ℝ) : cF a S₁ S₂ j p ≠ 0 := by
  fin_cases j <;> simp [cF, ha0, h10, h20]

omit hk hm hn in
open Filter Topology in
lemma sin2_at {S : ℝ → ℝ} (θ : ℝ) (eS : S =ᶠ[𝓝 θ] fun s => Real.sin s ^ 2) :
    S θ = Real.sin θ ^ 2 ∧ deriv S θ = 2 * Real.sin θ * Real.cos θ
      ∧ deriv (deriv S) θ = 2 * Real.cos θ ^ 2 - 2 * Real.sin θ ^ 2 := by
  have sd : ∀ s, HasDerivAt (fun s => Real.sin s ^ 2) (2 * Real.sin s * Real.cos s) s := fun s =>
    (show HasDerivAt (fun s => Real.sin s ^ 2) _ s from (Real.hasDerivAt_sin s).pow 2).congr_deriv (by norm_num)
  have e3 : deriv S =ᶠ[𝓝 θ] fun s => 2 * Real.sin s * Real.cos s :=
    eS.deriv.trans (Eventually.of_forall fun s => (sd s).deriv)
  refine ⟨eS.eq_of_nhds, by rw [eS.deriv_eq, (sd _).deriv], ?_⟩
  rw [e3.deriv_eq]
  have := (show HasDerivAt (fun s => 2 * Real.sin s * Real.cos s) _ θ from
    ((Real.hasDerivAt_sin θ).const_mul 2).mul (Real.hasDerivAt_cos θ))
  rw [this.deriv]; ring

omit hk hm hn in
open Filter Topology in
set_option maxHeartbeats 16000000 in
/-- **Row 72.** -/
theorem frw_closed {a S₁ S₂ : ℝ → ℝ} (ha : ContDiff ℝ ∞ a) (h1 : ContDiff ℝ ∞ S₁) (h2 : ContDiff ℝ ∞ S₂)
    (ha0 : ∀ s, a s ≠ 0) (h10 : ∀ s, S₁ s ≠ 0) (h20 : ∀ s, S₂ s ≠ 0) (p : Fin 4 → ℝ)
    (e1 : S₁ =ᶠ[𝓝 (p 1)] fun s => Real.sin s ^ 2) (e2 : S₂ =ᶠ[𝓝 (p 2)] fun s => Real.sin s ^ 2) :
    let g := fun i => cF a S₁ S₂ i p
    let Rf := fun i j k => curv (lcConn (Fin 4 → ℝ) (ndOf (diag4 (cF a S₁ S₂)) (diag4_symm _)
      (fun p u h => diag4_nondeg (fun i => cF_ne ha0 h10 h20 i p) u h)
      ((diag4_smooth (cF_smooth ha h1 h2)).differentiable (by simp))))
      (fun _ => (Pi.single i 1 : Fin 4 → ℝ)) (fun _ => (Pi.single j 1 : Fin 4 → ℝ))
      (fun _ => (Pi.single k 1 : Fin 4 → ℝ)) p
    let A := a (p 0); let A1 := deriv a (p 0); let A2 := deriv (deriv a) (p 0);
    scalC g Rf = 6 * (A * A2 + A1 ^ 2 + 1) / A ^ 2 ∧ weyl2C g Rf = 0
      ∧ A ^ 3 * gbC g Rf = 24 * A2 * (A1 ^ 2 + 1) := by
  intro g Rf A A1 A2
  have d0 : ∀ s, HasDerivAt a (deriv a s) s := fun s => ((ha.differentiable (by simp)) s).hasDerivAt
  have d1 : ∀ s, HasDerivAt (deriv a) (deriv (deriv a) s) s := fun s =>
    (((contDiff_infty_iff_deriv.1 ha).2.differentiable (by simp)) s).hasDerivAt
  have q1 : deriv (fun s => a s ^ 2) = fun s => 2 * a s * deriv a s :=
    funext fun s => ((d0 s).pow 2).deriv.trans (by simp)
  have q2 : deriv (deriv (fun s => a s ^ 2)) (p 0) = 2 * deriv a (p 0) ^ 2 + 2 * a (p 0) * deriv (deriv a) (p 0) := by
    rw [q1]
    have := (show HasDerivAt (fun s => 2 * a s * deriv a s) _ (p 0) from ((d0 (p 0)).const_mul 2).mul (d1 (p 0)))
    rw [this.deriv]; ring
  have hq : ContDiff ℝ ∞ (fun s => a s ^ 2) := ha.pow 2
  obtain ⟨s1v, s11, s12⟩ := sin2_at (p 1) e1
  obtain ⟨s2v, s21, s22⟩ := sin2_at (p 2) e2
  have hD1 : ∀ j v, fderiv ℝ (cF a S₁ S₂ j) p v = (![0, 2 * a (p 0) * deriv a (p 0) * v 0,
      2 * a (p 0) * deriv a (p 0) * v 0 * S₁ (p 1) + a (p 0) ^ 2 * (deriv S₁ (p 1) * v 1),
      2 * a (p 0) * deriv a (p 0) * v 0 * S₁ (p 1) * S₂ (p 2) + a (p 0) ^ 2 * (deriv S₁ (p 1) * v 1) * S₂ (p 2)
        + a (p 0) ^ 2 * S₁ (p 1) * (deriv S₂ (p 2) * v 2)] : Fin 4 → ℝ) j := fun j v => by
    fin_cases j
    · simp [cF]
    · show fderiv ℝ (fun y => (fun s => a s ^ 2) (y 0)) p v = _
      rw [co_d1 hq]; simp [q1]
    · show fderiv ℝ (fun y => (fun s => a s ^ 2) (y 0) * S₁ (y 1)) p v = _
      rw [pr_d1 hq h1]; simp [q1]
    · show fderiv ℝ (fun y => (fun s => a s ^ 2) (y 0) * S₁ (y 1) * S₂ (y 2)) p v = _
      rw [pr3_d1 hq h1 h2]; simp [q1]
  have hD2 : ∀ j u v, fderiv ℝ (fderiv ℝ (cF a S₁ S₂ j)) p u v = (![0,
      (2 * deriv a (p 0) ^ 2 + 2 * a (p 0) * deriv (deriv a) (p 0)) * u 0 * v 0,
      (2 * deriv a (p 0) ^ 2 + 2 * a (p 0) * deriv (deriv a) (p 0)) * u 0 * v 0 * S₁ (p 1)
        + 2 * a (p 0) * deriv a (p 0) * v 0 * (deriv S₁ (p 1) * u 1)
        + 2 * a (p 0) * deriv a (p 0) * u 0 * (deriv S₁ (p 1) * v 1)
        + a (p 0) ^ 2 * (deriv (deriv S₁) (p 1) * u 1 * v 1),
      (2 * deriv a (p 0) ^ 2 + 2 * a (p 0) * deriv (deriv a) (p 0)) * u 0 * v 0 * S₁ (p 1) * S₂ (p 2)
        + 2 * a (p 0) * deriv a (p 0) * v 0 * (deriv S₁ (p 1) * u 1) * S₂ (p 2)
        + 2 * a (p 0) * deriv a (p 0) * v 0 * S₁ (p 1) * (deriv S₂ (p 2) * u 2)
        + 2 * a (p 0) * deriv a (p 0) * u 0 * (deriv S₁ (p 1) * v 1) * S₂ (p 2)
        + a (p 0) ^ 2 * (deriv (deriv S₁) (p 1) * u 1 * v 1) * S₂ (p 2)
        + a (p 0) ^ 2 * (deriv S₁ (p 1) * v 1) * (deriv S₂ (p 2) * u 2)
        + 2 * a (p 0) * deriv a (p 0) * u 0 * S₁ (p 1) * (deriv S₂ (p 2) * v 2)
        + a (p 0) ^ 2 * (deriv S₁ (p 1) * u 1) * (deriv S₂ (p 2) * v 2)
        + a (p 0) ^ 2 * S₁ (p 1) * (deriv (deriv S₂) (p 2) * u 2 * v 2)] : Fin 4 → ℝ) j := fun j u v => by
    fin_cases j
    · simp [cF]
    · show fderiv ℝ (fderiv ℝ (fun y => (fun s => a s ^ 2) (y 0))) p u v = _
      rw [co_d2 hq]; simp [q2]
    · show fderiv ℝ (fderiv ℝ (fun y => (fun s => a s ^ 2) (y 0) * S₁ (y 1))) p u v = _
      rw [pr_d2 hq h1, q2]; simp [q1]
    · show fderiv ℝ (fderiv ℝ (fun y => (fun s => a s ^ 2) (y 0) * S₁ (y 1) * S₂ (y 2))) p u v = _
      rw [pr3_d2 hq h1 h2, q2]; simp [q1]
  have hA : a (p 0) ≠ 0 := ha0 _
  have hs1 : Real.sin (p 1) ≠ 0 := fun h => h10 (p 1) (by rw [s1v, h]; simp)
  have hs2 : Real.sin (p 2) ≠ 0 := fun h => h20 (p 2) (by rw [s2v, h]; simp)
  have hT : ∀ i j k l, curvD (cF a S₁ S₂) p (Pi.single i 1) (Pi.single j 1) (Pi.single k 1) l
      = fR (a (p 0)) (deriv a (p 0)) (deriv (deriv a) (p 0)) (Real.sin (p 1) ^ 2) (Real.sin (p 2) ^ 2) i j k l := by
    intro i j k l
    fin_cases i <;> fin_cases j <;> fin_cases k <;> fin_cases l <;>
      (simp only [curvD, Pi.sub_apply, Pi.add_apply, DGD, gamD, dC1, dC2, hD1, hD2]
       simp [cF, fR, Fin.sum_univ_four, s1v, s11, s12, s2v, s21, s22]
       try field_simp
       try ring_nf
       try simp only [Real.cos_sq']
       try ring)
  simp only [g, Rf, gbC, weyl2C, riem2C, ric2C, scalC, ricC,
    curvD_eq (cF_ne ha0 h10 h20) (cF_smooth ha h1 h2), hT]
  simp [Fin.sum_univ_four, fR, cF, s1v, s2v, A, A1, A2]
  refine ⟨?_, ?_, ?_⟩ <;> (field_simp; ring)

end Inst_R72

#print axioms frw_closed

end ShadowProbe

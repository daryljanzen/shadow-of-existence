import ShadowEngine

/-! # Campaign 6, stage B (`r7351+71`): the curvature of a NON-diagonal metric

The engine's `lcGam` is metric-agnostic (`♭⁻¹` of the Koszul form). What the diagonal layers add is a closed form
for it. Here the closed form is for any symmetric field of matrices `G i j` on `ℝⁿ`, smooth and nondegenerate,
given the INVERSE only at the point, as numbers `Gi` with `G(p)·Gi = 1`. The derivative of `Γ` at `p` comes from
differentiating `♭(Γ) = K`, so `∂(G⁻¹)` is never needed: `∂_u Γ = Gi·(∂_u K − ∂_u G·Γ)`. -/

open Bundle Manifold Filter Set VectorField
open scoped ContDiff Manifold Topology

namespace ShadowProbe

section EngineG

set_option synthInstance.maxHeartbeats 400000

variable {n : ℕ}

/-- The form `Σᵢⱼ Gᵢⱼ(p) dxᵢ dxⱼ` on `ℝⁿ`. -/
noncomputable def formG (G : Fin n → Fin n → (Fin n → ℝ) → ℝ) (p : Fin n → ℝ) :
    (Fin n → ℝ) →L[ℝ] (Fin n → ℝ) →L[ℝ] ℝ :=
  ∑ i, ∑ j, G i j p • (ContinuousLinearMap.mul ℝ ℝ).bilinearComp (ContinuousLinearMap.proj i)
    (ContinuousLinearMap.proj j)

lemma formG_apply (G : Fin n → Fin n → (Fin n → ℝ) → ℝ) (p u v : Fin n → ℝ) :
    formG G p u v = ∑ i, ∑ j, G i j p * (u i * v j) := by
  simp [formG]

lemma formG_symm {G : Fin n → Fin n → (Fin n → ℝ) → ℝ} (hs : ∀ i j p, G i j p = G j i p) (p u v : Fin n → ℝ) :
    formG G p u v = formG G p v u := by
  rw [formG_apply, formG_apply, Finset.sum_comm]
  exact Finset.sum_congr rfl fun i _ => Finset.sum_congr rfl fun j _ => by rw [hs]; ring

lemma formG_smooth {G : Fin n → Fin n → (Fin n → ℝ) → ℝ} (hGs : ∀ i j, ContDiff ℝ ∞ (G i j)) :
    ContDiff ℝ ∞ (formG G) := by
  rw [contDiff_clm_apply_iff]; intro a; rw [contDiff_clm_apply_iff]; intro b
  simp only [formG_apply]
  exact ContDiff.sum fun i _ => ContDiff.sum fun j _ => (hGs i j).mul contDiff_const

/-- First and second partials of an entry. -/
noncomputable def dG1 (G : Fin n → Fin n → (Fin n → ℝ) → ℝ) (p : Fin n → ℝ) (i j : Fin n) (v : Fin n → ℝ) : ℝ :=
  fderiv ℝ (G i j) p v
noncomputable def dG2 (G : Fin n → Fin n → (Fin n → ℝ) → ℝ) (p : Fin n → ℝ) (i j : Fin n) (u v : Fin n → ℝ) : ℝ :=
  fderiv ℝ (fderiv ℝ (G i j)) p u v

/-- The Koszul covector `K_l(a, b) = ½[∂_a G(b, e_l) + ∂_b G(e_l, a) − ∂_l G(a, b)]`. -/
noncomputable def kosG (G : Fin n → Fin n → (Fin n → ℝ) → ℝ) (p a b : Fin n → ℝ) (l : Fin n) : ℝ :=
  (∑ i, dG1 G p i l a * b i + ∑ j, dG1 G p l j b * a j
    - ∑ i, ∑ j, dG1 G p i j (Pi.single l 1) * (a i * b j)) / 2

/-- Its `∂_u`. -/
noncomputable def DkosG (G : Fin n → Fin n → (Fin n → ℝ) → ℝ) (p u a b : Fin n → ℝ) (l : Fin n) : ℝ :=
  (∑ i, b i * dG2 G p i l u a + ∑ j, a j * dG2 G p l j u b
    - ∑ i, ∑ j, (a i * b j) * dG2 G p i j u (Pi.single l 1)) / 2

/-- The Christoffel form with the inverse at the point given: `Γᵏ(a, b) = Σ_l K_l(a, b) Gi_lk`. -/
noncomputable def gamG (G : Fin n → Fin n → (Fin n → ℝ) → ℝ) (Gi : Fin n → Fin n → ℝ) (p a b : Fin n → ℝ) :
    Fin n → ℝ := fun k => ∑ l, kosG G p a b l * Gi l k

/-- `∂_u Γ = Gi·(∂_u K − ∂_u G·Γ)`. -/
noncomputable def DgamG (G : Fin n → Fin n → (Fin n → ℝ) → ℝ) (Gi : Fin n → Fin n → ℝ) (p u a b : Fin n → ℝ) :
    Fin n → ℝ := fun k =>
  ∑ l, (DkosG G p u a b l - ∑ m, dG1 G p m l u * gamG G Gi p a b m) * Gi l k

/-- **The non-diagonal closed form**: `R(u,v)w = ∂_u Γ(v,w) − ∂_v Γ(u,w) + Γ(u,Γ(v,w)) − Γ(v,Γ(u,w))`. -/
noncomputable def curvG (G : Fin n → Fin n → (Fin n → ℝ) → ℝ) (Gi : Fin n → Fin n → ℝ) (p u v w : Fin n → ℝ) :
    Fin n → ℝ :=
  DgamG G Gi p u v w - DgamG G Gi p v u w + gamG G Gi p u (gamG G Gi p v w) - gamG G Gi p v (gamG G Gi p u w)

/-- The scalar contraction with the inverse metric: `R = Σⱼₖ Gi_jk Ric_jk`. -/
noncomputable def scalG (Gi : Fin n → Fin n → ℝ) (Rf : Fin n → Fin n → Fin n → Fin n → ℝ) : ℝ :=
  ∑ j, ∑ k, Gi j k * ricCN Rf j k

/-- Solving against a right inverse at the point. -/
lemma solve_right {A : Fin n → Fin n → ℝ} {Gi : Fin n → Fin n → ℝ}
    (hinv : ∀ m k, ∑ l, A m l * Gi l k = if m = k then 1 else 0) {w c : Fin n → ℝ}
    (h : ∀ l, ∑ m, w m * A m l = c l) (k : Fin n) : w k = ∑ l, c l * Gi l k := by
  calc w k = ∑ m, w m * (if m = k then 1 else 0) := by simp
    _ = ∑ m, w m * ∑ l, A m l * Gi l k := by simp only [hinv]
    _ = ∑ l, (∑ m, w m * A m l) * Gi l k := by
        simp only [Finset.mul_sum, Finset.sum_mul]; rw [Finset.sum_comm]
        exact Finset.sum_congr rfl fun _ _ => Finset.sum_congr rfl fun _ _ => by ring
    _ = ∑ l, c l * Gi l k := by simp only [h]

lemma kosG_basis (G : Fin n → Fin n → (Fin n → ℝ) → ℝ) (p : Fin n → ℝ) (i j l : Fin n) :
    kosG G p (Pi.single i 1) (Pi.single j 1) l
      = (dG1 G p j l (Pi.single i 1) + dG1 G p l i (Pi.single j 1) - dG1 G p i j (Pi.single l 1)) / 2 := by
  simp [kosG, Pi.single_apply]

lemma DkosG_basis (G : Fin n → Fin n → (Fin n → ℝ) → ℝ) (p u : Fin n → ℝ) (i j l : Fin n) :
    DkosG G p u (Pi.single i 1) (Pi.single j 1) l
      = (dG2 G p j l u (Pi.single i 1) + dG2 G p l i u (Pi.single j 1) - dG2 G p i j u (Pi.single l 1)) / 2 := by
  simp [DkosG, Pi.single_apply]

variable {G : Fin n → Fin n → (Fin n → ℝ) → ℝ} (hs : ∀ i j p, G i j p = G j i p)
  (hn : ∀ p (u : Fin n → ℝ), (∀ v, formG G p u v = 0) → u = 0) (hGs : ∀ i j, ContDiff ℝ ∞ (G i j))
include hn hGs

omit hn in
lemma formG_fderiv (y e a b : Fin n → ℝ) :
    fderiv ℝ (formG G) y e a b = ∑ i, ∑ j, fderiv ℝ (G i j) y e * (a i * b j) := by
  rw [fderiv_apply₂' ((formG_smooth hGs).differentiable (by simp) y),
    show (fun y => formG G y a b) = fun y => ∑ i, ∑ j, G i j y * (a i * b j) from funext fun y => formG_apply G y a b]
  rw [(HasFDerivAt.fun_sum fun i _ => HasFDerivAt.fun_sum fun j _ =>
    (((hGs i j).differentiable (by simp) y).hasFDerivAt.mul_const (a i * b j))).fderiv]
  simp only [ContinuousLinearMap.coe_sum', Finset.sum_apply, ContinuousLinearMap.coe_smul', Pi.smul_apply, smul_eq_mul]
  exact Finset.sum_congr rfl fun _ _ => Finset.sum_congr rfl fun _ _ => by ring

omit hn in
lemma koszK_formG (y a b : Fin n → ℝ) (l : Fin n) :
    koszK (formG G) y a b (Pi.single l 1) = kosG G y a b l := by
  rw [koszK_apply, formG_fderiv hGs, formG_fderiv hGs, formG_fderiv hGs, kosG]
  congr 1
  simp only [dG1, Pi.single_apply, mul_ite, ite_mul, mul_one, one_mul, mul_zero, zero_mul,
    Finset.sum_ite_irrel, Finset.sum_const_zero, Finset.sum_ite_eq', Finset.mem_univ, ite_true]

omit hn hGs in
lemma formG_single (y w : Fin n → ℝ) (l : Fin n) : formG G y w (Pi.single l 1) = ∑ m, w m * G m l y := by
  rw [formG_apply]
  simp only [Pi.single_apply, mul_ite, mul_one, mul_zero, Finset.sum_ite_eq', Finset.mem_univ, ite_true]
  exact Finset.sum_congr rfl fun _ _ => by ring

/-- `♭(Γ) = K` everywhere, componentwise. -/
lemma lcGam_formG_eq (y a b : Fin n → ℝ) (l : Fin n) :
    ∑ m, lcGam (formG G) y a b m * G m l y = kosG G y a b l := by
  have inv := flat_isInvertible (formG G) hn y
  rw [← formG_single, ← koszK_formG hGs, lcGam_apply, inv.self_apply_inverse]

variable {p : Fin n → ℝ} {Gi : Fin n → Fin n → ℝ}
  (hinv : ∀ m k, ∑ l, G m l p * Gi l k = if m = k then 1 else 0)
include hinv

/-- **`lcGam` of any non-diagonal metric is `gamG`**, with the inverse given only at the point. -/
lemma lcGam_formG (a b : Fin n → ℝ) : lcGam (formG G) p a b = gamG G Gi p a b := by
  funext k
  exact solve_right hinv (lcGam_formG_eq hn hGs p a b) k

omit hn hinv in
lemma dG1_hasFDerivAt (i j : Fin n) (v : Fin n → ℝ) :
    HasFDerivAt (fun y => fderiv ℝ (G i j) y v) ((fderiv ℝ (fderiv ℝ (G i j)) p).flip v) p := by
  have h2 := ((hGs i j).fderiv_right (m := ∞) (by simp)).differentiable (by simp) p
  exact (h2.hasFDerivAt.clm_apply (hasFDerivAt_const v p)).congr_fderiv (by ext; simp)

omit hn hinv in
lemma kosG_hasFDerivAt (a b : Fin n → ℝ) (l : Fin n) :
    ∃ L : (Fin n → ℝ) →L[ℝ] ℝ, HasFDerivAt (fun y => kosG G y a b l) L p ∧ ∀ u, L u = DkosG G p u a b l := by
  have h := ((HasFDerivAt.sub (HasFDerivAt.add
    (HasFDerivAt.fun_sum (u := Finset.univ) fun i _ => (dG1_hasFDerivAt (p := p) hGs i l a).mul_const (b i))
    (HasFDerivAt.fun_sum (u := Finset.univ) fun j _ => (dG1_hasFDerivAt (p := p) hGs l j b).mul_const (a j)))
    (HasFDerivAt.fun_sum (u := Finset.univ) fun i _ => HasFDerivAt.fun_sum (u := Finset.univ) fun j _ =>
      (dG1_hasFDerivAt (p := p) hGs i j (Pi.single l 1)).mul_const (a i * b j))).const_mul (1 / 2 : ℝ))
  refine ⟨_, h.congr_of_eventuallyEq (Eventually.of_forall fun y => by
    simp only [kosG, dG1, Pi.add_apply, Pi.sub_apply]; ring), fun u => ?_⟩
  simp only [DkosG, dG2, ContinuousLinearMap.coe_smul', ContinuousLinearMap.coe_sum', Finset.sum_apply,
    ContinuousLinearMap.coe_add', ContinuousLinearMap.coe_sub', Pi.add_apply, Pi.sub_apply, Pi.smul_apply,
    ContinuousLinearMap.flip_apply, smul_eq_mul]
  ring

omit hinv in
lemma lcGam_differentiable : Differentiable ℝ (lcGam (formG G)) :=
  (lcGam_smooth hn (formG_smooth hGs)).differentiable (by simp)

/-- **`∂_u Γ` at the point**, from differentiating `♭(Γ) = K`: no derivative of the inverse is needed. -/
lemma fderiv_lcGam_formG (u a b : Fin n → ℝ) :
    fderiv ℝ (fun y => lcGam (formG G) y a b) p u = DgamG G Gi p u a b := by
  set Γ := fun y => lcGam (formG G) y a b with hΓ
  have hd : DifferentiableAt ℝ Γ p :=
    ((lcGam_differentiable hn hGs p).clm_apply (differentiableAt_const a)).clm_apply (differentiableAt_const b)
  have hc : ∀ m, HasFDerivAt (fun y => Γ y m) ((ContinuousLinearMap.proj m).comp (fderiv ℝ Γ p)) p :=
    fun m => (ContinuousLinearMap.proj (R := ℝ) (φ := fun _ : Fin n => ℝ) m).hasFDerivAt.comp p hd.hasFDerivAt
  funext k
  refine solve_right hinv (fun l => ?_) k
  obtain ⟨L, hL, hLu⟩ := kosG_hasFDerivAt (p := p) hGs a b l
  have hF : HasFDerivAt (fun y => ∑ m, Γ y m * G m l y) _ p :=
    HasFDerivAt.fun_sum fun m _ => (hc m).mul ((hGs m l).differentiable (by simp) p).hasFDerivAt
  have heq : (fun y => ∑ m, Γ y m * G m l y) = fun y => kosG G y a b l :=
    funext fun y => lcGam_formG_eq hn hGs y a b l
  rw [heq] at hF
  have hu := congrArg (fun T => T u) (hF.unique hL)
  simp only [hLu] at hu
  rw [← hu]
  have hΓp : ∀ m, Γ p m = gamG G Gi p a b m := fun m => by rw [hΓ]; simp only [lcGam_formG hn hGs hinv]
  simp only [ContinuousLinearMap.sum_apply, ContinuousLinearMap.add_apply, ContinuousLinearMap.smul_apply,
    ContinuousLinearMap.comp_apply, ContinuousLinearMap.proj_apply, smul_eq_mul, hΓp, dG1]
  rw [Finset.sum_add_distrib,
    Finset.sum_congr rfl fun x _ => mul_comm (gamG G Gi p a b x) (fderiv ℝ (G x l) p u),
    Finset.sum_congr rfl fun x _ => mul_comm (G x l p) (fderiv ℝ Γ p u x)]
  ring

/-- **The non-diagonal engine.** THE connection's curvature of `Σ Gᵢⱼ dxᵢ dxⱼ` on constant fields at `p` is
`curvG`, computed from `G(p)`'s inverse and the first two derivatives of `G` at `p` alone. -/
theorem curvG_eq (u v w : Fin n → ℝ) :
    curv (lcConn (Fin n → ℝ) (ndOf (formG G) (formG_symm hs) hn ((formG_smooth hGs).differentiable (by simp))))
      (fun _ => u) (fun _ => v) (fun _ => w) p = curvG G Gi p u v w := by
  have hF : ∀ e a b, fderiv ℝ (lcGam (formG G)) p e a b = DgamG G Gi p e a b := fun e a b => by
    rw [fderiv_apply₂' (lcGam_differentiable hn hGs p), fderiv_lcGam_formG hn hGs hinv]
  rw [curv_model _ _ (fun x w u => lcConn_const (formG_symm hs) _ _ x w u) (lcGam_differentiable hn hGs), hF, hF,
    lcGam_formG hn hGs hinv, lcGam_formG hn hGs hinv, lcGam_formG hn hGs hinv, lcGam_formG hn hGs hinv]
  rfl

/-- `Γ` is linear in its second slot: `Γ(a, b) = Σⱼ bⱼ Γ(a, eⱼ)`. -/
lemma gamG_right (a b : Fin n → ℝ) (k : Fin n) :
    gamG G Gi p a b k = ∑ j, b j * gamG G Gi p a (Pi.single j 1) k := by
  rw [← lcGam_formG hn hGs hinv]
  conv_lhs => rw [← Finset.univ_sum_single b]
  simp only [map_sum, Finset.sum_apply]
  refine Finset.sum_congr rfl fun j _ => ?_
  rw [show (Pi.single j (b j) : Fin n → ℝ) = b j • Pi.single j 1 by ext m; simp [Pi.single_apply], map_smul,
    lcGam_formG hn hGs hinv]
  rfl

end EngineG

/-! ## The squashed `S⁵` (row 83), in a chart where every entry is polynomial in a softmax

`S⁵ ⊂ ℂ³` with `|zₐ|² = μₐ`, `μ = softmax(y₀, y₁, 0)`, and the phases `y₂, y₃, y₄`. The round metric is
`¼(Σ μₐ dθₐ² − (Σ μₐ dθₐ)²)` on the base (the Fisher metric of the simplex in natural parameters) plus `Σ μₐ dφₐ²`,
and the canonical variation of the Hopf fibration adds `(t² − 1)η²` with `η = Σ μₐ dφₐ`. Every entry is smooth and the
whole form is positive definite on all of `ℝ⁵` (for `t ≠ 0`), so no cutoff is needed. -/

section SquashedS5

/-- The base's natural parameters, with the third pinned at `0`. -/
noncomputable def nuL : Fin 3 → (Fin 5 → ℝ) →L[ℝ] ℝ := ![ContinuousLinearMap.proj 0, ContinuousLinearMap.proj 1, 0]

noncomputable def nu (y : Fin 5 → ℝ) (a : Fin 3) : ℝ := nuL a y

noncomputable def mu (a : Fin 3) (y : Fin 5 → ℝ) : ℝ := Real.exp (nu y a) * (∑ b, Real.exp (nu y b))⁻¹

/-- `μ`'s directional derivative: `∂_v μₐ = μₐ(νₐ(v) − Σ_b μ_b ν_b(v))`. -/
noncomputable def dmu (a : Fin 3) (y v : Fin 5 → ℝ) : ℝ := mu a y * (nu v a - ∑ b, mu b y * nu v b)

/-- `∂_u ∂_v μₐ`. -/
noncomputable def ddmu (a : Fin 3) (y u v : Fin 5 → ℝ) : ℝ :=
  dmu a y u * (nu v a - ∑ b, mu b y * nu v b) - mu a y * ∑ b, nu v b * dmu b y u

lemma Z_pos (y : Fin 5 → ℝ) : 0 < ∑ b, Real.exp (nu y b) := Finset.sum_pos (fun _ _ => Real.exp_pos _) ⟨0, by simp⟩

lemma mu_pos (a : Fin 3) (y : Fin 5 → ℝ) : 0 < mu a y := mul_pos (Real.exp_pos _) (inv_pos.2 (Z_pos y))

lemma mu_sum (y : Fin 5 → ℝ) : ∑ a, mu a y = 1 := by
  simp only [mu, ← Finset.sum_mul]; exact mul_inv_cancel₀ (Z_pos y).ne'

lemma mu_hasFDerivAt (a : Fin 3) (y : Fin 5 → ℝ) :
    ∃ L : (Fin 5 → ℝ) →L[ℝ] ℝ, HasFDerivAt (mu a) L y ∧ ∀ v, L v = dmu a y v := by
  have hE : ∀ b, HasFDerivAt (fun y => Real.exp (nu y b)) (Real.exp (nu y b) • nuL b) y := fun b =>
    (nuL b).hasFDerivAt.exp
  have hq := (hE a).mul ((hasDerivAt_inv (Z_pos y).ne').comp_hasFDerivAt y
    (HasFDerivAt.fun_sum (u := Finset.univ) fun b _ => hE b))
  refine ⟨_, hq, fun v => ?_⟩
  have := (Z_pos y).ne'
  simp only [ContinuousLinearMap.coe_smul', ContinuousLinearMap.coe_add', ContinuousLinearMap.coe_sum',
    Function.comp_apply, Pi.smul_apply, Pi.add_apply, Finset.sum_apply, smul_eq_mul,
    dmu, mu]
  have hS : ∑ b, Real.exp (nu y b) * (∑ b, Real.exp (nu y b))⁻¹ * nu v b
      = (∑ b, Real.exp (nu y b))⁻¹ * ∑ b, Real.exp (nu y b) * nu v b := by
    rw [Finset.mul_sum]; exact Finset.sum_congr rfl fun _ _ => by ring
  rw [hS]
  change _ * (_ * ∑ x, Real.exp (nu y x) * nu v x) + _ * (_ * nu v a) = _
  field_simp
  ring

lemma fderiv_mu (a : Fin 3) (y v : Fin 5 → ℝ) : fderiv ℝ (mu a) y v = dmu a y v := by
  obtain ⟨L, hL, hv⟩ := mu_hasFDerivAt a y; rw [hL.fderiv, hv]

lemma mu_smooth (a : Fin 3) : ContDiff ℝ ∞ (mu a) := by
  have hE : ∀ b, ContDiff ℝ ∞ fun y => Real.exp (nu y b) := fun b => (nuL b).contDiff.exp
  exact (hE a).mul ((ContDiff.sum fun b _ => hE b).inv fun y => (Z_pos y).ne')

lemma dmu_hasFDerivAt (a : Fin 3) (p v : Fin 5 → ℝ) :
    ∃ L : (Fin 5 → ℝ) →L[ℝ] ℝ, HasFDerivAt (fun y => dmu a y v) L p ∧ ∀ u, L u = ddmu a p u v := by
  choose L hL hLv using fun b => mu_hasFDerivAt b p
  have h := (hL a).mul ((HasFDerivAt.fun_sum (u := Finset.univ) fun b _ => (hL b).mul_const (nu v b)).const_sub
    (nu v a))
  refine ⟨_, h, fun u => ?_⟩
  simp only [ContinuousLinearMap.coe_smul', ContinuousLinearMap.coe_add', ContinuousLinearMap.coe_neg',
    ContinuousLinearMap.coe_sum', Pi.smul_apply, Pi.add_apply, Pi.neg_apply, Finset.sum_apply, smul_eq_mul, hLv,
    ddmu]
  ring

/-- The two blocks (base, fibre) and the `μ` each coordinate carries. -/
def blk : Fin 5 → Fin 2 := ![0, 0, 1, 1, 1]
def cix : Fin 5 → Fin 3 := ![0, 1, 0, 1, 2]

noncomputable def alphaS (i j : Fin 5) : ℝ := if blk i = blk j then (if blk i = 0 then 1 / 4 else 1) else 0
noncomputable def betaS (t : ℝ) (i j : Fin 5) : ℝ := if blk i = blk j then (if blk i = 0 then -1 / 4 else t ^ 2 - 1) else 0

/-- **The squashed `S⁵`**: `¼(Σ μ dθ² − (Σ μ dθ)²) + Σ μ dφ² + (t² − 1)(Σ μ dφ)²`. -/
noncomputable def GS (t : ℝ) (i j : Fin 5) (y : Fin 5 → ℝ) : ℝ :=
  alphaS i j * ((if i = j then 1 else 0) * mu (cix i) y) + betaS t i j * (mu (cix i) y * mu (cix j) y)

noncomputable def GD1 (t : ℝ) (i j : Fin 5) (y v : Fin 5 → ℝ) : ℝ :=
  alphaS i j * ((if i = j then 1 else 0) * dmu (cix i) y v)
    + betaS t i j * (dmu (cix i) y v * mu (cix j) y + mu (cix i) y * dmu (cix j) y v)

noncomputable def GD2 (t : ℝ) (i j : Fin 5) (p u v : Fin 5 → ℝ) : ℝ :=
  alphaS i j * ((if i = j then 1 else 0) * ddmu (cix i) p u v)
    + betaS t i j * (ddmu (cix i) p u v * mu (cix j) p + dmu (cix i) p v * dmu (cix j) p u
      + dmu (cix i) p u * dmu (cix j) p v + mu (cix i) p * ddmu (cix j) p u v)

lemma GS_symm (t : ℝ) (i j : Fin 5) (y : Fin 5 → ℝ) : GS t i j y = GS t j i y := by
  fin_cases i <;> fin_cases j <;> simp [GS, alphaS, betaS, blk, cix, mul_comm]

lemma GS_smooth (t : ℝ) (i j : Fin 5) : ContDiff ℝ ∞ (GS t i j) :=
  (contDiff_const.mul (contDiff_const.mul (mu_smooth _))).add
    (contDiff_const.mul ((mu_smooth _).mul (mu_smooth _)))

lemma GS_hasFDerivAt (t : ℝ) (i j : Fin 5) (y : Fin 5 → ℝ) :
    ∃ L : (Fin 5 → ℝ) →L[ℝ] ℝ, HasFDerivAt (GS t i j) L y ∧ ∀ v, L v = GD1 t i j y v := by
  choose L hL hLv using fun b => mu_hasFDerivAt b y
  refine ⟨_, (((hL (cix i)).const_mul _).const_mul _).add (((hL (cix i)).mul (hL (cix j))).const_mul _),
    fun v => ?_⟩
  simp only [ContinuousLinearMap.coe_smul', ContinuousLinearMap.coe_add', Pi.smul_apply, Pi.add_apply,
    smul_eq_mul, hLv, GD1]
  ring

lemma fderiv_GS (t : ℝ) (i j : Fin 5) (y v : Fin 5 → ℝ) : fderiv ℝ (GS t i j) y v = GD1 t i j y v := by
  obtain ⟨L, hL, hv⟩ := GS_hasFDerivAt t i j y; rw [hL.fderiv, hv]

lemma fderiv2_GS (t : ℝ) (i j : Fin 5) (p u v : Fin 5 → ℝ) :
    fderiv ℝ (fderiv ℝ (GS t i j)) p u v = GD2 t i j p u v := by
  choose L hL hLv using fun b => mu_hasFDerivAt b p
  choose M hM hMv using fun b => dmu_hasFDerivAt b p v
  have h := ((((hM (cix i)).const_mul (if i = j then (1 : ℝ) else 0)).const_mul (alphaS i j)).add
    ((((hM (cix i)).mul (hL (cix j))).add ((hL (cix i)).mul (hM (cix j)))).const_mul (betaS t i j)))
  rw [d2_of (GS_smooth t i j) (fun y => fderiv_GS t i j y v) (h.congr_of_eventuallyEq
    (Eventually.of_forall fun y => by simp only [GD1, Pi.add_apply, Pi.mul_apply]))]
  simp only [ContinuousLinearMap.coe_smul', ContinuousLinearMap.coe_add', Pi.smul_apply, Pi.add_apply,
    smul_eq_mul, hLv, hMv, GD2]
  ring

/-- **Positive definite on all of `ℝ⁵`** for `t ≠ 0`, hence nondegenerate: the form is a sum of squares,
`¼(m₀m₁(u₀−u₁)² + m₀m₂u₀² + m₁m₂u₁²) + Σ_{a<b} mₐm_b(φₐ−φ_b)² + t²(Σ mₐφₐ)²`, using `Σ mₐ = 1`. -/
lemma GS_nondeg {t : ℝ} (ht : t ≠ 0) (y u : Fin 5 → ℝ) (h : ∀ v, formG (GS t) y u v = 0) : u = 0 := by
  have hQ := h u
  rw [formG_apply] at hQ
  simp only [Fin.sum_univ_five, GS, alphaS, betaS, blk, cix] at hQ
  simp at hQ
  have hs := mu_sum y
  simp only [Fin.sum_univ_three] at hs
  have p0 := mu_pos 0 y; have p1 := mu_pos 1 y; have p2 := mu_pos 2 y
  set m0 := mu 0 y; set m1 := mu 1 y; set m2 := mu 2 y
  have hm2 : m2 = 1 - m0 - m1 := by linarith
  have key : (m0 * m1 * (u 0 - u 1) ^ 2 + m0 * m2 * u 0 ^ 2 + m1 * m2 * u 1 ^ 2) / 4
      + (m0 * m1 * (u 2 - u 3) ^ 2 + m0 * m2 * (u 2 - u 4) ^ 2 + m1 * m2 * (u 3 - u 4) ^ 2)
      + t ^ 2 * (m0 * u 2 + m1 * u 3 + m2 * u 4) ^ 2 = 0 := by
    rw [← hQ, hm2]; ring
  have q1 := mul_nonneg (mul_nonneg p0.le p1.le) (sq_nonneg (u 0 - u 1))
  have q2 := mul_nonneg (mul_nonneg p0.le p2.le) (sq_nonneg (u 0))
  have q3 := mul_nonneg (mul_nonneg p1.le p2.le) (sq_nonneg (u 1))
  have q4 := mul_nonneg (mul_nonneg p0.le p1.le) (sq_nonneg (u 2 - u 3))
  have q5 := mul_nonneg (mul_nonneg p0.le p2.le) (sq_nonneg (u 2 - u 4))
  have q6 := mul_nonneg (sq_nonneg t) (sq_nonneg (m0 * u 2 + m1 * u 3 + m2 * u 4))
  have q7 := mul_nonneg (mul_nonneg p1.le p2.le) (sq_nonneg (u 3 - u 4))
  have z : ∀ {a b x : ℝ}, 0 < a → 0 < b → a * b * x ^ 2 = 0 → x = 0 := fun ha hb hx => by
    rcases mul_eq_zero.1 hx with h | h
    · exact absurd h (mul_pos ha hb).ne'
    · exact pow_eq_zero_iff (n := 2) (by norm_num) |>.1 h
  have e0 : u 0 = 0 := z p0 p2 (by linarith)
  have e1 : u 1 = 0 := z p1 p2 (by linarith)
  have e23 : u 2 - u 3 = 0 := z p0 p1 (by linarith)
  have e24 : u 2 - u 4 = 0 := z p0 p2 (by linarith)
  have em : m0 * u 2 + m1 * u 3 + m2 * u 4 = 0 := by
    have : t ^ 2 * (m0 * u 2 + m1 * u 3 + m2 * u 4) ^ 2 = 0 := by linarith
    rcases mul_eq_zero.1 this with h | h
    · exact absurd (pow_eq_zero_iff (n := 2) (by norm_num) |>.1 h) ht
    · exact pow_eq_zero_iff (n := 2) (by norm_num) |>.1 h
  have e2 : u 2 = 0 := by
    have : (m0 + m1 + m2) * u 2 = 0 := by rw [← em]; linear_combination m1 * e23 + m2 * e24
    rw [hs, one_mul] at this; exact this
  funext i; fin_cases i <;> simp <;> linarith

lemma mu_zero (a : Fin 3) : mu a 0 = 1 / 3 := by
  simp [mu, nu, nuL]

/-- The inverse at the point `y = 0` (where `μ = (⅓, ⅓, ⅓)`). -/
noncomputable def GiS (t : ℝ) : Fin 5 → Fin 5 → ℝ :=
  ![![24, 12, 0, 0, 0], ![12, 24, 0, 0, 0], ![0, 0, 2 + 1 / t ^ 2, -1 + 1 / t ^ 2, -1 + 1 / t ^ 2],
    ![0, 0, -1 + 1 / t ^ 2, 2 + 1 / t ^ 2, -1 + 1 / t ^ 2], ![0, 0, -1 + 1 / t ^ 2, -1 + 1 / t ^ 2, 2 + 1 / t ^ 2]]

lemma GiS_inv {t : ℝ} (ht : t ≠ 0) (m k : Fin 5) :
    ∑ l, GS t m l 0 * GiS t l k = if m = k then 1 else 0 := by
  fin_cases m <;> fin_cases k <;> simp [Fin.sum_univ_five, GS, alphaS, betaS, blk, cix, mu_zero, GiS] <;>
    field_simp <;> ring

noncomputable def D1L (t : ℝ) : Fin 5 → Fin 5 → Fin 5 → ℝ := ![![![(1/54), (-1/108), 0, 0, 0], ![(-1/108), (-1/108), 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]], ![![(-1/108), (-1/108), 0, 0, 0], ![(-1/108), (1/54), 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]], ![![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![(2*(2*t^2 + 1)/27), (-(2*t^2 + 1)/27), 0, 0, 0], ![((t - 1)*(t + 1)/27), ((t - 1)*(t + 1)/27), 0, 0, 0], ![((t - 1)*(t + 1)/27), (-2*(t - 1)*(t + 1)/27), 0, 0, 0]], ![![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![((t - 1)*(t + 1)/27), ((t - 1)*(t + 1)/27), 0, 0, 0], ![(-(2*t^2 + 1)/27), (2*(2*t^2 + 1)/27), 0, 0, 0], ![(-2*(t - 1)*(t + 1)/27), ((t - 1)*(t + 1)/27), 0, 0, 0]], ![![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![((t - 1)*(t + 1)/27), (-2*(t - 1)*(t + 1)/27), 0, 0, 0], ![(-2*(t - 1)*(t + 1)/27), ((t - 1)*(t + 1)/27), 0, 0, 0], ![(-(2*t^2 + 1)/27), (-(2*t^2 + 1)/27), 0, 0, 0]]]

noncomputable def D2L (t : ℝ) : Fin 5 → Fin 5 → Fin 5 → Fin 5 → ℝ := ![![![![(-1/54), (1/108), 0, 0, 0], ![(1/108), (-1/108), 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]], ![![(1/108), (-1/108), 0, 0, 0], ![(-1/108), (1/108), 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]], ![![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]], ![![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]], ![![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]]], ![![![(1/108), (-1/108), 0, 0, 0], ![(-1/108), (1/108), 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]], ![![(-1/108), (1/108), 0, 0, 0], ![(1/108), (-1/54), 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]], ![![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]], ![![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]], ![![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]]], ![![![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]], ![![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]], ![![(2*(2*t^2 - 1)/27), (-(2*t^2 - 1)/27), 0, 0, 0], ![(-(2*t^2 - 1)/27), (-1/27), 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]], ![![(-(t - 1)*(t + 1)/27), ((t - 1)*(t + 1)/27), 0, 0, 0], ![((t - 1)*(t + 1)/27), (-(t - 1)*(t + 1)/27), 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]], ![![(-(t - 1)*(t + 1)/27), 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]]], ![![![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]], ![![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]], ![![(-(t - 1)*(t + 1)/27), ((t - 1)*(t + 1)/27), 0, 0, 0], ![((t - 1)*(t + 1)/27), (-(t - 1)*(t + 1)/27), 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]], ![![(-1/27), (-(2*t^2 - 1)/27), 0, 0, 0], ![(-(2*t^2 - 1)/27), (2*(2*t^2 - 1)/27), 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]], ![![0, 0, 0, 0, 0], ![0, (-(t - 1)*(t + 1)/27), 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]]], ![![![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]], ![![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]], ![![(-(t - 1)*(t + 1)/27), 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]], ![![0, 0, 0, 0, 0], ![0, (-(t - 1)*(t + 1)/27), 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]], ![![(-1/27), (2*t^2/27), 0, 0, 0], ![(2*t^2/27), (-1/27), 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]]]]

/-- `Γᵏᵢⱼ` at `y = 0`, indexed `i j k`. -/
noncomputable def GamL (t : ℝ) : Fin 5 → Fin 5 → Fin 5 → ℝ := ![![![(1/6), 0, 0, 0, 0], ![(-1/6), (-1/6), 0, 0, 0], ![0, 0, ((t^2 + 2)/9), (-(t - 1)*(t + 1)/18), (-(t - 1)*(t + 1)/18)], ![0, 0, ((t - 1)*(t + 1)/9), (-(t^2 + 2)/18), (-(t - 1)*(t + 1)/18)], ![0, 0, ((t - 1)*(t + 1)/9), (-(t - 1)*(t + 1)/18), (-(t^2 + 2)/18)]], ![![(-1/6), (-1/6), 0, 0, 0], ![0, (1/6), 0, 0, 0], ![0, 0, (-(t^2 + 2)/18), ((t - 1)*(t + 1)/9), (-(t - 1)*(t + 1)/18)], ![0, 0, (-(t - 1)*(t + 1)/18), ((t^2 + 2)/9), (-(t - 1)*(t + 1)/18)], ![0, 0, (-(t - 1)*(t + 1)/18), ((t - 1)*(t + 1)/9), (-(t^2 + 2)/18)]], ![![0, 0, ((t^2 + 2)/9), (-(t - 1)*(t + 1)/18), (-(t - 1)*(t + 1)/18)], ![0, 0, (-(t^2 + 2)/18), ((t - 1)*(t + 1)/9), (-(t - 1)*(t + 1)/18)], ![(-2*(2*t^2 + 1)/3), 0, 0, 0, 0], ![(-2*(t - 1)*(t + 1)/3), (-2*(t - 1)*(t + 1)/3), 0, 0, 0], ![0, (2*(t - 1)*(t + 1)/3), 0, 0, 0]], ![![0, 0, ((t - 1)*(t + 1)/9), (-(t^2 + 2)/18), (-(t - 1)*(t + 1)/18)], ![0, 0, (-(t - 1)*(t + 1)/18), ((t^2 + 2)/9), (-(t - 1)*(t + 1)/18)], ![(-2*(t - 1)*(t + 1)/3), (-2*(t - 1)*(t + 1)/3), 0, 0, 0], ![0, (-2*(2*t^2 + 1)/3), 0, 0, 0], ![(2*(t - 1)*(t + 1)/3), 0, 0, 0, 0]], ![![0, 0, ((t - 1)*(t + 1)/9), (-(t - 1)*(t + 1)/18), (-(t^2 + 2)/18)], ![0, 0, (-(t - 1)*(t + 1)/18), ((t - 1)*(t + 1)/9), (-(t^2 + 2)/18)], ![0, (2*(t - 1)*(t + 1)/3), 0, 0, 0], ![(2*(t - 1)*(t + 1)/3), 0, 0, 0, 0], ![(2*(2*t^2 + 1)/3), (2*(2*t^2 + 1)/3), 0, 0, 0]]]

noncomputable def RicL (t : ℝ) : Fin 5 → Fin 5 → ℝ := ![![(-(t^2 - 3)/9), ((t^2 - 3)/18), 0, 0, 0], ![((t^2 - 3)/18), (-(t^2 - 3)/9), 0, 0, 0], ![0, 0, (4*(t^4 - t^2 + 3)/9), (2*(t - 1)*(t + 1)*(2*t^2 + 3)/9), (2*(t - 1)*(t + 1)*(2*t^2 + 3)/9)], ![0, 0, (2*(t - 1)*(t + 1)*(2*t^2 + 3)/9), (4*(t^4 - t^2 + 3)/9), (2*(t - 1)*(t + 1)*(2*t^2 + 3)/9)], ![0, 0, (2*(t - 1)*(t + 1)*(2*t^2 + 3)/9), (2*(t - 1)*(t + 1)*(2*t^2 + 3)/9), (4*(t^4 - t^2 + 3)/9)]]

set_option maxHeartbeats 0 in
lemma D1_tab (t : ℝ) (i j c : Fin 5) : dG1 (GS t) 0 i j (Pi.single c 1) = D1L t i j c := by
  rw [dG1, fderiv_GS]
  fin_cases i <;> fin_cases j <;> fin_cases c <;>
    simp [GD1, dmu, mu_zero, nu, nuL, alphaS, betaS, blk, cix, D1L, Fin.sum_univ_three] <;> ring

set_option maxHeartbeats 0 in
lemma D2_tab (t : ℝ) (i j a c : Fin 5) :
    dG2 (GS t) 0 i j (Pi.single a 1) (Pi.single c 1) = D2L t i j a c := by
  rw [dG2, fderiv2_GS]
  fin_cases i <;> fin_cases j <;> fin_cases a <;> fin_cases c <;>
    simp [GD2, ddmu, dmu, mu_zero, nu, nuL, alphaS, betaS, blk, cix, D2L, Fin.sum_univ_three] <;> (try ring) <;> simp

set_option maxHeartbeats 0 in
lemma Gam_tab {t : ℝ} (ht : t ≠ 0) (i j k : Fin 5) :
    gamG (GS t) (GiS t) 0 (Pi.single i 1) (Pi.single j 1) k = GamL t i j k := by
  simp only [gamG, kosG_basis, D1_tab, Fin.sum_univ_five]
  fin_cases i <;> fin_cases j <;> fin_cases k <;> simp [D1L, GiS, GamL] <;> field_simp <;> ring

/-- `∂_u Γ` at a basis triple, from the tables. -/
lemma DGam_basis {t : ℝ} (ht : t ≠ 0) (u i j k : Fin 5) :
    DgamG (GS t) (GiS t) 0 (Pi.single u 1) (Pi.single i 1) (Pi.single j 1) k
      = ∑ l, ((D2L t j l u i + D2L t l i u j - D2L t i j u l) / 2 - ∑ m, D1L t m l u * GamL t i j m) * GiS t l k := by
  simp only [DgamG, DkosG_basis, D2_tab, D1_tab, Gam_tab ht]

lemma GamGam {t : ℝ} (ht : t ≠ 0) (i j k l : Fin 5) :
    gamG (GS t) (GiS t) 0 (Pi.single i 1) (gamG (GS t) (GiS t) 0 (Pi.single j 1) (Pi.single k 1)) l
      = ∑ c, GamL t j k c * GamL t i c l := by
  rw [gamG_right (fun y u h => GS_nondeg ht y u h) (GS_smooth t) (GiS_inv ht)]
  simp only [Gam_tab ht]

/-- The curvature array of THE connection at `y = 0`, on coordinate fields. -/
noncomputable def RfS (t : ℝ) (i j k l : Fin 5) : ℝ :=
  curvG (GS t) (GiS t) 0 (Pi.single i 1) (Pi.single j 1) (Pi.single k 1) l

set_option maxHeartbeats 0 in
lemma Ric_tab {t : ℝ} (ht : t ≠ 0) (j k : Fin 5) : ricCN (RfS t) j k = RicL t j k := by
  simp only [ricCN, RfS, curvG, Pi.sub_apply, Pi.add_apply, GamGam ht, DGam_basis ht, Fin.sum_univ_five]
  fin_cases j <;> fin_cases k <;> simp [D1L, D2L, GiS, GamL, RicL] <;> field_simp <;> ring

/-- **Row 83.** THE connection of the squashed `S⁵` (the canonical variation of the Hopf fibration `S⁵ → ℂP²`
with fibre scale `t`) has scalar curvature `R = 24 − 4t²`, contracted with the inverse metric, at the point `y = 0`.
`t = 1` is the round sphere's `20`. -/
theorem row83_squashed_S5 {t : ℝ} (ht : t ≠ 0) :
    scalG (GiS t) (fun i j k l => curv (lcConn (Fin 5 → ℝ) (ndOf (formG (GS t)) (formG_symm (GS_symm t))
      (fun y u h => GS_nondeg ht y u h) ((formG_smooth (GS_smooth t)).differentiable (by simp))))
      (fun _ => Pi.single i 1) (fun _ => Pi.single j 1) (fun _ => Pi.single k 1) 0 l) = 24 - 4 * t ^ 2 := by
  have h : (fun i j k l => curv (lcConn (Fin 5 → ℝ) (ndOf (formG (GS t)) (formG_symm (GS_symm t))
      (fun y u h => GS_nondeg ht y u h) ((formG_smooth (GS_smooth t)).differentiable (by simp))))
      (fun _ => (Pi.single i 1 : Fin 5 → ℝ)) (fun _ => Pi.single j 1) (fun _ => Pi.single k 1) 0 l) = RfS t := by
    funext i j k l
    rw [curvG_eq (GS_symm t) (fun y u h => GS_nondeg ht y u h) (GS_smooth t) (GiS_inv ht)]
    rfl
  rw [h, scalG]
  simp only [Ric_tab ht, Fin.sum_univ_five]
  simp [GiS, RicL]
  field_simp
  ring

/-! ### Row 83's open half: the same computation at EVERY point `y`

At a general `y` the tables are polynomial (derivatives) or rational (`Γ`) in `m₀ = μ₀(y)`, `m₁ = μ₁(y)`, with
`μ₂ = 1 − m₀ − m₁`. -/

lemma mu_two (y : Fin 5 → ℝ) : mu 2 y = 1 - mu 0 y - mu 1 y := by
  have := mu_sum y; simp only [Fin.sum_univ_three] at this; linarith

noncomputable def GiG (m0 m1 t : ℝ) : Fin 5 → Fin 5 → ℝ := ![![(4*(m1 - 1)/(m0*(m0 + m1 - 1))), (-4/(m0 + m1 - 1)), 0, 0, 0], ![(-4/(m0 + m1 - 1)), (4*(m0 - 1)/(m1*(m0 + m1 - 1))), 0, 0, 0], ![0, 0, (-(m0*t^2 - m0 - t^2)/(m0*t^2)), (-(t - 1)*(t + 1)/t^2), (-(t - 1)*(t + 1)/t^2)], ![0, 0, (-(t - 1)*(t + 1)/t^2), (-(m1*t^2 - m1 - t^2)/(m1*t^2)), (-(t - 1)*(t + 1)/t^2)], ![0, 0, (-(t - 1)*(t + 1)/t^2), (-(t - 1)*(t + 1)/t^2), (-(m0*t^2 - m0 + m1*t^2 - m1 + 1)/(t^2*(m0 + m1 - 1)))]]

noncomputable def D1G (m0 m1 t : ℝ) : Fin 5 → Fin 5 → Fin 5 → ℝ := ![![![(m0*(m0 - 1)*(2*m0 - 1)/4), (m0*m1*(2*m0 - 1)/4), 0, 0, 0], ![(m0*m1*(2*m0 - 1)/4), (m0*m1*(2*m1 - 1)/4), 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]], ![![(m0*m1*(2*m0 - 1)/4), (m0*m1*(2*m1 - 1)/4), 0, 0, 0], ![(m0*m1*(2*m1 - 1)/4), (m1*(m1 - 1)*(2*m1 - 1)/4), 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]], ![![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![(-m0*(m0 - 1)*(2*m0*t^2 - 2*m0 + 1)), (-m0*m1*(2*m0*t^2 - 2*m0 + 1)), 0, 0, 0], ![(-m0*m1*(2*m0 - 1)*(t - 1)*(t + 1)), (-m0*m1*(2*m1 - 1)*(t - 1)*(t + 1)), 0, 0, 0], ![(m0*(2*m0 - 1)*(t - 1)*(t + 1)*(m0 + m1 - 1)), (2*m0*m1*(t - 1)*(t + 1)*(m0 + m1 - 1)), 0, 0, 0]], ![![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![(-m0*m1*(2*m0 - 1)*(t - 1)*(t + 1)), (-m0*m1*(2*m1 - 1)*(t - 1)*(t + 1)), 0, 0, 0], ![(-m0*m1*(2*m1*t^2 - 2*m1 + 1)), (-m1*(m1 - 1)*(2*m1*t^2 - 2*m1 + 1)), 0, 0, 0], ![(2*m0*m1*(t - 1)*(t + 1)*(m0 + m1 - 1)), (m1*(2*m1 - 1)*(t - 1)*(t + 1)*(m0 + m1 - 1)), 0, 0, 0]], ![![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![(m0*(2*m0 - 1)*(t - 1)*(t + 1)*(m0 + m1 - 1)), (2*m0*m1*(t - 1)*(t + 1)*(m0 + m1 - 1)), 0, 0, 0], ![(2*m0*m1*(t - 1)*(t + 1)*(m0 + m1 - 1)), (m1*(2*m1 - 1)*(t - 1)*(t + 1)*(m0 + m1 - 1)), 0, 0, 0], ![(-m0*(m0 + m1 - 1)*(2*m0*t^2 - 2*m0 + 2*m1*t^2 - 2*m1 - 2*t^2 + 1)), (-m1*(m0 + m1 - 1)*(2*m0*t^2 - 2*m0 + 2*m1*t^2 - 2*m1 - 2*t^2 + 1)), 0, 0, 0]]]

noncomputable def D2G (m0 m1 t : ℝ) : Fin 5 → Fin 5 → Fin 5 → Fin 5 → ℝ := ![![![![(-m0*(m0 - 1)*(6*m0^2 - 6*m0 + 1)/4), (-m0*m1*(6*m0^2 - 6*m0 + 1)/4), 0, 0, 0], ![(-m0*m1*(6*m0^2 - 6*m0 + 1)/4), (-m0*m1*(6*m0*m1 - 2*m0 - 2*m1 + 1)/4), 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]], ![![(-m0*m1*(6*m0^2 - 6*m0 + 1)/4), (-m0*m1*(6*m0*m1 - 2*m0 - 2*m1 + 1)/4), 0, 0, 0], ![(-m0*m1*(6*m0*m1 - 2*m0 - 2*m1 + 1)/4), (-m0*m1*(6*m1^2 - 6*m1 + 1)/4), 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]], ![![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]], ![![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]], ![![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]]], ![![![(-m0*m1*(6*m0^2 - 6*m0 + 1)/4), (-m0*m1*(6*m0*m1 - 2*m0 - 2*m1 + 1)/4), 0, 0, 0], ![(-m0*m1*(6*m0*m1 - 2*m0 - 2*m1 + 1)/4), (-m0*m1*(6*m1^2 - 6*m1 + 1)/4), 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]], ![![(-m0*m1*(6*m0*m1 - 2*m0 - 2*m1 + 1)/4), (-m0*m1*(6*m1^2 - 6*m1 + 1)/4), 0, 0, 0], ![(-m0*m1*(6*m1^2 - 6*m1 + 1)/4), (-m1*(m1 - 1)*(6*m1^2 - 6*m1 + 1)/4), 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]], ![![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]], ![![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]], ![![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]]], ![![![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]], ![![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]], ![![(m0*(m0 - 1)*(6*m0^2*t^2 - 6*m0^2 - 4*m0*t^2 + 6*m0 - 1)), (m0*m1*(6*m0^2*t^2 - 6*m0^2 - 4*m0*t^2 + 6*m0 - 1)), 0, 0, 0], ![(m0*m1*(6*m0^2*t^2 - 6*m0^2 - 4*m0*t^2 + 6*m0 - 1)), (m0*m1*(6*m0*m1*t^2 - 6*m0*m1 - 2*m0*t^2 + 2*m0 + 2*m1 - 1)), 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]], ![![(m0*m1*(t - 1)*(t + 1)*(6*m0^2 - 6*m0 + 1)), (m0*m1*(t - 1)*(t + 1)*(6*m0*m1 - 2*m0 - 2*m1 + 1)), 0, 0, 0], ![(m0*m1*(t - 1)*(t + 1)*(6*m0*m1 - 2*m0 - 2*m1 + 1)), (m0*m1*(t - 1)*(t + 1)*(6*m1^2 - 6*m1 + 1)), 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]], ![![(-m0*(t - 1)*(t + 1)*(m0 + m1 - 1)*(6*m0^2 - 6*m0 + 1)), (-2*m0*m1*(3*m0 - 1)*(t - 1)*(t + 1)*(m0 + m1 - 1)), 0, 0, 0], ![(-2*m0*m1*(3*m0 - 1)*(t - 1)*(t + 1)*(m0 + m1 - 1)), (-2*m0*m1*(3*m1 - 1)*(t - 1)*(t + 1)*(m0 + m1 - 1)), 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]]], ![![![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]], ![![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]], ![![(m0*m1*(t - 1)*(t + 1)*(6*m0^2 - 6*m0 + 1)), (m0*m1*(t - 1)*(t + 1)*(6*m0*m1 - 2*m0 - 2*m1 + 1)), 0, 0, 0], ![(m0*m1*(t - 1)*(t + 1)*(6*m0*m1 - 2*m0 - 2*m1 + 1)), (m0*m1*(t - 1)*(t + 1)*(6*m1^2 - 6*m1 + 1)), 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]], ![![(m0*m1*(6*m0*m1*t^2 - 6*m0*m1 + 2*m0 - 2*m1*t^2 + 2*m1 - 1)), (m0*m1*(6*m1^2*t^2 - 6*m1^2 - 4*m1*t^2 + 6*m1 - 1)), 0, 0, 0], ![(m0*m1*(6*m1^2*t^2 - 6*m1^2 - 4*m1*t^2 + 6*m1 - 1)), (m1*(m1 - 1)*(6*m1^2*t^2 - 6*m1^2 - 4*m1*t^2 + 6*m1 - 1)), 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]], ![![(-2*m0*m1*(3*m0 - 1)*(t - 1)*(t + 1)*(m0 + m1 - 1)), (-2*m0*m1*(3*m1 - 1)*(t - 1)*(t + 1)*(m0 + m1 - 1)), 0, 0, 0], ![(-2*m0*m1*(3*m1 - 1)*(t - 1)*(t + 1)*(m0 + m1 - 1)), (-m1*(t - 1)*(t + 1)*(m0 + m1 - 1)*(6*m1^2 - 6*m1 + 1)), 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]]], ![![![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]], ![![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]], ![![(-m0*(t - 1)*(t + 1)*(m0 + m1 - 1)*(6*m0^2 - 6*m0 + 1)), (-2*m0*m1*(3*m0 - 1)*(t - 1)*(t + 1)*(m0 + m1 - 1)), 0, 0, 0], ![(-2*m0*m1*(3*m0 - 1)*(t - 1)*(t + 1)*(m0 + m1 - 1)), (-2*m0*m1*(3*m1 - 1)*(t - 1)*(t + 1)*(m0 + m1 - 1)), 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]], ![![(-2*m0*m1*(3*m0 - 1)*(t - 1)*(t + 1)*(m0 + m1 - 1)), (-2*m0*m1*(3*m1 - 1)*(t - 1)*(t + 1)*(m0 + m1 - 1)), 0, 0, 0], ![(-2*m0*m1*(3*m1 - 1)*(t - 1)*(t + 1)*(m0 + m1 - 1)), (-m1*(t - 1)*(t + 1)*(m0 + m1 - 1)*(6*m1^2 - 6*m1 + 1)), 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]], ![![(m0*(m0 + m1 - 1)*(6*m0^2*t^2 - 6*m0^2 + 6*m0*m1*t^2 - 6*m0*m1 - 8*m0*t^2 + 6*m0 - 2*m1*t^2 + 2*m1 + 2*t^2 - 1)), (2*m0*m1*(m0 + m1 - 1)*(3*m0*t^2 - 3*m0 + 3*m1*t^2 - 3*m1 - 3*t^2 + 2)), 0, 0, 0], ![(2*m0*m1*(m0 + m1 - 1)*(3*m0*t^2 - 3*m0 + 3*m1*t^2 - 3*m1 - 3*t^2 + 2)), (m1*(m0 + m1 - 1)*(6*m0*m1*t^2 - 6*m0*m1 - 2*m0*t^2 + 2*m0 + 6*m1^2*t^2 - 6*m1^2 - 8*m1*t^2 + 6*m1 + 2*t^2 - 1)), 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0], ![0, 0, 0, 0, 0]]]]

noncomputable def GamG (m0 m1 t : ℝ) : Fin 5 → Fin 5 → Fin 5 → ℝ := ![![![(-(2*m0 - 1)/2), 0, 0, 0, 0], ![(-m1/2), (-m0/2), 0, 0, 0], ![0, 0, (-(m0 - 1)*(m0*t^2 - m0 + 1)/2), (-m0^2*(t - 1)*(t + 1)/2), (-m0^2*(t - 1)*(t + 1)/2)], ![0, 0, (-m1*(m0 - 1)*(t - 1)*(t + 1)/2), (-m0*(m1*t^2 - m1 + 1)/2), (-m0*m1*(t - 1)*(t + 1)/2)], ![0, 0, ((m0 - 1)*(t - 1)*(t + 1)*(m0 + m1 - 1)/2), (m0*(t - 1)*(t + 1)*(m0 + m1 - 1)/2), (m0*(m0*t^2 - m0 + m1*t^2 - m1 - t^2)/2)]], ![![(-m1/2), (-m0/2), 0, 0, 0], ![0, (-(2*m1 - 1)/2), 0, 0, 0], ![0, 0, (-m1*(m0*t^2 - m0 + 1)/2), (-m0*(m1 - 1)*(t - 1)*(t + 1)/2), (-m0*m1*(t - 1)*(t + 1)/2)], ![0, 0, (-m1^2*(t - 1)*(t + 1)/2), (-(m1 - 1)*(m1*t^2 - m1 + 1)/2), (-m1^2*(t - 1)*(t + 1)/2)], ![0, 0, (m1*(t - 1)*(t + 1)*(m0 + m1 - 1)/2), ((m1 - 1)*(t - 1)*(t + 1)*(m0 + m1 - 1)/2), (m1*(m0*t^2 - m0 + m1*t^2 - m1 - t^2)/2)]], ![![0, 0, (-(m0 - 1)*(m0*t^2 - m0 + 1)/2), (-m0^2*(t - 1)*(t + 1)/2), (-m0^2*(t - 1)*(t + 1)/2)], ![0, 0, (-m1*(m0*t^2 - m0 + 1)/2), (-m0*(m1 - 1)*(t - 1)*(t + 1)/2), (-m0*m1*(t - 1)*(t + 1)/2)], ![(-2*(2*m0*t^2 - 2*m0 + 1)), 0, 0, 0, 0], ![(-2*m1*(t - 1)*(t + 1)), (-2*m0*(t - 1)*(t + 1)), 0, 0, 0], ![(2*(t - 1)*(t + 1)*(2*m0 + m1 - 1)), (2*m0*(t - 1)*(t + 1)), 0, 0, 0]], ![![0, 0, (-m1*(m0 - 1)*(t - 1)*(t + 1)/2), (-m0*(m1*t^2 - m1 + 1)/2), (-m0*m1*(t - 1)*(t + 1)/2)], ![0, 0, (-m1^2*(t - 1)*(t + 1)/2), (-(m1 - 1)*(m1*t^2 - m1 + 1)/2), (-m1^2*(t - 1)*(t + 1)/2)], ![(-2*m1*(t - 1)*(t + 1)), (-2*m0*(t - 1)*(t + 1)), 0, 0, 0], ![0, (-2*(2*m1*t^2 - 2*m1 + 1)), 0, 0, 0], ![(2*m1*(t - 1)*(t + 1)), (2*(t - 1)*(t + 1)*(m0 + 2*m1 - 1)), 0, 0, 0]], ![![0, 0, ((m0 - 1)*(t - 1)*(t + 1)*(m0 + m1 - 1)/2), (m0*(t - 1)*(t + 1)*(m0 + m1 - 1)/2), (m0*(m0*t^2 - m0 + m1*t^2 - m1 - t^2)/2)], ![0, 0, (m1*(t - 1)*(t + 1)*(m0 + m1 - 1)/2), ((m1 - 1)*(t - 1)*(t + 1)*(m0 + m1 - 1)/2), (m1*(m0*t^2 - m0 + m1*t^2 - m1 - t^2)/2)], ![(2*(t - 1)*(t + 1)*(2*m0 + m1 - 1)), (2*m0*(t - 1)*(t + 1)), 0, 0, 0], ![(2*m1*(t - 1)*(t + 1)), (2*(t - 1)*(t + 1)*(m0 + 2*m1 - 1)), 0, 0, 0], ![(-2*(2*m0*t^2 - 2*m0 + 2*m1*t^2 - 2*m1 - 2*t^2 + 1)), (-2*(2*m0*t^2 - 2*m0 + 2*m1*t^2 - 2*m1 - 2*t^2 + 1)), 0, 0, 0]]]

noncomputable def RicG (m0 m1 t : ℝ) : Fin 5 → Fin 5 → ℝ := ![![(m0*(m0 - 1)*(t^2 - 3)/2), (m0*m1*(t^2 - 3)/2), 0, 0, 0], ![(m0*m1*(t^2 - 3)/2), (m1*(m1 - 1)*(t^2 - 3)/2), 0, 0, 0], ![0, 0, (2*m0*(2*m0*t^4 + m0*t^2 - 3*m0 - t^2 + 3)), (2*m0*m1*(t - 1)*(t + 1)*(2*t^2 + 3)), (-2*m0*(t - 1)*(t + 1)*(2*t^2 + 3)*(m0 + m1 - 1))], ![0, 0, (2*m0*m1*(t - 1)*(t + 1)*(2*t^2 + 3)), (2*m1*(2*m1*t^4 + m1*t^2 - 3*m1 - t^2 + 3)), (-2*m1*(t - 1)*(t + 1)*(2*t^2 + 3)*(m0 + m1 - 1))], ![0, 0, (-2*m0*(t - 1)*(t + 1)*(2*t^2 + 3)*(m0 + m1 - 1)), (-2*m1*(t - 1)*(t + 1)*(2*t^2 + 3)*(m0 + m1 - 1)), (2*(m0 + m1 - 1)*(2*m0*t^4 + m0*t^2 - 3*m0 + 2*m1*t^4 + m1*t^2 - 3*m1 - 2*t^4))]]

lemma GiG_inv {t : ℝ} (ht : t ≠ 0) (y : Fin 5 → ℝ) (m k : Fin 5) :
    ∑ l, GS t m l y * GiG (mu 0 y) (mu 1 y) t l k = if m = k then 1 else 0 := by
  have h0 := (mu_pos 0 y).ne'; have h1 := (mu_pos 1 y).ne'
  have h2 : 1 - mu 0 y - mu 1 y ≠ 0 := by rw [← mu_two]; exact (mu_pos 2 y).ne'
  have h2' : -1 + mu 0 y + mu 1 y ≠ 0 := fun h => h2 (by linarith)
  have h3 : mu 0 y + mu 1 y - 1 ≠ 0 := fun h => h2 (by linarith)
  fin_cases m <;> fin_cases k <;> simp [Fin.sum_univ_five, GS, alphaS, betaS, blk, cix, mu_two, GiG] <;>
    field_simp <;> ring

set_option maxHeartbeats 0 in
lemma D1G_tab (t : ℝ) (y : Fin 5 → ℝ) (i j c : Fin 5) :
    dG1 (GS t) y i j (Pi.single c 1) = D1G (mu 0 y) (mu 1 y) t i j c := by
  rw [dG1, fderiv_GS]
  fin_cases i <;> fin_cases j <;> fin_cases c <;>
    simp [GD1, dmu, mu_two, nu, nuL, alphaS, betaS, blk, cix, D1G, Fin.sum_univ_three] <;> ring

set_option maxHeartbeats 0 in
lemma D2G_tab (t : ℝ) (y : Fin 5 → ℝ) (i j a c : Fin 5) :
    dG2 (GS t) y i j (Pi.single a 1) (Pi.single c 1) = D2G (mu 0 y) (mu 1 y) t i j a c := by
  rw [dG2, fderiv2_GS]
  fin_cases i <;> fin_cases j <;> fin_cases a <;> fin_cases c <;>
    simp [GD2, ddmu, dmu, mu_two, nu, nuL, alphaS, betaS, blk, cix, D2G, Fin.sum_univ_three] <;> (try ring) <;> simp

lemma mu_facts (y : Fin 5 → ℝ) : mu 0 y ≠ 0 ∧ mu 1 y ≠ 0 ∧ mu 0 y + mu 1 y - 1 ≠ 0 ∧ -1 + mu 0 y + mu 1 y ≠ 0 ∧
    1 - mu 0 y - mu 1 y ≠ 0 := by
  have h2 : 1 - mu 0 y - mu 1 y ≠ 0 := by rw [← mu_two]; exact (mu_pos 2 y).ne'
  exact ⟨(mu_pos 0 y).ne', (mu_pos 1 y).ne', fun h => h2 (by linarith), fun h => h2 (by linarith), h2⟩

set_option maxHeartbeats 0 in
lemma GamG_tab {t : ℝ} (ht : t ≠ 0) (y : Fin 5 → ℝ) (i j k : Fin 5) :
    gamG (GS t) (GiG (mu 0 y) (mu 1 y) t) y (Pi.single i 1) (Pi.single j 1) k = GamG (mu 0 y) (mu 1 y) t i j k := by
  obtain ⟨h0, h1, h3, h3', h2⟩ := mu_facts y
  simp only [gamG, kosG_basis, D1G_tab, Fin.sum_univ_five]
  generalize mu 0 y = a at *; generalize mu 1 y = b at *
  fin_cases i <;> fin_cases j <;> fin_cases k <;> simp [D1G, GiG, GamG] <;> field_simp <;> ring

lemma DGamG_basis {t : ℝ} (ht : t ≠ 0) (y : Fin 5 → ℝ) (u i j k : Fin 5) :
    DgamG (GS t) (GiG (mu 0 y) (mu 1 y) t) y (Pi.single u 1) (Pi.single i 1) (Pi.single j 1) k
      = ∑ l, ((D2G (mu 0 y) (mu 1 y) t j l u i + D2G (mu 0 y) (mu 1 y) t l i u j - D2G (mu 0 y) (mu 1 y) t i j u l) / 2
        - ∑ m, D1G (mu 0 y) (mu 1 y) t m l u * GamG (mu 0 y) (mu 1 y) t i j m) * GiG (mu 0 y) (mu 1 y) t l k := by
  simp only [DgamG, DkosG_basis, D2G_tab, D1G_tab, GamG_tab ht]

lemma GamGamG {t : ℝ} (ht : t ≠ 0) (y : Fin 5 → ℝ) (i j k l : Fin 5) :
    gamG (GS t) (GiG (mu 0 y) (mu 1 y) t) y (Pi.single i 1)
      (gamG (GS t) (GiG (mu 0 y) (mu 1 y) t) y (Pi.single j 1) (Pi.single k 1)) l
      = ∑ c, GamG (mu 0 y) (mu 1 y) t j k c * GamG (mu 0 y) (mu 1 y) t i c l := by
  rw [gamG_right (fun y u h => GS_nondeg ht y u h) (GS_smooth t) (GiG_inv ht y)]
  simp only [GamG_tab ht]

/-- The curvature array of THE connection at `y`, on coordinate fields. -/
noncomputable def RfG (t : ℝ) (y : Fin 5 → ℝ) (i j k l : Fin 5) : ℝ :=
  curvG (GS t) (GiG (mu 0 y) (mu 1 y) t) y (Pi.single i 1) (Pi.single j 1) (Pi.single k 1) l

set_option maxHeartbeats 0 in
lemma RicG_tab {t : ℝ} (ht : t ≠ 0) (y : Fin 5 → ℝ) (j k : Fin 5) :
    ricCN (RfG t y) j k = RicG (mu 0 y) (mu 1 y) t j k := by
  obtain ⟨h0, h1, h3, h3', h2⟩ := mu_facts y
  simp only [ricCN, RfG, curvG, Pi.sub_apply, Pi.add_apply, GamGamG ht, DGamG_basis ht, Fin.sum_univ_five]
  generalize mu 0 y = a at *; generalize mu 1 y = b at *
  fin_cases j <;> fin_cases k <;> simp [D1G, D2G, GiG, GamG, RicG] <;> field_simp <;> ring

/-- **Row 83, the open half closed.** THE connection of the squashed `S⁵` has scalar curvature `24 − 4t²` at EVERY
point `y ∈ ℝ⁵` of the chart, contracted with the inverse metric there. -/
theorem row83_squashed_S5_everywhere {t : ℝ} (ht : t ≠ 0) (y : Fin 5 → ℝ) :
    scalG (GiG (mu 0 y) (mu 1 y) t) (fun i j k l => curv (lcConn (Fin 5 → ℝ) (ndOf (formG (GS t))
      (formG_symm (GS_symm t)) (fun y u h => GS_nondeg ht y u h) ((formG_smooth (GS_smooth t)).differentiable (by simp))))
      (fun _ => Pi.single i 1) (fun _ => Pi.single j 1) (fun _ => Pi.single k 1) y l) = 24 - 4 * t ^ 2 := by
  have h : (fun i j k l => curv (lcConn (Fin 5 → ℝ) (ndOf (formG (GS t)) (formG_symm (GS_symm t))
      (fun y u h => GS_nondeg ht y u h) ((formG_smooth (GS_smooth t)).differentiable (by simp))))
      (fun _ => (Pi.single i 1 : Fin 5 → ℝ)) (fun _ => Pi.single j 1) (fun _ => Pi.single k 1) y l) = RfG t y := by
    funext i j k l
    rw [curvG_eq (GS_symm t) (fun y u h => GS_nondeg ht y u h) (GS_smooth t) (GiG_inv ht y)]
    rfl
  obtain ⟨h0, h1, h3, h3', h2⟩ := mu_facts y
  rw [h, scalG]
  simp only [RicG_tab ht, Fin.sum_univ_five]
  generalize mu 0 y = a at *; generalize mu 1 y = b at *
  simp [GiG, RicG]
  field_simp
  ring

end SquashedS5

/-! ## Campaign 15 (`r7367+71.5`): row 17's half — SdS's Kretschmann scalar AT the Nariai horizon point

The ingoing Eddington–Finkelstein chart `−F(r) dv² + 2 dv dr + P(r)(dθ² + S(θ) dφ²)`, coordinates `(v, r, θ, φ)`.
Its determinant is `−P²S`, so it is nondegenerate for EVERY `F`, including where `F = 0`, which is where the static
chart `−F dt² + dr²/F` fails. THE connection's curvature comes through `curvG_eq` with the inverse given only at the
point. The Kretschmann scalar `R^a_{dbc} R_a^{dbc}` is contracted through two `256`-entry tables (`RE`, `RUE`), so the
eight-index sum is never expanded. The tables were generated by `r7367_71_campaign15/gen_ef_tables.py` (committed),
and every entry is checked here. -/

section EFNariai

set_option synthInstance.maxHeartbeats 400000

open Filter Topology

/-- Numeric coefficient matrices: `G = eF·F + eO + eP·P + eQ·P·S`. -/
def eF : Fin 4 → Fin 4 → ℝ := ![![-1, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]]
def eO : Fin 4 → Fin 4 → ℝ := ![![0, 1, 0, 0], ![1, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]]
def eP : Fin 4 → Fin 4 → ℝ := ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 1, 0], ![0, 0, 0, 0]]
def eQ : Fin 4 → Fin 4 → ℝ := ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 1]]

/-- **The ingoing Eddington–Finkelstein metric** `−F dv² + 2 dv dr + P(dθ² + S dφ²)`. -/
noncomputable def GE (F P S : ℝ → ℝ) (i j : Fin 4) (y : Fin 4 → ℝ) : ℝ :=
  eF i j * F (y 1) + eO i j + eP i j * P (y 1) + eQ i j * (P (y 1) * S (y 2))

lemma GE_symm (F P S : ℝ → ℝ) (i j : Fin 4) (y : Fin 4 → ℝ) : GE F P S i j y = GE F P S j i y := by
  fin_cases i <;> fin_cases j <;> simp [GE, eF, eO, eP, eQ]

variable {F P S : ℝ → ℝ} (hF : ContDiff ℝ ∞ F) (hP : ContDiff ℝ ∞ P) (hS : ContDiff ℝ ∞ S)

include hF hP hS in
lemma GE_smooth (i j : Fin 4) : ContDiff ℝ ∞ (GE F P S i j) :=
  (((contDiff_const.mul (hF.comp (contDiff_apply ℝ ℝ 1))).add contDiff_const).add
    (contDiff_const.mul (hP.comp (contDiff_apply ℝ ℝ 1)))).add
    (contDiff_const.mul ((hP.comp (contDiff_apply ℝ ℝ 1)).mul (hS.comp (contDiff_apply ℝ ℝ 2))))

include hF hP hS in
lemma GE_fd1 (i j : Fin 4) (y v : Fin 4 → ℝ) :
    fderiv ℝ (GE F P S i j) y v = eF i j * (deriv F (y 1) * v 1) + eP i j * (deriv P (y 1) * v 1)
      + eQ i j * (deriv P (y 1) * v 1 * S (y 2) + P (y 1) * (deriv S (y 2) * v 2)) := by
  have h := (((((fd_coord_i (n := 4) 1 ((hF.differentiable (by simp)) (y 1))).const_mul (eF i j)).add_const
    (eO i j)).add ((fd_coord_i (n := 4) 1 ((hP.differentiable (by simp)) (y 1))).const_mul (eP i j))).add
    (((fd_coord_i (n := 4) 1 ((hP.differentiable (by simp)) (y 1))).mul
      (fd_coord_i (n := 4) 2 ((hS.differentiable (by simp)) (y 2)))).const_mul (eQ i j)))
  have h' : HasFDerivAt (GE F P S i j) _ y := h
  rw [h'.fderiv]
  simp; ring

include hF hP hS in
lemma GE_fd2 (i j : Fin 4) (p u v : Fin 4 → ℝ) :
    fderiv ℝ (fderiv ℝ (GE F P S i j)) p u v = eF i j * (deriv (deriv F) (p 1) * u 1 * v 1)
      + eP i j * (deriv (deriv P) (p 1) * u 1 * v 1)
      + eQ i j * (deriv (deriv P) (p 1) * u 1 * v 1 * S (p 2) + deriv P (p 1) * v 1 * (deriv S (p 2) * u 2)
        + deriv P (p 1) * u 1 * (deriv S (p 2) * v 2) + P (p 1) * (deriv (deriv S) (p 2) * u 2 * v 2)) := by
  have dF := fun s => ((contDiff_infty_iff_deriv.1 hF).2.differentiable (by simp)) s
  have dP := fun s => ((contDiff_infty_iff_deriv.1 hP).2.differentiable (by simp)) s
  have dS := fun s => ((contDiff_infty_iff_deriv.1 hS).2.differentiable (by simp)) s
  have P0 := fun s => (hP.differentiable (by simp)) s
  have S0 := fun s => (hS.differentiable (by simp)) s
  rw [d2_of (F := GE F P S i j) (GE_smooth hF hP hS i j) (fun y => GE_fd1 hF hP hS i j y v)
    (((((fd_coord_i (n := 4) 1 (dF _)).mul_const (v 1)).const_mul (eF i j)).add
      (((fd_coord_i (n := 4) 1 (dP _)).mul_const (v 1)).const_mul (eP i j))).add
      (((((fd_coord_i (n := 4) 1 (dP _)).mul_const (v 1)).mul (fd_coord_i (n := 4) 2 (S0 _))).add
        ((fd_coord_i (n := 4) 1 (P0 _)).mul ((fd_coord_i (n := 4) 2 (dS _)).mul_const (v 2)))).const_mul (eQ i j)))]
  simp; ring

/-- Nondegenerate at every point for EVERY `F`: the `(v, r)` block `[[−F, 1], [1, 0]]` has determinant `−1`. -/
lemma GE_nondeg (hP0 : ∀ s, P s ≠ 0) (hS0 : ∀ s, S s ≠ 0) (y u : Fin 4 → ℝ) (h : ∀ v, formG (GE F P S) y u v = 0) :
    u = 0 := by
  have e : ∀ c : Fin 4, formG (GE F P S) y u (Pi.single c 1) = ∑ i, GE F P S i c y * u i := fun c => by
    rw [formG_apply]; simp [Pi.single_apply, mul_comm]
  have h1 := (e 1).symm.trans (h _); have h0 := (e 0).symm.trans (h _)
  have h2 := (e 2).symm.trans (h _); have h3 := (e 3).symm.trans (h _)
  simp [Fin.sum_univ_four, GE, eF, eO, eP, eQ] at h0 h1 h2 h3
  have hp := hP0 (y 1); have hs := hS0 (y 2)
  have hu0 : u 0 = 0 := by simpa using h1
  have hu1 : u 1 = 0 := by rw [hu0] at h0; linarith
  have hu2 : u 2 = 0 := by simp_all
  have hu3 : u 3 = 0 := by simp_all
  ext k; fin_cases k <;> simp [hu0, hu1, hu2, hu3]

/-- The inverse at the point, with `F0 = F(r)`, `P = r²`, `S = s²`; and the tables, checked below. -/
noncomputable def GiE (F0 F1 F2 r s c : ℝ) : Fin 4 → Fin 4 → ℝ :=
  ![![(0), (1), (0), (0)], ![(1), (F0), (0), (0)], ![(0), (0), ((1/r^2)), (0)], ![(0), (0), (0), (1/(r^2*s^2))]]
noncomputable def D1E (F0 F1 F2 r s c : ℝ) : Fin 4 → Fin 4 → Fin 4 → ℝ :=
  ![![![(0), (-F1), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (2*r), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (2*r*s^2), (2*c*r^2*s), (0)]]]
noncomputable def D2E (F0 F1 F2 r s c : ℝ) : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ :=
  ![![![![(0), (0), (0), (0)], ![(0), (-F2), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]]], ![![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]]], ![![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (2), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]]], ![![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (2*s^2), (4*c*r*s), (0)], ![(0), (4*c*r*s), (-2*r^2*(-c + s)*(c + s)), (0)], ![(0), (0), (0), (0)]]]]
noncomputable def GamE (F0 F1 F2 r s c : ℝ) : Fin 4 → Fin 4 → Fin 4 → ℝ :=
  ![![![(F1/2), (F0*F1/2), (0), (0)], ![(0), (-F1/2), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (-F1/2), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (1/r), (0)], ![(0), (0), (0), (1/r)]], ![![(0), (0), (0), (0)], ![(0), (0), (1/r), (0)], ![(-r), (-F0*r), (0), (0)], ![(0), (0), (0), (c/s)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (1/r)], ![(0), (0), (0), (c/s)], ![(-r*s^2), (-F0*r*s^2), (-c*s), (0)]]]
noncomputable def RE (F0 F1 F2 r s c : ℝ) : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ :=
  ![![![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(-F2/2), (-F0*F2/2), (0), (0)], ![(0), (F2/2), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (-F0*F1/(2*r)), (0)], ![(0), (0), (F1/(2*r)), (0)], ![(-F1*r/2), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (-F0*F1/(2*r))], ![(0), (0), (0), (F1/(2*r))], ![(0), (0), (0), (0)], ![(-F1*r*s^2/2), (0), (0), (0)]]], ![![![(F2/2), (F0*F2/2), (0), (0)], ![(0), (-F2/2), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (F1/(2*r)), (0)], ![(0), (0), (0), (0)], ![(0), (-F1*r/2), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (F1/(2*r))], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (-F1*r*s^2/2), (0), (0)]]], ![![![(0), (0), (F0*F1/(2*r)), (0)], ![(0), (0), (-F1/(2*r)), (0)], ![(F1*r/2), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (-F1/(2*r)), (0)], ![(0), (0), (0), (0)], ![(0), (F1*r/2), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (F0 - 1)], ![(0), (0), (-s^2*(F0 - 1)), (0)]]], ![![![(0), (0), (0), (F0*F1/(2*r))], ![(0), (0), (0), (-F1/(2*r))], ![(0), (0), (0), (0)], ![(F1*r*s^2/2), (0), (0), (0)]], ![![(0), (0), (0), (-F1/(2*r))], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (F1*r*s^2/2), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (1 - F0)], ![(0), (0), (s^2*(F0 - 1)), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]]]]
noncomputable def RUE (F0 F1 F2 r s c : ℝ) : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ :=
  ![![![![(0), (0), (0), (0)], ![(-F2/2), (-F0*F2/2), (0), (0)], ![(0), (0), (-F1/(2*r^3)), (0)], ![(0), (0), (0), (-F1/(2*r^3*s^2))]], ![![(F2/2), (F0*F2/2), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (F1/(2*r^3)), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (F1/(2*r^3*s^2))], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]]], ![![![(0), (0), (0), (0)], ![(0), (F2/2), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (-F2/2), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (-F1/(2*r^3)), (0)], ![(0), (0), (0), (-F1/(2*r^3*s^2))]], ![![(0), (0), (0), (0)], ![(0), (0), (F1/(2*r^3)), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (F1/(2*r^3*s^2))], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]]], ![![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (F1/(2*r)), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(F1/(2*r)), (F0*F1/(2*r)), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (-F1/(2*r)), (0), (0)], ![(-F1/(2*r)), (-F0*F1/(2*r)), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (-(F0 - 1)/(r^4*s^2))]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), ((F0 - 1)/(r^4*s^2))], ![(0), (0), (0), (0)]]], ![![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (F1/(2*r)), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(F1/(2*r)), (F0*F1/(2*r)), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), ((F0 - 1)/r^4), (0)]], ![![(0), (-F1/(2*r)), (0), (0)], ![(-F1/(2*r)), (-F0*F1/(2*r)), (0), (0)], ![(0), (0), (-(F0 - 1)/r^4), (0)], ![(0), (0), (0), (0)]]]]


section EFTables

variable {p : Fin 4 → ℝ} (hPv : P (p 1) = p 1 ^ 2) (hP1 : deriv P (p 1) = 2 * p 1) (hP2 : deriv (deriv P) (p 1) = 2)
  (hSv : S (p 2) = Real.sin (p 2) ^ 2) (hS1 : deriv S (p 2) = 2 * Real.sin (p 2) * Real.cos (p 2))
  (hS2 : deriv (deriv S) (p 2) = 2 * Real.cos (p 2) ^ 2 - 2 * Real.sin (p 2) ^ 2)
  (hr : p 1 ≠ 0) (hs : Real.sin (p 2) ≠ 0)

include hPv hSv hr hs in
lemma GiE_inv (m k : Fin 4) : ∑ l, GE F P S m l p * GiE (F (p 1)) (deriv F (p 1)) (deriv (deriv F) (p 1)) (p 1)
    (Real.sin (p 2)) (Real.cos (p 2)) l k = if m = k then 1 else 0 := by
  fin_cases m <;> fin_cases k <;> simp [Fin.sum_univ_four, GE, eF, eO, eP, eQ, GiE, hPv, hSv] <;> field_simp <;> ring

/-- The tables at a point `p`, from the profile's point values. -/
noncomputable def GiP (F : ℝ → ℝ) (p : Fin 4 → ℝ) := GiE (F (p 1)) (deriv F (p 1)) (deriv (deriv F) (p 1)) (p 1)
  (Real.sin (p 2)) (Real.cos (p 2))
noncomputable def D1P (F : ℝ → ℝ) (p : Fin 4 → ℝ) := D1E (F (p 1)) (deriv F (p 1)) (deriv (deriv F) (p 1)) (p 1)
  (Real.sin (p 2)) (Real.cos (p 2))
noncomputable def D2P (F : ℝ → ℝ) (p : Fin 4 → ℝ) := D2E (F (p 1)) (deriv F (p 1)) (deriv (deriv F) (p 1)) (p 1)
  (Real.sin (p 2)) (Real.cos (p 2))
noncomputable def GamP (F : ℝ → ℝ) (p : Fin 4 → ℝ) := GamE (F (p 1)) (deriv F (p 1)) (deriv (deriv F) (p 1)) (p 1)
  (Real.sin (p 2)) (Real.cos (p 2))
noncomputable def RP (F : ℝ → ℝ) (p : Fin 4 → ℝ) := RE (F (p 1)) (deriv F (p 1)) (deriv (deriv F) (p 1)) (p 1)
  (Real.sin (p 2)) (Real.cos (p 2))
noncomputable def RUP (F : ℝ → ℝ) (p : Fin 4 → ℝ) := RUE (F (p 1)) (deriv F (p 1)) (deriv (deriv F) (p 1)) (p 1)
  (Real.sin (p 2)) (Real.cos (p 2))

set_option maxHeartbeats 0 in
include hF hP hS hPv hP1 hSv hS1 in
lemma D1E_tab (i j c : Fin 4) : dG1 (GE F P S) p i j (Pi.single c 1) = D1P F p i j c := by
  rw [dG1, GE_fd1 hF hP hS, hPv, hP1, hSv, hS1]
  fin_cases i <;> fin_cases j <;> fin_cases c <;> simp [eF, eP, eQ, D1P, D1E] <;> ring

set_option maxHeartbeats 0 in
include hF hP hS hPv hP1 hP2 hSv hS1 hS2 in
lemma D2E_tab (i j a c : Fin 4) :
    dG2 (GE F P S) p i j (Pi.single a 1) (Pi.single c 1) = D2P F p i j a c := by
  rw [dG2, GE_fd2 hF hP hS, hPv, hP1, hP2, hSv, hS1, hS2]
  fin_cases i <;> fin_cases j <;> fin_cases a <;> fin_cases c <;> simp [eF, eP, eQ, D2P, D2E] <;> ring

set_option maxHeartbeats 0 in
include hF hP hS hPv hP1 hSv hS1 hr hs in
lemma GamE_tab (i j k : Fin 4) : gamG (GE F P S) (GiP F p) p (Pi.single i 1) (Pi.single j 1) k = GamP F p i j k := by
  simp only [gamG, kosG_basis, D1E_tab hF hP hS hPv hP1 hSv hS1, Fin.sum_univ_four]
  fin_cases i <;> fin_cases j <;> fin_cases k <;> simp [D1P, D1E, GiP, GiE, GamP, GamE] <;> field_simp <;> ring

include hF hP hS hPv hP1 hP2 hSv hS1 hS2 hr hs in
lemma DGamE_basis (u i j k : Fin 4) :
    DgamG (GE F P S) (GiP F p) p (Pi.single u 1) (Pi.single i 1) (Pi.single j 1) k
      = ∑ l, ((D2P F p j l u i + D2P F p l i u j - D2P F p i j u l) / 2
        - ∑ m, D1P F p m l u * GamP F p i j m) * GiP F p l k := by
  simp only [DgamG, DkosG_basis, D2E_tab hF hP hS hPv hP1 hP2 hSv hS1 hS2,
    D1E_tab hF hP hS hPv hP1 hSv hS1, GamE_tab hF hP hS hPv hP1 hSv hS1 hr hs]

include hF hP hS hPv hP1 hSv hS1 hr hs in
lemma GamGamE (hP0 : ∀ s, P s ≠ 0) (hS0 : ∀ s, S s ≠ 0) (i j k l : Fin 4) :
    gamG (GE F P S) (GiP F p) p (Pi.single i 1) (gamG (GE F P S) (GiP F p) p (Pi.single j 1) (Pi.single k 1)) l
      = ∑ c, GamP F p j k c * GamP F p i c l := by
  have hinv : ∀ m k, ∑ l, GE F P S m l p * GiP F p l k = if m = k then 1 else 0 := GiE_inv hPv hSv hr hs
  rw [gamG_right (fun y u h => GE_nondeg hP0 hS0 y u h) (GE_smooth hF hP hS) hinv]
  simp only [GamE_tab hF hP hS hPv hP1 hSv hS1 hr hs]

/-- THE connection's curvature array at `p` in the EF chart, on coordinate fields. -/
noncomputable def RfE (F P S : ℝ → ℝ) (p : Fin 4 → ℝ) (i j k l : Fin 4) : ℝ :=
  curvG (GE F P S) (GiP F p) p (Pi.single i 1) (Pi.single j 1) (Pi.single k 1) l

set_option maxHeartbeats 0 in
include hF hP hS hPv hP1 hP2 hSv hS1 hS2 hr hs in
lemma RE_tab (hP0 : ∀ s, P s ≠ 0) (hS0 : ∀ s, S s ≠ 0) (i j k l : Fin 4) : RfE F P S p i j k l = RP F p i j k l := by
  simp only [RfE, curvG, Pi.sub_apply, Pi.add_apply, GamGamE hF hP hS hPv hP1 hSv hS1 hr hs hP0 hS0,
    DGamE_basis hF hP hS hPv hP1 hP2 hSv hS1 hS2 hr hs, Fin.sum_univ_four]
  fin_cases i <;> fin_cases j <;> fin_cases k <;> fin_cases l <;>
    simp [D1P, D1E, D2P, D2E, GiP, GiE, GamP, GamE, RP, RE] <;> field_simp <;> (try ring) <;> simp

set_option maxHeartbeats 0 in
include hPv hSv hr hs in
lemma RUE_tab (a b c d : Fin 4) : ∑ e, GE F P S a e p * ∑ f, ∑ g, ∑ h,
    GiP F p b f * GiP F p c g * GiP F p d h * RP F p f g h e = RUP F p a b c d := by
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases d <;>
    simp [Fin.sum_univ_four, GE, eF, eO, eP, eQ, hPv, hSv, GiP, GiE, RP, RE, RUP, RUE] <;> field_simp <;> ring

/-- The Kretschmann contraction `R^a_{dbc} R_a^{dbc}`: lower with `G` at `p`, raise with `Gi`. -/
noncomputable def kretG (G : Fin 4 → Fin 4 → (Fin 4 → ℝ) → ℝ) (Gi : Fin 4 → Fin 4 → ℝ)
    (Rf : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ) (p : Fin 4 → ℝ) : ℝ :=
  ∑ a, ∑ b, ∑ c, ∑ d, Rf b c d a * ∑ e, G a e p * ∑ f, ∑ g, ∑ h, Gi b f * Gi c g * Gi d h * Rf f g h e

set_option maxHeartbeats 0 in
include hPv hSv hr hs in
lemma kret_tab : kretG (GE F P S) (GiP F p) (RP F p) p
    = deriv (deriv F) (p 1) ^ 2 + 4 * deriv F (p 1) ^ 2 / p 1 ^ 2 + 4 * (1 - F (p 1)) ^ 2 / p 1 ^ 4 := by
  simp only [kretG, RUE_tab hPv hSv hr hs]
  simp [Fin.sum_univ_four, RP, RE, RUP, RUE]
  field_simp; ring

end EFTables

/-- `sin²` and its two derivatives at `θ`. -/
lemma sin2_ef {S : ℝ → ℝ} {θ : ℝ} (eS : S =ᶠ[𝓝 θ] fun s => Real.sin s ^ 2) :
    S θ = Real.sin θ ^ 2 ∧ deriv S θ = 2 * Real.sin θ * Real.cos θ ∧
      deriv (deriv S) θ = 2 * Real.cos θ ^ 2 - 2 * Real.sin θ ^ 2 := by
  have sd : ∀ s, HasDerivAt (fun s => Real.sin s ^ 2) (2 * Real.sin s * Real.cos s) s := fun s =>
    (show HasDerivAt (fun s => Real.sin s ^ 2) _ s from (Real.hasDerivAt_sin s).pow 2).congr_deriv (by norm_num)
  refine ⟨eS.eq_of_nhds, by rw [eS.deriv_eq, (sd _).deriv], ?_⟩
  rw [(eS.deriv.trans (Eventually.of_forall fun s => (sd s).deriv) :
    deriv S =ᶠ[𝓝 θ] fun s => 2 * Real.sin s * Real.cos s).deriv_eq,
    (show HasDerivAt (fun s => 2 * Real.sin s * Real.cos s) _ θ from
      ((Real.hasDerivAt_sin θ).const_mul 2).mul (Real.hasDerivAt_cos θ)).deriv]
  ring

include hF hP hS in
/-- **Row 17's half: THE connection's Kretschmann scalar in the ingoing EF chart**, for ANY smooth `F`, vanishing at
the point or not, with `P = r²` and `S = sin²θ` near it: `K = F″² + 4F′²/r² + 4(1 − F)²/r⁴`. The chart is nondegenerate
where `F = 0`, so this holds AT a horizon. -/
theorem ef_kretschmann (hP0 : ∀ s, P s ≠ 0) (hS0 : ∀ s, S s ≠ 0) (p : Fin 4 → ℝ)
    (eP : P =ᶠ[𝓝 (p 1)] fun s => s ^ 2) (eS : S =ᶠ[𝓝 (p 2)] fun s => Real.sin s ^ 2) :
    kretG (GE F P S) (GiP F p) (fun i j k l => curv (lcConn (Fin 4 → ℝ) (ndOf (formG (GE F P S))
      (formG_symm (GE_symm F P S)) (fun y u h => GE_nondeg hP0 hS0 y u h)
      ((formG_smooth (GE_smooth hF hP hS)).differentiable (by simp))))
      (fun _ => (Pi.single i 1 : Fin 4 → ℝ)) (fun _ => Pi.single j 1) (fun _ => Pi.single k 1) p l) p
    = deriv (deriv F) (p 1) ^ 2 + 4 * deriv F (p 1) ^ 2 / p 1 ^ 2 + 4 * (1 - F (p 1)) ^ 2 / p 1 ^ 4 := by
  have hPv : P (p 1) = p 1 ^ 2 := eP.eq_of_nhds
  have hP1 : deriv P (p 1) = 2 * p 1 := by rw [eP.deriv_eq]; simp
  have hP2 : deriv (deriv P) (p 1) = 2 := by
    rw [(eP.deriv.trans (Eventually.of_forall fun s => by simp) : deriv P =ᶠ[𝓝 (p 1)] fun s => 2 * s).deriv_eq]
    simp
  obtain ⟨hSv, hS1, hS2⟩ := sin2_ef eS
  have hr : p 1 ≠ 0 := fun h => hP0 (p 1) (by rw [hPv, h]; simp)
  have hs : Real.sin (p 2) ≠ 0 := fun h => hS0 (p 2) (by rw [hSv, h]; simp)
  have h : (fun i j k l => curv (lcConn (Fin 4 → ℝ) (ndOf (formG (GE F P S))
      (formG_symm (GE_symm F P S)) (fun y u h => GE_nondeg hP0 hS0 y u h)
      ((formG_smooth (GE_smooth hF hP hS)).differentiable (by simp))))
      (fun _ => (Pi.single i 1 : Fin 4 → ℝ)) (fun _ => Pi.single j 1) (fun _ => Pi.single k 1) p l) = RP F p := by
    funext i j k l
    rw [curvG_eq (GE_symm F P S) (fun y u h => GE_nondeg hP0 hS0 y u h) (GE_smooth hF hP hS)
      (GiE_inv hPv hSv hr hs)]
    exact RE_tab hF hP hS hPv hP1 hP2 hSv hS1 hS2 hr hs hP0 hS0 i j k l
  rw [h]
  exact kret_tab hPv hSv hr hs

omit hF hP hS in
/-- SdS's profile `F = 1 − 2M/r − r²/α²` near `r ≠ 0`: the closed form is `48M²/r⁶ + 24/α⁴` there, at a horizon or
not. -/
theorem sds_kretschmann_ef (M α : ℝ) (hα : α ≠ 0) {r : ℝ} (hr : r ≠ 0)
    (eF : F =ᶠ[𝓝 r] fun s => 1 - 2 * M / s - s ^ 2 / α ^ 2) :
    deriv (deriv F) r ^ 2 + 4 * deriv F r ^ 2 / r ^ 2 + 4 * (1 - F r) ^ 2 / r ^ 4 = 48 * M ^ 2 / r ^ 6 + 24 / α ^ 4 ∧
      F r = 1 - 2 * M / r - r ^ 2 / α ^ 2 ∧ deriv F r = 2 * M / r ^ 2 - 2 * r / α ^ 2 := by
  have hd : ∀ s, s ≠ 0 → HasDerivAt (fun s => 1 - 2 * M / s - s ^ 2 / α ^ 2) (2 * M / s ^ 2 - 2 * s / α ^ 2) s :=
    fun s hs => by
      have := ((hasDerivAt_const s (1 : ℝ)).sub ((hasDerivAt_inv hs).const_mul (2 * M))).sub
        ((hasDerivAt_pow 2 s).div_const (α ^ 2))
      convert this using 1
      · ext t; simp [div_eq_mul_inv]
      · field_simp; ring
  have e1 : deriv F =ᶠ[𝓝 r] fun s => 2 * M / s ^ 2 - 2 * s / α ^ 2 :=
    eF.deriv.trans ((eventually_ne_nhds hr).mono fun s hs => (hd s hs).deriv)
  have h2 : HasDerivAt (fun s => 2 * M / s ^ 2 - 2 * s / α ^ 2) (-4 * M / r ^ 3 - 2 / α ^ 2) r := by
    have := ((((hasDerivAt_pow 2 r).inv (pow_ne_zero 2 hr)).const_mul (2 * M)).sub
      ((hasDerivAt_id r).const_mul (2 / α ^ 2)))
    convert this using 1
    · ext t; simp [div_eq_mul_inv]; ring
    · field_simp; ring
  have v0 : F r = 1 - 2 * M / r - r ^ 2 / α ^ 2 := eF.eq_of_nhds
  have v1 : deriv F r = 2 * M / r ^ 2 - 2 * r / α ^ 2 := e1.eq_of_nhds
  have v2 : deriv (deriv F) r = -4 * M / r ^ 3 - 2 / α ^ 2 := by rw [e1.deriv_eq, h2.deriv]
  refine ⟨?_, v0, v1⟩
  rw [v0, v1, v2]
  field_simp; ring

omit hF hP hS in
/-- **The Nariai point.** At `α² = 27M²` the two horizons merge at `r_N = 3M` (`= α/√3`): `F(r_N) = F′(r_N) = 0`, the
static chart's `1/F` is singular there, and the EF chart's `K` is `72/α⁴`, the receipt's value. -/
theorem nariai_horizon_kretschmann (M α : ℝ) (hM : M ≠ 0) (hα2 : α ^ 2 = 27 * M ^ 2)
    (eF : F =ᶠ[𝓝 (3 * M)] fun s => 1 - 2 * M / s - s ^ 2 / α ^ 2) :
    F (3 * M) = 0 ∧ deriv F (3 * M) = 0 ∧
      deriv (deriv F) (3 * M) ^ 2 + 4 * deriv F (3 * M) ^ 2 / (3 * M) ^ 2 + 4 * (1 - F (3 * M)) ^ 2 / (3 * M) ^ 4
        = 72 / α ^ 4 := by
  have hα : α ≠ 0 := fun h => hM (by nlinarith [sq_nonneg M, h ▸ hα2])
  have h3 : (3 * M) ≠ 0 := mul_ne_zero three_ne_zero hM
  obtain ⟨hK, v0, v1⟩ := sds_kretschmann_ef M α hα h3 eF
  have hα4 : α ^ 4 = 729 * M ^ 4 := by rw [show α ^ 4 = (α ^ 2) ^ 2 by ring, hα2]; ring
  refine ⟨?_, ?_, ?_⟩
  · rw [v0, hα2]; field_simp; ring
  · rw [v1, hα2]; field_simp; ring
  · rw [hK, hα4]; field_simp; ring

end EFNariai

end ShadowProbe

#print axioms ShadowProbe.lcGam_formG
#print axioms ShadowProbe.fderiv_lcGam_formG
#print axioms ShadowProbe.curvG_eq
#print axioms ShadowProbe.GS_nondeg
#print axioms ShadowProbe.GiS_inv
#print axioms ShadowProbe.D2_tab
#print axioms ShadowProbe.Ric_tab
#print axioms ShadowProbe.row83_squashed_S5
#print axioms ShadowProbe.GiG_inv
#print axioms ShadowProbe.D2G_tab
#print axioms ShadowProbe.RicG_tab
#print axioms ShadowProbe.row83_squashed_S5_everywhere
#print axioms ShadowProbe.GE_nondeg
#print axioms ShadowProbe.RE_tab
#print axioms ShadowProbe.RUE_tab
#print axioms ShadowProbe.ef_kretschmann
#print axioms ShadowProbe.sds_kretschmann_ef
#print axioms ShadowProbe.nariai_horizon_kretschmann

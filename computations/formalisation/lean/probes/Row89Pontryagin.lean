import ShadowEngine
import Mathlib.LinearAlgebra.Matrix.Permutation
import Mathlib.LinearAlgebra.Matrix.Kronecker
import Mathlib.Analysis.SpecialFunctions.SmoothTransition

/-! # Campaign 44 (`r7443+71.32`): row 89, the constituent count is conserved on every static member and the twist
alone violates it

Pre-registered at `computations/formalisation/r7443_71_campaign44/PREDICTION.md`. The receipt is
`P14_the_constituent_count_is_conserved_on_every_static_member_and_the_twist_alone_violates_it.py`.

**Copied (probes cannot import probes).** The engine section `EngineG`, row 69's core (`eps4`, `pontArr`,
`pontryaginLC`, `pontryaginLC_eq`), row 96's recipe and parity framework (`GamF`, `RiemF`, `pontryagin_parity`,
`tabs_bridge`, `rho`) and campaign 43's transgression (`transgression`, `ratio_neg_one`), verbatim up to the
pontryagin-only `tabs_bridge`. New here: the 2-jet calculus `HasJ` (sum, product, inverse, exponential rules), which
turns a metric's entries into the recipe's first- and second-partial tables.

**What is proved.**
* *Part 1, Kerr* (symbolic `M` and `a`). `KerrExt M a` is Boyer–Lindquist Kerr with `u = cos θ` (the receipt's
  `kerr_bl`) on the open region `KU M` (`r > 2|M| + 2`, `|u| < 5/16`), and a smooth nondegenerate metric on all of
  `ℝ⁴` (clamped profiles `rK`, `qK`). `kerr_pontryagin`: there `*RR = −96M²a r u(3r² − a²u²)(r² − 3a²u²)/Σ⁶`
  (`kerrClosed`), from sympy tables proved layer by layer. `kerrClosed_odd`, `kerr_odd`: odd in `a`. The receipt's three
  spins at `M = 1`: `kerr_receipt_odd`, `kerr_receipt_zero`, `kerr_receipt_ne`. `kerr_psi2`: `kerrClosed = −48 Im Ψ₂²`,
  `Ψ₂ = −M/(r − iau)³`. `kerr_static_zero`: `a = 0` gives `*RR ≡ 0` everywhere, structurally (Part 5's lemma).
* *Part 2.* `baryon_charge`, `diquark_charge`, `meson_charge`, `seat_charge`, `trivial_charge`: the generator
  `(d/dθ)ρ(V(θ))|₀ / i` of `Λ³`, `Λ²` (2×2 minors), `V ⊗ V̄` (Kronecker), `V`, trivial is `3, 2, 0, 1, 0` times `1`;
  `eig_scalar`: a generator `q·1` has the single eigenvalue `q`.
* *Part 3.* `wall_content` … `turnaround_lift`: the linear traces `3, 0, 1`, and the convention sign flip.
* *Part 4.* `local_residual`, `local_residual_ne`, `global_residual`; `clifford` (the receipt's Dirac matrices);
  `dirac_fixes` (the Dirac equation fixes `∂₀Ψ`); `div_onShell` (`∂_μ(Ψ̄γ^μΨ) = 0` on shell, all 32 real unknowns and
  `m`); `div_offShell`, `div_offShell_ne` (off shell `2 Re⟨δ, Ψ⟩`, nonzero); `density_count` (`j⁰ = Σ|Ψᵢ|²`).
* *Part 5.* `static_pontryagin_zero`: `g_{tj} = 0` and `∂_t g = 0` give `*RR ≡ 0` (row 96's parity lemma with `k = t`).
  `static_f_zero`, `static_fhS_zero`, `static_weyl_zero`, `static_named_zero`: the receipt's three static families and
  its named members, all profiles arbitrary.
* *Part 6.* `gowdy_pontryagin`: for the unpolarised Gowdy form with `A, ψ, ω, R` ARBITRARY smooth functions of `(t, z)`,
  `*RR = 4e^{2ψ}(WLin + e^{4ψ}WCub)/(e^{4A}R³|R|)`, `WLin` linear and `WCub` cubic in `ω`'s derivatives, no bare `ω`.
  `gowdy_grading`: `ω → εω` gives `ε·gLin + ε³·gCub`; `grading_exact`: both are nonzero on the member, so the powers
  are exactly `{1, 3}`. `gowdy_twist_odd`: `*RR(−ω) = −*RR(ω)`. `gowdy_const_twist`: `*RR ≡ 0` at constant `ω`.
  `gowdy_shift`: bare `ω` never appears. The member `(t/3, z/5, ctz, t)`: `member_pontryagin`, `member_odd`,
  `member_zero`, `member_ne`.
* *Part 8.* `member_transgression`, `member_ratio` (`∂_μK^μ/(√−g *RR) = −1`, from campaign 43's `ratio_neg_one`),
  `member_divK_ne`, `member_divK_odd`.

**Caveats.** The density and the current are the receipt's coordinate formulas on THE Levi-Civita connection of the
coordinate metric on `ℝ⁴`; the engine needs a metric smooth and nondegenerate everywhere, so `sin²θ`, `r²` and the
singular Kerr and Gowdy profiles enter as global profiles that agree with the receipt's where it evaluates (`KU`;
`t > 3/2` for the member, `R = rho(t)`). Imported: the anomaly normalisation `1/384π²` and the representation
semantics. The paper-text checks (Part 7) are not formalised. -/

set_option linter.unusedTactic false
set_option linter.unnecessarySeqFocus false
set_option linter.unusedSimpArgs false
set_option linter.unusedSectionVars false
set_option linter.unusedVariables false
set_option linter.unreachableTactic false
set_option linter.style.longLine false
set_option linter.style.setOption false
set_option linter.flexible false
-- the engine section is copied verbatim from `NonDiag.lean`, deprecated lemma names included
set_option linter.deprecated false
-- this linter walks the info tree of every term, and on the long table literals it alone takes minutes
set_option linter.constructorNameAsVariable false
set_option maxHeartbeats 1000000000
set_option maxRecDepth 200000
-- elaborate one declaration at a time: the table layers in parallel exceed the memory budget
set_option Elab.async false

open Bundle Manifold Filter Set VectorField
open scoped ContDiff Manifold Topology

namespace ShadowProbe

namespace R89Pontryagin

/-! ## The engine (copied from `probes/NonDiag.lean`, section `EngineG`, since probes cannot import probes) -/

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

/-! ## The core: the Levi-Civita symbol and the Pontryagin density -/

section Core

/-- **The `Fin 4` Levi-Civita symbol**, `ε₀₁₂₃ = +1`: the product of the signs of the six differences
`(n − m)(r − m)(s − m)(r − n)(s − n)(s − r)`. It is `0` on a repeated index and the sign of the permutation otherwise
(checked by `decide +kernel` in `esum_perm`'s uses). -/
def eps4 (m n r s : Fin 4) : ℤ :=
  Int.sign ((n.val : ℤ) - m.val) * Int.sign ((r.val : ℤ) - m.val) * Int.sign ((s.val : ℤ) - m.val)
    * Int.sign ((r.val : ℤ) - n.val) * Int.sign ((s.val : ℤ) - n.val) * Int.sign ((s.val : ℤ) - r.val)

/-- On a permutation, `eps4` is `Equiv.Perm.sign`. -/
theorem eps4_sign : ∀ σ : Equiv.Perm (Fin 4), eps4 (σ 0) (σ 1) (σ 2) (σ 3) = Equiv.Perm.sign σ := by
  decide +kernel

/-- **The receipt's `EPS`**: `EPS[perm] = det` of the matrix with a `1` at `(i, perm i)`, i.e. the permutation
matrix; that determinant is `eps4`. -/
theorem eps4_det (σ : Equiv.Perm (Fin 4)) : (σ.permMatrix ℤ).det = eps4 (σ 0) (σ 1) (σ 2) (σ 3) := by
  rw [Matrix.det_permutation, eps4_sign]
  norm_cast

/-- The contraction against `eps4` is the signed sum over the `24` permutations (the receipt's `EPS.items()` loop). -/
theorem sum_eps (f : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ) :
    ∑ m, ∑ n, ∑ r, ∑ s, (eps4 m n r s : ℝ) * f m n r s =
      f 0 1 2 3 - f 0 1 3 2 - f 0 2 1 3 + f 0 2 3 1 + f 0 3 1 2 - f 0 3 2 1 - f 1 0 2 3 + f 1 0 3 2 + f 1 2 0 3 - f 1 2 3 0 - f 1 3 0 2 + f 1 3 2 0 + f 2 0 1 3 - f 2 0 3 1 - f 2 1 0 3 + f 2 1 3 0 + f 2 3 0 1 - f 2 3 1 0 - f 3 0 1 2 + f 3 0 2 1 + f 3 1 0 2 - f 3 1 2 0 - f 3 2 0 1 + f 3 2 1 0 := by
  simp [Fin.sum_univ_four, eps4, show Int.sign 2 = 1 from rfl, show Int.sign 3 = 1 from rfl]
  ring1

/-- `R_{mnab} = Σₛ g_{ms} R^s_{nab}`, with `R^s_{nab} = Rf a b n s`. -/
def lowR (g : Matrix (Fin 4) (Fin 4) ℝ) (Rf : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ) (m n a b : Fin 4) : ℝ :=
  ∑ s, g m s * Rf a b n s

/-- `R_{mn}{}^{ab} = Σ_{αβ} g^{aα} g^{bβ} R_{mnαβ}`. -/
def raiseR (g gi : Matrix (Fin 4) (Fin 4) ℝ) (Rf : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ) (m n a b : Fin 4) : ℝ :=
  ∑ α, ∑ β, gi a α * gi b β * lowR g Rf m n α β

/-- **The Pontryagin density's coordinate formula**, the receipt's `pontryagin`:
`*RR = ½ Σ_{mnrs} ε^{mnrs} Σ_{ab} R_{mnab} R_{rs}{}^{ab} / √(−det g)`. -/
noncomputable def pontArr (g gi : Matrix (Fin 4) (Fin 4) ℝ) (Rf : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ) : ℝ :=
  (1 / 2) * (∑ m, ∑ n, ∑ r, ∑ s, (eps4 m n r s : ℝ) * ∑ a, ∑ b, lowR g Rf m n a b * raiseR g gi Rf r s a b)
    / Real.sqrt (-g.det)

/-- The metric matrix `Gᵢⱼ(p)`. -/
def gm (G : Fin 4 → Fin 4 → (Fin 4 → ℝ) → ℝ) (p : Fin 4 → ℝ) : Matrix (Fin 4) (Fin 4) ℝ := Matrix.of fun i j => G i j p

/-- **THE Levi-Civita connection's curvature array** of `Σ Gᵢⱼ dxᵢ dxⱼ` at `p`, on coordinate fields:
`riemLC i j k l = (R(∂ᵢ, ∂ⱼ)∂ₖ)ˡ = Rˡ_{kij}`, with `R(X,Y)Z = ∇_X∇_Y Z − ∇_Y∇_X Z − ∇_{[X,Y]}Z` (engine's `curv`). -/
noncomputable def riemLC (G : Fin 4 → Fin 4 → (Fin 4 → ℝ) → ℝ) (hs : ∀ i j p, G i j p = G j i p)
    (hn : ∀ p (u : Fin 4 → ℝ), (∀ v, formG G p u v = 0) → u = 0) (hGs : ∀ i j, ContDiff ℝ ∞ (G i j))
    (p : Fin 4 → ℝ) (i j k l : Fin 4) : ℝ :=
  curv (lcConn (Fin 4 → ℝ) (ndOf (formG G) (formG_symm hs) hn ((formG_smooth hGs).differentiable (by simp))))
    (fun _ => (Pi.single i 1 : Fin 4 → ℝ)) (fun _ => Pi.single j 1) (fun _ => Pi.single k 1) p l

/-- **The Pontryagin density of a coordinate metric** at `p`: `pontArr` with `g = G(p)`, `gi = G(p)⁻¹` and THE
connection's curvature. -/
noncomputable def pontryaginLC (G : Fin 4 → Fin 4 → (Fin 4 → ℝ) → ℝ) (hs : ∀ i j p, G i j p = G j i p)
    (hn : ∀ p (u : Fin 4 → ℝ), (∀ v, formG G p u v = 0) → u = 0) (hGs : ∀ i j, ContDiff ℝ ∞ (G i j))
    (p : Fin 4 → ℝ) : ℝ :=
  pontArr (gm G p) (gm G p)⁻¹ (riemLC G hs hn hGs p)

/-- A right inverse at the point is the matrix inverse. -/
lemma gm_inv {G : Fin 4 → Fin 4 → (Fin 4 → ℝ) → ℝ} {p : Fin 4 → ℝ} {Gi : Fin 4 → Fin 4 → ℝ}
    (hinv : ∀ m k, ∑ l, G m l p * Gi l k = if m = k then 1 else 0) : (gm G p)⁻¹ = Matrix.of Gi := by
  refine Matrix.inv_eq_right_inv ?_
  ext m k
  simp only [Matrix.mul_apply, gm, Matrix.of_apply, hinv m k, Matrix.one_apply]

/-- **The bridge** (row 69's). The density is the receipt's coordinate recipe: `pontArr` on the engine's closed form
`curvG`, with the inverse given only at the point. -/
theorem pontryaginLC_eq {G : Fin 4 → Fin 4 → (Fin 4 → ℝ) → ℝ} (hs : ∀ i j p, G i j p = G j i p)
    (hn : ∀ p (u : Fin 4 → ℝ), (∀ v, formG G p u v = 0) → u = 0) (hGs : ∀ i j, ContDiff ℝ ∞ (G i j))
    {p : Fin 4 → ℝ} {Gi : Fin 4 → Fin 4 → ℝ} (hinv : ∀ m k, ∑ l, G m l p * Gi l k = if m = k then 1 else 0) :
    pontryaginLC G hs hn hGs p = pontArr (gm G p) (Matrix.of Gi)
      (fun i j k l => curvG G Gi p (Pi.single i 1) (Pi.single j 1) (Pi.single k 1) l) := by
  have h : riemLC G hs hn hGs p = fun i j k l => curvG G Gi p (Pi.single i 1) (Pi.single j 1) (Pi.single k 1) l := by
    funext i j k l
    rw [riemLC, curvG_eq hs hn hGs hinv]
  rw [pontryaginLC, gm_inv hinv, h]

end Core

/-! ## The coordinate recipe on tables, and the Chern–Simons current -/

section Recipe

set_option synthInstance.maxHeartbeats 400000

/-- `Γᵏᵢⱼ = Σ_l ½(∂ᵢ g_jl + ∂ⱼ g_li − ∂_l g_ij) g^{lk}`, from the first partials `d1 i j c = ∂_c g_ij` and an inverse
`gi` (the receipt's `christoffels`). -/
noncomputable def GamF (d1 : Fin 4 → Fin 4 → Fin 4 → ℝ) (gi : Fin 4 → Fin 4 → ℝ) (i j k : Fin 4) : ℝ :=
  ∑ l, (d1 j l i + d1 l i j - d1 i j l) / 2 * gi l k

/-- `∂ᵤ Γᵏᵢⱼ = Σ_l (½(∂ᵤ∂ᵢ g_jl + ∂ᵤ∂ⱼ g_li − ∂ᵤ∂_l g_ij) − Σₘ ∂ᵤ g_ml Γᵐᵢⱼ) g^{lk}`, from `d2 i j a c = ∂_a∂_c g_ij`. -/
noncomputable def DGamF (d1 : Fin 4 → Fin 4 → Fin 4 → ℝ) (d2 : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ) (gi : Fin 4 → Fin 4 → ℝ)
    (u i j k : Fin 4) : ℝ :=
  ∑ l, ((d2 j l u i + d2 l i u j - d2 i j u l) / 2 - ∑ m, d1 m l u * GamF d1 gi i j m) * gi l k

/-- `Rˡ_{kij} = ∂ᵢΓˡⱼₖ − ∂ⱼΓˡᵢₖ + Γᶜⱼₖ Γˡᵢc − Γᶜᵢₖ Γˡⱼc`, stored as `RiemF i j k l`. -/
noncomputable def RiemF (d1 : Fin 4 → Fin 4 → Fin 4 → ℝ) (d2 : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ) (gi : Fin 4 → Fin 4 → ℝ)
    (i j k l : Fin 4) : ℝ :=
  DGamF d1 d2 gi i j k l - DGamF d1 d2 gi j i k l + ∑ c, GamF d1 gi j k c * GamF d1 gi i c l
    - ∑ c, GamF d1 gi i k c * GamF d1 gi j c l

/-- The metric's first and second coordinate partials at `p`. -/
noncomputable def d1At (G : Fin 4 → Fin 4 → (Fin 4 → ℝ) → ℝ) (p : Fin 4 → ℝ) (i j c : Fin 4) : ℝ :=
  dG1 G p i j (Pi.single c 1)
noncomputable def d2At (G : Fin 4 → Fin 4 → (Fin 4 → ℝ) → ℝ) (p : Fin 4 → ℝ) (i j a c : Fin 4) : ℝ :=
  dG2 G p i j (Pi.single a 1) (Pi.single c 1)

lemma gamG_basis (G : Fin 4 → Fin 4 → (Fin 4 → ℝ) → ℝ) (Gi : Fin 4 → Fin 4 → ℝ) (p : Fin 4 → ℝ) (i j k : Fin 4) :
    gamG G Gi p (Pi.single i 1) (Pi.single j 1) k = GamF (d1At G p) Gi i j k := by
  simp only [gamG, kosG_basis, GamF, d1At]

lemma DgamG_basis (G : Fin 4 → Fin 4 → (Fin 4 → ℝ) → ℝ) (Gi : Fin 4 → Fin 4 → ℝ) (p : Fin 4 → ℝ) (u i j k : Fin 4) :
    DgamG G Gi p (Pi.single u 1) (Pi.single i 1) (Pi.single j 1) k = DGamF (d1At G p) (d2At G p) Gi u i j k := by
  simp only [DgamG, DkosG_basis, gamG_basis, DGamF, d1At, d2At]

/-- The inverse matrix at `p`, as an array. -/
noncomputable def gmi (G : Fin 4 → Fin 4 → (Fin 4 → ℝ) → ℝ) (p : Fin 4 → ℝ) : Fin 4 → Fin 4 → ℝ :=
  fun l k => (gm G p)⁻¹ l k

lemma of_gmi (G : Fin 4 → Fin 4 → (Fin 4 → ℝ) → ℝ) (p : Fin 4 → ℝ) : Matrix.of (gmi G p) = (gm G p)⁻¹ := rfl

variable {G : Fin 4 → Fin 4 → (Fin 4 → ℝ) → ℝ}

/-- Nondegeneracy of the form makes the matrix invertible. -/
lemma gm_det_ne (hn : ∀ p (u : Fin 4 → ℝ), (∀ v, formG G p u v = 0) → u = 0) (p : Fin 4 → ℝ) :
    (gm G p).det ≠ 0 := by
  intro h
  obtain ⟨v, hv0, hv⟩ := Matrix.exists_vecMul_eq_zero_iff.2 h
  refine hv0 (hn p v fun w => ?_)
  have hj : ∀ j, ∑ i, v i * G i j p = 0 := fun j => by
    have := congrFun hv j
    simpa [Matrix.vecMul, dotProduct, gm] using this
  rw [formG_apply, Finset.sum_comm]
  exact Finset.sum_eq_zero fun j _ => by
    rw [show ∑ i, G i j p * (v i * w j) = (∑ i, v i * G i j p) * w j by
      rw [Finset.sum_mul]; exact Finset.sum_congr rfl fun _ _ => by ring, hj, zero_mul]

lemma gm_hinv (hn : ∀ p (u : Fin 4 → ℝ), (∀ v, formG G p u v = 0) → u = 0) (p : Fin 4 → ℝ) (m k : Fin 4) :
    ∑ l, G m l p * gmi G p l k = if m = k then 1 else 0 := by
  have h := congrFun (congrFun (Matrix.mul_nonsing_inv (gm G p) (isUnit_iff_ne_zero.2 (gm_det_ne hn p))) m) k
  simpa [Matrix.mul_apply, gm, gmi, Matrix.one_apply] using h

variable (hs : ∀ i j p, G i j p = G j i p) (hn : ∀ p (u : Fin 4 → ℝ), (∀ v, formG G p u v = 0) → u = 0)
  (hGs : ∀ i j, ContDiff ℝ ∞ (G i j))

include hn hGs in
/-- THE connection's curvature array is the table recipe on the metric's partials. -/
theorem riemLC_tab (p : Fin 4 → ℝ) :
    riemLC G hs hn hGs p = RiemF (d1At G p) (d2At G p) (gmi G p) := by
  funext i j k l
  have hinv := gm_hinv hn p
  rw [riemLC, curvG_eq hs hn hGs hinv]
  simp only [curvG, Pi.sub_apply, Pi.add_apply, DgamG_basis, RiemF]
  rw [gamG_right hn hGs hinv (Pi.single i 1), gamG_right hn hGs hinv (Pi.single j 1)]
  simp only [gamG_basis]

/-- **THE connection's Christoffel symbols** at `y`: `chrLC … y i j k = (∇_{∂ᵢ} ∂ⱼ)ᵏ = Γᵏᵢⱼ`, the engine's `lcConn`
of `Σ Gᵢⱼ dxᵢ dxⱼ` on coordinate fields. -/
noncomputable def chrLC (G : Fin 4 → Fin 4 → (Fin 4 → ℝ) → ℝ) (hs : ∀ i j p, G i j p = G j i p)
    (hn : ∀ p (u : Fin 4 → ℝ), (∀ v, formG G p u v = 0) → u = 0) (hGs : ∀ i j, ContDiff ℝ ∞ (G i j))
    (y : Fin 4 → ℝ) (i j k : Fin 4) : ℝ :=
  (show Fin 4 → ℝ from lcConn (Fin 4 → ℝ) (ndOf (formG G) (formG_symm hs) hn ((formG_smooth hGs).differentiable (by simp)))
    (fun _ => (Pi.single j 1 : Fin 4 → ℝ)) y (Pi.single i 1)) k

/-- **The Chern–Simons current's coordinate formula**, the receipt's `cs_current`:
`K^μ = 2 Σ ε^{μνρσ} (Σ_{ab} Γᵃ_{νb} ∂_ρ Γᵇ_{σa} + ⅔ Σ_{abc} Γᵃ_{νb} Γᵇ_{ρc} Γᶜ_{σa})`, with `Γ i j k = Γᵏᵢⱼ` and
`DΓ u i j k = ∂ᵤ Γᵏᵢⱼ`. -/
noncomputable def csArr (Γ : Fin 4 → Fin 4 → Fin 4 → ℝ) (DΓ : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ) (μ : Fin 4) : ℝ :=
  2 * ∑ ν, ∑ ρ, ∑ σ, (eps4 μ ν ρ σ : ℝ) *
    (∑ a, ∑ b, Γ ν b a * DΓ ρ σ a b + 2 / 3 * ∑ a, ∑ b, ∑ c, Γ ν b a * Γ ρ c b * Γ σ a c)

/-- **The Chern–Simons current of a coordinate metric** at `p`: `csArr` on THE connection's Christoffel symbols
`chrLC` and their coordinate partials `∂ᵤ` at `p` (Fréchet derivatives of `y ↦ chrLC … y i j k`). -/
noncomputable def csLC (G : Fin 4 → Fin 4 → (Fin 4 → ℝ) → ℝ) (hs : ∀ i j p, G i j p = G j i p)
    (hn : ∀ p (u : Fin 4 → ℝ), (∀ v, formG G p u v = 0) → u = 0) (hGs : ∀ i j, ContDiff ℝ ∞ (G i j))
    (p : Fin 4 → ℝ) (μ : Fin 4) : ℝ :=
  csArr (chrLC G hs hn hGs p) (fun u i j k => fderiv ℝ (fun y => chrLC G hs hn hGs y i j k) p (Pi.single u 1)) μ

include hn hGs in
lemma chrLC_eq (y : Fin 4 → ℝ) (i j k : Fin 4) :
    chrLC G hs hn hGs y i j k = lcGam (formG G) y (Pi.single i 1) (Pi.single j 1) k := by
  rw [chrLC, lcConn_const (formG_symm hs) hn]

lemma d2At_symm (hGs : ∀ i j, ContDiff ℝ ∞ (G i j)) (p : Fin 4 → ℝ) (i j a c : Fin 4) :
    d2At G p i j a c = d2At G p i j c a :=
  (hGs i j).contDiffAt.isSymmSndFDerivAt (by simp) _ _

end Recipe

/-! ## Parity: a coordinate the metric does not depend on, and that does not mix -/

section Parity

/-- The parity of the number of indices of `l` in the set `P`. -/
def pb (P : Fin 4 → Bool) : List (Fin 4) → Bool
  | [] => false
  | i :: l => xor (P i) (pb P l)

/-- **Parity of the tables at a point**: every entry with an odd number of `P`-indices vanishes. -/
structure TabPar (P : Fin 4 → Bool) (g gi : Fin 4 → Fin 4 → ℝ) (d1 : Fin 4 → Fin 4 → Fin 4 → ℝ)
    (d2 : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ) : Prop where
  g0 : ∀ i j, pb P [i, j] = true → g i j = 0
  gi0 : ∀ i j, pb P [i, j] = true → gi i j = 0
  d10 : ∀ i j c, pb P [i, j, c] = true → d1 i j c = 0
  d20 : ∀ i j a c, pb P [i, j, a, c] = true → d2 i j a c = 0

variable {P : Fin 4 → Bool} {g gi : Fin 4 → Fin 4 → ℝ} {d1 : Fin 4 → Fin 4 → Fin 4 → ℝ}
  {d2 : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ}

lemma GamF_par (T : TabPar P g gi d1 d2) {i j k : Fin 4} (h : pb P [i, j, k] = true) : GamF d1 gi i j k = 0 := by
  refine Finset.sum_eq_zero fun l _ => ?_
  by_cases hl : pb P [l, k] = true
  · rw [T.gi0 _ _ hl, mul_zero]
  · have e : pb P [j, l, i] = true ∧ pb P [l, i, j] = true ∧ pb P [i, j, l] = true := by
      revert h hl; simp only [pb, Bool.xor_false]
      cases P i <;> cases P j <;> cases P k <;> cases P l <;> decide
    rw [T.d10 _ _ _ e.1, T.d10 _ _ _ e.2.1, T.d10 _ _ _ e.2.2]; ring

lemma DGamF_par (T : TabPar P g gi d1 d2) {u i j k : Fin 4} (h : pb P [u, i, j, k] = true) :
    DGamF d1 d2 gi u i j k = 0 := by
  refine Finset.sum_eq_zero fun l _ => ?_
  by_cases hl : pb P [l, k] = true
  · rw [T.gi0 _ _ hl, mul_zero]
  · have e : pb P [j, l, u, i] = true ∧ pb P [l, i, u, j] = true ∧ pb P [i, j, u, l] = true := by
      revert h hl; simp only [pb, Bool.xor_false]
      cases P u <;> cases P i <;> cases P j <;> cases P k <;> cases P l <;> decide
    have hs : ∑ m, d1 m l u * GamF d1 gi i j m = 0 := Finset.sum_eq_zero fun m _ => by
      by_cases hm : pb P [m, l, u] = true
      · rw [T.d10 _ _ _ hm, zero_mul]
      · have : pb P [i, j, m] = true := by
          revert h hl hm; simp only [pb, Bool.xor_false]
          cases P u <;> cases P i <;> cases P j <;> cases P k <;> cases P l <;> cases P m <;> decide
        rw [GamF_par T this, mul_zero]
    rw [T.d20 _ _ _ _ e.1, T.d20 _ _ _ _ e.2.1, T.d20 _ _ _ _ e.2.2, hs]; ring

lemma RiemF_par (T : TabPar P g gi d1 d2) {i j k l : Fin 4} (h : pb P [i, j, k, l] = true) :
    RiemF d1 d2 gi i j k l = 0 := by
  have h2 : pb P [j, i, k, l] = true := by
    revert h; simp only [pb, Bool.xor_false]; cases P i <;> cases P j <;> cases P k <;> cases P l <;> decide
  have hs : ∀ a b, pb P [a, b, k, l] = true →
      ∑ c, GamF d1 gi b k c * GamF d1 gi a c l = 0 := fun a b hab => Finset.sum_eq_zero fun c _ => by
    by_cases hc : pb P [b, k, c] = true
    · rw [GamF_par T hc, zero_mul]
    · have : pb P [a, c, l] = true := by
        revert hab hc; simp only [pb, Bool.xor_false]
        cases P a <;> cases P b <;> cases P k <;> cases P l <;> cases P c <;> decide
      rw [GamF_par T this, mul_zero]
  rw [RiemF, DGamF_par T h, DGamF_par T h2, hs i j h, hs j i h2]; ring

lemma lowR_par (hg : ∀ i j, pb P [i, j] = true → g i j = 0) {Rf : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ}
    (hR : ∀ i j k l, pb P [i, j, k, l] = true → Rf i j k l = 0) {m n a b : Fin 4} (h : pb P [m, n, a, b] = true) :
    lowR g Rf m n a b = 0 := by
  refine Finset.sum_eq_zero fun s _ => ?_
  by_cases hs : pb P [m, s] = true
  · rw [hg _ _ hs, zero_mul]
  · have : pb P [a, b, n, s] = true := by
      revert h hs; simp only [pb, Bool.xor_false]
      cases P m <;> cases P n <;> cases P a <;> cases P b <;> cases P s <;> decide
    rw [hR _ _ _ _ this, mul_zero]

lemma raiseR_par (hg : ∀ i j, pb P [i, j] = true → g i j = 0) (hgi : ∀ i j, pb P [i, j] = true → gi i j = 0)
    {Rf : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ} (hR : ∀ i j k l, pb P [i, j, k, l] = true → Rf i j k l = 0)
    {m n a b : Fin 4} (h : pb P [m, n, a, b] = true) : raiseR g gi Rf m n a b = 0 := by
  refine Finset.sum_eq_zero fun α _ => Finset.sum_eq_zero fun β _ => ?_
  by_cases ha : pb P [a, α] = true
  · rw [hgi _ _ ha]; ring
  by_cases hb : pb P [b, β] = true
  · rw [hgi _ _ hb]; ring
  have : pb P [m, n, α, β] = true := by
    revert h ha hb; simp only [pb, Bool.xor_false]
    cases P m <;> cases P n <;> cases P a <;> cases P b <;> cases P α <;> cases P β <;> decide
  rw [lowR_par hg hR this, mul_zero]

/-- Where `ε` is nonzero its four indices are `0, 1, 2, 3` in some order. -/
theorem eps4_pb_aux : ∀ b₀ b₁ b₂ b₃ : Bool, ∀ m n r s : Fin 4, eps4 m n r s ≠ 0 →
    pb ![b₀, b₁, b₂, b₃] [m, n, r, s] = pb ![b₀, b₁, b₂, b₃] [0, 1, 2, 3] := by
  decide +kernel

lemma eps4_pb (P : Fin 4 → Bool) {m n r s : Fin 4} (h : eps4 m n r s ≠ 0) :
    pb P [m, n, r, s] = pb P [0, 1, 2, 3] := by
  have e : P = ![P 0, P 1, P 2, P 3] := by funext i; fin_cases i <;> rfl
  rw [e]; exact eps4_pb_aux _ _ _ _ m n r s h

/-- **The density vanishes** when the tables have `P`-parity and `P` holds an odd number of the four coordinates. -/
theorem pontArr_par (hg : ∀ i j, pb P [i, j] = true → g i j = 0) (hgi : ∀ i j, pb P [i, j] = true → gi i j = 0)
    {Rf : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ} (hR : ∀ i j k l, pb P [i, j, k, l] = true → Rf i j k l = 0)
    (h0 : pb P [0, 1, 2, 3] = true) : pontArr (Matrix.of g) (Matrix.of gi) Rf = 0 := by
  have : ∑ m, ∑ n, ∑ r, ∑ s, (eps4 m n r s : ℝ) *
      ∑ a, ∑ b, lowR (Matrix.of g) Rf m n a b * raiseR (Matrix.of g) (Matrix.of gi) Rf r s a b = 0 := by
    refine Finset.sum_eq_zero fun m _ => Finset.sum_eq_zero fun n _ => Finset.sum_eq_zero fun r _ =>
      Finset.sum_eq_zero fun s _ => ?_
    by_cases he : eps4 m n r s = 0
    · simp [he]
    have hp := eps4_pb P he
    rw [h0] at hp
    rw [Finset.sum_eq_zero fun a _ => Finset.sum_eq_zero fun b _ => ?_, mul_zero]
    by_cases ha : pb P [m, n, a, b] = true
    · rw [lowR_par (g := Matrix.of g) hg hR ha, zero_mul]
    · have : pb P [r, s, a, b] = true := by
        revert hp ha; simp only [pb, Bool.xor_false]
        cases P m <;> cases P n <;> cases P r <;> cases P s <;> cases P a <;> cases P b <;> decide
      rw [raiseR_par (g := Matrix.of g) (gi := Matrix.of gi) hg hgi hR this, mul_zero]
  rw [pontArr, this]; simp

/-- The inverse matrix inherits the parity. -/
lemma inv_par (P : Fin 4 → Bool) (M : Matrix (Fin 4) (Fin 4) ℝ) (h : ∀ i j, pb P [i, j] = true → M i j = 0)
    (i j : Fin 4) (hij : pb P [i, j] = true) : M⁻¹ i j = 0 := by
  set s : Fin 4 → ℝ := fun i => if P i then -1 else 1 with hs
  set D : Matrix (Fin 4) (Fin 4) ℝ := Matrix.diagonal s
  have hss : ∀ i, s i * s i = 1 := fun i => by simp only [hs]; split_ifs <;> norm_num
  have hDD : D * D = 1 := by
    rw [Matrix.diagonal_mul_diagonal]; ext a b; simp [Matrix.one_apply, Matrix.diagonal_apply, hss]
  have hM : D * M * D = M := by
    ext a b
    simp only [D, Matrix.mul_diagonal, Matrix.diagonal_mul]
    by_cases hab : pb P [a, b] = true
    · rw [h a b hab]; ring
    · have : s a * s b = 1 := by
        simp only [hs]; revert hab; simp only [pb, Bool.xor_false]; cases P a <;> cases P b <;> norm_num
      calc s a * M a b * s b = (s a * s b) * M a b := by ring
        _ = M a b := by rw [this, one_mul]
  have hDi : D⁻¹ = D := Matrix.inv_eq_left_inv hDD
  have hMi : M⁻¹ = D * M⁻¹ * D := by
    conv_lhs => rw [← hM]
    rw [Matrix.mul_inv_rev, Matrix.mul_inv_rev, hDi, Matrix.mul_assoc]
  have e := congrFun (congrFun hMi i) j
  simp only [D, Matrix.mul_diagonal, Matrix.diagonal_mul] at e
  have : s i * s j = -1 := by
    simp only [hs]; revert hij; simp only [pb, Bool.xor_false]; cases P i <;> cases P j <;> norm_num
  have : M⁻¹ i j = -M⁻¹ i j := by linear_combination e + M⁻¹ i j * this
  linarith

/-- A function that does not change along `v` has zero derivative along `v`. -/
lemma fderiv_dir_zero {f : (Fin 4 → ℝ) → ℝ} (hf : Differentiable ℝ f) {v : Fin 4 → ℝ}
    (h : ∀ y (c : ℝ), f (y + c • v) = f y) (y : Fin 4 → ℝ) : fderiv ℝ f y v = 0 := by
  have hl : HasDerivAt (fun c : ℝ => y + c • v) v 0 := by
    simpa using ((hasDerivAt_id (0 : ℝ)).smul_const v).const_add y
  have h1 := (hf (y + (0 : ℝ) • v)).hasFDerivAt.comp_hasDerivAt (0 : ℝ) hl
  rw [show (f ∘ fun c : ℝ => y + c • v) = fun _ => f y from funext (h y)] at h1
  simpa using h1.unique (hasDerivAt_const (0 : ℝ) (f y))

variable {G : Fin 4 → Fin 4 → (Fin 4 → ℝ) → ℝ}

lemma d1At_indep (hGs : ∀ i j, ContDiff ℝ ∞ (G i j)) {i j k : Fin 4}
    (h : ∀ y (c : ℝ), G i j (y + c • Pi.single k 1) = G i j y) (p : Fin 4 → ℝ) : d1At G p i j k = 0 :=
  fderiv_dir_zero ((hGs i j).differentiable (by simp)) h p

lemma d2At_indep (hGs : ∀ i j, ContDiff ℝ ∞ (G i j)) {i j k : Fin 4}
    (h : ∀ y (c : ℝ), G i j (y + c • Pi.single k 1) = G i j y) (p : Fin 4 → ℝ) (a : Fin 4) :
    d2At G p i j a k = 0 ∧ d2At G p i j k a = 0 :=
  d2_indep (hGs i j) (fun y => fderiv_dir_zero ((hGs i j).differentiable (by simp)) h y) p (Pi.single a 1)

lemma d1At_zero {i j : Fin 4} (h : ∀ y, G i j y = 0) (p : Fin 4 → ℝ) (c : Fin 4) : d1At G p i j c = 0 := by
  rw [d1At, dG1, show G i j = fun _ => 0 from funext h]; simp

lemma d2At_zero {i j : Fin 4} (h : ∀ y, G i j y = 0) (p : Fin 4 → ℝ) (a c : Fin 4) : d2At G p i j a c = 0 := by
  rw [d2At, dG2, show G i j = fun _ => 0 from funext h]; simp

/-- **The tables of a metric have `P`-parity** when every entry with one index in `P` vanishes identically and the
metric does not depend on the coordinates in `P`. -/
theorem tabPar_of (P : Fin 4 → Bool) (hn : ∀ p (u : Fin 4 → ℝ), (∀ v, formG G p u v = 0) → u = 0)
    (hGs : ∀ i j, ContDiff ℝ ∞ (G i j)) (hz : ∀ i j, pb P [i, j] = true → ∀ y, G i j y = 0)
    (hI : ∀ k, P k = true → ∀ i j y (c : ℝ), G i j (y + c • Pi.single k 1) = G i j y) (p : Fin 4 → ℝ) :
    TabPar P (gm G p) (gmi G p) (d1At G p) (d2At G p) where
  g0 i j h := hz i j h p
  gi0 := inv_par P (gm G p) fun i j h => hz i j h p
  d10 i j c h := by
    by_cases hc : P c = true
    · exact d1At_indep hGs (hI c hc i j) p
    · have : pb P [i, j] = true := by
        revert h hc; simp only [pb, Bool.xor_false]; cases P i <;> cases P j <;> cases P c <;> decide
      exact d1At_zero (hz i j this) p c
  d20 i j a c h := by
    by_cases hc : P c = true
    · exact (d2At_indep hGs (hI c hc i j) p a).1
    by_cases ha : P a = true
    · exact (d2At_indep hGs (hI a ha i j) p c).2
    have : pb P [i, j] = true := by
      revert h hc ha; simp only [pb, Bool.xor_false]; cases P i <;> cases P j <;> cases P a <;> cases P c <;> decide
    exact d2At_zero (hz i j this) p a c

variable (hs : ∀ i j p, G i j p = G j i p) (hn : ∀ p (u : Fin 4 → ℝ), (∀ v, formG G p u v = 0) → u = 0)
  (hGs : ∀ i j, ContDiff ℝ ∞ (G i j))

include hn hGs in
/-- **The parity theorem for the density.** If `G` does not mix the coordinates in `P` with the others and does not
depend on them, and `P` holds an odd number of the four coordinates, THE connection's `*RR` vanishes everywhere. -/
theorem pontryagin_parity (P : Fin 4 → Bool) (hz : ∀ i j, pb P [i, j] = true → ∀ y, G i j y = 0)
    (hI : ∀ k, P k = true → ∀ i j y (c : ℝ), G i j (y + c • Pi.single k 1) = G i j y)
    (h0 : pb P [0, 1, 2, 3] = true) (p : Fin 4 → ℝ) : pontryaginLC G hs hn hGs p = 0 := by
  have T := tabPar_of P hn hGs hz hI p
  rw [pontryaginLC, riemLC_tab hs hn hGs]
  exact pontArr_par (g := gm G p) T.g0 T.gi0 (fun i j k l h => RiemF_par T h) h0

end Parity

section Algebra

open Matrix

/-- Index quadruples. -/
abbrev Q4 := Fin 4 × Fin 4 × Fin 4 × Fin 4

/-- **The `ε`-contraction** `Σ ε^{mnrs} f(m, n, r, s)`. -/
noncomputable def esum (f : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ) : ℝ :=
  ∑ m, ∑ n, ∑ r, ∑ s, (eps4 m n r s : ℝ) * f m n r s

lemma esum_prod (f : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ) :
    esum f = ∑ x : Q4, (eps4 x.1 x.2.1 x.2.2.1 x.2.2.2 : ℝ) * f x.1 x.2.1 x.2.2.1 x.2.2.2 := by
  simp only [esum, Fintype.sum_prod_type]

/-- Reindexing by a permutation `e` of the quadruples on which `ε` picks up the sign `c`. -/
lemma esum_perm (f g : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ) (e : Q4 ≃ Q4) (c : ℤ)
    (hε : ∀ x : Q4, eps4 x.1 x.2.1 x.2.2.1 x.2.2.2 = c * eps4 (e x).1 (e x).2.1 (e x).2.2.1 (e x).2.2.2)
    (hg : ∀ x : Q4, g x.1 x.2.1 x.2.2.1 x.2.2.2 = f (e x).1 (e x).2.1 (e x).2.2.1 (e x).2.2.2) :
    esum g = c * esum f := by
  rw [esum_prod, esum_prod, Finset.mul_sum]
  refine Fintype.sum_equiv e _ _ fun x => ?_
  rw [hε x, hg x]; push_cast; ring

/-- The five reindexings used: `(01)`, `(23)`, `(02)`, the pair swap, the `3`-cycle on `n r s`, the `4`-cycle. -/
lemma esum_sw01 (f : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ) : esum (fun m n r s => f n m r s) = -esum f := by
  have := esum_perm f (fun m n r s => f n m r s)
    ⟨fun x => (x.2.1, x.1, x.2.2), fun x => (x.2.1, x.1, x.2.2), fun _ => rfl, fun _ => rfl⟩ (-1)
    (by decide +kernel) (fun _ => rfl)
  rw [this]; push_cast; ring

lemma esum_sw23 (f : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ) : esum (fun m n r s => f m n s r) = -esum f := by
  have := esum_perm f (fun m n r s => f m n s r)
    ⟨fun x => (x.1, x.2.1, x.2.2.2, x.2.2.1), fun x => (x.1, x.2.1, x.2.2.2, x.2.2.1), fun _ => rfl, fun _ => rfl⟩
    (-1) (by decide +kernel) (fun _ => rfl)
  rw [this]; push_cast; ring

lemma esum_sw02 (f : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ) : esum (fun m n r s => f r n m s) = -esum f := by
  have := esum_perm f (fun m n r s => f r n m s)
    ⟨fun x => (x.2.2.1, x.2.1, x.1, x.2.2.2), fun x => (x.2.2.1, x.2.1, x.1, x.2.2.2), fun _ => rfl, fun _ => rfl⟩
    (-1) (by decide +kernel) (fun _ => rfl)
  rw [this]; push_cast; ring

lemma esum_pair (f : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ) : esum (fun m n r s => f r s m n) = esum f := by
  have := esum_perm f (fun m n r s => f r s m n)
    ⟨fun x => (x.2.2.1, x.2.2.2, x.1, x.2.1), fun x => (x.2.2.1, x.2.2.2, x.1, x.2.1), fun _ => rfl, fun _ => rfl⟩
    1 (by decide +kernel) (fun _ => rfl)
  rw [this]; push_cast; ring

lemma esum_cyc3 (f : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ) : esum (fun m n r s => f m r s n) = esum f := by
  have := esum_perm f (fun m n r s => f m r s n)
    ⟨fun x => (x.1, x.2.2.1, x.2.2.2, x.2.1), fun x => (x.1, x.2.2.2, x.2.1, x.2.2.1), fun _ => rfl, fun _ => rfl⟩
    1 (by decide +kernel) (fun _ => rfl)
  rw [this]; push_cast; ring

lemma esum_cyc4 (f : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ) : esum (fun m n r s => f n r s m) = -esum f := by
  have := esum_perm f (fun m n r s => f n r s m)
    ⟨fun x => (x.2.1, x.2.2.1, x.2.2.2, x.1), fun x => (x.2.2.2, x.1, x.2.1, x.2.2.1), fun _ => rfl, fun _ => rfl⟩
    (-1) (by decide +kernel) (fun _ => rfl)
  rw [this]; push_cast; ring

lemma esum_add (f g : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ) :
    esum (fun m n r s => f m n r s + g m n r s) = esum f + esum g := by
  simp only [esum, mul_add, Finset.sum_add_distrib]

lemma esum_sub (f g : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ) :
    esum (fun m n r s => f m n r s - g m n r s) = esum f - esum g := by
  simp only [esum, mul_sub, Finset.sum_sub_distrib]

lemma esum_smul (c : ℝ) (f : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ) :
    esum (fun m n r s => c * f m n r s) = c * esum f := by
  simp only [esum, Finset.mul_sum]; exact Finset.sum_congr rfl fun _ _ => Finset.sum_congr rfl fun _ _ =>
    Finset.sum_congr rfl fun _ _ => Finset.sum_congr rfl fun _ _ => by ring

lemma esum_congr {f g : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ} (h : ∀ m n r s, f m n r s = g m n r s) :
    esum f = esum g := by
  simp only [esum, h]

/-- A function odd under an odd reindexing has zero contraction. -/
lemma esum_zero_of {f : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ} (h : esum f = -esum f) : esum f = 0 := by linarith

variable (Γ : Fin 4 → Matrix (Fin 4) (Fin 4) ℝ) (dΓ : Fin 4 → Fin 4 → Matrix (Fin 4) (Fin 4) ℝ)
  (ddΓ : Fin 4 → Fin 4 → Fin 4 → Matrix (Fin 4) (Fin 4) ℝ)

/-- **The field strength** `F_{μν} = ∂_μΓ_ν − ∂_νΓ_μ + Γ_μΓ_ν − Γ_νΓ_μ` (`dΓ μ ν = ∂_μΓ_ν`). -/
def Fc (μ ν : Fin 4) : Matrix (Fin 4) (Fin 4) ℝ := dΓ μ ν - dΓ ν μ + Γ μ * Γ ν - Γ ν * Γ μ

/-- **The Chern–Simons form** `CS^μ = Σ ε^{μνρσ} tr(Γ_ν ∂_ρΓ_σ + ⅔ Γ_νΓ_ρΓ_σ)`. -/
noncomputable def CS (μ : Fin 4) : ℝ :=
  ∑ ν, ∑ ρ, ∑ σ, (eps4 μ ν ρ σ : ℝ) * trace (Γ ν * dΓ ρ σ + (2 / 3 : ℝ) • (Γ ν * Γ ρ * Γ σ))

/-- **Its `∂_l`, by the product rule**, with `ddΓ l ρ σ = ∂_l∂_ρΓ_σ`. -/
noncomputable def dCS (l μ : Fin 4) : ℝ :=
  ∑ ν, ∑ ρ, ∑ σ, (eps4 μ ν ρ σ : ℝ) * trace (dΓ l ν * dΓ ρ σ + Γ ν * ddΓ l ρ σ
    + (2 / 3 : ℝ) • (dΓ l ν * Γ ρ * Γ σ + Γ ν * dΓ l ρ * Γ σ + Γ ν * Γ ρ * dΓ l σ))

/-- **The algebraic transgression identity**: for any `Γ`, `∂Γ` and Schwarz-symmetric `∂²Γ`,
`Σ ε^{μνρσ} tr(F_{μν}F_{ρσ}) = 4 Σ_μ ∂_μ CS^μ`. From trace cyclicity, the antisymmetry of `ε` and Schwarz only. -/
theorem transgression_alg (hdd : ∀ a b ν, ddΓ a b ν = ddΓ b a ν) :
    esum (fun m n r s => trace (Fc Γ dΓ m n * Fc Γ dΓ r s)) = 4 * ∑ μ, dCS Γ dΓ ddΓ μ μ := by
  -- the four pieces
  set P : Fin 4 → Fin 4 → Matrix (Fin 4) (Fin 4) ℝ := fun m n => dΓ m n + Γ m * Γ n with hP
  set h : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ := fun m n r s => trace (P m n * P r s) with hh
  set tDD : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ := fun m n r s => trace (dΓ m n * dΓ r s) with htDD
  set tD : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ := fun m n r s => trace (dΓ m n * (Γ r * Γ s)) with htD
  set t4 : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ := fun m n r s => trace (Γ m * Γ n * (Γ r * Γ s)) with ht4
  set tS : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ := fun m n r s => trace (Γ n * ddΓ m r s) with htS
  -- `F_{mn} = P_{mn} − P_{nm}`: four `ε`-equal copies of `tr(P P)`
  have hF : ∀ m n r s, trace (Fc Γ dΓ m n * Fc Γ dΓ r s) = h m n r s - h n m r s - h m n s r + h n m s r := by
    intro m n r s
    have e : ∀ a b, Fc Γ dΓ a b = P a b - P b a := fun a b => by simp only [Fc, hP]; abel
    simp only [hh, e, sub_mul, mul_sub, trace_sub]; ring
  have hL : esum (fun m n r s => trace (Fc Γ dΓ m n * Fc Γ dΓ r s)) = 4 * esum h := by
    rw [esum_congr hF, esum_add, esum_sub, esum_sub, esum_sw01 h, esum_sw23 h,
      esum_sw01 (fun m n r s => h m n s r), esum_sw23 h]; ring
  -- `tr(P P) = tr(∂Γ∂Γ) + 2·tr(∂Γ ΓΓ) + tr(ΓΓΓΓ)` under `ε`
  have hh' : ∀ m n r s, h m n r s = tDD m n r s + tD m n r s + tD r s m n + t4 m n r s := by
    intro m n r s
    simp only [hh, hP, htDD, htD, ht4, add_mul, mul_add, trace_add]
    rw [trace_mul_comm (Γ m * Γ n) (dΓ r s)]; ring
  have h4 : esum t4 = 0 := esum_zero_of (by
    rw [← esum_cyc4 t4]; refine esum_congr fun m n r s => ?_
    simp only [ht4, Matrix.mul_assoc]; rw [trace_mul_comm (Γ m)]; simp only [Matrix.mul_assoc])
  have hLh : esum h = esum tDD + 2 * esum tD := by
    rw [esum_congr hh', esum_add, esum_add, esum_add, esum_pair tD, h4]; ring
  -- the right side
  have hS : esum tS = 0 := esum_zero_of (by
    rw [← esum_sw02 tS]; refine esum_congr fun m n r s => ?_
    simp only [htS, hdd m r s])
  have hR : ∑ μ, dCS Γ dΓ ddΓ μ μ = esum tDD + esum tS + 2 / 3 * (esum tD + esum (fun m n r s => tD m r s n)
      + esum (fun m n r s => tD m s n r)) := by
    have e : ∑ μ, dCS Γ dΓ ddΓ μ μ = esum (fun m n r s => tDD m n r s + tS m n r s
        + 2 / 3 * (tD m n r s + tD m r s n + tD m s n r)) := by
      simp only [dCS, esum]
      refine Finset.sum_congr rfl fun m _ => Finset.sum_congr rfl fun n _ => Finset.sum_congr rfl fun r _ =>
        Finset.sum_congr rfl fun s _ => ?_
      congr 1
      simp only [htDD, htS, htD, trace_add, trace_smul, smul_eq_mul]
      rw [trace_mul_comm (Γ n * dΓ m r) (Γ s), ← Matrix.mul_assoc, trace_mul_comm (Γ s * Γ n),
        trace_mul_comm (Γ n * Γ r) (dΓ m s), Matrix.mul_assoc (dΓ m n)]
    rw [e, esum_add, esum_add, esum_smul, esum_add, esum_add]
  have hc1 : esum (fun m n r s => tD m r s n) = esum tD := esum_cyc3 tD
  have hc2 : esum (fun m n r s => tD m s n r) = esum tD := by
    rw [← esum_cyc3 (fun m n r s => tD m s n r)]
  rw [hL, hLh, hR, hS, hc1, hc2]; ring

end Algebra

/-! ## Layer 2: the bridge to THE connection -/

section Tables

open Matrix

/-! ### The Pontryagin side: pair symmetry of the tabled curvature, and the contraction to `−tr(F F)` -/

variable {g : Matrix (Fin 4) (Fin 4) ℝ} {gi : Fin 4 → Fin 4 → ℝ} {d1 : Fin 4 → Fin 4 → Fin 4 → ℝ}
  {d2 : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ}

/-- The lowered Christoffel symbol `Γ_{l,ij} = ½(∂ᵢg_jl + ∂ⱼg_li − ∂_l g_ij)`: `GamF i j k = Σ_l Kos i j l g^{lk}`. -/
noncomputable def Kos (d1 : Fin 4 → Fin 4 → Fin 4 → ℝ) (i j l : Fin 4) : ℝ := (d1 j l i + d1 l i j - d1 i j l) / 2

/-- `∂ᵤΓᵏᵢⱼ = Σ_l Xf u i j l g^{lk}`. -/
noncomputable def Xf (d1 : Fin 4 → Fin 4 → Fin 4 → ℝ) (d2 : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ) (gi : Fin 4 → Fin 4 → ℝ)
    (u i j l : Fin 4) : ℝ :=
  (d2 j l u i + d2 l i u j - d2 i j u l) / 2 - ∑ m, d1 m l u * GamF d1 gi i j m

lemma GamF_eq (i j k : Fin 4) : GamF d1 gi i j k = ∑ l, Kos d1 i j l * gi l k := rfl
lemma DGamF_eq (u i j k : Fin 4) : DGamF d1 d2 gi u i j k = ∑ l, Xf d1 d2 gi u i j l * gi l k := rfl

/-- `q(x, y, z, w) = Σ_t Γᵗ_{xy} Γ_{t,zw}`. -/
noncomputable def qf (d1 : Fin 4 → Fin 4 → Fin 4 → ℝ) (gi : Fin 4 → Fin 4 → ℝ) (x y z w : Fin 4) : ℝ :=
  ∑ t, GamF d1 gi x y t * Kos d1 z w t

/-- **The lowered curvature in closed form**: `R_{mnab} = ½(∂_a∂_n g_mb − ∂_b∂_n g_ma − ∂_a∂_m g_nb + ∂_b∂_m g_na)
+ q(a,n,b,m) − q(b,n,a,m)` (`d2 i j a c = ∂_a∂_c g_ij`). -/
noncomputable def L1 (d1 : Fin 4 → Fin 4 → Fin 4 → ℝ) (d2 : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ) (gi : Fin 4 → Fin 4 → ℝ)
    (m n a b : Fin 4) : ℝ :=
  (d2 m b a n - d2 b n a m - d2 m a b n + d2 a n b m) / 2 + qf d1 gi a n b m - qf d1 gi b n a m

section Sym
variable (hd1 : ∀ i j c, d1 i j c = d1 j i c) (hd2 : ∀ i j a c, d2 i j a c = d2 j i a c)
  (hd2' : ∀ i j a c, d2 i j a c = d2 i j c a) (hgi : ∀ i j, gi i j = gi j i)

include hd1 in
lemma Kos_symm (i j l : Fin 4) : Kos d1 i j l = Kos d1 j i l := by
  simp only [Kos]; rw [hd1 j l, hd1 l i, hd1 i j]; ring

include hd1 in
lemma qf_12 (x y z w : Fin 4) : qf d1 gi x y z w = qf d1 gi y x z w := by
  simp only [qf, GamF_eq, Kos_symm hd1 x y]

include hd1 in
lemma qf_34 (x y z w : Fin 4) : qf d1 gi x y z w = qf d1 gi x y w z := by
  simp only [qf, Kos_symm hd1 z w]

include hgi in
lemma qf_pair (x y z w : Fin 4) : qf d1 gi x y z w = qf d1 gi z w x y := by
  simp only [qf, GamF_eq, Finset.sum_mul]
  rw [Finset.sum_comm]
  exact Finset.sum_congr rfl fun t _ => Finset.sum_congr rfl fun l _ => by rw [hgi]; ring

include hd2 hgi in
/-- Antisymmetry in the first (fibre) pair: metric compatibility. -/
lemma L1_anti (m n a b : Fin 4) : L1 d1 d2 gi n m a b = -L1 d1 d2 gi m n a b := by
  simp only [L1]
  rw [hd2 n b, hd2 b m, hd2 n a, hd2 a m, qf_pair hgi a m b n, qf_pair hgi b m a n]; ring

include hd1 hd2 hd2' hgi in
/-- **Pair symmetry** `R_{mnab} = R_{abmn}`. -/
lemma L1_pair (m n a b : Fin 4) : L1 d1 d2 gi a b m n = L1 d1 d2 gi m n a b := by
  simp only [L1]
  have e1 := hd2' a n m b
  have e2 : d2 n b m a = d2 b n a m := by rw [hd2, hd2']
  have e3 : d2 a m n b = d2 m a b n := by rw [hd2, hd2']
  have e4 := hd2' m b n a
  have e5 : qf d1 gi m b n a = qf d1 gi a n b m := by
    rw [qf_12 hd1 m b, qf_34 hd1 b m n a, qf_pair hgi b m a n]
  have e6 : qf d1 gi n b m a = qf d1 gi b n a m := by rw [qf_12 hd1 n b, qf_34 hd1 b n m a]
  rw [e1, e2, e3, e4, e5, e6]; ring

end Sym

variable (hc : ∀ m l, ∑ s, g m s * gi l s = if l = m then 1 else 0)

include hc in
lemma contr (Y : Fin 4 → ℝ) (m : Fin 4) : ∑ s, g m s * ∑ l, Y l * gi l s = Y m := by
  calc ∑ s, g m s * ∑ l, Y l * gi l s = ∑ l, Y l * ∑ s, g m s * gi l s := by
        simp only [Finset.mul_sum]; rw [Finset.sum_comm]
        exact Finset.sum_congr rfl fun _ _ => Finset.sum_congr rfl fun _ _ => by ring
    _ = Y m := by simp [hc]

include hc in
/-- **`R_{mnab}` of the table recipe is `L1`**, given `Σₛ g_{ms} g^{ls} = δ`, `∂g` and `∂²g` symmetric. -/
lemma lowR_L1 (hd1 : ∀ i j c, d1 i j c = d1 j i c) (hd2' : ∀ i j a c, d2 i j a c = d2 i j c a) (m n a b : Fin 4) :
    lowR g (RiemF d1 d2 gi) m n a b = L1 d1 d2 gi m n a b := by
  have hR : ∀ s, RiemF d1 d2 gi a b n s = ∑ l, (Xf d1 d2 gi a b n l - Xf d1 d2 gi b a n l
      + ∑ c, GamF d1 gi b n c * Kos d1 a c l - ∑ c, GamF d1 gi a n c * Kos d1 b c l) * gi l s := fun s => by
    have e : ∀ x y, ∑ c, GamF d1 gi x n c * GamF d1 gi y c s
        = ∑ l, (∑ c, GamF d1 gi x n c * Kos d1 y c l) * gi l s := fun x y => by
      simp only [GamF_eq (k := s), Finset.mul_sum, Finset.sum_mul]; rw [Finset.sum_comm]
      exact Finset.sum_congr rfl fun _ _ => Finset.sum_congr rfl fun _ _ => by ring
    rw [RiemF, e, e, DGamF_eq, DGamF_eq]
    simp only [add_mul, sub_mul, Finset.sum_add_distrib, Finset.sum_sub_distrib]
  simp only [lowR, hR]
  rw [contr hc]
  have hK : ∀ x t, d1 t m x = Kos d1 x t m + Kos d1 x m t := fun x t => by
    simp only [Kos]; rw [hd1 m t, hd1 m x, hd1 t x]; ring
  have z : ∀ x y, ∑ c, GamF d1 gi y n c * Kos d1 x c m
      = ∑ t, d1 t m x * GamF d1 gi y n t - qf d1 gi y n x m := fun x y => by
    rw [qf, ← Finset.sum_sub_distrib]; exact Finset.sum_congr rfl fun t _ => by rw [hK]; ring
  simp only [Xf, L1]
  rw [z a b, z b a, hd2' n m a b]; ring

/-- The fibre matrix of the tabled curvature: `(F_{mn})ˡ_k = Rˡ_{kmn} = RiemF m n k l`. -/
noncomputable def Fm (d1 : Fin 4 → Fin 4 → Fin 4 → ℝ) (d2 : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ) (gi : Fin 4 → Fin 4 → ℝ)
    (m n : Fin 4) : Matrix (Fin 4) (Fin 4) ℝ := Matrix.of fun l k => RiemF d1 d2 gi m n k l

lemma gFm (m n a b : Fin 4) : (g * Fm d1 d2 gi a b) m n = lowR g (RiemF d1 d2 gi) m n a b := by
  simp [Fm, lowR, Matrix.mul_apply]

lemma sum_conj (M B : Matrix (Fin 4) (Fin 4) ℝ) (a b : Fin 4) :
    ∑ α, ∑ β, M a α * M b β * B α β = (M * B * Mᵀ) a b := by
  simp only [Matrix.mul_apply, transpose_apply, Finset.sum_mul]
  rw [Finset.sum_comm]
  exact Finset.sum_congr rfl fun _ _ => Finset.sum_congr rfl fun _ _ => by ring

lemma sum_had (A C : Matrix (Fin 4) (Fin 4) ℝ) : ∑ a, ∑ b, A a b * C a b = trace (A * Cᵀ) := by
  simp [trace, Matrix.mul_apply]

include hc in
/-- **The Pontryagin contraction**: `Σ_{ab} R_{mnab} R_{rs}{}^{ab} = −tr(F_{mn}F_{rs})`. -/
lemma pont_contract (hd1 : ∀ i j c, d1 i j c = d1 j i c) (hd2 : ∀ i j a c, d2 i j a c = d2 j i a c)
    (hd2' : ∀ i j a c, d2 i j a c = d2 i j c a) (hgi : ∀ i j, gi i j = gi j i)
    (hgg : Matrix.of gi * g = 1) (m n r s : Fin 4) :
    ∑ a, ∑ b, lowR g (RiemF d1 d2 gi) m n a b * raiseR g (Matrix.of gi) (RiemF d1 d2 gi) r s a b
      = -trace (Fm d1 d2 gi m n * Fm d1 d2 gi r s) := by
  have hpair : ∀ m n a b, lowR g (RiemF d1 d2 gi) m n a b = (g * Fm d1 d2 gi m n) a b := fun m n a b => by
    rw [gFm, lowR_L1 hc hd1 hd2', lowR_L1 hc hd1 hd2', L1_pair hd1 hd2 hd2' hgi]
  have hBt : (g * Fm d1 d2 gi r s)ᵀ = -(g * Fm d1 d2 gi r s) := by
    ext a b
    simp only [transpose_apply, Matrix.neg_apply, gFm]
    rw [lowR_L1 hc hd1 hd2', lowR_L1 hc hd1 hd2', L1_anti hd2 hgi]
  have hR : ∀ a b, raiseR g (Matrix.of gi) (RiemF d1 d2 gi) r s a b
      = (Matrix.of gi * (g * Fm d1 d2 gi r s) * (Matrix.of gi)ᵀ) a b := fun a b => by
    simp only [raiseR, hpair r s]; exact sum_conj _ _ a b
  have hgT : (Matrix.of gi)ᵀ = Matrix.of gi := by ext i j; simp [hgi j i]
  simp only [hpair m n, hR]
  rw [sum_had, transpose_mul, transpose_mul, transpose_transpose, hgT, hBt]
  simp only [Matrix.mul_neg, Matrix.neg_mul, trace_neg, neg_inj, Matrix.mul_assoc]
  rw [← Matrix.mul_assoc (Matrix.of gi) g, hgg, Matrix.one_mul, trace_mul_comm g]
  simp only [Matrix.mul_assoc]
  rw [hgg, Matrix.mul_one]

/-- `ε`-contraction of a negation. -/
lemma esum_neg (f : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ) : esum (fun m n r s => -f m n r s) = -esum f := by
  have := esum_smul (-1) f; simp only [neg_one_mul] at this; exact this

include hc in
/-- **The left side is `−2√−g *RR`**: for tables of a metric with `det g < 0`,
`√(−det g) · pontArr = −½ Σ ε^{mnrs} tr(F_{mn}F_{rs})`. -/
theorem pont_tab (hd1 : ∀ i j c, d1 i j c = d1 j i c) (hd2 : ∀ i j a c, d2 i j a c = d2 j i a c)
    (hd2' : ∀ i j a c, d2 i j a c = d2 i j c a) (hgi : ∀ i j, gi i j = gi j i)
    (hgg : Matrix.of gi * g = 1) (hdet : g.det < 0) :
    Real.sqrt (-g.det) * pontArr g (Matrix.of gi) (RiemF d1 d2 gi)
      = -(1 / 2) * esum (fun m n r s => trace (Fm d1 d2 gi m n * Fm d1 d2 gi r s)) := by
  have hN : (∑ m, ∑ n, ∑ r, ∑ s, (eps4 m n r s : ℝ) *
      ∑ a, ∑ b, lowR g (RiemF d1 d2 gi) m n a b * raiseR g (Matrix.of gi) (RiemF d1 d2 gi) r s a b)
      = -esum (fun m n r s => trace (Fm d1 d2 gi m n * Fm d1 d2 gi r s)) := by
    rw [← esum_neg]; exact esum_congr fun m n r s => pont_contract hc hd1 hd2 hd2' hgi hgg m n r s
  have hs : Real.sqrt (-g.det) ≠ 0 := (Real.sqrt_pos.2 (by linarith)).ne'
  rw [pontArr, hN]; field_simp

end Tables

/-! ### The current side: `csLC = 2 CS`, its derivative, and `F = curv` -/

section Current

open Matrix

/-- Array to fibre matrix: `(matΓ X ν)ᵃ_b = X ν b a`, i.e. `(Γ_ν)ᵃ_b = Γᵃ_{νb}` for `X = chrLC`. -/
def matΓ (X : Fin 4 → Fin 4 → Fin 4 → ℝ) (ν : Fin 4) : Matrix (Fin 4) (Fin 4) ℝ := Matrix.of fun a b => X ν b a

lemma tr2 (X Y : Fin 4 → Fin 4 → Fin 4 → ℝ) (ν σ : Fin 4) :
    trace (matΓ X ν * matΓ Y σ) = ∑ a, ∑ b, X ν b a * Y σ a b := by
  simp [matΓ, trace, Matrix.mul_apply]

lemma tr3 (X Y Z : Fin 4 → Fin 4 → Fin 4 → ℝ) (ν ρ σ : Fin 4) :
    trace (matΓ X ν * matΓ Y ρ * matΓ Z σ) = ∑ a, ∑ b, ∑ c, X ν b a * Y ρ c b * Z σ a c := by
  simp only [matΓ, trace, diag, Matrix.mul_apply, Matrix.of_apply, Finset.sum_mul]
  exact Finset.sum_congr rfl fun _ _ => Finset.sum_comm

/-- **Row 96's current is twice the Chern–Simons form**: `csArr Γ DΓ = 2 CS` with `(Γ_ν)ᵃ_b = Γᵃ_{νb}`. -/
theorem csArr_eq_CS (Γ : Fin 4 → Fin 4 → Fin 4 → ℝ) (DΓ : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ) (μ : Fin 4) :
    csArr Γ DΓ μ = 2 * CS (matΓ Γ) (fun ρ => matΓ (DΓ ρ)) μ := by
  simp only [csArr, CS, trace_add, trace_smul, tr2, tr3, smul_eq_mul]

/-- The product-rule derivative of `csArr`, `Γ' = ∂Γ`, `DΓ' = ∂(∂Γ)` along one direction. -/
noncomputable def csArrD (Γ Γ' : Fin 4 → Fin 4 → Fin 4 → ℝ) (DΓ DΓ' : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ) (μ : Fin 4) : ℝ :=
  2 * ∑ ν, ∑ ρ, ∑ σ, (eps4 μ ν ρ σ : ℝ) * (∑ a, ∑ b, (Γ' ν b a * DΓ ρ σ a b + Γ ν b a * DΓ' ρ σ a b)
    + 2 / 3 * ∑ a, ∑ b, ∑ c, ((Γ' ν b a * Γ ρ c b + Γ ν b a * Γ' ρ c b) * Γ σ a c + Γ ν b a * Γ ρ c b * Γ' σ a c))

lemma csArrD_eq (Γ : Fin 4 → Fin 4 → Fin 4 → ℝ) (DΓ : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ)
    (DD : Fin 4 → Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ) (l μ : Fin 4) :
    csArrD Γ (DΓ l) DΓ (DD l) μ = 2 * dCS (matΓ Γ) (fun ρ => matΓ (DΓ ρ)) (fun l ρ => matΓ (DD l ρ)) l μ := by
  simp only [csArrD, dCS, trace_add, trace_smul, tr2, tr3, smul_eq_mul, add_mul, mul_add, Finset.sum_add_distrib]

/-- A function with a derivative `L` at `p` whose values are `φ`. -/
def HD (f : (Fin 4 → ℝ) → ℝ) (p : Fin 4 → ℝ) (φ : (Fin 4 → ℝ) → ℝ) : Prop :=
  ∃ L : (Fin 4 → ℝ) →L[ℝ] ℝ, HasFDerivAt f L p ∧ ∀ v, L v = φ v

variable {p : Fin 4 → ℝ}

lemma HD.add {f g : (Fin 4 → ℝ) → ℝ} {φ ψ : (Fin 4 → ℝ) → ℝ} (hf : HD f p φ) (hg : HD g p ψ) :
    HD (fun y => f y + g y) p (fun v => φ v + ψ v) := by
  obtain ⟨L, hL, e⟩ := hf; obtain ⟨M, hM, e'⟩ := hg
  exact ⟨_, hL.add hM, fun v => by simp only [ContinuousLinearMap.add_apply, e, e']⟩

lemma HD.mul {f g : (Fin 4 → ℝ) → ℝ} {φ ψ : (Fin 4 → ℝ) → ℝ} (hf : HD f p φ) (hg : HD g p ψ) :
    HD (fun y => f y * g y) p (fun v => φ v * g p + f p * ψ v) := by
  obtain ⟨L, hL, e⟩ := hf; obtain ⟨M, hM, e'⟩ := hg
  exact ⟨_, hL.mul hM, fun v => by
    simp only [ContinuousLinearMap.add_apply, ContinuousLinearMap.smul_apply, smul_eq_mul, e, e']; ring⟩

lemma HD.const_mul (c : ℝ) {f : (Fin 4 → ℝ) → ℝ} {φ : (Fin 4 → ℝ) → ℝ} (hf : HD f p φ) :
    HD (fun y => c * f y) p (fun v => c * φ v) := by
  obtain ⟨L, hL, e⟩ := hf
  exact ⟨_, hL.const_mul c, fun v => by simp only [ContinuousLinearMap.smul_apply, smul_eq_mul, e]⟩

lemma HD.sum {f : Fin 4 → (Fin 4 → ℝ) → ℝ} {φ : Fin 4 → (Fin 4 → ℝ) → ℝ} (h : ∀ i, HD (f i) p (φ i)) :
    HD (fun y => ∑ i, f i y) p (fun v => ∑ i, φ i v) := by
  choose L hL e using h
  exact ⟨_, HasFDerivAt.fun_sum (u := Finset.univ) fun i _ => hL i, fun v => by
    simp only [ContinuousLinearMap.coe_sum', Finset.sum_apply, e]⟩

/-- **The product rule for the current**, on any differentiable `Γ`, `∂Γ`. -/
lemma HD_csArr {c : Fin 4 → Fin 4 → Fin 4 → (Fin 4 → ℝ) → ℝ} {c' : Fin 4 → Fin 4 → Fin 4 → (Fin 4 → ℝ) → ℝ}
    {d d' : Fin 4 → Fin 4 → Fin 4 → Fin 4 → (Fin 4 → ℝ) → ℝ} (hc : ∀ i j k, HD (c i j k) p (c' i j k))
    (hd : ∀ u i j k, HD (d u i j k) p (d' u i j k)) (μ : Fin 4) :
    HD (fun y => csArr (fun i j k => c i j k y) (fun u i j k => d u i j k y) μ) p
      (fun v => csArrD (fun i j k => c i j k p) (fun i j k => c' i j k v) (fun u i j k => d u i j k p)
        (fun u i j k => d' u i j k v) μ) :=
  HD.const_mul _ (HD.sum fun ν => HD.sum fun ρ => HD.sum fun σ => HD.const_mul _ (HD.add
    (HD.sum fun a => HD.sum fun b => HD.mul (hc ν b a) (hd ρ σ a b))
    (HD.const_mul _ (HD.sum fun a => HD.sum fun b => HD.sum fun e =>
      HD.mul (HD.mul (hc ν b a) (hc ρ e b)) (hc σ a e)))))

end Current

/-! ### THE connection -/

section Bridge

open Matrix

set_option synthInstance.maxHeartbeats 400000

variable {G : Fin 4 → Fin 4 → (Fin 4 → ℝ) → ℝ} (hs : ∀ i j p, G i j p = G j i p)
  (hn : ∀ p (u : Fin 4 → ℝ), (∀ v, formG G p u v = 0) → u = 0) (hGs : ∀ i j, ContDiff ℝ ∞ (G i j))

include hn hGs in
lemma chr_smooth (i j k : Fin 4) : ContDiff ℝ ∞ (fun y => chrLC G hs hn hGs y i j k) := by
  have h := ((lcGam_smooth hn (formG_smooth hGs)).clm_apply (contDiff_const (c := (Pi.single i 1 : Fin 4 → ℝ)))).clm_apply
    (contDiff_const (c := (Pi.single j 1 : Fin 4 → ℝ)))
  simp only [chrLC_eq hs hn hGs]
  exact contDiff_pi.1 h k

include hn hGs in
lemma dchr_smooth (u i j k : Fin 4) :
    ContDiff ℝ ∞ (fun y => fderiv ℝ (fun y => chrLC G hs hn hGs y i j k) y (Pi.single u 1)) :=
  ((chr_smooth hs hn hGs i j k).fderiv_right (m := ∞) (by simp)).clm_apply contDiff_const

/-- `∂_l∂_u Γᵏᵢⱼ` at `p`. -/
noncomputable def ddchr (p : Fin 4 → ℝ) (l u i j k : Fin 4) : ℝ :=
  fderiv ℝ (fun y => fderiv ℝ (fun y => chrLC G hs hn hGs y i j k) y (Pi.single u 1)) p (Pi.single l 1)

include hn hGs in
/-- **Schwarz** for THE connection's Christoffel symbols. -/
lemma ddchr_symm (p : Fin 4 → ℝ) (l u i j k : Fin 4) : ddchr hs hn hGs p l u i j k = ddchr hs hn hGs p u l i j k := by
  have h : ∀ v w, fderiv ℝ (fun y => fderiv ℝ (fun y => chrLC G hs hn hGs y i j k) y w) p v
      = fderiv ℝ (fderiv ℝ (fun y => chrLC G hs hn hGs y i j k)) p v w := fun v w => by
    have h2 := ((chr_smooth hs hn hGs i j k).fderiv_right (m := ∞) (by simp)).differentiable (by simp) p
    have hh : HasFDerivAt (fun y => fderiv ℝ (fun y => chrLC G hs hn hGs y i j k) y w)
        ((fderiv ℝ (fderiv ℝ (fun y => chrLC G hs hn hGs y i j k)) p).flip w) p :=
      (h2.hasFDerivAt.clm_apply (hasFDerivAt_const w p)).congr_fderiv (by ext; simp)
    rw [hh.fderiv]; rfl
  simp only [ddchr, h]
  exact (chr_smooth hs hn hGs i j k).contDiffAt.isSymmSndFDerivAt (by simp) _ _

include hn hGs in
lemma HD_csLC (p : Fin 4 → ℝ) (μ : Fin 4) :
    HD (fun y => csLC G hs hn hGs y μ) p (fun v => csArrD (chrLC G hs hn hGs p)
      (fun i j k => fderiv ℝ (fun y => chrLC G hs hn hGs y i j k) p v)
      (fun u i j k => fderiv ℝ (fun y => chrLC G hs hn hGs y i j k) p (Pi.single u 1))
      (fun u i j k => fderiv ℝ (fun y => fderiv ℝ (fun y => chrLC G hs hn hGs y i j k) y (Pi.single u 1)) p v) μ) :=
  HD_csArr (c := fun i j k y => chrLC G hs hn hGs y i j k)
    (d := fun u i j k y => fderiv ℝ (fun y => chrLC G hs hn hGs y i j k) y (Pi.single u 1))
    (fun i j k => ⟨_, ((chr_smooth hs hn hGs i j k).differentiable (by simp) p).hasFDerivAt, fun _ => rfl⟩)
    (fun u i j k => ⟨_, ((dchr_smooth hs hn hGs u i j k).differentiable (by simp) p).hasFDerivAt, fun _ => rfl⟩) μ

/-- `∂Γ` at `p` as an array, `DΓ u i j k = ∂ᵤΓᵏᵢⱼ` (row 96's second argument of `csArr` in `csLC`). -/
noncomputable def dchr (p : Fin 4 → ℝ) (u i j k : Fin 4) : ℝ :=
  fderiv ℝ (fun y => chrLC G hs hn hGs y i j k) p (Pi.single u 1)

include hn hGs in
/-- **The divergence of the current is `2 Σ_μ ∂_μ CS^μ`** on THE connection's `Γ`, `∂Γ`, `∂²Γ`. -/
theorem div_csLC (p : Fin 4 → ℝ) :
    ∑ μ, fderiv ℝ (fun y => csLC G hs hn hGs y μ) p (Pi.single μ 1)
      = 2 * ∑ μ, dCS (matΓ (chrLC G hs hn hGs p)) (fun ρ => matΓ (dchr hs hn hGs p ρ))
          (fun l ρ => matΓ (ddchr hs hn hGs p l ρ)) μ μ := by
  rw [Finset.mul_sum]
  refine Finset.sum_congr rfl fun μ _ => ?_
  obtain ⟨L, hL, e⟩ := HD_csLC hs hn hGs p μ
  rw [hL.fderiv, e]
  exact csArrD_eq (chrLC G hs hn hGs p) (dchr hs hn hGs p) (ddchr hs hn hGs p) μ μ

include hn hGs in
lemma chr_tab (p : Fin 4 → ℝ) : chrLC G hs hn hGs p = GamF (d1At G p) (gmi G p) := by
  funext i j k; rw [chrLC_eq hs hn hGs, lcGam_formG hn hGs (gm_hinv hn p), gamG_basis]

include hn hGs in
lemma dchr_tab (p : Fin 4 → ℝ) : dchr hs hn hGs p = DGamF (d1At G p) (d2At G p) (gmi G p) := by
  have hinv := gm_hinv hn p
  funext u i j k
  have hd : DifferentiableAt ℝ (fun y => lcGam (formG G) y (Pi.single i 1) (Pi.single j 1)) p :=
    ((lcGam_differentiable hn hGs p).clm_apply (differentiableAt_const _)).clm_apply (differentiableAt_const _)
  have hc : HasFDerivAt (fun y => lcGam (formG G) y (Pi.single i 1) (Pi.single j 1) k)
      ((ContinuousLinearMap.proj k).comp (fderiv ℝ (fun y => lcGam (formG G) y (Pi.single i 1) (Pi.single j 1)) p)) p :=
    (ContinuousLinearMap.proj (R := ℝ) (φ := fun _ : Fin 4 => ℝ) k).hasFDerivAt.comp p hd.hasFDerivAt
  simp only [dchr, chrLC_eq hs hn hGs]
  rw [hc.fderiv]
  simp only [ContinuousLinearMap.comp_apply, ContinuousLinearMap.proj_apply]
  rw [fderiv_lcGam_formG hn hGs hinv, DgamG_basis]

include hn hGs in
/-- **`F` is the engine's curvature**: the field strength of `Γ_ν = chrLC`, `∂Γ = dchr` is `riemLC` (`curv` on
coordinate fields): `(F_{mn})ˡ_k = (R(∂_m, ∂_n)∂_k)ˡ`. -/
theorem Fc_eq_curv (p : Fin 4 → ℝ) (m n : Fin 4) :
    Fc (matΓ (chrLC G hs hn hGs p)) (fun ρ => matΓ (dchr hs hn hGs p ρ)) m n
      = Matrix.of fun l k => riemLC G hs hn hGs p m n k l := by
  rw [chr_tab hs hn hGs, dchr_tab hs hn hGs, riemLC_tab hs hn hGs]
  ext l k
  simp only [Fc, matΓ, RiemF, Matrix.add_apply, Matrix.sub_apply, Matrix.mul_apply, Matrix.of_apply]
  rw [Finset.sum_congr rfl fun c _ =>
      mul_comm (GamF (d1At G p) (gmi G p) m c l) (GamF (d1At G p) (gmi G p) n k c),
    Finset.sum_congr rfl fun c _ =>
      mul_comm (GamF (d1At G p) (gmi G p) n c l) (GamF (d1At G p) (gmi G p) m k c)]

include hn hGs in
/-- **THE TRANSGRESSION IDENTITY** on THE connection of any smooth nondegenerate `Σ Gᵢⱼ dxᵢ dxⱼ` on `ℝ⁴` with
`det g < 0` at `p`: `Σ_μ ∂_μ K^μ = −√(−det g) *RR`, with row 96's `csLC` and row 69's `pontryaginLC`. -/
theorem transgression (p : Fin 4 → ℝ) (hdet : (gm G p).det < 0) :
    ∑ μ, fderiv ℝ (fun y => csLC G hs hn hGs y μ) p (Pi.single μ 1)
      = -(Real.sqrt (-(gm G p).det) * pontryaginLC G hs hn hGs p) := by
  have hdd : ∀ a b ν, matΓ (ddchr hs hn hGs p a b) ν = matΓ (ddchr hs hn hGs p b a) ν := fun a b ν => by
    ext x y; simp only [matΓ, Matrix.of_apply, ddchr_symm hs hn hGs p a b]
  have alg := transgression_alg (matΓ (chrLC G hs hn hGs p)) (fun ρ => matΓ (dchr hs hn hGs p ρ))
    (fun l ρ => matΓ (ddchr hs hn hGs p l ρ)) hdd
  have hF : ∀ m n, Fc (matΓ (chrLC G hs hn hGs p)) (fun ρ => matΓ (dchr hs hn hGs p ρ)) m n
      = Fm (d1At G p) (d2At G p) (gmi G p) m n := fun m n => by
    rw [Fc_eq_curv hs hn hGs, riemLC_tab hs hn hGs]; rfl
  simp only [hF] at alg
  -- the Pontryagin side, on the tables at `p`
  have hdet0 := gm_det_ne hn p
  have hgg : Matrix.of (gmi G p) * gm G p = 1 := by
    rw [of_gmi]; exact Matrix.nonsing_inv_mul _ (isUnit_iff_ne_zero.2 hdet0)
  have hgT : (gm G p)ᵀ = gm G p := by ext i j; simp [gm, hs i j]
  have hgi : ∀ i j, gmi G p i j = gmi G p j i := fun i j => by
    have := congrFun (congrFun (Matrix.transpose_nonsing_inv (gm G p)) i) j
    rw [hgT] at this; simpa [gmi] using this.symm
  have hc : ∀ m l, ∑ s, gm G p m s * gmi G p l s = if l = m then 1 else 0 := fun m l => by
    have := congrFun (congrFun (Matrix.mul_nonsing_inv (gm G p) (isUnit_iff_ne_zero.2 hdet0)) m) l
    simp only [Matrix.mul_apply, Matrix.one_apply] at this
    rw [show (if l = m then (1 : ℝ) else 0) = if m = l then 1 else 0 from by simp [eq_comm], ← this]
    exact Finset.sum_congr rfl fun s _ => by rw [hgi]; rfl
  have hd1 : ∀ i j c, d1At G p i j c = d1At G p j i c := fun i j c => by
    simp only [d1At, dG1, show G i j = G j i from funext (hs i j)]
  have hd2 : ∀ i j a c, d2At G p i j a c = d2At G p j i a c := fun i j a c => by
    simp only [d2At, dG2, show G i j = G j i from funext (hs i j)]
  have hP := pont_tab hc hd1 hd2 (d2At_symm hGs p) hgi hgg hdet
  rw [pontryaginLC, riemLC_tab hs hn hGs, ← of_gmi, hP, div_csLC hs hn hGs, alg]
  ring

end Bridge

/-! ## Layer 3: corollaries -/

section Corollary

open Matrix

set_option synthInstance.maxHeartbeats 400000

variable {G : Fin 4 → Fin 4 → (Fin 4 → ℝ) → ℝ} (hs : ∀ i j p, G i j p = G j i p)
  (hn : ∀ p (u : Fin 4 → ℝ), (∀ v, formG G p u v = 0) → u = 0) (hGs : ∀ i j, ContDiff ℝ ∞ (G i j))

include hn hGs in
/-- **The receipts' ratio is `−1` for every metric** with `det g < 0` and `*RR ≠ 0` at `p`. -/
theorem ratio_neg_one (p : Fin 4 → ℝ) (hdet : (gm G p).det < 0) (hP : pontryaginLC G hs hn hGs p ≠ 0) :
    (∑ μ, fderiv ℝ (fun y => csLC G hs hn hGs y μ) p (Pi.single μ 1))
      / (Real.sqrt (-(gm G p).det) * pontryaginLC G hs hn hGs p) = -1 := by
  have hs0 : Real.sqrt (-(gm G p).det) ≠ 0 := (Real.sqrt_pos.2 (by linarith)).ne'
  rw [transgression hs hn hGs p hdet, neg_div, div_self (mul_ne_zero hs0 hP)]

end Corollary

/-! ## The bridge to explicit tables -/

section Bridge

variable {G : Fin 4 → Fin 4 → (Fin 4 → ℝ) → ℝ} (hs : ∀ i j p, G i j p = G j i p)
  (hn : ∀ p (u : Fin 4 → ℝ), (∀ v, formG G p u v = 0) → u = 0) (hGs : ∀ i j, ContDiff ℝ ∞ (G i j))

include hn hGs in
/-- **The bridge.** If at `p` the metric, a right inverse, and the first and second partials are given by tables,
THE connection's density is the recipe on those tables. -/
theorem tabs_bridge {p : Fin 4 → ℝ} {g gi : Fin 4 → Fin 4 → ℝ} {d1 : Fin 4 → Fin 4 → Fin 4 → ℝ}
    {d2 : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ} (hg : ∀ i j, G i j p = g i j)
    (hinv : ∀ m k, ∑ l, G m l p * gi l k = if m = k then 1 else 0)
    (h1 : ∀ i j c, d1At G p i j c = d1 i j c) (h2 : ∀ i j a c, d2At G p i j a c = d2 i j a c) :
    pontryaginLC G hs hn hGs p = pontArr (Matrix.of g) (Matrix.of gi) (RiemF d1 d2 gi) := by
  have hgm : gm G p = Matrix.of g := by ext i j; simp [gm, hg]
  have hgi : gmi G p = gi := funext fun l => funext fun k => by
    simp only [gmi, gm_inv hinv, Matrix.of_apply]
  have hd1 : d1At G p = d1 := funext fun i => funext fun j => funext fun c => h1 i j c
  have hd2 : d2At G p = d2 := funext fun i => funext fun j => funext fun a => funext fun c => h2 i j a c
  rw [pontryaginLC, riemLC_tab hs hn hGs, gm_inv hinv, hgi, hd1, hd2, hgm]

end Bridge

#print axioms ShadowProbe.R89Pontryagin.eps4_det
#print axioms ShadowProbe.R89Pontryagin.pontryaginLC_eq
#print axioms ShadowProbe.R89Pontryagin.pontryagin_parity
#print axioms ShadowProbe.R89Pontryagin.transgression
#print axioms ShadowProbe.R89Pontryagin.ratio_neg_one
#print axioms ShadowProbe.R89Pontryagin.tabs_bridge

/-! ## 2-jets: value, first and second coordinate partials of a function at a point, with the sum, product,
inverse and exponential rules -/

section Jets

/-- `F` is `C²` near `p` with value `v`, partials `∂_c F = d c` and `∂_a∂_c F = h a c` at `p`. -/
structure HasJ (F : (Fin 4 → ℝ) → ℝ) (p : Fin 4 → ℝ) (v : ℝ) (d : Fin 4 → ℝ) (h : Fin 4 → Fin 4 → ℝ) : Prop where
  cd : ContDiffAt ℝ 2 F p
  v0 : F p = v
  d1 : ∀ c, fderiv ℝ F p (Pi.single c 1) = d c
  d2 : ∀ a c, fderiv ℝ (fderiv ℝ F) p (Pi.single a 1) (Pi.single c 1) = h a c

variable {F G : (Fin 4 → ℝ) → ℝ} {p : Fin 4 → ℝ} {v w : ℝ} {d e : Fin 4 → ℝ} {h k : Fin 4 → Fin 4 → ℝ}

lemma HasJ.of_eq (hF : HasJ F p v d h) {v' : ℝ} {d' : Fin 4 → ℝ} {h' : Fin 4 → Fin 4 → ℝ} (ev : v = v')
    (ed : ∀ c, d c = d' c) (eh : ∀ a c, h a c = h' a c) : HasJ F p v' d' h' :=
  ⟨hF.cd, ev ▸ hF.v0, fun c => (hF.d1 c).trans (ed c), fun a c => (hF.d2 a c).trans (eh a c)⟩

lemma HasJ.congr (hF : HasJ F p v d h) (hG : G =ᶠ[𝓝 p] F) : HasJ G p v d h := by
  refine ⟨hF.cd.congr_of_eventuallyEq hG, hG.eq_of_nhds.trans hF.v0, fun c => ?_, fun a c => ?_⟩
  · rw [hG.fderiv_eq]; exact hF.d1 c
  · rw [hG.fderiv.fderiv_eq]; exact hF.d2 a c

lemma HasJ.diffNear (hF : HasJ F p v d h) : ∀ᶠ y in 𝓝 p, DifferentiableAt ℝ F y :=
  (hF.cd.eventually (by simp)).mono fun y hy => hy.differentiableAt (by simp)

lemma HasJ.hasD (hF : HasJ F p v d h) : HasFDerivAt F (fderiv ℝ F p) p :=
  (hF.cd.differentiableAt (by simp)).hasFDerivAt

lemma HasJ.hasD2 (hF : HasJ F p v d h) : HasFDerivAt (fderiv ℝ F) (fderiv ℝ (fderiv ℝ F) p) p :=
  ((hF.cd.fderiv_right (m := 1) (by norm_num)).differentiableAt (by simp)).hasFDerivAt

/-- A smooth function: its own partials. -/
lemma hasJ_of (hF : ContDiff ℝ ∞ F) (p : Fin 4 → ℝ) :
    HasJ F p (F p) (fun c => fderiv ℝ F p (Pi.single c 1))
      (fun a c => fderiv ℝ (fderiv ℝ F) p (Pi.single a 1) (Pi.single c 1)) :=
  ⟨hF.contDiffAt.of_le (by simp), rfl, fun _ => rfl, fun _ _ => rfl⟩

lemma hasJ_const (c : ℝ) (p : Fin 4 → ℝ) : HasJ (fun _ => c) p c (fun _ => 0) (fun _ _ => 0) :=
  ⟨contDiffAt_const, rfl, fun _ => by simp, fun _ _ => by simp⟩

/-- The coordinate `y ↦ y i`. -/
lemma hasJ_coord (i : Fin 4) (p : Fin 4 → ℝ) :
    HasJ (fun y => y i) p (p i) (fun c => if c = i then 1 else 0) (fun _ _ => 0) := by
  have hL : ∀ y, HasFDerivAt (fun y : Fin 4 → ℝ => y i) (ContinuousLinearMap.proj (R := ℝ) (φ := fun _ : Fin 4 => ℝ) i) y :=
    fun y => hasFDerivAt_apply i y
  have hf : fderiv ℝ (fun y : Fin 4 → ℝ => y i) = fun _ => ContinuousLinearMap.proj (R := ℝ) (φ := fun _ : Fin 4 => ℝ) i :=
    funext fun y => (hL y).fderiv
  refine ⟨(contDiff_apply ℝ ℝ i).contDiffAt, rfl, fun c => ?_, fun a c => ?_⟩
  · rw [(hL p).fderiv]; simp [Pi.single_apply, eq_comm]
  · rw [hf]; simp

lemma HasJ.add (hF : HasJ F p v d h) (hG : HasJ G p w e k) :
    HasJ (fun y => F y + G y) p (v + w) (fun c => d c + e c) (fun a c => h a c + k a c) := by
  have hn : fderiv ℝ (fun y => F y + G y) =ᶠ[𝓝 p] fun y => fderiv ℝ F y + fderiv ℝ G y :=
    (hF.diffNear.and hG.diffNear).mono fun y hy => fderiv_fun_add hy.1 hy.2
  refine ⟨hF.cd.add hG.cd, by rw [hF.v0, hG.v0], fun c => ?_, fun a c => ?_⟩
  · rw [fderiv_fun_add (hF.hasD.differentiableAt) (hG.hasD.differentiableAt)]; simp [hF.d1, hG.d1]
  · have H : HasFDerivAt (fun y => fderiv ℝ F y + fderiv ℝ G y) _ p := hF.hasD2.add hG.hasD2
    rw [hn.fderiv_eq, H.fderiv]; simp [hF.d2, hG.d2]

lemma HasJ.const_mul (r : ℝ) (hF : HasJ F p v d h) :
    HasJ (fun y => r * F y) p (r * v) (fun c => r * d c) (fun a c => r * h a c) := by
  have hn : fderiv ℝ (fun y => r * F y) = fun y => r • fderiv ℝ F y := funext fun y => by
    by_cases hy : DifferentiableAt ℝ F y
    · exact fderiv_const_mul hy r
    · by_cases hr : r = 0
      · subst hr; simp
      · rw [fderiv_zero_of_not_differentiableAt hy, fderiv_zero_of_not_differentiableAt]; · simp
        exact fun h' => hy (by simpa [hr] using h'.const_mul r⁻¹)
  refine ⟨contDiffAt_const.mul hF.cd, by rw [hF.v0], fun c => ?_, fun a c => ?_⟩
  · rw [hn]; simp [hF.d1]
  · have H : HasFDerivAt (fun y => r • fderiv ℝ F y) _ p := hF.hasD2.const_smul r
    rw [hn, H.fderiv]; simp [hF.d2]

lemma HasJ.mul (hF : HasJ F p v d h) (hG : HasJ G p w e k) :
    HasJ (fun y => F y * G y) p (v * w) (fun c => d c * w + v * e c)
      (fun a c => h a c * w + d c * e a + d a * e c + v * k a c) := by
  have hn : fderiv ℝ (fun y => F y * G y) =ᶠ[𝓝 p] fun y => F y • fderiv ℝ G y + G y • fderiv ℝ F y :=
    (hF.diffNear.and hG.diffNear).mono fun y hy => fderiv_fun_mul hy.1 hy.2
  refine ⟨hF.cd.mul hG.cd, by rw [hF.v0, hG.v0], fun c => ?_, fun a c => ?_⟩
  · rw [fderiv_fun_mul (hF.hasD.differentiableAt) (hG.hasD.differentiableAt)]
    simp [hF.d1, hG.d1, hF.v0, hG.v0]; ring
  · have H : HasFDerivAt (fun y => F y • fderiv ℝ G y + G y • fderiv ℝ F y) _ p :=
      (hF.hasD.smul hG.hasD2).add (hG.hasD.smul hF.hasD2)
    rw [hn.fderiv_eq, H.fderiv]
    simp [hF.d1, hG.d1, hF.d2, hG.d2, hF.v0, hG.v0]; ring

lemma HasJ.inv (hF : HasJ F p v d h) (hv : v ≠ 0) :
    HasJ (fun y => (F y)⁻¹) p v⁻¹ (fun c => -d c / v ^ 2) (fun a c => -h a c / v ^ 2 + 2 * d a * d c / v ^ 3) := by
  have hp : F p ≠ 0 := hF.v0 ▸ hv
  have hne : ∀ᶠ y in 𝓝 p, F y ≠ 0 := (hF.hasD.continuousAt).eventually_ne hp
  have hI : ∀ y, F y ≠ 0 → DifferentiableAt ℝ F y →
      HasFDerivAt (fun y => (F y)⁻¹) ((-(F y ^ 2)⁻¹) • fderiv ℝ F y) y :=
    fun y hy hd => (hasDerivAt_inv hy).comp_hasFDerivAt y hd.hasFDerivAt
  have hn : fderiv ℝ (fun y => (F y)⁻¹) =ᶠ[𝓝 p] fun y => (-(F y ^ 2)⁻¹) • fderiv ℝ F y :=
    (hF.diffNear.and hne).mono fun y hy => (hI y hy.2 hy.1).fderiv
  have hs : HasFDerivAt (fun y => -(F y ^ 2)⁻¹) _ p :=
    ((hasDerivAt_inv (pow_ne_zero 2 hp)).comp_hasFDerivAt p (hF.hasD.pow 2)).neg
  refine ⟨hF.cd.inv hp, by rw [hF.v0], fun c => ?_, fun a c => ?_⟩
  · rw [(hI p hp hF.hasD.differentiableAt).fderiv]; simp [hF.d1, hF.v0]; try field_simp
  · have H : HasFDerivAt (fun y => (-(F y ^ 2)⁻¹) • fderiv ℝ F y) _ p := hs.smul hF.hasD2
    rw [hn.fderiv_eq, H.fderiv]
    simp [hF.d1, hF.d2, hF.v0]; field_simp; try ring

lemma HasJ.exp (hF : HasJ F p v d h) :
    HasJ (fun y => Real.exp (F y)) p (Real.exp v) (fun c => Real.exp v * d c)
      (fun a c => Real.exp v * (h a c + d a * d c)) := by
  have hE : ∀ y, DifferentiableAt ℝ F y →
      HasFDerivAt (fun y => Real.exp (F y)) (Real.exp (F y) • fderiv ℝ F y) y :=
    fun y hd => (Real.hasDerivAt_exp (F y)).comp_hasFDerivAt y hd.hasFDerivAt
  have hn : fderiv ℝ (fun y => Real.exp (F y)) =ᶠ[𝓝 p] fun y => Real.exp (F y) • fderiv ℝ F y :=
    hF.diffNear.mono fun y hy => (hE y hy).fderiv
  refine ⟨Real.contDiff_exp.contDiffAt.comp p hF.cd, by rw [hF.v0], fun c => ?_, fun a c => ?_⟩
  · rw [(hE p hF.hasD.differentiableAt).fderiv]; simp [hF.d1, hF.v0]
  · have H : HasFDerivAt (fun y => Real.exp (F y) • fderiv ℝ F y) _ p := (hE p hF.hasD.differentiableAt).smul hF.hasD2
    rw [hn.fderiv_eq, H.fderiv]
    simp [hF.d1, hF.d2, hF.v0]; ring

/-- The bridge from jets to the recipe's tables: `d1At`, `d2At` of an entry are its jet. -/
lemma HasJ.d1At {G : Fin 4 → Fin 4 → (Fin 4 → ℝ) → ℝ} {i j : Fin 4} (hF : HasJ (G i j) p v d h) (c : Fin 4) :
    d1At G p i j c = d c := hF.d1 c

lemma HasJ.d2At {G : Fin 4 → Fin 4 → (Fin 4 → ℝ) → ℝ} {i j : Fin 4} (hF : HasJ (G i j) p v d h) (a c : Fin 4) :
    d2At G p i j a c = h a c := hF.d2 a c

end Jets

#print axioms ShadowProbe.R89Pontryagin.HasJ.mul
#print axioms ShadowProbe.R89Pontryagin.HasJ.inv
#print axioms ShadowProbe.R89Pontryagin.HasJ.exp

/-! ## Part 1: Kerr in Boyer–Lindquist coordinates `(t, r, u = cos θ, φ)` — the tables

Generated by sympy (symbolic `M`, `a`) and proved layer by layer: each layer from the one below. -/

section KerrTables

noncomputable def KGT (r u a M S D P Q : ℝ) : Fin 4 → Fin 4 → ℝ :=
  ![![((2*M*r - a^(2:ℕ)*u^(2:ℕ) - r^(2:ℕ)) / (S)), 0, 0, ((2*M*a*r*(u - 1)*(u + 1)) / (S))], 
    ![0, ((a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ)) / (D)), 0, 0], 
    ![0, 0, ((-a^(2:ℕ)*u^(2:ℕ) - r^(2:ℕ)) / (P * Q)), 0], 
    ![((2*M*a*r*(u - 1)*(u + 1)) / (S)), 0, 0, ((-(u - 1)*(u + 1)*(-2*M*a^(2:ℕ)*r*u^(2:ℕ) + 2*M*a^(2:ℕ)*r + a^(4:ℕ)*u^(2:ℕ) + a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) + a^(2:ℕ)*r^(2:ℕ) + r^(4:ℕ))) / (S))]]

noncomputable def KGiT (r u a M S D P Q : ℝ) : Fin 4 → Fin 4 → ℝ :=
  ![![((2*M*a^(2:ℕ)*r*u^(2:ℕ) - 2*M*a^(2:ℕ)*r - a^(4:ℕ)*u^(2:ℕ) - a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) - a^(2:ℕ)*r^(2:ℕ) - r^(4:ℕ)) / (S * D)), 0, 0, ((-2*M*a*r) / (S * D))], 
    ![0, ((-2*M*r + a^(2:ℕ) + r^(2:ℕ)) / (S)), 0, 0], 
    ![0, 0, ((-(u - 1)*(u + 1)) / (S)), 0], 
    ![((-2*M*a*r) / (S * D)), 0, 0, ((2*M*r - a^(2:ℕ)*u^(2:ℕ) - r^(2:ℕ)) / (P * Q * S * D))]]

noncomputable def KD1T (r u a M S D P Q : ℝ) : Fin 4 → Fin 4 → Fin 4 → ℝ :=
  ![![![0, ((-2*M*(-a*u + r)*(a*u + r)) / (S^(2:ℕ))), ((-4*M*a^(2:ℕ)*r*u) / (S^(2:ℕ))), 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, ((-2*M*a*(u - 1)*(u + 1)*(-a*u + r)*(a*u + r)) / (S^(2:ℕ))), ((4*M*a*r*u*(a^(2:ℕ) + r^(2:ℕ))) / (S^(2:ℕ))), 0]], 
    ![![0, 0, 0, 0], ![0, ((-2*(-M*a^(2:ℕ)*u^(2:ℕ) + M*r^(2:ℕ) + a^(2:ℕ)*r*u^(2:ℕ) - a^(2:ℕ)*r)) / (D^(2:ℕ))), ((2*a^(2:ℕ)*u) / (D)), 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], 
    ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, ((-2*r) / (P * Q)), ((2*u*(a^(2:ℕ) + r^(2:ℕ))) / (P^(2:ℕ) * Q^(2:ℕ))), 0], ![0, 0, 0, 0]], 
    ![![0, ((-2*M*a*(u - 1)*(u + 1)*(-a*u + r)*(a*u + r)) / (S^(2:ℕ))), ((4*M*a*r*u*(a^(2:ℕ) + r^(2:ℕ))) / (S^(2:ℕ))), 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, ((-2*(u - 1)*(u + 1)*(-M*a^(4:ℕ)*u^(4:ℕ) + M*a^(4:ℕ)*u^(2:ℕ) + M*a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) - M*a^(2:ℕ)*r^(2:ℕ) + a^(4:ℕ)*r*u^(4:ℕ) + 2*a^(2:ℕ)*r^(3:ℕ)*u^(2:ℕ) + r^(5:ℕ))) / (S^(2:ℕ))), ((-2*u*(-2*M*a^(4:ℕ)*r*u^(4:ℕ) + 2*M*a^(4:ℕ)*r - 4*M*a^(2:ℕ)*r^(3:ℕ)*u^(2:ℕ) + 4*M*a^(2:ℕ)*r^(3:ℕ) + a^(6:ℕ)*u^(4:ℕ) + a^(4:ℕ)*r^(2:ℕ)*u^(4:ℕ) + 2*a^(4:ℕ)*r^(2:ℕ)*u^(2:ℕ) + 2*a^(2:ℕ)*r^(4:ℕ)*u^(2:ℕ) + a^(2:ℕ)*r^(4:ℕ) + r^(6:ℕ))) / (S^(2:ℕ))), 0]]]

noncomputable def KD2T (r u a M S D P Q : ℝ) : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ :=
  ![![![![0, 0, 0, 0], ![0, ((4*M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (S^(3:ℕ))), ((4*M*a^(2:ℕ)*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (S^(3:ℕ))), 0], ![0, ((4*M*a^(2:ℕ)*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (S^(3:ℕ))), ((-4*M*a^(2:ℕ)*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (S^(3:ℕ))), 0], ![0, 0, 0, 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, 0, 0, 0], ![0, ((4*M*a*r*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (S^(3:ℕ))), ((-4*M*a*u*(-a^(4:ℕ)*u^(2:ℕ) - 3*a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ)*r^(2:ℕ) + r^(4:ℕ))) / (S^(3:ℕ))), 0], ![0, ((-4*M*a*u*(-a^(4:ℕ)*u^(2:ℕ) - 3*a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ)*r^(2:ℕ) + r^(4:ℕ))) / (S^(3:ℕ))), ((4*M*a*r*(a^(2:ℕ) + r^(2:ℕ))*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (S^(3:ℕ))), 0], ![0, 0, 0, 0]]], 
    ![![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, 0, 0, 0], ![0, ((2*(4*M^(2:ℕ)*a^(2:ℕ)*u^(2:ℕ) - 6*M*a^(2:ℕ)*r*u^(2:ℕ) + 2*M*r^(3:ℕ) - a^(4:ℕ)*u^(2:ℕ) + a^(4:ℕ) + 3*a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) - 3*a^(2:ℕ)*r^(2:ℕ))) / (D^(3:ℕ))), ((-4*a^(2:ℕ)*u*(-M + r)) / (D^(2:ℕ))), 0], ![0, ((-4*a^(2:ℕ)*u*(-M + r)) / (D^(2:ℕ))), ((2*a^(2:ℕ)) / (D)), 0], ![0, 0, 0, 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]]], 
    ![![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, 0, 0, 0], ![0, ((-2) / (P * Q)), ((4*r*u) / (P^(2:ℕ) * Q^(2:ℕ))), 0], ![0, ((4*r*u) / (P^(2:ℕ) * Q^(2:ℕ))), ((-2*(a^(2:ℕ) + r^(2:ℕ))*(3*u^(2:ℕ) + 1)) / (P^(3:ℕ) * Q^(3:ℕ))), 0], ![0, 0, 0, 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]]], 
    ![![![0, 0, 0, 0], ![0, ((4*M*a*r*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (S^(3:ℕ))), ((-4*M*a*u*(-a^(4:ℕ)*u^(2:ℕ) - 3*a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ)*r^(2:ℕ) + r^(4:ℕ))) / (S^(3:ℕ))), 0], ![0, ((-4*M*a*u*(-a^(4:ℕ)*u^(2:ℕ) - 3*a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ)*r^(2:ℕ) + r^(4:ℕ))) / (S^(3:ℕ))), ((4*M*a*r*(a^(2:ℕ) + r^(2:ℕ))*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (S^(3:ℕ))), 0], ![0, 0, 0, 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, 0, 0, 0], ![0, ((-2*(u - 1)*(u + 1)*(6*M*a^(4:ℕ)*r*u^(4:ℕ) - 6*M*a^(4:ℕ)*r*u^(2:ℕ) - 2*M*a^(2:ℕ)*r^(3:ℕ)*u^(2:ℕ) + 2*M*a^(2:ℕ)*r^(3:ℕ) + a^(6:ℕ)*u^(6:ℕ) + 3*a^(4:ℕ)*r^(2:ℕ)*u^(4:ℕ) + 3*a^(2:ℕ)*r^(4:ℕ)*u^(2:ℕ) + r^(6:ℕ))) / (S^(3:ℕ))), ((-4*u*(-M*a^(6:ℕ)*u^(6:ℕ) + M*a^(6:ℕ)*u^(2:ℕ) - 3*M*a^(4:ℕ)*r^(2:ℕ)*u^(4:ℕ) + 6*M*a^(4:ℕ)*r^(2:ℕ)*u^(2:ℕ) - 3*M*a^(4:ℕ)*r^(2:ℕ) + 2*M*a^(2:ℕ)*r^(4:ℕ)*u^(2:ℕ) - 2*M*a^(2:ℕ)*r^(4:ℕ) + a^(6:ℕ)*r*u^(6:ℕ) + 3*a^(4:ℕ)*r^(3:ℕ)*u^(4:ℕ) + 3*a^(2:ℕ)*r^(5:ℕ)*u^(2:ℕ) + r^(7:ℕ))) / (S^(3:ℕ))), 0], ![0, ((-4*u*(-M*a^(6:ℕ)*u^(6:ℕ) + M*a^(6:ℕ)*u^(2:ℕ) - 3*M*a^(4:ℕ)*r^(2:ℕ)*u^(4:ℕ) + 6*M*a^(4:ℕ)*r^(2:ℕ)*u^(2:ℕ) - 3*M*a^(4:ℕ)*r^(2:ℕ) + 2*M*a^(2:ℕ)*r^(4:ℕ)*u^(2:ℕ) - 2*M*a^(2:ℕ)*r^(4:ℕ) + a^(6:ℕ)*r*u^(6:ℕ) + 3*a^(4:ℕ)*r^(3:ℕ)*u^(4:ℕ) + 3*a^(2:ℕ)*r^(5:ℕ)*u^(2:ℕ) + r^(7:ℕ))) / (S^(3:ℕ))), ((-2*(-2*M*a^(6:ℕ)*r*u^(6:ℕ) - 6*M*a^(6:ℕ)*r*u^(2:ℕ) - 6*M*a^(4:ℕ)*r^(3:ℕ)*u^(4:ℕ) - 12*M*a^(4:ℕ)*r^(3:ℕ)*u^(2:ℕ) + 2*M*a^(4:ℕ)*r^(3:ℕ) - 12*M*a^(2:ℕ)*r^(5:ℕ)*u^(2:ℕ) + 4*M*a^(2:ℕ)*r^(5:ℕ) + a^(8:ℕ)*u^(6:ℕ) + a^(6:ℕ)*r^(2:ℕ)*u^(6:ℕ) + 3*a^(6:ℕ)*r^(2:ℕ)*u^(4:ℕ) + 3*a^(4:ℕ)*r^(4:ℕ)*u^(4:ℕ) + 3*a^(4:ℕ)*r^(4:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ)*r^(6:ℕ)*u^(2:ℕ) + a^(2:ℕ)*r^(6:ℕ) + r^(8:ℕ))) / (S^(3:ℕ))), 0], ![0, 0, 0, 0]]]]

noncomputable def KGamT (r u a M S D P Q : ℝ) : Fin 4 → Fin 4 → Fin 4 → ℝ :=
  ![![![0, ((M*(-a*u + r)*(a*u + r)*(-2*M*r + a^(2:ℕ) + r^(2:ℕ))) / (S^(3:ℕ))), ((-2*M*a^(2:ℕ)*r*u*(u - 1)*(u + 1)) / (S^(3:ℕ))), 0], ![((M*(a^(2:ℕ) + r^(2:ℕ))*(-a*u + r)*(a*u + r)) / (D * S^(2:ℕ))), 0, 0, ((M*a*(-a*u + r)*(a*u + r)) / (D * S^(2:ℕ)))], ![((2*M*a^(2:ℕ)*r*u) / (S^(2:ℕ))), 0, 0, ((-2*M*a*r*u) / (P * Q * S^(2:ℕ)))], ![0, ((M*a*(u - 1)*(u + 1)*(-a*u + r)*(a*u + r)*(-2*M*r + a^(2:ℕ) + r^(2:ℕ))) / (S^(3:ℕ))), ((2*M*a*r*u*(a^(2:ℕ) + r^(2:ℕ))*(u - 1)*(u + 1)) / (S^(3:ℕ))), 0]], 
    ![![((M*(a^(2:ℕ) + r^(2:ℕ))*(-a*u + r)*(a*u + r)) / (D * S^(2:ℕ))), 0, 0, ((M*a*(-a*u + r)*(a*u + r)) / (D * S^(2:ℕ)))], ![0, ((M*a^(2:ℕ)*u^(2:ℕ) - M*r^(2:ℕ) - a^(2:ℕ)*r*u^(2:ℕ) + a^(2:ℕ)*r) / (S * D)), ((a^(2:ℕ)*u*(u - 1)*(u + 1)) / (S * D)), 0], ![0, ((a^(2:ℕ)*u) / (S)), ((r) / (S)), 0], ![((M*a*(u - 1)*(u + 1)*(-a^(4:ℕ)*u^(2:ℕ) + a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) + a^(2:ℕ)*r^(2:ℕ) + 3*r^(4:ℕ))) / (D * S^(2:ℕ))), 0, 0, ((-M*a^(4:ℕ)*u^(4:ℕ) + M*a^(4:ℕ)*u^(2:ℕ) - M*a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) - M*a^(2:ℕ)*r^(2:ℕ) - 2*M*r^(4:ℕ) + a^(4:ℕ)*r*u^(4:ℕ) + 2*a^(2:ℕ)*r^(3:ℕ)*u^(2:ℕ) + r^(5:ℕ)) / (D * S^(2:ℕ)))]], 
    ![![((2*M*a^(2:ℕ)*r*u) / (S^(2:ℕ))), 0, 0, ((-2*M*a*r*u) / (P * Q * S^(2:ℕ)))], ![0, ((a^(2:ℕ)*u) / (S)), ((r) / (S)), 0], ![0, ((r*(-2*M*r + a^(2:ℕ) + r^(2:ℕ))) / (P * Q * S)), ((-u*(a^(2:ℕ) + r^(2:ℕ))) / (P * Q * S)), 0], ![((2*M*a^(3:ℕ)*r*u*(u - 1)*(u + 1)) / (S^(2:ℕ))), 0, 0, ((u*(-2*M*a^(2:ℕ)*r*u^(2:ℕ) + 2*M*a^(2:ℕ)*r + a^(4:ℕ)*u^(4:ℕ) + 2*a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) + r^(4:ℕ))) / (P * Q * S^(2:ℕ)))]], 
    ![![0, ((M*a*(u - 1)*(u + 1)*(-a*u + r)*(a*u + r)*(-2*M*r + a^(2:ℕ) + r^(2:ℕ))) / (S^(3:ℕ))), ((2*M*a*r*u*(a^(2:ℕ) + r^(2:ℕ))*(u - 1)*(u + 1)) / (S^(3:ℕ))), 0], ![((M*a*(u - 1)*(u + 1)*(-a^(4:ℕ)*u^(2:ℕ) + a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) + a^(2:ℕ)*r^(2:ℕ) + 3*r^(4:ℕ))) / (D * S^(2:ℕ))), 0, 0, ((-M*a^(4:ℕ)*u^(4:ℕ) + M*a^(4:ℕ)*u^(2:ℕ) - M*a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) - M*a^(2:ℕ)*r^(2:ℕ) - 2*M*r^(4:ℕ) + a^(4:ℕ)*r*u^(4:ℕ) + 2*a^(2:ℕ)*r^(3:ℕ)*u^(2:ℕ) + r^(5:ℕ)) / (D * S^(2:ℕ)))], ![((2*M*a^(3:ℕ)*r*u*(u - 1)*(u + 1)) / (S^(2:ℕ))), 0, 0, ((u*(-2*M*a^(2:ℕ)*r*u^(2:ℕ) + 2*M*a^(2:ℕ)*r + a^(4:ℕ)*u^(4:ℕ) + 2*a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) + r^(4:ℕ))) / (P * Q * S^(2:ℕ)))], ![0, (((u - 1)*(u + 1)*(-2*M*r + a^(2:ℕ) + r^(2:ℕ))*(-M*a^(4:ℕ)*u^(4:ℕ) + M*a^(4:ℕ)*u^(2:ℕ) + M*a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) - M*a^(2:ℕ)*r^(2:ℕ) + a^(4:ℕ)*r*u^(4:ℕ) + 2*a^(2:ℕ)*r^(3:ℕ)*u^(2:ℕ) + r^(5:ℕ))) / (S^(3:ℕ))), ((-u*(u - 1)*(u + 1)*(-2*M*a^(4:ℕ)*r*u^(4:ℕ) + 2*M*a^(4:ℕ)*r - 4*M*a^(2:ℕ)*r^(3:ℕ)*u^(2:ℕ) + 4*M*a^(2:ℕ)*r^(3:ℕ) + a^(6:ℕ)*u^(4:ℕ) + a^(4:ℕ)*r^(2:ℕ)*u^(4:ℕ) + 2*a^(4:ℕ)*r^(2:ℕ)*u^(2:ℕ) + 2*a^(2:ℕ)*r^(4:ℕ)*u^(2:ℕ) + a^(2:ℕ)*r^(4:ℕ) + r^(6:ℕ))) / (S^(3:ℕ))), 0]]]

noncomputable def KDGT (r u a M S D P Q : ℝ) : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ :=
  ![![![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]]], 
    ![![![0, ((-2*M*(-M*a^(4:ℕ)*u^(4:ℕ) + 8*M*a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) - 3*M*r^(4:ℕ) + a^(4:ℕ)*r*u^(4:ℕ) - 4*a^(4:ℕ)*r*u^(2:ℕ) - 4*a^(2:ℕ)*r^(3:ℕ)*u^(2:ℕ) + 2*a^(2:ℕ)*r^(3:ℕ) + r^(5:ℕ))) / (S^(4:ℕ))), ((2*M*a^(2:ℕ)*u*(u - 1)*(u + 1)*(-a^(2:ℕ)*u^(2:ℕ) + 5*r^(2:ℕ))) / (S^(4:ℕ))), 0], ![((-2*M*(M*a^(6:ℕ)*u^(4:ℕ) - M*a^(4:ℕ)*r^(2:ℕ)*u^(4:ℕ) + 6*M*a^(4:ℕ)*r^(2:ℕ)*u^(2:ℕ) + 6*M*a^(2:ℕ)*r^(4:ℕ)*u^(2:ℕ) - 3*M*a^(2:ℕ)*r^(4:ℕ) - M*r^(6:ℕ) - 3*a^(6:ℕ)*r*u^(2:ℕ) - 6*a^(4:ℕ)*r^(3:ℕ)*u^(2:ℕ) + a^(4:ℕ)*r^(3:ℕ) - 3*a^(2:ℕ)*r^(5:ℕ)*u^(2:ℕ) + 2*a^(2:ℕ)*r^(5:ℕ) + r^(7:ℕ))) / (D^(2:ℕ) * S^(3:ℕ))), 0, 0, ((-2*M*a*(M*a^(4:ℕ)*u^(4:ℕ) + 6*M*a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) - 3*M*r^(4:ℕ) - a^(4:ℕ)*r*u^(4:ℕ) - 3*a^(4:ℕ)*r*u^(2:ℕ) - 3*a^(2:ℕ)*r^(3:ℕ)*u^(2:ℕ) + a^(2:ℕ)*r^(3:ℕ) + 2*r^(5:ℕ))) / (D^(2:ℕ) * S^(3:ℕ)))], ![((-2*M*a^(2:ℕ)*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (S^(3:ℕ))), 0, 0, ((2*M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (P * Q * S^(3:ℕ)))], ![0, ((-2*M*a*(u - 1)*(u + 1)*(-M*a^(4:ℕ)*u^(4:ℕ) + 8*M*a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) - 3*M*r^(4:ℕ) + a^(4:ℕ)*r*u^(4:ℕ) - 4*a^(4:ℕ)*r*u^(2:ℕ) - 4*a^(2:ℕ)*r^(3:ℕ)*u^(2:ℕ) + 2*a^(2:ℕ)*r^(3:ℕ) + r^(5:ℕ))) / (S^(4:ℕ))), ((-2*M*a*u*(u - 1)*(u + 1)*(-a^(4:ℕ)*u^(2:ℕ) - 3*a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) + 5*a^(2:ℕ)*r^(2:ℕ) + 3*r^(4:ℕ))) / (S^(4:ℕ))), 0]], ![![((-2*M*(M*a^(6:ℕ)*u^(4:ℕ) - M*a^(4:ℕ)*r^(2:ℕ)*u^(4:ℕ) + 6*M*a^(4:ℕ)*r^(2:ℕ)*u^(2:ℕ) + 6*M*a^(2:ℕ)*r^(4:ℕ)*u^(2:ℕ) - 3*M*a^(2:ℕ)*r^(4:ℕ) - M*r^(6:ℕ) - 3*a^(6:ℕ)*r*u^(2:ℕ) - 6*a^(4:ℕ)*r^(3:ℕ)*u^(2:ℕ) + a^(4:ℕ)*r^(3:ℕ) - 3*a^(2:ℕ)*r^(5:ℕ)*u^(2:ℕ) + 2*a^(2:ℕ)*r^(5:ℕ) + r^(7:ℕ))) / (D^(2:ℕ) * S^(3:ℕ))), 0, 0, ((-2*M*a*(M*a^(4:ℕ)*u^(4:ℕ) + 6*M*a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) - 3*M*r^(4:ℕ) - a^(4:ℕ)*r*u^(4:ℕ) - 3*a^(4:ℕ)*r*u^(2:ℕ) - 3*a^(2:ℕ)*r^(3:ℕ)*u^(2:ℕ) + a^(2:ℕ)*r^(3:ℕ) + 2*r^(5:ℕ))) / (D^(2:ℕ) * S^(3:ℕ)))], ![0, ((2*M^(2:ℕ)*a^(4:ℕ)*u^(4:ℕ) + 8*M^(2:ℕ)*a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) - 2*M^(2:ℕ)*r^(4:ℕ) - 2*M*a^(4:ℕ)*r*u^(4:ℕ) - 4*M*a^(4:ℕ)*r*u^(2:ℕ) - 8*M*a^(2:ℕ)*r^(3:ℕ)*u^(2:ℕ) + 4*M*a^(2:ℕ)*r^(3:ℕ) + 2*M*r^(5:ℕ) - a^(6:ℕ)*u^(4:ℕ) + a^(6:ℕ)*u^(2:ℕ) + a^(4:ℕ)*r^(2:ℕ)*u^(4:ℕ) - a^(4:ℕ)*r^(2:ℕ) + 3*a^(2:ℕ)*r^(4:ℕ)*u^(2:ℕ) - 3*a^(2:ℕ)*r^(4:ℕ)) / (S^(2:ℕ) * D^(2:ℕ))), ((-2*a^(2:ℕ)*u*(u - 1)*(u + 1)*(-M*a^(2:ℕ)*u^(2:ℕ) - 3*M*r^(2:ℕ) + a^(2:ℕ)*r*u^(2:ℕ) + a^(2:ℕ)*r + 2*r^(3:ℕ))) / (S^(2:ℕ) * D^(2:ℕ))), 0], ![0, ((-2*a^(2:ℕ)*r*u) / (S^(2:ℕ))), ((-(-a*u + r)*(a*u + r)) / (S^(2:ℕ))), 0], ![((-2*M*a*(u - 1)*(u + 1)*(M*a^(6:ℕ)*u^(4:ℕ) + M*a^(4:ℕ)*r^(2:ℕ)*u^(4:ℕ) + 6*M*a^(4:ℕ)*r^(2:ℕ)*u^(2:ℕ) + 6*M*a^(2:ℕ)*r^(4:ℕ)*u^(2:ℕ) - 3*M*a^(2:ℕ)*r^(4:ℕ) - 3*M*r^(6:ℕ) - 2*a^(6:ℕ)*r*u^(4:ℕ) - 3*a^(6:ℕ)*r*u^(2:ℕ) - 8*a^(4:ℕ)*r^(3:ℕ)*u^(2:ℕ) + a^(4:ℕ)*r^(3:ℕ) - a^(2:ℕ)*r^(5:ℕ)*u^(2:ℕ) + 2*a^(2:ℕ)*r^(5:ℕ) + 3*r^(7:ℕ))) / (D^(2:ℕ) * S^(3:ℕ))), 0, 0, ((-2*M^(2:ℕ)*a^(6:ℕ)*u^(6:ℕ) + 2*M^(2:ℕ)*a^(6:ℕ)*u^(4:ℕ) - 8*M^(2:ℕ)*a^(4:ℕ)*r^(2:ℕ)*u^(4:ℕ) + 12*M^(2:ℕ)*a^(4:ℕ)*r^(2:ℕ)*u^(2:ℕ) + 6*M^(2:ℕ)*a^(2:ℕ)*r^(4:ℕ)*u^(2:ℕ) - 6*M^(2:ℕ)*a^(2:ℕ)*r^(4:ℕ) - 4*M^(2:ℕ)*r^(6:ℕ) + 2*M*a^(6:ℕ)*r*u^(6:ℕ) - 6*M*a^(6:ℕ)*r*u^(2:ℕ) + 6*M*a^(4:ℕ)*r^(3:ℕ)*u^(4:ℕ) - 12*M*a^(4:ℕ)*r^(3:ℕ)*u^(2:ℕ) + 2*M*a^(4:ℕ)*r^(3:ℕ) + 4*M*a^(2:ℕ)*r^(5:ℕ) + 4*M*r^(7:ℕ) + a^(8:ℕ)*u^(6:ℕ) - a^(6:ℕ)*r^(2:ℕ)*u^(6:ℕ) + 3*a^(6:ℕ)*r^(2:ℕ)*u^(4:ℕ) - 3*a^(4:ℕ)*r^(4:ℕ)*u^(4:ℕ) + 3*a^(4:ℕ)*r^(4:ℕ)*u^(2:ℕ) - 3*a^(2:ℕ)*r^(6:ℕ)*u^(2:ℕ) + a^(2:ℕ)*r^(6:ℕ) - r^(8:ℕ)) / (D^(2:ℕ) * S^(3:ℕ)))]], ![![((-2*M*a^(2:ℕ)*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (S^(3:ℕ))), 0, 0, ((2*M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (P * Q * S^(3:ℕ)))], ![0, ((-2*a^(2:ℕ)*r*u) / (S^(2:ℕ))), ((-(-a*u + r)*(a*u + r)) / (S^(2:ℕ))), 0], ![0, ((-4*M*a^(2:ℕ)*r*u^(2:ℕ) + a^(4:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) - a^(2:ℕ)*r^(2:ℕ) + r^(4:ℕ)) / (P * Q * S^(2:ℕ))), ((-2*a^(2:ℕ)*r*u) / (S^(2:ℕ))), 0], ![((-2*M*a^(3:ℕ)*u*(u - 1)*(u + 1)*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (S^(3:ℕ))), 0, 0, ((2*M*a^(2:ℕ)*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (S^(3:ℕ)))]], ![![0, ((-2*M*a*(u - 1)*(u + 1)*(-M*a^(4:ℕ)*u^(4:ℕ) + 8*M*a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) - 3*M*r^(4:ℕ) + a^(4:ℕ)*r*u^(4:ℕ) - 4*a^(4:ℕ)*r*u^(2:ℕ) - 4*a^(2:ℕ)*r^(3:ℕ)*u^(2:ℕ) + 2*a^(2:ℕ)*r^(3:ℕ) + r^(5:ℕ))) / (S^(4:ℕ))), ((-2*M*a*u*(u - 1)*(u + 1)*(-a^(4:ℕ)*u^(2:ℕ) - 3*a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) + 5*a^(2:ℕ)*r^(2:ℕ) + 3*r^(4:ℕ))) / (S^(4:ℕ))), 0], ![((-2*M*a*(u - 1)*(u + 1)*(M*a^(6:ℕ)*u^(4:ℕ) + M*a^(4:ℕ)*r^(2:ℕ)*u^(4:ℕ) + 6*M*a^(4:ℕ)*r^(2:ℕ)*u^(2:ℕ) + 6*M*a^(2:ℕ)*r^(4:ℕ)*u^(2:ℕ) - 3*M*a^(2:ℕ)*r^(4:ℕ) - 3*M*r^(6:ℕ) - 2*a^(6:ℕ)*r*u^(4:ℕ) - 3*a^(6:ℕ)*r*u^(2:ℕ) - 8*a^(4:ℕ)*r^(3:ℕ)*u^(2:ℕ) + a^(4:ℕ)*r^(3:ℕ) - a^(2:ℕ)*r^(5:ℕ)*u^(2:ℕ) + 2*a^(2:ℕ)*r^(5:ℕ) + 3*r^(7:ℕ))) / (D^(2:ℕ) * S^(3:ℕ))), 0, 0, ((-2*M^(2:ℕ)*a^(6:ℕ)*u^(6:ℕ) + 2*M^(2:ℕ)*a^(6:ℕ)*u^(4:ℕ) - 8*M^(2:ℕ)*a^(4:ℕ)*r^(2:ℕ)*u^(4:ℕ) + 12*M^(2:ℕ)*a^(4:ℕ)*r^(2:ℕ)*u^(2:ℕ) + 6*M^(2:ℕ)*a^(2:ℕ)*r^(4:ℕ)*u^(2:ℕ) - 6*M^(2:ℕ)*a^(2:ℕ)*r^(4:ℕ) - 4*M^(2:ℕ)*r^(6:ℕ) + 2*M*a^(6:ℕ)*r*u^(6:ℕ) - 6*M*a^(6:ℕ)*r*u^(2:ℕ) + 6*M*a^(4:ℕ)*r^(3:ℕ)*u^(4:ℕ) - 12*M*a^(4:ℕ)*r^(3:ℕ)*u^(2:ℕ) + 2*M*a^(4:ℕ)*r^(3:ℕ) + 4*M*a^(2:ℕ)*r^(5:ℕ) + 4*M*r^(7:ℕ) + a^(8:ℕ)*u^(6:ℕ) - a^(6:ℕ)*r^(2:ℕ)*u^(6:ℕ) + 3*a^(6:ℕ)*r^(2:ℕ)*u^(4:ℕ) - 3*a^(4:ℕ)*r^(4:ℕ)*u^(4:ℕ) + 3*a^(4:ℕ)*r^(4:ℕ)*u^(2:ℕ) - 3*a^(2:ℕ)*r^(6:ℕ)*u^(2:ℕ) + a^(2:ℕ)*r^(6:ℕ) - r^(8:ℕ)) / (D^(2:ℕ) * S^(3:ℕ)))], ![((-2*M*a^(3:ℕ)*u*(u - 1)*(u + 1)*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (S^(3:ℕ))), 0, 0, ((2*M*a^(2:ℕ)*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (S^(3:ℕ)))], ![0, (((u - 1)*(u + 1)*(2*M^(2:ℕ)*a^(6:ℕ)*u^(6:ℕ) - 2*M^(2:ℕ)*a^(6:ℕ)*u^(4:ℕ) - 16*M^(2:ℕ)*a^(4:ℕ)*r^(2:ℕ)*u^(4:ℕ) + 16*M^(2:ℕ)*a^(4:ℕ)*r^(2:ℕ)*u^(2:ℕ) + 6*M^(2:ℕ)*a^(2:ℕ)*r^(4:ℕ)*u^(2:ℕ) - 6*M^(2:ℕ)*a^(2:ℕ)*r^(4:ℕ) - 6*M*a^(6:ℕ)*r*u^(6:ℕ) + 10*M*a^(6:ℕ)*r*u^(4:ℕ) - 8*M*a^(6:ℕ)*r*u^(2:ℕ) - 12*M*a^(4:ℕ)*r^(3:ℕ)*u^(2:ℕ) + 4*M*a^(4:ℕ)*r^(3:ℕ) - 6*M*a^(2:ℕ)*r^(5:ℕ)*u^(2:ℕ) + 2*M*a^(2:ℕ)*r^(5:ℕ) + a^(8:ℕ)*u^(6:ℕ) + 3*a^(6:ℕ)*r^(2:ℕ)*u^(6:ℕ) + a^(6:ℕ)*r^(2:ℕ)*u^(4:ℕ) + 7*a^(4:ℕ)*r^(4:ℕ)*u^(4:ℕ) - a^(4:ℕ)*r^(4:ℕ)*u^(2:ℕ) + 5*a^(2:ℕ)*r^(6:ℕ)*u^(2:ℕ) - a^(2:ℕ)*r^(6:ℕ) + r^(8:ℕ))) / (S^(4:ℕ))), ((-2*a^(2:ℕ)*u*(u - 1)^(2:ℕ)*(u + 1)^(2:ℕ)*(-M*a^(4:ℕ)*u^(4:ℕ) - M*a^(4:ℕ)*u^(2:ℕ) - M*a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) + 5*M*a^(2:ℕ)*r^(2:ℕ) + 6*M*r^(4:ℕ) + a^(4:ℕ)*r*u^(4:ℕ) + 2*a^(2:ℕ)*r^(3:ℕ)*u^(2:ℕ) + r^(5:ℕ))) / (S^(4:ℕ))), 0]]], 
    ![![![0, ((-4*M*a^(2:ℕ)*u*(-a^(2:ℕ)*u^(2:ℕ) + 2*r^(2:ℕ))*(-2*M*r + a^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ))), ((-2*M*a^(2:ℕ)*r*(-3*a^(2:ℕ)*u^(4:ℕ) + 5*a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ)*u^(2:ℕ) - r^(2:ℕ))) / (S^(4:ℕ))), 0], ![((-2*M*a^(2:ℕ)*u*(a^(2:ℕ) + r^(2:ℕ))*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (D * S^(3:ℕ))), 0, 0, ((-2*M*a^(3:ℕ)*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (D * S^(3:ℕ)))], ![((2*M*a^(2:ℕ)*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (S^(3:ℕ))), 0, 0, ((2*M*a*r*(5*a^(2:ℕ)*u^(4:ℕ) - 3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (P^(2:ℕ) * Q^(2:ℕ) * S^(3:ℕ)))], ![0, ((2*M*a*u*(-2*M*r + a^(2:ℕ) + r^(2:ℕ))*(a^(4:ℕ)*u^(4:ℕ) - 2*a^(4:ℕ)*u^(2:ℕ) - 4*a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) + 4*a^(2:ℕ)*r^(2:ℕ) + r^(4:ℕ))) / (S^(4:ℕ))), ((2*M*a*r*(a^(2:ℕ) + r^(2:ℕ))*(-3*a^(2:ℕ)*u^(4:ℕ) + 5*a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ)*u^(2:ℕ) - r^(2:ℕ))) / (S^(4:ℕ))), 0]], ![![((-2*M*a^(2:ℕ)*u*(a^(2:ℕ) + r^(2:ℕ))*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (D * S^(3:ℕ))), 0, 0, ((-2*M*a^(3:ℕ)*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (D * S^(3:ℕ)))], ![0, ((-2*a^(2:ℕ)*r*u) / (S^(2:ℕ))), ((a^(2:ℕ)*(a^(2:ℕ)*u^(4:ℕ) + a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ)*u^(2:ℕ) - r^(2:ℕ))) / (D * S^(2:ℕ))), 0], ![0, ((a^(2:ℕ)*(-a*u + r)*(a*u + r)) / (S^(2:ℕ))), ((-2*a^(2:ℕ)*r*u) / (S^(2:ℕ))), 0], ![((2*M*a*u*(a^(2:ℕ) + r^(2:ℕ))^(2:ℕ)*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (D * S^(3:ℕ))), 0, 0, ((2*M*a^(2:ℕ)*u*(a^(2:ℕ) + r^(2:ℕ))*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (D * S^(3:ℕ)))]], ![![((2*M*a^(2:ℕ)*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (S^(3:ℕ))), 0, 0, ((2*M*a*r*(5*a^(2:ℕ)*u^(4:ℕ) - 3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (P^(2:ℕ) * Q^(2:ℕ) * S^(3:ℕ)))], ![0, ((a^(2:ℕ)*(-a*u + r)*(a*u + r)) / (S^(2:ℕ))), ((-2*a^(2:ℕ)*r*u) / (S^(2:ℕ))), 0], ![0, ((-2*r*u*(-2*M*r + a^(2:ℕ) + r^(2:ℕ))*(2*a^(2:ℕ)*u^(2:ℕ) - a^(2:ℕ) + r^(2:ℕ))) / (P^(2:ℕ) * Q^(2:ℕ) * S^(2:ℕ))), (((a^(2:ℕ) + r^(2:ℕ))*(3*a^(2:ℕ)*u^(4:ℕ) - a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (P^(2:ℕ) * Q^(2:ℕ) * S^(2:ℕ))), 0], ![((2*M*a^(3:ℕ)*r*(-a^(2:ℕ)*u^(4:ℕ) + 3*a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ)*u^(2:ℕ) - r^(2:ℕ))) / (S^(3:ℕ))), 0, 0, ((6*M*a^(4:ℕ)*r*u^(6:ℕ) - 12*M*a^(4:ℕ)*r*u^(4:ℕ) + 6*M*a^(4:ℕ)*r*u^(2:ℕ) - 2*M*a^(2:ℕ)*r^(3:ℕ)*u^(4:ℕ) + 4*M*a^(2:ℕ)*r^(3:ℕ)*u^(2:ℕ) - 2*M*a^(2:ℕ)*r^(3:ℕ) - a^(6:ℕ)*u^(8:ℕ) - a^(6:ℕ)*u^(6:ℕ) - 3*a^(4:ℕ)*r^(2:ℕ)*u^(6:ℕ) - 3*a^(4:ℕ)*r^(2:ℕ)*u^(4:ℕ) - 3*a^(2:ℕ)*r^(4:ℕ)*u^(4:ℕ) - 3*a^(2:ℕ)*r^(4:ℕ)*u^(2:ℕ) - r^(6:ℕ)*u^(2:ℕ) - r^(6:ℕ)) / (P^(2:ℕ) * Q^(2:ℕ) * S^(3:ℕ)))]], ![![0, ((2*M*a*u*(-2*M*r + a^(2:ℕ) + r^(2:ℕ))*(a^(4:ℕ)*u^(4:ℕ) - 2*a^(4:ℕ)*u^(2:ℕ) - 4*a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) + 4*a^(2:ℕ)*r^(2:ℕ) + r^(4:ℕ))) / (S^(4:ℕ))), ((2*M*a*r*(a^(2:ℕ) + r^(2:ℕ))*(-3*a^(2:ℕ)*u^(4:ℕ) + 5*a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ)*u^(2:ℕ) - r^(2:ℕ))) / (S^(4:ℕ))), 0], ![((2*M*a*u*(a^(2:ℕ) + r^(2:ℕ))^(2:ℕ)*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (D * S^(3:ℕ))), 0, 0, ((2*M*a^(2:ℕ)*u*(a^(2:ℕ) + r^(2:ℕ))*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (D * S^(3:ℕ)))], ![((2*M*a^(3:ℕ)*r*(-a^(2:ℕ)*u^(4:ℕ) + 3*a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ)*u^(2:ℕ) - r^(2:ℕ))) / (S^(3:ℕ))), 0, 0, ((6*M*a^(4:ℕ)*r*u^(6:ℕ) - 12*M*a^(4:ℕ)*r*u^(4:ℕ) + 6*M*a^(4:ℕ)*r*u^(2:ℕ) - 2*M*a^(2:ℕ)*r^(3:ℕ)*u^(4:ℕ) + 4*M*a^(2:ℕ)*r^(3:ℕ)*u^(2:ℕ) - 2*M*a^(2:ℕ)*r^(3:ℕ) - a^(6:ℕ)*u^(8:ℕ) - a^(6:ℕ)*u^(6:ℕ) - 3*a^(4:ℕ)*r^(2:ℕ)*u^(6:ℕ) - 3*a^(4:ℕ)*r^(2:ℕ)*u^(4:ℕ) - 3*a^(2:ℕ)*r^(4:ℕ)*u^(4:ℕ) - 3*a^(2:ℕ)*r^(4:ℕ)*u^(2:ℕ) - r^(6:ℕ)*u^(2:ℕ) - r^(6:ℕ)) / (P^(2:ℕ) * Q^(2:ℕ) * S^(3:ℕ)))], ![0, ((2*u*(-2*M*r + a^(2:ℕ) + r^(2:ℕ))*(-2*M*a^(6:ℕ)*u^(4:ℕ) + 2*M*a^(6:ℕ)*u^(2:ℕ) - 4*M*a^(4:ℕ)*r^(2:ℕ)*u^(4:ℕ) + 8*M*a^(4:ℕ)*r^(2:ℕ)*u^(2:ℕ) - 4*M*a^(4:ℕ)*r^(2:ℕ) + 2*M*a^(2:ℕ)*r^(4:ℕ)*u^(2:ℕ) - 2*M*a^(2:ℕ)*r^(4:ℕ) + a^(6:ℕ)*r*u^(4:ℕ) + a^(4:ℕ)*r^(3:ℕ)*u^(4:ℕ) + 2*a^(4:ℕ)*r^(3:ℕ)*u^(2:ℕ) + 2*a^(2:ℕ)*r^(5:ℕ)*u^(2:ℕ) + a^(2:ℕ)*r^(5:ℕ) + r^(7:ℕ))) / (S^(4:ℕ))), ((2*M*a^(6:ℕ)*r*u^(8:ℕ) + 2*M*a^(6:ℕ)*r*u^(6:ℕ) + 6*M*a^(6:ℕ)*r*u^(4:ℕ) - 10*M*a^(6:ℕ)*r*u^(2:ℕ) + 10*M*a^(4:ℕ)*r^(3:ℕ)*u^(6:ℕ) + 14*M*a^(4:ℕ)*r^(3:ℕ)*u^(4:ℕ) - 26*M*a^(4:ℕ)*r^(3:ℕ)*u^(2:ℕ) + 2*M*a^(4:ℕ)*r^(3:ℕ) + 20*M*a^(2:ℕ)*r^(5:ℕ)*u^(4:ℕ) - 24*M*a^(2:ℕ)*r^(5:ℕ)*u^(2:ℕ) + 4*M*a^(2:ℕ)*r^(5:ℕ) - a^(8:ℕ)*u^(8:ℕ) - a^(8:ℕ)*u^(6:ℕ) - a^(6:ℕ)*r^(2:ℕ)*u^(8:ℕ) - 6*a^(6:ℕ)*r^(2:ℕ)*u^(6:ℕ) - a^(6:ℕ)*r^(2:ℕ)*u^(4:ℕ) - 5*a^(4:ℕ)*r^(4:ℕ)*u^(6:ℕ) - 8*a^(4:ℕ)*r^(4:ℕ)*u^(4:ℕ) + a^(4:ℕ)*r^(4:ℕ)*u^(2:ℕ) - 7*a^(2:ℕ)*r^(6:ℕ)*u^(4:ℕ) - 2*a^(2:ℕ)*r^(6:ℕ)*u^(2:ℕ) + a^(2:ℕ)*r^(6:ℕ) - 3*r^(8:ℕ)*u^(2:ℕ) + r^(8:ℕ)) / (S^(4:ℕ))), 0]]], 
    ![![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]]]]

noncomputable def KRT (r u a M S D P Q : ℝ) : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ :=
  ![![![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, ((M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-4*M*r - a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + 2*r^(2:ℕ))) / (S^(4:ℕ))), ((-3*M*a^(2:ℕ)*u*(u - 1)*(u + 1)*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (S^(4:ℕ))), 0], ![((M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + 2*r^(2:ℕ))) / (D * S^(3:ℕ))), 0, 0, ((3*M*a*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (D * S^(3:ℕ)))], ![((M*a^(2:ℕ)*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-4*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (D * S^(3:ℕ))), 0, 0, ((-M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-4*M*r - a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + 2*r^(2:ℕ))) / (P * Q * D * S^(3:ℕ)))], ![0, ((M*a*r*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-4*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (S^(4:ℕ))), ((M*a*u*(u - 1)*(u + 1)*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + 2*r^(2:ℕ))) / (S^(4:ℕ))), 0]], ![![0, ((3*M*a^(2:ℕ)*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*M*r + a^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ))), ((-M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-2*M*r - 2*a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ))), 0], ![((M*a^(2:ℕ)*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (D * S^(3:ℕ))), 0, 0, ((-M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*M*r - 2*a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + r^(2:ℕ))) / (P * Q * D * S^(3:ℕ)))], ![((M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-2*a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + r^(2:ℕ))) / (P * Q * S^(3:ℕ))), 0, 0, ((3*M*a*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (P * Q * S^(3:ℕ)))], ![0, ((-M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*M*r + a^(2:ℕ) + r^(2:ℕ))*(-2*a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ))), ((-M*a*r*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-2*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (S^(4:ℕ))), 0]], ![![((-2*M^(2:ℕ)*a*r^(2:ℕ)*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ))), 0, 0, ((-M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-2*M*r + a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ)))], ![0, 0, ((M*a*u*(u - 1)*(u + 1)*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (S^(3:ℕ))), 0], ![0, ((M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*M*r + a^(2:ℕ) + r^(2:ℕ))) / (S^(3:ℕ))), 0, 0], ![((M*r*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-2*M*a^(2:ℕ)*r*u^(2:ℕ) + 2*M*a^(2:ℕ)*r + a^(4:ℕ)*u^(2:ℕ) + a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) + a^(2:ℕ)*r^(2:ℕ) + r^(4:ℕ))) / (S^(4:ℕ))), 0, 0, ((2*M^(2:ℕ)*a*r^(2:ℕ)*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ)))]]], 
    ![![![0, ((-M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-4*M*r - a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + 2*r^(2:ℕ))) / (S^(4:ℕ))), ((3*M*a^(2:ℕ)*u*(u - 1)*(u + 1)*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (S^(4:ℕ))), 0], ![((-M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + 2*r^(2:ℕ))) / (D * S^(3:ℕ))), 0, 0, ((-3*M*a*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (D * S^(3:ℕ)))], ![((-M*a^(2:ℕ)*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-4*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (D * S^(3:ℕ))), 0, 0, ((M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-4*M*r - a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + 2*r^(2:ℕ))) / (P * Q * D * S^(3:ℕ)))], ![0, ((-M*a*r*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-4*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (S^(4:ℕ))), ((-M*a*u*(u - 1)*(u + 1)*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + 2*r^(2:ℕ))) / (S^(4:ℕ))), 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![((2*M^(2:ℕ)*a^(2:ℕ)*r*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (D * S^(3:ℕ))), 0, 0, ((M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*M*r + a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (P * Q * D * S^(3:ℕ)))], ![0, 0, ((M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (D * S^(2:ℕ))), 0], ![0, ((M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (P * Q * S^(2:ℕ))), 0, 0], ![((-M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*M*a^(2:ℕ)*r*u^(2:ℕ) + 2*M*a^(2:ℕ)*r + a^(4:ℕ)*u^(2:ℕ) + a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) + a^(2:ℕ)*r^(2:ℕ) + r^(4:ℕ))) / (D * S^(3:ℕ))), 0, 0, ((-2*M^(2:ℕ)*a^(2:ℕ)*r*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (D * S^(3:ℕ)))]], ![![0, ((-M*a*r*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-4*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (S^(4:ℕ))), ((-M*a*u*(u - 1)*(u + 1)*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ))), 0], ![((-3*M*a*r*(a^(2:ℕ) + r^(2:ℕ))*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (D * S^(3:ℕ))), 0, 0, ((M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-2*a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + r^(2:ℕ))) / (D * S^(3:ℕ)))], ![((M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(4*M*a^(2:ℕ)*r*u^(2:ℕ) - 4*M*a^(2:ℕ)*r - 2*a^(4:ℕ)*u^(2:ℕ) + 3*a^(4:ℕ) - 2*a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) + 4*a^(2:ℕ)*r^(2:ℕ) + r^(4:ℕ))) / (D * S^(3:ℕ))), 0, 0, ((M*a^(2:ℕ)*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-4*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (D * S^(3:ℕ)))], ![0, ((M*r*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(4*M*a^(2:ℕ)*r*u^(2:ℕ) - 4*M*a^(2:ℕ)*r - 2*a^(4:ℕ)*u^(2:ℕ) + 3*a^(4:ℕ) - 2*a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) + 4*a^(2:ℕ)*r^(2:ℕ) + r^(4:ℕ))) / (S^(4:ℕ))), ((-3*M*a^(2:ℕ)*u*(a^(2:ℕ) + r^(2:ℕ))*(u - 1)^(2:ℕ)*(u + 1)^(2:ℕ)*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (S^(4:ℕ))), 0]]], 
    ![![![0, ((-3*M*a^(2:ℕ)*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*M*r + a^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ))), ((M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-2*M*r - 2*a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ))), 0], ![((-M*a^(2:ℕ)*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (D * S^(3:ℕ))), 0, 0, ((M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*M*r - 2*a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + r^(2:ℕ))) / (P * Q * D * S^(3:ℕ)))], ![((-M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-2*a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + r^(2:ℕ))) / (P * Q * S^(3:ℕ))), 0, 0, ((-3*M*a*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (P * Q * S^(3:ℕ)))], ![0, ((M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*M*r + a^(2:ℕ) + r^(2:ℕ))*(-2*a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ))), ((M*a*r*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-2*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (S^(4:ℕ))), 0]], ![![((-2*M^(2:ℕ)*a^(2:ℕ)*r*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (D * S^(3:ℕ))), 0, 0, ((-M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*M*r + a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (P * Q * D * S^(3:ℕ)))], ![0, 0, ((-M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (D * S^(2:ℕ))), 0], ![0, ((-M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (P * Q * S^(2:ℕ))), 0, 0], ![((M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*M*a^(2:ℕ)*r*u^(2:ℕ) + 2*M*a^(2:ℕ)*r + a^(4:ℕ)*u^(2:ℕ) + a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) + a^(2:ℕ)*r^(2:ℕ) + r^(4:ℕ))) / (D * S^(3:ℕ))), 0, 0, ((2*M^(2:ℕ)*a^(2:ℕ)*r*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (D * S^(3:ℕ)))]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, ((M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*M*r + a^(2:ℕ) + r^(2:ℕ))*(-a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + 2*r^(2:ℕ))) / (S^(4:ℕ))), ((M*a*r*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-2*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (S^(4:ℕ))), 0], ![((M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(2*M*a^(2:ℕ)*r*u^(2:ℕ) - 2*M*a^(2:ℕ)*r - a^(4:ℕ)*u^(2:ℕ) + 3*a^(4:ℕ) - a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) + 5*a^(2:ℕ)*r^(2:ℕ) + 2*r^(4:ℕ))) / (D * S^(3:ℕ))), 0, 0, ((M*a^(2:ℕ)*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (D * S^(3:ℕ)))], ![((-3*M*a*r*(a^(2:ℕ) + r^(2:ℕ))*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (S^(3:ℕ))), 0, 0, ((M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + 2*r^(2:ℕ))) / (P * Q * S^(3:ℕ)))], ![0, ((3*M*a^(2:ℕ)*u*(a^(2:ℕ) + r^(2:ℕ))*(u - 1)*(u + 1)*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*M*r + a^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ))), ((-M*r*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(2*M*a^(2:ℕ)*r*u^(2:ℕ) - 2*M*a^(2:ℕ)*r - a^(4:ℕ)*u^(2:ℕ) + 3*a^(4:ℕ) - a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) + 5*a^(2:ℕ)*r^(2:ℕ) + 2*r^(4:ℕ))) / (S^(4:ℕ))), 0]]], 
    ![![![((2*M^(2:ℕ)*a*r^(2:ℕ)*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ))), 0, 0, ((M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-2*M*r + a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ)))], ![0, 0, ((-M*a*u*(u - 1)*(u + 1)*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (S^(3:ℕ))), 0], ![0, ((-M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*M*r + a^(2:ℕ) + r^(2:ℕ))) / (S^(3:ℕ))), 0, 0], ![((-M*r*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-2*M*a^(2:ℕ)*r*u^(2:ℕ) + 2*M*a^(2:ℕ)*r + a^(4:ℕ)*u^(2:ℕ) + a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) + a^(2:ℕ)*r^(2:ℕ) + r^(4:ℕ))) / (S^(4:ℕ))), 0, 0, ((-2*M^(2:ℕ)*a*r^(2:ℕ)*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ)))]], ![![0, ((M*a*r*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-4*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (S^(4:ℕ))), ((M*a*u*(u - 1)*(u + 1)*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ))), 0], ![((3*M*a*r*(a^(2:ℕ) + r^(2:ℕ))*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (D * S^(3:ℕ))), 0, 0, ((-M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-2*a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + r^(2:ℕ))) / (D * S^(3:ℕ)))], ![((-M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(4*M*a^(2:ℕ)*r*u^(2:ℕ) - 4*M*a^(2:ℕ)*r - 2*a^(4:ℕ)*u^(2:ℕ) + 3*a^(4:ℕ) - 2*a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) + 4*a^(2:ℕ)*r^(2:ℕ) + r^(4:ℕ))) / (D * S^(3:ℕ))), 0, 0, ((-M*a^(2:ℕ)*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-4*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (D * S^(3:ℕ)))], ![0, ((-M*r*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(4*M*a^(2:ℕ)*r*u^(2:ℕ) - 4*M*a^(2:ℕ)*r - 2*a^(4:ℕ)*u^(2:ℕ) + 3*a^(4:ℕ) - 2*a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) + 4*a^(2:ℕ)*r^(2:ℕ) + r^(4:ℕ))) / (S^(4:ℕ))), ((3*M*a^(2:ℕ)*u*(a^(2:ℕ) + r^(2:ℕ))*(u - 1)^(2:ℕ)*(u + 1)^(2:ℕ)*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (S^(4:ℕ))), 0]], ![![0, ((-M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*M*r + a^(2:ℕ) + r^(2:ℕ))*(-a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + 2*r^(2:ℕ))) / (S^(4:ℕ))), ((-M*a*r*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-2*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (S^(4:ℕ))), 0], ![((-M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(2*M*a^(2:ℕ)*r*u^(2:ℕ) - 2*M*a^(2:ℕ)*r - a^(4:ℕ)*u^(2:ℕ) + 3*a^(4:ℕ) - a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) + 5*a^(2:ℕ)*r^(2:ℕ) + 2*r^(4:ℕ))) / (D * S^(3:ℕ))), 0, 0, ((-M*a^(2:ℕ)*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (D * S^(3:ℕ)))], ![((3*M*a*r*(a^(2:ℕ) + r^(2:ℕ))*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (S^(3:ℕ))), 0, 0, ((-M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + 2*r^(2:ℕ))) / (P * Q * S^(3:ℕ)))], ![0, ((-3*M*a^(2:ℕ)*u*(a^(2:ℕ) + r^(2:ℕ))*(u - 1)*(u + 1)*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*M*r + a^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ))), ((M*r*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(2*M*a^(2:ℕ)*r*u^(2:ℕ) - 2*M*a^(2:ℕ)*r - a^(4:ℕ)*u^(2:ℕ) + 3*a^(4:ℕ) - a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) + 5*a^(2:ℕ)*r^(2:ℕ) + 2*r^(4:ℕ))) / (S^(4:ℕ))), 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]]]]

noncomputable def KRDT (r u a M S D P Q : ℝ) : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ :=
  ![![![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, ((-M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-4*M*r - a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + 2*r^(2:ℕ))) / (D * S^(3:ℕ))), ((-3*M*a^(2:ℕ)*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (S^(3:ℕ))), 0], ![((M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-4*M*r - a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + 2*r^(2:ℕ))) / (D * S^(3:ℕ))), 0, 0, ((M*a*r*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-4*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (D * S^(3:ℕ)))], ![((3*M*a^(2:ℕ)*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (S^(3:ℕ))), 0, 0, ((-M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + 2*r^(2:ℕ))) / (S^(3:ℕ)))], ![0, ((-M*a*r*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-4*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (D * S^(3:ℕ))), ((M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + 2*r^(2:ℕ))) / (S^(3:ℕ))), 0]], ![![0, ((-3*M*a^(2:ℕ)*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (S^(3:ℕ))), ((-M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-2*M*r - 2*a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + r^(2:ℕ))) / (P * Q * S^(3:ℕ))), 0], ![((3*M*a^(2:ℕ)*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (S^(3:ℕ))), 0, 0, ((-M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + r^(2:ℕ))) / (S^(3:ℕ)))], ![((M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-2*M*r - 2*a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + r^(2:ℕ))) / (P * Q * S^(3:ℕ))), 0, 0, ((M*a*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-2*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (S^(3:ℕ)))], ![0, ((M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + r^(2:ℕ))) / (S^(3:ℕ))), ((-M*a*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-2*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (S^(3:ℕ))), 0]], ![![0, 0, 0, ((-M*r*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-2*M*r + a^(2:ℕ) + r^(2:ℕ))) / (S^(3:ℕ)))], ![0, 0, ((M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (S^(2:ℕ))), 0], ![0, ((-M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (S^(2:ℕ))), 0, 0], ![((M*r*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-2*M*r + a^(2:ℕ) + r^(2:ℕ))) / (S^(3:ℕ))), 0, 0, 0]]], 
    ![![![0, ((M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-4*M*r - a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + 2*r^(2:ℕ))) / (D * S^(3:ℕ))), ((3*M*a^(2:ℕ)*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (S^(3:ℕ))), 0], ![((-M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-4*M*r - a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + 2*r^(2:ℕ))) / (D * S^(3:ℕ))), 0, 0, ((-M*a*r*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-4*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (D * S^(3:ℕ)))], ![((-3*M*a^(2:ℕ)*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (S^(3:ℕ))), 0, 0, ((M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + 2*r^(2:ℕ))) / (S^(3:ℕ)))], ![0, ((M*a*r*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-4*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (D * S^(3:ℕ))), ((-M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + 2*r^(2:ℕ))) / (S^(3:ℕ))), 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, 0, 0, ((M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (S^(2:ℕ)))], ![0, 0, ((M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (P * Q * S * D)), 0], ![0, ((-M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (P * Q * S * D)), 0, 0], ![((-M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (S^(2:ℕ))), 0, 0, 0]], ![![0, ((M*a*r*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-4*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (D * S^(3:ℕ))), ((-M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + r^(2:ℕ))) / (S^(3:ℕ))), 0], ![((-M*a*r*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-4*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (D * S^(3:ℕ))), 0, 0, ((M*r*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(4*M*a^(2:ℕ)*r*u^(2:ℕ) - 4*M*a^(2:ℕ)*r - 2*a^(4:ℕ)*u^(2:ℕ) + 3*a^(4:ℕ) - 2*a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) + 4*a^(2:ℕ)*r^(2:ℕ) + r^(4:ℕ))) / (D * S^(3:ℕ)))], ![((M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + r^(2:ℕ))) / (S^(3:ℕ))), 0, 0, ((3*M*a^(2:ℕ)*u*(a^(2:ℕ) + r^(2:ℕ))*(u - 1)*(u + 1)*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (S^(3:ℕ)))], ![0, ((-M*r*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(4*M*a^(2:ℕ)*r*u^(2:ℕ) - 4*M*a^(2:ℕ)*r - 2*a^(4:ℕ)*u^(2:ℕ) + 3*a^(4:ℕ) - 2*a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) + 4*a^(2:ℕ)*r^(2:ℕ) + r^(4:ℕ))) / (D * S^(3:ℕ))), ((-3*M*a^(2:ℕ)*u*(a^(2:ℕ) + r^(2:ℕ))*(u - 1)*(u + 1)*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (S^(3:ℕ))), 0]]], 
    ![![![0, ((3*M*a^(2:ℕ)*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (S^(3:ℕ))), ((M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-2*M*r - 2*a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + r^(2:ℕ))) / (P * Q * S^(3:ℕ))), 0], ![((-3*M*a^(2:ℕ)*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (S^(3:ℕ))), 0, 0, ((M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + r^(2:ℕ))) / (S^(3:ℕ)))], ![((-M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-2*M*r - 2*a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + r^(2:ℕ))) / (P * Q * S^(3:ℕ))), 0, 0, ((-M*a*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-2*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (S^(3:ℕ)))], ![0, ((-M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + r^(2:ℕ))) / (S^(3:ℕ))), ((M*a*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-2*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (S^(3:ℕ))), 0]], ![![0, 0, 0, ((-M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (S^(2:ℕ)))], ![0, 0, ((-M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (P * Q * S * D)), 0], ![0, ((M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (P * Q * S * D)), 0, 0], ![((M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (S^(2:ℕ))), 0, 0, 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, ((-M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + 2*r^(2:ℕ))) / (S^(3:ℕ))), ((M*a*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-2*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (S^(3:ℕ))), 0], ![((M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + 2*r^(2:ℕ))) / (S^(3:ℕ))), 0, 0, ((3*M*a^(2:ℕ)*u*(a^(2:ℕ) + r^(2:ℕ))*(u - 1)*(u + 1)*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (S^(3:ℕ)))], ![((-M*a*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-2*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (S^(3:ℕ))), 0, 0, ((M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(2*M*a^(2:ℕ)*r*u^(2:ℕ) - 2*M*a^(2:ℕ)*r - a^(4:ℕ)*u^(2:ℕ) + 3*a^(4:ℕ) - a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) + 5*a^(2:ℕ)*r^(2:ℕ) + 2*r^(4:ℕ))) / (S^(3:ℕ)))], ![0, ((-3*M*a^(2:ℕ)*u*(a^(2:ℕ) + r^(2:ℕ))*(u - 1)*(u + 1)*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (S^(3:ℕ))), ((-M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(2*M*a^(2:ℕ)*r*u^(2:ℕ) - 2*M*a^(2:ℕ)*r - a^(4:ℕ)*u^(2:ℕ) + 3*a^(4:ℕ) - a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) + 5*a^(2:ℕ)*r^(2:ℕ) + 2*r^(4:ℕ))) / (S^(3:ℕ))), 0]]], 
    ![![![0, 0, 0, ((M*r*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-2*M*r + a^(2:ℕ) + r^(2:ℕ))) / (S^(3:ℕ)))], ![0, 0, ((-M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (S^(2:ℕ))), 0], ![0, ((M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (S^(2:ℕ))), 0, 0], ![((-M*r*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-2*M*r + a^(2:ℕ) + r^(2:ℕ))) / (S^(3:ℕ))), 0, 0, 0]], ![![0, ((-M*a*r*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-4*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (D * S^(3:ℕ))), ((M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + r^(2:ℕ))) / (S^(3:ℕ))), 0], ![((M*a*r*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-4*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (D * S^(3:ℕ))), 0, 0, ((-M*r*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(4*M*a^(2:ℕ)*r*u^(2:ℕ) - 4*M*a^(2:ℕ)*r - 2*a^(4:ℕ)*u^(2:ℕ) + 3*a^(4:ℕ) - 2*a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) + 4*a^(2:ℕ)*r^(2:ℕ) + r^(4:ℕ))) / (D * S^(3:ℕ)))], ![((-M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + r^(2:ℕ))) / (S^(3:ℕ))), 0, 0, ((-3*M*a^(2:ℕ)*u*(a^(2:ℕ) + r^(2:ℕ))*(u - 1)*(u + 1)*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (S^(3:ℕ)))], ![0, ((M*r*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(4*M*a^(2:ℕ)*r*u^(2:ℕ) - 4*M*a^(2:ℕ)*r - 2*a^(4:ℕ)*u^(2:ℕ) + 3*a^(4:ℕ) - 2*a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) + 4*a^(2:ℕ)*r^(2:ℕ) + r^(4:ℕ))) / (D * S^(3:ℕ))), ((3*M*a^(2:ℕ)*u*(a^(2:ℕ) + r^(2:ℕ))*(u - 1)*(u + 1)*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (S^(3:ℕ))), 0]], ![![0, ((M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + 2*r^(2:ℕ))) / (S^(3:ℕ))), ((-M*a*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-2*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (S^(3:ℕ))), 0], ![((-M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + 2*r^(2:ℕ))) / (S^(3:ℕ))), 0, 0, ((-3*M*a^(2:ℕ)*u*(a^(2:ℕ) + r^(2:ℕ))*(u - 1)*(u + 1)*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (S^(3:ℕ)))], ![((M*a*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-2*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (S^(3:ℕ))), 0, 0, ((-M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(2*M*a^(2:ℕ)*r*u^(2:ℕ) - 2*M*a^(2:ℕ)*r - a^(4:ℕ)*u^(2:ℕ) + 3*a^(4:ℕ) - a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) + 5*a^(2:ℕ)*r^(2:ℕ) + 2*r^(4:ℕ))) / (S^(3:ℕ)))], ![0, ((3*M*a^(2:ℕ)*u*(a^(2:ℕ) + r^(2:ℕ))*(u - 1)*(u + 1)*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (S^(3:ℕ))), ((M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(2*M*a^(2:ℕ)*r*u^(2:ℕ) - 2*M*a^(2:ℕ)*r - a^(4:ℕ)*u^(2:ℕ) + 3*a^(4:ℕ) - a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) + 5*a^(2:ℕ)*r^(2:ℕ) + 2*r^(4:ℕ))) / (S^(3:ℕ))), 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]]]]

noncomputable def KRUT (r u a M S D P Q : ℝ) : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ :=
  ![![![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, ((M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + 2*r^(2:ℕ))) / (S^(4:ℕ))), ((-M*a^(2:ℕ)*u*(u - 1)*(u + 1)*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-4*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (D * S^(4:ℕ))), 0], ![((-M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + 2*r^(2:ℕ))) / (S^(4:ℕ))), 0, 0, ((-3*M*a*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ)))], ![((M*a^(2:ℕ)*u*(u - 1)*(u + 1)*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-4*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (D * S^(4:ℕ))), 0, 0, ((-M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-4*M*r - a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + 2*r^(2:ℕ))) / (D * S^(4:ℕ)))], ![0, ((3*M*a*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ))), ((M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-4*M*r - a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + 2*r^(2:ℕ))) / (D * S^(4:ℕ))), 0]], ![![0, ((M*a^(2:ℕ)*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (S^(4:ℕ))), ((-M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-2*a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ))), 0], ![((-M*a^(2:ℕ)*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (S^(4:ℕ))), 0, 0, ((M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*M*r - 2*a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + r^(2:ℕ))) / (P * Q * S^(4:ℕ)))], ![((M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-2*a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ))), 0, 0, ((3*M*a*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ)))], ![0, ((-M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*M*r - 2*a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + r^(2:ℕ))) / (P * Q * S^(4:ℕ))), ((-3*M*a*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ))), 0]], ![![0, 0, 0, ((-M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (S^(3:ℕ)))], ![0, 0, ((-M*a*u*(u - 1)*(u + 1)*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*M*r + a^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ))), 0], ![0, ((M*a*u*(u - 1)*(u + 1)*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*M*r + a^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ))), 0, 0], ![((M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (S^(3:ℕ))), 0, 0, 0]]], 
    ![![![0, ((-M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + 2*r^(2:ℕ))) / (S^(4:ℕ))), ((M*a^(2:ℕ)*u*(u - 1)*(u + 1)*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-4*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (D * S^(4:ℕ))), 0], ![((M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + 2*r^(2:ℕ))) / (S^(4:ℕ))), 0, 0, ((3*M*a*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ)))], ![((-M*a^(2:ℕ)*u*(u - 1)*(u + 1)*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-4*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (D * S^(4:ℕ))), 0, 0, ((M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-4*M*r - a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + 2*r^(2:ℕ))) / (D * S^(4:ℕ)))], ![0, ((-3*M*a*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ))), ((-M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-4*M*r - a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + 2*r^(2:ℕ))) / (D * S^(4:ℕ))), 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, 0, 0, ((M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (P * Q * D * S^(2:ℕ)))], ![0, 0, ((-M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (S^(3:ℕ))), 0], ![0, ((M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (S^(3:ℕ))), 0, 0], ![((-M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (P * Q * D * S^(2:ℕ))), 0, 0, 0]], ![![0, ((-3*M*a*r*(a^(2:ℕ) + r^(2:ℕ))*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ))), ((-M*a*u*(u - 1)*(u + 1)*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(4*M*a^(2:ℕ)*r*u^(2:ℕ) - 4*M*a^(2:ℕ)*r - 2*a^(4:ℕ)*u^(2:ℕ) + 3*a^(4:ℕ) - 2*a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) + 4*a^(2:ℕ)*r^(2:ℕ) + r^(4:ℕ))) / (D * S^(4:ℕ))), 0], ![((3*M*a*r*(a^(2:ℕ) + r^(2:ℕ))*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ))), 0, 0, ((-M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-2*a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ)))], ![((M*a*u*(u - 1)*(u + 1)*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(4*M*a^(2:ℕ)*r*u^(2:ℕ) - 4*M*a^(2:ℕ)*r - 2*a^(4:ℕ)*u^(2:ℕ) + 3*a^(4:ℕ) - 2*a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) + 4*a^(2:ℕ)*r^(2:ℕ) + r^(4:ℕ))) / (D * S^(4:ℕ))), 0, 0, ((M*a^(2:ℕ)*u*(u - 1)*(u + 1)*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-4*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (D * S^(4:ℕ)))], ![0, ((M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-2*a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ))), ((-M*a^(2:ℕ)*u*(u - 1)*(u + 1)*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-4*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (D * S^(4:ℕ))), 0]]], 
    ![![![0, ((-M*a^(2:ℕ)*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (S^(4:ℕ))), ((M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-2*a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ))), 0], ![((M*a^(2:ℕ)*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (S^(4:ℕ))), 0, 0, ((-M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*M*r - 2*a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + r^(2:ℕ))) / (P * Q * S^(4:ℕ)))], ![((-M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-2*a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ))), 0, 0, ((-3*M*a*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ)))], ![0, ((M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*M*r - 2*a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + r^(2:ℕ))) / (P * Q * S^(4:ℕ))), ((3*M*a*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ))), 0]], ![![0, 0, 0, ((-M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (P * Q * D * S^(2:ℕ)))], ![0, 0, ((M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (S^(3:ℕ))), 0], ![0, ((-M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (S^(3:ℕ))), 0, 0], ![((M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))) / (P * Q * D * S^(2:ℕ))), 0, 0, 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, ((M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(2*M*a^(2:ℕ)*r*u^(2:ℕ) - 2*M*a^(2:ℕ)*r - a^(4:ℕ)*u^(2:ℕ) + 3*a^(4:ℕ) - a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) + 5*a^(2:ℕ)*r^(2:ℕ) + 2*r^(4:ℕ))) / (S^(4:ℕ))), ((3*M*a*r*(a^(2:ℕ) + r^(2:ℕ))*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ))), 0], ![((-M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(2*M*a^(2:ℕ)*r*u^(2:ℕ) - 2*M*a^(2:ℕ)*r - a^(4:ℕ)*u^(2:ℕ) + 3*a^(4:ℕ) - a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) + 5*a^(2:ℕ)*r^(2:ℕ) + 2*r^(4:ℕ))) / (S^(4:ℕ))), 0, 0, ((-M*a^(2:ℕ)*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (S^(4:ℕ)))], ![((-3*M*a*r*(a^(2:ℕ) + r^(2:ℕ))*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ))), 0, 0, ((M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + 2*r^(2:ℕ))) / (S^(4:ℕ)))], ![0, ((M*a^(2:ℕ)*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (S^(4:ℕ))), ((-M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + 2*r^(2:ℕ))) / (S^(4:ℕ))), 0]]], 
    ![![![0, 0, 0, ((M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (S^(3:ℕ)))], ![0, 0, ((M*a*u*(u - 1)*(u + 1)*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*M*r + a^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ))), 0], ![0, ((-M*a*u*(u - 1)*(u + 1)*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*M*r + a^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ))), 0, 0], ![((-M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (S^(3:ℕ))), 0, 0, 0]], ![![0, ((3*M*a*r*(a^(2:ℕ) + r^(2:ℕ))*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ))), ((M*a*u*(u - 1)*(u + 1)*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(4*M*a^(2:ℕ)*r*u^(2:ℕ) - 4*M*a^(2:ℕ)*r - 2*a^(4:ℕ)*u^(2:ℕ) + 3*a^(4:ℕ) - 2*a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) + 4*a^(2:ℕ)*r^(2:ℕ) + r^(4:ℕ))) / (D * S^(4:ℕ))), 0], ![((-3*M*a*r*(a^(2:ℕ) + r^(2:ℕ))*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ))), 0, 0, ((M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-2*a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ)))], ![((-M*a*u*(u - 1)*(u + 1)*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(4*M*a^(2:ℕ)*r*u^(2:ℕ) - 4*M*a^(2:ℕ)*r - 2*a^(4:ℕ)*u^(2:ℕ) + 3*a^(4:ℕ) - 2*a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) + 4*a^(2:ℕ)*r^(2:ℕ) + r^(4:ℕ))) / (D * S^(4:ℕ))), 0, 0, ((-M*a^(2:ℕ)*u*(u - 1)*(u + 1)*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-4*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (D * S^(4:ℕ)))], ![0, ((-M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-2*a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ))), ((M*a^(2:ℕ)*u*(u - 1)*(u + 1)*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-4*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (D * S^(4:ℕ))), 0]], ![![0, ((-M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(2*M*a^(2:ℕ)*r*u^(2:ℕ) - 2*M*a^(2:ℕ)*r - a^(4:ℕ)*u^(2:ℕ) + 3*a^(4:ℕ) - a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) + 5*a^(2:ℕ)*r^(2:ℕ) + 2*r^(4:ℕ))) / (S^(4:ℕ))), ((-3*M*a*r*(a^(2:ℕ) + r^(2:ℕ))*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ))), 0], ![((M*a*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(2*M*a^(2:ℕ)*r*u^(2:ℕ) - 2*M*a^(2:ℕ)*r - a^(4:ℕ)*u^(2:ℕ) + 3*a^(4:ℕ) - a^(2:ℕ)*r^(2:ℕ)*u^(2:ℕ) + 5*a^(2:ℕ)*r^(2:ℕ) + 2*r^(4:ℕ))) / (S^(4:ℕ))), 0, 0, ((M*a^(2:ℕ)*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (S^(4:ℕ)))], ![((3*M*a*r*(a^(2:ℕ) + r^(2:ℕ))*(u - 1)*(u + 1)*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))) / (S^(4:ℕ))), 0, 0, ((-M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + 2*r^(2:ℕ))) / (S^(4:ℕ)))], ![0, ((-M*a^(2:ℕ)*u*(-a^(2:ℕ)*u^(2:ℕ) + 3*r^(2:ℕ))*(-2*M*r + 3*a^(2:ℕ) + 3*r^(2:ℕ))) / (S^(4:ℕ))), ((M*r*(-3*a^(2:ℕ)*u^(2:ℕ) + r^(2:ℕ))*(-a^(2:ℕ)*u^(2:ℕ) + 3*a^(2:ℕ) + 2*r^(2:ℕ))) / (S^(4:ℕ))), 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]]]]

variable {r u a M S D P Q : ℝ} (hS : S ≠ 0) (hD : D ≠ 0) (hP : P ≠ 0) (hQ : Q ≠ 0)
  (eS : S = r ^ 2 + a ^ 2 * u ^ 2) (eD : D = r ^ 2 - 2 * M * r + a ^ 2) (eP : P = u - 1) (eQ : Q = u + 1)
include hS hD hP hQ eS eD eP eQ

lemma KGiT_ok (m k : Fin 4) : ∑ l, KGT r u a M S D P Q m l * KGiT r u a M S D P Q l k = if m = k then 1 else 0 := by
  fin_cases m <;> fin_cases k <;> simp [Fin.sum_univ_four, KGT, KGiT] <;> (try field_simp) <;> (subst eS eD eP eQ; ring1)

lemma KGamT_ok (i j k : Fin 4) : GamF (KD1T r u a M S D P Q) (KGiT r u a M S D P Q) i j k = KGamT r u a M S D P Q i j k := by
  simp only [GamF]
  fin_cases i <;> fin_cases j <;> fin_cases k <;> simp [Fin.sum_univ_four, KD1T, KGiT, KGamT] <;>
    (try field_simp) <;> (subst eS eD eP eQ; ring1)

lemma KDGT_ok0 (i j k : Fin 4) : DGamF (KD1T r u a M S D P Q) (KD2T r u a M S D P Q) (KGiT r u a M S D P Q) 0 i j k = KDGT r u a M S D P Q 0 i j k := by
  simp only [DGamF, KGamT_ok hS hD hP hQ eS eD eP eQ]; fin_cases i <;> fin_cases j <;> fin_cases k <;> simp [Fin.sum_univ_four, KD2T, KD1T, KGiT, KGamT, KDGT] <;> (try field_simp) <;> (subst eS eD eP eQ; ring1)
lemma KDGT_ok1 (i j k : Fin 4) : DGamF (KD1T r u a M S D P Q) (KD2T r u a M S D P Q) (KGiT r u a M S D P Q) 1 i j k = KDGT r u a M S D P Q 1 i j k := by
  simp only [DGamF, KGamT_ok hS hD hP hQ eS eD eP eQ]; fin_cases i <;> fin_cases j <;> fin_cases k <;> simp [Fin.sum_univ_four, KD2T, KD1T, KGiT, KGamT, KDGT] <;> (try field_simp) <;> (subst eS eD eP eQ; ring1)
lemma KDGT_ok2 (i j k : Fin 4) : DGamF (KD1T r u a M S D P Q) (KD2T r u a M S D P Q) (KGiT r u a M S D P Q) 2 i j k = KDGT r u a M S D P Q 2 i j k := by
  simp only [DGamF, KGamT_ok hS hD hP hQ eS eD eP eQ]; fin_cases i <;> fin_cases j <;> fin_cases k <;> simp [Fin.sum_univ_four, KD2T, KD1T, KGiT, KGamT, KDGT] <;> (try field_simp) <;> (subst eS eD eP eQ; ring1)
lemma KDGT_ok3 (i j k : Fin 4) : DGamF (KD1T r u a M S D P Q) (KD2T r u a M S D P Q) (KGiT r u a M S D P Q) 3 i j k = KDGT r u a M S D P Q 3 i j k := by
  simp only [DGamF, KGamT_ok hS hD hP hQ eS eD eP eQ]; fin_cases i <;> fin_cases j <;> fin_cases k <;> simp [Fin.sum_univ_four, KD2T, KD1T, KGiT, KGamT, KDGT] <;> (try field_simp) <;> (subst eS eD eP eQ; ring1)
lemma KDGT_ok (w i j k : Fin 4) : DGamF (KD1T r u a M S D P Q) (KD2T r u a M S D P Q) (KGiT r u a M S D P Q) w i j k = KDGT r u a M S D P Q w i j k := by
  fin_cases w
  exacts [KDGT_ok0 hS hD hP hQ eS eD eP eQ i j k, KDGT_ok1 hS hD hP hQ eS eD eP eQ i j k, KDGT_ok2 hS hD hP hQ eS eD eP eQ i j k, KDGT_ok3 hS hD hP hQ eS eD eP eQ i j k]

lemma KRT_ok0 (j k l : Fin 4) : RiemF (KD1T r u a M S D P Q) (KD2T r u a M S D P Q) (KGiT r u a M S D P Q) 0 j k l = KRT r u a M S D P Q 0 j k l := by
  simp only [RiemF, KDGT_ok hS hD hP hQ eS eD eP eQ, KGamT_ok hS hD hP hQ eS eD eP eQ]; fin_cases j <;> fin_cases k <;> fin_cases l <;> simp [Fin.sum_univ_four, KDGT, KGamT, KRT] <;> (try field_simp) <;> (subst eS eD eP eQ; ring1)
lemma KRT_ok1 (j k l : Fin 4) : RiemF (KD1T r u a M S D P Q) (KD2T r u a M S D P Q) (KGiT r u a M S D P Q) 1 j k l = KRT r u a M S D P Q 1 j k l := by
  simp only [RiemF, KDGT_ok hS hD hP hQ eS eD eP eQ, KGamT_ok hS hD hP hQ eS eD eP eQ]; fin_cases j <;> fin_cases k <;> fin_cases l <;> simp [Fin.sum_univ_four, KDGT, KGamT, KRT] <;> (try field_simp) <;> (subst eS eD eP eQ; ring1)
lemma KRT_ok2 (j k l : Fin 4) : RiemF (KD1T r u a M S D P Q) (KD2T r u a M S D P Q) (KGiT r u a M S D P Q) 2 j k l = KRT r u a M S D P Q 2 j k l := by
  simp only [RiemF, KDGT_ok hS hD hP hQ eS eD eP eQ, KGamT_ok hS hD hP hQ eS eD eP eQ]; fin_cases j <;> fin_cases k <;> fin_cases l <;> simp [Fin.sum_univ_four, KDGT, KGamT, KRT] <;> (try field_simp) <;> (subst eS eD eP eQ; ring1)
lemma KRT_ok3 (j k l : Fin 4) : RiemF (KD1T r u a M S D P Q) (KD2T r u a M S D P Q) (KGiT r u a M S D P Q) 3 j k l = KRT r u a M S D P Q 3 j k l := by
  simp only [RiemF, KDGT_ok hS hD hP hQ eS eD eP eQ, KGamT_ok hS hD hP hQ eS eD eP eQ]; fin_cases j <;> fin_cases k <;> fin_cases l <;> simp [Fin.sum_univ_four, KDGT, KGamT, KRT] <;> (try field_simp) <;> (subst eS eD eP eQ; ring1)
lemma KRT_ok (i j k l : Fin 4) : RiemF (KD1T r u a M S D P Q) (KD2T r u a M S D P Q) (KGiT r u a M S D P Q) i j k l = KRT r u a M S D P Q i j k l := by
  fin_cases i
  exacts [KRT_ok0 hS hD hP hQ eS eD eP eQ j k l, KRT_ok1 hS hD hP hQ eS eD eP eQ j k l, KRT_ok2 hS hD hP hQ eS eD eP eQ j k l, KRT_ok3 hS hD hP hQ eS eD eP eQ j k l]

lemma KRDT_ok0 (n a' b : Fin 4) : lowR (Matrix.of (KGT r u a M S D P Q)) (KRT r u a M S D P Q) 0 n a' b = KRDT r u a M S D P Q 0 n a' b := by
  fin_cases n <;> fin_cases a' <;> fin_cases b <;> simp [lowR, Fin.sum_univ_four, KGT, KRT, KRDT] <;> (try field_simp) <;> (subst eS eD eP eQ; ring1)
lemma KRDT_ok1 (n a' b : Fin 4) : lowR (Matrix.of (KGT r u a M S D P Q)) (KRT r u a M S D P Q) 1 n a' b = KRDT r u a M S D P Q 1 n a' b := by
  fin_cases n <;> fin_cases a' <;> fin_cases b <;> simp [lowR, Fin.sum_univ_four, KGT, KRT, KRDT] <;> (try field_simp) <;> (subst eS eD eP eQ; ring1)
lemma KRDT_ok2 (n a' b : Fin 4) : lowR (Matrix.of (KGT r u a M S D P Q)) (KRT r u a M S D P Q) 2 n a' b = KRDT r u a M S D P Q 2 n a' b := by
  fin_cases n <;> fin_cases a' <;> fin_cases b <;> simp [lowR, Fin.sum_univ_four, KGT, KRT, KRDT] <;> (try field_simp) <;> (subst eS eD eP eQ; ring1)
lemma KRDT_ok3 (n a' b : Fin 4) : lowR (Matrix.of (KGT r u a M S D P Q)) (KRT r u a M S D P Q) 3 n a' b = KRDT r u a M S D P Q 3 n a' b := by
  fin_cases n <;> fin_cases a' <;> fin_cases b <;> simp [lowR, Fin.sum_univ_four, KGT, KRT, KRDT] <;> (try field_simp) <;> (subst eS eD eP eQ; ring1)
lemma KRDT_ok (m n a' b : Fin 4) : lowR (Matrix.of (KGT r u a M S D P Q)) (KRT r u a M S D P Q) m n a' b = KRDT r u a M S D P Q m n a' b := by
  fin_cases m
  exacts [KRDT_ok0 hS hD hP hQ eS eD eP eQ n a' b, KRDT_ok1 hS hD hP hQ eS eD eP eQ n a' b, KRDT_ok2 hS hD hP hQ eS eD eP eQ n a' b, KRDT_ok3 hS hD hP hQ eS eD eP eQ n a' b]

lemma KRUT_ok0 (n a' b : Fin 4) :
    raiseR (Matrix.of (KGT r u a M S D P Q)) (Matrix.of (KGiT r u a M S D P Q)) (KRT r u a M S D P Q) 0 n a' b = KRUT r u a M S D P Q 0 n a' b := by
  simp only [raiseR, KRDT_ok hS hD hP hQ eS eD eP eQ, Matrix.of_apply]; fin_cases n <;> fin_cases a' <;> fin_cases b <;> simp [Fin.sum_univ_four, KGiT, KRDT, KRUT] <;> (try field_simp) <;> (subst eS eD eP eQ; ring1)
lemma KRUT_ok1 (n a' b : Fin 4) :
    raiseR (Matrix.of (KGT r u a M S D P Q)) (Matrix.of (KGiT r u a M S D P Q)) (KRT r u a M S D P Q) 1 n a' b = KRUT r u a M S D P Q 1 n a' b := by
  simp only [raiseR, KRDT_ok hS hD hP hQ eS eD eP eQ, Matrix.of_apply]; fin_cases n <;> fin_cases a' <;> fin_cases b <;> simp [Fin.sum_univ_four, KGiT, KRDT, KRUT] <;> (try field_simp) <;> (subst eS eD eP eQ; ring1)
lemma KRUT_ok2 (n a' b : Fin 4) :
    raiseR (Matrix.of (KGT r u a M S D P Q)) (Matrix.of (KGiT r u a M S D P Q)) (KRT r u a M S D P Q) 2 n a' b = KRUT r u a M S D P Q 2 n a' b := by
  simp only [raiseR, KRDT_ok hS hD hP hQ eS eD eP eQ, Matrix.of_apply]; fin_cases n <;> fin_cases a' <;> fin_cases b <;> simp [Fin.sum_univ_four, KGiT, KRDT, KRUT] <;> (try field_simp) <;> (subst eS eD eP eQ; ring1)
lemma KRUT_ok3 (n a' b : Fin 4) :
    raiseR (Matrix.of (KGT r u a M S D P Q)) (Matrix.of (KGiT r u a M S D P Q)) (KRT r u a M S D P Q) 3 n a' b = KRUT r u a M S D P Q 3 n a' b := by
  simp only [raiseR, KRDT_ok hS hD hP hQ eS eD eP eQ, Matrix.of_apply]; fin_cases n <;> fin_cases a' <;> fin_cases b <;> simp [Fin.sum_univ_four, KGiT, KRDT, KRUT] <;> (try field_simp) <;> (subst eS eD eP eQ; ring1)
lemma KRUT_ok (m n a' b : Fin 4) :
    raiseR (Matrix.of (KGT r u a M S D P Q)) (Matrix.of (KGiT r u a M S D P Q)) (KRT r u a M S D P Q) m n a' b = KRUT r u a M S D P Q m n a' b := by
  fin_cases m
  exacts [KRUT_ok0 hS hD hP hQ eS eD eP eQ n a' b, KRUT_ok1 hS hD hP hQ eS eD eP eQ n a' b, KRUT_ok2 hS hD hP hQ eS eD eP eQ n a' b, KRUT_ok3 hS hD hP hQ eS eD eP eQ n a' b]

/-- **The `ε`-contraction from the tables**: `Σ ε^{mnrs} R_{mnab} R_{rs}{}^{ab} = −192M²a r u(3r² − a²u²)(r² − 3a²u²)/Σ⁵`. -/
lemma Kcontr_ok : (∑ m, ∑ n, ∑ r', ∑ s, (eps4 m n r' s : ℝ) * ∑ a', ∑ b,
      lowR (Matrix.of (KGT r u a M S D P Q)) (KRT r u a M S D P Q) m n a' b * raiseR (Matrix.of (KGT r u a M S D P Q)) (Matrix.of (KGiT r u a M S D P Q)) (KRT r u a M S D P Q) r' s a' b)
    = -192 * M^2 * a * r * u * (3*r^2 - a^2*u^2) * (r^2 - 3*a^2*u^2) / S^5 := by
  rw [sum_eps]
  simp only [KRDT_ok hS hD hP hQ eS eD eP eQ, KRUT_ok hS hD hP hQ eS eD eP eQ]
  simp [Fin.sum_univ_four, KRDT, KRUT]
  field_simp
  subst eS eD eP eQ; ring1

end KerrTables

#print axioms ShadowProbe.R89Pontryagin.Kcontr_ok

/-! ### Global smooth profiles (row 96's `rho`, copied) -/

section Profiles

/-- A smooth profile, `≥ ½` everywhere and equal to `s` for `s ≥ 3/2`. -/
noncomputable def rho (s : ℝ) : ℝ := 1 / 2 + (s - 1 / 2) * Real.smoothTransition (s - 1 / 2)

lemma rho_smooth : ContDiff ℝ ∞ rho :=
  contDiff_const.add ((contDiff_id.sub contDiff_const).mul
    ((Real.smoothTransition.contDiff (n := ⊤)).comp (contDiff_id.sub contDiff_const)))

lemma rho_ge (s : ℝ) : 1 / 2 ≤ rho s := by
  unfold rho
  rcases le_or_gt s (1 / 2) with h | h
  · rw [Real.smoothTransition.zero_of_nonpos (by linarith)]; simp
  · have := Real.smoothTransition.nonneg (s - 1 / 2)
    nlinarith

lemma rho_le (s : ℝ) : rho s ≤ max s (1 / 2) := by
  unfold rho
  rcases le_or_gt s (1 / 2) with h | h
  · rw [Real.smoothTransition.zero_of_nonpos (by linarith)]; simp
  · have := Real.smoothTransition.le_one (s - 1 / 2)
    have := le_max_left s (1 / 2)
    nlinarith

lemma rho_ne (s : ℝ) : rho s ≠ 0 := by have := rho_ge s; positivity

lemma rho_eq {s : ℝ} (h : 3 / 2 ≤ s) : rho s = s := by
  unfold rho; rw [Real.smoothTransition.one_of_one_le (by linarith)]; ring

end Profiles

/-! ## Part 1: Kerr — the metric, globally -/

section KerrMetric

/-- **Kerr in Boyer–Lindquist coordinates with `u = cos θ`** (the receipt's `kerr_bl`), entries as functions of
`(r, u)`: `Σ = r² + a²u²`, `Δ = r² − 2Mr + a²`, `1 − u² = sin²θ`. -/
noncomputable def kform (M a r u : ℝ) : Fin 4 → Fin 4 → ℝ :=
  ![![-1 + 2 * M * (r * (r ^ 2 + a ^ 2 * u ^ 2)⁻¹), 0, 0, -2 * M * a * (r * ((1 - u ^ 2) * (r ^ 2 + a ^ 2 * u ^ 2)⁻¹))],
    ![0, (r ^ 2 + a ^ 2 * u ^ 2) * (r ^ 2 - 2 * M * r + a ^ 2)⁻¹, 0, 0],
    ![0, 0, (r ^ 2 + a ^ 2 * u ^ 2) * (1 - u ^ 2)⁻¹, 0],
    ![-2 * M * a * (r * ((1 - u ^ 2) * (r ^ 2 + a ^ 2 * u ^ 2)⁻¹)), 0, 0,
      (r ^ 2 + a ^ 2 + 2 * M * a ^ 2 * (r * ((1 - u ^ 2) * (r ^ 2 + a ^ 2 * u ^ 2)⁻¹))) * (1 - u ^ 2)]]

/-- The radial clamp: `≥ 2|M| + 1` everywhere, `= r` for `r ≥ 2|M| + 2`. -/
noncomputable def rK (M s : ℝ) : ℝ := 2 * |M| + 1 / 2 + rho (s - 2 * |M| - 1 / 2)

/-- The polar clamp: `|qK u| ≤ 7/16` everywhere, `= u` for `|u| ≤ 5/16`. -/
noncomputable def loK (u : ℝ) : ℝ := (rho (8 * u + 4) - 4) / 8
noncomputable def qK (u : ℝ) : ℝ := -loK (-loK u)

lemma rK_ge (M s : ℝ) : 2 * |M| + 1 ≤ rK M s := by have := rho_ge (s - 2 * |M| - 1 / 2); unfold rK; linarith

lemma rK_eq {M s : ℝ} (h : 2 * |M| + 2 ≤ s) : rK M s = s := by unfold rK; rw [rho_eq (by linarith)]; ring

lemma loK_ge (u : ℝ) : -7 / 16 ≤ loK u := by have := rho_ge (8 * u + 4); unfold loK; linarith

lemma loK_le {u : ℝ} (h : u ≤ 7 / 16) : loK u ≤ 7 / 16 := by
  have := rho_le (8 * u + 4); unfold loK
  have : max (8 * u + 4) (1 / 2) ≤ 15 / 2 := max_le (by linarith) (by norm_num)
  linarith

lemma loK_eq {u : ℝ} (h : -5 / 16 ≤ u) : loK u = u := by unfold loK; rw [rho_eq (by linarith)]; ring

lemma qK_bd (u : ℝ) : -7 / 16 ≤ qK u ∧ qK u ≤ 7 / 16 := by
  have h1 := loK_ge u
  have h2 := loK_ge (-loK u)
  have h3 := loK_le (u := -loK u) (by linarith)
  unfold qK; constructor <;> linarith

lemma qK_eq {u : ℝ} (h1 : -5 / 16 ≤ u) (h2 : u ≤ 5 / 16) : qK u = u := by
  unfold qK; rw [loK_eq h1, loK_eq (by linarith)]; ring

lemma rK_smooth (M : ℝ) : ContDiff ℝ ∞ (rK M) :=
  contDiff_const.add (rho_smooth.comp (by fun_prop))

lemma qK_smooth : ContDiff ℝ ∞ qK := by
  have hl : ContDiff ℝ ∞ loK :=
    ((rho_smooth.comp ((contDiff_const.mul contDiff_id).add contDiff_const)).sub contDiff_const).div_const _
  exact (hl.comp (hl.neg)).neg

/-- **The Kerr metric on all of `ℝ⁴`**: the receipt's entries at `(rK(r), qK(u))`, which is Kerr itself on the open
region `KU` (`r > 2|M| + 2`, `|u| < 5/16`) and smooth and nondegenerate everywhere. -/
noncomputable def KerrExt (M a : ℝ) (i j : Fin 4) (y : Fin 4 → ℝ) : ℝ := kform M a (rK M (y 1)) (qK (y 2)) i j

/-- The region where `KerrExt` is Kerr. -/
def KU (M : ℝ) : Set (Fin 4 → ℝ) := {y | 2 * |M| + 2 < y 1 ∧ -5 / 16 < y 2 ∧ y 2 < 5 / 16}

lemma KU_open (M : ℝ) : IsOpen (KU M) :=
  (isOpen_lt continuous_const (continuous_apply 1)).inter
    ((isOpen_lt continuous_const (continuous_apply 2)).inter (isOpen_lt (continuous_apply 2) continuous_const))

lemma KerrExt_ev (M a : ℝ) {p : Fin 4 → ℝ} (hp : p ∈ KU M) (i j : Fin 4) :
    KerrExt M a i j =ᶠ[𝓝 p] fun y => kform M a (y 1) (y 2) i j :=
  Filter.mem_of_superset ((KU_open M).mem_nhds hp) fun y hy => by
    simp only [Set.mem_setOf_eq, KerrExt]
    rw [rK_eq hy.1.le, qK_eq hy.2.1.le hy.2.2.le]

lemma KerrExt_symm (M a : ℝ) (i j : Fin 4) (y : Fin 4 → ℝ) : KerrExt M a i j y = KerrExt M a j i y := by
  fin_cases i <;> fin_cases j <;> simp [KerrExt, kform]

section Pos
variable (M a s v : ℝ)

lemma kS_pos : 0 < rK M s ^ 2 + a ^ 2 * qK v ^ 2 := by
  have h : 0 < rK M s := by have := rK_ge M s; have := abs_nonneg M; linarith
  positivity

lemma kD_pos : 0 < rK M s ^ 2 - 2 * M * rK M s + a ^ 2 := by
  have h := rK_ge M s; have h1 := le_abs_self M; have h2 := abs_nonneg M
  nlinarith [sq_nonneg a]

lemma kQ_pos : 0 < 1 - qK v ^ 2 := by
  obtain ⟨h1, h2⟩ := qK_bd v; nlinarith

end Pos

lemma KerrExt_smooth (M a : ℝ) (i j : Fin 4) : ContDiff ℝ ∞ (KerrExt M a i j) := by
  have hr : ContDiff ℝ ∞ (fun y : Fin 4 → ℝ => rK M (y 1)) := (rK_smooth M).comp (contDiff_apply ℝ ℝ 1)
  have hq : ContDiff ℝ ∞ (fun y : Fin 4 → ℝ => qK (y 2)) := qK_smooth.comp (contDiff_apply ℝ ℝ 2)
  have hS : ContDiff ℝ ∞ (fun y : Fin 4 → ℝ => (rK M (y 1) ^ 2 + a ^ 2 * qK (y 2) ^ 2)⁻¹) :=
    ((hr.pow 2).add (contDiff_const.mul (hq.pow 2))).inv fun y => (kS_pos M a _ _).ne'
  have hD : ContDiff ℝ ∞ (fun y : Fin 4 → ℝ => (rK M (y 1) ^ 2 - 2 * M * rK M (y 1) + a ^ 2)⁻¹) :=
    (((hr.pow 2).sub (contDiff_const.mul hr)).add contDiff_const).inv fun y => (kD_pos M a _).ne'
  have hQ : ContDiff ℝ ∞ (fun y : Fin 4 → ℝ => (1 - qK (y 2) ^ 2)⁻¹) :=
    (contDiff_const.sub (hq.pow 2)).inv fun y => (kQ_pos (y 2)).ne'
  have hQ' : ContDiff ℝ ∞ (fun y : Fin 4 → ℝ => 1 - qK (y 2) ^ 2) := contDiff_const.sub (hq.pow 2)
  have hS' : ContDiff ℝ ∞ (fun y : Fin 4 → ℝ => rK M (y 1) ^ 2 + a ^ 2 * qK (y 2) ^ 2) :=
    (hr.pow 2).add (contDiff_const.mul (hq.pow 2))
  fin_cases i <;> fin_cases j <;> simp only [KerrExt, kform] <;> simp <;>
    first
    | exact contDiff_const
    | exact contDiff_const.add (contDiff_const.mul (hr.mul hS))
    | exact contDiff_const.mul (hr.mul (hQ'.mul hS))
    | exact hS'.mul hD
    | exact hS'.mul hQ
    | exact ((((hr.pow 2).add contDiff_const).add (contDiff_const.mul (hr.mul (hQ'.mul hS))))).mul hQ'
    | fun_prop

/-- And conversely (row 96's): an invertible matrix at every point is a nondegenerate form. -/
lemma nondeg_of_det {G : Fin 4 → Fin 4 → (Fin 4 → ℝ) → ℝ} (hd : ∀ p, (gm G p).det ≠ 0) (p : Fin 4 → ℝ) (u : Fin 4 → ℝ)
    (h : ∀ v, formG G p u v = 0) : u = 0 := by
  refine Matrix.eq_zero_of_vecMul_eq_zero (hd p) (funext fun j => ?_)
  have := h (Pi.single j 1)
  rw [formG_apply] at this
  simpa [Matrix.vecMul, dotProduct, gm, Pi.single_apply, mul_comm] using this

/-- The determinant of the Boyer–Lindquist form is `−Σ²`. -/
lemma kform_det {M a r u : ℝ} (hS : r ^ 2 + a ^ 2 * u ^ 2 ≠ 0) (hD : r ^ 2 - 2 * M * r + a ^ 2 ≠ 0)
    (hQ : 1 - u ^ 2 ≠ 0) : (Matrix.of (kform M a r u)).det = -(r ^ 2 + a ^ 2 * u ^ 2) ^ 2 := by
  unfold kform
  generalize eS : r ^ 2 + a ^ 2 * u ^ 2 = S at hS ⊢
  generalize eD : r ^ 2 - 2 * M * r + a ^ 2 = D at hD ⊢
  generalize eQ : 1 - u ^ 2 = Q at hQ ⊢
  simp [Matrix.det_succ_row_zero, Fin.sum_univ_succ,
    show (Fin.succAbove 1 2 : Fin 4) = 3 by decide, show (Fin.succAbove 3 2 : Fin 4) = 2 by decide]
  field_simp
  subst eS eD eQ; ring

lemma KerrExt_nondeg (M a : ℝ) : ∀ p (u : Fin 4 → ℝ), (∀ v, formG (KerrExt M a) p u v = 0) → u = 0 :=
  nondeg_of_det fun y => by
    have e : gm (KerrExt M a) y = Matrix.of (kform M a (rK M (y 1)) (qK (y 2))) := by ext i j; rfl
    rw [e, kform_det (kS_pos M a _ _).ne' (kD_pos M a _).ne' (kQ_pos _).ne']
    exact neg_ne_zero.2 (pow_ne_zero 2 (kS_pos M a _ _).ne')

end KerrMetric

/-! ### The jets of the Kerr entries at a point of `KU` -/

section KerrJets

variable (M a : ℝ) (p : Fin 4 → ℝ)

lemma jR2 : HasJ (fun y => y 1 ^ 2) p (p 1 ^ 2) ![0, 2 * p 1, 0, 0] ![0, ![0, 2, 0, 0], 0, 0] :=
  (((hasJ_coord 1 p).mul (hasJ_coord 1 p)).congr (Eventually.of_forall fun y => by ring)).of_eq (by ring)
    (fun c => by fin_cases c <;> simp <;> ring) (fun a' c => by fin_cases a' <;> fin_cases c <;> simp <;> ring)

lemma jS : HasJ (fun y => y 1 ^ 2 + a ^ 2 * y 2 ^ 2) p (p 1 ^ 2 + a ^ 2 * p 2 ^ 2) ![0, 2 * p 1, 2 * a ^ 2 * p 2, 0]
    ![0, ![0, 2, 0, 0], ![0, 0, 2 * a ^ 2, 0], 0] :=
  (((hasJ_coord 1 p).mul (hasJ_coord 1 p)).add (((hasJ_coord 2 p).mul (hasJ_coord 2 p)).const_mul (a ^ 2))).congr
    (Eventually.of_forall fun y => by ring) |>.of_eq (by ring)
    (fun c => by fin_cases c <;> simp <;> ring) (fun a' c => by fin_cases a' <;> fin_cases c <;> simp <;> ring)

lemma jD : HasJ (fun y => y 1 ^ 2 - 2 * M * y 1 + a ^ 2) p (p 1 ^ 2 - 2 * M * p 1 + a ^ 2)
    ![0, 2 * p 1 - 2 * M, 0, 0] ![0, ![0, 2, 0, 0], 0, 0] :=
  (((hasJ_coord 1 p).mul (hasJ_coord 1 p)).add (((hasJ_coord 1 p).const_mul (-2 * M)).add (hasJ_const (a ^ 2) p))).congr
    (Eventually.of_forall fun y => by ring) |>.of_eq (by ring)
    (fun c => by fin_cases c <;> simp <;> ring) (fun a' c => by fin_cases a' <;> fin_cases c <;> simp <;> ring)

lemma jQ : HasJ (fun y => 1 - y 2 ^ 2) p (1 - p 2 ^ 2) ![0, 0, -2 * p 2, 0] ![0, 0, ![0, 0, -2, 0], 0] :=
  ((hasJ_const 1 p).add (((hasJ_coord 2 p).mul (hasJ_coord 2 p)).const_mul (-1))).congr
    (Eventually.of_forall fun y => by ring) |>.of_eq (by ring)
    (fun c => by fin_cases c <;> simp <;> ring) (fun a' c => by fin_cases a' <;> fin_cases c <;> simp <;> ring)

variable {M a p} (hp : p ∈ KU M) {S D P Q : ℝ} (hS : S ≠ 0) (hD : D ≠ 0) (hP : P ≠ 0) (hQ : Q ≠ 0)
  (eS : S = p 1 ^ 2 + a ^ 2 * p 2 ^ 2) (eD : D = p 1 ^ 2 - 2 * M * p 1 + a ^ 2) (eP : P = p 2 - 1) (eQ : Q = p 2 + 1)
include hp hS hD hP hQ eS eD eP eQ

/-- **The entries' jets at `p` are the tables** `KGT`, `KD1T`, `KD2T` (denominators as atoms `S, D, P, Q`). -/
lemma kerr_jets (i j : Fin 4) :
    HasJ (KerrExt M a i j) p (KGT (p 1) (p 2) a M S D P Q i j) (KD1T (p 1) (p 2) a M S D P Q i j)
      (KD2T (p 1) (p 2) a M S D P Q i j) := by
  have jS' := (jS a p).of_eq eS.symm (fun _ => rfl) (fun _ _ => rfl)
  have jD' := (jD M a p).of_eq eD.symm (fun _ => rfl) (fun _ _ => rfl)
  have jQ' := (jQ p).of_eq (show 1 - p 2 ^ 2 = -(P * Q) by rw [eP, eQ]; ring) (fun _ => rfl) (fun _ _ => rfl)
  have hPQ : -(P * Q) ≠ 0 := neg_ne_zero.2 (mul_ne_zero hP hQ)
  have jSi := jS'.inv hS
  have jDi := jD'.inv hD
  have jQi := jQ'.inv hPQ
  have jr := hasJ_coord 1 p
  have j0 := (hasJ_const (-1) p).add ((jr.mul jSi).const_mul (2 * M))
  have j3 := (jr.mul (jQ'.mul jSi)).const_mul (-2 * M * a)
  have j11 := jS'.mul jDi
  have j22 := jS'.mul jQi
  have j33 := ((((jR2 p).add (hasJ_const (a ^ 2) p)).add ((jr.mul (jQ'.mul jSi)).const_mul (2 * M * a ^ 2)))).mul jQ'
  have hz : ∀ i j, (∀ y : Fin 4 → ℝ, kform M a (y 1) (y 2) i j = 0) → KGT (p 1) (p 2) a M S D P Q i j = 0 →
      KD1T (p 1) (p 2) a M S D P Q i j = 0 → KD2T (p 1) (p 2) a M S D P Q i j = 0 →
      HasJ (KerrExt M a i j) p (KGT (p 1) (p 2) a M S D P Q i j) (KD1T (p 1) (p 2) a M S D P Q i j)
        (KD2T (p 1) (p 2) a M S D P Q i j) :=
    fun i j h1 h2 h3 h4 => ((hasJ_const 0 p).congr ((KerrExt_ev M a hp i j).trans (Eventually.of_forall h1))).of_eq
      h2.symm (fun c => by rw [h3]; rfl) fun a c => by rw [h4]; rfl
  have h00 : HasJ (KerrExt M a 0 0) p (KGT (p 1) (p 2) a M S D P Q 0 0) (KD1T (p 1) (p 2) a M S D P Q 0 0) (KD2T (p 1) (p 2) a M S D P Q 0 0) :=
    (j0.congr ((KerrExt_ev M a hp _ _).trans (Eventually.of_forall fun y => by simp [kform]))).of_eq
      (by simp [KGT]; field_simp; subst eS eD eP eQ; ring)
      (fun c => by fin_cases c <;> simp [KD1T] <;> field_simp <;> (subst eS eD eP eQ; ring))
      (fun a' c => by fin_cases a' <;> fin_cases c <;> simp [KD2T] <;> field_simp <;> (subst eS eD eP eQ; ring))
  have h03 : HasJ (KerrExt M a 0 3) p (KGT (p 1) (p 2) a M S D P Q 0 3) (KD1T (p 1) (p 2) a M S D P Q 0 3) (KD2T (p 1) (p 2) a M S D P Q 0 3) :=
    (j3.congr ((KerrExt_ev M a hp _ _).trans (Eventually.of_forall fun y => by simp [kform]))).of_eq
      (by simp [KGT]; field_simp; subst eS eD eP eQ; ring)
      (fun c => by fin_cases c <;> simp [KD1T] <;> field_simp <;> (subst eS eD eP eQ; ring))
      (fun a' c => by fin_cases a' <;> fin_cases c <;> simp [KD2T] <;> field_simp <;> (subst eS eD eP eQ; ring))
  have h30 : HasJ (KerrExt M a 3 0) p (KGT (p 1) (p 2) a M S D P Q 3 0) (KD1T (p 1) (p 2) a M S D P Q 3 0) (KD2T (p 1) (p 2) a M S D P Q 3 0) :=
    (j3.congr ((KerrExt_ev M a hp _ _).trans (Eventually.of_forall fun y => by simp [kform]))).of_eq
      (by simp [KGT]; field_simp; subst eS eD eP eQ; ring)
      (fun c => by fin_cases c <;> simp [KD1T] <;> field_simp <;> (subst eS eD eP eQ; ring))
      (fun a' c => by fin_cases a' <;> fin_cases c <;> simp [KD2T] <;> field_simp <;> (subst eS eD eP eQ; ring))
  have h11 : HasJ (KerrExt M a 1 1) p (KGT (p 1) (p 2) a M S D P Q 1 1) (KD1T (p 1) (p 2) a M S D P Q 1 1) (KD2T (p 1) (p 2) a M S D P Q 1 1) :=
    (j11.congr ((KerrExt_ev M a hp _ _).trans (Eventually.of_forall fun y => by simp [kform]))).of_eq
      (by simp [KGT]; field_simp; subst eS eD eP eQ; ring)
      (fun c => by fin_cases c <;> simp [KD1T] <;> field_simp <;> (subst eS eD eP eQ; ring))
      (fun a' c => by fin_cases a' <;> fin_cases c <;> simp [KD2T] <;> field_simp <;> (subst eS eD eP eQ; ring))
  have h22 : HasJ (KerrExt M a 2 2) p (KGT (p 1) (p 2) a M S D P Q 2 2) (KD1T (p 1) (p 2) a M S D P Q 2 2) (KD2T (p 1) (p 2) a M S D P Q 2 2) :=
    (j22.congr ((KerrExt_ev M a hp _ _).trans (Eventually.of_forall fun y => by simp [kform]))).of_eq
      (by simp [KGT]; field_simp; subst eS eD eP eQ; ring)
      (fun c => by fin_cases c <;> simp [KD1T] <;> field_simp <;> (subst eS eD eP eQ; ring))
      (fun a' c => by fin_cases a' <;> fin_cases c <;> simp [KD2T] <;> field_simp <;> (subst eS eD eP eQ; ring))
  have h33 : HasJ (KerrExt M a 3 3) p (KGT (p 1) (p 2) a M S D P Q 3 3) (KD1T (p 1) (p 2) a M S D P Q 3 3) (KD2T (p 1) (p 2) a M S D P Q 3 3) :=
    (j33.congr ((KerrExt_ev M a hp _ _).trans (Eventually.of_forall fun y => by simp [kform]))).of_eq
      (by simp [KGT]; field_simp; subst eS eD eP eQ; ring)
      (fun c => by fin_cases c <;> simp [KD1T] <;> field_simp <;> (subst eS eD eP eQ; ring))
      (fun a' c => by fin_cases a' <;> fin_cases c <;> simp [KD2T] <;> field_simp <;> (subst eS eD eP eQ; ring))
  fin_cases i <;> fin_cases j
  all_goals first | exact h00 | exact h03 | exact h30 | exact h11 | exact h22 | exact h33 | skip
  all_goals refine hz _ _ ?_ ?_ ?_ ?_
  all_goals first | (intro y; simp [kform]; done) | (simp [KGT, KD1T, KD2T]; done)

end KerrJets

/-! ### The density -/

section KerrHeadline

/-- **The receipt's closed form** `−96M²a r u(3r² − a²u²)(r² − 3a²u²)/Σ⁶`. -/
noncomputable def kerrClosed (M a r u : ℝ) : ℝ :=
  -96 * M ^ 2 * a * r * u * (3 * r ^ 2 - a ^ 2 * u ^ 2) * (r ^ 2 - 3 * a ^ 2 * u ^ 2) / (r ^ 2 + a ^ 2 * u ^ 2) ^ 6

lemma KU_facts {M a : ℝ} {p : Fin 4 → ℝ} (hp : p ∈ KU M) :
    p 1 ^ 2 + a ^ 2 * p 2 ^ 2 ≠ 0 ∧ p 1 ^ 2 - 2 * M * p 1 + a ^ 2 ≠ 0 ∧ 1 - p 2 ^ 2 ≠ 0 ∧ p 2 - 1 ≠ 0 ∧ p 2 + 1 ≠ 0 := by
  obtain ⟨h1, h2, h3⟩ := hp
  have hM := le_abs_self M; have hM' := abs_nonneg M
  have h0 : 0 < p 1 := by linarith
  refine ⟨by positivity, by nlinarith [sq_nonneg a], by nlinarith, by linarith, by linarith⟩

/-- **Part 1, Kerr, for symbolic `M` and `a`**: THE connection's `*RR` of the Boyer–Lindquist metric is the closed form
at every point of the region `KU` (`r > 2|M| + 2`, `|cos θ| < 5/16`), where `KerrExt` is Kerr. -/
theorem kerr_pontryagin (M a : ℝ) {p : Fin 4 → ℝ} (hp : p ∈ KU M) :
    pontryaginLC (KerrExt M a) (KerrExt_symm M a) (KerrExt_nondeg M a) (KerrExt_smooth M a) p
      = kerrClosed M a (p 1) (p 2) := by
  obtain ⟨hS, hD, hQ, hu1, hu2⟩ := KU_facts (a := a) hp
  set S := p 1 ^ 2 + a ^ 2 * p 2 ^ 2 with eS
  set D := p 1 ^ 2 - 2 * M * p 1 + a ^ 2 with eD
  set P := p 2 - 1 with eP
  set Q := p 2 + 1 with eQ
  have J := kerr_jets hp hS hD hu1 hu2 eS eD eP eQ
  have hg : ∀ i j, KerrExt M a i j p = KGT (p 1) (p 2) a M S D P Q i j := fun i j => (J i j).v0
  have hinv : ∀ m k, ∑ l, KerrExt M a m l p * KGiT (p 1) (p 2) a M S D P Q l k = if m = k then 1 else 0 := fun m k => by
    simp only [hg]; exact KGiT_ok hS hD hu1 hu2 eS eD eP eQ m k
  rw [tabs_bridge _ _ _ hg hinv (fun i j c => (J i j).d1At c) (fun i j a c => (J i j).d2At a c)]
  have hR : RiemF (KD1T (p 1) (p 2) a M S D P Q) (KD2T (p 1) (p 2) a M S D P Q) (KGiT (p 1) (p 2) a M S D P Q)
      = KRT (p 1) (p 2) a M S D P Q := by
    funext i j k l; exact KRT_ok hS hD hu1 hu2 eS eD eP eQ i j k l
  have hdet : (Matrix.of (KGT (p 1) (p 2) a M S D P Q)).det = -S ^ 2 := by
    simp [Matrix.det_succ_row_zero, Fin.sum_univ_succ, KGT,
      show (Fin.succAbove 1 2 : Fin 4) = 3 by decide, show (Fin.succAbove 3 2 : Fin 4) = 2 by decide]
    field_simp; rw [eS, eD, eP, eQ]; ring
  have hpos : 0 < S := lt_of_le_of_ne (by positivity) (Ne.symm hS)
  rw [hR, pontArr, Kcontr_ok hS hD hu1 hu2 eS eD eP eQ, hdet, neg_neg, Real.sqrt_sq hpos.le]
  unfold kerrClosed; rw [← eS]; field_simp; ring

/-- The closed form is **odd in the spin**, for symbolic `a`. -/
theorem kerrClosed_odd (M a r u : ℝ) : kerrClosed M (-a) r u = -kerrClosed M a r u := by
  unfold kerrClosed; ring

/-- **`*RR(a) + *RR(−a) = 0`** on `KU`, for every `M` and `a`. -/
theorem kerr_odd (M a : ℝ) {p : Fin 4 → ℝ} (hp : p ∈ KU M) :
    pontryaginLC (KerrExt M a) (KerrExt_symm M a) (KerrExt_nondeg M a) (KerrExt_smooth M a) p
      + pontryaginLC (KerrExt M (-a)) (KerrExt_symm M (-a)) (KerrExt_nondeg M (-a)) (KerrExt_smooth M (-a)) p = 0 := by
  rw [kerr_pontryagin M a hp, kerr_pontryagin M (-a) hp, kerrClosed_odd]; ring

/-- **The receipt's three spins at `M = 1`**: `*RR(1/2) + *RR(−1/2) = 0` and `*RR(0) = 0` on `KU`. -/
theorem kerr_receipt_odd {p : Fin 4 → ℝ} (hp : p ∈ KU 1) :
    pontryaginLC (KerrExt 1 (1 / 2)) (KerrExt_symm 1 _) (KerrExt_nondeg 1 _) (KerrExt_smooth 1 _) p
      + pontryaginLC (KerrExt 1 (-(1 / 2))) (KerrExt_symm 1 _) (KerrExt_nondeg 1 _) (KerrExt_smooth 1 _) p = 0 :=
  kerr_odd 1 (1 / 2) hp

theorem kerr_receipt_zero {p : Fin 4 → ℝ} (hp : p ∈ KU 1) :
    pontryaginLC (KerrExt 1 0) (KerrExt_symm 1 0) (KerrExt_nondeg 1 0) (KerrExt_smooth 1 0) p = 0 := by
  rw [kerr_pontryagin 1 0 hp]; unfold kerrClosed; simp

/-- **`*RR(1/2) ≠ 0`**: at `r = 10`, `cos θ = 1/4` (a point of `KU 1`). -/
theorem kerr_receipt_ne :
    pontryaginLC (KerrExt 1 (1 / 2)) (KerrExt_symm 1 _) (KerrExt_nondeg 1 _) (KerrExt_smooth 1 _) ![0, 10, 1 / 4, 0] ≠ 0 := by
  have hp : (![0, 10, 1 / 4, 0] : Fin 4 → ℝ) ∈ KU 1 := by
    simp only [KU, Set.mem_setOf_eq]; norm_num
  rw [kerr_pontryagin 1 (1 / 2) hp]; unfold kerrClosed; norm_num

/-- **The type-D route**: the closed form is `−48 Im Ψ₂²` with `Ψ₂ = −M/(r − iau)³`. -/
theorem kerr_psi2 (M a r u : ℝ) (hS : r ^ 2 + a ^ 2 * u ^ 2 ≠ 0) :
    kerrClosed M a r u = -48 * ((-(M : ℂ) / ((r : ℂ) - a * u * Complex.I) ^ 3) ^ 2).im := by
  set z : ℂ := (r : ℂ) - a * u * Complex.I with hz'
  set w : ℂ := (r : ℂ) + a * u * Complex.I with hw
  have hz : z * w = ((r ^ 2 + a ^ 2 * u ^ 2 : ℝ) : ℂ) := by
    rw [hz', hw]; push_cast; ring_nf; rw [Complex.I_sq]; ring
  have hS' : ((r ^ 2 + a ^ 2 * u ^ 2 : ℝ) : ℂ) ≠ 0 := by exact_mod_cast hS
  have hz0 : z ≠ 0 := fun h => hS' (by rw [← hz, h, zero_mul])
  have hw0 : w ≠ 0 := fun h => hS' (by rw [← hz, h, mul_zero])
  have key : (-(M : ℂ) / z ^ 3) ^ 2 = ((M ^ 2 / (r ^ 2 + a ^ 2 * u ^ 2) ^ 6 : ℝ) : ℂ) * w ^ 6 := by
    calc (-(M : ℂ) / z ^ 3) ^ 2 = (M : ℂ) ^ 2 * w ^ 6 / (z ^ 6 * w ^ 6) := by field_simp
      _ = (M : ℂ) ^ 2 * w ^ 6 / ((r ^ 2 + a ^ 2 * u ^ 2 : ℝ) : ℂ) ^ 6 := by rw [← mul_pow, hz]
      _ = ((M ^ 2 / (r ^ 2 + a ^ 2 * u ^ 2) ^ 6 : ℝ) : ℂ) * w ^ 6 := by push_cast; ring
  rw [key, Complex.im_ofReal_mul, hw]
  simp [pow_succ, Complex.mul_im, Complex.mul_re]
  unfold kerrClosed
  field_simp
  ring

end KerrHeadline

#print axioms ShadowProbe.R89Pontryagin.kerr_pontryagin
#print axioms ShadowProbe.R89Pontryagin.kerrClosed_odd
#print axioms ShadowProbe.R89Pontryagin.kerr_odd
#print axioms ShadowProbe.R89Pontryagin.kerr_receipt_odd
#print axioms ShadowProbe.R89Pontryagin.kerr_receipt_zero
#print axioms ShadowProbe.R89Pontryagin.kerr_receipt_ne
#print axioms ShadowProbe.R89Pontryagin.kerr_psi2

/-! ## Part 5: `*RR ≡ 0` on every static member, from the parity lemma with `k = t` -/

section Static

/-- The coordinate `t = x⁰`. -/
def Pt : Fin 4 → Bool := fun i => decide (i = 0)

variable {G : Fin 4 → Fin 4 → (Fin 4 → ℝ) → ℝ} (hs : ∀ i j p, G i j p = G j i p)
  (hn : ∀ p (u : Fin 4 → ℝ), (∀ v, formG G p u v = 0) → u = 0) (hGs : ∀ i j, ContDiff ℝ ∞ (G i j))

include hn hGs in
/-- **The static theorem.** If `G` does not mix `t` with the other coordinates (`g_{tj} = 0`, `j ≠ t`) and does not
depend on `t`, THE connection's `*RR` vanishes at every point: the parity lemma with `k = t` (`ε` forces exactly one
`t` index, and every curvature component with an odd number of `t`'s is zero). -/
theorem static_pontryagin_zero (hz : ∀ j, j ≠ 0 → ∀ y, G 0 j y = 0)
    (hI : ∀ i j y (c : ℝ), G i j (y + c • Pi.single 0 1) = G i j y) (p : Fin 4 → ℝ) :
    pontryaginLC G hs hn hGs p = 0 := by
  refine pontryagin_parity hs hn hGs Pt (fun i j h y => ?_) (fun k hk i j y c => ?_) (by decide) p
  · fin_cases i <;> fin_cases j <;> simp [pb, Pt] at h
    all_goals first | exact hz _ (by decide) y | (rw [hs]; exact hz _ (by decide) y)
  · simp [Pt] at hk; subst hk; exact hI i j y c

/-- **A static diagonal metric** `diag(F₀, F₁, F₂, F₃)`. -/
noncomputable def diagG (F : Fin 4 → (Fin 4 → ℝ) → ℝ) : Fin 4 → Fin 4 → (Fin 4 → ℝ) → ℝ :=
  fun i j y => if i = j then F i y else 0

variable {F : Fin 4 → (Fin 4 → ℝ) → ℝ}

lemma diagG_symm (F : Fin 4 → (Fin 4 → ℝ) → ℝ) (i j : Fin 4) (y : Fin 4 → ℝ) : diagG F i j y = diagG F j i y := by
  unfold diagG; by_cases h : i = j <;> simp [h, eq_comm]

lemma diagG_smooth (hF : ∀ i, ContDiff ℝ ∞ (F i)) (i j : Fin 4) : ContDiff ℝ ∞ (diagG F i j) := by
  unfold diagG; by_cases h : i = j <;> simp [h, hF, contDiff_const]

lemma diagG_nondeg (h0 : ∀ i y, F i y ≠ 0) : ∀ p (u : Fin 4 → ℝ), (∀ v, formG (diagG F) p u v = 0) → u = 0 :=
  nondeg_of_det fun y => by
    have e : gm (diagG F) y = Matrix.diagonal fun i => F i y := by
      ext i j; simp [gm, diagG, Matrix.diagonal_apply]
    rw [e, Matrix.det_diagonal]; exact Finset.prod_ne_zero_iff.2 fun i _ => h0 i y

/-- A function that does not depend on `t`. -/
def NoT (f : (Fin 4 → ℝ) → ℝ) : Prop := ∀ y (c : ℝ), f (y + c • Pi.single 0 1) = f y

/-- **Every static diagonal metric, profiles arbitrary**: `*RR ≡ 0`. -/
theorem diag_static_zero (hF : ∀ i, ContDiff ℝ ∞ (F i)) (h0 : ∀ i y, F i y ≠ 0) (hT : ∀ i, NoT (F i))
    (p : Fin 4 → ℝ) : pontryaginLC (diagG F) (diagG_symm F) (diagG_nondeg h0) (diagG_smooth hF) p = 0 :=
  static_pontryagin_zero (diagG_symm F) (diagG_nondeg h0) (diagG_smooth hF)
    (fun j hj y => by simp [diagG, Ne.symm hj]) (fun i j y c => by simp only [diagG]; split_ifs <;> simp [hT i y c]) p

lemma noT_of {f : (Fin 4 → ℝ) → ℝ} (h : ∀ y y' : Fin 4 → ℝ, y 1 = y' 1 → y 2 = y' 2 → f y = f y') : NoT f :=
  fun y c => h _ _ (by simp) (by simp)

/-- **Family 2**, `diag(−f(r), h(r), S(r)², S(r)² k(θ))`, `f, h, S` ARBITRARY. -/
noncomputable def sph2F (f h S k : ℝ → ℝ) : Fin 4 → (Fin 4 → ℝ) → ℝ :=
  ![fun y => -f (y 1), fun y => h (y 1), fun y => S (y 1) ^ 2, fun y => S (y 1) ^ 2 * k (y 2)]

/-- **Family 3, the static Weyl form** `diag(−e^{2U}, e^{2K−2U}, e^{2K−2U}, e^{−2U} W)`, `U, K` ARBITRARY smooth
functions of `(r, θ)` (`W` stands for `r² sin²θ`, any nowhere-zero profile of `(r, θ)`). -/
noncomputable def weylF (U K W : (Fin 4 → ℝ) → ℝ) : Fin 4 → (Fin 4 → ℝ) → ℝ :=
  ![fun y => -Real.exp (2 * U y), fun y => Real.exp (2 * K y - 2 * U y), fun y => Real.exp (2 * K y - 2 * U y),
    fun y => Real.exp (-2 * U y) * W y]

variable {f h S k : ℝ → ℝ} (hf : ContDiff ℝ ∞ f) (hh : ContDiff ℝ ∞ h) (hS : ContDiff ℝ ∞ S) (hk : ContDiff ℝ ∞ k)
  (hf0 : ∀ s, f s ≠ 0) (hh0 : ∀ s, h s ≠ 0) (hS0 : ∀ s, S s ≠ 0) (hk0 : ∀ s, k s ≠ 0)

lemma noT_sph2 (f h S k : ℝ → ℝ) : ∀ i, NoT (sph2F f h S k i) := by
  intro i; fin_cases i <;> exact noT_of fun y y' h1 h2 => by simp [sph2F, h1, h2]

include hf hh hS hk in
lemma sph2_smooth : ∀ i, ContDiff ℝ ∞ (sph2F f h S k i) := by
  have c1 := fun {g : ℝ → ℝ} (hg : ContDiff ℝ ∞ g) => hg.comp (contDiff_apply ℝ ℝ (1 : Fin 4))
  have c2 := fun {g : ℝ → ℝ} (hg : ContDiff ℝ ∞ g) => hg.comp (contDiff_apply ℝ ℝ (2 : Fin 4))
  intro i; fin_cases i
  exacts [(c1 hf).neg, c1 hh, (c1 hS).pow 2, ((c1 hS).pow 2).mul (c2 hk)]

include hf0 hh0 hS0 hk0 in
lemma sph2_ne : ∀ i y, sph2F f h S k i y ≠ 0 := by
  intro i y; fin_cases i <;> simp [sph2F, hf0, hh0, hS0, hk0]

include hf hh hS hk hf0 hh0 hS0 hk0 in
/-- **Family 2**: `*RR ≡ 0` for `diag(−f(r), h(r), S(r)², S(r)² k(θ))`, all four profiles arbitrary. -/
theorem static_fhS_zero (p : Fin 4 → ℝ) :
    pontryaginLC (diagG (sph2F f h S k)) (diagG_symm _) (diagG_nondeg (sph2_ne hf0 hh0 hS0 hk0))
      (diagG_smooth (sph2_smooth hf hh hS hk)) p = 0 :=
  diag_static_zero (sph2_smooth hf hh hS hk) (sph2_ne hf0 hh0 hS0 hk0) (noT_sph2 f h S k) p

include hf hS hk hf0 hS0 hk0 in
/-- **Family 1**: `*RR ≡ 0` for `diag(−f(r), 1/f(r), S(r)², S(r)² k(θ))`, `f` arbitrary. -/
theorem static_f_zero (p : Fin 4 → ℝ) :
    pontryaginLC (diagG (sph2F f (fun s => (f s)⁻¹) S k)) (diagG_symm _)
      (diagG_nondeg (sph2_ne hf0 (fun s => inv_ne_zero (hf0 s)) hS0 hk0))
      (diagG_smooth (sph2_smooth hf (hf.inv hf0) hS hk)) p = 0 :=
  diag_static_zero (sph2_smooth hf (hf.inv hf0) hS hk) (sph2_ne hf0 (fun s => inv_ne_zero (hf0 s)) hS0 hk0)
    (noT_sph2 _ _ _ _) p

/-- **The named static members** (Schwarzschild `1 − 2M/r`, Schwarzschild–de Sitter `1 − 2M/r − r²/α²`, de Sitter
`1 − r²/α²`, the Nariai member at `2M = 2α/(3√3)`) are instances of family 1: for ANY global profile `f` agreeing
with the named one on a radial range, `*RR ≡ 0` (the equality is not used: the vanishing holds for every `f`). -/
noncomputable def namedF (M α : ℝ) : Fin 4 → ℝ → ℝ :=
  ![fun r => 1 - 2 * M / r, fun r => 1 - 2 * M / r - r ^ 2 / α ^ 2, fun r => 1 - r ^ 2 / α ^ 2,
    fun r => 1 - 2 * (α / (3 * Real.sqrt 3)) / r - r ^ 2 / α ^ 2]

include hf hS hk hf0 hS0 hk0 in
theorem static_named_zero (M α : ℝ) (n : Fin 4) (I : Set ℝ) (hfn : Set.EqOn f (namedF M α n) I) (p : Fin 4 → ℝ) :
    pontryaginLC (diagG (sph2F f (fun s => (f s)⁻¹) S k)) (diagG_symm _)
      (diagG_nondeg (sph2_ne hf0 (fun s => inv_ne_zero (hf0 s)) hS0 hk0))
      (diagG_smooth (sph2_smooth hf (hf.inv hf0) hS hk)) p = 0 :=
  static_f_zero hf hS hk hf0 hS0 hk0 p

variable {U K W : (Fin 4 → ℝ) → ℝ} (hU : ContDiff ℝ ∞ U) (hK : ContDiff ℝ ∞ K) (hW : ContDiff ℝ ∞ W)
  (hW0 : ∀ y, W y ≠ 0) (hUt : NoT U) (hKt : NoT K) (hWt : NoT W)

include hU hK hW hW0 in
lemma weyl_smooth : ∀ i, ContDiff ℝ ∞ (weylF U K W i) := by
  intro i; fin_cases i
  exacts [(contDiff_const.mul hU).exp.neg, ((contDiff_const.mul hK).sub (contDiff_const.mul hU)).exp,
    ((contDiff_const.mul hK).sub (contDiff_const.mul hU)).exp, (contDiff_const.mul hU).exp.mul hW]

include hW0 in
lemma weyl_ne : ∀ i y, weylF U K W i y ≠ 0 := by
  intro i y; fin_cases i <;> simp [weylF, Real.exp_ne_zero, hW0]

include hUt hKt hWt in
lemma weyl_noT : ∀ i, NoT (weylF U K W i) := by
  intro i y c; fin_cases i <;> simp [weylF, hUt y c, hKt y c, hWt y c]

include hU hK hW hW0 hUt hKt hWt in
/-- **Family 3, the static Weyl form**: `*RR ≡ 0`, `U, K` arbitrary functions of the non-`t` coordinates. -/
theorem static_weyl_zero (p : Fin 4 → ℝ) :
    pontryaginLC (diagG (weylF U K W)) (diagG_symm _) (diagG_nondeg (weyl_ne hW0))
      (diagG_smooth (weyl_smooth hU hK hW hW0)) p = 0 :=
  diag_static_zero (weyl_smooth hU hK hW hW0) (weyl_ne hW0) (weyl_noT hUt hKt hWt) p

/-- **Kerr at `a = 0` (Schwarzschild in Boyer–Lindquist form) by the same lemma**, at EVERY point, not only on `KU`:
`g_{tφ} = 0` when `a = 0` and nothing depends on `t`. -/
theorem kerr_static_zero (M : ℝ) (p : Fin 4 → ℝ) :
    pontryaginLC (KerrExt M 0) (KerrExt_symm M 0) (KerrExt_nondeg M 0) (KerrExt_smooth M 0) p = 0 :=
  static_pontryagin_zero _ _ _ (fun j hj y => by fin_cases j <;> simp [KerrExt, kform] at hj ⊢)
    (fun i j y c => by simp [KerrExt]) p

end Static

#print axioms ShadowProbe.R89Pontryagin.static_pontryagin_zero
#print axioms ShadowProbe.R89Pontryagin.diag_static_zero
#print axioms ShadowProbe.R89Pontryagin.static_f_zero
#print axioms ShadowProbe.R89Pontryagin.static_fhS_zero
#print axioms ShadowProbe.R89Pontryagin.static_named_zero
#print axioms ShadowProbe.R89Pontryagin.static_weyl_zero
#print axioms ShadowProbe.R89Pontryagin.kerr_static_zero

/-! ## Part 2: the channel charges `3 / 2 / 0 / 1 / 0`, read off the generator of the determinant circle -/

section Charges

open Complex Matrix

/-- The determinant circle `w(θ) = e^{iθ}`, acting on the seats as `V(θ) = w(θ)·1₃` and on the conjugate seats as
`V̄(θ) = w̄(θ)·1₃`. -/
noncomputable def wθ (θ : ℝ) : ℂ := Complex.exp (θ * I)
noncomputable def Vc (θ : ℝ) : Matrix (Fin 3) (Fin 3) ℂ := wθ θ • 1
noncomputable def Vbar (θ : ℝ) : Matrix (Fin 3) (Fin 3) ℂ := starRingEnd ℂ (wθ θ) • 1

/-- The receipt's basis `e₀∧e₁, e₀∧e₂, e₁∧e₂` of `Λ²`, and the induced action by `2 × 2` minors. -/
def basis2 : Fin 3 → Fin 2 → Fin 3 := ![![0, 1], ![0, 2], ![1, 2]]
def lam2 (g : Matrix (Fin 3) (Fin 3) ℂ) : Matrix (Fin 3) (Fin 3) ℂ := Matrix.of fun I J =>
  g (basis2 I 0) (basis2 J 0) * g (basis2 I 1) (basis2 J 1) - g (basis2 I 0) (basis2 J 1) * g (basis2 I 1) (basis2 J 0)

/-- **The generator** of a representation `ρ(θ)`: entrywise `(d/dθ) ρ(θ)` at `θ = 0`, divided by `i` (the receipt's
`charges`). -/
noncomputable def gen {n : Type*} (ρ : ℝ → Matrix n n ℂ) : Matrix n n ℂ :=
  Matrix.of fun i j => deriv (fun θ => ρ θ i j) 0 / I

lemma hasDerivAt_phase (q : ℝ) : HasDerivAt (fun θ : ℝ => Complex.exp (((q * θ : ℝ) : ℂ) * I)) (q * I) 0 := by
  have h := (((hasDerivAt_id (0 : ℝ)).const_mul q).ofReal_comp.mul_const I).cexp
  simpa using h

/-- A representation acting as the phase `e^{iqθ}` has generator `q·1`. -/
lemma gen_phase {n : Type*} [DecidableEq n] (q : ℝ) {ρ : ℝ → Matrix n n ℂ}
    (hρ : ∀ θ, ρ θ = Complex.exp (((q * θ : ℝ) : ℂ) * I) • 1) : gen ρ = (q : ℂ) • 1 := by
  ext i j
  simp only [gen, hρ, Matrix.of_apply, Matrix.smul_apply, smul_eq_mul]
  rw [((hasDerivAt_phase q).mul_const ((1 : Matrix n n ℂ) i j)).deriv]
  field_simp

/-- **The charges are the eigenvalues**: a generator `q·1` has the single eigenvalue `q`. -/
theorem eig_scalar {n : Type*} [Fintype n] [DecidableEq n] (q μ : ℂ) :
    (∃ v : n → ℂ, v ≠ 0 ∧ ((q • 1 : Matrix n n ℂ) *ᵥ v) = μ • v) ↔ (μ = q ∧ Nonempty n) := by
  constructor
  · rintro ⟨v, hv, h⟩
    rw [Matrix.smul_mulVec, Matrix.one_mulVec] at h
    obtain ⟨i, hi⟩ : ∃ i, v i ≠ 0 := by
      by_contra hc; apply hv; funext i; by_contra h; exact hc ⟨i, h⟩
    have := congrFun h i
    simp only [Pi.smul_apply, smul_eq_mul] at this
    exact ⟨(mul_right_cancel₀ hi this).symm, ⟨i⟩⟩
  · rintro ⟨rfl, ⟨i⟩⟩
    exact ⟨Pi.single i 1, by simp, by rw [Matrix.smul_mulVec, Matrix.one_mulVec]⟩

lemma wθ_pow (θ : ℝ) (k : ℕ) : wθ θ ^ k = Complex.exp ((((k : ℝ) * θ : ℝ) : ℂ) * I) := by
  rw [wθ, ← Complex.exp_nat_mul]; congr 1; push_cast; ring

lemma wθ_conj (θ : ℝ) : wθ θ * starRingEnd ℂ (wθ θ) = 1 := by
  rw [wθ, ← Complex.exp_conj, ← Complex.exp_add]
  simp [Complex.conj_ofReal]

/-- **Baryon, `Λ³V`**: `det V(θ) = e^{3iθ}`, generator `3`. -/
theorem baryon_charge : gen (fun θ => (Matrix.of fun _ _ => (Vc θ).det : Matrix (Fin 1) (Fin 1) ℂ)) = (3 : ℂ) • 1 := by
  have := gen_phase (n := Fin 1) 3 (ρ := fun θ => (Matrix.of fun _ _ => (Vc θ).det)) fun θ => by
    ext i j; fin_cases i; fin_cases j
    simp [Vc, Matrix.det_smul, wθ_pow]
  simpa using this

/-- **Diquark, `Λ²V`** (the `2 × 2` minors): `Λ²V(θ) = e^{2iθ}·1`, generator `2`. -/
theorem diquark_charge : gen (fun θ => lam2 (Vc θ)) = (2 : ℂ) • 1 := by
  have hlam : ∀ θ, lam2 (Vc θ) = wθ θ ^ 2 • 1 := fun θ => by
    ext i j; fin_cases i <;> fin_cases j <;> simp [lam2, basis2, Vc, Matrix.one_apply] <;> ring
  have := gen_phase 2 (ρ := fun θ => lam2 (Vc θ)) fun θ => by rw [hlam θ, wθ_pow]; norm_num
  simpa using this

/-- **Meson, `V ⊗ V̄`**: `V(θ) ⊗ V̄(θ) = 1`, generator `0`. -/
theorem meson_charge : gen (fun θ => Matrix.kronecker (Vc θ) (Vbar θ)) = (0 : ℂ) • 1 := by
  have := gen_phase (n := Fin 3 × Fin 3) 0 (ρ := fun θ => Matrix.kronecker (Vc θ) (Vbar θ)) fun θ => by
    ext ⟨i, i'⟩ ⟨j, j'⟩
    simp only [Vc, Vbar, Matrix.kronecker, Matrix.kroneckerMap_apply, Matrix.smul_apply, Matrix.one_apply, smul_eq_mul]
    rw [show (((0 : ℝ) * θ : ℝ) : ℂ) * I = 0 by simp, Complex.exp_zero]
    by_cases h1 : i = j <;> by_cases h2 : i' = j' <;> simp [h1, h2, Prod.ext_iff]
    linear_combination wθ_conj θ
  simpa using this

/-- **One seat, `V`**: generator `1`. -/
theorem seat_charge : gen Vc = (1 : ℂ) • 1 := by
  have := gen_phase 1 (ρ := Vc) fun θ => by simp [Vc, wθ]
  simpa using this

/-- **Calibration**: the trivial representation has generator `0`. -/
theorem trivial_charge : gen (fun _ : ℝ => (1 : Matrix (Fin 2) (Fin 2) ℂ)) = (0 : ℂ) • 1 := by
  have := gen_phase (n := Fin 2) 0 (ρ := fun _ => 1) fun θ => by simp
  simpa using this

end Charges

/-! ## Part 3: the linear trace `A = Σ₊ q − Σ₋ q`, and the chirality convention -/

section Traces

/-- The receipt's `coefficient(plus, minus, sign)`. -/
def coefficient (plus minus : List ℤ) (sign : ℤ := 1) : ℤ := sign * (plus.sum - minus.sum)

theorem wall_content : coefficient [1, 1, 1] [] = 3 := rfl
theorem vector_like : coefficient [1, 1, 1] [1, 1, 1] = 0 := rfl
theorem vector_like_both_conventions :
    coefficient [1, 1, 1] [1, 1, 1] 1 = 0 ∧ coefficient [1, 1, 1] [1, 1, 1] (-1) = 0 := ⟨rfl, rfl⟩
/-- The convention flips the sign of `3` and never sends it to zero. -/
theorem wall_conventions : coefficient [1, 1, 1] [] 1 = 3 ∧ coefficient [1, 1, 1] [] (-1) = -3 := ⟨rfl, rfl⟩
theorem one_seat : coefficient [1] [] = 1 := rfl
theorem turnaround_lift : coefficient [1, 1] [1] = 1 := rfl

end Traces

/-! ## Part 4: a constant phase commutes with the derivative, and its Noether current is conserved -/

section Current4

open Complex Matrix

/-- **`D(gΨ) − g DΨ = g′Ψ`** for differentiable `g, Ψ`. -/
theorem local_residual {g Ψ : ℝ → ℂ} {x : ℝ} (hg : DifferentiableAt ℝ g x) (hΨ : DifferentiableAt ℝ Ψ x) :
    deriv (fun y => g y * Ψ y) x - g x * deriv Ψ x = deriv g x * Ψ x := by
  rw [deriv_fun_mul hg hΨ]; ring

/-- It is nonzero for a non-constant `g` (`g(x) = x`, `Ψ = 1`). -/
theorem local_residual_ne : deriv (fun y : ℝ => (y : ℂ) * 1) 0 - ((0 : ℝ) : ℂ) * deriv (fun _ : ℝ => (1 : ℂ)) 0 ≠ 0 := by
  have : deriv (fun y : ℝ => (y : ℂ) * 1) 0 = 1 := by
    simpa using ((hasDerivAt_id (0 : ℝ)).ofReal_comp).deriv
  rw [this]; simp

/-- **A constant phase commutes**: `D(e^{iθ₀}Ψ) − e^{iθ₀}DΨ = 0`, for every `Ψ`. -/
theorem global_residual (θ₀ : ℝ) (Ψ : ℝ → ℂ) (x : ℝ) :
    deriv (fun y => Complex.exp (θ₀ * I) * Ψ y) x - Complex.exp (θ₀ * I) * deriv Ψ x = 0 := by
  rw [deriv_const_mul_field']; ring

/-- The receipt's Dirac matrices (Dirac basis). -/
def γ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ := ![
  !![1, 0, 0, 0; 0, 1, 0, 0; 0, 0, -1, 0; 0, 0, 0, -1],
  !![0, 0, 0, 1; 0, 0, 1, 0; 0, -1, 0, 0; -1, 0, 0, 0],
  !![0, 0, 0, -I; 0, 0, I, 0; 0, I, 0, 0; -I, 0, 0, 0],
  !![0, 0, 1, 0; 0, 0, 0, -1; -1, 0, 0, 0; 0, 1, 0, 0]]

/-- `η = diag(1, −1, −1, −1)`. -/
def η : Fin 4 → Fin 4 → ℂ := fun μ ν => if μ = ν then (if μ = 0 then 1 else -1) else 0

/-- **The Clifford relation** `γ^μγ^ν + γ^νγ^μ = 2η^{μν}·1`. -/
theorem clifford (μ ν : Fin 4) : γ μ * γ ν + γ ν * γ μ = (2 * η μ ν) • 1 := by
  fin_cases μ <;> fin_cases ν <;> ext i j <;> fin_cases i <;> fin_cases j <;>
    simp [γ, η, Matrix.mul_apply, Fin.sum_univ_four, Matrix.one_apply] <;> ring_nf <;> simp [Complex.I_sq] <;> ring

lemma γ00 : γ 0 * γ 0 = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [γ, Matrix.mul_apply, Fin.sum_univ_four, Matrix.one_apply]

/-- The spatial part `Σₖ γ^k ∂ₖΨ`. -/
noncomputable def spat (d : Fin 4 → Fin 4 → ℂ) : Fin 4 → ℂ := γ 1 *ᵥ d 1 + γ 2 *ᵥ d 2 + γ 3 *ᵥ d 3

/-- The time derivative the Dirac equation `iγ^μ∂_μΨ = mΨ` forces, given `Ψ` and the free spatial derivatives:
`∂₀Ψ = −iγ⁰(mΨ − iΣₖγ^k∂ₖΨ)` (the receipt's `ON_SHELL`). -/
noncomputable def onShell (Ψ : Fin 4 → ℂ) (d : Fin 4 → Fin 4 → ℂ) (m : ℝ) : Fin 4 → ℂ :=
  (-I) • (γ 0 *ᵥ ((m : ℂ) • Ψ - I • spat d))

/-- The Dirac equation with `∂₀Ψ = d₀`. -/
def dirac (Ψ : Fin 4 → ℂ) (d0 : Fin 4 → ℂ) (d : Fin 4 → Fin 4 → ℂ) (m : ℝ) : Prop :=
  I • (γ 0 *ᵥ d0 + spat d) = (m : ℂ) • Ψ

/-- **The Dirac equation fixes `∂₀Ψ`**: `onShell` solves it, and it is the only solution. -/
theorem dirac_fixes (Ψ : Fin 4 → ℂ) (d : Fin 4 → Fin 4 → ℂ) (m : ℝ) (d0 : Fin 4 → ℂ) :
    dirac Ψ d0 d m ↔ d0 = onShell Ψ d m := by
  have hI : (-I) * I = 1 := by rw [neg_mul, I_mul_I, neg_neg]
  have e1 : dirac Ψ d0 d m ↔ γ 0 *ᵥ d0 + spat d = (-I * m) • Ψ := by
    unfold dirac; constructor
    · intro h; have := congrArg (fun v => (-I) • v) h
      simp only [smul_smul, hI, one_smul] at this; exact this
    · intro h; rw [h, smul_smul]; congr 1; rw [← mul_assoc, mul_neg, I_mul_I, neg_neg, one_mul]
  have e2 : onShell Ψ d m = γ 0 *ᵥ ((-I * m) • Ψ - spat d) := by
    unfold onShell
    rw [← Matrix.mulVec_smul, smul_sub, smul_smul, smul_smul, hI, one_smul]
  rw [e1, e2]
  constructor
  · intro h; rw [← h, add_sub_cancel_right, Matrix.mulVec_mulVec, γ00, Matrix.one_mulVec]
  · intro h; rw [h, Matrix.mulVec_mulVec, γ00, Matrix.one_mulVec, sub_add_cancel]

/-- `Ψ̄ γ^μ Φ = Σᵢⱼ Ψ̄ᵢ (γ⁰γ^μ)ᵢⱼ Φⱼ`. -/
noncomputable def bil (Ψ Φ : Fin 4 → ℂ) (μ : Fin 4) : ℂ := ∑ i, ∑ j, starRingEnd ℂ (Ψ i) * (γ 0 * γ μ) i j * Φ j

/-- `∂_μ(Ψ̄γ^μΨ) = Σ_μ (∂_μΨ̄ γ^μ Ψ + Ψ̄ γ^μ ∂_μΨ)`, with `∂₀Ψ = d0` and `∂ₖΨ = d k`. -/
noncomputable def divJ (Ψ d0 : Fin 4 → ℂ) (d : Fin 4 → Fin 4 → ℂ) : ℂ :=
  (bil d0 Ψ 0 + bil Ψ d0 0) + (bil (d 1) Ψ 1 + bil Ψ (d 1) 1) + (bil (d 2) Ψ 2 + bil Ψ (d 2) 2)
    + (bil (d 3) Ψ 3 + bil Ψ (d 3) 3)

/-- **The current is conserved on shell**: `∂_μ(Ψ̄γ^μΨ) = 0` for every spinor, every mass and every choice of the
spatial derivatives (32 real unknowns), when `∂₀Ψ` is the one the Dirac equation forces. -/
theorem div_onShell (Ψ : Fin 4 → ℂ) (d : Fin 4 → Fin 4 → ℂ) (m : ℝ) : divJ Ψ (onShell Ψ d m) d = 0 := by
  simp only [divJ, bil, onShell, spat, Matrix.mulVec, dotProduct, Fin.sum_univ_four, γ, Matrix.mul_apply,
    Pi.smul_apply, Pi.sub_apply, Pi.add_apply, smul_eq_mul]
  simp [Matrix.vecHead, Matrix.vecTail]
  apply Complex.ext <;> simp [Complex.mul_re, Complex.mul_im, Complex.conj_re, Complex.conj_im] <;> ring

/-- **Control**: off shell (`∂₀Ψ` shifted by `δ`) the divergence is `⟨δ, Ψ⟩ + ⟨Ψ, δ⟩ = 2 Re⟨δ, Ψ⟩`. -/
theorem div_offShell (Ψ δ : Fin 4 → ℂ) (d : Fin 4 → Fin 4 → ℂ) (m : ℝ) :
    divJ Ψ (onShell Ψ d m + δ) d = ∑ i, (starRingEnd ℂ (δ i) * Ψ i + starRingEnd ℂ (Ψ i) * δ i) := by
  have h0 := div_onShell Ψ d m
  have e : ∀ v w : Fin 4 → ℂ, bil v w 0 = ∑ i, starRingEnd ℂ (v i) * w i := fun v w => by
    simp only [bil, γ00, Matrix.one_apply]; simp
  have e1 : bil (onShell Ψ d m + δ) Ψ 0 = bil (onShell Ψ d m) Ψ 0 + ∑ i, starRingEnd ℂ (δ i) * Ψ i := by
    rw [e, e, ← Finset.sum_add_distrib]; simp [add_mul]
  have e2 : bil Ψ (onShell Ψ d m + δ) 0 = bil Ψ (onShell Ψ d m) 0 + ∑ i, starRingEnd ℂ (Ψ i) * δ i := by
    rw [e, e, ← Finset.sum_add_distrib]; simp [mul_add]
  unfold divJ at h0 ⊢
  rw [e1, e2, Finset.sum_add_distrib]
  linear_combination h0

/-- At `Ψ = δ = e₀` (and `m = 0`, `∂ₖΨ = 0`) the off-shell divergence is `2 ≠ 0`. -/
theorem div_offShell_ne : divJ (Pi.single 0 1) (onShell (Pi.single 0 1) 0 0 + Pi.single 0 1) 0 ≠ 0 := by
  rw [div_offShell]; simp [Fin.sum_univ_four]

/-- **`j⁰ = Ψ̄γ⁰Ψ = Σ|Ψᵢ|²`**: a count, not a signed charge. -/
theorem density_count (Ψ : Fin 4 → ℂ) : bil Ψ Ψ 0 = ((∑ i, Complex.normSq (Ψ i) : ℝ) : ℂ) := by
  simp only [bil, γ00, Matrix.one_apply]
  simp [Complex.normSq_eq_conj_mul_self]

end Current4

#print axioms ShadowProbe.R89Pontryagin.eig_scalar
#print axioms ShadowProbe.R89Pontryagin.baryon_charge
#print axioms ShadowProbe.R89Pontryagin.diquark_charge
#print axioms ShadowProbe.R89Pontryagin.meson_charge
#print axioms ShadowProbe.R89Pontryagin.seat_charge
#print axioms ShadowProbe.R89Pontryagin.trivial_charge
#print axioms ShadowProbe.R89Pontryagin.wall_content
#print axioms ShadowProbe.R89Pontryagin.vector_like_both_conventions
#print axioms ShadowProbe.R89Pontryagin.wall_conventions
#print axioms ShadowProbe.R89Pontryagin.turnaround_lift
#print axioms ShadowProbe.R89Pontryagin.local_residual
#print axioms ShadowProbe.R89Pontryagin.local_residual_ne
#print axioms ShadowProbe.R89Pontryagin.global_residual
#print axioms ShadowProbe.R89Pontryagin.clifford
#print axioms ShadowProbe.R89Pontryagin.dirac_fixes
#print axioms ShadowProbe.R89Pontryagin.div_onShell
#print axioms ShadowProbe.R89Pontryagin.div_offShell
#print axioms ShadowProbe.R89Pontryagin.div_offShell_ne
#print axioms ShadowProbe.R89Pontryagin.density_count

/-! ## Part 6: the general unpolarised Gowdy form, four arbitrary functions of `(t, z)` — the tables -/

section GowdyTables

/-- The 2-jet at the point: `ea = e^{2A}`, `ep = e^{2ψ}`, and the first and second `(t, z)`-partials of `A, ψ, ω, R`
(`1 = ∂_t`, `2 = ∂_z`, `11 = ∂_t²`, `12 = ∂_t∂_z`, `22 = ∂_z²`), with the values `w0 = ω`, `r0 = R`. -/
structure GJ where
  ea : ℝ
  ep : ℝ
  a1 : ℝ
  a2 : ℝ
  a11 : ℝ
  a12 : ℝ
  a22 : ℝ
  p1 : ℝ
  p2 : ℝ
  p11 : ℝ
  p12 : ℝ
  p22 : ℝ
  w0 : ℝ
  w1 : ℝ
  w2 : ℝ
  w11 : ℝ
  w12 : ℝ
  w22 : ℝ
  r0 : ℝ
  r1 : ℝ
  r2 : ℝ
  r11 : ℝ
  r12 : ℝ
  r22 : ℝ

noncomputable def WGT (J : GJ) : Fin 4 → Fin 4 → ℝ :=
  ![![(-J.ea), 0, 0, 0], 
    ![0, (J.ea), 0, 0], 
    ![0, 0, (J.ep), (J.ep*J.w0)], 
    ![0, 0, (J.ep*J.w0), ((J.ep^(2:ℕ)*J.w0^(2:ℕ) + J.r0^(2:ℕ)) / ((J.ep)))]]

noncomputable def WGiT (J : GJ) : Fin 4 → Fin 4 → ℝ :=
  ![![((-1) / ((J.ea))), 0, 0, 0], 
    ![0, ((1) / ((J.ea))), 0, 0], 
    ![0, 0, ((J.ep^(2:ℕ)*J.w0^(2:ℕ) + J.r0^(2:ℕ)) / ((J.ep) * (J.r0)^(2:ℕ))), ((-J.ep*J.w0) / ((J.r0)^(2:ℕ)))], 
    ![0, 0, ((-J.ep*J.w0) / ((J.r0)^(2:ℕ))), ((J.ep) / ((J.r0)^(2:ℕ)))]]

noncomputable def WD1T (J : GJ) : Fin 4 → Fin 4 → Fin 4 → ℝ :=
  ![![![(-2*J.a1*J.ea), (-2*J.a2*J.ea), 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], 
    ![![0, 0, 0, 0], ![(2*J.a1*J.ea), (2*J.a2*J.ea), 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], 
    ![![0, 0, 0, 0], ![0, 0, 0, 0], ![(2*J.ep*J.p1), (2*J.ep*J.p2), 0, 0], ![(J.ep*(2*J.p1*J.w0 + J.w1)), (J.ep*(2*J.p2*J.w0 + J.w2)), 0, 0]], 
    ![![0, 0, 0, 0], ![0, 0, 0, 0], ![(J.ep*(2*J.p1*J.w0 + J.w1)), (J.ep*(2*J.p2*J.w0 + J.w2)), 0, 0], ![((2*(J.ep^(2:ℕ)*J.p1*J.w0^(2:ℕ) + J.ep^(2:ℕ)*J.w0*J.w1 - J.p1*J.r0^(2:ℕ) + J.r0*J.r1)) / ((J.ep))), ((2*(J.ep^(2:ℕ)*J.p2*J.w0^(2:ℕ) + J.ep^(2:ℕ)*J.w0*J.w2 - J.p2*J.r0^(2:ℕ) + J.r0*J.r2)) / ((J.ep))), 0, 0]]]

noncomputable def WD2T (J : GJ) : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ :=
  ![![![![(-2*J.ea*(2*J.a1^(2:ℕ) + J.a11)), (-2*J.ea*(2*J.a1*J.a2 + J.a12)), 0, 0], ![(-2*J.ea*(2*J.a1*J.a2 + J.a12)), (-2*J.ea*(2*J.a2^(2:ℕ) + J.a22)), 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]]], 
    ![![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![(2*J.ea*(2*J.a1^(2:ℕ) + J.a11)), (2*J.ea*(2*J.a1*J.a2 + J.a12)), 0, 0], ![(2*J.ea*(2*J.a1*J.a2 + J.a12)), (2*J.ea*(2*J.a2^(2:ℕ) + J.a22)), 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]]], 
    ![![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![(2*J.ep*(2*J.p1^(2:ℕ) + J.p11)), (2*J.ep*(2*J.p1*J.p2 + J.p12)), 0, 0], ![(2*J.ep*(2*J.p1*J.p2 + J.p12)), (2*J.ep*(2*J.p2^(2:ℕ) + J.p22)), 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![(J.ep*(4*J.p1^(2:ℕ)*J.w0 + 4*J.p1*J.w1 + 2*J.p11*J.w0 + J.w11)), (J.ep*(4*J.p1*J.p2*J.w0 + 2*J.p1*J.w2 + 2*J.p12*J.w0 + 2*J.p2*J.w1 + J.w12)), 0, 0], ![(J.ep*(4*J.p1*J.p2*J.w0 + 2*J.p1*J.w2 + 2*J.p12*J.w0 + 2*J.p2*J.w1 + J.w12)), (J.ep*(4*J.p2^(2:ℕ)*J.w0 + 4*J.p2*J.w2 + 2*J.p22*J.w0 + J.w22)), 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]]], 
    ![![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![(J.ep*(4*J.p1^(2:ℕ)*J.w0 + 4*J.p1*J.w1 + 2*J.p11*J.w0 + J.w11)), (J.ep*(4*J.p1*J.p2*J.w0 + 2*J.p1*J.w2 + 2*J.p12*J.w0 + 2*J.p2*J.w1 + J.w12)), 0, 0], ![(J.ep*(4*J.p1*J.p2*J.w0 + 2*J.p1*J.w2 + 2*J.p12*J.w0 + 2*J.p2*J.w1 + J.w12)), (J.ep*(4*J.p2^(2:ℕ)*J.w0 + 4*J.p2*J.w2 + 2*J.p22*J.w0 + J.w22)), 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![((2*(2*J.ep^(2:ℕ)*J.p1^(2:ℕ)*J.w0^(2:ℕ) + 4*J.ep^(2:ℕ)*J.p1*J.w0*J.w1 + J.ep^(2:ℕ)*J.p11*J.w0^(2:ℕ) + J.ep^(2:ℕ)*J.w0*J.w11 + J.ep^(2:ℕ)*J.w1^(2:ℕ) + 2*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p1*J.r0*J.r1 - J.p11*J.r0^(2:ℕ) + J.r0*J.r11 + J.r1^(2:ℕ))) / ((J.ep))), ((2*(2*J.ep^(2:ℕ)*J.p1*J.p2*J.w0^(2:ℕ) + 2*J.ep^(2:ℕ)*J.p1*J.w0*J.w2 + J.ep^(2:ℕ)*J.p12*J.w0^(2:ℕ) + 2*J.ep^(2:ℕ)*J.p2*J.w0*J.w1 + J.ep^(2:ℕ)*J.w0*J.w12 + J.ep^(2:ℕ)*J.w1*J.w2 + 2*J.p1*J.p2*J.r0^(2:ℕ) - 2*J.p1*J.r0*J.r2 - J.p12*J.r0^(2:ℕ) - 2*J.p2*J.r0*J.r1 + J.r0*J.r12 + J.r1*J.r2)) / ((J.ep))), 0, 0], ![((2*(2*J.ep^(2:ℕ)*J.p1*J.p2*J.w0^(2:ℕ) + 2*J.ep^(2:ℕ)*J.p1*J.w0*J.w2 + J.ep^(2:ℕ)*J.p12*J.w0^(2:ℕ) + 2*J.ep^(2:ℕ)*J.p2*J.w0*J.w1 + J.ep^(2:ℕ)*J.w0*J.w12 + J.ep^(2:ℕ)*J.w1*J.w2 + 2*J.p1*J.p2*J.r0^(2:ℕ) - 2*J.p1*J.r0*J.r2 - J.p12*J.r0^(2:ℕ) - 2*J.p2*J.r0*J.r1 + J.r0*J.r12 + J.r1*J.r2)) / ((J.ep))), ((2*(2*J.ep^(2:ℕ)*J.p2^(2:ℕ)*J.w0^(2:ℕ) + 4*J.ep^(2:ℕ)*J.p2*J.w0*J.w2 + J.ep^(2:ℕ)*J.p22*J.w0^(2:ℕ) + J.ep^(2:ℕ)*J.w0*J.w22 + J.ep^(2:ℕ)*J.w2^(2:ℕ) + 2*J.p2^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p2*J.r0*J.r2 - J.p22*J.r0^(2:ℕ) + J.r0*J.r22 + J.r2^(2:ℕ))) / ((J.ep))), 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]]]]

noncomputable def WGamT (J : GJ) : Fin 4 → Fin 4 → Fin 4 → ℝ :=
  ![![![(J.a1), (J.a2), 0, 0], ![(J.a2), (J.a1), 0, 0], ![0, 0, ((-(J.ep^(2:ℕ)*J.w0*J.w1 - 2*J.p1*J.r0^(2:ℕ))/2) / ((J.r0)^(2:ℕ))), ((J.ep^(2:ℕ)*J.w1/2) / ((J.r0)^(2:ℕ)))], ![0, 0, ((-(J.ep^(2:ℕ)*J.w0^(2:ℕ)*J.w1 - 4*J.p1*J.r0^(2:ℕ)*J.w0 - J.r0^(2:ℕ)*J.w1 + 2*J.r0*J.r1*J.w0)/2) / ((J.r0)^(2:ℕ))), (((J.ep^(2:ℕ)*J.w0*J.w1 - 2*J.p1*J.r0^(2:ℕ) + 2*J.r0*J.r1)/2) / ((J.r0)^(2:ℕ)))]], 
    ![![(J.a2), (J.a1), 0, 0], ![(J.a1), (J.a2), 0, 0], ![0, 0, ((-(J.ep^(2:ℕ)*J.w0*J.w2 - 2*J.p2*J.r0^(2:ℕ))/2) / ((J.r0)^(2:ℕ))), ((J.ep^(2:ℕ)*J.w2/2) / ((J.r0)^(2:ℕ)))], ![0, 0, ((-(J.ep^(2:ℕ)*J.w0^(2:ℕ)*J.w2 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - J.r0^(2:ℕ)*J.w2 + 2*J.r0*J.r2*J.w0)/2) / ((J.r0)^(2:ℕ))), (((J.ep^(2:ℕ)*J.w0*J.w2 - 2*J.p2*J.r0^(2:ℕ) + 2*J.r0*J.r2)/2) / ((J.r0)^(2:ℕ)))]], 
    ![![0, 0, ((-(J.ep^(2:ℕ)*J.w0*J.w1 - 2*J.p1*J.r0^(2:ℕ))/2) / ((J.r0)^(2:ℕ))), ((J.ep^(2:ℕ)*J.w1/2) / ((J.r0)^(2:ℕ)))], ![0, 0, ((-(J.ep^(2:ℕ)*J.w0*J.w2 - 2*J.p2*J.r0^(2:ℕ))/2) / ((J.r0)^(2:ℕ))), ((J.ep^(2:ℕ)*J.w2/2) / ((J.r0)^(2:ℕ)))], ![((J.ep*J.p1) / ((J.ea))), ((-J.ep*J.p2) / ((J.ea))), 0, 0], ![((J.ep*(2*J.p1*J.w0 + J.w1)/2) / ((J.ea))), ((-J.ep*(2*J.p2*J.w0 + J.w2)/2) / ((J.ea))), 0, 0]], 
    ![![0, 0, ((-(J.ep^(2:ℕ)*J.w0^(2:ℕ)*J.w1 - 4*J.p1*J.r0^(2:ℕ)*J.w0 - J.r0^(2:ℕ)*J.w1 + 2*J.r0*J.r1*J.w0)/2) / ((J.r0)^(2:ℕ))), (((J.ep^(2:ℕ)*J.w0*J.w1 - 2*J.p1*J.r0^(2:ℕ) + 2*J.r0*J.r1)/2) / ((J.r0)^(2:ℕ)))], ![0, 0, ((-(J.ep^(2:ℕ)*J.w0^(2:ℕ)*J.w2 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - J.r0^(2:ℕ)*J.w2 + 2*J.r0*J.r2*J.w0)/2) / ((J.r0)^(2:ℕ))), (((J.ep^(2:ℕ)*J.w0*J.w2 - 2*J.p2*J.r0^(2:ℕ) + 2*J.r0*J.r2)/2) / ((J.r0)^(2:ℕ)))], ![((J.ep*(2*J.p1*J.w0 + J.w1)/2) / ((J.ea))), ((-J.ep*(2*J.p2*J.w0 + J.w2)/2) / ((J.ea))), 0, 0], ![((J.ep^(2:ℕ)*J.p1*J.w0^(2:ℕ) + J.ep^(2:ℕ)*J.w0*J.w1 - J.p1*J.r0^(2:ℕ) + J.r0*J.r1) / ((J.ea) * (J.ep))), ((-J.ep^(2:ℕ)*J.p2*J.w0^(2:ℕ) - J.ep^(2:ℕ)*J.w0*J.w2 + J.p2*J.r0^(2:ℕ) - J.r0*J.r2) / ((J.ea) * (J.ep))), 0, 0]]]

noncomputable def WDGT (J : GJ) : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ :=
  ![![![![(J.a11), (J.a12), 0, 0], ![(J.a12), (J.a11), 0, 0], ![0, 0, ((-(4*J.ep^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 + J.ep^(2:ℕ)*J.r0*J.w0*J.w11 + J.ep^(2:ℕ)*J.r0*J.w1^(2:ℕ) - 2*J.ep^(2:ℕ)*J.r1*J.w0*J.w1 - 2*J.p11*J.r0^(3:ℕ))/2) / ((J.r0)^(3:ℕ))), ((J.ep^(2:ℕ)*(4*J.p1*J.r0*J.w1 + J.r0*J.w11 - 2*J.r1*J.w1)/2) / ((J.r0)^(3:ℕ)))], ![0, 0, ((-(4*J.ep^(2:ℕ)*J.p1*J.r0*J.w0^(2:ℕ)*J.w1 + J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w11 + 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1^(2:ℕ) - 2*J.ep^(2:ℕ)*J.r1*J.w0^(2:ℕ)*J.w1 - 4*J.p1*J.r0^(3:ℕ)*J.w1 - 4*J.p11*J.r0^(3:ℕ)*J.w0 - J.r0^(3:ℕ)*J.w11 + 2*J.r0^(2:ℕ)*J.r1*J.w1 + 2*J.r0^(2:ℕ)*J.r11*J.w0 - 2*J.r0*J.r1^(2:ℕ)*J.w0)/2) / ((J.r0)^(3:ℕ))), (((4*J.ep^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 + J.ep^(2:ℕ)*J.r0*J.w0*J.w11 + J.ep^(2:ℕ)*J.r0*J.w1^(2:ℕ) - 2*J.ep^(2:ℕ)*J.r1*J.w0*J.w1 - 2*J.p11*J.r0^(3:ℕ) + 2*J.r0^(2:ℕ)*J.r11 - 2*J.r0*J.r1^(2:ℕ))/2) / ((J.r0)^(3:ℕ)))]], ![![(J.a12), (J.a11), 0, 0], ![(J.a11), (J.a12), 0, 0], ![0, 0, ((-(4*J.ep^(2:ℕ)*J.p1*J.r0*J.w0*J.w2 + J.ep^(2:ℕ)*J.r0*J.w0*J.w12 + J.ep^(2:ℕ)*J.r0*J.w1*J.w2 - 2*J.ep^(2:ℕ)*J.r1*J.w0*J.w2 - 2*J.p12*J.r0^(3:ℕ))/2) / ((J.r0)^(3:ℕ))), ((J.ep^(2:ℕ)*(4*J.p1*J.r0*J.w2 + J.r0*J.w12 - 2*J.r1*J.w2)/2) / ((J.r0)^(3:ℕ)))], ![0, 0, ((-(4*J.ep^(2:ℕ)*J.p1*J.r0*J.w0^(2:ℕ)*J.w2 + J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w12 + 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1*J.w2 - 2*J.ep^(2:ℕ)*J.r1*J.w0^(2:ℕ)*J.w2 - 4*J.p12*J.r0^(3:ℕ)*J.w0 - 4*J.p2*J.r0^(3:ℕ)*J.w1 - J.r0^(3:ℕ)*J.w12 + 2*J.r0^(2:ℕ)*J.r12*J.w0 + 2*J.r0^(2:ℕ)*J.r2*J.w1 - 2*J.r0*J.r1*J.r2*J.w0)/2) / ((J.r0)^(3:ℕ))), (((4*J.ep^(2:ℕ)*J.p1*J.r0*J.w0*J.w2 + J.ep^(2:ℕ)*J.r0*J.w0*J.w12 + J.ep^(2:ℕ)*J.r0*J.w1*J.w2 - 2*J.ep^(2:ℕ)*J.r1*J.w0*J.w2 - 2*J.p12*J.r0^(3:ℕ) + 2*J.r0^(2:ℕ)*J.r12 - 2*J.r0*J.r1*J.r2)/2) / ((J.r0)^(3:ℕ)))]], ![![0, 0, ((-(4*J.ep^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 + J.ep^(2:ℕ)*J.r0*J.w0*J.w11 + J.ep^(2:ℕ)*J.r0*J.w1^(2:ℕ) - 2*J.ep^(2:ℕ)*J.r1*J.w0*J.w1 - 2*J.p11*J.r0^(3:ℕ))/2) / ((J.r0)^(3:ℕ))), ((J.ep^(2:ℕ)*(4*J.p1*J.r0*J.w1 + J.r0*J.w11 - 2*J.r1*J.w1)/2) / ((J.r0)^(3:ℕ)))], ![0, 0, ((-(4*J.ep^(2:ℕ)*J.p1*J.r0*J.w0*J.w2 + J.ep^(2:ℕ)*J.r0*J.w0*J.w12 + J.ep^(2:ℕ)*J.r0*J.w1*J.w2 - 2*J.ep^(2:ℕ)*J.r1*J.w0*J.w2 - 2*J.p12*J.r0^(3:ℕ))/2) / ((J.r0)^(3:ℕ))), ((J.ep^(2:ℕ)*(4*J.p1*J.r0*J.w2 + J.r0*J.w12 - 2*J.r1*J.w2)/2) / ((J.r0)^(3:ℕ)))], ![((-J.ep*(2*J.a1*J.p1 - 2*J.p1^(2:ℕ) - J.p11)) / ((J.ea))), ((J.ep*(2*J.a1*J.p2 - 2*J.p1*J.p2 - J.p12)) / ((J.ea))), 0, 0], ![((-J.ep*(4*J.a1*J.p1*J.w0 + 2*J.a1*J.w1 - 4*J.p1^(2:ℕ)*J.w0 - 4*J.p1*J.w1 - 2*J.p11*J.w0 - J.w11)/2) / ((J.ea))), ((J.ep*(4*J.a1*J.p2*J.w0 + 2*J.a1*J.w2 - 4*J.p1*J.p2*J.w0 - 2*J.p1*J.w2 - 2*J.p12*J.w0 - 2*J.p2*J.w1 - J.w12)/2) / ((J.ea))), 0, 0]], ![![0, 0, ((-(4*J.ep^(2:ℕ)*J.p1*J.r0*J.w0^(2:ℕ)*J.w1 + J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w11 + 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1^(2:ℕ) - 2*J.ep^(2:ℕ)*J.r1*J.w0^(2:ℕ)*J.w1 - 4*J.p1*J.r0^(3:ℕ)*J.w1 - 4*J.p11*J.r0^(3:ℕ)*J.w0 - J.r0^(3:ℕ)*J.w11 + 2*J.r0^(2:ℕ)*J.r1*J.w1 + 2*J.r0^(2:ℕ)*J.r11*J.w0 - 2*J.r0*J.r1^(2:ℕ)*J.w0)/2) / ((J.r0)^(3:ℕ))), (((4*J.ep^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 + J.ep^(2:ℕ)*J.r0*J.w0*J.w11 + J.ep^(2:ℕ)*J.r0*J.w1^(2:ℕ) - 2*J.ep^(2:ℕ)*J.r1*J.w0*J.w1 - 2*J.p11*J.r0^(3:ℕ) + 2*J.r0^(2:ℕ)*J.r11 - 2*J.r0*J.r1^(2:ℕ))/2) / ((J.r0)^(3:ℕ)))], ![0, 0, ((-(4*J.ep^(2:ℕ)*J.p1*J.r0*J.w0^(2:ℕ)*J.w2 + J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w12 + 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1*J.w2 - 2*J.ep^(2:ℕ)*J.r1*J.w0^(2:ℕ)*J.w2 - 4*J.p12*J.r0^(3:ℕ)*J.w0 - 4*J.p2*J.r0^(3:ℕ)*J.w1 - J.r0^(3:ℕ)*J.w12 + 2*J.r0^(2:ℕ)*J.r12*J.w0 + 2*J.r0^(2:ℕ)*J.r2*J.w1 - 2*J.r0*J.r1*J.r2*J.w0)/2) / ((J.r0)^(3:ℕ))), (((4*J.ep^(2:ℕ)*J.p1*J.r0*J.w0*J.w2 + J.ep^(2:ℕ)*J.r0*J.w0*J.w12 + J.ep^(2:ℕ)*J.r0*J.w1*J.w2 - 2*J.ep^(2:ℕ)*J.r1*J.w0*J.w2 - 2*J.p12*J.r0^(3:ℕ) + 2*J.r0^(2:ℕ)*J.r12 - 2*J.r0*J.r1*J.r2)/2) / ((J.r0)^(3:ℕ)))], ![((-J.ep*(4*J.a1*J.p1*J.w0 + 2*J.a1*J.w1 - 4*J.p1^(2:ℕ)*J.w0 - 4*J.p1*J.w1 - 2*J.p11*J.w0 - J.w11)/2) / ((J.ea))), ((J.ep*(4*J.a1*J.p2*J.w0 + 2*J.a1*J.w2 - 4*J.p1*J.p2*J.w0 - 2*J.p1*J.w2 - 2*J.p12*J.w0 - 2*J.p2*J.w1 - J.w12)/2) / ((J.ea))), 0, 0], ![((-2*J.a1*J.ep^(2:ℕ)*J.p1*J.w0^(2:ℕ) - 2*J.a1*J.ep^(2:ℕ)*J.w0*J.w1 + 2*J.a1*J.p1*J.r0^(2:ℕ) - 2*J.a1*J.r0*J.r1 + 2*J.ep^(2:ℕ)*J.p1^(2:ℕ)*J.w0^(2:ℕ) + 4*J.ep^(2:ℕ)*J.p1*J.w0*J.w1 + J.ep^(2:ℕ)*J.p11*J.w0^(2:ℕ) + J.ep^(2:ℕ)*J.w0*J.w11 + J.ep^(2:ℕ)*J.w1^(2:ℕ) + 2*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p1*J.r0*J.r1 - J.p11*J.r0^(2:ℕ) + J.r0*J.r11 + J.r1^(2:ℕ)) / ((J.ea) * (J.ep))), ((2*J.a1*J.ep^(2:ℕ)*J.p2*J.w0^(2:ℕ) + 2*J.a1*J.ep^(2:ℕ)*J.w0*J.w2 - 2*J.a1*J.p2*J.r0^(2:ℕ) + 2*J.a1*J.r0*J.r2 - 2*J.ep^(2:ℕ)*J.p1*J.p2*J.w0^(2:ℕ) - 2*J.ep^(2:ℕ)*J.p1*J.w0*J.w2 - J.ep^(2:ℕ)*J.p12*J.w0^(2:ℕ) - 2*J.ep^(2:ℕ)*J.p2*J.w0*J.w1 - J.ep^(2:ℕ)*J.w0*J.w12 - J.ep^(2:ℕ)*J.w1*J.w2 - 2*J.p1*J.p2*J.r0^(2:ℕ) + 2*J.p1*J.r0*J.r2 + J.p12*J.r0^(2:ℕ) + 2*J.p2*J.r0*J.r1 - J.r0*J.r12 - J.r1*J.r2) / ((J.ea) * (J.ep))), 0, 0]]], 
    ![![![(J.a12), (J.a22), 0, 0], ![(J.a22), (J.a12), 0, 0], ![0, 0, ((-(4*J.ep^(2:ℕ)*J.p2*J.r0*J.w0*J.w1 + J.ep^(2:ℕ)*J.r0*J.w0*J.w12 + J.ep^(2:ℕ)*J.r0*J.w1*J.w2 - 2*J.ep^(2:ℕ)*J.r2*J.w0*J.w1 - 2*J.p12*J.r0^(3:ℕ))/2) / ((J.r0)^(3:ℕ))), ((J.ep^(2:ℕ)*(4*J.p2*J.r0*J.w1 + J.r0*J.w12 - 2*J.r2*J.w1)/2) / ((J.r0)^(3:ℕ)))], ![0, 0, ((-(4*J.ep^(2:ℕ)*J.p2*J.r0*J.w0^(2:ℕ)*J.w1 + J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w12 + 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1*J.w2 - 2*J.ep^(2:ℕ)*J.r2*J.w0^(2:ℕ)*J.w1 - 4*J.p1*J.r0^(3:ℕ)*J.w2 - 4*J.p12*J.r0^(3:ℕ)*J.w0 - J.r0^(3:ℕ)*J.w12 + 2*J.r0^(2:ℕ)*J.r1*J.w2 + 2*J.r0^(2:ℕ)*J.r12*J.w0 - 2*J.r0*J.r1*J.r2*J.w0)/2) / ((J.r0)^(3:ℕ))), (((4*J.ep^(2:ℕ)*J.p2*J.r0*J.w0*J.w1 + J.ep^(2:ℕ)*J.r0*J.w0*J.w12 + J.ep^(2:ℕ)*J.r0*J.w1*J.w2 - 2*J.ep^(2:ℕ)*J.r2*J.w0*J.w1 - 2*J.p12*J.r0^(3:ℕ) + 2*J.r0^(2:ℕ)*J.r12 - 2*J.r0*J.r1*J.r2)/2) / ((J.r0)^(3:ℕ)))]], ![![(J.a22), (J.a12), 0, 0], ![(J.a12), (J.a22), 0, 0], ![0, 0, ((-(4*J.ep^(2:ℕ)*J.p2*J.r0*J.w0*J.w2 + J.ep^(2:ℕ)*J.r0*J.w0*J.w22 + J.ep^(2:ℕ)*J.r0*J.w2^(2:ℕ) - 2*J.ep^(2:ℕ)*J.r2*J.w0*J.w2 - 2*J.p22*J.r0^(3:ℕ))/2) / ((J.r0)^(3:ℕ))), ((J.ep^(2:ℕ)*(4*J.p2*J.r0*J.w2 + J.r0*J.w22 - 2*J.r2*J.w2)/2) / ((J.r0)^(3:ℕ)))], ![0, 0, ((-(4*J.ep^(2:ℕ)*J.p2*J.r0*J.w0^(2:ℕ)*J.w2 + J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w22 + 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w2^(2:ℕ) - 2*J.ep^(2:ℕ)*J.r2*J.w0^(2:ℕ)*J.w2 - 4*J.p2*J.r0^(3:ℕ)*J.w2 - 4*J.p22*J.r0^(3:ℕ)*J.w0 - J.r0^(3:ℕ)*J.w22 + 2*J.r0^(2:ℕ)*J.r2*J.w2 + 2*J.r0^(2:ℕ)*J.r22*J.w0 - 2*J.r0*J.r2^(2:ℕ)*J.w0)/2) / ((J.r0)^(3:ℕ))), (((4*J.ep^(2:ℕ)*J.p2*J.r0*J.w0*J.w2 + J.ep^(2:ℕ)*J.r0*J.w0*J.w22 + J.ep^(2:ℕ)*J.r0*J.w2^(2:ℕ) - 2*J.ep^(2:ℕ)*J.r2*J.w0*J.w2 - 2*J.p22*J.r0^(3:ℕ) + 2*J.r0^(2:ℕ)*J.r22 - 2*J.r0*J.r2^(2:ℕ))/2) / ((J.r0)^(3:ℕ)))]], ![![0, 0, ((-(4*J.ep^(2:ℕ)*J.p2*J.r0*J.w0*J.w1 + J.ep^(2:ℕ)*J.r0*J.w0*J.w12 + J.ep^(2:ℕ)*J.r0*J.w1*J.w2 - 2*J.ep^(2:ℕ)*J.r2*J.w0*J.w1 - 2*J.p12*J.r0^(3:ℕ))/2) / ((J.r0)^(3:ℕ))), ((J.ep^(2:ℕ)*(4*J.p2*J.r0*J.w1 + J.r0*J.w12 - 2*J.r2*J.w1)/2) / ((J.r0)^(3:ℕ)))], ![0, 0, ((-(4*J.ep^(2:ℕ)*J.p2*J.r0*J.w0*J.w2 + J.ep^(2:ℕ)*J.r0*J.w0*J.w22 + J.ep^(2:ℕ)*J.r0*J.w2^(2:ℕ) - 2*J.ep^(2:ℕ)*J.r2*J.w0*J.w2 - 2*J.p22*J.r0^(3:ℕ))/2) / ((J.r0)^(3:ℕ))), ((J.ep^(2:ℕ)*(4*J.p2*J.r0*J.w2 + J.r0*J.w22 - 2*J.r2*J.w2)/2) / ((J.r0)^(3:ℕ)))], ![((-J.ep*(2*J.a2*J.p1 - 2*J.p1*J.p2 - J.p12)) / ((J.ea))), ((J.ep*(2*J.a2*J.p2 - 2*J.p2^(2:ℕ) - J.p22)) / ((J.ea))), 0, 0], ![((-J.ep*(4*J.a2*J.p1*J.w0 + 2*J.a2*J.w1 - 4*J.p1*J.p2*J.w0 - 2*J.p1*J.w2 - 2*J.p12*J.w0 - 2*J.p2*J.w1 - J.w12)/2) / ((J.ea))), ((J.ep*(4*J.a2*J.p2*J.w0 + 2*J.a2*J.w2 - 4*J.p2^(2:ℕ)*J.w0 - 4*J.p2*J.w2 - 2*J.p22*J.w0 - J.w22)/2) / ((J.ea))), 0, 0]], ![![0, 0, ((-(4*J.ep^(2:ℕ)*J.p2*J.r0*J.w0^(2:ℕ)*J.w1 + J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w12 + 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1*J.w2 - 2*J.ep^(2:ℕ)*J.r2*J.w0^(2:ℕ)*J.w1 - 4*J.p1*J.r0^(3:ℕ)*J.w2 - 4*J.p12*J.r0^(3:ℕ)*J.w0 - J.r0^(3:ℕ)*J.w12 + 2*J.r0^(2:ℕ)*J.r1*J.w2 + 2*J.r0^(2:ℕ)*J.r12*J.w0 - 2*J.r0*J.r1*J.r2*J.w0)/2) / ((J.r0)^(3:ℕ))), (((4*J.ep^(2:ℕ)*J.p2*J.r0*J.w0*J.w1 + J.ep^(2:ℕ)*J.r0*J.w0*J.w12 + J.ep^(2:ℕ)*J.r0*J.w1*J.w2 - 2*J.ep^(2:ℕ)*J.r2*J.w0*J.w1 - 2*J.p12*J.r0^(3:ℕ) + 2*J.r0^(2:ℕ)*J.r12 - 2*J.r0*J.r1*J.r2)/2) / ((J.r0)^(3:ℕ)))], ![0, 0, ((-(4*J.ep^(2:ℕ)*J.p2*J.r0*J.w0^(2:ℕ)*J.w2 + J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w22 + 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w2^(2:ℕ) - 2*J.ep^(2:ℕ)*J.r2*J.w0^(2:ℕ)*J.w2 - 4*J.p2*J.r0^(3:ℕ)*J.w2 - 4*J.p22*J.r0^(3:ℕ)*J.w0 - J.r0^(3:ℕ)*J.w22 + 2*J.r0^(2:ℕ)*J.r2*J.w2 + 2*J.r0^(2:ℕ)*J.r22*J.w0 - 2*J.r0*J.r2^(2:ℕ)*J.w0)/2) / ((J.r0)^(3:ℕ))), (((4*J.ep^(2:ℕ)*J.p2*J.r0*J.w0*J.w2 + J.ep^(2:ℕ)*J.r0*J.w0*J.w22 + J.ep^(2:ℕ)*J.r0*J.w2^(2:ℕ) - 2*J.ep^(2:ℕ)*J.r2*J.w0*J.w2 - 2*J.p22*J.r0^(3:ℕ) + 2*J.r0^(2:ℕ)*J.r22 - 2*J.r0*J.r2^(2:ℕ))/2) / ((J.r0)^(3:ℕ)))], ![((-J.ep*(4*J.a2*J.p1*J.w0 + 2*J.a2*J.w1 - 4*J.p1*J.p2*J.w0 - 2*J.p1*J.w2 - 2*J.p12*J.w0 - 2*J.p2*J.w1 - J.w12)/2) / ((J.ea))), ((J.ep*(4*J.a2*J.p2*J.w0 + 2*J.a2*J.w2 - 4*J.p2^(2:ℕ)*J.w0 - 4*J.p2*J.w2 - 2*J.p22*J.w0 - J.w22)/2) / ((J.ea))), 0, 0], ![((-2*J.a2*J.ep^(2:ℕ)*J.p1*J.w0^(2:ℕ) - 2*J.a2*J.ep^(2:ℕ)*J.w0*J.w1 + 2*J.a2*J.p1*J.r0^(2:ℕ) - 2*J.a2*J.r0*J.r1 + 2*J.ep^(2:ℕ)*J.p1*J.p2*J.w0^(2:ℕ) + 2*J.ep^(2:ℕ)*J.p1*J.w0*J.w2 + J.ep^(2:ℕ)*J.p12*J.w0^(2:ℕ) + 2*J.ep^(2:ℕ)*J.p2*J.w0*J.w1 + J.ep^(2:ℕ)*J.w0*J.w12 + J.ep^(2:ℕ)*J.w1*J.w2 + 2*J.p1*J.p2*J.r0^(2:ℕ) - 2*J.p1*J.r0*J.r2 - J.p12*J.r0^(2:ℕ) - 2*J.p2*J.r0*J.r1 + J.r0*J.r12 + J.r1*J.r2) / ((J.ea) * (J.ep))), ((2*J.a2*J.ep^(2:ℕ)*J.p2*J.w0^(2:ℕ) + 2*J.a2*J.ep^(2:ℕ)*J.w0*J.w2 - 2*J.a2*J.p2*J.r0^(2:ℕ) + 2*J.a2*J.r0*J.r2 - 2*J.ep^(2:ℕ)*J.p2^(2:ℕ)*J.w0^(2:ℕ) - 4*J.ep^(2:ℕ)*J.p2*J.w0*J.w2 - J.ep^(2:ℕ)*J.p22*J.w0^(2:ℕ) - J.ep^(2:ℕ)*J.w0*J.w22 - J.ep^(2:ℕ)*J.w2^(2:ℕ) - 2*J.p2^(2:ℕ)*J.r0^(2:ℕ) + 4*J.p2*J.r0*J.r2 + J.p22*J.r0^(2:ℕ) - J.r0*J.r22 - J.r2^(2:ℕ)) / ((J.ea) * (J.ep))), 0, 0]]], 
    ![![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]]], 
    ![![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]]]]

noncomputable def WRT (J : GJ) : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ :=
  ![![![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, (J.a11 - J.a22), 0, 0], ![(J.a11 - J.a22), 0, 0, 0], ![0, 0, ((-J.ep^(2:ℕ)*J.w0*(2*J.p1*J.r0*J.w2 - 2*J.p2*J.r0*J.w1 - J.r1*J.w2 + J.r2*J.w1)/2) / ((J.r0)^(3:ℕ))), ((J.ep^(2:ℕ)*(2*J.p1*J.r0*J.w2 - 2*J.p2*J.r0*J.w1 - J.r1*J.w2 + J.r2*J.w1)/2) / ((J.r0)^(3:ℕ)))], ![0, 0, ((-(J.ep^(2:ℕ)*J.w0^(2:ℕ) + J.r0^(2:ℕ))*(2*J.p1*J.r0*J.w2 - 2*J.p2*J.r0*J.w1 - J.r1*J.w2 + J.r2*J.w1)/2) / ((J.r0)^(3:ℕ))), ((J.ep^(2:ℕ)*J.w0*(2*J.p1*J.r0*J.w2 - 2*J.p2*J.r0*J.w1 - J.r1*J.w2 + J.r2*J.w1)/2) / ((J.r0)^(3:ℕ)))]], ![![0, 0, (((2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a1*J.p1*J.r0^(3:ℕ) + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a2*J.p2*J.r0^(3:ℕ) - 8*J.ep^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w11 - J.ep^(2:ℕ)*J.r0*J.w1^(2:ℕ) + 2*J.ep^(2:ℕ)*J.r1*J.w0*J.w1 + 4*J.p1^(2:ℕ)*J.r0^(3:ℕ) + 4*J.p11*J.r0^(3:ℕ))/4) / ((J.r0)^(3:ℕ))), ((-J.ep^(2:ℕ)*(J.a1*J.r0*J.w1 + J.a2*J.r0*J.w2 - 4*J.p1*J.r0*J.w1 - J.r0*J.w11 + J.r1*J.w1)/2) / ((J.r0)^(3:ℕ)))], ![0, 0, (((2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a1*J.p2*J.r0^(3:ℕ) + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a2*J.p1*J.r0^(3:ℕ) - 6*J.ep^(2:ℕ)*J.p1*J.r0*J.w0*J.w2 - 2*J.ep^(2:ℕ)*J.p2*J.r0*J.w0*J.w1 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w12 - J.ep^(2:ℕ)*J.r0*J.w1*J.w2 + 2*J.ep^(2:ℕ)*J.r1*J.w0*J.w2 + 4*J.p1*J.p2*J.r0^(3:ℕ) + 4*J.p12*J.r0^(3:ℕ))/4) / ((J.r0)^(3:ℕ))), ((-J.ep^(2:ℕ)*(J.a1*J.r0*J.w2 + J.a2*J.r0*J.w1 - 3*J.p1*J.r0*J.w2 - J.p2*J.r0*J.w1 - J.r0*J.w12 + J.r1*J.w2)/2) / ((J.r0)^(3:ℕ)))], ![((-J.ep*(4*J.a1*J.p1*J.r0^(2:ℕ) + 4*J.a2*J.p2*J.r0^(2:ℕ) + J.ep^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p11*J.r0^(2:ℕ))/4) / ((J.ea) * (J.r0)^(2:ℕ))), ((J.ep*(4*J.a1*J.p2*J.r0^(2:ℕ) + 4*J.a2*J.p1*J.r0^(2:ℕ) + J.ep^(2:ℕ)*J.w1*J.w2 - 4*J.p1*J.p2*J.r0^(2:ℕ) - 4*J.p12*J.r0^(2:ℕ))/4) / ((J.ea) * (J.r0)^(2:ℕ))), 0, 0], ![((-J.ep*(4*J.a1*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w1 + 4*J.a2*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w2 + J.ep^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p11*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w11 + 2*J.r0*J.r1*J.w1)/4) / ((J.ea) * (J.r0)^(2:ℕ))), ((J.ep*(4*J.a1*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w2 + 4*J.a2*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w1 + J.ep^(2:ℕ)*J.w0*J.w1*J.w2 - 4*J.p1*J.p2*J.r0^(2:ℕ)*J.w0 - 6*J.p1*J.r0^(2:ℕ)*J.w2 - 4*J.p12*J.r0^(2:ℕ)*J.w0 - 2*J.p2*J.r0^(2:ℕ)*J.w1 - 2*J.r0^(2:ℕ)*J.w12 + 2*J.r0*J.r1*J.w2)/4) / ((J.ea) * (J.r0)^(2:ℕ))), 0, 0]], ![![0, 0, (((J.a1*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w1 - 4*J.a1*J.p1*J.r0^(3:ℕ)*J.w0 - J.a1*J.r0^(3:ℕ)*J.w1 + 2*J.a1*J.r0^(2:ℕ)*J.r1*J.w0 + J.a2*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w2 - 4*J.a2*J.p2*J.r0^(3:ℕ)*J.w0 - J.a2*J.r0^(3:ℕ)*J.w2 + 2*J.a2*J.r0^(2:ℕ)*J.r2*J.w0 - 4*J.ep^(2:ℕ)*J.p1*J.r0*J.w0^(2:ℕ)*J.w1 - J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w11 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1^(2:ℕ) + J.ep^(2:ℕ)*J.r1*J.w0^(2:ℕ)*J.w1 + 4*J.p1*J.r0^(3:ℕ)*J.w1 + 4*J.p1*J.r0^(2:ℕ)*J.r1*J.w0 + 4*J.p11*J.r0^(3:ℕ)*J.w0 + J.r0^(3:ℕ)*J.w11 - J.r0^(2:ℕ)*J.r1*J.w1 - 2*J.r0^(2:ℕ)*J.r11*J.w0)/2) / ((J.r0)^(3:ℕ))), ((-(2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a1*J.p1*J.r0^(3:ℕ) + 4*J.a1*J.r0^(2:ℕ)*J.r1 + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a2*J.p2*J.r0^(3:ℕ) + 4*J.a2*J.r0^(2:ℕ)*J.r2 - 8*J.ep^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w11 - 3*J.ep^(2:ℕ)*J.r0*J.w1^(2:ℕ) + 2*J.ep^(2:ℕ)*J.r1*J.w0*J.w1 - 4*J.p1^(2:ℕ)*J.r0^(3:ℕ) + 8*J.p1*J.r0^(2:ℕ)*J.r1 + 4*J.p11*J.r0^(3:ℕ) - 4*J.r0^(2:ℕ)*J.r11)/4) / ((J.r0)^(3:ℕ)))], ![0, 0, (((J.a1*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w2 - 4*J.a1*J.p2*J.r0^(3:ℕ)*J.w0 - J.a1*J.r0^(3:ℕ)*J.w2 + 2*J.a1*J.r0^(2:ℕ)*J.r2*J.w0 + J.a2*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w1 - 4*J.a2*J.p1*J.r0^(3:ℕ)*J.w0 - J.a2*J.r0^(3:ℕ)*J.w1 + 2*J.a2*J.r0^(2:ℕ)*J.r1*J.w0 - 3*J.ep^(2:ℕ)*J.p1*J.r0*J.w0^(2:ℕ)*J.w2 - J.ep^(2:ℕ)*J.p2*J.r0*J.w0^(2:ℕ)*J.w1 - J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w12 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1*J.w2 + J.ep^(2:ℕ)*J.r1*J.w0^(2:ℕ)*J.w2 + J.p1*J.r0^(3:ℕ)*J.w2 + 2*J.p1*J.r0^(2:ℕ)*J.r2*J.w0 + 4*J.p12*J.r0^(3:ℕ)*J.w0 + 3*J.p2*J.r0^(3:ℕ)*J.w1 + 2*J.p2*J.r0^(2:ℕ)*J.r1*J.w0 + J.r0^(3:ℕ)*J.w12 - 2*J.r0^(2:ℕ)*J.r12*J.w0 - J.r0^(2:ℕ)*J.r2*J.w1)/2) / ((J.r0)^(3:ℕ))), ((-(2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a1*J.p2*J.r0^(3:ℕ) + 4*J.a1*J.r0^(2:ℕ)*J.r2 + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a2*J.p1*J.r0^(3:ℕ) + 4*J.a2*J.r0^(2:ℕ)*J.r1 - 6*J.ep^(2:ℕ)*J.p1*J.r0*J.w0*J.w2 - 2*J.ep^(2:ℕ)*J.p2*J.r0*J.w0*J.w1 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w12 - 3*J.ep^(2:ℕ)*J.r0*J.w1*J.w2 + 2*J.ep^(2:ℕ)*J.r1*J.w0*J.w2 - 4*J.p1*J.p2*J.r0^(3:ℕ) + 4*J.p1*J.r0^(2:ℕ)*J.r2 + 4*J.p12*J.r0^(3:ℕ) + 4*J.p2*J.r0^(2:ℕ)*J.r1 - 4*J.r0^(2:ℕ)*J.r12)/4) / ((J.r0)^(3:ℕ)))], ![((-J.ep*(4*J.a1*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w1 + 4*J.a2*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w2 + J.ep^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p11*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w11 + 2*J.r0*J.r1*J.w1)/4) / ((J.ea) * (J.r0)^(2:ℕ))), ((J.ep*(4*J.a1*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w2 + 4*J.a2*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w1 + J.ep^(2:ℕ)*J.w0*J.w1*J.w2 - 4*J.p1*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.p1*J.r0^(2:ℕ)*J.w2 - 4*J.p12*J.r0^(2:ℕ)*J.w0 - 6*J.p2*J.r0^(2:ℕ)*J.w1 - 2*J.r0^(2:ℕ)*J.w12 + 2*J.r0*J.r2*J.w1)/4) / ((J.ea) * (J.r0)^(2:ℕ))), 0, 0], ![((-(4*J.a1*J.ep^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a1*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.a1*J.p1*J.r0^(4:ℕ) + 4*J.a1*J.r0^(3:ℕ)*J.r1 + 4*J.a2*J.ep^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a2*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 4*J.a2*J.p2*J.r0^(4:ℕ) + 4*J.a2*J.r0^(3:ℕ)*J.r2 + J.ep^(4:ℕ)*J.w0^(2:ℕ)*J.w1^(2:ℕ) - 4*J.ep^(2:ℕ)*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 16*J.ep^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.ep^(2:ℕ)*J.p11*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 4*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w11 - 3*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w1^(2:ℕ) + 4*J.ep^(2:ℕ)*J.r0*J.r1*J.w0*J.w1 - 4*J.p1^(2:ℕ)*J.r0^(4:ℕ) + 8*J.p1*J.r0^(3:ℕ)*J.r1 + 4*J.p11*J.r0^(4:ℕ) - 4*J.r0^(3:ℕ)*J.r11)/4) / ((J.ea) * (J.ep) * (J.r0)^(2:ℕ))), (((4*J.a1*J.ep^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a1*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 4*J.a1*J.p2*J.r0^(4:ℕ) + 4*J.a1*J.r0^(3:ℕ)*J.r2 + 4*J.a2*J.ep^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a2*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.a2*J.p1*J.r0^(4:ℕ) + 4*J.a2*J.r0^(3:ℕ)*J.r1 + J.ep^(4:ℕ)*J.w0^(2:ℕ)*J.w1*J.w2 - 4*J.ep^(2:ℕ)*J.p1*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 8*J.ep^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0*J.w2 - 4*J.ep^(2:ℕ)*J.p12*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 8*J.ep^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w12 - 3*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w1*J.w2 + 2*J.ep^(2:ℕ)*J.r0*J.r1*J.w0*J.w2 + 2*J.ep^(2:ℕ)*J.r0*J.r2*J.w0*J.w1 - 4*J.p1*J.p2*J.r0^(4:ℕ) + 4*J.p1*J.r0^(3:ℕ)*J.r2 + 4*J.p12*J.r0^(4:ℕ) + 4*J.p2*J.r0^(3:ℕ)*J.r1 - 4*J.r0^(3:ℕ)*J.r12)/4) / ((J.ea) * (J.ep) * (J.r0)^(2:ℕ))), 0, 0]]], 
    ![![![0, (-J.a11 + J.a22), 0, 0], ![(-J.a11 + J.a22), 0, 0, 0], ![0, 0, ((J.ep^(2:ℕ)*J.w0*(2*J.p1*J.r0*J.w2 - 2*J.p2*J.r0*J.w1 - J.r1*J.w2 + J.r2*J.w1)/2) / ((J.r0)^(3:ℕ))), ((-J.ep^(2:ℕ)*(2*J.p1*J.r0*J.w2 - 2*J.p2*J.r0*J.w1 - J.r1*J.w2 + J.r2*J.w1)/2) / ((J.r0)^(3:ℕ)))], ![0, 0, (((J.ep^(2:ℕ)*J.w0^(2:ℕ) + J.r0^(2:ℕ))*(2*J.p1*J.r0*J.w2 - 2*J.p2*J.r0*J.w1 - J.r1*J.w2 + J.r2*J.w1)/2) / ((J.r0)^(3:ℕ))), ((-J.ep^(2:ℕ)*J.w0*(2*J.p1*J.r0*J.w2 - 2*J.p2*J.r0*J.w1 - J.r1*J.w2 + J.r2*J.w1)/2) / ((J.r0)^(3:ℕ)))]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, 0, (((2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a1*J.p2*J.r0^(3:ℕ) + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a2*J.p1*J.r0^(3:ℕ) - 2*J.ep^(2:ℕ)*J.p1*J.r0*J.w0*J.w2 - 6*J.ep^(2:ℕ)*J.p2*J.r0*J.w0*J.w1 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w12 - J.ep^(2:ℕ)*J.r0*J.w1*J.w2 + 2*J.ep^(2:ℕ)*J.r2*J.w0*J.w1 + 4*J.p1*J.p2*J.r0^(3:ℕ) + 4*J.p12*J.r0^(3:ℕ))/4) / ((J.r0)^(3:ℕ))), ((-J.ep^(2:ℕ)*(J.a1*J.r0*J.w2 + J.a2*J.r0*J.w1 - J.p1*J.r0*J.w2 - 3*J.p2*J.r0*J.w1 - J.r0*J.w12 + J.r2*J.w1)/2) / ((J.r0)^(3:ℕ)))], ![0, 0, (((2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a1*J.p1*J.r0^(3:ℕ) + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a2*J.p2*J.r0^(3:ℕ) - 8*J.ep^(2:ℕ)*J.p2*J.r0*J.w0*J.w2 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w22 - J.ep^(2:ℕ)*J.r0*J.w2^(2:ℕ) + 2*J.ep^(2:ℕ)*J.r2*J.w0*J.w2 + 4*J.p2^(2:ℕ)*J.r0^(3:ℕ) + 4*J.p22*J.r0^(3:ℕ))/4) / ((J.r0)^(3:ℕ))), ((-J.ep^(2:ℕ)*(J.a1*J.r0*J.w1 + J.a2*J.r0*J.w2 - 4*J.p2*J.r0*J.w2 - J.r0*J.w22 + J.r2*J.w2)/2) / ((J.r0)^(3:ℕ)))], ![((-J.ep*(4*J.a1*J.p2*J.r0^(2:ℕ) + 4*J.a2*J.p1*J.r0^(2:ℕ) + J.ep^(2:ℕ)*J.w1*J.w2 - 4*J.p1*J.p2*J.r0^(2:ℕ) - 4*J.p12*J.r0^(2:ℕ))/4) / ((J.ea) * (J.r0)^(2:ℕ))), ((J.ep*(4*J.a1*J.p1*J.r0^(2:ℕ) + 4*J.a2*J.p2*J.r0^(2:ℕ) + J.ep^(2:ℕ)*J.w2^(2:ℕ) - 4*J.p2^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p22*J.r0^(2:ℕ))/4) / ((J.ea) * (J.r0)^(2:ℕ))), 0, 0], ![((-J.ep*(4*J.a1*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w2 + 4*J.a2*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w1 + J.ep^(2:ℕ)*J.w0*J.w1*J.w2 - 4*J.p1*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.p1*J.r0^(2:ℕ)*J.w2 - 4*J.p12*J.r0^(2:ℕ)*J.w0 - 6*J.p2*J.r0^(2:ℕ)*J.w1 - 2*J.r0^(2:ℕ)*J.w12 + 2*J.r0*J.r2*J.w1)/4) / ((J.ea) * (J.r0)^(2:ℕ))), ((J.ep*(4*J.a1*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w1 + 4*J.a2*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w2 + J.ep^(2:ℕ)*J.w0*J.w2^(2:ℕ) - 4*J.p2^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p2*J.r0^(2:ℕ)*J.w2 - 4*J.p22*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w22 + 2*J.r0*J.r2*J.w2)/4) / ((J.ea) * (J.r0)^(2:ℕ))), 0, 0]], ![![0, 0, (((J.a1*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w2 - 4*J.a1*J.p2*J.r0^(3:ℕ)*J.w0 - J.a1*J.r0^(3:ℕ)*J.w2 + 2*J.a1*J.r0^(2:ℕ)*J.r2*J.w0 + J.a2*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w1 - 4*J.a2*J.p1*J.r0^(3:ℕ)*J.w0 - J.a2*J.r0^(3:ℕ)*J.w1 + 2*J.a2*J.r0^(2:ℕ)*J.r1*J.w0 - J.ep^(2:ℕ)*J.p1*J.r0*J.w0^(2:ℕ)*J.w2 - 3*J.ep^(2:ℕ)*J.p2*J.r0*J.w0^(2:ℕ)*J.w1 - J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w12 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1*J.w2 + J.ep^(2:ℕ)*J.r2*J.w0^(2:ℕ)*J.w1 + 3*J.p1*J.r0^(3:ℕ)*J.w2 + 2*J.p1*J.r0^(2:ℕ)*J.r2*J.w0 + 4*J.p12*J.r0^(3:ℕ)*J.w0 + J.p2*J.r0^(3:ℕ)*J.w1 + 2*J.p2*J.r0^(2:ℕ)*J.r1*J.w0 + J.r0^(3:ℕ)*J.w12 - J.r0^(2:ℕ)*J.r1*J.w2 - 2*J.r0^(2:ℕ)*J.r12*J.w0)/2) / ((J.r0)^(3:ℕ))), ((-(2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a1*J.p2*J.r0^(3:ℕ) + 4*J.a1*J.r0^(2:ℕ)*J.r2 + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a2*J.p1*J.r0^(3:ℕ) + 4*J.a2*J.r0^(2:ℕ)*J.r1 - 2*J.ep^(2:ℕ)*J.p1*J.r0*J.w0*J.w2 - 6*J.ep^(2:ℕ)*J.p2*J.r0*J.w0*J.w1 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w12 - 3*J.ep^(2:ℕ)*J.r0*J.w1*J.w2 + 2*J.ep^(2:ℕ)*J.r2*J.w0*J.w1 - 4*J.p1*J.p2*J.r0^(3:ℕ) + 4*J.p1*J.r0^(2:ℕ)*J.r2 + 4*J.p12*J.r0^(3:ℕ) + 4*J.p2*J.r0^(2:ℕ)*J.r1 - 4*J.r0^(2:ℕ)*J.r12)/4) / ((J.r0)^(3:ℕ)))], ![0, 0, (((J.a1*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w1 - 4*J.a1*J.p1*J.r0^(3:ℕ)*J.w0 - J.a1*J.r0^(3:ℕ)*J.w1 + 2*J.a1*J.r0^(2:ℕ)*J.r1*J.w0 + J.a2*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w2 - 4*J.a2*J.p2*J.r0^(3:ℕ)*J.w0 - J.a2*J.r0^(3:ℕ)*J.w2 + 2*J.a2*J.r0^(2:ℕ)*J.r2*J.w0 - 4*J.ep^(2:ℕ)*J.p2*J.r0*J.w0^(2:ℕ)*J.w2 - J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w22 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w2^(2:ℕ) + J.ep^(2:ℕ)*J.r2*J.w0^(2:ℕ)*J.w2 + 4*J.p2*J.r0^(3:ℕ)*J.w2 + 4*J.p2*J.r0^(2:ℕ)*J.r2*J.w0 + 4*J.p22*J.r0^(3:ℕ)*J.w0 + J.r0^(3:ℕ)*J.w22 - J.r0^(2:ℕ)*J.r2*J.w2 - 2*J.r0^(2:ℕ)*J.r22*J.w0)/2) / ((J.r0)^(3:ℕ))), ((-(2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a1*J.p1*J.r0^(3:ℕ) + 4*J.a1*J.r0^(2:ℕ)*J.r1 + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a2*J.p2*J.r0^(3:ℕ) + 4*J.a2*J.r0^(2:ℕ)*J.r2 - 8*J.ep^(2:ℕ)*J.p2*J.r0*J.w0*J.w2 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w22 - 3*J.ep^(2:ℕ)*J.r0*J.w2^(2:ℕ) + 2*J.ep^(2:ℕ)*J.r2*J.w0*J.w2 - 4*J.p2^(2:ℕ)*J.r0^(3:ℕ) + 8*J.p2*J.r0^(2:ℕ)*J.r2 + 4*J.p22*J.r0^(3:ℕ) - 4*J.r0^(2:ℕ)*J.r22)/4) / ((J.r0)^(3:ℕ)))], ![((-J.ep*(4*J.a1*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w2 + 4*J.a2*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w1 + J.ep^(2:ℕ)*J.w0*J.w1*J.w2 - 4*J.p1*J.p2*J.r0^(2:ℕ)*J.w0 - 6*J.p1*J.r0^(2:ℕ)*J.w2 - 4*J.p12*J.r0^(2:ℕ)*J.w0 - 2*J.p2*J.r0^(2:ℕ)*J.w1 - 2*J.r0^(2:ℕ)*J.w12 + 2*J.r0*J.r1*J.w2)/4) / ((J.ea) * (J.r0)^(2:ℕ))), ((J.ep*(4*J.a1*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w1 + 4*J.a2*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w2 + J.ep^(2:ℕ)*J.w0*J.w2^(2:ℕ) - 4*J.p2^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p2*J.r0^(2:ℕ)*J.w2 - 4*J.p22*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w22 + 2*J.r0*J.r2*J.w2)/4) / ((J.ea) * (J.r0)^(2:ℕ))), 0, 0], ![((-(4*J.a1*J.ep^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a1*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 4*J.a1*J.p2*J.r0^(4:ℕ) + 4*J.a1*J.r0^(3:ℕ)*J.r2 + 4*J.a2*J.ep^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a2*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.a2*J.p1*J.r0^(4:ℕ) + 4*J.a2*J.r0^(3:ℕ)*J.r1 + J.ep^(4:ℕ)*J.w0^(2:ℕ)*J.w1*J.w2 - 4*J.ep^(2:ℕ)*J.p1*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 8*J.ep^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0*J.w2 - 4*J.ep^(2:ℕ)*J.p12*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 8*J.ep^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w12 - 3*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w1*J.w2 + 2*J.ep^(2:ℕ)*J.r0*J.r1*J.w0*J.w2 + 2*J.ep^(2:ℕ)*J.r0*J.r2*J.w0*J.w1 - 4*J.p1*J.p2*J.r0^(4:ℕ) + 4*J.p1*J.r0^(3:ℕ)*J.r2 + 4*J.p12*J.r0^(4:ℕ) + 4*J.p2*J.r0^(3:ℕ)*J.r1 - 4*J.r0^(3:ℕ)*J.r12)/4) / ((J.ea) * (J.ep) * (J.r0)^(2:ℕ))), (((4*J.a1*J.ep^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a1*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.a1*J.p1*J.r0^(4:ℕ) + 4*J.a1*J.r0^(3:ℕ)*J.r1 + 4*J.a2*J.ep^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a2*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 4*J.a2*J.p2*J.r0^(4:ℕ) + 4*J.a2*J.r0^(3:ℕ)*J.r2 + J.ep^(4:ℕ)*J.w0^(2:ℕ)*J.w2^(2:ℕ) - 4*J.ep^(2:ℕ)*J.p2^(2:ℕ)*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 16*J.ep^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0*J.w2 - 4*J.ep^(2:ℕ)*J.p22*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 4*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w22 - 3*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w2^(2:ℕ) + 4*J.ep^(2:ℕ)*J.r0*J.r2*J.w0*J.w2 - 4*J.p2^(2:ℕ)*J.r0^(4:ℕ) + 8*J.p2*J.r0^(3:ℕ)*J.r2 + 4*J.p22*J.r0^(4:ℕ) - 4*J.r0^(3:ℕ)*J.r22)/4) / ((J.ea) * (J.ep) * (J.r0)^(2:ℕ))), 0, 0]]], 
    ![![![0, 0, ((-(2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a1*J.p1*J.r0^(3:ℕ) + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a2*J.p2*J.r0^(3:ℕ) - 8*J.ep^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w11 - J.ep^(2:ℕ)*J.r0*J.w1^(2:ℕ) + 2*J.ep^(2:ℕ)*J.r1*J.w0*J.w1 + 4*J.p1^(2:ℕ)*J.r0^(3:ℕ) + 4*J.p11*J.r0^(3:ℕ))/4) / ((J.r0)^(3:ℕ))), ((J.ep^(2:ℕ)*(J.a1*J.r0*J.w1 + J.a2*J.r0*J.w2 - 4*J.p1*J.r0*J.w1 - J.r0*J.w11 + J.r1*J.w1)/2) / ((J.r0)^(3:ℕ)))], ![0, 0, ((-(2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a1*J.p2*J.r0^(3:ℕ) + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a2*J.p1*J.r0^(3:ℕ) - 6*J.ep^(2:ℕ)*J.p1*J.r0*J.w0*J.w2 - 2*J.ep^(2:ℕ)*J.p2*J.r0*J.w0*J.w1 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w12 - J.ep^(2:ℕ)*J.r0*J.w1*J.w2 + 2*J.ep^(2:ℕ)*J.r1*J.w0*J.w2 + 4*J.p1*J.p2*J.r0^(3:ℕ) + 4*J.p12*J.r0^(3:ℕ))/4) / ((J.r0)^(3:ℕ))), ((J.ep^(2:ℕ)*(J.a1*J.r0*J.w2 + J.a2*J.r0*J.w1 - 3*J.p1*J.r0*J.w2 - J.p2*J.r0*J.w1 - J.r0*J.w12 + J.r1*J.w2)/2) / ((J.r0)^(3:ℕ)))], ![((J.ep*(4*J.a1*J.p1*J.r0^(2:ℕ) + 4*J.a2*J.p2*J.r0^(2:ℕ) + J.ep^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p11*J.r0^(2:ℕ))/4) / ((J.ea) * (J.r0)^(2:ℕ))), ((-J.ep*(4*J.a1*J.p2*J.r0^(2:ℕ) + 4*J.a2*J.p1*J.r0^(2:ℕ) + J.ep^(2:ℕ)*J.w1*J.w2 - 4*J.p1*J.p2*J.r0^(2:ℕ) - 4*J.p12*J.r0^(2:ℕ))/4) / ((J.ea) * (J.r0)^(2:ℕ))), 0, 0], ![((J.ep*(4*J.a1*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w1 + 4*J.a2*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w2 + J.ep^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p11*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w11 + 2*J.r0*J.r1*J.w1)/4) / ((J.ea) * (J.r0)^(2:ℕ))), ((-J.ep*(4*J.a1*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w2 + 4*J.a2*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w1 + J.ep^(2:ℕ)*J.w0*J.w1*J.w2 - 4*J.p1*J.p2*J.r0^(2:ℕ)*J.w0 - 6*J.p1*J.r0^(2:ℕ)*J.w2 - 4*J.p12*J.r0^(2:ℕ)*J.w0 - 2*J.p2*J.r0^(2:ℕ)*J.w1 - 2*J.r0^(2:ℕ)*J.w12 + 2*J.r0*J.r1*J.w2)/4) / ((J.ea) * (J.r0)^(2:ℕ))), 0, 0]], ![![0, 0, ((-(2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a1*J.p2*J.r0^(3:ℕ) + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a2*J.p1*J.r0^(3:ℕ) - 2*J.ep^(2:ℕ)*J.p1*J.r0*J.w0*J.w2 - 6*J.ep^(2:ℕ)*J.p2*J.r0*J.w0*J.w1 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w12 - J.ep^(2:ℕ)*J.r0*J.w1*J.w2 + 2*J.ep^(2:ℕ)*J.r2*J.w0*J.w1 + 4*J.p1*J.p2*J.r0^(3:ℕ) + 4*J.p12*J.r0^(3:ℕ))/4) / ((J.r0)^(3:ℕ))), ((J.ep^(2:ℕ)*(J.a1*J.r0*J.w2 + J.a2*J.r0*J.w1 - J.p1*J.r0*J.w2 - 3*J.p2*J.r0*J.w1 - J.r0*J.w12 + J.r2*J.w1)/2) / ((J.r0)^(3:ℕ)))], ![0, 0, ((-(2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a1*J.p1*J.r0^(3:ℕ) + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a2*J.p2*J.r0^(3:ℕ) - 8*J.ep^(2:ℕ)*J.p2*J.r0*J.w0*J.w2 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w22 - J.ep^(2:ℕ)*J.r0*J.w2^(2:ℕ) + 2*J.ep^(2:ℕ)*J.r2*J.w0*J.w2 + 4*J.p2^(2:ℕ)*J.r0^(3:ℕ) + 4*J.p22*J.r0^(3:ℕ))/4) / ((J.r0)^(3:ℕ))), ((J.ep^(2:ℕ)*(J.a1*J.r0*J.w1 + J.a2*J.r0*J.w2 - 4*J.p2*J.r0*J.w2 - J.r0*J.w22 + J.r2*J.w2)/2) / ((J.r0)^(3:ℕ)))], ![((J.ep*(4*J.a1*J.p2*J.r0^(2:ℕ) + 4*J.a2*J.p1*J.r0^(2:ℕ) + J.ep^(2:ℕ)*J.w1*J.w2 - 4*J.p1*J.p2*J.r0^(2:ℕ) - 4*J.p12*J.r0^(2:ℕ))/4) / ((J.ea) * (J.r0)^(2:ℕ))), ((-J.ep*(4*J.a1*J.p1*J.r0^(2:ℕ) + 4*J.a2*J.p2*J.r0^(2:ℕ) + J.ep^(2:ℕ)*J.w2^(2:ℕ) - 4*J.p2^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p22*J.r0^(2:ℕ))/4) / ((J.ea) * (J.r0)^(2:ℕ))), 0, 0], ![((J.ep*(4*J.a1*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w2 + 4*J.a2*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w1 + J.ep^(2:ℕ)*J.w0*J.w1*J.w2 - 4*J.p1*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.p1*J.r0^(2:ℕ)*J.w2 - 4*J.p12*J.r0^(2:ℕ)*J.w0 - 6*J.p2*J.r0^(2:ℕ)*J.w1 - 2*J.r0^(2:ℕ)*J.w12 + 2*J.r0*J.r2*J.w1)/4) / ((J.ea) * (J.r0)^(2:ℕ))), ((-J.ep*(4*J.a1*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w1 + 4*J.a2*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w2 + J.ep^(2:ℕ)*J.w0*J.w2^(2:ℕ) - 4*J.p2^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p2*J.r0^(2:ℕ)*J.w2 - 4*J.p22*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w22 + 2*J.r0*J.r2*J.w2)/4) / ((J.ea) * (J.r0)^(2:ℕ))), 0, 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, ((J.ep*(2*J.p1*J.r0*J.w2 - 2*J.p2*J.r0*J.w1 - J.r1*J.w2 + J.r2*J.w1)/2) / ((J.ea) * (J.r0))), 0, 0], ![((J.ep*(2*J.p1*J.r0*J.w2 - 2*J.p2*J.r0*J.w1 - J.r1*J.w2 + J.r2*J.w1)/2) / ((J.ea) * (J.r0))), 0, 0, 0], ![0, 0, ((-J.ep*J.w0*(J.ep^(2:ℕ)*J.w1^(2:ℕ) - J.ep^(2:ℕ)*J.w2^(2:ℕ) + 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p1*J.r0*J.r1 - 4*J.p2^(2:ℕ)*J.r0^(2:ℕ) + 4*J.p2*J.r0*J.r2)/4) / ((J.ea) * (J.r0)^(2:ℕ))), ((J.ep*(J.ep^(2:ℕ)*J.w1^(2:ℕ) - J.ep^(2:ℕ)*J.w2^(2:ℕ) + 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p1*J.r0*J.r1 - 4*J.p2^(2:ℕ)*J.r0^(2:ℕ) + 4*J.p2*J.r0*J.r2)/4) / ((J.ea) * (J.r0)^(2:ℕ)))], ![0, 0, ((-(J.ep^(2:ℕ)*J.w0^(2:ℕ) + J.r0^(2:ℕ))*(J.ep^(2:ℕ)*J.w1^(2:ℕ) - J.ep^(2:ℕ)*J.w2^(2:ℕ) + 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p1*J.r0*J.r1 - 4*J.p2^(2:ℕ)*J.r0^(2:ℕ) + 4*J.p2*J.r0*J.r2)/4) / ((J.ea) * (J.ep) * (J.r0)^(2:ℕ))), ((J.ep*J.w0*(J.ep^(2:ℕ)*J.w1^(2:ℕ) - J.ep^(2:ℕ)*J.w2^(2:ℕ) + 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p1*J.r0*J.r1 - 4*J.p2^(2:ℕ)*J.r0^(2:ℕ) + 4*J.p2*J.r0*J.r2)/4) / ((J.ea) * (J.r0)^(2:ℕ)))]]], 
    ![![![0, 0, ((-(J.a1*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w1 - 4*J.a1*J.p1*J.r0^(3:ℕ)*J.w0 - J.a1*J.r0^(3:ℕ)*J.w1 + 2*J.a1*J.r0^(2:ℕ)*J.r1*J.w0 + J.a2*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w2 - 4*J.a2*J.p2*J.r0^(3:ℕ)*J.w0 - J.a2*J.r0^(3:ℕ)*J.w2 + 2*J.a2*J.r0^(2:ℕ)*J.r2*J.w0 - 4*J.ep^(2:ℕ)*J.p1*J.r0*J.w0^(2:ℕ)*J.w1 - J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w11 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1^(2:ℕ) + J.ep^(2:ℕ)*J.r1*J.w0^(2:ℕ)*J.w1 + 4*J.p1*J.r0^(3:ℕ)*J.w1 + 4*J.p1*J.r0^(2:ℕ)*J.r1*J.w0 + 4*J.p11*J.r0^(3:ℕ)*J.w0 + J.r0^(3:ℕ)*J.w11 - J.r0^(2:ℕ)*J.r1*J.w1 - 2*J.r0^(2:ℕ)*J.r11*J.w0)/2) / ((J.r0)^(3:ℕ))), (((2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a1*J.p1*J.r0^(3:ℕ) + 4*J.a1*J.r0^(2:ℕ)*J.r1 + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a2*J.p2*J.r0^(3:ℕ) + 4*J.a2*J.r0^(2:ℕ)*J.r2 - 8*J.ep^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w11 - 3*J.ep^(2:ℕ)*J.r0*J.w1^(2:ℕ) + 2*J.ep^(2:ℕ)*J.r1*J.w0*J.w1 - 4*J.p1^(2:ℕ)*J.r0^(3:ℕ) + 8*J.p1*J.r0^(2:ℕ)*J.r1 + 4*J.p11*J.r0^(3:ℕ) - 4*J.r0^(2:ℕ)*J.r11)/4) / ((J.r0)^(3:ℕ)))], ![0, 0, ((-(J.a1*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w2 - 4*J.a1*J.p2*J.r0^(3:ℕ)*J.w0 - J.a1*J.r0^(3:ℕ)*J.w2 + 2*J.a1*J.r0^(2:ℕ)*J.r2*J.w0 + J.a2*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w1 - 4*J.a2*J.p1*J.r0^(3:ℕ)*J.w0 - J.a2*J.r0^(3:ℕ)*J.w1 + 2*J.a2*J.r0^(2:ℕ)*J.r1*J.w0 - 3*J.ep^(2:ℕ)*J.p1*J.r0*J.w0^(2:ℕ)*J.w2 - J.ep^(2:ℕ)*J.p2*J.r0*J.w0^(2:ℕ)*J.w1 - J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w12 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1*J.w2 + J.ep^(2:ℕ)*J.r1*J.w0^(2:ℕ)*J.w2 + J.p1*J.r0^(3:ℕ)*J.w2 + 2*J.p1*J.r0^(2:ℕ)*J.r2*J.w0 + 4*J.p12*J.r0^(3:ℕ)*J.w0 + 3*J.p2*J.r0^(3:ℕ)*J.w1 + 2*J.p2*J.r0^(2:ℕ)*J.r1*J.w0 + J.r0^(3:ℕ)*J.w12 - 2*J.r0^(2:ℕ)*J.r12*J.w0 - J.r0^(2:ℕ)*J.r2*J.w1)/2) / ((J.r0)^(3:ℕ))), (((2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a1*J.p2*J.r0^(3:ℕ) + 4*J.a1*J.r0^(2:ℕ)*J.r2 + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a2*J.p1*J.r0^(3:ℕ) + 4*J.a2*J.r0^(2:ℕ)*J.r1 - 6*J.ep^(2:ℕ)*J.p1*J.r0*J.w0*J.w2 - 2*J.ep^(2:ℕ)*J.p2*J.r0*J.w0*J.w1 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w12 - 3*J.ep^(2:ℕ)*J.r0*J.w1*J.w2 + 2*J.ep^(2:ℕ)*J.r1*J.w0*J.w2 - 4*J.p1*J.p2*J.r0^(3:ℕ) + 4*J.p1*J.r0^(2:ℕ)*J.r2 + 4*J.p12*J.r0^(3:ℕ) + 4*J.p2*J.r0^(2:ℕ)*J.r1 - 4*J.r0^(2:ℕ)*J.r12)/4) / ((J.r0)^(3:ℕ)))], ![((J.ep*(4*J.a1*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w1 + 4*J.a2*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w2 + J.ep^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p11*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w11 + 2*J.r0*J.r1*J.w1)/4) / ((J.ea) * (J.r0)^(2:ℕ))), ((-J.ep*(4*J.a1*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w2 + 4*J.a2*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w1 + J.ep^(2:ℕ)*J.w0*J.w1*J.w2 - 4*J.p1*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.p1*J.r0^(2:ℕ)*J.w2 - 4*J.p12*J.r0^(2:ℕ)*J.w0 - 6*J.p2*J.r0^(2:ℕ)*J.w1 - 2*J.r0^(2:ℕ)*J.w12 + 2*J.r0*J.r2*J.w1)/4) / ((J.ea) * (J.r0)^(2:ℕ))), 0, 0], ![(((4*J.a1*J.ep^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a1*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.a1*J.p1*J.r0^(4:ℕ) + 4*J.a1*J.r0^(3:ℕ)*J.r1 + 4*J.a2*J.ep^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a2*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 4*J.a2*J.p2*J.r0^(4:ℕ) + 4*J.a2*J.r0^(3:ℕ)*J.r2 + J.ep^(4:ℕ)*J.w0^(2:ℕ)*J.w1^(2:ℕ) - 4*J.ep^(2:ℕ)*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 16*J.ep^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.ep^(2:ℕ)*J.p11*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 4*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w11 - 3*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w1^(2:ℕ) + 4*J.ep^(2:ℕ)*J.r0*J.r1*J.w0*J.w1 - 4*J.p1^(2:ℕ)*J.r0^(4:ℕ) + 8*J.p1*J.r0^(3:ℕ)*J.r1 + 4*J.p11*J.r0^(4:ℕ) - 4*J.r0^(3:ℕ)*J.r11)/4) / ((J.ea) * (J.ep) * (J.r0)^(2:ℕ))), ((-(4*J.a1*J.ep^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a1*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 4*J.a1*J.p2*J.r0^(4:ℕ) + 4*J.a1*J.r0^(3:ℕ)*J.r2 + 4*J.a2*J.ep^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a2*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.a2*J.p1*J.r0^(4:ℕ) + 4*J.a2*J.r0^(3:ℕ)*J.r1 + J.ep^(4:ℕ)*J.w0^(2:ℕ)*J.w1*J.w2 - 4*J.ep^(2:ℕ)*J.p1*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 8*J.ep^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0*J.w2 - 4*J.ep^(2:ℕ)*J.p12*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 8*J.ep^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w12 - 3*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w1*J.w2 + 2*J.ep^(2:ℕ)*J.r0*J.r1*J.w0*J.w2 + 2*J.ep^(2:ℕ)*J.r0*J.r2*J.w0*J.w1 - 4*J.p1*J.p2*J.r0^(4:ℕ) + 4*J.p1*J.r0^(3:ℕ)*J.r2 + 4*J.p12*J.r0^(4:ℕ) + 4*J.p2*J.r0^(3:ℕ)*J.r1 - 4*J.r0^(3:ℕ)*J.r12)/4) / ((J.ea) * (J.ep) * (J.r0)^(2:ℕ))), 0, 0]], ![![0, 0, ((-(J.a1*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w2 - 4*J.a1*J.p2*J.r0^(3:ℕ)*J.w0 - J.a1*J.r0^(3:ℕ)*J.w2 + 2*J.a1*J.r0^(2:ℕ)*J.r2*J.w0 + J.a2*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w1 - 4*J.a2*J.p1*J.r0^(3:ℕ)*J.w0 - J.a2*J.r0^(3:ℕ)*J.w1 + 2*J.a2*J.r0^(2:ℕ)*J.r1*J.w0 - J.ep^(2:ℕ)*J.p1*J.r0*J.w0^(2:ℕ)*J.w2 - 3*J.ep^(2:ℕ)*J.p2*J.r0*J.w0^(2:ℕ)*J.w1 - J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w12 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1*J.w2 + J.ep^(2:ℕ)*J.r2*J.w0^(2:ℕ)*J.w1 + 3*J.p1*J.r0^(3:ℕ)*J.w2 + 2*J.p1*J.r0^(2:ℕ)*J.r2*J.w0 + 4*J.p12*J.r0^(3:ℕ)*J.w0 + J.p2*J.r0^(3:ℕ)*J.w1 + 2*J.p2*J.r0^(2:ℕ)*J.r1*J.w0 + J.r0^(3:ℕ)*J.w12 - J.r0^(2:ℕ)*J.r1*J.w2 - 2*J.r0^(2:ℕ)*J.r12*J.w0)/2) / ((J.r0)^(3:ℕ))), (((2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a1*J.p2*J.r0^(3:ℕ) + 4*J.a1*J.r0^(2:ℕ)*J.r2 + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a2*J.p1*J.r0^(3:ℕ) + 4*J.a2*J.r0^(2:ℕ)*J.r1 - 2*J.ep^(2:ℕ)*J.p1*J.r0*J.w0*J.w2 - 6*J.ep^(2:ℕ)*J.p2*J.r0*J.w0*J.w1 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w12 - 3*J.ep^(2:ℕ)*J.r0*J.w1*J.w2 + 2*J.ep^(2:ℕ)*J.r2*J.w0*J.w1 - 4*J.p1*J.p2*J.r0^(3:ℕ) + 4*J.p1*J.r0^(2:ℕ)*J.r2 + 4*J.p12*J.r0^(3:ℕ) + 4*J.p2*J.r0^(2:ℕ)*J.r1 - 4*J.r0^(2:ℕ)*J.r12)/4) / ((J.r0)^(3:ℕ)))], ![0, 0, ((-(J.a1*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w1 - 4*J.a1*J.p1*J.r0^(3:ℕ)*J.w0 - J.a1*J.r0^(3:ℕ)*J.w1 + 2*J.a1*J.r0^(2:ℕ)*J.r1*J.w0 + J.a2*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w2 - 4*J.a2*J.p2*J.r0^(3:ℕ)*J.w0 - J.a2*J.r0^(3:ℕ)*J.w2 + 2*J.a2*J.r0^(2:ℕ)*J.r2*J.w0 - 4*J.ep^(2:ℕ)*J.p2*J.r0*J.w0^(2:ℕ)*J.w2 - J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w22 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w2^(2:ℕ) + J.ep^(2:ℕ)*J.r2*J.w0^(2:ℕ)*J.w2 + 4*J.p2*J.r0^(3:ℕ)*J.w2 + 4*J.p2*J.r0^(2:ℕ)*J.r2*J.w0 + 4*J.p22*J.r0^(3:ℕ)*J.w0 + J.r0^(3:ℕ)*J.w22 - J.r0^(2:ℕ)*J.r2*J.w2 - 2*J.r0^(2:ℕ)*J.r22*J.w0)/2) / ((J.r0)^(3:ℕ))), (((2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a1*J.p1*J.r0^(3:ℕ) + 4*J.a1*J.r0^(2:ℕ)*J.r1 + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a2*J.p2*J.r0^(3:ℕ) + 4*J.a2*J.r0^(2:ℕ)*J.r2 - 8*J.ep^(2:ℕ)*J.p2*J.r0*J.w0*J.w2 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w22 - 3*J.ep^(2:ℕ)*J.r0*J.w2^(2:ℕ) + 2*J.ep^(2:ℕ)*J.r2*J.w0*J.w2 - 4*J.p2^(2:ℕ)*J.r0^(3:ℕ) + 8*J.p2*J.r0^(2:ℕ)*J.r2 + 4*J.p22*J.r0^(3:ℕ) - 4*J.r0^(2:ℕ)*J.r22)/4) / ((J.r0)^(3:ℕ)))], ![((J.ep*(4*J.a1*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w2 + 4*J.a2*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w1 + J.ep^(2:ℕ)*J.w0*J.w1*J.w2 - 4*J.p1*J.p2*J.r0^(2:ℕ)*J.w0 - 6*J.p1*J.r0^(2:ℕ)*J.w2 - 4*J.p12*J.r0^(2:ℕ)*J.w0 - 2*J.p2*J.r0^(2:ℕ)*J.w1 - 2*J.r0^(2:ℕ)*J.w12 + 2*J.r0*J.r1*J.w2)/4) / ((J.ea) * (J.r0)^(2:ℕ))), ((-J.ep*(4*J.a1*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w1 + 4*J.a2*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w2 + J.ep^(2:ℕ)*J.w0*J.w2^(2:ℕ) - 4*J.p2^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p2*J.r0^(2:ℕ)*J.w2 - 4*J.p22*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w22 + 2*J.r0*J.r2*J.w2)/4) / ((J.ea) * (J.r0)^(2:ℕ))), 0, 0], ![(((4*J.a1*J.ep^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a1*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 4*J.a1*J.p2*J.r0^(4:ℕ) + 4*J.a1*J.r0^(3:ℕ)*J.r2 + 4*J.a2*J.ep^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a2*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.a2*J.p1*J.r0^(4:ℕ) + 4*J.a2*J.r0^(3:ℕ)*J.r1 + J.ep^(4:ℕ)*J.w0^(2:ℕ)*J.w1*J.w2 - 4*J.ep^(2:ℕ)*J.p1*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 8*J.ep^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0*J.w2 - 4*J.ep^(2:ℕ)*J.p12*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 8*J.ep^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w12 - 3*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w1*J.w2 + 2*J.ep^(2:ℕ)*J.r0*J.r1*J.w0*J.w2 + 2*J.ep^(2:ℕ)*J.r0*J.r2*J.w0*J.w1 - 4*J.p1*J.p2*J.r0^(4:ℕ) + 4*J.p1*J.r0^(3:ℕ)*J.r2 + 4*J.p12*J.r0^(4:ℕ) + 4*J.p2*J.r0^(3:ℕ)*J.r1 - 4*J.r0^(3:ℕ)*J.r12)/4) / ((J.ea) * (J.ep) * (J.r0)^(2:ℕ))), ((-(4*J.a1*J.ep^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a1*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.a1*J.p1*J.r0^(4:ℕ) + 4*J.a1*J.r0^(3:ℕ)*J.r1 + 4*J.a2*J.ep^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a2*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 4*J.a2*J.p2*J.r0^(4:ℕ) + 4*J.a2*J.r0^(3:ℕ)*J.r2 + J.ep^(4:ℕ)*J.w0^(2:ℕ)*J.w2^(2:ℕ) - 4*J.ep^(2:ℕ)*J.p2^(2:ℕ)*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 16*J.ep^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0*J.w2 - 4*J.ep^(2:ℕ)*J.p22*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 4*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w22 - 3*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w2^(2:ℕ) + 4*J.ep^(2:ℕ)*J.r0*J.r2*J.w0*J.w2 - 4*J.p2^(2:ℕ)*J.r0^(4:ℕ) + 8*J.p2*J.r0^(3:ℕ)*J.r2 + 4*J.p22*J.r0^(4:ℕ) - 4*J.r0^(3:ℕ)*J.r22)/4) / ((J.ea) * (J.ep) * (J.r0)^(2:ℕ))), 0, 0]], ![![0, ((-J.ep*(2*J.p1*J.r0*J.w2 - 2*J.p2*J.r0*J.w1 - J.r1*J.w2 + J.r2*J.w1)/2) / ((J.ea) * (J.r0))), 0, 0], ![((-J.ep*(2*J.p1*J.r0*J.w2 - 2*J.p2*J.r0*J.w1 - J.r1*J.w2 + J.r2*J.w1)/2) / ((J.ea) * (J.r0))), 0, 0, 0], ![0, 0, ((J.ep*J.w0*(J.ep^(2:ℕ)*J.w1^(2:ℕ) - J.ep^(2:ℕ)*J.w2^(2:ℕ) + 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p1*J.r0*J.r1 - 4*J.p2^(2:ℕ)*J.r0^(2:ℕ) + 4*J.p2*J.r0*J.r2)/4) / ((J.ea) * (J.r0)^(2:ℕ))), ((-J.ep*(J.ep^(2:ℕ)*J.w1^(2:ℕ) - J.ep^(2:ℕ)*J.w2^(2:ℕ) + 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p1*J.r0*J.r1 - 4*J.p2^(2:ℕ)*J.r0^(2:ℕ) + 4*J.p2*J.r0*J.r2)/4) / ((J.ea) * (J.r0)^(2:ℕ)))], ![0, 0, (((J.ep^(2:ℕ)*J.w0^(2:ℕ) + J.r0^(2:ℕ))*(J.ep^(2:ℕ)*J.w1^(2:ℕ) - J.ep^(2:ℕ)*J.w2^(2:ℕ) + 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p1*J.r0*J.r1 - 4*J.p2^(2:ℕ)*J.r0^(2:ℕ) + 4*J.p2*J.r0*J.r2)/4) / ((J.ea) * (J.ep) * (J.r0)^(2:ℕ))), ((-J.ep*J.w0*(J.ep^(2:ℕ)*J.w1^(2:ℕ) - J.ep^(2:ℕ)*J.w2^(2:ℕ) + 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p1*J.r0*J.r1 - 4*J.p2^(2:ℕ)*J.r0^(2:ℕ) + 4*J.p2*J.r0*J.r2)/4) / ((J.ea) * (J.r0)^(2:ℕ)))]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]]]]

noncomputable def WRDT (J : GJ) : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ :=
  ![![![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, (-J.ea*(J.a11 - J.a22)), 0, 0], ![(J.ea*(J.a11 - J.a22)), 0, 0, 0], ![0, 0, 0, ((-J.ep*(2*J.p1*J.r0*J.w2 - 2*J.p2*J.r0*J.w1 - J.r1*J.w2 + J.r2*J.w1)/2) / ((J.r0)))], ![0, 0, ((J.ep*(2*J.p1*J.r0*J.w2 - 2*J.p2*J.r0*J.w1 - J.r1*J.w2 + J.r2*J.w1)/2) / ((J.r0))), 0]], ![![0, 0, ((J.ep*(4*J.a1*J.p1*J.r0^(2:ℕ) + 4*J.a2*J.p2*J.r0^(2:ℕ) + J.ep^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p11*J.r0^(2:ℕ))/4) / ((J.r0)^(2:ℕ))), ((J.ep*(4*J.a1*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w1 + 4*J.a2*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w2 + J.ep^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p11*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w11 + 2*J.r0*J.r1*J.w1)/4) / ((J.r0)^(2:ℕ)))], ![0, 0, ((J.ep*(4*J.a1*J.p2*J.r0^(2:ℕ) + 4*J.a2*J.p1*J.r0^(2:ℕ) + J.ep^(2:ℕ)*J.w1*J.w2 - 4*J.p1*J.p2*J.r0^(2:ℕ) - 4*J.p12*J.r0^(2:ℕ))/4) / ((J.r0)^(2:ℕ))), ((J.ep*(4*J.a1*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w2 + 4*J.a2*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w1 + J.ep^(2:ℕ)*J.w0*J.w1*J.w2 - 4*J.p1*J.p2*J.r0^(2:ℕ)*J.w0 - 6*J.p1*J.r0^(2:ℕ)*J.w2 - 4*J.p12*J.r0^(2:ℕ)*J.w0 - 2*J.p2*J.r0^(2:ℕ)*J.w1 - 2*J.r0^(2:ℕ)*J.w12 + 2*J.r0*J.r1*J.w2)/4) / ((J.r0)^(2:ℕ)))], ![((-J.ep*(4*J.a1*J.p1*J.r0^(2:ℕ) + 4*J.a2*J.p2*J.r0^(2:ℕ) + J.ep^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p11*J.r0^(2:ℕ))/4) / ((J.r0)^(2:ℕ))), ((-J.ep*(4*J.a1*J.p2*J.r0^(2:ℕ) + 4*J.a2*J.p1*J.r0^(2:ℕ) + J.ep^(2:ℕ)*J.w1*J.w2 - 4*J.p1*J.p2*J.r0^(2:ℕ) - 4*J.p12*J.r0^(2:ℕ))/4) / ((J.r0)^(2:ℕ))), 0, 0], ![((-J.ep*(4*J.a1*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w1 + 4*J.a2*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w2 + J.ep^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p11*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w11 + 2*J.r0*J.r1*J.w1)/4) / ((J.r0)^(2:ℕ))), ((-J.ep*(4*J.a1*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w2 + 4*J.a2*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w1 + J.ep^(2:ℕ)*J.w0*J.w1*J.w2 - 4*J.p1*J.p2*J.r0^(2:ℕ)*J.w0 - 6*J.p1*J.r0^(2:ℕ)*J.w2 - 4*J.p12*J.r0^(2:ℕ)*J.w0 - 2*J.p2*J.r0^(2:ℕ)*J.w1 - 2*J.r0^(2:ℕ)*J.w12 + 2*J.r0*J.r1*J.w2)/4) / ((J.r0)^(2:ℕ))), 0, 0]], ![![0, 0, ((J.ep*(4*J.a1*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w1 + 4*J.a2*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w2 + J.ep^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p11*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w11 + 2*J.r0*J.r1*J.w1)/4) / ((J.r0)^(2:ℕ))), (((4*J.a1*J.ep^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a1*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.a1*J.p1*J.r0^(4:ℕ) + 4*J.a1*J.r0^(3:ℕ)*J.r1 + 4*J.a2*J.ep^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a2*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 4*J.a2*J.p2*J.r0^(4:ℕ) + 4*J.a2*J.r0^(3:ℕ)*J.r2 + J.ep^(4:ℕ)*J.w0^(2:ℕ)*J.w1^(2:ℕ) - 4*J.ep^(2:ℕ)*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 16*J.ep^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.ep^(2:ℕ)*J.p11*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 4*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w11 - 3*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w1^(2:ℕ) + 4*J.ep^(2:ℕ)*J.r0*J.r1*J.w0*J.w1 - 4*J.p1^(2:ℕ)*J.r0^(4:ℕ) + 8*J.p1*J.r0^(3:ℕ)*J.r1 + 4*J.p11*J.r0^(4:ℕ) - 4*J.r0^(3:ℕ)*J.r11)/4) / ((J.ep) * (J.r0)^(2:ℕ)))], ![0, 0, ((J.ep*(4*J.a1*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w2 + 4*J.a2*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w1 + J.ep^(2:ℕ)*J.w0*J.w1*J.w2 - 4*J.p1*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.p1*J.r0^(2:ℕ)*J.w2 - 4*J.p12*J.r0^(2:ℕ)*J.w0 - 6*J.p2*J.r0^(2:ℕ)*J.w1 - 2*J.r0^(2:ℕ)*J.w12 + 2*J.r0*J.r2*J.w1)/4) / ((J.r0)^(2:ℕ))), (((4*J.a1*J.ep^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a1*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 4*J.a1*J.p2*J.r0^(4:ℕ) + 4*J.a1*J.r0^(3:ℕ)*J.r2 + 4*J.a2*J.ep^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a2*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.a2*J.p1*J.r0^(4:ℕ) + 4*J.a2*J.r0^(3:ℕ)*J.r1 + J.ep^(4:ℕ)*J.w0^(2:ℕ)*J.w1*J.w2 - 4*J.ep^(2:ℕ)*J.p1*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 8*J.ep^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0*J.w2 - 4*J.ep^(2:ℕ)*J.p12*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 8*J.ep^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w12 - 3*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w1*J.w2 + 2*J.ep^(2:ℕ)*J.r0*J.r1*J.w0*J.w2 + 2*J.ep^(2:ℕ)*J.r0*J.r2*J.w0*J.w1 - 4*J.p1*J.p2*J.r0^(4:ℕ) + 4*J.p1*J.r0^(3:ℕ)*J.r2 + 4*J.p12*J.r0^(4:ℕ) + 4*J.p2*J.r0^(3:ℕ)*J.r1 - 4*J.r0^(3:ℕ)*J.r12)/4) / ((J.ep) * (J.r0)^(2:ℕ)))], ![((-J.ep*(4*J.a1*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w1 + 4*J.a2*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w2 + J.ep^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p11*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w11 + 2*J.r0*J.r1*J.w1)/4) / ((J.r0)^(2:ℕ))), ((-J.ep*(4*J.a1*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w2 + 4*J.a2*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w1 + J.ep^(2:ℕ)*J.w0*J.w1*J.w2 - 4*J.p1*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.p1*J.r0^(2:ℕ)*J.w2 - 4*J.p12*J.r0^(2:ℕ)*J.w0 - 6*J.p2*J.r0^(2:ℕ)*J.w1 - 2*J.r0^(2:ℕ)*J.w12 + 2*J.r0*J.r2*J.w1)/4) / ((J.r0)^(2:ℕ))), 0, 0], ![((-(4*J.a1*J.ep^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a1*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.a1*J.p1*J.r0^(4:ℕ) + 4*J.a1*J.r0^(3:ℕ)*J.r1 + 4*J.a2*J.ep^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a2*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 4*J.a2*J.p2*J.r0^(4:ℕ) + 4*J.a2*J.r0^(3:ℕ)*J.r2 + J.ep^(4:ℕ)*J.w0^(2:ℕ)*J.w1^(2:ℕ) - 4*J.ep^(2:ℕ)*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 16*J.ep^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.ep^(2:ℕ)*J.p11*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 4*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w11 - 3*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w1^(2:ℕ) + 4*J.ep^(2:ℕ)*J.r0*J.r1*J.w0*J.w1 - 4*J.p1^(2:ℕ)*J.r0^(4:ℕ) + 8*J.p1*J.r0^(3:ℕ)*J.r1 + 4*J.p11*J.r0^(4:ℕ) - 4*J.r0^(3:ℕ)*J.r11)/4) / ((J.ep) * (J.r0)^(2:ℕ))), ((-(4*J.a1*J.ep^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a1*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 4*J.a1*J.p2*J.r0^(4:ℕ) + 4*J.a1*J.r0^(3:ℕ)*J.r2 + 4*J.a2*J.ep^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a2*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.a2*J.p1*J.r0^(4:ℕ) + 4*J.a2*J.r0^(3:ℕ)*J.r1 + J.ep^(4:ℕ)*J.w0^(2:ℕ)*J.w1*J.w2 - 4*J.ep^(2:ℕ)*J.p1*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 8*J.ep^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0*J.w2 - 4*J.ep^(2:ℕ)*J.p12*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 8*J.ep^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w12 - 3*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w1*J.w2 + 2*J.ep^(2:ℕ)*J.r0*J.r1*J.w0*J.w2 + 2*J.ep^(2:ℕ)*J.r0*J.r2*J.w0*J.w1 - 4*J.p1*J.p2*J.r0^(4:ℕ) + 4*J.p1*J.r0^(3:ℕ)*J.r2 + 4*J.p12*J.r0^(4:ℕ) + 4*J.p2*J.r0^(3:ℕ)*J.r1 - 4*J.r0^(3:ℕ)*J.r12)/4) / ((J.ep) * (J.r0)^(2:ℕ))), 0, 0]]], 
    ![![![0, (J.ea*(J.a11 - J.a22)), 0, 0], ![(-J.ea*(J.a11 - J.a22)), 0, 0, 0], ![0, 0, 0, ((J.ep*(2*J.p1*J.r0*J.w2 - 2*J.p2*J.r0*J.w1 - J.r1*J.w2 + J.r2*J.w1)/2) / ((J.r0)))], ![0, 0, ((-J.ep*(2*J.p1*J.r0*J.w2 - 2*J.p2*J.r0*J.w1 - J.r1*J.w2 + J.r2*J.w1)/2) / ((J.r0))), 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, 0, ((J.ep*(4*J.a1*J.p2*J.r0^(2:ℕ) + 4*J.a2*J.p1*J.r0^(2:ℕ) + J.ep^(2:ℕ)*J.w1*J.w2 - 4*J.p1*J.p2*J.r0^(2:ℕ) - 4*J.p12*J.r0^(2:ℕ))/4) / ((J.r0)^(2:ℕ))), ((J.ep*(4*J.a1*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w2 + 4*J.a2*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w1 + J.ep^(2:ℕ)*J.w0*J.w1*J.w2 - 4*J.p1*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.p1*J.r0^(2:ℕ)*J.w2 - 4*J.p12*J.r0^(2:ℕ)*J.w0 - 6*J.p2*J.r0^(2:ℕ)*J.w1 - 2*J.r0^(2:ℕ)*J.w12 + 2*J.r0*J.r2*J.w1)/4) / ((J.r0)^(2:ℕ)))], ![0, 0, ((J.ep*(4*J.a1*J.p1*J.r0^(2:ℕ) + 4*J.a2*J.p2*J.r0^(2:ℕ) + J.ep^(2:ℕ)*J.w2^(2:ℕ) - 4*J.p2^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p22*J.r0^(2:ℕ))/4) / ((J.r0)^(2:ℕ))), ((J.ep*(4*J.a1*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w1 + 4*J.a2*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w2 + J.ep^(2:ℕ)*J.w0*J.w2^(2:ℕ) - 4*J.p2^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p2*J.r0^(2:ℕ)*J.w2 - 4*J.p22*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w22 + 2*J.r0*J.r2*J.w2)/4) / ((J.r0)^(2:ℕ)))], ![((-J.ep*(4*J.a1*J.p2*J.r0^(2:ℕ) + 4*J.a2*J.p1*J.r0^(2:ℕ) + J.ep^(2:ℕ)*J.w1*J.w2 - 4*J.p1*J.p2*J.r0^(2:ℕ) - 4*J.p12*J.r0^(2:ℕ))/4) / ((J.r0)^(2:ℕ))), ((-J.ep*(4*J.a1*J.p1*J.r0^(2:ℕ) + 4*J.a2*J.p2*J.r0^(2:ℕ) + J.ep^(2:ℕ)*J.w2^(2:ℕ) - 4*J.p2^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p22*J.r0^(2:ℕ))/4) / ((J.r0)^(2:ℕ))), 0, 0], ![((-J.ep*(4*J.a1*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w2 + 4*J.a2*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w1 + J.ep^(2:ℕ)*J.w0*J.w1*J.w2 - 4*J.p1*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.p1*J.r0^(2:ℕ)*J.w2 - 4*J.p12*J.r0^(2:ℕ)*J.w0 - 6*J.p2*J.r0^(2:ℕ)*J.w1 - 2*J.r0^(2:ℕ)*J.w12 + 2*J.r0*J.r2*J.w1)/4) / ((J.r0)^(2:ℕ))), ((-J.ep*(4*J.a1*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w1 + 4*J.a2*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w2 + J.ep^(2:ℕ)*J.w0*J.w2^(2:ℕ) - 4*J.p2^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p2*J.r0^(2:ℕ)*J.w2 - 4*J.p22*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w22 + 2*J.r0*J.r2*J.w2)/4) / ((J.r0)^(2:ℕ))), 0, 0]], ![![0, 0, ((J.ep*(4*J.a1*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w2 + 4*J.a2*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w1 + J.ep^(2:ℕ)*J.w0*J.w1*J.w2 - 4*J.p1*J.p2*J.r0^(2:ℕ)*J.w0 - 6*J.p1*J.r0^(2:ℕ)*J.w2 - 4*J.p12*J.r0^(2:ℕ)*J.w0 - 2*J.p2*J.r0^(2:ℕ)*J.w1 - 2*J.r0^(2:ℕ)*J.w12 + 2*J.r0*J.r1*J.w2)/4) / ((J.r0)^(2:ℕ))), (((4*J.a1*J.ep^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a1*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 4*J.a1*J.p2*J.r0^(4:ℕ) + 4*J.a1*J.r0^(3:ℕ)*J.r2 + 4*J.a2*J.ep^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a2*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.a2*J.p1*J.r0^(4:ℕ) + 4*J.a2*J.r0^(3:ℕ)*J.r1 + J.ep^(4:ℕ)*J.w0^(2:ℕ)*J.w1*J.w2 - 4*J.ep^(2:ℕ)*J.p1*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 8*J.ep^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0*J.w2 - 4*J.ep^(2:ℕ)*J.p12*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 8*J.ep^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w12 - 3*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w1*J.w2 + 2*J.ep^(2:ℕ)*J.r0*J.r1*J.w0*J.w2 + 2*J.ep^(2:ℕ)*J.r0*J.r2*J.w0*J.w1 - 4*J.p1*J.p2*J.r0^(4:ℕ) + 4*J.p1*J.r0^(3:ℕ)*J.r2 + 4*J.p12*J.r0^(4:ℕ) + 4*J.p2*J.r0^(3:ℕ)*J.r1 - 4*J.r0^(3:ℕ)*J.r12)/4) / ((J.ep) * (J.r0)^(2:ℕ)))], ![0, 0, ((J.ep*(4*J.a1*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w1 + 4*J.a2*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w2 + J.ep^(2:ℕ)*J.w0*J.w2^(2:ℕ) - 4*J.p2^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p2*J.r0^(2:ℕ)*J.w2 - 4*J.p22*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w22 + 2*J.r0*J.r2*J.w2)/4) / ((J.r0)^(2:ℕ))), (((4*J.a1*J.ep^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a1*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.a1*J.p1*J.r0^(4:ℕ) + 4*J.a1*J.r0^(3:ℕ)*J.r1 + 4*J.a2*J.ep^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a2*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 4*J.a2*J.p2*J.r0^(4:ℕ) + 4*J.a2*J.r0^(3:ℕ)*J.r2 + J.ep^(4:ℕ)*J.w0^(2:ℕ)*J.w2^(2:ℕ) - 4*J.ep^(2:ℕ)*J.p2^(2:ℕ)*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 16*J.ep^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0*J.w2 - 4*J.ep^(2:ℕ)*J.p22*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 4*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w22 - 3*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w2^(2:ℕ) + 4*J.ep^(2:ℕ)*J.r0*J.r2*J.w0*J.w2 - 4*J.p2^(2:ℕ)*J.r0^(4:ℕ) + 8*J.p2*J.r0^(3:ℕ)*J.r2 + 4*J.p22*J.r0^(4:ℕ) - 4*J.r0^(3:ℕ)*J.r22)/4) / ((J.ep) * (J.r0)^(2:ℕ)))], ![((-J.ep*(4*J.a1*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w2 + 4*J.a2*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w1 + J.ep^(2:ℕ)*J.w0*J.w1*J.w2 - 4*J.p1*J.p2*J.r0^(2:ℕ)*J.w0 - 6*J.p1*J.r0^(2:ℕ)*J.w2 - 4*J.p12*J.r0^(2:ℕ)*J.w0 - 2*J.p2*J.r0^(2:ℕ)*J.w1 - 2*J.r0^(2:ℕ)*J.w12 + 2*J.r0*J.r1*J.w2)/4) / ((J.r0)^(2:ℕ))), ((-J.ep*(4*J.a1*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w1 + 4*J.a2*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w2 + J.ep^(2:ℕ)*J.w0*J.w2^(2:ℕ) - 4*J.p2^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p2*J.r0^(2:ℕ)*J.w2 - 4*J.p22*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w22 + 2*J.r0*J.r2*J.w2)/4) / ((J.r0)^(2:ℕ))), 0, 0], ![((-(4*J.a1*J.ep^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a1*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 4*J.a1*J.p2*J.r0^(4:ℕ) + 4*J.a1*J.r0^(3:ℕ)*J.r2 + 4*J.a2*J.ep^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a2*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.a2*J.p1*J.r0^(4:ℕ) + 4*J.a2*J.r0^(3:ℕ)*J.r1 + J.ep^(4:ℕ)*J.w0^(2:ℕ)*J.w1*J.w2 - 4*J.ep^(2:ℕ)*J.p1*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 8*J.ep^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0*J.w2 - 4*J.ep^(2:ℕ)*J.p12*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 8*J.ep^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w12 - 3*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w1*J.w2 + 2*J.ep^(2:ℕ)*J.r0*J.r1*J.w0*J.w2 + 2*J.ep^(2:ℕ)*J.r0*J.r2*J.w0*J.w1 - 4*J.p1*J.p2*J.r0^(4:ℕ) + 4*J.p1*J.r0^(3:ℕ)*J.r2 + 4*J.p12*J.r0^(4:ℕ) + 4*J.p2*J.r0^(3:ℕ)*J.r1 - 4*J.r0^(3:ℕ)*J.r12)/4) / ((J.ep) * (J.r0)^(2:ℕ))), ((-(4*J.a1*J.ep^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a1*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.a1*J.p1*J.r0^(4:ℕ) + 4*J.a1*J.r0^(3:ℕ)*J.r1 + 4*J.a2*J.ep^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a2*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 4*J.a2*J.p2*J.r0^(4:ℕ) + 4*J.a2*J.r0^(3:ℕ)*J.r2 + J.ep^(4:ℕ)*J.w0^(2:ℕ)*J.w2^(2:ℕ) - 4*J.ep^(2:ℕ)*J.p2^(2:ℕ)*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 16*J.ep^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0*J.w2 - 4*J.ep^(2:ℕ)*J.p22*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 4*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w22 - 3*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w2^(2:ℕ) + 4*J.ep^(2:ℕ)*J.r0*J.r2*J.w0*J.w2 - 4*J.p2^(2:ℕ)*J.r0^(4:ℕ) + 8*J.p2*J.r0^(3:ℕ)*J.r2 + 4*J.p22*J.r0^(4:ℕ) - 4*J.r0^(3:ℕ)*J.r22)/4) / ((J.ep) * (J.r0)^(2:ℕ))), 0, 0]]], 
    ![![![0, 0, ((-J.ep*(4*J.a1*J.p1*J.r0^(2:ℕ) + 4*J.a2*J.p2*J.r0^(2:ℕ) + J.ep^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p11*J.r0^(2:ℕ))/4) / ((J.r0)^(2:ℕ))), ((-J.ep*(4*J.a1*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w1 + 4*J.a2*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w2 + J.ep^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p11*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w11 + 2*J.r0*J.r1*J.w1)/4) / ((J.r0)^(2:ℕ)))], ![0, 0, ((-J.ep*(4*J.a1*J.p2*J.r0^(2:ℕ) + 4*J.a2*J.p1*J.r0^(2:ℕ) + J.ep^(2:ℕ)*J.w1*J.w2 - 4*J.p1*J.p2*J.r0^(2:ℕ) - 4*J.p12*J.r0^(2:ℕ))/4) / ((J.r0)^(2:ℕ))), ((-J.ep*(4*J.a1*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w2 + 4*J.a2*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w1 + J.ep^(2:ℕ)*J.w0*J.w1*J.w2 - 4*J.p1*J.p2*J.r0^(2:ℕ)*J.w0 - 6*J.p1*J.r0^(2:ℕ)*J.w2 - 4*J.p12*J.r0^(2:ℕ)*J.w0 - 2*J.p2*J.r0^(2:ℕ)*J.w1 - 2*J.r0^(2:ℕ)*J.w12 + 2*J.r0*J.r1*J.w2)/4) / ((J.r0)^(2:ℕ)))], ![((J.ep*(4*J.a1*J.p1*J.r0^(2:ℕ) + 4*J.a2*J.p2*J.r0^(2:ℕ) + J.ep^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p11*J.r0^(2:ℕ))/4) / ((J.r0)^(2:ℕ))), ((J.ep*(4*J.a1*J.p2*J.r0^(2:ℕ) + 4*J.a2*J.p1*J.r0^(2:ℕ) + J.ep^(2:ℕ)*J.w1*J.w2 - 4*J.p1*J.p2*J.r0^(2:ℕ) - 4*J.p12*J.r0^(2:ℕ))/4) / ((J.r0)^(2:ℕ))), 0, 0], ![((J.ep*(4*J.a1*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w1 + 4*J.a2*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w2 + J.ep^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p11*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w11 + 2*J.r0*J.r1*J.w1)/4) / ((J.r0)^(2:ℕ))), ((J.ep*(4*J.a1*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w2 + 4*J.a2*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w1 + J.ep^(2:ℕ)*J.w0*J.w1*J.w2 - 4*J.p1*J.p2*J.r0^(2:ℕ)*J.w0 - 6*J.p1*J.r0^(2:ℕ)*J.w2 - 4*J.p12*J.r0^(2:ℕ)*J.w0 - 2*J.p2*J.r0^(2:ℕ)*J.w1 - 2*J.r0^(2:ℕ)*J.w12 + 2*J.r0*J.r1*J.w2)/4) / ((J.r0)^(2:ℕ))), 0, 0]], ![![0, 0, ((-J.ep*(4*J.a1*J.p2*J.r0^(2:ℕ) + 4*J.a2*J.p1*J.r0^(2:ℕ) + J.ep^(2:ℕ)*J.w1*J.w2 - 4*J.p1*J.p2*J.r0^(2:ℕ) - 4*J.p12*J.r0^(2:ℕ))/4) / ((J.r0)^(2:ℕ))), ((-J.ep*(4*J.a1*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w2 + 4*J.a2*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w1 + J.ep^(2:ℕ)*J.w0*J.w1*J.w2 - 4*J.p1*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.p1*J.r0^(2:ℕ)*J.w2 - 4*J.p12*J.r0^(2:ℕ)*J.w0 - 6*J.p2*J.r0^(2:ℕ)*J.w1 - 2*J.r0^(2:ℕ)*J.w12 + 2*J.r0*J.r2*J.w1)/4) / ((J.r0)^(2:ℕ)))], ![0, 0, ((-J.ep*(4*J.a1*J.p1*J.r0^(2:ℕ) + 4*J.a2*J.p2*J.r0^(2:ℕ) + J.ep^(2:ℕ)*J.w2^(2:ℕ) - 4*J.p2^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p22*J.r0^(2:ℕ))/4) / ((J.r0)^(2:ℕ))), ((-J.ep*(4*J.a1*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w1 + 4*J.a2*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w2 + J.ep^(2:ℕ)*J.w0*J.w2^(2:ℕ) - 4*J.p2^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p2*J.r0^(2:ℕ)*J.w2 - 4*J.p22*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w22 + 2*J.r0*J.r2*J.w2)/4) / ((J.r0)^(2:ℕ)))], ![((J.ep*(4*J.a1*J.p2*J.r0^(2:ℕ) + 4*J.a2*J.p1*J.r0^(2:ℕ) + J.ep^(2:ℕ)*J.w1*J.w2 - 4*J.p1*J.p2*J.r0^(2:ℕ) - 4*J.p12*J.r0^(2:ℕ))/4) / ((J.r0)^(2:ℕ))), ((J.ep*(4*J.a1*J.p1*J.r0^(2:ℕ) + 4*J.a2*J.p2*J.r0^(2:ℕ) + J.ep^(2:ℕ)*J.w2^(2:ℕ) - 4*J.p2^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p22*J.r0^(2:ℕ))/4) / ((J.r0)^(2:ℕ))), 0, 0], ![((J.ep*(4*J.a1*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w2 + 4*J.a2*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w1 + J.ep^(2:ℕ)*J.w0*J.w1*J.w2 - 4*J.p1*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.p1*J.r0^(2:ℕ)*J.w2 - 4*J.p12*J.r0^(2:ℕ)*J.w0 - 6*J.p2*J.r0^(2:ℕ)*J.w1 - 2*J.r0^(2:ℕ)*J.w12 + 2*J.r0*J.r2*J.w1)/4) / ((J.r0)^(2:ℕ))), ((J.ep*(4*J.a1*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w1 + 4*J.a2*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w2 + J.ep^(2:ℕ)*J.w0*J.w2^(2:ℕ) - 4*J.p2^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p2*J.r0^(2:ℕ)*J.w2 - 4*J.p22*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w22 + 2*J.r0*J.r2*J.w2)/4) / ((J.r0)^(2:ℕ))), 0, 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, ((-J.ep*(2*J.p1*J.r0*J.w2 - 2*J.p2*J.r0*J.w1 - J.r1*J.w2 + J.r2*J.w1)/2) / ((J.r0))), 0, 0], ![((J.ep*(2*J.p1*J.r0*J.w2 - 2*J.p2*J.r0*J.w1 - J.r1*J.w2 + J.r2*J.w1)/2) / ((J.r0))), 0, 0, 0], ![0, 0, 0, ((-(J.ep^(2:ℕ)*J.w1^(2:ℕ) - J.ep^(2:ℕ)*J.w2^(2:ℕ) + 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p1*J.r0*J.r1 - 4*J.p2^(2:ℕ)*J.r0^(2:ℕ) + 4*J.p2*J.r0*J.r2)/4) / ((J.ea)))], ![0, 0, (((J.ep^(2:ℕ)*J.w1^(2:ℕ) - J.ep^(2:ℕ)*J.w2^(2:ℕ) + 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p1*J.r0*J.r1 - 4*J.p2^(2:ℕ)*J.r0^(2:ℕ) + 4*J.p2*J.r0*J.r2)/4) / ((J.ea))), 0]]], 
    ![![![0, 0, ((-J.ep*(4*J.a1*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w1 + 4*J.a2*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w2 + J.ep^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p11*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w11 + 2*J.r0*J.r1*J.w1)/4) / ((J.r0)^(2:ℕ))), ((-(4*J.a1*J.ep^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a1*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.a1*J.p1*J.r0^(4:ℕ) + 4*J.a1*J.r0^(3:ℕ)*J.r1 + 4*J.a2*J.ep^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a2*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 4*J.a2*J.p2*J.r0^(4:ℕ) + 4*J.a2*J.r0^(3:ℕ)*J.r2 + J.ep^(4:ℕ)*J.w0^(2:ℕ)*J.w1^(2:ℕ) - 4*J.ep^(2:ℕ)*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 16*J.ep^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.ep^(2:ℕ)*J.p11*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 4*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w11 - 3*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w1^(2:ℕ) + 4*J.ep^(2:ℕ)*J.r0*J.r1*J.w0*J.w1 - 4*J.p1^(2:ℕ)*J.r0^(4:ℕ) + 8*J.p1*J.r0^(3:ℕ)*J.r1 + 4*J.p11*J.r0^(4:ℕ) - 4*J.r0^(3:ℕ)*J.r11)/4) / ((J.ep) * (J.r0)^(2:ℕ)))], ![0, 0, ((-J.ep*(4*J.a1*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w2 + 4*J.a2*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w1 + J.ep^(2:ℕ)*J.w0*J.w1*J.w2 - 4*J.p1*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.p1*J.r0^(2:ℕ)*J.w2 - 4*J.p12*J.r0^(2:ℕ)*J.w0 - 6*J.p2*J.r0^(2:ℕ)*J.w1 - 2*J.r0^(2:ℕ)*J.w12 + 2*J.r0*J.r2*J.w1)/4) / ((J.r0)^(2:ℕ))), ((-(4*J.a1*J.ep^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a1*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 4*J.a1*J.p2*J.r0^(4:ℕ) + 4*J.a1*J.r0^(3:ℕ)*J.r2 + 4*J.a2*J.ep^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a2*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.a2*J.p1*J.r0^(4:ℕ) + 4*J.a2*J.r0^(3:ℕ)*J.r1 + J.ep^(4:ℕ)*J.w0^(2:ℕ)*J.w1*J.w2 - 4*J.ep^(2:ℕ)*J.p1*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 8*J.ep^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0*J.w2 - 4*J.ep^(2:ℕ)*J.p12*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 8*J.ep^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w12 - 3*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w1*J.w2 + 2*J.ep^(2:ℕ)*J.r0*J.r1*J.w0*J.w2 + 2*J.ep^(2:ℕ)*J.r0*J.r2*J.w0*J.w1 - 4*J.p1*J.p2*J.r0^(4:ℕ) + 4*J.p1*J.r0^(3:ℕ)*J.r2 + 4*J.p12*J.r0^(4:ℕ) + 4*J.p2*J.r0^(3:ℕ)*J.r1 - 4*J.r0^(3:ℕ)*J.r12)/4) / ((J.ep) * (J.r0)^(2:ℕ)))], ![((J.ep*(4*J.a1*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w1 + 4*J.a2*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w2 + J.ep^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p11*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w11 + 2*J.r0*J.r1*J.w1)/4) / ((J.r0)^(2:ℕ))), ((J.ep*(4*J.a1*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w2 + 4*J.a2*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w1 + J.ep^(2:ℕ)*J.w0*J.w1*J.w2 - 4*J.p1*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.p1*J.r0^(2:ℕ)*J.w2 - 4*J.p12*J.r0^(2:ℕ)*J.w0 - 6*J.p2*J.r0^(2:ℕ)*J.w1 - 2*J.r0^(2:ℕ)*J.w12 + 2*J.r0*J.r2*J.w1)/4) / ((J.r0)^(2:ℕ))), 0, 0], ![(((4*J.a1*J.ep^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a1*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.a1*J.p1*J.r0^(4:ℕ) + 4*J.a1*J.r0^(3:ℕ)*J.r1 + 4*J.a2*J.ep^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a2*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 4*J.a2*J.p2*J.r0^(4:ℕ) + 4*J.a2*J.r0^(3:ℕ)*J.r2 + J.ep^(4:ℕ)*J.w0^(2:ℕ)*J.w1^(2:ℕ) - 4*J.ep^(2:ℕ)*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 16*J.ep^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.ep^(2:ℕ)*J.p11*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 4*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w11 - 3*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w1^(2:ℕ) + 4*J.ep^(2:ℕ)*J.r0*J.r1*J.w0*J.w1 - 4*J.p1^(2:ℕ)*J.r0^(4:ℕ) + 8*J.p1*J.r0^(3:ℕ)*J.r1 + 4*J.p11*J.r0^(4:ℕ) - 4*J.r0^(3:ℕ)*J.r11)/4) / ((J.ep) * (J.r0)^(2:ℕ))), (((4*J.a1*J.ep^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a1*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 4*J.a1*J.p2*J.r0^(4:ℕ) + 4*J.a1*J.r0^(3:ℕ)*J.r2 + 4*J.a2*J.ep^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a2*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.a2*J.p1*J.r0^(4:ℕ) + 4*J.a2*J.r0^(3:ℕ)*J.r1 + J.ep^(4:ℕ)*J.w0^(2:ℕ)*J.w1*J.w2 - 4*J.ep^(2:ℕ)*J.p1*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 8*J.ep^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0*J.w2 - 4*J.ep^(2:ℕ)*J.p12*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 8*J.ep^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w12 - 3*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w1*J.w2 + 2*J.ep^(2:ℕ)*J.r0*J.r1*J.w0*J.w2 + 2*J.ep^(2:ℕ)*J.r0*J.r2*J.w0*J.w1 - 4*J.p1*J.p2*J.r0^(4:ℕ) + 4*J.p1*J.r0^(3:ℕ)*J.r2 + 4*J.p12*J.r0^(4:ℕ) + 4*J.p2*J.r0^(3:ℕ)*J.r1 - 4*J.r0^(3:ℕ)*J.r12)/4) / ((J.ep) * (J.r0)^(2:ℕ))), 0, 0]], ![![0, 0, ((-J.ep*(4*J.a1*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w2 + 4*J.a2*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w1 + J.ep^(2:ℕ)*J.w0*J.w1*J.w2 - 4*J.p1*J.p2*J.r0^(2:ℕ)*J.w0 - 6*J.p1*J.r0^(2:ℕ)*J.w2 - 4*J.p12*J.r0^(2:ℕ)*J.w0 - 2*J.p2*J.r0^(2:ℕ)*J.w1 - 2*J.r0^(2:ℕ)*J.w12 + 2*J.r0*J.r1*J.w2)/4) / ((J.r0)^(2:ℕ))), ((-(4*J.a1*J.ep^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a1*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 4*J.a1*J.p2*J.r0^(4:ℕ) + 4*J.a1*J.r0^(3:ℕ)*J.r2 + 4*J.a2*J.ep^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a2*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.a2*J.p1*J.r0^(4:ℕ) + 4*J.a2*J.r0^(3:ℕ)*J.r1 + J.ep^(4:ℕ)*J.w0^(2:ℕ)*J.w1*J.w2 - 4*J.ep^(2:ℕ)*J.p1*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 8*J.ep^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0*J.w2 - 4*J.ep^(2:ℕ)*J.p12*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 8*J.ep^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w12 - 3*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w1*J.w2 + 2*J.ep^(2:ℕ)*J.r0*J.r1*J.w0*J.w2 + 2*J.ep^(2:ℕ)*J.r0*J.r2*J.w0*J.w1 - 4*J.p1*J.p2*J.r0^(4:ℕ) + 4*J.p1*J.r0^(3:ℕ)*J.r2 + 4*J.p12*J.r0^(4:ℕ) + 4*J.p2*J.r0^(3:ℕ)*J.r1 - 4*J.r0^(3:ℕ)*J.r12)/4) / ((J.ep) * (J.r0)^(2:ℕ)))], ![0, 0, ((-J.ep*(4*J.a1*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w1 + 4*J.a2*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w2 + J.ep^(2:ℕ)*J.w0*J.w2^(2:ℕ) - 4*J.p2^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p2*J.r0^(2:ℕ)*J.w2 - 4*J.p22*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w22 + 2*J.r0*J.r2*J.w2)/4) / ((J.r0)^(2:ℕ))), ((-(4*J.a1*J.ep^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a1*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.a1*J.p1*J.r0^(4:ℕ) + 4*J.a1*J.r0^(3:ℕ)*J.r1 + 4*J.a2*J.ep^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a2*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 4*J.a2*J.p2*J.r0^(4:ℕ) + 4*J.a2*J.r0^(3:ℕ)*J.r2 + J.ep^(4:ℕ)*J.w0^(2:ℕ)*J.w2^(2:ℕ) - 4*J.ep^(2:ℕ)*J.p2^(2:ℕ)*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 16*J.ep^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0*J.w2 - 4*J.ep^(2:ℕ)*J.p22*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 4*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w22 - 3*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w2^(2:ℕ) + 4*J.ep^(2:ℕ)*J.r0*J.r2*J.w0*J.w2 - 4*J.p2^(2:ℕ)*J.r0^(4:ℕ) + 8*J.p2*J.r0^(3:ℕ)*J.r2 + 4*J.p22*J.r0^(4:ℕ) - 4*J.r0^(3:ℕ)*J.r22)/4) / ((J.ep) * (J.r0)^(2:ℕ)))], ![((J.ep*(4*J.a1*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w2 + 4*J.a2*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w1 + J.ep^(2:ℕ)*J.w0*J.w1*J.w2 - 4*J.p1*J.p2*J.r0^(2:ℕ)*J.w0 - 6*J.p1*J.r0^(2:ℕ)*J.w2 - 4*J.p12*J.r0^(2:ℕ)*J.w0 - 2*J.p2*J.r0^(2:ℕ)*J.w1 - 2*J.r0^(2:ℕ)*J.w12 + 2*J.r0*J.r1*J.w2)/4) / ((J.r0)^(2:ℕ))), ((J.ep*(4*J.a1*J.p1*J.r0^(2:ℕ)*J.w0 + 2*J.a1*J.r0^(2:ℕ)*J.w1 + 4*J.a2*J.p2*J.r0^(2:ℕ)*J.w0 + 2*J.a2*J.r0^(2:ℕ)*J.w2 + J.ep^(2:ℕ)*J.w0*J.w2^(2:ℕ) - 4*J.p2^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p2*J.r0^(2:ℕ)*J.w2 - 4*J.p22*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w22 + 2*J.r0*J.r2*J.w2)/4) / ((J.r0)^(2:ℕ))), 0, 0], ![(((4*J.a1*J.ep^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a1*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 4*J.a1*J.p2*J.r0^(4:ℕ) + 4*J.a1*J.r0^(3:ℕ)*J.r2 + 4*J.a2*J.ep^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a2*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.a2*J.p1*J.r0^(4:ℕ) + 4*J.a2*J.r0^(3:ℕ)*J.r1 + J.ep^(4:ℕ)*J.w0^(2:ℕ)*J.w1*J.w2 - 4*J.ep^(2:ℕ)*J.p1*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 8*J.ep^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0*J.w2 - 4*J.ep^(2:ℕ)*J.p12*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 8*J.ep^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w12 - 3*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w1*J.w2 + 2*J.ep^(2:ℕ)*J.r0*J.r1*J.w0*J.w2 + 2*J.ep^(2:ℕ)*J.r0*J.r2*J.w0*J.w1 - 4*J.p1*J.p2*J.r0^(4:ℕ) + 4*J.p1*J.r0^(3:ℕ)*J.r2 + 4*J.p12*J.r0^(4:ℕ) + 4*J.p2*J.r0^(3:ℕ)*J.r1 - 4*J.r0^(3:ℕ)*J.r12)/4) / ((J.ep) * (J.r0)^(2:ℕ))), (((4*J.a1*J.ep^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a1*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.a1*J.p1*J.r0^(4:ℕ) + 4*J.a1*J.r0^(3:ℕ)*J.r1 + 4*J.a2*J.ep^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) + 4*J.a2*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 4*J.a2*J.p2*J.r0^(4:ℕ) + 4*J.a2*J.r0^(3:ℕ)*J.r2 + J.ep^(4:ℕ)*J.w0^(2:ℕ)*J.w2^(2:ℕ) - 4*J.ep^(2:ℕ)*J.p2^(2:ℕ)*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 16*J.ep^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0*J.w2 - 4*J.ep^(2:ℕ)*J.p22*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 4*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w22 - 3*J.ep^(2:ℕ)*J.r0^(2:ℕ)*J.w2^(2:ℕ) + 4*J.ep^(2:ℕ)*J.r0*J.r2*J.w0*J.w2 - 4*J.p2^(2:ℕ)*J.r0^(4:ℕ) + 8*J.p2*J.r0^(3:ℕ)*J.r2 + 4*J.p22*J.r0^(4:ℕ) - 4*J.r0^(3:ℕ)*J.r22)/4) / ((J.ep) * (J.r0)^(2:ℕ))), 0, 0]], ![![0, ((J.ep*(2*J.p1*J.r0*J.w2 - 2*J.p2*J.r0*J.w1 - J.r1*J.w2 + J.r2*J.w1)/2) / ((J.r0))), 0, 0], ![((-J.ep*(2*J.p1*J.r0*J.w2 - 2*J.p2*J.r0*J.w1 - J.r1*J.w2 + J.r2*J.w1)/2) / ((J.r0))), 0, 0, 0], ![0, 0, 0, (((J.ep^(2:ℕ)*J.w1^(2:ℕ) - J.ep^(2:ℕ)*J.w2^(2:ℕ) + 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p1*J.r0*J.r1 - 4*J.p2^(2:ℕ)*J.r0^(2:ℕ) + 4*J.p2*J.r0*J.r2)/4) / ((J.ea)))], ![0, 0, ((-(J.ep^(2:ℕ)*J.w1^(2:ℕ) - J.ep^(2:ℕ)*J.w2^(2:ℕ) + 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p1*J.r0*J.r1 - 4*J.p2^(2:ℕ)*J.r0^(2:ℕ) + 4*J.p2*J.r0*J.r2)/4) / ((J.ea))), 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]]]]

noncomputable def WRUT (J : GJ) : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ :=
  ![![![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, ((J.a11 - J.a22) / ((J.ea))), 0, 0], ![((-J.a11 + J.a22) / ((J.ea))), 0, 0, 0], ![0, 0, 0, ((-J.ep*(2*J.p1*J.r0*J.w2 - 2*J.p2*J.r0*J.w1 - J.r1*J.w2 + J.r2*J.w1)/2) / ((J.r0)^(3:ℕ)))], ![0, 0, ((J.ep*(2*J.p1*J.r0*J.w2 - 2*J.p2*J.r0*J.w1 - J.r1*J.w2 + J.r2*J.w1)/2) / ((J.r0)^(3:ℕ))), 0]], ![![0, 0, (((2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a1*J.p1*J.r0^(3:ℕ) + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a2*J.p2*J.r0^(3:ℕ) - 8*J.ep^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w11 - J.ep^(2:ℕ)*J.r0*J.w1^(2:ℕ) + 2*J.ep^(2:ℕ)*J.r1*J.w0*J.w1 + 4*J.p1^(2:ℕ)*J.r0^(3:ℕ) + 4*J.p11*J.r0^(3:ℕ))/4) / ((J.ea) * (J.r0)^(3:ℕ))), ((-J.ep^(2:ℕ)*(J.a1*J.r0*J.w1 + J.a2*J.r0*J.w2 - 4*J.p1*J.r0*J.w1 - J.r0*J.w11 + J.r1*J.w1)/2) / ((J.ea) * (J.r0)^(3:ℕ)))], ![0, 0, ((-(2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a1*J.p2*J.r0^(3:ℕ) + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a2*J.p1*J.r0^(3:ℕ) - 6*J.ep^(2:ℕ)*J.p1*J.r0*J.w0*J.w2 - 2*J.ep^(2:ℕ)*J.p2*J.r0*J.w0*J.w1 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w12 - J.ep^(2:ℕ)*J.r0*J.w1*J.w2 + 2*J.ep^(2:ℕ)*J.r1*J.w0*J.w2 + 4*J.p1*J.p2*J.r0^(3:ℕ) + 4*J.p12*J.r0^(3:ℕ))/4) / ((J.ea) * (J.r0)^(3:ℕ))), ((J.ep^(2:ℕ)*(J.a1*J.r0*J.w2 + J.a2*J.r0*J.w1 - 3*J.p1*J.r0*J.w2 - J.p2*J.r0*J.w1 - J.r0*J.w12 + J.r1*J.w2)/2) / ((J.ea) * (J.r0)^(3:ℕ)))], ![((-(2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a1*J.p1*J.r0^(3:ℕ) + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a2*J.p2*J.r0^(3:ℕ) - 8*J.ep^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w11 - J.ep^(2:ℕ)*J.r0*J.w1^(2:ℕ) + 2*J.ep^(2:ℕ)*J.r1*J.w0*J.w1 + 4*J.p1^(2:ℕ)*J.r0^(3:ℕ) + 4*J.p11*J.r0^(3:ℕ))/4) / ((J.ea) * (J.r0)^(3:ℕ))), (((2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a1*J.p2*J.r0^(3:ℕ) + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a2*J.p1*J.r0^(3:ℕ) - 6*J.ep^(2:ℕ)*J.p1*J.r0*J.w0*J.w2 - 2*J.ep^(2:ℕ)*J.p2*J.r0*J.w0*J.w1 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w12 - J.ep^(2:ℕ)*J.r0*J.w1*J.w2 + 2*J.ep^(2:ℕ)*J.r1*J.w0*J.w2 + 4*J.p1*J.p2*J.r0^(3:ℕ) + 4*J.p12*J.r0^(3:ℕ))/4) / ((J.ea) * (J.r0)^(3:ℕ))), 0, 0], ![((J.ep^(2:ℕ)*(J.a1*J.r0*J.w1 + J.a2*J.r0*J.w2 - 4*J.p1*J.r0*J.w1 - J.r0*J.w11 + J.r1*J.w1)/2) / ((J.ea) * (J.r0)^(3:ℕ))), ((-J.ep^(2:ℕ)*(J.a1*J.r0*J.w2 + J.a2*J.r0*J.w1 - 3*J.p1*J.r0*J.w2 - J.p2*J.r0*J.w1 - J.r0*J.w12 + J.r1*J.w2)/2) / ((J.ea) * (J.r0)^(3:ℕ))), 0, 0]], ![![0, 0, (((J.a1*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w1 - 4*J.a1*J.p1*J.r0^(3:ℕ)*J.w0 - J.a1*J.r0^(3:ℕ)*J.w1 + 2*J.a1*J.r0^(2:ℕ)*J.r1*J.w0 + J.a2*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w2 - 4*J.a2*J.p2*J.r0^(3:ℕ)*J.w0 - J.a2*J.r0^(3:ℕ)*J.w2 + 2*J.a2*J.r0^(2:ℕ)*J.r2*J.w0 - 4*J.ep^(2:ℕ)*J.p1*J.r0*J.w0^(2:ℕ)*J.w1 - J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w11 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1^(2:ℕ) + J.ep^(2:ℕ)*J.r1*J.w0^(2:ℕ)*J.w1 + 4*J.p1*J.r0^(3:ℕ)*J.w1 + 4*J.p1*J.r0^(2:ℕ)*J.r1*J.w0 + 4*J.p11*J.r0^(3:ℕ)*J.w0 + J.r0^(3:ℕ)*J.w11 - J.r0^(2:ℕ)*J.r1*J.w1 - 2*J.r0^(2:ℕ)*J.r11*J.w0)/2) / ((J.ea) * (J.r0)^(3:ℕ))), ((-(2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a1*J.p1*J.r0^(3:ℕ) + 4*J.a1*J.r0^(2:ℕ)*J.r1 + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a2*J.p2*J.r0^(3:ℕ) + 4*J.a2*J.r0^(2:ℕ)*J.r2 - 8*J.ep^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w11 - 3*J.ep^(2:ℕ)*J.r0*J.w1^(2:ℕ) + 2*J.ep^(2:ℕ)*J.r1*J.w0*J.w1 - 4*J.p1^(2:ℕ)*J.r0^(3:ℕ) + 8*J.p1*J.r0^(2:ℕ)*J.r1 + 4*J.p11*J.r0^(3:ℕ) - 4*J.r0^(2:ℕ)*J.r11)/4) / ((J.ea) * (J.r0)^(3:ℕ)))], ![0, 0, ((-(J.a1*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w2 - 4*J.a1*J.p2*J.r0^(3:ℕ)*J.w0 - J.a1*J.r0^(3:ℕ)*J.w2 + 2*J.a1*J.r0^(2:ℕ)*J.r2*J.w0 + J.a2*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w1 - 4*J.a2*J.p1*J.r0^(3:ℕ)*J.w0 - J.a2*J.r0^(3:ℕ)*J.w1 + 2*J.a2*J.r0^(2:ℕ)*J.r1*J.w0 - 3*J.ep^(2:ℕ)*J.p1*J.r0*J.w0^(2:ℕ)*J.w2 - J.ep^(2:ℕ)*J.p2*J.r0*J.w0^(2:ℕ)*J.w1 - J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w12 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1*J.w2 + J.ep^(2:ℕ)*J.r1*J.w0^(2:ℕ)*J.w2 + J.p1*J.r0^(3:ℕ)*J.w2 + 2*J.p1*J.r0^(2:ℕ)*J.r2*J.w0 + 4*J.p12*J.r0^(3:ℕ)*J.w0 + 3*J.p2*J.r0^(3:ℕ)*J.w1 + 2*J.p2*J.r0^(2:ℕ)*J.r1*J.w0 + J.r0^(3:ℕ)*J.w12 - 2*J.r0^(2:ℕ)*J.r12*J.w0 - J.r0^(2:ℕ)*J.r2*J.w1)/2) / ((J.ea) * (J.r0)^(3:ℕ))), (((2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a1*J.p2*J.r0^(3:ℕ) + 4*J.a1*J.r0^(2:ℕ)*J.r2 + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a2*J.p1*J.r0^(3:ℕ) + 4*J.a2*J.r0^(2:ℕ)*J.r1 - 6*J.ep^(2:ℕ)*J.p1*J.r0*J.w0*J.w2 - 2*J.ep^(2:ℕ)*J.p2*J.r0*J.w0*J.w1 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w12 - 3*J.ep^(2:ℕ)*J.r0*J.w1*J.w2 + 2*J.ep^(2:ℕ)*J.r1*J.w0*J.w2 - 4*J.p1*J.p2*J.r0^(3:ℕ) + 4*J.p1*J.r0^(2:ℕ)*J.r2 + 4*J.p12*J.r0^(3:ℕ) + 4*J.p2*J.r0^(2:ℕ)*J.r1 - 4*J.r0^(2:ℕ)*J.r12)/4) / ((J.ea) * (J.r0)^(3:ℕ)))], ![((-(J.a1*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w1 - 4*J.a1*J.p1*J.r0^(3:ℕ)*J.w0 - J.a1*J.r0^(3:ℕ)*J.w1 + 2*J.a1*J.r0^(2:ℕ)*J.r1*J.w0 + J.a2*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w2 - 4*J.a2*J.p2*J.r0^(3:ℕ)*J.w0 - J.a2*J.r0^(3:ℕ)*J.w2 + 2*J.a2*J.r0^(2:ℕ)*J.r2*J.w0 - 4*J.ep^(2:ℕ)*J.p1*J.r0*J.w0^(2:ℕ)*J.w1 - J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w11 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1^(2:ℕ) + J.ep^(2:ℕ)*J.r1*J.w0^(2:ℕ)*J.w1 + 4*J.p1*J.r0^(3:ℕ)*J.w1 + 4*J.p1*J.r0^(2:ℕ)*J.r1*J.w0 + 4*J.p11*J.r0^(3:ℕ)*J.w0 + J.r0^(3:ℕ)*J.w11 - J.r0^(2:ℕ)*J.r1*J.w1 - 2*J.r0^(2:ℕ)*J.r11*J.w0)/2) / ((J.ea) * (J.r0)^(3:ℕ))), (((J.a1*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w2 - 4*J.a1*J.p2*J.r0^(3:ℕ)*J.w0 - J.a1*J.r0^(3:ℕ)*J.w2 + 2*J.a1*J.r0^(2:ℕ)*J.r2*J.w0 + J.a2*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w1 - 4*J.a2*J.p1*J.r0^(3:ℕ)*J.w0 - J.a2*J.r0^(3:ℕ)*J.w1 + 2*J.a2*J.r0^(2:ℕ)*J.r1*J.w0 - 3*J.ep^(2:ℕ)*J.p1*J.r0*J.w0^(2:ℕ)*J.w2 - J.ep^(2:ℕ)*J.p2*J.r0*J.w0^(2:ℕ)*J.w1 - J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w12 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1*J.w2 + J.ep^(2:ℕ)*J.r1*J.w0^(2:ℕ)*J.w2 + J.p1*J.r0^(3:ℕ)*J.w2 + 2*J.p1*J.r0^(2:ℕ)*J.r2*J.w0 + 4*J.p12*J.r0^(3:ℕ)*J.w0 + 3*J.p2*J.r0^(3:ℕ)*J.w1 + 2*J.p2*J.r0^(2:ℕ)*J.r1*J.w0 + J.r0^(3:ℕ)*J.w12 - 2*J.r0^(2:ℕ)*J.r12*J.w0 - J.r0^(2:ℕ)*J.r2*J.w1)/2) / ((J.ea) * (J.r0)^(3:ℕ))), 0, 0], ![(((2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a1*J.p1*J.r0^(3:ℕ) + 4*J.a1*J.r0^(2:ℕ)*J.r1 + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a2*J.p2*J.r0^(3:ℕ) + 4*J.a2*J.r0^(2:ℕ)*J.r2 - 8*J.ep^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w11 - 3*J.ep^(2:ℕ)*J.r0*J.w1^(2:ℕ) + 2*J.ep^(2:ℕ)*J.r1*J.w0*J.w1 - 4*J.p1^(2:ℕ)*J.r0^(3:ℕ) + 8*J.p1*J.r0^(2:ℕ)*J.r1 + 4*J.p11*J.r0^(3:ℕ) - 4*J.r0^(2:ℕ)*J.r11)/4) / ((J.ea) * (J.r0)^(3:ℕ))), ((-(2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a1*J.p2*J.r0^(3:ℕ) + 4*J.a1*J.r0^(2:ℕ)*J.r2 + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a2*J.p1*J.r0^(3:ℕ) + 4*J.a2*J.r0^(2:ℕ)*J.r1 - 6*J.ep^(2:ℕ)*J.p1*J.r0*J.w0*J.w2 - 2*J.ep^(2:ℕ)*J.p2*J.r0*J.w0*J.w1 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w12 - 3*J.ep^(2:ℕ)*J.r0*J.w1*J.w2 + 2*J.ep^(2:ℕ)*J.r1*J.w0*J.w2 - 4*J.p1*J.p2*J.r0^(3:ℕ) + 4*J.p1*J.r0^(2:ℕ)*J.r2 + 4*J.p12*J.r0^(3:ℕ) + 4*J.p2*J.r0^(2:ℕ)*J.r1 - 4*J.r0^(2:ℕ)*J.r12)/4) / ((J.ea) * (J.r0)^(3:ℕ))), 0, 0]]], 
    ![![![0, ((-J.a11 + J.a22) / ((J.ea))), 0, 0], ![((J.a11 - J.a22) / ((J.ea))), 0, 0, 0], ![0, 0, 0, ((J.ep*(2*J.p1*J.r0*J.w2 - 2*J.p2*J.r0*J.w1 - J.r1*J.w2 + J.r2*J.w1)/2) / ((J.r0)^(3:ℕ)))], ![0, 0, ((-J.ep*(2*J.p1*J.r0*J.w2 - 2*J.p2*J.r0*J.w1 - J.r1*J.w2 + J.r2*J.w1)/2) / ((J.r0)^(3:ℕ))), 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, 0, (((2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a1*J.p2*J.r0^(3:ℕ) + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a2*J.p1*J.r0^(3:ℕ) - 2*J.ep^(2:ℕ)*J.p1*J.r0*J.w0*J.w2 - 6*J.ep^(2:ℕ)*J.p2*J.r0*J.w0*J.w1 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w12 - J.ep^(2:ℕ)*J.r0*J.w1*J.w2 + 2*J.ep^(2:ℕ)*J.r2*J.w0*J.w1 + 4*J.p1*J.p2*J.r0^(3:ℕ) + 4*J.p12*J.r0^(3:ℕ))/4) / ((J.ea) * (J.r0)^(3:ℕ))), ((-J.ep^(2:ℕ)*(J.a1*J.r0*J.w2 + J.a2*J.r0*J.w1 - J.p1*J.r0*J.w2 - 3*J.p2*J.r0*J.w1 - J.r0*J.w12 + J.r2*J.w1)/2) / ((J.ea) * (J.r0)^(3:ℕ)))], ![0, 0, ((-(2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a1*J.p1*J.r0^(3:ℕ) + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a2*J.p2*J.r0^(3:ℕ) - 8*J.ep^(2:ℕ)*J.p2*J.r0*J.w0*J.w2 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w22 - J.ep^(2:ℕ)*J.r0*J.w2^(2:ℕ) + 2*J.ep^(2:ℕ)*J.r2*J.w0*J.w2 + 4*J.p2^(2:ℕ)*J.r0^(3:ℕ) + 4*J.p22*J.r0^(3:ℕ))/4) / ((J.ea) * (J.r0)^(3:ℕ))), ((J.ep^(2:ℕ)*(J.a1*J.r0*J.w1 + J.a2*J.r0*J.w2 - 4*J.p2*J.r0*J.w2 - J.r0*J.w22 + J.r2*J.w2)/2) / ((J.ea) * (J.r0)^(3:ℕ)))], ![((-(2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a1*J.p2*J.r0^(3:ℕ) + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a2*J.p1*J.r0^(3:ℕ) - 2*J.ep^(2:ℕ)*J.p1*J.r0*J.w0*J.w2 - 6*J.ep^(2:ℕ)*J.p2*J.r0*J.w0*J.w1 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w12 - J.ep^(2:ℕ)*J.r0*J.w1*J.w2 + 2*J.ep^(2:ℕ)*J.r2*J.w0*J.w1 + 4*J.p1*J.p2*J.r0^(3:ℕ) + 4*J.p12*J.r0^(3:ℕ))/4) / ((J.ea) * (J.r0)^(3:ℕ))), (((2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a1*J.p1*J.r0^(3:ℕ) + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a2*J.p2*J.r0^(3:ℕ) - 8*J.ep^(2:ℕ)*J.p2*J.r0*J.w0*J.w2 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w22 - J.ep^(2:ℕ)*J.r0*J.w2^(2:ℕ) + 2*J.ep^(2:ℕ)*J.r2*J.w0*J.w2 + 4*J.p2^(2:ℕ)*J.r0^(3:ℕ) + 4*J.p22*J.r0^(3:ℕ))/4) / ((J.ea) * (J.r0)^(3:ℕ))), 0, 0], ![((J.ep^(2:ℕ)*(J.a1*J.r0*J.w2 + J.a2*J.r0*J.w1 - J.p1*J.r0*J.w2 - 3*J.p2*J.r0*J.w1 - J.r0*J.w12 + J.r2*J.w1)/2) / ((J.ea) * (J.r0)^(3:ℕ))), ((-J.ep^(2:ℕ)*(J.a1*J.r0*J.w1 + J.a2*J.r0*J.w2 - 4*J.p2*J.r0*J.w2 - J.r0*J.w22 + J.r2*J.w2)/2) / ((J.ea) * (J.r0)^(3:ℕ))), 0, 0]], ![![0, 0, (((J.a1*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w2 - 4*J.a1*J.p2*J.r0^(3:ℕ)*J.w0 - J.a1*J.r0^(3:ℕ)*J.w2 + 2*J.a1*J.r0^(2:ℕ)*J.r2*J.w0 + J.a2*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w1 - 4*J.a2*J.p1*J.r0^(3:ℕ)*J.w0 - J.a2*J.r0^(3:ℕ)*J.w1 + 2*J.a2*J.r0^(2:ℕ)*J.r1*J.w0 - J.ep^(2:ℕ)*J.p1*J.r0*J.w0^(2:ℕ)*J.w2 - 3*J.ep^(2:ℕ)*J.p2*J.r0*J.w0^(2:ℕ)*J.w1 - J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w12 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1*J.w2 + J.ep^(2:ℕ)*J.r2*J.w0^(2:ℕ)*J.w1 + 3*J.p1*J.r0^(3:ℕ)*J.w2 + 2*J.p1*J.r0^(2:ℕ)*J.r2*J.w0 + 4*J.p12*J.r0^(3:ℕ)*J.w0 + J.p2*J.r0^(3:ℕ)*J.w1 + 2*J.p2*J.r0^(2:ℕ)*J.r1*J.w0 + J.r0^(3:ℕ)*J.w12 - J.r0^(2:ℕ)*J.r1*J.w2 - 2*J.r0^(2:ℕ)*J.r12*J.w0)/2) / ((J.ea) * (J.r0)^(3:ℕ))), ((-(2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a1*J.p2*J.r0^(3:ℕ) + 4*J.a1*J.r0^(2:ℕ)*J.r2 + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a2*J.p1*J.r0^(3:ℕ) + 4*J.a2*J.r0^(2:ℕ)*J.r1 - 2*J.ep^(2:ℕ)*J.p1*J.r0*J.w0*J.w2 - 6*J.ep^(2:ℕ)*J.p2*J.r0*J.w0*J.w1 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w12 - 3*J.ep^(2:ℕ)*J.r0*J.w1*J.w2 + 2*J.ep^(2:ℕ)*J.r2*J.w0*J.w1 - 4*J.p1*J.p2*J.r0^(3:ℕ) + 4*J.p1*J.r0^(2:ℕ)*J.r2 + 4*J.p12*J.r0^(3:ℕ) + 4*J.p2*J.r0^(2:ℕ)*J.r1 - 4*J.r0^(2:ℕ)*J.r12)/4) / ((J.ea) * (J.r0)^(3:ℕ)))], ![0, 0, ((-(J.a1*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w1 - 4*J.a1*J.p1*J.r0^(3:ℕ)*J.w0 - J.a1*J.r0^(3:ℕ)*J.w1 + 2*J.a1*J.r0^(2:ℕ)*J.r1*J.w0 + J.a2*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w2 - 4*J.a2*J.p2*J.r0^(3:ℕ)*J.w0 - J.a2*J.r0^(3:ℕ)*J.w2 + 2*J.a2*J.r0^(2:ℕ)*J.r2*J.w0 - 4*J.ep^(2:ℕ)*J.p2*J.r0*J.w0^(2:ℕ)*J.w2 - J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w22 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w2^(2:ℕ) + J.ep^(2:ℕ)*J.r2*J.w0^(2:ℕ)*J.w2 + 4*J.p2*J.r0^(3:ℕ)*J.w2 + 4*J.p2*J.r0^(2:ℕ)*J.r2*J.w0 + 4*J.p22*J.r0^(3:ℕ)*J.w0 + J.r0^(3:ℕ)*J.w22 - J.r0^(2:ℕ)*J.r2*J.w2 - 2*J.r0^(2:ℕ)*J.r22*J.w0)/2) / ((J.ea) * (J.r0)^(3:ℕ))), (((2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a1*J.p1*J.r0^(3:ℕ) + 4*J.a1*J.r0^(2:ℕ)*J.r1 + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a2*J.p2*J.r0^(3:ℕ) + 4*J.a2*J.r0^(2:ℕ)*J.r2 - 8*J.ep^(2:ℕ)*J.p2*J.r0*J.w0*J.w2 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w22 - 3*J.ep^(2:ℕ)*J.r0*J.w2^(2:ℕ) + 2*J.ep^(2:ℕ)*J.r2*J.w0*J.w2 - 4*J.p2^(2:ℕ)*J.r0^(3:ℕ) + 8*J.p2*J.r0^(2:ℕ)*J.r2 + 4*J.p22*J.r0^(3:ℕ) - 4*J.r0^(2:ℕ)*J.r22)/4) / ((J.ea) * (J.r0)^(3:ℕ)))], ![((-(J.a1*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w2 - 4*J.a1*J.p2*J.r0^(3:ℕ)*J.w0 - J.a1*J.r0^(3:ℕ)*J.w2 + 2*J.a1*J.r0^(2:ℕ)*J.r2*J.w0 + J.a2*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w1 - 4*J.a2*J.p1*J.r0^(3:ℕ)*J.w0 - J.a2*J.r0^(3:ℕ)*J.w1 + 2*J.a2*J.r0^(2:ℕ)*J.r1*J.w0 - J.ep^(2:ℕ)*J.p1*J.r0*J.w0^(2:ℕ)*J.w2 - 3*J.ep^(2:ℕ)*J.p2*J.r0*J.w0^(2:ℕ)*J.w1 - J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w12 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1*J.w2 + J.ep^(2:ℕ)*J.r2*J.w0^(2:ℕ)*J.w1 + 3*J.p1*J.r0^(3:ℕ)*J.w2 + 2*J.p1*J.r0^(2:ℕ)*J.r2*J.w0 + 4*J.p12*J.r0^(3:ℕ)*J.w0 + J.p2*J.r0^(3:ℕ)*J.w1 + 2*J.p2*J.r0^(2:ℕ)*J.r1*J.w0 + J.r0^(3:ℕ)*J.w12 - J.r0^(2:ℕ)*J.r1*J.w2 - 2*J.r0^(2:ℕ)*J.r12*J.w0)/2) / ((J.ea) * (J.r0)^(3:ℕ))), (((J.a1*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w1 - 4*J.a1*J.p1*J.r0^(3:ℕ)*J.w0 - J.a1*J.r0^(3:ℕ)*J.w1 + 2*J.a1*J.r0^(2:ℕ)*J.r1*J.w0 + J.a2*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w2 - 4*J.a2*J.p2*J.r0^(3:ℕ)*J.w0 - J.a2*J.r0^(3:ℕ)*J.w2 + 2*J.a2*J.r0^(2:ℕ)*J.r2*J.w0 - 4*J.ep^(2:ℕ)*J.p2*J.r0*J.w0^(2:ℕ)*J.w2 - J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w22 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w2^(2:ℕ) + J.ep^(2:ℕ)*J.r2*J.w0^(2:ℕ)*J.w2 + 4*J.p2*J.r0^(3:ℕ)*J.w2 + 4*J.p2*J.r0^(2:ℕ)*J.r2*J.w0 + 4*J.p22*J.r0^(3:ℕ)*J.w0 + J.r0^(3:ℕ)*J.w22 - J.r0^(2:ℕ)*J.r2*J.w2 - 2*J.r0^(2:ℕ)*J.r22*J.w0)/2) / ((J.ea) * (J.r0)^(3:ℕ))), 0, 0], ![(((2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a1*J.p2*J.r0^(3:ℕ) + 4*J.a1*J.r0^(2:ℕ)*J.r2 + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a2*J.p1*J.r0^(3:ℕ) + 4*J.a2*J.r0^(2:ℕ)*J.r1 - 2*J.ep^(2:ℕ)*J.p1*J.r0*J.w0*J.w2 - 6*J.ep^(2:ℕ)*J.p2*J.r0*J.w0*J.w1 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w12 - 3*J.ep^(2:ℕ)*J.r0*J.w1*J.w2 + 2*J.ep^(2:ℕ)*J.r2*J.w0*J.w1 - 4*J.p1*J.p2*J.r0^(3:ℕ) + 4*J.p1*J.r0^(2:ℕ)*J.r2 + 4*J.p12*J.r0^(3:ℕ) + 4*J.p2*J.r0^(2:ℕ)*J.r1 - 4*J.r0^(2:ℕ)*J.r12)/4) / ((J.ea) * (J.r0)^(3:ℕ))), ((-(2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a1*J.p1*J.r0^(3:ℕ) + 4*J.a1*J.r0^(2:ℕ)*J.r1 + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a2*J.p2*J.r0^(3:ℕ) + 4*J.a2*J.r0^(2:ℕ)*J.r2 - 8*J.ep^(2:ℕ)*J.p2*J.r0*J.w0*J.w2 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w22 - 3*J.ep^(2:ℕ)*J.r0*J.w2^(2:ℕ) + 2*J.ep^(2:ℕ)*J.r2*J.w0*J.w2 - 4*J.p2^(2:ℕ)*J.r0^(3:ℕ) + 8*J.p2*J.r0^(2:ℕ)*J.r2 + 4*J.p22*J.r0^(3:ℕ) - 4*J.r0^(2:ℕ)*J.r22)/4) / ((J.ea) * (J.r0)^(3:ℕ))), 0, 0]]], 
    ![![![0, 0, ((-(2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a1*J.p1*J.r0^(3:ℕ) + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a2*J.p2*J.r0^(3:ℕ) - 8*J.ep^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w11 - J.ep^(2:ℕ)*J.r0*J.w1^(2:ℕ) + 2*J.ep^(2:ℕ)*J.r1*J.w0*J.w1 + 4*J.p1^(2:ℕ)*J.r0^(3:ℕ) + 4*J.p11*J.r0^(3:ℕ))/4) / ((J.ea) * (J.r0)^(3:ℕ))), ((J.ep^(2:ℕ)*(J.a1*J.r0*J.w1 + J.a2*J.r0*J.w2 - 4*J.p1*J.r0*J.w1 - J.r0*J.w11 + J.r1*J.w1)/2) / ((J.ea) * (J.r0)^(3:ℕ)))], ![0, 0, (((2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a1*J.p2*J.r0^(3:ℕ) + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a2*J.p1*J.r0^(3:ℕ) - 6*J.ep^(2:ℕ)*J.p1*J.r0*J.w0*J.w2 - 2*J.ep^(2:ℕ)*J.p2*J.r0*J.w0*J.w1 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w12 - J.ep^(2:ℕ)*J.r0*J.w1*J.w2 + 2*J.ep^(2:ℕ)*J.r1*J.w0*J.w2 + 4*J.p1*J.p2*J.r0^(3:ℕ) + 4*J.p12*J.r0^(3:ℕ))/4) / ((J.ea) * (J.r0)^(3:ℕ))), ((-J.ep^(2:ℕ)*(J.a1*J.r0*J.w2 + J.a2*J.r0*J.w1 - 3*J.p1*J.r0*J.w2 - J.p2*J.r0*J.w1 - J.r0*J.w12 + J.r1*J.w2)/2) / ((J.ea) * (J.r0)^(3:ℕ)))], ![(((2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a1*J.p1*J.r0^(3:ℕ) + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a2*J.p2*J.r0^(3:ℕ) - 8*J.ep^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w11 - J.ep^(2:ℕ)*J.r0*J.w1^(2:ℕ) + 2*J.ep^(2:ℕ)*J.r1*J.w0*J.w1 + 4*J.p1^(2:ℕ)*J.r0^(3:ℕ) + 4*J.p11*J.r0^(3:ℕ))/4) / ((J.ea) * (J.r0)^(3:ℕ))), ((-(2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a1*J.p2*J.r0^(3:ℕ) + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a2*J.p1*J.r0^(3:ℕ) - 6*J.ep^(2:ℕ)*J.p1*J.r0*J.w0*J.w2 - 2*J.ep^(2:ℕ)*J.p2*J.r0*J.w0*J.w1 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w12 - J.ep^(2:ℕ)*J.r0*J.w1*J.w2 + 2*J.ep^(2:ℕ)*J.r1*J.w0*J.w2 + 4*J.p1*J.p2*J.r0^(3:ℕ) + 4*J.p12*J.r0^(3:ℕ))/4) / ((J.ea) * (J.r0)^(3:ℕ))), 0, 0], ![((-J.ep^(2:ℕ)*(J.a1*J.r0*J.w1 + J.a2*J.r0*J.w2 - 4*J.p1*J.r0*J.w1 - J.r0*J.w11 + J.r1*J.w1)/2) / ((J.ea) * (J.r0)^(3:ℕ))), ((J.ep^(2:ℕ)*(J.a1*J.r0*J.w2 + J.a2*J.r0*J.w1 - 3*J.p1*J.r0*J.w2 - J.p2*J.r0*J.w1 - J.r0*J.w12 + J.r1*J.w2)/2) / ((J.ea) * (J.r0)^(3:ℕ))), 0, 0]], ![![0, 0, ((-(2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a1*J.p2*J.r0^(3:ℕ) + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a2*J.p1*J.r0^(3:ℕ) - 2*J.ep^(2:ℕ)*J.p1*J.r0*J.w0*J.w2 - 6*J.ep^(2:ℕ)*J.p2*J.r0*J.w0*J.w1 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w12 - J.ep^(2:ℕ)*J.r0*J.w1*J.w2 + 2*J.ep^(2:ℕ)*J.r2*J.w0*J.w1 + 4*J.p1*J.p2*J.r0^(3:ℕ) + 4*J.p12*J.r0^(3:ℕ))/4) / ((J.ea) * (J.r0)^(3:ℕ))), ((J.ep^(2:ℕ)*(J.a1*J.r0*J.w2 + J.a2*J.r0*J.w1 - J.p1*J.r0*J.w2 - 3*J.p2*J.r0*J.w1 - J.r0*J.w12 + J.r2*J.w1)/2) / ((J.ea) * (J.r0)^(3:ℕ)))], ![0, 0, (((2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a1*J.p1*J.r0^(3:ℕ) + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a2*J.p2*J.r0^(3:ℕ) - 8*J.ep^(2:ℕ)*J.p2*J.r0*J.w0*J.w2 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w22 - J.ep^(2:ℕ)*J.r0*J.w2^(2:ℕ) + 2*J.ep^(2:ℕ)*J.r2*J.w0*J.w2 + 4*J.p2^(2:ℕ)*J.r0^(3:ℕ) + 4*J.p22*J.r0^(3:ℕ))/4) / ((J.ea) * (J.r0)^(3:ℕ))), ((-J.ep^(2:ℕ)*(J.a1*J.r0*J.w1 + J.a2*J.r0*J.w2 - 4*J.p2*J.r0*J.w2 - J.r0*J.w22 + J.r2*J.w2)/2) / ((J.ea) * (J.r0)^(3:ℕ)))], ![(((2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a1*J.p2*J.r0^(3:ℕ) + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a2*J.p1*J.r0^(3:ℕ) - 2*J.ep^(2:ℕ)*J.p1*J.r0*J.w0*J.w2 - 6*J.ep^(2:ℕ)*J.p2*J.r0*J.w0*J.w1 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w12 - J.ep^(2:ℕ)*J.r0*J.w1*J.w2 + 2*J.ep^(2:ℕ)*J.r2*J.w0*J.w1 + 4*J.p1*J.p2*J.r0^(3:ℕ) + 4*J.p12*J.r0^(3:ℕ))/4) / ((J.ea) * (J.r0)^(3:ℕ))), ((-(2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a1*J.p1*J.r0^(3:ℕ) + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a2*J.p2*J.r0^(3:ℕ) - 8*J.ep^(2:ℕ)*J.p2*J.r0*J.w0*J.w2 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w22 - J.ep^(2:ℕ)*J.r0*J.w2^(2:ℕ) + 2*J.ep^(2:ℕ)*J.r2*J.w0*J.w2 + 4*J.p2^(2:ℕ)*J.r0^(3:ℕ) + 4*J.p22*J.r0^(3:ℕ))/4) / ((J.ea) * (J.r0)^(3:ℕ))), 0, 0], ![((-J.ep^(2:ℕ)*(J.a1*J.r0*J.w2 + J.a2*J.r0*J.w1 - J.p1*J.r0*J.w2 - 3*J.p2*J.r0*J.w1 - J.r0*J.w12 + J.r2*J.w1)/2) / ((J.ea) * (J.r0)^(3:ℕ))), ((J.ep^(2:ℕ)*(J.a1*J.r0*J.w1 + J.a2*J.r0*J.w2 - 4*J.p2*J.r0*J.w2 - J.r0*J.w22 + J.r2*J.w2)/2) / ((J.ea) * (J.r0)^(3:ℕ))), 0, 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]], ![![0, ((J.ep*(2*J.p1*J.r0*J.w2 - 2*J.p2*J.r0*J.w1 - J.r1*J.w2 + J.r2*J.w1)/2) / ((J.r0) * (J.ea)^(2:ℕ))), 0, 0], ![((-J.ep*(2*J.p1*J.r0*J.w2 - 2*J.p2*J.r0*J.w1 - J.r1*J.w2 + J.r2*J.w1)/2) / ((J.r0) * (J.ea)^(2:ℕ))), 0, 0, 0], ![0, 0, 0, ((-(J.ep^(2:ℕ)*J.w1^(2:ℕ) - J.ep^(2:ℕ)*J.w2^(2:ℕ) + 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p1*J.r0*J.r1 - 4*J.p2^(2:ℕ)*J.r0^(2:ℕ) + 4*J.p2*J.r0*J.r2)/4) / ((J.ea) * (J.r0)^(2:ℕ)))], ![0, 0, (((J.ep^(2:ℕ)*J.w1^(2:ℕ) - J.ep^(2:ℕ)*J.w2^(2:ℕ) + 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p1*J.r0*J.r1 - 4*J.p2^(2:ℕ)*J.r0^(2:ℕ) + 4*J.p2*J.r0*J.r2)/4) / ((J.ea) * (J.r0)^(2:ℕ))), 0]]], 
    ![![![0, 0, ((-(J.a1*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w1 - 4*J.a1*J.p1*J.r0^(3:ℕ)*J.w0 - J.a1*J.r0^(3:ℕ)*J.w1 + 2*J.a1*J.r0^(2:ℕ)*J.r1*J.w0 + J.a2*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w2 - 4*J.a2*J.p2*J.r0^(3:ℕ)*J.w0 - J.a2*J.r0^(3:ℕ)*J.w2 + 2*J.a2*J.r0^(2:ℕ)*J.r2*J.w0 - 4*J.ep^(2:ℕ)*J.p1*J.r0*J.w0^(2:ℕ)*J.w1 - J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w11 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1^(2:ℕ) + J.ep^(2:ℕ)*J.r1*J.w0^(2:ℕ)*J.w1 + 4*J.p1*J.r0^(3:ℕ)*J.w1 + 4*J.p1*J.r0^(2:ℕ)*J.r1*J.w0 + 4*J.p11*J.r0^(3:ℕ)*J.w0 + J.r0^(3:ℕ)*J.w11 - J.r0^(2:ℕ)*J.r1*J.w1 - 2*J.r0^(2:ℕ)*J.r11*J.w0)/2) / ((J.ea) * (J.r0)^(3:ℕ))), (((2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a1*J.p1*J.r0^(3:ℕ) + 4*J.a1*J.r0^(2:ℕ)*J.r1 + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a2*J.p2*J.r0^(3:ℕ) + 4*J.a2*J.r0^(2:ℕ)*J.r2 - 8*J.ep^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w11 - 3*J.ep^(2:ℕ)*J.r0*J.w1^(2:ℕ) + 2*J.ep^(2:ℕ)*J.r1*J.w0*J.w1 - 4*J.p1^(2:ℕ)*J.r0^(3:ℕ) + 8*J.p1*J.r0^(2:ℕ)*J.r1 + 4*J.p11*J.r0^(3:ℕ) - 4*J.r0^(2:ℕ)*J.r11)/4) / ((J.ea) * (J.r0)^(3:ℕ)))], ![0, 0, (((J.a1*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w2 - 4*J.a1*J.p2*J.r0^(3:ℕ)*J.w0 - J.a1*J.r0^(3:ℕ)*J.w2 + 2*J.a1*J.r0^(2:ℕ)*J.r2*J.w0 + J.a2*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w1 - 4*J.a2*J.p1*J.r0^(3:ℕ)*J.w0 - J.a2*J.r0^(3:ℕ)*J.w1 + 2*J.a2*J.r0^(2:ℕ)*J.r1*J.w0 - 3*J.ep^(2:ℕ)*J.p1*J.r0*J.w0^(2:ℕ)*J.w2 - J.ep^(2:ℕ)*J.p2*J.r0*J.w0^(2:ℕ)*J.w1 - J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w12 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1*J.w2 + J.ep^(2:ℕ)*J.r1*J.w0^(2:ℕ)*J.w2 + J.p1*J.r0^(3:ℕ)*J.w2 + 2*J.p1*J.r0^(2:ℕ)*J.r2*J.w0 + 4*J.p12*J.r0^(3:ℕ)*J.w0 + 3*J.p2*J.r0^(3:ℕ)*J.w1 + 2*J.p2*J.r0^(2:ℕ)*J.r1*J.w0 + J.r0^(3:ℕ)*J.w12 - 2*J.r0^(2:ℕ)*J.r12*J.w0 - J.r0^(2:ℕ)*J.r2*J.w1)/2) / ((J.ea) * (J.r0)^(3:ℕ))), ((-(2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a1*J.p2*J.r0^(3:ℕ) + 4*J.a1*J.r0^(2:ℕ)*J.r2 + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a2*J.p1*J.r0^(3:ℕ) + 4*J.a2*J.r0^(2:ℕ)*J.r1 - 6*J.ep^(2:ℕ)*J.p1*J.r0*J.w0*J.w2 - 2*J.ep^(2:ℕ)*J.p2*J.r0*J.w0*J.w1 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w12 - 3*J.ep^(2:ℕ)*J.r0*J.w1*J.w2 + 2*J.ep^(2:ℕ)*J.r1*J.w0*J.w2 - 4*J.p1*J.p2*J.r0^(3:ℕ) + 4*J.p1*J.r0^(2:ℕ)*J.r2 + 4*J.p12*J.r0^(3:ℕ) + 4*J.p2*J.r0^(2:ℕ)*J.r1 - 4*J.r0^(2:ℕ)*J.r12)/4) / ((J.ea) * (J.r0)^(3:ℕ)))], ![(((J.a1*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w1 - 4*J.a1*J.p1*J.r0^(3:ℕ)*J.w0 - J.a1*J.r0^(3:ℕ)*J.w1 + 2*J.a1*J.r0^(2:ℕ)*J.r1*J.w0 + J.a2*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w2 - 4*J.a2*J.p2*J.r0^(3:ℕ)*J.w0 - J.a2*J.r0^(3:ℕ)*J.w2 + 2*J.a2*J.r0^(2:ℕ)*J.r2*J.w0 - 4*J.ep^(2:ℕ)*J.p1*J.r0*J.w0^(2:ℕ)*J.w1 - J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w11 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1^(2:ℕ) + J.ep^(2:ℕ)*J.r1*J.w0^(2:ℕ)*J.w1 + 4*J.p1*J.r0^(3:ℕ)*J.w1 + 4*J.p1*J.r0^(2:ℕ)*J.r1*J.w0 + 4*J.p11*J.r0^(3:ℕ)*J.w0 + J.r0^(3:ℕ)*J.w11 - J.r0^(2:ℕ)*J.r1*J.w1 - 2*J.r0^(2:ℕ)*J.r11*J.w0)/2) / ((J.ea) * (J.r0)^(3:ℕ))), ((-(J.a1*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w2 - 4*J.a1*J.p2*J.r0^(3:ℕ)*J.w0 - J.a1*J.r0^(3:ℕ)*J.w2 + 2*J.a1*J.r0^(2:ℕ)*J.r2*J.w0 + J.a2*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w1 - 4*J.a2*J.p1*J.r0^(3:ℕ)*J.w0 - J.a2*J.r0^(3:ℕ)*J.w1 + 2*J.a2*J.r0^(2:ℕ)*J.r1*J.w0 - 3*J.ep^(2:ℕ)*J.p1*J.r0*J.w0^(2:ℕ)*J.w2 - J.ep^(2:ℕ)*J.p2*J.r0*J.w0^(2:ℕ)*J.w1 - J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w12 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1*J.w2 + J.ep^(2:ℕ)*J.r1*J.w0^(2:ℕ)*J.w2 + J.p1*J.r0^(3:ℕ)*J.w2 + 2*J.p1*J.r0^(2:ℕ)*J.r2*J.w0 + 4*J.p12*J.r0^(3:ℕ)*J.w0 + 3*J.p2*J.r0^(3:ℕ)*J.w1 + 2*J.p2*J.r0^(2:ℕ)*J.r1*J.w0 + J.r0^(3:ℕ)*J.w12 - 2*J.r0^(2:ℕ)*J.r12*J.w0 - J.r0^(2:ℕ)*J.r2*J.w1)/2) / ((J.ea) * (J.r0)^(3:ℕ))), 0, 0], ![((-(2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a1*J.p1*J.r0^(3:ℕ) + 4*J.a1*J.r0^(2:ℕ)*J.r1 + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a2*J.p2*J.r0^(3:ℕ) + 4*J.a2*J.r0^(2:ℕ)*J.r2 - 8*J.ep^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w11 - 3*J.ep^(2:ℕ)*J.r0*J.w1^(2:ℕ) + 2*J.ep^(2:ℕ)*J.r1*J.w0*J.w1 - 4*J.p1^(2:ℕ)*J.r0^(3:ℕ) + 8*J.p1*J.r0^(2:ℕ)*J.r1 + 4*J.p11*J.r0^(3:ℕ) - 4*J.r0^(2:ℕ)*J.r11)/4) / ((J.ea) * (J.r0)^(3:ℕ))), (((2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a1*J.p2*J.r0^(3:ℕ) + 4*J.a1*J.r0^(2:ℕ)*J.r2 + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a2*J.p1*J.r0^(3:ℕ) + 4*J.a2*J.r0^(2:ℕ)*J.r1 - 6*J.ep^(2:ℕ)*J.p1*J.r0*J.w0*J.w2 - 2*J.ep^(2:ℕ)*J.p2*J.r0*J.w0*J.w1 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w12 - 3*J.ep^(2:ℕ)*J.r0*J.w1*J.w2 + 2*J.ep^(2:ℕ)*J.r1*J.w0*J.w2 - 4*J.p1*J.p2*J.r0^(3:ℕ) + 4*J.p1*J.r0^(2:ℕ)*J.r2 + 4*J.p12*J.r0^(3:ℕ) + 4*J.p2*J.r0^(2:ℕ)*J.r1 - 4*J.r0^(2:ℕ)*J.r12)/4) / ((J.ea) * (J.r0)^(3:ℕ))), 0, 0]], ![![0, 0, ((-(J.a1*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w2 - 4*J.a1*J.p2*J.r0^(3:ℕ)*J.w0 - J.a1*J.r0^(3:ℕ)*J.w2 + 2*J.a1*J.r0^(2:ℕ)*J.r2*J.w0 + J.a2*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w1 - 4*J.a2*J.p1*J.r0^(3:ℕ)*J.w0 - J.a2*J.r0^(3:ℕ)*J.w1 + 2*J.a2*J.r0^(2:ℕ)*J.r1*J.w0 - J.ep^(2:ℕ)*J.p1*J.r0*J.w0^(2:ℕ)*J.w2 - 3*J.ep^(2:ℕ)*J.p2*J.r0*J.w0^(2:ℕ)*J.w1 - J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w12 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1*J.w2 + J.ep^(2:ℕ)*J.r2*J.w0^(2:ℕ)*J.w1 + 3*J.p1*J.r0^(3:ℕ)*J.w2 + 2*J.p1*J.r0^(2:ℕ)*J.r2*J.w0 + 4*J.p12*J.r0^(3:ℕ)*J.w0 + J.p2*J.r0^(3:ℕ)*J.w1 + 2*J.p2*J.r0^(2:ℕ)*J.r1*J.w0 + J.r0^(3:ℕ)*J.w12 - J.r0^(2:ℕ)*J.r1*J.w2 - 2*J.r0^(2:ℕ)*J.r12*J.w0)/2) / ((J.ea) * (J.r0)^(3:ℕ))), (((2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a1*J.p2*J.r0^(3:ℕ) + 4*J.a1*J.r0^(2:ℕ)*J.r2 + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a2*J.p1*J.r0^(3:ℕ) + 4*J.a2*J.r0^(2:ℕ)*J.r1 - 2*J.ep^(2:ℕ)*J.p1*J.r0*J.w0*J.w2 - 6*J.ep^(2:ℕ)*J.p2*J.r0*J.w0*J.w1 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w12 - 3*J.ep^(2:ℕ)*J.r0*J.w1*J.w2 + 2*J.ep^(2:ℕ)*J.r2*J.w0*J.w1 - 4*J.p1*J.p2*J.r0^(3:ℕ) + 4*J.p1*J.r0^(2:ℕ)*J.r2 + 4*J.p12*J.r0^(3:ℕ) + 4*J.p2*J.r0^(2:ℕ)*J.r1 - 4*J.r0^(2:ℕ)*J.r12)/4) / ((J.ea) * (J.r0)^(3:ℕ)))], ![0, 0, (((J.a1*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w1 - 4*J.a1*J.p1*J.r0^(3:ℕ)*J.w0 - J.a1*J.r0^(3:ℕ)*J.w1 + 2*J.a1*J.r0^(2:ℕ)*J.r1*J.w0 + J.a2*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w2 - 4*J.a2*J.p2*J.r0^(3:ℕ)*J.w0 - J.a2*J.r0^(3:ℕ)*J.w2 + 2*J.a2*J.r0^(2:ℕ)*J.r2*J.w0 - 4*J.ep^(2:ℕ)*J.p2*J.r0*J.w0^(2:ℕ)*J.w2 - J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w22 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w2^(2:ℕ) + J.ep^(2:ℕ)*J.r2*J.w0^(2:ℕ)*J.w2 + 4*J.p2*J.r0^(3:ℕ)*J.w2 + 4*J.p2*J.r0^(2:ℕ)*J.r2*J.w0 + 4*J.p22*J.r0^(3:ℕ)*J.w0 + J.r0^(3:ℕ)*J.w22 - J.r0^(2:ℕ)*J.r2*J.w2 - 2*J.r0^(2:ℕ)*J.r22*J.w0)/2) / ((J.ea) * (J.r0)^(3:ℕ))), ((-(2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a1*J.p1*J.r0^(3:ℕ) + 4*J.a1*J.r0^(2:ℕ)*J.r1 + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a2*J.p2*J.r0^(3:ℕ) + 4*J.a2*J.r0^(2:ℕ)*J.r2 - 8*J.ep^(2:ℕ)*J.p2*J.r0*J.w0*J.w2 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w22 - 3*J.ep^(2:ℕ)*J.r0*J.w2^(2:ℕ) + 2*J.ep^(2:ℕ)*J.r2*J.w0*J.w2 - 4*J.p2^(2:ℕ)*J.r0^(3:ℕ) + 8*J.p2*J.r0^(2:ℕ)*J.r2 + 4*J.p22*J.r0^(3:ℕ) - 4*J.r0^(2:ℕ)*J.r22)/4) / ((J.ea) * (J.r0)^(3:ℕ)))], ![(((J.a1*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w2 - 4*J.a1*J.p2*J.r0^(3:ℕ)*J.w0 - J.a1*J.r0^(3:ℕ)*J.w2 + 2*J.a1*J.r0^(2:ℕ)*J.r2*J.w0 + J.a2*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w1 - 4*J.a2*J.p1*J.r0^(3:ℕ)*J.w0 - J.a2*J.r0^(3:ℕ)*J.w1 + 2*J.a2*J.r0^(2:ℕ)*J.r1*J.w0 - J.ep^(2:ℕ)*J.p1*J.r0*J.w0^(2:ℕ)*J.w2 - 3*J.ep^(2:ℕ)*J.p2*J.r0*J.w0^(2:ℕ)*J.w1 - J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w12 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1*J.w2 + J.ep^(2:ℕ)*J.r2*J.w0^(2:ℕ)*J.w1 + 3*J.p1*J.r0^(3:ℕ)*J.w2 + 2*J.p1*J.r0^(2:ℕ)*J.r2*J.w0 + 4*J.p12*J.r0^(3:ℕ)*J.w0 + J.p2*J.r0^(3:ℕ)*J.w1 + 2*J.p2*J.r0^(2:ℕ)*J.r1*J.w0 + J.r0^(3:ℕ)*J.w12 - J.r0^(2:ℕ)*J.r1*J.w2 - 2*J.r0^(2:ℕ)*J.r12*J.w0)/2) / ((J.ea) * (J.r0)^(3:ℕ))), ((-(J.a1*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w1 - 4*J.a1*J.p1*J.r0^(3:ℕ)*J.w0 - J.a1*J.r0^(3:ℕ)*J.w1 + 2*J.a1*J.r0^(2:ℕ)*J.r1*J.w0 + J.a2*J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w2 - 4*J.a2*J.p2*J.r0^(3:ℕ)*J.w0 - J.a2*J.r0^(3:ℕ)*J.w2 + 2*J.a2*J.r0^(2:ℕ)*J.r2*J.w0 - 4*J.ep^(2:ℕ)*J.p2*J.r0*J.w0^(2:ℕ)*J.w2 - J.ep^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w22 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w2^(2:ℕ) + J.ep^(2:ℕ)*J.r2*J.w0^(2:ℕ)*J.w2 + 4*J.p2*J.r0^(3:ℕ)*J.w2 + 4*J.p2*J.r0^(2:ℕ)*J.r2*J.w0 + 4*J.p22*J.r0^(3:ℕ)*J.w0 + J.r0^(3:ℕ)*J.w22 - J.r0^(2:ℕ)*J.r2*J.w2 - 2*J.r0^(2:ℕ)*J.r22*J.w0)/2) / ((J.ea) * (J.r0)^(3:ℕ))), 0, 0], ![((-(2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a1*J.p2*J.r0^(3:ℕ) + 4*J.a1*J.r0^(2:ℕ)*J.r2 + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a2*J.p1*J.r0^(3:ℕ) + 4*J.a2*J.r0^(2:ℕ)*J.r1 - 2*J.ep^(2:ℕ)*J.p1*J.r0*J.w0*J.w2 - 6*J.ep^(2:ℕ)*J.p2*J.r0*J.w0*J.w1 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w12 - 3*J.ep^(2:ℕ)*J.r0*J.w1*J.w2 + 2*J.ep^(2:ℕ)*J.r2*J.w0*J.w1 - 4*J.p1*J.p2*J.r0^(3:ℕ) + 4*J.p1*J.r0^(2:ℕ)*J.r2 + 4*J.p12*J.r0^(3:ℕ) + 4*J.p2*J.r0^(2:ℕ)*J.r1 - 4*J.r0^(2:ℕ)*J.r12)/4) / ((J.ea) * (J.r0)^(3:ℕ))), (((2*J.a1*J.ep^(2:ℕ)*J.r0*J.w0*J.w1 - 4*J.a1*J.p1*J.r0^(3:ℕ) + 4*J.a1*J.r0^(2:ℕ)*J.r1 + 2*J.a2*J.ep^(2:ℕ)*J.r0*J.w0*J.w2 - 4*J.a2*J.p2*J.r0^(3:ℕ) + 4*J.a2*J.r0^(2:ℕ)*J.r2 - 8*J.ep^(2:ℕ)*J.p2*J.r0*J.w0*J.w2 - 2*J.ep^(2:ℕ)*J.r0*J.w0*J.w22 - 3*J.ep^(2:ℕ)*J.r0*J.w2^(2:ℕ) + 2*J.ep^(2:ℕ)*J.r2*J.w0*J.w2 - 4*J.p2^(2:ℕ)*J.r0^(3:ℕ) + 8*J.p2*J.r0^(2:ℕ)*J.r2 + 4*J.p22*J.r0^(3:ℕ) - 4*J.r0^(2:ℕ)*J.r22)/4) / ((J.ea) * (J.r0)^(3:ℕ))), 0, 0]], ![![0, ((-J.ep*(2*J.p1*J.r0*J.w2 - 2*J.p2*J.r0*J.w1 - J.r1*J.w2 + J.r2*J.w1)/2) / ((J.r0) * (J.ea)^(2:ℕ))), 0, 0], ![((J.ep*(2*J.p1*J.r0*J.w2 - 2*J.p2*J.r0*J.w1 - J.r1*J.w2 + J.r2*J.w1)/2) / ((J.r0) * (J.ea)^(2:ℕ))), 0, 0, 0], ![0, 0, 0, (((J.ep^(2:ℕ)*J.w1^(2:ℕ) - J.ep^(2:ℕ)*J.w2^(2:ℕ) + 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p1*J.r0*J.r1 - 4*J.p2^(2:ℕ)*J.r0^(2:ℕ) + 4*J.p2*J.r0*J.r2)/4) / ((J.ea) * (J.r0)^(2:ℕ)))], ![0, 0, ((-(J.ep^(2:ℕ)*J.w1^(2:ℕ) - J.ep^(2:ℕ)*J.w2^(2:ℕ) + 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p1*J.r0*J.r1 - 4*J.p2^(2:ℕ)*J.r0^(2:ℕ) + 4*J.p2*J.r0*J.r2)/4) / ((J.ea) * (J.r0)^(2:ℕ))), 0]], ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]]]]
/-- The part of the density **linear** in the twist's derivatives `ω_t, ω_z, ω_tt, ω_tz, ω_zz`. -/
noncomputable def WLin (J : GJ) : ℝ :=
  (J.r0*(4*J.a1^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w2 - 4*J.a1^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w1 - 2*J.a1^(2:ℕ)*J.r0*J.r1*J.w2 + 2*J.a1^(2:ℕ)*J.r0*J.r2*J.w1 - 8*J.a1*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w2 - 4*J.a1*J.p1*J.r0^(2:ℕ)*J.w12 + 4*J.a1*J.p1*J.r0*J.r1*J.w2 - 2*J.a1*J.p11*J.r0^(2:ℕ)*J.w2 + 4*J.a1*J.p12*J.r0^(2:ℕ)*J.w1 + 8*J.a1*J.p2^(2:ℕ)*J.r0^(2:ℕ)*J.w2 + 2*J.a1*J.p2*J.r0^(2:ℕ)*J.w11 + 2*J.a1*J.p2*J.r0^(2:ℕ)*J.w22 + 4*J.a1*J.p2*J.r0*J.r1*J.w1 - 8*J.a1*J.p2*J.r0*J.r2*J.w2 - 2*J.a1*J.p22*J.r0^(2:ℕ)*J.w2 + 2*J.a1*J.r0*J.r1*J.w12 + J.a1*J.r0*J.r11*J.w2 - 2*J.a1*J.r0*J.r12*J.w1 - J.a1*J.r0*J.r2*J.w11 - J.a1*J.r0*J.r2*J.w22 + J.a1*J.r0*J.r22*J.w2 - J.a1*J.r1^(2:ℕ)*J.w2 + J.a1*J.r2^(2:ℕ)*J.w2 - 2*J.a11*J.p1*J.r0^(2:ℕ)*J.w2 + 2*J.a11*J.p2*J.r0^(2:ℕ)*J.w1 + J.a11*J.r0*J.r1*J.w2 - J.a11*J.r0*J.r2*J.w1 - 4*J.a2^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w2 + 4*J.a2^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w1 + 2*J.a2^(2:ℕ)*J.r0*J.r1*J.w2 - 2*J.a2^(2:ℕ)*J.r0*J.r2*J.w1 + 8*J.a2*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w1 + 2*J.a2*J.p1*J.r0^(2:ℕ)*J.w11 + 2*J.a2*J.p1*J.r0^(2:ℕ)*J.w22 - 8*J.a2*J.p1*J.r0*J.r1*J.w1 + 4*J.a2*J.p1*J.r0*J.r2*J.w2 - 2*J.a2*J.p11*J.r0^(2:ℕ)*J.w1 + 4*J.a2*J.p12*J.r0^(2:ℕ)*J.w2 - 8*J.a2*J.p2^(2:ℕ)*J.r0^(2:ℕ)*J.w1 - 4*J.a2*J.p2*J.r0^(2:ℕ)*J.w12 + 4*J.a2*J.p2*J.r0*J.r2*J.w1 - 2*J.a2*J.p22*J.r0^(2:ℕ)*J.w1 - J.a2*J.r0*J.r1*J.w11 - J.a2*J.r0*J.r1*J.w22 + J.a2*J.r0*J.r11*J.w1 - 2*J.a2*J.r0*J.r12*J.w2 + 2*J.a2*J.r0*J.r2*J.w12 + J.a2*J.r0*J.r22*J.w1 + J.a2*J.r1^(2:ℕ)*J.w1 - J.a2*J.r2^(2:ℕ)*J.w1 + 2*J.a22*J.p1*J.r0^(2:ℕ)*J.w2 - 2*J.a22*J.p2*J.r0^(2:ℕ)*J.w1 - J.a22*J.r0*J.r1*J.w2 + J.a22*J.r0*J.r2*J.w1 + 4*J.p1^(3:ℕ)*J.r0^(2:ℕ)*J.w2 - 4*J.p1^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w1 - 2*J.p1^(2:ℕ)*J.r0*J.r1*J.w2 - 2*J.p1^(2:ℕ)*J.r0*J.r2*J.w1 + 4*J.p1*J.p11*J.r0^(2:ℕ)*J.w2 - 8*J.p1*J.p12*J.r0^(2:ℕ)*J.w1 - 4*J.p1*J.p2^(2:ℕ)*J.r0^(2:ℕ)*J.w2 + 4*J.p1*J.p2*J.r0*J.r1*J.w1 + 4*J.p1*J.p2*J.r0*J.r2*J.w2 + 4*J.p1*J.p22*J.r0^(2:ℕ)*J.w2 + 2*J.p1*J.r0*J.r1*J.w12 - J.p1*J.r0*J.r11*J.w2 + 4*J.p1*J.r0*J.r12*J.w1 - J.p1*J.r0*J.r2*J.w11 - J.p1*J.r0*J.r2*J.w22 - 3*J.p1*J.r0*J.r22*J.w2 + J.p1*J.r1^(2:ℕ)*J.w2 - 2*J.p1*J.r1*J.r2*J.w1 + J.p1*J.r2^(2:ℕ)*J.w2 + 4*J.p11*J.p2*J.r0^(2:ℕ)*J.w1 + 2*J.p11*J.r0^(2:ℕ)*J.w12 - J.p11*J.r0*J.r1*J.w2 - J.p11*J.r0*J.r2*J.w1 - 8*J.p12*J.p2*J.r0^(2:ℕ)*J.w2 - 2*J.p12*J.r0^(2:ℕ)*J.w11 - 2*J.p12*J.r0^(2:ℕ)*J.w22 + 2*J.p12*J.r0*J.r1*J.w1 + 2*J.p12*J.r0*J.r2*J.w2 + 4*J.p2^(3:ℕ)*J.r0^(2:ℕ)*J.w1 - 2*J.p2^(2:ℕ)*J.r0*J.r1*J.w2 - 2*J.p2^(2:ℕ)*J.r0*J.r2*J.w1 + 4*J.p2*J.p22*J.r0^(2:ℕ)*J.w1 - J.p2*J.r0*J.r1*J.w11 - J.p2*J.r0*J.r1*J.w22 - 3*J.p2*J.r0*J.r11*J.w1 + 4*J.p2*J.r0*J.r12*J.w2 + 2*J.p2*J.r0*J.r2*J.w12 - J.p2*J.r0*J.r22*J.w1 + J.p2*J.r1^(2:ℕ)*J.w1 - 2*J.p2*J.r1*J.r2*J.w2 + J.p2*J.r2^(2:ℕ)*J.w1 + 2*J.p22*J.r0^(2:ℕ)*J.w12 - J.p22*J.r0*J.r1*J.w2 - J.p22*J.r0*J.r2*J.w1 - J.r0*J.r11*J.w12 + J.r0*J.r12*J.w11 + J.r0*J.r12*J.w22 - J.r0*J.r22*J.w12 - J.r1*J.r12*J.w1 + J.r1*J.r22*J.w2 + J.r11*J.r2*J.w1 - J.r12*J.r2*J.w2))

/-- The part **cubic** in them (it enters with `e^{4ψ}`). -/
noncomputable def WCub (J : GJ) : ℝ :=
  (-J.a1*J.r0*J.w1^(2:ℕ)*J.w2 + J.a1*J.r0*J.w2^(3:ℕ) + J.a2*J.r0*J.w1^(3:ℕ) - J.a2*J.r0*J.w1*J.w2^(2:ℕ) + 3*J.p1*J.r0*J.w1^(2:ℕ)*J.w2 - 3*J.p1*J.r0*J.w2^(3:ℕ) - 3*J.p2*J.r0*J.w1^(3:ℕ) + 3*J.p2*J.r0*J.w1*J.w2^(2:ℕ) - J.r0*J.w1^(2:ℕ)*J.w12 + J.r0*J.w1*J.w11*J.w2 + J.r0*J.w1*J.w2*J.w22 - J.r0*J.w12*J.w2^(2:ℕ) - J.r1*J.w1^(2:ℕ)*J.w2 + J.r1*J.w2^(3:ℕ) + J.r2*J.w1^(3:ℕ) - J.r2*J.w1*J.w2^(2:ℕ))

variable (J : GJ) (hA : J.ea ≠ 0) (hP : J.ep ≠ 0) (hR : J.r0 ≠ 0)
include hA hP hR

lemma WGiT_ok (m k : Fin 4) : ∑ l, WGT J m l * WGiT J l k = if m = k then 1 else 0 := by
  fin_cases m <;> fin_cases k <;> simp [Fin.sum_univ_four, WGT, WGiT] <;> (try field_simp) <;> ring1

lemma WGamT_ok (i j k : Fin 4) : GamF (WD1T J) (WGiT J) i j k = WGamT J i j k := by
  simp only [GamF]
  fin_cases i <;> fin_cases j <;> fin_cases k <;> simp [Fin.sum_univ_four, WD1T, WGiT, WGamT] <;>
    (try field_simp) <;> ring1

lemma WDGT_ok0 (i j k : Fin 4) : DGamF (WD1T J) (WD2T J) (WGiT J) 0 i j k = WDGT J 0 i j k := by
  simp only [DGamF, WGamT_ok J hA hP hR]; fin_cases i <;> fin_cases j <;> fin_cases k <;> simp [Fin.sum_univ_four, WD2T, WD1T, WGiT, WGamT, WDGT] <;> (try field_simp) <;> ring1
lemma WDGT_ok1 (i j k : Fin 4) : DGamF (WD1T J) (WD2T J) (WGiT J) 1 i j k = WDGT J 1 i j k := by
  simp only [DGamF, WGamT_ok J hA hP hR]; fin_cases i <;> fin_cases j <;> fin_cases k <;> simp [Fin.sum_univ_four, WD2T, WD1T, WGiT, WGamT, WDGT] <;> (try field_simp) <;> ring1
lemma WDGT_ok2 (i j k : Fin 4) : DGamF (WD1T J) (WD2T J) (WGiT J) 2 i j k = WDGT J 2 i j k := by
  simp only [DGamF, WGamT_ok J hA hP hR]; fin_cases i <;> fin_cases j <;> fin_cases k <;> simp [Fin.sum_univ_four, WD2T, WD1T, WGiT, WGamT, WDGT] <;> (try field_simp) <;> ring1
lemma WDGT_ok3 (i j k : Fin 4) : DGamF (WD1T J) (WD2T J) (WGiT J) 3 i j k = WDGT J 3 i j k := by
  simp only [DGamF, WGamT_ok J hA hP hR]; fin_cases i <;> fin_cases j <;> fin_cases k <;> simp [Fin.sum_univ_four, WD2T, WD1T, WGiT, WGamT, WDGT] <;> (try field_simp) <;> ring1
lemma WDGT_ok (w i j k : Fin 4) : DGamF (WD1T J) (WD2T J) (WGiT J) w i j k = WDGT J w i j k := by
  fin_cases w
  exacts [WDGT_ok0 J hA hP hR i j k, WDGT_ok1 J hA hP hR i j k, WDGT_ok2 J hA hP hR i j k, WDGT_ok3 J hA hP hR i j k]

lemma WRT_ok0 (j k l : Fin 4) : RiemF (WD1T J) (WD2T J) (WGiT J) 0 j k l = WRT J 0 j k l := by
  simp only [RiemF, WDGT_ok J hA hP hR, WGamT_ok J hA hP hR]; fin_cases j <;> fin_cases k <;> fin_cases l <;> simp [Fin.sum_univ_four, WDGT, WGamT, WRT] <;> (try field_simp) <;> ring1
lemma WRT_ok1 (j k l : Fin 4) : RiemF (WD1T J) (WD2T J) (WGiT J) 1 j k l = WRT J 1 j k l := by
  simp only [RiemF, WDGT_ok J hA hP hR, WGamT_ok J hA hP hR]; fin_cases j <;> fin_cases k <;> fin_cases l <;> simp [Fin.sum_univ_four, WDGT, WGamT, WRT] <;> (try field_simp) <;> ring1
lemma WRT_ok2 (j k l : Fin 4) : RiemF (WD1T J) (WD2T J) (WGiT J) 2 j k l = WRT J 2 j k l := by
  simp only [RiemF, WDGT_ok J hA hP hR, WGamT_ok J hA hP hR]; fin_cases j <;> fin_cases k <;> fin_cases l <;> simp [Fin.sum_univ_four, WDGT, WGamT, WRT] <;> (try field_simp) <;> ring1
lemma WRT_ok3 (j k l : Fin 4) : RiemF (WD1T J) (WD2T J) (WGiT J) 3 j k l = WRT J 3 j k l := by
  simp only [RiemF, WDGT_ok J hA hP hR, WGamT_ok J hA hP hR]; fin_cases j <;> fin_cases k <;> fin_cases l <;> simp [Fin.sum_univ_four, WDGT, WGamT, WRT] <;> (try field_simp) <;> ring1
lemma WRT_ok (i j k l : Fin 4) : RiemF (WD1T J) (WD2T J) (WGiT J) i j k l = WRT J i j k l := by
  fin_cases i
  exacts [WRT_ok0 J hA hP hR j k l, WRT_ok1 J hA hP hR j k l, WRT_ok2 J hA hP hR j k l, WRT_ok3 J hA hP hR j k l]

lemma WRDT_ok0 (n a b : Fin 4) : lowR (Matrix.of (WGT J)) (WRT J) 0 n a b = WRDT J 0 n a b := by
  fin_cases n <;> fin_cases a <;> fin_cases b <;> simp [lowR, Fin.sum_univ_four, WGT, WRT, WRDT] <;> (try field_simp) <;> ring1
lemma WRDT_ok1 (n a b : Fin 4) : lowR (Matrix.of (WGT J)) (WRT J) 1 n a b = WRDT J 1 n a b := by
  fin_cases n <;> fin_cases a <;> fin_cases b <;> simp [lowR, Fin.sum_univ_four, WGT, WRT, WRDT] <;> (try field_simp) <;> ring1
lemma WRDT_ok2 (n a b : Fin 4) : lowR (Matrix.of (WGT J)) (WRT J) 2 n a b = WRDT J 2 n a b := by
  fin_cases n <;> fin_cases a <;> fin_cases b <;> simp [lowR, Fin.sum_univ_four, WGT, WRT, WRDT] <;> (try field_simp) <;> ring1
lemma WRDT_ok3 (n a b : Fin 4) : lowR (Matrix.of (WGT J)) (WRT J) 3 n a b = WRDT J 3 n a b := by
  fin_cases n <;> fin_cases a <;> fin_cases b <;> simp [lowR, Fin.sum_univ_four, WGT, WRT, WRDT] <;> (try field_simp) <;> ring1
lemma WRDT_ok (m n a b : Fin 4) : lowR (Matrix.of (WGT J)) (WRT J) m n a b = WRDT J m n a b := by
  fin_cases m
  exacts [WRDT_ok0 J hA hP hR n a b, WRDT_ok1 J hA hP hR n a b, WRDT_ok2 J hA hP hR n a b, WRDT_ok3 J hA hP hR n a b]

lemma WRUT_ok0 (n a b : Fin 4) :
    raiseR (Matrix.of (WGT J)) (Matrix.of (WGiT J)) (WRT J) 0 n a b = WRUT J 0 n a b := by
  simp only [raiseR, WRDT_ok J hA hP hR, Matrix.of_apply]; fin_cases n <;> fin_cases a <;> fin_cases b <;> simp [Fin.sum_univ_four, WGiT, WRDT, WRUT] <;> (try field_simp) <;> ring1
lemma WRUT_ok1 (n a b : Fin 4) :
    raiseR (Matrix.of (WGT J)) (Matrix.of (WGiT J)) (WRT J) 1 n a b = WRUT J 1 n a b := by
  simp only [raiseR, WRDT_ok J hA hP hR, Matrix.of_apply]; fin_cases n <;> fin_cases a <;> fin_cases b <;> simp [Fin.sum_univ_four, WGiT, WRDT, WRUT] <;> (try field_simp) <;> ring1
lemma WRUT_ok2 (n a b : Fin 4) :
    raiseR (Matrix.of (WGT J)) (Matrix.of (WGiT J)) (WRT J) 2 n a b = WRUT J 2 n a b := by
  simp only [raiseR, WRDT_ok J hA hP hR, Matrix.of_apply]; fin_cases n <;> fin_cases a <;> fin_cases b <;> simp [Fin.sum_univ_four, WGiT, WRDT, WRUT] <;> (try field_simp) <;> ring1
lemma WRUT_ok3 (n a b : Fin 4) :
    raiseR (Matrix.of (WGT J)) (Matrix.of (WGiT J)) (WRT J) 3 n a b = WRUT J 3 n a b := by
  simp only [raiseR, WRDT_ok J hA hP hR, Matrix.of_apply]; fin_cases n <;> fin_cases a <;> fin_cases b <;> simp [Fin.sum_univ_four, WGiT, WRDT, WRUT] <;> (try field_simp) <;> ring1
lemma WRUT_ok (m n a b : Fin 4) :
    raiseR (Matrix.of (WGT J)) (Matrix.of (WGiT J)) (WRT J) m n a b = WRUT J m n a b := by
  fin_cases m
  exacts [WRUT_ok0 J hA hP hR n a b, WRUT_ok1 J hA hP hR n a b, WRUT_ok2 J hA hP hR n a b, WRUT_ok3 J hA hP hR n a b]

/-- **The `ε`-contraction from the tables**: `8 e^{2ψ}(WLin + e^{4ψ} WCub)/(e^{2A} R³)`. -/
lemma Wcontr_ok : (∑ m, ∑ n, ∑ r, ∑ s, (eps4 m n r s : ℝ) * ∑ a, ∑ b,
      lowR (Matrix.of (WGT J)) (WRT J) m n a b * raiseR (Matrix.of (WGT J)) (Matrix.of (WGiT J)) (WRT J) r s a b)
    = 8 * J.ep * (WLin J + J.ep ^ 2 * WCub J) / (J.ea * J.r0 ^ 3) := by
  rw [sum_eps]
  simp only [WRDT_ok J hA hP hR, WRUT_ok J hA hP hR]
  simp [Fin.sum_univ_four, WRDT, WRUT, WLin, WCub]
  field_simp
  ring1

end GowdyTables

#print axioms ShadowProbe.R89Pontryagin.Wcontr_ok

/-! ### The general unpolarised Gowdy metric -/

section GowdyMetric

/-- **P11's unpolarised Gowdy form** (the receipt's `gowdy_unpolarised`), coordinates `(t, z, x, y)`:
`e^{2A}(−dt² + dz²) + e^{2ψ}(dx + ω dy)² + R² e^{−2ψ} dy²`. -/
noncomputable def gowdyG (A ψ om R : (Fin 4 → ℝ) → ℝ) : Fin 4 → Fin 4 → (Fin 4 → ℝ) → ℝ := fun i j y =>
  (![![-Real.exp (2 * A y), 0, 0, 0], ![0, Real.exp (2 * A y), 0, 0],
    ![0, 0, Real.exp (2 * ψ y), Real.exp (2 * ψ y) * om y],
    ![0, 0, Real.exp (2 * ψ y) * om y, Real.exp (2 * ψ y) * (om y * om y) + R y * R y * (Real.exp (2 * ψ y))⁻¹]] :
    Fin 4 → Fin 4 → ℝ) i j

/-- A smooth function of `(t, z)` only: it does not change along `x` or `y`. -/
structure TZ (F : (Fin 4 → ℝ) → ℝ) : Prop where
  sm : ContDiff ℝ ∞ F
  ix : ∀ y (c : ℝ), F (y + c • Pi.single 2 1) = F y
  iy : ∀ y (c : ℝ), F (y + c • Pi.single 3 1) = F y

/-- Partials at `p`. -/
noncomputable def pd (F : (Fin 4 → ℝ) → ℝ) (p : Fin 4 → ℝ) (c : Fin 4) : ℝ := fderiv ℝ F p (Pi.single c 1)
noncomputable def pdd (F : (Fin 4 → ℝ) → ℝ) (p : Fin 4 → ℝ) (a c : Fin 4) : ℝ :=
  fderiv ℝ (fderiv ℝ F) p (Pi.single a 1) (Pi.single c 1)

lemma TZ.hasJ {F : (Fin 4 → ℝ) → ℝ} (hF : TZ F) (p : Fin 4 → ℝ) :
    HasJ F p (F p) ![pd F p 0, pd F p 1, 0, 0]
      ![![pdd F p 0 0, pdd F p 0 1, 0, 0], ![pdd F p 0 1, pdd F p 1 1, 0, 0], 0, 0] := by
  have dx := fun y => fderiv_dir_zero (hF.sm.differentiable (by simp)) (hF.ix) y
  have dy := fun y => fderiv_dir_zero (hF.sm.differentiable (by simp)) (hF.iy) y
  refine (hasJ_of hF.sm p).of_eq rfl (fun c => ?_) (fun a c => ?_)
  · fin_cases c <;> simp [pd, dx, dy]
  · have sx := d2_indep hF.sm dx p; have sy := d2_indep hF.sm dy p
    have sym : pdd F p 1 0 = pdd F p 0 1 := hF.sm.contDiffAt.isSymmSndFDerivAt (by simp) _ _
    fin_cases a <;> fin_cases c <;> simp [pdd, (sx _).1, (sx _).2, (sy _).1, (sy _).2] at sym ⊢ <;> exact sym

/-- The jet of the metric functions at `p`. -/
noncomputable def jetG (A ψ om R : (Fin 4 → ℝ) → ℝ) (p : Fin 4 → ℝ) : GJ where
  ea := Real.exp (2 * A p)
  ep := Real.exp (2 * ψ p)
  a1 := pd A p 0
  a2 := pd A p 1
  a11 := pdd A p 0 0
  a12 := pdd A p 0 1
  a22 := pdd A p 1 1
  p1 := pd ψ p 0
  p2 := pd ψ p 1
  p11 := pdd ψ p 0 0
  p12 := pdd ψ p 0 1
  p22 := pdd ψ p 1 1
  w0 := om p
  w1 := pd om p 0
  w2 := pd om p 1
  w11 := pdd om p 0 0
  w12 := pdd om p 0 1
  w22 := pdd om p 1 1
  r0 := R p
  r1 := pd R p 0
  r2 := pd R p 1
  r11 := pdd R p 0 0
  r12 := pdd R p 0 1
  r22 := pdd R p 1 1

variable {A ψ om R : (Fin 4 → ℝ) → ℝ}

lemma gowdyG_symm (A ψ om R : (Fin 4 → ℝ) → ℝ) (i j : Fin 4) (y : Fin 4 → ℝ) :
    gowdyG A ψ om R i j y = gowdyG A ψ om R j i y := by
  fin_cases i <;> fin_cases j <;> simp [gowdyG]

lemma gowdyG_smooth (hA : TZ A) (hψ : TZ ψ) (hom : TZ om) (hR : TZ R) (i j : Fin 4) :
    ContDiff ℝ ∞ (gowdyG A ψ om R i j) := by
  have eA : ContDiff ℝ ∞ (fun y => Real.exp (2 * A y)) := (contDiff_const.mul hA.sm).exp
  have eP : ContDiff ℝ ∞ (fun y => Real.exp (2 * ψ y)) := (contDiff_const.mul hψ.sm).exp
  have eI : ContDiff ℝ ∞ (fun y => (Real.exp (2 * ψ y))⁻¹) := eP.inv fun y => (Real.exp_pos _).ne'
  fin_cases i <;> fin_cases j <;> simp only [gowdyG] <;> simp <;>
    first
    | exact contDiff_const
    | exact eA
    | exact eA.neg
    | exact eP
    | exact eP.mul hom.sm
    | exact (eP.mul (hom.sm.mul hom.sm)).add ((hR.sm.mul hR.sm).mul eI)

lemma gowdyG_det (y : Fin 4 → ℝ) :
    (gm (gowdyG A ψ om R) y).det = -(Real.exp (2 * A y)) ^ 2 * R y ^ 2 := by
  have := (Real.exp_pos (2 * ψ y)).ne'
  simp [Matrix.det_succ_row_zero, Fin.sum_univ_succ, gm, gowdyG,
    show (Fin.succAbove 1 2 : Fin 4) = 3 by decide, show (Fin.succAbove 3 2 : Fin 4) = 2 by decide]
  field_simp; ring

lemma gowdyG_nondeg (hR0 : ∀ y, R y ≠ 0) : ∀ p (u : Fin 4 → ℝ), (∀ v, formG (gowdyG A ψ om R) p u v = 0) → u = 0 :=
  nondeg_of_det fun y => by
    rw [gowdyG_det]
    exact mul_ne_zero (neg_ne_zero.2 (pow_ne_zero 2 (Real.exp_pos _).ne')) (pow_ne_zero 2 (hR0 y))

variable (hA : TZ A) (hψ : TZ ψ) (hom : TZ om) (hR : TZ R) (p : Fin 4 → ℝ)
include hA hψ hom hR

/-- **The entries' jets at `p` are the tables.** -/
lemma gowdy_jets (i j : Fin 4) :
    HasJ (gowdyG A ψ om R i j) p (WGT (jetG A ψ om R p) i j) (WD1T (jetG A ψ om R p) i j) (WD2T (jetG A ψ om R p) i j) := by
  have jA := hA.hasJ p; have jP := hψ.hasJ p; have jW := hom.hasJ p; have jR := hR.hasJ p
  have eA := (jA.const_mul 2).exp
  have eP := (jP.const_mul 2).exp
  have e00 := eA.const_mul (-1)
  have e23 := eP.mul jW
  have e33 := (eP.mul (jW.mul jW)).add ((jR.mul jR).mul (eP.inv (Real.exp_pos _).ne'))
  have hE := (Real.exp_pos (2 * ψ p)).ne'
  have hz : ∀ i j, (∀ y, gowdyG A ψ om R i j y = 0) → WGT (jetG A ψ om R p) i j = 0 →
      WD1T (jetG A ψ om R p) i j = 0 → WD2T (jetG A ψ om R p) i j = 0 →
      HasJ (gowdyG A ψ om R i j) p (WGT (jetG A ψ om R p) i j) (WD1T (jetG A ψ om R p) i j) (WD2T (jetG A ψ om R p) i j) :=
    fun i j h1 h2 h3 h4 => ((hasJ_const 0 p).congr (Eventually.of_forall h1)).of_eq h2.symm (fun c => by rw [h3]; rfl)
      fun a c => by rw [h4]; rfl
  have h00 : HasJ (gowdyG A ψ om R 0 0) p (WGT (jetG A ψ om R p) 0 0) (WD1T (jetG A ψ om R p) 0 0) (WD2T (jetG A ψ om R p) 0 0) :=
    (e00.congr (Eventually.of_forall fun y => by simp [gowdyG])).of_eq (by simp [WGT, jetG]; try ring)
      (fun c => by fin_cases c <;> simp [WD1T, jetG] <;> ring)
      (fun a c => by fin_cases a <;> fin_cases c <;> simp [WD2T, jetG] <;> ring)
  have h11 : HasJ (gowdyG A ψ om R 1 1) p (WGT (jetG A ψ om R p) 1 1) (WD1T (jetG A ψ om R p) 1 1) (WD2T (jetG A ψ om R p) 1 1) :=
    (eA.congr (Eventually.of_forall fun y => by simp [gowdyG])).of_eq (by simp [WGT, jetG]; try ring)
      (fun c => by fin_cases c <;> simp [WD1T, jetG] <;> ring)
      (fun a c => by fin_cases a <;> fin_cases c <;> simp [WD2T, jetG] <;> ring)
  have h22 : HasJ (gowdyG A ψ om R 2 2) p (WGT (jetG A ψ om R p) 2 2) (WD1T (jetG A ψ om R p) 2 2) (WD2T (jetG A ψ om R p) 2 2) :=
    (eP.congr (Eventually.of_forall fun y => by simp [gowdyG])).of_eq (by simp [WGT, jetG]; try ring)
      (fun c => by fin_cases c <;> simp [WD1T, jetG] <;> ring)
      (fun a c => by fin_cases a <;> fin_cases c <;> simp [WD2T, jetG] <;> ring)
  have h23 : HasJ (gowdyG A ψ om R 2 3) p (WGT (jetG A ψ om R p) 2 3) (WD1T (jetG A ψ om R p) 2 3) (WD2T (jetG A ψ om R p) 2 3) :=
    (e23.congr (Eventually.of_forall fun y => by simp [gowdyG])).of_eq (by simp [WGT, jetG]; try ring)
      (fun c => by fin_cases c <;> simp [WD1T, jetG] <;> ring)
      (fun a c => by fin_cases a <;> fin_cases c <;> simp [WD2T, jetG] <;> ring)
  have h32 : HasJ (gowdyG A ψ om R 3 2) p (WGT (jetG A ψ om R p) 3 2) (WD1T (jetG A ψ om R p) 3 2) (WD2T (jetG A ψ om R p) 3 2) :=
    (e23.congr (Eventually.of_forall fun y => by simp [gowdyG])).of_eq (by simp [WGT, jetG]; try ring)
      (fun c => by fin_cases c <;> simp [WD1T, jetG] <;> ring)
      (fun a c => by fin_cases a <;> fin_cases c <;> simp [WD2T, jetG] <;> ring)
  have h33 : HasJ (gowdyG A ψ om R 3 3) p (WGT (jetG A ψ om R p) 3 3) (WD1T (jetG A ψ om R p) 3 3) (WD2T (jetG A ψ om R p) 3 3) :=
    (e33.congr (Eventually.of_forall fun y => by simp [gowdyG])).of_eq (by simp [WGT, jetG]; field_simp; try ring)
      (fun c => by fin_cases c <;> simp [WD1T, jetG] <;> field_simp <;> ring)
      (fun a c => by fin_cases a <;> fin_cases c <;> simp [WD2T, jetG] <;> field_simp <;> ring)
  fin_cases i <;> fin_cases j
  all_goals first | exact h00 | exact h11 | exact h22 | exact h23 | exact h32 | exact h33 | skip
  all_goals refine hz _ _ ?_ ?_ ?_ ?_
  all_goals first | (intro y; simp [gowdyG]; done) | (simp [WGT, WD1T, WD2T]; done)

end GowdyMetric

/-! ### Part 6: the density of the general member, and what follows from it -/

section GowdyHeadline

/-- **The density of the general member**: `*RR = 4e^{2ψ}(WLin + e^{4ψ}WCub)/(e^{4A} R³ |R|)`. -/
noncomputable def gowdyDens (J : GJ) : ℝ :=
  4 * J.ep * (WLin J + J.ep ^ 2 * WCub J) / (J.ea ^ 2 * J.r0 ^ 3 * |J.r0|)

variable {A ψ om R : (Fin 4 → ℝ) → ℝ} (hA : TZ A) (hψ : TZ ψ) (hom : TZ om) (hR : TZ R) (hR0 : ∀ y, R y ≠ 0)

include hA hψ hom hR in
/-- **Part 6, the general unpolarised member**: for ARBITRARY `A, ψ, ω, R` of `(t, z)` (`R` nowhere zero), THE
connection's `*RR` is `gowdyDens` of the 2-jet at the point. -/
theorem gowdy_pontryagin (p : Fin 4 → ℝ) :
    pontryaginLC (gowdyG A ψ om R) (gowdyG_symm A ψ om R) (gowdyG_nondeg hR0) (gowdyG_smooth hA hψ hom hR) p
      = gowdyDens (jetG A ψ om R p) := by
  set J := jetG A ψ om R p
  have Jt := gowdy_jets hA hψ hom hR p
  have hEA : J.ea ≠ 0 := (Real.exp_pos _).ne'
  have hEP : J.ep ≠ 0 := (Real.exp_pos _).ne'
  have hJR : J.r0 ≠ 0 := hR0 p
  have hg : ∀ i j, gowdyG A ψ om R i j p = WGT J i j := fun i j => (Jt i j).v0
  have hinv : ∀ m k, ∑ l, gowdyG A ψ om R m l p * WGiT J l k = if m = k then 1 else 0 := fun m k => by
    simp only [hg]; exact WGiT_ok J hEA hEP hJR m k
  rw [tabs_bridge _ _ _ hg hinv (fun i j c => (Jt i j).d1At c) (fun i j a c => (Jt i j).d2At a c)]
  have hRf : RiemF (WD1T J) (WD2T J) (WGiT J) = WRT J := by funext i j k l; exact WRT_ok J hEA hEP hJR i j k l
  have hdet : (Matrix.of (WGT J)).det = -(J.ea * J.r0) ^ 2 := by
    simp [Matrix.det_succ_row_zero, Fin.sum_univ_succ, WGT,
      show (Fin.succAbove 1 2 : Fin 4) = 3 by decide, show (Fin.succAbove 3 2 : Fin 4) = 2 by decide]
    field_simp; ring
  have hEApos : 0 < J.ea := Real.exp_pos _
  rw [hRf, pontArr, Wcontr_ok J hEA hEP hJR, hdet, neg_neg, Real.sqrt_sq_eq_abs, abs_mul, abs_of_pos hEApos]
  unfold gowdyDens
  have : |J.r0| ≠ 0 := abs_ne_zero.2 hJR
  field_simp; ring

/-- The linear and cubic coefficients of the twist grading. -/
noncomputable def gLin (J : GJ) : ℝ := 4 * J.ep * WLin J / (J.ea ^ 2 * J.r0 ^ 3 * |J.r0|)
noncomputable def gCub (J : GJ) : ℝ := 4 * J.ep ^ 3 * WCub J / (J.ea ^ 2 * J.r0 ^ 3 * |J.r0|)

lemma TZ.const_mul {F : (Fin 4 → ℝ) → ℝ} (hF : TZ F) (ε : ℝ) : TZ (fun y => ε * F y) :=
  ⟨contDiff_const.mul hF.sm, fun y c => by simp [hF.ix], fun y c => by simp [hF.iy]⟩

include hA hψ hom hR in
/-- **The twist grading `ω → εω`**: the density is `ε·gLin + ε³·gCub`, with `gLin`, `gCub` independent of `ε` — only the
powers `1` and `3` of `ε` occur. -/
theorem gowdy_grading (ε : ℝ) (p : Fin 4 → ℝ) :
    pontryaginLC (gowdyG A ψ (fun y => ε * om y) R) (gowdyG_symm _ _ _ _) (gowdyG_nondeg hR0)
        (gowdyG_smooth hA hψ (hom.const_mul ε) hR) p
      = ε * gLin (jetG A ψ om R p) + ε ^ 3 * gCub (jetG A ψ om R p) := by
  rw [gowdy_pontryagin hA hψ (hom.const_mul ε) hR hR0 p]
  have jW := ((hasJ_of hom.sm p).const_mul ε)
  have e1 : ∀ c, pd (fun y => ε * om y) p c = ε * pd om p c := fun c => jW.d1 c
  have e2 : ∀ a c, pdd (fun y => ε * om y) p a c = ε * pdd om p a c := fun a c => jW.d2 a c
  simp only [gowdyDens, gLin, gCub, jetG, e1, e2, WLin, WCub]
  have : |R p| ≠ 0 := abs_ne_zero.2 (hR0 p)
  have := hR0 p
  field_simp
  try ring

/-- `pontryaginLC` sees only the metric (the proofs are irrelevant). -/
lemma pontryaginLC_congr {G G' : Fin 4 → Fin 4 → (Fin 4 → ℝ) → ℝ} (h : G = G') {hs hn hGs hs' hn' hGs'} (p : Fin 4 → ℝ) :
    pontryaginLC G hs hn hGs p = pontryaginLC G' hs' hn' hGs' p := by subst h; rfl

lemma TZ.add_const {F : (Fin 4 → ℝ) → ℝ} (hF : TZ F) (c : ℝ) : TZ (fun y => F y + c) :=
  ⟨hF.sm.add contDiff_const, fun y d => by simp [hF.ix], fun y d => by simp [hF.iy]⟩

lemma TZ.neg {F : (Fin 4 → ℝ) → ℝ} (hF : TZ F) : TZ (fun y => -F y) :=
  ⟨hF.sm.neg, fun y c => by simp [hF.ix], fun y c => by simp [hF.iy]⟩

include hA hψ hom hR in
/-- **`*RR(−ω) = −*RR(ω)`** for arbitrary `A, ψ, ω, R`. -/
theorem gowdy_twist_odd (p : Fin 4 → ℝ) :
    pontryaginLC (gowdyG A ψ (fun y => -om y) R) (gowdyG_symm _ _ _ _) (gowdyG_nondeg hR0)
        (gowdyG_smooth hA hψ hom.neg hR) p
      = -pontryaginLC (gowdyG A ψ om R) (gowdyG_symm A ψ om R) (gowdyG_nondeg hR0) (gowdyG_smooth hA hψ hom hR) p := by
  rw [pontryaginLC_congr (G' := gowdyG A ψ (fun y => -1 * om y) R) (by funext i j y; simp [neg_one_mul])
      (hs' := gowdyG_symm _ _ _ _) (hn' := gowdyG_nondeg hR0) (hGs' := gowdyG_smooth hA hψ (hom.const_mul (-1)) hR),
    gowdy_grading hA hψ hom hR hR0, pontryaginLC_congr (G' := gowdyG A ψ (fun y => 1 * om y) R) (by funext i j y; simp)
      (hs' := gowdyG_symm _ _ _ _) (hn' := gowdyG_nondeg hR0) (hGs' := gowdyG_smooth hA hψ (hom.const_mul 1) hR),
    gowdy_grading hA hψ hom hR hR0]
  ring

include hA hψ hR in
/-- **`*RR ≡ 0` at constant `ω`** (P11's polarised cut, and every constant shear of it), for arbitrary `A, ψ, R`. -/
theorem gowdy_const_twist (om₀ : ℝ) (p : Fin 4 → ℝ) :
    pontryaginLC (gowdyG A ψ (fun _ => om₀) R) (gowdyG_symm _ _ _ _) (gowdyG_nondeg hR0)
      (gowdyG_smooth hA hψ ⟨contDiff_const, fun _ _ => rfl, fun _ _ => rfl⟩ hR) p = 0 := by
  rw [gowdy_pontryagin hA hψ ⟨contDiff_const, fun _ _ => rfl, fun _ _ => rfl⟩ hR hR0 p]
  simp [gowdyDens, jetG, pd, pdd, WLin, WCub]

include hA hψ hom hR in
/-- **Bare `ω` never appears**: shifting `ω` by a constant does not change the density. -/
theorem gowdy_shift (c : ℝ) (p : Fin 4 → ℝ) :
    pontryaginLC (gowdyG A ψ (fun y => om y + c) R) (gowdyG_symm _ _ _ _) (gowdyG_nondeg hR0)
        (gowdyG_smooth hA hψ (hom.add_const c) hR) p
      = pontryaginLC (gowdyG A ψ om R) (gowdyG_symm A ψ om R) (gowdyG_nondeg hR0) (gowdyG_smooth hA hψ hom hR) p := by
  rw [gowdy_pontryagin hA hψ (hom.add_const c) hR hR0, gowdy_pontryagin hA hψ hom hR hR0]
  have hf : fderiv ℝ (fun y => om y + c) = fderiv ℝ om := funext fun x => fderiv_add_const c
  have e1 : ∀ d, pd (fun y => om y + c) p d = pd om p d := fun d => by simp only [pd, hf]
  have e2 : ∀ a d, pdd (fun y => om y + c) p a d = pdd om p a d := fun a d => by simp only [pdd, hf]
  simp only [gowdyDens, jetG, e1, e2, WLin, WCub]

end GowdyHeadline

/-! ### The explicit member `(A, ψ, ω, R) = (t/3, z/5, c t z, t)` -/

section GowdyMember

/-- The member, with `R = ρ(t)` (row 96's global profile, `= t` for `t ≥ 3/2`). -/
noncomputable def mA : (Fin 4 → ℝ) → ℝ := fun y => 1 / 3 * y 0
noncomputable def mψ : (Fin 4 → ℝ) → ℝ := fun y => 1 / 5 * y 1
noncomputable def mom (c : ℝ) : (Fin 4 → ℝ) → ℝ := fun y => c * (y 0 * y 1)
noncomputable def mR : (Fin 4 → ℝ) → ℝ := fun y => rho (y 0)

lemma tz_of {F : (Fin 4 → ℝ) → ℝ} (hF : ContDiff ℝ ∞ F) (h : ∀ y y' : Fin 4 → ℝ, y 0 = y' 0 → y 1 = y' 1 → F y = F y') : TZ F :=
  ⟨hF, fun y c => h _ _ (by simp) (by simp), fun y c => h _ _ (by simp) (by simp)⟩

lemma mA_tz : TZ mA := tz_of (by unfold mA; fun_prop) fun y y' h0 h1 => by simp [mA, h0]
lemma mψ_tz : TZ mψ := tz_of (by unfold mψ; fun_prop) fun y y' h0 h1 => by simp [mψ, h1]
lemma mom_tz (c : ℝ) : TZ (mom c) := tz_of (by unfold mom; fun_prop) fun y y' h0 h1 => by simp [mom, h0, h1]
lemma mR_tz : TZ mR := tz_of (rho_smooth.comp (contDiff_apply ℝ ℝ 0)) fun y y' h0 h1 => by simp [mR, h0]
lemma mR_ne : ∀ y, mR y ≠ 0 := fun y => rho_ne _

/-- **Its density** at a point with `t > 3/2`:
`*RR = 4e^{2z/5}(c·Lm + c³e^{4z/5}·Cm)/(e^{4t/3} t⁴)` with the receipt's polynomials `Lm`, `Cm`. -/
noncomputable def memLin (t z : ℝ) : ℝ := -t * (-120 * t ^ 3 + 64 * t ^ 2 * z + 340 * t ^ 2 - 300 * t * z - 375 * t - 225 * z) / 1125
noncomputable def memCub (t z : ℝ) : ℝ := -t * (-5 * t ^ 3 - 9 * t ^ 2 * z + 5 * t * z ^ 2 + 9 * z ^ 3 + 30 * z ^ 2) / 15

lemma jet_member (c : ℝ) {p : Fin 4 → ℝ} (hp : 3 / 2 < p 0) :
    jetG mA mψ (mom c) mR p = ⟨Real.exp (2 * (1 / 3 * p 0)), Real.exp (2 * (1 / 5 * p 1)), 1 / 3, 0, 0, 0, 0, 0, 1 / 5,
      0, 0, 0, c * (p 0 * p 1), c * p 1, c * p 0, 0, c, 0, p 0, 1, 0, 0, 0, 0⟩ := by
  have jA : HasJ mA p _ _ _ := (hasJ_coord 0 p).const_mul (1 / 3)
  have jP : HasJ mψ p _ _ _ := (hasJ_coord 1 p).const_mul (1 / 5)
  have jW : HasJ (mom c) p _ _ _ := ((hasJ_coord 0 p).mul (hasJ_coord 1 p)).const_mul c
  have jR : HasJ mR p (p 0) _ _ := (hasJ_coord 0 p).congr
    (Filter.mem_of_superset ((isOpen_lt continuous_const (continuous_apply 0)).mem_nhds hp)
      fun y (hy : 3 / 2 < y 0) => rho_eq hy.le)
  simp only [jetG, pd, pdd, jA.d1, jA.d2, jP.d1, jP.d2, jW.d1, jW.d2, jR.d1, jR.d2, jR.v0]
  simp [mA, mψ, mom]

theorem member_pontryagin (c : ℝ) {p : Fin 4 → ℝ} (hp : 3 / 2 < p 0) :
    pontryaginLC ((gowdyG mA mψ (mom c) mR)) (gowdyG_symm _ _ _ _) (gowdyG_nondeg mR_ne) (gowdyG_smooth mA_tz mψ_tz (mom_tz c) mR_tz) p
      = 4 * Real.exp (2 * (1 / 5 * p 1)) * (c * memLin (p 0) (p 1) + c ^ 3 * Real.exp (2 * (1 / 5 * p 1)) ^ 2 * memCub (p 0) (p 1))
        / (Real.exp (2 * (1 / 3 * p 0)) ^ 2 * p 0 ^ 4) := by
  rw [gowdy_pontryagin mA_tz mψ_tz (mom_tz c) mR_tz mR_ne p, jet_member c hp]
  have h0 : 0 < p 0 := by linarith
  simp only [gowdyDens, WLin, WCub, memLin, memCub, abs_of_pos h0]
  field_simp; ring

/-- **Odd in `c`**, and **zero at `c = 0`**. -/
theorem member_odd (c : ℝ) {p : Fin 4 → ℝ} (hp : 3 / 2 < p 0) :
    pontryaginLC ((gowdyG mA mψ (mom (-c)) mR)) (gowdyG_symm _ _ _ _) (gowdyG_nondeg mR_ne) (gowdyG_smooth mA_tz mψ_tz (mom_tz _) mR_tz) p
      = -pontryaginLC ((gowdyG mA mψ (mom c) mR)) (gowdyG_symm _ _ _ _) (gowdyG_nondeg mR_ne) (gowdyG_smooth mA_tz mψ_tz (mom_tz c) mR_tz) p := by
  rw [member_pontryagin _ hp, member_pontryagin _ hp]; ring

theorem member_zero {p : Fin 4 → ℝ} (hp : 3 / 2 < p 0) :
    pontryaginLC ((gowdyG mA mψ (mom 0) mR)) (gowdyG_symm _ _ _ _) (gowdyG_nondeg mR_ne) (gowdyG_smooth mA_tz mψ_tz (mom_tz 0) mR_tz) p = 0 := by
  rw [member_pontryagin _ hp]; ring

/-- The point `t = 2`, `z = x = y = 0`. -/
def p2 : Fin 4 → ℝ := ![2, 0, 0, 0]

lemma memLin_p2 : memLin 2 0 = 28 / 45 := by norm_num [memLin]
lemma memCub_p2 : memCub 2 0 = 16 / 3 := by norm_num [memCub]

/-- **Nonzero for every `c ≠ 0`** (at `t = 2`, `z = 0`). -/
theorem member_ne {c : ℝ} (hc : c ≠ 0) :
    pontryaginLC ((gowdyG mA mψ (mom c) mR)) (gowdyG_symm _ _ _ _) (gowdyG_nondeg mR_ne) (gowdyG_smooth mA_tz mψ_tz (mom_tz c) mR_tz) p2 ≠ 0 := by
  rw [member_pontryagin c (by norm_num [p2])]
  simp only [p2, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.head_cons, memLin_p2, memCub_p2]
  have : c * (28 / 45) + c ^ 3 * Real.exp (2 * (1 / 5 * 0)) ^ 2 * (16 / 3) ≠ 0 := by
    simp only [mul_zero, Real.exp_zero, one_pow, mul_one]
    have : c * (28 / 45 + c ^ 2 * (16 / 3)) ≠ 0 := mul_ne_zero hc (by positivity)
    convert this using 1; ring
  have := Real.exp_pos (2 * (1 / 5 * (0 : ℝ))); have := Real.exp_pos (2 * (1 / 3 * (2 : ℝ)))
  positivity

/-- **Exactly the powers `{1, 3}`**: on the member both grading coefficients are nonzero (at `t = 2`, `z = 0`, `c = 1`),
so neither power is absent from the general density. -/
theorem grading_exact :
    gLin (jetG mA mψ (mom 1) mR p2) ≠ 0 ∧ gCub (jetG mA mψ (mom 1) mR p2) ≠ 0 := by
  rw [jet_member 1 (by norm_num [p2])]
  simp only [gLin, gCub, WLin, WCub, p2, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.head_cons]
  have := Real.exp_pos (2 * (1 / 3 * (2 : ℝ)))
  constructor <;> norm_num <;> positivity

end GowdyMember

#print axioms ShadowProbe.R89Pontryagin.gowdy_pontryagin
#print axioms ShadowProbe.R89Pontryagin.gowdy_grading
#print axioms ShadowProbe.R89Pontryagin.gowdy_twist_odd
#print axioms ShadowProbe.R89Pontryagin.gowdy_const_twist
#print axioms ShadowProbe.R89Pontryagin.gowdy_shift
#print axioms ShadowProbe.R89Pontryagin.member_pontryagin
#print axioms ShadowProbe.R89Pontryagin.member_odd
#print axioms ShadowProbe.R89Pontryagin.member_zero
#print axioms ShadowProbe.R89Pontryagin.member_ne
#print axioms ShadowProbe.R89Pontryagin.grading_exact

/-! ## Part 8: the Chern–Simons current on the member, as a corollary of campaign 43's transgression -/

section Part8

/-- `∂_μK^μ` of the member's Chern–Simons current (row 96's `csLC`) at `p`. -/
noncomputable def divK (c : ℝ) (p : Fin 4 → ℝ) : ℝ :=
  ∑ μ, fderiv ℝ (fun y => csLC ((gowdyG mA mψ (mom c) mR)) (gowdyG_symm _ _ _ _) (gowdyG_nondeg mR_ne)
    (gowdyG_smooth mA_tz mψ_tz (mom_tz c) mR_tz) y μ) p (Pi.single μ 1)

lemma member_det (c : ℝ) (p : Fin 4 → ℝ) : (gm ((gowdyG mA mψ (mom c) mR)) p).det < 0 := by
  rw [gowdyG_det]
  have := Real.exp_pos (2 * mA p); have := mR_ne p
  have : 0 < Real.exp (2 * mA p) ^ 2 * mR p ^ 2 := by positivity
  linarith

/-- **`∂_μK^μ = −√−g *RR` on the member**, everywhere (campaign 43's `transgression`). -/
theorem member_transgression (c : ℝ) (p : Fin 4 → ℝ) :
    divK c p = -(Real.sqrt (-(gm ((gowdyG mA mψ (mom c) mR)) p).det) * pontryaginLC ((gowdyG mA mψ (mom c) mR)) (gowdyG_symm _ _ _ _) (gowdyG_nondeg mR_ne)
      (gowdyG_smooth mA_tz mψ_tz (mom_tz c) mR_tz) p) :=
  transgression _ _ _ p (member_det c p)

/-- **The receipt's ratio**: `∂_μK^μ / (√−g *RR) = −1` on the twisted member (`c ≠ 0`, at `t = 2`, `z = 0`), as a
corollary of campaign 43's `ratio_neg_one`. -/
theorem member_ratio {c : ℝ} (hc : c ≠ 0) :
    divK c p2 / (Real.sqrt (-(gm ((gowdyG mA mψ (mom c) mR)) p2).det) * pontryaginLC ((gowdyG mA mψ (mom c) mR)) (gowdyG_symm _ _ _ _) (gowdyG_nondeg mR_ne)
      (gowdyG_smooth mA_tz mψ_tz (mom_tz c) mR_tz) p2) = -1 :=
  ratio_neg_one _ _ _ p2 (member_det c p2) (member_ne hc)

/-- `∂_μK^μ` is nonzero on the twisted member. -/
theorem member_divK_ne {c : ℝ} (hc : c ≠ 0) : divK c p2 ≠ 0 := by
  rw [member_transgression]
  have hs : Real.sqrt (-(gm ((gowdyG mA mψ (mom c) mR)) p2).det) ≠ 0 := (Real.sqrt_pos.2 (by linarith [member_det c p2])).ne'
  exact neg_ne_zero.2 (mul_ne_zero hs (member_ne hc))

/-- **`∂K` is odd in `c`**, at every point with `t > 3/2` (`√−g` does not see `ω`). -/
theorem member_divK_odd (c : ℝ) {p : Fin 4 → ℝ} (hp : 3 / 2 < p 0) : divK (-c) p = -divK c p := by
  rw [member_transgression, member_transgression, member_odd c hp]
  have : (gm ((gowdyG mA mψ (mom (-c)) mR)) p).det = (gm ((gowdyG mA mψ (mom c) mR)) p).det := by rw [gowdyG_det, gowdyG_det]
  rw [this]; ring

end Part8

#print axioms ShadowProbe.R89Pontryagin.member_transgression
#print axioms ShadowProbe.R89Pontryagin.member_ratio
#print axioms ShadowProbe.R89Pontryagin.member_divK_ne
#print axioms ShadowProbe.R89Pontryagin.member_divK_odd

end R89Pontryagin

end ShadowProbe

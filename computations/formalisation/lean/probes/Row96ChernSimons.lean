import ShadowEngine
import Mathlib.MeasureTheory.Integral.IntervalIntegral.FundThmCalculus
import Mathlib.MeasureTheory.Integral.DivergenceTheorem
import Mathlib.LinearAlgebra.Matrix.Permutation
import Mathlib.Analysis.SpecialFunctions.SmoothTransition

/-! # Campaign 42 (`r7443+71.26`): row 96, the history is spherically symmetric, so the Chern–Simons number never moves

The receipt is `P15_the_history_is_spherically_symmetric_throughout_so_the_chern_simons_number_never_moves.py`. It
`exec`s `christoffels`, `pontryagin` and `cs_current` from
`P14_the_constituent_count_is_conserved_on_every_static_member_and_the_twist_alone_violates_it.py`.

**The exact definitions.**
* `eps4`: the `Fin 4` Levi-Civita symbol, `ε₀₁₂₃ = +1` (= the receipt's `EPS`, `eps4_det`).
* THE connection: the engine's `lcConn` (Levi-Civita connection of `Σ Gᵢⱼ dxᵢ dxⱼ` on `ℝ⁴`, `G` smooth, symmetric,
  nondegenerate everywhere). `chrLC … y i j k = (∇_{∂ᵢ}∂ⱼ)ᵏ = Γᵏᵢⱼ`; `riemLC … p i j k l = (R(∂ᵢ,∂ⱼ)∂ₖ)ˡ = Rˡ_{kij}`.
* **The density** `pontryaginLC`: `*RR = ½ Σ ε^{mnrs} Σ_{ab} R_{mnab} R_{rs}{}^{ab} / √(−det g)` with
  `R_{mnab} = g_{ms}R^s_{nab}`, `R_{rs}{}^{ab} = g^{aα}g^{bβ}R_{rsαβ}` (the receipt's `pontryagin`).
* **The current** `csLC`: `K^μ = 2 Σ ε^{μνρσ}(Σ_{ab} Γᵃ_{νb} ∂_ρΓᵇ_{σa} + ⅔ Σ_{abc} Γᵃ_{νb}Γᵇ_{ρc}Γᶜ_{σa})` on THE
  connection's `Γ` and the Fréchet partials of `y ↦ Γ(y)` (the receipt's `cs_current`). `riemLC_tab`, `csLC_tab`:
  both are the coordinate recipe (`GamF`, `DGamF`, `RiemF`) on the metric's first two partials at the point.
* **Caveat (registered):** the density and the current are the receipt's COORDINATE formulas on THE connection of the
  coordinate metric. Their covariance (tensoriality of `*RR`, the transformation law of `K`) is NOT proved, nor is the
  general transgression identity; `∂_μK^μ = −√−g *RR` is proved on the receipt's member only.

**What is proved.**
* *Structure.* `pontryagin_parity` / `cs_parity`: if the coordinates in a set `P` do not mix with the others and the
  metric does not depend on them, `*RR = 0` when `|P|` is odd and `K^μ = 0` when `[μ ∈ P] ≠ |P| mod 2`.
  `warped_pontryagin` / `warped_cs`: on any metric of the warped shape (`Warped`) `*RR ≡ 0` and ALL FOUR `K^μ ≡ 0`;
  `K^φ` (not reached by `φ`-parity) by `csArr_three`: a second, partial `θ`-parity on the `(t, r, θ)` block plus the
  symmetry of `∂_ρΓ^φ_{σφ}`.
* *Part 1.* `nariai_pontryagin_zero`, `nariai_rotated_pontryagin_zero` (and `nariai_general_pontryagin_zero` for any
  `a(χ), b(χ), c(θ), e(θ), w`): sympy-generated tables, proved layer by layer.
* *Part 2.* `polarised_pontryagin_zero` (`A, ψ, R` arbitrary of `(t, z)`); `unpolarised_nonzero`; row 69's plane-wave
  facts re-derived (`gowdy_pontryagin`, `gowdy_plane_wave_pontryagin`, `gowdy_areal_pontryagin`, `gowdy_areal_silenced`).
* *Part 3.* `gowdy_cs` (the current of the plane-wave Gowdy metric, any profiles); on the member
  `gowdy(0, log(t − z), t − z, t)`: `member_cs` (`K^t = −12u/t`, `K^z = −2u(5t+z)/t²`, `K^x = K^y = 0`),
  `member_pontryagin` (`√−g *RR = −8u/t²`), `member_divergence` (`∂_tK^t + ∂_zK^z = −√−g *RR`), `member_stokes`
  (Mathlib's `integral2_divergence_prod_of_hasFDerivAt_off_countable`: volume integral = minus the boundary flux),
  `member_volume` (`= 8/15 − 8 log(5/3) = log(6561/390625) + 8/15 < 0`).
* *Part 4.* `sph_pontryagin_zero`, `sph_cs_zero`: the general dynamic spherically symmetric metric (`A, B, C, S`
  arbitrary smooth functions of `(t, r)`, `dt dr` term kept), `*RR ≡ 0` and `K^t = K^r = K^θ = K^φ ≡ 0`.
* *Part 6.* `net_count`.

**Profiles.** The engine needs `G` smooth and nondegenerate on all of `ℝ⁴`, so `sin²θ`, `1 − χ²`, `log(t − z)`, `R = t`
enter as smooth global profiles agreeing with them where the receipt evaluates (arbitrary nowhere-zero `h(θ)` in Part
4; positive `f, h` in Part 1; the explicit `rho`, `psiM` in Part 3, equal to `t`, `log u` for arguments `≥ 3/2`).
The seven paper-text checks are not formalised. -/

-- The layer lemmas are closed by ONE uniform tactic per layer, run on every index; on some indices a step of it is
-- idle. These linters report that idleness, not a gap.
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

namespace R96ChernSimons

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
(`eps4_sign`). -/
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

/-- **The bridge.** The density is the receipt's coordinate recipe: `pontArr` on the engine's closed form `curvG`,
with the inverse given only at the point. -/
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

/-- And conversely: an invertible matrix at every point is a nondegenerate form. -/
lemma nondeg_of_det (hd : ∀ p, (gm G p).det ≠ 0) (p : Fin 4 → ℝ) (u : Fin 4 → ℝ)
    (h : ∀ v, formG G p u v = 0) : u = 0 := by
  refine Matrix.eq_zero_of_vecMul_eq_zero (hd p) (funext fun j => ?_)
  have := h (Pi.single j 1)
  rw [formG_apply] at this
  simpa [Matrix.vecMul, dotProduct, gm, Pi.single_apply, mul_comm] using this

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

include hn hGs in
/-- **The bridge for the current**: `csLC` is the table recipe, with the inverse at the point. -/
theorem csLC_tab (p : Fin 4 → ℝ) (μ : Fin 4) :
    csLC G hs hn hGs p μ = csArr (GamF (d1At G p) (gmi G p)) (DGamF (d1At G p) (d2At G p) (gmi G p)) μ := by
  have hinv := gm_hinv hn p
  have h1 : chrLC G hs hn hGs p = GamF (d1At G p) (gmi G p) := by
    funext i j k; rw [chrLC_eq hs hn hGs, lcGam_formG hn hGs hinv, gamG_basis]
  have h2 : (fun u i j k => fderiv ℝ (fun y => chrLC G hs hn hGs y i j k) p (Pi.single u 1))
      = DGamF (d1At G p) (d2At G p) (gmi G p) := by
    funext u i j k
    have hd : DifferentiableAt ℝ (fun y => lcGam (formG G) y (Pi.single i 1) (Pi.single j 1)) p :=
      ((lcGam_differentiable hn hGs p).clm_apply (differentiableAt_const _)).clm_apply (differentiableAt_const _)
    have hc : HasFDerivAt (fun y => lcGam (formG G) y (Pi.single i 1) (Pi.single j 1) k)
        ((ContinuousLinearMap.proj k).comp (fderiv ℝ (fun y => lcGam (formG G) y (Pi.single i 1) (Pi.single j 1)) p)) p :=
      (ContinuousLinearMap.proj (R := ℝ) (φ := fun _ : Fin 4 => ℝ) k).hasFDerivAt.comp p hd.hasFDerivAt
    simp only [chrLC_eq hs hn hGs]
    rw [hc.fderiv]
    simp only [ContinuousLinearMap.comp_apply, ContinuousLinearMap.proj_apply]
    rw [fderiv_lcGam_formG hn hGs hinv, DgamG_basis]
  rw [csLC, h1, h2]

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

/-- **The current's `μ` component vanishes** when `Γ` and `∂Γ` have `P`-parity and `μ`'s membership in `P` differs
from the parity of `P` over all four coordinates. -/
theorem csArr_par {Γ : Fin 4 → Fin 4 → Fin 4 → ℝ} {DΓ : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ}
    (hΓ : ∀ i j k, pb P [i, j, k] = true → Γ i j k = 0) (hD : ∀ u i j k, pb P [u, i, j, k] = true → DΓ u i j k = 0)
    (μ : Fin 4) (hμ : xor (P μ) (pb P [0, 1, 2, 3]) = true) : csArr Γ DΓ μ = 0 := by
  rw [csArr, Finset.sum_eq_zero fun ν _ => Finset.sum_eq_zero fun ρ _ => Finset.sum_eq_zero fun σ _ => ?_, mul_zero]
  by_cases he : eps4 μ ν ρ σ = 0
  · simp [he]
  have hp := eps4_pb P he
  have h3 : pb P [ν, ρ, σ] = true := by
    revert hp hμ; simp only [pb, Bool.xor_false]
    cases P μ <;> cases P ν <;> cases P ρ <;> cases P σ <;> cases P 0 <;> cases P 1 <;> cases P 2 <;> cases P 3 <;>
      decide
  have q : ∑ a, ∑ b, Γ ν b a * DΓ ρ σ a b = 0 :=
    Finset.sum_eq_zero fun a _ => Finset.sum_eq_zero fun b _ => by
      by_cases hb : pb P [ν, b, a] = true
      · rw [hΓ _ _ _ hb, zero_mul]
      · have : pb P [ρ, σ, a, b] = true := by
          revert h3 hb; simp only [pb, Bool.xor_false]
          cases P ν <;> cases P ρ <;> cases P σ <;> cases P a <;> cases P b <;> decide
        rw [hD _ _ _ _ this, mul_zero]
  have c : ∑ a, ∑ b, ∑ c, Γ ν b a * Γ ρ c b * Γ σ a c = 0 :=
    Finset.sum_eq_zero fun a _ => Finset.sum_eq_zero fun b _ => Finset.sum_eq_zero fun c _ => by
      by_cases hb : pb P [ν, b, a] = true
      · rw [hΓ _ _ _ hb]; ring
      by_cases hc : pb P [ρ, c, b] = true
      · rw [hΓ _ _ _ hc]; ring
      have : pb P [σ, a, c] = true := by
        revert h3 hb hc; simp only [pb, Bool.xor_false]
        cases P ν <;> cases P ρ <;> cases P σ <;> cases P a <;> cases P b <;> cases P c <;> decide
      rw [hΓ _ _ _ this, mul_zero]
  rw [q, c]; ring

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

lemma d2At_symm (hGs : ∀ i j, ContDiff ℝ ∞ (G i j)) (p : Fin 4 → ℝ) (i j a c : Fin 4) :
    d2At G p i j a c = d2At G p i j c a :=
  (hGs i j).contDiffAt.isSymmSndFDerivAt (by simp) _ _

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

include hn hGs in
/-- **The parity theorem for the current.** Same hypotheses: `K^μ = 0` whenever `μ`'s membership in `P` differs from
the parity of `P` over all four coordinates. -/
theorem cs_parity (P : Fin 4 → Bool) (hz : ∀ i j, pb P [i, j] = true → ∀ y, G i j y = 0)
    (hI : ∀ k, P k = true → ∀ i j y (c : ℝ), G i j (y + c • Pi.single k 1) = G i j y)
    (μ : Fin 4) (hμ : xor (P μ) (pb P [0, 1, 2, 3]) = true) (p : Fin 4 → ℝ) : csLC G hs hn hGs p μ = 0 := by
  have T := tabPar_of P hn hGs hz hI p
  rw [csLC_tab hs hn hGs]
  exact csArr_par (fun i j k h => GamF_par T h) (fun u i j k h => DGamF_par T h) μ hμ

end Parity

/-! ## The warped class: `K^φ` by a second, partial parity -/

section Warped

/-- The coordinate `φ = x³`, and the coordinate `θ = x²`. -/
def Pph : Fin 4 → Bool := fun i => decide (i = 3)
def Pth : Fin 4 → Bool := fun i => decide (i = 2)

lemma sum_eps3 (f : Fin 4 → Fin 4 → Fin 4 → ℝ) :
    ∑ ν, ∑ ρ, ∑ σ, (eps4 3 ν ρ σ : ℝ) * f ν ρ σ
      = -f 0 1 2 + f 0 2 1 + f 1 0 2 - f 1 2 0 - f 2 0 1 + f 2 1 0 := by
  simp [Fin.sum_univ_four, eps4, show Int.sign 2 = 1 from rfl, show Int.sign 3 = 1 from rfl]
  ring1

/-- **The `K^φ` lemma on arrays.** If `Γ` has `φ`-parity, its `(t, r, θ)` block has `θ`-parity, the `(t, r, θ)` block of
`∂Γ` has `θ`-parity (derivative slot included), and `∂_ρ Γ^φ_{σφ}` is symmetric in `ρσ`, then `K^φ = 0`: the
`a = b = φ` terms cancel by that symmetry, the all-`φ` cubic terms by antisymmetry, and every other term has an odd
factor. -/
lemma csArr_three {Γ : Fin 4 → Fin 4 → Fin 4 → ℝ} {DΓ : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ}
    (h1 : ∀ ν b a, pb Pph [ν, b, a] = true → Γ ν b a = 0)
    (h3 : ∀ ν b a, ν ≠ 3 → b ≠ 3 → a ≠ 3 → pb Pth [ν, b, a] = true → Γ ν b a = 0)
    (h4 : ∀ ρ σ a b, ρ ≠ 3 → σ ≠ 3 → a ≠ 3 → b ≠ 3 → pb Pth [ρ, σ, a, b] = true → DΓ ρ σ a b = 0)
    (h5 : ∀ ρ σ, DΓ ρ σ 3 3 = DΓ σ ρ 3 3) : csArr Γ DΓ 3 = 0 := by
  rw [csArr, sum_eps3]
  simp only [Fin.sum_univ_four]
  simp (disch := decide) only [h1, h3, h4, zero_mul, mul_zero, add_zero, zero_add]
  rw [h5 2 1, h5 2 0, h5 1 0]; ring

variable {gi : Fin 4 → Fin 4 → ℝ} {d1 : Fin 4 → Fin 4 → Fin 4 → ℝ} {d2 : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ}

lemma GamF_rpar (hgi : ∀ i j, pb Pth [i, j] = true → gi i j = 0) (hgi3 : ∀ l, l ≠ 3 → gi 3 l = 0)
    (hd1 : ∀ x y z, x ≠ 3 → y ≠ 3 → pb Pth [x, y, z] = true → d1 x y z = 0)
    {i j k : Fin 4} (hi : i ≠ 3) (hj : j ≠ 3) (hk : k ≠ 3) (h : pb Pth [i, j, k] = true) : GamF d1 gi i j k = 0 := by
  refine Finset.sum_eq_zero fun l _ => ?_
  by_cases l3 : l = 3
  · subst l3; rw [hgi3 k hk, mul_zero]
  by_cases hl : pb Pth [l, k] = true
  · rw [hgi _ _ hl, mul_zero]
  have e : pb Pth [j, l, i] = true ∧ pb Pth [l, i, j] = true ∧ pb Pth [i, j, l] = true := by
    revert h hl; simp only [pb, Bool.xor_false]
    cases Pth i <;> cases Pth j <;> cases Pth k <;> cases Pth l <;> decide
  rw [hd1 _ _ _ hj l3 e.1, hd1 _ _ _ l3 hi e.2.1, hd1 _ _ _ hi hj e.2.2]; ring

lemma DGamF_rpar (hgi : ∀ i j, pb Pth [i, j] = true → gi i j = 0) (hgi3 : ∀ l, l ≠ 3 → gi 3 l = 0)
    (hd1 : ∀ x y z, x ≠ 3 → y ≠ 3 → pb Pth [x, y, z] = true → d1 x y z = 0)
    (hd1' : ∀ l u, l ≠ 3 → d1 3 l u = 0)
    (hd2 : ∀ x y a c, x ≠ 3 → y ≠ 3 → pb Pth [x, y, a, c] = true → d2 x y a c = 0)
    {u i j k : Fin 4} (hi : i ≠ 3) (hj : j ≠ 3) (hk : k ≠ 3) (h : pb Pth [u, i, j, k] = true) :
    DGamF d1 d2 gi u i j k = 0 := by
  refine Finset.sum_eq_zero fun l _ => ?_
  by_cases l3 : l = 3
  · subst l3; rw [hgi3 k hk, mul_zero]
  by_cases hl : pb Pth [l, k] = true
  · rw [hgi _ _ hl, mul_zero]
  have e : pb Pth [j, l, u, i] = true ∧ pb Pth [l, i, u, j] = true ∧ pb Pth [i, j, u, l] = true := by
    revert h hl; simp only [pb, Bool.xor_false]
    cases Pth u <;> cases Pth i <;> cases Pth j <;> cases Pth k <;> cases Pth l <;> decide
  have hs : ∑ m, d1 m l u * GamF d1 gi i j m = 0 := Finset.sum_eq_zero fun m _ => by
    by_cases m3 : m = 3
    · subst m3; rw [hd1' l u l3, zero_mul]
    by_cases hm : pb Pth [m, l, u] = true
    · rw [hd1 _ _ _ m3 l3 hm, zero_mul]
    · have : pb Pth [i, j, m] = true := by
        revert h hl hm; simp only [pb, Bool.xor_false]
        cases Pth u <;> cases Pth i <;> cases Pth j <;> cases Pth k <;> cases Pth l <;> cases Pth m <;> decide
      rw [GamF_rpar hgi hgi3 hd1 hi hj m3 this, mul_zero]
  rw [hd2 _ _ _ _ hj l3 e.1, hd2 _ _ _ _ l3 hi e.2.1, hd2 _ _ _ _ hi hj e.2.2, hs]; ring

/-- `∂_ρ Γ^φ_{σφ} = (½ ∂_ρ∂_σ g_φφ − ½ ∂_ρ g_φφ ∂_σ g_φφ g^{φφ}) g^{φφ}`, symmetric in `ρσ`. -/
lemma DGamF_33 (hgi : ∀ l, l ≠ 3 → gi l 3 = 0) (hd1m : ∀ m u, m ≠ 3 → d1 m 3 u = 0)
    (hd1d : ∀ x y, d1 x y 3 = 0) (hd2d : ∀ x y a, d2 x y a 3 = 0) (hsym : ∀ a c, d2 3 3 a c = d2 3 3 c a)
    (ρ σ : Fin 4) : DGamF d1 d2 gi ρ σ 3 3 = DGamF d1 d2 gi σ ρ 3 3 := by
  have key : ∀ ρ σ, DGamF d1 d2 gi ρ σ 3 3
      = (d2 3 3 ρ σ / 2 - d1 3 3 ρ * (d1 3 3 σ / 2 * gi 3 3)) * gi 3 3 := by
    intro ρ σ
    simp only [DGamF, GamF, Fin.sum_univ_four, hgi 0 (by decide), hgi 1 (by decide), hgi 2 (by decide),
      hd1m 0 _ (by decide), hd1m 1 _ (by decide), hd1m 2 _ (by decide), hd1d, hd2d]
    ring
  rw [key, key, hsym]; ring

variable {G : Fin 4 → Fin 4 → (Fin 4 → ℝ) → ℝ} (hs : ∀ i j p, G i j p = G j i p)
  (hn : ∀ p (u : Fin 4 → ℝ), (∀ v, formG G p u v = 0) → u = 0) (hGs : ∀ i j, ContDiff ℝ ∞ (G i j))

/-- **The warped structure**: `φ = x³` does not mix and nothing depends on it; `θ = x²` does not mix with `(x⁰, x¹)`;
and every entry but `g_φφ` is independent of `θ`. -/
structure Warped (G : Fin 4 → Fin 4 → (Fin 4 → ℝ) → ℝ) : Prop where
  zφ : ∀ i j, pb Pph [i, j] = true → ∀ y, G i j y = 0
  zθ : ∀ i j, pb Pth [i, j] = true → ∀ y, G i j y = 0
  iφ : ∀ i j y (c : ℝ), G i j (y + c • Pi.single 3 1) = G i j y
  iθ : ∀ i j, i ≠ 3 → j ≠ 3 → ∀ y (c : ℝ), G i j (y + c • Pi.single 2 1) = G i j y

lemma Warped.iP (W : Warped G) : ∀ k, Pph k = true → ∀ i j y (c : ℝ), G i j (y + c • Pi.single k 1) = G i j y := by
  intro k hk
  have : k = 3 := by simpa [Pph] using hk
  subst this; exact W.iφ

include hn hGs in
/-- **On the warped class `*RR ≡ 0`** (the `φ`-parity theorem). -/
theorem warped_pontryagin (W : Warped G) (p : Fin 4 → ℝ) : pontryaginLC G hs hn hGs p = 0 :=
  pontryagin_parity hs hn hGs Pph W.zφ W.iP (by decide) p

include hn hGs in
/-- **On the warped class every component of the Chern–Simons current vanishes**: `K^t, K^r, K^θ` by `φ`-parity,
`K^φ` by `csArr_three`. -/
theorem warped_cs (W : Warped G) (p : Fin 4 → ℝ) (μ : Fin 4) : csLC G hs hn hGs p μ = 0 := by
  by_cases hμ : μ = 3
  swap
  · exact cs_parity hs hn hGs Pph W.zφ W.iP μ (by revert hμ; fin_cases μ <;> decide) p
  subst hμ
  have T := tabPar_of Pph hn hGs W.zφ W.iP p
  rw [csLC_tab hs hn hGs]
  have hgiθ := inv_par Pth (gm G p) fun i j h => W.zθ i j h p
  have hgi3 : ∀ l, l ≠ 3 → (gm G p)⁻¹ 3 l = 0 := fun l hl => T.gi0 3 l (by revert hl; fin_cases l <;> decide)
  have hgi3' : ∀ l, l ≠ 3 → (gm G p)⁻¹ l 3 = 0 := fun l hl => T.gi0 l 3 (by revert hl; fin_cases l <;> decide)
  have hd1 : ∀ x y z, x ≠ 3 → y ≠ 3 → pb Pth [x, y, z] = true → d1At G p x y z = 0 := by
    intro x y z hx hy h
    by_cases hz : z = 2
    · subst hz; exact d1At_indep hGs (W.iθ x y hx hy) p
    · have : pb Pth [x, y] = true := by simpa [pb, Pth, hz] using h
      exact d1At_zero (W.zθ x y this) p z
  have hd1' : ∀ l u, l ≠ 3 → d1At G p 3 l u = 0 := fun l u hl =>
    d1At_zero (W.zφ 3 l (by revert hl; fin_cases l <;> decide)) p u
  have hd2 : ∀ x y a c, x ≠ 3 → y ≠ 3 → pb Pth [x, y, a, c] = true → d2At G p x y a c = 0 := by
    intro x y a c hx hy h
    by_cases hc : c = 2
    · subst hc; exact (d2At_indep hGs (W.iθ x y hx hy) p a).1
    by_cases ha : a = 2
    · subst ha; exact (d2At_indep hGs (W.iθ x y hx hy) p c).2
    have : pb Pth [x, y] = true := by simpa [pb, Pth, ha, hc] using h
    exact d2At_zero (W.zθ x y this) p a c
  apply csArr_three
  · exact fun ν b a h => GamF_par T h
  · exact fun ν b a hν hb ha h => GamF_rpar hgiθ hgi3 hd1 hν hb ha h
  · exact fun ρ σ a b hρ hσ ha hb h => DGamF_rpar hgiθ hgi3 hd1 hd1' hd2 hσ ha hb h
  · exact DGamF_33 hgi3' (fun m u hm => d1At_zero (W.zφ m 3 (by revert hm; fin_cases m <;> decide)) p u)
      (fun x y => d1At_indep hGs (W.iφ x y) p) (fun x y a => (d2At_indep hGs (W.iφ x y) p a).1)
      (fun a c => d2At_symm hGs p 3 3 a c)

end Warped

/-! ## Part 4: the general dynamic spherically symmetric metric -/

section Spherical

set_option synthInstance.maxHeartbeats 400000

lemma cd2 {A : ℝ × ℝ → ℝ} (hA : ContDiff ℝ ∞ A) : ContDiff ℝ ∞ (fun y : Fin 4 → ℝ => A (y 0, y 1)) :=
  hA.comp ((contDiff_apply ℝ ℝ (0 : Fin 4)).prodMk (contDiff_apply ℝ ℝ (1 : Fin 4)))

/-- **The receipt's `gsph`**, with `A, B, C, S` arbitrary functions of `(t, r) = (x⁰, x¹)` and the angular profile
`h(θ)` in place of `sin²θ`: `−A dt² + 2C dt dr + B dr² + S² dθ² + S² h(θ) dφ²`, coordinates `(t, r, θ, φ)`. -/
noncomputable def gsph (A B C S : ℝ × ℝ → ℝ) (h : ℝ → ℝ) (i j : Fin 4) (y : Fin 4 → ℝ) : ℝ :=
  (![![-A (y 0, y 1), C (y 0, y 1), 0, 0], ![C (y 0, y 1), B (y 0, y 1), 0, 0], ![0, 0, S (y 0, y 1) ^ 2, 0],
    ![0, 0, 0, S (y 0, y 1) ^ 2 * h (y 2)]] : Fin 4 → Fin 4 → ℝ) i j

variable {A B C S : ℝ × ℝ → ℝ} {h : ℝ → ℝ}

lemma gsph_symm (i j : Fin 4) (y : Fin 4 → ℝ) : gsph A B C S h i j y = gsph A B C S h j i y := by
  fin_cases i <;> fin_cases j <;> rfl

lemma gsph_smooth (hA : ContDiff ℝ ∞ A) (hB : ContDiff ℝ ∞ B) (hC : ContDiff ℝ ∞ C) (hS : ContDiff ℝ ∞ S)
    (hh : ContDiff ℝ ∞ h) (i j : Fin 4) : ContDiff ℝ ∞ (gsph A B C S h i j) := by
  fin_cases i <;> fin_cases j <;> simp only [gsph] <;>
    simp only [Fin.zero_eta, Fin.mk_one, Fin.reduceFinMk, Matrix.cons_val, Matrix.cons_val_zero, Matrix.cons_val_one] <;>
    first
    | exact contDiff_const
    | exact (cd2 hA).neg
    | exact cd2 hB
    | exact cd2 hC
    | exact (cd2 hS).pow 2
    | exact ((cd2 hS).pow 2).mul (hh.comp (contDiff_apply ℝ ℝ (2 : Fin 4)))

lemma gsph_det (y : Fin 4 → ℝ) :
    (gm (gsph A B C S h) y).det = -(A (y 0, y 1) * B (y 0, y 1) + C (y 0, y 1) ^ 2) * S (y 0, y 1) ^ 4 * h (y 2) := by
  simp [Matrix.det_succ_row_zero, Fin.sum_univ_succ, gm, gsph, show (Fin.succAbove 1 2 : Fin 4) = 3 by decide]
  ring

lemma gsph_nondeg (hAB : ∀ x, A x * B x + C x ^ 2 ≠ 0) (hS0 : ∀ x, S x ≠ 0) (hh0 : ∀ s, h s ≠ 0) :
    ∀ p (u : Fin 4 → ℝ), (∀ v, formG (gsph A B C S h) p u v = 0) → u = 0 :=
  nondeg_of_det fun y => by
    rw [gsph_det]
    exact mul_ne_zero (mul_ne_zero (neg_ne_zero.2 (hAB _)) (pow_ne_zero _ (hS0 _))) (hh0 _)

lemma gsph_warped : Warped (gsph A B C S h) where
  zφ i j hij y := by fin_cases i <;> fin_cases j <;> simp_all [pb, Pph, gsph]
  zθ i j hij y := by fin_cases i <;> fin_cases j <;> simp_all [pb, Pth, gsph]
  iφ i j y c := by fin_cases i <;> fin_cases j <;> simp [gsph, Pi.single_apply]
  iθ i j hi hj y c := by fin_cases i <;> fin_cases j <;> simp_all [gsph, Pi.single_apply]

variable (hA : ContDiff ℝ ∞ A) (hB : ContDiff ℝ ∞ B) (hC : ContDiff ℝ ∞ C) (hS : ContDiff ℝ ∞ S)
  (hh : ContDiff ℝ ∞ h) (hAB : ∀ x, A x * B x + C x ^ 2 ≠ 0) (hS0 : ∀ x, S x ≠ 0) (hh0 : ∀ s, h s ≠ 0)
include hA hB hC hS hh hAB hS0 hh0

/-- **Part 4, the density.** On the general DYNAMIC spherically symmetric metric (four arbitrary smooth functions of
`(t, r)`, the `dt dr` cross term kept), THE connection's `*RR` vanishes at every point. -/
theorem sph_pontryagin_zero (p : Fin 4 → ℝ) :
    pontryaginLC (gsph A B C S h) gsph_symm (gsph_nondeg hAB hS0 hh0) (gsph_smooth hA hB hC hS hh) p = 0 :=
  warped_pontryagin _ _ _ gsph_warped p

/-- **Part 4, the current.** On the same class ALL FOUR components of THE connection's Chern–Simons current vanish
identically: `K^t = K^r = K^θ = K^φ = 0`. -/
theorem sph_cs_zero (p : Fin 4 → ℝ) (μ : Fin 4) :
    csLC (gsph A B C S h) gsph_symm (gsph_nondeg hAB hS0 hh0) (gsph_smooth hA hB hC hS hh) p μ = 0 :=
  warped_cs _ _ _ gsph_warped p μ

end Spherical

/-! ## Part 2: the polarised Gowdy cut -/

section Polarised

set_option synthInstance.maxHeartbeats 400000

/-- **The receipt's `gowdy(A, ψ, 0, R)`**, the linearly polarised cut: `e^{2A}(−dt² + dz²) + e^{2ψ} dx² + R² e^{−2ψ} dy²`,
with `A, ψ, R` arbitrary functions of `(t, z) = (x⁰, x¹)`; coordinates `(t, z, x, y)`. -/
noncomputable def gpol (A ψ R : ℝ × ℝ → ℝ) (i j : Fin 4) (y : Fin 4 → ℝ) : ℝ :=
  (![![-Real.exp (2 * A (y 0, y 1)), 0, 0, 0], ![0, Real.exp (2 * A (y 0, y 1)), 0, 0],
    ![0, 0, Real.exp (2 * ψ (y 0, y 1)), 0],
    ![0, 0, 0, Real.exp (2 * ψ (y 0, y 1)) * 0 ^ 2 + R (y 0, y 1) ^ 2 * Real.exp (-2 * ψ (y 0, y 1))]] :
      Fin 4 → Fin 4 → ℝ) i j

variable {A ψ R : ℝ × ℝ → ℝ}

lemma gpol_symm (i j : Fin 4) (y : Fin 4 → ℝ) : gpol A ψ R i j y = gpol A ψ R j i y := by
  fin_cases i <;> fin_cases j <;> rfl

lemma gpol_smooth (hA : ContDiff ℝ ∞ A) (hψ : ContDiff ℝ ∞ ψ) (hR : ContDiff ℝ ∞ R) (i j : Fin 4) :
    ContDiff ℝ ∞ (gpol A ψ R i j) := by
  fin_cases i <;> fin_cases j <;> simp only [gpol] <;>
    simp only [Fin.zero_eta, Fin.mk_one, Fin.reduceFinMk, Matrix.cons_val, Matrix.cons_val_zero, Matrix.cons_val_one] <;>
    first
    | exact contDiff_const
    | exact (Real.contDiff_exp.comp (contDiff_const.mul (cd2 hA))).neg
    | exact Real.contDiff_exp.comp (contDiff_const.mul (cd2 hA))
    | exact Real.contDiff_exp.comp (contDiff_const.mul (cd2 hψ))
    | exact ((Real.contDiff_exp.comp (contDiff_const.mul (cd2 hψ))).mul contDiff_const).add
        (((cd2 hR).pow 2).mul (Real.contDiff_exp.comp (contDiff_const.mul (cd2 hψ))))

lemma gpol_nondeg (hR0 : ∀ x, R x ≠ 0) : ∀ p (u : Fin 4 → ℝ), (∀ v, formG (gpol A ψ R) p u v = 0) → u = 0 :=
  nondeg_of_det fun y => by
    simp [Matrix.det_succ_row_zero, Fin.sum_univ_succ, gm, gpol, Real.exp_ne_zero, hR0]

/-- `x = x²` as the parity set. -/
def Px : Fin 4 → Bool := fun i => decide (i = 2)

/-- **Part 2, the polarised cut.** With `ω = 0` and `A, ψ, R` arbitrary smooth functions of `(t, z)` (`R` nowhere zero),
THE connection's `*RR` vanishes everywhere (`x`-parity: nothing depends on `x` and `x` does not mix). -/
theorem polarised_pontryagin_zero (hA : ContDiff ℝ ∞ A) (hψ : ContDiff ℝ ∞ ψ) (hR : ContDiff ℝ ∞ R)
    (hR0 : ∀ x, R x ≠ 0) (p : Fin 4 → ℝ) :
    pontryaginLC (gpol A ψ R) gpol_symm (gpol_nondeg hR0) (gpol_smooth hA hψ hR) p = 0 := by
  refine pontryagin_parity _ _ _ Px (fun i j hij y => ?_) (fun k hk i j y c => ?_) (by decide) p
  · fin_cases i <;> fin_cases j <;> simp_all [pb, Px, gpol]
  · have : k = 2 := by simpa [Px] using hk
    subst this
    fin_cases i <;> fin_cases j <;> simp [gpol, Pi.single_apply]

end Polarised

/-! ## The plane-wave Gowdy instance (row 69's, copied; with the `∂Γ` table added for the current) -/

section Gowdy

set_option synthInstance.maxHeartbeats 400000

/-- The jet at the point: `E = e^{2ψ(u)}`, `ψ′, ψ″, ω, ω′, ω″` at `u = t − z`, and `R, R′, R″` at `t`. -/
structure Jet where
  E : ℝ
  p1 : ℝ
  p2 : ℝ
  w0 : ℝ
  w1 : ℝ
  w2 : ℝ
  r0 : ℝ
  r1 : ℝ
  r2 : ℝ

noncomputable def GT (J : Jet) : Fin 4 → Fin 4 → ℝ :=
  ![![(-1), (0), (0), (0)], ![(0), (1), (0), (0)], ![(0), (0), (J.E), (J.E*J.w0)], ![(0), (0), (J.E*J.w0), ((J.E^(2:ℕ)*J.w0^(2:ℕ) + J.r0^(2:ℕ))/J.E)]]

noncomputable def GiT (J : Jet) : Fin 4 → Fin 4 → ℝ :=
  ![![(-1), (0), (0), (0)], ![(0), (1), (0), (0)], ![(0), (0), ((J.E^(2:ℕ)*J.w0^(2:ℕ) + J.r0^(2:ℕ))/(J.E*J.r0^(2:ℕ))), (-J.E*J.w0/J.r0^(2:ℕ))], ![(0), (0), (-J.E*J.w0/J.r0^(2:ℕ)), (J.E/J.r0^(2:ℕ))]]

noncomputable def D1T (J : Jet) : Fin 4 → Fin 4 → Fin 4 → ℝ :=
  ![![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(2*J.E*J.p1), (-2*J.E*J.p1), (0), (0)], ![(J.E*(2*J.p1*J.w0 + J.w1)), (-J.E*(2*J.p1*J.w0 + J.w1)), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(J.E*(2*J.p1*J.w0 + J.w1)), (-J.E*(2*J.p1*J.w0 + J.w1)), (0), (0)], ![(2*(J.E^(2:ℕ)*J.p1*J.w0^(2:ℕ) + J.E^(2:ℕ)*J.w0*J.w1 - J.p1*J.r0^(2:ℕ) + J.r0*J.r1)/J.E), (-2*(J.E^(2:ℕ)*J.p1*J.w0^(2:ℕ) + J.E^(2:ℕ)*J.w0*J.w1 - J.p1*J.r0^(2:ℕ))/J.E), (0), (0)]]]

noncomputable def D2T (J : Jet) : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ :=
  ![![![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]]], ![![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]]], ![![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(2*J.E*(2*J.p1^(2:ℕ) + J.p2)), (-2*J.E*(2*J.p1^(2:ℕ) + J.p2)), (0), (0)], ![(-2*J.E*(2*J.p1^(2:ℕ) + J.p2)), (2*J.E*(2*J.p1^(2:ℕ) + J.p2)), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(J.E*(4*J.p1^(2:ℕ)*J.w0 + 4*J.p1*J.w1 + 2*J.p2*J.w0 + J.w2)), (-J.E*(4*J.p1^(2:ℕ)*J.w0 + 4*J.p1*J.w1 + 2*J.p2*J.w0 + J.w2)), (0), (0)], ![(-J.E*(4*J.p1^(2:ℕ)*J.w0 + 4*J.p1*J.w1 + 2*J.p2*J.w0 + J.w2)), (J.E*(4*J.p1^(2:ℕ)*J.w0 + 4*J.p1*J.w1 + 2*J.p2*J.w0 + J.w2)), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]]], ![![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(J.E*(4*J.p1^(2:ℕ)*J.w0 + 4*J.p1*J.w1 + 2*J.p2*J.w0 + J.w2)), (-J.E*(4*J.p1^(2:ℕ)*J.w0 + 4*J.p1*J.w1 + 2*J.p2*J.w0 + J.w2)), (0), (0)], ![(-J.E*(4*J.p1^(2:ℕ)*J.w0 + 4*J.p1*J.w1 + 2*J.p2*J.w0 + J.w2)), (J.E*(4*J.p1^(2:ℕ)*J.w0 + 4*J.p1*J.w1 + 2*J.p2*J.w0 + J.w2)), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(2*(2*J.E^(2:ℕ)*J.p1^(2:ℕ)*J.w0^(2:ℕ) + 4*J.E^(2:ℕ)*J.p1*J.w0*J.w1 + J.E^(2:ℕ)*J.p2*J.w0^(2:ℕ) + J.E^(2:ℕ)*J.w0*J.w2 + J.E^(2:ℕ)*J.w1^(2:ℕ) + 2*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p1*J.r0*J.r1 - J.p2*J.r0^(2:ℕ) + J.r0*J.r2 + J.r1^(2:ℕ))/J.E), (-2*(2*J.E^(2:ℕ)*J.p1^(2:ℕ)*J.w0^(2:ℕ) + 4*J.E^(2:ℕ)*J.p1*J.w0*J.w1 + J.E^(2:ℕ)*J.p2*J.w0^(2:ℕ) + J.E^(2:ℕ)*J.w0*J.w2 + J.E^(2:ℕ)*J.w1^(2:ℕ) + 2*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 2*J.p1*J.r0*J.r1 - J.p2*J.r0^(2:ℕ))/J.E), (0), (0)], ![(-2*(2*J.E^(2:ℕ)*J.p1^(2:ℕ)*J.w0^(2:ℕ) + 4*J.E^(2:ℕ)*J.p1*J.w0*J.w1 + J.E^(2:ℕ)*J.p2*J.w0^(2:ℕ) + J.E^(2:ℕ)*J.w0*J.w2 + J.E^(2:ℕ)*J.w1^(2:ℕ) + 2*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 2*J.p1*J.r0*J.r1 - J.p2*J.r0^(2:ℕ))/J.E), (2*(2*J.E^(2:ℕ)*J.p1^(2:ℕ)*J.w0^(2:ℕ) + 4*J.E^(2:ℕ)*J.p1*J.w0*J.w1 + J.E^(2:ℕ)*J.p2*J.w0^(2:ℕ) + J.E^(2:ℕ)*J.w0*J.w2 + J.E^(2:ℕ)*J.w1^(2:ℕ) + 2*J.p1^(2:ℕ)*J.r0^(2:ℕ) - J.p2*J.r0^(2:ℕ))/J.E), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]]]]

noncomputable def GamT (J : Jet) : Fin 4 → Fin 4 → Fin 4 → ℝ :=
  ![![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (-(J.E^(2:ℕ)*J.w0*J.w1 - 2*J.p1*J.r0^(2:ℕ))/(2*J.r0^(2:ℕ))), (J.E^(2:ℕ)*J.w1/(2*J.r0^(2:ℕ)))], ![(0), (0), (-(J.E^(2:ℕ)*J.w0^(2:ℕ)*J.w1 - 4*J.p1*J.r0^(2:ℕ)*J.w0 - J.r0^(2:ℕ)*J.w1 + 2*J.r0*J.r1*J.w0)/(2*J.r0^(2:ℕ))), ((J.E^(2:ℕ)*J.w0*J.w1 - 2*J.p1*J.r0^(2:ℕ) + 2*J.r0*J.r1)/(2*J.r0^(2:ℕ)))]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), ((J.E^(2:ℕ)*J.w0*J.w1 - 2*J.p1*J.r0^(2:ℕ))/(2*J.r0^(2:ℕ))), (-J.E^(2:ℕ)*J.w1/(2*J.r0^(2:ℕ)))], ![(0), (0), ((J.E^(2:ℕ)*J.w0^(2:ℕ)*J.w1 - 4*J.p1*J.r0^(2:ℕ)*J.w0 - J.r0^(2:ℕ)*J.w1)/(2*J.r0^(2:ℕ))), (-(J.E^(2:ℕ)*J.w0*J.w1 - 2*J.p1*J.r0^(2:ℕ))/(2*J.r0^(2:ℕ)))]], ![![(0), (0), (-(J.E^(2:ℕ)*J.w0*J.w1 - 2*J.p1*J.r0^(2:ℕ))/(2*J.r0^(2:ℕ))), (J.E^(2:ℕ)*J.w1/(2*J.r0^(2:ℕ)))], ![(0), (0), ((J.E^(2:ℕ)*J.w0*J.w1 - 2*J.p1*J.r0^(2:ℕ))/(2*J.r0^(2:ℕ))), (-J.E^(2:ℕ)*J.w1/(2*J.r0^(2:ℕ)))], ![(J.E*J.p1), (J.E*J.p1), (0), (0)], ![(J.E*(2*J.p1*J.w0 + J.w1)/2), (J.E*(2*J.p1*J.w0 + J.w1)/2), (0), (0)]], ![![(0), (0), (-(J.E^(2:ℕ)*J.w0^(2:ℕ)*J.w1 - 4*J.p1*J.r0^(2:ℕ)*J.w0 - J.r0^(2:ℕ)*J.w1 + 2*J.r0*J.r1*J.w0)/(2*J.r0^(2:ℕ))), ((J.E^(2:ℕ)*J.w0*J.w1 - 2*J.p1*J.r0^(2:ℕ) + 2*J.r0*J.r1)/(2*J.r0^(2:ℕ)))], ![(0), (0), ((J.E^(2:ℕ)*J.w0^(2:ℕ)*J.w1 - 4*J.p1*J.r0^(2:ℕ)*J.w0 - J.r0^(2:ℕ)*J.w1)/(2*J.r0^(2:ℕ))), (-(J.E^(2:ℕ)*J.w0*J.w1 - 2*J.p1*J.r0^(2:ℕ))/(2*J.r0^(2:ℕ)))], ![(J.E*(2*J.p1*J.w0 + J.w1)/2), (J.E*(2*J.p1*J.w0 + J.w1)/2), (0), (0)], ![((J.E^(2:ℕ)*J.p1*J.w0^(2:ℕ) + J.E^(2:ℕ)*J.w0*J.w1 - J.p1*J.r0^(2:ℕ) + J.r0*J.r1)/J.E), ((J.E^(2:ℕ)*J.p1*J.w0^(2:ℕ) + J.E^(2:ℕ)*J.w0*J.w1 - J.p1*J.r0^(2:ℕ))/J.E), (0), (0)]]]

noncomputable def DGT (J : Jet) : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ :=
  ![![![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (-(4*J.E^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 + J.E^(2:ℕ)*J.r0*J.w0*J.w2 + J.E^(2:ℕ)*J.r0*J.w1^(2:ℕ) - 2*J.E^(2:ℕ)*J.r1*J.w0*J.w1 - 2*J.p2*J.r0^(3:ℕ))/(2*J.r0^(3:ℕ))), (J.E^(2:ℕ)*(4*J.p1*J.r0*J.w1 + J.r0*J.w2 - 2*J.r1*J.w1)/(2*J.r0^(3:ℕ)))], ![(0), (0), (-(4*J.E^(2:ℕ)*J.p1*J.r0*J.w0^(2:ℕ)*J.w1 + J.E^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w2 + 2*J.E^(2:ℕ)*J.r0*J.w0*J.w1^(2:ℕ) - 2*J.E^(2:ℕ)*J.r1*J.w0^(2:ℕ)*J.w1 - 4*J.p1*J.r0^(3:ℕ)*J.w1 - 4*J.p2*J.r0^(3:ℕ)*J.w0 - J.r0^(3:ℕ)*J.w2 + 2*J.r0^(2:ℕ)*J.r1*J.w1 + 2*J.r0^(2:ℕ)*J.r2*J.w0 - 2*J.r0*J.r1^(2:ℕ)*J.w0)/(2*J.r0^(3:ℕ))), ((4*J.E^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 + J.E^(2:ℕ)*J.r0*J.w0*J.w2 + J.E^(2:ℕ)*J.r0*J.w1^(2:ℕ) - 2*J.E^(2:ℕ)*J.r1*J.w0*J.w1 - 2*J.p2*J.r0^(3:ℕ) + 2*J.r0^(2:ℕ)*J.r2 - 2*J.r0*J.r1^(2:ℕ))/(2*J.r0^(3:ℕ)))]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), ((4*J.E^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 + J.E^(2:ℕ)*J.r0*J.w0*J.w2 + J.E^(2:ℕ)*J.r0*J.w1^(2:ℕ) - 2*J.E^(2:ℕ)*J.r1*J.w0*J.w1 - 2*J.p2*J.r0^(3:ℕ))/(2*J.r0^(3:ℕ))), (-J.E^(2:ℕ)*(4*J.p1*J.r0*J.w1 + J.r0*J.w2 - 2*J.r1*J.w1)/(2*J.r0^(3:ℕ)))], ![(0), (0), ((4*J.E^(2:ℕ)*J.p1*J.r0*J.w0^(2:ℕ)*J.w1 + J.E^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w2 + 2*J.E^(2:ℕ)*J.r0*J.w0*J.w1^(2:ℕ) - 2*J.E^(2:ℕ)*J.r1*J.w0^(2:ℕ)*J.w1 - 4*J.p1*J.r0^(3:ℕ)*J.w1 - 4*J.p2*J.r0^(3:ℕ)*J.w0 - J.r0^(3:ℕ)*J.w2)/(2*J.r0^(3:ℕ))), (-(4*J.E^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 + J.E^(2:ℕ)*J.r0*J.w0*J.w2 + J.E^(2:ℕ)*J.r0*J.w1^(2:ℕ) - 2*J.E^(2:ℕ)*J.r1*J.w0*J.w1 - 2*J.p2*J.r0^(3:ℕ))/(2*J.r0^(3:ℕ)))]], ![![(0), (0), (-(4*J.E^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 + J.E^(2:ℕ)*J.r0*J.w0*J.w2 + J.E^(2:ℕ)*J.r0*J.w1^(2:ℕ) - 2*J.E^(2:ℕ)*J.r1*J.w0*J.w1 - 2*J.p2*J.r0^(3:ℕ))/(2*J.r0^(3:ℕ))), (J.E^(2:ℕ)*(4*J.p1*J.r0*J.w1 + J.r0*J.w2 - 2*J.r1*J.w1)/(2*J.r0^(3:ℕ)))], ![(0), (0), ((4*J.E^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 + J.E^(2:ℕ)*J.r0*J.w0*J.w2 + J.E^(2:ℕ)*J.r0*J.w1^(2:ℕ) - 2*J.E^(2:ℕ)*J.r1*J.w0*J.w1 - 2*J.p2*J.r0^(3:ℕ))/(2*J.r0^(3:ℕ))), (-J.E^(2:ℕ)*(4*J.p1*J.r0*J.w1 + J.r0*J.w2 - 2*J.r1*J.w1)/(2*J.r0^(3:ℕ)))], ![(J.E*(2*J.p1^(2:ℕ) + J.p2)), (J.E*(2*J.p1^(2:ℕ) + J.p2)), (0), (0)], ![(J.E*(4*J.p1^(2:ℕ)*J.w0 + 4*J.p1*J.w1 + 2*J.p2*J.w0 + J.w2)/2), (J.E*(4*J.p1^(2:ℕ)*J.w0 + 4*J.p1*J.w1 + 2*J.p2*J.w0 + J.w2)/2), (0), (0)]], ![![(0), (0), (-(4*J.E^(2:ℕ)*J.p1*J.r0*J.w0^(2:ℕ)*J.w1 + J.E^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w2 + 2*J.E^(2:ℕ)*J.r0*J.w0*J.w1^(2:ℕ) - 2*J.E^(2:ℕ)*J.r1*J.w0^(2:ℕ)*J.w1 - 4*J.p1*J.r0^(3:ℕ)*J.w1 - 4*J.p2*J.r0^(3:ℕ)*J.w0 - J.r0^(3:ℕ)*J.w2 + 2*J.r0^(2:ℕ)*J.r1*J.w1 + 2*J.r0^(2:ℕ)*J.r2*J.w0 - 2*J.r0*J.r1^(2:ℕ)*J.w0)/(2*J.r0^(3:ℕ))), ((4*J.E^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 + J.E^(2:ℕ)*J.r0*J.w0*J.w2 + J.E^(2:ℕ)*J.r0*J.w1^(2:ℕ) - 2*J.E^(2:ℕ)*J.r1*J.w0*J.w1 - 2*J.p2*J.r0^(3:ℕ) + 2*J.r0^(2:ℕ)*J.r2 - 2*J.r0*J.r1^(2:ℕ))/(2*J.r0^(3:ℕ)))], ![(0), (0), ((4*J.E^(2:ℕ)*J.p1*J.r0*J.w0^(2:ℕ)*J.w1 + J.E^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w2 + 2*J.E^(2:ℕ)*J.r0*J.w0*J.w1^(2:ℕ) - 2*J.E^(2:ℕ)*J.r1*J.w0^(2:ℕ)*J.w1 - 4*J.p1*J.r0^(3:ℕ)*J.w1 - 4*J.p2*J.r0^(3:ℕ)*J.w0 - J.r0^(3:ℕ)*J.w2)/(2*J.r0^(3:ℕ))), (-(4*J.E^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 + J.E^(2:ℕ)*J.r0*J.w0*J.w2 + J.E^(2:ℕ)*J.r0*J.w1^(2:ℕ) - 2*J.E^(2:ℕ)*J.r1*J.w0*J.w1 - 2*J.p2*J.r0^(3:ℕ))/(2*J.r0^(3:ℕ)))], ![(J.E*(4*J.p1^(2:ℕ)*J.w0 + 4*J.p1*J.w1 + 2*J.p2*J.w0 + J.w2)/2), (J.E*(4*J.p1^(2:ℕ)*J.w0 + 4*J.p1*J.w1 + 2*J.p2*J.w0 + J.w2)/2), (0), (0)], ![((2*J.E^(2:ℕ)*J.p1^(2:ℕ)*J.w0^(2:ℕ) + 4*J.E^(2:ℕ)*J.p1*J.w0*J.w1 + J.E^(2:ℕ)*J.p2*J.w0^(2:ℕ) + J.E^(2:ℕ)*J.w0*J.w2 + J.E^(2:ℕ)*J.w1^(2:ℕ) + 2*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p1*J.r0*J.r1 - J.p2*J.r0^(2:ℕ) + J.r0*J.r2 + J.r1^(2:ℕ))/J.E), ((2*J.E^(2:ℕ)*J.p1^(2:ℕ)*J.w0^(2:ℕ) + 4*J.E^(2:ℕ)*J.p1*J.w0*J.w1 + J.E^(2:ℕ)*J.p2*J.w0^(2:ℕ) + J.E^(2:ℕ)*J.w0*J.w2 + J.E^(2:ℕ)*J.w1^(2:ℕ) + 2*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 2*J.p1*J.r0*J.r1 - J.p2*J.r0^(2:ℕ))/J.E), (0), (0)]]], ![![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), ((4*J.E^(2:ℕ)*J.p1*J.w0*J.w1 + J.E^(2:ℕ)*J.w0*J.w2 + J.E^(2:ℕ)*J.w1^(2:ℕ) - 2*J.p2*J.r0^(2:ℕ))/(2*J.r0^(2:ℕ))), (-J.E^(2:ℕ)*(4*J.p1*J.w1 + J.w2)/(2*J.r0^(2:ℕ)))], ![(0), (0), ((4*J.E^(2:ℕ)*J.p1*J.w0^(2:ℕ)*J.w1 + J.E^(2:ℕ)*J.w0^(2:ℕ)*J.w2 + 2*J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - J.r0^(2:ℕ)*J.w2 + 2*J.r0*J.r1*J.w1)/(2*J.r0^(2:ℕ))), (-(4*J.E^(2:ℕ)*J.p1*J.w0*J.w1 + J.E^(2:ℕ)*J.w0*J.w2 + J.E^(2:ℕ)*J.w1^(2:ℕ) - 2*J.p2*J.r0^(2:ℕ))/(2*J.r0^(2:ℕ)))]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (-(4*J.E^(2:ℕ)*J.p1*J.w0*J.w1 + J.E^(2:ℕ)*J.w0*J.w2 + J.E^(2:ℕ)*J.w1^(2:ℕ) - 2*J.p2*J.r0^(2:ℕ))/(2*J.r0^(2:ℕ))), (J.E^(2:ℕ)*(4*J.p1*J.w1 + J.w2)/(2*J.r0^(2:ℕ)))], ![(0), (0), (-(4*J.E^(2:ℕ)*J.p1*J.w0^(2:ℕ)*J.w1 + J.E^(2:ℕ)*J.w0^(2:ℕ)*J.w2 + 2*J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - J.r0^(2:ℕ)*J.w2)/(2*J.r0^(2:ℕ))), ((4*J.E^(2:ℕ)*J.p1*J.w0*J.w1 + J.E^(2:ℕ)*J.w0*J.w2 + J.E^(2:ℕ)*J.w1^(2:ℕ) - 2*J.p2*J.r0^(2:ℕ))/(2*J.r0^(2:ℕ)))]], ![![(0), (0), ((4*J.E^(2:ℕ)*J.p1*J.w0*J.w1 + J.E^(2:ℕ)*J.w0*J.w2 + J.E^(2:ℕ)*J.w1^(2:ℕ) - 2*J.p2*J.r0^(2:ℕ))/(2*J.r0^(2:ℕ))), (-J.E^(2:ℕ)*(4*J.p1*J.w1 + J.w2)/(2*J.r0^(2:ℕ)))], ![(0), (0), (-(4*J.E^(2:ℕ)*J.p1*J.w0*J.w1 + J.E^(2:ℕ)*J.w0*J.w2 + J.E^(2:ℕ)*J.w1^(2:ℕ) - 2*J.p2*J.r0^(2:ℕ))/(2*J.r0^(2:ℕ))), (J.E^(2:ℕ)*(4*J.p1*J.w1 + J.w2)/(2*J.r0^(2:ℕ)))], ![(-J.E*(2*J.p1^(2:ℕ) + J.p2)), (-J.E*(2*J.p1^(2:ℕ) + J.p2)), (0), (0)], ![(-J.E*(4*J.p1^(2:ℕ)*J.w0 + 4*J.p1*J.w1 + 2*J.p2*J.w0 + J.w2)/2), (-J.E*(4*J.p1^(2:ℕ)*J.w0 + 4*J.p1*J.w1 + 2*J.p2*J.w0 + J.w2)/2), (0), (0)]], ![![(0), (0), ((4*J.E^(2:ℕ)*J.p1*J.w0^(2:ℕ)*J.w1 + J.E^(2:ℕ)*J.w0^(2:ℕ)*J.w2 + 2*J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - J.r0^(2:ℕ)*J.w2 + 2*J.r0*J.r1*J.w1)/(2*J.r0^(2:ℕ))), (-(4*J.E^(2:ℕ)*J.p1*J.w0*J.w1 + J.E^(2:ℕ)*J.w0*J.w2 + J.E^(2:ℕ)*J.w1^(2:ℕ) - 2*J.p2*J.r0^(2:ℕ))/(2*J.r0^(2:ℕ)))], ![(0), (0), (-(4*J.E^(2:ℕ)*J.p1*J.w0^(2:ℕ)*J.w1 + J.E^(2:ℕ)*J.w0^(2:ℕ)*J.w2 + 2*J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - J.r0^(2:ℕ)*J.w2)/(2*J.r0^(2:ℕ))), ((4*J.E^(2:ℕ)*J.p1*J.w0*J.w1 + J.E^(2:ℕ)*J.w0*J.w2 + J.E^(2:ℕ)*J.w1^(2:ℕ) - 2*J.p2*J.r0^(2:ℕ))/(2*J.r0^(2:ℕ)))], ![(-J.E*(4*J.p1^(2:ℕ)*J.w0 + 4*J.p1*J.w1 + 2*J.p2*J.w0 + J.w2)/2), (-J.E*(4*J.p1^(2:ℕ)*J.w0 + 4*J.p1*J.w1 + 2*J.p2*J.w0 + J.w2)/2), (0), (0)], ![(-(2*J.E^(2:ℕ)*J.p1^(2:ℕ)*J.w0^(2:ℕ) + 4*J.E^(2:ℕ)*J.p1*J.w0*J.w1 + J.E^(2:ℕ)*J.p2*J.w0^(2:ℕ) + J.E^(2:ℕ)*J.w0*J.w2 + J.E^(2:ℕ)*J.w1^(2:ℕ) + 2*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 2*J.p1*J.r0*J.r1 - J.p2*J.r0^(2:ℕ))/J.E), (-(2*J.E^(2:ℕ)*J.p1^(2:ℕ)*J.w0^(2:ℕ) + 4*J.E^(2:ℕ)*J.p1*J.w0*J.w1 + J.E^(2:ℕ)*J.p2*J.w0^(2:ℕ) + J.E^(2:ℕ)*J.w0*J.w2 + J.E^(2:ℕ)*J.w1^(2:ℕ) + 2*J.p1^(2:ℕ)*J.r0^(2:ℕ) - J.p2*J.r0^(2:ℕ))/J.E), (0), (0)]]], ![![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]]], ![![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]]]]

noncomputable def RT (J : Jet) : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ :=
  ![![![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (-J.E^(2:ℕ)*J.r1*J.w0*J.w1/(2*J.r0^(3:ℕ))), (J.E^(2:ℕ)*J.r1*J.w1/(2*J.r0^(3:ℕ)))], ![(0), (0), (-J.r1*J.w1*(J.E^(2:ℕ)*J.w0^(2:ℕ) + J.r0^(2:ℕ))/(2*J.r0^(3:ℕ))), (J.E^(2:ℕ)*J.r1*J.w0*J.w1/(2*J.r0^(3:ℕ)))]], ![![(0), (0), (-(8*J.E^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.r0*J.w0*J.w2 + J.E^(2:ℕ)*J.r0*J.w1^(2:ℕ) - 2*J.E^(2:ℕ)*J.r1*J.w0*J.w1 - 4*J.p1^(2:ℕ)*J.r0^(3:ℕ) - 4*J.p2*J.r0^(3:ℕ))/(4*J.r0^(3:ℕ))), (J.E^(2:ℕ)*(4*J.p1*J.r0*J.w1 + J.r0*J.w2 - J.r1*J.w1)/(2*J.r0^(3:ℕ)))], ![(0), (0), ((8*J.E^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.r0*J.w0*J.w2 + J.E^(2:ℕ)*J.r0*J.w1^(2:ℕ) - 2*J.E^(2:ℕ)*J.r1*J.w0*J.w1 - 4*J.p1^(2:ℕ)*J.r0^(3:ℕ) - 4*J.p2*J.r0^(3:ℕ))/(4*J.r0^(3:ℕ))), (-J.E^(2:ℕ)*(4*J.p1*J.r0*J.w1 + J.r0*J.w2 - J.r1*J.w1)/(2*J.r0^(3:ℕ)))], ![(-J.E*(J.E^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ))), (-J.E*(J.E^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ))), (0), (0)], ![(-J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2 + 2*J.r0*J.r1*J.w1)/(4*J.r0^(2:ℕ))), (-J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2 + 2*J.r0*J.r1*J.w1)/(4*J.r0^(2:ℕ))), (0), (0)]], ![![(0), (0), (-(4*J.E^(2:ℕ)*J.p1*J.r0*J.w0^(2:ℕ)*J.w1 + J.E^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w2 + 2*J.E^(2:ℕ)*J.r0*J.w0*J.w1^(2:ℕ) - J.E^(2:ℕ)*J.r1*J.w0^(2:ℕ)*J.w1 - 4*J.p1*J.r0^(3:ℕ)*J.w1 - 4*J.p1*J.r0^(2:ℕ)*J.r1*J.w0 - 4*J.p2*J.r0^(3:ℕ)*J.w0 - J.r0^(3:ℕ)*J.w2 + J.r0^(2:ℕ)*J.r1*J.w1 + 2*J.r0^(2:ℕ)*J.r2*J.w0)/(2*J.r0^(3:ℕ))), ((8*J.E^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.r0*J.w0*J.w2 + 3*J.E^(2:ℕ)*J.r0*J.w1^(2:ℕ) - 2*J.E^(2:ℕ)*J.r1*J.w0*J.w1 + 4*J.p1^(2:ℕ)*J.r0^(3:ℕ) - 8*J.p1*J.r0^(2:ℕ)*J.r1 - 4*J.p2*J.r0^(3:ℕ) + 4*J.r0^(2:ℕ)*J.r2)/(4*J.r0^(3:ℕ)))], ![(0), (0), ((4*J.E^(2:ℕ)*J.p1*J.r0*J.w0^(2:ℕ)*J.w1 + J.E^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w2 + 2*J.E^(2:ℕ)*J.r0*J.w0*J.w1^(2:ℕ) - J.E^(2:ℕ)*J.r1*J.w0^(2:ℕ)*J.w1 - 4*J.p1*J.r0^(3:ℕ)*J.w1 - 2*J.p1*J.r0^(2:ℕ)*J.r1*J.w0 - 4*J.p2*J.r0^(3:ℕ)*J.w0 - J.r0^(3:ℕ)*J.w2)/(2*J.r0^(3:ℕ))), (-(8*J.E^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.r0*J.w0*J.w2 + 3*J.E^(2:ℕ)*J.r0*J.w1^(2:ℕ) - 2*J.E^(2:ℕ)*J.r1*J.w0*J.w1 + 4*J.p1^(2:ℕ)*J.r0^(3:ℕ) - 4*J.p1*J.r0^(2:ℕ)*J.r1 - 4*J.p2*J.r0^(3:ℕ))/(4*J.r0^(3:ℕ)))], ![(-J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2 + 2*J.r0*J.r1*J.w1)/(4*J.r0^(2:ℕ))), (-J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2)/(4*J.r0^(2:ℕ))), (0), (0)], ![(-(J.E^(4:ℕ)*J.w0^(2:ℕ)*J.w1^(2:ℕ) - 4*J.E^(2:ℕ)*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 16*J.E^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.E^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 4*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 3*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w1^(2:ℕ) + 4*J.E^(2:ℕ)*J.r0*J.r1*J.w0*J.w1 - 4*J.p1^(2:ℕ)*J.r0^(4:ℕ) + 8*J.p1*J.r0^(3:ℕ)*J.r1 + 4*J.p2*J.r0^(4:ℕ) - 4*J.r0^(3:ℕ)*J.r2)/(4*J.E*J.r0^(2:ℕ))), (-(J.E^(4:ℕ)*J.w0^(2:ℕ)*J.w1^(2:ℕ) - 4*J.E^(2:ℕ)*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 16*J.E^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.E^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 4*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 3*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w1^(2:ℕ) + 2*J.E^(2:ℕ)*J.r0*J.r1*J.w0*J.w1 - 4*J.p1^(2:ℕ)*J.r0^(4:ℕ) + 4*J.p1*J.r0^(3:ℕ)*J.r1 + 4*J.p2*J.r0^(4:ℕ))/(4*J.E*J.r0^(2:ℕ))), (0), (0)]]], ![![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (J.E^(2:ℕ)*J.r1*J.w0*J.w1/(2*J.r0^(3:ℕ))), (-J.E^(2:ℕ)*J.r1*J.w1/(2*J.r0^(3:ℕ)))], ![(0), (0), (J.r1*J.w1*(J.E^(2:ℕ)*J.w0^(2:ℕ) + J.r0^(2:ℕ))/(2*J.r0^(3:ℕ))), (-J.E^(2:ℕ)*J.r1*J.w0*J.w1/(2*J.r0^(3:ℕ)))]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), ((8*J.E^(2:ℕ)*J.p1*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.w0*J.w2 + J.E^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ))), (-J.E^(2:ℕ)*(4*J.p1*J.w1 + J.w2)/(2*J.r0^(2:ℕ)))], ![(0), (0), (-(8*J.E^(2:ℕ)*J.p1*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.w0*J.w2 + J.E^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ))), (J.E^(2:ℕ)*(4*J.p1*J.w1 + J.w2)/(2*J.r0^(2:ℕ)))], ![(J.E*(J.E^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ))), (J.E*(J.E^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ))), (0), (0)], ![(J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2)/(4*J.r0^(2:ℕ))), (J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2)/(4*J.r0^(2:ℕ))), (0), (0)]], ![![(0), (0), ((4*J.E^(2:ℕ)*J.p1*J.w0^(2:ℕ)*J.w1 + J.E^(2:ℕ)*J.w0^(2:ℕ)*J.w2 + 2*J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1*J.r0^(2:ℕ)*J.w1 - 2*J.p1*J.r0*J.r1*J.w0 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - J.r0^(2:ℕ)*J.w2 + J.r0*J.r1*J.w1)/(2*J.r0^(2:ℕ))), (-(8*J.E^(2:ℕ)*J.p1*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.w0*J.w2 + 3*J.E^(2:ℕ)*J.w1^(2:ℕ) + 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p1*J.r0*J.r1 - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ)))], ![(0), (0), (-(4*J.E^(2:ℕ)*J.p1*J.w0^(2:ℕ)*J.w1 + J.E^(2:ℕ)*J.w0^(2:ℕ)*J.w2 + 2*J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - J.r0^(2:ℕ)*J.w2)/(2*J.r0^(2:ℕ))), ((8*J.E^(2:ℕ)*J.p1*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.w0*J.w2 + 3*J.E^(2:ℕ)*J.w1^(2:ℕ) + 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ)))], ![(J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2 + 2*J.r0*J.r1*J.w1)/(4*J.r0^(2:ℕ))), (J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2)/(4*J.r0^(2:ℕ))), (0), (0)], ![((J.E^(4:ℕ)*J.w0^(2:ℕ)*J.w1^(2:ℕ) - 4*J.E^(2:ℕ)*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 16*J.E^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.E^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 4*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 3*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w1^(2:ℕ) + 2*J.E^(2:ℕ)*J.r0*J.r1*J.w0*J.w1 - 4*J.p1^(2:ℕ)*J.r0^(4:ℕ) + 4*J.p1*J.r0^(3:ℕ)*J.r1 + 4*J.p2*J.r0^(4:ℕ))/(4*J.E*J.r0^(2:ℕ))), ((J.E^(4:ℕ)*J.w0^(2:ℕ)*J.w1^(2:ℕ) - 4*J.E^(2:ℕ)*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 16*J.E^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.E^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 4*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 3*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(4:ℕ) + 4*J.p2*J.r0^(4:ℕ))/(4*J.E*J.r0^(2:ℕ))), (0), (0)]]], ![![![(0), (0), ((8*J.E^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.r0*J.w0*J.w2 + J.E^(2:ℕ)*J.r0*J.w1^(2:ℕ) - 2*J.E^(2:ℕ)*J.r1*J.w0*J.w1 - 4*J.p1^(2:ℕ)*J.r0^(3:ℕ) - 4*J.p2*J.r0^(3:ℕ))/(4*J.r0^(3:ℕ))), (-J.E^(2:ℕ)*(4*J.p1*J.r0*J.w1 + J.r0*J.w2 - J.r1*J.w1)/(2*J.r0^(3:ℕ)))], ![(0), (0), (-(8*J.E^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.r0*J.w0*J.w2 + J.E^(2:ℕ)*J.r0*J.w1^(2:ℕ) - 2*J.E^(2:ℕ)*J.r1*J.w0*J.w1 - 4*J.p1^(2:ℕ)*J.r0^(3:ℕ) - 4*J.p2*J.r0^(3:ℕ))/(4*J.r0^(3:ℕ))), (J.E^(2:ℕ)*(4*J.p1*J.r0*J.w1 + J.r0*J.w2 - J.r1*J.w1)/(2*J.r0^(3:ℕ)))], ![(J.E*(J.E^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ))), (J.E*(J.E^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ))), (0), (0)], ![(J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2 + 2*J.r0*J.r1*J.w1)/(4*J.r0^(2:ℕ))), (J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2 + 2*J.r0*J.r1*J.w1)/(4*J.r0^(2:ℕ))), (0), (0)]], ![![(0), (0), (-(8*J.E^(2:ℕ)*J.p1*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.w0*J.w2 + J.E^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ))), (J.E^(2:ℕ)*(4*J.p1*J.w1 + J.w2)/(2*J.r0^(2:ℕ)))], ![(0), (0), ((8*J.E^(2:ℕ)*J.p1*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.w0*J.w2 + J.E^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ))), (-J.E^(2:ℕ)*(4*J.p1*J.w1 + J.w2)/(2*J.r0^(2:ℕ)))], ![(-J.E*(J.E^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ))), (-J.E*(J.E^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ))), (0), (0)], ![(-J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2)/(4*J.r0^(2:ℕ))), (-J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2)/(4*J.r0^(2:ℕ))), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (J.E*J.r1*J.w1/(2*J.r0)), (0), (0)], ![(J.E*J.r1*J.w1/(2*J.r0)), (0), (0), (0)], ![(0), (0), (J.E*J.p1*J.r1*J.w0/J.r0), (-J.E*J.p1*J.r1/J.r0)], ![(0), (0), (J.p1*J.r1*(J.E^(2:ℕ)*J.w0^(2:ℕ) + J.r0^(2:ℕ))/(J.E*J.r0)), (-J.E*J.p1*J.r1*J.w0/J.r0)]]], ![![![(0), (0), ((4*J.E^(2:ℕ)*J.p1*J.r0*J.w0^(2:ℕ)*J.w1 + J.E^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w2 + 2*J.E^(2:ℕ)*J.r0*J.w0*J.w1^(2:ℕ) - J.E^(2:ℕ)*J.r1*J.w0^(2:ℕ)*J.w1 - 4*J.p1*J.r0^(3:ℕ)*J.w1 - 4*J.p1*J.r0^(2:ℕ)*J.r1*J.w0 - 4*J.p2*J.r0^(3:ℕ)*J.w0 - J.r0^(3:ℕ)*J.w2 + J.r0^(2:ℕ)*J.r1*J.w1 + 2*J.r0^(2:ℕ)*J.r2*J.w0)/(2*J.r0^(3:ℕ))), (-(8*J.E^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.r0*J.w0*J.w2 + 3*J.E^(2:ℕ)*J.r0*J.w1^(2:ℕ) - 2*J.E^(2:ℕ)*J.r1*J.w0*J.w1 + 4*J.p1^(2:ℕ)*J.r0^(3:ℕ) - 8*J.p1*J.r0^(2:ℕ)*J.r1 - 4*J.p2*J.r0^(3:ℕ) + 4*J.r0^(2:ℕ)*J.r2)/(4*J.r0^(3:ℕ)))], ![(0), (0), (-(4*J.E^(2:ℕ)*J.p1*J.r0*J.w0^(2:ℕ)*J.w1 + J.E^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w2 + 2*J.E^(2:ℕ)*J.r0*J.w0*J.w1^(2:ℕ) - J.E^(2:ℕ)*J.r1*J.w0^(2:ℕ)*J.w1 - 4*J.p1*J.r0^(3:ℕ)*J.w1 - 2*J.p1*J.r0^(2:ℕ)*J.r1*J.w0 - 4*J.p2*J.r0^(3:ℕ)*J.w0 - J.r0^(3:ℕ)*J.w2)/(2*J.r0^(3:ℕ))), ((8*J.E^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.r0*J.w0*J.w2 + 3*J.E^(2:ℕ)*J.r0*J.w1^(2:ℕ) - 2*J.E^(2:ℕ)*J.r1*J.w0*J.w1 + 4*J.p1^(2:ℕ)*J.r0^(3:ℕ) - 4*J.p1*J.r0^(2:ℕ)*J.r1 - 4*J.p2*J.r0^(3:ℕ))/(4*J.r0^(3:ℕ)))], ![(J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2 + 2*J.r0*J.r1*J.w1)/(4*J.r0^(2:ℕ))), (J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2)/(4*J.r0^(2:ℕ))), (0), (0)], ![((J.E^(4:ℕ)*J.w0^(2:ℕ)*J.w1^(2:ℕ) - 4*J.E^(2:ℕ)*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 16*J.E^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.E^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 4*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 3*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w1^(2:ℕ) + 4*J.E^(2:ℕ)*J.r0*J.r1*J.w0*J.w1 - 4*J.p1^(2:ℕ)*J.r0^(4:ℕ) + 8*J.p1*J.r0^(3:ℕ)*J.r1 + 4*J.p2*J.r0^(4:ℕ) - 4*J.r0^(3:ℕ)*J.r2)/(4*J.E*J.r0^(2:ℕ))), ((J.E^(4:ℕ)*J.w0^(2:ℕ)*J.w1^(2:ℕ) - 4*J.E^(2:ℕ)*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 16*J.E^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.E^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 4*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 3*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w1^(2:ℕ) + 2*J.E^(2:ℕ)*J.r0*J.r1*J.w0*J.w1 - 4*J.p1^(2:ℕ)*J.r0^(4:ℕ) + 4*J.p1*J.r0^(3:ℕ)*J.r1 + 4*J.p2*J.r0^(4:ℕ))/(4*J.E*J.r0^(2:ℕ))), (0), (0)]], ![![(0), (0), (-(4*J.E^(2:ℕ)*J.p1*J.w0^(2:ℕ)*J.w1 + J.E^(2:ℕ)*J.w0^(2:ℕ)*J.w2 + 2*J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1*J.r0^(2:ℕ)*J.w1 - 2*J.p1*J.r0*J.r1*J.w0 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - J.r0^(2:ℕ)*J.w2 + J.r0*J.r1*J.w1)/(2*J.r0^(2:ℕ))), ((8*J.E^(2:ℕ)*J.p1*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.w0*J.w2 + 3*J.E^(2:ℕ)*J.w1^(2:ℕ) + 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p1*J.r0*J.r1 - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ)))], ![(0), (0), ((4*J.E^(2:ℕ)*J.p1*J.w0^(2:ℕ)*J.w1 + J.E^(2:ℕ)*J.w0^(2:ℕ)*J.w2 + 2*J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - J.r0^(2:ℕ)*J.w2)/(2*J.r0^(2:ℕ))), (-(8*J.E^(2:ℕ)*J.p1*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.w0*J.w2 + 3*J.E^(2:ℕ)*J.w1^(2:ℕ) + 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ)))], ![(-J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2 + 2*J.r0*J.r1*J.w1)/(4*J.r0^(2:ℕ))), (-J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2)/(4*J.r0^(2:ℕ))), (0), (0)], ![(-(J.E^(4:ℕ)*J.w0^(2:ℕ)*J.w1^(2:ℕ) - 4*J.E^(2:ℕ)*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 16*J.E^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.E^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 4*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 3*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w1^(2:ℕ) + 2*J.E^(2:ℕ)*J.r0*J.r1*J.w0*J.w1 - 4*J.p1^(2:ℕ)*J.r0^(4:ℕ) + 4*J.p1*J.r0^(3:ℕ)*J.r1 + 4*J.p2*J.r0^(4:ℕ))/(4*J.E*J.r0^(2:ℕ))), (-(J.E^(4:ℕ)*J.w0^(2:ℕ)*J.w1^(2:ℕ) - 4*J.E^(2:ℕ)*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 16*J.E^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.E^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 4*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 3*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(4:ℕ) + 4*J.p2*J.r0^(4:ℕ))/(4*J.E*J.r0^(2:ℕ))), (0), (0)]], ![![(0), (-J.E*J.r1*J.w1/(2*J.r0)), (0), (0)], ![(-J.E*J.r1*J.w1/(2*J.r0)), (0), (0), (0)], ![(0), (0), (-J.E*J.p1*J.r1*J.w0/J.r0), (J.E*J.p1*J.r1/J.r0)], ![(0), (0), (-J.p1*J.r1*(J.E^(2:ℕ)*J.w0^(2:ℕ) + J.r0^(2:ℕ))/(J.E*J.r0)), (J.E*J.p1*J.r1*J.w0/J.r0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]]]]

noncomputable def RDT (J : Jet) : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ :=
  ![![![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (-J.E*J.r1*J.w1/(2*J.r0))], ![(0), (0), (J.E*J.r1*J.w1/(2*J.r0)), (0)]], ![![(0), (0), (J.E*(J.E^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ))), (J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2 + 2*J.r0*J.r1*J.w1)/(4*J.r0^(2:ℕ)))], ![(0), (0), (-J.E*(J.E^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ))), (-J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2 + 2*J.r0*J.r1*J.w1)/(4*J.r0^(2:ℕ)))], ![(-J.E*(J.E^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ))), (J.E*(J.E^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ))), (0), (0)], ![(-J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2 + 2*J.r0*J.r1*J.w1)/(4*J.r0^(2:ℕ))), (J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2 + 2*J.r0*J.r1*J.w1)/(4*J.r0^(2:ℕ))), (0), (0)]], ![![(0), (0), (J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2 + 2*J.r0*J.r1*J.w1)/(4*J.r0^(2:ℕ))), ((J.E^(4:ℕ)*J.w0^(2:ℕ)*J.w1^(2:ℕ) - 4*J.E^(2:ℕ)*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 16*J.E^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.E^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 4*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 3*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w1^(2:ℕ) + 4*J.E^(2:ℕ)*J.r0*J.r1*J.w0*J.w1 - 4*J.p1^(2:ℕ)*J.r0^(4:ℕ) + 8*J.p1*J.r0^(3:ℕ)*J.r1 + 4*J.p2*J.r0^(4:ℕ) - 4*J.r0^(3:ℕ)*J.r2)/(4*J.E*J.r0^(2:ℕ)))], ![(0), (0), (-J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2)/(4*J.r0^(2:ℕ))), (-(J.E^(4:ℕ)*J.w0^(2:ℕ)*J.w1^(2:ℕ) - 4*J.E^(2:ℕ)*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 16*J.E^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.E^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 4*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 3*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w1^(2:ℕ) + 2*J.E^(2:ℕ)*J.r0*J.r1*J.w0*J.w1 - 4*J.p1^(2:ℕ)*J.r0^(4:ℕ) + 4*J.p1*J.r0^(3:ℕ)*J.r1 + 4*J.p2*J.r0^(4:ℕ))/(4*J.E*J.r0^(2:ℕ)))], ![(-J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2 + 2*J.r0*J.r1*J.w1)/(4*J.r0^(2:ℕ))), (J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2)/(4*J.r0^(2:ℕ))), (0), (0)], ![(-(J.E^(4:ℕ)*J.w0^(2:ℕ)*J.w1^(2:ℕ) - 4*J.E^(2:ℕ)*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 16*J.E^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.E^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 4*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 3*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w1^(2:ℕ) + 4*J.E^(2:ℕ)*J.r0*J.r1*J.w0*J.w1 - 4*J.p1^(2:ℕ)*J.r0^(4:ℕ) + 8*J.p1*J.r0^(3:ℕ)*J.r1 + 4*J.p2*J.r0^(4:ℕ) - 4*J.r0^(3:ℕ)*J.r2)/(4*J.E*J.r0^(2:ℕ))), ((J.E^(4:ℕ)*J.w0^(2:ℕ)*J.w1^(2:ℕ) - 4*J.E^(2:ℕ)*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 16*J.E^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.E^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 4*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 3*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w1^(2:ℕ) + 2*J.E^(2:ℕ)*J.r0*J.r1*J.w0*J.w1 - 4*J.p1^(2:ℕ)*J.r0^(4:ℕ) + 4*J.p1*J.r0^(3:ℕ)*J.r1 + 4*J.p2*J.r0^(4:ℕ))/(4*J.E*J.r0^(2:ℕ))), (0), (0)]]], ![![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (J.E*J.r1*J.w1/(2*J.r0))], ![(0), (0), (-J.E*J.r1*J.w1/(2*J.r0)), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (-J.E*(J.E^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ))), (-J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2)/(4*J.r0^(2:ℕ)))], ![(0), (0), (J.E*(J.E^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ))), (J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2)/(4*J.r0^(2:ℕ)))], ![(J.E*(J.E^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ))), (-J.E*(J.E^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ))), (0), (0)], ![(J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2)/(4*J.r0^(2:ℕ))), (-J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2)/(4*J.r0^(2:ℕ))), (0), (0)]], ![![(0), (0), (-J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2 + 2*J.r0*J.r1*J.w1)/(4*J.r0^(2:ℕ))), (-(J.E^(4:ℕ)*J.w0^(2:ℕ)*J.w1^(2:ℕ) - 4*J.E^(2:ℕ)*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 16*J.E^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.E^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 4*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 3*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w1^(2:ℕ) + 2*J.E^(2:ℕ)*J.r0*J.r1*J.w0*J.w1 - 4*J.p1^(2:ℕ)*J.r0^(4:ℕ) + 4*J.p1*J.r0^(3:ℕ)*J.r1 + 4*J.p2*J.r0^(4:ℕ))/(4*J.E*J.r0^(2:ℕ)))], ![(0), (0), (J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2)/(4*J.r0^(2:ℕ))), ((J.E^(4:ℕ)*J.w0^(2:ℕ)*J.w1^(2:ℕ) - 4*J.E^(2:ℕ)*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 16*J.E^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.E^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 4*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 3*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(4:ℕ) + 4*J.p2*J.r0^(4:ℕ))/(4*J.E*J.r0^(2:ℕ)))], ![(J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2 + 2*J.r0*J.r1*J.w1)/(4*J.r0^(2:ℕ))), (-J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2)/(4*J.r0^(2:ℕ))), (0), (0)], ![((J.E^(4:ℕ)*J.w0^(2:ℕ)*J.w1^(2:ℕ) - 4*J.E^(2:ℕ)*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 16*J.E^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.E^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 4*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 3*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w1^(2:ℕ) + 2*J.E^(2:ℕ)*J.r0*J.r1*J.w0*J.w1 - 4*J.p1^(2:ℕ)*J.r0^(4:ℕ) + 4*J.p1*J.r0^(3:ℕ)*J.r1 + 4*J.p2*J.r0^(4:ℕ))/(4*J.E*J.r0^(2:ℕ))), (-(J.E^(4:ℕ)*J.w0^(2:ℕ)*J.w1^(2:ℕ) - 4*J.E^(2:ℕ)*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 16*J.E^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.E^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 4*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 3*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(4:ℕ) + 4*J.p2*J.r0^(4:ℕ))/(4*J.E*J.r0^(2:ℕ))), (0), (0)]]], ![![![(0), (0), (-J.E*(J.E^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ))), (-J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2 + 2*J.r0*J.r1*J.w1)/(4*J.r0^(2:ℕ)))], ![(0), (0), (J.E*(J.E^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ))), (J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2 + 2*J.r0*J.r1*J.w1)/(4*J.r0^(2:ℕ)))], ![(J.E*(J.E^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ))), (-J.E*(J.E^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ))), (0), (0)], ![(J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2 + 2*J.r0*J.r1*J.w1)/(4*J.r0^(2:ℕ))), (-J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2 + 2*J.r0*J.r1*J.w1)/(4*J.r0^(2:ℕ))), (0), (0)]], ![![(0), (0), (J.E*(J.E^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ))), (J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2)/(4*J.r0^(2:ℕ)))], ![(0), (0), (-J.E*(J.E^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ))), (-J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2)/(4*J.r0^(2:ℕ)))], ![(-J.E*(J.E^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ))), (J.E*(J.E^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ))), (0), (0)], ![(-J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2)/(4*J.r0^(2:ℕ))), (J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2)/(4*J.r0^(2:ℕ))), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (-J.E*J.r1*J.w1/(2*J.r0)), (0), (0)], ![(J.E*J.r1*J.w1/(2*J.r0)), (0), (0), (0)], ![(0), (0), (0), (J.p1*J.r0*J.r1)], ![(0), (0), (-J.p1*J.r0*J.r1), (0)]]], ![![![(0), (0), (-J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2 + 2*J.r0*J.r1*J.w1)/(4*J.r0^(2:ℕ))), (-(J.E^(4:ℕ)*J.w0^(2:ℕ)*J.w1^(2:ℕ) - 4*J.E^(2:ℕ)*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 16*J.E^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.E^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 4*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 3*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w1^(2:ℕ) + 4*J.E^(2:ℕ)*J.r0*J.r1*J.w0*J.w1 - 4*J.p1^(2:ℕ)*J.r0^(4:ℕ) + 8*J.p1*J.r0^(3:ℕ)*J.r1 + 4*J.p2*J.r0^(4:ℕ) - 4*J.r0^(3:ℕ)*J.r2)/(4*J.E*J.r0^(2:ℕ)))], ![(0), (0), (J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2)/(4*J.r0^(2:ℕ))), ((J.E^(4:ℕ)*J.w0^(2:ℕ)*J.w1^(2:ℕ) - 4*J.E^(2:ℕ)*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 16*J.E^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.E^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 4*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 3*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w1^(2:ℕ) + 2*J.E^(2:ℕ)*J.r0*J.r1*J.w0*J.w1 - 4*J.p1^(2:ℕ)*J.r0^(4:ℕ) + 4*J.p1*J.r0^(3:ℕ)*J.r1 + 4*J.p2*J.r0^(4:ℕ))/(4*J.E*J.r0^(2:ℕ)))], ![(J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2 + 2*J.r0*J.r1*J.w1)/(4*J.r0^(2:ℕ))), (-J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2)/(4*J.r0^(2:ℕ))), (0), (0)], ![((J.E^(4:ℕ)*J.w0^(2:ℕ)*J.w1^(2:ℕ) - 4*J.E^(2:ℕ)*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 16*J.E^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.E^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 4*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 3*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w1^(2:ℕ) + 4*J.E^(2:ℕ)*J.r0*J.r1*J.w0*J.w1 - 4*J.p1^(2:ℕ)*J.r0^(4:ℕ) + 8*J.p1*J.r0^(3:ℕ)*J.r1 + 4*J.p2*J.r0^(4:ℕ) - 4*J.r0^(3:ℕ)*J.r2)/(4*J.E*J.r0^(2:ℕ))), (-(J.E^(4:ℕ)*J.w0^(2:ℕ)*J.w1^(2:ℕ) - 4*J.E^(2:ℕ)*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 16*J.E^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.E^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 4*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 3*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w1^(2:ℕ) + 2*J.E^(2:ℕ)*J.r0*J.r1*J.w0*J.w1 - 4*J.p1^(2:ℕ)*J.r0^(4:ℕ) + 4*J.p1*J.r0^(3:ℕ)*J.r1 + 4*J.p2*J.r0^(4:ℕ))/(4*J.E*J.r0^(2:ℕ))), (0), (0)]], ![![(0), (0), (J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2 + 2*J.r0*J.r1*J.w1)/(4*J.r0^(2:ℕ))), ((J.E^(4:ℕ)*J.w0^(2:ℕ)*J.w1^(2:ℕ) - 4*J.E^(2:ℕ)*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 16*J.E^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.E^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 4*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 3*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w1^(2:ℕ) + 2*J.E^(2:ℕ)*J.r0*J.r1*J.w0*J.w1 - 4*J.p1^(2:ℕ)*J.r0^(4:ℕ) + 4*J.p1*J.r0^(3:ℕ)*J.r1 + 4*J.p2*J.r0^(4:ℕ))/(4*J.E*J.r0^(2:ℕ)))], ![(0), (0), (-J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2)/(4*J.r0^(2:ℕ))), (-(J.E^(4:ℕ)*J.w0^(2:ℕ)*J.w1^(2:ℕ) - 4*J.E^(2:ℕ)*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 16*J.E^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.E^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 4*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 3*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(4:ℕ) + 4*J.p2*J.r0^(4:ℕ))/(4*J.E*J.r0^(2:ℕ)))], ![(-J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2 + 2*J.r0*J.r1*J.w1)/(4*J.r0^(2:ℕ))), (J.E*(J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0 - 8*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - 2*J.r0^(2:ℕ)*J.w2)/(4*J.r0^(2:ℕ))), (0), (0)], ![(-(J.E^(4:ℕ)*J.w0^(2:ℕ)*J.w1^(2:ℕ) - 4*J.E^(2:ℕ)*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 16*J.E^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.E^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 4*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 3*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w1^(2:ℕ) + 2*J.E^(2:ℕ)*J.r0*J.r1*J.w0*J.w1 - 4*J.p1^(2:ℕ)*J.r0^(4:ℕ) + 4*J.p1*J.r0^(3:ℕ)*J.r1 + 4*J.p2*J.r0^(4:ℕ))/(4*J.E*J.r0^(2:ℕ))), ((J.E^(4:ℕ)*J.w0^(2:ℕ)*J.w1^(2:ℕ) - 4*J.E^(2:ℕ)*J.p1^(2:ℕ)*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 16*J.E^(2:ℕ)*J.p1*J.r0^(2:ℕ)*J.w0*J.w1 - 4*J.E^(2:ℕ)*J.p2*J.r0^(2:ℕ)*J.w0^(2:ℕ) - 4*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w0*J.w2 - 3*J.E^(2:ℕ)*J.r0^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(4:ℕ) + 4*J.p2*J.r0^(4:ℕ))/(4*J.E*J.r0^(2:ℕ))), (0), (0)]], ![![(0), (J.E*J.r1*J.w1/(2*J.r0)), (0), (0)], ![(-J.E*J.r1*J.w1/(2*J.r0)), (0), (0), (0)], ![(0), (0), (0), (-J.p1*J.r0*J.r1)], ![(0), (0), (J.p1*J.r0*J.r1), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]]]]

noncomputable def RUT (J : Jet) : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ :=
  ![![![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (-J.E*J.r1*J.w1/(2*J.r0^(3:ℕ)))], ![(0), (0), (J.E*J.r1*J.w1/(2*J.r0^(3:ℕ))), (0)]], ![![(0), (0), (-(8*J.E^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.r0*J.w0*J.w2 + J.E^(2:ℕ)*J.r0*J.w1^(2:ℕ) - 2*J.E^(2:ℕ)*J.r1*J.w0*J.w1 - 4*J.p1^(2:ℕ)*J.r0^(3:ℕ) - 4*J.p2*J.r0^(3:ℕ))/(4*J.r0^(3:ℕ))), (J.E^(2:ℕ)*(4*J.p1*J.r0*J.w1 + J.r0*J.w2 - J.r1*J.w1)/(2*J.r0^(3:ℕ)))], ![(0), (0), (-(8*J.E^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.r0*J.w0*J.w2 + J.E^(2:ℕ)*J.r0*J.w1^(2:ℕ) - 2*J.E^(2:ℕ)*J.r1*J.w0*J.w1 - 4*J.p1^(2:ℕ)*J.r0^(3:ℕ) - 4*J.p2*J.r0^(3:ℕ))/(4*J.r0^(3:ℕ))), (J.E^(2:ℕ)*(4*J.p1*J.r0*J.w1 + J.r0*J.w2 - J.r1*J.w1)/(2*J.r0^(3:ℕ)))], ![((8*J.E^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.r0*J.w0*J.w2 + J.E^(2:ℕ)*J.r0*J.w1^(2:ℕ) - 2*J.E^(2:ℕ)*J.r1*J.w0*J.w1 - 4*J.p1^(2:ℕ)*J.r0^(3:ℕ) - 4*J.p2*J.r0^(3:ℕ))/(4*J.r0^(3:ℕ))), ((8*J.E^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.r0*J.w0*J.w2 + J.E^(2:ℕ)*J.r0*J.w1^(2:ℕ) - 2*J.E^(2:ℕ)*J.r1*J.w0*J.w1 - 4*J.p1^(2:ℕ)*J.r0^(3:ℕ) - 4*J.p2*J.r0^(3:ℕ))/(4*J.r0^(3:ℕ))), (0), (0)], ![(-J.E^(2:ℕ)*(4*J.p1*J.r0*J.w1 + J.r0*J.w2 - J.r1*J.w1)/(2*J.r0^(3:ℕ))), (-J.E^(2:ℕ)*(4*J.p1*J.r0*J.w1 + J.r0*J.w2 - J.r1*J.w1)/(2*J.r0^(3:ℕ))), (0), (0)]], ![![(0), (0), (-(4*J.E^(2:ℕ)*J.p1*J.r0*J.w0^(2:ℕ)*J.w1 + J.E^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w2 + 2*J.E^(2:ℕ)*J.r0*J.w0*J.w1^(2:ℕ) - J.E^(2:ℕ)*J.r1*J.w0^(2:ℕ)*J.w1 - 4*J.p1*J.r0^(3:ℕ)*J.w1 - 4*J.p1*J.r0^(2:ℕ)*J.r1*J.w0 - 4*J.p2*J.r0^(3:ℕ)*J.w0 - J.r0^(3:ℕ)*J.w2 + J.r0^(2:ℕ)*J.r1*J.w1 + 2*J.r0^(2:ℕ)*J.r2*J.w0)/(2*J.r0^(3:ℕ))), ((8*J.E^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.r0*J.w0*J.w2 + 3*J.E^(2:ℕ)*J.r0*J.w1^(2:ℕ) - 2*J.E^(2:ℕ)*J.r1*J.w0*J.w1 + 4*J.p1^(2:ℕ)*J.r0^(3:ℕ) - 8*J.p1*J.r0^(2:ℕ)*J.r1 - 4*J.p2*J.r0^(3:ℕ) + 4*J.r0^(2:ℕ)*J.r2)/(4*J.r0^(3:ℕ)))], ![(0), (0), (-(4*J.E^(2:ℕ)*J.p1*J.r0*J.w0^(2:ℕ)*J.w1 + J.E^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w2 + 2*J.E^(2:ℕ)*J.r0*J.w0*J.w1^(2:ℕ) - J.E^(2:ℕ)*J.r1*J.w0^(2:ℕ)*J.w1 - 4*J.p1*J.r0^(3:ℕ)*J.w1 - 2*J.p1*J.r0^(2:ℕ)*J.r1*J.w0 - 4*J.p2*J.r0^(3:ℕ)*J.w0 - J.r0^(3:ℕ)*J.w2)/(2*J.r0^(3:ℕ))), ((8*J.E^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.r0*J.w0*J.w2 + 3*J.E^(2:ℕ)*J.r0*J.w1^(2:ℕ) - 2*J.E^(2:ℕ)*J.r1*J.w0*J.w1 + 4*J.p1^(2:ℕ)*J.r0^(3:ℕ) - 4*J.p1*J.r0^(2:ℕ)*J.r1 - 4*J.p2*J.r0^(3:ℕ))/(4*J.r0^(3:ℕ)))], ![((4*J.E^(2:ℕ)*J.p1*J.r0*J.w0^(2:ℕ)*J.w1 + J.E^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w2 + 2*J.E^(2:ℕ)*J.r0*J.w0*J.w1^(2:ℕ) - J.E^(2:ℕ)*J.r1*J.w0^(2:ℕ)*J.w1 - 4*J.p1*J.r0^(3:ℕ)*J.w1 - 4*J.p1*J.r0^(2:ℕ)*J.r1*J.w0 - 4*J.p2*J.r0^(3:ℕ)*J.w0 - J.r0^(3:ℕ)*J.w2 + J.r0^(2:ℕ)*J.r1*J.w1 + 2*J.r0^(2:ℕ)*J.r2*J.w0)/(2*J.r0^(3:ℕ))), ((4*J.E^(2:ℕ)*J.p1*J.r0*J.w0^(2:ℕ)*J.w1 + J.E^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w2 + 2*J.E^(2:ℕ)*J.r0*J.w0*J.w1^(2:ℕ) - J.E^(2:ℕ)*J.r1*J.w0^(2:ℕ)*J.w1 - 4*J.p1*J.r0^(3:ℕ)*J.w1 - 2*J.p1*J.r0^(2:ℕ)*J.r1*J.w0 - 4*J.p2*J.r0^(3:ℕ)*J.w0 - J.r0^(3:ℕ)*J.w2)/(2*J.r0^(3:ℕ))), (0), (0)], ![(-(8*J.E^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.r0*J.w0*J.w2 + 3*J.E^(2:ℕ)*J.r0*J.w1^(2:ℕ) - 2*J.E^(2:ℕ)*J.r1*J.w0*J.w1 + 4*J.p1^(2:ℕ)*J.r0^(3:ℕ) - 8*J.p1*J.r0^(2:ℕ)*J.r1 - 4*J.p2*J.r0^(3:ℕ) + 4*J.r0^(2:ℕ)*J.r2)/(4*J.r0^(3:ℕ))), (-(8*J.E^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.r0*J.w0*J.w2 + 3*J.E^(2:ℕ)*J.r0*J.w1^(2:ℕ) - 2*J.E^(2:ℕ)*J.r1*J.w0*J.w1 + 4*J.p1^(2:ℕ)*J.r0^(3:ℕ) - 4*J.p1*J.r0^(2:ℕ)*J.r1 - 4*J.p2*J.r0^(3:ℕ))/(4*J.r0^(3:ℕ))), (0), (0)]]], ![![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (J.E*J.r1*J.w1/(2*J.r0^(3:ℕ)))], ![(0), (0), (-J.E*J.r1*J.w1/(2*J.r0^(3:ℕ))), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), ((8*J.E^(2:ℕ)*J.p1*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.w0*J.w2 + J.E^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ))), (-J.E^(2:ℕ)*(4*J.p1*J.w1 + J.w2)/(2*J.r0^(2:ℕ)))], ![(0), (0), ((8*J.E^(2:ℕ)*J.p1*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.w0*J.w2 + J.E^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ))), (-J.E^(2:ℕ)*(4*J.p1*J.w1 + J.w2)/(2*J.r0^(2:ℕ)))], ![(-(8*J.E^(2:ℕ)*J.p1*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.w0*J.w2 + J.E^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ))), (-(8*J.E^(2:ℕ)*J.p1*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.w0*J.w2 + J.E^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ))), (0), (0)], ![(J.E^(2:ℕ)*(4*J.p1*J.w1 + J.w2)/(2*J.r0^(2:ℕ))), (J.E^(2:ℕ)*(4*J.p1*J.w1 + J.w2)/(2*J.r0^(2:ℕ))), (0), (0)]], ![![(0), (0), ((4*J.E^(2:ℕ)*J.p1*J.w0^(2:ℕ)*J.w1 + J.E^(2:ℕ)*J.w0^(2:ℕ)*J.w2 + 2*J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1*J.r0^(2:ℕ)*J.w1 - 2*J.p1*J.r0*J.r1*J.w0 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - J.r0^(2:ℕ)*J.w2 + J.r0*J.r1*J.w1)/(2*J.r0^(2:ℕ))), (-(8*J.E^(2:ℕ)*J.p1*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.w0*J.w2 + 3*J.E^(2:ℕ)*J.w1^(2:ℕ) + 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p1*J.r0*J.r1 - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ)))], ![(0), (0), ((4*J.E^(2:ℕ)*J.p1*J.w0^(2:ℕ)*J.w1 + J.E^(2:ℕ)*J.w0^(2:ℕ)*J.w2 + 2*J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - J.r0^(2:ℕ)*J.w2)/(2*J.r0^(2:ℕ))), (-(8*J.E^(2:ℕ)*J.p1*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.w0*J.w2 + 3*J.E^(2:ℕ)*J.w1^(2:ℕ) + 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ)))], ![(-(4*J.E^(2:ℕ)*J.p1*J.w0^(2:ℕ)*J.w1 + J.E^(2:ℕ)*J.w0^(2:ℕ)*J.w2 + 2*J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1*J.r0^(2:ℕ)*J.w1 - 2*J.p1*J.r0*J.r1*J.w0 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - J.r0^(2:ℕ)*J.w2 + J.r0*J.r1*J.w1)/(2*J.r0^(2:ℕ))), (-(4*J.E^(2:ℕ)*J.p1*J.w0^(2:ℕ)*J.w1 + J.E^(2:ℕ)*J.w0^(2:ℕ)*J.w2 + 2*J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - J.r0^(2:ℕ)*J.w2)/(2*J.r0^(2:ℕ))), (0), (0)], ![((8*J.E^(2:ℕ)*J.p1*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.w0*J.w2 + 3*J.E^(2:ℕ)*J.w1^(2:ℕ) + 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p1*J.r0*J.r1 - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ))), ((8*J.E^(2:ℕ)*J.p1*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.w0*J.w2 + 3*J.E^(2:ℕ)*J.w1^(2:ℕ) + 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ))), (0), (0)]]], ![![![(0), (0), ((8*J.E^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.r0*J.w0*J.w2 + J.E^(2:ℕ)*J.r0*J.w1^(2:ℕ) - 2*J.E^(2:ℕ)*J.r1*J.w0*J.w1 - 4*J.p1^(2:ℕ)*J.r0^(3:ℕ) - 4*J.p2*J.r0^(3:ℕ))/(4*J.r0^(3:ℕ))), (-J.E^(2:ℕ)*(4*J.p1*J.r0*J.w1 + J.r0*J.w2 - J.r1*J.w1)/(2*J.r0^(3:ℕ)))], ![(0), (0), ((8*J.E^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.r0*J.w0*J.w2 + J.E^(2:ℕ)*J.r0*J.w1^(2:ℕ) - 2*J.E^(2:ℕ)*J.r1*J.w0*J.w1 - 4*J.p1^(2:ℕ)*J.r0^(3:ℕ) - 4*J.p2*J.r0^(3:ℕ))/(4*J.r0^(3:ℕ))), (-J.E^(2:ℕ)*(4*J.p1*J.r0*J.w1 + J.r0*J.w2 - J.r1*J.w1)/(2*J.r0^(3:ℕ)))], ![(-(8*J.E^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.r0*J.w0*J.w2 + J.E^(2:ℕ)*J.r0*J.w1^(2:ℕ) - 2*J.E^(2:ℕ)*J.r1*J.w0*J.w1 - 4*J.p1^(2:ℕ)*J.r0^(3:ℕ) - 4*J.p2*J.r0^(3:ℕ))/(4*J.r0^(3:ℕ))), (-(8*J.E^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.r0*J.w0*J.w2 + J.E^(2:ℕ)*J.r0*J.w1^(2:ℕ) - 2*J.E^(2:ℕ)*J.r1*J.w0*J.w1 - 4*J.p1^(2:ℕ)*J.r0^(3:ℕ) - 4*J.p2*J.r0^(3:ℕ))/(4*J.r0^(3:ℕ))), (0), (0)], ![(J.E^(2:ℕ)*(4*J.p1*J.r0*J.w1 + J.r0*J.w2 - J.r1*J.w1)/(2*J.r0^(3:ℕ))), (J.E^(2:ℕ)*(4*J.p1*J.r0*J.w1 + J.r0*J.w2 - J.r1*J.w1)/(2*J.r0^(3:ℕ))), (0), (0)]], ![![(0), (0), (-(8*J.E^(2:ℕ)*J.p1*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.w0*J.w2 + J.E^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ))), (J.E^(2:ℕ)*(4*J.p1*J.w1 + J.w2)/(2*J.r0^(2:ℕ)))], ![(0), (0), (-(8*J.E^(2:ℕ)*J.p1*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.w0*J.w2 + J.E^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ))), (J.E^(2:ℕ)*(4*J.p1*J.w1 + J.w2)/(2*J.r0^(2:ℕ)))], ![((8*J.E^(2:ℕ)*J.p1*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.w0*J.w2 + J.E^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ))), ((8*J.E^(2:ℕ)*J.p1*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.w0*J.w2 + J.E^(2:ℕ)*J.w1^(2:ℕ) - 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ))), (0), (0)], ![(-J.E^(2:ℕ)*(4*J.p1*J.w1 + J.w2)/(2*J.r0^(2:ℕ))), (-J.E^(2:ℕ)*(4*J.p1*J.w1 + J.w2)/(2*J.r0^(2:ℕ))), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (J.E*J.r1*J.w1/(2*J.r0)), (0), (0)], ![(-J.E*J.r1*J.w1/(2*J.r0)), (0), (0), (0)], ![(0), (0), (0), (J.p1*J.r1/J.r0)], ![(0), (0), (-J.p1*J.r1/J.r0), (0)]]], ![![![(0), (0), ((4*J.E^(2:ℕ)*J.p1*J.r0*J.w0^(2:ℕ)*J.w1 + J.E^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w2 + 2*J.E^(2:ℕ)*J.r0*J.w0*J.w1^(2:ℕ) - J.E^(2:ℕ)*J.r1*J.w0^(2:ℕ)*J.w1 - 4*J.p1*J.r0^(3:ℕ)*J.w1 - 4*J.p1*J.r0^(2:ℕ)*J.r1*J.w0 - 4*J.p2*J.r0^(3:ℕ)*J.w0 - J.r0^(3:ℕ)*J.w2 + J.r0^(2:ℕ)*J.r1*J.w1 + 2*J.r0^(2:ℕ)*J.r2*J.w0)/(2*J.r0^(3:ℕ))), (-(8*J.E^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.r0*J.w0*J.w2 + 3*J.E^(2:ℕ)*J.r0*J.w1^(2:ℕ) - 2*J.E^(2:ℕ)*J.r1*J.w0*J.w1 + 4*J.p1^(2:ℕ)*J.r0^(3:ℕ) - 8*J.p1*J.r0^(2:ℕ)*J.r1 - 4*J.p2*J.r0^(3:ℕ) + 4*J.r0^(2:ℕ)*J.r2)/(4*J.r0^(3:ℕ)))], ![(0), (0), ((4*J.E^(2:ℕ)*J.p1*J.r0*J.w0^(2:ℕ)*J.w1 + J.E^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w2 + 2*J.E^(2:ℕ)*J.r0*J.w0*J.w1^(2:ℕ) - J.E^(2:ℕ)*J.r1*J.w0^(2:ℕ)*J.w1 - 4*J.p1*J.r0^(3:ℕ)*J.w1 - 2*J.p1*J.r0^(2:ℕ)*J.r1*J.w0 - 4*J.p2*J.r0^(3:ℕ)*J.w0 - J.r0^(3:ℕ)*J.w2)/(2*J.r0^(3:ℕ))), (-(8*J.E^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.r0*J.w0*J.w2 + 3*J.E^(2:ℕ)*J.r0*J.w1^(2:ℕ) - 2*J.E^(2:ℕ)*J.r1*J.w0*J.w1 + 4*J.p1^(2:ℕ)*J.r0^(3:ℕ) - 4*J.p1*J.r0^(2:ℕ)*J.r1 - 4*J.p2*J.r0^(3:ℕ))/(4*J.r0^(3:ℕ)))], ![(-(4*J.E^(2:ℕ)*J.p1*J.r0*J.w0^(2:ℕ)*J.w1 + J.E^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w2 + 2*J.E^(2:ℕ)*J.r0*J.w0*J.w1^(2:ℕ) - J.E^(2:ℕ)*J.r1*J.w0^(2:ℕ)*J.w1 - 4*J.p1*J.r0^(3:ℕ)*J.w1 - 4*J.p1*J.r0^(2:ℕ)*J.r1*J.w0 - 4*J.p2*J.r0^(3:ℕ)*J.w0 - J.r0^(3:ℕ)*J.w2 + J.r0^(2:ℕ)*J.r1*J.w1 + 2*J.r0^(2:ℕ)*J.r2*J.w0)/(2*J.r0^(3:ℕ))), (-(4*J.E^(2:ℕ)*J.p1*J.r0*J.w0^(2:ℕ)*J.w1 + J.E^(2:ℕ)*J.r0*J.w0^(2:ℕ)*J.w2 + 2*J.E^(2:ℕ)*J.r0*J.w0*J.w1^(2:ℕ) - J.E^(2:ℕ)*J.r1*J.w0^(2:ℕ)*J.w1 - 4*J.p1*J.r0^(3:ℕ)*J.w1 - 2*J.p1*J.r0^(2:ℕ)*J.r1*J.w0 - 4*J.p2*J.r0^(3:ℕ)*J.w0 - J.r0^(3:ℕ)*J.w2)/(2*J.r0^(3:ℕ))), (0), (0)], ![((8*J.E^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.r0*J.w0*J.w2 + 3*J.E^(2:ℕ)*J.r0*J.w1^(2:ℕ) - 2*J.E^(2:ℕ)*J.r1*J.w0*J.w1 + 4*J.p1^(2:ℕ)*J.r0^(3:ℕ) - 8*J.p1*J.r0^(2:ℕ)*J.r1 - 4*J.p2*J.r0^(3:ℕ) + 4*J.r0^(2:ℕ)*J.r2)/(4*J.r0^(3:ℕ))), ((8*J.E^(2:ℕ)*J.p1*J.r0*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.r0*J.w0*J.w2 + 3*J.E^(2:ℕ)*J.r0*J.w1^(2:ℕ) - 2*J.E^(2:ℕ)*J.r1*J.w0*J.w1 + 4*J.p1^(2:ℕ)*J.r0^(3:ℕ) - 4*J.p1*J.r0^(2:ℕ)*J.r1 - 4*J.p2*J.r0^(3:ℕ))/(4*J.r0^(3:ℕ))), (0), (0)]], ![![(0), (0), (-(4*J.E^(2:ℕ)*J.p1*J.w0^(2:ℕ)*J.w1 + J.E^(2:ℕ)*J.w0^(2:ℕ)*J.w2 + 2*J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1*J.r0^(2:ℕ)*J.w1 - 2*J.p1*J.r0*J.r1*J.w0 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - J.r0^(2:ℕ)*J.w2 + J.r0*J.r1*J.w1)/(2*J.r0^(2:ℕ))), ((8*J.E^(2:ℕ)*J.p1*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.w0*J.w2 + 3*J.E^(2:ℕ)*J.w1^(2:ℕ) + 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p1*J.r0*J.r1 - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ)))], ![(0), (0), (-(4*J.E^(2:ℕ)*J.p1*J.w0^(2:ℕ)*J.w1 + J.E^(2:ℕ)*J.w0^(2:ℕ)*J.w2 + 2*J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - J.r0^(2:ℕ)*J.w2)/(2*J.r0^(2:ℕ))), ((8*J.E^(2:ℕ)*J.p1*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.w0*J.w2 + 3*J.E^(2:ℕ)*J.w1^(2:ℕ) + 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ)))], ![((4*J.E^(2:ℕ)*J.p1*J.w0^(2:ℕ)*J.w1 + J.E^(2:ℕ)*J.w0^(2:ℕ)*J.w2 + 2*J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1*J.r0^(2:ℕ)*J.w1 - 2*J.p1*J.r0*J.r1*J.w0 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - J.r0^(2:ℕ)*J.w2 + J.r0*J.r1*J.w1)/(2*J.r0^(2:ℕ))), ((4*J.E^(2:ℕ)*J.p1*J.w0^(2:ℕ)*J.w1 + J.E^(2:ℕ)*J.w0^(2:ℕ)*J.w2 + 2*J.E^(2:ℕ)*J.w0*J.w1^(2:ℕ) - 4*J.p1*J.r0^(2:ℕ)*J.w1 - 4*J.p2*J.r0^(2:ℕ)*J.w0 - J.r0^(2:ℕ)*J.w2)/(2*J.r0^(2:ℕ))), (0), (0)], ![(-(8*J.E^(2:ℕ)*J.p1*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.w0*J.w2 + 3*J.E^(2:ℕ)*J.w1^(2:ℕ) + 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p1*J.r0*J.r1 - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ))), (-(8*J.E^(2:ℕ)*J.p1*J.w0*J.w1 + 2*J.E^(2:ℕ)*J.w0*J.w2 + 3*J.E^(2:ℕ)*J.w1^(2:ℕ) + 4*J.p1^(2:ℕ)*J.r0^(2:ℕ) - 4*J.p2*J.r0^(2:ℕ))/(4*J.r0^(2:ℕ))), (0), (0)]], ![![(0), (-J.E*J.r1*J.w1/(2*J.r0)), (0), (0)], ![(J.E*J.r1*J.w1/(2*J.r0)), (0), (0), (0)], ![(0), (0), (0), (-J.p1*J.r1/J.r0)], ![(0), (0), (J.p1*J.r1/J.r0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]]]]

lemma GiT_ok (J : Jet) (hE : J.E ≠ 0) (hr : J.r0 ≠ 0) (m k : Fin 4) :
    ∑ l, GT J m l * GiT J l k = if m = k then 1 else 0 := by
  fin_cases m <;> fin_cases k <;> simp [Fin.sum_univ_four, GT, GiT] <;> (try field_simp) <;> ring1

lemma GamT_ok (J : Jet) (hE : J.E ≠ 0) (hr : J.r0 ≠ 0) (i j k : Fin 4) :
    GamF (D1T J) (GiT J) i j k = GamT J i j k := by
  simp only [GamF]
  fin_cases i <;> fin_cases j <;> fin_cases k <;> simp [Fin.sum_univ_four, D1T, GiT, GamT] <;> (try field_simp) <;> ring1

lemma DGT_ok (J : Jet) (hE : J.E ≠ 0) (hr : J.r0 ≠ 0) (u i j k : Fin 4) :
    DGamF (D1T J) (D2T J) (GiT J) u i j k = DGT J u i j k := by
  simp only [DGamF, GamT_ok J hE hr]
  fin_cases u <;> fin_cases i <;> fin_cases j <;> fin_cases k <;>
    simp [Fin.sum_univ_four, D2T, D1T, GiT, GamT, DGT] <;> (try field_simp) <;> ring1

lemma RT_ok (J : Jet) (hE : J.E ≠ 0) (hr : J.r0 ≠ 0) (i j k l : Fin 4) :
    RiemF (D1T J) (D2T J) (GiT J) i j k l = RT J i j k l := by
  simp only [RiemF, DGT_ok J hE hr, GamT_ok J hE hr]
  fin_cases i <;> fin_cases j <;> fin_cases k <;> fin_cases l <;>
    simp [Fin.sum_univ_four, DGT, GamT, RT] <;> (try field_simp) <;> ring1

lemma RDT_ok (J : Jet) (hE : J.E ≠ 0) (hr : J.r0 ≠ 0) (m n a b : Fin 4) :
    lowR (Matrix.of (GT J)) (RT J) m n a b = RDT J m n a b := by
  fin_cases m <;> fin_cases n <;> fin_cases a <;> fin_cases b <;>
    simp [lowR, Fin.sum_univ_four, GT, RT, RDT] <;> (try field_simp) <;> ring1

lemma RUT_ok (J : Jet) (hE : J.E ≠ 0) (hr : J.r0 ≠ 0) (m n a b : Fin 4) :
    raiseR (Matrix.of (GT J)) (Matrix.of (GiT J)) (RT J) m n a b = RUT J m n a b := by
  simp only [raiseR, RDT_ok J hE hr, Matrix.of_apply]
  fin_cases m <;> fin_cases n <;> fin_cases a <;> fin_cases b <;>
    simp [Fin.sum_univ_four, GiT, RDT, RUT] <;> (try field_simp) <;> ring1

lemma det_ok (J : Jet) (hE : J.E ≠ 0) : (Matrix.of (GT J)).det = -J.r0 ^ 2 := by
  simp [Matrix.det_succ_row_zero, Fin.sum_univ_succ, GT]
  field_simp
  ring

/-- **The density from the tables**: `½ ε R R / √(−det g) = 4E(4ψ′ω′RR″ − 2ψ′ω′R′² + ω″RR″)/(R²|R|)`. -/
lemma pont_ok (J : Jet) (hE : J.E ≠ 0) (hr : J.r0 ≠ 0) :
    pontArr (Matrix.of (GT J)) (Matrix.of (GiT J)) (RT J)
      = 4 * J.E * (4 * J.p1 * J.w1 * J.r0 * J.r2 - 2 * J.p1 * J.w1 * J.r1 ^ 2 + J.w2 * J.r0 * J.r2)
        / (J.r0 ^ 2 * |J.r0|) := by
  rw [pontArr, sum_eps, det_ok J hE, neg_neg, Real.sqrt_sq_eq_abs]
  simp only [RDT_ok J hE hr, RUT_ok J hE hr]
  have ha : |J.r0| ≠ 0 := abs_ne_zero.2 hr
  simp [Fin.sum_univ_four, RDT, RUT]
  field_simp
  ring

/-- The `μ`-sum of the current against `ε` with `μ` fixed, written out. -/
lemma sum_eps_mu (f : Fin 4 → Fin 4 → Fin 4 → ℝ) :
    (∑ ν, ∑ ρ, ∑ σ, (eps4 0 ν ρ σ : ℝ) * f ν ρ σ = f 1 2 3 - f 1 3 2 - f 2 1 3 + f 2 3 1 + f 3 1 2 - f 3 2 1) ∧
    (∑ ν, ∑ ρ, ∑ σ, (eps4 1 ν ρ σ : ℝ) * f ν ρ σ = -f 0 2 3 + f 0 3 2 + f 2 0 3 - f 2 3 0 - f 3 0 2 + f 3 2 0) ∧
    (∑ ν, ∑ ρ, ∑ σ, (eps4 2 ν ρ σ : ℝ) * f ν ρ σ = f 0 1 3 - f 0 3 1 - f 1 0 3 + f 1 3 0 + f 3 0 1 - f 3 1 0) ∧
    (∑ ν, ∑ ρ, ∑ σ, (eps4 3 ν ρ σ : ℝ) * f ν ρ σ = -f 0 1 2 + f 0 2 1 + f 1 0 2 - f 1 2 0 - f 2 0 1 + f 2 1 0) := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;>
  · simp [Fin.sum_univ_four, eps4, show Int.sign 2 = 1 from rfl, show Int.sign 3 = 1 from rfl]
    ring1

/-- **The current from the tables**: `K^t = −2E R′(6ψ′ω′ + ω″)/R`, `K^z = −2E(6ψ′RR′ω′ + RR′ω″ − RR″ω′ − R′²ω′)/R²`,
`K^x = K^y = 0`. -/
lemma cs_ok (J : Jet) (hr : J.r0 ≠ 0) :
    csArr (GamT J) (DGT J) 0 = -2 * J.E * J.r1 * (6 * J.p1 * J.w1 + J.w2) / J.r0 ∧
    csArr (GamT J) (DGT J) 1
      = -2 * J.E * (6 * J.p1 * J.r0 * J.r1 * J.w1 + J.r0 * J.r1 * J.w2 - J.r0 * J.r2 * J.w1 - J.r1 ^ 2 * J.w1)
        / J.r0 ^ 2 ∧
    csArr (GamT J) (DGT J) 2 = 0 ∧ csArr (GamT J) (DGT J) 3 = 0 := by
  obtain ⟨e0, e1, e2, e3⟩ := sum_eps_mu (fun ν ρ σ =>
    ∑ a, ∑ b, GamT J ν b a * DGT J ρ σ a b + 2 / 3 * ∑ a, ∑ b, ∑ c, GamT J ν b a * GamT J ρ c b * GamT J σ a c)
  simp only [csArr, e0, e1, e2, e3]
  refine ⟨?_, ?_, ?_, ?_⟩ <;>
  · simp [Fin.sum_univ_four, GamT, DGT]
    try field_simp
    try ring1

end Gowdy

/-! ## The bridge to explicit tables -/

section Bridge

variable {G : Fin 4 → Fin 4 → (Fin 4 → ℝ) → ℝ} (hs : ∀ i j p, G i j p = G j i p)
  (hn : ∀ p (u : Fin 4 → ℝ), (∀ v, formG G p u v = 0) → u = 0) (hGs : ∀ i j, ContDiff ℝ ∞ (G i j))

include hn hGs in
/-- **The bridge.** If at `p` the metric, a right inverse, and the first and second partials are given by tables,
THE connection's density and current are the recipe on those tables. -/
theorem tabs_bridge {p : Fin 4 → ℝ} {g gi : Fin 4 → Fin 4 → ℝ} {d1 : Fin 4 → Fin 4 → Fin 4 → ℝ}
    {d2 : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ} (hg : ∀ i j, G i j p = g i j)
    (hinv : ∀ m k, ∑ l, G m l p * gi l k = if m = k then 1 else 0)
    (h1 : ∀ i j c, d1At G p i j c = d1 i j c) (h2 : ∀ i j a c, d2At G p i j a c = d2 i j a c) :
    pontryaginLC G hs hn hGs p = pontArr (Matrix.of g) (Matrix.of gi) (RiemF d1 d2 gi) ∧
      ∀ μ, csLC G hs hn hGs p μ = csArr (GamF d1 gi) (DGamF d1 d2 gi) μ := by
  have hgm : gm G p = Matrix.of g := by ext i j; simp [gm, hg]
  have hgi : gmi G p = gi := funext fun l => funext fun k => by
    simp only [gmi, gm_inv hinv, Matrix.of_apply]
  have hd1 : d1At G p = d1 := funext fun i => funext fun j => funext fun c => h1 i j c
  have hd2 : d2At G p = d2 := funext fun i => funext fun j => funext fun a => funext fun c => h2 i j a c
  refine ⟨?_, fun μ => ?_⟩
  · rw [pontryaginLC, riemLC_tab hs hn hGs, gm_inv hinv, hgi, hd1, hd2, hgm]
  · rw [csLC_tab hs hn hGs, hgi, hd1, hd2]

end Bridge

/-! ## Part 1: the Nariai member `dS₂ × S²`, and its rotated (non-diagonal) form -/

section Nariai

set_option synthInstance.maxHeartbeats 400000

/-- The jet at the point: `a, b` and two derivatives at `χ = x¹`; `c, e` and two derivatives at `θ = x²`; the constant `w`. -/
structure NJet where
  a0 : ℝ
  a1 : ℝ
  a2 : ℝ
  b0 : ℝ
  b1 : ℝ
  b2 : ℝ
  c0 : ℝ
  c1 : ℝ
  c2 : ℝ
  e0 : ℝ
  e1 : ℝ
  e2 : ℝ
  w : ℝ

noncomputable def NGT (J : NJet) : Fin 4 → Fin 4 → ℝ :=
  ![![(J.a0), (0), (0), (J.e0*J.w)], ![(0), (J.b0), (0), (0)], ![(0), (0), (J.c0), (0)], ![(J.e0*J.w), (0), (0), (J.e0)]]

noncomputable def NGiT (J : NJet) : Fin 4 → Fin 4 → ℝ :=
  ![![(1/(J.a0 - J.e0*J.w^(2:ℕ))), (0), (0), (-J.w/(J.a0 - J.e0*J.w^(2:ℕ)))], ![(0), (1/J.b0), (0), (0)], ![(0), (0), (1/J.c0), (0)], ![(-J.w/(J.a0 - J.e0*J.w^(2:ℕ))), (0), (0), (J.a0/(J.e0*(J.a0 - J.e0*J.w^(2:ℕ))))]]

noncomputable def ND1T (J : NJet) : Fin 4 → Fin 4 → Fin 4 → ℝ :=
  ![![![(0), (J.a1), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (J.e1*J.w), (0)]], ![![(0), (0), (0), (0)], ![(0), (J.b1), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (J.c1), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (J.e1*J.w), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (J.e1), (0)]]]

noncomputable def ND2T (J : NJet) : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ :=
  ![![![![(0), (0), (0), (0)], ![(0), (J.a2), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (J.e2*J.w), (0)], ![(0), (0), (0), (0)]]], ![![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (J.b2), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]]], ![![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (J.c2), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]]], ![![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (J.e2*J.w), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (J.e2), (0)], ![(0), (0), (0), (0)]]]]

noncomputable def NGamT (J : NJet) : Fin 4 → Fin 4 → Fin 4 → ℝ :=
  ![![![(0), (-J.a1/(2*J.b0)), (0), (0)], ![(J.a1/(2*(J.a0 - J.e0*J.w^(2:ℕ)))), (0), (0), (-J.a1*J.w/(2*(J.a0 - J.e0*J.w^(2:ℕ))))], ![(-J.e1*J.w^(2:ℕ)/(2*(J.a0 - J.e0*J.w^(2:ℕ)))), (0), (0), (J.a0*J.e1*J.w/(2*J.e0*(J.a0 - J.e0*J.w^(2:ℕ))))], ![(0), (0), (-J.e1*J.w/(2*J.c0)), (0)]], ![![(J.a1/(2*(J.a0 - J.e0*J.w^(2:ℕ)))), (0), (0), (-J.a1*J.w/(2*(J.a0 - J.e0*J.w^(2:ℕ))))], ![(0), (J.b1/(2*J.b0)), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(-J.e1*J.w^(2:ℕ)/(2*(J.a0 - J.e0*J.w^(2:ℕ)))), (0), (0), (J.a0*J.e1*J.w/(2*J.e0*(J.a0 - J.e0*J.w^(2:ℕ))))], ![(0), (0), (0), (0)], ![(0), (0), (J.c1/(2*J.c0)), (0)], ![(0), (0), (0), (J.e1/(2*J.e0))]], ![![(0), (0), (-J.e1*J.w/(2*J.c0)), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (J.e1/(2*J.e0))], ![(0), (0), (-J.e1/(2*J.c0)), (0)]]]

noncomputable def NDGT (J : NJet) : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ :=
  ![![![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]]], ![![![(0), ((J.a1*J.b1 - J.a2*J.b0)/(2*J.b0^(2:ℕ))), (0), (0)], ![((J.a0*J.a2 - J.a1^(2:ℕ) - J.a2*J.e0*J.w^(2:ℕ))/(2*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ))), (0), (0), (-J.w*(J.a0*J.a2 - J.a1^(2:ℕ) - J.a2*J.e0*J.w^(2:ℕ))/(2*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ)))], ![(J.a1*J.e1*J.w^(2:ℕ)/(2*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ))), (0), (0), (-J.a1*J.e1*J.w^(3:ℕ)/(2*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ)))], ![(0), (0), (0), (0)]], ![![((J.a0*J.a2 - J.a1^(2:ℕ) - J.a2*J.e0*J.w^(2:ℕ))/(2*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ))), (0), (0), (-J.w*(J.a0*J.a2 - J.a1^(2:ℕ) - J.a2*J.e0*J.w^(2:ℕ))/(2*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ)))], ![(0), ((J.b0*J.b2 - J.b1^(2:ℕ))/(2*J.b0^(2:ℕ))), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(J.a1*J.e1*J.w^(2:ℕ)/(2*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ))), (0), (0), (-J.a1*J.e1*J.w^(3:ℕ)/(2*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ)))], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]]], ![![![(0), (0), (0), (0)], ![(J.a1*J.e1*J.w^(2:ℕ)/(2*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ))), (0), (0), (-J.a1*J.e1*J.w^(3:ℕ)/(2*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ)))], ![(-J.w^(2:ℕ)*(J.a0*J.e2 - J.e0*J.e2*J.w^(2:ℕ) + J.e1^(2:ℕ)*J.w^(2:ℕ))/(2*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ))), (0), (0), (J.a0*J.w*(J.a0*J.e0*J.e2 - J.a0*J.e1^(2:ℕ) - J.e0^(2:ℕ)*J.e2*J.w^(2:ℕ) + 2*J.e0*J.e1^(2:ℕ)*J.w^(2:ℕ))/(2*J.e0^(2:ℕ)*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ)))], ![(0), (0), (-J.w*(J.c0*J.e2 - J.c1*J.e1)/(2*J.c0^(2:ℕ))), (0)]], ![![(J.a1*J.e1*J.w^(2:ℕ)/(2*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ))), (0), (0), (-J.a1*J.e1*J.w^(3:ℕ)/(2*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ)))], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(-J.w^(2:ℕ)*(J.a0*J.e2 - J.e0*J.e2*J.w^(2:ℕ) + J.e1^(2:ℕ)*J.w^(2:ℕ))/(2*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ))), (0), (0), (J.a0*J.w*(J.a0*J.e0*J.e2 - J.a0*J.e1^(2:ℕ) - J.e0^(2:ℕ)*J.e2*J.w^(2:ℕ) + 2*J.e0*J.e1^(2:ℕ)*J.w^(2:ℕ))/(2*J.e0^(2:ℕ)*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ)))], ![(0), (0), (0), (0)], ![(0), (0), ((J.c0*J.c2 - J.c1^(2:ℕ))/(2*J.c0^(2:ℕ))), (0)], ![(0), (0), (0), ((J.e0*J.e2 - J.e1^(2:ℕ))/(2*J.e0^(2:ℕ)))]], ![![(0), (0), (-J.w*(J.c0*J.e2 - J.c1*J.e1)/(2*J.c0^(2:ℕ))), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), ((J.e0*J.e2 - J.e1^(2:ℕ))/(2*J.e0^(2:ℕ)))], ![(0), (0), (-(J.c0*J.e2 - J.c1*J.e1)/(2*J.c0^(2:ℕ))), (0)]]], ![![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]]]]

noncomputable def NRT (J : NJet) : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ :=
  ![![![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (-(J.a0*J.a1*J.b1 - 2*J.a0*J.a2*J.b0 + J.a1^(2:ℕ)*J.b0 - J.a1*J.b1*J.e0*J.w^(2:ℕ) + 2*J.a2*J.b0*J.e0*J.w^(2:ℕ))/(4*J.b0^(2:ℕ)*(J.a0 - J.e0*J.w^(2:ℕ)))), (J.a1*J.e1*J.w^(2:ℕ)/(4*J.c0*(J.a0 - J.e0*J.w^(2:ℕ)))), (0)], ![((J.a0*J.a1*J.b1 - 2*J.a0*J.a2*J.b0 + J.a1^(2:ℕ)*J.b0 - J.a1*J.b1*J.e0*J.w^(2:ℕ) + 2*J.a2*J.b0*J.e0*J.w^(2:ℕ))/(4*J.b0*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ))), (0), (0), (-J.w*(J.a0*J.a1*J.b1 - 2*J.a0*J.a2*J.b0 + J.a1^(2:ℕ)*J.b0 - J.a1*J.b1*J.e0*J.w^(2:ℕ) + 2*J.a2*J.b0*J.e0*J.w^(2:ℕ))/(4*J.b0*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ)))], ![(-J.a1*J.e1*J.w^(2:ℕ)/(4*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ))), (0), (0), (J.a1*J.e1*J.w^(3:ℕ)/(4*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ)))], ![(0), (0), (0), (0)]], ![![(0), (J.a1*J.e1*J.w^(2:ℕ)/(4*J.b0*(J.a0 - J.e0*J.w^(2:ℕ)))), (-J.a0*J.e1^(2:ℕ)*J.w^(2:ℕ)/(4*J.c0*J.e0*(J.a0 - J.e0*J.w^(2:ℕ)))), (0)], ![(-J.a1*J.e1*J.w^(2:ℕ)/(4*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ))), (0), (0), (J.a1*J.e1*J.w^(3:ℕ)/(4*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ)))], ![(J.w^(2:ℕ)*(2*J.a0*J.c0*J.e2 - J.a0*J.c1*J.e1 - 2*J.c0*J.e0*J.e2*J.w^(2:ℕ) + J.c0*J.e1^(2:ℕ)*J.w^(2:ℕ) + J.c1*J.e0*J.e1*J.w^(2:ℕ))/(4*J.c0*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ))), (0), (0), (-J.a0*J.w*(2*J.a0*J.c0*J.e0*J.e2 - J.a0*J.c0*J.e1^(2:ℕ) - J.a0*J.c1*J.e0*J.e1 - 2*J.c0*J.e0^(2:ℕ)*J.e2*J.w^(2:ℕ) + 2*J.c0*J.e0*J.e1^(2:ℕ)*J.w^(2:ℕ) + J.c1*J.e0^(2:ℕ)*J.e1*J.w^(2:ℕ))/(4*J.c0*J.e0^(2:ℕ)*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ)))], ![(0), (0), (J.w*(2*J.c0*J.e0*J.e2 - J.c0*J.e1^(2:ℕ) - J.c1*J.e0*J.e1)/(4*J.c0^(2:ℕ)*J.e0)), (0)]], ![![(J.e1^(2:ℕ)*J.w^(3:ℕ)/(4*J.c0*(J.a0 - J.e0*J.w^(2:ℕ)))), (0), (0), (-J.a0*J.e1^(2:ℕ)*J.w^(2:ℕ)/(4*J.c0*J.e0*(J.a0 - J.e0*J.w^(2:ℕ))))], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(J.e1^(2:ℕ)*J.w^(2:ℕ)/(4*J.c0*(J.a0 - J.e0*J.w^(2:ℕ)))), (0), (0), (-J.e1^(2:ℕ)*J.w^(3:ℕ)/(4*J.c0*(J.a0 - J.e0*J.w^(2:ℕ))))]]], ![![![(0), ((J.a0*J.a1*J.b1 - 2*J.a0*J.a2*J.b0 + J.a1^(2:ℕ)*J.b0 - J.a1*J.b1*J.e0*J.w^(2:ℕ) + 2*J.a2*J.b0*J.e0*J.w^(2:ℕ))/(4*J.b0^(2:ℕ)*(J.a0 - J.e0*J.w^(2:ℕ)))), (-J.a1*J.e1*J.w^(2:ℕ)/(4*J.c0*(J.a0 - J.e0*J.w^(2:ℕ)))), (0)], ![(-(J.a0*J.a1*J.b1 - 2*J.a0*J.a2*J.b0 + J.a1^(2:ℕ)*J.b0 - J.a1*J.b1*J.e0*J.w^(2:ℕ) + 2*J.a2*J.b0*J.e0*J.w^(2:ℕ))/(4*J.b0*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ))), (0), (0), (J.w*(J.a0*J.a1*J.b1 - 2*J.a0*J.a2*J.b0 + J.a1^(2:ℕ)*J.b0 - J.a1*J.b1*J.e0*J.w^(2:ℕ) + 2*J.a2*J.b0*J.e0*J.w^(2:ℕ))/(4*J.b0*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ)))], ![(J.a1*J.e1*J.w^(2:ℕ)/(4*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ))), (0), (0), (-J.a1*J.e1*J.w^(3:ℕ)/(4*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ)))], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]]], ![![![(0), (-J.a1*J.e1*J.w^(2:ℕ)/(4*J.b0*(J.a0 - J.e0*J.w^(2:ℕ)))), (J.a0*J.e1^(2:ℕ)*J.w^(2:ℕ)/(4*J.c0*J.e0*(J.a0 - J.e0*J.w^(2:ℕ)))), (0)], ![(J.a1*J.e1*J.w^(2:ℕ)/(4*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ))), (0), (0), (-J.a1*J.e1*J.w^(3:ℕ)/(4*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ)))], ![(-J.w^(2:ℕ)*(2*J.a0*J.c0*J.e2 - J.a0*J.c1*J.e1 - 2*J.c0*J.e0*J.e2*J.w^(2:ℕ) + J.c0*J.e1^(2:ℕ)*J.w^(2:ℕ) + J.c1*J.e0*J.e1*J.w^(2:ℕ))/(4*J.c0*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ))), (0), (0), (J.a0*J.w*(2*J.a0*J.c0*J.e0*J.e2 - J.a0*J.c0*J.e1^(2:ℕ) - J.a0*J.c1*J.e0*J.e1 - 2*J.c0*J.e0^(2:ℕ)*J.e2*J.w^(2:ℕ) + 2*J.c0*J.e0*J.e1^(2:ℕ)*J.w^(2:ℕ) + J.c1*J.e0^(2:ℕ)*J.e1*J.w^(2:ℕ))/(4*J.c0*J.e0^(2:ℕ)*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ)))], ![(0), (0), (-J.w*(2*J.c0*J.e0*J.e2 - J.c0*J.e1^(2:ℕ) - J.c1*J.e0*J.e1)/(4*J.c0^(2:ℕ)*J.e0)), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (-J.w*(2*J.c0*J.e0*J.e2 - J.c0*J.e1^(2:ℕ) - J.c1*J.e0*J.e1)/(4*J.c0^(2:ℕ)*J.e0)), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), ((2*J.c0*J.e0*J.e2 - J.c0*J.e1^(2:ℕ) - J.c1*J.e0*J.e1)/(4*J.c0*J.e0^(2:ℕ)))], ![(0), (0), (-(2*J.c0*J.e0*J.e2 - J.c0*J.e1^(2:ℕ) - J.c1*J.e0*J.e1)/(4*J.c0^(2:ℕ)*J.e0)), (0)]]], ![![![(-J.e1^(2:ℕ)*J.w^(3:ℕ)/(4*J.c0*(J.a0 - J.e0*J.w^(2:ℕ)))), (0), (0), (J.a0*J.e1^(2:ℕ)*J.w^(2:ℕ)/(4*J.c0*J.e0*(J.a0 - J.e0*J.w^(2:ℕ))))], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(-J.e1^(2:ℕ)*J.w^(2:ℕ)/(4*J.c0*(J.a0 - J.e0*J.w^(2:ℕ)))), (0), (0), (J.e1^(2:ℕ)*J.w^(3:ℕ)/(4*J.c0*(J.a0 - J.e0*J.w^(2:ℕ))))]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (J.w*(2*J.c0*J.e0*J.e2 - J.c0*J.e1^(2:ℕ) - J.c1*J.e0*J.e1)/(4*J.c0^(2:ℕ)*J.e0)), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (-(2*J.c0*J.e0*J.e2 - J.c0*J.e1^(2:ℕ) - J.c1*J.e0*J.e1)/(4*J.c0*J.e0^(2:ℕ)))], ![(0), (0), ((2*J.c0*J.e0*J.e2 - J.c0*J.e1^(2:ℕ) - J.c1*J.e0*J.e1)/(4*J.c0^(2:ℕ)*J.e0)), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]]]]

noncomputable def NRDT (J : NJet) : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ :=
  ![![![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), ((J.a0*J.a1*J.b1 - 2*J.a0*J.a2*J.b0 + J.a1^(2:ℕ)*J.b0 - J.a1*J.b1*J.e0*J.w^(2:ℕ) + 2*J.a2*J.b0*J.e0*J.w^(2:ℕ))/(4*J.b0*(J.a0 - J.e0*J.w^(2:ℕ)))), (-J.a1*J.e1*J.w^(2:ℕ)/(4*(J.a0 - J.e0*J.w^(2:ℕ)))), (0)], ![(-(J.a0*J.a1*J.b1 - 2*J.a0*J.a2*J.b0 + J.a1^(2:ℕ)*J.b0 - J.a1*J.b1*J.e0*J.w^(2:ℕ) + 2*J.a2*J.b0*J.e0*J.w^(2:ℕ))/(4*J.b0*(J.a0 - J.e0*J.w^(2:ℕ)))), (0), (0), (0)], ![(J.a1*J.e1*J.w^(2:ℕ)/(4*(J.a0 - J.e0*J.w^(2:ℕ)))), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (-J.a1*J.e1*J.w^(2:ℕ)/(4*(J.a0 - J.e0*J.w^(2:ℕ)))), (J.a0*J.e1^(2:ℕ)*J.w^(2:ℕ)/(4*J.e0*(J.a0 - J.e0*J.w^(2:ℕ)))), (0)], ![(J.a1*J.e1*J.w^(2:ℕ)/(4*(J.a0 - J.e0*J.w^(2:ℕ)))), (0), (0), (0)], ![(-J.a0*J.e1^(2:ℕ)*J.w^(2:ℕ)/(4*J.e0*(J.a0 - J.e0*J.w^(2:ℕ)))), (0), (0), (J.w*(2*J.c0*J.e0*J.e2 - J.c0*J.e1^(2:ℕ) - J.c1*J.e0*J.e1)/(4*J.c0*J.e0))], ![(0), (0), (-J.w*(2*J.c0*J.e0*J.e2 - J.c0*J.e1^(2:ℕ) - J.c1*J.e0*J.e1)/(4*J.c0*J.e0)), (0)]], ![![(0), (0), (0), (J.e1^(2:ℕ)*J.w^(2:ℕ)/(4*J.c0))], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(-J.e1^(2:ℕ)*J.w^(2:ℕ)/(4*J.c0)), (0), (0), (0)]]], ![![![(0), (-(J.a0*J.a1*J.b1 - 2*J.a0*J.a2*J.b0 + J.a1^(2:ℕ)*J.b0 - J.a1*J.b1*J.e0*J.w^(2:ℕ) + 2*J.a2*J.b0*J.e0*J.w^(2:ℕ))/(4*J.b0*(J.a0 - J.e0*J.w^(2:ℕ)))), (J.a1*J.e1*J.w^(2:ℕ)/(4*(J.a0 - J.e0*J.w^(2:ℕ)))), (0)], ![((J.a0*J.a1*J.b1 - 2*J.a0*J.a2*J.b0 + J.a1^(2:ℕ)*J.b0 - J.a1*J.b1*J.e0*J.w^(2:ℕ) + 2*J.a2*J.b0*J.e0*J.w^(2:ℕ))/(4*J.b0*(J.a0 - J.e0*J.w^(2:ℕ)))), (0), (0), (0)], ![(-J.a1*J.e1*J.w^(2:ℕ)/(4*(J.a0 - J.e0*J.w^(2:ℕ)))), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]]], ![![![(0), (J.a1*J.e1*J.w^(2:ℕ)/(4*(J.a0 - J.e0*J.w^(2:ℕ)))), (-J.a0*J.e1^(2:ℕ)*J.w^(2:ℕ)/(4*J.e0*(J.a0 - J.e0*J.w^(2:ℕ)))), (0)], ![(-J.a1*J.e1*J.w^(2:ℕ)/(4*(J.a0 - J.e0*J.w^(2:ℕ)))), (0), (0), (0)], ![(J.a0*J.e1^(2:ℕ)*J.w^(2:ℕ)/(4*J.e0*(J.a0 - J.e0*J.w^(2:ℕ)))), (0), (0), (-J.w*(2*J.c0*J.e0*J.e2 - J.c0*J.e1^(2:ℕ) - J.c1*J.e0*J.e1)/(4*J.c0*J.e0))], ![(0), (0), (J.w*(2*J.c0*J.e0*J.e2 - J.c0*J.e1^(2:ℕ) - J.c1*J.e0*J.e1)/(4*J.c0*J.e0)), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (J.w*(2*J.c0*J.e0*J.e2 - J.c0*J.e1^(2:ℕ) - J.c1*J.e0*J.e1)/(4*J.c0*J.e0)), (0)], ![(0), (0), (0), (0)], ![(-J.w*(2*J.c0*J.e0*J.e2 - J.c0*J.e1^(2:ℕ) - J.c1*J.e0*J.e1)/(4*J.c0*J.e0)), (0), (0), (-(2*J.c0*J.e0*J.e2 - J.c0*J.e1^(2:ℕ) - J.c1*J.e0*J.e1)/(4*J.c0*J.e0))], ![(0), (0), ((2*J.c0*J.e0*J.e2 - J.c0*J.e1^(2:ℕ) - J.c1*J.e0*J.e1)/(4*J.c0*J.e0)), (0)]]], ![![![(0), (0), (0), (-J.e1^(2:ℕ)*J.w^(2:ℕ)/(4*J.c0))], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(J.e1^(2:ℕ)*J.w^(2:ℕ)/(4*J.c0)), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (-J.w*(2*J.c0*J.e0*J.e2 - J.c0*J.e1^(2:ℕ) - J.c1*J.e0*J.e1)/(4*J.c0*J.e0)), (0)], ![(0), (0), (0), (0)], ![(J.w*(2*J.c0*J.e0*J.e2 - J.c0*J.e1^(2:ℕ) - J.c1*J.e0*J.e1)/(4*J.c0*J.e0)), (0), (0), ((2*J.c0*J.e0*J.e2 - J.c0*J.e1^(2:ℕ) - J.c1*J.e0*J.e1)/(4*J.c0*J.e0))], ![(0), (0), (-(2*J.c0*J.e0*J.e2 - J.c0*J.e1^(2:ℕ) - J.c1*J.e0*J.e1)/(4*J.c0*J.e0)), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]]]]

noncomputable def NRUT (J : NJet) : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℝ :=
  ![![![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), ((J.a0*J.a1*J.b1 - 2*J.a0*J.a2*J.b0 + J.a1^(2:ℕ)*J.b0 - J.a1*J.b1*J.e0*J.w^(2:ℕ) + 2*J.a2*J.b0*J.e0*J.w^(2:ℕ))/(4*J.b0^(2:ℕ)*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ))), (-J.a1*J.e1*J.w^(2:ℕ)/(4*J.c0*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ))), (0)], ![(-(J.a0*J.a1*J.b1 - 2*J.a0*J.a2*J.b0 + J.a1^(2:ℕ)*J.b0 - J.a1*J.b1*J.e0*J.w^(2:ℕ) + 2*J.a2*J.b0*J.e0*J.w^(2:ℕ))/(4*J.b0^(2:ℕ)*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ))), (0), (0), (J.w*(J.a0*J.a1*J.b1 - 2*J.a0*J.a2*J.b0 + J.a1^(2:ℕ)*J.b0 - J.a1*J.b1*J.e0*J.w^(2:ℕ) + 2*J.a2*J.b0*J.e0*J.w^(2:ℕ))/(4*J.b0^(2:ℕ)*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ)))], ![(J.a1*J.e1*J.w^(2:ℕ)/(4*J.c0*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ))), (0), (0), (-J.a1*J.e1*J.w^(3:ℕ)/(4*J.c0*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ)))], ![(0), (-J.w*(J.a0*J.a1*J.b1 - 2*J.a0*J.a2*J.b0 + J.a1^(2:ℕ)*J.b0 - J.a1*J.b1*J.e0*J.w^(2:ℕ) + 2*J.a2*J.b0*J.e0*J.w^(2:ℕ))/(4*J.b0^(2:ℕ)*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ))), (J.a1*J.e1*J.w^(3:ℕ)/(4*J.c0*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ))), (0)]], ![![(0), (-J.a1*J.e1*J.w^(2:ℕ)/(4*J.b0*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ))), (J.w^(2:ℕ)*(2*J.a0*J.c0*J.e2 - J.a0*J.c1*J.e1 - 2*J.c0*J.e0*J.e2*J.w^(2:ℕ) + J.c0*J.e1^(2:ℕ)*J.w^(2:ℕ) + J.c1*J.e0*J.e1*J.w^(2:ℕ))/(4*J.c0^(2:ℕ)*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ))), (0)], ![(J.a1*J.e1*J.w^(2:ℕ)/(4*J.b0*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ))), (0), (0), (-J.a1*J.e1*J.w^(3:ℕ)/(4*J.b0*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ)))], ![(-J.w^(2:ℕ)*(2*J.a0*J.c0*J.e2 - J.a0*J.c1*J.e1 - 2*J.c0*J.e0*J.e2*J.w^(2:ℕ) + J.c0*J.e1^(2:ℕ)*J.w^(2:ℕ) + J.c1*J.e0*J.e1*J.w^(2:ℕ))/(4*J.c0^(2:ℕ)*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ))), (0), (0), (J.a0*J.w*(2*J.a0*J.c0*J.e0*J.e2 - J.a0*J.c0*J.e1^(2:ℕ) - J.a0*J.c1*J.e0*J.e1 - 2*J.c0*J.e0^(2:ℕ)*J.e2*J.w^(2:ℕ) + 2*J.c0*J.e0*J.e1^(2:ℕ)*J.w^(2:ℕ) + J.c1*J.e0^(2:ℕ)*J.e1*J.w^(2:ℕ))/(4*J.c0^(2:ℕ)*J.e0^(2:ℕ)*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ)))], ![(0), (J.a1*J.e1*J.w^(3:ℕ)/(4*J.b0*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ))), (-J.a0*J.w*(2*J.a0*J.c0*J.e0*J.e2 - J.a0*J.c0*J.e1^(2:ℕ) - J.a0*J.c1*J.e0*J.e1 - 2*J.c0*J.e0^(2:ℕ)*J.e2*J.w^(2:ℕ) + 2*J.c0*J.e0*J.e1^(2:ℕ)*J.w^(2:ℕ) + J.c1*J.e0^(2:ℕ)*J.e1*J.w^(2:ℕ))/(4*J.c0^(2:ℕ)*J.e0^(2:ℕ)*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ))), (0)]], ![![(0), (0), (0), (J.e1^(2:ℕ)*J.w^(2:ℕ)/(4*J.c0*J.e0*(J.a0 - J.e0*J.w^(2:ℕ))))], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(-J.e1^(2:ℕ)*J.w^(2:ℕ)/(4*J.c0*J.e0*(J.a0 - J.e0*J.w^(2:ℕ)))), (0), (0), (0)]]], ![![![(0), (-(J.a0*J.a1*J.b1 - 2*J.a0*J.a2*J.b0 + J.a1^(2:ℕ)*J.b0 - J.a1*J.b1*J.e0*J.w^(2:ℕ) + 2*J.a2*J.b0*J.e0*J.w^(2:ℕ))/(4*J.b0^(2:ℕ)*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ))), (J.a1*J.e1*J.w^(2:ℕ)/(4*J.c0*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ))), (0)], ![((J.a0*J.a1*J.b1 - 2*J.a0*J.a2*J.b0 + J.a1^(2:ℕ)*J.b0 - J.a1*J.b1*J.e0*J.w^(2:ℕ) + 2*J.a2*J.b0*J.e0*J.w^(2:ℕ))/(4*J.b0^(2:ℕ)*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ))), (0), (0), (-J.w*(J.a0*J.a1*J.b1 - 2*J.a0*J.a2*J.b0 + J.a1^(2:ℕ)*J.b0 - J.a1*J.b1*J.e0*J.w^(2:ℕ) + 2*J.a2*J.b0*J.e0*J.w^(2:ℕ))/(4*J.b0^(2:ℕ)*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ)))], ![(-J.a1*J.e1*J.w^(2:ℕ)/(4*J.c0*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ))), (0), (0), (J.a1*J.e1*J.w^(3:ℕ)/(4*J.c0*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ)))], ![(0), (J.w*(J.a0*J.a1*J.b1 - 2*J.a0*J.a2*J.b0 + J.a1^(2:ℕ)*J.b0 - J.a1*J.b1*J.e0*J.w^(2:ℕ) + 2*J.a2*J.b0*J.e0*J.w^(2:ℕ))/(4*J.b0^(2:ℕ)*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ))), (-J.a1*J.e1*J.w^(3:ℕ)/(4*J.c0*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ))), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]]], ![![![(0), (J.a1*J.e1*J.w^(2:ℕ)/(4*J.b0*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ))), (-J.w^(2:ℕ)*(2*J.a0*J.c0*J.e2 - J.a0*J.c1*J.e1 - 2*J.c0*J.e0*J.e2*J.w^(2:ℕ) + J.c0*J.e1^(2:ℕ)*J.w^(2:ℕ) + J.c1*J.e0*J.e1*J.w^(2:ℕ))/(4*J.c0^(2:ℕ)*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ))), (0)], ![(-J.a1*J.e1*J.w^(2:ℕ)/(4*J.b0*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ))), (0), (0), (J.a1*J.e1*J.w^(3:ℕ)/(4*J.b0*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ)))], ![(J.w^(2:ℕ)*(2*J.a0*J.c0*J.e2 - J.a0*J.c1*J.e1 - 2*J.c0*J.e0*J.e2*J.w^(2:ℕ) + J.c0*J.e1^(2:ℕ)*J.w^(2:ℕ) + J.c1*J.e0*J.e1*J.w^(2:ℕ))/(4*J.c0^(2:ℕ)*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ))), (0), (0), (-J.a0*J.w*(2*J.a0*J.c0*J.e0*J.e2 - J.a0*J.c0*J.e1^(2:ℕ) - J.a0*J.c1*J.e0*J.e1 - 2*J.c0*J.e0^(2:ℕ)*J.e2*J.w^(2:ℕ) + 2*J.c0*J.e0*J.e1^(2:ℕ)*J.w^(2:ℕ) + J.c1*J.e0^(2:ℕ)*J.e1*J.w^(2:ℕ))/(4*J.c0^(2:ℕ)*J.e0^(2:ℕ)*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ)))], ![(0), (-J.a1*J.e1*J.w^(3:ℕ)/(4*J.b0*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ))), (J.a0*J.w*(2*J.a0*J.c0*J.e0*J.e2 - J.a0*J.c0*J.e1^(2:ℕ) - J.a0*J.c1*J.e0*J.e1 - 2*J.c0*J.e0^(2:ℕ)*J.e2*J.w^(2:ℕ) + 2*J.c0*J.e0*J.e1^(2:ℕ)*J.w^(2:ℕ) + J.c1*J.e0^(2:ℕ)*J.e1*J.w^(2:ℕ))/(4*J.c0^(2:ℕ)*J.e0^(2:ℕ)*(J.a0 - J.e0*J.w^(2:ℕ))^(2:ℕ))), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (-(2*J.c0*J.e0*J.e2 - J.c0*J.e1^(2:ℕ) - J.c1*J.e0*J.e1)/(4*J.c0^(2:ℕ)*J.e0^(2:ℕ)))], ![(0), (0), ((2*J.c0*J.e0*J.e2 - J.c0*J.e1^(2:ℕ) - J.c1*J.e0*J.e1)/(4*J.c0^(2:ℕ)*J.e0^(2:ℕ))), (0)]]], ![![![(0), (0), (0), (-J.e1^(2:ℕ)*J.w^(2:ℕ)/(4*J.c0*J.e0*(J.a0 - J.e0*J.w^(2:ℕ))))], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(J.e1^(2:ℕ)*J.w^(2:ℕ)/(4*J.c0*J.e0*(J.a0 - J.e0*J.w^(2:ℕ)))), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), ((2*J.c0*J.e0*J.e2 - J.c0*J.e1^(2:ℕ) - J.c1*J.e0*J.e1)/(4*J.c0^(2:ℕ)*J.e0^(2:ℕ)))], ![(0), (0), (-(2*J.c0*J.e0*J.e2 - J.c0*J.e1^(2:ℕ) - J.c1*J.e0*J.e1)/(4*J.c0^(2:ℕ)*J.e0^(2:ℕ))), (0)]], ![![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)], ![(0), (0), (0), (0)]]]]

variable (J : NJet) (hA : J.a0 - J.w ^ 2 * J.e0 ≠ 0) (hB : J.b0 ≠ 0) (hC : J.c0 ≠ 0) (hE : J.e0 ≠ 0)
include hA hB hC hE

lemma NGiT_ok (m k : Fin 4) : ∑ l, NGT J m l * NGiT J l k = if m = k then 1 else 0 := by
  have hA' : J.a0 - J.e0 * J.w ^ 2 ≠ 0 := by rwa [mul_comm]
  fin_cases m <;> fin_cases k <;> simp [Fin.sum_univ_four, NGT, NGiT] <;> (try field_simp) <;> ring1

lemma NGamT_ok (i j k : Fin 4) : GamF (ND1T J) (NGiT J) i j k = NGamT J i j k := by
  have hA' : J.a0 - J.e0 * J.w ^ 2 ≠ 0 := by rwa [mul_comm]
  simp only [GamF]
  fin_cases i <;> fin_cases j <;> fin_cases k <;> simp [Fin.sum_univ_four, ND1T, NGiT, NGamT] <;>
    (try field_simp) <;> ring1

lemma NDGT_ok (u i j k : Fin 4) : DGamF (ND1T J) (ND2T J) (NGiT J) u i j k = NDGT J u i j k := by
  have hA' : J.a0 - J.e0 * J.w ^ 2 ≠ 0 := by rwa [mul_comm]
  simp only [DGamF, NGamT_ok J hA hB hC hE]
  fin_cases u <;> fin_cases i <;> fin_cases j <;> fin_cases k <;>
    simp [Fin.sum_univ_four, ND2T, ND1T, NGiT, NGamT, NDGT] <;> (try field_simp) <;> ring1

lemma NRT_ok (i j k l : Fin 4) : RiemF (ND1T J) (ND2T J) (NGiT J) i j k l = NRT J i j k l := by
  have hA' : J.a0 - J.e0 * J.w ^ 2 ≠ 0 := by rwa [mul_comm]
  simp only [RiemF, NDGT_ok J hA hB hC hE, NGamT_ok J hA hB hC hE]
  fin_cases i <;> fin_cases j <;> fin_cases k <;> fin_cases l <;>
    simp [Fin.sum_univ_four, NDGT, NGamT, NRT] <;> (try field_simp) <;> ring1

lemma NRDT_ok (m n a b : Fin 4) : lowR (Matrix.of (NGT J)) (NRT J) m n a b = NRDT J m n a b := by
  have hA' : J.a0 - J.e0 * J.w ^ 2 ≠ 0 := by rwa [mul_comm]
  fin_cases m <;> fin_cases n <;> fin_cases a <;> fin_cases b <;>
    simp [lowR, Fin.sum_univ_four, NGT, NRT, NRDT] <;> (try field_simp) <;> ring1

lemma NRUT_ok (m n a b : Fin 4) :
    raiseR (Matrix.of (NGT J)) (Matrix.of (NGiT J)) (NRT J) m n a b = NRUT J m n a b := by
  have hA' : J.a0 - J.e0 * J.w ^ 2 ≠ 0 := by rwa [mul_comm]
  simp only [raiseR, NRDT_ok J hA hB hC hE, Matrix.of_apply]
  fin_cases m <;> fin_cases n <;> fin_cases a <;> fin_cases b <;>
    simp [Fin.sum_univ_four, NGiT, NRDT, NRUT] <;> (try field_simp) <;> ring1

/-- **The density from the tables is zero.** -/
lemma Npont_ok : pontArr (Matrix.of (NGT J)) (Matrix.of (NGiT J)) (NRT J) = 0 := by
  have hA' : J.a0 - J.e0 * J.w ^ 2 ≠ 0 := by rwa [mul_comm]
  rw [pontArr, sum_eps, div_eq_zero_iff]
  left
  simp only [NRDT_ok J hA hB hC hE, NRUT_ok J hA hB hC hE]
  simp [Fin.sum_univ_four, NRDT, NRUT]
  try field_simp
  try ring1

end Nariai

section NariaiMetric

set_option synthInstance.maxHeartbeats 400000

def nA : Fin 4 → Fin 4 → ℝ := ![![1, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]]
def nB : Fin 4 → Fin 4 → ℝ := ![![0, 0, 0, 0], ![0, 1, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]]
def nC : Fin 4 → Fin 4 → ℝ := ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 1, 0], ![0, 0, 0, 0]]
def nE (w : ℝ) : Fin 4 → Fin 4 → ℝ := ![![0, 0, 0, w], ![0, 0, 0, 0], ![0, 0, 0, 0], ![w, 0, 0, 1]]

/-- **The generalised rotated Nariai form** in coordinates `(τ, χ, θ, φ)`:
`a(χ) dτ² + b(χ) dχ² + c(θ) dθ² + 2w e(θ) dτ dφ + e(θ) dφ²`. -/
noncomputable def NG (a b c e : ℝ → ℝ) (w : ℝ) (i j : Fin 4) (y : Fin 4 → ℝ) : ℝ :=
  nA i j * a (y 1) + nB i j * b (y 1) + nC i j * c (y 2) + nE w i j * e (y 2)

lemma NG_symm (a b c e : ℝ → ℝ) (w : ℝ) (i j : Fin 4) (y : Fin 4 → ℝ) : NG a b c e w i j y = NG a b c e w j i y := by
  fin_cases i <;> fin_cases j <;> simp [NG, nA, nB, nC, nE]

variable {a b c e : ℝ → ℝ} {w : ℝ} (ha : ContDiff ℝ ∞ a) (hb : ContDiff ℝ ∞ b) (hc : ContDiff ℝ ∞ c)
  (he : ContDiff ℝ ∞ e)

include ha hb hc he in
lemma NG_smooth (i j : Fin 4) : ContDiff ℝ ∞ (NG a b c e w i j) :=
  (((contDiff_const.mul (ha.comp (contDiff_apply ℝ ℝ (1 : Fin 4)))).add
    (contDiff_const.mul (hb.comp (contDiff_apply ℝ ℝ (1 : Fin 4))))).add
    (contDiff_const.mul (hc.comp (contDiff_apply ℝ ℝ (2 : Fin 4))))).add
    (contDiff_const.mul (he.comp (contDiff_apply ℝ ℝ (2 : Fin 4))))

include ha hb hc he in
lemma NG_fd1 (i j : Fin 4) (y v : Fin 4 → ℝ) :
    fderiv ℝ (NG a b c e w i j) y v = nA i j * (deriv a (y 1) * v 1) + nB i j * (deriv b (y 1) * v 1)
      + nC i j * (deriv c (y 2) * v 2) + nE w i j * (deriv e (y 2) * v 2) := by
  have d := fun {k : ℝ → ℝ} (hk : ContDiff ℝ ∞ k) s => (hk.differentiable (by simp) : Differentiable ℝ k) s
  have h := (((((fd_coord_i (x := y) 1 (d ha _)).const_mul (nA i j)).add ((fd_coord_i (x := y) 1 (d hb _)).const_mul (nB i j))).add
    ((fd_coord_i (x := y) 2 (d hc _)).const_mul (nC i j))).add ((fd_coord_i (x := y) 2 (d he _)).const_mul (nE w i j)))
  have h' : HasFDerivAt (NG a b c e w i j) _ y := h
  rw [h'.fderiv]
  simp

include ha hb hc he in
lemma NG_fd2 (i j : Fin 4) (p u v : Fin 4 → ℝ) :
    fderiv ℝ (fderiv ℝ (NG a b c e w i j)) p u v = nA i j * (deriv (deriv a) (p 1) * u 1 * v 1)
      + nB i j * (deriv (deriv b) (p 1) * u 1 * v 1) + nC i j * (deriv (deriv c) (p 2) * u 2 * v 2)
      + nE w i j * (deriv (deriv e) (p 2) * u 2 * v 2) := by
  have d2 := fun {k : ℝ → ℝ} (hk : ContDiff ℝ ∞ k) s =>
    ((contDiff_infty_iff_deriv.1 hk).2.differentiable (by simp) : Differentiable ℝ (deriv k)) s
  rw [d2_of (F := NG a b c e w i j) (NG_smooth ha hb hc he i j) (fun y => NG_fd1 ha hb hc he i j y v)
    ((((((fd_coord_i (x := p) 1 (d2 ha _)).mul_const (v 1)).const_mul (nA i j)).add
      (((fd_coord_i (x := p) 1 (d2 hb _)).mul_const (v 1)).const_mul (nB i j))).add
      (((fd_coord_i (x := p) 2 (d2 hc _)).mul_const (v 2)).const_mul (nC i j))).add
      (((fd_coord_i (x := p) 2 (d2 he _)).mul_const (v 2)).const_mul (nE w i j)))]
  simp; ring1

lemma NG_det (y : Fin 4 → ℝ) :
    (gm (NG a b c e w) y).det = b (y 1) * c (y 2) * e (y 2) * (a (y 1) - w ^ 2 * e (y 2)) := by
  simp [Matrix.det_succ_row_zero, Fin.sum_univ_succ, gm, NG, nA, nB, nC, nE,
    show (Fin.succAbove 1 2 : Fin 4) = 3 by decide, show (Fin.succAbove 3 2 : Fin 4) = 2 by decide]
  ring

variable (hb0 : ∀ s, b s ≠ 0) (hc0 : ∀ s, c s ≠ 0) (he0 : ∀ s, e s ≠ 0) (hae : ∀ s s', a s - w ^ 2 * e s' ≠ 0)

include hb0 hc0 he0 hae in
lemma NG_nondeg : ∀ p (u : Fin 4 → ℝ), (∀ v, formG (NG a b c e w) p u v = 0) → u = 0 :=
  nondeg_of_det fun y => by
    rw [NG_det]
    exact mul_ne_zero (mul_ne_zero (mul_ne_zero (hb0 _) (hc0 _)) (he0 _)) (hae _ _)

/-- The jet at `p`. -/
noncomputable def jetN (a b c e : ℝ → ℝ) (w : ℝ) (p : Fin 4 → ℝ) : NJet where
  a0 := a (p 1)
  a1 := deriv a (p 1)
  a2 := deriv (deriv a) (p 1)
  b0 := b (p 1)
  b1 := deriv b (p 1)
  b2 := deriv (deriv b) (p 1)
  c0 := c (p 2)
  c1 := deriv c (p 2)
  c2 := deriv (deriv c) (p 2)
  e0 := e (p 2)
  e1 := deriv e (p 2)
  e2 := deriv (deriv e) (p 2)
  w := w

include ha hb hc he hb0 hc0 he0 hae in
/-- **Part 1, the general statement.** For ANY smooth `a(χ), b(χ), c(θ), e(θ)` and constant `w` making the form
nondegenerate, THE connection's `*RR` of `a dτ² + b dχ² + c dθ² + 2w e dτ dφ + e dφ²` vanishes at every point. -/
theorem nariai_general_pontryagin_zero (p : Fin 4 → ℝ) :
    pontryaginLC (NG a b c e w) (NG_symm a b c e w) (NG_nondeg hb0 hc0 he0 hae) (NG_smooth ha hb hc he) p = 0 := by
  set J := jetN a b c e w p
  have hg : ∀ i j, NG a b c e w i j p = NGT J i j := fun i j => by
    fin_cases i <;> fin_cases j <;> simp [NG, nA, nB, nC, nE, NGT, J, jetN] <;> ring1
  have hJ : J.a0 - J.w ^ 2 * J.e0 ≠ 0 := hae _ _
  have hinv : ∀ m k, ∑ l, NG a b c e w m l p * NGiT J l k = if m = k then 1 else 0 := fun m k => by
    simp only [hg]; exact NGiT_ok J hJ (hb0 _) (hc0 _) (he0 _) m k
  have h1 : ∀ i j k, d1At (NG a b c e w) p i j k = ND1T J i j k := fun i j k => by
    rw [d1At, dG1, NG_fd1 ha hb hc he]
    fin_cases i <;> fin_cases j <;> fin_cases k <;> simp [nA, nB, nC, nE, ND1T, J, jetN] <;> ring1
  have h2 : ∀ i j k l, d2At (NG a b c e w) p i j k l = ND2T J i j k l := fun i j k l => by
    rw [d2At, dG2, NG_fd2 ha hb hc he]
    fin_cases i <;> fin_cases j <;> fin_cases k <;> fin_cases l <;> simp [nA, nB, nC, nE, ND2T, J, jetN] <;> ring1
  rw [(tabs_bridge (NG_symm a b c e w) (NG_nondeg hb0 hc0 he0 hae) (NG_smooth ha hb hc he) hg hinv h1 h2).1]
  have hR : RiemF (ND1T J) (ND2T J) (NGiT J) = NRT J := by
    funext i j k l; exact NRT_ok J hJ (hb0 _) (hc0 _) (he0 _) i j k l
  rw [hR]
  exact Npont_ok J hJ (hb0 _) (hc0 _) (he0 _)

end NariaiMetric

section NariaiReceipt

variable {L ω₀ : ℝ} (hL : 0 < L) {f h : ℝ → ℝ} (hf : ContDiff ℝ ∞ f) (hh : ContDiff ℝ ∞ h) (hf0 : ∀ s, 0 < f s)
  (hh0 : ∀ s, 0 < h s)

include hL hf0 hh0 in
lemma nr_ae (s s' : ℝ) : -L * f s - ω₀ ^ 2 * (L * h s') ≠ 0 :=
  (by nlinarith [mul_pos hL (hf0 s), mul_nonneg (sq_nonneg ω₀) (mul_pos hL (hh0 s')).le] :
    -L * f s - ω₀ ^ 2 * (L * h s') < 0).ne

include hL hf hh hf0 hh0 in
/-- **Part 1, the receipt's rotated Nariai form**: `−L f(χ) dτ² + L/f(χ) dχ² + L dθ² + 2ω₀ L h(θ) dτ dφ + L h(θ) dφ²`
(the receipt's `NARIAI_ROT` with `f = 1 − χ²`, `h = sin²θ`, `L = α²/3`), for ANY smooth positive profiles `f, h` — the
engine needs a metric nondegenerate on all of `ℝ⁴`, so the receipt's profiles enter as profiles equal to `1 − χ²` and
`sin²θ` near a point with `|χ| < 1`, `0 < θ < π`; the density at a point sees only the 2-jet there. `*RR = 0`. -/
theorem nariai_rotated_pontryagin_zero (p : Fin 4 → ℝ) :
    pontryaginLC (NG (fun s => -L * f s) (fun s => L / f s) (fun _ => L) (fun s => L * h s) ω₀) (NG_symm _ _ _ _ _)
      (NG_nondeg (fun s => (div_pos hL (hf0 s)).ne') (fun _ => hL.ne') (fun s => (mul_pos hL (hh0 s)).ne')
        (nr_ae hL hf0 hh0))
      (NG_smooth (contDiff_const.mul hf) (contDiff_const.div hf fun s => (hf0 s).ne') contDiff_const
        (contDiff_const.mul hh)) p = 0 :=
  nariai_general_pontryagin_zero (contDiff_const.mul hf) (contDiff_const.div hf fun s => (hf0 s).ne') contDiff_const
    (contDiff_const.mul hh) (fun s => (div_pos hL (hf0 s)).ne') (fun _ => hL.ne') (fun s => (mul_pos hL (hh0 s)).ne')
    (nr_ae hL hf0 hh0) p

include hL hf hh hf0 hh0 in
/-- **Part 1, Nariai `dS₂ × S²` in its own form**, `diag(−L f(χ), L/f(χ), L, L h(θ))`: the case `ω₀ = 0`. `*RR = 0`. -/
theorem nariai_pontryagin_zero (p : Fin 4 → ℝ) :
    pontryaginLC (NG (fun s => -L * f s) (fun s => L / f s) (fun _ => L) (fun s => L * h s) 0) (NG_symm _ _ _ _ _)
      (NG_nondeg (fun s => (div_pos hL (hf0 s)).ne') (fun _ => hL.ne') (fun s => (mul_pos hL (hh0 s)).ne')
        (nr_ae (ω₀ := 0) hL hf0 hh0))
      (NG_smooth (contDiff_const.mul hf) (contDiff_const.div hf fun s => (hf0 s).ne') contDiff_const
        (contDiff_const.mul hh)) p = 0 :=
  nariai_rotated_pontryagin_zero hL hf hh hf0 hh0 p

/-- The diagonal form's entries are the receipt's `NARIAI`. -/
theorem nariai_apply (y : Fin 4 → ℝ) (i j : Fin 4) :
    NG (fun s => -L * f s) (fun s => L / f s) (fun _ => L) (fun s => L * h s) ω₀ i j y
      = (![![-L * f (y 1), 0, 0, ω₀ * (L * h (y 2))], ![0, L / f (y 1), 0, 0], ![0, 0, L, 0],
          ![ω₀ * (L * h (y 2)), 0, 0, L * h (y 2)]] : Fin 4 → Fin 4 → ℝ) i j := by
  fin_cases i <;> fin_cases j <;> simp [NG, nA, nB, nC, nE]

end NariaiReceipt

/-! ### The metric and its first two partials -/

section GowdyMetric

set_option synthInstance.maxHeartbeats 400000

/-- Numeric coefficient matrices: `G = cO + cA·a(u) + cB·b(u) + cC·(c(u) + q(t)·d(u))`, `u = t − z`. -/
def cO : Fin 4 → Fin 4 → ℝ := ![![-1, 0, 0, 0], ![0, 1, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0]]
def cA : Fin 4 → Fin 4 → ℝ := ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 1, 0], ![0, 0, 0, 0]]
def cB : Fin 4 → Fin 4 → ℝ := ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 1], ![0, 0, 1, 0]]
def cC : Fin 4 → Fin 4 → ℝ := ![![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 0], ![0, 0, 0, 1]]

/-- The shape of the metric, with five one-variable profiles `a, b, c, d` (of `u = y₀ − y₁`) and `q` (of `t = y₀`). -/
noncomputable def GWgen (a b c d q : ℝ → ℝ) (i j : Fin 4) (y : Fin 4 → ℝ) : ℝ :=
  cO i j + cA i j * a (y 0 - y 1) + cB i j * b (y 0 - y 1) + cC i j * (c (y 0 - y 1) + q (y 0) * d (y 0 - y 1))

/-- The profiles of the Gowdy entries. -/
noncomputable def aF (ψ : ℝ → ℝ) (s : ℝ) : ℝ := Real.exp (2 * ψ s)
noncomputable def bF (ψ om : ℝ → ℝ) (s : ℝ) : ℝ := aF ψ s * om s
noncomputable def cF (ψ om : ℝ → ℝ) (s : ℝ) : ℝ := bF ψ om s * om s
noncomputable def dF (ψ : ℝ → ℝ) (s : ℝ) : ℝ := Real.exp (-2 * ψ s)
def qF (R : ℝ → ℝ) (s : ℝ) : ℝ := R s * R s

/-- **The plane-wave Gowdy metric**, the receipt's `gowdy(0, ψ(t − z), ω(t − z), R(t))` in coordinates
`(t, z, x, y) = (y₀, y₁, y₂, y₃)`: `−dt² + dz² + e^{2ψ}(dx + ω dy)² + R² e^{−2ψ} dy²` (`GW_apply`).
In the code the profile `ω` is named `om`, since `ω` is reserved notation in Mathlib. -/
noncomputable def GW (ψ om R : ℝ → ℝ) : Fin 4 → Fin 4 → (Fin 4 → ℝ) → ℝ :=
  GWgen (aF ψ) (bF ψ om) (cF ψ om) (dF ψ) (qF R)

lemma exp_neg_two (x : ℝ) : Real.exp (-2 * x) = (Real.exp (2 * x))⁻¹ := by
  rw [← Real.exp_neg]; ring_nf

/-- The entries are the receipt's `gowdy(0, ψ, ω, R)` matrix at `u = t − z`. -/
theorem GW_apply (ψ om R : ℝ → ℝ) (y : Fin 4 → ℝ) (i j : Fin 4) :
    GW ψ om R i j y = (![![-1, 0, 0, 0], ![0, 1, 0, 0],
      ![0, 0, Real.exp (2 * ψ (y 0 - y 1)), Real.exp (2 * ψ (y 0 - y 1)) * om (y 0 - y 1)],
      ![0, 0, Real.exp (2 * ψ (y 0 - y 1)) * om (y 0 - y 1),
        Real.exp (2 * ψ (y 0 - y 1)) * om (y 0 - y 1) ^ 2 + R (y 0) ^ 2 * Real.exp (-2 * ψ (y 0 - y 1))]] :
        Fin 4 → Fin 4 → ℝ) i j := by
  fin_cases i <;> fin_cases j <;> simp [GW, GWgen, cO, cA, cB, cC, aF, bF, cF, dF, qF] <;> ring1

lemma GW_symm (ψ om R : ℝ → ℝ) (i j : Fin 4) (y : Fin 4 → ℝ) : GW ψ om R i j y = GW ψ om R j i y := by
  fin_cases i <;> fin_cases j <;> simp [GW, GWgen, cO, cA, cB, cC]

lemma fd_u {k : ℝ → ℝ} {x : Fin 4 → ℝ} (hk : DifferentiableAt ℝ k (x 0 - x 1)) :
    HasFDerivAt (fun y : Fin 4 → ℝ => k (y 0 - y 1))
      (deriv k (x 0 - x 1) • (ContinuousLinearMap.proj (R := ℝ) (φ := fun _ : Fin 4 => ℝ) 0
        - ContinuousLinearMap.proj (R := ℝ) (φ := fun _ : Fin 4 => ℝ) 1)) x :=
  hk.hasDerivAt.comp_hasFDerivAt x ((hasFDerivAt_apply (𝕜 := ℝ) 0 x).sub (hasFDerivAt_apply (𝕜 := ℝ) 1 x))

variable {a b c d q : ℝ → ℝ} (ha : ContDiff ℝ ∞ a) (hb : ContDiff ℝ ∞ b) (hc : ContDiff ℝ ∞ c)
  (hd : ContDiff ℝ ∞ d) (hq : ContDiff ℝ ∞ q)
include ha hb hc hd hq

lemma cu {k : ℝ → ℝ} (hk : ContDiff ℝ ∞ k) : ContDiff ℝ ∞ (fun y : Fin 4 → ℝ => k (y 0 - y 1)) :=
  hk.comp ((contDiff_apply ℝ ℝ (0 : Fin 4)).sub (contDiff_apply ℝ ℝ (1 : Fin 4)))

omit ha hb hc hd hq in
lemma cu' {k : ℝ → ℝ} (hk : ContDiff ℝ ∞ k) : ContDiff ℝ ∞ (fun y : Fin 4 → ℝ => k (y 0 - y 1)) :=
  hk.comp ((contDiff_apply ℝ ℝ (0 : Fin 4)).sub (contDiff_apply ℝ ℝ (1 : Fin 4)))

lemma GWgen_smooth (i j : Fin 4) : ContDiff ℝ ∞ (GWgen a b c d q i j) :=
  ((contDiff_const.add (contDiff_const.mul (cu' ha))).add (contDiff_const.mul (cu' hb))).add
    (contDiff_const.mul ((cu' hc).add ((hq.comp (contDiff_apply ℝ ℝ (0 : Fin 4))).mul (cu' hd))))

lemma GWgen_fd1 (i j : Fin 4) (y v : Fin 4 → ℝ) :
    fderiv ℝ (GWgen a b c d q i j) y v = cA i j * (deriv a (y 0 - y 1) * (v 0 - v 1))
      + cB i j * (deriv b (y 0 - y 1) * (v 0 - v 1))
      + cC i j * (deriv c (y 0 - y 1) * (v 0 - v 1)
        + (deriv q (y 0) * v 0 * d (y 0 - y 1) + q (y 0) * (deriv d (y 0 - y 1) * (v 0 - v 1)))) := by
  have da := fun s => (ha.differentiable (by simp)) s
  have db := fun s => (hb.differentiable (by simp)) s
  have dc := fun s => (hc.differentiable (by simp)) s
  have dd := fun s => (hd.differentiable (by simp)) s
  have dq := fun s => (hq.differentiable (by simp)) s
  have h := (((((fd_u (x := y) (da _)).const_mul (cA i j)).const_add (cO i j)).add ((fd_u (x := y) (db _)).const_mul (cB i j))).add
    (((fd_u (x := y) (dc _)).add ((fd_coord_i (x := y) 0 (dq _)).mul (fd_u (x := y) (dd _)))).const_mul (cC i j)))
  have h' : HasFDerivAt (GWgen a b c d q i j) _ y := h
  rw [h'.fderiv]
  simp; ring1

lemma GWgen_fd2 (i j : Fin 4) (p w v : Fin 4 → ℝ) :
    fderiv ℝ (fderiv ℝ (GWgen a b c d q i j)) p w v
      = cA i j * (deriv (deriv a) (p 0 - p 1) * (w 0 - w 1) * (v 0 - v 1))
      + cB i j * (deriv (deriv b) (p 0 - p 1) * (w 0 - w 1) * (v 0 - v 1))
      + cC i j * (deriv (deriv c) (p 0 - p 1) * (w 0 - w 1) * (v 0 - v 1)
        + deriv (deriv q) (p 0) * w 0 * v 0 * d (p 0 - p 1)
        + deriv q (p 0) * v 0 * (deriv d (p 0 - p 1) * (w 0 - w 1))
        + deriv q (p 0) * w 0 * (deriv d (p 0 - p 1) * (v 0 - v 1))
        + q (p 0) * (deriv (deriv d) (p 0 - p 1) * (w 0 - w 1) * (v 0 - v 1))) := by
  have d1 := fun {k : ℝ → ℝ} (hk : ContDiff ℝ ∞ k) s => (hk.differentiable (by simp) : Differentiable ℝ k) s
  have d2 := fun {k : ℝ → ℝ} (hk : ContDiff ℝ ∞ k) s =>
    ((contDiff_infty_iff_deriv.1 hk).2.differentiable (by simp) : Differentiable ℝ (deriv k)) s
  rw [d2_of (F := GWgen a b c d q i j) (GWgen_smooth ha hb hc hd hq i j)
    (fun y => GWgen_fd1 ha hb hc hd hq i j y v)
    (((((fd_u (x := p) (d2 ha _)).mul_const (v 0 - v 1)).const_mul (cA i j)).add
      (((fd_u (x := p) (d2 hb _)).mul_const (v 0 - v 1)).const_mul (cB i j))).add
      ((((fd_u (x := p) (d2 hc _)).mul_const (v 0 - v 1)).add
        ((((fd_coord_i (x := p) 0 (d2 hq _)).mul_const (v 0)).mul (fd_u (x := p) (d1 hd _))).add
          ((fd_coord_i (x := p) 0 (d1 hq _)).mul ((fd_u (x := p) (d2 hd _)).mul_const (v 0 - v 1))))).const_mul (cC i j)))]
  simp; ring1

end GowdyMetric

/-! ### One-variable jets -/

section Jets

lemma jet_mul {f g : ℝ → ℝ} (hf : ContDiff ℝ ∞ f) (hg : ContDiff ℝ ∞ g) (s : ℝ) :
    deriv (fun x => f x * g x) s = deriv f s * g s + f s * deriv g s ∧
      deriv (deriv (fun x => f x * g x)) s
        = deriv (deriv f) s * g s + 2 * (deriv f s * deriv g s) + f s * deriv (deriv g) s := by
  have df := fun x => (hf.differentiable (by simp) : Differentiable ℝ f) x
  have dg := fun x => (hg.differentiable (by simp) : Differentiable ℝ g) x
  have ddf := fun x => ((contDiff_infty_iff_deriv.1 hf).2.differentiable (by simp) : Differentiable ℝ (deriv f)) x
  have ddg := fun x => ((contDiff_infty_iff_deriv.1 hg).2.differentiable (by simp) : Differentiable ℝ (deriv g)) x
  have h1 : deriv (fun x => f x * g x) = fun x => deriv f x * g x + f x * deriv g x :=
    funext fun x => deriv_mul (df x) (dg x)
  refine ⟨by rw [h1], ?_⟩
  rw [h1]
  refine (((ddf s).hasDerivAt.mul (dg s).hasDerivAt).add ((df s).hasDerivAt.mul (ddg s).hasDerivAt)).deriv.trans ?_
  ring1

lemma jet_exp (k : ℝ) {f : ℝ → ℝ} (hf : ContDiff ℝ ∞ f) (s : ℝ) :
    deriv (fun x => Real.exp (k * f x)) s = k * deriv f s * Real.exp (k * f s) ∧
      deriv (deriv (fun x => Real.exp (k * f x))) s
        = (k * deriv (deriv f) s + k ^ 2 * deriv f s ^ 2) * Real.exp (k * f s) := by
  have df := fun x => (hf.differentiable (by simp) : Differentiable ℝ f) x
  have ddf := fun x => ((contDiff_infty_iff_deriv.1 hf).2.differentiable (by simp) : Differentiable ℝ (deriv f)) x
  have h1 : deriv (fun x => Real.exp (k * f x)) = fun x => k * deriv f x * Real.exp (k * f x) :=
    funext fun x => (((df x).hasDerivAt.const_mul k).exp.deriv).trans (by ring1)
  refine ⟨by rw [h1], ?_⟩
  rw [h1]
  refine (((ddf s).hasDerivAt.const_mul k).mul (((df s).hasDerivAt.const_mul k).exp)).deriv.trans ?_
  ring1

variable {ψ om R : ℝ → ℝ} (hψ : ContDiff ℝ ∞ ψ) (hom : ContDiff ℝ ∞ om) (hR : ContDiff ℝ ∞ R)

include hψ in
lemma aF_smooth : ContDiff ℝ ∞ (aF ψ) := Real.contDiff_exp.comp (contDiff_const.mul hψ)
include hψ in
lemma dF_smooth : ContDiff ℝ ∞ (dF ψ) := Real.contDiff_exp.comp (contDiff_const.mul hψ)
include hψ hom in
lemma bF_smooth : ContDiff ℝ ∞ (bF ψ om) := (aF_smooth hψ).mul hom
include hψ hom in
lemma cF_smooth : ContDiff ℝ ∞ (cF ψ om) := (bF_smooth hψ hom).mul hom
include hR in
lemma qF_smooth : ContDiff ℝ ∞ (qF R) := hR.mul hR

include hψ hom hR in
lemma GW_smooth (i j : Fin 4) : ContDiff ℝ ∞ (GW ψ om R i j) :=
  GWgen_smooth (aF_smooth hψ) (bF_smooth hψ hom) (cF_smooth hψ hom) (dF_smooth hψ) (qF_smooth hR) i j

/-- Nondegenerate at every point when `R` never vanishes: the `(x, y)` block has determinant `R²`. -/
lemma GW_nondeg (hR0 : ∀ s, R s ≠ 0) (y u : Fin 4 → ℝ) (h : ∀ v, formG (GW ψ om R) y u v = 0) : u = 0 := by
  have e : ∀ c : Fin 4, formG (GW ψ om R) y u (Pi.single c 1) = ∑ i, GW ψ om R i c y * u i := fun c => by
    rw [formG_apply]; simp [Pi.single_apply, mul_comm]
  have h0 := (e 0).symm.trans (h _); have h1 := (e 1).symm.trans (h _)
  have h2 := (e 2).symm.trans (h _); have h3 := (e 3).symm.trans (h _)
  simp only [Fin.sum_univ_four, GW, GWgen, cO, cA, cB, cC, aF, bF, cF, dF, qF] at h0 h1 h2 h3
  norm_num at h0 h1 h2 h3
  have hu0 : u 0 = 0 := by linarith
  have hu1 : u 1 = 0 := by linarith
  have hE := Real.exp_pos (2 * ψ (y 0 - y 1))
  have hD := Real.exp_pos (-(2 * ψ (y 0 - y 1)))
  have k3 : (R (y 0) * R (y 0) * Real.exp (-(2 * ψ (y 0 - y 1)))) * u 3 = 0 := by
    linear_combination h3 - om (y 0 - y 1) * h2
  have hu3 : u 3 = 0 := by
    rcases mul_eq_zero.1 k3 with h | h
    · exact absurd h (mul_ne_zero (mul_ne_zero (hR0 _) (hR0 _)) hD.ne')
    · exact h
  have hu2 : u 2 = 0 := by
    have : Real.exp (2 * ψ (y 0 - y 1)) * u 2 = 0 := by linear_combination h2 - Real.exp (2 * ψ (y 0 - y 1)) * om (y 0 - y 1) * hu3
    rcases mul_eq_zero.1 this with h | h
    · exact absurd h hE.ne'
    · exact h
  ext k; fin_cases k <;> simp [hu0, hu1, hu2, hu3]

/-- The jet of the profiles at the point `p`. -/
noncomputable def jetAt (ψ om R : ℝ → ℝ) (p : Fin 4 → ℝ) : Jet where
  E := Real.exp (2 * ψ (p 0 - p 1))
  p1 := deriv ψ (p 0 - p 1)
  p2 := deriv (deriv ψ) (p 0 - p 1)
  w0 := om (p 0 - p 1)
  w1 := deriv om (p 0 - p 1)
  w2 := deriv (deriv om) (p 0 - p 1)
  r0 := R (p 0)
  r1 := deriv R (p 0)
  r2 := deriv (deriv R) (p 0)

end Jets

/-! ### The tables at the point -/

section GowdyTables

variable {ψ om R : ℝ → ℝ} (hψ : ContDiff ℝ ∞ ψ) (hom : ContDiff ℝ ∞ om) (hR : ContDiff ℝ ∞ R)
  (hR0 : ∀ s, R s ≠ 0) (p : Fin 4 → ℝ)

lemma G_tab (i j : Fin 4) : GW ψ om R i j p = GT (jetAt ψ om R p) i j := by
  fin_cases i <;> fin_cases j <;> simp [GW, GWgen, cO, cA, cB, cC, aF, bF, cF, dF, qF, GT, jetAt, exp_neg_two, Real.exp_neg] <;>
    (try field_simp) <;> ring1

include hψ hom hR in
lemma D1_tab (i j c : Fin 4) : dG1 (GW ψ om R) p i j (Pi.single c 1) = D1T (jetAt ψ om R p) i j c := by
  obtain ⟨a1, -⟩ := jet_exp 2 hψ (p 0 - p 1)
  obtain ⟨d1, -⟩ := jet_exp (-2) hψ (p 0 - p 1)
  obtain ⟨b1, -⟩ := jet_mul (aF_smooth hψ) hom (p 0 - p 1)
  obtain ⟨c1, -⟩ := jet_mul (bF_smooth hψ hom) hom (p 0 - p 1)
  obtain ⟨q1, -⟩ := jet_mul hR hR (p 0)
  have ea : deriv (aF ψ) (p 0 - p 1) = _ := a1
  have ed : deriv (dF ψ) (p 0 - p 1) = _ := d1
  have eb : deriv (bF ψ om) (p 0 - p 1) = _ := b1
  have ec : deriv (cF ψ om) (p 0 - p 1) = _ := c1
  have eqq : deriv (qF R) (p 0) = _ := q1
  rw [dG1, GW, GWgen_fd1 (aF_smooth hψ) (bF_smooth hψ hom) (cF_smooth hψ hom) (dF_smooth hψ) (qF_smooth hR),
    ec, eb, ea, ed, eqq]
  fin_cases i <;> fin_cases j <;> fin_cases c <;>
    simp [cA, cB, cC, D1T, jetAt, aF, bF, cF, dF, qF, exp_neg_two, Real.exp_neg] <;> (try field_simp) <;> ring1

include hψ hom hR in
lemma D2_tab (i j a c : Fin 4) :
    dG2 (GW ψ om R) p i j (Pi.single a 1) (Pi.single c 1) = D2T (jetAt ψ om R p) i j a c := by
  obtain ⟨a1, a2⟩ := jet_exp 2 hψ (p 0 - p 1)
  obtain ⟨d1, d2⟩ := jet_exp (-2) hψ (p 0 - p 1)
  obtain ⟨b1, b2⟩ := jet_mul (aF_smooth hψ) hom (p 0 - p 1)
  obtain ⟨c1, c2⟩ := jet_mul (bF_smooth hψ hom) hom (p 0 - p 1)
  obtain ⟨q1, q2⟩ := jet_mul hR hR (p 0)
  have ea : deriv (aF ψ) (p 0 - p 1) = _ := a1
  have ea2 : deriv (deriv (aF ψ)) (p 0 - p 1) = _ := a2
  have ed : deriv (dF ψ) (p 0 - p 1) = _ := d1
  have ed2 : deriv (deriv (dF ψ)) (p 0 - p 1) = _ := d2
  have eb : deriv (bF ψ om) (p 0 - p 1) = _ := b1
  have eb2 : deriv (deriv (bF ψ om)) (p 0 - p 1) = _ := b2
  have ec2 : deriv (deriv (cF ψ om)) (p 0 - p 1) = _ := c2
  have eqq : deriv (qF R) (p 0) = _ := q1
  have eqq2 : deriv (deriv (qF R)) (p 0) = _ := q2
  rw [dG2, GW, GWgen_fd2 (aF_smooth hψ) (bF_smooth hψ hom) (cF_smooth hψ hom) (dF_smooth hψ) (qF_smooth hR),
    ec2, eb2, ea2, eb, ea, ed2, ed, eqq2, eqq]
  fin_cases i <;> fin_cases j <;> fin_cases a <;> fin_cases c <;>
    simp [cA, cB, cC, D2T, jetAt, aF, bF, cF, dF, qF, exp_neg_two, Real.exp_neg] <;> (try field_simp) <;> ring1

lemma jE : (jetAt ψ om R p).E ≠ 0 := (Real.exp_pos _).ne'

include hR0 in
lemma jr : (jetAt ψ om R p).r0 ≠ 0 := hR0 (p 0)

include hR0 in
lemma Gi_inv (m k : Fin 4) : ∑ l, GW ψ om R m l p * GiT (jetAt ψ om R p) l k = if m = k then 1 else 0 := by
  simp only [G_tab]
  exact GiT_ok _ (jE p) (jr hR0 p) m k

end GowdyTables

/-! ## The headlines -/

section Headlines

variable {ψ om R : ℝ → ℝ} (hψ : ContDiff ℝ ∞ ψ) (hom : ContDiff ℝ ∞ om) (hR : ContDiff ℝ ∞ R)

include hψ hom hR in
/-- **The Pontryagin density of the plane-wave Gowdy metric, for ANY profiles.** With `ψ = ψ(t − z)`,
`ω = ω(t − z)` arbitrary smooth and `R = R(t)` smooth and nowhere zero, THE connection's
`*RR = ½ ε^{mnrs} R_{mnab} R_{rs}{}^{ab} / √(−g)` at `p` is
`4 e^{2ψ} (4ψ′ω′ R R″ − 2ψ′ω′ R′² + ω″ R R″) / (R² |R|)`, with `ψ, ω` and their derivatives at `u = t − z` and
`R` and its derivatives at `t`. -/
theorem gowdy_pontryagin (hR0 : ∀ s, R s ≠ 0) (p : Fin 4 → ℝ) :
    pontryaginLC (GW ψ om R) (GW_symm ψ om R) (fun y u h => GW_nondeg hR0 y u h) (GW_smooth hψ hom hR) p
      = 4 * Real.exp (2 * ψ (p 0 - p 1)) * (4 * deriv ψ (p 0 - p 1) * deriv om (p 0 - p 1) * R (p 0)
          * deriv (deriv R) (p 0) - 2 * deriv ψ (p 0 - p 1) * deriv om (p 0 - p 1) * deriv R (p 0) ^ 2
          + deriv (deriv om) (p 0 - p 1) * R (p 0) * deriv (deriv R) (p 0)) / (R (p 0) ^ 2 * |R (p 0)|) := by
  rw [(tabs_bridge (GW_symm ψ om R) (fun y u h => GW_nondeg hR0 y u h) (GW_smooth hψ hom hR) (G_tab p)
    (Gi_inv hR0 p) (D1_tab hψ hom hR p) (D2_tab hψ hom hR p)).1]
  have hc : RiemF (D1T (jetAt ψ om R p)) (D2T (jetAt ψ om R p)) (GiT (jetAt ψ om R p)) = RT (jetAt ψ om R p) := by
    funext i j k l; exact RT_ok _ (jE p) (jr hR0 p) i j k l
  rw [hc, pont_ok _ (jE p) (jr hR0 p)]
  simp only [jetAt]

include hψ hom hR in
/-- **The Chern–Simons current of the plane-wave Gowdy metric, for ANY profiles** (THE connection's `K^μ`):
`K^t = −2e^{2ψ} R′(6ψ′ω′ + ω″)/R`, `K^z = −2e^{2ψ}(6ψ′RR′ω′ + RR′ω″ − RR″ω′ − R′²ω′)/R²`, `K^x = K^y = 0`. -/
theorem gowdy_cs (hR0 : ∀ s, R s ≠ 0) (p : Fin 4 → ℝ) :
    let K := csLC (GW ψ om R) (GW_symm ψ om R) (fun y u h => GW_nondeg hR0 y u h) (GW_smooth hψ hom hR) p
    let J := jetAt ψ om R p
    K 0 = -2 * J.E * J.r1 * (6 * J.p1 * J.w1 + J.w2) / J.r0 ∧
    K 1 = -2 * J.E * (6 * J.p1 * J.r0 * J.r1 * J.w1 + J.r0 * J.r1 * J.w2 - J.r0 * J.r2 * J.w1 - J.r1 ^ 2 * J.w1)
        / J.r0 ^ 2 ∧ K 2 = 0 ∧ K 3 = 0 := by
  intro K J
  have e1 : GamF (D1T (jetAt ψ om R p)) (GiT (jetAt ψ om R p)) = GamT (jetAt ψ om R p) := by
    funext i j k; exact GamT_ok _ (jE p) (jr hR0 p) i j k
  have e2 : DGamF (D1T (jetAt ψ om R p)) (D2T (jetAt ψ om R p)) (GiT (jetAt ψ om R p)) = DGT (jetAt ψ om R p) := by
    funext u i j k; exact DGT_ok _ (jE p) (jr hR0 p) u i j k
  have hK : ∀ μ, K μ = csArr (GamT J) (DGT J) μ := fun μ => by
    have := (tabs_bridge (GW_symm ψ om R) (fun y u h => GW_nondeg hR0 y u h) (GW_smooth hψ hom hR) (G_tab p)
      (Gi_inv hR0 p) (D1_tab hψ hom hR p) (D2_tab hψ hom hR p)).2 μ
    rw [e1, e2] at this
    exact this
  rw [hK, hK, hK, hK]
  exact cs_ok J (jr hR0 p)

include hψ hom in
/-- **`R = 1`: a pure plane wave gives exactly zero, however polarised** (the receipt's first check). -/
theorem gowdy_plane_wave_pontryagin (p : Fin 4 → ℝ) :
    pontryaginLC (GW ψ om fun _ => 1) (GW_symm ψ om _) (fun y u h => GW_nondeg (fun _ => one_ne_zero) y u h)
      (GW_smooth hψ hom contDiff_const) p = 0 := by
  rw [gowdy_pontryagin hψ hom contDiff_const (fun _ => one_ne_zero)]
  simp

include hψ hom hR in
/-- **`R = t` (the areal factor) near a point with `t > 0`**: `*RR = −8 e^{2ψ} ψ′ ω′ / t³`. Since `R` must be
smooth and nowhere zero on all of `ℝ` for the engine, it is any such profile equal to `t` near `t₀`
(`areal_profile_exists`); curvature at the point sees only the jet there. -/
theorem gowdy_areal_pontryagin (hR0 : ∀ s, R s ≠ 0) (p : Fin 4 → ℝ) (hp : 0 < p 0)
    (eR : R =ᶠ[𝓝 (p 0)] fun s => s) :
    pontryaginLC (GW ψ om R) (GW_symm ψ om R) (fun y u h => GW_nondeg hR0 y u h) (GW_smooth hψ hom hR) p
      = -8 * Real.exp (2 * ψ (p 0 - p 1)) * deriv ψ (p 0 - p 1) * deriv om (p 0 - p 1) / p 0 ^ 3 := by
  have h0 : R (p 0) = p 0 := eR.eq_of_nhds
  have h1 : deriv R (p 0) = 1 := by rw [eR.deriv_eq]; simp
  have h2 : deriv (deriv R) (p 0) = 0 := by
    rw [(eR.deriv.trans (Eventually.of_forall fun s => by simp) : deriv R =ᶠ[𝓝 (p 0)] fun _ => (1 : ℝ)).deriv_eq]
    simp
  rw [gowdy_pontryagin hψ hom hR hR0, h0, h1, h2, abs_of_pos hp]
  field_simp
  ring1

include hψ hom hR in
/-- **Silencing either channel kills it**: with the areal factor, `*RR = 0` wherever `ψ′ = 0` or `ω′ = 0` (in
particular for a constant `ψ` or a constant `ω`, the receipt's rebuilt metrics). -/
theorem gowdy_areal_silenced (hR0 : ∀ s, R s ≠ 0) (p : Fin 4 → ℝ) (hp : 0 < p 0)
    (eR : R =ᶠ[𝓝 (p 0)] fun s => s) (h : deriv ψ (p 0 - p 1) = 0 ∨ deriv om (p 0 - p 1) = 0) :
    pontryaginLC (GW ψ om R) (GW_symm ψ om R) (fun y u h => GW_nondeg hR0 y u h) (GW_smooth hψ hom hR) p = 0 := by
  rw [gowdy_areal_pontryagin hψ hom hR hR0 p hp eR]
  rcases h with h | h <;> simp [h]

/-- The areal profiles exist: for `t₀ > 0` there is a smooth, nowhere-zero `R` equal to `t` near `t₀`. -/
theorem areal_profile_exists {t₀ : ℝ} (ht : 0 < t₀) :
    ∃ R : ℝ → ℝ, ContDiff ℝ ∞ R ∧ (∀ s, R s ≠ 0) ∧ R =ᶠ[𝓝 t₀] fun s => s :=
  exists_global_profile ht contDiff_id.contDiffOn ht.ne'

end Headlines

/-! ## Part 3: the current and Stokes on the member `gowdy(0, log(t − z), t − z, t)` -/

section Stokes

open intervalIntegral MeasureTheory
open scoped Interval

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

lemma rho_ne (s : ℝ) : rho s ≠ 0 := by have := rho_ge s; positivity

lemma rho_eq {s : ℝ} (h : 3 / 2 ≤ s) : rho s = s := by
  unfold rho; rw [Real.smoothTransition.one_of_one_le (by linarith)]; ring

lemma rho_ev {s : ℝ} (h : 3 / 2 < s) : rho =ᶠ[𝓝 s] fun x => x :=
  Filter.mem_of_superset (Ioi_mem_nhds h) fun x hx => rho_eq (le_of_lt hx)

/-- `ψ = log ρ`, equal to `log u` for `u ≥ 3/2`. -/
noncomputable def psiM (s : ℝ) : ℝ := Real.log (rho s)

lemma psiM_smooth : ContDiff ℝ ∞ psiM := rho_smooth.log rho_ne

lemma psiM_ev {s : ℝ} (h : 3 / 2 < s) : psiM =ᶠ[𝓝 s] Real.log :=
  (rho_ev h).mono fun x hx => by simp only [psiM, hx]

/-- **The member** `gowdy(0, log(t − z), t − z, t)` on the region `t > 3/2`, `t − z > 3/2` (which contains the closed
rectangle `[3,5] × [0,1]`): row 69's `GW` with the global profiles `ψ = log ρ`, `ω = id`, `R = ρ`. -/
noncomputable def GM : Fin 4 → Fin 4 → (Fin 4 → ℝ) → ℝ := GW psiM (fun s => s) rho

lemma GM_nondeg : ∀ y (u : Fin 4 → ℝ), (∀ v, formG GM y u v = 0) → u = 0 :=
  fun y u h => GW_nondeg rho_ne y u h
lemma GM_smooth : ∀ i j, ContDiff ℝ ∞ (GM i j) := GW_smooth psiM_smooth contDiff_id rho_smooth
lemma GM_symm : ∀ i j p, GM i j p = GM j i p := fun i j p => GW_symm _ _ _ i j p

/-- The member's metric entries on the region are the receipt's: `g_xx = u², g_xy = u³, g_yy = u⁴ + t²/u²`. -/
theorem GM_apply {p : Fin 4 → ℝ} (h0 : 3 / 2 < p 0) (h1 : 3 / 2 < p 0 - p 1) :
    GM 2 2 p = (p 0 - p 1) ^ 2 ∧ GM 2 3 p = (p 0 - p 1) ^ 3 ∧
      GM 3 3 p = (p 0 - p 1) ^ 4 + p 0 ^ 2 / (p 0 - p 1) ^ 2 := by
  have hu : 0 < p 0 - p 1 := by linarith
  have e1 : Real.exp (2 * psiM (p 0 - p 1)) = (p 0 - p 1) ^ 2 := by
    rw [psiM, rho_eq h1.le, show 2 * Real.log (p 0 - p 1) = Real.log (p 0 - p 1) + Real.log (p 0 - p 1) by ring,
      Real.exp_add, Real.exp_log hu]; ring
  have e2 : Real.exp (-(2 * psiM (p 0 - p 1))) = ((p 0 - p 1) ^ 2)⁻¹ := by rw [Real.exp_neg, e1]
  simp only [GM, GW_apply, rho_eq h0.le]
  simp [e1, e2]
  refine ⟨by ring, by field_simp⟩

lemma mvals {p : Fin 4 → ℝ} (h0 : 3 / 2 < p 0) (h1 : 3 / 2 < p 0 - p 1) :
    Real.exp (2 * psiM (p 0 - p 1)) = (p 0 - p 1) ^ 2 ∧ deriv psiM (p 0 - p 1) = 1 / (p 0 - p 1) ∧
    deriv (deriv psiM) (p 0 - p 1) = -1 / (p 0 - p 1) ^ 2 ∧ deriv (fun s : ℝ => s) (p 0 - p 1) = 1 ∧
    deriv (deriv fun s : ℝ => s) (p 0 - p 1) = 0 ∧ rho (p 0) = p 0 ∧ deriv rho (p 0) = 1 ∧
    deriv (deriv rho) (p 0) = 0 := by
  have hu : 0 < p 0 - p 1 := by linarith
  have eψ := psiM_ev h1
  have dψ : deriv psiM =ᶠ[𝓝 (p 0 - p 1)] fun x => x⁻¹ :=
    eψ.deriv.trans (Eventually.of_forall fun x => by simp [Real.deriv_log'])
  have dR : deriv rho =ᶠ[𝓝 (p 0)] fun _ => (1 : ℝ) :=
    (rho_ev h0).deriv.trans (Eventually.of_forall fun x => by simp)
  refine ⟨?_, ?_, ?_, by simp, by simp, rho_eq h0.le, dR.eq_of_nhds, by rw [dR.deriv_eq]; simp⟩
  · rw [psiM, rho_eq h1.le, show 2 * Real.log (p 0 - p 1) = Real.log (p 0 - p 1) + Real.log (p 0 - p 1) by ring,
      Real.exp_add, Real.exp_log hu]; ring
  · rw [dψ.eq_of_nhds, one_div]
  · rw [dψ.deriv_eq, deriv_inv]; field_simp

lemma jet_member {p : Fin 4 → ℝ} (h0 : 3 / 2 < p 0) (h1 : 3 / 2 < p 0 - p 1) :
    jetAt psiM (fun s => s) rho p = ⟨(p 0 - p 1) ^ 2, 1 / (p 0 - p 1), -1 / (p 0 - p 1) ^ 2, p 0 - p 1, 1, 0,
      p 0, 1, 0⟩ := by
  obtain ⟨e1, e2, e3, e4, e5, e6, e7, e8⟩ := mvals h0 h1
  simp only [jetAt, e1, e2, e3, e4, e5, e6, e7, e8]

/-- **The current on the member**: `K^t = −12u/t`, `K^z = −2u(5t + z)/t²`, `K^x = K^y = 0` (`u = t − z`), at every
point of the region (whatever `x`, `y`). -/
theorem member_cs {p : Fin 4 → ℝ} (h0 : 3 / 2 < p 0) (h1 : 3 / 2 < p 0 - p 1) :
    csLC GM GM_symm GM_nondeg GM_smooth p 0 = -12 * (p 0 - p 1) / p 0 ∧
    csLC GM GM_symm GM_nondeg GM_smooth p 1 = -2 * (p 0 - p 1) * (5 * p 0 + p 1) / p 0 ^ 2 ∧
    csLC GM GM_symm GM_nondeg GM_smooth p 2 = 0 ∧ csLC GM GM_symm GM_nondeg GM_smooth p 3 = 0 := by
  have hu : p 0 - p 1 ≠ 0 := by intro h; linarith
  have ht : p 0 ≠ 0 := by intro h; linarith
  obtain ⟨k0, k1, k2, k3⟩ := gowdy_cs (om := fun s : ℝ => s) psiM_smooth contDiff_id rho_smooth rho_ne p
  simp only [jet_member h0 h1] at k0 k1
  refine ⟨?_, ?_, k2, k3⟩
  · refine k0.trans ?_; field_simp; ring
  · refine k1.trans ?_; field_simp; ring

/-- **The density on the member**: `*RR = −8u/t³`, and `√(−det g) *RR = −8u/t²`. -/
theorem member_pontryagin {p : Fin 4 → ℝ} (h0 : 3 / 2 < p 0) (h1 : 3 / 2 < p 0 - p 1) :
    pontryaginLC GM GM_symm GM_nondeg GM_smooth p = -8 * (p 0 - p 1) / p 0 ^ 3 ∧
    Real.sqrt (-(gm GM p).det) * pontryaginLC GM GM_symm GM_nondeg GM_smooth p = -8 * (p 0 - p 1) / p 0 ^ 2 := by
  have hu : p 0 - p 1 ≠ 0 := by intro h; linarith
  have ht : 0 < p 0 := by linarith
  have hP : pontryaginLC GM GM_symm GM_nondeg GM_smooth p = -8 * (p 0 - p 1) / p 0 ^ 3 := by
    have := gowdy_pontryagin (om := fun s : ℝ => s) psiM_smooth contDiff_id rho_smooth rho_ne p
    obtain ⟨e1, e2, e3, e4, e5, e6, e7, e8⟩ := mvals h0 h1
    refine this.trans ?_
    simp only [e1, e2, e3, e4, e5, e6, e7, e8, abs_of_pos ht]
    field_simp; ring
  have hdet : (gm GM p).det = -p 0 ^ 2 := by
    have hg : gm GM p = Matrix.of (GT (jetAt psiM (fun s => s) rho p)) := by
      ext i j; exact G_tab (ψ := psiM) (om := fun s => s) (R := rho) p i j
    rw [hg, det_ok _ (jE p), jet_member h0 h1]
  refine ⟨hP, ?_⟩
  rw [hP, hdet, neg_neg, Real.sqrt_sq ht.le]
  field_simp

/-- **Part 2, the unpolarised member is nonzero** (an exhibit): at `(t, z) = (4, 1/2)`, `*RR = −7/16`. -/
theorem unpolarised_nonzero :
    pontryaginLC GM GM_symm GM_nondeg GM_smooth ![4, 1 / 2, 0, 0] = -7 / 16 ∧
      pontryaginLC GM GM_symm GM_nondeg GM_smooth ![4, 1 / 2, 0, 0] ≠ 0 := by
  have := (member_pontryagin (p := ![4, 1 / 2, 0, 0]) (by norm_num) (by norm_num)).1
  simp only [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val] at this
  norm_num at this
  exact ⟨by rw [this]; norm_num, by rw [this]; norm_num⟩

/-- The points of the `(t, z)` plane (`x = y = 0`). -/
def pt (x : ℝ × ℝ) : Fin 4 → ℝ := ![x.1, x.2, 0, 0]

/-- `K^t`, `K^z` and `√−g *RR` on the `(t, z)` plane. -/
noncomputable def Kt (x : ℝ × ℝ) : ℝ := csLC GM GM_symm GM_nondeg GM_smooth (pt x) 0
noncomputable def Kz (x : ℝ × ℝ) : ℝ := csLC GM GM_symm GM_nondeg GM_smooth (pt x) 1
noncomputable def dens (x : ℝ × ℝ) : ℝ :=
  Real.sqrt (-(gm GM (pt x)).det) * pontryaginLC GM GM_symm GM_nondeg GM_smooth (pt x)

/-- The region. -/
def U : Set (ℝ × ℝ) := {x | 3 / 2 < x.1 ∧ 3 / 2 < x.1 - x.2}

lemma U_open : IsOpen U :=
  (isOpen_lt continuous_const continuous_fst).inter (isOpen_lt continuous_const (continuous_fst.sub continuous_snd))

lemma evU {x : ℝ × ℝ} (hx : x ∈ U) : ∀ᶠ y in 𝓝 x, y ∈ U := U_open.mem_nhds hx

noncomputable def kt (x : ℝ × ℝ) : ℝ := -12 * (x.1 - x.2) * (x.1)⁻¹
noncomputable def kz (x : ℝ × ℝ) : ℝ := -2 * (x.1 - x.2) * (5 * x.1 + x.2) * (x.1 ^ 2)⁻¹
noncomputable def dd (x : ℝ × ℝ) : ℝ := -8 * (x.1 - x.2) / x.1 ^ 2

lemma on_U {x : ℝ × ℝ} (hx : x ∈ U) : Kt x = kt x ∧ Kz x = kz x ∧ dens x = dd x := by
  obtain ⟨c0, c1, -, -⟩ := member_cs (p := pt x) hx.1 hx.2
  obtain ⟨-, d⟩ := member_pontryagin (p := pt x) hx.1 hx.2
  simp only [pt, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val] at c0 c1 d
  refine ⟨?_, ?_, ?_⟩
  · simp only [Kt, pt]; rw [c0, kt, div_eq_mul_inv]
  · simp only [Kz, pt]; rw [c1, kz, div_eq_mul_inv]
  · simp only [dens, pt]; rw [d, dd]

lemma kt_hasFDerivAt {x : ℝ × ℝ} (hx : x.1 ≠ 0) :
    HasFDerivAt kt (fderiv ℝ kt x) x ∧ fderiv ℝ kt x (1, 0) = -12 * x.2 / x.1 ^ 2 := by
  have hf : HasFDerivAt (fun y : ℝ × ℝ => y.1) (ContinuousLinearMap.fst ℝ ℝ ℝ) x := hasFDerivAt_fst
  have hs : HasFDerivAt (fun y : ℝ × ℝ => y.2) (ContinuousLinearMap.snd ℝ ℝ ℝ) x := hasFDerivAt_snd
  have h : HasFDerivAt kt _ x := ((hf.sub hs).const_mul (-12 : ℝ)).mul ((hasDerivAt_inv hx).comp_hasFDerivAt x hf)
  refine ⟨h.differentiableAt.hasFDerivAt, ?_⟩
  rw [h.fderiv]; simp; field_simp; ring

lemma kz_hasFDerivAt {x : ℝ × ℝ} (hx : x.1 ≠ 0) :
    HasFDerivAt kz (fderiv ℝ kz x) x ∧ fderiv ℝ kz x (0, 1) = (8 * x.1 + 4 * x.2) / x.1 ^ 2 := by
  have hf : HasFDerivAt (fun y : ℝ × ℝ => y.1) (ContinuousLinearMap.fst ℝ ℝ ℝ) x := hasFDerivAt_fst
  have hs : HasFDerivAt (fun y : ℝ × ℝ => y.2) (ContinuousLinearMap.snd ℝ ℝ ℝ) x := hasFDerivAt_snd
  have h : HasFDerivAt kz _ x :=
    (((hf.sub hs).const_mul (-2 : ℝ)).mul ((hf.const_mul (5 : ℝ)).add hs)).mul
      ((hasDerivAt_inv (pow_ne_zero 2 hx)).comp_hasFDerivAt x (hf.pow 2))
  refine ⟨h.differentiableAt.hasFDerivAt, ?_⟩
  rw [h.fderiv]; simp; field_simp; ring

/-- **`∂_μ K^μ = −√−g *RR` on the member**, at every point of the region: `∂_t K^t + ∂_z K^z = −√−g *RR` (the receipt's
ratio `−1`), with `K^x = K^y = 0` there (`member_cs`). -/
theorem member_divergence {x : ℝ × ℝ} (hx : x ∈ U) :
    fderiv ℝ Kt x (1, 0) + fderiv ℝ Kz x (0, 1) = -dens x := by
  have h1 : x.1 ≠ 0 := by have := hx.1; intro h; linarith
  have ev : ∀ᶠ y in 𝓝 x, y ∈ U := U_open.mem_nhds hx
  have et : Kt =ᶠ[𝓝 x] kt := ev.mono fun y hy => (on_U hy).1
  have ez : Kz =ᶠ[𝓝 x] kz := ev.mono fun y hy => (on_U hy).2.1
  rw [et.fderiv_eq, ez.fderiv_eq, (kt_hasFDerivAt h1).2, (kz_hasFDerivAt h1).2, (on_U hx).2.2, dd]
  field_simp; ring

lemma rect_U {x : ℝ × ℝ} (hx : x ∈ [[(3 : ℝ), 5]] ×ˢ [[(0 : ℝ), 1]]) : x ∈ U := by
  obtain ⟨h1, h2⟩ := hx
  rw [Set.uIcc_of_le (by norm_num)] at h1 h2
  exact ⟨by linarith [h1.1], by linarith [h1.1, h2.2]⟩

lemma ioo_U {x : ℝ × ℝ}
    (hx : x ∈ Ioo (min (3 : ℝ) 5) (max 3 5) ×ˢ Ioo (min (0 : ℝ) 1) (max 0 1)) : x ∈ U := by
  obtain ⟨h1, h2⟩ := hx
  simp only [Set.mem_Ioo] at h1 h2
  norm_num at h1 h2
  exact ⟨by linarith [h1.1], by linarith [h1.1, h2.2]⟩

/-- **Stokes on the rectangle `[3,5] × [0,1]`** (Mathlib's divergence theorem): the volume integral of `√−g *RR`
equals MINUS the boundary flux of `(K^t, K^z)`. -/
theorem member_stokes :
    (∫ t in (3 : ℝ)..5, ∫ z in (0 : ℝ)..1, dens (t, z)) =
      -((((∫ t in (3 : ℝ)..5, Kz (t, 1)) - ∫ t in (3 : ℝ)..5, Kz (t, 0)) + ∫ z in (0 : ℝ)..1, Kt (5, z))
        - ∫ z in (0 : ℝ)..1, Kt (3, z)) := by
  have hne : ∀ x ∈ U, x.1 ≠ 0 := fun x hx h => by have := hx.1; linarith
  rw [← integral2_divergence_prod_of_hasFDerivAt_off_countable Kt Kz (fun x => fderiv ℝ kt x)
    (fun x => fderiv ℝ kz x) 3 0 5 1 ∅ Set.countable_empty]
  · rw [← intervalIntegral.integral_neg]
    refine intervalIntegral.integral_congr fun t ht => ?_
    rw [← intervalIntegral.integral_neg]
    refine intervalIntegral.integral_congr fun z hz => ?_
    have hx : (t, z) ∈ U := rect_U ⟨ht, hz⟩
    have := member_divergence hx
    have et : Kt =ᶠ[𝓝 (t, z)] kt := (evU hx).mono fun y hy => (on_U hy).1
    have ez : Kz =ᶠ[𝓝 (t, z)] kz := (evU hx).mono fun y hy => (on_U hy).2.1
    rw [et.fderiv_eq, ez.fderiv_eq] at this
    linarith
  · refine ContinuousOn.congr (f := kt) ?_ fun x hx => (on_U (rect_U hx)).1
    exact ContinuousOn.mul (by fun_prop) (ContinuousOn.inv₀ (by fun_prop) fun x hx => hne x (rect_U hx))
  · refine ContinuousOn.congr (f := kz) ?_ fun x hx => (on_U (rect_U hx)).2.1
    exact ContinuousOn.mul (by fun_prop) (ContinuousOn.inv₀ (by fun_prop) fun x hx => pow_ne_zero 2 (hne x (rect_U hx)))
  · intro x hx
    have hU : x ∈ U := ioo_U hx.1
    exact (kt_hasFDerivAt (hne x hU)).1.congr_of_eventuallyEq
      ((evU hU).mono fun y hy => (on_U hy).1)
  · intro x hx
    have hU : x ∈ U := ioo_U hx.1
    exact (kz_hasFDerivAt (hne x hU)).1.congr_of_eventuallyEq
      ((evU hU).mono fun y hy => (on_U hy).2.1)
  · refine (ContinuousOn.integrableOn_compact (isCompact_uIcc.prod isCompact_uIcc)
      (f := fun x : ℝ × ℝ => 8 * (x.1 - x.2) / x.1 ^ 2) ?_).congr_fun (fun x hx => ?_)
      (measurableSet_uIcc.prod measurableSet_uIcc)
    · exact ContinuousOn.div (by fun_prop) (by fun_prop) fun x hx => pow_ne_zero 2 (hne x (rect_U hx))
    · have h1 := hne x (rect_U hx)
      simp only [(kt_hasFDerivAt h1).2, (kz_hasFDerivAt h1).2]
      field_simp; ring

/-- **The common value is nonzero**: `∫∫ √−g *RR = 8/15 − 8 log(5/3) = log(6561/390625) + 8/15 < 0`. -/
theorem member_volume :
    (∫ t in (3 : ℝ)..5, ∫ z in (0 : ℝ)..1, dens (t, z)) = 8 / 15 - 8 * Real.log (5 / 3) ∧
      8 / 15 - 8 * Real.log (5 / 3) = Real.log (6561 / 390625) + 8 / 15 ∧
      8 / 15 - 8 * Real.log (5 / 3) < 0 := by
  have inner : ∀ t ∈ [[(3 : ℝ), 5]], (∫ z in (0 : ℝ)..1, dens (t, z)) = -8 / t + 4 / t ^ 2 := by
    intro t ht
    have ht' : 3 ≤ t := by rw [Set.uIcc_of_le (by norm_num)] at ht; exact ht.1
    have htn : t ≠ 0 := by intro h; linarith
    rw [intervalIntegral.integral_congr (g := fun z => -8 * (t - z) / t ^ 2) fun z hz => by
      have hU : (t, z) ∈ U := rect_U ⟨ht, hz⟩
      simp only [(on_U hU).2.2, dd] ]
    rw [integral_eq_sub_of_hasDerivAt (f := fun z => -8 * (t * z - z ^ 2 / 2) / t ^ 2) (fun z _ => by
      have := ((((hasDerivAt_id z).const_mul t).sub ((hasDerivAt_pow 2 z).div_const 2)).const_mul (-8 : ℝ)).div_const
        (t ^ 2)
      convert this using 1; simp; ring) (by apply Continuous.intervalIntegrable; fun_prop)]
    field_simp; ring
  rw [intervalIntegral.integral_congr inner]
  have hF : ∀ t ∈ [[(3 : ℝ), 5]], HasDerivAt (fun t => -8 * Real.log t - 4 / t) (-8 / t + 4 / t ^ 2) t := by
    intro t ht
    have ht' : 0 < t := by rw [Set.uIcc_of_le (by norm_num)] at ht; linarith [ht.1]
    have := ((Real.hasDerivAt_log ht'.ne').const_mul (-8 : ℝ)).sub ((hasDerivAt_inv ht'.ne').const_mul (4 : ℝ))
    convert this using 1
    · funext s; simp [div_eq_mul_inv]
    · field_simp; ring
  rw [integral_eq_sub_of_hasDerivAt hF (by
    refine ContinuousOn.intervalIntegrable ?_
    refine ContinuousOn.add (ContinuousOn.div continuousOn_const continuousOn_id fun t ht => ?_)
      (ContinuousOn.div continuousOn_const (continuousOn_id.pow 2) fun t ht => ?_)
    all_goals rw [Set.uIcc_of_le (by norm_num)] at ht; have := ht.1; positivity)]
  have l53 : Real.log (5 / 3) = Real.log 5 - Real.log 3 := Real.log_div (by norm_num) (by norm_num)
  refine ⟨by rw [l53]; ring, ?_, ?_⟩
  · have : (6561 / 390625 : ℝ) = (5 / 3) ^ (-8 : ℤ) := by norm_num
    rw [this, Real.log_zpow]; push_cast; ring
  · have := Real.one_sub_inv_le_log_of_pos (show (0 : ℝ) < 5 / 3 by norm_num)
    norm_num at this; linarith

end Stokes

/-! ## Part 6: the arithmetic -/

/-- **Part 6.** `Δ N_CS = 0` (every component of the current vanishes on the class, `sph_cs_zero`), coefficient `3`,
net count `3 × 0 = 0`. -/
theorem net_count : (3 : ℤ) * 0 = 0 := by norm_num

end R96ChernSimons

end ShadowProbe

#print axioms ShadowProbe.R96ChernSimons.eps4_sign
#print axioms ShadowProbe.R96ChernSimons.eps4_det
#print axioms ShadowProbe.R96ChernSimons.sum_eps
#print axioms ShadowProbe.R96ChernSimons.pontryaginLC_eq
#print axioms ShadowProbe.R96ChernSimons.riemLC_tab
#print axioms ShadowProbe.R96ChernSimons.csLC_tab
#print axioms ShadowProbe.R96ChernSimons.tabs_bridge
#print axioms ShadowProbe.R96ChernSimons.pontryagin_parity
#print axioms ShadowProbe.R96ChernSimons.cs_parity
#print axioms ShadowProbe.R96ChernSimons.csArr_three
#print axioms ShadowProbe.R96ChernSimons.warped_pontryagin
#print axioms ShadowProbe.R96ChernSimons.warped_cs
#print axioms ShadowProbe.R96ChernSimons.sph_pontryagin_zero
#print axioms ShadowProbe.R96ChernSimons.sph_cs_zero
#print axioms ShadowProbe.R96ChernSimons.polarised_pontryagin_zero
#print axioms ShadowProbe.R96ChernSimons.nariai_general_pontryagin_zero
#print axioms ShadowProbe.R96ChernSimons.nariai_rotated_pontryagin_zero
#print axioms ShadowProbe.R96ChernSimons.nariai_pontryagin_zero
#print axioms ShadowProbe.R96ChernSimons.nariai_apply
#print axioms ShadowProbe.R96ChernSimons.GW_apply
#print axioms ShadowProbe.R96ChernSimons.gowdy_pontryagin
#print axioms ShadowProbe.R96ChernSimons.gowdy_cs
#print axioms ShadowProbe.R96ChernSimons.gowdy_plane_wave_pontryagin
#print axioms ShadowProbe.R96ChernSimons.gowdy_areal_pontryagin
#print axioms ShadowProbe.R96ChernSimons.gowdy_areal_silenced
#print axioms ShadowProbe.R96ChernSimons.areal_profile_exists
#print axioms ShadowProbe.R96ChernSimons.GM_apply
#print axioms ShadowProbe.R96ChernSimons.member_cs
#print axioms ShadowProbe.R96ChernSimons.member_pontryagin
#print axioms ShadowProbe.R96ChernSimons.unpolarised_nonzero
#print axioms ShadowProbe.R96ChernSimons.member_divergence
#print axioms ShadowProbe.R96ChernSimons.member_stokes
#print axioms ShadowProbe.R96ChernSimons.member_volume
#print axioms ShadowProbe.R96ChernSimons.net_count

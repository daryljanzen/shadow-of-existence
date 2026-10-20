import ShadowEngine

/-! # Campaign 43 (`r7443+71.29`): the general transgression identity `∂_μK^μ = −√−g *RR`

Pre-registered at `computations/formalisation/r7443_71_campaign43/PREDICTION.md`.

* **Layer 1, algebra** (`transgression_alg`). For ANY `Γ : Fin 4 → Matrix (Fin 4) (Fin 4) ℝ`, any first derivatives
  `dΓ μ ν = ∂_μΓ_ν` and any `ddΓ l ρ σ = ∂_l∂_ρΓ_σ` symmetric in `l, ρ`, with `F_{μν} = ∂_μΓ_ν − ∂_νΓ_μ + [Γ_μ, Γ_ν]`:
  `Σ ε^{μνρσ} tr(F_{μν}F_{ρσ}) = 4 Σ_μ ∂_μ[Σ ε^{μνρσ} tr(Γ_ν∂_ρΓ_σ + ⅔Γ_νΓ_ρΓ_σ)]`, `∂_μ` by the product rule
  (`dCS`). Proved from trace cyclicity, the sign of `ε` under six reindexings (`esum_perm`, each sign by
  `decide +kernel`), and Schwarz; no component expansion. The quartic term dies on the odd `4`-cycle (`esum_cyc4`).
* **Layer 2, bridge** (`transgression`). On THE connection (`lcConn`) of any smooth nondegenerate `Σ Gᵢⱼ dxᵢ dxⱼ` on
  `ℝ⁴`, `(Γ_ν)ᵃ_b = Γᵃ_{νb}` (row 96's `chrLC`): `F` is the engine's `curv` (`Fc_eq_curv`); row 96's current is
  `csLC = 2 CS` (`csArr_eq_CS`), its divergence `2 Σ ∂_μCS^μ` (`div_csLC`, Fréchet derivatives of `chrLC`, Schwarz
  `ddchr_symm`); row 69's density satisfies `√(−det g) *RR = −½ Σ ε tr(FF)` (`pont_tab`, via the pair symmetry
  `L1_pair` and antisymmetry `L1_anti` of the lowered tabled curvature). Hence, at every point with `det g < 0`:
  `Σ_μ ∂_μ csLC^μ = −√(−det g) · pontryaginLC`. The sign is derived, not chosen.
* **Layer 3, corollaries.** `ratio_neg_one`: the receipts' ratio `−1` for every metric with `*RR ≠ 0`.
  `plane_divergence`: row 96's `member_divergence` statement (`∂_tK^t + ∂_zK^z = −√−g *RR` on the `(t, z)` plane) for
  ANY metric whose `K^x`, `K^y` vanish near the point; row 96's member `GM` has this on its region (`member_cs`).

**Caveats.** Coordinates on `ℝ⁴`, not the coordinate-free `d CS = tr(R ∧ R)`; covariance of `K` not claimed. The
hypothesis `det g < 0` is needed: `pontArr` divides by `√(−det g)`, which Lean sets to `0` when `det g > 0`.
The definitions `formG … csLC` below are copied verbatim from `probes/Row96ChernSimons.lean` (probes cannot import
probes). -/

set_option linter.unusedTactic false
set_option linter.unnecessarySeqFocus false
set_option linter.unusedSimpArgs false
set_option linter.unusedSectionVars false
set_option linter.unusedVariables false
set_option linter.style.longLine false
set_option linter.style.setOption false
set_option linter.flexible false

open Bundle Manifold Filter Set VectorField
open scoped ContDiff Manifold Topology

namespace ShadowProbe

namespace Transgression


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

/-- Row 96's `(t, z)` plane (`x = y = 0`), verbatim. -/
def pt (x : ℝ × ℝ) : Fin 4 → ℝ := ![x.1, x.2, 0, 0]

/-- Row 96's `Kt`, `Kz`, `dens`, for any metric (row 96 has them for its member `GM`). -/
noncomputable def KtG (x : ℝ × ℝ) : ℝ := csLC G hs hn hGs (pt x) 0
noncomputable def KzG (x : ℝ × ℝ) : ℝ := csLC G hs hn hGs (pt x) 1
noncomputable def densG (x : ℝ × ℝ) : ℝ :=
  Real.sqrt (-(gm G (pt x)).det) * pontryaginLC G hs hn hGs (pt x)

/-- `pt` as a continuous linear map. -/
noncomputable def ptL : ℝ × ℝ →L[ℝ] (Fin 4 → ℝ) :=
  ContinuousLinearMap.pi fun i => ![ContinuousLinearMap.fst ℝ ℝ ℝ, ContinuousLinearMap.snd ℝ ℝ ℝ, 0, 0] i

lemma pt_eq : pt = ptL := by
  funext x; ext i; fin_cases i <;> rfl

include hn hGs in
lemma fderiv_plane (μ : Fin 4) (x w : ℝ × ℝ) :
    fderiv ℝ (fun x => csLC G hs hn hGs (pt x) μ) x w
      = fderiv ℝ (fun y => csLC G hs hn hGs y μ) (pt x) (ptL w) := by
  obtain ⟨L, hL, -⟩ := HD_csLC hs hn hGs (pt x) μ
  rw [pt_eq] at hL ⊢
  have h := hL.comp x ptL.hasFDerivAt
  rw [show (fun x => csLC G hs hn hGs (ptL x) μ) = (fun y => csLC G hs hn hGs y μ) ∘ ptL from rfl, h.fderiv,
    hL.fderiv]; rfl

include hn hGs in
/-- **Row 96's `member_divergence`, for every metric**: on the `(t, z)` plane, wherever `det g < 0` and `K^x`, `K^y`
vanish near the point (row 96's `member_cs` gives both on its member's open region), `∂_tK^t + ∂_zK^z = −√−g *RR`. -/
theorem plane_divergence {x : ℝ × ℝ} (hdet : (gm G (pt x)).det < 0)
    (h2 : (fun y => csLC G hs hn hGs y 2) =ᶠ[nhds (pt x)] fun _ => 0)
    (h3 : (fun y => csLC G hs hn hGs y 3) =ᶠ[nhds (pt x)] fun _ => 0) :
    fderiv ℝ (KtG hs hn hGs) x (1, 0) + fderiv ℝ (KzG hs hn hGs) x (0, 1) = -densG hs hn hGs x := by
  have T := transgression hs hn hGs (pt x) hdet
  rw [Fin.sum_univ_four, h2.fderiv_eq, h3.fderiv_eq] at T
  have e0 : ptL (1, 0) = Pi.single 0 1 := by ext i; fin_cases i <;> simp [ptL]
  have e1 : ptL (0, 1) = Pi.single 1 1 := by ext i; fin_cases i <;> simp [ptL]
  show fderiv ℝ (fun x => csLC G hs hn hGs (pt x) 0) x (1, 0) + fderiv ℝ (fun x => csLC G hs hn hGs (pt x) 1) x (0, 1)
    = -(Real.sqrt (-(gm G (pt x)).det) * pontryaginLC G hs hn hGs (pt x))
  rw [fderiv_plane hs hn hGs, fderiv_plane hs hn hGs, e0, e1, ← T]
  simp

end Corollary

#print axioms ShadowProbe.Transgression.transgression_alg
#print axioms ShadowProbe.Transgression.L1_pair
#print axioms ShadowProbe.Transgression.pont_tab
#print axioms ShadowProbe.Transgression.csArr_eq_CS
#print axioms ShadowProbe.Transgression.div_csLC
#print axioms ShadowProbe.Transgression.Fc_eq_curv
#print axioms ShadowProbe.Transgression.transgression
#print axioms ShadowProbe.Transgression.ratio_neg_one
#print axioms ShadowProbe.Transgression.plane_divergence

end Transgression

end ShadowProbe

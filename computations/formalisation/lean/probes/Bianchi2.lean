import ShadowEngine

/-! # Campaign 8 (`r7353+71`): row 6, the contracted Bianchi identity in general

`L174…/I10`: "the contracted Bianchi identity … is OFF-SHELL and holds for ANY metric". The receipt checks it to
`O(ε²)` on one non-diagonal two-wave metric. Here it is built for THE connection of any metric the engine accepts.

Piece A is the differential (second) Bianchi identity. With `G = Γ(x)`, `D1 = DΓ(x)` and `D2 = D²Γ(x)`, the curvature
is `curv_model`'s `R(u,v)w = D1 u v w − D1 v u w + G u (G v w) − G v (G u w)`. Its covariant derivative's cyclic
sum vanishes, given:
- `G` symmetric (torsion-free);
- `D2` symmetric in its two directions (Schwarz) and in its last two slots. -/

open Bundle Manifold Filter Set VectorField
open scoped ContDiff Manifold Topology

namespace ShadowProbe

section Bianchi2

set_option synthInstance.maxHeartbeats 4000000

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]

/-- The curvature from a Christoffel form and its first derivative. -/
def RmB (G : E →L[ℝ] E →L[ℝ] E) (D1 : E →L[ℝ] E →L[ℝ] E →L[ℝ] E) (u v w : E) : E :=
  D1 u v w - D1 v u w + G u (G v w) - G v (G u w)

/-- Its derivative in direction `e`. -/
def DRmB (G : E →L[ℝ] E →L[ℝ] E) (D1 : E →L[ℝ] E →L[ℝ] E →L[ℝ] E)
    (D2 : E →L[ℝ] E →L[ℝ] E →L[ℝ] E →L[ℝ] E) (e u v w : E) : E :=
  D2 e u v w - D2 e v u w + D1 e u (G v w) + G u (D1 e v w) - D1 e v (G u w) - G v (D1 e u w)

/-- The covariant derivative `(∇_e R)(u, v) w`. -/
def nablaRB (G : E →L[ℝ] E →L[ℝ] E) (D1 : E →L[ℝ] E →L[ℝ] E →L[ℝ] E)
    (D2 : E →L[ℝ] E →L[ℝ] E →L[ℝ] E →L[ℝ] E) (e u v w : E) : E :=
  DRmB G D1 D2 e u v w + G e (RmB G D1 u v w) - RmB G D1 (G e u) v w - RmB G D1 u (G e v) w
    - RmB G D1 u v (G e w)

/-- **The differential Bianchi identity**, as algebra: `Σ_cyclic (∇_u R)(v, w) z = 0`. -/
theorem bianchi2_alg {G : E →L[ℝ] E →L[ℝ] E} {D1 : E →L[ℝ] E →L[ℝ] E →L[ℝ] E}
    {D2 : E →L[ℝ] E →L[ℝ] E →L[ℝ] E →L[ℝ] E}
    (hG : ∀ a b, G a b = G b a) (hD2 : ∀ e f a b, D2 e f a b = D2 f e a b)
    (u v w z : E) :
    nablaRB G D1 D2 u v w z + nablaRB G D1 D2 v w u z + nablaRB G D1 D2 w u v z = 0 := by
  simp only [nablaRB, DRmB, RmB, map_add, map_sub]
  rw [hD2 v u, hD2 w v, hD2 u w, hG v u, hG w v, hG u w]
  abel

/-- `DRmB` IS the derivative of the curvature closed form, for any smooth `Γ`. -/
lemma hasFDerivAt_RmB {Γ : E → E →L[ℝ] E →L[ℝ] E} (hΓ : ContDiff ℝ ∞ Γ) (x u v w : E) :
    ∃ L : E →L[ℝ] E, HasFDerivAt (fun y => RmB (Γ y) (fderiv ℝ Γ y) u v w) L x ∧
      ∀ e, L e = DRmB (Γ x) (fderiv ℝ Γ x) (fderiv ℝ (fderiv ℝ Γ) x) e u v w := by
  have h0 : HasFDerivAt Γ (fderiv ℝ Γ x) x := (hΓ.differentiable (by simp) x).hasFDerivAt
  have h1 : HasFDerivAt (fderiv ℝ Γ) (fderiv ℝ (fderiv ℝ Γ) x) x :=
    ((hΓ.fderiv_right (m := ∞) (by simp)).differentiable (by simp) x).hasFDerivAt
  have c : ∀ a : E, HasFDerivAt (fun _ : E => a) (0 : E →L[ℝ] E) x := fun a => hasFDerivAt_const a x
  have d1 : ∀ a b c' : E, HasFDerivAt (fun y => fderiv ℝ Γ y a b c') _ x := fun a b c' =>
    ((h1.clm_apply (c a)).clm_apply (c b)).clm_apply (c c')
  have g1 : ∀ a b : E, HasFDerivAt (fun y => Γ y a b) _ x := fun a b => (h0.clm_apply (c a)).clm_apply (c b)
  have gg : ∀ a b c' : E, HasFDerivAt (fun y => Γ y a (Γ y b c')) _ x := fun a b c' =>
    (h0.clm_apply (c a)).clm_apply (g1 b c')
  refine ⟨_, (((d1 u v w).sub (d1 v u w)).add (gg u v w)).sub (gg v u w), fun e => ?_⟩
  simp [DRmB]
  abel

variable [FiniteDimensional ℝ E]

/-- `lcGam` is symmetric (torsion-free) when the form is. -/
lemma lcGam_symm {B : E → E →L[ℝ] E →L[ℝ] ℝ} (hs : ∀ x u v, B x u v = B x v u) (hB : Differentiable ℝ B)
    (x a b : E) : lcGam B x a b = lcGam B x b a := by
  have hD : ∀ e p q, fderiv ℝ B x e p q = fderiv ℝ B x e q p := fun e p q => by
    rw [fderiv_apply₂' (hB x), fderiv_apply₂' (hB x), show (fun y => B y p q) = fun y => B y q p from
      funext fun y => hs y p q]
  rw [lcGam_apply, lcGam_apply]
  congr 1
  refine ContinuousLinearMap.ext fun v => ?_
  rw [koszK_apply, koszK_apply, hD a b v, hD b a v, hD v a b]
  ring

set_option backward.isDefEq.respectTransparency false in
/-- **Piece A, the second Bianchi identity for THE connection of any smooth metric on `E`.**
1. THE connection's curvature on constant fields is `RmB` of `lcGam` and its derivative.
2. Its derivative is `DRmB`.
3. The cyclic sum of `∇R`, built from these, vanishes. -/
theorem bianchi2_lc {B : E → E →L[ℝ] E →L[ℝ] ℝ} (hs : ∀ x u v, B x u v = B x v u)
    (hn : ∀ x (u : E), (∀ v, B x u v = 0) → u = 0) (hB : ContDiff ℝ ∞ B) (x u v w z : E) :
    (∀ y a b c, curv (lcConn E (ndOf B hs hn (hB.differentiable (by simp)))) (fun _ => a) (fun _ => b) (fun _ => c) y
        = RmB (lcGam B y) (fderiv ℝ (lcGam B) y) a b c) ∧
    (∃ L : E →L[ℝ] E, HasFDerivAt (fun y => RmB (lcGam B y) (fderiv ℝ (lcGam B) y) v w z) L x ∧
        ∀ e, L e = DRmB (lcGam B x) (fderiv ℝ (lcGam B) x) (fderiv ℝ (fderiv ℝ (lcGam B)) x) e v w z) ∧
    nablaRB (lcGam B x) (fderiv ℝ (lcGam B) x) (fderiv ℝ (fderiv ℝ (lcGam B)) x) u v w z
      + nablaRB (lcGam B x) (fderiv ℝ (lcGam B) x) (fderiv ℝ (fderiv ℝ (lcGam B)) x) v w u z
      + nablaRB (lcGam B x) (fderiv ℝ (lcGam B) x) (fderiv ℝ (fderiv ℝ (lcGam B)) x) w u v z = 0 := by
  have hΓ := lcGam_smooth hn hB
  refine ⟨fun y a b c => ?_, hasFDerivAt_RmB hΓ x v w z, ?_⟩
  · rw [curv_model _ _ (fun x w u => lcConn_const hs _ _ x w u) (hΓ.differentiable (by simp))]
    rfl
  · have hsym := (hΓ.contDiffAt (x := x)).isSymmSndFDerivAt (by simp)
    exact bianchi2_alg (fun a b => lcGam_symm hs (hB.differentiable (by simp)) x a b)
      (fun e f a b => by rw [hsym e f]) u v w z

/-! ### Piece B: the metric symmetries of `R`, toward the contraction -/

/-- `♭Γ = K`: `B(Γ(e, a), b) = K(e, a, b)` at every point. -/
lemma flat_lcGam {B : E → E →L[ℝ] E →L[ℝ] ℝ} (hn : ∀ x (u : E), (∀ v, B x u v = 0) → u = 0) (x e a b : E) :
    B x (lcGam B x e a) b = koszK B x e a b := by
  rw [lcGam_apply, (flat_isInvertible B hn x).self_apply_inverse]

/-- **Metric compatibility** at every point: `∂_e B(a, b) = B(Γ(e, a), b) + B(a, Γ(e, b))`. -/
lemma compat_lc {B : E → E →L[ℝ] E →L[ℝ] ℝ} (hs : ∀ x u v, B x u v = B x v u)
    (hn : ∀ x (u : E), (∀ v, B x u v = 0) → u = 0) (hB : Differentiable ℝ B) (x e a b : E) :
    fderiv ℝ B x e a b = B x (lcGam B x e a) b + B x a (lcGam B x e b) := by
  have hD : ∀ e p q, fderiv ℝ B x e p q = fderiv ℝ B x e q p := fun e p q => by
    rw [fderiv_apply₂' (hB x), fderiv_apply₂' (hB x), show (fun y => B y p q) = fun y => B y q p from
      funext fun y => hs y p q]
  rw [hs x a, flat_lcGam hn, flat_lcGam hn, koszK_apply, koszK_apply, hD a b e, hD b e a, hD e b a]
  ring

/-- Compatibility, differentiated once more, through the scalar entries `y ↦ B y a b` (the iterated derivative of
`B` itself sits at a depth `mathlib`'s instance search does not reach). -/
lemma compat_deriv {B : E → E →L[ℝ] E →L[ℝ] ℝ} (hs : ∀ x u v, B x u v = B x v u)
    (hn : ∀ x (u : E), (∀ v, B x u v = 0) → u = 0) (hB : ContDiff ℝ ∞ B) (x u e a b : E) :
    fderiv ℝ (fderiv ℝ (fun y => B y a b)) x u e = fderiv ℝ B x u (lcGam B x e a) b
      + B x (fderiv ℝ (lcGam B) x u e a) b + fderiv ℝ B x u a (lcGam B x e b) + B x a (fderiv ℝ (lcGam B) x u e b) := by
  have hΓ := lcGam_smooth hn hB
  have hBd := hB.differentiable (by simp)
  have hf : ContDiff ℝ ∞ (fun y => B y a b) := (hB.clm_apply contDiff_const).clm_apply contDiff_const
  have c : ∀ p : E, HasFDerivAt (fun _ : E => p) (0 : E →L[ℝ] E) x := fun p => hasFDerivAt_const p x
  have hB0 : HasFDerivAt B (fderiv ℝ B x) x := (hBd x).hasFDerivAt
  have hΓ0 : HasFDerivAt (lcGam B) (fderiv ℝ (lcGam B) x) x := (hΓ.differentiable (by simp) x).hasFDerivAt
  have hR := ((hB0.clm_apply ((hΓ0.clm_apply (c e)).clm_apply (c a))).clm_apply (c b)).add
    ((hB0.clm_apply (c a)).clm_apply ((hΓ0.clm_apply (c e)).clm_apply (c b)))
  have heq : (fun y => fderiv ℝ (fun z => B z a b) y e) = fun y => B y (lcGam B y e a) b + B y a (lcGam B y e b) :=
    funext fun y => by rw [← fderiv_apply₂' (hBd y), compat_lc hs hn hBd y e a b]
  have hd1 : DifferentiableAt ℝ (fderiv ℝ fun y => B y a b) x :=
    (hf.fderiv_right (m := ∞) (by simp)).differentiable (by simp) x
  rw [show fderiv ℝ (fderiv ℝ (fun y => B y a b)) x u e = fderiv ℝ (fun y => fderiv ℝ (fun z => B z a b) y e) x u by
    rw [fderiv_clm_apply hd1 (differentiableAt_const e)]; simp, heq]
  have hR' : HasFDerivAt (fun y => B y (lcGam B y e a) b + B y a (lcGam B y e b)) _ x := hR
  rw [hR'.fderiv]
  simp
  ring

/-- **`R` is antisymmetric for the metric**: `B(R(u,e)a, b) + B(a, R(u,e)b) = 0`. -/
lemma curv_metric_antisymm {B : E → E →L[ℝ] E →L[ℝ] ℝ} (hs : ∀ x u v, B x u v = B x v u)
    (hn : ∀ x (u : E), (∀ v, B x u v = 0) → u = 0) (hB : ContDiff ℝ ∞ B) (x u e a b : E) :
    B x (RmB (lcGam B x) (fderiv ℝ (lcGam B) x) u e a) b + B x a (RmB (lcGam B x) (fderiv ℝ (lcGam B) x) u e b) = 0 := by
  have hBd := hB.differentiable (by simp)
  have hf : ContDiff ℝ ∞ (fun y => B y a b) := (hB.clm_apply contDiff_const).clm_apply contDiff_const
  have h1 := compat_deriv hs hn hB x u e a b
  have h2 := compat_deriv hs hn hB x e u a b
  have hS : fderiv ℝ (fderiv ℝ (fun y => B y a b)) x u e = fderiv ℝ (fderiv ℝ (fun y => B y a b)) x e u :=
    (hf.contDiffAt (x := x)).isSymmSndFDerivAt (by simp) u e
  have c := fun p q r => compat_lc hs hn hBd x p q r
  simp only [RmB, map_add, map_sub, ContinuousLinearMap.add_apply, ContinuousLinearMap.sub_apply]
  rw [c u (lcGam B x e a) b, c u a (lcGam B x e b)] at h1
  rw [c e (lcGam B x u a) b, c e a (lcGam B x u b)] at h2
  linear_combination hS - h1 + h2

omit [FiniteDimensional ℝ E] in
/-- **The first Bianchi identity**, as algebra: `R(u,v)w + R(v,w)u + R(w,u)v = 0` for `Γ` and `DΓ` symmetric. -/
theorem bianchi1_alg {G : E →L[ℝ] E →L[ℝ] E} {D1 : E →L[ℝ] E →L[ℝ] E →L[ℝ] E}
    (hG : ∀ a b, G a b = G b a) (hD1 : ∀ e a b, D1 e a b = D1 e b a) (u v w : E) :
    RmB G D1 u v w + RmB G D1 v w u + RmB G D1 w u v = 0 := by
  simp only [RmB]
  rw [hD1 u v w, hD1 v w u, hD1 w u v, hG u w, hG v u, hG w v]
  abel

omit [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] in
/-- **Pair symmetry** from the two antisymmetries and the first Bianchi identity, as real algebra:
`r(a,b,c,d) = r(c,d,a,b)`. -/
lemma pair_symm_alg (r : E → E → E → E → ℝ) (h12 : ∀ a b c d, r a b c d = -r b a c d)
    (h34 : ∀ a b c d, r a b c d = -r a b d c) (hb : ∀ a b c d, r a b c d + r b c a d + r c a b d = 0)
    (a b c d : E) : r a b c d = r c d a b := by
  linear_combination (1 / 2 : ℝ) * h34 a b c d + (1 / 2 : ℝ) * hb a b c d - (1 / 2 : ℝ) * hb a b d c
    - (1 / 2 : ℝ) * h12 a c b d + (1 / 2 : ℝ) * h34 a c b d - (1 / 2 : ℝ) * hb a c d b + (1 / 2 : ℝ) * h12 a d b c
    - (1 / 2 : ℝ) * h34 a d b c + (1 / 2 : ℝ) * h12 a d c b - (1 / 2 : ℝ) * h34 b c a d + (1 / 2 : ℝ) * hb b c d a
    + (1 / 2 : ℝ) * h34 b d a c - (1 / 2 : ℝ) * h12 b d c a - (1 / 2 : ℝ) * h34 c d a b

omit [FiniteDimensional ℝ E] in
/-- `∇R` is antisymmetric in its first pair. -/
lemma nablaRB_antisymm (G : E →L[ℝ] E →L[ℝ] E) (D1 : E →L[ℝ] E →L[ℝ] E →L[ℝ] E)
    (D2 : E →L[ℝ] E →L[ℝ] E →L[ℝ] E →L[ℝ] E) (e u v w : E) :
    nablaRB G D1 D2 e u v w = -nablaRB G D1 D2 e v u w := by
  simp only [nablaRB, DRmB, RmB, map_add, map_sub, neg_add, neg_sub]
  abel

omit [FiniteDimensional ℝ E] in
/-- **The first Bianchi identity for `∇R`**, as algebra. -/
theorem bianchi1_nabla_alg {G : E →L[ℝ] E →L[ℝ] E} {D1 : E →L[ℝ] E →L[ℝ] E →L[ℝ] E}
    {D2 : E →L[ℝ] E →L[ℝ] E →L[ℝ] E →L[ℝ] E}
    (hG : ∀ a b, G a b = G b a) (hD1 : ∀ e a b, D1 e a b = D1 e b a) (hD2 : ∀ e f a b, D2 e f a b = D2 e f b a)
    (e u v w : E) :
    nablaRB G D1 D2 e u v w + nablaRB G D1 D2 e v w u + nablaRB G D1 D2 e w u v = 0 := by
  have b1 := fun p q r => bianchi1_alg (D1 := D1) hG hD1 p q r
  have hDR : DRmB G D1 D2 e u v w + DRmB G D1 D2 e v w u + DRmB G D1 D2 e w u v = 0 := by
    simp only [DRmB]
    rw [hD2 e u v w, hD2 e v w u, hD2 e w u v, hG w v, hG u w, hG v u, hD1 e w v, hD1 e u w, hD1 e v u]
    abel
  have hG0 : G e (RmB G D1 u v w) + G e (RmB G D1 v w u) + G e (RmB G D1 w u v) = 0 := by
    rw [← map_add, ← map_add, b1, map_zero]
  calc nablaRB G D1 D2 e u v w + nablaRB G D1 D2 e v w u + nablaRB G D1 D2 e w u v
      = (DRmB G D1 D2 e u v w + DRmB G D1 D2 e v w u + DRmB G D1 D2 e w u v)
        + (G e (RmB G D1 u v w) + G e (RmB G D1 v w u) + G e (RmB G D1 w u v))
        - (RmB G D1 (G e u) v w + RmB G D1 v w (G e u) + RmB G D1 w (G e u) v)
        - (RmB G D1 u (G e v) w + RmB G D1 (G e v) w u + RmB G D1 w u (G e v))
        - (RmB G D1 u v (G e w) + RmB G D1 v (G e w) u + RmB G D1 (G e w) u v) := by
        simp only [nablaRB]; abel
    _ = 0 := by rw [hDR, hG0, b1, b1, b1]; simp

/-- **`∇R` is antisymmetric for the metric** in its last pair: `B((∇_e R)(u,v)w, z) + B(w, (∇_e R)(u,v)z) = 0`,
by differentiating `curv_metric_antisymm` and using compatibility. -/
lemma nabla_metric_antisymm {B : E → E →L[ℝ] E →L[ℝ] ℝ} (hs : ∀ x u v, B x u v = B x v u)
    (hn : ∀ x (u : E), (∀ v, B x u v = 0) → u = 0) (hB : ContDiff ℝ ∞ B) (x e u v w z : E) :
    B x (nablaRB (lcGam B x) (fderiv ℝ (lcGam B) x) (fderiv ℝ (fderiv ℝ (lcGam B)) x) e u v w) z
      + B x w (nablaRB (lcGam B x) (fderiv ℝ (lcGam B) x) (fderiv ℝ (fderiv ℝ (lcGam B)) x) e u v z) = 0 := by
  have hΓ := lcGam_smooth hn hB
  have hBd := hB.differentiable (by simp)
  have c : ∀ p : E, HasFDerivAt (fun _ : E => p) (0 : E →L[ℝ] E) x := fun p => hasFDerivAt_const p x
  have hB0 : HasFDerivAt B (fderiv ℝ B x) x := (hBd x).hasFDerivAt
  obtain ⟨Lw, hLw, hLwe⟩ := hasFDerivAt_RmB hΓ x u v w
  obtain ⟨Lz, hLz, hLze⟩ := hasFDerivAt_RmB hΓ x u v z
  have hF := ((hB0.clm_apply hLw).clm_apply (c z)).add ((hB0.clm_apply (c w)).clm_apply hLz)
  have h0 : (fun y => B y (RmB (lcGam B y) (fderiv ℝ (lcGam B) y) u v w) z
      + B y w (RmB (lcGam B y) (fderiv ℝ (lcGam B) y) u v z)) = fun _ => 0 :=
    funext fun y => curv_metric_antisymm hs hn hB y u v w z
  have hF' : HasFDerivAt (fun y => B y (RmB (lcGam B y) (fderiv ℝ (lcGam B) y) u v w) z
      + B y w (RmB (lcGam B y) (fderiv ℝ (lcGam B) y) u v z)) _ x := hF
  rw [h0] at hF'
  have L0 := congrArg (fun T => T e) (hF'.unique (hasFDerivAt_const (0 : ℝ) x))
  simp only [ContinuousLinearMap.add_apply, ContinuousLinearMap.comp_apply, ContinuousLinearMap.flip_apply,
    ContinuousLinearMap.zero_apply, map_zero, ContinuousLinearMap.coe_comp', Function.comp_apply] at L0
  simp at L0
  rw [hLwe, hLze, compat_lc hs hn hBd x e, compat_lc hs hn hBd x e] at L0
  have A := fun p q r t => curv_metric_antisymm hs hn hB x p q r t
  simp only [nablaRB, map_add, map_sub, ContinuousLinearMap.add_apply, ContinuousLinearMap.sub_apply]
  linear_combination L0 - A u v w (lcGam B x e z) - A u v (lcGam B x e w) z - A (lcGam B x e u) v w z
    - A u (lcGam B x e v) w z

/-- Three-fold application under `fderiv`. -/
lemma fderiv_apply₃ {F : Type*} [NormedAddCommGroup F] [NormedSpace ℝ F]
    {Φ : E → (E →L[ℝ] E →L[ℝ] E →L[ℝ] F)} {p : E} (hΦ : DifferentiableAt ℝ Φ p) (e a b c : E) :
    fderiv ℝ Φ p e a b c = fderiv ℝ (fun y => Φ y a b c) p e := by
  rw [fderiv_clm_apply ((hΦ.clm_apply (differentiableAt_const a)).clm_apply (differentiableAt_const b))
    (differentiableAt_const c), fderiv_clm_apply (hΦ.clm_apply (differentiableAt_const a)) (differentiableAt_const b),
    fderiv_clm_apply hΦ (differentiableAt_const a)]
  simp

/-- `DΓ` and `D²Γ` of `lcGam` are symmetric in their last two slots. -/
lemma lcGam_deriv_symm {B : E → E →L[ℝ] E →L[ℝ] ℝ} (hs : ∀ x u v, B x u v = B x v u)
    (hn : ∀ x (u : E), (∀ v, B x u v = 0) → u = 0) (hB : ContDiff ℝ ∞ B) (x : E) :
    (∀ e a b, fderiv ℝ (lcGam B) x e a b = fderiv ℝ (lcGam B) x e b a) ∧
    (∀ e f a b, fderiv ℝ (fderiv ℝ (lcGam B)) x e f a b = fderiv ℝ (fderiv ℝ (lcGam B)) x e f b a) := by
  have hΓ := lcGam_smooth hn hB
  have hBd := hB.differentiable (by simp)
  have h1 : ∀ y e a b, fderiv ℝ (lcGam B) y e a b = fderiv ℝ (lcGam B) y e b a := fun y e a b => by
    rw [fderiv_apply₂' (hΓ.differentiable (by simp) y), fderiv_apply₂' (hΓ.differentiable (by simp) y),
      show (fun z => lcGam B z a b) = fun z => lcGam B z b a from funext fun z => lcGam_symm hs hBd z a b]
  refine ⟨h1 x, fun e f a b => ?_⟩
  have hd : DifferentiableAt ℝ (fderiv ℝ (lcGam B)) x :=
    (hΓ.fderiv_right (m := ∞) (by simp)).differentiable (by simp) x
  rw [fderiv_apply₃ hd, fderiv_apply₃ hd, show (fun y => fderiv ℝ (lcGam B) y f a b) = fun y => fderiv ℝ (lcGam B) y f b a
    from funext fun y => h1 y f a b]

end Bianchi2

/-! ### Piece B, the double contraction on `ℝⁿ` -/

section Contract

set_option synthInstance.maxHeartbeats 4000000

variable {n : ℕ}

/-- Relabelling four summation variables. -/
lemma sum4_swap (f : Fin n → Fin n → Fin n → Fin n → ℝ) :
    ∑ a, ∑ c, ∑ j, ∑ l, f j l c a = ∑ a, ∑ c, ∑ j, ∑ l, f a c j l :=
  calc ∑ a, ∑ c, ∑ j, ∑ l, f j l c a = ∑ a, ∑ j, ∑ c, ∑ l, f j l c a :=
        Finset.sum_congr rfl fun _ _ => Finset.sum_comm
    _ = ∑ j, ∑ a, ∑ c, ∑ l, f j l c a := Finset.sum_comm
    _ = ∑ j, ∑ a, ∑ l, ∑ c, f j l c a :=
        Finset.sum_congr rfl fun _ _ => Finset.sum_congr rfl fun _ _ => Finset.sum_comm
    _ = ∑ j, ∑ l, ∑ a, ∑ c, f j l c a := Finset.sum_congr rfl fun _ _ => Finset.sum_comm
    _ = ∑ j, ∑ l, ∑ c, ∑ a, f j l c a :=
        Finset.sum_congr rfl fun _ _ => Finset.sum_congr rfl fun _ _ => Finset.sum_comm

/-- `(∇_e R)(u, v)w` for THE connection of `B`, at `x`. -/
noncomputable def NB (B : (Fin n → ℝ) → (Fin n → ℝ) →L[ℝ] (Fin n → ℝ) →L[ℝ] ℝ) (x e u v w : Fin n → ℝ) : Fin n → ℝ :=
  nablaRB (lcGam B x) (fderiv ℝ (lcGam B) x) (fderiv ℝ (fderiv ℝ (lcGam B)) x) e u v w

/-- `(∇_e Ric)(b, c) = tr(u ↦ (∇_e R)(u, b)c)`. -/
noncomputable def nRic (B : (Fin n → ℝ) → (Fin n → ℝ) →L[ℝ] (Fin n → ℝ) →L[ℝ] ℝ) (x e b c : Fin n → ℝ) : ℝ :=
  ∑ j, NB B x e (Pi.single j 1) b c j

/-- **Row 6, the contracted Bianchi identity**, `∇^a R_ab = ½ ∇_b R`, i.e. `∇^a G_ab = 0`: for THE connection of
any smooth, symmetric, nondegenerate metric on `ℝⁿ`, with the inverse `gi` given at the point. -/
theorem contracted_bianchi {B : (Fin n → ℝ) → (Fin n → ℝ) →L[ℝ] (Fin n → ℝ) →L[ℝ] ℝ}
    (hs : ∀ x u v, B x u v = B x v u) (hn : ∀ x (u : Fin n → ℝ), (∀ v, B x u v = 0) → u = 0) (hB : ContDiff ℝ ∞ B)
    (x : Fin n → ℝ) {gi : Fin n → Fin n → ℝ}
    (hinv : ∀ m k, ∑ l, B x (Pi.single m 1) (Pi.single l 1) * gi l k = if m = k then 1 else 0)
    (hgi : ∀ a c, gi a c = gi c a) (w : Fin n → ℝ) :
    ∑ a, ∑ c, gi a c * nRic B x (Pi.single a 1) (Pi.single c 1) w
      = (1 / 2) * ∑ a, ∑ c, gi a c * nRic B x w (Pi.single a 1) (Pi.single c 1) := by
  set e : Fin n → Fin n → ℝ := fun j => Pi.single j 1 with he
  set nn : (Fin n → ℝ) → (Fin n → ℝ) → (Fin n → ℝ) → (Fin n → ℝ) → (Fin n → ℝ) → ℝ :=
    fun p u v q z => B x (NB B x p u v q) z with hnn
  -- components through the metric
  have comp : ∀ (X : Fin n → ℝ) k, X k = ∑ l, B x X (e l) * gi l k := fun X k => by
    have hX : ∀ l, B x X (e l) = ∑ m, X m * B x (e m) (e l) := fun l => by
      conv_lhs => rw [← Finset.univ_sum_single X]
      simp only [map_sum, ContinuousLinearMap.coe_sum', Finset.sum_apply]
      refine Finset.sum_congr rfl fun m _ => ?_
      rw [show (Pi.single m (X m) : Fin n → ℝ) = X m • e m by ext i; simp [he, Pi.single_apply], map_smul]
      rfl
    simp only [hX, Finset.sum_mul]
    rw [Finset.sum_comm]
    have hinv' : ∀ m k, ∑ l, B x (e m) (e l) * gi l k = if m = k then 1 else 0 := hinv
    simp only [mul_assoc, ← Finset.mul_sum, hinv']
    simp
  have hR : ∀ p b c, nRic B x p b c = ∑ j, ∑ l, nn p (e j) b c (e l) * gi l j := fun p b c => by
    simp only [nRic, hnn]; exact Finset.sum_congr rfl fun j _ => comp _ j
  -- the symmetries of `∇R`
  have hΓs := fun a b => lcGam_symm hs (hB.differentiable (by simp)) x a b
  obtain ⟨hD1, hD2⟩ := lcGam_deriv_symm hs hn hB x
  have S1 : ∀ p u v q z, nn p u v q z = -nn p v u q z := fun p u v q z => by
    simp only [hnn, NB]; rw [nablaRB_antisymm, map_neg, ContinuousLinearMap.neg_apply]
  have S2 : ∀ p u v q z, nn p u v q z = -nn p u v z q := fun p u v q z => by
    have := nabla_metric_antisymm hs hn hB x p u v q z
    simp only [hnn, NB]; rw [hs x q] at this; linarith
  have S3 : ∀ p u v q z, nn p u v q z + nn p v q u z + nn p q u v z = 0 := fun p u v q z => by
    simp only [hnn, NB, ← ContinuousLinearMap.add_apply, ← map_add,
      bianchi1_nabla_alg hΓs hD1 hD2 p u v q, map_zero, ContinuousLinearMap.zero_apply]
  have S4 : ∀ p u v q z, nn p u v q z = nn p q z u v := fun p =>
    pair_symm_alg (nn p) (fun u v q z => S1 p u v q z) (fun u v q z => S2 p u v q z) (fun u v q z => S3 p u v q z)
  have S5 : ∀ p u v q z, nn p u v q z + nn u v p q z + nn v p u q z = 0 := fun p u v q z => by
    have hsym := (lcGam_smooth hn hB).contDiffAt (x := x) |>.isSymmSndFDerivAt (by simp)
    simp only [hnn, NB, ← ContinuousLinearMap.add_apply, ← map_add,
      bianchi2_alg (D1 := fderiv ℝ (lcGam B) x) hΓs (fun e f a b => by rw [hsym e f]) p u v q, map_zero,
      ContinuousLinearMap.zero_apply]
  -- the computation
  set L := ∑ a, ∑ c, ∑ j, ∑ l, gi a c * gi l j * nn (e a) (e j) (e c) w (e l) with hL
  have hlhs : ∑ a, ∑ c, gi a c * nRic B x (e a) (e c) w = L := by
    simp only [hR, Finset.mul_sum, hL]
    exact Finset.sum_congr rfl fun _ _ => Finset.sum_congr rfl fun _ _ => Finset.sum_congr rfl fun _ _ =>
      Finset.sum_congr rfl fun _ _ => by ring
  have T1 : ∑ a, ∑ c, ∑ j, ∑ l, gi a c * gi l j * nn (e j) (e a) w (e c) (e l) = -L := by
    have : ∀ a c j l, gi a c * gi l j * nn (e j) (e a) w (e c) (e l)
        = -(gi j l * gi a c * nn (e j) (e c) (e l) w (e a)) := fun a c j l => by
      rw [S1, S4 (e j) w (e a), hgi l j]; ring
    simp only [this, Finset.sum_neg_distrib]
    rw [sum4_swap (fun A C J L' => gi A C * gi L' J * nn (e A) (e J) (e C) w (e L'))]
  have T2 : ∑ a, ∑ c, ∑ j, ∑ l, gi a c * gi l j * nn (e a) w (e j) (e c) (e l) = -L := by
    have : ∀ a c j l, gi a c * gi l j * nn (e a) w (e j) (e c) (e l)
        = -(gi a c * gi j l * nn (e a) (e l) (e c) w (e j)) := fun a c j l => by
      rw [S4 (e a) w (e j), S1 (e a) (e c), hgi l j]; ring
    simp only [this, Finset.sum_neg_distrib, hL]
    congr 1
    exact Finset.sum_congr rfl fun _ _ => Finset.sum_congr rfl fun _ _ => Finset.sum_comm
  have hrhs : ∑ a, ∑ c, gi a c * nRic B x w (e a) (e c)
      = -(∑ a, ∑ c, ∑ j, ∑ l, gi a c * gi l j * nn (e j) (e a) w (e c) (e l))
        - ∑ a, ∑ c, ∑ j, ∑ l, gi a c * gi l j * nn (e a) w (e j) (e c) (e l) := by
    simp only [hR, Finset.mul_sum, ← Finset.sum_neg_distrib, ← Finset.sum_sub_distrib]
    exact Finset.sum_congr rfl fun a _ => Finset.sum_congr rfl fun c _ => Finset.sum_congr rfl fun j _ =>
      Finset.sum_congr rfl fun l _ => by
        have := S5 w (e j) (e a) (e c) (e l); linear_combination (gi a c * gi l j) * this
  rw [hlhs, hrhs, T1, T2]; ring

/-- The Ricci form of THE connection at `y`: `Ric(b, c) = tr(u ↦ R(u, b)c)`. -/
noncomputable def RicY (B : (Fin n → ℝ) → (Fin n → ℝ) →L[ℝ] (Fin n → ℝ) →L[ℝ] ℝ) (y b c : Fin n → ℝ) : ℝ :=
  ∑ j, RmB (lcGam B y) (fderiv ℝ (lcGam B) y) (Pi.single j 1) b c j

lemma RmB_first_lin (G : (Fin n → ℝ) →L[ℝ] (Fin n → ℝ) →L[ℝ] (Fin n → ℝ))
    (D1 : (Fin n → ℝ) →L[ℝ] (Fin n → ℝ) →L[ℝ] (Fin n → ℝ) →L[ℝ] (Fin n → ℝ)) (X v w : Fin n → ℝ) :
    RmB G D1 X v w = ∑ k, X k • RmB G D1 (Pi.single k 1) v w := by
  have hX : X = ∑ k, X k • (Pi.single k 1 : Fin n → ℝ) := by ext i; simp [Pi.single_apply]
  conv_lhs => rw [hX]
  simp only [RmB, map_sum, map_smul, ContinuousLinearMap.coe_sum', ContinuousLinearMap.coe_smul', Finset.sum_apply,
    Pi.smul_apply, smul_sub, smul_add, Finset.sum_sub_distrib, Finset.sum_add_distrib]

/-- **`nRic` is the covariant derivative of the Ricci form**:
`(∇_e Ric)(b, c) = ∂_e Ric(b, c) − Ric(Γ(e, b), c) − Ric(b, Γ(e, c))`. -/
lemma nRic_eq {B : (Fin n → ℝ) → (Fin n → ℝ) →L[ℝ] (Fin n → ℝ) →L[ℝ] ℝ}
    (hn : ∀ x (u : Fin n → ℝ), (∀ v, B x u v = 0) → u = 0) (hB : ContDiff ℝ ∞ B) (x e b c : Fin n → ℝ) :
    nRic B x e b c = fderiv ℝ (fun y => RicY B y b c) x e - RicY B x (lcGam B x e b) c
      - RicY B x b (lcGam B x e c) := by
  have hΓ := lcGam_smooth hn hB
  choose L hL hLe using fun j : Fin n => hasFDerivAt_RmB hΓ x (Pi.single j 1) b c
  have hd : HasFDerivAt (fun y => RicY B y b c) (∑ j, (ContinuousLinearMap.proj j).comp (L j)) x :=
    HasFDerivAt.fun_sum fun j _ => (ContinuousLinearMap.proj (R := ℝ) (φ := fun _ : Fin n => ℝ) j).hasFDerivAt.comp x (hL j)
  rw [hd.fderiv]
  set G := lcGam B x; set D1 := fderiv ℝ (lcGam B) x
  -- the trace of a commutator vanishes
  have tr : ∑ j, G e (RmB G D1 (Pi.single j 1) b c) j = ∑ j, RmB G D1 (G e (Pi.single j 1)) b c j := by
    simp only [RmB_first_lin G D1 (G e (Pi.single _ 1)), Finset.sum_apply, Pi.smul_apply, smul_eq_mul]
    have hG : ∀ (X : Fin n → ℝ) j, G e X j = ∑ k, X k * G e (Pi.single k 1) j := fun X j => by
      conv_lhs => rw [show X = ∑ k, X k • (Pi.single k 1 : Fin n → ℝ) by ext i; simp [Pi.single_apply]]
      simp [map_sum, map_smul]
    simp only [hG (RmB G D1 _ b c)]
    rw [Finset.sum_comm]
    exact Finset.sum_congr rfl fun _ _ => Finset.sum_congr rfl fun _ _ => by ring
  simp only [nRic, NB, nablaRB, RicY, ContinuousLinearMap.coe_sum', ContinuousLinearMap.coe_comp', Finset.sum_apply,
    Function.comp_apply, ContinuousLinearMap.proj_apply, hLe, Pi.add_apply, Pi.sub_apply, Finset.sum_add_distrib,
    Finset.sum_sub_distrib]
  rw [tr]; ring

end Contract

end ShadowProbe

#print axioms ShadowProbe.bianchi2_alg
#print axioms ShadowProbe.bianchi2_lc
#print axioms ShadowProbe.compat_lc
#print axioms ShadowProbe.curv_metric_antisymm
#print axioms ShadowProbe.bianchi1_alg
#print axioms ShadowProbe.pair_symm_alg
#print axioms ShadowProbe.nabla_metric_antisymm
#print axioms ShadowProbe.contracted_bianchi
#print axioms ShadowProbe.nRic_eq

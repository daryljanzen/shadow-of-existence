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

end Bianchi2

end ShadowProbe

#print axioms ShadowProbe.bianchi2_alg
#print axioms ShadowProbe.bianchi2_lc
#print axioms ShadowProbe.compat_lc
#print axioms ShadowProbe.curv_metric_antisymm
#print axioms ShadowProbe.bianchi1_alg
#print axioms ShadowProbe.pair_symm_alg

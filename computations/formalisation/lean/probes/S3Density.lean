import Mathlib

/-!
# Campaign 54 / programme stage P3: polynomial (tensor) fields are dense on `S³`

* `polyS`: restrictions to `S³ ⊂ ℝ⁴` of real polynomials in `x₀..x₃`, a subalgebra of `C(S³, ℝ)`
  (the range of `aeval coord`). It separates points; by Stone–Weierstrass it is dense in sup norm.
* For **every** finite Borel measure `μ` on `S³` (in particular `σ = volume.toSphere`) its image in `L²(μ)`
  is dense.
* Componentwise: tuples `Fin n → _`, 2-tensors `Fin 3 → Fin 3 → _`, and symmetric traceless 2-tensors
  (polynomial sym. traceless tensors are dense in the sym. traceless tensors), in `C` and in `L²`.
* Frame remark: the left-invariant frame `E_a(q) = q·u_a` is linear in `q`, so the frame components of an
  ambient polynomial 2-tensor field are polynomial.
-/

namespace ShadowProbe.S3Density

open MvPolynomial MeasureTheory Metric

/-- `ℝ⁴`. -/
abbrev E4 := EuclideanSpace ℝ (Fin 4)
/-- The unit sphere `S³ ⊂ ℝ⁴`. -/
abbrev S3 := sphere (0 : E4) 1

/-! ## 1. The polynomial subalgebra and Stone–Weierstrass -/

/-- The coordinate functions `x_i` restricted to `S³`. -/
def coord (i : Fin 4) : C(S3, ℝ) :=
  ⟨fun x => (x : E4) i, (continuous_apply i).comp (PiLp.continuous_ofLp 2 _ |>.comp continuous_subtype_val)⟩

@[simp] theorem coord_apply (i : Fin 4) (x : S3) : coord i x = (x : E4) i := rfl

/-- Restriction to `S³` of a real polynomial, as an algebra map. -/
noncomputable def evalS : MvPolynomial (Fin 4) ℝ →ₐ[ℝ] C(S3, ℝ) := aeval coord

theorem evalS_apply (p : MvPolynomial (Fin 4) ℝ) (x : S3) :
    evalS p x = eval (fun i => (x : E4) i) p := by
  have := congrArg (fun φ : MvPolynomial (Fin 4) ℝ →ₐ[ℝ] ℝ => φ p)
    (MvPolynomial.comp_aeval (R := ℝ) coord (ContinuousMap.evalAlgHom ℝ ℝ x))
  simpa [evalS, MvPolynomial.aeval_eq_eval, MvPolynomial.coe_aeval_eq_eval] using this

/-- **The polynomial functions on `S³`.** -/
noncomputable def polyS : Subalgebra ℝ C(S3, ℝ) := evalS.range

theorem evalS_mem (p : MvPolynomial (Fin 4) ℝ) : evalS p ∈ polyS := ⟨p, rfl⟩

theorem coord_mem (i : Fin 4) : coord i ∈ polyS := ⟨X i, by simp [evalS]⟩

theorem const_mem (c : ℝ) : ContinuousMap.const S3 c ∈ polyS := by
  have h := polyS.algebraMap_mem c
  convert h using 1
  all_goals (ext; simp [Algebra.algebraMap_eq_smul_one])

theorem polyS_separatesPoints : polyS.SeparatesPoints := by
  intro x y hxy
  have : (x : E4) ≠ (y : E4) := fun h => hxy (Subtype.ext h)
  obtain ⟨i, hi⟩ : ∃ i, (x : E4) i ≠ (y : E4) i := by
    by_contra h; push Not at h; exact this (PiLp.ext h)
  exact ⟨coord i, ⟨coord i, coord_mem i, rfl⟩, by simpa using hi⟩

/-- **Stone–Weierstrass on `S³`.** -/
theorem polyS_closure_eq_top : polyS.topologicalClosure = ⊤ :=
  ContinuousMap.subalgebra_topologicalClosure_eq_top_of_separatesPoints polyS polyS_separatesPoints

theorem polyS_dense : Dense (polyS : Set C(S3, ℝ)) := by
  rw [dense_iff_closure_eq, ← Subalgebra.topologicalClosure_coe, polyS_closure_eq_top]; rfl

/-- **Headline C.** Every continuous function on `S³` is a uniform limit of polynomials. -/
theorem exists_poly_near (f : C(S3, ℝ)) {ε : ℝ} (hε : 0 < ε) :
    ∃ p : MvPolynomial (Fin 4) ℝ, ‖evalS p - f‖ < ε := by
  obtain ⟨g, hg, ⟨p, rfl⟩⟩ := Metric.dense_iff.mp polyS_dense f ε hε
  exact ⟨p, by rw [← dist_eq_norm]; exact Metric.mem_ball.mp hg⟩

#print axioms polyS_closure_eq_top
#print axioms exists_poly_near

/-! ## 2. Density in `L²(μ)` for every finite Borel measure; the sphere measure `σ` -/

/-- The sphere measure. -/
noncomputable abbrev σ : Measure S3 := (volume : Measure E4).toSphere

example : IsFiniteMeasure σ := inferInstance

/-- The polynomials, as a subspace of `L²(μ)`. -/
noncomputable def polyL2 (μ : Measure S3) [IsFiniteMeasure μ] : Submodule ℝ (Lp ℝ 2 μ) :=
  (Subalgebra.toSubmodule polyS).map (ContinuousMap.toLp (E := ℝ) 2 μ ℝ).toLinearMap

theorem mem_polyL2 (μ : Measure S3) [IsFiniteMeasure μ] (p : MvPolynomial (Fin 4) ℝ) :
    ContinuousMap.toLp (E := ℝ) 2 μ ℝ (evalS p) ∈ polyL2 μ :=
  ⟨evalS p, evalS_mem p, rfl⟩

theorem polyL2_dense (μ : Measure S3) [IsFiniteMeasure μ] : Dense (polyL2 μ : Set (Lp ℝ 2 μ)) := by
  have hd := ContinuousMap.toLp_denseRange (α := S3) (E := ℝ) (p := 2) (μ := μ) ℝ (by norm_num)
  have := hd.dense_image (ContinuousMap.toLp (E := ℝ) 2 μ ℝ).continuous polyS_dense
  simpa [polyL2] using this

/-- **Headline L².** For any finite Borel measure on `S³`, every `L²` function is an `L²` limit of
polynomials. -/
theorem exists_poly_near_L2 (μ : Measure S3) [IsFiniteMeasure μ] (f : Lp ℝ 2 μ) {ε : ℝ} (hε : 0 < ε) :
    ∃ p : MvPolynomial (Fin 4) ℝ, ‖ContinuousMap.toLp (E := ℝ) 2 μ ℝ (evalS p) - f‖ < ε := by
  obtain ⟨g, hg, ⟨q, hq, rfl⟩⟩ := Metric.dense_iff.mp (polyL2_dense μ) f ε hε
  obtain ⟨p, rfl⟩ := hq
  exact ⟨p, by rw [← dist_eq_norm]; exact Metric.mem_ball.mp hg⟩

/-- The same for the sphere measure `σ`. -/
theorem exists_poly_near_L2_σ (f : Lp ℝ 2 σ) {ε : ℝ} (hε : 0 < ε) :
    ∃ p : MvPolynomial (Fin 4) ℝ, ‖ContinuousMap.toLp (E := ℝ) 2 σ ℝ (evalS p) - f‖ < ε :=
  exists_poly_near_L2 σ f hε

#print axioms polyL2_dense
#print axioms exists_poly_near_L2
#print axioms exists_poly_near_L2_σ

/-! ## 3. Componentwise: tuples and 2-tensors -/

section Generic
variable {V : Type*} [TopologicalSpace V]

theorem dense_tuple {s : Set V} (hs : Dense s) (n : ℕ) :
    Dense {F : Fin n → V | ∀ i, F i ∈ s} := by
  have := dense_pi (I := Set.univ) (s := fun _ : Fin n => s) (fun i _ => hs)
  simpa [Set.pi, Set.mem_univ] using this

theorem dense_tensor {s : Set V} (hs : Dense s) :
    Dense {T : Fin 3 → Fin 3 → V | ∀ b c, T b c ∈ s} := by
  have h1 : Dense {F : Fin 3 → V | ∀ i, F i ∈ s} := dense_tuple hs 3
  have := dense_tuple h1 3
  simpa using this

end Generic

/-- **Headline tuples, C.** -/
theorem tuple_dense_C (n : ℕ) : Dense {F : Fin n → C(S3, ℝ) | ∀ i, F i ∈ polyS} :=
  dense_tuple polyS_dense n

/-- **Headline tuples, L².** -/
theorem tuple_dense_L2 (μ : Measure S3) [IsFiniteMeasure μ] (n : ℕ) :
    Dense {F : Fin n → Lp ℝ 2 μ | ∀ i, F i ∈ polyL2 μ} :=
  dense_tuple (polyL2_dense μ) n

theorem tensor_dense_C : Dense {T : Fin 3 → Fin 3 → C(S3, ℝ) | ∀ b c, T b c ∈ polyS} :=
  dense_tensor polyS_dense

theorem tensor_dense_L2 (μ : Measure S3) [IsFiniteMeasure μ] :
    Dense {T : Fin 3 → Fin 3 → Lp ℝ 2 μ | ∀ b c, T b c ∈ polyL2 μ} :=
  dense_tensor (polyL2_dense μ)

#print axioms tuple_dense_C
#print axioms tuple_dense_L2
#print axioms tensor_dense_C
#print axioms tensor_dense_L2

/-! ## 4. Symmetric traceless tensors: the projection preserves polynomials -/

section SymTL
variable {V : Type*} [AddCommGroup V] [Module ℝ V]

/-- Symmetric and traceless. -/
def IsSymTL (h : Fin 3 → Fin 3 → V) : Prop := (∀ b c, h b c = h c b) ∧ ∑ a, h a a = 0

/-- The symmetric traceless projection `h ↦ sym h − (tr h / 3) δ`. -/
noncomputable def projTL (h : Fin 3 → Fin 3 → V) : Fin 3 → Fin 3 → V := fun b c =>
  (1 / 2 : ℝ) • (h b c + h c b) - (if b = c then (1 : ℝ) else 0) • ((1 / 3 : ℝ) • ∑ a, h a a)

theorem projTL_isSymTL (h : Fin 3 → Fin 3 → V) : IsSymTL (projTL h) := by
  refine ⟨fun b c => ?_, ?_⟩
  · simp only [projTL, add_comm (h b c), eq_comm (a := b)]
  · simp only [projTL, Fin.sum_univ_three, ite_true]
    module

theorem projTL_of_isSymTL {h : Fin 3 → Fin 3 → V} (hh : IsSymTL h) : projTL h = h := by
  funext b c
  simp only [projTL, hh.2, smul_zero, sub_zero, ← hh.1 b c]
  module

/-- The projection maps tensors with components in a subspace `S` to such tensors (each component is a
linear combination of components): for `S = polyS`, the traceless projection of a polynomial tensor is
polynomial. -/
theorem projTL_mem (S : Submodule ℝ V) {h : Fin 3 → Fin 3 → V} (hS : ∀ b c, h b c ∈ S) (b c : Fin 3) :
    projTL h b c ∈ S :=
  S.sub_mem (S.smul_mem _ (S.add_mem (hS b c) (hS c b)))
    (S.smul_mem _ (S.smul_mem _ (S.sum_mem fun a _ => hS a a)))

variable [TopologicalSpace V] [IsTopologicalAddGroup V] [ContinuousSMul ℝ V]

theorem continuous_projTL : Continuous (projTL : (Fin 3 → Fin 3 → V) → Fin 3 → Fin 3 → V) := by
  have hc : ∀ b c, Continuous fun h : Fin 3 → Fin 3 → V => h b c := fun b c =>
    (continuous_apply c).comp (continuous_apply b)
  refine continuous_pi fun b => continuous_pi fun c => ?_
  exact ((hc b c).add (hc c b)).const_smul _ |>.sub
    ((continuous_finsetSum _ fun a _ => hc a a).const_smul _ |>.const_smul _)

/-- **Generic sym. traceless density.** If `S` is dense in `V`, every symmetric traceless tensor is a limit
of symmetric traceless tensors with components in `S`. -/
theorem symTL_mem_closure (S : Submodule ℝ V) (hS : Dense (S : Set V))
    {h : Fin 3 → Fin 3 → V} (hh : IsSymTL h) :
    h ∈ closure {p : Fin 3 → Fin 3 → V | (∀ b c, p b c ∈ S) ∧ IsSymTL p} := by
  have hd := dense_tensor (V := V) hS
  have h1 : h ∈ projTL '' closure {T : Fin 3 → Fin 3 → V | ∀ b c, T b c ∈ (S : Set V)} :=
    ⟨h, hd.closure_eq ▸ Set.mem_univ _, projTL_of_isSymTL hh⟩
  refine closure_mono ?_ (image_closure_subset_closure_image continuous_projTL h1)
  rintro _ ⟨T, hT, rfl⟩
  exact ⟨projTL_mem S hT, projTL_isSymTL T⟩

end SymTL

/-- **Headline sym. traceless, C.** -/
theorem symTL_dense_C {h : Fin 3 → Fin 3 → C(S3, ℝ)} (hh : IsSymTL h) :
    h ∈ closure {p | (∀ b c, p b c ∈ polyS) ∧ IsSymTL p} :=
  symTL_mem_closure (Subalgebra.toSubmodule polyS) polyS_dense hh

/-- **Headline sym. traceless, L².** -/
theorem symTL_dense_L2 (μ : Measure S3) [IsFiniteMeasure μ] {h : Fin 3 → Fin 3 → Lp ℝ 2 μ}
    (hh : IsSymTL h) : h ∈ closure {p | (∀ b c, p b c ∈ polyL2 μ) ∧ IsSymTL p} :=
  symTL_mem_closure (polyL2 μ) (polyL2_dense μ) hh

#print axioms symTL_dense_C
#print axioms symTL_dense_L2

/-! ## 5. The frame remark

Conventions of `probes/S3TTSpectrum.lean` (`dval`, `dR`): `E_a(q) = q·u_a`, `u = (i, j, k)`, linear in `q`. -/

/-- The frame vectors as linear real polynomials (`dval` of `S3TTSpectrum`, over `ℝ`). -/
noncomputable def dpoly : Fin 3 → Fin 4 → MvPolynomial (Fin 4) ℝ
  | 0 => ![-X 1, X 0, X 3, -X 2]
  | 1 => ![-X 2, -X 3, X 0, X 1]
  | 2 => ![-X 3, X 2, -X 1, X 0]

/-- The frame vector fields on `ℝ⁴` (`dR` of `S3TTSpectrum`). -/
def dR : Fin 3 → (Fin 4 → ℝ) → Fin 4 → ℝ
  | 0 => fun x => ![-x 1, x 0, x 3, -x 2]
  | 1 => fun x => ![-x 2, -x 3, x 0, x 1]
  | 2 => fun x => ![-x 3, x 2, -x 1, x 0]

/-- The frame components, as continuous functions on `S³`. -/
noncomputable def frameS (a : Fin 3) (i : Fin 4) : C(S3, ℝ) := evalS (dpoly a i)

theorem frameS_apply (a : Fin 3) (i : Fin 4) (x : S3) :
    frameS a i x = dR a (fun j => (x : E4) j) i := by
  rw [frameS, evalS_apply]
  fin_cases a <;> fin_cases i <;> simp [dpoly, dR]

/-- Frame components `h_ab = Σ_ij E_a^i E_b^j H_ij` of an ambient 2-tensor field `H` on `S³`. -/
noncomputable def frameComp (H : Fin 4 → Fin 4 → C(S3, ℝ)) (a b : Fin 3) : C(S3, ℝ) :=
  ∑ i, ∑ j, frameS a i * frameS b j * H i j

theorem frameComp_apply (H : Fin 4 → Fin 4 → C(S3, ℝ)) (a b : Fin 3) (x : S3) :
    frameComp H a b x = ∑ i, ∑ j, dR a (fun k => (x : E4) k) i * dR b (fun k => (x : E4) k) j * H i j x := by
  simp [frameComp, frameS_apply, ContinuousMap.sum_apply]

/-- **Frame remark.** The frame components of a polynomial ambient tensor field are polynomial. -/
theorem frameComp_mem {H : Fin 4 → Fin 4 → C(S3, ℝ)} (hH : ∀ i j, H i j ∈ polyS) (a b : Fin 3) :
    frameComp H a b ∈ polyS :=
  polyS.sum_mem fun i _ => polyS.sum_mem fun j _ =>
    polyS.mul_mem (polyS.mul_mem (evalS_mem _) (evalS_mem _)) (hH i j)

/-- And the traceless projection of the frame components is polynomial too. -/
theorem projTL_frameComp_mem {H : Fin 4 → Fin 4 → C(S3, ℝ)} (hH : ∀ i j, H i j ∈ polyS) (a b : Fin 3) :
    projTL (frameComp H) a b ∈ polyS :=
  projTL_mem (Subalgebra.toSubmodule polyS) (frameComp_mem hH) a b

#print axioms frameS_apply
#print axioms frameComp_mem
#print axioms projTL_frameComp_mem

end ShadowProbe.S3Density

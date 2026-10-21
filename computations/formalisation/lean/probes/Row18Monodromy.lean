import Mathlib.Analysis.Complex.Polynomial.Basic
import Mathlib.Analysis.Calculus.InverseFunctionTheorem.FDeriv
import Mathlib.Analysis.Calculus.Deriv.Pow
import Mathlib.Analysis.SpecialFunctions.Complex.Circle
import Mathlib.Algebra.Polynomial.SpecificDegree
import Mathlib.RingTheory.Polynomial.RationalRoot
import Mathlib.Topology.Algebra.Polynomial
import Mathlib.Topology.Homotopy.Lifting
import Mathlib.Tactic

open Polynomial

namespace ShadowProbe.Row18Monodromy

attribute [local instance] Polynomial.Gal.splits_ℚ_ℂ

/-! ## Route A: the Galois group of the `E = 0`, `M = 1` member `X³ − X + 2` is `S₃`. -/

/-- The family cubic `r³ + (E² − 1) r + 2M` at the rational specialisation `E = 0`, `M = 1`. -/
noncomputable def cubicQ : ℚ[X] := X ^ 3 - X + C 2

lemma cubicQ_natDegree : cubicQ.natDegree = 3 := by
  unfold cubicQ; compute_degree!

lemma cubicQ_ne_zero : cubicQ ≠ 0 := by
  intro h; have := cubicQ_natDegree; rw [h] at this; simp at this

lemma cubicQ_aeval {K : Type*} [Field K] [Algebra ℚ K] (x : K) :
    aeval x cubicQ = x ^ 3 - x + 2 := by
  simp [cubicQ]

/-- No rational root (rational root theorem: a root of the monic integer cubic is an integer). -/
lemma cubicQ_no_root (x : ℚ) : ¬ IsRoot cubicQ x := by
  intro hx
  have hx' : x ^ 3 - x + 2 = 0 := by
    have : eval x cubicQ = x ^ 3 - x + 2 := by simp [cubicQ]
    rw [← this]; exact hx
  let pZ : ℤ[X] := X ^ 3 - X + C 2
  have hmon : pZ.Monic := by unfold pZ; monicity!
  have hr : aeval x pZ = 0 := by
    simp only [pZ, map_add, map_sub, map_pow, aeval_X, map_ofNat]
    exact hx'
  obtain ⟨n, hn⟩ := isInteger_of_is_root_of_monic hmon hr
  have hn' : ((n : ℚ)) ^ 3 - n + 2 = 0 := by rw [← hn] at hx'; simpa using hx'
  have hz : n ^ 3 - n + 2 = 0 := by exact_mod_cast hn'
  have h1 : n ≤ 1 := by nlinarith [sq_nonneg (n - 1), sq_nonneg (n + 1)]
  have h2 : -2 ≤ n := by nlinarith [sq_nonneg (n - 1), sq_nonneg (n + 1)]
  interval_cases n <;> omega

theorem cubicQ_irreducible : Irreducible cubicQ :=
  irreducible_of_degree_le_three_of_not_isRoot (by rw [cubicQ_natDegree]; decide) cubicQ_no_root

/-- The discriminant `−4p³ − 27q²` at `p = −1`, `q = 2` is `−104 = 4((1 − 0²)³ − 27·1²)`: not a square in `ℚ`. -/
theorem cubicQ_disc_not_square :
    (-4 * (-1 : ℚ) ^ 3 - 27 * 2 ^ 2 = 4 * ((1 - 0 ^ 2) ^ 3 - 27 * 1 ^ 2)) ∧
      (-4 * (-1 : ℚ) ^ 3 - 27 * 2 ^ 2 = -104) ∧ ¬ ∃ d : ℚ, d ^ 2 = -104 := by
  refine ⟨by norm_num, by norm_num, ?_⟩
  rintro ⟨d, hd⟩; nlinarith [sq_nonneg d]

lemma cubicQ_card_complex : Fintype.card (cubicQ.rootSet ℂ) = 3 := by
  rw [← cubicQ_natDegree]
  simp_rw [rootSet_def, Finset.coe_sort_coe, Fintype.card_coe]
  rw [Multiset.toFinset_card_of_nodup, ← Splits.natDegree_eq_card_roots, natDegree_map]
  · exact IsAlgClosed.splits _
  · exact nodup_roots ((separable_map (algebraMap ℚ ℂ)).mpr cubicQ_irreducible.separable)

/-- At most one real root: a real root has `r < −1`, and two such cannot both satisfy `a² + ab + b² = 1`. -/
lemma cubicQ_card_real : Fintype.card (cubicQ.rootSet ℝ) ≤ 1 := by
  rw [Fintype.card_le_one_iff_subsingleton]
  constructor
  rintro ⟨a, ha⟩ ⟨b, hb⟩
  rw [mem_rootSet, cubicQ_aeval] at ha hb
  have ha' := ha.2; have hb' := hb.2
  have hneg : ∀ r : ℝ, r ^ 3 - r + 2 = 0 → r < -1 := by
    intro r hr
    by_contra hc; push Not at hc
    nlinarith [sq_nonneg (r - 1), sq_nonneg (r + 1), sq_nonneg r, mul_self_nonneg (r - 1 / 2)]
  have ha1 := hneg a ha'; have hb1 := hneg b hb'
  apply Subtype.ext
  by_contra hne
  have hsub : (a - b) * (a ^ 2 + a * b + b ^ 2 - 1) = 0 := by linear_combination ha' - hb'
  rcases mul_eq_zero.1 hsub with h | h
  · exact hne (by linarith)
  · nlinarith [mul_pos (neg_pos.2 (by linarith : a + 1 < 0)) (neg_pos.2 (by linarith : b + 1 < 0))]

/-- **Route A headline.** The Galois group of `X³ − X + 2` over `ℚ` acts as the full symmetric group on its
three complex roots: `galActionHom` is bijective, so `Gal ≃* S₃` and `|Gal| = 6`. -/
theorem cubicQ_gal_full :
    Function.Bijective (Gal.galActionHom cubicQ ℂ) ∧ Nat.card cubicQ.Gal = 6 := by
  have hb : Function.Bijective (Gal.galActionHom cubicQ ℂ) :=
    Gal.galActionHom_bijective_of_prime_degree' cubicQ_irreducible
      (by rw [cubicQ_natDegree]; norm_num)
      (by rw [cubicQ_card_complex]; have := cubicQ_card_real; omega)
      (by rw [cubicQ_card_complex]; omega)
  refine ⟨hb, ?_⟩
  rw [Nat.card_eq_of_bijective _ hb, Nat.card_perm, Nat.card_eq_fintype_card, cubicQ_card_complex]
  rfl

/-- `Gal(X³ − X + 2 / ℚ) ≃* S₃`. -/
noncomputable def cubicQ_gal_equiv : cubicQ.Gal ≃* Equiv.Perm (Fin 3) :=
  (MulEquiv.ofBijective _ cubicQ_gal_full.1).trans
    (Equiv.permCongrHom (Fintype.equivFinOfCardEq cubicQ_card_complex))

/-! ## Route B: the root cover over the punctured mass line and its monodromy.

At `E = 0` the cubic is `r³ − r + 2M` (the receipt's `2M = r₀ − r₀³`). Its roots over `M` are the fibre of
`massOf r = (r − r³)/2`. The branch locus is `27M² = 1`; `base` is its complement and `Cover` its preimage. -/

open Complex Set unitInterval ComplexConjugate

/-- `M` as a function of a root: `r³ − r + 2M = 0 ↔ M = (r − r³)/2`. -/
noncomputable def massOf (r : ℂ) : ℂ := (r - r ^ 3) / 2

/-- The punctured mass line: the complement of the branch locus `27M² = 1`. -/
def base : Set ℂ := {M | 27 * M ^ 2 ≠ 1}

/-- The total space of the root cover: roots lying over unbranched masses. -/
abbrev Cover : Set ℂ := massOf ⁻¹' base

/-- The root cover: a root `r` maps to its mass `M`. -/
noncomputable def proj : Cover → base := base.restrictPreimage massOf

@[simp] lemma proj_val (z : Cover) : ((proj z : base) : ℂ) = massOf z := rfl

lemma massOf_root_iff (r M : ℂ) : r ^ 3 - r + 2 * M = 0 ↔ massOf r = M := by
  unfold massOf; constructor <;> intro h
  · linear_combination (-1/2 : ℂ) * h
  · linear_combination -2 * h

/-- Over an unbranched mass every root is simple (`3r² ≠ 1`), so the three roots are distinct. -/
lemma simple_root {r : ℂ} (hr : r ∈ Cover) : 1 - 3 * r ^ 2 ≠ 0 := by
  intro h; apply hr
  show 27 * massOf r ^ 2 = 1
  have h3 : r ^ 2 = 1 / 3 := by linear_combination (-1/3 : ℂ) * h
  unfold massOf
  have : (r - r ^ 3) ^ 2 = r ^ 2 * (1 - r ^ 2) ^ 2 := by ring
  rw [div_pow, this, h3]; norm_num

lemma massOf_eq_eval : massOf = fun r => (C (1 / 2 : ℂ) * (X - X ^ 3)).eval r := by
  funext r; simp [massOf]; ring

lemma massOf_isClosedMap : IsClosedMap massOf := by
  rw [massOf_eq_eval]; exact Polynomial.isClosedMap_eval _

lemma massOf_fibre_finite (M : ℂ) : (massOf ⁻¹' {M}).Finite := by
  have hne : (X ^ 3 - X + C (2 * M) : ℂ[X]) ≠ 0 := by
    intro h
    have h2 := congrArg (eval 2) h; have h0 := congrArg (eval 0) h
    simp at h2 h0; rw [h0] at h2; norm_num at h2
  refine (Polynomial.finite_setOfPred_isRoot hne).subset fun r hr => ?_
  simp only [mem_preimage, mem_singleton_iff] at hr
  simp only [mem_ofPred_eq, IsRoot, eval_add, eval_sub, eval_pow, eval_X, eval_C]
  exact (massOf_root_iff r M).2 hr

lemma massOf_hasStrictDerivAt (r : ℂ) : HasStrictDerivAt massOf ((1 - 3 * r ^ 2) / 2) r := by
  have h := ((hasStrictDerivAt_id r).fun_sub (hasStrictDerivAt_pow 3 r)).div_const 2
  convert h using 1
  funext x; simp [massOf]

/-- Inverse function theorem: `massOf` is a local homeomorphism at every point of the cover. -/
lemma massOf_isLocalHomeomorphOn : IsLocalHomeomorphOn massOf Cover := by
  refine IsLocalHomeomorphOn.mk _ _ fun r hr => ?_
  have hd : (1 - 3 * r ^ 2) / 2 ≠ 0 := div_ne_zero (simple_root hr) two_ne_zero
  let i : ℂ ≃L[ℂ] ℂ := .unitsEquivAut ℂ (.mk0 _ hd)
  have hfd : HasStrictFDerivAt massOf i.toContinuousLinearMap r := massOf_hasStrictDerivAt r
  exact ⟨hfd.toOpenPartialHomeomorph massOf, hfd.mem_toOpenPartialHomeomorph_source, fun _ _ => rfl⟩

/-- **The root map is a covering map** over the punctured mass line. -/
theorem proj_isCoveringMap : IsCoveringMap proj :=
  (massOf_isClosedMap.isCoveringMapOn_of_isLocalHomeomorphOn (fun M _ => massOf_fibre_finite M)
    massOf_isLocalHomeomorphOn).isCoveringMap_restrictPreimage

/-! ### The base point `M = 0` and its fibre `{0, 1, −1}` -/

def x₀ : base := ⟨0, by simp [base]⟩

lemma mem_fibre_iff (z : Cover) : z ∈ proj ⁻¹' {x₀} ↔ massOf z = 0 := by
  simp only [mem_preimage, mem_singleton_iff, Subtype.ext_iff, proj_val]; rfl

lemma fibre_massOf (z : proj ⁻¹' {x₀}) : massOf ((z : Cover) : ℂ) = 0 := (mem_fibre_iff _).1 z.2

lemma massOf_zero_cases {w : ℂ} (h : massOf w = 0) : w = 0 ∨ w = 1 ∨ w = -1 := by
  have : w * ((1 - w) * (1 + w)) = 0 := by unfold massOf at h; linear_combination 2 * h
  rcases mul_eq_zero.1 this with h | h
  · exact Or.inl h
  rcases mul_eq_zero.1 h with h | h
  · exact Or.inr (Or.inl (by linear_combination -h))
  · exact Or.inr (Or.inr (by linear_combination h))

lemma fibre_cases (z : proj ⁻¹' {x₀}) :
    ((z : Cover) : ℂ) = 0 ∨ ((z : Cover) : ℂ) = 1 ∨ ((z : Cover) : ℂ) = -1 :=
  massOf_zero_cases (fibre_massOf z)

lemma fibre_ext {z w : proj ⁻¹' {x₀}} (h : ((z : Cover) : ℂ) = ((w : Cover) : ℂ)) : z = w :=
  Subtype.ext (Subtype.ext h)

def e₀ : proj ⁻¹' {x₀} := ⟨⟨0, by simp [Cover, base, massOf]⟩, (mem_fibre_iff _).2 (by simp [massOf])⟩

/-! ### Symmetries: complex conjugation and `r ↦ −r` -/

lemma massOf_conj (r : ℂ) : massOf (conj r) = conj (massOf r) := by
  simp [massOf, map_ofNat]

lemma massOf_neg (r : ℂ) : massOf (-r) = -massOf r := by unfold massOf; ring

lemma conj_mem_base {M : ℂ} (h : M ∈ base) : conj M ∈ base := by
  intro h'; apply h
  have := congrArg conj h'; simpa [map_mul, map_pow, map_ofNat] using this

lemma neg_mem_base {M : ℂ} (h : M ∈ base) : -M ∈ base := by
  intro h'; apply h; simpa [base, neg_sq] using h'

def conjC (z : Cover) : Cover := ⟨conj (z : ℂ), by
  show massOf _ ∈ base; rw [massOf_conj]; exact conj_mem_base z.2⟩

def negC (z : Cover) : Cover := ⟨-(z : ℂ), by
  show massOf _ ∈ base; rw [massOf_neg]; exact neg_mem_base z.2⟩

lemma continuous_conjC : Continuous conjC :=
  continuous_induced_rng.2 (Complex.continuous_conj.comp continuous_subtype_val)

lemma continuous_negC : Continuous negC := continuous_induced_rng.2 continuous_subtype_val.neg

/-! ### The general swap criterion

If a loop `δ` at `M = 0` is conjugation-symmetric (`δ(1 − t) = conj δ(t)`), and its lift from the root `0` is
non-real at `t = 1/2`, then its monodromy is the transposition of `0` with the endpoint of that lift. -/

noncomputable def half : I := ⟨1 / 2, by norm_num, by norm_num⟩

lemma symm_half : σ half = half := Subtype.ext (by simp [half]; norm_num)

section swap

variable (δ : Path x₀ x₀)

/-- The lift of `δ` starting at the root `0`. -/
noncomputable def liftAt0 : C(I, Cover) :=
  proj_isCoveringMap.liftPath δ (e₀ : Cover) (δ.source.trans e₀.2.symm)

lemma liftAt0_massOf (t : I) : massOf (liftAt0 δ t : ℂ) = (δ t : ℂ) := by
  have := congrFun (proj_isCoveringMap.liftPath_lifts δ (e₀ : Cover) (δ.source.trans e₀.2.symm)) t
  exact congrArg Subtype.val this

lemma liftAt0_zero : liftAt0 δ 0 = (e₀ : Cover) := proj_isCoveringMap.liftPath_zero ..

/-- The monodromy of `δ` acting on the fibre over `M = 0`. -/
noncomputable def mono : proj ⁻¹' {x₀} → proj ⁻¹' {x₀} :=
  proj_isCoveringMap.monodromy (Path.Homotopic.Quotient.mk δ)

lemma mono_e₀ : ((mono δ e₀ : Cover) : ℂ) = (liftAt0 δ 1 : ℂ) := by
  rw [mono, proj_isCoveringMap.coe_monodromy_mk]; rfl

theorem mono_swap (hsym : ∀ t, (δ (σ t) : ℂ) = conj (δ t : ℂ)) (hhalf : (liftAt0 δ half : ℂ).im ≠ 0) :
    mono δ e₀ ≠ e₀ ∧ mono δ (mono δ e₀) = e₀ := by
  set Γ := liftAt0 δ
  -- the conjugate-reversed lift
  let Γ' : C(I, Cover) := ⟨fun t => conjC (Γ (σ t)), continuous_conjC.comp (Γ.continuous.comp continuous_symm)⟩
  have hΓ' : proj ∘ Γ' = δ := by
    funext t; apply Subtype.ext
    simp only [Function.comp_apply, proj_val, Γ', ContinuousMap.coe_mk, conjC]
    rw [massOf_conj, liftAt0_massOf, hsym, Complex.conj_conj]
  have hΓ : proj ∘ Γ = δ := proj_isCoveringMap.liftPath_lifts ..
  have hreal : ∀ z : proj ⁻¹' {x₀}, conj ((z : Cover) : ℂ) = ((z : Cover) : ℂ) := fun z => by
    rcases fibre_cases z with h | h | h <;> rw [h] <;> simp
  have hend : (Γ 1 : ℂ) = ((mono δ e₀ : Cover) : ℂ) := (mono_e₀ δ).symm
  have hΓ'0 : Γ' 0 = (mono δ e₀ : Cover) := by
    apply Subtype.ext
    show conj (Γ (σ 0) : ℂ) = _
    rw [symm_zero, hend, hreal]
  have hΓ'1 : (Γ' 1 : ℂ) = 0 := by
    show conj (Γ (σ 1) : ℂ) = 0
    rw [symm_one, liftAt0_zero]; simp [e₀]
  refine ⟨fun heq => hhalf ?_, ?_⟩
  · -- if the lift closed up, uniqueness of lifts would force `Γ' = Γ`, making `Γ(1/2)` real
    have h0 : Γ' 0 = Γ 0 := by rw [hΓ'0, heq, liftAt0_zero]
    have := proj_isCoveringMap.eq_of_comp_eq Γ'.continuous Γ.continuous (hΓ'.trans hΓ.symm) 0 h0
    have hh := congrArg (fun g => ((g half : Cover) : ℂ)) this
    simp only [Γ', ContinuousMap.coe_mk, conjC, symm_half] at hh
    have := congrArg Complex.im hh
    simp at this; linarith
  · apply fibre_ext
    have := proj_isCoveringMap.monodromy_eq_apply_one (γ := δ) (e := mono δ e₀) (Γ := Γ') hΓ' hΓ'0
    show ((proj_isCoveringMap.monodromy (Path.Homotopic.Quotient.mk δ) (mono δ e₀) : Cover) : ℂ) = _
    rw [this, hΓ'1]; rfl

end swap

/-! ### The explicit loop around the branch point `M = +1/√27`

`γ(t) = 4t(1 − t) + i·t(1 − t)(1 − 2t)`: it leaves `0` into the upper half-plane, crosses the real axis at
`M = 1 > 1/√27`, and returns through the lower half-plane. It is conjugation-symmetric. -/

noncomputable def γc (t : ℝ) : ℂ := ((4 * t * (1 - t) : ℝ) : ℂ) + ((t * (1 - t) * (1 - 2 * t) : ℝ) : ℂ) * Complex.I

@[simp] lemma γc_re (t : ℝ) : (γc t).re = 4 * t * (1 - t) := by simp [γc]
@[simp] lemma γc_im (t : ℝ) : (γc t).im = t * (1 - t) * (1 - 2 * t) := by simp [γc]

lemma γc_cont : Continuous γc := by unfold γc; fun_prop

lemma γc_mem (t : ℝ) : γc t ∈ base := by
  intro h
  rw [Complex.ext_iff] at h
  simp only [sq, Complex.mul_re, Complex.mul_im, Complex.re_ofNat, Complex.im_ofNat, γc_re, γc_im,
    Complex.one_re, Complex.one_im] at h
  obtain ⟨h1, h2⟩ := h
  have hab : (4 * t * (1 - t)) * (t * (1 - t) * (1 - 2 * t)) = 0 := by nlinarith
  rcases mul_eq_zero.1 hab with ha | hb
  · rw [ha] at h1; nlinarith [sq_nonneg (t * (1 - t) * (1 - 2 * t))]
  · rw [hb] at h1
    rcases mul_eq_zero.1 hb with hb | hb
    · rcases mul_eq_zero.1 hb with hb | hb
      · rw [hb] at h1; norm_num at h1
      · have : t = 1 := by linarith
        rw [this] at h1; norm_num at h1
    · have : t = 1 / 2 := by linarith
      rw [this] at h1; norm_num at h1

/-- The loop `γ` in the punctured mass line, based at `M = 0`. -/
noncomputable def loopPlus : Path x₀ x₀ where
  toFun t := ⟨γc t, γc_mem t⟩
  continuous_toFun := (γc_cont.comp continuous_subtype_val).subtype_mk _
  source' := Subtype.ext (by simp [γc, x₀])
  target' := Subtype.ext (by simp [γc, x₀])

/-- The mirror loop `−γ`, around the other branch point `M = −1/√27`. -/
noncomputable def loopMinus : Path x₀ x₀ where
  toFun t := ⟨-γc t, neg_mem_base (γc_mem t)⟩
  continuous_toFun := ((γc_cont.comp continuous_subtype_val).neg).subtype_mk _
  source' := Subtype.ext (by simp [γc, x₀])
  target' := Subtype.ext (by simp [γc, x₀])

lemma γc_symm (t : I) : γc (σ t) = conj (γc t) := by
  apply Complex.ext <;> simp [unitInterval.coe_symm_eq] <;> ring

lemma massOf_im (z : ℂ) : (massOf z).im = z.im * (1 - 3 * z.re ^ 2 + z.im ^ 2) / 2 := by
  simp [massOf, pow_succ, Complex.mul_re, Complex.mul_im]; ring

lemma massOf_re (z : ℂ) : (massOf z).re = (z.re - (z.re ^ 3 - 3 * z.re * z.im ^ 2)) / 2 := by
  simp [massOf, pow_succ, Complex.mul_re, Complex.mul_im]; ring

/-- **The half-plane argument.** A continuous lift `g` of `γ` from the root `0` stays in the component
`{Im r > 0, 3(Re r)² − (Im r)² < 1}` of the preimage of the upper half-plane while `γ` is there, so at `t = 1/2`
(where `γ = 1`) it is not real: the real root over `M = 1` lies outside that component's closure. -/
theorem lift_half_nonreal (g : I → ℂ) (hg : Continuous g) (h0 : g 0 = 0)
    (hl : ∀ t : I, massOf (g t) = γc t) : (g half).im ≠ 0 := by
  let h : ℝ → ℂ := g ∘ projIcc (0 : ℝ) 1 zero_le_one
  have hq : Continuous fun z : ℂ => 3 * z.re ^ 2 - z.im ^ 2 :=
    ((continuous_re.pow 2).const_mul 3).sub (continuous_im.pow 2)
  have hc : Continuous h := hg.comp continuous_projIcc
  have hl' : ∀ t ∈ Icc (0 : ℝ) 1, massOf (h t) = γc t := fun t ht => by
    simp only [h, Function.comp_apply, projIcc_of_mem _ ht]; exact hl _
  let U₀ : Set ℂ := {z | 0 < z.im ∧ 3 * z.re ^ 2 - z.im ^ 2 < 1}
  let U₁ : Set ℂ := {z | z.im < 0 ∧ 1 < 3 * z.re ^ 2 - z.im ^ 2}
  have hU₀ : IsOpen U₀ := (isOpen_lt continuous_const continuous_im).inter
    (isOpen_lt hq continuous_const)
  have hU₁ : IsOpen U₁ := (isOpen_lt continuous_im continuous_const).inter
    (isOpen_lt continuous_const hq)
  have hdisj : Disjoint U₀ U₁ := Set.disjoint_left.2 fun z h₀ h₁ => by linarith [h₀.1, h₁.1]
  have hsub : h '' Ioo 0 (1 / 2) ⊆ U₀ ∪ U₁ := by
    rintro _ ⟨t, ht, rfl⟩
    have hpos : 0 < (massOf (h t)).im := by
      rw [hl' t ⟨ht.1.le, by linarith [ht.2]⟩, γc_im]
      exact mul_pos (mul_pos ht.1 (by linarith [ht.2])) (by linarith [ht.2])
    rw [massOf_im] at hpos
    have : 0 < (h t).im * (1 - 3 * (h t).re ^ 2 + (h t).im ^ 2) := by linarith
    rcases pos_and_pos_or_neg_and_neg_of_mul_pos this with ⟨a, b⟩ | ⟨a, b⟩
    · exact Or.inl ⟨a, by linarith⟩
    · exact Or.inr ⟨a, by linarith⟩
  have hne : (h '' Ioo 0 (1 / 2) ∩ U₀).Nonempty := by
    have hW : IsOpen {z : ℂ | 3 * z.re ^ 2 - z.im ^ 2 < 1} := isOpen_lt hq continuous_const
    have h0' : h 0 = 0 := by simpa [h, projIcc_of_mem _ (⟨le_rfl, zero_le_one⟩ : (0:ℝ) ∈ Icc 0 1)] using h0
    have ev1 : ∀ᶠ t in nhdsWithin (0 : ℝ) (Ioi 0), h t ∈ {z : ℂ | 3 * z.re ^ 2 - z.im ^ 2 < 1} :=
      ((hc.tendsto 0).eventually (hW.mem_nhds (by simp [h0']))).filter_mono nhdsWithin_le_nhds
    have ev2 : ∀ᶠ t in nhdsWithin (0 : ℝ) (Ioi 0), t ∈ Ioo (0 : ℝ) (1 / 2) := Ioo_mem_nhdsGT (by norm_num)
    obtain ⟨t, ht1, ht2⟩ := (ev1.and ev2).exists
    refine ⟨h t, ⟨t, ht2, rfl⟩, ?_⟩
    rcases hsub ⟨t, ht2, rfl⟩ with h' | h'
    · exact h'
    · exact absurd h'.2 (by simp only [mem_ofPred_eq] at ht1; linarith)
  have hin : h '' Ioo 0 (1 / 2) ⊆ U₀ :=
    (isPreconnected_Ioo.image h hc.continuousOn).subset_left_of_subset_union hU₀ hU₁ hdisj hsub hne
  -- pass to the closure
  let Cl : Set ℂ := {z | 0 ≤ z.im ∧ 3 * z.re ^ 2 - z.im ^ 2 ≤ 1}
  have hCl : IsClosed (h ⁻¹' Cl) :=
    ((isClosed_le continuous_const continuous_im).inter
      (isClosed_le hq continuous_const)).preimage hc
  have hIoo : Ioo (0 : ℝ) (1 / 2) ⊆ h ⁻¹' Cl := fun t ht =>
    have := hin ⟨t, ht, rfl⟩; ⟨this.1.le, this.2.le⟩
  have hhalf : (1 / 2 : ℝ) ∈ h ⁻¹' Cl := by
    have := hCl.closure_subset_iff.2 hIoo
    rw [closure_Ioo (by norm_num)] at this
    exact this ⟨by norm_num, le_rfl⟩
  have hgh : h (1 / 2) = g half := by
    simp only [h, Function.comp_apply]
    rw [projIcc_of_mem _ (⟨by norm_num, by norm_num⟩ : (1 / 2 : ℝ) ∈ Icc (0 : ℝ) 1)]; rfl
  have hhalf' : g half ∈ Cl := hgh ▸ hhalf
  intro him
  obtain ⟨-, hb⟩ := hhalf'
  have hm := congrArg Complex.re (hl half)
  rw [massOf_re, him, γc_re, show ((half : I) : ℝ) = 1 / 2 from rfl] at hm
  rw [him] at hb
  have hx : (g half).re ^ 2 ≤ 1 / 3 := by linarith
  have e : (g half).re - (g half).re ^ 3 = 2 := by linear_combination 2 * hm
  have h4 : (g half).re ^ 2 * (1 - (g half).re ^ 2) ^ 2 = 4 := by
    linear_combination ((g half).re - (g half).re ^ 3 + 2) * e
  have hq1 : (1 - (g half).re ^ 2) ^ 2 ≤ 1 := by nlinarith [sq_nonneg (g half).re]
  nlinarith [mul_le_mul_of_nonneg_left hq1 (sq_nonneg (g half).re)]

/-! ### The two transpositions -/

lemma liftPlus_half : (liftAt0 loopPlus half : ℂ).im ≠ 0 :=
  lift_half_nonreal (fun t => (liftAt0 loopPlus t : ℂ)) (continuous_subtype_val.comp (liftAt0 loopPlus).continuous)
    (by rw [liftAt0_zero]; rfl) (fun t => by rw [liftAt0_massOf]; rfl)

lemma liftMinus_eq : liftAt0 loopMinus =
    ⟨fun t => negC (liftAt0 loopPlus t), continuous_negC.comp (liftAt0 loopPlus).continuous⟩ := by
  symm
  refine (proj_isCoveringMap.eq_liftPath_iff' _).2 ⟨funext fun t => Subtype.ext ?_, Subtype.ext ?_⟩
  · simp only [Function.comp_apply, proj_val, ContinuousMap.coe_mk, negC]
    rw [massOf_neg, liftAt0_massOf]; rfl
  · simp only [ContinuousMap.coe_mk, negC]; rw [liftAt0_zero]; simp [e₀]

theorem swap_plus : mono loopPlus e₀ ≠ e₀ ∧ mono loopPlus (mono loopPlus e₀) = e₀ :=
  mono_swap loopPlus (fun t => γc_symm t) liftPlus_half

theorem swap_minus : mono loopMinus e₀ ≠ e₀ ∧ mono loopMinus (mono loopMinus e₀) = e₀ := by
  refine mono_swap loopMinus (fun t => ?_) ?_
  · show -γc (σ t) = conj (-γc t); rw [γc_symm, map_neg]
  · rw [liftMinus_eq]; simp only [ContinuousMap.coe_mk, negC, neg_im, ne_eq, neg_eq_zero]
    exact liftPlus_half

lemma mono_minus_val : ((mono loopMinus e₀ : Cover) : ℂ) = -((mono loopPlus e₀ : Cover) : ℂ) := by
  rw [mono_e₀, mono_e₀, liftMinus_eq]; rfl

/-- A permutation of the fibre that swaps `a` and `b` and is a bijection fixes the third point: it is `swap a b`. -/
lemma eq_swap_of (g : Equiv.Perm (proj ⁻¹' {x₀})) (a b : proj ⁻¹' {x₀}) (ha : ((a : Cover) : ℂ) = 0)
    (hab : b ≠ a) (h1 : g a = b) (h2 : g b = a) : g = Equiv.swap a b := by
  ext z : 1
  by_cases hza : z = a
  · subst hza; simp [h1]
  by_cases hzb : z = b
  · subst hzb; simp [h2]
  rw [Equiv.swap_apply_of_ne_of_ne hza hzb]
  have hga : g z ≠ b := fun h => hza (g.injective (h.trans h1.symm))
  have hgb : g z ≠ a := fun h => hzb (g.injective (h.trans h2.symm))
  have va : ∀ w : proj ⁻¹' {x₀}, w ≠ a → ((w : Cover) : ℂ) ≠ 0 := fun w hw h =>
    hw (fibre_ext (h.trans ha.symm))
  have vb : ∀ w : proj ⁻¹' {x₀}, w ≠ b → ((w : Cover) : ℂ) ≠ ((b : Cover) : ℂ) := fun w hw h =>
    hw (fibre_ext h)
  apply fibre_ext
  have hb0 := va b hab
  rcases fibre_cases b with hb | hb | hb
  · exact absurd hb hb0
  all_goals
    rcases fibre_cases z with hz | hz | hz <;> rcases fibre_cases (g z) with hw | hw | hw <;>
    first
    | exact absurd hz (va z hza)
    | exact absurd hw (va _ hgb)
    | exact absurd (hz.trans hb.symm) (vb z hzb)
    | exact absurd (hw.trans hb.symm) (vb _ hga)
    | (rw [hz, hw])

/-! ### Headline: the monodromy group is all of `S₃` -/

/-- The fibre over `M = 0` is `{e₀, b, c}` = `{0, r*, −r*}`, with `b, c` the images of `e₀` under the two loops. -/
lemma fibre_facts :
    e₀ ≠ mono loopPlus e₀ ∧ e₀ ≠ mono loopMinus e₀ ∧ mono loopPlus e₀ ≠ mono loopMinus e₀ ∧
      ∀ z : proj ⁻¹' {x₀}, z = e₀ ∨ z = mono loopPlus e₀ ∨ z = mono loopMinus e₀ := by
  set b := mono loopPlus e₀
  set c := mono loopMinus e₀
  have hb := swap_plus
  have he0 : ((e₀ : Cover) : ℂ) = 0 := rfl
  have hbv : ((b : Cover) : ℂ) ≠ 0 := fun h => hb.1 (fibre_ext (h.trans he0.symm))
  have hcv : ((c : Cover) : ℂ) = -((b : Cover) : ℂ) := mono_minus_val
  refine ⟨fun h => hb.1 h.symm, fun h => hbv ?_, fun h => hbv ?_, fun z => ?_⟩
  · have := congrArg (fun w : proj ⁻¹' {x₀} => ((w : Cover) : ℂ)) h
    simp only [hcv, he0] at this; linear_combination this
  · have := congrArg (fun w : proj ⁻¹' {x₀} => ((w : Cover) : ℂ)) h
    simp only [hcv] at this; linear_combination this / 2
  rcases fibre_cases z with hz | hz | hz
  · exact Or.inl (fibre_ext (hz.trans he0.symm))
  all_goals rcases fibre_cases b with hb' | hb' | hb'
  all_goals first
    | exact absurd hb' hbv
    | exact Or.inr (Or.inl (fibre_ext (hz.trans hb'.symm)))
    | exact Or.inr (Or.inr (fibre_ext (by simp [hz, hcv, hb'])))

/-- The fibre over `M = 0`, enumerated. -/
lemma fibre_enum_bijective : Function.Bijective (![e₀, mono loopPlus e₀, mono loopMinus e₀]) := by
  obtain ⟨h1, h2, h3, hall⟩ := fibre_facts
  refine ⟨fun i j h => ?_, fun z => ?_⟩
  · fin_cases i <;> fin_cases j <;> simp at h ⊢
    all_goals first | exact h1 h | exact h2 h | exact h3 h | exact h1 h.symm | exact h2 h.symm | exact h3 h.symm
  · rcases hall z with h | h | h
    exacts [⟨0, h.symm⟩, ⟨1, h.symm⟩, ⟨2, h.symm⟩]

/-- **The cover is three-sheeted:** the fibre over `M = 0` has exactly three points. -/
theorem fibre_card : Nat.card (proj ⁻¹' {x₀}) = 3 := by
  rw [← Nat.card_eq_of_bijective _ fibre_enum_bijective]; simp

instance : Finite (proj ⁻¹' {x₀}) := Finite.of_surjective _ fibre_enum_bijective.2

/-- **Route B headline.** The monodromy action of the fundamental group of the punctured mass line
`ℂ ∖ {27M² = 1}`, based at `M = 0`, on the three roots `{0, 1, −1}` of `r³ − r` is onto the full
symmetric group of the fibre. -/
theorem monodromy_surjective : Function.Surjective (proj_isCoveringMap.monodromyPerm x₀) := by
  set mp := proj_isCoveringMap.monodromyPerm x₀
  obtain ⟨hab, hac, hbc, hall⟩ := fibre_facts
  set b := mono loopPlus e₀
  set c := mono loopMinus e₀
  have he0 : ((e₀ : Cover) : ℂ) = 0 := rfl
  have h1 : Equiv.swap e₀ b ∈ mp.range :=
    ⟨FundamentalGroup.fromPath (Path.Homotopic.Quotient.mk loopPlus),
      eq_swap_of _ _ _ he0 (Ne.symm hab) rfl swap_plus.2⟩
  have h2 : Equiv.swap e₀ c ∈ mp.range :=
    ⟨FundamentalGroup.fromPath (Path.Homotopic.Quotient.mk loopMinus),
      eq_swap_of _ _ _ he0 (Ne.symm hac) rfl swap_minus.2⟩
  have h3 : Equiv.swap b c ∈ mp.range := by
    have := mp.range.mul_mem (mp.range.mul_mem h1 h2) h1
    rwa [Equiv.swap_comm e₀ c, Equiv.swap_mul_swap_mul_swap hac.symm hbc.symm] at this
  have hrange : mp.range = ⊤ := by
    rw [eq_top_iff, ← Equiv.Perm.closure_isSwap, Subgroup.closure_le]
    rintro τ ⟨x, y, hxy, rfl⟩
    rcases hall x with rfl | rfl | rfl <;> rcases hall y with rfl | rfl | rfl <;>
      first
      | exact absurd rfl hxy
      | assumption
      | rwa [Equiv.swap_comm]
  exact MonoidHom.range_eq_top.1 hrange

/-- **The ROW object.** The monodromy group of the root cover (image of `π₁(ℂ ∖ {27M² = 1}, 0)` in the
permutations of the fibre) is `S₃`. -/
noncomputable def monodromyGroup_equiv_S3 :
    (proj_isCoveringMap.monodromyPerm x₀).range ≃* Equiv.Perm (Fin 3) :=
  ((MulEquiv.subgroupCongr (MonoidHom.range_eq_top.2 monodromy_surjective)).trans Subgroup.topEquiv).trans
    (Equiv.permCongrHom (Equiv.ofBijective _ fibre_enum_bijective).symm)

/-- The topological monodromy group and the Galois group of the `M = 1` member are abstractly isomorphic
(both `≃* S₃`). This is NOT the canonical identification (Riemann existence); see the report. -/
noncomputable def monodromy_equiv_gal :
    (proj_isCoveringMap.monodromyPerm x₀).range ≃* cubicQ.Gal :=
  monodromyGroup_equiv_S3.trans cubicQ_gal_equiv.symm

end ShadowProbe.Row18Monodromy

#print axioms ShadowProbe.Row18Monodromy.cubicQ_irreducible
#print axioms ShadowProbe.Row18Monodromy.cubicQ_disc_not_square
#print axioms ShadowProbe.Row18Monodromy.cubicQ_gal_full
#print axioms ShadowProbe.Row18Monodromy.cubicQ_gal_equiv
#print axioms ShadowProbe.Row18Monodromy.proj_isCoveringMap
#print axioms ShadowProbe.Row18Monodromy.monodromy_surjective
#print axioms ShadowProbe.Row18Monodromy.fibre_card
#print axioms ShadowProbe.Row18Monodromy.monodromyGroup_equiv_S3
#print axioms ShadowProbe.Row18Monodromy.monodromy_equiv_gal
#print axioms ShadowProbe.Row18Monodromy.swap_plus
#print axioms ShadowProbe.Row18Monodromy.swap_minus
#print axioms ShadowProbe.Row18Monodromy.lift_half_nonreal

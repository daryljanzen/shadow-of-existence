import Mathlib

/-! # Campaign 50 (`r7443+71.50`), row 53: the range is the essential image

Receipt: `receipts/P09_range_paper/K7_range_is_essential_image.py`. It reads P9's range as the essential image of
the parameter-to-geometry map. The upper bound is the solution class (`prop:bound`), and the bound is attained
(`prop:surj`). Its fibres are "1 for SdS; FOUR for Type-D", and its strata isotropies have dimensions 10, 6 and 4
inside 15.

The receipt never writes the functor down, so this probe supplies it. Here the essential image is
`CategoryTheory.Functor.essImage`, taken on concrete categories:

- ***SdS.***
  - The source is `Discrete ℝ`, the mass line.
  - The target is the category `Prof` of radial profiles `f : ℝ → ℝ`. There is one morphism `f ⟶ g` exactly when
    `f = g` on `r > 0`. That is the thin groupoid of "same geometry on the static region".
  - The functor sends `M ↦ 1 − 2M/r − Λr²/3`.
- ***Type-D.***
  - The source is `Discrete (Fin 4 → ℝ)`.
  - The target is `Discrete (ℝ[X] × ℝ[X])`, the quartic pairs `(D_r, D_p)`.

The headlines:

- `sds_essImage`: the essential image is EXACTLY the class of differentiable solutions of
  `r f' + f − 1 + Λr² = 0` on `r > 0`.
- `sds_equiv`: the functor is fully faithful, so `Discrete ℝ ≌ essImage`.
- `sds_fibre`: every solution has exactly one `M`.
- `sds_dim`: on `(0,∞)` the class is `f₀ + ℝ·(−2/r)`, a line, of dimension `1`.
- `td_essImage`: the essential image is EXACTLY the intrinsic class: both entries of degree ≤ 4, leading
  coefficient `−Λ/3`, no cubic term, opposite `r²`/`p²` coefficients and a shared constant term.
- `td_equiv`, `td_dim`: the class is `base + range L` with `L` injective linear, of dimension `4`.
- `strata_finrank`: Mathlib's indefinite `so'(p,q)` has `dim so(4,1) = 10`, `dim so(2,1) ⊕ so(3) = 6`,
  `dim ℝ ⊕ so(3) = 4` and `dim so(5,1) = 15`. -/

namespace ShadowProbe.Row53Image

open CategoryTheory Polynomial Matrix

attribute [local instance 100] LieRing.ofAssociativeRing

/-! ### SdS: the category of radial profiles -/

/-- a radial profile `f(r)` -/
structure Prof where
  fn : ℝ → ℝ

/-- `f ≤ g` iff `f = g` on the static region `r > 0`; it is symmetric, so the category is a thin groupoid -/
instance : Preorder Prof where
  le f g := ∀ r : ℝ, 0 < r → f.fn r = g.fn r
  le_refl _ _ _ := rfl
  le_trans _ _ _ h1 h2 r hr := (h1 r hr).trans (h2 r hr)

theorem iso_iff (f g : Prof) : Nonempty (f ≅ g) ↔ ∀ r : ℝ, 0 < r → f.fn r = g.fn r := by
  refine ⟨fun ⟨e⟩ => leOfHom e.hom, fun h => ⟨⟨homOfLE h, homOfLE fun r hr => (h r hr).symm,
    Subsingleton.elim _ _, Subsingleton.elim _ _⟩⟩⟩

/-- the SdS kernel `f = 1 − 2M/r − Λr²/3` -/
noncomputable def fSdS (M Λ r : ℝ) : ℝ := 1 - 2 * M / r - Λ * r ^ 2 / 3

/-- copied from `Row53Row86.lean` (campaign 32) -/
theorem sds_kernel (Λ : ℝ) :
    (∀ M r : ℝ, 0 < r → HasDerivAt (fSdS M Λ) (2 * M / r ^ 2 - 2 * Λ * r / 3) r ∧
        r * (2 * M / r ^ 2 - 2 * Λ * r / 3) + fSdS M Λ r - 1 + Λ * r ^ 2 = 0) ∧
      ∀ f f' : ℝ → ℝ, (∀ r, 0 < r → HasDerivAt f (f' r) r) →
        (∀ r, 0 < r → r * f' r + f r - 1 + Λ * r ^ 2 = 0) →
        ∃! M : ℝ, ∀ r, 0 < r → f r = fSdS M Λ r := by
  refine ⟨fun M r hr => ⟨?_, ?_⟩, fun f f' hf hode => ?_⟩
  · have h1 : HasDerivAt (fun x : ℝ => x⁻¹) (-(r ^ 2)⁻¹) r := hasDerivAt_inv hr.ne'
    have h2 : HasDerivAt (fun x : ℝ => x ^ 2) (2 * r) r := by simpa using hasDerivAt_pow 2 r
    have := ((h1.const_mul (2 * M)).const_sub 1).sub (h2.const_mul (Λ / 3))
    convert this using 1
    · funext x; simp [fSdS]; ring
    · field_simp
  · simp only [fSdS]; field_simp; ring
  · set g : ℝ → ℝ := fun r => r * f r - r + Λ * r ^ 3 / 3 with hg
    have hgd : ∀ r, 0 < r → HasDerivAt g 0 r := by
      intro r hr
      have h3 : HasDerivAt (fun x : ℝ => x ^ 3) (3 * r ^ 2) r := by simpa using hasDerivAt_pow 3 r
      have := (((hasDerivAt_id r).mul (hf r hr)).sub (hasDerivAt_id r)).add (h3.const_mul (Λ / 3))
      convert this using 1
      · funext x; simp [hg]; ring
      · simp; linarith [hode r hr]
    have hconst : ∀ r, 0 < r → g r = g 1 := by
      intro r hr
      have hdiff : DifferentiableOn ℝ g (Set.Ioi 0) := fun x hx => (hgd x hx).differentiableAt.differentiableWithinAt
      have hder : Set.EqOn (deriv g) 0 (Set.Ioi 0) := fun x hx => (hgd x hx).deriv
      exact isOpen_Ioi.is_const_of_deriv_eq_zero (convex_Ioi 0).isPreconnected hdiff hder hr (by norm_num : (0:ℝ) < 1)
    refine ⟨-(g 1) / 2, fun r hr => ?_, fun M hM => ?_⟩
    · have := hconst r hr
      simp only [hg, fSdS] at this ⊢
      field_simp
      linarith
    · have h1 := hM 1 one_pos
      simp only [hg, fSdS] at h1 ⊢
      linarith

/-- the parameter-to-geometry functor of the SdS family -/
noncomputable def sdsF (Λ : ℝ) : Discrete ℝ ⥤ Prof := Discrete.functor fun M => ⟨fSdS M Λ⟩

/-- the solution class: differentiable solutions of `r f' + f − 1 + Λr² = 0` on `r > 0` -/
def IsSol (Λ : ℝ) : ObjectProperty Prof := fun f => ∃ f' : ℝ → ℝ,
  (∀ r, 0 < r → HasDerivAt f.fn (f' r) r) ∧ ∀ r, 0 < r → r * f' r + f.fn r - 1 + Λ * r ^ 2 = 0

/-- ⛭ **`sds_essImage`.** The essential image of `M ↦ 1 − 2M/r − Λr²/3` IS the solution class: `prop:bound`
(`⊆`) and `prop:surj` (`⊇`) as one equality of object properties. -/
theorem sds_essImage (Λ : ℝ) : (sdsF Λ).essImage = IsSol Λ := by
  funext f
  apply propext
  constructor
  · rintro ⟨⟨M⟩, ⟨e⟩⟩
    have h := (iso_iff _ _).1 ⟨e⟩
    refine ⟨fun r => 2 * M / r ^ 2 - 2 * Λ * r / 3, fun r hr => ?_, fun r hr => ?_⟩
    · exact ((sds_kernel Λ).1 M r hr).1.congr_of_eventuallyEq
        (Filter.eventuallyEq_of_mem (Ioi_mem_nhds hr) fun x hx => (h x hx).symm)
    · rw [← h r hr]; exact ((sds_kernel Λ).1 M r hr).2
  · rintro ⟨f', hf, hode⟩
    obtain ⟨M, hM, -⟩ := (sds_kernel Λ).2 f.fn f' hf hode
    exact ⟨⟨M⟩, (iso_iff _ _).2 fun r hr => (hM r hr).symm⟩

theorem fSdS_inj (Λ M M' : ℝ) (h : ∀ r, 0 < r → fSdS M Λ r = fSdS M' Λ r) : M = M' := by
  have := h 1 one_pos; simp only [fSdS] at this; linarith

instance (Λ : ℝ) : (sdsF Λ).Full where
  map_surjective {X Y} g := ⟨eqToHom (Discrete.ext (fSdS_inj Λ X.as Y.as (leOfHom g))), Subsingleton.elim _ _⟩

instance (Λ : ℝ) : (sdsF Λ).Faithful where
  map_injective _ := Subsingleton.elim _ _

instance (Λ : ℝ) : (sdsF Λ).toEssImage.IsEquivalence where

/-- ⛭ **`sds_equiv`.** The mass line IS the essential image, as an equivalence of categories. -/
noncomputable def sds_equiv (Λ : ℝ) : Discrete ℝ ≌ (sdsF Λ).EssImageSubcategory :=
  (sdsF Λ).toEssImage.asEquivalence

/-- ⛭ **`sds_fibre`.** Over each solution, exactly ONE parameter: "1 for SdS". -/
theorem sds_fibre (Λ : ℝ) (f : Prof) (hf : IsSol Λ f) : ∃! M : ℝ, Nonempty ((sdsF Λ).obj ⟨M⟩ ≅ f) := by
  rw [← sds_essImage] at hf
  obtain ⟨⟨M⟩, ⟨e⟩⟩ := hf
  refine ⟨M, ⟨e⟩, fun M' ⟨e'⟩ => ?_⟩
  have h := (iso_iff _ _).1 ⟨e⟩; have h' := (iso_iff _ _).1 ⟨e'⟩
  exact fSdS_inj Λ M' M fun r hr => (h' r hr).trans (h r hr).symm

/-- restriction to the static region; `res f = res g ↔ Nonempty (f ≅ g)` -/
def res (f : Prof) : Set.Ioi (0 : ℝ) → ℝ := fun r => f.fn r

/-- the direction `−2/r` of the family -/
noncomputable def vSdS : Set.Ioi (0 : ℝ) → ℝ := fun r => -2 / (r : ℝ)

/-- ⛭ **`sds_dim`.** On `(0,∞)` the solution class is the affine line `f₀ + ℝ·(−2/r)`, of dimension `1`. -/
theorem sds_dim (Λ : ℝ) :
    res '' {f | IsSol Λ f} = {w | w - res ⟨fSdS 0 Λ⟩ ∈ ℝ ∙ vSdS} ∧ Module.finrank ℝ (ℝ ∙ vSdS) = 1 := by
  have key : ∀ M : ℝ, res ⟨fSdS M Λ⟩ - res ⟨fSdS 0 Λ⟩ = M • vSdS := by
    intro M; funext r
    have hr : (r : ℝ) ≠ 0 := r.2.ne'
    simp only [res, vSdS, fSdS, Pi.sub_apply, Pi.smul_apply, smul_eq_mul]; field_simp; ring
  refine ⟨Set.ext fun w => ⟨?_, ?_⟩, finrank_span_singleton fun h => ?_⟩
  · rintro ⟨f, hf, rfl⟩
    rw [Set.mem_ofPred_eq, ← sds_essImage] at hf
    obtain ⟨⟨M⟩, ⟨e⟩⟩ := hf
    have h := (iso_iff _ _).1 ⟨e⟩
    have : res f = res ⟨fSdS M Λ⟩ := funext fun r => (h r r.2).symm
    exact Submodule.mem_span_singleton.2 ⟨M, by rw [this, key]⟩
  · intro hw
    obtain ⟨M, hM⟩ := Submodule.mem_span_singleton.1 hw
    refine ⟨⟨fSdS M Λ⟩, ?_, ?_⟩
    · show IsSol Λ _; rw [← sds_essImage]; exact ⟨⟨M⟩, ⟨Iso.refl _⟩⟩
    · have := key M; rw [hM] at this; exact sub_left_inj.mp this
  · have := congrFun h ⟨1, Set.mem_Ioi.2 one_pos⟩; simp [vSdS] at this

#print axioms sds_essImage
#print axioms sds_equiv
#print axioms sds_fibre
#print axioms sds_dim

/-! ### Type-D: the quartic pair -/

/-- the receipt's quartics, as functions (campaign 32) -/
noncomputable def Dr (Λ c2 c1 c0 r : ℝ) : ℝ := -Λ / 3 * r ^ 4 + c2 * r ^ 2 + c1 * r + c0
noncomputable def Dp (Λ c2 d1 c0 p : ℝ) : ℝ := -Λ / 3 * p ^ 4 - c2 * p ^ 2 + d1 * p + c0

/-- the same quartics, as polynomials -/
noncomputable def DrP (Λ c2 c1 c0 : ℝ) : ℝ[X] := monomial 4 (-Λ / 3) + monomial 2 c2 + monomial 1 c1 + monomial 0 c0
noncomputable def DpP (Λ c2 d1 c0 : ℝ) : ℝ[X] :=
  monomial 4 (-Λ / 3) + monomial 2 (-c2) + monomial 1 d1 + monomial 0 c0

theorem eval_DrP (Λ c2 c1 c0 r : ℝ) : (DrP Λ c2 c1 c0).eval r = Dr Λ c2 c1 c0 r := by
  simp [DrP, Dr, eval_monomial]
theorem eval_DpP (Λ c2 d1 c0 p : ℝ) : (DpP Λ c2 d1 c0).eval p = Dp Λ c2 d1 c0 p := by
  simp [DpP, Dp, eval_monomial]; ring

/-- the parameter map `(c₂, c₁, c₀, d₁) ↦ (D_r, D_p)` -/
noncomputable def tdMap (Λ : ℝ) (c : Fin 4 → ℝ) : ℝ[X] × ℝ[X] := (DrP Λ (c 0) (c 1) (c 2), DpP Λ (c 0) (c 3) (c 2))

noncomputable def tdF (Λ : ℝ) : Discrete (Fin 4 → ℝ) ⥤ Discrete (ℝ[X] × ℝ[X]) := Discrete.functor fun c => ⟨tdMap Λ c⟩

/-- the intrinsic class: degree ≤ 4, leading `−Λ/3`, no cubic term, OPPOSITE `c₂`, SHARED `c₀` -/
def IsTD (Λ : ℝ) : ObjectProperty (Discrete (ℝ[X] × ℝ[X])) := fun PQ =>
  PQ.as.1.natDegree ≤ 4 ∧ PQ.as.2.natDegree ≤ 4 ∧ PQ.as.1.coeff 4 = -Λ / 3 ∧ PQ.as.2.coeff 4 = -Λ / 3 ∧
    PQ.as.1.coeff 3 = 0 ∧ PQ.as.2.coeff 3 = 0 ∧ PQ.as.2.coeff 2 = -PQ.as.1.coeff 2 ∧ PQ.as.2.coeff 0 = PQ.as.1.coeff 0

theorem tdMap_isTD (Λ : ℝ) (c : Fin 4 → ℝ) : IsTD Λ ⟨tdMap Λ c⟩ := by
  refine ⟨natDegree_le_iff_coeff_eq_zero.2 fun N hN => ?_, natDegree_le_iff_coeff_eq_zero.2 fun N hN => ?_,
    ?_, ?_, ?_, ?_, ?_, ?_⟩
  all_goals first
    | (simp [tdMap, DrP, DpP, coeff_monomial, show (4:ℕ) ≠ N by omega, show (2:ℕ) ≠ N by omega,
        show (1:ℕ) ≠ N by omega, coeff_C, show N ≠ 0 by omega])
    | simp [tdMap, DrP, DpP, coeff_monomial]

theorem tdMap_surj (Λ : ℝ) (PQ : Discrete (ℝ[X] × ℝ[X])) (h : IsTD Λ PQ) :
    tdMap Λ ![PQ.as.1.coeff 2, PQ.as.1.coeff 1, PQ.as.1.coeff 0, PQ.as.2.coeff 1] = PQ.as := by
  obtain ⟨⟨P, Q⟩⟩ := PQ
  obtain ⟨hP, hQ, h4, h4', h3, h3', h2, h0⟩ := h
  simp only at hP hQ h4 h4' h3 h3' h2 h0 ⊢
  refine Prod.ext (Polynomial.ext fun n => ?_) (Polynomial.ext fun n => ?_) <;>
  · rcases n with _ | _ | _ | _ | _ | n <;> simp [tdMap, DrP, DpP, coeff_monomial, *]
    rw [coeff_eq_zero_of_natDegree_lt (by omega)]

theorem tdMap_inj (Λ : ℝ) : Function.Injective (tdMap Λ) := by
  intro c c' h
  have e2 := congrArg (fun PQ : ℝ[X] × ℝ[X] => PQ.1.coeff 2) h
  have e1 := congrArg (fun PQ : ℝ[X] × ℝ[X] => PQ.1.coeff 1) h
  have e0 := congrArg (fun PQ : ℝ[X] × ℝ[X] => PQ.1.coeff 0) h
  have d1 := congrArg (fun PQ : ℝ[X] × ℝ[X] => PQ.2.coeff 1) h
  simp [tdMap, DrP, DpP, coeff_monomial] at e2 e1 e0 d1
  funext i; fin_cases i <;> assumption

/-- ⛭ **`td_essImage`.** The essential image of the Type-D parameter map IS the intrinsic quartic class. -/
theorem td_essImage (Λ : ℝ) : (tdF Λ).essImage = IsTD Λ := by
  funext PQ
  apply propext
  constructor
  · rintro ⟨⟨c⟩, ⟨e⟩⟩
    have h : tdMap Λ c = PQ.as := Discrete.eq_of_hom e.hom
    rw [show PQ = ⟨tdMap Λ c⟩ from Discrete.ext h.symm]; exact tdMap_isTD Λ c
  · intro h
    refine ⟨⟨![PQ.as.1.coeff 2, PQ.as.1.coeff 1, PQ.as.1.coeff 0, PQ.as.2.coeff 1]⟩, ⟨eqToIso ?_⟩⟩
    exact Discrete.ext (tdMap_surj Λ PQ h)

instance (Λ : ℝ) : (tdF Λ).Full where
  map_surjective {_ _} g := ⟨eqToHom (Discrete.ext (tdMap_inj Λ (Discrete.eq_of_hom g))), Subsingleton.elim _ _⟩

instance (Λ : ℝ) : (tdF Λ).Faithful where
  map_injective _ := Subsingleton.elim _ _

instance (Λ : ℝ) : (tdF Λ).toEssImage.IsEquivalence where

/-- ⛭ **`td_equiv`.** The four-parameter space IS the Type-D essential image. -/
noncomputable def td_equiv (Λ : ℝ) : Discrete (Fin 4 → ℝ) ≌ (tdF Λ).EssImageSubcategory :=
  (tdF Λ).toEssImage.asEquivalence

/-- the linear part of the parameter map -/
noncomputable def L : (Fin 4 → ℝ) →ₗ[ℝ] ℝ[X] × ℝ[X] :=
  LinearMap.prod
    ((monomial 2).comp (LinearMap.proj 0) + (monomial 1).comp (LinearMap.proj 1) + (monomial 0).comp (LinearMap.proj 2))
    (-(monomial 2).comp (LinearMap.proj 0) + (monomial 1).comp (LinearMap.proj 3) +
      (monomial 0).comp (LinearMap.proj 2))

noncomputable def base (Λ : ℝ) : ℝ[X] × ℝ[X] := (monomial 4 (-Λ / 3), monomial 4 (-Λ / 3))

theorem tdMap_eq (Λ : ℝ) (c : Fin 4 → ℝ) : tdMap Λ c = base Λ + L c := by
  refine Prod.ext ?_ ?_ <;> simp [tdMap, DrP, DpP, base, L, monomial_neg] <;> abel

/-- ⛭ **`td_dim`.** The class is `base + range L`, with `L` injective, so it has dimension FOUR, not six. -/
theorem td_dim (Λ : ℝ) :
    {PQ : ℝ[X] × ℝ[X] | IsTD Λ ⟨PQ⟩} = {PQ | PQ - base Λ ∈ LinearMap.range L} ∧
      Module.finrank ℝ (LinearMap.range L) = 4 := by
  have hinj : Function.Injective L := fun c c' h => tdMap_inj Λ (by rw [tdMap_eq, tdMap_eq, h])
  refine ⟨Set.ext fun PQ => ⟨fun h => ⟨![PQ.1.coeff 2, PQ.1.coeff 1, PQ.1.coeff 0, PQ.2.coeff 1], ?_⟩, fun ⟨c, hc⟩ => ?_⟩, ?_⟩
  · have : tdMap Λ ![PQ.1.coeff 2, PQ.1.coeff 1, PQ.1.coeff 0, PQ.2.coeff 1] = PQ := tdMap_surj Λ ⟨PQ⟩ h
    rw [tdMap_eq] at this; rw [eq_sub_iff_add_eq, add_comm]; exact this
  · have : tdMap Λ c = PQ := by rw [tdMap_eq, hc]; abel
    rw [Set.mem_ofPred_eq, ← this]; exact tdMap_isTD Λ c
  · rw [LinearMap.finrank_range_of_inj hinj, Module.finrank_fin_fun]

#print axioms td_essImage
#print axioms td_equiv
#print axioms td_dim

/-! ### The strata: dimensions of the isotropy algebras, from Mathlib's indefinite `so'(p,q)` -/

/-- the skew-symmetric matrices on an index type -/
def skew (n : Type) [Fintype n] [DecidableEq n] : Submodule ℝ (Matrix n n ℝ) where
  carrier := {A | Aᵀ = -A}
  add_mem' := by intro A B hA hB; simp only [Set.mem_ofPred_eq] at *; rw [Matrix.transpose_add, hA, hB]; abel
  zero_mem' := by simp
  smul_mem' := by intro c A hA; simp only [Set.mem_ofPred_eq] at *; rw [Matrix.transpose_smul, hA, smul_neg]

/-- strictly upper pairs, ordered through `e : n ≃ Fin k` -/
abbrev Up {n : Type} {k : ℕ} (e : n ≃ Fin k) := {p : n × n // e p.1 < e p.2}

/-- a skew matrix is its strictly upper entries -/
noncomputable def skewEquiv {n : Type} [Fintype n] [DecidableEq n] {k : ℕ} (e : n ≃ Fin k) :
    skew n ≃ₗ[ℝ] (Up e → ℝ) where
  toFun A := fun p => (A : Matrix n n ℝ) p.1.1 p.1.2
  map_add' A B := by ext p; simp
  map_smul' c A := by ext p; simp
  invFun f := ⟨Matrix.of fun i j => if h : e i < e j then f ⟨(i, j), h⟩ else
      if h' : e j < e i then -f ⟨(j, i), h'⟩ else 0, by
    ext i j
    simp only [Matrix.transpose_apply, Matrix.of_apply, Matrix.neg_apply]
    rcases lt_trichotomy (e i) (e j) with h | h | h
    · simp [h, not_lt.mpr h.le]
    · simp [h]
    · simp [h, not_lt.mpr h.le]⟩
  left_inv A := by
    have hA : (A : Matrix n n ℝ)ᵀ = -A := A.2
    ext i j
    simp only [Matrix.of_apply]
    rcases lt_trichotomy (e i) (e j) with h | h | h
    · simp [h]
    · have hij := e.injective h; subst hij
      have := congrFun (congrFun hA i) i
      simp [Matrix.transpose_apply] at this ⊢; linarith
    · have := congrFun (congrFun hA i) j
      simp [Matrix.transpose_apply] at this
      simp [h, not_lt.mpr h.le, this]
  right_inv f := by ext p; simp [p.2]

theorem skew_finrank {n : Type} [Fintype n] [DecidableEq n] {k : ℕ} (e : n ≃ Fin k) :
    Module.finrank ℝ (skew n) = Fintype.card {p : Fin k × Fin k // p.1 < p.2} := by
  rw [(skewEquiv e).finrank_eq, Module.finrank_fintype_fun_eq_card]
  exact Fintype.card_congr (Equiv.subtypeEquiv (e.prodCongr e) fun _ => Iff.rfl)

section so
variable (p q : Type) [Fintype p] [Fintype q] [DecidableEq p] [DecidableEq q]

local notation "η" => LieAlgebra.Orthogonal.indefiniteDiagonal p q ℝ

theorem eta_sq : η * η = 1 := by
  rw [LieAlgebra.Orthogonal.indefiniteDiagonal, diagonal_mul_diagonal, ← diagonal_one]
  congr 1; funext i; cases i <;> simp

omit [Fintype p] [Fintype q] in
theorem eta_t : ηᵀ = η := by rw [LieAlgebra.Orthogonal.indefiniteDiagonal, diagonal_transpose]

theorem mem_so' (A : Matrix (p ⊕ q) (p ⊕ q) ℝ) :
    A ∈ (LieAlgebra.Orthogonal.so' p q ℝ).toSubmodule ↔ Aᵀ * η = η * -A := by
  rw [LieSubalgebra.mem_toSubmodule, LieAlgebra.Orthogonal.so', mem_skewAdjointMatricesLieSubalgebra,
    mem_skewAdjointMatricesSubmodule]; rfl

/-- `A ↦ ηA` carries `so'(p,q)` onto the skew matrices -/
noncomputable def soSkew : (LieAlgebra.Orthogonal.so' p q ℝ).toSubmodule ≃ₗ[ℝ] skew (p ⊕ q) where
  toFun A := ⟨η * (A : Matrix (p ⊕ q) (p ⊕ q) ℝ), by
    have h := (mem_so' p q A).1 A.2
    show (η * (A : Matrix (p ⊕ q) (p ⊕ q) ℝ))ᵀ = -(η * (A : Matrix (p ⊕ q) (p ⊕ q) ℝ))
    rw [transpose_mul, eta_t, h, Matrix.mul_neg]⟩
  invFun B := ⟨η * (B : Matrix (p ⊕ q) (p ⊕ q) ℝ), by
    have h : (B : Matrix (p ⊕ q) (p ⊕ q) ℝ)ᵀ = -(B : Matrix (p ⊕ q) (p ⊕ q) ℝ) := B.2
    rw [mem_so', transpose_mul, eta_t, Matrix.mul_assoc, eta_sq, Matrix.mul_one, h, Matrix.mul_neg,
      ← Matrix.mul_assoc, eta_sq, Matrix.one_mul]⟩
  map_add' A B := by ext1; simp [Matrix.mul_add]
  map_smul' c A := by ext1; simp
  left_inv A := by ext1; simp [← Matrix.mul_assoc, eta_sq]
  right_inv B := by ext1; simp [← Matrix.mul_assoc, eta_sq]

theorem so'_finrank {k : ℕ} (e : p ⊕ q ≃ Fin k) :
    Module.finrank ℝ (LieAlgebra.Orthogonal.so' p q ℝ).toSubmodule = Fintype.card {x : Fin k × Fin k // x.1 < x.2} :=
  ((soSkew p q).finrank_eq).trans (skew_finrank e)

end so

/-- ⛭ **`strata_finrank`.** The receipt's isotropy dimensions, on Mathlib's `so'(p,q)`:
`so(4,1)` is `10` (Type O), `so(2,1) ⊕ so(3)` is `3 + 3 = 6` (Nariai), `ℝ_t ⊕ so(3)` is `1 + 3 = 4`
(generic SdS), inside `so(5,1)` of `15`. -/
theorem strata_finrank :
    Module.finrank ℝ (LieAlgebra.Orthogonal.so' (Fin 4) (Fin 1) ℝ).toSubmodule = 10 ∧
      Module.finrank ℝ ((LieAlgebra.Orthogonal.so' (Fin 2) (Fin 1) ℝ).toSubmodule ×
        (LieAlgebra.Orthogonal.so' (Fin 3) Empty ℝ).toSubmodule) = 6 ∧
      Module.finrank ℝ (ℝ × (LieAlgebra.Orthogonal.so' (Fin 3) Empty ℝ).toSubmodule) = 4 ∧
      Module.finrank ℝ (LieAlgebra.Orthogonal.so' (Fin 5) (Fin 1) ℝ).toSubmodule = 15 := by
  have e3 : Fin 3 ⊕ Empty ≃ Fin 3 := Equiv.sumEmpty _ _
  refine ⟨?_, ?_, ?_, ?_⟩
  · rw [so'_finrank _ _ finSumFinEquiv]; decide
  · rw [Module.finrank_prod, so'_finrank _ _ finSumFinEquiv, so'_finrank _ _ e3]; decide
  · rw [Module.finrank_prod, Module.finrank_self, so'_finrank _ _ e3]; decide
  · rw [so'_finrank _ _ finSumFinEquiv]; decide

#print axioms strata_finrank

end ShadowProbe.Row53Image

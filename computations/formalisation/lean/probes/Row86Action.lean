import Mathlib

/-! # Campaign 50, row 86: the `Z₃` action on loci of the quadric

Receipt: `receipts/P14_matter_sector_paper/P14_is_there_a_singlet_for_the_axis_pair.py`.

- ***The quadric.*** The equatorial section `−X₀² + X₁² + X₂² = α²` (`P14_the_wall_is_a_wall_of_a_hinge.py`), i.e. the
  height rule `X₀² = pow`, `pow = |X|² − α²`. `X = (X₁, X₂)` is real and `X₀` is complex, so the axis pair
  `X₀ = ±iα` is present ("imaginary and NOT absent").
- ***The `Z₃`.*** The rotation by `120°` of the `X`-plane, acting trivially on `X₀`.
- ***The loci.*** The throat circle `|X| = α`; the three walls on it at polar `60°, 180°, 300°`; the three hinges
  antipodal to them at `0°, 120°, 240°` (at any radius `ρ > 0`); the axis `X = 0`.
- ***The branch flip `σ : X₀ ↦ −X₀`*** exchanges the axis pair. -/

namespace ShadowProbe.Row86Action

/-- a point `(X₀, (X₁, X₂))`, `X₀ ∈ ℂ`, `X₁, X₂ ∈ ℝ` -/
abbrev Pt := ℂ × ℝ × ℝ

/-- `s = √3` -/
noncomputable abbrev s : ℝ := Real.sqrt 3

lemma s_sq : s ^ 2 = 3 := Real.sq_sqrt (by norm_num)

lemma s_pos : 0 < s := Real.sqrt_pos.mpr (by norm_num)

/-! ### The rotation and the action -/

/-- the `120°` rotation of the `X`-plane -/
noncomputable def rot (X : ℝ × ℝ) : ℝ × ℝ :=
  (-X.1 / 2 - s / 2 * X.2, s / 2 * X.1 - X.2 / 2)

lemma rot_rot (X : ℝ × ℝ) : rot (rot X) = (-X.1 / 2 + s / 2 * X.2, -(s / 2) * X.1 - X.2 / 2) := by
  have h := s_sq
  obtain ⟨x, y⟩ := X
  simp only [rot, Prod.mk.injEq]
  constructor
  · linear_combination (-x / 4) * h
  · linear_combination (-y / 4) * h

lemma rot3 (X : ℝ × ℝ) : rot (rot (rot X)) = X := by
  have h := s_sq
  rw [rot_rot]
  obtain ⟨x, y⟩ := X
  simp only [rot, Prod.mk.injEq]
  constructor
  · linear_combination (x / 4) * h
  · linear_combination (y / 4) * h

/-- the generator `g` on the total space: rotate `X`, keep `X₀` -/
noncomputable def g (p : Pt) : Pt := (p.1, rot p.2)

lemma g3 : g ∘ g ∘ g = id := by
  funext p; simp [g, rot3]

lemma g_iter_mod (n : ℕ) : g^[n] = g^[n % 3] := by
  conv_lhs => rw [← Nat.mod_add_div n 3, Function.iterate_add, Function.iterate_mul]
  have : g^[3] = id := by simpa [Function.iterate_succ, Function.comp_assoc] using g3
  rw [this, Function.iterate_id, Function.comp_id]

/-- ⛭ the action of `Z₃ = Multiplicative (ZMod 3)`: `k` acts as `g^[k]` -/
noncomputable instance : MulAction (Multiplicative (ZMod 3)) Pt where
  smul k p := g^[(Multiplicative.toAdd k).val] p
  one_smul p := by
    show g^[(0 : ZMod 3).val] p = p
    simp
  mul_smul a b p := by
    show g^[(Multiplicative.toAdd a + Multiplicative.toAdd b).val] p =
      g^[(Multiplicative.toAdd a).val] (g^[(Multiplicative.toAdd b).val] p)
    rw [ZMod.val_add, ← g_iter_mod, ← Function.iterate_add_apply]

/-- the generator of `Z₃` -/
abbrev gen : Multiplicative (ZMod 3) := Multiplicative.ofAdd 1

lemma gen_smul (p : Pt) : gen • p = g p := by
  show g^[(1 : ZMod 3).val] p = g p
  rfl

/-- ⛭ **`action_faithful_order3`.** The generator acts as `g`, `g³ = id`, and `g ≠ id`: the action is faithful of
order exactly `3`. -/
theorem action_faithful_order3 :
    (∀ p : Pt, gen • p = g p) ∧ g ∘ g ∘ g = id ∧ g ≠ id := by
  refine ⟨gen_smul, g3, fun h => ?_⟩
  have := congrArg (fun f => (f ((0 : ℂ), ((1 : ℝ), (0 : ℝ)))).2.1) h
  simp [g, rot] at this
  norm_num at this

/-! ### The quadric -/

/-- `pow = |X|² − α²` -/
def pw (α : ℝ) (X : ℝ × ℝ) : ℝ := X.1 ^ 2 + X.2 ^ 2 - α ^ 2

/-- the quadric `−X₀² + X₁² + X₂² = α²`, i.e. `X₀² = pow` -/
def Q (α : ℝ) : Set Pt := {p | p.1 ^ 2 = ((pw α p.2 : ℝ) : ℂ)}

lemma pw_rot (α : ℝ) (X : ℝ × ℝ) : pw α (rot X) = pw α X := by
  have h := s_sq
  obtain ⟨x, y⟩ := X
  simp only [pw, rot]
  linear_combination (x ^ 2 / 4 + y ^ 2 / 4) * h

/-- ⛭ **`preserves_quadric`.** Every element of `Z₃` maps `Q` onto `Q` (and preserves `pow`). -/
theorem preserves_quadric (α : ℝ) (k : Multiplicative (ZMod 3)) (p : Pt) :
    k • p ∈ Q α ↔ p ∈ Q α := by
  show g^[(Multiplicative.toAdd k).val] p ∈ Q α ↔ p ∈ Q α
  induction (Multiplicative.toAdd k).val generalizing p with
  | zero => rfl
  | succ n ih =>
    rw [Function.iterate_succ_apply, ih]
    simp [Q, g, pw_rot]

/-! ### The loci in the plane -/

/-- the throat circle `|X| = α` (`pow = 0`) -/
def throat (α : ℝ) : Set (ℝ × ℝ) := {X | pw α X = 0}

/-- the three walls, ON the throat, at polar `180°, 300°, 60°` (`j = 0, 1, 2`) -/
noncomputable def wall (α : ℝ) : Fin 3 → ℝ × ℝ
  | 0 => (-α, 0)
  | 1 => (α / 2, -(s / 2) * α)
  | 2 => (α / 2, s / 2 * α)

/-- the three hinges at polar `0°, 120°, 240°`, radius `ρ` -/
noncomputable def hinge (ρ : ℝ) : Fin 3 → ℝ × ℝ
  | 0 => (ρ, 0)
  | 1 => (-ρ / 2, s / 2 * ρ)
  | 2 => (-ρ / 2, -(s / 2) * ρ)

/-- ⛭ **`loci`.** The walls lie on the throat; each wall is ANTIPODAL to its hinge (`wall j = −(α/ρ) hinge j`);
`g` permutes walls and hinges by the same 3-cycle `j ↦ j + 1`; the throat is `g`-stable as a set; and the axis
`X = 0` is fixed. -/
theorem loci (α ρ : ℝ) (hρ : ρ ≠ 0) :
    (∀ j, wall α j ∈ throat α) ∧
    (∀ j, wall α j = (-(α / ρ) * (hinge ρ j).1, -(α / ρ) * (hinge ρ j).2)) ∧
    (∀ j, rot (wall α j) = wall α (j + 1)) ∧
    (∀ j, rot (hinge ρ j) = hinge ρ (j + 1)) ∧
    (∀ X, rot X ∈ throat α ↔ X ∈ throat α) ∧
    rot (0, 0) = (0, 0) := by
  have h := s_sq
  refine ⟨?_, ?_, ?_, ?_, fun X => by simp [throat, pw_rot], by simp [rot]⟩
  · intro j; fin_cases j <;> simp [wall, throat, pw] <;> linear_combination (α ^ 2 / 4) * h
  · intro j; fin_cases j <;> simp [wall, hinge, Prod.ext_iff] <;> (try field_simp) <;> (try simp)
  · intro j; fin_cases j <;> simp [wall, rot, Prod.ext_iff] <;> (try constructor) <;> (try ring_nf) <;>
      (try simp only [h]) <;> (try ring_nf)
  · intro j; fin_cases j <;> simp [hinge, rot, Prod.ext_iff] <;> (try constructor) <;> (try ring_nf) <;>
      (try simp only [h]) <;> (try ring_nf)

/-! ### Fixed points and orbits of the `Z₃` -/

lemma smul_def (k : Multiplicative (ZMod 3)) (p : Pt) : k • p = g^[(Multiplicative.toAdd k).val] p := rfl

lemma rot_fixed_iff (X : ℝ × ℝ) : rot X = X ↔ X = (0, 0) := by
  have h := s_sq
  constructor
  · intro e
    obtain ⟨x, y⟩ := X
    simp only [rot, Prod.mk.injEq] at e ⊢
    obtain ⟨e1, e2⟩ := e
    have hx : x = 0 := by
      have : 12 * x = 0 := by linear_combination (-6) * e1 + (2 * s) * e2 + (-x) * h
      linarith
    subst hx
    refine ⟨rfl, ?_⟩
    linarith
  · rintro rfl; simp [rot]

/-- ⛭ **`orbit_free`.** Off the axis every `X` has three DISTINCT images `X, gX, g²X`. -/
theorem orbit_free (X : ℝ × ℝ) (hX : X ≠ (0, 0)) :
    rot X ≠ X ∧ rot (rot X) ≠ X ∧ rot (rot X) ≠ rot X := by
  have h1 : rot X ≠ X := fun e => hX ((rot_fixed_iff X).mp e)
  refine ⟨h1, fun e => h1 ?_, fun e => h1 ?_⟩
  · calc rot X = rot (rot (rot X)) := by rw [e]
      _ = X := rot3 X
  · have := congrArg (fun Y => rot (rot Y)) e
    simp only [rot3] at this
    exact this

/-- ⛭ **`fixedPoints_eq`.** The `Z₃`-fixed points of the total space are exactly the points over the axis. -/
theorem fixedPoints_eq :
    MulAction.fixedPoints (Multiplicative (ZMod 3)) Pt = {p | p.2 = (0, 0)} := by
  ext p
  simp only [MulAction.mem_fixedPoints, Set.mem_ofPred_eq]
  constructor
  · intro hp
    have := hp gen
    rw [gen_smul] at this
    exact (rot_fixed_iff p.2).mp (congrArg Prod.snd this)
  · intro hp k
    rw [smul_def]
    induction (Multiplicative.toAdd k).val with
    | zero => rfl
    | succ n ih =>
      rw [Function.iterate_succ_apply', ih]
      ext <;> simp [g, hp, rot]

/-- ⛭ **`orbit_three`.** Every point off the axis has a `Z₃`-orbit of exactly three points `{p, gp, g²p}`. -/
theorem orbit_three (p : Pt) (hp : p.2 ≠ (0, 0)) :
    MulAction.orbit (Multiplicative (ZMod 3)) p = {p, g p, g (g p)} ∧
      (MulAction.orbit (Multiplicative (ZMod 3)) p).ncard = 3 := by
  obtain ⟨d1, d2, d3⟩ := orbit_free p.2 hp
  have e : MulAction.orbit (Multiplicative (ZMod 3)) p = {p, g p, g (g p)} := by
    ext q
    simp only [MulAction.mem_orbit_iff, Set.mem_insert_iff, Set.mem_singleton_iff, smul_def]
    constructor
    · rintro ⟨k, rfl⟩
      have hk := (Multiplicative.toAdd k).val_lt
      interval_cases (Multiplicative.toAdd k).val <;> simp
    · rintro (rfl | rfl | rfl)
      · exact ⟨Multiplicative.ofAdd 0, rfl⟩
      · exact ⟨Multiplicative.ofAdd 1, rfl⟩
      · exact ⟨Multiplicative.ofAdd 2, rfl⟩
  refine ⟨e, ?_⟩
  rw [e, Set.ncard_eq_three]
  refine ⟨p, g p, g (g p), ?_, ?_, ?_, rfl⟩
  · intro h; exact d1 (congrArg Prod.snd h).symm
  · intro h; exact d2 (congrArg Prod.snd h).symm
  · intro h; exact d3 (congrArg Prod.snd h).symm

/-- ⛭ **`throat_points_permuted`.** For `α ≠ 0` the throat is `Z₃`-stable but carries no fixed point: each of its
points lies in a free orbit of three, and the walls are ONE such orbit (`wall 0 ↦ wall 1 ↦ wall 2 ↦ wall 0`). -/
theorem throat_points_permuted (α : ℝ) (hα : α ≠ 0) (X : ℝ × ℝ) (hX : X ∈ throat α) :
    rot X ∈ throat α ∧ rot X ≠ X ∧ rot (rot X) ≠ X ∧ rot (rot X) ≠ rot X := by
  have hX0 : X ≠ (0, 0) := by
    rintro rfl; simp [throat, pw] at hX; exact hα hX
  exact ⟨((loci α 1 one_ne_zero).2.2.2.2.1 X).mpr hX, orbit_free X hX0⟩

/-! ### Branches: the height rule `X₀² = pow` over `ℂ` -/

/-- the fibre of the quadric over `X`: the values of `X₀` -/
def fibre (α : ℝ) (X : ℝ × ℝ) : Set ℂ := {z | z ^ 2 = ((pw α X : ℝ) : ℂ)}

/-- the receipt's `_branches`: the number of values of `X₀` -/
noncomputable def branches (α : ℝ) (X : ℝ × ℝ) : ℕ := (fibre α X).ncard

/-- ⛭ **`branches_eq`.** `branches = 1` on the throat (`pow = 0`) and `2` everywhere else. -/
theorem branches_eq (α : ℝ) (X : ℝ × ℝ) : branches α X = if pw α X = 0 then 1 else 2 := by
  unfold branches fibre
  split_ifs with h
  · rw [Set.ncard_eq_one]
    refine ⟨0, ?_⟩
    ext z; simp [h]
  · set c : ℂ := ((pw α X : ℝ) : ℂ)
    have hc : c ≠ 0 := by simpa [c] using h
    obtain ⟨w, hw⟩ := IsAlgClosed.exists_pow_nat_eq c two_pos
    have hw0 : w ≠ 0 := by rintro rfl; apply hc; rw [← hw]; ring
    have hne : w ≠ -w := by intro e; apply hw0; linear_combination e / 2
    have : {z : ℂ | z ^ 2 = c} = {w, -w} := by
      ext z; simp only [Set.mem_ofPred_eq, Set.mem_insert_iff, Set.mem_singleton_iff]
      rw [← hw]; exact sq_eq_sq_iff_eq_or_eq_neg
    rw [this, Set.ncard_pair hne]

/-- ⛭ **`axis_pair`.** Over the axis the fibre is the imaginary pair `{iα, −iα}`, two distinct points for `α ≠ 0`;
and both are FIXED by the `Z₃`. -/
theorem axis_pair (α : ℝ) (hα : α ≠ 0) :
    pw α (0, 0) = -α ^ 2 ∧
    fibre α (0, 0) = {Complex.I * α, -(Complex.I * α)} ∧ Complex.I * α ≠ -(Complex.I * α) ∧
    ∀ k : Multiplicative (ZMod 3), k • ((Complex.I * α, (0, 0)) : Pt) = (Complex.I * α, (0, 0)) ∧
      k • ((-(Complex.I * α), (0, 0)) : Pt) = (-(Complex.I * α), (0, 0)) := by
  have hIa : Complex.I * α ≠ 0 := mul_ne_zero Complex.I_ne_zero (by exact_mod_cast hα)
  refine ⟨by simp [pw], ?_, fun e => hIa (by linear_combination e / 2), fun k => ⟨?_, ?_⟩⟩
  · ext z
    simp only [fibre, Set.mem_ofPred_eq, Set.mem_insert_iff, Set.mem_singleton_iff]
    have : ((pw α (0, 0) : ℝ) : ℂ) = (Complex.I * α) ^ 2 := by
      simp [pw, mul_pow]
    rw [this]; exact sq_eq_sq_iff_eq_or_eq_neg
  · have := fixedPoints_eq ▸ (show ((Complex.I * α, (0, 0)) : Pt) ∈ {p : Pt | p.2 = (0, 0)} from rfl)
    exact this k
  · have := fixedPoints_eq ▸ (show ((-(Complex.I * α), (0, 0)) : Pt) ∈ {p : Pt | p.2 = (0, 0)} from rfl)
    exact this k

/-- the branch flip `σ : X₀ ↦ −X₀` -/
def σ (p : Pt) : Pt := (-p.1, p.2)

/-- ⛭ **`flip`.** `σ` is an involution, preserves the quadric, commutes with the `Z₃`, EXCHANGES the axis pair, and
on the quadric its fixed points are exactly the points over the throat (`X₀ = 0`, `pow = 0`). -/
theorem flip (α : ℝ) (hα : α ≠ 0) :
    (∀ p, σ (σ p) = p) ∧ (∀ p, σ p ∈ Q α ↔ p ∈ Q α) ∧
    (∀ (k : Multiplicative (ZMod 3)) p, k • σ p = σ (k • p)) ∧
    σ (Complex.I * α, (0, 0)) = (-(Complex.I * α), (0, 0)) ∧
    σ (Complex.I * α, (0, 0)) ≠ (Complex.I * α, (0, 0)) ∧
    ∀ p ∈ Q α, σ p = p ↔ p.1 = 0 ∧ p.2 ∈ throat α := by
  have hIa : Complex.I * α ≠ 0 := mul_ne_zero Complex.I_ne_zero (by exact_mod_cast hα)
  refine ⟨fun p => by simp [σ], fun p => by simp [σ, Q], fun k p => ?_, rfl, ?_, fun p hp => ?_⟩
  · rw [smul_def, smul_def]
    induction (Multiplicative.toAdd k).val with
    | zero => rfl
    | succ n ih => rw [Function.iterate_succ_apply', ih, Function.iterate_succ_apply']; rfl
  · intro e; apply hIa; have := congrArg Prod.fst e; simp [σ] at this; linear_combination -this / 2
  · simp only [Q, Set.mem_ofPred_eq] at hp
    simp only [σ, Prod.ext_iff, neg_eq_self, and_true, throat, Set.mem_ofPred_eq]
    constructor
    · intro h0; refine ⟨h0, ?_⟩; rw [h0] at hp
      have : ((pw α p.2 : ℝ) : ℂ) = 0 := by rw [← hp]; ring
      exact_mod_cast this
    · exact fun h => h.1

/-! ### The singlet question -/

/-- a locus is hinge-free when it contains none of the three walls (the colour index) -/
def HingeFree (α : ℝ) (S : Set (ℝ × ℝ)) : Prop := ∀ j, wall α j ∉ S

/-- ⛭ **`singlet_obstructed`** (the receipt's PART 1–4 and its three assertions).
- `branches α = 1`, `branches 2α = 2`, `branches 0 = 2`, and `pow(axis) = −α²`;
- (i) the one-branch locus is EXACTLY the throat;
- (ii) it contains all three walls, so it is NOT hinge-free;
- the walls are one `Z₃`-orbit of three;
- (iii) the `σ`-fixed points of the quadric lie over the one-branch locus, so over the walls' circle;
- and no point is both one-branch and `Z₃`-fixed: the only `Z₃`-fixed `X` is the axis, which has two branches. -/
theorem singlet_obstructed (α : ℝ) (hα : 0 < α) :
    branches α (α, 0) = 1 ∧ branches α (2 * α, 0) = 2 ∧ branches α (0, 0) = 2 ∧ pw α (0, 0) = -α ^ 2 ∧
    {X | branches α X = 1} = throat α ∧
    ¬ HingeFree α {X | branches α X = 1} ∧
    (∀ j, rot (wall α j) = wall α (j + 1)) ∧ wall α 0 ≠ wall α 1 ∧ wall α 0 ≠ wall α 2 ∧ wall α 1 ≠ wall α 2 ∧
    (∀ p ∈ Q α, σ p = p → branches α p.2 = 1) ∧
    (∀ X, branches α X = 1 → rot X ≠ X) := by
  have ha : α ≠ 0 := hα.ne'
  have hs := s_pos
  have one_iff : ∀ X, branches α X = 1 ↔ X ∈ throat α := by
    intro X; rw [branches_eq]; split_ifs with h <;> simp [throat, h]
  have L := loci α 1 one_ne_zero
  refine ⟨?_, ?_, ?_, by simp [pw], Set.ext one_iff, ?_, L.2.2.1, ?_, ?_, ?_, ?_, ?_⟩
  · rw [branches_eq]; simp [pw]
  · rw [branches_eq]; simp [pw]; intro h; nlinarith
  · rw [branches_eq]; simp [pw, ha]
  · intro hf; exact hf 0 ((one_iff _).mpr (L.1 0))
  · simp [wall, Prod.ext_iff]; intro h; linarith
  · simp [wall, Prod.ext_iff]; intro h; linarith
  · simp [wall, Prod.ext_iff]; intro h; nlinarith [mul_pos hs hα]
  · intro p hp hfix; exact (one_iff _).mpr (((flip α ha).2.2.2.2.2 p hp).mp hfix).2
  · intro X hX; exact (throat_points_permuted α ha X ((one_iff X).mp hX)).2.1

end ShadowProbe.Row86Action

#print axioms ShadowProbe.Row86Action.action_faithful_order3
#print axioms ShadowProbe.Row86Action.preserves_quadric
#print axioms ShadowProbe.Row86Action.loci
#print axioms ShadowProbe.Row86Action.orbit_free
#print axioms ShadowProbe.Row86Action.fixedPoints_eq
#print axioms ShadowProbe.Row86Action.orbit_three
#print axioms ShadowProbe.Row86Action.throat_points_permuted
#print axioms ShadowProbe.Row86Action.branches_eq
#print axioms ShadowProbe.Row86Action.axis_pair
#print axioms ShadowProbe.Row86Action.flip
#print axioms ShadowProbe.Row86Action.singlet_obstructed

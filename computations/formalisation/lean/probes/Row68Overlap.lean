import ShadowEngine

namespace ShadowProbe

namespace R68Overlap

open Finset Real

/-! ### A -/

/-- the integer shapes of the five basis elements -/
def Nm : Fin 5 → Fin 3 → Fin 3 → ℤ :=
  ![![![0, 1, 0], ![1, 0, 0], ![0, 0, 0]],
    ![![0, 0, 1], ![0, 0, 0], ![1, 0, 0]],
    ![![0, 0, 0], ![0, 0, 1], ![0, 1, 0]],
    ![![1, 0, 0], ![0, -1, 0], ![0, 0, 0]],
    ![![1, 0, 0], ![0, 1, 0], ![0, 0, -2]]]

/-- the normalisations `2, 2, 2, 2, 6` under the square roots -/
def den : Fin 5 → ℕ := ![2, 2, 2, 2, 6]

/-- the receipt's basis: `h_k = (1/√den_k) · N_k` -/
noncomputable def h (k : Fin 5) : Matrix (Fin 3) (Fin 3) ℝ :=
  Matrix.of fun i j => 1 / Real.sqrt (den k) * (Nm k i j : ℝ)

theorem h_mul (k : Fin 5) (a b c d : Fin 3) :
    h k a b * h k c d = 1 / (den k : ℝ) * ((Nm k a b : ℝ) * (Nm k c d : ℝ)) := by
  have hpos : (0 : ℝ) < den k := by fin_cases k <;> norm_num [den]
  have hs := Real.sq_sqrt hpos.le
  have hne : Real.sqrt (den k) ≠ 0 := (Real.sqrt_pos.2 hpos).ne'
  simp only [h, Matrix.of_apply]
  field_simp
  rw [hs]; ring

/-- the projector onto symmetric traceless tensors -/
noncomputable def P (a b c d : Fin 3) : ℝ :=
  1 / 2 * ((if a = c then 1 else 0) * (if b = d then 1 else 0) + (if a = d then 1 else 0) * (if b = c then 1 else 0))
    - 1 / 3 * ((if a = b then 1 else 0) * (if c = d then 1 else 0))

theorem completeness (a b c d : Fin 3) : ∑ k, h k a b * h k c d = P a b c d := by
  simp only [h_mul]
  fin_cases a <;> fin_cases b <;> fin_cases c <;> fin_cases d <;>
    norm_num [Fin.sum_univ_five, Nm, den, P]

theorem traceless (k : Fin 5) : Matrix.trace (h k) = 0 := by
  fin_cases k <;> simp [Matrix.trace, Fin.sum_univ_three, h, Nm]
  ring

theorem orthonormal (k l : Fin 5) :
    ∑ i, ∑ j, h k i j * h l i j = if k = l then 1 else 0 := by
  have h2 : Real.sqrt 2 ^ 2 = 2 := Real.sq_sqrt (by norm_num)
  have h6 : Real.sqrt 6 ^ 2 = 6 := Real.sq_sqrt (by norm_num)
  have n2 : Real.sqrt 2 ≠ 0 := by positivity
  have n6 : Real.sqrt 6 ≠ 0 := by positivity
  fin_cases k <;> fin_cases l <;>
    simp [Fin.sum_univ_three, h, Nm, den] <;> field_simp <;> (try rw [h2]) <;> (try rw [h6]) <;> norm_num

theorem trace_P : ∑ a, ∑ b, P a b a b = 5 := by
  norm_num [Fin.sum_univ_three, P]

theorem norms (k : Fin 5) : Matrix.trace (h k * h k) = 1 := by
  have := orthonormal k k
  simp only [ite_true] at this
  rw [← this, Matrix.trace]
  refine Finset.sum_congr rfl fun i _ => ?_
  simp only [Matrix.diag, Matrix.mul_apply]
  refine Finset.sum_congr rfl fun j _ => ?_
  have hs : h k j i = h k i j := by
    fin_cases k <;> fin_cases i <;> fin_cases j <;> simp [h, Nm]
  rw [hs]

/-- IMPORTED: the degeneracy `d(m) = 2(m² − 4)` of the TT rank-two harmonics on `S³` (both chiralities) -/
def dm (m : ℝ) : ℝ := 2 * (m ^ 2 - 4)

theorem level_three : (∑ k, Matrix.trace (h k * h k)) = 5 ∧ 2 * (∑ k, Matrix.trace (h k * h k)) = 10 ∧
    2 * (∑ k, Matrix.trace (h k * h k)) = dm 3 := by
  simp only [norms]; norm_num [dm]

open Classical in
theorem drop_one :
    ¬ (∀ a b c d : Fin 3, ∑ k : Fin 4, h k.castSucc a b * h k.castSucc c d = P a b c d) ∧
    (Finset.univ.filter (fun t : Fin 3 × Fin 3 × Fin 3 × Fin 3 =>
        ∑ k : Fin 4, h k.castSucc t.1 t.2.1 * h k.castSucc t.2.2.1 t.2.2.2 ≠ P t.1 t.2.1 t.2.2.1 t.2.2.2)).card = 9 ∧
    ∑ k : Fin 4, Matrix.trace (h k.castSucc * h k.castSucc) = 4 := by
  have key : ∀ a b c d : Fin 3, ∑ k : Fin 4, h k.castSucc a b * h k.castSucc c d
      = P a b c d - 1 / 6 * ((Nm 4 a b : ℝ) * (Nm 4 c d : ℝ)) := by
    intro a b c d
    rw [← completeness]
    simp only [Fin.sum_univ_five, Fin.sum_univ_four, h_mul]
    simp [den]
  refine ⟨fun hall => ?_, ?_, ?_⟩
  · have := hall 0 0 0 0
    rw [key] at this
    norm_num [Nm] at this
  · rw [Finset.filter_congr (q := fun t : Fin 3 × Fin 3 × Fin 3 × Fin 3 =>
        Nm 4 t.1 t.2.1 * Nm 4 t.2.2.1 t.2.2.2 ≠ 0)]
    · decide
    · intro t _
      rw [key]
      constructor
      · intro hne hz; apply hne; rw [show ((Nm 4 t.1 t.2.1 : ℝ) * Nm 4 t.2.2.1 t.2.2.2) = 0 by exact_mod_cast hz]; ring
      · intro hz he
        apply hz
        have : ((Nm 4 t.1 t.2.1 * Nm 4 t.2.2.1 t.2.2.2 : ℤ) : ℝ) = 0 := by push_cast; linarith
        exact_mod_cast this
  · simp only [norms]; norm_num

/-! ### B -/

/-- the level-summed overlap, with the pure number `c` and the volume `V = 2π²` -/
noncomputable def Sigma (c m m' : ℝ) : ℝ := dm m * dm m' * c / (2 * π ^ 2)

/-- `r6998`'s rate exponent `6 − 2s` -/
def rate (s : ℝ) : ℝ := 6 - 2 * s

theorem exponent_zero (c : ℝ) :
    (∀ m m', dm m ≠ 0 → dm m' ≠ 0 → Sigma c m m' / (dm m * dm m') = c / (2 * π ^ 2)) ∧
    rate 0 = 6 ∧ (∀ s, rate s = 0 ↔ s = 3) ∧ rate 4 < 0 ∧ (∀ s, 3 < s → rate s < 0) ∧
    dm 3 = 10 ∧ dm 4 = 24 ∧ dm 3 < dm 4 := by
  refine ⟨fun m m' h1 h2 => ?_, by norm_num [rate], fun s => ?_, by norm_num [rate],
    fun s hs => by unfold rate; linarith, by norm_num [dm], by norm_num [dm], by norm_num [dm]⟩
  · unfold Sigma; field_simp
  · unfold rate; constructor <;> intro h <;> linarith

/-! ### D -/

/-- the frame metric `η = diag(−1, 1, 1, 1)`, as its diagonal -/
def eta : Fin 4 → ℝ := ![-1, 1, 1, 1]

theorem eta_sq (a : Fin 4) : eta a * eta a = 1 := by fin_cases a <;> norm_num [eta]

/-- `η_{ab}` -/
def g (a b : Fin 4) : ℝ := if a = b then eta a else 0

/-- `R_{abcd} = K(η_ac η_bd − η_ad η_bc)` -/
def Rl (K : ℝ) (a b c d : Fin 4) : ℝ := K * (g a c * g b d - g a d * g b c)

/-- `R^{ab}{}_{cd}` (the receipt's `mix`) -/
def mix (K : ℝ) (a b c d : Fin 4) : ℝ := eta a * eta b * Rl K a b c d

/-- `δ` -/
def δ (a b : Fin 4) : ℝ := if a = b then 1 else 0

theorem mix_eq (K : ℝ) (a b c d : Fin 4) :
    mix K a b c d = K * (δ a c * δ b d - δ a d * δ b c) := by
  have e : ∀ x y : Fin 4, eta x * g x y = δ x y := fun x y => by
    unfold g δ; split_ifs with hxy
    · subst hxy; exact eta_sq x
    · ring
  have : mix K a b c d = K * ((eta a * g a c) * (eta b * g b d) - (eta a * g a d) * (eta b * g b c)) := by
    unfold mix Rl; ring
  rw [this, e, e, e, e]

/-- the contraction lemma: `R^{ab}{}_{cd} Y^{cd} = K(Y^{ab} − Y^{ba})` -/
theorem contract (K : ℝ) (a b : Fin 4) (Y : Fin 4 → Fin 4 → ℝ) :
    ∑ c, ∑ d, mix K a b c d * Y c d = K * (Y a b - Y b a) := by
  simp only [mix_eq, δ, mul_sub, sub_mul, Finset.sum_sub_distrib, ite_mul, zero_mul, mul_ite,
    mul_one, mul_zero]
  simp [Finset.sum_ite_eq]

theorem mix_anti (K : ℝ) (a b c d : Fin 4) : mix K b a c d = - mix K a b c d := by
  rw [mix_eq, mix_eq]; ring

theorem mix_mix (K : ℝ) (a b e f : Fin 4) :
    ∑ c, ∑ d, mix K a b c d * mix K c d e f = 2 * K * mix K a b e f := by
  rw [contract K a b (fun c d => mix K c d e f), mix_anti]; ring

theorem diag_sum (K : ℝ) : ∑ a, ∑ b, mix K a b a b = 12 * K := by
  simp [mix_eq, δ, Fin.sum_univ_four]; ring

/-- `R_{bd} = Σ_a η^{aa} R_{abad}` -/
def Ric (K : ℝ) (b d : Fin 4) : ℝ := ∑ a, eta a * Rl K a b a d
/-- `R = Σ_i η^{ii} R_{ii}` -/
def Rs (K : ℝ) : ℝ := ∑ i, eta i * Ric K i i
/-- `R^{ij}` -/
def Ru (K : ℝ) (i j : Fin 4) : ℝ := eta i * eta j * Ric K i j
/-- `R^a{}_b`, as a matrix -/
def Rm (K : ℝ) : Matrix (Fin 4) (Fin 4) ℝ := Matrix.of fun a b => eta a * Ric K a b
/-- `Riem² = R_{abcd} R^{abcd}` -/
def Riem2 (K : ℝ) : ℝ :=
  ∑ a, ∑ b, ∑ c, ∑ d, Rl K a b c d * eta a * eta b * eta c * eta d * Rl K a b c d
/-- `Ric² = R_{ij} R^{ij}` -/
def RicRic (K : ℝ) : ℝ := ∑ i, ∑ j, Ric K i j * Ru K i j
/-- `Riem³ = R^{ab}{}_{cd} R^{cd}{}_{ef} R^{ef}{}_{ab}` (the receipt's `I7`) -/
def I7 (K : ℝ) : ℝ :=
  ∑ a, ∑ b, ∑ c, ∑ d, ∑ e, ∑ f, mix K a b c d * mix K c d e f * mix K e f a b
/-- the `Riem⁴` chain -/
def chain (K : ℝ) : ℝ :=
  ∑ a, ∑ b, ∑ c, ∑ d, ∑ e, ∑ f, ∑ g', ∑ h',
    mix K a b c d * mix K c d e f * mix K e f g' h' * mix K g' h' a b

theorem lower_eq (K : ℝ) (a b c d : Fin 4) : eta c * eta d * Rl K a b c d = mix K a b c d := by
  have e : ∀ x y : Fin 4, eta y * g x y = δ x y := fun x y => by
    unfold g δ; split_ifs with hxy
    · subst hxy; exact eta_sq x
    · ring
  have : eta c * eta d * Rl K a b c d =
      K * ((eta c * g a c) * (eta d * g b d) - (eta d * g a d) * (eta c * g b c)) := by
    unfold Rl; ring
  rw [this, e, e, e, e, mix_eq]

theorem Ric_eq (K : ℝ) (b d : Fin 4) : Ric K b d = 3 * K * g b d := by
  fin_cases b <;> fin_cases d <;> simp [Ric, Rl, g, eta, Fin.sum_univ_four] <;> ring

theorem Rs_eq (K : ℝ) : Rs K = 12 * K := by
  simp [Rs, Ric_eq, g, eta, Fin.sum_univ_four]; ring

theorem RicRic_eq (K : ℝ) : RicRic K = 36 * K ^ 2 := by
  simp [RicRic, Ru, Ric_eq, g, eta, Fin.sum_univ_four]; ring

theorem Riem2_eq (K : ℝ) : Riem2 K = 24 * K ^ 2 := by
  have : Riem2 K = ∑ a, ∑ b, ∑ c, ∑ d, mix K a b c d * mix K a b c d := by
    unfold Riem2
    refine Finset.sum_congr rfl fun a _ => Finset.sum_congr rfl fun b _ =>
      Finset.sum_congr rfl fun c _ => Finset.sum_congr rfl fun d _ => ?_
    rw [show mix K a b c d * mix K a b c d =
      (eta a * eta b * Rl K a b c d) * (eta c * eta d * Rl K a b c d) by rw [lower_eq]; rfl]
    ring
  rw [this]
  simp only [contract]
  simp [mix_eq, δ, Fin.sum_univ_four]; ring

theorem Rm_eq (K : ℝ) : Rm K = (3 * K) • (1 : Matrix (Fin 4) (Fin 4) ℝ) := by
  ext a b
  have : eta a * g a b = δ a b := by
    unfold g δ; split_ifs with hab
    · subst hab; exact eta_sq a
    · ring
  simp only [Rm, Matrix.of_apply, Ric_eq, Matrix.smul_apply, Matrix.one_apply, smul_eq_mul]
  rw [show eta a * (3 * K * g a b) = 3 * K * (eta a * g a b) by ring, this, δ]

theorem trRm4 (K : ℝ) : Matrix.trace (Rm K * Rm K * Rm K * Rm K) = 324 * K ^ 4 := by
  rw [Rm_eq]; simp [smul_smul, Matrix.trace_smul]; ring

theorem trRm3 (K : ℝ) : Matrix.trace (Rm K * Rm K * Rm K) = 108 * K ^ 3 := by
  rw [Rm_eq]; simp [smul_smul, Matrix.trace_smul]; ring

theorem I7_eq (K : ℝ) : I7 K = 48 * K ^ 3 := by
  have : I7 K = ∑ a, ∑ b, ∑ c, ∑ d, mix K a b c d * ∑ e, ∑ f, mix K c d e f * mix K e f a b := by
    simp only [I7, Finset.mul_sum, mul_assoc]
  rw [this]
  simp only [contract]
  simp [mix_eq, δ, Fin.sum_univ_four]; ring

theorem chain_eq (K : ℝ) : chain K = 96 * K ^ 4 := by
  have : chain K = ∑ a, ∑ b, ∑ c, ∑ d, mix K a b c d *
      ∑ e, ∑ f, mix K c d e f * ∑ g', ∑ h', mix K e f g' h' * mix K g' h' a b := by
    simp only [chain, Finset.mul_sum, mul_assoc]
  rw [this]
  simp only [contract]
  simp [mix_eq, δ, Fin.sum_univ_four]; ring

/-- the receipt's ten dimension-eight invariants, in its order -/
noncomputable def eight (K : ℝ) : Fin 10 → ℝ :=
  ![Rs K ^ 4, Rs K ^ 2 * RicRic K, Rs K ^ 2 * Riem2 K, RicRic K ^ 2, Riem2 K ^ 2, RicRic K * Riem2 K,
    Matrix.trace (Rm K * Rm K * Rm K * Rm K), Rs K * Matrix.trace (Rm K * Rm K * Rm K), Rs K * I7 K, chain K]

/-- the receipt's printed ratios to `Λ⁴` -/
def ratios : Fin 10 → ℚ := ![256, 64, 128 / 3, 16, 64 / 9, 32 / 3, 4, 16, 64 / 9, 32 / 27]

/-- ⛭ **`eight_values`.** At `K = Λ/3` each of the ten is exactly its rational times `Λ⁴` -/
theorem eight_values (Λ : ℝ) (i : Fin 10) : eight (Λ / 3) i = (ratios i : ℝ) * Λ ^ 4 := by
  fin_cases i <;>
    simp [eight, ratios, Rs_eq, RicRic_eq, Riem2_eq, trRm4, trRm3, I7_eq, chain_eq] <;> ring

theorem ratios_ne_zero (i : Fin 10) : ratios i ≠ 0 := by
  fin_cases i <;> norm_num [ratios]

/-- **`eight_homogeneous`.** each, as a function of `Λ`, satisfies `Λ f'(Λ) = 4 f(Λ)` -/
theorem eight_homogeneous (Λ : ℝ) (i : Fin 10) :
    deriv (fun L => eight (L / 3) i) Λ * Λ = 4 * eight (Λ / 3) i := by
  simp only [eight_values]
  rw [deriv_const_mul _ (differentiableAt_pow 4)]
  simp; ring

/-- **`value_rank_one`.** the ten values span a one-dimensional `ℚ`-space -/
theorem value_rank_one : Module.finrank ℚ (Submodule.span ℚ {ratios}) = 1 :=
  finrank_span_singleton (fun h => ratios_ne_zero 0 (by rw [h]; rfl))

/-- homogeneity of `Λᵏ`, `k = 3, …, 6` (the receipt's every-dimension check, for all `k`) -/
theorem pow_homogeneous (k : ℕ) (Λ : ℝ) :
    deriv (fun L : ℝ => L ^ (k + 1)) Λ * Λ = ((k + 1 : ℕ) : ℝ) * Λ ^ (k + 1) := by
  rw [deriv_pow_field]; simp only [Nat.add_sub_cancel]; ring

theorem pow_homogeneous_3_to_6 (Λ : ℝ) : ∀ k ∈ ({3, 4, 5, 6} : Finset ℕ),
    deriv (fun L : ℝ => L ^ k) Λ * Λ = (k : ℝ) * Λ ^ k := by
  intro k hk
  simp only [Finset.mem_insert, Finset.mem_singleton] at hk
  rcases hk with rfl | rfl | rfl | rfl
  · exact pow_homogeneous 2 Λ
  · exact pow_homogeneous 3 Λ
  · exact pow_homogeneous 4 Λ
  · exact pow_homogeneous 5 Λ

/-- **`combo_homogeneous`.** any rational combination of the ten is `(Σ cᵢ rᵢ) Λ⁴`, so homogeneous of degree 4 -/
theorem combo_homogeneous (c : Fin 10 → ℚ) (Λ : ℝ) :
    ∑ i, (c i : ℝ) * eight (Λ / 3) i = ((∑ i, c i * ratios i : ℚ) : ℝ) * Λ ^ 4 ∧
    deriv (fun L => ∑ i, (c i : ℝ) * eight (L / 3) i) Λ * Λ = 4 * ∑ i, (c i : ℝ) * eight (Λ / 3) i := by
  have hv : ∀ L : ℝ, ∑ i, (c i : ℝ) * eight (L / 3) i = ((∑ i, c i * ratios i : ℚ) : ℝ) * L ^ 4 := by
    intro L; simp only [eight_values]; push_cast; rw [Finset.sum_mul]
    exact Finset.sum_congr rfl fun i _ => by ring
  refine ⟨hv Λ, ?_⟩
  simp only [hv]
  rw [deriv_const_mul _ (differentiableAt_pow 4)]
  simp; ring

/-! ### E -/

theorem trivia : Real.log 2 ≠ 0 ∧ deriv (fun _ : ℝ => Real.log 2) 1 = 0 ∧ (3 : ℕ) > 2 ∧ (2 : ℕ) > 1 := by
  refine ⟨?_, by simp, by norm_num, by norm_num⟩
  exact (Real.log_pos (by norm_num)).ne'

/-! ### C -/

/-- occupation numbers of the three modes -/
abbrev Occ := Fin 3 → ℕ
/-- a state: its coefficient on each number basis vector `|n₀ n₁ n₂⟩` (zero off the box) -/
abbrev St := Occ → ℝ

/-- the unit occupation vector of mode `i` -/
def e (i : Fin 3) : Occ := fun j => if j = i then 1 else 0

section ladder

-- which levels a mode keeps: `ok k ↔ k < 5` is the receipt's truncation, `ok = True` the full ladder
variable (ok : ℕ → Prop) [DecidablePred ok]

/-- the box of kept occupations (for `ok k ↔ k < 5`, the receipt's `125`-dimensional space) -/
def inBox (n : Occ) : Prop := ok (n 0) ∧ ok (n 1) ∧ ok (n 2)

instance (n : Occ) : Decidable (inBox ok n) := by unfold inBox; infer_instance

/-- the lowering operator `aᵢ`: `(aψ)(n) = √(nᵢ+1) ψ(n+eᵢ)`, when `n` and `n + eᵢ` are kept -/
noncomputable def lower (i : Fin 3) (ψ : St) : St :=
  fun n => if inBox ok n ∧ ok (n i + 1) then Real.sqrt (n i + 1) * ψ (n + e i) else 0

/-- the raising operator `aᵢ†`: `(a†ψ)(n) = √nᵢ ψ(n−eᵢ)` for `nᵢ ≥ 1`, when `n` is kept -/
noncomputable def raise (i : Fin 3) (ψ : St) : St :=
  fun n => if inBox ok n ∧ 0 < n i then Real.sqrt (n i) * ψ (n - e i) else 0

/-- `1/√(2wᵢ)` -/
noncomputable def cc (w : Fin 3 → ℝ) (i : Fin 3) : ℝ := (Real.sqrt (2 * w i))⁻¹

/-- `qᵢ = (aᵢ + aᵢ†)/√(2wᵢ)` -/
noncomputable def q (w : Fin 3 → ℝ) (i : Fin 3) (ψ : St) : St :=
  fun n => cc w i * (lower ok i ψ n + raise ok i ψ n)

/-- the vacuum `|000⟩` -/
def vac : St := fun n => if n 0 = 0 ∧ n 1 = 0 ∧ n 2 = 0 then 1 else 0

/-- `⟨0|qᵢ qⱼ|0⟩` (pairing with `⟨0|` is reading the coefficient at `n = 0`) -/
noncomputable def vev2 (w : Fin 3 → ℝ) (i j : Fin 3) : ℝ := q ok w i (q ok w j vac) 0

/-- `⟨0|q_A q_B q_C q_D|0⟩` -/
noncomputable def vev4 (w : Fin 3 → ℝ) (A B C D : Fin 3) : ℝ :=
  q ok w A (q ok w B (q ok w C (q ok w D vac))) 0

end ladder

/-- the free two-point function the Wick sum is built from -/
noncomputable def W (w : Fin 3 → ℝ) (i j : Fin 3) : ℝ := if i = j then 1 / (2 * w i) else 0

theorem cc_sq (w : Fin 3 → ℝ) (hw : ∀ i, 0 < w i) (i : Fin 3) : cc w i ^ 2 = 1 / (2 * w i) := by
  have := hw i
  rw [cc, inv_pow, Real.sq_sqrt (by positivity), one_div]

theorem W_cc (w : Fin 3 → ℝ) (hw : ∀ i, 0 < w i) (i j : Fin 3) :
    W w i j = if i = j then cc w i ^ 2 else 0 := by
  rw [W, cc_sq w hw]

section ladder

variable (ok : ℕ → Prop) [DecidablePred ok]

/-- ⛭ **`two_point`.** `⟨0|qᵢqⱼ|0⟩ = δᵢⱼ/(2wᵢ)`: diagonal, computed from the mode operators.
Any truncation keeping levels `0, 1` will do. -/
theorem two_point (h0 : ok 0) (h1 : ok 1) (w : Fin 3 → ℝ) (hw : ∀ i, 0 < w i) (i j : Fin 3) :
    vev2 ok w i j = W w i j := by
  rw [W_cc w hw]
  fin_cases i <;> fin_cases j <;> simp [vev2, q, lower, raise, vac, inBox, e, h0, h1] <;> ring

/-- ⛭ **`wick`.** all `81` quartic vacuum expectations equal the Wick sum exactly.
Any truncation keeping levels `0, 1, 2` will do: the receipt's five levels, and the full ladder. -/
theorem wick (h0 : ok 0) (h1 : ok 1) (h2 : ok 2) (w : Fin 3 → ℝ) (hw : ∀ i, 0 < w i) (A B C D : Fin 3) :
    vev4 ok w A B C D = W w A B * W w C D + W w A C * W w B D + W w A D * W w B C := by
  have s2 : Real.sqrt 2 ^ 2 = 2 := Real.sq_sqrt (by norm_num)
  simp only [W_cc w hw]
  fin_cases A <;> fin_cases B <;> fin_cases C <;> fin_cases D <;>
    simp [vev4, q, lower, raise, vac, inBox, e, h0, h1, h2] <;>
    (ring_nf; try simp only [s2]; try ring_nf)

end ladder

/-- the receipt's truncation: five levels per mode -/
def trunc5 (k : ℕ) : Prop := k < 5

instance : DecidablePred trunc5 := fun k => by unfold trunc5; infer_instance

/-- ⛭ **`wick_receipt`.** the receipt's computation itself (five levels per mode, `125` states), and the same on
the untruncated ladder: two-point functions diagonal and `1/(2w)`, every quartic equal to its Wick sum -/
theorem wick_receipt (w : Fin 3 → ℝ) (hw : ∀ i, 0 < w i) :
    (∀ i j, vev2 trunc5 w i j = W w i j) ∧
    (∀ A B C D, vev4 trunc5 w A B C D = W w A B * W w C D + W w A C * W w B D + W w A D * W w B C) ∧
    (∀ i j, vev2 (fun _ => True) w i j = W w i j) ∧
    (∀ A B C D, vev4 (fun _ => True) w A B C D =
      W w A B * W w C D + W w A C * W w B D + W w A D * W w B C) := by
  refine ⟨two_point _ ?_ ?_ w hw, wick _ ?_ ?_ ?_ w hw, two_point _ trivial trivial w hw,
    wick _ trivial trivial trivial w hw⟩ <;> norm_num [trunc5]

/-- ⛭ **`support`.** a non-zero quartic is supported on one or two distinct labels, never three or four;
both one and two occur -/
theorem support (w : Fin 3 → ℝ) (hw : ∀ i, 0 < w i) :
    (∀ A B C D, vev4 trunc5 w A B C D ≠ 0 → ({A, B, C, D} : Finset (Fin 3)).card ∈ ({1, 2} : Finset ℕ)) ∧
    vev4 trunc5 w 0 0 0 0 ≠ 0 ∧ ({0, 0, 0, 0} : Finset (Fin 3)).card = 1 ∧
    vev4 trunc5 w 0 0 1 1 ≠ 0 ∧ ({0, 0, 1, 1} : Finset (Fin 3)).card = 2 := by
  have h3 := (wick_receipt w hw).2.1
  have hpos : ∀ i, 0 < W w i i := fun i => by have := hw i; simp [W]; positivity
  have hW : ∀ i j, W w i j ≠ 0 → i = j := fun i j h => by by_contra hij; simp [W, hij] at h
  have comb : ∀ A B C D : Fin 3, (A = B ∧ C = D) ∨ (A = C ∧ B = D) ∨ (A = D ∧ B = C) →
      ({A, B, C, D} : Finset (Fin 3)).card ∈ ({1, 2} : Finset ℕ) := by decide
  refine ⟨fun A B C D hne => comb A B C D ?_, ?_, by decide, ?_, by decide⟩
  · rw [h3] at hne
    by_contra hc
    simp only [not_or, not_and_or] at hc
    apply hne
    have z : ∀ i j, i ≠ j → W w i j = 0 := fun i j hij => by_contra fun h => hij (hW i j h)
    clear hne h3 comb hpos hW
    rcases hc with ⟨hab | hcd, hac | hbd, had | hbc⟩ <;> simp [*]
  · rw [h3]; have := hpos 0; positivity
  · rw [h3]; have := hpos 0; have := hpos 1
    simp only [W, ite_true, show (0 : Fin 3) ≠ 1 by decide, ite_false, mul_zero, add_zero]
    have := hw 0; have := hw 1; positivity

/-- **`factorises`.** the two-label term is a product of two single-label moments -/
theorem factorises (w : Fin 3 → ℝ) (hw : ∀ i, 0 < w i) :
    vev2 trunc5 w 0 0 * vev2 trunc5 w 1 1 = 1 / (4 * w 0 * w 1) := by
  rw [(wick_receipt w hw).1, (wick_receipt w hw).1]
  have := hw 0; have := hw 1
  simp [W]; field_simp; ring

end R68Overlap

end ShadowProbe

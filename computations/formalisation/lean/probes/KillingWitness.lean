import Mathlib

/-!
# Probe of `r7645+71.2` (campaign 82, `r7645`): the owed witness for `lem:killing` and `cor:stationary`

Registered target: `computations/formalisation/r7645_71_campaign82/PREDICTION.md`.
Base: campaign 59's `probes/KillingHorizon.lean`, copied verbatim (prefix `kh_` → `kw_`, namespace
`ShadowProbe.KillingWitnessProbe`); the witness section is new.

**Status: BUILT.** Both registered witnesses are exhibited, not only implied.

* `kw_lemma_killing_witness`: the concrete chart `kw_chart` (`n = 1`, `E = ℝ`, points `(λ, x) ∈ ℝ × ℝ`)
  with constant metric `ds² = 2 dλ dx` (Minkowski `1+1` in light-cone form), `x₀ = 0`,
  `p = (0,0) ≠ q = (1,0)`, and `MetricallyCoincident kw_chart p q`, obtained from `kw_lemma_killing`
  after proving its `hnull` hypothesis (`kw_hnull`: `χ = ∂_λ` is null, `g(χ,χ) = g₀₀ = 0`).
* `kw_cor_stationary_witness`: `X = {0}` (the null line `x = 0`, the `1+1` null hyperplane),
  `H = unionOfOrbits X` non-empty, a `Rigidity 1 H` instance built from `kw_chart`, the full conclusion
  of `kw_cor_stationary` for this `H`, and the concrete pair `(0,0), (1,0) ∈ H` metrically coincident
  under the chart that the corollary returns.

**Nondegeneracy check (the witness is genuinely Lorentzian).** The structure `KillingChart` imposes
only symmetry and `λ`-independence — no nondegeneracy and no signature. So the **zero metric satisfies
every hypothesis trivially**: `kw_zero_rigidity` proves `Rigidity 1 Set.univ` from `g ≡ 0`, which is why
a witness by itself proves nothing unless it is checked non-degenerate. Our witness is not the zero
metric: `kw_lightCone_det` (`det = -1 ≠ 0`), `kw_timelike` (`ds²(1,-1) = -2 < 0`), `kw_spacelike`
(`ds²(1,1) = 2 > 0`), `kw_orth` (those two are `g`-orthogonal), packaged as `kw_lorentzian`: an
orthogonal basis with one negative and one positive square, i.e. signature `(−,+)`, and `χ` null.
This is flat space with a null translation — the paper's own example (P1: every null hyperplane of
flat space is a metric singularity).

Nothing imports this file.
-/

namespace ShadowProbe.KillingWitnessProbe

open Finset

variable {n : ℕ} {E : Type*}

/-- Component matrices of a metric at a point; index `0` is the `λ`-direction. -/
abbrev Comp (n : ℕ) := Fin (n + 1) → Fin (n + 1) → ℝ

/-- An adapted Killing chart: a symmetric metric field whose components do not depend on `λ`,
i.e. `χ = ∂_λ` is Killing. -/
structure KillingChart (n : ℕ) (E : Type*) where
  g : ℝ × E → Comp n
  symm : ∀ p a b, g p a b = g p b a
  killing : ∀ (s : ℝ) (p : ℝ × E), g (p.1 + s, p.2) = g p

/-- The line element `ds²(v) = g_ab vᵃ vᵇ`. -/
def interval (G : Comp n) (v : Fin (n + 1) → ℝ) : ℝ :=
  ∑ a, ∑ b, G a b * v a * v b

/-- `χ = ∂_λ = e₀`. -/
def chi (n : ℕ) : Fin (n + 1) → ℝ := Pi.single 0 1

/-- `|χ|²(p) = g p 0 0`. -/
def normSq (K : KillingChart n E) (p : ℝ × E) : ℝ := K.g p 0 0

/-- The `χ`-orbit through `(λ₀, x₀)`: `γ s = (λ₀ + s, x₀)`. -/
def orbit (l₀ : ℝ) (x₀ : E) (s : ℝ) : ℝ × E := (l₀ + s, x₀)

/-- The flow of `χ`: `Φ s (λ, x) = (λ + s, x)`. -/
def flow (s : ℝ) (p : ℝ × E) : ℝ × E := (p.1 + s, p.2)

/-! ### Setting -/

/-- `χ ≠ 0` in the chart (away from a bifurcation surface). -/
theorem kw_chi_ne_zero : chi n ≠ 0 := by
  intro h
  have := congrFun h 0
  simp [chi] at this

/-- The components are constant in `λ` along each orbit. -/
theorem kw_killing_const (K : KillingChart n E) (x : E) (l l' : ℝ) : K.g (l, x) = K.g (l', x) := by
  have h1 := K.killing (l - l') (l', x)
  simp only [add_sub_cancel] at h1
  exact h1

/-- The derivative form of the Killing equation: `∂_λ g_ab = 0`. -/
theorem kw_killing_deriv (K : KillingChart n E) (x : E) (a b : Fin (n + 1)) (l : ℝ) :
    HasDerivAt (fun l' => K.g (l', x) a b) 0 l := by
  have : (fun l' => K.g (l', x) a b) = fun _ => K.g (0, x) a b := by
    funext l'; rw [kw_killing_const K x l' 0]
  rw [this]; exact hasDerivAt_const _ _

/-! ### Forcing -/

/-- Tangent of the orbit `c • e₀` (`dλ = c`): `ds² = c² |χ|²`. -/
theorem kw_interval_orbit (G : Comp n) (c : ℝ) : interval G (c • chi n) = c ^ 2 * G 0 0 := by
  unfold interval chi
  rw [Finset.sum_eq_single (0 : Fin (n + 1))]
  · rw [Finset.sum_eq_single (0 : Fin (n + 1))]
    · simp; ring
    · intro b _ hb; simp [hb]
    · simp
  · intro a _ ha
    apply Finset.sum_eq_zero
    intro b _; simp [Pi.single_apply, ha]
  · simp

/-- **Forcing.** If the orbit is null at one parameter with `dλ = c ≠ 0`, then `|χ|² = 0` there. -/
theorem kw_forcing (K : KillingChart n E) (p : ℝ × E) (c : ℝ) (hc : c ≠ 0)
    (hnull : interval (K.g p) (c • chi n) = 0) : normSq K p = 0 := by
  rw [kw_interval_orbit] at hnull
  rcases mul_eq_zero.mp hnull with h | h
  · exact absurd (pow_eq_zero_iff two_ne_zero |>.mp h) hc
  · exact h

/-- `|χ|²` is constant along each orbit (Killing invariance). -/
theorem kw_normsq_orbit_const (K : KillingChart n E) (l₀ : ℝ) (x₀ : E) (s t : ℝ) :
    normSq K (orbit l₀ x₀ s) = normSq K (orbit l₀ x₀ t) := by
  unfold normSq orbit; rw [kw_killing_const K x₀ (l₀ + s) (l₀ + t)]

/-- **Forcing, along the generator.** Null at one parameter (with `dλ ≠ 0`) implies `|χ|² = 0` and the
orbit null, for every tangent `c' • χ`, at every parameter. -/
theorem kw_null_along_generator (K : KillingChart n E) (l₀ : ℝ) (x₀ : E) (s₀ c : ℝ) (hc : c ≠ 0)
    (hnull : interval (K.g (orbit l₀ x₀ s₀)) (c • chi n) = 0) :
    ∀ t c' : ℝ, normSq K (orbit l₀ x₀ t) = 0 ∧ interval (K.g (orbit l₀ x₀ t)) (c' • chi n) = 0 := by
  intro t c'
  have h0 := kw_forcing K _ c hc hnull
  have ht : normSq K (orbit l₀ x₀ t) = 0 := by rw [kw_normsq_orbit_const K l₀ x₀ t s₀]; exact h0
  refine ⟨ht, ?_⟩
  rw [kw_interval_orbit]; unfold normSq at ht; rw [ht, mul_zero]

/-! ### (b) as isometric transport -/

/-- The flow is an isometry on components: `g (Φ s p) = g p`. -/
theorem kw_flow_isometry (K : KillingChart n E) (s : ℝ) (p : ℝ × E) : K.g (flow s p) = K.g p :=
  K.killing s p

/-- `dΦ_s` is the identity in these coordinates. -/
theorem kw_flow_hasFDerivAt [NormedAddCommGroup E] [NormedSpace ℝ E] (s : ℝ) (p : ℝ × E) :
    HasFDerivAt (flow s) (ContinuousLinearMap.id ℝ (ℝ × E)) p := by
  have : flow s = fun q : ℝ × E => q + ((s, 0) : ℝ × E) := by
    funext q; ext <;> simp [flow]
  rw [this]; exact (hasFDerivAt_id p).add_const _

/-- Pullback of a component field along a map whose Jacobian (in the chart) is `D`. -/
def pullback (G : ℝ × E → Comp n) (φ : ℝ × E → ℝ × E) (D : Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ)
    (p : ℝ × E) : Comp n :=
  fun a b => ∑ a', ∑ b', D a' a * D b' b * G (φ p) a' b'

/-- **Isometry.** `Φ_s^* g = g`: with Jacobian the identity, the pullback equals the original. -/
theorem kw_flow_pullback (K : KillingChart n E) (s : ℝ) :
    pullback K.g (flow s) (1 : Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ) = K.g := by
  funext p a b
  simp only [pullback, kw_flow_isometry]
  rw [Finset.sum_eq_single a]
  · rw [Finset.sum_eq_single b]
    · simp
    · intro b' _ hb'; simp [hb']
    · simp
  · intro a' _ ha'; apply Finset.sum_eq_zero; intro b' _; simp [Matrix.one_apply, ha']
  · simp

/-- The flow maps each orbit into itself: `Φ s (γ t) = γ (t + s)`. -/
theorem kw_flow_orbit (l₀ : ℝ) (x₀ : E) (s t : ℝ) : flow s (orbit l₀ x₀ t) = orbit l₀ x₀ (t + s) := by
  simp [flow, orbit, add_assoc]

/-- A union of orbits: the points whose transverse coordinate lies in `X`. -/
def unionOfOrbits (X : Set E) : Set (ℝ × E) := {p | p.2 ∈ X}

/-- Flow-invariant set. -/
def FlowInvariant (S : Set (ℝ × E)) : Prop := ∀ s p, p ∈ S → flow s p ∈ S

/-- The flow maps a union of orbits into itself. -/
theorem kw_flow_maps_union_of_orbits (X : Set E) : FlowInvariant (unionOfOrbits X) := by
  intro s p hp; exact hp

/-- Image form: `Φ s '' 𝒦 ⊆ 𝒦` for a flow-invariant `𝒦`. -/
theorem kw_flow_image_subset (S : Set (ℝ × E)) (hS : FlowInvariant S) (s : ℝ) : flow s '' S ⊆ S := by
  rintro _ ⟨p, hp, rfl⟩; exact hS s p hp

/-- **Transverse invariants are carried along.** For `I p = F (p.2, g p)`, `I (Φ s p) = I p`. -/
theorem kw_transverse_invariant (K : KillingChart n E) {α : Type*} (F : E → Comp n → α)
    (s : ℝ) (p : ℝ × E) : F (flow s p).2 (K.g (flow s p)) = F p.2 (K.g p) := by
  rw [kw_flow_isometry]; rfl

/-- The metric restricted to the transverse indices `1..n`. -/
def transverse (G : Comp n) : Fin n → Fin n → ℝ := fun i j => G i.succ j.succ

/-- Special case: any function of `(x, g|transverse)` is invariant. -/
theorem kw_transverse_restricted (K : KillingChart n E) {α : Type*} (F : E → (Fin n → Fin n → ℝ) → α)
    (s : ℝ) (p : ℝ × E) :
    F (flow s p).2 (transverse (K.g (flow s p))) = F p.2 (transverse (K.g p)) :=
  kw_transverse_invariant K (fun x G => F x (transverse G)) s p

/-- The transverse invariants agree at `p`, at `q = Φ s p`, and at every point between. -/
theorem kw_transverse_invariant_between (K : KillingChart n E) {α : Type*} (F : E → Comp n → α)
    (s : ℝ) (p : ℝ × E) :
    F (flow s p).2 (K.g (flow s p)) = F p.2 (K.g p) ∧
      ∀ t ∈ Set.uIcc 0 s, F (flow t p).2 (K.g (flow t p)) = F p.2 (K.g p) :=
  ⟨kw_transverse_invariant K F s p, fun t _ => kw_transverse_invariant K F t p⟩

/-- `Δx = 0` for the transverse coordinate along the flow. -/
theorem kw_delta_x_zero [NormedAddCommGroup E] (s : ℝ) (p : ℝ × E) : ‖(flow s p).2 - p.2‖ = 0 := by
  simp [flow]

/-- **`Δτ = 0`** (self-contained): `Δs² = Δx² − Δτ²`, `Δs² = 0`, `Δx = 0` give `Δτ = 0`. -/
theorem kw_delta_tau_zero (Δs2 Δx Δτ : ℝ) (h : Δs2 = Δx ^ 2 - Δτ ^ 2) (hs : Δs2 = 0) (hx : Δx = 0) :
    Δτ = 0 := by
  subst hx; rw [hs] at h
  have : Δτ ^ 2 = 0 := by linarith
  exact pow_eq_zero_iff two_ne_zero |>.mp this

/-! ### `lem:killing` -/

/-- The conclusion: hypotheses (a) and (b) of `thm:metric-singularity` for `p`, `q`, and metric
coincidence `Δτ = 0`. -/
structure MetricallyCoincident [NormedAddCommGroup E] (K : KillingChart n E) (p q : ℝ × E) : Prop where
  /-- (a): `|χ|² = 0` at `p`, at `q`, and along the whole generator. -/
  hypA : ∀ t, normSq K (p.1 + t, p.2) = 0
  /-- (b): every transverse invariant takes the same value at `p` and at `q`. -/
  hypB : ∀ (α : Type) (F : E → Comp n → α), F q.2 (K.g q) = F p.2 (K.g p)
  /-- (b), between: and at every point of the connecting generator segment. -/
  hypB_between : ∀ (α : Type) (F : E → Comp n → α), ∀ t ∈ Set.uIcc 0 (q.1 - p.1),
    F (flow t p).2 (K.g (flow t p)) = F p.2 (K.g p)
  /-- `Δx = 0`. -/
  deltaX : ‖q.2 - p.2‖ = 0
  /-- `Δτ = 0` from `Δs² = Δx² − Δτ²` on the null connection. -/
  deltaTau : ∀ Δτ : ℝ, 0 = ‖q.2 - p.2‖ ^ 2 - Δτ ^ 2 → Δτ = 0

/-- **`lem:killing` (adapted chart).** Two events `p`, `q` on one orbit (generator) `x = x₀`, which is null
at some parameter with `dλ = c ≠ 0`, are metrically coincident. -/
theorem kw_lemma_killing [NormedAddCommGroup E] (K : KillingChart n E) (x₀ : E) (p q : ℝ × E)
    (hp : p.2 = x₀) (hq : q.2 = x₀) (s₀ c : ℝ) (hc : c ≠ 0)
    (hnull : interval (K.g (orbit 0 x₀ s₀)) (c • chi n) = 0) : MetricallyCoincident K p q := by
  have hq' : q = flow (q.1 - p.1) p := by
    ext
    · simp [flow]
    · simp [flow, hp, hq]
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · intro t
    have := (kw_null_along_generator K 0 x₀ s₀ c hc hnull (p.1 + t) 1).1
    simpa [orbit, hp] using this
  · intro α F; rw [hq']; exact kw_transverse_invariant K F _ p
  · intro α F; exact (kw_transverse_invariant_between K F (q.1 - p.1) p).2
  · rw [hp, hq]; simp
  · intro Δτ h
    have hx : ‖q.2 - p.2‖ = 0 := by rw [hp, hq]; simp
    exact kw_delta_tau_zero 0 _ Δτ h rfl hx

/-! ### `cor:stationary` (rigidity as a hypothesis) -/

/-- "`𝓗⁺` is a Killing horizon": a Killing chart in which `𝓗⁺` is a union of orbits, each null with
`χ ≠ 0` (the null tangent `c • χ`, `c ≠ 0`). -/
structure IsKillingHorizon (n : ℕ) (H : Set (ℝ × E)) where
  K : KillingChart n E
  X : Set E
  union : H = unionOfOrbits X
  null : ∀ x ∈ X, ∃ s₀ c : ℝ, c ≠ 0 ∧ interval (K.g (orbit 0 x s₀)) (c • chi n) = 0

/-- The rigidity hypothesis, as a `Prop`: the event horizon is a Killing horizon. -/
def Rigidity (n : ℕ) (H : Set (ℝ × E)) : Prop := Nonempty (IsKillingHorizon (E := E) n H)

/-- **`cor:stationary`.** Under rigidity, there is a Killing chart in which every pair of events on one
generator of `𝓗⁺` is metrically coincident; `𝓗⁺` is flow-invariant. -/
theorem kw_cor_stationary [NormedAddCommGroup E] (H : Set (ℝ × E)) (hR : Rigidity n H) :
    ∃ K : KillingChart n E, FlowInvariant H ∧
      ∀ p ∈ H, ∀ q ∈ H, p.2 = q.2 → MetricallyCoincident K p q := by
  obtain ⟨⟨K, X, hU, hN⟩⟩ := hR
  refine ⟨K, ?_, ?_⟩
  · rw [hU]; exact kw_flow_maps_union_of_orbits X
  · intro p hp q _ hpq
    rw [hU] at hp
    obtain ⟨s₀, c, hc, hnull⟩ := hN p.2 hp
    exact kw_lemma_killing K p.2 p q rfl hpq.symm s₀ c hc hnull


/-! ### Campaign 82: the witness (null translation in Minkowski `1+1`, light-cone form) -/

/-- Minkowski `1+1` in light-cone form, `ds² = 2 dλ dx`: `g₀₀ = g₁₁ = 0`, `g₀₁ = g₁₀ = 1`. -/
def kw_lightCone : Comp 1 := fun a b => if a = b then 0 else 1

/-- The witness chart: constant metric, so the Killing condition holds by `rfl`. -/
def kw_chart : KillingChart 1 ℝ where
  g := fun _ => kw_lightCone
  symm := by intro _ a b; simp only [kw_lightCone, eq_comm]
  killing := by intro _ _; rfl

/-- The bilinear form `g(v, w) = g_ab vᵃ wᵇ`. -/
def bilin (G : Comp n) (v w : Fin (n + 1) → ℝ) : ℝ := ∑ a, ∑ b, G a b * v a * w b

/-- `χ` is null: `g(χ,χ) = g₀₀ = 0` everywhere. -/
theorem kw_chi_null (p : ℝ × ℝ) : normSq kw_chart p = 0 := by
  simp [normSq, kw_chart, kw_lightCone]

/-- The `hnull` hypothesis of `kw_lemma_killing` holds at every `x₀`, `s₀` (with `c = 1`). -/
theorem kw_hnull (x₀ s₀ : ℝ) : interval (kw_chart.g (orbit 0 x₀ s₀)) ((1 : ℝ) • chi 1) = 0 := by
  rw [kw_interval_orbit]; simp [kw_chart, kw_lightCone]

/-- Nondegeneracy: `det g = -1 ≠ 0`. -/
theorem kw_lightCone_det : (Matrix.of kw_lightCone).det = -1 := by
  rw [Matrix.det_fin_two]; simp [kw_lightCone]

/-- A timelike vector: `ds²(1,-1) = -2 < 0`. -/
theorem kw_timelike : interval kw_lightCone ![1, -1] = -2 := by
  simp [interval, kw_lightCone, Fin.sum_univ_two]; norm_num

/-- A spacelike vector: `ds²(1,1) = 2 > 0`. -/
theorem kw_spacelike : interval kw_lightCone ![1, 1] = 2 := by
  simp [interval, kw_lightCone, Fin.sum_univ_two]; norm_num

/-- The timelike and spacelike vectors are `g`-orthogonal. -/
theorem kw_orth : bilin kw_lightCone ![1, -1] ![1, 1] = 0 := by
  simp [bilin, kw_lightCone, Fin.sum_univ_two]

/-- **Lorentzian, not degenerate.** `det ≠ 0`, and an orthogonal basis `{(1,-1), (1,1)}` with squares
`-2 < 0 < 2`: signature `(−,+)`. The metric is not zero, and `χ` is null. -/
theorem kw_lorentzian :
    (Matrix.of kw_lightCone).det ≠ 0 ∧ kw_lightCone ≠ 0 ∧
      interval kw_lightCone ![1, -1] < 0 ∧ 0 < interval kw_lightCone ![1, 1] ∧
      bilin kw_lightCone ![1, -1] ![1, 1] = 0 ∧ LinearIndependent ℝ ![(![1, -1] : Fin 2 → ℝ), ![1, 1]] ∧
      interval kw_lightCone (chi 1) = 0 := by
  refine ⟨by rw [kw_lightCone_det]; norm_num, ?_, by rw [kw_timelike]; norm_num,
    by rw [kw_spacelike]; norm_num, kw_orth, ?_, ?_⟩
  · intro h; have := congrFun (congrFun h 0) 1; simp [kw_lightCone] at this
  · rw [LinearIndependent.pair_iff]
    intro s t hst
    have h0 := congrFun hst 0; have h1 := congrFun hst 1
    simp at h0 h1
    constructor <;> linarith
  · have := kw_interval_orbit kw_lightCone 1; simp at this; rw [this]; simp [kw_lightCone]

/-- **Caveat: the structure admits the zero metric.** `KillingChart` imposes no nondegeneracy, so
`g ≡ 0` satisfies `Rigidity` for *every* union of orbits, here all of `ℝ × ℝ`. A witness must
therefore be checked non-degenerate (`kw_lorentzian`); the zero chart is not our witness. -/
theorem kw_zero_rigidity : Rigidity 1 (Set.univ : Set (ℝ × ℝ)) :=
  ⟨{ K := { g := fun _ => 0, symm := fun _ _ _ => rfl, killing := fun _ _ => rfl }
     X := Set.univ
     union := by ext p; simp [unionOfOrbits]
     null := fun _ _ => ⟨0, 1, one_ne_zero, by simp [interval]⟩ }⟩

/-- **Witness for `lem:killing`.** A concrete chart, `x₀ = 0`, `p = (0,0) ≠ q = (1,0)` on the orbit
`x = 0`, metrically coincident; the chart's metric is the nondegenerate Lorentzian `kw_lightCone`. -/
theorem kw_lemma_killing_witness :
    ∃ (K : KillingChart 1 ℝ) (x₀ : ℝ) (p q : ℝ × ℝ), p ≠ q ∧ p.2 = x₀ ∧ q.2 = x₀ ∧
      MetricallyCoincident K p q ∧ (∀ r, K.g r = kw_lightCone) :=
  ⟨kw_chart, 0, (0, 0), (1, 0), by simp, rfl, rfl,
    kw_lemma_killing kw_chart 0 (0, 0) (1, 0) rfl rfl 0 1 one_ne_zero (kw_hnull 0 0),
    fun _ => rfl⟩

/-- The concrete instance, stated without existentials. -/
theorem kw_coincident_concrete : MetricallyCoincident kw_chart ((0 : ℝ), (0 : ℝ)) ((1 : ℝ), (0 : ℝ)) :=
  kw_lemma_killing kw_chart 0 (0, 0) (1, 0) rfl rfl 0 1 one_ne_zero (kw_hnull 0 0)

/-- The null line `x = 0`, union of the orbits through `X = {0}`. -/
def kw_H : Set (ℝ × ℝ) := unionOfOrbits {0}

/-- The Killing-horizon structure on `kw_H`, built from `kw_chart`. -/
def kw_isKillingHorizon : IsKillingHorizon 1 kw_H where
  K := kw_chart
  X := {0}
  union := rfl
  null := fun x _ => ⟨0, 1, one_ne_zero, kw_hnull x 0⟩

/-- `Rigidity 1 kw_H`. -/
theorem kw_rigidity : Rigidity 1 kw_H := ⟨kw_isKillingHorizon⟩

/-- **Witness for `cor:stationary`.** `H = unionOfOrbits X` with `X = {0}` non-empty, `H` non-empty, a
`Rigidity` instance (from the Lorentzian `kw_chart`), the full conclusion of `kw_cor_stationary`, and a
concrete pair `(0,0) ≠ (1,0)` in `H` metrically coincident under the chart the corollary returns. -/
theorem kw_cor_stationary_witness :
    ∃ (H : Set (ℝ × ℝ)) (X : Set ℝ), X.Nonempty ∧ H = unionOfOrbits X ∧ H.Nonempty ∧
      Rigidity 1 H ∧
      ∃ K : KillingChart 1 ℝ, FlowInvariant H ∧
        (∀ p ∈ H, ∀ q ∈ H, p.2 = q.2 → MetricallyCoincident K p q) ∧
        ((0 : ℝ), (0 : ℝ)) ∈ H ∧ ((1 : ℝ), (0 : ℝ)) ∈ H ∧ ((0 : ℝ), (0 : ℝ)) ≠ ((1 : ℝ), (0 : ℝ)) ∧
        MetricallyCoincident K ((0 : ℝ), (0 : ℝ)) ((1 : ℝ), (0 : ℝ)) := by
  obtain ⟨K, hF, hM⟩ := kw_cor_stationary kw_H kw_rigidity
  have h0 : ((0 : ℝ), (0 : ℝ)) ∈ kw_H := rfl
  have h1 : ((1 : ℝ), (0 : ℝ)) ∈ kw_H := rfl
  exact ⟨kw_H, {0}, ⟨0, rfl⟩, rfl, ⟨_, h0⟩, kw_rigidity, K, hF, hM, h0, h1, by simp,
    hM _ h0 _ h1 rfl⟩

end ShadowProbe.KillingWitnessProbe


#print axioms ShadowProbe.KillingWitnessProbe.kw_killing_deriv
#print axioms ShadowProbe.KillingWitnessProbe.kw_interval_orbit
#print axioms ShadowProbe.KillingWitnessProbe.kw_forcing
#print axioms ShadowProbe.KillingWitnessProbe.kw_normsq_orbit_const
#print axioms ShadowProbe.KillingWitnessProbe.kw_null_along_generator
#print axioms ShadowProbe.KillingWitnessProbe.kw_flow_isometry
#print axioms ShadowProbe.KillingWitnessProbe.kw_flow_hasFDerivAt
#print axioms ShadowProbe.KillingWitnessProbe.kw_flow_pullback
#print axioms ShadowProbe.KillingWitnessProbe.kw_flow_orbit
#print axioms ShadowProbe.KillingWitnessProbe.kw_flow_maps_union_of_orbits
#print axioms ShadowProbe.KillingWitnessProbe.kw_flow_image_subset
#print axioms ShadowProbe.KillingWitnessProbe.kw_transverse_invariant
#print axioms ShadowProbe.KillingWitnessProbe.kw_transverse_restricted
#print axioms ShadowProbe.KillingWitnessProbe.kw_transverse_invariant_between
#print axioms ShadowProbe.KillingWitnessProbe.kw_delta_x_zero
#print axioms ShadowProbe.KillingWitnessProbe.kw_delta_tau_zero
#print axioms ShadowProbe.KillingWitnessProbe.kw_lemma_killing
#print axioms ShadowProbe.KillingWitnessProbe.kw_cor_stationary
#print axioms ShadowProbe.KillingWitnessProbe.kw_chi_null
#print axioms ShadowProbe.KillingWitnessProbe.kw_hnull
#print axioms ShadowProbe.KillingWitnessProbe.kw_lightCone_det
#print axioms ShadowProbe.KillingWitnessProbe.kw_timelike
#print axioms ShadowProbe.KillingWitnessProbe.kw_spacelike
#print axioms ShadowProbe.KillingWitnessProbe.kw_orth
#print axioms ShadowProbe.KillingWitnessProbe.kw_lorentzian
#print axioms ShadowProbe.KillingWitnessProbe.kw_zero_rigidity
#print axioms ShadowProbe.KillingWitnessProbe.kw_lemma_killing_witness
#print axioms ShadowProbe.KillingWitnessProbe.kw_coincident_concrete
#print axioms ShadowProbe.KillingWitnessProbe.kw_rigidity
#print axioms ShadowProbe.KillingWitnessProbe.kw_cor_stationary_witness

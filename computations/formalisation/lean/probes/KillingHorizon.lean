import Mathlib

/-!
# Probe of `r7613+71.3` (campaign 59, `r7613` ②): `lem:killing` and `cor:stationary`, adapted chart

Source: `corpus/BH_causality_v2.tex`, `lem:killing` and `cor:stationary`. Registered target:
`computations/formalisation/r7613_71_campaign59/PREDICTION.md`.

**Setting.** Points are `ℝ × E` with coordinates `(λ, x)`. The metric is a field of symmetric component
matrices `g : ℝ × E → Fin (n+1) → Fin (n+1) → ℝ`; index `0` is the `λ`-direction, so `χ = ∂_λ = e₀`
and `|χ|²(p) = g p 0 0`. `χ` is Killing in this chart: the components are `λ`-independent,
`g (λ + s, x) = g (λ, x)` (the Killing equation `∂_λ g_ab = 0` in adapted coordinates; the derivative
form is `kh_killing_deriv`).

**Pieces.**
* Forcing: `kh_interval_orbit`, `kh_forcing`, `kh_normsq_orbit_const`, `kh_null_along_generator`.
* (b) as isometric transport: `kh_flow_isometry`, `kh_flow_hasFDerivAt`, `kh_flow_pullback`,
  `kh_flow_orbit`, `kh_flow_maps_union_of_orbits`, `kh_transverse_invariant`,
  `kh_transverse_invariant_between`, `kh_delta_x_zero`, `kh_delta_tau_zero`.
* `lem:killing`: `kh_lemma_killing`.  `cor:stationary` (rigidity as a hypothesis): `kh_cor_stationary`.

Nothing imports this file.
-/

namespace KillingHorizonProbe

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
theorem kh_chi_ne_zero : chi n ≠ 0 := by
  intro h
  have := congrFun h 0
  simp [chi] at this

/-- The components are constant in `λ` along each orbit. -/
theorem kh_killing_const (K : KillingChart n E) (x : E) (l l' : ℝ) : K.g (l, x) = K.g (l', x) := by
  have h1 := K.killing (l - l') (l', x)
  simp only [add_sub_cancel] at h1
  exact h1

/-- The derivative form of the Killing equation: `∂_λ g_ab = 0`. -/
theorem kh_killing_deriv (K : KillingChart n E) (x : E) (a b : Fin (n + 1)) (l : ℝ) :
    HasDerivAt (fun l' => K.g (l', x) a b) 0 l := by
  have : (fun l' => K.g (l', x) a b) = fun _ => K.g (0, x) a b := by
    funext l'; rw [kh_killing_const K x l' 0]
  rw [this]; exact hasDerivAt_const _ _

/-! ### Forcing -/

/-- Tangent of the orbit `c • e₀` (`dλ = c`): `ds² = c² |χ|²`. -/
theorem kh_interval_orbit (G : Comp n) (c : ℝ) : interval G (c • chi n) = c ^ 2 * G 0 0 := by
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
theorem kh_forcing (K : KillingChart n E) (p : ℝ × E) (c : ℝ) (hc : c ≠ 0)
    (hnull : interval (K.g p) (c • chi n) = 0) : normSq K p = 0 := by
  rw [kh_interval_orbit] at hnull
  rcases mul_eq_zero.mp hnull with h | h
  · exact absurd (pow_eq_zero_iff two_ne_zero |>.mp h) hc
  · exact h

/-- `|χ|²` is constant along each orbit (Killing invariance). -/
theorem kh_normsq_orbit_const (K : KillingChart n E) (l₀ : ℝ) (x₀ : E) (s t : ℝ) :
    normSq K (orbit l₀ x₀ s) = normSq K (orbit l₀ x₀ t) := by
  unfold normSq orbit; rw [kh_killing_const K x₀ (l₀ + s) (l₀ + t)]

/-- **Forcing, along the generator.** Null at one parameter (with `dλ ≠ 0`) implies `|χ|² = 0` and the
orbit null, for every tangent `c' • χ`, at every parameter. -/
theorem kh_null_along_generator (K : KillingChart n E) (l₀ : ℝ) (x₀ : E) (s₀ c : ℝ) (hc : c ≠ 0)
    (hnull : interval (K.g (orbit l₀ x₀ s₀)) (c • chi n) = 0) :
    ∀ t c' : ℝ, normSq K (orbit l₀ x₀ t) = 0 ∧ interval (K.g (orbit l₀ x₀ t)) (c' • chi n) = 0 := by
  intro t c'
  have h0 := kh_forcing K _ c hc hnull
  have ht : normSq K (orbit l₀ x₀ t) = 0 := by rw [kh_normsq_orbit_const K l₀ x₀ t s₀]; exact h0
  refine ⟨ht, ?_⟩
  rw [kh_interval_orbit]; unfold normSq at ht; rw [ht, mul_zero]

/-! ### (b) as isometric transport -/

/-- The flow is an isometry on components: `g (Φ s p) = g p`. -/
theorem kh_flow_isometry (K : KillingChart n E) (s : ℝ) (p : ℝ × E) : K.g (flow s p) = K.g p :=
  K.killing s p

/-- `dΦ_s` is the identity in these coordinates. -/
theorem kh_flow_hasFDerivAt [NormedAddCommGroup E] [NormedSpace ℝ E] (s : ℝ) (p : ℝ × E) :
    HasFDerivAt (flow s) (ContinuousLinearMap.id ℝ (ℝ × E)) p := by
  have : flow s = fun q : ℝ × E => q + ((s, 0) : ℝ × E) := by
    funext q; ext <;> simp [flow]
  rw [this]; exact (hasFDerivAt_id p).add_const _

/-- Pullback of a component field along a map whose Jacobian (in the chart) is `D`. -/
def pullback (G : ℝ × E → Comp n) (φ : ℝ × E → ℝ × E) (D : Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ)
    (p : ℝ × E) : Comp n :=
  fun a b => ∑ a', ∑ b', D a' a * D b' b * G (φ p) a' b'

/-- **Isometry.** `Φ_s^* g = g`: with Jacobian the identity, the pullback equals the original. -/
theorem kh_flow_pullback (K : KillingChart n E) (s : ℝ) :
    pullback K.g (flow s) (1 : Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ) = K.g := by
  funext p a b
  simp only [pullback, kh_flow_isometry]
  rw [Finset.sum_eq_single a]
  · rw [Finset.sum_eq_single b]
    · simp
    · intro b' _ hb'; simp [hb']
    · simp
  · intro a' _ ha'; apply Finset.sum_eq_zero; intro b' _; simp [Matrix.one_apply, ha']
  · simp

/-- The flow maps each orbit into itself: `Φ s (γ t) = γ (t + s)`. -/
theorem kh_flow_orbit (l₀ : ℝ) (x₀ : E) (s t : ℝ) : flow s (orbit l₀ x₀ t) = orbit l₀ x₀ (t + s) := by
  simp [flow, orbit, add_assoc]

/-- A union of orbits: the points whose transverse coordinate lies in `X`. -/
def unionOfOrbits (X : Set E) : Set (ℝ × E) := {p | p.2 ∈ X}

/-- Flow-invariant set. -/
def FlowInvariant (S : Set (ℝ × E)) : Prop := ∀ s p, p ∈ S → flow s p ∈ S

/-- The flow maps a union of orbits into itself. -/
theorem kh_flow_maps_union_of_orbits (X : Set E) : FlowInvariant (unionOfOrbits X) := by
  intro s p hp; exact hp

/-- Image form: `Φ s '' 𝒦 ⊆ 𝒦` for a flow-invariant `𝒦`. -/
theorem kh_flow_image_subset (S : Set (ℝ × E)) (hS : FlowInvariant S) (s : ℝ) : flow s '' S ⊆ S := by
  rintro _ ⟨p, hp, rfl⟩; exact hS s p hp

/-- **Transverse invariants are carried along.** For `I p = F (p.2, g p)`, `I (Φ s p) = I p`. -/
theorem kh_transverse_invariant (K : KillingChart n E) {α : Type*} (F : E → Comp n → α)
    (s : ℝ) (p : ℝ × E) : F (flow s p).2 (K.g (flow s p)) = F p.2 (K.g p) := by
  rw [kh_flow_isometry]; rfl

/-- The metric restricted to the transverse indices `1..n`. -/
def transverse (G : Comp n) : Fin n → Fin n → ℝ := fun i j => G i.succ j.succ

/-- Special case: any function of `(x, g|transverse)` is invariant. -/
theorem kh_transverse_restricted (K : KillingChart n E) {α : Type*} (F : E → (Fin n → Fin n → ℝ) → α)
    (s : ℝ) (p : ℝ × E) :
    F (flow s p).2 (transverse (K.g (flow s p))) = F p.2 (transverse (K.g p)) :=
  kh_transverse_invariant K (fun x G => F x (transverse G)) s p

/-- The transverse invariants agree at `p`, at `q = Φ s p`, and at every point between. -/
theorem kh_transverse_invariant_between (K : KillingChart n E) {α : Type*} (F : E → Comp n → α)
    (s : ℝ) (p : ℝ × E) :
    F (flow s p).2 (K.g (flow s p)) = F p.2 (K.g p) ∧
      ∀ t ∈ Set.uIcc 0 s, F (flow t p).2 (K.g (flow t p)) = F p.2 (K.g p) :=
  ⟨kh_transverse_invariant K F s p, fun t _ => kh_transverse_invariant K F t p⟩

/-- `Δx = 0` for the transverse coordinate along the flow. -/
theorem kh_delta_x_zero [NormedAddCommGroup E] (s : ℝ) (p : ℝ × E) : ‖(flow s p).2 - p.2‖ = 0 := by
  simp [flow]

/-- **`Δτ = 0`** (self-contained): `Δs² = Δx² − Δτ²`, `Δs² = 0`, `Δx = 0` give `Δτ = 0`. -/
theorem kh_delta_tau_zero (Δs2 Δx Δτ : ℝ) (h : Δs2 = Δx ^ 2 - Δτ ^ 2) (hs : Δs2 = 0) (hx : Δx = 0) :
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
theorem kh_lemma_killing [NormedAddCommGroup E] (K : KillingChart n E) (x₀ : E) (p q : ℝ × E)
    (hp : p.2 = x₀) (hq : q.2 = x₀) (s₀ c : ℝ) (hc : c ≠ 0)
    (hnull : interval (K.g (orbit 0 x₀ s₀)) (c • chi n) = 0) : MetricallyCoincident K p q := by
  have hq' : q = flow (q.1 - p.1) p := by
    ext
    · simp [flow]
    · simp [flow, hp, hq]
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · intro t
    have := (kh_null_along_generator K 0 x₀ s₀ c hc hnull (p.1 + t) 1).1
    simpa [orbit, hp] using this
  · intro α F; rw [hq']; exact kh_transverse_invariant K F _ p
  · intro α F; exact (kh_transverse_invariant_between K F (q.1 - p.1) p).2
  · rw [hp, hq]; simp
  · intro Δτ h
    have hx : ‖q.2 - p.2‖ = 0 := by rw [hp, hq]; simp
    exact kh_delta_tau_zero 0 _ Δτ h rfl hx

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
theorem kh_cor_stationary [NormedAddCommGroup E] (H : Set (ℝ × E)) (hR : Rigidity n H) :
    ∃ K : KillingChart n E, FlowInvariant H ∧
      ∀ p ∈ H, ∀ q ∈ H, p.2 = q.2 → MetricallyCoincident K p q := by
  obtain ⟨⟨K, X, hU, hN⟩⟩ := hR
  refine ⟨K, ?_, ?_⟩
  · rw [hU]; exact kh_flow_maps_union_of_orbits X
  · intro p hp q _ hpq
    rw [hU] at hp
    obtain ⟨s₀, c, hc, hnull⟩ := hN p.2 hp
    exact kh_lemma_killing K p.2 p q rfl hpq.symm s₀ c hc hnull

end KillingHorizonProbe

#print axioms KillingHorizonProbe.kh_killing_deriv
#print axioms KillingHorizonProbe.kh_interval_orbit
#print axioms KillingHorizonProbe.kh_forcing
#print axioms KillingHorizonProbe.kh_normsq_orbit_const
#print axioms KillingHorizonProbe.kh_null_along_generator
#print axioms KillingHorizonProbe.kh_flow_isometry
#print axioms KillingHorizonProbe.kh_flow_hasFDerivAt
#print axioms KillingHorizonProbe.kh_flow_pullback
#print axioms KillingHorizonProbe.kh_flow_orbit
#print axioms KillingHorizonProbe.kh_flow_maps_union_of_orbits
#print axioms KillingHorizonProbe.kh_flow_image_subset
#print axioms KillingHorizonProbe.kh_transverse_invariant
#print axioms KillingHorizonProbe.kh_transverse_restricted
#print axioms KillingHorizonProbe.kh_transverse_invariant_between
#print axioms KillingHorizonProbe.kh_delta_x_zero
#print axioms KillingHorizonProbe.kh_delta_tau_zero
#print axioms KillingHorizonProbe.kh_lemma_killing
#print axioms KillingHorizonProbe.kh_cor_stationary

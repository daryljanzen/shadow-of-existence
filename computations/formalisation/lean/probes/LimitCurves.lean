import Mathlib

/-!
# Probe `r7619+71.1` (campaign 61, `r7619` ①): Lipschitz causal curves and the limit-curve lemma

Registration: `computations/formalisation/r7619_71_campaign61/PREDICTION.md`. Setting: campaign 60's
`probes/CausalStructure.lean` (one chart). Probes cannot import probes, so `Spacetime`, `FutCausal`,
`CStep` and `Cau` are copied verbatim into the namespace `ShadowProbe.LimitCurvesProbe`. Every
theorem here is prefixed `lc_`.

## Setting

`V` is a real normed space, `M ⊆ V` open, `g : V → (V →L V →L ℝ)` continuous and symmetric, `T`
continuous with `g_x(T,T) < 0` and `g_x` positive definite on `T^⊥` for `x ∈ M` (campaign 60's
encoding of signature `(−,+,…,+)`). Results marked *(fd)* also assume `[FiniteDimensional ℝ V]`.

## The definition chosen (`LipCausal`)

* The closed future cone is `C x = {v | g_x(v,v) ≤ 0 ∧ g_x(v,T x) ≤ 0}` (`CC`).
* For `ε > 0` and `A ⊆ V`, put `Hull_ε(A) = closure (convexHull (⋃_{y ∈ thickening ε A ∩ M} C y))`
  (`coneHull`).
* `γ : ℝ → V` is a **Lipschitz future-causal curve** (`LipCausal`) iff
  1. `γ` is `L`-Lipschitz on `[0,1]` for some `L`,
  2. `γ([0,1]) ⊆ M`, and
  3. (`ConeCond`) for all `0 ≤ s < t ≤ 1` and every `ε > 0`,
     `(γ t − γ s)/(t − s) ∈ Hull_ε(γ([s,t]))`.
* `LStep x y` means there is such a `γ` with `γ 0 = x`, `γ 1 = y`. `LCau` is its
  reflexive-transitive closure.

This is the "cone-difference quotients over (neighbourhoods of) the image" form: the cone form of
the registration, with the `o(t−s)` error absorbed by the `ε`-fattening. It has no modulus, and
that is why the limit-curve lemma needs no uniformity hypothesis.

**Why it is faithful.**
* Every `C¹` curve with velocity in `C` satisfies it (`lc_c1_lipCausal`). The proof uses the mean
  value theorem in its convex-hull form (`lc_chord_mem_of_deriv_mem`), via Hahn–Banach and scalar
  Lagrange. So campaign 60's `≤` is contained in `LCau` (`lc_cau_lcau`).
* Conversely, every one-sided velocity of a `LipCausal` curve lies in the outer cone
  `Ĉ x = ⋂_ε Hull_ε({x})` (`lc_velocity_mem_coneHat`; no dimension hypothesis).
* *(fd)* `Ĉ x = C x` for `x ∈ M` (`lc_coneHat_eq_cone`). The proof combines
  - reverse Cauchy–Schwarz (`lc_reverse_cs`), which also gives convexity of `C x`
    (`lc_convex_cone`),
  - a uniform coercivity estimate near `x` (`lc_coercive`, by compactness of the unit sphere), and
  - a half-space separation (`lc_halfspace`).
  Hence velocities lie in `C` (`lc_velocity_mem_cone_fd`), and for `C¹` curves `LipCausal` is
  **equivalent** to "in `M`, with velocity in the closed future cone on `[0,1]`"
  (`lc_c1_lipCausal_iff`).
* In infinite dimension, `Ĉ x ⊆ C x` is not proved. `lc_velocity_mem_cone` takes it as an
  explicit hypothesis.
* Caveats.
  - The closed cone includes `0`, so constant curves are causal (this is standard for the closed
    relation `J`).
  - The a.e.-velocity form (Rademacher) is **not** used, and its equivalence with the cone form
    for general Lipschitz curves is **not** proved. Only the `C¹` equivalence above is.

## The limit-curve lemma and Arzelà–Ascoli

* `lc_limit_curve`. Take `Fₙ` uniformly `L`-Lipschitz on `[0,1]`, mapping `[0,1]` into a closed
  `K ⊆ M`, each with `ConeCond`, and `Fₙ → γ` uniformly on `[0,1]`. Then `γ` is `L`-Lipschitz,
  maps into `K`, and is `LipCausal`. **No uniform modulus is needed**, because for `n` large
  `Fₙ([s,t]) ⊆ thickening (ε/2) γ([s,t])` and the hulls are closed. Uniform convergence is used
  only for that inclusion; pointwise convergence handles the quotients.
* `lc_arzela_ascoli`. With `K` compact, there are a subsequence and a `γ` such that the
  subsequence converges uniformly to `γ` on `[0,1]`, and `γ` is an `L`-Lipschitz causal curve into
  `K`. The proof uses `BoundedContinuousFunction.arzela_ascoli` and
  `LipschitzWith.uniformEquicontinuous`.
* `lc_lstep_of_limit`. Endpoint form: if `pₙ → p`, `qₙ → q`, and causal pieces `pₙ → qₙ` are
  uniformly Lipschitz in a compact `K ⊆ M`, then there is a causal piece `p → q` inside `K`.

## Not attempted (stretch): null generators of `∂J⁻(S)` and the tangency clause

These are REPORTED. The first missing lemma is a *uniform Lipschitz reparametrisation*: in a compact
`K ⊆ M` (fd), every causal curve segment in `K`, reparametrised by a fixed local time function,
should be `L_K`-Lipschitz with `L_K` independent of the curve. `lc_coercive` is the pointwise
ingredient. Without this lemma, the curves from `pₙ ∈ J⁻(S)` to `S` have no common Lipschitz bound,
and the limit lemma cannot be applied. After it, two more lemmas are needed:
* push-up for the Lipschitz relation, `LCau q p → Chr p z → Chr q z`, so that the limit curve
  stays on `∂J⁻(S)`;
* `int J⁻ = I⁻` for that relation.
Tangency needs, in addition, that generators are null geodesics. That requires geodesics of `g`,
which are absent here.
-/

open Set Filter Topology Metric
open scoped BoundedContinuousFunction

namespace ShadowProbe.LimitCurvesProbe

variable {V : Type*} [NormedAddCommGroup V] [NormedSpace ℝ V]

/-- A time-oriented Lorentzian chart (copied verbatim from `probes/CausalStructure.lean`). -/
structure Spacetime (V : Type*) [NormedAddCommGroup V] [NormedSpace ℝ V] where
  M : Set V
  isOpen_M : IsOpen M
  g : V → V →L[ℝ] V →L[ℝ] ℝ
  cont_g : Continuous g
  symm : ∀ x v w, g x v w = g x w v
  T : V → V
  cont_T : Continuous T
  T_timelike : ∀ x ∈ M, g x (T x) (T x) < 0
  pos_on_perp : ∀ x ∈ M, ∀ v, g x v (T x) = 0 → v ≠ 0 → 0 < g x v v

namespace Spacetime
variable (S : Spacetime V)

/-- Future-directed causal vector at `x` (campaign 60). -/
def FutCausal (x v : V) : Prop := S.g x v v ≤ 0 ∧ S.g x v (S.T x) < 0

/-- One `C¹` future-causal piece from `x` to `y` (campaign 60). -/
def CStep (x y : V) : Prop :=
  ∃ γ : ℝ → V, ContDiff ℝ 1 γ ∧ γ 0 = x ∧ γ 1 = y ∧
    ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ S.M ∧ S.FutCausal (γ t) (deriv γ t)

/-- Campaign 60's causal relation `x ≤ y`: a finite chain of `C¹` causal pieces. -/
def Cau (x y : V) : Prop := Relation.ReflTransGen S.CStep x y

/-! ### The closed cone field and the Lipschitz causal class -/

/-- The closed future cone at `x`: `C x = {v | g_x(v,v) ≤ 0 ∧ g_x(v,T x) ≤ 0}` (contains `0`). -/
def CC (x : V) : Set V := {v | S.g x v v ≤ 0 ∧ S.g x v (S.T x) ≤ 0}

/-- The closed convex hull of the closed cones over the points of `M` within `ε` of `A`. -/
def coneHull (ε : ℝ) (A : Set V) : Set V :=
  closure (convexHull ℝ (⋃ x ∈ thickening ε A ∩ S.M, S.CC x))

/-- The cone condition on `[0,1]`: every chord quotient over `[s,t]` lies in the closed convex hull
of the cones over every `ε`-neighbourhood of the arc `γ([s,t])`. -/
def ConeCond (γ : ℝ → V) : Prop :=
  ∀ s t : ℝ, 0 ≤ s → s < t → t ≤ 1 → ∀ ε > 0,
    (t - s)⁻¹ • (γ t - γ s) ∈ S.coneHull ε (γ '' Icc s t)

/-- A **Lipschitz future-causal curve** on `[0,1]`. -/
def LipCausal (γ : ℝ → V) : Prop :=
  (∃ L : NNReal, LipschitzOnWith L γ (Icc 0 1)) ∧ MapsTo γ (Icc 0 1) S.M ∧ S.ConeCond γ

/-- One Lipschitz causal piece from `x` to `y`. -/
def LStep (x y : V) : Prop := ∃ γ : ℝ → V, S.LipCausal γ ∧ γ 0 = x ∧ γ 1 = y

/-- The Lipschitz causal relation: finite chains of Lipschitz causal pieces. -/
def LCau (x y : V) : Prop := Relation.ReflTransGen S.LStep x y

lemma lc_isClosed_coneHull (ε : ℝ) (A : Set V) : IsClosed (S.coneHull ε A) := isClosed_closure

lemma lc_convex_coneHull (ε : ℝ) (A : Set V) : Convex ℝ (S.coneHull ε A) :=
  (convex_convexHull ℝ _).closure

/-- Monotonicity of the hull in the set and the radius. -/
lemma lc_coneHull_mono {ε δ ε' : ℝ} {A B : Set V} (h : A ⊆ thickening δ B) (hle : ε + δ ≤ ε') :
    S.coneHull ε A ⊆ S.coneHull ε' B := by
  have h1 : thickening ε A ⊆ thickening ε' B :=
    (thickening_subset_of_subset ε h).trans
      ((thickening_thickening_subset ε δ B).trans (thickening_mono hle B))
  exact closure_mono (convexHull_mono
    (biUnion_subset_biUnion_left (inter_subset_inter_left _ h1)))

lemma lc_cone_subset_coneHull {ε : ℝ} {A : Set V} {x : V} (hx : x ∈ thickening ε A)
    (hM : x ∈ S.M) :
    S.CC x ⊆ S.coneHull ε A := fun _ hv =>
  subset_closure (subset_convexHull ℝ _ (mem_iUnion₂.2 ⟨x, ⟨hx, hM⟩, hv⟩))

/-- **Mean value theorem, convex-hull form.** If `γ` is differentiable on `(s,t)` and continuous on
`[s,t]` and its derivatives on `(s,t)` lie in a closed convex set `K`, then so does the chord
quotient. Proof by Hahn–Banach separation and the scalar mean value theorem. -/
theorem lc_chord_mem_of_deriv_mem {γ γ' : ℝ → V} {s t : ℝ} (hst : s < t)
    (hc : ContinuousOn γ (Icc s t)) (hd : ∀ r ∈ Ioo s t, HasDerivAt γ (γ' r) r)
    {K : Set V} (hK : Convex ℝ K) (hKc : IsClosed K) (hγ' : ∀ r ∈ Ioo s t, γ' r ∈ K) :
    (t - s)⁻¹ • (γ t - γ s) ∈ K := by
  by_contra h
  obtain ⟨f, u, hfK, hu⟩ := geometric_hahn_banach_closed_point hK hKc h
  obtain ⟨c, hc', hceq⟩ := exists_hasDerivAt_eq_slope (fun r => f (γ r)) (fun r => f (γ' r)) hst
    (f.continuous.comp_continuousOn hc)
    (fun r hr => f.hasFDerivAt.comp_hasDerivAt r (hd r hr))
  have h1 := hfK _ (hγ' c hc')
  have h2 : f ((t - s)⁻¹ • (γ t - γ s)) = f (γ' c) := by
    rw [hceq, map_smul, map_sub, smul_eq_mul, div_eq_inv_mul]
  linarith

/-! ### The bridge from campaign 60 -/

/-- **Bridge, curve form.** A `C¹` curve that stays in `M` on `[0,1]` with velocity in the closed
future cone is a Lipschitz future-causal curve. -/
theorem lc_c1_lipCausal {γ : ℝ → V} (hγ : ContDiff ℝ 1 γ)
    (hc : ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ S.M ∧ deriv γ t ∈ S.CC (γ t)) : S.LipCausal γ := by
  refine ⟨?_, fun t ht => (hc t ht).1, ?_⟩
  · exact (hγ.locallyLipschitz.locallyLipschitzOn).exists_lipschitzOnWith_of_compact isCompact_Icc
  · intro s t hs hst ht ε hε
    refine lc_chord_mem_of_deriv_mem hst hγ.continuous.continuousOn
      (fun r _ => ((hγ.differentiable one_ne_zero) r).hasDerivAt) (S.lc_convex_coneHull _ _)
      (S.lc_isClosed_coneHull _ _) fun r hr => ?_
    have hrI : r ∈ Icc (0:ℝ) 1 := ⟨by linarith [hr.1], by linarith [hr.2]⟩
    obtain ⟨hM, hC⟩ := hc r hrI
    exact S.lc_cone_subset_coneHull (self_subset_thickening hε (γ '' Icc s t)
      (mem_image_of_mem γ (Ioo_subset_Icc_self hr))) hM hC

/-- **Bridge.** A `C¹` future-causal step of campaign 60 is a Lipschitz future-causal curve. -/
theorem lc_cstep_lstep {x y : V} (h : S.CStep x y) : S.LStep x y := by
  obtain ⟨γ, hγ, h0, h1, hc⟩ := h
  exact ⟨γ, S.lc_c1_lipCausal hγ fun t ht => ⟨(hc t ht).1, (hc t ht).2.1, (hc t ht).2.2.le⟩,
    h0, h1⟩

/-- **Bridge, relation form.** Campaign 60's `≤` is contained in the Lipschitz causal relation. -/
theorem lc_cau_lcau {x y : V} (h : S.Cau x y) : S.LCau x y := by
  induction h with
  | refl => exact Relation.ReflTransGen.refl
  | tail _ h ih => exact ih.tail (S.lc_cstep_lstep h)

/-! ### The limit-curve lemma -/

/-- **Limit-curve lemma.** A uniform limit on `[0,1]` of uniformly `L`-Lipschitz curves into a
closed `K ⊆ M`, each satisfying the cone condition, is `L`-Lipschitz, maps into `K`, and is a
Lipschitz future-causal curve. No uniform modulus is needed. -/
theorem lc_limit_curve {F : ℕ → ℝ → V} {γ : ℝ → V} {K : Set V} (hK : IsClosed K)
    (hKM : K ⊆ S.M) {L : NNReal} (hLip : ∀ n, LipschitzOnWith L (F n) (Icc 0 1))
    (hmem : ∀ n, MapsTo (F n) (Icc 0 1) K) (hc : ∀ n, S.ConeCond (F n))
    (hu : TendstoUniformlyOn F γ atTop (Icc 0 1)) :
    LipschitzOnWith L γ (Icc 0 1) ∧ MapsTo γ (Icc 0 1) K ∧ S.LipCausal γ := by
  have hp : ∀ t ∈ Icc (0:ℝ) 1, Tendsto (fun n => F n t) atTop (𝓝 (γ t)) :=
    fun t ht => hu.tendsto_at ht
  have hL : LipschitzOnWith L γ (Icc 0 1) := by
    refine LipschitzOnWith.of_dist_le_mul fun x hx y hy => ?_
    exact le_of_tendsto' ((hp x hx).dist (hp y hy)) fun n => (hLip n).dist_le_mul x hx y hy
  have hK' : MapsTo γ (Icc 0 1) K := fun t ht =>
    hK.mem_of_tendsto (hp t ht) (Eventually.of_forall fun n => hmem n ht)
  refine ⟨hL, hK', ⟨L, hL⟩, fun t ht => hKM (hK' ht), ?_⟩
  intro s t hs hst ht ε hε
  have hsI : s ∈ Icc (0:ℝ) 1 := ⟨hs, by linarith⟩
  have htI : t ∈ Icc (0:ℝ) 1 := ⟨by linarith, ht⟩
  have hq : Tendsto (fun n => (t - s)⁻¹ • (F n t - F n s)) atTop
      (𝓝 ((t - s)⁻¹ • (γ t - γ s))) :=
    ((hp t htI).sub (hp s hsI)).const_smul _
  refine (S.lc_isClosed_coneHull _ _).mem_of_tendsto hq ?_
  filter_upwards [Metric.tendstoUniformlyOn_iff.1 hu (ε / 2) (by linarith)] with n hn
  refine S.lc_coneHull_mono (ε := ε / 2) (δ := ε / 2) ?_ (by linarith) (hc n s t hs hst ht _
    (by linarith))
  rintro _ ⟨r, hr, rfl⟩
  have hrI : r ∈ Icc (0:ℝ) 1 := ⟨by linarith [hr.1], by linarith [hr.2]⟩
  exact mem_thickening_iff.2 ⟨γ r, ⟨r, hr, rfl⟩, by rw [dist_comm]; exact hn r hrI⟩

/-- **Arzelà–Ascoli corollary.** A sequence of uniformly `L`-Lipschitz curves into a compact
`K ⊆ M`, each satisfying the cone condition, has a subsequence converging uniformly on `[0,1]`, and
its limit is an `L`-Lipschitz future-causal curve into `K`. -/
theorem lc_arzela_ascoli {F : ℕ → ℝ → V} {K : Set V} (hK : IsCompact K) (hKM : K ⊆ S.M)
    {L : NNReal} (hLip : ∀ n, LipschitzOnWith L (F n) (Icc 0 1))
    (hmem : ∀ n, MapsTo (F n) (Icc 0 1) K) (hc : ∀ n, S.ConeCond (F n)) :
    ∃ φ : ℕ → ℕ, StrictMono φ ∧ ∃ γ : ℝ → V,
      TendstoUniformlyOn (fun n => F (φ n)) γ atTop (Icc 0 1) ∧
      LipschitzOnWith L γ (Icc 0 1) ∧ MapsTo γ (Icc 0 1) K ∧ S.LipCausal γ := by
  let G : ℕ → (Icc (0:ℝ) 1 →ᵇ V) := fun n =>
    BoundedContinuousFunction.mkOfCompact
      ⟨fun x => F n x, (hLip n).to_restrict.continuous⟩
  have hGL : ∀ n, LipschitzWith L (G n) := fun n => (hLip n).to_restrict
  have hA : IsCompact (closure (range G)) := by
    refine BoundedContinuousFunction.arzela_ascoli K hK (range G) ?_ ?_
    · rintro f x ⟨n, rfl⟩; exact hmem n x.2
    · refine (LipschitzWith.uniformEquicontinuous
        (fun f : range G => ⇑(f : Icc (0:ℝ) 1 →ᵇ V)) L ?_).equicontinuous
      rintro ⟨f, n, rfl⟩; exact hGL n
  obtain ⟨a, -, φ, hφ, hlim⟩ := hA.tendsto_subseq (fun n => subset_closure (mem_range_self n))
  have hU := BoundedContinuousFunction.tendsto_iff_tendstoUniformly.1 hlim
  let γ : ℝ → V := fun r => a (projIcc 0 1 zero_le_one r)
  have hu : TendstoUniformlyOn (fun n => F (φ n)) γ atTop (Icc 0 1) := by
    rw [Metric.tendstoUniformlyOn_iff]
    intro ε hε
    filter_upwards [Metric.tendstoUniformly_iff.1 hU ε hε] with n hn
    intro x hx
    have := hn ⟨x, hx⟩
    simp only [γ, projIcc_of_mem _ hx]
    exact this
  exact ⟨φ, hφ, γ, hu, S.lc_limit_curve hK.isClosed hKM (fun n => hLip (φ n))
    (fun n => hmem (φ n)) (fun n => hc (φ n)) hu⟩

/-- **Closedness of the Lipschitz causal step under limits.** If `pₙ → p`, `qₙ → q`, and each `pₙ`
is joined to `qₙ` by a Lipschitz causal piece, uniformly `L`-Lipschitz and inside a compact
`K ⊆ M`, then `p` is joined to `q` by a Lipschitz causal piece inside `K`. -/
theorem lc_lstep_of_limit {F : ℕ → ℝ → V} {K : Set V} (hK : IsCompact K) (hKM : K ⊆ S.M)
    {L : NNReal} (hLip : ∀ n, LipschitzOnWith L (F n) (Icc 0 1))
    (hmem : ∀ n, MapsTo (F n) (Icc 0 1) K) (hc : ∀ n, S.ConeCond (F n))
    {P Q : ℕ → V} {p q : V} (h0 : ∀ n, F n 0 = P n) (h1 : ∀ n, F n 1 = Q n)
    (hP : Tendsto P atTop (𝓝 p)) (hQ : Tendsto Q atTop (𝓝 q)) :
    ∃ γ : ℝ → V, S.LipCausal γ ∧ MapsTo γ (Icc 0 1) K ∧ γ 0 = p ∧ γ 1 = q := by
  obtain ⟨φ, hφ, γ, hu, -, hγK, hγ⟩ := S.lc_arzela_ascoli hK hKM hLip hmem hc
  refine ⟨γ, hγ, hγK, ?_, ?_⟩
  · refine tendsto_nhds_unique (hu.tendsto_at ⟨le_rfl, zero_le_one⟩) ?_
    simpa [Function.comp_def, h0] using hP.comp hφ.tendsto_atTop
  · refine tendsto_nhds_unique (hu.tendsto_at ⟨zero_le_one, le_rfl⟩) ?_
    simpa [Function.comp_def, h1] using hQ.comp hφ.tendsto_atTop

/-! ### Faithfulness: velocities of Lipschitz causal curves -/

/-- The *outer cone* at `x`: `Ĉ x = ⋂_{ε>0}` closed convex hull of the cones over `B(x,ε) ∩ M`. -/
def coneHat (x : V) : Set V := ⋂ ε > 0, S.coneHull ε {x}

lemma lc_cone_subset_coneHat {x : V} (hx : x ∈ S.M) : S.CC x ⊆ S.coneHat x :=
  fun _ hv => mem_iInter₂.2 fun _ hε =>
    S.lc_cone_subset_coneHull (self_subset_thickening hε _ (mem_singleton x)) hx hv

/-- **Velocity lemma.** Wherever a Lipschitz causal curve has a right derivative `v` at
`s ∈ [0,1)`, `v` lies in the outer cone `Ĉ(γ s)`. -/
theorem lc_velocity_mem_coneHat {γ : ℝ → V} (hγ : S.LipCausal γ) {s : ℝ} (hs0 : 0 ≤ s)
    (hs1 : s < 1) {v : V} (hv : HasDerivWithinAt γ v (Ioi s) s) : v ∈ S.coneHat (γ s) := by
  obtain ⟨⟨L, hL⟩, -, hcone⟩ := hγ
  refine mem_iInter₂.2 fun ε hε => ?_
  have hcont : ContinuousWithinAt γ (Icc 0 1) s := hL.continuousOn s ⟨hs0, hs1.le⟩
  obtain ⟨δ, hδ, hδP⟩ := Metric.continuousWithinAt_iff.1 hcont (ε / 2) (by linarith)
  have hsl : Tendsto (slope γ s) (𝓝[>] s) (𝓝 v) :=
    (hasDerivWithinAt_iff_tendsto_slope' (lt_irrefl s)).1 hv
  refine (S.lc_isClosed_coneHull _ _).mem_of_tendsto hsl ?_
  filter_upwards [Ioo_mem_nhdsGT (show s < min (s + δ) 1 from lt_min (by linarith) hs1)]
    with t ht
  have hm1 := min_le_left (s + δ) 1
  have hm2 := min_le_right (s + δ) 1
  rw [slope_def_module]
  refine S.lc_coneHull_mono (ε := ε / 2) (δ := ε / 2) ?_ (by linarith)
    (hcone s t hs0 ht.1 (by linarith [ht.2]) _ (by linarith))
  rintro _ ⟨r, hr, rfl⟩
  rw [thickening_singleton, mem_ball]
  refine hδP ⟨by linarith [hr.1], by linarith [hr.2, ht.2]⟩ ?_
  rw [Real.dist_eq, abs_lt]; constructor <;> linarith [hr.1, hr.2, ht.2]

/-- Velocity lemma, sharp form: under the cone-semicontinuity property `Ĉ(γ s) ⊆ C(γ s)`, a right
derivative of a Lipschitz causal curve lies in the closed future cone `C(γ s)`. -/
theorem lc_velocity_mem_cone {γ : ℝ → V} (hγ : S.LipCausal γ) {s : ℝ} (hs0 : 0 ≤ s)
    (hs1 : s < 1) {v : V} (hv : HasDerivWithinAt γ v (Ioi s) s)
    (husc : S.coneHat (γ s) ⊆ S.CC (γ s)) : v ∈ S.CC (γ s) :=
  husc (S.lc_velocity_mem_coneHat hγ hs0 hs1 hv)


/-! ### Reverse Cauchy–Schwarz, convexity of the closed cone, and cone semicontinuity -/

lemma lc_cont_gvw {X : Type*} [TopologicalSpace X] {x v w : X → V} (hx : Continuous x)
    (hv : Continuous v) (hw : Continuous w) : Continuous fun a => S.g (x a) (v a) (w a) :=
  ((S.cont_g.comp hx).clm_apply hv).clm_apply hw

lemma lc_perp_nonneg {x : V} (hx : x ∈ S.M) {u : V} (hu : S.g x u (S.T x) = 0) :
    0 ≤ S.g x u u := by
  by_cases h : u = 0
  · simp [h]
  · exact (S.pos_on_perp x hx u hu h).le

/-- Cauchy–Schwarz for `g_x` on the `g_x`-orthogonal complement of `T x`, where it is positive
semidefinite. -/
lemma lc_cs_perp {x : V} (hx : x ∈ S.M) {u w : V} (hu : S.g x u (S.T x) = 0)
    (hw : S.g x w (S.T x) = 0) : S.g x u w ^ 2 ≤ S.g x u u * S.g x w w := by
  have h : ∀ c : ℝ, 0 ≤ S.g x w w * (c * c) + (2 * S.g x u w) * c + S.g x u u := by
    intro c
    have h1 : S.g x (u + c • w) (S.T x) = 0 := by simp [hu, hw]
    have h2 := S.lc_perp_nonneg hx h1
    have hs := S.symm x w u
    simp only [map_add, map_smul, FunLike.coe_add, Pi.add_apply, FunLike.coe_smul,
      Pi.smul_apply, smul_eq_mul] at h2
    rw [hs] at h2
    linarith
  have := discrim_le_zero h
  unfold discrim at this
  nlinarith [this]

/-- **Reverse Cauchy–Schwarz.** For `u, w` in the closed future cone at `x ∈ M`,
`g_x(u,w) ≤ 0`; strictly if `u ≠ 0` and `w` is timelike. -/
theorem lc_reverse_cs {x : V} (hx : x ∈ S.M) {u w : V} (hu : u ∈ S.CC x) (hw : w ∈ S.CC x) :
    S.g x u w ≤ 0 ∧ (u ≠ 0 → S.g x w w < 0 → S.g x u w < 0) := by
  obtain ⟨huu, huT⟩ := hu
  obtain ⟨hww, hwT⟩ := hw
  have ht : S.g x (S.T x) (S.T x) < 0 := S.T_timelike x hx
  obtain ⟨t, htd⟩ : ∃ t, S.g x (S.T x) (S.T x) = t := ⟨_, rfl⟩
  rw [htd] at ht
  obtain ⟨a, ha⟩ : ∃ a, S.g x u (S.T x) = a * t :=
    ⟨S.g x u (S.T x) / t, (div_mul_cancel₀ _ ht.ne).symm⟩
  obtain ⟨b, hb⟩ : ∃ b, S.g x w (S.T x) = b * t :=
    ⟨S.g x w (S.T x) / t, (div_mul_cancel₀ _ ht.ne).symm⟩
  have ha0 : 0 ≤ a := by nlinarith
  have hb0 : 0 ≤ b := by nlinarith
  have hTu : S.g x (S.T x) u = a * t := by rw [S.symm, ha]
  have hTw : S.g x (S.T x) w = b * t := by rw [S.symm, hb]
  have hwu : S.g x w u = S.g x u w := S.symm _ _ _
  have hu'T : S.g x (u - a • S.T x) (S.T x) = 0 := by simp [ha, htd]
  have hw'T : S.g x (w - b • S.T x) (S.T x) = 0 := by simp [hb, htd]
  have hu'u' : S.g x (u - a • S.T x) (u - a • S.T x) = S.g x u u - a ^ 2 * t := by
    simp [ha, hTu, htd]; ring
  have hw'w' : S.g x (w - b • S.T x) (w - b • S.T x) = S.g x w w - b ^ 2 * t := by
    simp [hb, hTw, htd]; ring
  have hu'w' : S.g x (u - a • S.T x) (w - b • S.T x) = S.g x u w - a * b * t := by
    simp [ha, hTw, htd]; ring
  have hA := S.lc_perp_nonneg hx hu'T
  have hB := S.lc_perp_nonneg hx hw'T
  have hcs := S.lc_cs_perp hx hu'T hw'T
  rw [hu'u'] at hA
  rw [hw'w'] at hB
  rw [hu'u', hw'w', hu'w'] at hcs
  have hab : 0 ≤ -(a * b * t) := by nlinarith [mul_nonneg ha0 hb0]
  have hAB : (S.g x u u - a ^ 2 * t) * (S.g x w w - b ^ 2 * t) ≤
      (-(a ^ 2 * t)) * (-(b ^ 2 * t)) :=
    mul_le_mul (by linarith) (by linarith) hB (by nlinarith [sq_nonneg a])
  refine ⟨?_, fun hu0 hwt => ?_⟩
  · have key : (S.g x u w - a * b * t) ^ 2 ≤ (-(a * b * t)) ^ 2 := by nlinarith
    have := (abs_le_of_sq_le_sq' key hab).2
    linarith
  · have hapos : 0 < a := by
      rcases ha0.lt_or_eq with h | h
      · exact h
      · exfalso
        subst h
        have hu'eq : u - (0:ℝ) • S.T x = u := by simp
        rw [hu'eq] at hu'T
        have := S.pos_on_perp x hx u hu'T hu0
        linarith
    have hbpos : 0 < b := by
      rcases hb0.lt_or_eq with h | h
      · exact h
      · exfalso
        subst h
        have : S.g x w (S.T x) = 0 := by rw [hb]; ring
        have := S.lc_perp_nonneg hx this
        linarith
    have hAB' : (S.g x u u - a ^ 2 * t) * (S.g x w w - b ^ 2 * t) <
        (-(a ^ 2 * t)) * (-(b ^ 2 * t)) := by
      have h1 : (S.g x u u - a ^ 2 * t) * (S.g x w w - b ^ 2 * t) ≤
          (-(a ^ 2 * t)) * (S.g x w w - b ^ 2 * t) :=
        mul_le_mul_of_nonneg_right (by linarith) hB
      have h2 : (-(a ^ 2 * t)) * (S.g x w w - b ^ 2 * t) < (-(a ^ 2 * t)) * (-(b ^ 2 * t)) :=
        mul_lt_mul_of_pos_left (by linarith) (by nlinarith [mul_pos hapos hapos])
      linarith
    have key : (S.g x u w - a * b * t) ^ 2 < (-(a * b * t)) ^ 2 := by nlinarith
    have := (abs_lt_of_sq_lt_sq' key hab).2
    linarith

lemma lc_cone_smul {x u : V} {c : ℝ} (hc : 0 ≤ c) (hu : u ∈ S.CC x) : c • u ∈ S.CC x := by
  obtain ⟨h1, h2⟩ := hu
  refine ⟨?_, ?_⟩
  · simp only [map_smul, FunLike.coe_smul, Pi.smul_apply, smul_eq_mul]
    nlinarith [mul_nonneg hc hc]
  · simp only [map_smul, FunLike.coe_smul, Pi.smul_apply, smul_eq_mul]
    nlinarith

/-- **Convexity of the closed future cone** at every `x ∈ M` (from reverse Cauchy–Schwarz). -/
theorem lc_convex_cone {x : V} (hx : x ∈ S.M) : Convex ℝ (S.CC x) := by
  intro u hu w hw α β hα hβ _
  have h1 := (S.lc_reverse_cs hx hu hw).1
  have hwu := S.symm x w u
  obtain ⟨huu, huT⟩ := hu
  obtain ⟨hww, hwT⟩ := hw
  refine ⟨?_, ?_⟩
  · simp only [map_add, map_smul, FunLike.coe_add, Pi.add_apply, FunLike.coe_smul,
      Pi.smul_apply, smul_eq_mul]
    rw [hwu]
    nlinarith [mul_nonneg hα hβ, mul_nonneg hα hα, mul_nonneg hβ hβ,
      mul_nonpos_of_nonneg_of_nonpos (mul_nonneg hα hβ) h1,
      mul_nonpos_of_nonneg_of_nonpos (mul_nonneg hα hα) huu,
      mul_nonpos_of_nonneg_of_nonpos (mul_nonneg hβ hβ) hww]
  · simp only [map_add, map_smul, FunLike.coe_add, Pi.add_apply, FunLike.coe_smul,
      Pi.smul_apply, smul_eq_mul]
    nlinarith [mul_nonpos_of_nonneg_of_nonpos hα huT, mul_nonpos_of_nonneg_of_nonpos hβ hwT]

/-- Uniform coercivity near `x` (finite dimension): pairing with a fixed timelike `w` controls the
norm of causal vectors at all nearby points. -/
lemma lc_coercive [FiniteDimensional ℝ V] {x : V} (hx : x ∈ S.M) {w : V}
    (hw : S.g x w w < 0) (hwT : S.g x w (S.T x) < 0) :
    ∃ r > 0, ∃ c > 0, ∀ y ∈ closedBall x r, ∀ u ∈ S.CC y, S.g y u w ≤ -(c * ‖u‖) := by
  have hO : IsOpen {y | y ∈ S.M ∧ S.g y w w < 0 ∧ S.g y w (S.T y) < 0} :=
    S.isOpen_M.inter ((isOpen_lt (S.lc_cont_gvw continuous_id continuous_const continuous_const)
      continuous_const).inter
      (isOpen_lt (S.lc_cont_gvw continuous_id continuous_const S.cont_T) continuous_const))
  obtain ⟨r0, hr0, hball⟩ := Metric.isOpen_iff.1 hO x ⟨hx, hw, hwT⟩
  have hr : 0 < r0 / 2 := by positivity
  have hsub : closedBall x (r0 / 2) ⊆ {y | y ∈ S.M ∧ S.g y w w < 0 ∧ S.g y w (S.T y) < 0} :=
    (closedBall_subset_ball (by linarith)).trans hball
  let Z : Set (V × V) := {p | p.1 ∈ closedBall x (r0 / 2) ∧ p.2 ∈ sphere (0:V) 1 ∧
    S.g p.1 p.2 p.2 ≤ 0 ∧ S.g p.1 p.2 (S.T p.1) ≤ 0}
  have hZc : IsCompact Z := by
    refine ((isCompact_closedBall x (r0 / 2)).prod (isCompact_sphere (0:V) 1)).of_isClosed_subset
      ?_ ?_
    · exact (isClosed_closedBall.preimage continuous_fst).inter
        ((isClosed_sphere.preimage continuous_snd).inter
        ((isClosed_le (S.lc_cont_gvw continuous_fst continuous_snd continuous_snd)
          continuous_const).inter
        (isClosed_le (S.lc_cont_gvw continuous_fst continuous_snd (S.cont_T.comp continuous_fst))
          continuous_const)))
    · rintro p ⟨h1, h2, -⟩; exact ⟨h1, h2⟩
  have hf : Continuous fun p : V × V => S.g p.1 p.2 w :=
    S.lc_cont_gvw continuous_fst continuous_snd continuous_const
  have hnorm : ∀ u : V, u ≠ 0 → ‖u‖⁻¹ • u ∈ sphere (0:V) 1 := fun u hu => by
    rw [mem_sphere_zero_iff_norm]; exact norm_smul_inv_norm hu
  rcases Z.eq_empty_or_nonempty with hZ | hZ
  · refine ⟨r0 / 2, hr, 1, one_pos, fun y hy u hu => ?_⟩
    by_cases hu0 : u = 0
    · simp [hu0]
    · exfalso
      have hs := S.lc_cone_smul (inv_nonneg.2 (norm_nonneg u)) hu
      have hmem : (y, ‖u‖⁻¹ • u) ∈ Z := ⟨hy, hnorm u hu0, hs.1, hs.2⟩
      rw [hZ] at hmem; exact hmem
  · obtain ⟨p, hpZ, hmax⟩ := hZc.exists_isMaxOn hZ hf.continuousOn
    obtain ⟨hp1, hp2, hp3, hp4⟩ := hpZ
    have hyM := hsub hp1
    have hp0 : p.2 ≠ 0 := by
      intro h; rw [h, mem_sphere_zero_iff_norm, norm_zero] at hp2; exact zero_ne_one hp2
    have hneg : S.g p.1 p.2 w < 0 :=
      (S.lc_reverse_cs hyM.1 ⟨hp3, hp4⟩ ⟨hyM.2.1.le, hyM.2.2.le⟩).2 hp0 hyM.2.1
    refine ⟨r0 / 2, hr, -S.g p.1 p.2 w, by linarith, fun y hy u hu => ?_⟩
    by_cases hu0 : u = 0
    · simp [hu0]
    · have hn : 0 < ‖u‖ := norm_pos_iff.2 hu0
      have hs := S.lc_cone_smul (inv_nonneg.2 hn.le) hu
      have hmem : (y, ‖u‖⁻¹ • u) ∈ Z := ⟨hy, hnorm u hu0, hs.1, hs.2⟩
      have h1 : S.g y (‖u‖⁻¹ • u) w ≤ S.g p.1 p.2 w := isMaxOn_iff.1 hmax _ hmem
      have h2 : S.g y (‖u‖⁻¹ • u) w = ‖u‖⁻¹ * S.g y u w := by simp
      rw [h2] at h1
      have h3 : S.g y u w = ‖u‖ * (‖u‖⁻¹ * S.g y u w) := by field_simp
      rw [h3]
      nlinarith [mul_le_mul_of_nonneg_left h1 hn.le]

/-- Near `x`, every closed cone lies in the closed half-space `{u | g_x(u,w) ≤ 0}` cut out by a
timelike `w` at `x` (finite dimension). -/
lemma lc_halfspace [FiniteDimensional ℝ V] {x : V} (hx : x ∈ S.M) {w : V}
    (hw : S.g x w w < 0) (hwT : S.g x w (S.T x) < 0) :
    ∃ ε > 0, ∀ y ∈ ball x ε, ∀ u ∈ S.CC y, S.g x u w ≤ 0 := by
  obtain ⟨r, hr, c, hc, hco⟩ := S.lc_coercive hx hw hwT
  have hcn : Continuous fun y => dist (S.g y) (S.g x) := S.cont_g.dist continuous_const
  obtain ⟨δ, hδ, hδP⟩ := Metric.eventually_nhds_iff.1 (hcn.continuousAt.eventually
    (Iio_mem_nhds (show dist (S.g x) (S.g x) < c / (‖w‖ + 1) by rw [dist_self]; positivity)))
  refine ⟨min r δ, lt_min hr hδ, fun y hy u hu => ?_⟩
  have hyr : y ∈ closedBall x r :=
    ball_subset_closedBall (ball_subset_ball (min_le_left _ _) hy)
  have hyd : dist y x < δ := lt_of_lt_of_le (mem_ball.1 hy) (min_le_right _ _)
  have h1 := hco y hyr u hu
  have h2 : ‖S.g y - S.g x‖ < c / (‖w‖ + 1) := by
    have e : dist (S.g y) (S.g x) = ‖S.g y - S.g x‖ := by exact dist_eq_norm (S.g y) (S.g x)
    rw [← e]; exact hδP hyd
  have h3 : |S.g y u w - S.g x u w| ≤ ‖S.g y - S.g x‖ * ‖u‖ * ‖w‖ := by
    have := (S.g y - S.g x).le_opNorm₂ u w
    simpa [Real.norm_eq_abs] using this
  have h4 : ‖S.g y - S.g x‖ * ‖w‖ ≤ c := by
    have hw0 := norm_nonneg w
    have h5 : c / (‖w‖ + 1) * ‖w‖ ≤ c := by
      rw [div_mul_eq_mul_div, div_le_iff₀ (by positivity)]; nlinarith
    have h6 := mul_le_mul_of_nonneg_right h2.le hw0
    linarith
  have h5 := (abs_le.1 h3).1
  have hu0 := norm_nonneg u
  nlinarith [mul_le_mul_of_nonneg_left h4 hu0]

/-- **Cone semicontinuity** (finite dimension): the outer cone `Ĉ x` equals the closed future
cone `C x` at every `x ∈ M`. -/
theorem lc_coneHat_eq_cone [FiniteDimensional ℝ V] {x : V} (hx : x ∈ S.M) :
    S.coneHat x = S.CC x := by
  refine Subset.antisymm (fun v hv => ?_) (S.lc_cone_subset_coneHat hx)
  have hdual : ∀ w, S.g x w w < 0 → S.g x w (S.T x) < 0 → S.g x v w ≤ 0 := by
    intro w hw hwT
    obtain ⟨ε, hε, hH⟩ := S.lc_halfspace hx hw hwT
    have hvε := mem_iInter₂.1 hv ε hε
    have hHc : IsClosed {u : V | S.g x u w ≤ 0} :=
      isClosed_le ((S.g x).continuous.clm_apply continuous_const) continuous_const
    have hHv : Convex ℝ {u : V | S.g x u w ≤ 0} := by
      intro a ha b hb α β hα hβ _
      simp only [mem_ofPred_eq, map_add, map_smul, FunLike.coe_add, Pi.add_apply,
        FunLike.coe_smul, Pi.smul_apply, smul_eq_mul] at ha hb ⊢
      nlinarith [mul_nonpos_of_nonneg_of_nonpos hα ha, mul_nonpos_of_nonneg_of_nonpos hβ hb]
    have hsub : S.coneHull ε {x} ⊆ {u | S.g x u w ≤ 0} := by
      refine closure_minimal (convexHull_min ?_ hHv) hHc
      refine iUnion₂_subset fun y hy => ?_
      rw [thickening_singleton] at hy
      exact fun u hu => hH y hy.1 u hu
    exact hsub hvε
  have hT := S.T_timelike x hx
  have hvT : S.g x v (S.T x) ≤ 0 := hdual _ hT hT
  refine ⟨?_, hvT⟩
  by_contra hpos
  push Not at hpos
  obtain ⟨t, htd⟩ : ∃ t, S.g x (S.T x) (S.T x) = t := ⟨_, rfl⟩
  rw [htd] at hT
  obtain ⟨a, ha⟩ : ∃ a, S.g x v (S.T x) = a * t :=
    ⟨S.g x v (S.T x) / t, (div_mul_cancel₀ _ hT.ne).symm⟩
  have ha0 : 0 ≤ a := by nlinarith
  have hTv : S.g x (S.T x) v = a * t := by rw [S.symm, ha]
  obtain ⟨q, hq⟩ : ∃ q, S.g x v v = q + a ^ 2 * t := ⟨S.g x v v - a ^ 2 * t, by ring⟩
  have hq1 : a ^ 2 * (-t) < q := by linarith
  have hq0 : 0 < q := by nlinarith [sq_nonneg a]
  have hτ : 0 < -t := by linarith
  have hlt : a * (-t) / q < Real.sqrt ((-t) / q) := by
    rw [Real.lt_sqrt (by positivity), div_pow, div_lt_div_iff₀ (by positivity) hq0]
    nlinarith [mul_pos hτ hq0]
  obtain ⟨μ, hμ1, hμ2⟩ := exists_between hlt
  have hμ0 : 0 ≤ μ := le_trans (by positivity) hμ1.le
  have hμq : a * (-t) < μ * q := by rwa [div_lt_iff₀ hq0] at hμ1
  have hμsq : μ ^ 2 * q < -t := by
    have := (Real.lt_sqrt hμ0).1 hμ2
    rwa [lt_div_iff₀ hq0] at this
  have hww : S.g x (S.T x + μ • (v - a • S.T x)) (S.T x + μ • (v - a • S.T x)) =
      t + μ ^ 2 * q := by
    simp only [map_add, map_sub, map_smul, FunLike.coe_add, FunLike.coe_sub, Pi.add_apply,
      Pi.sub_apply, FunLike.coe_smul, Pi.smul_apply, smul_eq_mul, ha, hTv, htd, hq]
    ring
  have hwT : S.g x (S.T x + μ • (v - a • S.T x)) (S.T x) = t := by
    simp only [map_add, map_sub, map_smul, FunLike.coe_add, FunLike.coe_sub, Pi.add_apply,
      Pi.sub_apply, FunLike.coe_smul, Pi.smul_apply, smul_eq_mul, ha, htd]
    ring
  have hvw : S.g x v (S.T x + μ • (v - a • S.T x)) = a * t + μ * q := by
    simp only [map_add, map_sub, map_smul, FunLike.coe_add, FunLike.coe_sub, Pi.add_apply,
      Pi.sub_apply, FunLike.coe_smul, Pi.smul_apply, smul_eq_mul, ha, hTv, htd, hq]
    ring
  have := hdual _ (by rw [hww]; linarith) (by rw [hwT]; exact hT)
  rw [hvw] at this
  linarith

/-- **Velocity lemma, finite dimension.** Wherever a Lipschitz causal curve has a right derivative
`v` at `s ∈ [0,1)`, `v` lies in the closed future cone `C(γ s)`. No extra hypothesis. -/
theorem lc_velocity_mem_cone_fd [FiniteDimensional ℝ V] {γ : ℝ → V} (hγ : S.LipCausal γ)
    {s : ℝ} (hs0 : 0 ≤ s) (hs1 : s < 1) {v : V} (hv : HasDerivWithinAt γ v (Ioi s) s) :
    v ∈ S.CC (γ s) :=
  S.lc_velocity_mem_cone hγ hs0 hs1 hv
    (S.lc_coneHat_eq_cone (hγ.2.1 ⟨hs0, hs1.le⟩)).subset


/-- **Faithfulness for `C¹` curves** (finite dimension). A `C¹` curve is a Lipschitz future-causal
curve iff it stays in `M` on `[0,1]` with velocity in the closed future cone there. -/
theorem lc_c1_lipCausal_iff [FiniteDimensional ℝ V] {γ : ℝ → V} (hγ : ContDiff ℝ 1 γ) :
    S.LipCausal γ ↔ ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ S.M ∧ deriv γ t ∈ S.CC (γ t) := by
  refine ⟨fun h => ?_, S.lc_c1_lipCausal hγ⟩
  have hIco : ∀ t ∈ Ico (0:ℝ) 1, deriv γ t ∈ S.CC (γ t) := fun t ht =>
    S.lc_velocity_mem_cone_fd h ht.1 ht.2
      ((hγ.differentiable one_ne_zero) t).hasDerivAt.hasDerivWithinAt
  have hcl : IsClosed {t : ℝ | deriv γ t ∈ S.CC (γ t)} := by
    have hd : Continuous (deriv γ) := hγ.continuous_deriv le_rfl
    exact (isClosed_le (S.lc_cont_gvw hγ.continuous hd hd) continuous_const).inter
      (isClosed_le (S.lc_cont_gvw hγ.continuous hd (S.cont_T.comp hγ.continuous))
        continuous_const)
  have hIcc : Icc (0:ℝ) 1 ⊆ {t : ℝ | deriv γ t ∈ S.CC (γ t)} := by
    rw [← closure_Ico (zero_ne_one' ℝ)]
    exact closure_minimal hIco hcl
  exact fun t ht => ⟨h.2.1 ht, hIcc ht⟩

end Spacetime

open Spacetime
#print axioms lc_chord_mem_of_deriv_mem
#print axioms Spacetime.lc_c1_lipCausal
#print axioms Spacetime.lc_cstep_lstep
#print axioms Spacetime.lc_cau_lcau
#print axioms Spacetime.lc_limit_curve
#print axioms Spacetime.lc_arzela_ascoli
#print axioms Spacetime.lc_lstep_of_limit
#print axioms Spacetime.lc_velocity_mem_coneHat
#print axioms Spacetime.lc_velocity_mem_cone
#print axioms Spacetime.lc_reverse_cs
#print axioms Spacetime.lc_convex_cone
#print axioms Spacetime.lc_coneHat_eq_cone
#print axioms Spacetime.lc_velocity_mem_cone_fd
#print axioms Spacetime.lc_c1_lipCausal_iff

end ShadowProbe.LimitCurvesProbe

import Mathlib

/-!
# Probe `r7629+71.1` (campaign 65, `r7629` ①): concatenation of `LCau` chains, past-inextendible
# limit curves, and the ∂J⁻ generator with its approximants discharged

Registration: `computations/formalisation/r7629_71_campaign65/PREDICTION.md`. Setting: campaign 63's
`probes/CausalReparam.lean`, copied in whole (probes cannot import probes) under the namespace
`ShadowProbe.CausalConcatProbe`, with every theorem renamed `cr_* ↦ cc_*`. The copied part is
unchanged; its docstrings still describe campaign 63's results. The new material is at the end of
the file, after `cc_boundary_generator`.

## ① Concatenation (BUILT)

* `cc_chord_split`: for `s < m < t`, the chord quotient over `[s,t]` is the convex combination
  `((m−s)/(t−s)) q[s,m] + ((t−m)/(t−s)) q[m,t]`.
* `cc_coneCondOn_glue`: the cone condition on `[a,m]` and `[m,b]` gives it on `[a,b]`. A chord
  across `m` is split; each sub-chord lies in the cone hull of its sub-arc, hence of the whole arc
  (monotonicity), and the hull is convex.
* `cc_coneCondOn_affine`, `cc_coneCondOn_congr`: the pieces rescaled by `2`.
* `cc_join_lipschitz`: an `L₁`- and an `L₂`-Lipschitz piece join to a `2·max(L₁,L₂)`-Lipschitz
  curve (`cc_lipschitzOnWith_glue`).
* `cc_join_lipCausal`, `cc_lstep_trans`, `cc_lstepIn_trans`: `LStep x y → LStep y z → LStep x z`,
  and the same inside `K`.
* `cc_lcau_iff : LCau x y ↔ x = y ∨ LStep x y`, `cc_lcau_eq_reflGen : LCau = ReflGen LStep`,
  `cc_reflTransGen_lstepIn_iff` (inside `K`).

## ② Past-inextendibility (BUILT, with stated hypotheses)

* Definitions. `PastCausal γ`: `γ` on `[0,∞)` such that each unit piece run backwards,
  `r ↦ γ(n+1−r)`, is Lipschitz future-causal. `PastInextendible γ`: `γ t` has no limit in `M` as
  `t → ∞` (the standard no-endpoint form). `LeavesCompacts γ`: eventually outside every compact
  subset of `M`. `cc_inextendible_of_leaves`: the second implies the first.
* `cc_exit_step`: the last exits of the approximating curves from `int C` converge, along a
  subsequence, to `x' ∈ C ∖ int C`, joined to the previous point by a piece in `C`. This is campaign
  63's closedness `cc_lstepIn_of_limit` applied to the exit arcs.
* `cc_past_chain`: the recursive construction over a compact exhaustion `Kⱼ`, refining the
  subsequence at each stage. Each stage keeps only finitely many conditions, so no single diagonal
  subsequence is needed. It produces `x₀ = p` and `xⱼ₊₁ ∉ int Kⱼ₊₁` with a piece
  `xⱼ₊₁ → xⱼ` in `Kⱼ₊₁`.
* `cc_past_inextendible_limit`: the pieces concatenate (`chainCurve`) to a past-inextendible
  past-directed causal curve from `p`. `cc_past_inextendible_of_lcau` gives the same from `LCau`
  data, using ①. `cc_exists_exhaustion`: a compact exhaustion of `M` always exists.
* Hypotheses: a time functional `τⱼ` positive on the cones over each `Kⱼ`; approximating curves
  whose past endpoints eventually leave every compact set. **Non-imprisonment is not needed** for
  the standard form. It is needed only for `LeavesCompacts`, where it is taken as a hypothesis
  (`cc_past_inextendible_limit_leaves`, a direct consequence).

## ③ Stretch: the approximants of the ∂J⁻ generator (BUILT IN PART)

* `cc_approximants`: from `p ∈ closure J⁻_Lip(A)`, `p ∉ closure A`, and the causal-diamond
  hypothesis `J⁻_Lip(A) ∩ J⁺_Lip(U) ⊆ K` for a neighbourhood `U` of `p`, it derives the
  single-piece approximants in `K` that campaign 63 assumed.
* `cc_boundary_generator_of_diamond`: `cc_boundary_generator` with that hypothesis replaced.
* Not built: replacing the single compact `K` by the exhaustion, which would give a
  past-inextendible generator. The stop is uniformising `τ`: one `τ` positive over the whole
  diamond is still a hypothesis.
-/

open Set Filter Topology Metric
open scoped BoundedContinuousFunction Pointwise

namespace ShadowProbe.CausalConcatProbe

variable {V : Type*} [NormedAddCommGroup V] [NormedSpace ℝ V]

/-- A time-oriented Lorentzian chart (copied verbatim from `probes/LimitCurves.lean`). -/
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

lemma cc_isClosed_coneHull (ε : ℝ) (A : Set V) : IsClosed (S.coneHull ε A) := isClosed_closure

lemma cc_convex_coneHull (ε : ℝ) (A : Set V) : Convex ℝ (S.coneHull ε A) :=
  (convex_convexHull ℝ _).closure

/-- Monotonicity of the hull in the set and the radius. -/
lemma cc_coneHull_mono {ε δ ε' : ℝ} {A B : Set V} (h : A ⊆ thickening δ B) (hle : ε + δ ≤ ε') :
    S.coneHull ε A ⊆ S.coneHull ε' B := by
  have h1 : thickening ε A ⊆ thickening ε' B :=
    (thickening_subset_of_subset ε h).trans
      ((thickening_thickening_subset ε δ B).trans (thickening_mono hle B))
  exact closure_mono (convexHull_mono
    (biUnion_subset_biUnion_left (inter_subset_inter_left _ h1)))

lemma cc_cone_subset_coneHull {ε : ℝ} {A : Set V} {x : V} (hx : x ∈ thickening ε A)
    (hM : x ∈ S.M) :
    S.CC x ⊆ S.coneHull ε A := fun _ hv =>
  subset_closure (subset_convexHull ℝ _ (mem_iUnion₂.2 ⟨x, ⟨hx, hM⟩, hv⟩))

/-! ### The limit-curve lemma -/

/-- **Limit-curve lemma.** A uniform limit on `[0,1]` of uniformly `L`-Lipschitz curves into a
closed `K ⊆ M`, each satisfying the cone condition, is `L`-Lipschitz, maps into `K`, and is a
Lipschitz future-causal curve. No uniform modulus is needed. -/
theorem cc_limit_curve {F : ℕ → ℝ → V} {γ : ℝ → V} {K : Set V} (hK : IsClosed K)
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
  refine (S.cc_isClosed_coneHull _ _).mem_of_tendsto hq ?_
  filter_upwards [Metric.tendstoUniformlyOn_iff.1 hu (ε / 2) (by linarith)] with n hn
  refine S.cc_coneHull_mono (ε := ε / 2) (δ := ε / 2) ?_ (by linarith) (hc n s t hs hst ht _
    (by linarith))
  rintro _ ⟨r, hr, rfl⟩
  have hrI : r ∈ Icc (0:ℝ) 1 := ⟨by linarith [hr.1], by linarith [hr.2]⟩
  exact mem_thickening_iff.2 ⟨γ r, ⟨r, hr, rfl⟩, by rw [dist_comm]; exact hn r hrI⟩

/-- **Arzelà–Ascoli corollary.** A sequence of uniformly `L`-Lipschitz curves into a compact
`K ⊆ M`, each satisfying the cone condition, has a subsequence converging uniformly on `[0,1]`, and
its limit is an `L`-Lipschitz future-causal curve into `K`. -/
theorem cc_arzela_ascoli {F : ℕ → ℝ → V} {K : Set V} (hK : IsCompact K) (hKM : K ⊆ S.M)
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
  exact ⟨φ, hφ, γ, hu, S.cc_limit_curve hK.isClosed hKM (fun n => hLip (φ n))
    (fun n => hmem (φ n)) (fun n => hc (φ n)) hu⟩

/-- **Closedness of the Lipschitz causal step under limits.** If `pₙ → p`, `qₙ → q`, and each `pₙ`
is joined to `qₙ` by a Lipschitz causal piece, uniformly `L`-Lipschitz and inside a compact
`K ⊆ M`, then `p` is joined to `q` by a Lipschitz causal piece inside `K`. -/
theorem cc_lstep_of_limit {F : ℕ → ℝ → V} {K : Set V} (hK : IsCompact K) (hKM : K ⊆ S.M)
    {L : NNReal} (hLip : ∀ n, LipschitzOnWith L (F n) (Icc 0 1))
    (hmem : ∀ n, MapsTo (F n) (Icc 0 1) K) (hc : ∀ n, S.ConeCond (F n))
    {P Q : ℕ → V} {p q : V} (h0 : ∀ n, F n 0 = P n) (h1 : ∀ n, F n 1 = Q n)
    (hP : Tendsto P atTop (𝓝 p)) (hQ : Tendsto Q atTop (𝓝 q)) :
    ∃ γ : ℝ → V, S.LipCausal γ ∧ MapsTo γ (Icc 0 1) K ∧ γ 0 = p ∧ γ 1 = q := by
  obtain ⟨φ, hφ, γ, hu, -, hγK, hγ⟩ := S.cc_arzela_ascoli hK hKM hLip hmem hc
  refine ⟨γ, hγ, hγK, ?_, ?_⟩
  · refine tendsto_nhds_unique (hu.tendsto_at ⟨le_rfl, zero_le_one⟩) ?_
    simpa [Function.comp_def, h0] using hP.comp hφ.tendsto_atTop
  · refine tendsto_nhds_unique (hu.tendsto_at ⟨zero_le_one, le_rfl⟩) ?_
    simpa [Function.comp_def, h1] using hQ.comp hφ.tendsto_atTop

lemma cc_cont_gvw {X : Type*} [TopologicalSpace X] {x v w : X → V} (hx : Continuous x)
    (hv : Continuous v) (hw : Continuous w) : Continuous fun a => S.g (x a) (v a) (w a) :=
  ((S.cont_g.comp hx).clm_apply hv).clm_apply hw

lemma cc_perp_nonneg {x : V} (hx : x ∈ S.M) {u : V} (hu : S.g x u (S.T x) = 0) :
    0 ≤ S.g x u u := by
  by_cases h : u = 0
  · simp [h]
  · exact (S.pos_on_perp x hx u hu h).le

/-- Cauchy–Schwarz for `g_x` on the `g_x`-orthogonal complement of `T x`, where it is positive
semidefinite. -/
lemma cc_cs_perp {x : V} (hx : x ∈ S.M) {u w : V} (hu : S.g x u (S.T x) = 0)
    (hw : S.g x w (S.T x) = 0) : S.g x u w ^ 2 ≤ S.g x u u * S.g x w w := by
  have h : ∀ c : ℝ, 0 ≤ S.g x w w * (c * c) + (2 * S.g x u w) * c + S.g x u u := by
    intro c
    have h1 : S.g x (u + c • w) (S.T x) = 0 := by simp [hu, hw]
    have h2 := S.cc_perp_nonneg hx h1
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
theorem cc_reverse_cs {x : V} (hx : x ∈ S.M) {u w : V} (hu : u ∈ S.CC x) (hw : w ∈ S.CC x) :
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
  have hA := S.cc_perp_nonneg hx hu'T
  have hB := S.cc_perp_nonneg hx hw'T
  have hcs := S.cc_cs_perp hx hu'T hw'T
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
        have := S.cc_perp_nonneg hx this
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

lemma cc_cone_smul {x u : V} {c : ℝ} (hc : 0 ≤ c) (hu : u ∈ S.CC x) : c • u ∈ S.CC x := by
  obtain ⟨h1, h2⟩ := hu
  refine ⟨?_, ?_⟩
  · simp only [map_smul, FunLike.coe_smul, Pi.smul_apply, smul_eq_mul]
    nlinarith [mul_nonneg hc hc]
  · simp only [map_smul, FunLike.coe_smul, Pi.smul_apply, smul_eq_mul]
    nlinarith

/-- **Convexity of the closed future cone** at every `x ∈ M` (from reverse Cauchy–Schwarz). -/
theorem cc_convex_cone {x : V} (hx : x ∈ S.M) : Convex ℝ (S.CC x) := by
  intro u hu w hw α β hα hβ _
  have h1 := (S.cc_reverse_cs hx hu hw).1
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
lemma cc_coercive [FiniteDimensional ℝ V] {x : V} (hx : x ∈ S.M) {w : V}
    (hw : S.g x w w < 0) (hwT : S.g x w (S.T x) < 0) :
    ∃ r > 0, ∃ c > 0, ∀ y ∈ closedBall x r, ∀ u ∈ S.CC y, S.g y u w ≤ -(c * ‖u‖) := by
  have hO : IsOpen {y | y ∈ S.M ∧ S.g y w w < 0 ∧ S.g y w (S.T y) < 0} :=
    S.isOpen_M.inter ((isOpen_lt (S.cc_cont_gvw continuous_id continuous_const continuous_const)
      continuous_const).inter
      (isOpen_lt (S.cc_cont_gvw continuous_id continuous_const S.cont_T) continuous_const))
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
        ((isClosed_le (S.cc_cont_gvw continuous_fst continuous_snd continuous_snd)
          continuous_const).inter
        (isClosed_le (S.cc_cont_gvw continuous_fst continuous_snd (S.cont_T.comp continuous_fst))
          continuous_const)))
    · rintro p ⟨h1, h2, -⟩; exact ⟨h1, h2⟩
  have hf : Continuous fun p : V × V => S.g p.1 p.2 w :=
    S.cc_cont_gvw continuous_fst continuous_snd continuous_const
  have hnorm : ∀ u : V, u ≠ 0 → ‖u‖⁻¹ • u ∈ sphere (0:V) 1 := fun u hu => by
    rw [mem_sphere_zero_iff_norm]; exact norm_smul_inv_norm hu
  rcases Z.eq_empty_or_nonempty with hZ | hZ
  · refine ⟨r0 / 2, hr, 1, one_pos, fun y hy u hu => ?_⟩
    by_cases hu0 : u = 0
    · simp [hu0]
    · exfalso
      have hs := S.cc_cone_smul (inv_nonneg.2 (norm_nonneg u)) hu
      have hmem : (y, ‖u‖⁻¹ • u) ∈ Z := ⟨hy, hnorm u hu0, hs.1, hs.2⟩
      rw [hZ] at hmem; exact hmem
  · obtain ⟨p, hpZ, hmax⟩ := hZc.exists_isMaxOn hZ hf.continuousOn
    obtain ⟨hp1, hp2, hp3, hp4⟩ := hpZ
    have hyM := hsub hp1
    have hp0 : p.2 ≠ 0 := by
      intro h; rw [h, mem_sphere_zero_iff_norm, norm_zero] at hp2; exact zero_ne_one hp2
    have hneg : S.g p.1 p.2 w < 0 :=
      (S.cc_reverse_cs hyM.1 ⟨hp3, hp4⟩ ⟨hyM.2.1.le, hyM.2.2.le⟩).2 hp0 hyM.2.1
    refine ⟨r0 / 2, hr, -S.g p.1 p.2 w, by linarith, fun y hy u hu => ?_⟩
    by_cases hu0 : u = 0
    · simp [hu0]
    · have hn : 0 < ‖u‖ := norm_pos_iff.2 hu0
      have hs := S.cc_cone_smul (inv_nonneg.2 hn.le) hu
      have hmem : (y, ‖u‖⁻¹ • u) ∈ Z := ⟨hy, hnorm u hu0, hs.1, hs.2⟩
      have h1 : S.g y (‖u‖⁻¹ • u) w ≤ S.g p.1 p.2 w := isMaxOn_iff.1 hmax _ hmem
      have h2 : S.g y (‖u‖⁻¹ • u) w = ‖u‖⁻¹ * S.g y u w := by simp
      rw [h2] at h1
      have h3 : S.g y u w = ‖u‖ * (‖u‖⁻¹ * S.g y u w) := by field_simp
      rw [h3]
      nlinarith [mul_le_mul_of_nonneg_left h1 hn.le]

/-! ### Part ①: coercivity of a time functional over a compact set -/

lemma cc_isClosed_CC (x : V) : IsClosed (S.CC x) :=
  (isClosed_le (S.cc_cont_gvw continuous_const continuous_id continuous_id) continuous_const).inter
    (isClosed_le (S.cc_cont_gvw continuous_const continuous_id continuous_const) continuous_const)

lemma cc_zero_mem_CC (x : V) : (0 : V) ∈ S.CC x := by simp [CC]

/-- Strict half-space lemma (finite dimension): near `x`, every closed cone lies in the half-space
`{u | g_x(u,w) ≤ −c'‖u‖}` cut out by a future timelike `w` at `x`, with `c' > 0` uniform. -/
lemma cc_halfspace_strict [FiniteDimensional ℝ V] {x : V} (hx : x ∈ S.M) {w : V}
    (hw : S.g x w w < 0) (hwT : S.g x w (S.T x) < 0) :
    ∃ ε > 0, ∃ c > 0, ∀ y ∈ ball x ε, ∀ u ∈ S.CC y, S.g x u w ≤ -(c * ‖u‖) := by
  obtain ⟨r, hr, c, hc, hco⟩ := S.cc_coercive hx hw hwT
  have hcn : Continuous fun y => dist (S.g y) (S.g x) := S.cont_g.dist continuous_const
  obtain ⟨δ, hδ, hδP⟩ := Metric.eventually_nhds_iff.1 (hcn.continuousAt.eventually
    (Iio_mem_nhds (show dist (S.g x) (S.g x) < (c / 2) / (‖w‖ + 1) by
      rw [dist_self]; positivity)))
  refine ⟨min r δ, lt_min hr hδ, c / 2, by positivity, fun y hy u hu => ?_⟩
  have hyr : y ∈ closedBall x r :=
    ball_subset_closedBall (ball_subset_ball (min_le_left _ _) hy)
  have hyd : dist y x < δ := lt_of_lt_of_le (mem_ball.1 hy) (min_le_right _ _)
  have h1 := hco y hyr u hu
  have h2 : ‖S.g y - S.g x‖ < (c / 2) / (‖w‖ + 1) := by
    have e : dist (S.g y) (S.g x) = ‖S.g y - S.g x‖ := dist_eq_norm (S.g y) (S.g x)
    rw [← e]; exact hδP hyd
  have h3 : |S.g y u w - S.g x u w| ≤ ‖S.g y - S.g x‖ * ‖u‖ * ‖w‖ := by
    have := (S.g y - S.g x).le_opNorm₂ u w
    simpa [Real.norm_eq_abs] using this
  have h4 : ‖S.g y - S.g x‖ * ‖w‖ ≤ c / 2 := by
    have hw0 := norm_nonneg w
    have h5 : (c / 2) / (‖w‖ + 1) * ‖w‖ ≤ c / 2 := by
      rw [div_mul_eq_mul_div, div_le_iff₀ (by positivity)]; nlinarith
    have h6 := mul_le_mul_of_nonneg_right h2.le hw0
    linarith
  have h5 := (abs_le.1 h3).1
  have hu0 := norm_nonneg u
  nlinarith [mul_le_mul_of_nonneg_left h4 hu0]

/-- **Local time functional, derived from the timelike `T`.** At `x₀ ∈ M`, the linear functional
`τ₀ v = −g_{x₀}(v, T x₀)` is strictly positive on the nonzero closed future cones at every point
of a small closed ball around `x₀`. -/
theorem cc_local_time_functional [FiniteDimensional ℝ V] {x₀ : V} (hx₀ : x₀ ∈ S.M) :
    ∃ r > 0, ∀ y ∈ closedBall x₀ r, ∀ v ∈ S.CC y, v ≠ 0 →
      0 < (-((S.g x₀).flip (S.T x₀))) v := by
  have hT := S.T_timelike x₀ hx₀
  obtain ⟨ε, hε, c, hc, hco⟩ := S.cc_halfspace_strict hx₀ hT hT
  refine ⟨ε / 2, by positivity, fun y hy v hv hv0 => ?_⟩
  have h1 := hco y (closedBall_subset_ball (by linarith) hy) v hv
  have h2 : 0 < ‖v‖ := norm_pos_iff.2 hv0
  simp only [neg_apply, ContinuousLinearMap.flip_apply]
  nlinarith [mul_pos hc h2]

/-- **Coercivity over a compact set** (finite dimension). If a continuous linear functional `τ` is
strictly positive on the nonzero closed future cone at every point of a compact `K`, then for some
`δ > 0` and `c > 0`, `‖v‖ ≤ c · τ v` for every `v ∈ C y` and every `y` within `δ` of `K`. -/
theorem cc_coercive_K [FiniteDimensional ℝ V] {K : Set V} (hK : IsCompact K) (τ : V →L[ℝ] ℝ)
    (hτ : ∀ x ∈ K, ∀ v ∈ S.CC x, v ≠ 0 → 0 < τ v) :
    ∃ δ > 0, ∃ c > 0, ∀ y ∈ thickening δ K, ∀ v ∈ S.CC y, ‖v‖ ≤ c * τ v := by
  let h : V × V → ℝ := fun p => max (τ p.2) (max (S.g p.1 p.2 p.2) (S.g p.1 p.2 (S.T p.1)))
  have hc : Continuous h := (τ.continuous.comp continuous_snd).max
    ((S.cc_cont_gvw continuous_fst continuous_snd continuous_snd).max
      (S.cc_cont_gvw continuous_fst continuous_snd (S.cont_T.comp continuous_fst)))
  have hunit : ∀ v : V, v ≠ 0 → ‖v‖⁻¹ • v ∈ sphere (0:V) 1 := fun v hv => by
    rw [mem_sphere_zero_iff_norm]; exact norm_smul_inv_norm hv
  have hpos : ∀ p ∈ K ×ˢ sphere (0:V) 1, 0 < h p := by
    rintro ⟨x, u⟩ ⟨hx, hu⟩
    have hu0 : u ≠ 0 := by
      rintro rfl; simp at hu
    by_cases hC : u ∈ S.CC x
    · exact lt_max_of_lt_left (hτ x hx u hC hu0)
    · simp only [CC, mem_ofPred_eq, not_and_or, not_le] at hC
      rcases hC with h1 | h1
      · exact lt_max_of_lt_right (lt_max_of_lt_left h1)
      · exact lt_max_of_lt_right (lt_max_of_lt_right h1)
  have hZc : IsCompact (K ×ˢ sphere (0:V) 1) := hK.prod (isCompact_sphere 0 1)
  rcases (K ×ˢ sphere (0:V) 1).eq_empty_or_nonempty with hZ | hZ
  · refine ⟨1, one_pos, 1, one_pos, fun y hy v hv => ?_⟩
    by_cases hv0 : v = 0
    · simp [hv0]
    · exfalso
      obtain ⟨x, hx, -⟩ := mem_thickening_iff.1 hy
      have : (x, ‖v‖⁻¹ • v) ∈ K ×ˢ sphere (0:V) 1 := ⟨hx, hunit v hv0⟩
      rw [hZ] at this; exact this
  · obtain ⟨p₀, hp₀, hmin⟩ := hZc.exists_isMinOn hZ hc.continuousOn
    have hm : 0 < h p₀ := hpos p₀ hp₀
    have hO : IsOpen {p : V × V | h p₀ / 2 < h p} := isOpen_lt continuous_const hc
    have hsub : K ×ˢ sphere (0:V) 1 ⊆ {p | h p₀ / 2 < h p} := fun p hp => by
      have := isMinOn_iff.1 hmin p hp
      show h p₀ / 2 < h p
      linarith
    obtain ⟨δ, hδ, hδs⟩ := hZc.exists_thickening_subset_open hO hsub
    refine ⟨δ, hδ, 2 / h p₀, by positivity, fun y hy v hv => ?_⟩
    by_cases hv0 : v = 0
    · simp [hv0]
    obtain ⟨x, hx, hxy⟩ := mem_thickening_iff.1 hy
    have hn : 0 < ‖v‖ := norm_pos_iff.2 hv0
    have hmem : (y, ‖v‖⁻¹ • v) ∈ thickening δ (K ×ˢ sphere (0:V) 1) := by
      refine mem_thickening_iff.2 ⟨(x, ‖v‖⁻¹ • v), ⟨hx, hunit v hv0⟩, ?_⟩
      rw [Prod.dist_eq, dist_self, max_eq_left dist_nonneg]; exact hxy
    have h1 : h p₀ / 2 < h (y, ‖v‖⁻¹ • v) := hδs hmem
    have hCu := S.cc_cone_smul (inv_nonneg.2 hn.le) hv
    have h2 : h p₀ / 2 < τ (‖v‖⁻¹ • v) := by
      rcases lt_max_iff.1 h1 with h3 | h3
      · exact h3
      · rcases lt_max_iff.1 h3 with h4 | h4
        · have := hCu.1; simp only at h4; linarith
        · have := hCu.2; simp only at h4; linarith
    rw [map_smul, smul_eq_mul] at h2
    have h3 : h p₀ / 2 * ‖v‖ < τ v := by
      have := mul_lt_mul_of_pos_left h2 hn
      rwa [← mul_assoc, mul_inv_cancel₀ hn.ne', one_mul, mul_comm] at this
    rw [div_mul_eq_mul_div, le_div_iff₀ hm]
    nlinarith

/-- The closed convex set `{u | ‖u‖ ≤ c · τ u}` contains a cone hull as soon as it contains the
cones generating it. -/
lemma cc_hull_coercive {c : ℝ} (τ : V →L[ℝ] ℝ) {ε : ℝ} {A : Set V}
    (h : ∀ y ∈ thickening ε A, ∀ v ∈ S.CC y, ‖v‖ ≤ c * τ v) {w : V}
    (hw : w ∈ S.coneHull ε A) : ‖w‖ ≤ c * τ w := by
  have hconv : Convex ℝ {u : V | ‖u‖ ≤ c * τ u} := by
    intro u hu w hw a b ha hb _
    simp only [mem_ofPred_eq] at hu hw ⊢
    calc ‖a • u + b • w‖ ≤ ‖a • u‖ + ‖b • w‖ := norm_add_le _ _
      _ = a * ‖u‖ + b * ‖w‖ := by
          rw [norm_smul, norm_smul, Real.norm_of_nonneg ha, Real.norm_of_nonneg hb]
      _ ≤ a * (c * τ u) + b * (c * τ w) := by gcongr
      _ = c * τ (a • u + b • w) := by simp only [map_add, map_smul, smul_eq_mul]; ring
  have hcl : IsClosed {u : V | ‖u‖ ≤ c * τ u} :=
    isClosed_le continuous_norm (continuous_const.mul τ.continuous)
  exact closure_minimal (convexHull_min (iUnion₂_subset fun y hy v hv => h y hy.1 v hv) hconv)
    hcl hw

/-- **Chord bound.** If `‖v‖ ≤ c · τ v` on the cones over the `δ`-neighbourhood of `K`, then along
a curve with the cone condition and image in `K`, `‖γ t − γ s‖ ≤ c · (τ(γ t) − τ(γ s))` for
`0 ≤ s ≤ t ≤ 1`. -/
theorem cc_chord_bound {τ : V →L[ℝ] ℝ} {K : Set V} {δ c : ℝ} (hδ : 0 < δ)
    (hco : ∀ y ∈ thickening δ K, ∀ v ∈ S.CC y, ‖v‖ ≤ c * τ v) {γ : ℝ → V} (hγ : S.ConeCond γ)
    (hK : MapsTo γ (Icc 0 1) K) {s t : ℝ} (hs : 0 ≤ s) (hst : s ≤ t) (ht : t ≤ 1) :
    ‖γ t - γ s‖ ≤ c * (τ (γ t) - τ (γ s)) := by
  rcases hst.lt_or_eq with hlt | heq
  · have hq := hγ s t hs hlt ht δ hδ
    have hA : thickening δ (γ '' Icc s t) ⊆ thickening δ K := thickening_subset_of_subset δ
      (by rintro _ ⟨r, hr, rfl⟩; exact hK ⟨by linarith [hr.1], by linarith [hr.2]⟩)
    have h1 := S.cc_hull_coercive τ (fun y hy v hv => hco y (hA hy) v hv) hq
    have hts : 0 < t - s := sub_pos.2 hlt
    rw [norm_smul, map_smul, map_sub, smul_eq_mul,
      Real.norm_of_nonneg (inv_nonneg.2 hts.le)] at h1
    have h2 := mul_le_mul_of_nonneg_left h1 hts.le
    have e1 : (t - s) * ((t - s)⁻¹ * ‖γ t - γ s‖) = ‖γ t - γ s‖ := by field_simp
    have e2 : (t - s) * (c * ((t - s)⁻¹ * (τ (γ t) - τ (γ s)))) =
        c * (τ (γ t) - τ (γ s)) := by field_simp
    linarith
  · subst heq; simp

/-- **Monotonicity of the time functional** along the curve. -/
theorem cc_tau_mono {τ : V →L[ℝ] ℝ} {K : Set V} {δ c : ℝ} (hδ : 0 < δ) (hc : 0 < c)
    (hco : ∀ y ∈ thickening δ K, ∀ v ∈ S.CC y, ‖v‖ ≤ c * τ v) {γ : ℝ → V} (hγ : S.ConeCond γ)
    (hK : MapsTo γ (Icc 0 1) K) {s t : ℝ} (hs : 0 ≤ s) (hst : s ≤ t) (ht : t ≤ 1) :
    τ (γ s) ≤ τ (γ t) := by
  have := S.cc_chord_bound hδ hco hγ hK hs hst ht
  have h0 := norm_nonneg (γ t - γ s)
  by_contra hlt
  push Not at hlt
  nlinarith

/-- Two-sided form of the chord bound. -/
lemma cc_chord_bound_abs {τ : V →L[ℝ] ℝ} {K : Set V} {δ c : ℝ} (hδ : 0 < δ) (hc : 0 ≤ c)
    (hco : ∀ y ∈ thickening δ K, ∀ v ∈ S.CC y, ‖v‖ ≤ c * τ v) {γ : ℝ → V} (hγ : S.ConeCond γ)
    (hK : MapsTo γ (Icc 0 1) K) {s t : ℝ} (hs : s ∈ Icc (0:ℝ) 1) (ht : t ∈ Icc (0:ℝ) 1) :
    ‖γ t - γ s‖ ≤ c * |τ (γ t) - τ (γ s)| := by
  rcases le_total s t with h | h
  · have := S.cc_chord_bound hδ hco hγ hK hs.1 h ht.2
    exact this.trans (mul_le_mul_of_nonneg_left (le_abs_self _) hc)
  · have := S.cc_chord_bound hδ hco hγ hK ht.1 h hs.2
    rw [← norm_neg, neg_sub, abs_sub_comm]
    exact this.trans (mul_le_mul_of_nonneg_left (le_abs_self _) hc)

/-- Cone hulls are closed under multiplication by positive scalars. -/
lemma cc_coneHull_smul {ε a : ℝ} (ha : 0 < a) {A : Set V} {w : V} (hw : w ∈ S.coneHull ε A) :
    a • w ∈ S.coneHull ε A := by
  have h1 : a • w ∈ a • S.coneHull ε A := smul_mem_smul_set hw
  refine (smul_closure_subset a _).trans (closure_mono ?_) h1
  rw [← convexHull_smul]
  refine convexHull_mono ?_
  rintro _ ⟨u, hu, rfl⟩
  obtain ⟨x, hx, hux⟩ := mem_iUnion₂.1 hu
  exact mem_iUnion₂.2 ⟨x, hx, S.cc_cone_smul ha.le hux⟩

lemma cc_coneHull_mono_set {ε : ℝ} {A B : Set V} (h : A ⊆ B) :
    S.coneHull ε A ⊆ S.coneHull ε B :=
  closure_mono (convexHull_mono
    (biUnion_subset_biUnion_left (inter_subset_inter_left _ (thickening_subset_of_subset ε h))))

/-! ### Part ①: the reparametrisation by the time functional -/

/-- **Reparametrisation by a time functional.** Under the coercivity bound on the `δ`-neighbourhood
of `K`, every Lipschitz causal curve with image in `K` has the same image and the same endpoints as
a Lipschitz causal curve that is `c · (τ(γ 1) − τ(γ 0))`-Lipschitz. The new curve is `γ ∘ σ⁻¹`
with `σ = τ ∘ γ` rescaled to `[0,1]`. On intervals where `σ` is constant, `γ` is constant by the
chord bound, so the choice of preimage does not matter. -/
theorem cc_reparam {τ : V →L[ℝ] ℝ} {K : Set V} {δ c : ℝ} (hδ : 0 < δ) (hc : 0 < c)
    (hco : ∀ y ∈ thickening δ K, ∀ v ∈ S.CC y, ‖v‖ ≤ c * τ v) {γ : ℝ → V} (hγ : S.LipCausal γ)
    (hK : MapsTo γ (Icc 0 1) K) :
    ∃ γ' : ℝ → V, S.LipCausal γ' ∧
      LipschitzOnWith (Real.toNNReal (c * (τ (γ 1) - τ (γ 0)))) γ' (Icc 0 1) ∧
      γ' '' Icc 0 1 = γ '' Icc 0 1 ∧ γ' 0 = γ 0 ∧ γ' 1 = γ 1 := by
  obtain ⟨⟨L, hL⟩, hM, hcc⟩ := hγ
  set σ : ℝ → ℝ := fun t => τ (γ t) with hσ
  have hσc : ContinuousOn σ (Icc 0 1) := τ.continuous.comp_continuousOn hL.continuousOn
  have hmono : ∀ s t, 0 ≤ s → s ≤ t → t ≤ 1 → σ s ≤ σ t := fun s t hs hst ht =>
    S.cc_tau_mono hδ hc hco hcc hK hs hst ht
  have hkey : ∀ s ∈ Icc (0:ℝ) 1, ∀ t ∈ Icc (0:ℝ) 1, ‖γ t - γ s‖ ≤ c * |σ t - σ s| :=
    fun s hs t ht => S.cc_chord_bound_abs hδ hc.le hco hcc hK hs ht
  have heq : ∀ s ∈ Icc (0:ℝ) 1, ∀ t ∈ Icc (0:ℝ) 1, σ s = σ t → γ s = γ t := by
    intro s hs t ht h
    have := hkey s hs t ht
    rw [h, sub_self, abs_zero, mul_zero] at this
    exact (sub_eq_zero.1 (norm_le_zero_iff.1 this)).symm
  set a := σ 0
  set Δ := σ 1 - σ 0 with hΔ
  have hΔ0 : 0 ≤ Δ := sub_nonneg.2 (hmono 0 1 le_rfl zero_le_one le_rfl)
  let cl : ℝ → ℝ := fun u => max 0 (min u 1)
  have hcl0 : ∀ u, 0 ≤ cl u := fun u => le_max_left _ _
  have hcl1 : ∀ u, cl u ≤ 1 := fun u => max_le zero_le_one (min_le_right _ _)
  have hclI : ∀ u ∈ Icc (0:ℝ) 1, cl u = u := fun u hu => by
    simp only [cl, min_eq_left hu.2, max_eq_right hu.1]
  let lam : ℝ → ℝ := fun u => a + cl u * Δ
  have hlamc : Continuous lam := continuous_const.add
    ((continuous_const.max (continuous_id.min continuous_const)).mul continuous_const)
  have hIVT : ∀ u, ∃ t ∈ Icc (0:ℝ) 1, σ t = lam u := by
    intro u
    have hmem : lam u ∈ Icc (σ 0) (σ 1) := ⟨by
      show σ 0 ≤ a + cl u * Δ; nlinarith [hcl0 u], by
      show a + cl u * Δ ≤ σ 1; nlinarith [hcl1 u]⟩
    obtain ⟨t, ht, hteq⟩ := intermediate_value_Icc zero_le_one hσc hmem
    exact ⟨t, ht, hteq⟩
  choose Tm hTmI hTm using hIVT
  let γ' : ℝ → V := fun u => γ (Tm u)
  -- the Lipschitz estimate
  have hlip : ∀ u ∈ Icc (0:ℝ) 1, ∀ u' ∈ Icc (0:ℝ) 1,
      dist (γ' u) (γ' u') ≤ c * Δ * dist u u' := by
    intro u hu u' hu'
    have := hkey (Tm u') (hTmI u') (Tm u) (hTmI u)
    rw [hTm, hTm] at this
    have e : lam u - lam u' = (u - u') * Δ := by
      simp only [lam, hclI u hu, hclI u' hu']; ring
    rw [e, abs_mul, abs_of_nonneg hΔ0] at this
    rw [dist_eq_norm, Real.dist_eq]
    calc ‖γ' u - γ' u'‖ = ‖γ (Tm u) - γ (Tm u')‖ := rfl
      _ ≤ c * (|u - u'| * Δ) := this
      _ = c * Δ * |u - u'| := by ring
  -- points of the arc of `γ` over `[Tm u, Tm u']` are on the arc of `γ'` over `[u, u']`
  have harc : ∀ u ∈ Icc (0:ℝ) 1, ∀ u' ∈ Icc (0:ℝ) 1, u ≤ u' →
      γ '' Icc (Tm u) (Tm u') ⊆ γ' '' Icc u u' := by
    rintro u hu u' hu' huu' _ ⟨r, hr, rfl⟩
    have hrI : r ∈ Icc (0:ℝ) 1 := ⟨(hTmI u).1.trans hr.1, hr.2.trans (hTmI u').2⟩
    have hσr : σ r ∈ Icc (lam u) (lam u') := by
      rw [← hTm u, ← hTm u']
      exact ⟨hmono _ _ (hTmI u).1 hr.1 hrI.2, hmono _ _ hrI.1 hr.2 (hTmI u').2⟩
    obtain ⟨w, hw, hweq⟩ := intermediate_value_Icc huu' hlamc.continuousOn hσr
    have hwI : w ∈ Icc (0:ℝ) 1 := ⟨hu.1.trans hw.1, hw.2.trans hu'.2⟩
    refine ⟨w, hw, heq _ (hTmI w) _ hrI ?_⟩
    rw [hTm, hweq]
  refine ⟨γ', ⟨⟨_, LipschitzOnWith.of_dist_le' hlip⟩, ?_, ?_⟩, ?_, ?_, ?_, ?_⟩
  · intro u _; exact hM (hTmI u)
  · -- the cone condition
    intro u u' hu hlt hu' ε hε
    have huI : u ∈ Icc (0:ℝ) 1 := ⟨hu, by linarith⟩
    have hu'I : u' ∈ Icc (0:ℝ) 1 := ⟨by linarith, hu'⟩
    by_cases hT : Tm u < Tm u'
    · have hq := hcc (Tm u) (Tm u') (hTmI u).1 hT (hTmI u').2 ε hε
      have hpos : 0 < (u' - u)⁻¹ * (Tm u' - Tm u) :=
        mul_pos (inv_pos.2 (sub_pos.2 hlt)) (sub_pos.2 hT)
      have h1 := S.cc_coneHull_smul hpos hq
      have e : ((u' - u)⁻¹ * (Tm u' - Tm u)) • ((Tm u' - Tm u)⁻¹ • (γ (Tm u') - γ (Tm u))) =
          (u' - u)⁻¹ • (γ' u' - γ' u) := by
        rw [smul_smul, mul_assoc, mul_inv_cancel₀ (sub_pos.2 hT).ne', mul_one]
      rw [e] at h1
      exact S.cc_coneHull_mono_set (harc u huI u' hu'I hlt.le) h1
    · push Not at hT
      have h1 : σ (Tm u') ≤ σ (Tm u) := hmono _ _ (hTmI u').1 hT (hTmI u).2
      rw [hTm, hTm] at h1
      have h2 : lam u ≤ lam u' := by
        simp only [lam, hclI u huI, hclI u' hu'I]; nlinarith
      have h3 : γ' u' = γ' u := heq _ (hTmI u') _ (hTmI u) (by rw [hTm, hTm]; linarith)
      rw [h3, sub_self, smul_zero]
      refine S.cc_cone_subset_coneHull (x := γ' u) ?_ (hM (hTmI u)) (S.cc_zero_mem_CC _)
      exact self_subset_thickening hε _ ⟨u, ⟨le_rfl, hlt.le⟩, rfl⟩
  · exact LipschitzOnWith.of_dist_le' hlip
  · apply Subset.antisymm
    · rintro _ ⟨u, -, rfl⟩; exact ⟨Tm u, hTmI u, rfl⟩
    · rintro _ ⟨r, hr, rfl⟩
      have hσr : σ r ∈ Icc (lam 0) (lam 1) := by
        rw [← hTm 0, ← hTm 1]
        refine ⟨?_, ?_⟩
        · rw [hTm]; simp only [lam, hclI 0 ⟨le_rfl, zero_le_one⟩, zero_mul, add_zero]
          exact hmono 0 r le_rfl hr.1 hr.2
        · rw [hTm]; simp only [lam, hclI 1 ⟨zero_le_one, le_rfl⟩, one_mul, a, Δ]
          rw [add_sub_cancel]; exact hmono r 1 hr.1 hr.2 le_rfl
      obtain ⟨w, hw, hweq⟩ := intermediate_value_Icc zero_le_one hlamc.continuousOn hσr
      exact ⟨w, hw, heq _ (hTmI w) _ hr (by rw [hTm, hweq])⟩
  · show γ (Tm 0) = γ 0
    refine heq _ (hTmI 0) _ ⟨le_rfl, zero_le_one⟩ ?_
    rw [hTm]; simp only [lam, hclI 0 ⟨le_rfl, zero_le_one⟩, zero_mul, add_zero, a]
  · show γ (Tm 1) = γ 1
    refine heq _ (hTmI 1) _ ⟨zero_le_one, le_rfl⟩ ?_
    rw [hTm]; simp only [lam, hclI 1 ⟨zero_le_one, le_rfl⟩, one_mul, a, Δ]; ring

/-- **Uniform Lipschitz reparametrisation** (finite dimension). Let `K` be compact and let `τ` be
strictly positive on the nonzero closed future cones over `K`. There is `c_K > 0` such that for
every `D ≥ sup_K τ − inf_K τ` (any `D` bounding the oscillation of `τ` on `K`), every Lipschitz
causal curve with image in `K` has the same image and the same endpoints as a Lipschitz causal
curve that is `L_K = c_K · D`-Lipschitz on `[0,1]`. -/
theorem cc_uniform_reparam [FiniteDimensional ℝ V] {K : Set V} (hK : IsCompact K)
    (τ : V →L[ℝ] ℝ) (hτ : ∀ x ∈ K, ∀ v ∈ S.CC x, v ≠ 0 → 0 < τ v) :
    ∃ c > 0, ∀ D : ℝ, (∀ x ∈ K, ∀ y ∈ K, τ x - τ y ≤ D) →
      ∀ γ : ℝ → V, S.LipCausal γ → MapsTo γ (Icc 0 1) K →
        ∃ γ' : ℝ → V, S.LipCausal γ' ∧ LipschitzOnWith (Real.toNNReal (c * D)) γ' (Icc 0 1) ∧
          γ' '' Icc 0 1 = γ '' Icc 0 1 ∧ γ' 0 = γ 0 ∧ γ' 1 = γ 1 := by
  obtain ⟨δ, hδ, c, hc, hco⟩ := S.cc_coercive_K hK τ hτ
  refine ⟨c, hc, fun D hD γ hγ hγK => ?_⟩
  obtain ⟨γ', h1, h2, h3, h4, h5⟩ := S.cc_reparam hδ hc hco hγ hγK
  refine ⟨γ', h1, h2.weaken ?_, h3, h4, h5⟩
  exact Real.toNNReal_le_toNNReal (mul_le_mul_of_nonneg_left
    (hD _ (hγK ⟨zero_le_one, le_rfl⟩) _ (hγK ⟨le_rfl, zero_le_one⟩)) hc.le)

/-- The oscillation of a continuous linear functional on a compact set is bounded. -/
lemma cc_osc_bound {K : Set V} (hK : IsCompact K) (τ : V →L[ℝ] ℝ) :
    ∃ D : ℝ, ∀ x ∈ K, ∀ y ∈ K, τ x - τ y ≤ D := by
  obtain ⟨C, hC⟩ := hK.exists_bound_of_continuousOn τ.continuous.continuousOn
  refine ⟨2 * C, fun x hx y hy => ?_⟩
  have h1 := hC x hx
  have h2 := hC y hy
  rw [Real.norm_eq_abs] at h1 h2
  linarith [le_abs_self (τ x), neg_abs_le (τ y)]

/-- **Uniform Lipschitz pieces.** Under the same hypotheses there is one `L_K` such that every
Lipschitz causal piece `x → y` with image in `K` can be replaced by an `L_K`-Lipschitz one with the
same image and endpoints. -/
theorem cc_uniform_pieces [FiniteDimensional ℝ V] {K : Set V} (hK : IsCompact K)
    (τ : V →L[ℝ] ℝ) (hτ : ∀ x ∈ K, ∀ v ∈ S.CC x, v ≠ 0 → 0 < τ v) :
    ∃ L : NNReal, ∀ x y : V, ∀ γ : ℝ → V, S.LipCausal γ → MapsTo γ (Icc 0 1) K → γ 0 = x →
      γ 1 = y → ∃ γ' : ℝ → V, S.LipCausal γ' ∧ LipschitzOnWith L γ' (Icc 0 1) ∧
        MapsTo γ' (Icc 0 1) K ∧ γ' 0 = x ∧ γ' 1 = y := by
  obtain ⟨c, hc, hrep⟩ := S.cc_uniform_reparam hK τ hτ
  obtain ⟨D, hD⟩ := cc_osc_bound hK τ
  refine ⟨Real.toNNReal (c * D), fun x y γ hγ hγK h0 h1 => ?_⟩
  obtain ⟨γ', g1, g2, g3, g4, g5⟩ := hrep D hD γ hγ hγK
  refine ⟨γ', g1, g2, ?_, g4.trans h0, g5.trans h1⟩
  intro u hu
  have : γ' u ∈ γ '' Icc 0 1 := g3 ▸ mem_image_of_mem γ' hu
  obtain ⟨r, hr, hre⟩ := this
  rw [← hre]; exact hγK hr

/-- A Lipschitz causal piece from `x` to `y` with image in `K`. -/
def LStepIn (K : Set V) (x y : V) : Prop :=
  ∃ γ : ℝ → V, S.LipCausal γ ∧ MapsTo γ (Icc 0 1) K ∧ γ 0 = x ∧ γ 1 = y

/-- **Closedness of the causal relation on `K`, sequence form** (finite dimension). If `pₙ → p`,
`qₙ → q` and each `pₙ` is joined to `qₙ` by a Lipschitz causal piece with image in the compact
`K ⊆ M`, then so is `p` to `q`. Hypothesis: `τ` is strictly positive on the nonzero closed future
cones over `K`. -/
theorem cc_lstepIn_of_limit [FiniteDimensional ℝ V] {K : Set V} (hK : IsCompact K)
    (hKM : K ⊆ S.M) (τ : V →L[ℝ] ℝ) (hτ : ∀ x ∈ K, ∀ v ∈ S.CC x, v ≠ 0 → 0 < τ v)
    {P Q : ℕ → V} {p q : V} (hP : Tendsto P atTop (𝓝 p)) (hQ : Tendsto Q atTop (𝓝 q))
    (hstep : ∀ n, S.LStepIn K (P n) (Q n)) : S.LStepIn K p q := by
  obtain ⟨L, hL⟩ := S.cc_uniform_pieces hK τ hτ
  have h : ∀ n, ∃ γ' : ℝ → V, S.LipCausal γ' ∧ LipschitzOnWith L γ' (Icc 0 1) ∧
      MapsTo γ' (Icc 0 1) K ∧ γ' 0 = P n ∧ γ' 1 = Q n := fun n => by
    obtain ⟨γ, h1, h2, h3, h4⟩ := hstep n
    exact hL _ _ γ h1 h2 h3 h4
  choose F hF hFL hFK hF0 hF1 using h
  exact S.cc_lstep_of_limit hK hKM hFL hFK (fun n => (hF n).2.2) hF0 hF1 hP hQ

/-- **Closedness of the causal relation on `K`** (finite dimension): the set of pairs `(x, y)`
joined by a Lipschitz causal piece inside the compact `K ⊆ M` is closed in `V × V`. -/
theorem cc_isClosed_lstepIn [FiniteDimensional ℝ V] {K : Set V} (hK : IsCompact K)
    (hKM : K ⊆ S.M) (τ : V →L[ℝ] ℝ) (hτ : ∀ x ∈ K, ∀ v ∈ S.CC x, v ≠ 0 → 0 < τ v) :
    IsClosed {pq : V × V | S.LStepIn K pq.1 pq.2} := by
  refine isClosed_of_closure_subset fun pq hpq => ?_
  obtain ⟨u, hu, hlim⟩ := mem_closure_iff_seq_limit.1 hpq
  exact S.cc_lstepIn_of_limit hK hKM τ hτ ((continuous_fst.tendsto _).comp hlim)
    ((continuous_snd.tendsto _).comp hlim) hu

/-- **Closedness near any point, with no extra hypothesis** (finite dimension). Every `x₀ ∈ M` has
a closed ball `B` around it such that, for every compact `K ⊆ B ∩ M`, the relation "joined by a
Lipschitz causal piece inside `K`" is closed. The time functional is `−g_{x₀}(·, T x₀)`. -/
theorem cc_isClosed_lstepIn_local [FiniteDimensional ℝ V] {x₀ : V} (hx₀ : x₀ ∈ S.M) :
    ∃ r > 0, ∀ K : Set V, IsCompact K → K ⊆ closedBall x₀ r → K ⊆ S.M →
      IsClosed {pq : V × V | S.LStepIn K pq.1 pq.2} := by
  obtain ⟨r, hr, hτ⟩ := S.cc_local_time_functional hx₀
  exact ⟨r, hr, fun K hK hKB hKM => S.cc_isClosed_lstepIn hK hKM _
    fun x hx v hv hv0 => hτ x (hKB hx) v hv hv0⟩

/-! ### Part ②: the chronological relation (copied from `probes/CausalStructure.lean`) -/

/-- Future-directed timelike vector at `x` (campaign 60). -/
def FutTimelike (x v : V) : Prop := S.g x v v < 0 ∧ S.g x v (S.T x) < 0

/-- One `C¹` future-timelike piece from `x` to `y` (campaign 60). -/
def TStep (x y : V) : Prop :=
  ∃ γ : ℝ → V, ContDiff ℝ 1 γ ∧ γ 0 = x ∧ γ 1 = y ∧
    ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ S.M ∧ S.FutTimelike (γ t) (deriv γ t)

/-- Campaign 60's chronological relation `x ≪ y`: a finite chain of `C¹` timelike pieces. -/
def Chr (x y : V) : Prop := Relation.TransGen S.TStep x y

/-- Chronological past `I⁻(p)`. -/
def Ipast (p : V) : Set V := {q | S.Chr q p}

lemma cc_isOpen_timelikePairs :
    IsOpen {pv : V × V | pv.1 ∈ S.M ∧ S.FutTimelike pv.1 pv.2} := by
  refine (S.isOpen_M.preimage continuous_fst).inter (IsOpen.inter ?_ ?_)
  · exact isOpen_lt (S.cc_cont_gvw continuous_fst continuous_snd continuous_snd) continuous_const
  · exact isOpen_lt (S.cc_cont_gvw continuous_fst continuous_snd
      (S.cont_T.comp continuous_fst)) continuous_const

lemma cc_tube {P Q : V → ℝ → V} (hP : Continuous fun z : V × ℝ => P z.1 z.2)
    (hQ : Continuous fun z : V × ℝ => Q z.1 z.2)
    (h0 : ∀ t ∈ Icc (0:ℝ) 1, P 0 t ∈ S.M ∧ S.FutTimelike (P 0 t) (Q 0 t)) :
    ∀ᶠ w in 𝓝 (0:V), ∀ t ∈ Icc (0:ℝ) 1, P w t ∈ S.M ∧ S.FutTimelike (P w t) (Q w t) := by
  refine isCompact_Icc.eventually_forall_of_forall_eventually fun t ht => ?_
  have hO := S.cc_isOpen_timelikePairs.preimage (hP.prodMk hQ)
  exact hO.mem_nhds (h0 t ht)

lemma cc_hasDerivAt_of_contDiff {γ : ℝ → V} (hγ : ContDiff ℝ 1 γ) (t : ℝ) :
    HasDerivAt γ (deriv γ t) t :=
  ((hγ.differentiable one_ne_zero) t).hasDerivAt

lemma cc_tstep_start_eventually {p y : V} (h : S.TStep p y) : ∀ᶠ p' in 𝓝 p, S.TStep p' y := by
  obtain ⟨γ, hγ, h0, h1, hγt⟩ := h
  have hdc : Continuous (deriv γ) := hγ.continuous_deriv le_rfl
  have hT := S.cc_tube (P := fun w t => γ t + (1 - t) • w) (Q := fun w t => deriv γ t - w)
    ((hγ.continuous.comp continuous_snd).add
      ((continuous_const.sub continuous_snd).smul continuous_fst))
    ((hdc.comp continuous_snd).sub continuous_fst) (by simpa using hγt)
  have hlim : Tendsto (fun p' => p' - p) (𝓝 p) (𝓝 0) := tendsto_sub_nhds_zero_iff.2 tendsto_id
  filter_upwards [hlim.eventually hT] with p' hp'
  refine ⟨fun t => γ t + (1 - t) • (p' - p),
    hγ.add ((contDiff_const.sub contDiff_id).smul contDiff_const), by simp [h0],
    by simp [h1], fun t ht => ?_⟩
  have hd : deriv (fun t => γ t + (1 - t) • (p' - p)) t = deriv γ t - (p' - p) := by
    have h : HasDerivAt (fun t => γ t + (1 - t) • (p' - p))
        (deriv γ t + ((0:ℝ) - 1) • (p' - p)) t :=
      (cc_hasDerivAt_of_contDiff hγ t).add
        (((hasDerivAt_const t (1:ℝ)).sub (hasDerivAt_id' t)).smul_const (p' - p))
    rw [h.deriv, zero_sub, neg_one_smul, ← sub_eq_add_neg]
  rw [hd]; exact hp' t ht

theorem cc_isOpen_Ipast (p : V) : IsOpen (S.Ipast p) := by
  refine isOpen_iff_mem_nhds.2 fun q hq => ?_
  obtain ⟨y, hqy, hyp⟩ := Relation.TransGen.head'_iff.1 hq
  filter_upwards [S.cc_tstep_start_eventually hqy] with q' hq'
  exact Relation.TransGen.head' hq' hyp

lemma cc_futTimelike_smul {x u : V} {c : ℝ} (hc : 0 < c) (h : S.FutTimelike x u) :
    S.FutTimelike x (c • u) := by
  obtain ⟨h1, h2⟩ := h
  refine ⟨?_, ?_⟩
  · simp only [map_smul, FunLike.coe_smul, Pi.smul_apply, smul_eq_mul]
    nlinarith [mul_pos hc hc]
  · simp only [map_smul, FunLike.coe_smul, Pi.smul_apply, smul_eq_mul]
    nlinarith

/-! ### Part ②: straight timelike segments and polygons -/

/-- A straight segment whose direction is future timelike at every point is a timelike step. -/
lemma cc_segment_tstep {a b : V}
    (h : ∀ r ∈ Icc (0:ℝ) 1, a + r • (b - a) ∈ S.M ∧ S.FutTimelike (a + r • (b - a)) (b - a)) :
    S.TStep a b := by
  refine ⟨fun r => a + r • (b - a), contDiff_const.add (contDiff_id.smul contDiff_const),
    by simp, by simp, fun r hr => ?_⟩
  have hd : deriv (fun r : ℝ => a + r • (b - a)) r = b - a := by
    have : HasDerivAt (fun r : ℝ => a + r • (b - a)) ((1:ℝ) • (b - a)) r :=
      ((hasDerivAt_id r).smul_const (b - a)).const_add a
    rw [this.deriv, one_smul]
  rw [hd]; exact h r hr

/-- A polygon of timelike steps is a chronological chain. -/
lemma cc_chain {P : ℕ → V} {N : ℕ} (hN : 0 < N) (h : ∀ i < N, S.TStep (P i) (P (i + 1))) :
    S.Chr (P 0) (P N) := by
  induction N with
  | zero => omega
  | succ n ih =>
    rcases Nat.eq_zero_or_pos n with rfl | hn
    · exact Relation.TransGen.single (h 0 (by omega))
    · exact (ih hn fun i hi => h i (by omega)).tail (h n (by omega))

/-- Time orientation from a timelike reference vector: a causal `a` with `g_p(a,w) ≤ 0` for a
future timelike `w` is future-directed. -/
lemma cc_orient {p a w : V} (hp : p ∈ S.M) (hw : w ∈ S.CC p) (hww : S.g p w w < 0)
    (haa : S.g p a a ≤ 0) (haw : S.g p a w ≤ 0) : a ∈ S.CC p := by
  refine ⟨haa, ?_⟩
  by_contra h
  have h' : 0 < S.g p a (S.T p) := lt_of_not_ge h
  have hna : -a ∈ S.CC p := ⟨by simpa using haa, by simp; linarith⟩
  have hne : -a ≠ 0 := by
    intro h0; rw [neg_eq_zero] at h0; subst h0; simp at h'
  have := (S.cc_reverse_cs hp hna hw).2 hne hww
  simp at this; linarith

/-- Closed future causal plus a positive multiple of a future timelike vector is future
timelike. -/
lemma cc_timelike_add {p a v : V} (hp : p ∈ S.M) (ha : a ∈ S.CC p) (hv : v ∈ S.CC p)
    (hvv : S.g p v v < 0) {μ : ℝ} (hμ : 0 < μ) : S.FutTimelike p (a + μ • v) := by
  have h1 := (S.cc_reverse_cs hp ha hv).1
  have hTT := S.T_timelike p hp
  have hvT : S.g p v (S.T p) < 0 := by
    have hv0 : v ≠ 0 := by rintro rfl; simp at hvv
    exact (S.cc_reverse_cs hp hv ⟨hTT.le, hTT.le⟩).2 hv0 hTT
  have hva := S.symm p v a
  have haa := ha.1
  have haT := ha.2
  refine ⟨?_, ?_⟩
  · simp only [map_add, map_smul, FunLike.coe_add, Pi.add_apply, FunLike.coe_smul,
      Pi.smul_apply, smul_eq_mul]
    rw [hva]; nlinarith [mul_pos hμ hμ, mul_nonpos_of_nonneg_of_nonpos hμ.le h1]
  · simp only [map_add, map_smul, FunLike.coe_add, Pi.add_apply, FunLike.coe_smul,
      Pi.smul_apply, smul_eq_mul]
    nlinarith [mul_pos hμ (neg_pos.2 hvT)]

/-- The algebra of the tilt: if `u` pairs with the future timelike `v` at `p` by at most `−k`,
and `g_p(u,u) ≤ 2θk²`, then `u + θ a v` is closed future causal at `p` for any `a ≥ k ≥ 0`. -/
lemma cc_tilt_vec {p u v : V} {a θ k : ℝ} (hp : p ∈ S.M) (hvp : v ∈ S.CC p)
    (hvv : S.g p v v < 0) (hθ : 0 ≤ θ) (hk : 0 ≤ k) (hka : k ≤ a) (huv : S.g p u v ≤ -k)
    (huu : S.g p u u ≤ 2 * θ * k ^ 2) : u + (θ * a) • v ∈ S.CC p := by
  have hsym := S.symm p v u
  have hs : 0 ≤ θ * a := mul_nonneg hθ (hk.trans hka)
  have e1 : S.g p (u + (θ * a) • v) (u + (θ * a) • v) =
      S.g p u u + 2 * (θ * (a * S.g p u v)) + (θ * a) * (θ * a) * S.g p v v := by
    simp only [map_add, map_smul, FunLike.coe_add, Pi.add_apply, FunLike.coe_smul,
      Pi.smul_apply, smul_eq_mul]
    rw [hsym]; ring
  have e2 : S.g p (u + (θ * a) • v) v = S.g p u v + (θ * a) * S.g p v v := by
    simp only [map_add, map_smul, FunLike.coe_add, Pi.add_apply, FunLike.coe_smul,
      Pi.smul_apply, smul_eq_mul]
  have h1 : a * S.g p u v ≤ -(k * k) := by
    have h5 := mul_le_mul_of_nonneg_left huv (hk.trans hka)
    have h6 : a * (-k) ≤ k * (-k) := mul_le_mul_of_nonpos_right hka (by linarith)
    linarith
  have h2 : (θ * a) * (θ * a) * S.g p v v ≤ 0 :=
    mul_nonpos_of_nonneg_of_nonpos (mul_self_nonneg _) hvv.le
  have h3 : θ * (a * S.g p u v) ≤ θ * (-(k * k)) := mul_le_mul_of_nonneg_left h1 hθ
  have h4 : (θ * a) * S.g p v v ≤ 0 := mul_nonpos_of_nonneg_of_nonpos hs hvv.le
  have hk2 : θ * (-(k * k)) = -(θ * k ^ 2) := by ring
  refine S.cc_orient hp hvp hvv ?_ ?_
  · rw [e1]; linarith
  · rw [e2]; linarith

/-- **The tilt on chord quotients** (finite dimension, locally Lipschitz `g`). Near `x₀ ∈ M`, let
`v = T x₀`. If `w` lies in the cone hull over a set `A` all of whose `ε`-neighbours are close to
`p` (closer than `κ l /(B+1)`), and `‖w‖ ≤ B`, then `w + l v` is future timelike at `p`. The proof
applies the linear map `u ↦ u + θ τ₀(u) v` (with `τ₀ = −g_{x₀}(·, v)`), which sends the cones over
the neighbours into the closed cone at `p`; the preimage of that cone is closed and convex, so it
contains the whole hull. -/
lemma cc_tilt [FiniteDimensional ℝ V] (hL : LocallyLipschitz S.g) {x₀ : V} (hx₀ : x₀ ∈ S.M) :
    ∃ ρ > 0, ∃ κ > 0, ∀ B l : ℝ, 0 ≤ B → 0 < l → ∀ (p w : V) (A : Set V) (ε : ℝ),
      p ∈ ball x₀ ρ → (∀ y ∈ thickening ε A, y ∈ ball x₀ ρ ∧ dist p y ≤ κ * l / (B + 1)) →
      w ∈ S.coneHull ε A → ‖w‖ ≤ B → p ∈ S.M ∧ S.FutTimelike p (w + l • S.T x₀) := by
  set v := S.T x₀ with hv
  have hT := S.T_timelike x₀ hx₀
  obtain ⟨r₁, hr₁, c, hc, hco⟩ := S.cc_coercive hx₀ hT hT
  obtain ⟨K, N, hN, hK⟩ := hL x₀
  obtain ⟨r₂, hr₂, hr₂N⟩ := Metric.mem_nhds_iff.1 hN
  have hO : IsOpen {y | y ∈ S.M ∧ S.g y v v < 0 ∧ S.g y v (S.T y) < 0} :=
    S.isOpen_M.inter ((isOpen_lt (S.cc_cont_gvw continuous_id continuous_const continuous_const)
      continuous_const).inter
      (isOpen_lt (S.cc_cont_gvw continuous_id continuous_const S.cont_T) continuous_const))
  obtain ⟨r₃, hr₃, hr₃O⟩ := Metric.isOpen_iff.1 hO x₀ ⟨hx₀, hT, hT⟩
  have hK0 : (0:ℝ) ≤ K := K.2
  set Cφ : ℝ := ‖S.g x₀‖ * ‖v‖ + 1 with hCφdef
  have hCφ : 0 < Cφ := by positivity
  set r₄ : ℝ := c / (4 * (K + 1) * (‖v‖ + 1)) with hr₄
  have hr₄p : 0 < r₄ := by positivity
  set ρ := min (min r₁ r₂) (min r₃ r₄) with hρdef
  have hρ : 0 < ρ := lt_min (lt_min hr₁ hr₂) (lt_min hr₃ hr₄p)
  have hρ1 : ρ ≤ r₁ := (min_le_left _ _).trans (min_le_left _ _)
  have hρ2 : ρ ≤ r₂ := (min_le_left _ _).trans (min_le_right _ _)
  have hρ3 : ρ ≤ r₃ := (min_le_right _ _).trans (min_le_left _ _)
  have hρ4 : ρ ≤ r₄ := (min_le_right _ _).trans (min_le_right _ _)
  refine ⟨ρ, hρ, c ^ 2 / (4 * Cφ * (K + 1)), by positivity, ?_⟩
  intro B l hB hl p w A ε hp hA hw hwB
  have hball : ∀ y ∈ ball x₀ ρ, y ∈ closedBall x₀ r₁ ∧ y ∈ N ∧ y ∈ S.M ∧ S.g y v v < 0 ∧
      S.g y v (S.T y) < 0 := by
    intro y hy
    have h3 := hr₃O (ball_subset_ball hρ3 hy)
    exact ⟨ball_subset_closedBall (ball_subset_ball hρ1 hy), hr₂N (ball_subset_ball hρ2 hy),
      h3.1, h3.2.1, h3.2.2⟩
  have hgdiff : ∀ y ∈ ball x₀ ρ, ∀ q ∈ ball x₀ ρ, ‖S.g q - S.g y‖ ≤ K * dist q y :=
    fun y hy q hq => by
      have := hK.dist_le_mul q (hball q hq).2.1 y (hball y hy).2.1
      rwa [dist_eq_norm] at this
  have hdist2 : ∀ y ∈ ball x₀ ρ, ∀ q ∈ ball x₀ ρ, dist q y ≤ 2 * ρ := fun y hy q hq => by
    have := dist_triangle_right q y x₀
    rw [mem_ball] at hy hq; linarith
  have hKρ : (K:ℝ) * (2 * ρ) * ‖v‖ ≤ c / 2 := by
    have h1 : (K:ℝ) * (2 * ρ) * ‖v‖ ≤ (K + 1) * (2 * ρ) * (‖v‖ + 1) := by
      have := norm_nonneg v
      have : 0 ≤ ρ := hρ.le
      nlinarith [mul_nonneg hK0 hρ.le]
    have h2 : (K + 1) * (2 * ρ) * (‖v‖ + 1) ≤ (K + 1) * (2 * r₄) * (‖v‖ + 1) := by
      have := norm_nonneg v
      apply mul_le_mul_of_nonneg_right _ (by positivity)
      apply mul_le_mul_of_nonneg_left _ (by positivity)
      linarith
    have h3 : (K + 1) * (2 * r₄) * (‖v‖ + 1) = c / 2 := by
      rw [hr₄]; field_simp; ring
    linarith
  -- (E1) the cones over the ball pair negatively with `v`, uniformly
  have E1 : ∀ y ∈ ball x₀ ρ, ∀ q ∈ ball x₀ ρ, ∀ u ∈ S.CC y, S.g q u v ≤ -(c / 2 * ‖u‖) := by
    intro y hy q hq u hu
    have h1 := hco y (hball y hy).1 u hu
    have h3 : |S.g q u v - S.g y u v| ≤ ‖S.g q - S.g y‖ * ‖u‖ * ‖v‖ := by
      have := (S.g q - S.g y).le_opNorm₂ u v
      simpa [Real.norm_eq_abs] using this
    have h4 : ‖S.g q - S.g y‖ * ‖v‖ ≤ c / 2 :=
      (mul_le_mul_of_nonneg_right ((hgdiff y hy q hq).trans
        (mul_le_mul_of_nonneg_left (hdist2 y hy q hq) hK0)) (norm_nonneg v)).trans hKρ
    have h5 := (abs_le.1 h3).2
    nlinarith [mul_le_mul_of_nonneg_left h4 (norm_nonneg u)]
  -- (E2) the quadratic form moves by at most `K · dist`
  have E2 : ∀ y ∈ ball x₀ ρ, ∀ q ∈ ball x₀ ρ, ∀ u ∈ S.CC y,
      S.g q u u ≤ K * dist q y * (‖u‖ * ‖u‖) := by
    intro y hy q hq u hu
    have h3 : |S.g q u u - S.g y u u| ≤ ‖S.g q - S.g y‖ * ‖u‖ * ‖u‖ := by
      have := (S.g q - S.g y).le_opNorm₂ u u
      simpa [Real.norm_eq_abs] using this
    have h5 := (abs_le.1 h3).2
    have h6 : ‖S.g q - S.g y‖ * ‖u‖ * ‖u‖ ≤ K * dist q y * (‖u‖ * ‖u‖) := by
      rw [mul_assoc]; exact mul_le_mul_of_nonneg_right (hgdiff y hy q hq) (by positivity)
    have := hu.1
    linarith
  -- the linear time functional and its bounds
  set φ : V →L[ℝ] ℝ := -((S.g x₀).flip v) with hφdef
  have hφ : ∀ u, φ u = -S.g x₀ u v := fun u => by simp [hφdef]
  have hx₀b : x₀ ∈ ball x₀ ρ := mem_ball_self hρ
  have E3 : ∀ y ∈ ball x₀ ρ, ∀ u ∈ S.CC y, c / 2 * ‖u‖ ≤ φ u := fun y hy u hu => by
    rw [hφ]; linarith [E1 y hy x₀ hx₀b u hu]
  have hφB : φ w ≤ Cφ * B := by
    have h1 : |S.g x₀ w v| ≤ ‖S.g x₀‖ * ‖w‖ * ‖v‖ := by
      have := (S.g x₀).le_opNorm₂ w v
      simpa [Real.norm_eq_abs] using this
    rw [hφ]
    have h2 := neg_abs_le (S.g x₀ w v)
    have h3 : ‖S.g x₀‖ * ‖w‖ * ‖v‖ ≤ Cφ * B := by
      have : ‖S.g x₀‖ * ‖w‖ * ‖v‖ = (‖S.g x₀‖ * ‖v‖) * ‖w‖ := by ring
      rw [this]
      exact mul_le_mul (by linarith) hwB (norm_nonneg _) hCφ.le
    linarith
  -- the tilt map
  obtain ⟨θ, hθdef⟩ : ∃ θ : ℝ, θ = l / (2 * Cφ * (B + 1)) := ⟨_, rfl⟩
  have hθ : 0 < θ := by rw [hθdef]; positivity
  let Am : V → V := fun u => u + (θ * φ u) • v
  have hpb := hball p hp
  have hvp : v ∈ S.CC p := ⟨hpb.2.2.2.1.le, hpb.2.2.2.2.le⟩
  have hKd : ∀ y, dist p y ≤ c ^ 2 / (4 * Cφ * (K + 1)) * l / (B + 1) →
      (K:ℝ) * dist p y ≤ θ * c ^ 2 / 2 := by
    intro y hpy
    have h1 : (K:ℝ) * dist p y ≤ K * (c ^ 2 / (4 * Cφ * (K + 1)) * l / (B + 1)) :=
      mul_le_mul_of_nonneg_left hpy hK0
    have hB1 : 0 < B + 1 := by linarith
    have e : (K:ℝ) * (c ^ 2 / (4 * Cφ * (K + 1)) * l / (B + 1)) =
        (K / (K + 1)) * (θ * c ^ 2 / 2) := by
      rw [hθdef]; field_simp; ring
    have hKK : (K:ℝ) / (K + 1) ≤ 1 := by rw [div_le_one (by positivity)]; linarith
    have h2 : (K / (K + 1)) * (θ * c ^ 2 / 2) ≤ θ * c ^ 2 / 2 :=
      mul_le_of_le_one_left (by positivity) hKK
    linarith
  have hgen : ∀ y ∈ thickening ε A ∩ S.M, ∀ u ∈ S.CC y, Am u ∈ S.CC p := by
    rintro y ⟨hyA, -⟩ u hu
    obtain ⟨hyb, hpy⟩ := hA y hyA
    have e2 := E2 y hyb p hp u hu
    have hk := hKd y hpy
    have huu : S.g p u u ≤ 2 * θ * (c / 2 * ‖u‖) ^ 2 := by
      have h3 : (K:ℝ) * dist p y * (‖u‖ * ‖u‖) ≤ θ * c ^ 2 / 2 * (‖u‖ * ‖u‖) :=
        mul_le_mul_of_nonneg_right hk (by positivity)
      have e : θ * c ^ 2 / 2 * (‖u‖ * ‖u‖) = 2 * θ * (c / 2 * ‖u‖) ^ 2 := by ring
      linarith
    exact S.cc_tilt_vec hpb.2.2.1 hvp hpb.2.2.2.1 hθ.le (by positivity) (E3 y hyb u hu)
      (E1 y hyb p hp u hu) huu
  have hAmc : Continuous Am := continuous_id.add
    ((continuous_const.mul φ.continuous).smul continuous_const)
  have hconv : Convex ℝ (Am ⁻¹' S.CC p) := by
    intro u hu u' hu' a b ha hb hab
    have e : Am (a • u + b • u') = a • Am u + b • Am u' := by
      simp only [Am, map_add, map_smul, smul_eq_mul]
      module
    show Am (a • u + b • u') ∈ S.CC p
    rw [e]; exact S.cc_convex_cone hpb.2.2.1 hu hu' ha hb hab
  have hwE : Am w ∈ S.CC p :=
    closure_minimal (convexHull_min (iUnion₂_subset fun y hy u hu => hgen y hy u hu) hconv)
      ((S.cc_isClosed_CC p).preimage hAmc) hw
  have hμ : 0 < l - θ * φ w := by
    have h1 : θ * φ w ≤ θ * (Cφ * B) := mul_le_mul_of_nonneg_left hφB hθ.le
    have h2 : θ * (Cφ * B) < l := by
      rw [hθdef, div_mul_eq_mul_div, div_lt_iff₀ (by positivity)]
      nlinarith [mul_pos hl hCφ, mul_nonneg (mul_nonneg hl.le hCφ.le) hB]
    linarith
  have e : w + l • v = Am w + (l - θ * φ w) • v := by simp only [Am]; module
  refine ⟨hpb.2.2.1, ?_⟩
  rw [e]
  exact S.cc_timelike_add hpb.2.2.1 hwE hvp hpb.2.2.2.1 hμ

/-- One side of the polygon: from `α t₁ + μ₁ v` to `α t₂ + μ₂ v` with the tilt increment
`μ₂ − μ₁ = l (t₂ − t₁)`, under explicit smallness conditions, is a timelike step. -/
lemma cc_polygon_side [FiniteDimensional ℝ V] {x₀ v : V} {ρ κ : ℝ}
    (htilt : ∀ B l : ℝ, 0 ≤ B → 0 < l → ∀ (p w : V) (A : Set V) (ε : ℝ),
      p ∈ ball x₀ ρ → (∀ y ∈ thickening ε A, y ∈ ball x₀ ρ ∧ dist p y ≤ κ * l / (B + 1)) →
      w ∈ S.coneHull ε A → ‖w‖ ≤ B → p ∈ S.M ∧ S.FutTimelike p (w + l • v))
    {α : ℝ → V} {L : NNReal} (hLip : LipschitzOnWith L α (Icc 0 1)) (hcc : S.ConeCond α)
    {t₁ t₂ μ l ε : ℝ} (h0 : 0 ≤ t₁) (h12 : t₁ < t₂) (h2 : t₂ ≤ 1) (hl : 0 < l) (hε : 0 < ε)
    (hball : ∀ r ∈ Icc t₁ t₂, dist (α r) x₀ + |μ| * ‖v‖ + (t₂ - t₁) * (L + l * ‖v‖) + ε < ρ)
    (hclose : |μ| * ‖v‖ + (t₂ - t₁) * (2 * L + l * ‖v‖) + ε ≤ κ * l / (L + 1)) :
    S.TStep (α t₁ + μ • v) (α t₂ + (μ + l * (t₂ - t₁)) • v) := by
  have hΔ : 0 < t₂ - t₁ := sub_pos.2 h12
  set Δ := t₂ - t₁ with hΔdef
  have hI1 : t₁ ∈ Icc (0:ℝ) 1 := ⟨h0, by linarith⟩
  have hI2 : t₂ ∈ Icc (0:ℝ) 1 := ⟨by linarith, h2⟩
  set w := Δ⁻¹ • (α t₂ - α t₁) with hw
  have hwc : w ∈ S.coneHull ε (α '' Icc t₁ t₂) := hcc t₁ t₂ h0 h12 h2 ε hε
  have hLr : (0:ℝ) ≤ L := L.2
  have hαd : ∀ r ∈ Icc t₁ t₂, dist (α r) (α t₁) ≤ L * Δ := by
    intro r hr
    have hrI : r ∈ Icc (0:ℝ) 1 := ⟨by linarith [hr.1], by linarith [hr.2]⟩
    have := hLip.dist_le_mul r hrI t₁ hI1
    rw [Real.dist_eq, abs_of_nonneg (by linarith [hr.1])] at this
    exact this.trans (mul_le_mul_of_nonneg_left (by linarith [hr.2]) hLr)
  have hwB : ‖w‖ ≤ L := by
    have h := hαd t₂ ⟨h12.le, le_rfl⟩
    rw [dist_eq_norm] at h
    rw [hw, norm_smul, Real.norm_of_nonneg (inv_nonneg.2 hΔ.le)]
    calc Δ⁻¹ * ‖α t₂ - α t₁‖ ≤ Δ⁻¹ * (L * Δ) := mul_le_mul_of_nonneg_left h (by positivity)
      _ = L := by field_simp
  have hdiff : α t₂ + (μ + l * Δ) • v - (α t₁ + μ • v) = Δ • (w + l • v) := by
    rw [hw, smul_add, smul_smul, mul_inv_cancel₀ hΔ.ne', one_smul, smul_smul]
    module
  refine S.cc_segment_tstep fun r hr => ?_
  rw [hdiff]
  set p := α t₁ + μ • v + r • (Δ • (w + l • v)) with hp
  have hpd : dist p (α t₁) ≤ |μ| * ‖v‖ + Δ * (L + l * ‖v‖) := by
    rw [hp, dist_eq_norm, add_assoc, add_sub_cancel_left]
    calc ‖μ • v + r • (Δ • (w + l • v))‖ ≤ ‖μ • v‖ + ‖r • (Δ • (w + l • v))‖ := norm_add_le _ _
      _ ≤ |μ| * ‖v‖ + Δ * (L + l * ‖v‖) := by
        rw [norm_smul, norm_smul, norm_smul, Real.norm_eq_abs μ, Real.norm_of_nonneg hr.1,
          Real.norm_of_nonneg hΔ.le]
        have h1 : ‖w + l • v‖ ≤ L + l * ‖v‖ := by
          have := norm_add_le w (l • v)
          rw [norm_smul l v, Real.norm_of_nonneg hl.le] at this; linarith
        have h2 : r * (Δ * ‖w + l • v‖) ≤ 1 * (Δ * (L + l * ‖v‖)) :=
          mul_le_mul hr.2 (mul_le_mul_of_nonneg_left h1 hΔ.le) (by positivity) zero_le_one
        linarith
  have hpb : p ∈ ball x₀ ρ := by
    rw [mem_ball]
    have := hball t₁ ⟨le_rfl, h12.le⟩
    have := dist_triangle p (α t₁) x₀
    linarith
  have hA : ∀ y ∈ thickening ε (α '' Icc t₁ t₂), y ∈ ball x₀ ρ ∧
      dist p y ≤ κ * l / (L + 1) := by
    intro y hy
    obtain ⟨_, ⟨r', hr', rfl⟩, hyr⟩ := mem_thickening_iff.1 hy
    have h1 := hαd r' hr'
    have h2 := hball r' hr'
    refine ⟨?_, ?_⟩
    · rw [mem_ball]
      have := dist_triangle y (α r') x₀
      have : 0 ≤ |μ| * ‖v‖ + Δ * (L + l * ‖v‖) := by positivity
      linarith
    · have h3 := dist_triangle p (α t₁) y
      have h4 := dist_triangle (α t₁) (α r') y
      rw [dist_comm (α t₁) (α r')] at h4
      have h5 : dist (α r') y < ε := by rw [dist_comm]; exact hyr
      have : Δ * (2 * L + l * ‖v‖) = Δ * (L + l * ‖v‖) + L * Δ := by ring
      linarith
  have := htilt L l hLr hl p w (α '' Icc t₁ t₂) ε hpb hA hwc hwB
  exact ⟨this.1, S.cc_futTimelike_smul hΔ this.2⟩

/-- **Local push-up for Lipschitz causal curves** (finite dimension, locally Lipschitz `g`). Along a
Lipschitz causal curve `α`, for `t` slightly after `s` and every small `l > 0`, the point
`α t + l (t − s) T(α s)` is in the chronological future of `α s`. The witness is a polygon of
straight timelike segments through the tilted points `α tᵢ + l (tᵢ − s) T(α s)` of a fine
partition; each segment is timelike by `cc_tilt`. -/
lemma cc_local_pushup [FiniteDimensional ℝ V] (hL : LocallyLipschitz S.g) {α : ℝ → V}
    (hα : S.LipCausal α) {s : ℝ} (hs : s ∈ Icc (0:ℝ) 1) :
    ∃ h > 0, ∀ t ∈ Icc (0:ℝ) 1, s < t → t < s + h → ∀ l : ℝ, 0 < l → l < h →
      S.Chr (α s) (α t + (l * (t - s)) • S.T (α s)) := by
  obtain ⟨⟨L, hLip⟩, hαM, hcc⟩ := hα
  obtain ⟨ρ, hρ, κ, hκ, htilt⟩ := S.cc_tilt hL (hαM hs)
  obtain ⟨v, hv⟩ : ∃ v, v = S.T (α s) := ⟨_, rfl⟩
  rw [← hv] at htilt ⊢
  have hLr : (0:ℝ) ≤ L := L.2
  have hnv := norm_nonneg v
  obtain ⟨h, hhdef⟩ : ∃ h : ℝ, h = min (min 1 (ρ / (4 * (L + ‖v‖ + 1))))
      (κ / (2 * (L + 1) * (‖v‖ + 1))) := ⟨_, rfl⟩
  have hh1 : h ≤ 1 := hhdef ▸ (min_le_left _ _).trans (min_le_left _ _)
  have hhρ : h ≤ ρ / (4 * (L + ‖v‖ + 1)) := hhdef ▸ (min_le_left _ _).trans (min_le_right _ _)
  have hhκ : h ≤ κ / (2 * (L + 1) * (‖v‖ + 1)) := hhdef ▸ min_le_right _ _
  have hhpos : 0 < h := by rw [hhdef]; exact lt_min (lt_min one_pos (by positivity)) (by positivity)
  refine ⟨h, hhpos, fun t ht hst hth l hl hlh => ?_⟩
  obtain ⟨d, hd⟩ : ∃ d, d = t - s := ⟨_, rfl⟩
  have hd0 : 0 < d := by rw [hd]; linarith
  have hdh : d < h := by rw [hd]; linarith
  have hl1 : l < 1 := lt_of_lt_of_le hlh hh1
  -- the smallness facts
  have hdρ : d * (L + ‖v‖ + 1) ≤ ρ / 4 := by
    have := (le_div_iff₀ (by positivity : (0:ℝ) < 4 * (L + ‖v‖ + 1))).1 (hdh.le.trans hhρ)
    linarith
  obtain ⟨D, hD⟩ : ∃ D, D = κ * l / (L + 1) := ⟨_, rfl⟩
  have hDpos : 0 < D := by rw [hD]; positivity
  have hldv : l * d * ‖v‖ ≤ D / 2 := by
    have h1 := (le_div_iff₀ (by positivity : (0:ℝ) < 2 * (L + 1) * (‖v‖ + 1))).1
      (hdh.le.trans hhκ)
    have h2 : d * ‖v‖ * (2 * (L + 1)) ≤ κ := by nlinarith
    have h3 : D / 2 = l * κ / (2 * (L + 1)) := by rw [hD]; field_simp
    rw [h3, le_div_iff₀ (by positivity)]
    nlinarith [mul_le_mul_of_nonneg_left h2 hl.le]
  obtain ⟨ε, hε⟩ : ∃ ε, ε = min (D / 4) (ρ / 4) := ⟨_, rfl⟩
  have hεpos : 0 < ε := by rw [hε]; exact lt_min (by positivity) (by positivity)
  have hεD : ε ≤ D / 4 := hε ▸ min_le_left _ _
  have hερ : ε ≤ ρ / 4 := hε ▸ min_le_right _ _
  obtain ⟨N, hN⟩ := exists_nat_gt (d * (2 * L + l * ‖v‖) / (D / 4))
  have hN0 : (0:ℝ) < N := lt_of_le_of_lt (by positivity) hN
  have hNpos : 0 < N := by exact_mod_cast hN0
  obtain ⟨Δ, hΔ⟩ : ∃ Δ, Δ = d / N := ⟨_, rfl⟩
  have hΔpos : 0 < Δ := by rw [hΔ]; positivity
  have hNΔ : (N:ℝ) * Δ = d := by rw [hΔ]; field_simp
  have hΔsmall : Δ * (2 * L + l * ‖v‖) < D / 4 := by
    rw [div_lt_iff₀ (by positivity)] at hN
    have : Δ * (2 * L + l * ‖v‖) * N = d * (2 * L + l * ‖v‖) := by
      rw [← hNΔ]; ring
    nlinarith
  -- the polygon
  let P : ℕ → V := fun i => α (s + i * Δ) + (l * (i * Δ)) • v
  have hP0 : P 0 = α s := by simp [P]
  have hPN : P N = α t + (l * (t - s)) • v := by
    simp only [P]; rw [hNΔ, hd, add_sub_cancel]
  rw [← hP0, ← hPN]
  refine S.cc_chain hNpos fun i hi => ?_
  have hiN : (i:ℝ) + 1 ≤ N := by exact_mod_cast hi
  obtain ⟨X, hX⟩ : ∃ X : ℝ, X = i * Δ := ⟨_, rfl⟩
  have hX0 : 0 ≤ X := by rw [hX]; exact mul_nonneg (Nat.cast_nonneg i) hΔpos.le
  have hXd : X + Δ ≤ d := by
    have := mul_le_mul_of_nonneg_right hiN hΔpos.le
    rw [hNΔ] at this; rw [hX]; linarith
  have hc1 : ((i + 1 : ℕ) : ℝ) * Δ = X + Δ := by rw [hX]; push_cast; ring
  have hPi : P i = α (s + X) + (l * X) • v := by
    show α (s + (i:ℝ) * Δ) + (l * ((i:ℝ) * Δ)) • v = _
    rw [← hX]
  have hPi1 : P (i + 1) = α (s + (X + Δ)) + (l * X + l * (s + (X + Δ) - (s + X))) • v := by
    show α (s + ((i + 1 : ℕ) : ℝ) * Δ) + (l * (((i + 1 : ℕ) : ℝ) * Δ)) • v = _
    rw [hc1]; congr 2; ring
  rw [hPi, hPi1]
  have hts : t = s + d := by rw [hd]; ring
  have hlX : l * X ≤ X := by
    have := mul_le_mul_of_nonneg_right hl1.le hX0; linarith
  have h5 : s + (X + Δ) - (s + X) = Δ := by ring
  refine S.cc_polygon_side (x₀ := α s) (v := v) htilt hLip hcc (by linarith [hs.1])
    (by linarith) (by linarith [ht.2]) hl hεpos ?_ ?_ <;>
    rw [abs_of_nonneg (mul_nonneg hl.le hX0)]
  · intro r hr
    have hrI : r ∈ Icc (0:ℝ) 1 := ⟨by linarith [hr.1, hs.1], by linarith [hr.2, ht.2]⟩
    have h1 := hLip.dist_le_mul r hrI s hs
    rw [Real.dist_eq, abs_of_nonneg (by linarith [hr.1])] at h1
    have h3 : (L:ℝ) * (r - s) ≤ L * d :=
      mul_le_mul_of_nonneg_left (by linarith [hr.2]) hLr
    have h4 : l * X * ‖v‖ ≤ d * ‖v‖ :=
      mul_le_mul_of_nonneg_right (by linarith) hnv
    rw [h5]
    have h6 : Δ * (L + l * ‖v‖) ≤ d * (L + ‖v‖) := by
      have : l * ‖v‖ ≤ ‖v‖ := by
        have := mul_le_mul_of_nonneg_right hl1.le hnv; linarith
      exact mul_le_mul (by linarith) (by linarith) (by positivity) hd0.le
    have e1 : d * (L + ‖v‖ + 1) = L * d + d * ‖v‖ + d := by ring
    have e2 : d * (L + ‖v‖) = L * d + d * ‖v‖ := by ring
    linarith
  · rw [h5, ← hD]
    have h4 : l * X * ‖v‖ ≤ l * d * ‖v‖ :=
      mul_le_mul_of_nonneg_right (mul_le_mul_of_nonneg_left (by linarith) hl.le) hnv
    linarith

/-- **Push-up along one Lipschitz causal piece** (finite dimension, locally Lipschitz `g`). -/
lemma cc_pushup_lstep [FiniteDimensional ℝ V] (hL : LocallyLipschitz S.g) {x y z : V}
    (hxy : S.LStep x y) (hyz : S.Chr y z) : S.Chr x z := by
  obtain ⟨α, hα, h0, h1⟩ := hxy
  have hαc : ContinuousOn α (Icc 0 1) := hα.1.choose_spec.continuousOn
  let A : Set ℝ := {t | t ∈ Icc (0:ℝ) 1 ∧ S.Chr (α t) z}
  have h1A : (1:ℝ) ∈ A := ⟨⟨zero_le_one, le_rfl⟩, by simp only [h1]; exact hyz⟩
  have hne : A.Nonempty := ⟨1, h1A⟩
  have hbdd : BddBelow A := ⟨0, fun t ht => ht.1.1⟩
  have hs0 : 0 ≤ sInf A := le_csInf hne fun t ht => ht.1.1
  have hs1 : sInf A ≤ 1 := csInf_le hbdd h1A
  have hsA : S.Chr (α (sInf A)) z := by
    obtain ⟨ε, hε, hloc⟩ := S.cc_local_pushup hL hα ⟨hs0, hs1⟩
    obtain ⟨t, htA, hts⟩ := exists_lt_of_csInf_lt hne (show sInf A < sInf A + ε by linarith)
    have hst : sInf A ≤ t := csInf_le hbdd htA
    rcases hst.lt_or_eq with hst | hst
    · have hcl : Continuous fun l : ℝ => α t + (l * (t - sInf A)) • S.T (α (sInf A)) := by
        fun_prop
      have hev : ∀ᶠ l in 𝓝 (0:ℝ), S.Chr (α t + (l * (t - sInf A)) • S.T (α (sInf A))) z := by
        have := hcl.tendsto 0
        simp only [zero_mul, zero_smul, add_zero] at this
        exact this.eventually ((S.cc_isOpen_Ipast z).mem_nhds htA.2)
      obtain ⟨l, hl, hlpos, hlε⟩ :=
        ((hev.filter_mono nhdsWithin_le_nhds).and (Ioo_mem_nhdsGT hε)).exists
      exact Relation.TransGen.trans (hloc t htA.1 hst hts l hlpos hlε) hl
    · rw [hst]; exact htA.2
  have hs : sInf A = 0 := by
    by_contra hne0
    have hspos : 0 < sInf A := lt_of_le_of_ne hs0 (Ne.symm hne0)
    have hev : ∀ᶠ t in 𝓝[Icc 0 1] (sInf A), S.Chr (α t) z :=
      (hαc _ ⟨hs0, hs1⟩).eventually ((S.cc_isOpen_Ipast z).mem_nhds hsA)
    obtain ⟨δ, hδ, hδP⟩ := Metric.eventually_nhds_iff.1 (eventually_nhdsWithin_iff.1 hev)
    have hm1 := min_le_left δ (sInf A)
    have hm2 := min_le_right δ (sInf A)
    have hm3 := lt_min hδ hspos
    have ht : sInf A - min δ (sInf A) / 2 ∈ A := by
      have hI : sInf A - min δ (sInf A) / 2 ∈ Icc (0:ℝ) 1 := ⟨by linarith, by linarith⟩
      refine ⟨hI, hδP ?_ hI⟩
      rw [Real.dist_eq, abs_lt]; constructor <;> linarith
    have := csInf_le hbdd ht
    linarith
  rw [← h0, ← hs]; exact hsA

/-- **Push-up for the Lipschitz relation** (finite dimension, locally Lipschitz `g`):
`LCau q p → Chr p z → Chr q z`, i.e. `J⁻_Lip(I⁻(z)) ⊆ I⁻(z)`. -/
theorem cc_pushup [FiniteDimensional ℝ V] (hL : LocallyLipschitz S.g) {q p z : V}
    (hqp : S.LCau q p) (hpz : S.Chr p z) : S.Chr q z := by
  induction hqp using Relation.ReflTransGen.head_induction_on with
  | refl => exact hpz
  | head h _ ih => exact S.cc_pushup_lstep hL h ih

/-! ### Part ③ (stretch): limit curves on the boundary of `J⁻(A)` -/

/-- Mean value theorem, convex-hull form (copied from `probes/LimitCurves.lean`). -/
theorem cc_chord_mem_of_deriv_mem {γ γ' : ℝ → V} {s t : ℝ} (hst : s < t)
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

/-- A `C¹` curve in `M` with velocity in the closed cone is Lipschitz causal (copied from
`probes/LimitCurves.lean`). -/
theorem cc_c1_lipCausal {γ : ℝ → V} (hγ : ContDiff ℝ 1 γ)
    (hc : ∀ t ∈ Icc (0:ℝ) 1, γ t ∈ S.M ∧ deriv γ t ∈ S.CC (γ t)) : S.LipCausal γ := by
  refine ⟨?_, fun t ht => (hc t ht).1, ?_⟩
  · exact (hγ.locallyLipschitz.locallyLipschitzOn).exists_lipschitzOnWith_of_compact isCompact_Icc
  · intro s t hs hst ht ε hε
    refine cc_chord_mem_of_deriv_mem hst hγ.continuous.continuousOn
      (fun r _ => ((hγ.differentiable one_ne_zero) r).hasDerivAt) (S.cc_convex_coneHull _ _)
      (S.cc_isClosed_coneHull _ _) fun r hr => ?_
    have hrI : r ∈ Icc (0:ℝ) 1 := ⟨by linarith [hr.1], by linarith [hr.2]⟩
    obtain ⟨hM, hC⟩ := hc r hrI
    exact S.cc_cone_subset_coneHull (self_subset_thickening hε (γ '' Icc s t)
      (mem_image_of_mem γ (Ioo_subset_Icc_self hr))) hM hC

/-- **Bridge** `I ⊆ J_Lip`: a chronological chain gives the Lipschitz causal relation. -/
theorem cc_chr_lcau {x y : V} (h : S.Chr x y) : S.LCau x y := by
  have hstep : ∀ {a b : V}, S.TStep a b → S.LStep a b := by
    intro a b hab
    obtain ⟨γ, hγ, h0, h1, hc⟩ := hab
    exact ⟨γ, S.cc_c1_lipCausal hγ fun t ht => ⟨(hc t ht).1, (hc t ht).2.1.le,
      (hc t ht).2.2.le⟩, h0, h1⟩
  induction h with
  | single h => exact Relation.ReflTransGen.single (hstep h)
  | tail _ h ih => exact ih.tail (hstep h)

/-- **Restriction.** The affine reparametrisation `r ↦ γ(a + r (b − a))` of a Lipschitz causal
curve to a subinterval `[a, b] ⊆ [0,1]` is Lipschitz causal. -/
theorem cc_restrict {γ : ℝ → V} (hγ : S.LipCausal γ) {a b : ℝ} (ha : 0 ≤ a) (hab : a < b)
    (hb : b ≤ 1) : S.LipCausal (fun r => γ (a + r * (b - a))) := by
  obtain ⟨⟨L, hL⟩, hM, hcc⟩ := hγ
  have hba : 0 < b - a := sub_pos.2 hab
  have hf : ∀ r ∈ Icc (0:ℝ) 1, a + r * (b - a) ∈ Icc (0:ℝ) 1 := fun r hr =>
    ⟨by nlinarith [hr.1], by nlinarith [hr.2]⟩
  refine ⟨⟨_, LipschitzOnWith.of_dist_le' (K := L * (b - a)) fun x hx y hy => ?_⟩,
    fun r hr => hM (hf r hr), ?_⟩
  · have := hL.dist_le_mul _ (hf x hx) _ (hf y hy)
    have e : dist (a + x * (b - a)) (a + y * (b - a)) = (b - a) * dist x y := by
      rw [Real.dist_eq, Real.dist_eq, show a + x * (b - a) - (a + y * (b - a)) = (x - y) * (b - a)
        by ring, abs_mul, abs_of_pos hba, mul_comm]
    rw [e] at this; linarith
  · intro s t hs hst ht ε hε
    have hfs := hf s ⟨hs, by linarith⟩
    have hft := hf t ⟨by linarith, ht⟩
    have hlt : a + s * (b - a) < a + t * (b - a) := by nlinarith
    have hq := hcc _ _ hfs.1 hlt hft.2 ε hε
    have h1 := S.cc_coneHull_smul hba hq
    have e : (b - a) • ((a + t * (b - a) - (a + s * (b - a)))⁻¹ •
        (γ (a + t * (b - a)) - γ (a + s * (b - a)))) =
        (t - s)⁻¹ • ((fun r => γ (a + r * (b - a))) t - (fun r => γ (a + r * (b - a))) s) := by
      rw [smul_smul, show a + t * (b - a) - (a + s * (b - a)) = (t - s) * (b - a) by ring,
        mul_inv, ← mul_assoc, mul_comm (b - a), mul_assoc, mul_inv_cancel₀ hba.ne', mul_one]
    rw [e] at h1
    refine S.cc_coneHull_mono_set ?_ h1
    rintro _ ⟨r, hr, rfl⟩
    refine ⟨(r - a) / (b - a), ⟨?_, ?_⟩, ?_⟩
    · rw [le_div_iff₀ hba]; linarith [hr.1]
    · rw [div_le_iff₀ hba]; linarith [hr.2]
    · simp only
      congr 1; field_simp; ring

/-- Points of a Lipschitz causal curve are Lipschitz-causally related in curve order. -/
lemma cc_lcau_of_le {γ : ℝ → V} (hγ : S.LipCausal γ) {a b : ℝ} (ha : 0 ≤ a) (hab : a ≤ b)
    (hb : b ≤ 1) : S.LCau (γ a) (γ b) := by
  rcases hab.lt_or_eq with hlt | heq
  · refine Relation.ReflTransGen.single ⟨_, S.cc_restrict hγ ha hlt hb, by simp, ?_⟩
    simp
  · rw [heq]; exact Relation.ReflTransGen.refl

/-- The Lipschitz causal past `J⁻_Lip(A)`. -/
def JpastL (A : Set V) : Set V := {x | ∃ y ∈ A, S.LCau x y}

/-- The chronological past `I⁻(A)`. -/
def IpastSet (A : Set V) : Set V := {x | ∃ y ∈ A, S.Chr x y}

theorem cc_isOpen_IpastSet (A : Set V) : IsOpen (S.IpastSet A) := by
  have : S.IpastSet A = ⋃ y ∈ A, S.Ipast y := by
    ext x; simp [IpastSet, Ipast]
  rw [this]; exact isOpen_biUnion fun y _ => S.cc_isOpen_Ipast y

theorem cc_IpastSet_subset_interior (A : Set V) : S.IpastSet A ⊆ interior (S.JpastL A) :=
  interior_maximal (fun _ ⟨y, hy, h⟩ => ⟨y, hy, S.cc_chr_lcau h⟩) (S.cc_isOpen_IpastSet A)

/-- **Limit curve from a boundary point** (stretch ③, BUILT IN PART). Let `p` be a boundary point of
`J⁻_Lip(A)`, approached by points `pₙ` joined to points `qₙ ∈ A` by Lipschitz causal pieces inside a
compact `K ⊆ M` over which a time functional `τ` is positive on the cones. Then there is a Lipschitz
causal curve `γ` in `K` from `p` to a point of `closure A` all of whose points lie in
`closure J⁻_Lip(A)` but **not** in `I⁻(A)`. The last clause is push-up (`cc_pushup`). Upgrading
"not in `I⁻(A)`" to "on `∂J⁻_Lip(A)`" needs `interior J⁻_Lip(A) ⊆ I⁻(A)`, which is not proved. -/
theorem cc_boundary_limit_curve [FiniteDimensional ℝ V] (hL : LocallyLipschitz S.g)
    {K : Set V} (hK : IsCompact K) (hKM : K ⊆ S.M) (τ : V →L[ℝ] ℝ)
    (hτ : ∀ x ∈ K, ∀ v ∈ S.CC x, v ≠ 0 → 0 < τ v) {A : Set V} {p : V}
    (hp : p ∈ frontier (S.JpastL A)) {P Q : ℕ → V} (hP : Tendsto P atTop (𝓝 p))
    (hQA : ∀ n, Q n ∈ A) (hstep : ∀ n, S.LStepIn K (P n) (Q n)) :
    ∃ γ : ℝ → V, S.LipCausal γ ∧ MapsTo γ (Icc 0 1) K ∧ γ 0 = p ∧ γ 1 ∈ closure A ∧
      ∀ u ∈ Icc (0:ℝ) 1, γ u ∈ closure (S.JpastL A) ∧ γ u ∉ S.IpastSet A := by
  obtain ⟨L, hLu⟩ := S.cc_uniform_pieces hK τ hτ
  have h : ∀ n, ∃ γ' : ℝ → V, S.LipCausal γ' ∧ LipschitzOnWith L γ' (Icc 0 1) ∧
      MapsTo γ' (Icc 0 1) K ∧ γ' 0 = P n ∧ γ' 1 = Q n := fun n => by
    obtain ⟨γ, h1, h2, h3, h4⟩ := hstep n
    exact hLu _ _ γ h1 h2 h3 h4
  choose F hF hFL hFK hF0 hF1 using h
  obtain ⟨φ, hφ, γ, hu, -, hγK, hγ⟩ :=
    S.cc_arzela_ascoli hK hKM hFL hFK (fun n => (hF n).2.2)
  have hγ0 : γ 0 = p := by
    refine tendsto_nhds_unique (hu.tendsto_at ⟨le_rfl, zero_le_one⟩) ?_
    simpa [Function.comp_def, hF0] using hP.comp hφ.tendsto_atTop
  refine ⟨γ, hγ, hγK, hγ0, ?_, fun u hu' => ⟨?_, ?_⟩⟩
  · refine mem_closure_of_tendsto (hu.tendsto_at ⟨zero_le_one, le_rfl⟩)
      (Eventually.of_forall fun n => ?_)
    simp only [hF1]; exact hQA _
  · refine mem_closure_of_tendsto (hu.tendsto_at hu') (Eventually.of_forall fun n => ?_)
    refine ⟨Q (φ n), hQA _, ?_⟩
    rw [← hF1]; exact S.cc_lcau_of_le (hF _) hu'.1 hu'.2 le_rfl
  · rintro ⟨z, hz, hchr⟩
    have h1 : S.LCau p (γ u) := hγ0 ▸ S.cc_lcau_of_le hγ le_rfl hu'.1 hu'.2
    have h2 : p ∈ S.IpastSet A := ⟨z, hz, S.cc_pushup hL h1 hchr⟩
    exact hp.2 (S.cc_IpastSet_subset_interior A h2)

/-- Nonconstancy: if the boundary point is off `closure A`, the limit curve is not constant. -/
theorem cc_boundary_limit_curve_nonconst [FiniteDimensional ℝ V] (hL : LocallyLipschitz S.g)
    {K : Set V} (hK : IsCompact K) (hKM : K ⊆ S.M) (τ : V →L[ℝ] ℝ)
    (hτ : ∀ x ∈ K, ∀ v ∈ S.CC x, v ≠ 0 → 0 < τ v) {A : Set V} {p : V}
    (hp : p ∈ frontier (S.JpastL A)) (hpA : p ∉ closure A) {P Q : ℕ → V}
    (hP : Tendsto P atTop (𝓝 p)) (hQA : ∀ n, Q n ∈ A) (hstep : ∀ n, S.LStepIn K (P n) (Q n)) :
    ∃ γ : ℝ → V, S.LipCausal γ ∧ MapsTo γ (Icc 0 1) K ∧ γ 0 = p ∧ γ 1 ≠ p ∧
      ∀ u ∈ Icc (0:ℝ) 1, γ u ∈ closure (S.JpastL A) ∧ γ u ∉ S.IpastSet A := by
  obtain ⟨γ, h1, h2, h3, h4, h5⟩ :=
    S.cc_boundary_limit_curve hL hK hKM τ hτ hp hP hQA hstep
  exact ⟨γ, h1, h2, h3, fun h => hpA (h ▸ h4), h5⟩

/-! ### Part ③: the dual push-up `I ∘ J_Lip ⊆ I`, and `int J⁻ ⊆ I⁻` -/

/-- **Dual local push-up** (finite dimension, locally Lipschitz `g`): for `t` slightly before `s`
and small `l > 0`, `α t − l (s − t) T(α s) ≪ α s`. Same polygon, with the tilt into the past. -/
lemma cc_local_pushup' [FiniteDimensional ℝ V] (hL : LocallyLipschitz S.g) {α : ℝ → V}
    (hα : S.LipCausal α) {s : ℝ} (hs : s ∈ Icc (0:ℝ) 1) :
    ∃ h > 0, ∀ t ∈ Icc (0:ℝ) 1, t < s → s < t + h → ∀ l : ℝ, 0 < l → l < h →
      S.Chr (α t + (l * (t - s)) • S.T (α s)) (α s) := by
  obtain ⟨⟨L, hLip⟩, hαM, hcc⟩ := hα
  obtain ⟨ρ, hρ, κ, hκ, htilt⟩ := S.cc_tilt hL (hαM hs)
  obtain ⟨v, hv⟩ : ∃ v, v = S.T (α s) := ⟨_, rfl⟩
  rw [← hv] at htilt ⊢
  have hLr : (0:ℝ) ≤ L := L.2
  have hnv := norm_nonneg v
  obtain ⟨h, hhdef⟩ : ∃ h : ℝ, h = min (min 1 (ρ / (4 * (L + ‖v‖ + 1))))
      (κ / (2 * (L + 1) * (‖v‖ + 1))) := ⟨_, rfl⟩
  have hh1 : h ≤ 1 := hhdef ▸ (min_le_left _ _).trans (min_le_left _ _)
  have hhρ : h ≤ ρ / (4 * (L + ‖v‖ + 1)) := hhdef ▸ (min_le_left _ _).trans (min_le_right _ _)
  have hhκ : h ≤ κ / (2 * (L + 1) * (‖v‖ + 1)) := hhdef ▸ min_le_right _ _
  have hhpos : 0 < h := by rw [hhdef]; exact lt_min (lt_min one_pos (by positivity)) (by positivity)
  refine ⟨h, hhpos, fun t ht hts hth l hl hlh => ?_⟩
  obtain ⟨d, hd⟩ : ∃ d, d = s - t := ⟨_, rfl⟩
  have hd0 : 0 < d := by rw [hd]; linarith
  have hdh : d < h := by rw [hd]; linarith
  have hl1 : l < 1 := lt_of_lt_of_le hlh hh1
  have hdρ : d * (L + ‖v‖ + 1) ≤ ρ / 4 := by
    have := (le_div_iff₀ (by positivity : (0:ℝ) < 4 * (L + ‖v‖ + 1))).1 (hdh.le.trans hhρ)
    linarith
  obtain ⟨D, hD⟩ : ∃ D, D = κ * l / (L + 1) := ⟨_, rfl⟩
  have hDpos : 0 < D := by rw [hD]; positivity
  have hldv : l * d * ‖v‖ ≤ D / 2 := by
    have h1 := (le_div_iff₀ (by positivity : (0:ℝ) < 2 * (L + 1) * (‖v‖ + 1))).1
      (hdh.le.trans hhκ)
    have h2 : d * ‖v‖ * (2 * (L + 1)) ≤ κ := by nlinarith
    have h3 : D / 2 = l * κ / (2 * (L + 1)) := by rw [hD]; field_simp
    rw [h3, le_div_iff₀ (by positivity)]
    nlinarith [mul_le_mul_of_nonneg_left h2 hl.le]
  obtain ⟨ε, hε⟩ : ∃ ε, ε = min (D / 4) (ρ / 4) := ⟨_, rfl⟩
  have hεpos : 0 < ε := by rw [hε]; exact lt_min (by positivity) (by positivity)
  have hεD : ε ≤ D / 4 := hε ▸ min_le_left _ _
  have hερ : ε ≤ ρ / 4 := hε ▸ min_le_right _ _
  obtain ⟨N, hN⟩ := exists_nat_gt (d * (2 * L + l * ‖v‖) / (D / 4))
  have hN0 : (0:ℝ) < N := lt_of_le_of_lt (by positivity) hN
  have hNpos : 0 < N := by exact_mod_cast hN0
  obtain ⟨Δ, hΔ⟩ : ∃ Δ, Δ = d / N := ⟨_, rfl⟩
  have hΔpos : 0 < Δ := by rw [hΔ]; positivity
  have hNΔ : (N:ℝ) * Δ = d := by rw [hΔ]; field_simp
  have hΔsmall : Δ * (2 * L + l * ‖v‖) < D / 4 := by
    rw [div_lt_iff₀ (by positivity)] at hN
    have : Δ * (2 * L + l * ‖v‖) * N = d * (2 * L + l * ‖v‖) := by
      rw [← hNΔ]; ring
    nlinarith
  let P : ℕ → V := fun i => α (t + i * Δ) + (l * (i * Δ - d)) • v
  have hP0 : P 0 = α t + (l * (t - s)) • v := by
    show α (t + ((0:ℕ):ℝ) * Δ) + (l * (((0:ℕ):ℝ) * Δ - d)) • v = _
    rw [Nat.cast_zero, zero_mul, add_zero, zero_sub, hd]; congr 2; ring
  have hPN : P N = α s := by
    show α (t + (N:ℝ) * Δ) + (l * ((N:ℝ) * Δ - d)) • v = α s
    rw [hNΔ, sub_self, mul_zero, zero_smul, add_zero, hd]; congr 1; ring
  rw [← hP0, ← hPN]
  refine S.cc_chain hNpos fun i hi => ?_
  have hiN : (i:ℝ) + 1 ≤ N := by exact_mod_cast hi
  obtain ⟨X, hX⟩ : ∃ X : ℝ, X = i * Δ := ⟨_, rfl⟩
  have hX0 : 0 ≤ X := by rw [hX]; exact mul_nonneg (Nat.cast_nonneg i) hΔpos.le
  have hXd : X + Δ ≤ d := by
    have := mul_le_mul_of_nonneg_right hiN hΔpos.le
    rw [hNΔ] at this; rw [hX]; linarith
  have hc1 : ((i + 1 : ℕ) : ℝ) * Δ = X + Δ := by rw [hX]; push_cast; ring
  have hPi : P i = α (t + X) + (l * (X - d)) • v := by
    show α (t + (i:ℝ) * Δ) + (l * ((i:ℝ) * Δ - d)) • v = _
    rw [← hX]
  have hPi1 : P (i + 1) = α (t + (X + Δ)) + (l * (X - d) + l * (t + (X + Δ) - (t + X))) • v := by
    show α (t + ((i + 1 : ℕ) : ℝ) * Δ) + (l * (((i + 1 : ℕ) : ℝ) * Δ - d)) • v = _
    rw [hc1]; congr 2; ring
  rw [hPi, hPi1]
  have hst' : s = t + d := by rw [hd]; ring
  have habs : |l * (X - d)| = l * (d - X) := by
    rw [abs_of_nonpos (mul_nonpos_of_nonneg_of_nonpos hl.le (by linarith))]; ring
  have hlX : l * (d - X) ≤ d - X := by
    have := mul_le_mul_of_nonneg_right hl1.le (show 0 ≤ d - X by linarith); linarith
  have h5 : t + (X + Δ) - (t + X) = Δ := by ring
  refine S.cc_polygon_side (x₀ := α s) (v := v) htilt hLip hcc (by linarith [ht.1])
    (by linarith) (by linarith [hs.2]) hl hεpos ?_ ?_ <;> rw [habs]
  · intro r hr
    have hrI : r ∈ Icc (0:ℝ) 1 := ⟨by linarith [hr.1, ht.1], by linarith [hr.2, hs.2]⟩
    have h1 := hLip.dist_le_mul r hrI s hs
    rw [Real.dist_eq, abs_of_nonpos (by linarith [hr.2])] at h1
    have h3 : (L:ℝ) * (-(r - s)) ≤ L * d :=
      mul_le_mul_of_nonneg_left (by linarith [hr.1]) hLr
    have h4 : l * (d - X) * ‖v‖ ≤ d * ‖v‖ :=
      mul_le_mul_of_nonneg_right (by linarith) hnv
    rw [h5]
    have h6 : Δ * (L + l * ‖v‖) ≤ d * (L + ‖v‖) := by
      have : l * ‖v‖ ≤ ‖v‖ := by
        have := mul_le_mul_of_nonneg_right hl1.le hnv; linarith
      exact mul_le_mul (by linarith) (by linarith) (by positivity) hd0.le
    have e1 : d * (L + ‖v‖ + 1) = L * d + d * ‖v‖ + d := by ring
    have e2 : d * (L + ‖v‖) = L * d + d * ‖v‖ := by ring
    linarith
  · rw [h5, ← hD]
    have h4 : l * (d - X) * ‖v‖ ≤ l * d * ‖v‖ :=
      mul_le_mul_of_nonneg_right (mul_le_mul_of_nonneg_left (by linarith) hl.le) hnv
    linarith

/-- Chronological future `I⁺(p)`. -/
def Ifut (p : V) : Set V := {q | S.Chr p q}

/-- The end of a timelike step can be moved in an open set (copied from campaign 60). -/
lemma cc_tstep_end_eventually {y q : V} (h : S.TStep y q) : ∀ᶠ q' in 𝓝 q, S.TStep y q' := by
  obtain ⟨γ, hγ, h0, h1, hγt⟩ := h
  have hdc : Continuous (deriv γ) := hγ.continuous_deriv le_rfl
  have hT := S.cc_tube (P := fun w t => γ t + t • w) (Q := fun w t => deriv γ t + w)
    ((hγ.continuous.comp continuous_snd).add (continuous_snd.smul continuous_fst))
    ((hdc.comp continuous_snd).add continuous_fst) (by simpa using hγt)
  have hlim : Tendsto (fun q' => q' - q) (𝓝 q) (𝓝 0) := tendsto_sub_nhds_zero_iff.2 tendsto_id
  filter_upwards [hlim.eventually hT] with q' hq'
  refine ⟨fun t => γ t + t • (q' - q), hγ.add (contDiff_id.smul contDiff_const), by simp [h0],
    by simp [h1], fun t ht => ?_⟩
  have hd : deriv (fun t => γ t + t • (q' - q)) t = deriv γ t + (q' - q) := by
    have h : HasDerivAt (fun t => γ t + t • (q' - q)) (deriv γ t + (1:ℝ) • (q' - q)) t :=
      (cc_hasDerivAt_of_contDiff hγ t).add ((hasDerivAt_id' t).smul_const (q' - q))
    rw [h.deriv, one_smul]
  rw [hd]; exact hq' t ht

theorem cc_isOpen_Ifut (p : V) : IsOpen (S.Ifut p) := by
  refine isOpen_iff_mem_nhds.2 fun q hq => ?_
  obtain ⟨y, hpy, hyq⟩ := Relation.TransGen.tail'_iff.1 hq
  filter_upwards [S.cc_tstep_end_eventually hyq] with q' hq'
  exact Relation.TransGen.tail' hpy hq'

/-- **Dual push-up along one Lipschitz causal piece**: `q ≪ x`, `x → y` Lipschitz causal give
`q ≪ y` (finite dimension, locally Lipschitz `g`). -/
lemma cc_pushup_dual_lstep [FiniteDimensional ℝ V] (hL : LocallyLipschitz S.g) {q x y : V}
    (hqx : S.Chr q x) (hxy : S.LStep x y) : S.Chr q y := by
  obtain ⟨α, hα, h0, h1⟩ := hxy
  have hαc : ContinuousOn α (Icc 0 1) := hα.1.choose_spec.continuousOn
  let B : Set ℝ := {t | t ∈ Icc (0:ℝ) 1 ∧ S.Chr q (α t)}
  have h0B : (0:ℝ) ∈ B := ⟨⟨le_rfl, zero_le_one⟩, by simp only [h0]; exact hqx⟩
  have hne : B.Nonempty := ⟨0, h0B⟩
  have hbdd : BddAbove B := ⟨1, fun t ht => ht.1.2⟩
  have hs0 : 0 ≤ sSup B := le_csSup hbdd h0B
  have hs1 : sSup B ≤ 1 := csSup_le hne fun t ht => ht.1.2
  have hsB : S.Chr q (α (sSup B)) := by
    obtain ⟨ε, hε, hloc⟩ := S.cc_local_pushup' hL hα ⟨hs0, hs1⟩
    obtain ⟨t, htB, hts⟩ := exists_lt_of_lt_csSup hne (show sSup B - ε < sSup B by linarith)
    have hst : t ≤ sSup B := le_csSup hbdd htB
    rcases hst.lt_or_eq with hst | hst
    · have hcl : Continuous fun l : ℝ => α t + (l * (t - sSup B)) • S.T (α (sSup B)) := by
        fun_prop
      have hev : ∀ᶠ l in 𝓝 (0:ℝ), S.Chr q (α t + (l * (t - sSup B)) • S.T (α (sSup B))) := by
        have := hcl.tendsto 0
        simp only [zero_mul, zero_smul, add_zero] at this
        exact this.eventually ((S.cc_isOpen_Ifut q).mem_nhds htB.2)
      obtain ⟨l, hl, hlpos, hlε⟩ :=
        ((hev.filter_mono nhdsWithin_le_nhds).and (Ioo_mem_nhdsGT hε)).exists
      exact Relation.TransGen.trans hl (hloc t htB.1 hst (by linarith) l hlpos hlε)
    · rw [← hst]; exact htB.2
  have hs : sSup B = 1 := by
    by_contra hne1
    have hslt : sSup B < 1 := lt_of_le_of_ne hs1 hne1
    have hev : ∀ᶠ t in 𝓝[Icc 0 1] (sSup B), S.Chr q (α t) :=
      (hαc _ ⟨hs0, hs1⟩).eventually ((S.cc_isOpen_Ifut q).mem_nhds hsB)
    obtain ⟨δ, hδ, hδP⟩ := Metric.eventually_nhds_iff.1 (eventually_nhdsWithin_iff.1 hev)
    have hm1 := min_le_left δ (1 - sSup B)
    have hm2 := min_le_right δ (1 - sSup B)
    have hm3 : 0 < min δ (1 - sSup B) := lt_min hδ (by linarith)
    have ht : sSup B + min δ (1 - sSup B) / 2 ∈ B := by
      have hI : sSup B + min δ (1 - sSup B) / 2 ∈ Icc (0:ℝ) 1 := ⟨by linarith, by linarith⟩
      refine ⟨hI, hδP ?_ hI⟩
      rw [Real.dist_eq, abs_lt]; constructor <;> linarith
    have := le_csSup hbdd ht
    linarith
  rw [← h1, ← hs]; exact hsB

/-- **Dual push-up for the Lipschitz relation**: `Chr q p → LCau p z → Chr q z`. -/
theorem cc_pushup_dual [FiniteDimensional ℝ V] (hL : LocallyLipschitz S.g) {q p z : V}
    (hqp : S.Chr q p) (hpz : S.LCau p z) : S.Chr q z := by
  induction hpz with
  | refl => exact hqp
  | tail _ h ih => exact S.cc_pushup_dual_lstep hL ih h

/-- **`int J⁻_Lip(A) ⊆ I⁻(A)`** on `M` (finite dimension, locally Lipschitz `g`). A point `x` of
the interior is followed by a short timelike segment along `T x` to a point still in `J⁻_Lip(A)`,
and the dual push-up concludes. -/
theorem cc_interior_JpastL_subset [FiniteDimensional ℝ V] (hL : LocallyLipschitz S.g)
    (A : Set V) : interior (S.JpastL A) ∩ S.M ⊆ S.IpastSet A := by
  rintro x ⟨hxi, hxM⟩
  have hO : IsOpen {p | p ∈ S.M ∧ S.FutTimelike p (S.T x)} :=
    S.cc_isOpen_timelikePairs.preimage (continuous_id.prodMk continuous_const)
  have hT := S.T_timelike x hxM
  have hU : interior (S.JpastL A) ∩ {p | p ∈ S.M ∧ S.FutTimelike p (S.T x)} ∈ 𝓝 x :=
    inter_mem (isOpen_interior.mem_nhds hxi) (hO.mem_nhds ⟨hxM, hT, hT⟩)
  obtain ⟨ε, hε, hball⟩ := Metric.mem_nhds_iff.1 hU
  obtain ⟨η, hη⟩ : ∃ η : ℝ, η = ε / (2 * (‖S.T x‖ + 1)) := ⟨_, rfl⟩
  have hηpos : 0 < η := by rw [hη]; positivity
  have hseg : ∀ r ∈ Icc (0:ℝ) 1, x + r • (η • S.T x) ∈ ball x ε := by
    intro r hr
    rw [mem_ball, dist_eq_norm, add_sub_cancel_left, norm_smul, norm_smul,
      Real.norm_of_nonneg hr.1, Real.norm_of_nonneg hηpos.le]
    have h1 : η * ‖S.T x‖ < ε := by
      rw [hη, div_mul_eq_mul_div, div_lt_iff₀ (by positivity)]
      nlinarith [norm_nonneg (S.T x)]
    have h2 : r * (η * ‖S.T x‖) ≤ η * ‖S.T x‖ := by
      have : 0 ≤ η * ‖S.T x‖ := by positivity
      nlinarith [hr.2]
    linarith
  have hstep : S.TStep x (x + η • S.T x) := by
    refine S.cc_segment_tstep fun r hr => ?_
    rw [add_sub_cancel_left]
    have := (hball (hseg r hr)).2
    exact ⟨this.1, S.cc_futTimelike_smul hηpos this.2⟩
  have hx' : x + η • S.T x ∈ S.JpastL A := by
    have := hseg 1 ⟨zero_le_one, le_rfl⟩
    rw [one_smul] at this
    exact interior_subset (hball this).1
  obtain ⟨a, ha, hlc⟩ := hx'
  exact ⟨a, ha, S.cc_pushup_dual hL (Relation.TransGen.single hstep) hlc⟩

/-- **A boundary generator of `J⁻_Lip(A)`** (stretch ③; finite dimension, locally Lipschitz `g`).
Let `p ∈ ∂J⁻_Lip(A) ∖ closure A` be approached by points `pₙ` joined to points `qₙ ∈ A` by
Lipschitz causal pieces inside a compact `K ⊆ M` over which the time functional `τ` is positive on
the cones. Then there is a non-constant Lipschitz future-causal curve `γ` in `K` from `p` to a
point of `closure A`, lying entirely in `∂J⁻_Lip(A)`, and **achronal**: no two of its points are
chronologically related. -/
theorem cc_boundary_generator [FiniteDimensional ℝ V] (hL : LocallyLipschitz S.g)
    {K : Set V} (hK : IsCompact K) (hKM : K ⊆ S.M) (τ : V →L[ℝ] ℝ)
    (hτ : ∀ x ∈ K, ∀ v ∈ S.CC x, v ≠ 0 → 0 < τ v) {A : Set V} {p : V}
    (hp : p ∈ frontier (S.JpastL A)) (hpA : p ∉ closure A) {P Q : ℕ → V}
    (hP : Tendsto P atTop (𝓝 p)) (hQA : ∀ n, Q n ∈ A) (hstep : ∀ n, S.LStepIn K (P n) (Q n)) :
    ∃ γ : ℝ → V, S.LipCausal γ ∧ MapsTo γ (Icc 0 1) K ∧ γ 0 = p ∧ γ 1 ∈ closure A ∧
      γ 1 ≠ p ∧ MapsTo γ (Icc 0 1) (frontier (S.JpastL A)) ∧
      ∀ u ∈ Icc (0:ℝ) 1, ∀ u' ∈ Icc (0:ℝ) 1, ¬ S.Chr (γ u) (γ u') := by
  obtain ⟨γ, h1, h2, h3, h4, h5⟩ :=
    S.cc_boundary_limit_curve hL hK hKM τ hτ hp hP hQA hstep
  refine ⟨γ, h1, h2, h3, h4, fun h => hpA (h ▸ h4), fun u hu => ⟨(h5 u hu).1, fun hint => ?_⟩,
    fun u hu u' hu' hchr => ?_⟩
  · exact (h5 u hu).2 (S.cc_interior_JpastL_subset hL A ⟨hint, hKM (h2 hu)⟩)
  · obtain ⟨w, hwI, hwJ⟩ := mem_closure_iff_nhds.1 (h5 u' hu').1 (S.Ifut (γ u))
      ((S.cc_isOpen_Ifut (γ u)).mem_nhds hchr)
    obtain ⟨a, ha, hwa⟩ := hwJ
    exact (h5 u hu).2 ⟨a, ha, S.cc_pushup_dual hL hwI hwa⟩


/-! ## Part ①: concatenation -/

/-- The cone condition on a subinterval `[a, b]`. On `[0,1]` it is `ConeCond`. -/
def ConeCondOn (γ : ℝ → V) (a b : ℝ) : Prop :=
  ∀ s t : ℝ, a ≤ s → s < t → t ≤ b → ∀ ε > 0,
    (t - s)⁻¹ • (γ t - γ s) ∈ S.coneHull ε (γ '' Icc s t)

/-- **Chord splitting.** For `s < m < t`, the chord quotient over `[s,t]` is the convex combination
`((m−s)/(t−s))·q[s,m] + ((t−m)/(t−s))·q[m,t]` of the two sub-chord quotients, so it lies in any
convex set containing both. -/
theorem cc_chord_split {γ : ℝ → V} {H : Set V} (hH : Convex ℝ H) {s m t : ℝ} (hsm : s < m)
    (hmt : m < t) (h1 : (m - s)⁻¹ • (γ m - γ s) ∈ H) (h2 : (t - m)⁻¹ • (γ t - γ m) ∈ H) :
    (t - s)⁻¹ • (γ t - γ s) ∈ H := by
  have hts : 0 < t - s := by linarith
  have hms : 0 < m - s := by linarith
  have htm : 0 < t - m := by linarith
  have hsum : (m - s) / (t - s) + (t - m) / (t - s) = 1 := by
    rw [← add_div, div_eq_one_iff_eq hts.ne']; ring
  have key := hH h1 h2 (div_nonneg hms.le hts.le) (div_nonneg htm.le hts.le) hsum
  convert key using 1
  rw [smul_smul, smul_smul]
  have e1 : (m - s) / (t - s) * (m - s)⁻¹ = (t - s)⁻¹ := by field_simp
  have e2 : (t - m) / (t - s) * (t - m)⁻¹ = (t - s)⁻¹ := by field_simp
  rw [e1, e2, ← smul_add]
  congr 1; abel

/-- **Gluing the cone condition** across a junction `m`: the cone condition on `[a,m]` and on
`[m,b]` gives it on `[a,b]`. Chords across `m` are split (`cc_chord_split`); each sub-chord lies in
the cone hull of its sub-arc, hence of the whole arc (monotonicity), and cone hulls are convex. -/
theorem cc_coneCondOn_glue {γ : ℝ → V} {a m b : ℝ} (h1 : S.ConeCondOn γ a m)
    (h2 : S.ConeCondOn γ m b) : S.ConeCondOn γ a b := by
  intro s t hs hst htb ε hε
  rcases le_or_gt t m with htm | hmt
  · exact h1 s t hs hst htm ε hε
  rcases le_or_gt m s with hms | hsm
  · exact h2 s t hms hst htb ε hε
  refine cc_chord_split (S.cc_convex_coneHull ε _) hsm hmt ?_ ?_
  · exact S.cc_coneHull_mono_set (image_mono (Icc_subset_Icc_right hmt.le))
      (h1 s m hs hsm le_rfl ε hε)
  · exact S.cc_coneHull_mono_set (image_mono (Icc_subset_Icc_left hsm.le))
      (h2 m t le_rfl hmt htb ε hε)

/-- The cone condition only depends on the values on the interval. -/
lemma cc_coneCondOn_congr {γ δ : ℝ → V} {a b : ℝ} (h : EqOn γ δ (Icc a b))
    (hγ : S.ConeCondOn γ a b) : S.ConeCondOn δ a b := by
  intro s t hs hst htb ε hε
  have hsub : Icc s t ⊆ Icc a b := Icc_subset_Icc hs htb
  have := hγ s t hs hst htb ε hε
  rwa [h ⟨hs, by linarith⟩, h ⟨by linarith, htb⟩, (h.mono hsub).image_eq] at this

/-- **Affine pull-back.** If `γ` has the cone condition on `[0,1]` and `c > 0`, then
`r ↦ γ (c r + d)` has it on any `[a,b]` that the affine map sends into `[0,1]`. -/
theorem cc_coneCondOn_affine {γ : ℝ → V} (hγ : S.ConeCond γ) {c d a b : ℝ} (hc : 0 < c)
    (ha : 0 ≤ c * a + d) (hb : c * b + d ≤ 1) :
    S.ConeCondOn (fun r => γ (c * r + d)) a b := by
  intro s t hs hst htb ε hε
  have h1 : c * s + d < c * t + d := by nlinarith
  have hq := hγ _ _ (by nlinarith) h1 (by nlinarith) ε hε
  have h2 := S.cc_coneHull_smul hc hq
  have e : c • ((c * t + d - (c * s + d))⁻¹ • (γ (c * t + d) - γ (c * s + d))) =
      (t - s)⁻¹ • ((fun r => γ (c * r + d)) t - (fun r => γ (c * r + d)) s) := by
    rw [smul_smul, show c * t + d - (c * s + d) = c * (t - s) by ring, mul_inv, ← mul_assoc,
      mul_inv_cancel₀ hc.ne', one_mul]
  rw [e] at h2
  refine S.cc_coneHull_mono_set ?_ h2
  rintro _ ⟨r, hr, rfl⟩
  refine ⟨(r - d) / c, ⟨?_, ?_⟩, ?_⟩
  · rw [le_div_iff₀ hc]; nlinarith [hr.1]
  · rw [div_le_iff₀ hc]; nlinarith [hr.2]
  · have : c * ((r - d) / c) + d = r := by field_simp; ring
    simp only [this]

/-- **Gluing Lipschitz bounds** across a junction `m`. -/
lemma cc_lipschitzOnWith_glue {f : ℝ → V} {L : NNReal} {a m b : ℝ}
    (h1 : LipschitzOnWith L f (Icc a m)) (h2 : LipschitzOnWith L f (Icc m b)) (ham : a ≤ m)
    (hmb : m ≤ b) : LipschitzOnWith L f (Icc a b) := by
  have key : ∀ x ∈ Icc a b, ∀ y ∈ Icc a b, x ≤ y → dist (f x) (f y) ≤ L * dist x y := by
    intro x hx y hy hxy
    rcases le_total y m with hym | hmy
    · exact h1.dist_le_mul x ⟨hx.1, hxy.trans hym⟩ y ⟨hy.1, hym⟩
    rcases le_total m x with hmx | hxm
    · exact h2.dist_le_mul x ⟨hmx, hx.2⟩ y ⟨hmy, hy.2⟩
    have e1 := h1.dist_le_mul x ⟨hx.1, hxm⟩ m ⟨ham, le_rfl⟩
    have e2 := h2.dist_le_mul m ⟨le_rfl, hmb⟩ y ⟨hmy, hy.2⟩
    have e3 := dist_triangle (f x) (f m) (f y)
    rw [Real.dist_eq] at e1 e2 ⊢
    rw [abs_of_nonpos (sub_nonpos.2 hxm)] at e1
    rw [abs_of_nonpos (sub_nonpos.2 hmy)] at e2
    rw [abs_of_nonpos (sub_nonpos.2 hxy)]
    have e4 : (L : ℝ) * -(x - m) + L * -(m - y) = L * -(x - y) := by ring
    linarith
  refine LipschitzOnWith.of_dist_le_mul fun x hx y hy => ?_
  rcases le_total x y with h | h
  · exact key x hx y hy h
  · rw [dist_comm, dist_comm x]; exact key y hy x hx h

/-- **Concatenation** of two curves on `[0,1]`: `γ₁` at double speed on `[0,½]`, then `γ₂`. -/
noncomputable def joinCurve (γ₁ γ₂ : ℝ → V) : ℝ → V :=
  fun t => if t ≤ 1 / 2 then γ₁ (2 * t) else γ₂ (2 * t - 1)

lemma cc_join_eqOn_left (γ₁ γ₂ : ℝ → V) :
    EqOn (joinCurve γ₁ γ₂) (fun r => γ₁ (2 * r + 0)) (Icc 0 (1 / 2)) := by
  intro r hr
  simp only [joinCurve, hr.2, ite_true, add_zero]

lemma cc_join_eqOn_right {γ₁ γ₂ : ℝ → V} (h : γ₁ 1 = γ₂ 0) :
    EqOn (joinCurve γ₁ γ₂) (fun r => γ₂ (2 * r + -1)) (Icc (1 / 2) 1) := by
  intro r hr
  simp only [joinCurve]
  split_ifs with hr'
  · have : r = 1 / 2 := le_antisymm hr' hr.1
    subst this; norm_num [h]
  · ring_nf

lemma cc_join_zero (γ₁ γ₂ : ℝ → V) : joinCurve γ₁ γ₂ 0 = γ₁ 0 := by
  simp [joinCurve]

lemma cc_join_one (γ₁ γ₂ : ℝ → V) : joinCurve γ₁ γ₂ 1 = γ₂ 1 := by
  simp only [joinCurve]; norm_num

lemma cc_join_mapsTo {γ₁ γ₂ : ℝ → V} {K : Set V} (h1 : MapsTo γ₁ (Icc 0 1) K)
    (h2 : MapsTo γ₂ (Icc 0 1) K) : MapsTo (joinCurve γ₁ γ₂) (Icc 0 1) K := by
  intro t ht
  simp only [joinCurve]
  split_ifs with h
  · exact h1 ⟨by linarith [ht.1], by linarith⟩
  · push Not at h
    exact h2 ⟨by linarith, by linarith [ht.2]⟩

/-- **Lipschitz constant of the concatenation**: an `L₁`-Lipschitz and an `L₂`-Lipschitz piece
join, after rescaling each by `2`, to a `2 · max L₁ L₂`-Lipschitz curve on `[0,1]`. -/
theorem cc_join_lipschitz {γ₁ γ₂ : ℝ → V} {L₁ L₂ : NNReal}
    (h1 : LipschitzOnWith L₁ γ₁ (Icc 0 1)) (h2 : LipschitzOnWith L₂ γ₂ (Icc 0 1))
    (h : γ₁ 1 = γ₂ 0) : LipschitzOnWith (2 * max L₁ L₂) (joinCurve γ₁ γ₂) (Icc 0 1) := by
  have hL1 : (L₁ : ℝ) ≤ max (L₁ : ℝ) L₂ := le_max_left _ _
  have hL2 : (L₂ : ℝ) ≤ max (L₁ : ℝ) L₂ := le_max_right _ _
  have hd : ∀ x y d : ℝ, dist (2 * x + d) (2 * y + d) = 2 * dist x y := by
    intro x y d
    rw [Real.dist_eq, Real.dist_eq, show 2 * x + d - (2 * y + d) = 2 * (x - y) by ring, abs_mul,
      abs_two]
  refine cc_lipschitzOnWith_glue (m := 1 / 2) ?_ ?_ (by norm_num) (by norm_num)
  · refine LipschitzOnWith.of_dist_le_mul fun x hx y hy => ?_
    rw [cc_join_eqOn_left γ₁ γ₂ hx, cc_join_eqOn_left γ₁ γ₂ hy]
    have := h1.dist_le_mul (2 * x + 0) ⟨by linarith [hx.1], by linarith [hx.2]⟩ (2 * y + 0)
      ⟨by linarith [hy.1], by linarith [hy.2]⟩
    rw [hd] at this
    push_cast
    nlinarith [dist_nonneg (x := x) (y := y)]
  · refine LipschitzOnWith.of_dist_le_mul fun x hx y hy => ?_
    rw [cc_join_eqOn_right h hx, cc_join_eqOn_right h hy]
    have := h2.dist_le_mul (2 * x + -1) ⟨by linarith [hx.1], by linarith [hx.2]⟩ (2 * y + -1)
      ⟨by linarith [hy.1], by linarith [hy.2]⟩
    rw [hd] at this
    push_cast
    nlinarith [dist_nonneg (x := x) (y := y)]

/-- **The concatenation is Lipschitz causal.** -/
theorem cc_join_lipCausal {γ₁ γ₂ : ℝ → V} (h1 : S.LipCausal γ₁) (h2 : S.LipCausal γ₂)
    (h : γ₁ 1 = γ₂ 0) : S.LipCausal (joinCurve γ₁ γ₂) := by
  obtain ⟨⟨L₁, hL₁⟩, hM₁, hc₁⟩ := h1
  obtain ⟨⟨L₂, hL₂⟩, hM₂, hc₂⟩ := h2
  refine ⟨⟨_, cc_join_lipschitz hL₁ hL₂ h⟩, cc_join_mapsTo hM₁ hM₂, ?_⟩
  have hl : S.ConeCondOn (joinCurve γ₁ γ₂) 0 (1 / 2) :=
    S.cc_coneCondOn_congr (cc_join_eqOn_left γ₁ γ₂).symm
      (S.cc_coneCondOn_affine hc₁ two_pos (by norm_num) (by norm_num))
  have hr : S.ConeCondOn (joinCurve γ₁ γ₂) (1 / 2) 1 :=
    S.cc_coneCondOn_congr (cc_join_eqOn_right h).symm
      (S.cc_coneCondOn_affine hc₂ two_pos (by norm_num) (by norm_num))
  exact S.cc_coneCondOn_glue hl hr

/-- **Concatenation of Lipschitz causal pieces**: `LStep x y → LStep y z → LStep x z`. -/
theorem cc_lstep_trans {x y z : V} (hxy : S.LStep x y) (hyz : S.LStep y z) : S.LStep x z := by
  obtain ⟨γ₁, h1, h10, h11⟩ := hxy
  obtain ⟨γ₂, h2, h20, h21⟩ := hyz
  exact ⟨joinCurve γ₁ γ₂, S.cc_join_lipCausal h1 h2 (h11.trans h20.symm),
    (cc_join_zero γ₁ γ₂).trans h10, (cc_join_one γ₁ γ₂).trans h21⟩

/-- **Concatenation inside `K`**: `LStepIn K x y → LStepIn K y z → LStepIn K x z`. -/
theorem cc_lstepIn_trans {K : Set V} {x y z : V} (hxy : S.LStepIn K x y)
    (hyz : S.LStepIn K y z) : S.LStepIn K x z := by
  obtain ⟨γ₁, h1, hK1, h10, h11⟩ := hxy
  obtain ⟨γ₂, h2, hK2, h20, h21⟩ := hyz
  exact ⟨joinCurve γ₁ γ₂, S.cc_join_lipCausal h1 h2 (h11.trans h20.symm),
    cc_join_mapsTo hK1 hK2, (cc_join_zero γ₁ γ₂).trans h10, (cc_join_one γ₁ γ₂).trans h21⟩

omit [NormedAddCommGroup V] [NormedSpace ℝ V] in
/-- A transitive relation equals its transitive closure. -/
lemma cc_of_transGen {α : Type*} {r : α → α → Prop} (ht : ∀ a b c, r a b → r b c → r a c)
    {a b : α} (h : Relation.TransGen r a b) : r a b := by
  induction h with
  | single h => exact h
  | tail _ h ih => exact ht _ _ _ ih h

/-- **`LCau` is one piece or nothing**: `LCau x y ↔ x = y ∨ LStep x y`. -/
theorem cc_lcau_iff {x y : V} : S.LCau x y ↔ x = y ∨ S.LStep x y := by
  unfold LCau
  rw [Relation.reflTransGen_iff_eq_or_transGen]
  exact or_congr eq_comm ⟨cc_of_transGen (r := S.LStep) (fun _ _ _ h1 h2 => S.cc_lstep_trans h1 h2),
    Relation.TransGen.single⟩

/-- `LCau = ReflGen LStep`. -/
theorem cc_lcau_eq_reflGen : S.LCau = Relation.ReflGen S.LStep := by
  funext x y
  apply propext
  rw [S.cc_lcau_iff]
  constructor
  · rintro (rfl | h)
    · exact Relation.ReflGen.refl
    · exact Relation.ReflGen.single h
  · rintro (_ | h)
    · exact Or.inl rfl
    · exact Or.inr h

/-- The same inside `K`: chains of pieces in `K` are one piece in `K`, or nothing. -/
theorem cc_reflTransGen_lstepIn_iff {K : Set V} {x y : V} :
    Relation.ReflTransGen (S.LStepIn K) x y ↔ x = y ∨ S.LStepIn K x y := by
  rw [Relation.reflTransGen_iff_eq_or_transGen]
  exact or_congr eq_comm ⟨cc_of_transGen (r := S.LStepIn K)
    (fun _ _ _ h1 h2 => S.cc_lstepIn_trans h1 h2),
    Relation.TransGen.single⟩

/-- A constant curve at a point of `K ∩ M` is a causal piece in `K`. -/
lemma cc_lstepIn_refl {K : Set V} {x : V} (hxK : x ∈ K) (hxM : x ∈ S.M) : S.LStepIn K x x := by
  have hc : S.ConeCond (fun _ : ℝ => x) := by
    intro s t hs hst ht ε hε
    simp only [sub_self, smul_zero]
    exact S.cc_cone_subset_coneHull (self_subset_thickening hε ((fun _ : ℝ => x) '' Icc s t)
      (mem_image_of_mem _ ⟨le_rfl, hst.le⟩)) hxM (S.cc_zero_mem_CC x)
  have hl : S.LipCausal (fun _ : ℝ => x) := by
    unfold LipCausal
    exact ⟨⟨0, (LipschitzWith.const x).lipschitzOnWith⟩, fun _ _ => hxM, hc⟩
  exact ⟨fun _ => x, hl, fun _ _ => hxK, rfl, rfl⟩

/-- `LipCausal` only depends on the values on `[0,1]`. -/
lemma cc_lipCausal_congr {γ δ : ℝ → V} (h : EqOn γ δ (Icc 0 1)) (hγ : S.LipCausal γ) :
    S.LipCausal δ := by
  obtain ⟨⟨L, hL⟩, hM, hc⟩ := hγ
  refine ⟨⟨L, LipschitzOnWith.of_dist_le_mul fun x hx y hy => ?_⟩, fun t ht => h ht ▸ hM ht,
    S.cc_coneCondOn_congr h hc⟩
  rw [← h hx, ← h hy]; exact hL.dist_le_mul x hx y hy

/-! ## Part ②: past-inextendibility -/

/-- A **past-directed causal curve on `[0,∞)`**: on each `[n, n+1]`, the curve run backwards,
`r ↦ γ(n + 1 − r)`, is a Lipschitz future-causal curve on `[0,1]`. Consecutive pieces share their
endpoints (they are values of one function), so `γ` is continuous on `[0,∞)`. -/
def PastCausal (γ : ℝ → V) : Prop := ∀ n : ℕ, S.LipCausal (fun r => γ ((n : ℝ) + 1 - r))

/-- **Past-inextendible** (standard form): `γ(t)` has no limit in `M` as `t → ∞`. -/
def PastInextendible (γ : ℝ → V) : Prop := ¬ ∃ q ∈ S.M, Tendsto γ atTop (𝓝 q)

/-- The stronger form: `γ` eventually leaves every compact subset of `M` for good. -/
def LeavesCompacts (γ : ℝ → V) : Prop :=
  ∀ C : Set V, IsCompact C → C ⊆ S.M → ∀ᶠ t in atTop, γ t ∉ C

/-- Every point of `M` has a compact neighbourhood (a closed ball) inside `M`. -/
lemma cc_compact_nhd [FiniteDimensional ℝ V] {q : V} (hq : q ∈ S.M) :
    ∃ r > 0, closedBall q r ⊆ S.M := by
  obtain ⟨ε, hε, hball⟩ := Metric.isOpen_iff.1 S.isOpen_M q hq
  exact ⟨ε / 2, by positivity, (closedBall_subset_ball (by linarith)).trans hball⟩

/-- **Leaving every compact implies past-inextendible.** -/
theorem cc_inextendible_of_leaves [FiniteDimensional ℝ V] {γ : ℝ → V}
    (h : S.LeavesCompacts γ) : S.PastInextendible γ := by
  rintro ⟨q, hq, hlim⟩
  obtain ⟨r, hr, hsub⟩ := S.cc_compact_nhd hq
  have h1 : ∀ᶠ t in atTop, γ t ∈ closedBall q r := hlim (closedBall_mem_nhds q hr)
  have h2 := h _ (isCompact_closedBall q r) hsub
  obtain ⟨t, ht1, ht2⟩ := (h1.and h2).exists
  exact ht2 ht1

section Exhaustion

variable {K : ℕ → Set V}

omit [NormedSpace ℝ V] in
lemma cc_exhaust_mono (hKi : ∀ j, K j ⊆ interior (K (j + 1))) : Monotone K :=
  monotone_nat_of_le_succ fun j => (hKi j).trans interior_subset

/-- Every compact subset of `M` lies in one member of the exhaustion. -/
lemma cc_compact_subset_exhaust (hKi : ∀ j, K j ⊆ interior (K (j + 1)))
    (hcov : S.M ⊆ ⋃ j, K j) {C : Set V} (hC : IsCompact C) (hCM : C ⊆ S.M) :
    ∃ j, C ⊆ K j := by
  have hmono := cc_exhaust_mono hKi
  have hU : C ⊆ ⋃ j, interior (K (j + 1)) := by
    intro x hx
    obtain ⟨j, hj⟩ := mem_iUnion.1 (hcov (hCM hx))
    exact mem_iUnion.2 ⟨j, hKi j hj⟩
  obtain ⟨j, hj⟩ := hC.elim_directed_cover _ (fun _ => isOpen_interior) hU
    (Monotone.directed_le fun a b hab => interior_mono (hmono (Nat.succ_le_succ hab)))
  exact ⟨j + 1, hj.trans interior_subset⟩

/-- Points `x (j+1) ∉ interior (K (j+1))` eventually leave every compact subset of `M`. -/
lemma cc_points_leave (hKi : ∀ j, K j ⊆ interior (K (j + 1))) (hcov : S.M ⊆ ⋃ j, K j)
    {x : ℕ → V} (hx : ∀ j, x (j + 1) ∉ interior (K (j + 1))) {C : Set V} (hC : IsCompact C)
    (hCM : C ⊆ S.M) : ∀ᶠ j in atTop, x j ∉ C := by
  obtain ⟨m, hm⟩ := S.cc_compact_subset_exhaust hKi hcov hC hCM
  filter_upwards [eventually_ge_atTop (m + 1)] with j hj hxC
  obtain ⟨i, rfl⟩ : ∃ i, j = i + 1 := ⟨j - 1, by omega⟩
  exact hx i (hKi i (cc_exhaust_mono hKi (by omega : m ≤ i) (hm hxC)))

end Exhaustion

/-- **One exit step** (finite dimension). Let `C ⊆ M` be compact with `τ` positive on its cones.
Let `F n` be Lipschitz causal curves whose initial points eventually lie outside `C`, and let points
`F n (s n)` on them converge to `x ∈ int C`. Then, along a subsequence, the last exits
`F n (tₙ)` (`tₙ ≤ sₙ`) of the curves from `int C` converge to a point `x' ∈ C ∖ int C`, joined to
`x` by a causal piece inside `C` (the limit of the arcs `F n|[tₙ, sₙ] ⊆ C`, by campaign 63's
closedness `cc_lstepIn_of_limit`). The new points again lie on a subsequence of the curves. -/
theorem cc_exit_step [FiniteDimensional ℝ V] {C : Set V} (hC : IsCompact C) (hCM : C ⊆ S.M)
    (τ : V →L[ℝ] ℝ) (hτ : ∀ x ∈ C, ∀ v ∈ S.CC x, v ≠ 0 → 0 < τ v)
    {F : ℕ → ℝ → V} (hF : ∀ n, S.LipCausal (F n)) (hout : ∀ᶠ n in atTop, F n 0 ∉ C)
    {x : V} (hx : x ∈ interior C) {s : ℕ → ℝ} (hs : ∀ n, s n ∈ Icc (0:ℝ) 1)
    (hlim : Tendsto (fun n => F n (s n)) atTop (𝓝 x)) :
    ∃ x' ∈ C, x' ∉ interior C ∧ S.LStepIn C x' x ∧ ∃ ψ : ℕ → ℕ, StrictMono ψ ∧
      ∃ s' : ℕ → ℝ, (∀ n, s' n ∈ Icc (0:ℝ) 1) ∧
        Tendsto (fun n => F (ψ n) (s' n)) atTop (𝓝 x') := by
  have hev : ∀ᶠ n in atTop, F n (s n) ∈ interior C := hlim (isOpen_interior.mem_nhds hx)
  obtain ⟨N, hN⟩ := eventually_atTop.1 (hev.and hout)
  have key : ∀ n, ∃ t ∈ Icc (0:ℝ) 1, F (n + N) t ∈ C ∧ F (n + N) t ∉ interior C ∧
      S.LStepIn C (F (n + N) t) (F (n + N) (s (n + N))) := by
    intro n
    set m := n + N
    obtain ⟨hin, hout'⟩ := hN m (by omega)
    have hcont : ContinuousOn (F m) (Icc 0 1) := (hF m).1.choose_spec.continuousOn
    have hs0 := (hs m).1
    have hs1 := (hs m).2
    let B : Set ℝ := Icc 0 (s m) ∩ F m ⁻¹' (interior C)ᶜ
    have hBc : IsClosed B := (hcont.mono (Icc_subset_Icc_right hs1)).preimage_isClosed_of_isClosed
      isClosed_Icc isOpen_interior.isClosed_compl
    have hBk : IsCompact B := isCompact_Icc.of_isClosed_subset hBc inter_subset_left
    have h0B : (0:ℝ) ∈ B := ⟨⟨le_rfl, hs0⟩, fun h => hout' (interior_subset h)⟩
    obtain ⟨t, htB, htmax⟩ := hBk.exists_isGreatest ⟨0, h0B⟩
    have ht0 : 0 ≤ t := htB.1.1
    have hts : t ≤ s m := htB.1.2
    have htlt : t < s m := by
      rcases hts.lt_or_eq with h | h
      · exact h
      · exact absurd (h ▸ hin) htB.2
    have hafter : ∀ r ∈ Ioc t (s m), F m r ∈ interior C := by
      intro r hr
      by_contra hrC
      have := htmax ⟨⟨by linarith [hr.1], hr.2⟩, hrC⟩
      linarith [hr.1]
    have htC : F m t ∈ C := by
      have hcw : ContinuousWithinAt (F m) (Ioc t (s m)) t :=
        (hcont t ⟨ht0, hts.trans hs1⟩).mono fun r hr => ⟨by linarith [hr.1], hr.2.trans hs1⟩
      have h1 := hcw.mem_closure_image (by rw [closure_Ioc htlt.ne]; exact ⟨le_rfl, hts⟩)
      have h2 : F m '' Ioc t (s m) ⊆ C := by
        rintro _ ⟨r, hr, rfl⟩; exact interior_subset (hafter r hr)
      exact closure_minimal h2 hC.isClosed h1
    refine ⟨t, ⟨ht0, hts.trans hs1⟩, htC, htB.2, ?_⟩
    refine ⟨fun r => F m (t + r * (s m - t)), S.cc_restrict (hF m) ht0 htlt hs1, ?_, by simp,
      by simp⟩
    intro r hr
    have hr' : t + r * (s m - t) ∈ Icc t (s m) := ⟨by nlinarith [hr.1], by nlinarith [hr.2]⟩
    rcases hr'.1.lt_or_eq with h | h
    · exact interior_subset (hafter _ ⟨h, hr'.2⟩)
    · show F m (t + r * (s m - t)) ∈ C
      rw [← h]; exact htC
  choose t ht htC hnint hstep using key
  obtain ⟨x', hx'C, ψ, hψ, hlim'⟩ := hC.tendsto_subseq htC
  have hx'int : x' ∉ interior C :=
    isOpen_interior.isClosed_compl.mem_of_tendsto hlim' (Eventually.of_forall fun n => hnint (ψ n))
  have hQ : Tendsto (fun n => F (ψ n + N) (s (ψ n + N))) atTop (𝓝 x) :=
    hlim.comp ((tendsto_add_atTop_nat N).comp hψ.tendsto_atTop)
  refine ⟨x', hx'C, hx'int, S.cc_lstepIn_of_limit hC hCM τ hτ hlim' hQ fun n => hstep (ψ n),
    fun n => ψ n + N, fun a b hab => by simp only; exact Nat.add_lt_add_right (hψ hab) N,
    fun n => t (ψ n), fun n => ht (ψ n), hlim'⟩

/-- **The past chain** (finite dimension). Let `K₀ ⊆ K₁ ⊆ ⋯` be a compact exhaustion of `M`
(`Kⱼ ⊆ int Kⱼ₊₁`, `⋃ Kⱼ ⊇ M`), with a time functional `τⱼ` positive on the cones over each `Kⱼ`.
Let `F n` be Lipschitz causal curves whose final points `F n 1` converge to `p ∈ K₀` and whose
initial points `F n 0` eventually leave each `Kⱼ`. Then there are points `x₀ = p, x₁, x₂, …` with
`xⱼ ∈ Kⱼ`, `xⱼ₊₁ ∉ int Kⱼ₊₁`, each `xⱼ₊₁` joined to `xⱼ` by a causal piece inside `Kⱼ₊₁`.
The construction applies `cc_exit_step` recursively, refining the subsequence at each stage. -/
theorem cc_past_chain [FiniteDimensional ℝ V] {K : ℕ → Set V} (hKc : ∀ j, IsCompact (K j))
    (hKM : ∀ j, K j ⊆ S.M) (hKi : ∀ j, K j ⊆ interior (K (j + 1)))
    (hτ : ∀ j, ∃ τ : V →L[ℝ] ℝ, ∀ x ∈ K j, ∀ v ∈ S.CC x, v ≠ 0 → 0 < τ v)
    {F : ℕ → ℝ → V} (hF : ∀ n, S.LipCausal (F n)) {p : V} (hp : p ∈ K 0)
    (hP : Tendsto (fun n => F n 1) atTop (𝓝 p)) (hout : ∀ j, ∀ᶠ n in atTop, F n 0 ∉ K j) :
    ∃ x : ℕ → V, x 0 = p ∧ (∀ j, x j ∈ K j) ∧ (∀ j, x (j + 1) ∉ interior (K (j + 1))) ∧
      ∀ j, S.LStepIn (K (j + 1)) (x (j + 1)) (x j) := by
  let Good : ℕ → V × (ℕ → ℕ) × (ℕ → ℝ) → Prop := fun j st =>
    st.1 ∈ K j ∧ StrictMono st.2.1 ∧ (∀ n, st.2.2 n ∈ Icc (0:ℝ) 1) ∧
      Tendsto (fun n => F (st.2.1 n) (st.2.2 n)) atTop (𝓝 st.1)
  have step : ∀ j st, ∃ st' : V × (ℕ → ℕ) × (ℕ → ℝ), Good j st →
      Good (j + 1) st' ∧ st'.1 ∉ interior (K (j + 1)) ∧ S.LStepIn (K (j + 1)) st'.1 st.1 := by
    intro j st
    by_cases hg : Good j st
    · obtain ⟨hxK, hφ, hs, hlim⟩ := hg
      obtain ⟨τ, hτj⟩ := hτ (j + 1)
      obtain ⟨x', hx'C, hx'int, hst, ψ, hψ, s', hs', hlim'⟩ :=
        S.cc_exit_step (F := fun n => F (st.2.1 n)) (hKc (j + 1)) (hKM (j + 1)) τ hτj
          (fun n => hF _) (hφ.tendsto_atTop.eventually (hout (j + 1))) (hKi j hxK) hs hlim
      exact ⟨(x', st.2.1 ∘ ψ, s'), fun _ => ⟨⟨hx'C, hφ.comp hψ, hs', hlim'⟩, hx'int, hst⟩⟩
    · exact ⟨st, fun h => absurd h hg⟩
  choose nxt hnxt using step
  let seq : ℕ → V × (ℕ → ℕ) × (ℕ → ℝ) := fun j =>
    Nat.rec (p, id, fun _ => 1) (fun j st => nxt j st) j
  have hseq : ∀ j, seq (j + 1) = nxt j (seq j) := fun _ => rfl
  have hgood : ∀ j, Good j (seq j) := by
    intro j
    induction j with
    | zero => exact ⟨hp, strictMono_id, fun _ => ⟨zero_le_one, le_rfl⟩, hP⟩
    | succ j ih => rw [hseq]; exact (hnxt j _ ih).1
  refine ⟨fun j => (seq j).1, rfl, fun j => (hgood j).1, fun j => ?_, fun j => ?_⟩
  · show (seq (j + 1)).1 ∉ _
    rw [hseq]; exact (hnxt j _ (hgood j)).2.1
  · show S.LStepIn _ (seq (j + 1)).1 (seq j).1
    rw [hseq]; exact (hnxt j _ (hgood j)).2.2

/-- The curve on `[0,∞)` obtained by running the pieces `c j` (from `x (j+1)` to `x j`) backwards,
`c j` on `[j, j+1]`. -/
noncomputable def chainCurve (c : ℕ → ℝ → V) : ℝ → V :=
  fun t => c ⌊t⌋₊ ((⌊t⌋₊ : ℝ) + 1 - t)

omit [NormedSpace ℝ V] in
lemma cc_chainCurve_nat {c : ℕ → ℝ → V} (n : ℕ) : chainCurve c n = c n 1 := by
  simp [chainCurve]

omit [NormedSpace ℝ V] in
lemma cc_chainCurve_eqOn {c : ℕ → ℝ → V} (hc : ∀ j, c j 0 = c (j + 1) 1) (n : ℕ) :
    EqOn (fun r => chainCurve c ((n : ℝ) + 1 - r)) (c n) (Icc 0 1) := by
  intro r hr
  simp only [chainCurve]
  rcases hr.1.lt_or_eq with h | h
  · have hf : ⌊(n : ℝ) + 1 - r⌋₊ = n :=
      (Nat.floor_eq_iff (by linarith [hr.2])).2 ⟨by linarith [hr.2], by linarith⟩
    rw [hf]; congr 1; ring
  · subst h
    have hf : ⌊(n : ℝ) + 1 - 0⌋₊ = n + 1 :=
      (Nat.floor_eq_iff (by linarith [(Nat.cast_nonneg n : (0:ℝ) ≤ n)])).2 ⟨by push_cast; linarith, by push_cast; linarith⟩
    rw [hf, hc n]; congr 1; push_cast; ring

/-- **Past-inextendible causal curve from a chain.** If the points `x j` eventually leave every
compact subset of `M`, the pieces `c j : x (j+1) → x j` concatenate to a past-directed causal curve
on `[0,∞)` from `x 0` with no limit in `M`. -/
theorem cc_chainCurve_inextendible [FiniteDimensional ℝ V] {c : ℕ → ℝ → V}
    (hc : ∀ j, S.LipCausal (c j)) (hjn : ∀ j, c j 0 = c (j + 1) 1)
    (hleave : ∀ C : Set V, IsCompact C → C ⊆ S.M → ∀ᶠ j in atTop, c j 1 ∉ C) :
    chainCurve c 0 = c 0 1 ∧ S.PastCausal (chainCurve c) ∧ S.PastInextendible (chainCurve c) := by
  refine ⟨by simpa using cc_chainCurve_nat (c := c) 0, fun n =>
    S.cc_lipCausal_congr (cc_chainCurve_eqOn hjn n).symm (hc n), ?_⟩
  rintro ⟨q, hq, hlim⟩
  obtain ⟨r, hr, hsub⟩ := S.cc_compact_nhd hq
  have h1 : ∀ᶠ j : ℕ in atTop, chainCurve c j ∈ closedBall q r :=
    (hlim.comp tendsto_natCast_atTop_atTop) (closedBall_mem_nhds q hr)
  have h2 := hleave _ (isCompact_closedBall q r) hsub
  obtain ⟨j, hj1, hj2⟩ := (h1.and h2).exists
  rw [cc_chainCurve_nat] at hj1
  exact hj2 hj1

/-- **Limit curve: a past-inextendible causal curve through `p`** (finite dimension).
Hypotheses:
* a compact exhaustion `Kⱼ` of `M` (`Kⱼ ⊆ M`, `Kⱼ ⊆ int Kⱼ₊₁`, `⋃ Kⱼ ⊇ M`) with `p ∈ K₀`;
* on each `Kⱼ`, a continuous linear `τⱼ` strictly positive on the nonzero closed cones;
* Lipschitz causal curves `F n` from `F n 0` to `F n 1`, with `F n 1 → p` and the initial points
  eventually outside each `Kⱼ`.

Then there is a past-directed causal curve `γ` on `[0,∞)` with `γ 0 = p`, past-inextendible
(`γ t` has no limit in `M`), whose `j`-th unit piece lies in `Kⱼ₊₁` and is a limit of arcs of the
`F n`. No non-imprisonment hypothesis is needed for this (standard, no-endpoint) form. -/
theorem cc_past_inextendible_limit [FiniteDimensional ℝ V] {K : ℕ → Set V}
    (hKc : ∀ j, IsCompact (K j)) (hKM : ∀ j, K j ⊆ S.M) (hKi : ∀ j, K j ⊆ interior (K (j + 1)))
    (hcov : S.M ⊆ ⋃ j, K j)
    (hτ : ∀ j, ∃ τ : V →L[ℝ] ℝ, ∀ x ∈ K j, ∀ v ∈ S.CC x, v ≠ 0 → 0 < τ v)
    {F : ℕ → ℝ → V} (hF : ∀ n, S.LipCausal (F n)) {p : V} (hp : p ∈ K 0)
    (hP : Tendsto (fun n => F n 1) atTop (𝓝 p)) (hout : ∀ j, ∀ᶠ n in atTop, F n 0 ∉ K j) :
    ∃ γ : ℝ → V, γ 0 = p ∧ S.PastCausal γ ∧ S.PastInextendible γ ∧
      (∀ n : ℕ, MapsTo (fun r => γ ((n : ℝ) + 1 - r)) (Icc 0 1) (K (n + 1))) ∧
      ∀ n : ℕ, n ≠ 0 → γ n ∉ interior (K n) := by
  obtain ⟨x, hx0, -, hxint, hstep⟩ := S.cc_past_chain hKc hKM hKi hτ hF hp hP hout
  choose c hc hcK hc0 hc1 using hstep
  have hjn : ∀ j, c j 0 = c (j + 1) 1 := fun j => (hc0 j).trans (hc1 (j + 1)).symm
  have hleave : ∀ C : Set V, IsCompact C → C ⊆ S.M → ∀ᶠ j in atTop, c j 1 ∉ C := by
    intro C hC hCM
    simpa only [hc1] using S.cc_points_leave hKi hcov hxint hC hCM
  obtain ⟨h0, hpc, hinext⟩ := S.cc_chainCurve_inextendible hc hjn hleave
  refine ⟨chainCurve c, h0.trans ((hc1 0).trans hx0), hpc, hinext, fun n r hr => ?_,
    fun n hn => ?_⟩
  · rw [cc_chainCurve_eqOn hjn n hr]; exact hcK n hr
  · obtain ⟨i, rfl⟩ : ∃ i, n = i + 1 := ⟨n - 1, by omega⟩
    rw [cc_chainCurve_nat, hc1]; exact hxint i

/-- **With non-imprisonment.** If moreover no past-inextendible past-directed causal curve is
partially imprisoned in a compact subset of `M` (stated as the hypothesis `hni`), the limit curve
leaves every compact subset of `M`. The hypothesis is used exactly as stated, so this is a direct
consequence. -/
theorem cc_past_inextendible_limit_leaves [FiniteDimensional ℝ V] {K : ℕ → Set V}
    (hKc : ∀ j, IsCompact (K j)) (hKM : ∀ j, K j ⊆ S.M) (hKi : ∀ j, K j ⊆ interior (K (j + 1)))
    (hcov : S.M ⊆ ⋃ j, K j)
    (hτ : ∀ j, ∃ τ : V →L[ℝ] ℝ, ∀ x ∈ K j, ∀ v ∈ S.CC x, v ≠ 0 → 0 < τ v)
    (hni : ∀ γ : ℝ → V, S.PastCausal γ → S.PastInextendible γ → S.LeavesCompacts γ)
    {F : ℕ → ℝ → V} (hF : ∀ n, S.LipCausal (F n)) {p : V} (hp : p ∈ K 0)
    (hP : Tendsto (fun n => F n 1) atTop (𝓝 p)) (hout : ∀ j, ∀ᶠ n in atTop, F n 0 ∉ K j) :
    ∃ γ : ℝ → V, γ 0 = p ∧ S.PastCausal γ ∧ S.PastInextendible γ ∧ S.LeavesCompacts γ := by
  obtain ⟨γ, h0, hpc, hin, -⟩ :=
    S.cc_past_inextendible_limit hKc hKM hKi hcov hτ hF hp hP hout
  exact ⟨γ, h0, hpc, hin, hni γ hpc hin⟩

/-- **A compact exhaustion of `M` exists** (finite dimension): `M` is open in a finite-dimensional
space, hence locally compact and σ-compact; take Mathlib's `CompactExhaustion` of the subtype. -/
theorem cc_exists_exhaustion [FiniteDimensional ℝ V] :
    ∃ K : ℕ → Set V, (∀ j, IsCompact (K j)) ∧ (∀ j, K j ⊆ S.M) ∧
      (∀ j, K j ⊆ interior (K (j + 1))) ∧ S.M ⊆ ⋃ j, K j := by
  have : LocallyCompactSpace S.M := S.isOpen_M.locallyCompactSpace
  let E := CompactExhaustion.choice S.M
  refine ⟨fun j => Subtype.val '' E j, fun j => (E.isCompact j).image continuous_subtype_val,
    fun j => by rintro _ ⟨y, -, rfl⟩; exact y.2, fun j => ?_, fun x hx => ?_⟩
  · have hO : IsOpen (Subtype.val '' interior (E (j + 1))) :=
      S.isOpen_M.isOpenMap_subtype_val _ isOpen_interior
    refine (image_mono (E.subset_interior_succ j)).trans (interior_maximal ?_ hO)
    exact image_mono interior_subset
  · have : (⟨x, hx⟩ : S.M) ∈ ⋃ j, E j := by rw [E.iUnion_eq]; trivial
    obtain ⟨j, hj⟩ := mem_iUnion.1 this
    exact mem_iUnion.2 ⟨j, ⟨_, hj, rfl⟩⟩

/-- **Past-inextendible limit curve from `LCau` data** (finite dimension; uses ① and ②). Let
`Kⱼ` be a compact exhaustion of `M` with a time functional `τⱼ` positive on the cones over each
`Kⱼ`. Let `Qₙ ≤ Pₙ` in the Lipschitz causal relation (`LCau`, finite chains of pieces), with
`Pₙ → p ∈ M` and `Qₙ` eventually outside every compact subset of `M`. Then there is a
past-inextendible past-directed causal curve on `[0,∞)` starting at `p`. Concatenation turns each
chain `Qₙ → Pₙ` into a single piece. -/
theorem cc_past_inextendible_of_lcau [FiniteDimensional ℝ V] {K : ℕ → Set V}
    (hKc : ∀ j, IsCompact (K j)) (hKM : ∀ j, K j ⊆ S.M) (hKi : ∀ j, K j ⊆ interior (K (j + 1)))
    (hcov : S.M ⊆ ⋃ j, K j)
    (hτ : ∀ j, ∃ τ : V →L[ℝ] ℝ, ∀ x ∈ K j, ∀ v ∈ S.CC x, v ≠ 0 → 0 < τ v)
    {P Q : ℕ → V} (hPQ : ∀ n, S.LCau (Q n) (P n)) {p : V} (hp : p ∈ S.M)
    (hP : Tendsto P atTop (𝓝 p))
    (hout : ∀ C : Set V, IsCompact C → C ⊆ S.M → ∀ᶠ n in atTop, Q n ∉ C) :
    ∃ γ : ℝ → V, γ 0 = p ∧ S.PastCausal γ ∧ S.PastInextendible γ := by
  have hmono := cc_exhaust_mono hKi
  obtain ⟨j₀, hj₀⟩ := mem_iUnion.1 (hcov hp)
  -- eventually `Qₙ ≠ Pₙ`, so the chain is one piece
  have hne : ∀ᶠ n in atTop, Q n ≠ P n := by
    filter_upwards [hP (isOpen_interior.mem_nhds (hKi j₀ hj₀)),
      hout _ (hKc (j₀ + 1)) (hKM (j₀ + 1))] with n h1 h2 h3
    exact h2 (h3 ▸ interior_subset h1)
  obtain ⟨N, hN⟩ := eventually_atTop.1 hne
  have hstep : ∀ n, S.LStep (Q (n + N)) (P (n + N)) := fun n =>
    ((S.cc_lcau_iff).1 (hPQ (n + N))).resolve_left (hN _ (by omega))
  choose F hF hF0 hF1 using hstep
  have hP' : Tendsto (fun n => F n 1) atTop (𝓝 p) := by
    simp only [hF1]; exact hP.comp (tendsto_add_atTop_nat N)
  have hout' : ∀ j, ∀ᶠ n in atTop, F n 0 ∉ K (j₀ + j) := by
    intro j
    simp only [hF0]
    exact (tendsto_add_atTop_nat N).eventually (hout _ (hKc _) (hKM _))
  obtain ⟨γ, h0, hpc, hin, -⟩ := S.cc_past_inextendible_limit (K := fun j => K (j₀ + j))
    (fun j => hKc _) (fun j => hKM _) (fun j => hKi _)
    (fun x hx => by
      obtain ⟨j, hj⟩ := mem_iUnion.1 (hcov hx)
      exact mem_iUnion.2 ⟨j, hmono (by omega) hj⟩)
    (fun j => hτ _) hF (by simpa using hj₀) hP' hout'
  exact ⟨γ, h0, hpc, hin⟩

/-! ## Part ③ (stretch): the approximants of the ∂J⁻ generator -/

/-- The Lipschitz causal future `J⁺_Lip(U)`. -/
def JfutL (U : Set V) : Set V := {x | ∃ u ∈ U, S.LCau u x}

/-- **The approximants, derived** (uses ①). Let `p ∈ closure J⁻_Lip(A)`, `p ∉ closure A`, and
suppose the causal diamond `J⁻_Lip(A) ∩ J⁺_Lip(U)` lies in `K` for a neighbourhood `U` of `p`
(the compactness hypothesis). Then there are `Pₙ → p` and `Qₙ ∈ A`, each `Pₙ` joined to `Qₙ` by a
**single** Lipschitz causal piece inside `K`: concatenation (`cc_lcau_iff`) makes the `LCau` chain
one piece, and every point of that piece is in `J⁻_Lip(A) ∩ J⁺_Lip(U)`. -/
theorem cc_approximants {A U K : Set V} {p : V} (hp : p ∈ closure (S.JpastL A))
    (hpA : p ∉ closure A) (hU : U ∈ 𝓝 p) (hK : S.JpastL A ∩ S.JfutL U ⊆ K) :
    ∃ P Q : ℕ → V, Tendsto P atTop (𝓝 p) ∧ (∀ n, Q n ∈ A) ∧ ∀ n, S.LStepIn K (P n) (Q n) := by
  obtain ⟨P', hP'J, hP'lim⟩ := mem_closure_iff_seq_limit.1 hp
  have hev : ∀ᶠ n in atTop, P' n ∈ U ∧ P' n ∉ closure A :=
    (hP'lim.eventually_mem hU).and
      (hP'lim.eventually_mem (isClosed_closure.isOpen_compl.mem_nhds hpA))
  obtain ⟨N, hN⟩ := eventually_atTop.1 hev
  have key : ∀ n, ∃ q ∈ A, S.LStepIn K (P' (n + N)) q := by
    intro n
    obtain ⟨hU', hA'⟩ := hN (n + N) (by omega)
    obtain ⟨q, hq, hlc⟩ := hP'J (n + N)
    rcases (S.cc_lcau_iff).1 hlc with h | ⟨γ, hγ, h0, h1⟩
    · exact absurd (h ▸ subset_closure hq) hA'
    refine ⟨q, hq, γ, hγ, fun r hr => hK ⟨⟨q, hq, ?_⟩, ⟨P' (n + N), hU', ?_⟩⟩, h0, h1⟩
    · rw [← h1]; exact S.cc_lcau_of_le hγ hr.1 hr.2 le_rfl
    · rw [← h0]; exact S.cc_lcau_of_le hγ le_rfl hr.1 hr.2
  choose Q hQA hQ using key
  exact ⟨fun n => P' (n + N), Q, hP'lim.comp (tendsto_add_atTop_nat N), hQA, hQ⟩

/-- **The ∂J⁻ generator with its approximants discharged** (stretch ③; finite dimension, locally
Lipschitz `g`). Same conclusion as `cc_boundary_generator`, but the approximating pieces are no
longer assumed: they come from `p ∈ ∂J⁻_Lip(A)` by `cc_approximants`. The hypotheses are the
compact `K ⊆ M` with `τ` positive on its cones, and the causal-diamond hypothesis
`J⁻_Lip(A) ∩ J⁺_Lip(U) ⊆ K` for some neighbourhood `U` of `p`. -/
theorem cc_boundary_generator_of_diamond [FiniteDimensional ℝ V] (hL : LocallyLipschitz S.g)
    {K : Set V} (hK : IsCompact K) (hKM : K ⊆ S.M) (τ : V →L[ℝ] ℝ)
    (hτ : ∀ x ∈ K, ∀ v ∈ S.CC x, v ≠ 0 → 0 < τ v) {A U : Set V} {p : V}
    (hp : p ∈ frontier (S.JpastL A)) (hpA : p ∉ closure A) (hU : U ∈ 𝓝 p)
    (hdiam : S.JpastL A ∩ S.JfutL U ⊆ K) :
    ∃ γ : ℝ → V, S.LipCausal γ ∧ MapsTo γ (Icc 0 1) K ∧ γ 0 = p ∧ γ 1 ∈ closure A ∧
      γ 1 ≠ p ∧ MapsTo γ (Icc 0 1) (frontier (S.JpastL A)) ∧
      ∀ u ∈ Icc (0:ℝ) 1, ∀ u' ∈ Icc (0:ℝ) 1, ¬ S.Chr (γ u) (γ u') := by
  obtain ⟨P, Q, hP, hQA, hstep⟩ := S.cc_approximants (frontier_subset_closure hp) hpA hU hdiam
  exact S.cc_boundary_generator hL hK hKM τ hτ hp hpA hP hQA hstep
end Spacetime

open Spacetime
#print axioms Spacetime.cc_limit_curve
#print axioms Spacetime.cc_arzela_ascoli
#print axioms Spacetime.cc_lstep_of_limit
#print axioms Spacetime.cc_reverse_cs
#print axioms Spacetime.cc_local_time_functional
#print axioms Spacetime.cc_coercive_K
#print axioms Spacetime.cc_chord_bound
#print axioms Spacetime.cc_tau_mono
#print axioms Spacetime.cc_reparam
#print axioms Spacetime.cc_uniform_reparam
#print axioms Spacetime.cc_uniform_pieces
#print axioms Spacetime.cc_lstepIn_of_limit
#print axioms Spacetime.cc_isClosed_lstepIn
#print axioms Spacetime.cc_isClosed_lstepIn_local
#print axioms Spacetime.cc_tilt
#print axioms Spacetime.cc_local_pushup
#print axioms Spacetime.cc_pushup_lstep
#print axioms Spacetime.cc_pushup
#print axioms Spacetime.cc_chr_lcau
#print axioms Spacetime.cc_restrict
#print axioms Spacetime.cc_boundary_limit_curve
#print axioms Spacetime.cc_local_pushup'
#print axioms Spacetime.cc_pushup_dual
#print axioms Spacetime.cc_interior_JpastL_subset
#print axioms Spacetime.cc_boundary_generator
#print axioms Spacetime.cc_chord_split
#print axioms Spacetime.cc_coneCondOn_glue
#print axioms Spacetime.cc_coneCondOn_affine
#print axioms Spacetime.cc_lipschitzOnWith_glue
#print axioms Spacetime.cc_join_lipschitz
#print axioms Spacetime.cc_join_lipCausal
#print axioms Spacetime.cc_lstep_trans
#print axioms Spacetime.cc_lstepIn_trans
#print axioms Spacetime.cc_lcau_iff
#print axioms Spacetime.cc_lcau_eq_reflGen
#print axioms Spacetime.cc_reflTransGen_lstepIn_iff
#print axioms Spacetime.cc_lstepIn_refl
#print axioms Spacetime.cc_inextendible_of_leaves
#print axioms Spacetime.cc_compact_subset_exhaust
#print axioms Spacetime.cc_points_leave
#print axioms Spacetime.cc_exit_step
#print axioms Spacetime.cc_past_chain
#print axioms Spacetime.cc_chainCurve_inextendible
#print axioms Spacetime.cc_past_inextendible_limit
#print axioms Spacetime.cc_past_inextendible_limit_leaves
#print axioms Spacetime.cc_exists_exhaustion
#print axioms Spacetime.cc_past_inextendible_of_lcau
#print axioms Spacetime.cc_approximants
#print axioms Spacetime.cc_boundary_generator_of_diamond

end ShadowProbe.CausalConcatProbe

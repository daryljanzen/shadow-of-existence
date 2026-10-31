import Mathlib

/-!
# Probe `r7643+71.2` (campaign 80, `r7643` ①): the tangency condition, frame-free

Registration: `computations/formalisation/r7643_71_campaign80/PREDICTION.md`. Nothing imports this
file, and it imports no other probe. The 2D frame bookkeeping (`ℓ = ∂_V`, `n ∝ ∂_U`,
`g = −F dU dV` symmetrised as in campaign 79's `gM`) is adapted from `probes/SliceTangency.lean`;
campaign 79's frame-component lemma `st_null_frame_bound` is re-proved here basis-free
(`tc_W_bound`), and `st_alignment_iff`'s content is subsumed by `tc_tendsto`.

## ① Frame-free — BUILT

*Setting.* `E` any real vector space (no dimension or basis needed), `g : LinearMap.BilinForm ℝ E`;
`NullFrame g ℓ n`: `g` symmetric, `g(ℓ,ℓ) = g(n,n) = 0`, `g(ℓ,n) = −1`, and `g(e,e) ≥ 0` for
`e ∈ W = {e | g(ℓ,e) = 0 ∧ g(n,e) = 0}` (positive **semi**definite: weaker than registered, so more
general). Future causal: `FutCausal g ℓ n v :⟺ g(v,v) ≤ 0 ∧ g(v, ℓ+n) < 0`; `tc_futCausal_iff`
proves this is exactly `{αℓ + βn + e | α,β ≥ 0, e ∈ W, g(e,e) ≤ 2αβ, (α,β) ≠ 0}`. `ξ : E →ₗ ℝ`
temporal: `∀ v, FutCausal g ℓ n v → 0 < ξ v`.
- `tc_pos`: `ξ(ℓ), ξ(n) > 0`. `tc_W_bound`: `ξ(e)² ≤ 2 ξ(ℓ) ξ(n) g(e,e)` for `e ∈ W`.
- **`tc_pointwise`**: `∀ w, |ξ w − ξ n·(−g ℓ w)| ≤ ξ ℓ·|g n w| + √(2 ξℓ ξn)·√(g(w_W,w_W))`,
  `w_W = projW g ℓ n w = w + g(n,w) ℓ + g(ℓ,w) n` (signs checked: `g(ℓ,w_W) = g(n,w_W) = 0`).
- **`tc_opNorm_bound`** (normed `E`, continuous `g`, `ξ`; `FrameHyp g ℓ n ξ` bundles the above):
  `‖ξ/ξ(n) + g(ℓ,·)‖ ≤ (ξℓ/ξn)‖g‖‖n‖ + √(2ξℓ/ξn)·√‖g‖·(1 + 2‖g‖‖n‖‖ℓ‖)`.
- **`tc_tendsto`** — moving frames *and* moving metrics, any filter: frame hypotheses eventually,
  `‖g_i‖, ‖g_i‖‖n_i‖, ‖ℓ_i‖ ≤ C`, `ξ_i(ℓ_i)/ξ_i(n_i) → 0` ⟹ `ξ_i/ξ_i(n_i) + g_i(ℓ_i,·) → 0` in
  operator norm. `tc_tendsto_limit`: if also `g_i(ℓ_i,·) → G₀` (e.g. `g_i → g`, `ℓ_i → ℓ`) then
  `ξ_i/ξ_i(n_i) → −G₀`. `tc_ratio_of_bounded`: `ξ_i(ℓ_i)` bounded and `ξ_i(n_i) → ∞` ⟹ ratio `→ 0`.
- **`tc_sequence`** (registered fixed-frame form): `ξ_m(ℓ) ≤ A`, `ξ_m(n) → ∞` ⟹
  `ξ_m/ξ_m(n) → −g(ℓ,·)` in operator norm and pointwise in `w`.
So the registered stretch (frames `ℓ_m → ℓ`, `n_m → n`) is BUILT, with only boundedness needed.

## ② Kruskal plane — BUILT

`P = ℝ × ℝ`, `(U,V)`, region I `regI = {U < 0 < V}`, horizon filter `𝓝[regI] (0, V₀)`, `V₀ > 0`
(`tc_L_neBot`: it is not `⊥`). `g = gF (F p) = −F(p)·(dU dV)_sym`, `ℓ = ∂_V`, `n = nF (F p) =
(2/F(p)) ∂_U`; `tc_frameHyp2`: for every `f > 0` this is a null frame (`W = 0`) and any covector with
`ξ(∂_U), ξ(∂_V) > 0` is temporal. `tc_kruskal_align` feeds this to `tc_tendsto` for any `F > 0` on
region I with `F ≤ C` near `(0,V₀)` (only an upper bound is needed: `‖g‖‖n‖` is `F`-free);
`tc_kruskal_limit`: if `F → F₀` the limit covector is `(F₀/2) dU = −g(ℓ,·)`.
- **Stationary — BUILT** (`tc_stationary`): `t = 2M log(−V/U)`, `dt(ℓ) = 2M/V`,
  `dt(n) = (2/F)·2M(−U)⁻¹`, frame hypotheses at every point of region I, `dt(ℓ) → 2M/V₀`,
  `dt(n) → ∞`, `dt/dt(n) + g(ℓ,·) → 0` in operator norm.
- **Retarded — BUILT, no hypotheses on `r_U, r_V`** (`tc_retarded`): `h(x) = (x/2M − 1)e^{x/2M}` is
  strictly increasing on `[0,∞)` (`h′ = x e^{x/2M}/4M²`), `h(0) = −1`, onto `(−1,∞)` by the IVT;
  `rinv` is its inverse, continuous by monotonicity (`continuousAt_of_monotoneOn_of_image_mem_nhds`)
  and differentiable by `HasDerivAt.of_local_left_inverse`. `r = rK = h⁻¹(−UV)`;
  `tc_rK_partials`: `r_U = −V/h′(r)`, `r_V = −U/h′(r)` (`kK = 1/h′(r) = 4M²/(r e^{r/2M})`, `kK_eq`).
  For `Θ = a(−4M log(−U) + ηr)`, `a, η > 0`: `dΘ(ℓ) = aη r_V → 0`, `dΘ(n) = (2/F)a(4M/|U| + η r_U)
  → ∞`, the frame hypotheses hold eventually near `(0,V₀)` (temporal there, not on all of region I:
  `η r_U < 0`), and `dΘ/dΘ(n) + g(ℓ,·) → 0` in operator norm. The registered reachable negative did
  not occur.
- **Actual Schwarzschild `F` — BUILT** (`tc_schwarzschild`): `FS = (32M³/r)e^{−r/2M}` with `r = rK`
  is positive on region I and tends to `16M²/e` at `(0,V₀)`, so both slicings align for the
  Kruskal-plane Schwarzschild metric, `ξ/ξ(n) → (F₀/2) dU`, `F₀ = 32M³/(2M)·e^{−1}`. (The metric
  `−F dU dV` is taken as the definition of the radial Schwarzschild plane; it is not derived from
  the `(t,r)` form.)

## ③ Non-vacuity — BUILT

- ①: `tc_minkowski_nonvacuous`: 2D Minkowski (`F = 1`, `n = 2∂_U`), `ξ_m = (m+1)dU + dV`: all frame
  hypotheses hold, `ξ_m(ℓ) = 1`, `ξ_m(n) = 2(m+1) → ∞`, `ξ_m/ξ_m(n) → ½ dU`. `tc_futCausal_iff`
  shows the cone hypothesis is the standard one.
- ②: `tc_L_neBot` (the horizon filter is proper); `tc_stationary`/`tc_retarded` *prove* the
  temporality hypotheses of ① (they are conclusions, not assumptions) for any `F > 0` bounded above,
  and `tc_schwarzschild` instantiates `F` with Schwarzschild's.

## ④ 4D — REPORTED (not built)

- The causal setting of the earlier campaigns lives in a single chart (a normed space); 4D
  Schwarzschild needs the angular `S²`, which has no global chart, so the slicings are checked
  on the radial Kruskal plane only.
- Route not taken: the spherically-symmetric lift. ① is already dimension-free: for a spherically
  symmetric `Θ` the angular directions are `g`-orthogonal to `ℓ, n` and `ξ`-null, so they sit in
  `W` (positive definite there, `r²` times the round metric) and contribute `ξ(e) = 0`; at a single
  point of a 4D chart away from the poles, `tc_pointwise`/`tc_tendsto` apply verbatim with
  `E = ℝ⁴`. What is missing is (a) the 4D metric as a `Spacetime`-style chart object with angular
  coordinates, (b) the check that `fderiv Θ` kills the angular directions and `‖g‖` stays bounded
  near the horizon in that chart, and (c) the joining of chart-local statements over `S²` (the
  manifold setting of campaigns 66/68). None of this is in the file.

`#print axioms` at the end: `[propext, Classical.choice, Quot.sound]` for every main theorem.
`set_option synthInstance.maxHeartbeats 400000` is set inside `Kruskal` (as in campaign 79).
-/
open Set Filter Topology

namespace ShadowProbe.TangencyConditionProbe

/-! ## ① Frame-free: the pointwise inequality (pure linear algebra, no basis, no dimension) -/

section FrameFree

variable {E : Type*} [AddCommGroup E] [Module ℝ E]

/-- A null frame `ℓ, n` for a symmetric bilinear `g`: `g(ℓ,ℓ) = g(n,n) = 0`, `g(ℓ,n) = −1`, and `g`
positive **semi**definite on `W = {ℓ,n}^⊥` (weaker than the registered "positive definite"). -/
structure NullFrame (g : LinearMap.BilinForm ℝ E) (ℓ n : E) : Prop where
  symm : ∀ v w, g v w = g w v
  ll : g ℓ ℓ = 0
  nn : g n n = 0
  ln : g ℓ n = -1
  posW : ∀ e, g ℓ e = 0 → g n e = 0 → 0 ≤ g e e

/-- Future causal: `g(v,v) ≤ 0` and `g(v, ℓ+n) < 0` (`ℓ + n` is future timelike, `g = −2`). Such `v`
are automatically nonzero. `tc_futCausal_iff` shows this is exactly the cone
`{αℓ + βn + e | α, β ≥ 0, e ∈ W, g(e,e) ≤ 2αβ, (α,β) ≠ 0}`. -/
def FutCausal (g : LinearMap.BilinForm ℝ E) (ℓ n v : E) : Prop := g v v ≤ 0 ∧ g v (ℓ + n) < 0

/-- The `g`-orthogonal projection onto `W`: `w_W = w + g(n,w) ℓ + g(ℓ,w) n`. -/
def projW (g : LinearMap.BilinForm ℝ E) (ℓ n w : E) : E := w + g n w • ℓ + g ℓ w • n

/-- The splitting `w = (−g(n,w)) ℓ + (−g(ℓ,w)) n + w_W`. -/
lemma decompW (g : LinearMap.BilinForm ℝ E) (ℓ n w : E) :
    w = (-g n w) • ℓ + (-g ℓ w) • n + projW g ℓ n w := by
  simp only [projW, neg_smul]; abel

variable {g : LinearMap.BilinForm ℝ E} {ℓ n : E}

namespace NullFrame
variable (hF : NullFrame g ℓ n)
include hF

lemma nl : g n ℓ = -1 := by rw [hF.symm]; exact hF.ln

lemma projW_l (w : E) : g ℓ (projW g ℓ n w) = 0 := by
  simp [projW, hF.ll, hF.ln]

lemma projW_n (w : E) : g n (projW g ℓ n w) = 0 := by
  simp [projW, hF.nn, hF.nl]


/-- `g(αℓ + βn + e, αℓ + βn + e) = −2αβ + g(e,e)` for `e ∈ W`. -/
lemma quad (α β : ℝ) {e : E} (he1 : g ℓ e = 0) (he2 : g n e = 0) :
    g (α • ℓ + β • n + e) (α • ℓ + β • n + e) = -2 * α * β + g e e := by
  have h1 : g e ℓ = 0 := by rw [hF.symm]; exact he1
  have h2 : g e n = 0 := by rw [hF.symm]; exact he2
  simp [hF.ll, hF.nn, hF.ln, hF.nl, he1, he2, h1, h2]; ring

/-- `g(αℓ + βn + e, ℓ + n) = −α − β` for `e ∈ W`. -/
lemma lin (α β : ℝ) {e : E} (he1 : g ℓ e = 0) (he2 : g n e = 0) :
    g (α • ℓ + β • n + e) (ℓ + n) = -α - β := by
  have h1 : g e ℓ = 0 := by rw [hF.symm]; exact he1
  have h2 : g e n = 0 := by rw [hF.symm]; exact he2
  simp [hF.ll, hF.nn, hF.ln, hF.nl, h1, h2]; ring

end NullFrame

/-- The future causal cone, made explicit in the splitting `ℓ, n, W`. -/
theorem tc_futCausal_iff (hF : NullFrame g ℓ n) (v : E) :
    FutCausal g ℓ n v ↔ ∃ α β : ℝ, ∃ e : E, 0 ≤ α ∧ 0 ≤ β ∧ g ℓ e = 0 ∧ g n e = 0 ∧
      g e e ≤ 2 * α * β ∧ (α ≠ 0 ∨ β ≠ 0) ∧ v = α • ℓ + β • n + e := by
  constructor
  · rintro ⟨h1, h2⟩
    have hd := decompW g ℓ n v
    set α := -g n v
    set β := -g ℓ v
    set e := projW g ℓ n v
    have he1 := hF.projW_l v
    have he2 := hF.projW_n v
    have hq := hF.quad α β he1 he2
    have hl := hF.lin α β he1 he2
    rw [← hd] at hq hl
    have hW := hF.posW e he1 he2
    have hs : 0 < α + β := by linarith
    have hab : 0 ≤ α * β := by linarith
    have hα : 0 ≤ α := by
      by_contra h; push Not at h; nlinarith
    have hβ : 0 ≤ β := by
      by_contra h; push Not at h; nlinarith
    refine ⟨α, β, e, hα, hβ, he1, he2, by linarith, ?_, hd⟩
    by_contra h; push Not at h; rw [h.1, h.2] at hs; simp at hs
  · rintro ⟨α, β, e, hα, hβ, he1, he2, hq, hne, rfl⟩
    refine ⟨by rw [hF.quad α β he1 he2]; linarith, ?_⟩
    rw [hF.lin α β he1 he2]
    rcases hne with h | h
    · have := lt_of_le_of_ne hα (Ne.symm h); linarith
    · have := lt_of_le_of_ne hβ (Ne.symm h); linarith

variable {ξ : E →ₗ[ℝ] ℝ}

/-- Temporality forces `ξ(ℓ) > 0` and `ξ(n) > 0`. -/
theorem tc_pos (hF : NullFrame g ℓ n) (hξ : ∀ v, FutCausal g ℓ n v → 0 < ξ v) :
    0 < ξ ℓ ∧ 0 < ξ n := by
  refine ⟨hξ ℓ ⟨by rw [hF.ll], ?_⟩, hξ n ⟨by rw [hF.nn], ?_⟩⟩
  · simp [hF.ll, hF.ln]
  · simp [hF.nn, hF.nl]

/-- **The basis-free form of campaign 79's `st_null_frame_bound`**: for `e ∈ W`,
`ξ(e)² ≤ 2 ξ(ℓ) ξ(n) g(e,e)`. Proof: test `ξ` on the null vector `αℓ + βn ∓ e` with
`β = |ξ e|/(2ξ(n))`, `α = g(e,e) ξ(n)/|ξ e|`. -/
theorem tc_W_bound (hF : NullFrame g ℓ n) (hξ : ∀ v, FutCausal g ℓ n v → 0 < ξ v) {e : E}
    (he1 : g ℓ e = 0) (he2 : g n e = 0) : ξ e ^ 2 ≤ 2 * ξ ℓ * ξ n * g e e := by
  obtain ⟨ha, hb⟩ := tc_pos hF hξ
  have hq := hF.posW e he1 he2
  set a := ξ ℓ
  set b := ξ n
  set q := g e e
  have key : ∀ s : ℝ, s * s = 1 → 0 < s * ξ e → (s * ξ e) ^ 2 < 2 * a * b * q := by
    intro s hs hc
    set c := s * ξ e
    have hse1 : g ℓ ((-s) • e) = 0 := by simp [he1]
    have hse2 : g n ((-s) • e) = 0 := by simp [he2]
    have hqs : g ((-s) • e) ((-s) • e) = q := by simp [q]; nlinarith
    set β := c / (2 * b)
    set α := q * b / c
    have hβ : 0 < β := by positivity
    have hα : 0 ≤ α := by positivity
    have hv : FutCausal g ℓ n (α • ℓ + β • n + (-s) • e) := by
      refine ⟨?_, ?_⟩
      · rw [hF.quad α β hse1 hse2, hqs]
        have : α * β = q / 2 := by simp only [α, β]; field_simp
        linarith
      · rw [hF.lin α β hse1 hse2]; linarith
    have hp := hξ _ hv
    simp only [map_add, map_smul, smul_eq_mul] at hp
    have : -s * ξ e = -c := by simp [c]
    rw [this] at hp
    have e1 : α * a = q * a * b / c := by simp only [α]; ring
    have e2 : β * b = c / 2 := by simp only [β]; field_simp
    rw [e1, e2] at hp
    have : c / 2 < q * a * b / c := by linarith
    rw [lt_div_iff₀ hc] at this
    nlinarith
  rcases lt_trichotomy (ξ e) 0 with h | h | h
  · have := key (-1) (by norm_num) (by linarith); nlinarith
  · rw [h]; have := mul_nonneg (mul_pos (mul_pos two_pos ha) hb).le hq; nlinarith
  · have := key 1 (by norm_num) (by linarith); nlinarith

/-- **① The pointwise, basis-free inequality.** For every `w`,
`|ξ(w) − ξ(n)·(−g(ℓ,w))| ≤ ξ(ℓ)·|g(n,w)| + √(2 ξ(ℓ) ξ(n))·√(g(w_W, w_W))`,
`w_W = w + g(n,w) ℓ + g(ℓ,w) n`. -/
theorem tc_pointwise (hF : NullFrame g ℓ n) (hξ : ∀ v, FutCausal g ℓ n v → 0 < ξ v) (w : E) :
    |ξ w - ξ n * (-g ℓ w)| ≤
      ξ ℓ * |g n w| + Real.sqrt (2 * ξ ℓ * ξ n) * Real.sqrt (g (projW g ℓ n w) (projW g ℓ n w)) := by
  obtain ⟨ha, hb⟩ := tc_pos hF hξ
  have he1 := hF.projW_l w
  have he2 := hF.projW_n w
  have hB := tc_W_bound hF hξ he1 he2
  have hxi : ξ w = (-g n w) * ξ ℓ + (-g ℓ w) * ξ n + ξ (projW g ℓ n w) := by
    conv_lhs => rw [decompW g ℓ n w]
    simp
  have habs : |ξ (projW g ℓ n w)| ≤
      Real.sqrt (2 * ξ ℓ * ξ n) * Real.sqrt (g (projW g ℓ n w) (projW g ℓ n w)) := by
    rw [← Real.sqrt_mul (by positivity)]; exact Real.abs_le_sqrt hB
  have : ξ w - ξ n * (-g ℓ w) = -(ξ ℓ * g n w) + ξ (projW g ℓ n w) := by rw [hxi]; ring
  rw [this]
  calc |-(ξ ℓ * g n w) + ξ (projW g ℓ n w)| ≤ |-(ξ ℓ * g n w)| + |ξ (projW g ℓ n w)| :=
        abs_add_le _ _
    _ ≤ _ := by rw [abs_neg, abs_mul, abs_of_pos ha]; linarith

end FrameFree

/-! ## ① The operator-norm bound and the corollary (normed setting, frames and metrics may move) -/

section Normed

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]

/-- A continuous bilinear form as a `LinearMap.BilinForm`. -/
noncomputable def bil (g : E →L[ℝ] E →L[ℝ] ℝ) : LinearMap.BilinForm ℝ E :=
  LinearMap.mk₂ ℝ (fun v w => g v w) (by simp) (by simp) (by simp) (by simp)

@[simp] lemma bil_apply (g : E →L[ℝ] E →L[ℝ] ℝ) (v w : E) : bil g v w = g v w := rfl

/-- The frame hypotheses at one point: `(ℓ, n)` is a null frame for `g` and `ξ` is positive on the
future causal cone. -/
def FrameHyp (g : E →L[ℝ] E →L[ℝ] ℝ) (ℓ n : E) (ξ : E →L[ℝ] ℝ) : Prop :=
  NullFrame (bil g) ℓ n ∧ ∀ v, FutCausal (bil g) ℓ n v → 0 < ξ v

/-- **① in operator norm.** Under the frame hypotheses,
`‖ξ/ξ(n) + g(ℓ,·)‖ ≤ (ξℓ/ξn)·‖g‖‖n‖ + √(2 ξℓ/ξn)·√‖g‖·(1 + 2‖g‖‖n‖‖ℓ‖)`. -/
theorem tc_opNorm_bound {g : E →L[ℝ] E →L[ℝ] ℝ} {ℓ n : E} {ξ : E →L[ℝ] ℝ}
    (h : FrameHyp g ℓ n ξ) :
    ‖(ξ n)⁻¹ • ξ + g ℓ‖ ≤ ξ ℓ / ξ n * (‖g‖ * ‖n‖) +
      Real.sqrt (2 * (ξ ℓ / ξ n)) * (Real.sqrt ‖g‖ * (1 + 2 * (‖g‖ * ‖n‖) * ‖ℓ‖)) := by
  obtain ⟨hF, hξ⟩ := h
  have hξ' : ∀ v, FutCausal (bil g) ℓ n v → 0 < (ξ : E →ₗ[ℝ] ℝ) v := hξ
  obtain ⟨ha, hb⟩ := tc_pos hF hξ'
  set a := ξ ℓ
  set b := ξ n
  have ha' : 0 < a := ha
  have hb' : 0 < b := hb
  have hr : 0 ≤ a / b := by positivity
  refine ContinuousLinearMap.opNorm_le_bound _ (by positivity) fun w => ?_
  have hP := tc_pointwise hF hξ' w
  simp only [bil_apply, ContinuousLinearMap.coe_coe] at hP
  set e := projW (bil g) ℓ n w
  -- the size of `w_W`
  have hgn : |g n w| ≤ ‖g‖ * ‖n‖ * ‖w‖ := by
    rw [← Real.norm_eq_abs]; exact g.le_opNorm₂ n w
  have hgl : |g ℓ w| ≤ ‖g‖ * ‖ℓ‖ * ‖w‖ := by
    rw [← Real.norm_eq_abs]; exact g.le_opNorm₂ ℓ w
  have he : ‖e‖ ≤ (1 + 2 * (‖g‖ * ‖n‖) * ‖ℓ‖) * ‖w‖ := by
    have : ‖e‖ ≤ ‖w‖ + |g n w| * ‖ℓ‖ + |g ℓ w| * ‖n‖ := by
      simp only [e, projW, bil_apply]
      refine (norm_add₃_le).trans ?_
      rw [norm_smul, norm_smul, Real.norm_eq_abs, Real.norm_eq_abs]
    have h1 := mul_le_mul_of_nonneg_right hgn (norm_nonneg ℓ)
    have h2 := mul_le_mul_of_nonneg_right hgl (norm_nonneg n)
    nlinarith [norm_nonneg w, norm_nonneg g, norm_nonneg ℓ, norm_nonneg n]
  have hq : Real.sqrt (g e e) ≤ Real.sqrt ‖g‖ * ‖e‖ := by
    have : g e e ≤ ‖g‖ * ‖e‖ ^ 2 := by
      have := g.le_opNorm₂ e e
      rw [Real.norm_eq_abs] at this
      nlinarith [le_abs_self (g e e)]
    calc Real.sqrt (g e e) ≤ Real.sqrt (‖g‖ * ‖e‖ ^ 2) := Real.sqrt_le_sqrt this
      _ = Real.sqrt ‖g‖ * ‖e‖ := by
        rw [Real.sqrt_mul (norm_nonneg g), Real.sqrt_sq (norm_nonneg e)]
  have hsq : Real.sqrt (2 * a * b) = Real.sqrt (2 * (a / b)) * b := by
    have : 2 * a * b = 2 * (a / b) * b ^ 2 := by field_simp
    rw [this, Real.sqrt_mul (by positivity), Real.sqrt_sq hb'.le]
  -- assemble
  have hval : ((b)⁻¹ • ξ + g ℓ) w = (ξ w - b * (-g ℓ w)) / b := by
    simp only [FunLike.coe_add, FunLike.coe_smul, Pi.add_apply,
      Pi.smul_apply, smul_eq_mul]
    have hbb : b⁻¹ * b = 1 := inv_mul_cancel₀ hb'.ne'
    rw [eq_div_iff hb'.ne']
    linear_combination (ξ w) * hbb
  rw [hval, Real.norm_eq_abs, abs_div, abs_of_pos hb', div_le_iff₀ hb']
  rw [hsq] at hP
  have hs0 : 0 ≤ Real.sqrt (2 * (a / b)) := Real.sqrt_nonneg _
  have hsg : 0 ≤ Real.sqrt ‖g‖ := Real.sqrt_nonneg _
  have hab : a = a / b * b := by field_simp
  calc |ξ w - b * -g ℓ w| ≤ a * |g n w| + Real.sqrt (2 * (a / b)) * b * Real.sqrt (g e e) := hP
    _ ≤ a / b * b * (‖g‖ * ‖n‖ * ‖w‖) +
        Real.sqrt (2 * (a / b)) * b * (Real.sqrt ‖g‖ * ((1 + 2 * (‖g‖ * ‖n‖) * ‖ℓ‖) * ‖w‖)) := by
      rw [← hab]
      gcongr
      exact hq.trans (mul_le_mul_of_nonneg_left he hsg)
    _ = _ := by ring

/-- `a` eventually positive and bounded above, `b → ∞` ⟹ `a/b → 0`. -/
theorem tc_ratio_of_bounded {ι : Type*} {L : Filter ι} {a b : ι → ℝ} {A : ℝ}
    (ha : ∀ᶠ i in L, 0 < a i) (hA : ∀ᶠ i in L, a i ≤ A) (hb : Tendsto b L atTop) :
    Tendsto (fun i => a i / b i) L (𝓝 0) := by
  have hAb : Tendsto (fun i => A / b i) L (𝓝 0) := tendsto_const_nhds.div_atTop hb
  refine tendsto_of_tendsto_of_tendsto_of_le_of_le' tendsto_const_nhds hAb ?_ ?_
  · filter_upwards [ha, hb.eventually_gt_atTop 0] with i h1 h2; positivity
  · filter_upwards [hA, hb.eventually_gt_atTop 0] with i h1 h2
    exact div_le_div_of_nonneg_right h1 h2.le

/-- **① The corollary, moving frames and moving metrics, in operator norm.** Along any filter, if
the frame hypotheses hold eventually, `‖g_i‖`, `‖g_i‖‖n_i‖` and `‖ℓ_i‖` stay bounded, and
`ξ_i(ℓ_i)/ξ_i(n_i) → 0`, then `ξ_i/ξ_i(n_i) + g_i(ℓ_i,·) → 0` in operator norm. -/
theorem tc_tendsto {ι : Type*} {L : Filter ι} {g : ι → E →L[ℝ] E →L[ℝ] ℝ} {ℓ n : ι → E}
    {ξ : ι → E →L[ℝ] ℝ} {C : ℝ} (hF : ∀ᶠ i in L, FrameHyp (g i) (ℓ i) (n i) (ξ i))
    (hg : ∀ᶠ i in L, ‖g i‖ ≤ C) (hgn : ∀ᶠ i in L, ‖g i‖ * ‖n i‖ ≤ C)
    (hl : ∀ᶠ i in L, ‖ℓ i‖ ≤ C)
    (hr : Tendsto (fun i => ξ i (ℓ i) / ξ i (n i)) L (𝓝 0)) :
    Tendsto (fun i => (ξ i (n i))⁻¹ • ξ i + g i (ℓ i)) L (𝓝 0) := by
  set K := Real.sqrt C * (1 + 2 * C * C)
  have hlim : Tendsto (fun i => ξ i (ℓ i) / ξ i (n i) * C +
      Real.sqrt (2 * (ξ i (ℓ i) / ξ i (n i))) * K) L (𝓝 0) := by
    have h1 := hr.mul_const C
    have h2 := ((Real.continuous_sqrt.tendsto _).comp (hr.const_mul 2)).mul_const K
    simpa using h1.add h2
  refine squeeze_zero_norm' ?_ hlim
  filter_upwards [hF, hg, hgn, hl] with i hFi hgi hgni hli
  refine (tc_opNorm_bound hFi).trans ?_
  have hξ' : ∀ v, FutCausal (bil (g i)) (ℓ i) (n i) v → 0 < ((ξ i) : E →ₗ[ℝ] ℝ) v := hFi.2
  obtain ⟨ha, hb⟩ := tc_pos hFi.1 hξ'
  have ha' : 0 < ξ i (ℓ i) := ha
  have hb' : 0 < ξ i (n i) := hb
  have hr0 : 0 ≤ ξ i (ℓ i) / ξ i (n i) := by positivity
  have hC : 0 ≤ C := (norm_nonneg (g i)).trans hgi
  have h1 : Real.sqrt ‖g i‖ ≤ Real.sqrt C := Real.sqrt_le_sqrt hgi
  have h2 : 1 + 2 * (‖g i‖ * ‖n i‖) * ‖ℓ i‖ ≤ 1 + 2 * C * C := by
    nlinarith [mul_le_mul hgni hli (norm_nonneg _) hC]
  have hK : Real.sqrt ‖g i‖ * (1 + 2 * (‖g i‖ * ‖n i‖) * ‖ℓ i‖) ≤ K :=
    mul_le_mul h1 h2 (by positivity) (Real.sqrt_nonneg _)
  exact add_le_add (mul_le_mul_of_nonneg_left hgni hr0)
    (mul_le_mul_of_nonneg_left hK (Real.sqrt_nonneg _))

/-- The limit form: if moreover `g_i(ℓ_i,·) → G₀`, then `ξ_i/ξ_i(n_i) → −G₀` in operator norm. -/
theorem tc_tendsto_limit {ι : Type*} {L : Filter ι} {g : ι → E →L[ℝ] E →L[ℝ] ℝ} {ℓ n : ι → E}
    {ξ : ι → E →L[ℝ] ℝ} {C : ℝ} {G₀ : E →L[ℝ] ℝ}
    (hF : ∀ᶠ i in L, FrameHyp (g i) (ℓ i) (n i) (ξ i))
    (hg : ∀ᶠ i in L, ‖g i‖ ≤ C) (hgn : ∀ᶠ i in L, ‖g i‖ * ‖n i‖ ≤ C)
    (hl : ∀ᶠ i in L, ‖ℓ i‖ ≤ C)
    (hr : Tendsto (fun i => ξ i (ℓ i) / ξ i (n i)) L (𝓝 0))
    (hG : Tendsto (fun i => g i (ℓ i)) L (𝓝 G₀)) :
    Tendsto (fun i => (ξ i (n i))⁻¹ • ξ i) L (𝓝 (-G₀)) := by
  have := (tc_tendsto hF hg hgn hl hr).sub hG
  simpa using this

/-- **① The sequence corollary, fixed frame** (the registered form with `ℓ_m = ℓ`, `n_m = n`):
`ξ_m(ℓ) ≤ A` and `ξ_m(n) → ∞` ⟹ `ξ_m/ξ_m(n) → −g(ℓ,·)` in operator norm, hence pointwise. -/
theorem tc_sequence {g : E →L[ℝ] E →L[ℝ] ℝ} {ℓ n : E} {ξ : ℕ → E →L[ℝ] ℝ} {A : ℝ}
    (hF : ∀ m, FrameHyp g ℓ n (ξ m)) (hA : ∀ m, ξ m ℓ ≤ A)
    (hb : Tendsto (fun m => ξ m n) atTop atTop) :
    Tendsto (fun m => (ξ m n)⁻¹ • ξ m) atTop (𝓝 (-g ℓ)) ∧
      ∀ w, Tendsto (fun m => ξ m w / ξ m n) atTop (𝓝 (-g ℓ w)) := by
  have hpos : ∀ m, 0 < ξ m ℓ := fun m => by
    have hξ' : ∀ v, FutCausal (bil g) ℓ n v → 0 < ((ξ m) : E →ₗ[ℝ] ℝ) v := (hF m).2
    exact (tc_pos (hF m).1 hξ').1
  have hr := tc_ratio_of_bounded (Eventually.of_forall hpos) (Eventually.of_forall hA) hb
  have hop := tc_tendsto_limit (C := max ‖g‖ (max (‖g‖ * ‖n‖) ‖ℓ‖)) (G₀ := g ℓ)
    (Eventually.of_forall hF) (Eventually.of_forall fun _ => le_max_left _ _)
    (Eventually.of_forall fun _ => (le_max_left _ _).trans (le_max_right _ _))
    (Eventually.of_forall fun _ => (le_max_right _ _).trans (le_max_right _ _)) hr
    tendsto_const_nhds
  refine ⟨hop, fun w => ?_⟩
  have := ((ContinuousLinearMap.apply ℝ ℝ w).continuous.tendsto _).comp hop
  simpa [Function.comp_def, div_eq_inv_mul] using this

end Normed

/-! ## ② The Kruskal plane -/

namespace Kruskal
open ContinuousLinearMap

set_option synthInstance.maxHeartbeats 400000

/-- Kruskal coordinates `p = (U, V)`. -/
abbrev P := ℝ × ℝ

/-- `dU dV`, symmetrised (times 2): `S(v,w) = v_U w_V + v_V w_U`. -/
noncomputable def S : P →L[ℝ] P →L[ℝ] ℝ :=
  (fst ℝ ℝ ℝ).smulRight (snd ℝ ℝ ℝ) + (snd ℝ ℝ ℝ).smulRight (fst ℝ ℝ ℝ)

/-- `g = −f dU dV` (symmetrised) at a point where the conformal factor is `f`. -/
noncomputable def gF (f : ℝ) : P →L[ℝ] P →L[ℝ] ℝ := (-(f / 2)) • S

lemma gF_apply (f : ℝ) (v w : P) : gF f v w = -f * (v.1 * w.2 + v.2 * w.1) / 2 := by
  simp [gF, S]; ring

/-- `ℓ = ∂_V`. -/
def ℓ : P := (0, 1)
/-- `∂_U`. -/
def e1 : P := (1, 0)
/-- `n = (2/f) ∂_U`. -/
noncomputable def nF (f : ℝ) : P := (2 / f) • e1

lemma gF_ℓ (f : ℝ) (w : P) : gF f ℓ w = -f * w.1 / 2 := by
  rw [gF_apply]; simp [ℓ]

/-- **The frame hypotheses in the 2D model, for every conformal factor `f > 0`.** `(ℓ, n)` is a null
frame for `−f dU dV` (`W = 0`), and a covector with `ξ(∂_U) > 0`, `ξ(∂_V) > 0` is positive on the
future causal cone. -/
theorem tc_frameHyp2 {f : ℝ} (hf : 0 < f) {ξ : P →L[ℝ] ℝ} (h1 : 0 < ξ e1) (h2 : 0 < ξ ℓ) :
    FrameHyp (gF f) ℓ (nF f) ξ := by
  have hf' := hf.ne'
  refine ⟨⟨fun v w => ?_, ?_, ?_, ?_, fun e he1 he2 => ?_⟩, fun v hv => ?_⟩
  · simp only [bil_apply, gF_apply]; ring
  · simp [gF_apply, ℓ]
  · simp [gF_apply, nF, e1]
  · simp [gF_apply, nF, e1, ℓ]; field_simp
  · simp only [bil_apply, gF_apply, ℓ, nF, e1] at he1 he2 ⊢
    simp at he1 he2
    have h1 : e.1 = 0 := by
      rcases he1 with h | h
      · exact absurd h hf'
      · exact h
    rw [h1]; simp
  · obtain ⟨hv1, hv2⟩ := hv
    simp only [bil_apply, gF_apply, ℓ, nF, e1] at hv1 hv2
    simp at hv2
    have hs : 0 < f * v.1 + 2 * v.2 := by
      have : f * v.1 + 2 * v.2 = -2 * (-f * (v.1 * 1 + v.2 * (2 / f)) / 2) := by
        field_simp
      nlinarith
    have hp : 0 ≤ v.1 * v.2 := by nlinarith
    have hv : v = v.1 • e1 + v.2 • ℓ := by ext <;> simp [e1, ℓ]
    rw [hv, map_add, map_smul, map_smul, smul_eq_mul, smul_eq_mul]
    have hv1' : 0 ≤ v.1 := by
      by_contra h; push Not at h
      have : v.2 ≤ 0 := by nlinarith
      nlinarith
    have hv2' : 0 ≤ v.2 := by
      by_contra h; push Not at h
      have : v.1 ≤ 0 := by nlinarith
      nlinarith
    rcases hv1'.eq_or_lt with h0 | h0
    · rw [← h0] at hs ⊢
      have : 0 < v.2 := by linarith
      simp only [zero_mul, zero_add]; positivity
    · have := mul_pos h0 h1
      nlinarith [mul_nonneg hv2' h2.le]

/-! ### Region I and the horizon filter -/

/-- Region I: `U < 0 < V`. -/
def regI : Set P := {p | p.1 < 0 ∧ 0 < p.2}

lemma regI_eq : regI = Iio 0 ×ˢ Ioi 0 := rfl

lemma regI_open : IsOpen regI := by rw [regI_eq]; exact isOpen_Iio.prod isOpen_Ioi

lemma L_eq {V₀ : ℝ} (hV : 0 < V₀) :
    𝓝[regI] ((0 : ℝ), V₀) = 𝓝[<] (0 : ℝ) ×ˢ 𝓝 V₀ := by
  rw [regI_eq, nhdsWithin_prod_eq, isOpen_Ioi.nhdsWithin_eq hV]

/-- **Non-vacuity of the horizon filter**: `(0, V₀)` is approached from inside region I. -/
theorem tc_L_neBot {V₀ : ℝ} (hV : 0 < V₀) : (𝓝[regI] ((0 : ℝ), V₀)).NeBot := by
  rw [L_eq hV]; infer_instance

lemma L_mem {V₀ : ℝ} : ∀ᶠ p in 𝓝[regI] ((0 : ℝ), V₀), p ∈ regI := self_mem_nhdsWithin

lemma L_fst {V₀ : ℝ} (hV : 0 < V₀) :
    Tendsto (fun p : P => p.1) (𝓝[regI] ((0 : ℝ), V₀)) (𝓝[<] 0) := by
  rw [L_eq hV]; exact tendsto_fst

lemma L_snd {V₀ : ℝ} (hV : 0 < V₀) :
    Tendsto (fun p : P => p.2) (𝓝[regI] ((0 : ℝ), V₀)) (𝓝 V₀) := by
  rw [L_eq hV]; exact tendsto_snd

lemma L_nhds {V₀ : ℝ} : 𝓝[regI] ((0 : ℝ), V₀) ≤ 𝓝 ((0 : ℝ), V₀) := nhdsWithin_le_nhds

lemma L_invU {V₀ : ℝ} (hV : 0 < V₀) :
    Tendsto (fun p : P => (-p.1)⁻¹) (𝓝[regI] ((0 : ℝ), V₀)) atTop := by
  refine tendsto_inv_nhdsGT_zero.comp ?_
  have h := L_fst hV
  refine tendsto_nhdsWithin_iff.2 ⟨?_, ?_⟩
  · have := (continuous_neg.tendsto (0:ℝ)).comp (tendsto_nhdsWithin_iff.1 h).1
    simpa [Function.comp_def] using this
  · filter_upwards [(tendsto_nhdsWithin_iff.1 h).2] with p hp
    exact neg_pos.2 (show p.1 < 0 from hp)

lemma L_UV {V₀ : ℝ} : Tendsto (fun p : P => -(p.1 * p.2)) (𝓝[regI] ((0 : ℝ), V₀)) (𝓝 0) := by
  have : Continuous fun p : P => -(p.1 * p.2) := by fun_prop
  have h := (this.tendsto ((0:ℝ), V₀)).mono_left L_nhds
  simpa using h

lemma norm_gF_le {f : ℝ} (hf : 0 ≤ f) : ‖gF f‖ ≤ f / 2 * ‖S‖ := by
  refine ContinuousLinearMap.opNorm_le_bound _ (by positivity) fun v => ?_
  have h : gF f v = (-(f / 2)) • S v := rfl
  rw [h, norm_smul, Real.norm_eq_abs, abs_neg, abs_of_nonneg (by positivity), mul_assoc]
  exact mul_le_mul_of_nonneg_left (S.le_opNorm v) (by positivity)

/-- **② The alignment step in the Kruskal plane, for any conformal factor.** If `F > 0` on region I
and `F ≤ C` near `(0, V₀)`, and the covector field `ξ` has `ξ(∂_U), ξ(∂_V) > 0` near `(0,V₀)` and
`ξ(ℓ)/ξ(n) → 0` there, then `ξ/ξ(n) + g(ℓ,·) → 0` in operator norm (by ①). -/
theorem tc_kruskal_align {V₀ : ℝ} {F : P → ℝ} (hF : ∀ p ∈ regI, 0 < F p) {C : ℝ}
    (hC : ∀ᶠ p in 𝓝[regI] ((0 : ℝ), V₀), F p ≤ C) {ξ : P → P →L[ℝ] ℝ}
    (hpos : ∀ᶠ p in 𝓝[regI] ((0 : ℝ), V₀), 0 < ξ p e1 ∧ 0 < ξ p ℓ)
    (hr : Tendsto (fun p => ξ p ℓ / ξ p (nF (F p))) (𝓝[regI] ((0 : ℝ), V₀)) (𝓝 0)) :
    Tendsto (fun p => (ξ p (nF (F p)))⁻¹ • ξ p + gF (F p) ℓ) (𝓝[regI] ((0 : ℝ), V₀)) (𝓝 0) := by
  have hFL : ∀ᶠ p in 𝓝[regI] ((0 : ℝ), V₀), 0 < F p := by
    filter_upwards [L_mem] with p hp using hF p hp
  refine tc_tendsto (C := max (C / 2 * ‖S‖) (max (‖S‖ * ‖e1‖) ‖ℓ‖)) ?_ ?_ ?_ ?_ hr
  · filter_upwards [hFL, hpos] with p hp h
    exact tc_frameHyp2 hp h.1 h.2
  · filter_upwards [hFL, hC] with p hp hc
    refine le_trans ?_ (le_max_left _ _)
    refine (norm_gF_le hp.le).trans ?_
    gcongr
  · filter_upwards [hFL] with p hp
    refine le_trans ?_ ((le_max_left _ _).trans (le_max_right _ _))
    have hn : ‖nF (F p)‖ = 2 / F p * ‖e1‖ := by
      rw [nF, norm_smul, Real.norm_eq_abs, abs_of_pos (by positivity)]
    calc ‖gF (F p)‖ * ‖nF (F p)‖ ≤ F p / 2 * ‖S‖ * (2 / F p * ‖e1‖) := by
          rw [hn]; gcongr; exact norm_gF_le hp.le
      _ = ‖S‖ * ‖e1‖ := by field_simp
  · exact Eventually.of_forall fun _ => (le_max_right _ _).trans (le_max_right _ _)

/-- The limit covector, when the conformal factor converges: `−g(ℓ,·) → (F₀/2) dU`. -/
theorem tc_kruskal_limit {V₀ : ℝ} {F : P → ℝ} {F₀ : ℝ}
    (hF₀ : Tendsto F (𝓝[regI] ((0 : ℝ), V₀)) (𝓝 F₀)) {ξ : P → P →L[ℝ] ℝ}
    (h : Tendsto (fun p => (ξ p (nF (F p)))⁻¹ • ξ p + gF (F p) ℓ) (𝓝[regI] ((0 : ℝ), V₀))
      (𝓝 0)) :
    Tendsto (fun p => (ξ p (nF (F p)))⁻¹ • ξ p) (𝓝[regI] ((0 : ℝ), V₀))
      (𝓝 ((F₀ / 2) • fst ℝ ℝ ℝ)) := by
  have hG : Tendsto (fun p => gF (F p) ℓ) (𝓝[regI] ((0 : ℝ), V₀)) (𝓝 (gF F₀ ℓ)) := by
    have : Tendsto (fun p => (-(F p / 2)) • S ℓ) (𝓝[regI] ((0 : ℝ), V₀))
        (𝓝 ((-(F₀ / 2)) • S ℓ)) := ((hF₀.div_const 2).neg).smul_const _
    simpa [gF] using this
  have e : -gF F₀ ℓ = (F₀ / 2) • fst ℝ ℝ ℝ := by
    ext <;> simp [gF_ℓ]
    ring
  rw [← e]; simpa using h.sub hG

/-! ### The stationary slicing `t = 2M log(−V/U)` -/

/-- Schwarzschild time in region I. -/
noncomputable def tK (M : ℝ) (p : P) : ℝ := 2 * M * Real.log (-p.2 / p.1)

lemma tK_hasFDerivAt (M : ℝ) {p : P} (hp : p ∈ regI) :
    HasFDerivAt (tK M) ((-2 * M / p.1) • fst ℝ ℝ ℝ + (2 * M / p.2) • snd ℝ ℝ ℝ) p := by
  obtain ⟨h1, h2⟩ := hp
  have hev : (fun q : P => 2 * M * (Real.log q.2 - Real.log (-q.1))) =ᶠ[𝓝 p] tK M := by
    filter_upwards [regI_open.mem_nhds ⟨h1, h2⟩] with q ⟨hq1, hq2⟩
    simp only [tK]
    rw [show -q.2 / q.1 = q.2 / (-q.1) by ring, Real.log_div hq2.ne' (by linarith)]
  refine HasFDerivAt.congr_of_eventuallyEq ?_ hev.symm
  have hd := ((hasFDerivAt_snd (p := p)).log h2.ne').sub
    (((hasFDerivAt_fst (p := p)).neg).log (by simp; linarith))
  refine (hd.const_mul (2 * M)).congr_fderiv ?_
  ext <;> simp <;> field_simp

lemma tK_fderiv (M : ℝ) {p : P} (hp : p ∈ regI) :
    fderiv ℝ (tK M) p ℓ = 2 * M / p.2 ∧ fderiv ℝ (tK M) p e1 = 2 * M * (-p.1)⁻¹ := by
  rw [(tK_hasFDerivAt M hp).fderiv]
  have : p.1 ≠ 0 := hp.1.ne
  constructor
  · simp [ℓ]
  · simp [e1]; field_simp

/-- `ξ(n) = (2/F) ξ(∂_U)`. -/
lemma apply_nF (ξ : P →L[ℝ] ℝ) (f : ℝ) : ξ (nF f) = 2 / f * ξ e1 := by
  simp [nF]

/-- **② The stationary slicing aligns** (`BUILT`, any conformal factor `F > 0` bounded near the
horizon point). In region I, `dt(ℓ) = 2M/V`, `dt(n) = (2/F)·2M/|U|`; the frame hypotheses hold at
every point of region I; `dt(ℓ) → 2M/V₀` (bounded), `dt(n) → ∞`, and
`dt/dt(n) + g(ℓ,·) → 0` in operator norm as `p → (0,V₀)` within region I. -/
theorem tc_stationary {M : ℝ} (hM : 0 < M) {V₀ : ℝ} (hV : 0 < V₀) {F : P → ℝ}
    (hF : ∀ p ∈ regI, 0 < F p) {C : ℝ} (hC : ∀ᶠ p in 𝓝[regI] ((0 : ℝ), V₀), F p ≤ C) :
    (∀ p ∈ regI, fderiv ℝ (tK M) p ℓ = 2 * M / p.2 ∧
      fderiv ℝ (tK M) p (nF (F p)) = 2 / F p * (2 * M * (-p.1)⁻¹)) ∧
    (∀ p ∈ regI, FrameHyp (gF (F p)) ℓ (nF (F p)) (fderiv ℝ (tK M) p)) ∧
    Tendsto (fun p => fderiv ℝ (tK M) p ℓ) (𝓝[regI] ((0 : ℝ), V₀)) (𝓝 (2 * M / V₀)) ∧
    Tendsto (fun p => fderiv ℝ (tK M) p (nF (F p))) (𝓝[regI] ((0 : ℝ), V₀)) atTop ∧
    Tendsto (fun p => (fderiv ℝ (tK M) p (nF (F p)))⁻¹ • fderiv ℝ (tK M) p + gF (F p) ℓ)
      (𝓝[regI] ((0 : ℝ), V₀)) (𝓝 0) := by
  have hval : ∀ p ∈ regI, fderiv ℝ (tK M) p ℓ = 2 * M / p.2 ∧
      fderiv ℝ (tK M) p (nF (F p)) = 2 / F p * (2 * M * (-p.1)⁻¹) := fun p hp => by
    rw [apply_nF, (tK_fderiv M hp).2]; exact ⟨(tK_fderiv M hp).1, rfl⟩
  have hposI : ∀ p ∈ regI, 0 < fderiv ℝ (tK M) p e1 ∧ 0 < fderiv ℝ (tK M) p ℓ := fun p hp => by
    rw [(tK_fderiv M hp).1, (tK_fderiv M hp).2]
    have := hp.1; have := hp.2
    exact ⟨by have : 0 < -p.1 := by linarith
              positivity, by positivity⟩
  have hl : Tendsto (fun p => fderiv ℝ (tK M) p ℓ) (𝓝[regI] ((0 : ℝ), V₀)) (𝓝 (2 * M / V₀)) := by
    have h : Tendsto (fun p : P => 2 * M / p.2) (𝓝[regI] ((0 : ℝ), V₀)) (𝓝 (2 * M / V₀)) :=
      tendsto_const_nhds.div (L_snd hV) hV.ne'
    refine h.congr' ?_
    filter_upwards [L_mem] with p hp using (hval p hp).1.symm
  have hFL : ∀ᶠ p in 𝓝[regI] ((0 : ℝ), V₀), 0 < F p := by
    filter_upwards [L_mem] with p hp using hF p hp
  have hCpos : 0 < C := by
    have := tc_L_neBot hV
    obtain ⟨p, hp1, hp2⟩ := (hFL.and hC).exists
    linarith
  have hn : Tendsto (fun p => fderiv ℝ (tK M) p (nF (F p))) (𝓝[regI] ((0 : ℝ), V₀)) atTop := by
    have h0 : Tendsto (fun p : P => 2 / C * (2 * M) * (-p.1)⁻¹) (𝓝[regI] ((0 : ℝ), V₀)) atTop :=
      (L_invU hV).const_mul_atTop (by positivity)
    refine tendsto_atTop_mono' _ ?_ h0
    filter_upwards [L_mem, hFL, hC] with p hp hFp hCp
    rw [(hval p hp).2]
    have hu : 0 < (-p.1)⁻¹ := inv_pos.2 (by linarith [hp.1])
    have : 2 / C ≤ 2 / F p := div_le_div_of_nonneg_left (by norm_num) hFp hCp
    have h2M : 0 < 2 * M * (-p.1)⁻¹ := by positivity
    nlinarith
  refine ⟨hval, fun p hp => tc_frameHyp2 (hF p hp) (hposI p hp).1 (hposI p hp).2, hl, hn, ?_⟩
  refine tc_kruskal_align hF hC (by filter_upwards [L_mem] with p hp using hposI p hp) ?_
  refine tc_ratio_of_bounded (A := 2 * M / V₀ + 1) ?_ ?_ hn
  · filter_upwards [L_mem] with p hp using (hposI p hp).2
  · exact (hl.eventually (gt_mem_nhds (lt_add_one _))).mono fun _ h => h.le


/-! ### The areal radius `r(U,V)`: inverse of `h(x) = (x/2M − 1) e^{x/2M}` -/

/-- `h(x) = (x/(2M) − 1) e^{x/(2M)}`; `r` solves `h(r) = −UV`. -/
noncomputable def hK (M x : ℝ) : ℝ := (x / (2 * M) - 1) * Real.exp (x / (2 * M))

/-- `h′(x) = x/(4M²) e^{x/(2M)}`. -/
noncomputable def hK' (M x : ℝ) : ℝ := x / (4 * M ^ 2) * Real.exp (x / (2 * M))

section Radius
variable {M : ℝ} (hM : 0 < M)
include hM

lemma hasDerivAt_hK (x : ℝ) : HasDerivAt (hK M) (hK' M x) x := by
  have h1 : HasDerivAt (fun x : ℝ => x / (2 * M)) (1 / (2 * M)) x :=
    (hasDerivAt_id x).div_const _
  have h := (h1.sub_const 1).mul h1.exp
  refine h.congr_deriv ?_
  simp only [hK']; field_simp; ring

omit hM in
lemma continuous_hK : Continuous (hK M) := by
  unfold hK; fun_prop

lemma hK_strictMonoOn : StrictMonoOn (hK M) (Ici 0) := by
  refine strictMonoOn_of_deriv_pos (convex_Ici 0) continuous_hK.continuousOn fun x hx => ?_
  rw [interior_Ici] at hx
  rw [(hasDerivAt_hK hM x).deriv]
  have : 0 < x := hx
  unfold hK'; positivity

omit hM in
lemma hK_zero : hK M 0 = -1 := by simp [hK]

lemma hK_two : hK M (2 * M) = 0 := by
  simp only [hK]; rw [div_self (by positivity)]; simp

lemma hK_gt {x : ℝ} (hx : 0 < x) : -1 < hK M x := by
  rw [← hK_zero]
  exact hK_strictMonoOn hM (mem_Ici.2 le_rfl) hx.le hx

lemma hK_exists {y : ℝ} (hy : -1 < y) : ∃ x, 0 < x ∧ hK M x = y := by
  set b := 2 * M * (|y| + 2)
  have hb : 0 ≤ b := by positivity
  have hyb : y ≤ hK M b := by
    have h1 : 0 ≤ b / (2 * M) - 1 := by
      rw [show b / (2 * M) = |y| + 2 by simp only [b]; field_simp]
      linarith [abs_nonneg y]
    have h2 : b / (2 * M) - 1 ≤ hK M b :=
      le_mul_of_one_le_right h1 (Real.one_le_exp (by positivity))
    have h3 : b / (2 * M) - 1 = |y| + 1 := by simp only [b]; field_simp; ring
    linarith [le_abs_self y]
  obtain ⟨x, hx, hxy⟩ := intermediate_value_Icc hb continuous_hK.continuousOn
    ⟨by rw [hK_zero]; exact hy.le, hyb⟩
  refine ⟨x, ?_, hxy⟩
  rcases hx.1.eq_or_lt with h | h
  · rw [← h, hK_zero] at hxy; linarith
  · exact h

end Radius

open Classical in
/-- The inverse of `h` on `(−1, ∞) → (0, ∞)` (junk value `0` elsewhere). -/
noncomputable def rinv (M y : ℝ) : ℝ :=
  if h : ∃ x, 0 < x ∧ hK M x = y then h.choose else 0

section Radius2
variable {M : ℝ} (hM : 0 < M)
include hM

lemma rinv_spec {y : ℝ} (hy : -1 < y) : 0 < rinv M y ∧ hK M (rinv M y) = y := by
  have h := hK_exists hM hy
  simp only [rinv, h, ↓reduceDIte]
  exact h.choose_spec

lemma rinv_hK {x : ℝ} (hx : 0 < x) : rinv M (hK M x) = x := by
  obtain ⟨h1, h2⟩ := rinv_spec hM (hK_gt hM hx)
  exact (hK_strictMonoOn hM).injOn (mem_Ici.2 h1.le) (mem_Ici.2 hx.le) h2

lemma rinv_zero : rinv M 0 = 2 * M := by
  rw [← hK_two hM, rinv_hK hM (by positivity)]

lemma rinv_strictMonoOn : StrictMonoOn (rinv M) (Ioi (-1)) := by
  intro y₁ hy₁ y₂ hy₂ hlt
  obtain ⟨a1, b1⟩ := rinv_spec hM hy₁
  obtain ⟨a2, b2⟩ := rinv_spec hM hy₂
  by_contra h; push Not at h
  have := (hK_strictMonoOn hM).monotoneOn (mem_Ici.2 a2.le) (mem_Ici.2 a1.le) h
  rw [b1, b2] at this; linarith

lemma rinv_continuousAt {a : ℝ} (ha : -1 < a) : ContinuousAt (rinv M) a := by
  refine continuousAt_of_monotoneOn_of_image_mem_nhds (rinv_strictMonoOn hM).monotoneOn
    (Ioi_mem_nhds ha) ?_
  refine mem_of_superset (Ioi_mem_nhds (rinv_spec hM ha).1) fun x hx => ?_
  exact ⟨hK M x, hK_gt hM hx, rinv_hK hM hx⟩

/-- **The derivative of the inverse** (inverse function theorem in one variable). -/
lemma rinv_hasDerivAt {a : ℝ} (ha : -1 < a) :
    HasDerivAt (rinv M) (hK' M (rinv M a))⁻¹ a := by
  refine HasDerivAt.of_local_left_inverse (rinv_continuousAt hM ha) (hasDerivAt_hK hM _) ?_ ?_
  · have := (rinv_spec hM ha).1; unfold hK'; positivity
  · filter_upwards [Ioi_mem_nhds ha] with y hy using (rinv_spec hM hy).2

end Radius2

/-- The areal radius in Kruskal coordinates: `r(U,V) = h⁻¹(−UV)`. -/
noncomputable def rK (M : ℝ) (p : P) : ℝ := rinv M (-(p.1 * p.2))

/-- `1/h′(r)`: the factor in `r_U = −V/h′(r)`, `r_V = −U/h′(r)`. -/
noncomputable def kK (M : ℝ) (p : P) : ℝ := (hK' M (rK M p))⁻¹

/-- The retarded slicing `Θ = a(u + ηr)`, `u = −4M log(−U)`. -/
noncomputable def ΘK (M a η : ℝ) (p : P) : ℝ := a * (-4 * M * Real.log (-p.1) + η * rK M p)

section Retarded
variable {M : ℝ} (hM : 0 < M)
include hM

omit hM in
lemma regI_UV {p : P} (hp : p ∈ regI) : -1 < -(p.1 * p.2) := by
  have := mul_neg_of_neg_of_pos hp.1 hp.2; linarith

lemma rK_spec {p : P} (hp : p ∈ regI) : 0 < rK M p ∧ hK M (rK M p) = -(p.1 * p.2) :=
  rinv_spec hM (regI_UV hp)

lemma kK_eq {p : P} (hp : p ∈ regI) :
    kK M p = 4 * M ^ 2 / (rK M p * Real.exp (rK M p / (2 * M))) := by
  have := (rK_spec hM hp).1
  simp only [kK, hK']; field_simp

lemma kK_pos {p : P} (hp : p ∈ regI) : 0 < kK M p := by
  rw [kK_eq hM hp]; have := (rK_spec hM hp).1; positivity

lemma rK_hasFDerivAt {p : P} (hp : p ∈ regI) :
    HasFDerivAt (rK M) ((kK M p) • (-((p.1 • snd ℝ ℝ ℝ) + p.2 • fst ℝ ℝ ℝ))) p := by
  have hin : HasFDerivAt (fun q : P => -(q.1 * q.2)) (-((p.1 • snd ℝ ℝ ℝ) + p.2 • fst ℝ ℝ ℝ)) p :=
    ((hasFDerivAt_fst (p := p)).mul (hasFDerivAt_snd (p := p))).neg
  exact (rinv_hasDerivAt hM (regI_UV hp)).comp_hasFDerivAt p hin

/-- **The implicit derivatives** `r_U = −V/h′(r)`, `r_V = −U/h′(r)` (`BUILT`). -/
theorem tc_rK_partials {p : P} (hp : p ∈ regI) :
    fderiv ℝ (rK M) p e1 = kK M p * (-p.2) ∧ fderiv ℝ (rK M) p ℓ = kK M p * (-p.1) := by
  rw [(rK_hasFDerivAt hM hp).fderiv]
  constructor <;> simp [e1, ℓ]

lemma ΘK_hasFDerivAt (a η : ℝ) {p : P} (hp : p ∈ regI) :
    HasFDerivAt (ΘK M a η) (a • ((-4 * M) • ((-p.1)⁻¹ • (-fst ℝ ℝ ℝ)) +
      η • ((kK M p) • (-((p.1 • snd ℝ ℝ ℝ) + p.2 • fst ℝ ℝ ℝ))))) p := by
  have hu := (((hasFDerivAt_fst (p := p)).neg).log (by simp; linarith [hp.1])).const_mul (-4 * M)
  exact (hu.add ((rK_hasFDerivAt hM hp).const_mul η)).const_mul a

lemma ΘK_fderiv (a η : ℝ) {p : P} (hp : p ∈ regI) :
    fderiv ℝ (ΘK M a η) p ℓ = a * (η * (kK M p * (-p.1))) ∧
    fderiv ℝ (ΘK M a η) p e1 = a * (4 * M * (-p.1)⁻¹ + η * (kK M p * (-p.2))) := by
  rw [(ΘK_hasFDerivAt hM a η hp).fderiv]
  constructor
  · simp [ℓ]
  · simp [e1]; ring

/-- `r → 2M` and `1/h′(r) → 1/h′(2M)` at the horizon point. -/
lemma rK_tendsto {V₀ : ℝ} :
    Tendsto (rK M) (𝓝[regI] ((0 : ℝ), V₀)) (𝓝 (2 * M)) := by
  have h := (rinv_continuousAt hM (a := 0) (by norm_num)).tendsto.comp (L_UV (V₀ := V₀))
  rw [rinv_zero hM] at h; exact h

lemma kK_tendsto {V₀ : ℝ} :
    Tendsto (kK M) (𝓝[regI] ((0 : ℝ), V₀)) (𝓝 (hK' M (2 * M))⁻¹) := by
  have hc : Continuous (hK' M) := by unfold hK'; fun_prop
  have hne : hK' M (2 * M) ≠ 0 := by unfold hK'; positivity
  exact ((hc.tendsto _).comp (rK_tendsto hM)).inv₀ hne

/-- **② The retarded slicing aligns** (`BUILT`, any conformal factor `F > 0` bounded near the
horizon point, `a, η > 0`). `r` is the genuine inverse of `h` (no hypotheses on `r_U, r_V`):
`dΘ(ℓ) = aη r_V → 0` (bounded), `dΘ(n) = (2/F)·a(4M/|U| + η r_U) → ∞`; the frame hypotheses hold
near `(0, V₀)` in region I; and `dΘ/dΘ(n) + g(ℓ,·) → 0` in operator norm. -/
theorem tc_retarded {a η : ℝ} (ha : 0 < a) (hη : 0 < η) {V₀ : ℝ} (hV : 0 < V₀)
    {F : P → ℝ} (hF : ∀ p ∈ regI, 0 < F p) {C : ℝ}
    (hC : ∀ᶠ p in 𝓝[regI] ((0 : ℝ), V₀), F p ≤ C) :
    (∀ p ∈ regI, 0 < rK M p ∧ hK M (rK M p) = -(p.1 * p.2)) ∧
    (∀ p ∈ regI, fderiv ℝ (rK M) p e1 = kK M p * (-p.2) ∧
      fderiv ℝ (rK M) p ℓ = kK M p * (-p.1)) ∧
    (∀ p ∈ regI, fderiv ℝ (ΘK M a η) p ℓ = a * (η * fderiv ℝ (rK M) p ℓ) ∧
      fderiv ℝ (ΘK M a η) p (nF (F p)) =
        2 / F p * (a * (4 * M * (-p.1)⁻¹ + η * fderiv ℝ (rK M) p e1))) ∧
    Tendsto (fun p => fderiv ℝ (ΘK M a η) p ℓ) (𝓝[regI] ((0 : ℝ), V₀)) (𝓝 0) ∧
    Tendsto (fun p => fderiv ℝ (ΘK M a η) p (nF (F p))) (𝓝[regI] ((0 : ℝ), V₀)) atTop ∧
    (∀ᶠ p in 𝓝[regI] ((0 : ℝ), V₀),
      FrameHyp (gF (F p)) ℓ (nF (F p)) (fderiv ℝ (ΘK M a η) p)) ∧
    Tendsto (fun p => (fderiv ℝ (ΘK M a η) p (nF (F p)))⁻¹ • fderiv ℝ (ΘK M a η) p +
      gF (F p) ℓ) (𝓝[regI] ((0 : ℝ), V₀)) (𝓝 0) := by
  set L := 𝓝[regI] ((0 : ℝ), V₀)
  have hval : ∀ p ∈ regI, fderiv ℝ (ΘK M a η) p ℓ = a * (η * fderiv ℝ (rK M) p ℓ) ∧
      fderiv ℝ (ΘK M a η) p (nF (F p)) =
        2 / F p * (a * (4 * M * (-p.1)⁻¹ + η * fderiv ℝ (rK M) p e1)) := fun p hp => by
    rw [apply_nF, (ΘK_fderiv hM a η hp).1, (ΘK_fderiv hM a η hp).2,
      (tc_rK_partials hM hp).1, (tc_rK_partials hM hp).2]
    exact ⟨rfl, rfl⟩
  have hk := kK_tendsto hM (V₀ := V₀)
  have hU : Tendsto (fun p : P => -p.1) L (𝓝 0) := by
    have := ((continuous_neg.tendsto (0:ℝ)).comp (tendsto_nhdsWithin_iff.1 (L_fst hV)).1)
    simpa [Function.comp_def] using this
  have hl : Tendsto (fun p => fderiv ℝ (ΘK M a η) p ℓ) L (𝓝 0) := by
    have h : Tendsto (fun p => a * (η * (kK M p * (-p.1)))) L (𝓝 0) := by
      simpa using ((hk.mul hU).const_mul η).const_mul a
    refine h.congr' ?_
    filter_upwards [L_mem] with p hp using (ΘK_fderiv hM a η hp).1.symm
  have he1 : Tendsto (fun p => fderiv ℝ (ΘK M a η) p e1) L atTop := by
    have hb : Tendsto (fun p : P => η * (kK M p * (-p.2))) L (𝓝 (η * ((hK' M (2 * M))⁻¹ * -V₀))) :=
      (hk.mul (L_snd hV).neg).const_mul η
    have h : Tendsto (fun p : P => a * (4 * M * (-p.1)⁻¹ + η * (kK M p * (-p.2)))) L atTop :=
      Tendsto.const_mul_atTop ha
        (((L_invU hV).const_mul_atTop (by positivity)).atTop_add hb)
    refine h.congr' ?_
    filter_upwards [L_mem] with p hp using (ΘK_fderiv hM a η hp).2.symm
  have hFL : ∀ᶠ p in L, 0 < F p := by
    filter_upwards [L_mem] with p hp using hF p hp
  have hCpos : 0 < C := by
    have := tc_L_neBot hV
    obtain ⟨p, hp1, hp2⟩ := (hFL.and hC).exists
    linarith
  have hpos : ∀ᶠ p in L, 0 < fderiv ℝ (ΘK M a η) p e1 ∧ 0 < fderiv ℝ (ΘK M a η) p ℓ := by
    filter_upwards [L_mem, he1.eventually_gt_atTop 0] with p hp h1
    refine ⟨h1, ?_⟩
    rw [(ΘK_fderiv hM a η hp).1]
    have := kK_pos hM hp; have : 0 < -p.1 := by linarith [hp.1]
    positivity
  have hn : Tendsto (fun p => fderiv ℝ (ΘK M a η) p (nF (F p))) L atTop := by
    refine tendsto_atTop_mono' _ ?_ (he1.const_mul_atTop (show 0 < 2 / C by positivity))
    filter_upwards [hFL, hC, hpos] with p hFp hCp hp
    rw [apply_nF]
    have : 2 / C ≤ 2 / F p := div_le_div_of_nonneg_left (by norm_num) hFp hCp
    nlinarith [hp.1]
  refine ⟨fun p hp => rK_spec hM hp, fun p hp => tc_rK_partials hM hp, hval, hl, hn, ?_, ?_⟩
  · filter_upwards [L_mem, hpos] with p hp h using tc_frameHyp2 (hF p hp) h.1 h.2
  · refine tc_kruskal_align hF hC hpos ?_
    refine tc_ratio_of_bounded (A := 1) (hpos.mono fun _ h => h.2) ?_ hn
    exact (hl.eventually (gt_mem_nhds one_pos)).mono fun _ h => h.le

/-! ### The actual Schwarzschild conformal factor -/

/-- `F = (32M³/r) e^{−r/2M}`, with `r = rK`. -/
noncomputable def FS (M : ℝ) (p : P) : ℝ := 32 * M ^ 3 / rK M p * Real.exp (-rK M p / (2 * M))

lemma FS_pos {p : P} (hp : p ∈ regI) : 0 < FS M p := by
  have := (rK_spec hM hp).1; unfold FS; positivity

lemma FS_tendsto {V₀ : ℝ} :
    Tendsto (FS M) (𝓝[regI] ((0 : ℝ), V₀))
      (𝓝 (32 * M ^ 3 / (2 * M) * Real.exp (-(2 * M) / (2 * M)))) := by
  have hr := rK_tendsto hM (V₀ := V₀)
  have h2 : (2 * M) ≠ 0 := by positivity
  exact ((tendsto_const_nhds.div hr h2).mul
    ((Real.continuous_exp.tendsto _).comp ((hr.neg).div_const _)))

/-- **② with Schwarzschild's own conformal factor** (`BUILT`): `F = (32M³/r)e^{−r/2M}` is positive on
region I and bounded near `(0, V₀)`, so both slicings align for the Schwarzschild Kruskal metric
`g = −F dU dV`, with limit covector `(F₀/2) dU`, `F₀ = 16M²/e`. -/
theorem tc_schwarzschild {a η : ℝ} (ha : 0 < a) (hη : 0 < η) {V₀ : ℝ} (hV : 0 < V₀) :
    Tendsto (fun p => (fderiv ℝ (tK M) p (nF (FS M p)))⁻¹ • fderiv ℝ (tK M) p)
      (𝓝[regI] ((0 : ℝ), V₀))
      (𝓝 ((32 * M ^ 3 / (2 * M) * Real.exp (-(2 * M) / (2 * M)) / 2) • fst ℝ ℝ ℝ)) ∧
    Tendsto (fun p => (fderiv ℝ (ΘK M a η) p (nF (FS M p)))⁻¹ • fderiv ℝ (ΘK M a η) p)
      (𝓝[regI] ((0 : ℝ), V₀))
      (𝓝 ((32 * M ^ 3 / (2 * M) * Real.exp (-(2 * M) / (2 * M)) / 2) • fst ℝ ℝ ℝ)) := by
  have hFt := FS_tendsto hM (V₀ := V₀)
  have hC := hFt.eventually (gt_mem_nhds (lt_add_one _))
  have hC' := hC.mono fun _ h => h.le
  exact ⟨tc_kruskal_limit hFt (tc_stationary hM hV (fun p hp => FS_pos hM hp) hC').2.2.2.2,
    tc_kruskal_limit hFt (tc_retarded hM ha hη hV (fun p hp => FS_pos hM hp) hC').2.2.2.2.2.2⟩

end Retarded

end Kruskal

/-! ## ③ Non-vacuity of ① in 2D Minkowski -/

/-- **③ Non-vacuity of the sequence corollary.** 2D Minkowski `g = −dU dV` (`F = 1`),
`ℓ = ∂_V`, `n = 2∂_U`, `ξ_m = (m+1) dU + dV`: every frame hypothesis holds, `ξ_m(ℓ) = 1`,
`ξ_m(n) = 2(m+1) → ∞`, and `ξ_m/ξ_m(n) → −g(ℓ,·) = ½ dU`. -/
theorem tc_minkowski_nonvacuous :
    let ξ : ℕ → Kruskal.P →L[ℝ] ℝ := fun m =>
      ((m : ℝ) + 1) • ContinuousLinearMap.fst ℝ ℝ ℝ + ContinuousLinearMap.snd ℝ ℝ ℝ
    (∀ m, FrameHyp (Kruskal.gF 1) Kruskal.ℓ (Kruskal.nF 1) (ξ m)) ∧
    (∀ m, ξ m Kruskal.ℓ = 1) ∧
    Tendsto (fun m => ξ m (Kruskal.nF 1)) atTop atTop ∧
    Tendsto (fun m => (ξ m (Kruskal.nF 1))⁻¹ • ξ m) atTop
      (𝓝 ((1 / 2 : ℝ) • ContinuousLinearMap.fst ℝ ℝ ℝ)) := by
  intro ξ
  have hF : ∀ m, FrameHyp (Kruskal.gF 1) Kruskal.ℓ (Kruskal.nF 1) (ξ m) := fun m =>
    Kruskal.tc_frameHyp2 one_pos (by simp [ξ, Kruskal.e1]; positivity) (by simp [ξ, Kruskal.ℓ])
  have hl : ∀ m, ξ m Kruskal.ℓ = 1 := fun m => by simp [ξ, Kruskal.ℓ]
  have hn : Tendsto (fun m => ξ m (Kruskal.nF 1)) atTop atTop := by
    have : (fun m => ξ m (Kruskal.nF 1)) = fun m : ℕ => 2 * ((m : ℝ) + 1) := by
      ext m; simp [ξ, Kruskal.nF, Kruskal.e1]; ring
    rw [this]
    exact Tendsto.const_mul_atTop two_pos
      (tendsto_atTop_add_const_right _ 1 tendsto_natCast_atTop_atTop)
  have h := (tc_sequence hF (fun m => (hl m).le) hn).1
  have e : -(Kruskal.gF 1 Kruskal.ℓ) = (1 / 2 : ℝ) • ContinuousLinearMap.fst ℝ ℝ ℝ := by
    ext <;> simp [Kruskal.gF_ℓ]
    norm_num
  exact ⟨hF, hl, hn, e ▸ h⟩

#print axioms tc_pointwise
#print axioms tc_W_bound
#print axioms tc_futCausal_iff
#print axioms tc_opNorm_bound
#print axioms tc_tendsto
#print axioms tc_tendsto_limit
#print axioms tc_sequence
#print axioms Kruskal.tc_frameHyp2
#print axioms Kruskal.tc_L_neBot
#print axioms Kruskal.tc_kruskal_align
#print axioms Kruskal.tc_kruskal_limit
#print axioms Kruskal.tc_stationary
#print axioms Kruskal.tc_rK_partials
#print axioms Kruskal.tc_retarded
#print axioms Kruskal.tc_schwarzschild
#print axioms tc_minkowski_nonvacuous

end ShadowProbe.TangencyConditionProbe

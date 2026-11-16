# `r7809+71.1` — PRE-REGISTRATION: 6b-ii, **phase 2: the kit's causal arcs are locally cone curves; the limit-curve theorem for chains, in a chart and on `N`**. ⌗ `800` new lines (band 600–1100), p(K1–K5 and K7 all BUILT) `0.45`

*Registered before any Lean. The plan is `../r7807_71_6bii/PLAN.md` (phase 2: 900–1800 lines, p 0.35). The probe is
the new standalone `probes/ConeCurves.lean` (`kc_`). It imports only Mathlib and carries verbatim copies of
`probes/LimitCurve.lean`'s phase-1 section (L1–L3) and of the kit blocks it needs from `probes/GeneratorStretch.lean`
(the chart `Spacetime` with `restrict`; the manifold `MSpacetime`, `chartSp` and `ch_cau_iff` for K5). Copies are
not counted in the band.*

**Setting.** `V` is a finite-dimensional real normed space and `S : Spacetime V` is the kit's chart spacetime
(`g` and `T` continuous on the open `M`). At `x₀ ∈ M` put `τ₀ v = −g_{x₀}(v, T x₀)`, a continuous linear functional,
and `K(c) = {v : c‖v‖ ≤ τ₀ v}`: closed, and closed under addition and non-negative scaling. This is the
"constant cone slightly wider than the light cone" of the plan.

| Row | Statement | Lines | p | Note |
|---|---|---|---|---|
| K1 | **The cone lemma.** For `x₀ ∈ M` there are `r, c > 0` with `ball x₀ r ⊆ M` such that every future-causal vector at every `x ∈ ball x₀ r` lies in `K(c)` | 100–180 | 0.75 | By compactness of the unit sphere and continuity of `g`, `T`; the limit vector would be `g_{x₀}`-orthogonal to `T x₀` and causal, against `pos_on_perp` |
| K2 | **Arcs and chains are cone curves.** A `C¹` arc with velocity in `K(c)` on `[a, b]` is a `K(c)`-curve (mean-value inequality with a boundary function, `image_norm_le_of_norm_deriv_right_le_deriv_boundary`). So for `B = ball x₀ r`, every `(S.restrict B).CStep` arc is one, and `(S.restrict B).Cau x y` gives `y − x ∈ K(c)` | 60–140 | 0.8 | |
| K3 | **`τ₀`-parametrisation of chains.** `(S.restrict B).Cau x y` gives a `τ₀`-parametrised `K(c)`-curve on `[τ₀ x, τ₀ y]` from `x` to `y` with values in `B`: each arc reparametrised by the inverse of the strictly increasing `τ₀ ∘ γ` (`Function.invFunOn`), and arcs concatenated | 150–300 | 0.6 | |
| K4 | **The local limit-curve theorem for causal chains in a chart.** Chains `(S.restrict B).Cau xₙ yₙ` with `xₙ → p` and `τ₀ yₙ ≥ τ₀ xₙ + δ` have parametrisations `ηₙ` on `[0, δ]` and a subsequence converging uniformly to a `τ₀`-parametrised `K(c)`-curve `γ` with `γ 0 = p` | 80–160 | 0.65 | Phase 1's L3 applied to K3's curves, shifted |
| K5 | **On `N`.** Under the kit's `OneChart p₀`, the same for chains of the manifold kit inside the chart: transported by `ch_cau_iff` and `chartSp`, the limit is a continuous curve in `N` through `p` (the chart inverse of K4's `γ`), approached uniformly in the chart | 150–350 | 0.45 | Needs a ball in the chart image and the restricted chart spacetime to agree with `chartSp` of the restricted `MSpacetime`; if that bookkeeping costs more than it buys, K5 is stated on `chartSp` directly and marked BUILT IN PART |
| K6 | **The global limit-curve theorem on `N`** in an auxiliary metric, patching charts | — | 0.15 | **The expected stop.** Patching local segments into one curve is the same maximal-extension argument that inextendibility (phase 3) runs; I expect to report it as moving there rather than build it twice |
| K7 | **Non-vacuity.** A 2D Minkowski chart (`g = diag(−1, 1)`, `T = (1, 0)`) with causal chains to which K1–K4 apply, and a sequence of chains converging to a limit curve | 50–120 | 0.75 | |

**Not in this phase:** inextendibility and non-imprisonment (3), the achronal-boundary argument (4), and
`HasFutureGenerators` (5). P1's 6b-ii stays BUILT IN PART.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

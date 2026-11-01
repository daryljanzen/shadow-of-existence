# `r7649+71.1` — PRE-REGISTRATION: campaign 84 built, `r7649`, route (c), global-chart transport. The headline on any Mathlib manifold whose spacetime region lies in one chart, proved by moving it back to campaign 81's single-chart theorem. ⌗ `1000–1500` new lines plus about `100` changed, in one probe (band 700–2200 new), ⛔ stop `2600` new. ⌗ p: c1 `0.75`, c2 `0.4`, **whole `0.35`**. **If it fails, the expected missing piece is the chart transfer of the timelike step** (`TStep_N ↔ chart TStep`), at the squash reparametrisation and the `mfderiv`/`deriv` identification along a curve. Second likeliest: localising `𝓗⁺` to the chart target

*Under `r7649` (69 chose route (c)). The route, its estimate and its risks are registered in
`r7647_71_campaign84/PREDICTION.md` and `SCOPING.md`, and are not repeated here. No Lean was written before this
registration.*

## The build (`probes/ChartHeadline.lean`)

***c1: the `V` side.*** Copy campaign 81's `HeadlineHypotheses.lean`.
- **The fields.** `Spacetime`'s `cont_g`, `cont_T` and `LocallyLipschitz g` are weakened from all of `V` to `M`:
  `ContinuousOn` and `LocallyLipschitzOn`. Every proof that used them is re-checked.
- **The localised headline.** `hl_causal_alignment_gh_loc` takes an open `W ⊇ M`, the chart target, with
  `𝓗⁺ ∩ W ⊆ M` in place of `𝓗⁺ ⊆ M`. Its conclusions are intersected with `W`.
- **The witness.** Campaign 81's model is re-checked under it, with `W = univ`.

***c2: the manifold side.***
- **The structure.** A manifold spacetime on `N` (`ChartedSpace E N`, `IsManifold 𝓘(ℝ,E) 1 N`): sections `g` and `T`,
  an open `M ⊆ (chartAt p₀).source`, and the manifold `TStep_N` and `CStep_N`, which are curves with `mfderiv` velocity
  future-timelike or causal.
- **The chart spacetime.** `M_V = φ(M)`, `g_V = hRep g p₀`, `T_V = chartRep T p₀`, built from campaign 68's lemmas.
- **The transport.** `TStep_N x y ↔ TStep_V (φx) (φy)`, the step the prediction names as the likeliest stop. Then
  `Chr`, `Cau`, `D`, `𝓗⁺` (inside the chart), slices, `KLi`/`KLs`, `IsTemporal` and the two-sided Cauchy property.
- **The headline.** `hl_causal_alignment_gh_N`: `KLi = KLs = 𝓗⁺` on `N`, under P1's hypotheses read on `N` plus
  `M ⊆ (chartAt p₀).source` and `g` C¹ in that chart.
- **Non-vacuity.** A witness with a non-identity chart, such as the Rindler model on a manifold whose chart is a
  linear isomorphism. If even the identity chart is all that is reachable, RESULT says so.

***Failable:*** each piece is BUILT, BUILT IN PART, or REPORTED, with the step that stopped.

***What would change P1.*** Nothing in P1's statement changes if (c) is BUILT. P1's exemplars fit one chart, and the
general clause stays covered only by the paper argument, with route (b) named as the remaining formalisation. If (c)
fails at the transport, P1 is unchanged and the inventory row stays BUILT IN PART (chart).

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

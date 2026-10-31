# `r7647+71.3` — PROPOSAL AND PRE-REGISTRATION: campaign 84, `r7647` ②, the single chart. **The causal layer does not exist on the manifold layer at all**: campaigns 66 and 68 have no time orientation, no causal vectors or curves, and no `≪`, `D`, `𝓗⁺` or Θ. So the headline cannot be carried onto them as they stand. The proposal is a **global-chart transport**: state the headline on a Mathlib manifold whose `M` lies in one chart, and prove it by moving it back to campaign 81's single-chart theorem. No causal argument is re-proved. ⌗ estimate `1000–1500` new lines plus about `100` changed, in one probe (band 700–2200 new), ⛔ stop `2600` new. ⌗ p: c1 `0.75`, c2 `0.4`, whole `0.35`. **Not started: 71 asks 69 to approve the route first**

*Under `r7647` ②. The scoping is `SCOPING.md` beside this file: a read-only survey of `HeadlineHypotheses.lean` and of
`FlowManifold`/`LieDerivManifold`. No Lean has been written for it.*

## What exists, and what does not

***The single-chart proof.*** It uses `V`'s vector-space structure in only two ways:
- **On short arcs inside one chart:** the tube lemma, `local_pushup`, the short future and past steps, and the line
  `q − εe^{−t}T(q)`.
- **With no one-chart form:** the polygonal past extension, whose no-limit argument is metric.

***Everything else is topological or relational.*** `Chr`/`Cau`, `D`, `𝓗⁺` as a frontier, `KLi`/`KLs`, properness,
the Kuratowski steps and the Cauchy equivalence.

***The manifold layer of campaigns 66 and 68.***
- **It has:** `N` with `ChartedSpace`/`IsManifold`, vector fields, `mfderiv`, flows and flow boxes, the Lie derivative,
  `hRep`/`chartRep` and `LocalKillingChart`.
- **It lacks:** any time orientation or causal notion. A grep of the 14 manifold probes finds no `TStep`, `Chr` or
  `Timelike`.

## The first missing pieces, exactly

1. **On the `V` side.** `Spacetime` asks for `cont_g`, `cont_T` and `LocallyLipschitz g` on all of `V`. That is not
   chart-invariant, and a chart's pulled-back metric cannot satisfy it off the chart's image.
   - The proofs use `g` and `T` only on `M`, so restricting these fields to `M` is mechanical.
   - `𝓗⁺` is a frontier in all of `V`, so it needs a localised form: `𝓗⁺ ∩ W ⊆ M` for the chart target `W`.
2. **On the manifold side, the first thing that does not exist.** A spacetime on `N` (sections `g`, `T`); the manifold
   timelike step `TStep_N` (C¹ curves with `mfderiv` velocity future-timelike); and its chart transfer
   `TStep_N x y ↔ (chart spacetime).TStep (φx) (φy)`. The transfer needs a squash reparametrisation, since `V`'s `TStep`
   asks for `ContDiff` on all of `ℝ`.
3. **For general multi-chart manifolds only.** The inextendible extension of a causal curve on `N`: pieces of the
   integral curve of `−T` from campaign 66's `FlowData`, with convergence ruled out by the temporal `Θ`.

## The routes, estimated

| route | new lines | campaigns | the main risk |
|---|---|---|---|
| (a) full lift, re-proving the chain on `N` | 3000–5000+ | 4–6 | the vector-space steps need charts anyway, so it collapses into (b) at higher cost |
| (b) localisation, for multi-chart `N` | 2000–3500 | 3–5 | the extension theorem (500–900 lines on its own); splitting curves across a chart cover |
| **(c) global-chart transport** | **1000–1500 + about 100 changed** | **1** (c1 + c2) | the `TStep` transfer (squash, `ContMDiff`); `TangentSpace` instance heartbeats |

## The proposal: route (c)

***c1.*** Weaken `Spacetime`'s `cont_g`, `cont_T` and `LocallyLipschitz g` to `M`, and localise `𝓗⁺` to the chart
target. Campaign 81's chain is then re-checked. p `0.75`.

***c2.***
- The manifold definitions.
- The transport of steps, relations, `D`, `𝓗⁺`, slices, `KLi`/`KLs`, `IsTemporal` and the Cauchy property along
  `chartAt p₀`.
- `hl_causal_alignment_gh_N`: the headline on any Mathlib manifold with `M ⊆ (chartAt p₀).source` and `g` C¹ in that
  chart.
- A witness with a non-identity chart.

p `0.4`. Whole campaign p `0.35`.

***What (c) would claim, honestly.*** The headline holds on every manifold whose spacetime region lies in one chart.
- That covers P1's exemplars. The Kruskal and Oppenheimer–Snyder exteriors are open subsets of `ℝ⁴`, though that fact
  is itself not formalised.
- P1's general clause, "any asymptotically flat spacetime whose exterior is globally hyperbolic", would still need
  route (b), beginning with the extension theorem as its own campaign.

***Why it is not started.*** 69's order asks for an honest estimate before any Lean. This is a refactor of the shared
`Spacetime` structure (c1) plus a transport layer of about 1000+ lines (c2). 71 asks 69 to choose:
- (c) as proposed;
- (c1) alone first;
- or to go straight to (b).

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

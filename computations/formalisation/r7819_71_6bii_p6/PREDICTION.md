# `r7819+71.1` — PRE-REGISTRATION: 6b-ii, **phase 6: `HasFutureGeneratorsM` landed under `LocallyOneChart`, and "monotonically"**. ⌗ `2800` new lines (band 1800–4000), p(W1 BUILT) `0.8`, p(W1–W7 all BUILT) `0.2`

*Registered before any Lean. The order is 69's `r7819`: land the generator hypothesis under the multi-chart
`LocallyOneChart`, and state and prove that the cone boundaries approach `𝓗⁺` monotonically. The probe is the new
standalone `probes/MultiChart.lean` (`m6_`). It imports only Mathlib and carries a verbatim copy (not counted) of all
of `probes/Generators.lean`, which already holds the kit, phases 3 and 4, and phase 5.*

## Monotonicity, as I will state it

The cones are `cone O τ = ∂J⁻(O τ)`, and the stretch is `{q ∈ 𝓗⁺ | infDist q (cone O τ) < ε}`.

- **(i) The pasts nest.** `J⁻(O s) ⊆ J⁻(O t)` for `s < t`.
- **(ii) Distance to the pasts.** For every point `x`, `τ ↦ infDist x (J⁻(O τ))` is antitone.
- **(iii) Horizon points stay outside.** Every `q ∈ 𝓗⁺` lies outside every `J⁻(O τ)`, by push-up into `D J`.
- **(iv) The cone boundaries, under one disclosed hypothesis.** If the metric's balls are connected, then for
  horizon points the distance to the boundary `∂J⁻(O τ)` equals the distance to `J⁻(O τ)`. So the boundaries approach
  `𝓗⁺` monotonically, and the stretch increases with `τ`.
  - The hypothesis holds for normed metrics, and so for the 4D witness.
  - **Why it is needed.** For an arbitrary metric on `N`, the distance to a boundary need not be monotone even
    though the sets nest. That gap is topological, not a Mathlib gap, so I disclose the hypothesis rather than stop
    on it.

## The multi-chart landing, as I will build it

**Why phases 3–5 do not carry over.** They build the generator inside one chart. Under `LocallyOneChart` no chart
holds the generator. Local pieces cannot be landed separately either: restricting the spacetime to a patch breaks
`hOD`, because `J⁻` in the patch is not `J⁻` in `S`.

**The plan:**
- **Local segments.** Each local segment comes from phase 3 and 4's tools, applied in the chart of one patch:
  - from points of `D J` converging to `p`, take the initial pieces of the chains to `O`, truncated by Θ-rise;
  - the stay lemma keeps them in a chart ball;
  - Arzelà–Ascoli and the limit lemmas keep them Θ-causal and keep the linear constraints;
  - `pu4_closure` gives the segment's points in `closure (I⁺(p) ∪ {p})`.
- **Globally on `N`, with the kit's `N`-level lemmas:**
  - `𝓗⁺` membership;
  - transitivity of `closure (I⁺(·) ∪ {·})`;
  - the iteration, with a segment length uniform on compacts;
  - non-imprisonment.

**Hypotheses added beyond phase 5's, disclosed:**
- `[SecondCountableTopology N]` and `[T2Space N]`, the manifold convention, for a compact exhaustion of `M`;
- `LocallyOneChart` in place of `OneChart`.

| Row | Statement | Lines | p | Note |
|---|---|---|---|---|
| W1 | **Monotonicity**, (i)–(iv) | 150–350 | 0.8 | `IsPreconnected.inter_frontier_nonempty`-type argument for (iv) |
| W2 | **Transitivity on `N`.** `y ∈ closure (I⁺(x) ∪ {x})` and `z ∈ closure (I⁺(y) ∪ {y})` give `z ∈ closure (I⁺(x) ∪ {x})`. Also concatenation of curves with this property | 100–250 | 0.75 | Openness of `I⁻` under `LocallyOneChart` (`mk_isOpen_Ipast`) |
| W3 | **The local segment.** For `p ∈ 𝓗⁺ ∩ M`, in a patch chart around `p`: a continuous, Θ-parametrised curve on `[0, δ]` from `p`, in `𝓗⁺ ∩ closure (I⁺(p) ∪ {p})`, that is a uniform limit (in the chart) of chain parametrisations | 600–1200 | 0.4 | Truncation of chains by Θ-rise; a local limit that keeps `pu4_Lin` |
| W4 | **Uniform length.** On every compact `K ⊆ M` there is one `δ_K > 0` for all `p ∈ 𝓗⁺ ∩ K` | 200–450 | 0.45 | Finite subcover of patch balls |
| W5 | **The cone bound across charts, and non-imprisonment on `N`.** A segment built in one patch meets the cone bound in every other patch chart, being a limit of chains that are chains there too. So a concatenation that accumulates at `z ∈ M` as `t → T*` converges to `z` | 400–900 | 0.3 | **The expected stop.** Chart change for limits of chain parametrisations |
| W6 | **The landing.** Under `LocallyOneChart`, second countability, `T2Space`, and the hypotheses of phase 5 (with `OneChart` dropped): `HasFutureGeneratorsM S J`, by iteration on the exhaustion's index (as in phase 3's diagonal) and `g5_reparam`. With `g5_future_stretch`, the stretch statement follows without assuming generators | 300–700 | 0.3 | |
| W7 | **Non-vacuity.** The 4D witness meets W1 (normed metric, connected balls) and W6's hypotheses. A witness that no single chart covers is not in the kit's base (the kit's cylinder and `Pt` live in other probes), so it is reported, not built, unless time allows | 80–200 | 0.6 | |

**Mathlib.** No gap is expected. Arzelà–Ascoli, compact exhaustions (`CompactExhaustion`, `SigmaCompactSpace` from
second countability and local compactness), connectedness and frontiers are all there. The risk is the size of the
chart-change bookkeeping in W5. If W5 does not close, I report the exact missing step and how much of W6 stands
without it.

**Not in this phase:** route (a), which 69 ruled is not needed.

P1's 6b-ii moves to BUILT only when W1 and W6 are both built.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

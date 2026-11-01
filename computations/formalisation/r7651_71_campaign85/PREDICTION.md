# `r7651+71.1` — PRE-REGISTRATION: campaign 85, `r7651`, route (b)'s first piece. The extension of inextendible causal curves on a multi-chart manifold `N`, then two-sided Cauchy ⇒ future Cauchy on `N`. ⌗ `800` new lines in one probe (band 400–1600 new), ⛔ stop `2200` new. ⌗ p: the extension `0.45`, two-sided ⇒ future on `N` `0.4`. **Expected stop: gluing the infinitely many manifold `TStep`s into one piecewise-`ContMDiff` curve `ℝ → N` with breaks at the integers.** Second likeliest: the uniform step at the limit point through that point's own chart. **Route (b) re-priced: 3 campaigns, about 2000–3000 new lines, within r7647's 2000–3500 over 3–5, so building**

*Under `r7651`. The setting is campaign 84's `probes/ChartHeadline.lean` (the manifold spacetime, `TStep_N`, the arctan
squash, and the chart transfer `ch_tstep_iff`), copied into a new probe, `probes/ManifoldExtension.lean`. No Lean was
written before this registration.*

## The route, and why it avoids the hard part

***The obstacle the V proof meets.*** Campaign 78's polygonal extension proves "no past limit" with a uniform step
length near a limit point, measured in `V`'s norm. On a multi-chart `N` the steps would be taken in different charts.
`chartAt` is an arbitrary choice, so no uniform coordinate length exists across them.

***The registered route measures each step by how much `Θ` drops, not by its length.*** `Θ` is temporal on `M`, and
`Θ` is always present where the extension is used (the Cauchy property).
- **The step size.** Set `δ(x) := min(1, sup {Θ(x) − Θ(y) : TStep_N y x})`. This needs no metric.
- **The polygon.** Choose `x_{k+1}` with `TStep_N x_{k+1} x_k` and `Θ(x_k) − Θ(x_{k+1}) ≥ δ(x_k)/2`.
- **No past limit in `M`.** Suppose `x_k → x* ∈ M`.
  - In `x*`'s **own** chart, take a fixed coordinate length.
  - By campaign 84's transfer `ch_tstep_iff`, each nearby `x` has a past `TStep` dropping `Θ` by at least a fixed
    `c > 0`. This uses the tube lemma and the continuity of `dΘ` and `g` in that one chart.
  - So `δ ≥ c` near `x*`. Then `Θ(x_k)` falls by at least `c/2` per step eventually, so `Θ(x_k) → −∞`.
  - That contradicts `Θ(x_k) → Θ(x*)`.
- **The curve.** Concatenate the steps on `[−k−1, −k]`, after reparametrising each `TStep_N`.
- **The assumptions on `N`.** `LocallyOneChart`: every `p ∈ M` has `hRep g p` C¹ and `chartRep T p` continuous near
  `φ_p(p)`. This is P1's smooth `g` and `T`. It replaces campaign 84's single `OneChart`.

***Then.***
- `InextCausalCurve_N`.
- Two-sided Cauchy ⇒ future Cauchy on `N`, by gluing the extension to a future-inextendible curve, as in campaign 78.

## Route (b), re-priced with campaign 84's machinery

1. **Campaign 85, this one.** The extension, and two-sided ⇒ future on `N`. About `800` lines.
2. **Campaign 86, the local kit.** The local lemmas, each through one chart's transfer:
   - openness of `I^±` on `N`;
   - push-up on `N`, using `local_pushup` in a chart plus `Chr`/`Cau` concatenation;
   - the short future and past steps, and the curve `q − εe^{−t}T(q)` in `q`'s chart.

   About `700–1100` lines.
3. **Campaign 87, the assembly.** The chain on `N`: properness, `hint`/`hcl`, the slice limits and Kuratowski, giving
   `hl_causal_alignment_gh` for any manifold with `LocallyOneChart`, with a two-chart witness. About `600–1100` lines.

***The total.*** 3 campaigns, about `2000–3000` new lines. That is within r7647's pricing of 2000–3500 lines over
3–5 campaigns. **So this is built, not referred back.**

***Failable:*** each piece is BUILT, BUILT IN PART, or REPORTED, with the step that stopped.

***Reachable negative.*** If gluing the steps is heavy, RESULT states the extension as a sequence of `TStep_N`s with
no past accumulation point in `M`. That is enough for the Cauchy argument only once the gluing exists, so RESULT
names gluing as the remaining piece.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

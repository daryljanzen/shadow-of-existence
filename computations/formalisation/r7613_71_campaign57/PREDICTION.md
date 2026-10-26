# `r7613+71.1` — PRE-REGISTRATION: campaign 57, `r7613` ①, `thm:metric-singularity` and `cor:threefold` (iii)–(iv) as Lean theorems. ⌗ `300` lines in one probe (band 120–700), ⛔ stop `1200`. ⌗ p: built `0.9`, non-invariance clause `0.7`

*Under `r7613` ①. The source is `corpus/BH_causality_v2.tex`, lines 130–200. No Lean was written before this registration.*

## ① The pieces (`probes/MetricSingularity.lean`)

- ***The relation.*** In the adapted frame of hypothesis (b), the invariant separations satisfy `Δs² = Δx² − Δτ²`.
  Stated as the paper states it: the hypotheses are this relation, (a) `Δs² = 0`, and (b) `Δx = 0`. The conclusion
  is `Δτ = 0`. The relation is a hypothesis of the theorem, and the frame is not constructed.
- ***Along the connection.*** For a C¹ curve `γ : [0,1] → ℝ × ℝⁿ`, write `γ = (τ, x)`. Assume
  `g(γ′, γ′) = |x′|² − τ′² = 0` and (b) `x′ = 0` on the whole segment. Then `τ′ = 0` on the segment, so
  `τ(1) = τ(0)` and `Δτ = 0`. This is the remark's form, with (b) holding at every point of the connection.
- ***`cor:threefold` (iii).*** Along such a segment `g(γ̇, γ̇) = 0` at every parameter.
- ***`cor:threefold` (iv), second half: non-invariance without (b).*** For any temporal function `τ` and any curve
  with `γ(0) ≠ γ(1)`, there is a smooth `τ̃ = τ + φ` with the same temporal property near `γ`, with `φ` of
  arbitrarily small C⁰ size and supported near `γ(1)`, and with `τ̃(q) − τ̃(p) ≠ τ(q) − τ(p)`. "Temporal" is taken
  as `∂_t τ > 0` in a chart. The bump `φ` is built from Mathlib's `ContDiffBump`.

***Failable:*** BUILT, BUILT IN PART, or REPORTED per piece. ***Reachable negative:*** the non-invariance clause
needs the temporal property to survive the bump. If a C¹-small bump with that control cannot be had from
`ContDiffBump` within the stop, (iv)'s second half is REPORTED, with the missing estimate named, and the rest
stands.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

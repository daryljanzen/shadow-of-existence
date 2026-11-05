# `r7687+71.1` — PRE-REGISTRATION: campaign 104, `r7687` ①, **2i under P1's new hypothesis: with no closed causal curves, the endpoints of a causal curve are distinct and so topologically distinguishable; and the hypothesis holds wherever a temporal function exists, so on `D` and on the witnesses.** ⌗ `250` new lines (band 120–600), p `0.85`. **Expected stop:** strict increase of a temporal function along a chain of causal steps

*Registered before any Lean. The new probe is `probes/ThreefoldDistinct.lean`, a copy of campaign 103's
`ThreefoldOrder.lean`. Everything new is prefixed `td_`.*

## The definition

- **`S.NoClosedCausal`:** no point is joined to itself by a non-empty chain of the kit's future causal steps. Formally,
  `∀ p, ¬ Relation.TransGen S.CStep p p`, using the kit's `CStep`, or the step relation underlying `Cau`, whichever the
  kit defines. A causal step's velocity is future causal, so it is non-zero, so a step is never a constant curve.
- **Said plainly:** on this definition 2i itself is immediate. Its content lies in the definition being the right one,
  and in the sufficient condition below.

## ① 2i — p `0.95`

- **`td_cor_threefold_i`:** under `NoClosedCausal`, if `TransGen CStep p q`, then `p ≠ q`.
- **And distinguishable:** on a Hausdorff `N`, there are disjoint open neighbourhoods of `p` and `q`, by
  `t2_separation`.
- **This covers P1's segment:** `γ` from `p` to `q` is a causal curve, a chain of steps.

## ② Why the hypothesis holds in P1's settings — p `0.8`

- **`td_noClosed_of_temporal`:** if some `τ` is temporal on `M`, then `NoClosedCausal`. Each step strictly raises `τ`,
  by the kit's `temporal_curve` form, so a chain does too, and `τ p < τ p` is impossible. This is the expected stop.
- **`td_noClosed_D`:** a Cauchy temporal function on `D` gives `NoClosedCausal` for `D` as a spacetime (`Dsp`, or the
  restriction). That is P1's globally hyperbolic exterior.
- **Witnesses:**
  - `td_minkN_noClosed`: Minkowski on `Pt`, with `τ = U + V`.
  - Hence `to_cor_1c`'s pair also satisfies (i)'s hypothesis.

## Not attempted

The counterexample, Minkowski modulo a null translation with a closed null geodesic, would need a quotient manifold.
It is argued in campaign 103's registration and not built.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

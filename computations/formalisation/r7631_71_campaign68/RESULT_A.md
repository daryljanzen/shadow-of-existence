# `r7631+71.4` — RESULT: campaign 68, `r7631` ②, the Lie derivative of (0,2)-tensor fields on a manifold BUILT, with chart formula, tensoriality and chart independence; `lem:killing` (b) BUILT with the coordinate-free condition `L_X g = 0`; the C² requirement REMAINS, and where is stated. ⌗ `2081` lines in one probe (`1543` copied from campaign 66, about `540` new against the registered `700`; band 250–3000). ⌗ p: definition + chart formula `0.55` came true, coordinate-free Killing `0.45` came true, C² removed `0.2` did not

*Against `PREDICTION.md` (`r7631+71.2`). 71 re-ran `lake env lean probes/LieDerivManifold.lean`. It exits 0 with no
errors. All `96` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`.*

## ① The Lie derivative, by the registered bracket route

***Definition.*** `lieDeriv X h x v w` is `X(h(V,W)) − h([X,V],W) − h(V,[X,W])`, with Mathlib's `mlieBracket`,
evaluated on `constExt x v` and `constExt x w`. These are fields constant in the chart at `x`, built with
`mpullback`.

***Results.***
- `ld_chartLie_core` and `ld_lieDerivForm_model`: on the model space the test-field expression is the chart formula
  `chartLie F X̃ = DF(X̃) + F(DX̃·,·) + F(·,DX̃·)`, campaigns 62 and 66's `IsKilling` expression.
- `ld_lieDeriv_chart_self`: the chart formula holds in the chart at the point. This works on a C¹ manifold.
- **`ld_lieDerivForm_eq_lieDeriv`**: tensoriality. Any C¹ test sections give the same value, on a C¹ manifold.
- **`ld_lieDeriv_chart`**: chart independence. For `x` in the chart at `p`, `lieDeriv X h x v w` equals
  `chartLie (hRep h p) (chartRep X p)` at `φ_p x` on `(Dφ_p v, Dφ_p w)`. It needs a C² manifold.
  - Mathlib's `mpullback_mlieBracket` carries the bracket's invariance under C² maps, so no transformation law is
    written by hand.

## ② `lem:killing` (b), coordinate-free

***`ld_manifold_killingChart_lieDeriv`.***
- **Hypotheses:**
  - `X` is C¹ at `p` as a tangent-bundle section, with `X p ≠ 0`;
  - `g` is differentiable near `p` in the chart;
  - **`lieDeriv X g x v w = 0` for all `v, w` and all `x` near `p`.**
- **Conclusion:** a `LocalKillingChart`.
- `LocalKillingChart.ld_metric_N`: the chart's metric components are `g`'s own on `N`, so `∂_λ g_ab = 0` is a
  statement about `g` itself.
- The Killing condition is now coordinate-free. Only `g`'s differentiability is still stated in chart form.

## The C² question, answered as `r7631` asked: it remains

***Works on a C¹ manifold.***
- The definition.
- The chart formula at the point.
- Tensoriality.
- The pointwise flow box.

***Needs a C² manifold.***
- Chart independence, `ld_lieDeriv_chart`, through `mpullback_mlieBracket`, which needs a symmetric second
  derivative of the transition map.
- The C¹-ness of a section's representative in another chart.
- Therefore the neighbourhood form of `lem:killing` (b), which compares `lieDeriv` at points `x ≠ p` with the chart
  at `p`.

***Why this is a limit.*** On a C¹ manifold, `mlieBracket` itself is not chart-invariant. This is a mathematical limit,
not a missing declaration.

## Not built

- A chart-free smoothness hypothesis on `h`. That would need a smoothness notion for sections of the bundle of
  bilinear forms on `TN`, linked to `hRep`.

No census row moves: `lem:killing` is a P1 theorem, not a row.

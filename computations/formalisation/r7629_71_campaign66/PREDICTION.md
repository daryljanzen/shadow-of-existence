# `r7629+71.2` — PRE-REGISTRATION: campaign 66, `r7629` ②, the section form of the field's `C¹` hypothesis for the manifold flow-box chart, and `lem:killing`'s manifold transfer stated without the chart-form hypothesis. ⌗ `500` lines in one probe (band 150–1500), ⛔ stop `2500`. ⌗ p: section form `0.7`, `lem:killing` (b) on a manifold `0.45`

*Under `r7629` ②. The setting is campaign 64's `probes/FlowLocal.lean`, together with the Killing part of campaign
62's `probes/FlowC1.lean`, both copied in under a new namespace. No Lean was written before this registration.*

## ① The section form (`probes/FlowManifold.lean`)

***Statement.*** For `X : Π x, TangentSpace 𝓘(ℝ,E) x` on `N`, the section hypothesis
`ContMDiffAt 𝓘(ℝ,E) 𝓘(ℝ,E).tangent 1 (fun x ↦ (⟨x, X x⟩ : TangentBundle 𝓘(ℝ,E) N)) p`, or the same on a
neighbourhood, implies `ContDiffOn ℝ 1 (chartRep X p)` on a neighbourhood of `extChartAt p p`. Then
`fl_manifold_flowBox` holds with the section hypothesis.

***Route.***
- `contMDiffAt_section` / `contMDiffAt_totalSpace` in the trivialisation at `p`.
- `TangentBundle.continuousLinearMapAt_trivializationAt` to identify the trivialisation with
  `mfderiv (extChartAt p)`.

## ② `lem:killing` (b) on a manifold

***Statement.***
- Take a pseudo-Riemannian metric on `N` given in a chart, with `X` Killing in campaign 62's coordinate sense
  (`IsKilling` for the chart representatives) and `X p ≠ 0`.
- Then there is a chart around `p` in which `X = ∂_λ` and the metric components are `λ`-independent.
- This is the local adapted chart campaign 59's `KillingChart` assumed. It is stated as a local `KillingChart`
  record on the chart's source.

***Failable:*** each piece is BUILT, BUILT IN PART, or REPORTED.

***Reachable negative:*** `①`'s likely stop is the definitional mismatch between `TangentSpace` and `E` in
`mfderiv` and the trivialisation; campaign 64 warned of it. `②`'s likely stop is a coordinate-free Killing
condition on `N`, since Mathlib has no Lie derivative of `(0,2)`-tensor fields. In that case the Killing condition
is stated in chart form and RESULT says so.

***Census:*** `lem:killing` is a P1 theorem, not a `ROWS.tsv` row; all 111 rows are already `DONE`. So this moves
no census row. RESULT will restate this, as `r7629` asks.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

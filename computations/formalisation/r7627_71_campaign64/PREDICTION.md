# `r7627+71.2` — PRE-REGISTRATION: campaign 64, `r7627` ②, the local `FlowData` constructor from `ContDiffOn` on a ball, then the flow-box chart carried to a manifold chart. ⌗ `700` lines in one probe (band 200–2000), ⛔ stop `3000`. ⌗ p: local constructor `0.7`, manifold flow-box chart `0.35`

*Under `r7627` ②. The setting is campaign 62's `probes/FlowC1.lean`, copied in under a new namespace. No Lean was
written before this registration.*

## ① The local constructor (`probes/FlowLocal.lean`)

***Statement.*** `ContDiffOn ℝ 1 f (ball x₀ ρ) → Nonempty (FlowData f x₀)`, or `FlowData` restated so that it only
needs `f` on a closed ball.

***Route.*** Two options:
- **Cutoff.** Multiply `f` by a smooth bump equal to `1` on `closedBall x₀ (ρ/2)` and supported in `ball x₀ ρ`.
  This gives a global `C¹` field equal to `f` near `x₀`. Then show that the global flow stays in `ball x₀ (ρ/2)`
  for small `t` (speed is bounded by `sup‖f‖`), so it is a flow of `f` there.
- **Trajectory bound.** Prove the trajectory-stays-in-ball bound that Mathlib uses internally
  (`FunSpace.compProj_mem_closedBall`) and is not exported.

The cutoff is the registered route.

## ② The flow-box chart on a manifold

***Statement.*** Let `X` be a `C¹` (or smooth) vector field on a smooth manifold `N` modelled on `E`, with
`X p ≠ 0`. Then there is a chart `ψ` around `p` in which the pushed-forward field is the constant `e_λ`, stated as
`mfderiv` of `ψ⁻¹` at `(λ,h)` applied to `(1,0)` equals `X(ψ⁻¹(λ,h))`.

***Route.***
- Take the chart representative of `X`, which is `ContDiffOn` on the chart target.
- Apply ① and campaign 62's flow box.
- Compose with the chart.

***Failable:*** each piece is BUILT, BUILT IN PART, or REPORTED.

***Reachable negative:*** `②`'s likely stop is Mathlib's representation of vector fields on manifolds and their
chart pushforward. Possible missing pieces are `mfderiv` of a chart's `symm` composed with a partial homeomorphism,
or the `TangentBundle` section form. If it stops, the first missing declaration is named.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

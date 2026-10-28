# `r7619+71.2` — PRE-REGISTRATION: campaign 62, `r7619` ②, smooth dependence of flows on initial data, then a flow-box chart. ⌗ `900` lines in up to two probes (band 300–2500), ⛔ stop `3000`. ⌗ p: flow `C¹` in the initial point on a vector space `0.6`, flow-box chart on a vector space `0.45`, chart transfer to a manifold `0.25`

*Under `r7619` ②. The base is the unfinished T3b probe, `probes/SmoothFlowProbe.lean` (`r7281+71.5`). It stopped
at 230 of 250 lines on `flow_hasFDerivAt`, after its steps 1–3. No new Lean was written before this
registration.*

## ① The flow is `C¹` in the initial point (`probes/FlowC1.lean`)

***Setting.*** A `C¹` vector field `f` on a finite-dimensional real normed space `E`, and its local flow `φ(t, x)`
on a neighbourhood of `(0, x₀)`, taken from Mathlib's Picard–Lindelöf.

***Theorem.*** For small `|t|`, `x ↦ φ(t, x)` has derivative `J(t, x)` near `x₀`. Here `J` solves the variational
equation `J′ = Df(φ)·J` with `J(0) = id`, and `J` is continuous in `x`. So the flow map is `C¹` jointly near
`(0, x₀)`.

***Route.*** This is T3b's own steps 4–6: Grönwall on the first-order remainder, then Grönwall on `J_y − J_x`.

## ② The flow-box chart

***Theorem.*** If `f(x₀) ≠ 0`, take a hyperplane `H` complementary to `f(x₀)`. Then
`Ψ(λ, h) = φ(λ, x₀ + h)` is a local `C¹` diffeomorphism near `(0, 0)`, and in these coordinates `f = ∂_λ`, so
`DΨ · e_λ = f ∘ Ψ`.

***Proof.*** `DΨ(0, 0) = [f(x₀) | incl_H]` is invertible, so Mathlib's inverse function theorem applies
(`HasStrictFDerivAt.toPartialHomeomorph`).

## ③ Stretch: the manifold version and `lem:killing`

- Transfer the chart to a smooth manifold through a chart at `x₀`.
- State `lem:killing`'s hypothesis (b) coordinate-free. If `L_χ g = 0`, then in the flow-box chart `∂_λ g_ab = 0`,
  and campaign 59's `KillingChart` applies.

***Failable:*** each piece is BUILT, BUILT IN PART, or REPORTED.

***Reachable negative:*** if `①` stops again, RESULT names the first missing declaration exactly. The candidates
are the variational equation's solution being continuous in parameters, or a uniform Grönwall over a parameter
family. `②` depends on `①`. `③`'s likely stop is the link from `L_χ g` (as in `LieDerivProbe.lean`) to the chart
components; if it stops, that is named instead.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

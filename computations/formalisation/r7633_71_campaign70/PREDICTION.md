# `r7633+71.2` — PRE-REGISTRATION: campaign 70, `r7633` ②, the corner-cutting lemma, then the tangency clause of `prop:causal-alignment`. ⌗ `900` lines in one probe (band 300–3000), ⛔ stop `4500`. ⌗ p: the geodesic equation in a chart `0.7`, corner-cutting for C² curves `0.3`, tangency clause `0.1`

*Under `r7633` ②. The setting is a single chart, with a C² metric `g` on an open `M ⊆ V` (finite dimension), using
campaign 60's `Spacetime` structure strengthened to `C²`. No Lean was written before this registration.*

## ① Christoffel symbols and pregeodesics (`probes/CornerCutting.lean`)

***Definitions.***
- The Christoffel symbols of a C¹ metric in the chart:
  `Γ(x)(u,v) = ½ g_x⁻¹(Dg(u)v + Dg(v)u − (Dg(·)(u,v))♭)`.
- The geodesic operator `∇_{γ′}γ′ = γ″ + Γ(γ′,γ′)`.
- A curve is a **pregeodesic** if `∇_{γ′}γ′ ∥ γ′`.

## ② The corner-cutting lemma

***Statement.*** Let `γ` be a C² future-null curve on `[a,b]` that is not a pregeodesic at some interior parameter.
Then there are `s < t` with `γ(s) ≪ γ(t)`.

***Route.*** This is the standard first-variation argument. Take a variation `γ_ε = γ + εW`, with `W` built from
`∇_{γ′}γ′` (its transverse part) and a cutoff. Then `g(γ_ε′, γ_ε′) < 0` for small `ε > 0` on a subinterval. That
gives a timelike curve between nearby points, and push-up joins them to `γ(s)`, `γ(t)`.

## ③ Stretch: the tangency clause

***Statement.*** A generator that is C² is a null pregeodesic. The past cones `∂J⁻(O(τ))` accumulate onto `𝓗⁺`,
in a form the generators support, for example Hausdorff convergence on compact sets.

***Failable:*** each piece is BUILT, BUILT IN PART, or REPORTED.

***Reachable negative:*** `②`'s likely stop is constructing the variation field with
`g(γ′ + εW′, γ′ + εW′) < 0`. That needs the sign of `g(∇_{γ′}γ′, W)` against `g(γ′, W′)` to be controlled, which
is the heart of the standard proof. If it stops, RESULT names the inequality. `③` also needs the generators to be
C², which campaign 69 does not give. The expected split is the geodesic equation and corner-cutting for C² curves
as built, with tangency reported against generator regularity beyond Lipschitz.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

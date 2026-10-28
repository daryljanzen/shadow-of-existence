# `r7631+71.2` — PRE-REGISTRATION: campaign 68, `r7631` ②, the Lie derivative of (0,2)-tensor fields on a manifold with its chart formula, then `lem:killing` (b) stated coordinate-free. ⌗ `700` lines of new material in one probe (band 250–3000 including the copied base), ⛔ stop `4000`. ⌗ p: definition + chart formula `0.55`, `lem:killing` (b) coordinate-free `0.45`, C² requirement removed `0.2`

*Under `r7631` ②. The setting is campaign 66's `probes/FlowManifold.lean`, copied in under a new namespace. No Lean
was written before this registration.*

## ① The Lie derivative (`probes/LieDerivManifold.lean`)

***Definition, local.*** For a `C¹` vector field `X` and a `C¹` (0,2)-tensor field `h` on `N`, given as
`h : Π x, TangentSpace x →L TangentSpace x →L ℝ`, define `(L_X h)_x(v, w)`. Either:
- as the derivative of the pullback along the flow, at `t = 0`; or
- by the coordinate-free formula through test fields,
  `X(h(V,W)) − h([X,V],W) − h(V,[X,W])`, using Mathlib's `VectorField.mlieBracket`.

The bracket form is the registered route.

***Chart formula, as a lemma.*** In the chart at `p`, `(L_X h)` agrees with
`Dh(X)(v,w) + h(DX v, w) + h(v, DX w)`, i.e. the model-space `lieDerivForm` / `IsKilling` of campaigns 62 and 66.

## ② `lem:killing` (b) coordinate-free

***Statement.*** If `L_X g = 0` on a neighbourhood of `p`, with `g` a metric on `N` and `X p ≠ 0`, then a
`LocalKillingChart` exists.

***Proof.*** The chart formula reduces it to campaign 66's `fm_manifold_killingChart`.

## The C² question, as `r7631` asks

Campaign 66 needed a `C²` manifold only for the section hypothesis on the whole chart. Here the Killing hypothesis
is on a neighbourhood, so it needs the chart representative to be `C¹` on that neighbourhood. RESULT says whether
`C²` remains. The expectation is that it does for the neighbourhood form, because Mathlib's tangent bundle is a `C¹`
bundle only from `C²` onward; and that the pointwise flow-box part does not need it.

***Failable:*** each piece is BUILT, BUILT IN PART, or REPORTED.

***Reachable negative:*** `①`'s likely stop is Mathlib's `mlieBracket` API, its chart formula, and the
`TangentSpace` coercions. If the bracket route stops, the flow-pullback definition is used instead, with the
flow-box chart, and RESULT says which.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves: `lem:killing` is a
P1 theorem, not a row.*

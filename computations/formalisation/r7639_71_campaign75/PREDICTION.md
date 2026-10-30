# `r7639+71.1` — PRE-REGISTRATION: campaign 75, `r7639` ①, does P1's `prop:causal-alignment` need properness? **Registered answer: no.** Properness, and the slice lower limit, follow from the proposition's own hypotheses. Campaign 74's Schwarzschild example does not sit inside them. ⌗ `500` new lines in one probe (band 150–2000 new), ⛔ stop `3500` total. ⌗ p: the slice lower limit with no properness or local-connectedness hypothesis `0.75`, properness derived `0.7`, the curve made inextendible inside the Lean definition `0.4`

*Under `r7639` ①. This registration states its predicted answer before any Lean, with a p. The setting is campaign 74's
`probes/SliceConvergence.lean`, copied in under a new namespace. No Lean was written before this registration.*

## The predicted answer and its argument (`probes/CauchyProperness.lean`)

***Hypotheses, the proposition's own.*** `Θ` is a Cauchy temporal function of `D = I⁻(𝒥⁺)`. That is, `Θ` is temporal on
`D`, and every inextendible causal curve in `D` meets each level set.

***The argument, for a horizon point `q ∈ 𝓗⁺ ⊆ closure D`.***
1. **`I⁻(q) ⊆ D`.** If `x ≪ q`, then `I⁺(x)` is an open neighbourhood of `q`, so it meets `D` in some `d`. Then
   `x ≪ d ∈ I⁻(𝒥⁺)`, so `x ∈ D`. This uses only openness of `I⁺` and transitivity of `≪`.
2. **A timelike curve in `D` ending at `q` is future-inextendible in `D`.** Take, for example, a straight past-directed
   segment from `q` along `−T`, run toward `q`. Its only limit point is `q`, and `q ∉ D`.
3. **`Θ → ∞` along it.** The Cauchy property says it meets every level. Since `Θ` increases along it, every value
   above its starting value is attained.
4. **Properness.** Pick `r` on the curve with `Θ(r) > T`. Then `I⁺(r)` is a neighbourhood of `q`, and every
   `x ∈ I⁺(r) ∩ D` has `Θ(x) > Θ(r) > T`, by campaign 74's `sc_temporalD_chr`. So `Θ → ∞` at `q`. This is
   campaign 74's `SublevelProper` at `q`.
5. **The slice lower limit, with no further hypothesis.** The tail of the curve lies in any given neighbourhood `U` of
   `q`. By the intermediate value theorem on that tail, it meets every level `S_τ` for `τ ≥` the tail's starting
   value. So `q ∈ KLi(S_τ)`.
   - **This needs neither properness nor local connectedness.** Both hypotheses of campaign 74 drop out.

***Why campaign 74's example fails.***
- Any spacetime that contains the bifurcation sphere contains a neighbourhood of it. That neighbourhood includes points
  of the white-hole region IV.
- Those points lie in `I⁻(𝒥⁺) = D`, and there Schwarzschild `t` is not a temporal function.
- In a spacetime that excludes IV, for instance one built from regions I and II, or a collapse spacetime, the sphere is
  not in `M`. In region I, `t → ∞` at the future horizon, consistent with step 4.
- So the example does not satisfy the proposition's hypotheses, and P1's sentence needs no amendment on this account.

## What is registered for Lean

***Statement.***
- `q ∈ 𝓗⁺ ⟹ I⁻(q) ⊆ D`.
- A future-directed timelike curve in `D` with limit `q` meets every level, from the Cauchy property.
- Hence properness, and the slice lower limit with no added hypotheses.
- Then `KLi(S_τ) = KLs(S_τ) = 𝓗⁺` under the proposition's hypotheses plus campaign 72's `hcl` and `hint`.

***Failable:*** each piece is BUILT, BUILT IN PART, or REPORTED.

***Reachable negative.*** Campaign 60's `InextCausalCurve` needs a curve on all of `ℝ`, inextendible in *both*
directions. Extending the timelike curve into the past without an endpoint in `D` may be heavy. If it is, the Cauchy
property is stated in its future-inextendible form. That form is equivalent in the standard theory, since any
future-inextendible causal curve extends to an inextendible one. RESULT says so, and the "properness is a hypothesis"
gap shrinks to that equivalence.

***A registered negative also counts.*** If the argument fails, RESULT gives the failing step and a counterexample inside
the hypotheses, as `r7639` asks.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

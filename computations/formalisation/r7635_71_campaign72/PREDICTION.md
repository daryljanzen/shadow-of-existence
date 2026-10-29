# `r7635+71.2` — PRE-REGISTRATION: campaign 72, `r7635` ②, the convergence `∂J⁻(O(τ)) → 𝓗⁺` and the tangency clause of `prop:causal-alignment` in its convergence form. ⌗ `700` new lines in one probe (band 250–2500 new), ⛔ stop `4500` total. ⌗ p: lower limit `𝓗⁺ ⊆ liminf ∂J⁻(O(τ))` `0.75`, upper limit `limsup ⊆ 𝓗⁺` `0.6`, the clause stated and proved in Kuratowski form `0.5`

*Under `r7635` ②. The setting is campaign 60's `CausalStructure.lean`: `D = I⁻(𝒥⁺)`, `𝓗⁺ = ∂J⁻(𝒥⁺)`, and the
observer `O` with `I⁻(range O) = D`. It adds campaign 63's `int J⁻ ⊆ I⁻` where the Lipschitz relation is needed.
No Lean was written before this registration.*

## ① The lower limit (`probes/HorizonConvergence.lean`)

***Statement.*** Every `p ∈ 𝓗⁺` is a limit of points `pₙ ∈ ∂J⁻(O(τₙ))`, with `τₙ → ∞`.

***Hypothesis.*** The paper's own `closure J⁻(𝒥⁺) = closure D`, taken as a stated hypothesis if it is not derivable.

***Route.***
- Since `p ∈ closure D`, pick `xₙ ∈ D` with `xₙ → p`. Each `xₙ ∈ I⁻(O(τₙ))` for some `τₙ`.
- `p ∉ J⁻(O(τ))` for every `τ`, because `J⁻(O(τ)) ⊆ D` and `D ∩ 𝓗⁺ = ∅` (campaign 60).
- So the segment from `xₙ` to `p` meets `∂J⁻(O(τₙ))`, by connectedness of the segment, at a point within
  `‖xₙ − p‖` of `p`.
- `τₙ` can be taken increasing, using `J⁻(O(τ))` monotone in `τ`.

## ② The upper limit

***Statement.*** If `yₙ ∈ ∂J⁻(O(τₙ))`, `τₙ → ∞` and `yₙ → y ∈ M`, then `y ∈ 𝓗⁺`.

***Route.***
- `y ∈ closure D`.
- If `y ∈ D`, then `y ∈ I⁻(O(τ))` for some `τ`, which is open. So eventually `yₙ ∈ I⁻(O(τ)) ⊆ I⁻(O(τₙ))`,
  and `I⁻(O(τₙ)) ⊆ int J⁻(O(τₙ))`, contradicting `yₙ` lying on the boundary.
- So `y ∈ closure D ∖ D`. That is `𝓗⁺`, given `int J⁻(𝒥⁺) = D`, from campaign 63's `int J⁻ ⊆ I⁻` or stated.

## ③ The tangency clause

***Statement.*** The past cones `∂J⁻(O(τ))` converge to `𝓗⁺` in the Kuratowski sense as `τ → ∞`, which is ① and ②
together. The slices `S_τ`, for an adapted `Θ`, accumulate on `𝓗⁺` in the same sense.

***Scope.*** "Asymptotically tangent", in a differential sense, needs the generators' geodesic regularity, which is
campaign 71. RESULT states which form is proved.

***Failable:*** each piece is BUILT, BUILT IN PART, or REPORTED.

***Reachable negative:*** `①` needs the segment from `xₙ` to `p` to lie in `M`, so take `M` convex near `p`, or work
in a ball. `②` needs `int J⁻(𝒥⁺) = D` in campaign 60's C¹-chain relation; if only the Lipschitz version is
available, the bridge is stated. The differential tangency is REPORTED against campaign 71 if `71` does not close.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

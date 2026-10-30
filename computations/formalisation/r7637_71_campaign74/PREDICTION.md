# `r7637+71.2` — PRE-REGISTRATION: campaign 74, `r7637` ④, the slice lower limit `𝓗⁺ ⊆ KLi(S_τ)`. ⌗ `400` new lines in one probe (band 150–1500 new), ⛔ stop `3000` total. ⌗ p: `Θ → ∞` on approach to `𝓗⁺` from the Cauchy property `0.5`, slice lower limit `0.45`

*Under `r7637` ④. The setting is campaign 72's `probes/HorizonConvergence.lean`, copied in under a new namespace,
with campaign 60's `IsCauchyTemporal` definitions. No Lean was written before this registration.*

## ① `Θ` blows up at the horizon (`probes/SliceConvergence.lean`)

***Statement.***
- Let `Θ` be a Cauchy temporal function on `D`, so every inextendible causal curve in `D` meets each level set
  exactly once.
- Then for every `p ∈ 𝓗⁺` and every `T`, there is a neighbourhood `U` of `p` with `Θ > T` on `U ∩ D`.

***Hypotheses.*** If the clean derivation needs it, a properness hypothesis is stated instead, and RESULT says so: for
example that `Θ⁻¹((−∞, T])` is closed in `M`, or that the region below a level set has closure inside `D`.

## ② The slice lower limit

***Statement.*** `𝓗⁺ ⊆ KLi(τ ↦ S_τ)`.

***Route.***
- For `p ∈ 𝓗⁺` and a neighbourhood `U`, take `x ∈ D ∩ U`.
- By ①, there are points of `D ∩ U` with arbitrarily large `Θ`.
- A connected path in `D ∩ U` between `x` and such a point, with `Θ` continuous, meets every intermediate level
  `S_τ`. This is the intermediate value theorem.
- This needs `D ∩ U` path-connected near `p`, for example a convex `U` meeting `D` in a connected set. That is stated
  if it is not derivable.

***Failable:*** each piece is BUILT, BUILT IN PART, or REPORTED.

***Reachable negative:*** `①`'s likely stop is deriving the blow-up from the Cauchy property, which needs an
inextendible causal curve in `D` approaching `p`, i.e. past-directed limit curves from `𝓗⁺`. If it stops, the
properness hypothesis stands in. `②`'s likely stop is the local connectedness of `D` near `𝓗⁺`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

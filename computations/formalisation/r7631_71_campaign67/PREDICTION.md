# `r7631+71.1` — PRE-REGISTRATION: campaign 67, `r7631` ①, the ∂J⁻ generator extended past-inextendibly inside ∂J⁻, with the time functional working across the compact exhaustion; stretch: geodesics of `g`. ⌗ `1200` lines of new material in one probe (band 400–3500 including the copied base), ⛔ stop `4500`. ⌗ p: per-compact `τ` from local `τ`s `0.5`, past-inextendible generator `0.3`, geodesics `0.1`

*Under `r7631` ①. The setting is campaign 65's `probes/CausalConcat.lean`, copied in under a new namespace. No Lean
was written before this registration.*

## ① The time functional across the exhaustion (`probes/CausalGenerator.lean`)

***What campaign 65 needs.*** Campaign 65 takes, for each compact set `K_j`, a linear `τ_j` positive on the cones
over `K_j`. No single linear `τ` serves a large `K`.

***The replacement.*** Cover `K_j` by finitely many small balls, each carrying campaign 63's local
`τ₀ = −g_{x₀}(·, T x₀)`. Redo the uniform reparametrisation piecewise: a curve in `K_j` splits into finitely many
sub-arcs, each inside one ball, using the Lebesgue number. Each sub-arc gets the local bound, so there is one
Lipschitz constant over `K_j`.

***Statement.*** The closedness of the causal relation on any compact `K ⊆ M`, `cc_isClosed_lstepIn` with no
hypothesis on `τ`.

## ② The past-inextendible generator

***Statement.*** For `p ∈ ∂J⁻(A) ∖ closure A`, under campaign 65's diamond condition on each compact set of the
exhaustion, or a global-hyperbolicity-flavoured hypothesis (stated if used), there is a past-directed causal curve
from `p` that:
- lies in `∂J⁻(A)`;
- is achronal;
- is either past-inextendible, or reaches `closure A`.

***Route.*** Iterate campaign 63's boundary generator step through the exhaustion, using campaign 65's
`cc_exit_step` and ①.

## ③ Stretch: geodesics of `g`

Define the Christoffel symbols in the chart. Show that a generator, if it is `C²`, is a null pregeodesic.

***Failable:*** each piece is BUILT, BUILT IN PART, or REPORTED.

***Reachable negative:*** `①`'s likely stop is the Lebesgue-number splitting of a Lipschitz causal curve into
finitely many sub-arcs, each in one ball. `②` may need the diamond condition on every compact set, as a
hypothesis. `③` is expected to stop at the regularity of generators: the generators here are only Lipschitz, and
the geodesic property needs the maximality of null geodesics. If so, RESULT names that.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

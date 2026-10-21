# `r7443+71.43` — PRE-REGISTRATION: campaign 47, row 101's one open check — the `23.254 %` ratio `∫_{π/4}^{π/2} sin^{−2/3} / ∫_0^{π/2} sin^{−2/3}` to the receipt's tolerance. ⌗ `500` lines (band 250–1100), ⛔ stop `1600`. ⌗ p `0.40`

*Under `r7443`. Row 101 is the last LIMIT row (campaign 46). No Lean was written before this registration.*

## ① The piece: `probes/Row101Ratio.lean`

***Route.***
- The integrand `g(θ) = sin^{−2/3}θ` is decreasing and convex on `(0, π/2]`.
- The full integral is `½B(1/6, 1/2)`. Either use that closed form (Mathlib has `Real.Beta`/`Complex.betaIntegral`
  and Gamma values), or bracket it as below.
- The near-zero piece `∫_0^a` is bracketed with `sin θ ∈ [θ − θ³/6, θ]`. That gives
  `∫_0^a θ^{−2/3} ≤ ∫_0^a g ≤ ∫_0^a (θ − θ³/6)^{−2/3}`, and the second is bounded in closed form.
- The rest is bracketed by convexity on a uniform mesh: the trapezoid sum is an upper bound and the midpoint sum a
  lower bound. Sines come from Taylor brackets and `x^{−2/3}` from rational brackets of cube roots; every
  inequality is over ℚ and checked by `decide +kernel` or `norm_num`.

***Target.*** `|ratio − 0.23254| <` the receipt's tolerance, read from the receipt, which is about `4·10⁻⁵`
relative. ***Then the whole row `→ DONE`.***

***Failable:*** BUILT (the bracket is inside the tolerance), BUILT IN PART (a looser bracket, with its width
stated), or REPORTED. p `0.40`. ***Risk:*** the kernel cost of the mesh needed for `O(h²)` width at about `4·10⁻⁵`,
estimated at 100–200 nodes.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

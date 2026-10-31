# `r7641+71.2` — PRE-REGISTRATION: campaign 77, `r7641` ①, the causal-`P` bootstrap for a merely Lipschitz start, by measuring time along the curve with `T` instead of the curve parameter; then the tangent hyperplane of `𝓗⁺`, where it exists, as the null hyperplane of the generator. ⌗ `600` new lines in one probe (band 200–2500 new), ⛔ stop `5000` total. ⌗ p: Lipschitz-start bootstrap `0.5`, generator theorem with the C¹-start hypotheses removed `0.45`, tangent hyperplane `0.55`

*Under `r7641` ①. The setting is campaign 76's `probes/ConoidBootstrap.lean`, copied in under a new namespace. No Lean
was written for this campaign before this registration. Campaign 76 does not use `IsTemporal`, so the vacuity
finding in `r7641+71.1` does not touch it.*

## ① The Lipschitz-start bootstrap (`probes/LipschitzBootstrap.lean`)

***The gap.*** Campaign 76's `cb_small_t` needs `γ′ → u` at `0`. For a merely Lipschitz start, its iteration needs
`limsup (−g(γ′,T))/(−g(P,T)/t) < 2`, and the parameter `t` does not give that.

***The registered route.*** Replace `t` by the `T`-arclength `s(t) = ∫₀ᵗ −g(γ′,T)`. This needs no reparametrisation
of the curve.
1. `‖γ(t) − p‖ ≤ C s(t)`, since `−g(w,T) ≥ c‖w‖` for causal `w` near `p`.
2. `−g(P(γ t),T) ≥ (1 − o(1)) s(t)`, since `P(x) = (x − p) + o(‖x − p‖)` (`D exp⁻¹(p) = id`) and
   `−g_p(γ(t) − p, T p) = ∫ −g_p(γ′, T p)`. This needs no causality of `P`.
3. Campaign 76's `cb_near_conoid` gives `(Q∘γ)′ ≤ s′·Q⁺/((1 − ε)s)` a.e.
4. So `Q⁺/s^α` with `α = 1/(1 − ε) < 2` is non-increasing where `Q > 0`. It tends to `0` at `s → 0`, since
   `Q = O(s²)`. Hence `Q ∘ γ ≤ 0`.

***Statement.*** `cb_causal_in_conoid`, with `u`, `hd0` and `hC1` removed. Then `cb_H_generator_null_geodesic` with the
same hypotheses removed: a Lipschitz causal curve from `p` in `𝓗⁺`, inside the small ball and avoiding `p` after
time `0`, is a null pregeodesic on the conoid.

## ② The tangent hyperplane of `𝓗⁺`

***Statement.*** At a point `x ≠ p` of a generator from `p`, every C¹ curve `c` in `𝓗⁺` through `x = c 0`, near `x`,
has `DQ(x)(c′(0)) = 0`. Where `𝓗⁺` is differentiable at `x`, its tangent hyperplane is therefore `ker DQ(x) = P(x)^⊥`,
the null hyperplane of the generator.

***Route.***
- Near `x`, points with `Q < 0` have a future `exp⁻¹`, by continuity of `g_p(exp⁻¹·, T p)`. So they lie in `I⁺(p)`
  (`cb_chr_of_Q_neg`), and achronality (`cb_H_achronal`) excludes them from `𝓗⁺`.
- So `Q ≥ 0` on `𝓗⁺` near `x`, with `Q(x) = 0`. The derivative along any such curve therefore vanishes.

***Not attempted, with the reason.***
- The reverse inclusion "`𝓗⁺` locally equals the conoid" is not a consequence. Horizons can be non-differentiable on
  dense sets (Chruściel–Galloway).
- `②` is the correct one-sided statement, and it is the only one slice tangency needs (`r7641+71.4`).

***Failable:*** each piece is BUILT, BUILT IN PART, or REPORTED.

***Reachable negative.*** Step 2's `o(1)` needs a uniform first-order expansion of `exp⁻¹` at `p`. If that is heavy,
RESULT states the bootstrap with that expansion as a named hypothesis.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

# `r7641+71.4` — PRE-REGISTRATION: campaign 79, `r7641` ③, slice tangency. **Registered answer: P1's tangency clause does not follow from its hypotheses.** "The tangent hyperplanes of `S_τ` become asymptotically tangent to the generators, `∇Θ` aligning with the generator in direction" fails for some adapted Cauchy temporal `Θ` in P1's own setting. It holds under an added hypothesis, which P1's two worked slicings satisfy. ⌗ `900` new lines in one probe (band 300–3000 new), ⛔ stop `4000` total. ⌗ p: a model meeting the repaired hypotheses with `𝓗⁺ ≠ ∅` `0.45`, the failing sequence in it `0.6` given the model, the null-frame reduction `0.5`, the paper counterexample in P1's collapse setting surviving 69's reading `0.7`

*Under `r7641` ③. A new probe, `probes/SliceTangency.lean`, in campaign 78's setting with the repaired `IsTemporal`
(C¹ on `M` only, `r7641+71.1`). No Lean was written for this campaign before this registration.*

## The counterexample, on paper, in P1's setting

***Where it lives.*** The exterior of an Oppenheimer–Snyder collapse. Near a late horizon point it is Schwarzschild
region I in Kruskal coordinates: `U < 0`, `V > 0`, `𝓗⁺ = {U = 0}`, generators `∂_V`, and
`g = −F dU dV + r² dΩ²`. With no angular dependence, `Θ` is temporal iff `Θ_U > 0` and `Θ_V > 0`. Alignment with the
generator means `Θ_V/Θ_U → 0`.

***The construction.***
1. **The base.** Start from P1's `Θ₀ = a(u + ηr)`.
2. **A bounded `V`-bump.** Add `β(V)`, non-decreasing, with `β′ ≥ 1` on a band of `V`, and constant outside it. The
   band lies after the body's surface crosses `𝓗⁺`, so the bump is in vacuum.
3. **A bounded `U`-term, cut off in `V`.** Add `χ(V)·B(U)`, with `χ ∈ [0,1]` supported where `β′ ≥ 1`. The term `B`
   is bounded and makes `Θ_U = O(1)` on thin bands `U ≈ U_n → 0`:
   - `B′ = −(4Ma/s)(1 − w(s)) + K₀`, with `s = −U`;
   - `w = s_n` on intervals of length `s_n 2^{−n}` around `s_n`, and `w = 1` elsewhere;
   - `K₀ > 2·sup|aη r_U|`.
4. **Temporality survives.** `Θ_U > 0` holds in both regimes of `χ`, and `Θ_V ≥ 1 − ε·sup|χ′| > 0`.
5. **The Cauchy property survives.** The added terms are bounded, so along every inextendible causal curve `Θ` still
   ranges over `ℝ`, and strictly.
6. **Adaptation.** The `U`-band misses a static observer at large `r`. The bump `β` is undone by `Θ ↦ h∘Θ`, which
   changes no level set and no gradient direction.

***The failure.*** At `x_n = (U_n, V*)` with `χ(V*) = 1`, both `Θ_U` and `Θ_V` are `O(1)`. So the level-set tangent
planes stay transverse to `∂_V`. Yet `x_n → (0, V*) ∈ 𝓗⁺` and `Θ(x_n) → ∞`.

***The gap in P1's proof.*** "`S_τ` meets `∂J⁻(O(τ))` transversely" constrains `S_τ` only along that intersection, not
its tangent planes elsewhere near `𝓗⁺`.

## What restores the clause

***The reduction.*** Take a null frame `ℓ` (along the generators), `n` (transverse), and spatial `e_i`, near `q ∈ 𝓗⁺`.
- Temporality gives `Σ dΘ(e_i)² < 2·dΘ(ℓ)·dΘ(n)`.
- So alignment holds **iff** `dΘ(ℓ)/dΘ(n) → 0`.

***A sufficient hypothesis.*** `dΘ(ℓ)` bounded and `dΘ(n) → ∞` near `𝓗⁺`.
- Stationary `t`: `t_V = 2M/V` bounded, `t_U = 2M/|U| → ∞`.
- Retarded `a(u + ηr)`: `Θ_V → 0`, `Θ_U ≈ 4Ma/|U|`.
- **For 69:** the clause stands for those two slicings. For general `Θ`, it needs that hypothesis or the ratio
  condition.

## What is registered for Lean (`probes/SliceTangency.lean`)

1. **The model.**
   - 2D Minkowski with `J` the Rindler worldline `O(σ)`, `U·V = −1`, and `M = ℝ²`.
   - Then `D = {U < 0}`, `𝓗⁺ = {U = 0}`, and every hypothesis of the repaired `cp_causal_alignment` holds.
   - `Θ₀ = −log(−U) + V`, reparametrised along `O`, is future-Cauchy temporal on `D` (non-vacuity), and `∇Θ₀`
     aligns.
2. **The failure.** With `F(s) = −log s − sin(log s) − s` and `Θ = F(−U) + V`:
   - `Θ_U = (1 + cos log s)/s + 1 ≥ 1`;
   - at `s_m = e^{−(2m+1)π}`, `dΘ = dU + dV`;
   - so `dΘ(ℓ)/‖dΘ‖` stays bounded away from `0` along `x_m → q ∈ 𝓗⁺`, while `Θ(x_m) → ∞`.
3. **The reduction**, as linear algebra.

***Failable:*** each piece is BUILT, BUILT IN PART, or REPORTED.

***Reachable negative.*** Proving the future Cauchy property in the model needs `U` and `V` monotone along piecewise
C¹ causal curves, then a monotone-bounded convergence argument. If that is heavy, RESULT builds the failure (2) and
the reduction (3), and states the model's Cauchy property as REPORTED with the step that stopped.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

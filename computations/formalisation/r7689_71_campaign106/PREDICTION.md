# `r7689+71.1` — PRE-REGISTRATION: campaign 106, `r7689` ②, **row 5, `cor:stationary` on `N`: if `S.H J` is a Killing horizon (rigidity's conclusion, taken as the hypothesis P1 cites), every pair of events on one generator is metrically coincident, through the whole `lem:killing`; witnessed on Schwarzschild's `∂J⁻(𝒥⁺)` on `W`.** ⌗ `550` new lines (band 300–1200). p `0.85` for ①, `0.5` for ②, `0.5` for the whole. **Expected stop:** the Lie derivative of `∂_t` carried onto the `Opens` subtype `W`

*Registered before any Lean. The new probe is `probes/StationaryHorizon.lean`, a copy of campaign 100's
`SchwarzschildConformal.lean` (which has `MSpacetime`, `se_S` on `W` and `sx_prop_causal_alignment`). Into it go
campaign 96's `KillingWhole.lean` section (`kw_`, `kg_`, `kl_` and their `ld_` base) and campaign 97 ③'s `sq_`
Killing facts from `SchwarzschildKilling.lean`. Clashes in the copied kit (`hRep`, `chartRep`, `ld_`) keep one copy.
Everything new is prefixed `st_`.*

## ① The corollary on `N` — `150` lines, p `0.85`

***`S.IsKillingHorizon X Hs`*** is rigidity's conclusion, stated for an `MSpacetime`. It holds when `X` is a vector
field that:
- is `C¹` near `Hs`, and non-zero on it;
- has `L_X g = 0` near `Hs`;
- through every point `p ∈ Hs`, has an integral curve inside `Hs`;
- is null somewhere on each such curve.

The metric's chart representative is also required to be differentiable near `Hs`, as `kw_lemma_killing_whole`
asks.

***`st_cor_stationary`:*** if `S.IsKillingHorizon X (S.H J)`, then along every generator `γ` on `[a, b]` inside `𝓗⁺`,
all of `kw_lemma_killing_whole`'s conclusions hold:
- `g(γ′, γ′) = 0`;
- `kg_Related` for every pair, which is metric coincidence;
- for the horizon splitting, `Δx = 0` and `Δτ = 0`.

***Stated plainly:***
- **Rigidity stays a hypothesis, as P1 cites it** (Hawking, with analyticity). Proving it needs the Einstein equations,
  which are not in the kit.
- **"Stationary" has no formal content** beyond invoking rigidity.

## ② The witness on an actual event horizon — `400` lines, p `0.5`

***`st_witness`:*** on Schwarzschild on `W`, `𝓗⁺ = ∂J⁻(𝒥⁺)` (`sx_prop_causal_alignment`) is a Killing horizon for
`χ = ∂_t = (V∂_V − U∂_U)/4M`:
- `L_χ g = 0`, from `sq_`'s Killing fact carried onto `W`;
- on `𝓗⁺ = {U = 0, V > 0}`, `χ = V∂_V/4M`, which is non-zero and null, with integral curves `V = V₀ e^{s/4M}` inside
  `𝓗⁺`.

So `st_cor_stationary` applies: two events `(0, V₁) ≠ (0, V₂)` on `∂J⁻(𝒥⁺)` are metrically coincident.

***Expected stop:*** `lieDeriv` on the subtype `W`. Its chart is the inclusion (`se_dchart`), so the Lie derivative
should reduce to `P`'s, but that reduction is the step.

***Fallback, p `0.75`:*** the witness on the model plane's Kruskal set, with `𝓗⁺` identified as `{U = 0}` but not
as `∂J⁻(𝒥⁺)`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

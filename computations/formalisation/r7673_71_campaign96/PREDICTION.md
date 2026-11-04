# `r7673+71.1` — PRE-REGISTRATION: campaign 96, `r7673`. **`lem:killing` 4d to BUILT:** global `Δx = 0` along a whole Killing-horizon generator, read through ruling 2's adapted splitting, so that `lem:killing` is whole. ⌗ `250` new lines (band 100–700), p `0.85`. **Expected stop: none.** The second likeliest difficulty is a linear form `dλ` with `dλ(X) = 1` chosen along `γ`, which needs `X ≠ 0` and finite dimension

*Under `r7673`. A new probe, `probes/KillingWhole.lean`, from campaign 95's `KillingGenerator.lean` with campaign 94's
`AdaptedSplitting` and `ac_metric_singularity_along` copied in. No Lean was written before this registration.*

## Why 4d first

It is the cheapest BUILT IN PART row, and 69 prefers it because it finishes `lem:killing`. The other rows each need a
Schwarzschild instance as an `MSpacetime`:
- 3a and 3b need the EF chart and the horizon `r = r_h`;
- 8 needs Kruskal with `𝒥⁺`;
- 5 rests on rigidity, which is a hypothesis.

Their prices are about `800–1500` lines at p `0.3–0.4` in the refreshed inventory.

## The construction

***The splitting along `γ`,*** on ruling 2's reading for a Killing horizon: the adapted time is `λ`, and the lapse is
`|χ|`.
- `n s := √(max 0 (−g(X, X)))`, which is `|X|`, and is `0` along `γ` by stage 2's (a).
- `dt s` is a linear form with `dt s (X (γ s)) = 1`. It exists because `X ≠ 0` (`kw_dλ_exists`, by finite dimension).
- `h s := g_{γ s} + n² dt ⊗ dt`, which is `g_{γ s}` on `γ`.

***Checks.***
- `g = h − n² dt²` holds.
- `h(γ′, γ′) = g(γ′, γ′) = 0 ≥ 0`, by stage 2's (a).

***`kw_lemma_killing_whole`.*** Under stage 2's hypotheses, along `[a, b]`:
1. stage 2's (a), (b) and (c);
2. `Δx = ∫ √h(γ′, γ′) = 0` along the **whole** generator;
3. `Δτ = ∫ n |dt(γ′)| = 0`, from `ac_metric_singularity_along`.

So every field of `MetricallyCoincident` holds globally on ruling 2's reading.

## Stated in advance

- `Δx` depends on the splitting. This one is the horizon's own, with lapse `|χ|`.
- `h` here is `g` on `γ`. It is not positive semidefinite off `γ′`, and the ruling asks only that `h(γ′, γ′) ≥ 0`.
- This matches P1's proof, where on a Killing horizon `ds² = |χ|² dλ²` and the spatial leg along the generator is what
  vanishes. RESULT will say so plainly.

## The witness

Stage 2's Rindler generator `(0, e^s)` for `s ∈ [0, 10]`: `Δx = 0`, `Δτ = 0`, and `γ 0 ≠ γ 10`.

***Failable:*** BUILT, BUILT IN PART, or REPORTED.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

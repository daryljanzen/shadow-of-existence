# `r7673+71.2` — RESULT: campaign 96, **`lem:killing` 4d BUILT**. Global `Δx = 0` and `Δτ = 0` along a whole Killing-horizon generator, through the horizon's own adapted splitting. **`lem:killing` is whole** on ruling 2's reading. ⌗ `3533` lines in one probe (`326` new, band 100–700). ⌗ p `0.85` came true

*Against `PREDICTION.md` (`r7673+71.1`). 71 re-ran `lake env lean probes/KillingWhole.lean`. It exits 0 with no errors
and no warnings. All `182` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`: `172` copied and
`10` new. The forbidden-token grep is clean, and the probe imports only Mathlib. `check_no_sorry.py` reports ALL 29
THEOREMS COMPILE. The probe copies campaign 95's `KillingGenerator.lean` and campaign 94's splitting material,
adapted to a raw `g`.*

## The splitting

`kw_horizonSplitting` is a `kw_AdaptedSplitting` along `γ` on `[a, b]`, built from three pieces:
- **the lapse** `n = √(max 0 (−g(X, X)))`, which is `|X|`;
- **the adapted time** `dt` with `dt(X) = 1`. It exists by `kw_dλ_exists`, using finite dimension and `X ≠ 0`;
- **the spatial part** `h = g + n² dt ⊗ dt`.

What holds for it:
- `kw_split`: `g = h − n² dt ⊗ dt`, everywhere.
- `kw_h_X`: `h(X, X) = max (g(X, X)) 0 ≥ 0`.

## `kw_lemma_killing_whole`

It takes exactly stage 2's hypotheses. For the horizon splitting `σ`, it concludes:
- stage 2's (a), (b) and (c), and `kg_deltaTau = 0`;
- `σ.h s = g_{γ s}` and `σ.h(γ′, γ′) = 0` on `[a, b]`;
- **`σ.Δx = ∫ₐᵇ √h(γ′, γ′) = 0` along the whole generator;**
- **`σ.Δτ = ∫ₐᵇ n |dt(γ′)| = 0`,** by `kw_metric_singularity_along`, with `a = b` handled separately.

## The witness, `kw_witness`

It uses the Rindler generator on `[0, 10]`.
- `σ` is the horizon splitting itself.
- `Δx = 0` and `Δτ = 0`.
- `∫₀¹⁰ dt(γ′) = 10`, so the Killing parameter separates the endpoints and the result is not vacuous.
- `γ 0 ≠ γ 10`, and the two endpoints are related by stage 2's (b).

## Stated in advance, and holding

- The splitting is the horizon's own, with lapse `|χ|` and adapted time `λ`. `Δx` is relative to it.
- `h` equals `g` on `γ`. It is non-negative on `γ′`, as the ruling requires, but not positive semidefinite in every
  direction.

## Marks

`lem:killing` 4b, 4c and 4d are **BUILT**, so **`lem:killing` is whole**: every field of `MetricallyCoincident` holds
along a whole generator, on the manifold.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

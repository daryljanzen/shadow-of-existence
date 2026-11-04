# `r7677+71.2` — RESULT: campaign 98 ③ and ④, **both slicings of `lem:alignment` align with the generator on Schwarzschild, on the manifold, at every future horizon point. BUILT.** ④′, the retarded slicing's Cauchy property, is REPORTED. ⌗ `8565` lines in one probe (`556` new). ⌗ p: ③ `0.7` came true; ④ `0.6` came true; ④′ `0.2` was not attempted

*Against `PREDICTION.md` (`r7677+71.1`). 71 re-ran `lake env lean probes/SchwarzschildAlign.lean`. It exits 0 with no
errors and no warnings. All `117` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`: `112`
inherited and `5` new. The forbidden-token grep is clean, and the probe imports only Mathlib. It copies campaign 97's
`SchwarzschildKruskal.lean`.*

## The setting

- The spacetime is campaign 97's `sk_S`: Kruskal, with `g = −F(r) dU dV`.
- Region I is `{U < 0, V > 0}`, which is P1's exterior.
- The approach is along `𝓝[region I] q` at `q = (0, V₀)` with `V₀ > 0`.
- The frame is `ℓ = ∂_V` and `n = (2/F)∂_U`.
- Tangency is local, so this filter is the same on EF's domain `W` from ①②, with the same metric.

## ③ `sa_stationary_aligns` — BUILT

***The slicing.*** `t = 2M(log V − log(−U))`, which is C¹ on region I.

***The horizon point.***
- `q` lies on every static observer's `H`, with `r = 2M`.
- Region I lies inside each observer's `D`.
- `𝓝[region I] q` is a non-trivial filter.

***The limit.***
- The frame hypotheses hold on region I.
- The rate is **`F · (−U)/(2V)` exactly, and it tends to `0`**.
- The limit is `−g_q(ℓ, ·)`, which is **`(F(q)/2) dU`** in the chart.

## ④ `sa_retarded_aligns` — BUILT

***The slicing.*** `Θ = a(u + ηr)` with `u = −4M log(−U)`, for any `a > 0` and `η > 0`.

***The frame and the limit.***
- The frame hypotheses hold eventually near `q`.
- `dΘ(ℓ) = aη r_V → 0`, and `dΘ(n) → ∞`.
- The rate is `F η U²/(2k) → 0`.
- The limit is the same, `(F(q)/2) dU`.

***No bound on `η` is needed for tangency.*** The frame hypothesis needs `k = 4M h′(r) − ηV(−U) > 0`, and `k → 4M h′(2M) > 0`
at the horizon. P1's "`η` small" matters only for temporality on the whole of region I, which is ④′.

## Non-vacuity, `sa_nonvacuous`

- It takes `M = 1`, `V₀ = 1`, `a = η = 1`.
- Both limits equal `(8/e) dU`, which differs from the flat `½ dU`.

## ④′ — REPORTED

The retarded slicing's Cauchy property on region I is not attempted. It needs `Θ_ret` to be temporal on all of region
I, which is where a bound on `η` enters, plus a Cauchy transport. The estimate is over 400 lines.

## Marks

- **8ii-a, both slicings align → BUILT on Schwarzschild, on the manifold.**
- The retarded half of 8ii-b waits on ④′.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

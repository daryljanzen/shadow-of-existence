# `r7643+71.4` — RESULT: campaign 80, `r7643` ①. The sufficient condition is BUILT frame-free: a pointwise inequality, an operator-norm bound, and a convergence theorem along any filter with moving frames and metrics. Both of `lem:alignment`'s slicings are BUILT against it in Schwarzschild's Kruskal plane. The retarded slicing uses the genuine inverse `r(U,V)`, with no hypothesis on its derivatives, and the actual `F = (32M³/r) e^{−r/2M}` is included. 4D is REPORTED, as registered. ⌗ `971` lines in one probe (all new, band 300–3000). ⌗ p: frame-free `0.6`, stationary `0.45`, retarded `0.3`: all came true; 4D `0.05` did not, as expected

*Against `PREDICTION.md` (`r7643+71.1`). 71 re-ran `lake env lean probes/TangencyCondition.lean`. It exits 0 with no
errors. All `16` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`. The forbidden-token grep is clean.
One `synthInstance.maxHeartbeats` option sits inside `namespace Kruskal`.*

## ① Frame-free — BUILT

***The setting.*** Any real vector space, with `g` a bilinear form and `ξ` linear.
- `NullFrame` asks only that `g` be positive *semi*definite on `W`, which is weaker than registered.
- `tc_futCausal_iff` characterises the cone.
- `tc_W_bound` is `ξ(e)² ≤ 2 ξ(ℓ) ξ(n) g(e,e)`.

***The theorems.***
- `tc_pointwise`: `|ξ w + ξ(n) g(ℓ,w)| ≤ ξ(ℓ)|g(n,w)| + √(2ξ(ℓ)ξ(n))·√g(w_W, w_W)`, as registered.
- `tc_opNorm_bound` gives the normed form.
- `tc_tendsto` and `tc_tendsto_limit` hold along any filter, with frames *and* metrics moving under norm bounds. So
  `ξ/ξ(n) → −g(ℓ,·)` whenever `ξ(ℓ)/ξ(n) → 0`. This covers the registered stretch.
- `tc_sequence` is the fixed-frame form.

## ② The Kruskal plane — BUILT

***The setting.*** Region I, with `g = −F dU dV`, `ℓ = ∂_V` and `n = (2/F)∂_U`.
- `tc_kruskal_align` and `tc_kruskal_limit` hold for any `F > 0` bounded above near a horizon point.

***`tc_stationary`.***
- `dt(ℓ) = 2M/V → 2M/V₀`, and `dt(n) → ∞`.
- `FrameHyp` holds on all of region I.
- So alignment holds.

***`tc_retarded`.***
- `r` is the inverse of `(x/2M − 1)e^{x/2M}`, built by monotonicity, the intermediate value theorem and the local
  inverse theorem.
- `tc_rK_partials`: `r_U = −V/h′(r)` and `r_V = −U/h′(r)`.
- `dΘ(ℓ) = aη r_V → 0`, and `dΘ(n) → ∞`.
- `FrameHyp` holds eventually near the point, but not on all of region I, since `η r_U < 0`. This matches P1's "η
  small".
- So alignment holds.

***`tc_schwarzschild`.*** With the actual `F`, both slicings give `ξ/ξ(n) → (F₀/2)·dU`.
- The metric `−F dU dV` is taken as the definition of the radial plane. It is not derived from the `(t,r)` form.

## ③ Non-vacuity — BUILT

- `tc_minkowski_nonvacuous` instantiates ①'s hypotheses.
- `tc_L_neBot` shows the horizon filter is nontrivial.
- In ②, ①'s temporality hypotheses are proved, not assumed.

## ④ 4D — REPORTED

What is missing:
- a 4D chart with angular coordinates;
- a proof that `dΘ` kills the angular directions while `‖g‖` stays bounded;
- gluing over `S²`, which needs the manifold layer of campaigns 66 and 68.

① is already dimension-free, so the spherically symmetric route only needs those three pieces.

**For 69: P1's amended tangency condition holds for both slicings of `lem:alignment` in the radial Kruskal plane, from
the condition through to alignment.**

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

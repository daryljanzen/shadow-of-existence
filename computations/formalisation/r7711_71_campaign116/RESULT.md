# `r7711+71.2` — RESULT: campaign 116, **5b BUILT, both halves. The `r < 0` back-seam region is horizonless with asymptotically flat coefficients. As a geometry in its own right, through a tortoise null chart, its Kretschmann scalar is `48M²/r⁶`, which tends to `0` as `r → −∞`. Maximality is priced in the registration.** ⌗ `17282` lines in one probe (`341` new, inside the registered band of 340–580). ⌗ p `0.55` came true. The expected stop at 5b-ii-② did not occur

*Against `PREDICTION.md` (`r7711+71.1`). 71 ran `lake env lean probes/CircleBackSeam.lean`. It exits 0 with no errors
and no warnings. All `625` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`: `600` inherited and
`25` new. The forbidden-token grep is clean, the probe imports only Mathlib, and `check_no_sorry.py` reads ALL 29
THEOREMS COMPILE. The probe copies campaign 115's `CirclePatches.lean`.*

## 5b-i, the coefficients — BUILT

**`bs_coeffs`:**
- On `r < 0`, `f = 1 − 2M/r > 1`. So `g_tt = −f < 0` and `g_rr = f⁻¹ > 0` everywhere: the region is horizonless.
- As `r → −∞`, `f → 1` and `f⁻¹ → 1`: the coefficients are asymptotically flat.
- Campaign 112's `cy_backseam_schw` already gives `f = coth²(ρ′/2)` at `r = M(1 − cosh ρ′)`.

## 5b-ii, the geometry and K — BUILT

**① The tortoise coordinate:** `bs_rs = r + 2M log(1 − r/2M)` on `(−∞, 0)`.
- Its derivative is `1/f` (`bs_hasDerivAt_rs`), so it is strictly increasing.
- It maps `(−∞, 0)` onto `(−∞, 0)` (`bs_rs_neg`, `bs_rs_surj`). For onto, the explicit lower point is
  `a = −2M((2 + q)² − 1)` with `q = −x/2M`, using `log w ≤ w − 1`.
- Its inverse `bs_ρ` has `ρ′ = f(ρ)` (`bs_hasDerivAt_ρ`).

**② The null chart:** `u = t − r*`, `v = t + r*` on `{v < u}`, with `r = ρ((v − u)/2)`.
- **`bs_SD`:** the warped datum `−f du dv + R²(dθ² + sin²θ dφ²)` with `R = −r = |r|`. Only `R²` enters the metric,
  and the kit's datum asks for `R > 0`.
- **`bs_SD_good`:** all twelve partials follow from `ρ′ = f(ρ)` alone. The expected stop did not occur.

**③ The curvature:**
- **`bs_kretschmann`:** campaign 110's `kr_warped` gives `K = 48M²/r⁶` at every chart point with `sin θ ≠ 0`.
- **`bs_backseam`:** the chart covers every `r < 0`, at `(u, v) = (−r*, r*)`, and `48M²/r⁶ → 0` as `r → −∞`.

## Maximality, priced (in `PREDICTION.md`)

- **(a) Within the chart plane:** every boundary point of `{UV < 1}` lies on `UV = 1`, where `K → ∞`. That gives
  chart-level `C²` inextendibility. 80–150 lines at p `0.85`.
- **(b) As a spacetime:** 2000+ lines at p `< 0.1`. Not attempted.

## Limits

- **`t` is not built as a separate coordinate.** The chart is `(u, v, θ, φ)`, the null form, which is where `K` is
  computed. The `(t, r)` form is the coefficient statement 5b-i.
- **The angular sphere is written in by hand,** as in campaign 110.

## Marks (P2's inventory)

- **BUILT (18):** 1a, 1b, 2a, 2b, 3, 4a, 4b, 5a, 5b, 6a, 6b, 6c, 7a–7e and 8a. **Every formal row is built.**
- **Interpretive:** 6d and 8b. Maximality is priced, with (a) cheap and (b) not attempted.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

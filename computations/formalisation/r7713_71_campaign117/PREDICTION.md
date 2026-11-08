# `r7713+71.1` — PRE-REGISTRATION: campaign 117, **maximality (a): chart-level C² inextendibility of Kruskal's `{UV < 1}`**; with **6d and 8b priced** for a formal core. ⌗ `120` new lines (band 80–150), p `0.85`. **Expected stop:** none; the pieces exist (`kr_schwarzschild`, `kr_rinv_to_zero`, `kr_pow_blowup`)

*Registered before any Lean. The probe is `probes/CircleMaximal.lean`, a copy of campaign 116's
`CircleBackSeam.lean`. Everything new is prefixed `mx_`.*

## Maximality (a): the statement

Let `K(U, V)` be the Kretschmann scalar of the Kruskal chart's coordinate metric at `(U, V, θ, φ)`, with `sin θ ≠ 0`.
`kr_schwarzschild` gives `K = 48M²/rK⁶` on `{UV < 1}`.

| Stage | Statement | Lines | p |
|---|---|---|---|
| ① | `frontier {UV < 1} = {UV = 1}` in `ℝ²`. The closure is `{UV ≤ 1}`: each point with `UV = 1` is the limit of `(tU, V)` as `t → 1⁻` | 30–50 | 0.9 |
| ② | At every frontier point `p`, `𝓝[{UV < 1}] p` is non-trivial, and `K → +∞` along it. As `y → p` inside the domain, `−UV → −1⁺`, so `rK = rinv(−UV) → 0⁺` (`kr_rinv_to_zero`) and `48M²/r⁶ → ∞` (`kr_pow_blowup`) | 40–70 | 0.85 |
| ③ | **Inextendibility:** no function `G` continuous at a frontier point `p` agrees with `K` on `{UV < 1}` near `p`. A `C²` extension of the metric across `p` would make `K` continuous there, so `C²` inextendibility across every finite boundary point of the chart is the formal content | 20–40 | 0.9 |

**The reading:**
- **Sense (a)** is maximality within the Kruskal plane. The domain has no boundary point in `ℝ²` other than
  `UV = 1`, and across that the curvature is unbounded.
- **Sense (b)** is maximality as an abstract spacetime, with no isometric embedding into a larger Lorentzian manifold.
  It stays not formalised. I know of no cheaper route: it needs either geodesic completeness of the ends
  `U, V → ±∞` or an inextendibility criterion, and the kit has neither.

## 6d and 8b, priced for a formal core (not built)

| Row | Its claim | Formal core | Lines | p |
|---|---|---|---|---|
| 6d | "a single analytic curve — hyperbola, circle, hyperbola" and "maximal analytic completion" | **Yes, small.** `r(z) = M(1 + cos z)` with conjugate `s(z) = M sin z` is entire, and `(r − M)² + s² = M²` for every complex `z`. On real `z` that is the circle. On `z = iρ` (with `s = iσ`, `σ = M sinh ρ`) it is the hyperbola `(r − M)² − σ² = M²`, and the same holds on `z = π + iρ′`. The "maximal analytic completion" is the entire function itself; the word "maximal" is interpretive | 40–80 | 0.95 |
| 8b | "the labelling is part of the perspectival construction" | **None.** It is an ontological reading. Its only formal neighbours are 7a (`K` finite at `U = V = 0`) and 8a (`ck_mislabel`), both built | — | — |

**Recommendation:**
- **6d's core is worth building.** It machine-checks the "hyperbola–circle–hyperbola" sentence at almost no cost.
- **8b has no formal core.** With 6d's core built, P2's formalisation closes.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

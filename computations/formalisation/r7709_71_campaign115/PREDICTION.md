# `r7709+71.1` — PRE-REGISTRATION: campaign 115, **6b: the four `r ≥ 0` patches, with the horizons at which they meet, are exactly Kruskal's `{UV < 1}`**; with **5b priced** (not built). ⌗ `350` new lines (band 250–450), p `0.7`. **Expected stop:** 6b-i, inverting `Φ` and `Ψ` on the open quadrants

*Registered before any Lean. The probe is `probes/CirclePatches.lean`, a copy of campaign 114's
`CircleExterior.lean`. Everything new is prefixed `cp_`.*

## Where 6b is stated (69's question)

**On the full domain `{UV < 1}` (`sk_kM ⊆ P = ℝ²`), not on `W`.**
- **The manifold:** Kruskal's own `sk_S`, campaign 97's `MSpacetime` on `Pt` with `M = φ⁻¹{UV < 1}`, is the
  manifold that carries it.
- **The chart:** its global null chart at `p₀` gives `hRep (sk_S hM).g p₀ y = F(y)·gM` at every `y ∈ {UV < 1}`
  (`sk_hRep`).
- **What follows:** the set identity is stated in that chart, and the four patches' metrics are read through
  `sk_hRep`. That covers the two reflected patches outside `W`, so the reflection is no longer coefficient-level
  only.
- **Consistency with campaigns 113 and 114:** on `W`, `sk_hRep` and `se_hRep` give the same `F·gM`, so `cc_pullback`
  and `ce_pullback` carry over.

## The patches

- **The black-hole interior `BH`:** `{Φ(η, t) : η ∈ (0, π), t ∈ ℝ}`, campaign 113's chart.
- **The white-hole interior `WH`:** `{−Φ(η, t)}`. In P2's chart it is `z = η ∈ (−π, 0)` with `r` even (`cy_patches`).
- **The right exterior `RE`:** `{Ψ(ρ, t) : ρ > 0, t ∈ ℝ}`, campaign 114's chart.
- **The left exterior `LE`:** `{−Ψ(ρ, t)}`.
- **The horizons `Hor`:** `{UV = 0}`. That is all four horizon halves and the bifurcation point `U = V = 0`. There,
  `r = 2M` (`sk_rK_eq_two_iff`).

## Stages

| Stage | Statement | Lines | p |
|---|---|---|---|
| 6b-i, onto | Every point of `{UV < 1}` off `UV = 0` is in a patch. For `U, V > 0`: take `r = rK(U, V) ∈ (0, 2M)`, `η = arccos(r/M − 1)` and `t = 2M log(V/U)`. Then `Φ(η, t) = (U, V)`, matched by squares (`s² = UV`, `e^{t/2M} = V/U`) with no square root. For `U < 0 < V`: `ρ = arcosh(r/M − 1)` and `t = 2M log(V/(−U))`. The other two quadrants follow by `(U, V) ↦ (−U, −V)` | 150–250 | 0.75 |
| 6b-ii, the identity | `BH ∪ WH ∪ RE ∪ LE ∪ Hor = {UV < 1}`. Each patch lies in its open quadrant, so the five sets are pairwise disjoint, and `Hor` meets no patch | 60–120 | 0.9 |
| 6b-iii, the metric on `sk_S` | Through `sk_hRep`, all four patches pull back to P2's metrics. `BH` and `WH` give `−4M²cos⁴(η/2) dη² + tan²(η/2) dt²`. `RE` and `LE` give `4M²cosh⁴(ρ/2) dρ² − tanh²(ρ/2) dt²` | 60–120 | 0.85 |

**Expected stop: 6b-i.** It needs `rK < 2M` on the open interior quadrant and `rK > 2M` on the exterior one, from
`hK` being strictly monotone. **Fallback:** if `arccos`/`arcosh` misbehave, use the intermediate value theorem on
`cy_r` and `ce_r`.

**The reading:** "meet at the bifurcation 2-sphere" (l.311) becomes "together with the horizons `UV = 0` at which they
meet", as 69's text now has it.

## 5b, priced (not built)

**The statement:** "the Schwarzschild form for `r < 0`" as a geometry, horizonless and asymptotically flat, with
`K = 48M²/r⁶ → 0` as `r → −∞`.

| Part | What it needs | Lines | p |
|---|---|---|---|
| 5b-i, coefficients | On `r < 0`: `1 − 2M/r > 1`, so `g_tt` never vanishes (horizonless). `1 − 2M/r → 1` as `r → −∞` (the coefficients are asymptotically flat). The back-seam metric equals the Schwarzschild form there (`cy_backseam_schw`, already built) | 40–80 | 0.95 |
| 5b-ii, the geometry and `K` | Null coordinates `u = t − r*`, `v = t + r*` with the tortoise `r* = r + 2M log(1 − r/2M)` on `r < 0`. That is strictly increasing, with range `(−∞, 0)`. The metric is `−f du dv + r² dΩ²`, and campaign 110's `kr_warped` then gives `K = 48M²/r⁶ → 0` | 300–500 | 0.55 |

- **Total:** 340–580 lines, at p `0.55` (`0.95` for 5b-i alone).
- **Expected stop:** the inverse of `r*` and its derivatives in `(u, v)`, the analogue of `rK` for `r < 0`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

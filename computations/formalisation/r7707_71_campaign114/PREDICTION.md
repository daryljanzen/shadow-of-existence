# `r7707+71.1` — PRE-REGISTRATION: campaign 114, **4b: the Region I chart pulled back from the Kruskal manifold**, so `prop:region_I_metric` is a pullback as the interior now is; with **6b priced** (not built). ⌗ `300` new lines (band 200–450), p `0.85`. **Expected stop:** none; the method is campaign 113's

*Registered before any Lean. The probe is `probes/CircleExterior.lean`, a copy of campaign 113's `CircleChart.lean`.
Everything new is prefixed `ce_`.*

## The reading

**The manifold is `se_S` on `W = {V > 0, UV < 1}`, as in campaign 113.** Region I, the right exterior
`{U < 0 < V}`, lies in `W`.

**The map is `Ψ(ρ, t) = (−σ(ρ)e^{−t/4M}, σ(ρ)e^{t/4M})`, with `σ(ρ) = sinh(ρ/2)·e^{r/4M}` and `r = M(1 + cosh ρ)`.**
- **Checked in advance:**
  - `UV = −σ² = −sinh²(ρ/2)e^{r/2M} = −hK(r)`, since `r/2M − 1 = sinh²(ρ/2)`;
  - `σ′ = e^{r/4M}cosh³(ρ/2)/2`;
  - `−F dU dV` pulls back to `F σ′² dρ² − F σ²/(16M²) dt²`;
  - `F σ′² = 4M²cosh⁴(ρ/2)` and `F σ²/16M² = tanh²(ρ/2)`;
  - so `Ψ*g = 4M²cosh⁴(ρ/2) dρ² − tanh²(ρ/2) dt²`, which is P2's `eq:Region_I_metric` (radial part).

## Rows

| Stage | Statement | Lines | p |
|---|---|---|---|
| 4b-① | For `ρ > 0`, `Ψ(ρ, t) ∈ W` with `U < 0`, and `rK(Ψ) = M(1 + cosh ρ)`. `Ψ` is injective on `(0, ∞) × ℝ` | 80–150 | 0.9 |
| 4b-② | With `∂_ρΨ` and `∂_tΨ` as `HasDerivAt`, through `se_hRep`: `g(∂_ρ, ∂_ρ) = 4M²cosh⁴(ρ/2)`, `g(∂_t, ∂_t) = −tanh²(ρ/2)`, `g(∂_ρ, ∂_t) = 0`. These are also P2's Schwarzschild exterior coefficients, `−(1 − 2M/r)` and `(1 − 2M/r)⁻¹(dr/dρ)²` (campaign 112's `cy_regionI_schw`) | 120–250 | 0.85 |
| 4b-③ | Region I's two continuations `z = ±iρ` give the same `r`. The `−iρ` branch is the left exterior `{U > 0 > V}`, which is not in `W`. That branch is stated through the reflection `(U, V) ↦ (−U, −V)` at the level of coefficients only | 20–50 | 0.9 |

## 6b, priced (not built)

**The statement:** the four `r ≥ 0` patches are exactly Kruskal. That is, the images of
- the black-hole interior `Φ` (campaign 113), in `{U, V > 0}`;
- the white-hole interior `−Φ`, in `{U, V < 0}`;
- the right exterior `Ψ`, in `{U < 0 < V}`;
- the left exterior `−Ψ`, in `{U > 0 > V}`;

are pairwise disjoint. Together with the horizons `{UV = 0}`, they cover Kruskal's `{UV < 1}`.

| Part | What it needs | Lines | p |
|---|---|---|---|
| 6b-i, onto | Each quadrant point is hit. For `U, V > 0`: `η = arccos(rK(U, V)/M − 1)` and `t = 2M log(V/U)`, using `rinv_spec`, `cc_hK` and `s = √(UV)`. The exterior uses `arcosh`. The reflections follow by symmetry | 150–250 | 0.75 |
| 6b-ii, disjoint and the horizons | Each patch lies in its open quadrant, and `UV = 0` is in no patch (`sk_rK_eq_two_iff`: `r = 2M`) | 40–80 | 0.95 |
| 6b-iii, the metric on the reflected patches | `(U, V) ↦ (−U, −V)` preserves `−F(UV) dU dV`. That is a set-level statement in `P`; on the manifold `sk_S` (`Pt`, two charts) it costs more | 60–120 | 0.8 |

- **Total:** 250–450 lines, at p `0.7`.
- **Expected stop:** 6b-i's inversion at the quadrant boundary, where `log(V/U)` needs `U, V ≠ 0`. That is
  handled by working on the open quadrants.
- **The reading:** "meet at the bifurcation 2-sphere" (l.311) is the horizons `UV = 0` lying in no patch. The
  patches meet along all four horizon halves in the manifold, and at `U = V = 0` only in the `(η, t)` chart's
  limit.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

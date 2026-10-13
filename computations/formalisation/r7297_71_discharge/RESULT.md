# `r7297+71.7` — RESULT: the discharge is CHEAP, and `r7295`'s `6` was mis-ordered, not wrong — all five candidates land, every one under the `200`-line hand route (76, 166, 66, 149, 112), so the stop rule never fires. ⌗ And the cumulative rate beats the baseline, `857/6 ≈ 143 < 150`, which my own central costs said it would NOT

*Read against `PREDICTION.md` in this directory, pushed at `r7297+71.1` before any `mathlib` file was read for this
order. The pre-registration is not revised. Landed one candidate per commit, `+71.2` to `+71.6`.*

*Run: `PROBE_RUN_C1_C5.txt`, which supersedes the earlier runs. The probes are the `r7297` sections of
`lean/probes/CurvatureProbe.lean`. All `65` theorems in the file rest on `[propext, Classical.choice, Quot.sound]`.*

## ⚠ First, the premise the order rested on

*The order asked for "the `5` remaining pre-registered discharges … as named". `r7295`'s pre-registration
predicted a COUNT of `6` and named none. So the five here were fixed at `+71.1`, by a rule, before any cost was
measured:*
- *statable;*
- *the stand-in carries a connection hypothesis;*
- *the metric fits in one chart;*
- *cheapest first by prediction.*

***That is the closest honest reading of "as named". It is not the order's reading.***

## ⛔ The negative — scored on the rule pushed at `+71.1`

| # | receipt | lands? | marginal lines `cᵢ` | predicted | rule |
|---|---|---|---|---|---|
| **C1** | 43 — homothety charge on null geodesics | **yes** | **76** | 90 | `≤ 200` → next |
| **C2** | 92 — `sinh^{2/3}` solves the E = 1 radial geodesic | **yes** | **166** | 150 | `≤ 200` → next |
| **C3** | 41 — `κ = f′/2` | **yes** | **66** | 120 | `≤ 200` → next |
| **C4** | 29 — the cycloid solves the radial geodesic | **yes** | **149** | 220 | `≤ 200` → next |
| **C5** | 77 — `∂_x`, `∂_y` Killing via `∇_(a ξ_b) = 0` | **yes** | **112** | 350 | `≤ 200` |

***The rule: every candidate landed with `cᵢ ≤ 200` → "the discharge is cheap and `r7295`'s `6` was mis-ordered,
not wrong".*** *The STOP row never fired, and the order's second branch — "the port's value is the character
change, not the discharge" — is NOT the answer. **The port's value is both, and the discharge is cheaper per
receipt than building each connection by hand.***

| after | cumulative lines / discharge | pre-registered central |
|---|---|---|
| port alone | `288 / 1 = 288` | 288 |
| C1 | `364 / 2 = 182` | 189 |
| C2 | `530 / 3 = 177` | 176 |
| C3 | `596 / 4 = 149` | 162 |
| C4 | `745 / 5 = 149` | 174 |
| C5 | ***`857 / 6 ≈ 143`*** | 203 |

***"Beating the baseline" was fixed at `< 150`. It is met, at `143`.*** *My central costs predicted it would never be
met. **C3, C4 and C5 came in under their predictions by 54, 71 and 238 lines.** That margin is the whole difference.*

| quantity | predicted | **measured** |
|---|---|---|
| C1 lands | 0.8 | **yes** |
| C2 | 0.65 | **yes** |
| C3 | 0.5 | **yes** |
| C4 | 0.3 | **yes** |
| C5 | 0.2 | **yes** |
| stop rule fires before C5 | **0.75** | ***no*** |
| "the port's value is the character change, not the discharge" | **0.6** | ***no*** |

***Wrong in the direction this programme keeps being wrong in: the cost came in under the estimate, five times out
of five.***

## Why it went cheap — in terms

- ***One shape of proof served four of the five.*** *C2, C3, C4 and C5 each:*
  - *write the named metric as an `NDMetric` on a model space (symmetry by `ring`, nondegeneracy from two or four
    basis vectors, `mdiff` by `fun_prop`);*
  - *test the vector they want against an arbitrary field `Z` (`g_inj`);*
  - *read `lcConn` off as the Koszul form (`lcConn_apply`);*
  - *and finish with `ring` or `linear_combination`.*
  - ***No Christoffel symbol was computed anywhere.*** *That is what the port bought. The hand route computes them.*
- ***The right chart made the named metrics global.*** *Both had a singularity in their usual coordinates:*
  - *SdS's E = 1 profile, in `r = eˢ`;*
  - *the Schwarzschild interior, in `η = 2 arctan eᵘ`.*
  - *There `b = e²ᵘ` and `c = 4M eᵘ/(1 + e²ᵘ)²`, smooth and nondegenerate on all of `ℝ²`, so `NDMetric`'s
    everywhere-nondegeneracy never had to be weakened.*

## What each candidate holds, in terms

- **C1 (l.1468–1543), receipt 43.**
  - `flatCov`, torsion-free and compatible with any constant `η`.
  - **`flat_isLeviCivita`** — by L1, every torsion-free `η`-compatible connection IS the flat one, any signature.
  - **`homothety_nabla`:** `∇ξ = id` for `ξ(x) = x`.
  - **`homothety_charge`:** along `t ↦ p + t v`, `Q = η(ξ, γ̇)` has `Q′ = η(v, v)`, so it is conserved exactly on
    null geodesics.
- **C2 (l.1547–1712), receipt 92.**
  - `pgMetric A w`: `−dτ² + (A ds − w dτ)²`, an `NDMetric` on `ℝ²` for `A ≠ 0`.
  - **`rain_geodesic`:** `∇_V V = 0` for `V = ∂_τ + (w/A)∂_s`.
  - **`sds_rain_geodesic`:** SdS in `r = eˢ`.
  - **`sinh23_flow`:** `r = (2Mα² sinh²(3τ/2α))^{1/3}` solves `ṙ = √(2M/r + r²/α²)`.
- **C3 (l.1714–1779), receipt 41.**
  - **`surface_gravity`:** with `A = 1`, on the horizon `w = −1`, `∇_ξ ξ = w′ ξ` for `ξ = ∂_τ`.
  - **`kappa_half_fprime`:** `w′ = f′/2`, with `f = 1 − w²`.
- **C4 (l.1782–1930), receipt 29.**
  - `dgMetric c b`: `−c² du² + b dt²`.
  - **`unitU_geodesic`:** `U = c⁻¹ ∂_u` is geodesic.
  - **`interior_chart`:** `b = 2M/r − 1` and `r′ = −c eᵘ`, so this IS the Schwarzschild interior.
  - **`interior_geodesic`:** on that metric.
  - **`cycloid_proper_time`:** `τ = M(η + sin η)` has `τ′ = c`, and `r = M(1 + cos η)`.
- **C5 (l.1932–2043), receipt 77.**
  - **`killing_of_invariant`:** translation invariance along `K` makes `K` Killing for THE connection, any
    dimension, any signature.
  - **`gowdy_killing`:** for every diagonal metric on `ℝ⁴` with coefficients depending on `(t, z)` only, `∂_x` and
    `∂_y` are Killing.

## Beside the score, said and not rounded

1. ***Each discharge is of the STAND-IN pre-registered at `+71.1`, not of everything the receipt says.***
   - *C5: 77 also says "EXACTLY two": no third Killing vector. That is a Lie-derivative statement with no
     connection in it, so it is not a discharge candidate, and it is not built.*
   - *C1: 43's "only" is the converse direction, and it is in `homothety_charge` (`Q′ = η(v, v)`, zero iff null).*
2. ***Glue left as reading:***
   - *C2 proves the flow-line ODE in `r` (`ṙ = v(r)`). The rain field lives in `s = log r`. The chain rule
     between them is a line, not stated.*
   - *C4 states the chart identity by coefficients (`b`, `r′`), not as S1's `pullG` of the `(r, t)` metric.*
3. ***C3 is for the generic metric function, as 41's reading is*** *("both readings on one metric function"). No
   named profile is substituted.*
4. ***"THE connection" means `lcConn` of an `NDMetric` (C2–C5), or uniqueness through L1 (C1).*** *The same
   standing caveats as `r7295` apply: `mdiff` is a field of `NDMetric`, and the deferred smoothness class on `lcConn`
   is not discharged. No discharge here used either.*
5. ***Receipt-level count:*** *`r7295` discharged 42. This order discharges 43, 92, 41, 29, 77. **`6` receipts in
   full, against the `6` `r7295` predicted.***

## The order's other constraints

- *Nothing in the quote-pin stride.*
- *No candidate outside the five.*
- *The `r7295` port itself is unchanged; everything here sits beside it.*

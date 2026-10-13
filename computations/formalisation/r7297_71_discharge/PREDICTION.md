# `r7297+71.1` — PRE-REGISTRATION: the port's discharge rate — five candidates fixed by a rule (the order's premise corrected first), costed cheapest first, and the symmetric negative as a MARGINAL RATE: stop at the first candidate that costs more than building its connection by hand

*Committed and pushed before any `mathlib` file is read for this order. The order is `FOR_71.md` §`r7297`.*

## ⚠ The order's premise, corrected first

*The order says "the `5` remaining pre-registered discharges … You named them; take them as named." **I did not name
them.** `r7295+71.1` predicted a COUNT — "L1 discharges `6` receipts (band 3–12)" — and gave no list. The count
came out `1` because only receipt 42 names the 2D conformal metric (`r7295` RESULT). So there are no five named
receipts to take. **The five below are fixed NOW, by a rule, before any cost is measured.** That is the closest
honest reading of "take them as named".*

## The rule that picks the five

*A receipt is a CANDIDATE when:*
- *it is one of the `97` statable;*
- *its stand-in statement carries a CONNECTION hypothesis — it uses `∇`: a geodesic equation, the covariant Killing
  equation, `∇_ξ ξ`;*
- *its metric can be written in ONE chart of a model space.*

*A first integral, a Killing statement by Lie derivative, or a pure ODE carries no connection hypothesis, so it has
nothing to discharge, and is NOT a candidate. That is why 91 ("satisfies the radial geodesic first integral") is
out and 92 ("solves the E = 1 radial geodesic") is in.*

*Among the G1/G2 candidates, the five with the lowest predicted cost, by my reading of each claim's first lines:*

| # | receipt | stand-in, as it will be stated | metric, one chart | predicted lines | band |
|---|---|---|---|---|---|
| **C1** | **43** — homothety charge conserved on null geodesics only | for a constant metric `η` on `E`, the LC connection IS the flat one (L1); `ξ(x) = x` has `L_ξ η = 2η`; along a geodesic `Q = η(ξ, γ̇)` has `Q′ = η(γ̇, γ̇)`, so `Q` is constant iff `γ` is null | flat, any signature | **90** | 50–180 |
| **C2** | **92** — `sinh^{2/3}` solves the E = 1 radial geodesic | 2D Painlevé–Gullstrand `g = −dτ² + (dr − v(r) dτ)²`, nondegenerate everywhere (`det = −1`): the rain field `V = ∂_τ + v ∂_r` is GEODESIC for `lcConn`, `∇_V V = 0`, for every smooth `v`; with SdS's `v`, its flow line is the `sinh^{2/3}` law | PG, 2D | **150** | 80–300 |
| **C3** | **41** — null flow fixed points with `κ = f′/2` | in the same PG chart, `ξ = ∂_τ` satisfies `∇_ξ ξ = κ ξ` on the horizon `v = 1`, with `κ = f′/2`, `f = 1 − v²` | PG, 2D | **120** marginal on C2 | 60–250 |
| **C4** | **29** — the cycloid solves the radial geodesic equation | the interior radial geodesic of Schwarzschild in a chart with no horizon singularity, as `∇_γ̇ γ̇ = 0` on the cycloid | Schwarzschild interior, 2D | **220** | 120–450 |
| **C5** | **77** — exactly two Killing vectors (via `∇_(a ξ_b) = 0`) | for polarized Gowdy–dS, `∂_x`, `∂_y` satisfy the covariant Killing equation of `lcConn` | Gowdy–dS, 4D | **350** | 200–700 |

*Shared machinery, charged to C1 and not spread across the others:*
- *`NDMetric` from a smooth nondegenerate matrix field on a model space — the `mdiff` field proved once, from
  differentiability of the field of forms;*
- *`lcConn` paired with constant fields, read off `lcConn_apply`.*

## ⛔ The negative — as a RATE, fixed now

*The port's `288` lines are SUNK. What is measured now is the MARGINAL cost `cᵢ` of discharging candidate `i` in
full, in lines of Lean that build. The alternative for each receipt is R3's route: one explicit Christoffel form
with its torsion-freeness and compatibility by hand, about `200` lines per metric (`r7277`).*

| outcome | scored |
|---|---|
| **a candidate lands with `cᵢ ≤ 200`** | it is a discharge the port BOUGHT more cheaply than the hand route. Take the next one. |
| **a candidate lands with `cᵢ > 200`, or does not land within `2×` its central budget** | ***STOP.*** *From that point the port is not cheaper than the hand route per receipt, so **the port's value is the CHARACTER CHANGE of `r7295` (the `97` move off a hypothesis), not the discharge count.** Reported as that, and not pursued to a number.* |
| **all five land, each with `cᵢ ≤ 200`** | ***the discharge is cheap and `r7295`'s `6` was mis-ordered, not wrong***: the cumulative rate `(288 + Σcᵢ)/(1 + k)` is reported against the baseline `288/1` |

- ***"Beating the baseline" means, fixed now:*** *the cumulative lines per discharge, `(288 + Σcᵢ)/(1 + k)`, falls
  below `150`, half the baseline. On my central costs it runs:*

  | after | cumulative lines / discharge |
  |---|---|
  | C1 | `(288 + 90)/2 = 189` |
  | C2 | `378 + 150 = 528`, over 3 = `176` |
  | C3 | `648 / 4 = 162` |
  | C4 | `868 / 5 = 174` |
  | C5 | `1218 / 6 = 203` |

  ***So on my own prediction the cumulative rate never beats the baseline, even while every marginal discharge
  but C5 is cheaper than the hand route.*** *The two numbers answer different questions, and both will be
  reported.*
- ***My probabilities:***
  - *C1 lands **0.8**;*
  - *C2 **0.65**;*
  - *C3 **0.5**;*
  - *C4 **0.3**;*
  - *C5 **0.2**;*
  - *the STOP rule fires before C5: **0.75**;*
  - *the verdict "the port's value is the character change, not the discharge": **0.6**.*

## What this order does NOT do

- *Nothing in the quote-pin stride.*
- *No candidate outside the five. If the stop rule fires, nothing past it is attempted.*
- *No change to the `r7295` port itself, except what the shared machinery adds beside it.*

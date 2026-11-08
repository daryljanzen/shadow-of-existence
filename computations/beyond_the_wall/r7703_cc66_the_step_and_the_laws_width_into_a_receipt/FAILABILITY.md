# `r7703` (cc66) — FAILABILITY, **and leg B is the reason this revision withdraws a figure already inside an order**

| leg | perturbation | total FAIL | named target failed |
|---|---|---|---|
| **A** | the second peak's `q` scaled `1.04` | 1 | ✔ the half-rise-at-the-peak gate |
| **B** | the law's translated half-rise forced to track the shift | 1 | ✔ the located-feature gate |
| **C** | the law's lowest-band ratio scaled `1.35` | 1 | ✔ the same-size gate |
| **D** | the resolution floor tightened to `0.2 h` | 1 | ✔ the sharpness gate |
| **E** | the law's increments reversed | 1 | ✔ the ramp gate |

*Each leg asserts its own perturbation applied before the run; one form of leg B reported `VOID` because
I had regex-escaped the brackets in a literal-string replace, and the harness said so instead of
passing.*

## ⛔⛔⛔ AND THE FIRST FORM OF LEG B DID NOT FAIL — WHICH IS HOW THE WITHDRAWAL WAS FOUND

The leg I wrote first translated the interval the **law** is read on by `+0.30` in `q` and expected the
"same place" gate to fire. **It reported `0` FAIL.** ⇒ *Not a harness fault: the gate was insensitive,
because the thing it claimed to locate does not exist.*

| translation of the read interval | the EXCESS's half-rise | the LAW's half-rise |
|---|---|---|
| `+0.00` | `1.7830` | `1.8021` |
| `+0.15` | `1.6329` (`−0.1501`) | `1.8001` (`−0.0020`) |
| `+0.30` | `1.4868` (`−0.2962`) | `1.7983` (`−0.0038`) |
| `−0.30` | `1.8864` (`+0.1034`) | `1.8075` (`+0.0054`) |

*** A located feature moves by `−d`. The excess's does. The law's does not move at all. *** ⇒ **For the
law the locator is returning the SCAN WINDOW, not a feature of the curve** — its plateaux are re-measured
from the translated curve, so a broad monotone ramp crosses its own midpoint at about the same place
whatever you do to it.

⇒ *** SO `r7701+cc66`'s ROUTED FIGURE — "the law's transition sits at `q = 1.8021` against the step's
`1.7830`" — IS WITHDRAWN. *** ⌗ *`1.8021` was never wrong as an **output**. It was wrong as a
**location**, and nothing in `r7701` asked whether the thing being located existed. **The failability
leg asked, one revision later.*** ⚠ **`69` merged that figure into the `r7703` order text**, so the
withdrawal is routed and not merely recorded.

## ⇒ WHAT REPLACES IT, AND IT IS A BETTER SENTENCE

**The law does not have a step.** Its seven bands rise strictly and decelerate throughout —
`+0.0167 +0.0122 +0.0087 +0.0061 +0.0042 +0.0027` — a smooth saturating ramp with no feature in it.

⇒ **Where the measurement steps, the law ramps.** *The law still carries the step's **size** — the
lowest band runs `0.4816` of the rest under the law against `0.4771` measured, agreeing to `0.9` per
cent — and that survives the withdrawal **because it is a band average and never needed the step to be
located.** The `q ≈ 1.9` residual is the sharp step read against the smooth ramp.*

⌗ *** THE LESSON, AND IT IS THE THIRD VARIANT OF ONE THING IN THREE REVISIONS. *** *`r7695`: a number
that falls for the wrong reason. `r7701`: a repair that moves the figure its instrument is validated
against. `r7703`: **a locator reporting a location for a curve that has none.** All three are an
instrument answering a question subtly different from the one I meant to ask — and this one was caught
only because the gate was perturbed rather than merely run.*

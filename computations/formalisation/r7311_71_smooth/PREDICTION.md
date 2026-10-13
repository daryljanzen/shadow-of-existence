# `r7311+71.1` — PRE-REGISTRATION: item A, the smoothness class on THE connection. In four pieces, on the model space, with costs in lines; the stop at `600` is scored first; and the symmetric negative: a class that comes in under `120` was never worth carrying

*Committed and pushed before any `mathlib` file is read for this order. The order is `FOR_71.md` §`r7311`, which
accepts `r7309+71.1`'s proposal unchanged. This file is that proposal's A, made checkable.*

***What I have read for this, all of it in my own tree:***
- *`CurvatureProbe.lean`'s `contMDiffCov_model` (K2, l.279). It turns a `C^∞` Christoffel form `G` on `E` into
  `ContMDiffCovariantDerivative cov ∞`.*
- *`NDMetric` (l.1272).*
- *`lcConn` (l.1424).*

*Nothing of `mathlib` has been read for this order.*

## The statement, fixed now

***For a `C^∞` field of symmetric nondegenerate bilinear forms `B : E → (E →L[ℝ] E →L[ℝ] ℝ)` on a model space
`E`, the Levi-Civita connection `lcConn` of the `NDMetric` it defines is a `C^∞` covariant derivative:
`ContMDiffCovariantDerivative (lcConn …) ∞`.*** *This is on the model space, as all six discharges are. The general
manifold, through `mathlib`'s bundle smoothness API, is **not** in scope. If it is reached cheaply it is reported,
but it is not owed.*

## The pieces

| # | piece | central lines | band |
|---|---|---|---|
| **A1** | `lcConn`'s Christoffel form on `E`: `lcConn (const w) x u = Γ x u w`, with `Γ x u w` the `B x`-dual of the Koszul form on constant fields, `½[(DB·u)(w,·) + (DB·w)(u,·) − (DB·(·))(u,w)]` | **110** | 60–250 |
| **A2** | `Γ` is `C^∞` when `B` is, by `x ↦ (B x)♭⁻¹` being `C^∞`, the inverse of a `C^∞` family of continuous linear equivalences | **80** | 30–250 |
| **A3** | the class itself, by `contMDiffCov_model`; then on each named `NDMetric` already in the tree (`pgMetric`, `dgMetric`, `diag4Metric`), its `B` shown `C^∞` | **40** | 20–100 |
| **A4** | K1 applied to `lcConn` of one named metric with no class hypothesis left: `curv_smul_left` on `pgMetric` | **20** | 10–60 |
| | **total** | **250** | **120–600** |

## ⛔ The rule, scored first

| outcome | scored |
|---|---|
| **A1–A4 build in `≤ 600` lines** | ***A LANDS.*** The `97` rest on no carried hypothesis about the connection on the model space. B runs on this base. |
| **over `600` lines, or A2 needs a lemma for the smooth inverse of `♭` that is absent from `mathlib` and costs `> 150` lines alone** | ***A IS NOT WORTH ITS COST.*** *The class stays a named hypothesis on K1–K3. **B then runs under it**, and every B line says so. Named by the lemma that stopped it.* |
| **⛭ the symmetric negative: A lands in `< 120` lines** | ***the class was cheap, and `r7295`'s caveat 2 carried for three cycles a hypothesis that one short file removes.*** *That is reported as a defect in how the port was scoped, not as a success of A.* |

- ***`2×` is not the stop here.*** *The proposal fixed `600`, and `600` is what is scored. `2 × 250 = 500` is reported
  beside it.*

## The `C²` packaging prediction, made scorable

*`r7309+71.1` predicted that A makes the `C²` tensorial packaging unnecessary for every receipt in the tree.*
- **Scored by A4.** If `curv_smul_left` applies to `lcConn` of `pgMetric` with nothing but A3's instance, the
  `C^∞` statements already built apply as they stand → **unnecessary**.
- If A4 needs a `C²`-only form of a K1 lemma → **necessary**, and named.

## My probabilities

| quantity | p |
|---|---|
| A lands (`≤ 600`) | **0.60** |
| A lands within `2×` central (`≤ 500`) | 0.55 |
| A lands under `120` (the symmetric negative) | 0.10 |
| A2's smooth inverse is present in `mathlib` (no port of it needed) | 0.75 |
| A4: the `C²` packaging is unnecessary | 0.60 |
| the general manifold reached as well | 0.15 |

## What this does NOT do

- Nothing in the quote-pin stride.
- Nothing of B. That is pre-registered after A's verdict.
- No change to L1/L2 (`r7295`) or to the six discharges, except what A3 adds beside them.

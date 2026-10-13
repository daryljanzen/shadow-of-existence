# `r7287+71.1` — PRE-REGISTRATION: the curvature stratum G2 — the curvature tensor with the connection a hypothesis, its model formula, Ricci and scalar curvature, and one instance — under budgets, with the order's symmetric negative

*Committed and pushed before any probe is written and before any `mathlib` file is read for this order. The order
is `FOR_71.md` §`re r7287`.*

***What I already know, and so cannot predict blind.***
- *From `r7273+71.5` B10: `CovariantDerivative/Basic.lean` l.108's docstring defers the smoothness of `∇_Y Z`
  as a section ("We will prove in a later file …"). The order names `ContMDiffCovariantDerivativeOn` as where
  that deferral sits. I have not read that declaration.*
- *From `r7277+71.5` R3: an explicit `CovariantDerivative` on `ℝ × ℝ` (`covConf`) built from a Christoffel form,
  torsion-free and compatible with `a(η)²(−dη² + dx²)`.*
- *From `r7281`: `covDerivAlong_model`. On `E` as its own model, every trivialisation's frame is the constant
  basis.*
- *From `r7285`: the `26` G2 receipts state curvature quantities of NAMED metrics — Kretschmann, Ricci, Weyl,
  scalar, Pontryagin, curvature invariants — mostly in dimension 4 and up.*
- ***One thing I state now so it cannot be bent later.***
  - *T3b's gap is that the flow is `C¹` in its initial point (`flow_hasFDerivAt`).*
  - *The curvature gap, if there is one, is that `∇_Y Z` is a differentiable section.*
  - *These are different statements about different objects. **I expect that if curvature stops, it stops on a
    DIFFERENT lemma.** The order's "two strata behind one gap" is scored on the lemma actually stopped on, not
    on the resemblance.*

## The items, fixed now

| # | needed for a G2 statement | path | what would count as PRESENT / DEF |
|---|---|---|---|
| K-A | the curvature of a connection, `R(X,Y)Z = ∇_X∇_Y Z − ∇_Y∇_X Z − ∇_[X,Y] Z`, as a definition | **ON** | a definition over `CovariantDerivative` and `mlieBracket` |
| K-B | **tensoriality**: `R(X,Y)Z` at `x` depends only on `X x`, `Y x`, `Z x` — `C^∞`-linearity in each slot | **ON** | a theorem |
| K-C | the model formula on `E`: for a `cov` with Christoffel form `G`, `R(u,v)w = (DG·u)(v,w) − (DG·v)(u,w) + G(u, G(v,w)) − G(v, G(u,w))` on constant fields | **ON** | a theorem |
| K-D | the Ricci tensor, a trace of `w ↦ R(w,u)v` | **ON** | a definition over `LinearMap.trace` |
| K-E | the scalar curvature, a metric contraction of Ricci through a nondegenerate form | **ON** | a definition |
| K-F | the first Bianchi identity, for a torsion-free `cov` | OFF | a theorem |
| K-G | one instance: the scalar curvature of `covConf a`, the programme's 2D conformal metric, in closed form | **ON** — *one named metric, the R3 pattern* | a theorem |

## The probes, fixed now — in `lean/probes/`, imported by nothing, the connection a HYPOTHESIS throughout

| probe | items | statement | budget |
|---|---|---|---|
| **K1** | K-A, K-B | define `curv cov X Y Z`; prove `C^∞`-linearity in `Z`, then in `X` and `Y`, **carrying as a named hypothesis `hcov` that `∇_Y Z` is differentiable where `Y`, `Z` are `C²`** | **250 lines** |
| **K2** | K-C, and DISCHARGE `hcov` on `E` | on `E`, with `∇_w (const u) = G x w u` and `G` `C¹`: `∇_Y Z` is differentiable, so `hcov` holds, and K-C | **250 lines** |
| **K3** | K-D, K-E | Ricci by `LinearMap.trace`; scalar curvature through a nondegenerate symmetric form on a finite-dimensional space | **120 lines** |
| **K4** | K-G | the scalar curvature of `covConf a` on `ℝ × ℝ` in closed form, from K2 and K3 | **250 lines** |

*K-F (Bianchi) is OFF the path and classed by reading.*

***`hcov` is the deferred smoothness, carried as a hypothesis exactly as the layers carried `hg` and
`CoeffDiffAt`.*** *So K1 measures whether the identities need anything MORE than that smoothness. K2 measures
whether, on a chart, the smoothness is a lemma rather than a gap. **A K1 build with `hcov` is not a claim that
`hcov` is free on a manifold.** On a manifold, `hcov` is discharged by reading or not at all, and the result
says which.*

## Predictions

| probe | builds inside budget |
|---|---|
| K1 | **0.6** — *tensoriality in `Z` is `leibniz` twice plus `hcov`; in `X` it needs `mlieBracket` of `f • X`* |
| K2 | **0.55** — *the frame is constant on `E`, so `∇_Y Z = DZ·Y + G(Y, Z)`; differentiating needs `G` `C¹`* |
| K3 | **0.75** |
| K4 | **0.35** — *a 2D Christoffel form differentiated once more; R3 took `208` lines for the connection alone* |

## ⛔ The negative — the order's, symmetric, scored on a rule fixed now

| outcome | scored |
|---|---|
| **K1, K2 and K3 all build** | ***G2 is STATABLE over the tree*** — the curvature tensor is reachable with the connection a hypothesis, the smoothness is a lemma on a chart, and the statable count goes from `26` to `52` of `111` |
| **K1 or K2 stops on a lemma that IS the deferred smoothness of `∇_Y Z`** | ***G2 is behind a NAMED gap***, with the lemma named. It is scored as **the same gap as T3b iff the lemma it stopped on is `flow_hasFDerivAt` or depends on it**; otherwise as a second, different gap, said so |
| **anything else** — a build failure on a lemma that is not the smoothness, or K3 failing | ***mixed***, named by the lemma each probe stopped on and not rounded either way |

- *K4 is scored beside the rule, not in it. One named metric is the R3 pattern, not the stratum.*
- ***Probabilities:***
  - *statable: **0.4**;*
  - *named gap: **0.35**, with **0.9** that it is a different lemma from T3b's;*
  - *mixed: **0.25**.*

## The order's other constraint

***The port is not begun, and nothing here begins it.*** *Every probe takes the connection as a hypothesis or, in
K4, uses the one explicit connection already in the tree.*

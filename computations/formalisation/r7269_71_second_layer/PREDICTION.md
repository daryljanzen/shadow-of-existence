# `r7269+71.1` — PRE-REGISTRATION: layer 2, the Lie derivative of a tensor and Killing fields, declaration by declaration, with I20's path marked BEFORE the search

*Committed and pushed before any search of `mathlib` for this order. The order is `FOR_71.md` §`r7269`: the
same instrument as `r7267+71.1`. **"Layer 2" in the order is layers 2 and 3 of `ShadowFormal/I20.lean`'s
docstring** — the Lie derivative of a tensor field, and the (conformal-)Killing equation — so both are measured
here. Layers 4 and 5 (null geodesics, the charge along them) are not.*

***What I already know, and so cannot predict blind.*** *From `r7259+71.5`: `mathlib` has
`VectorField.mlieBracket`, and "Killing" there is the Killing FORM of a Lie algebra. From `r7267+71.2`:
`CovariantDerivative/Basic.lean`, `Torsion.lean` and `Metric.lean` exist, and so do the hom-bundle and the
layer-1 probe structure `ContMDiffPseudoRiemannianMetric`. Every other line below is a prediction.*

## What changes from `r7267+71.1`, and why

***Each item is marked ON or OFF `I20`'s path NOW, before the search.*** *Last cycle the path reading came
after the count, and I had to label it unregistered. This cycle it is part of the instrument, so the reachable
negative can be scored on it directly. The path is `I20`'s geometric statement as written in `I20.lean`: "`ξ =
∂_η` is a conformal Killing field of `a(η)² (−dη² + dx²)`".* **An item is ON when that sentence cannot be stated,
or its instance proved, without it.**

## The list, fixed now

*Eighteen items. It is not extended after the search. An item I find I left out is recorded as an omission and
not counted.*

| # | needed | path | what would count as PRESENT |
|---|---|---|---|
| A1 | the Lie bracket of vector fields on a manifold | ON | `VectorField.mlieBracket` |
| A2 | the Lie bracket on a vector space, and its agreement with the manifold bracket on the model space | ON | `VectorField.lieBracket` with an `mlieBracket` ↔ `lieBracket` lemma |
| A3 | the derivative of a function along a vector field on a manifold | ON | `mfderiv f x (X x)` or a named wrapper |
| A4 | integral curves of a vector field on a manifold, local existence | OFF | `IsMIntegralCurve…` and an existence theorem |
| A5 | a flow (one-parameter local diffeomorphisms) of a vector field on a manifold | OFF | a flow definition with a group law |
| A6 | pullback of a field of bilinear forms by a smooth map | OFF | a definition through `mfderiv` |
| A7 | torsion of a connection | OFF | `Torsion.lean` |
| A8 | metric compatibility of a connection | OFF | `CovariantDerivative/Metric.lean` |
| B1 | the Lie derivative of a (0,2)-tensor field: `(𝓛_X g)(Y,Z) = X(g(Y,Z)) − g([X,Y],Z) − g(Y,[X,Z])` | **ON** | a definition in `mathlib` |
| B2 | that `𝓛_X g` is tensorial in `Y` and `Z` (a tensor at a point) | OFF | a theorem |
| B3 | the flow definition of `𝓛_X g` (`d/dt φ_t^* g`) and its agreement with B1 | OFF | a definition and a theorem |
| B4 | Killing vector field: `𝓛_X g = 0` | **ON** | a definition |
| B5 | conformal Killing vector field: `𝓛_X g = 2σ g` for a function `σ` | **ON** | a definition |
| B6 | Killing ⇔ `∇X` skew for the Levi-Civita connection | OFF | a theorem |
| B7 | Killing fields form a Lie subalgebra | OFF | a theorem |
| B8 | **the instance: `∂_η` is conformal Killing for `a(η)² (−dη² + dx²)` on a vector space, with `σ = a′/a`** | **ON** | a theorem |
| B9 | Killing ⇒ its flow acts by isometries | OFF | a theorem |
| B10 | naturality of `𝓛` under pullback by diffeomorphisms | OFF | a theorem |

***ON the path: A1, A2, A3, B1, B4, B5, B8 — seven items.*** *B4 is ON because the order names Killing
fields and B5 is B4 with a factor. B2 is OFF because the conformal-Killing equation can be stated as an identity
for all vector fields `Y`, `Z` without first proving that `𝓛_X g` is a tensor.*

## How each ABSENT item is classed — the `+71.1` rule, with PORT generalised in advance

- **DEF:** writable as a `def`, `structure` or `instance` over PRESENT machinery. Its proof obligations are
  discharged by lemmas `mathlib` already has.
- **PORT:** `mathlib` proves it in a neighbouring setting — a vector space instead of a manifold, Riemannian
  instead of pseudo-Riemannian, a vector field instead of a tensor. Transferring it replaces named ingredients
  with named existing `mathlib` lemmas.
- **THEORY:** no proof to port, or the transfer needs a result `mathlib` does not have.

### Probes, fixed now

*Three probes, against `mathlib` `4e6064a4`, in `computations/formalisation/lean/probes/`. Imported by
nothing, like the layer-1 probe.*
- **P1:** B1 as a definition over the layer-1 probe structure.
- **P2:** B4 and B5 as definitions over P1.
- **P3:** B8, the instance. *This is the one that can fail on mathematics rather than on syntax: it needs
  `mlieBracket` of a constant field computed on the model space.*
- **Budget for P3: 150 lines of Lean, or the end of this cycle, whichever comes first.** If it does not build
  with no `sorryAx` inside the budget, B8 is classed by reading. The lemma it stopped on is named.

*Probes are measurements and not the start of the port. Per the order, the Levi-Civita PORT costed at
`r7267+71.2` is not begun, and nothing here touches it.*

## Predictions

| quantity | central | band |
|---|---|---|
| A present (of 8) | **7** | 6–8 — *A5, a global flow with a group law, is my expected absence* |
| B present (of 10) | **0** | 0–1 |
| present / 18 | **7 / 18 = 39 %** | 30 %–50 % |
| absent classed THEORY, all | **4** | 2–6 — *B3, B9, B10, and one of A5 or B6* |
| **absent classed THEORY, ON the path** | **1** | 0–2 — *B8 if `mlieBracket` cannot be computed on the model space* |
| P1 builds with no `sorryAx` | **yes, 0.85** | — |
| P2 builds with no `sorryAx` | **yes, 0.85** | — |
| P3 builds with no `sorryAx` inside its budget | **0.45** | — |

## ⛔ The reachable negative — the order's, scored on the path marked above

***If THEORY ON the path is `0`, then layer 2, like layer 1, is DEF-or-PORT on `I20`'s path. Then, per the
order, `r7263`'s `the geometric core is not formalisable this year` is a sentence about a horizon and not a
wall, and I say so at the head of the result.***

- **ON-path THEORY `≥ 1`:** the items are named, with the lemma each stopped on.
- **My probability that it fires: 0.45.** *Under one half, because B8 needs the bracket computed in
  coordinates, and I have not seen that lemma. Not far under, because layer 1's one expected absence turned out
  to be present.*

*The OFF-path count is reported in full beside it and does not move the negative either way. That was decided
here, before any search.*

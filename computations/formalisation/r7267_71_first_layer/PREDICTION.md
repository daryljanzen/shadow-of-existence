# `r7267+71.1` — PRE-REGISTRATION: the distance to the first missing layer, declaration by declaration, and whether Physlib tracks its gap

*Committed and pushed before any search of `mathlib` or `Physlib` for this order. The order is `FOR_71.md`
§`r7267`. **What I already know, and so cannot pretend to predict blind**, is from my own `r7259+71.5`
measurement: `mathlib` has `RiemannianMetric` with a positive-definite `pos` field, `ContMDiffRiemannianMetric`,
`IsRiemannianManifold`, a Riemannian-only `IsLeviCivitaConnection`, and `Matrix.indefiniteDiagonal`. Every
other line below is a prediction.*

## ① The first layer: a pseudo-Riemannian metric on a manifold

*The pinned commit is `mathlib` `4e6064a4`, the commit `lean/` already builds against.*

### The list, fixed now

Twenty declarations, or groups of tightly linked declarations, that a pseudo-Riemannian metric layer needs. **A**
is what the layer would be built FROM. **B** is what the layer itself would add. *The list is fixed here and is
not extended after the search. An item I find I left out goes in the result as an omission and is not counted.*

| # | needed | what would count as PRESENT |
|---|---|---|
| A1 | the tangent bundle as a vector bundle over a manifold | `TangentSpace`, `VectorBundle` instance on it |
| A2 | smooth sections of a vector bundle | `ContMDiffSection` or equivalent |
| A3 | the fibrewise bilinear-map bundle and its smoothness | a hom-bundle `E x →L E x →L ℝ` with a `ContMDiff` notion |
| A4 | nondegeneracy of a bilinear form | `LinearMap.BilinForm.Nondegenerate` or `SeparatingLeft/Right` |
| A5 | symmetry of a bilinear form | `LinearMap.IsSymm` or `BilinForm.IsSymm` |
| A6 | diagonalisation of a real quadratic form to signs | an `equivalent_…weighted_sum_squares` / `signType` form |
| A7 | Sylvester's law of inertia — the signature is well defined | a theorem that the number of `-1`s is an invariant |
| A8 | a signature-`(p,q)` model form | `Matrix.indefiniteDiagonal` or equivalent |
| A9 | the musical isomorphism of a nondegenerate form, finite dimension | `BilinForm.toDual` or equivalent |
| A10 | the Riemannian metric structure, as template | `Bundle.RiemannianMetric` |
| A11 | smoothness of a metric, as template | `ContMDiffRiemannianMetric` |
| B1 | a pseudo-Riemannian metric structure (fibrewise symmetric, nondegenerate) | a `structure` or `class` in `mathlib` |
| B2 | the index (signature) of the metric at a point | a definition |
| B3 | the index is locally constant / constant on a connected manifold | a theorem |
| B4 | a Lorentzian metric (index 1) | a definition |
| B5 | the musical isomorphisms as smooth bundle maps | a definition with its smoothness |
| B6 | Levi-Civita: existence and uniqueness for a NONDEGENERATE metric | theorems |
| B7 | Minkowski space as an instance of B1 | an instance |
| B8 | a warped-product metric `−dt² + a(t)² g` (the FLRW form) as an instance of B1 | an instance or definition |
| B9 | the metric's induced volume form or density, nondegenerate case | a definition |

### How every ABSENT item is classed, fixed now

- **DEF:** writable as a `def`, `structure` or `instance` over PRESENT machinery. Its proof obligations are
  discharged by lemmas `mathlib` already has.
- **PORT:** `mathlib` proves the Riemannian version. That proof's use of positivity is replaceable by a named,
  existing `mathlib` lemma about nondegenerate forms.
- **THEORY:** no proof in `mathlib` to port, or the proof uses definiteness essentially. Needs new mathematics
  in the library.

*The classification is by reading source, with one compile probe. B1 is written against `mathlib` `4e6064a4`
as a probe file in this directory, and built. If it builds with no `sorryAx`, B1 is DEF by measurement rather
than by reading. **The probe is a measurement, not the start of the layer.** It is not imported by
`ShadowFormal`, and nothing is built on it, as ordered.*

### Predictions

| quantity | central | band |
|---|---|---|
| A present (of 11) | **10** | 9–11 — *A7, Sylvester's uniqueness, is my one expected absence* |
| B present (of 9) | **0** | 0–1 |
| **present / 20** | **10 / 20 = 50 %** | 40 %–60 % |
| absent items classed **THEORY** | **3** | 2–5 — *expected: B3, B6, and A7 (or B2 through it)* |
| absent items classed DEF or PORT | **7** | 5–9 |
| B1 probe builds with no `sorryAx` | **yes, 0.85** | — |

### ⛔ The reachable negative, and its rule, fixed now

***If the THEORY count is `0`, the absence is a DEFINITION problem.*** *Then I say "`r7263`'s `the geometric core
is not formalisable this year` should be withdrawn", in those words, at the head of the result.*

- **THEORY `1`:** reported as "one theorem from a definition problem", with that theorem named. Not rounded
  either way.
- **THEORY `≥ 2`:** a theory problem. Counted, and the theorems named.

*My probability that the negative fires: **0.1**. This seat's own numbers have twice come in above my
predictions, so the band is wide on the cheap side.*

## ② Is the gap a tracked one in Physlib?

*One question, with a yes or no behind it.* **Tracked** means at least one of the following:
- a GitHub issue on the Physlib repository naming the FLRW metric, its curvature, or Lorentzian or
  pseudo-Riemannian manifolds;
- a `TODO` entry in Physlib's own TODO system at those declarations;
- a roadmap item.

**Owned** means one of those carries an assignee or a named person.

| | prediction |
|---|---|
| tracked | **yes, 0.7** — *I expect a `TODO` beside `def FLRW : Type := sorry`* |
| owned (an assignee or a named person) | **0.3** |

*Read at `Physlib` `b0e7ca1c` (the source in `lean-physlib/.lake`) and on the live repository's issue list, if
this container's network reaches it. If it does not, that is said, and the answer rests on source alone.*

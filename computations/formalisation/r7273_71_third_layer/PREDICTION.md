# `r7273+71.1` — PRE-REGISTRATION: layer 3, the connection and the covariant derivative, with I20's path marked before the search; and whether the Levi-Civita PORT's `32` survives contact

*Committed and pushed before any search of `mathlib` for this order. The order is `FOR_71.md` §`r7271`, which
stands unchanged at §`r7273`. Instrument: the same as `r7269+71.1`: a fixed list, path marks fixed now, the
DEF / PORT / THEORY rule, and probes with budgets.*

***What I already know, and so cannot predict blind.*** *From `r7267+71.2`:*
- *`CovariantDerivative/Basic.lean`, `Torsion.lean`, `Metric.lean` and `LeviCivita.lean` exist;*
- *mathlib constructs the Riemannian Levi-Civita connection and proves the Koszul formula and uniqueness;*
- *positivity enters only through `inner_self_eq_zero` and `InnerProductSpace.toDual`;*
- *the PORT was costed at `32` declarations by `grep` (22 in `LeviCivita.lean`, 10 in `Metric.lean`).*

*From `r7269+71.2`: `lieDerivForm`, `IsConformalKilling` and I20's instance, as probes.*

## The path, fixed now

*`I20`'s geometric statement ends in **"for a conformal Killing field `ξ` the charge `g(ξ, γ̇)` is conserved
along every null geodesic `γ`"**. Its proof is one line:*

    d/dt g(ξ, γ̇) = g(∇_γ̇ ξ, γ̇) + g(ξ, ∇_γ̇ γ̇) = ½ (𝓛_ξ g)(γ̇, γ̇) + 0 = σ g(γ̇, γ̇) = 0.

***Layer 3 is everything in that line that is about a connection.*** The geodesic equation `∇_γ̇ γ̇ = 0`, the
null condition and the charge are layers 4 and 5, and are not in this list. **An item is ON when that line
cannot be written, or its connection steps proved, without it.**

## The list, fixed now

*Eighteen items. It is not extended after the search. An item I would add afterwards is recorded as an omission
and not counted.*

| # | needed | path | what would count as PRESENT |
|---|---|---|---|
| A1 | a covariant derivative on a vector bundle | ON | `CovariantDerivative` |
| A2 | torsion of a connection on `TM` | ON | `Torsion.lean` |
| A3 | metric compatibility, Riemannian | OFF | `Metric.lean` (template) |
| A4 | Levi-Civita existence and uniqueness, Riemannian | OFF | `LeviCivita.lean` (template) |
| A5 | the Koszul formula, Riemannian | OFF | `IsLeviCivitaConnection.apply_eq` |
| A6 | tensoriality machinery | OFF | `Tensoriality.lean` |
| A7 | the velocity of a curve as a tangent vector | ON | `mfderiv` of `γ : ℝ → M`, or a named velocity |
| B1 | metric compatibility for a field of NONDEGENERATE forms | **ON** | a definition |
| B2 | Levi-Civita existence for a pseudo-Riemannian metric | **ON** | *the PORT; already classed PORT at `r7267+71.2`. Re-costed below, not begun.* |
| B3 | Levi-Civita uniqueness, pseudo-Riemannian | OFF | a theorem |
| B4 | **`(𝓛_X g)(Y,Z) = g(∇_Y X, Z) + g(Y, ∇_Z X)` for a torsion-free `g`-compatible `∇`** | **ON** | a theorem |
| B5 | conformal Killing in `∇` form: `g(∇_Y ξ, Z) + g(Y, ∇_Z ξ) = 2σ g(Y,Z)` | **ON** | a theorem |
| B6 | the covariant derivative of a vector field ALONG a curve, `D/dt` | **ON** | a definition |
| B7 | compatibility along a curve: `d/dt g(V,W) = g(DV/dt, W) + g(V, DW/dt)` | **ON** | a theorem |
| B8 | for `X` defined near `γ`: `D/dt (X ∘ γ) = ∇_γ̇ X` | **ON** | a theorem |
| B9 | parallel transport | OFF | a definition with existence |
| B10 | the curvature tensor | OFF | a definition |
| B11 | Christoffel symbols in a chart | OFF | a definition |

***ON the path: A1, A2, A7, B1, B2, B4, B5, B6, B7, B8 — ten items.***

## The rule — unchanged from `r7269+71.1`, and one consequence stated now

- **DEF:** a `def`, `structure` or `instance` over PRESENT machinery, with its proof obligations discharged by
  existing lemmas. **A theorem proved by a probe within budget is DEF by measurement, as B8 was at
  `r7269+71.2`.**
- **PORT:** proved in a neighbouring setting; the transfer replaces named ingredients with named existing
  lemmas.
- **THEORY:** neither of the above.

***Consequence, stated before the search:*** *last cycle B6 there (Killing ⇔ `∇X` skew) was classed THEORY,
OFF-path, unprobed. **Its content is this cycle's B4, and B4 is ON.** So it is probed this time, and a probe
that fails inside budget leaves it THEORY. **That is the route by which the negative can fire.***

### Probes, fixed now — `computations/formalisation/lean/probes/ConnectionProbe.lean`, imported by nothing

*None needs Levi-Civita to exist. Each takes a connection as a HYPOTHESIS: any `cov`, torsion-free and
compatible with `g`. So nothing begins the port, and nothing touches `LeviCivita.lean`, `Metric.lean` or the
layer-1 probe.*

| probe | item | budget |
|---|---|---|
| Q1 | B1, compatibility for a field of forms, as a `def` | — |
| Q2 | B4, the `∇` form of `lieDerivForm`, proved | **200 lines** |
| Q3 | B5, a corollary of Q2 with `IsConformalKilling` | 40 lines |
| Q4 | B6, `D/dt` along a curve, as a `def` | **150 lines** |
| Q5 | B7 and B8, the curve-side theorems | **200 lines** |

*A probe that does not build with no `sorryAx` inside its budget leaves its item classed by reading, with the
lemma it stopped on named.*

## Predictions

| quantity | central | band |
|---|---|---|
| A present (of 7) | **7** | 6–7 |
| B present (of 11) | **0** | 0–1 |
| present / 18 | **7 / 18 = 39 %** | 30–50 % |
| absent classed THEORY, all | **5** | 3–7 |
| **absent classed THEORY, ON the path** | **1** | 0–3 — *the along-curve cluster, B6 to B8. `D/dt` needs fields along a map, i.e. a pullback bundle, and I have not seen it.* |
| Q1 builds | **0.9** | — |
| Q2 builds inside 200 lines | **0.6** | — |
| Q3 builds | **0.85, given Q2** | — |
| Q4 builds inside 150 lines | **0.4** | — |
| Q5 builds inside 200 lines | **0.3, given Q4** | — |

## ⛔ The reachable negative — the order's, against the gate's own ruling

***If ON-path THEORY is non-zero, then "a port and a coercion discipline" is withdrawn as the account of the
`82` per cent, and the result says so in its first line.***

*My probability that it fires: **0.55**. Just over one half, because the along-curve cluster is three ON
items, and `mathlib`'s connection files work on sections of a bundle over `M`, not along a map into it.*

## ② Does the PORT's `32` survive contact?

*Re-costed by reading what the layer-3 work touches. **The port is not begun.** The `32` came from counting
declarations with a direct inner-product reference in two files. The re-cost counts, in addition:*
- declarations that reach the fibre inner product **transitively**, through `RiemannianBundle`,
  `IsContMDiffRiemannianBundle` or the scoped norm instance;
- **files** the port would have to touch beyond the two.

| quantity | central | band |
|---|---|---|
| the re-costed PORT, in declarations | **45** | 32–80 |
| files touched beyond `LeviCivita.lean` and `Metric.lean` | **1** | 0–3 — *`VectorBundle/Riemannian.lean`'s `IsContMDiffRiemannianBundle`* |

***A re-cost under `32` is reported as the first estimate having been too high, not rounded to it.***

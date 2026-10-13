# `r7281+71.1` — PRE-REGISTRATION: probe the never-probed THEORY cluster — parallel transport, geodesic existence, the flow — under budgets, with the order's symmetric negative

*Committed and pushed before any probe is written and before any `mathlib` file is read for this order. The order
is `FOR_71.md` §`r7281`.*

***What I already know, and so cannot predict blind.***
- *From `r7269+71.2`: `mathlib` has integral curves of a vector field on a manifold
  (`exists_isMIntegralCurveAt_of_contMDiffAt`), and no flow.*
- *From `r7273+71.5`: there is no parallel transport. `Metric.lean` names it as absent, and `Basic.lean`
  defers the smoothness of `∇`.*
- *From `r7277+71.5`: there is no geodesic.*
- *Before writing this I listed the FILE NAMES (not the contents) of `Mathlib/Analysis/ODE/` (`Basic`,
  `DiscreteGronwall`, `ExistUnique`, `Gronwall`, `PicardLindelof`, `Transform`) and of
  `Mathlib/Geometry/Manifold/IntegralCurve/` (`Basic`, `ExistUnique`, `Transform`, `UniformTime`).*

## The items probed, chosen now by a rule

***Rule: one item for each of the three foundations the order names — parallel transport, ODE existence, the
flow — taking the one closest to `I20`'s path.*** The flow is split in two, because "flow" was classed as one item
while containing two claims of very different cost.

| probe | item (as classed THEORY) | the exact statement probed | scope |
|---|---|---|---|
| **T1** | `r7273` B9, parallel transport | for a `cov` on `TE` whose Christoffel form is continuous along `γ`, a `C¹` curve `γ`, `T > 0` and `v`, there is `V` on `[0, T]` with `V 0 = v` and `covDerivAlong cov γ V t = 0` for `t ∈ (0, T)` | **`M = E`, a finite-dimensional vector space, its own model** |
| **T2** | `r7277` B7, geodesic existence | for a `cov` on `TE` whose Christoffel form is `C¹`, any `x`, `v`: there are `ε > 0` and `γ` with `γ 0 = x`, `vel γ 0 = v`, `IsGeodesicAt cov γ t` for `|t| < ε` | **`M = E`, as T1** |
| **T3a** | `r7269` A5, the flow — **its group law** | for a `C¹` vector field on a boundaryless manifold, the local flow `φ(t, x)`, defined from `mathlib`'s integral curves, satisfies `φ(s + t, x) = φ(t, φ(s, x))` on a common domain | **a manifold** |
| **T3b** | `r7269` A5, the flow — **smooth dependence on `x`** | `x ↦ φ(t, x)` is `C¹` near a point, for small `t` | **a manifold** |

***The scope cut is stated before the search, and it is scored as one.*** *T1 and T2 are probed on a vector
space. There `covDerivAlong`'s frame is the same at every `t`, so the question is the ODE alone and not the
gluing of frames. **A build there is a build of the vector-space form.** The manifold form adds frame
independence of `covDerivAlong` across trivialisations. That was never stated in this project, and it is
classed by reading in the result, not claimed.*

### Budgets

| probe | budget |
|---|---|
| T1 | **300 lines** |
| T2 | **300 lines** |
| T3a | **250 lines** |
| T3b | **250 lines** |

*A probe that does not build with no `sorryAx` inside its budget leaves its item THEORY, with the lemma it
stopped on named. All probes go in `lean/probes/`, imported by nothing.*

## Predictions

| probe | builds inside budget |
|---|---|
| T1 | **0.45** — *a linear ODE on a compact interval. Global existence needs a Lipschitz bound over the whole interval, which I expect `PicardLindelof.lean` to give if the interval is set up as its hypotheses want* |
| T2 | **0.4** — *local existence for a `C¹` field on `E × E`, then translating `x″ + Γ(x)(x′, x′) = 0` into `covDerivAlong` on the model space* |
| T3a | **0.5** — *uniqueness of integral curves is what the group law needs, and `IntegralCurve/ExistUnique.lean`'s name suggests it is there* |
| T3b | **0.1** — *smooth dependence on initial data is the piece I named as deferred* |
| **builds, of 4** | **central 1.5**, band 0–3 |

## ⛔ The negative — the order's, symmetric, scored on a rule fixed now

| builds | scored |
|---|---|
| **≥ 3 of 4** | **the rule over-classes** — the bound moves down, even where `mathlib` defers |
| **≤ 1 of 4** | **THEORY is a real category** — the 82 per cent is closer to a measure than a bound |
| **2 of 4** | **mixed** — reported by naming which two built and which did not, with the lemma each stopped on, and not rounded either way |

***The direction goes in the first line of the result.*** *T1 and T2 carry their scope cut. A vector-space build
counts as a build, and the result says beside it that the manifold form is classed by reading.*

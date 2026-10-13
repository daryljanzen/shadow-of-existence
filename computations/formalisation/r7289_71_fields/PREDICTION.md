# `r7289+71.1` — PRE-REGISTRATION: G4, physics on a background — the Einstein tensor, the wave operator and the covariant derivative of a tensor, with the connection and the background both hypotheses; the `32` sub-classed now; and the order's symmetric negative

*Committed and pushed before any probe is written and before any `mathlib` file is read for this order. The order is
`FOR_71.md` §`re r7289`.*

***What I already know, and so cannot predict blind.***
- *From `r7287`, in `lean/probes/CurvatureProbe.lean`:*
  - *`curv`, `C^∞`-linear in all three slots;*
  - *`ricci` and `scal` over a fibre;*
  - *the model formula on `E`;*
  - *`covConf a` with `Ric = (log a)″ η` and `R = 2 (log a)″/a²`.*
- *From `r7259`: `Physlib` states the Friedmann equations at the level of the scale factor, and `def FLRW : Type :=
  sorry`. `mathlib` has no Einstein tensor.*
- *I have read the one-line `claim` and my `r7285` reading of each of the `32` G4 receipts, and nothing else about
  them.*

## The `32`, sub-classed now — by what their stand-in statement needs beyond G0–G2

| sub-class | receipts | needs | count |
|---|---|---|---|
| **G4a — field equations** | 13, 35, 48, 49, 51, 53, 54, 74, 75 | the Einstein tensor `Ric − ½ R g`, `Λ`, a stress tensor | **9** |
| **G4b — wave and mode operators** | 8, 65, 76, 95 | `□` on functions; on symmetric 2-tensors for 65 | **4** |
| **G4c — follows if G4a and G4b do** | 67 (TT harmonics, eigenvalue 6: an operator equation); 23 (counterterm reduction: curvature identities plus EOM terms) | as G4a, G4b | **2** |
| **G4d — thermodynamic definitions** | 11, 109 | `κ` (G1) and `T = κ/2π`, `S = A/4` as definitions | **2** |
| **G4e — also needs G3** | 20 (momentum constraint), 46 (horizon areas), 58 (ADM kinetic term) | extrinsic curvature or an induced area | **3** |
| **G4f — spectral, heat-kernel, quantum** | 24, 57, 60, 63, 64 (heat-kernel / zeta / anomaly); 68 (completeness); 66 (an action's cubic vertex — needs the volume form); 70, 73 (perturbative energy shifts) | spectral theory of Laplace-type operators on a manifold, or the volume form | **9** |
| **G4g — spin** | 82, 84, 85 | a spin structure, the spinor bundle, the Dirac operator | **3** |
| | | | **32** |

## The probes, fixed now — in `lean/probes/`, imported by nothing, the connection and the background hypotheses throughout

| probe | items | statement | budget |
|---|---|---|---|
| **F1** | G4a | the Einstein tensor `Ein = Ric − ½ R g` over a fibre (on K3's `ricci`, `scal`); the vacuum-with-`Λ` and perfect-fluid equations as predicates; **instance:** `Ein` of `covConf a` vanishes identically (two dimensions) | **150 lines** |
| **F2** | G4b | `Hess f (X,Y) = X(Yf) − (∇_X Y) f` for a `cov` taken as a hypothesis, `C^∞`-linear in `X` and `Y`; `□ f` its `g`-trace over a fibre; **instance:** on `covConf a`, `□ f = a⁻² (−f_ηη + f_xx)` | **250 lines** |
| **F3** | G4b (65), G4a's divergence | `∇T (X; Y, Z) = X(T(Y,Z)) − T(∇_X Y, Z) − T(Y, ∇_X Z)` for a `(0,2)` field `T`, `C^∞`-linear in `X`, `Y`, `Z` | **200 lines** |

***G4f and G4g are classed by a SEARCH, not a probe.*** *After this file is pushed, `mathlib` and `Physlib` are
searched for:*
- *a heat kernel or heat semigroup on a manifold, zeta-regularised determinants, and spectral decomposition of an
  elliptic operator on a compact manifold;*
- *a spin structure, a spinor bundle, and a Dirac operator on a manifold.*

*Each hit is read before it is called present. If absent, the sub-class is THEORY by the rule, with the patterns
searched stated.*

## Predictions

| quantity | central | band |
|---|---|---|
| F1 builds | **0.8** | — |
| F2 builds | **0.55** | — |
| F3 builds | **0.6** | — |
| heat kernel / zeta on a manifold present | **0.1** | — |
| spinor bundle / Dirac operator present | **0.1** | — |
| **G4 statable, if F1–F3 build** | **17** (G4a + G4b + G4c + G4d) | 12–22 |

## ⛔ The negative — the order's, symmetric, scored on a rule fixed now

| outcome | scored |
|---|---|
| **F1, F2, F3 all build, AND the statable part of G4 ≥ `22` of `32`** (two-thirds) | ***G4 STATABLE*** — three strata of six, and the statable count passes half of `111` |
| **F1, F2, F3 all build, statable part `< 22`** | ***G4 SPLITS*** — the field equations are statable, and the remainder is named by what blocks it (G3, spectral theory, spin). *Whether that remainder is "about the field equations rather than the geometry" is answered by those names, not asserted.* |
| **F1, F2 or F3 fails** | ***G4 BLOCKED on the field equations***, at the lemma named — the order's second branch, *a different kind of obstruction from anything measured so far* |

- ***My probabilities:*** *statable 0.15; splits **0.6**; blocked 0.25.*
- *The `22` is fixed now because the sub-classes are fixed now: on my reading, G4f and G4g alone are `12` of `32`,
  so "statable" needs one of those classes to be cheaper than I expect.*

## The order's other constraint

***The port is not begun, and nothing here begins it.*** *Every probe takes the connection as a hypothesis, or uses
`covConf`, the one explicit connection in the tree.*

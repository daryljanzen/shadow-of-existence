# `r7291+71.1` — PRE-REGISTRATION: G3, the submanifold stratum — the induced metric of a map, the second fundamental form for a connection taken as a hypothesis, and one instance; the `17` and the `3` of G4e sub-classed now; and the order's symmetric negative

*Committed and pushed before any probe is written and before any `mathlib` file is read for this order. The order is
`FOR_71.md` §`re r7291`.*

***What I already know, and so cannot predict blind.***
- *The tree as of `r7289`:*
  - *curvature, `C^∞`-linear;*
  - *Ricci, scalar and Einstein over a fibre;*
  - *`Hess`, `□`, and `∇` of a `(0,2)` field;*
  - *`covConf a` with its curvature, Ricci, scalar curvature, Einstein tensor and wave operator in closed form.*
- *I have read the `r7285` reading and the one-line `claim` of each of the `17` G3 receipts and of G4e's three, and
  nothing else about them.*

## The `17`, sub-classed now — and the three of G4e that wait on G3

| sub-class | receipts | needs | count |
|---|---|---|---|
| **G3a — induced metric** of an embedding or a parametrised surface (with its intrinsic curvature where stated) | 9, 10, 50, 52, 61, 108 | the pullback of a metric along a map; for 52 and 108, G2 applied to it | **6** |
| **G3b — a slice's intrinsic curvature** | 32, 34, 36, 38, 103 | induced metric, then G2 | **5** |
| **G3c — extrinsic curvature** of slices or a foliation (shear, umbilic, `K_ab`, the ADM identity) | 7, 47, 79, 94, 102 | the second fundamental form `K(X,Y) = g(∇_X N, Y)` | **5** |
| **G3d — a foliation as an object** | 107 | level sets of a function with nonvanishing differential | **1** |
| | | | **17** |
| G4e-20 (momentum constraint) | 20 | G3c and F3's `∇` | *unblocked if G3c is* |
| G4e-58 (ADM kinetic term) | 58 | G3c | *unblocked if G3c is* |
| G4e-46 (horizon AREAS) | 46 | an AREA — the volume form, `r7267` B9, THEORY | ***not unblocked by G3*** |

***So the order's `89` is `88` on this reading.*** *If G3 is statable: `69 + 17 + 2 = 88` of `111`. Receipt 46 waits
on the volume form, which is already on the record as a THEORY item. That makes the residual three named things,
not two:*
- *spectral theory;*
- *spin;*
- *the volume form.*

*The volume form is not a new obstruction. It has been THEORY since `r7267` and is already named under G2's four
volume-form receipts.*

## The probes, fixed now — sections of `lean/probes/CurvatureProbe.lean`, imported by nothing, the connection and the metric hypotheses throughout

| probe | items | statement | budget |
|---|---|---|---|
| **S1** | G3a, G3b | `pullG φ g` — the pullback `(φ*g)_y(u,v) = g_{φ y}(dφ u, dφ v)` along a smooth map; symmetric if `g` is. **Instance (receipt 50, in 1+1):** the flat slicing `(τ, x) ↦ X` of the de Sitter hyperboloid `−X₀² + X₁² + X₂² = α²` in `ℝ^{1,2}` lies on it, and pulls `−dX₀² + dX₁² + dX₂²` back to `−dτ² + e^{2τ/α} dx²` | **250 lines** |
| **S2** | G3c | the second fundamental form `sff cov g N X Y = g(∇_X N, Y)` for a field `N`, `C^∞`-linear in `X` and `Y`; **symmetric** when `N` is `g`-normal to `X`, `Y`, `cov` is torsion-free and compatible, and `[X, Y]` is tangent. Compatibility enters as `IsCompatible`-type hypotheses, as in layer 3. | **200 lines** |
| **S3** | instance, scored beside the rule | on `covConf a`, the slices `η = const` with unit normal `N = a⁻¹ ∂_η`: `K(∂_x, ∂_x) = a′(η)` | **150 lines** |

***G3d is classed by reading:*** *a foliation by level sets of a submersion is a definition over `mfderiv`.*

***Searched after this file is pushed:*** *`mathlib` for submanifolds, immersions, embeddings, a second fundamental
form, and pullback metrics. Each hit is read before it is called present.*

## Predictions

| quantity | central |
|---|---|
| S1 builds (with the instance) | **0.6** — *the instance's `fderiv` of a three-component map is the cost* |
| S2 builds | **0.65** |
| S3 builds | **0.5** |
| `mathlib` has a second fundamental form | **0.1** |

## ⛔ The negative — the order's, symmetric, scored on a rule fixed now

| outcome | scored |
|---|---|
| **S1 and S2 both build** | ***G3 STATABLE*** — the count becomes `88` of `111`, and the residual is spectral theory, spin and the volume form, all three named absences |
| **S1 or S2 stops on a named lemma** | ***a THIRD kind of obstruction*** — about submanifolds, named by that lemma, and the residual has three things in it that are not the volume form |

- *S3 is scored beside the rule.*
- ***My probability that G3 comes back statable: 0.65.***

## The order's other constraint

***The port is not begun, and nothing here begins it.***

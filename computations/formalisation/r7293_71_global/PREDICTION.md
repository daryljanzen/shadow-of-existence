# `r7293+71.1` — PRE-REGISTRATION: G5, the global stratum — the `10` sub-classed now, three probes under budgets (a product metric with the round sphere, a periodic identification as a covering with its cyclic deck action, and a continuation seam that is `C¹` and not `C²`), two receipts classed by a search fixed now, and the order's symmetric negative

*Committed and pushed before any probe is written and before any `mathlib` file is read for this order. The order is
`FOR_71.md` §`re r7293`.*

***What I already know, and so cannot predict blind.***
- *The tree as of `r7291`:*
  - *`pullG`, the induced metric along a map, with composition;*
  - *`sff`;*
  - *curvature, Ricci, scalar and Einstein over a fibre;*
  - *`covConf` and its slices.*
- *From `r7291`'s search: `mathlib` has immersions, embeddings and submersions (`Immersion.lean`,
  `SmoothEmbedding.lean`, `Submersion.lean`).*
- *I know by general familiarity, NOT from reading for this order, that `mathlib` has:*
  - *`AddCircle`;*
  - *`IsCoveringMap`;*
  - *the unit sphere in a Euclidean space as a manifold;*
  - *Lie groups;*
  - *a Killing form.*
  - *Whether each reaches what a probe needs is what the probes and the search measure.*
- *I have read the `r7285` reading of each of the `10` G5 receipts and the first lines of its docstring, and
  nothing else about them.*

## The `10`, sub-classed now — by what their stand-in statement needs beyond G0–G3

| sub-class | receipts | what the stand-in states | needs | count |
|---|---|---|---|---|
| **G5a — a metric identified as a product** | 21 (Nariai → `dS₂ × S²`), 97 (the slice is `ℝ × S²` with `−f dχ² + r² dΩ²`), 100 (the layer's metric tends to `dS₂ × S²`), 104 (`dS₂ × S²` radii; flat induced 3-metric) | in coordinates, a metric equals `g₁ ⊕ g₂` on a product, with a round `S²` factor of a given radius | the product of two metrics, and the round metric on `S²` | **4** |
| **G5b — a periodic identification** | 40 (deck group `ℤ_{D−1}` from the imaginary period), 18 (branched covering, its flat connection) | a coordinate identified mod a period is a covering, and a cyclic group acts freely as deck transformations | a covering map onto a circle, and a free cyclic action | **2** |
| **G5c — continuation across a seam, and real forms** | 37 (`θ → π/2 + iψ`, a `C¹`-not-`C²` join with signature flip), 106 (Wick rotation identifies the `dS₅` quadric with `S⁵`) | the warp factor glued from `cos` and `cosh` is `C¹` and not `C²` at the seam; `X₀ ↦ i X₀` carries one complex quadric onto the other | real analysis on one variable, and a linear map on `ℂⁿ⁺¹` | **2** |
| **G5d — a homogeneous space** | 80 (dS as a coset space with the Killing-form metric) | `G/H` as a manifold, with the metric induced by the Killing form | the quotient of a Lie group by a closed subgroup as a manifold | **1** |
| **G5e — global causal structure** | 26 (horizons sorted by completion) | horizons as boundaries of causal pasts of inextendible curves; completeness | causal curves, causal past, inextendibility on a Lorentzian manifold | **1** |
| | | | | **10** |

***18 is classed with G5b on this reading:*** *off its branch locus, a branched covering is a covering. **18 is
counted statable iff P2 builds**, with "off the branch locus" said beside the score. A branched covering as an
object is searched for, and if it is absent, that is said too.*

## The probes, fixed now — new sections of `lean/probes/CurvatureProbe.lean`, imported by nothing

| probe | items | statement | budget |
|---|---|---|---|
| **P1** | G5a | `prodG g₁ g₂ = pr₁*g₁ + pr₂*g₂` on `M₁ × M₂`, built from S1's `pullG`; symmetric if both are. **Instance:** the round metric of the unit `S²` is `pullG` of the Euclidean inner product along the inclusion `S² → ℝ³`, and it is **positive definite** on each tangent space | **200 lines** |
| **P2** | G5b | for `β > 0`, the quotient `ℝ → AddCircle β` is a covering map; for `n ≥ 1`, rotation by `β/n` generates a cyclic group of order `n` acting freely on `AddCircle β` | **150 lines** |
| **P3** | G5c | (i) `w(s) = cos s` for `s ≤ 0`, `cosh s` for `s > 0`, is `C¹` at `0` and NOT `C²` at `0`; (ii) on `ℂⁿ⁺¹`, `X ↦ (i X₀, X₁, …, Xₙ)` maps `{−X₀² + Σ Xᵢ² = α²}` onto `{Σ Xⱼ² = α²}` bijectively | **200 lines** |

***G5d and G5e are classed by a SEARCH, not a probe.*** *After this file is pushed, `mathlib` is searched for:*
- *the quotient of a Lie group by a closed subgroup as a manifold, or a homogeneous space with a smooth structure;*
- *Lorentzian causal structure: causal or timelike curves, causal past or future, inextendible curves, global
  hyperbolicity;*
- *a branched covering, for 18's own object.*

*Each hit is read before it is called present. If absent, the receipt is **THEORY** by the rule, with the patterns
searched stated.*

## Predictions

| quantity | central |
|---|---|
| P1 builds (with the instance) | **0.65** — *the sphere's tangent space and the derivative of its inclusion are the cost* |
| P2 builds | **0.55** |
| P3 builds | **0.6** — *`¬ C²` needs the second derivative from each side* |
| homogeneous space `G/H` as a manifold present | **0.2** |
| Lorentzian causal structure present | **0.05** |
| branched covering present | **0.1** |

## ⛔ The negative — the order's, symmetric, scored on a rule fixed now

| outcome | scored |
|---|---|
| **P1, P2, P3 all build, AND G5d and G5e are both reachable** (present, or a definition over what is present) | ***G5 STATABLE*** — the count becomes `98` of `111`, and the map closes with no global obstruction |
| **P1, P2, P3 all build, and G5d or G5e is absent** | ***G5 SPLITS*** — `8` statable (`96` of `111`), and the absent one is ***a THIRD kind of obstruction, global***, named by what the search did not find. *By the order: "the `r7291` reading that there were only two was premature."* |
| **P1, P2 or P3 fails** | ***G5 BLOCKED*** at the lemma named — also a third kind, and named by that lemma rather than by an absence |

- ***One correction to the order's arithmetic, stated now so it cannot be bent later.***
  - *If G5 is statable, the residual is `111 − 98 = 13`, not "exactly the two named absences": spectral `9`,
    spin `3`, AND receipt 46's volume form `1`.*
  - *The volume form is THEORY since `r7267` and is not global. So "statable" closes the map with three named
    items in the residual, two of them absences.*
- ***G5e on its own can split the stratum.*** *My reading is that causal structure is a set of DEFINITIONS over G1
  (a causal curve is `g(γ′, γ′) ≤ 0`, `J⁻` is a set), so "reachable" for G5e means **a definition over what is
  present**, and the search scores whether its parts are there. A definition I would have to WRITE is not
  present; it is reachable only if its constituents are, and the result will list them.*
- ***My probabilities:*** *statable **0.3**; splits **0.5**; blocked **0.2**.*

## The order's other constraint

***The port is not begun, and nothing here begins it.***

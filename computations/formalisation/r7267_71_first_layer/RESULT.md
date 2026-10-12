# `r7267+71.2` — RESULT: the first missing layer is 11 of 20 present, 2 THEORY items, so the pre-registered rule scores a THEORY problem; but neither THEORY item is on `I20`'s path, and Physlib tracks the FLRW type and not the layer under it

*Read against `PREDICTION.md` in this directory, pushed at `r7267+71.1` before any search. The pre-registration
is not revised. The list of twenty is the list. One item I would add now is recorded at the end as an omission
and is not counted.*

*Sources: `mathlib` `4e6064a4` (the source in `lean/.lake/packages/mathlib`); `Physlib` `b0e7ca1c` (in
`lean-physlib/.lake/packages/Physlib`) and its live head `89d99e8` (a shallow clone of
`leanprover-community/physlib`, committed `2026-10-12T20:15Z`). Every PRESENT line names a declaration and its
place. Every ABSENT line names its search.*

## ① The count

| | central | band | **measured** |
|---|---|---|---|
| A present (of 11) | 10 | 9–11 | **11** ✔, above central |
| B present (of 9) | 0 | 0–1 | **0** ✔ |
| **present / 20** | 50 % | 40–60 % | **11 / 20 = 55 %** ✔ |
| absent classed **THEORY** | 3 | 2–5 | **2** ✔, at the floor |
| absent classed DEF or PORT | 7 | 5–9 | **7** ✔ (6 DEF, 1 PORT) |
| B1 probe builds with no `sorryAx` | yes, 0.85 | — | **yes** ✔ |

### A — what the layer would be built FROM: 11 of 11 present

| # | declaration | place in `mathlib` |
|---|---|---|
| A1 | `TangentSpace.vectorBundle` | `Geometry/Manifold/VectorBundle/Tangent.lean` l.189 |
| A2 | `ContMDiffSection` | `Geometry/Manifold/VectorBundle/ContMDiffSection.lean` |
| A3 | the hom-bundle, smooth | `Geometry/Manifold/VectorBundle/Hom.lean`, `Topology/VectorBundle/Hom.lean`; used as `F →L[ℝ] F →L[ℝ] ℝ` in `ContMDiffRiemannianMetric.contMDiff` |
| A4 | `LinearMap.SeparatingLeft`, `LinearMap.Nondegenerate` | `LinearAlgebra/SesquilinearForm/Basic.lean` l.525, l.547 |
| A5 | `LinearMap.IsSymm`, `LinearMap.BilinForm.IsSymm` | `…/SesquilinearForm/Basic.lean` l.149; `…/BilinearForm/Properties.lean` l.88 |
| A6 | `QuadraticForm.equivalent_signType_weighted_sum_squared` | `LinearAlgebra/QuadraticForm/Real.lean` l.78 |
| **A7** | **`QuadraticForm.sigPos`, `sigNeg`, `sigPos_of_equiv_weightedSumSquares`, `sigNeg_of_equiv_weightedSumSquares`, `QuadraticMap.Equivalent.sigNeg_eq`** | **`LinearAlgebra/QuadraticForm/Signature.lean` l.65, l.98, l.243, l.251, l.133** — *the uniqueness half of Sylvester's law, by its own header* |
| A8 | `Matrix.indefiniteDiagonal` | `Algebra/Lie/Classical.lean` l.175 |
| A9 | `LinearMap.BilinForm.toDual` (nondegenerate, finite dimension) | `LinearAlgebra/BilinearForm/Properties.lean` l.350 |
| A10 | `Bundle.RiemannianMetric`, `RiemannianBundle` | `Topology/VectorBundle/Riemannian.lean` l.370, l.420 |
| A11 | `ContMDiffRiemannianMetric` | `Geometry/Manifold/VectorBundle/Riemannian.lean` l.245 |

***A7 was my one expected absence, and it is present.*** *`Signature.lean` is copyright 2026, David Loeffler, from
work by Sina Keller, Philipp Schumann and Nicolas Trutmann. **The signature of a real quadratic form is defined
intrinsically, as the maximal dimension of a definite subspace, and is proved to equal the count of signs in any
diagonalisation.** That is the piece that makes "index 1" a definition rather than a theorem.*

### B — what the layer itself would add: 0 of 9 present, and how each absence is classed

*The search for every B line: `grep -rliE` over `Mathlib/` for `pseudo.?riemann`, `semi.?riemann`, `lorentz`,
`minkowski space|minkowskiMetric|MinkowskiSpace`, `warped`, `musical|flat.*sharp`, and
`Measure|volume` in `Geometry/Manifold`. **Zero hits** for the first five patterns. The musical isomorphism
occurs only inside `LeviCivita.lean`, pointwise. The manifold measure hits are path length (`PathELength.lean`)
and not a volume.*

| # | needed | class | why, by the rule fixed at `+71.1` |
|---|---|---|---|
| **B1** | pseudo-Riemannian metric structure | **DEF — by measurement** | *the probe below builds, no `sorryAx`* |
| B2 | the index at a point | **DEF** | `sigNeg` of the fibre form's quadratic map (A7); no proof obligation |
| B3 | the index is locally constant | **THEORY** | needs lower semicontinuity of `sigPos` and `sigNeg` along a continuous family of nondegenerate forms. `sigPos_add_sigNeg_add_radical` (l.232) supplies only the half that makes their sum constant. *No proof to port: the Riemannian case has no index.* |
| B4 | Lorentzian metric | **DEF** | B1 plus `sigNeg = 1` at every point (B2) |
| B5 | the musical isomorphisms as smooth bundle maps | **DEF** | pointwise `BilinForm.toDual` (A9). Smoothness of the inverse by `contDiffAt_map_inverse` (`Analysis/Calculus/ContDiff/Operations.lean` l.845). ⚠ *Classed by reading, not probed. The least certain DEF on the list.* |
| **B6** | Levi-Civita, existence and uniqueness, nondegenerate | **PORT** | read at source below |
| B7 | Minkowski space as an instance of B1 | **DEF** | `riemannianMetricVectorSpace` (`Riemannian/Basic.lean` l.102) is the template: a constant form, smoothness by `contMDiffAt_const`. Swap `innerSL` for the `indefiniteDiagonal` form; nondegeneracy is a matrix fact. |
| B8 | the warped product `−dt² + a(t)² g` | **DEF** | the same template, a form depending smoothly on `t`. Nondegeneracy needs `a t ≠ 0`, a hypothesis. |
| B9 | the metric's volume density | **THEORY** | *`mathlib` has no measure induced by a metric on a manifold, **in the Riemannian case either**, so there is no proof to port. It needs the chart-gluing of densities that the library does not have.* |

**B6, read at source** (`Geometry/Manifold/VectorBundle/CovariantDerivative/LeviCivita.lean`, 415 lines).
- *`mathlib` constructs the Riemannian Levi-Civita connection (`leviCivitaConnection`) and proves the Koszul
  formula and uniqueness. **The fibre inner product's positivity enters at exactly two named places:***
  - injectivity: `injective_inner_mdifferentiableAt_section`, l.96, and its `C^n` twin at l.109, both through
    `inner_self_eq_zero` (l.102, l.115). Every later use of positivity goes through these two lemmas (l.260,
    l.341, l.349, l.401);
  - the Riesz map: `leviCivitaAuxOfMDiffAt`, l.310, through `InnerProductSpace.toDual`.
- **Each has a nondegenerate-form replacement in `mathlib`:** `LinearMap.SeparatingLeft` (A4) and
  `LinearMap.BilinForm.toDual` (A9), finite dimension. *The Koszul formula itself is algebra in `⟪·,·⟫` and does
  not use positivity.* ⇒ **PORT.**
- ⚠ *What PORT costs, said as a number so it is not mistaken for zero.* Every declaration reaches the form
  through the `InnerProductSpace` instance that `RiemannianBundle` registers on each fibre. So the port is a
  re-plumbing onto an explicit bilinear form:
  - `LeviCivita.lean`: **22** declarations, 91 inner-product references;
  - `CovariantDerivative/Metric.lean`: **10** declarations, 22 references;
  - **32 in all.**
  - `CovariantDerivative/Basic.lean` (28) and `Torsion.lean` (11) carry **zero** inner-product references and
    are reused as they stand. *The counts are `grep -cE` of declaration keywords and of
    `⟪|inner|InnerProductSpace|RiemannianBundle|\.pos\b`, per file.*

### The B1 probe — DEF by measurement

*`computations/formalisation/lean/probes/PseudoRiemannianProbe.lean`, run with
`lake env lean probes/PseudoRiemannianProbe.lean`. Raw output: `PROBE_RUN.txt` beside this file. **Not imported
by `ShadowFormal`. Nothing is built on it, as ordered.***

- **What it is:** `ContMDiffRiemannianMetric` with `pos` and `isVonNBounded` replaced by one field,
  `nondegenerate`. *`isVonNBounded` exists only to make the inner product's norm agree with the fibre topology.
  An indefinite form defines no norm, and the tangent fibres keep the model space's topology.*
- **Its one proof obligation, `ofRiemannian`:** every smooth Riemannian metric is a pseudo-Riemannian one. Two
  tactic lines from `pos`.
- **Axioms read:** `'ShadowProbe.ofRiemannian' depends on axioms: [propext, Classical.choice, Quot.sound]`, and
  the same for `ofRiemannian_inner`. **7.5 s.**
- *One fix before it built:* `ℕ∞ω` is scoped notation and needed `open scoped ContDiff`. That was a syntax
  error, not a missing fact.
- ⌗ *The probe's reading carries no planted control of its own. It is a direct `#print axioms` with the same
  allow-list as `check_no_sorry.py`, whose gate zero passes in CI on every push to `lean/`.*

## ⛔ The reachable negative — DID NOT FIRE under its rule, and what the rule could not see

***THEORY = `2` (B3, B9). The rule fixed at `+71.1` says THEORY `≥ 2` is a theory problem. So the negative does
not fire, and I do not say `r7263`'s sentence should be withdrawn.*** *That is the scoring, given first.*

***And then one reading that is NOT pre-registered, labelled as such, because it is the most useful thing the
count shows.*** *Neither THEORY item is on the path to stating `I20`'s first layer:*

- **B3**, the index constant on a connected manifold, is needed only if "Lorentzian" is defined as index 1
  somewhere. Defined as index 1 at every point — B4 as classed — B3 is never invoked.
- **B9**, the volume density, does not appear in `I20` at all. Its statement is a Lie derivative of the metric
  and a conserved charge.

⇒ ***On `I20`'s path, the first layer is B1, B2, B4 and B8, all DEF, with B6 (PORT) if a connection is wanted.
THEORY on that path: `0`.*** *I wrote the list of twenty before the search, and two of its items turned out to be
off the path. A rule scored over the list cannot see that. **I do not use this to fire the negative after the
fact. It is what a pre-registration owes: the scoring as written, then the reading, labelled.***

⌗ ***What this does NOT measure, so it cannot carry the withdrawal either way.*** *Layers 2 to 5 — the Lie
derivative of a tensor and Killing fields, curvature, geodesics, Einstein's equations — are not measured here.
`r7263`'s sentence is about "the geometric core", and layer 1 is not the core. **On the measured layer, the
distance is a definition problem plus a 32-declaration port. Whether the sentence stands is decided by layer 2,
which is unmeasured.***

## ② Is the gap tracked in Physlib? — the FLRW TYPE is tracked; the LAYER UNDER IT is not; no item has an owner

| | prediction | measured |
|---|---|---|
| tracked | yes, 0.7 | **split** — see below |
| owned | 0.3 | **no** |

- **The FLRW type is tracked.** A `TODO` follows `def FLRW : Type := sorry` (`Physlib/Cosmology/FLRW/Basic.lean`
  l.101–109, at `b0e7ca1c` and at the live head `89d99e8`). *It asks for a structure bundling the scale factor
  and the spatial geometry, **not for a metric on a spacetime manifold**.*
- **The curvature is tracked, but only as a consequence.** `TODO "Prove that the Milne solution … has vanishing
  scalar curvature"` (`Solutions.lean` l.532). And the overview, read at source:
  `neither the curvature of the FLRW metric nor a perturbation theory of the Friedmann equations is available
  yet` (l.21–22, unchanged at `89d99e8`).
- **The layer under it is not tracked.** *Searched: `grep -rliE
  "pseudo.?riemann|lorentzian manifold|lorentzian metric|einstein field|ricci"` over `Physlib/`, `PhyslibAlpha/`,
  `QuantumInfo/` and `docs/` at both commits, and every `TODO "` body (78 files) for
  `metric|manifold|curvature|lorentz|geodesic|christoffel|einstein|spacetime`.* **Zero hits for a Lorentzian or
  pseudo-Riemannian manifold.** The Lorentz-related TODOs are about the Lorentz group and tensor
  representations, and the `SpaceTime` TODO is a refactor of flat `SpaceTime d`.
- **No owner.** *Physlib's `TODO` command carries a string and a hash tag, nothing else (`Physlib/Meta/TODO/Basic.lean`
  l.20–48), so a TODO cannot be owned.*
- ⚠ ***GitHub issues: NOT YET CHECKED.*** *This session reads Physlib's git anonymously. Its issue list needs the
  repository attached with credentials, and a read does not justify that. The answer above rests on source at
  two commits, and an issue tracking the layer is possible.*

⇒ **The answer to the order's question:**
- **Physlib is not working on the layer the gap lives in.** It is working on the cosmology *above* that layer.
- **`mathlib` is the side that is moving.** `Signature.lean` is from 2026. `LeviCivita.lean`'s header says
  "Future PRs will prove smoothness".
- *So the gap to wait for is on the `mathlib` side, and only for the Riemannian half. The pseudo-Riemannian half
  is unremarked in both libraries' source.*

## ⌗ A correction to my own `r7265` result

*`r7265_71_sinh_law/RESULT.md` quotes Physlib as saying the FLRW curvature is "not available yet". The source
sentence is `neither the curvature of the FLRW metric nor … is available yet`. The meaning is the same, but the
quotation marks held a compression. **That file is left as merged, and the exact sentence is above.***

## Omission, recorded and not counted

*An item I would add to the list now:* **the Lie derivative of a (0,2)-tensor along a vector field.** It sits at
the boundary of layers 1 and 2, and it is the operation `I20`'s check ① computes. `mathlib` has
`VectorField.mlieBracket` (my `r7259` reading), which is the Lie derivative of a vector field only. It is not on
the list, so it is not in the count.

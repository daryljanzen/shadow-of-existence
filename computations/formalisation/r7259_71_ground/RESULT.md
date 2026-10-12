# `r7259+71.5` — RESULT against the pre-registration: what `mathlib` and `Physlib` carry, the cost of stating I20, and the slice

*Read against `PREDICTION.md` in this directory, pushed at `r7259+71.3` before anything below was opened. Every
band is reported, including the misses. Library state: `mathlib4` at `4e6064a4a3a617a3ba6739b50152b02e4d6ad3ea`
and `Physlib` (the repository formerly called PhysLean, cloned from `HEPLean/PhysLean`) at
`b0e7ca1ccb215b1faf5dc7d4d7984cfda845abb8`, both cloned 2026-10-12.*

## Ⓐ The population — REPRODUCED, with one implementation bug disclosed

`classify_receipts.py`, run to completion here, prints `VERDICT: POPULATION REPRODUCED`:

| quantity | predicted | band | measured | the gate's |
|---|---|---|---|---|
| receipts | 1,043 | 1,000–1,090 | **1,043** ✔ | 1,043 |
| symbolic | 267 | 230–300 | **285** ✔ | 267 |
| numerical | — | — | 514 | 504 |
| corpus-measurement / arithmetic | — | — | 196 / 48 | 128 / 144 |

- **The bug in the first run.** It read 135 symbolic. The import pattern used `\s`, which spans newlines, so one
  match swallowed the lines after it and lost their imports. I fixed the implementation, left the rule as
  registered, and commented the fix in place.
- **The split the rule does not match.** My corpus-measurement pattern is wider than the gate's, so the
  corpus-measurement / arithmetic split differs. That does not touch the symbolic population.
- **A leak I measured rather than assumed.** In a blind sample of 12, one "symbolic" receipt
  (`L204_physics_reach/P7_the_temperature_is_taken_and_the_entropy_never_is`) is a word count over the papers
  that happens to import sympy. Across the 285, 48 open corpus text; none of those has fewer than three
  sympy/mpmath calls. So the pure-measurement leak is about one in twelve, and at most 48 of 285.

## Ⓑ The slice — MOSTLY MISSED, and in a direction that favours formalisation

*285 receipts, read one by one by five readers (scratch JSONL merged into `slice_reading.json` here). Each
reader recorded the first-fit bin, whether the receipt's subject is geometric, and whether its core is a
coordinate identity. I then cross-read a seeded sample of 12 blind (seed 7259071).*

| bin | predicted | band | measured | |
|---|---|---|---|---|
| A · finite / Galois | 8% | 3–15% | **17.9%** (51) | miss, above |
| B · exact algebra | 30% | 18–45% | **61.4%** (175) | miss, above |
| C · analysis | 35% | 22–50% | **17.9%** (51) | miss, below |
| D · differential geometry | 27% | 15–40% | **2.8%** (8) | miss, below — *partly an artefact, see below* |
| **algebraic slice A + B** | **38%** | 22–55% | **79.3%** (226) | **miss, above** |
| geometric *subject*, in any bin | — | — | **47.4%** (135) | — |
| …of which the core is a coordinate identity | 60% | 35–80% | **82.2%** (111 / 135) | miss, above by 2 points |

- **D is near empty partly because of how I built the rule.** The bins are taken in the order A, B, C, D.
  D is defined as geometry "not reducible to a B or C computation as actually performed". Four of the five
  readers found every metric, curvature or Killing receipt done as exact symbolic simplification, and put it
  in B. The fifth put 8 in D and said that on a strict reading they are B too. *So the bins measure how the
  receipts compute, not what they are about.*
- **The subject flag is the honest answer to the question the order asked.** 47% of the population is
  geometric in subject. That is about half: closer to the order's "most" than to my "about a quarter". On
  subject, my prior was wrong.
- **The sub-prediction that matters holds, a little above its band.** 82% of the geometric receipts verify a
  coordinate identity: a statement mathlib can write today, standing in for a geometric theorem it cannot write.
- **Readers' reliability: 8 of 12 agree with my blind reading.** The four disagreements are:
  - one B/A — a matrix commutant read as finite group theory;
  - two B/C — receipts that mix an exact identity with a quadrature;
  - the measurement leak above.

  *So the bin numbers are uncertain at about the ±15-point level. A+B at 79% is far enough from the stop
  threshold (15%) that this does not decide anything.*

## Ⓒ The libraries — the Lorentzian layer is ABSENT, as predicted, and two things are present that I had not predicted

*Every "present" below names a declaration I read at source. Every "absent" gives the patterns searched across
`Mathlib/` (or `Physlib/` and `PhyslibAlpha/`), with zero declaration hits, or with hits that are a different
object, named.*

| object | `mathlib` | `Physlib` | predicted |
|---|---|---|---|
| Riemannian metric on a manifold | **PRESENT** — `RiemannianMetric` (`Topology/VectorBundle/Riemannian.lean` l.370, with field `pos : 0 < inner b v v`), `RiemannianBundle` (l.420), `ContMDiffRiemannianMetric` (`Geometry/Manifold/VectorBundle/Riemannian.lean` l.245), `IsRiemannianManifold` (`Geometry/Manifold/Riemannian/Basic.lean` l.80) | — | present (0.6) ✔ |
| pseudo-Riemannian / Lorentzian metric on a manifold | **ABSENT** — searched `PseudoRiemannian`, `Lorentz`: 0 files; the only metric structure enforces `pos` | **ABSENT** — searched `PseudoRiemannian`: 0; `Lorentzian` occurs in 2 tensor files as vocabulary, not a manifold metric | absent ✔ ✔ |
| Minkowski metric / Lorentz group | absent — the 14 `Minkowski` files are the Minkowski inequality, functional, sum and geometry of numbers | **PRESENT** — `minkowskiMatrix` (`Relativity/MinkowskiMatrix.lean` l.69), `minkowskiProduct` (`Tensors/RealTensor/Vector/MinkowskiProduct.lean` l.93), **`LorentzGroup (d : ℕ)`** (`Relativity/LorentzGroup/Basic.lean` l.48) **for every d — so `SO(5,1)` is `LorentzGroup 5` as it stands** | ✔ ✔ |
| covariant derivative / **Levi-Civita** | **PRESENT, Riemannian only — not predicted**: `CovariantDerivative.IsLeviCivitaConnection` (`…/CovariantDerivative/LeviCivita.lean` l.202), `IsLeviCivitaConnection.uniqueness` (l.256), `leviCivitaConnection`; built on `RiemannianBundle` and fibre inner products (l.91, l.127), with `Torsion.lean` and `Metric.lean` beside it. `Christoffel`: 0 | absent: `Christoffel` 0 | absent (0.75) ✘ for mathlib — **but it cannot carry a Lorentzian metric** |
| Riemann / Ricci curvature | **ABSENT** — `Ricci`, `riemannCurvature`, `Curvature` in `Mathlib/Geometry`: 0 | **ABSENT** — `Ricci` 0; FLRW's own header: *"neither the curvature of the FLRW metric … is available yet"* | ✔ ✔ |
| Killing / conformal-Killing vector field | **ABSENT** — the 13 `Killing` files are the Killing *form* of a Lie algebra (`Algebra/Lie/Killing.lean` and others) | absent — one file, the `SU(n)` Killing form | ✔ ✔ |
| Lie bracket of vector fields | **PRESENT** — `VectorField.mlieBracket` (`Geometry/Manifold/VectorField/LieBracket.lean`) | — | ✔ |
| Lie derivative of a tensor field | **ABSENT** — `lieDerivative`: 0 | absent: 0 | ✔ ✔ |
| geodesics of a metric | **ABSENT** — the only `IsGeodesic` is the word metric of a group (`Geometry/Group/WordMetric.lean` l.68) | absent: `Geodesic` 0; `geodesic` appears in FLRW docstrings only | ✔ ✔ |
| Einstein equations | **ABSENT** — the one `Einstein` file is CHSH | **stated at scale-factor level only**: `FirstOrderFriedmann`, `SecondOrderFriedmann` (`Cosmology/FLRW/Basic.lean` l.133, l.156), with **`def FLRW : Type := sorry`** (l.101); the GR file `PhyslibAlpha/Relativity/General/Schwarzschild/IncompressibleSphere.lean` *"takes the two metrics and the pressure as given (the field equations are not verified here)"* | ✔ ✔ |
| de Sitter space | **ABSENT** — 0 | `deSitterScaleFactor` (a scale factor `a(t)`, `Cosmology/FLRW/Solutions.lean`), not a spacetime | ✔ ✔ |
| Galois theory | **PRESENT** — `IsGalois` (`FieldTheory/Galois/Basic.lean` l.55), `Polynomial.Gal` (`FieldTheory/PolynomialGaloisGroup.lean` l.56) | — | ✔ |
| finite groups | **PRESENT** — `alternatingGroup` (`GroupTheory/SpecificGroups/Alternating.lean` l.73) and the whole permutation-group library | — | ✔ |
| `SU(n)`, `so(p,q)` | **PRESENT** — `Matrix.specialUnitaryGroup` (`LinearAlgebra/UnitaryGroup.lean` l.272+); **`LieAlgebra.Orthogonal.so'` with `indefiniteDiagonal` and `soIndefiniteEquiv`** (`Algebra/Lie/Classical.lean` l.166–224), so `so(5,1)` as a matrix Lie algebra exists | `SpecialUnitary` Lie algebra | ✔ |
| quadratic forms | **PRESENT** — `QuadraticMap.Anisotropic` (`LinearAlgebra/QuadraticForm/Basic.lean` l.1056) | — | ✔ |
| **the cubic's discriminant** | **PRESENT, not predicted, and directly on the corpus's central object** — `Cubic.discr` (`Algebra/CubicDiscriminant.lean` l.463), `discr_ne_zero_iff_roots_nodup` (l.479), `discr_eq_prod_three_roots` (l.467). *The Nariai member is the zero of exactly this.* | — | — |

⇒ ***The order's reachable negative holds as stated: the Lorentzian foundations are not there.*** *mathlib has
gone further than I predicted in the Riemannian direction (a Levi-Civita connection, with uniqueness), and every
piece of it is tied to positive-definite fibre inner products. Physlib has the Lorentz group and the Minkowski
product in every dimension, but no metric on a manifold; its GR and cosmology state results as identities about
coefficient functions and scale factors.*

## Ⓓ The cost of STATING I20 — FIVE layers missing, as predicted

*I20 run to completion here first. Its own verdict line: `VERDICT: ALL PASS.`*

| layer, as pre-registered | needed for I20? | state |
|---|---|---|
| 1 · pseudo-Riemannian metric as a smooth (0,2)-tensor field | yes | **missing** in both |
| 2 · Lie derivative of that tensor along a vector field | yes | **missing** (the Lie bracket of vector fields exists) |
| 3 · the conformal-Killing equation | yes | **missing** |
| 4 · null vectors and null geodesics of the metric | yes | **missing** (null vectors of a quadratic form exist algebraically; geodesics do not exist) |
| 5 · de Sitter as the hyperboloid with its induced metric | **no** — I20 lives on conformal FLRW | statable as a **set** in Physlib (`minkowskiProduct x x = α²` in `Vector 5`), not as a manifold with an induced metric |
| 6 · the charge `g(K, γ̇)` along a null geodesic | yes | **missing** (needs 1 and 4) |

**Five missing, against a central prediction of 5 and a band of 3–6.**

- **What I20 actually verifies is statable today.** Matrices of real functions, derivatives and exact
  identities are all in mathlib. That is Physlib's own pattern, and it is the 82% of Ⓑ.
- **Read with a formal statement's eye** (`I20_which_checks_could_fail.py`, run here:
  `VERDICT: I20's CLAIMS HOLD, AND OF ITS TEN CHECKS ONE CANNOT FAIL …`), the ten checks sort as follows:
  - one carries the geometry: the Lie-derivative identity `L_ξ g = 2(a′/a) g`;
  - one cannot fail: the "ln(1+z) = ∫H dt" check never uses `H`;
  - one reads back an input asserted in a comment: `p^η = C/a²`, which I derived from the geodesic equation,
    and it is true;
  - two pass whenever `simplify` does not reach 0; re-run exactly here, both claims are true.

  *I20's claims are right. What the probe shows is that its pass is not evidence for them in four of ten
  places, and a Lean statement of the same content would show those four as trivial or as hypotheses.*

## Ⓔ The open derivation in `L221_the_bridge`

*The `{0,1,2}` derivation, as posed, cannot be stated: "a single condition" has no definition.* The
corpus's own B12 (`r2631`) argues that the two triples are different types of object: three roots of `f = 0`,
against three values `f = 0, 1, 2`. A formal statement would have to choose what "condition" means, and that is
the work the open item is missing, not a proof.

What is statable now, against my prior of 0.6:
- the Nariai factorisation `r³ − r + 2/(3√3) = (r − 1/√3)²(r + 2/√3)`;
- its vanishing `Cubic.discr`;
- the three level sets as three distinct points;
- the finite-group content (`Δ(27)` as a finite group, `SU(3)` as `Matrix.specialUnitaryGroup`).

## Ⓕ The toolchain — YES

`elan` installed through this container's network policy, and Lean `4.35.0-rc4` (the toolchain `mathlib4`
pins) now runs: `Lean (version 4.35.0-rc4, x86_64-unknown-linux-gnu, commit c29b6dda…, Release)`. *mathlib's
build cache was not fetched this order, so no Lean file has been compiled. That is the next step, not a claim.*

## ⛔ The two outcomes that would have made the order wrong

- **Algebraic slice below 15% → stop: NOT MET.** It is 79%. *Even taking the readers' disagreement at its
  worst, it is above 60%.*
- **Lorentzian layer present → reversal: NOT MET.** The layer is absent in both libraries, with the declarations
  named above.

*Every miss in Ⓑ is reported against its own band. The pre-registration was not revised.*

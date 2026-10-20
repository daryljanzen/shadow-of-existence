# `r7453+71.1` — THE LIBRARY GAPS AS A CLASS (`r7453` ③). ⌗ FOUR ROWS, TWO MISSING STRUCTURES, AND NEITHER BLOCKS A ROW'S COMPUTED CHECKS. ⌗ TWO OF THE FOUR ARE NOW BUILT (`70`, `96`); ONE LOCAL PIECE IS PRICED AND REGISTERED

*The four rows labelled `LIBRARY GAP` when `r7453` was written: `60`, `70` (spectral theory) and `89`, `96` (the
Levi-Civita volume form). Rows `70` and `96` were built while this was being written (campaigns 41 and 42), and
that build is part of the evidence below. The census does not move on this file: a row leaves the list only by
being `DONE`.*

## How the absences were searched — keyed on the object

Every claim of absence below was searched in the Mathlib source this lake build pins
(`lake-manifest.json`, mathlib rev `4e6064a4a3a617a3ba6739b50152b02e4d6ad3ea`, `.lake/packages/mathlib/Mathlib`).
For each object we searched four ways:

1. the concept under its other names;
2. the structure or typeclass that would carry it;
3. the files where it would have to live, opened and read;
4. for row 70's objects, the delegated agent also scanned the names of every constant in the environment loaded by
   `import ShadowEngine`.

A plain grep for one name is not counted as a search. File counts are the number of `.lean` files matching a
case-insensitive pattern.

| object | patterns searched (files matched) | the files that would carry it, read |
|---|---|---|
| curvature tensor of a connection | `curvature` (2, both unrelated: `VirtuallyCyclic`, `Measure/Doubling`), `riemannCurvature\|curvatureTensor\|RiemannTensor` (0), `Ricci` (0), `Bianchi` (0), `Weyl tensor\|weylTensor` (0), `scalar curvature` (0), `Christoffel` (0) | `Geometry/Manifold/VectorBundle/CovariantDerivative/{Basic,Metric,Torsion,LeviCivita}.lean`: covariant derivative, torsion, `IsLeviCivitaConnection`, the Koszul formula, uniqueness, `leviCivitaConnection`. ***No curvature is defined*** |
| an indefinite (Lorentzian) metric on a manifold | `pseudo-?riemannian\|lorentz` (0), `Minkowski` (number theory and convexity only) | `Topology/VectorBundle/Riemannian.lean` (`structure RiemannianMetric`, `class RiemannianBundle`): positive-definite inner products only. `QuadraticForm` signature is linear algebra, not a metric on a bundle |
| the volume form and Hodge star | `HodgeStar` (1), `volumeForm` (3) | `LinearAlgebra/ExteriorPower/HodgeStar.lean`: `exteriorPower.hodgeStar` for ***any bijective bilinear form*** over a commutative ring, so Lorentzian signature is covered algebraically. `Analysis/InnerProductSpace/Orientation.lean`: `volumeForm`, inner-product spaces only. ***So the volume form is present, not missing*** |
| Pontryagin density, Chern–Simons form, transgression | `Pontryagin` (2, both Pontryagin DUALITY), `Chern.?Simons` (0), `transgression` (0), `Chern.?Weil` (0) | `Analysis/Calculus/DifferentialForm/{Basic,VectorField}.lean`: `extDeriv` and `d∘d = 0` on normed spaces. There is no wedge product of End-valued forms and no trace on them |
| Laplacian on a manifold and its spectrum | `Laplace.?Beltrami` (0), `spherical harmonic\|SphericalHarmonic\|zonal` (0), `heat kernel` (0); `Laplacian` (13 files, all flat: `InnerProductSpace/Laplacian.lean` on `E → F`, graph `LapMatrix`, Schwartz and Sobolev) | `Analysis/InnerProductSpace/Laplacian.lean` and `Harmonic/`: the Laplacian of functions on a flat inner-product space. ***No operator on a curved manifold, so no spectrum of one*** |
| representation-theoretic level sums | `Schur` (18, of which `CategoryTheory/Preadditive/Schur.lean` and `RepresentationTheory/FDRep.lean` ***are*** Schur's lemma), `invariant theory\|FirstFundamental` (0) | Schur's lemma is present. ***Absent:*** the SO(4) action on harmonics of `S³` and the first fundamental theorem of SO(3) invariant theory |
| oscillator / perturbation theory | `harmonic oscillator` (0), `Fock\|ladder operator\|creation operator` (0), `Rayleigh` (3: `rayleighQuotient`, variational only), `Hermite` (polynomials only) | no Rayleigh–Schrödinger or Kato theory |

## ⓐ What each row is missing, as one declaration

- ***Row 89.*** The Riemann tensor of the Levi-Civita connection of an indefinite metric. Its density
  `*RR = ½ ε R R / √−g` needs only that tensor and `ε`. Mathlib's `leviCivitaConnection` requires
  `[RiemannianBundle]` and defines no curvature.
- ***Row 96.*** The same tensor, plus the Chern–Simons current `K^μ = 2ε^{μνρσ}(Γ∂Γ + ⅔ΓΓΓ)` and the transgression
  identity `∂_μK^μ = −√−g *RR`. This is coordinate form of `d CS(Γ) = tr(R ∧ R)`.
- ***Row 70.*** As labelled, a spectral theory. ***As built, none was needed.*** The receipt's checks are a
  formal second-order formula on finite ladder truncations, curvature on the same indefinite connection, and the
  TT spectrum entering as cited data in one section (E).
- ***Row 60.*** The spectrum of the Lichnerowicz Laplacian on transverse-traceless tensor harmonics of `S³`:
  the levels `λ = m² − 3`, `deg = 2(m² − 4)`, the value of `c_C`, and the fact that level sums of products of
  harmonics are SO(3)-invariant tensors (SO(4) acting on the harmonics, then Schur). Not one piece of this chain
  exists in Mathlib; Schur's lemma, its last step, does.

## ⓑ One gap or four? ***Two structures, and the label conflated two different questions***

- ***Structure I, curvature of an indefinite Levi-Civita connection*** (rows `89`, `96`; also used by `69` and
  `70`, both `DONE`). Mathlib stops one step short: it has the connection, for definite metrics only, and the
  algebraic Hodge star for any signature. ***The project's own `ShadowEngine` has supplied this all along***:
  - `NDMetric` / `ndOf`, a nondegenerate metric of any signature;
  - `lcConn`, its Levi-Civita connection;
  - `curv` and the coordinate formulas `curvD_eq` and `curv_T`.

  Rows 69, 70 and 96 were built on it. In the Mathlib sense structure I is a gap; it was never a gap in this
  project's library. The step the engine lacks is the general ***transgression identity***, which rows `89`
  (Part 8) and `96` (Part 3) both measure as a ratio `−1` on one member.
- ***Structure II, spectral data of TT harmonics on `S³`*** (row `60`; imported in rows `63`, `68`, `70`, `73`,
  all `DONE` with it imported). Mathlib has no Laplacian on a curved manifold. Every row of the corpus that uses
  these spectra imports them, and the rows were declared `DONE` on that basis. Row 60 is the one whose label points
  at structure II. ***Its computed checks A–E, as `PRICING.md` lists them, take the spectrum, `c_C` and the level-sum
  ansatz as imports, exactly as rows 70 and 73 do.***
- ***So the finding:*** `LIBRARY GAP` was answering "does Mathlib have the structure the row's mathematics lives
  in?" The census needs a different question answered: "can the row's computed checks be built?" For all four rows
  the answer to the second question is yes:
  - rows 70 and 96 are now built;
  - row 89 needs only the engine and the Pontryagin core (`Row69Pontryagin.lean`);
  - row 60 needs the engine and imported spectral data.

  What remains beyond reach is the same in every case: ***derivations of imported data***, never computations.

## ⓒ What is reachable by building locally, priced

| piece | serves | price | registered |
|---|---|---|---|
| general transgression identity `∂_μK^μ = −√−g *RR` for the engine's indefinite Levi-Civita connection in four dimensions: a polynomial identity in `(Γ, ∂Γ, ∂²Γ)` using Schwarz symmetry, trace cyclicity and the antisymmetry of `ε` | rows 89 and 96, where the measured ratio `−1` becomes a corollary | M | ***yes: campaign 43, `r7443_71_campaign43/PREDICTION.md`*** |
| row 89 in full (Kerr closed form, U(3) charges, Clifford relation, the static and Gowdy families) | row 89 | XL (1500–2500 per `PRICING.md`) | next, after 43 |
| row 60's checks A–E with the spectrum imported | row 60 | XL (900–2500 per `PRICING.md`) | after 89 |
| TT harmonics on `S³`, the SO(4) action and level sums, derived | the imports of rows 60, 63, 68, 70 and 73 | research-scale: a Laplace–Beltrami operator on a Riemannian manifold, its spectrum on `S³`, and the representation theory. ***Not priced; not proposed*** | no |
| Mathlib's `leviCivitaConnection` generalised to indefinite metrics, with curvature | contribution, not needed by any row | several hundred lines or more; ***not proposed*** | no |

***Contribution rather than blocker:*** the transgression identity in coordinates, and curvature on the engine's
indefinite connection, are self-contained pieces Mathlib lacks entirely. They are the candidate contribution if
one is wanted. No row waits on them reaching Mathlib.

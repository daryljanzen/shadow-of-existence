# `r7259+71.3` — PRE-REGISTRATION: what `mathlib` and `PhysLean` carry, what stating one geometric receipt would cost, and how big the algebraic slice is

*Committed and pushed before `mathlib`, `PhysLean` or any of the `267` symbolic receipts is opened for this
order. The order is `FOR_71.md` §`r7259` ③. Everything below is a prior; the measurement replaces it and is
reported against it, band by band, including where it misses.*

## Ⓐ The population: reproducing the `267`

The four-way classification of the `1,043` receipts exists only in `r7259`'s commit message; there is no
receipt or table for it in the tree. So the first step is to reproduce it by a rule fixed here, before running:

- **numerical / data** — the receipt imports any of `numpy`, `scipy`, `camb`, `classy`, `healpy`, `astropy`;
- **symbolic** — not numerical, and imports `sympy` or `mpmath`;
- **measurement over the corpus** — neither, and it opens corpus `.tex`/`.md` files or the git history;
- **plain arithmetic / structural** — everything else.

*A receipt is a `.py` file under `receipts/`, helpers and `__init__` excluded.*

| quantity | central | band |
|---|---|---|
| receipts found | **1,043** | 1,000–1,090 |
| symbolic under this rule | **267** | 230–300 |

⛔ *If the symbolic count lands outside 230–300, my rule is not the gate's. I then report both and work on my own
population with the difference stated, and do not adjust the rule until it matches.*

## Ⓑ The slice: what the symbolic receipts are about

Each symbolic receipt is read: its stem, its docstring, and the objects it builds. It goes in exactly one bin,
the first that fits:

| bin | what puts a receipt there | central | band |
|---|---|---|---|
| **A · finite / Galois** | permutation groups, finite groups, Galois groups, field extensions, root systems as finite objects, counting | **8%** | 3–15% |
| **B · exact algebra** | polynomial or rational-function identities, factorisations, exact linear algebra, explicit matrix or Lie-bracket identities, exact rational arithmetic | **30%** | 18–45% |
| **C · analysis** | series, limits, integrals, special functions, ODE solutions, asymptotics, numerical evaluation at high precision | **35%** | 22–50% |
| **D · differential geometry** | a metric, connection, curvature, Killing or conformal-Killing field, or geodesic treated as an object on a manifold | **27%** | 15–40% |
| **algebraic slice = A + B** | | **38%** | 22–55% |

*My prior differs from the order's on one point, and I state it so the measurement can settle it: the order
expects most of the `267` to be differential-geometric. **I expect D to be about a quarter**, because I expect
most geometric receipts to compute in explicit coordinates and so to land in B or C. If D comes out above 50 per
cent, the order's reading was right and mine wrong; if below, the reverse.*

⌗ *And a sub-prediction that matters more than the bins: among the D receipts, **I expect about 60 per cent
(band 35–80) to have a computational core that is a coordinate identity**, a rational-function or polynomial
statement that `mathlib` can state today, while the geometric theorem it stands for cannot be stated. If that
holds, it is the main result: a formal statement of such a receipt checks the identity and not the geometry, and
the gap between the two is exactly the "satisfied by construction" class the order is aimed at.*

## Ⓒ The libraries: what I expect to find

*Method, fixed now: shallow clones of `leanprover-community/mathlib4` and the `PhysLean` repository, with each
`HEAD` SHA recorded. Search the Lean sources for declarations (`def`, `structure`, `class`, `theorem`,
`lemma`, `abbrev`, `instance`) against the patterns below, then **read** every hit before calling it present.
An empty search is reported as "looked, none", with the patterns used, and is not read as more than that.*

*Patterns:* `PseudoRiemannian`, `Riemannian`, `Lorentz`, `Minkowski`, `LeviCivita`, `Christoffel`,
`covariantDerivative`, `Connection`, `Curvature`, `Ricci`, `riemannTensor`, `Killing`, `conformal`, `Einstein`,
`deSitter`, `lieDerivative`, `mlieBracket`, `Geodesic`, `IsGalois`, `Polynomial.Gal`, `alternatingGroup`,
`specialUnitaryGroup`, `LieAlgebra.Orthogonal`, `QuadraticForm`, `discriminant`.

| object | in `mathlib` | in `PhysLean` |
|---|---|---|
| Riemannian metric on a manifold, as a declared structure | **present** (0.6) | — |
| pseudo-Riemannian or Lorentzian metric on a manifold | **absent** (0.7) | **absent** (0.6) |
| Minkowski metric / Lorentz group on ℝ^{1,3} | absent (0.7) | **present** (0.95) |
| Levi-Civita connection, Christoffel symbols | **absent** (0.75) | absent (0.8) |
| Riemann / Ricci curvature of a metric on a manifold | **absent** (0.8) | absent (0.8) |
| Killing or conformal-Killing vector field | **absent** (0.9) | absent (0.9) |
| Lie bracket of vector fields on a manifold | **present** (0.7) | — |
| Lie derivative of a tensor field | absent (0.75) | absent (0.8) |
| geodesics of a general metric | absent (0.75) | absent (0.8) |
| Einstein field equations | **absent** (0.95) | absent (0.8) |
| de Sitter space | **absent** (0.95) | absent (0.95) |
| Galois group of a polynomial, `IsGalois`, irreducibility | **present** (0.98) | — |
| permutation and alternating groups, finite group theory | **present** (0.99) | — |
| `SU(n)`, unitary and orthogonal groups as matrix groups | **present** (0.85) | present (0.6) |
| quadratic forms, isotropic vectors | **present** (0.95) | — |

## Ⓓ The cost of STATING one geometric receipt

*Target, fixed now as the first geometric receipt the order names:*
`I20_the_redshift_is_a_conformal_killing_charge_on_the_null_cone`.

*What I expect has to be built before its theorem can even be written down, in foundation layers rather than
effort:*

1. a pseudo-Riemannian metric of signature (1, n) as a smooth symmetric (0,2)-tensor field;
2. the Lie derivative of that tensor along a vector field;
3. the conformal-Killing equation, `𝓛_K g = φ g`;
4. null vectors and null geodesics of that metric;
5. de Sitter space as the hyperboloid in ℝ^{1,5} with its induced metric;
6. the conserved quantity `g(K, γ̇)` along a null geodesic.

| quantity | central | band |
|---|---|---|
| missing layers from this list after the search | **5** | 3–6 |

⌗ *Recorded alongside: whether the receipt's own sympy core is a coordinate identity that `mathlib` can state
today (Ⓑ's sub-prediction, for one receipt): **yes, 0.7.***

## Ⓔ The open derivation the order points at

`L221_the_bridge`: *"no derivation producing {0,1,2} from a single condition has been exhibited."* I have not
read it. The prior: **the statement is expressible with `mathlib`'s finite groups and complex representations
as they stand (0.6)**. This is a statability check only, not an attempt at the derivation.

## Ⓕ The toolchain

*Whether `elan`, a Lean toolchain and `mathlib`'s build cache can be installed in this container through its
network policy: **yes, 0.6.** If not, Ⓒ is measured by reading source and no Lean file is compiled this order;
that is stated in the result, not worked around.*

## ⛔ What would make the order itself wrong

- **If the algebraic slice (A + B) is below 15 per cent of the symbolic population**, there is too little
  deductive algebra to justify a Lean project on this corpus. I report it as a stop, not a scope.
- **If the Lorentzian layer is present** (both of Ⓒ's pseudo-Riemannian rows come back present, with
  curvature), the order's expected negative is false and the geometric three-quarters is in reach. I report it
  as a reversal, not a footnote.

*Every receipt cited in the result is run to completion here and quoted by its own verdict line. This
container does not have `sympy` installed; installing it is part of the run, and a receipt that cannot be run is
reported as not run.*

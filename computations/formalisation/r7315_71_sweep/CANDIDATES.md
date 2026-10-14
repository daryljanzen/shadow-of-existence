# `r7315+71.2` — CANDIDATES: `37` of the `91` statable-not-yet-discharged readings pass `r7297`'s rule. That is inside the pre-registered band (12–45) and above the central `25`. Each candidate has a predicted marginal cost, fixed here before any `mathlib` file is read or any Lean is written. ⌗ I predict the stop rule fires at candidate 10, the first that needs a chart I have not built

*Read from `r7285_71_restate/READINGS.tsv` (111 rows, `index · path · class · stand-in`) against the rule in
`PREDICTION.md`. The verdict on each row is a reading of its stand-in, given with its reason. ***This is the step
where I used judgement, and every call is listed so that another seat can redo it.***

## The arithmetic

| | count |
|---|---|
| readings | 111 |
| unstatable: spectral 9 (23, 24, 57, 60, 63, 64, 68, 70, 73), spin 3 (82, 84, 85), volume form 1 (46), `G/H` 1 (80) | −14 |
| **statable** | **97** |
| already discharged in full (29, 41, 42, 43, 77, 92) | −6 |
| **statable, not yet discharged** | **91** |
| ***candidates*** | ***37*** |
| not candidates: no connection hypothesis | 35 |
| not candidates: no everywhere-nondegenerate chart on a model space (13 with an `S²`/`S^{D−2}` factor, 3 on `S³`/`S⁵`) | 16 |
| not candidates: need the Levi-Civita volume form (THEORY since `r7267`) | 3 |

***Count: `37` against a predicted `25` (12–45). In band, and high.*** *The surplus is G3: I counted `12` extrinsic- and
slice-curvature readings as connection-carrying, because their stand-ins are built on S2's second fundamental form,
which takes `cov`.*

## ⌗ A finding before any cost: the class I predicted the stop on is excluded by the rule itself

***`13` statable readings fail the candidate rule's chart clause.***
- Rows 13, 17, 28, 35, 45, 48, 49, 51, 54, 81, 93, 104 and 110 all name a metric with an `S²` or `S^{D−2}` factor:
  SdS, Kantowski–Sachs, Nariai, LTB, TOV, Tangherlini.
- Their angular chart degenerates at the poles, so no single model-space chart carries them as an `NDMetric`.

*I predicted that the sweep's natural stop would be a CLASS of metric with no regular chart. **It is, and it can be
seen before the sweep starts:***
- *the connection layer the sweep can reach is these 37;*
- *the 13 are where a port change (`NDMetric` on an open set, or a product with `S²` as a manifold) would be needed.*

That is a proposal for after B, not part of B.

## The 37, cheapest first, with predicted marginal cost

| # | row | stand-in | metric, chart | predicted `cᵢ` |
|---|---|---|---|---|
| 1 | 99 | surface gravities at the two roots | PG, 2D (C3's) | **50** |
| 2 | 109 | de Sitter surface gravity (entropy a definition) | dS in PG form, 2D | **60** |
| 3 | 11 | surface gravity and the Unruh temperature | Rindler/dS, PG 2D | **70** |
| 4 | 34 | a slice's Gaussian curvature `= −f′/(2r)` | 2D slice metric | **140** |
| 5 | 36 | its zero locus and the Nariai discriminant | over row 34 | **60** |
| 6 | 103 | Gaussian curvature of the slicing surface | 2D | **120** |
| 7 | 32 | geodesic acceleration `= r K_G` | 2D | **150** |
| 8 | 38 | the same, at the Hubble–Eddington radius | over row 32 | **60** |
| 9 | 56 | Killing algebra of the plane wave, covariantly | Brinkmann, `ℝ⁴` | **180** |
| 10 | 44 | photon-sphere Lyapunov exponent of the geodesic flow | SdS equatorial, a NEW chart `(τ, s, φ)` on `ℝ³`, `r = eˢ` | **250** |
| 11 | 78 | Brinkmann wave Ricci-flat | `ℝ⁴` | 220 |
| 12 | 55 | pp-wave Riemann, vacuum iff harmonic, type N | `ℝ⁴` | 300 |
| 13 | 8 | TT mode function on de Sitter | flat slicing, `ℝ⁴` | 250 |
| 14 | 76 | Mukhanov mode equation on dS | `ℝ⁴` | 250 |
| 15 | 22 | dS curvature invariants | `ℝ⁴` | 300 |
| 16 | 0 | max-symmetric curvature invariants, `R` of a slicing | `ℝ⁴` | 300 |
| 17 | 4 | invariants; Ricci scalar of a layer | `ℝ⁴` | 300 |
| 18 | 5 | Ricci scalar of two slicings | `ℝ⁴` | 300 |
| 19 | 2 | `Weyl² = 0` on FRW | flat FRW, `ℝ⁴` | 350 |
| 20 | 3 | rank of the invariant basis, `Weyl² = 0` | `ℝ⁴` | 350 |
| 21 | 72 | ranks of FRW invariants | `ℝ⁴` | 350 |
| 22 | 1 | `Weyl²` as a polynomial in shear | Bianchi I, `ℝ⁴` | 400 |
| 23 | 74 | Gowdy-dS background, `3H² = Λ`, shear charge | `ℝ⁴` (C5's `diag4`) | 350 |
| 24 | 75 | Einstein tensor of Gowdy-dS = wave + constraint | `ℝ⁴` | 450 |
| 25 | 98 | Einstein condition and the optical tidal matrix | dS, `ℝ⁴` | 300 |
| 26 | 79 | leaves' `K_ab = 0`, leaf scalar curvature | `ℝ⁴` slicing | 250 |
| 27 | 47 | shear of a foliation from `K` | `ℝ⁴` | 250 |
| 28 | 102 | extrinsic-curvature shear, closed form | `ℝ⁴` | 300 |
| 29 | 94 | umbilic locus of a foliation | `ℝ⁴` | 300 |
| 30 | 7 | ADM identity for `K_ij` | generic, model space | 300 |
| 31 | 52 | open slicing as a hyperboloid embedding, 3-curvature *(closed case excluded: `S³`)* | `ℝ⁴` | 300 |
| 32 | 108 | hyperplane sections of constant curvature | `ℝ⁵` | 350 |
| 33 | 58 | ADM kinetic term and Legendre transform | generic | 350 |
| 34 | 20 | momentum constraint, mode ODE, `div G` | generic | 400 |
| 35 | 6 | contracted Bianchi identity, `div G = 0` | generic | 450 |
| 36 | 19 | `Weyl²`; Gauss–Bonnet a total derivative | generic 4D | 500 |
| 37 | 71 | `C² = E₄ + 2(Ric² − R²/3)` | generic 4D | 450 |

***Predicted: candidates 1–9 land under `200` each (Σ ≈ 890). Candidate 10, row 44 at a predicted `250`, is the
first over the line, so the stop fires there with `k = 9`.***
- *The cumulative rate would then be `(857 + 890)/15 ≈ 116`, under the `150` line.*
- ***On my own numbers, the connection layer is cheap for 2D metrics, and the stop falls where a 4D curvature or a
  new chart is first needed.*** *That gives the answer to the order's question a second form. **Rows 11–37 are mostly
  4D curvature computations at 220–500 lines each, which is about 8,500 lines: work for more hands, or for a 4D
  curvature engine built once (a proposal, not B).***

## Not candidates — by reason, with the rows

- **No connection hypothesis (38):**
  - G0: rows 14, 15, 16, 31, 33, 39, 86, 87, 88, 90, 101, 105;
  - G1: rows 12, 25, 27, 30 (metric coefficients, Killing norm, causal character) and 91 (a first integral);
  - G3: rows 9, 10 (identifications with a radius), 50 (induced metric only), 61 (degenerate induced metric), 107 (a
    foliation family);
  - G4: rows 53 (a parameter count), 65, 66, 67 (on `S³`, also chart-excluded), 95 (Killing vectors by Lie
    derivative);
  - G5: rows 18, 21, 26, 37, 40, 97, 100, 106.
  - *Rows 65, 66, 67 are on `S³`. They are listed here, once, because neither clause holds for them.*
- **No regular model-space chart (13):** rows 13, 17, 28, 35, 45, 48, 49, 51, 54, 81, 93, 104, 110.
- **Need the volume form (3):** rows 69, 89, 96 (Pontryagin densities, which need `ε`).
- **Also excluded, chart-only:** rows 59 and 62 (`S³` frame jets) and row 83 (squashed `S⁵`).
- *Sum: 38 + 13 + 3 = 54, and with 59, 62, 83 counted in the 38's G2 complement:*

  ***rows 59, 62 and 83 are connection-carrying but have no regular chart. They belong with the 13, which makes it 16
  and the no-connection list 35. Corrected here before any cost is measured: 35 + 16 + 3 = 54.***

## Fixed by this file, before any Lean

- the order above;
- the predicted `cᵢ` per candidate;
- the stop rule: `cᵢ > 200`, or not landing within `2×` its prediction.

***A candidate predicted above 200 cannot pass the rule. If it is reached, the run stops there.*** *So candidates
10–37 are predicted unreachable under the registered rule, and the sweep's own result will say whether that
prediction holds at candidate 10.*

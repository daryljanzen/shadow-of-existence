# `r7411+71.2` — RESULT: `r7383` ① and ②. ⌗ ① the 4 "obstructions" are not obstructions: no receipt computes anything global except iterated integrals of explicit trig polynomials over the Euler box. The one genuinely spectral object, the TT spectrum of `S³`, is IMPORTED by all four as given formulas and derived by none. REAL OBSTRUCTION `4` → `0`. ⌗ ② the 32: ORDER `17`, LIMIT `10`, ROW `5`; the largest single group is `6` (points on an ambient quadric), so no lemma is a campaign. ⌗ The registered ① band (0–2 of 4 not obstructions) is REFUTED at `4`

*Scored against `PREDICTION.md` in this directory (pushed at `r7411+71.1`, before any receipt was opened for this item).
It is not revised. The lists are derived by `derive_lists.py` from `ROWS.tsv` and `READINGS.tsv` at HEAD
(`LISTS.txt`, committed before the reading). Each of the 36 receipts was read in full: the 32 by three readers, the 4
by a fourth, with every load-bearing claim spot-checked against the file. Rows 67, 88 and 105 were re-read by me.
Nothing was built.*

***The standard, stated once:*** each row is classified by what its receipt COMPUTES AND ASSERTS, the same standard
campaigns 16–19 were built and scored on. A headline the receipt only prints or states in prose is not the receipt's
object, and the row's text says so where it matters.

## ① The four "obstructions", written up as results

| row | to be formalised (the census stand-in) | what the receipt computes | what is obstructed | what would remove it |
|---|---|---|---|---|
| 59 | algebraic quartic of a curvature expansion | (A) the quartic residual on 3 × 3 matrices, **built**: `quartic_identity`, `quartic_traceless`; (B) trace identities of explicit Euler-angle matrix fields, pointwise; (C) the curvature series of `exp(εH)` on the `S³` frame to `ε⁴` and its integrals; (D) jet ranks `5`, `12`, `8` (finite linear algebra over ℚ); (E) integrals of the series for a non-constant `H` | ***nothing the receipt computes.*** The integrals are of explicit trig polynomials over a box. The "tower" labels (`m = 5`, `λ = 22`) are inputs | a non-diagonal `Fin 3` instance (the `r7351` `EngineG` at `n = 3`) and `intervalIntegral` over the Euler box. Both are in reach |
| 65 | curvature shifts a TT mode frequency | an ODE/Lagrangian reduction with the Milnor formula (frame algebra); a flat-`ℝ³` plane-wave period average; `R_ikjl h^kl = −K h_ij` (ℝ³ algebra); asymptotic series in `m`; `ζ(0) = 10` from `ζ_R(0)`, `ζ_R(−2)`; a floating cutoff slope | ***nothing global.*** The spectrum `(m² − 1, 2(m² − 4))` is fed in as formulas | nothing new: Mathlib has the zeta values. The floating slope is a stated limit and would not be a theorem |
| 66 | cubic kinetic vertex on `S³` | frame algebra (structure equations, `−∇² = 6` by structure constants, Milnor, `tr h³ = 3 det h`); the volume `2π²` by an iterated integral; ODE analysis on `[1, ∞)` | ***nothing on `S³` beyond the volume.*** The deficiency-index conclusion is prose | a non-diagonal `Fin 3` instance; one iterated integral; improper integrals on `[1, ∞)` (in Mathlib) |
| 67 | TT harmonics on `S³`, eigenvalue `6` (spectral) | everything pointwise in the Euler chart or the frame (structure equations, transversality via Christoffels, `−∇² = 6`, `det(e⁻¹He) = det H`), plus the volume `2π²` | ***nothing.*** The degeneracy `10 = 2(3² − 4)` is arithmetic on an imported formula, and "5 left- plus 5 right-invariant" is asserted | a non-diagonal `Fin 3` instance and one iterated integral |

- ***The finding, which is the one `r7383` ① asked to be told:*** none of the four is an obstruction wearing a library
  gap's clothes. **All four are reachable rows wearing an obstruction's clothes.**
  - What made them look global is the object they are ABOUT: the TT spectrum of `S³`.
  - That object is computed by none of them. Each imports it as closed-form formulas, and checks only polynomial
    identities between those formulas.
- ***What IS obstructed is one premise, not four rows.*** It is that `m² − 3` and `2(m² − 4)` are the TT eigenvalues
  and degeneracies of `S³`. That needs Peter–Weyl or Laplacian spectral theory on `S³`. It is the ***spectral theory***
  library gap already on the census nine times. It does not need a tenth row. It is the same gap.
- ***Census move:*** `59`, `65`, `66`, `67`: `REAL OBSTRUCTION` → `ORDER: ENGINE-REACHABLE`. Each row's text names
  what it waits on and that the spectrum is imported. **REAL OBSTRUCTION `4` → `0`**, and the real end is `17` library
  gaps, all backlog.

## ② The 32, priced on the `r7013` split

*Per row in `CLASSIFICATION.tsv`: the split, the group, what the receipt computes and asserts, and what carries it or
what it waits on.*

| split | rows | count |
|---|---|---|
| ***ORDER***, a remainder whose discharge is known | 14, 15, 16, 25, 27, 30, 31, 33, 37, 39, 50, 61, 87, 88, 90, 95, 107 | ***17*** |
| ***LIMIT***, the same question at finer resolution, carried by a DONE row: NOT rowed | 9, 10, 12, 21, 91, 97, 100, 101, 105, 106 | ***10*** |
| ***ROW***, a different KIND of object, which no receipt computes | 18 (a covering with its monodromy), 26 (completion of a spacetime), 40 (a deck group), 53 (an essential image / moduli of solutions), 86 (a Z₃ action on loci of the quadric) | ***5*** |

***The grouping, which `r7383` ② says is the whole value:***

| group (what the ORDERs wait on) | rows | count |
|---|---|---|
| G2 points on an ambient quadric (`ring`, `nlinarith`, `exp` identities) | 39, 50, 87, 88, 90, 107 | ***6*** |
| G1 trig and hyperbolic identities, real and complex, on the cycloid and its continuations | 14, 27, 30, 31, 37 | 5 |
| G3 metric-coefficient algebra (`ring`, `field_simp`, `Matrix.det`) | 25, 33, 61 | 3 |
| G4 signs and a log-derivative (mostly text pins around them) | 15, 16 | 2 |
| G5 the engine: **misfiled**, its content is connection content (`killF_model` for the `so(3)` fields, `boxD` for the separation) | 95 | 1 |

- ***The LIMITs are carried by four DONE theorems:***
  - `row104_nariai_root`: 12, 21, 100, 101, 105;
  - `section_quadric`, which is general in the vector space: 9, 10;
  - `sinh23_flow`: 91, 97, 101;
  - `nariai_curvature`, `sds_kretschmann`, `dS5_constant_curvature`: 21, 97, 100, 106.

  ***The Nariai double root alone is re-checked by five receipts*** (12, 21, 100, 101, 105), and by row 26's part 3.
- ***The ROWs are headline claims stated in prose and never computed.*** In each case the receipt asserts a
  placeholder: `degree == 3`, a hard-coded truth table, one root of unity, symbol counts, or nothing. ***Each is a
  different kind of object, and none is a formalisation backlog item until a receipt computes it.*** The trivial
  residue each one does compute is ORDER-able, and is noted in its line.
- ***The refutation clause (`r7383` ②, registered):*** no group of ORDERs reaches `8` rows on one route. ⇒ ***"A map,
  not a campaign" stands***, and no single lemma is worth registering.
  - ***What the map does show instead:*** `16` of the `17` ORDERs wait on NOTHING, only Mathlib as it is (`ring`,
    `field_simp`, trig/hyperbolic lemmas, `Tendsto`, `Matrix.det`). They are unbuilt because no order has asked for
    them, not because anything blocks them.
  - ***The price, if it is wanted:*** one sweep campaign over G1–G4, ≈ `25` lines a row, ≈ `400` lines for the `16`,
    band 250–700. It is offered, not taken.

## The registration, scored

| quantity | registered | measured | |
|---|---|---|---|
| ORDER | `18` (12–24) | ***`17`*** | inside |
| ROW | `8` (4–13) | ***`5`*** | inside |
| LIMIT | `6` (2–11) | ***`10`*** | inside |
| groups among the ORDERs | `5` (3–8) | ***`5`*** | inside, on the point |
| rows in the largest group | `9` (6–14) | ***`6`*** | inside, at the floor |
| the largest group is (a), the quadric group | failable | ***(a)*** | survives |
| obstructions that are not obstructions | `1` (0–2) | ***`4`*** | ***REFUTED*** |

- ***Five of five ② bands held, and that is the weaker half.*** The classification is mine, made after the
  registration, so a band I set could be met by how I drew a boundary. The rows nearest a boundary are:
  - 14 (ORDER, not a LIMIT of row 29's cycloid: it identifies the FRW scale factor, which row 29 does not);
  - 26 (ROW by its stand-in; its computed content is a LIMIT of rows 11, 99, 109);
  - 95 (ORDER, filed under no-connection in error).

  Row 95 has no other way to go: it is reachable either way, on the engine. Moving 14 and 26 the other way gives
  ORDER `16`, LIMIT `12`, ROW `4`. That leaves ROW at its floor and puts LIMIT over its ceiling of `11`. ***The
  LIMIT band is the fragile one, and it holds only on my reading of those two rows.***
- ***The ① band was refuted, and it is the more informative result.*** I registered `67` as the one likely to fall,
  because it is explicit harmonics checked pointwise. All four fell, for one reason: the spectrum is an input to every
  one of them. Since `r7325` the census filed them by their subject (`S³` spectra) rather than by their computations,
  and that is the error this order exists to find.

## Census (moved in this push)

| status | before | after |
|---|---|---|
| DONE | 56 | 56 |
| GENERIC-METRIC IDENTITY | 2 | 2 |
| LIBRARY GAP (backlog) | 17 | 17 |
| REAL OBSTRUCTION | 4 | ***0*** |
| NO-CONNECTION, NOT DONE | 32 | ***0***, split as below |
| ORDER: NO-CONNECTION, REACHABLE | — | 16 |
| ORDER: ENGINE-REACHABLE | — | 5 (59, 65, 66, 67, 95) |
| LIMIT OF A DONE ROW | — | 10 |
| ROW: A DIFFERENT KIND | — | 5 |
| **total** | **111** | **111** |

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. Nothing was built.*

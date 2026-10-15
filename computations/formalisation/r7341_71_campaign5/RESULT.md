# `r7341+71.6` — RESULT: the port lands at `153` lines against `250` (band 150–400), with every existing axiom line unchanged. The coordinate recipes followed it, generalised in place. ⌗ Rows 108 and 35 are BUILT IN PART, at `106` and `178`. Row 83 is REPORTED: its obstruction is not the dimension, it is a non-diagonal metric. ⌗ Survival: `2` of my `3` readings survived, against an expected `1.9`; the running rate is `11` of `15`. ⌗ Compile time: a `625`-case `Fin 5` table took `453 s`, `2.4×` the `256`-case `187 s`, against a registered `2.5×`

*Scored against `PREDICTION.md` in this directory (pushed at `r7341+71.2`, before any receipt was opened). It is not
revised. Every new axiom line is `[propext, Classical.choice, Quot.sound]`, with no `sorryAx` (`PROBE_RUN_PORT.txt`,
`PROBE_RUN_RECIPES.txt`, `PROBE_RUN_ROWS.txt`).*

## ⛔ The stops, scored first

| condition | measured |
|---|---|
| the port over `500` | ***no*** — `153` |
| any existing axiom line changes, or any existing theorem stops building | ***no*** — `125` engine lines unchanged, and all seven downstream files clean, twice |
| one instance over `200`, or two in a row over `170` | ***no*** — the largest is `178` |

## The pieces

| piece | predicted | measured | band | outcome |
|---|---|---|---|---|
| ***the port*** (`EngineN`: `diagN`, `gamDN`, `lcGam_diagN`, `curvDN_eq`, the `n`-dimensional contractions with `weyl2CN`) | `250` | ***`153`*** | 150–400, in at the floor | ***landed*** |
| the recipes over `Fin n` (`fd_coord_i`, `d2_of`, `d2_indep`, `co_d*`, `pr_d*`, `tw*`), IN PLACE | — (in the port's model) | ***`42`*** lines changed | — | ***landed***; no statement changes at `n = 4` |
| row 108 | `120` | ***`106`*** | 60–170, in | ***built in part*** |
| row 83 | `150` | ***`0`*** | — | ***reported*** |
| row 35 | `200` | ***`178`*** | 60–170, over (as registered) | ***built at `D = 5`*** |
| ***campaign 5*** | ***`720`*** | ***`479`*** | | |

***Why the port came in under.***
- The general LC machinery (`ndOf`, `koszK`, `lcGam`, `curv_model`) was already written for any finite-dimensional
  `E`, so the port is only the diagonal layer.
- Its one `Fin 4`-specific step was the Koszul identity in `lcGam_diag4`, closed there with `Fin.sum_univ_four`.
  Here it goes by linearity and one `Finset.sum_comm`.
- I priced a port of an engine. The engine was already mostly dimension-free, and the port was its diagonal shell.

## What each row proves, and the caveats beside the score

- ***Row 108*** (`probes/HigherDim.lean`):
  - `section_quadric`: a hyperplane section of `η(X, X) = α²` is the quadric `η(Y, Y) = α² − c²`.
  - `dS5_constant_curvature`: `dS₅`, in the flat slicing on `ℝ⁵`, has `R(eᵢ,eⱼ)eₖ = H²(g_jk eᵢ − g_ik eⱼ)` under THE
    connection. That is maximal symmetry, and the first `Fin 5` instance.
  - `sds_K_radial`: SdS's `K` has `∂_r K = −288M²/r⁷`, non-zero iff `M ≠ 0`.

  ***Not built:*** the receipt's (4)–(5), that no static, spherically symmetric hypersurface of `dS₅` induces SdS
  at `M ≠ 0`. That is an embedding-nonexistence argument, not a pointwise curvature claim, so the row is a half.
- ***Row 35*** (`tangherlini5_Gtt`, `tangherlini5_kernel`): at `D = 5`, THE connection's
  `G^t_t = 3(rF′ + 2F − 2)/(2r²)` for ANY `F`. That is `(D−2)/(2r²)[rF′ + (D−3)(F − 1)]` at five.
  - `F = 1 − 2M/r² − Λr²/6` solves `G^t_t + Λ = 0`.
  - The proof needs a triple-product recipe (`tr_d1`, `tr_d2`) for `r² sin²a sin²b`, and the identity
    `sin² + cos² = 1` on the first angle.
  - ***Not built:*** every other `D`. The receipt checks `4` to `8`. All `D` at once needs a table indexed by
    coordinate class, which I registered at p `0.4`, and it did not land, so the row is a half.
- ***Row 83, reported:***
  - The squashed `S⁵` is the `SU(3)`-invariant canonical variation of the Hopf fibration, NON-diagonal in any
    coordinate chart. The engine is diagonal.
  - The receipt does not compute `R_t = 24 − 4t²` from a metric. It quotes O'Neill's formula for a Riemannian
    submersion.
  - ***Reclassified as a generic-metric identity***, waiting on campaign 6's non-diagonal engine. The dimension is no
    longer its obstruction.

***The census, moved in this push:***

| status | after `r7341` | now |
|---|---|---|
| DONE | `42` | `42` |
| DONE (chartable half) | `7` | ***`9`*** (+ 108, 35) |
| NEEDS A DIMENSION CHANGE | `3` | ***`0`*** |
| GENERIC-METRIC IDENTITY | `7` | ***`8`*** (+ 83) |
| real end | `20` | `20` |

## ② The survival rate (`r7341` ⑤)

| row | my reading before opening | p | survived? |
|---|---|---|---|
| 108 | `dS₅` as a quadric, with SdS's four-metric a hypersurface in it | `0.6` | ***no***: the receipt PROVES no such static hypersurface exists at `M ≠ 0`. The quadric and hyperplane-section half of the reading was right, but the hypersurface half was the opposite of the receipt's result |
| 83 | squashed `S⁵` as a `U(1)` bundle over `ℂP²`, NOT diagonal | `0.55` | ***yes*** |
| 35 | `D`-dimensional Tangherlini–de Sitter with `G_ab = −Λg_ab` | `0.75` | ***yes*** |

***`2` of `3`, against an expected `1.9`. Running rate: `11` of `15` (`0.73`).***
- *Row 108's failure has the registered shape: the stand-in names a construction, and the receipt's object is the
  construction's failure. It is the fourth miss of that shape in four.*

## ③ Compile time

| instance | table | live coordinates | wall |
|---|---|---|---|
| `dS5_constant_curvature` | ***`625`*** cases | 1 | ***`453 s`*** |
| row 1 (`r7339`) | `256` | 1 | `187 s` |
| `tangherlini5_Gtt` | none (the `25` Ricci-trace entries, inside one goal) | 3 | ≈ `7 s` |

- ***Registered: `2.5×` for `625` against `256` at the same entry size. Measured: `2.4×`.*** The cost per case is
  roughly constant at one live coordinate, whatever the dimension.
- Row 35 confirms the axis from the other side: three live coordinates and no table, in seconds.
- *Neither separates the live-coordinate reading from the expression-size reading, as `r7341` ⑥ asks. None is sold
  as doing so.*

## The probabilities

| quantity | p | outcome |
|---|---|---|
| the port lands under `400` | `0.6` | ***yes***, `153` |
| row 83 needs a non-diagonal engine, and is reported | `0.5` | ***yes*** |
| row 35 lands for all `D` | `0.4` | ***no***, `D = 5` only |

## Beside the score

1. ***CI on #436.*** "fast — registers, views, IDs" fails on `check_order_acknowledged` for node 70's backlog. It is
   red on main at `9029f8ae2` too. "the plain suite" is red on carried receipts (`S19`, `S20`, a P15 receipt). One
   comment on the PR.
2. ***A slip, reported:*** while scanning local gate outputs, my pattern matched a stale `check_quote_pins` output
   file from an earlier run (`05:01`). One header line printed before I saw it. The file is deleted, unread beyond
   that line. I did not run that gate this cycle.
3. *Nothing in the quote-pin stride otherwise. The `21` calibration keys are untouched.*

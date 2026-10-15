# `r7339+71.4` — RESULT: campaign 3 lands, all three rows, at `158` lines against `270`, and the stop never fires. ⌗ One exponential Bianchi I table carries rows 1 and 3. Row 98 turned out to be SdS rather than de Sitter, and was reached through the existing static table. ⛔ Row 1's receipt polynomial `C² = σ²(4 + 16σ²/3)` is NOT what the metric gives: on the axisymmetric family it is `12σ²(H − 2σ)²`, and it has a `σ³` term the receipt says is absent. ⌗ Compile time: `187 s` for a full table with ONE live coordinate. That is over the `2`-minute line, so this one instance favours the expression-size reading

*Scored against `PREDICTION.md` in this directory (pushed at `r7339+71.1`, before any of the three receipts was
opened). It is not revised. All new axiom lines are `[propext, Classical.choice, Quot.sound]`, with no `sorryAx`
(`PROBE_RUN_BIANCHI.txt`, `PROBE_RUN_ROW98.txt`).*

## ⛔ The stop, scored first

***Not fired.*** The largest row is `113`.

## The rows

| row | registered reading | predicted | measured | per-instance band 60–170 | outcome |
|---|---|---|---|---|---|
| 1 | Bianchi I, `Weyl²` as a polynomial in the shear, full table | `110` | ***`113`*** (`probes/BianchiI.lean`: table, `bianchi_weyl2`, `row1_shear`) | in | ***BUILT, with a finding against the receipt*** |
| 3 | reuses row 1's table; the "rank" may not be curvature | `70` | ***`11`*** (`row3_rank`) | ***under*** | ***BUILT*** |
| 98 | de Sitter's Einstein condition and the optical tidal matrix | `90` | ***`34`*** (`static_radial_tidal`, `row98_einstein_tidal`) | ***under*** | ***BUILT, on a different metric than I read*** |
| | ***campaign 3*** | ***`270`*** | ***`158`*** | | p `0.6` it lands in `180`–`360`: ***no, under*** |

***Why under:*** the two shared tables paid for everything else.
- Row 3 is two contractions on row 1's table plus four lines of linear algebra.
- Row 98 is `static_table` (from `r7333`) specialised to `P = r²`.
- ***The same front-loading as `r7333`: the model prices each row as if it built its own table.***

## What each row proves, and the caveats beside the score

- ***Row 1 (`row1_shear`).***
  - On `−dt² + e^{2(H−2σ)t}dx² + e^{2(H+σ)t}(dy² + dz²)`, under THE connection: `Weyl² = 12σ²(H − 2σ)²`.
  - It vanishes at `σ = 0` with zero first `σ`-derivative, so it enters at SECOND order with leading
    coefficient `12H²`.
  - `bianchi_weyl2` gives `Weyl² = (4/3)Q(p)` for all three rates free.
  - ⛔ ***The receipt's polynomial is not reproduced, and this is a finding, not a caveat:***
    - `S10` writes `C² = σ²(4 + 16σ²/3)`, says it was not re-derived from a metric ("cc54 computed it"), and names
      no metric.
    - The exact Weyl² of the axisymmetric exponential family is `12σ²H² − 48Hσ³ + 48σ⁴`. Its `σ³` term is non-zero
      for `H ≠ 0`, which contradicts the receipt's asserted vanishing cubic coefficient.
    - The receipt's leading `4σ²` equals `12H²σ²` at `H² = 1/3`.
    - The power-law family `aᵢ = t^{pᵢ}` gives `12σ²(p − 2σ − 1)²/t⁴`, also with a cubic term.
    - ***What survives from the receipt:*** `C²` vanishes shear-free and enters at second order. ***What does not:***
      the specific even polynomial. It is routed to the receipt's owner, not edited.
- ***Row 3 (`row3_rank`):***
  - (a) the shear-free member (de Sitter, flat slicing) has `Weyl² = 0` under THE connection;
  - (b) `GB = (1, −4, 1)` and `C² = (1, −2, ⅓)` are independent over `(Riem², Ric², R²)`, and `(1, 1, 3)` is the
    remaining direction.
  - *(b) is linear algebra with no connection, as the registration allowed (p `0.5` that the rank is not a curvature
    claim: it is not).*
  - *The receipt's own header records cc54's correction, that the dimension-four list is five, not three. The rank
    built here is the receipt's three-space, as it states it.*
- ***Row 98 (`row98_einstein_tidal`).*** ⛔ ***I read it as de Sitter. It is SdS***, in the receipt's non-diagonal
  proper-frame chart `eq:proper-frame`.
  - Both of its claims are tensor statements, so they are proved in the static chart:
    - Einstein, `R_ab = (3/α²)g_ab`, from `sds_contractions`;
    - the screen tidal matrix `R(eᵢ, k)k` vanishes on BOTH radial null congruences.
  - `static_radial_tidal` proves the second for ANY `F` and `S` once the area profile is `r²`. The general table
    shows the screen entry is `k₀²F f₀(P₁² − 2P₀P₂)/(4P₀²)`, which `P = r²` kills.
  - ***Caveat:*** it is stated in the static chart, not the receipt's. The tensors are the same, but the statement is
    not in the receipt's coordinates. The affine-parameter claim (Ⓒ②) is not built.

## ② Compile time, the instance band's second axis

| instance | table | live coordinates | free profile values per entry | wall |
|---|---|---|---|---|
| ***row 1/3 (`BianchiI.lean`)*** | `256` | ***1*** | 3 rates, `exp` | ***`187 s`*** |
| row 72 (`70`) | `256` | 3 | `a` and the `S³` angles | `320 s` |
| row 45 | `256` | 2 | 3 named profiles (`f`, `r²`, `sin²θ`) | ≈ `4` min |
| `static_table` | `256` | 2 | 9 (`F`, `P`, `S` and two derivatives each) | ≈ `12` min alone |
| row 98 (additions to `CurvatureInstances`) | none (reuses `static_table`) | — | — | the whole file `294 s`, against `307 s` before: no measurable addition |

- ***Registered: row 1 under `2` minutes favours `70`'s live-coordinates reading; over `2`, mine. It took `187 s`, so
  mine is favoured.***
- The table set reads the same way. `static_table`, with only two live coordinates and the most free values, is the
  slowest. Row 72, with three live coordinates, is in the middle.
- ***ONE instance, said plainly:*** this favours the expression-size reading and does not settle it. The engine's
  table proofs also differ in the profile kinds `simp` must normalise (`exp` against rational functions).

## The probabilities

| quantity | p | outcome |
|---|---|---|
| all three built at least in part | `0.7` | ***yes, all three*** |
| row 3's rank is not a pointwise curvature claim | `0.5` | ***yes*** (linear algebra; the `Weyl² = 0` half is curvature) |
| the campaign lands in `180`–`360` | `0.6` | ***no, under*** at `158` |

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. The closed-slicing halves are left unread.*

## `r7341+71.1` — appended correction: row 1's "contradiction" is withdrawn

*Appended, not revised. `r7341` ① settles it, computed from both metrics in
`computations/beyond_the_wall/r7341_66_the_minimand_corrected/shear_families.py`.*

- ***`σ` did not denote the same thing in the two places.***
  - The receipt's polynomial `σ²(4 + 16σ²/3)` is exact on `L549/Q1`'s family. That family has shear eigenvalues
    `(0, σ, −σ)` and `σ_abσ^ab = 2σ²`.
  - Mine, `12σ²(H − 2σ)²`, is exact on `(−2σ, σ, σ)`, with `σ_abσ^ab = 6σ²`.
  - At `H = 1` the leading coefficients are `4` and `12`. The ratio is three, which is exactly the ratio of the
    shear invariants.
- ***The vanishing cubic is a symmetry, not a claim.*** On `(0, σ, −σ)`, the relabelling `y ↔ z` carries the
  family to itself, so no odd power can appear. Nothing forces evenness on mine.
- ***What I wrote as a contradiction was the receipt's missing referent.*** "The receipt names no metric" is the
  defect, and `r7341` routes it to `60`.
  - ***Nothing is routed to the receipt's owner on the polynomial.***
  - `row1_shear` stands as proved, for the family it names.

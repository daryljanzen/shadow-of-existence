# `r7427+71.2` — RESULT: campaign 26 BUILT. ⌗ Row 18's computable residue is proved, ported from `P7`'s `order3_bridge`: the discriminant as squared root differences, the family's discriminant and its Nariai branch points, square in `M` ⟺ `p = 0` ⟺ equilateral roots, and simple branching. ⌗ `97` lines against `100` (band 50–220). ⌗ Row 18 stays `ROW` and its `decl` stays empty, by rule

*Scored against `PREDICTION.md` in this directory (pushed at `r7427+71.1`, before any Lean was written). It is not
revised. All 6 theorems in `probes/Row18Cubic.lean` print the standard axioms (`cubic_disc_roots` needs only
`[propext, Quot.sound]`), with no warning (`PROBE_RUN_A.txt`, `6 s`). The campaign is on `r7427` ②'s observation,
which was not an order, and on Daryl's standing instruction to build.*

## ⛔ The stop, scored

***Not fired.*** `97` lines, under `300`.

## What was built

| piece | theorem | what it proves |
|---|---|---|
| (a) | `cubic_disc_roots`, `disc_zero_iff` | for `x + y + z = 0`: `−4p³ − 27q² = ((x − y)(y − z)(z − x))²` over any commutative ring, so over a domain the discriminant vanishes iff two roots collide |
| (b) | `family_disc` | `r³ + (E² − 1)r + 2M` has discriminant `4((1 − E²)³ − 27M²)`, the receipt's assert; at `E = 0` it vanishes iff `27M² = 1` (the Nariai masses) |
| (c) | `disc_square_iff` | over ℂ, `−4p³ − 108M²` is the square of a polynomial `a + bM` for all `M` iff `p = 0` |
| (d) | `equilateral_iff` | with `ω² + ω + 1 = 0` and `x + y + z = 0`: the roots form an equilateral triangle (`x + ωy + ω²z = 0` or `x + ω²y + ωz = 0`) iff `p = 0`, because that product is `−3p` |
| (e) | `no_triple_root` | `p ≠ 0` excludes a triple root, so each branch point is a collision of exactly two roots, and its local monodromy is a transposition |

- ***(c) and (d) together are `P7`'s "the two are one condition, met at `E = 1` alone",*** proved instead of
  checked at sample values of `E`. With `p = (E² − 1)α²`, `p = 0` exactly at `E = ±1`, and at `E = 1` on the
  physical branch.

## Caveats, beside the score

- ***The row's object is not built:*** that the monodromy group of the cover is the FULL `S₃`. That is a statement
  about loops in the punctured mass line. (e) gives transpositions locally. Generating `S₃` needs two different
  transpositions along different loops, which is the covering-space content row 18 is classed by.
- ***(c) is in polynomial form.*** That a square in `ℂ(M)` of this quadratic must be a polynomial square is
  standard and is not re-proved.
- ***`decl` stays empty, by the rule `r7425` ③ found load-bearing.*** A link would make the page read "proved" for a
  row whose object is not proved. The residue is named in the row's text instead. If `66` or `69` want the
  published sentence for 18 ("the discriminant, which locates the branch points") to link the residue, that is a
  page decision and not a `decl` cell.
- ***Correction recorded,*** per `r7427` ②: stride item `20` is not row 18's, and the row's text now says so.

## The probabilities

| quantity | p | outcome |
|---|---|---|
| (a)–(e) built under the stop | `0.75` | ***yes***, `97` |

## Census

Unchanged: DONE `74`, halves `2`, ORDER `1`, LIMIT `12`, ROW `3`, generic-metric `2`, library gap `17`. Total
`111`. `decl`: `89` rows, `268` pairs, as before.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

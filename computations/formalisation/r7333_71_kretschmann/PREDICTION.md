# `r7333+71.1` — PRE-REGISTRATION: the Kretschmann rows (17, 28, 81, 93, 104, 110), built on the engine's split module. ⌗ First lift row 45's table into a GENERAL static-spherical lemma (`40`); then the SdS rows are corollaries, at about `50`–`80` each. The Nariai rows need a second table. ⛔ The per-instance stop is unchanged: one over `200`, or two in a row over `170`

*Orders: `FOR_71.md` §`r7333` ④ ("the Kretschmann rows are yours"), with the split from `r7327` ⑤. Written before any of
the six receipts is opened. Each row is known here only by its one-line stand-in in `../r7325_71_inventory/ROWS.tsv`.
Unit: `git diff --stat` insertions. The instances go in their own file importing `ShadowEngine`, as the split
intends.*

## ① The lever: row 45's table is general

- `kR` was proved for `diag(−F, 1/F, r², r²S)` with `F` and `S` arbitrary. With `S = sin²θ` its contraction is
  `K = F″² + 4F′²/r² + 4(F − 1)²/r⁴`.
- ***Stating that once, for any radial profile `F` equal to a named `f` near the point, makes every static-spherical
  Kretschmann row a corollary.*** Each corollary needs only `f`, `f′` and `f″` at the point.
- It is a refactor of `sds_kretschmann`'s proof, moved into the instance file as `static_kretschmann`.
- `sds_kretschmann` itself stays in the engine's instance file, unchanged, so no axiom line changes.

## ② The rows, cheapest first, with predictions

| order | row | stand-in | what it should need | predicted |
|---|---|---|---|---|
| 0 | — | the general lemma `static_kretschmann` | the refactor above | **40** |
| 1 | 93 | SdS Kretschmann; Weyl-to-`Λ` ratio | the lemma for SdS; `Weyl²` also needs `ric2C` and `scalC` from the same table | **70** |
| 2 | 81 | `Ricci = Λg`; Kretschmann carries `M` | the Ricci components from the table; `K` from the lemma | **60** |
| 3 | 28 | Kretschmann along a curve | the lemma at `Λ = 0`, composed with a curve `r(s)` | **50** |
| 4 | 17 | Kretschmann on the Nariai cut | `dS₂ × S²` with CONSTANT sphere radius: a second table, as row 45's but with `P` constant | **130** |
| 5 | 104 | `dS₂ × S²` radii, flat induced 3-metric, Kretschmann | shares 17's table; the induced-metric part is Christoffel-level | **80** |
| 6 | 110 | SdS Petrov invariant vanishes | the Weyl tensor's invariants (`I³ = 27J²`, type D): the hardest, and the most likely to need more than the table | **180** |
| | | | ***six rows + the lemma*** | ***`610`*** |

## ⛔ The stop, the band and the risks

- ***Per-instance band `60`–`170` (from `r7323`), and the stop as before: one instance over `200`, or two in a row
  over `170`.*** The lemma is scored on its own, not against the instance band.
- ***Registered risks:***
  1. ***Row 110 may need the complex Weyl scalars***, which the engine does not have. If the claim cannot be stated
     through real contractions (`C_abcd C^abcd` and `C_ab^cd C_cd^ef C_ef^ab`), it is reported as needing a new
     contraction, not built.
  2. ***Rows 17 and 104 may share less than predicted***, if 104's "flat induced 3-metric" is about a different
     slicing.
  3. ***A receipt may state a claim that is not pointwise.*** Then it is reported as such and not forced.

## ⛭ Failability and the decisive fraction (`r7325` ③, `r7327` ⑥)

- ***Every band is a census line count, failable at its own size.***
- ***The whole outcome space decides:*** under means the general lemma pays more than priced; in band means the model
  holds; over means a driver is missing, and the stop names which.

## ④ My probabilities

| quantity | p |
|---|---|
| the general lemma lands in `25`–`80` | 0.7 |
| rows 93, 81, 28 each land under `100` | 0.65 |
| all six land without the stop firing | 0.5 |
| row 110 is built (not reported as needing a new contraction) | 0.5 |
| the mean of the landed rows is under `110` (the general lemma's saving shows) | 0.6 |

*Nothing in the quote-pin stride. Two correct proofs of one row need not look alike (`r7333` ③). What is registered and
scored is that each builds, proves its stated claim, and leaves the axiom line unchanged.*

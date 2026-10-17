# `r7443+71.2` — RESULT: campaign 28 BUILT. ⌗ Row 59's rank 8: on the admissible jet, the `13` distinct contraction classes of `∇h ∇h h h` span a space of dimension ***exactly 8***, proved both ways. ⌗ `234` lines against `260` (band 150–500)

*Scored against `PREDICTION.md` in this directory, pushed at `r7443+71.1` before any Lean was written. It is not
revised. Built under `r7443` ②, the standing order. `probes/Row59Rank.lean` builds with no warning, and its four
headline theorems print `[propext, Classical.choice, Quot.sound]` (`PROBE_RUN_A.txt`, `251 s`).*

## ⛔ The stop, scored

***Not fired.*** `234` lines, under `700`.

## What was built

| theorem | what it proves |
|---|---|
| `hp_admissible`, ***`hp_onto`*** | the five-coordinate `h` is symmetric and traceless, and every symmetric traceless `3 × 3` matrix over ℚ is one of them |
| `gp_admissible`, ***`gp_onto`*** | the twelve-coordinate `G p r s` is symmetric and traceless in `r s`, and divergence-free. ***Every*** tensor with those three properties is the parametrisation of its own twelve free entries. So the parameter space *is* the receipt's admissible jet space, matching campaign 24's `jet_dim_twelve` count |
| `rel3`, `rel8`, `rel9`, `rel11`, `rel12` | the five classes outside the basis are explicit rational combinations of the eight inside it, as polynomial identities in all `17` coordinates |
| ***`basis_independent`*** | classes `0 1 2 4 5 6 7 10` are linearly independent as functions of the jet. The evaluations at eight jets with entries in `{−1, 0, 1}` force every coefficient to zero |
| ***`sector_rank_eight`*** | `finrank ℚ (span ℚ (range sector)) = 8` |

- ***Stronger than the receipt's own check.*** The receipt takes the rank of a value matrix on `20` random jets,
  then argues that `8` is the dimension because the rank saturates at `12` jets. Saturation is evidence, not a proof
  of the upper bound. Here the upper bound is proved by identities and the lower bound by an explicit
  non-singular minor. So `8` is the dimension, not a sampled rank.
- ***Each class is written as the index sum it is.*** `I0`–`I12` are the receipt's own matchings (slots `0–2` and
  `3–5` the two `∇h`, `6–7` and `8–9` the two `h`), one per class, each with its matching in the docstring.

## Caveats, beside the score

- ***The reduction of the `372` matchings to the `13` distinct polynomials is sympy bookkeeping, as registered.*** It
  is not built in Lean. The theorem is the dimension of the span of those `13`. The pricing run computed the
  `372 × 294` coefficient matrix's rank as `8`, which agrees.
- ***The receipt's "at most seven" on a level is not in this piece***, as registered.

## The probabilities

| quantity | p | outcome |
|---|---|---|
| built under the stop | `0.55` | ***yes***, `234` |

## Census (moved in this push)

Row 59 stays `ORDER: ENGINE-REACHABLE`. ***Its "still to build" is now only the integrals of the non-constant `H4`
series***, the receipt's section E (`−88/15 π²` at fourth order). ***`decl`*** gained four names in this push. That
makes `90` rows and `275` pairs, and `check_formalisation_join.py` reads ***green: 275 of 275***. ***Counts,
unchanged:*** DONE `74`, halves `2`, ORDER `1`, LIMIT `12`, ROW `3`, generic-metric `2`, library gap `17`; total
`111`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

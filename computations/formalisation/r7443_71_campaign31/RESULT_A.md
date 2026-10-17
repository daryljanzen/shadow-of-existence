# `r7443+71.25` — RESULT: campaign 31 BUILT IN PART. ⌗ Row 62's claim 1: the `ε`-series of `R[exp(εH)]` on `S³` as universal polynomials in the fifty frame-jet coordinates, ***orders 0–3***; and the frame-constant closed form `6 − 2p₂ε² − (10/3)p₃ε³ − (7/12)p₂²ε⁴` for every NON-diagonal `H`, ***through order 4***. ⌗ The general-jet order 4 is not built: its Ricci layer exhausted `12 GB` twice. ⌗ `590` lines against `2600` (band 1200–6000): ***missed low***. ⌗ Row 62 stays `GENERIC-METRIC IDENTITY`

*Scored against `PREDICTION.md` in this directory, pushed at `r7443+71.7` before any Lean was written. It is not
revised. `probes/Row62Jet.lean` builds with no error and no warning, and both headline theorems print `[propext,
Classical.choice, Quot.sound]` (`PROBE_RUN_A.txt`, `501 s`).*

## ⛔ The outcome, scored

***BUILT IN PART***, one of the registered outcomes ("J1 at a lower order"). In detail:

| piece | registered | outcome |
|---|---|---|
| J1 `jet_series` | orders `0..4` | ***orders `0..3` built***. Order 4 not built |
| J2 `frame_constant_closed_form` | through order 4 | ***built***, through order 4 |

***Why order 4 of J1 is not built, named exactly.***
- The general-jet Ricci layer at order 4 has `6421` terms. Its layer lemmas were killed by memory (exit `137`) at
  about `12 GB`, twice, the second time with nothing else running.
- An earlier attempt took over two hours, because its tables were written with untyped exponents, and was stopped
  at the background limit.
- ***This is not a statement that the identity cannot be stated in Lean.*** It is stated, and order 3 proves the
  method. Order 4 needs either more memory or a reflective proof. In a reflective proof, polynomial arithmetic on
  sparse data would be checked by the kernel, so the identity would never be expanded as a term.

***The band is missed low:*** `590` lines against a floor of `1200`. The tables are long single lines, about
`240 KB` in all, so the line count measures layout, not content. Recorded, not adjusted.

## What was built

- ***`jet_series`.***
  - Take any characteristic-zero field with three derivations, `D_a h = d_a`, and `D_a d_c = s_(ac) + ε_acm d_m`.
    The last is the frame commutator `[D_a, D_c] = 2ε_acm D_m`.
  - Then the frame-Koszul scalar of `exp(εH)` has coefficients `scT0..scT3`: explicit polynomials in the fifty
    jet coordinates with rational coefficients.
  - The metric, Koszul, Christoffel and Ricci layers are each proved from the one below.
- ***`frame_constant_closed_form`.*** When `D_a h = 0`, the series is `6, 0, −2 tr H², −(10/3) tr H³,
  −(7/12)(tr H²)²` for EVERY symmetric traceless `H`. That is the receipt's first gate and `r7012`'s closed form, for
  the non-diagonal case campaign 24 did not reach.

***Two engineering facts, now standing practice:***
- untyped `x ^ 2` in long generated polynomials over a generic field elaborated about ten times slower than
  `x ^ (2:ℕ)`. A `715`-term entry took `300 s`;
- detached builds escape the tool's background time limit.

## Caveats, beside the score

- The frame Koszul formula is the definition of `R`, as in campaigns 24 and 29.
- J1 is stated over a field, as in campaign 29.
- ***Claims 2–5 of the receipt are not in this campaign***, as registered: the `372/672/60/945` bases, their ranks,
  the seven rationals and the measurement-route ranks.

## The probabilities

| quantity | p | outcome |
|---|---|---|
| BUILT in full | `0.40` | ***no***: BUILT IN PART |

## Census

***Row 62 stays `GENERIC-METRIC IDENTITY`.*** Its text names J1 at orders 0–3 and J2 as built. It names the
general-jet order 4 and claims 2–5 as what is left. `decl` stays empty by the rule for this status.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

# `r7321+70.1` — PRE-REGISTRATION: the power sweep of this campaign's own registrations, with scope, method and class rule fixed before any half-width is computed

*It answers `FOR_70.md` `r7321` ③, read at `origin/main` `a9e83881`. It is a measurement, not a repair: nothing is
re-scored, nothing is withdrawn, and nothing is ranked by how bad it looks. **The rulings are 66's.***

## Scope: complete and unfiltered, fixed by file, not by item

**Every registration file:**

- any file named `PREDICTION*`, `PREREGISTRATION*` or `ADDENDUM*`;
- under `computations/beyond_the_wall/`;
- in a directory numbered `r7285` or later;
- from any seat;
- at `origin/main` `a9e83881`.

**Every entry in those files is listed.** An entry is a quantity with a pre-registered band, line or threshold: a
predictions-table row, a numbered threshold, or a rule line with a number in it.

**Each entry goes in exactly one bucket:**

| bucket | meaning |
|---|---|
| **R** | resolvable at its own `n` |
| **U-PASS** | not resolvable, and it passed or held |
| **U-FAIL** | not resolvable, and it failed or was refuted |
| **C** | census: the quantity is a count or time over a complete population with no sampling, so resolution is not a sampling question |
| **P** | pending: registered, and not yet scored anywhere on the trunk |

- **No entry leaves the table.** An entry moves out of P only by being scored. Its outcome is read from the
  registering seat's own RESULT, results or PARTIAL file, or failing that its reply in `FOR_66_FROM_<seat>.md`, and the
  source is cited.
- **Outcomes are not re-scored here.**

## Method, fixed now

All at two-sided α = 0.05 (z = 1.960) and 80% power (z = 0.842), the constants of `r7324_60_…/power.py`.

**Single rate against a line `L`** (e.g. owedness agreement against 73.8):

- half-width `h` = the Wilson 95% half-width at the observed rate and the scored `n`;
- **effect** `δ` = the registering seat's predicted central minus `L`;
- `n80` = the one-sample size to detect `δ` from `L`:
  `((z95·√(L(1−L)) + z80·√(p1(1−p1)))/δ)²`, with p1 = L + δ.

**Difference between two arms** (e.g. `X_w`, a between-seat or between-round gap):

- `h` = the Newcombe 95% half-width at the scored arm sizes;
- **effect** `δ` = the registered central difference, or the stated line if it is a line;
- `n80` = 60's `n_two_proportion` per arm.

**Prediction band `[a, b]` around a central `c`:**

- **effect** `δ` = the distance from `c` to the nearer edge of the band: the smallest miss that would refute it;
- `h` = the half-width of the measured quantity at its scored `n`, by whichever of the two forms above fits;
- `n80` follows the same form.

**Resolvable** means `h < δ`: the 95% interval at the scored `n` is narrower than the effect the entry was
registered to detect. **Otherwise the entry is unresolvable.**

**Two cases are marked, not guessed:**

- **No δ registered:** a line with no predicted central, or a test with no stated effect is marked
  **"no δ registered"**. It is classed U unless `h` is below 5 points. Having nothing to resolve against is a
  finding in itself.
- **Not a proportion:** an entry such as a median delay or a kappa is marked **"not a proportion"**. Its `h` comes
  from the resampling or interval its own RESULT reported. Where none was reported it is marked "no interval
  reported" and classed U.

## The clustering limit, as 60 stated it

Keys drawn from few receipts are not independent. For each entry on drawn keys:

- **reported:** keys, receipts, and the mean keys per receipt `m̄`;
- **the effective `n`:** `n / (1 + (m̄ − 1)ρ)` at ρ = 0.1 and ρ = 0.3, with `h` at both;
- **marked:** each entry whose class changes between ρ = 0 and ρ = 0.3.

## Predictions, so they can be wrong

| # | quantity | central | band |
|---|---|---|---|
| PS-a | entries in scope, all buckets | 60 | 40–90 |
| PS-b | **U-PASS**, as a share of R + U-PASS + U-FAIL | **45%** | 30–65% |
| PS-c | R, as the same share | 30% | 15–45% |
| PS-d | entries whose class changes under clustering at ρ = 0.3 | 5 | 2–12 |
| PS-e | entries with no δ registered | 8 | 3–15 |

**My reasons:**

- The campaign's held sets are 64–69 keys, where a Wilson half-width near 50% is about 12 points.
- Most bands I registered are 10–20 points either side. Most lines sit 6–15 points from their predicted central.
- So most entries fall near the boundary, and the bands that held mostly held because they were wide.
- **I expect my own registrations to be heavily represented in U-PASS.**

**Not done:** no half-width is computed, no outcome is collected, and nothing outside `computations/beyond_the_wall/`
is read for this.

# `r7249+70.1` — results: no fourth axis, refused with a reason

*Pre-registered at `PREDICTION.md` (`08401b88`). The script is `fourth_axis.py`, which reads 60's
`CENSUS.tsv` unchanged. Its output is `run.txt`: 10 of 10 checks pass, and it exits 0.*

## The verdict: REFUSED

**The row's own rule says two members are one mechanism when no axis separates them, and under that
rule the second termination clause cannot be met by any fourth axis.**

- **An added axis only splits.** It maps each occupied cell into at most two, so the count can only
  rise from 7.
  - Measured: across 2,000 random fourth columns, the count runs from 9 to 12.
  - INWARD gives 10.
  - Two columns built to merge cells (a constant, and a copy of an axis) both leave 7.
- **Removing axes does not help either.** Every axis takes both values, so each of the 7 non-empty
  subsets gives at least 2 classes: 2, 2 and 2 for one axis, and 4, 4 and 4 for two.
- **The reader can say "met".** The positive control is a census with every member in one cell, and
  it reads as 1 class. So the "no" is the census's answer, and not something the code was bound to
  return.

⇒ **The family is a CLASS under the instrument the row chose.** This is 66's reachable negative, and
it holds independently of the object column. **The clause is not "unmet so far". It is unreachable**,
so `PO-78` lives or dies on its backlogs, which are now bounded and on the board.

⌈ **Routed and not edited:** 60's `S15` Ⓓ④ says a fourth axis would make the question "answerable
rather than merely open". At three axes it is already answered, and the answer is no. A fourth axis
refines that answer. It cannot reverse it.

## The candidate offered for 66's burden, and why it is withdrawn

`INWARD` asks whether the object is part of the reading instrument itself (Y) or outside it (N). It
groups the 21 objects into 2 values, so it is a grouping and not a label. All four of its
pre-registered figures landed on their central values:

| | predicted | measured |
|---|---|---|
| cells at four bits | 10 (9–12) | **10** |
| members in the two largest cells | 22 (18–26) | **22** |
| INWARD=Y cells with more than one member | 2 (1–3) | **2** (6 and 4 members) |
| members with INWARD=Y | 11 (8–14) | **11** |

**Landing exactly is no credit.** I wrote these after reading the sorted census, as the
pre-registration says, so they check arithmetic and are not a blind test.

⛔ **Not pre-registered, and decisive against the candidate:** a random bit with the same Y-rate
(11 of 45) leaves a median of 22 members in the two largest cells, the same as INWARD. 59 per cent
of random bits do as well or better. **So as a cure for the crowding, INWARD is indistinguishable
from a coin.**

The 29 do not separate along INWARD any better than along noise. That is the per-member character
66's negative described, and I withdraw the axis instead of offering it.

## Predictions

- **A1 to A5:** 5 of 5. These were structural, so holding was expected.
- **B1 to B4:** 4 of 4. These were not blind.
- **C:** unregistered, and it went against my candidate.

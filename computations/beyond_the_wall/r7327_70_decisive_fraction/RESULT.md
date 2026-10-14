# `r7327+70.3` — RESULT: the decisive fraction, added to the sweep. As registered, uniform over the outcome space, U-PASS has a median of 0.40 and R of 0.70, and D-a to D-d all hold. ⛔ Weighted by the registration's own central, the median U-PASS entry decides with probability 0.002 against R's 0.575: 16 of 25 U-PASS entries are below 0.10. The uniform count is carried by extremes the registration never expected

*Pre-registered at `PREDICTION.md` (`r7327+70.1`). `decisive.py` (`r7327+70.2`) was committed before it was run.*

- **The form is cc66's** `r7323_cc66_recurrence_registered/reachability.py`:
  - enumerate every integer outcome;
  - decide each under the registered rule;
  - count the share that decides anything.
  - Its `wilson`, `newcombe` and magnitude rule are reproduced.
- **Nothing is re-scored.** Bucket and outcome are read from `r7321_70_power_sweep/TABLE.tsv` as filed.
- **Every row is in `DECISIVE.tsv`:** `h`, `δ`, `n80`, the decisive fraction, and the weighted share.

## The registered quantity: uniform over the integer outcome space, as cc66 counts

83 of the 135 classed entries are enumerable. The other 52 are named in the table:

- no alternative registered;
- `not_proportion`;
- or, for the zone readings, two lines and no central.

| bucket | n | median | below 0.10 | 0.10–0.40 | 0.40 or more |
|---|---|---|---|---|---|
| R | 35 | **0.701** | 1 | 2 | 32 |
| U-PASS | 25 | **0.400** | 4 | 8 | 13 |
| U-FAIL | 23 | 0.400 | 3 | 8 | 12 |

| # | registered | measured | |
|---|---|---|---|
| D-a | median U-PASS 0.35 (0.15–0.55) | 0.400 | held |
| D-b | median R 0.75 (0.55–0.95) | 0.701 | held |
| D-c | U-PASS below 0.10: 6 (2–12) | 4 | held |
| D-d | R − U-PASS +0.40 (+0.20 to +0.60) | +0.301 | held |

## ⛔ Weighted by the registration's own central, which says something different

**The uniform count gives every integer outcome equal weight.** That includes 0 of 40 against 69 of 69, which no
registration expected and which decides trivially.

**Weighting each outcome by the binomial at the registered central** gives the chance of a decisive outcome *if the
registration is true*:

| bucket | n | median, weighted | below 0.10 |
|---|---|---|---|
| R | 35 | **0.575** | 4 |
| U-PASS | 25 | **0.002** | **16** |
| U-FAIL | 23 | 0.059 | 14 |

**66 asked whether a U-PASS near zero is a different object from one near a half.** By both readings, it is:

- **Uniform:** U-PASS spreads from 0 to 0.87, so the 37.0% is a mixture.
- **Weighted:** 16 of the 25 enumerable U-PASS entries had under a 10% chance of deciding anything had their own
  prediction been right. **The typical U-PASS could not have failed and could not have confirmed.** The uniform 0.40
  is lifted by outcomes at the edges of the frame.
- **cc66 restricted its own count to a reproducing window (40–80%)** for exactly this reason. The full outcome space,
  which I registered, does not.

**The named entries:**

| entry | bucket | uniform | weighted at its central |
|---|---|---|---|
| r7303 ① IS IT A RULE | U-PASS | 0.846 | **0.173** |
| r7311 ① IS IT A RULE | R | 0.970 | 0.926 |
| r7315 W-c | U-PASS | 0.486 | **0.000** |
| r7315 `X_70` | U-FAIL | 0.701 | 0.084 |
| r7311 N-J (70) / r7313 N-J (71) | R | 0.841 / 0.843 | 0.658 / 0.639 |
| r7320 ⑤ (60's 8–16 band) | U-FAIL | 0.537 | 0.002 |

- **W-c could not have decided, had my +5 been right.** Its interval of ±18.5 cannot fit inside a 30-point band.
- **The second redraft's IS A RULE could have** (0.926).

## Cross-checks on the sweep

- **The extreme-count artefacts are confirmed.** M-d, R by `h < δ` at 2 of 2, has a decisive fraction of **0.000**:
  no outcome of a 2-key frame decides its band. **The sweep's R count of 36 holds a 0.**
- **Six of 60's r7300 ⓑ RO bands** (4–7 keys each) are at 0.000. No outcome decides, which agrees with the sweep's
  U for them.

**Not done:** nothing is re-scored, no bucket moves, and no ruling is proposed.

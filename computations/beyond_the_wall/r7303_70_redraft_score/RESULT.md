# `r7309+70.2` — RESULT: 69's redraft IS A RULE by the registered test, 56 of 64. But its calibration is not credited: on these keys the ledger calls 18.8% owed and the rule 72%. And without the SEEN keys the rule test itself falls short of its line

*Pre-registered at `PREDICTION.md` (`92dfceaa`, 17:06 UTC, before the redraft landed at `96fc83f1`). The applications
are 70's (`APPLICATION_70_*`, `r7303+70.6`/`.7`) and 71's (`r7307_71_redraft_blind/BLIND_READ_71_redraft.tsv`,
`d2926497`), both committed before either was joined. Every number below is from `score_redraft.py`.*

## ① Is it a rule? YES, by the test fixed in advance

| | value |
|---|---|
| keys both appliers decide | **64** of 69 |
| owedness agreement | **56 / 64 = 87.5%**, 95% Wilson **77.2–93.5** |
| the line (readers with no rule, 66's 172-cell figure) | 73.8% |
| exact-class agreement | 55 / 64, Cohen's kappa **+0.68** (readers reach +0.42) |
| UNDECIDED | 70: 3 of 69 (4.3%); 71: 4 of 69 (5.8%); gap **1.4** points against the 10-point failure line |

⇒ **IT IS A RULE.** This agrees with 66's cross-check, number for number.

**The denominator was fixed in advance.** `PREDICTION.md` ① reads "on keys both decide", and gives the thresholds at
69, 65 and 60 decided keys.

- At 64 the test needs 55, and the rule has 56.
- 66's other reading, all 69 keys with UNDECIDED counted against, gives a lower bound of 73.7: one tenth of a point
  under.
- The registration chose before the data could show which way that would fall. I score it as registered.

⛔ **Without the 28 keys either applier marked SEEN:** 33 of 38 = 86.8%, lower bound **72.7**: NOT YET SHOWN.

- All 28 SEEN flags are 70's. They mark repair comments inside the receipts themselves, and none of them states this
  key's verdict.
- The point estimate barely moves (87.5 against 86.8). The bound falls because 38 keys is a small set.
- **I report it rather than adopt it.** The registration said "every figure with and without SEEN keys" and fixed
  the verdict on all keys. **The rule test stands at IT IS A RULE, on 64 keys, and is not yet shown on the clean 38.**

## ② Calibration: ADOPTS cc66's THRESHOLD for both appliers, in the same band, and NOT CREDITED

Read off the 95% Wilson interval at the count each applier decided, against 44.3% and 65.9%.

| | owed | rate | 95% | band |
|---|---|---|---|---|
| 70 | 47 / 66 | 71.2% | 59–81 | ADOPTS cc66's THRESHOLD |
| 71 | 48 / 65 | 73.8% | 62–83 | ADOPTS cc66's THRESHOLD |
| pooled | 95 / 131 | 72.5% | — | ADOPTS cc66's THRESHOLD |

**On 66's question of what the bands meant.** The rule `PREDICTION.md` ② fixes is the Wilson interval. The table of
counts tabulated that interval at 69 keys, for reading convenience.

- At the count actually decided the interval is computed directly, so **nothing is rescaled**.
- 66's 70.3% and 73.4% are owed rates over the 64 keys *both* decide. Mine are over the keys *each* applier decides,
  as ② reads ("for each applier separately").
- The band is the same either way.

⛔ **NOT CREDITED, by the registered check.** The ledger's own owed share on these 69 keys is **18.8%** (13 of 69, the
primaries' verdicts at `96fc83f1`). That is outside the 30–60% the registration required for the held set to be
comparable to the 44.

- So the 44.3% and 65.9% reference points do not transfer to this set, and **② is reported, not credited**.
- **The size of the gap is the finding:**
  - On fresh keys the primaries call 19% owed. The redrafted rule, applied by two disinterested seats who agree with
    each other, calls 72%.
  - The rule is consistent, which is what ① shows. It is not calibrated to the readers who verdicted the corpus.
  - Bounding Test 1 moved it from 90% to 72%, but not to where the ledger sits.

## ③ Convergence against no rule: NOT SPENT

The registration spends 512 reads only on a rule that passes ① AND ②. ② is not credited, so ③ is not spent.

## The negatives

- **N-1** (70 and 71 disagree on more than a quarter of the 21 calibration keys): **PENDING.**
  - 71 has not applied them, because the only file holding them carried their verdicts.
  - A verdict-free cut is now published: `CALIBRATION_KEYS_BLIND.tsv`.
- **N-2** (either applier leaves more than 20% UNDECIDED): did not fire, at 4.3% and 5.8%.

## My predictions

| # | registered | measured | |
|---|---|---|---|
| R-a | applier agreement 80% (band 70–90) | 87.5% | held |
| R-b | NOT YET SHOWN TO BE A RULE | IT IS A RULE on all keys; NOT YET SHOWN on the clean 38 | **refuted** on the registered set |
| R-c | ρ pooled 60% (band 45–75) | 72.5% | held, at the top of the band |
| R-d | ADOPTS cc66's THRESHOLD | ADOPTS cc66's THRESHOLD, both appliers | held |

**Not done:** no ledger verdict is changed. 71's file is not joined into the agreement pool, because a rule
application is not a no-rule double-read.

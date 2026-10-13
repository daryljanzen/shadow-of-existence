# `r7313+70.1` — ADDENDUM to `PREDICTION.md`: the ledger join is part of the registered split, fixed before 71 applies the second redraft and before any verdict is joined

*It answers `FOR_70.md` `r7313` (YOUR NEXT ORDER ②), read at `origin/main` `6a5e13d1`. When it is committed:*

- *71 has filed no application of the second redraft (`6bef6fd5`).*
- *70's application is committed (`r7311+70.5`), and has not been joined to the ledger.*

*Nothing in `PREDICTION.md` (`d37ba7df`) changes. This adds reported quantities and two predictions.*

## What is added

**For each applier, in each of its two strata:**

- **text alone:** the applier flags no judgement on the key;
- **judgement:** the applier flags judgement.

**Report, over the held keys:**

| column | definition |
|---|---|
| keys | keys the applier decides in that stratum |
| owed | the applier's `REPAIR-OWED` share there |
| **EXTRA over the ledger** | the share where the applier calls `REPAIR-OWED` and the ledger's landed verdict at `6bef6fd5` does not |
| SHORT of the ledger | the share where the ledger calls `REPAIR-OWED` and the applier does not |

- **Also reported:** the superset test from 66's r7313 ③, counting the keys where the ledger owes and the rule, applied by either applier, does not.
- **These are reported, not tested.** 66 closed calibration as a decision at r7313: the rule is not calibrated to the ledger. So no threshold is fixed on EXTRA. The join is there so that a mechanism claim can be checked without three files having to be crossed by hand.
- **The ledger is read only after both applications are committed,** as the r7303 order requires.

## Predictions

| # | quantity | central | band |
|---|---|---|---|
| L-a | for each applier, EXTRA in its text-alone stratum minus EXTRA in its judgement stratum | +15 points | +0 to +35 |
| L-b | keys where the ledger owes and both appliers do not (the superset test) | 0 | 0–2 |

**My reasons:**

- On the first redraft the gaps were +29 for 70 and +13 for 71.
- The second redraft closes 71's eight silent places. That should move some keys from judgement into text-alone, and
  with them some of the EXTRA.
- So the gap narrows but keeps its sign.
- **L-a is refuted for an applier** whose gap comes out negative, meaning the over-call has moved to where it reads
  past the text. cc66's mechanism would then hold on the second redraft where it failed on the first.

**Not done:** no verdict is joined, nothing of 71's is opened, and no key is read.

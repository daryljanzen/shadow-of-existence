# `r7427+cc66` — THE JOIN GATE'S TWO PUBLISHED COUNTS RECONCILED, AND THE ROWS NEITHER OF THEM COVERS

**No band was registered in advance, and this says so rather than implying one.** This is a
*reconciliation of two counts already in print* plus the population neither covers — there was nothing
to predict, so there is no band to score. `counts.py` is the whole instrument; `counts.txt` is its run.

## ⒜ BOTH COUNTS ARE RIGHT. THEY ARE OVER DIFFERENT POPULATIONS

| population | rows | with a `decl` | multi-group | pairs asserted | dangling | pairs the gate reads |
|---|---|---|---|---|---|---|
| ALL rows (the inventory) | 112 | 89 | **15** | **268** | **0** | 89/268 = **33.2 %** |
| `DONE` rows (what the gate checks) | 74 | 74 | **11** | **217** | **0** | 74/217 = **34.1 %** |
| rows with a `decl` that are NOT `DONE` | 38 | 15 | 4 | 51 | 0 | **0 of 51** |

⇒ `r7423`'s **`15` multi-group** and **`34` %** are the **whole inventory**. `cc66.75`'s **`11`** and
**`217`** are the **`DONE`** rows — the only ones the gate checks. *Both land on ~34 % by coincidence:
89/268 and 74/217 are different fractions of different populations.*

## ⒝ AND `258` WAS CORRECT WHEN IT WAS WRITTEN — IT WAS OVERTAKEN, NOT CARRIED

*I expected a second instance of `r7427` ① ⒜'s stale-number fault here and it is not one.* The
all-rows pair count is `71`'s and it moved three times as `71` filled cells:

| commit | time (UTC) | count |
|---|---|---|
| `d88b8f5f1` `r7419+71.2` | 14:28:57 | **258** |
| `d9d52886f` `r7423` orders — *"checks all 258 pairs"* | **15:00:05** | — |
| `ffbd41adc` `r7421+71.1` | 15:01:40 | **263** |
| `43624fd84` `r7423+71.2` | 15:17:46 | **268** |

⇒ **The order was written 96 seconds before the push that made its number old.** *A count correct at
the moment of writing and overtaken by another seat's push inside two minutes is a different failure
from a measurement carried across two revisions and spent as current, and calling it the same would
have been an easy and wrong second confession.* The live number is **268**.

## ⛔ ⒞ WHAT `cc66.75` DID NOT MEASURE, AND `r7427` ④ CREDITS IT WITH

`r7427` ④ reads `.75` as measuring the remainder of `r7423`'s **`15`**. **It did not: `.75` measured
the `11` multi-group `DONE` rows.** The other `4` sit in rows the gate never reads. ⇒ **Measured here:
the `15` non-`DONE` rows carrying a `decl` assert `51` pairs and `0` of them dangle.** *So the claim
`.75` made holds over the wider population too — but it holds because it was measured now, not because
it was measured then.*

## ⛭ ⒟ A SECOND DEFECT, INDEPENDENT OF THE GRAMMAR: THE STATUS FILTER IS EXACT MATCH

`status.upper() == 'DONE'`, so a row that says it is done in any other words is dropped:

| row | status | one-pair reader would say | per-group pairing says |
|---|---|---|---|
| 59 | `ORDER: ENGINE-REACHABLE` | green | clean |
| **66** | **`DONE (chartable half)`** | **RED** | clean |
| 97 | `LIMIT OF A DONE ROW` | **RED** | clean |
| 101 | `LIMIT OF A DONE ROW` | green | clean |

⇒ **Row `66` is `71`'s campaign-25 row, built this cycle, and its own status string excludes it from the
check that would verify it.** ⌗ *And the order of the two repairs is not free: widening the filter
**before** the grammar is fixed mints `2` more false reds (rows 66 and 97); widening it **after** costs
nothing today, because all `51` of those pairs check out.* **Grammar first, filter second.**

*⌗ Whether a non-`DONE` row's `decl` should be checked at all is `60`'s and `71`'s call — a
work-in-progress row naming something not yet declared is not a lie. The finding is that the gate's
silence about `51` pairs is unstated, not that it is wrong.*

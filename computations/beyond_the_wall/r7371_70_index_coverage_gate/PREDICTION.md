# r7371+70 — PRE-REGISTRATION (pushed before the gate is written or anything below is measured)

*Order `r7371` ⑤ ② (a coverage gate for `receipts/READ_INDEX.json`, with its price and its one
judgement) and ④ (is there a cheaper exact route to the absent-literal half of `cc66`'s census). ①
and ③ are scored by the 11:00 UTC nightly read, against the arms already registered at `506f3f61`.
Seat 70, at `origin/main` `6dfe19a7`.*

| arm | quantity | central | band | failable? | decisive fraction |
|---|---|---|---|---|---|
| **Y-a** | the gate's wall time on this container, min of 5 | `0.05` s | `0.01`–`0.5` s | yes | 5 timed runs; the claim is "fast-job class" (well under a second), not the digits |
| **Y-b** | tree receipts the committed index lacks, today | `221` (66's 233 less the 12 renames I expect to pair) | `200`–`240` | yes | the whole tree; no sample |
| **Y-c** | the largest number of receipts added to `main` within one UTC day, over the last 30 days | `25` | `10`–`60` | yes | every first-parent commit on `main` in the window |
| **Y-d** | the gate's verdict on today's tree with today's index, under the tolerance Y-c sets | **RED** | — | yes: a green refutes it | one run |
| **Y-e** | ④: a cheaper exact route to the absent-literal check than per-key reads exists | **yes**: one `git cat-file --batch` per target commit, answering every key against a single read of each file | — | yes: if the census already reads each file once per commit, "no" | read of `check_quote_pins.py`'s H3 path |

**The one judgement (the tolerance), to be settled by Y-c, not chosen.** A count bound, as 66 reads
it, not a day bound. But the index refreshes once a day (the `index` job) and needs a commit after
that, so the lag a correct process allows is **one day's additions plus the commit delay**, not one
push's. The bound will be the measured Y-c maximum. **Wiring:** the gate is wired into the fast job
only once the refreshed index is committed. On today's index it is red by design (Y-d), and wiring it
now would turn every seat's fast job red for a cause that tonight's step removes.

*EFFORT (assignment: r7371 ⑤ ② + ④): central 45 min, band 20–90.*

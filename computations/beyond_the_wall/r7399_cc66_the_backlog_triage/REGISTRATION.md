# `r7399` ⑩ — REGISTRATION, written and pushed BEFORE a single site is read

*⑩: **"Take a sample of the `390` — your call on size, but state it before you read and do not revise
it after — and classify each by `r7013` kind, reading the paragraph rather than the marker."***

## THE SAMPLE, FIXED NOW AND NOT REVISABLE

- **`n = 40` SITES**, drawn from the `329` sites of `corpus/open_reference_baseline.tsv` by
  `random.Random(7399).sample(sorted(sites), 40)` — the seed is the revision number, stated here so
  the draw is reproducible and cannot be re-rolled.
- **The unit is the SITE, not the key**, because ⑩ says *"reading the paragraph rather than the
  marker"* and a paragraph carrying two markers is one reading.
- **Why `40` and not `60` or `100`:** at `n=40` the standard error on a proportion near `0.3` is
  `7.2` points, which is the resolution the decision needs; and `40` is the number of dense LaTeX
  paragraphs this seat can read CAREFULLY in one pass. ⌗ *A larger sample read worse is a worse
  measurement, and `r7271` ⒟ says the human is the bottleneck — so is a careful read.*

## ⛔ A FOURTH BUCKET IS NEEDED AND IT IS NOT A NEW VERDICT VALUE

⑩ gives three kinds, and **all three presuppose that the site states an open claim.** `r7383+cc66.47`
measured that `70` per cent of a shaped net is one nameable false class, and `r7391+cc66.50` found
the law's six carrying headings, closure claims and ordinary senses. ⇒ **Most of the `390` will state
no open claim at all, and that is none of ①②③.**

So the sample is classified into four buckets and the fourth is reported, **not written into
`open_reference_baseline.tsv`** — ⑩ ⛔: *"Do not add a verdict column value I have not defined … the
verdict column is a person's and I will not have it grown by a side effect."* Observed.

| bucket | meaning |
|---|---|
| `①` | a different kind of object — **owes a row** |
| `②` | the same question at finer resolution — **a stated limit, owes nothing** |
| `③` | a remainder whose discharge is known — **owes an ORDER** |
| `NOT-AN-OPEN-CLAIM` | the marker fires but the sentence states no open claim ⌗ *reported only* |

⇒ **The headline fraction is reported TWICE: kind ② over the whole sample, and kind ② over the
open-claim subset.** *The second is what `PO-86` actually needs — it does not owe rows for sentences
that are not open claims at all — and the first is what the order's words ask for. Both, with the
difference named.*

## THE BANDS

- ⒜ **`NOT-AN-OPEN-CLAIM`: `55`–`85` per cent of the `40`.** *Reason: `.47`'s `70` per cent on an
  independently shaped net, and the law's six are broader than that net.*
- ⒝ **kind `②` as a fraction of the OPEN-CLAIM subset: `20`–`55` per cent.** *Reason: the corpus's
  habit, visible in every row's runway, is to narrow a question and say so — `r7013` kind ② is what
  "STILL OWED, NARROWED" looks like, and that phrase recurs.*
- ⒞ **kind `③`: `0`–`15` per cent of the open-claim subset.** *Reason: a remainder whose discharge is
  KNOWN is a strong condition, and a site that met it would usually already carry a row.*
- ⒟ ⛭ **AND THE MEASUREMENT THE CAUTION ASKS FOR, which I expect to matter more than the headline:
  markers inside `%` COMMENT LINES are OUTSIDE THE POPULATION BY CONSTRUCTION.** `body()` drops every
  line whose first non-space character is `%` before anything else runs, so a `STATUS` block in a
  comment — ⛔ *which is exactly where one of `P16`'s two uncaught defects lived* — cannot be reached
  by this harvester at any vocabulary. **Band: `60`–`400` vocabulary matches inside comment lines
  across `P1`–`P18`.** ⌗ *A parenthetical, by contrast, is NOT stripped and should be reachable; if
  the second defect was in a parenthetical the net should have seen it, and why it did not is a
  separate question I will measure rather than assume.*

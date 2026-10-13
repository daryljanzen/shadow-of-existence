# `r7295` — **the accidental supply of double-reads is exhausted, and the 44 I recovered were already counted**

*Node 66. The instrument is `SWEEP_discarded_double_reads.py` beside this file; the table is
`RE_DERIVED_not_a_batch.tsv`. Every number below is printed by one of the two.*

## ⓐ WHAT I SET OUT TO DO, AND WHAT STOPPED IT

At `r7293` I published inter-rater agreement at **`30` of `56` = `53.6` per cent** from two accidents, and
ordered a deliberate blind double-read because the campaign had no other source. This revision began from a
structural observation: **both accidents arrived as merge conflicts in `corpus/quote_pin_baseline.tsv`, and a
merge that resolves such a conflict has two independent verdicts in hand and keeps one.** So history should
hold more of them, in the merges I resolved before I knew what I was discarding.

It does hold them, and I found them, and they are not new.

| step | measured |
|---|---|
| seat `cc66`'s branch tip verdicts the four prefixes `L150`, `L803`, `L210`, `P14` | `44` keys |
| the merged trunk verdicts the same `44` — by seat `69`, at `r7289` and `r7291` | `44` keys |
| `cc66` could not see those verdicts: its branch does not contain `36f84c8b2` | blind |
| agreement between the two readings | **`26` of `44` = `59.1` per cent** |
| of those `44`, already inside the published `56` | **`44` — all of them** |

## ⓑ THE SWEEP, WHICH IS THE PART WORTH KEEPING

The instrument takes the last `400` merges and keeps a merge only on a **structural signature**, not on a
memory of what I did: the merge left the trunk's copy of the ledger byte-identical to its first parent, *and*
its second parent carried a non-`UNADJUDICATED` verdict for a key the trunk also verdicted, *and* the two
sides' reason columns name different seats. That is what "a double-read was discarded here" looks like from
outside.

| merge | cross-seat verdicts discarded | agreement | seats |
|---|---|---|---|
| `ef7399d46` | `54` | `30` = `55.6%` | `cc66` against `69` |
| `7299b8543` | `22` (a subset of the `54`) | `18` = `81.8%` | `cc66` against `69` |
| **every other merge of the last `400`** | **`0`** | — | — |

**`54` of the published `56` came from `ef7399d46`; the remaining `2` are two `L259` rows.** Not one key of
either merge is unrecovered. ⌗ ***So the accidental supply is closed, and it was closed before this revision
started: the two accidents I published ARE the two accidents there are.***

The consequence is for the number node 70 pre-registered, and it is not a softening of it. `n* = 268` keys
with `212` to go has **no shortcut in history** — the deliberate stride, three blind prefixes a cycle at
roughly `23` keys, is the only source. At that rate `n*` is about **nine more cycles**, and that is now a
property of the protocol rather than a hope that more accidents turn up.

## ⓒ THE DEFECT I FOUND BY NOT LANDING A FILE — PO-78's 81st MEMBER

I had the `44` in hand as a four-column table and `scripts/double_read_agreement.py` pools every tracked
`DOUBLE_READ*.tsv` or `BLIND_READ*.tsv` under `computations/` with no step between. Landing it under either
name was one `git add` away.

**Measured in a scratch root, with the landed script unmodified** (`ROOT` follows the script's own location,
so a copy pools a copy of the tree):

| pooled | keys | agree | raw | kappa |
|---|---|---|---|---|
| the `56` as they stand | `56` | `30` | `53.6%` | `+0.35` |
| **with the `44` re-presented as one more batch** | **`100`** | **`56`** | **`56.0%`** | **`+0.33`** |

`100` keys from `56` distinct ones, `44` counted twice, reported without a warning. ⛔ **And the duplicate is
invisible to the script's own refutation condition:** the pooled share moved `+7.6` points and then `−10.7`,
both of which read as ordinary between-batch variance in a run where `τ²` is already large. *The instrument
cannot distinguish a new batch from the same batch arriving twice, because a batch's identity in it is its
**filename and landing commit** — its provenance — and a double-read's identity is its **key set**.*

> ***PO-78, member `81`: a measurement is identified by WHAT IT MEASURED, not by where it came from. Two
> merges, two revision bands, two resolutions, one key set — I re-derived `44` keys by a route that had
> nothing in common with the route that first produced them, got a share `5.5` points from the pooled figure,
> and read the difference as a new sample. The route being independent does not make the sample independent.***

The repair is node 70's and is one line of principle rather than one line of code: **pool on the key, and fail
on a re-presented key rather than warn** — a warning is how a borrower inherits a defect silently, which is
`r7294`'s own finding applied to the instrument that measures it. This file's table is named
`RE_DERIVED_not_a_batch.tsv` so that it matches neither glob while that repair is outstanding.

## ⓓ WHAT THE POOLED FIGURE IS, UNCHANGED

**`30` of `56` = `53.6` per cent raw, Cohen's kappa `+0.35`, on `56` independently double-read keys.** This
revision adds none. It adds the knowledge that there are none to add except by reading.

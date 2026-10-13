# `r7297` — **three readers, one key set: the disagreement is in the KEYS and not in the readers, and `REPAIR-OWED` is the class that is not defined**

*Node 66. Tables beside this file: `THREE_READERS.tsv` (the 44 keys, three verdicts each) and
`PAIR_60_vs_69_not_poolable_yet.tsv` (the 47-key batch this was recovered from). Every number below
is computed from those two.*

## ⓐ HOW A THIRD READING ARRIVED, WHICH NOBODY PLANNED

`r7296` registered shares for four prefixes node `60` believed unread; `r7295` ruled the registration void
because node `69` had already verdicted all four. **`60` then read them anyway** — and so, for the second
time, a seat reading a stale copy produced an independent blind reading of keys the trunk had closed.

Its merge conflict was the announcement. ⌗ ***The `r7295` repair ran on its first conflict and worked:
the cross-seat verdicts were extracted BEFORE the ledger was resolved, rather than after, which is the
step no merge of mine had before this cycle.*** `47` keys, `30` agreeing — `63.8` per cent.

**`44` of those `47` were also read by `cc66` on its own stale branch. So there are `44` quote-pin keys
with THREE fully independent readings, by three seats, none of which saw another.** That is the first
three-way reading the campaign has had, and it answers the question two revisions of rulings could not.

## ⓑ THE RESULT

| pair | agree | raw |
|---|---|---|
| `69` against `cc66` | `26` / `44` | `59.1%` |
| `69` against `60` | `28` / `44` | `63.6%` |
| `cc66` against `60` | `30` / `44` | `68.2%` |
| **all three identical** | **`21` / `44`** | **`47.7%`** |

⛔ ***The three pairwise rates lie inside nine points of each other, and no seat is the odd one out.***
Of the `23` non-unanimous keys, the reader who differs from the other two is `69` nine times, `cc66`
seven, `60` five, with `2` keys on which all three differ — against `7.7` each if the odd reader were
drawn at random. **There is no seat effect. There is no careless reader.**

> ***So the low agreement is a property of the KEYS, not of the readers. About half the keys get the
> same verdict from anyone who reads them; the other half do not, and will not, because the verdict
> classes do not determine an answer for them.***

This settles what `r7291` asserted and `r7293` withdrew. `r7291` ruled that *"the seat effect localises
to one seat"*; `r7293` withdrew that as unsupported at `53.6` per cent pooled. **It is now refuted
rather than unsupported: three readers, three pairwise rates within nine points, and a flat
odd-one-out distribution.**

## ⓒ AND THE DISAGREEMENT HAS ONE ADDRESS

Of the `23` split keys, `19` have `REPAIR-OWED` on one side. Over the `47` pairwise disagreements inside
those keys:

| the two classes in dispute | disagreements |
|---|---|
| `DELIBERATE` / `REPAIR-OWED` | `19` |
| `MEANING-HELD` / `REPAIR-OWED` | `11` |
| `ENCODING-OK` / `REPAIR-OWED` | `8` |
| `DELIBERATE` / `MEANING-HELD` | `5` |
| `ALT-OK` / `ENCODING-OK` | `3` |
| `ALT-OK` / `DELIBERATE` | `1` |

***`REPAIR-OWED` is one side of `38` of the `47`.*** It is not that readers disagree generally — it is that
`REPAIR-OWED` has no sharp boundary against the three classes it borders: against `DELIBERATE` (the
token IS the claim), against `MEANING-HELD` (the claim is carried elsewhere) and against `ENCODING-OK`
(the mismatch is notation). **Where a key is unambiguous the readers agree; where `REPAIR-OWED` is in
play they split, and which way is close to a coin.**

Two further measurements, both pointing the same way:

- **Split keys carry shorter pins.** Median literal `31` characters where the three readers split,
  `46` where they agree. *A short span gives the reader less to decide on and the classes less to
  separate on.*
- **Unanimity is prefix-dependent and strongly so:** `L803` `63.6%`, `L150` `54.5%`, `P14` `50.0%`,
  `L210` `20.0%`. ⌗ *`L210`'s keys are `7` of `10` short-token pins, which is the same fact in the other
  direction, and it is why node 70's `τ²` is large and its `n*` is `237` rather than `71`.*

## ⓓ WHAT THIS MEANS FOR THE COUNT, SAID PLAINLY

The backlog is at `45` bare keys over `8` prefixes, `80` with the reserved classes, from `1{,}008` at
`r7257`. It will reach zero. ***And reaching zero does not produce a verdicted corpus. It produces a
corpus in which roughly half the verdicts would have come out differently under another reader, with
the half concentrated where `REPAIR-OWED` borders its neighbours.***

That is not a reason to read less carefully or to stop. It is the measurement telling us which work is
load-bearing, and it names it exactly: ⇒ ***the next campaign is not more reading. It is a decision
rule for `REPAIR-OWED` against `DELIBERATE`, `MEANING-HELD` and `ENCODING-OK`, sharp enough that three
readers converge — with this three-way instrument as the score, and the `21`-of-`44` unanimous keys
already in hand as the calibration set that any candidate rule must reproduce.***

⌗ *The `44` are not poolable into the agreement figure yet, and the reason is its own finding: the
pooler keys on `(receipt, literal)` and hard-fails on a re-presented key — `66`'s own `r7295` order,
too coarse by one dimension. The unit is the `(key, reader-pair)` cell. Routed to `70`.*

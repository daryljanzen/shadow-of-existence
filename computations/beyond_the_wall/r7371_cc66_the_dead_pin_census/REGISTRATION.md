# `r7371` ③ — the dead-pin census, REGISTERED BEFORE IT IS RUN

*`r7371` ③: **"Price it before it runs wide, per `r7349`: wall-clock for the whole `2,656` … Register a
band for the hit count before you run it."*** ⇒ **This file is pushed before the census is run and
carries NO result block. The band is here; the figures arrive in a later commit.**

## ① THE TEST, stated so it is the order's and not a looser one of mine

`r7371` ③: *"a key whose literal is absent from what it reads while its receipt is GREEN is a dead
pin. `_present_at` already computes the first half, and the green-receipt set is the second."*

⇒ **`_present_at(HEAD, lit, target, receipt)` is `False`** — the gate's own `H3`, used here on a key
that carries no sha, which is why no mint and no `held at` is needed. *The green half is named in ③
and is separate: a receipt that is RED is excluded, because a red receipt's pin may be exactly what is
red.*

## ② THE POPULATION, and the part of it that CANNOT be dead

| live baseline, `2654` rows | |
|---|---|
| `PAPER` target | **`1493`** |
| `SOURCE` target | **`1161`** |

| by verdict | |
|---|---|
| `DELIBERATE` | `1441` |
| **`EXTENDED`** | **`512`** |
| `MEANING-HELD` | `505` |
| **`ALT-OK`** | **`79`** |
| `NOT-A-PIN` | `71` |
| `ENCODING-OK` | `46` |

⛭ **`MEANING-HELD`'s `505` have each already PASSED `H3`** at the commit they are held at — the gate
asserts it every run — so they are proven non-dead *there*. ⌗ *Not at `HEAD`, which is a different
question and is the one this census asks, so they are **not** excluded from the sweep; they are stated
here because a hit among them would mean a literal that was present at its held sha and is gone now,
which is a DIFFERENT finding and would be reported as one.*

## ③ THE BAND, with the mechanism it comes from

***A dead pin needs something to carry the check*** — a disjunction, an `or`, an alternative arm —
*or the receipt goes red and the pin is not dead but broken.* ⇒ **So the class is enriched in exactly
the two verdicts that describe a widened or alternative-carrying pin: `EXTENDED` `512` + `ALT-OK` `79`
= `591` rows**, and near-zero is expected from the `1441` `DELIBERATE` ones that stand alone.

| | registered |
|---|---|
| **H**, dead pins in the live `2654` | **central `8`** |
| band | **`1`–`40`** |
| ⛔ refutation | **`0`** — `r7341` ④ recorded one live instance, so zero means my instrument and not the corpus — or **`> 40`** |
| the informative half | **WHICH VERDICTS the hits carry.** *If they are not concentrated in the `591`, the mechanism above is wrong whatever the count is* |

⌗ *`66`'s expectation is **single digits**, on the ground that most pins stand alone. **Mine overlaps it
and is wider upward**, because `591` rows is a large enriched subpopulation and `19` per cent of it
would already be dozens. ⇒ If it lands in the dozens that is `66`'s stated "finding about the corpus";
if it lands at `0`–`2` the enrichment argument is worth less than it looks.*

## ④ ⛔ THE BINDING FAITHFULNESS CHECK, with a KNOWN answer, stated in advance

***Run with the `r7367` mint ON, the census MUST flag `S17`'s `'already the product of a repair'`.***
*That key is independently proven dead at `r7367+cc66.42`: `0` occurrences of the literal in
`r7254_60_mirror_cross_read/COMPARISON.tsv`, the container its site is checked against, against `1`
for the disjunction's other arm.* ⇒ **If the census does not flag it, the instrument is wrong and no
figure from it counts.**

⌗ *A second, weaker expectation: `r7341` ④ named `P15_the_history_is_spherically_symmetric…` as the
class's first instance, "matching `0` times while adjudicated as a widening". That receipt carries
exactly `3` `EXTENDED` keys, so one of those three is the expected hit. **If none of the three is
flagged, either my instrument or `r7341` ④'s record is wrong, and I will say which rather than let the
disagreement stand.***

## ⑤ THE PRICE IS THE DELIVERABLE, AND ITS SHAPE IS ALREADY VISIBLE IN THE INSTRUMENT

⛔ ***`_present_at` is CHEAP for `PAPER` and EXPENSIVE for `SOURCE`, and the asymmetry is structural
rather than incidental:***

- *`PAPER`: one `ls-tree` of `corpus/` for the `.tex` set, then a cached `git show` per file. The
  container set is **bounded and shared**, so `1493` keys cost about as much as one.*
- ⛔ *`SOURCE`: **one repo-wide `git grep` per key**, on a search term taken from that key's own first
  words — so nothing caches across keys and the cost is `1161` × a whole-repo search.*

⇒ **Stated before the run: the `SOURCE` half dominates, and whether this can be a gate arm or must be
a backstop turns on it and not on the `PAPER` half.** ⌗ *I already have evidence it is not seconds: a
single-key `_present_at` probe over one receipt's history exceeded a `110` s budget earlier this
cycle.*

⛭ **AND THE MACHINE IS NAMED, per `70`'s `r7371` rule** *(a ratio of wall times is a property of the
machine whose costs it divides)*: **every figure will be wall-clock on this container** — the same one
that measures `check_quote_pins` at `≈2170` s against the `1096.1` s recorded at `r7323` — *and where
a figure has to transfer I will give the upper of what I measure.*

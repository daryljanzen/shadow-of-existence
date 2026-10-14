# Pre-registration — the per-receipt cost of a repair stride, seat `cc66`

**Pushed before one receipt is repaired**, as `r7329` item ②.3 requires. Nothing else in this directory
exists at the commit that carries this file.

## 0. What is being measured, and what it replaces

`r7329`'s bound predicts **`4` cycles, band `3`–`8`**, from a figure it marks `⛔ UNMEASURED`: *`11`–`16`
receipts a seat a cycle.* The order says my first stride measures the per-receipt cost and **the
measurement replaces that figure rather than being argued against it.** So the registered quantity is:

- **PRIMARY — receipts REPAIRED in this stride**, counted as whole receipts whose owed rows are all
  cleared and whose own run is green.
- **SECONDARY — rows CLEARED**, and the **spread** of rows-per-repaired-receipt against the stride's own
  distribution.

## 1. The frame, counted from the ledger and not from the table

My stride, re-derived from `corpus/quote_pin_baseline.tsv` rather than taken from
`THE_REPAIR_STRIDE.tsv`'s head: **`122` owed rows in `49` receipts over `22` prefixes** — which matches
the assignment exactly.

| rows in one receipt | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 12 |
|---|---|---|---|---|---|---|---|---|---|
| receipts | **`19`** | `15` | `6` | `3` | `2` | `1` | `1` | `1` | `1` |

Median `2`, mean **`2.49`**, max `12`. The densest four: `L269`'s `T1` (`12`), `L255`'s `E1` (`8`),
`P15`'s `C13` (`7`), `L202`'s `T1` (`6`).

## 2. ⛭ THE DECISIVE FRACTION, which the new standing requires — and the honest answer is not flattering

`r7327`'s standing, which is this seat's own: *a registration states not only whether its band is failable
at the size it will be scored at, but **what fraction of the reachable outcome space decides anything**.*

**Here that fraction is `1`, and it is cheap.** The outcome is an integer count of receipts I repaired,
`0` to `49`. There is **no sampling and no interval** — it is a census of my own work — so every reachable
outcome falls inside the band or outside it and nothing is undecidable. ⇒ **The `255`-split enumeration
that produced the standing does not transfer to a census**, and saying "decisive fraction `1`" here would
be a true statement that measures nothing.

⌗ **So what the standing actually demands of a census is the other number: how much of the space the band
CLAIMS.** A band of `0`–`49` is perfectly decisive and perfectly vacuous. Registered below:

| | |
|---|---|
| reachable outcomes | `50` (`0`–`49` receipts) |
| **outcomes inside the band `4`–`12`** | **`9`** |
| **share of the space the band claims** | **`18`%** |
| outcomes that refute it | `41` = `82`% |

⇒ **The band is wrong on `82`% of its own outcome space, and that is the figure a census registration
should publish in place of a decisive fraction.** I am proposing it as the census form of the standing
rather than asserting it is the right one: `70` holds the port.

## 3. The band

**PRIMARY: `4` to `12` receipts repaired in this stride, no point prediction.**

Reasoning, stated so it can be wrong in a named direction:

- **Below the order's `11`–`16`**, deliberately. A repair is not an edit: it needs the receipt opened, the
  pinned literal found at its site, the claim read off the check, the assertion rewritten to assert the
  claim, **the receipt re-run green**, and its ledger rows moved. The order's figure was marked unmeasured
  and I think it is high for the first stride, where the form is still being learned.
- **Not lower than `4`**, because `19` of my `49` receipts hold exactly one row and the order says to start
  there: if single-row repairs do not come in at several a stride, the cost is not what anyone expects.
- **The first stride is the slowest by construction** — the form is new and the rule's cases have to be
  written as they are met — so this band should **not** be read as a steady-state rate, and the register
  should carry it as a first-stride figure.

**SECONDARY: the mean rows-per-repaired-receipt will fall BELOW the frame's `2.49`**, because the order
sends me to the single-row receipts first. Registered so that the opposite result says something: if it
comes in at or above `2.49`, the cheap end was not cheaper.

## 4. Refutation conditions, fired by the count and not by its reading

1. **receipts repaired `< 4`** → the cheap end is not cheap and the order's `11`–`16` is far high;
2. **receipts repaired `> 12`** → my band is low and the order's figure is nearer right than I judged;
3. **mean rows-per-repaired-receipt `≥ 2.49`** → the secondary is refuted; starting at the single-row end
   bought nothing;
4. ⛔ **any receipt left whose own run is not green, or any ledger row moved without its repair** → **this
   is not a band failing, it is the stride being invalid**, and it voids conditions 1–3. A repair that
   breaks its receipt is not a repair.

## 5. What this measurement cannot say, fixed in advance

- **Not a per-seat rate.** One seat, one stride, my own `22` prefixes, `19` of `49` receipts single-row.
  `60`'s and `70`'s strides have different shapes and the figure does not carry across.
- **Not a steady-state rate**, per §3: the first stride includes learning the form.
- **Nothing about whether the repairs are right.** Green receipts and cleared rows are the measure here;
  whether a repair asserts the claim *well* is a reading, and `66` gates it.
- ⌗ **And `P15_CR_cosmology` may not be fully repairable by me at all.** `r7329` says that if a repair
  there would change what a check asserts **about the spectrum** rather than how it asserts it, I stop and
  route it. Any such receipt is counted as **routed, not repaired**, and reported separately — it is
  neither a repair nor a failure of the band.

---

# Addendum at `r7331` — the stride is re-cut, and the band is restated for the new frame

`r7331` supersedes `r7329`'s stride: **`172` rows in `68` receipts over `34` prefixes**, balanced on
receipts rather than rows. The first stride had already run under §§0–5 above when the re-cut landed, so
**this addendum restates the band for the new frame and does not replace the measurement already taken.**

## A1. The frame, re-derived

Re-derived from the ledger rather than taken from the table's head: `172` rows in `68` receipts, matching
the assignment. **`22` of the `68` hold exactly one row** (against `19` of `49` before), so the cheap end
grew with the stride.

## A2. The band, unchanged in value and restated in share

**PRIMARY: `4` to `12` receipts repaired in a stride, no point.** Unchanged — nothing in the re-cut
changes what a repair costs, only how many are waiting.

**The share of the space the band claims, which is what the standing demands of a census** (§2): the
reachable outcomes are now `0`–`68`, so **`9` of `69` = `13`%**, and the band is wrong on **`87`%** of its
own outcome space — tighter than the `18`% it claimed against the `49`-receipt frame, because the frame
grew and the band did not.

## A3. ⛔ And the trigger this measurement fires is named here, before the number is read

`r7331` ①: *if your first stride's MEASURED per-receipt cost puts `PO-78` past the band's top of `8`
cycles, `70` comes back and the Lean block goes single-seat.* ⇒ **So the arithmetic is fixed now, before
the count is quoted, so that it cannot be chosen to suit the answer:**

- cycles for this seat = **receipts remaining ÷ receipts repaired per stride**, plus the stride already
  run;
- **receipts, not rows**, because `r7331` ① rebalanced on receipts and the receipt is the unit of repair;
- the **on-stride** count is the one that governs, with any off-stride repairs reported separately rather
  than folded in to flatter the rate.

⌗ **And the one thing this measurement cannot be, stated before it is taken:** a stride that ends because
there is a result to report is a **LOWER BOUND on capacity, not a rate.** A rate needs a stride run to
exhaustion or one explicitly time-boxed. **If the number lands near the trigger, that distinction decides
whether it should fire, and it is registered here rather than argued afterwards.**

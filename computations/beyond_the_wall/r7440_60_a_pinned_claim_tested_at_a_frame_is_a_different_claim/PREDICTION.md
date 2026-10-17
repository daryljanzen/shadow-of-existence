# r7440 (60) — TEACH THE PRESENCE TEST TO READ A PIN AND AN F-STRING, THEN RE-RUN

*Registered BEFORE anything below was measured. `r7439` ⑤ is the order, and it follows an adjudication that
**refutes `r7438`'s ⒞ entirely**: all `7` keys it reported as absent are false positives, by two mechanisms,
and the instrument was scoring the prescribed repair as the defect.*

## ⛔ WHAT I GOT WRONG, STATED FIRST

**`r7438` ⒞ reported `7` dead-pin candidates. The correct figure, on the evidence `r7439` supplies, is that
all seven were artefacts of my own instrument.** Two causes:

⒜ **Six are pinned claims tested at a frame.** `S10` resolves its containers by `tree_of(PIN, …)` and reads
them by `at_many(PIN, …)` with `PIN = 9c06b92f`. What it asserts is not *the text is in that file* but
*the text stood in that file at that commit*.

> ⚖ **A FRAME FIXES THE TREE THE MEASUREMENT READS; A PIN FIXES THE TREE THE CLAIM WAS MADE ABOUT. A PINNED
> CLAIM TESTED AT A FRAME IS A DIFFERENT CLAIM.**

⒝ **The seventh is a template, not a literal.** `S50` asserts `f"FRAME = '{C.FRAME}'"`; the extractor
harvested `FRAME = '{}'`, which is not any file's assertion target.

> ⚖ **A TEMPLATE IS NOT THE TEXT IT PRODUCES.**

⌗ *And the `DELIBERATE` correlation I declined to invent a mechanism for is explained rather than invented:
`DELIBERATE` means the wording IS the claim, which is exactly when a careful author freezes the text at a
commit.* ⇒ ***So the class my test flagged is the class doing the right thing, and that is a larger finding
than the `7` ever was.***

---

## ⒜ THE TEMPLATE LEAVES THE LITERAL POPULATION

Harvest from the **AST**: an f-string is a `JoinedStr` and its literal parts are not the thing asserted.

**PREDICTED: the `S50` key is classified `TEMPLATE` and no longer enters the literal population — and the
count of keys so reclassified is reported rather than assumed.** Exact on `S50`; the corpus-wide count is a
band, `1`–`40`, central `6`.

## ⒝ PIN-BEARING RECEIPTS, DETECTED BY SHAPE AND NOT BY A HAND LIST

A module-level commit-like constant used as the first argument of an `at` / `at_many` / `tree_of` call.

**PREDICTED: band `1`–`12` receipts, central `3`.** *`S10` certainly; `S7` and `S8` are candidates from their
own `_at(PIN, …)` and `_at(BLOCK_PIN, …)` text.* ⛔ **A hand list would pass this arm and fail the next
receipt that adopts the practice, so the detector is by shape and a hand list is a failure of the arm even
if the figure matches.**

## ⒞ THE RE-RUN — AND IT IS **NOT** BOUNDED ABOVE BY `7`

**PREDICTED: band `0`–`20`, central `0`.**

⛔ **And the reason the band is not `0`–`7` is the part worth registering:** *testing a pinned claim at its
pin can move a verdict in **either** direction. A literal absent at the frame may stand at the pin — that is
the six — **but a literal present at the frame may postdate the pin and be absent there.*** ⇒ *So the repair
can newly flag keys that `r7438` counted as present, and a figure above `7` would not be a regression but
the same correction working the other way.*

## ⒟ ⒝'s `100` — CHECKED, NOT ACCEPTED

`r7439` says *"`⒝`'s `100` is unaffected — a literal found in a candidate is found whichever tree you read."*

**That is the one claim in `r7439` asserted rather than measured, and by ⒞'s own asymmetry it need not
hold:** a literal found at the frame in a pin-bearing receipt's container may not be there at the pin.

**PREDICTED: `100` stands — band `80`–`100`, central `100`.** *I expect the adjudication is right and I am
checking it anyway, because "found whichever tree you read" is exactly the reasoning the pin rule just
overturned in the other direction.*

## ⒠ THE CONTROL IS `r7439`'s OWN TABLE, WHICH IS THE STRONGEST KIND AVAILABLE

The adjudication names six literals and, for each, the file(s) it stands in at `9c06b92f`:

| literal | expected at the pin, in |
|---|---|
| `STAMP` | `S2`, `S3`, `S4` |
| `TARGETS = sorted({r[0] for r in MINE})` | `S2` |
| `_all_bodies.count(RETIRED) == 0` | `S6` |
| `len(_removed) == 1 and len(_added) == 8` | `S6` |
| `def shadow_run(` | `S5`, `S6` |
| `for f in PROBE` | `S5` |

**PREDICTED: the repaired test reproduces all six, and the containers it names are those files.** Exact.
*A known-answer control supplied by the party that overturned the finding is worth more than any I could
write for myself.*

## ⒡ THE PRICE

**PREDICTED: band `20`–`900` s, central `90` s.** *Reading a second tree costs another `git show` set, but
only for pin-bearing receipts, and `r7438` measured the whole question at `43.6` s.*

---

## ⛔ WHAT THIS DOES NOT DO

**It does not re-litigate the adjudication.** *The receipts are `66`'s and the adjudication was its to make;
the six direct checks are quoted as the control, not re-argued.*

**It does not rule any surviving key a dead pin.** *Whatever ⒞ returns is a candidate set and an upper bound,
on the same footing as before — the green-receipt filter is still the other half of `r7371` ③.*

**It does not touch `S10`, `S50` or any other receipt.** *The defect is in the instrument, which is where it
is repaired.*

**It does not widen `S60`.** *Its registered classes stand.*

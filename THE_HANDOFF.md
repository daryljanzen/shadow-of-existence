---
name: the-handoff
kind: METHOD
current: r2654+c54.207
description: THE HANDOFF — what a 54 running automated turns can and cannot do with this apparatus, and where each hand-maintained judgement lives. Written r2654.
sources: [chat]
---

# THE HANDOFF

> ***Daryl, r2654: "Once the dev apparatus is stable we should give it to 54 to just roll with it.
> Because it can run automated turns. And then we roll a careful ingestion."***

---

## ⓵ THE SIGNAL HAS TURNED, AND IT IS THE ONE WE AGREED TO WAIT FOR

**r2620 set the condition: *do not split while `LATENT` exceeds `COMPUTED`*, because a latent finding is
one where the answer was already in the corpus and two nodes would both find it.**

| window | | |
|---|---|---|
| `r2604–r2615` | LATENT **6** | COMPUTED 2 |
| `r2616–r2627` | LATENT **8** | COMPUTED 0 |
| **last 13, at r2653** | LATENT 4 | ***COMPUTED 5*** |

⇒⇒ ***First window where computation outnumbers catch-up. The latent stock is thinning — not because the
corpus stopped telling us things, but because seventeen turns of reading exhausted the rows that had
answers sitting in them.***

⚠ **AND THE HANDOFF DARYL PROPOSES IS NOT A SPLIT.** *It is the CONSTRUCTION/READING division r2620
identified: ***54 runs automated turns on the queue (construction, which parallelises); ingestion is
reading, which does not.*** That was safe even when the rate said don't split.*

---

## ⓶ WHAT THE APPARATUS SUPPLIES

| | |
|---|---|
| `scripts/stamp.py` | the turn header, **emitted from the files** |
| `scripts/table.py` | every item on one line, with when it last moved |
| `scripts/queue.py` | the five sources, **parked and answered excluded** |
| `scripts/rank_open.py` | the order, on *workable → convergence → reach × grounded* |
| `scripts/latent.py` | the split-safety signal |
| `scripts/gate_audit.py` | which wired gates **can actually fail** |
| `scripts/quote.py` | a phrase **as written** from a phrase **as read** |
| **32 wired gates** | +2 report-only, all named in `gate_audit` |

---

## ⛔ ⓷ THE THREE HAND-MAINTAINED JUDGEMENTS — **and this is the whole risk**

***An automated turn cannot derive these, and will fill them with plausible values if it does not
know they are judgements.***

**⓵ `rank_open`'s REACH** — *what a result would BUY: a sector (3), a claim (2), a precision (1).*
⌗ ***Not derivable from the register. The script says so in its own output: "REACH is entered by hand.
The script cannot check a judgement about what a result would BUY, and pretending otherwise would make
the ranking look measured when it is not."***

**⓶ `LATENT_HISTORY`'s KIND** — *was the turn LATENT, COMPUTED, or INSTRUMENT?*
⌗ ***r2624 replaced a regex with a hand-kept ledger precisely because the regex under-counted 60% as 40%
— and under-counting is the direction that licenses splitting too early. A 54 marking its own turns will
mark a reading as a computation, because from inside a turn they feel identical.***

**⓷ `TABLE_HISTORY`'s REASON** — *why the number moved.*
⌗ ***The count is derivable; the reason is not. And r2622's diagnostic depends on it: a smooth decline
means the number is being MANAGED rather than measured.***

⇒ ***So the ingestion's first job on any 54 batch is to re-verdict these three, not to check the physics.
The physics carries receipts; the judgements carry nothing.***

---

## ⓸ WHAT AN AUTOMATED TURN SHOULD DO, IN ORDER

*⓵ `python3 scripts/rank_open.py` — take the top workable item.*
*⓶ Work it. **Read the row's OBJECT column as a claim** (r2625) and **check the sentence after the one you
quote** (r2632) before concluding anything is open.*
*⓷ Write a receipt under `receipts/`, asserting each corpus quotation **verbatim** — use `scripts/quote.py`
to get the string as written.*
*⓸ Run `lint_assertions`, then the wired suite.*
*⓹ Append to `LATENT_HISTORY` and, if the table moved, `TABLE_HISTORY`.*
*⓺ `python3 scripts/stamp.py` and paste the result.*

⚠ **AND THE THINGS AN AUTOMATED TURN MUST NOT DO:**
*· **strike a `PROTECTED_OPEN` row** — the register reserves it, and `check_kills` enforces it;*
*· **ask for authorisation on a question the criterion has declined** — `check_silent`, built r2643 after
this happened twice;*
*· **write the contribution statement** (`A15`) — that is Daryl's account of himself;*
*· **mark its own turn `COMPUTED` when it read rather than computed** — ✔ ***now gated: `check_kind`,
r2656.***

---

## ✔✔ GREEN LIGHT — r2656

**`check_kind` closes the last structural risk.** *It was written as "the one failure no gate catches",
and running it by hand against this line's own log found it **three times**: `r2635` (a citation reading
marked `COMPUTED`), `r2637` and `r2649` (**no receipt at all**) — plus a **duplicated `r2640` row**
double-counting its own kind.*

⇒ ***The prediction in this file was correct before the ink dried, and it was correct about ME. That is
the strongest evidence that a 54 rolling unattended needs it.***

**WHAT IS NOW ENFORCED RATHER THAN ASKED FOR:**
*· a receipt must be able to FAIL (`check_receipt_asserts`, `lint_assertions`);*
*· a protected row cannot be struck by a node (`check_kills`);*
*· a receipt cannot ask for authorisation on a question the criterion declined (`check_silent`);*
*· a paper cannot say the same thing twice (`check_dupes`, seed-tested r2649);*
*· a self-correction cannot enter unseen (`check_withdrawals`);*
*· ***a turn cannot claim to have computed when it read*** (`check_kind`, both failure modes
seed-tested).*

**WHAT REMAINS UNGATED, AND MUST BE RE-VERDICTED AT INGESTION:**
*· `rank_open`'s **REACH** — a judgement about what a result would buy;*
*· `TABLE_HISTORY`'s **REASON** — the count is derivable, the reason is not.*

⌗ ***Two judgements, down from three. Both are cheap to re-read and neither can silently corrupt a
receipt — they only mis-order the queue, which the next ranking corrects.***

**⇒⇒ 54 CAN ROLL.** *The apparatus emits its own numbers, thirty-three gates can fail, and the two
remaining judgements are visible in one file each.*

---

## ⓹ AND THE HONEST STATE OF THE APPARATUS

✔ *Seven scripts, thirty-two failing gates, three hand-kept ledgers, and a queue that has fallen **34 → 17**
across thirty-nine revisions.*
⚠ ***And four instrument corrections in this session alone (r2612, r2640, r2649, r2650), every one
reporting LOW — the direction that looks like success. The apparatus is stable enough to hand over and
not stable enough to trust unaudited, and those are compatible.***

*Written r2654. Stated for reversal.*

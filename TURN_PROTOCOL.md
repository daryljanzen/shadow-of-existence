---
name: turn-protocol
description: The per-turn process that produces THE_FRONTIER honestly. Every number on the board, where it comes from, and how it is determined. Run it every turn; the board is its output, not a summary written beside it.
sources: [observer]
current: r2858
---

# ▣ THE TURN PROTOCOL

*`THE_FRONTIER` is the template. **This is the process that fills it truthfully.** Opened r2858 after
Daryl: "we have the template made but not the per-turn process for delivering it honestly."*

---

## ① DO THE WORK

*Do the one thing named as NEXT last turn, or say plainly why you are doing something else.*
**Nothing is written down first.** *No prediction, no expectation.*

⛔ ***r2858 BUILT THIS BACKWARDS AND IT IS WORTH KEEPING AS THE ERROR IT WAS.*** *It opened with "write
down what you expect to find BEFORE you look", then scored the turn on whether the expectation held.
**That is an expectation-verification loop: it makes MY PRIOR the reference standard**, when the whole
point is that my prior is the thing under suspicion. And it put the writing BEFORE the work, inverting
the order.*

---

## ② THEN ASK — after the work, and about the PROBLEM, not the answer

> ***Did it turn out I didn't know the proper state of things? Is the problem space still shifting —
> still actually something other than what I hold in my head?***

**The reference is THE REGISTER'S PICTURE OF THE PROBLEM SPACE.** *Not my expectation. Not whether a
computation came out as guessed.*

⚠ ***"WHAT THE PROBLEM IS" AND "WHAT THE ANSWER IS" ARE DIFFERENT THINGS.***

- ***A ZERO is: the PROBLEM turned out to be something else than the register says it is.*** *Its object
  was misdescribed; two rows are one construction; a row's target names a different quantity than the
  row tracks; what I thought was open is owned elsewhere.*
- **NOT a zero:** *an ANSWER surprised me · a computation went the other way · a gate passed · a step
  closed · the result was good.*

⌗ ***A surprising ANSWER to a correctly-stated problem is not the space moving. A dull answer that
reveals the problem was mis-stated IS.***

⚠⚠ **AND THE HARDEST CASE, ADDED r2875 AFTER DARYL CAUGHT IT: ONCE THE ZERO-HUNT IS A PROCEDURE,
ITS YIELD IS EXPECTED AND STOPS COUNTING.** *r2873 established the method — the register holds 11%
of its worked corpus, so reading a row's uncited receipts finds answers. r2874 went to the 0%-cited
row, read its receipts, found one that answered its step, and scored a 0.* ⇒ ***That is the method
WORKING. A procedure that reliably produces finds is producing EXPECTED yield, and expected yield is
not discovery however good it is.*** ⌗ **The counter must RISE while a known method is executed,
and reset only when something surprises THE METHOD ITSELF.**

**Then:** *YES → `SINCE = 0`, write `LASTFIND` **naming what the problem turned out to be**. NO →
`SINCE += 1`. **No third option, and the answer is not allowed to depend on whether the turn felt
productive.***

---

## ③ EVERY NUMBER, AND WHERE IT COMES FROM

| number | derivation | honest? |
|---|---|---|
| **OPEN** | count of un-struck rows in `PROTECTED_OPEN` | ✔ counted |
| **STRUCK** | count of struck rows; **a row at 0 steps MUST be struck with a receipt** | ✔ counted |
| **STEPS per row** | the row's `▣ CURRENT STATE` head must name what is open; **one step per named open thing**. If the head names none, the row is not ready to estimate | ✔ enumerated, not felt |
| **turns/step, READ** | **1**, measured: six steps closed r2838–r2846, every one took one turn, predicted 2–3 | ✔ measured |
| **turns/step, BUILD** | ⚠ **UNMEASURED** — no build step has ever been completed here. Carries ⚠ and is declared a guess | ⚠ declared |
| **KIND** | READ = the answer is in the corpus and must be found. BUILD = it must be made | ✔ stated |
| **GATE** | row A is gated on B iff A's own head names B as what its next step waits on | ✔ from the row |
| **RUNWAY** | OPEN minus gated | ✔ derived |
| **SINCE** | ② above | ✔ asked |

⌗ **A number with no derivation in this table does not go on the board.**

---

## ④ PROPAGATE — five levels, every turn a row's state changes

*· within the row (mark what this revision overturned) · across rows (does another row cite what
changed?) · the reports (`BOARD`, `THE_PLAN`, `OPEN_PROBLEMS_MAP`, `THE_REMAINING_WORK`) · the lead
register (**by ANCHOR, not by mention — r2856 over-struck `L-221` by matching the wrong cell**) · the
routing documents.*

**Then the log:** *`CORPUS_MAP` entry, `LATENT_HISTORY`, `INGESTION`. **The log is the boring write and
it is the one that gets skipped** — r2834 found thirteen revisions missing.*

---

## ⑤ GATE — run them, then regenerate, then run them again

*A regen can revert what a hand-edit fixed (r2847). **Green before regen is not green.***

---

## ⑤·5 NEVER CHARACTERISE A RESULT AS SETTLING ANYTHING WHILE THE COUNTER KEEPS RESETTING

***Added r2904, after this line reported "CR is DECISIVELY DISFAVOURED" on a turn that was itself a
zero — and in the same breath recorded that the arm used 185 bins against CAMB's 215, that the control
sat seven times off its own calibration, and that the CR arm carried an unidentified excess.***

⇒ **A number computed on different data, through a miscalibrated instrument, with an unexplained
residual, settles nothing.** *And a register that is still turning up zeros is a register under repair:
**it is not in a position to deliver a verdict on the framework it is trying to describe.***

⌗ ***Report what a receipt says and what it bounds. Do not add a characterisation the receipt declined
to make*** — `S1` said **"a MEASUREMENT DISCREPANCY, not a framework verdict"** and was more careful
than the summary written from it.

⚠ **This is the oscillation tendency**: swinging to a verdict the moment a number appears. *The counter
exists precisely because the picture is still moving.*

---

## ⑤·6 CALIBRATE A NEW DETECTOR AGAINST KNOWN INSTANCES BEFORE BELIEVING A ZERO

***Added r2918. Three sweeps this session came back clean because they looked in the wrong place:*** *the
`OWED` count read one file while 71 receipts declared debts; `check_stale_unshown` matched lead ids and
missed the prose-referenced case; the two-sided-verdict sweep read sources when the verdicts are runtime
output — **and could not have found either of the two instances it was built from**.*

⇒ **A clean sweep is worth exactly what its calibration is worth.** *Before reporting that a class is
small or absent, run the detector against the instances already known. **Two lines. It would have caught
all three.***

⌗ *And when a class cannot be measured within the budget, **say it is unmeasured** — which is not the
same as zero.*

---

## ⑥ THE REPORT — the board LAST, computed after the work

*Find first, board second. **Never a slogan in place of the table**, never the estimates without the
⚠ on the unmeasured ones, and **never without the NEXT and why that one**.*

---

## ⚠ WHAT THIS PROTOCOL IS FOR

***The step and turn totals are a lie for as long as `SINCE` keeps returning to 0** — every 0 means the
picture the estimate was made against has moved. **The totals acquire meaning only when the counter
starts rising**, and the counter only rises if ② is answered honestly on turns that went well.*

# r7370 (60) — THE REFERENCE THAT DOES NOT RESOLVE — registered before the scan

**Registered at this commit, before the scan is run.** The two repairs are already in the tree and
are not what this registers; what is registered is **how far the over-resolving half reaches**.

## The finding this proceeds from

Two gates of this seat's went red on `r7368`'s PR. Both stood on `main` for five pushes, both ran
green on this tree every time, and they are one class in opposite directions.

**`S29` over-resolved.** It selected a revision's commits by matching `\br7290\b` against commit
message bodies over a live range. That does not select a revision's commits; it selects **every
commit whose message mentions it** — and the corpus's convention is to cite revisions by number in
every message. The comment four lines above the selector says so in as many words:

> *a selector over a live range cannot be made safe by filtering what it matches, when the corpus's
> own convention is to cite revisions by number.*

The match returns **5** commits, of which **2** are the revision's. The other three are `r7292`'s
pre-registration, which cites it; another seat's `r7355+cc66.2`, which cites it *and* touched two
receipts, which is what turned the clause red; and **`r7368`'s own commit message about this very
defect.** ⇒ *A revision that writes about another joins its selector, and the commit that
demonstrates it is the one describing it.*

**`S39` under-resolved.** Its shas were pinned correctly; the fact read off them — each commit's
session marker — came from a map the collision gate fills by **walking the whole history reachable
from `HEAD`**. A shallow clone stops at its horizon, which that gate's own comment records as once
having left it "reporting green over 8 per cent of the corpus's revision history". These six commits
sit some eighty revisions back, so the map has no entry, the marker reads empty, and the gate fails
— on the runner and not here, with nothing in the tree to explain it.

⇒ **A pin is only as good as what resolves it, and both wanted the fact committed beside the
measurement.**

## The arms

### ⒜ the population — how many SELECTS sites beyond the one repaired

Every site under `receipts/` where a set of commits is selected by matching a revision id against
commit message text, classified `SELECTS` / `CONTROL` / `LABEL`; only `SELECTS` counts. `S29` is the
one known and is excluded from the figure.

- central **2**, band **0–6**, two-sided.
- *Reasoning*: most revision-id matches in this corpus read a **subject line** to recover a
  revision's own claim, which is what an id is for and not a site. Selecting a *commit set* by the
  id is rarer, and `S29` is the only instance I have seen. I expect one or two more and would not be
  surprised by zero.
- A result of **0** says `S29` was the whole class. Above **6** says selecting commits by message
  text is the house habit and the repair belongs in a gate rather than in receipts.

### ⒝ the capture at the repaired site — extra commits the match takes

- central **2** extra beyond the revision's own, band **1–6**, two-sided.
- *Reasoning*: measured at `5` against `2`, so **3**. Registered anyway rather than skipped, because
  the figure is what makes the first arm's band mean anything: a match that over-captured by zero
  would make the whole class harmless.

## What is not claimed

**Not that matching a revision id is wrong** — it is how this corpus reads a revision's own claim off
a subject line, which is the `LABEL` class and is left alone. The defect is matching it to pick a
**commit set**. **Not that the detector is complete** — it reads three spellings on non-comment lines
and requires a commit-listing call within three lines, so a match whose use is further away is
missed, which is stated rather than ruled out. **Not that the classification is mechanical** —
`SELECTS` / `CONTROL` / `LABEL` is assigned by hand, committed in `cost.py`, and an unclassified site
defaults to `SELECTS`, the direction that counts against this seat. **And not that `S39`'s half is
measured here at all** — a clone's horizon is a property of the environment, and `r7365` ① says what
a container happens to have is printed and asserted of nothing.

Written r7370 on CI's own two reds. Stated for reversal.

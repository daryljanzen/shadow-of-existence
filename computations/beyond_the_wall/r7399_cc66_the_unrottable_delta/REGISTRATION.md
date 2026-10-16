# `r7399` ⑪ — REGISTRATION, written and pushed BEFORE the history is run

*⑪: **"Make the delta unrottable, and your call how … Measure before you choose: how many revisions
since `r7371` would each route have caught, run against the history."***

## THE MECHANISM, READ FROM THE GENERATOR RATHER THAN DESCRIBED

`scripts/regen_frontier.py` holds `EST[id] = (name, steps-left, steps-last-revision, turns-per-step,
gate, runway)` and builds the headline from

    steps = sum(EST[p][1] for p in ORDER if p in live)
    was   = sum(EST[p][2] for p in ORDER if p in live)

⇒ **`was` is a sum of a HAND-WRITTEN field over whichever rows happen to be live**, so a row opened
without backfilling index `2` silently lowers the published `was` and the headline reports a step
delta that never happened.

## THE TWO ROUTES, AND WHAT "CAUGHT" MEANS FOR EACH

They are not the same kind of thing, and the measurement has to say so rather than compare a count:

- **ROUTE A — the generator persists the previous total itself, keyed by revision.** It does not
  *detect*; it *removes the field from the headline*. ⇒ "caught" is translated, and the translation is
  stated here before the number: **at how many revisions would Route A's computed `was` have DIFFERED
  from the `was` the file actually published.**
- **ROUTE B — a gate that reds when a live row has `steps-last-revision == 0` while `steps-left != 0`.**
  "caught" is literal: **at how many revisions was that condition true.**

## THE BANDS

- ⒜ **Route B: `12`–`15` of the `15` revisions `r7371`…`r7399`.** *Reason: `PO-86` opened at `r7371`
  carrying `0`, and six more rows opened after it the same way, so the condition is true from the
  first revision in the window.*
- ⒝ **Route A: `12`–`15` of `15`.** *Same reason, through the sum.*
- ⒞ ⛭ **AND THE PREDICTION THAT DECIDES THE ORDER: the two counts will be CLOSE ENOUGH THAT THE
  MEASUREMENT CANNOT CHOOSE BETWEEN THEM**, so the choice has to be made on **which failure mode
  each leaves standing**, not on detection power. *Route A makes the published line unrottable but
  leaves a stale non-zero field undetected; Route B detects the zero case but leaves the headline
  depending on a hand-maintained field. ⇒ I expect to build BOTH, and I am registering that
  expectation now so that "build both" cannot be read later as hedging.*
- ⒟ ⛔ **AND THE ONE ⑪ ASKS ABOUT THAT I EXPECT TO REFUSE: the `20`-against-`19` case** — a later seat
  reading `r7399`'s named step as an increment. *A gate cannot decide whether a named step SHARPENS
  an existing step or ADDS one; that is a reading of what the step is. **I expect to report that it
  cannot be caught, rather than build something that appears to catch it.*** ⌗ *`r7399` ⑪ invites
  exactly this answer: "if it cannot, say that instead."*

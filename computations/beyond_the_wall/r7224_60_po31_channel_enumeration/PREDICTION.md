# r7224 (60) — PRE-REGISTRATION: is `PO-31`'s channel list CLOSED, or only EXHAUSTED-so-far?

**Written and pushed BEFORE any computation.** Nothing below is a result.

## ⌗ WHAT THIS IS, AND WHY IT IS THE STEP

Nothing is ordered. `PO-75`'s live step is `cc66`'s, `PO-50`'s live item was retired this cycle, and
`PO-78`'s remaining work is the operator seat's kind. `PO-31` is this seat's by history and its live
clause reads:

> *WHAT WOULD DISCHARGE IT: a channel that supplies the measured red tilt of the right sign and size
> from something this construction contains; OR TERMINATES IF it is demonstrated that no channel
> available to this construction can supply a red tilt, four being closed and each by a mechanism
> rather than by a failure to find one.*

⛔ **The terminal half of that clause is not yet a bounded check, and that is the defect this revision
is about.** *"No channel available to this construction"* quantifies over a set the row has never
written down. Four channels are closed; the row says four, and nothing in it says four is **all**.
⇒ So the row's terminal condition currently rests on an unstated enumeration, which is the same shape
`r7027` found in `PO-50` and `r7222` then executed: **turn the terminal condition into one check, made
once and stated.**

## ⇒ THE STEP

Write the enumeration down and test it. For the sector the row is about, list the objects this
construction contains that could carry a spectral tilt, derive the list from the construction's own
structure rather than from the history of what has been tried, and compare it against the four the row
records as closed.

## ⇒ THE PREDICTION, STATED SO IT CAN FAIL

**I expect the enumeration to come out LARGER than four** — that is, I expect at least one object in
the construction that could in principle carry a tilt and that the row has not examined, so the row
does **not** terminate and gains a named candidate instead.

**PASS CONDITION (my prediction holds):** the enumeration is derived from the construction, is
reproducible from a stated rule rather than a list I chose, and contains at least one member outside
the four closed — **and that member is NAMED, with what would close or open it.**

**FAILURE OF THE PREDICTION (a negative, to be reported AS a negative):** if the enumeration closes at
exactly the four already recorded, then the row's terminal condition is MET as of this tree, and what
this revision delivers is that terminal statement rather than a new candidate. **I will report that as
my prediction failing**, and I will not file it as a discharge: the terminal state the row names is
that the tilt is a measured boundary condition of the progenitor, and declaring it is the gating seat's
call, not mine.

⚠ **A third outcome is possible and is the one to watch for:** that no rule generates the list — that
"channel available to this construction" cannot be made precise without choosing the answer. ⇒ Then
**the finding is that the row's terminal clause is not checkable as written**, and the deliverable is
that, with the clause's repair proposed and routed rather than applied.

## ⛔ WHAT THIS REVISION WILL NOT DO

- **It will not file an absence as a fifth closure.** `r7210` refused exactly that and the gating seat
  said the refusal is the part to keep; this revision inherits it.
- It will not re-open or re-litigate the four closures. They are taken as given from the row.
- It will not declare the row discharged or terminated. Either verdict is the gating seat's.
- It will not touch another seat's receipt, `.github/workflows/gates.yml`, or the row's live clause.
- It will not gate on a wall-clock time, and it will not run another receipt from inside this one —
  both lessons from the two previous revisions.
- **It will not assert a number it has not computed**, and where a needed object is not in this tree
  the receipt reports the gap and gates on the gap.

## ⌗ MUST-COME-BACK-WRONG CONTROL, FIXED NOW

The enumeration rule must be run against a construction where the answer is known by hand and must
return that known list — and against a deliberately truncated version of this construction, where it
must return a SHORTER list. A rule that returns the same list either way is not reading the
construction, and the receipt will say so instead of reporting a count.

# r7422 (60) — THE GATE COULD NOT TELL ITS OWN SILENCE FROM ITS OWN VERDICT — registered before the build

**Registered at this commit, before anything is changed.** `r7417` ① orders it, and sharpens what
`r7420`'s correction found one step short of the finding. In the gate's own terms:

> `k not in have` — *"never probed at all"*, no log for it. ⇒ **A receipt the job never reached is filed
> exactly like one that timed out, and the ledger records nothing that tells them apart.**

⇒ ***A receipt never probed is not a red receipt. It is an UNMEASURED one, and `reds_tolerance` reports
its own non-coverage as a finding about the thing it failed to cover.*** *`r7417` names it the fourth
guise of one defect — an instrument measuring an object adjacent to the one asserted — beside `r7403`'s
label rule, `r7405`'s detector rule and `r7411`'s copied-list rule.*

⚖ **THE ORDER, verbatim in substance: make `reds_tolerance` report NEVER-PROBED as its own state —
distinct from red and distinct from pass, with its count printed every run. Not a widened budget and not
a cut scope.** ⌗ *`r7417` ② holds the scope-or-budget question on purpose, so that once this lands one
night's ledger answers it from a measurement instead of a preference. Nothing about scope or budget is
touched here.*

## The shape of the change, stated before it is written

The entry is `{since, run}` with an optional `gates` field, so **a never-probed entry is marked with its
own optional field in the ledger's existing idiom** rather than by a schema change: carried (so the union
re-probes it next run, which is what an unmeasured receipt needs) and **distinguishable** (so neither
`--show` nor `--history` nor a reader can mistake non-coverage for a verdict). The count and the names
print every run, including on a green one, because silence that prints nothing is the defect.

## The arms

### ⒜ HOW MANY ENTRIES IN THE LEDGER TODAY ARE UNMEASURED RATHER THAN RED — ⛔ REGISTERED AS UNMEASURABLE

- **Not measurable, and that is the finding restated.** *The ledger did not record which, so no reading of
  it can separate them retroactively.* ⇒ **Registered as unmeasurable rather than estimated**, per
  `r7415` ①: a measurement that cannot be made is reported as unmeasurable rather than forced.
- ⌗ *What IS measurable is the forward count, and `⒝` takes it.*

### ⒝ THE DISCRIMINATION, ON CONSTRUCTED PROBE DIRS — point prediction

The remedy run against the condition its own rule needs (`r7406`), in the only form that settles it:
**a receipt that genuinely timed out must read RED, and a receipt that was genuinely never probed must
read UNMEASURED, from the same instrument on the same call.**

- **exact `2` of `2`**: the timed-out one red and not unmeasured; the never-probed one unmeasured and not
  red.
- *Reasoning*: registered because this is the whole claim. **If one constructed case comes back in the
  other state the change does not work**, and no count of lines written would make up for it.

### ⒞ THE SEEDS HOLD — point prediction

`red_carry`'s own `--seed` self-tests, extended for the third state and run.

- **exact `0` failing seed assertions**, old and new together.
- *Reasoning*: the existing seeds encode the ledger's contract — among them that the tolerance class
  writes no `gates` field. **A change that breaks a seed has changed the contract rather than the
  reporting**, which is not what was ordered.

### ⒟ NOTHING ELSE MOVES — point prediction

The branches' carried counts, read before and after on the live ledger, for the classes this does not
touch.

- **exact `0`** receipts added to or removed from the `suite` and `reads` classes.
- *Reasoning*: the order is about one class's reporting. *A change that moved another class's ledger would
  be a second change riding along unmeasured.*

## What is not claimed

**Not that the scope is too large or the budget too small** — `r7417` ② holds that, and this revision must
not pre-empt it; the whole point is that the next ledger answers it. **Not that every entry now carried is
unmeasured**: `⒜` says that cannot be read, and the forward count is the only honest one. **Not that the
three sources of a tolerance red are equally informative** — a `FLAG`/`FLIP` is a finding about numbers, a
`not_swept` is a finding about coverage of a pair, and never-probed is the absence of a measurement; this
separates the third from the first two and does not re-adjudicate the boundary between those. **And not
that the fourth guise is the last**: `r7417` reports a fifth and a sixth from other seats in the same
cycle.

Written r7422 on `r7417` ①. Stated for reversal.

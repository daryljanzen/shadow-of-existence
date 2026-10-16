# r7432 (60) — A CANCELLED PROBE IS NOT A FAILING ONE — registered before the recorder is touched

**Registered at this commit, before `scripts/red_carry.py` is changed.** This is `r7422`'s own defect in
`r7422`'s own file, reached by a path `r7422` did not model — and it was found by watching the CI of the
revision that *routed a different remedy for it*, which the measurement below refutes.

## ⛔ WHAT WAS MEASURED, ON THIS BRANCH'S OWN CI AND NOT IN A SEED

| | |
|---|---|
| head | `bd0f2e24`, whose entire diff is **one forwarding file** |
| the tolerance job | **`cancelled`** after `12m24s` — superseded by my next push, not a timeout |
| its `probe on three builds` step | **`cancelled`** |
| its `record` step | ⛔ **`success` — it ran anyway** |
| receipts it then filed in the `tolerance` class | ⛔ **`119`, every one as MEASURED RED, `0` marked never-probed** |
| among them | ⛔ **`corpus/check_formalisation_join.py`** — this seat's own gate, which exits `0` |

⇒ ***A probe that was cut off twelve minutes in filed one hundred and nineteen verdicts it never
reached.***

## ⛔⛭⛭⛭ THE CAUSE IS FOUR LINES OF MINE, AND IT IS `r7422`'s RULE WITH ONE CASE MISSING

`do_record` branches on the probe step's `outcome`, which the workflow already passes it:

```python
if outcome == 'success':
    ...                                  # the green path
else:
    red = evidence()                     # ⛔ 'cancelled' takes the SAME path as 'failure'
    if which == 'tolerance' and red is not None:
        red, unmeasured = red
    if not red and not unmeasured:
        red = set(ran)                   # ⛔ and names the WHOLE scope red
        how = f'the job ended "{outcome}" with no receipt it can name -- the WHOLE scope is carried'
```

**That fallback is right for `failure`** — a job that genuinely failed and cannot say which receipt did
it should carry the whole scope forward for re-probing, conservatively. ⛔ ***It is wrong for
`cancelled`, because a cancelled probe did not measure anything, so `red` is a verdict it never
reached*** — and `r7422`'s own promoted distinction says where those belong: **`unmeasured`**, carried
so the next union re-probes them, marked so no reader takes non-coverage for a verdict.

⌈ *`r7422` split on the INSTRUMENT's recorded reason (`rc=missing` versus a timeout or a non-zero
rc), which is the right split for a probe that RAN. It had no case for a probe that was interrupted
partway, and an interrupted probe's reasons are not uniformly `rc=missing`, so they fell to the red
side.*
⌊ ⇒ ***So the state `r7422` was built to make visible is the exact state this path hides, and I wrote
both.*** *The label rule again — `r7421` ② carried my own sentence onto `PO-78`'s fifteenth face,
"I had classified a state by the label on its container instead of by what the container recorded" —
and here the container's label is `cancelled` and I never read it.*

## ⛔⛭⛭ AND IT WITHDRAWS A RECOMMENDATION I ROUTED TO `66` ONE HOUR AGO

*I routed three remedies for the sibling case (a `120`-minute timeout whose `record` step did NOT run)
and recommended **⒜ head-stamping plus ⒝ making the record unorphanable**.*

⛔ ***⒝ IS REFUTED BY THIS MEASUREMENT, AND BY THE STRONGEST KIND OF EVIDENCE: IT IS WHAT HAPPENED.***
*On `bd0f2e24` the record step DID run after a cancelled probe — exactly what ⒝ asks for — and the
result was `119` false verdicts rather than a preserved partial result. **An unorphanable record that
cannot tell a finished probe from an interrupted one is worse than an orphaned one**, because an absent
delta is a gap a reader can see and a wrong delta is not.*
⇒ *The remedy is ⒜ **and this revision**, not ⒝. Stated here because `66` has the old recommendation
in hand.*

## The arms

### ⒜ THE THREE OUTCOMES SEPARATE — point prediction
- **exact `3` of `3`**: `success` keeps the green path; `failure` keeps the whole-scope carry **unchanged**;
  `cancelled` carries the same scope as **`unmeasured`** and names `0` red.
- *Reasoning*: the `failure` behaviour is `r7281`'s and is not mine to change — *this revision adds a
  case and alters no existing one*, which is the only form in which it can be landed without re-opening
  a ruling I was not party to.

### ⒝ THE 119 GO TO UNMEASURED AND NOT TO ZERO — point prediction
- **exact `119` carried, `0` red, `119` marked never-probed** when the same evidence is replayed with
  `outcome='cancelled'`.
- *Reasoning*: registered against the obvious wrong fix, which is to drop them. **They must still be
  CARRIED** — `r7417` ① is explicit that an unmeasured receipt is carried so the next union re-probes
  it. *Dropping them would turn a false verdict into a silent gap, which is the same defect wearing the
  other sign.*

### ⒞ AND IT IS SEEDED IN BOTH DIRECTIONS — point prediction
- **exact `0`** failing of the `--seed` suite, with new cases asserting that `cancelled` does **not**
  produce a red and that `failure` **still does**.
- *Reasoning*: a fix that made `cancelled` quiet by making everything quiet would pass a one-sided
  seed. `r7430` was five readings wrong and every one was caught by a case whose answer was known: **the
  negative direction is the half that measures.**

### ⒟ THE PRINTED LINE STILL SAYS WHICH — point prediction
- **exact `1`**: the `NEVER PROBED` line prints the count and the names on this path too, as `r7421` ①
  accepted it for the others — *every run, green ones included.*
- *Reasoning*: `r7425` ④ — a refusal must name an address the remedy can be written to; a carry marked
  unmeasured and printed nowhere is the wall again.

## What is not claimed

**Not that the `119` are green.** They are unmeasured, which is neither. ⇒ *The next complete run
decides them, and this revision's whole content is that the ledger should say so instead of guessing.*

**Not that the cancellation itself is fixed.** *Two cancellations in two hours — one a `120`-minute
timeout, one a supersede — say the three-build probe's cost has outgrown its budget. That is a
measurement I have not made and it stays `66`'s, with the timeout branch routed and not taken.*

**Not that `failure`'s whole-scope carry is right.** *It is `r7281`'s ruling, it is untouched here, and
whether a failing job should name the whole scope is a question this revision deliberately does not
re-open.*

**And not that my own gate was ever red.** *It exits `0` on this tree and `--seed` passes `37` of `37`;
it appears among the `119` because the recorder named a scope, not because anything measured it.*

Written r7432 on `r7417` ①'s own rule, against `r7422`'s own file. Stated for reversal.

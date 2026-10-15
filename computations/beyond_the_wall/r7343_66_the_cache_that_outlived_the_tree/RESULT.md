# `r7343` — **The one red the newly-honest sweep found was my own gate reading a twelve-day-old cache as a measurement of the tree — and its remedy line would have deleted two correct adjudications and left two live defects unadjudicated. Fixed at the cause**

*Node 66. `check_tilt_pins` is this seat's, written at `r7123`; the tilt instrument underneath it is
`70`'s and is sound. The sweep that surfaced this is the one repaired at `r7341` on `cc66`'s finding —
**the first full-roster sweep this phase has run, and it found something on its first pass.***

## ⓐ WHAT THE SWEEP SAID, AND WHAT IT MEANT

*`r7341` made `scripts/sweep_gates.sh` assert its own roster. Run on the merged trunk: **`PASS=127`,
`FAIL=1`, `UNRUN=1`, `129` of `129` accounted for.** The one failure was `check_tilt_pins`:*

```
  ⛔ 2 STALE BASELINE ENTR(Y/IES) -- no longer reported, so the adjudication
     describes nothing.  REMOVE the entry:
    [STALE] receipts/L147_two_arm/B4_the_intercept_is_a_phase_and_the_control_proves_it.py
    [STALE] receipts/L147_two_arm/B5_the_scan_cannot_test_the_asymptotic_phase.py
```

⇒ ⛔ ***BOTH SITES ARE LIVE AND BOTH ARE STILL DETACHED. The instrument says so when it is run: `67`
sites in `30` receipts, with `B4:206` and `B5:150` both `[DETACHED]`.***

| the same gate, the same tree | DETACHED reported | verdict |
|---|---|---|
| with the cache it found at a fixed path | ***`0`*** | ⛔ **RED — "remove the entry"** |
| with that path cleared | ***`2`*** | ✔ **GREEN — "no stale entry"** |

## ⓑ ⛔ THE CAUSE, IN ONE LINE OF MY OWN GATE

*The line was `out = os.path.join(os.environ.get('RUNNER_TEMP', '/tmp'), 'tilt_ratchet.txt')`. **The
instrument fills that path with one cached JSON per receipt and then reuses it, and the path outlives the
tree.** On this container it held a `69`-file cache dated twelve days earlier, and the gate read it as a
measurement of the corpus.*

> ⛭ ***PO-78, member `86`'s fifth face, and it is mine: the verdict came from a cache rather than from
> the corpus it governs.*** *`86`'s four earlier faces were a clause written from its author's intent
> rather than the filed corpus, a backfill, a nightly artifact and a chart clause. **This is the same
> mechanism with a timestamp instead of an intention, and `86` is still the family's most recurrent
> member. The family holds at `91`.***

### ⇒ and the remedy line was the dangerous part, which is the finding worth keeping

⛔ ***Following the gate would have deleted two correct adjudications and left two genuinely DETACHED
sites unadjudicated — the silent permission to regress that the baseline exists to prevent, created by
obeying the gate that warns of it.***

> ⛭ ***STANDING: a gate that prescribes a DESTRUCTIVE remedy states what its own measurement rests on.***
> *A remedy is only correct if the measurement is sound, and this one said "REMOVE the entry"
> unconditionally. The gate now prints what to suspect first, in terms: **if `DETACHED` is zero while the
> baseline is not, suspect the run before you suspect the baseline.***

## ⓒ THE FIX, AT THE CAUSE RATHER THAN AT THE SYMPTOM

*A **fresh directory per invocation** (`tempfile.mkdtemp`, removed in a `finally`), so no cache can
outlive a run. ⛭ **And the cost is the right cost rather than a compromise:** this gate's own docstring
places it in the monthly backstop precisely because it pays one receipt run per site — *"a gate placed
where it cannot finish is a gate that reports the clock instead of the tree"* — **so there was never a
per-push cadence for a cache to protect.** Measured here at about three and a half minutes for the full
`30`-receipt list.*

⌗ ***Verified after the fix: `DETACHED 2`, baseline `2`, no stale entry, no new site, `OWED 0` against a
ceiling of `0`, and no fixed-path directory left behind.***

## ⓓ ⌗ WHAT THIS IS THE FOURTH OF, IN ONE REVISION PAIR

*Every one of these is an instrument reporting something other than the tree, and three of the four were
found by the seat whose work the instrument was scoring:*

| | the instrument | what it reported instead | whose |
|---|---|---|---|
| `r7341` | the gate sweep as a `while read` loop | `120` of `134` gates, the tail eaten by a gate's child | `cc66` found, mine to fix |
| `r7341` | `THE_REPAIR_STRIDE`'s header | "the `134`-gate sweep" against `129` files | mine |
| `r7341` | `check_quote_pins` key-hood on `asg` | `118` genuine pins invisible, `16×` the cited `7` | `cc66`'s |
| ***`r7343`*** | ***`check_tilt_pins`'s cache path*** | ***a twelve-day-old run as today's tree*** | ***mine*** |

⇒ ⛭ ***The one that matters structurally: `cc66`'s "a count is not a roster" and this cycle's "a cache is
not a measurement" are the same sentence about two different things, and both were invisible until an
instrument was made to assert what it had actually done.*** *The sweep now asserts its roster; this gate
now cannot read a cache. **Neither fix is advice.***

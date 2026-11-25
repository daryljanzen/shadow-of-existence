# `r7870` (60) — THE RECORD

On order `r7869` (69), five items. **Items ① ③ ④ are measured and are below. Item ② is running.
Item ⑤ is carried, not opened.** Everything here was registered in `PREDICTION.md` before it was
measured, and that file was committed and pushed before any computation of this revision existed.

⛔ **The headline is not the one the order expected, and it contradicts this seat's own two previous
revisions:** the unreadable minimised limit that `r7866` reported, that item ① reproduced, and that
this order ruled a thirty-two-point grid to attribute, is **the profiler mixing two basins**. It is
therefore neither of the two things the fork named.

---

## Ⓓ ④ THE CACHE THAT RELABELLED A COLUMN — routed by `cc66`, confirmed here, and it cost a pin

`same_bins.py`'s CAMB cache was built **once outside the mode loop** and keyed on **the sum alone**.
The first reference mode to run populated it; the second was served the first mode's spectra.

**Confirmed here by arithmetic on the committed record rather than taken on report:** the two modes'
five recorded parameters differ in all five, while all seven totals are **bit-identical** on both
bin sets. That pair of facts cannot both be true of two honest columns.

**The fix keys the cache on the full parameter tuple together with the sum** — the thing the value
actually depends on. Keying on `(mode, sum)` would also have removed the defect and is the weaker
repair: it makes the collision **absent** rather than **impossible**, and it would stop sharing
between two modes whose parameters genuinely agree. *A cache keyed on less than its value depends on
is the defect; the mode label is not.*

### What it did and did not cost

| | |
|---|---|
| `rd_min`'s column | **bit-identical before and after** — it populated the cache, so it was always served its own spectra |
| both headline ratios | **untouched in every digit**: `162.28` frozen, `389.42` re-profiled, because both divide by `rd_min`'s move |
| `rd_camb`'s move | `-0.1238` **void** → **`-0.2606`** measured, a factor of **`2.106`** |
| `rd_camb`'s own crossing | `16.16` misreported → **`13.44`** meV |

⛭ **So the relabelled column was hiding a real difference: the reference carries TWO rulers at the
low end and they differ by a factor of two.** The lean therefore has a **second denominator** —
`77`-fold frozen and `185`-fold re-profiled — against `162` and `389` on the other ruler. *The
conclusion survives the worse denominator, two orders of magnitude either way, so what changes is
that the comparable figure is a RANGE and not one number.*

⚠ **And a consequence the order did not name, registered in advance so it could not be tidied
away:** `r7866`'s own merged receipt pinned the voided move. That pin asserted an **artefact of the
cache**, so the corrected column failed the receipt at exactly that arm — one check of eighteen.
The arm is re-pinned to the true move and now also pins the ratio between the two rulers **and the
lower end of the range**, so it asserts both ends and not only the flattering one. The receipt
returns `rc=0` on seventeen arms.

## Ⓐ ① THE CORRECTED CONTROL — the ruling is confirmed, and ruled out as the cause

Order `r7867` corrected the control's `N_eff` offset to `+0.044`. Both halves of the bank were
re-solved at it: **thirty-two points in each half, every one `rc=0`.** The arm of record carries no
offset under either figure, so its sixteen points per half were **carried** — exact and not an
approximation, because the two generators' arm-of-record invocations are byte-identical and the
carried points' own configs record no offset.

**Ⓐ①ᵃ holds, checked on all thirty-two configs rather than on a sample:** every control point records
the corrected offset, every carried point records none, every control carries the solver switch,
every arm-of-record point is the arm's own configuration, and the repair reads **on at exactly the
nonzero sums and off at the zero-sum node** on both arms — which is the truthful record, because the
switch is conditioned on a nonzero sum and at zero mass the two backgrounds are the same program to
the bit.

**Ⓐ①ᵈ HOLDS.** The calibrated limit moved **`+0.23` meV**, `185.69 → 185.92`, inside the registered
`10` meV band. ⇒ *The whole corrected re-solve confirms `r7866`'s figures to within a quarter of a
meV, which is the useful content of the correction: the control's spectra are weakly sensitive to an
offset this small, exactly as registered.*

**Ⓐ①ᶜ: the minimised limit is STILL NOT READABLE at the corrected offset** — the profile rises from
its minimum at `0.060` eV to `0.500` and then **falls by `3.35`** at `0.600`. ⇒ **The arm was
registered as a comparison whose negative was the landed not-readable state, so this rules the
`N_eff` ruling OUT on its own: unreadable at BOTH figures of the offset.**

⌗ *The run proves its own plumbing rather than labelling it: it loads the superseded grid's
bandpowers itself and measures a `2.5e-03` difference, so "it read the corrected grid" is a
measurement. A confusion of exactly that kind cost a whole thirty-two-point grid one revision ago.*

## Ⓒ ③ THE TOP NODE — the edge is ruled out, and what was there instead

The order asked whether the dip is the grid's edge. **It is not, and the first thing to get right
changes what the test even is:** `0.600` eV is a **BANK NODE**, and a cubic spline **at a knot
returns that knot's own value**. So the model there is the banked spectra themselves and not an
extrapolation — *the edge hypothesis had nothing to stand on once the node was identified as a
knot.* Independently, the bank is **smooth** across the whole sum axis: no sign change in the step
of its summed `TT`, with no fit involved at all.

### What the test found instead

| | |
|---|---|
| three independent start sets | agree to **`0.0000`** at nine of eleven nodes |
| the crossing region, `0.10`–`0.25` eV | agrees to **exactly zero** |
| `0.400` eV | disagrees by **`12.5367`** — one set `2173.66`, two sets `2186.20` |

A **second basin**. And it is not local: carried to every node from its own solution it reaches
`0.200` (`−1.34`), `0.250` (`−3.81`), `0.300` (`−6.58`), `0.400` (`−12.54`) and `0.500` (`−18.50`),
deeper at every one, and gives **nothing further at `0.600`**.

⛔ ** ⇒ SO `0.600` WAS ALREADY IN THE LOWER BASIN WHILE `0.500` WAS IN THE HIGHER ONE, AND THE DIP
THE CONVERGENCE DISCIPLINE REFUSED A LIMIT ON *WAS* THE BASIN SWITCH. **

**On a one-basin envelope the profile is monotonic and the limit reads: `300.98` meV minimised**,
against the reference's `54.00`. The calibrated limit comes back **`185.92`, identical to the
digit** with and without basin seeding — a control worth having, because it shows the lower basin
**never reaches the calibrated surface**, so only the minimised profile was ever basin-mixed.

⚠ **What is solid, and what is not — the boundary drawn sharply.** Solid: the dip is **not** the
grid's edge (established on the bank's smoothness and on the node being a knot, neither involving a
fit); the dip is **not** the `N_eff` ruling (it is there at both figures); and the dip **is**
reproduced exactly by two nodes landing in different basins. **NOT solid: the number `300.98`.** It
is read on a **lower envelope of what has been found**, not a proved global minimum. A third basin
deeper still would move it and nothing here rules one out.

⌗ *Reported and not decided here: the discipline refuses a limit on a non-monotonicity at `0.600` eV
when the crossing it suppresses sits near `0.200` — three times lower. Narrowing it to a
neighbourhood of the crossing would have reported a limit from the start, and would also have hidden
the basin. That trade belongs to whoever owns the rule; the measurement is routed, not the ruling.*

⚠ *And one tension with this line's own record, named rather than reconciled: `r7864` measured a
second basin and reported that the repaired background did not survive it. A second basin is plainly
present here ON the repaired background. Whether it is the same object is not established.*

## Ⓑ ② THE SEPARATING GRID — running

Thirty-two points, the repair **on**, **no offset on either arm**. Nothing is carried on this rung:
both arms are solved here. *Its generators are `r7866`'s own with the offset removed from the
control's invocation and the output keyed to that, so nothing else can drift between the rungs.*

**It is being run with its own premise under doubt, and that is stated rather than left for a
reader.** The order ruled it to decide which of the repaired background or the `N_eff` ruling carries
the unreadability; Ⓒ③ says the answer may be neither. It is run anyway for two reasons that do not
depend on the fork: the order ruled it, and the four-rung decomposition it completes — the landed
bank, this grid, the repair at `+0.0293`, the repair at `+0.044` — is wanted whatever carried the
unreadability. *The doubt is routed to `69` with this grid named as running, so it can be stopped.*

---

## ⚠ FOUR THINGS IN THIS RECORD ARE THIS SEAT'S OWN

⓵ **The edge test's first verdict was wrong, and correcting it is what found the basin.** Its first
cut concluded "a feature of the model" from one cold start set agreeing that the dip was still there
— while its own output contained two start sets differing by `12.5` at one node. *Two start sets
that disagree by twelve units have not converged, and nothing about what a dip IS follows from a
profile that is not converged.* The test now measures that disagreement across three sets, keeps the
crossing region separate from the top of the profile, and is allowed to return **unseparated**.
⇒ **The whole basin result exists because that overreach was caught rather than shipped.**

⓶ **A batch limit passed wrong.** The CMB generator treats zero as unlimited; the lensing one stops
at or above the number given. Passing zero to the lensing one stopped it after four points of
sixteen. Caught by reading its log rather than its exit code.

⓷ **An import that died on a side effect not understood.** The instrument's module directories reach
the path *as a consequence of importing the limits module*; the first cut of the edge test inserted
only this revision's own path.

⓸ **`300.98` meV is an envelope, not a limit**, and it is not offered as one anywhere in this record.

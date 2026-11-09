# `r7717+cc66` — REGISTERED BEFORE ANY COMPUTATION, AND THIS TIME THAT MATTERS MORE THAN USUAL

**The order** (`r7717`, 69): the estimator question is ruled **option 2** — the scatter about a line
*within* each band group is the right denominator, because the step is a difference between two groups'
**levels** and a gradient inside a group is not uncertainty about a level. ⇒ With four conditions:
**register first; calibrate on nulls before the real spectra; read everything under BOTH estimators side
by side; and report the well-posedness test under the new one too.**

---

## ⛔⛔ WHY THE ORDER OF OPERATIONS IS THE WHOLE PROBLEM HERE, AND WHAT I AM DOING ABOUT IT

**I have already read the four real spectra under the old estimator.** I know what it said: own × own
`3.51` sd, the kernel difference `1.47` sd and negative, the source difference `1.92` sd and positive, and
the well-posedness test passing by `0.8` of a percentage point. ⇒ **So "register before computing" cannot
mean what it meant at `r7713`, and pretending otherwise would be the dishonest move available to me.**
What it can mean, and what I am doing:

1. ⛭ **The new denominator is not invented here. It is taken VERBATIM from a probe I wrote and pushed
   BEFORE this order existed** — `r7713+cc66.10`'s
   `dryrun/probe_the_significance_denominator.py`, the `sd_alt` branch:
   `sqrt( (res(c_lo, R_lo)² + res(c_hi, R_hi)²) / 2 )`, where `res(c, r)` is
   `(r − polyval(polyfit(c, r, 1), c)).std(ddof=2)`, refusing on fewer than `3` points.
   **`git log` on that file against this file is the check, and it is the only defence available that
   does not rest on my word.** Not one character of it is changed here.
2. ⛔ **Every threshold is carried over unchanged, and none is new.** The `5` sd bar, the widest-window
   rule, the agreement gate, the well-posedness threshold and the whole decision table are copied from
   `r7713+cc66.0` and `.10` as they stand. **The only thing this revision changes is the denominator,
   because that is the only thing 69 ruled.**
3. ⛔ **The nulls are computed and reported BEFORE the real spectra are re-read**, in one run, in that
   order, and the run refuses to print a verdict if the calibration does not license the estimator.

## ⛭ THE NEW DENOMINATOR, FIXED

For a group with band centres `c` and ratio values `r`:

> `res(c, r) = std( r − (least-squares line in c fitted to r) , ddof=2 )`, and
> `sd_new = sqrt( (res(c_lo, r_lo)² + res(c_hi, r_hi)²) / 2 )`

against the registered `sd_old = sqrt( (var(r_lo, ddof=1) + var(r_hi, ddof=1)) / 2 )`.

⌗ *`ddof=2` because a line costs two parameters; `ddof=1` is right for the old form because a mean costs
one. Neither is a choice made here — both are in the probe.*

## ⛔⛔ THE CALIBRATION, AND THE NUMBER I AM REGISTERING NOW

**The estimator is licensed at `5` sd only if the null false-positive rate at `5` sd is at or below the
rate registered here.** So here it is, with its arithmetic in the open:

| | |
|---|---|
| null trials per family | **`N = 2000`** |
| registered requirement | **ZERO trials at or above `5` sd, in every null family** |
| what zero of `2000` bounds the rate at | **`< 1.5 × 10⁻³`** (rule of three, `95` %) |

⛔ **AND THE THING THAT MUST BE SAID IN ADVANCE RATHER THAN DISCOVERED LATER: a bar called "`5` sd" that
is calibrated this way certifies about `1.5 × 10⁻³`, NOT the `5.7 × 10⁻⁷` the name suggests.** The gap is
a factor of about `2600`. ⇒ *The name is a label for the statistic's value and it is not a probability
claim, and I am registering that before the calibration runs rather than conceding it after. To certify
`5.7 × 10⁻⁷` empirically would need of order `10⁷` trials, which is not what this costs or what the
order asks for.* **If 69 wants the name to mean the probability, that is a different and much larger
calibration, and it should be ordered as one.**

### THE NULL FAMILIES — two from the real banks, one already on disk

1. ⓵ **The synthetic nulls already run** (`r7713+cc66.10`, `dryrun/`). Already committed and pushed, so
   that they predate this order is checkable rather than asserted.
2. ⓶ **GROUP-ASSIGNMENT PERMUTATION** on the real ratios — 69's own first suggestion. The pooled set of
   band centres is reassigned at random to "low" and "high", keeping both group sizes. ⚠ **And a defect
   of this null is registered in advance, because it bears on the new denominator specifically: a
   permuted group is NOT CONTIGUOUS in `c`, so the line fitted inside it is fitted to scattered
   abscissae.** That is not the geometry the real groups have, so this null tests the denominator on a
   configuration it will not meet. ⇒ It is reported, and it is **not** the one the licence rests on.
3. ⓷ **PHASE-RANDOMISED SURROGATES** of the real per-`l` log-ratio — **the family the licence rests on.**
   Fourier transform in `q`, randomise the phases, invert, keeping the amplitude spectrum exactly. ⇒
   This preserves the data's own scatter AND its autocorrelation structure exactly while destroying any
   systematic step, and it keeps the real band geometry, so the groups stay contiguous and the line is
   fitted to the abscissae it will really meet. *A null that is easier than the data is a null that
   licenses an estimator falsely, which is why the structure-preserving family decides and not the
   permutation.*

### ⛔ AND 69's SECOND EXAMPLE IS NOT AVAILABLE TO ME — SAID NOW, NOT AFTER THE FACT

The order offers *"a ratio of a combination against itself across two runners"*. **I cannot build it.**
Each of the three CI combinations ran on exactly one runner, and the only thing computed on more than one
machine is the control: the banked combination's **first block, `25` `l`** of a `693`-`l` band. The slide
needs band centres across `q ∈ [0.85, 3.0]`; `25` `l` spans about `0.08` in `q` and admits no band at the
narrowest registered half-width, let alone two groups. ⇒ **Family ⓷ is what replaces it.** *If that
substitution is not acceptable, the across-runner null needs a second matrix run of an
already-computed combination, which is about an hour of runner time and which I have not spent without
being asked.*

## ⛭ WHAT IS REPORTED, AND IN WHAT ORDER — the run enforces this, it is not a convention

1. the two real-bank null calibrations, and the licence verdict;
2. **the three ratios and own × own under BOTH estimators, side by side, whatever the licence says** —
   69 asked for this explicitly so a reader can see what the denominator did;
3. the **well-posedness test** (interaction residual against own × own) under **both**;
4. the agreement gate, unchanged;
5. **the verdict — and ONLY if the estimator is licensed.** ⛔ If the calibration does not license it,
   the numbers are printed and **no row of the table is taken**, because a significance from an
   uncalibrated denominator is not a significance.

## THE DECISION TABLE — copied from `r7713+cc66.0`, unchanged

| verdict | what must hold |
|---|---|
| **THE PROJECTION CREATES IT** | the **kernel** difference alone gives a step of the measured sign and at least comparable size at **≥ 5 sd**; AND the **source** difference alone is under `2` sd or of the **opposite** sign. |
| **IT FAILS TO CANCEL** | the mirror image. |
| **NEITHER ⒜** | both under `5` sd. |
| **NEITHER ⒝** | both resolved, both of the measured sign, both comparable. |
| **NEITHER ⒞** | the well-posedness test refuses. |

⇒ Each difference is read at the **widest** registered half-width and must pass the **agreement gate**
(same sign at every width, magnitudes within a factor of two) — both unchanged from `r7713`.

## ⛔ AND WHAT I PREDICT, SO THAT IT IS ON THE RECORD BEFORE THE NUMBERS ARE

**I expect the single differences to clear `5` sd under the new denominator, and I expect that NOT to
settle the question.** The probe measured the kernel difference at `13.3` sd under `sd_new` against
`4.21` under `sd_old` on synthetic data with a planted effect — a factor of about `3.2`. Applied to the
real `1.47` and `1.92`, a similar factor lands both near `5`–`6` sd. ⚠ **But both would then be resolved,
both would be of their own signs — kernel negative, source positive — and the registered table's
"creates" and "fails to cancel" rows each require the OTHER difference to be unresolved or
opposite-signed.** Kernel negative and source positive against a positive own × own means the source
difference carries the sign and the kernel difference opposes it. ⇒ **That is the "fails to cancel" row's
shape, and I am registering now that I expect it to be reachable, so that if it comes out that way nobody
has to wonder whether I steered it.** ⌗ *And if the licence fails, none of this is claimed.*

## IF IT IS STILL NOT RESOLVED

Then, per the order: **"not resolved by this construction", with the reason named** — and that is a
finding about where the question sits, not a shortfall. ⇒ Plus **a proposal for what construction WOULD
separate the two mechanisms, if one exists**, which is owed either way and is the one genuinely new piece
of thinking this revision has to do.

## FAILABILITY

The null calibration is itself the failability: a denominator that manufactures significance shows it as
null trials over the bar. ⌗ *And the planted-effect synthetic scenarios are re-run under the new
denominator as a GREEN CONTROL FIRST, so that a calibration which licenses nothing is distinguished from
one that licenses everything.* ⛔ *A leg reporting `0` false positives on a null that is easier than the
data has measured the null, not the estimator — which is exactly why family ⓷ decides.*

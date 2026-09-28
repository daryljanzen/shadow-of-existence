---
name: r6999_PREDICTION
description: cc66.52 — the pre-registration for IMPOSING THE PROJECTION WIDTH, including the null. Written for r6999's ⓵.
status: WORKING DOCUMENT — pre-registration, not a result
current: r6999
---

# ⛭ `r6999` → `cc66.52` — PRE-REGISTRATION FOR THE WIDTH CHANNEL

*The order's ⓵ requires it: **"pre-register what each outcome would mean including the one where it does
nothing, since a measured-size channel that does nothing is as informative as one that works."** And the
standing guard adds: **"when a channel's size is measured rather than fitted, a result of 'it does
nothing' is a real result and has to be claimable in advance."***

## ⛔ WHAT WAS ALREADY COMMITTED, AND WHAT IS BEING ADDED NOW — SAID IN THAT ORDER

**⌗ COMMITTED AT `r6993`, BEFORE ANY OF THIS WAS MEASURED.** The filter's two teeth: a candidate carries
the excess only if its departure from unity **grows** across the bands as the target's does ($G=3.55$)
**and decelerates** (negative quadratic curvature, the target's $-0.0033$).

**⚠ ADDED NOW, AFTER SEEING A RESULT, AND DECLARED AS AN ADDITION RATHER THAN PRESENTED AS A HOLDING.**
Two conditions:

1. **SIGN IS THE FIRST TOOTH.** $G$ is a ratio of a departure at the top band to a departure at the
   bottom, so it is **blind to their common sign**: a channel that pushes the contrast uniformly and
   increasingly DOWN returns a large positive $G$ and a negative curvature, and passes both committed
   teeth while moving the measurement the wrong way. *This was found on an estimate that has since been
   superseded, and is registered anyway because it is a defect of the statistic and not of that
   estimate.* ⇒ **The departure must carry the target's sign before $G$ is read at all.**
2. **A STRETCH MUST NAME ITS FIXED POINT.** Widening a window by a factor is not an operation until the
   point held fixed is named; a stretch about the wrong point is a stretch plus a displacement, and a
   displacement of the visibility moves the **comb**, not the contrast. ⇒ **Any width result is quoted
   under both natural anchorings — the visibility's mean in $\eta$ and its peak — or it is not quoted.**

*Neither addition can be used to rescue this channel: both are conditions a candidate must pass, so
adding them can only make the filter harder, never easier. That is the whole reason they are admissible
after the fact.*

## ⌗ THE RUN BEING PRE-REGISTERED

*`ACOUSTIC_two_arm.py`, HIERARCHY path (`LOS=1 HIER=1`), at the refit minima. Control
`ARM=lcdm LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248`; arm
`ARM=cr CRH0=68.581133 CROM=0.297209 ZSTART=3e7 LEAFSCALES=1 WBH2=0.021524 NS=0.997952`. The operation:
**give the control the arm's conformal-time window width at the arm's measured size, holding the leaf
width.** Reported: the seven-band contrast ratio on `r6911+cc66.40`'s statistic, the anchored statistic
against the symmetric baseline $1.95$ (`cc66.48`), the comb, and the first four peak positions.*

**⌗ THE SIZE IS NOT A FREE COEFFICIENT.** It is $s = w_\eta(\text{arm}) / w_\eta(\text{control})$, read
off the banked visibilities: $1.135$ on the half-fall width, $1.146$ on FWHM, $1.065$ on RMS. **The
definition is named with the number, and the RMS reading is the tail-weighted one.**

## ⛭ WHAT EACH OUTCOME WOULD MEAN — ALL FOUR, INCLUDING THE NULL

| outcome | what it would mean |
|---|---|
| **① The contrast ratio moves UP by $2$–$8$ per cent, growing across the bands and DECELERATING** | The projection width is the carrier, or most of it. `PO-56` closes on a channel whose size was never fitted, and the two-rate assignment predicts the excess rather than accommodating it. *This is the only outcome that closes the row.* |
| **② It moves UP but by much less than the target, or with the wrong curvature** | The width is a **contributing channel and not the carrier**. `PO-56` stays open, the residual to be explained shrinks by the measured amount, and the paper carries the width as a stated CR effect of known size. |
| **③ It moves DOWN** | The width works **against** the measurement: the excess is larger than the raw arm-versus-control comparison shows, because part of it is being cancelled by a channel the construction forces. *That would make the row harder, not easier, and it would still be a result.* |
| **④ THE NULL — it does nothing, below a few tenths of a per cent in every band** | **A real result and the one this pre-registration exists for.** The projection's conformal width, though it differs between the arms by a measured and forced amount, does not reach the contrast statistic. ⇒ *The channel is closed by measurement rather than left unmeasured, the `PO-56` runway loses an item, and the width survives only as a prediction about the window (⓷) with no observational consequence in this statistic.* |

**⛔ AND WHAT WOULD NOT BE CLAIMED UNDER ANY OF THEM.** Nothing about the comb or the peak positions is a
contrast result: a width change that moves the comb has displaced the window, which is outcome ③'s
warning sign and not a success. *If the comb moves by more than a grid step, the operation is reported as
having changed the window's position and the contrast numbers are not read.*

## ⚠ AND THE ONE OUTCOME THAT WOULD MEAN THE RUN CANNOT BE DONE

*If the conformal width cannot be changed in this instrument without also changing the leaf width, the
operation is not the one ordered and **that is reported rather than substituted for**. The standing
instruction is explicit: a run that cannot be constructed is a fact about the instrument, and the papers
can carry it without embarrassment.*

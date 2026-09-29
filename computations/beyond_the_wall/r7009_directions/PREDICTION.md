---
name: r7009_PREDICTION
description: cc66.57 — the pre-registration for whether the step is the excess's or the estimator's, written BEFORE any of it was measured, on the order's explicit sequencing.
status: WORKING DOCUMENT — pre-registration, not a result
current: r7009
---

# ⛭ `r7009` → `cc66.57` — WRITTEN BEFORE THE MEASUREMENT, WHICH THE ORDER REQUIRED IN TERMS

*The order's ⓵: **"PRE-REGISTER THAT BEFORE ANYTHING ELSE... I am asking for this first because ⓶ and ⓷
are both built on the step, and I would rather lose the step now than build two revisions on it."***

**⌗ SO THE ORDERING IS REAL THIS TIME AND IS STATED AS SUCH.** Nothing in ⓵ has been computed at the time
this file is written. *The previous three revisions each had to say that their outcome tables came after
their measurements; this one does not, and the difference is the order's sequencing rather than any virtue
of this seat's.*

## ⛔ THE HAZARD, NAMED BEFORE IT IS TESTED

**`r7009`'s new guard: *a step at the edge band is where an edge artefact lives.*** Band 1 spans
$q \in [0.85,\,1.55]$ and the banked spectra begin at $q = 0.3316$. A running envelope of half-width
$0.5$ evaluated at $q = 0.85$ reaches down to $q = 0.35$ — **inside the data by $0.018$ in $q$, which is
about five multipoles.** ⇒ *Band 1 is the only band whose envelope is within a hair of truncating, and
a truncated running mean of a falling spectrum is biased high, which would depress the band's contrast.
That is exactly the artefact that would manufacture a step.*

## ⌗ WHAT ⓵ WILL DO, FIXED HERE

1. **A THIRD ENVELOPE, different in kind rather than in width.** A local low-order polynomial fit
   (Savitzky–Golay) rather than a running mean or a running median. *The order says to add a third, not
   to choose among them, and no envelope will be chosen.*
2. **AND A READING THAT NEEDS NO ENVELOPE AT ALL.** The peak-to-trough depth per acoustic cycle,
   $(\max - \min)/(\max + \min)$, formed from the spectrum's own local extrema. *No running window
   enters it, so no edge of a window can bias it.*
3. **AND THE EDGE HAZARD MEASURED DIRECTLY**: how much of band 1's contrast comes from the part of the
   band whose envelope window is closest to truncating, and what the band reads with that part excluded.

**⚠ AND THE STEP'S DEFINITION IS NAMED BEFORE IT IS USED**, per the standing guard: **the step is the
ratio of band 1's excess to the mean of the excess over bands 2–7.** *It is $0.33$ on the arithmetic
envelope. A "surviving" step means that ratio stays well below one on every reading; a step that
"goes away" means it comes back towards one.*

## ⚠ THE FAILURE MODES — AND THE ONE THAT EMBARRASSES THE REVISION IS FIRST

| failure mode | what it would mean |
|---|---|
| **THE STEP GOES AWAY ON THE THIRD ENVELOPE** | ***The finding is the statistic's and not the excess's, and it is reported as that.*** `cc66.56`'s ⓷ — which this seat called the sector's real finding and which `r7009` has already landed in two sections — **would be withdrawn**, and the four mismatches would go back to being four mismatches. *Tabled first because it is the outcome that costs this seat most.* |
| **The step survives the third envelope but not the envelope-free reading** | Then it is a property of *having* an envelope rather than of which one, which is a narrower but still fatal result for ⓶ and ⓷. |
| **The step survives everything but band 1's contrast is dominated by the near-truncating edge** | ⇒ *The step is real as a number and untrustworthy as a measurement; ⓶ and ⓷ would have to be run on the part of band 1 that is clear of the edge, or not at all.* |
| **The extrema-based reading cannot be formed in band 1** | Band 1 holds about one acoustic cycle of the spectrum's comb, so there may be too few extrema to form a depth. ⇒ *Report that the envelope-free check is not available there rather than substituting a windowed one for it.* |
| **The step survives every reading** | ⓶ and ⓷ proceed. *This is the outcome the order expects and it is therefore the one to be most careful about.* |

## ⛭ AND WHAT ⓶ AND ⓷ WOULD MEAN, TABLED NOW SO THEY ARE NOT TABLED AFTERWARDS

| outcome | what it means |
|---|---|
| **⓶ the step's location coincides with a scale the construction fixes** | ***The carrier's signature, with no free coefficient*** — the same shape as the width prediction. |
| **⓶ it coincides with nothing in the construction** | *A different and also useful finding*, and the order says so in advance. |
| **⓶ the step has a width comparable to a band** | Then "step" is the wrong word and it is a slow feature the band edges are aliasing; the location question would not be well posed. |
| **⓷ one of the four produces a step of the right sign and size** | *That candidate has been failing the wrong test for four revisions.* |
| **⓷ none of the four can be evaluated at band 1 by any route** | ***The identifiability floor closing over the whole candidate list at once***, which the order rightly says is stronger than four mismatches. |
| **⓷ they can be evaluated and none produces the step** | The list is exhausted against the right feature, which is the first time it would have been. |

**⛔ AND WHAT WILL NOT BE CLAIMED.** That the step is the carrier, or that a coincidence of scales is a
mechanism. *A step at a scale is a signature to be explained, not an explanation.*

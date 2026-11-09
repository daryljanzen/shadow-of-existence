# `r7717+cc66` — THE RULED DENOMINATOR IS **NOT LICENSED**, AND THE CALIBRATION IS WHY THAT MATTERS

**The order's second condition did its job.** `r7717` ruled option 2 and required it be calibrated on
nulls *before* it touched the real spectra again. It was. **It fails, and it fails at exactly the window
the registered rule reads at.**

---

## ⓵ THE GREEN CONTROL FIRST — the ruled denominator DOES see a real effect

| ratio (planted synthetic) | old | **ruled** |
|---|---|---|
| own × own | `6.21` sd | **`20.88` sd** |
| kernel alone | `4.21` sd | **`13.83` sd** |
| source alone | `3.77` sd | **`10.65` sd** |

⇒ It is sharper on a planted effect by a factor of about `3`. *A denominator that licenses nothing would
be useless, so this is established before it is asked not to invent anything.*

## ⛔⛔ ⓶ AND THEN THE NULLS, WHICH REFUSE IT

`2000` step-free trials per family per ratio per width. Registered requirement: **zero** at or above
`5` sd in **every** family.

| ratio | width | permutation | **structure-preserving surrogate** |
|---|---|---|---|
| own × own | `0.175` | `0`/2000 | `0`/2000 |
| own × own | `0.250` | `0`/2000 | **`36`**/2000 |
| own × own | `0.350` | `0`/2000 | **`277`**/2000 |
| kernel alone | `0.350` | `0`/2000 | **`62`**/2000 |
| source alone | `0.250` | `0`/2000 | **`60`**/2000 |
| source alone | `0.350` | `0`/2000 | **`349`**/2000 |

⛔ **Up to `17` per cent of step-free trials cross `5` sd at the widest window — the window the
registered rule reads at.** The permutation family shows zero everywhere, exactly as `PREDICTION.md`
said it would, which is why the licence was registered to rest on the structure-preserving family and
not on it.

⇒ **NOT LICENSED.** And therefore **no row of the decision table is taken**: a significance from an
uncalibrated denominator is not a significance.

## ⛭ ⓷ WHY IT FAILS — and 69's REASONING IS NOT WHAT FAILED

The ruling's argument was: *a gradient inside a group is not uncertainty about that group's level.*
**That is right.** What the measurement shows is that the fix removes more than the gradient:

> **removing a line inside each group also removes the long-wavelength fluctuation — and that
> fluctuation IS the uncertainty of the group's level.**

⇒ So the two denominators fail in **opposite directions, from one cause**:

| | what it does | direction |
|---|---|---|
| the old form | counts the within-group gradient as uncertainty | **too large** |
| the ruled form | removes the gradient, and the long-wavelength fluctuation with it | **too small** |

⛔ **The common cause: the step is a LOW-FREQUENCY feature of a correlated curve, and no within-group
summary of that curve can estimate the uncertainty of a low-frequency feature.** *That is a statement
about the statistic, not about either seat's reasoning, and it is the thing this revision establishes.*

## ⓸ BOTH ESTIMATORS SIDE BY SIDE, AS ORDERED

| ratio | step (widest) | old | ruled |
|---|---|---|---|
| own × own | `+0.0261` | `3.51` sd | `7.25` sd |
| kernel alone | `−0.0286` | `1.47` sd | `2.06` sd |
| source alone | `+0.0481` | `1.92` sd | `3.10` sd |

⌗ *The ruled denominator roughly doubles own × own and barely moves the two single differences, which is
already a hint that it is not doing what it was meant to: the thing it sharpens most is the ratio whose
curve is smoothest.*

## ⓹ THE WELL-POSEDNESS TEST, UNDER BOTH, AS ORDERED

| width | residual step | old | ruled |
|---|---|---|---|
| `0.175` | `+0.014870` | `2.90` sd | **`5.03` sd** |
| `0.250` | `+0.013830` | `3.20` sd | **`6.18` sd** |
| `0.350` | `+0.010792` | `2.88` sd | **`7.84` sd** |

The residual step is **`49.2` %** of the own × own step, unchanged — it is the same steps. ⇒ So the
registered refusal (`≥ 2` sd **and** `≥ 50` %) **still does not fire, by `0.8` of a percentage point,
under either denominator.** ⚠ **But it is now a `5`–`8` sd interaction**, which makes that margin far
more uncomfortable than it was at `r7713`, and I am saying so rather than banking the pass.

## ⓺ THE AGREEMENT GATE

All three ratios: one sign at every width, magnitudes spanning `1.12`–`1.21`×. **Passes cleanly.**

## ⛔⛔ AND THE NUMBER THAT CHANGES THE PICTURE — THE ONLY CALIBRATED TEST AVAILABLE

The surrogates can be read the other way round: not as a licence test for an `sd`, but as the step's own
null distribution. `20000` step-free surrogates per curve, two-sided:

| ratio | widest window | `p` |
|---|---|---|
| own × own | `+0.0261` | **`0.087`** |
| kernel alone | `−0.0286` | **`0.470`** |
| source alone | `+0.0481` | **`0.358`** |

⛔ **Against step-free curves carrying the data's own scatter and autocorrelation, neither single
difference is distinguishable from the curve's own wiggliness at all, and own × own is marginal.** ⇒
*Both parametric denominators were optimistic — the old one by a lot, the ruled one by more. The honest
reading of the pseudo-spectrum route is that it resolves nothing, and `r7713`'s `3.51` sd was already
too generous.*

⚠ **This is NOT a verdict and it is NOT an installed estimator.** It is unregistered, and a reading
under an unregistered estimator cannot settle anything. It is here because the order asked for a
proposal and a proposal with its own numbers is worth more than a description of one.

## ⇒ THE PROPOSAL, WHICH IS NOT A THIRD DENOMINATOR

**Stop summarising the null with an `sd`.** Compare the step against the distribution of steps from
phase-randomised surrogates of the detrended curve, and report its percentile. No `sd`, no normality,
no within-group summary — and the machinery already exists, because it is the licence test read
backwards.

| | |
|---|---|
| cost per surrogate | **`26` µs**, measured |
| to express a `5.7 × 10⁻⁷` bar | about `10⁷` surrogates ⇒ **about `4` minutes of one core per curve** |
| ⇒ | a genuinely `5`-sd-calibrated non-parametric test **is affordable**, which is the point |

⌗ *And it would dissolve the whole `5` sd naming problem registered in `PREDICTION.md`: a percentile
against `10⁷` surrogates means what it says, where "`5` sd" from a `2000`-trial calibration certifies
only `1.5 × 10⁻³`.*

## ⚠ WHAT I GOT WRONG, ON THE RECORD BECAUSE I REGISTERED IT

`PREDICTION.md` registered my expectation: *"I expect the single differences to clear `5` sd under the new
denominator."* **They do not** — `2.06` and `3.10`. And I registered the shape I expected the verdict to
take, so that nobody would wonder whether I steered it. ⇒ **I steered it nowhere, and the prediction was
simply wrong in the direction that would have flattered the result.**

## WHAT IS NOT CLAIMED

- **No verdict.** The ruled denominator is unlicensed and the alternative is unregistered.
- **No attribution**, unchanged.
- **The acceptance kernel is not the exact transfer**, unchanged.
- **The permutation family's zeros are not evidence of licensing** — registered in advance as the weaker
  test, for a reason the run then confirmed.
- **The surrogate `p` values are not a result**, and the `20000`-trial floor (`4.06` sd equivalent) is
  stated so that none of them is read as smaller than it can be.

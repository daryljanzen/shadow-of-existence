# r7900 — REGISTER BEFORE EITHER SIDE RUNS: does the instrument's late-ISW term respond to Σ as CAMB's does?

Order `r7895` (69) item ②. ⌗ *Committed and pushed before any with/without spectrum is computed.*

The order: *"Compute the instrument's TT at multipoles `100`–`207` with and without its late-time
potential-decay source, at Σ = 0 and at `0.06`, `0.30` and `0.60` eV. `cc66` supplies CAMB's same
split (its `⑱ ③`). Register the comparison before either side runs. The question is whether the
instrument's late-ISW term responds to Σ as CAMB's does. If it does not, that is a mechanism located
exactly where the move is."*

`cc66`'s `⑱ ③` has **not** landed on `main` as of `665892507`, so neither side has run and registering
now is what the order asks.

## ⒜ WHAT THE INSTRUMENT'S POTENTIAL-DECAY SOURCE IS, EXACTLY

One term in the line-of-sight source, with its own switch already in the instrument:

    + _ISW * et * ( dΦ/dη + dΨ/dη )        _ISW = 0 when NOISW=1, else 1

So *with and without* is not new machinery and not an approximation — it is that switch. The other two
source terms, the monopole `SWSRC` and the Doppler dipole `DPSRC`, have their own switches and are
untouched.

## ⒝ AND THE SUPPORT IT IS INTEGRATED OVER, WHICH IS A FACT ABOUT THE INSTRUMENT AND NOT A RESULT

Read from the instrument's own background before any comparison was run, and stated here so that it
cannot be presented afterwards as though the scan discovered it:

| | conformal time | redshift |
|---|---|---|
| recombination, `eta_rec` | `280.67` | `1089.900` |
| **where the solve STOPS, `ETA_END`** | **`1893.12`** | **`53.545`** |
| today, `eta_0` | `14145.33` | `0.000` |

`ETA_END` is `float(ETAEND) or np.interp(min(20 * A_REC, 1.0), ag, eg)` — the conformal time at twenty
times the scale factor at recombination. **So the source is integrated over about `13` per cent of the
conformal time to today, and stops at `z ≈ 53.5`.**

⛭ **The late ISW is generated when the potential decays, and in a matter-dominated universe it does
not decay.** The decay that produces the late ISW is driven by Λ, at `z ≲ 1`, which is outside this
range entirely. ⌗ *This is a reading of the instrument's code and background, not a measurement of a
response, and it is the reason the outcome `Ⓔ⓸` below exists. It is written down BEFORE the
measurement precisely so that the measurement can refute it.*

⚠ **What this reading does NOT establish, and the scan must decide:** that the `100`–`207` ISW
difference is therefore negligible. Early ISW is inside the range and also lands at low multipoles, so
a large with/without difference there is entirely possible and would mean the support reading does not
decide the question. The size is measured, not inferred.

## ⒞ WHAT WILL BE MEASURED

TT over multipoles `100`–`207`, with `_ISW` on and off, at Σ = `0`, `0.06`, `0.30`, `0.60` eV — eight
runs of the instrument's own generator, the control arm, nothing else changed. ⌗ *Not read through a
crossing, as the order requires: `r7890` established that on this band the difference operator's own
artefact is `7.2` times the signal, so the comparison is on spectra directly.*

Reported per sum: the band-summed with/without difference, its fraction of TT in that band, and how
that fraction moves with Σ.

## ⒟ THE IDENTITY THAT MAKES THE DIFFERENCE EXACT RATHER THAN AN ADDITIVE FICTION

`r7874` established, and registered in advance of its own run, that **"each term's contribution" does
not exist**: the source terms add, but `D_l` is quadratic in the transfer, so the projected pieces do
not. What closes is the bilinear decomposition — ten pairs summing to `D_l` exactly, four of them
involving `isw`.

That makes the order's with/without difference a well-defined object with a known identity:

    D_l(ISW on) − D_l(ISW off)  ==  sw*isw + dp*isw + isw*pol + isw*isw

the four `isw`-involving pairs, which `r7874` banked at Σ = `0`, `0.30`, `0.60`. **The scan will check
that identity at those three sums** and report it as a closure. ⛔ *If it fails, the switch is not
doing what its name says and no response is reported at all.*

⌗ *So the difference is NOT "the ISW term's contribution" in any additive sense, and will not be
called that. It is the amount `D_l` changes when the term is removed, which is a different quantity
and the one the order asks for.*

## ⒠ THE OUTCOMES, FIXED NOW

| | outcome | criterion |
|---|---|---|
| `Ⓔ⓵` | **RESPONDS AS CAMB'S DOES** | the fractional difference moves with Σ in the same direction, and within a factor of `2` of CAMB's |
| `Ⓔ⓶` | **RESPONDS, BUT NOT AS CAMB'S DOES** | it moves with Σ beyond the instrument's own reproducibility, but not as above |
| `Ⓔ⓷` | **DOES NOT RESPOND** | the fractional difference is flat in Σ to within the instrument's own reproducibility |
| `Ⓔ⓸` | **THE TERM IS ABSENT WHERE IT MATTERS** | the with/without difference is under `1` per cent of TT across `100`–`207` at every sum |

⛔ **`Ⓔ⓵` and `Ⓔ⓶` require `cc66`'s `⑱ ③`.** If it has not landed when the instrument's side is
measured, those two branches **cannot be decided**, and the registration says now what happens then:
the instrument's side is reported alone, `Ⓔ⓷`/`Ⓔ⓸` are decided on it, and the comparison is left open
and named as waiting. ⌗ *A half-answer reported as a half-answer, not a whole one.*

⚠ **`Ⓔ⓸` is NOT exclusive with `Ⓔ⓷`.** A term that is absent has a trivially flat response, so both
may fire; where they do, **`Ⓔ⓸` is the stronger statement** and is the headline, with `Ⓔ⓷` reported
beside it. This is the same non-exclusivity discipline `r7892` and `r7894` were registered under, and
for the same reason: choosing between them after seeing the numbers is what registration excludes.

## ⒡ THE REGISTERED EXPECTATION

**`Ⓔ⓸`, with `Ⓔ⓷` beside it.** The grounds are a structural reading of the instrument rather than an
extrapolation from a neighbouring measurement, so this expectation is registered as the **strong**
kind — unlike `r7896`'s and `r7898`'s, both of which were weak and both of which were refuted.

⚠ **And its reachable negative is named:** if the with/without difference across `100`–`207` is a
significant fraction of TT, then early ISW carries that band and the support reading does not decide the question.
That would refute this expectation, and it would be the more useful result, because it would mean the
band has a live ISW term to compare against CAMB rather than a missing one.

## ⒢ THE CONTROL, AND IT GATES EVERYTHING

With `NOISW=1` the four `isw` pairs must be **identically zero**, and the six pairs that do not
involve `isw` must reproduce the default run's six to the instrument's own reproducibility.

⛔ **If the six non-`isw` pairs move, the switch is not inert outside its own term, and no difference
is reported** — because a difference that also carries a change in the monopole or the Doppler dipole
is not the ISW's.

## ⒣ WHAT THIS REVISION WILL NOT DO

- It will **not** extend `ETA_END` to today. Giving the instrument the late epoch is a change to what
  the instrument IS, every banked spectrum was computed without it, and whether the perturbation
  equations are valid to `z = 0` is a separate question this does not open. If `Ⓔ⓸` fires, that
  extension is the obvious next revision and will be named as such, not performed here.
- It will **not** read a limit. `r7888`'s `193.545` meV is untouched.
- It will **not** claim a mechanism for the low-end lean. A missing term in the band where the lean
  sits is a candidate and a coincidence of location, which `r7892` already recorded about a different
  candidate; naming it as the cause would need the lean to move when the term is supplied, and that is
  the extension this revision declines to make.

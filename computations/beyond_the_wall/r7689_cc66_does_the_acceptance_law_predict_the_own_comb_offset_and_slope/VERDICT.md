# `r7689` (cc66) — VERDICT

Scored against `PREDICTION.md`, pushed (`r7689+cc66.0`, `e3a67bbfd`) before any computation, with a
licence named for each figure in advance. **Four confirmed, one falsified, one check passed.**

## THE ANSWER: YES, TO WITHIN FIVE PER CENT IN AGGREGATE, AND WITH ONE BAND AND ONE SHAPE AGAINST IT

**Arm ⑤ first, as registered.** The law's arm/control ratio runs `1.0084`–`1.0877`; the measured
own-comb bands run `1.028`–`1.075`. Worst ratio-of-excesses between the two objects: **`1.17`**,
against my registered ill-posed threshold of `2`. ⇒ **COMMENSURABLE, so the accounting is licensed.**
⌗ *The bridge is stated rather than assumed: the law is banded by its band MEAN, because `A_\ell` is
already an amplitude fraction and not an oscillation to take an RMS of.*

### Band by band at the 7-band window-1 setting — what the order asked for

| q centre | the LAW | MEASURED | law − meas | law excess / meas excess |
|---|---|---|---|---|
| 1.20 | `1.0349` | `1.0364` | `−0.0016` | `95.7%` |
| **1.90** | `1.0516` | `1.0708` | **`−0.0192`** | **`72.9%`** ⛔ beyond the setting spread |
| 2.60 | `1.0638` | `1.0659` | `−0.0021` | `96.8%` |
| 3.30 | `1.0725` | `1.0699` | `+0.0026` | `103.7%` |
| 4.00 | `1.0786` | `1.0858` | `−0.0072` | `91.6%` |
| 4.70 | `1.0828` | `1.0827` | `+0.0001` | `100.1%` |
| 5.40 | `1.0854` | `1.0832` | `+0.0022` | `102.7%` |

**Summed excess: the law accounts for `94.9` per cent of the measurement, with six of seven bands
inside the statistic's own setting spread of `0.0089`.** From a formula with **nothing fitted.**

### And over the twelve settings

| | the LAW | MEASURED | law / measured |
|---|---|---|---|
| slope per period | `+0.01122` | `+0.01030` | `108.9%` |
| intercept | `1.0300` | `1.0260` | `115.6%` of the excess |
| lowest band | `1.0367` | `1.0280` | `131.2%` |
| highest band | `1.0857` | `1.0750` | `114.2%` |

⌗ **The two tables disagree and the band-by-band one is the measurement.** The intercept is a fit's
extrapolation to `q = 0` from a lowest band centred at `q ≈ 1.2`, and the law's shape extrapolates
differently from the measurement's — so `115.6%` is a property of two extrapolations and `94.9%` is a
property of seven bands. *Reported together, with which is which stated, rather than picking the
flattering one.* The law's slope spread over the twelve settings is `0.00059`, under half the
measurement's `0.00137`.

## THE ARMS

**① the ratio above one in every band — ✔ CONFIRMED** (`1.0349` to `1.0854`; `12` of `12` settings
give an intercept above one, as the measurement does).
*Licensed: the offset's sign. Not its cause.*

**② it accounts for ≥ 50 per cent of the offset — ✔ CONFIRMED, and far above the floor:** `94.9%`
band by band, `115.6%` of the fitted intercept excess.
*Licensed: "the law accounts for `94.9` per cent of the excess". ⛔ **NOT** licensed: that the missing
`5.1` per cent is the phase drift, noise, or anything else. **There is no remainder term in this
computation and I am not naming one.***

**③ the law accounts for less of the rise than of the offset, its slope under half the measured —
⛔ FALSIFIED, and in the direction I flagged as uncertain.** The law's slope is `+0.01122` against
`+0.01030` — `109` per cent, not under `50`. ⌗ *I registered low confidence because nothing had
measured whether the acceptance asymmetry grows with ℓ. **It does, monotonically**, `1.0349` to
`1.0854`. The rise is the law's as much as the offset is.*

**④ at least one band off by more than the setting spread — ✔ CONFIRMED, and exactly one:** `q ≈ 1.9`,
where the measurement sits `0.0192` above the law, `2.2 ×` the spread.
*Licensed: a per-band residual table and the statement that one band of seven is outside. ⛔ **NOT**
licensed: a cause for that band, or a verdict on the law as a whole from it.*

**⑤ the comparison may be ill-posed — ✔ CHECK PASSED,** `1.17` against a threshold of `2`.

**⑥ under `60 s` — ✔ CONFIRMED,** under one second, in its own file as registered.

## ⛔ THE ONE NEGATIVE RESULT, AND IT IS A SHAPE AND NOT A NUMBER

**The law rises monotonically across the seven bands. The measurement does not** — it goes `1.0364`,
`1.0708`, `1.0659`, `1.0699`, `1.0858`, `1.0827`, `1.0832`, dipping at the third band and again at the
sixth. ⇒ ***So the law cannot produce the measurement's non-monotonicity, and the `q ≈ 1.9` outlier is
where that difference is largest.***

*Licensed: "the law does not produce the measured band-to-band shape." ⛔ **NOT** licensed: that the
departure is the phase drift — which is the obvious thing to reach for, is exactly `r7687` row 6b's
error, and would need a measurement this computation does not contain.* ⌗ **What would test it:** the
own-comb null is already computed per band in `the_phase_systematic…`; banding its real-phase response
on these same seven bands and asking whether it reproduces the dip at `q ≈ 1.9` would settle it, and
that is a measurement rather than an inference.

## WHAT I WOULD TELL 69 IF THERE WERE ONE SENTENCE

**A law with no fitted coefficient reproduces, to five per cent in aggregate and inside the
statistic's own setting spread in six of seven bands, both the offset and the rise that `r7683`–`r7687`
spent four revisions measuring — and it fails on the band-to-band shape, which is the part nobody had
asked it for.**

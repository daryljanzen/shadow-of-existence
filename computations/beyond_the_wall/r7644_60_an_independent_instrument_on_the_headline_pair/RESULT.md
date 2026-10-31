# `r7644` (60) — EVERY FIGURE IN THE HEADLINE PAIR REPRODUCES ON A SECOND SCORER, AND THE CHOICE THAT MOVES THEM IS MEASURED RATHER THAN NAMED

**Receipt:** `independent.py` — 20 checks, 0 failures. **Registered:** `PREDICTION.md`, its own commit.
**Order:** `r7643` (69) — the lensed and unlensed no-fit pair and the refit pair, on the same 185 bins,
on an instrument independent of cc66's.

## ⚑ THE ANSWER TO "DO THE TWO INSTRUMENTS AGREE": YES, ON ALL EIGHT SCORES

| configuration | | control | namesake arm | arm of record | n/c | r/c | cc66 prints |
|---|---|---|---|---|---|---|---|
| `L2000` (no-fit) | unlensed | 696.0 | 1169.8 | 938.3 | 1.681 | **1.348** | 1.35 |
| `L2000` (no-fit) | **lensed** | **214.1** | **550.5** | **302.1** | **2.572** | **1.411** | 214.1 / 550.5 / 302.1 → 2.57 / 1.41 |
| `r185 verify` (refit) | unlensed | 592.8 | 910.1 | 924.2 | 1.535 | 1.559 | |
| `r185 verify` (refit) | **lensed** | **186.5** | **292.4** | **297.7** | **1.568** | **1.596** | 186.5 / 292.4 / 297.7 → 1.57 / 1.60 |
| `grid base` (refit) | **lensed** | **212.9** | **545.8** | **297.7** | **2.564** | **1.398** | 212.9 / 545.8 / 297.7 → 2.56 / 1.40 |

**Every score agrees to the digits the paper prints**, and both printed ratios with them — `2.57` and
`1.41` — along with the `1.35` unlensed figure the order cites and the refit row's `1.57`/`1.60`.
⇒ **Arm ⓐ is a HIT and the order's first negative is not reached:** nothing differs beyond the third
digit.

## ⌗ WHAT MAKES THIS A SECOND READING AND NOT A RE-TYPING

The data is shared **on purpose** — `plik_lite` TT, its binning weights and its covariance are the
measurement, and an instrument on other data would answer a different question. The **code is not**:
this receipt does not import the corpus's own scorer, the one every figure under test was produced by.
Its binning, its marginalisation and its amplitude fit are written here, and the bin count (185) and
range (ell 100 to 1996) are **asserted, not inherited**.

## ⚑ AND THE PART WORTH MORE THAN THE AGREEMENT: THE FOUR CHOICES, VARIED

cc66's scorer names four choices as the ones that matter. **A re-implementation making the same four
silently would show only that two people can agree**, so each was varied:

| variation | control | namesake | record | n/c | r/c |
|---|---|---|---|---|---|
| as cc66 chose | 696.0 | 1169.8 | 938.3 | 1.681 | 1.348 |
| **CONDITION** on the uncovered bins instead of marginalising | 709.8 | 1302.1 | 1047.9 | 1.834 | 1.476 |
| amplitude **FIXED at 1** instead of fitted | 360828.0 | 360831.3 | 360839.9 | 1.000 | 1.000 |
| bin the weighted ell **CENTRE** instead of the whole bin | 708.8 | 1181.9 | 954.2 | 1.668 | 1.346 |

- **The covariance choice is load-bearing at the second digit of a printed figure: `+9.5%` on the
  ratio.** Conditioning on the uncovered bins rather than marginalising over them is the choice cc66's
  receipt says matters most, and now there is a number for it.
- **Interpolating the bin centre instead moves it `-0.2%`** — so that choice is not load-bearing, and
  the receipt's ranking of its own four choices is confirmed by measurement.
- **The fitted amplitude is load-bearing rather than cosmetic.** Fixing it at 1 drives all three scores
  to ~360 830 and flattens both ratios to `1.000`: the banked spectra carry an inherited `A_s`, so the
  comparison is of **shape**, and a reader who did not fit the amplitude would read **no difference
  between the arms at all**.

⇒ **THE ORDERING SURVIVES EVERY VARIATION THAT COMPARES SHAPE** — control best, arm of record between,
namesake arm worst, in all three. **So the order's second negative is not reached either: which
configuration is the less favourable is the data's and not the scorer's.**

⛔ **AND IT DOES NOT SURVIVE THE FOURTH, WHICH IS WHY THE FOURTH WAS RUN.** With the amplitude fixed
the order **reverses** — but on differences of 3 and 12 in 360 828, one part in 10⁵ of a single shared
mismatch, so that row is not a comparison and its reversal is not a finding about the arms.
⌗ *The check that was going to assert survival across all four was first written as a constant. Made
into a real assertion it FAILED, and the failure is the honest reading. A guard that cannot fail on the
data it is given is not a guard.*

## ⌗ WHAT WAS BLOCKED, NARROWED FROM WHAT THE ORDER ASSUMED

The order says the no-fit spectrum on the arm of record does not exist yet. **Read against the bank
that is true of one thing and not of three:** the control, the namesake arm and the arm of record all
exist at the distances' point, so **the no-fit triple is computable now and is computed above**. What
does not exist is the arm of record's no-fit spectrum **as a file distinct from its refit one** —
⇒ and that block is **confirmed from the files rather than taken on cc66's word: on the arm of record
the grid base and the verification run are BIT-IDENTICAL.** So the two confrontations the blocked
reader needs are one file, and **no scoring code can narrow the `1.48`–`1.60` spread**, which is why
the refit half is reported here as a bound with its route named and never as a single number. Arm ⓑ
and arm ⓒ both hold.

## ⌗ THE LENSING OPERATOR, AND THE INSTALL THAT WAS DELIBERATELY NOT MADE

cc66 imposes CAMB's **full** lensed/unlensed ratio and its receipt rejects the first-order kernel by
name — the kernel reads a spurious `+13%` at ell = 1900 against the full operator's `+6.5%`. `camb` is
absent from the interpreter this corpus is **verified** on.
⛔ **And installing it there would have moved the arithmetic under every float comparison in the
corpus:** `pip install camb` pulls a newer `scipy`, which is the one event
`receipts/ENV_FINGERPRINT.txt` exists to catch — *"an UNPINNED install moves the arithmetic under every
float comparison in the corpus with no push at all."*
⇒ So the operator was computed by a **separate file under a separate interpreter** and saved; the
scorer reads that array on the pinned one. The operator is an **imposed input, not a fitted one**, so
it is data and may be read. It returns **1.0666** at ell = 1900, inside the `[1.05, 1.08]` cc66's own
receipt gates it into. **`check_env_fingerprint` is green and the scoring interpreter still reports the
swept numpy and scipy.**

## ⛔ ONE CORRECTION AGAINST THIS LINE

The first form of the refit part scored those rows **unlensed** and missed every figure. cc66's table
is the lensed confrontation throughout — its control reads `214.1` where the same file unlensed reads
`696.0` — so the refit row is lensed too. Corrected, with the mistake named in the receipt and **both**
halves printed rather than the wrong one quietly replaced.

## ⚠ WHAT IS NOT CLAIMED

- Not that the agreement makes the figures right: it makes them **instrument-independent at the printed
  digits**, which is a different and smaller claim, and the `+9.5%` above is the measure of how much
  smaller.
- Not a figure for the no-fit-against-refit contrast on the arm of record. That stays blocked, with the
  bit-identity that blocks it.
- No paper is edited, no figure moves, no parameter is pinned, and no receipt of cc66's or 70's is
  touched. The agreement is **routed**, because `P15`'s rule is that a printed figure moves only when
  every citing receipt is re-pointed, and this instrument is a check on those receipts rather than one
  of them.

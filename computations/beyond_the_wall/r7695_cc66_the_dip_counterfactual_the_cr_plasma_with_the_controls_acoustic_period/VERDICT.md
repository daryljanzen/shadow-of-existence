# `r7695` (cc66) — VERDICT. **THE COUNTERFACTUAL WORKED, THE GATES PASSED, AND THE RESULT IS THE REGISTERED NEGATIVE: THE `q ≈ 1.9` DEPARTURE IS NOT THE TWO ARMS' ACOUSTIC PERIOD-AND-PHASE DIFFERENCE**

| arm | registered | measured | verdict |
|---|---|---|---|
| **gate 3** | `T_K` at the control's `1.017000`, tolerance two grid steps | `1.016750` — **one** step | ✔ **PASSES** |
| **gate 3b** | `r_s`, `D_M`, `l_A`, the `k` grid unmoved | all identical to the digit | ✔ **PASSES** |
| **the `D_l`-side prediction** | it also lands within two steps | `1.004500 → 1.009750` against `1.009250` — **two** steps | ✔ **CONFIRMED** |
| **① what the test cannot separate** | a positive would not license "the departure is the phase drift" | *moot, and it held: no positive to over-read* | ✔ held |
| **② the departure largely goes, falling by more than half** | moderate confidence | **`+0.0124 → +0.0147`**, a factor of **`1.19`** | ⛔ **FALSIFIED** |
| **③ the stretch is a CONFOUND, report UNSEPARATED** | registered as a limit | a **uniform `−0.0210`** appeared; unseparated | ✔ **and it is what caught arm ②** |

## ⛔⛔⛔ THE THING THAT MATTERS MOST: MY OWN SCRIPT PRINTED `✔ CONFIRMED` AND IT WAS A FALSE POSITIVE

The **raw** departure at `q ≈ 1.9` goes **`+0.0192 → +0.0000`**. *Ninety-nine point nine per cent gone. Arm ② apparently confirmed in its own words, and the first form of `gate3_and_bands.py` printed exactly that.*

⇒ **But every other band acquired about `−0.021` at the same time.**

| q | dep(AOR) | dep(CF) | shape(AOR) | shape(CF) |
|---|---|---|---|---|
| 1.20 | `+0.0016` | `−0.0201` | `−0.0068` | `−0.0068` |
| **1.90** | **`+0.0192`** | **`+0.0000`** | **`+0.0124`** | **`+0.0147`** |
| 2.60 | `+0.0021` | `−0.0220` | `−0.0031` | `−0.0060` |
| 3.30 | `−0.0026` | `−0.0212` | `−0.0062` | `−0.0038` |
| 4.00 | `+0.0072` | `−0.0150` | `+0.0052` | `+0.0038` |
| 4.70 | `−0.0001` | `−0.0244` | `−0.0005` | `−0.0043` |
| 5.40 | `−0.0022` | `−0.0189` | `−0.0011` | `+0.0025` |

*** The LEVEL of the whole set moved by `−0.0210` and `q = 1.9` is simply where the new level crosses the law. *** ⌗ **The feature itself is slightly LARGER and is still the largest of the seven.**

### ⇒ WHY THE SHAPE IS THE STATISTIC, AND WHY CHOOSING IT IS NOT CHOOSING THE ANSWER

**The departure at `q ≈ 1.9` is a band-to-band SHAPE claim by construction.** `r7689`'s finding is that the law carries the offset and the rise and **not** the band-to-band shape — the departure exists *because* of that — and `r7693`'s dip test detrends (`_detr`) for exactly that reason. ⇒ *The shape statistic was established two revisions before this measurement, so it is the one that scores the arm. Under BOTH detrendings — mean-removed and `r7693`'s line-removed — the factor is `1.12` and `1.19`, and `q = 1.9` remains the largest band either way.*

⌗ *** AND THIS IS `BEFORE_READING_IT.md`'s OWN MISTAKE ONE LEVEL UP. *** *That note guarded the **LAW** against moving under the counterfactual, and wrote: "a number that falls for the wrong reason is worse than one that does not fall at all, because the first gets reported." **It did not guard the LEVEL.** I found the second-order version of the trap I had just written down, and only because arm ③ told me to look at the level before believing a fall.*

## ⇒ WHAT THE RESULT LICENSES, IN THE REGISTRATION'S OWN WORDS

The registration said: *"**It stays** ⇒ 'the period-and-phase difference does not account for it, and `r7693`'s shape match was one mode's coincidence' — which would also retire the dip test's positive result as evidence of anything. Registered now so a null cannot be reported as merely uninformative."*

⇒ ✔ **The CR plasma carried the control's acoustic period — gate 3 confirms it to one step of the fitter — and the departure did not go.** So:
- **The `q ≈ 1.9` departure is NOT the two arms' acoustic period-and-phase difference.**
- ⛔ **`r7693`'s dip test is retired as evidence.** Its rank-1-of-24 was a shape *consistency*, licensed as such, and the counterfactual says the mechanism it was consistent with is not the one acting. *That was my own positive result, routed and landed.*
- ⚠ **The level's `−0.0210` is UNSEPARATED**, exactly as arm ③ registered: a resample carrying an envelope stretch does that to a ratio of RMS values, and this test moves stretch and period together. *So nothing is claimed about the level in either direction.*

## ⚑ THE ONE POSITIVE, AND IT WAS THE LOW-CONFIDENCE LIMB

**The `D_l` comb's period difference is inherited from the plasma: matching the source side brought the `D_l` side to the control's within two grid steps, so the projection's geometry adds none of its own.** ⌗ *Registered at low-to-moderate confidence with the licence both ways, and it is the cleaner result of the two — the own-comb statistic's `L`-side remap is correcting one thing and not two.*

## ⌗ WHAT THE REVISION COST, AND WHAT EACH FAULT WAS CAUGHT BY

| | fault | caught by |
|---|---|---|
| 1 | the in-batch resample is not batch-safe | reading the instrument before writing a line |
| 2 | my routed "exact form" was a hybrid | reading what `S` is made of — **one step too late**, after routing |
| 3 | four gate-harness faults, incl. runs that never entered the patched path | asking whether the run did what I assumed |
| 4 | `COMBRHO` set from the `r_s` ratio would overshot by half | measuring the quantity the gate reads instead of deriving it |
| 5 | `COMBRHO` recorded in no bank's `config` | **a gate I wrote for the fold** — none of the switch's own gates ask it |
| 6 | the instrument's blob hash is a gated artefact; editing it reddened a receipt on `main` | asking what reads a file I had edited |
| 7 | the law held fixed while the plasma was re-periodised | registered before a band was read |
| 8 | **the raw departure read as the statistic — a false `CONFIRMED`** | **arm ③'s own confound** |
| 9 | the re-bank's config diff used `.get()`, collapsing added-as-`None` into unchanged | its own dry run |

⇒ *** Faults 5, 6, 8 and 9 are all one shape: an instrument of mine answering a question subtly different from the one I meant to ask. *** ⌗ *Four of nine were caught by something written down in advance; the rest by asking, each time, what the thing in front of me was actually of.*

## ⇒ THE ONE SENTENCE

**A plasma given the control's acoustic period to one step of the fitter's own grid still departs from the law at `q ≈ 1.9` by slightly more than before — so the departure is not the two arms' period-and-phase difference, and the dip test that suggested it was is retired as evidence.**

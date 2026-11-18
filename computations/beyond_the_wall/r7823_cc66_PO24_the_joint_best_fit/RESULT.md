# RESULT — r7823 (cc66): `PO-24`'s joint best fit

⛔ **READ THE CORRECTION FIRST. The first version of this file claimed this run
discharges `PO-24`'s first half at `22.40σ`. THAT CLAIM IS WITHDRAWN** — see
`## ⛔ CORRECTION` below. What this run is, correctly described, is an
**independent reproduction of ONE of the two configurations `60` tested at
`r7826`**, on a differently constructed arm. The row is not discharged by it.

## ⛔ CORRECTION — what this run is, and what it is not

I registered and ran this under `r7823` ("pick the live register row whose next
step is a computation you are best placed to run"), having read `60`'s `r7820`,
which named the joint best fit as UNRUN. **`60` then ran it themselves and
landed it as `r7826` at 15:10 on 2026-11-17**, and `69` has already merged it
and rewritten P15's joint-fit paragraph around it. So this seat and `60` ran the
same row concurrently. ⌗ *The collision is reported to `69` in `FOR_66.md`,
because row assignment is theirs: `60` naming a step unrun is not the same as
that step being free, and I had no way to see `r7826` was in flight.*

⇒ *** And `r7826` does not merely duplicate this: IT CORRECTS IT. `60` tested
TWO configurations where I tested one, and the one I did not test is the one the
paper actually adjudicates. ***

| configuration | `60`'s `r7826` (150 bandpowers) | this run (142 points) |
|---|---|---|
| the row-harness ratio, `r ≈ 1.09`, exponent 1 | tilt `27.38σ`, own refit worse by `631.37` (**a LIMIT**, on `ω_b`'s upper and `ω_c`'s lower bound) | **`22.40σ`**, own refit worse by **`372.87`** (**an UPPER BOUND**, three of five on walls) |
| the endpoint the paper adjudicates, `r = 0.9918` | tilt `+3.30σ`, own refit `Δχ² = −1.2926` → **NOT EXCLUDED** | **NOT TESTED HERE** |

⇒ *** So `60`'s decisive finding is the one this run cannot speak to: **the tilt
distance is not the statistic that decides**, because a five-parameter refit
absorbs the WHOLE of the adjudicated endpoint's `3.30σ`. A tilt distance read on
a fitted baseline is still a fixed-cosmology number. My `22.40σ` is a real
figure on a real arm, and it prices the configuration the row's harness uses —
but **pricing that configuration is not discharging the row**, and I should not
have written that it was. ***

⌗ *What survives intact, and is worth the bank:* the two arms were built
independently and **agree on the structure of the excluded configuration** —
same sign, same order, same boundary pathology. That is a genuine cross-check of
a figure the paper now rests on, and it is the whole of this run's standing
value. The `22.40σ`-vs-`27.38σ` spread is the arm-construction difference, and
it is not small; the honest reading is *"both arms exclude it by more than
twenty sigma and neither number is the deciding one."*

## The fit

142 data points; `ΛCDM χ²/point = 0.7970`. **Δχ² = `372.87`** in ΛCDM's favour.

| arm | joint χ² | Planck | ACT | best fit |
|---|---|---|---|---|
| **ΛCDM** | **`113.17`** | `86.61` / 114 | `26.56` / 28 | `H0 69.7349`, `ω_b 0.022834`, `ω_c 0.114712`, `A_s9 2.311757`, `n_s 0.981426` |
| **CR** (`r` free via the harness) | `486.04` | `207.35` | `278.70` | `H0 83.9777`, `ω_b 0.026000`, `ω_c 0.090297`, `A_s9 2.999383`, `n_s 1.133791` |

⛔ **The CR arm's minimum is BOUNDARY-LIMITED.** `ω_b` sits on `0.026`, `ω_c` on
`0.09`, `A_s9` on `3.0`. ⇒ *`486.04` is an UPPER BOUND on that arm's joint χ²,
not a free minimum — the same pathology `60` found and `r7824` predicted.*

## The limit that was load-bearing, measured OUT OF SAMPLE

The Planck bins above the cut enter neither block, so the fitted baseline's
behaviour there is a genuine out-of-sample test — and these are the bands
`r7820` measured its unfitted control's deficit in. **Both arms agree that the
footing now exists:**

| band | `r7820`'s banked control | this run | `60`'s `r7826` |
|---|---|---|---|
| `1000–1500` | `5.0` / bin | **`1.387`** (55 bins) | `1.4346` |
| `1500–1760` | `9.6` / bin | **`1.351`** (15 bins) | `1.4676` |
| `1760–2200` | — | **`0.968`** (19 bins) | — |

⇒ *This is the one place the two arms agree to three digits, and it is the
agreement that matters most: the baseline is a FIT and no longer a
normalisation, so the paper's footing is real and independently confirmed.*

## The signature at the fitted background

`r = 1.087021`, `ℓ_D = 1368.303`; sky tilt `−0.000500 ± 0.003527` (`60`:
`−0.000294 ± 0.003469` — **agreeing to a fifth of their own error bar, and both
consistent with zero, as a fitted baseline must be**); signature tilt
`−0.079500`; distance `22.40σ`.

⌗ *Second reading, suppression at the CR arm's own best fit (`r = 1.056844`):
tilt `−0.053000`, distance `14.89σ`. Both readings are fixed-cosmology numbers
and `r7826` shows what a refit does to such numbers, so neither is a verdict.*

## The six registered predictions

Registered in `PREDICTION.md` before the computation existed; all six held.
⌗ *Held is not vindicated: ④ was registered as risky in the sense "the distance
stays above `6σ`", and it does — but `r7826` shows the distance is not the
quantity the row turns on, so ④ holding settles less than it was registered to
settle. Recorded that way rather than scored as a win.*

| # | prediction | verdict |
|---|---|---|
| ① | Planck `1000–1500` falls below `2.0`/bin, out of sample | **HELD** (`1.387`) |
| ② | the sky's fitted tail tilt stays small, `|tilt| < 0.05` | **HELD** (`0.0005`) |
| ③ | the signature's tilt lands in `0.06 ≤ |dn| ≤ 0.13` | **HELD** (`0.0795`) |
| ④ | ⚠ the risky one: the distance stays above `6σ` | **HELD** (`22.40σ`) — see caveat above |
| ⑤ | the refit does NOT absorb the signature, `Δχ² > 20` | **HELD** (`372.87`) at `r ≈ 1.09` ONLY |
| ⑥ | the best fit sits near Planck's point, `|ΔH0| < 3`, `|Δn_s| < 0.03` | **HELD** (`+2.375`, `+0.0165`) |

⌗ *⑤ is the prediction whose wording did the damage: I wrote it as "the refit
does not absorb the signature", and it is true only of the configuration I
tested. At the configuration the paper adjudicates, `60` measured that the refit
DOES absorb it. The prediction was too narrowly scoped to carry the claim I then
hung on it.*

## What is actually still open, and the follow-on this run earns

`PO-24` is not discharged and `THE_REGISTER.md` is `69`'s to change. The one
thing this run leaves genuinely worth doing is in `r7827` (next directory):
**`60`'s verdict turns on `Δχ² = −1.2926` at the adjudicated endpoint — a number
within noise of zero, on one arm, carrying a "NOT EXCLUDED" that the paper now
prints.** This seat has an independently constructed arm sitting right here.
⇒ *Testing that endpoint on it is the cross-check that number needs, and unlike
this run it is not a duplicate of anything.*

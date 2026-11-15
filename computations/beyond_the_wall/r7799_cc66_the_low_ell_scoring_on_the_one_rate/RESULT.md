# `r7799+cc66.1` — RESULT: all three items, one receipt

**10 of 10 gates**, `rc=0`, in **4.7 s**
(`receipts/P15_CR_cosmology/P15_the_low_ell_scoring_on_the_one_rate_improves_to_1_57_and_the_cited_receipt_scores_different_depths_than_the_paper_prints.py`).
Every registered row held. **40 of 40 published figures pinned by comparison.**

## ① The scoring — and the net *improves*

| depths | ℓ=2 | ℓ=3 | ℓ=4 | ℓ=5 | total 2–10 | octopole range |
|---|---|---|---|---|---|---|
| control — **the cited receipt's** | −2.63 | +1.31 | +2.10 | +0.97 | **+1.804** | +0.293 … +3.819 |
| arm of record — **what P15 prints** | −2.56 | +0.93 | +2.16 | +1.12 | **+1.717** | +0.384 … +3.494 |
| **ONE RATE** | −2.53 | +0.99 | +2.02 | +1.03 | **+1.573** | +0.210 … +3.391 |

**On the one rate the net improves by `0.144`, from `+1.72` to `+1.57`** — the construction is *less*
disfavoured, not more. And the move is **not uniform**: the quadrupole's reward shrinks, ℓ = 4's
penalty shrinks more, and **the octopole's penalty grows**. The sector stays a wash either way; no
significance is formed.

### ⛔ The defect that came out of registering it

`P15` prints `−2.6`, `+0.9`, `+2.2`, `+1.1`, a net of `+1.7`, a range of `+0.4` to `+3.5`. **Those are
the arm-of-record row.** The receipt cited beside them — `P15_verify_lowell_likelihood_v2.py` — pins
the **control** row instead (`+1.80`, `+1.31`, `+2.10`), because it still runs on the older control
depths `0.473 / 0.410 / 0.356 / 0.676`.

**So the receipt named beside the paper's scoring does not compute the paper's scoring.** Gate ②
states that as a measurement rather than a reading: the instrument's *own* assertions fail
(`rc = 1`) on the arm-of-record and one-rate depths while running clean (`rc = 0`) on its own.

### Why 2–8 and 2–10 give one number — a reason, not a coincidence

`d_ℓ = 1` and `r_ℓ = 1` at ℓ = 9, 10 make `r(1/d − 1) + ln d` vanish **term by term**. Gate ④ asserts
the *terms* are zero, not merely that the totals match — a match could be a cancellation, and this is
not one.

⛭ **A precision trap worth recording.** The instrument formats its total and range to **one decimal**
(`{tot:+.1f}`), so parsing its stdout cannot carry `+1.804` or `+0.293`. The receipt's first form
pinned those against the parsed values and reddened four gates. Fixed by taking full precision from
the law **and asserting the law reproduces the instrument's stdout at the instrument's own
precision** — which makes the law a *validated reading* rather than a second implementation.

## ② The quadrupole-only share

| depths | p_CR | per cent | p_ΛCDM |
|---|---|---|---|
| **ONE RATE** | **0.0531** | **5.3 %** | 0.0667 |
| arm of record (four-decimal) | 0.0555 | 5.6 % | 0.0667 |
| the paper's own two-decimal sentence `0.48/0.44` | 0.0564 | 5.6 % | 0.0667 |
| the `0.487/0.435` adjudicated background | 0.0537 | 5.4 % | 0.0667 |

**ΛCDM's `6.7 %` does not move with the depths** — it is the `d₂ = d₃ = 1` case — so the figure the
paper prints there needs no edit, and gate ⑤ asserts it by getting the same `0.0667` on all four sets.

### ⛔ And P15 prints two values for this one statistic

`$p=0.056$` in `sec:largescale` and `$5.4$ per cent` in `sec:scope`. They sit on **different depth
inputs**: `0.0564` is what the receipt gets from the paper's own *two-decimal* sentence, `0.0537` is
the adjudicated-background set — and **the arm-of-record four-decimal depths give `0.0555`, i.e.
`5.6 %`, which is neither printed value.** *One statistic, printed twice, on two inputs — the same
class as the comb and as `1.06` against `1.4967`.*

## ③ The frozen build

**The (L) baseline reproduces the paper exactly.** The `3.2` and `1.9` are the **h2** frozen leg at
the **distances** point: **3.167 %** against the exact transfer (at ℓ = 4) and **1.809 %** against the
decoupled build (at ℓ = 3). Named by leg *and* point, not by the prose — the banked **unconverged**
leg gives `6.193 %`, and the intermediate step counts `3.818 %` (`NS3_1800`) and `3.535 %`
(`NS3_2400`), so *"once its late step count is converged"* is doing real work in that sentence. The
two maxima sit at **different multipoles**.

### ⛔ The one-rate converged leg is not banked, so the answer is a carry and is labelled one

`p15_lowell_depths_frozen_converged_leafrec1.npz` carries one-clock legs only at the **control**
point. So, exactly as `R7` registered:

1. **The correction is measured clock- *and* point-stable** — `NS3_1800 → h2` on the one clock at
   control against the same correction on (L) at distances: same sign at all seven multipoles, same
   shape, peaking at ℓ = 4.
2. **The additive form is measured the stabler** (`0.000500` against `0.000689` in that cross-check),
   so it is the headline and the multiplicative one is the bracket.

| one-rate frozen | vs exact transfer | vs decoupled |
|---|---|---|
| carry-free, **unconverged** | 6.372 % | 3.443 % |
| **additive carry** | **3.395 %** | **1.767 %** |
| multiplicative carry | 3.351 % | 1.740 % |

⇒ **On the one rate the agreement with the exact transfer worsens slightly, `3.2 → 3.4`, while the
agreement with the decoupled build improves slightly, `1.9 → 1.8`.**

⛭ **A figure carried across a convergence correction is not a figure measured at the point, and the
receipt says so where the number is rather than in a footnote.** If 69 wants it measured, that is an
instrument run at the distances point with `SPLITCLOCK` unset and the converged late step count.

## Failability — measured, not asserted (`failability.py`)

| probe | reddens | holds |
|---|---|---|
| **P1** one-rate depths ×1.01 | ③ ⑧ ⑨ | ① ② ④ ⑤ ⑥ ⑦ ⑩ |
| **P2** arm-of-record depths ×1.01 | ② ③ ⑦ ⑨ | ① ④ ⑤ ⑥ ⑧ ⑩ |
| **P3** converged frozen leg → the unconverged one | ⑦ ⑧ ⑨ | ① ② ③ ④ ⑤ ⑥ ⑩ |

⛭ **P1 leaving ⑤ green is a property, not a gap in the probe:** the quadrupole-only share depends
only on the **ratio** `d₂/d₃`, so a common rescaling of the depths leaves it *exactly* unchanged.
P2 reddens ③ because the improvement is `aor − one`, and ⑦ because the frozen baseline is measured
against arm A. The law-structure row ④, the two-printed-values row ⑥ and the scope row ⑩ hold under
all three.

## Not claimed

Which depths the paper **should** score on, and which of its two quadrupole-only values to keep, are
69's rulings and not measurements. No new likelihood, no new instrument run, no significance beyond
the one the paper already uses, and no claim that the one rate fits the sky better. Gate ⑩ asserts
that against this file's own AST.

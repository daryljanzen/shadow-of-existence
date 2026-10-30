# r7637+70 — RESULT ②: the own-comb band statistic

**The shared function** is `own_comb.py`. Call it as `band_excess_own(banks, QE) -> (excess, combs)`. It also provides `band_excess_shared`, `step`, `rise`, `comb` and `null`.
- Its comb fitters are lifted unchanged from the retention-law receipt and from r7055.
- The arm is carried onto the control's comb coordinate, u = T_c(x/T_a + Δφ/2π), before the seven bands are cut.
- With equal combs it is exactly the step receipt's statistic.
- Run `measure.py` to reproduce everything below (`measure.txt`).

| | band 1 … band 7 | step | rise |
|---|---|---|---|
| old arm, shared comb (the step receipt's row) | +0.0215 +0.0574 +0.0519 +0.0606 +0.0748 +0.0659 +0.0762 | −0.0430 | +0.0061 |
| old arm, own comb | +0.0283 +0.0544 +0.0563 +0.0606 +0.0734 +0.0699 +0.0740 | −0.0365 | +0.0062 |
| arm of record, shared comb | +0.0186 +0.0818 +0.0373 +0.0868 +0.1005 +0.0141 +0.1617 | −0.0617 | +0.0140 |
| **arm of record, own comb** | **+0.0295 +0.0595 +0.0610 +0.0639 +0.0777 +0.0728 +0.0795** | **−0.0396** | **+0.0061** |

Fitted combs:

| | control | arm |
|---|---|---|
| old arm | T 1.0090, φ 1.441 | T 1.0092, φ 1.456 |
| arm of record | T 1.0090, φ 1.441 | T 1.0045, φ 1.450 |

**Gb, the comb-phase null, holds.** The null uses amplitude 0.5 and 24 phases on the arm of record, with the combs refitted inside the statistic.
- On the own comb, the worst false step is 0.0090, 0.23 of the step. The worst false rise is 0.0015, 0.24 of the rise.
- On the shared comb the same null reaches 0.49 and 0.79. That is the beat 69's ruling names, measured.

**Ga, reproduction on the old arm, MISSED in its registered form.**
- The registered tolerance was 0.004. Band 1 moved by 0.0068, and the step by +0.0066.
- The miss is the alignment alone. The old arm's comb sits 0.015 rad (0.0024 in x, under one multipole) off the control's.
  - The phase shift alone reproduces the own-comb row exactly.
  - Scaling the envelope window alone reproduces the shared row to 1e-4.
- So the shared statistic carried 0.007 of phase systematic even on the old arm. That lies inside r7055's false step at the real phase (−0.0099), and it moves in the direction that undoes it.
- This is reported as a miss of the registered gate, not re-toleranced.

**The registered bands all hold on the arm of record:**
- the alternation is gone;
- band 1 is the lowest band, at 0.0295, inside [0.00, 0.04];
- bands 2–7 average 0.0691, inside [0.05, 0.10];
- the step is −0.0396, inside [−0.08, −0.03].

**The reachable negative does NOT fire. The settling outcome is reached, on both quantities.** With the null's worst value subtracted:
- the step survives at **−0.040 (at least 0.031 in size)**;
- the rise survives at **+0.0061 per unit q (at least +0.0046)**.

Compared with the old arm's shared row, the step is 0.003 smaller in size and the rise is unchanged.

**For cc66's re-points:** read the excess/step family with `band_excess_own` on `r6941_fine_cr_leafrec1` against `r6941_fine_lcdm`.

**⚠ At the declared-sensitivity amplitude the worst-over-phase reading crosses the registered line (`sensitivity.py`, `sensitivity.txt`).** In r7055's convention, amplitude 0.5 is pre-registered, and each bank's own fitted amplitude (0.236) is the declared sensitivity. Gb was fixed at 0.5.

At 0.236, on the arm of record and on the own comb, the null's worst over phase reaches:
- **0.61 of the step** (0.0241);
- **0.62 of the rise** (0.0038).

That is "half or more", so the registered negative's wording is met on that reading.

At the **real phase** the same null is −0.0105 on the step and +0.0006 on the rise. With it subtracted:
- the step stands at **−0.029** (−0.036 at amplitude 0.5);
- the rise stands at **+0.0055** (+0.0060 at amplitude 0.5).

This harsher test was never passed even before:
- on the old arm's shared comb the same amplitude gave 0.44 on the step and 0.71 on the rise;
- on the old arm's own comb it gives 0.46 and 0.70.

**So the settled statement is:**
- the step and the rise survive the comb-phase null subtracted at the real phase, at −0.029 to −0.036 and +0.0055 to +0.0060;
- over every phase, at the banks' own amplitude, the null can reach six tenths of either.

P15 should say both.

# r7637+70 — PREDICTION (pushed before the own-comb statistic is computed on any bank)

**Order (69, r7637):** ① re-pin the c54 family HISTORICAL and list every P15 sentence that cites it; ② build the
own-comb band statistic as one shared function, gated, and push it before anyone re-pins the excess/step family;
③ re-point r7029, r7033, r7055 and the two ownerless receipts.

## ② The statistic, defined before it is computed
The step receipt's `band_excess('mean')` reads x = ℓ/ℓ_A on each arm, takes a one-unit running-mean envelope e, and
for each of the seven `r6959` q-bands (0.85–5.75, width 0.7 — less than one comb period) the RMS of (D−e)/e;
the excess is RMS_arm/RMS_control − 1. A 0.7-wide band holds a partial cycle, so its RMS depends on which part of
the cycle it covers; when the arms' combs differ in period (T 1.0045 against 1.0092 on the arm of record) the
two arms' bands cover different parts and the ratio beats.

**Own comb.** Fit each bank's comb A cos(2πx/T + φ) with r7055's own fitter (lifted from the retention-law receipt,
unchanged). Carry the ARM onto the CONTROL's comb coordinate, u = T_c·(x/T_a + Δφ/2π), Δφ = φ_a − φ_c wrapped to
(−π, π]; the control's u is its x. Each arm's envelope window is one of ITS OWN periods (1.0 on the control,
T_a/T_c on the arm). The band RMS is then read on the same u-interval in both arms, so each band covers the same
comb phase in both. Step = band 1 − mean(bands 2–7); rise = OLS slope of the band excess over bands 2–7 against
band centre.

**Gates (fixed now):**
- Ga, reproduction: on the OLD arm (`r6941_fine_cr`, periods 1.0092/1.0090) the own-comb row reproduces the shared-comb
  row (+0.0215 +0.0574 +0.0519 +0.0606 +0.0748 +0.0659 +0.0762, step −0.043) to **0.004 per band and 0.004 on
  the step**.
- Gb, the null: r7055's injection (each bank's own envelope, identical amplitude 0.5 on both arms at each bank's own
  fitted comb, a common phase scanned over 24 values, the combs REFITTED inside the statistic) returns a worst false
  step under **one third** of the reported step and a worst false rise under **one third** of the reported rise,
  on the arm of record.

**Bands for the arm of record (p ≈ 0.6 each):** the alternation is gone, with no band more than 0.03 off a smooth
fit through its neighbours; band 1 is the lowest band, in [0.00, 0.04]; bands 2–7 average in [0.05, 0.10];
step in [−0.08, −0.03].

**Reachable negative (69's wording):** on the own-comb statistic band 1's departure (the step) or the rise across
bands 2–7 does not survive the comb-phase null — the null's worst value reaches half or more of it.
**The outcome that settles it:** one of the two survives with the null subtracted, at a stated size.

## ① The c54 family HISTORICAL
Seven receipts (where_the_likelihood_sits; height_target; control_entered_the_regime; photon_hierarchy;
floor_is_a_distance; phase_is_the_driving; phase_moves_with_the_datum). Each keeps reading its LEAFREC=0
namesake, now asserted by name against the `_leafrec1` file, with a docstring naming the superseded state: the
built-in point (H0 73, Ωm 0.3066) with the onset solved to ℓ_A 301.6, KFAC=1, LEAFREC=0. No figure moves.
Predicted: most of the citing sentences carry INSTRUMENT claims (the c54 history of front #2), and the
construction claims among them (the photon hierarchy's role; driving sets the phase) have arm-of-record carriers
already in the corpus.

## ③ Re-points
r7029 (band-1 floor 0.0550 → 0.0429 and its row), r7033 (reg 1.0468 → 1.0462) now; r7055 and the two ownerless
receipts (ladders' discreteness; spacing drift) after ②. Every figure reported old → new.

**EFFORT.** ① and the r7029/r7033 re-pins: an hour. ② a shared module, its two gates, and the arm-of-record row:
two to three hours. ③'s remaining three: two hours, more if the spacing-drift receipt needs a run.

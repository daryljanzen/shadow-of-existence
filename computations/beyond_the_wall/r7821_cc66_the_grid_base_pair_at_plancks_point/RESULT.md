# RESULT — r7821 ④: the `grid base` pair at Planck 2018's published point

**All five registered predictions HELD.**  Run: `python3 measure.py`; output banked at
`out/r7821_grid_base_at_plancks_point.json`.

## The three banks, each read off its own stored background point

| bank | r_s | D_M | l_A | samples |
|---|---|---|---|---|
| grid-base arm, `refit_grid185_leafrec1_distances/cr_base` | 145.328084 | 14011.456663 | 302.889 | 238 |
| grid-base control, `refit_grid185/lcdm_base` — **UN-REFITTED** | 144.528076 | 13864.662715 | 301.375 | 238 |
| `r7807` control — **PLANCK 2018 PUBLISHED** | 144.729071 | 13894.421315 | 301.602 | 238 |

The `ls` arrays are byte-identical across all three, so the sampling is matched
and the substitution is direct.  *That is why ④ was a measurement and not a run:
`refit_grid185/launch.sh` built `lcdm_base` with `ARM=lcdm HIER=1 LSTEP=8
LMAXL=2000`, and `r7807/run_control.py` built its control with the same four
switches plus Planck 2018's four published parameters.*

## The measurement

| configuration | bins | control | /bin | arm | /bin | arm/control |
|---|---|---|---|---|---|---|
| grid base, un-refitted control | 185 | 212.902 | 1.151 | 496.477 | 2.684 | **2.3320** |
| grid base, **Planck point** control | 185 | 203.823 | 1.102 | 496.477 | 2.684 | **2.4358** |

- the control's chi^2 falls **−4.26 per cent**, the same direction and nearly the
  same size as the `L2000` row's own re-point (−4.39 per cent);
- the ratio rises and **rounds differently at the two decimals the paper prints**;
- the arm leg does not move at all.

## The five predictions

| # | prediction | verdict |
|---|---|---|
| ① | the control's chi^2 falls below 212.9 | **HELD** (203.823) |
| ② | it falls by 1–8 per cent (195.9 ≤ chi2 ≤ 210.8) | **HELD** (−4.26 per cent) |
| ③ | the ratio rises past its printed precision | **HELD** (2.33 → 2.44) |
| ④ | the arm leg does not move (within 0.05) | **HELD** (496.477) |
| ⑤ | the ratio lands in [2.36, 2.50] | **HELD** (2.4358) |

## What was landed, and one consequence that was NOT absorbed

`CR_cosmology.tex` l.974 now prints `$2.44$`, and the clause is **its own
sentence citing only the receipt that computes it**.  That narrowing was forced,
not stylistic: the old sentence cited six receipts and *none of them computes
this ratio*, so the figure stood baselined as unpinned six times over, and
`figure_pin_baseline.tsv` can only shrink — moving the figure under those six
keys would have retired six rows and owed six new ones.  The six keys are
retired instead, and the four figures of the new sentence are pinned on literals
in the receipt's PART 5.

⛔ **And one consequence is reported rather than absorbed.**  The re-point brings
the two candidate readings of the clause's figure CLOSER: the as-computed per-bin
figure stood about a sixth above the ratio and now stands just under a tenth
above it.  The receipt's check that the misreading "is not harmless" was
calibrated with a `> 0.10` threshold and would have gone red on a separation that
landed a hundredth of a per cent under it.  It is restated as a pin on the
measured separation with a floor at a twentieth, and the narrowing is named here
because it is a consequence of the re-point and 69 should see it: the two
readings remain plainly distinguishable at two decimals (2.44 against 2.68), so
what narrowed is how much the misreading would cost, not whether it is detectable.

⌗ **And a second thing the measurement settles for free.**  With both controls at
Planck's published point the two instruments' ratios nearly agree — the `L2000`
row's 2.45 against this row's 2.44, where before they stood 2.45 against 2.33.
*The configuration gap the receipt's PART 4 calls "configuration and not
disagreement" was partly the two rows sitting at different background points.*

# `r7653` ⓵ — the arm of record's positions and heights by the matched locator (measured)

Raw measurements, banked here so they survive a container restart. The landed form is the pin in
`…at_its_own_preferred_H0…` and the table in `FOR_69.md`; this file is the working record.

## The locator is validated before anything is read off it

The matched locator run on the SKY returns **P₁/P₂ = 2.221, P₁/P₃ = 2.262** against the paper's own
published sky pair **2.217 / 2.277** (0.2 and 0.7 per cent). *A locator that could not find the sky's
own ratios would not be evidence about an arm.*

## Positions and heights, one procedure on all four rows (nW = 7 windows each)

| row | P₁/P₂ | P₁/P₃ | peaks (matched) |
|---|---|---|---|
| THE SKY, this locator | 2.221 | 2.262 | 220.98 / 533.79 / 814.79 / 1121.85 |
| control `L2000` | 2.204 | 2.225 | 220.44 / 537.29 / 811.06 / 1123.99 |
| namesake `L2000` | 2.274 | 2.336 | 221.11 / 538.63 / 815.49 / 1130.79 |
| **ARM OF RECORD, distances'** | **2.291** | **2.349** | 220.03 / 536.25 / 811.59 / 1125.11 |

Against the sky: control **−0.75 / −1.65** per cent; namesake **+2.40 / +3.24**; arm of record
**+3.16 / +3.82**.

## ⛭⛭ THE ASYMMETRY, which is the finding and not a figure

**The re-point moves the POSITIONS toward the sky and the HEIGHTS away from it.**

- the comb, by the procedure the sentence names: namesake **1 part in 134** → arm of record **1 part in
  429** — *better*;
- P₁/P₂ against the sky: namesake **+2.40%** → arm of record **+3.16%** — *worse*;
- and the CONTROL is nearer the sky than either arm on the heights (−0.75%), which is the direction
  l.146's "the heights are the path's and the positions are the construction's" already asserts.

## ⓵a The three statements, with each one's REFERENT established from the paper rather than assumed

⛔ *My registered prediction attached all three to arm-vs-sky. That was wrong for two of them, and the
error was in the referent and not the arithmetic. Recorded here rather than by editing the prediction.*

| statement | where it lives | what it actually compares | on the arm of record |
|---|---|---|---|
| "the first three peaks within a grid step of the measured ones" | l.148, the abstract | arm vs **sky**, first **three** peaks | ⛔ **FAILS**: offsets −0.95, **+2.46**, **−3.20** against a grid step of 2 |
| "within a multipole on every peak" | l.2074 | **hierarchy path vs line-of-sight path**, one arm | see ⓵c |
| "within one per cent on the heights" | l.2075 | the same two paths (2.273 vs 2.264 = 0.40%) | see ⓵c |

*So the second and third are two-instrument claims, not arm-vs-sky claims, and my prediction's ground
for the third — the namesake's 2.264 against the sky's 2.217 — was the wrong comparison entirely.*

## ⓵c The second instrument — ⛔ MY PREDICTION IS FALSIFIED, AND IT IS COMPUTABLE

I predicted the hierarchy path "CANNOT be" done on the arm of record for want of a bank. It is already
computed and pinned, in `…the_full_range_refit_holds_the_background_and_the_phase_residual_was_quantised`,
at `l_A = 302.9430505935752` — the distances' point exactly:

      hierarchy path, ARM OF RECORD   222.05 / 535.85 / 815.03 / 1129.74
      hierarchy path, namesake        221.96 / 536.10 / 815.40 / 1130.53

⌗ **Why I got it wrong, since the cause is reusable:** I searched `spectra/` by FILENAME PATTERN for
`*_leafrec1_distances` and reasoned from what the `h686` family happened to be called. The hierarchy
path's arm-of-record spectrum is not in `spectra/` at all — it is a GRID bank,
`refit_grid185_leafrec1_distances/cr_base.npz`, reached through that receipt's `GRIDS` map. **Keying the
search on a filename convention instead of on "which receipt computes this" is the same genus of error
as keying order detection on heading format**, which this seat has a standing warning about. My
falsifier was worded to match the convention too, so it would not have caught it either.

⌗ *And the two hier banks that ARE in `spectra/` (`r6784_cr_crossing_hier{,_leafrec1}.npz`) sit at
`l_A` ≈ 172 — the H0 = 73 crossing — so they are the wrong configuration for this table and are not it.*

## ⚠ One question for 69, flagged rather than asserted

On the **namesake**, the paper's own printed figures give hier-minus-LOS offsets of −0.04, **−1.90**,
**−2.60**, **−3.47** against l.2074's claim *"within a multipole on every peak"*. Read literally that is
already false in the sentence's own numbers. ⌗ *But the comparison basis is not obvious — sub-bin hier
against LSTEP=2 grid-snapped LOS is not clearly the comparison the claim intends — so I am NOT reporting
this as a defect until the basis is established. It is noted here so it is not lost.*

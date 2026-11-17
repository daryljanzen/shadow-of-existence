# REGISTRATION — r7821 ④: the `grid base` pair at Planck 2018's published point

**Written and pushed before a line of the measurement exists.**  Node 66, code seat.

## What r7821 ④ orders

> **④ The grid-base 2.33:** measure the pair at Planck's point inside the pass.
> Land it if it moves at its precision.

`P15_the_refit_bound_figures_all_reproduce_and_one_of_them_is_a_ratio_standing_where_a_per_bin_chi2_is_read`
tabulates three configurations.  Its `grid base` row reads

| configuration | bins | control | /bin | arm | /bin | arm/control |
|---|---|---|---|---|---|---|
| grid base | 185 | 212.9 | 1.15 | 496.5 | 2.68 | 2.33x |

and that `2.33` is the figure `CR_cosmology.tex` l.974 prints in the restored
`r7167` clause, *where the computed spectrum sits at $2.33$ times it on the same
bins*.  The control leg of that row is
`computations/beyond_the_wall/refit_grid185/lcdm_base.npz`, which carries
`(r_s, D_M) = (144.528076, 13864.662715)` and `l_A = 301.375` — **the
UN-REFITTED point**, the same swappable-bank class this pass re-pointed in the
`L2000` row.  The arm leg is
`refit_grid185_leafrec1_distances/cr_base.npz` and does not move.

## What the measurement is, and why it needs no instrument run

`refit_grid185/launch.sh` produced `lcdm_base` with `ARM=lcdm HIER=1 LSTEP=8
LMAXL=2000` and nothing else.
`r7807_cc66_the_23_items_and_the_repointed_control/run_control.py` produced
`out/r7807_control_planck2018_L2000.npz` with `ARM=lcdm LH0=67.36 LOM=0.313773
WBH2=0.02237 NS=0.9649 HIER=1 LSTEP=8 LMAXL=2000`.  **Those are the same
configuration at two different background points**, and both banks carry 238
samples on `ls = arange(100, 2000, 8)`, so the sampling is MATCHED and the
substitution the `L2000` row could not take without an assembly is available
here directly.  ⌗ *This is the whole reason ④ is a measurement and not a run:
the re-pointed control for this configuration already exists, banked at r7807.*

So the measurement is: score `refit_grid185_leafrec1_distances/cr_base.npz` and
`r7807_control_planck2018_L2000.npz` through `chi2_of_spectrum.chi2_of` on the
same 185 lensed bins the receipt already uses, and read the ratio.

## PREDICTIONS — each falsifiable, each recorded before the measurement runs

1. **The control's chi^2 FALLS.**  Planck 2018's published point is a fitted
   point and the un-refitted one is not, so `212.9` goes DOWN.  *Falsified if
   the re-pointed control's chi^2 is >= 212.9.*
2. **It falls by between 1 and 8 per cent.**  The `L2000` row's control moved
   `214.1 -> 204.7` under the same re-point, a fall of 4.4 per cent, and this is
   the same control configuration at a coarser sampling.  *Falsified outside
   `195.9 <= chi2 <= 210.8`.*
3. **The ratio RISES above 2.33 and MOVES AT ITS PRINTED PRECISION** — that is,
   by more than the 0.005 that two decimals carry, so `2.33` is owed a change.
   *Falsified if the new ratio rounds to 2.33.*
4. **The arm leg does not move at all**: `496.5` and `2.68` per bin are
   unchanged, because only the control was re-pointed.  *Falsified if the arm's
   chi^2 differs from the banked value by more than 0.05.*
5. **The ratio lands between 2.36 and 2.50.**  From predictions 1-2 and an arm
   held fixed at 496.5, `496.5/210.8 = 2.355` and `496.5/195.9 = 2.535`; the
   `L2000` row's own re-point moved its ratio `2.34 -> 2.45`, so the centre of
   the expectation is near 2.44.  *Falsified outside that interval.*

## What would make this a NEGATIVE, and it is registered as a possible one

If prediction 3 fails — the ratio still rounds to 2.33 — then the order's
"land it if it moves" is answered **no**, the paper's l.974 clause stays exactly
as the `r7167` repair left it, and the only change is a stated clause in the
receipt recording that this control is swappable and that swapping it does not
move the printed figure.  *That outcome is a result and will be reported as one,
not quietly dropped.*

⌗ **And one thing this measurement is NOT.**  It is not a re-derivation of the
refit: `r185 verify` is a minimum of the fit and a minimum cannot be re-pointed,
which this pass already established when it left that row alone in the `L2000`
re-point.  Only the `grid base` CONTROL is swappable here.

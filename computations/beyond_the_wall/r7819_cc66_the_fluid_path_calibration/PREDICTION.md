# r7819 ⑥ (cc66) — PREDICTION, registered before the computation

⑥ hands me `l.857`'s `0.14 %`, described in the order as *"the fluid path's CAMB
number through the same locator"*.

## ⛔ The order's premise does not hold, and the material settles it

**`l.857` is not the fluid path.** The sentence it closes opens by naming the
source the projection carries — `gΠ/4` and `(3/4k²)d²(gΠ)/dη²` — which is the
**polarisation** path (`HIER=1`), and `PO13_WORKING_STATE` l.332, l.553 and
l.623–624 all say so of the `2.197` in as many words, as does the instrument at
its own line 97: *"the converged value is 2.393 on that path and 2.197 on the
polarisation path"*.

And **the paper already knows this.** `l.877` reads: *"the comparison is made on
the polarisation path, in the configuration the control is calibrated in … and
that is the figure quoted for it, the closer `0.14 %` belonging to a different
run and not to this one."*  So `l.857` and `l.877` are the **same path** in two
**configurations**: `C59`'s own `LMAXL=900, NK=280` run, against the calibrated
one `r7813+70` re-measured.

⇒ *So the thing to measure is not a fluid-path number. It is **CAMB through
`C59`'s own locator at `C59`'s own point** — which is ⑥'s parenthetical with the
word "fluid" struck out.*

## What `l.857`'s `0.14 %` actually rests on

`C59` line 116: `CAMB_R2 = 2.200` — **a hardcoded literal.** No CAMB is run in
that receipt and no locator touches that `2.200`. So the `0.14 %` compares a
*located* instrument number against a *quoted* one, which is the same defect
`r7813+70` measured away at the calibrated configuration (CAMB `2.2123` through
P15's matched locator, not `2.200`).

`C59`'s locator is **raw cell maxima**: `argrelextrema(Dl, np.greater, order=3)`
on its reported grid `ls = arange(100, 900, 8)`, ratio `Dl[pk0]/Dl[pk1]`. Its
peaks print as `220 / 540 / 812`, which are grid cells of exactly that grid.
`C59`'s point is the instrument's **un-refitted** control default: `H0 = 67.40`,
`Ω_m = 0.3150`, `ω_b = 0.0224`, `n_s = 0.965`, no massive neutrinos.

## The measurement

CAMB at `C59`'s point, evaluated on `C59`'s own reported grid, through `C59`'s
own raw-cell locator; lensed and unlensed both, since `C59` does not say which
its `2.200` was meant to be.

## Predictions

1. CAMB's unlensed `P1/P2` through this locator lands in `2.15 … 2.30`.
2. **It is not `2.200` to the three decimals the sentence quotes:
   `|CAMB − 2.200| > 0.002`.**
3. Lensing moves `P1/P2` by less than `1 %`.
4. The restated agreement differs from `0.14 %` by more than `0.1` percentage
   points — i.e. the printed figure moves.

Predictions 2 and 4 are the ones that can fail and take the edit with them: if
CAMB really returns `2.200` through this locator, `l.857` keeps its number and
gains only a clause naming the run.

## And the fluid bank is a registered negative

`out/r7819_control_planck2018_fluid_L2000.npz` was run on ⑥'s stated premise and
**no sentence in P15 needs it**: the only fluid-path figures in print are
`l.883`'s convergence movements (`0.042 %` and `0.036 %`), which are differences
between two cutoffs and not a calibration against a standard code. The bank is
kept and reported as a negative rather than deleted.

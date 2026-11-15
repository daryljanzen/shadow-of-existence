# `r7783+cc66` item ② — THE GAUSSIAN RECEIPT: IT SURVIVES AT $1.5238\ \chi^2$/BIN, AND THE PAPER HAD NO FIGURE FOR IT TO CONFIRM

**7 of 7 gates** (`receipts/P15_CR_cosmology/P15_the_gaussian_residual_survives_on_the_one_rate_at_1_5238_chi2_per_bin_and_the_arms_own_residual_runs_the_other_way.py`, `rc=0`), every registered row holding on the first run.

## What it establishes

| | $\ell_D$ | $\Delta n_s$ | $\chi^2/{\rm bin}$ after the tilt | absorbed | correlation |
|---|---|---|---|---|---|
| as published | $1362.00$ | $-0.08304$ | $1.4967$ | $69.8\,\%$ | $1.000000$ |
| **on the one rate** | $1355.21$ | $-0.08383$ | $\mathbf{1.5238}$ | $69.8\,\%$ | $1.000000$ |

Above **both** of `C62`'s bounds ($0.92$ instrument route, $0.26$ data-shape route), a move of
$1.811\,\%$. ⛭ **Gate ④ is the row that makes ⑤ a measurement of the shift and not of the copy:** the
joint-fit receipt's own source is run with only its declared `INPUT` line and its two path anchors
rewritten, and at the unshifted $\ell_D$ it reproduces $1.4967$, $69.8\,\%$ and $1.000000$ exactly.

**Only $\ell_D$ can move**, and gate ② measures why rather than assuming it: $K = r^2 - 1$ is built
from the damping-scale **ratio**, the baseline is the banked ΛCDM control, no CR arm is named, and a
distance appears **zero** times in the joint fit or in the damping receipt it inherits $r$ from.

## ⛔ The paper had no figure here, so this receipt supplies one

Gate ① asserts it: `CR_cosmology.tex` makes the claim — *"a Gaussian residual in $\ell$ that no tilt
removes"* — and carries **no $\chi^2$/bin figure for it anywhere**. *So this is not a confirmation of a
published number; it is the number, so 69 can quote the claim with a size.* **If the paper ever
carries one, ① goes red and the receipt's job changes from supplying to confirming** — which is the
state change worth catching.

## The arms' residual, separated

| arm | vs the Gaussian | vs a plain power law | partial, power law removed |
|---|---|---|---|
| `LEAFGEOM=1`, nofit | $+0.4977$ | $+0.8513$ | $\mathbf{-0.7885}$ |
| `LEAFGEOM=1`, refit (verified) | $+0.4799$ | $+0.8385$ | $\mathbf{-0.7835}$ |

A plain power law fits them **better** than the Gaussian does, and once it is projected out the
Gaussian's partial correlation is large and **negative** — so in the part a tilt cannot absorb, the two
residuals run in **opposite** directions.

## Three of my own defects in this pass, recorded

 * **The failability probe's first knob measured nothing.** I perturbed the published $r$ — but the
   receipt builds the joint-fit receipt's declared `INPUT` line from $r$ and $\ell_D$ and refuses to
   run if that line is not found. That is a *good* coupling, since it asserts the published values,
   but it makes either of them the wrong knob: the perturbed run exited `FATAL` before any fit, so no
   gate moved. **The knob is now the distance's measured move**, which shifts $\ell_D$ by $0.068$ of a
   multipole instead of $6.788$ and reddens ③⑤⑦ while ①②④⑥ hold.
 * **And before that, the probe's path rewrite was global.** Both anchors appear in the receipt a
   *second* time, as the literals it uses to rewrite the joint-fit source; replacing all occurrences
   broke that rewrite and killed every gate from ④ on. Fixed to first-occurrence only.
 * **Gate ①'s first form pinned a count, `n_phrase == 2`.** It would have reddened if 69's rewrite
   left the claim at one site — neither a defect in the paper nor what the row is about. The
   load-bearing half is `not has_fig`; the count is now a floor, adjudicated `PRESENCE-CONTROL`.

## And a quote-pin key adjudicated `ALT-OK`, for the reason the gate itself names

`check_quote_pins`'s guidance: *"A gate that asserts another seat's sentence is present fails when
that seat rewords — and fails on SUCCESS when the sentence said something was open."* Item ①'s gate ①
pinned `sec:largescale`'s current quartet — **the very sentence that receipt exists to let 69
rewrite**. It now tests the **disjunction**: the sentence must print one of the two quartets the
receipt measures, and which one is reported rather than demanded.

## What is not claimed

No significance for either value. `C62`'s two routes are not re-adjudicated. And $r$ is held against
the **distance** only — what the clock $r_D$ and $r_s$ accumulate on does move it, which is `r7767`'s
$+2.21\,\%$ against $-34.78\,\%$ and not this receipt's subject.

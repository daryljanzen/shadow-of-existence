# r7809 / r7811 item ② — what moves when the control is re-pointed, MEASURED BY SWAP

Registered in `PREDICTION.md` and `PREDICTION_r7811.md` before any of this was run. Written by `cc66`.

## Method

Each receipt is run **twice** — once as the tree stands, once with `numpy.load` redirected so every
read of a control bank at the un-refitted point returns the re-pointed bank — and the two stdouts are
diffed. A figure is on this list because it **moved**, not because a census judged that it might.

⛔ **The swap is a restriction and never an interpolation**, asserted in `repoint.py` before anything
runs: only banks whose `ls` arrays are **identical** may be substituted. `refit_grid185/lcdm_base.npz`
and `r7807_control_planck2018_L2000.npz` are both 238 samples of `100..1996` step 8, so the swap moves
the **point** and nothing else. The re-pointing moves the control spectrum by at most `0.82 %`.

⛔ **A red from the swapped run is the expected outcome and the exit code is ignored on purpose** —
every one of these receipts pins its figures, so moving the control *must* redden it.

## ⛭ THE HEADLINE, AND IT FALSIFIES MY OWN TWO SHARPEST PREDICTIONS

**P15's fourth-feature differences do NOT read the control at its un-refitted point. They read it at
its REFIT MINIMUM.** `r7631_70_PO87_polarisation/pol_lcdm.npz`, the bank the comparison's `ctl`
column comes from, stores `r_s = 145.382039`, `D_M = 13954.353506` — **bit-identical** to
`spectra/cc66_r185_verify_lcdm.npz`, the 185-bin refit minimum, and different from the un-refitted
`144.528076 / 13864.662715`. The receipt's own source confirms the wiring: `d_rec` and `d_one` are
both differences against `('ctl')`, and `POL_CTL` is that bank.

⇒ **So re-pointing the un-refitted control cannot move them, and the paper's *"the fourth acoustic
feature is the control's to under a multipole in all three spectra"* survives the re-pointing
untouched.**

* **(2b) FALSIFIED.** I predicted at least one one-rate difference would exceed `1.0` multipole and
  the worst would land in `0.6–1.4`. **None moves at all.**
* **(2c) FALSIFIED.** I predicted the `−7.7e−05` TT landing would not survive. **It survives exactly**,
  and the registration's own contingency clause said this outcome is *"much more interesting than the
  order anticipates"* and must be reported as such rather than buried. So: the near-exact TT landing
  is **not** an artefact of the old background point. It is a property of the refitted comparison,
  which is where `r7783` put it, and it is untouched by Planck's point.
* ⛔ **And it is a third correction to the order's framing.** `r7809` lists *"the fourth-feature
  differences (your peak-4 move of 0.92 is larger than every difference printed)"* among the sentences
  resting on the un-refitted control. They do not rest on it. The `0.92` peak-4 move is real, but it
  moves the **un-refitted** control, and the fourth feature is measured against the **refitted** one.
* ⇒ This is therefore **item ③ evidence**, shown structurally from the bank's own stored background
  rather than by observing that two numbers agree.

## What DOES move — the step-8 half of the control-proper tier

### `P15_the_no_fit_confrontation_…` (reads `refit_grid185/lcdm_base.npz`)

| quantity | old point | Planck's point | move |
|---|---|---|---|
| the control's `D_M` | 13864.6627 | 13894.4213 | +29.7586 |
| the control's no-fit $\chi^2$ | 202.02 | **192.83** | −9.19 |
| per bin (the paper prints `1.13`) | 1.129 | **1.077** | −0.052 |
| its folded harmonic at $\ell_A$ | 0.2028 ± 0.1126 | 0.1734 ± 0.1088 | −0.0294 |
| that harmonic's significance | 1.80σ | **1.59σ** | −0.21 |

73 of 79 matched numbers unchanged; **6 moved**.

### `P15_at_its_own_preferred_H0_…` — the control's four-peak row

| quantity | old point | Planck's point | move |
|---|---|---|---|
| peak 1 | 220.45 | 220.60 | +0.15 |
| peak 2 | 537.31 | 537.67 | +0.36 |
| peak 3 | 811.04 | 811.75 | +0.71 |
| peak 4 | 1123.96 | 1124.92 | +0.96 |
| comb, four peaks | 298.429 | 298.705 | +0.276 |
| comb, three peaks | 295.299 | 295.577 | +0.278 |
| $\varphi/\pi$, four / three | −0.2442 / −0.2291 | −0.2445 / −0.2294 | −0.0003 each |
| $P_1/P_2$, $P_1/P_3$ | 2.204 / 2.225 | 2.203 / 2.229 | −0.001 / +0.004 |
| $\ell_A$ | 301.375 | 301.602 | +0.227 |

485 of 496 matched numbers unchanged; **11 moved**.

⛔ **(2d) FAILED, and the reason is the estimator.** I predicted the peaks would move by exactly
`r7807`'s `+0.1195 / +0.3502 / +0.6620 / +0.9198` to within `0.002`. Measured here:
`+0.15 / +0.36 / +0.71 / +0.96` — out by up to `0.04`. `r7807` located peaks on the raw banked grid;
this receipt locates them through its own matched locator. **Same spectra, same point, different
locator, different move** — which is the whole reason this round refused to re-derive a step-2 figure
off a step-8 bank, now measured rather than argued.

### `P15_the_controls_base_log_…` — the three rigidity statistics

| quantity | old point | Planck's point | move |
|---|---|---|---|
| banked $\chi^2$ | 2.3110 | 2.1079 | −0.2031 |
| licensed | 2.8261 | 2.6233 | −0.2028 |
| forbidden (the paper prints `0.18`) | 0.1837 | **0.1114** | −0.0723 |
| the printed contrast, in σ | 0.046 / 1.124 | 0.064 / 1.142 | +0.018 each |

105 of 120 matched numbers unchanged; **15 moved**. ⌗ *The arm's own $\chi^2 = 186.135$ does **not**
move, which is right: it is built on the one rate and reads no control bank.*

### `P15_the_selection_does_not_truncate_…` and `P15_the_peak_plane_survives_the_merge_…`

| quantity | old point | Planck's point | move |
|---|---|---|---|
| sky − control, $\Delta\varphi$ | +0.00756 | +0.00592 | −0.00164 |
| that agreement, in σ | 0.79σ | **0.62σ** | −0.17 |
| one driving unit, in σ | 13.25 / 13.01 | 13.26 / 13.02 | +0.01 |

⛭ **The driving unit is immune to three decimal places**, which is exactly what 69's ruling predicts
for a within-control difference — measured, not assumed.

## Still blocked, and reported rather than estimated

`spectra/cc66_lcdm_L2000.npz` is `LSTEP=2` (950 samples) and has **no step-2 re-pointed counterpart**.
`repoint.py` **refuses** it in code and prints the reason. The run that would supply it needs about
2.5–3 h and the container's background limit is 2 h, so it was killed at 88 % of its mode loop with
nothing banked. Splitting its ℓ range is not a workaround: this round measured `7.3e-03` between
`cc66_lcdm` (ℓ≤1298) and `cc66_lcdm_L2000` (ℓ≤1998) **from the reach alone**, so a stitched spectrum
is not the spectrum. Routed to 69 with the options rather than guessed at.

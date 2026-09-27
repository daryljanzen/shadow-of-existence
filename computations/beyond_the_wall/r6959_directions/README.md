# `r6959_directions` — the transfer's own normalisation across the visibility, measured and then swapped

*`r6959`'s order: the candidate offered unasked at `cc66.46` is the only mechanism left standing after
five eliminations, so it is the run. ⓵ᵃ measure the source's conformal-time dependence across the
window on both arms **as a function**; ⓵ᵇ impose one arm's normalisation on the other and check the
contrast moves by **the amount the measurement predicted in advance**; ⓵ᶜ say first what would refute
it, and say what the swap does to the comb and the depths as well as to the contrast.*

## WHAT WAS ADDED TO THE INSTRUMENT, AND WHY IT IS TWO SWITCHES AND NOT ONE

* **`SRCETA=<path>`** — the measurement. `SRCSAVE` already reports the source **at** the visibility
  peak and its $\eta$-**integral**; ⓵ᵃ asks for neither, it asks for the $\eta$-dependence itself.
  What is saved is the source's own weight across the window, band by band in $q=\ell/\ell_A$:
  $w(\eta,\text{band})=\sum_{k\in\text{band}}P(k)S(\eta,k)^2$, for the whole source, for the
  monopole-plus-Doppler combination, and for each of the four terms separately — together with the
  phase abscissa $r_{s,\rm leaf}(\eta)$ the smearing is a spread **in**, the visibility, $e^{-\tau}$
  and `Jac`. ⌗ *The band sum over $k$ is what turns an oscillation into a normalisation: at fixed $k$
  the source rings in $\eta$ as $\cos(k\,r_s(\eta))$ and neighbouring $k$ ring at different rates, so
  summing a band leaves the envelope. The bands are the contrast statistic's own, so the function comes
  out on the abscissa the excess is measured in.*
* **`SRCTAPER`, `SRCTAPERS0`** — the swap. The assembled source is multiplied by
  $\exp[-\alpha\,(r_{s,\rm leaf}(\eta)-s_0)^2]$ **after** every gradient inside $S$ has been taken, so
  it touches no plasma dynamics, no phase, and no $k$-dependence at fixed $\eta$: it changes only how
  much of each $\eta$ enters the integral. For a weight of spread $\sigma$ in $s$ this gives
  $1/\sigma'^2=1/\sigma^2+2\alpha$, so **the coefficient that imposes a target spread is fixed by the
  `SRCETA` measurement and by nothing else** — which is what makes the size predictable before the run.
  * ⚠ **The knob reaches the HIERARCHY path only**, because `_project` is called only from `hier_run`.
    That is the reporting path (`LOS=1 HIER=1`), where the contrast, the comb and the depths are all
    measured — said here rather than left to be discovered, on the r4558/cc66.36 practice.
  * The four decomposition terms carry the taper too, so `SRCSAVE`'s `resid` still gates that they sum
    to $S$; and `SRCTAPER=0` takes no product at all, so the default is byte-identical.

## THE RUNS

| script | what it is |
|---|---|
| `launch_a.sh` | ⓵ᵃ: the $\eta$-profile on both arms at the reported configuration. `LSTEP=8` with `LMAXL=2000` — the profile is a property of the **source**, so the k-grid is `r6941_fine_*`'s and the kernel work is an eighth of it. |
| `predict.py` | reads the two profiles, reports the function and its moments, forms the prediction $\mathcal R_1=\mathcal D_{\rm cr}/\mathcal D_{\rm lcdm}$, and **solves the taper coefficient**. Writes `prediction.json`, which `launch_b.sh` reads — so the coefficient cannot be chosen after the spectrum is seen. |
| `launch_b.sh` | ⓵ᵇ: the swap at `LSTEP=1 LMAXL=2000`, `r6941_fine_*`'s own sampling, so the tapered spectra are read against the banked baselines with no re-binning and the comb is read off the grid the locator was cleared on at `cc66.45`. |
| `PREDICTION.md` | ⓵ᶜ: committed **before** `launch_b.sh` ran. The predicted interval, the reason it is an interval, and six refutation conditions. |

⚠ **Only the bounded direction of the swap is run, and that is a choice with a reason.** A taper that
*widens* a window has a coefficient of the other sign, so the factor grows away from the anchor — and
the instrument applies it over the whole $\eta$ grid, where the ISW tail lives. At the coefficient the
reverse swap needs, that factor reaches $\sim700$ in the tail, which would test the tail and not the
window. *So the control is narrowed onto the arm ($\alpha>0$, taper $\le1$ everywhere) and the
predictor is calibrated a second time by narrowing the **arm** further — the same direction, an
independent number.*

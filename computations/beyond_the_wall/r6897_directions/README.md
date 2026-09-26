# `r6897+cc66.39` — the zero-point measurement, its calibration, and the control's own response

*`r6897`'s order: **is the contrast excess and the alternation excess one number?** — measured, not
inferred, and with no mechanism asked for or claimed.*

| script | what it runs | why |
|---|---|---|
| `launch.sh` | **the no-op gate** (both arms at the screen grid, against the banked screen base); **the fields at the visibility peak** on both arms via the new `ZPSAVE`, at `LSTEP=64 LMAXL=2000` so the $k$ grid is the reported one while the projection is cheap; and **the control's $\omega_b$ response** at five values, `LSTEP=8 LMAXL=2000`, in `KSLICE` pieces of 250 | (a) needs $\Theta_0$ and $\Psi$ at last scattering on the REPORTING path, which no existing save gave: `PHISAVE` is one of the nine switches `r6893+cc66.37` measured as OFF it. (c) needs a response measured on the instrument rather than an analytic derivative |
| `zpcal.sh` | the control again with its baryon density displaced by $\pm8$ per cent, `ZPSAVE` on | ⚑ **`r4558`'s rule applies to a measurement as much as to a knob.** *A number that has not been shown to move when the thing it measures moves is not a measurement* — so the estimator is asked to track a **known** $\Delta R$ before its verdict on the arm is read. It tracks $77$ per cent of it, and that measured response, not the raw $-R$, is what converts an offset difference into an effective $\Delta\omega_b$ |
| `bank.py` | folds the fields, the no-op pair and the summed $\omega_b$ response into `spectra/r6897_{fields,noop,wb_response_lcdm}.npz` | the slice count each summed spectrum came from is banked with it |

⚑ **Every long run is sliced on `KBATCH` boundaries**, which `r6895+cc66.38` measured as exact to
$10^{-16}$ on both arms — so a container restart costs one slice and not a run. *That finding was made
one revision ago while testing something else, and this is the first order it paid for.*

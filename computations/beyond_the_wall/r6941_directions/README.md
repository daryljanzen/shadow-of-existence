# `r6941+cc66.45` — the fourth peak, and the locator before the residual

*`r6941`'s order (66 heads it `r6939`): `cc66.44` closed the clock route, and what is left undecomposed
is **the fourth peak** — the decisive run reporting $222/538/818/1134$ against the sky's
$220.4/537.7/817.3/1123.9$, so peaks one to three land within a grid step while peak four is $10.1$ out,
and the comb is fitted on the first three, making **peak four the only one out of sample**.*

⚠ **But the first thing asked is the instrument and not the physics.** *The locator was validated at
$\ell_1$ on the banked `LSTEP=1` spectrum ($0.004$ of a multipole) — and $\ell_4$ sits where the damping
has flattened the peak, so its precision there is a different number, unestablished rather than assumed
bad. If the locator at $\ell_4$ is worse than ten multipoles the residual is not measured, the order ends
at step one, and that outcome is worth as much as the decomposition.*

| script | what it runs | why |
|---|---|---|
| `launch.sh` | the reported configuration again at **`LSTEP=1 LMAXL=2000`** — eight times the multipole sampling — on **both arms**, plus the arm's `VISLEAF` endpoints real and injected | the coarse grid's locator is then measured against a fine reference *at the same configuration*, peak by peak. ⚑ *The control is the null that makes it readable: there the sky's own peaks are what the control reproduces, so a locator error shows as a residual on an arm that has none* |
| `bank.py` | folds the slices into `spectra/r6941_fine_{lcdm,cr}.npz` and `r6941_fine_cr_visleaf.npz` | ⚠ the injected arrays are the projection's transfer of a known input and are **not** spectra of the model — separate keys, `r6925`'s caveat carried forward |

**Cost, and why it is sliced.** One `cr` slice at `LSTEP=1` costs $4$m$37$s against well under a minute
at `LSTEP=8`: $1900$ multipoles against $238$. ⚠ *`r6893` lost a whole `LSTEP=2` run to a container
restart at eighty minutes of a hundred — this instrument writes its `npz` only at the end, and a run
longer than its node's own lifetime is not a long run, it is a run that does not finish.* So the set is
sliced on `KBATCH` boundaries, idempotent, and resumable.

⛭ **The standing switch guard runs first** (`../switch_smoke.sh`): every distinct environment is
smoke-tested before the set goes out, and every slice's own log is checked for the `__SWITCHES__` line
carrying the values asked for.

⌗ **What the procedure half needs no new runs for.** The located peak's **window sensitivity** — how far
the answer moves as the parabola window is swept over the admissible range `cc66.28`/`PO-47` established
— is read off the banked reported spectra directly, and it is the half that grows with peak index.

# `r6911+cc66.40` — the contrast statistic at two points in the chain

*`r6911`'s order: **where is the acoustic contrast made — in the source, or in the projection?** One
statistic, applied at both ends. No knob is added and no mechanism is asked for.*

| script | what it runs | why |
|---|---|---|
| `launch.sh` | **the no-op pair** (both arms at the screen grid with `SRCSAVE` unset, and again with `SRCXS=1.5` and `SRCSAVE` still unset), then **the source at both ends** on both arms at `LSTEP=8 LMAXL=2000` in `KSLICE` pieces of $250$ | the $\ell$ end was banked and the $k$ end was not: `ZPSAVE` saves the **fields** at last scattering, and the source is a different object — $g$ times a combination, plus two $\eta$-derivatives. ⌗ `LSTEP=8` and not `r6897`'s cheap `LSTEP=64`, because this run must *also* deliver the reported spectrum on the fine $\ell$ grid — that is what makes the two ends one run |
| `pass2.sh` | the arm again with `KCONT=1`, the uniform continuum sampling at the control's own mode count, physics untouched | ⛔ **the guard the order asked for, run rather than argued.** The projection is a sum over each arm's $k$ grid with `dk = np.gradient(kb)` as its measure, and the two grids are not the same kind of grid — so a contrast read off the projected spectrum could be the arms' *sampling* of an oscillating integrand. *Three of the last five findings on this line were resolution or reference artefacts, and this is that shape exactly* |
| `bank.py` | folds the sliced source runs into `spectra/r6911_source_{lcdm,cr}.npz` | gates that the slice starts **tile the $k$ axis with no gap and no overlap** — a missing slice would otherwise show up as a perfectly plausible shorter grid — and that every slice reports the same multipoles |
| `bank2.py` | folds the no-op pair and the `KCONT=1` arm into `spectra/r6911_noop.npz` and `spectra/r6911_source_cr_kcont.npz` | the same accounting for the guard runs |

⚑ **The two new names and what makes them safe.** `SRCSAVE` writes the source; `SRCXS` writes beside it the
same source projected through `x0 * SRCXS`, which is the other arm's comoving distance. **Both are loaded
only inside `if _SRCS:` blocks**, so with `SRCSAVE` unset neither is read and the run is bit-identical —
gated on both arms, and gated again with `SRCXS=1.5` set and `SRCSAVE` unset, which is what makes the swap
an *output of the save* rather than a knob on the physics. *The order says not to add a knob, and this is
how that is honoured rather than asserted.*

⌗ **The swap ratios are read from the banked minima, not chosen**: the control $13954.353506$ Mpc and the
arm $14017.038576$ Mpc, so `SRCXS` is $1.004492152$ on the control and $0.995527938$ on the arm. ⚠ *The
order's own premise — a six per cent difference, $13005$ against $13865$ — is the **superseded**
configuration's, where the arm's was the smaller; at the adjudicated minima it is $0.449$ per cent and the
arm's is the larger.*

⚑ **Every long run is sliced on `KBATCH` boundaries**, exact to $10^{-16}$ on both arms
(`r6895+cc66.38`) — so a container restart costs one slice and not a run. Both launchers are idempotent
and resumable: a finished slice is skipped on the marker in its own log.

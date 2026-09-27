# `r6919+cc66.42` — a source with no physics in it, and the two geometric factors

*`r6919`'s order: **⓵** project an analytic oscillating source through both arms' own machinery and
measure how much of its oscillation each retains as a function of $q$; **⓶** then swap the two
geometric factors one at a time.*

| script | what it runs | why |
|---|---|---|
| `launch.sh` | the **no-op pair**, then **five configurations per arm** at `LSTEP=8 LMAXL=2000` in `KSLICE` pieces of 250: `sweep` on each arm's own clock at $\phi=0$ and $\phi=\pi/2$, `fixed` (no phase advance across the visibility), `sweep` with **both** arms forced onto the stacking clock, and `sweep` with each arm given **the other's visibility FWHM** | ⓵ needs a source with no terms in it, so `SRCINJ` replaces `S` with $g(\eta)\cos(k r_s(\eta)+\phi)\,k^{(1-n_s)/2}$ — the last factor makes the smooth part of $P S^2$ exactly $\mathrm dk/k$ on **both** arms, so the injection is identical in $q$ and the arms' different tilts cannot enter. ⌗ **The solver is skipped**: the analytic source replaces `S` entirely, so evolving the hierarchy would build an array nothing reads |
| `geom.py` | imports the instrument once per arm and banks the **projection geometry** across the visibility — `Jac`, $\mathrm d r_s$ on each clock, $\mathrm d\chi$, and their ratio | the numbers that decide ⓶ are properties of the background, not of any run, and two module imports are cheaper and clearer than a run |
| `bank.py` | folds the slices into `spectra/r6919_injected_{lcdm,cr}.npz` and the no-op pair into `spectra/r6919_noop.npz` | gates that the slice starts **tile the $k$ axis** and that every slice reports the same multipoles |

## ⛔ The order's named candidate is in the instrument, but not where the order puts it

*The order proposes that $\chi(\eta)$ — "this arm's own conformal-distance-to-time relation" — is read
on the other clock from the source.* ⚠ **`x0 = eta_0 - EE` on both arms, so $\chi(\eta)=\eta_0-\eta$
and $\mathrm d\chi/\mathrm d\eta \equiv 1$ identically on each, with no rate touching it on any path.
There is nothing there to exchange.**

⇒ **The two clocks sit between $r_s$ and $\eta$.** `eg` — conformal time, and so `x0` — is built from
`Hphys`, the *stacking* rate; the acoustic phase accumulates on the *leaf* rate. On the control
`Hleaf` and `Hphys` are character-identical, so `Jac = dη_leaf/dη_stack` is $1.000000$ everywhere; on
the arm it runs $0.789$ to $0.913$ across $\pm3$ FWHM of the visibility.

⇒ **So ⓶'s swap is done inside the injection**, where the phase accumulator is the only thing that
moves: same background, same visibility, same kernel, same $k$ grid. `SRCINJRS=stack` forces both arms
onto one clock; `SRCINJVIS` swaps the other factor, the visibility's width, by rescaling $g$ about each
arm's own peak with its integral preserved. *That is reported as the construction it is — the arms'
visibilities sit at $\eta=281.7$ and $486.0$, so the control's cannot be used on the arm's background
as it stands.*

⚠ **None of these runs is a spectrum of the model.** Each is what the projection makes of a *known*
input — the machinery's own transfer — so none may be compared with a banked spectrum or with the sky.

⚑ Sliced on `KBATCH` boundaries (`r6895+cc66.38`); idempotent and resumable.

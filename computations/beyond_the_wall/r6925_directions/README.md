# `r6925+cc66.43` — which clock the visibility is a density in

*`r6925`'s order: the rate rule says **comoving separations read across leaves take the stacking rate;
scales the plasma accumulates take the leaf's** — and $g=\tau'e^{-\tau}$ is neither. Locate every place
the visibility and the optical depth touch a rate, recompute $\mathrm dr_s/\mathrm d\chi$ under the
other admissible assignment, and report the retained fraction **and the comb**, side by side.*

## ⛔ The audit's finding: the instrument already answers this twice, and differently

Every site where $\tau$ or $g$ touches a rate is on the **stacking** clock — the recombination history
solved against `Hphys`, `taup_of` built on `eg`'s conformal time, `tau` integrated over `_egrid`,
`ETA_LS` and `ETA_LS_W` read off that grid. **But `1/k_D^2` twenty lines below *is* Jac-weighted under
`LEAFSCALES`.**

⇒ *So the diffusion length — a scale the plasma accumulates — takes the leaf clock, and the optical
depth — also accumulated by the plasma — takes the stacking clock. Two objects on the same side of the
rule, on opposite clocks, with nothing in the instrument or the corpus stating the choice.*

⇒ **So `VISLEAF=1` is not an invention: it applies to `tau` exactly the weighting `1/k_D^2` already
applies to itself.** On the control it is bit-identical (`Jac ≡ 1` by the rate identity); on the arm it
moves the visibility peak $485.99\to483.83$, its FWHM $43.591\to43.952$ Mpc, and $r_D$ $7.473\to7.168$.

| script | what it runs | why |
|---|---|---|
| `geom.py` | $\mathrm dr_s/\mathrm d\chi$ across the FWHM under **both** assignments, per arm | the decisive number is a property of the background, not of a run: $0.396733\to0.396957$, so $12.8\%$ lower becomes $12.7\%$ |
| `launch.sh` | the **two no-op gates** (`VISLEAF` unset on both arms, and *set* on the control), then the **injection** under `VISLEAF=1` and the **real reported spectrum** under it, both arms, `LSTEP=8 LMAXL=2000` in `KSLICE` pieces of 250 | the order asks for the contrast **and** the comb and refuses to have one picked over the other, so both come off one launch |
| `bank.py` | folds the slices into `spectra/r6925_visleaf_{lcdm,cr}.npz`, the geometry into `r6925_geometry.npz`, the gates into `r6925_noop.npz` | ⚠ the `injvl` arrays are the projection's transfer of a known input and the `combvl` arrays are spectra — kept under separate keys so nothing reads one as the other |

## ⛔ The launcher's own episode, recorded rather than quietly fixed

**The first version dropped its extra environment and thirty-six slices ran as plain `VISLEAF=0`
spectra.** It did `shift 4` and then referenced `$5 $6 $7 $8`, which after the shift point at the wrong
arguments — so `VISLEAF=1` and `SRCINJ=sweep` were never passed. *The runs completed, reported nothing
wrong, and reproduced the banked spectra — which is exactly the shape that gets banked as an answer.*

⇒ The extra environment is now taken as `"$@"` **after** the shift, and the fix is procedural as well
as textual: **smoke-test one slice and grep its log for the marker the switch must print** before the
set goes out. Here that is the FWHM reading $43.95$ rather than $43.59$, and the
`(injected source, solver skipped)` line.

⚑ Sliced on `KBATCH` boundaries; idempotent and resumable.

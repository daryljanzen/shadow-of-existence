# Banked spectra from `ACOUSTIC_two_arm.py`

** These exist so that the likelihood receipts can RECOMPUTE rather than PIN. **  Until c54.176 the
χ² values in `receipts/P15_CR_cosmology/P15_where_the_likelihood_sits.py` were numbers produced by a
scratch script under `/tmp` and typed into the file.  *A receipt whose number cannot be re-derived
from the corpus is a claim, not a receipt.*  Scoring them is now
`computations/planck_tt_likelihood/chi2_of_spectrum.py`, which reproduces both pinned values exactly.

Each file carries `ls`, `Dl`, `l_A`, `D_M`, `r_s`, `arm` — and `dampx` where a damping scan produced
it.

| file | revision | command |
|---|---|---|
| `c54.175_lcdm.npz` | r2376+c54.175 | `ARM=lcdm NK=600 LMAXL=2000 ETAEND=4000 SAVE=… python3 ACOUSTIC_two_arm.py` |
| `c54.175_cr.npz` | r2376+c54.175 | `ARM=cr NK=600 LMAXL=2000 ETAEND=4000 SAVE=… python3 ACOUSTIC_two_arm.py` |
| `c54.177_lcdm.npz` | r2376+c54.177 | same, with the DERIVED shear coefficient 16/15 |
| `c54.177_cr.npz` | r2376+c54.177 | same, with the DERIVED shear coefficient 16/15 |
| `c54.178_lcdm.npz` | r2376+c54.178 | `HIER=1 BSPLIT=1 ARM=lcdm NK=600 LMAXL=2000 ETAEND=4000 KBATCH=300 SAVE=… ` |
| `c54.178_cr.npz` | r2376+c54.178 | the same with `ARM=cr` |
| `c54.178_lcdm_noPi.npz` | r2376+c54.178 | the same with `PISRC=0` — the hierarchy WITHOUT the polarisation source terms, which is the control for what an envelope can and cannot supply |
| `c54.178_lcdm_noBsplit.npz` | r2376+c54.178 | the same with `BSPLIT=0` — the baryons at the CDM's density |

** THE c54.175 PAIR CARRIES 8/9 AND THE c54.177 PAIR CARRIES THE DERIVED 16/15, AND BOTH ARE KEPT
BECAUSE THE DIFFERENCE BETWEEN THEM IS A RESULT. **  16/15 costs the control Δχ² = 1123 and is the
standing default from c54.177, where it is derived from the polarised photon hierarchy rather than
remembered.  *Keeping the 8/9 pair is what lets `L-147`'s receipt show the cost in the file that
reports the verdict instead of asserting it from another.*

** THE SUPERSEDED NOTE, KEPT AS HISTORY. **  It was briefly
changed to 16/15 at c54.176 and changed back in the same revision, because neither value has been
derived in this corpus and a remembered number is not a derivation.  What the change measured is
kept: through plik_lite TT the control prefers 8/9 over 16/15 by Δχ² = 1123, and that preference is
reported as the size of a residual error in the damping tail rather than used to pick the
coefficient — see `P15_the_height_target_was_below_the_resolution_of_its_own_statistic.py`.

Each is a few kilobytes: a strided ℓ grid and its D_ℓ, nothing else.  They are inputs to receipts,
not results in themselves, and every one of them is reproducible from the command in the table.

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
| `L814_cr_phipi_L2000.npz` | r2674 (cc54, L-814) | **the same c54.178 CR-arm command with `CRPHI=3.14159265`** — the seam phase at the OTHER admissible value (φ=π), the φ=π branch of PO-10's F3 pair. `HIER=1 BSPLIT=1 ARM=cr CRPHI=3.14159265 NK=600 LMAXL=2000 ETAEND=4000 KBATCH=300`, `l_A=301.6` (CR's fitted acoustic scale, unchanged). Peaks at 188/436/684/964, ℓ₁/ℓ_A=0.6233, P1/P2=1.619. Scored on the SAME 185 bins as `c54.178_cr` (φ=0). |
| `c54.178_lcdm_noPi.npz` | r2376+c54.178 | the same with `PISRC=0` — the hierarchy WITHOUT the polarisation source terms, which is the control for what an envelope can and cannot supply |
| `c54.178_lcdm_noBsplit.npz` | r2376+c54.178 | the same with `BSPLIT=0` — the baryons at the CDM's density |
| `c54.186_cr_KCONT.npz` | r2441+c54.186 | the same with `ARM=cr KCONT=1` — **the CR arm on a CONTINUUM k-grid instead of its discrete ladder, which is the check the alias gate asks for in its own waiver text and which had never been run against χ²**. *1800 modes at 5.7 samples per Bessel period, against the ladder's ~725 at 2.3; the spectra agree to better than 0.7% everywhere and χ² to 2.1 in 51817, so the CR arm's projection does not depend on the discreteness. Seventh instrument state at ℓ₁/ℓ_A = 0.5703.* |
| `c54.186_lcdm_L3000.npz` | r2441+c54.186 | `HIER=1 BSPLIT=1 ARM=lcdm NK=900 LMAXL=3000 ETAEND=4000 KBATCH=300 SAVE=…` — **the wavenumber range opened, with the k-SPACING HELD FIXED** (NK scaled with LMAXL so the projection sampling is 5.7 per Bessel period in both). *Scored on the SAME 185 bins as the LMAXL=2000 run, the control goes χ² 989 → 218, χ²/dof 5.34 → **1.18** against a true ΛCDM fit's 1.01 — so **78% of what survived c54.183's lensing was the truncation and not physics**.* |
| `c54.186_cr_L3000.npz` | r2441+c54.186 | the same with `ARM=cr` — **so that `L-147`'s `F3` compares two arms at the SAME wavenumber range**, which is the mistake `F3` exists to avoid. *The CR arm moves 298.9 → 302.1 in χ²/dof and ℓ₁/ℓ_A = 0.5703 for the eighth instrument state.* |
| `c54.187_cr_phi<PHI>.npz` (nine files) | r2441+c54.187 | `HIER=1 BSPLIT=1 ARM=cr CRPHI=<PHI> NK=300 LMAXL=1000 ETAEND=4000 KBATCH=300 LSTEP=4 SAVE=…` — **the CR arm under the common phase its own seam datum leaves unspecified**, φ = 0 … π in nine steps. *`CRPHI=0` is the instrument exactly as coded before c54.187 and reproduces ℓ₁/ℓ_A = 0.5703, which is the control on the knob itself.* ⇒ **ℓ₁/ℓ_A runs 0.5703 → 1.2599 (2.21×) while the mean peak SPACING holds at 0.734–0.818 of ℓ_A (1.11×) and is never 1.0.** These are at reduced settings (LMAXL = 1000) and are scored only at ℓ ≤ 500, where they carry 2× wavenumber headroom — they are a *comparison among themselves*, not comparable to the LMAXL = 2000/3000 runs above. |

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

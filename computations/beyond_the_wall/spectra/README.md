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
| `L820_lcdm_nk600_reproduces_c54.178.npz` | r2674 (cc54, L-820) | **the exact c54.178 lcdm command re-run on a 15 GB node — `HIER=1 BSPLIT=1 ARM=lcdm NK=600 LMAXL=2000 ETAEND=4000 KBATCH=300`** — reproducing `c54.178_lcdm.npz` **bit-for-bit** (max \|ΔDl\| = 8×10⁻¹⁶). *This is the provenance check for `C52`: the banked file is `NK=600`, which passes the projection guard at 5.7 points per Bessel period. `C52` read the `.npz`'s 238-point shape as `NK=260`, but 238 = `len(arange(100, 2000, 8))` is set by `LSTEP=8`/`LMAXL=2000`, not `NK`. So the banked spectra are **not** under-sampled and the control's 7.14 / CR's 280.09 stand; what remains is `C51`'s dropped damping-tail bins.* |
| `L820_lcdm_L2512_nk800.npz` | r2674 (cc54, L-820 S2) | **the extension C51 asks for — `HIER=1 BSPLIT=1 ARM=lcdm NK=800 LMAXL=2512 ETAEND=4000 KBATCH=300`** (302 multipoles to ℓ=2508, 6.0 pts/period). *Recovers the 30 damping-tail bins the `LMAXL=2000` arm drops. On the SAME 185 bins the control goes χ²/dof 7.14 → 3.81 (the k-range/truncation effect of `c54.186`); the added tail moves it only → 3.68/dof.* |
| `L820_cr_L2512.npz` | r2674 (cc54, L-820 S2) | **the CR arm of the same extension — `ARM=cr LMAXL=2512 NK=800`** (physical ladder). *The overlap barely moves (280.1 → 281.1/dof); with the damping tail CR is 260.1/dof — still overwhelmingly disfavoured. F3 = χ²(CR)−χ²(LCDM) goes 50497 → 51547 across the extension, so including the dropped bins **widens** the gap: they do not rescue CR.* |
| `c54.178_lcdm_noPi.npz` | r2376+c54.178 | the same with `PISRC=0` — the hierarchy WITHOUT the polarisation source terms, which is the control for what an envelope can and cannot supply |
| `c54.178_lcdm_noBsplit.npz` | r2376+c54.178 | the same with `BSPLIT=0` — the baryons at the CDM's density |
| `c54.186_cr_KCONT.npz` | r2441+c54.186 | the same with `ARM=cr KCONT=1` — **the CR arm on a CONTINUUM k-grid instead of its discrete ladder, which is the check the alias gate asks for in its own waiver text and which had never been run against χ²**. *1800 modes at 5.7 samples per Bessel period, against the ladder's ~725 at 2.3; the spectra agree to better than 0.7% everywhere and χ² to 2.1 in 51817, so the CR arm's projection does not depend on the discreteness. Seventh instrument state at ℓ₁/ℓ_A = 0.5703.* |
| `c54.186_lcdm_L3000.npz` | r2441+c54.186 | `HIER=1 BSPLIT=1 ARM=lcdm NK=900 LMAXL=3000 ETAEND=4000 KBATCH=300 SAVE=…` — **the wavenumber range opened, with the k-SPACING HELD FIXED** (NK scaled with LMAXL so the projection sampling is 5.7 per Bessel period in both). *Scored on the SAME 185 bins as the LMAXL=2000 run, the control goes χ² 989 → 218, χ²/dof 5.34 → **1.18** against a true ΛCDM fit's 1.01 — so **78% of what survived c54.183's lensing was the truncation and not physics**.* **⚠ THE STORED `.npz` IS THE UNLENSED line-of-sight spectrum: scored RAW it is 3.73/dof, and the 1.18 is *after* multiplying by `c54.183`'s lensed/unlensed ratio (CAMB's, applied in `P15_the_control_entered_the_regime…` and `L-824`). A reader scoring the file directly gets 3.73, not 1.18 — the lensing is the operator, not something in the file.** |
| `c54.186_cr_L3000.npz` | r2441+c54.186 | the same with `ARM=cr` — **so that `L-147`'s `F3` compares two arms at the SAME wavenumber range**, which is the mistake `F3` exists to avoid. *The CR arm moves 298.9 → 302.1 in χ²/dof and ℓ₁/ℓ_A = 0.5703 for the eighth instrument state.*|
| `L824_lcdm_L3200_nk960.npz` | r2674 (cc54, L-824) | **the THIRD convergence point OWED #496 asks for — `HIER=1 BSPLIT=1 ARM=lcdm NK=960 LMAXL=3200 ETAEND=4000 KBATCH=300`** (388 multipoles, 5.7 pts/Bessel period, k-spacing held at the L2000/L2512/L3000 value). *Reproduces `c54.186_lcdm_L3000` on the same 185 bins both raw (3.73 vs 3.73/dof) and lensed (1.18 vs 1.19/dof), so the control has **converged by L3000** — the unlensed sequence 7.18→3.83→3.73→3.73 PLATEAUS (the `L^-3.4` law fit to the first two points predicts 2.23 at L3200; measured 3.73), and the ~3.73 floor is the lensing, not truncation. LMAXL past L2512 moves nothing on the body; the top bins ℓ1997-2508 go 2.73→1.22/dof as the ceiling clears them. Unlensed like every arm in this table.* |
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

| `L830_cr_lat280.npz` / `L830_cr_lat302.npz` / `L830_cr_lat320.npz` | r2803 (cc54, L-830) | **the pin test 56 routed — the CR arm at `LATARG = 280 / 301.6 / 320`** (`HIER=1 BSPLIT=1 ARM=cr NK=600 LMAXL=2000 ETAEND=4000 KBATCH=300 LATARG=<v>`), the runs 56's container OOM'd at projection. *Peaks track LATARG: mean spacing Δℓ = 240 / 258 / 274, so **Δℓ/L_A = 0.857 / 0.855 / 0.856 is constant** (slope d(Δℓ)/d(L_A) = 0.85) — the ~14% spacing deficit is a fixed structural ratio, not an artefact. Meanwhile l₁ = 164 / 172 / 172 is nearly pinned, so l₁/L_A = 0.586 / 0.570 / 0.537 drifts — the first-peak offset is a separate phase (PO-7).* |

Each is a few kilobytes: a strided ℓ grid and its D_ℓ, nothing else.  They are inputs to receipts,
not results in themselves, and every one of them is reproducible from the command in the table.

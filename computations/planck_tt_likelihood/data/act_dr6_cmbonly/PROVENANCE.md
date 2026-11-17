# ACT DR6 CMB-only (v1.0): provenance

*Banked at `r7815+70.1` on 69's order `r7815` ①, for 60's joint Planck + ACT DR6 tail-tilt likelihood (PO-24). It sits beside `../planck2018_plik_lite/`, in the same harness.*

## What is banked

| file | what it is | sha256 |
|---|---|---|
| `dr6_data_cmbonly.fits` | **verbatim**, the SACC file inside the archive below (9,581,760 bytes) | `c887dc9178d81f5e5e0ce76eca0cd3c9f089056630ab78a1cc4bb28ff8751c29` |
| `act_dr6_cmbonly.npz` | the same data extracted by `extract.py`: `ell_/Dl_/win_` for TT, TE, EE, `win_ell`, the 135×135 `cov` in TT, TE, EE order, `source_sha256` | regenerate with `python3 extract.py` |
| `extract.py` | refuses a FITS whose sha256 is not the one above, then writes the `.npz` | — |

**The archive it came from:**
- **URL:** `https://lambda.gsfc.nasa.gov/data/act/pspipe/sacc_files/dr6_data_cmbonly.tar.gz`, from NASA's LAMBDA archive, ACT DR6.02 power-spectrum products.
- **Fetched:** 2026-11-17. `Last-Modified: Tue, 18 Mar 2025 13:46:58 GMT`, `ETag "4610e-6309e23797f85"`, 286,990 bytes.
- **Archive sha256:** `3f057c2569211ada03759530b74848b322edc3d68d66b6b8c2db0679547dbbd8`.
- **Contents:** one member, `v1.0/dr6_data_cmbonly.fits`. This is the file ACT's `act_dr6_cmbonly` likelihood installs, and the one `r7625` read without banking it.
- **Why the archive itself is not banked:** `*.tar.gz` is git-ignored here, so the FITS is banked instead, with both hashes recorded.

## What it contains, as read

- **Bandpowers:** foreground-marginalised, CMB-only. TT, TE and EE, **45 bandpowers each**, effective ℓ 600.5–6125.5. Units are D_ℓ in μK².
  - Units check: TT at ℓ 1500.5 is 695.0 ± 6.5, against plik_lite's 701.6 at ℓ 1499.
- **Covariance:** **135 × 135**, symmetric to 0.0, positive-definite (smallest eigenvalue 2.46×10⁻²).
- **Windows:** **bandpower windows** for each spectrum on ℓ = 2…8501 (8500 points × 45). Each bin's weights sum to 1.

## What is NOT in it, and where it lives

- **ACT's calibration and polarisation-efficiency nuisances** (the likelihood's `A_act`, `P_act`) and their priors. These are set in the likelihood code (`ACTCollaboration/DR6-ACT-lite`), not in this file. ⚠ **That repository is refused from this container (HTTP 403).** So their values are not banked here and must be taken from the code or the paper.
- **The full multi-frequency data:** `dr6_data.tar.gz`, 413,203,437 bytes, at the same LAMBDA path. It is reachable but not banked, because a CMB-only joint does not need it.

## For the shared sky (the overlap treatment)

ACT's footprint lies inside Planck's sky, so the two are not independent where both measure. The public routes, and what each needs:

1. **ACT's own P-ACT combination** cuts Planck at a multipole and uses ACT above it. It needs no further data: only these bandpowers and `../planck2018_plik_lite/`. **The cut multipoles are ACT's published choice.** They were not read from a fetched source here, so they are not stated here.
2. **A cross-covariance model** (as in `r7625`'s per-multipole proxy) needs each experiment's effective sky and the overlap fraction.
   - ACT DR6's masks are on LAMBDA. Planck's likelihood masks are on the Planck Legacy Archive (`pla.esac.esa.int`), which answers from here.
   - **Neither is banked yet.** They are large maps, and which ones are needed depends on 60's design. **Name them and they will be banked here with the same provenance.**

## The Planck side, as banked (`../planck2018_plik_lite/`)

`cl_cmb_plik_v22.dat` has **613 rows**: TT (215, ℓ 32–2492), TE (199, ℓ 32–1988) and EE (199, ℓ 32–1988). `c_matrix_plik_v22.dat` is the full 613 × 613 TT/TE/EE covariance. So **the polarisation the joint needs is already banked.**
- Its PROVENANCE's *"TT only"* describes `chi2_of_spectrum.py`'s use of the file, not its contents.
- Its own caveat stays attached: it is a third-party re-implementation of `plik_lite` and not `clik`.

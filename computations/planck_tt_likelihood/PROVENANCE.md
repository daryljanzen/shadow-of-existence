# Planck 2018 plik_lite TT — provenance, and how it was reached

**Reached r1934.** The data are NOT on the allowed-domain list as such; they were reached through
`raw.githubusercontent.com`, which is.

- **Source repo:** `heatherprince/planck-lite-py` (master) — *"A python implementation of Planck's
  plik-lite likelihood code"*, found by the **unauthenticated GitHub repository-search API**
  (`api.github.com/search/repositories`) after the **code**-search API returned 401 for lack of auth.
- **Files taken:** `cl_cmb_plik_v22.dat` (binned spectrum, 215 TT bins, ℓ 30–2508) ·
  `c_matrix_plik_v22.dat` (3.0 MB Fortran-record covariance) · `blmin.dat`, `blmax.dat`,
  `bweight.dat` (binning) · `planck_lite_py.py` (the reference implementation).
- **Upstream of that repo:** the official Planck Legacy Archive, `https://pla.esac.esa.int/`, which is
  **not** reachable from here. The repo is a faithful re-implementation, not the official `clik`.

**⚠ SO THE CAVEAT IS STRUCTURAL AND STAYS ATTACHED:** *this is `plik_lite` **TT only** — no
polarisation, no low-ℓ (ℓ<30), no lensing likelihood, no external BBN/BAO/SH0ES priors, and a
third-party implementation rather than `clik`.* **The ΛCDM control returns χ²=206.4 over 215 bins
(χ²/dof≈0.96), which is the check that the pipeline is wired correctly.**

## What was run
- `fit.py lcdm|cr N` — Nelder–Mead over (H₀, ω_b, ω_c, A_s, n_s), τ fixed at 0.054, resumable via
  `lcdm.json` / `cr.json`. The CR case applies the **derived** damping suppression
  (`storyboard_receipts/C8_diffusion_length.py`, `C9_sound_horizon_and_ratio.py`) at every step,
  recomputed on each trial cosmology rather than held fixed.
- `inv.py` — the inverse question: what damping ratio `r` does Planck TT admit at ΛCDM's best fit.

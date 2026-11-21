# `r7847+cc66.1` — PREDICTION, registered before a line of the computation exists

**Order `r7847` (69) ①–④:** an independent CAMB reference for 60's neutrino-mass harness. 60's
ΛCDM control moved `277.7 → 99.67 → 111.38` meV and its effective mass `+67.5 → −7.0 → +44.3`,
against a published `64.2` meV and `−101`. 69 wants the instrument checked by a different seat, as
PO-24's refit was settled on two arms.

## 60's configuration, read off its own files rather than assumed

From `r7846/model6.py`, `r7846/lensing_like.py` and `r7842/model3.py`:

| | |
|---|---|
| control cosmology | `H0 = 67.40`, `Ω_m = 0.3150`, `ω_b = 0.0224`, `n_s = 0.965` |
| τ prior | `0.054 ± 0.007` |
| CMB half | 555 binned TT/TE/EE bins, `r7844`'s covariance, amplitude solved in closed form |
| lensing half | 9 Planck 2018 **conservative** bandpowers, nothing fitted to them |
| convention (69's) | total `ω_m` held, so `ω_cb` falls by `ω_ν`; three species, normal ordering |

⌗ Two properties of 60's instrument that its own docstring states, and that this reference is
positioned to test: its φφ scores `χ²/dof = 2.05` against the nine bandpowers **with a monotone
drift**, and `model6` takes the parameter response at `Sum = 0` only (eight directions), where
`r7844` took derivatives at every sum.

## ① The channel decomposition — what I expect, and why

The convention is doing real work here: holding total `ω_m` while `ω_cb` falls by `ω_ν` is chosen
precisely to suppress the background response, and for `Σm_ν ≲ 0.3` eV the species are still
relativistic at recombination. So:

- **Ⓐ For the primary spectra (TT, TE, EE), the LENSING-SMOOTHING channel dominates** the
  derivative at high ℓ, and the background-at-fixed-`ω_m` channel is the SMALLEST of the four.
- **Ⓑ For `C_L^φφ`, the late-time FREE-STREAMING growth suppression dominates**, and it suppresses
  power, so `∂C_L^φφ/∂Σm_ν < 0` across the banked range.
- **Ⓒ The radiation-era Φ channel is SUBDOMINANT in all four spectra** at these masses — it is the
  channel 60 is ordered to carry, so if it comes out large in the reference that is a finding
  against this prediction and *for* 69's reason for the order.

## ② The limit — my primary prediction, and it is the one that would change 69's conclusion

69 names the useful negative in advance. **I predict it fires: the CAMB reference will NOT reach
about 64 meV on this subset.** The subset is strictly less informative than the published
combination — binned TT/TE/EE rather than the full likelihood, conservative lensing only, no BAO,
and no low-ℓ EE beyond a τ prior.

- **Ⓓ The 95 % limit from the reference lands ABOVE 120 meV**, and I register the band **120–400
  meV**. Outside it, this prediction is wrong.
- **Ⓔ The effective mass does NOT reproduce the published `−101` meV.** With no BAO and only
  conservative lensing, I expect it consistent with zero: band **−50 to +100 meV**.
- ⇒ **Ⓕ If Ⓓ and Ⓔ hold, the gap is the DATA SUBSET, not 60's instrument**, and 60's `111.38` meV
  is then not evidence of an instrument fault at all. This is the outcome that would most change
  what 69 does next, which is why it is registered as the primary call rather than a hedge.

## ③ Two sharper, riskier calls

- **Ⓖ CAMB's φφ against the same nine bandpowers will score much better than `χ²/dof = 2.05`** —
  I predict **below 1.5** — and with **no monotone drift**. If so, that drift is the instrument's
  and not the data's. If CAMB drifts too, the bandpowers or their banking are implicated instead.
- **Ⓗ The `Sum = 0` linearisation is NOT the main cause of the gap.** A `1.7×` discrepancy in a
  limit is too large for a derivative-basis artefact. I expect re-deriving at non-zero sum to move
  the limit by **less than 20 %**.

## What this cannot settle

- **Whether 60's Φ transport through the radiation era is right.** This reference is CAMB's
  decomposition; it can say the channel is small, not that 60's treatment of it is correct.
- **The published figures' own provenance.** `64.2` meV and `−101` are taken from the order as
  given; I am not re-deriving which published combination they came from.

⌗ **Environment note, and it is a correction.** This container had no `camb` all session and I
recorded it as "will not install". That was wrong: the failure was a Debian-managed `packaging`
pip refused to replace, and `--ignore-installed packaging` installs **`camb 2.0.4`**, the version
`requirements-ci.txt` pins, from a manylinux wheel with no Fortran toolchain needed.
`check_env_fingerprint` now reads `rc=0` with all five entries `same`, so this container matches
the environment the tolerance sweep was last run on.

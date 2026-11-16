# `r7813+70` — the control's first-to-second height ratio at Planck's point: PREDICTION

*Registered before any run (`r7813` ①, 69).* The order asks for the control's P1/P2 at Planck 2018's published point (H₀ 67.36, ω_c 0.1200, ω_b 0.02237, n_s 0.9649). It is to be run in the configuration P15 makes the comparison in: the polarisation path, with the wavenumber integral converged at the KFAC the arms use.

The order asks for four things:
- the instrument's P1/P2 and peak positions at that KFAC;
- the same at 1.5 times that KFAC, which is the convergence check P15 states;
- CAMB's P1/P2 at the same point, to replace the printed `2.200`;
- the agreement between them, in per cent.

This settles the question cc66 left open at `r7809` (a2): which configuration the re-pointed ratio is measured in. It also retires the `2.200`, whose own configuration the instrument now refuses as k-truncated.

## The runs (fixed now)

**The background, in the instrument:**
- `ARM=lcdm LH0=67.36 LOM=0.313773 WBH2=0.02237 NS=0.9649`.
- Ω_m = (0.1200 + 0.02237)/0.6736² = 0.3137721. `0.313773` is the value cc66's `r7807` bank used, and it is kept so that bank can be reproduced. The two differ by 1×10⁻⁶ in Ω_m.

**The path:** `HIER=1`, the photon hierarchy with the polarisation multipoles, at `LSTEP=8 LMAXL=2000`. This is the 185-bin configuration of the arm of record.

**The cutoff:**
- `KFAC=2.0`. This is what the arm of record (`cc66_cr_x_h686_L2000_leafrec1_distances`) and `r7807`'s control bank both carry in their banked `config`.
- `KFAC=3.0` is the 1.5× check.

**The mode count is the instrument's own derived count at each KFAC.** Each run is summed from `KSLICE` pieces of 250 on `KBATCH` boundaries, which is exact to 10⁻¹⁶ (`r6895+cc66.38`).

**The neutrinos differ, and this is stated rather than hidden.** The instrument has no neutrino mass (three massless species), while Planck's model has Σm_ν = 0.06 eV. So the instrument's run is Planck's *point* in this instrument, not Planck's *model*. That is the same caveat `r7807` printed.

## CAMB, at the same point

- **Primary:** `H0=67.36, ombh2=0.02237, omch2=0.1200, ns=0.9649, mnu=0.06, tau=0.0544`, which is Planck's model.
- **Secondary:** the same with `mnu=0` and no massive species, which is the instrument's physics.
- **A_s is irrelevant to a ratio**, and the locator is invariant to an overall amplitude.

## The locator (fixed now)

**One procedure, applied identically to the instrument and to CAMB.** It is the `_sweep` of `P15_at_its_own_preferred_H0_…`, P15's own matched locator, imported from that receipt rather than copied:
- the spectrum is binned to Planck's bins and scaled by the bin factor;
- a cubic spline is fitted;
- parabola vertices are taken over the seven windows (40, 45, 50, 55, 60, 70, 80);
- heights and positions are averaged over the windows.

**Lensing:**
- *Primary (lensed):* the instrument's unlensed TT is multiplied by CAMB's lensed/unlensed ratio at this point (Planck's model), and CAMB's own lensed TT goes through the same locator.
- *Secondary (unlensed):* the instrument's TT against CAMB's unlensed TT, both through the locator with no lensing applied.

**Agreement** = 100 × (instrument/CAMB − 1), on P1/P2. P1/P3 and the peak positions are reported beside it.

## Predictions

- **(1) KFAC=2 reproduces `r7807`'s bank.** max |relative difference| ≤ 1×10⁻¹² on every banked multipole. It is the same switches on an instrument whose added knobs (`DNEFF`, `YHE`) are byte-identical when unset. Through the locator it then gives `r7809+cc66`'s 2.203 to the digit.
- **(2) Converged.** KFAC=3 moves P1/P2 by less than 0.05 % from KFAC=2. P15 states the control moves 0.000 % and 0.046 % between cutoffs.
- **(3) CAMB's lensed P1/P2 at Planck's point is in 2.19–2.21.** The printed `2.200` is the anchor.
- **(4) Agreement within ±0.3 %** on the primary comparison. P15 prints 0.23 % at the old point.
- **(5) Massless against Σm_ν = 0.06 moves CAMB's P1/P2 by less than 0.2 %.**

If any of these fails, it is reported as failed, with the measured value, and nothing is re-registered.

## Where it goes

- **A receipt** under `receipts/P15_CR_cosmology/`, registered in the INDEX.
- **The numbers** to cc66 in `FOR_66_FROM_70.md`, for the control's one pass.

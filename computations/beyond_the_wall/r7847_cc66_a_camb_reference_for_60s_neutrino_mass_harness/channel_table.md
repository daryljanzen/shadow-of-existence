# r7847+cc66 item (4): the channel-by-channel table for 60

CAMB 2.0.4, in 60's own convention read off `ratio_grid3.npz`: H0 = 67.400, omega_b h^2 = 0.02237,
TOTAL Omega_m h^2 = 0.143097 held so omega_cb falls by omega_nu, divisor 93.14, three massive
species, tau = 0.054, A_s = 2.1e-09, n_s = 0.965, lmax = 3000.

## Why the table has three columns and not one

`lensing_operator3.py` forms `RATIO = cl['total']/cl['unlensed_scalar']` from CAMB itself, so
the operator is **not an independent instrument** and cannot be where a discrepancy with CAMB
lives. What is the harness's own is the UNLENSED spectra its two-arm solver supplies. The sum
response therefore factorises exactly,

    d ln C_lensed / dSum  =  d ln C_unlensed / dSum  +  d ln RATIO / dSum

and only the first term is the harness's. Arm C below closes this to 4e-10 ppm, so the
factorisation is the whole story: there is no third term.

## Arm A -- CAMB against the BANKED operator (a reproduction check)

| setting | Sum (eV) | ratio_tt max | ratio_ee max | c_TE max abs |
|---|---|---|---|---|
| `auto4` | 0.00 | 0.0 ppm | 0.0 ppm | 0.000e+00 |
| `auto4` | 0.06 | 0.0 ppm | 0.0 ppm | 0.000e+00 |
| `auto4` | 0.12 | 0.0 ppm | 0.0 ppm | 0.000e+00 |
| `auto4` | 0.60 | 0.0 ppm | 0.0 ppm | 0.000e+00 |
| `lpa0` | 0.00 | 2447.8 ppm | 2855.9 ppm | 3.559e-04 |
| `lpa0` | 0.06 | 2362.4 ppm | 2754.0 ppm | 3.442e-04 |
| `lpa0` | 0.12 | 2251.8 ppm | 2624.8 ppm | 3.290e-04 |
| `lpa0` | 0.60 | 1394.6 ppm | 1627.1 ppm | 2.106e-04 |

`auto4` is the harness's OWN setting: `set_params(..., lmax=3000)` passes no
`lens_potential_accuracy`, and in camb 2.0.4 `set_for_lmax` reads None as an AUTOMATIC
HIGH-accuracy default of max(4, (lmax-1500)/500) = 4, with non-linear lensing on. It
reproduces the banked operator to 0.0 ppm in all three channels at every sum -- bit for bit.
**So the banked operator is confirmed, and the convention columns with it.** The `lpa0` rows
are the contrast that prices the choice: the old low-accuracy default would cost ~2400 ppm in
TT, which is the size of the ENTIRE Sum = 0.06 eV signal. Hand-setting
`lens_potential_accuracy` to 0 or 1 would be a real defect; leaving it unset is correct.

## Arm B -- the three terms, channel by channel

Per cent change against Sum = 0, band mean, at the harness's own accuracy. `unlensed` is the
term the harness's solver supplies and had no reference for; `operator` is the term
`ratio_grid3.npz` already banks; `lensed` is their sum, i.e. what the score actually sees.

### Sum = 0.06 eV

| channel | term | l 30-250 | l 250-650 | l 650-1200 | l 1200-1996 |
|---|---|---|---|---|---|
| TT | unlensed | +0.306% | +0.171% | +0.030% | -0.145% |
| TT | operator | -0.000% | -0.001% | +0.002% | -0.021% |
| TT | lensed | +0.306% | +0.170% | +0.032% | -0.166% |
| EE | unlensed | +0.272% | +0.502% | +0.077% | -0.020% |
| EE | operator | -0.026% | -0.016% | -0.012% | +0.002% |
| EE | lensed | +0.246% | +0.485% | +0.065% | -0.020% |
| TE | unlensed, additive | +9.161e-06 | -3.632e-05 | -5.417e-05 | -1.497e-04 |
| TE | lensed, additive | +8.927e-06 | -3.237e-05 | -5.751e-05 | -8.987e-05 |

TE is carried in the harness's own additive dimensionless form,
(C_TE - C_TE(Sum=0)) / C_TT(Sum=0), for the reason `lensing_operator3.py` gives.

### Sum = 0.12 eV

| channel | term | l 30-250 | l 250-650 | l 650-1200 | l 1200-1996 |
|---|---|---|---|---|---|
| TT | unlensed | +0.669% | +0.329% | +0.034% | -0.367% |
| TT | operator | -0.000% | -0.003% | +0.005% | -0.049% |
| TT | lensed | +0.669% | +0.326% | +0.039% | -0.416% |
| EE | unlensed | +0.591% | +1.081% | +0.129% | -0.065% |
| EE | operator | -0.061% | -0.037% | -0.025% | +0.004% |
| EE | lensed | +0.529% | +1.044% | +0.102% | -0.068% |
| TE | unlensed, additive | +1.964e-05 | -8.962e-05 | -1.192e-04 | -3.734e-04 |
| TE | lensed, additive | +1.911e-05 | -8.066e-05 | -1.262e-04 | -2.255e-04 |

TE is carried in the harness's own additive dimensionless form,
(C_TE - C_TE(Sum=0)) / C_TT(Sum=0), for the reason `lensing_operator3.py` gives.

### Sum = 0.60 eV

| channel | term | l 30-250 | l 250-650 | l 650-1200 | l 1200-1996 |
|---|---|---|---|---|---|
| TT | unlensed | +3.386% | +1.734% | +0.222% | -1.816% |
| TT | operator | +0.000% | -0.013% | +0.037% | -0.268% |
| TT | lensed | +3.386% | +1.720% | +0.251% | -2.109% |
| EE | unlensed | +3.148% | +5.873% | +0.857% | -0.082% |
| EE | operator | -0.309% | -0.171% | -0.103% | +0.103% |
| EE | lensed | +2.819% | +5.685% | +0.686% | -0.191% |
| TE | unlensed, additive | +1.413e-04 | -5.049e-04 | -6.197e-04 | -2.243e-03 |
| TE | lensed, additive | +1.390e-04 | -4.609e-04 | -6.462e-04 | -1.473e-03 |

TE is carried in the harness's own additive dimensionless form,
(C_TE - C_TE(Sum=0)) / C_TT(Sum=0), for the reason `lensing_operator3.py` gives.

## What the table says: the banked half is the SMALL half

The share of the TOTAL sum response that the banked operator carries, |operator / lensed|,
per band -- computed from the rows above, not asserted:

| Sum (eV) | channel | l 30-250 | l 250-650 | l 650-1200 | l 1200-1996 |
|---|---|---|---|---|---|
| 0.06 | TT | 0% | 1% | 7% | 13% |
| 0.06 | EE | 11% | 3% | 18% | 10% |
| 0.12 | TT | 0% | 1% | 14% | 12% |
| 0.12 | EE | 11% | 4% | 25% | 6% |
| 0.60 | TT | 0% | 1% | 15% | 13% |
| 0.60 | EE | 11% | 3% | 15% | 54% |

So the term the harness ALREADY HOLD -- the CAMB-derived operator -- carries only a small
fraction of the sensitivity to the sum, least of all in TT at the low multipoles that
dominate the 555-bin score. The term that sets the limit is the UNLENSED response the
harness's own two-arm solver supplies, and that is the row this reference newly provides.

## Arm C -- closure

| setting | Sum (eV) | TT residual max (ppm) | EE residual max (ppm) |
|---|---|---|---|
| `auto4` | 0.06 | 3.9e-10 | 3.8e-10 |
| `auto4` | 0.12 | 3.7e-10 | 3.7e-10 |
| `auto4` | 0.60 | 3.7e-10 | 3.5e-10 |
| `lpa0` | 0.06 | 3.5e-10 | 3.7e-10 |
| `lpa0` | 0.12 | 3.8e-10 | 3.6e-10 |
| `lpa0` | 0.60 | 3.5e-10 | 3.6e-10 |

Machine zero in every band. `d ln lensed - d ln unlensed - d ln RATIO = 0` identically, so a
discrepancy between this reference and the harness can only be in the unlensed term.


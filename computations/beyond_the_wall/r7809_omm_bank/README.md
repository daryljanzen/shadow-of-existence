# `r7809+70` — PO-24's ω_m response bank

*`r7809` ①: the last inherited parameter 60 needs for PO-24's degeneracy screen, in `r6897`'s mould.*

- **Knob:** the existing `LOM` (Ω_m), at fixed h = 0.67410309. So ω_m = Ω_m h² moves and Ω_Λ = 1 − Ω_m and D_M move with it, which is what changing the matter density at fixed H0 means in this instrument. No new switch.
- **Values:** Ω_m = 0.28504, 0.297433, 0.309826, 0.322219, 0.334612. That is ω_m = 0.129526 to 0.152053, at −8, −4, 0, +4, +8 per cent, as `r6897`'s ω_b set.
- **Setup:** the control at `r6897`'s refit background otherwise, `LSTEP=8 LMAXL=2000`, each value the sum of 11 of 11 `KSLICE` pieces.
- **`spectra/r7809_omm_response_lcdm.npz`:** keys `ls__`/`Dl__`/`lA__`/`rs__`/`DM__` per ω_m, plus `omega_m` and `Omega_m`.
  - **The centre equals `r6897`'s banked centre to 0.0.**
  - It passes `check_banked_config`, with the bank's `config` carrying `LOM` as the five values.

**The response, as a ratio to the centre:**

| ω_m | l_A | ℓ≈200 | 500 | 800 | 1100 | 1400 | 1700 | 1990 |
|---|---|---|---|---|---|---|---|---|
| 0.129526 | 305.46 | 1.047 | 1.026 | 0.993 | 0.988 | 0.966 | 0.973 | 0.974 |
| 0.152053 | 298.10 | 0.958 | 0.973 | 0.998 | 1.000 | 1.018 | 1.016 | 1.026 |

- **The response is mostly low-ℓ amplitude and an acoustic-scale shift (l_A ±3.5).** It changes sign by ℓ ≈ 1100. That is a peak-phase and amplitude direction, not a damping envelope, as 60's `r7800` overlap argument predicted.
- Whether it absorbs the signature is 60's fit.

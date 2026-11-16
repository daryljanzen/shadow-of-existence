# `r7805+70` — PO-24's lensing-amplitude (A_L) response bank

*`r7805`'s order: A_L acts on the high-ℓ shape by smoothing it, so it is the one parameter 60's `r7804` overlap screen cannot rule out from the physics alone.*

**The instrument has no lensing.** `ACOUSTIC_two_arm.py` computes unlensed spectra, so there is no A_L to expose as a byte-identical switch the way `DNEFF` and `YHE` were. A_L is a post-processing amplitude: it multiplies C_L^φφ before the lensing operator acts. `build.py` applies exactly that to the instrument's own spectrum:

- **The input** is the instrument's unlensed control, `r6897`'s banked centre (`LSTEP=8`, `LMAXL=2000`, refit background), splined onto every ℓ.
- **Above ℓ = 1996** it is extended with CAMB's unlensed TT at the same background, scaled at the join. The operator needs inputs band-limited to ℓ ≥ 2500.
- **C_L^φφ** is CAMB's (2.0.4) at the same background: N_eff 3.0, massless ν, **A_s = 2.1e-9**, a standard amplitude, because the instrument carries no normalisation.
- **A_L ∈ {0.8, 0.9, 1.0, 1.1, 1.2}** scales it, and `camb.correlations.lensed_cls` lenses TT (curved sky, Challinor & Lewis 2005). `Dl__0.00` is the unlensed input, kept for reference.

**Checks:**
- A_L = 0 returns the input: max |relative difference| **0.0**.
- The same operator run on CAMB's own unlensed TT reproduces CAMB's lensed/unlensed ratio to **3.8e-4** (ℓ 30–2000).
- **Tail-shape sensitivity** of the A_L 1.2/1.0 ratio, with the tail above 1996 tilted by (ℓ/1996)^±0.5: at most 1.4e-5 below ℓ 1500, 1.1e-4 for 1500–1800, and **5.8e-4 for 1800–1996**, against a response of about 4e-3 there. **The top band is about 15% tail-dependent**, and nothing below it is.
- `check_banked_config` passes. The `config` carries the instrument's resolved switches, `ALENS`, and the provenance.

**The response, as a ratio to A_L = 1.0** (`spectra/r7805_alens_response_lcdm.npz`):

| A_L | ℓ≈200 | 500 | 800 | 1100 | 1400 | 1700 | 1990 |
|---|---|---|---|---|---|---|---|
| 0.8 | 1.0002 | 1.0005 | 1.0030 | 1.0021 | 1.0038 | 0.9983 | 0.9956 |
| 1.2 | 0.9998 | 0.9995 | 0.9970 | 0.9980 | 0.9963 | 1.0018 | 1.0043 |

- **The response is a few parts in a thousand.** It oscillates with the peaks, because lensing fills the troughs and lowers the peaks, and it changes sign near ℓ ≈ 1600 as the tail gains power.
- **For comparison, at the same ℓ:** N_eff's response is ±7–9% and Y_He's ±5%.
- Whether it overlaps the signature's residual is 60's screen.

## Extended at `r7809` ②: A_L = 1.3 and 1.4

A cheap re-run of `build.py`, the same operator with nothing else changed. The checks are unchanged: identity 0.0, operator against CAMB 3.8e-4. **A_L 1.4 / 1.0:** 0.9996 at ℓ≈200, 0.9940 at 800, 0.9927 at 1400, 1.0036 at 1700, 1.0086 at 1990. The bank now spans A_L 0.8 to 1.4, so 60's published-window bound can be a fit.

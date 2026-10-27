# r7611+70 — PREDICTION: P15's imposed-route figures carried to the faithful exponent

Registered before any re-run. Order: `FOR_70.md` r7611 (restated at r7613).

## What "faithful" means, and the conversion the receipts need
- r7577+70.2 measured the instrument's damping ratio as exp[−α(r²−1)(ℓ/1951.9)²] with **α = 1.70** (ℓ_D = 1951.9 is the instrument header's damping multipole, the one α was fitted against).
- Equivalently the faithful signature is exp[−(r²−1)(ℓ/ℓ_eff)²] with **ℓ_eff = 1951.9/√1.70 = 1497**.
- The four receipts do not share an ℓ_D, so the correction is not one factor. For a receipt written with ℓ_D = L, the faithful exponent is the as-built one times **s = 1.70·(L/1951.9)²**:
  - L = 1362 (joint fit, wrong absorber, tilt off the tail): **s = 0.828**, a weaker signature.
  - L = D_M/r_D ≈ 2133.5 (the collapse receipt's derived ℓ_D at recombination; it varies by endpoint): **s ≈ 2.03**, a stronger one.
  - L = 1951.9 (C62's, which the collapse receipt also prints): s = 1.70.
- In the small-signature regime the shape χ² after a refit scales as s² and a tilt shift as s. At r = 1.0926 and 1.082 the signature is not small, so the scaling is expected to undershoot there.

## Predictions, each with a band
| arm | receipt | as built | predicted faithful | band | p |
|---|---|---|---|---|---|
| **G-1** | collapse: 185-bin χ² at the adjudicated ratio | 1.70 total | ≈ 6.5 (s² ≈ 4.1) | 4.5–8.0 | 0.6 |
| **G-2** | collapse: tilt at the adjudicated ratio | +0.0034 | ≈ +0.0068 (×s) | +0.0055 to +0.0080 | 0.6 |
| **G-3** | collapse: share absorbed by amplitude + tilt | seven tenths | unchanged | 0.62–0.78 | 0.75 |
| **G-4** | collapse: sign set by the endpoint; the 13- and 100-fold collapse against 1.082 | as stated | sign unchanged; collapse factors within ×2 | — | 0.7 |
| **G-5** | joint fit: χ²/bin at r = 1.0926 | 1.497 | ≈ 1.1 (between s and s² of 1.497) | 0.85–1.35 | 0.55 |
| **G-6** | joint fit: the Gaussian is left, and the bound is χ², not σ | as stated | unchanged | — | 0.85 |
| **G-7** | wrong absorber: dn_eff at ℓ = 2508 | −1.31 | −1.085 (exactly ×0.828) | ±0.01 | 0.95 |
| **G-8** | wrong absorber: the ~7000× swing over ℓ 30–2508 | (2508/30)² | unchanged (exponent-free) | exact | 0.99 |
| **G-9** | tail fit: the signature mock's shift on ℓ 1000–2508 | +0.025 | ≈ +0.021 (×0.828) | +0.018 to +0.023 | 0.6 |
| **G-10** | tail fit: precision needed to decide | 1.25× Planck | ≈ 1.5× (= 0.0158/(Δ/2)) | 1.35–1.70× | 0.6 |
| **G-11** | tail fit: is any window separated at 2σ? | none (best 1.94) | still none | — | 0.85 |

**Reachable negatives.**
- G-3 or G-6 failing would show that a "shape" statement depends on the exponent, against 69's expectation in r7611.
- G-10 coming in below 1.25 would mean the faithful route makes the tail easier to decide, not harder.

**Method.**
- Re-run each receipt's computation with only the signature's exponent changed, in a script under this directory, with the receipts left untouched.
- G-9–G-11 need new signature mocks on the four tail windows, from r7489's `wfit.py` with the faithful S.
- No paper edits; 69 lands P15's text.

**EFFORT:** about 3 h, most of it the four tail-window mock fits.

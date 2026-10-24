# r7577+70 — PREDICTION: PO-24's open half — which route to the damping signature's magnitude is faithful (registered before any number is read)

**Order:** `r7577` (69). Settle which route is the more faithful and why, pre-registered, and report the magnitude on it. **No new instrument**: only banked spectra and the existing likelihood are used.

## The two routes, as `C62` runs them
- **A, data-shape:** multiply plik_lite's binned TT by S_A(ℓ) = exp[−(DAMPX−1)(ℓ/1951.9)²]. ℓ_D = 1951.9 is the instrument's damping multipole on the control arm. Result: 0.26 χ²/bin after an amplitude+tilt refit (ℓ 100–1760).
- **B, instrument:** the banked pair `r7099_lcdm_LEAFREC1_DAMPX1.000/1.174`. DAMPX scales 1/k_D² **inside the source**. Result: 0.92 χ²/bin.

## The hypothesis, fixed now
**H1, the factor-of-2 exponent.** In the source, damping acts on the **amplitude**, ∝ exp(−k²/k_D²), so C_ℓ ∝ amplitude² carries **exp(−2(DAMPX−1)k²/k_D²)**. Route A applies the exponent once to C_ℓ.
- If ℓ_D = 1951.9 is k_D·D (the amplitude convention), A under-damps by a factor of 2 in the exponent.
- χ² after refit scales as the square of the residual amplitude, so it is off by about 2² = 4, close to the measured 0.92/0.26 = 3.5.
- What H1 does not explain is attributed to the Doppler-derivative term and projection smoothing, which only B carries.

## The test (one ratio, from banked spectra only)
- **T1. Fit:** R(ℓ) = D_ℓ(DAMPX 1.174)/D_ℓ(1.000) from the banked pair, fitted as ln R = c − α·(DAMPX−1)·(ℓ/1951.9)² over ℓ 500–2000. That is the damping regime, below the instrument's ceiling 2200 and above where the ISW lives.
  - **H1 predicts α = 2** (band 1.6–2.4).
  - Route A as built assumes α = 1.
- **T2. Closure:** re-run route A's own `C62` refit with α set to the measured value, nothing else changed.
  - If its χ²/bin lands within ±25 % of route B's 0.92, the factor of three is closed and its cause is named.
  - If it does not, the remainder is the source-only physics (the Doppler derivative and projection), and B stands as faithful *because* it carries what A cannot.
- **T3. Linearity:** the second banked pair `r4494_lcdm_DAMPX1.000/1.157` (an older configuration, `LEAFREC=0`) must give the same α to ±10 %. If it does, ln R is linear in DAMPX−1 and the magnitude scales to the settled endpoint.

## The magnitude at the settled endpoint (reported on the faithful route)
- **Endpoint:** r = 0.9918, so DAMPX = r² = 0.98366.
- **Signature:** S_B(ℓ) = exp[−α·(r²−1)·(ℓ/1951.9)²], with α from T1 (B's measured shape, scaled linearly per T3).
- **Metric:** the existing plik_lite TT refit (amplitude + tilt) over C62's windows. Reported: the shape residual χ²/bin, Δn_s and its σ.
- **Cross-check:** the same metric at DAMPX = 1.174 must reproduce B's 0.92 to within 25 %.

## Predictions
| arm | quantity | central | band |
|---|---|---|---|
| **F-1** | α (T1, r7099 pair) | **2.0** | 1.6–2.4 |
| **F-2** | α (T3, r4494 pair) / α (T1) | 1.00 | 0.90–1.10 |
| **F-3** | route A with measured α, χ²/bin over ℓ 100–1760 (T2) | 0.90 | 0.69–1.15 (±25 % of 0.92) |
| **F-4** | **verdict** | **B is faithful; the factor is A's single exponent (H1)** 65 % · B faithful and the remainder is source-only physics 30 % · neither 5 % | — |
| **F-5** | magnitude at r = 0.9918 on the faithful route: χ²/bin, ℓ 100–1760 | 0.006 | 0.002–0.015 (scales as (r²−1)², and (−0.0163/0.174)² × 0.92 ≈ 0.008) |
| **F-6** | Δn_s at r = 0.9918, ℓ 100–1760 | +0.008 | +0.004 to +0.012 |

**EFFORT:** 1 h (0.5–2). Every input is banked.

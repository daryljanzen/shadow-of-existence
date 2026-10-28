# r7627+70 — PREDICTION: PO-24's deciding measurement, an off-tail baseline from the same data as the tail

Registered before any fit. Order: `FOR_70.md` r7627.

## What is run
1. **Two same-data baselines on ℓ ≤ 800**, flat ΛCDM with six parameters free, Planck lensing and the τ prior (the r7471 configuration plus ACT):
   - **sum:** Planck TT/TE/EE ℓ ≤ 800 plus ACT DR6 CMB-only TT/TE/EE on ℓ 600–800. It pairs with the summed tail arm.
   - **pact:** the P-ACT cut. Planck TT ℓ ≤ 800 and Planck TE/EE below ℓ 600, plus ACT on ℓ 600–800. It pairs with the ACT-alone tail arm, the one that does not double-count the sky.
2. **New signature mocks.** Each tail arm gets its mock again, built from its own baseline's best fit times the faithful S (ℓ_eff 1497, r = 0.9918). The shift Δ is measured from that baseline. This is done on ℓ 1000–2508 and on ℓ 700–1760.
3. **Sky fits on 700–1760** in both arms (r7625 ran only 1000–2508).
4. **The strict rule** (r7489): the signature is decided against if the sky's tail n_s is more than 2σ from the baseline-plus-Δ prediction and within 2σ of the baseline.

## Predictions
| arm | quantity | prediction | band | p |
|---|---|---|---|---|
| **J-1** | sum baseline n_s, against Planck's off-tail 0.9611 | moves by under +0.003. ACT has only about 4 TT bins below 800, at 3–6× Planck's error there | −0.001 to +0.003 | 0.75 |
| **J-2** | pact baseline n_s | like J-1, slightly wider (Planck TE/EE dropped on 600–800) | −0.002 to +0.004 | 0.65 |
| **J-3** | **reachable negative:** the baseline moves up by about the ACT−Planck offset (~+0.01), so the lean disappears | **does not happen** | — | 0.85 |
| **J-4** | ACT alone on 1000–2508, sky's distance from the signature on the pact baseline | ≈ 1.5σ, undecided | 1.2–1.8σ | 0.7 |
| **J-5** | summed arm on 1000–2508, distance from the signature | ≈ 2.1σ (stays at the line) | 1.8–2.4σ | 0.65 |
| **J-6** | **the deciding outcome:** sky beyond 2σ from the signature on the same-data baseline in the ACT-alone arm | **not reached** | — | 0.8 |
| **J-7** | 700–1760 with ACT: separation Δ/σ | ≈ 2.3 (sum), ≈ 1.8 (ACT alone) | 1.8–2.8 and 1.3–2.3 | 0.55 |
| **J-8** | precision still missing in the ACT-alone arm, if undecided: the factor by which σ must shrink for the sky's present distance from the signature to reach 2σ | ≈ 1.3 | 1.15–1.5 | 0.6 |

**Why J-3 is expected not to happen.** ACT's higher n_s comes from its high-ℓ spectra, which is the tail itself. A baseline confined to ℓ ≤ 800 sees almost none of it.
- If that holds, the confound cannot be removed by an ℓ ≤ 800 baseline, and it is degenerate with the signal the test looks for.
- That would be stated as the result, alongside the precision still missing.

**EFFORT:** about 3 h, most of it 10 fits in two or three rounds of four.

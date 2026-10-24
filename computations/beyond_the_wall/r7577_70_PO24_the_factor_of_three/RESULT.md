# r7577+70 — RESULT: PO-24's open half — the factor of three, closed (registration `97c08c7`)

**Run:** `python3 measure.py`. It uses banked spectra and the existing plik_lite TT refit only; no instrument run.

| arm | registered | measured | verdict |
|---|---|---|---|
| **F-1** α, r7099 pair | 2.0 (1.6–2.4) | **1.70** | **HOLDS** (low side) |
| **F-2** α ratio, r4494/r7099 | 1.00 (0.90–1.10) | **1.004** | **HOLDS**: ln R is linear in DAMPX−1 across two configurations |
| **F-3** route A with measured α, χ²/bin over ℓ 100–1760 | 0.69–1.15 | **0.779**, against B's 0.92 (−15 %) | **HOLDS**: closure |
| **F-4** verdict | B faithful, the factor is A's exponent (65 %) | **B faithful; the factor is A's exponent** | **HOLDS** |
| **F-5** magnitude at r = 0.9918, ℓ 100–1760 | 0.006 (0.002–0.015) | **0.0087 χ²/bin** (1.48 over 171 bins) | **HOLDS** |
| **F-6** Δn_s at r = 0.9918, ℓ 100–1760 | +0.008 (+0.004 to +0.012) | **+0.0059 ± 0.0033** (1.8σ) | **HOLDS** |
| EFFORT | 1 h | ≈ 0.7 h | holds |

## Which route is faithful, and why
1. **Route B is the faithful one, because it damps where the physics damps.** DAMPX scales 1/k_D² inside the source, which damps the photon perturbation's amplitude. C_ℓ is quadratic in that amplitude, and the Doppler term picks up the damping through its derivative.
2. **Route A applied the damping exponent once to C_ℓ.** It used exp[−(DAMPX−1)(ℓ/ℓ_D)²] with ℓ_D the instrument's own damping multipole, which is the amplitude convention.
3. **The instrument's measured ratio has an effective exponent α = 1.70, not 1.** That is close to the factor 2 the amplitude-to-power step implies. It falls short of 2 because the projection and the Doppler term soften it at high ℓ: α is 1.82 over ℓ 500–1200 and 1.37 over 1200–2000.
4. **With α = 1.70, route A gives 0.779 χ²/bin against B's 0.92.** The factor of 3.5 closes to 1.18, and the remainder is the non-Gaussian ℓ-shape that a single α cannot carry. **The factor of three was route A's single exponent.**

## The magnitude on the faithful route, at the settled endpoint (r = 0.9918, DAMPX − 1 = −0.01633)
| window | χ²/bin after amplitude + tilt | total χ² | Δn_s | as built (α = 1) |
|---|---|---|---|---|
| 100–1760 | **0.0087** | 1.48 / 171 | +0.0059 ± 0.0033 (1.8σ) | 0.0030, +0.0034 |
| 700–1760 | 0.0026 | 0.27 / 104 | +0.0147 ± 0.0100 | 0.0009, +0.0086 |
| 1000–2508 | 0.0012 | 0.12 / 101 | +0.0226 ± 0.0147 | 0.0004, +0.0133 |

**The settled signature costs under a hundredth of χ² per bin on the faithful route,** so the "wash" stands, now at its faithful bound rather than its weaker one. The faithful figures are 2.9× (χ²) and 1.7× (tilt) the as-built route-A ones.

## A refinement that failed its own check, reported
- I also applied route B's raw measured ratio (not the α-Gaussian) to the data. At DAMPX 1.174 it gives **1.51 χ²/bin, 64 % above B's 0.92**, so it fails the registered ±25 % cross-check.
- The raw ratio carries B's acoustic-phase wiggles and low-ℓ offset onto the data's spectrum, and an amplitude-plus-tilt refit cannot absorb them.
- So it is not used. At r = 0.9918 it would read 0.021 χ²/bin, which is an overestimate.

## Scope
- The metric is plik_lite TT with amplitude and tilt free, as in C62. The shape residual is an upper bound, and the tilt is not a bound.
- Linear scaling of ln R in DAMPX−1 from 1.174 to 0.984 rests on F-2 (two configurations, 1.157 and 1.174).
- It is an extrapolation across DAMPX = 1.

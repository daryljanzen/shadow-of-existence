# r7471+70 — RESULT: PO-24 first half — the tilt off the damping tail, and the displacement weighed against it (registration `6f4f6a13d`)

**Run:**
- `python3 displacement.py`, which reproduces the joint-fit receipt's r = 1.0926 table exactly before changing r.
- `python3 fit.py NAME LMAX SPECTRA LENS PROFILE` for six configurations. The outputs are `fit_*.json`.
- Likelihood (`like.py`):
  - Planck 2018 `plik_lite` TT/TE/EE, restricted to the kept bins on the covariance;
  - Planck 2018 conservative lensing bandpowers, without the linear correction;
  - τ = 0.054 ± 0.007;
  - A_planck 1 ± 0.0025.
- Model: flat ΛCDM, 7 parameters, CAMB 2.0.4.

| arm | registered | measured | verdict |
|---|---|---|---|
| **T-0** control, ℓ_max 2508 | within 1σ of 0.9649 ± 0.0042 | **0.9636 ± 0.0040** (χ² 591.96, 613 bins + 9 lensing) | **HOLDS**: the pipeline is sound |
| **T-1** σ(n_s), off-tail primary | 0.0075 (0.005–0.011) | **0.00626** from the profile; Fisher 0.00627, ratio 0.998 | **HOLDS** |
| **T-2** central n_s, off-tail | 0.966 (0.955–0.978) | **0.9611** | **HOLDS** |
| **T-3** spread S at r = 0.9918 | 0.037 (0.015–0.06) | **0.0370** (+0.0074 → +0.0444, ratio 5.98) | **HOLDS** |
| **T-4** I vs S | I < S (75 %) | **I = 0.0125 < S = 0.0370** (a factor of 3.0) | **HOLDS** |
| **T-5** verdict | WINDOW-DEPENDENT (55 %) | **WINDOW-DEPENDENT** | **HOLDS** |
| **T-6** z on 100–1760 | 0.9 (0.4–1.8) | **1.19** | **HOLDS** |
| **T-7** σ at ℓ_max 650 / 1000 | 0.010 / 0.0060 | **0.0075 / 0.0052** | **HOLDS** (both in band; the 650 at its edge) |
| EFFORT | 4 h (2.5–7) | ≈ 1.3 h (22:27 → 23:45 UTC) | low |

## The weighing, per window (σ_off = 0.00626)

| window W | Δ(W) at r = 0.9918 | z = Δ/σ_off | |
|---|---|---|---|
| 100–1760 | +0.0074 | 1.19 | no tension |
| 100–2508 | +0.0092 | 1.46 | no tension |
| 700–1760 | +0.0181 | 2.90 | ≥ 2 |
| 1000–1760 | +0.0267 | 4.26 | ≥ 2 |
| 1000–2508 | +0.0293 | 4.69 | ≥ 2 |
| 1400–2508 | +0.0444 | 7.10 | ≥ 2 |

**Sensitivity:**

| configuration | n_s | σ |
|---|---|---|
| ℓ ≤ 650 | 0.9567 | 0.0075 |
| ℓ ≤ 1000 | 0.9659 | 0.0052 |
| ℓ ≤ 800, no lensing | 0.9613 | 0.0079 |
| ℓ ≤ 800, TT only | 0.9564 | 0.0079 |

Every arm keeps I < S, and every arm keeps the same split, with the two wide windows under 2 and the four tail windows over 2. The verdict is not an artefact of the cut or of the lensing.

## What it says
1. **The row's terminating case does not apply.** The sky's off-tail measure of the tilt is **three times narrower** than the displacement's window-to-window spread, so the sky *can* resolve the window-dependence.
2. **Against the wide windows, which are the ones a standard fit uses, the displacement is not a tension:** 1.2σ and 1.5σ. That agrees with the strike's +0.0034 ± 0.0031, which was read on a full-range window.
3. **Against the tail windows (ℓ ≥ 700), the displacement is 2.9–7.1σ of the off-tail precision.**
   - What that means, stated exactly: if the sky carries the signature at r = 0.9918, a ΛCDM fit restricted to those windows must return an n_s higher than the off-tail 0.9611 by +0.018 to +0.044.
   - The off-tail measurement is now precise enough to see that.
   - **This is not yet a finding of tension.** It is a prediction the data can check, and the check (n_s fitted on the real sky over the tail windows, against 0.9611 ± 0.0063) has not been run.
4. **So the question has moved.** Before, it was "is there an independent measure to weigh against?". Now there is one, and the open question is whether the sky's own tail windows show the predicted window-dependent rise in n_s.

## Scope, stated
- **The displacement table is the receipt's own:** TT only, two-parameter (A, Δn) fit on the banked control baseline. Its Δ(W) is what a tilt absorbs, not a full-ΛCDM re-fit. A full re-fit over a tail window would let ω_b and the others share the absorption, and could shrink the tail z's.
- **Missing pieces:**
  - low-ℓ (ℓ < 30) TT and EE are missing, with τ carried by a prior;
  - the lensing linear correction is not applied;
  - `plik_lite` is the foreground-marginalised compressed likelihood, not full `plik`.
- **None of these moves the verdict at the margins measured.** The smallest z above 2 is 2.9, and the largest below is 1.46.

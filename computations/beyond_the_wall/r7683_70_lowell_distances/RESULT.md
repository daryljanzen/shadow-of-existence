# r7683+70 — RESULT

**At the distances' point the split-clock hierarchy behaves as it does at the refit point.**
- ℓ = 3 rises +0.026 (FROZEN) and +0.029 (DECOUPLED) over the one-clock namesake. Every other ℓ moves by under 0.02.
- So arm A − arm B is **negative at ℓ = 3 only (−0.021, −0.024)**, and |A − B| ≤ 0.030 everywhere.
- On all three rows the minimum stays at ℓ = 4 and recovery at ℓ = 8.

Banked as `spectra/p15_lowell_depths_distances_leafrec1.npz` (an addition), the sibling of the refit-point `p15_lowell_depths_leafrec1`, with the same rows plus `config` and `manifest`.

## The rows

The point is (68.60, 0.2973), ω_b 0.02237, radiation 4.1833e-5/h². These are HIER's defaults; `OBF` and `ORF` are unset.

| ℓ | 2 | 3 | 4 | 5 | 6 | 7 | 8 | recovery |
|---|---|---|---|---|---|---|---|---|
| **arm A, exact transfer** | 0.4874 | 0.4348 | 0.3590 | 0.6663 | 0.9113 | 0.9831 | 0.9981 | ℓ=8 |
| **arm B split, FROZEN** | 0.4658 | 0.4560 | 0.3405 | 0.6363 | 0.9004 | 0.9820 | 0.9997 | ℓ=8 |
| **arm B split, DECOUPLED** | 0.4781 | 0.4589 | 0.3581 | 0.6508 | 0.9061 | 0.9818 | 0.9977 | ℓ=8 |
| A − B (FROZEN) | +0.0216 | **−0.0212** | +0.0185 | +0.0300 | +0.0109 | +0.0011 | −0.0016 | |
| A − B (DECOUPLED) | +0.0093 | **−0.0241** | +0.0009 | +0.0155 | +0.0052 | +0.0013 | +0.0004 | |
| split − one clock (FROZEN) | −0.0049 | **+0.0256** | +0.0040 | −0.0154 | −0.0082 | −0.0007 | +0.0031 | |
| split − one clock (DECOUPLED) | +0.0007 | **+0.0289** | +0.0096 | −0.0079 | −0.0030 | −0.0002 | +0.0002 | |

**Arm A reproduces P15's printed seven exactly** (0.487 / 0.435 / 0.359 / 0.666 / 0.911 / 0.983 / 0.998). Arm A has no clock switch: CAMB solves its own recombination and projection. So the A − B difference at ℓ = 3 is the split's ℓ = 3 shift, and it was the clock's at r7677: the onset and the initial data carry about 4% of it.

## Predictions

- P1 (arm A reproduces the printed seven) **holds**.
- P2 (ℓ = 3 rises +0.025 to +0.035; ℓ = 2, 4 and 5 move by under 0.02) **holds**: +0.026 and +0.029, with ℓ = 5 FROZEN the largest other move at −0.015.
- P3 (A − B at ℓ = 3 is −0.02 to −0.035; elsewhere |A − B| ≤ 0.035) **holds**: −0.021 and −0.024, and the largest elsewhere is +0.030 (ℓ = 5 FROZEN).
- P4 (minimum ℓ = 4, recovery ℓ = 8) **holds**.
- P5 (about 14 min) **holds**: 12 min.

## How, and gates

`bank_depths.py` → `depths.json`. It is r7681's script with the point moved and `OBF`/`ORF` unset. It uses the receipt's own `armA` and its own arm-B harness with its CASES, both lifted, and `SPLITCLOCK=1`. `check_banked_config`: passes. No receipt reads the file yet.

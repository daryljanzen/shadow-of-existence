# r7701+70 — RESULT: the (L) banks record their numerics, and the convergence sweep on (L)

**DECOUPLED, the build P15 prints as the hierarchy's depths, is converged on the arm of record in all three knobs.** The doubled opacity grid and the halved late step count move it by **0.0000** at every ℓ = 2–8. The extended continuum moves it by at most **0.0017** (0.36%, at ℓ = 2). So the clause can say this of the arm of record for DECOUPLED.

**FROZEN is not converged in its late step count, which is a miss of my P2.** It runs `NS3` = 900, HIER's default; the sweep's FROZEN entry never sets `NS3`, and the control sweep halved only DECOUPLED's.
- Halving to 450 moves FROZEN by up to **−10.0%** (−0.0333 at ℓ = 4).
- The unregistered ladder 450 / 900 / 1800 / 2400 converges at second order, and h² extrapolation puts the converged FROZEN (L) row at about **0.4704 / 0.4450 / 0.3427 / 0.6479 / 0.9057 / 0.9818 / 0.9973**.
- That converged FROZEN is within **3.1%** of arm A (L) at every ℓ, against 6.19% at `NS3` 900. It is also within **1.9%** of DECOUPLED, against a printed "build spread" of up to 3.3% on (L) and 4.9% on `=1`.
- **So most of FROZEN's distance from the other two rows was its own late-step error.**

## Item 1 — the re-key (`r7701+70.0`, done)

`rekey_numerics.py` → `rekey_numerics.json`.
- **`p15_lowell_depths_leafpert_leafrec1`:** each of the 6 rows records `NTAU`, `NS3`, `KLO`, `NLOW` and `ZEND` / `ZDEC`, read from the sweep's `CASES`, not retyped. FROZEN's `NS3` 900 is read from HIER's source default and marked `NS3_source: HIER default`.
- **`p15_lowell_depths_armA_leafpert_leafrec1`:** each of the 4 rows records `KLO` 0.1 and `NLOW` **320**, read from `camb_L.py`. That is not arm B's 480, which is stated in the row; gate G held at 0.51% with it. `NTAU` and `NS3` are null, with the grid `camb_L.py` uses in their place.
- **Arrays:** byte-identical (dtype, shape, bytes). The sha256s change only through `config` and `manifest`.
- **`check_banked_config`:** byte-identical output before and after, PASS.

## Item 2 — the three knobs on (L), distances point (`run_convergence.py` → `convergence.json`)

Banked as `spectra/p15_lowell_depths_leafpert_convergence_leafrec1.npz` (addition), with each row's knobs in `config.numerics`. Moves from the banked (L) row, ℓ = 2–8:

| run | move | largest | min / recovery |
|---|---|---|---|
| FROZEN, `NTAU` 300000 | 0.0000 everywhere | 0 | 4 / 8 |
| FROZEN, `NS3` 450 | −0.0201, −0.0277, −0.0333, −0.0130, −0.0034, −0.0033, −0.0009 | **−10.04% at ℓ = 4** | 4 / 8 |
| FROZEN, `KLO` 0.02 | −0.0017, −0.0002, +0.0001, +0.0003, +0.0008, −0.0007, −0.0002 | −0.37% at ℓ = 2 | 4 / 8 |
| DECOUPLED, `NTAU` 300000 | 0.0000 everywhere | 0 | 4 / 8 |
| DECOUPLED, `NS3` 30000 | 0.0000 everywhere | 0 | 4 / 8 |
| DECOUPLED, `KLO` 0.02 | −0.0017, 0.0000, +0.0001, −0.0006, +0.0004, +0.0004, +0.0007 | −0.36% at ℓ = 2 | 4 / 8 |

**The unregistered follow-up on FROZEN's `NS3`** (`ns3_frozen_followup.py` → `ns3_frozen_followup.json`, not banked):

| `NS3` | ℓ = 2 | 3 | 4 | 5 |
|---|---|---|---|---|
| 450 | 0.4443 | 0.4098 | 0.2984 | 0.6261 |
| 900 (banked) | 0.4644 | 0.4375 | 0.3317 | 0.6391 |
| 1800 | 0.4690 | 0.4433 | 0.3401 | 0.6458 |
| 2400 | 0.4695 | 0.4439 | 0.3411 | 0.6466 |
| h²-extrapolated | 0.4704 | 0.4450 | 0.3427 | 0.6479 |

- **The second-order check:** the 900 → 1800 step fixes the coefficient, which predicts the 1800 → 2400 step at +0.0007 / +0.0008 / +0.0012 / +0.0010. Observed: +0.0005 / +0.0006 / +0.0010 / +0.0008.
- **`NS3` 3600 returned exactly 1.0000 at every ℓ on two runs.** That is a degenerate output of HIER's late grid at that count, not a depth, so it is not used. I flag it as an instrument defect I have not diagnosed.
- **Converged FROZEN against arm A (L), %:** −2.97, +0.98, −3.08, −1.37, −0.33, −0.10, −0.19.
- **Against DECOUPLED (L), as % of arm A:** −0.47, +1.86, −0.17, −0.17, −0.03, −0.01, −0.03.

## Predictions

- **P1** (`NTAU` ≤ 0.0005): **holds**, at 0.0000 on both builds.
- **P2** (`NS3` halved, ≤ 0.0005 on DECOUPLED and ≤ 0.002 or non-finite on FROZEN): **holds for DECOUPLED (0.0000), misses for FROZEN** (−0.0333). FROZEN's default 900 is about 2.5% short of converged at ℓ = 4.
- **P3** (`KLO` ≤ 0.003, largest at ℓ = 2): **holds**, at 0.0017, ℓ = 2 on both.
- **P4** (minimum 4, recovery 8): **holds on all six**.
- **The overall bound (under 1% except FROZEN `NS3`):** holds as worded. The exception is the result.

## What this means for print and the receipt (not mine to change)

- **The convergence clause can say "on the arm of record" for the hierarchy's printed depths (DECOUPLED):** 0.0000 / 0.0000 / ≤ 0.36%.
- **It cannot say it for FROZEN in the late step count.** FROZEN's printed comparison figures are partly its own step error at `NS3` 900: on (L) −6.19% at ℓ = 4 and a "build spread" of −3.28% at ℓ = 4. Converged, they are about −3.1% and −0.2%.
- **The same is true on the control:** FROZEN there also runs `NS3` 900 and was never swept. The receipt's FROZEN/DECOUPLED comparisons on both backgrounds rest on an unconverged FROZEN.
- **Fixing it is 69's ruling** (run FROZEN at `NS3` ≥ 1800 or extrapolate). The `NS3` 3600 degeneracy would need understanding before a finer count is relied on.

## Gates

- `check_banked_config`: PASS, identical output before and after the re-key; the new bank carries config.
- The low-ℓ receipt by stem after the re-key: ALL CHECKS PASSED.
- `run_touched_readers.sh --class1`: GREEN.

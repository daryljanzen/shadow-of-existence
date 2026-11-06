# r7691+70 — RESULT, items 1–2: what clock arm A runs, and whether it can carry the split

**Arm A runs one clock: the leaf rate, for everything.** It does not carry the split, and stock CAMB 2.0.4 cannot be made to carry it from Python. The ℓ = 2–8 depths in print (0.487 / 0.435 / 0.359 / …) are therefore one-clock values. Nothing is banked under item 2, because there is nothing faithful to bank without modifying CAMB's Fortran, which is a new instrument and 69's call.

## Item 1 — read from the driver and measured

`arm_a_clock.py` → `arm_a_clock.json`.

- **The driver:** `armA` in `P15_the_low_multipole_depth_gap…` was lifted by `ast`. Its CAMB calls are `CAMBparams`, `set_cosmology(H0, ombh2, omch2, mnu=0.06, tau=0.0544)`, `InitPower.set_params`, `set_for_lmax`, `set_accuracy`, `get_results` and `get_cmb_transfer_data`. It assigns no attribute and touches no background or recombination hook (`Recomb`, `DarkEnergy`, `Reion`, `num_nu_massless`, `set_classes`: none). So it runs CAMB's defaults: Recfast, a cosmological constant (`DarkEnergyFluid` at w = −1), photons, neutrinos and ν mass 0.06 eV.
- **The rate, measured:** CAMB's own H(z) against the arm of record's two clocks.

| z | CAMB / leaf rate (distances · refit) | CAMB / stacking rate (distances · refit) |
|---|---|---|
| 10 | 0.9998 · 0.9998 | 1.0015 · 1.0015 |
| 100 | 0.9988 · 0.9988 | 1.014 · 1.014 |
| 1100 | 0.9983 · 0.9983 | 1.151 · 1.154 |
| 3000 | 0.9988 · 0.9988 | 1.376 · 1.383 |
| 10⁴ | 0.9994 · 0.9994 | 1.996 · 2.012 |
| 10⁵ | 0.9998 · 0.9998 | 5.56 · 5.62 |

  CAMB is the leaf rate to 0.2%; the residual is its massive-ν treatment against the 4.1833e-5/h² radiation constant. It is 15% above the stacking rate at recombination and 2× above it at z = 10⁴. That one rate sets CAMB's conformal-time grid, the projection distance in its line-of-sight integral, the perturbation evolution and Recfast's ionisation history.
- **So arm A is HIER's one-clock leg, not its split.** That fits r7689: on one clock the hierarchy sits 1.0–1.1% below arm A at ℓ = 3, and on the split 4.9–5.5% above.

## Item 2 — can arm A carry the split? Not in stock CAMB

The split needs two things CAMB 2.0.4's Python layer does not offer:

1. **An ionisation history on the leaf rate with the background on the stacking rate.** Recfast integrates on CAMB's own `dtauda`. The Python recombination classes are `Recfast`, `HyRec` and `CosmoRec`, all integrators on that same background; none takes a tabulated x_e(z).
2. **The grid and the projection on the stacking rate.** CAMB's background is the Friedmann sum of its species, and the same sums enter the perturbation equations. The dark-energy hooks (`DarkEnergyFluid`'s w(a) table, `DarkEnergyPPF`, the quintessence classes) add a component with positive density. They cannot subtract radiation from the expansion while leaving it in the perturbations: a fluid whose density cancels ρ_r would cross zero, and its w would diverge there.

**What a carry would take:** a CAMB fork, which edits the Fortran in three places:
- `dtauda` on the stacking rate;
- Recfast's Hubble term on the leaf rate;
- a ruling on what the Einstein equations read.

On that last point, HIER's split puts the perturbations' conformal Hubble (`Hc_of`) on the stacking rate while the content fractions stay normalised to the leaf total. CAMB's synchronous-gauge equations read the species densities directly, so a fork must choose between two options, and the choice is physics, not plumbing:
- reproduce HIER's pairing (r7677 named it as the one part of the construction not separated);
- keep CAMB's constraint consistent.

**Not a carry:** moving arm A's point (H0, Ωm) to match the split's D_M. That changes the background, not the clock, and it is the point-difference confound the receipt already names.

## What this means for print (69's ruling, not mine)

- The printed ℓ = 3 depth (0.435) is the one-clock exact transfer.
- The arm of record's octopole is, so far, only on the hierarchy: 0.456 (FROZEN) / 0.459 (DECOUPLED) at the distances point.
- What the two transfers cross-validate is the one-clock depths. At the distances point, one-clock DECOUPLED agrees with arm A to within 2.9% at every ℓ = 2–8; FROZEN reaches 6.3% at ℓ = 4.

## A defect in my own bank configs (flagged, not edited)

`p15_lowell_depths_leafrec1.npz` (r7681) and `p15_lowell_depths_distances_leafrec1.npz` (r7683) carry one bank-level `config` with `SPLITCLOCK: True` and `ARM: "cr (arm of record); arm A is CAMB with its own recombination"`. Both are true of the arm-B rows only. Their `armA_exact` row is one clock (leaf rate), as measured above. The `ARM` sentence reads as if arm A were on the arm of record too.
- **Proposed fix:** re-key each config with a per-row `clock` field (`armA_exact: one clock, leaf rate (CAMB)`, `armB_*: split`), leaving the arrays untouched.
- **Why I haven't done it:** both banks are merged and receipts read them, so I hold it for 69's ruling.

## Gates

No bank change. `run_touched_readers.sh --class1`: GREEN.

# r7675+70 — PREDICTION (registered before the switch is written)

## The switch

`SPLITCLOCK=1` in `storyboard_receipts/HIER_photon_hierarchy.py`, on the ARM-unset (leaf) branch, where the sweep's harness runs:
- the conformal-time grid `eg`, `Hc_of`, `eta_onset`, `rs_f` and the projection distance `DM` are built on the **stacking** rate, H0·√(Om/a³+OL), radiation-free;
- `xe_history` is solved on the **leaf** rate, H0·√(Or/a⁴+Om/a³+OL).

Everything else is held: the content fractions, the adiabatic initial data of the ARM-unset branch, and the ARM=cr branch.

- **G1 (byte-identical unset).** With `SPLITCLOCK` unset, the edited module's grid, background splines, ionisation history, visibility and a short `evolve()` are bitwise equal to the pre-edit file's. Checked by importing both side by side.
- **G2.** With `SPLITCLOCK=1` the ionisation history equals the unset run's at the same parameters bitwise, since it is the same rate. The grid differs.

## The runs

The two adjudicated configurations of `cc66_lowell_sweep` (FROZEN `KLO 0.1`, DECOUPLED `NS3 60000`) run through the receipt's own harness at the refit licensed point:
- H0 68.570730, Ωm 0.291246;
- ω_b 0.021643 (`OBF`), radiation 4.15e-5/h² (`ORF` = 4.15/4.1833);
- `SPLITCLOCK=1`.

They are banked as `spectra/cc66_lowell_sweep_leafrec1.npz` (addition), with a manifest.

- **P1.** The minimum stays at ℓ = 4 on both, and the depths at ℓ = 2–5 lie within 0.03 of the namesake's arm-B values (FROZEN 0.4707/0.4304/0.3365/0.6517; DECOUPLED 0.4774/0.4300/0.3485/0.6587). The point-only run (r7673 (a)) moved them by ≤ 0.009.
- **P2.** Recovery is by ℓ = 8 on both. I define it as the first ℓ ≥ 5 with depth ≥ 0.99.
- **P3.** Wall time is about 13 min for the two, as in r7673 (a).

## Stated before the runs

**The four depths P15 prints (0.487/0.435/0.359/0.666) are the receipt's arm A** (CAMB's exact transfer on the adjudicated background), not arm B. The sweep feeds arm B, and the switch does not touch arm A. Arm A on the arm of record is CAMB at the refit point, with CAMB's own recombination. I report it beside arm B for scale, but it is not a LEAFREC object.

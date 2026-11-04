# r7677+70 — PREDICTION (registered before any run)

## Item 1 — the ℓ = 3 separating test

The quantity is arm B's ℓ = 3 depth at the refit licensed point with `SPLITCLOCK=1`: FROZEN 0.4649, DECOUPLED 0.4680 (r7675). The point alone, one-clock, gives FROZEN 0.4395 (r7673 (a)). So the split's share is +0.0254 (FROZEN) and +0.029 (DECOUPLED); r7675 rounded it to +0.027.

**Tests, each under the split at the same point, everything else as r7675:**
- **(Z)** the onset `ZS` moved over 1e5, 3e5, 3e6 and 1e7 (default 1e6): FROZEN at all four, DECOUPLED at 1e5 and 1e7;
- **(C)** ARM=cr's characteristic initial data under the split. This needs a new switch, `SPLITIC=cr`, effective only with `SPLITCLOCK=1`. It selects the CR branch's initial-data block in `evolve()` and nothing else, with the byte-identical-unset gate re-run (G1, extended to `SPLITCLOCK=1` with `SPLITIC` unset).

**Predictions:**
- **P1.** The ℓ = 3 depth moves by under 0.005 across the ZS range on both variants. The adiabatic data's error decays well before the low-ℓ modes cross the horizon, so the onset should not carry it.
- **P2.** Under (C), ℓ = 3 moves by under 0.010 from the split's value. If so, **most of the +0.027 is the split's physics** (the grid and the projection on the stacking rate), and the construction (the initial data) carries the rest.
- **Reachable negative:** if (C) moves ℓ = 3 by more than half the split's share (> 0.013), the construction is carrying it. I will then say what the faithful initial data are.
- **P3.** The minimum stays at ℓ = 4 and recovery at ℓ = 8 under every test.

## Item 2 — the band-RMS sweep on the arm of record

**What exists:** `P15_the_band_rms_ratio_does_not_move_with_any_numerical_setting` folds r7041's `inj_{fixed,sweepown}_{cr,lcdm}_{setting}` runs from `/tmp/n66/r7041/inj` when present, and otherwise reads its hardcoded table. Those folded runs are not in the repository. **The band-RMS ratio needs both arms**, so a bank the receipt can read must carry the control legs too. The control does not move under LEAFREC (r7669), so its rebuild at LEAFREC=1 equals the namesake.

**Builds:**
- **CR:** 2 injections × 10 distinct settings = **20 runs**. On the arm `nk15`/`nk20` are `base` by construction; r7041's GRIDSAVE grids are byte-identical, and on the arm of record too (r7669 ③). That makes the order's 24 into 20 distinct builds.
- **Control:** 2 × 12 = **24 runs**, at the recorded control point with LEAFREC=1. NK is real on the control.
- All at `LSTEP=8 LMAXL=2000`, sliced on `KSLICE` and folded by `r7041_directions/fold.py`.

**Predictions:**
- **P4 (price).** CR about 8 CPU-h, control about 13 CPU-h. On 4 cores: about 2 h CR and 3.5 h control.
- **P5.** On the arm of record, `fixed` sits within 0.01 of 1.0587 and `sweepown` within 0.01 of 1.0660 at base. Every last step stays inside the 0.6% floor, and the worst is under 0.05%.
- **P6.** The verdict counts (1 converged, 7 not-turned-over, 4 two-points-only) are **not** registered to hold. Which readings turn over depends on signs of steps at the 1e-7 level, which a new point can reshuffle. I will report them as they fall.

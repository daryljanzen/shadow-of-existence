# r7675+70 — RESULT

**The split-clock switch is built and gated, the two adjudicated configurations are banked on the arm of record, and the minimum and the recovery do not move.**
- The minimum stays at ℓ = 4; recovery is by ℓ = 8.
- **The ℓ = 3 depth moves by +0.035 and +0.038, missing my registered ±0.03.**
- About three quarters of that move comes from the clock split, not from the point. I cannot yet tell whether it is physics or a construction effect, and I say so below rather than bank it as settled.
- **On the arm of record the receipt's own "frozen and decoupled agree to 4%" check would fail** (5.3% at ℓ = 4).

Bank change: **addition**, `spectra/cc66_lowell_sweep_leafrec1.npz`; the namesake is untouched. Instrument change: `storyboard_receipts/HIER_photon_hierarchy.py`, `SPLITCLOCK`, default off.

## ① The switch, and its gates

**`SPLITCLOCK=1`** applies on the ARM-unset branch, the one the sweep's harness runs:
- `Hub` becomes the radiation-free **stacking** rate H0·√(Om/a³+OL), so the conformal-time grid `eg`, `Hc_of`, `eta_onset`, `rs_f` and the projection distance `DM` follow it;
- the new `_Hrec` keeps the content-carrying **leaf** rate for `xe_history`;
- content fractions, the branch's adiabatic initial data and the ARM=cr branch are unchanged.

Unset, `_Hrec` is the same function object as `Hub`. The diff is 14 lines.

**`gate_unset.py`** → `gate_unset.json`, 63 s:
- **G1 holds.** The pre-edit file (from `d10b2bcda`) and the edited file are imported side by side with the switch unset. All 19 hashed quantities are **bitwise equal**, at the module default and at the sweep's adjudicated environment: `ag`, `eg`, `Hc_of` and six content fractions on `eg`, `_zg`/`_xeg`, `eta_rec`, `eta_0`, `DM`, `rs`, `eta_onset`, and a five-mode `evolve()`'s `E`, `Y` and switch time.
- **G2 holds.** Set, the ionisation history `_zg`/`_xeg` stays **bitwise equal** to the unset run's (it is the same leaf rate), while `eg`, `Hc_of`, `DM`, `eta_rec` and `evolve()` move.
- **A cross-check G2 gave for free:** with the split at (68.60, 0.2973), HIER's `DM` = **14011.456**. That is `ACOUSTIC_two_arm.py`'s arm-of-record D_M at the same point (`refit_grid185_leafrec1_distances/cr_base`, 14011.4567) to 1e-7, so the split puts HIER's projection where the arm of record puts it.

## ② The runs, banked

**Setup** (`run_bank.py` → `result.json`):
- the receipt's own arm-B harness, lifted by `r7109_directions/rederive_lowell_sweep.engine()`, with that file's own CASES;
- the refit licensed point: H0 68.570730, Ωm 0.291246, R0 = `r0_of(point)`;
- ω_b 0.021643 (`OBF`), radiation 4.15e-5/h² (`ORF` = 4.15/4.1833), `SPLITCLOCK=1`.

**Arm B, depth at ℓ = 2–8.** The namesake values are in brackets.

| | ℓ=2 | ℓ=3 | ℓ=4 | ℓ=5 | ℓ=6 | ℓ=7 | ℓ=8 | min | recovery |
|---|---|---|---|---|---|---|---|---|---|
| FROZEN | 0.4697 (0.4707) | **0.4649** (0.4304) | 0.3424 (0.3365) | 0.6321 (0.6517) | 0.8985 | 0.9805 | 1.0003 | ℓ=4 (4) | ℓ=8 (8) |
| DECOUPLED | 0.4826 (0.4774) | **0.4680** (0.4300) | 0.3604 (0.3485) | 0.6469 (0.6587) | 0.9046 | 0.9808 | 0.9982 | ℓ=4 (4) | ℓ=8 (8) |

- Recovery is the first ℓ ≥ 5 with depth ≥ 0.99, as registered.
- Wall time: 63 s and 627 s, about 11.5 min for the two (P3 holds).
- Banked under the namesake's own two key names, at its 4 dp, with `ells`, `config` (instrument blob, the switch, the point) and `manifest`. The six control keys need no counterpart: r7669 showed one rate is correct on the control.

**Arm A (CAMB, the figures P15 prints), beside, not banked:**
- Recipe check at the adjudicated point: 0.4874 / 0.4348 / 0.3590 / 0.6663. That is **0.487 / 0.435 / 0.359 / 0.666 exactly as printed**.
- At the refit licensed point (ω_b 0.021643): **0.4920 / 0.4434 / 0.3601 / 0.6627**, minimum ℓ=4, recovery ℓ=8.
- Arm A has no LEAFREC: CAMB solves its own recombination. This is the point's effect alone.

## ③ What the numbers say, and what they do not

**P1 missed at ℓ = 3.** I registered ±0.03 of the namesake at ℓ = 2–5. ℓ = 2, 4 and 5 hold (largest −0.0196); **ℓ = 3 moves +0.0345 (FROZEN) and +0.0380 (DECOUPLED)**. The minimum (ℓ = 4) and recovery (ℓ = 8) hold on both (P2 holds).

**Most of the ℓ = 3 move comes from the clock, not the point:**
- the point alone (r7673 (a), one-clock) moved ℓ = 3 by +0.009;
- CAMB at the same point moves it by +0.0086;
- so about **+0.027 of the +0.035–0.038 comes from the split**.

Whether that is the arm of record's physics or a construction effect, **I cannot separate here.** The split keeps the ARM-unset branch's adiabatic, radiation-era initial data and its content fractions, both normalised to the leaf total, on a radiation-free grid. The arm of record in `ACOUSTIC_two_arm.py` has its own onset (`ZSTART`) and its own conventions there, and HIER's ARM=cr branch uses characteristic data instead. **The test that would separate them:** the same two configurations with the onset moved (`ZS`), or with ARM=cr's initial data under the split. If ℓ = 3 holds still under both, the move is the clock's.

**The receipt's own checks, read on the arm of record:**
- "the two arms agree to 7% across ℓ = 2–8": arm A against arm B is 4.9% (FROZEN) and 5.5% (DECOUPLED), against 6.3% and 2.9% on the namesake. **It holds.**
- **"the frozen and decoupled variants agree to 4%": 5.3% at ℓ = 4** (3.6% on the namesake). **It would fail if repointed as is.** The split separates the two variants slightly more than the one-clock arrangement did.
- "the minimum is still at ℓ = 4 and recovery still by ℓ = 8 on every row": **holds**.

## Pre-push gates

- **The sweep's receipt, run by stem:** `P15_the_low_multipole_depth_gap_closes_and_two_defects_were_cancelling.py` exits 0 in 350 s with the switch in the tree, so HIER unset still gives what it read.
- `check_banked_config`: it first **failed** on the new file. Its `config` lacked the four defining keys, `LEAFSCALES`, `ZSTART`, `STACKPERT` and `VISLEAF`, which are `ACOUSTIC_two_arm.py` switches that HIER does not have. They are now written out as `null`, with a note that none of them is a switch of this instrument (HIER's onset is `ZS`, recorded as 1e6). The gate now passes. `run_bank.py` writes them the same way.
- `run_touched_readers.sh --class1`: GREEN.
- `gate_unset.py`: G1 and G2 hold.

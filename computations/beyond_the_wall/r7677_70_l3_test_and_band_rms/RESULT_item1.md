# r7677+70 — RESULT, item 1: the ℓ = 3 separating test

**The split's ℓ = 3 shift is the clock's.** Neither of the two construction choices moves it by more than about 0.001: the onset, over two decades, and the initial data, ARM=cr's characteristic data in place of the adiabatic radiation-era data. The split's share is +0.025 (FROZEN) and +0.029 (DECOUPLED). So about **96% of it is the split's physics**: the conformal-time grid and the projection on the stacking rate. About 4% is the construction, and its sign *reduces* the shift.

## What was run

`l3_test.py` → `l3_test.json`.
- **Base:** the sweep's two adjudicated configurations at the refit licensed point (68.570730 / 0.291246, ω_b 0.021643, radiation 4.15e-5/h²), through the receipt's arm-B harness, exactly as r7675.
- **One thing varied per row.** The one-clock (point-only) row and the split's own row are recomputed here from the same tree.
- **The new switch `SPLITIC=cr`** (effective only with `SPLITCLOCK=1`) selects the ARM=cr branch's initial-data block in `evolve()` and nothing else. `gate_splitic.py` → `gate_splitic.json`:
  - **G1:** with `SPLITIC` unset, all 19 hashed quantities are bitwise equal to the pre-edit file, at the default, at the adjudicated environment and under `SPLITCLOCK=1`;
  - **G2:** with it set, only `evolve()`'s output moves.

## The table: ℓ = 3 depth, with the minimum and recovery

| | FROZEN ℓ=3 | DECOUPLED ℓ=3 | min / recovery |
|---|---|---|---|
| one clock (point only) | 0.4395 | — | 4 / 8 |
| **split, ZS 1e6 (r7675)** | **0.4649** | **0.4680** | 4 / 8 |
| split, ZS 1e5 | 0.4656 | 0.4688 | 4 / 8 |
| split, ZS 3e5 | 0.4651 | — | 4 / 8 |
| split, ZS 3e6 | 0.4648 | — | 4 / 8 |
| split, ZS 1e7 | 0.4647 | 0.4679 | 4 / 8 |
| split, `SPLITIC=cr` | 0.4638 | 0.4670 | 4 / 8 |

- Over ZS 1e5–1e7, ℓ = 3 moves by at most **0.0009** on both.
- `SPLITIC=cr` moves it by **−0.0011** (FROZEN) and **−0.0010** (DECOUPLED).
- ℓ = 2, 4 and 5 move by ≤ 0.0009 in every row.

## Verdict

**The +0.027 is the split's physics.** The construction the order named carries about 0.001 of it:
- **The radiation-era adiabatic data:** replacing them with ARM=cr's characteristic data moves ℓ = 3 by 0.001.
- **The onset:** moving it two decades either way moves ℓ = 3 by under 0.001.

So the arm-of-record ℓ = 3 depth is 0.465 (FROZEN) / 0.468 (DECOUPLED), against the namesake's 0.430. Its uncertainty from initial-data construction is about ±0.001.

**One part of the construction is not separated here: the content fractions**, normalised to the leaf total while `Hc_of` is on the stacking rate. That is not an addition of mine. It is how HIER's own ARM=cr branch has always paired the two, so the split inherits the instrument's established CR-arm convention, and no switch in HIER offers another. I name it rather than claim it tested.

**The faithful initial data, should 69 want them pinned:** the data the arm of record itself uses. In `ACOUSTIC_two_arm.py`, the CR arm starts at `ZSTART` 3e7 with that instrument's own onset construction. Both HIER families tested here bracket that and agree to 0.001, so the choice does not reach the third decimal.

**Predictions:**
- P1 (the ZS range moves ℓ = 3 by under 0.005) **holds**: 0.0009.
- P2 (`SPLITIC=cr` moves it by under 0.010) **holds**: 0.0011.
- P3 (the minimum at 4 and recovery at 8 under every test) **holds**.
- The reachable negative did not fire.

**Wall time:** 11 runs, four at a time, 13 min (FROZEN about 58 s each, DECOUPLED about 9 min).

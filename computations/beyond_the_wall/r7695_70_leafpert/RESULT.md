# r7695+70 — RESULT, steps 1–3: both transfers on the arm of record's construction (L)

**Both transfers now carry the arm of record, and they agree.**

At the distances point:

| ℓ | arm A (L) | arm B FROZEN (L) | arm B DECOUPLED (L) |
|---|---|---|---|
| 2 | 0.4848 | 0.4644 | 0.4727 |
| 3 | 0.4407 | 0.4375 | 0.4368 |
| 4 | 0.3536 | 0.3317 | 0.3433 |
| 5 | 0.6569 | 0.6391 | 0.6490 |
| 6 | 0.9087 | 0.9027 | 0.9060 |
| 7 | 0.9828 | 0.9827 | 0.9819 |
| 8 | 0.9992 | 0.9995 | 0.9976 |

- **The cross-validation:** arm B DECOUPLED is within **2.9%** of arm A at every ℓ = 2–8, and FROZEN within **6.2%**. The octopole is **not** an exception (−0.73% and −0.88%).
- **The minimum and recovery:** the minimum is at ℓ = 4 and the recovery at ℓ = 8 on all three rows. The refit point gives the same picture to 0.01.
- **The arm of record's octopole on the exact transfer** is 0.4407 at the distances point and 0.4492 at the refit point. The one-clock exact transfer in print (0.4348) sits 1.3% below it.
- **Where the old 5.5% "excess" came from:** the dynamics of the retired `STACKPERT` pairing, 72–77% of the split's shift. The projection share is +0.006 to +0.007 on both transfers.

## Step 1 — HIER under (L)

`PREDICTION.md` was registered first (`r7695+70.0`).
- **The edit:** `SPLITCLOCK=L` in `storyboard_receipts/HIER_photon_hierarchy.py`. `_rhs` (both branches) reads the leaf ℋ (`_Hdyn`) and is multiplied by `Jac_of = H_stack/H_leaf`, as ACOUSTIC's `LEAFPERT` does. The onset ℋ and radiation-era η are the leaf's, and the stored slip reads the leaf ℋ. Ψ in the source, the visibility measure and the closures stay on the grid clock, as in ACOUSTIC. `SPLITCLOCK=1` is unchanged.
- **The gate** (`gate_leafpert.py` → `gate_leafpert.json`, base `b1f2613cd`):
  - **G1:** unset, `=1` and `=1`+`SPLITIC=cr` are each bitwise equal to the pre-edit file on 19 hashes, at the default and at the adjudicated environment.
  - **G2:** `=L` against `=1` moves only `evolve_Y`. The background, grid, `DM`, ionisation history and `evolve_E` are bitwise equal.
- **The runs:** `run_leafpert.py` → `leafpert.json`, banked as `spectra/p15_lowell_depths_leafpert_leafrec1.npz` (addition; pairing per row). Walls: FROZEN 67–73 s, DECOUPLED 578–595 s.

**The separation at ℓ = 3** (split `=1` minus one clock = dynamics share + projection share):

| point / build | one clock | (L) | split `=1` | total | dynamics | projection | dynamics fraction |
|---|---|---|---|---|---|---|---|
| distances FROZEN | 0.4304 | 0.4375 | 0.4560 | +0.0256 | +0.0185 | +0.0071 | 72% |
| distances DECOUPLED | 0.4300 | 0.4368 | 0.4589 | +0.0289 | +0.0221 | +0.0068 | 77% |
| refit FROZEN | 0.4395 | 0.4463 | 0.4649 | +0.0254 | +0.0186 | +0.0068 | 73% |
| refit DECOUPLED | 0.4390 | 0.4458 | 0.4680 | +0.0290 | +0.0222 | +0.0068 | 77% |

- **At ℓ = 2, 4, 5:** the projection share is −0.005, −0.005 and −0.010 to −0.013, and the dynamics share ranges from −0.003 to +0.015 (full rows are in `leafpert.json`).
- **Predictions:**
  - **P1:** holds. (L) differs from one clock by a projection share consistent across builds and points (+0.0068 to +0.0071).
  - **P2** (dynamics the larger share; (L) ℓ = 3 below 0.443 / 0.444): **holds**, at 0.4375 and 0.4368. The reachable negative did not fire.
  - **P3** ([0.425, 0.465]): holds.
  - **P4** (minimum 4, recovery 8): holds on every row.
  - **P5** (both points' shares agree within 0.005): holds, within 0.001.

## Step 2 — arm A under (L)

`../r7695_70_camb_split/PREDICTION.md` was registered first. That file records the change of method from the ordered Fortran edit and why.
- **The method:** CAMB 2.0.4's exact leaf-rate Boltzmann state, unmodified (the receipt's `armA` parameters, its own Recfast, reionisation τ = 0.0544). It is extracted Newtonian-gauge with `get_time_evolution` at the times HIER's grid maps to, and handed to HIER's own `source_terms` and the arm-B harness's own depth arithmetic. HIER is imported at `SPLITCLOCK=L`: χ on the stacking grid, the visibility in grid measure from CAMB's opacity, and Ψ on the stacking ℋ. The two arms share everything after the dynamics.
- **Gate G:** on one clock, the same pipeline reproduces stock arm A within **0.51%** at every ℓ = 2–8, at both points (ℓ = 3: +0.07% / +0.08%). So the arm-A/arm-B one-clock differences of 1–6% are dynamics, not projection.
- **The runs:** `camb_L.py`, `bank_armA.py` → `armA_L.json`, banked as `spectra/p15_lowell_depths_armA_leafpert_leafrec1.npz` (addition): the (L) rows and the one-clock gate rows, at both points. About 2 min per run; three at once ran out of memory, so the runs go two at a time.
- **Predictions:**
  - **P6** (arm A (L) ℓ = 3 ≈ 0.442 ± 0.005): **holds**, at 0.4407. The (L) − one-clock shift is +0.0056 against HIER's +0.0068–0.0071.
  - **P7** (minimum 4, recovery 8): holds.
- **The Fortran fork was not built.** The r7693 price (one Bessel-argument edit) undercounted: matching `VISLEAF=0` and the grid-time source derivatives in CAMB's expanded source is a rewrite. This route needs none of it and gives the cleaner comparison.

## Step 3 — the two (L) transfers against each other

Arm B (L) relative to arm A (L), in %:

| point / build | ℓ=2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|
| distances FROZEN | −4.21 | −0.73 | −6.19 | −2.71 | −0.66 | −0.01 | +0.03 |
| distances DECOUPLED | −2.50 | −0.88 | −2.91 | −1.20 | −0.30 | −0.09 | −0.16 |
| refit FROZEN | −4.17 | −0.65 | −6.06 | −2.67 | −0.67 | +0.06 | +0.06 |
| refit DECOUPLED | −2.37 | −0.76 | −2.76 | −1.13 | −0.28 | +0.02 | −0.17 |

- **P8** (inside the one-clock spreads; ℓ = 3 under 2%): **holds**. DECOUPLED reaches at most 2.91%, FROZEN at most 6.19%, and ℓ = 3 is at most 0.88%.
- **So on the arm of record** the two transfers agree as they do on one clock. The octopole exception was the retired pairing's, and it is gone.

## Gates

- **The edit's gate:** G1 and G2 hold.
- **The arm-A pipeline's gate:** G holds.
- **The banks:** `check_banked_config` passes for both new banks (additions).
- **The readers:** no receipt reads either new bank yet.
- `run_touched_readers.sh --class1`: GREEN. `HIER_photon_hierarchy.py` is touched, so its readers are in class 1's scope.

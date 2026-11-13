# r7749+70 — RESULT: with the projection's distance on the leaf rate, the full spectrum refitted is level with the control

**Headline.** The configuration is the arm of record (`LEAFREC=1 LEAFSCALES=1 ZSTART=3e7`) plus `LEAFGEOM=1`: the conformal-time grid and the comoving distance built on the leaf rate, radiation included.
- **Refitted on the four parameters the control is refitted on, the arm sits at 1.002× the control's distance from the data** (χ² 186.85 against 186.51, 1.01 per bin). The arm of record sits at 1.596×.
- **As computed at the distances' point, with no spectrum fit, it sits at 0.918×** (196.5 against the control's no-fit 214.1, 1.06 per bin). The arm of record sits at 2.35× (502.1, 2.71 per bin).
- **The BAO distances do not move, and θ\* moves 0.5%, toward Planck's value on the instrument's own definition.** See ⒞.

Every closure holds. Every registered expectation holds, and none of the three outcomes that would count against the assignment fires.

## ⒜ The figures, beside the arm of record's (185 lensed bins, scored as `r7643/measure.py` scores them)

| quantity | control | arm of record (stacking-rate distance) | **leaf-rate distance** |
|---|---|---|---|
| χ² as computed, at the distances' point (68.60, 0.2973) | 214.06 | 502.09 | **196.48** |
| per bin | 1.16 | 2.71 | **1.06** |
| × control | 1 | 2.346 | **0.918** |
| χ² refitted, at a verified minimum | 186.51 | 297.7 | **186.85** |
| per bin | 1.01 | 1.61 | **1.01** |
| × control | 1 | 1.596 | **1.002** |

**The refitted minimum** is H0 68.586, Ω_m 0.2945, ω_b 0.02218, n_s 0.9614, with the amplitude fitted as in every full-spectrum figure. The point is recorded in `figures.json`.

**How it was reached (PREDICTION Ⓑ):**
1. **First fit.** The linearised minimum on the existing one-clock grid (`r7093_directions/grid_oneclock_leafrec1`, centred on the arm of record's own refit point) predicted 185.07. It sat 2.7 grid steps out in n_s.
2. **First verify run** at that point: 189.58, |model − run| = 4.5 > 1.
3. **The registered re-centring:** a second 9-leg grid on that point (`launch_grid2.sh`). Its base reproduces 189.58, and its minimum, 186.23, lies inside half a step on every axis.
4. **Second verify run:** 186.85, |model − run| = 0.62 < 1. **The figure is established**, and it is scored on the run, not on the model.

## ⒝ Closures

| check | result |
|---|---|
| K1: the control reproduces 214.1 and 186.5 | 214.06 / 186.51 ✔ |
| K2: the arm of record's no-fit reproduces 502.1 | 502.09 ✔ |
| K3: the grid's base re-runs bit-identically under the current instrument blob (`e5319ce4`) | identical, max rel 0.0 ✔ |
| K4: the instrument's one-clock self-check (`__ONECLOCK__`) | max\|Jac−1\| = 0, max\|r_s,stack − r_s,leaf\| = 0, on every run ✔ |

## ⒞ The distances on the same assignment

| | D_M (Mpc) | r_s (Mpc) | ℓ_A | 100 θ\* = 100 r_s/D_M | pull vs Planck θ\* |
|---|---|---|---|---|---|
| distances' point, arm of record | 14011.5 | 145.328 | 302.89 | 1.03721 | −11.7σ |
| distances' point, **leaf-rate D_M** | 13941.6 | 145.328 | 301.38 | 1.04240 | +5.0σ |
| refit point, arm of record | 14134.0 | 146.573 | 302.94 | 1.03702 | −12.3σ |
| refit minimum, **leaf-rate D_M** | 13997.7 | 145.823 | 301.57 | 1.04176 | +2.9σ |

**θ\*.** At fixed parameters, the leaf-rate distance to last scattering is **0.50% shorter**, so θ\* is 0.50% higher. That is about 16 of Planck's σ, so E3 holds.
- **On the instrument's own definition (r_s/D_M at its own z_\*), the shift moves θ\* toward Planck's 0.0104085, not away.** The leaf-rate refit sits at +2.9σ, against the arm of record's −12.3σ at its refit.
- **The caveat, stated before anyone reads more into the pulls.** The arm of record reads −11.7σ at the point that was fitted to θ\*. So the instrument's r_s/D_M is not the definition that fit used. In the DESI receipt's construction, θ\* is matched through the onset, not through H0. The robust statements are therefore:
  - the 0.50% shift;
  - that it moves toward Planck on the instrument's own definition.
  
  An absolute θ\* pull is not one of them. A θ\* fit on the corpus's own definition, re-solved on this assignment, is the item that would settle it, and it is not done here.

**BAO, DESI DR2, 13 measurements** (P15 DESI receipt's data and integrals):

| point | at a common r_d: stacking geometry | leaf geometry | Δ | each geometry's own best r_d |
|---|---|---|---|---|
| distances' point (68.60, 0.2973) | 10.539 | 10.556 | +0.018 | 10.539 / 10.552 |
| leaf-rate refit minimum (68.586, 0.2945) | 10.654 | 10.650 | −0.005 | 10.654 / 10.645 |

At z < 3 radiation is negligible, so the leaf-rate geometry leaves the BAO fit where it was: about 0.88 per dof, changing by under 0.02 in χ². E4 holds. **The leaf-rate distance does not break what currently fits on BAO.**

## ⒟ Against the registration

- **E1 ✔:** the refitted multiple falls to ≤ 1.15. It is 1.002.
- **E2 ✔:** the as-computed multiple falls below 2.35. It is 0.918, below the control's own no-fit.
- **E3 ✔:** θ\* moves by more than Planck's 1σ at fixed parameters. It moves 0.50%, about 16σ, toward Planck on the instrument's own definition.
- **E4 ✔:** BAO χ² changes by under 1 at fixed parameters. It changes by 0.018.

**What counts against the leaf-rate assignment:**
1. The refitted multiple would not be below 1.60. It is 1.002, so this does not fire.
2. The refitted minimum's distances would break. BAO is unchanged (10.539 → 10.556). **On the corpus's own definition of θ\*** (⒡: r_snd on the leaf rate from 3e7 to z_rec, over D_M on the leaf rate), the refit sits at **+2.3σ**, within 3σ, so this does not fire. *(Corrected at `r7755`, on 60's `r7754` read. The first version cleared this with the instrument's r_s/D_M pull of +2.9σ, the very quantity ⒞ says this measure cannot bear. On that basis the clause was undetermined, not cleared. The corpus-definition figure is what clears it. The 0.50% shift in D_M is the robust figure to carry, and no paper sentence should rest on the instrument's pull.)*
3. The minimum would sit outside the linear range after one re-centring. The second verify agrees to 0.62, so this does not fire.

## ⒠ What this does and does not establish

- **It establishes the full measurement on this assignment.** On the leaf-rate distance, the arm reaches the control's χ² on the full-range lensed spectrum when refitted on the control's own parameter freedom. As computed at the distances' own point, it scores below the control's no-fit spectrum, the same arm that sits at 2.35× on the stacking-rate distance.
- **It does not adjudicate the assignment.** The corpus holds the stacking rate for the projection's distance on one identification, and that ruling is the gate's, not this receipt's. What is reported is what the data return on each assignment, measured the same way.
- **One parameter moved a long way: n_s, 1.015 → 0.961.** The arm of record's refit sat at 1.015. On this assignment the spectrum prefers a tilt near the control's (0.965), and that belongs in any reading of the result.
- **The improvement is in the distance, not the tilt.** With no spectrum fit at all, at the distances' point and the built-in n_s, the leaf-rate arm scores 196.48 against the control's own no-fit 214.06 (⒜). So the 1.60 → 1.002 improvement is not bought by n_s moving. *(Added at `r7755`, on 60's read.)*
- **What it cost, against the registered price** (2 runs, up to 11 with one further grid, under 1 core-h): **13 instrument runs.**
  - Ⓐ at LSTEP=2 ran twice, because a 1-hour background limit cut the first attempt.
  - The other runs: K3's base re-run, the first verify, the 9-leg re-centring grid, and the second verify, all at LSTEP=8.
  - The second verify and the K3 re-run were not in the registered count.
  - Ⓐ alone took over an hour on one core, so the core-hour price was also exceeded. The total was not metered; it is a few core-hours.

## Files

- `PREDICTION.md`: the registration, committed before any run (`3e2f4eec3`).
- `refit.py`: scoring and the linearised fit, the arm of record's own.
- `distances.py`: θ\* and DESI DR2 BAO.
- `launch_grid2.sh`: the re-centred grid.
- `figures.json` and `distances.json`: every figure.
- **Spectra:** the no-fit and verify spectra and the second grid are in this seat's scratchpad. They can be banked to `spectra/` as additions if the gate wants them, with the manifest pattern of `r7643`.

## ⒡ θ\* on the corpus's own definition (`r7753` ①), and the receipt (`r7753` ②)

**The definition** is the P15 DESI receipt's (`theta_corpus.py`). θ\* = r_s / D_M(z_rec):
- r_s is the leaf sound horizon from z_hi to z_rec = 1090, always on the leaf clock, per node 66's ruling;
- D_M is the distance on the geometry's own rate: stacking for the arm of record, leaf for this assignment;
- z_hi = the arm's ZSTART = 3e7 (1e8 changes the fifth decimal).

| point | arm of record (D_M stacking) | **leaf-rate assignment (D_M leaf)** |
|---|---|---|
| distances' point (68.60, 0.2973) | 1.03715, **−11.9σ**, no onset reaches θ_obs | 1.04235, **+4.8σ**, an onset at z = 1.23e6 matches |
| arm of record refit point | 1.03684, **−12.9σ**, no onset reaches θ_obs | 1.04215, +4.2σ, matched at 1.40e6 |
| **leaf-rate refit minimum** | 1.03633, −14.6σ, no onset reaches θ_obs | **1.04157, +2.3σ**, matched at 2.44e6 |

Values are 100 θ\*.

- **On the corpus's own definition, the leaf-rate refit sits at +2.3σ.** Within 3σ, so "what counts against" ② does not fire on this definition either.
- **The arm of record sits 12–15σ low, and no onset reaches Planck's θ\*,** because the leaf sound horizon run to z_hi = 1e9 is still short against the stacking-rate distance.
- On this assignment, an onset near z ≈ 2.4e6 matches θ\* exactly.
- The instrument's own r_s/D_M gave +2.9σ and −12.3σ, so the two definitions agree to a few tenths of a σ.

**The receipt:** `receipts/P15_CR_cosmology/P15_with_the_projection_distance_on_the_leaf_rate_the_refitted_spectrum_is_level_with_the_control_and_the_bao_fit_does_not_move.py`, 15 checks, all pass.
- It reads the two spectra banked at r7753, `spectra/r7749_leafgeom_nofit_L2000_cr.npz` and `…_refit_verify_cr.npz`. Each carries `switches` and `manifest`, and the receipt asserts LEAFGEOM=1 from each file's own switches line.
- It reproduces 186.85 / 1.002× and 196.5 / 0.918×, the arm of record's 502.1 / 2.35× and 297.7 / 1.60×, the BAO 10.539 → 10.556 and 10.654 → 10.650, and the θ\* figures above.
- It is registered in `receipts/INDEX.md` after the last P15 row, so no existing receipt is renumbered. The P15 and corpus appendices are regenerated: +5 lines each, and nothing else moves.

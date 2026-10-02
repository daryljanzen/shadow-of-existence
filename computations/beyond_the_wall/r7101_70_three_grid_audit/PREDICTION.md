# r7101+70.1: pre-registration for the three-grid audit (`FOR_70.md` `r7101`, Q1, which is `r7099`'s Q2 unchanged)

*This is committed before any statistic is computed. The only things read so far are metadata:*
- *each grid's `ls` sampling, `l_A`, `D_M`, `r_s` and `switches`;*
- *the SHA-256 of the control files;*
- *the `projection reach` and `l_D` lines of the two logged `cr_base` runs.*

*Nothing is run through the transfer. All three grids are banked and tracked.*

## What is audited

`cc66`'s receipt
`P15_the_licensed_rebuild_leaves_all_three_rigidity_numbers_where_they_were_and_the_forbidden_one_puts_the_arm_on_the_controls_own_floor.py`.
For each arm it measures three numbers on three grids:

| arm | unreachable χ² | crossings | longest run |
|---|---|---|---|
| control (all three grids) | 186.007 | 87 | 8 |
| licensed arm | 278.788 | 54 | 33 |
| forbidden arm | 184.989 | 91 | 8 |

## The outcomes, tabled with the one that costs another seat most first

1. **NOT LIKE-FOR-LIKE.** This costs `cc66`'s receipt and `P15`'s `sec:scope` claim. It holds if any of these is true:
   - the three grids differ in anything beyond the one intended switch;
   - the ℓ sampling, ℓ range, steps or parameters differ;
   - the controls are not byte-identical;
   - `rigidity.py`, run as a driver and not imported, does not reproduce the three numbers.
2. **A CEILING ARTEFACT.** This costs the "localised" reading, and with it the claim's strength. It holds if:
   - the forbidden arm's advantage over the licensed arm is not present once the data are cut well below ℓ_max = 2000 (at ℓ_cut ≤ 1600);
   - **or** the advantage lives in the top bins near the ceiling (ℓ > 1800);
   - **or** the projection reach k_max·D_M is not the same on both arms. That would be the specific coupling 66 names: k_max = 2ℓ_max/D_M with the forbidden arm's D_M smaller.
3. **SOMETHING IN THE BANKED SET POINTS THE OTHER WAY.** This costs the sector's "three statistics, one direction". It holds if any of these favours the licensed arm over the forbidden one:
   - per-band χ², especially ℓ < 850;
   - the refit χ² after the four-parameter fit;
   - the low-frequency power of the whitened residual;
   - the closed-form amplitude, which carries the peak heights.
4. **NONE OF THE ABOVE.** The measurement stands as reported, and the audit states the bound it supports.

## What I expect, so a miss is visible

- **(1) does not fire.** The controls are already seen to be byte-identical on all nine files, and the ℓ grid is 100..1996 in steps of 8 on all six bases. I expect `rigidity.py` to reproduce all nine numbers to at least 1e-6.
- **The specific k_max mechanism in (2) does not fire.** Both logged arms print k_max = 3998/D_M, ratio 2.00, so k_max·D_M is held fixed rather than k_max. Neither arm is nearer its own projection ceiling in units of its own D_M.
- **But I expect a ceiling-adjacent effect to be real and to need stating.** The two arms' **damping scales differ**: the logs give ℓ_D = 1868 (licensed) against 1958 (forbidden). So in units of ℓ_D the ceiling is 1.07 against 1.02. My prediction:
  - the forbidden arm's χ² advantage **survives** at ℓ_cut = 1600, but **shrinks** by more than a third from its full-range 93.8;
  - the crossings and longest-run gap **survives** at ℓ_cut = 1600.
- **(3):** I expect at least one band below ℓ = 850 where the forbidden arm is not better. That is because "the discriminating feature lives above ℓ ≃ 850" implies little discrimination below it. I expect nothing that reverses the overall direction.

## Instrument

`audit.py` in this directory:
- it imports `r7091_70_fit_rigidity/rigidity.py` read-only, for `build`, `W`, `STEP` and `stats`, and re-implements no model;
- it additionally runs `rigidity.py` as a subprocess with `--grid` on each grid and parses its printed numbers;
- the ℓ cut is applied by restricting the whitened residual to bins with upper edge ≤ ℓ_cut. The bins are re-whitened on the sub-covariance and the parameter directions re-projected there, so a cut is a fit to fewer data, not a mask on a full-range fit.

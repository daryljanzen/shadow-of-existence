# r7749+70 — PREDICTION: the full spectrum refitted with the projection's distance on the leaf rate

Order: `FOR_70.md` `r7749` (69, on Daryl's direction). This file is pushed before any run.

## The configuration (one switch from the arm of record)

The arm of record is `LEAFREC=1 LEAFSCALES=1 ZSTART=3e7 HIER=1`, with every other switch at its instrument default.

**Added: `LEAFGEOM=1`.** The conformal-time grid and the comoving distance are built on `Hleaf`, which includes radiation (`ACOUSTIC_two_arm.py` l.231–268). It is the one-clock assignment of `r7093`/`r7651`.

**The control is unchanged.** `LEAFGEOM` and `LEAFREC` do not reach it: `r7641` measured 3.6e-16.

## What is run, and the price

**Ⓐ As computed, at the distances' point.**
- One no-fit run at `CRH0=68.60 CROM=0.2973` with built-in ω_b and n_s, `LMAXL=2000`, scored on the 185 lensed bins.
- The scoring is the refit-bound receipt's own CAMB lensing operator with `chi2_of_spectrum`, exactly as `r7643/measure.py` scored the arm of record.

**Ⓑ Refitted.**
- **The grid:** the existing 9-leg response grid `r7093_directions/grid_oneclock_leafrec1/` (banked at `r7651`). It is centred on the arm of record's own refit point `(68.570730, 0.291246, 0.021643, 1.015066)`, the same centre as `refit_grid185_leafrec1/`, with only `LEAFGEOM=1` added.
- **The fit:** the linearised minimum over **the four parameters the control is refitted on (H0, Ω_m, ω_b, n_s)**, with the amplitude fitted as in every full-spectrum figure. It uses the arm of record's own fit (`r7641_cc66_grid_readers/full_range_refit_on_the_arm_of_record.py::fit`).
- **The verify run:** one full run **at that minimum**. The minimum is scored on that run, never on the linear model. If the run moves χ² by more than 1 from the model's prediction, one further grid step centred on the run is taken.

**Ⓒ The distances on the same assignment.**
- **θ*/ℓ_A** at Ⓐ's point and at Ⓑ's minimum, against Planck's θ*, the datum the distances' point is fitted to.
- **The DESI DR2 BAO distances** (D_M/r_d, D_H/r_d, D_V/r_d) on the leaf-rate geometry at both points, against the same data, through `P15_the_desi_dissolution…`'s own likelihood.

**Price:**
- 2 runs (Ⓐ plus Ⓑ's verify), up to 11 if one further grid is needed. At a few minutes per run on 1 core, that is **under 1 core-h**.
- The grid already exists, and the distances are background integrals measured in seconds.
- **Not nightly-class, so it runs here.** The `dlk.yml` pattern is not needed.

## The figures reported, beside the arm of record's

| quantity | control | arm of record (stacking-rate distance) | this build |
|---|---|---|---|
| χ²/bin as computed, 185 lensed bins | 1.16 | 2.71 | Ⓐ |
| arm's distance from the data, × control's, as computed | 1 | 2.35 | Ⓐ |
| the same, refitted | 1 | 1.60 (297.7 vs 186.5) | Ⓑ |
| θ* and ℓ_A | — | — | Ⓒ |
| BAO χ² | — | — | Ⓒ |

## Closures (each a refusal)

- **K1:** the control reproduces its banked figures bit for bit (214.1 and 186.5), since nothing reaches it.
- **K2:** with `LEAFGEOM=0` instead, Ⓐ's point reproduces the arm of record's 502.1 (2.71 per bin). The scorer and point are the arm of record's, so any change in Ⓐ is the switch's.
- **K3:** the grid's base leg (`grid_oneclock_leafrec1/cr_base`) re-runs bit-identically under the current instrument blob. Otherwise the grid is stale and is rebuilt before the fit.
- **K4:** `LEAFGEOM=1` asserts its own one-clock self-check, and the run refuses if it fails (the instrument's l.368–374).

## Expectations (registered)

- **E1 (refitted, the headline):** the refitted multiple falls from 1.60 to **≤ 1.15**, level with the control within the spread the control's own refit carries. The basis is the irreducible residual on this assignment, 186.135 against 186.007. Confidence 65%.
- **E2 (as computed):** the as-computed multiple at the distances' point falls below the arm of record's 2.35. I make no claim about how far: the distances' point was fixed on the stacking-rate geometry, so it need not be this assignment's preferred point. Confidence 60%.
- **E3 (θ*):** at fixed (H0, Ω_m), the leaf-rate distance to last scattering differs from the stacking-rate one, because radiation enters the integral. **I expect θ* to move by more than Planck's 1σ (0.03%) at the distances' point**, so the BAO + θ* point has to move, and Ⓒ reports by how much. Confidence 70%.
- **E4 (BAO):** at z < 3 radiation is negligible, so the BAO distances barely move: BAO χ² changes by < 1 at fixed parameters. Confidence 75%.

## What counts against the leaf-rate assignment

Stated before any run:
1. **The refitted multiple is not below 1.60.** Following the data would then not favour the leaf rate on the full spectrum.
2. **The refitted minimum's own distances break.** BAO χ²/dof worsens by more than 1 per dof against the arm of record's, or θ* cannot be met within 3σ at a point the spectrum also accepts (Δχ² < 4 from its minimum). In that case the leaf-rate assignment fits the spectrum by giving up what currently fits.
3. **The minimum sits outside the grid's linear range.** The verify run then disagrees with the model by more than 1 after one re-centring, and I report the figure as **not established**, not as a number.

Every outcome, including either kind of failure, is reported at the same weight.

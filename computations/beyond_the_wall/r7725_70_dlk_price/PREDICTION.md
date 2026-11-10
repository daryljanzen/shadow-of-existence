# r7725+70 — PREDICTION (registered before any timing is taken)

The order (`FOR_70.md`, `r7725`): price retaining the (ℓ, k) transfer Δ_ℓ(k) in the full real-source computation, over q ∈ [0.80, 3.10], in both arms, on one shared k grid, at enough ℓ to carry cc66's 142-component structure.
- Check that the row sums reproduce the banked spectra.
- Build and bank it if the price is nightly-class; otherwise report the price and what would bring it down, without changing the numerics.

## Read before registering (no timing yet)

**⒜ `Dlk_samp`, the existing retention.** It is not what `r7723+cc66` reported, and this is checked directly on the banks:
- **Where its samples sit:** `samp` holds INDICES into `ls`, and 20…204 are those indices. The sampled multipoles are **ℓ = 260, 468, 684, 892, 1100, 1308, 1524, 1732** (q 0.86–5.74, `bank_thin.py` draws them from q ∈ [0.85, 5.75]). **Four of the eight lie inside the step window** (q 0.86, 1.55, 2.27, 2.96).
- **Shared multipoles:** both arms carry the same eight ℓ, not four of eight.
- **Row sums:** they reproduce the banked spectra once the transfer's own definition is used, ℓ(ℓ+1) Σ_k P Δ² = D_ℓ. The maximum relative residual is **4.4×10⁻¹⁶** in all four (arm × injection) blocks, and each save's own `closes` key is 0.
- **The k grids do differ (2547 against 1452).** That objection stands.

**⒝ Why `Dlk_samp` still does not serve.** It comes from the r7039 runs, which replace the plasma source with an analytic injection (`SRCINJ=fixed` / `sweepown`). Under `fixed`, Δ_ℓ(k) factorises exactly, so it is the factorised object again. **The order's real-source run is the right ask.**

**⒞ The object and its closure.** `DLKSAVE` in `ACOUSTIC_two_arm.py` retains `_tr = ∫ S j_ℓ(k x0) dη`, the array whose Σ_k P·_tr² is `Cl`, per k-batch, and concatenates the batches along k. **Closure test, registered:** for every retained ℓ, ℓ(ℓ+1) Σ_k P Δ² reproduces the run's own D_ℓ to ≤ 1e-12 relative. Where the ℓ coincide with the banked r6911 spectra (`LSTEP=8`, same `LMAXL`, `KFAC` and switches), the run's D_ℓ must also reproduce those to ≤ 1e-10.

## The price model, registered

- cost = (hierarchy solve per 250-mode k-slice × slices) + (projection per ℓ per slice × ℓ retained × slices).
- slices: 11 for ΛCDM (2547 modes) and 6 for CR (1452).
- ℓ retained:
  - every integer ℓ in q ∈ [0.80, 3.10] is about 695 per arm (ℓ ≈ 241–935, l_A ≈ 301.5–301.8);
  - every second ℓ is about 348;
  - 142 rows is the floor, too thin to carry rank-142 structure;
  - so every integer ℓ is the target, matching cc66's 692-row plane.
- **Measured, not extrapolated:**
  - (i) one real 250-mode slice of each arm, run whole at the reported configuration with `DLKSAVE`, timed;
  - (ii) the per-ℓ projection cost inside the window at ℓ = 241, 588 and 935, on that slice's actual η grid.

## The shared k grid — the one place a numerics choice enters

The arms' k grids differ by construction (the arm's D_M, and CR's ladder). Two routes:
- **(S1) retain each arm on its own grid and resample.** Δ_ℓ(k) oscillates on Δk ≈ π/r_s*, and the grids sample that at about 4 points per period. Interpolation would add error a 142-component fit could read. **Registered as not acceptable for cc66's object** unless measured below the closure's precision.
- **(S2) a common physical-k grid**, the union or the finer grid, imposed on both arms. That changes which k the arm is computed at, so it is a numerics change. **Not built under this order.** It is priced and reported as the route, with its effect on D_ℓ measured if cheap.

## Expectations (registered)

- **P1:** a real 250-mode slice at `LSTEP=8, LMAXL=2000` takes 5–20 min of one core, the projection a minority of it.
- **P2:** retaining every integer ℓ in the window adds under 2× the slice time, because the window is 695 ℓ against the 238 of the `LSTEP=8` grid over 100–2000.
- **P3:** the total for both arms (17 slices) is 2–8 core-hours, inside a nightly-class budget of about 3 h wall on 4 workers, **for (S1)**. (S2) needs the shared-grid decision first.

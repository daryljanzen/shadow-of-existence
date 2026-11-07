# r7701+70 — PREDICTION (registered before the runs)

## Item 1 — the re-key (no run)

Both (L) banks' configs gain a per-row `numerics` record. All arrays stay byte-identical, checked as in r7693.

- **`p15_lowell_depths_leafpert_leafrec1` (HIER):**
  - FROZEN rows: `NTAU` 150000, `KLO` 0.1, `NLOW` 480, `NS3` unset (HIER's default 900), `ZEND` 0.
  - DECOUPLED rows: `NTAU` 150000, `NS3` 60000, `KLO` 0.1, `NLOW` 480, `ZDEC` 200.
  - These are the sweep's `CASES` entries as passed to `armB`.
- **`p15_lowell_depths_armA_leafpert_leafrec1` (CAMB through the shared projection):**
  - `KLO` 0.1 and **`NLOW` 320**. That is not arm B's 480: `camb_L.py` hard-codes 320, and I record it rather than leave it implied.
  - `NTAU` and `NS3` do not apply. The opacity is CAMB's, sampled on `camb_L.py`'s own grid of 2801 + 3001 times from η_rec − 160 to η₀, and the dynamics are CAMB's own integrator.

## Item 2 — the three knobs on HIER under (L), distances point, both builds

| knob | FROZEN | DECOUPLED |
|---|---|---|
| doubled opacity grid | `NTAU` 300000 | `NTAU` 300000 |
| halved late step count | `NS3` 450 (half its default 900) | `NS3` 30000 |
| extended continuum | `KLO` 0.02 | `KLO` 0.02 |

Every other setting is as in the banked (L) row. Banked as `spectra/p15_lowell_depths_leafpert_convergence_leafrec1.npz` (addition), with the knobs recorded per row.

**Expected sizes, from the same knobs on the control (`cc66_lowell_sweep.npz`):**
- On the control, `NTAU` doubled and `NS3` halved moved nothing at four decimals, and `KLO` 0.02 moved at most 0.0018 (0.39%, at ℓ = 2).
- (L) changes the dynamics' rate, not the numerics, so I expect the same scale:
  - **P1.** `NTAU` doubled: largest move ≤ 0.0005 at ℓ = 2–8 on both builds.
  - **P2.** `NS3` halved: ≤ 0.0005 on DECOUPLED (30000). FROZEN's halving (900 → 450) has never been run. It may move more, or go non-finite past z ≈ 10 as the receipt records for coarse late steps. I register ≤ 0.002 for it, or non-finite, either reported as found.
  - **P3.** `KLO` 0.02: ≤ 0.003 (≤ 0.7%), largest at ℓ = 2.
  - **P4.** The minimum stays at ℓ = 4 and the recovery at ℓ = 8 on every row.
- **Overall:** the largest move at ℓ = 2–8 across the six runs is under 1%, unless FROZEN's `NS3` 450 run is non-finite.

**Price:** six runs, four at a time: FROZEN about 70 s each, DECOUPLED about 10 min each. About 25 min in all.

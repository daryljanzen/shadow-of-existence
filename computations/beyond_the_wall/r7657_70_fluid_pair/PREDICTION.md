# r7657+70 — PREDICTION (pushed before any run)

**The fluid path on the arm of record.** The banked fluid pair is `cc66_cr_x_h686_fluid` + `cc66_lcdm_fluid`
(r6760+cc66.7). Its recipe, from that receipt's own docstring: `ARM=cr CRH0=68.6 CROM=0.2973 ZSTART=3e7 LEAFSCALES=1
LSTEP=2 LMAXL=1300`, with **`HIER` absent** (the fluid path; `HIER=1` is the polarisation path), against the
instrument's default control (D_M 13864.66). All five banked fluid spectra are LEAFREC=0.

**⛔ What I run against 69's switch list, and why.** The order lists `CRH0=68.570730 CROM=0.291246 HIER=1 LEAFGEOM=1
LEAFREC=1 LEAFSCALES=1 NS=1.015066 WBH2=0.021643`. Those are the switches, alphabetised and with ARM and SAVE dropped,
of `r7093_directions/grid_oneclock_leafrec1/cr_base.log`, which I banked at r7651.
- That is the **forbidden** configuration (`LEAFGEOM=1`) of the three-grid audit, not the arm of record. The arm of
  record is the licensed configuration, whose `config` records `LEAFGEOM: false`.
- That log's `HIER=1` is the polarisation path, which would not be a fluid run.
- Separately, 69's comparison figures (220.03/536.25/811.59/1125.11, 299.06, 2.291/2.349) are the **distances' point**
  (68.60/0.2973, `cc66_cr_x_h686_L2000_leafrec1_distances`), not the refitted 68.570730/0.291246.

So I run both readings of "the arm of record and its control", each on the fluid path (HIER absent, `LSTEP=2
LMAXL=1300`, `LEAFREC=1` set):
- **(a) `cc66_cr_x_h686_fluid_leafrec1_distances`.** The banked fluid arm's own sibling at 68.60/0.2973, the point
  69's figures are from. It pairs with the **default control** `cc66_lcdm_fluid`, which is re-run as a reproduction
  gate.
- **(b) `cc66_cr_fluid_leafrec1`.** The refitted arm of record (68.570730/0.291246/0.021643/1.015066, LEAFGEOM unset),
  with **its own control** `cc66_lcdm_fluid_refit` (LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248).

All are banked as additions (new files; nothing existing moves). Reader:
`P15_at_its_own_preferred_H0_…`'s two-path block, scored through its own `_matched` (lensed, the matched locator) and
`score` (133-bin unlensed).

**Measured before any run, with the receipt's own `_matched`:**

| | P1–P4 | comb | P1/P2 | P1/P3 |
|---|---|---|---|---|
| namesake pol `cc66_cr_x_h686_pol` | 221.11/538.62/815.48/1130.73 | 300.57 | 2.274 | 2.336 |
| arm of record pol `…_pol_leafrec1_distances` | 220.03/536.25/811.58/1125.05 | 299.04 | 2.291 | 2.349 |
| namesake fluid `cc66_cr_x_h686_fluid` | 220.55/530.63/812.95/1122.57 | 298.84 | 2.458 | 2.982 |
| default control fluid `cc66_lcdm_fluid` | 219.88/529.21/808.55/1116.09 | 296.80 | 2.401 | 2.810 |

**Predictions.**
- **(a)** The fluid arm moves by the polarisation path's own LEAFREC=0→1 shift:
  - peaks **219.5/528.3/809.1/1116.9 ± 1.5**;
  - comb **297.3 ± 1.0**;
  - P1/P2 **2.475 ± 0.03**, P1/P3 **2.995 ± 0.03**.
  - The fluid arm still overshoots its control in both height ratios.
  - Reachable negative: any band missed, which would mean LEAFREC acts differently on the two paths.
- **Control reproduction.** The default control re-run equals `cc66_lcdm_fluid` to < 1e-11 of the peak.
- **(b)** The refitted arm's comb is within 2.0 of (a)'s, and its heights within 0.06 of (a)'s. Its own control's
  heights are within 0.05 of the default control's 2.401/2.810. Reachable negative: outside these bands.

**EFFORT.** Four line-of-sight runs at LSTEP=2, LMAXL=1300: about 1 h wall on 4 cores.

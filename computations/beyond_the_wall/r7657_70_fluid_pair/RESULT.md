# r7657+70 — RESULT

**The fluid path now has arm-of-record banks.**
- **(a)** Prediction (a) holds almost exactly: at the distances' point, LEAFREC moves the fluid arm by the same shift it gives the polarisation arm.
- **(b)** Prediction (b) MISSED. On the *refitted* arm of record the fluid path's heights fall by 0.16 to 0.18, and the arm sits **below its own control** in both height ratios. The two-path height claim reads differently on the two arms of record.

`bank_measure.py` exits 0 and the logs are in `logs/`.

## What ran

The runs use the banked fluid pair's own recipe (r6760+cc66.7): `HIER` unset (the fluid path), `LSTEP=2 LMAXL=1300`, with `LEAFREC=1` set.

The order's switch list was the forbidden grid's log, not the arm of record. That log has `LEAFGEOM=1`, and its `HIER=1` is the polarisation path. PREDICTION.md gives the reasoning. So both readings ran:
- **(a)** `cc66_cr_x_h686_fluid_leafrec1_distances`: the banked fluid arm's sibling at the distances' point (68.60/0.2973). 69's comparison figures are from this point. It pairs with the **default control**. A re-run of that control reproduces `cc66_lcdm_fluid` **to 0.0**.
- **(b)** `cc66_cr_fluid_leafrec1`: the refitted arm of record (68.570730/0.291246/0.021643/1.015066, with `LEAFGEOM` unset). It pairs with **its own control**, `cc66_lcdm_fluid_refit` (LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248).

All three are **additions** (new files; nothing existing moves). Reader: `P15_at_its_own_preferred_H0_…`, which exits 0. Scoring uses that receipt's own `_matched` (lensed, the matched locator) and `score` (133-bin unlensed).

## The numbers

| spectrum | P1 | P2 | P3 | P4 | comb | P1/P2 | P1/P3 | 133-bin P1/P2 | P1/P3 | χ² |
|---|---|---|---|---|---|---|---|---|---|---|
| default control, fluid | 219.88 | 529.21 | 808.55 | 1116.09 | 296.80 | 2.401 | 2.810 | 2.392 | 2.766 | 3027 |
| namesake arm, fluid (LEAFREC=0) | 220.55 | 530.63 | 812.95 | 1122.57 | 298.84 | 2.458 | 2.982 | 2.448 | 2.934 | 4344 |
| **(a) arm, distances' point, fluid** | **219.57** | **528.34** | **809.09** | **1117.01** | **297.31** | **2.472** | **2.991** | 2.462 | 2.944 | 4801 |
| **(b) refit control, fluid** | 219.52 | 528.92 | 809.09 | 1116.76 | 297.19 | 2.397 | 2.854 | 2.388 | 2.809 | 3311 |
| **(b) refitted arm, fluid** | **221.15** | **528.38** | **809.92** | **1117.47** | **297.05** | **2.315** | **2.815** | 2.306 | 2.770 | 3874 |
| arm, distances' point, POL (69's reference) | 220.03 | 536.25 | 811.58 | 1125.05 | 299.04 | 2.291 | 2.349 | 2.281 | 2.312 | 584 |

**Prediction (a) ✔.** I predicted 219.5/528.3/809.1/1116.9 ±1.5, comb 297.3 ±1.0, and heights 2.475/2.995 ±0.03. The results are 219.57/528.34/809.09/1117.01, 297.31 and 2.472/2.991. LEAFREC acts on the fluid path as it does on the polarisation path. Old → new at the distances' point:
- peaks: 220.55/530.63/812.95/1122.57 → 219.57/528.34/809.09/1117.01;
- comb: 298.84 → 297.31;
- heights: 2.458/2.982 → 2.472/2.991.

The arm still overshoots its control on this path, by +3.0% in P1/P2 and +6.4% in P1/P3.

**Prediction (b) ⛔ MISSED.** The comb holds: 297.05, within 0.3 of (a). The refit control's heights also hold: 2.397/2.854 against the default control's 2.401/2.810. But the refitted arm's heights are **2.315/2.815**, which is 0.157 and 0.176 below (a), against a registered ±0.06. Against its own control, **P1/P2 is −3.4% and P1/P3 is −1.4%: on the fluid path the refitted arm of record sits below its control, where every other fluid arm sits above it.** I attributed the arm's heights to the point and to LEAFREC. The refit's ω_b/n_s move (0.021643/1.015066 against the built-in values) carries the larger share on this path, and I did not register for that.

## What this does to the two-path height claim

At the distances' point, the height *overshoot* persists on the fluid path: the comb is path-proof and the heights are not, as P15 says. On the refitted arm of record, the fluid path's heights fall **below** the control's. Which arm the claim is read on decides its sign on the fluid path. That reading belongs to cc66 and the paper's sentence to 69. Both banks are in place for it.

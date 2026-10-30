# r7639+70 — RESULT B: the retention statistic's own-comb form

**The function:** `r7637_70_own_comb_statistic/own_comb.py`. It provides `retained_own`, `retained_shared` (cc66's `retained`, lifted unchanged with its own `env_a` and `osc`), `retention_combs`, `slope12` and `retention_null`. The step statistic's rule is applied on both sides of the ratio: the arm's D_l goes onto the control's D_l comb coordinate, and the arm's source onto the control's source comb coordinate. Run `measure_retention.py` to reproduce the figures below (`measure_retention.txt`).

| | D_l combs (control / arm) | source combs (control / arm) | shared slope | **own-comb slope** |
|---|---|---|---|---|
| old arm | 1.0092 / 1.0092 | 1.0170 / 1.0160 | +0.01359 ± 0.00202 | +0.01002 ± 0.00142 |
| arm of record | 1.0092 / 1.0045 | 1.0170 / 1.0115 | +0.0269 ± 0.0123 | **+0.01034 ± 0.00137** |

On the arm of record, the own-comb band ratios at window 1 are 1.0364, 1.0708, 1.0659, 1.0699, 1.0858, 1.0827, 1.0832. The rise is smooth and band 1 is the lowest.

**Gr1 holds.** With each arm's comb parameters set to the control's, the own form equals cc66's `retained` on all twelve settings, to 4.4e-16 on the old arm and 1.8e-15 on the arm of record. The shared form reproduces the slope receipt's +0.01359 ± 0.00202.

**Gr2 holds, on the arm of record, at both amplitudes.** The real-phase null stays under a third of the own-comb slope:

| amplitude | real-phase null | share of slope | slope − null(real) |
|---|---|---|---|
| 0.5 (pre-registered) | +0.00328 | 0.32 | +0.00707 |
| banks' own, 0.231 / 0.937 (declared) | +0.00215 | 0.21 | +0.00820 |

Twice the setting spread is 0.0027. Reported and not gated: over every phase, the null's worst is **0.54 / 0.51** of the slope. On the old arm it is 0.21 / 0.48.

**The bands hold.**
- The arm-of-record own slope lies in [0, +0.015], with spread 0.0014, under the 0.004 limit.
- On the old arm the own slope (+0.0100) is below the shared slope (+0.0136). So, as with the step, the shared retention slope carried phase systematic even before: 0.0036 of it.

**The reachable negative does NOT fire. The settling outcome is reached.** On the own comb, the retention slope survives its real-phase null subtracted at **+0.0071 to +0.0082 per unit q**. That is 2.6 to 3.0 times twice its setting spread. Before subtraction it is **+0.0103**.

Old → new:
- P15's **+0.0139 ± 0.0021** (the shared comb on the LEAFREC=0 arm) becomes **+0.0103 ± 0.0014** on the arm of record (+0.0100 on the old arm).
- The shared reading on the arm of record, +0.0269 ± 0.0123, is the beat and is not a measurement.

As with the step: over every phase, at either amplitude, the null can reach about half of it.

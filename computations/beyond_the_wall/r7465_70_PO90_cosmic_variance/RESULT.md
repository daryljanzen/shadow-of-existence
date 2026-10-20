# r7465+70 — RESULT: PO-90 against the sector's own cosmic variance (registration `305237dfd`)

Run: `python3 measure.py` (exit 0; output in `measure.out`). Seed `20261020`; 10⁴ skies as the row asks, and 10⁶ for the tail.

| arm | registered | measured | verdict |
|---|---|---|---|
| **V-a** | MC = exact F(5,7) to < 3σ | all six cases within **0.4–1.0 σ** | **HOLDS** |
| **V-b** | p(CR), full sky, central: 0.055 (0.03–0.09) | **0.0539** (10⁶); 0.0507 at 10⁴ | **HOLDS** |
| **V-c** | 0.015 → 0.15 across the bracket | **0.0171 → 0.1555** | **HOLDS** at both ends |
| **V-d** | p(ΛCDM), central: 0.065 (0.04–0.10) | **0.0668** | **HOLDS** |
| **V-e** | p(CR), f_sky 0.78: 0.08 (0.05–0.13) | **0.0814** | **HOLDS** |
| **V-f** | BORDERLINE 60 % / TERMINATES 25 % / STANDS 15 % | **TERMINATES**: p = 0.054 ≥ 0.05 at the central sky | the 25 % branch |
| EFFORT | 1.5 h (1–3) | ≈ 0.5 h | low |

## What the numbers say
1. **⛭ Under the rule fixed before any draw, the row terminates as a result.** The central sky's selective quadrupole suppression (R = 0.238) is reached or exceeded by **5.4 %** of the construction's own skies.
2. **⚠ By a margin of 0.004 in p, which has to be read with it.**
   - At 10⁴ skies, exactly the number the row names, p = 0.0507. The 10⁴-draw sampling error is ±0.002, so that draw alone sits within about 0.3σ of the line.
   - On the most selective estimator in the paper's own bracket (Q 0.15, O 1.10), **p = 0.017**. On a cut sky (f_sky 0.78), every case rises: central 0.081, most selective 0.033.
   - **So "within cosmic variance" holds at the central sky and on a cut sky, and fails at 5 % on the most selective full-sky estimator.** That is the size of the item, now measured rather than "of order three".
3. **The floor is not what makes the shape unlikely.** The same statistic under ΛCDM gives **p = 0.067**: **p(CR)/p(ΛCDM) = 0.81**.
   - The single floor costs the selective-suppression shape 19 % of its probability, because the floor's ratio C₂/C₃ is 1.12, not 1.
   - **The rest is the sky's own low quadrupole, as unlikely under ΛCDM as under CR, to within that factor.** That is the row's *second* exit, *"the discrepancy shown to be the sky's own"*. It holds independently of the threshold: the construction is not what fails to produce the shape.
4. **What does not change:** P15's other statements, that the floor starves ℓ=2 and ℓ=3 *together* and that it produces no selective suppression, are true and stay true. What the measurement removes is the inference that this is a discrepancy *against the construction*. Read against cosmic variance, it is a ~2σ feature of the sky that ΛCDM shares.

## Scope, stated
- **Gaussian, isotropic skies:** Ĉ₂ and Ĉ₃ are independent χ². The quadrupole–octopole *alignment* is a separate anomaly (orientation, not power; `confront_lowell_data.py`) and is not touched.
- **The sky's R comes from the paper's own estimator ranges**, as fixed at registration. The central value uses the midpoints of those ranges. A different single estimator moves p along the bracket measured above, from 0.017 to 0.156.
- **The CR depths are the adjudicated exact-transfer ones.** The 1.4 % exact-filter shift on the ℓ=2-to-3 ratio (P15) moves the expectation ratio from 1.120 to about 1.104. That raises p slightly, which is the direction that does not threaten the verdict.

## Routed, not applied
- **For 66, the register:** PO-90 terminates by its own clause. My recommendation is to record **both** exits, the measured p (0.054 central, 0.017–0.156 across estimators) and the p(CR)/p(ΛCDM) = 0.81 reading, rather than the threshold alone, because the threshold is passed by 0.004.
- **For the paper owner, P15:** the sentence *"the observed sky's selective suppression of ℓ=2 alone, by a factor of order three, remains unaccounted for"* is now measured. On the sector's own Monte Carlo, the selective suppression has p ≈ 0.05 (and 0.07 under ΛCDM). The paper text is not mine to edit.

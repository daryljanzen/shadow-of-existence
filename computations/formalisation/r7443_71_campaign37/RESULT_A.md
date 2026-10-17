# `r7443+71.19` — RESULT: campaign 37 BUILT. ⌗ Row 73, every computed check of A–E: the Misner kinetic form, `R₃` DERIVED from the Koszul curvature (stronger than registered), its Taylor coefficients to order 4 along every ray, the two-mode Fock vertex shift `19κħ²/(27Va³) > 0`, its threshold `200/63`, and the residue arithmetic. ⌗ `841` lines against `450` (band 250–900). ⌗ Row 73 → `DONE`

*Scored against `PREDICTION.md` in this directory, pushed at `r7443+71.18` before any Lean was written. It is not
revised. `probes/Row73Vertex.lean` builds with no error and no warning, and its 27 theorems print `[propext,
Classical.choice, Quot.sound]` (`PROBE_RUN_A.txt`, `13 s`). No `native_decide` is used. The build was done by a
delegated agent and re-run by 71 before this record.*

## ⛔ The stop, scored

***Not fired.*** `841` lines, under `1300`. It is near the top of the band.

## What was built

| section | theorems | what they prove |
|---|---|---|
| A | `misner`, `unimodular`, `R3_round`, `R3_milnor`, `taylor`, `shapes`, `calibration` | `KK − K² = −6H² + 6(β̇₊² + β̇₋²)` with no cross term. ***`R₃` is the Koszul scalar of `diag(e^{2bᵢ})`***: Milnor's formula is re-proved in the file, where it was registered as typed. For every ray and every `n ≤ 4`, the `n`-th derivative at `0` is `n!·qₙ`, giving `6, 0, −48(β₊² + β₋²), 160(β₊³ − 3β₊β₋²), −336(β₊² + β₋²)²`. `q₃ = 160 Re(β₊ + iβ₋)³`. And `μ² = 8 = 3² − 1`, `d = 10` |
| B | `kinetic_linear`, `kinetic_exponential`, `unit_jacobian` | the kinetic term in `h` with its explicit remainder. The exponential variable has no field dependence at any order. The Jacobian at `0` is `1` |
| C | `quartic_vev`, `cubic_three_quanta`, `one_quantum_cancels`, `cubic_shift`, `fock_receipt`, `normalisation`, `total_shift`, `at_level_three`, `threshold`, `density_a6` | on a two-mode ladder algebra: `⟨V₄⟩ = 8c₄s²`. `V₃\|0⟩` lives on exactly two three-quanta states, and the one-quantum amplitude cancels. `dE₃ = −8g²s³/ħω` for any box with `N ≥ 4`, the receipt's `7` and the full ladder included. The total is `4κħ²(63μ² − 200)/(27Va³μ⁴)`, which is ***`19κħ²/(27Va³) > 0`*** at `μ = 2√2`. It is positive exactly above `200/63`, and the density scales as `a⁻⁶` |
| D | `linear_solves`, `rank_two` | unique at first order, a free family at second, and the Jacobian rank is `2` |
| E | `dmu_residues`, `dovmu_residues`, `faulhaber`, `log_coeff`, `residue_product` | the coefficients `2, −9, 15/4` and `2, −7` as limits. The Faulhaber closed forms, the log coefficient `15/4` (Euler–Mascheroni) and the product `½` |

## Caveats, beside the score

- ***Imported, labelled in the file:***
  - the identification of the frame-constant sector with `diag(e^{2bᵢ})`;
  - the TT spectrum beyond `m = 3`;
  - the RS second-order formula, as a formula and not an eigenvalue theorem;
  - the receipt's typed action normalisation and its scale-factor bookkeeping.
- ***Not built:***
  - the paper-text parse, which is a pin; its expression is proved by `misner`;
  - the receipt's section F, outside the registered A–E;
  - the Dirichlet series behind E's "pole" wording. E is built as the coefficients and limits the receipt computes.

## The probabilities

| quantity | p | outcome |
|---|---|---|
| built under the stop | `0.45` | ***yes***, `841` |

## Census (moved in this push)

***Row 73 → `DONE`***, `decl` filled with the 27 names. Library gap `8 → 7`, DONE `86`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

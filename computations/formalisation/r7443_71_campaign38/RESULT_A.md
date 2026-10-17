# `r7443+71.20` — RESULT: campaign 38 BUILT IN FULL, section C included. ⌗ Row 63: the anomaly's rank 3 is proved with no numerical integration, by a layered Vandermonde sign argument, and for EVERY `r > 0`, not only `r = 15/4`. ⌗ `915` lines against `380` (band 200–800): ***the band is missed, high***. ⌗ Row 63 → `DONE`

*Scored against `PREDICTION.md` in this directory, pushed at `r7443+71.18` before any Lean was written. It is not
revised. `probes/Row63Anomaly.lean` builds with no error and no warning, and its 27 theorems print `[propext,
Classical.choice, Quot.sound]` (`PROBE_RUN_A.txt`, `14 s`). No `native_decide` is used. The build was done by a
delegated agent and re-run by 71, who read the C statements against the receipt before this record.*

## ⛔ The stop and the band, scored

- ***The stop was not fired:*** `915` lines, under `1200`.
- ***The band was missed, high:*** `915` against a ceiling of `800`. The C proof, which the registration gave
  `p 0.20` and expected might be only reported, was built, and it cost the overrun. Recorded, not adjusted.

## What was built

| section | theorems | what they prove |
|---|---|---|
| A | `A1_cosh`, `addot_of_constraint`, `A2_variance`, `A2_const`, `A2_sign`, `A2_sample`, `A3_radiation`, `A3_flat` | `R = 12/α²` on `α cosh(t/α)`, with derivatives by `HasDerivAt`. The variance identity and its consequences. `Λ + radiation` gives `R = 4Λ` with `dR/da = 0` |
| B | `B1_bare`, `B2_trace`, `B3_R`, `B3_slope`, `B3_iff` | `Θ = 0` bare. `Θ = r/(2π²a⁴)` for every `C` and `μ`. `R = 4Λ + 4Gr/(πa⁴)`, and `dR/da ≠ 0 ↔ r ≠ 0` |
| C | `rank_one_of_const`, `moment_det_neg`, `C_controls`, `C_tower`, `C_receipt`, `adot_sq`, `Rtow_eq` | `triples` IS the receipt's matrix `2π²∫a³R^k/ȧ` over `[2,3], [3,5], [5,9]`, with `ȧ` and `R` tied to B3's constraint. Both null controls have rank 1. ***The tower has `det < 0` and rank 3 for every `r > 0`***. The receipt's three cases give ranks `1, 1, 3` |
| D | `zeta_rule_eq`, `Bj_zero`, `B3_zero`, `zeta_free_tower`, `zeta_protected`, `zeta_odd`, `series_inputs`, `rule_is_limit` | the receipt's formal rule as an explicit definition: the free tower gives `10`, the protected shifts give `10`, `+cm` gives `10 + 3c − c³/3`, `+c/m` gives `10 − c`, all independent of `M` and `J`. Each summand is the `s → 0` limit, through `riemannZeta_residue_one` |

***How C was proved.*** The rows are the integrals of `1`, `R` and `R²` against a positive weight over three
consecutive intervals, and `R = 4Λ + κ/a⁴` is strictly decreasing when `r > 0`. The determinant is expanded one row
at a time, and each layer is a Vandermonde factor `w·(z − y)(R − y)(R − z)` on ordered values. So each layer has a
strict sign, and `intervalIntegral_pos_of_pos_on` gives `det < 0`. ***The registration's "rank 3 needs verified
numerics" was wrong: the property is structural.***

## Findings inside the receipt (Lean follows its checks, which pass)

1. Its docstring gives `s₃/s₁ = 9.06e-8` for the tower; its run prints `1.394e-8`.
2. Its docstring ⓶ gives `δ = cm ⇒ Δζ(0) = c − c³/3`. Its check, and Lean, give `3c − c³/3` at the base `m² − 1`.
3. Its free-tower print label says `λ = m² − 3`; the code uses `m² − 1`.

These are text-against-code discrepancies in the receipt. They are routed to its owner and not corrected here.

## Caveats, beside the score

- ***Imported:***
  - `r = 15/4` and `ζ₀ = 10` as banked. In Lean `r` is a parameter and `10` is derived by the rule;
  - the semiclassical `C + r log(aμ)`;
  - the TT spectrum and degeneracy;
  - the typed closed-FRW `R`.
- ***Not built:***
  - the SVD's singular-value numbers. The exact ranks they measure are proved;
  - the genuine meromorphic `ζ_Δ`; D is the receipt's formal rule;
  - the paper-text parses, whose values are proved.

## The probabilities

| quantity | p | outcome |
|---|---|---|
| A, B and formal D built | `0.40` | ***yes*** |
| C rank 3 built | `0.20` | ***yes***: the low call was wrong, in the direction of the property being structural |

## Census (moved in this push)

***Row 63 → `DONE`***, `decl` filled with the 27 names. Library gap `7 → 6`, DONE `87`.

***Also in this push:*** rows 64, 68 and 73's `decl` cells are brought to the full lists of their files' headline
theorems. They had been written from incomplete shell captures. The text cells now name every theorem.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

# `r7443+71.17` — RESULT: campaign 36 BUILT. ⌗ Row 68, every computed check of A–E: the completeness relation in all 81 components, Wick's theorem on a ladder algebra for EVERY truncation keeping levels 0–2 (the receipt's five levels included) and for the full ladder, and the ten dimension-eight invariants by a contraction lemma. ⌗ `530` lines against `380` (band 200–800). ⌗ Row 68 → `DONE`

*Scored against `PREDICTION.md` in this directory, pushed at `r7443+71.15` before any Lean was written. It is not
revised. `probes/Row68Overlap.lean` builds with no error and no warning, and its 19 theorems print `[propext,
Classical.choice, Quot.sound]` (`PROBE_RUN_A.txt`, `26 s`). No `native_decide` is used; the only `decide` calls are
kernel decides over `ℤ` and over `Finset (Fin 3)`. The build was done by a delegated agent and re-run by 71 before
this record.*

## ⛔ The stop, scored

***Not fired.*** `530` lines, under `1100`.

## What was built

| section | theorems | what they prove |
|---|---|---|
| A | `traceless`, `orthonormal`, `completeness`, `trace_P`, `level_three`, `drop_one` | the five-element basis, with entries `1/√2` and `1/√6`, is traceless and orthonormal on all 25 pairs. `Σ_k h_k^ab h_k^cd = ½(δδ + δδ) − ⅓δδ` holds in ***all 81 components***, with `tr P = 5`. The level sums are `5`, `10 = d(3)`. Dropping one element fails in exactly `9` components, the receipt's own count |
| B | `exponent_zero` | the residual is the same constant `c/(2π²)` for every label pair. The rate is `6 − 2s`, zero exactly at `s = 3`. `d(3) = 10 < d(4) = 24` |
| C | `two_point`, `wick`, `wick_receipt`, `support`, `factorises` | on a ladder algebra over `(Fin 3 → ℕ) → ℝ`, with a truncation parameter: `⟨0\|q_iq_j\|0⟩ = δ_ij/(2w_i)`. ***All 81 quartic vacuum values equal their Wick sums*** for any truncation keeping levels 0, 1 and 2, the receipt's five levels and the full ladder included. The support is one or two labels, both occurring, and the two-label value factorises |
| D | `contract`, `eight_values`, `eight_homogeneous`, `value_rank_one`, `pow_homogeneous_3_to_6`, `combo_homogeneous` | the contraction lemma `Σ R^ab_cd Y^cd = K(Y^ab − Y^ba)` replaces the `4⁸` brute force. The ten invariants are `256, 64, 128/3, 16, 64/9, 32/3, 4, 16, 64/9, 32/27` times `Λ⁴`, each homogeneous of degree 4 by `deriv`. Their ratio span has rank 1 |
| E | `trivia` | `log 2 ≠ 0` and the convention count |

- ***Stronger than the receipt in one place.*** The receipt computes Wick on a 125-state truncated box. Here it is
  proved for every truncation that keeps levels 0–2, and for the untruncated ladder. So the receipt's
  "the truncation does not matter" is a theorem.

## Caveats, beside the score

- ***Imported, labelled in the file, not built:***
  - the level-summed density for general `m` (Schur and homogeneity), with `Sigma` defined as that import's
    consequence. This is the genuine spectral foundation, and it stays the spectral library's;
  - `∇Riem = 0`;
  - `d(m) = 2(m² − 4)`.
- ***B's "zero derivative in the labels"*** is stated as "the same constant for every label pair", not by `deriv`.
- Paper-text checks are pins.

## The probabilities

| quantity | p | outcome |
|---|---|---|
| built under the stop | `0.45` | ***yes***, `530` |

## Census (moved in this push)

***Row 68 → `DONE`***, `decl` filled with the 19 names, `330` pairs `ok` on the tree audit. Library gap `9 → 8`.
DONE `85`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

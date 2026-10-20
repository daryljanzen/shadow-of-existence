# `r7443+71.36` — RESULT: campaign 45 BUILT. ⌗ Row 60, every computed check A–E with the spectrum imported; Part A reaches the rank certificate within the candidate span; Part B's identity is proved on the TT variety, not fitted; both level sums are proved negative for every `m ≥ 3`. ⌗ `1228` lines against `1700` (band 900–2800, IN BAND). ⌗ p `0.25` came true. ⌗ Row 60 → `DONE`

*Scored against `PREDICTION.md` in this directory, pushed at `r7443+71.34` before any Lean was written. It is not
revised. `probes/Row60Levels.lean` builds with no error and no warning. All 14 headline theorems print
`[propext, Classical.choice, Quot.sound]` (`PROBE_RUN_A.txt`, `388 s`). No `native_decide`; the 21 integer
`3⁵`-sums use `decide +kernel`. The build was done by a delegated agent and re-run by 71 before this record.*

## ⛔ The stop, scored

***Not fired.*** `1228` lines, under `3400`.

## What was built

| part | theorems | what they prove |
|---|---|---|
| A | `invariant_basis`; `cert4`, `cert5`, `cert6`, `ker5_*`, `C_minor`; `P6_cond`, `B0_cond`, `C1i_cond`, `C2i_cond`; `trace_relation_fixes`, `full_traces`, `level_tensors_cond` | the δ/ε basis `P6`, `B0`, `C1i`, `C2i` meets every symmetry, tracelessness, transversality and pair-exchange condition (componentwise, `decide +kernel`). ***Rank certificate:*** any rational combination of the receipt's candidates that meets the conditions is a multiple of the basis. Rank 4: 3 candidates. Rank 5: 10 candidates, with 4 kernel relations exhibited. Rank 6: 15 candidates. So the dimensions are `(1,1,2)` ***within the span***. The trace relation fixes one of C's two numbers; `tr C = λ·deg` for every `c_C`, `tr A = deg`, `tr P = 5` |
| B | `second_order_identity`, `B_unique`, `scal_second_order`, `control_frame_constant`, `Box.control_euler_box`, `part_B` | row 62's `jet_series` (orders 0–2). On the TT variety (12 linear constraints in 50 jet coordinates), `scT2 = −¼∇h∇h + 0·(mixed) − ½hh`, by an explicit `linear_combination`, ***not fitted***. The coefficients are forced (three rational TT jets, determinant `−191472`), so the mixed coefficient is exactly `0`. Controls: `−2 tr h²` at frame-constant `h`; row 59's `R₂` integrand and its Euler-box `−16π²` |
| C | `seven_level_values`, `level_object_eq`, `weights_nonzero`, `level_sums_in_tower_variables`, `level_sums_sign`, `level_sums_sign_nat`, `part_C` | the seven level values reduce to `49/48·c_C·deg − 13/480·λ·deg² − 45·c_B²`, all three weights nonzero. Under the imports the second-order sum is `−¼·deg·μ²` and the fourth-order sum is `−(1/120)deg²(5μ² + 4)`. Both are `0` at `m = 2` and ***negative for every `m ≥ 3`, real or natural, proved by positivity rather than sampled*** |
| D | `cross_factorises`, `faulhaber`, `faulhaber_leading` | the cross-level sum factorises and its diagonal is C's level object; Faulhaber closed forms by induction, degree 5 with leading coefficient `−1/10` and degree 7 with `−1/42` |
| E | `sign_algebra` | honest = banked · `(2c₄/μ²)`; the two forms agree in sign for `c₄ > 0`; the counterexample at `(−1, 1, 8)`; honest `< 0` for `c₄ < 0` at every tower level |

## Imports, stated in the file as imports

- the spectrum `λ = m² − 3`, `deg = 2(m² − 4)`, `μ² = m² − 1`;
- `c_C = −(m² − 4)(m² + 5)/35`;
- the parity `c_B = 0`, as a hypothesis;
- the seven r7032 coefficients;
- the seven contractions, as transcribed (the count of 372 is not re-proved);
- the Wick-tensor ansatz.

Completeness of the δ/ε span is not claimed. The paper-text checks are not formalised.

## Two slips in the receipt's TEXT, routed to its owner

The receipt's computations are right and its gates pass. Two strings in it are wrong:

1. ***Docstring, line 10:*** "`45 * c_B^2` before parity". The computed weight is ***`−45`***; the receipt's own run
   prints `−45`, and Lean proves `−45`.
2. ***Section E's gate text, line 634:*** "honest `−9/8`" at `(c₄, g², μ²) = (−1, 1, 8)`. The value of
   `2c₄ − g²/μ²` there is ***`−17/8`***; the banked `17/2` is right. The sign conclusion is unaffected. The Lean file
   states `−17/8`.

## Against `r7453_71_gap_class/CLASS.md`

That file read row 60 as reachable with the spectrum imported, as rows 70 and 73 are. ***This build confirms
it:*** row 60's label `spectral theory` named a structure whose derivation no row computes, and whose values each
row imports.

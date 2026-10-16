# `r7419+71.2` — RESULT: `ROWS.tsv` carries `receipt` (all `111`) and `decl` (all `87` rows with something built). ⌗ The `11` ABSENT all resolve: they were in `r7315_71_sweep/RESULT.md`'s step table, which names rows as a `# | row` table rather than as "row N". ⌗ Of the `33` PARSE cells, `4` name something not declared in the named file, against a registered `3` (band 0–8): inside

*Scored against `PREDICTION.md` in this directory (pushed at `r7419+71.1`, before the selector was written or run).
It is not revised. The selector is `derive_join.py`, committed with its output `JOIN.tsv` and its run `RUN.txt`.
Rerun from the repository root:
`python3 computations/formalisation/r7419_71_join/derive_join.py computations/beyond_the_wall/r7419_66_the_formalisation_join/JOIN_SCOPE.tsv --write`.*

## What the columns are

- ***`receipt`:*** the receipt path, for every row. It is `r7285_71_restate/READINGS.tsv`'s path, which is the
  receipt each row was read from.
- ***`decl`:*** `repo-relative file: Namespace.name, …`, grouped by file, with ` | ` between files. It is filled
  for `DONE` (`74`), `DONE (chartable half)` (`2`), `LIMIT OF A DONE ROW` (`10`; the cell lists the carrying
  theorems) and the one `ORDER` row (`59`; what is built so far). That is `87`. It is ***empty by rule*** for
  `ROW`, `LIBRARY GAP` and `GENERIC-METRIC`: their cells may name a theorem without being carried by it, and row
  40's cell naming `sinh23_flow` is the case that made the rule necessary.
- ***How a name gets in:*** the selector indexes every `theorem`/`lemma`/`def`/… in `computations/formalisation/lean`
  by namespace and file. A name enters `decl` only if it is declared in the file written beside it. Candidates come
  from four places:
  - the row's own cell;
  - `JOIN_SCOPE`'s identifiers;
  - the sweep's per-step new declarations (consecutive `PROBE_RUN_B<k>.txt` files);
  - four rows read by hand and cited in the selector's `MANUAL`: 52, 72, 75, 99.
- ***Independent re-check:*** every one of the `258` names in the column was grepped for as a declaration in its
  stated file, and all `258` were found. That check is syntactic, at the level of `60`'s gate. It is not a Lean
  `#check`, because probes cannot be imported. ***`60`'s gate is still the verdict.***

## The registration, scored

| quantity | registered | measured | |
|---|---|---|---|
| ABSENT rows resolving to declared names | all `11`, p `0.85` | ***`11` of `11`*** | ***came true*** |
| PARSE cells naming an identifier not declared in the named file | `3` (0–8) | ***`4`*** | inside |

- ***The 11 were never absent.*** Each cell says "discharged in B (r7315)", and the sweep's `RESULT.md` maps each to a
  step `B<k>`. What made them look absent is that `probes/CurvatureProbe.lean`, the file the runs name, has
  since been folded into `ShadowEngine.lean` as sections `SweepB1`–`SweepB18`. The registered risk was a rename in
  that move, and it did not happen.
- ***The four PARSE misses, which are the gate working as the order said it would:***
  - row 6: `d_b` is notation in prose, not a declaration;
  - row 17: `nariai_curvature` is in `probes/CurvatureInstances.lean`, not in the `NonDiag.lean` the cell names, and
    `r_N` is prose;
  - row 19: `frw_closed` is in `SecondSeatFRW.lean`, and `frw_scal`, `frw_weyl` are in `ShadowEngine.lean`, not in
    the `FRWk.lean`/`RunningLayer.lean` named;
  - row 77: `coord_not_killing` and `gowdy_coord_not_killing` are in `probes/Row77Killing.lean`, not in the
    `ShadowEngine.lean` named, and `d_t`, `d_z`, `g_xx`, `g_yy` are prose.

  In every case the selector put the real theorem with its real file. ***The prose cells were wrong about files in
  three rows of `33`, and that is the measure of how far the cell's prose can be trusted.***

## Caveats, beside the score

- ***A `decl` cell lists what the row's campaign BUILT, helpers included.*** For the sweep rows it is every
  declaration new at that step, so `lcGam_diag` sits beside `slice_gauss` for row 34. The headline is not
  marked separately. Separating it would mean re-reading every proof, which the order rules out.
- ***`decl` says which theorem carries the row, not that it carries all of it.*** The scope notes ("not claimed",
  open halves) stay in `what it needs next`, where they were.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

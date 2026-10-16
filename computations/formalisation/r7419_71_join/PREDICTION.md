# `r7419+71.1` — PRE-REGISTRATION: the `receipt` and `decl` columns on `ROWS.tsv` (`r7419` ①–②). ⌗ The `11` ABSENT first: all `11` resolve to declarations that exist, p `0.85`. ⌗ Of the `33` PARSE lifts, `3` name an identifier NOT declared in the named file (band 0–8)

*Order: `FOR_71.md` §`r7419`. Written after reading the order, `JOIN_SCOPE.tsv`'s header and the 11 ABSENT rows'
cells (each says "discharged in B (r7315)"), and before any selector is run or any identifier is checked
against the Lean tree.*

## What I expect

- ***The 11 ABSENT are not absent.*** Each cell says "discharged in B (r7315)", and
  `r7315_71_sweep/RESULT.md` has a table `# | row` mapping each to a step `B<k>`. Each step has a
  `PROBE_RUN_B<k>.txt`. The search in `JOIN_SCOPE` looked for "row N" and missed the table form. ⇒ All 11 resolve,
  p `0.85`.
  - ***The risk:*** `probes/CurvatureProbe.lean`, which those runs name, is no longer in the tree. Its
    declarations will have moved, probably into `ShadowEngine.lean` or `ShadowFormal/`. A declaration renamed in
    that move would not resolve by name.
- ***PARSE is a starting point, not a verdict*** (the order's words). I expect `3` of the `33` to name an
  identifier that is not declared in the named file (band 0–8). The likely causes are a probe-local re-proof
  named after its engine original, and the old `CurvatureProbe.lean` path.
- ***The method, fixed now:*** a selector (`derive_join.py`, committed with its output) indexes every
  `theorem`/`lemma`/`def` in `lean/` by file. A `decl` cell is filled ONLY with names found in the file it names.
  Each row's names come from its own cell, `JOIN_SCOPE`'s identifiers, and the campaign tables, and are then
  checked against the index. Where a name is declared in several files, the cell names the file the row's
  campaign built.
- ***Scope:*** `receipt` for all `111` rows, which is the same as `READINGS.tsv`, so a lookup. `decl` for every
  row that has a built declaration: the `84` DONE and LIMIT rows, and the halves and the ORDER row, with what is
  built so far.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

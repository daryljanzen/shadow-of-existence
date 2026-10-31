# `r7643+71.2` — PRE-REGISTRATION: the inventory of P1, `r7643` ②, and the method by which the next campaign is proposed

*Under `r7643` ②. The inventory is a reading, not a Lean build. What is registered here is the method, so that the
classification cannot drift toward a conclusion.*

## The method

***The population.*** Every `theorem`, `proposition`, `lemma` and `corollary` environment of
`corpus/BH_causality_v2.tex` at the merged base. A grep finds `8`:
- `thm:metric-singularity`;
- `cor:threefold`;
- the EF-degeneracy corollary;
- `lem:killing`;
- `cor:stationary`;
- `prop:causal-alignment`;
- `cor:densities`;
- `lem:alignment`.

Remarks are listed, but only where they make a claim the proof of one of these uses.

***What each row carries.***
- The clauses of the statement, as P1 states them now, after `r7643`.
- For each clause, the probe and theorem name that formalise it, read from the probe itself and not from memory.
- A mark:
  - **BUILT**, when the Lean statement covers the clause under hypotheses no stronger than P1's, and is non-vacuous;
  - **BUILT IN PART**, with the gap named, for a stronger hypothesis, a reduced setting (a chart or 2D) or a missing
    non-vacuity witness;
  - **NOT BEGUN**.
- A probe whose hypotheses were later found unsatisfiable (campaigns 74–75, under the old `IsTemporal`) counts only
  through its repaired successor.

***The proposal.*** The next campaign is chosen by one rule: the NOT BEGUN or BUILT IN PART clause that P1's headline
conclusion rests on most directly, with "the event horizon occurs on no finite exterior slice" as the headline. Ties
are broken toward the smallest Lean cost. The reason is written beside it.

***Registered expectations*** (failable). `prop:causal-alignment`'s accumulation and finite-slice clauses come out BUILT,
via campaigns 72 and 78–79. Its tangency clause comes out BUILT IN PART until campaign 80 lands. `cor:densities` comes
out NOT BEGUN. At least one of the metric-singularity statements comes out BUILT IN PART on the 4D or angular
reduction. p `0.6` that all four expectations hold.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

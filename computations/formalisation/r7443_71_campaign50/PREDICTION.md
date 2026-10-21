# `r7443+71.50` — PRE-REGISTRATION: campaign 50, the three ROW objects (18, 53, 86), each built to the object itself or to a named Lean obstruction. ⌗ `1200` lines across three probes (band 500–2500), ⛔ stop `3500`. ⌗ p per row: 18 `0.25`, 53 `0.50`, 86 `0.45`

*Under `r7443`: a row leaves the list only by being `DONE`, or by being built far enough to show a specific Lean
obstruction. Each row's computable residue is already built (campaigns 26 and 32). What remains is the ROW object
the census names. No Lean was written before this registration. Receipts are in ROWS.tsv, column 6.*

## ① The pieces

***Row 18 — the S₃ monodromy of the cubic's root cover over the punctured mass line*** (`probes/Row18Monodromy.lean`).
- ***Route A, algebraic.***
  - The family cubic is irreducible over `ℚ(M)` (or at a rational specialisation `M₀`), and its discriminant is not
    a square.
  - So its Galois group is `S₃`, by Mathlib's `Polynomial.Gal` results for prime degree with two non-real roots,
    at a specialisation.
- ***Route B, topological.***
  - The root map is a covering over the complement of the branch locus: distinct roots plus the implicit function
    theorem.
  - Each loop around a branch point acts as a transposition (row 18's `no_triple_root` already gives simple
    branching).
  - Two distinct transpositions generate `S₃`.
- Whichever step Mathlib lacks is the named obstruction. ***The likeliest one:*** identifying topological
  monodromy with the Galois group, which is Riemann existence, or path lifting for this cover.

***Row 53 — the essential image of the range map*** (`probes/Row53Image.lean`).
- State the receipt's "range is the essential image" as the image of the parameter-to-solution map, or as
  Mathlib's `Functor.essImage` if the receipt's object is a functor.
- Prove it equals the receipt's solution class, building on `sds_kernel` (every solution is exactly one family
  member) and `typeD_four`.

***Row 86 — the `Z₃` action on loci of the quadric*** (`probes/Row86Action.lean`).
- Define the action exactly as the receipt does (from its own construction) as a `MulAction (Multiplicative (ZMod 3))`
  or an explicit order-3 map.
- Prove it preserves the quadric, permutes the named loci as the receipt says, and has the receipt's fixed set
  (the "singlet for the axis pair" question).

***Failable,*** per row: `DONE` when the object is built; otherwise the step that blocks it is named, and the row
stays ROW with that obstruction recorded. That is the order's other exit, and is not a reclassification.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

# `r7443+71.1` — PRE-REGISTRATION: campaign 28, row 59's rank 8, the derivative sector's pointwise dimension. ⌗ `260` lines (band 150–500), ⛔ stop `700`. ⌗ p `0.55`

*Under `r7443` ②, the standing order: row 59 first, no "build it" tag needed. The receipt
(`P10_the_algebraic_quartic_is_settled_by_…_eight.py`) was re-read at section D. One pricing run was made with sympy
before this registration, and no Lean was written before it:*
- *the `10`-slot matchings of `∇h ∇h h h`, with no pair inside one tensor, number `372`;*
- *on the admissible jet, parametrised by `5` coordinates for `h` and `12` for `∇h`, they give only `13` distinct
  polynomials;*
- *the `372` coefficient vectors over the `294` monomials have rank ***8***, so the receipt's random-jet `8` is the
  exact dimension of the polynomial span and not a sampling artefact.*

## ① The piece: `probes/Row59Rank.lean`

- ***The jet, as the receipt takes it.***
  - `h` is symmetric and traceless, parametrised by `a : Fin 5 → ℚ`.
  - `∇h` is `G p r s`: symmetric in `r s`, traceless in `r s`, and divergence-free in `p r`, parametrised by
    `v : Fin 12 → ℚ`. The parametrisation is the receipt's nullspace solved for six coordinates.
- ***Admissible both ways:***
  - each parametrised `G` satisfies the three conditions;
  - every `G` satisfying them is the parametrisation of its own free coordinates.

  So a statement on the parameter space is a statement on the admissible jets.
- ***The sector.***
  - The `13` distinct contractions are written in Lean as explicit index sums over `Fin 3`.
  - Each is one matching of the receipt's, chosen as the class representative.
  - Each is read as a function on `(Fin 5 → ℚ) × (Fin 12 → ℚ)`.
- ***(D) `sector_rank_eight`:*** the `ℚ`-span of the `13` functions has `finrank` exactly `8`.
  - Lower bound: `8` of them are linearly independent, by an `8 × 8` evaluation matrix at `8` rational jets with
    non-zero determinant.
  - Upper bound: the other `5` are in their span, by explicit polynomial identities.

***Caveats, registered.***
- The reduction of the `372` matchings to the `13` distinct polynomials is the sympy bookkeeping above. It is not
  built in Lean. The Lean theorem is the dimension of the span of those `13`.
- The receipt's integrated "at most seven" is not in this piece.

***Failable:*** BUILT, BUILT IN PART, or REPORTED. p `0.55`.
- ***Risk:*** each contraction expands to `243` products of four linear forms before `ring` closes the identities.

***Census if BUILT:*** row 59 stays `ORDER: ENGINE-REACHABLE`. Its "still to build" drops the rank 8 and keeps the
integrals of the non-constant `H4` series. Its `decl` gains the new names in the same push.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

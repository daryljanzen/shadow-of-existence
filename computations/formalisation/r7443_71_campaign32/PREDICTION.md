# `r7443+71.8` — PRE-REGISTRATION: campaign 32, step 3: the computable parts of structure rows 53 and 86. ⌗ `140` lines (band 70–300), ⛔ stop `420`. ⌗ p `0.70`

*Under `r7443` ②, step 3. Row 18's computable residue was built at campaign 26. The two receipts were re-read:
`P09_range_paper/K7_range_is_essential_image.py` (row 53) and
`P14_matter_sector_paper/P14_is_there_a_singlet_for_the_axis_pair.py` (row 86). No Lean was written before this
registration. The rows' own objects, an essential image (53) and a `Z₃` action on loci (86), stay the ROW objects,
as `r7421` ruled.*

## ① The piece: `probes/Row53Row86.lean`

***Row 53, the fibre counts of the essential image.***
- ***`sds_kernel`.*** Two halves:
  - `f = 1 − 2M/r − Λr²/3` solves `r f' + f − 1 + Λr² = 0` on `r > 0` for every `M`;
  - every differentiable solution on `r > 0` is of that form for exactly one `M`.

  So the SdS kernel is a one-parameter family: the receipt's "`1` for SdS", proved as a classification, where the
  receipt counts a symbol set.
- ***`typeD_four`.*** The Type-D quartic pair has leading coefficients `−Λ/3`, opposite `c₂` and a shared `c₀`. The
  map `(c₂, c₁, c₀, d₁) ↦ (D_r, D_p)` is injective as functions. So the family has exactly four parameters, the
  receipt's "FOUR".
- ***`orbit_dims`.*** The receipt's stratum arithmetic is `n(n − 1)/2` at `n = 3, 5, 6`. This is built as the dimension
  of the skew-symmetric `n × n` real matrices, `finrank = n(n − 1)/2`, for those `n`.

***Row 86, the branch count.***
- ***`branch_count`.*** Over `ℂ`, `z² = X² − α²` has exactly one root when `X² = α²` (the throat) and exactly two
  distinct roots otherwise. That includes `X = 0`, the axis, where the pair is imaginary and not absent.

***Caveats, registered.***
- None of this moves the rows. 53 and 86 stay `ROW: A DIFFERENT KIND`, and `decl` stays empty, by rule. Any
  residue link goes on the page phrase.
- `orbit_dims` is the matrix count, not the isotropy groups' own Lie algebras inside `so(5,1)`.

***Failable:*** BUILT, BUILT IN PART, or REPORTED. p `0.70`.
- ***Risk:*** the skew-symmetric `finrank` for general `n`. A fallback is per `n`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

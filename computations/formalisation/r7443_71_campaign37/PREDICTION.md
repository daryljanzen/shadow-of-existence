# `r7443+71.18` — PRE-REGISTRATION: campaign 37, library-gap row 73 (the vertex numbers are exact at the level this row owns). ⌗ `450` lines (band 250–900), ⛔ stop `1300`. ⌗ p `0.45`

*Under `r7443` ②, step 4, next in `PRICING.md`'s order. The receipt is
`P10_the_vertex_numbers_are_exact_at_the_level_this_row_owns_and_the_whole_scheme_is_one_series_pole_data.py`. No
Lean was written before this registration.*

## ① The piece: `probes/Row73Vertex.lean`

The receipt's computed checks are sections A–E as `PRICING.md` lists them.
- ***A.***
  - the Misner `KK − K² = −6H² + 6(β̇₊² + β̇₋²)`, with no cross term;
  - the unimodular product is `1`;
  - `R₃ = 2(2Σλ_iλ_j − Σλ_i²)`, with value `6` at `β = 0`;
  - its Taylor coefficients to order 4: `−48(β₊² + β₋²)`, `160(β₊³ − 3β₊β₋²)` and `−336(β₊² + β₋²)²`;
  - `μ² = 8 = m² − 1` at `m = 3`, and `d = 10`.
- ***B.*** The kinetic term, and the unit Jacobian at `0`.
- ***C.*** The two-mode ladder algebra:
  - `⟨V₄⟩ = 8c₄s²`;
  - `V₃` reaches only three-quantum states, and `dE₃ = −8g²s³/ħω`;
  - the normalisations `c₄ = 14κ/(3V)` and `g² = 800κ/(27V)`;
  - the total `4κħ²(63μ² − 200)/(27Va³μ⁴)`, which is `19κħ²/(27Va³) > 0` at `μ = 2√2`;
  - the threshold `200/63`, and the `a⁻⁶` scaling.
- ***D.*** The linear solve families, and the Jacobian rank `2`.
- ***E.*** The asymptotic and Faulhaber coefficients (`2, −9, 15/4`; `2, −7`; the log coefficient `15/4`; the product
  `½`).

***Caveats, registered.***
- ***Imported:***
  - the closed form of `R₃` in the receipt's typed form. Milnor's formula proves it; `S3Frame.lean`'s
    `milnor_scalar` cannot be imported into a probe, so the formula is typed and the link is named;
  - the TT spectrum beyond `m = 3`;
  - the RS formula, labelled.
- The paper-text parse is a pin.

***Failable:*** BUILT, BUILT IN PART (per section), or REPORTED. p `0.45`.

***Census if BUILT:*** row 73 → `DONE`, imports named, `decl` filled in the same push.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

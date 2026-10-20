# `r7443+71.34` — PRE-REGISTRATION: campaign 45, library-gap row 60 (the assembly gives both level sums), with the spectrum imported. ⌗ `1700` lines (band 900–2800), ⛔ stop `3400`. ⌗ p `0.25`

*Under `r7443` ②, step 4, and `r7453` ③: the one row of structure II in `r7453_71_gap_class/CLASS.md`. That file's
finding is that row 60's computed checks take the spectrum as an import, as rows 70 and 73 do. This campaign tests
the finding. The receipt is row 60's (ROWS.tsv, column 6). No Lean was written before this registration.*

## ① The piece: `probes/Row60Levels.lean`

The receipt's computed checks A–E, as `PRICING.md` §1 lists them for row 60.

- ***A.*** An explicit SO(3)-invariant basis built from δ and ε, verified componentwise over `Fin 3`: every
  symmetry, tracelessness, transversality and pair-exchange condition, and the trace relation
  `Σ_a C_{aij,akl} = (λ·deg/5)P_{ijkl}`. Hence the full trace `λ·deg`, independent of the free parameter.
  `A = (deg/5)P` with `tr P = 5`.
  - The dimensions `(1, 1, 2)` at ranks 4, 5, 6 are stated ***within the candidate span***, by a rank
    certificate: a nonzero minor, and kernels exhibited.
  - If that certificate is too heavy, A is reduced to sufficiency and recorded as such.
- ***B.*** The ε² coefficient of the frame-Koszul scalar of `exp(εH)` on `S³`, from row 62's `jet_series` (order 2),
  restricted to the TT constraint variety, equals the admissible contraction combination. The mixed coefficient is
  `0`.
  - Controls: `−2 tr h²` for frame-constant `h`, and the Euler-box `−16π²` from row 59's `section_e_integrals`.
  - The identity is to be proved on the variety, not fitted on samples.
- ***C.*** The seven level values as polynomial identities in `(c_C, c_B, λ, deg)` from the `3⁵`-index sums, and
  the substitution:
  - the second-order level sum is `−¼·deg·μ²`;
  - the fourth-order one is `−(1/120)deg²(5μ² + 4)`;
  - both are `0` at `m = 2` and ***negative for every `m ≥ 3`, proved rather than sampled***;
  - the `c_B²` weight and both remaining weights are nonzero.
- ***D.*** The cross-level double sum factorises, and its diagonal equals C. The Faulhaber sums of degrees 5 and 7
  have negative leading coefficients.
- ***E.*** The sign algebra for `2c₄ − g²/μ²`.

***Caveats, registered.***
- ***Imported, and stated as imports:***
  - the spectrum (`λ = m² − 3`, `deg = 2(m² − 4)`);
  - the value of `c_C`;
  - the parity `c_B = 0`;
  - the seven rational coefficients (r7032, row 62);
  - the Wick-tensor ansatz, that level sums of harmonic products are invariant tensors.
- Completeness of the δ/ε span (the first fundamental theorem of SO(3) invariant theory) is not claimed.
- Paper-text checks are not formalised.

***Failable:*** BUILT (A–E, with A at least to sufficiency), BUILT IN PART (per part), or REPORTED. p `0.25`.
***Risks:***
- the kernel cost of the `3⁵`- and `3⁶`-index sums without `native_decide`;
- matching the TT jet constraints to `Row62Jet`'s parameterisation.

***Census if BUILT:*** row 60 → `DONE`, imports named, `decl` filled. Library gaps would then number only those
rows not yet built.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

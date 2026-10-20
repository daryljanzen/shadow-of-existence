# `r7443+71.26` — PRE-REGISTRATION: campaign 41, library-gap row 70 (the second-order term is the quartic's deviation from the cubic's own completion). ⌗ `800` lines (band 450–1400), ⛔ stop `1900`. ⌗ p `0.40`

*Under `r7443` ②, step 4, next in `PRICING.md`'s order. The receipt is
`P10_the_second_order_term_is_the_quartics_deviation_from_the_cubics_own_completion_and_the_counterterm_collapses_to_lambda_cubed.py`.
No Lean was written before this registration.*

## ① The piece: `probes/Row70Quartic.lean`

The receipt's computed checks A–F as `PRICING.md` lists them.
- ***A.*** On a ladder algebra, `dE₂ = ⟨H₄⟩₀₀ − Σ|⟨s|H₃|0⟩|²/(E_s − E₀)` equals `(6g₄w² − 11g₃²)/(8w⁴)`,
  independent of the truncation. Unitary conjugation gives `dE₂ = 0` with both channels nonzero.
- ***B.*** The non-resonant generator: `i[A, H₀] = H₃`, `H₄fake = i[A, H₃]/2`, and `dE₂(H₃, H₄fake) = 0`. Hence the
  locus `g₄ = 11g₃²/(6w²)` is unique.
- ***C.*** The cubic channel's sign, the pure cubic's `−11g₃²/(8w⁴)`, `tr h³ = 3 det h`, and evenness in `g₃`.
- ***D.***
  - closed de Sitter with `R = 12/α²` and maximal symmetry;
  - the eight dimension-six scalars `(64, 16, 4, 32/3, 4, 8/3, 16/9, 8/9)Λ³`;
  - `Weyl ≡ 0` and both cubic Weyl contractions `0`;
  - the Bianchi I control `diag(−1, T², T⁴, T⁶)` at `T = 1`: `C² = 28/3`, both cubic contractions nonzero, and a
    nonzero `∇R`.
- ***E.*** The homogeneity checks.
- ***F.*** The ranks `1` against `2`, `lim(H_M − log M) = γ` and `lim(H_M − log 2M) = γ − log 2`, and the
  arithmetic.

***Caveats, registered.***
- ***The Rayleigh–Schrödinger formula is the receipt's formal second-order formula on finite matrix elements.*** It
  is ***not*** an eigenvalue statement: the cubic oscillator is unbounded below. The Lean statement says so.
- ***Imported:***
  - the `r6990` bound and the `1/60`, which are cited;
  - the TT spectrum (data in E).

***Failable:*** BUILT, BUILT IN PART (per section), or REPORTED. p `0.40`.
- ***Risk:*** the `4⁶`-index cubic Weyl sums at the control point.

***Census if BUILT:*** row 70 → `DONE`, imports named, `decl` filled.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

# `r7443+71.55` — RESULT, campaign 51, part S: row 65's hard-cutoff slope BUILT. ⌗ The receipt's measured `3.7497` is now a theorem: the slope tends to `15/4`, and the printed values are bracketed to their six decimals. ⌗ p `0.55` came true. ⌗ Part T (the TT spectrum) is still building

*`probes/Row65Slope.lean`: 10 theorems on `[propext, Classical.choice, Quot.sound]`, `20 s`, 508 lines, no error or
warning. The build was delegated and re-run by 71 (`PROBE_RUN_A.txt`).*

- ***An exact split, with no asymptotics needed.*** `summand(−a, −(8+a), k) = a(16−a)/(4k) + err`, with
  `0 ≤ err ≤ 36/k³`, from the identity `r² = k²(2r − a)` for `r = k(k − √(k² − a))`.
- ***The limits.*** For every `0 ≤ a ≤ 3`, the receipt's discrete slope between `M` and `2M` tends to `a(16−a)/4`.
  This uses `H_{2M} − H_M → log 2` (`Real.tendsto_harmonic_sub_log`) and an error sum `≤ 36/M`. The instances:
  - corrected: `15/4`;
  - old: `39/4`;
  - `dis`: identically `0`, because its summand vanishes for every `k`.

  In the shift form `μ² = m² + u`, the limit is the receipt's own `g₁ = −u(u+16)/4`.
- ***The printed values.*** Rational brackets on both difference quotients, `(2000, 4000)` and `(4000, 8000)`, for
  each frequency. They are tight enough to fix the receipt's printed `3.749662` and `9.749121`, and to prove that the
  corrected slope rises toward `15/4` from below. The method telescopes the log and cube bounds and closes with
  `Real.log_two_gt_d9` / `_lt_d9`.
- ***No disagreement with the receipt.***

***Census:*** row 65 stays `DONE (chartable half)`. Its open half is narrowed to the imported TT spectrum alone,
which is part T.

---

# `r7443+71.59` — RESULT, campaign 51, part T: the TT spectrum of the round S³, lower half BUILT at every level with full multiplicity; completeness REPORTED at a named obstruction. ⌗ p `0.35` (eigen-tensors at every level) came true. ⌗ Rows 65 and 66 stay `DONE (chartable half)`, each open half narrowed to completeness alone

*`probes/S3TTSpectrum.lean`: 13 theorems on `[propext, Classical.choice, Quot.sound]`, `87 s`, 1094 lines. The
build was delegated and re-run by 71 (`PROBE_RUN_B.txt`).*

## Built

- ***The model.*** Unit S³ in ℍ, with the left-invariant frame `E_a(q) = q·u_a` acting as derivations on `ℂ[x₀..x₃]`.
  `frame_bracket` proves `[E_a, E_b] = 2ε_abc E_c`, and the rough Laplacian reproduces `s3_tt_eigen` at `m = 3`.
- ***The restriction to S³ is genuine.*** `tangent` proves that the frame fields preserve the ideal of S³, so every
  operator descends to tensor fields on S³, and independence is proved there.
- ***Symmetry.*** Two `sl₂` triples, from the frame Lie derivatives and from the right-invariant fields, commute with
  `∇²` and preserve each TT eigenspace.
- ***Seeds.*** Two level-3 seeds, one frame-constant and one right-invariant, are raised by `wᴺ` to every level
  (`seed_TT`), with eigenvalue `(N+3)² − 3`.
- ***Multiplicity.*** Mathlib's `IsSl2Triple.HasPrimitiveVectorWith` gives non-vanishing, and
  `Module.End.eigenvectors_linearIndependent'` gives independence. ***`tt_level_multiplicity`:*** for every `m ≥ 3`
  there are `2(m² − 4)` tensor fields in `TT(m² − 3)` that are ℂ-linearly independent on S³. `tt_m345` gives 10, 24
  and 42.
- ***Agreement with the corpus:*** `λ = m² − 3` and `deg = 2(m² − 4)`, the two SO(4) multiplets `k = j ± 2`, each of
  size `(m+2)(m−2)`.

## The obstruction, named

"These are ALL the TT eigen-tensors" needs either Peter–Weyl for SU(2), or a Laplace–Beltrami operator on `L²`
tensor fields of a Riemannian manifold with its spectral theory. ***Searched by object*** (case-insensitive file
counts in the pinned Mathlib):

| pattern | files |
|---|---|
| `Peter.?Weyl` | 0 |
| `spherical.?harmonic` | 0 |
| `Laplace.?Beltrami` | 0 |
| `zonal` | 0 |
| `Wigner` | 0 |
| `Casimir` | 0 |
| `specialUnitaryGroup` | 1, the bare submonoid |
| `unitary.?representation` | 1, a docstring |
| `Laplacian` | 13, all flat space |
| `spectral theorem` | 3, finite-dimensional only |
| `haarMeasure` | 47, nothing specific to SU(2) |

Present and used: `IsSl2Triple` (8 files) and Stone–Weierstrass (10). `RepresentationTheory/` has no compact-group
completeness.

***One step not formalised:*** the passage from complex to real dimension (real and imaginary parts of a real
operator's eigenvectors). It is standard.

## Census

Rows 65 and 66 stay `DONE (chartable half)`. Each open half is now exactly ***completeness of the TT spectrum***, a
named Lean obstruction. That is the standing order's other exit. Row 66's deficiency claim is prose, excepted as
text pins are. Row 65's cutoff slope is built (part S).

# `r7437+71.2` — RESULT: campaign 27 BUILT. ⌗ Row 66's kinetic series for non-commuting modes. In the volume-preserving split, order 3 vanishes for ALL square matrices `h, ḣ`. In the linear split, order 3 is `−2 tr(h ḣ²)`. At the receipt's modes the two splits differ: `5/6` at order 4 against `2` at order 3. ⌗ `118` lines against `150` (band 80–320). ⌗ Row 66's open half is now only the deficiency prose and the imported spectrum

*Scored against `PREDICTION.md` in this directory, pushed at `r7437+71.1` before any Lean was written. It is not
revised. `probes/Row66Kinetic.lean` builds with no warning, and its three theorems print `[propext,
Classical.choice, Quot.sound]` (`PROBE_RUN_A.txt`, `6 s`). Built on Daryl's instruction: "Build it".*

## ⛔ The stop, scored

***Not fired.*** `118` lines, under `450`.

## What was built

| theorem | what it proves |
|---|---|
| ***`kinetic_volume_split`*** | for any square `h = A`, `ḣ = B` over ℝ (any size, not only `3 × 3`): with `u = exp(−εh) ⋆ d/dt exp(εh)` truncated, `tr(u ⋆ u)` has order 2 `= tr(ḣ²)` and ***order 3 `= 0`***. Also `tr u` vanishes at order 2, and at order 1 when `ḣ` is traceless: no shear–volume cross term |
| ***`kinetic_linear_split`*** | for any `A, B`: with `u = (1 + εh)⁻¹ ⋆ εḣ`, order 2 `= tr(ḣ²)` and ***order 3 `= −2 tr(h ḣ²)`*** |
| ***`kinetic_splits_differ`*** | at the receipt's `M₁ = diag(1, −1, 0)`, `M₂`: both are traceless and they do not commute. The volume-preserving order 4 is `5/6 ≠ 0`, the first kinetic correction being quartic. The linear order 3 is `2 ≠ 0`, a cubic vertex. So the `sym(π²φ)` structure exists or not according to the split |

- ***The identities are general, not sampled.*** The receipt checks them with two symbolic non-commuting modes.
  These hold for every pair of square matrices, of any size.
- ***The order-3 cancellation is trace cyclicity.*** `tr(B·[B, A]) = 0`, with campaign 25's `commutator_trace` for
  the bare identity. Here it is proved through the series, from the coefficients up.

## Caveats, beside the score

- ***`ġ` is the Leibniz expansion `d(hᵏ) = Σᵢ hⁱ ḣ hᵏ⁻¹⁻ⁱ`, taken as the definition.*** This is the receipt's
  symbolic differentiation. It is not derived from `HasDerivAt` on matrix-valued functions.
- ***The series is the receipt's truncation, not `Matrix.exp`.*** The coefficients are exactly those of `exp`, and no
  convergence is claimed.
- ***The linear split's `√det g` weight is not built.*** For traceless `h` it is `1 + O(ε²)`, so it cannot reach
  order 3. That is argued, as registered.

## The probabilities

| quantity | p | outcome |
|---|---|---|
| built under the stop | `0.60` | ***yes***, `118` |

## Census (moved in this push)

Row 66 stays `DONE (chartable half)`. Its open half is now the deficiency claim (prose) and the imported TT
spectrum, and neither is a computation. ***`decl`*** gained the three names in this push. That makes `89` rows and
`271` pairs, and `check_formalisation_join.py` reads ***green: 271 of 271***. ***Counts, unchanged:*** DONE `74`,
halves `2`, ORDER `1`, LIMIT `12`, ROW `3`, generic-metric `2`, library gap `17`; total `111`. *No new status.*

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

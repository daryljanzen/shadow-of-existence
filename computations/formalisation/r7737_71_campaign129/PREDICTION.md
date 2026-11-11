# `r7737+71.1` — PRE-REGISTRATION: campaign 129, **P5's monodromy and deck group: rows 11a, 11b, 12a and 12b**. ⌗ `700` new lines (band 600–950), p `0.75`, of which about `560` are a verbatim copy. **Expected stop:** none serious. The risk is the copy's own `open` and notation scoping inside `Groupoid.lean`

*Registered before any Lean.*
- **Everything goes into `probes/Groupoid.lean`,** P5's citable file.
- **The copy.** `Row18Monodromy.lean` (Mathlib-only) is copied verbatim into its own section, with its namespace
  `ShadowProbe.Row18Monodromy` and every name kept, so P5's names stay in one file.
  - Its covering map is `proj : Cover → base`, where `M = (r − r³)/2` over `base = {M : 27M² ≠ 1}`.
  - The base point is `M = 0`, with fibre `{0, 1, −1}`.
  - `loopPlus` and `loopMinus` encircle the two Nariai values `M = ±1/(3√3)`, which is `2M = ±2/(3√3)`.
- **New names** are prefixed `gp_`.

## Rows

| Row | Statement | Lines | p |
|---|---|---|---|
| 11a | `Δ(m) = 4 − 27m²` (`m = 2M`) vanishes at the Nariai values `m = ±2/(3√3)`, and `dΔ/dm = −54m ≠ 0` there: a simple zero, so two sheets meet | 15–30 | 0.95 |
| 11b | The monodromy of `loopPlus` is `swap e₀ b` and that of `loopMinus` is `swap e₀ c`, with `b ≠ c`. Each Nariai monodromy is a transposition, and the two transpose different pairs (`rem:monodromy-group`) | 30–60 | 0.85 |
| 12a | The monodromy group is all of `Perm (fibre) ≅ S₃` (copied `monodromy_surjective`, `monodromyGroup_equiv_S3`) | copy | 0.95 |
| 12b | **The deck group is trivial:** a permutation of the fibre that commutes with every monodromy permutation is the identity. **The cover is not normal:** the monodromy group (order 6) is transitive on the 3-point fibre with a non-trivial stabiliser (`swap b c` fixes `e₀`), so it does not act regularly | 50–100 | 0.8 |

**Interpretive, cited:** the identification of the deck group of a connected cover with the centraliser of its
monodromy group. Row 12b proves the centraliser statement.

**Non-vacuity:** the monodromy permutations are non-identity transpositions, and the stabiliser element is non-trivial.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

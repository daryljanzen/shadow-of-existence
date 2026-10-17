# `r7427+71.1` — PRE-REGISTRATION: campaign 26, row 18's computable residue, ported from `P7`'s `order3_bridge` as `r7427` ② suggests. ⌗ `100` lines (band 50–220), ⛔ stop `300`. ⌗ p `0.75`

*`r7427` ② is an observation, not an order: row 18's ORDER-able residue, the discriminant, is already computed in
`P7` (`corpus/slicing_operator.tex` §three-sheeted covers, receipt `receipts/P07_CR_framework/order3_bridge.py`).
Daryl's standing instruction is to build. Read for this campaign: the receipt's STAGE 2 and STAGE 6 and the
appended asserts, and `P7`'s remark.*

## ① The piece: `probes/Row18Cubic.lean`

- ***(a) The discriminant is the squared root-difference product:*** for `x + y + z = 0`, `p = xy + yz + zx` and
  `q = −xyz`, `−4p³ − 27q² = ((x − y)(y − z)(z − x))²`. So it vanishes exactly when two roots collide. This is an
  identity over any commutative ring, which covers ℂ.
- ***(b) The family:*** `r³ + (E² − 1)r + 2M` has discriminant `4((1 − E²)³ − 27M²)`. The receipt asserts exactly
  this. The horizon member `E = 0` branches at `27M² = 1`: the Nariai masses `M = ±1/(3√3)`.
- ***(c) Square in `M` ⟺ `p = 0`:*** over ℂ, `−4p³ − 108M²` is the square of a polynomial `a + bM` for all `M` if
  and only if `p = 0`.
- ***(d) Equilateral ⟺ `p = 0`:*** with `x + y + z = 0`, the roots form an equilateral triangle, meaning
  `x + ωy + ω²z = 0` or `x + ω²y + ωz = 0` with `ω² + ω + 1 = 0`, if and only if `p = 0`. Hence `P7`'s "two are one
  condition, met at `E = 1` alone".
- ***(e) Simple branching:*** for `p ≠ 0`, no triple root, so every collision is of exactly two roots. Each branch
  point's local monodromy is therefore a transposition.

***Not built:*** that the monodromy group of the cover is the full `S₃`. That is a statement about loops in the
punctured mass line, and is the covering-space object row 18 is classed by. Also not built: that a square in
`ℂ(M)` of a quadratic is a square in `ℂ[M]`, which (c) takes in polynomial form. Row 18 stays
`ROW: A DIFFERENT KIND` (ruled `r7421`), with `decl` empty by rule. Its text will name the residue as built.

***Failable:*** BUILT (a–e), BUILT IN PART, or REPORTED. p `0.75`.
- ***Risk:*** (c)'s converse over ℂ (`b² = −108` and `2ab = 0` force `a = 0` and then `p = 0`), and (d)'s two
  directions with `ω` as a hypothesis-carrying element.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

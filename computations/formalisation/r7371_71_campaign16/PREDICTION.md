# `r7371+71.2` — PRE-REGISTRATION: campaign 16, row 35's half: Tangherlini–de Sitter at D = 4, 6, 7 and 8, the receipt's other checks. D = 5 was built at `r7341+71.5`. A stereographic chart for the sphere makes ONE definition serve every D and needs no near-point convention for the sphere. ⌗ `260` lines (band 140–450), ⛔ stop `550`. ⌗ p `0.45`

*Orders: `FOR_71.md` §`r7371` ③ (the remaining halves, cheapest first, a band before each). Row 59 was moved to the
real end in the same push (`r7371+71.1`). ***No pre-opening reading:*** row 35's receipt
(`P03_operator_at_general_D.py`) was opened at `r7341`, and its reading survived.*

## ① The piece

- ***The metric, for any `n = D`:*** `−F(r)dt² + dr²/F(r) + P(r)·Ω(x)·Σᵢ dxᵢ²` on `ℝⁿ`, with `x = (y₂, …, y_{n−1})`.
  - `Ω(x) = 4/(1 + |x|²)²` is the round `S^{n−2}` in stereographic coordinates. It is smooth and nowhere zero on all
    of `ℝ^{n−2}`, so the sphere needs no convention.
  - `P = r²` near the point (the convention, for `P` only).
  - It is one `Fin n` definition, and every entry `i ≥ 2` is the same expression.
- ***On the `r7341` port*** (`diagN`, `curvDN_eq`): THE connection's `G^t_t = R^t_t − R/2`, for any `F`, at each
  `D ∈ {4, 6, 7, 8}`.
- ***The kernel:*** `F = 1 − 2M/r^{D−3} − 2Λr²/((D−1)(D−2))` gives `G^t_t + Λ = 0`, as `tangherlini5_kernel` did at
  `D = 5`.

***Failable:*** BUILT (all four D), BUILT IN PART (some D), or REPORTED. p `0.45` under the stop.
- ***Risk 1:*** the `D = 8` contraction, which is `8²` curvature entries in symbolic `|x|²`.
- ***Risk 2:*** `Ω`'s first and second derivatives over `n − 2` coordinates, as a generic derivative lemma.
- ***What it will not build:*** a theorem quantified over ALL `D`. That needs sums over `Fin n` for symbolic `n`,
  outside what `simp` expands. The receipt checks `4–8`, and that is the object.

***Census if BUILT:*** row 35 moves `DONE (chartable half)` → `DONE`. Then DONE `53` and halves `3` (7, 77, 108).

## ② Compile

- `tangherlini5_Gtt` took `≈ 7 s` at `D = 5` with nested sines, with no table: the contraction runs inside one goal.
- `Ω` makes every sphere entry a rational function of `|x|²`. Priced `1–10` minutes for all four D.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

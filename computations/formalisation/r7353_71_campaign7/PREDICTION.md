# `r7353+71.1` — PRE-REGISTRATION: campaign 7, two pieces for the night. ⌗ (A) Row 58 as exact algebra: the ADM kinetic scalar for `γ = a²·E(ε)` with `E` the receipt's own truncated exponential, worked in a polynomial ring over `3 × 3` matrices. Its `ε⁰`, `ε¹` and `ε²` coefficients are `−6h²`, `0` and `¼tr(Ḣ²)`: `80` lines, compile under `30 s`. ⌗ (B) Row 83's open half: `R = 24 − 4t²` at EVERY point of the chart, not only `y = 0`: `250` lines, ⛔ stop `500`, compile priced at `≈ 35` minutes and flagged before building. ⌗ No new readings: both receipts were opened before this registration

*Orders: `FOR_71.md` §`r7353` ① (register before building, census in the same push, price compile time on the
table-size axis, name the block) and ③ (long compiles need no permission: push what lands, name what is still
compiling). Written before either piece is built.*

## ① The pieces

| piece | row | what it needs | lines | compile |
|---|---|---|---|---|
| ***A*** | 58 | see A below | ***`80`*** (band 40–170) | no table: under `30 s` |
| ***B*** | 83, its open half | see B below | ***`250`*** (band 120–400, ⛔ stop `500`) | see ③ |

***A, row 58.*** `γ = a²E(ε)` with `E = Σ_{k≤3} εᵏHᵏ/k!`, the receipt's `NORD = 3` truncation, and `Ė` its exact
time derivative. `H` and `Ḣ` are any traceless `3 × 3` matrices.
- The kinetic scalar is `¼[tr(M²) − (tr M)²]`, where `M = E(−ε)·(2hE + Ė)` is the receipt's `γ⁻¹γ̇` with its own
  truncated inverse.
- It is a polynomial in `ε` with matrix coefficients, worked in `(Matrix (Fin 3) (Fin 3) ℝ)[X]`. Its coefficients
  `0`, `1` and `2` are `−6h²`, `0` and `¼tr(Ḣ²)`.
- ***What it will not build:*** the receipt's `det exp(εH) = 1` gate for the measure. `mathlib` has no `det_exp`.
  If that part is not reached, it is named as the open half.

***B, row 83's open half.*** The same engine (`curvG_eq`) and chart as `r7351+71.6`, at a GENERAL `y`.
- The tables are rational in `μ₀, μ₁, μ₂` (with `Σμ = 1`) and `t`. The derivatives of `μ` at `y` are polynomial in
  `μ`, and the inverse is `4(diag μ⁻¹ + J/μ₂)` on the base and `δ/μ − (t² − 1)/t²` on the fibre.
- The point is to replace "at `y = 0`" by "at every `y ∈ ℝ⁵`", which closes the half without proving
  `SU(3)`-homogeneity.

***Failable:***
- Each piece ends BUILT, BUILT IN PART (the unbuilt part named) or REPORTED (the obstruction named).
- p `0.8` that A lands in its band.
- p `0.45` that B lands under its stop. The risk is `field_simp`/`ring` on rational entries in four symbols across
  `950` cases, not the engine.

## ② The decisive fraction and the survival rate

***Decisive:*** B. If it lands, row 83 moves from a half to DONE. If it does not, the half stands, and the obstruction
(the expression size of symbolic tables) is named with a measured per-case cost.

***Readings: none this block.*** Row 58's receipt was opened at `r7351` stage C (and its reading scored there:
survived). Row 83's was opened at `r7341`. ***The running rate stays `14` of `21`.***

## ③ Compile time on the table-size axis

| piece | cases | multiplier `m` | predicted |
|---|---|---|---|
| A | none | — | under `30 s` |
| B | `950` (the same as `r7351+71.6`) | ***`3`***: rational entries in four symbols, against `0.34` measured for numeric entries | `0.73 × 950 × 3 ≈ 35` min |

- The multiplier is a prediction, and the axis is the case count, as settled at `r7351`.
- *If B's tables do not compile per case in under `10 s`, it is split to the Ricci contraction only, the `scalG` the
  row needs, and the full Γ table is dropped. That is decided on the first measured case, before the whole table
  runs.*

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. Pieces are pushed as they land.*

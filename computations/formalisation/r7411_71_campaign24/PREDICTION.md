# `r7411+71.12` — PRE-REGISTRATION: campaign 24, row 59's Euler-chart field identities, its frame-constant floor, and its first two counts. ⌗ ⚠ part of this was drafted BEFORE this registration and is scored as not blind. ⌗ The blind part: `+110` lines (band 50–260), ⛔ stop at `500` for the file. ⌗ p `0.55`

*Daryl's instruction: build. Row 59 is `ORDER: ENGINE-REACHABLE`; its text names what is still to build: the
Euler-chart field identities, the jet ranks `5`/`12`/`8`, and the integrals of non-constant `H4`. The receipt was
read in full at `+71.2`, and its parts B–D again for this campaign.*

## ⚠ The slip, stated first

While the campaign-23 file was rebuilding, I drafted and compiled `probes/Row59Euler.lean` with parts (B) and
(D-5) below **before writing this registration**. That breaks the order the `r7411` rules set: register, then
build. Nothing in that draft is scored blind. It stands at `158` lines, 5 declarations printing the standard
axioms, and it is committed as it is, in this push, so its state at registration is on the record.

## ① The pieces, in `probes/Row59Euler.lean`

- ***(B), drafted, not blind:*** `Rad · e = ẽ`, `det e = sin θ/8`, `Rad Radᵀ = 1` (`rad_coframes`);
  `tr((eᵀe)⁻¹eᵀHe)ᵏ = tr Hᵏ` for any invertible `e` (`chart_trace_pow`); for the receipt's `H4`: `p₁ = 0`,
  `p₂ = 2 − 2 sin²φ sin²θ`, `p₃ = 0`, `p₄ = p₂²/2`, and the superposition `H4 + H4b` traceless, at every point and
  in the chart (`h4_invariants`, `h4_chart`).
- ***(D-5), drafted, not blind:*** the receipt's five matrices are independent, traceless, symmetric and span
  (`tt_dim_five`).
- ***(C), blind:*** the frame-constant floor. For `H = diag(1, −1, 0)` and `diag(1, 1, −2)`, Milnor's
  `R = 2(4e₂ − e₁²)/e₃` at `λ = exp(εh)` is an exponential sum, and its Taylor coefficients at orders `0..4`
  (via `iteratedDeriv`), times `2π²`, are the receipt's `[12, 0, −8, 0, −14/3]` and `[12, 0, −24, 40, −42]`. They
  agree with `6 − 2p₂ε² − (10/3)p₃ε³ − (7/6)p₄ε⁴`, and `−(7/6)p₄ = −(7/12)p₂²` on both. Milnor's formula is
  `milnor_scalar` (campaign 21). Probes do not import each other, so here it enters as the definition of `R`, and
  the result says so.
- ***(D-12), blind:*** the admissible one-jet (symmetric and traceless in the last two indices, divergence-free) has
  dimension `12`, as `finrank` of a kernel by rank–nullity, with the constraint map shown surjective.

***Not built:*** the rank `8` (the receipt takes it on twenty RANDOM jets, so a Lean check of the exported matrix
would re-check numbers, not derive them), and the integrals of the non-constant `H4` series.

***Failable, on the blind part only:*** (C) and (D-12) BUILT, ONE BUILT, or NEITHER. p `0.55` for both.
- ***Risks:*** `iteratedDeriv` of exponential sums up to order 4; and the kernel's `finrank` through rank–nullity.

***Census if built:*** row 59 stays `ORDER: ENGINE-REACHABLE` whatever happens. The rank `8` and the
non-constant integrals remain, and the row's text names what was built.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

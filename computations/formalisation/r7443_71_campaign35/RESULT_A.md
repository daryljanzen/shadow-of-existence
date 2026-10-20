# `r7443+71.16` — RESULT: campaign 35 BUILT. ⌗ Row 64, every computed check of sections A–D: the descent's ranks, the rotating kernel and its divergence, the closed-FRW order structure, and `L = 15/4` and the harmonic log coefficient as genuine limits. ⌗ `622` lines against `330` (band 180–700). ⌗ Row 64 → `DONE`

*Scored against `PREDICTION.md` in this directory, pushed at `r7443+71.15` before any Lean was written. It is not
revised. `probes/Row64Descent.lean` builds with no error and no warning, and its 17 headline theorems print
`[propext, Classical.choice, Quot.sound]` (`PROBE_RUN_A.txt`, `15 s`). No `native_decide` is used. The build was
done by a delegated agent and re-run by 71 before this record.*

## ⛔ The stop, scored

***Not fired.*** `622` lines, under `1000`. That is inside the band but nearly twice the point estimate. The limits
and harmonic-sum statements cost more than priced.

## What was built

| section | theorems | what they prove |
|---|---|---|
| A | `rank_A`, `kernel_A`, `phase_A` | rank `2` on the four-point spectrum and `1` on the one-point spectrum, as genuine `Matrix.rank`. The kernel is EXACTLY the line through `(−L/(48Λ²ενq₆), 4L/(3Λενq₄), 1)`, and on the four-point spectrum it equals the coefficient matrix's kernel. The phase drops out of `diag(1,4)` and stays in `σₓ` |
| B | `substrate`, `R_deformed`, `inv_poly`, `orders`, `log_structure`, `ranks_by_order` | `ȧ` and `ä` of `α cosh(T/α)` are derived, giving `R = 4Λ`, `Ric² = 4Λ²`, `Riem² = 8Λ²/3`, `λ₀ = λ₁ = Λ`. `R = 4Λ + εν/a⁴` exactly. The four invariants are exact cubics in `ε`, with order 0 at `(64, 16, 32/3, 4)Λ³` and order 1 exactly `(3/4)(ν/a⁴)·c₀/Λ`. The `ε²` terms carry `log a`. The ranks by order are `1, 1, 2`, and the `a⁻⁶` control is rank `2` at order 1 |
| C | `L_coeff`, `rate_factor`, `log_coeff`, `control_weight`, `conventions_three`, `kernel_rotates` | ***`m·(2(m²−4)√(m²−1) − 2m³ + 9m) → 15/4`*** as a `Tendsto`. The partial sums have an exact closed form in Mathlib's `harmonic`, and their log coefficient is `gL` as a limit. Dropping any convention sends the limit to `+∞`. The kernel's third entry is zero at `ε = 0`, and the ratio diverges to `−∞` as `ε → 0⁺` |
| D | `one_number`, `A6_factor` | the single number; and the rank, the kernel line and its nonzero entry all survive `f₁ ↦ A₆f₁` |

## Findings beyond the receipt (none contradicts it)

- ***The order-2 rank `2` is structural, not a property of the sample points.*** Every order-2 coefficient lies in
  `span{ΛS², ΛQ}`, with `S = ν/(6a⁴)`, `A = (ν − 2 − 2ν log a)/(6a⁴)` and `Q = A² − SA + S²`. So `R·Riem²` and
  `tr Ric³` are proportional at second order.
- `R³`'s `ε²` term carries no log at all. That is consistent with the receipt, which checks the log only for the
  other three.
- The kernel ratio's divergence has a fixed sign: `−∞`.

## Caveats, beside the score

- ***Imported, labelled in the file:***
  - the TT weights;
  - the forms of `f₁`, `f₂` and `f₃`;
  - the closed-FRW invariant formulas in the receipt's typed form, and `ä/a = aF′/2 + F`.

  The derivatives they are fed (`ȧ`, `ä`, `F′`) are derived. The formulas are not tied to the engine's connection;
  that would mean copying much of `FRWk`.
- The paper-text check is a pin. Its value, `4Λ`, is proved.

## The probabilities

| quantity | p | outcome |
|---|---|---|
| built under the stop | `0.50` | ***yes***, `622` |

## Census (moved in this push)

***Row 64 → `DONE`***, `decl` filled with the 17 names, `319` pairs `ok` on the tree audit. Library gap `10 → 9`.

The join gate's `⓶ᵇ` reads UNANSWERABLE locally until the `formalisation-mathlib` record for this push's Lean tree
exists. CI writes that record on the push, and the gate is right not to read the absence as a pass.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

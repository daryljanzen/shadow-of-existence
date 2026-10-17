# `r7443+71.23` — RESULT: campaign 39 BUILT. ⌗ Row 57, every computed check: the realisable cubics' rank 3 equal to its gradient condition, the sample-point ranks 1, 1, 2, the harmonic sum's exact quartic closed form, and the `ζ` probe replaced by genuine limits (`riemannZeta_residue_one`, with the linear error decay to `cγ`). ⌗ `773` lines against `700` (band 400–1300). ⌗ Row 57 → `DONE`

*Scored against `PREDICTION.md` in this directory, pushed at `r7443+71.22` before any Lean was written. It is not
revised. `probes/Row57Second.lean` builds with no error and no warning, and all 26 `#print axioms` lines read
`[propext, Classical.choice, Quot.sound]` (`PROBE_RUN_A.txt`, `17 s`). No `native_decide` is used. The build was done
by a delegated agent and re-run by 71 before this record.*

## ⛔ The stop, scored

***Not fired.*** `773` lines, under `1800`.

## What was built

| section | theorems | what they prove |
|---|---|---|
| A | `turnover_unique`, `eps_size`, `inv_exp`, `source_moves` | the unique stationary point of `α cosh(T/α)`, at `T = 0`, with second derivative `1/α`. `10⁻¹²³ < ε_max < 10⁻¹²²` and `10⁻²⁴⁶ < ε_max² < 10⁻²⁴⁴`, exactly. The source `σε²/a⁸` leaves orders 0 and 1 and moves order 2 (`−576Λ²σ/a⁸` for `R³`) |
| B1 | `gradient_six`, `gradient_eight`, `realizable_cubics` | the gradient condition at `K₁ = K₂`. ***`∂₁P − ∂₂P = K²(3c₀ + c₁ − c₂ − 3c₃)`***, satisfied by all five invariants, whose rows span every cubic that satisfies it: rank 3, raised to 4 by `K₂³` |
| B2 | `dK_split`, `sector_orders`, `P_closed`, `ranks_by_order`, `second_direction`, `no_fourth_convention` | `δK₁ + δK₂` has no log and `δK₁ − δK₂` has one. Order 1 is a multiple of `S` alone, and order 2 lies in `span{S², Q}`. The ranks are `1, 1, 2` at the six sample points. The second direction factors through `(1,0,0)` and `(3,6,4)` |
| asymptotics, harmonic | `L_coeff`, `harmonic_closed`, `log_coeff` | `m(dμ − 2m³ + 9m) → 15/4`. The partial sum `M⁴/2 + M³ − 4M² − 9M/2 + 9 + L′(H_M − 3/2)` is exact, with no `M⁵`. The log coefficient is a genuine limit |
| C | `zeta_face`, `trace_face`, `curvature_face`, `control_weight`, `faces_together` | ***`c·h·ζ(1+h) → c`*** by `riemannZeta_residue_one`, and `(c·h·ζ(1+h) − c)/h → cγ`, the receipt's "linear error decay" as a limit. `ρ − 3p = L′/a⁴`. `R = 4Λ + εν/a⁴`. The control weight has no `1/m` term and no harmonic number. The three faces move together |
| D | `two_halves`, `vertex_scaled` | the order-1 rank is below the order-2 rank. A scaled vertex scales every coefficient and keeps both ranks |

- ***The `ε`-series coefficients are unique*** (`Exp3.unique`). So "the order-`k` coefficient" is a fixed quantity,
  not a formal substitution.

## Caveats, beside the score

- ***Imported, labelled in the file:***
  - the TT and control weights;
  - the FRW invariant formulas in `K₁` and `K₂`, and `K₁ = aF′/2 + F`, `K₂ = F + 1/a²` (`F′` is derived);
  - the receipt's model `F` and its typed pressure;
  - the measured `Λ` and `ℓ_P²`.
- ***Not built:*** the Dirichlet series' meromorphic continuation, as registered; the receipt does not do it either.
- In `second_direction`, uniqueness of the coefficients as a polynomial in `log a` is not separately proved. The
  identity holds for all `a > 0`.

## The probabilities

| quantity | p | outcome |
|---|---|---|
| built under the stop | `0.40` | ***yes***, `773` |

## Census (moved in this push)

***Row 57 → `DONE`***, `decl` filled. The theorem list is carried in the selector's `MANUAL` table, because several
names have no underscore. Library gap `6 → 5`, DONE `88`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

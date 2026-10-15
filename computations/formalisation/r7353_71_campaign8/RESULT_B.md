# `r7353+71.8` — RESULT, piece B: the contracted Bianchi identity, `∇^a G_ab = 0`, is PROVED for THE connection of ANY smooth, symmetric, nondegenerate metric on `ℝⁿ`. ⌗ `313` lines against `300` (band 150–500), and campaign 8 is `419` against `500`, ⛔ stop `900` not reached. ⌗ p `0.35` that B lands: yes. Row 6 is DONE. DONE `45`, halves `12`, generic-metric `2`

*Scored against `PREDICTION.md` in this directory (pushed at `r7353+71.4`). It is not revised. Every new axiom line is
`[propext, Classical.choice, Quot.sound]`, with no `sorryAx` (`PROBE_RUN_B.txt`, `54 s` for the whole file).*

| piece | registered | measured | outcome |
|---|---|---|---|
| A (`r7353+71.5`) | `200` (band 100–350) | `106` | ***BUILT***, in the band |
| B | `300` (band 150–500), p `0.35` | ***`313`*** | ***BUILT***, in the band. p: ***yes*** |
| ***campaign 8*** | ***`500`***, ⛔ `900` | ***`419`*** | |

## What is proved (`probes/Bianchi2.lean`)

Everything is for `lcConn (ndOf B …)`, THE Levi-Civita connection of the engine, of any `C^∞` field `B` of symmetric
nondegenerate forms.

| lemma | statement | scope |
|---|---|---|
| `compat_lc` | metric compatibility, `∂_e B(a,b) = B(Γ(e,a), b) + B(a, Γ(e,b))`, from the Koszul form | any finite-dimensional `E` |
| `compat_deriv` | the same, differentiated once | any finite-dimensional `E` |
| `curv_metric_antisymm` | `B(R(u,e)a, b) + B(a, R(u,e)b) = 0` | any finite-dimensional `E` |
| `bianchi1_alg` | the first Bianchi identity | algebra |
| `pair_symm_alg` | the pair symmetry | algebra; the combination solved exactly, not guessed |
| `bianchi1_nabla_alg` | the first Bianchi identity for `∇R` | algebra |
| `nablaRB_antisymm` | antisymmetry of `∇R` in its first pair | algebra |
| `nabla_metric_antisymm` | antisymmetry of `B(∇R…)` in its last pair, by differentiating `curv_metric_antisymm` | any finite-dimensional `E` |
| `contracted_bianchi` | `Σ_{ac} g^{ac} (∇_a Ric)(c, w) = ½ Σ_{ac} g^{ac} (∇_w Ric)(a, c)` for every `w`, that is `∇^a R_ab = ½∇_b R` and so `∇^a G_ab = 0` | `ℝⁿ`, with `g⁻¹` given at the point as numbers (the `r7351+71.6` convention: no derivative of the inverse is ever taken) |
| `nRic_eq` | `nRic`, the trace of `∇R`, IS `(∇_e Ric)(b,c) = ∂_e Ric(b,c) − Ric(Γ(e,b), c) − Ric(b, Γ(e,c))`, so the statement is about the covariant derivative of the Ricci form, not a stand-in | `ℝⁿ` |

***Why the registered failure shape did not happen:*** I expected `∂(g⁻¹)` to be needed. It is not. Write the right
side as `½ g^{ac}(∇_w Ric)(a, c)`: every derivative then falls on `B`, `Γ` or `R`, never on the inverse.

## Caveats beside the score

1. ***The right side:*** it is `½ g^{ac}(∇_b R)_{ac}`, not `½∂_b R`.
   - The two are equal because `∇g⁻¹ = 0`. That step is standard, and it is not built here.
   - The contracted identity as proved is the index form `∇^a R_ab = ½ g^{ac}∇_b R_ac`.
2. ***The receipt's instance:***
   - Its two-wave metric, to `O(ε²)`, is not evaluated separately. The theorem covers it wherever that metric is
     smooth and nondegenerate on all of `ℝ⁴`.
   - For the receipt's finite `ε` that is a condition on `ε`, and it is not checked here.
   - The receipt's own point, that the identity is off-shell and holds for any metric, is exactly what is proved.
3. ***`∇R` is the coordinate formula on constant fields*** (as in piece A). `mathlib` has no covariant derivative of a
   `(1,3)` field.
4. ***Instance search:*** `mathlib`'s instance search does not reach the iterated derivative of `B` itself
   (`E →L E →L E →L E →L ℝ`). So compatibility is differentiated through the scalar entries `y ↦ B y a b`. This is a
   library limit met and routed around, not a gap in the result.
5. ***`r7353+71.5`'s census slip:*** reported and corrected at `+71.6`. This push carries its census row, checked by
   its counts before the commit.

## Census (moved in this push)

| status | after `r7353+71.6` | now |
|---|---|---|
| DONE | `44` | ***`45`*** (+ 6) |
| DONE (chartable half) | `13` | ***`12`*** (− 6) |
| GENERIC-METRIC IDENTITY | `2` | `2` (20, 62: an argument and a jet-space rank, both reported) |
| real end | `20` | `20` |

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

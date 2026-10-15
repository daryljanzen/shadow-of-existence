# `r7371+71.9` — RESULT: campaign 19 BUILT. ⌗ Row 77 is DONE, and no chartable halves remain. Under THE connection, the Killing form of any differentiable field on a diagonal `ℝ⁴` metric is in closed form. `∂_z`, `∂_t` fail where `ψ_z`, `ψ_t ≠ 0`, and the `x ↔ y` rotation fails where `g_xx ≠ g_yy`. ⌗ `124` lines against `130` (band 70–260, ⛔ stop `320`): in the band. ⌗ `9 s` against under `1` minute

*Scored against `PREDICTION.md` in this directory (pushed at `r7371+71.8`, before the build). It is not revised.
Every axiom line is `[propext, Classical.choice, Quot.sound]`, with no `sorryAx` (`PROBE_RUN_A.txt`; one deprecation
warning, no error). New file: `probes/Row77Killing.lean`. No pre-opening reading was registered, so the running rate
stays `15` of `22`.*

## ⛔ The stop, scored first

***Not fired.*** `124` lines, under `320`.

## What was built

| piece | theorem | what it proves |
|---|---|---|
| (a) | `killF_model` | for ANY differentiable field `ξ` and any diagonal metric `Σcᵢdxᵢ²` on `ℝ⁴`: `g(∇_uξ, v) + g(u, ∇_vξ) = g(Dξ·u + Γ(u, ξ), v) + g(u, Dξ·v + Γ(v, ξ))`, `Γ = gamD` |
| (b) | `killF_coord` | for the constant field `∂_k`, the Killing form on `(∂ᵢ, ∂ᵢ)` is `∂_k cᵢ` |
| | `coord_not_killing` | `∂_k` is not Killing at `p` wherever some `∂_k cᵢ(p) ≠ 0` |
| | `gowdy_coord_not_killing` | with `g_xx = e^{2ψ}`, `∂_k` is not Killing at `p` wherever `∂_kψ(p) ≠ 0`, for `k = z` and `k = t` alike |
| (c) | `rot_killF` | for `ξ = −y∂_x + x∂_y`, with the coefficients' `x, y` derivatives zero at `p`: the Killing form on `(∂_x, ∂_y)` is `c_y − c_x` |
| | `gowdy_rot_not_killing` | for coefficients depending on `(t, z)` only, the Gowdy family, the rotation is not Killing at `p` wherever `g_xx(p) ≠ g_yy(p)` |

- With `gowdy_killing` (engine, `r7297` C5: `∂_x`, `∂_y` ARE Killing), every check the receipt runs is built.
- ***The price drop held.*** No new engine lemma: `cov_model` with `lcConn_const` gives `∇_wξ = Dξ·w + Γ(w, ξ)` for
  the non-constant rotation field. The registered risk, the coercions, cost one explicit `σ` and one rewrite.

## Caveats, beside the score

- ***Not claimed, as registered:*** that NO third Killing field of any form exists. The receipt tests three named
  candidates, and so does this. The general uniqueness would be a statement about the whole solution space of the
  Killing equation for a generic profile. Neither the receipt nor this file states it.
- The failures are pointwise: each candidate fails at every point where its stated quantity is nonzero. "Generic
  `ψ`" in the receipt is read as "some point with `ψ_z ≠ 0`", and so on.

## The probabilities

| quantity | p | outcome |
|---|---|---|
| campaign 19 BUILT under its stop | `0.65` | ***yes***, `124` |

## Census (moved in this push)

Row 77: `DONE (chartable half)` → ***`DONE`***, its text naming the six new declarations and what is not claimed.
***Counts, checked:*** DONE ***`56`***, halves ***`0`***, generic-metric `2`, no-connection `32`, library gap `17`,
real obstruction `4`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

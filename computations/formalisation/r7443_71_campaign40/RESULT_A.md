# `r7443+71.24` — RESULT: campaign 40 BUILT. ⌗ Row 69, and the Levi-Civita/Pontryagin core rows 96 and 89 will reuse: the density on THE Levi-Civita connection, the plane-wave Gowdy instance with ARBITRARY smooth profiles (`R = 1` gives `0`; `R = t` gives `−8e^{2ψ}ψ′ω′/t³`), a general-`R` formula the receipt does not have, and the cycle average `(k²ε²/2) cos δ`. ⌗ `940` lines against `600` (band 300–1200). ⌗ Row 69 → `DONE`

*Scored against `PREDICTION.md` in this directory, pushed at `r7443+71.22` before any Lean was written. It is not
revised. `probes/Row69Pontryagin.lean` builds with no error and no warning. 20 theorems print `[propext,
Classical.choice, Quot.sound]` and `eps4_antisymm` depends on no axioms (`PROBE_RUN_A.txt`, `400 s`). No
`native_decide` is used. The build was done by a delegated agent and re-run by 71 before this record.*

## ⛔ The stop, scored

***Not fired.*** `940` lines, under `1600`.

## What was built

| part | theorems | what they prove |
|---|---|---|
| core | `eps4`, `eps4_sign`, `eps4_det`, `eps4_zero_of_not_injective`, `eps4_antisymm`, `sum_eps`, `pontArr`, `pontryaginLC`, `pontryaginLC_eq` | the `Fin 4` Levi-Civita symbol equals `Equiv.Perm.sign`, and the permutation-matrix determinant the receipt builds `EPS` from. ***`*RR = ½ ε^{mnrs} R_mnab R_rs^ab / √−g`*** is defined on the engine's `curv` of THE Levi-Civita connection, and equals the receipt's Christoffel recipe (`pontryaginLC_eq`) |
| instance | `gowdy_pontryagin`, `gowdy_plane_wave_pontryagin`, `gowdy_areal_pontryagin`, `gowdy_areal_weight`, `gowdy_areal_silenced`, `gowdy_areal_psi_constant`, `gowdy_areal_omega_constant`, `areal_profile_exists` | the receipt's `gowdy(0, ψ(t−z), ω(t−z), R(t))` with ψ and ω ARBITRARY smooth profiles. For any smooth nowhere-zero `R`: `*RR = 4e^{2ψ}(4ψ′ω′RR″ − 2ψ′ω′R′² + ω″RR″)/(R²\|R\|)`. At `R = 1` this is `0`. At `R = t` (`t > 0`) it is `−8e^{2ψ}ψ′ω′/t³`; the weight `*RR/(ψ′ω′) = −8e^{2ψ}/(t²\|t\|)` is strictly negative and carries no derivative and no ω. It vanishes when either channel is constant |
| cycle | `cycle_average`, `cycle_average_quarter`, `cycle_average_in_step`, `cycle_average_anti_phase`, `cycle_average_bound`, `reflection_is_half_turn` | `⟨ψ′ω′⟩ = (k²ε²/2) cos δ`, taking `0, ±k²ε²/2` at `π/2, 0, π`. `ω ↦ −ω` is `δ ↦ δ + π`, which flips the sign |

***Beyond the receipt.*** The general-`R` formula shows an extra `ω″RR″` term when `R″ ≠ 0`. It vanishes at both of
the receipt's radii, so it changes none of its claims. It is recorded as a finding.

## Caveats, beside the score

- ***Tensorial covariance of the density is not proved***, as registered.
- The engine needs a metric nondegenerate everywhere, so `R = t` is stated as "`R` equal to `t` near a point with
  `t > 0`". Its existence is proved (`areal_profile_exists`), so the statements are not vacuous.
- ***Build notes, now standing practice for generated tables:***
  - exponents typed `^(n:ℕ)`;
  - `linter.constructorNameAsVariable` off on long literals.

## The probabilities

| quantity | p | outcome |
|---|---|---|
| built under the stop | `0.40` | ***yes***, `940` |

## Census (moved in this push)

***Row 69 → `DONE`***, `decl` filled through the selector's `MANUAL` table. Library gap `5 → 4` (70, 96, 89, 60).
DONE `89`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

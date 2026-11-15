# `r7803+71.2` — RESULT: **K4 BUILT: a vacuum-Λ point of the polarized Gowdy–de Sitter form at which the Weyl tensor is Petrov type I (`I = 7`, `J = 3`). P11 now stands at 9 of 12.** ⌗ `~275` new lines (band 350–600, estimate 450, **under by ~75**) plus 52 verbatim lines, at p `0.55`

*The registration is `PREDICTION.md`. The probe is `probes/Dynamics.lean`, appended. It is now 1052 lines: 337 lines
added, no line changed.*

## Verification
- `lake env lean probes/Dynamics.lean` gives **0 errors and 0 warnings**.
- **22 axiom lines** (16 earlier, 6 new), every one `[propext, Classical.choice, Quot.sound]`.
- The forbidden-token grep is clean, imports are `Mathlib` only, and `check_no_sorry.py` reports ALL 29.
- **All eight copied blocks are byte-identical to `Range.lean`.** These are the six from campaign 142 and the two
  added here: `ij_tbl`, and `ij_blk` through `ij_tr3`. The two new ones sit in a reopened
  `ShadowProbe.RangeProbe`.

## Rows

| Row | Statement (Lean) | Mark |
|---|---|---|
| K4a | `dy_gk_form`: where `C > 0`, `dy_gk = diag(−1, 1, B, C)` (`B = 1 + 2t + 5t² + z²`, `C = 1 + 2z − t² − 3z²`) **is** `eq:metric`'s `dy_g` with `γ = ψ = ½ log B`, `R = √(BC)`. `dy_Γk`: its Christoffel table, wherever `C ≠ 0`. `dy_Riem0`: its full Riemann tensor at the origin, `R^a{}_{bcd} = V_ab(δ_ac δ_bd − δ_ad δ_bc)` with eight nonzero `V_ab`. `dy_vacuum0`: `R_ab = 3g_ab` and `R = 12` there | **BUILT** |
| K4b | `dy_W0`: at the origin the Weyl bivector operator is `ij_tbl U`, `U` the explicit pair table. `dy_typeI`: `R_ab = 3g_ab`, `∂_z C = 2` (it depends on `z`), `I = 7`, `J = 3`, `I³ ≠ 27J²`: **Petrov type I** | **BUILT** |

**Against the registration:**
- **The named stop did not hold.** The 256-component Riemann table closed through the derivative facts of the eight
  Christoffel functions at the origin (`dy_k1_pd` … `dy_k8_pd`).
- **Size:** about 275 new lines against an estimate of 450 (band 350–600), so under the band.
- **What it is, stated plainly:** a type-I point of a metric of `eq:metric`'s form whose 2-jet satisfies the
  Einstein–Λ equations there. It is not a type-I theorem for a solution of the full system, and the paper itself
  has no closed-form one with `Λ > 0`. The jet was found by solving the field equations at the origin; they impose
  one consistency condition, `p₁p₂ = q₁q₂`, on the first-order coefficients. The electric eigenvalues are
  `(1, −3, 2)`, distinct.
- **Not formalised:**
  - that a solution of the full Gowdy–de Sitter system realises this jet (the paper's Cauchy-problem claim);
  - the word "generic".

**P11 tally: 9 of 12 cored rows BUILT** (A1–A3, K1, K2, K4, W1–W3). A4, K3 and W4 are beyond.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

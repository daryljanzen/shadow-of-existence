# `r7757+71.2` — RESULT: campaign 137, **P7's algebraic and complex rows BUILT: 11 of 11 (3a, 3b, 3c, 7a, 7b, 8a–8e, 9).** ⌗ `290` lines (band 300–600, **under by 10**), at p(all) `0.75`

*The registration is `PREDICTION.md`. The probe is the new `probes/Framework.lean` (`fw_`), P7's citable file. It
imports Mathlib only and copies nothing.*

## Verification
- `lake env lean probes/Framework.lean` gives **0 errors and 0 warnings**.
- **16 axiom lines**, every one `[propext, Classical.choice, Quot.sound]`.
- The forbidden-token grep is clean, imports are `Mathlib` only, and `check_no_sorry.py` reports ALL 29.
- No options are set, and no section is copied.

## Rows

`f(r) = 1 − 2M/r − r²/α²`.

| Row | Statement (Lean) | Mark |
|---|---|---|
| 3a | `fw_ef_inv`: in ingoing Eddington–Finkelstein form the inverse metric is explicit and regular wherever `r, sin θ ≠ 0` (horizon included), with `g^{rr} = f`. `fw_dS_null`: for de Sitter, `g^{-1}(dr, dr) = 0` on `r = α`, so the horizon is a null hypersurface | **BUILT** |
| 3b | `fw_horizons`: `f(α) = 0` (de Sitter, area `4πα²`). For Nariai, `f(α/√3) = f′(α/√3) = 0` (the two positive roots coincide), and `4π(α/√3)² = 4πα²/3` | **BUILT** |
| 3c | `fw_surface_gravity`: `κ = |f′|/2` is `1/α ≠ 0` for de Sitter and `0` for Nariai | **BUILT** |
| 7a | `fw_nariai_roots`: for `r ≠ 0`, the Nariai `f(r) = 0 ⇔ r = α/√3 ∨ r = −2α/√3` | **BUILT** |
| 7b | `fw_turnaround`: with `r₀³ = 2Mα²`, at `r = −r₀` the complex time `τ̃ = −iπα/3` satisfies the bead `r³ = 2Mα² sinh²(3τ̃/2α)`, and `1 − f(−r₀) = 0` | **BUILT** |
| 8a | `fw_one_sub_f`: `1 − f = 2M/r + r²/α²`, and `f = 1 ⇔ r³ = −2Mα²` | **BUILT** |
| 8b | `fw_comoving_roots`: the roots of `z³ + 2M` are exactly `−c, −cω, −cω²` (`c³ = 2M`, `ω = −½ + i√3/2`, `ω³ = 1`), and `z ↦ ωz` permutes them. `fw_equilateral`: all three squared distances are `3c²` | **BUILT** |
| 8c | `fw_three_real`: for `0 < M < 1/(3√3)`, `r³ − r + 2M` has three distinct real roots, located by the intermediate value theorem | **BUILT** |
| 8d | `fw_affine_inequiv`: no `z ↦ az + b` maps any three reals onto the comoving triangle (as sets). The proof compares real and imaginary parts of `(w₂ − w₁)(x₃ − x₁) = (w₃ − w₁)(x₂ − x₁)` | **BUILT** |
| 8e | `fw_rest_frame`: at `f = 1`, `E/f = 1 ⇔ E = 1` and `E² − f = 1 − f ⇔ E² = 1` | **BUILT** |
| 9 | `fw_action_odd`: `r(f − 1) = −2M − r³/α²`, odd under `R: (r, M) ↦ (−r, −M)` | **BUILT** |

**Non-vacuity, `fw_witness`:**
- the null horizon at `α = 1`;
- the turnaround at `M = ½`, `α = 1`, `r₀ = 1`;
- three real roots at `M = 1/10`;
- the triangle at `c = 1`.

**Against the registration:**
- **Size:** 290 lines against a band of 300–600.
- **The expected stop did not hold.** 8d, the preimage bookkeeping, closed by stating it for the image set directly,
  so the enumerated fallback was not needed.
- **Note on 8d:** it is stronger than registered. It needs no distinctness of the `xᵢ`, since equal preimages force a
  degenerate triangle, which is false.

**P7 tally:**
- **11 of 15 cored rows BUILT.**
- **Left for campaign 138:** 1 (the asymptotic non-intersection, a port of P2's `sr_future_diverges`), 3d (the
  injectivity of `p ↦ ℋ_c⁺(p)` in `ℝ^{1,4}`), 6 (the `sinh^{2/3}` law, a port of `rExp`) and the registered attempt
  at 7c (`|Im τ̃| ≤ πα/3`).
- **None touches P7's rate remark.**

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

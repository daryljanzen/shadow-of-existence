# `r7613+71.6` — RESULT: campaign 58, `r7613` ④, BUILT, both halves. ⌗ `244` lines in one probe (registered `250`, band 100–600). ⌗ both registered p came true (`0.9`, `0.85`); the `Matrix.inv` fallback was not needed

*Against `PREDICTION.md` (`r7613+71.2`). 71 re-ran `lake env lean probes/SchwarzschildSlicing.lean`. It exits 0
with no errors and 4 cosmetic linter notes. All `22` `#print axioms` lines read
`[propext, Classical.choice, Quot.sound]`.*

## Static slicing
- `ss_static_mul_inv`, `ss_static_inv_mul` and `ss_static_inv_eq` establish `(g_S)⁻¹ = diag(−f⁻¹, f, r⁻², (r² sin²θ)⁻¹)`
  as `Matrix.inv`, for `0 < r_h < r` and `sin θ ≠ 0`.
- `ss_static_gtt` gives `g^{tt} = −(1 − r_h/r)⁻¹`.
- `ss_static_gtt_tendsto` and `ss_static_gtt_matrix_tendsto` give `g^{tt} → −∞` along `r → r_h⁺`.
- `ss_lapse_tendsto` gives `N = √f → 0`.
- `ss_lapse_sq` and `ss_lapse_rpow` give `N = (−g^{tt})^{−1/2}`.

## Retarded slicing
- `ss_ret_mul_inv` and `ss_ret_inv_eq` cover the `(u, r)` block. `ss_ret4_*` cover the full 4×4 matrix. The
  inverse has `g^{uu} = 0`, `g^{ur} = −1`, `g^{rr} = f`.
- `ss_ret_norm` and `ss_ret4_norm` give `g^{ab}∇_aΘ∇_bΘ = a²(fη² − 2η) = a²η(fη − 2)` for `Θ = a(u + ηr)`.
- `ss_ret_tendsto` gives the limit `−2a²η` in the two-sided neighbourhood of `r_h`.
- `ss_ret_at_horizon` gives the exact value `−2a²η` at `r = r_h`.
- `ss_ret_neg_eventually` and `ss_ret_neg_nbhd` show the norm is strictly negative on a neighbourhood of `r_h`,
  for `a ≠ 0` and `η > 0`. So `Θ` stays a time function across the horizon, while the static lapse degenerates.

No census row moves.

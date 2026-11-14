# `r7765+71.2` — RESULT: campaign 139, **P13's nine reachable rows all BUILT (2a, 2b, 3a–3d, 4i, 4iii, 4iv). P13 stands at 9 of 10; row 1 is priced as beyond.** ⌗ `342` lines (band 350–650, **under by 8**), at p(all nine) `0.75`

*The registration is `PREDICTION.md`. The probe is the new standalone file `probes/Boundary.lean` (`bd_`), P13's citable
file. Of its 342 lines, 129 are the verbatim copy of P7's row-7c section; 213 are new.*

## Verification
- `lake env lean probes/Boundary.lean` gives **0 errors and 0 warnings**.
- **16 axiom lines** (3 for the copied `fw_` lemmas, 13 for `bd_`), every one `[propext, Classical.choice, Quot.sound]`.
- The forbidden-token grep is clean, imports are `Mathlib` only, and `check_no_sorry.py` reports ALL 29. No options are
  set.
- **The copy is byte-identical:** `Framework.lean`'s "Row 7c" block (`fw_y`, `fw_τ` and their lemmas through
  `fw_τ_cont`) diffs empty against `Boundary.lean`'s, in the same namespace `ShadowProbe.FrameworkProbe`.

## Rows

| Row | Statement (Lean) | Mark |
|---|---|---|
| 2a | `bd_parity`: `f = f_even + f_odd`, with `f_even = 1 + Q²/r² − Λr²/3` even in `r` and `f_odd = −2M/r` odd; hence `f(−r; −M) = f(r; M)` | **BUILT** |
| 2b | `bd_charge_even`: `f(Q) = f(−Q)`, while `A_t = −Q/r` is odd in `Q` | **BUILT** |
| 3a | `bd_R_isometry`: `Jᵀ g_{−M}(ρy) J = g_M(y)` for `g = diag(−f, 1/f, r², r² sin²θ)`, `ρ(t, r, θ, φ) = (t, −r, θ, φ)`, `J = diag(1, −1, 1, 1)`. `bd_Q_blind`: `g_{−Q} = g_Q` | **BUILT** |
| 3b | `bd_K_bead`: `K = conj` maps solutions of `r³ = 2Mα² sinh²(3τ̃/2α)` (`r, τ̃ ∈ ℂ`; `M, α` real) to solutions. `bd_K_antilinear`: `K(iz) = −iK(z)` and `K² = id` | **BUILT** |
| 3c | `bd_K_wings`: `K` fixes `ℝ`; for `r < −r₀`, `Im fw_τ(r) = −πα/3`, `Im K fw_τ(r) = +πα/3`, and both solve the bead at `r` | **BUILT** |
| 3d | `bd_RK`: `R ∘ K = K ∘ R` on `ℂ`, and `(R ∘ K)² = id` | **BUILT** |
| 4i | `bd_conj_rep`: `σ(a, b) = (b, a)` maps the weights of `𝟑`, `{(1, 0), (−1, 1), (0, −1)}`, onto their negatives (the weights of `𝟑̄`). `bd_neg_one_not_weyl`: `−1 ∉ Submonoid.closure {s₁, s₂}` (the simple reflections in fundamental-weight coordinates). The closure preserves the weights of `𝟑`; `−1` sends `(1, 0)` outside them | **BUILT** |
| 4iii | `bd_null_swap`: if `A = !![a, b; c, d]` has `Aᵀ η A = η` (`η = diag(−1, 1)`) and `det A = −1`, then `A(1, 1)` lies on the line of `(1, −1)` and `A(1, −1)` on the line of `(1, 1)` | **BUILT** |
| 4iv | `bd_R_fixed`: `−r = r ↔ r = 0`, and `0 < r ↔ −r < 0` | **BUILT** |

**Witnesses** (`bd_witness`):
- the parity at `M = Q = 1`, `Λ = 3`, `r = 2`, where `f = −15/4`;
- the isometry at the point `(0, 2, 1, 0)`;
- the wing swap at `α = r₀ = 1` (`M = ½`), `r = −2`, where `Im K τ̃ = π/3`;
- the null swap for `A = diag(1, −1)`.

**Against the registration:**
- **The named stop did not hold.** 4i's closure induction closed directly (`Submonoid.closure_induction`), so the
  fallback (an explicit six-element `W`) was not needed.
- **4iii is stated in components.** The four isometry and determinant equations are hypotheses on the entries, not a
  `Matrix` identity. This is the same content.
- **4i is a proof that `−1 ∉ W(A₂)` as a submonoid.** `W` is finite, so the submonoid and the subgroup coincide; the
  file does not prove that.
- **Size:** 342 lines against a band of 350–650 (estimate 450).

**P13 tally: 9 of 10 cored rows BUILT** (2a, 2b, 3a, 3b, 3c, 3d, 4i, 4iii, 4iv; 4ii is folded into 2a).
- **Row 1** (`prop:boundary`'s non-embedding) is NOT BEGUN, priced as beyond (Lie theory Mathlib lacks).
- **Not formalised (interpretive):** `C = (Q ↦ −Q)_field ∘ (R∘K)_geometric`; "`P` and `T` stay geometric"; "one `ℤ₂`,
  four faces"; "the matter/antimatter skeleton".

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

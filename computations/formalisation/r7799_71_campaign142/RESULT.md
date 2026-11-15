# `r7799+71.2` — RESULT: campaign 142, **P11's eight registered rows all BUILT (A1–A3, K1, K2, W1–W3). P11 stands at 8 of 12; K4 is reachable but priced separately, and A4, K3, W4 are beyond.** ⌗ `383` new lines (band 350–650, estimate 480, **in band**) plus a `332`-line verbatim copy, at p(all eight) `0.6`

*The census and registration are `PREDICTION.md`. The probe is the new standalone file `probes/Dynamics.lean` (715
lines), P11's citable file. The new rows are in `ShadowProbe.DynamicsProbe` (`dy_`).*

## Verification
- `lake env lean probes/Dynamics.lean` gives **0 errors and 0 warnings**.
- **16 axiom lines** (4 for copied P9 theorems, 12 for `dy_`), every one `[propext, Classical.choice, Quot.sound]`.
- The forbidden-token grep is clean, imports are `Mathlib` only, and `check_no_sorry.py` reports ALL 29.
- No options are set outside the copy. The copy carries `Range.lean`'s own `set_option maxHeartbeats 0 in` on
  `pw_Rlow_vanish`.
- **The copy is byte-identical.** Six blocks of `Range.lean` (332 lines) each appear verbatim in `Dynamics.lean`,
  and each is a substring of `Range.lean`:
  - the `KrCurvature` section;
  - `rn_Ric`/`rn_scal`;
  - `rn_Weyl`;
  - Row 8a;
  - Row 8b;
  - the `ij_` block through `pw_IJ`.

## Rows

| Row | Statement (Lean) | Mark |
|---|---|---|
| A1 | `dy_desitter`: on `c − kt > 0`, `ψ = −log(c − kt)` has `ψ_t = k e^ψ`, `(ψ_t)_t = ψ_t²` (ENERGY), and with `k² = Λ/3`, `3ψ_t² = Λe^{2ψ}` (AREA). Cosmic time `τ = −(1/k) log(c − kt)` has `dτ/dt = e^ψ`, and `a = e^ψ = e^{kτ}`: exact de Sitter, `H = k` | **BUILT** |
| A2 | `dy_shear`: if WAVE `(Rψ₁)_t = ΛRe^{2(γ−ψ)}` and AREA `(R₁)_t = 2ΛRe^{2(γ−ψ)}` hold for all `t`, then `C₀ = R₁ − 2Rψ₁` is constant; and with `R_t = R₁`, `ψ_t = ψ₁`, `R > 0`, the shear `s = ψ − ½ log R` has `s_t = −C₀/(2R)` | **BUILT** |
| A3 | `dy_W1_mukhanov`, `dy_W2_mukhanov`: `W₁ = cos kη − sin kη/(kη)` and `W₂ = −sin kη − cos kη/(kη)` solve `W″ + (k² − 2/η²)W = 0` at every `η ≠ 0`, with explicit first and second derivatives. `dy_Q_bounded`: with `a = −1/(Hη)`, `Q₂ = W₂/a → H/k` as `η → 0⁻`, and `|Q₁| ≤ |H| k² |η|³` for `|kη| ≤ 1` | **BUILT** |
| A4 | No obstruction at any order; unitary quantization | **NOT BEGUN** (beyond) |
| K1 | `dy_killing_xy`: for `eq:metric` with any `ψ, γ, R`, `L_{∂x} g = L_{∂y} g = 0` (all sixteen components; `dy_lie` is the coordinate Lie derivative in the copied `kr_pd`) | **BUILT** |
| K2 | `dy_not_killing`: for `ψ = sin t cos z` and **any** `γ, R`, `(L_ξ g)_xx` is `2` for `∂_t` at `(0, 0)`, `−2` for `∂_z` at `(π/2, π/2)`, and `2 cos 1 ≠ 0` for the boost `z∂_t + t∂_z` at `(0, 1)` | **BUILT** |
| K3 | "Exactly" two Killing vectors | **NOT BEGUN** (beyond) |
| K4 | Petrov type I | **NOT BEGUN** (reachable, priced separately) |
| W1 | `dy_wall_det`: `det g = −1` for every `H`, in the paper's `2du dv + H du² + dx² + dy²` and P9's `rn_pp` | **BUILT** |
| W2 | `dy_wall_vacuum`: `H = h₊(u)(x² − y²) + 2h×(u)xy` has all sixteen `R_μν = 0`, for any `h₊, h×` | **BUILT** |
| W3 | `dy_wall_regular`: for that `H`, `R = 0`, the Weyl bivector operator squares to zero, and `I = J = 0`. `dy_wall_typeN`: at `h₊ = 1`, `h× = 0`, `C_uxux = −1 ≠ 0`, so the wall is type N | **BUILT** |
| W4 | "All polynomial invariants vanish" (VSI) | **NOT BEGUN** (beyond) |

**Witnesses** (`dy_witness`, with K2's points explicit in `dy_not_killing`):
- the de Sitter background at `Λ = 3`, `c = k = 1`, `t = 0`;
- the Mukhanov modes at `k = 1`, `η = −1`;
- the wall at `h₊ = 1`, `h× = 0`: vacuum, with `C_uxux = −1`.

**Against the registration:**
- **The named stop did not hold.** A3's asymptotics closed through `Real.cos_bound`/`Real.sin_bound`; no fallback was
  needed.
- **K2 is stronger than the paper's verification.** It holds for any `γ, R`, not only "the corresponding solution",
  because the `xx` component already fails.
- **A2 takes WAVE and AREA as hypotheses on functions of `t`.** It does not derive them from `G_ab + Λg_ab = 0`.
- **A3's `Q₁` bound is a Taylor bound** (`|W₁| ≤ (kη)²` for `|kη| ≤ 1`), not a limit statement. `Q₁ = O(η³)`, which
  is `∝ a⁻³`.
- **The wall rows use P9's `rn_pp` (`H du² − 2du dv`).** W1 also states the paper's `2du dv` form; the two differ by
  `v ↦ −v`.
- **Size:** 383 new lines against an estimate of 480.

**P11 tally: 8 of 12 cored rows BUILT** (A1–A3, K1, K2, W1–W3).
- **K4** (type I) is reachable with `ij_I`/`ij_J`, priced at 400–700 lines alone.
- **A4, K3, W4** are beyond.
- **Not formalised (interpretive):** "admits rather than forces a quantum structure"; "the last confined stratum"; "a
  regular radiative boundary".

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

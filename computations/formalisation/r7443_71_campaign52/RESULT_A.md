# `r7443+71.65` — RESULT: campaign 52 (programme stage P1) BUILT. ⌗ Integration on S³: the sphere measure is invariant under unit-quaternion translations, the frame derivatives integrate to zero, and `∇²` is symmetric with `−∇² ≥ 0` on tensor fields. ⌗ `545` lines (band 400–1400, IN BAND). ⌗ p `0.45` came true

*Scored against `PREDICTION.md` (pushed at `r7443+71.61` before any Lean), not revised. `probes/S3Integration.lean`:
11 theorems on `[propext, Classical.choice, Quot.sound]`, `11 s`, no error or warning. The build was delegated and
re-run by 71 (`PROBE_RUN_A.txt`).*

| item | theorems | statement |
|---|---|---|
| 1 | `σ_finite_nonzero` | `σ = volume.toSphere` on the unit sphere of `ℝ⁴` is finite and nonzero; `σ univ = 4·vol(ball)` |
| 2 | `right_invariant`, `left_invariant` | `q ↦ q·g` and `q ↦ g·q` for `‖g‖ = 1` are linear isometries preserving `σ`. Built by hand (`sph_preserving`, `rmulH`/`lmulH`), because Mathlib packages neither |
| 3 | `integral_Ea` | `∫ E_a f dσ = 0` for every `f ∈ C¹(ℝ⁴)`, by differentiating the invariant `t ↦ ∫ f(q(cos t + sin t·u_a)) dσ` under the integral |
| 4 | `ibp`, `nab_skew`, `lap_symm`, `neg_lap_nonneg` | integration by parts; `∇_a` skew on tensor fields (connection terms via `ε`); `∫⟨∇²h,k⟩ = ∫⟨h,∇²k⟩` for `C²` fields; `∫⟨−∇²h,h⟩ = Σ_a ∫‖∇_a h‖² ≥ 0` |
| 5 | `Ea_poly`, `integral_D_poly`, `lapP_symm` | on polynomials, `E_a` is campaign 51's `D a`; `∇²` on polynomial tensors is symmetric |

***Carried to P4, as a stated limit:***
- These results assume `C¹`/`C²` on all of `ℝ⁴`. A smooth field given only on S³ needs an extension, e.g. `h(x/|x|)`
  times a radial bump that equals 1 near the sphere. P4 builds or avoids it.
- P4 must also identify P1's `nabP` with campaign 51's `nab` by unfolding, which is expected to be a one-line `simp`.

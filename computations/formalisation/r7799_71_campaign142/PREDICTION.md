# `r7799+71.1` — CENSUS AND PRE-REGISTRATION: campaign 142, **P11's cored rows: the de Sitter cut's admissible dynamics (`prop:admit`), the two Killing vectors (`prop:twoKV`), and the regular radiative wall (`prop:radiative-wall`)**. ⌗ `480` new lines (band 350–650) plus a `~330`-line verbatim copy, p(all eight BUILT) `0.6`

*Registered before any Lean, per r7799. The paper is P11, `corpus/dynamics_paper.tex`, read at `37fd9d2c9`; it has no
Lean paragraph. The probe is the new standalone `probes/Dynamics.lean` (`dy_`), P11's citable file. Mathlib only.*

**What is copied verbatim** from `probes/Range.lean` (P9), with names and namespaces kept, for the wall rows:
- the `KrCurvature` section (the `kr_` kit);
- `rn_Ric`, `rn_scal`, `rn_Weyl`;
- Row 8a's pp-wave block (`rn_H` … `rn_pp_witness`);
- Row 8b's (`pw_Rlow_vanish` … `pw_witness`);
- the `ij_` definitions with `pw_IJ`.

*The census covers P11's three propositions and the displayed computations each rests on (as for P17, campaign
140).*

## Census

### `prop:admit` (l.196) and `sec:nonlinear`'s displayed computations
| Row | Statement | Lines | p | Note |
|---|---|---|---|---|
| A1 | **The isotropic de Sitter background.** `ψ(t) = −log(c − kt)`, `k = √(Λ/3)`, solves `ψ_t = k e^ψ`, `ψ_tt = ψ_t²` (ENERGY) and `3ψ_t² = Λe^{2ψ}` (AREA). In cosmic time `τ = ∫ e^ψ dt` the scale factor `a = e^ψ` is `a₀e^{kτ}`, with `H² = Λ/3` | 40–70 | 0.9 | |
| A2 | **The shear charge.** In the homogeneous sector, WAVE `(Rψ_t)_t = ΛRe^{2(γ−ψ)}` and AREA `R_tt = 2ΛRe^{2(γ−ψ)}` give `d/dt (R_t − 2Rψ_t) = 0`; with `s = ψ − ½ log R`, `2R s_t = −C₀` | 30–50 | 0.9 | |
| A3 | **The Mukhanov mode is healthy.** `W₁ = cos kη − sin kη/(kη)` and `W₂ = −sin kη − cos kη/(kη)` solve `W″ + (k² − 2/η²)W = 0` on `η < 0`. With `a = −1/(Hη)`, `Q = W/a` has one branch `O(η³)` (`∝ a⁻³`) and one tending to the constant `H/k`: `Q` stays bounded as `η → 0⁻` | 80–140 | 0.7 | **The expected stop**: the asymptotics. **The fallback** is the two solutions, with the limits stated pointwise in a Taylor bound |
| A4 | No classical obstruction at any order, a deparametrized true Hamiltonian, unitary quantization in every checkable regime | — | — | **Beyond**: the Bianchi-identity consistency of a first-class system, Friedrich's stability theorem and Bunch–Davies quantization are not in Mathlib. Its computable support is A1–A3 |

### `prop:twoKV` (l.208)
The metric `eq:metric` is `e^{2(γ−ψ)}(−dt² + dz²) + e^{2ψ}dx² + R²e^{−2ψ}dy²`, with `ψ, γ, R` functions of `(t, z)`.
The Lie derivative is `(L_ξ g)_ab = ξ^c∂_c g_ab + g_cb ∂_a ξ^c + g_ac ∂_b ξ^c`, in the copied `kr_pd`.

| Row | Statement | Lines | p | Note |
|---|---|---|---|---|
| K1 | `∂_x` and `∂_y` are Killing for every `ψ, γ, R` | 30–50 | 0.9 | |
| K2 | For `ψ = sin t cos z` and **any** `γ, R`, none of `∂_t`, `∂_z` or the boost `z∂_t + t∂_z` is Killing: `(L_ξ g)_xx ≠ 0` at an explicit point | 50–90 | 0.85 | |
| K3 | "**Exactly** two": no other Killing vector at all | — | — | **Beyond**: the full Killing equation for a generic profile. The paper's verification itself rules out the three candidates, which is K2 |
| K4 | The Weyl tensor is Petrov type I | — | — | **Reachable but heavy**: `ij_I`, `ij_J` for a two-variable metric. Priced alone at 400–700 lines, so not in this campaign |

### `prop:radiative-wall` (l.222)
| Row | Statement | Lines | p | Note |
|---|---|---|---|---|
| W1 | **Non-degenerate.** `det g = −1` for every `H`, in both the paper's `2du dv + H du² + dx² + dy²` and P9's `H du² − 2du dv + dx² + dy²` (`v ↦ −v`) | 10–20 | 0.95 | |
| W2 | **Vacuum.** `H = h₊(u)(x² − y²) + 2h×(u)xy` has all sixteen `R_μν = 0`, for any `h₊, h×` | 50–80 | 0.85 | Through `rn_pp_vacuum_iff` |
| W3 | **Curvature-regular.** For that `H`: `R = 0`, the Weyl bivector operator squares to zero, and `I = J = 0`; and for `h₊ ≠ 0` the Weyl tensor is nonzero, so it is type N | 40–70 | 0.85 | Through `pw_nilpotent`, `pw_IJ` |
| W4 | "**All** polynomial curvature invariants vanish" (VSI) | — | — | **Beyond**: a theorem on the full algebra of curvature invariants. Its checkable core is W3 |

**Totals.** 3 statements, **12 cored rows**, **8 within reach this campaign** (A1–A3, K1, K2, W1–W3). K4 is reachable
but priced separately. A4, K3 and W4 are beyond.

## Registration: campaign 142
- **Rows:** A1, A2, A3, K1, K2, W1, W2, W3, in `probes/Dynamics.lean`.
- **Price:** 480 new lines (band 350–650), plus the verbatim copy. p(all eight BUILT) `0.6`.
- **The expected stop** is A3's asymptotics.
- **Non-vacuity:** witnesses at concrete values:
  - `Λ = 3`, `c = 1` (A1);
  - `k = 1`, `η = −1` (A3);
  - `(t, z) = (0, 0)`, `(π/2, π/2)`, `(0, 1)` (K2);
  - `h₊ = 1`, `h× = 0` (W2–W3).

**Interpretive, not formalised:**
- "admits rather than forces a quantum structure";
- "the last confined stratum before the wall";
- "a regular radiative boundary, not a place a clock is re-founded";
- the wall-name note.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

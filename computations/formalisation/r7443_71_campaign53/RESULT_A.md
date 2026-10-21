# `r7443+71.70` — RESULT: campaign 53 (programme stage P2) BUILT, uniformly in `m`, `d` and `λ`. ⌗ The polynomial spectrum of `∇²` on symmetric traceless tensors on S³, a degree bound for eigenvectors, and the exact TT count `2(m² − 4)` over ℂ AND over ℝ. ⌗ `2626` lines (band 800–3000, IN BAND). ⌗ p `0.30` came true

*Scored against `PREDICTION.md` (pushed at `r7443+71.62` before any Lean), not revised.
`probes/S3PolySpectrum.lean`: 30 theorems on `[propext, Classical.choice, Quot.sound]`, `171 s`, no error. Sections
1–8 are campaign 51, carried; sections 9–15 are new. The build was delegated and re-run by 71
(`PROBE_RUN_A.txt`).*

| item | theorems | statement |
|---|---|---|
| 1 | `Sd_fd`, `Sd_finrank`, `Sd_invariant` | `P_d` (symmetric traceless polynomial tensors of degree `≤ d`, on S³) is finite-dimensional, with `finrank = Σ_{N≤d} 5(N+1)²`, the harmonic count exactly. `∇²`, both `sl₂`s and the divergence preserve it |
| 2 | `lap_casimir`, `SJ_eq_CY`, `neg_lap_casimir`, `lap_spectrum` | `∇² = ½(S_J + C_K) − L·L` exactly, and `Σ E_a² = Σ Y_a²`. `P_d` has an eigenbasis `Ev` with `−∇²`-eigenvalues `(N(N+2) + μ(μ+2))/2 − 6`, `μ = N + 4 − 2t`, and these are all of them |
| 3 | `degree_bound` | a `−∇²`-eigenvector at `λ` in any `P_d` lies in `P_{⌈|λ|⌉+6}`: uniform |
| 4 | `tt_spectrum`, `tt_count`, `tt_count_real`, `finrank_TTR` | TT eigenvalues are exactly `m² − 3`. For `d ≥ m + 1` the TT eigenspace at `m² − 3` is ***spanned by campaign 51's eigen-tensors*** and has `finrank ℂ = 2(m² − 4)`. Its real part has `finrank ℝ = 2(m² − 4)`, which ***closes campaign 51's real-from-complex caveat*** |

***How the upper bound was reached without Clebsch–Gordan in Mathlib.***
- An explicit family `f_Y^q f_K^p(wᴺ⁻ᵗ T_t)` with five seed types, separated by one operator
  `Θ = hK − M·S_J + i(hY − M·C_K)`, so independent.
- A spanning family of the same size, from monomials reduced by `x₀² = 1 − x₁² − x₂² − x₃²`. Together these make it a
  basis.
- The TT filter `O = Ł∘div` acts on seed type `t` by `κ_t ≠ 0` for `t = 1, 2, 3` and by `0` for `t = 0, 4`. So TT
  eigenvectors use only campaign 51's two seed types.

***Mathlib gaps met and built around:*** Weyl complete reducibility and Clebsch–Gordan for `sl₂`, the harmonic
decomposition of polynomials on spheres, a degree-preservation lemma for derivations on `MvPolynomial`, and joint
eigenspace independence for commuting operators. Each was replaced by explicit construction and counting.

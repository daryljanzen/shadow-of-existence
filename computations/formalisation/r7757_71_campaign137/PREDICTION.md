# `r7757+71.1` — PRE-REGISTRATION: campaign 137, **P7's algebraic and complex rows: the de Sitter horizon is null, the horizon areas and surface gravities, the Nariai turning points, the turnaround time, and the two turnings**. ⌗ `420` new lines (band 300–600), p(all BUILT) `0.75`

*Registered before any Lean. The inventory is `r7755_71_survey/SURVEY.md`. The probe is a new standalone file,
`probes/Framework.lean` (`fw_`), which is P7's citable file (`corpus/CR_framework.tex`). It imports Mathlib only and
copies nothing: these rows need no curvature kit. None of these rows touches P7's rate remark (`eq:two-rate`), per
r7757.*

`f(r) = 1 − 2M/r − r²/α²`. The de Sitter member is `M = 0`, and the Nariai member is `M = α/(3√3)`.

## Rows

| Row | Statement | Lines | p | Note |
|---|---|---|---|---|
| 3a | In ingoing Eddington–Finkelstein form, `−f dv² + 2dv dr + r²dΩ²`, the inverse metric has `g^{rr} = f`. So at `r = α` with `M = 0` the hypersurface normal `dr` is null: `r = α` is a null hypersurface. The chart is regular there (`det ≠ 0` for `r ≠ 0`, `sin θ ≠ 0`) | 60–110 | 0.85 | The explicit inverse of the non-diagonal block |
| 3b | `M = 0`: `f(α) = 0`, area `4πα²`. Nariai: `f(α/√3) = f′(α/√3) = 0` (the two positive roots coincide), area `4π(α/√3)² = 4πα²/3` | 30–60 | 0.9 | |
| 3c | `κ = |f′(r_h)|/2`: `1/α ≠ 0` for de Sitter, `0` for Nariai | 20–40 | 0.95 | |
| 7a | Nariai: for `r ≠ 0`, `f(r) = 0 ⇔ r = α/√3 ∨ r = −2α/√3`, via `r³ − α²r + 2Mα² = (r − α/√3)²(r + 2α/√3)` | 30–60 | 0.9 | |
| 7b | With `r₀ > 0`, `r₀³ = 2Mα²`: at `r = −r₀` and `τ̃ = −iπα/3`, the bead `r³ = 2Mα² sinh²(3τ̃/2α)` holds in `ℂ`, and `1 − f(−r₀) = 0` | 40–80 | 0.85 | `Complex.sinh` at `−iπ/2` |
| 8a | `1 − f = 2M/r + r²/α²`, and `f = 1 ⇔ r³ = −2Mα²` (`r, α ≠ 0`) | 10–20 | 0.95 | |
| 8b | With `ω = −½ + i√3/2` (`ω³ = 1`, `ω ≠ 1`) and `c > 0` with `c³ = 2M`: the roots of `z³ + 2M` are `−c, −cω, −cω²`. They are pairwise distinct, the set is invariant under `z ↦ ωz`, and the three pairwise distances are equal (`c√3`) | 60–110 | 0.85 | |
| 8c | `0 < M < 1/(3√3)`: `r³ − r + 2M` has three distinct real roots, in `(−2, −1/√3)`, `(−1/√3, 1/√3)` and `(1/√3, 1)`, by the intermediate value theorem | 50–90 | 0.85 | |
| 8d | No `z ↦ az + b` (`a ≠ 0`) maps three distinct reals onto `{−c, −cω, −cω²}`: a real affine image has real cross-ratios `(w₂ − w₁)/(w₃ − w₁)`, and the triangle's is `½ − (√3/2)i` | 50–100 | 0.8 | Extracting preimages from the image equality |
| 8e | At `f = 1`: `dt/dτ = E/f = 1 ⇔ E = 1`, and `(dr/dτ)² = E² − f = 1 − f ⇔ E² = 1` | 15–30 | 0.95 | |
| 9 | `r(f − 1) = −2M − r³/α²`, odd under `R: (r, M) ↦ (−r, −M)` | 10–20 | 0.95 | |

**Non-vacuity:** a witness for every row with hypotheses:
- `α = 1` for 3a–c and 7a;
- `M = ½`, `α = 1`, `r₀ = 1` for 7b;
- `M = 1/10` for 8c, which also feeds 8d with `c = 1`, `M = ½` for the triangle.

**The expected stop** is 8d's preimage bookkeeping. **The fallback** is to state 8d for an ordered assignment
`a·xᵢ + b = wᵢ` with every permutation enumerated.

**Interpretive, not formalised:** the correspondence `𝒩`; property (iv); "the locus that defines the fundamental
rest frame"; "antimatter"; the closure of the bead on one smooth manifold.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

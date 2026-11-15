# `r7797+71.1` — CENSUS AND PRE-REGISTRATION: campaign 141, **P12's cored rows: the symmetric-space grading `so(5,1) = so(4,1) ⊕ 𝔪` (`prop:closure`)**. ⌗ `280` lines (band 200–400), p(all six BUILT) `0.7`

*Registered before any Lean, per r7797: take the next paper in the campaign sequence with no Lean paragraph, census
its cored rows, register, then build in a new standalone probe.*

*The sequence is r7763's survey: P13 (campaign 139) and P17 (campaign 140) are done, and the next is the runner-up
**P12, `corpus/algebroid_paper.tex`**. It has no Lean paragraph. The paper is read at `9ab1c83fb`. The probe is
`probes/Algebroid.lean` (`al_`), P12's citable file. Mathlib only.*

*The census covers the statements inside P12's one proposition (`prop:closure`, l.289), with the conventions of its
receipt `P12_bracket_closure.py`:*
- *`η = diag(−1, 1, 1, 1, 1, 1)` on `ℝ⁶`, indices `0..5`;*
- *`so(5,1) = {A : Aᵀη + ηA = 0}`;*
- *the generators `(M_μν)^ρ_σ = δ^ρ_μ η_νσ − δ^ρ_ν η_μσ`;*
- *`𝔥 = so(4,1)`, spanned by the `M_ab` with `a, b ≤ 4` (the elements of `so(5,1)` with row and column `5` zero);*
- *`𝔪`, spanned by the boosts `M_a5` (the elements of `so(5,1)` vanishing off row and column `5`).*

## Census: `prop:closure` (l.289)

| Row | Statement | Lines | p | Note |
|---|---|---|---|---|
| C0 | **The setting.** `so(5,1)` is closed under the commutator; `𝔥` and `𝔪` are subspaces of it; `so(5,1) = 𝔥 ⊕ 𝔪` (every element splits uniquely, `𝔥 ∩ 𝔪 = 0`) | 40–70 | 0.9 | Entrywise masks |
| C1 | `[𝔥, 𝔥] ⊂ 𝔥` | 15–30 | 0.95 | |
| C2 | `[𝔥, 𝔪] ⊂ 𝔪` | 20–40 | 0.9 | |
| C3 | `[𝔪, 𝔪] ⊂ 𝔥` | 20–40 | 0.9 | |
| C4 | **`𝔪` is not a subalgebra:** `M₀₅, M₁₅ ∈ 𝔪` and `[M₀₅, M₁₅] = −M₀₁`, which is nonzero and in `𝔥`, so not in `𝔪` | 20–40 | 0.95 | |
| C5 | **The count `10 + 5 = 15`:** the fifteen `M_μν` (`μ < ν`) are a basis of `so(5,1)`; ten lie in `𝔥` and five in `𝔪`. So `finrank 𝔥 = 10`, `finrank 𝔪 = 5` and `finrank so(5,1) = 15` | 80–150 | 0.6 | **The expected stop.** **The fallback** is linear independence and spanning stated without `finrank`, marked BUILT IN PART |

**Interpretive, not formalised:**
- the dictionary `𝔪 ↔ ℋ_⊥`, `𝔥 ↔ ℋ_a` and the reading of the inclusions as the hypersurface-deformation brackets;
- "the sign the substrate curvature".

**Outside the census** (in P12's text, not in a proposition), noted for completeness:
- the coset Killing form `∝ diag(+, −, −, −, −)` (`P12_coset_metric`);
- the Atiyah sequence's exactness over an orbit;
- the orbit dimensions `15 − dim 𝔥`;
- the horizon cubic's discriminant `−4α⁴(27M² − α²)` and its factorisation `(r − r₀)(r² + r r₀ + r₀² − 1)`.

**Totals.** 1 statement, **6 cored rows** (C0–C5), **all within reach**. Nothing is priced as beyond.

## Registration: campaign 141
- **Rows:** C0–C5, in `probes/Algebroid.lean`.
- **Price:** 280 lines (band 200–400). p(all six BUILT) `0.7`.
- **The expected stop** is C5's `finrank`.
- **Non-vacuity:** `M₀₁ ∈ 𝔥` and `M₀₅ ∈ 𝔪`, both nonzero, and the C4 bracket.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

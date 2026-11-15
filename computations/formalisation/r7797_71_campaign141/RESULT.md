# `r7797+71.2` — RESULT: campaign 141, **P12's six cored rows all BUILT (C0–C5). P12 is closed: 6 of 6.** ⌗ `324` lines (band 200–400, estimate 280, **in band**), at p(all six) `0.7`

*The census and registration are `PREDICTION.md`. The probe is the new standalone file `probes/Algebroid.lean` (`al_`),
P12's citable file.*

## Verification
- `lake env lean probes/Algebroid.lean` gives **0 errors and 0 warnings**.
- **14 axiom lines**, every one `[propext, Classical.choice, Quot.sound]`.
- The forbidden-token grep is clean, imports are `Mathlib` only, and `check_no_sorry.py` reports ALL 29. No options are
  set.

## Rows

*`al_skew A` is `Aᵀη + ηA = 0` read entrywise (`al_skew_iff`). The subspaces are `al_S P`: the elements of `so(5,1)`
whose above-diagonal entries vanish off the pattern `P`.*
- *`al_so`: all entries allowed;*
- *`al_h`: `ν ≠ 5`. By `al_mem_h` it is the part of `so(5,1)` with row and column `5` zero, i.e. `so(4,1)`;*
- *`al_m`: `ν = 5`. By `al_mem_m` it is the part vanishing off row and column `5`.*

| Row | Statement (Lean) | Mark |
|---|---|---|
| C0 | `al_so_bracket`: `so(5,1)` is closed under `[A, B] = AB − BA`. `al_direct_sum`: `𝔥, 𝔪 ≤ so(5,1)`, `𝔥 ⊓ 𝔪 = ⊥`, `𝔥 ⊔ 𝔪 = so(5,1)` | **BUILT** |
| C1 | `al_hh`: `[𝔥, 𝔥] ⊂ 𝔥` | **BUILT** |
| C2 | `al_hm`: `[𝔥, 𝔪] ⊂ 𝔪` | **BUILT** |
| C3 | `al_mm`: `[𝔪, 𝔪] ⊂ 𝔥`. The `(5, 5)` entry cancels through `A_k5 = −η_kk A_5k` | **BUILT** |
| C4 | `al_m_not_closed`: with the receipt's `(M_μν)^ρ_σ = δ^ρ_μ η_νσ − δ^ρ_ν η_μσ`, `M₀₅, M₁₅ ∈ 𝔪` and `[M₀₅, M₁₅] = −M₀₁`, which is in `𝔥`, nonzero, and not in `𝔪`. `al_M_mem_h`/`al_M_mem_m`: every `M_ab` (`a, b ≤ 4`) lies in `𝔥` and every `M_a5` in `𝔪` | **BUILT** |
| C5 | `al_dims`: `finrank so(5,1) = 15`, `finrank 𝔥 = 10`, `finrank 𝔪 = 5`, through `al_coord`, a linear equivalence of each pattern subspace with the functions on its allowed above-diagonal index pairs | **BUILT** |

**Witnesses** (`al_witness`): `M₀₁ ∈ 𝔥` and `M₀₅ ∈ 𝔪`, both nonzero; the C4 bracket is a nonzero element of `𝔥`.

**Against the registration:**
- **The named stop did not hold.** C5's `finrank` closed through the coordinate equivalence, not through linear
  independence of the `M_μν`.
- **`𝔥` and `𝔪` are defined by entry patterns**, and identified with the receipt's spans through C4's placement lemmas
  and C5's dimensions: ten `M_ab` in the 10-dimensional `𝔥`, and five `M_a5` in the 5-dimensional `𝔪`.
  That the `M_μν` are a basis is not stated separately.
- **Size:** 324 lines against an estimate of 280 (band 200–400).

**P12 tally: closed, 6 of 6 cored rows BUILT** (C0–C5).
- **Not formalised (interpretive):** the dictionary `𝔪 ↔ ℋ_⊥`, `𝔥 ↔ ℋ_a` and the reading of the inclusions as the
  hypersurface-deformation brackets; "the sign the substrate curvature".
- **Outside the census** (not in a proposition): the coset Killing form, the Atiyah sequence over an orbit, the orbit
  dimensions, and the horizon cubic's discriminant and factorisation.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

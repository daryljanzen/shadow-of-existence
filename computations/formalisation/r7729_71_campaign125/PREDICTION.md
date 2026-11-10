# `r7729+71.1` — PRE-REGISTRATION: campaign 125, **P8's radial geodesics (rows 4a–c), 60's `r7730` ⓶ statement repairs, and the off-diagonal Einstein components**. ⌗ `550` new lines (band 350–900), p `0.55`. **Expected stop:** the index repair's linear map `C¹[r₁, r₂] → C⁰[r₁, r₂]`

*Registered before any Lean.*
- **Everything goes into `probes/StaticEinstein.lean`, the file P8 cites,** so P8's citations stay exact. The cited
  names keep their names; three of them get stronger statements.
- **New names** are prefixed `es_`, `ok_` (the repairs) or `rg_` (the geodesics).
- **`OperatorKernel.lean`** stays the frozen campaign 123 record. It is not cited by P8.

## The repairs (60's `r7730` ⓶)

| Item | Repair | Lines | p |
|---|---|---|---|
| `ok_vacuum_iff_ode` | Drop the redundant `hf′`. The angular component on the reverse direction is closed through `ok_general_solution` (the SdS family), on which `f″/2 + f′/r + Λ = 0` identically | 40–80 | 0.9 |
| `ok_L_bound` | The operator bound. For `f` with `f′` continuous on `[r₁, r₂]`: `sup_{[r₁, r₂]} |Lf| ≤ max(1, r₂)(sup|f| + sup|f′|)` | 40–80 | 0.85 |
| `ok_index_one` | An explicit index. `L f = (rf)′` (one-sided at the ends) is a linear map from `C¹[r₁, r₂]` to `C⁰[r₁, r₂]`, as submodules of `ℝ → ℝ` vanishing off `[r₁, r₂]`. `ker L = span{1/r}`, `finrank ker L = 1`, `range L = ⊤`, and `finrank ker L − finrank (C⁰ ⧸ range L) = 1` as an integer. On the closed interval, as P8 states it | 150–300 | 0.55 |
| interval | The kernel on `[r₁, r₂]` is carried by `ok_index_one`. `ok_kernel` stays as the open-interval form, and both are true. **P8's wording `[r₁, r₂]` needs no change** | — | — |

## Added: the off-diagonal components

| Item | Statement | Lines | p |
|---|---|---|---|
| `es_offdiag` | `R_{bc} = 0` and `G^b_c = 0` for `b ≠ c`, for `diag(−A, 1/F, r², r² sin²θ)` | 30–80 | 0.85 |
| `es_sds_vacuum`, whole | For SdS, `G^b_c + Λδ^b_c = 0` for all 16 `(b, c)`. That is `thm:kernel`'s `T_{μν} = 0` formalised whole | 20–40 | 0.9 |

## Rows 4a–c (`prop:cosmo`, P8 l.339)

| Row | Statement | Lines | p |
|---|---|---|---|
| 4a | On the radial plane `diag(−f(r), 1/f(r))` (with `kr_Γ` on `Fin 2`), a geodesic `τ ↦ (t, r)` has `E = f(r)ṫ` conserved. If it is unit timelike (`−fṫ² + ṙ²/f = −1`), then `ṙ² = E² − f` | 120–250 | 0.7 |
| 4b | `E = 1`, `Λ = 3/α²`: `r(τ) = (2Mα²)^{1/3} sinh^{2/3}(3τ/2α)` has `ṙ = √(2M/r + r²/α²)` for `τ > 0`, so `ṙ² = E² − f` with `E = 1`. This is copied from `ShadowEngine`'s `sinh23_flow`, a Mathlib-only proof | 60–120 | 0.85 |
| 4c | `Λ = 0`: `r = (9M/2)^{1/3} τ^{2/3}` has `ṙ² = 2M/r` for `τ > 0` | 40–80 | 0.85 |

**The expected stop** is the index repair: the domain and codomain submodules, `derivWithin` on `Icc`,
`constant_of_derivWithin_zero`, and the fundamental theorem of calculus within `Icc` for the onto part. **The
fallback** is to state the kernel as `span{1/r}` with `finrank 1`, and onto-ness, without the quotient. That repair
would then be marked BUILT IN PART.

**Interpretive, not formalised:** "the flat ΛCDM scale factor" and "Oppenheimer–Snyder" in `prop:cosmo`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

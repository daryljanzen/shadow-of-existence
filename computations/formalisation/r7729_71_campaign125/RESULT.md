# `r7729+71.2` — RESULT: campaign 125, **P8's radial geodesics are BUILT (rows 4a–c). 60's four `r7730` ⓶ repairs are made. The off-diagonal Einstein components vanish, so SdS's `T_{μν} = 0` is formalised whole.** ⌗ `+459 / −54` lines in `StaticEinstein.lean`, inside the registered band of 350–900 (point `550`). ⌗ p `0.55` came true. The expected stop, the index map, fell, and no fallback was used

*Against `PREDICTION.md` (`r7729+71.1`). 71 ran `lake env lean probes/StaticEinstein.lean`. It exits 0 with no errors
and no warnings. All `37` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`: `21` from campaigns
123–124 and `16` new. The forbidden-token grep is clean, the probe imports only Mathlib, and `check_no_sorry.py`
reads ALL 29 THEOREMS COMPILE.*

**All of it is in `probes/StaticEinstein.lean`, the file P8 cites.** Every cited name keeps its name; three have
stronger statements. `OperatorKernel.lean` is unchanged, as campaign 123's record.

## 60's `r7730` ⓶ repairs

- **`ok_vacuum_iff_ode`:** the redundant `hf′` is gone. Only `f` differentiable on the interval is assumed, as in P8.
  - In the reverse direction, the ODE makes `f` the SdS profile (`ok_general_solution`).
  - On that profile, `f″/2 + f′/r + Λ = 0` is computed directly, using the new `ok_sds_hasDeriv`.
- **`ok_L_bound`:** the operator bound. For `f` differentiable on `[r₁, r₂]` with `f′` continuous there:
  - `sup |Lf| ≤ max(1, r₂)(sup |f| + sup |f′|)` over `[r₁, r₂]`;
  - the pointwise inequality is kept as the first conjunct.
- **`ok_index_one`:** an explicit index, on the closed interval as P8 states it.
  - **`ok_Lmap : ok_D r₁ r₂ →ₗ[ℝ] ok_C0 r₁ r₂`** is `f ↦ f + rf′`, which is `(rf)′` within `[r₁, r₂]` (`ok_Lfun_eq`).
  - **`ok_D`** is `C¹[r₁, r₂]`, one-sided at the ends; **`ok_C0`** is `C⁰[r₁, r₂]`. Both are submodules of
    `ℝ → ℝ` vanishing off `[r₁, r₂]`.
  - **Proved:** `ker L = ℝ ∙ (1/r)`, `finrank ker L = 1`, `range L = ⊤`, and
    `(finrank ker L : ℤ) − finrank (C⁰ ⧸ range L) = 1`.
  - **How:** the kernel by `constant_of_derivWithin_zero`; onto-ness by the fundamental theorem of calculus, after
    extending `g` continuously by clamping onto `[r₁, r₂]`.
- **The interval:** P8's `[r₁, r₂]` is now matched by `ok_index_one`. `ok_kernel` stays as the open-interval form,
  and both are true. **P8's wording needs no change.**

## Added: the off-diagonal components

- **`es_Ric_offdiag`:** `R_{bc} = 0` for `b ≠ c`, from the coordinate Riemann tensor.
- **`es_G_offdiag`:** `G^b_c = 0` for `b ≠ c`.
- **`es_sds_vacuum_full`:** for SdS, `G^b_c + Λδ^b_c = 0` for all sixteen `(b, c)`. **`thm:kernel`'s `T_{μν} = 0`
  is formalised whole.**

## Rows 4a–4c, `prop:cosmo` (P8 l.339) — BUILT

- **4a, `rg_cosmo`** (with `rg_Γ`, the Christoffel table of `diag(−f, 1/f)` from `kr_Γ`):
  - along a geodesic `ẍ^a + Γ^a_{bc}ẋ^bẋ^c = 0` of the radial plane, `E = f(r)ṫ` has zero derivative, so it is
    constant;
  - if the geodesic is unit timelike (`−fṫ² + ṙ²/f = −1`), then `ṙ² = E² − f`.
  - **`rg_witness`** (non-vacuity): `t = τ`, `r = 1` in Minkowski is a unit timelike geodesic.
- **4b, `rg_sinh23` and `rg_sinh23_radial`:** `r(τ) = (2Mα²)^{1/3} sinh^{2/3}(3τ/2α)` has
  `ṙ = √(2M/r + r²/α²)` for `τ > 0`. So `ṙ² = 1² − f(r)`: the `E = 1` equation. The proof is `ShadowEngine`'s
  `sinh23_flow`, copied, as it uses only Mathlib.
- **4c, `rg_tau23`:** `r = (9Mτ²/2)^{1/3} = (9M/2)^{1/3}τ^{2/3}` has `ṙ = √(2M/r)` for `τ > 0`.
- "The flat ΛCDM scale factor" and "Oppenheimer–Snyder" stay identifications by citation.

## Marks (P8's inventory, `r7725_71_survey/SURVEY.md`)

- **Built (12):** 1a–1e, 2, 3a–3c and 4a–4c.
- **Built in part (2):** 5b and 5c, in the other engine.
- **Not begun (1):** 5a.
- **No formal core (1):** 5d.

**Next (campaign 126):** 5a–c, the three leaves of `prop:trichotomy`. That would close P8.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

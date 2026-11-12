# `r7747+71.2` — RESULT: campaign 134, **P9's Kerr rows. Kerr–de Sitter is vacuum-Λ from the coordinate Riemann tensor (4a), its limits (4b), the constant-curvature `M = 0` member (4c), eq. `deltadecomp` (4d) and `J` (4e). All five are BUILT, with 4a and 4c in the chart `x = cos θ`.** ⌗ `638` new lines (band 700–1600, **under by 62**), at p `0.45`. **The expected stop did not hold:** `field_simp; ring` closed the Ricci components on the first full build

*The registration is `PREDICTION.md`. The probe is `probes/Range.lean`, P9's citable file, now 1086 lines, with the
section `kds_` appended.*

## Verification
- `lake env lean probes/Range.lean` gives **0 errors and 0 warnings** in about 8 minutes.
- **23 axiom lines** (14 from earlier campaigns, 9 new), every one `[propext, Classical.choice, Quot.sound]`.
- The forbidden-token grep (`sorry`, `admit`, `native_decide`, `axiom`) is clean, and the imports are `Mathlib` only.
- `check_no_sorry.py` reports ALL 29.
- The `KrCurvature` section is byte-identical to `StaticEinstein.lean`'s.
- **Options, stated in terms:**
  - `kds_Γ`, `kds_vacuum` and `kds_const_curv_aux` carry `set_option maxHeartbeats 0` and
    `linter.unusedSimpArgs false`. They are generated proofs over all index cases.
  - `kds_G233_dx` carries `maxHeartbeats 1000000`.

## The chart and the method
- **The chart is Boyer–Lindquist with `x = cos θ`.** The metric is
  `g = −(Δ_r/ρ²Ξ²)(dt − a(1−x²)dφ)² + (Δ_x(1−x²)/ρ²Ξ²)(a dt − (r²+a²)dφ)² + (ρ²/Δ_r)dr² + ρ²/(Δ_x(1−x²))dx²`.
  - `ρ² = r² + a²x²`, `Δ_r = (r²+a²)(1 − Λr²/3) − 2Mr`, `Δ_x = 1 + Λa²x²/3` and `Ξ = 1 + Λa²/3`.
  - Every component is rational in `(r, x)`. **The transfer of 4a and 4c to the θ chart is not formalised.**
- **A sympy generator** emits each `HasDerivAt` proof structurally, closed by `congr_deriv` with `field_simp` and
  `ring`. It covers 10 metric derivatives and 40 Christoffel derivatives, over 20 named Christoffel entries. It is
  recorded in `generator/`. Lean checks every emitted lemma; nothing rests on sympy.
- **The curvature** is the `kr_` kit's coordinate Riemann tensor, with nothing assumed:
  - `kds_inv` gives the explicit inverse;
  - `kds_Γ` gives `kr_Γ = kds_T` on the open set where `ρ², Δ_r, Δ_x, 1−x², Ξ ≠ 0`;
  - `kds_Hyp.U` and `kds_pd` carry it to a neighbourhood.

## Rows

| Row | Statement (Lean) | Mark |
|---|---|---|
| 4a | `kds_vacuum`: `rn_Ric (rn_kds a M Λ) x μ ν = Λ · rn_kds a M Λ x μ ν` for all 16, wherever `ρ², Δ_r, Δ_x, 1−x², Ξ ≠ 0`. **Non-vacuity, `kds_witness`:** `a = M = 1`, `Λ = 3` at `r = 2`, `x = 0`, where the hypotheses hold and the cross term `g_tφ = −3/2` is non-zero | **BUILT** (chart `x = cos θ`) |
| 4b | `kds_sds`: at `a = 0` the metric is `diag(−f, 1/f, r²/(1−x²), r²(1−x²))` with `f = 1 − 2M/r − Λr²/3`, entry by entry (`r ≠ 0`). `kds_desitter`: at `a = M = 0` it is static de Sitter. (`M = 0`, `a ≠ 0` is 4c.) | **BUILT** |
| 4c | `kds_const_curv`: at `M = 0`, `R_{abcd} = (Λ/3)(g_ac g_bd − g_ad g_bc)`, all 256 | **BUILT** (chart `x = cos θ`) |
| 4d | `kds_deltadecomp`: with `Λ = 3/α²`, `Δ_r = r²f_SdS + a²f_dS`, `Δ_x(cos θ) = 1 + (a/α)²cos²θ`, `Ξ = 1 + (a/α)²` | **BUILT** |
| 4e | `kds_J`: `Ma/Ξ² = 0 ↔ M = 0 ∨ a = 0` (for `Ξ ≠ 0`) | **BUILT** |

- **Against the registration:**
  - The size is 638 lines against a band of 700–1600: the generator's terms are long lines, not many lines.
  - The named stop, `field_simp; ring` on the Ricci components, did not hold. The ten distinct components closed on
    the first full build, and Lean's time went on the derivative closers.
  - Two fixes were needed:
    - **The pointwise forms.** `HasDerivAt.mul` and its siblings yield `f * g` as functions; the fix was the `fun_`
      variants.
    - **The leftovers in 4c.** `ring` fell back to `ring_nf` on 28 `ρ² = 0 ∨ True` goals; the fix was
      `ring_nf; simp`.
- **The hypotheses are wider than registered:** `kds_Hyp` asks `Δ_x, Ξ ≠ 0` rather than `Λ ≥ 0`.
- **A correction to the survey's totals** (`r7745_71_survey/SURVEY.md`). Its own listing has **17** rows, **13** with a
  formal core and 4 without (1, 2, 6, 9). Its totals line said 16, 9 and 7, which is wrong.
- **P9 tally:** 9 of 13 cored rows are BUILT (3a, 3b, 3c, 4a, 4b, 4c, 4d, 4e, 8a). Four remain NOT BEGUN, all priced in
  the survey:
  - 5, the Carter-form "iff";
  - 7a, Bianchi I, which needs `Real.rpow`;
  - 7b, its Petrov type;
  - 8b, the pp-wave's type N.

**Interpretive, not formalised:** "the offset taken in a twisted slice", and "sharing the throat" beyond `α² = 3/Λ`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

# `r7687+71.4` — RESULT: campaign 105, **7d BUILT on the shell model: on every finite slice the collapsing matter is exactly one point, in `D` and so outside `𝓗⁺`, at a finite `r > 2M`; it approaches its own horizon event `(u_H, v₀)` and reaches it only as `τ → ∞`.** ⌗ `11918` lines in one probe (`308` new, band 200–900). ⌗ p `0.7` came true. The expected stop (the shell ray as an inextendible causal curve in `D`) was not hit

*Against `PREDICTION.md` (`r7687+71.2`). 71 re-ran `lake env lean probes/ShellMatter.lean`. It exits 0 with no
errors and no warnings. All `332` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`: `311` inherited
and `21` new. The forbidden-token grep is clean, the probe imports only Mathlib, and `check_no_sorry.py` reads ALL 29
THEOREMS COMPILE. The probe copies campaign 102's `SchwarzschildShellHorizon.lean`.*

## The matter, a modelling choice

- **`sm_matter = {v = v₀} ∩ M′`.** This is where the metric changes form. The kit has no stress-energy.
- **`sm_curve`:** the shell ray `γ(s) = (u_H − e^{−s}, v₀)` is an `InextCausalCurveIn D`.
  - It is `C^∞` and future null.
  - As `s → −∞`, `ũ → −∞`. As `s → ∞`, `γ → (u_H, v₀) ∉ D`.
- **`sm_matter_D`:** `D ∩ matter` is the range of `γ`.
- **`sm_Θ_γ`:** along `γ`, `Θ = a(4Ms + (η/2 − 1)e^{−s} + const)`. For `η ≤ 2` this is strictly increasing
  (`sm_Θ_γ_strictMono`).

## ① One point per slice, outside `𝓗⁺` — BUILT

- **`sm_slice_meets_matter`:** for every `τ` (`0 < η ≤ 2`), `slice_τ ∩ matter` has exactly one point, `γ(s_τ)`. This
  comes from `sh_cauchy_D` applied to `γ`.
- **`sm_outside_H`:** `slice ∩ matter ∩ 𝓗⁺ = ∅`, for every `Θ`.

## ② Finite in extent — BUILT

**`sm_finite`:**
- `slice_τ ∩ matter = {γ(s_τ)}`, which is compact.
- There, `r = (v₀ − ũ)/2`, and `2M < r`.

## ③ Approaching its own horizon event — BUILT

**`sm_approaches`:**
- `γ → (u_H, v₀)`, which lies on `𝓗⁺` with `r = 2M` there.
- `Θ ∘ γ → ∞`.
- `s_τ` is strictly increasing in `τ` and tends to `∞`.
- On every slice, `ũ(γ(s_τ)) < u_H`.
- `γ(s_τ) → (u_H, v₀)` as `τ → ∞`.

So on every finite slice the element is short of its horizon event, and it reaches the event only in the limit.

## Non-vacuity, `sm_nonvacuous`

- It takes `M = 1`, `v₀ = 0`, `a = 1`, `η = 2`.
- `slice_0 ∩ matter = {(−8, 0)}`, at `r = 4 > 2`.

## Limits

- This is the radial plane, with one element, not a 2-sphere.
- The flat past has no regular centre.
- The shell is thin and only `C⁰`.
- **The matter is a modelling definition.**
- 7e has no formal content without a stress-energy, and is not attempted.

## Marks

- **7d → BUILT on the shell model, on the modelling reading.**
- The inventory is now **26 / 5 / 3**.
- **Left in part:** 2iii, 2iv-b, 5, 6b-ii and 7c.
- **Not begun:** 3c and 7e, which are interpretive, and 8ii-e, which needs a smoothed shell.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

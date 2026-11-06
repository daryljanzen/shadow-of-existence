# `r7687+71.2` — PRE-REGISTRATION: campaign 105, `r7687` ②, **7d on the shell model: on every finite slice the collapsing matter lies outside `𝓗⁺`, finite in extent, and still approaching its own horizon event.** ⌗ `350` new lines (band 200–900), p `0.7`. **Expected stop:** the shell ray as an inextendible causal curve in `D`, so that `sh_cauchy_D` gives the slice point

*Registered before any Lean. The new probe is `probes/ShellMatter.lean`, a copy of campaign 102's
`SchwarzschildShellHorizon.lean`. Everything new is prefixed `sm_`.*

## The modelling choice, stated plainly

**The matter is the shell, `𝔐 = {v = v₀} ∩ M′`.** The kit has no stress-energy, so "the matter" is read off where
the metric changes form (`sh_flat_past` / `sh_vacuum`), not derived. The radial plane carries one infalling element
per point of the shell. "Each element" is that element, not a 2-sphere's worth.

## ① One point per slice, outside `𝓗⁺` — p `0.75`

- **The shell ray** is `γ(s) = (u_H − e^{−s}, v₀)`: future null, in `D`, and inextendible in `D`.
  - As `s → −∞`, `ũ → −∞`.
  - As `s → ∞`, `ũ → u_H`, which leaves `D`.
- **`sm_slice_meets_matter`:** for every `τ`, the slice `S_τ` of the retarded slicing (`0 < η ≤ 2`) meets `𝔐 ∩ D` in
  exactly one point, `γ(s_τ)`. Existence and uniqueness come from `sh_cauchy_D` on `γ`.
- **`sm_outside_H`:** `S_τ ∩ 𝔐 ∩ 𝓗⁺ = ∅`. Slices lie in `D`, and `D ∩ 𝓗⁺ = ∅` (`sh_frontier`).

## ② Finite in extent — p `0.8`

- **`sm_finite`:** at the slice point, `r = (v₀ − ũ)/2` (`sh_r_shell`), and it is finite with `2M < r`.
- `S_τ ∩ 𝔐` is a single point, so it is compact.

## ③ Approaching its own horizon event — p `0.7`

- **`sm_approaches`:** `γ(s) → (u_H, v₀) ∈ 𝓗⁺` as `s → ∞`. That is the element's horizon event, at `r = 2M`.
- The slice parameter `τ(s) = Θ(γ(s)) → ∞`, and `s_τ` is increasing in `τ`.
- So on every finite slice the element is short of its horizon event, and it reaches the event only as `τ → ∞`.

## Limits

- This is the radial plane, so there is one element and no 2-sphere.
- The flat past has no regular centre.
- The shell is thin and only `C⁰`.
- **The matter is a modelling definition.**
- 7e stays unbuilt. Without a stress-energy it has no formal content beyond 7c and 7d.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

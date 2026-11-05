# `r7685+71.1` — PRE-REGISTRATION: campaign 102, `r7685` ①. **The frontier of `D` on the shell model: `∂D = 𝓗⁺ = {ũ = u_H}`, the future horizon alone, inside `M`.** ⌗ `600` new lines (band 300–1500), p `0.6`. **Expected stop:** the characterisation of `J⁻(O)` on the extended `M` (causal steps raise both null coordinates)

*Registered before any Lean. The new probe is `probes/SchwarzschildShellHorizon.lean`, a copy of campaign 101's
`SchwarzschildCollapse.lean`. Everything new is prefixed `sh_`. The inventory refresh, ② of `r7685`, is in
`r7685_71_inventory/INVENTORY.md`. It goes in this PR, and its cheapest row gets its own registration.*

## Why `M` must grow

In campaign 101, `M = D = {ũ < u_H}`. So `S.H J = frontier J⁻(O) = {ũ = u_H}` lies outside `M`. The registered fix is
to extend `M` across the horizon into the black-hole side.

## ① The extended shell model `sh_S`

- **`M′ = {ũ < v₀} ∩ {U(ũ) V(v) < 1}`.**
  - `U(ũ) = (ũ − u_H)/4M · e^{−ũ/4M}` and `V = e^{v/4M}`.
  - `ũ < v₀` keeps every outgoing ray meeting the shell at `r_s = (v₀ − ũ)/2 > 0`. There, `U′ > 0`.
  - `UV < 1` keeps `r > 0`.
- **The metric is `−Φ′ dũ dv`,** with `Φ′(ũ, v) = F_K(r) U′(ũ) V/4M` evaluated at `max(v, v₀)`, where
  `F_K = (32M³/r) e^{−r/2M}`. This is Kruskal pulled back.
- **Checked in advance, for every `ũ < v₀`:** at `v = v₀`, `hK(r_s) = U V`, so `r = r_s`, and `Φ′ = 1`.
  - So `Φ′ = 1` for `v ≤ v₀` (`sh_flat_past`), and it is Kruskal's `−F_K dU dV` for `v ≥ v₀` (`sh_vacuum`).
  - `Φ′` is positive on `M′` and continuous.
- **`Φ′ = Φ` on `D`** (`sh_agree`), which is the standard `F_K dU dV = f du dv`. So campaign 101's `sv_cauchy`
  carries over to `sh_S` on `D`, through campaign 98's `SeAgree`.

## ② The causal relation and `D`

- **`sh_seg_mem`:** `M′` is null-convex. A segment with `ũ` and `v` increasing stays in `M′`, because `U` is
  increasing on `ũ < v₀` and `UV ≤ U₂V₂ < 1` wherever `U > 0`.
- **`sh_chr`:** `Chr x y ↔ ũ_x < ũ_y ∧ v_x < v_y` in `M′`.
- **`sh_cau` / `sh_Jpast`:** `J⁻(O) = D = {ũ < u_H}`. A causal curve in `M′` raises both null coordinates, and
  `ũ_O(τ) < u_H`. This is the expected stop.

## ③ The frontier

- **`sh_frontier`:** `S.H J = frontier J⁻(O) = {ũ = u_H}`, the future horizon. It is non-empty and lies in `M′`
  (`U(u_H) = 0`).
- **"Alone":** the frontier has no past component, because the past of `D` is flat and boundaryless.
- **On `𝓗⁺`:** `r = 2M` where `v ≥ v₀`, and `Φ′ = 1` where `v < v₀`. So the horizon forms inside the body, in the flat
  region, before the shell arrives.
- **`sh_headline_D`:** `D = {ũ < u_H}`, `∂D = 𝓗⁺ ⊆ M′`, and the retarded slicing is Cauchy temporal on `D`
  (`0 < η ≤ 2`). So the slicing accumulates on this `𝓗⁺`.

## Stated in advance: the headline machinery does not run

`LocallyOneChart` asks for `hRep g` to be `C¹` in the chart. The thin shell's `Φ′` has a kink at `v = v₀`, so
`mh_causal_alignment_gh_N` and `mc_cone_kuratowski_N` cannot be applied. Accumulation as such is therefore not
machine-checked on the shell. Running it needs a smoothed shell, which brings `r` back as an ODE solution.

## Non-vacuity

`sh_nonvacuous`, with `M = 1`, `v₀ = 0`: a horizon point with `v < v₀` where `Φ′ = 1`; a horizon point with `v > v₀`
where `r = 2M`; and a point of `M′ ∖ D` (the black-hole side).

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

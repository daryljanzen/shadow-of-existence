# `r7685+71.3` — RESULT: campaign 102, **the shell model's frontier: `∂D = 𝓗⁺ = {ũ = u_H}`, the future horizon alone, inside the extended `M′`, with `r = 2M` on it after the shell and the horizon forming in the flat body before it.** The retarded slicing is still Cauchy on `D`. BUILT. ⌗ `11610` lines in one probe (`545` new, band 300–1500). ⌗ p `0.6` came true. The expected stop (`J⁻(O) = D`) was not hit

*Against `PREDICTION.md` (`r7685+71.1`). 71 re-ran `lake env lean probes/SchwarzschildShellHorizon.lean`. It exits 0
with no errors and no warnings. All `311` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`: `273`
inherited and `38` new. The forbidden-token grep is clean, the probe imports only Mathlib, and `check_no_sorry.py`
reads ALL 29 THEOREMS COMPILE. The probe copies campaign 101's `SchwarzschildCollapse.lean`.*

## ① The extended model `sh_S` — BUILT

- **The spacetime:** `M′ = sh_MS = {ũ < v₀, U(ũ)V(v) < 1}`, with `g = −Φ′ dũ dv` (`sh_hRep`).
  - `Φ′` is Kruskal's `F_K U′ V/4M`, taken at `max(v, v₀)`.
  - It is positive and continuous on `M′` (`sh_Φ_pos`, `sh_Φ_continuousOn`).
- **The identity checked in advance holds** (`sh_UV_shell`): `−U(ũ)V(v₀) = hK((v₀ − ũ)/2)` for every `ũ`. So
  `r = r_s` on the shell (`sh_r_shell`).
- **`sh_flat_past`:** `Φ′ = 1` for `v ≤ v₀`.
- **`sh_vacuum`:** for `v ≥ v₀`, `Φ′` is the Kruskal form.
- **`sh_agree`:** `Φ′ = Φ` (campaign 101's) on `{ũ < u_H}`.

## ② Causal structure — BUILT

- **`sh_seg_mem`:** `M′` is null-convex.
- **`sh_chr`:** `Chr x y ↔ ũ_x < ũ_y ∧ v_x < v_y`.
- **`sh_cau_le`:** causal steps raise both null coordinates. This goes through the flat `mink` steps.
- **`sh_Jpast`:** `J⁻(O) = {ũ < u_H} = D` (`sh_D`).

## ③ The frontier — BUILT

- **`sh_frontier`:** `S.H J = frontier J⁻(O) = {ũ = u_H}`. It is non-empty and lies in `M′` (`sh_H_sub`).
  - It is the future horizon alone. Nothing of it lies to the past, so there is no white-hole horizon.
- **`sh_H_r`:** `r = 2M` on `𝓗⁺` where `v ≥ v₀`.
- **`sh_H_flat`:** `Φ′ = 1` on `𝓗⁺` where `v ≤ v₀`. So the horizon forms inside the flat body before the shell
  arrives.
- **`sh_cauchy_D`:** the retarded slicing is Cauchy temporal on `D` for `0 < η ≤ 2`. It is carried over by conformal
  invariance from the flat restriction.
- **`sh_headline_D`:** all of the above in one statement: `D`, `J⁻(O) = D`, `𝓗⁺ = {ũ = u_H} ⊆ M′`, non-empty, and
  Cauchy.

## Non-vacuity, `sh_nonvacuous`

- It takes `M = 1`, `v₀ = 0`.
- `(−4, −1)` is on `𝓗⁺`, with `Φ′ = 1` there.
- `(−4, 1)` is on `𝓗⁺`, with `r = 2` there.
- `(−3, 0)` is in `M′ ∖ D`, on the black-hole side.
- `Φ′ > 1` at `(−5, 1)`.
- Cauchy holds at `η = 2`.

## As stated in advance

**The accumulation machinery does not run on the thin shell.** `Φ′` has a kink at `v = v₀`, so `LocallyOneChart` (a
`C¹` chart metric) fails. So "the slices accumulate on this `𝓗⁺`" is not machine-checked on the shell. That is the
inventory's row 8ii-e, which needs a smoothed shell.

## Marks

- **8ii-b on the collapse model:** `D`, its frontier `𝓗⁺` and the slicing's Cauchy property are all identified on one
  spacetime.
- **8ii-e** stays NOT BEGUN.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

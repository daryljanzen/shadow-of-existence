# `r7693+71.2` — RESULT: campaign 108, **8ii-e BUILT by conformal invariance: on the thin-shell collapse model, the retarded slicing's slices accumulate on `𝓗⁺ = {ũ = u_H}` and nowhere else (`KLi = KLs = 𝓗⁺`) with properness, and so do the observer's past cones, which never meet `𝓗⁺`. This is proved on the `C^∞` flat restriction and carried unchanged to the `C⁰` shell.** ⌗ `12328` lines in one probe (`407` new, band 200–900). ⌗ p `0.65` came true. The expected stop (the adapted observer) was not hit. The optional cone disjointness is BUILT too

*Against `PREDICTION.md` (`r7693+71.1`). 71 re-ran `lake env lean probes/ShellAccumulation.lean`. It exits 0 with no
errors and no warnings. All `362` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`: `332` inherited
and `30` new. The forbidden-token grep is clean, the probe imports only Mathlib, and `check_no_sorry.py` reads ALL 29
THEOREMS COMPILE. The probe copies campaign 105's `ShellMatter.lean`, and campaign 91's cone-disjointness chain is
copied in as `sa2_cone_disjoint`.*

## ① The flat restriction — BUILT

- **`sa2_flat_locallyOneChart`:** `sh_flat = cz_St.restrictM M′` is `LocallyOneChart`.
- **`sa2_S_chr`, `_D`, `_H`, `_slice`, `_cone`, `_sublevelProper`:** each says the shell's notion equals the flat one,
  because `sh_S = sh_flat.cz_scale Φ′`.
- **`sa2_flat_causal`:** `D = {ũ < u_H}`, `𝓗⁺ = {ũ = u_H} ⊆ M′`, and the observer is chronologically increasing.
- **`sa2_flat_cauchy`:** the retarded slicing is Cauchy temporal on `D` for `0 < η ≤ 2`.

## ② The adapted observer — BUILT, with no stop

- `g(τ) = Θ_shell(sv_O τ)` is continuous and strictly increasing (`mh_temporalD_chr`), and surjective (Cauchy, applied
  to `sa2_curve`, which is `sv_O` as an inextendible causal curve in `D`).
- **`sa2_O = sv_O ∘ g⁻¹`.** By `sa2_O_adapted`, it has the same range, it is chronologically increasing on both
  spacetimes, it is continuous, and `Θ(O′ τ) = τ`.

## ③ The accumulation — BUILT

- **`sa2_flat`:** `mh_causal_alignment_gh_N` on the flat restriction gives `SublevelProper` and
  `KLi = KLs = 𝓗⁺` for the slices.
- **`sa2_flat_cones`:** `mc_cone_kuratowski_N` gives `KLi = KLs = 𝓗⁺` for the cones, of `O′` and also of `sv_O`.
- **`sa2_flat_cone_disjoint`:** the cones miss `𝓗⁺`.
- **`sa2_shell`, on the `C⁰` shell `sh_S`:**
  - `range O′ = range sv_O`, and `Θ(O′ τ) = τ`;
  - `SublevelProper`;
  - `KLi = KLs = {ũ = u_H}` for the slices and for the cones of `O′`;
  - `𝓗⁺ = {ũ = u_H}`;
  - `cone(τ) ∩ 𝓗⁺ = ∅`.

## Non-vacuity, `sa2_nonvacuous`

- It takes `M = 1`, `v₀ = 0`, `a = 1`, `η = 2`.
- `(−4, −1)` is on `𝓗⁺`, in the flat body (`v < v₀`, `Φ′ = 1`).
- It lies in `KLi` of the slices and in `KLi` of the cones.

So the slices accumulate on the part of the horizon that formed inside the body.

## Stated plainly

- **Accumulation is causal, so the shell's `Φ′` never enters.**
- **Tangency (`mc_tangency_at_N`) involves `g`, and is not claimed on the shell.**
- This is the radial plane, with a two-dimensional flat past and no regular centre.

## Marks

- **8ii-e → BUILT.** `lem:alignment`'s collapse claims are now whole on the shell model: Cauchy (101), the frontier
  (102) and accumulation (108).
- The inventory is now **29 / 3 / 2**.
- **Left in part:** 2iv-b, 6b-ii and 7c.
- **Not begun:** 3c and 7e, both interpretive.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

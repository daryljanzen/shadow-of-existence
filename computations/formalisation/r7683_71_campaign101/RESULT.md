# `r7683+71.2` — RESULT: campaign 101, **the collapse exterior: on a thin-null-shell radial plane with a flat past, the retarded slicing, `a(u + ηr)` on the whole vacuum exterior and smooth through the body, is a Cauchy temporal function of `D` for every `0 < η ≤ 2`** (`sv_cauchy`). The eternal core lemma is BUILT. ⌗ `11065` lines in one probe (`1210` new, band 600–2500). ⌗ p `0.45` came true: ⓐ `0.6` came true; ⓑ `0.5` came true; the stretch ⓒ was not attempted. The expected stop (`η = 2`) was not hit

*Against `PREDICTION.md` (`r7683+71.1`). 71 re-ran `lake env lean probes/SchwarzschildCollapse.lean`. It exits 0
with no errors and no warnings. All `273` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`: `195`
inherited and `78` new. The forbidden-token grep is clean, the probe imports only Mathlib, and `check_no_sorry.py`
reads ALL 29 THEOREMS COMPILE. The probe copies campaign 100's `SchwarzschildConformal.lean`.*

## A generic Cauchy criterion — BUILT (new to the kit)

- **`MSpacetime.sv_cauchy_of_limits`:** on an open `U`, take `Θ` temporal. Suppose `Θ → +∞` along every inextendible
  causal curve to the future, and `Θ → −∞` to the past. Then `Θ` is Cauchy temporal on `U`.
- **`sv_monotone_of_brk`:** coordinate monotonicity along causal curves on all of `ℝ`.

## ⓐ The eternal core lemma — BUILT, for all `0 < η ≤ 2`

- **`sv_eternal_cauchy`:** on campaign 99's region I, `Θ_ψ = Θ_ret + aη ψ(4M log V)` is Cauchy temporal on `D`.
  - `ψ(v) = −(v₀ − v)·smoothTransition(v₀ − v)` is `C^∞`. It is `0` for `v ≥ v₀`, and tends to `−∞` as `v → −∞`.
- **`sv_eternal_eq`:** on `v ≥ v₀`, `Θ_ψ = Θ_ret`.
- **The past end (`sv_past_pure`)** uses the exact identity `sv_r_identity`, `r = 2M(log(−U) + log V − log(r/2M − 1))`.
  It gives `Θ_ψ ≤ C − 2Mηa log(r/2M − 1) → −∞` for every `η ≤ 2`, so **`η = 2` needs no separate case**.
  `sv_eta2_identity` is the registered form.
- **What this shows:** campaign 99's obstruction is only at the past end. Changing `Θ_ret` on `v < v₀` alone, for any
  `v₀`, makes it Cauchy on eternal Schwarzschild's region I.

## ⓑ The shell model — BUILT

- **`sv_S hM v₀`:** the flat plane in null coordinates `(ũ, v)`, restricted to `M = {ũ < u_H = v₀ − 4M}` and scaled
  by `Φ`.
  - `sv_hRep`: `g = −Φ dũ dv`.
  - `Φ` is continuous on `M` and positive.
- **`sv_flat_past`:** `Φ = 1` for `v ≤ v₀`.
- **`sv_vacuum`:** for `v ≥ v₀`, `Φ = (1 − 2M/r) F′(ũ)`, with `u = F(ũ) = ũ − 4M log((v₀ − ũ)/4M − 1)` and `r` given by
  Kruskal's `h(r) = e^{(v − u)/4M}`. So `−Φ dũ dv = −f(r) du dv`, which is Schwarzschild.
- **`sv_Φ_gt_one`:** `Φ > 1` on `v > v₀`, so the model is not flat.
- **`sv_D`:** for the observer `O(τ) = (u_H − e^{−τ}, τ)`, future timelike with `ũ → u_H`, `D = I⁻(O) = M`. The past of
  `D` is flat Minkowski, so there is no white-hole horizon.
- **`sv_cauchy` / `sv_cauchy_D`:** `Θ_shell = Θ_ψ ∘ χ` is Cauchy temporal on `D` for `0 < η ≤ 2`.
  - `χ(ũ, v) = (U(ũ), e^{v/4M})`, with `U(ũ) = −((v₀ − ũ)/4M − 1)e^{−ũ/4M}`, which is `−e^{−F/4M}` on `M`
    (`sv_χU_eq`).
  - The transport is through monotone coordinate paths (`sv_shell_fut`, `sv_shell_past`) and the conformal invariance
    of Cauchy temporality, which removes `Φ`.
- **`sv_retarded_eq`:** on `v ≥ v₀`, `Θ_shell = a(F(ũ) + ηr)`, which is **P1's `a(u + ηr)` exactly**.
- **Non-vacuity, `sv_nonvacuous`:**
  - It takes `M = 1`, `v₀ = 0`, `a = 1`.
  - Cauchy holds at `η = 2` and `η = 1`, and the eternal lemma at `η = 2`.
  - `Φ(−5, 0) = 1 < Φ(−5, 1)`.
  - `Θ_shell` is not constant.

## Not done

- **The frontier of `D` is not proved to be the future horizon `ũ = u_H` alone.** That `D` is the open half-plane, with
  its past flat, is proved (`sv_D`).
- The stretch ⓒ, the black-hole side inside `M`, so that `𝓗⁺ ⊆ M` and the headline can run, was not attempted.

## Limits, as registered

- **This is the radial plane, and the flat past is two-dimensional,** with no regular centre. The four-dimensional
  centre, where the outgoing cones close, is replaced by the flat half extending past `r = 0`.
- **The shell is thin,** so `Φ` is only `C⁰` across `v = v₀`. The kit's spacetimes ask for a continuous metric, and
  Cauchy temporality is conformally invariant.
- **`Θ = a(u + ηr)` holds on the vacuum exterior.** Inside the body it is the smooth continuation `a(u + η r_S + ηψ)`.

## Marks

- **P1 `lem:alignment` (ii), the retarded slicing's Cauchy property → BUILT on a collapse model.** That finishes the
  retarded half of 8ii-b.
- **For l.382, proposed sentence:** "on a radial-plane collapse by a thin null shell with flat past, the retarded
  slicing, equal to a(u+ηr) on the vacuum exterior and continued smoothly through the body, is a Cauchy temporal function
  of D for 0 < η ≤ 2 (`sv_cauchy`, `sv_retarded_eq`); on the eternal exterior, changing it only in the past suffices
  (`sv_eternal_cauchy`)."

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

# `r7683+71.1` — PRE-REGISTRATION: campaign 101, `r7683`. **The collapse exterior for the retarded slicing's Cauchy property** (P1 `lem:alignment` (ii)). Model: a **thin ingoing null shell** in the radial plane (the step-mass Vaidya analogue), with a flat past and therefore no white-hole horizon. Claim: **the retarded slicing, equal to `a(u + ηr)` on the whole vacuum exterior and continued smoothly through the body, is a Cauchy temporal function of `D` for `0 < η ≤ 2`.** ⌗ `1200` new lines (band 600–2500), p `0.45` for the whole. **Expected stop:** the past-end divergence at `η = 2`

*Registered before any Lean. The new probe is `probes/SchwarzschildCollapse.lean`, a copy of campaign 100's
`SchwarzschildConformal.lean`. Everything new is prefixed `sv_`.*

## Which collapse model is cheapest, and why the thin shell

- **The thin null shell is cheapest.** The past `v < v₀` is flat. After the shell, `v > v₀`, the plane is Schwarzschild
  of mass `M`.
  - **In the flat retarded coordinate `ũ` and advanced `v`, everything is explicit.**
    - The metric is `−Φ dũ dv`, with `Φ = 1` for `v ≤ v₀` and `Φ = f(r) F′(ũ)` for `v ≥ v₀`. It is continuous across
      the shell, where `f F′ = 1`.
    - The retarded time is `u = F(ũ) = ũ − 4M log((v₀ − ũ)/4M − 1)`.
    - `D` is the half-plane `ũ < u_H = v₀ − 4M`.
  - **Its one defect is that `Φ` is only `C⁰` across the shell.** The kit's `MSpacetime` asks only for a continuous
    metric. Cauchy temporality is conformally invariant (`cz_scale_isCauchyTemporalOn`), so the shell's kink does not
    enter.
- **Smooth-mass Vaidya:** `r` is the solution of an ODE, not a formula. That brings flow existence and `C¹` dependence,
  which costs far more.
- **Oppenheimer–Snyder:** a dust interior matched across a timelike surface. That needs junction conditions and
  costs more again.

## The one subtlety, settled in advance

- **`Θ = a(u + ηr)` with the true `r` is not `C¹` across the shell,** because `∂r` jumps there. The kit's
  `IsTemporalOn` asks for `C¹`.
- **So the registered `Θ` is a single smooth formula:** `Θ = a(u + η r_S + η ψ(v))`.
  - `r_S` is Schwarzschild's areal radius as a function of `(u, v)`, defined on the whole of `D`.
  - `ψ(v) = −(v₀ − v)·smoothTransition(v₀ − v)` is `C^∞`. It is `0` for `v ≥ v₀`, non-decreasing, and tends to `−∞` as
    `v → −∞`.
- **On the vacuum exterior `v ≥ v₀`, `r_S` is the true `r` and `ψ = 0`, so `Θ = a(u + ηr)` exactly.** This is P1's
  slicing, and inside the body it is "continued inward" as P1 l.382 says.

## ⓐ The eternal statement, the core lemma — `450` lines, p `0.6`

On campaign 99's region I, `Θ_ψ = sr_Θ + aη ψ(4M log V)` is Cauchy temporal on `D` for `0 < η ≤ 2`, and it equals
`sr_Θ` on `{v ≥ v₀}`.
- **Temporality:** `sr_temporal`, plus a non-negative `ψ′` term.
- **Future end:** `sr_future_diverges`, with `ψ ≥ ψ(start)` along the future.
- **Past end, the new part:** either `V → 0`, where `ψ → −∞` and the rest is bounded above for `η ≤ 2`; or
  `U → −∞` with `V → V_∞ > 0`, where `r → ∞`.
  - For `η < 2`, use `r ≤ 2M log(−UV) + C`.
  - **For `η = 2`, use the exact identity** `−4M log(−U) + 2r = 4M log V − 4M log(r/2M − 1) → −∞`. This is the
    expected stop.
- **So campaign 99's obstruction is only at the past end.** Any change of `Θ_ret` confined to `v < v₀` removes it.

## ⓑ The collapse model — `600` lines, p `0.5`

- **`sv_S`:** flat `−dũ dv` scaled by `Φ` on the half-plane, with `Φ` continuous and positive.
  - `sv_flat_past`: `Φ = 1` for `v ≤ v₀`.
  - `sv_vacuum`: for `v ≥ v₀`, `Φ dũ dv = f(r) du dv` with `u = F(ũ)`. That is Schwarzschild in null coordinates.
- **`sv_D`:** for a static observer at `r₀ > 2M`, `D = I⁻(O) = {ũ < u_H}`, and the frontier of `D` is the future
  horizon `ũ = u_H` alone. **The past of `D` has no boundary, so there is no white-hole horizon.**
- **`sv_cauchy`:** `Θ_shell = Θ_ψ ∘ χ` is Cauchy temporal on `D` for `0 < η ≤ 2`.
  - Here `χ(ũ, v) = (−e^{−F(ũ)/4M}, e^{v/4M})` maps `D` onto region I, preserving both null orders.
  - It is transported as campaign 98 transported `t` through `V ↦ log V`.
- **`sv_retarded_eq`:** on `v ≥ v₀`, `Θ_shell = a(u + ηr)`, with `r` the shell spacetime's areal radius.
- **Non-vacuity, `sv_nonvacuous`:** `M = 1`, `v₀ = 0`, `η = 2` (the boundary case), and `η = 1`. `Φ ≢ 1`, and
  `Θ_shell` is not constant.

## ⓒ Stretch, p `0.25`

The black-hole side of the shell model inside `M`, through the Kruskal-type `U(ũ) = −e^{−ũ/4M}((v₀ − ũ)/4M − 1)`,
which is smooth across `u_H`. With it, `𝓗⁺ ⊆ M` and the headline could run.

## Limits stated in advance

- **This is the radial plane, and the flat past is two-dimensional Minkowski.** There is no regular centre. The four-
  dimensional centre, where P1's outgoing cones close, is replaced by the flat half extending past `r = 0`.
- **The shell is thin,** so the metric is only `C⁰` across it.
- **`Θ = a(u + ηr)` holds on the vacuum exterior.** Inside the body it is a smooth continuation, not `a(u + ηr)`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

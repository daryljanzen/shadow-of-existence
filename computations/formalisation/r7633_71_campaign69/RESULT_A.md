# `r7633+71.3` — RESULT: campaign 69, `r7633` ①, the ∂J⁻ generators are a.e. differentiable with causal velocity BUILT, null a.e. BUILT, and θ-reparametrised with `dθ(σ′) = 1` a.e. BUILT on `[0,1]` (the inextendible case is assembled only piece by piece). ⌗ `3733` lines in one probe (campaign 67's copy plus about `519` new against the registered `600`). ⌗ every registered p came true (`0.75`, `0.55`, `0.4`)

*Against `PREDICTION.md` (`r7633+71.1`). 71 re-ran `lake env lean probes/GeneratorRegularity.lean`. It exits 0 with
no errors. All `93` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`.*

## ① a.e. differentiable, with causal velocity

- `gr_ae_differentiableAt_of_lipOn` is Rademacher on an interval, from Mathlib's
  `LipschitzOnWith.ae_differentiableWithinAt_of_mem`.
- `gr_ae_velocity` and `gr_ae_velocity_fut`: a `LipCausal` curve, or a `FutCausal` one on `[0,∞)`, is
  differentiable at almost every parameter, with velocity in the closed cone.
- That uses `gr_velocity_mem_cone_fd`, campaign 61's lemma, copied in.

## ② Null a.e.

The registered stop did not occur.

- `gr_chr_of_timelike_deriv`: a single point of differentiability with timelike velocity gives
  `γ(t) ≪ γ(t+h)` for small `h`. The straight chord is a timelike step.
- `gr_ae_null` and `gr_ae_null_fut`: an achronal causal curve has `g(γ′,γ′) = 0` almost everywhere.
- **`gr_generator_null_ae`**: campaign 67's `cg_generator`, with a.e. differentiability, causal velocity and
  `g(γ′,γ′) = 0` a.e. added in both of its cases.

## ③ Reparametrisation by the time function

- **`gr_theta_reparam`** applies to a non-constant causal piece on `[0,1]`. It has a Lipschitz
  θ-parametrisation `σ` with the same image and endpoints, with `θ(σ s) = s`. For almost every `s`, `σ` is
  differentiable, `σ′ ∈ CC`, and `dθ(σ′) = 1`.
- `gr_theta_reparam_null`: for an achronal piece, also `σ′ ≠ 0` and `g(σ′,σ′) = 0` a.e.

***Not built:*** one θ-parametrisation of the whole inextendible generator on `[0,∞)`. Each unit piece is done. The
first missing lemma is gluing infinitely many θ-parametrised pieces into one locally Lipschitz curve. That needs a
chord bound across piece boundaries on a compact union of pieces.

No census row moves.

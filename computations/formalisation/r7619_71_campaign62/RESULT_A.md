# `r7619+71.3` — RESULT: campaign 62, `r7619` ②, the flow is `C¹` in the initial point and the flow-box chart exists, BUILT on a vector space; `lem:killing` (b) coordinate-free BUILT on the model space; the manifold transfer REPORTED. ⌗ `891` lines in one probe (registered `900`, band 300–2500). ⌗ p: flow `C¹` `0.6` came true, flow box `0.45` came true, manifold transfer `0.25` did not

*Against `PREDICTION.md` (`r7619+71.2`). 71 re-ran `lake env lean probes/FlowC1.lean`. It exits 0 with no errors.
All `37` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`. T3b's stop at `flow_hasFDerivAt`
(`r7281+71.5`) is closed.*

## ① The flow is `C¹` in the initial point

***Setting.*** A `C¹` vector field `f` on a finite-dimensional real normed space `E`.
- `FlowData f x₀` holds the Picard–Lindelöf flow `α x t` for `x ∈ closedBall x₀ r` and `t ∈ [−τ, τ]`.
- `τ` is shrunk so that `Mτ ≤ 1/2`. The variational equation `J′ = Df(α)∘J`, `J(0) = id`, is then one more
  Picard–Lindelöf application in `E →L E`.

***Estimates.*** Two Grönwall estimates hold uniformly in time:
- `fc_remainder_uniform`: `‖α y s − α x s − J x s (y−x)‖ ≤ ε‖y−x‖`;
- `fc_J_uniform`: `‖J y s − J x s‖ ≤ ε`.

***Results.***
- `fc_flow_hasFDerivAt`: `D_x α(·, t) = J(x, t)`. This is the declaration T3b stopped at.
- `fc_flow_contDiffOn`: `C¹` in `x`.
- `fc_flow_contDiffOn_joint`: `C¹` jointly in `(t, x)` on `(−τ, τ) × ball`.
- `fc_flow_C1`: the headline, stated without `FlowData`.

## ② The flow-box chart

***Construction.*** `fc_complement_equiv` turns a complement `H` of `ℝ∙f(x₀)` into `ℝ × H ≃L E`.

***Results.***
- `fc_flowBox` and `fc_flowBox_exists`: if `f(x₀) ≠ 0`, there is an `OpenPartialHomeomorph (ℝ × H) E` with the
  following properties:
  - `Φ(λ, h) = α(x₀ + h, λ)`;
  - `Φ(0,0) = x₀`;
  - `Φ` is `C¹` on its source;
  - `DΦ(0,0)(a, h) = a·f(x₀) + h`;
  - `DΦ · (1,0) = f ∘ Φ`, i.e. `f = ∂_λ`;
  - `Φ⁻¹` is `C¹` near `x₀`.
- The proof is the inverse function theorem.

## ③ `lem:killing` (b), coordinate-free on the model space

- `fc_flow_pushes_field`: `f(α x t) = J(f x)`.
- `fc_flow_isometry`: if `L_f g = 0`, the flow is an isometry, `g(α x t)(Jv)(Jw) = g x v w`.
- `fc_flowBox_pullback` and `fc_flowBox_killing`: in the flow-box chart the pulled-back metric does not depend on
  `λ`, i.e. `∂_λ g_ab = 0`.
- `fc_isKilling_lie` and `fc_flowBox_killing_of_isKilling` derive the same from `LieDerivProbe`'s `IsKilling`. Its
  definitions are copied verbatim, since probes cannot import probes.

***What this supplies.*** This is the step campaign 59 took as its setting: a Killing field gives an adapted chart
with `χ = ∂_λ` and `λ`-independent components.

## REPORTED: the manifold transfer

***First missing declaration:***
`fc_flowData_exists_of_contDiffOn : ContDiffOn ℝ 1 f (ball x₀ ρ) → Nonempty (FlowData f x₀)`, a localized
constructor.
- `FlowData` currently assumes `ContDiff ℝ 1 f` on all of `E`, but a chart representative is `C¹` only on the
  chart target.
- Mathlib's `IsPicardLindelof.exists_forall_mem_closedBall_eq_hasDerivWithinAt_lipschitzOnWith` does not export
  that trajectories stay in the Picard–Lindelöf ball. `FunSpace.compProj_mem_closedBall` is used inside its proof
  but is not stated.

***Also not written.***
- The chart pushforward, and the `mfderiv` form of `DΦ · e_λ = X ∘ Φ`.
- The link to campaign 59's global `KillingChart` record. It needs a local version of that record, since the chart
  here is local.

No census row moves.

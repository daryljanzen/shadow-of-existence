# `r7613+71.7` — RESULT: campaign 59, `r7613` ②, BUILT in the adapted chart (the registered target); the manifold stretch REPORTED. ⌗ `280` lines in one probe (registered `500`, band 200–1200). ⌗ all three registered p came true (forcing `0.85`, transport `0.6`, `cor:stationary` `0.7`)

*Against `PREDICTION.md` (`r7613+71.3`). 71 re-ran `lake env lean probes/KillingHorizon.lean`. It exits 0 with no
errors. All `18` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`.*

***Setting.***
- `KillingChart` consists of a symmetric metric field `g` on `ℝ × E`, with index 0 being `λ`, and the Killing
  equation in adapted coordinates, `g(λ + s, x) = g(λ, x)`.
- The derivative form `∂_λ g_ab = 0` is `kh_killing_deriv`.

***Forcing.***
- `kh_interval_orbit`: `ds² = |χ|² dλ²`.
- `kh_forcing`: null with `dλ ≠ 0` gives `|χ|² = 0`.
- `kh_null_along_generator`: null at one parameter gives `|χ|² = 0` along the whole orbit, with the orbit null
  everywhere.

***(b) as isometric transport.***
- `kh_flow_isometry`, `kh_flow_hasFDerivAt` and `kh_flow_pullback`: `Φ_s^* g = g`, with `dΦ_s = id`.
- `kh_flow_orbit`, `kh_flow_maps_union_of_orbits` and `kh_flow_image_subset`: `Φ_s` maps each generator, and `𝒦`,
  into itself.
- `kh_transverse_invariant`, `kh_transverse_restricted` and `kh_transverse_invariant_between`: every transverse
  invariant agrees at `p`, at `q`, and at every point between them.
- `kh_delta_x_zero` and `kh_delta_tau_zero`: `Δx = 0`, then `Δτ = 0`.

***`lem:killing`.*** `kh_lemma_killing` proves that two events on one null generator, with `dλ ≠ 0`, are
`MetricallyCoincident`: (a), (b), (b) between them, `Δx = 0` and `Δτ = 0` all hold.

***`cor:stationary`.*** `kh_cor_stationary` assumes `Rigidity` as a HYPOTHESIS: the horizon is a Killing horizon
in some Killing chart, which needs analyticity. Under it, `𝓗⁺` is flow-invariant and every pair of events on one
generator is metrically coincident.

***REPORTED: the coordinate-free version.*** The first missing Mathlib piece is smooth dependence on initial
conditions for the flow of a smooth vector field. That gives the flow-box theorem, `χ ≠ 0` ⇒ there is a chart with
`χ = ∂_λ`, and with it the pullback `Φ_s^* g` and `L_χ g = 0 ⇒ Φ_s^* g = g`. Mathlib has local integral curves
and their uniqueness, but not this.

No census row moves.

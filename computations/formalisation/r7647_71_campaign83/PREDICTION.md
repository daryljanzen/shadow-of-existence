# `r7647+71.1` — PRE-REGISTRATION: campaign 83, `r7647` ①. The nondegeneracy field in `KillingChart`. Every probe that builds a `KillingChart` re-checks, and the witness is kept. ⌗ under `60` changed lines across `2` probes, ⛔ stop `150`. ⌗ p: all of campaign 59's theorems re-check unchanged `0.9`; the witness re-checks with the field discharged by its determinant `0.9`; `kw_zero_rigidity` is replaced by a proof that the zero metric is now excluded `0.85`

*Under `r7647` ①. No Lean was changed before this registration.*

***The field.*** `nondeg : ∀ p, (Matrix.of (g p)).det ≠ 0`, with `Comp n = Fin (n+1) → Fin (n+1) → ℝ`, added to
`KillingChart` in `probes/KillingHorizon.lean` (campaign 59) and in its copy `probes/KillingWitness.lean` (campaign 82).
- It is nondegeneracy, not full Lorentzian signature. `lem:killing`'s argument uses the Killing field's null orbit and
  the `λ`-independence of the components, and never the signature.
- RESULT says whether any theorem's proof would use the signature. None is expected to.

***The population.*** A grep finds `KillingChart` built only in those two files.
- `FlowManifold.lean` and `LieDerivManifold.lean` have a different structure, `LocalKillingChart`. It carries no metric
  field of its own: its components are pulled back from the manifold metric `gc`.
- RESULT says whether `gc`'s nondegeneracy is assumed anywhere there. If it is not, that is reported as the same gap at
  the manifold layer, with no change made, because those probes do not build `KillingChart`.

***The prediction.***
- `kh_lemma_killing`, `kh_cor_stationary` and the other copied theorems take a `KillingChart` as input and never
  construct one, so they re-check unchanged.
- The witness discharges `nondeg` with `kw_lightCone_det` (`det = −1`).
- `kw_zero_rigidity` can no longer be stated. It becomes `kw_zero_excluded`: no `KillingChart` has `g ≡ 0` when
  `n + 1 ≥ 1`.
- **Failable.** If a theorem breaks, RESULT names it and why. A theorem that needed the degenerate case was not about
  P1's setting.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

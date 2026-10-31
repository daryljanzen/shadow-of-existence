# `r7641+71.6` — RESULT: campaign 79, `r7641` ③, slice tangency. **The registered answer stands: P1's directional-tangency clause does not follow from its hypotheses.** A model satisfying every repaired hypothesis with `𝓗⁺ ≠ ∅` is BUILT, the failing sequence in it is BUILT, and the null-frame reduction is BUILT. ⌗ `977` lines in one probe (about `800` new, band 300–3000 new). ⌗ p: model `0.45`, failure `0.6`, reduction `0.5`: all came true; the paper counterexample `0.7` awaits 69's reading

*Against `PREDICTION.md` (`r7641+71.4`). 71 re-ran `lake env lean probes/SliceTangency.lean`. It exits 0 with no
errors. All `8` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`. The forbidden-token grep is clean.
The probe uses the repaired `IsTemporal`, with definitions identical to campaign 78's. One
`synthInstance.maxHeartbeats` option sits inside `namespace Model`.*

## The model — BUILT (`Model.st_model`, `Model.st_futCauchy`, `Model.GoodG.st_adapted`)

***The setting.***
- 2D Minkowski in null coordinates `(U, V)`, with `g = −dU dV` and `T = ∂_t`.
- `J` is the Rindler worldline `O σ = (−e^{−σ}, e^σ)`.
- `D = {U < 0}`, `𝓗⁺ = {U = 0}`, and `(0,0) ∈ 𝓗⁺`.
- `hOD`, `hmono`, `hcl`, `hint` and `𝓗⁺ ⊆ M` all hold.

***The Cauchy property.*** For every `G` that is C¹ and decreasing on `(0,∞)`, with `G → +∞` at `0⁺` and `→ −∞` at `∞`,
`Θ_G = G(−U) + V` is future-Cauchy temporal on `D`. This is proved in full: `U` and `V` are monotone along piecewise-C¹
causal curves, a bounded curve converges inside `D`, and the intermediate value theorem gives the level.

***Adaptation.*** It holds after reparametrising `O`.

***Consequence.*** **Every hypothesis of the repaired `cp_causal_alignment` is satisfiable with `𝓗⁺ ≠ ∅`.** This is
the non-vacuity check that campaigns 74 and 75 lacked.

## The failure — BUILT (`Model.st_tangency_fails`)

***The function.*** `Θf = F(−U) + V`, with `F(s) = −log s − sin(log s) − s`.
- It is future-Cauchy temporal and adapted.
- At `x_m = (−e^{−(2m+1)π}, 0)`:
  - `x_m → (0,0) ∈ 𝓗⁺`, and `Θf(x_m) → ∞`;
  - `dΘf(x_m) = dU + dV`;
  - `dΘf(ℓ)/‖dΘf‖ = 1/2`, which does not tend to `0`;
  - `dΘf(ℓ)/dΘf(n)` does not tend to `0` along `𝓝[D] (0,0)`.

***The aligned contrast.*** `Model.st_aligned`: `Θ₀ = −log(−U) + V` satisfies the same hypotheses, and its ratio
`dΘ₀(ℓ)/dΘ₀(n) = −U/2 → 0` at every horizon point.

## The reduction — BUILT (`st_null_frame_bound`, `st_alignment_iff`, `st_frame_cone_model`)

- **The bound.** In null-frame components, positivity on the causal cone gives `0 < a`, `0 < b` and `Σc_i² < 2ab`.
- **The equivalence.** Hence full alignment `⇔ a/b → 0`.
- **Not vacuous.** It is instantiated in the model.
- **The encoding.** The covector is given by its frame components, and the frame is not built from a general `g`.

## The answer for 69

- **The clause fails in general.** P1's "tangent hyperplanes of `S_τ` become asymptotically tangent to the generators,
  `∇Θ` aligning with the generator" fails for some adapted Cauchy temporal `Θ`, with the counterexample built in Lean
  in the model.
- **On paper, in P1's setting.** `PREDICTION.md` constructs the same failure in the Oppenheimer–Snyder exterior near a
  late horizon point.
- **What restores it.** The clause holds iff `dΘ(ℓ)/dΘ(n) → 0`. A sufficient condition is `dΘ(ℓ)` bounded and
  `dΘ(n) → ∞`, which P1's stationary and retarded slicings both satisfy.
- **The gap in the proof.** P1's proof step "`S_τ` meets `∂J⁻(O(τ))` transversely" does not control the tangent planes
  of `S_τ` elsewhere.
- **Suggested amendment.** State the tangency clause for slicings satisfying the condition, or for the two worked
  slicings. The accumulation clause, `KLi = KLs = 𝓗⁺`, stays general.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

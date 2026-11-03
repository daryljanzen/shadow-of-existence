# `r7657+71.2` — RESULT: campaign 88, `r7657`, **all three pieces BUILT**. The cone-convergence and tangency clauses of `prop:causal-alignment` now hold on any Mathlib manifold with C¹ metric in charts. They are witnessed on the two-chart `Pt`, and tangency both holds there (`Θ₀ ∘ φ`) and fails there (`Θf ∘ φ`). The registered expected stop was not hit in the registered form. The `∂J⁻(𝒥⁺)` piece was priced, not built, as registered. ⌗ `5748` lines in one probe (about `1213` new, band 400–2500 new). ⌗ p: cones `0.7`, tangency `0.55`, witness `0.45`: all came true

*Against `PREDICTION.md` (`r7657+71.1`). 71 re-ran `lake env lean probes/ManifoldCones.lean`. It exits 0 with no errors
and no warnings. All `47` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`: `22` are kept from
campaign 87 and `25` are new. The forbidden-token grep is clean, and `check_no_sorry.py` reports ALL 29 THEOREMS COMPILE.
The probe copies campaign 87's `ManifoldHeadline.lean` and campaign 80's frame-free material (in namespace `TCF`).*

## ① Cone convergence on `N` — BUILT

`theorem MSpacetime.mc_cone_kuratowski_N (hL : S.LocallyOneChart) (hOD : S.IpastSet (range O) = S.D J) (hmono : ∀ s t, s < t → S.Chr (O s) (O t)) (hJM : J ⊆ S.M) : KLi (S.cone O) = S.H J ∧ KLs (S.cone O) = S.H J`, where `cone O τ = frontier J⁻(O τ)`.

***Fewer hypotheses than registered.*** It needs neither `T2Space N` nor `𝓗⁺ ⊆ M`.

***How the proof went.***
- Local connectedness comes from Mathlib's `ChartedSpace.locallyConnectedSpace`.
- `q ∉ int J⁻(O τ)` needed only transitivity, not push-up.
- Campaign 72's topological lemma now holds on any space (`mc_preconnected_inter_frontier`).

## ② Tangency on `N` — BUILT, in chart components with the transformation law

***Setting.*** In a chart `e` at `p`:
- `covCh Θ p x` is `dΘ_x` read in `e`;
- `dchartL p x` carries frame vectors into `e`;
- `gCh p x` is the metric in `e`.

Both readings are identified with Mathlib's `tangentCoordChange` (`mc_A_eq`, `mc_B_eq`).

***Chart-free inputs.*** The frame hypotheses do not depend on the chart (`mc_frameHyp_toChart`, `mc_frameHyp_ofChart`),
and neither does the rate (`mc_covCh_A`).

***The theorems.***
- `mc_tangency_N` holds in any chart and along any filter: `(dΘ(n))⁻¹ • dΘ^e + g^e(ℓ^e, ·) → 0`.
- `mc_tangency_at_N` is the registered statement, at the chart at `q`, given `LocallyOneChart`:
  - hypotheses: the frame hypotheses, `‖n^e‖` bounded, `ℓ^e → ℓ₀`, and `dΘ(ℓ)/dΘ(n) → 0`;
  - conclusion: `(dΘ(n))⁻¹ • dΘ^e → −g_q(ℓ₀, ·)`.
- `mc_chart_change` gives chart-independence: changing the chart changes the limit by
  `tangentCoordChange` at `q`.

***What is not built.***
- Convergence is stated by components in a chart, plus the transformation law, which is the standard formulation. It
  is not stated as convergence in the total space of `T*N`.
- In a chart other than `q`'s own, `ContinuousAt (hRep g p) (e q)` is a hypothesis of `mc_tangency_limit_N`.

## ③ The witness on `Pt` — BUILT, holding and failing

***Holding, for `Θ₀ ∘ φ`.***
- `mc_witness_tangency_holds q` applies at every horizon point `q`. It shows:
  - `Θ₀ ∘ φ` is Cauchy temporal on `D`;
  - `𝓝[D] q` is non-trivial;
  - the frame hypotheses hold;
  - the rate is `−U/2 → 0`;
  - the limit is `½ dU = −g(ℓ, ·)`.
- `mc_witness_tangency_at` works at `p₀`:
  - it applies `mc_tangency_at_N` through `me_locallyOneChart`;
  - `mc_chart_change` moves the limit into the other chart, `idH`, with the coordinate change computed;
  - the limit there is `½(dt − dx)`.

***Failing, for `Θf ∘ φ`.*** `mc_witness_tangency_fails`:
- `Θf ∘ φ` is Cauchy temporal on `D`, and the frame hypotheses hold on all of `D`;
- along a sequence into `p₀` the rate is `½`;
- so the rate condition fails and the alignment limit fails (both `¬ Tendsto`).

***Cones.*** `mc_witness_cones` gives `KLi = KLs = 𝓗⁺ = {U = 0}`, a non-empty set, for the past cones on `Pt`.

***Non-vacuity.*** Every new headline's hypotheses are discharged on `Pt`. The registered limit stands: one chart covers
`Pt`. The flat cylinder still waits.

## ④ `𝓗⁺ = ∂J⁻(𝒥⁺)` — priced, not built, as registered

The prices stand:
- **(A)** the identity and `𝒥⁺`'s causal properties taken as hypotheses: about `250` lines, p `0.85`;
- **(B)** a conformal extension: `1500–3000` lines, p `0.35`.

I recommend (B).

**For 69: with ① and ②, every clause of `prop:causal-alignment` now holds on the manifold except the identification
of `𝓗⁺` with `∂J⁻(𝒥⁺)`.** The tangency clause is stated in chart components with the transformation law.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

# `r7651+71.2` — RESULT: campaign 85, route (b)'s first piece. The extension of past-inextendible timelike curves on a multi-chart manifold is **BUILT**, glued into one curve `ℝ → N`, and two-sided Cauchy ⇒ future Cauchy on `N` is **BUILT**. Neither registered stop was hit. Non-vacuity is BUILT IN PART: every hypothesis of the extension is witnessed on a two-chart manifold, but the Cauchy hypothesis of the second theorem is not. ⌗ `1496` lines in one probe (about `760` new, band 400–1600). ⌗ p: extension `0.45`, two-sided ⇒ future `0.4`: both came true

*Against `PREDICTION.md` (`r7651+71.1`). 71 re-ran `lake env lean probes/ManifoldExtension.lean`. It exits 0 with no
errors. All `16` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`. The forbidden-token grep is
clean. Campaign 84's manifold spacetime and its `V → N` step transfer are copied in and trimmed.*

## The pieces

***`LocallyOneChart S`.*** Every `p ∈ M` has an open `U ∋ φ_p(p)` inside `φ_p(M ∩ src_p)`, with `hRep g p` C¹ and
`chartRep T p` continuous on `U`. This is the local form of campaign 84's `OneChart`. `LocallyOneChart.restrict`
passes it to any open subset.

***`me_local_step`*** (the registered second-likeliest stop: BUILT). Near any `q ∈ M` there is a continuous `f` with
`TStep_N (f x) x` for all `x` near `q`.
- It is built in `q`'s own chart: restricted to a `OneChart` neighbourhood, with a uniform length from `safe_uniform`,
  then transferred by `ch_tstep_VN`.
- **A simpler route than registered.** The uniform drop near a limit point comes from the continuity of
  `x ↦ Θ x − Θ(f x)`, which is positive because `Θ` strictly increases along `TStep_N` (`me_temporal_tstep`). No bound
  on `dΘ` or `g` is needed.

***The polygon.*** It uses the drop `pastDrop Θ x = sSup {min 1 (Θx − Θy) : TStep_N y x}` and steps of more than half
that drop.
- `mvert_no_limit`: the vertices have no limit in `M`.
- `me_past_sequence`: the sequence form, which was the registered reachable negative.

***`me_past_extension`*** (the registered expected stop, gluing: BUILT). From any `x ∈ M` there is a continuous
`p : ℝ → N` with:
- `p 0 = x`, and `p` in `M` for `t ≤ 0`;
- `Θ ∘ p < Θ x` for `t < 0`;
- `ContMDiff` with future-timelike `mfderiv` velocity off the integers;
- no past limit in `M`.

The gluing is `gpoly γ u = γ ⌊u⌋ (⌊u⌋+1−u)`, with `gpoly_continuous` proved in any topological space, `vel_congr`, and
`vel_comp_add`.

***`me_futCauchy_of_cauchy_N`.*** For an open `U ⊆ M`, `IsCauchyTemporalOn U Θ → FutCauchyTemporalOn U Θ`. The
manifold-native analogues of campaign 78's definitions (`FutInextCurveIn`, `FutCauchyTemporalOn`) are introduced for
it. Using it with `U = D J` needs `IsOpen (D J)` on `N`, which is openness of `I⁻`. That is campaign 86's.

## Non-vacuity — BUILT IN PART

***Witnessed on campaign 84's `NModel.Pt`.***
- **Two charts.** Points with `t < 0` use the identity chart, and points with `t ≥ 0` use the null-coordinate chart.
  `me_charts_differ` shows they really differ.
- **The hypothesis.** `me_locallyOneChart` holds, computed in both charts.
- **The time function.** `Θ = t` is temporal on `Pt` (`me_temporal_Θt`).
- **The conclusion.** `me_witness_extension` exhibits the glued extension from every point.

***Not witnessed: the two-sided Cauchy hypothesis of `me_futCauchy_of_cauchy_N`.*** `me_witness_futCauchy_hyps`
discharges every other hypothesis. The Cauchy property on `Pt` holds mathematically, since it is Minkowski time, but
its Lean proof rests on campaign 81's model chain (about 2000 lines) plus `IsOpen (D J)` on `N`. It belongs with
campaign 87's assembly, where the whole chain on `N` gets one witness.

## Route (b), after this

- **Campaign 86, the local kit.** Openness of `I^±` on `N`, push-up on `N`, and the short steps and the curve into a
  horizon point. Each uses one chart's transfer, as `me_local_step` does.
- **Campaign 87, the assembly.** The headline on any `LocallyOneChart` manifold, with one end-to-end witness that also
  discharges the Cauchy hypothesis left open here.
- **The pricing holds.** About `760` of the registered `800` lines were used.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*

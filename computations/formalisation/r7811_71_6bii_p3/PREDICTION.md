# `r7811+71.1` — PRE-REGISTRATION: 6b-ii, **phase 3: inextendibility and non-imprisonment under a temporal function, and the global limit curve (phase 2's K6)**. ⌗ `1200` new lines (band 800–1700), p(T1–T5 and T8 all BUILT) `0.45`

*Registered before any Lean. The plan is `../r7807_71_6bii/PLAN.md`; phase 3 was re-priced at `r7809+71.2` to 800–1700
lines and p 0.35 when it absorbed phase 2's K6. The probe is the new standalone `probes/TemporalCurves.lean` (`tc3_`).
It imports only Mathlib and carries verbatim copies (not counted) of the kit blocks it needs: the chart `Spacetime`
with `restrict` and `IsTemporal` from `probes/GeneratorStretch.lean`, and, for T7, phase 2's manifold blocks.*

**Why `Θ` and not `τ₀`.** Phase 2 parametrised chains by a chart-linear `τ₀` that is good only near one point. A global
curve needs one parameter everywhere, so phase 3 parametrises by the **temporal function** `Θ` itself (the kit's
`IsTemporal`: `C¹` on `M`, with `dΘ` positive on future-causal vectors). This is the "global temporal function on `M`"
that r7669 named and the plan put here.

**Setting.** `V` is finite-dimensional, `S : Spacetime V`, and `Θ` is temporal for `S`. A curve `c` on an interval is
**`Θ`-parametrised** if `Θ (c s) = Θ (c a) + (s − a)`. It is **locally `Θ`-Lipschitz** if every `x₀ ∈ M` has `r, k > 0`
such that `‖c t − c s‖ ≤ k (Θ(c t) − Θ(c s))` whenever `s ≤ t` and `c([s, t]) ⊆ ball x₀ r`.

| Row | Statement | Lines | p | Note |
|---|---|---|---|---|
| T1 | **The temporal cone lemma.** For `x₀ ∈ M` there are `r, c > 0` with `ball x₀ r ⊆ M` such that `c‖v‖ ≤ dΘ_x(v)` for every future-causal `v` at every `x ∈ ball x₀ r`. The same compactness argument as phase 2's K1, with `dΘ` (continuous since `Θ` is `C¹`) in place of `τ₀`, and `dΘ_{x₀} > 0` on the causal cone | 80–150 | 0.8 | |
| T2 | **Chains rise in `Θ` by at least their displacement.** Arcs and chains of `S.restrict (ball x₀ r)` satisfy `c‖y − x‖ ≤ Θ y − Θ x` (the boundary-function mean-value inequality, as in K2) | 60–130 | 0.8 | |
| T3 | **`Θ`-parametrisation of chains.** A restricted chain from `x` gives a `Θ`-parametrised curve on `[Θ x, Θ y]` from `x` to `y`, with values in the ball and the T2 bound between any two of its parameters | 120–250 | 0.65 | Phase 2's `invFunOn`-and-concatenate construction, with `Θ ∘ γ` in place of `τ₀ ∘ γ` |
| T4 | **The local limit for `Θ`-parametrised curves.** Arzelà–Ascoli for uniformly Lipschitz families valued in a compact ball, stated once in general. Pointwise limits keep the `Θ`-parametrisation and the local `Θ`-Lipschitz bound | 150–300 | 0.6 | |
| T5 | **Non-imprisonment.** A `Θ`-parametrised, locally `Θ`-Lipschitz curve `c` on `[0, T)` with values in `M` either has a limit in `M` as `t → T` (it is extendible), or **eventually leaves every compact `K ⊆ M`**. If `T = ∞` the second case always holds, since `Θ` is bounded on `K` | 150–300 | 0.5 | Partial imprisonment is excluded by the uniform Lipschitz bound near an accumulation point: the curve stays in a ball and is Cauchy |
| T6 | **The global limit curve (phase 2's K6), in a chart.** Chains from `xₙ → p` whose `Θ`-rise tends to `∞` have a diagonal subsequence whose `Θ`-parametrisations converge, locally uniformly on `[0, T*)`, to a `Θ`-parametrised, locally `Θ`-Lipschitz curve from `p`. Either `T* = ∞`, or the curve leaves every compact of `M` as `t → T*` (by T5) | 250–500 | 0.25 | **The expected stop.** The diagonal over a compact exhaustion of `M`, with exit times varying in `n`, is the part I trust least. If it does not close, I report the exact missing step |
| T7 | **On `N` under `OneChart`.** T5 and T6 transported, as K5 transported K4 | 100–250 | 0.35 | Under `LocallyOneChart` (several charts) the patching is not attempted in this phase |
| T8 | **Non-vacuity.** The 2D Minkowski chart with `Θ(t, x) = t`: chains to which T1–T5 apply, and a curve running off to `T = ∞` | 50–120 | 0.75 | |

**Mathlib.** I expect no gap. Arzelà–Ascoli, compact exhaustion (`CompactExhaustion`), and the mean-value and
intermediate-value theorems are all there.

**Not in this phase:** the achronal-boundary argument (4), `HasFutureGenerators` (5), and multi-chart patching under
`LocallyOneChart`. P1's 6b-ii stays BUILT IN PART.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

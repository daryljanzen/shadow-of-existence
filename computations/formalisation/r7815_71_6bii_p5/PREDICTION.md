# `r7815+71.1` — PRE-REGISTRATION: 6b-ii, **phase 5: landing in the generator hypothesis by route (b), with compacts of `M` (69's ∂M ruling), reparametrised to `[0, ∞)` and transported to `N`**. ⌗ `900` new lines (band 600–1500), p(V1–V4 BUILT) `0.6`, p(all of V1–V7) `0.3`

*Registered before any Lean. The plan is `../r7807_71_6bii/PLAN.md` (phase 5(b): 300–700 lines, p 0.6). This
registration prices higher because the order adds three things to (b): the ∂M ruling, the reparametrisation and the
transport to `N`. The probe is the new standalone `probes/Generators.lean` (`g5_`). It imports only Mathlib and carries
verbatim copies (not counted) of all of `probes/GeneratorStretch.lean` (the kit, with `HasFutureGenerators`,
`hs_stretch_N` and `gs_future_stretch`) and all of `probes/PushUp.lean` (phases 3 and 4). Those two files live in
different namespaces (`GeneratorStretchProbe`, `TemporalCurvesProbe`), so the copies do not clash.*

## The ruling, as I will state it

- **The target.** Here `M` is the spacetime and `N` is only the manifold its chart lives on. The restated hypothesis
  `HasFutureGeneratorsM S J` asks, for every `q ∈ 𝓗⁺ ∩ M`, for a curve `γ` with:
  - `γ 0 = q`;
  - `γ` continuous on `[0, ∞)`;
  - `γ t ∈ 𝓗⁺ ∧ γ t ∈ closure J⁺(q)` for `t ≥ 0` (route (b));
  - `γ` eventually outside every compact `K ⊆ M`.
- **`q ∈ M` is disclosed as an addition.** A horizon point outside `M` has no spacetime through it to generate from.
  When `M = N` it is vacuous.
- **The old hypothesis implies the new one.** `HasFutureGenerators` gives `HasFutureGeneratorsM`, since `J⁺(q)` lies
  in its closure and `cocompact N` contains the complement of every compact `K ⊆ M`.
- **When `M = N` the escape clauses coincide.**

| Row | Statement | Lines | p | Note |
|---|---|---|---|---|
| V1 | **The bridge.** Field-by-field maps from the kit's `Spacetime` and `MSpacetime` to phase 4's copies. Under them `Chr`, `Cau`, `D`, `H`, `IsTemporal`, `IsTemporalOn`, `OneChart` and local Lipschitz continuity agree, by unfolding | 80–200 | 0.75 | The copies are textually identical, so each agreement should be `Iff.rfl`. The risk is elaboration time |
| V2 | **The restated hypothesis.** `HasFutureGeneratorsM`. `HasFutureGenerators → HasFutureGeneratorsM`. With `S.M = univ`, escape from compacts of `M` is equivalent to `Tendsto γ atTop (cocompact N)` | 60–150 | 0.8 | |
| V3 | **The restated stretch.** `g5_future_stretch`, under `hs_stretch_N`'s hypotheses and `HasFutureGeneratorsM`: for `q ∈ 𝓗⁺ ∩ M`, `ε > 0` and compact `K ⊆ M`, eventually the `ε`-stretch has a point in `closure J⁺(q)` outside `K`. With `M = N` the side condition `K ⊆ M` drops | 40–120 | 0.8 | Route as `gs_future_stretch`: the segment lemma needs only `γ t ∈ 𝓗⁺` |
| V4 | **The reparametrisation.** From phase 4's dichotomy (curves on every `[0, Tⱼ]`, with `Tⱼ → ∞` or `Tⱼ → T* < ∞`) to a curve continuous on `[0, ∞)` that keeps the pointwise properties and escapes compacts of `M` along `atTop`. The bounded case uses `s ↦ T* s / (1 + s)` | 100–250 | 0.65 | |
| V5 | **The transport to `N`** under `OneChart p₀`. The chart hypotheses come from those on `N`: `hOD`, `hmono`, `Θ` temporal (`tc3_temporal_NV`), local Lipschitz continuity (`ch_chart_lipschitz`), and `q ∈ 𝓗⁺ ∩ M`. The curve is pulled back by `φ⁻¹`, and `𝓗⁺` (`ch_mem_H_iff`), the closure of `I⁺(q) ∪ {q}` (`ch_mem_closure_iff`, `ch_chr_iff`) and escape from compacts of `M` are carried back | 200–450 | 0.45 | **The expected stop.** Transporting `hOD` (`I⁻(range O) = D J` in the chart) is the step I trust least |
| V6 | **The landing.** Under `OneChart p₀`, finite dimension, `J ⊆ M`, `hOD`, `hmono`, a temporal `Θ` on `M` with `Θ ∘ O → ∞`, and `g` (read in the chart) locally Lipschitz: `HasFutureGeneratorsM S J`. With V3, the stretch statement then holds without assuming generators | 60–150 | 0.4 | |
| V7 | **Non-vacuity and the existing uses.** The four-dimensional witness (`M = N`) meets `HasFutureGeneratorsM`, through V2 from `gs_hasFutureGenerators`. A one-chart instance of V6's hypotheses with `𝓗⁺ ≠ ∅` is attempted. Every existing use of `HasFutureGenerators` is reported as falling in the `M = N` case or not | 80–200 | 0.45 | If the 4D witness's `Θ ∘ O → ∞` cannot be shown cheaply, I report that and give the weaker witness |

**Mathlib.** No gap is expected. The steps are topology (closures and frontiers through a partial homeomorphism),
compactness, and an explicit homeomorphism `[0, ∞) → [0, T*)`. The risk is bookkeeping and the cost of the
cross-namespace bridge, not missing library material.

**Not in this phase:**
- the multi-chart `LocallyOneChart`, beyond what V6 uses through `OneChart`;
- route (a), `Cau`-reachability.

P1's 6b-ii stays BUILT IN PART until 69 rules on whether the restated target closes the row.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

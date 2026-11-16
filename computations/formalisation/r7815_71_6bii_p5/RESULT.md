# `r7815+71.2` — RESULT: 6b-ii, **phase 5 BUILT WHOLE: `HasFutureGeneratorsM` (route (b), compacts of `M`) is proved under `OneChart`, not assumed, and the stretch statement follows from the landing's hypotheses (V1–V7).** ⌗ `458` new lines (band 600–1500, estimate 900, **under the band by 142**), at p `0.3` for all of V1–V7

*The registration is `PREDICTION.md`, the plan is `../r7807_71_6bii/PLAN.md`, and the ∂M ruling is 69's (`r7815`).
The probe is the new standalone file `probes/Generators.lean` (`g5_`): 10948 lines, of which 10490 are verbatim
copies and 458 are new.*

## Verification
- `lake env lean probes/Generators.lean` gives **0 errors and 0 warnings**.
- **111 axiom lines**, every one `[propext, Classical.choice, Quot.sound]`.
  - 11 are new.
  - 100 are the copies' own lines, carried unchanged.
  - The `rfl`/`Iff.rfl` bridge lemmas are not printed, since they depend on no axioms.
- The forbidden-token grep is clean, the only import is `Mathlib`, and `check_no_sorry.py` reports ALL 29.
- **The copies are byte-identical** (checked by substring):
  - `probes/GeneratorStretch.lean` l.2–6573: all of it after the import.
  - `probes/PushUp.lean` l.2–3917: all of it after the import.
  - The two live in different namespaces (`GeneratorStretchProbe` and `TemporalCurvesProbe`), so they do not clash.
- **Options.** The new code sets one, twice: `set_option linter.unusedSectionVars false`, in its two manifold
  sections. This is the kit's own convention for every manifold section (`GeneratorStretch.lean` l.2779, 5258, 6215,
  6361), and it is a linter switch only. Without it, the linter flags the unused `[IsManifold 𝓘(ℝ, E) 1 N]` section
  variable. The copies carry their own options unchanged, among them phase 4's `maxHeartbeats` on `pu4_poly`.
- **How it was built.** For speed during development, the two copies were compiled once as a temporary library
  module, and the new code was checked against it. The module was not committed. The verdict above is from the
  standalone file.

## The ruling, as built

**`HasFutureGeneratorsM S J`.** For every `q ∈ 𝓗⁺` with `q ∈ M` there is a curve `γ` with:
- `γ 0 = q`;
- `γ` continuous on `[0, ∞)`;
- `γ t ∈ 𝓗⁺ ∧ γ t ∈ closure J⁺(q)` for every `t ≥ 0` (route (b));
- `γ` eventually outside every compact `K ⊆ M` (69's ruling: `M` is the spacetime, and running into ∂M in finite
  `Θ`-time is leaving it).

**What it adds beyond the order.** The hypothesis asks only about horizon points in `M`, as registered: there is no
spacetime through a horizon point outside `M`. When `M = N` this is vacuous.

## Rows

| Row | Statement (Lean) | Mark |
|---|---|---|
| V1 | `Spacetime.g5_tc` and `MSpacetime.g5_tc` are field-by-field bridges to phase 4's copies. Under them `Chr`, `Cau`, `I⁻`, `D`, `𝓗⁺`, `IsTemporal` and `IsTemporalOn` agree by `Iff.rfl`/`rfl`. `g5_oneChart` carries `OneChart`, and `g5_chartSp` shows the two chart spacetimes are equal by `rfl` | **BUILT** |
| V2 | `HasFutureGeneratorsM`. `g5_hasFutureGeneratorsM`: the old `HasFutureGenerators` implies it. `g5_cocompact_iff`: when `S.M = univ`, escape from the compacts of `M` is equivalent to `Tendsto γ atTop (cocompact N)` | **BUILT** |
| V3 | `g5_future_stretch` holds under `hs_stretch_N`'s hypotheses and `HasFutureGeneratorsM`: for `q ∈ 𝓗⁺ ∩ M`, `ε > 0` and compact `K ⊆ M`, eventually the `ε`-stretch has a point of `closure J⁺(q)` outside `K`. `g5_future_stretch_univ`: when `M = N`, the side conditions drop | **BUILT** |
| V4 | `g5_reparam`: phase 4's dichotomy (every `[0, Tⱼ]`, with `Tⱼ → ∞` or `Tⱼ ↑ T*`) gives a curve continuous on `[0, ∞)` with the same pointwise property, escaping along `atTop`. In the bounded case the curve is `c ∘ σ` with `σ s = T* − T*/(1 + s)` | **BUILT** |
| V5 | Inside `g5_generators`, the chart hypotheses are derived from those on `N`: `hOD` through `ch_mem_chartD_iff` on both sides, `hmono` through `ch_chr_iff`, `Θ` temporal through phase 3's `tc3_temporal_NV`, Lipschitz `g` through `ch_chart_lipschitz`, and `q ∈ 𝓗⁺ ∩ M` through `ch_mem_H_iff`. The curve is pulled back by `φ⁻¹`. `𝓗⁺` comes back through `ch_mem_H_iff`. `closure (I⁺(q) ∪ {q}) ⊆ closure J⁺(q)` comes back through `ch_mem_closure_iff` with `ch_chr_iff` and injectivity on the source. Escape from the compacts of `M` comes back through their compact chart images | **BUILT** |
| V6 | `g5_generators`: under `OneChart p₀`, finite dimension, `J ⊆ M`, `hOD`, `hmono`, and a temporal `Θ` on `M` with `Θ ∘ O → ∞`, `HasFutureGeneratorsM S J` holds. `g5_future_stretch_landed`: with `LocallyOneChart` and a metric, the stretch statement holds **without assuming generators** | **BUILT** |
| V7 | `FourD.g5_witness` uses the four-dimensional witness: `M = N`, one chart (`g5_oneChart`), `W = U + V` temporal (`g5_W_temporal`), and `W ∘ O → ∞` (`g5_W_O`: `W ≥ τ/2 − 1` once `τ ≥ 1`). There `𝓗⁺ = {U = 0} ≠ ∅`, and `g5_generators` gives `HasFutureGeneratorsM`. `FourD.g5_origin` is a generator from the origin, in `𝓗⁺ ∩ closure J⁺(0)` and continuous on `[0, ∞)`, that leaves every compact set of `N`. `FourD.g5_hasFutureGeneratorsM_old` also gets there from the kit's own generators, through V2 | **BUILT** |

## The existing uses of `HasFutureGenerators` (the order's last request)

All are in `probes/GeneratorStretch.lean`. No other file uses it.
- **`gs_segment_stretch` and `gs_future_stretch`** are general statements that take the hypothesis.
  `g5_future_stretch` restates the latter.
- **`FourD.gs_hasFutureGenerators` and `FourD.gs_witness`** fall in the **`M = N` case** (`fd_S.M = univ`,
  `g5_M_univ`). There the escape clauses coincide (`g5_cocompact_iff`), and the only remaining difference is
  `Cau` against its closure, which is route (b) itself.
- **No existing use has `M ≠ N`.** The cylinder and the other witnesses named in the kit's header are not in that
  file and do not use the hypothesis.

## Against the registration

- **All seven rows are built.** The registered joint event for V1–V4 (p 0.6) held, and so did all of V1–V7
  (p 0.3).
- **The named stop (V5, p 0.45) did not hold.** Transporting `hOD` was two applications of the kit's
  `ch_mem_chartD_iff` (with `range (φ ∘ O) = φ '' range O`), not the obstacle I had feared.
- **The cross-namespace bridge cost nothing.** The two copies' definitions are textually identical, so every
  agreement is `rfl`, including equality of the chart spacetimes.
- **Size: 458 new lines, under the band (600–1500, estimate 900).** The bridge, the transport of `hOD` and the
  witness's temporal function were each far shorter than priced.

**Mathlib gap: none found.** The order said to stop at the first gap Mathlib cannot cross and state it exactly.
There was none. Everything used is in Mathlib:
- closures and frontiers through a partial homeomorphism (the kit's `ch_` lemmas, on `extChartAt`);
- images of compacts (`IsCompact.image_of_continuousOn`);
- `ContinuousWithinAt.mono_of_mem_nhdsWithin` and `ContinuousWithinAt.comp` for the reparametrisation;
- `mfderiv_eq_fderiv` for the witness.

## Where 6b-ii stands

- **What the kit now proves.** Under one chart, the generator hypothesis is a theorem in route (b) form (closure of
  `J⁺(q)`, compacts of `M`, from points of `𝓗⁺ ∩ M`), and the stretch statement follows from the landing's
  hypotheses alone.
- **What is not built:**
  - **Route (a)**, `Cau q (γ t)` itself rather than its closure. That is the equality of Lipschitz-causal and
    piecewise-`C¹`-causal reachability, which the plan priced at 1500–3000 lines and p 0.2.
  - **The multi-chart `LocallyOneChart`** in place of `OneChart`, for the landing (V5 and V6). `g5_future_stretch`
    already takes `LocallyOneChart`, as `gs_future_stretch` did.
- **For 69 to rule:** whether route (b) under `OneChart` closes P1's 6b-ii row, or whether the row also needs either
  of these. Until then the standing stays **BUILT IN PART**.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

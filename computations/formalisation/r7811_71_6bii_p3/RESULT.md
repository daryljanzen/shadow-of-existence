# `r7811+71.2` — RESULT: 6b-ii, **phase 3 BUILT WHOLE: all eight rows (T1–T8), including T6, the global limit curve (phase 2's K6), which was the registered stop**. ⌗ `1368` new lines (band 800–1700, estimate 1200), at p `0.45` (T6 itself at p `0.25`)

*The registration is `PREDICTION.md` and the plan `../r7807_71_6bii/PLAN.md`. The probe is the new standalone file
`probes/TemporalCurves.lean` (`tc3_`): 2042 lines, of which 674 are verbatim copies and 1368 are new.*

## Verification
- `lake env lean probes/TemporalCurves.lean` gives **0 errors and 0 warnings**.
- **12 axiom lines**, every one `[propext, Classical.choice, Quot.sound]`.
- The forbidden-token grep is clean, the only import is `Mathlib`, and `check_no_sorry.py` reports ALL 29.
- **The copies are byte-identical** (checked by substring):
  - `probes/GeneratorStretch.lean`:
    - l.499–534 and l.1020–1030: the chart `Spacetime` and `restrict`.
    - l.906–907: `IsTemporal`.
    - l.627–636: `futTimelike_smul`.
    - l.2363–2448: campaign 84's helpers.
    - l.2777–3278: the manifold kit through `ch_cau_iff`.
  - `probes/ConeCurves.lean` l.519–545: the Minkowski chart.
- **One option is set, inside a verbatim copy.** The manifold block carries the kit's own
  `set_option linter.unusedSectionVars false` (`GeneratorStretch.lean` l.2779).
- **A correction to phase 2's `RESULT.md`.** It said "no options are set", but `ConeCurves.lean` carries the same
  line in its copy of the same block. No new code in either file sets an option.

## The notion

Chains are parametrised by the temporal function `Θ` itself, rather than by phase 2's chart-linear `τ₀`.

- **A cone set** `(B, c)` (`tc3_ConeSet`): an open `B ⊆ M` with `c‖v‖ ≤ dΘ_x(v)` for every future-causal `v` at
  every `x ∈ B`.
- **A `Θ`-causal curve on `[a, b]`** (`tc3_Causal`):
  - continuous;
  - `Θ`-parametrised (`Θ(η s) = Θ(η a) + (s − a)`);
  - in `M`;
  - on every cone set `(B, c)`, each segment lying in `B` rises in `Θ` by at least `c` times its displacement.
- It is the Lipschitz-type causal notion the limit-curve theorem needs. It is closed under concatenation,
  restriction, shift and uniform limits.

## Rows

| Row | Statement (Lean) | Mark |
|---|---|---|
| T1 | `tc3_cone`: for `x₀ ∈ M` there are `r, c > 0` with `closedBall x₀ r ⊆ M` and `c‖v‖ ≤ dΘ_x(v)` for future-causal `v` at every `x ∈ ball x₀ r` | **BUILT** |
| T2 | `tc3_arc_bound` (arcs, by the one-sided boundary mean-value inequality); `tc3_cstep_arc`; `tc3_cau_bound`: `c‖y − x‖ ≤ Θ y − Θ x` along restricted chains | **BUILT** |
| T3 | `tc3_reparam`, `tc3_concat`, `tc3_chain` (restricted chains, as registered). Beyond the registration: `tc3_arc_causal`, `tc3_causal_concat` and `tc3_chain_causal` show that **every chain of `S` from `x ∈ M` is a `Θ`-causal curve**. Continuity of the reparametrisation comes from `Continuous.isClosedEmbedding` | **BUILT** |
| T4 | `tc3_AA`: Arzelà–Ascoli for uniformly Lipschitz families in a closed ball. `tc3_local_limit`: the local limit for restricted chains. `tc3_causal_limit`: uniform limits of `Θ`-causal curves with values in `M` are `Θ`-causal | **BUILT** |
| T5 | `tc3_nonimprison_top`: a `Θ`-parametrised curve on `[0, ∞)` eventually leaves every compact `K ⊆ M`. `tc3_nonimprison`: a continuous, `Θ`-parametrised, locally `Θ`-bounded curve on `[0, T)` with no limit in `M` at `T⁻` eventually leaves every compact `K ⊆ M`. Partial imprisonment is excluded by a first-exit argument and Cauchy completeness | **BUILT** |
| T6 | `tc3_step`, `tc3_global_limit` and `tc3_global_escape`; detailed after the table | **BUILT** |
| T7 | `tc3_temporal_NV`: a temporal `Θ` on `M ⊆ N` (`IsTemporalOn`) is temporal in the chart. `tc3_manifold_escape`: under `OneChart p₀`, chains of `N` with these hypotheses give a curve `c` in `M` from `p` that is continuous with `Θ(c s) = Θ p + s` on every `[0, Tⱼ]`, is the pointwise limit in `N` of pulled-back chain parametrisations, and eventually leaves every compact `K ⊆ M` (`t → ∞` or `t → T*⁻`) | **BUILT** |
| T8 | `tc3_witness`: the 2D Minkowski chart with `Θ = fst` (`tc3_mink_temporal`). The straight chains `0 → (n + 1, 0)` rise by `n + 1 → ∞`, so the global limit curve from `0` exists and leaves every compact set | **BUILT** |

**T6 in detail**, under these hypotheses:
- finite dimension;
- chains of `S` from `xₙ ∈ M`;
- `xₙ → p ∈ M`;
- `Θ`-rise tending to `∞`.

What it gives:
- **Parametrisations:** `Θ`-causal parametrisations `ηₙ` on `[0, Lₙ]`.
- **A subsequence and a limit:** a subsequence converging uniformly, on every `[0, Tⱼ]`, to one curve `γ` from `p`
  that is `Θ`-causal on every `[0, Tⱼ]`. Here `Tⱼ` is strictly increasing from `0`.
- **A dichotomy:** either `Tⱼ → ∞`, or `Tⱼ → T* < ∞` and `γ` has no limit in `M` at `T*⁻`.
- **`tc3_global_escape`** combines this with T5: in either case `γ` eventually leaves every compact `K ⊆ M`.

How it is proved:
- **The diagonal:** a diagonal over a `CompactExhaustion` of `M`, with step lengths fixed by uniform cone constants
  on each compact (`tc3_uniform_cone`).
- **Each step (`tc3_step`):** the stay lemma (`tc3_stay`, `tc3_stay_lip`), then Arzelà–Ascoli, then concatenation.
- **The dichotomy:** if `γ` converged in `M`, its endpoints would eventually lie in one compact, the steps would be
  bounded below, and `Tⱼ → ∞`.

**Against the registration:**
- **All eight rows are built.** The registered joint event (T1–T5 and T8, p 0.45) held.
- **The named stop (T6, p 0.25) did not hold.** The diagonal over the compact exhaustion closed directly:
  - the exhaustion itself is Mathlib's `CompactExhaustion.choice` on the subtype `M`;
  - its `find` index and `subset_interior_succ` give the lower bound on step lengths;
  - continuity of the chain parametrisations, which the stay lemma needs, comes from a closed embedding.
- **T7 (p 0.35) is built.** The temporal-function transport is the first half of the kit's own `ch_isCauchy_NV`,
  adapted.
- **Size:** 1368 new lines, inside the band (estimate 1200).

**Mathlib gap: none found.** The order said to stop at the first gap Mathlib cannot cross and state it exactly.
There was none.

**What phase 3 does not give** (needed later):
- **One chart only.** T7 is stated under `OneChart p₀`; the kit's multi-chart `LocallyOneChart` is not attempted, as
  registered.
- **Not `Cau`-reachability.** The limit curve is `Θ`-causal, a Lipschitz notion relative to `Θ`. That its points are
  in the closure of `J⁺(p)`, or `Cau`-reachable, is not proved. That is phase 4's push-up argument and phase 5's
  route choice.
- **The parameter domain.** The curve's domain is `[0, T*)` with `T* ≤ ∞`. `HasFutureGenerators` asks for
  `[0, ∞)` and `Tendsto γ atTop (cocompact N)`. When `T* < ∞`, an increasing homeomorphism `[0, ∞) → [0, T*)` turns
  T7's eventual escape into exactly that. This is phase 5 bookkeeping.
- **Phase 4 must supply the rise.** T6 needs the chains' `Θ`-rise to tend to `∞`, which is where "`J` at infinity"
  enters.

**Re-pricing the remaining phases:** unchanged. Phase 4 is 700–1500 lines at p 0.3. Phase 5(b) is 300–700 lines at
p 0.6.

**Standing of 6b-ii:** still BUILT IN PART: nothing lands in P1 until the row is whole.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

# `r7819+71.2` — RESULT: 6b-ii, **phase 6 BUILT WHOLE: `HasFutureGeneratorsM` is proved under `LocallyOneChart` (several charts), and the cone boundaries approach `𝓗⁺` monotonically (W1–W7).** ⌗ `1174` new lines (band 1800–4000, estimate 2800, **under the band by 626**), at p `0.2` for all of W1–W7

*The registration is `PREDICTION.md`, and the order is 69's `r7819`. The probe is the new standalone file
`probes/MultiChart.lean` (`m6_`): 12121 lines, of which 10947 are a verbatim copy and 1174 are new.*

## Verification
- `lake env lean probes/MultiChart.lean` gives **0 errors and 0 warnings**.
- **123 axiom lines**, every one `[propext, Classical.choice, Quot.sound]`. 12 are new, and 111 are the copy's own.
- The forbidden-token grep is clean, the only import is `Mathlib`, and `check_no_sorry.py` reports ALL 29.
- **The copy is byte-identical** (checked by substring): `probes/Generators.lean` l.2–10948, that is, all of it
  after the import. It holds the kit, phases 3 and 4, and phase 5.
- **Options.** The new code sets one option: `set_option linter.unusedSectionVars false`, the kit's convention for
  its manifold sections. It is a linter switch only.
- **How it was built.** During development the copy was compiled once as an uncommitted library module, and the new
  code was checked against it. The verdict above is from the standalone file.

## Monotonicity (W1)

| Statement (Lean) | What it says |
|---|---|
| `m6_Jpast_mono` | **The pasts nest.** `J⁻(O s) ⊆ J⁻(O t)` for `s ≤ t`, because `O s ≪ O t` |
| `m6_infDist_antitone` | For any metric and any point, the distance to `J⁻(O τ)` is antitone in `τ` |
| `m6_H_not_mem_Jpast` | Horizon points lie outside every `J⁻(O τ)`: push-up would put them in `D J` |
| `m6_infDist_frontier`, `m6_cone_antitone`, `m6_stretch_mono` | **The cone boundaries.** If the metric's balls are connected, the distance from a horizon point to the cone `∂J⁻(O τ)` equals its distance to `J⁻(O τ)`. So it is antitone in `τ`, and the stretch grows with `τ` |

**One hypothesis, disclosed as registered: connected metric balls.** It holds for normed metrics. Without it the
inclusions and the distance to the pasts are still monotone, but the distance to their boundaries need not be. That
is a fact about arbitrary metrics, not a Mathlib gap.

## The multi-chart landing (W2–W6)

**Hypotheses:**
- `LocallyOneChart`, finite dimension and `[T2Space N]`;
- `J ⊆ M`;
- the observer: `I⁻(range O) = D J`, and `O s ≪ O t` for `s < t`;
- a temporal `Θ` on `M` with `Θ ∘ O → ∞`.

**Under these, `m6_generators` proves `HasFutureGeneratorsM S J`.** `m6_future_stretch_landed` then gives the
stretch statement without assuming generators.

| Row | Statement (Lean) | Mark |
|---|---|---|
| W2 | `m6_cl_trans`: transitivity of `closure (I⁺(·) ∪ {·})` on `N` | **BUILT** |
| W3 | `m6_one`, `m6_trunc`, `m6_bound`, `m6_local`: the truncation and the local segment, detailed after the table | **BUILT** |
| W4 | `m6_Seg` (a segment), `m6_patch_cone`, `m6_unif_local`, `m6_unif_compact`. `m6_step`: a length function, positive at horizon points and bounded below on every compact of `M` (taken as half a supremum), with a segment of that length from each such point | **BUILT** |
| W5 | `m6_stay`, the stay lemma on `N`, detailed after the table | **BUILT** |
| W6 | `m6_ps`, `m6_Ts`, `m6_curve`: generic iteration and continuity of the concatenation. `m6_generators`, detailed after the table | **BUILT** |
| W7 | `FourD.m6_witness` is the four-dimensional witness: `𝓗⁺ ≠ ∅`, `HasFutureGeneratorsM` by `m6_generators`, and the stretch statement. `FourD.m6_witness_mono` is monotonicity there, with the native metric, whose balls are convex | **BUILT** |

**W3 in detail.**
- **`m6_one`, `m6_trunc` (the `N`-level truncation).** A timelike chain from a point of a patch-chart ball, up to a
  `Θ`-level within reach, stays in the patch. The proof is first exit on each step, with the chain bound `m6_bound`
  keeping the chart image inside `2ρ/3`.
- **`m6_local`, the local segment.** It is built from:
  - approximating points of `D J`, taken in the chart because `N` is not assumed first countable;
  - their chains to `O`, truncated in the patch;
  - phases 3 and 4 in the patch chart: `pu4_chain`, the stay lemma, Arzelà–Ascoli, the limit lemmas, and
    `pu4_closure` from every point of the curve;
  - the pull-back to `N`, where the curve lies in `𝓗⁺ ∩ closure (I⁺ ∪ {·})`.

**W5 in detail.** **`m6_stay`:** a point of `closure (I⁺(x₀) ∪ {x₀})` that rises little in `Θ` above `x₀` stays in
the patch, within chart distance `ΔΘ/c` of `x₀`.

**W6 in detail.** **`m6_generators`.** Iterate the segments and take the dichotomy:
- **If the total length is infinite,** `Θ = Θ(q) + t` leaves every compact.
- **If it is finite,** suppose the curve kept returning to a compact `K ⊆ M`. Then:
  - `K` has a cluster point `z`;
  - near `z`, the stay lemma keeps every later point in one compact chart ball;
  - there the segment lengths are bounded below, so the total length is infinite, a contradiction.

Finally `g5_reparam` reparametrises onto `[0, ∞)`.

## Against the registration

- **All seven rows are built.** The joint event for W1 (p 0.8) and for all of W1–W7 (p 0.2) both held.
- **The named stop, W5 (p 0.3), did not hold, and a disclosed change of method made it go away.**
  - **What was registered:** carry the cone bound across chart changes for limits of chains.
  - **What was built instead:** non-imprisonment reduces to the `N`-level truncation lemma W3 already needs, via
    `m6_stay` and the transitivity of `closure (I⁺ ∪ {·})`. No chart-change argument is needed.
- **One registered hypothesis turned out unnecessary: `SecondCountableTopology N`.** The step length is half a
  supremum of admissible lengths, bounded below on compacts by a finite subcover, so no compact exhaustion is used.
  Only `[T2Space N]` remains, for compact sets to be closed.
- **Size: 1174 new lines, under the band (1800–4000, estimate 2800).** Each local step reused phase 3 and 4's chart
  lemmas unchanged, and W5 collapsed into W3.

**Mathlib gap: none found.** The order said to stop at the first gap Mathlib cannot cross and state it exactly.
There was none. Everything used is in Mathlib:
- `IsCompact.exists_clusterPt`, `IsCompact.elim_nhds_subcover` and `clusterPt_iff_nonempty`;
- `csSup` and `csInf` (first exit);
- `ContinuousOn.union_of_isClosed`, `tendsto_atTop_ciSup` and `IsPreconnected` (W1(iv), through the kit's
  `mc_preconnected_inter_frontier`).

## Where 6b-ii stands

Both items 69 named are built:
- **the landing under `LocallyOneChart`** (`m6_generators`, with `m6_future_stretch_landed`);
- **"monotonically"** (`m6_Jpast_mono` through `m6_stretch_mono`, with connected balls for the boundaries).

By 69's ruling in `r7819`, the row moves to **BUILT** once these are confirmed. The landing's hypotheses are:
- the observer;
- a temporal `Θ` with `Θ ∘ O → ∞`;
- `[T2Space N]`;
- finite dimension.

The monotone approach of the boundaries uses connected metric balls. Route (a) was ruled unnecessary.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

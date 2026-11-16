# `r7812+71.2` — RESULT: 6b-ii, **phase 4 BUILT WHOLE: the rise from "`J` at infinity", and the limit curve from `p ∈ 𝓗⁺` lying in `𝓗⁺` and in `closure (I⁺(p) ∪ {p})` (U1–U8). The registered stop (U6) did not hold.** ⌗ `1549` new lines (band 1000–2200, estimate 1500), at p `0.6` (U6 at `0.3`, U7 at `0.25`)

*The registration is `PREDICTION.md` and the plan `../r7807_71_6bii/PLAN.md`. The probe is the new standalone file
`probes/PushUp.lean` (`pu4_`): 3917 lines, of which 2368 are verbatim copies and 1549 are new.*

## Verification
- `lake env lean probes/PushUp.lean` gives **0 errors and 0 warnings**.
- **11 axiom lines**, every one `[propext, Classical.choice, Quot.sound]`.
- The forbidden-token grep is clean, the only import is `Mathlib`, and `check_no_sorry.py` reports ALL 29.
- **The copies are byte-identical** (checked by substring):
  - `probes/TemporalCurves.lean` l.28–2029: phase 3, with its own kit copies.
  - `probes/GeneratorStretch.lean`:
    - l.536–624: `I⁻`, its openness, transitivity.
    - l.638–892: push-up and time reversal.
    - l.944–954: `D`, `H`.
    - l.1008–1018: `D` open, `D ⊆ M`.
- **Options.** Two are set:
  - in a verbatim copy, the kit's own `set_option linter.unusedSectionVars false` (as in phases 2 and 3);
  - **in new code, `set_option maxHeartbeats 400000 in` on `pu4_poly`.** This is a time budget only, and it changes
    nothing about what is checked. I split the proof once (`pu4_piece`) to cut its cost; the bookkeeping left in
    `pu4_poly` still needs about twice the default budget. I chose to disclose it rather than fragment the proof
    further.

## The setting

- **The chart:** `S : Spacetime V`, with `V` finite-dimensional.
- **`Θ`** is temporal (the kit's `IsTemporal`).
- **`g`** is locally Lipschitz on `M`, the kit's `hL`; for a `C¹` chart metric it is `ch_chart_lipschitz`.
- **`J ⊆ M`.**
- **"`J` at infinity"** uses the observer hypotheses of `gs_future_stretch`:
  - `O s ≪ O t` for `s < t`;
  - `I⁻(range O) = D J`;
  - **one new hypothesis: `Θ ∘ O → ∞`.**

## Rows

| Row | Statement (Lean) | Mark |
|---|---|---|
| U1 | `pu4_rise`: under the observer hypotheses with `Θ ∘ O → ∞`, points `xₙ ∈ D J` with `Θ xₙ` bounded above have chains `xₙ ≪ O(tₙ)` with `Θ(O tₙ) − Θ xₙ → ∞` | **BUILT** |
| U2 | `pu4_Down`, `pu4_cstep_tail`, `pu4_chain`: every point of a chain's `Θ`-parametrisation is `≤` the chain's end. Inside `pu4_generator`, the limit curve lies in `closure (D J)` (push-up into `I⁻(range O) = D J`). `pu4_approx`: a horizon point is a limit of points of `D J` | **BUILT** |
| U3 | `pu4_cs`: Cauchy–Schwarz on `T⊥` (from `pos_on_perp`). `pu4_rcs`: reverse Cauchy–Schwarz on the closed future cone | **BUILT** |
| U4 | `pu4_dcone`: on a compact `K ⊆ M`, for every `δ > 0` there is `r` such that causal vectors within `r` of `x₀ ∈ K` meet `g_{x₀}(v, w) ≤ δ τ(v) τ(w)` for all `w` in the closed future cone at `x₀`. `pu4_ccone`: the uniform `τ`-cone. `pu4_Lin` with `pu4_arc`, `pu4_lin_concat`, `pu4_chain`, `pu4_lin_shift`/`_sub`/`_congr`/`_limit`: chain curves and their uniform limits meet every linear constraint that holds on the causal cones of a ball | **BUILT** |
| U5 | `pu4_dalg`: a vector meeting the δ-constraints has `τ ≥ 0` and `g(d, d) ≤ (2δ + δ²N) τ(d)²`. `pu4_tilt`: the tilted chord `d + l τ(d) T₀` gives a timelike straight step on a Lipschitz ball, with the time orientation by the intermediate value theorem (`T` only continuous). `pu4_up`: `x ≪ x + εT` and `x − εT ≪ x` | **BUILT** |
| U6 | `pu4_piece`, `pu4_poly`, `pu4_closure`; detailed after the table | **BUILT** |
| U7 | `pu4_global_limit`, `pu4_global_escape`, `pu4_generator`; detailed after the table | **BUILT** |
| U8 | `pu4_witness`: the 2D Minkowski chart with `Θ = fst`, `J = range O` and `O(t) = (t, 0)`. The observer hypotheses hold, U1 produces chains from the origin with rise `→ ∞`, `g` is locally Lipschitz, and reverse Cauchy–Schwarz holds on the null pair `(1, 1)`, `(1, −1)` | **BUILT** |

**U6 in detail.**
- **`pu4_poly`, the polygon.** For a `Θ`-causal, linearly constrained curve there are `κ, C, l₀` such that from any
  `z₀` within `l C` of `γ x`, a polygon of tilted chords is a timelike chain ending within `2 l C` of `γ t`,
  whenever `t − x ≤ κ`.
- **`pu4_closure`.** By real induction, **every point of the curve lies in `closure (I⁺(γ a) ∪ {γ a})`**.

**U7 in detail.**
- **The diagonal is re-run for a given family** (`pu4_global_limit`, `pu4_global_escape`), so the linear
  constraints carry through.
- **`pu4_generator`.** For `p ∈ H J ∩ M`, there is a `Θ`-causal curve `γ` from `p`, on every `[0, Tⱼ]` with
  `Tⱼ ↑ T* ≤ ∞`, such that:
  - every point is in `𝓗⁺ = H J` **and** in `closure (I⁺(p) ∪ {p}) ⊆ closure J⁺(p)`;
  - it eventually leaves every compact `K ⊆ M`.
- **How membership in `𝓗⁺` follows:**
  - the points lie in `closure (D J)`;
  - they are not in `interior J⁻(J)`, because `interior J⁻(J) ⊆ D J` by `pu4_up` and push-up;
  - a point of `D J` near `closure I⁺(p)` would put `p` in `D J`, against `p ∈ ∂J⁻(J)`.

## Against the registration

- **All eight rows are built.** The registered joint event (U1–U3 and U8, p 0.6) held.
- **The named stop (U6, p 0.3) did not hold.** U7 (p 0.25) is built too.
- **A change of method inside U6, disclosed.**
  - **What was registered:** real induction with a single tilt from `γ x` to `γ t`. That cannot work: as the tilt
    `l → 0`, the ball on which the δ-cone and the Lipschitz margin hold shrinks with `l`, so a fixed chord falls
    outside it.
  - **What replaced it:** a polygon of many tilted chords over short intervals, with base points on the curve.
  - **Why it works:**
    - its drift (`≤ l A (t − x)`) stays inside the Lipschitz margin for intervals shorter than a uniform `κ`;
    - its error is proportional to `l`;
    - real induction then works at the top level, as registered.
  - **What it costs:** uniform δ- and `τ`-cones over compact sets (`pu4_dcone`, `pu4_ccone`), and a re-run of
    phase 3's chain and diagonal constructions that also carries the linear constraints.
- **Size:** 1549 new lines, inside the band (estimate 1500).

**Mathlib gap: none found.** The order said to stop at the first gap Mathlib cannot cross and state it exactly.
There was none. Everything used is in Mathlib:
- Hahn–Banach (`exists_dual_vector''`);
- `LocallyLipschitzOn.exists_lipschitzOnWith_of_compact`;
- closed thickenings of compacts (`IsCompact.exists_cthickening_subset_open`, `IsCompact.cthickening`);
- uniform continuity on compacts;
- real induction (`IsClosed.Icc_subset_of_forall_mem_nhdsWithin`);
- the intermediate value theorem.

## What phase 4 does not give (for phase 5)

- **The closure of `J⁺(p)`, not `Cau p (γ t)`.** `HasFutureGenerators` asks for the latter. Route (b) of the plan
  restates `HasFutureGenerators` and `gs_future_stretch` with `closure J⁺(p)`; phase 4 supplies exactly that form.
- **Compacts of `M`, not of `N`.** The curve leaves every compact subset of `M`, whereas `HasFutureGenerators`
  asks for `Tendsto γ atTop (cocompact N)`. A generator that runs into `∂M` in finite `Θ`-time leaves every compact
  of `M` but not every compact of `N`. Phase 5 must either assume the generators stay away from `∂M`, for instance
  `M = N` or `M` closed in the relevant region, or restate the target with compacts of `M`. I flag this as the
  likeliest new obstacle.
- **The parameter domain.** Reparametrising `[0, T*)` onto `[0, ∞)` is bookkeeping.
- **One chart only.** The result is in the chart. Transport to `N` under `OneChart` follows phases 2 and 3; the
  multi-chart `LocallyOneChart` is not attempted.

**Standing of 6b-ii:** still BUILT IN PART: nothing lands in P1 until the row is whole.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

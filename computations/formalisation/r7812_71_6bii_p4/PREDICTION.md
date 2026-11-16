# `r7812+71.1` — PRE-REGISTRATION: 6b-ii, **phase 4: the rise from "`J` at infinity", and the limit curve in the closure of `J⁺(q)` and in `𝓗⁺`**. ⌗ `1500` new lines (band 1000–2200), p(U1–U3 and U8 BUILT) `0.6`, p(U6, the closure of `J⁺`) `0.3`

*Registered before any Lean. The plan is `../r7807_71_6bii/PLAN.md` (phase 4: 700–1500 lines, p 0.3). The probe is the
new standalone `probes/PushUp.lean` (`pu4_`). It imports only Mathlib and carries verbatim copies (not counted) of
`probes/TemporalCurves.lean` (phase 3, which carries its own kit copies) and of the kit blocks it needs from
`probes/GeneratorStretch.lean`: openness of `I⁻`, the push-ups `hl_pushup`/`hl_pushup'`, and `D`/`H`. Setting:
the chart (`Spacetime V`), finite-dimensional, `Θ` temporal, `g` locally Lipschitz on `M` where push-up is used.*

## What phase 4 has to supply

- **(a) The rise.** "`J` at infinity" is formalised the kit's way:
  - a curve `O` with `O s ≪ O t` for `s < t`;
  - `I⁻(range O) = D J = I⁻(J)` (the hypotheses of `gs_future_stretch`);
  - one new hypothesis: `Θ ∘ O` is unbounded above.
- **(b) The closure of `J⁺(q)`.** The approximating chains of phase 3 start at `xₙ → q`, never at `q`; by push-up,
  `J⁺(q) ∩ I⁻(J) = ∅`, so they cannot start in `J⁺(q)`. The limit curve's points must therefore be shown to be in
  `closure J⁺(q)` from the curve itself.
  - **Route.** A **tilt** of its chords: a chord that is nearly causal at `x₀`, plus a little `T₀`, is a timelike
    straight segment.
  - **Then real induction** along the curve.
  - **"Nearly causal" is a convex condition.** It is the family of linear constraints
    `g₀(v, w) ≤ δ τ₀(v) τ₀(w)`, one for each future-causal `w` at `x₀`. So it passes from arcs to chains to limits.

| Row | Statement | Lines | p | Note |
|---|---|---|---|---|
| U1 | **The rise.** Under (a), for `xₙ ∈ D J` with `Θ xₙ` bounded there are chains `xₙ → yₙ ∈ range O` with `Θ yₙ − Θ xₙ → ∞` | 60–150 | 0.8 | `xₙ ≪ O(tₙ)`, then along `O` |
| U2 | **Chain points.** Every point of a chain's `Θ`-parametrisation is `≤` the chain's end (sub-arcs of `C¹` arcs are steps). So the phase-3 limit curve from `q ∈ H J`, built from chains ending on `range O`, lies in `closure (D J)` | 150–300 | 0.7 | |
| U3 | **Reverse Cauchy–Schwarz** at a point: future-causal `v, w` (closed cone) have `g(v, w) ≤ 0`, from `pos_on_perp` by the `T`-decomposition | 80–180 | 0.75 | |
| U4 | **The δ-cone.** Near `x₀`, every future-causal vector at every point satisfies `g₀(v, w) ≤ δ τ₀(v) τ₀(w)` for all `w` in the closed future cone at `x₀` (compactness, as in K1, with U3 at the limit). Chain curves and their uniform limits satisfy every linear constraint that holds on the causal cones of a ball, on every segment inside the ball | 200–400 | 0.45 | |
| U5 | **The tilt.** A chord `d` meeting U4's constraints has `g₀(d, d) ≤ (2δ + δ²) τ₀(d)²`. For `δ` and the ball small against `l`, the straight segment from `y` to `y + d + l τ₀(d) T₀` is a timelike step | 150–300 | 0.45 | |
| U6 | **The limit curve is in `closure J⁺(q)`.** Every point of the phase-3 limit curve from `q` is in `closure I⁺(q) ∪ {q}`, by real induction (`IsClosed.Icc_subset_of_forall_mem_nhdsWithin`) with U5 and openness of `I⁻` | 150–300 | 0.3 | **The expected stop** |
| U7 | **In `𝓗⁺`.** With U2 and U6 and `g` locally Lipschitz (push-up), every point of the limit curve from `q ∈ H J` is in `H J`, and it leaves every compact set (phase 3) | 100–250 | 0.25 | |
| U8 | **Non-vacuity.** The 2D Minkowski chart: (a) holds for a timelike line `O` with `Θ = fst`, and U3–U5 hold there | 60–150 | 0.7 | |

**Mathlib.** No gap is expected. Every row is linear algebra, compactness, the mean-value theorem, and real
induction. The genuinely hard step is the analysis in U4–U6, not missing library material.

**Not in this phase:**
- landing in `HasFutureGenerators` (phase 5), including reparametrising `[0, T*)` to `[0, ∞)`;
- the multi-chart `LocallyOneChart`;
- transport to `N` (here only if time allows, not registered).

P1's 6b-ii stays BUILT IN PART.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

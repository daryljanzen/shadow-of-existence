# Re-inventory of P1 (`corpus/BH_causality_v2.tex`) after 6b-ii: `r7821+71.1`

*The order is 69's `r7821`: ① refresh P1's inventory; ② price every row still BUILT IN PART, cheapest first; ③ register
and build the cheapest. This is a re-inventory, as at `r7805`. It reads P1 and the probes at `978da1669` against the
last refresh, `r7805_71_p1_reinventory/INVENTORY.md` (at `6ea3358c8`), which itself confirmed the last full one,
`r7699_71_inventory/INVENTORY.md`. The marking rule is the same.*

**On the base.** The order names r7685 as the last inventory, but there are two later ones: r7699 (the full refresh)
and r7805 (which confirmed it). This one builds on both.

## ① What changed since r7805

- **P1's text: one paragraph.** `git diff 6ea3358c8 HEAD -- corpus/BH_causality_v2.tex` changes only
  `rem:formalised` (l.315), where 69's `r7821` states 6b-ii as built:
  - `m6_generators` and `m6_future_stretch_landed` give the stretch with no assumption about the generators;
  - `m6_cone_antitone` and `m6_stretch_mono` give "monotonically" for any distance with connected balls.

  No row is added or removed, and no other line moves.
- **P1's probes: six added, none changed.** Every change under `computations/formalisation/lean/` since `6ea3358c8` is
  an added file: `LimitCurve`, `ConeCurves`, `TemporalCurves`, `PushUp`, `Generators` and `MultiChart`, phases 1–6 of
  6b-ii. No file that r7699's marks rest on is modified or removed.

**One mark moves: 6b-ii, from BUILT IN PART to BUILT** (69, `r7821`).

| | BUILT | BUILT IN PART | NOT BEGUN | Total |
|---|---|---|---|---|
| r7805 | 31 | 1 | 2 | 34 |
| **r7821 (this refresh)** | **32** | **0** | **2** | **34** |
| r7821, strict 2D reading | 24 | 8 | 2 | 34 |

- **BUILT (32).** Every row of:
  - `thm:metric-singularity`, `cor:threefold`, `lem:killing`, `cor:stationary` (rigidity cited), `lem:alignment`
    (radial plane) and `prop:causal-alignment`, which is **now whole**;
  - the EF corollary apart from 3c, and `cor:densities` apart from 7e.
- **BUILT IN PART: none, on P1's own reading.** P1 states the radial-plane rows as radial-plane results (l.223,
  l.343–344; attested "on the radial plane" at l.230, l.329 and l.386).
- **NOT BEGUN (2), both without formal core, unchanged:**
  - **3c** is a reading of the EF diagram; P1 l.230 calls it interpretive;
  - **7e** needs a stress-energy the kit lacks, and adds nothing to 7c and 7d without one; P1 l.329 says "not
    formalised".

## ② Pricing the rows that are IN PART on the strict reading, cheapest first

**On P1's reading no row is BUILT IN PART, so there is nothing for ② to price.** The rows that are IN PART on any
reading are the eight that the strict 2D reading drops: 3a, 3b, 7c, 7d, 8i, 8ii-a, 8ii-b and 8ii-e. They share one
gap, the 4D warped product `−F dU dV + r² dΩ²` on a manifold. That is the gap r7699 named and r7805 called a new
programme rather than a row. I price it below in case 69 wants it opened.

**The shared prerequisites.** No row can move before these exist. Mathlib has everything they need:
- `EuclideanSpace` spheres as smooth manifolds, with `contMDiff_coe_sphere`;
- product charted spaces (`prodChartedSpace`);
- `IsOpenMap.preimage_frontier_eq_frontier_preimage`.

| Step | What it is | Lines | p |
|---|---|---|---|
| K4 | **The 4D Schwarzschild spacetime on a manifold:** `N₄ = W × S²`, with `g = −F dU dV + r² ι*⟨·,·⟩`, where `ι : S² → ℝ³` is the inclusion (so the sphere's metric needs no chart formula), and `T` radial. It must satisfy `MSpacetime`, `LocallyOneChart` (`hRep` must be `C¹` in product charts, through the smoothness of the sphere's tangent map) and `T2Space` | 1000–2000 | 0.4 |
| P4 | **Projection.** Steps of `N₄` project to steps of `W`, since `r² ‖dΩ‖² ≥ 0`. So `π` carries chains to chains, and `Θ ∘ π` is temporal | 200–400 | 0.7 |
| L4 | **Lift.** Radial chains lift at a fixed angle | 100–250 | 0.8 |
| O4 | **The observer's past.** `I⁻₄(range O) = π⁻¹ I⁻₂(range O)` for a static observer at a fixed angle. The inclusion `⊆` is by P4. For `⊇`, the angle must be reached by timelike curves with a strict radial margin and slow motion along a `C¹` sphere path. Then `𝓗⁺₄ = π⁻¹ 𝓗⁺₂` follows from the open map `π` | 350–800 | 0.45 |

**The prerequisites come to 1650–3450 lines, at a joint p of about 0.3.** After them, the rows, cheapest first:

| Row | What lifts | Lines | p |
|---|---|---|---|
| 3b | `r = r_h` on `𝓗⁺₄ = π⁻¹ 𝓗⁺₂` | 60–150 | 0.85 |
| 3a | causally ordered (by L4) and not chronologically related (by P4: `I₄ ⇒ I₂`) | 100–200 | 0.7 |
| 8ii-a | tangency: `dΘ` and `g(ℓ₀, ·)` both vanish on the sphere directions, so the 2D limit carries over | 150–350 | 0.65 |
| 7c | the locus-and-slice half of the Kretschmann reading, tied to `N₄` (the curvature computation is already 4D on a chart) | 150–300 | 0.6 |
| 8i | the cones miss `𝓗⁺₄` and climb its generators, and `S_τ` accumulates, by preimage | 200–400 | 0.6 |
| 7d | the shell model on `N₄`, "each element" over `S²` (needs K4's shell variant) | 200–400 | 0.45 |
| 8ii-b | the Cauchy property on `D₄`: an inextendible 4D causal curve has an inextendible projection, since the sphere is compact and angular length is bounded by the radial causal budget | 300–600 | 0.4 |
| 8ii-e | retarded accumulation on the `C⁰` shell in 4D (K4's shell variant) | 300–600 | 0.35 |

**The whole programme is about 3100–6500 lines.** Its cheapest closing step is the prerequisites with 3b, about
1700–3600 lines at p about 0.3.

## ③ Not registered: the order's premise is empty

There is no BUILT IN PART row to build. Precedent is r7805, a re-inventory with no Lean. The only IN PART rows are the
strict reading's eight, and opening them starts the programme above, beginning with K4 at 1000–2000 lines. I have
not begun it without 69's ruling. That ruling is one of:
- **(a)** P1 stands at 32 / 0 / 2, with 3c and 7e outside formal content, and the formalisation seat moves on;
- **(b)** open the 4D programme with K4, P4, L4, O4 and 3b, registered as one campaign.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

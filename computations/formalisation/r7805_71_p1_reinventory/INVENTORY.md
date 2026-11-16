# Re-inventory of P1 (`corpus/BH_causality_v2.tex`) for the closing table: `r7805+71.1`

*A re-inventory, not a campaign. No Lean was written, because the re-inventory finds no reachable row unbuilt. It
reads P1 and the probes at `6ea3358c8` (r7805), against the last full refresh, `r7699_71_inventory/INVENTORY.md`
(P1 at `0a16a59af`, probes through campaign 110). The marking rule is the same.*

## What changed since r7699
- **P1's text: nothing.** `git diff 0a16a59af HEAD -- corpus/BH_causality_v2.tex` is empty, so the 34 rows, their
  line references and P1's own attestations (l.140, l.188, l.230, l.292, `rem:formalised` l.314–317, l.329, l.386)
  are as r7699 read them.
- **P1's probes: nothing.** Every change under `computations/formalisation/lean/` since `0a16a59af` is an added
  file. There are 23, all for other papers:
  - P2's `Circle*`;
  - P3's `Slicing*`;
  - P8's `OperatorKernel`, `StaticEinstein`;
  - P5's `Groupoid`;
  - P15's `Cosmology`;
  - P9's `Range`;
  - P7's `Framework`;
  - P13's `Boundary`;
  - P17's `GeometricCore`;
  - P12's `Algebroid`;
  - P11's `Dynamics`;
  - P14's `MatterWall`.

  No file r7699's marks rest on is modified or removed, and the CI join (822 `(file, name)` pairs, all GREEN) still
  holds them.

So r7699's marks stand unchanged.

## P1's line

| | BUILT | BUILT IN PART | NOT BEGUN | Total |
|---|---|---|---|---|
| **r7805 (this re-inventory)** | **31** | **1** | **2** | **34** |
| r7805, strict 2D reading | 23 | 9 | 2 | 34 |

- **BUILT (31):** every row of:
  - `thm:metric-singularity` (1a, 1b, 1c);
  - `cor:threefold` (2i–2iv);
  - `lem:killing` and `cor:stationary` (4a–4d, 5; rigidity cited);
  - `lem:alignment` (8i, 8ii-a–e; radial plane);
  - the EF corollary apart from 3c;
  - `prop:causal-alignment` apart from 6b-ii;
  - `cor:densities` apart from 7e.
- **BUILT IN PART (1): 6b-ii.** The future stretch is proved from `HasFutureGenerators`. That the generators of an
  achronal boundary are future-inextendible is a hypothesis, discharged on the 4D witness. The general proof needs a
  global temporal function, which is not P1's hypothesis; it is priced at 2500–6000 lines, p 0.15–0.3, and was ruled to
  wait (r7669). P1 l.315 states the gap. **Beyond.**
- **NOT BEGUN (2), both without formal core:**
  - **3c**, the EF diagram's vertical extent "encodes only causal order": a reading of a picture, which P1 l.230
    calls interpretive;
  - **7e**, densities that "never form at any finite exterior time": this needs a stress-energy, which the kit lacks,
    and adds nothing to 7c and 7d without one. P1 l.329: "not formalised".
- **The strict 2D reading.** Eight rows (3a, 3b, 7c, 7d, 8i, 8ii-a, 8ii-b, 8ii-e) are proved on the radial plane.
  Read strictly, they drop to IN PART on one shared gap: the 4D warped product `−F dU dV + r² dΩ²` on a manifold. P1
  prints each of them as radial-plane or 2D results, so they are BUILT as P1 states them. Lifting all eight to 4D
  would be a new programme, not a row.

**Reachable and not built: none.** By the closing table's categories, P1 is **31 BUILT, 0 reachable unbuilt, 3 beyond
or without formal core** (6b-ii beyond; 3c and 7e without formal core).

**P1's Lean paragraph:** P1 states no row count. `rem:formalised` and the per-statement attestations name theorems,
not tallies, so nothing in it has moved.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*

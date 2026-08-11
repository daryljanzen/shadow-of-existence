# Bundle r972 — synthesis figure fully analytic (no schematic content)

r972 iterates r971's synthesis figure so that every physically meaningful curve is rendered from its
analytic description, not sketched. Two panels changed and the receipt now integrates real geodesics.

- **(b) reassigned (τ,χ):** the photon **null geodesics are now integrated analytically** from
  dτ/dχ = ±∂_χr, r(τ̃)=sinh^{2/3}((3/2)τ̃) — they curve so the light cones tip toward the seam (the
  qualitative feature the original BST inset carried and the earlier schematic straight cone killed).
  Coordinate families exact: constant-χ (fundamental, red), constant-τ (flat space, green),
  constant-τ̃=τ+χ (S³ layers, purple); the seam τ̃=0 is the null boundary.
- **(f) the lap's cos oscillation** (replaces the r971 two-slicings cartoon): the embedding coordinate
  around the conjugate lap is **X₁ = −cos(2πr/√3)** through the roots +α/√3, 0 (trough X₁=−α), −2α/√3,
  with the real ruling legs straight at slope π (C¹ at the junctions) — reproducing P3's fig:conjwave.
  This is the oscillation the hyperboloid flattens because it happens at the equatorial throat.
- **(e)** stripped to the clean analytic ±r(τ̃) envelope (the decorative interior worldlines removed).
- (a) hyperboloid, (c) lap r(τ̃), (d) Nariai trichotomy were already analytic and are unchanged.

No conceptual cartoons remain. Receipt: corpus/synthesis_figure.py (uses scipy solve_ivp for the nulls).
Caption in P7 updated for (b) and (f). P7 compiles clean (37 pp, 0 undefined); all 17 papers clean.

Prior: r971 (six-panel restructure fixing the four-fold reassignment), r970 (figure v1), r969 (references),
r968 (P-symbol + coherence). Bundle excludes only regenerable compiled paper PDFs and build cruft.

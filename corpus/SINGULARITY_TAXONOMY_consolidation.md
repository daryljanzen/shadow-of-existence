# The Singularity Taxonomy — consolidated (the r152–r156 confluence)

**Status.** Canonical consolidation of the singularity-taxonomy clarity matured across
r152–r156. This is the source the corpus-wide edit aligns to. It carries the full taxonomy
(three kinds), the metric-singularity genus and its two species, the derivative-order index
that locates the pair precisely, the elementary reason the location is forced (the circle),
the analogy that carries it to a lay reader (the cone tip), and what this earns Paper 2.
Pedagogy and rigour both, kept separate where they must be. Stated for reversal.

**What this is, and is not.** Not new physics — a clean sorting of geometric/topological
objects (the horizon, $r=0$, the coordinate singularity) that, *because* everyone already
"knew what a black hole is," were never properly sorted. An archaeological find: the bones
were always there; the field had them mis-shelved. The proof in Paper 2 does not move; once
the objects are correctly named, the sixty-year horizon-vs-singularity asymmetry simply is
not there to explain.

---

## 1. The three kinds (the dagger's frame: *point* vs *place*)

A singularity is where a **point** (a member of the manifold) and a **place** (a value of the
chart) come apart. There are exactly three ways:

1. **A place with no point** — the chart names a location the manifold lacks; the ruler has
   gone *infinite*; the manifold has a hole. The **curvature singularity** in its pure form
   ($\tan\theta$ at $\pi/2$).
2. **A point at many places** — one manifold point smeared across many chart-values by a
   degenerate chart; *no real collapse*, nothing piled up. The **coordinate singularity**
   (the Mercator pole). This kind is *outside* the metric-singularity genus — a different
   beast entirely.
3. **Many points at one place** — many distinct manifold points piled at one chart-location,
   the ruler collapsed to *zero* separation between them. The **metric singularity**. The
   genus the black hole's two features actually belong to.

## 2. The metric-singularity genus and its two species (Papers 1 & 2)

Kind 3 has two species, indexed by curvature:

- **finite-curvature metric singularity** — the **event horizon**: worldlines pass *through*;
  infinitely many distinct, causally-ordered, metrically-coincident events at the one areal
  radius $r=2M$; the place intact (Paper 1 makes this precise).
- **infinite-curvature metric singularity** — **$r=0$**: the infalling worldlines *end* (the
  family reaches a terminus), and the deep/intrinsic curvature genuinely diverges. This is a
  metric singularity (kind 3) that *also* carries a real curvature divergence.

The two are one genus, "distinguished only by curvature" (Paper 2). Note the discipline:
$r=0$ is **not** a kind-1 hole. The $1/r^6$ Kretschmann pole is a label artefact (chain rule;
§4), the *intrinsic* spike is real, and the analytic curve **continues through** $z=\pi$ —
so the inextendibility *inference* (curvature-divergence $\Rightarrow$ no continuation) fails
(Paper 2). $r=0$ is the infinite-curvature species of kind 3, which the standard reading
*mis-reads* as kind 1.

## 3. The standard classification's category error

The field shelves the horizon under **kind 2** (coordinate singularity, "removable") and
$r=0$ under **kind 1** (curvature singularity, "physics ends, the manifold tears"). Both are
**kind 3** (metric singularities), the two species of one genus. The error is one category
error committed twice; the asymmetry is the *labelling's*, not the geometry's.

## 4. The derivative-order index — locating the pair precisely (r154–r155)

The two species are the two critical points of one slicing curve. Their relationship, by
order — this is the index that was missing, and it locates the pair exactly inside the genus:

- **substrate / curve level:** topologically identical — the two critical points exchanged by
  the curve's involution.
- **0th order (interval / genus):** identical — both metric singularities; the line element
  collapses at both (in complementary sectors: temporal $g_{tt}\to0$ at the horizon, angular
  $r^2\to0$ at $r=0$ — and the sector is itself a function of the value $r$).
- **1st order (connection):** identical — there is **no first-order scalar invariant** (the
  lowest curvature invariant is the Ricci scalar, 2nd order in $g$; the Christoffels are
  gauge, killable in normal coordinates). The chart degenerates at *both* critical points,
  symmetrically. The curve's own first derivative is identical (zero) at both.
- **2nd order (curvature / species):** distinct — finite vs pole; the **first** invariant
  that distinguishes them, and it distinguishes them completely.

**Verdict.** First-order **identical**; the distinction is localized **entirely at second
order**. It is *sourced* at zeroth order — the value $r$ the chart assigns each pole, $2M$ vs
$0$ — but it *lands* at second order, because curvature is the lowest invariant and the one
that poles on $r$ ($K=48M^2/r^6$). The crack (normal coordinates can fail at a metric
singularity) is closed: the only invariant that exists at/near the singular point is the
2nd-order one — there is nothing at first order for a difference to hide in, and the apparent
first-order difference (the connection's $1/r$ blow-up at the axis) is the polar-coordinate
gauge degeneracy flat space has at any origin, symmetric at both, not invariant.
[Receipt: `scripts/firstorder_taxonomy_1.py`.]

**Retire "metrically identical" as false**, not merely confusing: the metric fixes the
curvature through its second derivative, and the curvature differs. What is identical:
topological-on-the-substrate, plus zeroth- and first-order-metric. What differs:
second-order-metric (curvature). That is the whole of it, stated at the right order.

## 5. Why the identity is forced — the circle (r156)

$r$ satisfies $r'' = -(r-M)$: simple harmonic motion about $r=M$, i.e. the projection of
uniform circular motion. With the conjugate $s=M\sin z$ (the coordinate that goes imaginary
to give the exteriors), $(r-M)^2+s^2=M^2$ — the **circle** of Paper 2's "hyperbola, circle,
hyperbola." The two critical points are the circle's two **$r$-poles** (where it crosses the
$r$-axis, $s=0$): $r=2M$ (far) and $r=0$ (near). At a pole the tangent is vertical, so
$dr/dz=0$ — **forced, not computed**; and the circle is **homogeneous** (no special point),
so the two poles are one point seen twice, related by reflection through the centre. The
*identical analytic character* is the circle's homogeneity.

The sole asymmetry is **where the Cartesian grid's origin landed** — on the $r=0$ pole — and
curvature $K=48M^2/r^6$ divides by the grid-coordinate, so the pole sitting on the origin is
the one that spikes. The difference was never in the object; it is the chart's choice of
origin, and curvature is precisely the thing that reads the chart's origin.

## 6. The analogy — the cone tip (and where it belongs)

Curvature of a swept surface = **the bend of the profile ÷ the distance to the axis**. The
two turning points bend **identically** ($|r''|=M$ at both — one a peak, one a trough, the
same steepness). So the lopsided curvature is *not in the curve's bend*. One pole sits out
at radius $r=2M$ — the bend over a healthy distance, gentle. The other sits *at* the axis,
$r=0$ — the *same* bend over zero distance, an infinitely sharp point, a **cone tip**. The
spike at the centre is not a sharper curve; it is the identical curve, swept where dividing
by $r$ blows up. This **is** the off-axis pivot, and it **is** the answer to the dagger's
deferred lopsidedness question ("why the spike at one end and not the other, when the curve
is even-handed?"): the Schwarzschild sweep pivots *at* the axis; the de Sitter sweep pivots
*away* from it, and nothing diverges.

**Placement (a sweep finding).** Because the cone-tip *is* the lopsidedness answer, it
belongs in the **double-dagger** (the off-axis-pivot installment the dagger hands forward),
**not** in the dagger, whose arc deliberately leaves that question open. And it **supersedes
the r154 three-questions draft**: that draft's line-vs-bowl picture shows two *different*
profile bends meeting at a point — which correctly illustrates the *general* "meet to first
order, split at second" truth, but **misrepresents this geometry**, where the two profile
bends are *equal* and the split is the sweep, not the bend. The dagger needs no insertion;
its "the curve is even-handed, the map is not" already carries the first-order identity in
its own voice. The rigorous order-index (no first-order invariant) lives in the papers (§4);
the cone-tip carries the *why* of the asymmetry in the double-dagger.

## 7. What this earns — Paper 2's place

Paper 2 *proved* the pair (same genus, distinguished only by curvature) but never seated them
in the full set; the dagger carried the three kinds, Paper 2 did not — which is why the
dagger outran the formal paper that did the circle properly. With §1–§6, Paper 2 can open by
naming the whole taxonomy (three kinds, the coordinate singularity included as the kind the
pair is *not*), prove its pair as two precisely-located points inside the metric-singularity
genus (identical through first order, split only at second, the location *forced* by the
circle's homogeneity), and name the standard "removable coordinate singularity / true
curvature singularity" labelling as the category error it is — a finite-curvature metric
singularity mis-shelved as a coordinate one, an infinite-curvature metric singularity
mis-shelved as a hole. Taxonomic hygiene: sorting the objects *is* the understanding. That is
Paper 2 earning its place beside 1, 3, and 5.

## 8. Pedagogy vs rigour (keep separate)

The cone-tip and three-questions pictures are clean **as pedagogy** — they ride general
truths (a swept surface's curvature divides by distance-to-axis; curves can meet to first
order and split at second) and need no caveat. The **rigorous** first-order claim (no
first-order invariant; the crack at the singular point) is **settled** (§4, receipt) and may
now be asserted in the formal papers. **Chapter X is not edited** (Daryl's call); **the
daggers are.**

---

## Edit map (targets, what lands where)

- **Paper 2 (`janzen_circle_v3.tex`) — PRIMARY.** Open with §1–§3 (the three kinds, the
  genus/species, the category error). Reseat Prop-critical with §5 (the circle: identical *by
  homogeneity*, not by differentiation; the chart's origin the only asymmetry). Add §4 (the
  derivative-order index) where it currently says "identical analytic character." This is the
  paper earning its place (§7).
- **Paper 1 (`BH_causality_v2.tex`).** Add the derivative-order index to its
  metric-singularity treatment; make explicit that the horizon is the *finite-curvature
  species of kind 3*, and the coordinate singularity (kind 2) is the kind it is *not*.
- **Paper 3 (`SdS-slicing-curve_v2.tex`).** Already aligned r153 (topological-on-substrate /
  not metrically identical). Check it carries the derivative-order order-index and the
  circle/cone-tip where natural; it owns the off-axis pivot (§6).
- **Dagger (`cosmicave_dagger_*.md`).** *No insertion* — survey finding. The essay's arc is
  already complete and correct: it raises "same yet lopsided," resolves "same kind" via the
  Mercator/sweep argument, concedes the real spike, and deliberately *defers* the lopsidedness
  to the next installment. Its "the curve is even-handed, the map is not" already carries the
  first-order identity. A curvature-splitting beat would misstate the geometry or spoil the
  deferral (§6).
- **Double-dagger (`cosmicave_double-dagger_DRAFT.md`).** The off-axis pivot is its content,
  and the **cone-tip is its centrepiece** — the deferred lopsidedness answer (bend ÷
  distance-to-axis; the two poles bend *identically*; the one at the axis becomes a cone tip;
  the de Sitter pivot is off-axis and nothing diverges). The circle seats it ("two $r$-poles
  of one homogeneous circle; the grid's origin the only asymmetry; curvature reads it"). This
  is where the r154 three-questions insight migrates, in cone form.
- **Chapter X — not edited (Daryl's call).**

---

## Value-added pass (r158) — the mirror held to every document

The coherence pass (r157) asked "is each document consistent with the taxonomy?" This pass
asks the higher question: "would each land harder if written with the taxonomy understood from
the start?" The honest finding: **the corpus was already deeply aligned** — the off-axis-pivot
/ sweep story is thoroughly built in Papers 3 and 4, and the metric-identity correction already
sits in Paper 3 §593. What the r152–r156 work actually produced was a **strengthened Paper 2
result** (the circle as the forced reason; the derivative-order index), and the value-add is
**propagating that strength outward** to the places that cite "identical analytic type" — which
dovetails with what 3 and 4 already argue (the asymmetry is the sweep, not the curve).

**Committed (r158):**
- **Paper 2 front matter.** Abstract: "distinguished only by curvature" → "...only at second
  order; identical through first order; the two $r$-poles of one homogeneous circle; the
  asymmetry entirely the chart's origin, not the curve." Intro: the "two extrema on the circle"
  line upgraded to the homogeneity-forced reason. The body grew (r157); the front matter now
  claims it. This is what makes Paper 2 read as the paper it is.
- **The framework paper (`framework_paper.tex`) §157.** The framework's distillation of Paper 2 sharpened: the even bend
  ($|d^2r/dz^2|=M$, the two poles of one homogeneous circle) localises the pair to first-order
  identity and parts them only at second order — so the whole asymmetry is the chart's origin.
- **Paper 3 §586 (sweep section).** Tied the qualitative pivot-divergence to the paper's own
  $K_G=1/\alpha^2-M/r^3$: a surface of revolution has $K_G=-r''/r$ (curvature ÷ distance-to-axis),
  so the $-M/r^3$ term is the pivot signature — divergent at $r=0$, absent for the $M=0$ de
  Sitter sweep. Quantifies §586's claim in the paper's own computed curvature.

**Assessed, not edited (honest):**
- **Paper 4.** Already adequate: §337/§341/§366 cite "identical analytic type" and state the
  asymmetry tracks the pivot "not the curve, which is symmetric." The stronger result does not
  change the groupoid argument; upgrading the citations is gilding. (Note: the cycloid's two
  critical points are *not* exchanged by the root-exchange $\sigma$ — $\sigma$ permutes horizon
  roots, and $r=0$ is not a root — so resist that tempting but false connection.)
- **Paper 1.** Well-served already (§151 genus/species, abstract frames horizon = metric
  singularity). Low add.
- **Paper 7.** Uses horizon = metric singularity as input; the taxonomy is background. Low add.
- **Methodological essay.** The circle as an exemplar of excavated forced necessity ("I see it,"
  not "that makes sense") is a genuine but optional add in Daryl's methodological voice —
  offered, his call.
- **Canonical-time paper.** Orthogonal to the singularity taxonomy. No add.
- **Frontier papers (slicing_operator, range_paper).** In flux; bringing them up waits until the
  frontier stabilises (per kickoff). Deferred.
- **Chapter X.** Not edited (Daryl's call).

---

## Full-corpus bake-in (r159) — the value pass done right, frontier papers included

The r158 pass deferred the frontier papers ("until the frontier stabilises") and called several
papers "already adequate" — the coherence bar masquerading as the value bar, and a stale guard
imported from a compaction summary (wake protocol re-run before this round). Daryl corrected it:
bake the whole notebook's nuance into the *entire* corpus now, one paper at a time, propagating
the understanding forward. Done. Each add genuine; one honest blank.

- **Paper 5 `slicing_operator.tex` §211.** The cosmological "$r=0$ Big Bang" named in the
  taxonomy: a **finite-curvature** metric singularity (the smooth past null boundary $B$, a
  horizon, the event-horizon's species), **not** the infinite-curvature centre — the Big-Bang
  reading is the cosmological face of the doubled category error. (Notebook §112–118 NBC-seam
  result, finally in the operator paper.)
- **Paper 6 `range_paper.tex` §97.** The range framed along the **null-degeneracy (Petrov)
  axis** with its **two boundaries**: the seam (Nariai, inner — two horizon null surfaces merge
  at the double root, still Type D) and the wall (outer — all degeneracy lost into the one
  Type-N null direction). Opposite ends of one axis. (Notebook §439–453 synthesis.)
- **P7 `CR_framework.tex` §641** (echoed in P13 `CR_cosmology.tex` abstract/intro)**.** The cosmogenesis seam seated in the two-species
  taxonomy: the event-of-events is the **finite-curvature** metric singularity (the horizon),
  substrate-regular, reached only in the infinite-cosmic-time limit — **never** the
  infinite-curvature $r=0$ no finite layer reaches. Reading the cosmic beginning as a curvature
  singularity is the cosmological face of the doubled category error. (The "low add" I had
  lazily dismissed at r158 — it was high.)
- **Paper 4 `groupoid_paper.tex` §337.** The diagnostic sharpened by the derivative-order
  result: the curve is even-handed **through first order**, so the off-axis pivot is the
  **entire** source of the second-order (curvature) difference — not merely "the curve is
  symmetric." (Resisted again the false $\sigma$-exchange; $\sigma$ permutes horizon roots,
  $r=0$ is not a root.)
- **Methodological essay `methodological_essay.tex` §161.** The circle route made an instance of
  the essay's own thesis (conclusion *forced*, not proposed): the two critical points are
  identical because they are the two poles of one circle, which has no distinguished point — the
  geometry forcing it, not the inspection proposing it.
- **`canonical_time.tex` — honest blank.** Drafted this session with the relevant results cited
  (§114 metric-singularity orientation, §152 non-singular cosmology); the singularity *taxonomy*
  is orthogonal to its problem-of-time content. No add.

With r157–r158, every corpus paper now carries the taxonomy where it adds value: Paper 1 (already
genus/species), Paper 2 (circle + order index + front matter), Paper 3 (§586 $K_G$ pivot
signature), the framework paper (§157), Papers 5/6/4/7 + the methodological essay (this round). Chapter X not
edited (Daryl's call); the daggers complete (cone-tip staged for the double-dagger, his register).

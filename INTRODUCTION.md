# Introduction

## 1 · What this is

General relativity does not single out a physical foliation. Nothing in the theory says which slicing of
spacetime is *the* present, and the standard reading takes that as a statement about the world: no objective
present, no fact about simultaneity, only the block.

**Cosmological Relativity begins from the observation that this is a statement about general relativity, not
about the world** — and that the world, in one specific circumstance, does single one out. Under gravitational
collapse the horizon's own geometry fixes a limiting causal direction, and it is generically non-orthogonal to
any spacelike slice. That direction is not a convention. It is forced, and it is what gets reassigned as
cosmic time.

Followed through, the picture inverts. Our universe is read as **the interior of a gravitational collapse** —
not an explosion from a point but the far side of one, on the conjugate branch: an antimatter progenitor,
decelerating to a turnaround, sweeping through the coordinate origin where the species reverses, re-expanding.
What we call the beginning is that passage. The origin is not where matter came from; it is a horizon the
slicing is anchored to, and the reading that made it a source was inherited from a choice of slicing rather
than found in the geometry.

The progenitor is not a free parameter. The collapse selects the one configuration whose limiting direction
grazes its own horizon, and that fixes its mass by the cosmological constant alone — **M = c²/3√Λ G**, about
4×10⁵² kg. Everything on the geometry scales from that single length.

## 2 · The corpus — seventeen papers

*The reading order is in `README.md`, which follows the corpus's own causal spine rather than the numbering.*

**The forcing.** **P1** shows the event horizon is a metric singularity — a missing definition in general
relativity, argued from causal structure alone. **P4** shows the redshift-isotropy floor forces the cosmic
foliation empirically. The two are a complementary pair: one *proves* it, the other *measures* it.

**The substrate.** **P2** gives the Schwarzschild and de Sitter circle — one homogeneous ring, the intrinsic

**⛔ THE DIMENSIONS, because the corpus is subtle here and a reader who guesses gets it wrong.** ***The SUBSTRATE is dS₅ = SO(5,1)/SO(4,1)*** — a hyperboloid in flat ambient M⁶, **the thing that is *sliced*.** ***The BACKGROUND is dS₄*** — the maximally symmetric four-geometry the substrate's leaves carry, **itself a cut, the thing that is *reassigned*.** Below those sit **the exact solutions** (Schwarzschild, Nariai, the Friedmann geometries), and below those **the layer 𝒮ₜ — the three-dimensional existent**, with the four-manifold M its *representation* and not an existent. *The fifth dimension is forced: **slicing a four-dimensional de Sitter space only re-coordinatizes it**, so a dS₄ substrate would generate nothing.* **"The substrate is four-dimensional" is a retracted error.**
geometry. **P3** gives the substrate and its slicing curve, horizons as turning points. **P5** gives the
description groupoid: generators, relations, and Schwarzschild as one member. **p0** is the geometric core —
the maximally symmetric substrate, reached through the imaginary and real by construction.

**The framework.** **P7** — *collapsed matter must become a universe*: the necessary and sufficient
augmentation of general relativity. **P8** gives the slicing operator and the covariance of geometries over
the substrate; **P9** its range, surjective onto the symmetry-reducible sector; **P11** why the cut bends.

**Time and the constraint algebra.** **P10** treats the canonical problem of time as a category error, with an
empirically forced cosmic time. **P12** identifies GR's constraint algebra as the symmetric-space structure of
the substrate — and the problem of time's "wrong sign" as the substrate's coset signature.

**Matter.** **P13** maps four converging routes to a geometric boundary on what the substrate's isometry does
and does not force. **P14** gives the fermion sector: three chiral generations from the maximally symmetric
substrate.

**Cosmology.** **P15** gives the expansion history from causal reassignment. **P16** gives cosmogenesis — the
Big Bang as a synthesis of the framework's deductively forced consequences.

**P6** stands apart and holds the rest: *the shadow of existence* — scientific theory-choice as an empirically
grounded discipline. It supplies the epistemic altitude the whole corpus is held at.

**Two documents are corpus in ledger form rather than paper form:** the geometry ledger (58 proved statements
across 25 receipts) and the combinatorics ledger (the corpus's numbers are two families, the boundary between
them the Standard Model's arrangement).

**Every computed claim cites a script that can be re-run.**

### The dependency matrix, and why the corpus has no first page

<figure>
  <object data="BOOK_INTRO_cosmiCave/assets/dependency_matrix.html" type="text/html" width="100%" height="640"></object>
  <figcaption><strong>Figure 1 — the corpus's citation dependency matrix.</strong> Entry <em>(i, j)</em> is the
  number of times paper <em>i</em> cites paper <em>j</em>. A <em>row</em> is what a paper rests on; a
  <em>column</em> is what it feeds. Heat-shaded; both poles marked; the P1↔P4 complementarity flagged.</figcaption>
</figure>

*(The live table is `BOOK_INTRO_cosmiCave/assets/dependency_matrix.html`, regenerated from the corpus by
`scripts/depmatrix.py`; the same data is P7's `tab:dependency-matrix`.)*

**Read down the columns and one thing stands out: exactly two papers are coupled to the whole corpus** — a
full row *and* a full column each. **P7, the framework**, and **p0, the geometric core.** *(Verified from the
source `.tex` rather than the rendered table: each cites all sixteen others and is cited by all sixteen. P3,
the waypoint, is cited by fifteen and has the largest column sum, **147** — recomputed r1612 at 146 and again r1632 after P3 gained a citation; the figure had read 134, stale since the r1600–r1608 placements added citations without re-running `scripts/depmatrix.py`.)* Everything feeds P7
and P7 feeds everything; p0 is built from every paper and points back to every paper. The other fifteen cluster
and gap; these two touch all.

**That is why the corpus resisted being put in an order for so long, and why it has no first page.** A one-hub
corpus is a tree with a root, and a root sits at the front. **A two-hub corpus has no linear slot — it has a
*between*:** fifteen papers stretched between two synthesis poles. p0 kept wanting to be "the border" for
exactly this reason.

### Where to come in
*Two things follow, and they answer different questions. **The doors** are per-reader: one arrives with an
interest and enters where it is answered. **The guided arc after them is one route for a room** — ordered by
structural depth rather than by readership, and **deliberately not opening with P1 and P4**, which carry the
load and also raise the guard before there is anything to weigh them against.*


The matrix is not only a self-portrait; it says as data where a reader should enter. **There is no single first
page, so here are the doors — and whichever you take, the road runs through P3**, the largest column sum in the
matrix and where the substrate's geometry is actually built.

**If you want what is *forced* — the sceptic's door: P1, then P4.** The two forcing keystones, and the matrix
marks them a complementary pair: **P1 proves** the foliation from causal structure alone, needing none of the
cosmology; **P4 measures** it, from the redshift-isotropy floor. Nothing downstream is load-bearing until these
hold.

**If you are a cosmologist: P1, P4, then P7, P15, P16.** The forcing, then the framework, then the expansion
history from causal reassignment, then cosmogenesis — the Big Bang as a synthesis of forced consequences, with
the light-element abundances reproduced and the Hubble tension resolved across the low-redshift distance
ladder.

**If you come from philosophy, epistemology, or the history of science: P6.** It is the door to the foundational
drivers, and it argues something prior to the physics — that *"the epistemology of scientific theory-choice is a
discipline of the same kind as the sciences it grounds, with the same object and the same method."* A physical
theory is chosen, ahead of any decisive measurement, by coherence, by **requiring rather than permitting** the
phenomena, by consolidation and resistance to patchwork. **P6 also supplies the altitude the whole corpus is
held at**, so it repays reading early even by those who came for the geometry.

**If you work in canonical general relativity — the esoteric door: P12, and P10 beside it.** P12 is entered
directly by anyone who knows the hypersurface-deformation algebra: it establishes that the Dirac algebra **is
not a Lie algebra but a Lie algebroid**, that the symmetric-space grading is that algebra *term for term*, and
that the **problem of time's "wrong sign" is the substrate's coset signature.** P10 treats the canonical problem
of time as a category error, with an empirically forced cosmic time.

**If you come for the Standard Model: P13, then P14.** P13 is a synthesis as much as a boundary — **four
converging routes** to one wall, with three operations co-located at the branch point pried apart. P14 gives three
chiral generations on the discrete residue.

**If you want the *whole*: either pole — p0 or P7.** From either, the rest is one step away. **These two are
what make the corpus a dipole**, and each is a full row *and* column of the matrix.

*(A different order exists and serves a different purpose: `README.md` steps 3–6 read the corpus along its
**causal spine**, the order in which the results are forced. That is for someone who must be able to stand on
each result before the next leans on it. **The doors above are interest-ordered; that order is
dependency-ordered.** Neither is the reading order — they are answers to different questions.)*

### The guided arc — if you had them all in a room

*The doors above are per-reader, each entering where their own question is answered. **This is the other thing:
one route, for a room of them.** It is ordered by what is most structurally arresting to someone who already
holds the machinery — and it deliberately **does not open with P1 and P4.** Those two carry the load, and they
are also the two that put a reader's guard up before there is anything to weigh them against. **They come at
the end, when the structure they force has already been seen.***

**① `P12` — the constraint algebra is a Lie algebroid, and the "wrong sign" is a coset signature.**
*Start here because it is checkable in an afternoon by anyone who knows hypersurface deformations, and because
it costs nothing to accept.* The Dirac algebra's structure function makes it **not a Lie algebra**; read as a
**Lie algebroid** the anchor is the ADM data as functions of the cut — **energy IS the Hamiltonian constraint,
the bend of the leaf**. And the symmetric-space grading $\mathfrak{so}(5,1)=\mathfrak h\oplus\mathfrak m$ **is
that algebra term for term**, with the notorious $\pm q^{ab}$ sign the substrate's **Lorentzian coset metric**.
*A recognition, not an addition — that is the paper's own weight-marking.*

**② `P10`, immediately beside it — what the algebroid licenses about time.**
The problem of time as a **category error**: the bare formalism singles out no foliation, and CR's selection is
**measured rather than posited**. Deparametrized, the constraint is solved for a **true Hamiltonian that
generates the advance**, and quantum evolution in cosmic time is unitary — *the frozen constraint and the true
Hamiltonian are the same canonical content under two readings.* **And the scale factor's lone self-adjoint
extension freedom is closed with no free parameter**, by the de Sitter horizon's own Hartle–Hawking state at
$\kappa=1/\alpha$ — **which is the substrate read on its other real form**, the global Wick carrying
$\mathrm{dS}_5$ to the compact $S^5$, the two being real forms of one $SO(6,\mathbb C)$.

**③ `P8` — matter is a bend of the cut, and the offset IS the mass.**
*This is the mechanism everything above was implicitly using, and it is the paper the whole mass reading rests
on.* The slicing operator carries geometries over the substrate: **a geodesic planar section is vacuum; an
offset section — a parallel plane not through the centre — is SdS with $M\neq0$**, and
$2M=\alpha\bigl((r_0/\alpha)-(r_0/\alpha)^3\bigr)$. ***The offset is the mass.*** **And that single
identification is the sharpest thing anyone gets out of this corpus about the asymptotic-mass problem:** an
asymptotic charge is built to measure a property the spacetime *possesses*, read off at its boundary — **but if
the mass IS where the cut sits, there is nothing at infinity to measure.** *The quantity being sought is a
placement of the section, not a content of the geometry.* **The standing difficulty that no conserved charge is
well defined in an asymptotically-de Sitter spacetime is not a gap in the definitions; the constructions differ
over how to subtract a de Sitter background, and on this reading there is no background to subtract.**

**④ `P9`, its range — the Carter constant as the substrate's own symmetry.**
*For anyone whose instinct is that hidden symmetries are where the truth is.* The operator's range runs onto
**Kerr–NUT–(A)dS**, and the Killing–Yano structure that gives Carter his constant is **not imported** — it is
what the substrate carries. **⌗ And the sharpest thing in the paper is a warning about a word:** its
"acceleration" is the **Plebański–Demiański parameter** — a bare accelerating mass with an irremovable conical
strut — *not* the cosmic acceleration, and the two are different objects.

**⑤ `P11` — why and how the cut bends in time.**
*Having seen that matter is a bend, the dynamics is the obvious next question, and P11 is the paper that asks
it.* In the symmetric sector the answer is closed-form and worth stating for its shape:
$\mathrm{d}^2r/\mathrm{d}\tilde\tau^2=rK_G$ — **the rate at which the cut's bend changes in time is the bend
itself**, up to the areal factor, so the cut straightens, is momentarily flat, and bends the other way as the
geometry passes its one sign change. **Then the inhomogeneous case, which is where the paper actually lives** —
the Gowdy sector, free gravitational radiation, and **the wall at which it begins, distinct from the seam**.
*And the standard puzzle it dissolves is one this readership will recognise: **gravitational-wave energy
non-localizability**, which stops being a defect once energy is the Hamiltonian constraint — a local functional
of the leaf's own bend — rather than a charge owed at a boundary.*

**⑥ `P13` → `P14` — the boundary, then what survives it.**
P13 is **four converging routes to one wall**: $\mathfrak{su}(3)\not\subset\mathfrak{so}(5,1)$, so colour is
**not** a realised continuous isometry. *A negative result of unusual quality — it says exactly what the
substrate does and does not force, and it pries apart three operations that sit on top of each other at the
seam.* **Then P14 shows what the wall leaves standing, and it is not small:** a Dirac field on the slicing
curve with $\dim\ker_+=3$, $\dim\ker_-=0$ — **three chiral generations, forced by least-arbitrariness rather
than posited**, protected as a $\gamma^5$-graded index under any deformation preserving the three-wall
structure. **A one-hinge truncation is excluded not as disfavoured but as carrying an unfixed modulus.** **⌗ AND THE SAME CONSTRUCTION, READ IN A GENERAL DIMENSION, SPEAKS ABOUT THE DIMENSION (r2376+c54.10).** *The fold the count reads is $D-1$; the horizon relation collapses to a single multiple-angle only at $D=4$ and $D=5$; and the mass-parity that grades chirality exists only at even $D$.* ⇒ ***four dimensions is the only one carrying both a generation count and a chirality, so three generations and four-dimensional spacetime are one fact in CR read at two ends.*** *At the sector's own altitude — forced within CR, not a proof about the world — and it settles the dimension of the **cut**, never the substrate's, which stays bounded below only.*

**⑦ `p0` — the one scale, and the Standard Model's own shape read off a circle.**
*This is the paper to sit with.* Maximal symmetry worn seven ways, and two of them are the reason to make the
trip. **The gravitational–cosmological–quantum sector spends no free dimensionless constant:** $c$ is the
null-ruling slope, $G$ appears only as $GM/c^2$ with the mass fixed to Nariai by $\Lambda$ —
**$\Lambda G^2M^2/c^4=1/9$** — and $\hbar$ enters only at the branch point, scaled by $\Lambda$ alone.
**And the waist:** the power of a point with respect to it **is the square of the point's height**, so
*Euclid III.36 and the null condition are the same equation, the minus sign in the metric doing all the work* —
which makes the double ruling and the classical power law **one statement, set by $\alpha$ and nothing else**.
Then the line worth the whole section: **$\mathrm{Aut}(A_2)=S_3\times\mathbb Z_2$ factorises because its
factors act on the two things a figure can be to a circle — the three roots are ON the waist, the two rulings
are TANGENT to it.** *A ruling is a line of the substrate, so exchanging them is an isometry: **chirality
descends gauged**. A root labels a different cut, so permuting them is no motion at all: **flavour is global**.*
***The Standard Model's arrangement of a gauged chirality against a global flavour, read as on versus tangent.***

**⑧ `P3`, with `P5` and `P2` beside it — the geometry all of that was read off, and its group.**
**`P5` is the algebraic half and it is the one to put beside p0**, because it does in group terms what §⑦ did in
figure terms: the **description groupoid** — generators, relations, and Schwarzschild as *one member* — with the
partition that matters, ***the invariant de Sitter geometry is the group's $R$-even part and the Schwarzschild
mass its $R$-odd perspectival artefact.*** **That is the shadow-reading in closed form: not a description of a
projection but a projection exhibited, as a group action with an even and an odd part.** *And it supplies the
algebraic content of P3's geometric result — the horizon–singularity asymmetry as a **sweep-pivot artefact** —
so the two hold one dissolution at two levels rather than one citing the other. Its own sharpening is worth
having: $\alpha$ is the **unique chart-invariant quantity** in the groupoid, so any fully invariant
gravitational mass would have to be built from $\alpha$ — **there is no invariant mass because the invariant is
not a mass.***
**Then `P3` itself**: the slicing curve, horizons as its turning points, and **mass as a reading** —
The slicing curve, horizons as its turning points, and **mass as a reading**: $2M=\alpha\sin u\cos^2u$, linear
in $\alpha$ with a dimensionless slicing profile as coefficient, so *"$M$ is not an intrinsic coefficient of a
spacetime; it is the throat radius projected through a turning of the slicing"* — **and the profile's maximum
is the Nariai value, so the largest mass any slicing can carry is set by the throat.** P2 then does the
economical thing: it undoes the standing verdict that the Schwarzschild curvature singularity is an
inextendible boundary **not by any claim about which manifold is fundamental**, but by exhibiting the
continuation that carries the curve through it.

**⑨ `P7`, then `P15` and `P16` — the framework, and what it predicts.**
P7 is the necessary-and-sufficient augmentation and the pole everything feeds. Then the cosmology, and here the
arc's tone changes from structure to consequence: **a geometric expansion rate**, the Hubble tension
resolved **across the low-redshift distance ladder and not by the acoustic angle alone**, and light-element
abundances reproduced from a collapse excursion — deuterium at $D/H\simeq2.5\times10^{-5}$, $Y_p\simeq0.25$.

**⑩ And only now, `P1` and `P4`.**
*Held to the end on purpose.* **P1: no event horizon completes at finite exterior time** — argued from causal
structure alone, needing none of the cosmology, and it is where the programme's whole weight sits. **P4: the
redshift-isotropy floor forces the cosmic foliation empirically**, $\lesssim3\times10^{-6}$ after secondaries.
*Read first, these two are a fight. **Read eighth, they are the two load-bearing legs under a structure the
reader has already found interesting** — and P4's own clause is the one to end on:* **"because the ontology's
necessary half is measured here rather than posited, those dissolutions are not free-standing coherence but
the consequences of a distinction whose foundation the redshift isotropy already forces."**

*(**P6 sits outside the arc and can be read at any point** — it supplies the altitude the whole thing is held
at, and its `prin:reclass` is the test every dissolution above is graded against: **exhibit the projection
under which the appearance arises; do not merely reproduce it, and do not discard it.**)*

### The parallel arc — for a pure mathematician

*The arc above is the theoretical physicist's. **A second one runs alongside it and is less developed**, and it
is worth drawing because the objects it visits are the same objects — met as mathematics rather than as
physics, and in almost the reverse order. **It can be read in parallel, by someone whose interest is the
structure rather than the world**, and it opens somewhere the other cannot: with a theorem from Euclid.*

**Ⓐ Classical plane geometry, and a two-thousand-year-old theorem doing modern work.** *`p0` §sec:power.*
The **power of a point** with respect to a circle — Euclid III.36, Steiner's invariant, $|X|^2-\alpha^2$ — and
the hyperboloid's own equation says that quantity **is the square of the point's height**. So the tangent from
any point runs exactly as far across as the point stands high, and $\mathrm{d}s^2=0$: ***the tangent–secant
relation and the null condition are the same equation, and the only thing turning one into the other is the
minus sign in the metric.*** **Bounded honestly, and the bound is the interesting part: it is a fact about ONE
circle** — a power taken with respect to any other is a perfectly good Euclidean quantity and is not a height,
because the identity *is* the hyperboloid's equation and the hyperboloid has one waist.
*Then the waist keeps paying: it is the **incircle** of an equilateral triangle **and that triangle's nine-point
circle**, so the hinge distance $2\alpha$ is an **output** rather than a stipulation; the triangle's three sides
are null rulings; and $r=0$ sits **on** the circle.*

**Ⓑ Trigonometry that turns out to be forced.** *`P3` `prop:gnomonic`, `prop:triple`.*
The mass–offset relation is $2M=\alpha(u-u^3)$, and under the gnomonic chart it becomes **the pure triple
angle**, $2M=\tfrac{2}{3\sqrt3}\alpha\sin 3w$. **The scale $2/\sqrt3$ is not chosen — it is the unique value
for which the relation is a pure multiple of $\sin 3w$ with no residual $\sin w$ harmonic.** *So the cubic
$r_0-r_0^3$ **is** the cubic in $\sin w$ that the triple-angle identity collapses; and the profile's maximum is
the Nariai configuration, which the identity therefore **returns of its own accord**.*

**Ⓒ Complex analysis: a continuation where the literature has a boundary.** *`P2`.*
The Schwarzschild curvature singularity is standardly an **inextendible** boundary. P2 undoes that verdict
**not by any claim about which manifold is fundamental** but by exhibiting the continuation that carries the
curve through it — *"the reclassification in its most economical form, and a reminder that dissolving a puzzle
by identity need not wait on settling an ontology."* **And the interior cycloid is a closed Friedmann scale
factor**: one homogeneous circle whose two poles are the horizon and the origin.
*With the monodromy that goes with it: $r^3$ has period $2\pi i\alpha/3$, so $r=(r^3)^{1/3}$ lives on the
**three-sheeted cube-root cover** and closes only after $2\pi i\alpha$.*

**Ⓓ Galois theory of a one-parameter family.** *`P5`, and the energy family.*
The turning cubics of the family $r^3+pr+q$, $p=(E^2-1)\alpha^2$, $q=2M\alpha^2$: **the roots are equilateral
iff $p=0$, and — since $p$ is $M$-independent while $q$ is linear in $M$ — the discriminant is a perfect square
in $M$ iff $p=0$ as well. One condition, met at $E=1$ alone.** So at $E<1$ the roots are colinear with **no
symmetry as a figure but full $S_3$ as monodromy of the cover**; at $E=1$ they form the equilateral triangle
carrying **$S_3$ as its own figure symmetry**, monodromy dropping to $\mathbb Z/3$. ***Neither end lacks the
$S_3$; the deformation exchanges the manner in which it is carried — from monodromy of the cover to symmetry of
the figure.*** *And `lem:twoturnings` forbids the shortcut: no affine change of variable identifies the two
threefold symmetries.*

**Ⓔ Root systems, and a factorisation with a geometric reason.** *`p0` §sec:unification.*
$\mathrm{Aut}(A_2)=S_3\times\mathbb Z_2$, and **the factorisation is not formal — its factors act on the two
things a figure can be to a circle.** The three roots are the special points **ON** the waist; the two rulings
are the lines **TANGENT** to it; *on* and *tangent* are independent, so the residue factorises. **And the two
kinds differ for the same reason: a ruling is a line of the substrate, so exchanging them is a motion of it —
an isometry; a root labels a different cut, so permuting them is no motion at all.** *Six Nariai geometries
form the $A_2$ hexad; the three hinges join into one skew hexagon — **resonance with the hexad, not identity.***

**Ⓕ Symmetric spaces, and two real forms of one complex group.** *`p0`, `P13`.*
$\mathrm{dS}_5=SO(5,1)/SO(4,1)$, and the global Wick $x_0\mapsto ix_0$ carries it to the **compact
$S^5=SO(6)/SO(5)$** — **the two real forms of one $SO(6,\mathbb C)$, meeting at the horizon where
$\beta=2\pi\alpha$.** *The Lorentzian form carries the real-geometric gauges, the compact form the thermal
ones; and $\mathfrak{su}(3)\subset\mathfrak{so}(6)$ while $\mathfrak{su}(3)\not\subset\mathfrak{so}(5)$,
which is the whole colour boundary in one containment.*

**Ⓖ Lie algebroids — where the physicist's arc began.** *`P12`.*
The hypersurface-deformation algebra's structure function makes it **not a Lie algebra**; read as a **Lie
algebroid** over the space of cuts, the anchor is the ADM data and **the symmetric-space grading is that algebra
term for term.** *This is station ① of the other arc, reached here from the opposite end.*

**Ⓗ An index theorem, as the destination rather than the entrance.** *`P14`.*
A Dirac field on the slicing curve: $\dim\ker_+=3$, $\dim\ker_-=0$, **a $\gamma^5$-graded index protected
under any deformation preserving the three-wall structure**. *The count is topological; what makes it three is
the substrate's own three-foldness, and a one-hinge truncation is excluded because it carries an unfixed
modulus.*

**⌗ The two arcs meet at `p0` and `P12` and run in opposite directions** — the physicist enters at the algebroid
and arrives at Euclid; the mathematician enters at Euclid and arrives at the algebroid. **Neither is the reading
order** *(that is `README` steps 3–6, the causal spine)*, and neither is the doors. **Three orderings, three
purposes: what is FORCED, what INTERESTS, and what is STRUCTURALLY DEEP.**

**The corpus takes any number of approaches** — which is a property of a structure read many ways rather than
an accident of arrangement, and the matrix is how you find your own way in.

## 3 · The scope — what is claimed, and at what weight

**The register.** Most of what the corpus establishes is **coherence, not correspondence**: the structures are
forced *within* CR, and self-consistency is not soundness. That distinction is load-bearing throughout, and the
discipline it rests on is P6 rather than a preface.

**What is settled.** The forcing arguments; the substrate's geometry and its slicing structure; the operator's
range; the constraint algebra's identification; three chiral generations on the discrete residue; the expansion
history; the cosmogenesis synthesis with the light-element abundances reproduced. On the observational axis the
programme has crossed **from coherence to empirically favoured**: the Hubble tension is resolved across the
low-redshift distance ladder, and not by the acoustic angle alone.

**What is open — five families, and they are named rather than implied.** The inherited datum ·
the scalar-perturbation sector to a verdict · **the propagating fermion sector**, which is the largest
undertaking and the gate the others wait on · the world-correspondence · and the interacting quantum tower,
which is not CR-specific. **Two families have left this list since it was written, and a list that shrinks and
says why is worth more than one that was always right**: the *matter branch-point crossing dynamics* closed at
r2376+c54.113 and the *irreducible interior reassignments* at c54.118.

**What would decide it.** Two things are held out to the world rather than argued: **no event horizon completes
at finite exterior time** — structural, resting on causal structure alone, and where the programme's whole
weight sits; and **the geometric expansion rate**, the nearest-term discriminator on expansion-history
data.

**And one thing that must always remain a conjecture:** that the framework the corpus has uncovered is the
framework our actual universe rides. No amount of internal coherence converts it. Empirical facts are primary,
and the work proceeds within those bounds.

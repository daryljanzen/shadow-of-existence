# Pivot–Slicing Geometry — Working Plan
> **⌖ RETIRED r1509 — verified landed before moving.** This planned the pivot–slicing geometry. **Landed:** P3 `SdS-slicing-curve_v2` exists and compiles.
> Kept as record; **do not plan from it.** Its numbering and era predate the current corpus.



*Status: exploratory. Nothing here is baked into the corpus. This is the map we adjust as we go.*
*Convention: each item carries a GOAL, the concrete COMPUTE/PROVE, a STATUS, DEPENDS-ON, and DONE-WHEN.*

---

## 0. The picture in one paragraph (so we don't lose the thread)

One de Sitter hyperboloid (the substrate). A slicing = a planar cut. Spinning the cut about a
pivot pin organizes a whole family by **pivot direction**: cut through the axis → de Sitter /
Schwarzschild (the two *vantages* of one slice, the π-flip: up-the-trunk = cosmos, down-the-hole =
hole); cut tangent to the throat → **Nariai** (which itself forks into a hole-voicing and *the*
cosmology); cut perpendicular (spacelike-constant, past the throat) → **H³**, hyperbolic 3-space.
The areal radius reads off the radial–temporal plane via **X₁²−X₀² = α²−r²**: r=α is the null
cone (the "X", the de Sitter horizon), r=0 is the centre hyperbola on the back side, reached by conjugating around the throat.
The black-hole front reading and the FLRW-cosmology back reading are the two vantages of the same SdS
cut (P7). The gift on the table: **S³(+), flat seam(0), H³(−) are the three constant-curvature
spatial sections of the one substrate, selected by pivot direction.**

---

## ★ FINDING (c23, this session, r407) — Aut(A₂) REALIZED GEOMETRICALLY in the pivot+ruling frame. NOT BAKED.

Prompted by Daryl's realization: the **double ruling** was the missing half of his picture (he'd gridded the
horn with circles only), and the three special points sit at **120°**. Computed this session:

- **S₃ = Weyl(A₂) on the sky circle (SOLID).** The three roots of the horizon cubic $r^3-r+2M=0$ are
  *exactly* 120° apart in the Viète angle: $r_k=(2/\sqrt3)\cos(\varphi-120^\circ k)$, amplitude $2/\sqrt3$
  = the pin radius / gnomonic scale. Reconstructed exactly from one angle + two 120° steps. The ℤ₃ (three
  roots = three descriptions of one mass) + the involution $w\leftrightarrow\pi/3-w$ (reflection about Nariai
  $w=\pi/6$) = **S₃**. The "three special points pivoting" are the three Viète roots; the third is forced.
- **ℤ₂ (diagram automorphism) = the double-ruling swap = the chirality (LOCKED mod one formality).** The
  one-sheeted substrate is doubly ruled by null generators. Computed iff: **swap-of-rulings ⟺ orientation-
  reversing (det −1)** — verified across the isometry zoo (rotations/boosts PRESERVE, det +1; every single
  reflection SWAPS, det −1; composites by det; no orientation-reversing isometry preserves). The reticle
  reflection $r_0\mapsto-r_0$ is orientation-reversing (O(5,1)∖SO₀, algebroid §7), flips $2M$ (the
  mass-reflection / A₂ diagram automorphism), and is the orientation parity that surfaces as the graviton
  chirality (r400). Orientation-reversing + the iff ⟹ **$r_0\mapsto-r_0$ swaps the rulings.**
- **TOGETHER: Aut(A₂) = S₃ × ℤ₂, in the pivot+ruling frame** — S₃ from the three 120° pins + Nariai
  reflection, ℤ₂ from the ruling-swap, the ℤ₂ factor being the **disconnected** orientation parity the
  chirality lives in (the r400 connected/disconnected mechanism). Unifies the pivot geometry (P3/P4), the
  A₂ skeleton (P12), and the chirality nugget into one object.

**LOCK STATUS: CLOSED (r408).** Explicit O(5,1) matrix exhibited: the reticle reflection is
$R=\mathrm{diag}(1,1,-1,1,1,1)$ (reflect the transverse aim direction X₂, since $r_0=(2/\sqrt3)\sin w$ is
the aim's transverse component). Verified: (i) isometry $R^\top\eta R=\eta$; (ii) $\det R=-1$ (O(5,1)∖SO₀,
matches algebroid §7); (iii) $\det=-1$ on the ruled (X₀,X₁,X₂) block *specifically* (the residual now
closed — orientation-reversing THERE, not just globally); (iv) maps ruling A → ruling B (SWAPS); (v)
$r_0\mapsto-r_0$ hence $2M\mapsto-2M$. So the double-ruling swap = orientation parity = A₂ diagram
automorphism = graviton chirality, and **Aut(A₂)=S₃×ℤ₂ realized geometrically is a THEOREM** (reduced ruled
picture). **BAKED (r409).** Landed lean, each piece where it is load-bearing: (a) the $\mathbb{Z}_2$=ruling-swap geometric realization + the $S_3$ 120° sharpening + the full $\mathrm{Aut}(A_2)=S_3\times\mathbb{Z}_2$ assembly → **P12** (algebroid, §discrete tail), with the explicit $R=\mathrm{diag}(1,1,-1,1,1,1)$; (b) the A coherence fix (P3 seam "signature flip" disambiguated as the slicing-surface 2-metric / the vantage, not the spacetime signature) → **P3**; (c) B was already baked in **P13** (the three-op taxonomy, line ~83, with the seam flip already stated as a *single slicing curve*) — added the throat-machinery cite to P3. C: framework indefinitely parked, no action. Compiles clean, 0 undefined.

---

## 1. What is solid (grounded/computed this session)

- **Embedding dictionary** (exact): X₁²−X₀² = α²−r². de Sitter horizon r=α ↔ null cone X₀=±X₁; r=0 ↔ centre
  hyperbola X₁²−X₀²=α²; 0<r<α spacelike wedge; r>α timelike (cosmological) wedge.
- **r=0 is a real curvature singularity for every M≠0** (under/Nariai/over alike; Kretschmann 48M²/r⁶
  from the 2M/r term); only M=0 (de Sitter) lacks it. [matches P7 §CR-SdS]
- **The pin / √3 family:** pin radius b = 2α/√3 (= the gnomonic image scale, forced by the
  triple-angle); pierce height T = √(b²−1) = α/√3 = the Nariai radius; observer ρ = √3α/2 = α/b.
- **Closest-point invariant:** slicing-curve vertex (nearest point to the hole) at (X₀,ρ)=(√(d²−1),d)
  migrates from the tangent point (Nariai, d=α) to the pin pierce point (perpendicular, d=b) as d:α→b.
- **Perpendicular slice = H³:** X₁=b>α cuts a two-sheeted hyperboloid, induced metric hyperbolic
  3-space, radius √(b²−1)=α/√3, sectional curvature −1/(b²−1). [new — see §4.3]
- **FLRW = backside of SdS:** the timelike-r (f<0) vantage of the SdS cut is the expanding cosmology;
  the physical case is Nariai (P7 §131, "the cosmological case is the Nariai configuration").
- **Discriminant identity:** the quadratic-factor discriminant is D = 4−3r₀² = **4cos²w** (gnomonic
  scale r₀=(2/√3)sin w). So the overcritical onset / H³ slice is forced to the perpendicular look
  w=π/2; the involution w↔π/3−w fixes Nariai (w=π/6). Two distinguished angles, π/6 and π/2.

## 2. New vs re-derived (keep this honest)

- **Re-derived (already in corpus, now better charted):** slicing curve, sweep-pivot, involution,
  overcritical continuation (P3); vantage fork (P5); FLRW-as-backside, Nariai-as-cosmology (P7);
  dS↔Schwarzschild "π pivot" = Prop r0zero's two readings of the r₀=0 slice.
- **New (not written down before):** (a) the perpendicular slice is H³; (b) S³/flat/H³ as one
  pivot-family on the substrate; (c) the closest-point invariant as the organizing quantity;
  (d) the H³ radius landing on the Nariai number.

## 3. Guardrails (the collapses we must not make)

- **H³ is not Lorentzian AdS₄.** The pivot gives the negative-curvature *spatial* section (Riemannian
  H³). AdS₄ needs two times (𝕄^{2,3}); the one-time dS substrate cannot contain it. Never write
  "AdS₄ is a slicing of dS₄."
- **dS₅ substrate ≠ dS₄ background.** Slicing operator acts on the substrate; causal reassignment on
  the background. Do not call the background a substrate.
- **a=0 (finite cosmogenetic seam) ≠ r=0 (infinite centre).** The Big Bang is the finite-curvature
  seam where the comoving ruler collapses; r=0 is the real-infinite never-actualised endpoint,
  conjugate to it. Both real; different loci.
- **The vantage changes the causal role, not the reality of r=0** (P7 §CR-SdS).

---

## 4. Work plan (sequenced; adjust freely)

### Phase A — Foundation: the chart (consolidate what's solid)

**A.1 Embedding-dictionary note. — RESOLVED (r377).** The dictionary X₁²−X₀²=α²−r² with the
throat/centre/wedge table is written in `PIVOT_EMBEDDING_FOUNDATION.md` §1 (confirmed not stated as
such elsewhere in the corpus). Backs P5 §trichotomy and the slicing-curve geometry.

**A.2 Closest-point invariant — proposition. — RESOLVED (r377).** Stated and proved as a lemma in
`PIVOT_EMBEDDING_FOUNDATION.md` §2: the slicing-plane vertex (closest approach to the throat) at
(√(d²−α²), d), migrating tangent-point (d=α, Nariai) → pin (d=b). Scaffolding, not load-bearing
beyond P3/P5; kept as the geometric foundation.

### Phase B — The parametrization: one knob for the whole family

**B.1 Pivot → sky-angle map (the "factor").** — RESOLVED (corrective).
FINDING: there is no single pivot angle carrying the whole family; the "spin" conflated **three
distinct structures**: (i) the **vantage fork** (dS↔Schwarzschild) — two *readings* of one slice
(r₀=0, P3 Prop r0zero), the π-flip of looking direction, not a motion in w; (ii) the **root
involution** w↔π/3−w (P3 §involution), swapping dS (w=0) ↔ throat-tangent (w=π/3), **fixed point
Nariai (w=π/6)**; (iii) the **overcritical boundary**, where H³ lives (see D.1). The clean "dS/Sch/AdS
at 0/π/(π/2), AdS self-dual" picture does not survive: the self-complementary slicing is **Nariai**,
not AdS. DONE.

**B.2 Where the named limits land.** — RESOLVED.
The real chart is w∈[0,π/3], r₀=(2/√3)sin w: dS(0) → Nariai(π/6) → throat-tangent(π/3); the
perpendicular look w=π/2 (r₀=2/√3) is the family's edge. Two distinguished angles, not one:
**w=π/6** = geometric Nariai (r₀=r_B, crest of sin3w, involution fixed point, the cosmology);
**w=π/2** = overcritical onset (r_B=r_A′), perpendicular look, the H³ slice. dS↔Sch is the vantage
fork (same slice), not a w-pairing. DONE.

### Phase C — The new result: H³ in the family

**C.1 H³ proposition.**
GOAL: the perpendicular slice X₁=b>α is H³, radius √(b²−α²), curvature −1/(b²−α²).
COMPUTE: induced metric on the two-sheeted slice; curvature in physical units; the S³/flat/H³ trichotomy
as constant-spacelike / null / constant-spacelike-past-throat cuts.
STATUS: computed in gauge; needs physical-unit curvature + clean proof. DEPENDS-ON: A.1.
DONE-WHEN: a proposition with the three constant-curvature sections as one corollary.

**C.2 The signature wall, stated.**
GOAL: record why this is spatial H³, not AdS₄ (one-time substrate; AdS₄ needs 𝕄^{2,3}).
STATUS: argued; needs one clean paragraph. DEPENDS-ON: C.1. DONE-WHEN: written as the scope limit of C.1.

### Phase D — The deep question

**D.1 Why does H³ sit at the Nariai radius / the overcritical onset?** — RESOLVED: FORCED.
MECHANISM: with the forced gnomonic scale r₀=(2/√3)sin w, the quadratic-factor discriminant is
**D = 4 − 3r₀² = 4cos²w** exactly. So D=0 only at **w=π/2 (cos w=0), the perpendicular look** — the
overcritical onset, r₀=2/√3 = the pin radius = the gnomonic scale. The H³ slice's radius √(b²−1)=1/√3
follows from b=2/√3, which is why it equals the Nariai horizon number. No free choice in the chain:
triple-angle → scale 2/√3 → D=4cos²w → perpendicular = discriminant-zero. The negative-curvature slice
sits at the overcritical onset *because* looking perpendicular is where the two horizons collide and go
complex. DONE. DEPENDS-ON: B.1. (Caveat held: this is the H³ *placement* in the family; the H³
*geometry* proof is C.1, and the spatial-not-AdS₄ wall is C.2.)

### Phase E — Coherence + write-up (only after the above)

**E.1 Cohere with P2/P3/P5/P7/groupoid/algebroid.**
GOAL: confirm the pivot family sits inside the existing structure with no contradiction.
STATUS: ongoing discipline. DONE-WHEN: each new proposition cross-checked against the named papers.

**E.2 Decide the home.**
GOAL: does this extend P3 (a new section), or is it its own short note?
STATUS: defer until C/D land. DONE-WHEN: Daryl calls it.

---

## 4b. Ripples into the groupoid and algebroid (this session)

**Groupoid — H³/overcritical-onset is a reflection axis of the S₃ (GROUNDED).**
Within-geometry morphisms generated by σ (root-exchange, w↦π/3−w) and τ (sky-angle periodicity,
order 3); ⟨σ,τ⟩=D₃≅S₃ (groupoid_paper §generators). The three transposition reflection axes are
w=π/6, π/2, 5π/6. So **w=π/6 (σ axis) = Nariai** (the established branch point of the 3-sheeted cover)
and **w=π/2 (στ² axis) = the overcritical onset / H³** (where D=4cos²w vanishes). The new distinguished
angle is a fixed point of a groupoid transposition — part of the established discrete skeleton, and the
locus where the groupoid paper's deck S₃ drops to its order-2 subgroup in the overcritical regime.

**Algebroid — H³ lives in the substrate, no dimensional rise (GROUNDED).**
H³ = SO(3,1)/SO(3), SO(3,1)⊂SO(5,1), so the negative-curvature slice is reachable within dS₅ alongside
S³=SO(4)/SO(3). Consistent with algebroid_paper's stance (no continuous 𝔰𝔲(3), no forced 6D rise;
SU(3)⊄SO(5)). H³ does not push the dimension.

**RESOLVED — no third symmetric stratum; w=π/2 is the negative-mass Nariai.**
The w=π/2 *slicing* has 2M=−2/(3√3), double root at r=−1/√3, cubic discriminant zero — the SAME Nariai
seam as w=π/6, mirrored by r↦−r (roots {+1/√3,+1/√3,−2/√3}↔{−1/√3,−1/√3,+2/√3}). Same dS₂×S²,
same isotropy SO(2,1)×SO(3) (dim 6). It is the ℤ₂ mass-reflection image of Nariai — the ℤ₂ already in
Aut(A₂)=S₃×ℤ₂≅D₆. So algebroid_paper's "symmetric grading at Type O and Nariai only" stands.

**RESOLVED — the three S₃ axes are all Nariai loci, not the three curvatures.**
w=π/6 and 5π/6 are +Nariai; w=π/2 is −Nariai. They are the ±mass double-root loci, not S³/flat/H³.

**THE DISTINCTION (the real catch).** The w=π/2 *slicing* (4D, negative-mass Nariai, dS₂×S², an
algebroid stratum) and the w=π/2 *perpendicular spatial cut* ({X₁=2/√3}, 3D, H³, the negative-curvature
member of the spatial trichotomy) are TWO DIFFERENT OBJECTS sharing the number 2/√3. So three genuinely
distinct layers, not one: (i) the algebroid's 4D strata; (ii) the S₃ permuting the three horizons of a
fixed cubic (axes = ±Nariai); (iii) the spatial-curvature trichotomy S³/flat/H³. They meet at 2/√3
because the gnomonic scale appears in all three — a coincidence of scale, not a single underlying object.
H³ is spatial-section structure, NOT a stratum and NOT a horizon fixed point.

**P5 (slicing operator) — the open FLRW slicing, the missing third leaf (GROUNDED).**
The H³ leaf stacks into a genuine cosmology: the open-slicing embedding (X₁=cosh τ, X₀=sinh τ cosh ρ,
X_{2,3,4}=sinh τ · H³ directions) lies on the dS hyperboloid and induces, verified symbolically,
**ds² = −dτ² + sinh²(τ) dH₃²** — the open (k=−1) FLRW slicing of de Sitter, τ timelike, H³ spatial.
The perpendicular cut {X₁=2/√3} is its leaf at τ=arccosh(2/√3), radius 1/√3. So P5's cosmological
sector completes: closed (−dT²+cosh²T dS₃²), flat (E=1, sinh^{2/3} ΛCDM), **open (−dτ²+sinh²τ dH₃²)**
— the three constant-curvature FLRW slicings (k=+1/0/−1 ↔ S³/E³/H³) of the one substrate, by which
structure the comoving frame synchronizes to (timelike vertical / null ruling / perpendicular).
P5 §cosmology writes only closed and flat ("flat ΛCDM, not the closed cosh"); this is the third.
SCOPE/OPEN: this is the *empty* (M=0) open de Sitter. P5's flat E=1 carries dust (M≠0, the bend).
The matter-filled open case — open ΛCDM via the bend — is the follow-on COMPUTE.
**RESOLVED (matter-filled open ΛCDM).** P5's bend=density is the Hamiltonian constraint
16πρ=³R+K²−K_ijK^ij−2Λ, which for any FLRW leaf gives (ȧ/a)²=(8π/3)ρ−k/a²+Λ/3, the curvature term
= the leaf's own ³R=6k/a². The comoving frame is the SdS radial geodesics r=a: (da/dτ)²=(E²−1)+2M/a+a²/α²,
matching Friedmann with −k=E²−1, dust 2M/a, Λ=3/α². So the three curvatures are three energies of ONE
SdS congruence — E<1 closed (S³), E=1 flat (E³, P5's sinh^{2/3}), E>1 open (H³, k=−1 at E=√2) — same
dust M, same Λ, only E differs. Open ΛCDM is the E>1 member, fully matter-filled, by P5's exact mechanism.
P5's cosmological sector is complete across all three FLRW curvatures; flat is the marginal (E=1) physical
member, open/closed the substrate's other available slicings.
RIPPLES to P6 (minor: open FLRW is Type O, swept by SO(3,1)⊂SO(5,1), within the established range —
the three FLRW curvatures = three sweep-subgroups SO(4)/E(3)/SO(3,1)); P9 (none: H³ is vacuum, no bend).

## 5. Loose ends (tracked, not forgotten)

- **r374 note correction (RESOLVED r375).** The CMB note's r=0 treatment is corrected: r=0 is a real
  infinite-curvature singularity for every M≠0 (P7 §479, Kretschmann 48M²/r⁶), character *fixed* (not
  reading-dependent); the sweep/reading sets only its reachability (never reached in the interior reading;
  the beginning is the finite seam, P7 §665) and causal role. The "coordinate singularity in the τ-χ chart"
  claim removed; substrate-extendibility kept as a distinct compatible fact. Baked into the CMB note +
  CORPUS_MAP r375 changelog; shipped in the r375 bundle.
- **Observer 2′ (RESOLVED r378).** The pin pierces at r=0 (the comoving geodesic p's worldline); its
  two ends (±T) are p's future/past, one observer — not two. **Observer 2 = the pin = p; observer 2′ =
  the antipode −p = the opposite-side pin** (X₁=−b), sharing the unoriented bifurcate horizon (P7 §665).
  Observer 1 = the read direction (the vantage fork), not a third point. Full set = the waist S³ of
  comoving geodesics. The "lost transcript" content was already compiled into P7's NBC machinery; no
  transcript needed. Recorded in `PIVOT_EMBEDDING_FOUNDATION.md` §4. This clears the foundation for the
  chirality chase (the handedness reversal past the H³ reflection locus d=b).
- **Chirality located (RESOLVED-AS-LOCATED r379).** The handedness flip past d=b (φ↔π−φ, related by
  X₂↦−X₂ fixing p) is a **mirror the geometry identifies** in the spherically-symmetric sector: the
  swept SO(3) supplies an orientation-preserving completion (the (X₂,X₃) π-rotation) that undoes it —
  across undercritical/Nariai/overcritical alike. **Genuine chirality lives where that isometry is lost
  — the wall** (P6: loss of continuous symmetry = onset of free radiation; the type-N two transverse
  polarizations ARE the handedness; P5 §open: "the loss of the last isometry is precisely the point at
  which the wave's polarization must turn from place to place"). The seam/Nariai (inner) and the wall
  (outer) are the two ends of P6's null-degeneracy axis; the H³ locus is where the mirror is exact, the
  wall where it can't be taken. Recorded in `PIVOT_EMBEDDING_FOUNDATION.md` §5.

## 5b. CHIRALITY — computed and located; one clean sub-question open

**Done (r379–r381).** Chirality = the turning of the polarization plane; handedness = ℤ₂ sign of
d/du arg(h₊+ih_×), helicity ±2 (§6, computed on the Type-N wall geometry). The helicity ℤ₂ is the
**substrate spatial parity O(5,1)/SO₀(5,1)** (§7), outside the connected SO₀(5,1) the algebroid acts by,
distinct from the Weyl S₃. Onset = the loss of the swept SO(3) (Type D→I): the unpolarized turning Gowdy
is the first chiral case, the wall is the generic locus. Visible in a parity-odd invariant at Type I;
non-polynomial (VSI) at the wall. P9 §discrete augmented (not rewritten): the radiating sector carries the
substrate-parity ℤ₂ as the helicity.

**RESOLVED (r384, via Daryl's pointer to P8+P1+P7): the helicity ℤ₂ and the Aut(A₂) mass-reflection ℤ₂
COINCIDE — one substrate-orientation parity O(5,1)/SO₀(5,1).** The mass-reflection P is the celestial
reflection w↦−w (r₀↦−r₀; r₀=(2/√3)sin w), a substrate isometry (orientation-reversing), inducing r↦−r on
the roots, connecting +M/−M across the SO₀-orbits (the connected action can't; a reflection can). The
+M/−M non-isometry (r382's basis) is at the level of the Lorentzian RECORD M — the perspectival/gauge
shadow — not the existent. P8's existence/occurrence ontology fixes the existent as the de Sitter substrate
(+ layer), M its shadow; granting the records existence is the block-universe category error P8 dissolves
(exactly r382's error). P1 (horizon/r=0 metric singularities of the record, collapse never completes) and
P7 (r=0 real-but-never-actualised, NBC causal-reading gauge) supply the pieces. So Aut(A₂)=S₃×ℤ₂ has its
ℤ₂ = the substrate orientation = the helicity = the chirality at the wall: ONE parity, three guises
(mass-sign in the symmetric record, helicity in the radiating sector, the un-undoable chirality past the
wall). Daryl's original "one parity threading both sectors" confirmed; the warrant is the existence/
occurrence ontology. Recorded in `PIVOT_EMBEDDING_FOUNDATION.md` §7 (supersedes r382 distinct / r383
undecided). Holds on CR's ontology; a block-universe reading would split them — the one stance CR rejects
on independent grounds (CMB rest frame + occurrence/existence, P8 §necessity).

**Chirality programme: COMPLETE at the kinematic/discrete level.** Located (§5), computed (§6), the ℤ₂
identified and separated from the cubic's discrete symmetry (§7). What remains is dynamical, not
classificatory: the actual evolution of a turning-polarization (unpolarized, chiral) wave — P9's confined
Hamiltonian extended to two coupled polarizations, the genuinely inhomogeneous regime past the wall — which
P9 §scope already names as the open dynamical frontier of the whole programme.

## 6. Standing principle

Nothing baked into the corpus until proven *and* confirmed. Daryl drives the sequence; small steps;
each computation grounded, not reasoned-from-model. The plan is adjustable — reorder freely.

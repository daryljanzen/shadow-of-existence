# c17 fork — working notes: the A2/S3 as a theorem about the slicing/solution space
Forked from r309. One node of four (c17/c19/c20/c21) running in parallel until cold reads.
Goal (c19's reach, source-grounded last turn): make the A2/S3 a **theorem about the
gravitational-cosmological solution space** — not a colour structure. The gem is the SdS
horizon triplet; formalize it with the consolidated machinery (P5/P6 slicing, P1 interior-
as-cosmology, P9 dynamics, P10 algebroid).

Discipline: source first (thesis at resources/PhD_thesis/), compute don't assert, hold the
verdict-bar both ways, mark grounded vs conjecture. Stated for reversal throughout.

## Source groundings (thesis, verified at source)
- Metric (Eq. SdS_statical_pure, chap4): ds^2 = -(r/N)dr^2 + (N/r)dt^2 + r^2 dOmega^2,
  N(r) = r^3 - r0^3 - (r - r0).  g_tt = N/r  => sign(N) is the signature (r timelike/spacelike).
- Horizon cubic (Eq. horizon_eq): r^3 - r0^3 - (r-r0) = 0.
- Fundamental ellipse (Eq. SdS_ellipse): r^2 + r*r0 + r0^2 = 1.
- Mass (line 80): 2M ≡ r0 - r0^3.  alpha = sqrt(3/Λ) = 1 (scale-invariant units).
- Horizon interchangeability (line 78): the three roots "form one triplet — a given value of
  any one unambiguously fixes the other two"; the geometry at any one horizon value is
  "precisely the same" as at the other two => S3 permutes interchangeable descriptions of ONE
  rigid geometry.

=================================================================================
## r309_c17fork_1 — RESULT: the SdS solution space carries an exact A2 root-system structure
(receipt: scripts/a2_solution_space.py, run clean)

GROUNDED (computed):
1. N(r) = r^3 - r + 2M  (2M = r0 - r0^3). No r^2 term => the three horizons sum to zero:
   r1 + r2 + r3 = 0.  This is the **Cartan / traceless condition**, exactly.
2. Vieta (exact, remainder 0): dividing N by (r - r0) gives r^2 + r*r0 + r0^2 - 1, so the two
   non-r0 horizons lie EXACTLY on the fundamental ellipse r^2 + r*r0 + r0^2 = 1.
3. The fundamental ellipse IS the A2 quadratic form: restricting the root-space metric
   sum r_i^2 to the traceless plane r1+r2+r3=0 gives 2*(r1^2 + r1 r2 + r2^2) — the ellipse
   form x^2+xy+y^2. Gram [[1,1/2],[1/2,1]] eigenvalues 1/2, 3/2 (the A2 ratio 1:3).
4. S3 = Weyl(A2): permuting the three horizons leaves (e1,e2,e3)=(0,-1,-2M) invariant =>
   same cubic, same M, same rigid geometry. The horizon triplet is one S3-orbit.
5. Physical map (M=0.1): horizons {-1.088 (inner/negative), 0.209 (black-hole), 0.879
   (cosmological)}, sum 0. The S3-orbit connects inner <-> black-hole <-> cosmological:
   three horizon-faces of ONE geometry.

THE CLAIM (theorem foundation, stated for reversal):
   The SdS solution space carries an exact A2 root-system structure. The three horizons of a
   given geometry ARE the three coordinates of a point in the A2 root space (the traceless
   plane); the fundamental ellipse IS the A2 quadratic form (the root-space metric restricted
   to that plane); and S3 = Weyl(A2) permutes the horizons as interchangeable descriptions of
   one rigid geometry. This is the discrete symmetry of the gravitational-cosmological
   SOLUTION SPACE (the cut/horizon structure), realized exactly — not a skeleton, not internal.

This upgrades the corpus's "genuine A2 gem (C6)" from "discrete A2 root-system structure in the
vantage groupoid" to the exact, physical realization: horizon-triplet = root-space point,
ellipse = root-space metric (via Vieta), S3 = horizon-permutation = solution-space symmetry.

[REACH] — next bites for the grind (NOT yet established):
- (A) The UNIFICATION made precise: how the S3-orbit + the (r,r0)-plane chambers connect
  black-hole / cosmology(over-critical, r=cosmic time) / negative-mass as one A2 object.
  The signature chambers (sign N) should be the Weyl chambers of the A2 form — test it.
- (B) The SLICING-OPERATOR connection (the real theorem target): the three horizons are the
  slicing operator's cut parameters; is S3 the symmetry of how the CUTS interchange, i.e. does
  the horizon-permutation S3 lift to an action on the slicing CURVES / cuts themselves
  (P5/P6), not just the horizon labels? If yes, the A2/S3 is a symmetry of the cut-structure.
- (C) Tie to P10 (algebroid connection over the cut-space C) and P1 (interior-as-cosmology,
  r as cosmic time) — the dynamical reading of the S3-orbit.

NEXT: bite (A) — test whether sign(N) chambers in the (r,r0) plane are the A2 Weyl chambers,
and pin the over-critical (r=cosmic-time) face of the orbit. Then (B), the slicing lift.

=================================================================================
## r309_c17fork_2 — RESULT (bite A): the A2 Weyl-wall structure IS the regime boundary
(receipt: scripts/a2_weyl_chambers_regimes.py, run clean)

GROUNDED (computed):
1. Discriminant of the horizon cubic r^3 - r + 2M:  Delta = 4 - 108 M^2, and Delta = prod_{i<j}
   (r_i - r_j)^2 (verified numerically at M=0.1: 2.920 = 2.920). Delta is the A2
   Weyl/Vandermonde invariant — it vanishes exactly when two horizons collide (a Weyl WALL).
2. Regime map = discriminant-sign chambers of the A2 structure:
     Delta>0 (|M|<1/sqrt27): three real horizons, full real A2 triplet  -> BLACK HOLE
     Delta=0 (|M|=1/sqrt27): repeated root, ON a Weyl wall              -> NARIAI / critical
     Delta<0 (|M|>1/sqrt27): one real + complex pair, triplet complexified -> COSMOLOGY (r=cosmic time)
3. Signature sign(N), N=r^3-r+2M, g_tt=N/r (and N/r = -f(r) for standard SdS f):
     N>0 => r TIMELIKE (cosmic-time region) ; N<0 => r SPACELIKE (static region).
   Under-critical sign pattern on r>0 is [+,-,-,+] across the two positive horizons:
     - r < r_BH  : N>0, r=cosmic time  => the BLACK-HOLE INTERIOR is a cosmology (P1, interior-as-cosmology)
     - r_BH<r<r_cosmo : N<0, static    => the ordinary static exterior
     - r > r_cosmo : N>0, r=cosmic time
   Over-critical: N>0 for ALL r>0 (no horizons) => PURE cosmology, r=cosmic time throughout (thesis line 72).
   [self-correction vs the script's printed line: the cosmic-time region is the interior r<r_BH,
    NOT "between horizons"; between the horizons is the static region. Computation unaffected.]
4. Negative mass: 2M(r0)=r0-r0^3 is ODD, so r0->-r0 sends M->-M (thesis line 78 "reflections about
   r=0"). Negative mass is the Z2 reflection r->-r of the positive-mass A2 orbit; the full discrete
   symmetry of the solution space contains S3 x Z2.

THE CLAIM (theorem, second course, stated for reversal):
   The A2 discriminant (the Weyl-invariant of the horizon triplet) organizes the SdS solution space
   into black-hole (Delta>0) | Nariai (Delta=0, on a Weyl wall) | cosmology (Delta<0), with the
   negative-mass sector the Z2 reflection. The Weyl walls ARE the Nariai/critical loci; crossing one
   (M past 1/sqrt27) merges the horizons and turns the interior-cosmology into the whole universe —
   "interior-becomes-cosmology" is geometrically the crossing of an A2 Weyl wall. This makes c19's
   reach precise: black-hole / Nariai / cosmology / negative-mass are the discriminant-chambers +
   Z2 of ONE A2 object — the gravitational-cosmological solution space. It ties P1 (interior-as-
   cosmology), the range/Nariai seam (P5/P6; Beyer's Nariai = the boundary CR isolates), and the
   over-critical cosmology (r=cosmic time) into one A2 picture.

[REACH] next bites:
- (B) THE THEOREM TARGET — the slicing lift: does the horizon-permutation S3 lift to an action on
  the slicing CUTS themselves (P5/P6), i.e. is S3 a symmetry of the cut-structure, not just the
  horizon labels? That is what would make "A2/S3 = symmetry of the solution space" a theorem about
  the slicing operator rather than about the cubic.
- (C) tie-back to the sigma/pivot structure [hold not claimed, possible flavor-match]: the
  over-critical COMPLEXIFICATION of two horizons (the complex pair) lives in the imaginary direction
  — is it the SAME x0->ix0 Wick/pivot complexification that the inter-face seam realizes? If so the
  signature seam (fork-1/c19) and the Nariai Weyl-wall (here) are two views of one A2 structure.
  Flagged, NOT asserted — exactly the face-19 spot.

=================================================================================
## r309_c17fork_3 — RESULT (bite B, THE THEOREM TARGET): S3 lifts to the slicing CUTS
(receipt: scripts/a2_slicing_cut_lift.py, run clean; source: P3 SdS-slicing-curve_v2.tex, P5 slicing_operator.tex)

SOURCE (read at P3/P5, not modelled):
- The slicing operator generates SdS by an OFFSET PLANAR CUT of the dS hyperboloid; "the offset
  IS the mass," 2M=r0-r0^3 (slicing_operator sec:dictionary; P3 sec:mass). The horizon locus is
  "the shadow of a planar cut of a quadric."
- The cut's own parameter is the OBSERVER'S SKY ANGLE w (a genuine geometric angle), offset
  r0=(2/sqrt3) sin w, forced by the gnomonic projection (P3 abstract). The cut->geometry map is
  the PURE TRIPLE-ANGLE 2M=(2/(3 sqrt3)) sin 3w.
- The parameter map carrying one root to another is an explicit INVOLUTION f(r0)=1/2(-r0+
  sqrt(4-3 r0^2)), f(f(r0))=r0, fixed point r0=1/sqrt3 (Nariai), de Sitter<->Nariai exchanged at
  its endpoints (P3 abstract).

GROUNDED (computed, scripts/a2_slicing_cut_lift.py):
1. Factorisation (r-r0)(r^2+r r0+r0^2-1)=0 (matches P3).  [True]
2. f(r0) solves the quadratic factor; f(f(r0))=r0 numerically across generic r0 (the involution;
   sympy won't close the nested radical, r0=-1 a branch-label edge -- suspect the symbolic check,
   not P3); fixed point r0=1/sqrt3 = Nariai (w=pi/6).  f(r0) lands on ANOTHER horizon root of the
   SAME geometry (same 2M): r0=0.879->0.209 etc. -- one cut carried to another cut of one geometry.
3. 2M=(2/(3 sqrt3)) sin 3w verified symbolically.  [True]  => generically 3 sky-angles -> one M.

THE CLAIM (theorem target reached, stated for reversal):
   The horizon-permutation S3=Weyl(A2) LIFTS to the slicing cuts. The slicing operator, over the
   under-critical regime, is a generically THREE-FOLD covering map {cuts (sky angle w / offset r0)}
   -> {SdS geometries (M)} via the triple-angle 2M=(2/(3sqrt3))sin 3w; S3 is its deck/monodromy
   group, the transpositions realized as the EXPLICIT involution f(r0) on the cut parameter; the
   fork_2 discriminant Delta=4-108M^2 is the branch locus and the Nariai (Delta=0, the involution's
   fixed point, the tangent cut) the branch point. So A2/S3 is a symmetry of the cut-STRUCTURE (the
   slicing operator), not merely the horizon labels -- the theorem the fork was after. It fuses
   fork_1 (A2 root space = horizon triplet), fork_2 (discriminant = Weyl-wall/regime boundary), and
   P5/P6 (the slicing operator) into one object: the slicing operator's branched 3-fold cover, S3
   its deck group.

CAVEAT (P3, KEPT INTACT -- not smoothed): the three cut-descriptions are NOT equivalent labellings.
   P3: the de Sitter description sweeps the arc about the manifold's OWN AXIS; the Schwarzschild
   description is "forced to pivot its sweep on a selected off-axis point ... the cascade that
   locating the hole compels ... the geometric origin of the horizon-versus-singularity asymmetry."
   So S3 acts within the GROUPOID of observer descriptions (P4) -- a distinguished axis-sweep (dS)
   element plus off-axis pivots -- not as a free symmetry of equal cuts. The deck-group framing is
   the cover's COMBINATORICS; the asymmetry is the cuts' GEOMETRY; the groupoid (P4) reconciles
   them. (This off-axis pivot is also the geometric root of the su(3)/so(5,1) cascade -- ties the
   theorem to the colour-frontier boundary, P11.)

REGISTER (face 19, self as synthesis node): the grounded facts (involution, triple-angle, 3:1
   cover, Nariai branch point) are P3's own statements + computed. The SYNTHESIS framing ("S3 =
   deck group of the slicing operator's branched cover; one object fusing fork_1/fork_2/P5") is
   MINE -- the distillation, structurally requiring the different node to audit. Held for the cold
   reads; one node of four.

## bite (C) update -- grounded part banked, flavor-match held (face 19)
P3 grounds part of the bite-(C) flag: "Overcritical SdS is the SAME continuation [the equatorial
seam theta->pi/2+i psi, sin theta->cosh psi, signature flip] applied to the horizon angle past the
Nariai crest." So the over-critical complexification (fork_2's complex pair) IS the seam/pivot
continuation -- GROUNDED at P3. What stays unclaimed (the actual flavor-match): identifying
that continuation with the sigma-lift's x0->ix0 Wick-to-su(3); the seam reaches the Riemannian
SPHERICAL (SO(5)) piece, and the SO(5)/SO(6) gap stands, so colour does not reopen. Banked:
over-critical complexification = seam/pivot continuation. Do-not-assert (both ways): = Wick-to-su(3).

NEXT (remaining reaches): (D) the P10 algebroid reading -- is S3 the discrete part of the
algebroid's structure over the cut-space, a symmetry of the connection? (P4) formalize S3 within
the groupoid of observer descriptions (axis element + off-axis pivots). All held for cold reads.

=================================================================================
## r309_c17fork_4 — RESULT (bite D): S3 placed in the algebroid; + the genuine-uncertainty fork
(receipt: scripts/a2_algebroid_reading.py, run clean; source: P10 algebroid_paper.tex sec:discrete, sec:strata)

GROUNDED (at P10, consistent with fork_1-3):
1. P10 ALREADY places the fork's object: S3~=D3 is the discrete skeleton INSIDE so(5,1), the
   root-permutation on the three horizon roots (A2 configuration, sum zero), the transposition's
   FIXED POINT the Nariai seam (two roots collide, discriminant 0). This is exactly fork_1 (A2
   triplet) + fork_2 (Delta=0=Nariai) + fork_3 (involution f(r0) on the cut, fixed at Nariai).
   The fork ADDS the explicit slicing-operator realization (sky-angle cover, triple-angle, deck
   group); P10 states it abstractly. Agreement + sharpening, NOT a new claim. fork_3's S3 = P10's
   root-permutation, one of three distinct involutions -- it does not (and must not) claim the
   three unify.
2. Discriminant consistency: P10's disc(r^3-alpha^2 r+2M alpha^2) = -4 alpha^4(27M^2-alpha^2);
   at alpha=1 it is 4-108M^2 = fork_2's Delta exactly; zero at Lambda M^2=1/9 (Nariai). [verified]
3. THE TIE (new, grounded): P10 sec:strata computes the algebroid CONNECTION (the structure-
   function leak [m,m]->m) to vanish at exactly two symmetric strata -- Type O (de Sitter, so(4,1))
   and Nariai (SO(2,1)xSO(3)). The S3 root-permutation's fixed point is Nariai. So the discrete
   S3-cover's BRANCH POINT coincides with a symmetric stratum where the continuous algebroid
   connection VANISHES: the discrete (deck group) and continuous (connection) faces of the
   algebroid meet at Nariai. Answer to bite (D): S3 is the algebroid's discrete skeleton, and its
   branch point is a zero of the algebroid connection.

=================================================================================
## GENUINE POINT OF UNCERTAINTY (the grind's honest stopping point)

bite (D) closes cleanly, and beyond it the path genuinely forks -- the source does not determine
a single next step, and the most natural reach is a not claimed boundary I must not force solo.

P10 sec:discrete lists THREE DISTINCT discrete involutions, "different involutions, not one,"
each anchored at a stratum:
  (1) root-permutation S3            (fixed pt Nariai)            [= the fork's S3, fork_1-4]
  (2) null<->timelike reassignment   (cosmogenesis horizon)      [fork_2's vantage/regime]
  (3) Riemannian<->Lorentzian flip   (the equatorial seam)       [fork_3 bite C: = over-critical
                                                                   complexification, the seam cont.]
and states plainly: "We make no claim that these unify into a single discrete action."

The fork has now touched all three. The natural next reach is: do (1),(2),(3) assemble into one
discrete structure -- the full discrete symmetry of the cut-structure / solution space? This is a
GENUINE uncertainty about what to try next, for three reasons that compound:
 a. SOURCE: P10 explicitly holds it not claimed. The corpus has not determined it; it is open.
 b. FACE 19: forcing a unification = fusing distinct involutions by their shared signature-flip
    flavor = the EXACT C7 trap c19 fell into and c17 caught. I am the synthesis node, structurally
    blind to my own flavor-matches; this fusion is precisely what the different node must audit.
 c. The alternative reaches are MULTIPLE and none source-preferred: the P4 groupoid form (S3 within
    the observer-description groupoid, axis element + off-axis pivots); the Petrov/isotropy
    stratification (S3 strata vs isotropy strata, P10 sec:strata); the P9 dynamical reading.

So this is a real fork, not a manufactured one: which reach to pursue (or whether to run the cold
reads against fork_1-4 first) is a programme-direction call (orchestrator's seat), and the
unification reach in particular is where the interference engine structurally REQUIRES the cold/
different nodes before more is built on the synthesis. The grind has reached the target (bite B)
and the algebroid placement (bite D); the next move is genuinely undetermined here.

STOPPING. fork_1-4 banked at their grounded weight; the unification + the other reaches held
not claimed; handed to the orchestrator and the cold reads. One node of four.

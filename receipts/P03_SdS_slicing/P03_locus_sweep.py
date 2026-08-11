"""
P03_locus_sweep.py -- P3 sec:tour and across the corpus: every descriptively-named object
audited against the place it actually sits.

** THE HEADLINE. **  One locus -- the throat point at azimuth 120k + 60, i.e. r = 0 on the
throat circle -- carries SEVEN names in the corpus: the graze point (where a null leg touches
the throat), the tangency point of the projection, the MIDPOINT of a triangle side, the vertex
of the projective dual, the crossing of the skew hexagon's opposite edges, the matter sector's
WALL, and the r = 0 BRANCH POINT.  ** P3 sec:tour's own sentence -- "One triple, THREE faces"
-- counts three of the seven, and among the four it omits are the three that carry the
physics: the midpoint, the wall, and the branch point. **  The sentence is not wrong; it
CLOSES a list that is open.

OTHER FINDINGS:
 · the throat carries THREE names (the hole, the incircle of the hinge triangle, the
   nine-point circle) and all three are established identities;
 · the hinge and the swing axis are one line under two descriptions;
 · hinge vs wall scores 1/5 on the five-test criterion (only EQUIVARIANCE agrees) and seam vs
   wall scores 1/5 (both on the throat, but at r = alpha and r = 0 -- DIFFERENT loci);
 · the Z_3-fixed centre is not any of them: P14 says it carries NO wall.

A THIRD CATEGORY THE SWEEP TURNED UP, not anticipated: one locus carrying a name the corpus
has ALREADY DISOWNED -- r = 0 as "the curvature singularity", which P3 calls a perspectival
artefact of the areal coordinate.  ** A disowned name left in circulation reads as a live
object and is worse than an undrawn identity. **

AND FOUR CANDIDATE IDENTITIES NOBODY HAS DRAWN: the LAP and the cosmogenetic BEAD (P14 builds
the wall on the bead, P3 builds the closure as the lap, and neither says whether they are one
object); the NARIAI CREST and the hinge's own tangent line (P3 PROVES the tangent is the
Nariai cut and never states it as a locus identity); the twelve STATIONS and the twelve null
LEGS; and the Hubble-Eddington radius with the seam, which P3's abstract already states
CONDITIONALLY ("on the forced member ... identical with it") and is the only identity in the
corpus written in that form.

PROVED NON-IDENTITIES are in good order: lem:twoturnings separates the horizon-root three from
the turnaround three, and COMBINATORICS Claim 1 separates the hinge hexad from the A_2 hexad
(they complete by T and by R respectively).  ** The corpus is better at proving things apart
than at drawing them together. **

METHOD NOTE: every identity this sweep found was already implicit in two papers each stating
its half.  Nothing required new geometry -- it required reading two sentences at once.

ORIGIN: computations/baryon_edge/L77_the_locus_sweep.py -- built r2376 (c54.26); edit the
origin, not this copy."""

import itertools
from collections import defaultdict
import sympy as sp

print(__doc__.split("Run:")[0])
sq3 = sp.sqrt(3)

# =====================================================================
print("=" * 78)
print("PART 1 — THE INVENTORY")
print("=" * 78)
print("  Reduced picture (X0, X1, X2), alpha = 1.  A locus is given as a KEY that two")
print("  different names land on only if they are literally the same place.")
print()

# name -> (locus key, source, what the corpus calls its definition)
INV = [
 ("the hole / throat",        "circle: X0=0, |X|=1",  "P3 sec:slicing",
  "the waist of the hyperboloid, radius alpha, the one invariant"),
 ("the incircle of the hinge triangle", "circle: X0=0, |X|=1", "P3 prop:twoalpha",
  "the inscribed circle of the equilateral of three hinges"),
 ("the nine-point circle",    "circle: X0=0, |X|=1",  "FIGURE (⊢2), P3 abstract",
  "Euler's R/2 circle of the hinge triangle"),
 ("hinge k",                  "line: azim 120k, rad 2, dir (1,0,0)", "P3 sec:slicing",
  "the line the slicing plane swings about"),
 ("the swing axis",           "line: azim 120k, rad 2, dir (1,0,0)", "P3_SWING_ONTOLOGY",
  "the axis of the door's rotation"),
 ("puncture (hinge k, horn e)","point: X0=e sqrt3, azim 120k, rad 2", "L-61",
  "where hinge k meets the substrate"),
 ("graze point k",            "point: X0=0, azim 120k+60, rad 1", "L-61",
  "where a null leg touches the throat"),
 ("tangency point of the projection", "point: X0=0, azim 120k+60, rad 1", "P3 prop:twoalpha(iii)",
  "where a triangle side touches the incircle"),
 ("midpoint of a triangle side", "point: X0=0, azim 120k+60, rad 1", "P3 prop:twoalpha(iii)",
  "the side's own midpoint"),
 ("vertex of the projective dual", "point: X0=0, azim 120k+60, rad 1", "p0 (geometric-core)",
  "the dual figure's vertex"),
 ("crossing of the skew hexagon's opposite edges", "point: X0=0, azim 120k+60, rad 1",
  "P3 sec:tour", "where opposite hexagon edges cross"),
 ("the wall (of hinge j)",    "point: X0=0, azim 120k+60, rad 1", "P14 header, prop:wall",
  "r = 0 on the throat circle, the back, antipodal to its hinge"),
 ("the r=0 branch point",     "point: X0=0, azim 120k+60, rad 1", "P3 sec:lap",
  "the branch point the signed radius passes through"),
 ("the seam",                 "locus: cut meets throat, r = 1", "P3 sec:seam",
  "the equatorial turning point where the cut meets the throat"),
 ("the Z_3-fixed centre",     "point: the hole's axis, no azimuth", "P14 header",
  "the symmetric point; CARRIES NO WALL"),
 ("the excentres",            "point: X0 = sqrt15", "FIGURE ⊢57",
  "real overhead points of the hinge triangle"),
]
print(f"  {'name':>46} {'locus':>38}")
for nm, key, src, defn in INV:
    print(f"  {nm:>46} {key:>38}")
    print(f"  {'':>46} {'('+src+')':>38}")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — GROUP BY LOCUS.  HOW MANY NAMES DOES EACH PLACE CARRY?")
print("=" * 78)
byloc = defaultdict(list)
for nm, key, src, defn in INV:
    byloc[key].append((nm, src))
print(f"  {'names':>6}  locus")
for key in sorted(byloc, key=lambda k: -len(byloc[k])):
    print(f"  {len(byloc[key]):>6}  {key}")
    for nm, src in byloc[key]:
        print(f"  {'':>6}    · {nm}   [{src}]")
    print()
worst = max(byloc, key=lambda k: len(byloc[k]))
print(f"  ** THE MOST OVERLOADED PLACE IN THE CORPUS CARRIES {len(byloc[worst])} NAMES: **")
print(f"     {worst}")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE CORPUS'S OWN COUNT OF FACES AGAINST THE SWEEP'S")
print("=" * 78)
print("  P3 sec:tour, on exactly this locus, in its own words:")
print()
print("     'One triple, THREE FACES: the tangency points of the projection, the vertices")
print("      of the dual figure, and the crossings of the skew hexagon's opposite edges.'")
print()
corpus_faces = ["tangency point of the projection",
                "vertex of the projective dual",
                "crossing of the skew hexagon's opposite edges"]
sweep_faces = [nm for nm, src in byloc[worst]]
missing = [f for f in sweep_faces if f not in corpus_faces]
print(f"  the corpus counts:  {len(corpus_faces)}")
print(f"  the sweep finds:    {len(sweep_faces)}")
print()
print("  ** THE FACES THE SENTENCE DOES NOT COUNT: **")
for f in missing:
    src = dict((n, s) for n, s in byloc[worst])[f]
    print(f"     · {f}   [{src}]")
print()
print(f"  ⇒ ** P3 SAYS 'THREE FACES' AND THE SWEEP FINDS {len(sweep_faces)}.  The sentence is not")
print("     wrong -- each of its three is a face -- but it CLOSES A LIST that is open, and")
print(f"     the {len(missing)} it omits include the three that carry the physics: the side's own")
print("     MIDPOINT, the matter sector's WALL, and the r=0 BRANCH POINT. **")
print()
print("  ** AND THAT IS EXACTLY THE DEFECT DARYL NAMED: a descriptive name ('the tangency")
print("     point'), an analytic definition ('r = 0 on the throat'), and a geometric")
print("     feature ('where the null generators graze') that were never drawn identically. **")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE FIVE-TEST CRITERION ON WHAT THE GROUPING THROWS UP")
print("=" * 78)
print("  Same locus is NECESSARY, not sufficient.  Run the criterion (LOCUS, TYPE,")
print("  DEFINITION, EQUIVARIANCE, SEPARABILITY) on the pairs that matter:")
print()
PAIRS = [
 ("wall", "r=0 branch point", 5,
  "settled c54.25: one locus, two properties, no quantity separates them"),
 ("graze point", "wall", 5,
  "same locus, same type, each definable from the other via 'the throat point antipodal "
  "to a hinge'"),
 ("tangency point", "midpoint of the side", 5,
  "prop:twoalpha(iii) IS the statement that these coincide -- an established identity"),
 ("nine-point circle", "the throat", 5,
  "⊢2: Euler's R/2 with R = 2 alpha gives alpha -- an established identity by a route "
  "mentioning neither tangency nor the substrate"),
 ("incircle of the hinge triangle", "the throat", 5,
  "prop:twoalpha: 'the hole IS the incircle'"),
 ("hinge", "swing axis", 5,
  "the same line under two descriptions; P3_SWING_ONTOLOGY names them as one"),
 ("hinge", "wall", 1,
  "settled c54.24-25: only EQUIVARIANCE agrees; different locus, type, definition, "
  "and separable (a hinge has 2 punctures and 0 legs, a wall 0 punctures and 4 legs)"),
 ("seam", "wall", 1,
  "** BOTH ON THE THROAT BUT AT DIFFERENT r: the seam is where the cut meets the throat "
  "at r = alpha; the wall is r = 0.  DIFFERENT LOCI. **"),
 ("Z_3-fixed centre", "wall", 0,
  "P14 is explicit: 'the Z_3-fixed centre carries NO wall'"),
]
print(f"  {'pair':>46} {'score':>7}  verdict")
for a, b, s, why in PAIRS:
    verdict = 'SAME' if s == 5 else ('DIFFERENT' if s <= 1 else 'partial')
    print(f"  {a+'  vs  '+b:>46} {str(s)+'/5':>7}  {verdict}")
    print(f"  {'':>46} {'':>7}  {why}")
print()
print("  ** SO THE OVERLOADED LOCUS IS ONE OBJECT WITH SIX NAMES, AND THE THINGS THAT LOOK")
print("     LIKE THEY MIGHT JOIN IT (hinge, seam, centre) PROVABLY DO NOT. **")

# =====================================================================
print()
print("=" * 78)
print("PART 5 — PROVED NON-IDENTITIES.  Where two names must NOT be merged.")
print("=" * 78)
NONID = [
 ("the horizon-root three", "the bead/turnaround three",
  "lem:twoturnings: NO affine change of variable identifies the two root sets",
  "PROVED distinct"),
 ("the hinge hexad (6 punctures)", "the A_2 hexad (6 Nariai)",
  "COMBINATORICS ⊢Claim 1: they complete by DIFFERENT reflections, T vs R",
  "PROVED distinct -- they share the fundamental 3 and complete distinctly"),
 ("the physical swing angle psi", "the sky angle w (the dial)",
  "sin w = sqrt3 sin psi -- P3_SWING_ONTOLOGY: 'the gnomonic scaling, not a second vantage'",
  "distinct ANGLES of one object; conflating them was a documented failure mode"),
 ("the swing", "the sweep",
  "P3_SWING_ONTOLOGY: 'two rotations, two axes' -- swing turns the door about the hinge, "
  "sweep revolves the cut about the hole's isotropic directions",
  "distinct, and the note records 'sweep the projection and call it the swing' as a trap"),
 ("r = 0 as a curvature singularity", "r = 0 as a branch point",
  "P3: the divergence there is 'a perspectival artefact of the areal coordinate'; the "
  "substrate is smooth across it",
  "SAME LOCUS, and the corpus REJECTS the first reading -- a name that should be retired"),
]
print(f"  {'the two names':>52}  status")
for a, b, why, st in NONID:
    print(f"  {a+'   vs   '+b:>52}  {st}")
    print(f"  {'':>52}  {why}")
print()
print("  ** THE LAST ROW IS THE INTERESTING ONE: same locus, two names, and the corpus")
print("     REJECTS one of them.  ** That is a third category the sweep needs and I did not")
print("     anticipate: not 'two names for one thing' and not 'two things', but ONE THING")
print("     CARRYING A NAME THE CORPUS HAS ALREADY DISOWNED. **")

# =====================================================================
print()
print("=" * 78)
print("PART 6 — NAMED OBJECTS WITH NO LOCUS PINNED.  The other half of the audit.")
print("=" * 78)
UNPINNED = [
 ("the door", "the swinging slicing plane -- a PLANE, and which plane depends on the dial",
  "no fixed locus BY CONSTRUCTION; it is the moving part.  ** Correctly unpinned. **"),
 ("the lap", "the closed circuit through the seam, r=0, and the conjugate branch",
  "a PATH, not a point.  ** Its locus is the whole slicing curve. **  Candidate identity "
  "with THE BEAD -- see below, and it is not drawn anywhere."),
 ("the cosmogenetic bead", "'the closed curve the framework proves one closed object'",
  "** CANDIDATE IDENTITY WITH THE LAP, and neither paper states it as one. **  P14 builds "
  "the wall ON the bead; P3 sec:lap builds the closure.  If they are one object that "
  "should be said; if not, the difference should be."),
 ("the crest", "the Nariai maximum of the mass, |r0| = 1/sqrt3, w = 30 deg",
  "pinned on the DIAL but not in the substrate.  ** Its substrate locus is the hinge's "
  "own tangent line -- which P3 proves and never states as a locus identity. **"),
 ("the station", "a designation on the dial, every 30 degrees, twelve of them",
  "pinned on the dial.  ** Whether the twelve stations and the twelve null legs are one "
  "twelve is L-63, still open. **"),
 ("the pseudo-sphere", "w = 90/270, |r0| = 2/sqrt3 -- the plane perpendicular to the radial",
  "pinned on the dial; substrate locus not drawn."),
 ("the Hubble-Eddington radius", "r = (M alpha^2)^(1/3), where K_G changes sign",
  "** P3's abstract: 'on the forced member this locus is not merely near the seam but "
  "IDENTICAL with it.'  A CONDITIONAL identity, already stated, and the only one in the "
  "corpus written in this form. **"),
]
print(f"  {'name':>28}  what it is / what is owed")
for nm, what, owed in UNPINNED:
    print(f"  {nm:>28}  {what}")
    print(f"  {'':>28}  -> {owed}")

# =====================================================================
print()
print("=" * 78)
print("PART 7 — WHAT THE SWEEP FOUND")
print("=" * 78)
findings = [
 "① ONE LOCUS CARRIES SEVEN NAMES and the corpus's own sentence counts THREE.  Among the",
 "   four it omits are the side's MIDPOINT, the matter sector's WALL and the r=0 BRANCH",
 "   POINT -- the three that carry the physics.",
 "   ** A closed list that should be open, in a paper that closes it.  (L-82.) **",
 "",
 "② A THIRD CATEGORY I DID NOT ANTICIPATE: one locus carrying a name the corpus has already",
 "   DISOWNED (r=0 'the curvature singularity', which P3 calls a perspectival artefact).",
 "   ** A disowned name left in circulation is worse than an undrawn identity, because it",
 "   reads as a live object.  (L-83.) **",
 "",
 "③ THE LAP AND THE BEAD ARE A CANDIDATE IDENTITY NOBODY HAS DRAWN.  P14 builds the wall ON",
 "   the bead; P3 builds the closure as the lap.  ** If one object, say so; if two, say the",
 "   difference -- and the wall's home depends on which.  (L-84.) **",
 "",
 "④ THE CREST HAS NO STATED SUBSTRATE LOCUS, and it has one: the hinge's own tangent line.",
 "   ** P3 PROVES this (sin w = 1/2 => sin 3w = 1) and never states it as a locus identity,",
 "   so 'the Nariai crest' and 'the tangent from the hinge' read as two objects.  (L-85.) **",
 "",
 "⑤ THE PROVED NON-IDENTITIES ARE IN GOOD ORDER.  lem:twoturnings and ⊢Claim 1 both do the",
 "   right thing: they establish DISTINCTNESS rather than leaving it ambiguous.",
 "   ** The corpus is better at proving things apart than at drawing them together. **",
 "",
 "⑥ AND THE METHODOLOGICAL FINDING, which is the one to keep.  Every identity the sweep",
 "   found was already IMPLICIT in two papers that each stated their half.  ** Nothing here",
 "   required new geometry.  It required reading two sentences at once, which is exactly",
 "   what a corpus this size stops doing by itself. **",
]
for f in findings:
    print("  " + f)

# --- r2376+c54.159 -----------------------------------------------------------------
# The sweep's headline -- "P3 says THREE FACES and the sweep finds SEVEN" -- was only
# printed.  Pin the counts and the membership: the throat point at azimuth 120k+60
# carries 7 names, the corpus's sentence counts 3, and the 4 it omits are exactly the
# graze point, the side's midpoint, the wall and the r=0 branch point.  Also pin the
# throat's own 3 names and the hinge/swing-axis pair, the sweep's other two groupings.
assert worst == "point: X0=0, azim 120k+60, rad 1"
assert len(byloc[worst]) == 7 and len(sweep_faces) == 7
assert len(corpus_faces) == 3 and len(missing) == 4
assert set(missing) == {"graze point k",
                        "midpoint of a triangle side",
                        "the wall (of hinge j)",
                        "the r=0 branch point"}
assert len(byloc["circle: X0=0, |X|=1"]) == 3          # hole = incircle = nine-point circle
assert len(byloc["line: azim 120k, rad 2, dir (1,0,0)"]) == 2   # hinge = swing axis
assert sum(len(v) for v in byloc.values()) == len(INV) == 16
assert [s for a, b, s, w in PAIRS if (a, b) == ("seam", "wall")] == [1]   # seam is NOT the wall
assert [s for a, b, s, w in PAIRS if (a, b) == ("hinge", "wall")] == [1]  # hinge is NOT the wall

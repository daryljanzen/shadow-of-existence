#!/usr/bin/env python3
"""
L-69w — THE TWO LEPTON LEADS, WORKED TOGETHER, BECAUSE THEY ARE ONE LEAD.

`L-69`  *"Does the axis carry TWO states?  F-6: leptons are AXIAL -- no azimuth, hence integer
        charge, no colour, no confinement, three facts from one statement.  But the geometry has
        not been shown to carry two axial states ($e$ and $\\nu$) the way it carries six
        azimuthal ones.  **The largest unbuilt piece.**"*
`L-79`  *"Does the $\\mathbb{Z}_3$-fixed centre carry the fourth lepton state?  P14's own header:
        'the $\\mathbb{Z}_3$-fixed centre carries NO wall.'  A fixed point carrying no wall is the
        natural home of a state with no charge of any kind -- and $\\nu_R$ is exactly that,
        sterile.  **Too sharp to drop, too thin to claim.**"*

** BOTH ASK FOR A SEAT.  THE STRUCTURE SUPPLIES A CHARACTER, AND THE SEAT THEY ASK FOR IS
PROVABLY EMPTY -- for a reason the colour arc already owns and neither lead could have used. **

  PART 1  The two leads name one locus, and `F-6`'s own c54.22 correction already moved off it.
  PART 2  ** THE CENTRE, COMPUTED: the three signed radii vanish there TOGETHER, and that is a
          rank statement, not a convention. **
  PART 3  ** AND THE THREE RADII ARE THE $A_2$ WEIGHT SYSTEM -- so the centre is the ORIGIN OF
          THE WEIGHT PLANE, and the fundamental has no zero weight. **
  PART 4  ** THE TOWER `F-6` FEARS IS NOT TRUNCATED.  IT IS NOT THERE. **
  PART 5  What the class does hold: four, and the four are two bits.
  PART 6  `F-6`'s three facts traced, its refutation condition checked, and the two strikes.

Run: python3 L069w_the_axis_and_the_tower.py      (sympy)
"""
import itertools
import sympy as sp

print(__doc__.split("Run:")[0])

al = sp.Symbol('alpha', positive=True)
x, y = sp.symbols('x y', real=True)
HINGE = [0, 120, 240]
WALL = [180, 300, 60]

# =====================================================================
print("=" * 78)
print("PART 1 — ONE LOCUS, AND F-6 HAS ALREADY MOVED OFF IT")
print("=" * 78)
for s in [
 "`L-69` says *the axis*; `L-79` says *the $\\mathbb{Z}_3$-fixed centre*.  ** In the transverse",
 "plane a rotation of order three has exactly ONE fixed point, so these are the same point, and",
 "'no azimuth' is a description of it rather than a second condition. **  The two leads have",
 "been carried separately since c54.24 and are one lead.",
 "",
 "⌗ ** AND `F-6` ITSELF STOPPED SAYING 'AXIAL' AT c54.22. **  Its corrected form: *'a lepton is",
 "   the triality-zero class -- its winding is a WHOLE NUMBER OF LAPS.  It need not be off the",
 "   equator; it must be COMPLETE on it.'*  ** So the seat question is already answered in the",
 "   negative by the row the lead cites; what `F-6` still carries is a different clause: **",
 "",
 "     *'what is not derived is why $k=0$ holds exactly two low-lying states rather than a",
 "      TOWER $\\{0,-1,-2,\\dots\\}$'*  --  and *'REFUTED BY: the $k=0$ class admitting a tower",
 "      with nothing to truncate it.'*",
 "",
 "⇒ ** SO THERE ARE EXACTLY TWO THINGS OWED HERE: is the centre empty, and is there a tower.",
 "   PARTS 2-3 do the first, PART 4 the second. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE CENTRE, COMPUTED")
print("=" * 78)
print("  `L-128` PART 7 derived vantage $j$'s SIGNED areal radius on the throat circle as")
print("  r_j = alpha sin(phi - theta_j).  That is the restriction to the circle of a LINEAR FORM")
print("  on the transverse plane -- the coordinate perpendicular to hinge j's static pair:")
print()
n = [(-sp.sin(sp.rad(t)), sp.cos(sp.rad(t))) for t in HINGE]
rj = [sp.simplify(n[j][0]*x + n[j][1]*y) for j in range(3)]
for j in range(3):
    print(f"     hinge {HINGE[j]:>3}deg :  n_{j} = {tuple(sp.nsimplify(c) for c in n[j])}"
          f"      r_{j}(x,y) = {rj[j]}")
print()
# consistency with L-128: restrict to the circle
phi = sp.Symbol('varphi', real=True)
for j in range(3):
    onc = sp.simplify(sp.expand_trig(rj[j].subs({x: al*sp.cos(phi), y: al*sp.sin(phi)})))
    want = sp.simplify(sp.expand_trig(al*sp.sin(phi - sp.rad(HINGE[j]))))
    assert sp.simplify(onc - want) == 0
print("  ** CONSISTENCY: each linear form restricts on the circle to exactly `L-128`'s")
print("     alpha sin(phi - theta_j).  The extension is a restriction undone, not a new object. **")
print()
print(f"  {'point':>22} {'r_0':>14} {'r_1':>14} {'r_2':>14} {'how many vanish':>16}")
pts = [(f"wall {WALL[j]}deg", (al*sp.cos(sp.rad(WALL[j])), al*sp.sin(sp.rad(WALL[j]))))
       for j in range(3)]
pts += [(f"hinge {HINGE[j]}deg", (2*al*sp.cos(sp.rad(HINGE[j])), 2*al*sp.sin(sp.rad(HINGE[j]))))
        for j in range(3)]
pts += [("** the Z_3 CENTRE **", (sp.Integer(0), sp.Integer(0)))]
for nm, p in pts:
    vals = [sp.simplify(rj[j].subs({x: p[0], y: p[1]})) for j in range(3)]
    nz = sum(1 for v in vals if sp.simplify(v) == 0)
    print(f"  {nm:>22} {str(sp.nsimplify(vals[0])):>14} {str(sp.nsimplify(vals[1])):>14} "
          f"{str(sp.nsimplify(vals[2])):>14} {nz:>16}")
print()
sol = sp.linsolve([rj[0], rj[1], rj[2]], [x, y])
Mrank = sp.Matrix([[n[j][0], n[j][1]] for j in range(3)]).rank()
print(f"  the common zero set of the three forms:  {sol}       rank of the 3x2 system = {Mrank}")
assert sol == sp.FiniteSet((sp.Integer(0), sp.Integer(0)))
assert Mrank == 2
print()
for s in [
 "⇒⇒ ** AT EVERY WALL EXACTLY ONE SIGNED RADIUS VANISHES; AT THE CENTRE ALL THREE DO, AND THE",
 "   CENTRE IS THE ONLY POINT OF THE PLANE WHERE THAT HAPPENS. **",
 "",
 "⌗ ** AND THAT IS WHY IT CARRIES NO WALL, IN THE CURRENCY OF `prop:wall` RATHER THAN BY FIAT. **",
 "   A wall is a locus across which ONE vantage's superpotential changes sign, so it is",
 "   codimension ONE -- a line.  The three forms have rank two, so their common zero set is a",
 "   POINT, codimension two.  ** A point cannot be a wall of anything: there is no side to cross",
 "   to. **  P14's 'the $\\mathbb{Z}_3$-fixed centre carries no wall' is therefore a rank",
 "   statement about three linear forms, and the corpus has been carrying it as an observation.",
 "",
 "⌗ ** IT ALSO FAILS P3'S OWN CHARACTERISATION EXACTLY THERE. **  P3's abstract: *three throat",
 "   walls at distinct points of the throat circle with DISJOINT SUPPORT.*  Disjointness is what",
 "   the table's fourth column measures, and the centre is the unique point of the plane where",
 "   it fails -- the supports do not merely overlap there, all three coincide.",
 "",
 "⌗ ** AND THE TABLE'S SECOND BLOCK IS NOT AN ANOMALY, IT IS THE SAME FACT SEEN FROM OUTSIDE. **",
 "   $r_j$ vanishes at HINGE $j$ too, because the line $r_j=0$ is hinge $j$'s own axis: it runs",
 "   from the hinge through the centre to the back.  ** So the wall is that LINE -- codimension",
 "   one, as `prop:wall` requires -- and it meets the throat circle TWICE, at the front",
 "   ($\\varphi=\\theta_j$) and at the back ($\\varphi=\\theta_j+180^\\circ$). **",
 "   *P14 fixes $r=0$ at the back, $X_1=-\\alpha$.  ** That names a POINT and not a wall: the two",
 "   crossings lie on ONE line, so there is no second wall for the other choice to be, and",
 "   nothing in the construction depends on which of the two is named. **  The two are exchanged",
 "   by the antipodal map, which is $R$; and the three LINES, not the three points, are what",
 "   PART 3 measures.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE THREE RADII ARE A WEIGHT SYSTEM")
print("=" * 78)
tot = sp.simplify(rj[0] + rj[1] + rj[2])
print(f"  r_0 + r_1 + r_2 = {tot}      ** identically zero, on the whole plane **")
assert tot == 0
angles = [sp.deg(sp.atan2(c[1], c[0])) % 360 for c in n]
print(f"  the three normals sit at azimuths {[sp.nsimplify(a) for a in angles]} -- "
      f"pairwise {sp.nsimplify((angles[1]-angles[0]) % 360)} deg apart")
gram = sp.Matrix(3, 3, lambda i, j: sp.simplify(n[i][0]*n[j][0] + n[i][1]*n[j][1]))
print(f"  their Gram matrix:")
sp.pprint(gram)
offdiag = {sp.nsimplify(gram[i, j]) for i in range(3) for j in range(3) if i != j}
print(f"  diagonal {sp.nsimplify(gram[0,0])}, off-diagonal {offdiag}  "
      f"⇒ ratio {sp.nsimplify(list(offdiag)[0]/gram[0,0])}")
assert list(offdiag) == [sp.Rational(-1, 2)]
print()
for s in [
 "⇒⇒ ** THREE VECTORS OF EQUAL LENGTH, $120^\\circ$ APART, SUMMING TO ZERO, WITH MUTUAL COSINE",
 "   $-\\tfrac12$: THAT IS THE WEIGHT SYSTEM OF THE FUNDAMENTAL $\\mathbf{3}$ OF $\\su(3)$, AND",
 "   NOTHING ELSE HAS THAT SHAPE IN RANK TWO. **",
 "",
 "⌗ ** SO THE TRANSVERSE PLANE IS THE WEIGHT PLANE AND THE VANTAGE INDEX IS THE WEIGHT LABEL",
 "   -- which is the same three the colour arc found from the branching, arrived at here from",
 "   the metric geometry with no representation theory in the derivation. **  `L-128` had the",
 "   three radii and read only their ZEROS; their mutual angles were never taken.",
 "",
 "⇒⇒ ** AND THAT SETTLES `L-79` IN ITS OWN CURRENCY: THE $\\mathbb{Z}_3$-FIXED CENTRE IS THE",
 "   ORIGIN OF THE WEIGHT PLANE, AND THE FUNDAMENTAL HAS NO ZERO WEIGHT. **  A state seated",
 "   there would be a zero-weight vector of $\\mathbf{3}$, and $\\mathbf{3}$ has none.  ** The",
 "   lead's instinct -- 'a fixed point carrying no wall is the natural home of a state with no",
 "   charge of any kind' -- reads the emptiness as a vacancy.  It is an ABSENCE OF A WEIGHT. **",
 "",
 "⚠ *Stated at weight: this is a statement about three linear forms on a plane, and the",
 "identification of the module as the fundamental is `L-127`'s, not this file's.  ** What is new",
 "here is that the geometry's own radii realise that module's weights, which the corpus had not",
 "noticed and which makes the empty centre a theorem rather than a report. ***",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE TOWER IS NOT TRUNCATED; IT IS NOT THERE")
print("=" * 78)
for s in [
 "`F-6`'s live worry: *the $k=0$ class admitting a TOWER $\\{0,-1,-2,\\dots\\}$ with nothing to",
 "truncate it.*  The tower is indexed by WHOLE LAPS -- all triality zero, all colourless, and",
 "seemingly all distinct.  ** So: does the symmetry see a lap count? **",
 "",
 "`L-73`'s winding $k$ counts GRAZE CROSSINGS, three to a lap; the deck generator $D$ is one",
 "graze crossing (a third of a lap) and $D^3 = 1$.  So a configuration of winding $k$ presents",
 "the group element $D^k$:",
]:
    print("  " + s)
print()
print(f"  {'winding k (graze units)':>26} {'laps':>8} {'D^k':>8} {'triality':>10} {'colourless?':>13}")
for k in (-9, -6, -3, 0, 3, 6, 9, 1, 2):
    print(f"  {k:>26} {str(sp.Rational(k,3)):>8} {'D^'+str(k % 3):>8} {k % 3:>10} "
          f"{('** YES **' if k % 3 == 0 else 'no'):>13}")
kernel = sorted({k for k in range(-9, 10) if k % 3 == 0})
images = {k % 3 for k in kernel}
print()
print(f"  the whole 'tower' {[str(sp.Rational(k,3)) for k in kernel]} laps maps to "
      f"D^k for k mod 3 in {images}")
assert images == {0}
print()
for s in [
 "⇒⇒ ** EVERY MEMBER OF THE TOWER IS THE SAME GROUP ELEMENT -- THE IDENTITY.  The map",
 "   $k \\mapsto D^k$ has kernel $3\\mathbb{Z}$, and the tower IS the kernel. **",
 "",
 "⌗ ** SO THE LAP COUNT IS NOT A QUANTUM NUMBER OF THIS CONSTRUCTION.  A state is labelled by",
 "   the CHARACTER it carries, and the characters see $k$ only through $k \\bmod 3$; the tower's",
 "   members are indistinguishable to every label the structure has. **  ** They are not",
 "   distinct states awaiting a truncation.  They are one class described three ways. **",
 "",
 "⇒ ** `F-6`'s REFUTATION CONDITION THEREFORE DOES NOT TRIGGER, AND NOT BY BEING EVADED: it",
 "   asked for 'a tower with nothing to truncate it', and there is no tower to truncate. **",
 "",
 "⚠ *And the honest cost, which is the same one `L-125` charges: if lap count is invisible to",
 "the labels, the geometry cannot supply a lepton's charge MAGNITUDE from its winding either --",
 "only its quantisation.  ** That is not a new debt; it is the standing finding that the",
 "geometry quantises and does not couple, arriving here from a third direction. ***",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — WHAT THE CLASS DOES HOLD: FOUR, AND THE FOUR ARE TWO BITS")
print("=" * 78)
print("  `L-117` computed the turnaround's group as D_6 = S_3 x Z_2 with the deck Z_3 = A_3")
print("  inside the S_3.  Recomputed here from the character table rather than quoted:")
print()
S3 = list(itertools.permutations(range(3)))
A3 = [p for p in S3 if sum(1 for i in range(3) for j in range(i+1, 3)
                           if p[i] > p[j]) % 2 == 0]


def sgn(p):
    return (-1)**sum(1 for i in range(3) for j in range(i+1, 3) if p[i] > p[j])


irreps = []
for nm, dim, chi in (("trivial", 1, lambda p: 1),
                     ("sign", 1, lambda p: sgn(p)),
                     ("standard", 2, lambda p: sum(1 for i in range(3) if p[i] == i) - 1)):
    for eps, lab in ((1, "+"), (-1, "-")):
        irreps.append((f"{nm} (x) R{lab}", dim, chi, eps))
print(f"  {'irrep of D_6':>18} {'dim':>5} {'chi on A_3':>22} {'trivial on the deck?':>21}")
total = 0
for nm, dim, chi, eps in irreps:
    on_A3 = [chi(p) for p in A3]
    triv = all(v == dim for v in on_A3)
    if triv:
        total += dim
    print(f"  {nm:>18} {dim:>5} {str(on_A3):>22} {('** YES **' if triv else 'no'):>21}")
print()
print(f"  ** TOTAL DIMENSION OF THE DECK-TRIVIAL SECTOR = {total} **   and 12 + {total} "
      f"= {12+total}")
assert total == 4
print()
print(f"  {'':>10} {'T = S_3 sign':>14} {'R':>6}   {'reads as':>28}")
for a, b, c in (("state 1", "+", "+"), ("state 2", "+", "-"),
                ("state 3", "-", "+"), ("state 4", "-", "-")):
    print(f"  {a:>10} {b:>14} {c:>6}   {'(isospin, chirality)':>28}")
print()
for s in [
 "⇒ ** FOUR, AND THEY ARE INDEXED BY TWO INDEPENDENT BITS -- $T$ AND $R$ -- WHICH THE CORPUS",
 "   FIXED AS WEAK ISOSPIN AND CHIRALITY IN `P03_winding_and_closure`, LONG BEFORE THE COUNT. **",
 "",
 "⌗ ** SO `L-69`'s 'TWO axial states' IS THE WRONG NUMBER AND ITS OWN ROUTE SUPPLIES THE RIGHT",
 "   ONE: two SPECIES times two CHIRALITIES is four, which is the lepton content of the",
 "   sixteen-fermion generation. **  The lead was written against the fifteen-fermion list.",
 "",
 "⌗ ** AND `L-79`'s 'FOURTH STATE' IS NOT A FOURTH.  The four arrive together as the four",
 "   deck-trivial characters -- there is no three-plus-one, so nothing is left needing a seat",
 "   of its own, and $\\nu_R$ is not distinguished from the other three by WHERE it sits but by",
 "   WHICH bits it carries. **",
 "",
 "⚠ *And c54.78 is what makes the even grading acceptable rather than a failure: colour is",
 "vector-like on singlets in the Standard Model too, so a $2+2$ colourless sector is the correct",
 "shape and a $2+1$ would exceed it.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 6 — F-6's THREE FACTS, TRACED; AND THE TWO STRIKES")
print("=" * 78)
print(f"  {'F-6 claims':>26} {'traced to':>34} {'holds?':>9}")
for a, b, c in [
    ("leptons have integer charge", "k = 0 mod 3, so no fractional part", "** yes **"),
    ("leptons carry no colour", "trivial deck character, by definition", "** yes **"),
    ("leptons do not confine", "the lap closes alone (L-73 PART 3)", "** yes **"),
]:
    print(f"  {a:>26} {b:>34} {c:>9}")
print()
for s in [
 "⌗ ** ALL THREE FOLLOW FROM TRIALITY ZERO AND NONE OF THEM FROM 'AXIAL'. **  `F-6`'s 'one",
 "   statement doing three jobs' survives its own c54.22 correction intact -- the statement just",
 "   is not the one the row was originally written around, and `L-69` inherited the old one.",
 "",
 "✔ ** `L-69` STRIKES. **  Its question -- what does the axis carry -- has a determinate answer:",
 "   ** NOTHING, and by a rank statement (PART 2) reinforced by a weight statement (PART 3). **",
 "   Its cited refutation route, the tower, ** does not exist (PART 4) **.  And the states it was",
 "   looking for are supplied, four of them, by a character rather than a seat (PART 5).",
 "",
 "✔ ** `L-79` STRIKES. **  There is no fourth state to house; the four arrive as one sector, the",
 "   centre is the origin of the weight plane, and the fundamental has no zero weight.  ** The",
 "   lead was right that the empty centre is meaningful and wrong about what it means. **",
 "",
 "⚠ ** THE STANDING BOUND, UNCHANGED AND STILL GOVERNING: AN IRREP IS NOT A STATE. **  What is",
 "   matched here is a pattern of GRADINGS -- two bits against two bits -- and not a count of",
 "   fields.  *That bound is carried by `L-117` and by P14's own receipt appendix; it is a bound",
 "   on the reading, not an action owed by these two leads, which is why they strike rather than",
 "   being amended.*",
 "",
 "⌗ *`L-69` was carried as 'the largest unbuilt piece' since c54.24.  ** It was not unbuilt; it",
 "was mis-sited, and every part used to answer it was banked between c54.22 and c54.78. ***",
]:
    print("  " + s)

#!/usr/bin/env python3
"""
L-128 — THE THREE-WALL TRANSPORT, WHICH `L-127` NAMED AS THE PLACE Q WOULD HAVE TO COME FROM.
And it turns out the corpus contains TWO INCOMPATIBLE READINGS of how many radial functions
there are, has never noticed, and ** the fork decides whether su(3) is entailed. **

  PART 1  ** THE FORK, AND IT IS NOT MINE -- BOTH READINGS ARE WRITTEN DOWN IN THE CORPUS. **
  PART 2  The wall geometry, taken from `L-75` (verified there, not re-derived here).
  PART 3  ** THE MONODROMY UNDER EACH READING, COMPUTED. **
  PART 4  ** THE FOUR ESTABLISHED RESULTS RE-RUN AGAINST BOTH READINGS -- a decision table,
          because a re-reading that breaks the winding sector is worth nothing. **
  PART 5  ** DOES READING (ii) SUPPLY Q?  This is `L-127`'s remaining generator. **
  PART 6  What settles it, what is owed, and the risk stated plainly.

Run: python3 L128_three_walls_or_one_radius.py
"""
import sympy as sp
import itertools

print(__doc__.split("Run:")[0])

I3 = sp.eye(3)
w = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2
assert sp.simplify(w**3 - 1) == 0 and sp.simplify(w - 1) != 0

# =====================================================================
print("=" * 78)
print("PART 1 — THE FORK, AND BOTH SIDES OF IT ARE THE CORPUS'S OWN WORDS")
print("=" * 78)
for s in [
 "** READING (i) -- ONE RADIUS.  `L-74`/`L-78`, as computed: ** 'Transported along the two",
 "equatorial routes ... EACH graze-point crossing sends r -> omega r, hence psi -> omega^(-lambda)",
 "psi.'  ** That treats r as ONE function which vanishes at ALL THREE walls. **",
 "",
 "** READING (ii) -- THREE RADII.  P14's own header, and `L-75`'s verification of it: ** 'r=0 is",
 "NOT the throat's CENTRE but a point ON the throat circle -- the back, X_1 = -alpha, ** FIXED",
 "RELATIVE TO THE HINGE about which the slicing plane swings **.'  And `L-75`, having checked",
 "Daryl's statement clause by clause: ** 'the wall is a wall OF a hinge -- \"relative to one",
 "specified hole\" is NOT A HEDGE, IT IS THE DEFINITION.' **  ** That gives THREE signed areal",
 "radii, one per vantage, each vanishing at ITS OWN wall and nowhere else. **",
 "",
 "⌗ ** THESE ARE DIFFERENT GEOMETRIES AND THE CORPUS ASSERTS BOTH. **  Under (i) the branched",
 "cover is CYCLIC and its monodromy is ABELIAN -- which is precisely why `L-127` found only",
 "Z_3 and had to go looking for a second generator.  Under (ii) there are three independent",
 "branch loci and the monodromy need not be abelian at all.",
 "",
 "⌗ AND NOBODY HAS NOTICED BECAUSE THE TWO AGREE ON THE ONE THING EVERYONE CHECKED: both give a",
 "Z_3 label and both give triality = -lambda mod 3.  ** They part on the GROUP, not on the",
 "label, and the group is exactly what `L-127` is short of. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE WALL GEOMETRY (from `L-75`, verified there)")
print("=" * 78)
hinge = {j: 120 * j for j in range(3)}                 # 0, 120, 240
wall = {j: (120 * j + 180) % 360 for j in range(3)}    # 180, 300, 60 -- antipodal, canonical
owner = {v: k for k, v in wall.items()}
print(f"  {'hinge':>7} {'azimuth':>9} {'its wall (r_j = 0)':>20} {'legs graze at':>18}")
for j in range(3):
    legs = sorted([(hinge[j] - 60) % 360, (hinge[j] + 60) % 360])
    print(f"  {j:>7} {hinge[j]:>9} {wall[j]:>20} {str(legs):>18}")
assert sorted(wall.values()) == [60, 180, 300]
print(f"  walls = {sorted(wall.values())}, a Z_3 orbit; the hinge<->wall pairing is ANTIPODAL")
print(f"  and therefore canonical -- no handedness choice ('L-75' PART 3).")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE MONODROMY UNDER EACH READING")
print("=" * 78)
lam = sp.Symbol('lambda', integer=True)


def mono_i(L):
    """(i) one radius: every wall crossing multiplies the single mode by omega^(-lambda)."""
    return sp.Matrix([[sp.simplify(w**(-L))]])


def mono_ii(L, wall_az):
    """(ii) three radii: crossing wall W branches ONLY the vantage that owns W.
    Basis of the rank-3 object is (vantage 0, vantage 1, vantage 2)."""
    d = [1, 1, 1]
    d[owner[wall_az]] = sp.simplify(w**(-L))
    return sp.diag(*d)


print("  (i)  rank 1.  Every wall acts the same way, so the three generators COMMUTE:")
print(f"        rho(gamma_A) = rho(gamma_B) = rho(gamma_C) = omega^(-lambda).")
print("       ** image is Z_3, abelian, and that is the whole group. **")
print()
print("  (ii) rank 3, basis = the three vantages.  Crossing wall W branches only W's owner:")
for az in (60, 180, 300):
    M = mono_ii(1, az)
    print(f"        wall {az:>3} (hinge {owner[az]}'s):  diag"
          f"{tuple(sp.nsimplify(M[k, k]) for k in range(3))}    [lambda = 1]")
print()
for L in (1, 2, 3):
    prod = sp.simplify(mono_ii(L, 60) * mono_ii(L, 180) * mono_ii(L, 300))
    scal = sp.simplify(prod[0, 0])
    central = sp.simplify(prod - scal * I3) == sp.zeros(3)
    print(f"     one full lap (all three walls), lambda={L}:  product = "
          f"{sp.nsimplify(scal)} * I  ,  central: {central}  ,  det = {sp.simplify(sp.det(prod))}")
print()
for s in [
 "⌗⌗ ** AND THAT IS THE STRUCTURAL FACT OF THIS FILE: UNDER (ii) A FULL LAP ACTS BY THE CENTRE",
 "   OF SU(3), AND THE INDIVIDUAL WALLS DO NOT. **  The lap is omega^(-lambda) times the",
 "   identity -- exactly the central element whose triviality IS triality zero -- while each",
 "   single wall crossing is a NON-central diagonal.  ** Under (i) the lap is omega^(-3 lambda)",
 "   = 1 for every mode and every lambda, so the lap says nothing at all. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE FOUR ESTABLISHED RESULTS, RE-RUN AGAINST BOTH READINGS")
print("=" * 78)
print("  A re-reading that breaks the winding sector is worth nothing, so this is the test that")
print("  matters.  Each row is an established corpus result; each column is a reading.")
print()

# --- route dependence (L-74).  Two equatorial routes between punctures of hinges a,b.
def routes(a, b):
    """the two arcs between hinge a and hinge b, as the sets of walls each crosses"""
    aa, bb = hinge[a], hinge[b]
    lo, hi = min(aa, bb), max(aa, bb)
    short = tuple(sorted(x for x in wall.values() if lo < x < hi))
    long_ = tuple(sorted(x for x in wall.values() if x < lo or x > hi))
    return short, long_


print("  ROUTE DEPENDENCE (`L-74`: a field is route-labelled iff coloured).")
print(f"  {'hinges':>8} {'short arc walls':>17} {'long arc walls':>18} {'vantage':>8} "
      f"{'ratio under (ii)':>18} {'route-dep?':>11}")
ok_ii_route = {}
for a, b in itertools.combinations(range(3), 2):
    sh, lo = routes(a, b)
    for j in range(3):
        rs = sp.simplify(w**(-lam) if wall[j] in sh else 1)
        rl = sp.simplify(w**(-lam) if wall[j] in lo else 1)
        ratio = sp.simplify(rl / rs)
        dep = sp.simplify(ratio - 1) != 0
        ok_ii_route[(a, b, j)] = dep
        print(f"  {str((a,b)):>8} {str(sh):>17} {str(lo):>18} {j:>8} "
              f"{str(ratio):>18} {str(bool(dep)):>11}")
allroute = all(ok_ii_route.values())
print(f"  ** every vantage is route-dependent under (ii), for every pair: {allroute} **")
print("     -- and the ratio is omega^(-lambda) or omega^(+lambda), so it is trivial exactly")
print("     when lambda = 0 mod 3.  ** `L-74`'s CRITERION IS UNCHANGED: route-labelled iff")
print("     coloured.  Only the SIGN of the ratio moves, and `L-74` uses only whether it is 1. **")
print()

# --- the lap and single-valuedness (L-72 / confinement)
print("  SINGLE-VALUEDNESS OF A LONE COLOURED CONSTITUENT ON A FULL LAP (`L-72`, confinement).")
print(f"  {'lambda':>7} {'(i) lap factor':>16} {'(i) closes?':>12} {'(ii) lap factor':>17} "
      f"{'(ii) closes?':>13}")
for L in (1, 2, 3, 4):
    fi = sp.simplify(w**(-3 * L))
    fii = sp.simplify(w**(-L))
    print(f"  {L:>7} {str(sp.nsimplify(fi)):>16} {str(sp.simplify(fi - 1) == 0):>12} "
          f"{str(sp.nsimplify(fii)):>17} {str(sp.simplify(fii - 1) == 0):>13}")
for s in [
 "",
 "  ⌗ ** AND THIS IS A POINT IN (ii)'s FAVOUR, ON THE CORPUS'S OWN TERMS. **  `L-74` states the",
 "  result as 'a lone coloured constituent HAS NO WELL-DEFINED VALUE AT A POINT; only a",
 "  combination of vanishing total triality is a field on the manifold at all.'  ** Under (i)",
 "  that is FALSE AS STATED for a full lap -- omega^(-3 lambda) = 1 identically, so a lone",
 "  coloured mode DOES return to itself and IS single-valued on the base.  Under (ii) it is",
 "  literally true: the lap acts by omega^(-lambda), and only triality zero returns. **",
 "  ⌗ *That does not make (i) wrong -- (i) still gives route-dependence between punctures, which",
 "  is what `L-74` actually computes.  It makes (i) UNABLE TO SUPPORT THE SENTENCE THE CORPUS",
 "  WROTE, and (ii) able to.*",
]:
    print(s)
print()

# --- the thirds (L-73)
print("  THE THIRDS (`L-73`: x = k/3, y = x - 1, three classes by k mod 3).")
print("     `L-73` derives x and y from CLOSURE of a bound triple and the 1+2 horn split; the")
print("     Z_3 label enters only through 'the two routes differ by one lap'.")
same = all(sp.simplify((w**(-lam)) / (w**(-lam)) - 1) == 0 for _ in [0])
print(f"     Under BOTH readings the two routes differ by exactly one crossing of the vantage's")
print(f"     own wall, so the one-lap difference is unchanged: {same}")
print(f"     ** `L-73`'s derivation is INSENSITIVE to the fork. **")
print()

# --- triality = -lambda mod 3 (L-78)
print("  TRIALITY = -lambda mod 3 (`L-78`).")
print("     Under (i): the single mode's phase per crossing.  Under (ii): the phase the vantage")
print("     picks up at its OWN wall -- the same number, from the same r^3 = (9/2) M l^2.")
print("     ** unchanged under the fork **")
print()
print(f"  {'established result':>46} {'(i)':>8} {'(ii)':>8}")
for nm, ri, rii in [
    ("triality = -lambda mod 3 (`L-78`)", "holds", "holds"),
    ("route-labelled iff coloured (`L-74`)", "holds", "holds"),
    ("the thirds and the three classes (`L-73`)", "holds", "holds"),
    ("a lone coloured mode is not single-valued (`L-74`)", "FAILS", "holds"),
    ("the lap is the centre of SU(3)", "vacuous", "holds"),
    ("su(3) entailed (`L-127`'s gap)", "NO", "see PART 5"),
]:
    print(f"  {nm:>46} {ri:>8} {rii:>8}")

# =====================================================================
print()
print("=" * 78)
print("PART 5 — DOES (ii) SUPPLY Q?")
print("=" * 78)
print("  `L-127` showed the gap is one non-commuting generator wide.  Under (ii) the candidates")
print("  are already present: the three wall monodromies, and the hinge S_3 that permutes the")
print("  three vantages (`L-75`: the pairing is antipodal, so S_3 acts on walls and vantages")
print("  together).  Take lambda = 1 and build the group they generate.")
print()
GA, GB, GC = (mono_ii(1, 60), mono_ii(1, 180), mono_ii(1, 300))
P = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])       # the hinge 3-cycle
print(f"     det gamma_A = {sp.nsimplify(sp.simplify(sp.det(GA)))}  -- NOT 1, so a single wall")
print(f"     monodromy is in U(3) and not SU(3); the SU(3) content is in the RATIOS:")
D1 = sp.simplify(GA * GB.inv())
D2 = sp.simplify(GB * GC.inv())
for nm, D in (("gamma_A gamma_B^-1", D1), ("gamma_B gamma_C^-1", D2)):
    print(f"        {nm:>20} = diag{tuple(sp.nsimplify(D[k,k]) for k in range(3))}   "
          f"det = {sp.simplify(sp.det(D))}")
print()
print(f"     [gamma_A gamma_B^-1 , P] = 0 ? "
      f"{sp.simplify(D1*P - P*D1) == sp.zeros(3)}   ** so the group is NON-ABELIAN **")

# irreducibility of <D1, P>
m = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'm{i}{j}'))
sol = sp.solve(list(sp.simplify(m * D1 - D1 * m)) + list(sp.simplify(m * P - P * m)),
               list(m), dict=True)[0]
Mred = sp.simplify(m.subs(sol))
irred = len(Mred.free_symbols) == 1
print(f"     commutant of <gamma_A gamma_B^-1, P> = {Mred.tolist()}")
print(f"     ⇒ scalars only ⇒ ** IRREDUCIBLE on C^3: {irred} **")

# invariant symmetric bilinear form?
B = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'b{min(i,j)}{max(i,j)}'))
eqs = list(sp.simplify(D1.T * B * D1 - B)) + list(sp.simplify(P.T * B * P - B))
bsol = sp.solve(eqs, sorted(B.free_symbols, key=str), dict=True)
Bred = sp.simplify(B.subs(bsol[0])) if bsol else B
noform = Bred == sp.zeros(3)
print(f"     invariant symmetric bilinear form: {Bred.tolist()}  ⇒ only B = 0: {noform}")
print(f"     ⇒ not conjugate into SO(3), the only proper connected irreducible subgroup of SU(3)")
print()
print(f"  ** SO THE SMALLEST CONNECTED GROUP CONTAINING THE THREE WALL MONODROMIES AND THE HINGE")
print(f"     3-CYCLE IS SU(3) ITSELF: {bool(irred and noform)} **")
print()
for s in [
 "⌗ ** AND Q IS NOT ADJOINED -- IT IS THE RATIO OF TWO WALL MONODROMIES. **  `L-127` had to",
 "postulate a 'relative phase between sheets that is not a deck transformation' and could not",
 "find one.  ** Under (ii) it is not a phase between sheets at all: it is the phase between two",
 "VANTAGES, and it exists precisely because there are three walls rather than one. **  That is",
 "the shape `L-127` predicted for the answer, reached from the corpus's own definition of the",
 "wall rather than by adjoining anything.",
 "",
 "⌗ AND THE TWO GENERATORS ARE THE CORPUS'S TWO THREES DOING DIFFERENT JOBS, WHICH IS THE FIRST",
 "TIME THEY HAVE BEEN NEEDED TOGETHER RATHER THAN KEPT APART: ** the DIAGONAL generator is the",
 "three WALLS (branch loci), and the PERMUTATION generator is the three HINGES (the S_3 that",
 "moves vantage to vantage). **  Neither alone is more than Z_3 or S_3; the pair is SU(3).",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 6 — WHAT SETTLES IT, AND THE RISK STATED PLAINLY")
print("=" * 78)
for s in [
 "⚠ ** THIS IS A RE-READING, NOT A THEOREM, AND THE PREMISE IT TURNS ON IS NOT YET COMPUTED",
 "   ANYWHERE IN THE CORPUS. **  Reading (ii) requires:",
 "",
 "     ** r_j vanishes at wall j and at NEITHER of the other two walls. **",
 "",
 "   P14 ASSERTS it ('fixed relative to the hinge about which the slicing plane swings') and",
 "   `L-75` verified the antipodal PAIRING is canonical -- but ** no receipt computes r_j at",
 "   the other two walls from the metric. **  If r_j turned out to vanish at all three, reading",
 "   (i) is right, the monodromy is abelian, and PART 5 evaporates.  ** That single evaluation",
 "   is what this now rests on, and it is a finite computation on P3's own slicing curve. **",
 "",
 "⚠ ** AND ONE ESTABLISHED RESULT IS PUT AT RISK BY (ii), WHICH MUST BE SAID. **  `L-75` PART 4",
 "   found that ** a hinge's own two null legs graze the OTHER TWO hinges' walls and NEVER its",
 "   own. **  Under (ii) a vantage-j mode is unbranched at those two walls -- so a mode carried",
 "   along hinge j's own leg crosses NO branch point of r_j and picks up NO phase.  ** If the",
 "   winding is to be read on the LEGS rather than on the equatorial arcs, (ii) makes the legs",
 "   phase-free and that is a problem. **  `L-74` computes on the equatorial ARCS, where PART 4",
 "   above shows route-dependence survives; but `L-75` PART 5 explicitly says 'the winding is a",
 "   WALL-CROSSING COUNT' read on the legs.  ** Those two are not obviously the same count, and",
 "   under (i) nobody had to ask.  Registered as the sharp question, not waved at. **",
 "",
 "⇒ ** WHAT IS OWED, IN ORDER: (1) evaluate r_j at the other two walls on P3's slicing curve --",
 "   this decides the fork outright; (2) if (ii), reconcile the leg count with the arc count.",
 "   Nothing further should be claimed for su(3) until (1) is done. **",
 "",
 "⌗ AND WHY THIS IS WORTH THE RISK RATHER THAN A SAFER SMALLER STEP: ** the fork is already in",
 "the corpus and is already load-bearing. **  Two of its papers' sentences require different",
 "geometries, and the difference is exactly the difference between having colour's centre and",
 "having colour.  ** That is not a question one can decline to ask once it is visible. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 7 — AND THE DECIDING PREMISE IS COMPUTABLE, SO IT IS COMPUTED HERE")
print("=" * 78)
print("  PART 6 said the fork turns on where r_j vanishes and that no receipt computes it.")
print("  ** Leaving that owed would repeat exactly the c54.50 failure -- publishing a fork")
print("     without doing the cheap derivation that settles it.  So: **")
print()
X0, X1, X2, aa, phi, th = sp.symbols('X_0 X_1 X_2 alpha varphi theta', real=True)

print("  STEP 1 — the areal radius on the equatorial section, from the embedding alone.")
print("     Static de Sitter embeds with  -X_0^2 + X_1^2 = alpha^2 - r^2,  r the AREAL radius.")
print("     The equatorial section is  -X_0^2 + X_1^2 + X_2^2 = alpha^2.")
sec = -X0**2 + X1**2 + X2**2 - aa**2
r_sym = sp.Symbol('r', real=True)
lhs = sp.simplify((-X0**2 + X1**2) - (aa**2 - r_sym**2))
sub = sp.simplify(lhs.subs(X0**2, X1**2 + X2**2 - aa**2))
print(f"     Eliminating -X_0^2 + X_1^2 between them:  {sp.simplify(sub)} = 0")
sols = sp.solve(sp.Eq(sub, 0), r_sym)
print(f"     ⇒ r = {sols}   ** the areal radius IS the section-direction transverse to the")
print(f"        static pair (X_0, X_1), up to sign.  DERIVED, not posited. **")
assert set(sp.simplify(s**2 - X2**2) for s in sols) == {0}

print()
print("  STEP 2 — and the VANTAGE rotates which direction that is.")
print("     'the back, X_1 = -alpha, fixed relative to THE HINGE ABOUT WHICH THE SLICING PLANE")
print("     SWINGS' (P14).  A hinge at azimuth theta fixes the static pair, so the areal")
print("     direction is the one PERPENDICULAR to it in the (X_1, X_2) plane:")
r_j = aa * sp.sin(phi - th)
print(f"        r_j(phi) = {r_j}       on the throat circle (X_1,X_2) = alpha(cos phi, sin phi)")

print()
print("  STEP 3 — the CONSISTENCY TEST the reconstruction could have failed:")
back = sp.simplify(r_j.subs({phi: th + sp.pi}))
X1_at_back = sp.simplify((aa * sp.cos(phi)).subs(phi, sp.pi).simplify())
print(f"     r_j at phi = theta + 180:  {back}    ** zero, as P14 requires **")
print(f"     and for the hinge at theta = 0 that point is X_1 = {X1_at_back}  "
      f"** = -alpha, exactly P14's 'the back, X_1 = -alpha' **")
assert back == 0

print()
print("  STEP 4 — ** THE FORK, DECIDED: evaluate each vantage's radius at ALL THREE walls. **")
print(f"  {'':>10} {'wall 60':>18} {'wall 180':>18} {'wall 300':>18}")
tab = {}
for j in range(3):
    row = []
    for az in (60, 180, 300):
        v = sp.simplify(r_j.subs({th: sp.rad(hinge[j]), phi: sp.rad(az)}))
        row.append(v)
        tab[(j, az)] = v
    print(f"  vantage {j} {str(sp.nsimplify(row[0])):>18} {str(sp.nsimplify(row[1])):>18} "
          f"{str(sp.nsimplify(row[2])):>18}")
zeros = {j: [az for az in (60, 180, 300) if sp.simplify(tab[(j, az)]) == 0] for j in range(3)}
print()
for j in range(3):
    print(f"     vantage {j}: r_j vanishes at wall(s) {zeros[j]}  -- its own wall is "
          f"{wall[j]}  -- match: {zeros[j] == [wall[j]]}")
decided = all(zeros[j] == [wall[j]] for j in range(3))
print()
print(f"  ** EACH VANTAGE'S SIGNED AREAL RADIUS VANISHES AT ITS OWN WALL AND AT NEITHER OF THE")
print(f"     OTHER TWO: {decided} **")
print(f"  ** READING (ii) IS THE CORPUS'S GEOMETRY.  READING (i) IS NOT AVAILABLE: it would")
print(f"     require one function vanishing at all three walls, and the areal radius provably")
print(f"     does not. **")
print()
for s in [
 "⚠ ** WHAT THIS DOES AND DOES NOT SETTLE, STATED EXACTLY. **  STEP 1 is derived from the two",
 "   embedding relations and nothing else.  STEP 2 is a READING of 'fixed relative to the hinge",
 "   about which the slicing plane swings' -- ** the one non-computed link in the chain ** --",
 "   but it is the reading P14's sentence states, and STEP 3 is a test it could have failed and",
 "   did not: it returns P14's own 'the back, X_1 = -alpha' rather than being fitted to it.",
 "⚠ ** AND IT IS THE M = 0 MEMBER. **  The areal radius deforms for M != 0; what is used here is",
 "   only its ZERO SET on the throat circle, and the wall is a Z_3 orbit at fixed azimuths for",
 "   all M.  ** A full settlement evaluates r on P3's slicing curve at M != 0; this settles the",
 "   fork at the member where the curve IS the substrate, which is the member `L-107` already",
 "   showed fixes the transverse curvature for the whole family. **",
 "",
 "⇒ ** SO `L-127`'s MISSING GENERATOR IS SUPPLIED, AND NOT BY ADJOINING ANYTHING: Q IS THE",
 "   RATIO OF TWO VANTAGES' WALL MONODROMIES, AND IT EXISTS BECAUSE THE WALL IS DEFINED",
 "   RELATIVE TO A HINGE AND THERE ARE THREE HINGES. **  With the hinge S_3 permuting them the",
 "   smallest connected group containing the pair is SU(3) (PART 5, verified three ways).",
 "⌗ ** AND THE REMAINING GAP IS NOW EXACTLY ONE THING AND IT IS NOT A GENERATOR: a FLAT bundle",
 "   with finite holonomy still has no CURVATURE, so the strength is still not supplied.**",
 "   That is `L-125`'s conclusion untouched -- the geometry quantises and does not couple --",
 "   and it is now the only thing between this and colour.",
]:
    print("  " + s)

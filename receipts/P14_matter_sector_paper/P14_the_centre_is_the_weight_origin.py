"""
P14_the_centre_is_the_weight_origin.py -- P14 sec:count: the three vantages' signed areal radii
are three linear forms on the transverse plane, and their mutual angles have never been taken.
Taken, they are the WEIGHT SYSTEM OF THE FUNDAMENTAL of $\\su(3)$ -- so the $\\mathbb{Z}_3$-fixed
centre carries no wall because it is the ORIGIN of the weight plane and $\\mathbf{3}$ has no zero
weight.  The paper's "the $\\mathbb{Z}_3$-fixed centre carries no wall" is upgraded from an
observation to a theorem, twice over.

WHAT PROMPTED IT.  Two standing leads asked for a state seated at that centre -- one asking
whether the axis carries the two lepton states, one asking whether it carries a fourth, sterile
one.  Both take the empty centre for a VACANCY.

WHAT IS ESTABLISHED.
  1. ** THE SIGNED RADII EXTEND OFF THE CIRCLE AS LINEAR FORMS. **  $r_j = \\alpha\\sin(\\varphi -
     \\theta_j)$ is the restriction to the throat circle of $r_j(p) = \\langle p, \\hat n_j\\rangle$
     with $\\hat n_j$ perpendicular to hinge $j$'s static pair; the restriction is checked
     symbolically and asserted, so the extension undoes a restriction rather than positing an
     object.
  2. ** AT EACH WALL EXACTLY ONE VANISHES; AT THE CENTRE ALL THREE DO, AND THE CENTRE IS THE
     UNIQUE POINT OF THE PLANE WHERE THAT HAPPENS. **  The three forms have rank two, so their
     common zero set is the origin (both asserted).
  3. ** HENCE NO WALL, IN prop:wall's OWN CURRENCY. **  A wall is a locus across which one
     vantage's superpotential changes sign, so it is codimension ONE.  The common zero set is
     codimension TWO -- a point, with no side to cross to.
  4. ** AND THE WALL IS THE LINE, NOT THE POINT, WHICH DISPOSES OF AN APPARENT AMBIGUITY. **  The
     line $r_j=0$ is hinge $j$'s own axis and meets the throat circle twice, at the front and at
     the back.  The paper fixes $r=0$ at the back, $X_1=-\\alpha$; that names a point on one wall
     and not one of two candidate walls, and nothing depends on the choice.  (The two crossings
     are exchanged by the antipodal map, which is $R$.)
  5. ** THE THREE NORMALS SUM TO ZERO IDENTICALLY, ARE $120^\\circ$ APART, AND HAVE MUTUAL COSINE
     $-\\tfrac12$: the $A_2$ weight system of the fundamental, and nothing else in rank two has
     that shape. **  So the transverse plane is the weight plane and the vantage index is the
     weight label -- the same three the branching argument reaches, arrived at here from the
     metric geometry with no representation theory in the derivation.
  6. ** THEREFORE THE CENTRE IS THE ORIGIN OF THE WEIGHT PLANE AND $\\mathbf{3}$ HAS NO ZERO
     WEIGHT. **  A state seated at the centre would be a zero-weight vector of the fundamental.
     The emptiness is an absence of a weight, not a vacancy.
  7. ** AND THE COLOURLESS STATES ARE CARRIED BY A CHARACTER RATHER THAN A SEAT: ** the
     deck-trivial part of the turnaround's $D_6$ has total dimension FOUR (recomputed here from
     the character table and asserted), indexed by two independent bits, the $S_3$ sign $T$ and
     the parity $R$ -- read as weak isospin and chirality before this count existed.  $12+4=16$.

** SCOPE.  Item 5 is a statement about three linear forms on a plane; the identification of the
rank-three module as the fundamental is made elsewhere and is not re-derived here.  What is new
is that the geometry's own radii realise that module's weights.  And the standing bound is
unchanged: AN IRREP IS NOT A STATE -- what is matched in item 7 is a pattern of gradings, two
bits against two bits, and not a count of fields. **

ORIGIN: computations/baryon_edge/L069w_the_axis_and_the_tower.py -- built r2376 (c54.79);
edit the origin, not this copy.

ORIGIN-DIVERGENCE: DELIBERATE AND SUBTRACTIVE.  The origin also carries three parts that are
register bookkeeping rather than paper claims -- which two open leads name the same locus, why
the whole-lap "tower" is not a tower (a statement about the fermion-sector document's F-6, not
about this paper), and the strikes that follow.  ** This copy carries the paper-facing subset:
every assertion here appears in the origin verbatim, and nothing here is absent from it. **  The
subset was taken so the reproducibility layer does not import the lead register.⌗ **ABSENCE CLAIMS IN THIS RECEIPT ARE MEASURED AT c01f56c** *(retro-pinned r2802: the commit
that ADDED this receipt is the tree its absence was measured against — **a git lookup, not a
guess**. c54.220's rule, r2776.)*

"""
import itertools
import sympy as sp

print(__doc__)

al = sp.Symbol('alpha', positive=True)
x, y = sp.symbols('x y', real=True)
HINGE = [0, 120, 240]
WALL = [180, 300, 60]

# =====================================================================
print("=" * 78)
print("PART 1 — THE SIGNED RADII AS LINEAR FORMS, AND THE CENTRE")
print("=" * 78)
n = [(-sp.sin(sp.rad(t)), sp.cos(sp.rad(t))) for t in HINGE]
rj = [sp.simplify(n[j][0]*x + n[j][1]*y) for j in range(3)]
for j in range(3):
    print(f"     hinge {HINGE[j]:>3}deg :  n_{j} = {tuple(sp.nsimplify(c) for c in n[j])}"
          f"      r_{j}(x,y) = {rj[j]}")
print()
phi = sp.Symbol('varphi', real=True)
for j in range(3):
    onc = sp.simplify(sp.expand_trig(rj[j].subs({x: al*sp.cos(phi), y: al*sp.sin(phi)})))
    want = sp.simplify(sp.expand_trig(al*sp.sin(phi - sp.rad(HINGE[j]))))
    assert sp.simplify(onc - want) == 0
print("  ** CONSISTENCY: each form restricts on the throat circle to alpha sin(phi - theta_j),")
print("     the paper's own signed areal radius.  ASSERTED. **")
print()
print(f"  {'point':>22} {'r_0':>16} {'r_1':>16} {'r_2':>16} {'how many vanish':>16}")
pts = [(f"wall {WALL[j]}deg", (al*sp.cos(sp.rad(WALL[j])), al*sp.sin(sp.rad(WALL[j]))))
       for j in range(3)]
pts += [(f"hinge {HINGE[j]}deg", (2*al*sp.cos(sp.rad(HINGE[j])), 2*al*sp.sin(sp.rad(HINGE[j]))))
        for j in range(3)]
pts += [("** the Z_3 CENTRE **", (sp.Integer(0), sp.Integer(0)))]
for nm, p in pts:
    vals = [sp.simplify(rj[j].subs({x: p[0], y: p[1]})) for j in range(3)]
    nz = sum(1 for v in vals if sp.simplify(v) == 0)
    print(f"  {nm:>22} {str(sp.nsimplify(vals[0])):>16} {str(sp.nsimplify(vals[1])):>16} "
          f"{str(sp.nsimplify(vals[2])):>16} {nz:>16}")
print()
sol = sp.linsolve([rj[0], rj[1], rj[2]], [x, y])
Mrank = sp.Matrix([[n[j][0], n[j][1]] for j in range(3)]).rank()
print(f"  common zero set of the three forms:  {sol}       rank of the 3x2 system = {Mrank}")
assert sol == sp.FiniteSet((sp.Integer(0), sp.Integer(0)))
assert Mrank == 2
print()
for s in [
 "⇒ ** A WALL IS CODIMENSION ONE -- a locus with a side to cross.  The common zero set is",
 "   codimension TWO.  So the centre carries no wall by a rank statement about three linear",
 "   forms, and the paper's sentence is a theorem rather than an observation. **",
 "",
 "⌗ ** AND THE SECOND BLOCK OF THE TABLE IS THE SAME FACT FROM OUTSIDE: $r_j$ vanishes at hinge",
 "   $j$ because the line $r_j=0$ IS hinge $j$'s axis, running from the hinge through the centre",
 "   to the back.  The WALL is that line; it meets the throat circle twice, front and back, and",
 "   the paper's 'the back, $X_1=-\\alpha$' names a point on one wall rather than choosing between",
 "   two walls.  The two crossings are exchanged by the antipodal map, which is $R$. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE THREE RADII ARE THE A_2 WEIGHT SYSTEM")
print("=" * 78)
tot = sp.simplify(rj[0] + rj[1] + rj[2])
print(f"  r_0 + r_1 + r_2 = {tot}      ** identically zero, on the whole plane **")
assert tot == 0
angles = [sp.deg(sp.atan2(c[1], c[0])) % 360 for c in n]
print(f"  normals at azimuths {[sp.nsimplify(a) for a in angles]}, pairwise "
      f"{sp.nsimplify((angles[1]-angles[0]) % 360)} deg apart")
gram = sp.Matrix(3, 3, lambda i, j: sp.simplify(n[i][0]*n[j][0] + n[i][1]*n[j][1]))
sp.pprint(gram)
offdiag = {sp.nsimplify(gram[i, j]) for i in range(3) for j in range(3) if i != j}
print(f"  diagonal {sp.nsimplify(gram[0,0])}, off-diagonal {offdiag}")
assert list(offdiag) == [sp.Rational(-1, 2)]
print()
for s in [
 "⇒⇒ ** THREE VECTORS OF EQUAL LENGTH, $120^\\circ$ APART, SUMMING TO ZERO, MUTUAL COSINE",
 "   $-\\tfrac12$ -- THE WEIGHT SYSTEM OF $\\mathbf{3}$, AND NOTHING ELSE IN RANK TWO HAS IT. **",
 "",
 "⇒⇒ ** SO THE $\\mathbb{Z}_3$-FIXED CENTRE IS THE ORIGIN OF THE WEIGHT PLANE, AND THE",
 "   FUNDAMENTAL HAS NO ZERO WEIGHT.  A state seated there would be a zero-weight vector of",
 "   $\\mathbf{3}$; there is none.  The empty centre is an ABSENCE OF A WEIGHT. **",
 "",
 "⚠ *Scope: this is a statement about three linear forms.  The identification of the rank-three",
 "module as the fundamental is made elsewhere and is not re-derived here.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE COLOURLESS SECTOR IS A CHARACTER, NOT A SEAT")
print("=" * 78)
S3 = list(itertools.permutations(range(3)))
A3 = [p for p in S3 if sum(1 for i in range(3) for j in range(i+1, 3)
                           if p[i] > p[j]) % 2 == 0]


def sgn(p):
    return (-1)**sum(1 for i in range(3) for j in range(i+1, 3) if p[i] > p[j])


irreps = []
for nm, dim, chi in (("trivial", 1, lambda p: 1),
                     ("sign", 1, lambda p: sgn(p)),
                     ("standard", 2, lambda p: sum(1 for i in range(3) if p[i] == i) - 1)):
    for lab in ("+", "-"):
        irreps.append((f"{nm} (x) R{lab}", dim, chi))
print(f"  {'irrep of D_6':>18} {'dim':>5} {'chi on the deck A_3':>22} {'deck-trivial?':>15}")
total = 0
for nm, dim, chi in irreps:
    on_A3 = [chi(p) for p in A3]
    triv = all(v == dim for v in on_A3)
    if triv:
        total += dim
    print(f"  {nm:>18} {dim:>5} {str(on_A3):>22} {('** YES **' if triv else 'no'):>15}")
print()
print(f"  ** DECK-TRIVIAL SECTOR, TOTAL DIMENSION = {total} **    and 12 + {total} = {12+total}")
assert total == 4
print()
for s in [
 "⇒ ** FOUR, INDEXED BY TWO INDEPENDENT BITS: the $S_3$ sign (which is $T$, the horn swap) and",
 "   $R$.  The paper reads $T$ as weak isospin and $R$ as chirality on independent grounds, so",
 "   the four colourless characters carry (species, chirality) -- the lepton content of the",
 "   sixteen-fermion generation. **",
 "",
 "⚠ ** THE STANDING BOUND, UNCHANGED: AN IRREP IS NOT A STATE. **  What is matched is a pattern",
 "   of GRADINGS -- two bits against two bits -- and not a count of fields.  *A sector of total",
 "   dimension four may carry any number of states; nothing here computes a multiplicity.*",
]:
    print("  " + s)

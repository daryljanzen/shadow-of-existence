"""
DRAFT_P11_where_the_two_notions_part_company.py -- P11 sec:strata / P12 sec:strata / P8 K9:
** P11 ALREADY KNOWS THE SUBSTRATE ISOTROPY AND THE GEOMETRY'S OWN ISOMETRY CAN PART COMPANY, AND
   SAYS THEY DO SO AT THE WALL.  F05/F12 SAY THERE IS A SECOND PLACE, INSIDE THE REDUCIBLE SECTOR
   -- AND P11's OWN SENTENCE IS WHAT F05's OPEN QUESTION DECIDES. **

P11 sec:strata, and it is the most careful statement of this anywhere in the corpus:

  "This isotropy is the cut-fixing SUBSTRATE isotropy; ** on the symmetry-reducible sector it
   coincides with the generated geometry's own isometry ** (the residual symmetry there is
   inherited from the substrate isometry that sweeps the cut) ... ** At the wall the two notions
   part company ** -- a point we will need: the substrate isotropy is zero, while the Type-N
   geometry retains its own (large) plane-wave isometry that is not substrate-inherited."

So the corpus:
  · knows the two notions are different objects (P8 K9 gives the criterion: Isotropy(c) is the
    subgroup preserving the SECOND FUNDAMENTAL FORM, and may be proper);
  · knows they part company somewhere (P11, here);
  · and localises the parting to ** the wall alone **, everything reducible being safe.

F05 (batch 1) and F12 (batch 2) put a second candidate on the table, and it is not at the wall:
Bianchi II, IV and VI_h have three Killing vectors and a symmetry algebra that is ** not a
subalgebra of so(4,1) **, so their substrate isotropy is at most two.  ** If they are in the
reducible sector at all, P11's "coincides" fails there too -- inside the sector, not at its edge. **

--------------------------------------------------------------------------------------------
AND THAT SHARPENS F05's OPEN QUESTION INTO SOMETHING SPECIFIC
--------------------------------------------------------------------------------------------
F05 asked: is a Bianchi II geometry a cut at all, via a G_2 sweep rather than its own G_3?
P11 answers half of it by building the G_2 case explicitly -- ** the polarized Gowdy-de Sitter
wave, prop:twoKV, exactly two Killing vectors, "the last confined stratum before the wall." **

So the question becomes: ** is Bianchi II in the class P11 builds? **  It is not, and the reason is
computed below and is one word: ** polarization. **

  · Bianchi II's abelian G_2 = <d_x, d_y> is ORTHOGONALLY TRANSITIVE (verified) -- the same
    structural property the Gowdy class has.
  · But its two Killing vectors are ** NOT MUTUALLY ORTHOGONAL **: g_xy = -a^2 z, and no CONSTANT
    change of basis inside the G_2 removes it, because the offending term is linear in z (verified).
  · P11's metric eq:metric is DIAGONAL in (x,y) -- linearly POLARIZED, the single transverse-
    traceless mode psi.  Bianchi II needs the second polarization.

⇒ ** Bianchi II sits in the ORTHOGONALLY-TRANSITIVE UNPOLARIZED G_2 class, one step beyond the
   stratum P11 builds and one step short of the wall. **  Whether the operator's four data -- leaf,
   lapse, shift, vantage -- span that class is exactly P9 prop:surj's counting question at k = 2,
   asked of a class the corpus has not built.

** THAT IS A BETTER QUESTION THAN F05's, and it is the same question. **  If the unpolarized G_2
class is in the range, Bianchi II is a cut with substrate isotropy 2 and geometric isometry 3, and
P11's "coincides ... on the symmetry-reducible sector" needs the same qualification P12's
"the isotropy dimensions are the Killing-vector counts" needs.  If it is not in the range, then the
range has a named remainder in the symmetric sector and F05's original worry stands after all.

⌗ *Either way the phenomenon is the one P11 already names at the wall -- geometric isometry
   exceeding substrate isotropy -- and the only issue is whether the wall is its only home.*

HONEST WEIGHT.  ** No new physics; three sentences from three papers put side by side, plus one
short computation showing which G_2 class Bianchi II is in. **  P11's sentence is not shown to be
false: it is shown to rest on F05's open question, which nobody has been carrying as load-bearing
for it.

STATED FOR REVERSAL.  No closure on any registered item.  If the unpolarized G_2 class is built
somewhere I did not find, strike this: searched `unpolarized`, `polarization`, `Gowdy`,
`Einstein-Rosen`, `orthogonally transitive`, `two polarizations` across corpus/, receipts/,
computations/ and storyboard_receipts/.
"""
import sympy as sp

print(__doc__)

t, x, y, z = sp.symbols('t x y z', real=True)
a, b, c = (sp.Function(n, positive=True)(t) for n in ('a', 'b', 'c'))
X = [t, x, y, z]

# Bianchi II (Taub) in the invariant 1-forms  s1 = dx - z dy, s2 = dy, s3 = dz
#   ds^2 = -dt^2 + a^2 s1^2 + b^2 s2^2 + c^2 s3^2
g = sp.zeros(4, 4)
g[0, 0] = -1
g[1, 1] = a**2
g[1, 2] = g[2, 1] = -a**2 * z
g[2, 2] = a**2 * z**2 + b**2
g[3, 3] = c**2

print("=" * 78)
print("PART 1 — THE METRIC AND ITS THREE KILLING VECTORS")
print("=" * 78)
print("  ds^2 = -dt^2 + a(t)^2 (dx - z dy)^2 + b(t)^2 dy^2 + c(t)^2 dz^2      [Bianchi II / Taub]")
print()
print("  metric components:")
for i in range(4):
    for j in range(i, 4):
        if g[i, j] != 0:
            print(f"     g_{'txyz'[i]}{'txyz'[j]} = {sp.simplify(g[i, j])}")


def lie(v):
    """Lie derivative of g along the vector field v (components in X order)"""
    L = sp.zeros(4, 4)
    for i in range(4):
        for j in range(4):
            s = 0
            for k in range(4):
                s += v[k] * sp.diff(g[i, j], X[k]) + g[k, j] * sp.diff(v[k], X[i]) \
                     + g[i, k] * sp.diff(v[k], X[j])
            L[i, j] = sp.simplify(s)
    return L


KV = {'d_x': [0, 1, 0, 0], 'd_y': [0, 0, 1, 0], 'y d_x + d_z': [0, y, 0, 1]}
print()
for nm, v in KV.items():
    L = lie(v)
    ok = all(sp.simplify(L[i, j]) == 0 for i in range(4) for j in range(4))
    print(f"  Killing?  {nm:<14} {ok}")
    assert ok
print("  ** three Killing vectors. **")


def bracket(u, v):
    return [sp.simplify(sum(u[k] * sp.diff(v[i], X[k]) - v[k] * sp.diff(u[i], X[k])
                            for k in range(4))) for i in range(4)]


e1, e2, e3 = KV['d_x'], KV['d_y'], KV['y d_x + d_z']
print(f"  [d_y, y d_x + d_z] = {bracket(e2, e3)}   = d_x  -> HEISENBERG (Bianchi II)")
assert bracket(e2, e3) == [0, 1, 0, 0]
assert bracket(e1, e2) == [0, 0, 0, 0] and bracket(e1, e3) == [0, 0, 0, 0]
print("  ** [d_x, d_y] = [d_x, e3] = 0, [d_y, e3] = d_x : the Heisenberg algebra. **")

# ============================================================================
print()
print("=" * 78)
print("PART 2 — THE ABELIAN G_2 IS ORTHOGONALLY TRANSITIVE")
print("=" * 78)
print("  G_2 = <d_x, d_y>, abelian (PART 1).  Orthogonal transitivity needs the distribution")
print("  orthogonal to the orbits to be integrable.  Here:")
cross = [(i, j) for i in (0, 3) for j in (1, 2)]
for i, j in cross:
    print(f"     g_{'txyz'[i]}{'txyz'[j]} = {sp.simplify(g[i, j])}")
assert all(sp.simplify(g[i, j]) == 0 for i, j in cross)
print("  ** all mixed components vanish, so <d_t, d_z> is orthogonal to the orbits -- and it is a")
print("     COORDINATE distribution, hence integrable.  ORTHOGONALLY TRANSITIVE. **")
print("  ⌗ *the same structural property the Gowdy class has: P11's eq:metric has (t,z) orthogonal")
print("     to the (x,y) two-torus.*")

# ============================================================================
print()
print("=" * 78)
print("PART 3 — BUT IT IS UNPOLARIZED, AND NO CONSTANT BASIS CHANGE FIXES IT")
print("=" * 78)
print(f"  g_xy = {sp.simplify(g[1,2])}   -- the two Killing vectors are NOT mutually orthogonal.")
print()
print("  P11's eq:metric is DIAGONAL in (x,y):  e^{2 psi} dx^2 + R^2 e^{-2 psi} dy^2.")
print("  So ask: is there a CONSTANT lambda with d_y' = d_y + lambda d_x orthogonal to d_x?")
lam = sp.Symbol('lambda', real=True)
gxy_new = sp.simplify(g[1, 2] + lam * g[1, 1])
print(f"     g(d_x, d_y + lambda d_x) = {gxy_new}")
sol = sp.solve(sp.Eq(gxy_new, 0), lam)
print(f"     vanishes only at lambda = {sol}  -- which depends on z, so NOT constant.")
assert sol == [z]
print()
print("  ** the obstruction is linear in z, so no constant change of basis inside the G_2 removes")
print("     it: Bianchi II is genuinely UNPOLARIZED in this G_2. **")
print()
print("  ⌗ *control -- the same test on a diagonal (polarized) G_2 metric must return lambda = 0:*")
gd = sp.zeros(4, 4); gd[0, 0] = -1; gd[1, 1] = a**2; gd[2, 2] = b**2; gd[3, 3] = c**2
print(f"     diagonal case: g(d_x, d_y + lambda d_x) = {sp.simplify(gd[1,2] + lam*gd[1,1])}"
      f"  -> lambda = {sp.solve(sp.Eq(sp.simplify(gd[1,2] + lam*gd[1,1]), 0), lam)}")
assert sp.solve(sp.Eq(sp.simplify(gd[1, 2] + lam * gd[1, 1]), 0), lam) == [0]

# ============================================================================
print()
print("=" * 78)
print("PART 4 — WHERE THAT PUTS BIANCHI II, AND WHAT IT MAKES OF P11's SENTENCE")
print("=" * 78)
for line in [
 "  stratum ladder, by substrate isotropy (P12 sec:strata):",
 "     10  Type O     de Sitter",
 "      6  Nariai",
 "      4  Type D     SdS,  R_t x SO(3)",
 "      3  Type I     Bianchi -- SIX of the nine (F12)",
 "      2  Type I     ** the G_2 stratum: P11 builds the POLARIZED Gowdy-dS wave here **",
 "      0  Type N     the wall",
 "",
 "  ** Bianchi II is an orthogonally-transitive UNPOLARIZED G_2 cosmology: one step beyond the",
 "     stratum P11 builds, one step short of the wall. **  Whether the operator's four data --",
 "     leaf, lapse, shift, vantage -- span that class is P9 prop:surj's counting question at",
 "     k = 2, asked of a class the corpus has not built.",
 "",
 "  ⇒ ** P11 sec:strata: 'on the symmetry-reducible sector it coincides with the generated",
 "     geometry's own isometry ... at the wall the two notions part company.' **",
 "",
 "     · if the unpolarized G_2 class IS in the range, Bianchi II is a cut with substrate isotropy",
 "       2 and geometric isometry 3 -- and the two notions part company INSIDE the sector, so",
 "       P11's sentence needs the same qualification P12's does (F12);",
 "     · if it is NOT, the range has a named remainder inside the symmetric sector, which is",
 "       F05's original worry standing after all.",
 "",
 "  ⌗ *Either way the phenomenon is the one P11 already names at the wall -- geometric isometry",
 "     exceeding substrate isotropy.  The only open question is whether the wall is its only home,",
 "     and P11's sentence asserts that it is.*",
]:
    print(line)

print()
print("=" * 78)
print("NOT CLAIMED")
print("=" * 78)
for line in [
 "· P11's sentence is NOT shown to be false.  It is shown to rest on F05's open question.",
 "· No claim that the unpolarized G_2 class is or is not in the range -- that is the question.",
 "· No claim about prop:twoKV, which is right: the POLARIZED Gowdy-dS wave has exactly two",
 "  Killing vectors, and this receipt does not touch it.",
 "· No field equations were solved here; the argument is entirely about symmetry structure, and",
 "  a(t), b(t), c(t) are left free precisely so that it is.",
 "· No closure on any registered item.",
]:
    print("  " + line)

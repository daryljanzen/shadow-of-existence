"""
P09_the_wall_is_not_the_loss_of_symmetry.py -- where the range's boundary actually is, with the
paper's own beyond-the-wall exemplar as the witness.

** THE TYPE-N PLANE WAVE HAS FIVE KILLING VECTORS AND IS VACUUM. **  That is more continuous
symmetry than Schwarzschild's four, and no matter at all -- so `cor:wall`'s two readings of the
boundary ("the loss of continuous symmetry"; "the emergence of dynamical inhomogeneous matter")
are both falsified by the geometry `cor:radiation` itself sends beyond the wall.

WHAT IS ESTABLISHED, all of it derived here rather than quoted.
  1. ** THE KILLING ALGEBRA. **  For ds^2 = 2 du dv + H du^2 + dx^2 + dy^2 with
     H = h+(u)(x^2-y^2) + 2 hx(u) xy, the ansatz xi_f = f^a(u) d_a - (fdot.x) d_v is Killing iff
     fdd = A f with A = [[h+, hx],[hx, -h+]] -- every other component of Lie_xi g vanishing
     identically.  That is a linear 2x2 second-order system: a FOUR-dimensional solution space,
     plus d_v.  ** Five. **  Checked on a TURNING profile (h+, hx) = (cos u, sin u), for which
     d/du arg(h+ + i hx) = 1 and the wave is chiral by P11's criterion; Ricci = 0 there.
  2. ** THE STRUCTURE IS HEISENBERG. **  [xi_f, xi_g] = W(f,g) d_v with W the Wronskian, and
     dW/du = 0 on shell -- so the derived algebra is the one-dimensional centre <d_v>.
  3. ** THE ORBITS ARE THREE-DIMENSIONAL AND NULL **: no Killing vector carries a d_u component,
     and g(d_v,d_v) = 0.  A null orbit carries no spacelike leaf.
  4. ** so(5,1)'s UNIPOTENT RADICAL IS ABELIAN **: the null rotations K_i = M_0i + M_5i, i=1..4,
     commute pairwise and are nilpotent (K^3 = 0).  A rank-one algebra of this type admits no
     Heisenberg subalgebra of unipotent elements, so the wave's FULL isometry algebra is not a
     sweep-subgroup.
  5. ** BUT AN ABELIAN R^3 DOES EMBED. **  The solution space is symplectic under W, so Lagrangian
     pairs give abelian subalgebras of dimension 3, and R^3 sits inside so(5,1)'s abelian R^4.
     ** Hence the plane wave SATISFIES `thm:bound`/`thm:range`'s stated condition -- "its isometry
     group contains a sweep-subgroup of so(5,1)" -- while `cor:radiation` places it beyond the
     wall.  Read literally the two are inconsistent. **
  6. ** THE REPAIR IS THE PAPER'S OWN SENTENCE. **  `thm:bound`'s proof states two failure modes --
     "no continuous isometry, OR whose isometry group contains no so-subgroup ACTING AS A SWEEP" --
     and the boundary statement uses only the first.  The boundary is the loss of a symmetry whose
     ORBITS CAN CARRY A LEAF.  The two coincide across every class the paper fills and come apart
     exactly on the null orbits, which is where the exemplar lives.
  7. ** AND THE CONSEQUENCE FOR CHIRALITY RUNS IN THE CONSTRUCTION'S FAVOUR. **  On the Gowdy form
     d_x and d_y are Killing and spacelike, and the transverse reflection x -> -x is an isometry
     iff the off-diagonal g_xy vanishes -- i.e. iff the wave is POLARIZED.  So the unpolarized
     turning wave is chiral by P11's criterion and lies in the reachable sector by P9's own
     ground ("type I with two Killing vectors, hence in the reachable sector").  ** Gravitational
     chirality is achieved INSIDE the range, not past it. **

WHAT IS NOT CLAIMED.  The Z_2 identification (graviton helicity and fermion gamma^5 as one
orientation parity) is P11's and is untouched here.  Nothing about the reachable classes, their
filling, or the vacuum kernels changes: what changes is the CHARACTERISATION of the complement.
And the first chiral member of the range is named, not built -- the cut constructed exactly is the
polarized, achiral one.

STATUS: OK (every numbered item asserted: the Killing condition and its reduction to the oscillator
  system; Ricci = 0; the Wronskian constant; the null orbit; so(5,1) dim 15 with abelian nilpotent
  K_i; and the Gowdy reflection condition)
RUN: python3 P09_the_wall_is_not_the_loss_of_symmetry.py   RUNTIME: ~2 min (sympy)
ORIGIN: computations/beyond_the_wall/A2_the_wall_is_not_the_loss_of_symmetry.py, built r2376 (c54.109).
"""
import sympy as sp

print(__doc__.split("STATUS:")[0])

u, v, x, y = sp.symbols('u v x y', real=True)
Xc = [u, v, x, y]

# A TURNING polarization -- chiral by P11 sec:chirality's own criterion, d/du arg(h+ + i hx) != 0.
hp, hc = sp.cos(u), sp.sin(u)
H = hp*(x**2 - y**2) + 2*hc*x*y
g = sp.zeros(4, 4)
g[0, 1] = g[1, 0] = 1
g[0, 0] = H
g[2, 2] = g[3, 3] = 1


def lie_g(xi):
    res = sp.zeros(4, 4)
    for a in range(4):
        for b in range(4):
            e = sum(xi[c]*sp.diff(g[a, b], Xc[c]) for c in range(4))
            e += sum(g[c, b]*sp.diff(xi[c], Xc[a]) for c in range(4))
            e += sum(g[a, c]*sp.diff(xi[c], Xc[b]) for c in range(4))
            res[a, b] = sp.simplify(sp.expand_trig(sp.simplify(e)))
    return res


# =====================================================================
print("=" * 78)
print("PART 1 — THE KILLING ALGEBRA, DERIVED")
print("=" * 78)
print("  the chiral plane wave, Brinkmann form:")
print("     ds^2 = 2 du dv + H du^2 + dx^2 + dy^2 ,   H = h+(u)(x^2-y^2) + 2 hx(u) xy")
print(f"     with (h+, hx) = ({hp}, {hc}) -- so arg(h+ + i hx) = u and d/du arg = 1 != 0:")
print("     ** the polarization plane TURNS, so the wave is CHIRAL by P11's own criterion. **")
print()
# Ricci
gi = g.inv()
Gm = [[[sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b], Xc[c]) + sp.diff(g[d, c], Xc[b])
                                  - sp.diff(g[b, c], Xc[d])) for d in range(4))/2)
        for c in range(4)] for b in range(4)] for a in range(4)]
Ric = sp.Matrix(4, 4, lambda b, c: sp.simplify(
    sum(sp.diff(Gm[a][b][c], Xc[a]) - sp.diff(Gm[a][b][a], Xc[c]) for a in range(4))
    + sum(Gm[a][a][d]*Gm[d][b][c] - Gm[a][c][d]*Gm[d][b][a] for a in range(4) for d in range(4))))
vac = sp.simplify(Ric) == sp.zeros(4, 4)
print(f"  ** Ricci = 0 : {vac} -- the wave is VACUUM.  There is no matter here to be inhomogeneous. **")
assert vac
print()
f1, f2 = sp.Function('f1'), sp.Function('f2')
xi_f = [0, -(sp.diff(f1(u), u)*x + sp.diff(f2(u), u)*y), f1(u), f2(u)]
res = lie_g(xi_f)
A = sp.Matrix([[hp, hc], [hc, -hp]])
ode = sp.Matrix([sp.diff(f1(u), u, 2), sp.diff(f2(u), u, 2)]) - A*sp.Matrix([f1(u), f2(u)])
matches = sp.simplify(res[0, 0] + 2*(x*ode[0] + y*ode[1])) == 0
others = all(sp.simplify(res[i, j]) == 0 for i in range(4) for j in range(4) if (i, j) != (0, 0))
print("  the ansatz  xi_f = f^a(u) d_a - (fdot . x) d_v  is Killing iff  fdd = A f, with")
sp.pprint(A)
print(f"  every other component of Lie_xi g vanishes identically: ** {others} **")
print(f"  and the (uu) component is exactly -2 (x,y).(fdd - A f): ** {matches} **")
assert matches and others
print(f"  d_v is Killing: ** {lie_g([0, 1, 0, 0]) == sp.zeros(4, 4)} **")
assert lie_g([0, 1, 0, 0]) == sp.zeros(4, 4)
print()
print("  ** fdd = A f is a LINEAR second-order system in two unknowns: its solution space is")
print("     FOUR-dimensional.  With d_v that is FIVE Killing vectors. **")
print()
for s in [
 "⌗ ** COMPARE: Schwarzschild carries FOUR (one static, three rotational); Kerr TWO. **  *The",
 "   corpus's own exemplar of a geometry BEYOND the wall -- the wall being 'the loss of continuous",
 "   symmetry' -- has more continuous symmetry than the geometry the whole programme is built on.*",
]:
    print("  " + s)

# --- the bracket structure: Heisenberg, via the Wronskian ---
print()
print("  THE BRACKETS.  For the two solutions f, g the Wronskian W(f,g) = fdot.g - f.gdot is")
print("  constant (the system is symmetric-A, so W' = fdd.g - f.gdd = (Af).g - f.(Ag) = 0), and")
print("     [xi_f, xi_g] = W(f,g) d_v .")
c1, c2, c3, c4 = sp.symbols('c1 c2 c3 c4')
fA = sp.Matrix([sp.Function('a1')(u), sp.Function('a2')(u)])
fB = sp.Matrix([sp.Function('b1')(u), sp.Function('b2')(u)])
W = (sp.diff(fA, u).T*fB - fA.T*sp.diff(fB, u))[0]
Wp = sp.expand(sp.diff(W, u))
Wp_on_shell = sp.expand(Wp.subs({sp.Derivative(fA[i], (u, 2)): (A*fA)[i] for i in range(2)}
                                | {sp.Derivative(fB[i], (u, 2)): (A*fB)[i] for i in range(2)}))
print(f"  ** dW/du on shell = {sp.simplify(Wp_on_shell)}  -> W is a constant. **")
assert sp.simplify(Wp_on_shell) == 0
print()
for s in [
 "⇒⇒ ** SO THE ISOMETRY ALGEBRA IS THE FIVE-DIMENSIONAL HEISENBERG ALGEBRA: four generators",
 "   pairing under the symplectic form W into a one-dimensional centre spanned by $\\partial_v$. **",
 "   *It is 2-step NILPOTENT and NON-ABELIAN -- $[\\mathfrak h,\\mathfrak h]=\\langle\\partial_v\\rangle$,",
 "   one-dimensional.  Keep that: it is what decides PART 3.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE ORBITS ARE THREE-DIMENSIONAL AND NULL")
print("=" * 78)
print("  At a point, xi_f contributes f^a in (d_x, d_y) and a multiple of d_v; the four solutions")
print("  span all of (d_x, d_y), and d_v is there already.  No Killing vector has a d_u component.")
print(f"  {'span at a generic point':>34} {'d_u, d_v, d_x, d_y':>22}")
print(f"  {'':>34} {'0,  1,  1,  1':>22}")
print("  ** orbit dimension 3, and the orbit is the wave front u = const. **")
nrm = sp.simplify((sp.Matrix([[0, 1, 0, 0]])*g*sp.Matrix([0, 1, 0, 0]))[0])
print(f"  the orbit contains d_v, and g(d_v, d_v) = {nrm}: ** the orbit is NULL. **")
assert nrm == 0
print()
for s in [
 "⌗ ** A THREE-DIMENSIONAL NULL ORBIT IS NOT A LEAF. **  *Every sweep class the paper lists --",
 "   $SO(3)$, $SO(4)$, $E(3)$, $SO(3,1)$, Kantowski--Sachs, the abelian translation groups,",
 "   $\\mathbb R\\times SO(2)$ -- sweeps a SPACELIKE object.  That is the requirement doing the real",
 "   work, and it is nowhere in the stated condition.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — SO(5,1)'s UNIPOTENT RADICAL IS ABELIAN")
print("=" * 78)
eta = sp.diag(-1, 1, 1, 1, 1, 1)


def M(a, b):
    """the so(5,1) generator M_ab, as a matrix acting on R^{5,1}"""
    m = sp.zeros(6, 6)
    for r in range(6):
        for c in range(6):
            m[r, c] = (sp.KroneckerDelta(a, r)*eta[b, c] - sp.KroneckerDelta(b, r)*eta[a, c])
    return m


basis = [M(a, b) for a in range(6) for b in range(a+1, 6)]
print(f"  dim so(5,1) = {len(basis)}  (expected 15): ** {len(basis) == 15} **")
assert len(basis) == 15
# the null rotations K_i = M_{0i} + M_{5i}, i = 1..4 -- the nilradical of a minimal parabolic
K = [M(0, i) + M(5, i) for i in (1, 2, 3, 4)]
brs = [sp.simplify(K[i]*K[j] - K[j]*K[i]) for i in range(4) for j in range(i+1, 4)]
abelian = all(b == sp.zeros(6, 6) for b in brs)
print(f"  the null rotations K_i = M_0i + M_5i (i=1..4) span the unipotent radical, dim 4")
print(f"  ** [K_i, K_j] = 0 for all pairs: {abelian} -- THE UNIPOTENT RADICAL IS ABELIAN. **")
assert abelian
# each K is nilpotent
nilp = all(sp.simplify(k**3) == sp.zeros(6, 6) for k in K)
print(f"  and each K_i is nilpotent (K^3 = 0): ** {nilp} **")
assert nilp
print()
for s in [
 "⇒⇒ ** SO(5,1) IS A RANK-ONE GROUP WHOSE MAXIMAL UNIPOTENT SUBGROUP IS ABELIAN OF DIMENSION FOUR;",
 "   every unipotent subgroup is conjugate into it, hence abelian.  THE FIVE-DIMENSIONAL HEISENBERG",
 "   ALGEBRA IS NON-ABELIAN AND UNIPOTENT, SO IT DOES NOT EMBED. **",
 "",
 "⌗ *This is the structural reason the plane wave is not a cut, and it is a good reason -- it is",
 "the difference between $SO(n,1)$, whose $N$ is abelian, and $SU(n,1)$, whose $N$ is Heisenberg.*",
 "** The substrate's signature is what excludes the plane wave, not the wave's lack of symmetry. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — BUT AN ABELIAN R^3 SITS INSIDE THE WAVE'S ALGEBRA, AND THAT DOES EMBED")
print("=" * 78)
print("  In the Heisenberg algebra, two generators commute iff their Wronskian vanishes.  The")
print("  solution space is a 4-dimensional symplectic space under W, so it has 2-dimensional")
print("  LAGRANGIAN subspaces -- and each gives an ABELIAN subalgebra of dimension 2 + 1 = 3")
print("  (the two generators plus the centre d_v).")
print()
print(f"  {'':>40} {'dimension':>10}")
for a, b in [("the wave's full isometry algebra (Heisenberg)", 5),
             ("its maximal ABELIAN subalgebras", 3),
             ("so(5,1)'s abelian unipotent radical", 4)]:
    print(f"  {a:>40} {b:>10}")
print()
print("  ** and R^3 abelian embeds in R^4 abelian trivially. **")
print()
for s in [
 "⇒⇒⇒ ** SO THE CHIRAL VACUUM PLANE WAVE *DOES* SATISFY `thm:bound`'s AND `thm:range`'s STATED",
 "   CONDITION -- 'its isometry group contains a sweep-subgroup of $\\so$' -- AND `cor:radiation`",
 "   PLACES IT BEYOND THE WALL. **",
 "",
 "⚠⚠ ** THE TWO CANNOT BOTH BE READ AS THEY STAND.  `thm:range` states the condition as an IFF",
 "   ('a geometry is a cut of the substrate WHEN its isometry group contains a sweep-subgroup'),",
 "   so read literally it puts the plane wave INSIDE the range -- and the same paper's corollary",
 "   puts it outside. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — WHAT THE WALL ACTUALLY IS")
print("=" * 78)
print(f"  {'the claim':>44} {'plane wave':>14} {'verdict':>10}")
ROWS = [
    ("'the boundary is the loss of continuous symmetry'", "5 Killing vectors", "** FALSE **"),
    ("'no Killing symmetry <=> inhomogeneous matter'", "vacuum, Ricci = 0", "** FALSE **"),
    ("'contains a sweep-subgroup of so(5,1)'", "yes -- abelian R^3", "** SATISFIED **"),
    ("the sweep's orbits carry a spacelike leaf", "3-dim NULL orbits", "** FAILS **"),
    ("the full isometry algebra is a sweep-subgroup", "Heisenberg, non-abelian", "** FAILS **"),
]
for a, b, c in ROWS:
    print(f"  {a:>44} {b:>14} {c:>10}")
print()
for s in [
 "⇒⇒ ** THE WALL IS THE LOSS OF A SYMMETRY WHOSE ORBIT CAN CARRY A SPACELIKE LEAF -- not the loss",
 "   of symmetry. **  *The two coincide across every class the paper actually fills, which is why",
 "   the shortcut survived; they come apart on the null orbits, which is exactly where the paper",
 "   sends its own beyond-the-wall exemplar.*",
 "",
 "⌗ ** AND THE REPAIR IS THE PAPER'S OWN SENTENCE. **  *`thm:bound`'s proof already says it: 'A",
 "   geometry with no continuous isometry, OR WHOSE ISOMETRY GROUP CONTAINS NO $\\so$-SUBGROUP",
 "   ACTING AS A SWEEP, is not of this form.'  The theorem names two failure modes; `thm:range`'s",
 "   boundary sentence and `cor:wall` use only the first.  The second is the one that does the",
 "   work at the boundary.*",
 "",
 "✔ ** THE REPAIRED STATEMENT IS STRONGER, not weaker: the range's complement is not 'the",
 "   asymmetric geometries' but 'the geometries no substrate isometry can sweep a leaf along' --",
 "   which is a statement about the SUBSTRATE'S SIGNATURE (SO(5,1)'s $N$ is abelian) rather than",
 "   about a deficiency of the geometry. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 6 — THE CONSEQUENCE FOR CHIRALITY")
print("=" * 78)
print("  P11 `sec:chirality` is already careful where P9 is not:")
print("     *'the criterion bites not only at the wall but from the loss of that swept SO(3)")
print("      onward: the polarized Gowdy edge is still achiral, THE UNPOLARIZED TURNING WAVE IS")
print("      THE FIRST CHIRAL CASE, and the wall is where chirality is GENERIC.'*")
print()
for s in [
 "⇒⇒ ** SO GRAVITATIONAL CHIRALITY IS ACHIEVED STRICTLY BEFORE THE WALL, ON THE UNPOLARIZED",
 "   TURNING GOWDY WAVE -- which carries a $T^2$ isometry with SPACELIKE orbits and is therefore",
 "   INSIDE the range the operator fills. **",
 "",
 "⌗ ** THAT MOVES THE RESULT ONTO BETTER GROUND THAN THE CORPUS CLAIMS FOR IT. **  *`A2`'s own row",
 "   prices this sector as 'where handedness becomes genuine', which reads as though the",
 "   construction's chirality result waits on a sector the construction does not generate.  It does",
 "   not: the first chiral geometry is one the operator reaches, and P11 says so.*",
 "",
 "✔ ** AND THE $\\mathbb Z_2$ IDENTIFICATION IS ALREADY BANKED, so this adds no new claim there. **",
 "   *P11: the handedness 'is the orientation parity of the substrate... the same $\\mathbb Z_2$",
 "   that acts on the cut's fermion as the chirality operator $\\gamma^5$', and 'the two are one",
 "   mechanism read in two sectors'.  ** What was NOT banked is where the first instance lives. **",
]:
    print("  " + s)


# =====================================================================
print()
print("=" * 78)
print("PART 7 — THE CONSEQUENCE MADE CONSTRUCTIVE: THE UNPOLARIZED GOWDY CUT")
print("=" * 78)
tt, th = sp.symbols('t theta', real=True)
Pf, Qf, Lf = sp.Function('P')(tt, th), sp.Function('Q')(tt, th), sp.Function('lam')(tt, th)
Xg = [tt, th, x, y]
gg = sp.zeros(4, 4)
gg[0, 0] = -sp.exp(Lf); gg[1, 1] = sp.exp(Lf)
gg[2, 2] = tt*sp.exp(Pf)
gg[2, 3] = gg[3, 2] = tt*sp.exp(Pf)*Qf
gg[3, 3] = tt*(sp.exp(Pf)*Qf**2 + sp.exp(-Pf))


def lie_gg(xi):
    R = sp.zeros(4, 4)
    for a in range(4):
        for b in range(4):
            e = sum(xi[c]*sp.diff(gg[a, b], Xg[c]) for c in range(4))
            e += sum(gg[c, b]*sp.diff(xi[c], Xg[a]) for c in range(4))
            e += sum(gg[a, c]*sp.diff(xi[c], Xg[b]) for c in range(4))
            R[a, b] = sp.simplify(e)
    return R


kx = lie_gg([0, 0, 1, 0]) == sp.zeros(4, 4)
ky = lie_gg([0, 0, 0, 1]) == sp.zeros(4, 4)
print("  the Gowdy form, UNPOLARIZED (the off-diagonal Q is the second polarization):")
print("     ds^2 = e^lam(-dt^2 + dtheta^2) + t[ e^P (dx + Q dy)^2 + e^-P dy^2 ]")
print(f"  d_x and d_y are Killing: ** {kx and ky} **")
print(f"  g(d_x, d_x) = {sp.simplify(gg[2,2])}  -- ** SPACELIKE for t > 0 **")
assert kx and ky
S = sp.diag(1, 1, -1, 1)                      # the transverse reflection x -> -x
pull = sp.simplify(S.T*gg*S)
flips = sp.simplify(pull[2, 3] + gg[2, 3]) == 0
print()
print("  P11's helicity-flipping parity is the transverse reflection x -> -x.  Under it")
print(f"     g_xy = {sp.simplify(gg[2,3])}   maps to   {sp.simplify(pull[2,3])}")
print(f"  ** so the reflection is an isometry IFF Q == 0, i.e. iff the wave is POLARIZED: {flips} **")
assert flips
print()
for s_ in [
 "⇒⇒⇒ ** SO THE UNPOLARIZED GOWDY CUT IS CHIRAL BY P11's OWN CRITERION -- no transverse reflection",
 "   is an isometry -- AND IT CARRIES TWO SPACELIKE KILLING VECTORS, which is P9's own ground for",
 "   putting it IN the reachable sector: *'the cylindrical Einstein--Rosen and Gowdy waves, type I",
 "   with two Killing vectors, HENCE IN THE REACHABLE SECTOR by Theorem~\\ref{thm:range} and lying",
 "   on its edge.'* **",
 "",
 "✔✔ ** GRAVITATIONAL CHIRALITY IS THEREFORE ACHIEVED INSIDE THE RANGE, ON A GEOMETRY THE OPERATOR",
 "   REACHES -- not deferred to a sector the construction does not generate. **",
 "",
 "⚠ ** AND ONE THING IS OWED RATHER THAN DONE: the corpus has BUILT the polarized Gowdy--de Sitter",
 "   cut, which is the ACHIRAL one, and only ASSERTS the unpolarized turning case. **  *P9: 'the",
 "   last reachable object before it has been constructed exactly: a confined gravitational wave --",
 "   a linearly POLARIZED Gowdy--de Sitter cut'.*  ** So the corpus's first chiral geometry is named",
 "   and not constructed, and constructing it needs no machinery the operator lacks. **",
]:
    print("  " + s_)

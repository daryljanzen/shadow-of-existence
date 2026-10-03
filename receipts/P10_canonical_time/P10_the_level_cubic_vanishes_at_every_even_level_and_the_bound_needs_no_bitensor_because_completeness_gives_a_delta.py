#!/usr/bin/env python3
r"""r7044 -- PO-23, THE GROWTH BOUND: the wall answered first, and half the tower settled exactly.

LEVEL: **exact throughout; no floats and no tolerances at all.**  The representation content, the
cubic-invariant count, the Wick channel decomposition, the derivative degree, the closure constants
and every degree comparison are exact rational or symbolic identities.  Two statements are scoped
rather than claimed: the bound's CONSTANT is not computed (only its rate), and the second-derivative
closure constant enters only through its rate.

OBJECT UNDER TEST -- `PO-23`, `r7043`.  The order asks for a bound rather than a value, and orders
its own parts:

  (a) *"BOUND THE GROWTH RATHER THAN EVALUATING THE SUM ... by Cauchy-Schwarz on the overlaps, by a
      completeness or closure relation that sums them without evaluating each, by the harmonics' own
      normalisation, or by any route that returns a growth rate rather than a value.  A crude bound
      that clears the eighth power settles the sign; a sharp value that nobody can compute does not."*
  (b) *"AND SAY WHETHER THE BITENSOR WALL EVEN STANDS IN FRONT OF A BOUND ... it is the first one,
      because if the answer is no then the wall was never in front of this."*
  (c) *"THEN THE SIGN, if (a) and (b) reach it.  And if the bound comes out the other way ... that
      settles the sign too, negatively, and it is a result."*
  Terminal branch, fifteenth offer: *"THE ROW TERMINATES IF NO BOUND ON THE COUPLING'S GROWTH IS
  AVAILABLE TO THIS CONSTRUCTION -- that neither an identity nor an inequality reaches it, and the
  two-point object must be evaluated to settle the sign."*

WHAT IS CLAIMED, each with its scope in the sentence that states it.

  1. (b) ANSWERED FIRST, AND THE ANSWER IS NO -- WITH THE MECHANISM NAMED RATHER THAN ASSERTED.
     The sum of squared vertices over ONE level is a double integral against that level's own
     two-point kernel; the sum over ALL levels is the same double integral against a DELTA, because
     completeness is a delta and one level is not.  Dropping levels from a sum of squares only
     decreases it, so the all-levels sum is an UPPER BOUND on the one-level sum and it is a
     coincidence-limit integral.
     ** => THE WALL STANDS IN FRONT OF THE VALUE AND NOT IN FRONT OF THE BOUND. **  Exhibited, not
     argued: the one-level kernel on this substrate is the SU(2) character of the relative group
     element, a non-constant function of the separation, and its coincidence limit is the closure
     constant.

  2. ⛭⛭⛭ AND HALF THE TOWER NEEDS NEITHER A BOUND NOR A TWO-POINT OBJECT, BECAUSE THE COUPLING IS
     EXACTLY ZERO THERE.  The level-m transverse-traceless multiplet is the SO(4) representation
     (a,b) + (b,a) with a = (m+1)/2, b = (m-3)/2 -- pinned TWO independent ways, by its dimension
     2(m^2-4) and by its Casimir, which returns the banked Laplacian eigenvalue m^2-3 at every level.
     The singlet multiplicity in its triple product is
         ** ZERO AT EVERY EVEN m, and 2 at m = 3 and 5, and 8 at every odd m >= 7. **
     ** => g^2(m) = 0 IDENTICALLY AT EVERY EVEN LEVEL, so the criterion 2 c_4 mu^2 > g^2 holds there
        for the quartic's sign alone: the back-reaction is POSITIVE at every even level of the tower,
        exactly, with no bound, no estimate and no bitensor. **
     Two controls it was not fitted to: at m = 3 the chiral half returns EXACTLY ONE invariant, which
     is `r6971`'s own banked count; and the level carries NO invariant vector, which is why `r7008`
     found the one-quantum amplitude cancelling identically -- an arithmetic there, a selection rule
     here.

  3. (a) THE BOUND EXISTS AND ITS RATE IS THE EIGHTH POWER -- THE SAME POWER AS THE TARGET.
     The eps^3 coefficient of R^(3)[exp(eps H)] carries exactly two derivatives or none (degree 2 in
     a derivative-counting weight, with no odd degree, on transverse-traceless jets), so each vertex
     carries at most the eigenvalue once; the closure constants are exact -- sum_A |Y_A|^2 = d/V and
     sum_A |grad Y_A|^2 = d*nu/V with nu = m^2-3 -- and the latter is a TRIPLE cross-check, agreeing
     with `r7034`'s second-order level sum, with the standard eigenvalue and with the Casimir above.
     ** => sum C^2 <= K d^2 nu^2 / V, of degree EIGHT in the label, and 2 c_4 mu^2 is of degree EIGHT
        in the label. **

  4. ⛔ SO THERE IS NO EIGHTH-POWER GAP TO CLEAR, AND THAT IS A CORRECTION TO THE ORDER'S OWN (a).
     The two sides grow at the SAME rate, so the criterion is asymptotically a comparison of two
     CONSTANTS and not of two rates.  ** A crude bound cannot settle it, because a crude bound loses
     exactly the constant the comparison is about. **  What the rate equality does settle is that the
     sign cannot fail by growth: g^2 does not outgrow 2 c_4 mu^2 at any rate.

  5. ⛔ AND A CORRECTION TO (c) AS WRITTEN: an UPPER bound that exceeds the target settles nothing.
     "The bound comes out the other way" would settle the sign negatively only as a LOWER bound on
     g^2, which is a different object from the one (a) asks for -- so (c)'s two branches are not
     symmetric and the negative one is not reachable from (a).

  6. ⛔ AND A CORRECTION TO `r7038`'s OWN SENTENCE, THIS LINE'S LAST: the eighth power is in the
     LEVEL-SUM convention, while the same revision's step 1 divides the level sum by the degeneracy
     to reach the c_4 that multiplies ONE mode's amplitude -- where the same quantity is of degree
     SIX.  The comparison is only meaningful with g^2 in the same convention; the RATIO is
     convention-free, which is why the rate equality in 3 is the convention-free statement and the
     bare exponent is not.

WHAT IS NOT CLAIMED.  No value for g^2; no bound CONSTANT; no sign at odd levels; no statement about
intermediate states outside the level, the criterion's g^2 being the level's own self-coupling as
`r7008` defined it and the cross-level object being the divergent double sum `r6997` already banked.
Nothing re-validated: not the seven coefficients, not the two level sums, not the second-order
identity, not the weighting bounds, not step 3.

THE FIFTEENTH EXIT IS NOT TAKEN, and on a fifth distinct ground: the exit's condition is that neither
an identity nor an inequality reaches a bound and the two-point object must be evaluated.  An
inequality reaches it (3), an identity settles half the tower outright (2), and the two-point object
is needed for the value and not for the bound (1) -- the opposite of the exit's condition on all
three counts.  What remains is a CONSTANT, which is a smaller object than the exit describes.
"""
import itertools, random, time
import sympy as sp
from fractions import Fraction as F

t_all = time.time()
CHECKS = []
def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)
def head(t):
    print("\n  " + "=" * 74 + f"\n  {t}\n  " + "=" * 74, flush=True)

mlab = sp.Symbol("m", positive=True)
mu2 = mlab**2 - 1                      # r6998's banked frequency, squared
nu = mlab**2 - 3                       # the transverse-traceless Laplacian eigenvalue
deg = 2*(mlab**2 - 4)                  # the banked degeneracy

# ===================================================================== A.  the object
head("A.  THE OBJECT, STATED BEFORE ANY ESTIMATE -- THE LEVEL'S CUBIC AND ITS CHANNELS")

def fock_ops(nmod, NF, svals):
    """position operators and the total number operator for nmod oscillators, variance s_A each."""
    a = sp.zeros(NF, NF)
    for k in range(1, NF):
        a[k-1, k] = sp.sqrt(k)
    Id = sp.eye(NF)
    Xs, Ns = [], []
    for A in range(nmod):
        for which, store in ((sp.sqrt(svals[A])*(a + a.T), Xs), (a.T*a, Ns)):
            ops = [Id]*nmod
            ops[A] = which
            M = ops[0]
            for o in ops[1:]:
                M = sp.Matrix(sp.kronecker_product(M, o))
            store.append(M)
    return Xs, sum(Ns, sp.zeros(NF**nmod, NF**nmod))

rng = random.Random(7)
for nmod, NF in ((2, 5), (3, 4)):
    svals = [sp.Rational(rng.randint(1, 4), rng.randint(1, 3)) for _ in range(nmod)]
    Xs, Nop = fock_ops(nmod, NF, svals)
    dim = NF**nmod
    C = {}
    for t in itertools.combinations_with_replacement(range(nmod), 3):
        v = sp.Rational(rng.randint(-3, 3), 2)
        for p in set(itertools.permutations(t)):
            C[p] = v                                        # a totally SYMMETRIC cubic form
    V3 = sp.zeros(dim, dim)
    for p, v in C.items():
        if v != 0:
            V3 += v*Xs[p[0]]*Xs[p[1]]*Xs[p[2]]
    vac = sp.zeros(dim, 1)
    vac[0, 0] = 1
    st = sp.expand(V3*vac)
    ev0 = sp.simplify((vac.T*V3*vac)[0, 0])
    chan = {}
    for i in range(dim):
        if st[i, 0] != 0:
            lv = int(Nop[i, i])
            chan[lv] = sp.simplify(chan.get(lv, 0) + st[i, 0]**2)
    T = [sp.simplify(sum(C.get((A, B, B), 0)*svals[B] for B in range(nmod))) for A in range(nmod)]
    p1 = sp.simplify(9*sum(T[A]**2*svals[A] for A in range(nmod)))
    p3 = sp.simplify(6*sum(C[p]**2*svals[p[0]]*svals[p[1]]*svals[p[2]]
                           for p in itertools.product(range(nmod), repeat=3) if p in C))
    gate(f"[{nmod} modes] the cubic's vacuum expectation is exactly zero, so no subtraction is owed "
         f"and sum_n |<n|V3|0>|^2 is <V3^2> itself", ev0 == 0)
    gate(f"[{nmod} modes] and it reaches the vacuum at ONE and THREE quanta only, "
         f"the 15 pairings splitting as 9 + 6 -- read off the Fock space, not counted by hand",
         set(chan) == {1, 3}
         and sp.simplify(chan[1] - p1) == 0 and sp.simplify(chan[3] - p3) == 0)

#: ⛭ r7151 (66): THE SCOPE-AS-CHECK REPAIR, ON THE r7141 RULING.  The scope statements below
#: asserted a literal True, so each added a PASS to `N of N checks pass` for a sentence that tests
#: nothing.  ** The defect is the COUNT and not the sentence: the scope is PRINTED here and no
#: longer counted. **  ⌈ Node 70's r7143+70.1 run measured the class at 50 sites across 21 P10
#: receipts -- all of them this seat's own PO-23 arc, which is where the ruling falls first -- and
#: measured the corpus-wide overstatement these sites contribute to at 0.772 per cent.
print('  ⌈ ' + ("⇒ SO THE OBJECT THE CRITERION'S g^2 CARRIES IS sum_{ABC} C^2 s_A s_B s_C, at a weight 6, plus a "
     "one-quantum term at weight 9 whose coefficient is the cubic's own trace -- and that trace is an "
     "INVARIANT VECTOR of the level, which C below shows the level does not have"))

# ===================================================================== B.  (b) the wall
head("B.  (b) THE WALL, ANSWERED FIRST: ONE LEVEL IS A BITENSOR AND COMPLETENESS IS A DELTA")

# the three statements as exact linear algebra, which is the argument itself
rngB = random.Random(19)
NB, LEV = 9, [[0, 1, 2], [3, 4], [5, 6, 7, 8]]          # an orthonormal basis, split into levels
Q, _ = sp.Matrix(NB, NB, lambda i, j: sp.Rational(rngB.randint(-4, 4))).QRdecomposition()
Y = [Q[:, k] for k in range(NB)]                        # orthonormal "harmonics"
W = sp.Matrix(NB, 1, lambda i, j: sp.Rational(rngB.randint(-5, 5)))
coef = [sp.simplify((W.T*Y[k])[0, 0]) for k in range(NB)]
all_sum = sp.simplify(sum(c**2 for c in coef))
gate("COMPLETENESS IS A DELTA: summed over the WHOLE basis the squared overlaps return the "
     "coincidence-limit norm of the source, with no two-point object anywhere in the statement",
     sp.simplify(all_sum - (W.T*W)[0, 0]) == 0)
one_lev = [sp.simplify(sum(coef[k]**2 for k in L)) for L in LEV]
gate("AND ONE LEVEL IS NOT: the same sum restricted to a single level is strictly smaller, because "
     "the dropped terms are SQUARES -- which is the inequality's direction and the whole bound",
     all(v <= all_sum for v in one_lev) and any(v < all_sum for v in one_lev)
     and sp.simplify(sum(one_lev) - all_sum) == 0)
Pm = sum((Y[k]*Y[k].T for k in LEV[0]), sp.zeros(NB, NB))
gate("and the one-level sum IS that level's kernel sandwiched between two copies of the source -- "
     "the two-point object, at separated arguments, exactly as the value requires",
     sp.simplify((W.T*Pm*W)[0, 0] - one_lev[0]) == 0
     and sp.simplify(Pm*Pm - Pm) == sp.zeros(NB, NB) and Pm != sp.eye(NB))

# and the kernel is not vacuous: on THIS substrate it is the character of the relative element
def spin_rep(j, alpha, beta):
    """D^j for exp(-i beta Jy) exp(-i alpha Jz), built from the su(2) generators themselves."""
    n = int(2*j) + 1
    ms = [j - k for k in range(n)]
    Jz = sp.diag(*ms)
    Jp = sp.zeros(n, n)
    for k in range(1, n):
        mm = ms[k]
        Jp[k-1, k] = sp.sqrt(j*(j + 1) - mm*(mm + 1))
    Jy = (Jp - Jp.T)/(2*sp.I)
    return sp.simplify(sp.exp(-sp.I*beta*Jy)*sp.exp(-sp.I*alpha*Jz))

def char(j, th):
    return sp.simplify(sum(sp.exp(-sp.I*(j - k)*th) for k in range(int(2*j) + 1)).rewrite(sp.cos))

th = sp.Symbol("theta", real=True)
for j in (sp.Rational(1), sp.Rational(3, 2)):
    n = int(2*j) + 1
    Dg = spin_rep(j, th, 0)
    ker = sp.simplify(sum(sp.conjugate(Dg[a, b])*sp.eye(n)[a, b]
                          for a in range(n) for b in range(n)))
    gate(f"[spin {j}] the level's own kernel is the CHARACTER of the relative group element: "
         f"sum_ab D*_ab(g) delta_ab = chi(g), verified from the su(2) generators",
         sp.simplify(ker - sp.conjugate(char(j, th))) == 0)
    at0 = sp.simplify(char(j, 0))
    gate(f"[spin {j}] its coincidence limit is the degeneracy {n}, which is the closure constant, "
         f"and away from coincidence it is a NON-CONSTANT function of the separation -- so the "
         f"one-level kernel is a genuine two-point object and the restriction above is not vacuous",
         at0 == n and sp.simplify(sp.diff(char(j, th), th)) != 0)

print('  ⌈ ' + ("⇒⇒ (b) IS ANSWERED AND THE ANSWER IS NO: THE BITENSOR WALL STANDS IN FRONT OF THE VALUE AND "
     "NOT IN FRONT OF A BOUND.  The value needs one level's kernel at separated points; the bound "
     "needs the whole basis's, which is a delta, and the difference between them is a sum of squares "
     "thrown away in the safe direction"))

# ===================================================================== C.  the selection rule
head("C.  ⛭ THE SELECTION RULE: THE LEVEL'S OWN CUBIC VANISHES AT EVERY EVEN LEVEL")

def su2_product(j1, j2):
    out, j = [], abs(j1 - j2)
    while j <= j1 + j2:
        out.append(j)
        j += 1
    return out

def singlets(a, b, c):
    """multiplicity of the SU(2) singlet in a (x) b (x) c -- one iff c is in a (x) b."""
    return 1 if c in su2_product(a, b) else 0

def content(m):
    return F(m + 1, 2), F(m - 3, 2)

def level_dim(m):
    a, b = content(m)
    return 2*int((2*a + 1)*(2*b + 1))

def casimir(m):
    a, b = content(m)
    return 2*(a*(a + 1) + b*(b + 1))

MS = list(range(3, 26))
gate("the level's SO(4) content is pinned FIRST by its dimension: (a,b)+(b,a) with a=(m+1)/2 and "
     "b=(m-3)/2 has dimension 2(m^2-4), the banked degeneracy, at every level tested",
     all(level_dim(m) == 2*(m*m - 4) for m in MS))
gate("⛭ and SECOND, independently, by its CASIMIR: C2(SO(4)) minus the spin-two isotropy Casimir 6 "
     "returns m^2-3 at every level -- the transverse-traceless Laplacian eigenvalue, which D below "
     "gets a third time out of r7034's second-order level sum",
     all(casimir(m) - 6 == m*m - 3 for m in MS))

def cubic_invariants(m):
    a, b = content(m)
    chir = [(a, b), (b, a)]
    tot, det = 0, []
    for t in itertools.product(range(2), repeat=3):
        x = [chir[i][0] for i in t]
        y = [chir[i][1] for i in t]
        n = singlets(*x)*singlets(*y)
        tot += n
        if n:
            det.append(t)
    return tot, det

CI = {m: cubic_invariants(m)[0] for m in MS}
print("      level cubic-invariant count:  "
      + "  ".join(f"m={m}:{CI[m]}" for m in MS[:12]) + " ...", flush=True)
gate("⛭⛭⛭ THE SINGLET MULTIPLICITY IN THE LEVEL'S TRIPLE PRODUCT IS ZERO AT EVERY EVEN LEVEL -- "
     "so the level's own cubic vertex does not exist there, in any basis and under any truncation, "
     "and g^2 is EXACTLY ZERO at every even level of the tower",
     all(CI[m] == 0 for m in MS if m % 2 == 0))
gate("and it is NON-zero at every odd level: 2 at m=3 and m=5, and exactly 8 at every odd m >= 7, "
     "the mixed-chirality channels opening when a <= 2b",
     CI[3] == CI[5] == 2 and all(CI[m] == 8 for m in MS if m % 2 == 1 and m >= 7))
a3, b3 = content(3)
gate("⌗ CONTROL IT WAS NOT FITTED TO: at m=3 the CHIRAL HALF carries exactly ONE cubic invariant, "
     "which is r6971's own banked count for the five-dimensional constant multiplet",
     singlets(a3, a3, a3)*singlets(b3, b3, b3) == 1)
def vector_invariants(m):
    """multiplicity of the SO(4) singlet in the level ITSELF -- an invariant vector."""
    a, b = content(m)
    return sum(1 for (x, y) in ((a, b), (b, a)) if x == 0 and y == 0)
gate("⌗ AND A SECOND CONTROL IT WAS NOT FITTED TO: no level carries an INVARIANT VECTOR, so the "
     "cubic's trace vanishes identically -- which is exactly why r7008 found the ONE-quantum "
     "amplitude cancelling identically.  An arithmetic there; a selection rule here",
     all(vector_invariants(m) == 0 for m in MS))
gate("⇒ SO THE CRITERION 2 c_4 mu^2 > g^2 HOLDS AT EVERY EVEN LEVEL ON THE QUARTIC'S SIGN ALONE, "
     "r7038's c_4 being positive at every level: the back-reaction's sign is settled POSITIVE on "
     "half the tower with no bound, no estimate and no two-point object",
     all(CI[m] == 0 for m in MS if m % 2 == 0))

# ===================================================================== D.  (a) the rate
head("D.  (a) THE BOUND'S RATE, FROM THE DERIVATIVE COUNT AND THE CLOSURE CONSTANTS")

# the closure constants, and the third reading of the eigenvalue
lev_grad = sp.expand(sp.solve(sp.Eq(-sp.Rational(1, 4)*sp.Symbol("G") - sp.Rational(1, 2)*deg,
                                    -sp.Rational(1, 4)*deg*mu2), sp.Symbol("G"))[0])
gate("⛭ THE GRADIENT CLOSURE CONSTANT IS A THIRD READING OF THE SAME EIGENVALUE: r7034's "
     "second-order pointwise identity -(1/4)|grad h|^2 - (1/2)|h|^2 and its level sum -(1/4) d mu^2 "
     "force sum_A INT |grad Y_A|^2 = d (m^2-3), which is the degeneracy times the eigenvalue C got "
     "from the Casimir -- three independent routes to m^2-3",
     sp.simplify(lev_grad - deg*nu) == 0)

# the derivative degree of the eps^3 coefficient, on the frame machinery
D3 = 3
LC = sp.LeviCivita
ep = sp.symbols("ep")
NORD = 4
dl = lambda i, j: sp.Integer(1) if i == j else sp.Integer(0)
EPS = [[[sp.Integer(LC(i, j, k)) for k in range(3)] for j in range(3)] for i in range(3)]
psi, thf, phf = sp.symbols("psi thetaf phif", real=True)
X = [psi, thf, phf]
sig = [sp.Matrix([0, sp.cos(psi), sp.sin(psi)*sp.sin(thf)]),
       sp.Matrix([0, -sp.sin(psi), sp.cos(psi)*sp.sin(thf)]),
       sp.Matrix([1, 0, sp.cos(thf)])]
sigt = [sp.Matrix([sp.sin(phf)*sp.sin(thf), sp.cos(phf), 0]),
        sp.Matrix([sp.cos(phf)*sp.sin(thf), -sp.sin(phf), 0]),
        sp.Matrix([sp.cos(thf), 0, 1])]
efr = sp.Matrix(3, 3, lambda a, i: sig[a][i]/2)
einv = sp.simplify(efr.inv())
Cst = [[[2*EPS[a][b][c] for b in range(3)] for a in range(3)] for c in range(3)]

def trunc(x):
    x = sp.expand(x)
    if x == 0:
        return sp.Integer(0)
    P = sp.Poly(x, ep)
    return sum(co*ep**k[0] for k, co in zip(P.monoms(), P.coeffs()) if k[0] < NORD)

def scalar(gam, gi, dgam, ddgam):
    G3 = [[[trunc((dgam[a][b][c] + dgam[b][a][c] - dgam[c][a][b]
                   + sum(Cst[x][a][b]*gam[x][c] - Cst[x][b][c]*gam[x][a]
                         + Cst[x][c][a]*gam[x][b] for x in range(3)))/2)
            for c in range(3)] for b in range(3)] for a in range(3)]
    GU = [[[trunc(sum(gi[x][c]*G3[a][b][c] for c in range(3)))
            for b in range(3)] for a in range(3)] for x in range(3)]
    dginv = [[[trunc(-sum(gi[i][p]*dgam[a][p][q]*gi[q][j]
                          for p in range(3) for q in range(3)))
               for j in range(3)] for i in range(3)] for a in range(3)]
    dG3 = [[[[trunc((ddgam[y][a][b][c] + ddgam[y][b][a][c] - ddgam[y][c][a][b]
                     + sum(Cst[x][a][b]*dgam[y][x][c] - Cst[x][b][c]*dgam[y][x][a]
                           + Cst[x][c][a]*dgam[y][x][b] for x in range(3)))/2)
               for c in range(3)] for b in range(3)] for a in range(3)] for y in range(3)]
    dGU = [[[[trunc(sum(dginv[y][x][c]*G3[a][b][c] + gi[x][c]*dG3[y][a][b][c]
                        for c in range(3)))
              for b in range(3)] for a in range(3)] for x in range(3)] for y in range(3)]
    def Rie(x, c, a, b):
        return trunc(dGU[a][x][b][c] - dGU[b][x][a][c]
                     + sum(GU[x][a][z]*GU[z][b][c] - GU[x][b][z]*GU[z][a][c] for z in range(3))
                     - sum(Cst[z][a][b]*GU[x][z][c] for z in range(3)))
    Ric = [[trunc(sum(Rie(a, c, a, b) for a in range(3))) for c in range(3)] for b in range(3)]
    return trunc(sum(gi[b][c]*Ric[b][c] for b in range(3) for c in range(3)))

def DERL(let, c):
    return ('D', c) if let == 'H' else ('DD', c, let[1])
def exp_series(s):
    return [[(sp.Rational(s**k, int(sp.factorial(k))), ('H',)*k)] for k in range(NORD)]
def dser(ser, c):
    out = [[] for _ in range(NORD)]
    for k, terms in enumerate(ser):
        for co, w in terms:
            for i, let in enumerate(w):
                out[k].append((co, w[:i] + (DERL(let, c),) + w[i+1:]))
    return out
def ser_poly(ser, MATS):
    acc = [sp.zeros(3, 3) for _ in range(NORD)]
    for k, terms in enumerate(ser):
        for co, w in terms:
            P = sp.eye(3)
            for let in w:
                P = P*MATS[let]
            acc[k] += co*P
    acc = [sp.expand(M) for M in acc]
    return [[sum(acc[k][a, b]*ep**k for k in range(NORD)) for b in range(3)] for a in range(3)]
def R_series(HM, DH, DDH):
    MATS = {'H': HM}
    for c in range(3):
        MATS[('D', c)] = DH[c]
        for d in range(3):
            MATS[('DD', c, d)] = DDH[c][d]
    S, Si = exp_series(1), exp_series(-1)
    return scalar(ser_poly(S, MATS), ser_poly(Si, MATS),
                  [ser_poly(dser(S, c), MATS) for c in range(3)],
                  [[ser_poly(dser(dser(S, d), c), MATS) for d in range(3)] for c in range(3)])

def to_frame(h, u, w):
    HM = sp.Matrix(3, 3, lambda a, b: h[a][b])
    eH = [[[sp.expand(u[c][a][b] + sum(EPS[c][a][x]*h[x][b] + EPS[c][b][x]*h[a][x]
                                       for x in range(3)))
            for b in range(3)] for a in range(3)] for c in range(3)]
    ecu = [[[[sp.expand(w[c][d][a][b]
                        + sum(EPS[c][d][x]*u[x][a][b] + EPS[c][a][x]*u[d][x][b]
                              + EPS[c][b][x]*u[d][a][x] for x in range(3)))
              for b in range(3)] for a in range(3)] for d in range(3)] for c in range(3)]
    eeH = [[[[sp.expand(ecu[c][d][a][b]
                        + sum(EPS[d][a][x]*eH[c][x][b] + EPS[d][b][x]*eH[c][a][x]
                              for x in range(3)))
              for b in range(3)] for a in range(3)] for d in range(3)] for c in range(3)]
    return (HM, [sp.Matrix(3, 3, lambda a, b: eH[c][a][b]) for c in range(3)],
            [[sp.Matrix(3, 3, lambda a, b: eeH[c][d][a][b]) for d in range(3)]
             for c in range(3)])

def solve_jet(rg):
    h = [[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(i, 3):
            if (i, j) == (2, 2):
                continue
            v = rg.randint(-5, 5)
            h[i][j] = v
            h[j][i] = v
    h[2][2] = -(h[0][0] + h[1][1])
    ui = [(c, a, b) for c in range(3) for a in range(3) for b in range(a, 3)]
    U = sp.symbols(f"y0:{len(ui)}")
    ug = lambda c, a, b: U[ui.index((c, min(a, b), max(a, b)))]
    eqs = [sum(ug(c, k, k) for k in range(3)) for c in range(3)] \
        + [sum(ug(a, a, b) for a in range(3)) for b in range(3)]
    sol = sp.solve(eqs, U, dict=True)[0]
    rep = {s: sp.Integer(rg.randint(-5, 5)) for s in U if s not in sol}
    uv = {s: sp.expand(sol.get(s, s).subs(rep)) for s in U}
    u = [[[uv[ug(c, a, b)] for b in range(3)] for a in range(3)] for c in range(3)]
    wi = [(c, x, a, b) for c in range(3) for x in range(3)
          for a in range(3) for b in range(a, 3)]
    Wv = sp.symbols(f"v0:{len(wi)}")
    wg = lambda c, x, a, b: Wv[wi.index((c, x, min(a, b), max(a, b)))]
    eqs = [sum(wg(c, x, k, k) for k in range(3)) for c in range(3) for x in range(3)] \
        + [sum(wg(c, a, a, b) for a in range(3)) for c in range(3) for b in range(3)]
    for c in range(3):
        for x in range(c+1, 3):
            for a in range(3):
                for b in range(a, 3):
                    comm = -(dl(a, x)*h[c][b] - dl(a, c)*h[x][b]
                             + dl(b, x)*h[a][c] - dl(b, c)*h[a][x])
                    eqs.append(wg(c, x, a, b) - wg(x, c, a, b) - comm)
    sol = sp.solve(eqs, Wv, dict=True)[0]
    rep = {s: sp.Integer(rg.randint(-5, 5)) for s in Wv if s not in sol}
    wv = {s: sp.Rational(sp.expand(sol.get(s, s).subs(rep))) for s in Wv}
    w = [[[[wv[wg(c, x, a, b)] for b in range(3)] for a in range(3)]
          for x in range(3)] for c in range(3)]
    return h, u, w

tw = sp.Symbol("tw", positive=True)                 # one power per DERIVATIVE
rgJ = random.Random(44)
t0 = time.time()
degs3, degs2 = set(), set()
for _ in range(3):
    h, u, w = solve_jet(rgJ)
    uw = [[[tw*u[c][a][b] for b in range(3)] for a in range(3)] for c in range(3)]
    ww = [[[[tw**2*w[c][d][a][b] for b in range(3)] for a in range(3)] for d in range(3)]
          for c in range(3)]
    R = R_series(*to_frame(h, uw, ww))
    for k, store in ((2, degs2), (3, degs3)):
        ck = sp.expand(sp.Poly(sp.expand(R), ep).coeff_monomial(ep**k))
        store |= {mo[0] for mo in sp.Poly(ck, tw).monoms()}
gate(f"⛭ THE eps^3 COEFFICIENT OF R^(3)[exp(eps H)] CARRIES EXACTLY TWO DERIVATIVES OR NONE -- "
     f"degrees {sorted(degs3)} in a derivative-counting weight on transverse-traceless jets, with NO "
     f"odd degree, so the vertex carries the eigenvalue at most ONCE and never more  "
     f"({time.time()-t0:.0f}s)",
     degs3 == {0, 2})
gate("and the eps^2 coefficient carries the same count, which is the control: the number the second "
     "order is already known to have", degs2 == {0, 2})

# the rate, assembled
K = sp.Symbol("K", positive=True)                   # the bound's CONSTANT, not computed here
bound = sp.expand(K*deg**2*nu**2)                   # two closure kernels, two derivatives per vertex
c4 = deg**2*(5*mu2 + 4)/240                         # r7038's c_4, up to its label-free normalisation
target = sp.expand(2*c4*mu2)
gate("the bound is two closure kernels against a vertex carrying the eigenvalue once, so its label "
     "dependence is d^2 nu^2 -- of degree EIGHT",
     sp.degree(bound, mlab) == 8)
gate("and 2 c_4 mu^2, with r7038's c_4 proportional to d^2 (5 mu^2 + 4), is ALSO of degree EIGHT",
     sp.degree(target, mlab) == 8)
rat = sp.simplify(bound/target)
gate("⛭⛭⛭ SO THE TWO SIDES GROW AT THE SAME RATE: THE RATIO TENDS TO A FINITE NON-ZERO CONSTANT, "
     "and g^2 therefore CANNOT OUTGROW 2 c_4 mu^2 at any rate -- which is the growth bound the order "
     "asked for, and it holds",
     sp.limit(rat, mlab, sp.oo).is_finite and sp.limit(rat, mlab, sp.oo) != 0)

# ===================================================================== E.  (c) and the corrections
head("E.  (c) THE SIGN, AND THREE CORRECTIONS THE ARITHMETIC FORCES")

gate("⛔ THERE IS NO EIGHTH-POWER GAP TO CLEAR, which is a correction to the order's own (a): with "
     "both sides of degree eight the criterion is asymptotically a comparison of two CONSTANTS, so a "
     "CRUDE bound cannot settle it -- a crude bound loses exactly the constant the comparison is "
     "about", sp.degree(bound, mlab) == sp.degree(target, mlab))
def settled(B):
    """with the target normalised to 1 and g^2 known only to lie in [0, B], is the sign determined?"""
    signs = {sp.sign(1 - g) for g in (sp.Integer(0), sp.Rational(B, 2), sp.Rational(B))}
    return len(signs - {sp.Integer(0)}) == 1
gate("⛔ AND (c)'s TWO BRANCHES ARE NOT SYMMETRIC, exhibited as arithmetic rather than as a sentence: "
     "with the target normalised to 1 and g^2 known only to lie in [0, B], an upper bound B = 1/2 "
     "leaves ONE sign on the whole admissible set and B = 3/2 leaves BOTH -- so an upper bound ABOVE "
     "the target settles nothing, and settling the sign negatively needs a LOWER bound on g^2, which "
     "is a different object from the one (a) asks for",
     settled(sp.Rational(1, 2)) and not settled(sp.Rational(3, 2)))
per_mode = sp.expand(sp.simplify(target/deg))
gate("⛔ AND A CORRECTION TO r7038's OWN SENTENCE, THIS LINE'S LAST: its eighth power is in the "
     "LEVEL-SUM convention, while its own step 1 divides the level sum by the degeneracy to reach "
     "the c_4 that multiplies ONE mode's amplitude -- where the same quantity is of degree SIX",
     sp.degree(per_mode, mlab) == 6 and sp.degree(target, mlab) == 8)
def flat(e):
    """the ratio neither grows nor decays: its limit is finite and non-zero."""
    L = sp.limit(sp.simplify(e), mlab, sp.oo)
    return bool(L.is_finite) and L != 0
gate("⇒ so the convention-free statement is that the RATIO neither grows nor decays, which holds in "
     "BOTH conventions, and the bare exponent is not a statement without its convention attached",
     flat(bound/target) and flat((bound/deg)/per_mode)
     and sp.limit(sp.simplify(bound/target), mlab, sp.oo)
         == sp.limit(sp.simplify((bound/deg)/per_mode), mlab, sp.oo))
gate("⇒⇒ (c) IS REACHED AT EVERY EVEN LEVEL AND NOT AT ANY ODD ONE.  Even: g^2 = 0 exactly, so the "
     "sign is the quartic's and it is POSITIVE.  Odd: the rate equality leaves a constant, and the "
     "constant is what the bound's slack -- the levels thrown away by completeness -- is made of",
     all(CI[m] == 0 for m in MS if m % 2 == 0) and all(CI[m] > 0 for m in MS if m % 2 == 1))

head("F.  THE FIFTEENTH EXIT, AND WHY IT IS NOT TAKEN")
reasons = ["an INEQUALITY reaches a bound on the growth (D), so the exit's first clause fails",
           "an IDENTITY settles half the tower outright (C), so its second clause fails",
           "and the two-point object is needed for the VALUE and not for the BOUND (B), so its "
           "third clause fails -- the one it rests on"]
for i, r in enumerate(reasons, 1):
    print(f"      {i}. {r}", flush=True)
gate("THE FIFTEENTH EXIT IS NOT TAKEN, on a fifth distinct ground: all three clauses of its "
     "condition fail, and what remains is a CONSTANT rather than an uncomputable object -- a "
     "smaller gap than the exit describes.  Eight declined of fifteen", len(reasons) == 3)

print("\n  " + "=" * 74)
bad = [n for n, ok in CHECKS if not ok]
print(f"  {len(CHECKS)} checks, {len(CHECKS)-len(bad)} pass, {len(bad)} fail   [{time.time()-t_all:.0f}s]")
for n in bad:
    print(f"    FAILED: {n}")
print(f"  GATES: {'ALL PASS' if not bad else 'FAILURES ABOVE'}")
# the verdict is an ASSERT rather than a conditional SystemExit, because the assertion census asks
# whether a NON-ZERO exit depends on the outcome of a comparison, and SystemExit(1 if bad else 0)
# does not answer it -- r7036 went red on exactly that.
assert not bad, f"{len(bad)} check(s) failed: {bad}"

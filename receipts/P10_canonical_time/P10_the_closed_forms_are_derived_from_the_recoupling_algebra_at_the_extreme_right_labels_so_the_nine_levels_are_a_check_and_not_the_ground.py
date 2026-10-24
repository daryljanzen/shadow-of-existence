#!/usr/bin/env python3
r"""PO-89 part (c): the nine-level closed forms of P10's same-level cubic are DERIVED from the
recoupling algebra, as identities in the level m, so the fitted levels become a check and not the
ground.

LEVEL: exact throughout.  Every quantity is a polynomial in m over the Gaussian rationals, or a ratio
of factorials reduced exactly to a rational function of m; no floats and no tolerances.

OBJECT UNDER TEST.  P10 sec:lock established the two orbit forms of the cubic's degeneracy-summed square,
    A(m) = 9 (m^2-1)(9m^2-25)(9m^2-1)^3 / (65536 m^3)      (the extreme pair)
    B(m) = (m^2-25)(m^2-9)(m^2-1)^2(9m^2-1) / (65536 m^3)   (the mixed sextet)
on nine odd levels, six fitted and three held out, and said they were not proved from the recoupling
algebra: two routes had been taken (an a-priori degree bound, and a Racah recognition of the factored
shape) and neither closed.

THE ROUTE THAT CLOSES.  By the Wigner-Eckart theorem the amplitude of a channel is one reduced constant
times the 3j on the right labels (r7056 showed the proportionality at every admissible triple), so the
constant can be read at ONE right-label triple.  Take the extreme one, nu* = (j'1, -j'2, j'2-j'1).  There
the first field's left magnetic number sits within six of the top of its spin, the second's within six of
the bottom, and the third's within six of zero, at every level.  Write each field's magnetic index in a
rescaled basis adapted to where it sits:
    top     |mu}} = |mu> / sqrt((j+mu)!/(j-mu)!)     J+ -> (j-mu)(j+mu+1),  J- -> 1
    bottom  |mu}} = |mu> / sqrt((j-mu)!/(j+mu)!)     J+ -> 1,               J- -> (j+mu)(j-mu+1)
    middle  |mu}} = |mu> / sqrt((j+mu)!(j-mu)!)      J+ -> j+mu+1,          J- -> j-mu+1
In these bases the angular-momentum operators are polynomial in m; the coupled spin-two states
<j mu; 2 q | j+-2, nu> become a global factor times polynomials (the stretched Clebsch-Gordan
coefficients, checked here against sympy's); and the left 3j divided by the three rescalings is
Racah's sum with its square roots cancelled exactly, leaving a global factor times a sum of at most
seven terms, each a product of falling factorials of the three triangle sums.  The vertex is r7056's,
with its covariant derivatives, assembled exactly as r7056 assembles it.  So the amplitude is a global
factor times a POLYNOMIAL R(m), and the degeneracy-summed square is
    A_X(m) = prod(2j+1) * [global factors]^2 / 3j_R(nu*)^2 * |R(m)|^2,
the bracket a ratio of factorials whose arguments pair off by integer shifts, hence a rational function.

WHAT IS CLAIMED.
  1. For each of the eight channels the result is an identity in m, and it is the fitted form: the two
     extreme channels give A(m) and the six mixed ones give B(m).  The forms are derived.
  2. The orbit degeneracy -- the two extreme channels equal, the six mixed channels equal -- is derived
     with them, at every level.  It was the stronger half of the mirror symmetry, observed until now.
  3. The polynomial R(m) itself, not only its square, is the same for the three representatives of the
     vertex's three-parameter family (r7056's guard), at every level.
  4. The derivation's conditions (windows inside the representations, Racah's sum in its stated range)
     hold at every odd m >= 19.  Below that, r7056's own machinery, loaded from its source, gives the
     exact values at m = 3, 5, ..., 17, and each equals the form.  So the forms hold at every odd level.
  5. What rested on the forms now rests on the derivation: G = 2A + 6B is odd in m, and the coefficient
     of m^-1 in the cubic summand is -15405/8192, the value P10 states.

SCOPE.  The same-level cubic on the representative P10 uses, at odd levels (the even levels vanish by
r7044's singlet count, used here and not re-derived).  Nothing about the renormalised value or the
invariant the coefficient belongs to, PO-89's parts (a) and (b), which stay as they are.
"""
import contextlib, io, itertools, os, sys, time
import sympy as sp
from sympy.physics.quantum.cg import CG

t_all = time.time()
CHECKS = []
def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)
def head(t):
    print("\n  " + "=" * 74 + f"\n  {t}\n  " + "=" * 74, flush=True)
print(__doc__)

m = sp.Symbol('m')
QI = sp.QQ_I
def P(e):
    return sp.Poly(sp.nsimplify(e) if not isinstance(e, sp.Poly) else e, m, domain=QI) \
        if not isinstance(e, sp.Poly) else e
ZERO = sp.Poly(0, m, domain=QI)
ONE = sp.Poly(1, m, domain=QI)
I = sp.Poly(sp.I, m, domain=QI)
R3 = range(3)
EPS = lambda i, j, k: int(sp.LeviCivita(i, j, k))

def ff(X, n):
    """X!/(X-n)! for integer n >= 0, X a Poly"""
    out = ONE
    for i in range(n):
        out = out * (X - i)
    return out

# ---------------------------------------------------------------- frame (rational tensors)
UT = {2: [[-sp.Rational(1, 2), -sp.I/2, 0], [-sp.I/2, sp.Rational(1, 2), 0], [0, 0, 0]],
      1: [[0, 0, 1], [0, 0, sp.I], [1, sp.I, 0]],
      0: [[1, 0, 0], [0, 1, 0], [0, 0, -2]],
      -1: [[0, 0, -1], [0, 0, sp.I], [-1, sp.I, 0]],
      -2: [[-sp.Rational(1, 2), sp.I/2, 0], [sp.I/2, sp.Rational(1, 2), 0], [0, 0, 0]]}
UT = {q: [[P(x) for x in row] for row in M] for q, M in UT.items()}

def tz():
    return [[ZERO]*3 for _ in R3]
def tadd(A, B):
    return [[A[i][k] + B[i][k] for k in R3] for i in R3]
def tscale(A, s):
    return [[A[i][k]*s for k in R3] for i in R3]
def Eop(a, T):
    return [[-sum((T[d][c]*EPS(a, b, d) for d in R3), ZERO) - sum((T[b][d]*EPS(a, c, d) for d in R3), ZERO)
             for c in R3] for b in R3]

def sadd(S1, S2):
    out = dict(S1)
    for k, v in S2.items():
        out[k] = tadd(out[k], v) if k in out else v
    return out
def sscale(S, s):
    return {k: tscale(v, s) for k, v in S.items()}

class Field:
    """role: 'top', 'bot' or 'mid'; j, jp, nu as sympy expressions in m (j, jp linear, nu linear)"""
    def __init__(self, role, j, jp, nu):
        self.role, self.j, self.jp, self.nu = role, sp.expand(j), sp.expand(jp), sp.expand(nu)
        self.J = P(self.j)
        # integer offsets
        if role == 'top':
            self.c0 = sp.simplify(self.j - self.nu)       # j - mu = c0 - delta
            assert self.c0.is_integer
        elif role == 'bot':
            self.c0 = sp.simplify(self.j + self.nu)       # j + mu = c0 + delta
            assert self.c0.is_integer
        self.state, self.gsq = self.build()

    def mu(self, d):
        return P(self.nu + d)

    def build(self):
        j, jp, nu, f = self.j, self.jp, self.nu, sp.factorial
        up = sp.simplify(jp - j) == 2
        st = {}
        # global factor squared, and the per-component polynomial y
        if up:
            gsq = f(2*j)*f(jp + nu)*f(jp - nu)/f(2*j + 4)
        else:
            gsq = f(2*j - 3)/(f(2*j + 1)*f(jp + nu)*f(jp - nu))
        for q in range(-2, 3):
            d = -q                      # mu = nu - q
            sgn = 1 if (up or q % 2 == 0) else -1
            if self.role == 'top':
                jm = int(self.c0 - d)   # j - mu
                if jm < 0:
                    continue
                if up:
                    y = sp.Rational(1, sp.factorial(jm))
                    yP = P(y)
                else:                   # (j+mu)! / (2j-6)!  with j+mu = 2j - jm
                    yP = ff(P(2*j - jm), 6 - jm)
            elif self.role == 'bot':
                jpl = int(self.c0 + d)  # j + mu
                if jpl < 0:
                    continue
                if up:
                    yP = P(sp.Rational(1, sp.factorial(jpl)))
                else:                   # (j-mu)!/(2j-6)!
                    yP = ff(P(2*j - jpl), 6 - jpl)
            else:
                if up:
                    yP = ONE
                else:                   # (j+mu)!(j-mu)! / ((j-6)!)^2,  |mu| <= 6
                    mu_ = nu - q
                    a1 = sp.simplify(j + mu_ - (j - 6)); a2 = sp.simplify(j - mu_ - (j - 6))
                    assert a1.is_integer and a2.is_integer and a1 >= 0 and a2 >= 0
                    yP = ff(P(j + mu_), int(a1)) * ff(P(j - mu_), int(a2))
            st[d] = tscale(UT[q], yP*sgn)
        if not up:
            if self.role in ('top', 'bot'):
                gsq = gsq*f(2*j - 6)**2
            else:
                gsq = gsq*f(j - 6)**4
        else:
            if self.role == 'top':
                pass
            elif self.role == 'bot':
                pass
        return st, gsq

    # scaled J on the magnetic index
    def Jpm(self, S, sign):
        out = {}
        for d, T in S.items():
            nd = d + sign
            mu = self.mu(d)
            if self.role == 'top':
                jm = int(self.c0 - d)
                if sign > 0:
                    coef = P(jm) * (self.J + mu + 1) if jm > 0 else ZERO
                else:
                    coef = ONE
            elif self.role == 'bot':
                jpl = int(self.c0 + d)
                if sign > 0:
                    coef = ONE
                else:
                    coef = P(jpl) * (self.J - mu + 1) if jpl > 0 else ZERO
            else:
                coef = (self.J + mu + 1) if sign > 0 else (self.J - mu + 1)
            if coef.is_zero:
                continue
            v = tscale(T, coef)
            out[nd] = tadd(out[nd], v) if nd in out else v
        return out

    def Jz(self, S):
        return {d: tscale(T, self.mu(d)) for d, T in S.items()}

    def N(self, a, S):
        """covariant derivative N_a = -2i J_a (x) 1 + 1 (x) E_a"""
        if a == 0:
            Ja = sscale(sadd(self.Jpm(S, +1), self.Jpm(S, -1)), P(sp.Rational(1, 2)))
        elif a == 1:
            Ja = sscale(sadd(self.Jpm(S, +1), sscale(self.Jpm(S, -1), P(-1))), P(-sp.I/2))
        else:
            Ja = self.Jz(S)
        out = sscale(Ja, P(-2*sp.I))
        return sadd(out, {d: Eop(a, T) for d, T in S.items()})

    def arrays(self):
        p0 = self.state
        p1 = [self.N(c, p0) for c in R3]
        p2 = [[None]*3 for _ in R3]
        for c in R3:
            for d in R3:
                v = self.N(c, p1[d])
                for x in R3:
                    if EPS(c, d, x):
                        v = sadd(v, sscale(p1[x], P(-EPS(c, d, x))))
                p2[c][d] = v
        return p0, p1, p2

def term(nm, P_, Q_, R_, dp, dq, dr):
    (p0, p1, p2), (q0, q1, q2), (r0, r1, r2) = P_, Q_, R_
    s = ZERO
    g0 = lambda arr, d: arr.get(d)
    if nm == "S0":
        A, B, C = g0(p0, dp), g0(q0, dq), g0(r0, dr)
        if A is None or B is None or C is None: return ZERO
        for a in R3:
            for b in R3:
                for c in R3:
                    s += A[a][b]*B[b][c]*C[c][a]
        return s
    A = g0(p0, dp)
    if A is None: return ZERO
    for a in R3:
        for b in R3:
            if A[a][b].is_zero: continue
            for c in R3:
                for d in R3:
                    if nm == "S1":
                        X, Y = q1[a].get(dq), r1[b].get(dr)
                        if X is None or Y is None: continue
                        s += A[a][b]*X[c][d]*Y[c][d]
                    elif nm == "S2":
                        X, Y = q1[c].get(dq), r1[c].get(dr)
                        if X is None or Y is None: continue
                        s += A[a][b]*X[a][d]*Y[b][d]
                    elif nm == "S3":
                        X, Y = q1[c].get(dq), r1[d].get(dr)
                        if X is None or Y is None: continue
                        s += A[a][b]*X[a][d]*Y[b][c]
                    elif nm == "W1":
                        X, Y = q0.get(dq), r2[a][c].get(dr)
                        if X is None or Y is None: continue
                        s += A[a][b]*X[c][d]*Y[b][d]
                    elif nm == "W2":
                        X, Y = q0.get(dq), r2[d][d].get(dr)
                        if X is None or Y is None: continue
                        s += A[a][b]*X[b][c]*Y[c][a]
                    elif nm == "W3":
                        X, Y = q0.get(dq), r2[c][d].get(dr)
                        if X is None or Y is None: continue
                        s += A[a][b]*X[c][d]*Y[a][b]
                    elif nm == "U9":
                        X, Y = q1[c].get(dq), r1[d].get(dr)
                        if X is None or Y is None: continue
                        s += A[a][b]*X[d][a]*Y[c][b]
    return s

REP0 = {"S0": sp.Rational(1, 6), "S1": sp.Rational(1, 6), "S2": sp.Rational(-1, 6),
        "S3": sp.Rational(1, 4), "W1": sp.Rational(1, 6)}

a_, b_ = (m + 1)/2, (m - 3)/2

def gamma_rational(e):
    """reduce a product of factorials/gammas whose arguments pair off by integer shifts to a rational function"""
    e = sp.gammasimp(sp.combsimp(e)).rewrite(sp.gamma)
    num, den = sp.fraction(sp.powsimp(sp.together(e)))
    def gam(x):
        out = []
        for fct, p in sp.Mul.make_args(x) and [f.as_base_exp() for f in sp.Mul.make_args(x)]:
            out.append((fct, p))
        return out
    G = {}
    rest = sp.Integer(1)
    for side, sgn in ((num, 1), (den, -1)):
        for fct, p in gam(side):
            if isinstance(fct, sp.gamma):
                G[fct.args[0]] = G.get(fct.args[0], 0) + sgn*p
            else:
                rest *= fct**(sgn*p)
    args = list(G)
    while args:
        x = args.pop()
        if G[x] == 0: continue
        for y in args:
            d = sp.simplify(x - y)
            if d.is_integer and G[y] != 0:
                # gamma(x)^p gamma(y)^q, transfer: gamma(x) = gamma(y) * prod_{i<d}(y+i) for d>0
                p = G[x]
                if d > 0:
                    rest *= sp.prod([y + i for i in range(int(d))])**p
                else:
                    rest /= sp.prod([x + i for i in range(int(-d))])**p
                G[y] += p; G[x] = 0
                break
    left = {x: p for x, p in G.items() if p != 0}
    assert not left, ('unpaired gammas', left)
    return sp.factor(rest)

def channel_A(js, jps, coeffs=REP0, verbose=True):
    t0 = time.time()
    nu = (jps[0], -jps[1], jps[1] - jps[0])
    roles = ('top', 'bot', 'mid')
    F = [Field(r, j, jp, n) for r, j, jp, n in zip(roles, js, jps, nu)]
    AR = [f.arrays() for f in F]
    j1, j2, j3 = js
    L1, L2, L3 = P(j1 - j2 + j3), P(-j1 + j2 + j3), P(j1 + j2 - j3)
    ph0 = sp.simplify(j1 - j2 - nu[2]); assert ph0.is_integer
    c1 = sp.simplify(j1 - nu[0]); c2 = sp.simplify(j2 + nu[1])
    assert c1.is_integer and c2.is_integer
    coef = {k: P(v) for k, v in coeffs.items() if v}
    Rsum = ZERO
    rng = range(-4, 5)
    for d1 in rng:
        for d2 in rng:
            d3 = -d1 - d2
            if d3 not in rng: continue
            k1 = int(c1 - d1)     # j1 - mu1
            k2 = int(c2 + d2)     # j2 + mu2
            if k1 < 0 or k2 < 0: continue
            Tm = ZERO
            for t in range(0, min(k1, k2) + 1):
                cst = sp.Integer((-1)**t)*sp.factorial(k1)*sp.factorial(k2) / \
                    (sp.factorial(t)*sp.factorial(k1 - t)*sp.factorial(k2 - t))
                Tm += ff(L1, k1 - t)*ff(L2, k2 - t)*ff(L3, t)*P(cst)
            Tm = Tm*P(1 if int(ph0 - d3) % 2 == 0 else -1)
            if Tm.is_zero: continue
            dd = (d1, d2, d3)
            inner = ZERO
            for perm in itertools.permutations(range(3)):
                Pp, Qp, Rp = AR[perm[0]], AR[perm[1]], AR[perm[2]]
                for nm, c in coef.items():
                    inner += term(nm, Pp, Qp, Rp, dd[perm[0]], dd[perm[1]], dd[perm[2]])*c
            Rsum += Tm*inner
    # global factor:  A = prod(2j+1) * G_L^2 * prod g^2 / 3jR^2 * |R|^2
    f = sp.factorial
    Jt = j1 + j2 + j3
    GL2 = 1/(f(j1 - j2 + j3)*f(-j1 + j2 + j3)*f(j1 + j2 - j3)*f(Jt + 1))
    jp1, jp2, jp3 = jps
    Lp1, Lp2, Lp3 = jp1 - jp2 + jp3, -jp1 + jp2 + jp3, jp1 + jp2 - jp3
    R3j2 = f(2*jp1)*f(2*jp2)*f(jp3 + nu[2])*f(jp3 - nu[2])/(f(Lp1)*f(Lp2)*f(Lp3)*f(jp1 + jp2 + jp3 + 1))
    glob = (2*j1 + 1)*(2*j2 + 1)*(2*j3 + 1)*GL2*F[0].gsq*F[1].gsq*F[2].gsq/R3j2
    glob = gamma_rational(glob)
    Rexpr = Rsum.as_expr()
    Rc = sp.expand(sp.conjugate(Rexpr).subs(sp.conjugate(m), m))
    A = sp.factor(sp.expand(glob*sp.expand(Rexpr*Rc)))
    if verbose:
        print(f"  {''.join('a' if j == a_ else 'b' for j in js)}: deg R = {Rsum.degree()}, glob = {glob}"
              f"  [{time.time()-t0:.0f}s]", flush=True)
    return A, Rsum, glob

def chans():
    out = []
    for c in itertools.product([(a_, b_), (b_, a_)], repeat=3):
        out.append((tuple(x[0] for x in c), tuple(x[1] for x in c)))
    return out


# ============================================================ A. the ingredients, checked
head("A.  THE INGREDIENTS: THE FRAME'S SPIN-TWO BASIS AND THE STRETCHED CLEBSCH-GORDAN COEFFICIENTS")

def Emat(a, T):
    return sp.Matrix(3, 3, lambda b, c: -sum(EPS(a, b, d)*T[d, c] for d in R3) - sum(EPS(a, c, d)*T[b, d] for d in R3))
Sfr = lambda a, T: sp.I*Emat(a, T)
UTm = {q: sp.Matrix([[x.as_expr() for x in row] for row in M]) for q, M in UT.items()}
qconst = {q: sp.sqrt(sp.Rational(sp.factorial(2 + q)*sp.factorial(2 - q), 24)) for q in UT}
U = {q: UTm[q]*qconst[q] for q in UT}
okz = all(sp.simplify(Sfr(2, U[q]) - q*U[q]) == sp.zeros(3, 3) for q in U)
okl = all(sp.simplify(Sfr(0, U[q]) - sp.I*Sfr(1, U[q]) - sp.sqrt((2 + q)*(2 - q + 1))*U[q - 1]) == sp.zeros(3, 3)
          for q in (2, 1, 0, -1))
okn = sp.simplify(sum(U[2][i, k]*sp.conjugate(U[2][i, k]) for i in R3 for k in R3)) == 1
okt = all(U[q].trace() == 0 and U[q] == U[q].T for q in U)
okh = sp.simplify(Sfr(0, U[2]) + sp.I*Sfr(1, U[2])) == sp.zeros(3, 3)
gate("the five frame tensors are the STANDARD spin-two basis of the frame spin S_a = i E_a, where E_a is "
     "r7056's connection (SG/2): symmetric, traceless, S_z eigenvalues -2..2, the top annihilated by "
     "S_+, the top normalised, and each obtained from the one above by the standard lowering -- so "
     "Clebsch-Gordan coupling applies to them without a phase choice entering",
     okz and okl and okn and okt and okh)
f_ = sp.factorial
def K(j, jp, mu, q, nu):
    if jp == j + 2:
        return sp.sqrt(f_(2*j)*f_(jp + nu)*f_(jp - nu)/(f_(2*j + 4)*f_(j + mu)*f_(j - mu)))
    return (-1)**q*sp.sqrt(f_(2*j - 3)*f_(j + mu)*f_(j - mu)/(f_(2*j + 1)*f_(jp + nu)*f_(jp - nu)))
bad = 0; nck = 0
for j in (3, 4, sp.Rational(7, 2), 6):
    for jp in (j + 2, j - 2):
        for nu in [jp - k for k in range(int(2*jp) + 1)]:
            for q in range(-2, 3):
                mu = nu - q
                if abs(mu) > j:
                    continue
                nck += 1
                if sp.simplify(CG(j, mu, 2, q, jp, nu).doit()
                               - sp.sqrt(sp.Rational(24, f_(2 + q)*f_(2 - q)))*K(j, jp, mu, q, nu)) != 0:
                    bad += 1
gate(f"the stretched coefficients <j mu; 2 q | j+-2, nu> used in the rescaled bases agree with sympy's "
     f"Clebsch-Gordan coefficients at all {nck} components checked, integer and half-integer spins", bad == 0 and nck > 250)

# and the Field implementation, evaluated at one level, against those coefficients times the rescalings
def s_of(role, j, mu):
    if role == 'top': return sp.sqrt(f_(j + mu)/f_(j - mu))
    if role == 'bot': return sp.sqrt(f_(j - mu)/f_(j + mu))
    return sp.sqrt(f_(j + mu)*f_(j - mu))
mt = 21; okf = True; nf = 0
for role, j, jp, nu in (('top', a_, b_, b_), ('top', b_, a_, a_), ('bot', a_, b_, -b_), ('bot', b_, a_, -a_),
                        ('mid', a_, b_, 0), ('mid', b_, a_, 0), ('mid', a_, b_, 2), ('mid', b_, a_, -2)):
    Fd = Field(role, j, jp, nu)
    jv, jpv, nuv = (sp.sympify(x).subs(m, mt) for x in (j, jp, nu))
    for q in range(-2, 3):
        mu = nuv - q
        want = CG(jv, mu, 2, q, jpv, nuv).doit()*s_of(role, jv, mu) if abs(mu) <= jv else 0
        got = Fd.state.get(-q)
        gotM = sp.Matrix([[x.as_expr().subs(m, mt) for x in row] for row in got]) if got else sp.zeros(3, 3)
        okf &= sp.simplify(gotM*sp.sqrt(Fd.gsq.subs(m, mt)) - want*U[q]) == sp.zeros(3, 3)
        nf += 1
gate(f"and the rescaled coupled states the derivation builds -- global factor times polynomial, for the top, "
     f"bottom and middle placements and both couplings j' = j+2 and j' = j-2 -- equal Clebsch-Gordan "
     f"times the rescaling times the frame tensor, component by component ({nf} checked at m = {mt})", okf)

# ============================================================ B. the derivation
head("B.  THE EIGHT CHANNELS, DERIVED AS IDENTITIES IN m")

Aform = 9*(m**2 - 1)*(9*m**2 - 25)*(9*m**2 - 1)**3/(65536*m**3)
Bform = (m**2 - 25)*(m**2 - 9)*(m**2 - 1)**2*(9*m**2 - 1)/(65536*m**3)
DER, RPOL = {}, {}
name = lambda js: ''.join('a' if j == a_ else 'b' for j in js)
for js, jps in chans():
    A_, R_, g_ = channel_A(js, jps, verbose=False)
    DER[name(js)], RPOL[name(js)] = sp.factor(A_), R_
    print(f"      {name(js)}:  A(m) = {DER[name(js)]}", flush=True)
ext = [k for k in DER if k.count('a') in (0, 3)]
mix = [k for k in DER if k.count('a') in (1, 2)]
gate("THE TWO EXTREME CHANNELS GIVE A(m) EXACTLY, as an identity in m: the form P10 fitted is derived",
     len(ext) == 2 and all(sp.simplify(DER[k] - Aform) == 0 for k in ext))
gate("THE SIX MIXED CHANNELS GIVE B(m) EXACTLY, as an identity in m", len(mix) == 6
     and all(sp.simplify(DER[k] - Bform) == 0 for k in mix))
gate("and the ORBIT DEGENERACY is derived with them -- the extreme pair equal to each other and all six "
     "mixed channels equal -- at every level, where it had been observed at the computed ones",
     len({sp.simplify(DER[k] - DER[ext[0]]) for k in ext}) == 1
     and len({sp.simplify(DER[k] - DER[mix[0]]) for k in mix}) == 1)
gate("⌗ and the result is not reached by its own structure regardless of the vertex: dropping one "
     "structure (S3) from the vertex changes the extreme channel's A(m), so the identity is a fact "
     "about this vertex",
     sp.simplify(sp.factor(channel_A(chans()[0][0], chans()[0][1],
                                     {k: v for k, v in REP0.items() if k != 'S3'}, verbose=False)[0]) - Aform) != 0)

# ============================================================ C. the representative
head("C.  THE THREE REPRESENTATIVES GIVE THE SAME POLYNOMIAL, AT EVERY LEVEL")

REPS = {"tau1 = 1": {"S0": sp.Rational(1, 6) - 3, "S1": sp.Rational(1, 6), "S2": sp.Rational(-1, 6),
                     "S3": sp.Rational(1, 4), "W1": sp.Rational(1, 6) - 1, "W2": sp.Integer(1), "W3": sp.Integer(1)},
        "tau2 = 1": {"S0": sp.Rational(1, 6), "S1": sp.Rational(1, 6), "S2": sp.Rational(-1, 6),
                     "S3": sp.Rational(1, 4) - 1, "W1": sp.Rational(1, 6), "U9": sp.Integer(1)}}
okrep = True
for rn, rep in REPS.items():
    for js, jps in chans():
        R2 = channel_A(js, jps, rep, verbose=False)[1]
        okrep &= sp.expand(R2.as_expr() - RPOL[name(js)].as_expr()) == 0
gate("the amplitude polynomial R(m) itself -- not only its square -- is IDENTICAL for r7056's three "
     "representatives of the vertex, in every channel, so the guard r7056 checked at computed levels "
     "holds at every level", okrep)

# ============================================================ D. every odd level
head("D.  THE DERIVATION'S RANGE, AND THE LEVELS BELOW IT BY r7056's OWN MACHINERY")

m0 = 3
for js, jps in chans():
    nu = (jps[0], -jps[1], jps[1] - jps[0])
    j1, j2, j3 = js
    conds = [j3 - (abs(sp.simplify(nu[2])) + 5), j1 + nu[0] - 5, j2 - nu[1] - 5]
    conds += [L - 6 for L in (j1 - j2 + j3, -j1 + j2 + j3, j1 + j2 - j3)] + [2*j - 6 for j in js]
    mm = 3
    while not all(sp.simplify(c.subs(m, mm)) >= 0 for c in conds):
        mm += 2
    m0 = max(m0, mm)
    # and every condition is linear and increasing in m, so it stays true above
    assert all(sp.diff(c, m) > 0 for c in conds)
gate(f"the derivation's conditions -- the third field's window strictly inside its representation, the "
     f"first two away from the opposite edge, every reference factorial's argument non-negative and "
     f"Racah's sum in the range written -- hold for every odd m >= {m0}, each being linear and "
     f"increasing in m", m0 == 19)

HERE = os.path.dirname(os.path.abspath(__file__))
R7056 = ("P10_the_odd_residue_is_five_levels_and_the_sign_is_mixed_because_the_vertex_"
         "carries_covariant_not_frame_derivatives.py")
srcl = open(os.path.join(HERE, R7056), encoding="utf-8").read().split("\n")
cut = next(i for i, ln in enumerate(srcl) if ln.startswith('head("D.'))
NS = {"__name__": "r7056_machinery"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile("\n".join(srcl[:cut]), R7056, "exec"), NS)
from sympy.physics.wigner import wigner_3j
def direct(mm):
    a = sp.Rational(mm + 1, 2)
    ext_, mix_ = [], []
    for (js, jps) in NS['channels'](mm):
        flds = [(j, jp, NS['mult'](j, jp)) for (j, jp) in zip(js, jps)]
        nu = next(NS['nu_triples'](jps))
        c = sp.nsimplify(sp.simplify(NS['amp'](flds, nu, NS['REPS']['tau = 0'], True)
                                     / wigner_3j(jps[0], jps[1], jps[2], *nu)))
        v = sp.nsimplify(sp.prod([2*j + 1 for j in js])*sp.Abs(c)**2)
        (ext_ if sum(1 for j in js if j == a) in (0, 3) else mix_).append(v)
    return ext_, mix_
okd = True
for mm in range(3, m0 + 1, 2):
    t0 = time.time()
    e_, x_ = direct(mm)
    okd &= all(sp.simplify(v - Aform.subs(m, mm)) == 0 for v in e_)
    okd &= all(sp.simplify(v - Bform.subs(m, mm)) == 0 for v in x_)
    print(f"      m = {mm:2d}: {len(e_)} extreme, {len(x_)} mixed channels, each equal to the form  "
          f"[{time.time()-t0:.0f}s]", flush=True)
gate(f"below that, r7056's machinery loaded from its own source gives the exact value of every channel at "
     f"m = 3, 5, ..., {m0}, and each equals the derived form (at m = 3 and 5 the mixed channels are absent "
     f"and B's own factors vanish there) -- so the forms hold at EVERY odd level", okd)

# ============================================================ E. what rested on them
head("E.  WHAT RESTED ON THE FORMS NOW RESTS ON THE DERIVATION")

Gm = sp.together(2*Aform + 6*Bform)
gate("G = 2A + 6B is odd in m -- the parity, which the channel list's mirror symmetry proves on its own, "
     "read off the derived forms", sp.simplify(Gm.subs(m, -m) + Gm) == 0)
u = sp.Symbol('u', positive=True)
N = sp.expand(Gm*m**3)
frac = sp.apart(sp.simplify(N.subs(m, sp.sqrt(u))/(u - 1)**2), u)
Qe = sp.expand(sum(t for t in sp.Add.make_args(frac) if not sp.denom(sp.together(t)).has(u)))
qm1 = sp.nsimplify(Qe.coeff(u, 1))
gate(f"and the coefficient of m^-1 in the cubic summand N(m^2)/(m^3 (m^2-1)^2) is {qm1}, P10's "
     f"-15405/8192: the pole and its residue now rest on derived forms", qm1 == sp.Rational(-15405, 8192))

print("\n  " + "=" * 74)
bad = [n for n, ok in CHECKS if not ok]
print(f"  {len(CHECKS)} checks, {len(CHECKS)-len(bad)} pass, {len(bad)} fail   [{time.time()-t_all:.0f}s]")
for n in bad:
    print(f"    FAILED: {n}")
print(f"  GATES: {'ALL PASS' if not bad else 'FAILURES ABOVE'}")
assert not bad, f"{len(bad)} check(s) failed: {bad}"

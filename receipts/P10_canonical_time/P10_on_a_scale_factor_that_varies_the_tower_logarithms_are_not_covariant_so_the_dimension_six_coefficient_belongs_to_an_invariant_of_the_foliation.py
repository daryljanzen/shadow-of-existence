#!/usr/bin/env python3
r"""PO-89 part (b): on a scale factor that varies, the transverse-traceless tower's logarithms are not
reductions of spacetime-covariant invariants -- already at dimension four, for the free tower -- so the
dimension-six coefficient P10 computes belongs to an invariant of the foliation, not of the four-geometry.

LEVEL: exact symbolic algebra for every derived statement; one numerical check (the local expansion against
the propagator integrated by an ODE solver), reported with its scaling and tolerance.

OBJECT UNDER TEST.  P10 sec:lock computes the same-level cubic's logarithmic coefficient at dimension six,
-15405/8192, on the scale factor at one instant, and says the invariant it is the coefficient of cannot be
named there: on the one-parameter family the five dimension-six scalars have rank one.  The construction
quantizes the scale factor, and on a scale factor that varies those scalars are independent (r7062).  So the
datum the naming needs is on the admitted class: the tower's divergence on a time-varying scale factor.

THE ROUTE.  Euclidean, closed Friedmann geometry d tau^2 + a(tau)^2 dOmega_3.  Each level is P10's oscillator
with mass a^3 and frequency mu/a, mu^2 = m^2 - 1, and the potential cubic carries one power of a (the
Einstein-Hilbert cubic's spatial-gradient term, a^3 times a^-2).  At second order in the cubic the effective
action is  Gamma_2 = -3 S_m  Int Int a(t) a(t') G(t,t')^3,  S_m the level's degeneracy-summed squared vertex
(2A + 6B, the derived closed forms), G the propagator.  G is written exactly in WKB form,
    G(t,t') = [M(t) M(t') W(t) W(t')]^(-1/2) / 2 * exp(-|Int_t^t' W|),
with W the exact solution of the Euclidean Riccati-WKB equation, expanded in derivatives of a; the double
integral is expanded about the midpoint.  Each order of 2k derivatives comes with mu^(-4-2k), so the level
sum's logarithm at that order is the 1/m coefficient of S_m (m^2-1)^(-2-k).  The same machinery, run on the
free tower (Gamma_1 = (1/2) sum_m d(m) Int W), gives the dimension-four logarithm.

WHAT IS CLAIMED.
  1. The local expansion is right: against the propagator integrated numerically on a(tau) = 1.3 + 0.2 sin(0.7 tau),
     the residual after orders 0, 2 and 4 falls as mu^-2, mu^-4 and mu^-6.
  2. The machinery reproduces covariance where covariance is owed.  A minimally coupled scalar's tower
     (degeneracy m^2, the same frequencies) returns, on every scale factor, exactly -1/576 a^3 R^2: the known
     (1/16 pi^2)(1/72) R^2 of its a_2 coefficient times the volume 2 pi^2, normalisation included.
  3. The free transverse-traceless tower does not.  Its degeneracy is 2(m^2-4), two scalar towers less eight
     modes per level.  The two scalar towers give 2 x (-1/576) a^3 R^2; the eight-per-level deficit gives
     2(1 - a'^2)/a up to a total derivative, which is no multiple of a^3 R^2 -- the only covariant
     dimension-four functional on this class -- and is the foliation invariant a^3 [ (3R)^2/18 - (3R) K^2/27 ]
     (3R the slice's curvature, K the trace of its extrinsic curvature).  The static logarithm 15/4 is
     -1/4 from the two scalar towers and 4 from the deficit.
  4. At dimension six the same holds.  The level logarithms are q_0 = -15405/8192 (P10's), q_1 = -8313/4096,
     q_2 = 14769/8192 and q_3 = 0; the six covariant dimension-six scalars (R^3, R Ric^2, Ric^3, (grad R)^2,
     R Box R, (grad Ric)^2) span four directions on this class modulo total derivatives, and the tower's
     functional is not in that span: the matching system has coefficient rank 4 and augmented rank 5.
  5. So the coefficient is not the coefficient of a spacetime invariant on the admitted class.  Its carrier is
     an invariant of the foliation, which the construction's absolute cosmic time makes admissible, and on the
     isotropic class the foliation's invariants are themselves degenerate (K_ij is proportional to the slice
     metric there), so naming the carrier among them needs the tower's own shear.

SCOPE.  The same-level cubic, as P10 computes it, and the transverse-traceless tower the deparametrization
leaves after the constraints are solved; nothing about the cross-level couplings, and no claim about a
covariant theory carrying the removed sectors, whose divergences would combine with these.
"""
import os, time, pickle
import sympy as sp

t_all = time.time()
CHECKS = []
def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)
def head(t):
    print("\n  " + "=" * 74 + f"\n  {t}\n  " + "=" * 74, flush=True)
print(__doc__)

NJ = 12
A = sp.symbols('A0:%d' % NJ, positive=True)          # jets of a at the midpoint
mu, Dl = sp.symbols('mu Delta', positive=True)
O = 4


def Dx(e):
    return sum(sp.diff(e, A[k]) * A[k + 1] for k in range(NJ - 1))
def S(*c):
    return [sp.expand(x) for x in c] + [0] * (O + 1 - len(c))
def add(p, q):
    return [sp.expand(p[i] + q[i]) for i in range(O + 1)]
def scal(p, c):
    return [sp.expand(c * x) for x in p]
def mul(p, q):
    r = [0] * (O + 1)
    for i in range(O + 1):
        if p[i] == 0:
            continue
        for j in range(O + 1 - i):
            if q[j] != 0:
                r[i + j] += p[i] * q[j]
    return [sp.expand(x) if x != 0 else 0 for x in r]
def D(p):
    return [0] + [sp.expand(Dx(p[i])) for i in range(O)]
def powser(p, alpha):
    p0 = p[0]
    y = [0] + [sp.expand(sp.powsimp(sp.expand(x / p0), force=True)) for x in p[1:]]
    res, term = S(1), S(1)
    for n in range(1, O + 1):
        term = mul(term, y)
        res = add(res, scal(term, sp.binomial(alpha, n)))
    return [sp.expand(sp.powsimp(sp.expand(x * p0 ** alpha), force=True)) for x in res]


def wkb_W(extra):
    """W^2 = Omega^2 + W''/2W - 3/4 (W'/W)^2,  Omega^2 = mu^2/a^2 + (sqrt M)''/sqrt M + extra, M = a^3"""
    a = A[0]
    Om2 = S(mu ** 2 / a ** 2, 0, sp.Rational(3, 2) * A[2] / a + sp.Rational(3, 4) * A[1] ** 2 / a ** 2 + extra)
    W = S(mu / a)
    for _ in range(3):
        Wp = D(W); Wpp = D(Wp); Wi = powser(W, -1)
        rhs = add(Om2, add(scal(mul(Wpp, Wi), sp.Rational(1, 2)),
                           scal(mul(mul(Wp, Wi), mul(Wp, Wi)), -sp.Rational(3, 4))))
        W = powser(rhs, sp.Rational(1, 2))
    return W


W = wkb_W(0)
a = A[0]

# ---------------------------------------------------------------- the cubic's local expansion
P = [sp.expand(sp.powsimp(x * a ** sp.Rational(-7, 2), force=True)) for x in powser(W, -sp.Rational(3, 2))]
Dn = [P]
for n in range(O):
    Dn.append(D(Dn[-1]))
def shifted(sign):
    r = S(0)
    for n in range(O + 1):
        r = add(r, scal(Dn[n], (sign * Dl / 2) ** n / sp.factorial(n)))
    return r
PP = mul(shifted(1), shifted(-1))
Wd = [W]
for n in range(O):
    Wd.append(D(Wd[-1]))
corr = S(0)
for n in range(2, O + 1, 2):
    corr = add(corr, scal(Wd[n], 2 * (Dl / 2) ** (n + 1) / sp.factorial(n + 1)))
ex, term = S(1), S(1)
for k in range(1, 3):
    term = mul(term, scal(corr, -3))
    ex = add(ex, scal(term, sp.Rational(1, sp.factorial(k))))
integ = scal(mul(PP, ex), sp.Rational(1, 8))
res = S(0)
cache = {}
for order in range(O + 1):
    e = sp.expand(integ[order])
    if e == 0:
        continue
    for (n,), c in sp.Poly(e, Dl).terms():
        if n not in cache:
            cache[n] = powser(scal(W, 3), -(n + 1))
        part = scal(cache[n], 2 * sp.factorial(n) * c)
        res = add(res, [0] * order + part[:O + 1 - order])
Pk = {k: sp.expand(sp.powsimp(sp.expand(res[2 * k] * mu ** (4 + 2 * k)), force=True)) for k in range(3)}

# ============================================================ A. the expansion is right
head("A.  THE LOCAL EXPANSION, AGAINST THE PROPAGATOR INTEGRATED NUMERICALLY")

gate("every order is mu^(-4-2k) times a function of the scale factor's derivatives alone, and the odd orders "
     "vanish: P_0 = 1/(12 a^3), the static second-order energy of a cubic on modes of one frequency",
     all(not v.has(mu) for v in Pk.values()) and sp.expand(res[1]) == 0 and sp.expand(res[3]) == 0
     and sp.simplify(Pk[0] - 1/(12 * a ** 3)) == 0)
print(f"      P_1 = {sp.factor(Pk[1])}\n      P_2 = {sp.factor(Pk[2])}", flush=True)

import numpy as np
from scipy.integrate import solve_ivp, quad
from scipy.interpolate import CubicSpline
tt = sp.Symbol('t')
aex = sp.Rational(13, 10) + sp.Rational(1, 5) * sp.sin(sp.Rational(7, 10) * tt)
jets = {A[k]: sp.diff(aex, tt, k) for k in range(NJ)}
af = sp.lambdify(tt, aex); daf = sp.lambdify(tt, sp.diff(aex, tt))
t0 = 0.4
def F_exact(m_):
    om = lambda t: m_ / af(t)
    rhs = lambda t, r: [om(t) ** 2 - r[0] ** 2 - 3 * daf(t) / af(t) * r[0]]
    L = 120 / m_ * af(t0) + 3
    grid = np.linspace(t0 - L, t0 + L, 40001)
    sp_ = solve_ivp(rhs, [t0 + L + 8, t0 - L], [-om(t0 + L + 8)], t_eval=grid[::-1], rtol=1e-12, atol=1e-14,
                    method='DOP853')
    sm = solve_ivp(rhs, [t0 - L - 8, t0 + L], [om(t0 - L - 8)], t_eval=grid, rtol=1e-12, atol=1e-14,
                   method='DOP853')
    Rp = CubicSpline(grid, sp_.y[0][::-1]); Rm = CubicSpline(grid, sm.y[0]); Ip = Rp.antiderivative()
    G = lambda t1, t2: np.exp(Ip(t2) - Ip(t1)) / (af(t1) ** 3 * (Rm(t1) - Rp(t1)))
    f = lambda d: af(t0 - d / 2) * af(t0 + d / 2) * G(t0 - d / 2, t0 + d / 2) ** 3
    return 2 * quad(f, 0, 2 * L - 1e-9, limit=400, epsabs=0, epsrel=1e-13)[0]
Pnum = [float(Pk[k].subs(jets).subs(tt, t0)) for k in range(3)]
resid = {}
for m_ in (6.0, 9.0, 13.0, 19.0):
    ex_ = F_exact(m_)
    resid[m_] = [abs(ex_ - sum(Pnum[k] * m_ ** (-4 - 2 * k) for k in range(K + 1))) / ex_ for K in range(3)]
    print(f"      mu = {m_:4.0f}:  relative residual after orders 0, 2, 4: "
          + "  ".join(f"{r:.2e}" for r in resid[m_]), flush=True)
slopes = [np.log(resid[6.0][K] / resid[19.0][K]) / np.log(19 / 6) for K in range(3)]
print(f"      measured slopes: {[round(s, 2) for s in slopes]}  (expected 2, 4, 6)", flush=True)
gate("the residual after orders 0, 2 and 4 falls as mu^-2, mu^-4 and mu^-6 (slopes within 0.15), so the "
     "expansion is the propagator's own and each order is complete", all(abs(slopes[K] - 2 * (K + 1)) < 0.15
                                                                          for K in range(3)))

# ---------------------------------------------------------------- Euler operator and the covariant scalars
B = sp.symbols('A0:%d' % NJ)
def plain(e):
    return e.subs({s: sp.Symbol(s.name) for s in e.free_symbols if s.name.startswith('A')})
def Dt(e):
    return sp.expand(sum(sp.diff(e, B[k]) * B[k + 1] for k in range(NJ - 1)))
def EL(L):
    out = 0
    for k in range(NJ - 2):
        d = sp.diff(L, B[k])
        for _ in range(k):
            d = Dt(d)
        out += (-1) ** k * d
    return sp.expand(out)
def fit(Lt, Lcs):
    c = sp.symbols('c0:%d' % len(Lcs))
    num = sp.Poly(sp.numer(sp.together(sp.expand(EL(Lt) - sum(ci * EL(Li) for ci, Li in zip(c, Lcs))))), *B)
    M = sp.Matrix([[sp.diff(e, ci) for ci in c] for e in num.coeffs()])
    Mb = M.row_join(sp.Matrix([e.subs({ci: 0 for ci in c}) for e in num.coeffs()]))
    return sp.solve(num.coeffs(), c, dict=True), M.rank(), Mb.rank()

t = sp.Symbol('t'); af_ = sp.Function('a')(t)
chi, th, ph = sp.symbols('chi theta phi')
X = [t, chi, th, ph]
g = sp.diag(1, af_ ** 2, af_ ** 2 * sp.sin(chi) ** 2, af_ ** 2 * sp.sin(chi) ** 2 * sp.sin(th) ** 2)
gi = g.inv(); N = 4
Gam = [[[sp.simplify(sum(gi[c, d] * (sp.diff(g[d, i], X[j]) + sp.diff(g[d, j], X[i]) - sp.diff(g[i, j], X[d]))
                         for d in range(N)) / 2) for j in range(N)] for i in range(N)] for c in range(N)]
def Rud(r, s_, m_, n):
    e = sp.diff(Gam[r][n][s_], X[m_]) - sp.diff(Gam[r][m_][s_], X[n])
    for l in range(N):
        e += Gam[r][m_][l] * Gam[l][n][s_] - Gam[r][n][l] * Gam[l][m_][s_]
    return sp.simplify(e)
Ric = sp.Matrix(N, N, lambda i, j: sp.simplify(sum(Rud(r, i, r, j) for r in range(N))))
Rm = sp.simplify(gi * Ric); Rs = sp.simplify(Rm.trace())
Ric2 = sp.simplify(sum(Rm[i, j] * Rm[j, i] for i in range(N) for j in range(N)))
Ric3 = sp.simplify(sum(Rm[i, j] * Rm[j, k] * Rm[k, i] for i in range(N) for j in range(N) for k in range(N)))
dR = sp.diff(Rs, t)
def covRic(a_, b, c):
    return (sp.diff(Ric[b, c], X[a_]) - sum(Gam[d][a_][b] * Ric[d, c] for d in range(N))
            - sum(Gam[d][a_][c] * Ric[b, d] for d in range(N)))
gRic2 = sp.simplify(sum(gi[i, i] * gi[j, j] * gi[k, k] * sp.simplify(covRic(i, j, k)) ** 2
                        for i in range(N) for j in range(N) for k in range(N)))
rep = {sp.diff(af_, t, k): B[k] for k in reversed(range(1, NJ))}
red = lambda o: sp.expand(sp.simplify(af_ ** 3 * o).subs(rep).subs(af_, B[0]))
six = [red(Rs ** 3), red(Rs * Ric2), red(Ric3), red(dR ** 2), red(Rs * sp.diff(af_ ** 3 * dR, t) / af_ ** 3),
       red(gRic2)]
R2 = red(Rs ** 2)
m = sp.Symbol('m')
def lc(f):
    x = sp.Symbol('x', positive=True)
    return sp.expand(sp.series(sp.simplify(f.subs(m, 1 / x)), x, 0, 6).removeO()).coeff(x, 1)

# ============================================================ B. dimension four, the free tower
head("B.  DIMENSION FOUR: THE CONTROL PASSES, AND THE FREE TOWER DOES NOT")

Wk = {k: plain(sp.expand(sp.powsimp(sp.expand(W[2 * k] * mu ** (2 * k - 1)), force=True))) for k in range(3)}
def oneloop(deg):
    q = {k: lc(deg * (m ** 2 - 1) ** sp.Rational(1 - 2 * k, 2)) for k in range(3)}
    return sum(q[k] * Wk[k] for k in range(3)) / 2, q
Lsc, qsc = oneloop(m ** 2)
sol, r1, r2 = fit(Lsc, [R2])
gate(f"CONTROL: a minimally coupled scalar's tower (degeneracy m^2, the same frequencies) gives exactly "
     f"{sol[0] if sol else None} times a^3 R^2 on every scale factor -- the (1/16 pi^2)(1/72) R^2 of its a_2 "
     f"coefficient times the volume 2 pi^2, normalisation included",
     bool(sol) and sol[0][sp.Symbol('c0')] == -sp.Rational(1, 16) / sp.pi ** 2 * sp.Rational(1, 72) * 2 * sp.pi ** 2)
Ltt, qtt = oneloop(2 * (m ** 2 - 4))
sol, r1, r2 = fit(Ltt, [R2])
gate(f"THE FREE TRANSVERSE-TRACELESS TOWER (degeneracy 2(m^2-4)) is NOT a multiple of a^3 R^2, the only "
     f"covariant dimension-four functional on this class modulo total derivatives: rank {r1} against "
     f"augmented {r2}", not sol and r2 == r1 + 1)
Ldef = sp.expand(Ltt - 2 * Lsc)
b0, b1, b2 = B[0], B[1], B[2]
gate(f"and the difference is the eight modes per level by which 2(m^2-4) falls short of two scalar towers: "
     f"{sp.factor(Ldef)}, which is 2(1 - a'^2)/a up to the total derivative -2a''",
     sp.simplify(Ldef - (2 / b0 - 2 * b2 - 2 * b1 ** 2 / b0)) == 0
     and sp.simplify(sp.expand(2 * (m ** 2 + 0) - 2 * (m ** 2 - 4)) - 8) == 0)
R3s, Ks = 6 / b0 ** 2, 3 * b1 / b0
gate("that piece is the foliation invariant a^3 [ (3R)^2/18 - (3R) K^2/27 ] (3R = 6/a^2 the slice's curvature, "
     "K = 3a'/a the trace of its extrinsic curvature), and it fits no multiple of a^3 R^2",
     EL(sp.expand(b0 ** 3 * (R3s ** 2 / 18 - R3s * Ks ** 2 / 27))) == EL(Ldef) and not fit(Ldef, [R2])[0])
gate(f"and the static logarithm P10 states, 15/4, is {qsc[0]*2} from the two scalar towers and "
     f"{lc(-8 * (m ** 2 - 1) ** sp.Rational(1, 2))} from the deficit",
     qtt[0] == sp.Rational(15, 4) and 2 * qsc[0] == -sp.Rational(1, 4)
     and lc(-8 * (m ** 2 - 1) ** sp.Rational(1, 2)) == 4)

# ============================================================ C. dimension six, the cubic
head("C.  DIMENSION SIX: THE SAME-LEVEL CUBIC'S LOGARITHM IS NOT IN THE COVARIANT SPAN")

Aform = 9 * (m ** 2 - 1) * (9 * m ** 2 - 25) * (9 * m ** 2 - 1) ** 3 / (65536 * m ** 3)
Bform = (m ** 2 - 25) * (m ** 2 - 9) * (m ** 2 - 1) ** 2 * (9 * m ** 2 - 1) / (65536 * m ** 3)
Sm = 2 * Aform + 6 * Bform
q = {k: lc(Sm * (m ** 2 - 1) ** (-2 - k)) for k in range(4)}
print(f"      level logarithms q_k: {q}", flush=True)
P10TXT = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'corpus',
                           'canonical_time.tex'), encoding='utf-8').read()
gate(f"q_0 is the value P10 prints for the instant (read from canonical_time.tex: {'$-15405/8192$' in P10TXT}), "
     f"and q_3 = 0: the logarithm stops at four derivatives",
     q[0] == sp.Rational(-15405, 8192) and '$-15405/8192$' in P10TXT and q[3] == 0)
L6 = sum(q[k] * plain(Pk[k]) for k in range(3))
vecs = [sp.Poly(sp.numer(sp.together(EL(L))), *B).as_dict() for L in six]
mons = sorted(set().union(*vecs))
rank6 = sp.Matrix([[v.get(mo, 0) for mo in mons] for v in vecs]).rank()
gate(f"the six covariant scalars R^3, R Ric^2, Ric^3, (grad R)^2, R Box R and (grad Ric)^2 span {rank6} "
     f"directions on this class modulo total derivatives", rank6 == 4)
sol, r1, r2 = fit(L6, six)
gate(f"⛭ AND THE TOWER'S DIMENSION-SIX LOGARITHM IS NOT IN THAT SPAN: coefficient rank {r1}, augmented "
     f"{r2}, no solution -- so on the admitted class the coefficient belongs to no spacetime invariant",
     not sol and r1 == 4 and r2 == 5)
Lfake = sp.expand(sp.Rational(3, 7) * six[0] - 2 * six[2] + sp.Rational(5, 3) * six[3])
gate("⌗ and the test can pass: a functional built from the covariant scalars is recovered by it",
     bool(fit(Lfake, six)[0]))

# ============================================================ D. what it is
head("D.  WHAT THE COEFFICIENT BELONGS TO")
gate("so the carrier is an invariant of the foliation -- admissible because cosmic time is absolute here -- "
     "and the free tower's logarithm is already one at dimension four; the foliation's invariants are "
     "themselves degenerate on the isotropic class, K_ij being proportional to the slice metric, so naming "
     "the carrier among them needs the tower's own shear",
     not sol and not fit(Ltt, [R2])[0])

print("\n  " + "=" * 74)
bad = [n for n, ok in CHECKS if not ok]
print(f"  {len(CHECKS)} checks, {len(CHECKS)-len(bad)} pass, {len(bad)} fail   [{time.time()-t_all:.0f}s]")
for n in bad:
    print(f"    FAILED: {n}")
print(f"  GATES: {'ALL PASS' if not bad else 'FAILURES ABOVE'}")
assert not bad, f"{len(bad)} check(s) failed: {bad}"

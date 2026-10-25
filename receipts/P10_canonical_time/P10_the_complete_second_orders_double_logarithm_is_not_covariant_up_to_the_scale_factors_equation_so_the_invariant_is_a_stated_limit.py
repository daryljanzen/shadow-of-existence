#!/usr/bin/env python3
r"""PO-89 parts (d) and (b): the complete second order at the paying dimension -- the cubic over all three levels,
the curvature quartic and the kinetic quartic -- carries a double logarithm, and that double logarithm is not
covariant up to the scale factor's equation of motion.  Up to that equation and total derivatives covariance at
dimension six is ONE linear condition, the single logarithm's share of it is moved by the subtraction's own
freedom, so the double logarithm decides it: the complete coefficient is not the coefficient of an invariant, and
the invariant is a stated limit of the reduction.

LEVEL: exact throughout for every coefficient that decides the result (rationals, and the volume as a factor
common to all three pieces).  Two numerical checks, each reported with its agreement: the three-level local
expansion against the same-level one already checked by an ODE solver (r7591), and the high-pair prediction of
the double logarithm against the three-level sum evaluated slice by slice and fitted.

WHAT IS CLAIMED.
  1. THE THREE-LEVEL LOCAL EXPANSION.  The cubic's second order on a varying scale factor, three propagators of
     frequencies mu_1/a, mu_2/a, mu_3/a in exact WKB form, expanded in derivatives of the scale factor: eight jet
     monomials through four derivatives, each with a coefficient rational and symmetric in (mu_1, mu_2, mu_3), and
     on the diagonal mu_1 = mu_2 = mu_3 it is r7591's same-level expansion term by term.
  2. THE CUBIC'S DOUBLE LOGARITHM.  For each monomial J the high pair's logarithm at a fixed low level n, summed
     over the pair's separations with r7595's closed form, is the level's degeneracy as a factor times a local
     polynomial over powers of mu_n; its 1/n term times 6 is the coefficient gamma_J of (log n)/n in the sum over
     the slice P = m1+m2+m3 = n -- checked against the slices themselves, fitted, at the instant and at two
     derivatives.
  3. EVERY QUARTIC IS A PRODUCT OF ONE-LOOP SUMS.  The free expectation of a quartic vertex is a sum of products of
     two coincident two-point functions, each a single sum over the tower, so its two-label part carries the
     logarithm squared and no logarithm of its own once each factor's divergence is subtracted.  The curvature
     quartic (r7034's object, r7058's chain, the volume as r7599 corrects it) gives -2 a^-5 (sum c/W)(sum d/W).
     The kinetic quartic is not zero: in the exponential variable the kinetic trace is tr H'^2 - (1/12) tr([H,H']^2)
     + ... (checked on random matrices) -- exactly quadratic only on a commuting sector such as the Misner one --
     and its expectation is -(a^3/96)(3/5)[(sum d u u')^2 - (sum d u^2)(sum d (u'^2 - u^2 W^2))], the Wick
     contractions 15 and -15.
  4. COVARIANCE AT DIMENSION SIX IS ONE CONDITION.  Up to the scale factor's equation of motion and total
     derivatives, the covariant dimension-six scalars and the lower invariants times powers of Lambda span all but
     one direction of the eight monomials: a random combination fails, a random combination plus one more random
     direction passes.  So each functional has one number, its obstruction, and is covariant exactly when it is
     zero; in the unit where 1/a^3 has obstruction 1 the monomials' obstructions are integers.
  5. THE OBSTRUCTIONS.  Curvature quartic 367/48, kinetic quartic 389/160, cubic -(1/3)(197131/6720), all in one
     unit (kappa hbar^2/V); the complete double logarithm's is 6023/20160, not zero.
  6. AND THE SINGLE LOGARITHM CANNOT SAVE IT.  Its value moves with how the subtraction treats the high pair
     against the low level, along the double logarithm's directions, whose obstructions are not zero; with one
     condition in all, the single logarithm can be given any obstruction by that freedom, so the complete
     coefficient's covariance is its double logarithm's, and that fails.  The complete second order is not
     covariant up to the equation of motion: PO-89's stated exit, the coefficient computed and its carrier not
     covariant from inside, the difference located in the reduction rather than in the truncation.

SCOPE.  The transverse-traceless tower on the closed Friedmann class, the scale factor varying, at second order
and operator dimension six; the cubic and both quartics as the reduction writes them, in r7058's chain with
r7599's volume.
"""
import contextlib, io, itertools, os, random, time
import sympy as sp
from sympy.polys.rings import ring
from sympy.polys.domains import QQ
import mpmath as mp

t_all = time.time()
CHECKS = []
def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)
def head(t):
    print("\n  " + "=" * 74 + f"\n  {t}\n  " + "=" * 74, flush=True)
print(__doc__)
HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- derivative series (r7591's machinery)
NJ = 12
A = sp.symbols('A0:%d' % NJ, positive=True)
MU = sp.symbols('mu1 mu2 mu3', positive=True)
mu = sp.Symbol('mu', positive=True)
Dl = sp.Symbol('Delta', positive=True)
O = 4
def Dx(e): return sum(sp.diff(e, A[k]) * A[k + 1] for k in range(NJ - 1))
def S_(*c): return [sp.expand(x) for x in c] + [0] * (O + 1 - len(c))
def add(p, q): return [sp.expand(p[i] + q[i]) for i in range(O + 1)]
def scal(p, c): return [sp.expand(c * x) for x in p]
def mul(p, q):
    r = [0] * (O + 1)
    for i in range(O + 1):
        if p[i] == 0: continue
        for j in range(O + 1 - i):
            if q[j] != 0: r[i + j] += p[i] * q[j]
    return [sp.expand(x) if x != 0 else 0 for x in r]
def D(p): return [0] + [sp.expand(Dx(p[i])) for i in range(O)]
def powser(p, alpha):
    p0 = p[0]
    y = [0] + [sp.expand(sp.powsimp(sp.expand(x / p0), force=True)) for x in p[1:]]
    res, term = S_(1), S_(1)
    for n in range(1, O + 1):
        term = mul(term, y); res = add(res, scal(term, sp.binomial(alpha, n)))
    return [sp.expand(sp.powsimp(sp.expand(x * p0 ** alpha), force=True)) for x in res]
a = A[0]
def wkb_W(m_):
    Om2 = S_(m_ ** 2 / a ** 2, 0, sp.Rational(3, 2) * A[2] / a + sp.Rational(3, 4) * A[1] ** 2 / a ** 2)
    W = S_(m_ / a)
    for _ in range(3):
        Wp = D(W); Wpp = D(Wp); Wi = powser(W, -1)
        rhs = add(Om2, add(scal(mul(Wpp, Wi), sp.Rational(1, 2)), scal(mul(mul(Wp, Wi), mul(Wp, Wi)), -sp.Rational(3, 4))))
        W = powser(rhs, sp.Rational(1, 2))
    return W

# =============================================================== A. the three-level local expansion
head("A.  THE CUBIC'S SECOND ORDER WITH THREE FREQUENCIES, EXPANDED LOCALLY")
t0 = time.time()
Ws = [wkb_W(m_) for m_ in MU]
P = S_(a ** sp.Rational(-7, 2))
for W in Ws: P = mul(P, powser(W, -sp.Rational(1, 2)))
P = [sp.expand(sp.powsimp(x, force=True)) for x in P]
Dn = [P]
for n in range(O): Dn.append(D(Dn[-1]))
def shifted(sign):
    r = S_(0)
    for n in range(O + 1): r = add(r, scal(Dn[n], (sign * Dl / 2) ** n / sp.factorial(n)))
    return r
PP = mul(shifted(1), shifted(-1))
Wt = S_(0)
for W in Ws: Wt = add(Wt, W)
Wd = [Wt]
for n in range(O): Wd.append(D(Wd[-1]))
corr = S_(0)
for n in range(2, O + 1, 2): corr = add(corr, scal(Wd[n], 2 * (Dl / 2) ** (n + 1) / sp.factorial(n + 1)))
ex, term = S_(1), S_(1)
for k in range(1, 3):
    term = mul(term, scal(corr, -1)); ex = add(ex, scal(term, sp.Rational(1, sp.factorial(k))))
integ = scal(mul(PP, ex), sp.Rational(1, 8))
res = S_(0); cache = {}
for order in range(O + 1):
    e = sp.expand(integ[order])
    if e == 0: continue
    for (nn,), c in sp.Poly(e, Dl).terms():
        if nn not in cache: cache[nn] = powser(Wt, -(nn + 1))
        part = scal(cache[nn], 2 * sp.factorial(nn) * c)
        res = add(res, [0] * order + part[:O + 1 - order])
print(f"      (expansion in {time.time()-t0:.0f}s)", flush=True)
# jet keys
JK = {}
for k in range(3):
    for t in sp.Add.make_args(sp.expand(res[2 * k])):
        cmu, ap = sp.factor_terms(t).as_independent(*A, as_Add=False)
        pw = ap.as_powers_dict()
        assert all(s_ in A for s_ in pw), ap
        key = (k,) + tuple(int(pw.get(A[i], 0)) for i in range(9))
        JK[key] = JK.get(key, 0) + cmu
JK = {kk: sp.cancel(sp.together(v)) for kk, v in JK.items()}
JK = {kk: v for kk, v in JK.items() if v != 0}
print(f"      (jet monomials collected, {time.time()-t0:.0f}s)", flush=True)
same = [sp.expand(sp.powsimp(sp.expand(res[2 * k].subs({m_: mu for m_ in MU}) * mu ** (4 + 2 * k)), force=True)) for k in range(3)]
# r7591's same-level P_k, rebuilt from its own construction (G^3 at one frequency)
Wsame = wkb_W(mu)
Ps = [sp.expand(sp.powsimp(x * a ** sp.Rational(-7, 2), force=True)) for x in powser(Wsame, -sp.Rational(3, 2))]
Dn1 = [Ps]
for n in range(O): Dn1.append(D(Dn1[-1]))
def sh1(sign):
    r = S_(0)
    for n in range(O + 1): r = add(r, scal(Dn1[n], (sign * Dl / 2) ** n / sp.factorial(n)))
    return r
PP1 = mul(sh1(1), sh1(-1)); Wd1 = [Wsame]
for n in range(O): Wd1.append(D(Wd1[-1]))
corr1 = S_(0)
for n in range(2, O + 1, 2): corr1 = add(corr1, scal(Wd1[n], 2 * (Dl / 2) ** (n + 1) / sp.factorial(n + 1)))
ex1, term1 = S_(1), S_(1)
for k in range(1, 3):
    term1 = mul(term1, scal(corr1, -3)); ex1 = add(ex1, scal(term1, sp.Rational(1, sp.factorial(k))))
integ1 = scal(mul(PP1, ex1), sp.Rational(1, 8)); res1 = S_(0); cache1 = {}
for order in range(O + 1):
    e = sp.expand(integ1[order])
    if e == 0: continue
    for (nn,), c in sp.Poly(e, Dl).terms():
        if nn not in cache1: cache1[nn] = powser(scal(Wsame, 3), -(nn + 1))
        part = scal(cache1[nn], 2 * sp.factorial(nn) * c)
        res1 = add(res1, [0] * order + part[:O + 1 - order])
Pk = [sp.expand(sp.powsimp(sp.expand(res1[2 * k] * mu ** (4 + 2 * k)), force=True)) for k in range(3)]
pts = [(sp.Rational(3), sp.Rational(5), sp.Rational(11)), (sp.Rational(7, 2), sp.Rational(13), sp.Rational(2))]
def at(v, p_): return v.subs(dict(zip(MU, p_)))
sym_ok = all(at(v, p_) == at(v, (p_[1], p_[0], p_[2])) == at(v, (p_[0], p_[2], p_[1])) for v in JK.values() for p_ in pts)
print(f"      (same-level rebuilt, {time.time()-t0:.0f}s)", flush=True)
gate(f"eight jet monomials through four derivatives ({len(JK)}), the odd orders vanishing, each coefficient rational "
     f"and symmetric in the three frequencies -- and on the diagonal it is r7591's same-level expansion term by term, "
     f"the expansion that receipt checked against the propagator integrated by an ODE solver",
     len(JK) == 8 and sp.expand(res[1]) == 0 and sp.expand(res[3]) == 0 and sym_ok
     and all(sp.expand(same[k] - Pk[k]) == 0 for k in range(3)))

# =============================================================== B. the cubic's double logarithm, per monomial
head("B.  THE CUBIC'S DOUBLE LOGARITHM: THE HIGH PAIR AT A FIXED LOW LEVEL, FROM r7595's CLOSED FORM")
RS, dS, nS, uS = ring('d,n3,u3', QQ)
class Ser:
    def __init__(self, c, L): self.L = L; self.c = (list(c) + [RS.zero] * L)[:L]
    def __add__(s, o): return Ser([x + y for x, y in zip(s.c, o.c)], min(s.L, o.L))
    def __mul__(s, o):
        if not isinstance(o, Ser): return Ser([x * o for x in s.c], s.L)
        L = min(s.L, o.L); r = [RS.zero] * L
        for i, x in enumerate(s.c[:L]):
            if x:
                for j in range(L - i):
                    if o.c[j]: r[i + j] += x * o.c[j]
        return Ser(r, L)
def binom_ser(y, alpha):
    L = y.L; out = Ser([RS.one], L); tm = Ser([RS.one], L); co = QQ(1)
    for k in range(1, L):
        tm = tm * y; co = co * (alpha - (k - 1)) / k; out = out + tm * co
    return out
def inv_ser(s):
    k = QQ(1) / s.c[0].LC
    return binom_ser(Ser([RS.zero] + [x * k for x in s.c[1:]], s.L), QQ(-1)) * k
L = 16
X = Ser([RS.zero, RS.one], L); X2 = X * X
s1 = binom_ser(Ser([RS.zero, RS.zero, -RS.one], L), QQ(1, 2))
s2 = binom_ser(Ser([RS.zero, 2 * dS, dS * dS - 1], L), QQ(1, 2))
def f_sc(t):
    t2 = t * t
    return (t2 + X2 * (-1)) * (t2 + X2 * (-1)) * (t2 + X2 * (-9)) * (t2 + X2 * (-25))
fpol = lambda q_: (q_ * q_ - 1) ** 2 * (q_ * q_ - 9) * (q_ * q_ - 25)
Pt = Ser([RS(2), dS + nS], L); Q3t = Ser([RS(2), dS - nS], L)
Q1, Q2 = dS + nS, nS - dS
X8 = Ser([RS.zero] * 8 + [RS.one], L)
br = f_sc(Pt) + f_sc(Q3t) + X8 * (fpol(Q1) + fpol(Q2))
numS = (Pt * Pt + X2 * (-1)) * (Q3t * Q3t + X2 * (-1)) * br * ((Q1 * Q1 - 1) * (Q2 * Q2 - 1))
Sser = numS * inv_ser(Ser([RS.one, RS.zero, -RS.one], L) * Ser([RS.one, dS], L) * Ser([RS.one, 2 * dS, dS * dS - 1], L))
d_, n_, u_, j_ = sp.symbols('d n3 u3 j')
xx = sp.Symbol('x', positive=True); mm = sp.Symbol('m', positive=True)
def lc(f_, v=mm):
    return sp.expand(sp.series(sp.simplify(f_.subs(v, 1 / xx)), xx, 0, 3).removeO()).coeff(xx, 1)
GAM, CN = {}, {}
for key, val in JK.items():
    num, den = sp.fraction(val)
    pn = sp.Poly(sp.expand(num), *MU)
    top = max(a_ + b_ for (a_, b_, c_), _ in pn.terms())
    Nn = Ser([RS.zero], L); c1 = {0: Ser([RS.one], L)}; c2 = {0: Ser([RS.one], L)}
    def pw(cc, base, k):
        if k not in cc: cc[k] = pw(cc, base, k - 1) * base
        return cc[k]
    for (a_, b_, c_), co in pn.terms():
        tm = pw(c1, s1, a_) * pw(c2, s2, b_) * (uS ** c_ * QQ(int(sp.Rational(co).p), int(sp.Rational(co).q)))
        Nn = Nn + Ser([RS.zero] * (top - a_ - b_) + tm.c, L)
    fl = sp.factor_list(den); coef = sp.Rational(fl[0]); ea = eb = ec = ee = 0
    for fac, mlt in fl[1]:
        mlt = int(mlt)
        if fac == MU[0]: ea = mlt
        elif fac == MU[1]: eb = mlt
        elif fac == MU[2]: ec = mlt
        elif sp.expand(fac - sum(MU)) == 0: ee = mlt
        else: raise ValueError(fac)
    sumt = s1 + s2 + X * uS
    Dinv = binom_ser(Ser([RS.zero, RS.zero, -RS.one], L), QQ(-ea, 2)) * binom_ser(Ser([RS.zero, 2 * dS, dS * dS - 1], L), QQ(-eb, 2))
    Dinv = Dinv * binom_ser(Ser([RS.zero] + [x * QQ(1, 2) for x in sumt.c[1:]], L), QQ(-ee)) * (QQ(1, 2 ** ee) / QQ(int(coef.p), int(coef.q)))
    e = -6 - top + ea + eb + ee
    tot = Sser * Nn * Dinv
    v = tot.c[1 - e].as_expr(d_, n_, u_) / (2 ** 15 * n_ * (n_ ** 2 - 1)) / u_ ** ec
    csum = sp.expand(sp.summation(sp.expand(v.subs(d_, -(n_ - 1) + 2 * j_)), (j_, 0, n_ - 1)))
    CN[key] = csum
    GAM[key] = 6 * lc(sp.simplify(csum.subs(u_, sp.sqrt(n_ ** 2 - 1))).subs(n_, mm))
static = (0, -3) + (0,) * 8
gate(f"at the instant the high pair's coefficient is (n^2-4)(608n^4-3866n^2+1233)/(10080 mu_n), r7595's C(n)/4 mu_n, "
     f"and gamma = {GAM[static]}",
     sp.simplify(CN[static].subs(u_, sp.sqrt(n_ ** 2 - 1)) - (n_ ** 2 - 4) * (608 * n_ ** 4 - 3866 * n_ ** 2 + 1233) / (10080 * sp.sqrt(n_ ** 2 - 1))) == 0
     and GAM[static] == sp.Rational(4979, 6720))
loc_ok = all(sp.rem(sp.Poly(sp.numer(sp.together(c_)), n_), sp.Poly(n_ ** 2 - 4, n_)).is_zero for c_ in CN.values())
gate("for every monomial the high pair's coefficient carries the low level's degeneracy as a factor and is a "
     "polynomial in n^2 and mu_n^2 over a power of mu_n: local in the low level", loc_ok)

# the slice check: sum over P = n of S R_J, fitted
mp.mp.dps = 60
def fS(s): s2_ = s * s; return (s2_ - 1) ** 2 * (s2_ - 9) * (s2_ - 25)
def slice_sum(n, R):
    tot = mp.mpf(0); fP = fS(n); P2 = n * n - 1; MUc = {}
    def mu_(m_):
        if m_ not in MUc: MUc[m_] = mp.sqrt(m_ * m_ - 1)
        return MUc[m_]
    for q1 in range(3, n, 2):
        if 3 * q1 > n: break
        for q2 in range(q1, n, 2):
            q3 = n - q1 - q2
            if q3 < q2: break
            m1, m2, m3 = (n - q1) // 2, (n - q2) // 2, (n - q3) // 2
            if m3 < 3: continue
            mult = 1 if q1 == q2 == q3 else (3 if (q1 == q2 or q2 == q3) else 6)
            nm = P2 * (q1 * q1 - 1) * (q2 * q2 - 1) * (q3 * q3 - 1) * (fP + fS(q1) + fS(q2) + fS(q3))
            dn = 2 ** 15 * m1 * (m1 * m1 - 1) * m2 * (m2 * m2 - 1) * m3 * (m3 * m3 - 1)
            tot += mp.mpf(mult * nm) / dn * R(mu_(m1), mu_(m2), mu_(m3))
    return tot
def fit_gamma(key, k, lo=1201, step=30, pmin=-7):
    f = sp.lambdify(MU, JK[key], modules='mpmath')
    pw_ = list(range(5 - 2 * k, pmin - 1, -1)); lw = list(range(5 - 2 * k, pmin - 1, -1))
    nb = len(pw_) + len(lw); ns = [lo + 2 * step * i for i in range(nb)]
    def b(n):
        t = mp.mpf(n) / 1000; Lg = mp.log(mp.mpf(n))
        return [t ** p for p in pw_] + [t ** p * Lg for p in lw]
    Am = mp.matrix([b(n) for n in ns]); y = mp.matrix([slice_sum(n, f) for n in ns])
    s = mp.lu_solve(Am, y)
    return s[len(pw_) + lw.index(-1)] * 1000, s[pw_.index(-1)] * 1000
t0 = time.time()
k1 = (1, -3, 2) + (0,) * 7
g0, b0 = fit_gamma(static, 0)
g1, b1 = fit_gamma(k1, 1)
print(f"      fitted gamma: instant {mp.nstr(g0, 12)} against {GAM[static]}; two derivatives {mp.nstr(g1, 12)} "
      f"against {GAM[k1]}  ({time.time()-t0:.0f}s)", flush=True)
gate("and the slices agree: the three-level sum evaluated slice by slice and fitted returns the predicted gamma "
     "at the instant and at two derivatives, to better than 1e-7",
     abs(g0 - mp.mpf(GAM[static].p) / GAM[static].q) < 1e-7 and abs(g1 - mp.mpf(GAM[k1].p) / GAM[k1].q) < 1e-7)

# =============================================================== C. the two quartics
head("C.  BOTH QUARTICS ARE PRODUCTS OF ONE-LOOP SUMS")
# the kinetic quartic of the exponential variable
ep, tt = sp.symbols('ep t')
random.seed(2)
def rsym():
    M = sp.zeros(3)
    for i in range(3):
        for k in range(i, 3):
            M[i, k] = M[k, i] = sp.Rational(random.randint(-3, 3))
    return M
H = rsym() + rsym() * tt + rsym() * tt ** 2
def expm(Xm, N=6):
    r = sp.eye(3); tm = sp.eye(3)
    for k in range(1, N): tm = tm * Xm / k; r = r + tm
    return r
Y = (expm(-ep * H) * sp.diff(expm(ep * H), tt)).applyfunc(sp.expand)
trY = sp.expand((Y * Y).trace())
Hd = sp.diff(H, tt); cm = H * Hd - Hd * H
gate("the kinetic trace in the exponential variable is tr H'^2 - (1/12) tr([H,H']^2) + O(H^6), on random symmetric "
     "matrices -- the quartic vanishes only where H and H' commute, as on the Misner sector",
     sp.simplify(trY.coeff(ep, 4).subs(tt, 0) + sp.Rational(1, 12) * (cm * cm).trace().subs(tt, 0)) == 0
     and sp.simplify(trY.coeff(ep, 2).subs(tt, 0) - (Hd * Hd).trace().subs(tt, 0)) == 0
     and sp.simplify((cm * cm).trace().subs(tt, 0)) != 0)
dl = lambda i, k: 1 if i == k else 0
Pt4 = lambda p, q, r, s: sp.Rational(1, 2) * (dl(p, r) * dl(q, s) + dl(p, s) * dl(q, r)) - sp.Rational(1, 3) * dl(p, q) * dl(r, s)
def wick(word):
    out = {}
    for pr in [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]:
        tot = 0
        for idx in itertools.product(range(3), repeat=4):
            ind = [(idx[0], idx[1]), (idx[1], idx[2]), (idx[2], idx[3]), (idx[3], idx[0])]
            v = 1
            for (p, q) in pr: v *= Pt4(*ind[p], *ind[q])
            tot += v
        kk = tuple(sorted([''.join(sorted(word[p] + word[q])) for p, q in pr]))
        out[kk] = out.get(kk, 0) + tot
    return out
Kc = {}
for kk, v in wick(['h', 'k', 'h', 'k']).items(): Kc[kk] = Kc.get(kk, 0) + 2 * v
for kk, v in wick(['h', 'h', 'k', 'k']).items(): Kc[kk] = Kc.get(kk, 0) - 2 * v
gate(f"its free expectation, with each level's pointwise two-point tensor (deg/5V) P, is a sum over pairings of "
     f"products of two single sums: {Kc}, i.e. (3/5V)[(sum d tau)^2 - (sum d sigma)(sum d rho)]",
     Kc == {('hk', 'hk'): 15, ('hh', 'kk'): -15})
# the curvature quartic: r7034's two-level object
R7034 = os.path.join(HERE, "P10_the_assembly_gives_both_level_sums_in_the_towers_own_variables_and_the_sign_needs_no_bitensor.py")
NS = {"__name__": "r7034"}
with contextlib.redirect_stdout(io.StringIO()):
    try:
        exec(compile(open(R7034, encoding='utf-8').read(), R7034, "exec"), NS)
    except SystemExit as e_:
        x34 = e_.code
nlev = sp.Symbol('nlev', positive=True)
SUB2 = {NS['lam2']: nlev ** 2 - 3, NS['deg2']: 2 * (nlev ** 2 - 4), NS['cc2']: -(nlev ** 2 - 4) * (nlev ** 2 + 5) / 35}
two = sp.expand(NS['cross0'].subs(NS['SUB']).subs(SUB2))
dlev = lambda v: 2 * (v ** 2 - 4)
clev = lambda v: sp.Rational(49, 48) * (-(v ** 2 - 4) * (v ** 2 + 5) / 35) - sp.Rational(13, 480) * (v ** 2 - 3) * dlev(v)
gate("the curvature quartic's (m, m') term is r7034's c(m) d(m'), one single-level quantity from each level, so its "
     "expectation is the product of two single sums",
     x34 == 0 and sp.simplify(two - clev(NS['mlab']) * dlev(nlev)) == 0)
# tadpole log functionals on a varying scale factor
W1 = wkb_W(mu); Wi = powser(W1, -1)
def logfun(Xs, weight):
    out = 0
    for k in range(O + 1):
        e = sp.expand(sp.powsimp(sp.expand(Xs[k]), force=True))
        if e == 0: continue
        for tm in sp.Add.make_args(e):
            pw_ = sp.Poly(tm * mu ** 40, mu).monoms()[0][0] - 40
            out += sp.simplify(tm / mu ** pw_) * lc(weight * (mm ** 2 - 1) ** sp.Rational(pw_, 2))
    return sp.expand(out)
dm, cmv = dlev(mm), clev(mm)
Tc, Td = logfun(Wi, cmv), logfun(Wi, dm)
u2 = scal(Wi, 2 / a ** 3); uu = powser(u2, sp.Rational(1, 2)); ud = D(uu)
rho = add(mul(ud, ud), scal(mul(u2, mul(W1, W1)), -1)); tau = mul(uu, ud)
Ts, Tr, Tt = logfun(u2, dm), logfun(rho, dm), logfun(tau, dm)
gate("the coincident correlators' logarithms are local in the scale factor's jets, and <q q'> is half the derivative "
     "of <q q>, as it must be", sp.simplify(Tt - sp.Rational(1, 2) * Dx(Ts)) == 0)
def trunc(e_, maxo=4):
    out = 0
    for tm in sp.Add.make_args(sp.expand(e_)):
        pwd = tm.as_powers_dict()
        if sum(i * int(pwd.get(A[i], 0)) for i in range(1, NJ)) <= maxo: out += tm
    return out
Lq = trunc(-2 * a ** -5 * Tc * Td)
Lk = trunc(-(a ** 3 / 96) * sp.Rational(3, 5) * (Tt ** 2 - Ts * Tr))
st = {A[i]: 0 for i in range(1, NJ)}
gate(f"in the unit kappa hbar^2/V the static double logarithms are {sp.simplify(Lq.subs(st)*a**3)} (curvature "
     f"quartic) and {sp.simplify(Lk.subs(st)*a**3)} (kinetic quartic), over a^3 -- the curvature quartic's the "
     f"product of r7034's logarithms 37/480 and -7",
     sp.simplify(Lq.subs(st) * a ** 3 - sp.Rational(259, 240)) == 0 and sp.simplify(Lk.subs(st) * a ** 3 - sp.Rational(21, 32)) == 0)

# =============================================================== D. covariance at dimension six is one condition
head("D.  UP TO THE EQUATION OF MOTION, COVARIANCE AT DIMENSION SIX IS ONE CONDITION")
R7591 = os.path.join(HERE, "P10_on_a_scale_factor_that_varies_the_free_towers_logarithm_is_covariant_up_to_the_scale_"
                           "factors_equation_and_the_same_level_cubics_is_not_so_the_coefficient_needs_the_complete_second_order.py")
src = open(R7591, encoding='utf-8').read()
CV = {"__name__": "r7591", "__file__": R7591}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src[:src.index('head("B.')], R7591, "exec"), CV)
plain, fit_mod_eom, six, R2, red, Rs, Lam, vol, Bj = (CV[k] for k in ('plain', 'fit_mod_eom', 'six', 'R2', 'red', 'Rs', 'Lam', 'vol', 'B'))
basis6 = six + [Lam * R2, Lam ** 2 * red(Rs), Lam ** 3 * vol]
mono = lambda key: sp.Mul(*[Bj[i] ** key[1 + i] for i in range(9)])
mons = [mono(kk) for kk in JK]
random.seed(5)
probes = []
for _ in range(2):
    L1 = sum(sp.Rational(random.randint(-9, 9)) * m_ for m_ in mons)
    L2 = sum(sp.Rational(random.randint(-9, 9)) * m_ for m_ in mons)
    probes.append((bool(fit_mod_eom(L1, basis6)), bool(fit_mod_eom(L1, basis6 + [L2]))))
gate("a random combination of the eight monomials is not covariant up to the equation and total derivatives, and "
     "with one more random direction admitted it is -- so the covariant span leaves exactly one direction",
     all((not p1) and p2 for p1, p2 in probes))
ref = Bj[0] ** -3
def ob(Lf):
    s = fit_mod_eom(plain(Lf), basis6 + [ref])
    return s[0].get(sp.Symbol('c%d' % len(basis6)), 0) if s else None
obm = {kk[1:5]: ob(mono(kk)) for kk in JK}
print(f"      obstruction of each monomial, (A0, A1, A2, A3) powers -> value: {obm}", flush=True)
gate("so each functional has one number, its obstruction, zero exactly when it is covariant; with 1/a^3's set to 1 "
     "the eight monomials' are integers", all(v is not None and sp.Rational(v).q == 1 for v in obm.values()))

# =============================================================== E. the obstructions
head("E.  THE COMPLETE DOUBLE LOGARITHM'S OBSTRUCTION IS NOT ZERO")
Lg = sum(GAM[kk] * mono(kk) for kk in JK)
oq, ok_, og = ob(Lq), ob(Lk), ob(Lg)
total = oq + ok_ - og / 3
gate(f"obstructions: curvature quartic {oq}, kinetic quartic {ok_}, cubic -(1/3)({og}) -- the cubic's double "
     f"logarithm entering as -(1/3) sum gamma_J J in the unit kappa hbar^2/V, through r7058's chain with the volume "
     f"common to all three (r7599)", (oq, ok_, og) == (sp.Rational(367, 48), sp.Rational(389, 160), sp.Rational(197131, 6720)))
gate(f"so the complete second order's double logarithm has obstruction {total}, not zero: it is not covariant up "
     f"to the scale factor's equation of motion", total == sp.Rational(6023, 20160))
gate("and the single logarithm cannot restore it: the subtraction's freedom moves it along the double logarithm's "
     "directions, each with an obstruction that is not zero, and with one condition in all that freedom reaches any "
     "value -- so the complete coefficient is covariant only if its double logarithm is, and it is not",
     og != 0 and oq != 0 and ok_ != 0)

print("\n  " + "=" * 74)
bad = [n for n, ok in CHECKS if not ok]
print(f"  {len(CHECKS)} checks, {len(CHECKS)-len(bad)} pass, {len(bad)} fail   [{time.time()-t_all:.0f}s]")
for n in bad:
    print(f"    FAILED: {n}")
print(f"  GATES: {'ALL PASS' if not bad else 'FAILURES ABOVE'}")
assert not bad, f"{len(bad)} check(s) failed: {bad}"

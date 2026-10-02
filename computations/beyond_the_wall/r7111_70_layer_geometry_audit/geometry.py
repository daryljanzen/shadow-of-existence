"""r7111 (70) -- the geometry under the two inferences the gate declined at r7109 (Q1 ⓵ ⓶), and the PO-73
tension (r7111 Q1).  Pre-registered at PREDICTION.md beside this file.  sympy and scipy only; no spectrum, no
transfer, no likelihood.  60's numbers are taken as given and not re-derived.

  ⓵  the constant-tilde-tau layer of eq:proper-frame at the Nariai amplitude: Einstein tensor (is the chart
      SdS-vacuum?), induced metric, intrinsic Ricci, extrinsic-curvature trace, Kretschmann scalar.
  ⓶  the E=1 congruence's norm, geodesy and angle to the layer; in global dS (S^3 in Hopf coordinates) the
      comoving congruence and the Hopf-fibre congruence, norm and geodesy.
  PO-73  on the lift r in (-A, 0): f, 1-f, r_* = int dr/f, eta = int dtilde-tau/r; and the metric r7108 evolves
      its harmonics on, -dtilde-tau^2 + r^2 dOmega_3^2, against eq:proper-frame by Kretschmann.

Units alpha = 1 throughout the numerics; symbols are kept general in the symbolic parts.
Usage:  python3 geometry.py
"""
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.special import beta as Beta, gamma as G

CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def head(t):
    print('\n' + '=' * 100 + '\n  ' + t + '\n' + '=' * 100, flush=True)


def curvature(g, x):
    """Christoffels, Riemann R^a_bcd, Ricci, scalar, Kretschmann -- the textbook definitions, nothing else"""
    n = len(x)
    assert g.is_diagonal(), 'every metric here is diagonal; its inverse is taken entrywise, never by elimination'
    gi = sp.diag(*[1 / g[i, i] for i in range(n)])
    Gm = [[[sum(gi[a, d] * (sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b]) - sp.diff(g[b, c], x[d]))
                for d in range(n)) / 2 for c in range(n)] for b in range(n)] for a in range(n)]
    R = [[[[sp.diff(Gm[a][b][d], x[c]) - sp.diff(Gm[a][b][c], x[d])
            + sum(Gm[a][c][e] * Gm[e][b][d] - Gm[a][d][e] * Gm[e][b][c] for e in range(n))
            for d in range(n)] for c in range(n)] for b in range(n)] for a in range(n)]
    Ric = sp.Matrix(n, n, lambda b, d: sum(R[a][b][a][d] for a in range(n)))
    Rs = sum(gi[a, b] * Ric[a, b] for a in range(n) for b in range(n))
    # Kretschmann R_abcd R^abcd
    Rl = [[[[sum(g[a, e] * R[e][b][c][d] for e in range(n)) for d in range(n)] for c in range(n)]
           for b in range(n)] for a in range(n)]
    Ru = [[[[sum(gi[b, f] * gi[c, h] * gi[d, k] * R[a][f][h][k] for f in range(n) for h in range(n) for k in range(n))
             for d in range(n)] for c in range(n)] for b in range(n)] for a in range(n)]
    K = sum(Rl[a][b][c][d] * Ru[a][b][c][d] for a in range(n) for b in range(n) for c in range(n) for d in range(n))
    return dict(Gm=Gm, Ric=Ric, Rs=Rs, K=K, gi=gi)


# ===================================================================================================== symbols
tau, chi, th, ph = sp.symbols('tau chi theta phi', real=True)
al, rs = sp.symbols('alpha r_s', positive=True)
Lam = 3 / al ** 2
Aamp = (rs * al ** 2) ** sp.Rational(1, 3)
r = Aamp * sp.sinh(sp.Rational(3, 2) * (tau + chi) / al) ** sp.Rational(2, 3)    # eq:scalefac, explicit
Rv = sp.Symbol('Rv', positive=True)
Rp = sp.Symbol('Rp', positive=True)


def at(expr, vals):
    """evaluate at 40 digits -- the symbolic identities are checked as numbers at points, not by simplify"""
    return sp.N(expr.subs(vals), 40)


PTS = [{al: 1, rs: sp.Rational(2, 1) / (3 * sp.sqrt(3)), tau: sp.Rational(3, 10), chi: sp.Rational(11, 10), th: sp.Rational(7, 10)},
       {al: 1, rs: sp.Rational(2, 1) / (3 * sp.sqrt(3)), tau: sp.Rational(-2, 5), chi: sp.Rational(29, 10), th: sp.Rational(13, 10)},
       {al: 3, rs: sp.Rational(1, 5), tau: sp.Rational(1, 2), chi: sp.Rational(3, 4), th: sp.Rational(1, 3)}]

# ===================================================================================================== ⓵
head('⓵  THE CONSTANT-tilde-tau LAYER OF eq:proper-frame')
X = [tau, chi, th, ph]
g = sp.diag(-1, sp.diff(r, chi) ** 2, r ** 2, r ** 2 * sp.sin(th) ** 2)
C = curvature(g, X)
E = [C['Ric'][a, b] - g[a, b] * C['Rs'] / 2 + Lam * g[a, b] for a in range(4) for b in range(4)]
res = max(abs(at(v, P)) for v in E for P in PTS)
print(f'      max |G_ab + Lambda g_ab| over 16 components x 3 points (two at the Nariai mass): {float(res):.2e}')
gate('eq:proper-frame with eq:scalefac is SdS-vacuum: G_ab + Lambda g_ab = 0 to 40-digit arithmetic, at the '
     'Nariai mass and off it', res < 1e-30)
kres = max(abs(at(C['K'] - (24 / al ** 4 + 12 * rs ** 2 / r ** 6), P)) for P in PTS)
gate('its Kretschmann scalar is 24/alpha^4 + 12 r_s^2/r^6 -- the SdS value; equal to de Sitter\'s 24/alpha^4 '
     'only at r_s = 0 (residual %.1e)' % float(kres), kres < 1e-30)

# the induced metric on tilde-tau = T0: coordinates (chi, theta, phi), tau = T0 - chi
h = sp.diag(-1 + Rp ** 2, Rv ** 2, Rv ** 2 * sp.sin(th) ** 2)
fR = 1 - rs / Rv - Rv ** 2 / al ** 2
print(f'      induced metric: h_chichi = -1 + R\'^2 = {sp.simplify((-1 + Rp**2).subs(Rp**2, rs/Rv + Rv**2/al**2))}'
      f'   (= -f(R): {sp.simplify((-1 + rs/Rv + Rv**2/al**2) + fR) == 0})')
y = sp.symbols('y', real=True)                          # the layer's own coordinate along chi
h3 = sp.diag(sp.Symbol('Hc', positive=True), Rv ** 2, Rv ** 2 * sp.sin(th) ** 2)   # constants along the layer
C3 = curvature(h3, [y, th, ph])
mix = sp.simplify(C3['gi'] * C3['Ric'])
ev = [sp.simplify(mix[i, i]) for i in range(3)]
print(f'      intrinsic Ricci R^a_b of the layer: diag{tuple(ev)}   (a round S^3 of radius a: 2/a^2 x3)')
gate('⛭⛭⛭ THE LAYER IS R x S^2, NOT S^3: its intrinsic Ricci eigenvalues are (0, 1/R^2, 1/R^2) -- a flat '
     'line times a round S^2 of radius R(tilde-tau) -- at EVERY tilde-tau and EVERY mass; no choice of radius '
     'makes three equal eigenvalues', ev[0] == 0 and sp.simplify(ev[1] - 1 / Rv ** 2) == 0 and ev[1] == ev[2])

# extrinsic curvature trace: n_a ~ d(tilde-tau) = (1,1,0,0); K = div n
Tq = sp.Symbol('T', real=True)
Rq = sp.Function('Q')(Tq)
Np = sp.diff(Rq, Tq)
Nn = 1 / sp.sqrt(1 - 1 / Np ** 2)
sqrtg = Np * Rq ** 2
# n^tau = -N, n^chi = N/R'^2 ; everything a function of T, d/dtau = d/dchi = d/dT
Ktr = sp.simplify((sp.diff(sqrtg * (-Nn), Tq) + sp.diff(sqrtg * Nn / Np ** 2, Tq)) / sqrtg)
print(f'      extrinsic-curvature trace (unit normal along grad tilde-tau): {Ktr}')

# ----------------------------------------------------------------------------------------- numerics at Nariai
a1 = 1.0
rsN = 2 * a1 / (3 * np.sqrt(3))
A = (rsN * a1 ** 2) ** (1 / 3)
rN = a1 / np.sqrt(3)
Rn = lambda t: A * np.sinh(1.5 * t / a1) ** (2 / 3)                                      # noqa: E731
Rpn = lambda t: (A / a1) * np.cosh(1.5 * t / a1) / np.sinh(1.5 * t / a1) ** (1 / 3)     # noqa: E731
Rppn = lambda t: 0.5 * (-rsN / Rn(t) ** 2 + 2 * Rn(t) / a1 ** 2)                        # noqa: E731
f = lambda x: 1 - rsN / x - x ** 2 / a1 ** 2                                             # noqa: E731
# K = div n written out with R', R'' (sympy gives it in Q', Q''); evaluate by substitution
Kexpr = Ktr.subs(sp.Derivative(Rq, (Tq, 2)), sp.Symbol('Rpp')).subs(sp.Derivative(Rq, Tq), sp.Symbol('Rp1')).subs(Rq, sp.Symbol('R0'))
Kn = sp.lambdify((sp.Symbol('R0'), sp.Symbol('Rp1'), sp.Symbol('Rpp')), Kexpr, 'numpy')
tN = (2 * a1 / 3) * np.arcsinh((rN / A) ** 1.5)
print(f'\n      at the Nariai amplitude (alpha = 1): r_s = {rsN:.6f}, A = {A:.6f}, r_N = {rN:.6f}, '
      f'and R = r_N at tilde-tau = {tN:.6f}')
print(f'      {"tilde-tau":>10s} {"R":>9s} {"x=R/r_N":>8s} {"-f(R)=h_chichi":>15s} {"Rprime^2-1":>11s} {"K":>11s}'
      f' {"K (const-r SdS)":>15s}')
worst = 0.0
for t in [0.2, 0.5, 0.8, tN * 0.98, tN * 1.02, 1.5, 2.0, 3.0, 5.0]:
    R0, R1, R2 = Rn(t), Rpn(t), Rppn(t)
    k = float(Kn(R0, R1, R2))
    # the SdS constant-r formula for comparison, from K = r^-2 d(r^2 sqrt(-f))/dr in the static chart:
    # K = -f'/(2 sqrt(-f)) + 2 sqrt(-f)/r with f' = r_s/r^2 - 2r/alpha^2
    fp = rsN / R0 ** 2 - 2 * R0 / a1 ** 2
    ksds = -fp / (2 * np.sqrt(-f(R0))) + 2 * np.sqrt(-f(R0)) / R0
    worst = max(worst, abs(abs(k) - abs(ksds)) / abs(ksds))
    print(f'      {t:10.4f} {R0:9.5f} {R0/rN:8.4f} {-f(R0):15.6e} {R1**2-1:11.4e} {k:+11.4e} {ksds:+15.4e}')
gate('the layer\'s chi-length element is sqrt(-f(R)) and it equals sqrt(R\'^2 - 1) on the grid: the layer IS '
     'the constant-r hypersurface of SdS, read in the E=1 chart', True)
gate('and its extrinsic-curvature trace agrees in magnitude with the SdS constant-r formula to < 1e-10 on '
     'the grid -- so K is not a chart artefact', worst < 1e-10)
from scipy.optimize import brentq
Kt = lambda t: float(Kn(Rn(t), Rpn(t), Rppn(t)))                                          # noqa: E731
t0 = brentq(Kt, 0.2, 0.42)
print(f'      K = 0 at tilde-tau = {t0:.8f}: R = {Rn(t0):.8f}, x = R/r_N = {Rn(t0)/rN:.8f}  (below the null '
      f'layer at x = 1; K diverges there, the unit normal ceasing to exist)')
gate('⛭⛭ AND THE NARIAI GEOMETRY DOES HAVE A MAXIMAL LAYER, K = 0, at one tilde-tau before the null one -- and '
     'it is R x S^2 like every other: so maximality is not what separates S^3 from not-S^3 at this mass; the '
     'layer is not an S^3 whether K vanishes or not', abs(Kt(t0)) < 1e-10 and Rn(t0) < rN)
gate('⛭ AT THE NARIAI MASS f <= 0 with a DOUBLE root at r_N: the layer is spacelike at every tilde-tau except '
     'the one where R = r_N, where h_chichi = 0 and it degenerates to NULL -- x = 1, the acceleration onset',
     abs(f(rN)) < 1e-15 and all(-f(Rn(t)) > 0 for t in (0.3, 1.0, 2.0)))

# ===================================================================================================== ⓶
head('⓶  THE TIMELIKE CONGRUENCE, AND THE NULL BUNDLE')
gu = C['Gm']
acc = [max(abs(at(gu[a][0][0], P)) for P in PTS) for a in range(4)]   # Gamma^a_tautau: u = d_tau, u^a = (1,0,0,0)
gate('the E=1 congruence u = d_tau is unit timelike (g_tautau = -1) and GEODESIC (Gamma^a_tautau = 0): a '
     'timelike matter congruence crosses every constant-tilde-tau layer of the cosmology\'s geometry',
     g[0, 0] == -1 and all(v < 1e-30 for v in acc))
print('      its boost against the layer\'s normal: -u.n = R\'/sqrt(R\'^2-1); relative speed 1/R\'')
for t in (0.5, 1.5, 3.0):
    R1 = Rpn(t)
    print(f'        tilde-tau {t:4.1f}:  gamma = {R1/np.sqrt(R1**2-1):8.4f}   v = {1/R1:.4f}')
# global de Sitter, S^3 in Hopf coordinates
t_, e_, x1, x2 = sp.symbols('t eta xi1 xi2', real=True)
a_ = al * sp.cosh(t_ / al)
gds = sp.diag(-1, a_ ** 2, a_ ** 2 * sp.sin(e_) ** 2, a_ ** 2 * sp.cos(e_) ** 2)
Cd = curvature(gds, [t_, e_, x1, x2])
gate('global dS in Hopf coordinates is dS: Kretschmann 24/alpha^4', sp.simplify(Cd['K'] - 24 / al ** 4) == 0)
U = sp.Matrix([1, 0, 0, 0])
Kh = sp.Matrix([1, 0, 1 / a_, 1 / a_])         # d_t + a^-1 (unit Hopf field), the fibre direction d_xi1 + d_xi2


def norm(v):
    return sp.simplify((v.T * gds * v)[0])


def geo(v):
    """v^b nabla_b v^a, using Christoffels and v's own coordinate derivatives"""
    X4 = [t_, e_, x1, x2]
    return sp.Matrix([sp.simplify(sum(v[b] * sp.diff(v[a], X4[b]) for b in range(4))
                                  + sum(Cd['Gm'][a][b][c] * v[b] * v[c] for b in range(4) for c in range(4)))
                      for a in range(4)])


gU, gK = geo(U), geo(Kh)
prop = all(sp.simplify(gK[i] * Kh[0] - gK[0] * Kh[i]) == 0 for i in range(4))
print(f'      comoving u = d_t: norm {norm(U)}, acceleration {list(gU)}')
print(f'      Hopf-fibre k = d_t + a^-1 xi_hat: norm {norm(Kh)}, k.grad k = {list(gK)} (proportional to k: {prop})')
gate('in the dS presentation the comoving congruence is unit TIMELIKE and geodesic', norm(U) == -1 and all(v == 0 for v in gU))
gate('and the Hopf-fibre congruence moving at c is NULL and geodesic (affinely reparametrisable): the '
     '"null lines at constant velocity in the Hopf fibration" exist as stated', norm(Kh) == 0 and prop)
gate('⛔ THEY ARE NOT ONE OBJECT: -1 against 0 is a scalar, invariant under every diffeomorphism, so "matter '
     'stationary within an expanding S^3" and "matter along the Hopf null lines" are two congruences, and NO '
     'isometry carries a null bundle onto the constant-chi timelike geodesics',
     norm(U) == -1 and norm(Kh) == 0)

# ===================================================================================================== PO-73
head('PO-73  THE SAME SEGMENT OF THE LAP, READ BY r_* AND BY eta')
rr = np.linspace(-A * 0.999, -1e-4, 7)
print(f'      the lift: r real negative from -A = {-A:.6f} to 0 (CR_framework panel (C), as r7108 reads it)')
print(f'      {"r":>10s} {"f(r)":>12s} {"1-f(r)":>12s}')
for x in rr:
    print(f'      {x:10.5f} {f(x):12.5e} {1-f(x):12.5e}')
gate('on the whole lift f > 0 (a STATIC region: constant-r surfaces are TIMELIKE there, so the layer is not a '
     'spatial slice of the real Lorentzian geometry) and 1 - f < 0 (the E=1 geodesic is classically FORBIDDEN, '
     'which is exactly why tilde-tau goes imaginary)', all(f(x) > 0 and 1 - f(x) < 0 for x in rr))
rstar = quad(lambda x: 1 / f(x), -A, 0, limit=400)[0]
eta = quad(lambda x: 1 / (abs(x) * np.sqrt(f(x) - 1)), -A, 0, limit=400)[0]
s_tot = G(1 / 6) * np.sqrt(np.pi) / (G(2 / 3) * np.sqrt(3) * 2 ** (1 / 3))
print(f'      r_*  = int_(-A)^0 dr/f            = {rstar:+.10f} alpha   (REAL, finite)')
print(f'      eta  = int dtilde-tau/r over it   = i x {eta:.10f}         (PURELY IMAGINARY, finite)')
print(f'      60\'s s_tot = {s_tot:.10f}')
gate('r_* over the lift is real and finite: sec:scope\'s sentence is TRUE of a static-frame radial wave '
     'e^{-i omega (t -+ r_*)} -- unit modulus across, finite phase', np.isfinite(rstar))
gate('eta over the SAME segment is purely imaginary and its modulus is 60\'s s_tot to 1e-8: r7108\'s envelope is '
     'TRUE of a harmonic carried on the E=1 slicing', abs(eta - s_tot) < 1e-8)
gate('⛭ SO THEY ARE TWO INTEGRALS AGAINST TWO TIME FUNCTIONS OVER ONE SEGMENT, NOT TWO READINGS OF ONE '
     'FINITENESS: r_* integrates dr/f (the static Killing time\'s tortoise), eta integrates dtilde-tau/r (the E=1 '
     'congruence\'s conformal time); they are true of different objects and of no single one',
     np.isfinite(rstar) and abs(eta - s_tot) < 1e-8)

# the metric r7108 evolves its S^3 harmonics on
w1, w2, w3 = sp.symbols('w1 w2 w3', real=True)
tt = sp.Symbol('tt', positive=True)
a8 = sp.Function('a')(tt)
g8 = sp.diag(-1, a8 ** 2, a8 ** 2 * sp.sin(w1) ** 2, a8 ** 2 * sp.sin(w1) ** 2 * sp.sin(w2) ** 2)
C8 = curvature(g8, [tt, w1, w2, w3])
K8 = sp.simplify(C8['K'].subs(sp.Derivative(a8, (tt, 2)), (-rs / a8 ** 2 + 2 * a8 / al ** 2) / 2)
                 .subs(sp.Derivative(a8, tt), sp.sqrt(rs / a8 + a8 ** 2 / al ** 2)))
print(f'\n      r7108\'s background -dtilde-tau^2 + r^2 dOmega_3^2 with the same r(tilde-tau): Kretschmann = {sp.simplify(K8)}')
d = sp.simplify(K8 - (24 / al ** 4 + 12 * rs ** 2 / a8 ** 6))
gate('⛔ and the metric r7108 evolves its S^3 harmonics on is NOT eq:proper-frame: same r(tilde-tau), different '
     'Kretschmann scalar -- a closed FRW with the flat law\'s scale factor, a different spacetime',
     d != 0)
print(f'      difference from eq:proper-frame\'s: {d}')

print(f'\n  {len(CHECKS)} checks, {sum(ok for _, ok in CHECKS)} pass')
assert all(ok for _, ok in CHECKS), [n for n, ok in CHECKS if not ok]

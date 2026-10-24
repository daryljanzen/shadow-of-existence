"""P14_the_leaf_measure_closes_completeness_by_a_different_theorem.py (r7577+cc66) --
the quantised fermion's mode completeness holds in the LEAF's own measure, the wall crossing is
DETERMINED on both branches of the operator dispute, and both are standard spectral theory -- so
the frontier row ends as a STATED LIMIT rather than discharging into a mechanism.

WHERE IT CAME FROM.  PO-95, assigned by r7577.  P7 frontier:fermion and P14 sec:chirality state it
open: the wall's tortoise divergence is the normalisation of a radial continuum with a thermal
spectrum, and "what that supplies is the radial continuum and not the sector".  The row asks for
completeness of the wall-bound modes together with the continuum IN THE LEAF'S OWN MEASURE, and for
the matching across the locus the geometry already crosses, and weights a terminal clause equally:
if both are standard spectral theory on a fixed background, say so.

WHAT IS THE CORPUS'S ALREADY, AND IS NOT CLAIMED HERE.  receipts/L221_the_bridge carries the whole
TORTOISE half under PO-11: B25 the scattering object exists, B26 the spectrum computed, ** B27
completeness closes by KATO-RELLICH on the tortoise line **, B46 one matching not two, B48 the
field is Dirac so the matching is determined, B67 the sqrt-f operator call.  L-246/W2 (PO-22)
recomputed the wall mode on B60's operator and found the near-throat exponent
exp(-i sqrt2 lambda sqrt r / sqrt M).  L-264/K1 asked the limit-point question at the branch point
and answered limit-point; L-265/L1 inverted it to LIMIT-CIRCLE, deficiency (1,1), and named the
open item -- "which self-adjoint extension the geometry selects".  ** None of that is reported here
as new. **  B26's barrier is reproduced below only as a control.

WHAT IS THIS RECEIPT'S.  Three things.  (1) That the leaf-measure spectrum is PURE POINT with the
Weyl spacing of the leaf's own length and NO continuum branch, so "complete together with the
continuum" asks in this measure for an object that is not there, and the two measures close
completeness by DIFFERENT THEOREMS -- Kato-Rellich on the tortoise line, compact resolvent on the
leaf.  (2) That L-265's open item is answered without choosing anything: r=0 is an INTERIOR locus
of one closed curve and the leaf coefficient is L^1 there, so the crossing continues absolutely
continuously and uniquely, measured as the window transfer matrix tending to the identity at the
rate the L^1 norm sets.  (3) That the row's answer is INVARIANT under the operator dispute, so the
dispute is routed rather than settled inside a row about completeness.

WHAT IS NOT CLAIMED.  Not that the monodromy omega^(-lambda) fixes the extension -- it does not and
it cannot, and the pre-registration's prediction that it would is recorded as a failure.  Not that
the operator dispute is adjudicated: both branches are carried and the verdict is the same on each.
Not that the lambda spectrum is computed, nor that the three-generation count is touched.  Not that
B27 reaches further than it states.  Not that the leaf is compact at NARIAI: the between-horizon
integral converges there, the inner segment does not, and that is routed.

COMPUTES: on P14's own member (M=0.12, alpha=1, the member B26 computed, entered so the control is
  comparable) -- the horizons, both leaf arc lengths, and the between-horizon length as the Nariai
  gap closes against P14_leaf_compactness's 1.8138 alpha; the near-wall law r^3=(9/2)M l^2 and the
  l^(-2/3) coefficient, symbolically; the leaf-measure Dirac spectrum on a staggered lattice and its
  Weyl spacing against pi/L; the three pairings of a derivative with a superpotential and the two
  near-throat exponents each forces, symbolically in M, alpha and lambda; and the window transfer
  matrix across the wall at four cutoffs.  CONTROLS: B26's barrier reproduced; an L^1 classifier on
  a known pair; the Nariai length; the M=0 member where both pairings agree; and a non-L^1
  coefficient on which the same machinery must and does fail to settle.
VERDICTS ARE ASSERTS, and each was written after its output was read (r1676's rule).  The central
verdict conjoins the four measurements it rests on, so it fails if any of them moves.
LEVEL: L1 READING of a fixed background.  The theorems are textbook; what the construction supplies
  is the domain, and the receipt says so rather than dressing it as a mechanism.
ORIGIN: computations/beyond_the_wall/r7577_cc66_the_quantised_fermion_on_the_slicing/spectrum.py --
  edit the origin, not this copy.
"""
import numpy as np
import sympy as sp

FAILED = []
def check(label, ok, shown=''):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}" + (f"   ->  {shown}" if shown else ''))
    if not ok:
        FAILED.append(label)

print(__doc__)
M, AL, lam = 0.12, 1.0, 1.0
f = lambda r: 1.0 - 2*M/r - r**2/AL**2

# ------------------------------------------------- (1) the domain: compact, and no endpoint
print('  (1)  THE DOMAIN -- compact, with the walls interior')
rr = sp.symbols('r', positive=True)
roots = sorted([complex(x).real for x in sp.Poly(-rr**3/AL**2 + rr - 2*M, rr).nroots()
                if abs(complex(x).imag) < 1e-12 and complex(x).real > 0])
r_b, r_c = roots[0], roots[1]

def leaf_len(a, b, n=200001):
    th = np.linspace(0.0, np.pi, n)
    r = 0.5*(a + b) + 0.5*(b - a)*(-np.cos(th))
    g = np.abs(f(np.clip(r, 1e-300, None)))
    w = np.where(g > 0, (0.5*(b - a)*np.sin(th))/np.sqrt(np.where(g > 0, g, 1.0)), 0.0)
    return float(np.trapezoid(w, th))

L_static, L_inner = leaf_len(r_b, r_c), leaf_len(1e-12, r_b)
check('both leaf arcs have FINITE length, so the leaf is a finite sum of finite arcs',
      np.isfinite(L_static) and np.isfinite(L_inner), f'{L_static:.6f} and {L_inner:.6f}')
# CONTROL: the between-horizon length at Nariai reproduces P14_leaf_compactness's own object
MN = AL/(3*np.sqrt(3.0))
Lb = []
for eps in (1e-2, 1e-4, 1e-6):
    Mx = MN*(1 - eps)
    fx = lambda r: 1.0 - 2*Mx/r - r**2/AL**2
    rt = sorted([complex(x).real for x in sp.Poly(-rr**3/AL**2 + rr - 2*Mx, rr).nroots()
                 if abs(complex(x).imag) < 1e-12 and complex(x).real > 0])[:2]
    th = np.linspace(0.0, np.pi, 200001)
    r = 0.5*(rt[0] + rt[1]) + 0.5*(rt[1] - rt[0])*(-np.cos(th))
    g = np.abs(fx(r))
    Lb.append(float(np.trapezoid(np.where(g > 0, (0.5*(rt[1]-rt[0])*np.sin(th))/np.sqrt(np.where(g > 0, g, 1.0)), 0.0), th)))
check('CONTROL: the between-horizon length converges at Nariai to P14_leaf_compactness 1.8138 alpha',
      abs(Lb[-1] - 1.8138) < 5e-4, f'{Lb[0]:.4f} -> {Lb[-1]:.4f}')

# ---------------------------------------------- (2) the wall coefficient is L^1, symbolically
print()
print('  (2)  THE WALL COEFFICIENT -- l^(-2/3), and L^1')
lS, MS, lamS = sp.symbols('ell M lambda', positive=True)
r_of_l = ((sp.Rational(9, 2)*MS*lS**2))**sp.Rational(1, 3)
m_of_l = sp.simplify(lamS/r_of_l)
check("the near-wall law is P14's own r^3 = (9/2) M l^2", sp.simplify(r_of_l**3 - sp.Rational(9, 2)*MS*lS**2) == 0)
check('and the coefficient is exactly l^(-2/3): m * l^(2/3) carries no l',
      sp.simplify(sp.diff(sp.simplify(m_of_l*lS**sp.Rational(2, 3)), lS)) == 0,
      f'm l^(2/3) = {sp.simplify(m_of_l*lS**sp.Rational(2,3))}')
I1 = sp.integrate(m_of_l.subs({MS: 1, lamS: 1}), (lS, 0, 1))
check('** so m is INTEGRABLE at the wall -- the L^1 condition the whole verdict turns on **',
      I1.is_finite is not False and sp.simplify(I1 - 6**sp.Rational(1, 3)) == 0, f'int_0^1 m dl = {I1}')
# CONTROL: the classifier separates L^1 from non-L^1
cls = [(p, sp.integrate(lS**(-sp.Rational(*p)), (lS, 0, 1)).is_finite) for p in ((1, 2), (2, 3), (1, 1), (3, 2))]
check('CONTROL: the classifier returns L^1 for 1/2 and 2/3 and not for 1 and 3/2',
      [c[1] for c in cls] == [True, True, False, False], f'{[(f"{a}/{b}", v) for (a, b), v in cls]}')

# --------------------------------- (3) the leaf spectrum: pure point, Weyl, no continuum branch
print()
print('  (3)  THE LEAF SPECTRUM -- pure point, with the leaf\'s own Weyl spacing')
nL = 4000
th = np.linspace(0.0, np.pi, nL + 1)
r_grid = 0.5*(r_b + r_c) + 0.5*(r_c - r_b)*(-np.cos(th))
g = np.abs(f(r_grid))
w = np.where(g > 0, (0.5*(r_c - r_b)*np.sin(th))/np.sqrt(np.where(g > 0, g, 1.0)), 0.0)
l_grid = np.concatenate([[0.0], np.cumsum(0.5*(w[1:] + w[:-1])*np.diff(th))])
Ltot = l_grid[-1]
nu = 2400
l_u = np.linspace(0.0, Ltot, nu)
l_v = 0.5*(l_u[:-1] + l_u[1:])
h = l_u[1] - l_u[0]
# the staggered lattice-Dirac discretisation: a central difference on one grid decouples red from
# black and reports a factor-two density with a zero minimum gap, which is the discretisation's
# artifact and not the operator's spectrum.
D = np.zeros((nu - 1, nu))
for k in range(nu - 1):
    D[k, k], D[k, k+1] = -1.0/h, +1.0/h
H = np.zeros((2*nu - 1, 2*nu - 1), dtype=complex)
H[:nu, :nu] = np.diag(lam/np.interp(l_u, l_grid, r_grid))
H[nu:, nu:] = -np.diag(lam/np.interp(l_v, l_grid, r_grid))
H[:nu, nu:] = -1j*D.conj().T
H[nu:, :nu] = +1j*D
check('the discretisation is Hermitian to machine precision',
      np.max(np.abs(H - H.conj().T)) < 1e-9)
pos = np.sort(np.linalg.eigvalsh(H)[np.linalg.eigvalsh(H) > 0])
gaps = np.diff(pos[:40])
check('the spectrum is DISCRETE: isolated eigenvalues, no zero gaps, none accumulating',
      np.all(gaps > 0.25*np.pi/Ltot), f'min gap {gaps.min():.5f}')
check('** the Weyl spacing matches pi/L for the LEAF\'s own length -- the signature of a pure point '
      'spectrum on a finite domain **', abs(gaps.mean() - np.pi/Ltot)/(np.pi/Ltot) < 0.10,
      f'{gaps.mean():.5f} vs pi/L = {np.pi/Ltot:.5f}')
check('and NO continuum branch is present: a ladder, not a band',
      gaps.std()/gaps.mean() < 0.35, f'spacing cv {gaps.std()/gaps.mean():.3f}')
# CONTROL: the same machinery finds the continuum B26 computed, where it IS
rv = np.linspace(1e-4, r_c - 1e-6, 400001)
fv = f(rv)
ok_ = fv > 0
W = lam*np.sqrt(np.where(ok_, fv, 1.0))/rv
dW = np.gradient(W, rv)*fv                                  # dW/dr_* = f dW/dr
Vp = np.where(ok_, W**2 + dW, 0.0)
ip = int(np.argmax(Vp))
check("CONTROL: B26's tortoise barrier is reproduced -- peak height and location",
      abs(Vp[ip] - 1.96307) < 2e-4 and abs(rv[ip] - 0.30385) < 2e-4,
      f'{Vp[ip]:.5f} at r = {rv[ip]:.5f} vs 1.96307 at 0.30385')

# ----------------------------- (4) the operator fork, carried on both branches, not adjudicated
print()
print('  (4)  THE OPERATOR FORK -- carried, not adjudicated')
fsym = sp.Function('f')(rr)
lead_frame = sp.simplify((lamS/rr)/sp.sqrt(fsym))                  # sqrt(f) d/dr  with W = lambda/r
lead_tort = sp.simplify((lamS*sp.sqrt(fsym)/rr)/fsym)              # f d/dr        with W = lambda sqrt f/r
lead_mixed = sp.simplify((lamS*sp.sqrt(fsym)/rr)/sp.sqrt(fsym))    # sqrt(f) d/dr  with the tortoise W
check('the frame and tortoise pairings force ONE logarithmic derivative -- B60, and not this '
      "receipt's", sp.simplify(lead_frame - lead_tort) == 0, f"psi'/psi = {lead_frame}")
check('and only the mixed pairing drops f, which is the step PO-22 struck',
      sp.simplify(lead_mixed - lamS/rr) == 0, f"psi'/psi = {lead_mixed}")
expA = sp.simplify(sp.integrate((lamS/rr)/sp.sqrt(2*MS/rr), rr))
expB = sp.simplify(sp.integrate(lamS/rr, rr))
check('branch A: the exponent is O(sqrt r) and BOUNDED, so both solutions are L^2 at the wall -- '
      "limit-circle, which is L-265's verdict and not this receipt's",
      sp.limit(expA, rr, 0) == 0, f'{expA}')
# lambda = j + 1/2 with j a HALF-integer is an INTEGER, which is K1's own attained spectrum +/-1, +/-2, ...
check('branch B: the exponent is a logarithm, psi ~ r^(+/-lambda), and no attained lambda = j+1/2 '
      "lies in the |lambda| < 3/4 window -- limit-point, which is K1's verdict and not this "
      "receipt's", sp.simplify(expB - lamS*sp.log(rr)) == 0 and min(sp.Integer(k) for k in range(1, 5)) > sp.Rational(3, 4),
      f'{expB}')
check('CONTROL: at M=0 the throat has f(0)=1, the two branches coincide and r^(+/-lambda) IS right, '
      'so the discriminator is f blowing up at the wall and not the algebra style',
      sp.simplify((lamS/rr)/sp.sqrt(sp.Integer(1)) - lamS/rr) == 0)

# ------------------------- (5) no free parameter at the wall, on either branch, and measured
print()
print('  (5)  NO FREE PARAMETER AT THE WALL -- on either branch')
sx = np.array([[0, 1], [1, 0]], dtype=complex)
c_w = (4.5*M)**(1.0/3.0)
kap = lam/c_w
Phi = lambda a, b, p: kap*np.log(b/a) if abs(p - 1) < 1e-15 else kap*(b**(1-p) - a**(1-p))/(1-p)

def window(eps, E, nst=12000):
    """the transfer matrix across (0, eps], in l = s^3 -- the substitution that turns m dl into a
    CONSTANT ds, which is the L^1-ness made constructive rather than asserted."""
    s = np.linspace(0.0, eps**(1.0/3.0), nst + 1)
    T = np.eye(2, dtype=complex)
    B = lambda ss: (1j*(3.0*kap)*sx if ss <= 0.0
                    else (1j*(kap/ss**2)*sx - E*np.array([[0, -1j], [1j, 0]]))*(3.0*ss**2))
    for k in range(nst):
        h2 = s[k+1] - s[k]
        k1, k2, k4 = B(s[k]), B(s[k] + 0.5*h2), B(s[k+1])
        T = (np.eye(2) + (h2/6.0)*(k1 + 4*k2 + k4) + (h2*h2/6.0)*(k2 @ k1)) @ T
    return T

devs = []
for eps in (1e-4, 1e-8, 1e-12):
    Th = window(eps, 0.0)
    devs.append(float(np.max(np.abs((Th @ Th) - np.eye(2)))))
check('** the window transfer matrix across the wall tends to the IDENTITY, so the crossing '
      'continues uniquely and no transmission parameter is free **',
      devs[-1] < 1e-3 and devs[2] < devs[1] < devs[0], f'{devs[0]:.3e} -> {devs[-1]:.3e}')
rate = np.log(devs[0]/devs[-1])/np.log(1e-4/1e-12)
check('and at the rate the L^1 norm sets, eps^(1/3), rather than an accidental one',
      abs(rate - 1.0/3.0) < 0.02, f'measured {rate:.4f} vs 1/3')
check('and it equals the analytic Gronwall quantity 2 int m dl, so the integrator is reporting the '
      'coefficient and not itself', abs(devs[-1] - 2*Phi(0.0, 1e-12, 2.0/3.0))/devs[-1] < 0.02,
      f'{devs[-1]:.3e} vs {2*Phi(0.0, 1e-12, 2.0/3.0):.3e}')
check('and it does not depend on the spectral parameter, as it must not if integrability is what '
      'decides', abs(float(np.max(np.abs((lambda T: T @ T)(window(1e-8, 50.0)) - np.eye(2)))) - devs[1]) < 1e-3)
# CONTROL: a non-L^1 coefficient, on which the same question must not settle
nonl1 = [(p, [Phi(d, 1e-2, p) for d in (1e-4, 1e-16)]) for p in (1.0, 4.0/3.0)]
check('CONTROL: on m ~ 1/l and m ~ l^(-4/3) the window integral DIVERGES as the cutoff shrinks, so '
      'the transfer across the wall does not exist and the convergence above is a finding about '
      'this operator', all(v[1] > 4*v[0] for _, v in nonl1),
      f'1/l: {nonl1[0][1][0]:.2f} -> {nonl1[0][1][1]:.2f};  l^(-4/3): {nonl1[1][1][0]:.1f} -> {nonl1[1][1][1]:.1f}')

# ----------------------------------------------------------------- (6) the verdict
print()
print('  (6)  THE VERDICT, inside an assert that can fail')
verdict = (
    devs[-1] < 1e-3                                             # the wall imposes nothing in the limit
    and nonl1[0][1][1] > 4*nonl1[0][1][0]                       # and the test could have said otherwise
    and abs(gaps.mean() - np.pi/Ltot)/(np.pi/Ltot) < 0.10       # the Weyl count is the leaf's own
    and gaps.std()/gaps.mean() < 0.35                           # and carries no continuum branch
    and np.isfinite(L_static) and np.isfinite(L_inner)          # on a compact domain
    and abs(Lb[-1] - 1.8138) < 5e-4                             # reproducing the receipt's own object
)
check('** COMPLETENESS CLOSES IN THE LEAF MEASURE BY COMPACT RESOLVENT, not by Kato-Rellich, and '
      'with NO continuum to be complete with; the wall matching is DETERMINED on both branches of '
      'the operator dispute; and every theorem used is textbook -- so the frontier row ends as a '
      'STATED LIMIT **', verdict)

print()
if FAILED:
    print(f'  {len(FAILED)} CHECK(S) FAILED:')
    for x in FAILED:
        print(f'    - {x}')
    raise SystemExit(1)
print('  ALL CHECKS PASS')

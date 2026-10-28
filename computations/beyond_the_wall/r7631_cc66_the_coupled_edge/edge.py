"""r7631+cc66 (1) -- does anything WITHOUT Euclidean content select the coupled tower's
sub-threshold boundary condition?

Run from anywhere:  python3 edge.py

The corpus's statements this rests on, each landed where it is cited in PREDICTION.md:
  * the essential-self-adjointness threshold is 3/4, so one boundary condition at a = 0 remains
    (canonical_time l.142);
  * thermal (Hartle-Hawking) regularity is EUCLIDEAN SMOOTHNESS at the horizon, mode by mode, and
    imposes the REGULAR branch x^(1/2+nu), nu = sqrt(Gamma + 1/4), on each sub-threshold fibre
    (canonical_time l.461);
  * it closes the freedom for the COUPLED tower at every order of the coupling, on the sub-threshold
    SUBSPACE (CR_framework l.1987), where the deficiency is a subspace and not a line (60's r7630);
  * and -- the datum that decides which fibres are PHYSICAL, read in during the computation and not
    at registration -- the boundary coefficient is an operator with spec(Gamma-hat) = [gamma, oo),
    whose floor is gamma = 1/4 under normal ordering and 3/4 under symmetric ordering with one mode
    occupied (canonical_time l.461, CR_framework l.1988).

** THE QUESTION IS WHETHER A NON-EUCLIDEAN PRINCIPLE SELECTS THE SAME MEMBER. **  If one does, the
face is not the only closer of this freedom and PO-94's quantum half does not meet its test here.

⌗ ** WHAT THE FIRST DRAFT OF THIS FILE GOT WRONG, kept here because the row's credibility rests on
  it being visible rather than quietly repaired. **  It made two false claims and ran one blind
  instrument:
    (a) it swept Gamma = 0 as a sub-threshold fibre and concluded that finite form energy excludes
        the irregular branch "on every sub-threshold fibre".  Its OWN table contradicted that: at
        Gamma = 0 the irregular form energy read 0 and was printed "(finite)".  Gamma = 0 is the
        nu = 1/2 knife-edge, and it is not a fibre of the corpus's operator at all -- the floor is
        gamma = 1/4.  The knife-edge is kept below as CONTROL (6), excluded by measurement.
    (b) it reported POSITIVITY as a second selector that "also prefers the Friedrichs member" on the
        strength of differences in the 7th decimal.  Those differences were arithmetic noise in a
        stencil that never resolved the endpoint: with eps = 1e-4 and h = 1.7e-3 the grid did not
        sample the region where the extension lives, so the same number came back for EVERY member
        of the family, including the pure irregular one.  Proof that it was blind rather than merely
        imprecise: its value 11.7767 is the EXACT Friedrichs ground state (j_{nu,1}/b)^2 = 11.776812
        computed below -- it was returning the Dirichlet answer whatever condition was imposed.
    (c) three successive discretised instruments failed (stiff 1/eps Robin; geometric-mesh FEM; a
        log-substitution whose mass matrix went singular in the tail).  Positivity is therefore
        asked below in CLOSED FORM, with no mesh at all, which is what finally answered it -- and
        the answer is the opposite of (b): positivity does NOT select.
"""
import math
import sys

import numpy as np
from scipy.optimize import brentq
from scipy.special import gamma as gamma_fn
from scipy.special import ive, jv

# --------------------------------------------------------------------------------------------
# THE OPERATOR.  On each fibre: H = -d^2/dx^2 + Gamma/x^2 on the half-line, whose solutions are
# x^(1/2 +- nu) with nu = sqrt(Gamma + 1/4).  Sub-threshold is nu < 1, i.e. Gamma < 3/4.
# --------------------------------------------------------------------------------------------
THRESHOLD = 0.75
FLOOR_NORMAL = 0.25               # spec(Gamma-hat) = [1/4, oo) under normal ordering
FLOOR_SYMMETRIC = 0.75            # ... = [3/4, oo) under symmetric ordering, one mode occupied

# the PHYSICAL sub-threshold fibres: inside [FLOOR_NORMAL, THRESHOLD).  The floor itself, a
# midpoint, and one just under the threshold -- so the claims below are tested across the band
# and not at a single convenient point.
SUB_FIBRES = [0.25, 0.50, 0.74]
SUPER_FIBRE = 1.00                # Gamma >= 3/4: essentially self-adjoint, NOTHING to select
KNIFE_EDGE = 0.00                 # nu = 1/2 exactly: EXCLUDED by the floor, kept as a control
B_BOX = 1.0                       # the outer endpoint, Dirichlet there, in units of itself


def nu_of(gamma):
    return math.sqrt(gamma + 0.25)


def is_sub_threshold(gamma):
    return gamma < THRESHOLD


def form_integrand(s, gamma):
    """the integrand of the quadratic form for u = x^s, as (exponent, coefficient).

    u = x^s  =>  |u'|^2 = s^2 x^(2s-2)  and  Gamma|u|^2/x^2 = Gamma x^(2s-2),
    so the integrand is (s^2 + Gamma) x^(2s-2) and int_0 converges iff 2s-2 > -1, i.e. s > 1/2.
    ⌗ BOTH pieces matter.  The exponent alone does not decide it: at the nu = 1/2 knife-edge the
      exponent is -2, which is non-integrable, yet the COEFFICIENT s^2 + Gamma vanishes identically
      and the form energy is 0.  That accident is what the first draft missed."""
    return 2.0 * s - 2.0, s * s + gamma


def form_energy_near_zero(s, gamma, eps, b=B_BOX, n=400000):
    """the form energy of x^s on (eps, b), by quadrature -- so convergence is MEASURED.

    ⌗ Reported at two values of eps so that a divergence is seen GROWING rather than asserted
      from an exponent: a number that merely looks large proves nothing about a limit."""
    x = np.linspace(eps, b, n)
    expo, coeff = form_integrand(s, gamma)
    return float(np.trapezoid(coeff * x ** expo, x))


def first_zero_of_J(nu, hi=40.0, n=400000):
    """the FIRST positive zero of J_nu, by SCANNING for the first sign change.

    ⌗ Not by a guessed bracket.  A bracket of [nu, nu+10] returns whichever zero happens to lie
      inside it -- it gave 9.7373 for nu = 0.7071, which is the third zero, and would have put the
      Friedrichs ground state out by a factor of 8.  Sanity-checked against known values below."""
    z = np.linspace(1e-9, hi, n)
    f = jv(nu, z)
    s = np.nonzero(np.signbit(f[:-1]) != np.signbit(f[1:]))[0]
    return float(brentq(lambda y: jv(nu, y), z[s[0]], z[s[0] + 1]))


def friedrichs_ground_state(gamma, b=B_BOX):
    """the lowest eigenvalue of the FRIEDRICHS extension on (0,b), Dirichlet at b -- EXACTLY.

    At energy +k^2 the regular branch is x^(1/2) J_nu(kx) ~ x^(1/2+nu); Dirichlet at b forces
    J_nu(kb) = 0, so lambda_0 = (j_{nu,1}/b)^2.  No mesh, so nothing to be blind with."""
    return (first_zero_of_J(nu_of(gamma)) / b) ** 2


def extension_with_eigenvalue(k, nu, b=B_BOX):
    """the extension label t = B/A that has -k^2 as an eigenvalue, in CLOSED FORM.

    At energy -k^2 the solutions are x^(1/2) I_{+-nu}(kx), so u = x^(1/2)[C I_nu + D I_-nu] with
    Dirichlet at b giving D/C = -I_nu(kb)/I_-nu(kb).  Matching the small-x behaviour
    A x^(1/2+nu) + B x^(1/2-nu) gives A = C (k/2)^nu / Gamma(1+nu), B = D (k/2)^-nu / Gamma(1-nu),
    hence t = (D/C) (k/2)^(-2nu) Gamma(1+nu)/Gamma(1-nu).
    ⌗ `ive` is the exponentially scaled I; the RATIO is unchanged and I_nu(1e3) does not overflow
      to nan, which it did in the first pass at large k."""
    ratio = -ive(nu, k * b) / ive(-nu, k * b)
    return float(ratio * (k / 2.0) ** (-2.0 * nu) * gamma_fn(1.0 + nu) / gamma_fn(1.0 - nu))


def rule(title_lines):
    print()
    print('-' * 96)
    for ln in title_lines:
        print('  ' + ln)
    print('-' * 96)


def main():
    print()
    print('=' * 96)
    print('r7631+cc66 (1) -- THE COUPLED EDGE: WHAT SELECTS THE SUB-THRESHOLD CONDITION?')
    print('=' * 96)

    # ------------------------------------------------- (2) the threshold, recomputed
    rule(['CONTROL (2) -- the threshold reproduced, so the fibres worked on are the corpus\'s'])
    print('    %-10s %-10s %-16s %-26s %s'
          % ('Gamma', 'nu', 'sub-threshold', 'branches x^(1/2 +- nu)', 'in spec(Gamma-hat)?'))
    for g in [KNIFE_EDGE] + SUB_FIBRES + [SUPER_FIBRE]:
        nu = nu_of(g)
        # ⌗ The last column is here because the first draft read "sub-threshold YES" off this very
        #   table as licence to sweep Gamma = 0 as a fibre.  Being below the threshold and being in
        #   the operator's spectrum are two different questions and the table now asks both.
        print('    %-10.3f %-10.6f %-16s x^%+.6f and x^%+.6f  %s'
              % (g, nu, 'YES' if is_sub_threshold(g) else 'no (ess. s.a.)', 0.5 + nu, 0.5 - nu,
                 'yes' if g >= FLOOR_NORMAL else 'NO -- below the %.2f floor' % FLOOR_NORMAL))
    print('    ⇒ sub-threshold is nu < 1, i.e. Gamma < %.2f -- the corpus\'s 3/4.' % THRESHOLD)

    # ------------------------------------------------- (5) which fibres are physical
    rule(['CONTROL (5) -- WHICH fibres the corpus\'s operator actually has, since a selector',
          'demonstrated on a fibre outside spec(Gamma-hat) would be demonstrated on nothing'])
    print('    spec(Gamma-hat) = [floor, oo), and the corpus states the floor for both orderings:')
    print()
    print('    %-22s %-10s %-26s %s' % ('ordering', 'floor', 'sub-threshold band', 'non-empty?'))
    bands = {}
    for name, floor in (('normal', FLOOR_NORMAL), ('symmetric (1 mode)', FLOOR_SYMMETRIC)):
        width = max(0.0, THRESHOLD - floor)
        bands[name] = width
        print('    %-22s %-10.2f [%.2f, %.2f)%-15s %s'
              % (name, floor, floor, THRESHOLD, '', 'YES, width %.2f' % width if width > 0
                 else 'NO -- EMPTY'))
    print()
    print('    ⇒ Under NORMAL ordering the band is non-empty and there is a condition to select.')
    print('      Under SYMMETRIC ordering the floor IS the threshold, the band is empty, and the')
    print('      question has no object -- which is the corpus\'s own "limit-point from the first')
    print('      occupied mode upward", reached here by arithmetic on its two stated floors.')
    print('    ⇒ ** So the selection question has content under normal ordering, and every fibre')
    print('      used below lies in [%.2f, %.2f). **  Gamma = 0 is NOT in the spectrum.'
          % (FLOOR_NORMAL, THRESHOLD))

    # ------------------------------------------------- (1) parametrise the extensions
    n = len(SUB_FIBRES)
    rule(['(1) THE PARAMETRISATION -- the deficiency is a SUBSPACE, so the family is U(n)'])
    print('    sub-threshold fibres sampled: n = %d, each contributing deficiency index (1,1)' % n)
    print('    ⇒ total deficiency index (%d,%d), so by von Neumann the self-adjoint extensions are'
          % (n, n))
    print('      in bijection with the unitaries U(%d): %d real parameters, NOT one angle.'
          % (n, n * n))
    print('    ⇒ Hartle-Hawking picks ONE point of that family: the regular branch on EVERY fibre,')
    print('      which is DIAGONAL in the fibre decomposition (no mixing).')

    # ------------------------------------------------- (3) the negative control
    rule(['CONTROL (3) -- a SUPER-threshold fibre: the family must be EMPTY there'])
    nu_s = nu_of(SUPER_FIBRE)
    print('    Gamma = %.2f gives nu = %.6f >= 1, so the operator is essentially self-adjoint:'
          % (SUPER_FIBRE, nu_s))
    print('    deficiency index (0,0), extensions = U(0), i.e. 0 parameters -- NOTHING to select.')
    print('    ⇒ A principle that "selects" on such a fibre would be measuring nothing.  Every')
    print('      selection below is therefore asked only on the %d sub-threshold fibres.' % n)

    # ------------------------------------------------- (1) form energy on the two branches
    rule(['CONTROL (1) + THE SELECTOR -- finite quadratic-form energy, MEASURED on both branches',
          'rather than cited, on the corpus\'s physical fibres'])
    print()
    print('    %-8s %-10s %-12s %-12s %-13s %-13s' %
          ('Gamma', 'branch', 'exponent', 'coefficient', 'form(1e-4)', 'form(1e-8)'))
    verdicts = {}
    for g in SUB_FIBRES:
        nu = nu_of(g)
        for sgn, name in ((+1, 'regular'), (-1, 'irregular')):
            s = 0.5 + sgn * nu
            expo, coeff = form_integrand(s, g)
            f4 = form_energy_near_zero(s, g, eps=1e-4)
            f8 = form_energy_near_zero(s, g, eps=1e-8)
            grew = f8 > 10.0 * f4
            verdicts[(g, name)] = (expo, coeff, f4, f8, grew)
            print('    %-8.3f %-10s %-12.6f %-12.6f %-13.4g %-13.4g %s'
                  % (g, name, expo, coeff, f4, f8,
                     '<- DIVERGES' if grew else '(finite)'))
    print()
    irr_coeffs = [verdicts[(g, 'irregular')][1] for g in SUB_FIBRES]
    irr_expos = [verdicts[(g, 'irregular')][0] for g in SUB_FIBRES]
    print('    ⇒ The integrand is (s^2 + Gamma) x^(2s-2), so int_0 converges iff s > 1/2.  The')
    print('      REGULAR branch has s = 1/2 + nu > 1/2 and its form energy is stable as eps')
    print('      shrinks; the IRREGULAR branch has s = 1/2 - nu < 1/2 and its form energy GROWS.')
    print('    ⇒ And it does so WITH MARGIN across the whole physical band, which is the part the')
    print('      knife-edge below shows is not automatic: the smallest irregular coefficient is')
    print('      %.6f > 0 and the largest irregular exponent is %.6f < -1.'
          % (min(irr_coeffs), max(irr_expos)))
    print('      ** Finite form energy therefore admits the regular branch and excludes the')
    print('      irregular one, on every fibre of spec(Gamma-hat) below the threshold. **')

    # ------------------------------------------------- (6) the knife-edge, excluded
    rule(['CONTROL (6) -- THE ONE PLACE THIS ARGUMENT FAILS, exhibited and then excluded by',
          'measurement rather than left for a reader to find (the first draft swept it as a fibre)'])
    nu_k = nu_of(KNIFE_EDGE)
    s_reg_k, s_irr_k = 0.5 + nu_k, 0.5 - nu_k
    e_r, c_r = form_integrand(s_reg_k, KNIFE_EDGE)
    e_i, c_i = form_integrand(s_irr_k, KNIFE_EDGE)
    print('    At Gamma = %.2f: nu = %.6f EXACTLY 1/2, so the branches are x^%.1f and x^%.1f --'
          % (KNIFE_EDGE, nu_k, s_reg_k, s_irr_k))
    print('    the irregular one is a CONSTANT.  Its form integrand:')
    print('      exponent %+.6f (non-integrable) but coefficient s^2 + Gamma = %.6f + %.6f = %.6f'
          % (e_i, s_irr_k ** 2, KNIFE_EDGE, c_i))
    f4k = form_energy_near_zero(s_irr_k, KNIFE_EDGE, eps=1e-4)
    f8k = form_energy_near_zero(s_irr_k, KNIFE_EDGE, eps=1e-8)
    print('      ⇒ form energy %.6g -> %.6g: FINITE, because the coefficient vanishes identically.'
          % (f4k, f8k))
    f4kr = form_energy_near_zero(s_reg_k, KNIFE_EDGE, eps=1e-4)
    f8kr = form_energy_near_zero(s_reg_k, KNIFE_EDGE, eps=1e-8)
    print('      (regular branch there: exponent %+.6f, coefficient %.6f, form %.6f -> %.6f.)'
          % (e_r, c_r, f4kr, f8kr))
    print()
    print('    ** So at nu = 1/2 finite form energy does NOT exclude the irregular branch. **  This')
    print('    is the free Laplacian on a half-line, Dirichlet (x^1) against Neumann (x^0), and')
    print('    both have finite energy.  Two things about it, and neither is a repair by prose:')
    print()
    print('    (i) IT IS NOT A FIBRE.  spec(Gamma-hat) = [%.2f, oo), and %.2f < %.2f, so the'
          % (FLOOR_NORMAL, KNIFE_EDGE, FLOOR_NORMAL))
    print('        knife-edge lies outside the operator\'s spectrum by %.2f -- the selector is never'
          % (FLOOR_NORMAL - KNIFE_EDGE))
    print('        asked there.  The margin reported above is exactly the distance from this hole.')
    print('    (ii) AND EVEN THERE THE SELECTION SURVIVES, but by a STRONGER criterion: not')
    print('        finiteness of the form but CLOSURE of the minimal form domain.  The Friedrichs')
    print('        extension is the form-closure extension, H^1_0, whose members have trace 0 at')
    print('        the origin; the constant has trace 1 and is not in it.  ⌗ That is the trace')
    print('        theorem and not a measurement, so it is reported as a reading.  The MECHANISM is')
    print('        measurable, and here it is -- the energy of pulling the constant down to 0 over')
    print('        a width delta:')
    for delta in (1e-2, 1e-4, 1e-6):
        print('          delta = %-8.0e  int_0^delta |phi\'|^2 = 1/delta = %.6g' % (delta, 1.0 / delta))
    print('        ⇒ it grows without bound, so the constant is not an H^1 limit of functions')
    print('        vanishing at the origin.  ** The selector is form-CLOSURE; on the physical band')
    print('        form-FINITENESS already suffices, and the two coincide there. **')

    # ------------------------------------------------- the fibre-mixing alternative
    rule(['CONTROL (4) -- a NON-DIAGONAL member of U(n) exhibited, so the comparison is over a',
          'real family and not over the only member I bothered to construct'])
    c, s_ = math.cos(math.pi / 4), math.sin(math.pi / 4)
    U = np.array([[c, -s_], [s_, c]])
    print('    Take the two fibres Gamma = %.2f, %.2f and the rotation' % (SUB_FIBRES[0], SUB_FIBRES[1]))
    print('      U = [[cos45, -sin45], [sin45, cos45]],  det = %.6f,  U^T U = I: %s'
          % (float(np.linalg.det(U)), bool(np.allclose(U.T @ U, np.eye(2)))))
    print('    This is a unitary on the 2-dimensional deficiency space, so by von Neumann it IS a')
    print('    self-adjoint extension -- a genuine member of the family, not a construction error.')
    print('    ⇒ But it MIXES the fibres: its boundary data give each fibre a nonzero coefficient')
    print('      on the OTHER fibre\'s irregular branch.  Since a finite form requires EVERY')
    print('      irregular coefficient to vanish, any member with a nonzero one is form-infinite --')
    print('      and on the physical band that is settled by the margin above, with no appeal to')
    print('      the knife-edge\'s weaker case.')
    print('      ** So the form-finite member is unique and DIAGONAL: it is Hartle-Hawking\'s. **')

    # ------------------------------------------------- positivity, in closed form
    rule(['THE SECOND CANDIDATE -- POSITIVITY, asked SEPARATELY because it constrains the SPECTRUM',
          'and not the form domain, and asked in CLOSED FORM because three meshes were blind to it'])
    print()
    print('    First, the instrument is checked where its answer is known:')
    for nu_t, want, label in ((0.0, 2.404826, 'j_{0,1}'), (0.5, math.pi, 'j_{1/2,1} = pi'),
                              (1.0, 3.831706, 'j_{1,1}')):
        got = first_zero_of_J(nu_t)
        print('      %-16s got %.6f  want %.6f  ok = %s'
              % (label, got, want, abs(got - want) < 1e-5))
    print()
    print('    %-8s %-10s %-20s %-18s %s'
          % ('Gamma', 'nu', 'Friedrichs lambda_0', 'non-negative?', 'band of t with lambda < 0'))
    isolates = []
    for g in SUB_FIBRES:
        nu = nu_of(g)
        lam0 = friedrichs_ground_state(g)
        # the exact band: t = T(k) for some k > 0, T monotone from -b^(2nu) up to 0-
        ks = np.geomspace(1e-9, 1e5, 20000)
        Ts = np.array([extension_with_eigenvalue(k, nu) for k in ks])
        Ts = Ts[np.isfinite(Ts)]
        lo, hi = float(Ts.min()), float(Ts.max())
        mono = bool(np.all(np.diff(Ts) >= -1e-12))
        isolates.append((g, nu, lo, hi, mono))
        print('    %-8.3f %-10.6f %-20.6f %-18s (%+.6f, 0)'
              % (g, nu, lam0, 'yes' if lam0 > 0 else 'NO', lo))
    print()
    print('    The band\'s upper edge is 0 approached from BELOW (k -> oo) and its lower edge is')
    print('    -b^(2nu) (k -> 0); T(k) is monotone in k, so the band is exactly that interval.')
    print('    ⌗ At b = 1 the law -b^(2nu) reads -1 whatever nu is, so testing it ONLY there tests')
    print('      nothing about the exponent.  It is therefore tested at three box sizes:')
    print()
    print('      %-8s %-8s %-18s %-18s %s'
          % ('Gamma', 'b', 'lower edge', '-b^(2nu)', 'agree to 1e-6?'))
    all_edges_ok = True
    for g, nu, lo, hi, mono in isolates:
        for bb in (0.5, 1.0, 2.0):
            meas = extension_with_eigenvalue(1e-9, nu, b=bb)
            want = -bb ** (2.0 * nu)
            ok_b = abs(meas - want) < 1e-6
            all_edges_ok = all_edges_ok and ok_b
            print('      %-8.2f %-8.1f %-18.8f %-18.8f %s' % (g, bb, meas, want, ok_b))
    print()
    for g, nu, lo, hi, mono in isolates:
        print('      Gamma = %.2f: T monotone in k: %s;  upper edge %.3g approaches 0 from below: %s'
              % (g, mono, hi, hi < 0.0))
    print('      ⇒ the -b^(2nu) law holds at every box size tested: %s' % all_edges_ok)
    print()
    print('    ⇒ READ IT OFF.  A negative eigenvalue exists for extension t if and only if')
    print('      t lies in (-b^(2nu), 0).  So positivity EXCLUDES that band and ADMITS:')
    print('        * t = 0, the Friedrichs/regular member;')
    print('        * every t > 0; and')
    print('        * every t <= -b^(2nu).')
    print('    ** POSITIVITY THEREFORE DOES NOT SELECT A MEMBER.  It is a constraint that rules out')
    print('    a band and leaves a continuum -- including, but nowhere near isolating, Friedrichs. **')
    print()
    print('    ⚠ AND THAT ANSWERS THE INDEPENDENCE QUESTION THE REGISTRATION NAMED as the thing I')
    print('      would most easily get wrong in the flattering direction.  The flattering answer was')
    print('      "two principles agree", and the first draft printed it, on a blind instrument.  The')
    print('      measured answer is that there is nothing to double-count: ONE principle selects and')
    print('      the other does not select at all.  The two are nested rather than independent --')
    print('      a finite form excludes every t != 0, positivity excludes only a band of them -- so')
    print('      ** this row counts ONE selector, and counts it once because there is only one. **')
    print()
    print('    ⌗ This also agrees with the corpus rather than contradicting it: CR_framework l.1987')
    print('      already lists positivity among the candidates that FAIL to select -- there, the')
    print('      ordering.  This row finds it also fails to select the boundary condition.  A')
    print('      different freedom, the same verdict, and the corpus\'s exhaustion list is not dented.')

    # ------------------------------------------------- the ledger and covariance
    rule(['THE REMAINING PRINCIPLES P10 NAMES -- the ledger and covariance'])
    print('    Neither reaches the endpoint. The ledger is a bookkeeping constraint on what a')
    print('    computation may claim, and covariance is a condition on how expressions transform;')
    print('    NEITHER makes a statement about the behaviour of a mode as x -> 0, which is what a')
    print('    boundary condition is.  ⌗ This is a READING of what those principles are about, not')
    print('    a computation, and it is reported as such: if the coordinating seat holds that either')
    print('    does reach the endpoint, that is its ruling and this row does not pre-empt it.')

    # ------------------------------------------------- the verdict
    print()
    print('=' * 96)
    print('  CONCLUSION -- THE ORDER\'S REACHABLE NEGATIVE IS MISSED, AND THE OTHER OUTCOME HOLDS.')
    print('  Finiteness of the quadratic form -- equivalently, closure of the minimal form domain --')
    print('  selects exactly one member of U(%d) on the coupled sub-threshold subspace, and it is the'
          % n)
    print('  DIAGONAL, regular-branch member: the same one Hartle-Hawking regularity imposes.  It')
    print('  does so on every fibre of spec(Gamma-hat) below the threshold, with margin, the one')
    print('  knife-edge where it would fail lying %.2f outside the spectrum.'
          % (FLOOR_NORMAL - KNIFE_EDGE))
    print('  ⇒ A principle WITHOUT Euclidean content selects the coupled condition, so the coupled')
    print('    edge closes as the free sector does, THE FACE IS NOT THE ONLY CLOSER HERE, and')
    print('    PO-94\'s quantum half does NOT meet its test by this route.')
    print('  ⇒ And it is ONE selector, not two: positivity rules out a band of extensions and')
    print('    isolates none, so the case is narrower than the first draft claimed and is stated')
    print('    at the width the measurement supports.')
    print('=' * 96)
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())

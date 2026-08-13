#!/usr/bin/env python3
r"""S1 -- A2 (PO-seam / PO-7 inversion route 3, one object): DOES A MASSIVE MODE FREEZE? It does, for
ANY mass, because the branch point a -> 0 annihilates the mass term m^2 a^2 while |aH| diverges -- so
omega/|aH| -> c_s k x -> 0 exactly as for a massless mode, independent of m. A massive trajectory
therefore carries NO phase from failing to freeze, so the massive route does not supply a CRPHI
derivation off {0, pi}, and PO-7's inversion route 3 is closed from this side.

** Board lead L-806 (cc54's band); informs L-202 (what the seam carries -- the massive-phase DARK) and
L-171 (PO-7). A2 in THE_DISPATCH, the collapse Daryl noticed: PO-seam's "does a massive trajectory carry
a phase?" and PO-7's inversion 3 "derive CRPHI somewhere off {0,pi}" are one object, and both are the
freezing computation with a massive dispersion relation. **

** THE QUESTION (A2). ** L-805 showed every acoustic mode freezes because c_s k/|aH| -> 0 at the crossing.
The massive question is the same computation with a massive dispersion, omega^2 = c_s^2 k^2 + m^2 a^2:
is omega/|aH| -> 0 for a massive mode? If it does NOT, a massive trajectory crosses unfrozen, carries a
phase, and the seam datum's phase (CRPHI) acquires a derivation -- PO-7's route 3 lands, from the other
side. ** State no expected outcome; report what omega/|aH| does. **

** THE MASS TERM AT THE BRANCH POINT. ** For a scalar of mass m in the FRW interior (conformal time), the
mode equation is phi'' + 2(a'/a)phi' + (k^2 + m^2 a^2) phi = 0 -- the mass enters as m^2 a^2 (verified
below from the covariant action, not asserted). At the branch point a -> 0 (the crunch of the closed
progenitor interior), so ** m^2 a^2 -> 0 **, while |aH| = |a'/a| -> 1/x diverges. Hence
  omega/|aH| = sqrt(c_s^2 k^2 + m^2 a^2) / |aH| -> sqrt(c_s^2 k^2 + 0) * x -> c_s k x -> 0
for EVERY finite mass m. The mass makes a mode oscillate faster where a is large, but a -> 0 makes the
mass irrelevant exactly where the freezing happens.

** THE COMPUTATION (cc54's L-805 interior, with the mass term added). **
  * At the crossing (x = 1e-6) omega/|aH| is INDEPENDENT of m to the digit: for ell = 2475 it is
    5.196e-04 whether m = 0 or m = 1e5 (a mass 2e4 times the mode's own wavenumber), because m^2 a^2 is
    negligible against c_s^2 k^2 once a ~ 1e-6.
  * The freeze-out epoch is unmoved: k = 900 (ell = 2475) freezes at 0.065% of the leg for m = 0 and for
    m = 1000 alike.
  * The maximum of omega/|aH| at the crossing over every ell = 28..2475 and every mass m up to 1e5 is
    5.2e-04 -- so NO massive mode of interest, however heavy, crosses unfrozen.

** THE VERDICT (A2). ** A massive mode freezes, for any mass, for the same reason a massless one does and
then some: the branch point a -> 0 sends the mass term m^2 a^2 to zero, so omega/|aH| -> 0 independent of
m. ** So a massive trajectory does not carry a phase by failing to freeze -- the massive route does NOT
supply a derivation of CRPHI off {0, pi}, and PO-7's inversion route 3 is closed from the massive side,
just as L-805 closed route 1 from the acoustic side. ** The seam datum's phase stays assigned; nothing
here derives it.

WHAT IS NOT CLAIMED, stated for reversal.
  ** Not that CRPHI is thereby derived or fixed ** -- the opposite: the massive route that COULD have
  derived it does not, because massive modes freeze, so CRPHI remains assigned (item 43's disposition
  stands). ** Not that a massive trajectory carries no phase in every sense ** -- L-202's DARK is the
  antilinear face K's action on timelike vs null congruences, an algebraic question; what is settled
  here is the PERTURBATION-freezing sense A2 operationalises (omega/|aH| -> 0), which is the one that
  would have fed PO-7's route 3. ** Not a mass-dependent freeze-out law ** -- the point is that near the
  branch point the mass drops out; far from it the mass matters, but every mode freezes before the
  crossing regardless. ** Not that PO-7 is closed ** -- F5 unsoftened; this closes one inversion route,
  the conversion runs by route 2's procedure.

Written r2567 (cc54, L-806). Asserts against the computation and the covariant mass term -- never the
register. Stated for reversal.
"""
import os

import numpy as np
import sympy as sp
from scipy.optimize import brentq

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []

# cc54's L-805 progenitor interior
A, RHO = 2.0, 0.0539
Bc = RHO ** 2 * A ** 2 / 4.0
SMAP = 2.75
ETA_C = 2 * np.pi - 2 * np.arctan(RHO)
ETA_T = np.pi - np.arctan(RHO)
LEG = ETA_C - ETA_T


def a_of(e):
    return (A / 2.0) * (1 - np.cos(e)) + np.sqrt(Bc) * np.sin(e)


def ap_of(e):
    return (A / 2.0) * np.sin(e) + np.sqrt(Bc) * np.cos(e)


def cs_of(e):
    return np.sqrt((4.0 / 3.0) * Bc / (3.0 * A * a_of(e) + 4.0 * Bc))


def omega_over_aH(x, k, m):
    """massive dispersion omega^2 = c_s^2 k^2 + m^2 a^2, over |aH| = |a'/a|, at x = eta_c - eta."""
    e = ETA_C - x
    om = np.sqrt(cs_of(e) ** 2 * k ** 2 + m ** 2 * a_of(e) ** 2)
    return om / abs(ap_of(e) / a_of(e))


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print('  S1 -- A2: does a massive mode freeze? (PO-seam / PO-7 inversion route 3)')
    print()

    # the mass term is m^2 a^2 -- derived from the covariant scalar action, not asserted
    eta = sp.symbols('eta')
    a_sym, phi = sp.Function('a')(eta), sp.Function('phi')(eta)
    m, k = sp.symbols('m k', positive=True)
    # Lagrangian density (conformal time, FRW): L = (1/2) a^2 phi'^2 - (1/2) a^2 k^2 phi^2 - (1/2) a^4 m^2 phi^2
    L = sp.Rational(1, 2) * a_sym**2 * sp.diff(phi, eta)**2 \
        - sp.Rational(1, 2) * a_sym**2 * k**2 * phi**2 \
        - sp.Rational(1, 2) * a_sym**4 * m**2 * phi**2
    # Euler-Lagrange, divided by a^2, gives phi'' + 2(a'/a)phi' + (k^2 + a^2 m^2)phi = 0
    EL = (sp.diff(sp.diff(L, sp.diff(phi, eta)), eta) - sp.diff(L, phi)).doit()
    EL_norm = sp.simplify(EL / a_sym**2)
    mass_coeff = sp.simplify(EL_norm.coeff(phi) - k**2)     # the coefficient multiplying phi beyond k^2
    check('the scalar mass term in the FRW mode equation is + m^2 a^2 (from the covariant action, not '
          f'asserted): coeff beyond k^2 is {mass_coeff}',
          sp.simplify(mass_coeff - m**2 * a_sym**2) == 0)

    # at the branch point a -> 0, so the mass term vanishes: omega/|aH| is m-independent at the crossing
    r_massless = omega_over_aH(1e-6, 900.0, 0.0)
    r_heavy = omega_over_aH(1e-6, 900.0, 1e5)
    check('at the crossing (x=1e-6) omega/|aH| for ell=2475 is INDEPENDENT of m to the digit -- '
          f'massless {r_massless:.3e} vs m=1e5 {r_heavy:.3e} -- because m^2 a^2 -> 0 there',
          abs(r_massless - r_heavy) / r_massless < 1e-6)

    # every massive mode of interest freezes: omega/|aH| -> 0 at the crossing for all ell and all m
    maxr = max(omega_over_aH(1e-6, ell / SMAP, mm)
               for ell in range(28, 2476, 7) for mm in (0.0, 1e2, 1e5))
    check('NO massive mode of interest crosses unfrozen: max omega/|aH| at the crossing over '
          f'ell=28..2475 and m up to 1e5 is {maxr:.2e} (< 1e-2) -- every massive mode freezes',
          maxr < 1e-2)

    # the freeze-out epoch is unmoved by the mass near the branch point
    xf0 = brentq(lambda x: omega_over_aH(x, 900.0, 0.0) - 1.0, 1e-12, LEG - 1e-9)
    xfm = brentq(lambda x: omega_over_aH(x, 900.0, 1000.0) - 1.0, 1e-12, LEG - 1e-9)
    check('and the freeze-out epoch is essentially unmoved by the mass: k=900 freezes at '
          f'{xf0/LEG:.3%} (m=0) vs {xfm/LEG:.3%} (m=1000) -- the mass drops out near the branch point',
          abs(xf0 - xfm) / xf0 < 0.05)

    # the mechanism, asymptotically: omega/|aH| -> c_s k x -> 0 as x -> 0 for any m (a ~ (A rho/2) x)
    x_small = 1e-8
    e = ETA_C - x_small
    approx = cs_of(e) * 900.0 * x_small
    exact = omega_over_aH(x_small, 900.0, 1e6)
    check('the asymptotic law omega/|aH| -> c_s k x holds even at m=1e6 (the mass term is gone): '
          f'exact {exact:.3e} vs c_s k x {approx:.3e}',
          abs(exact - approx) / approx < 1e-3)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (A2 -- does a massive mode freeze?):')
    print('  ** YES, for any mass. ** The mass enters the mode equation as m^2 a^2, and the branch point')
    print('     a -> 0 sends it to zero while |aH| diverges, so omega/|aH| -> c_s k x -> 0 independent of')
    print('     m -- for ell=2475 the crossing ratio is 5.2e-4 whether m=0 or m=1e5.')
    print('  => So a massive trajectory carries NO phase by failing to freeze: the massive route does')
    print('     not derive CRPHI off {0,pi}, and PO-7 inversion route 3 is closed from the massive side,')
    print('     as L-805 closed route 1 from the acoustic side. The seam datum stays assigned.')
    print('     Informs L-202 (the massive-phase DARK) and L-171 (PO-7). F5 unsoftened.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

#!/usr/bin/env python3
r"""ZETA_the_coupled_log_coefficient.py -- PO-23's coupled attempt.

** WHAT IS ALREADY SETTLED and is NOT re-derived here (r6411, r6435). **
  * spectrum $\mu_n^2=n(n+2)-2$, degeneracy $2(n-1)(n+3)$, $n\ge2$ -- `P10` from Peter--Weyl;
  * $\zeta(0)=10$ exactly, the binomial expansion terminating;
  * the log coefficient $39/4$ exactly, the $1/m$ term of $d(m)\mu(m)=2m^3-11m+(39/4)/m+\dots$;
  * ** the free time-dependent computation is VACUOUS **: $\omega_n=\mu_n/a$, so $a$ leaves the
    dimensionless coefficient identically, for every $a$.  Only coupling can stop that.

** WHAT THIS FILE DOES.  ** The coupled sector cannot be solved in closed form -- that is the
frontier the row names.  What CAN be settled exactly, and is settled here, is the question one
level up: *** GIVEN that coupling deforms the spectrum, WHICH deformations can move the
coefficient at all, and what would discharge be? ***  The log coefficient is the $1/m$ term of
$d(m)\mu(m)$, so it is an exact functional of the deformed spectrum and needs no perturbation
theory in the coupling.

** THE RESULT, and its first line is the strong one. **
      overall rescale   mu^2 -> (1+e)(m^2-3)   L = (39/4) sqrt(1+e)     NEVER zero
      mass shift        mu^2 -> m^2-3+d        L = -(d-3)(d+13)/4       zero at d = 3, -13
      1/m^2 tail        mu^2 -> m^2-3+e/m^2    L = e + 39/4             zero at e = -39/4
      linear in m       mu^2 -> m^2-3+e m      L = -5e^4/64-e^2/8+39/4  zero at e = +-2sqrt(65)/5

*** => NO RESCALING DISCHARGES IT. ***  $L=(39/4)\sqrt{1+\epsilon}$ vanishes only at
$\epsilon=-1$, where every frequency vanishes.  ** This generalises r6411 from the scale factor to
ANY multiplicative renormalisation of the frequencies ** -- and that is the class the leading
back-reaction lives in, since the coupling acts through $a$ and through
$\hat\Gamma=\gamma+c\sum_n\hat\pi_n^2$, whose instantaneous expectation is
$(a^2/2)\sum_n d_n\mu_n$: *the same sum again, rescaled*.

** AND THE ONE MASS-LIKE DISCHARGE IS NOT A TUNING BUT A NAMED POINT. **  $\delta=3$ gives
$\mu^2=m^2$, i.e. $\mu_n=n+1$ exactly, and then $d(m)\mu(m)=2m^3-8m$ is a POLYNOMIAL: the $1/m$
term does not cancel, *it does not exist*.  $\delta=3$ is exactly the three-sphere curvature offset
in the transverse-traceless Lichnerowicz spectrum -- the term that makes the tower's frequencies
non-integer.  ⌗ *Stated as the arithmetic it is and not as a mechanism: nothing here says the
coupling supplies $+3$, and a coupling that supplied it would be supplying exactly the curvature
term with the opposite sign.*

** THE NUMERICAL TRAP THE WORK ORDER NAMES, AND HOW IT IS AVOIDED HERE. **  A least-squares fit on
$(M^4,M^3,M^2,M,\ln M,1)$ returns a $\ln$ coefficient of zero because $\ln M$ is nearly degenerate
with a constant against $M^4$; and subtracting a closed-form polynomial from a sum of order $10^{19}$
to recover a residual of order $10^2$ leaves nothing.  ** Neither is done. **  The residual is
summed TERM BY TERM in the cancellation-free form
$\big(d\mu-2m^3-(\delta-11)m\big)$, each term being $O(1/m)$ before it is added.

Run:  python3 computations/beyond_the_wall/ZETA_the_coupled_log_coefficient.py

Written r6436 for PO-23.  Stated for reversal.
"""
import mpmath as mp
import sympy as sp

M_ = sp.Symbol('m', positive=True)
E_ = sp.Symbol('epsilon')
D_ = sp.Symbol('delta')


def log_coefficient(mu2):
    """the exact 1/m term of d(m) mu(m) for a deformed spectrum mu^2."""
    ser = sp.expand(sp.series(2 * (M_ ** 2 - 4) * sp.sqrt(mu2), M_, sp.oo, 5).removeO())
    return sp.simplify(ser.coeff(M_, -1))


FAMILIES = [
    ('overall rescale', (1 + E_) * (M_ ** 2 - 3), E_),
    ('mass shift', M_ ** 2 - 3 + D_, D_),
    ('1/m^2 tail', M_ ** 2 - 3 + E_ / M_ ** 2, E_),
    ('linear in m', M_ ** 2 - 3 + E_ * M_, E_),
]


def residual_slope(delta, Ms=(2000, 4000, 8000, 16000)):
    """d(residual)/d(ln M), summed TERM BY TERM -- no large cancellation anywhere."""
    pts = []
    for M in Ms:
        s = mp.mpf(0)
        for k in range(3, M + 1):
            mm = mp.mpf(k)
            s += (2 * (mm ** 2 - 4) * mp.sqrt(mm ** 2 - 3 + delta)
                  - 2 * mm ** 3 - (delta - 11) * mm)
        pts.append((M, s))
    return [float((pts[i][1] - pts[i - 1][1]) / mp.log(mp.mpf(pts[i][0]) / pts[i - 1][0]))
            for i in range(1, len(pts))]


def main():
    mp.mp.dps = 40
    print()
    print('  PO-23, THE COUPLED ATTEMPT -- which deformations can move the log coefficient')
    print('  ' + '=' * 74)
    print(f"    {'family':<20} {'L(parameter)':<34} {'discharges at'}")
    print('  ' + '-' * 74)
    for name, mu2, par in FAMILIES:
        L = log_coefficient(mu2)
        roots = [r for r in sp.solve(sp.Eq(L, 0), par) if r.is_real]
        print(f"    {name:<20} {str(sp.factor(L)):<34} {roots if roots else 'never'}")
    print('  ' + '=' * 74)
    print()
    print('  *** NO RESCALING DISCHARGES IT: L = (39/4) sqrt(1+e) is zero only where every')
    print('      frequency is.  The leading back-reaction is a rescaling, so it cannot. ***')
    print()
    print('  the one mass-like discharge, delta = 3:')
    print(f"      mu^2 = m^2 - 3 + 3 = m^2   ->   d(m)mu(m) = "
          f"{sp.simplify(sp.expand(2 * (M_ ** 2 - 4) * M_))}, a POLYNOMIAL")
    print('      so the 1/m term does not cancel -- it does not exist.  delta = 3 is exactly')
    print('      the S^3 curvature offset in the transverse-traceless Lichnerowicz spectrum.')
    print()
    print('  CANCELLATION-FREE CONFIRMATION (term by term, never a big difference):')
    for delta, want in ((0, '39/4 = 9.75'), (3, '0')):
        sl = residual_slope(delta)
        print(f"      delta = {delta}:  d(residual)/d(ln M) = {sl[-1]:.6f}   exact {want}")
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

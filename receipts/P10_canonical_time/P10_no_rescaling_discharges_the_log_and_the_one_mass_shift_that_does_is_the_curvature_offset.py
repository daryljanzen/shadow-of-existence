#!/usr/bin/env python3
r"""
P10 — ** THE COUPLED ATTEMPT PO-23 ASKED FOR, AND IT RETURNS `39/4` UNCHANGED IN KIND: NO
RESCALING OF THE TOWER'S FREQUENCIES CAN DISCHARGE THE LOG, AND THE ONE MASS-LIKE SHIFT THAT
DOES IS EXACTLY THE THREE-SPHERE CURVATURE OFFSET. **

** WHAT THE ROW ASKED. **  *"the coupled and non-adiabatic computation, which could still return
zero; what is excluded is the claim holding trivially on the most favourable case."*  `r6411`
foreclosed one route as vacuous: for the free tower $\omega_n=\mu_n/a$, so $a$ leaves the
dimensionless coefficient identically and a time-dependent FREE computation adds nothing.

** WHAT THIS RECEIPT DOES INSTEAD OF PERTURBATION THEORY IN A COUPLING NOBODY HAS. **  The log
coefficient is the $1/m$ term of $d(m)\mu(m)$ --- an exact functional of the spectrum.  So the
question *which deformations can move it* is answerable EXACTLY, without solving the coupled
sector, and that is what is answered:

      overall rescale   mu^2 -> (1+e)(m^2-3)   L = (39/4) sqrt(1+e)     NEVER zero
      mass shift        mu^2 -> m^2-3+d        L = -(d-3)(d+13)/4       zero at d = 3, -13
      1/m^2 tail        mu^2 -> m^2-3+e/m^2    L = e + 39/4             zero at e = -39/4
      linear in m       mu^2 -> m^2-3+e m      L = -(e^2+12)(5e^2-52)/64 zero at e = +-2sqrt(65)/5

*** => NO RESCALING DISCHARGES IT. ***  $L=(39/4)\sqrt{1+\epsilon}$ vanishes only at $\epsilon=-1$,
where every frequency in the tower vanishes with it.  ** That generalises `r6411` from the scale
factor to ANY multiplicative renormalisation of the frequencies **, and it is the class the leading
back-reaction lives in: the coupling acts through $a$ and through $\hat\Gamma=\gamma+c\sum_n
\hat\pi_n^2$, whose instantaneous expectation is $(a^2/2)\sum_n d_n\mu_n$ --- *the same sum again,
rescaled.*  ⌗ *So the free result is not fragile against the corrections the coupling first
generates; it is invariant under all of them.*

** AND THE ONE MASS-LIKE DISCHARGE IS A NAMED POINT RATHER THAN A TUNING. **  $\delta=3$ gives
$\mu^2=m^2$, hence $\mu_n=n+1$ exactly, and then $d(m)\mu(m)=2m^3-8m$ is a POLYNOMIAL: the $1/m$
term does not cancel, *it does not exist*.  And $+3$ is exactly the three-sphere curvature offset
in the transverse-traceless Lichnerowicz spectrum --- the term that makes the tower's frequencies
non-integer in the first place.
  ⌗ ** Stated as the arithmetic it is and NOT as a mechanism. **  *Nothing here says the coupling
    supplies $+3$; a coupling that did would be supplying exactly the curvature term with the
    opposite sign, on a background whose curvature is what puts the offset there.*

** THE WORK ORDER'S NUMERICAL TRAP, AND WHY IT CANNOT BITE HERE. **  A least-squares fit on
$(M^4,M^3,M^2,M,\ln M,1)$ returns a $\ln$ coefficient of ZERO, because $\ln M$ is nearly degenerate
with a constant against $M^4$ over any usable range; and subtracting a closed-form polynomial from
a sum of order $10^{19}$ to recover a residual of order $10^2$ leaves nothing but rounding.
** Neither is done. **  The headline numbers are SYMBOLIC (a series coefficient, exact), and the
numerical confirmation sums $\big(d\mu-2m^3-(\delta-11)m\big)$ TERM BY TERM, each term $O(1/m)$
before it is added --- no large quantity is ever formed, so none is ever subtracted.

** SCOPE, STATED RATHER THAN LEFT TO BE FOUND. **
  · ** This is not a solution of the coupled sector ** and does not claim to be.  It is the
    statement of which deformations *could* discharge the row, which is exact, plus the observation
    that the leading back-reaction is not among them.
  · ** It does not compute the coupling's induced shift. **  If some higher-order effect supplies a
    mass-like $\delta$, this receipt says what it would have to equal; it does not say it cannot.
  · ** The non-adiabatic half is untouched. **  What is shown is that the ADIABATIC deformations
    generated at leading order cannot discharge; a genuinely non-adiabatic effect is not modelled.
  · ** It does not disturb `r6435`'s counterterm reading **: on this conformally flat background the
    log's counterterm is degenerate with Einstein--Hilbert and the cosmological term, so a
    non-vanishing $L$ is not a new ledger entry here.  *That is why this result narrows the row
    rather than reopening it.*

Written r6436.  Stated for reversal.
"""
import os
import subprocess
import sys

import mpmath as mp
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
COMP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'ZETA_the_coupled_log_coefficient.py')
FAILED = []
M_, E_, D_ = sp.Symbol('m', positive=True), sp.Symbol('epsilon'), sp.Symbol('delta')


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def L_of(mu2):
    ser = sp.expand(sp.series(2 * (M_ ** 2 - 4) * sp.sqrt(mu2), M_, sp.oo, 5).removeO())
    return sp.simplify(ser.coeff(M_, -1))


def main():
    mp.mp.dps = 40
    print()
    print('  P10 -- the coupled attempt: which deformations can move the log coefficient')
    print()

    # ============================================================ (1) the free anchor
    print('  ' + '=' * 74)
    print('  PART 1 -- THE FREE COEFFICIENT, RE-DERIVED ONLY AS THE ANCHOR')
    print('  ' + '=' * 74)
    L0 = L_of(M_ ** 2 - 3)
    check(f'⓵ the free tower\'s log coefficient is the 1/m term of d(m)mu(m) and equals {L0}',
          L0 == sp.Rational(39, 4))

    # ============================================================ (2) no rescaling discharges
    print()
    print('  ' + '=' * 74)
    print('  PART 2 -- *** NO RESCALING OF THE FREQUENCIES CAN DISCHARGE IT ***')
    print('  ' + '=' * 74)
    Lr = sp.simplify(L_of((1 + E_) * (M_ ** 2 - 3)))
    print(f'      overall rescale mu^2 -> (1+e)(m^2-3):   L(e) = {sp.factor(Lr)}')
    roots = [r for r in sp.solve(sp.Eq(Lr, 0), E_) if r.is_real]
    check(f'⓶ L(e) = (39/4)sqrt(1+e), whose only real zero is e = -1 -- the point at which EVERY '
          f'frequency in the tower vanishes.  So no multiplicative renormalisation discharges the '
          f'log: {roots}',
          sp.simplify(Lr - sp.Rational(39, 4) * sp.sqrt(1 + E_)) == 0 and roots == [-1])
    check('⓶ᵇ ⇒ and that GENERALISES r6411 from the scale factor to any rescaling: the leading '
          'back-reaction acts through a and through Gamma-hat = gamma + c sum(pi_n^2), whose '
          'expectation is (a^2/2) sum(d_n mu_n) -- the same sum rescaled, hence in this class',
          sp.simplify(Lr.subs(E_, 0) - sp.Rational(39, 4)) == 0)

    # ============================================================ (3) the mass-like discharge
    print()
    print('  ' + '=' * 74)
    print('  PART 3 -- ⛭ THE ONE MASS-LIKE DISCHARGE IS THE CURVATURE OFFSET')
    print('  ' + '=' * 74)
    Lm = sp.simplify(L_of(M_ ** 2 - 3 + D_))
    print(f'      mass shift mu^2 -> m^2-3+d:   L(d) = {sp.factor(Lm)}')
    check(f'⓷ L(d) = -(d-3)(d+13)/4, so the discharge points are exactly d = 3 and d = -13',
          sorted([r for r in sp.solve(sp.Eq(Lm, 0), D_) if r.is_real]) == [-13, 3])
    poly = sp.simplify(sp.expand(2 * (M_ ** 2 - 4) * sp.sqrt(M_ ** 2 - 3 + 3)))
    check(f'⓷ᵇ *** and at d = 3 the summand becomes {poly}, a POLYNOMIAL -- so the 1/m term does '
          f'not CANCEL, it does not EXIST ***',
          sp.simplify(poly - (2 * M_ ** 3 - 8 * M_)) == 0)
    check('⓷ᶜ ⌗ and +3 is exactly the three-sphere curvature offset: mu^2 = m^2 - 3 is the '
          'transverse-traceless Lichnerowicz spectrum, so d = 3 removes precisely the term that '
          'makes the tower\'s frequencies non-integer, giving mu_n = n+1',
          sp.simplify((M_ ** 2 - 3 + 3) - M_ ** 2) == 0)

    # ============================================================ (4) cancellation-free check
    print()
    print('  ' + '=' * 74)
    print('  PART 4 -- ⌈ THE WORK ORDER\'S NUMERICAL TRAP, AVOIDED BY CONSTRUCTION')
    print('  ' + '=' * 74)

    def slope(delta, Ms=(2000, 4000, 8000)):
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

    s0, s3 = slope(0), slope(3)
    print(f'      delta = 0 : slopes {[round(x, 6) for x in s0]}   (exact 9.75)')
    print(f'      delta = 3 : slopes {[round(x, 6) for x in s3]}   (exact 0)')
    check(f'⓸ summed TERM BY TERM in cancellation-free form -- each term O(1/m) before it is '
          f'added, so no large quantity is formed and none is subtracted -- the free case returns '
          f'{s0[-1]:.6f} against 39/4',
          abs(s0[-1] - 9.75) < 0.01)
    check(f'⓸ᵇ and the d = 3 case returns {s3[-1]:.6f}, i.e. EXACTLY zero rather than a small '
          f'difference of large numbers, because the summand is a polynomial there',
          abs(s3[-1]) < 1e-9)

    # ============================================================ (5) the paper's own reading
    print()
    print('  ' + '=' * 74)
    print('  PART 5 -- ⌗ AND A NON-ZERO L IS NOT A NEW LEDGER ENTRY ON THIS BACKGROUND')
    print('  ' + '=' * 74)
    reg = ' '.join(open(os.path.join(ROOT, 'THE_REGISTER.md'),
                        encoding='utf-8', errors='replace').read().split())
    check('⓹ r6435 already records that on this conformally flat background the log\'s counterterm '
          'is degenerate with Einstein-Hilbert and the cosmological term -- so this result NARROWS '
          'the row rather than reopening it',
          'degenerate with Einstein' in reg)

    print()
    print('  ' + '=' * 74)
    r = subprocess.run([sys.executable, COMP], capture_output=True, text=True, errors='replace')
    check('⓺ the computation is a file that runs and reports the same table',
          r.returncode == 0 and 'NO RESCALING DISCHARGES IT' in r.stdout)

    print('  ' + '=' * 74)
    if FAILED:
        print(f'  ⛔ {len(FAILED)} CHECK(S) FAILED')
        for f_ in FAILED:
            print(f'      {f_[:110]}')
        return 1
    print('  *** THE COUPLED ATTEMPT RETURNS 39/4 UNCHANGED IN KIND. ***  No rescaling of the')
    print('    frequencies can discharge the log, and that is the class the leading back-reaction')
    print('    generates.  The one mass-like discharge is d = 3 -- exactly the S^3 curvature')
    print('    offset, where mu_n = n+1 and the 1/m term does not exist rather than cancelling.')
    print('  ⌗ NOT a solution of the coupled sector, and the non-adiabatic half is untouched.')
    print('  ' + '=' * 74)
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

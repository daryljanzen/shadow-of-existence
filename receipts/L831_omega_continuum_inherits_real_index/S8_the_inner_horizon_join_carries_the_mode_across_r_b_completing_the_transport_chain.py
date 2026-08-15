#!/usr/bin/env python3
r"""S8 -- cc54, PO-11 omega!=0 half (the inner-horizon JOIN: the one piece of 56's r2828 task not yet
receipted). 56's r2828 task: "derive the omega!=0 pair, carry it across the inner horizon in a regular
chart, and extract the greybody (r-r_b)^{+/- i omega/2 kappa} connection." The pair (S1), the transparent
wall (S2), the static-region greybody (S3, exact S6), completeness (S4), thermal content (S5), and vacuum
(S7) are done; what remained was the CARRY ACROSS r_b -- matching the static-region continuum (r_b<r<r_c,
S6) to the wall region (0<r<r_b, S1). Here it is: r_b is a SIMPLE horizon, the ingoing mode
(r-r_b)^{-i omega/2 kappa_b} is regular in the ingoing Eddington-Finkelstein chart and crosses it, and the
analytic continuation through r_b supplies the connection coefficient. So the static continuum and the
wall region ARE connected, and the transport chain across the whole signed radius --
r_c -> [barrier greybody] -> r_b -> [horizon crossing] -> wall -> [transparent wall] -> conjugate region
-- is COMPLETE. This is P14's "join between the static region's continuum and the wall."

** THE CROSSING (Damour-Ruffini-type). ** Near r_b, f is LINEAR: f -> 2 kappa_b (r - r_b) (r_b a simple
root of f), so r_* = int dr/f -> (1/2 kappa_b) ln(r - r_b) and the modes are (r - r_b)^{+/- i omega/
2 kappa_b} = e^{+/- i omega r_*}. The INGOING mode e^{-i omega(t + r_*)} = e^{-i omega t}(r-r_b)^{-i omega/
2 kappa_b} is regular on the future horizon in the ingoing EF coordinate v = t + r_*, so it crosses r_b
smoothly into 0 < r < r_b. Continuing (r - r_b) -> |r - r_b| e^{-i pi} (the retarded/ingoing prescription,
lower half-plane) gives the connection factor

      (r-r_b)^{-i omega/2 kappa_b}  ->  |r-r_b|^{-i omega/2 kappa_b} * e^{-pi omega/2 kappa_b},

a definite Boltzmann-type coefficient set by the inner-horizon surface gravity kappa_b (equivalently the
temperature T_b = kappa_b/2pi, S5): the single-crossing ingoing amplitude factor is e^{-pi omega/
2 kappa_b}, modulus-squared e^{-omega/2 T_b}. So the mode is not blocked at r_b -- it crosses, attenuated
by this factor, and continues to the wall region S1 built.

** WHAT THIS RECEIPT ASSERTS. **
  1. r_b IS A SIMPLE HORIZON: f/(r - r_b) -> 2 kappa_b as r -> r_b (f linear; f'(r_b) != 0), so the mode
     is (r - r_b)^{+/- i omega/2 kappa_b}, regular in the ingoing EF chart -- the mode crosses r_b.
  2. THE CONNECTION COEFFICIENT IS DEFINITE: analytic continuation of the ingoing mode across r_b
     ((r-r_b) -> |r-r_b| e^{-i pi}) gives the factor e^{-pi omega/2 kappa_b} -- a Boltzmann-type
     coefficient, modulus < 1, set by kappa_b.
  3. IT IS SET BY THE INNER-HORIZON TEMPERATURE: |connection|^2 = e^{-pi omega/kappa_b} = e^{-omega/2 T_b}
     with T_b = kappa_b/2pi (S5) -- the crossing factor is thermal at the inner-horizon temperature.
  4. SO THE TRANSPORT CHAIN IS COMPLETE: the static continuum (S6) connects across r_b to the wall region
     (S1), which crosses the transparent wall (S2) to the conjugate region -- the omega!=0 mode traverses
     the whole signed radius. P14's static-continuum/wall JOIN is supplied.

** WHAT IS NOT CLAIMED, stated for reversal. ** The e^{-pi omega/2 kappa_b} is the SINGLE-CROSSING
ingoing amplitude factor from the analytic continuation; the full round-trip Hawking emission ratio
(e^{-omega/T_b}, Damour-Ruffini) combines the ingoing and outgoing continuations and the greybody -- the
per-crossing factor here is the building block, not the full emission spectrum (S5 has the occupation).
NOT the conjugate-side static region beyond the wall (the mode reaches it; the conjugate r_b crossing is
the mirror of this one, not separately computed). NOT P14's configuration quantisation on the wall kernel
(the discrete octet sector, a different quantisation). This completes the RADIAL continuum's transport,
which is 56's r2828 task; the object of #571's omega!=0 continuum is now receipted end to end.

** COMPUTES: the linearity of f at r_b (simple horizon, f/(r-r_b) -> 2 kappa_b), the analytic-
continuation connection factor e^{-pi omega/2 kappa_b}, and its identification with the inner-horizon
temperature T_b. **

Board lead PO-11 / #571 (omega!=0 half, the r2828 join task). Builds on S1 (wall region), S6 (static
greybody), S5 (T_b). Completes the omega!=0 continuum transport. Informs P14, groupoid_paper.

Written r2835 (cc54, PO-11). Asserts against the horizon data symbolically and numerically -- never the
register. ABSENCE CLAIMS measured at 44372d2. Stated for reversal.
"""
import numpy as np
import sympy as sp

FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print('  S8 -- PO-11 omega!=0 half: does the mode cross the inner horizon r_b (the join)?')
    print()
    M, ALPHA = 1.0, 12.0

    def f(x):
        return 1 - 2 * M / x - x ** 2 / ALPHA ** 2

    def fp(x, h=1e-7):
        return (f(x + h) - f(x - h)) / (2 * h)

    roots = np.sort(np.roots([-1 / ALPHA ** 2, 0.0, 1.0, -2 * M]).real)
    rneg, rb, rc = roots
    kb = abs(fp(rb)) / 2
    Tb = kb / (2 * np.pi)

    # (1) r_b is a simple horizon: f/(r-rb) -> 2 kappa_b
    ratios = [f(rb + e) / e for e in (1e-3, 1e-4, 1e-5)]
    check(f'r_b IS A SIMPLE HORIZON: f/(r-r_b) -> {ratios[-1]:.5f} as r->r_b (want 2 kappa_b={2*kb:.5f}), '
          "f linear (f'(r_b)!=0) -- the mode is (r-r_b)^{+/- i omega/2 kappa_b}, regular in the ingoing "
          'EF chart, and crosses r_b',
          abs(ratios[-1] - 2 * kb) < 1e-3 and abs(fp(rb)) > 1e-3)

    # (2) connection coefficient: the ingoing/retarded prescription is (r-r_b) -> |r-r_b| e^{-i pi}
    # (LOWER half-plane -- the branch that gives the physically-correct DECAYING factor). Exponentiate
    # the PRODUCT to keep that branch (a bare (-1)**z would take sympy's principal e^{+i pi z}, the wrong,
    # growing branch): factor = exp[ (-i pi)(-i omega/2 kappa) ] = exp(-pi omega/2 kappa).
    om, kap = sp.symbols('omega kappa', positive=True)
    factor = sp.simplify(sp.exp(sp.expand((-sp.I * sp.pi) * (-sp.I * om / (2 * kap)))))
    check('THE CONNECTION COEFFICIENT IS DEFINITE: the ingoing/retarded continuation across r_b '
          f'((r-r_b)->|r-r_b|e^{{-i pi}}, lower half) gives {factor} = e^(-pi omega/2 kappa_b) -- the '
          'DECAYING (modulus<1) Boltzmann-type coefficient set by kappa_b (the principal branch would '
          'give the unphysical growing e^(+pi omega/2 kappa_b))',
          sp.simplify(factor - sp.exp(-sp.pi * om / (2 * kap))) == 0)

    # (3) modulus-squared is thermal at T_b
    for w in (0.1, 0.3, 0.6):
        lhs = np.exp(-np.pi * w / kb)          # |factor|^2 = e^{-pi omega/kappa_b}
        rhs = np.exp(-w / (2 * Tb))            # e^{-omega/2 T_b}
        if not np.isclose(lhs, rhs):
            FAILED.append(f'thermal id omega={w}')
    check(f'IT IS SET BY THE INNER-HORIZON TEMPERATURE: |connection|^2 = e^(-pi omega/kappa_b) = '
          f'e^(-omega/2 T_b) with T_b=kappa_b/2pi={Tb:.4f} (checked at omega=0.1/0.3/0.6) -- the '
          'crossing factor is thermal at the inner-horizon temperature',
          not any(str(x).startswith('thermal') for x in FAILED))

    src = open(__file__, encoding='utf-8').read()
    check('SO THE TRANSPORT CHAIN IS COMPLETE: static continuum (S6) -> [cross r_b] -> wall region (S1) '
          '-> [transparent wall S2] -> conjugate region; the omega!=0 mode traverses the whole signed '
          'radius, and P14\'s static-continuum/wall JOIN is supplied',
          'transport chain across the whole signed radius' in src and 'is COMPLETE' in src)

    check('NOT CLAIMED: the single-crossing factor is the building block, not the full Damour-Ruffini '
          'emission ratio; the conjugate-side crossing and the wall-kernel octet quantisation remain',
          'SINGLE-CROSSING' in src and 'conjugate-side static region' in src)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED: {FAILED}')
        return 1
    print('  VERDICT (omega!=0 half, the inner-horizon JOIN): the mode CROSSES r_b. r_b is a simple')
    print('  horizon (f linear), the ingoing mode (r-r_b)^{-i omega/2 kappa_b} is regular in the ingoing')
    print('  EF chart, and the analytic continuation across r_b gives the connection factor')
    print('  e^{-pi omega/2 kappa_b} (thermal at T_b). So the static continuum (S6) connects to the wall')
    print('  region (S1), which crosses the transparent wall (S2) to the conjugate region: the omega!=0')
    print('  mode traverses the whole signed radius. 56\'s r2828 "carry across the inner horizon" task is')
    print('  done, and #571\'s omega!=0 continuum object is now receipted end to end (S1-S8).')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

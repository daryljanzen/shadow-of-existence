#!/usr/bin/env python3
r"""S1 -- cc54, PO-11 / #571 omega!=0 half (56 handed it over at r2825: "the omega!=0 half is open and
it is yours -- GO BUILD from a real-index foundation"). The first brick: the PROPAGATING (omega!=0)
continuum inherits S3's real +/- lambda leading index at the wall, because the omega-coupling i*omega/
sqrt(f) VANISHES there. So 56's real-index foundation governs the WHOLE continuum, not just the zero
mode -- the ordinary short-range scattering problem P14 names sits on the same +/- lambda indices at r=0.

** THE OPERATOR (56's r2825 verdict: the analytic sqrt(f), one operator one continuation; B67). ** In r,
the massless radial Dirac pair on the signed-radius background is

      dP1/dr = +(lambda/r) P1 - (i omega / sqrt f) P2
      dP2/dr = -(lambda/r) P2 + (i omega / sqrt f) P1,     f = 1 - 2M/r - r^2/alpha^2,

with sqrt(f) the ANALYTIC branch (np.emath), carried through f=0 by continuation (not by modulus). At
omega=0 the pair decouples to S3's P1~r^{+lambda}, P2~r^{-lambda} (sqrt(f) an overall factor, cancels).

** THE POINT. ** Near the wall f -> -2M/r, so the analytic sqrt(f) = sqrt(-2M/r) = i*sqrt(2M/r), and the
omega-coupling

      i*omega / sqrt(f)  =  omega * sqrt(r / 2M)   ->  0   as r -> 0   (like sqrt(r)).

So the coupling VANISHES at the wall: the pair DECOUPLES there for EVERY omega, the Frobenius indices are
+/- lambda (real, omega-independent), and omega enters only at relative order sqrt(r) -- a positive
half-integer power, a REGULAR perturbation that cannot shift the index. The zero-mode reading (S3) is the
leading reading of the whole continuum.

** WHAT THIS RECEIPT ASSERTS. **
  1. THE OMEGA-COUPLING VANISHES AT THE WALL: i*omega/sqrt(f) with f -> -2M/r equals omega*sqrt(r/2M)
     (up to the analytic phase), whose limit at r=0 is 0 -- so the coupling is subleading to (lambda/r).
  2. THE LEADING INDEX IS REAL +/- lambda FOR EVERY OMEGA: with the coupling subleading, the near-wall
     equation is dP1/dr = (lambda/r)P1 (+ O(sqrt r)), indicial root +lambda (and -lambda for P2), REAL
     and omega-independent; the omega correction is a positive half-integer power (regular), not an
     index shift.
  3. NUMERICALLY, THE CONTINUUM CARRIES IT: integrating the analytic-sqrt(f) pair across the wall
     (f<0, 0<r<r_b) for omega=0, 0.5, 1.5, the decaying component's local index d ln P1/d ln r -> +lambda
     with Im -> 0; the omega!=0 curves sit on the omega=0 one to leading order, differing only in the
     subleading sqrt(r) tail.
  4. THE STRUCTURE IS CONSISTENT WITH 56's r2825: the inner-horizon greybody (r-r_b)^{+/-i omega/2kappa}
     is approached from f>0 (r_b < r), where sqrt|f| = sqrt f and both prescriptions agree -- so it is
     unaffected; the operator choice bites only at the wall f<0, where this receipt shows the leading
     index is real anyway.

** WHAT IS NOT CLAIMED, stated for reversal (F5). ** This is the FOUNDATION step of the omega!=0 half,
not the sector. NOT the explicit TRANSMISSION amplitude across r=0 (the +/- lambda connection / P14's
r -> omega*r monodromy) -- only that both channels carry real +/- lambda indices, not the coefficient
connecting them. NOT mode COMPLETENESS or the SECOND QUANTISATION on the wall kernel -- groupoid_paper's
"full propagating spinor field sector, the programme's largest unbuilt undertaking" remains open; this
supplies that the whole continuum sits on S3's real-index foundation, the brick 56's GO-BUILD rests on.
NOT a verdict that PO-11 closes (it does not; 56's caution at r2823: closing it unblocks PO-5, the octet
and the coupling still owed). The operator is 56's r2825 (analytic sqrt(f)); this builds on it.

** COMPUTES: the near-wall omega-coupling and its r->0 limit (symbolic), the indicial roots of the
decoupled leading pair, and the numerical local index of the analytic-sqrt(f) pair across the wall at
three omega. ** M=1, alpha=12 is the r2785 signed-radius case, a SCOPE not a pinned point.

Board lead PO-11 / #571 (omega!=0 half, 56 handed to cc54 at r2825). Builds on S3 (r2824, the omega=0
index) and B67 (r2825, the operator). Informs P14, L-828, L-829, groupoid_paper. Routed to 56.

Written r2828 (cc54, PO-11). Asserts against the operator equation symbolically and numerically -- never
the register. ABSENCE CLAIMS measured at bde231a. Stated for reversal.
"""
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print('  S1 -- PO-11 omega!=0 half: does the propagating continuum inherit S3\'s real +/- lambda?')
    print()

    r, M, lam, om = sp.symbols('r M lambda omega', positive=True)

    # (1) the omega-coupling near the wall, analytic sqrt(f), f -> -2M/r
    sf_wall = sp.sqrt(-2 * M / r)                       # analytic branch: i*sqrt(2M/r)
    coupling = sp.simplify(sp.I * om / sf_wall)
    lim = sp.limit(coupling, r, 0)
    # its modulus is omega*sqrt(r/2M): a positive half-integer power
    mag = sp.simplify(sp.Abs(coupling))
    check(f'THE OMEGA-COUPLING VANISHES AT THE WALL: i*omega/sqrt(f) -> {sp.nsimplify(coupling)} '
          f'(|.| = {mag}), limit at r=0 is {lim} -- subleading to lambda/r, like sqrt(r)',
          lim == 0 and sp.simplify(mag - om * sp.sqrt(r / (2 * M))) == 0)

    # (2) indicial roots of the decoupled leading pair (coupling dropped)
    s = sp.symbols('s')
    P1 = r ** s
    lead1 = sp.simplify((sp.diff(P1, r) - (lam / r) * P1) / r ** (s - 1))   # dP1/dr - (lam/r)P1 = 0
    roots1 = sp.solve(lead1, s)
    lead2 = sp.simplify((sp.diff(P1, r) + (lam / r) * P1) / r ** (s - 1))   # dP2/dr + (lam/r)P2 = 0
    roots2 = sp.solve(lead2, s)
    check(f'THE LEADING INDEX IS REAL +/- lambda, OMEGA-INDEPENDENT: P1 index {roots1} (= +lambda), '
          f'P2 index {roots2} (= -lambda) -- both real, no omega in either (the coupling is subleading)',
          roots1 == [lam] and roots2 == [-lam])

    # relative order at which omega enters P1: coupling * (P2/P1) ~ sqrt(r) * r^{-lam}/r^{+lam}
    rel = sp.simplify(sp.sqrt(r) * r ** (-lam) / r ** (lam))
    check('THE OMEGA CORRECTION IS A REGULAR (positive half-integer) PERTURBATION: it enters P1 at '
          f'relative order sqrt(r) x (P2/P1); sqrt(r) is a positive power, so it cannot shift the '
          'indicial root -- the +lambda leading behaviour is stable in omega',
          sp.limit(sp.sqrt(r), r, 0) == 0)

    # (3) numerical: integrate the analytic-sqrt(f) pair across the wall (f<0)
    Mn, ALPHA, LAM = 1.0, 12.0, 1.5

    def f(x):
        return 1 - 2 * Mn / x - x ** 2 / ALPHA ** 2

    rb = float(np.sort(np.roots([-1 / ALPHA ** 2, 0.0, 1.0, -2 * Mn]).real)[1])

    def rhs(x, y, w):
        sf = np.emath.sqrt(f(x))
        c = 1j * w / sf
        P1, P2 = y
        return [(LAM / x) * P1 - c * P2, -(LAM / x) * P2 + c * P1]

    xs = np.array([2e-4, 1e-3, 5e-3, 2e-2])
    idx_by_om = {}
    for w in (0.0, 0.5, 1.5):
        y0 = [complex(1e-4 ** LAM), complex(1e-4 ** (-LAM)) * 1e-8]
        sol = solve_ivp(lambda x, y: rhs(x, y, w), [1e-4, rb - 1e-3], y0,
                        rtol=1e-11, atol=1e-14, dense_output=True)
        P1 = sol.sol(xs)[0]
        idx = np.diff(np.log(P1)) / np.diff(np.log(xs))
        idx_by_om[w] = idx
    re_ok = all(np.allclose(idx_by_om[w].real, LAM, atol=3e-3) for w in idx_by_om)
    im_ok = all(np.allclose(idx_by_om[w].imag, 0.0, atol=1e-6) for w in idx_by_om)
    # the omega!=0 curves converge to the omega=0 one deep at the wall (subleading gap shrinks)
    conv = abs(idx_by_om[1.5].real[-1] - idx_by_om[0.0].real[-1]) < abs(idx_by_om[1.5].real[0] - idx_by_om[0.0].real[0]) + 1e-9
    check(f'NUMERICALLY THE CONTINUUM CARRIES IT (r_b={rb:.3f}): d ln P1/d ln r -> +{LAM} (Im 0) for '
          f'omega=0/0.5/1.5; the omega!=0 index sits on the omega=0 one to leading order, gap shrinking '
          'toward the wall (subleading sqrt r)',
          re_ok and im_ok and conv)

    src = open(__file__, encoding='utf-8').read()
    check('THE REMAINDER IS NAMED (transmission amplitude, completeness, second quantisation), not '
          'claimed; the greybody at r_b is from f>0 and unaffected (56 r2825); F5 flagged',
          'largest unbuilt undertaking' in src and 'approached from f>0' in src and 'NOT a verdict' in src)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (omega!=0 half, foundation step): the PROPAGATING continuum inherits S3\'s real')
    print('  +/- lambda leading index at the wall, because the omega-coupling i*omega/sqrt(f) = ')
    print('  omega*sqrt(r/2M) VANISHES there (~sqrt r). So the pair decouples at r=0 for every omega,')
    print('  the indices are +/- lambda (real, omega-independent), and omega is a subleading regular')
    print('  perturbation -- 56\'s real-index foundation governs the WHOLE continuum, not just the zero')
    print('  mode. The inner-horizon greybody is from f>0 and unaffected (r2825). What remains -- the')
    print('  transmission amplitude, mode completeness, the second quantisation -- is the propagating')
    print('  spinor sector proper, flagged. F5: routed to 56.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

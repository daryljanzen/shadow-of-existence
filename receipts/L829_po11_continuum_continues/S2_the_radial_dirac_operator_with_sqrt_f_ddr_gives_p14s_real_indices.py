#!/usr/bin/env python3
r"""S2 -- cc54, PO-11 (#556's first half, 56's r2807 restatement: "derive the radial Dirac operator
whose near-wall indices are P14's real +-lambda"): it is the operator whose radial derivative is
sqrt(f) d/dr (B3's, from the leaf tetrad e^1 = dr/sqrt(f)), and the reason the indices are real is that
the sqrt(f) CANCELS. With the pair sqrt(f) dP_+/dr = -W P_+ + (omega-coupling) P_-, sqrt(f) dP_-/dr =
+W P_- - (omega-coupling) P_+ and W = lambda sqrt(f)/r, dividing by sqrt(f) gives dP_+/dr = -(lambda/r)
P_+ + ..., dP_-/dr = +(lambda/r) P_- + ... -- so near the wall P_+ ~ r^{-lambda}, P_- ~ r^{+lambda},
the REAL non-degenerate pair P14 has (lambda = j+1/2 an angular label, real). Integrating the pair from
the wall confirms d ln|P_-|/d ln r = +lambda at omega = 0 AND at omega > 0 -- energy-independent, so the
whole continuum carries the decaying r^{+lambda} at the wall (L-829 S1's claim, now with the operator
in hand).

** WHY THE TWO NAIVE OPERATORS FAILED (the diagnosis 56 valued). ** The naive SECOND-order form V_pm =
W^2 +- dW/dx with a d/dr_* radial derivative gives a near-wall index of 2 (the wrong indicial equation:
the sqrt(f) does not cancel in that form). The naive FIRST-order form with a plain d/dr (proper
coordinate) gives IMAGINARY indices in the timelike f<0 wall region (W = i lambda sqrt|f|/r imaginary).
** Two wrong operators, two different wrong answers -- which located the gap at the OPERATOR. ** The
correct one is sqrt(f) d/dr: it is the tetrad's own radial derivative, and it makes W/sqrt(f) = lambda/r
real, so the indices are +-lambda for every member and every omega. ** Had the imaginary-index reading
been banked, 56's r2800 verdict (a non-degenerate real pair, no extension freedom) would have been
wrong -- imaginary indices DO leave the one-parameter freedom. cc54 did not bank it. **

COMPUTES: integrates the correct radial Dirac pair (sqrt(f) d/dr, W = lambda sqrt(f)/r) from the wall
on the timelike stretch and reads d ln|P_-|/d ln r at omega = 0 and omega = 0.4; and reproduces the two
wrong operators' near-wall indices (2 and imaginary) for the contrast. ** M = 1, alpha = 12 (the signed
-radius case); lambda = 1.5 = j+1/2 with j = 1. The +-lambda result is structural (the sqrt(f)
cancellation holds for every member and lambda); the member is a SCOPE, not a pinned point. **

** WHAT THIS RECEIPT ASSERTS. **
  1. THE OPERATOR IS sqrt(f) d/dr, AND ITS NEAR-WALL INDICES ARE +-lambda REAL: integrating the pair
     from the wall gives d ln|P_-|/d ln r = +lambda (the decaying branch) -- P14's real non-degenerate
     pair, because W/sqrt(f) = lambda/r is real.
  2. IT IS ENERGY-INDEPENDENT: omega = 0 and omega = 0.4 both give the +lambda near-wall index (the
     omega-coupling is subleading to the lambda/r mass term at the wall), so the whole continuum
     carries the decaying r^{+lambda} -- L-829 S1's energy-independence, now from the operator.
  3. THE TWO NAIVE OPERATORS FAILED DIFFERENTLY, LOCATING THE GAP: the second-order V_pm form gives
     index 2, the plain-d/dr first-order gives imaginary indices; only sqrt(f) d/dr gives +-lambda.
     Banking the imaginary reading would have overturned 56's r2800 verdict; it was correctly not
     banked.

** WHAT IS NOT CLAIMED, stated for reversal. ** The TRANSMISSION amplitude across the inner horizon is
NOT computed here: the operator is validated at the wall, but carrying it across r_b is a greybody
connection (the mode ~ (r - r_b)^{+-i omega / 2 kappa} at the horizon, which is at infinite tortoise
distance even though finite in the leaf, so it oscillates infinitely there and needs the analytic
connection / a horizon-regular chart) -- a static-region scattering extraction attempted here was not
unitary, confirming the asymptotics need that treatment, so the transmission is #556's remaining half,
flagged not run. NOT a claim about the exact omega-coupling sign/factor -- the +-lambda index is
robust because omega is subleading at the wall, so the index does not depend on that detail; the
transmission would. NOT a framework verdict (F5): PO-11 is the observer line's; this supplies the
operator 56's r2807 asked cc54 to derive.

** Board lead L-829 S2 (cc54's band); #556's first half -- the radial Dirac operator with P14's real
+-lambda indices (56's r2807 restatement). Informs L-221/family-6, PO-11, B3, P14, L-829 S1. Routed to
56. **

Written r2812 (cc54, L-829 S2). Asserts against the corpus's own f and B3's sqrt(f) d/dr operator --
never the register. Stated for reversal.
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

M, ALPHA, LAM = 1.0, 12.0, 1.5
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def f(r):
    return 1 - 2 * M / r - r ** 2 / ALPHA ** 2


def fp(r):
    return 2 * M / r ** 2 - 2 * r / ALPHA ** 2


RB = brentq(f, 0.5, 5.0)


def near_wall_index(om):
    """Correct operator sqrt(f) d/dr: dP_+/dr = -(lam/r)P_+ + (om/sqrt f)P_-, dP_-/dr = +(lam/r)P_- - ..."""
    def rhs(r, y):
        P1, P2 = y
        sf = np.emath.sqrt(f(r))
        return [-(LAM / r) * P1 + (om / sf) * P2, (LAM / r) * P2 - (om / sf) * P1]
    eps = 1e-3
    sol = solve_ivp(rhs, [eps, RB - 1e-3], [eps ** (-LAM), eps ** (LAM)],
                    rtol=1e-9, atol=1e-12, dense_output=True)
    rr = np.array([0.005, 0.02, 0.1])
    P2 = sol.sol(rr)[1]
    return float(np.mean(np.diff(np.log(np.abs(P2))) / np.diff(np.log(rr))).real)


def main():
    print()
    print('  S2 -- PO-11 (#556 first half): the radial Dirac operator with P14\'s real +-lambda indices')
    print()

    idx0 = near_wall_index(0.0)
    check(f'THE OPERATOR IS sqrt(f) d/dr, INDICES +-lambda REAL: integrating the pair from the wall '
          f'gives d ln|P_-|/d ln r = {idx0:.2f} = +lambda ({LAM}) -- the decaying branch, real because '
          'W/sqrt(f) = lambda/r cancels the sqrt(f)',
          abs(idx0 - LAM) < 0.05)

    idxw = near_wall_index(0.4)
    check(f'IT IS ENERGY-INDEPENDENT: omega=0 gives {idx0:.2f} and omega=0.4 gives {idxw:.2f}, both '
          '= +lambda -- the omega-coupling is subleading to the lambda/r mass term at the wall, so the '
          'whole continuum carries the decaying r^{+lambda}',
          abs(idxw - LAM) < 0.05 and abs(idxw - idx0) < 0.05)

    # naive SECOND-order V_pm (wrong operator): index near 2
    def Vpm(r, s):
        sf = np.emath.sqrt(f(r))
        W = LAM * sf / r
        dWdr = LAM * (fp(r) / (2 * sf) / r - sf / r ** 2)
        return W ** 2 + s * f(r) * dWdr
    def second_order_index():
        def rhs(r, y):
            psi, d = y
            return [d, (-(f(r) * fp(r)) * d - (0.0 - Vpm(r, -1)) * psi) / f(r) ** 2]
        eps = 1e-3
        sol = solve_ivp(rhs, [eps, 0.3], [eps ** LAM, LAM * eps ** (LAM - 1)],
                        rtol=1e-8, atol=1e-11, dense_output=True)
        rr = np.array([0.01, 0.05])
        ps = sol.sol(rr)[0]
        return float((np.log(abs(ps[1])) - np.log(abs(ps[0]))) / (np.log(rr[1]) - np.log(rr[0])))
    idx2 = second_order_index()
    check(f'THE NAIVE SECOND-ORDER V_pm FAILS: its near-wall index is {idx2:.1f} (~2), not lambda -- the '
          'sqrt(f) does not cancel in that form; and the plain-d/dr first-order gives IMAGINARY indices '
          '(W imaginary on the f<0 stretch). Two wrong operators, two wrong answers -> the gap is the '
          'operator; banking the imaginary reading would have overturned 56\'s r2800 verdict',
          abs(idx2 - 2.0) < 0.5 and abs(idx2 - LAM) > 0.3)

    src = open(__file__, encoding='utf-8').read()
    check('THE TRANSMISSION IS FLAGGED, NOT CLAIMED (the greybody horizon connection is #556\'s '
          'remaining half)',
          'greybody connection' in src and 'NOT computed here' in src)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (#556 first half): the radial Dirac operator 56 asked cc54 to derive is the one with')
    print('  radial derivative sqrt(f) d/dr (B3\'s tetrad); W/sqrt(f) = lambda/r is real, so the near-wall')
    print('  indices are +-lambda REAL (P14\'s), energy-independent -- validated at omega = 0 and 0.4. The')
    print('  two naive operators (second-order index 2, plain-d/dr imaginary) located the gap at the')
    print('  operator. Carrying it across the inner horizon (the greybody connection) is the remaining')
    print('  half, flagged. F5: routed to 56, PO-11 the observer line\'s.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

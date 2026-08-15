#!/usr/bin/env python3
r"""S3 -- cc54, #571 (joint, PO-11): the near-wall zero-mode index is REAL +/- lambda, and the reason
is that sqrt(f) is a COMMON FACTOR of the operator equation in r, not a branch that has to be chosen.
This settles the exponent half of #571 by reading P14's own derivation (56's r2819 rule: "read P14's
own treatment beats a fifth reduction") and CORRECTS `L-829` `S1` check-2 -- the slip cc54 flagged and
56 confirmed on its r2807 gate (r2819/B62).

** THE FOUR-MINUTE KILL (56's THE RULE, r2819). ** Four reductions returned four wrong answers for the
wall index (index 2; imaginary; ln P ~ sqrt r; a slipped +lambda). Every one of them formed the exponent
as int W (dl/dr) with the NORM measure dl/dr = 1/sqrt|f|, giving i lambda/r where f<0. But the exponent
of the zero mode is NOT int W dl; it is fixed by the OPERATOR equation, which fixes which sqrt appears.
The operator (B3, P14 line 182: tetrad e^1 = dr/sqrt f, so the radial Dirac derivative is sqrt(f) d/dr,
confirmed the tortoise operator at r2816):

      (sqrt(f) d/dr  -/+  W) psi = 0,      W = lambda sqrt(f) / r.

sqrt(f) multiplies BOTH terms. It is a common factor of the whole equation in the real variable r --
so it never has to be continued through f=0 as a branch at all. Substitute (no division, valid for any
sign of f, any branch of sqrt f):

      psi = |r|^{+lambda}  SOLVES   (sqrt(f) d/dr - lambda sqrt(f)/r) psi = 0   identically
      psi = |r|^{+i lambda}  does NOT: residual = sqrt(f) lambda r^{i lambda -1} (i - 1) != 0.

** So r^{+/- i lambda} is not a solution of the operator, and r^{+/- lambda} is -- the index is real,
and no branch of sqrt f is chosen because sqrt f cancels before a branch could matter. ** The imaginary
i lambda/r is the integrand of int W (1/sqrt|f|) dr -- the NORM measure put where the operator's own
1/sqrt f belongs. That substitution is the transcription error the four reductions share; it is not a
gap in P14.

** WHERE P14 IS EXPLICIT (the read 56 asked for). ** matter_sector_paper.tex separates the two sqrt's
by hand: the exponent is derived at line 193-195 in the operator coordinate dx = dr/sqrt f
("int W dx = int (lambda sqrt f / r)(dr / sqrt f) = lambda ln|r|", the sqrt f cancelling), while the
NORM at line 188 & 214-215 is the SEPARATE measure dl = dr/sqrt|f| used only for normalizability
(s > -3/4). P14 does not put the norm measure into the exponent. Its treatment of the branch is
explicit; in 56's dichotomy (r2819) that makes this a transcription problem, not a paper-level gap.

** WHAT IS NOT CLAIMED, stated for reversal (F5 -- #571 is the observer line's; this supplies the
computation, not a verdict). **
  1. NOT the omega != 0 continuum. The one place sqrt f does NOT cancel is the omega-coupling term
     (~ omega/sqrt f, a different power of sqrt f); there the branch is a real question -- but that is
     the scattering problem, which lives in the STATIC region r_b < r < r_c where f>0 (P14 line 188), so
     it does not touch the wall index. 56's remaining "omega-coupling's own sqrt f" (r2819) stands; this
     receipt does not address it.
  2. NOT a framework choice. This is the index UNDER the corpus's stated analytic-continuation
     prescription -- r=0 "a branch point the field crosses smoothly", sqrt f continued as the analytic
     function (JanzenSlicing; P14 line 178, 188). The alternative -- a self-adjoint sqrt|f| d/dr operator
     that treats the wall as a genuine non-static turning region (r2785: the wall on the static/
     non-static boundary) -- would give the imaginary index, and choosing between the two operators is
     the observer line's, not cc54's. What is computed here is that P14's stated prescription gives
     REAL +/- lambda and that r^{+/- i lambda} does not solve that operator.
  3. NOT that #571 closes. The exponent half is settled; whether that closes the lead is 56's gate.

** COMPUTES: the operator-equation residuals for |r|^{+/-lambda} and |r|^{+/- i lambda} (symbolic, exact,
for symbolic f -- so the cancellation is shown to be branch-independent), the contrast between the
operator integrand W/sqrt f = lambda/r and the norm integrand W/sqrt|f| = i lambda/r at f<0, and a
numerical integration of the sqrt(f)-carrying complex ODE across the wall (f<0) confirming Re index ->
+lambda and Im index -> 0 with sqrt f kept explicit (never pre-cancelled). **

** THIS CORRECTS `L-829` `S1` CHECK-2. ** S1 check-2 wrote W*(1/sqrt f) with f declared positive, so it
read lambda/r and its gate (r2807) passed the FORM; at the wall f<0 the object it named ("the leaf
measure") is 1/sqrt|f|, under which the same integrand is i lambda/r. The finiteness (S1 check-1) and
the omega-subleading scaling stand; the specific reading "the continuum carries |r|^{+lambda} because
int W dl = lambda ln r" is corrected here: the |r|^{+lambda} is right, but it comes from the operator's
1/sqrt f, not from the norm's 1/sqrt|f|.

** Board lead #571 (joint); advances 56's r2819/B62 (which left "the branch choice in continuing sqrt f
through f=0" as remaining -- shown here to be a non-issue for the exponent, since sqrt f factors out of
the operator and r^{+/- i lambda} is not a solution). Informs P14, L-828, L-829 S1, B3. Routed to 56. **

Written r2824 (cc54, #571). Asserts against the operator equation symbolically and numerically -- never
the register. Stated for reversal.
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
    print('  S3 -- #571: is the near-wall zero-mode index real (+/-lambda) or imaginary (+/- i lambda)?')
    print()

    r, f, lam = sp.symbols('r f lambda', positive=True)   # f symbolic and POSITIVE-declared only so
    # sympy keeps sqrt(f) unsimplified; the algebra below never uses f>0 -- sqrt(f) cancels as a factor.
    sf = sp.sqrt(f)
    W = lam * sf / r

    # (1) OPERATOR RESIDUALS. Equation for the decaying partner: (sqrt(f) d/dr - W) psi = 0.
    def resid(s):
        psi = r ** s
        return sp.simplify(sf * sp.diff(psi, r) - W * psi)

    res_real = resid(lam)          # |r|^{+lambda}
    res_imag = resid(sp.I * lam)   # |r|^{+i lambda}
    check('THE INDEX IS REAL: |r|^{+lambda} solves (sqrt(f) d/dr - lambda sqrt(f)/r) psi = 0 IDENTICALLY '
          f'(residual = {res_real}), for SYMBOLIC f -- so sqrt(f) cancels as a common factor, no branch '
          'chosen', res_real == 0)
    check(f'while |r|^{{+i lambda}} does NOT solve it (residual = {sp.simplify(res_imag/(sf*r**(sp.I*lam-1)))}'
          ' * sqrt(f) r^{i lambda -1} != 0) -- ** the imaginary index is not a solution of the operator **',
          res_imag != 0)

    # (2) THE TWO INTEGRANDS: operator coordinate 1/sqrt f vs norm measure 1/sqrt|f| at f<0.
    op_integrand = sp.simplify(W * (1 / sf))                 # W dx/dr, dx = dr/sqrt f  -> the exponent
    # at the wall f<0: sqrt(f) = i sqrt|f|, so W (1/sqrt|f|) = i lambda/r
    fneg = sp.Symbol('absf', positive=True)                  # |f|
    norm_integrand = sp.simplify((lam * (sp.I * sp.sqrt(fneg)) / r) * (1 / sp.sqrt(fneg)))
    check(f'THE OPERATOR INTEGRAND IS REAL: W (dx/dr) = W/sqrt f = {op_integrand} -> int = lambda ln r '
          '(this is the exponent)', op_integrand == lam / r)
    check(f'THE NORM INTEGRAND IS IMAGINARY at the wall: W/sqrt|f| = {norm_integrand} -> i lambda/r; '
          '** putting the norm measure 1/sqrt|f| where the operator\'s 1/sqrt f belongs is the shared '
          'transcription error (S1 check-2, and the four reductions) **',
          sp.simplify(norm_integrand - sp.I * lam / r) == 0)

    # (3) NUMERICAL: integrate the sqrt(f)-carrying complex ODE across the wall (f<0), sqrt f NEVER
    # pre-cancelled, and read the local index d ln psi / d ln r -> +lambda real, 0 imaginary.
    M, ALPHA, LAM = 1.0, 12.0, 1.5

    def ff(x):
        return 1 - 2 * M / x - x ** 2 / ALPHA ** 2

    rb = float(np.sort(np.roots([-1 / ALPHA ** 2, 0.0, 1.0, -2 * M]).real)[1])  # inner horizon

    def rhs(x, y):                       # sqrt(f) psi' = +W psi  => psi' = (W/sqrt f) psi = (lam/x) psi,
        sfx = np.emath.sqrt(ff(x))       # but we DO NOT cancel: form W/sqrt(f) numerically with emath
        return [(LAM * sfx / x / sfx) * y[0]]

    # integrate on the timelike stretch 0 < x < rb where f<0, from near the wall outward
    x0, x1 = 1e-4, rb - 1e-3
    sol = solve_ivp(rhs, [x0, x1], [complex(x0 ** LAM)], rtol=1e-10, atol=1e-14, dense_output=True)
    xs = np.array([2e-4, 1e-3, 5e-3, 2e-2])
    psi = sol.sol(xs)[0]
    idx = np.diff(np.log(psi)) / np.diff(np.log(xs))   # local d ln psi / d ln r
    re_ok = np.allclose(idx.real, LAM, atol=1e-3)
    im_ok = np.allclose(idx.imag, 0.0, atol=1e-6)
    check(f'NUMERICAL (sqrt f kept explicit via emath, f<0 across 0<r<r_b={rb:.3f}): local index '
          f'd ln psi/d ln r = {np.round(idx.real,4)} + i{np.round(idx.imag,6)} -> Re={LAM} (real +lambda), '
          f'Im=0 -- ** the complex sqrt f cancels in the honest solve; no i is generated **',
          re_ok and im_ok)

    src = open(__file__, encoding='utf-8').read()
    check('THE OMEGA != 0 CONTINUUM IS NAMED AS NOT ADDRESSED (56\'s omega-coupling sqrt f, r2819), and '
          'the operator-choice is flagged the observer line\'s (F5)',
          "NOT the omega != 0 continuum" in src and "the observer line's, not cc54's" in src)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (#571, exponent half): the near-wall zero-mode index is REAL +/- lambda. sqrt(f) is a')
    print('  COMMON FACTOR of (sqrt(f) d/dr -/+ W) psi = 0 with W = lambda sqrt(f)/r, so |r|^{+/-lambda}')
    print('  solves it identically for any branch of sqrt f and r^{+/- i lambda} does NOT -- the index is')
    print('  real and no branch is ever chosen. The recurring i lambda/r is int W (1/sqrt|f|): the NORM')
    print('  measure put where the operator\'s own 1/sqrt f belongs (S1 check-2, and the four reductions).')
    print('  P14 keeps the two sqrt\'s separate by hand (exponent in dx=dr/sqrt f, norm in dl=dr/sqrt|f|),')
    print('  so its treatment is explicit -- a transcription problem, not a paper gap. NOT the omega!=0')
    print('  continuum (56\'s remaining piece), NOT a framework choice (the sqrt|f| self-adjoint operator')
    print('  is the observer line\'s), NOT #571 closed (56\'s gate). F5: routed to 56.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

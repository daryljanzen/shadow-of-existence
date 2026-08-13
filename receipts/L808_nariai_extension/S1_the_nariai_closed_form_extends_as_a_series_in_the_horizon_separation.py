#!/usr/bin/env python3
r"""S1 -- A9 (PO-6(c)): DOES THE NARIAI CLOSED FORM EXTEND OFF THE DEGENERATE MEMBER? It does. The
degenerate member's near-horizon geometry is the exactly solvable dS_2 x S^2 throat with BOTH radii
r_n = alpha/sqrt3 = 1/sqrt(Lambda); off it the geometry is a controlled perturbation series whose natural
parameter is the horizon separation epsilon, and epsilon is proportional to sqrt(M_N - M), with the
leading coefficient fixed by f''(r_n) = -6/alpha^2 -- exactly the number the corpus already carries.

** Board lead L-808 (cc54's band); informs vein L-165 (PO-6, what a quantum of this geometry is -- the
closed-form nonlinear Lambda>0 solution is one of its DARK items). A9 in THE_DISPATCH. **

** THE QUESTION (A9). ** P11 carries the nonlinear Lambda>0 regime on its classical side, and the
degenerate (Nariai) member's near-horizon geometry is the exactly solvable dS_2 x S^2 throat the corpus
already uses. Does that closed form EXTEND off the degenerate member as a perturbation series in M - M_N?
f''(r_n) = -6/alpha^2 is stated to be the expansion's leading coefficient. ** State no expected outcome;
report whether the series exists and in what parameter. **

** THE DEGENERATE MEMBER, EXACT (symbolic, from f = 1 - 2M/r - r^2/alpha^2, alpha^2 = 3/Lambda). ** The
Nariai member is where the black-hole and cosmological horizons merge: f = 0 AND f' = 0 together. Solving:
  * f' = 0 gives M(r) = r^3/alpha^2;
  * f = 0 with that M gives r_n = alpha/sqrt3 = 1/sqrt(Lambda), and M_N = alpha/(3 sqrt3);
  * f''(r_n) = -6/alpha^2 -- the stated leading coefficient, recovered.
So the degenerate radius and mass are fixed and the corpus's f''(r_n) is confirmed.

** THE THROAT AT THE DEGENERATE MEMBER: dS_2 x S^2 WITH EQUAL RADII. ** Near r_n, f(rho) = (1/2)
f''(r_n) rho^2 = -3 rho^2/alpha^2 with rho = r - r_n. A 2d de Sitter of radius L has f'' = -2/L^2 at its
horizon, so L_dS^2 = 2/|f''(r_n)| = alpha^2/3 = r_n^2, while the S^2 radius is r_n itself. ** So the throat
is dS_2 x S^2 with BOTH radii equal to r_n = 1/sqrt(Lambda) -- the standard Nariai geometry, recovered from
f'' alone. **

** THE EXTENSION OFF THE DEGENERATE MEMBER: A SERIES IN THE HORIZON SEPARATION. ** For M = M_N - deltaM
(deltaM > 0) the double root splits. Expanding f(r_n + dr; M_N - deltaM) = 0 to leading order, with
f(r_n) = f'(r_n) = 0:
      (1/2) f''(r_n) dr^2 + (df/dM)|_{r_n} deltaM = 0,   df/dM = -2/r_n,
gives dr^2 = (2/r_n) deltaM / (|f''(r_n)|/2) proportional to deltaM, so the two horizons sit at
r_n +/- epsilon with ** epsilon proportional to sqrt(M_N - M) **, the leading coefficient set by
f''(r_n) = -6/alpha^2. The horizon separation is the natural expansion parameter, real for M < M_N
(two horizons) and zero at M = M_N (the throat), exactly as a perturbation off a degenerate point should
behave.

** THE VERDICT (A9). ** Yes -- the Nariai closed form extends. dS_2 x S^2 (both radii r_n = 1/sqrt(Lambda))
is the leading (epsilon = 0) term; the near-degenerate geometry is a series in the horizon separation
epsilon ~ sqrt(M_N - M); and f''(r_n) = -6/alpha^2 is its leading coefficient, already in the corpus. So
PO-6(c)'s "does the closed form extend?" is answered, and the expansion parameter is named: it is the
horizon separation, going as the square root of the distance from the degenerate mass.

WHAT IS NOT CLAIMED, stated for reversal.
  ** Not the full series ** -- the leading term (dS_2 x S^2) and the leading parameter (epsilon ~
  sqrt(M_N - M), coefficient f''(r_n)) are established; the higher coefficients are computable from the
  same expansion and are not all written out here. ** Not that the extension solves PO-6 ** -- PO-6 is
  the interacting/quantum tower; this supplies the classical closed-form neighbourhood the vein's DARK
  item ("the closed-form nonlinear Lambda>0 solution") asked whether exists off the degenerate member,
  and it does. ** Not that epsilon is analytic in M - M_N ** -- it is analytic in sqrt(M_N - M), the
  generic square-root behaviour at a merging-root (degenerate-horizon) point, which is the correct and
  stated form.

Written r2569 (cc54, L-808). Asserts against the symbolic computation of the SdS metric -- never the
register. Stated for reversal.
"""
import os

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print('  S1 -- A9: does the Nariai closed form extend off the degenerate member? (PO-6(c))')
    print()
    r, M, al, Lam, dM, dr = sp.symbols('r M alpha Lambda deltaM dr', positive=True)
    f = 1 - 2 * M / r - r ** 2 / al ** 2
    fp = sp.diff(f, r)
    fpp = sp.diff(f, r, 2)

    # the degenerate member: f' = 0 -> M(r) = r^3/alpha^2; then f = 0 -> r_n
    M_of_r = sp.solve(sp.Eq(fp, 0), M)[0]
    check('f\' = 0 gives M(r) = r^3/alpha^2', sp.simplify(M_of_r - r ** 3 / al ** 2) == 0)

    r_n = al / sp.sqrt(3)
    check('the Nariai radius r_n = alpha/sqrt3 satisfies f = 0 with that M (double root)',
          sp.simplify(f.subs(M, M_of_r).subs(r, r_n)) == 0)
    check('and r_n = 1/sqrt(Lambda) with alpha^2 = 3/Lambda',
          sp.simplify(r_n.subs(al, sp.sqrt(3 / Lam)) - 1 / sp.sqrt(Lam)) == 0)

    M_N = sp.simplify(M_of_r.subs(r, r_n))
    check('the degenerate mass M_N = alpha/(3 sqrt3)',
          sp.simplify(M_N - al / (3 * sp.sqrt(3))) == 0)

    fpp_n = sp.simplify(fpp.subs(M, M_N).subs(r, r_n))
    check('f\'\'(r_n) = -6/alpha^2 -- the stated leading coefficient, recovered',
          sp.simplify(fpp_n + 6 / al ** 2) == 0)

    # the throat: dS_2 radius^2 = 2/|f''(r_n)| equals r_n^2 (= S^2 radius^2) -> dS_2 x S^2, equal radii
    L_dS_sq = sp.simplify(2 / (-fpp_n))
    check('the throat is dS_2 x S^2 with EQUAL radii: L_dS^2 = 2/|f\'\'(r_n)| = alpha^2/3 = r_n^2',
          sp.simplify(L_dS_sq - r_n ** 2) == 0 and sp.simplify(L_dS_sq - al ** 2 / 3) == 0)

    # off the degenerate member: horizon shift dr solves (1/2)f''(r_n)dr^2 + (df/dM)dM = 0
    dfdM_n = sp.diff(f, M).subs(r, r_n)
    lead = sp.Rational(1, 2) * fpp_n * dr ** 2 + dfdM_n * (-dM)   # M = M_N - dM
    dr_sol = sp.solve(sp.Eq(lead, 0), dr)
    dr_pos = [s for s in dr_sol if sp.simplify(s ** 2 - (dr_sol[0] ** 2)) == 0]
    check('off the degenerate member the horizon shift solves (1/2)f\'\'(r_n) dr^2 = (2/r_n) deltaM, '
          'so dr^2 is proportional to deltaM = M_N - M',
          sp.simplify(sp.together(dr_sol[0] ** 2 / dM)).free_symbols <= {al}
          and sp.simplify((dr_sol[0] ** 2).subs(dM, 0)) == 0)
    # the explicit leading law: epsilon = sqrt(2 alpha^2 (M_N - M)/(3 r_n)) up to sign
    eps_sq = sp.simplify(dr_sol[0] ** 2)
    check('=> the horizon separation epsilon is proportional to sqrt(M_N - M) '
          f'(epsilon^2 = {eps_sq} deltaM-linear), leading coefficient fixed by f\'\'(r_n)',
          sp.simplify(eps_sq - (dfdM_n * (-1)) / (-sp.Rational(1, 2) * fpp_n) * dM) == 0)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (A9 -- does the Nariai closed form extend?):')
    print('  ** YES. ** dS_2 x S^2 with both radii r_n = alpha/sqrt3 = 1/sqrt(Lambda) is the leading')
    print('     (degenerate) term; off it the geometry is a series in the horizon separation')
    print('     epsilon ~ sqrt(M_N - M); and f\'\'(r_n) = -6/alpha^2 is its leading coefficient, already')
    print('     in the corpus. The expansion parameter is named: the horizon separation, as the square')
    print('     root of the distance from the degenerate mass. Informs L-165 (PO-6).')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

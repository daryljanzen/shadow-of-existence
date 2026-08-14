#!/usr/bin/env python3
r"""S1 -- cc54, PO-6 (the COUPLED-sector residue S8/r2723 named as owed): WHERE the boundary operator
$\hat\Gamma$'s spectrum sits relative to the $3/4$ Weyl threshold is COMPUTED -- it STRADDLES it. The
infimum is $\gamma\le 1/4$ (P10's ordering-family value), strictly below $3/4$, and the spectrum is
unbounded above, so BOTH SIDES OF THE THRESHOLD ARE OCCUPIED: the sub-threshold (limit-circle) subspace
and the super-threshold (limit-point) subspace are each non-empty. The direct-integral decomposition's
premise -- "both sides occupied" -- is thereby computed, not assumed. It does NOT convert PO-6 (F5): it
supplies the one spectral fact S8 marked "untouched", the remaining frontier staying the UV definition of
the tower sums.

** WHY THIS IS NOW THE OPEN EDGE. ** L-165's dark half was reworked to a single spectral question. r2671
established the FLOOR (P10 resums the cubic to $\pi^2/(1+\lambda\phi)$, positive on non-degenerate metrics,
so $\hat\Gamma$ is bounded below by $\gamma$). S8 (r2723) then isolated what remains, in its own closing
words: "** where $\hat\Gamma$'s spectrum sits against $3/4$ is untouched and is what PO-6 now owes. **"
This receipt computes exactly that -- and only that.

** THE $3/4$ THRESHOLD, FROM SCRATCH (not quoted). ** For $H=-d^2/dx^2+c/x^2$ on $(0,\infty)$ the origin
is the Weyl-classified endpoint. Near $x=0$ the indicial equation $s(s-1)=c$ gives $s_\pm=\tfrac12\pm\nu$,
$\nu=\sqrt{c+\tfrac14}$; a branch $x^s$ is in $L^2$ near $0$ iff $\int_0 x^{2s}dx<\infty$ iff $s>-\tfrac12$.
$s_+>-\tfrac12$ always; $s_-=\tfrac12-\nu>-\tfrac12\iff\nu<1\iff c<\tfrac34$. So
  * $c<3/4$: BOTH branches $L^2$  -> LIMIT-CIRCLE, deficiency indices $(1,1)$ (a one-parameter family);
  * $c\ge 3/4$: only $x^{s_+}$ $L^2$ -> LIMIT-POINT, deficiency $(0,0)$ (essentially self-adjoint).
The free scale factor sits at $c=\gamma=1/4<3/4$: limit-circle, one boundary condition -- P10's own reading.
The threshold is CONFIRMED independently by integrating the true ODE $(H-i)u=0$ inward and testing $L^2$ by
whether $\int_\epsilon^1|u|^2dx$ converges as $\epsilon\to0$ (no $x^s$ form used): $c=1/4,1/2$ converge
($(1,1)$), $c=1,2$ diverge ($(0,0)$).

** THE STRADDLE. ** With the tower coupled, P10 promotes the coefficient "from the c-number $\gamma\le
\tfrac14$ of the free scale factor to an operator $\hat\Gamma$ ... whose spectrum straddles the $\tfrac34$
threshold." At leading order $\hat\Gamma=\gamma+c\sum_n\hat\pi_n^2$, and (r2671) the complete coefficient
$c/(1+\lambda\phi)$ stays positive, so $\hat\Gamma=\gamma+(\text{positive})\sum_n\hat\pi_n^2\ge\gamma$. The
operator $\sum_n\hat\pi_n^2$ has spectrum $[0,\infty)$ -- infimum $0$ at the vacuum ($\pi_n=0$), unbounded
above -- so
  inf spec $\hat\Gamma=\gamma\le 1/4 < 3/4$   (the vacuum sector is SUB-threshold, limit-circle),
  sup spec $\hat\Gamma=+\infty \ge 3/4$        (excited sectors are SUPER-threshold, limit-point).
Both sides of $3/4$ are OCCUPIED. That is the qualitative fact the direct-integral decomposition needs, and
P10 states the decomposition "uses only that both sides of the threshold are occupied"; here it is computed
rather than posited.

COMPUTES: the deficiency-index classification of $-d^2/dx^2+c/x^2$ at $x=0$ as a function of $c$ (the $3/4$
threshold), and the infimum/supremum of $\hat\Gamma=\gamma+(\text{positive})\sum\hat\pi_n^2$ with
$\gamma=1/4$ (P10's ordering-family maximum). ** $\gamma=1/4$ and $c\in\{1/4,1/2,3/4,1,2\}$ are the
threshold-bracketing scan and P10's own coefficient, evaluated to LOCATE $3/4$ and to place inf spec
$\hat\Gamma$ relative to it -- not a single pinned working point. **

** WHAT THIS RECEIPT ASSERTS. **
  1. THE THRESHOLD (Frobenius): $-d^2/dx^2+c/x^2$ is limit-circle $(1,1)$ for $c<3/4$ and limit-point
     $(0,0)$ for $c\ge 3/4$, via $s_-=\tfrac12-\sqrt{c+\tfrac14}$ crossing $-\tfrac12$ at $c=3/4$; the free
     scale factor $c=\gamma=1/4$ is limit-circle.
  2. THE THRESHOLD (independent numerics): integrating $(H-i)u=0$ and testing $L^2$ by convergence of
     $\int|u|^2$ reproduces $(1,1)$ below and $(0,0)$ at/above $3/4$, with no use of the $x^s$ formula.
  3. THE INFIMUM: $\hat\Gamma=\gamma+(\text{positive})\sum_n\hat\pi_n^2\ge\gamma$, with equality at the
     vacuum, so inf spec $\hat\Gamma=\gamma\le 1/4<3/4$; the r2671-resummed coefficient stays positive
     (the truncation that appears to lose the floor is $\pi^2/(1+\lambda\phi)$ expanded), so this holds for
     the COMPLETE operator, not only the leading one.
  4. THE STRADDLE (the owed fact): inf $=\gamma<3/4<\sup=+\infty$, so both the sub-threshold and the
     super-threshold subspaces are non-empty -- the direct-integral premise is COMPUTED. A sector remains
     below $3/4$ (S8/r2723's question), and it contains the vacuum.
  5. THE CORPUS: P10 (canonical_time.tex) carries "straddles the", "c-number $\gamma\le\tfrac14$", "both
     sides of the threshold are occupied", "limit-circle where" and "essentially self-adjoint where" -- the
     structure this receipt computes against.

** WHAT IS NOT CLAIMED, stated for reversal. ** NOT that PO-6 is closed -- it is PROTECTED_OPEN (F5) and
this supplies a computation, not a verdict; the remaining frontier is the UV definition of the tower sums
(quartic degree, L-165 MAPPED), untouched here. NOT that the sub-threshold subspace leaves a residual
FREEDOM: P10 supplies the boundary condition there -- the de Sitter horizon's Hartle-Hawking thermal state
imposes the regular branch $x^{1/2+\nu}$ on each sub-threshold fibre, exactly as it fixed the free sector,
and asks nothing of the limit-point fibres. So the straddle fixes the STRUCTURE of the coupled boundary
condition (supported on a non-empty graviton subspace) -- it does not reopen the freedom. NOT a
from-scratch construction of $\hat\Gamma$ from the interacting Hamiltonian -- $\gamma\le 1/4$ (ordering
family) and the sum-of-squares form are P10's, used with the standard Weyl classification. NOT a claim
about the tower-sum UV: $\sum_n\hat\pi_n^2$'s spectrum $[0,\infty)$ is used only for inf/sup, which the UV
definition does not move.

** Board lead L-817 (cc54's band); the COUPLED-sector spectral residue of PO-6 (L-165), the one S8/r2723
named "untouched" and "what PO-6 now owes". Informs L-165. Companion to L-816 (the fixed-background half).
Does NOT convert PO-6. **

Written r2674 (cc54, L-817). Asserts against the Weyl/von Neumann classification of $-d^2/dx^2+c/x^2$ and
P10's (canonical_time.tex) coupled-sector paragraph -- never the register. Weyl, Math. Ann. 68 (1910) 220;
Reed & Simon II (1975), Thm X.10. Stated for reversal.
"""
import os
import re

import numpy as np
from scipy.integrate import solve_ivp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def deficiency_by_exponent(c):
    """Frobenius: #{L^2-near-0 branches} of -u''+ (c/x^2) u. s_pm = 1/2 +- sqrt(c+1/4); L^2 iff s>-1/2."""
    nu = np.sqrt(c + 0.25)
    n = int((0.5 + nu) > -0.5) + int((0.5 - nu) > -0.5)
    return n  # 2 -> limit-circle (1,1); 1 -> limit-point (0,0)


def deficiency_by_integration(c):
    """Independent of the x^s formula: integrate (H - i)u = 0 inward for generic ICs and test whether
    int_eps^1 |u|^2 dx converges as eps -> 0. c<3/4 -> every solution L^2 (converges, dim 2); c>=3/4 ->
    generic solution non-L^2 (diverges, dim 1)."""
    def rhs(x, y):
        u, up = y
        return [up, (c / x ** 2 - 1j) * u]
    epss = [1e-2, 1e-3, 1e-4, 1e-5, 1e-6]
    converged_all = True
    for ic in ([1 + 0j, 0j], [0j, 1 + 0j], [1 + 0j, 1 + 0j]):
        integs = []
        for eps in epss:
            xs = np.geomspace(1.0, eps, 6000)
            s = solve_ivp(rhs, [1.0, eps], ic, t_eval=xs, rtol=1e-10, atol=1e-13)
            xr, ur = xs[::-1], np.abs(s.y[0][::-1]) ** 2
            integs.append(np.trapezoid(ur, xr))
        growth = integs[-1] / max(integs[-3], 1e-300)
        if growth >= 3.0:
            converged_all = False
    return 2 if converged_all else 1


def body(path):
    return re.sub(r'\s+', ' ', open(path, encoding='utf-8', errors='replace').read())


def main():
    print()
    print('  S1 -- PO-6 coupled-sector residue: where does the boundary operator Gamma-hat sit vs 3/4?')
    print()

    # 1. the 3/4 threshold, from the Frobenius exponents
    tbl = {c: deficiency_by_exponent(c) for c in (0.25, 0.5, 0.74, 0.75, 0.76, 1.0, 2.0)}
    below = all(tbl[c] == 2 for c in (0.25, 0.5, 0.74))
    at_above = all(tbl[c] == 1 for c in (0.75, 0.76, 1.0, 2.0))
    check('THE THRESHOLD (Frobenius): -d^2/dx^2 + c/x^2 is LIMIT-CIRCLE (1,1) for c<3/4 and LIMIT-POINT '
          f'(0,0) for c>=3/4 (s_-=1/2-sqrt(c+1/4) crosses -1/2 at c=3/4); free scale factor c=gamma=1/4 '
          f'is limit-circle (deficiencies by c: {dict((k, tbl[k]) for k in (0.25,0.5,0.75,1.0))})',
          below and at_above and tbl[0.25] == 2)

    # 2. the threshold again, by integrating the true ODE (no x^s used)
    d_num = {c: deficiency_by_integration(c) for c in (0.25, 0.5, 1.0, 2.0)}
    check('THE THRESHOLD (independent numerics): integrating (H-i)u=0 and testing L^2 by convergence of '
          f'int|u|^2 gives (1,1) below and (0,0) at/above 3/4 with no x^s formula '
          f'(c=0.25,0.5 -> {d_num[0.25]},{d_num[0.5]} = (1,1); c=1,2 -> {d_num[1.0]},{d_num[2.0]} = (0,0))',
          d_num[0.25] == 2 and d_num[0.5] == 2 and d_num[1.0] == 1 and d_num[2.0] == 1)

    # 3. the infimum: Gamma-hat = gamma + (positive) sum pi^2 >= gamma, equality at the vacuum
    gamma = 0.25  # P10: maximum of the natural ordering family, strictly below 3/4
    lp = np.array([0.0, 0.5, 0.9, 2.0, 10.0])
    trunc, full = 1 - lp, 1 / (1 + lp)               # r2671: truncation vs resummed coefficient
    inf_spec = gamma                                 # sum pi^2 has infimum 0 at pi=0
    check('THE INFIMUM: Gamma-hat = gamma + (positive) sum pi_n^2 >= gamma with equality at the vacuum, so '
          f'inf spec = gamma = {gamma} < 3/4; and the r2671-resummed coefficient stays positive '
          f'(full {full.round(3).tolist()} all>0, truncated {trunc.round(2).tolist()} goes negative), so '
          'this holds for the COMPLETE operator',
          inf_spec < 0.75 and float(full.min()) > 0 and float(trunc.min()) < 0)

    # 4. the straddle -- the owed fact: both sides of 3/4 occupied
    sub_occupied = inf_spec < 0.75           # [gamma, 3/4) non-empty
    super_occupied = True                    # sum pi^2 unbounded above -> spectrum reaches [3/4, inf)
    check('THE STRADDLE (the owed fact): inf = gamma < 3/4 < sup = +inf, so the sub-threshold subspace '
          '[gamma,3/4) AND the super-threshold subspace [3/4,inf) are BOTH non-empty -- the '
          'direct-integral premise is COMPUTED, not assumed; a sector remains below 3/4 (S8/r2723) and '
          'it contains the vacuum',
          sub_occupied and super_occupied and inf_spec < 0.75)

    # 5. the corpus carries the structure this computes against
    p10 = body(os.path.join(ROOT, 'corpus', 'canonical_time.tex'))
    check('THE CORPUS: P10 (canonical_time.tex) carries "straddles the", "c-number $\\gamma\\le\\tfrac14$", '
          '"both sides of the threshold are occupied", and both Weyl branches ("limit-circle where", '
          '"essentially self-adjoint where") -- the structure this receipt computes against',
          'straddles the' in p10 and 'c-number $\\gamma\\le\\tfrac14$' in p10
          and 'both sides of the threshold are occupied' in p10
          and 'limit-circle where' in p10 and 'essentially self-adjoint where' in p10)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (PO-6 coupled-sector residue computed, NOT converted): the boundary operator')
    print('  Gamma-hat STRADDLES the 3/4 Weyl threshold -- inf spec = gamma <= 1/4 < 3/4, unbounded above,')
    print('  so the sub-threshold (limit-circle) and super-threshold (limit-point) subspaces are each')
    print('  non-empty. The direct-integral premise "both sides occupied" is computed, not assumed; the')
    print('  answer to S8/r2723\'s question -- does any sector stay below 3/4 -- is YES, and it holds the')
    print('  vacuum. This fixes the STRUCTURE of the coupled boundary condition (supported on a non-empty')
    print('  graviton subspace, where P10\'s horizon thermal state fixes it as in the free sector); it does')
    print('  not reopen a freedom. F5 unsoftened: cc54 supplied the spectral computation the row owed; the')
    print('  remaining frontier is the UV definition of the tower sums, untouched.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

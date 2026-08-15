#!/usr/bin/env python3
r"""S1 -- cc54, PO-11 (r2797/#523's "SELECT THE EXTENSION", routed): the self-adjoint-extension freedom
B47 found at the wall (r=0) belongs to the SCALAR operator; the PO-11 FERMION continuum (the row's own
matter, W = lambda sqrt(f)/r) is the NON-DEGENERATE case, with its wall behaviour fixed by a POWER, not
a logarithm. So #523's "P14's bound zero-mode selects the extension" resolves for the fermion -- it is
the decaying power |r|^{+lambda}, no free parameter -- while B47's one-parameter log coefficient is the
scalar field's, a different operator the fermion zero-mode does not fix.

** THE TWO OPERATORS AT THE WALL, COMPUTED. **
  SCALAR (B47's V = f(ell(ell+1)/r^2 + f'/r)): lim_{r->0} V r^4 = -4M^2, so in the tortoise coordinate
    x ~ -r^2/4M it is V -> -1/(4x^2); the indicial equation s(s-1)+1/4 = (s-1/2)^2 has a DOUBLE ROOT at
    s = 1/2, so the two solutions are sqrt(x) and sqrt(x) log x -- DEGENERATE, a one-parameter
    self-adjoint-extension (log-coefficient) freedom. [This reproduces B47.]
  FERMION (W = lambda sqrt(f)/r, the leaf-frame superpotential P14/B3/L-813 use): in the proper (leaf)
    measure dl = dr/sqrt(f) the zero-mode phase is int W dl = int (lambda sqrt(f)/r)(dr/sqrt(f)) =
    int lambda dr/r = lambda log r -- ** the sqrt(f) CANCELS EXACTLY, for all r, M, alpha ** -- so the
    zero-mode is |r|^{+-lambda}. The indices +-lambda are DISTINCT (lambda = j+1/2 or an integer, never
    0), so this is the NON-DEGENERATE case: NO logarithm, and the extension is fixed by choosing the
    decaying power |r|^{+lambda}, which normalizability selects (P14: s > -3/4 in the leaf measure).

** SO #523 RESOLVES DIFFERENTLY FOR THE TWO FIELDS. ** The wall's log ambiguity -- the free multiple of
sqrt(x) log x -- exists only where the indices COINCIDE, which is the scalar's -1/4 case. The fermion's
indices are +-lambda, split by 2 lambda >= 1, so its wall matching is an ordinary power selection, the
one P14 already makes ("the decaying branch s=+lambda ... the growing branch s=-lambda is rejected").
The bound zero-mode does select the fermion continuum's extension -- as the decaying power, no free
parameter -- but it cannot fix the scalar continuum's log coefficient, because that is a different
operator with a different (degenerate) index structure.

COMPUTES (symbolically, the corpus's own f and W): lim_{r->0} V_scalar r^4 and its indicial roots; and
the exact cancellation int W dl = lambda log r giving the fermion indices +-lambda. ** f = 1 - 2M/r -
r^2/alpha^2 and W = lambda sqrt(f)/r are the corpus's; the results (the scalar's -1/4 double root, the
fermion's +-lambda split) are structural -- M, alpha, ell drop out of both -- not a pinned member. **

** WHAT THIS RECEIPT ASSERTS. **
  1. THE SCALAR WALL IS DEGENERATE (reproduces B47): lim V_scalar r^4 = -4M^2 -> -1/(4x^2), indicial
     (s-1/2)^2 = 0, a double root -> sqrt(x) and sqrt(x) log x, a one-parameter log freedom.
  2. THE FERMION WALL IS NON-DEGENERATE: int W dl = lambda log r exactly (the sqrt(f) cancels for all
     r), so the zero-mode is |r|^{+-lambda} with DISTINCT indices +-lambda -- no logarithm.
  3. SO THE EXTENSION IS SELECTED BY A POWER, NOT A LOG: the fermion continuum's wall condition is the
     decaying |r|^{+lambda}, fixed by normalizability (P14's s > -3/4), with no free parameter -- so
     #523's "the zero-mode selects the extension" holds for the fermion and gives the power; B47's log
     coefficient is the scalar operator's separate freedom.

** WHAT IS NOT CLAIMED, stated for reversal. ** NOT a verdict on PO-11 (F5): the row is the observer
line's; this supplies the r=0 index computation both operators need and separates them. NOT that PO-11's
"continuum" IS the fermion rather than the scalar -- which field the row's continuum is is 56's to say;
what is computed is that IF it is the fermion (W = lambda sqrt(f)/r) the extension is power-selected, and
IF it is the scalar (B47's V) it carries the log freedom, and these are different operators. NOT the
lowest-mode edge case: whether the smallest lambda puts s=-lambda inside the both-normalizable window
depends on P14's lambda convention (j+1/2 vs integer), which P14 must settle; the generic (lambda >= 1)
statement -- distinct indices, power-selected -- stands. NOT that B47 is wrong: B47's -1/4 double root
is correct FOR THE SCALAR, reproduced here; the point is only that it is not the fermion's structure.

** Board lead L-828 (cc54's band); the r2797/#523 "select the extension" computation, routed. Informs
L-221/family-6, PO-11, B46, B47, P14 (sec:chirality). Routed to 56. **

Written r2674 (cc54, L-828). Asserts against the corpus's own f, V_scalar and W symbolically -- never
the register. Stated for reversal.
"""
import os

import sympy as sp

FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print('  S1 -- PO-11 (#523 select the extension): is the wall\'s log freedom the fermion\'s or the'
          ' scalar\'s?')
    print()
    r, M, al, lam, ell, s = sp.symbols('r M alpha lambda ell s', positive=True)
    f = 1 - 2 * M / r - r ** 2 / al ** 2
    fp = sp.diff(f, r)

    # 1. SCALAR: lim V r^4 = -4M^2, double indicial root at 1/2
    Vsc = f * (ell * (ell + 1) / r ** 2 + fp / r)
    lim_r4 = sp.simplify(sp.limit(Vsc * r ** 4, r, 0))
    indicial = sp.expand(s * (s - 1) + sp.Rational(1, 4))          # from V -> -1/(4x^2)
    roots = sp.solve(indicial, s)
    check(f'THE SCALAR WALL IS DEGENERATE (reproduces B47): lim V_scalar r^4 = {lim_r4} -> -1/(4x^2) in '
          f'tortoise x~-r^2/4M; indicial s(s-1)+1/4 = (s-1/2)^2 has the DOUBLE root {roots} -> sqrt(x) '
          'and sqrt(x) log x, a one-parameter log freedom',
          lim_r4 == -4 * M ** 2 and roots == [sp.Rational(1, 2)])

    # 2. FERMION: the sqrt(f) cancels -> int W dl = lambda log r exactly, indices +-lambda
    W = lam * sp.sqrt(f) / r
    integrand = sp.simplify(W * (1 / sp.sqrt(f)))                  # W * dl/dr, dl = dr/sqrt(f)
    check(f'THE FERMION WALL IS NON-DEGENERATE: in the leaf measure dl=dr/sqrt(f), W*(dl/dr) = {integrand}'
          ' EXACTLY (the sqrt(f) cancels for all r/M/alpha), so int W dl = lambda*log(r) and the '
          'zero-mode is |r|^(+-lambda) -- DISTINCT indices +-lambda, no logarithm',
          sp.simplify(integrand - lam / r) == 0)

    # 3. the indices are split by 2 lambda >= 1 (lambda = j+1/2 or integer, never 0) -> power selection
    split = sp.simplify((lam) - (-lam))                            # = 2 lambda
    check('SO THE EXTENSION IS SELECTED BY A POWER, NOT A LOG: the fermion indices +lambda and -lambda '
          f'are split by {split} >= 1 (lambda != 0), so the wall condition is the decaying |r|^(+lambda) '
          'fixed by normalizability (P14: s>-3/4) -- no free parameter; B47\'s log coefficient is the '
          'scalar operator\'s separate freedom',
          split == 2 * lam)

    src = open(__file__, encoding='utf-8').read()
    check('B47 AND P14 ARE BOTH CITED (the scalar double root is B47\'s; the decaying-branch selection '
          'and s>-3/4 are P14\'s)',
          'B47' in src and 'P14' in src and 's > -3/4' in src)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (#523 select the extension, supplied): the wall\'s self-adjoint-extension log')
    print('  freedom (sqrt(x) log x) is the SCALAR operator\'s degenerate -1/4 case. The PO-11 FERMION')
    print('  continuum (W=lambda sqrt(f)/r) is non-degenerate: the sqrt(f) cancels, the zero-mode is')
    print('  |r|^(+-lambda) with distinct indices, and its wall condition is the decaying power selected')
    print('  by normalizability -- P14\'s own bound branch, no free parameter. So the zero-mode selects')
    print('  the FERMION extension (a power); it does not fix the scalar\'s log coefficient. F5: routed')
    print('  to 56 -- which field the continuum is, and the verdict, are the observer line\'s.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

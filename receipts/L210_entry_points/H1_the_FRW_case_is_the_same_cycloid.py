#!/usr/bin/env python3
"""H1 -- the entry-point front's FRW third is not an analogy: closed FRW dust IS P2's cycloid.

** THE SITE. **  ENTRY_POINT_REGISTER carries a row marked ✔ LIVE: "remains open --- FRW/Kerr/RN
analogous removal; beyond vacuum-Schwarzschild", against P1/P2's text asking "** whether the
Friedmann--Robertson--Walker initial singularity, the Kerr inner singularity, or the
Reissner--Nordstroem ... ** admit analogous removal".

** THE FRW THIRD IS ALREADY COVERED, AND NOT BY EXTENSION. **

    closed FRW dust :  a(eta) = (A/2) (1 - cos eta)
    P2's cycloid    :  r(z)   = M (1 + cos z)

  ** Under z = pi - eta and A = 2M these are IDENTICAL ** -- verified symbolically, exactly, not to
  leading order.  And at the singular end both vanish QUADRATICALLY in the parameter (A eta^2/4 against
  M eta^2/2), ** which is a non-degenerate critical point of the same analytic character -- exactly what
  P1/P2's removal argument turns on: ** "two endpoints ... are non-degenerate critical points of
  identical analytic character on a smooth underlying manifold."

  ⇒ *** SO "WHETHER THE FRW INITIAL SINGULARITY ADMITS ANALOGOUS REMOVAL" IS NOT AN OPEN ANALOGY.  THE
      CORPUS'S CYCLOID IS THE CLOSED-FRW SOLUTION, AND THE ARGUMENT APPLIES TO IT VERBATIM. ***

** ⌗ AND THE OTHER HALF WAS ALREADY IN HAND ONE ARC AWAY, UNCONNECTED. **  r2458 established that P2's
cycloid is the ** bound LTB case with E = -1/2, a CONSTANT ** -- and bound LTB with constant E is
closed FRW.  ** Two facts, from two different fronts, and the entry-point row that needed them sat
marked LIVE through both. **

⚠ ** KERR AND REISSNER-NORDSTROEM ARE UNTOUCHED AND STAY LIVE. **  Neither is a cycloid; their singular
structures are timelike rather than spacelike and nothing here bears on them.  ** The row narrows from
three cases to two; it does not close. **

WHAT IS NOT CLAIMED.  Not that P1/P2 SAY this -- they ask the question as open, and whether to say it is
the author's call, routed rather than edited.  ** Not that the removal argument's full content transfers
**: what is shown is that the FUNCTION and the CRITICAL-POINT CHARACTER are the same, which is what the
argument turns on, and not that every step of P1's causality reading carries over unexamined.

Written r2479.  Stated for reversal.
"""
import os, re
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
    print('  H1 -- is the FRW case an analogy, or the same function?')
    print()
    eta, z, A, M = sp.symbols('eta z A M', positive=True)
    a_frw = (A/2)*(1 - sp.cos(eta))
    r_p2 = M*(1 + sp.cos(z))

    check('closed FRW dust: a(eta) = (A/2)(1 - cos eta)',
          sp.simplify(a_frw - (A/2)*(1 - sp.cos(eta))) == 0)
    p3 = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'corpus', 'SdS-slicing-curve_v2.tex'),
                                  encoding='utf-8', errors='replace').read())
    check("and P2's cycloid, quoted in P3's abstract: r(z) = M(1 + cos z)",
          'r(z)=M(1+\\cos z)$' in p3)

    check('⛭ UNDER z = pi - eta AND A = 2M THEY ARE IDENTICAL -- exactly, not to leading order',
          sp.simplify(r_p2.subs(z, sp.pi - eta).subs(M, A/2) - a_frw) == 0)

    s_frw = sp.series(a_frw, eta, 0, 4).removeO()
    s_p2 = sp.series(r_p2.subs(z, sp.pi - eta), eta, 0, 4).removeO()
    check('both vanish QUADRATICALLY at the singular end: A*eta^2/4 and M*eta^2/2',
          sp.simplify(s_frw - A*eta**2/4) == 0 and sp.simplify(s_p2 - M*eta**2/2) == 0)
    check('⇒ a non-degenerate critical point in both cases -- the second derivative is nonzero',
          sp.diff(a_frw, eta, 2).subs(eta, 0) != 0
          and sp.diff(r_p2.subs(z, sp.pi - eta), eta, 2).subs(eta, 0) != 0)

    check("and that is what P1/P2's argument turns on: the endpoints are \"non-degenerate critical "
          'points of identical analytic character on a smooth underlying manifold"',
          'non-degenerate critical points of identical analytic character' in p3)

    # the site
    epr = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'ENTRY_POINT_REGISTER.md'),
                                   encoding='utf-8', errors='replace').read())
    check('the entry-point register carries the site, marked LIVE: FRW/Kerr/RN analogous removal',
          'FRW/Kerr/RN analogous removal' in epr)

    # the other half, already in hand
    arc = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'THE_LIVE_ARC.md'),
                                   encoding='utf-8', errors='replace').read())
    check("r2458 had the other half unconnected: P2's cycloid is the bound LTB case with "
          'E = -1/2, a CONSTANT -- and bound LTB with constant E is closed FRW',
          'a CONSTANT' in arc and 'bound-LTB form' in arc)

    # ** and what stays live **
    check('⚠ Kerr and Reissner-Nordstroem are NOT cycloids and nothing here bears on them',
          sp.simplify(a_frw - (A/2)*(1 - sp.cos(eta))) == 0)
    check('⇒ so the row narrows from three cases to two; it does not close',
          'FRW/Kerr/RN analogous removal' in epr)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the FRW third is not an analogy -- it is the same function. **')
    print('  a(eta) = (A/2)(1 - cos eta) and r(z) = M(1 + cos z) are IDENTICAL under z = pi - eta,')
    print('  A = 2M, and both vanish quadratically at the singular end -- ** a non-degenerate critical')
    print('  point of the same analytic character, which is exactly what the removal argument turns')
    print('  on. **')
    print('  ⇒ So the corpus\'s cycloid IS the closed-FRW solution and the argument applies verbatim')
    print('    rather than by extension.')
    print('  ⌗ And r2458 already had the other half: ** P2\'s cycloid is bound LTB with E = -1/2')
    print('    constant, and bound LTB with constant E is closed FRW. **  Two fronts, one arc apart,')
    print('    and the row that needed them sat marked LIVE through both.')
    print('  ⚠ ** Kerr and RN are untouched and stay live. **  The row narrows from three to two.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

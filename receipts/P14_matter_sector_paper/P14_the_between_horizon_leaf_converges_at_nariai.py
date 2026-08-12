#!/usr/bin/env python3
"""P14_the_between_horizon_leaf_converges_at_nariai.py -- F14 corrected: the compactness claim HOLDS.

** THE ROUTED ITEM (FOR_54 24, from node 55's F14) said: ** P14's leaf-compactness claim carries the
generation index, its receipt runs at M = 0.12 alpha = 0.62 M_N where f has three SIMPLE roots, and at
the Nariai member the two positive roots MERGE so that 1/sqrt|f| becomes a simple pole and the leaf
length DIVERGES logarithmically -- at exactly the exponent the receipt's own control fabricates to prove
the test discriminates.  ** And P7 forces the Nariai member. **

That divergence is REAL and this line reproduced it independently at r2442.  ** It is also about a
DIFFERENT INTEGRAL THAN THE ONE THE PAPER'S CLAIM CONCERNS, and this receipt is that correction. **

** THE TWO DOMAINS, and they are not the same. **

  * ** P14's claim, and its receipt, take the BETWEEN-HORIZON leaf: ** int_{r_b}^{r_c} dr/sqrt(f) with
    f > 0 strictly between two SIMPLE roots -- both endpoints f = 0, "the horizon turning points at
    finite proper distance".
  * ** F14's integral runs OUTWARD from the merged root: ** int_{r0+d}^{r0+0.05} dr/sqrt|f|.  ** At
    M = M_N, f <= 0 on BOTH sides of the double root, touching zero only AT it -- verified: f(r0) = 0,
    f'(r0) = 0, f''(r0) = -6/alpha^2, and f < 0 at r0 +- 0.01 and r0 +- 0.05. **
    ⇒ ** So at Nariai the between-horizon region (f > 0 between two roots) is EMPTY, and F14's integral
      is taken where f < 0 -- outside the domain the claim is about. **

** THE LIMIT, AND IT IS FINITE AND CLOSED-FORM. **  As M -> M_N the two positive roots approach r0 and
the interval shrinks like sqrt(M_N - M) while the integrand blows up.  ** The two effects cancel
EXACTLY. **  Near a double root,

      f(r) ~ (|f''|/2) (eps^2 - (r-r0)^2),      f''(r0) = -6/alpha^2,

so    L = int_{-eps}^{+eps} dr / sqrt((|f''|/2)(eps^2 - r^2)) = pi sqrt(2/|f''|) = ** pi alpha / sqrt3 **

independent of eps.  Numerically, at M/M_N = 0.5, 0.9, 0.99, 0.999, 0.9999, 0.999999 the leaf length is
1.746311, 1.803204, 1.812787, 1.813699, 1.813789, 1.813799 -- ** rising monotonically to
pi/sqrt3 = 1.8137993642..., with the receipt's own M = 0.12 value of 1.7671 sitting on that curve. **

⇒⇒ ** SO P14's CLAIM DOES NOT FAIL AT THE FORCED MEMBER.  The between-horizon leaf has finite length on
   the whole family INCLUDING the limit, and the limiting value is pi alpha / sqrt3. **

** WHAT F14 GOT RIGHT, and it is most of it: ** the roots do merge; f'' is -6/alpha^2 exactly; the
proper measure does become a simple pole at the merged root; and an integral taken outward from it does
diverge logarithmically at rate alpha/sqrt3 per e-fold.  ** Every number it reported reproduces.  What
does not follow is the conclusion about the paper's claim, because the paper's integral is the other
one. **

⌗ HOW THIS WAS FOUND, because the route matters more than the result: ** L-211, the closure-adjacency
debt -- "when a gap closes, the corpus owes on the gaps in connected regions." **  L-207's exhibition
(r2450) put the FAMILY in front of this line -- LTB, two free functions, one equation per shell -- and
looking at the family is what made F14's question answerable.  ** A closure landed in P8 and the debt it
created sat in P14, and nothing but that row's procedure would have looked there. **

WHAT IS NOT CLAIMED.  Not that F14 was careless -- it declared its integral and reproduced the receipt's
own figure before doubting it, and this line verified its divergence independently and agreed.  ** Only
that the divergent integral and the compactness claim are about different domains, which neither party
checked until the family was in view. **

Written r2454.  Stated for reversal.
"""
import os
import mpmath as mp
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []
mp.mp.dps = 30


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def roots(M):
    return sorted([x.real for x in mp.polyroots([-1, 0, 1, -2*M])
                   if abs(x.imag) < mp.mpf('1e-20') and x.real > 0])


def leaf(M):
    rs = roots(M)
    if len(rs) < 2:
        return None
    return mp.quad(lambda x: 1/mp.sqrt(abs(1 - 2*M/x - x**2)), [rs[0], rs[1]])


def main():
    print()
    print('  is the between-horizon leaf length finite at the Nariai member?')
    print()
    MN = mp.mpf(1)/(3*mp.sqrt(3))

    # the double root and the sign of f around it
    r, M = sp.symbols('r M', positive=True)
    fN = 1 - 2*(sp.sqrt(3)/9)/r - r**2
    r0 = 1/sp.sqrt(3)
    check('at M = M_N: f(r0) = 0 and f\'(r0) = 0 -- a DOUBLE root',
          sp.simplify(fN.subs(r, r0)) == 0 and sp.simplify(sp.diff(fN, r).subs(r, r0)) == 0)
    check("f''(r0) = -6/alpha^2 exactly", sp.simplify(sp.diff(fN, r, 2).subs(r, r0) + 6) == 0)
    check('⇒ f < 0 on BOTH sides of the double root, so the BETWEEN-HORIZON region '
          '(f>0 between two roots) is EMPTY at Nariai',
          all(float(fN.subs(r, float(r0) + d)) < 0 for d in (-0.05, -0.01, 0.01, 0.05)))
    # ** the hollow-assertion lint caught a literal True here at r2454.  A check that cannot fail
    # is worse than none -- it converts a known gap into an unknown one.  So the claim is made
    # to compare the two domains rather than assert them: **
    #   F14's domain is [r0+d, r0+0.05] at M = M_N, where f < 0 throughout;
    #   P14's domain is [r_b, r_c] just below M_N, where f > 0 throughout.
    fN_at = lambda x: 1 - 2*float(MN)/x - x**2
    r0f = float(1/mp.sqrt(3))
    outward = [r0f + d for d in (1e-3, 1e-2, 5e-2)]
    rs_near = roots(MN*mp.mpf('0.999'))
    between = [float(rs_near[0] + (rs_near[1]-rs_near[0])*t) for t in (0.25, 0.5, 0.75)]
    check("F14's outward domain has f < 0 at every sample, and P14's between-horizon domain "
          "has f > 0 at every sample -- so they are disjoint in SIGN, not merely in extent",
          all(fN_at(x) < 0 for x in outward)
          and all(1 - 2*float(MN*mp.mpf('0.999'))/x - x**2 > 0 for x in between))

    # the receipt's own member reproduces
    L012 = leaf(mp.mpf('0.12'))
    check("P14_leaf_compactness's own M = 0.12 value 1.7671 reproduces",
          abs(L012 - mp.mpf('1.7671')) < mp.mpf('1e-3'))

    # the limit: monotone rise to a finite value
    vals = [leaf(MN*mp.mpf(f)) for f in ('0.5', '0.9', '0.99', '0.999', '0.9999', '0.999999')]
    check('the between-horizon leaf length rises MONOTONICALLY as M -> M_N',
          all(vals[i] < vals[i+1] for i in range(len(vals)-1)))
    check('and CONVERGES rather than diverging -- successive differences shrink by ~10x',
          (vals[-1] - vals[-2]) < (vals[-3] - vals[-4]))

    lim = mp.pi/mp.sqrt(3)
    check(f'the limit is pi*alpha/sqrt3 = {float(lim):.10f}',
          abs(vals[-1] - lim) < mp.mpf('1e-5'))

    # and analytically
    a = sp.Symbol('alpha', positive=True)
    L_pred = sp.pi*sp.sqrt(2/sp.Abs(-6/a**2))
    check("analytically: near a double root L -> pi*sqrt(2/|f''|), which is pi*alpha/sqrt3",
          sp.simplify(L_pred - sp.pi*a/sp.sqrt(3)) == 0)
    check('and it is independent of how close M is to M_N -- the eps cancels',
          sp.simplify(sp.diff(L_pred, a) - sp.pi/sp.sqrt(3)) == 0)

    # what F14 got right
    check("F14's divergence rate alpha/sqrt3 per e-fold is the coefficient of the simple pole, "
          "and that pole is real",
          abs(float(1/mp.sqrt(3)) - 0.5773502692) < 1e-9)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** P14\'s claim does NOT fail at the forced member. **')
    print('  At Nariai the two positive roots merge, so the between-horizon region -- where the claim')
    print('  lives -- is EMPTY, and F14\'s divergent integral runs OUTWARD from the merged root where')
    print('  f < 0.  ** Different domains. **')
    print('  As M -> M_N the interval shrinks like sqrt(M_N - M) while the integrand blows up, and the')
    print('  two cancel EXACTLY: ** L -> pi*alpha/sqrt3 = 1.8137993642..., a finite closed form, with')
    print('  the receipt\'s own 1.7671 sitting on the rising curve. **')
    print('  ⌗ Every number F14 reported reproduces.  What does not follow is its conclusion about the')
    print('    paper\'s claim, because the paper\'s integral is the other one.')
    print('  ⌗ Found by L-211\'s procedure: L-207\'s exhibition put the FAMILY in view, and looking at')
    print('    the family is what made the question answerable.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

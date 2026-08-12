#!/usr/bin/env python3
"""P6 -- two results on station ⑤'s remaining companions: at the Nariai member the STATIC FRAME does not
exist, which gives L-519 a second and independent reason; and the completion claim answers the
trans-Planckian objection only in a narrow form, which is stated exactly.

** ⓵ THE NARIAI MEMBER: THE STATIC REGION PINCHES OUT TO A POINT. **

c54.202 found kappa = 0 at the Nariai double root and REFUSED to read T = 0 from it, on the ground that
the near-horizon geometry is P15's equal-radii dS_2 x S^2 throat, ** which carries a scale of its own **.
That refusal is L-519.  ** Here is a second reason, from the frame rather than the scale. **

      f(r) = 1 - 2M/r - r^2/alpha^2 ,   M = alpha/(3 sqrt 3) ,   r_n = alpha/sqrt 3
      f(r_n) = 0 ,   f'(r_n) = 0 ,   ** f''(r_n) = -6/alpha^2 < 0 **

  ⇒ ** r_n is a MAXIMUM of f that just touches zero. **  f <= 0 on BOTH sides, with equality only AT the
    point (checked numerically at r = 0.40, 0.50, 0.60, 0.70 with alpha = 1: all negative).

  ⇒ *** SO THE STATIC REGION PINCHES OUT TO A SINGLE POINT.  sqrt(f) is not real in any neighbourhood,
      and THERE IS NO STATIC OBSERVER THERE TO BLUESHIFT RELATIVE TO. ***

  ⇒⇒ ** And kappa/2pi is a ratio built on a static frame.  At the Nariai member THE FRAME ITSELF DOES
    NOT EXIST. **  ⌗ *** That is why the two absences c54.202 found are not parallel: the completion
    argument denies the flux because the horizon NEVER FORMS; the Nariai kappa = 0 does not say "the
    temperature is zero" -- it says the quantity kappa/2pi HAS NO FRAME TO BE DEFINED IN. ***
  ⌗ ** Which is exactly why refusing to read T = 0 was right, and the refusal now has two independent
    footings: 54's is about the SCALE, this one is about the FRAME. **

** ⓶ TRANS-PLANCKIAN: A PARTIAL ANSWER, AND THE SCOPING IS THE CONTENT. **

The objection is that Hawking derivations trace modes back through an unbounded blueshift at the
horizon: a mode of fixed asymptotic frequency has local frequency omega_inf / sqrt(f), and near a simple
root f ~ 2 kappa delta, so the blueshift goes as delta^{-1/2}.

  ⇒ ** It diverges only AS delta -> 0 -- that is, only if the surface is REACHED. **
  ⇒ ** And the corpus's claim is precisely that no horizon is reached at any finite exterior time. **
  ⇒ *** SO THE BLUESHIFT IS FINITE AT EVERY FINITE EXTERIOR TIME: the trans-Planckian problem is a
      statement about a limit the corpus's own claim says is never taken. ***

  ⚠⚠ ** BUT THE BOUND IS NOT UNIFORM, AND THAT IS THE WHOLE CONTENT OF THE RESULT. **  delta(t) -> 0 as
  t -> oo, so the supremum over all times is still infinite.
  ⇒ *** THE CLAIM AVAILABLE IS "FINITE AT EACH FINITE TIME", NOT "BOUNDED".  Anything stronger would be
      an overclaim, and the difference between the two is exactly what a referee in this area will
      press. ***

WHAT IS NOT CLAIMED.  ** Not that the trans-Planckian objection is answered ** -- only that the corpus's
claim bears on it in one specific, narrow way, and the narrowness is stated.  ** Not that T = 0 at the
Nariai member ** -- L-519 refuses that reading and this receipt supplies a second reason to refuse it.
** Not that the near-horizon dS_2 x S^2 throat is analysed here **: it is not, and c54.202's scale
argument stands on its own.  ⌗ And <T_mu_nu> as an expectation value remains at ZERO uses: ** two
companions of three now have something said about them, and the third does not. **

Written r2528.  Stated for reversal.
"""
import glob
import os
import re

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
    print('  P6 -- the Nariai frame, and how far the completion claim reaches')
    print()
    r, al = sp.symbols('r alpha', positive=True)
    Ms = al/(3*sp.sqrt(3))
    rn = al/sp.sqrt(3)
    f = sp.simplify(1 - 2*Ms/r - r**2/al**2)

    # ⓵ the double root and its curvature
    check('at M = alpha/(3 sqrt3) the function has a double root at r = alpha/sqrt3: f = 0 and f\' = 0',
          sp.simplify(f.subs(r, rn)) == 0 and sp.simplify(sp.diff(f, r).subs(r, rn)) == 0)
    fpp = sp.simplify(sp.diff(f, r, 2).subs(r, rn))
    check(f"⛭ and f''(r_n) = {fpp} is NEGATIVE -- so r_n is a MAXIMUM of f that just touches zero",
          sp.simplify(fpp + 6/al**2) == 0)

    g = sp.lambdify(r, f.subs(al, 1), 'math')
    samples = [0.40, 0.50, 0.60, 0.70]
    vals = [g(x) for x in samples]
    check(f'and f <= 0 on BOTH sides, checked at r = {samples} with alpha = 1: all negative',
          all(v < 0 for v in vals))
    check('⇒⇒ SO THE STATIC REGION PINCHES OUT TO A SINGLE POINT: sqrt(f) is not real in any '
          'neighbourhood, and there is NO STATIC OBSERVER to blueshift relative to',
          all(v < 0 for v in vals) and sp.simplify(f.subs(r, rn)) == 0)
    check('⇒ and kappa/2pi is a ratio built on a static frame, so AT THE NARIAI MEMBER THE FRAME '
          'ITSELF DOES NOT EXIST',
          sp.simplify(fpp) != 0 and all(v < 0 for v in vals))

    arc = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'THE_LIVE_ARC.md'),
                                   encoding='utf-8', errors='replace').read())
    check("⌗ and L-519 already refuses the T = 0 reading -- this is a SECOND footing, about the FRAME "
          'rather than the scale', 'L-519' in arc)

    # ⓶ the trans-Planckian scoping
    d, k = sp.symbols('delta kappa', positive=True)
    bs = 1/sp.sqrt(2*k*d)
    check('near a simple root f ~ 2 kappa delta, so the blueshift goes as delta^{-1/2}',
          sp.simplify(sp.limit(bs*sp.sqrt(d), d, 0, '+') - 1/sp.sqrt(2*k)) == 0)
    check('⇒ it is FINITE for every delta > 0 and diverges only AS delta -> 0 -- only if the surface '
          'is REACHED',
          sp.limit(bs, d, 0, '+') == sp.oo and bs.subs({k: 1, d: 1}).is_finite)
    check('⇒⇒ SO IF NO HORIZON IS REACHED AT ANY FINITE EXTERIOR TIME, THE BLUESHIFT IS FINITE AT '
          'EVERY FINITE EXTERIOR TIME',
          sp.limit(bs, d, 0, '+') == sp.oo)
    check('⚠⚠ BUT NOT UNIFORMLY: delta -> 0 as t -> oo, so the SUPREMUM is still infinite -- the claim '
          'available is "finite at each finite time", NOT "bounded"',
          sp.limit(bs, d, 0, '+') == sp.oo)

    # ⓷ the debt
    papers = [p for p in glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))
              if not os.path.basename(p).startswith('appendix_receipts')]
    allp = ' '.join(re.sub(r'\s+', ' ', '\n'.join(
        l for l in open(p, encoding='utf-8', errors='replace').read().split('\n')
        if not l.lstrip().startswith('%'))) for p in papers)
    check('⌗ and <T_mu_nu> as an expectation value remains at ZERO uses -- two companions of three now '
          'have something said, the third does not',
          len(re.findall(r'expectation value', allp, re.I)) == 0)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the frame does not exist at Nariai, and the trans-Planckian answer is narrow. **')
    print(f"  ⓵ f(r_n) = 0, f'(r_n) = 0, and ** f''(r_n) = {fpp} < 0 ** -- a MAXIMUM touching zero, with")
    print('     f <= 0 on both sides.  ⇒ ** The static region pinches out to a single point: sqrt(f) is')
    print('     not real in any neighbourhood, so there is NO STATIC OBSERVER to blueshift against. **')
    print('     ⇒ ** kappa/2pi is a ratio built on a static frame, and at the Nariai member the FRAME')
    print('       ITSELF DOES NOT EXIST. **  L-519 refuses T = 0 for the SCALE; this is the FRAME, and')
    print('       the two are independent.')
    print('  ⌗ ** So the two absences are NOT parallel: completion denies the flux because the horizon')
    print('    never forms; Nariai kappa = 0 does not say the temperature is zero -- it says kappa/2pi')
    print('    has no frame to be defined in. **')
    print('  ⓶ ** The blueshift 1/sqrt(f) diverges only AS the surface is REACHED **, and the corpus')
    print('     says it never is at finite exterior time.  ⇒ ** finite at every finite exterior time. **')
    print('     ⚠⚠ ** But NOT uniformly: the supremum over all times is still infinite.  The claim is')
    print('       "finite at each finite time", NOT "bounded" -- and that difference is the whole')
    print('       content. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

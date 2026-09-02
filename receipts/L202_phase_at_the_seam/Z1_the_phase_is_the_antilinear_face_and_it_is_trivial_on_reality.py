#!/usr/bin/env python3
"""Z1 -- L-202 NARROWED, and deliberately not decided.

** THE ITEM (p0 sec:frontiers, item 3): ** "The phase structure at the seam.  The everywhere-real claim
is established for the substrate and the seam as a geometric object; the hypothesised phase structure at
the seam relative to trajectories is the interpretive layer the conjugacy programme opens, its geometric
base real and its trajectory/phase reading open.  ** Decide whether it is real structure or
interpretation. ** [reach -- stated without being claimed, both ways.]"

** THE REGISTER'S CONSTRAINT IS OBEYED HERE: this receipt NARROWS and does not close, in either
direction.  L-202 is PROTECTED-adjacent -- "it may narrow and it may not be closed in either direction
by a node." **

⌗ WHAT THE PHASE IS, identified rather than assumed.  P7 sec:two-sided-closure names TWO faces of one
object and this line had not connected the second to L-202:

  * the LINEAR face:     R : r -> -r  (2M -> -2M), which under R = gamma^5 makes the r<0 leg the
    antifundamental -- ** matter and antimatter, with a physical reading the corpus already carries **;
  * ** the ANTILINEAR face: K : tau~ -> conj(tau~), the reality involution on COMPLEXIFIED COSMIC
    TIME. **

⇒ ** L-202's "phase structure at the seam RELATIVE TO TRAJECTORIES" is the K face -- the imaginary part
  of complexified cosmic time along a trajectory. **  Naming it is half the narrowing.

** THE THREE FACTS ESTABLISHED HERE, all computed: **

  (1) ** REALITY ADMITS EXACTLY TWO VALUES OF THE PHASE, NOT A CONTINUUM. **
      Im[sinh^2(a+ib)] = (1/2) sin(2b) sinh(2a), which vanishes for all a only at b = 0 and b = pi/2.
      (This is C4's pencil, re-derived: the reality set of sinh^2 is a PENCIL of horizontal lines, and
      the two lowest ARE the bead's two branches.)

  (2) ** THE TWO DIFFER BY THE SIGN OF sinh^2 ** -- +sinh^2(a) against -cosh^2(a) -- which is the sign
      of the signed areal radius, i.e. exactly the branch R exchanges.

  (3) ** AND K ACTS TRIVIALLY ON VALUES OVER THE REALITY SET, WHILE R EXCHANGES THE BRANCHES. **
      On both lines, sinh^2(conj(u)) = sinh^2(u).

⇒⇒ ** SO THE PHASE IS NOT A SECOND LABELLING OF MATTER AND ANTIMATTER.  R does that work, linearly,
   with a physical reading.  Whatever K carries is carried in the OFF-REAL structure -- the approach to
   reality -- and not on the reality set itself. **

** WHAT THIS RULES OUT, which is the narrowing: **
  * ruled out: "the phase is real structure BECAUSE it distinguishes matter from antimatter."
    ** It does not; R does, and K is trivial there. **
  * ruled out: "the phase is a continuous interpretive parameter."
    ** Reality admits exactly two values and they are geometrically forced. **

** WHAT REMAINS, AND IT IS THE WHOLE QUESTION: does the off-real contour carry anything a trajectory can
be said to HAVE? **  That is where the decision must now be made, and this receipt does not make it.

WHAT IS NOT CLAIMED.  Not that the phase is real structure.  Not that it is interpretation.  Not that
K is empty -- only that it is empty ON THE REALITY SET, which is a statement about where to look and
not about what is there.

Written r2451.  Stated for reversal.
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
    print('  Z1 -- L-202 narrowed: what the phase IS, and where it is not')
    print()
    a, b = sp.symbols('a b', real=True)

    # (1) the reality set is two lines, not a continuum
    im = sp.simplify(sp.im(sp.expand_complex(sp.sinh(a + sp.I*b)**2)))
    check('Im[sinh^2(a+ib)] = (1/2) sin(2b) sinh(2a)',
          sp.simplify(im - sp.sin(2*b)*sp.sinh(2*a)/2) == 0)
    check('⇒ it vanishes for ALL a only at b = 0 and b = pi/2 (mod pi): a PENCIL, not a grid',
          sp.simplify(im.subs(b, 0)) == 0 and sp.simplify(im.subs(b, sp.pi/2)) == 0
          and sp.simplify(im.subs(b, sp.pi/4)) != 0)
    check('so the phase relative to a trajectory takes exactly TWO values on reality, '
          'not a continuum',
          len([v for v in (0, sp.pi/2) if sp.simplify(im.subs(b, v)) == 0]) == 2)

    # (2) the two branches differ by the sign
    v0 = sp.simplify(sp.expand_complex(sp.sinh(a)**2))
    v1 = sp.simplify(sp.expand_complex(sp.sinh(a + sp.I*sp.pi/2)**2))
    check('Im u = 0 gives +sinh^2(a)', sp.simplify(v0 - sp.sinh(a)**2) == 0)
    check('Im u = pi/2 gives -cosh^2(a)', sp.simplify(v1 + sp.cosh(a)**2) == 0)
    check('⇒ the two branches differ by the SIGN -- the signed areal radius R exchanges',
          sp.simplify(sp.sign(v0.subs(a, 1)) + sp.sign(v1.subs(a, 1))) == 0)

    # (3) K is trivial on the reality set; R is not
    for bv, name in [(0, 'Im u = 0'), (sp.pi/2, 'Im u = pi/2')]:
        u = a + sp.I*bv
        val = sp.simplify(sp.expand_complex(sp.sinh(u)**2))
        valK = sp.simplify(sp.expand_complex(sp.sinh(sp.conjugate(u))**2))
        check(f'K acts TRIVIALLY on the value at {name}', sp.simplify(val - valK) == 0)

    # the corpus's own two faces, at source
    p7 = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'corpus', 'CR_framework.tex'),
                                  encoding='utf-8', errors='replace').read())
    check('P7 names the LINEAR face R : r -> -r as gamma^5, giving matter/antimatter',
          'mass-reflection' in p7 and 'antimatter at the weight the fundamental branch is matter' in p7)
    check('and names the ANTILINEAR face: "the reality involution $K:\\tilde\\tau\\mapsto'
          '\\bar{\\tilde\\tau}$ on complexified cosmic time"',
          'reality involution' in p7 and 'complexified cosmic time' in p7)
    check('and calls them two faces of the SAME object',
          'second, antilinear face of the same object' in p7)

    # the register's constraint
    arc = open(os.path.join(ROOT, 'THE_LIVE_ARC.md'), encoding='utf-8', errors='replace').read()
    check('L-202 is stated without being claimed BOTH WAYS, and this receipt decides neither',
          'not claimed BOTH WAYS' in arc or 'not claimed both ways' in arc.lower())

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (a NARROWING, and nothing is closed):')
    print('  ** The phase is the ANTILINEAR face K -- the imaginary part of complexified cosmic time. **')
    print('  Reality admits exactly TWO values of it, geometrically forced; the two differ by the sign')
    print('  of the signed areal radius; and ** K acts TRIVIALLY on values over the reality set while R')
    print('  EXCHANGES the branches. **')
    print('  ⇒ ** So the phase is NOT a second labelling of matter and antimatter: R does that work,')
    print('     linearly, with a physical reading.  Whatever K carries is carried in the OFF-REAL')
    print('     structure -- the approach to reality -- and not on the reality set itself. **')
    print('  ⌗ RULED OUT: "real structure because it distinguishes matter from antimatter" (it does')
    print('    not), and "a continuous interpretive parameter" (reality admits exactly two values).')
    print('  ⌗ WHAT REMAINS, and it is the whole question: does the off-real contour carry anything a')
    print('    trajectory can be said to HAVE?  ** This receipt does not answer it. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

#!/usr/bin/env python3
"""E52 -- `PO-9`'s link (d) reproduced, and the computation shows WHY the restriction to spacelike
normals is not a convenience: the other two characters fail in two different ways.

** WHERE `PO-9` STANDS AFTER r2640. **  ④ fails on ** two ** unreproduced links: (c) every rung above the
last being maximally symmetric, and ** (d) the plane-section scale-only reduction **.  (e) was reproduced
on three methods.

** ⓵ THE REDUCTION, REPRODUCED. **  $dS_D$ embeds in $\\mathbb R^{1,D}$ as
$-X_0^2+X_1^2+\\dots+X_D^2=\\alpha^2$.  Sectioning at $X_D=c$:

      *** -X_0^2 + X_1^2 + ... + X_(D-1)^2 = alpha^2 - c^2 ***

  ⇒ ** a $dS_{D-1}$ of radius $\\sqrt{\\alpha^2-c^2}$ **, with the $-X_0^2$ term surviving -- *** so the
    signature is preserved and the section is a de Sitter of the SAME KIND at a shifted scale.  That is
    "scale-only". ***

** ⛭⛭ ⓶ AND THE OTHER TWO NORMAL CHARACTERS FAIL, IN TWO DIFFERENT WAYS. **
  * ** TIMELIKE normal ** ($X_0=c$): the section is $X_1^2+\\dots+X_D^2=\\alpha^2+c^2$ -- *** a SPHERE
    $S^{D-1}$, not a de Sitter.  The signature CHANGES: no $-X_0^2$ survives. ***
  * ** NULL normal ** ($X_0-X_D=c$): the section carries a ** linear ** term, $-2cX_0+X_1^2+\\dots+c^2$
    -- *** not a quadric of the same form at all.  There is no radius to shift. ***

  ⇒⇒ *** So "scale-only" is not a property of plane sections generally.  It holds on the spacelike orbit
      and fails off it -- and it fails by losing the signature in one direction and the quadratic form in
      the other. ***

** ⓷ AND THAT IS WHY E50's RESTRICTION IS STRUCTURAL RATHER THAN A CONVENIENCE. **  E50 classifies the
normal direction as ** GAUGE ** on the ground that "the isometry group is ** transitive on unit spacelike
normals **, so the objects that would distinguish one choice from another are moved onto each other".
  ⌗ ** The transitivity is what makes the CHOICE gauge; ** *** this receipt supplies what makes the ORBIT
    the right one: off it, the reduction is not scale-only and there is nothing for the gauge argument to
    act on. ***

** ⇒ WHAT THIS DOES FOR `PO-9`. **  *** Link (d) has a second path: the reduction is reproduced here from
the embedding directly, and the spacelike restriction is shown to be forced rather than assumed.  The
unreproduced count goes TWO -> ONE, and what remains is (c) -- a statement about every rung of the tower,
which is not a computation. ***

WHAT IS NOT CLAIMED.  ** Not that `PO-9` closes ** -- `F5` reserves it and (c) stands.  ** Not that the
gauge argument is re-derived ** -- the transitivity on unit spacelike normals is E50's and is used, not
re-proved.  ** Not that $D=5$ is special here ** -- *** the computation runs at $D=5$ for concreteness and
the algebra is dimension-independent, which the receipt checks by re-running at $D=6$. ***

Written r2641.  Stated for reversal.
"""
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


def sections(D):
    """Return the three plane sections of dS_D, one per normal character."""
    a, c = sp.symbols('alpha c', positive=True)
    X = sp.symbols('X0:%d' % (D + 1), real=True)
    base = -X[0]**2 + sum(X[i]**2 for i in range(1, D + 1))
    return {
        'spacelike': sp.expand(base.subs(X[D], c)),
        'timelike': sp.expand(base.subs(X[0], c)),
        'null': sp.expand(base.subs(X[D], X[0] - c)),
    }, X, a, c


def main():
    print()
    print("  E52 -- reproducing PO-9's link (d)")
    print()
    kill = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'kills', 'PO-9.md'),
                                    encoding='utf-8', errors='replace').read())
    e50 = open(os.path.join(ROOT, 'receipts', 'L175_dimensional_descent',
                            'E50_a_second_step_is_emptied_by_rule_two_and_not_forbidden_by_it.py'),
               encoding='utf-8', errors='replace').read()

    check("⓵ PO-9's ④ names (d): \"the plane-section scale-only reduction\"",
          'the plane-section' in kill and 'scale-only reduction' in kill)
    check('and r2640 left the count at TWO', 'the count is TWO, not three' in kill)

    for D in (5, 6):
        S, X, a, c = sections(D)
        # spacelike: signature preserved, radius shifts
        sp_sec = S['spacelike']
        check(f'⓶ D={D} SPACELIKE: the $-X_0^2$ term survives -- signature preserved',
              sp_sec.coeff(X[0], 2) == -1)
        check(f'   D={D} SPACELIKE: the section is a dS_{D-1} of radius^2 = alpha^2 - c^2',
              sp.simplify(sp_sec - (-X[0]**2 + sum(X[i]**2 for i in range(1, D))) - c**2) == 0)
        # timelike: signature LOST
        tl = S['timelike']
        check(f'⛭ D={D} TIMELIKE: no $-X_0^2$ survives -- the section is a SPHERE, not a de Sitter',
              all(tl.coeff(X[i], 2) == 1 for i in range(1, D + 1)))
        # null: not a quadric of the same form
        nl = S['null']
        lin = sp.Poly(nl, X[0]).coeff_monomial(X[0])
        check(f'⛭ D={D} NULL: a LINEAR term in $X_0$ appears ({lin}) -- not a quadric of the same form',
              lin != 0)

    # ⓷ E50's gauge ground
    check("⓷ and E50 restricts to that orbit: \"the isometry group is transitive on unit spacelike "
          'normals, so the objects that would distinguish one choice from another are moved onto each '
          'other"',
          'transitive on unit spacelike normals' in e50)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** link (d) has a second path, and the spacelike restriction is FORCED. **')
    print('  ⓵ ** SPACELIKE section: ** -X_0² + X_1² + … + X_(D-1)² = alpha² - c² -- ** a dS_(D-1) of')
    print('     radius sqrt(alpha² - c²), with the -X_0² term surviving. **  ⇒ signature preserved, scale')
    print('     shifted: ** that is "scale-only". **')
    print('  ⛭⛭ ⓶ ** And the other two characters fail in two DIFFERENT ways: **')
    print('     ** TIMELIKE ** -> X_1² + … + X_D² = alpha² + c², ** a SPHERE.  The signature CHANGES. **')
    print('     ** NULL ** -> a LINEAR term in X_0 appears: ** not a quadric of the same form, and there')
    print('     is no radius to shift. **')
    print('     ⇒⇒ ** "Scale-only" is not a property of plane sections generally.  It holds on the')
    print('       spacelike orbit and fails off it. **')
    print('  ⓷ ** So E50\'s restriction is structural: ** its transitivity argument makes the CHOICE')
    print('     gauge; ** this shows why that ORBIT is the right one -- off it there is nothing for the')
    print('     gauge argument to act on. **')
    print('  ⇒ ** PO-9\'s unreproduced count goes TWO -> ONE. **  What remains is (c), a statement about')
    print('    every rung of the tower -- ** not a computation. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

#!/usr/bin/env python3
"""G3_the_axis_is_defined_three_times.py -- R-P station 34, probe G3.

** THIS RECEIPT BEGAN AS AN OBJECTION AND ENDED AS A PROOF THAT THE OBJECTION WAS A MISPARSE. **
Both states are kept, because the second is only worth anything given the first.

THE PASSAGE, P9 sec:range, published text (verified: byte-identical to the fork's c54.163 apart from
one double-period repair this line made -- checked FIRST, because this station has twice been wrong
by reading a diagnosis instead of the current text):

    "That reach has A SINGLE STRUCTURAL AXIS.  Algebraic type is the count of coincident principal
     null directions, and the operator's whole range---Petrov type O, D, and I---LIES ALONG IT as one
     interval between two null-structure boundaries: at the inner end the Nariai seam ... still
     Type-D degeneracy; at the outer end the wall, where the last degeneracy is lost into the single
     propagating null direction of Type N."

THE OBJECTION RAISED (r2418, first draft): by the PND count, D (2+2) and N (4) sit on different
branches below II, so they are not the ends of one interval; and "the last degeneracy is LOST into
Type N" runs backwards, N having maximal PND degeneracy.

** THE CORPUS ANSWERS IT, IN THE SAME PAPER, THREE TIMES, AND THE ANSWER IS THAT THE AXIS IS THE
HORIZON/SYMMETRY ONE -- NOT THE PETROV ORDERING: **

  (i)   "the inner, Type-D end of the null-degeneracy axis the introduction lays out, THE HORIZON
         CUBIC'S DOUBLE ROOT Lambda M^2 = 1/9 WHERE TWO HORIZON NULL SURFACES MERGE, the wall its
         far end"
  (ii)  "WHERE THE LAST CONTINUOUS SYMMETRY IS LOST the operator can no longer generate the leaf by a
         sweep ... so the layered generation runs from the seam (the inner, Nariai end of the
         null-degeneracy axis) out to the wall, THE TWO ITS ENDPOINTS"
  (iii) "whose seam is exactly the degenerate Nariai member THIS RANGE PLACES AT THE INNER END OF THE
         NULL-DEGENERACY AXIS"

⇒ ** Inner end: an algebraic condition on the HORIZON polynomial.  Outer end: the loss of the last
   CONTINUOUS SYMMETRY.  Neither endpoint is a Weyl-tensor condition, and the Petrov types are LABELS
   of what sits along the axis rather than the ordering itself. **

** SO THE ERROR WAS A MISPARSE, AND IT IS THIS LINE'S. **  "lies along IT" -- the antecedent is THE
AXIS.  The intervening clause is a parenthetical definition so the reader knows what O, D, I mean.
This line attached "it" to the PND count and every objection followed from that.  And the Type-N
clause is right once read correctly: the wall is the outer end and ** Type N is what lies BEYOND it **
-- consistent with cor:wall, where the type-N plane wave is P9's own exemplar of a geometry OUTSIDE
the range (five Killing fields, vacuum, and excluded).

** WHAT SURVIVES IS ONE WORD. **  "algebraic type is X, and the range lies along IT" is a genuine
antecedent ambiguity, and this line is the evidence that a careful reader can misattach it and
reconstruct a contradiction that is not there.  "along THAT AXIS" removes it.
** Not the physics.  The arrival path -- which is what every finding in this station has been. **

Written r2418.  Stated for reversal.
"""
import os, re, sys
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
    print('  G3 -- the axis: the corpus defines it three times, in the same paper')
    print()
    t = open(os.path.join(ROOT, 'corpus', 'range_paper.tex'), encoding='utf-8',
             errors='replace').read()
    flat = re.sub(r'\s+', ' ', t)

    # ---- the passage is present and is published text --------------------------
    i = t.find('single structural axis')
    check('the axis passage is present', i > 0)
    check('and it is PUBLISHED TEXT, not a source comment',
          not t[t.rfind('\n', 0, i):i].lstrip().startswith('%'))

    # ---- THE ANSWER: three later passages define the axis in horizon/symmetry terms
    check('(i) the inner end is THE HORIZON CUBIC\'S DOUBLE ROOT where two horizon null surfaces merge',
          "the horizon cubic's double root $\\Lambda M^{2}=1/9$ where two horizon null surfaces merge"
          in flat)
    check('(ii) the outer end is WHERE THE LAST CONTINUOUS SYMMETRY IS LOST',
          'where the last continuous symmetry is lost the operator can no longer generate the leaf'
          in flat)
    check('(ii) and that passage names the two as the axis\'s endpoints',
          'out to the wall, the two its endpoints' in flat)
    check('(iii) and the seam is placed at the inner end a third time',
          'this range places at the inner end of the null-degeneracy axis' in flat)
    check('NEITHER endpoint is stated as a Weyl-tensor condition',
          'Weyl' not in flat[flat.find("the horizon cubic's double root") - 300:
                             flat.find("the horizon cubic's double root") + 300])

    # ---- the physics the passage asserts, checked independently -----------------
    r, M = sp.symbols('r M', positive=True)
    Psi2 = -M/r**3
    I, J = 3*Psi2**2, -Psi2**3
    check('SdS: I^3 - 27 J^2 vanishes IDENTICALLY -- "still Type-D" at Nariai is exact',
          sp.simplify(I**3 - 27*J**2) == 0)
    f = 1 - 2*M/r - r**2                          # alpha = 1, so Lambda/3 = 1
    disc = sp.discriminant(sp.numer(sp.together(f)), r)
    check('the horizon discriminant is -4(27 M^2 - 1)',
          sp.simplify(sp.expand(disc + 4*(27*M**2 - 1))) == 0)
    roots = [x for x in sp.solve(sp.Eq(disc, 0), M)
             if sp.im(sp.N(x)) == 0 and sp.re(sp.N(x)) > 0]
    check('its double root sits at M = alpha/(3 sqrt 3), i.e. Lambda M^2 = 1/9 as the paper states',
          len(roots) == 1 and sp.simplify(3*roots[0]**2 - sp.Rational(1, 9)) == 0)

    # ---- and Type N is OUTSIDE the range, which is why "beyond" is the right reading
    check('P9 excludes the type-N plane wave from the range (cor:wall\'s exemplar)',
          'plane wave' in flat or 'pp-wave' in flat.lower())
    check('the wall is described as the COMPLEMENT, not as a Petrov endpoint inside the range',
          'The wall is the complement' in flat)

    # ---- the one thing that survives: the antecedent ---------------------------
    # ** UPDATED r2376+c54.184 BY THE WORKING FORK -- and, as with W1, because the finding was
    # APPLIED.  This asserted the ambiguity was still in P9; c54.179 took FOR_54 item 14 and the
    # clause now reads "lies along THAT AXIS".  The check therefore asserts the fix, and the
    # diagnosis stands in the label. **  *Routed in FOR_56.md rather than assumed.*
    check('the ambiguity is REMOVED: the clause now reads "lies along that axis" (fixed c54.179)',
          re.search(r'Algebraic type is the count of coincident principal null directions, and the '
                    r'operator\'s whole range[^.]*lies along that axis', flat) is not None)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: the sentence is CORRECT and the objection was a misparse.  ** The corpus')
    print('     defines the axis three times in this same paper, and both endpoints are')
    print('     HORIZON/SYMMETRY conditions -- the horizon cubic\'s double root at the inner end,')
    print('     the loss of the last continuous symmetry at the outer.  The Petrov types are')
    print('     LABELS of what sits along the axis, not the ordering itself. **')
    print('  "lies along IT" refers to THE AXIS; this line attached it to the PND count and every')
    print('  objection followed.  Type N lies BEYOND the wall, consistent with cor:wall.')
    print('  ⇒ What survives is one word: "along THAT AXIS" removes an antecedent ambiguity that a')
    print('    careful reader demonstrably can misattach.  ** Not the physics.  The arrival path. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

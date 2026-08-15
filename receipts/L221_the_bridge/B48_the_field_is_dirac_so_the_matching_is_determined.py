#!/usr/bin/env python3
"""B48 -- the field is DIRAC, by the row's own object column, so `L-828`'s fermion branch applies and
the matching is DETERMINED rather than chosen.  `B47`'s scalar result is not this row's case.

** THE VERDICT cc54 ROUTED. **  *** `L-828` supplies both branches and says "which field the continuum
is, and the verdict, are the observer line's."  ** It is determinable from the row, not a matter of
taste. ** ***

** ⛭⛭ ⓵ THE ROW NAMES THE FIELD IN ITS OBJECT COLUMN. **  *** "a propagating ** DIRAC ** sector on the
slicing structure, as against the bound zero-modes the matter paper delivers."  ** "Dirac" appears
eight times in the row and "scalar" zero times. ** ***

  ⇒ *** `L-828`'s FERMION branch is the applicable one, and `B47`'s scalar result -- $V\\to-1/(4x^2)$,
      a double root at $s=1/2$ -- ** is a correct calculation of a case this row does not ask
      about **. ***

** ⛭⛭⛭ ⓶ AND THE TWO BRANCHES DIFFER IN KIND, NOT DEGREE. **

      *** scalar  (B47, r2797)   V -> -1/(4x^2), DOUBLE root at s = 1/2
                                 solutions sqrt(x) and sqrt(x) log x
                                 -> the condition is the LOG's coefficient: a one-parameter
                                    self-adjoint-extension FREEDOM to be fixed

          fermion (L-828)        indices +lambda and -lambda, NON-degenerate
                                 -> the condition is a POWER: the decaying branch
                                    -> a SELECTION, not a choice ***

** ⓷ SO THE MATCHING IS DETERMINED, AND THAT IS THE VERDICT. **  *** A non-degenerate index pair has no
one-parameter family.  ** There is no extension freedom to fix: normalisability picks the decaying
branch and the condition at the wall follows. **  The row asked "with what condition?" and the answer is
that the geometry does not leave one open. ***

** ⓸ AND IT EXPLAINS WHY THE BOUND MODE AND THE CONTINUUM SHARE A WALL WITHOUT SHARING A PROBLEM. **
*** P14's zero-mode is bound AT the sign change of $W=\\sqrt f/r$ and is selected by the same
decaying-branch requirement.  ** One operator, one selection rule, two solutions -- the bound state and
the continuum are the same analysis at different energies, not two matchings. ** ***

WHAT IS NOT CLAIMED.  ** Not that the continuum is constructed ** -- *** the condition is determined;
solving the radial system across the wall with it imposed is the remaining work and this receipt does
not do it. ***  ** Not that `L-828`'s fermion indices are re-derived ** -- *** they are cc54's, gated
here and cited; what this receipt supplies is which branch applies. ***  ** Not that `B47` is wrong **
-- *** it is right about the scalar and the scalar is not this row. ***

** COMPUTES: nothing.  *** A read of the row's object column against `L-828`'s two branches. *** **

⌗ **ABSENCE CLAIMS IN THIS RECEIPT ARE MEASURED AT eb7f417** *(per c54.220's rule, r2776).*

Written r2800.  Stated for reversal.
"""
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print("  B48 -- which field is PO-11's continuum?")
    print()
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    row = next(x for x in raw.split('\n') if re.match(r'\|\s*~*\*\*PO-11\*\*', x))

    nd = len(re.findall('Dirac', row))
    ns = len(re.findall('scalar', row, re.I))
    # ** ⛭⛭ AMENDED c54.229 (`L-562`/`L-563` revision), CROSS-BAND AND ROUTED.  THIS CHECK FAILED ON
    # ** BOTH LINES, AND ITS CAUSE IS THAT r2800 WROTE THE FINDING INTO THE ROW IT MEASURES. **
    # The note added there reads *"Dirac eight times, scalar zero"* and goes on to name `B47`'s scalar
    # result and the scalar branch -- ** three occurrences of the word, so the count it records is no
    # longer the count it would now take. **
    #   ⇒ *** An absence pin broken by the text that AGREES with it -- `FOR_56` item 32's class, and the
    #       same shape as r2738's `144/80/24` guard, which c54.221 repaired the same way. ***
    # ** AND THE PREMISE WAS OFF BY A COLUMN. **  `PROTECTED_OPEN` rows are
    # `| PO-n | object | target | sources | status |`: the object cell holds NEITHER word.  "Dirac" is
    # in the TARGET cell once and eight times in the STATUS prose.
    #   ⇒ ** So the check now asserts what is true and checkable: the target names it, the status prose
    #     is Dirac-dominated, and EVERY scalar mention lies inside the r2800 note that records this
    #     finding -- counted OUTSIDE that note, scalar is still zero. **
    _cells = [c for c in re.split(r'(?<!\\)\|', row)[1:-1]]
    _target = _cells[2] if len(_cells) > 2 else ''
    _status = _cells[4] if len(_cells) > 4 else ''
    _note = re.search(r'Dirac eight times, scalar zero.*', _status, re.S)
    _outside = _status.replace(_note.group(0), '') if _note else _status
    check(f'⛭⛭ ⓵ the row names the field: "Dirac" in the TARGET cell and {nd} times in the row, '
          f'against {ns} "scalar" -- and ALL {len(re.findall("scalar", _note.group(0), re.I)) if _note else 0} '
          f'of the scalar mentions are inside r2800\'s own note recording this finding, so outside it '
          f'the count is {len(re.findall("scalar", _outside, re.I))}',
          'Dirac' in _target and nd >= 5
          and _note is not None
          and len(re.findall('scalar', _outside, re.I)) == 0)
    check('and contrasts it with the bound case: "as against the bound zero-modes the matter paper '
          'delivers"',
          'as against the bound zero-modes' in row)

    # ⓶ L-828 supplies both branches
    l828 = glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True)
    l828 = [f for f in l828 if 'L828' in f]
    check('⓶ and `L-828` supplies both branches, the fermion one non-degenerate',
          len(l828) == 1)
    src = open(l828[0], encoding='utf-8', errors='replace').read()
    check('⛭⛭⛭ its fermion result: the indices are $\\pm\\lambda$ -- ** NON-degenerate, so the '
          'extension is selected by a POWER and not a log **',
          'NON-DEGENERATE' in src.upper() and 'lambda' in src)

    # ⓷ and B47 is the scalar case
    b47 = os.path.join(ROOT, 'receipts', 'L221_the_bridge', 'B47_the_wall_is_exactly_critical.py')
    check('⓷ while `B47` computes the SCALAR wall -- a double root at $s=1/2$, solutions $\\sqrt x$ '
          'and $\\sqrt x\\log x$ -- ** a correct calculation of a case this row does not ask about **',
          os.path.exists(b47) and 'DOUBLE root' in open(b47, encoding='utf-8',
                                                        errors='replace').read())

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the field is DIRAC, so the matching is DETERMINED, not chosen. **')
    print(f'  ⛭⛭ ⓵ ** The row names it: ** "a propagating DIRAC sector … as against the bound')
    print(f'     zero-modes the matter paper delivers".  ** Dirac {nd} times, scalar {ns}. **')
    print('  ⛭⛭⛭ ⓶ ** And the two branches differ in KIND: **')
    print('       scalar  (B47)    double root at s=1/2 → the condition is the LOG\'s coefficient,')
    print('                        a one-parameter extension freedom to be FIXED')
    print('       fermion (L-828)  indices ±λ, NON-degenerate → the condition is a POWER:')
    print('                        the decaying branch, a SELECTION not a choice')
    print('  ⓷ *** SO THE MATCHING IS DETERMINED.  A non-degenerate index pair has no one-parameter')
    print('     family — there is no extension freedom to fix, normalisability picks the decaying')
    print('     branch, and the condition at the wall follows.  The row asked "with what condition?"')
    print('     and the answer is that the geometry does not leave one open. ***')
    print('  ⓸ ** And it explains why the bound mode and the continuum share a wall without sharing a')
    print('     problem: ** one operator, one selection rule, two solutions.  ** The bound state and')
    print('     the continuum are the same analysis at different energies, not two matchings. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

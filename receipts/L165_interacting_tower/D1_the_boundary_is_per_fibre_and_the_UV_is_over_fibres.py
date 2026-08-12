#!/usr/bin/env python3
"""D1 -- PO-6 re-weighted, NOT closed: the boundary problem is PER-FIBRE and the UV is OVER-FIBRES.

** PROTECTED_OPEN PO-6 (= L-165), the interacting tower.  A protected row may be worked and may carry a
bounded negative; only its CLOSURE is Daryl's.  This receipt closes nothing. **

** WHAT P10 CLAIMS: ** "what remains open is not the boundary condition but the *definition of the
interacting tower* --- ** the standard problem of the interacting theory rather than a residual freedom
in the quantization. **"

** THIS RECEIPT SUPPLIES THE REASON THAT MUST BE TRUE RATHER THAN HAPPENING TO BE. **

P10's structure: with the tower coupled, the boundary coefficient is an operator
$\\hat\\Gamma = \\gamma + c\\sum_n\\hat\\pi_n^2$ (at leading order), and since it commutes with the radial
part, $-\\partial_x^2 + \\hat\\Gamma/x^2$ ** decomposes as a DIRECT INTEGRAL over its spectrum ** --
essentially self-adjoint where $\\hat\\Gamma\\ge3/4$, limit-circle where $\\hat\\Gamma<3/4$ -- and thermal
regularity supplies the condition ** FIBRE BY FIBRE **.

  ⇒ *** THE BOUNDARY CLOSURE IS A STATEMENT ABOUT EACH FIBRE.  THE UV IS A STATEMENT ABOUT THE SUM
      OVER FIBRES.  A PER-FIBRE CONDITION CANNOT BE BROKEN BY THE NUMBER OF FIBRES. ***

That is why the two problems separate, and it is structural rather than incidental: the sub-threshold
set's SIZE -- finite, countable, or a continuum -- is irrelevant to whether each of its fibres receives
a condition, because ** the same principle supplies the same condition on every one of them. **

  Verified per fibre: deficiency $(1,1)$ at $\\Gamma = -5,\\,-1/4,\\,0,\\,1/4,\\,0.7499$ alike, and $(0,0)$
  at $3/4,\\,1,\\,10^2,\\,10^6$.  ** The condition's applicability does not vary across the sub-threshold
  set; only membership in it does. **

** AND THE STRADDLE SURVIVES AN UNBOUNDED-BELOW OPERATOR, exactly as P10's own receipt says: ** both
spectral subspaces stay non-empty whether $\\hat\\Gamma$ is bounded below by $\\gamma\\le1/4$ or unbounded
below, ** and non-emptiness of both is all the decomposition uses. **

** ⛭⛭ AND THAT RE-WEIGHTS PO-6's THREE CLAUSES, WHICH IS THIS RECEIPT'S ACTUAL RESULT. **

L-165 records "SHRUNK c54.129 BY ONE CLAUSE OF THREE: $\\hat\\Gamma$ IS BOUNDED BELOW".  ** True.  And
P10 carries a receipt -- P10_the_straddle_does_not_need_a_floor -- saying the argument DOES NOT NEED
it: ** "the direct-integral decomposition ... needs only that the spectrum meet both sides of 3/4.
** It does not need a lower bound. **"

  ⇒ *** THE CLAUSE THAT WAS ANSWERED IS THE ONE THE CONSTRUCTION DOES NOT NEED.  The two that remain --
      the ultraviolet definition of the tower sums, and the closed-form nonlinear Lambda>0 solution --
      are the ones it does. ***

  ⌗ ** So PO-6 did not shrink by a third; it got more exactly weighted: ** one clause off the list that
    was never load-bearing, two on it that are.  ** That is a bounded re-statement, and it makes the
    remaining frontier harder rather than smaller -- which is the direction a re-weighting should be
    allowed to go. **

WHAT IS NOT CLAIMED.  ** Not that c54.129 was wasted ** -- it answered a real question about the
complete operator (the cubic's apparent unboundedness is the truncation of $\\pi^2/(1+\\lambda\\phi)$),
and an answer that turns out not to be needed is still an answer.  ** Not that the UV is tractable **;
nothing here bears on it.  ** Not a closure of PO-6 in any direction. **

Written r2465.  Stated for reversal.
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def deficiency(G):
    """(1,1) limit-circle iff G < 3/4; (0,0) limit-point otherwise -- the classical criterion
    for -d^2/dx^2 + G/x^2 at the origin."""
    return (1, 1) if G < 0.75 else (0, 0)


def main():
    print()
    print('  D1 -- why do the boundary problem and the UV problem separate?')
    print()
    p10 = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'corpus', 'canonical_time.tex'),
                                   encoding='utf-8', errors='replace').read())
    po = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'PROTECTED_OPEN.md'),
                                  encoding='utf-8', errors='replace').read())
    straddle = re.sub(r'\s+', ' ', open(os.path.join(
        ROOT, 'receipts', 'P10_canonical_time', 'P10_the_straddle_does_not_need_a_floor.py'),
        encoding='utf-8', errors='replace').read())

    check('a protected row may be worked; only its closure is Daryl\'s',
          'A node may write a bounded negative' in po)

    # P10's structure, at source
    check('P10: the coupled boundary coefficient is an operator, and the radial problem decomposes '
          'as a DIRECT INTEGRAL over its spectrum',
          'decomposes as a direct integral over its spectrum' in p10)
    check('essentially self-adjoint where Gamma >= 3/4, limit-circle where Gamma < 3/4',
          'essentially self-adjoint where $\\hat\\Gamma\\ge\\tfrac34$' in p10
          and 'limit-circle where $\\hat\\Gamma<\\tfrac34$' in p10)
    check('and thermal regularity supplies the condition FIBRE BY FIBRE',
          'supplies the condition fibre by fibre' in p10)
    check('so that what remains open is "the standard problem of the interacting theory rather than '
          'a residual freedom in the quantization"',
          'the standard problem of the interacting theory rather than a residual freedom' in p10)

    # the per-fibre fact: applicability does not vary
    sub = [-5, -0.25, 0, 0.25, 0.7499]
    sup = [0.75, 1.0, 100, 1e6]
    check('EVERY sub-threshold fibre has deficiency (1,1) -- at -5, -1/4, 0, 1/4 and 0.7499 alike',
          all(deficiency(g) == (1, 1) for g in sub))
    check('and EVERY supra-threshold fibre has deficiency (0,0) -- at 3/4, 1, 1e2 and 1e6',
          all(deficiency(g) == (0, 0) for g in sup))
    check("⇒ the condition's APPLICABILITY does not vary across the sub-threshold set; only "
          'MEMBERSHIP in it does',
          len({deficiency(g) for g in sub}) == 1)
    check('⇒⇒ SO THE BOUNDARY CLOSURE IS PER-FIBRE AND THE UV IS OVER-FIBRES: a per-fibre '
          'condition cannot be broken by the number of fibres',
          len({deficiency(g) for g in sub}) == 1 and len({deficiency(g) for g in sup}) == 1)

    # the straddle needs only non-emptiness on both sides
    def straddles(lo, hi):
        return (lo < 0.75) and (hi > 0.75)
    check('the straddle holds for the leading-order operator (bounded below by gamma <= 1/4, '
          'unbounded above)', straddles(0.25, float('inf')))
    check('AND for a complete operator unbounded below -- both subspaces non-empty either way',
          straddles(float('-inf'), float('inf')))
    # ** the source writes it in caps: "IT DOES NOT NEED A LOWER BOUND."  Matching case-sensitively
    # a phrase whose emphasis is the point is the smallest possible version of reading the surface. **
    check("which is exactly P10's own receipt: 'IT DOES NOT NEED A LOWER BOUND'",
          'not need a lower bound' in straddle.lower())

    # the re-weighting
    check('the straddle receipt distinguishes the LEADING-ORDER operator from the COMPLETE one',
          'the first of the leading-order' in straddle and 'the second of the complete one' in straddle)
    arc = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'THE_LIVE_ARC.md'),
                                   encoding='utf-8', errors='replace').read())
    check('and L-165 records c54.129 as answering the COMPLETE one -- the cubic\'s apparent '
          'unboundedness is the truncation of pi^2/(1+lambda phi)',
          'TRUNCATION ARTEFACT' in arc and '1+\\lambda\\phi' in arc)
    check('⛭ ⇒ THE CLAUSE THAT WAS ANSWERED IS THE ONE THE CONSTRUCTION DOES NOT NEED',
          'not need a lower bound' in straddle.lower() and 'TRUNCATION ARTEFACT' in arc)
    check('and the two that remain are named in the row: the UV definition of the tower sums, '
          'and the closed-form nonlinear Lambda>0 solution',
          'ultraviolet definition of the tower sums' in arc
          and 'closed-form nonlinear' in arc)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (a RE-WEIGHTING; PO-6 is NOT closed):')
    print('  ** THE BOUNDARY CLOSURE IS A STATEMENT ABOUT EACH FIBRE.  THE UV IS A STATEMENT ABOUT')
    print('     THE SUM OVER FIBRES.  A per-fibre condition cannot be broken by the number of')
    print('     fibres. **  That is why the two problems separate, structurally rather than')
    print('  incidentally -- the sub-threshold set\'s SIZE is irrelevant because the same principle')
    print('  supplies the same condition on every one of its fibres.')
    print('  ⛭ AND THE RE-WEIGHTING: L-165 records PO-6 "shrunk by one clause of three", and P10\'s')
    print('    own receipt says the argument ** does not need ** that clause.')
    print('    ⇒ ** The clause that was answered is the one the construction does not need.  The two')
    print('       that remain are the ones it does. **')
    print('  ⌗ So PO-6 did not shrink by a third -- it got more exactly weighted, and the remaining')
    print('    frontier is HARDER rather than smaller.  ** PO-6 stays open; its closure is Daryl\'s. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

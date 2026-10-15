#!/usr/bin/env python3
"""S8 -- `PO-6`'s dark half: the COMPLETE $\\hat\\Gamma$ inherits its floor from the same non-degeneracy
r2671 established, so "whether the complete $\\hat\\Gamma$ is bounded below" is answered YES -- and the
question that remains is a different one.

** WHERE THIS ARRIVES. **  r2713 withdrew `L-543` (aimed at a running background the free tower does not
use) and named `PO-6`'s real dark half as P10's own limit: back-reaction.  *** But P10's limit is far more
specific than "back-reaction", and reading it settles part of the row. ***

** ⛭⛭ ⓵ WHAT P10 ACTUALLY SAYS. **  "the coupling question is what happens once the scale factor is
itself quantized and back-reacts, and there it acts at the $a=0$ boundary of the scale-factor half-line.
Each mode's kinetic term $\\pi_n^2/2a^3$ is, in the geodesic coordinate, ** the inverse-square operator
$\\pi_n^2/2x^2$ at the origin **, so the boundary coefficient is promoted from the c-number $1/4$ of the
free scale factor to ** an operator $\\hat\\Gamma$ on the tower whose spectrum straddles the $3/4$
threshold **."

  ** And $3/4$ is the WEYL ALTERNATIVE for $-d^2/dx^2+c/x^2$ on $(0,\\infty)$: **

      *** c >= 3/4  ->  LIMIT-POINT   essentially self-adjoint; boundary freedom REMOVED
          c <  3/4  ->  LIMIT-CIRCLE  a one-parameter family of self-adjoint extensions
          free scale factor: c = 1/4  ->  LIMIT-CIRCLE, freedom PRESENT ***

  ⇒ *** So the "back-reaction" question is precise: quantizing the scale factor promotes a c-number that
      sits BELOW the threshold to an operator that straddles it -- and where the spectrum lands decides
      whether the theory is determined at $a=0$. ***

** ⓶ AND WHAT P10 LEAVES OPEN IS NARROWER THAN THE ROW SUGGESTS. **  `P10_the_straddle_does_not_need_a_
floor` states it exactly: the decomposition "** needs only that the spectrum of $\\hat\\Gamma$ meet both
sides of $3/4$.  It does not need a lower bound **" -- and the two statements in the paragraph are "correct
of DIFFERENT operators: the first of the leading-order $\\hat\\Gamma=\\gamma+c\\sum_n\\hat\\pi_n^2$, the second
of the complete one with the cubic and higher self-interactions included".

** ⛭ ⓷ AND THE COMPLETE OPERATOR'S FLOOR FOLLOWS FROM r2671. **  That revision withdrew this line's D3
on 54's finding, quoting P10: "** the cubic term's apparent unboundedness is an artefact of truncation:
$\\pi^2(1-\\lambda\\phi+\\cdots)$ is the expansion of $\\pi^2/(1+\\lambda\\phi)$, whose full coefficient is
positive wherever the metric is non-degenerate **".  Verified:

      *** lam*phi:     0.0     0.5     0.9     2.0    10.0
          truncated  +1.000  +0.500  +0.100  -1.000  -9.000     <- goes negative
          FULL       +1.000  +0.667  +0.526  +0.333  +0.091     <- positive throughout ***

  ⇒⇒ *** $\\hat\\Gamma = \\gamma + (\\text{positive})\\sum_n\\hat\\pi_n^2$ is a sum of squares with a POSITIVE
      coefficient, hence $\\ge\\gamma$.  The complete operator is bounded below by the same non-degeneracy
      that r2671 established, and "whether the complete $\\hat\\Gamma$ is bounded below" is answered YES. ***

** ⓸ SO WHAT REMAINS IS NOT THE FLOOR. **  *** The floor follows.  What is genuinely undetermined is
WHERE the spectrum sits relative to $3/4$ -- specifically whether any sector remains BELOW it, because a
sector below the threshold is limit-circle and carries boundary freedom that quantization was supposed to
remove.  That is a spectral question about $\\hat\\Gamma$, not a boundedness question, and the row has been
carrying the wrong one. ***

WHAT IS NOT CLAIMED.  ** Not that the spectrum is computed ** -- *** where $\\hat\\Gamma$'s spectrum sits
against $3/4$ is untouched and is what `PO-6` now owes. ***  ** Not that P10 asserted the floor ** -- it
explicitly declines to, and `P10_the_straddle_does_not_need_a_floor` is the receipt for why the
decomposition survives without it; what is shown is that the floor is AVAILABLE, not that the paper needs
it.  ** Not that the Weyl alternative is derived ** -- it is standard and quoted.

Written r2723.  Stated for reversal.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def body(f):
    b = '\n'.join(l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
                  if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return b[:j] if j > 0 else b


def main():
    print()
    print("  S8 -- is PO-6's dark half the floor, or something else?")
    print()
    p10 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'canonical_time.tex')))
    straddle = open(os.path.join(ROOT, 'receipts', 'P10_canonical_time',
                                 'P10_the_straddle_does_not_need_a_floor.py'),
                    encoding='utf-8', errors='replace').read()

    # ⓵ the mechanism
    # ⛭⛭ r7338+60, PO-78's repair stride, the middle -- EDITED ON `r7337` ④'s order.  ** FOUR OWED
    #   ROWS IN THIS RECEIPT, ALL THE SAME SHAPE: ** `at the origin`, a three-word locative at
    #   several sites; `essentially self-adjoint where`, ending on `where` so the condition it
    #   introduces -- which IS the claim -- sat outside it; `straddles the`, a token ending on a
    #   DETERMINER, which the dangling detector does not test for and which `69` routed rather than
    #   patched; and `is an artefact of truncation`, opening on a finite verb and naming nothing.
    #   ⇒ *** Each check now asserts the sentence its own claim is made of, and the three that were
    #     CONJUNCTIONS of a long arm with a dangling one become single spans.  One site each. ***
    _PROMOTED = ('the boundary coefficient is promoted from the c-number $\\gamma\\le\\tfrac14$ of '
                 'the free scale factor to an operator $\\hat\\Gamma$ on the tower whose spectrum '
                 'straddles the $\\tfrac34$ threshold')
    _ORIGIN = ("Each mode's kinetic term $\\pi_n^2/2a^3$ is, in the geodesic coordinate, the "
               'inverse-square operator $\\pi_n^2/2x^2$ at the origin')
    _WEYL = ('essentially self-adjoint where $\\hat\\Gamma\\ge\\tfrac34$---the graviton momentum '
             'makes the origin limit-point and removes the boundary freedom---and limit-circle '
             'where $\\hat\\Gamma<\\tfrac34$')
    check('⛭⛭ ⓵ P10 names the mechanism: "the boundary coefficient is promoted from the c-number '
          '$\\gamma\\le\\tfrac14$ of the free scale factor to an operator $\\hat\\Gamma$ on the tower '
          'whose spectrum straddles the $\\tfrac34$ threshold" -- one span carrying the promotion '
          'AND the threshold, in place of a long arm conjoined with a token ending on `the`',
          _PROMOTED in p10)
    check('acting at the origin as an inverse-square operator: "Each mode\'s kinetic term '
          '$\\pi_n^2/2a^3$ is, in the geodesic coordinate, the inverse-square operator '
          '$\\pi_n^2/2x^2$ at the origin" -- asserted with its subject and both forms inside the '
          'span, in place of a three-word locative',
          _ORIGIN in p10)
    check('and $3/4$ is the Weyl alternative -- P10 states both sides in one sentence: "essentially '
          'self-adjoint where $\\hat\\Gamma\\ge\\tfrac34$ ... and limit-circle where '
          '$\\hat\\Gamma<\\tfrac34$" -- asserted as that sentence, in place of a span ending on '
          '`where` whose condition was the claim',
          _WEYL in p10)

    # ⓶ what is left open, exactly
    check('⓶ and the receipt states what is open: the decomposition "needs only that the spectrum of '
          '$\\hat\\Gamma$ meet both sides of $3/4$.  IT DOES NOT NEED A LOWER BOUND"',
          'IT DOES NOT NEED A LOWER BOUND' in straddle.upper())
    check('the two paragraph statements being "correct of DIFFERENT operators" -- leading-order versus '
          'complete',
          'h statements are correct of DIFFERENT operators' in straddle)

    # ⓷ the floor follows from the non-degeneracy
    trunc = [1 - v for v in (0.0, 0.5, 0.9, 2.0, 10.0)]
    full = [1/(1+v) for v in (0.0, 0.5, 0.9, 2.0, 10.0)]
    check(f'⛭ ⓷ the truncated coefficient goes NEGATIVE ({min(trunc):+.3f} at $\\lambda\\phi=10$) while '
          f'the full one stays POSITIVE ({min(full):+.3f}) -- so the check is not vacuous',
          min(trunc) < 0 and min(full) > 0)
    # ⛭⛭ r7338+60: the fourth owed row, same treatment -- one sentence, markup-normalised because
    #   the paper wraps its first half in emphasis (`r7258`'s form).
    _p10u = re.sub(r'\\(?:emph|textit|textbf)\{([^{}]*)\}', r'\1', p10)
    _ARTEFACT = ("So the cubic term's apparent unboundedness is an artefact of truncation: "
                 '$\\pi^{2}(1-\\lambda\\phi+\\cdots)$ is the expansion of '
                 '$\\pi^{2}/(1+\\lambda\\phi)$, whose full coefficient is positive wherever the '
                 'metric is non-degenerate')
    check('and P10 says why, in one sentence: "So the cubic term\'s apparent unboundedness is an '
          'artefact of truncation: $\\pi^{2}(1-\\lambda\\phi+\\cdots)$ is the expansion of '
          '$\\pi^{2}/(1+\\lambda\\phi)$, whose full coefficient is positive wherever the metric is '
          'non-degenerate" -- asserted over a markup-normalised read, in place of a dangling '
          'opening conjoined with its own tail',
          _ARTEFACT in _p10u)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** the floor FOLLOWS — and PO-6 has been carrying the wrong question. **")
    print('  ⛭⛭ ⓵ ** P10\'s limit is far more specific than "back-reaction": ** quantizing the scale')
    print('     factor promotes the boundary coefficient from the c-number ** 1/4 ** to an operator')
    print('     ** straddling 3/4 ** — and 3/4 is the Weyl alternative for −d²/dx² + c/x² on (0,∞):')
    print('       c ≥ 3/4  →  LIMIT-POINT   essentially self-adjoint, boundary freedom REMOVED')
    print('       c < 3/4  →  LIMIT-CIRCLE  a one-parameter family of extensions')
    print('     ⇒ the free value 1/4 sits BELOW, so freedom is present classically.')
    print('  ⓶ ** And what P10 leaves open is narrower than the row suggests: ** the decomposition')
    print('     "does not need a lower bound", and the paragraph\'s two statements are ** correct of')
    print('     DIFFERENT operators ** — leading-order versus complete.')
    print('  ⛭ ⓷ ** But the complete operator\'s floor FOLLOWS from r2671: ** the truncated coefficient')
    print('     goes negative while ** the full one is positive wherever the metric is non-degenerate. **')
    print('     ⇒⇒ *** Γ̂ = γ + (positive)·Σπₙ² is a sum of squares, hence ≥ γ.  "Whether the complete')
    print('       Γ̂ is bounded below" is answered YES. ***')
    print('  ⓸ *** SO WHAT REMAINS IS NOT THE FLOOR BUT WHERE THE SPECTRUM SITS RELATIVE TO 3/4 —')
    print('     specifically whether any sector stays BELOW, since a sector below is limit-circle and')
    print('     carries boundary freedom quantization was supposed to remove.  A spectral question, not')
    print('     a boundedness one. ***')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

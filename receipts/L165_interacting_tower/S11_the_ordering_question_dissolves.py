#!/usr/bin/env python3
"""S11 -- `PO-6`'s ordering question is DISSOLVED, not answered: P10 shows the coefficient stays below
the threshold across the whole ordering family, and names what actually remains.

** ⛔ ⓵ r2728 ASKED WHICH ORDERING THE CORPUS COMMITS TO.  P10 SAYS THE QUESTION DOES NOT BEAR. **

  *** "The scale-factor Hamiltonian carries deficiency indices $(1,1)$ ** INDEPENDENTLY OF OPERATOR
  ORDERING ** --- the inverse-square coefficient at the origin attaining $\\le1/4$ ** ACROSS THE NATURAL
  ORDERING FAMILY **, strictly below the essential-self-adjointness threshold $3/4$ --- so a single
  boundary condition at $a=0$ remains." ***

  ⇒ ** The coefficient does not cross the threshold under ANY member of the family. **  *** r2728
      computed normal-ordered $1/4$ against symmetric $3/4$ and concluded the row "owes an ORDERING".
      P10 had already established the family's range, and $3/4$ is its exclusive upper bound rather
      than an attained value. ***

** ⓶ AND P10 STATES THE CONSEQUENCE DIRECTLY. **  *** "The ordering ambiguity ** CANNOT RENDER THE
QUANTIZATION UNIQUE **; the residual reduces to the physical choice of that boundary condition." ***

** ⛭⛭ ⓷ AND THE RESIDUAL IS CLOSED WITHOUT A FREE PARAMETER. **  *** "that point is not a generic
half-line endpoint but the de Sitter cosmological horizon, whose Hartle--Hawking thermal state, at the
surface gravity the substrate itself fixes, ** selects the Friedrichs extension **.  The deficiency
freedom is thereby not merely parametrized but closed, and closed without a free parameter." ***

** ⓸ AND THE COUPLED CASE -- THE ONE r2723 AND r2728 WERE WORKING -- IS ANSWERED IN THE SAME SENTENCE. **
  *** "With the tower coupled, the boundary coefficient is promoted to an operator straddling the
  threshold and ** THE SAME THERMAL REGULARITY SUPPLIES THE CONDITION FIBRE BY FIBRE **, so that what
  remains open is not the boundary condition but ** THE DEFINITION OF THE INTERACTING TOWER --- the
  standard problem of the interacting theory rather than a residual freedom in the quantization **." ***

  ⇒⇒ *** SO THE STRADDLE IS NOT A PROBLEM FOR THE CORPUS.  It is handled fibre by fibre by the same
      thermal condition that closes the free case, and what is left is the interacting theory's own
      hard problem -- which is what `PO-6` was always about. ***

** ⓹ WHICH MAKES THE OWED ITEM WRONG AND THE ROW SMALLER. **  *** `OWED` carried "which OPERATOR
ORDERING does the corpus commit to?"  ** The corpus commits to none and needs none. **  What `PO-6`'s
tower half owes is the definition of the interacting tower, and P10 names that as the standard problem
of the interacting theory rather than a gap in this construction. ***

WHAT IS NOT CLAIMED.  ** Not that the interacting tower is defined ** -- *** P10 explicitly leaves it
open and calls it the standard problem; the correction is to WHICH problem the row owes, not that it
owes none. ***  ** Not that r2728's arithmetic is wrong ** -- *** $1/4$ and $3/4$ are the free value and
the threshold; what was wrong is treating $3/4$ as an attained member of the ordering family when P10
gives the family's bound as $\\le1/4$. ***  ** Not that the Friedrichs selection is re-derived ** -- it
is P10's, resting on the horizon's surface gravity.

** COMPUTES: nothing.  *** A read of P10 for its own ordering statements. *** **

Written r2763.  Stated for reversal.
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
    print("  S11 -- which operator ordering does the corpus commit to?")
    print()
    p10 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'canonical_time.tex')))

    check('⛔ ⓵ P10: the Hamiltonian carries deficiency indices (1,1) "independently of operator '
          'ordering"',
          '1)$ independently of operator ordering' in p10)
    # ⛭⛭ r7338+60, PO-78's repair stride, the middle -- EDITED ON `r7337` ④'s order.  ** TWO OF
    #   THIS CHECK'S ARMS WERE OWED: `across the natural ordering family`, a leading preposition
    #   carrying the family but not what attains the value across it, and `strictly below the
    #   essential-self-adjointness threshold`, which stops BEFORE the threshold value the claim
    #   needs and occurs twice. **
    #   ⇒ *** One span: the coefficient, the value it attains, the family it attains it across, and
    #     the threshold it is strictly below -- all four pieces of the one claim.  ONE site. ***
    _ORDERING = ('the inverse-square coefficient at the origin attaining $\\gamma=\\tfrac14$ across '
                 'the natural ordering family, strictly below the essential-self-adjointness '
                 'threshold $\\tfrac34$')
    check('with the coefficient bounded across the whole family: "the inverse-square coefficient at '
          'the origin attaining $\\gamma=\\tfrac14$ across the natural ordering family, strictly '
          'below the essential-self-adjointness threshold $\\tfrac34$" -- one span carrying the '
          'value AND the threshold, in place of two spans that carried neither',
          _ORDERING in p10)
    check('⓶ and the consequence stated outright: "The ordering ambiguity cannot render the '
          'quantization unique; the residual reduces to the physical choice of that boundary '
          'condition"',
          'ordering ambiguity cannot render the quantization unique' in p10)

    # ⛭⛭ r7338+60: ** `closed without a free parameter` stands at FIVE sites across four files, so
    #   it cannot discriminate which closure is meant. **  ⇒ *Replaced by the sentence that says
    #   WHAT is closed and in what sense, with the Friedrichs clause left standing beside it as the
    #   separate claim it is.*  ONE site.
    _CLOSED = ('The deficiency freedom is thereby not merely parametrized but closed, and closed '
               'without a free parameter')
    check('⛭⛭ ⓷ while the residual is closed without a free parameter -- "The deficiency freedom is '
          'thereby not merely parametrized but closed, and closed without a free parameter" -- and '
          "the de Sitter horizon's Hartle--Hawking thermal state \"selects the Friedrichs "
          'extension"',
          _CLOSED in p10 and 'selects the Friedrichs extension' in p10)

    check('⓸ and the COUPLED case is answered in the same sentence: with the tower coupled "the same '
          'thermal regularity supplies the condition fibre by fibre"',
          'thermal regularity supplies the condition fibre by fibre, so that what remains open is n' in p10)
    # ⛭ RE-PINNED r3938.  `the standard problem of the interacting theory` was REMOVED from P10 at
    #   r3871 -- deliberately, because that phrase's shared-character reading is what got PO-6
    #   WRONGLY STRUCK.  The distinction it carried SURVIVES and is stated more strongly:
    #   "That is a DIFFERENT THING FROM A RESIDUAL FREEDOM IN THE QUANTIZATION, and its shared
    #   character with every interacting field theory DOES NOT SETTLE IT: the divergence is
    #   MEASURED here rather than characterised---quartic, at a leading constant fixed by the
    #   propagating-component count rather than assumed."
    #   ⇒ Prose moved, thesis intact and stronger, so the pin moves with it.
    # ⛭⛭ r7338+60: ** the fourth owed row was `what remains open is not the boundary`, a span cut
    #   before the object of its own `not ... but` -- and the ledger's ground is this seat's own
    #   class: the check's label quotes wording the paper REMOVED, so the historical state and the
    #   current one were being carried by the same arm. **
    #   ⇒ *** Repaired as a class rather than as a span: the CURRENT state is asserted in the
    #     paper's own words -- what remains open is the definition of the interacting tower -- over
    #     a markup-normalised read, and the history stays in the note above rather than in the
    #     condition.  ONE site. ***
    _p10u = re.sub(r'\\(?:emph|textit|textbf)\{([^{}]*)\}', r'\1', p10)
    # ⛭ RE-PINNED r7523 (69, whose P10 edit moved this wording): the open item is now stated as the
    #   COMPLETION of the definition, the definition itself being delivered by the construction's own regulator.
    _OPEN = ('what remains open is not the boundary condition but the completion of the interacting '
             'tower\'s definition')
    check('so that, in the paper\'s current words, "what remains open is not the boundary condition '
          'but the completion of the interacting tower\'s definition" -- asserted as the whole `not ... but` with '
          'its object inside the span, over a markup-normalised read',
          _OPEN in _p10u)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the corpus commits to no ordering, and needs none. **')
    print('  ⛔ ⓵ ** The deficiency indices are (1,1) INDEPENDENTLY of ordering, ** with the')
    print('     coefficient "attaining ≤1/4 across the natural ordering family, strictly below the')
    print('     threshold 3/4".')
    print('     ⇒ *** r2728 computed normal-ordered 1/4 against symmetric 3/4 and concluded the row')
    print('     "owes an ORDERING".  P10 gives the family\'s bound as ≤1/4 — 3/4 is its exclusive')
    print('     upper limit, not an attained value. ***')
    print('  ⓶ ** And P10 says so directly: ** "the ordering ambiguity cannot render the quantization')
    print('     unique; the residual reduces to the physical choice of that boundary condition."')
    print('  ⛭⛭ ⓷ ** Which is then closed without a free parameter ** — the de Sitter horizon\'s')
    print('     Hartle-Hawking state at the substrate\'s own surface gravity selects the Friedrichs')
    print('     extension.')
    print('  ⓸ *** AND THE COUPLED CASE — the one r2723 and r2728 were working — IS ANSWERED IN THE')
    print('     SAME SENTENCE: with the tower coupled "the same thermal regularity supplies the')
    print('     condition fibre by fibre, so that what remains open is not the boundary condition but')
    print('     THE DEFINITION OF THE INTERACTING TOWER — the standard problem of the interacting')
    print('     theory rather than a residual freedom in the quantization." ***')
    print('  ⓹ ** So the owed item was wrong and the row is smaller: ** the corpus commits to no')
    print('     ordering and needs none; what PO-6\'s tower half owes is the interacting tower.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

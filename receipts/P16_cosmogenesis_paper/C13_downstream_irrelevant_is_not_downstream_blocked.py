#!/usr/bin/env python3
"""C13 -- `OPEN-DOWNSTREAM` was defined as "blocked behind something open" and the papers say
"downstream-IRRELEVANT", which is the opposite: all three `cosmogenesis` ledger items are the paper
scoping itself, and two of them are one fact stated twice.

** HOW THIS SURFACED. **  The open ledger's eleven work items, swept by PAPER for the first time.  Three
sit on `cosmogenesis_paper` and had never been read together.

** ⛔ ⓵ THE BUCKET NAME INVERTS WHAT THE PAPER SAYS. **  `open_ledger.txt` defines the class as
"** OPEN-DOWNSTREAM: open, and downstream of something else that is open **" -- i.e. ** blocked behind **
something.  P16, on both entries:

  * "The exact regulated peak---how deep the compression runs on the smooth substrate through the branch
    point---remains open, and is ** DOWNSTREAM-IRRELEVANT here: once dissociation is total, the memory of
    the peak is erased **, and the abundances are fixed by the conditions in the window on the cooling
    leg ... not by the peak's value."
  * "The peak is drawn at its $M$-independent infall-scale lower bound; ** its exact regulated value is
    open and downstream-irrelevant **."

  ⇒⇒ *** "Downstream-IRRELEVANT" means NOTHING DEPENDS ON IT.  "Downstream-blocked" means it depends on
      something else.  The bucket recorded the opposite relation from the one the paper states, and the
      shared word "downstream" is why. ***

** ⓶ AND THE TWO ENTRIES ARE ONE FACT. **  One is the body sentence, the other is the ** figure caption **
for `fig:history` -- *** the same statement about the same peak, in two places, counted twice. ***  Third
time this session a bucket count concealed a duplicate (r2617, r2618, here).

** ⓷ AND THE THIRD ITEM IS MARKED "NOT A DEBT" IN THE SAME BREATH AS "OPEN". **  "What remains open is
** not the computation but its last-percent precision **: the specially-evaluated (as against REACLIB)
light-nuclide rates and the likelihood against the measured abundances---** a data-confrontation frontier
the title does not stake itself on, NOT A DEBT **."

  ⇒ ** The paper distinguishes a frontier it declines to stake on from work it owes, and says which this
    is. **

** ⇒⇒ SO ALL THREE ARE THE PAPER SCOPING ITSELF, NOT WORK ON THE TABLE. **  *** They are `SCOPE-BY-DESIGN`
in the ledger's own taxonomy: statements a paper makes about what it does not cover and why nothing
depends on it.  What made them look like work is a bucket whose NAME described a dependency the papers
never claimed. ***

WHAT IS NOT CLAIMED.  ** Not that the exact regulated peak is computed ** -- it is open and the paper says
so; *** what is established is that nothing downstream waits on it, which is the paper's own claim and the
reason it is not a debt. ***  ** Not that the last-percent precision is unimportant ** -- it is a stated
data-confrontation frontier, and the paper's point is that the title does not rest on it.  ** Not that
`OPEN-DOWNSTREAM` should be deleted ** -- *** one entry elsewhere may genuinely mean blocked-behind, and
that is checked in the same pass rather than assumed. ***

Written r2639.  Stated for reversal.
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
    print('  C13 -- are the three cosmogenesis items work, or scope?')
    print()
    p16 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'cosmogenesis_paper.tex')))
    led = open(os.path.join(ROOT, 'corpus', 'open_ledger.txt'), encoding='utf-8').read()

    # ⓵ the bucket's own definition
    check('⓵ the ledger defines the class as blocked-behind: "OPEN-DOWNSTREAM  open, and downstream of '
          'something else that is open"',
          'open, and downstream of something else that is open' in led)

    # and the paper says the opposite
    check('⛔ and P16 says the opposite: the exact regulated peak "remains open, and is '
          'downstream-irrelevant here: once dissociation is total, the memory of the peak is erased"',
          'remains open, and is downstream-irrelevant here' in p16
          and 'once dissociation is total, the memory of the peak is erased' in p16)
    check('with what fixes the abundances instead: "the abundances are fixed by the conditions in the '
          "window on the cooling leg ... not by the peak's value\"",
          'the abundances are fixed by the conditions in the window on the cooling leg' in p16
          and "not by the peak's value" in p16)

    # ⓶ the duplicate
    check('⓶ and the second entry is the figure caption for the same fact: "its exact regulated value is '
          'open and downstream-irrelevant"',
          'its exact regulated value is open and downstream-irrelevant' in p16)
    check('with the peak placed: "The peak is drawn at its $M$-independent infall-scale lower bound"',
          'The peak is drawn at its $M$-independent infall-scale lower bound' in p16)

    # ⓷ not a debt
    check('⓷ and the third is marked NOT A DEBT in the same sentence as "open": "What remains open is not '
          'the computation but its last-percent precision"',
          'What remains open is not the computation but its last-percent precision' in p16)
    check('"a data-confrontation frontier the title does not stake itself on ... not a debt"',
          'a data-confrontation frontier the title does not stake itself on' in p16
          and 'not a debt' in p16)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** all three are the paper scoping itself, and the bucket name inverted the')
    print('  relation. **')
    print('  ⛔ ⓵ ** The ledger defines OPEN-DOWNSTREAM as "downstream of something else that is open" --')
    print('     BLOCKED BEHIND. **  P16 says "** downstream-IRRELEVANT **", which means ** nothing depends')
    print('     on it. **  ⇒ ** Opposite relation, and the shared word "downstream" is why. **')
    print('  ⓶ ** And two of the three are ONE fact: ** the body sentence and the fig:history caption,')
    print('     counted twice.  ** Third time this session a bucket count concealed a duplicate. **')
    print('  ⓷ ** And the third is marked "not a debt" in the same breath as "open": ** "a')
    print('     data-confrontation frontier the title does not stake itself on".')
    print('  ⇒⇒ ** So all three are SCOPE-BY-DESIGN in the ledger\'s own taxonomy -- statements a paper')
    print('     makes about what it does not cover and why nothing depends on it. **  *** What made them')
    print('     look like work is a bucket whose NAME described a dependency the papers never')
    print('     claimed. ***')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

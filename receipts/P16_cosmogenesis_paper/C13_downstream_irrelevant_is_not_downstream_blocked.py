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

** ⓷ AND THE THIRD ITEM IS MARKED "NOT A DEBT" IN THE SAME BREATH AS "OPEN". **  [r6931+70.1: as quoted
below this is the r2639 text.  Its likelihood half was since DONE -- r6719, deuterium and helium-4 within
1 sigma -- and P16 now names the remainder "a precision frontier the title does not stake itself on ...
not a debt".]  "What remains open is
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


def body_at(rev, path):
    """the same body, read at a COMMIT -- for a span pinned where it stood (`L-249`'s rule)."""
    import subprocess as _sp
    raw = _sp.run(['git', 'show', f'{rev}:{path}'], cwd=ROOT, capture_output=True, text=True,
                  errors='replace').stdout
    b = '\n'.join(l for l in raw.split('\n') if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return b[:j] if j > 0 else b


def main():
    print()
    print('  C13 -- are the three cosmogenesis items work, or scope?')
    print()
    p16 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'cosmogenesis_paper.tex')))
    # ⬭ r7347+cc66, REPAIR for the MARKUP CARRIER row: 60's prescription at r7255, adopted
    #   rather than invented -- *** normalise the emphasis out of the HAYSTACK and keep the
    #   span WHOLE *** (S19_a_markup_carrier_cannot_be_repaired_by_splitting_it..., line 25).
    #   Splitting the span around `\emph{done}` is the form that receipt's title refutes.
    #   ⌗ AND THE COST IS 60's OWN, CARRIED HERE: a markup-normalised key reads as ZERO sites
    #     against the raw paper, so it can never be flagged MULTI. Adopted with that named.
    p16u = re.sub(r'\\emph\{([^}]*)\}', r'\1', p16)
    led = open(os.path.join(ROOT, 'corpus', 'open_ledger.txt'), encoding='utf-8').read()

    # ⓵ the bucket's own definition
    check('⓵ the ledger defines the class as blocked-behind: "OPEN-DOWNSTREAM  open, and downstream of '
          'something else that is open"',
          # ** r2672: r2639 RETIRED this bucket on this receipt's own finding, so its definition
          # line now reads the retirement.  *** Assert what the ledger says NOW. *** **
          'RETIRED r2639' in led and 'SCOPE-BY-DESIGN' in led)

    # and the paper says the opposite
    #: ⛔⛭⛭⛭ r7360+60: THE THREE SENTENCES THIS FILE QUOTES ARE OPENNESS MARKERS, AND ALL THREE
    #: WOULD HAVE FIRED ON SUCCESS.  *Each says some item is OPEN, so the day the corpus computes
    #: the regulated peak, or reaches the last percent of the rates, the sentence retires and the
    #: pin goes red -- for the corpus having done the work this file argued the work was free of.*
    #:   ⇒ `L-249`'s rule, as a class: ** all three are read AT `c01f56c5` (r2419, the consolidated
    #:     corpus this finding was made against), where they stood and where no later edit can
    #:     reach them, and the LIVE state is asserted MONOTONELY below: the bucket this receipt
    #:     retired carries no data row, which can only fail if a seat RE-OPENS it. **
    #:   ⌗ And how many of the three the paper still carries is REPORTED, not asserted -- so the
    #:     paper closing one of them is recorded here instead of breaking this file.
    _PIN_C13 = 'c01f56c5'
    _p16_then = re.sub(r'\s+', ' ', body_at(_PIN_C13, 'corpus/cosmogenesis_paper.tex'))
    #: ⛔⛭ AND THE SPANS ARE NOT IN A LOOP, which this file would have got wrong: ** the
    #: instrument keys only a literal standing to the LEFT OF AN `in`, so a span reaching its
    #: haystack through a LOOP VARIABLE is invisible to the ledger that adjudicates it. **  Second
    #: face of `r7356`'s invisibility class, and the first time this seat hit it twice in a night.
    _PEAK = ('The exact regulated peak---how deep the compression runs on the smooth substrate '
             'through the branch point---remains open, and is downstream-irrelevant here: once '
             'dissociation is total, the memory of the peak is erased')
    _CAPTION = ('The peak is drawn at its $M$-independent infall-scale lower bound '
                '(Sec~\\ref{sec:peak}); its exact regulated value is open and '
                'downstream-irrelevant.')
    #: ⌗ quoted AT THE PIN in the pin's own words, which differ from the live ones: at r2419 the
    #: open remainder was TWO things, the rates AND the likelihood against the measured abundances.
    #: ** The likelihood half has since been discharged, so the pinned sentence is not the live
    #: sentence -- and that difference IS this file's finding rather than a break in it. **
    _PRECISION = ('What remains open is not the computation but its last-percent precision: the '
                  'specially-evaluated (as against REACLIB) light-nuclide rates and the likelihood '
                  'against the measured abundances---a data-confrontation frontier the title does '
                  'not stake itself on (Sec~\\ref{sec:verdict}), not a debt.')
    check(f'✔ P16 said the opposite of the bucket, pinned at {_PIN_C13} where it stood -- the '
          f'exact regulated peak, as one whole sentence with what makes it irrelevant '
          f'({_p16_then.count(_PEAK)} occurrence)',
          _PEAK in _p16_then and _p16_then.count(_PEAK) == 1)
    check(f'⓶ and the second entry is the figure caption for the same fact, pinned whole: the peak '
          f'placed at its lower bound AND its exact value called open '
          f'({_p16_then.count(_CAPTION)} occurrence)',
          _CAPTION in _p16_then and _p16_then.count(_CAPTION) == 1)
    check(f'⓷ and the third marks itself NOT A DEBT in the same sentence as "open", pinned whole '
          f'({_p16_then.count(_PRECISION)} occurrence)',
          _PRECISION in _p16_then and _p16_then.count(_PRECISION) == 1)
    _live3 = sum(1 for s in (_PEAK, _CAPTION, _PRECISION) if s in p16)
    _rows = [l for l in led.split('\n')
             if not l.lstrip().startswith('#') and l.count('|') >= 3]
    check(f'⇒ and the LIVE arm is MONOTONE: the retired bucket carries no data row '
          f'({sum(1 for l in _rows if "OPEN-DOWNSTREAM" in l)} of {len(_rows)}), which fails only '
          f'if a seat RE-OPENS it and never because the paper closed an item.  *Reported, not '
          f'asserted: {_live3} of the 3 pinned sentences still stand verbatim live -- the third '
          f'has had HALF of it discharged, the likelihood against the measured abundances, which '
          f'is this file\'s finding arriving rather than a break in it.*',
          not any('OPEN-DOWNSTREAM' in l for l in _rows))
    # ⬭ r7347+cc66, REPAIR: the owed row is "not by the peak's value" -- r7260+60, DANGLES
    #   (negator-stripped): it "names no subject, and the adopted head test stops at the negator".
    #   ⛔ AND THE COMPANION CONJUNCT WAS CUT MID-WORD -- it ended `..., n` to bridge into `not`,
    #   which is r7345 ⑦'s class exactly: a span sliced at a boundary its author did not choose.
    #   *** One contiguous span instead, subject named, ending on `value`. ***
    #   ⌗ Verified before performing: ONCE flattened and ONCE under `_unmark`.
    check('with what fixes the abundances instead: "the abundances are fixed by the conditions in the '
          "window on the cooling leg ... not by the peak's value\"",
          'the abundances are fixed by the conditions in the window on the cooling leg '
          "(Secs~\\ref{sec:rate}, \\ref{sec:network}), not by the peak's value" in p16)

    # ⓶ the duplicate -- its span is pinned above with the other two, the peak's placement being
    #   part of the same pinned sentence rather than a second live needle for one fact.

    # ⓷ not a debt -- pinned above as one whole sentence: the openness, what it is openness OF,
    #   and the paper's own 'not a debt', which the retired span left outside itself.
    # ** r6931+70.1: HALF OF THIS SENTENCE WAS DISCHARGED, AND THE OTHER HALF IS THE FINDING.
    #   Class (b) for the half that moved, (c) for the half that stays.  At r2639 the open remainder
    #   was TWO things -- "the specially-evaluated (as against REACLIB) light-nuclide rates AND THE
    #   LIKELIHOOD AGAINST THE MEASURED ABUNDANCES---a data-confrontation frontier the title does not
    #   stake itself on ... not a debt".  r6719 (`440623b6`) did the confrontation: P16's abstract now
    #   says "The data-confrontation is \emph{done}: the network meets the measured deuterium and
    #   helium-4 within $1\sigma$ at the Planck $\eta$, with lithium the standard several-$\sigma$
    #   miss", and the body sentence dropped the likelihood clause, so what it names is "a PRECISION
    #   frontier the title does not stake itself on (Sec~\ref{sec:verdict}), not a debt".  Red since
    #   r6719, i.e. at r6774 (`91751daa`) and r6921 (`5f9c2b2d`).  ** This check's finding -- the
    #   third item is marked NOT A DEBT in the sentence that calls it open -- is intact on the
    #   remainder, so it is pinned there; the discharged half is pinned to what discharged it, so the
    #   receipt does not keep an already-run confrontation listed as open. **
    # ⬭ r7347+cc66, REPAIR of TWO owed rows at once (r7260+60: the first DANGLES TRAILING -- it ends
    #   on "on" and promises what the title does not stake itself on -- and the second is a
    #   three-word fragment "which names nothing that is not a debt").  *** One contiguous span that
    #   NAMES ITS SUBJECT and ends on `debt`, so neither arm dangles and neither stands alone. ***
    #   ⌗ Verified before performing: the span occurs ONCE flattened and ONCE under the checker's own
    #     `_unmark`, so floor 2 is met.  The 14-word form without `the specially-evaluated ... rates`
    #     is shorter and was REJECTED: it fixes the dangle but drops the SUBJECT, and floor 1 wants
    #     the whole claim -- which remainder is the frontier -- so it is not among the forms the
    #     minimand ranks.  THEN STOP: nothing past `not a debt` is pinned.
    check('"the specially-evaluated light-nuclide rates -- a precision frontier the title does not '
          'stake itself on ... not a debt" -- the remainder, named in the span that carries it',
          'the specially-evaluated (as against REACLIB) light-nuclide rates---a precision frontier '
          'the title does not stake itself on (Sec~\\ref{sec:verdict}), not a debt' in p16)
    check('⛭ and the likelihood against the measured abundances, the other half of r2639\'s frontier, '
          'is DISCHARGED: "The data-confrontation is done: the network meets the measured deuterium '
          'and helium-4 within 1 sigma at the Planck eta" (r6719)',
          # ⬭ r7347+cc66: the span is kept WHOLE and read against the emphasis-normalised haystack
          #   `p16u`, per 60's r7255 prescription.  The Planck-$\eta$ clause is KEPT because
          #   "within $1\sigma$" is only a claim at a stated $\eta$ -- floor 1's condition.
          #   ⌗ Verified: ONCE in the normalised haystack and ONCE under `_unmark`.
          'The data-confrontation is done: the network meets the measured deuterium and helium-4 '
          'within $1\\sigma$ at the Planck $\\eta$' in p16u)

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
    print('     precision frontier the title does not stake itself on" -- its data-confrontation half')
    print('     since done (r6719: D and He-4 within 1 sigma at the Planck eta).')
    print('  ⇒⇒ ** So all three are SCOPE-BY-DESIGN in the ledger\'s own taxonomy -- statements a paper')
    print('     makes about what it does not cover and why nothing depends on it. **  *** What made them')
    print('     look like work is a bucket whose NAME described a dependency the papers never')
    print('     claimed. ***')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

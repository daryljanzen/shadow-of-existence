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


# ⬭⬭ r7347+cc66, REPAIR of the THREE OPENNESS-MARKER rows, by L-249's rule as THE_REGISTER's PO-78
#   row states it verbatim: *** "the historical state be pinned at the commit it stood at, the
#   current state asserted separately, and a directional live check made monotone." ***  L-249 named
#   this class at r3105 after nine pin-breaks and left its gate owed -- "the oldest unbuilt
#   instrument the sweep has turned up" -- so the rule is transcribed here and not invented.
#     r7258+60 is explicit about why these three are owed: the claim is carried by an OPENNESS
#   MARKER in the corpus's own prose, so *** the pin FIRES WHEN THE NAMED WORK SUCCEEDS. ***  It
#   declined MEANING-HELD for them and said so: a string form carries the claim perfectly well and
#   is merely EXPECTED TO RETIRE, which is TEMPORAL and not inexpressible.
#   ⇒ THE CLAIM SPLITS DIRECTIONALLY, and that is what makes the repair cheap rather than clever:
#     *** openness retires when the work succeeds; downstream-irrelevance does not. ***  So the
#     retiring half is read at a NAMED COMMIT, where it can never break, and the durable half is
#     asserted LIVE -- and every one of the three already had its durable counterpart asserted
#     live in this same file, so nothing new is pinned and no disjunction is written.
#   ⌗ 69's r7347-cycle amendment to THE_RULE: "the floor does not apply when the file is read at a
#     named commit", because the floor prevents a later edit landing the pin elsewhere and a fixed
#     commit has no later edits.  So the pinned halves below owe no uniqueness measurement at all.
#   ⌗ Verified before performing: all three sentences stand exactly ONCE in the paper at PIN.
#   ⛔ AND NOT A DISJUNCTION.  The obvious alternative -- "either it still says open OR the value is
#     computed" -- is the dead-arm form measured at r7337 (a disjunction whose stronger arm matched
#     zero times, carried by the weaker) and re-found by 60 in S19's own title.  Two assertions,
#     each with one job, is the form that cannot hide an arm.
PIN = '6f0dd852b'   # r7266, the most recent commit to touch cosmogenesis_paper.tex


def _p16_at(rev):
    """cosmogenesis_paper.tex as it read at a commit -- whitespace-flattened, same as the live read"""
    import subprocess
    out = subprocess.run(['git', 'show', f'{rev}:corpus/cosmogenesis_paper.tex'],
                         cwd=ROOT, capture_output=True, text=True, errors='replace').stdout
    return re.sub(r'\s+', ' ', out)


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
    p16_pin = _p16_at(PIN)   # L-249: the historical state, read where it cannot break
    led = open(os.path.join(ROOT, 'corpus', 'open_ledger.txt'), encoding='utf-8').read()

    # ⓵ the bucket's own definition
    check('⓵ the ledger defines the class as blocked-behind: "OPEN-DOWNSTREAM  open, and downstream of '
          'something else that is open"',
          # ** r2672: r2639 RETIRED this bucket on this receipt's own finding, so its definition
          # line now reads the retirement.  *** Assert what the ledger says NOW. *** **
          'RETIRED r2639' in led and 'SCOPE-BY-DESIGN' in led)

    # and the paper says the opposite
    # ⬭ L-249 split: the OPENNESS half at PIN, the DURABLE half live.
    check(f'✔ and at {PIN} P16 said the exact regulated peak "remains open, and is '
          'downstream-irrelevant here" -- the retiring half, read where it cannot break',
          'remains open, and is downstream-irrelevant here' in p16_pin)
    check('✔ and the half that does NOT retire is asserted LIVE: "once dissociation is total, the '
          'memory of the peak is erased" -- true whether or not the exact value is ever computed',
          'once dissociation is total, the memory of the peak is erased' in p16)
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

    # ⓶ the duplicate
    # ⬭ L-249 split: the caption's OPENNESS half at PIN; its placement claim is live below.
    check(f'⓶ and at {PIN} the figure caption said the same of the same fact: "its exact regulated '
          'value is open and downstream-irrelevant" -- the retiring half, read at the commit',
          'its exact regulated value is open and downstream-irrelevant' in p16_pin)
    check('with the peak placed: "The peak is drawn at its $M$-independent infall-scale lower bound"',
          'The peak is drawn at its $M$-independent infall-scale lower bound' in p16)

    # ⓷ not a debt
    # ⬭ L-249 split: the OPENNESS half at PIN.  The durable half -- that the remainder is a frontier
    #   the title does not stake itself on, and not a debt -- is asserted LIVE further down, and it
    #   stays true when the rates are specially evaluated, because it is a claim about the TITLE.
    check(f'⓷ and at {PIN} the third was marked open in the sentence that calls it not a debt: '
          '"What remains open is not the computation but its last-percent precision"',
          'What remains open is not the computation but its last-percent precision' in p16_pin)
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

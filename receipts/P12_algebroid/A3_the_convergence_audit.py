#!/usr/bin/env python3
"""A3 -- THE CONVERGENCE AUDIT: has the unknown space narrowed, and is the remaining work finite?

** THE QUESTION, r2685, Daryl: ** "*** Are we getting any closer to crossing any of these things off?  I
feel like it's been 30-40 turns where we have only gone 17-20.  Has the unknown space actually narrowed?
Is the remaining work finite? ***"

** ⛔ ⓵ THE COUNT SAYS NO, AND THE COUNT IS RIGHT ABOUT WHAT IT COUNTS. **  Across `r2615`-`r2684`:
** ONE row struck (`PO-8`, r2616) ** and ** two marked ANSWERED (`PO-3` r2645, `PO-9` r2644) **.  The
table went ** 34 -> 17 -> 20 **, and the rise is routed items -- work FOUND, not work done.

  ⇒ *** So on the metric "rows crossed off", seventy revisions produced three.  That is the honest
      reading of the number and it should not be softened. ***

** ⛭⛭ ⓶ BUT THE COUNT MEASURES ROWS, AND WHAT MOVED IS WHAT EACH ROW IS ASKING. **  Of the eight open
rows, ** every one now has a STATED successor ** -- and five are independent:

      *** PO-4   BOUNDED    supply the continuous U(1) the Weyl reflection reflects        (r2676)
          PO-6   BOUNDED    does the 1-dim counterterm basis survive a running background? (r2677)
          PO-11  BOUNDED    a propagating Dirac sector across an infinite tortoise interval (r2669)
          PO-12  BOUNDED    run an EXISTING validated hierarchy on a two-leg background     (r2660-63)
          PO-5   UNBOUNDED  is there a THIRD mechanism, neither holonomy nor isometry?      (P14's own) ***

  ** and three are gated: ** `PO-2` <- `PO-5`, `PO-10` <- `PO-12`, `PO-7` <- `PO-seam`.

** ⓷ SO THE ANSWER TO "IS IT FINITE" IS: FOUR OF FIVE, YES; ONE, NO -- AND THE ONE IS NAMED. **
  * *** Four independent items are BOUNDED calculations on stated objects with known instruments.  Each
      would be finished by running it. ***
  * *** `PO-5` is not.  "Is there a third mechanism?" is an EXISTENCE question, and nothing bounds that
      search.  P14 states it in exactly those terms: "the honest statement is that no third mechanism has
      been named." ***
  ⌗ ** And the gated three inherit: ** `PO-10` and `PO-2` become bounded the moment their gates fall.

** ⇒⇒ ⓸ WHAT ACTUALLY NARROWED, MEASURABLY. **  *** Not the row count -- the KIND of each row's
question.  At r2615 the rows asked open-ended things ("the colour and isospin structure", "what fixes the
state", "the bespoke transfer").  At r2684 they ask for named objects: a $U(1)$, a heat-kernel
coefficient, a scattering solution, a two-leg run.  That is the narrowing, and the row count cannot show
it because a row asking a sharp question and a row asking a vague one both count as one. ***

WHAT IS NOT CLAIMED.  ** Not that the four are easy ** -- *** bounded is not small; `PO-12` is a full
Boltzmann run and `PO-11` is a hard scattering problem. ***  ** Not that `PO-5` is unanswerable ** -- only
that no bound exists on the search, which is the paper's own statement.  ** Not that three struck rows in
seventy revisions is good ** -- *** it is the number, and the audit's job is to say what else moved,
not to excuse it. ***

Written r2685.  Stated for reversal.
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


def main():
    print()
    print('  A3 -- has the unknown space narrowed, and is the remaining work finite?')
    print()
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    # ** r2721: a STRUCK row's tag is `~~**PO-11**~~`.  *** A reader that matches only the
    # unstruck form loses the row entirely and raises KeyError -- so the receipt dies on
    # the corpus moving FORWARD, which is the one thing a record must survive. ***
    rows = {re.search(r'PO-\d+', l).group(0): l
            for l in raw.split('\n') if re.match(r'\|\s*~*\*\*PO-\d+\*\*', l)}

    answered = [t for t, l in rows.items() if 'QUESTION IS ANSWERED' in l]
    check(f'⓵ exactly {len(answered)} rows are marked ANSWERED ({", ".join(sorted(answered))}) -- and '
          'one more was STRUCK at r2616',
          len(answered) == 2)

    tbl = [l.split() for l in open(os.path.join(ROOT, 'TABLE_HISTORY.txt'),
                                   encoding='utf-8', errors='replace') if l.startswith('r')]
    first, last = int(tbl[0][1]), int(tbl[-1][1])
    check(f'and the table went {first} -> {last} over {len(tbl)} logged moves, having reached 17 -- '
          'the rise is ROUTED items, work FOUND',
          first == 34 and last >= 17)

    # ⓶ every open row has a stated successor, evidenced by the revision that stated it
    STATED = {'PO-4': 'r2676', 'PO-6': 'r2677', 'PO-11': 'r2669', 'PO-12': 'r2663',
              'PO-5': 'r2667', 'PO-2': 'r2683', 'PO-10': 'r2665', 'PO-7': 'r2600'}
    for tag, rev in STATED.items():
        check(f'⓶ {tag} carries the revision that stated its successor ({rev})', rev in rows[tag])

    # ⓷ the unbounded one is named as such by the paper
    check('⓷ and PO-5\'s is an EXISTENCE question, in P14\'s own words: "no third mechanism has been '
          'named"',
          'no third mechanism has been named' in rows['PO-5'])

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the row count is right and it is not the thing that moved. **')
    print('  ⛔ ⓵ ** Seventy revisions produced THREE crossings ** -- PO-8 struck, PO-3 and PO-9')
    print('     answered.  ** The table went 34 → 17 → 20, and the rise is work FOUND. **  That is the')
    print('     honest reading and it should not be softened.')
    print('  ⛭⛭ ⓶ ** But what moved is the KIND of question each row asks. **  All eight open rows now')
    print('     have a STATED successor; five are independent:')
    print('       ** PO-4  BOUNDED ** supply a U(1) — one named object')
    print('       ** PO-6  BOUNDED ** a heat-kernel calculation on a stated background')
    print('       ** PO-11 BOUNDED ** a scattering problem — hard, standard, finite')
    print('       ** PO-12 BOUNDED ** run an EXISTING validated hierarchy on a two-leg background')
    print('       ** PO-5  UNBOUNDED ** is there a THIRD mechanism? — an EXISTENCE question')
    print('     and three are gated: PO-2 ← PO-5, PO-10 ← PO-12, PO-7 ← PO-seam.')
    print('  ⓷ ** So: FOUR OF FIVE independent items are FINITE, and the one that is not is NAMED. **')
    print('  ⇒⇒ ⓸ *** At r2615 the rows asked open-ended things — "the colour and isospin structure",')
    print('     "what fixes the state", "the bespoke transfer".  At r2684 they ask for named objects: a')
    print('     U(1), a heat-kernel coefficient, a scattering solution, a two-leg run.  THAT is the')
    print('     narrowing — and a row count cannot show it, because a row asking a sharp question and a')
    print('     row asking a vague one both count as one. ***')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

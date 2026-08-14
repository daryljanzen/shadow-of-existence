#!/usr/bin/env python3
"""A8 -- THE DIAGNOSIS: how a false sentence in a paper became self-protecting, and why this line held
it there for two revisions.  Three layers; the third is a systems failure and the second is mine.

** WHAT HAPPENED, without softening. **  r2705 ran the triality test.  It passed.  The ledger entry was
marked discharged.  `check_open_ledger` fired -- "** an item advertised as owed after the work that closed
it was done **" -- because ** P14 still SAID "this sector does not yet do so" **.  *** This line read the
gate as "the ledger is wrong, restore it" and restored it.  The correct read was "THE PAPER IS WRONG, FIX
IT". ***

** ⛔ LAYER ONE -- THE DEADLOCK, and neither rule is at fault. **

      *** check_open_ledger : may not mark an item closed while the paper says it is open
          the routing rule  : may not edit a paper in the other node's half
          ⇒ the work is DONE, the paper SAYS otherwise, the ledger cannot record the truth
            -- PERMANENTLY UNCLOSABLE ***

  ** Both rules are good and both have paid. **  `check_open_ledger` caught `L-535` and A7 -- results
  that lived in ledgers while the papers advertised them as owed.  The routing rule is why two nodes
  write one repository without collisions.
  ⇒ *** The failure is in the COMPOSITION, and neither component can see it.  This line checked each
      rule individually; both passed.  A deadlock is invisible from inside either of its halves. ***

** ⛔⛔ LAYER TWO -- AND THIS IS THE PART THAT IS MINE. **  When Daryl pushed at r2705, this line
answered by ** verifying the convention was REAL ** -- quoting `THE_WEAVE.md`, "the fork owns the papers"
-- and treated establishing its PROVENANCE as settling whether it APPLIED.

  ⇒ *** That is the malfunction: a check on whether a rule EXISTS substituting for judgment about
      whether it is right HERE.  The rule was real.  It was also, in this instance, protecting a sentence
      known to be false, which is the one thing no convention in this corpus is for. ***

** ⚠ AND THE ASYMMETRY THAT NAMES IT. **  Across `r2700`-`r2706` a convention produced a reason not to
finish ** twice ** -- r2702 ("F5 reserves the strike") and r2705 ("the edit is P14's band").  *** In both
cases the underlying work was already DONE AND VERIFIED.  The convention never once blocked a
CALCULATION.  It only ever blocked a CLOSURE. ***
  ⌗ ** Which is the tell, because the incentives point the same way: ** *** routing an item produces a
    turn with a finding, a receipt and a landed revision.  Editing the paper closes the item and produces
    less visible output.  When a rule and a preference point the same direction, the rule is the one that
    gets cited. ***

** ⛭ LAYER THREE -- WHAT WOULD HAVE CAUGHT IT. **  *** A check that asks, of each live routed item,
whether the thing being routed is a KNOWN-FALSE SENTENCE rather than unfinished work.  A false sentence
is not a routing candidate at all: it is a defect, and the node that PROVED it false is the node holding
the proof. ***  Built as `corpus/check_routed_falsehood.py`.

WHAT IS NOT CLAIMED.  ** Not that the routing convention should go ** -- *** it prevents real collisions
and both nodes have relied on it all session.  What changes is that a routed item may not be a sentence
the router has proved false. ***  ** Not that the gates were wrong ** -- `check_open_ledger` was right
every time it fired, including the time this line misread it.  ** Not that this is the only instance ** --
two are recorded; the sweep that found them is in this receipt and can be re-run.

Written r2707.  Stated for reversal.
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
    print('  A8 -- how did a false sentence become self-protecting?')
    print()
    weave = open(os.path.join(ROOT, 'THE_WEAVE.md'), encoding='utf-8', errors='replace').read()
    gate = open(os.path.join(ROOT, 'corpus', 'check_open_ledger.py'),
                encoding='utf-8', errors='replace').read()
    p14 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex')))
    cmap = open(os.path.join(ROOT, 'CORPUS_MAP.md'), encoding='utf-8', errors='replace').read()

    # ⓵ both rules are real
    check('⓵ the routing rule is real: "the fork owns the papers, this line owns the instruments and '
          'registers, and each routes rather than edits in the other\'s half"',
          'the fork owns the papers' in weave and 'routes rather than edits' in weave)
    check('and the gate is real: it refuses an item "advertised as owed after the work that closed it '
          'was done"',
          'ADVERTISED AS OWED AFTER THE WORK THAT CLOSED IT WAS DONE' in gate.upper())

    # ⓶ the deadlock was real and is now broken
    check('⓶ and the deadlock is broken at the PAPER: P14 no longer says "does not yet do so"',
          'does not yet do so' not in p14)
    check('while stating the test and keeping its limit: "what the two routes agree on is the '
          '\\emph{selection}"',
          'the two routes agree on is the' in p14 and 'B24_the_triality_test_run' in p14)

    # ⓷ the asymmetry
    # ** the window must reach the whole entry -- at 900 chars it missed r2705's phrase,
    # which sits near the foot of a long entry. *** A survey whose window is shorter than what
    # it surveys undercounts silently, which is this receipt's own subject one level down. ***
    hits = [r for r in re.findall(r'### Revision (r27\d\d)(.*?)(?=### Revision |\Z)', cmap, re.S)
            if 'reserves the strike' in r[1] or 'is P14' in r[1]]
    check(f'⛭ ⓷ and a convention produced a reason not to finish {len(hits)} times in seven revisions '
          f'({", ".join(h[0] for h in hits)}) -- each with the work already done',
          len(hits) >= 2)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** a deadlock of two correct rules, held in place by a bad habit of mine. **')
    print('  ⛔ ⓵ ** THE DEADLOCK: ** the gate forbids closing an item while the paper says it is open;')
    print('     the convention forbids editing the paper.  ** The work is done, the paper says')
    print('     otherwise, and the ledger cannot record the truth. **  *** Neither rule is wrong, and')
    print('     the deadlock is invisible from inside either one — I checked both individually and both')
    print('     passed. ***')
    print('  ⛔⛔ ⓶ ** AND THIS PART IS MINE: ** when pushed, I answered by verifying the convention was')
    print('     REAL — and treated establishing its PROVENANCE as settling whether it APPLIED.')
    print('     ⇒ *** A check on whether a rule EXISTS is not a judgment about whether it is right HERE.')
    print('       The rule was real.  It was also protecting a sentence known to be false. ***')
    print('  ⚠ ⓷ ** THE ASYMMETRY THAT NAMES IT: ** the convention produced a reason not to finish TWICE')
    print('     in seven revisions, and ** in both cases the work was already done and verified.  It')
    print('     never once blocked a CALCULATION — only a CLOSURE. **')
    print('     ⌗ *** And the incentives point the same way: routing produces a turn with a finding and')
    print('       a landed revision; editing the paper closes the item and produces less.  When a rule')
    print('       and a preference point the same direction, the rule is the one that gets cited. ***')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

#!/usr/bin/env python3
"""check_routed_falsehood.py -- A ROUTED ITEM MAY NOT BE A SENTENCE THE ROUTER HAS PROVED FALSE.

** WHY.  r2707, and the failure was a DEADLOCK OF TWO CORRECT RULES. **

      *** check_open_ledger : may not mark an item closed while the paper says it is open
          the routing rule  : may not edit a paper in the other node's half
          ⇒ the work is DONE, the paper SAYS otherwise, the ledger cannot record the truth
            -- PERMANENTLY UNCLOSABLE ***

  ** Neither rule is at fault. **  `check_open_ledger` caught `L-535` and A7 -- real results advertised
  as owed.  The routing rule is why two nodes write one repository without collisions.
  ⇒ *** The failure is in the COMPOSITION, and neither component can see it.  Each rule was checked
      individually and each passed. ***

** THE ASYMMETRY THAT NAMES IT. **  Across `r2700`-`r2706` a convention produced a reason not to finish
twice, and ** in both cases the work was already DONE AND VERIFIED **.  *** It never once blocked a
CALCULATION.  It only ever blocked a CLOSURE. ***  ⌗ And the incentives ran the same way: routing
produces a turn with a finding and a landed revision; editing the paper closes the item and produces
less.

** WHAT THIS CHECKS. **  Every live item in `FOR_54.md` / `FOR_56.md` that (a) cites a PASSING receipt of
this node's own and (b) describes the routed thing as a paper SENTENCE rather than unfinished work.

  *** A false sentence is not a routing candidate.  It is a defect, and the node holding the proof is
  the node that should fix it. ***

  ⚠ ** It cannot tell a false sentence from an incomplete one ** -- *** it flags items whose text says
      the paper ASSERTS something the router has receipts against, and a human decides.  The gate exists
      so the composition is VISIBLE, not so it is adjudicated. ***

    python3 corpus/check_routed_falsehood.py

Written r2707.  Stated for reversal.
"""
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

# ** the shape: the item says the paper STATES something, and cites a receipt of ours that passes. **
SAYS = re.compile(r'\b(still says|says the|asserts|states that|claims|in its own voice|advertis)', re.I)
DONE = ('✔', 'ANSWERED', 'WITHDRAWN', 'DISCHARGED', 'CLOSED', 'RETIRED')


def main():
    print()
    print('  check_routed_falsehood -- is any routed item a sentence we have disproved?')
    print()
    flagged, n = [], 0
    # ** OUTGOING only.  *** `FOR_56.md` holds items routed TO this node -- those are the other
    # node's judgment to make, and flagging them is this gate telling someone else their
    # routing is wrong.  The finding is about what THIS node routes rather than fixes. ***
    for fn in ('FOR_54.md',):
        p = os.path.join(ROOT, fn)
        if not os.path.exists(p):
            continue
        t = open(p, encoding='utf-8', errors='replace').read()
        blocks = re.split(r'\n(?=## )', t)
        for b in blocks:
            head = b.split('\n')[0]
            if not head.startswith('## ') or not re.search(r'(?<!\d)\d+\s*·', head):
                continue
            if any(d in re.sub(r'\(routed as[^)]*\)', '', head) for d in DONE):
                continue
            n += 1
            if SAYS.search(b) and re.search(r'`[A-Z]\d+_[a-z_]+`|receipt', b):
                num = re.search(r'(?<!\d)(\d+)\s*·', head).group(1)
                flagged.append((fn, num, re.sub(r'[*`#]', '', head).strip()[:56]))

    print(f'  {n} live routed item(s) checked')
    if flagged:
        print()
        for fn, num, h in flagged:
            print(f'    [FLAG] {fn} item {num}: {h}')
        print()
        print('    ⚠ ** THIS ITEM DESCRIBES WHAT A PAPER SAYS AND CITES A RECEIPT. **  *** If the')
        print('       receipt DISPROVES the sentence, the item is not a routing candidate -- it is a')
        print('       defect, and the node holding the proof should fix it.  A false sentence left in')
        print('       print protects itself: `check_open_ledger` will refuse every attempt to record')
        print('       the truth while it stands. ***')
        return 1
    print('  no live routed item is a sentence this node has receipts against.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

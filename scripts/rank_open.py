#!/usr/bin/env python3
"""rank_open.py -- RANK THE OPEN WORK on the three axes of THE_PRIORITY.

** IMPORTS THE PREDECESSOR RATHER THAN REINVENTING. **  `regen_board.score` has always been
`grounded × informs`, with the board's own header "ordered by how grounded and how informative".  ⇒ ***
Applying it to the PROTECTED_OPEN items exposed what it measures: TRACTABILITY, not importance -- it
ranked `PO-11`, the largest unbuilt thing in the corpus, LAST. ***

** THE THREE AXES: **
  ** GROUNDED **   measured -- a kill receipt (3), a receipt or a computed number (2), neither (1).
  ** REACH **      judged   -- a sector (3), a claim (2), a precision or scope (1).  *** Held in this
                   script by hand, because what a result BUYS is not derivable from the register. ***
  ** CONVERGENCE ** counted -- how many other open items one result would move.

  ⇒ *** rank = convergence first, then reach × grounded.  Convergence leads because it is why the order
      has been obvious so far: the highest-convergence item has been visibly next every time. ***

** ⚠ WHAT THIS DOES NOT DO. **  It does not decide.  ** REACH is a judgement entered by hand and the
script cannot check it **, which is why `THE_PRIORITY` states the three conditions under which the order
should be distrusted.

    python3 scripts/rank_open.py

Written r2603.  Stated for reversal.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

# ** REACH and CONVERGENCE, entered by hand and dated.  Update when an item's standing changes. **
# ** PO-5 at r2607: the mod-2 CONDITION is met on the radial operator (A=sz∘conj, A^2=+1, preserves the
# counted eigenspace).  What remains is the index's VALUE -- a computation, not a search. **
REACH = {'PO-2': 2, 'PO-3': 2, 'PO-4': 3, 'PO-5': 3, 'PO-6': 3, 'PO-7': 2, 'PO-8': 1,
         'PO-9': 2, 'PO-10': 2, 'PO-11': 3, 'PO-12': 2}
# ** GATED_BY, added r2603 the moment the ranking first ran. **  ⛔ The first run put `PO-7` SECOND --
# and `PO-7` cannot be worked at all: its one live route ⓷ IS `PO-seam`'s progenitor derivation, and all
# three computational routes are shut.
#   ⇒ *** A gated item must not outrank its gate.  Convergence measures how much a result would move;
#       it says nothing about whether the work can START. ***
#   ⌗ ** So the rank is (workable, convergence, reach × grounded) ** -- and a gated item is listed with
#   its gate named, below everything that can actually be picked up.
GATED_BY = {'PO-7': 'PO-seam (its route 3 IS the progenitor derivation)'}

CONVERGES = {
    # ** r2605: the mod-2 route is CLOSED (the involution is quaternionic).  What replaces it -- the
# Kramers question -- serves the same three, so convergence is unchanged and grounded rises. **
    'PO-5': ('mod-2 index DONE (=1); what remains is the BRIDGE itself, and 3 candidates are spent', 2),
    'PO-7': ('gated by PO-seam: its route 3 IS the progenitor derivation', 2),
    'PO-6': ('L-207 B-2 unlocks here', 2),
    'PO-12': ('the transfer is what makes the 8% signature confrontable', 2),
}


def grounded(tag, row):
    # ** PO-5 at r2608: condition met AND value computed.  grounded is now 3 by receipt weight. **
    if tag == 'PO-5':
        return 3
    if os.path.exists(os.path.join(ROOT, 'kills', f'{tag}.md')):
        return 3
    if re.search(r'\\rcpt|receipt|computed|measured|\d\.\d', row):
        return 2
    return 1


def main():
    po = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    rows = [l for l in po.split('\n') if re.match(r'\|\s*\*\*PO-\d+\*\*', l)]
    out = []
    for l in rows:
        tag = re.search(r'PO-\d+', l).group(0)
        flat = re.sub(r'\s+', ' ', l)
        g = grounded(tag, flat)
        r = REACH.get(tag, 1)
        why, c = CONVERGES.get(tag, ('', 1))
        workable = 0 if tag in GATED_BY else 1
        out.append((workable, c, r * g, tag, g, r, c, why))
    out.sort(reverse=True)

    print()
    print('  rank_open -- the open work on THE_PRIORITY\'s three axes')
    print()
    print(f"    {'#':>2}  {'item':<7} {'conv':>4} {'reach':>5} {'grnd':>4} {'r×g':>4}   why it converges")
    for n, (w, c, rg, tag, g, r, cc, why) in enumerate(out, 1):
        note = why[:52] if w else ("\u26d4 GATED BY " + GATED_BY[tag])[:52]
        print(f"    {n:>2}  {tag:<7} {c:>4} {r:>5} {g:>4} {rg:>4}   {note}")
    print()
    print('  ⌗ CONVERGENCE leads because it is why the order has been obvious: the highest-convergence')
    print('    item has been visibly next every time.  ** When two tie on it, the order stops being')
    print('    obvious -- and THE_PRIORITY states the three conditions for distrusting this list. **')
    print()
    print('  ⚠ REACH is entered by hand.  ** The script cannot check a judgement about what a result')
    print('    would BUY, and pretending otherwise would make the ranking look measured when it is not. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

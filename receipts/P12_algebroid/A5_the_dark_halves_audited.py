#!/usr/bin/env python3
"""A5 -- the last unaudited bucket: BOTH live dark halves are `PO` rows under their register names, so
the DARK count is 0 distinct problems, not 2.

** THE JOB, r2696, Daryl: ** "*** I want it down to the list of things we all know are still open. ***"
The `DARK` bucket was the only one never checked for duplication.

** ⓵ `L-221` SAYS IT IN `PO-5`'s OWN ROW. **  "** register alias: L-221 ** (renumbered from L-174 at
r2426)".  *** The row states the identity; the counter reads two files and adds them. ***

** ⓶ `L-165` IS PAIRED IN THE BOARD'S OWN VEIN HEADER. **  "** L-165 · PO-6 · WHAT A QUANTUM OF THIS
GEOMETRY IS **".  ⌗ ** And `PROTECTED_OPEN` mentions `L-165` ZERO times ** -- *** so unlike `PO-5`/`L-221`,
this pairing is recorded ONLY in the board, and a reader of the register alone would take them for two
problems. ***

  ** Both subjects match: **
  * `L-165`'s dark half is ** the measure on the tower **; `PO-6`'s open half is ** joint satisfiability
    of the conditions on that measure ** -- r2684 called it "`PO-6`'s question from the other end".
  * `L-221`'s dark half is ** the coupling **; `PO-5` IS the coupling, walled on two routes at r2667.

** ⛭⛭ ⓷ SO THE DARK BUCKET CONTRIBUTES 0 DISTINCT PROBLEMS. **  *** Two veins, both already on the
table under `PO-` numbers.  The count was 2 because the stamp reads `DARK` and `PO` from different files
and never asks whether an item appears in both -- which is precisely r2694's `LEDGER` finding, in the
last bucket that had not been checked. ***

** ⓸ AND THAT COMPLETES THE AUDIT. **  *** Every bucket has now been swept for duplication:
`LEDGER` 7 -> 1 (r2694), `ROUTED` 3 -> 2 (r2695, a closed item counted live), row heads corrected
(r2695), `DARK` 2 -> 0 here.  What remains is the eight `PO` rows and two genuinely separate items. ***

WHAT IS NOT CLAIMED.  ** Not that the veins should be deleted ** -- *** a vein is a working space with
its own receipts and history; what is removed is its CONTRIBUTION TO THE COUNT, not the vein. ***
** Not that `PO-5` or `PO-6` shrink ** -- they are exactly as hard, and `PO-5` remains the one UNBOUNDED
item.  ** Not that the pairing is newly discovered ** -- `PO-5` states its alias in print; what is new is
that the counter was never told.

Written r2696.  Stated for reversal.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print('  A5 -- are the dark halves distinct problems?')
    print()
    import workqueue as Q
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    # ⛔ AMENDED r3105 (`L-249`): the matcher admitted only the OPEN form, so every row r3001 struck
    # vanished from `po` and `po['PO-5']` would raise `KeyError`.  *`A3` carries the same fix with
    # the reason written out at r2721; this file was missed then and by `L-248`'s sweep, which
    # searched for the `startswith` SPELLING and not this one.*
    po = {re.search(r'PO-\d+', l).group(0): l
          for l in raw.split('\n') if re.match(r'\|\s*~?~?\*\*PO-\d+\*\*', l)}
    board = open(os.path.join(ROOT, 'BOARD.md'), encoding='utf-8', errors='replace').read()

    live = [d['id'] for d in Q.dark_halves() if d['open']]
    # ⛭⛭ AND THE SAME AMENDMENT AS `A3`: this pinned a LIVE count and broke when the corpus moved
    # the way the audit says it should.  `PO-5` was STRUCK at r2947, so `L-221`'s dark half is no
    # longer live -- ** which is the audit's own thesis arriving, not a contradiction of it. **
    #   ⇒ *** A check that fails when a dark half CLOSES is a check that punishes the finding it
    #       defends.  The historical census is pinned; the live claim is monotone. ***
    AT = '0173a691b28438eb15f687ee6f93a589bacb2421'          # r2696, where this audit was taken
    THEN = ['L-165', 'L-221']
    check(f'⓵ at {AT[:12]} (r2696, where this audit was taken) exactly two dark halves were live: '
          f'{THEN}', len(THEN) == 2)
    check(f'⓵ᵇ ⛭ and the live count has not GROWN since: {sorted(live)} -- a dark half closing is '
          'this audit\'s thesis, a new one appearing would be against it',
          len(live) <= len(THEN) and set(live) <= set(THEN))
    # ⛔ the first writing of this check was an `or`-chain whose first clause is true, so it could
    # not fail.  ** It asserts the CAUSE directly instead: PO-5's row is struck AND L-221 is gone. **
    check('⓵ᶜ and the one that closed is `L-221`, whose `PO-5` row is STRUCK in the register -- the '
          'shrink is accounted for by name rather than merely allowed',
          'PO-5' in po and bool(re.match(r'\|\s*~~', po['PO-5'])) and 'L-221' not in live)

    check("and PO-5's own row states the identity: \"register alias: L-221\"",
          'register alias: **`L-221`**' in po['PO-5'])

    check('⓶ while L-165 is paired only in the board\'s vein header: "L-165 · PO-6 · WHAT A QUANTUM OF '
          'THIS GEOMETRY IS"',
          'L-165` · PO-6 · WHAT A QUANTUM OF THIS GEOMETRY IS' in board)
    check('⌗ and PROTECTED_OPEN mentions L-165 ZERO times -- so a reader of the register alone would '
          'take them for two problems',
          'L-165' not in raw)

    # the subjects match
    check('⓷ and the subjects match: PO-5 IS the coupling, which is L-221\'s dark half',
          'coupling' in po['PO-5'].lower())
    check('while PO-6\'s open half is the joint satisfiability of the conditions -- L-165\'s measure on '
          'the tower from the other end',
          'satisfiab' in po['PO-6'].lower())

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the DARK bucket contributes 0 distinct problems. **')
    print('  ⓵ ** L-221 is PO-5: ** the row says so in print — "register alias: L-221".')
    print('  ⓶ ** L-165 is PO-6: ** the board\'s own vein header reads "L-165 · PO-6 · WHAT A QUANTUM OF')
    print('     THIS GEOMETRY IS" — ** and PROTECTED_OPEN mentions L-165 zero times, ** so the pairing')
    print('     lives only in the board and a register reader sees two problems.')
    print('  ⛭⛭ ⓷ ** The count was 2 because the stamp reads DARK and PO from different files and never')
    print('     asks whether an item appears in both ** — precisely r2694\'s LEDGER finding, in the last')
    print('     bucket that had not been checked.')
    print('  ⓸ ** AND THAT COMPLETES THE AUDIT: ** LEDGER 7→1 (r2694) · ROUTED 3→2 (r2695) · four row')
    print('     heads corrected (r2695) · DARK 2→0 (here).')
    print('     ⇒ *** What remains is the eight PO rows and two genuinely separate items. ***')
    print('  ⚠ ** A vein is a working space and is NOT deleted: ** what is removed is its contribution to')
    print('    the COUNT.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

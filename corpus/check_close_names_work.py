#!/usr/bin/env python3
"""check_close_names_work.py -- A KILL RECEIPT WHOSE OWN CHECKS DO NOT CLEAR MAY NOT LEAVE THE ROW STRUCK.

** WHY.  `THE_CODA`, "The closure self-check" (r1279): **

    *** "the test is 'CAN I STILL NAME WORK THAT COULD BE DONE?', not 'can I write a clean verdict.'
        ... Close only when the exploration returns ALL PARTS FILLED." ***

  ⛔ ** r2717 struck `PO-11` and, in the same row, named what was not closed.  r2712 struck `PO-10`,
  whose specification was withdrawn thirteen revisions later. **  *** Both were BOUNDED NEGATIVES --
  the node's to write -- wearing a CLOSURE's clothes, which are not. ***

** ⛭ AND WHY THIS WATCHES STRUCTURE AND NOT WORDING.  *** The first version of this gate matched
phrases: "what remains", "is untouched".  It reported `PO-8` twice -- once for "what remains OF THE
ITEM after the gate" (describing the object) and once for "the reducible sector's settlement is
untouched, AS IT WAS NEVER IN QUESTION" (a scope note).  Both are careful writing, and a regex
cannot tell them from a leftover.  ** Same failure as r2726's symbol-matching pass and r2730's
synonym hole: I keep building word-matchers for structural properties. ** ***

** WHAT THIS CHECKS, structurally. **  A kill receipt's five checks each carry a verdict marker.
*** If any check does NOT clear, the receipt itself says the close was not earned -- and the row must
not remain struck.  That is unambiguous, unwordable-around, and it is the receipt's own testimony
rather than this gate's reading of prose. ***

  ⌗ ** The correct outcome of a non-clearing check is not to hide it. **  *** It is to reverse the
    strike, or to name the verdict BOUNDED.  `kills/PO-10.md` does exactly that and the row was
    reopened at r2730 on its own finding. ***

    python3 corpus/check_close_names_work.py

Written r2730.  Stated for reversal.
"""
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

# ** a check that did not clear says so on its own heading. **
NOT_CLEARED = re.compile(r'^##\s*[⓵⓶⓷⓸⓹①②③④⑤].*?(?:DOES NOT CLEAR|FAILS|⛔)', re.M)
# ** and a receipt that reversed or bounded its own strike says THAT. **
HANDLED = re.compile(r'does not ratify|recommends REVERSING|BOUNDED NEGATIVE was the honest'
                     r'|a bounded negative', re.I)


def struck_ids():
    reg = os.path.join(ROOT, 'PROTECTED_OPEN.md')
    if not os.path.exists(reg):
        return set()
    return {m.group(1) for m in
            re.finditer(r'\|\s*~~\s*\*\*(PO-\d+)\*\*\s*~~',
                        open(reg, encoding='utf-8', errors='replace').read())}


def main():
    print()
    print('  check_close_names_work -- does any STRUCK row rest on a receipt whose checks fail?')
    print()
    struck = struck_ids()
    flagged, n = [], 0

    for f in sorted(glob.glob(os.path.join(ROOT, 'kills', '*.md'))):
        pid = os.path.basename(f)[:-3]
        d = open(f, encoding='utf-8', errors='replace').read()
        n += 1
        fails = NOT_CLEARED.findall(d)
        if fails and pid in struck and not HANDLED.search(d):
            flagged.append((pid, len(fails)))

    print(f'  {n} kill receipt(s) checked · {len(struck)} row(s) currently struck')
    if flagged:
        print()
        for pid, k in flagged:
            print(f'    [FAIL] {pid} is STRUCK, and its own receipt reports {k} check(s) not clearing')
        print()
        print('    ⛔⛭ ** THE CODA: "close only when the exploration returns ALL PARTS FILLED." **')
        print('       *** A receipt that reports a non-clearing check has said, in its own words,')
        print('       that the close was not earned.  The remedy is to REVERSE the strike or to name')
        print('       the verdict BOUNDED -- never to leave the row struck on a receipt that')
        print('       contradicts it. ***')
        return 1
    print('  no struck row rests on a receipt whose own checks fail.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

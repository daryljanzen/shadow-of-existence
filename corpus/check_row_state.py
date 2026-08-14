#!/usr/bin/env python3
"""check_row_state.py -- EVERY `PROTECTED_OPEN` ROW MUST DECLARE ITS CURRENT STATE FIRST.

** WHY.  r2695, Daryl: ** "*** You can't solve problems in a corpus that's stale all over the place.  If
the open problems map is not even a genuine list of open problems ... work the list till it's a
legitimate list. ***"

** WHAT THE AUDIT FOUND. **
  * ** `PO-3` and `PO-9` opened with `OPEN` ** while the stamp reported them ANSWERED -- ** fifty
    revisions ** after the answers landed at r2645 and r2644.  *** A reader opening the row saw the
    opposite of the truth. ***
  * ** `PO-6` read "THREE OF ITS FOUR HALVES" ** while r2684 had established it declares ** TWO **.
  * ** `PO-5` read "WORKED FOUR TIMES r2525--r2572" ** after three more workings.
  * ** `FOR_54` item 59 ** carried "⛔⛔ AND ANSWERED AT c54.212" ** in its own header ** and was counted
    LIVE, because `routed()` tested for the single glyph `✔`.

  ⇒ *** A row's state field accumulates notes at its TAIL while its HEAD keeps the sentence it was
      registered with.  Every reader sees the head. ***

** WHAT THIS CHECKS. **  The state field of every `PO-` row must BEGIN with a state marker -- `OPEN`,
`ANSWERED`, `STRUCK`, `WITHDRAWN`, `CLOSED` -- within its first 40 characters.

  ⚠ ** It cannot check the marker is TRUE ** -- *** that is a reading, and the four corrections above were
      found by reading.  What it enforces is that a state is DECLARED at the head, which is the property
      whose absence let a stale head survive fifty revisions. ***

    python3 corpus/check_row_state.py

Written r2695.  Stated for reversal.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

MARKERS = ('OPEN', 'ANSWERED', 'STRUCK', 'WITHDRAWN', 'CLOSED', 'RETIRED')


def main():
    print()
    print('  check_row_state -- does every row declare its state first?')
    print()
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    bad, n = [], 0
    for l in raw.split('\n'):
        m = re.match(r'\|\s*\*\*(PO-\d+)\*\*', l)
        if not m:
            continue
        n += 1
        head = re.sub(r'[*`~]', '', l.split(' | ')[-1])[:40].upper()
        if not any(head.lstrip().startswith(k) for k in MARKERS):
            bad.append((m.group(1), head[:34]))

    print(f'  {n} row(s) checked')
    if bad:
        print()
        for tag, head in bad:
            print(f'    [FAIL] {tag} opens "{head}" -- no state marker in the first 40 chars')
        print()
        print('    ⛔ ** A ROW\'S STATE FIELD ACCUMULATES NOTES AT ITS TAIL WHILE ITS HEAD KEEPS THE')
        print('       SENTENCE IT WAS REGISTERED WITH. **  *** PO-3 and PO-9 read `OPEN` for fifty')
        print('       revisions after being answered.  Put the current state first. ***')
        return 1
    print('  every row declares its state at the head.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

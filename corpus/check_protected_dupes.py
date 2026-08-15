#!/usr/bin/env python3
"""check_protected_dupes.py -- NO PROTECTED ID MAY APPEAR ON TWO ROWS.  Built c54.224, after twice.

** WHY, and it is a count rather than an argument. **

  * ** c54.221 ** -- `c53be44`, the merge of the fork's own c54.220, put `PO-4`, `PO-5`, `PO-6` and
    `PO-7` on TWO ROWS EACH.  For `PO-4` and `PO-6` neither copy was a superset, so the observer
    line's r2768-r2775 and the fork's `L-552`/`L-553`/`L-554` sat in different copies of one row.
    ** Every register gate was green. **  `L-555` repaired it and said so.
  * ** c54.224 ** -- `19139ed`, the merge of the fork's c54.222, did *** the same four rows again ***,
    and it stayed live through r2783, r2783a, r2784 and r2785.  This time `PO-4`'s two copies did not
    even agree on STATE: one carried `~~PO-4~~` struck (r2778) and the other did not.

  ⇒ *** A closed item was un-closed by a merge, and nothing standing was asking. ***

** ⛭⛭ WHAT WAS THERE, AND WHY NONE OF IT FIRES. **  `check_id_bands` polices `THE_LIVE_ARC.md`;
`check_dupes` polices document names; `check_row_state`, `check_kills`, `check_open_ledger`,
`check_family_pointers` and `check_register_columns` all read `PROTECTED_OPEN.md` ** one row at a
time ** -- and a row that is perfectly well formed twice satisfies every one of them.
  ⇒ ** A per-row check cannot see a whole-file property. **  *That is not a defect in any of them;
    it is a hole between them, and it is the hole a merge falls through.*

** ⌗ AND `PROTECTED_OPEN.md` IS NOT DECLARED `merge=union`. **  Checked: `.gitattributes` declares
union on `THE_LIVE_ARC.md`, `WHATS_TEED_UP.md`, `THE_BURN_DOWN.md` and `CORPUS_MAP.md`, and its own
comment says *"union merge cannot detect a duplicate ID"*.  So this is the OTHER route to the same
place: rows tens of thousands of characters long, both nodes editing them, and a conflict resolved by
keeping both sides.  ** The declared-union hole was already known and gated; this one was not. **

** WHAT IT CHECKS AND WHAT IT DOES NOT. **  It counts row IDs and nothing else -- it does not compare
the copies, does not judge which is authoritative, and does not repair.  *Repair is a reading, and a
gate that guessed which copy to keep would be worse than none: at c54.224 the losing copy's unique
content was the fork's own c54.221 note, which the observer line had pruned deliberately, and only a
reader could know that.*

    python3 corpus/check_protected_dupes.py

Written c54.224 (`L-558`).  Stated for reversal.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
REG = os.path.join(ROOT, 'PROTECTED_OPEN.md')

#: matches a register row's ID whether the row is struck (`~~PO-4~~`) or open (`**PO-4**`).
#: ** The strike marker is INSIDE the match on purpose: two copies that disagree about state are
#: still two copies of one ID, and that is the case c54.224 found. **
ROW = re.compile(r'\|\s*(~~)?\s*\*\*(PO-\d+[a-z]?)\*\*')


def main():
    print()
    print('  check_protected_dupes -- does any protected ID appear on more than one row?')
    print()
    if not os.path.exists(REG):
        print('  [FAIL] PROTECTED_OPEN.md is missing')
        return 1

    seen = {}
    for n, line in enumerate(open(REG, encoding='utf-8', errors='replace'), 1):
        m = ROW.match(line)
        if m:
            seen.setdefault(m.group(2), []).append((n, bool(m.group(1)), len(line)))

    if not seen:
        print('  [FAIL] no protected rows found -- the reader is broken, not the file')
        return 1

    dupes = {k: v for k, v in seen.items() if len(v) > 1}
    print(f'  {len(seen)} protected ID(s) across {sum(len(v) for v in seen.values())} row(s)')
    if not dupes:
        print('  every protected ID appears exactly once.')
        print()
        return 0

    print()
    for pid, hits in sorted(dupes.items()):
        states = {s for _, s, _ in hits}
        print(f'    [FAIL] {pid} appears on {len(hits)} rows: '
              + ', '.join(f'line {n} ({"struck" if s else "open"}, {c} chars)' for n, s, c in hits))
        if len(states) > 1:
            print(f'           ⛔ AND THE COPIES DISAGREE ABOUT STATE -- one struck, one open.  '
                  f'A merge has un-closed a closed item.')
    print()
    print('    ⛭ ** This is a MERGE keeping both sides of a row both nodes edited. **  It has happened')
    print('       twice (`c53be44` at c54.221, `19139ed` at c54.224) and both times every other')
    print('       register gate was green, because *** a per-row check cannot see a whole-file')
    print('       property. ***')
    print('    ⌗ The repair is a READING, not a merge: compare the two copies against the two merge')
    print('       parents (`git show <parent>:PROTECTED_OPEN.md`) and decide which is authoritative.')
    print('       ** Neither copy being a superset of the other is the normal case, not the odd one. **')
    print()
    return 1


if __name__ == '__main__':
    sys.exit(main())

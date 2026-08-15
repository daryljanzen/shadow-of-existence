#!/usr/bin/env python3
"""check_withdrawals_propagate.py -- A WITHDRAWAL MUST REACH EVERY ROW THAT CITES ITS VICTIM.

** WHY.  r2832. **  *** `PO-7` carried r2790's diagnosis -- "the stored $r_s$ moves the wrong way" --
as current for thirty-three revisions.  ** r2799 withdrew that framing (the value is a fitted design
choice, not an error), and the withdrawal was written into `PO-10` and nowhere else. **  Two more of the
same shape were then found: r2658's withdrawal reached `PO-12` and not `PO-10`; r2661's reached `PO-12`
and not `PO-5`. ***

  ⇒ ** A correction propagates into the row it is written in, and into no other. **  *** The register
      has no mechanism carrying a withdrawal sideways, so a retracted claim survives in every row the
      corrector did not happen to be editing -- reading as current, in the corrector's own voice. ***

** WHAT THIS CHECKS. **  *** For every "X WITHDRAWS/CORRECTS/REVERSES/RETRACTS Y" pair found in any row:
any OTHER row citing Y must also cite X, or carry a mark naming the withdrawal. ***

  ⌗ ** It does not judge whether the withdrawal APPLIES to the other row's use of the victim ** --
    *** sometimes it will not, and then the mark says so.  What it stops is the other row never hearing
    about it. ***

    python3 corpus/check_withdrawals_propagate.py

Written r2832.  Stated for reversal.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

ROW = re.compile(r'\|\s*(~~)?\s*\*\*(PO-\d+[a-z]?)\*\*')
OVERTURN = re.compile(r'(WITHDRAW[SN]?|CORRECTS|REVERSES|RETRACT\w*)\s+(r\d{4})', re.I)


def main():
    print()
    print('  check_withdrawals_propagate -- did each withdrawal reach every row citing its victim?')
    print()
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()

    rows = {}
    for l in raw.split('\n'):
        m = ROW.match(l)
        if not m:
            continue
        cells = [c.strip() for c in re.split(r'(?<!\\)\|', l)[1:-1]]
        if len(cells) > 4:
            rows[m.group(2)] = cells[4]

    bad = []
    for pid, s in rows.items():
        for mm in OVERTURN.finditer(s):
            by = re.search(r'\b(r\d{4})\b', s[max(0, mm.start()-150):mm.start()])
            if not by:
                continue
            victim, over = mm.group(2), by.group(1)
            for pid2, s2 in rows.items():
                if pid2 == pid or victim not in s2:
                    continue
                # ** r2832a: `over in s2` passed the seed -- the overturning revision appears
                # elsewhere in a 40,000-character cell for an unrelated reason.  *** Mentioning
                # it somewhere is not the withdrawal ARRIVING.  Require it, or a mark, within
                # 400 characters of the victim's citation. ***
                k = s2.find(victim)
                near = s2[max(0, k-400):k+400]
                if over in near or 'OVERTURNED' in near or f'⟨r2832: {victim}' in near:
                    continue
                bad.append((victim, over, pid, pid2))

    print(f'  {len(rows)} row(s) cross-checked')
    if bad:
        print()
        for victim, over, src, dst in bad[:10]:
            print(f'    [FAIL] {victim} is overturned by {over} in {src},')
            print(f'           but {dst} cites {victim} and never hears about it')
        print()
        print('    ⛭ ** A correction propagates into the row it is written in and into no other. **')
        print('       *** Carry the withdrawal sideways, or mark the other row\'s use of the victim. ***')
        return 1

    print('  every withdrawal reached the rows citing its victim.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

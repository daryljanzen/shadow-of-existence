#!/usr/bin/env python3
"""check_rows_cite_receipts.py -- EVERY OPEN ROW MUST CITE THE RECEIPTS ON ITS OWN OBJECT.

** WHY.  r2873-r2874, Daryl: "Every fucking row needs to be citing the corpus." **

  *** Measured: the register cites ** 51 of 483 ** receipts bearing on its open rows -- ** 11% **.
      Per row: `PO-10` 26%, `PO-5` 19%, `PO-6` 9%, `PO-7` 3%, `PO-1c` 2%, and ** `PO-1b` 0 of 52 **. ***

  ⇒ ** And the consequences were not abstract. **  *** `PO-5` carried 3 of 11 delivered contents and
      spent six revisions denying a structure (the integer winding part separating $u$ from $d$) that
      sat in an uncited receipt.  `PO-7` held C57's LEVEL offset and not B6's ** 98.2%-of-the-acoustic-
      rate ** reproduction.  `PO-1b` asked a question `P14_P14_payoff` answers, and cited nothing. ***

** WHAT THIS CHECKS. **  *** Every OPEN row's status cell must cite at least a floor number of receipts
that exist on its object.  The floor starts LOW and is meant to RISE -- it is a ratchet, not a
standard. ***

  ⌗ ** A row is not required to cite everything ** -- *** many of the 483 are keyword-adjacent rather
    than load-bearing.  What is required is that the row have GONE AND LOOKED, and the count is the only
    externally visible sign of that. ***

    python3 corpus/check_rows_cite_receipts.py

Written r2874.  Stated for reversal.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

# ** the ratchet: raise these as rows are worked; never lower one **
FLOOR = {'PO-5': 17, 'PO-10': 21, 'PO-6': 7, 'PO-7': 5, 'PO-1c': 1}
DEFAULT = 1

CITE = re.compile(r'`([A-Za-z0-9_]+)`')
RECEIPTISH = re.compile(r'^[A-Z]\d+[a-z]?_|^L\d+|^S\d+_|^P\d+_|^M\d+_|^C\d+_|^B\d+_|^Z\d+_')


def main():
    print()
    print('  check_rows_cite_receipts -- does every open row cite the work behind it?')
    print()
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()

    bad, rows = [], 0
    for line in raw.split('\n'):
        m = re.match(r'\|\s*(~~)?\s*\*\*(PO-\d+[a-z]?)\*\*', line)
        if not m or m.group(1) or line.lstrip('|').lstrip().startswith('~~'):
            continue
        pid = m.group(2)
        rows += 1
        cited = {c for c in CITE.findall(line) if RECEIPTISH.match(c)}
        floor = FLOOR.get(pid, DEFAULT)
        print(f'    {pid:<8} cites {len(cited):>3}   floor {floor}')
        if len(cited) < floor:
            bad.append((pid, len(cited), floor))

    print()
    print(f'  {rows} open row(s)')
    if bad:
        print()
        for pid, n, floor in bad:
            print(f'    [FAIL] {pid} cites {n} receipt(s), below its floor of {floor}')
        print()
        print('    ⛭ ** A row that cites nothing is asserting its own state. **  *** The register')
        print('       held 11% of its worked corpus and the gaps were not abstract: six revisions')
        print('       spent denying a structure that sat in an uncited receipt. ***')
        return 1

    print('  every open row meets its citation floor.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

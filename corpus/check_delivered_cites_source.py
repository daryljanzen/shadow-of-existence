#!/usr/bin/env python3
"""check_delivered_cites_source.py -- A ROW'S DELIVERED BLOCK MUST CITE A RECEIPT, NOT A SUMMARY.

** WHY.  r2871. **  *** Twice this line built multi-revision arguments on a row's SUMMARY of its own
delivered content instead of on the receipt behind it. ***

  ⇒ ** `PO-5`'s delivered block said "second quantisation returns baryon 1, diquark 0, meson 1" -- THREE
      contents. **  *** P03's receipt has ELEVEN, tested against the observed hadron spectrum and
      agreeing 11 of 11, plus an account of CONFINEMENT as failure to close the lap, plus the fact that
      ** the INTEGER winding part distinguishes u from d ** -- the exact structure r2858-r2868 spent six
      revisions arguing does not exist. ***

  ⌗ ** The summary was not WRONG.  It was a quarter of the content, and nothing marked it as partial. **
    *** An argument built on it inherits the missing three quarters as an assumed absence. ***

** WHAT THIS CHECKS. **  *** Every open row's "WHAT IS DELIVERED" block must name a receipt or a paper
section -- something re-readable -- not only the row's own prose. ***

    python3 corpus/check_delivered_cites_source.py

Written r2871.  Stated for reversal.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

SOURCE = re.compile(r'\bP\d{1,2}\b|\bp0\b|`[A-Z]\d+[a-z]?_|`L\d+|receipt|sec:')


def main():
    print()
    print('  check_delivered_cites_source -- does every delivered block name a source?')
    print()
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()

    bad, checked = [], 0
    for line in raw.split('\n'):
        m = re.match(r'\|\s*(~~)?\s*\*\*(PO-\d+[a-z]?)\*\*', line)
        if not m or m.group(1) or line.lstrip('|').lstrip().startswith('~~'):
            continue
        cells = [c.strip() for c in re.split(r'(?<!\\)\|', line)[1:-1]]
        if len(cells) < 5:
            continue
        s = cells[4]
        j = s.find('▣ HISTORY')
        head = s[:j] if j > 0 else s
        k = head.find('WHAT IS DELIVERED')
        if k < 0:
            # ** not every row has a delivered half; that is not a defect **
            continue
        checked += 1
        block = head[k:k+2400]
        if not SOURCE.search(block):
            bad.append((m.group(2), 'delivered block names no receipt or paper section'))

    print(f'  {checked} row(s) with a delivered block')
    if bad:
        print()
        for pid, why in bad:
            print(f'    [FAIL] {pid}: {why}')
        print()
        print('    ⛭ ** A summary of delivered content is not wrong; it is PARTIAL, and nothing')
        print('       marks it as partial. *** An argument built on it inherits the missing')
        print('       remainder as an assumed absence. ***')
        return 1

    print('  every delivered block names a source.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

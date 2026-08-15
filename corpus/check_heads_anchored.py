#!/usr/bin/env python3
"""check_heads_anchored.py -- A ROW'S CURRENT-STATE HEAD MUST BE CHECKABLE AGAINST THE CORPUS.

** WHY.  r2832. **  *** Every live row was given a `▣ CURRENT STATE` head this revision, and ** four of
the ten cited nothing from the corpus ** -- no paper, no quoted sentence, no named document.  Two of the
four were written by this line the same day. ***

  ⇒ ** A head that cites nothing cannot be checked against anything. **  *** It is the register asserting
      its own state, which is precisely the map-as-territory failure the whole apparatus exists to
      prevent -- and the register is the map. ***

** WHAT THIS CHECKS. **  *** Every OPEN row's head (the text before the `▣ HISTORY` marker) must name a
paper (`P7`, `p0`, `CR_cosmology`, ...), a corpus document, or carry a quoted sentence of 25+
characters. ***

  ⌗ ** It checks that an anchor EXISTS, not that it is right ** -- *** a wrong citation is a different
    failure.  What this stops is a state nobody can trace to a source. ***

    python3 corpus/check_heads_anchored.py

Written r2832.  Stated for reversal.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

ROW = re.compile(r'\|\s*(~~)?\s*\*\*(PO-\d+[a-z]?)\*\*')
ANCHOR = re.compile(r'\bP\d{1,2}\b|\bp0\b|`(CR_|FIGURE_|GEOMETRY_|THE_|ONTOLOGY_)')
QUOTE = re.compile(r'"[^"]{25,}"')


def main():
    print()
    print('  check_heads_anchored -- is every open row\'s state head traceable to a source?')
    print()
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()

    bad, checked = [], 0
    for line in raw.split('\n'):
        m = ROW.match(line)
        if not m or m.group(1) or line.lstrip('|').lstrip().startswith('~~'):
            continue
        cells = [c.strip() for c in re.split(r'(?<!\\)\|', line)[1:-1]]
        if len(cells) < 5:
            continue
        s = cells[4]
        j = s.find('▣ HISTORY')
        head = s[:j] if j > 0 else s
        if '▣ CURRENT STATE' not in head:
            bad.append((m.group(2), 'no CURRENT STATE head'))
            continue
        checked += 1
        if not (ANCHOR.search(head) or QUOTE.search(head)):
            bad.append((m.group(2), 'head cites no paper, document or quotation'))

    print(f'  {checked} open row head(s) checked')
    if bad:
        print()
        for pid, why in bad:
            print(f'    [FAIL] {pid}: {why}')
        print()
        print('    ⛭ ** A head that cites nothing cannot be checked against anything. **')
        print('       *** That is the register asserting its own state — map-as-territory,')
        print('       committed by the map itself. ***')
        return 1

    print('  every open row\'s state head names a source.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

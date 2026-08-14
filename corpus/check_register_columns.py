#!/usr/bin/env python3
"""check_register_columns.py -- EVERY REGISTER ROW MUST HAVE THE HEADER'S COLUMN COUNT.

** WHY.  cc54, c54.219: ** *** "my register edit broke `PO-6`'s cell count on unescaped `|_{...}`
bars --- ** fourth time, same hand, two revisions after I diagnosed the class **.  The identical string
went into the INDEX row, where your column lint caught it instantly.  ** The register needed me to
notice. ** " ***

  ⇒ ** `receipts/INDEX.md` has a column lint and `PROTECTED_OPEN.md` does not. **  *** The same defect
      from the same edit was caught in one file and shipped in the other, four times.  That is not a
      discipline problem -- it is a missing instrument, and cc54 said so more precisely than this line
      had. ***

** ⛭⛭ THE TEST IS RAW-PIPE COUNT, NOT SEPARATOR COUNT, AND THE DIFFERENCE IS THE WHOLE POINT. **  ***
A restriction bar `$R^2|_{O(h^2)}$` inserted into a cell leaves the `' | '` count UNCHANGED -- it has no
surrounding spaces -- while markdown still reads it as a cell boundary.  ** A check on `' | '` passes a
broken row. **  Counting raw unescaped `|` catches it, and catches every other cause too: absolute
values, norms, set-builders, restriction bars.  *** No enumeration of LaTeX constructs is needed or
would be complete. ***

    python3 corpus/check_register_columns.py

Written r2772.  Stated for reversal.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
REG = os.path.join(ROOT, 'PROTECTED_OPEN.md')

ROW = re.compile(r'\|\s*~*\s*\*\*(PO-\d+)\*\*')
RAW_PIPE = re.compile(r'(?<!\\)\|')


def main():
    print()
    print('  check_register_columns -- does every register row carry the header\'s column count?')
    print()
    if not os.path.exists(REG):
        print('  [FAIL] PROTECTED_OPEN.md is missing')
        return 1

    lines = open(REG, encoding='utf-8', errors='replace').read().split('\n')
    rows = [(i, l) for i, l in enumerate(lines) if ROW.match(l)]
    if not rows:
        print('  [FAIL] no register rows found -- the reader is broken, not the file')
        return 1

    counts = [len(RAW_PIPE.findall(l)) for _, l in rows]
    expect = max(set(counts), key=counts.count)

    bad = [(i, ROW.match(l).group(1), n)
           for (i, l), n in zip(rows, counts) if n != expect]

    print(f'  {len(rows)} register row(s) · expected {expect} raw pipes '
          f'({expect - 1} cells)')
    if bad:
        print()
        for i, pid, n in bad:
            print(f'    [FAIL] {pid} (line {i+1}) has {n} raw pipes, not {expect}')
        print()
        print('    ⛭ ** An unescaped `|` inside a cell -- a restriction bar, an absolute value, a')
        print('       norm -- is a CELL BOUNDARY to markdown. **  *** And it leaves the `\' | \'` count')
        print('       unchanged, which is why a separator-based check passes a broken row.  Escape it')
        print('       as `\\|` or write it as `\\vert`. ***')
        return 1
    print('  every row matches the header.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

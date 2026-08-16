#!/usr/bin/env python3
"""check_citations_resolve.py -- EVERY RECEIPT CITED IN A ROW MUST BE A REAL FILE.

** WHY.  r2940. **  *** The citation project (r2874) raised the register from 51 cited receipts to
125 -- and `check_owed_rows_live` then caught two of them pointing at nothing: I had written
`P15_the_spacing_deficit_survives_the_one_fitted_NUMBER` where the file is `..._PARAMETER`, and
`P14_characters_label_they_do_not_multiPLY` where it is `...multiPLET`.  ** I quoted titles as I read
them rather than as they are. ** ***

  ⇒ ** A sweep of all 125 found six ** -- *** four TRUNCATIONS (`M3_station_G_supplies_the_sequence`
      for `..._and_the_three_are_one_knot`; `S50_the_counterterm_basis_is_one_dimensional` for
      `..._because_the_background_family_is`; `I3_the_identification_is_general` for
      `..._and_the_shear_count_is_the_gap`) and two AMBIGUOUS stubs (`L212`, which prefixes two
      distinct receipts). ***

  ⌗ ** And a citation that does not resolve is not a citation. ** *** The whole point of raising the
    ratio was that a future reader can go and read the thing.  A truncated name sends them nowhere,
    and a stub sends them to the wrong one of two. ***

** WHAT THIS CHECKS. **  *** Every receipt-shaped name in backticks in any row -- open or struck --
resolves to a file under `receipts/`. ***

    python3 corpus/check_citations_resolve.py

Written r2940.  Stated for reversal.
"""
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

RECEIPTISH = re.compile(r'^[A-Z]\d+[a-z]?_|^L\d+|^S\d+_|^P\d+_|^M\d+_|^C\d+_|^B\d+_|^Z\d+_|'
                        r'^F\d+_|^I\d+_|^D\d+_|^Q\d+_|^T\d+_|^A\d+_|^R\d+_|^W\d+_|^N\d+_|'
                        r'^E\d+_|^K\d+_|^X\d+_')


def main():
    print()
    print('  check_citations_resolve -- does every cited receipt exist?')
    print()
    real = {os.path.basename(x)[:-3]
            for x in glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True)}
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()

    total, bad = 0, []
    for line in raw.split('\n'):
        m = re.match(r'\|\s*(~~)?\s*\*\*(PO-\d+[a-z]?)\*\*', line)
        if not m:
            continue
        pid = m.group(2)
        for c in {x for x in re.findall(r'`([A-Za-z0-9_]+)`', line) if RECEIPTISH.match(x)}:
            total += 1
            if c not in real:
                near = [r for r in real if r.startswith(c[:18])]
                bad.append((pid, c, near[:2]))

    print(f'  {len(real)} receipts on disk; {total} receipt-shaped citations in rows')
    if bad:
        print()
        for pid, c, near in bad[:12]:
            print(f'    [FAIL] {pid} cites `{c}`')
            if near:
                print(f'           did you mean: {near[0]}')
        print()
        print('    ⛭ ** A citation that does not resolve is not a citation. ***  The point of')
        print('       raising the ratio is that a reader can go and read the thing.')
        return 1

    print('  every cited receipt resolves.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

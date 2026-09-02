#!/usr/bin/env python3
"""check_gate_currency.py -- A ROW'S GATE-HOLDING DOCUMENT MUST NOT LAG THE ROW.

** WHY.  r2803. **  *** `PO-2` was stated without being claimed on three levels.  Its row RECORDED four
findings (r2629--r2633) that moved two of them and argued from them at length.
`GEOMETRY_PHYSICS_TAXONOMY.md` --- ** the document that HOLDS the three levels ** --- still read "the
three levels ... stand exactly as r693 set them", in two places, and had never heard of any of it. ***

  ⇒ ** The row and the document it defers to disagreed for 170 revisions and nothing checked. **
      *** The row read as triply held while its own text said otherwise, and the 54s would not touch
      the row while the programme blocked it. ***

** ⛭⛭ WHAT MAKES THIS DETECTABLE. **  *** A gate is a DEFERRAL: the row names a document and the
document holds the state.  ** So the check is a comparison of two revision numbers ** --- the newest
revision the row cites against the newest the document cites.  A document that has not heard of the
row's own findings cannot be holding a current gate. ***

** WHAT THIS CHECKS. **  For every `PROTECTED_OPEN` row naming a state-holding document on disk, the
document must cite a revision within `LAG` of the row's newest.

  ⌗ ** Registers are exempt: ** *** `INDEX.md`, `OWED.md`, `PROTECTED_OPEN.md`, `CLAIMS.md` and the
    `FOR_*` routing files are APPENDED logs, not gate-holders.  A row citing them is not deferring to
    them for its state. ***

  ⌗ ** Report-only where the lag predates this gate: ** *** existing lags are baselined so the gate
    fires on NEW staleness rather than on a backlog, per the `check_arc_columns` pattern. ***

    python3 corpus/check_gate_currency.py

Written r2812.  Stated for reversal.
"""
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

ROW = re.compile(r'\|\s*~*\s*\*\*(PO-\d+[a-z]?)\*\*')
VER = re.compile(r'\br(\d{3,4})\b')

# ** appended registers and routing files: a row citing these is not deferring to them **
EXEMPT = {'INDEX.md', 'OWED.md', 'PROTECTED_OPEN.md', 'CLAIMS.md', 'NEXT.md',
          'LATENT_HISTORY.md', 'INGESTION.md', 'CORPUS_MAP.md', 'THE_LIVE_ARC.md'}

# ** r2812: the lag at which a holding document stops being current.  *** PO-2's was 170. *** **
LAG = 120

# ** baselined at r2812 -- these lags predate the gate and are report-only **
BASELINE = 8


def docs_on_disk():
    out = {}
    for f in glob.glob(os.path.join(ROOT, '*.md')) + glob.glob(os.path.join(ROOT, 'capstones', '*.md')):
        b = os.path.basename(f)
        if b not in EXEMPT:
            out[b] = f
    return out


def main():
    print()
    print('  check_gate_currency -- does any row defer to a document that lags it?')
    print()
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    docs = docs_on_disk()

    stale, checked = [], 0
    for l in raw.split('\n'):
        m = ROW.match(l)
        if not m:
            continue
        revs = [int(x) for x in VER.findall(l)]
        if not revs:
            continue
        newest = max(revs)
        for name, path in docs.items():
            if name[:-3] not in l:
                continue
            checked += 1
            dr = [int(x) for x in VER.findall(open(path, encoding='utf-8',
                                                   errors='replace').read())]
            if not dr:
                continue
            lag = newest - max(dr)
            if lag > LAG:
                stale.append((m.group(1), name, newest, max(dr), lag))

    print(f'  {checked} row->document deferral(s) checked, lag threshold {LAG}')
    if stale:
        print()
        for pid, name, nr, dr, lag in sorted(stale, key=lambda x: -x[4]):
            print(f'    [{"FAIL" if len(stale) > BASELINE else "REPORT"}] {pid} defers to {name} -- '
                  f'row cites r{nr}, document cites r{dr} ({lag} behind)')
        print()
        print('    ⛭ ** A document that has not heard of the row\'s own findings cannot be holding')
        print('       a current gate. **  *** Update the document, or stop citing it as the holder. ***')
        if len(stale) > BASELINE:
            print()
            print(f'  {len(stale)} stale deferral(s), baseline {BASELINE} -- NEW staleness.')
            return 1
        print(f'  {len(stale)} stale deferral(s), at or under the r2812 baseline of {BASELINE}.')
        return 0
    print('  every gate-holding document is current with its row.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

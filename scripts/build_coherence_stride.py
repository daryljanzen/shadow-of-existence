#!/usr/bin/env python3
"""build_coherence_stride.py -- THE 29 ITEMS OF THE COHERENCE PHASE, READ OUT OF 69's CENSUS RATHER THAN RETYPED.

** WHY A SCRIPT AND NOT A HAND-WRITTEN LIST. **  `r7371`'s rule, `cc66`'s: *the selector of a measured
population is committed with the measurement, or the measurement is a claim and not a re-runnable fact.*
The population here is the 29 distinct open items node 69 read out of the eighteen published papers, and
it lives in that census's own prose table.  ⇒ ** So the stride is GENERATED from the census and the
generator is committed beside it. **  A hand-typed copy of 29 rows is a second population nobody can
re-derive, which is the defect this rule exists for.

  python3 scripts/build_coherence_stride.py            # rewrite the DATA half of THE_COHERENCE_STRIDE.tsv
  python3 scripts/build_coherence_stride.py --check     # exit 1 if the file's data lines differ

⌗ ** The RULING and OWNER columns are hand-held and are never overwritten. **  The generator fills the
columns the census decides (item, class, title, papers, register, contradiction) and carries forward
whatever the file already holds for the two columns the phase fills in as it works.

Written r7371.  Stated for reversal.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CENSUS = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7367_69_the_register_census', 'CENSUS.md')
STRIDE = os.path.join(ROOT, 'THE_COHERENCE_STRIDE.tsv')

CLASS = {
    'Stated open in the papers; every register row that touched it is struck': 'STRUCK-ROW',
    'Stated open in the papers; no register row has ever carried it': 'NO-ROW',
    'Stated open in the papers, and carried by a live row': 'LIVE-ROW',
}


def items():
    """(n, class, title, papers, register, contradiction) for every numbered row of the census tables."""
    sec, out = None, []
    for ln in open(CENSUS, encoding='utf-8').read().split('\n'):
        if ln.startswith('### '):
            sec = ln[4:].strip()
        m = re.match(r'^\|\s*(\d+)\s*\|(.*)$', ln)
        if not (m and sec in CLASS):
            continue
        cells = [c.strip() for c in m.group(2).split('|')]
        raw = re.sub(r'\*+', '', cells[0])
        title = re.sub(r'\.\s.*$', '', raw).strip()[:96]
        papers = re.sub(r'\*+', '', cells[1]).strip() if len(cells) > 1 else ''
        reg = re.sub(r'\*+', '', cells[2]).strip() if len(cells) > 2 else ''
        # the census writes "contradiction Cn" inline wherever a paper disagrees with another
        cs = sorted(set(re.findall(r'contradiction (C\d+)', raw + ' ' + reg)))
        out.append((int(m.group(1)), CLASS[sec], title, papers,
                    re.sub(r'\s+', ' ', reg)[:160] or '--', '+'.join(cs) or '--'))
    return sorted(out)


def held():
    """item -> (ruling, owner), whatever the file already carries; never regenerated."""
    out = {}
    if not os.path.exists(STRIDE):
        return out
    for ln in open(STRIDE, encoding='utf-8'):
        if ln.startswith('#') or not ln.strip():
            continue
        f = ln.rstrip('\n').split('\t')
        if len(f) >= 8 and f[0].isdigit():
            out[int(f[0])] = (f[6], f[7])
    return out


def data_lines():
    keep = held()
    out = []
    for n, cls, title, papers, reg, cs in items():
        ruling, owner = keep.get(n, ('--', '--'))
        out.append('\t'.join([str(n), cls, title, papers, reg, cs, ruling, owner]))
    return out


def main():
    lines = data_lines()
    if '--check' in sys.argv:
        cur = [ln.rstrip('\n') for ln in open(STRIDE, encoding='utf-8')
               if ln.strip() and not ln.startswith('#')]
        if cur != lines:
            print('  ⛔ THE_COHERENCE_STRIDE.tsv\'s data lines differ from the census.')
            return 1
        print(f'  the stride carries the census: {len(lines)} item(s).')
        return 0
    head = open(STRIDE, encoding='utf-8').read().split('\n') if os.path.exists(STRIDE) else []
    header = [l for l in head if l.startswith('#')]
    open(STRIDE, 'w', encoding='utf-8').write('\n'.join(header + lines) + '\n')
    print(f'  wrote {len(lines)} item(s) under {len(header)} header line(s).')
    return 0


if __name__ == '__main__':
    sys.exit(main())

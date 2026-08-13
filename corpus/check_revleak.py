#!/usr/bin/env python3
"""check_revleak.py -- THE WORKING RECORD MUST NOT APPEAR IN THE PUBLISHED TEXT.

** WHY. **  The rehoming campaign (r2580, `L-537`) rests on a principle: ** a paper is a MAP OF THE
PRESENT STATE **, and the story of how it got there belongs in `CONSOLIDATE`.  ⇒ *** An internal
revision number is that story's most concrete form: `r2376+c54.164` names a moment in this programme's
own working, and it means nothing whatever to a reader of the physics. ***

** MEASURED r2584: 37 internal revision references across THIRTEEN paper bodies. **  `CR_cosmology`
carries ** 15 ** of them; `sec:refit-bound` alone is ** 57,452 characters of which 59% narrates the
paper's own revision history **, with five revision numbers in the published text.

  ⌗ ** And this is the one part of the campaign that IS mechanical. **  Deciding where a paragraph
  belongs is a reading; *** deciding that `r2376+c54.164` does not belong in a physics paper is not. ***

** WHAT IT CHECKS. **  Every non-comment line of every paper body (bibliography excluded) for the
programme's own revision syntax: `rNNNN`, `c54.N`, `rNNNN+c54.N`.
  ⚠ ** The bibliography is excluded ** because a citation may legitimately carry a version tag, and
  ** comments are excluded ** because a `%` note to a future editor is not published text -- which is
  the same line `check_provenance` draws, from the other side.

** ⚠ AND IT SHIPS GRANDFATHERED, on r2557's rule. **  ** 37 failures on day one is a gate nobody runs. **
The existing 37 are frozen into a baseline of PATHS-AND-TOKENS; *** a revision reference ADDED after
r2584 fails. ***  ⇒ ** So the leak stops growing while the campaign drains it, and each rehoming pass
can remove baseline entries as it goes. **

    python3 corpus/check_revleak.py
    python3 corpus/check_revleak.py --baseline

Written r2584.  Stated for reversal.
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
BASELINE = os.path.join(HERE, 'revleak_baseline.txt')
REV = re.compile(r'r\d{4}\+c54\.\d+|c54\.\d+|\br\d{4}\b')


def papers():
    return sorted(f for f in glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))
                  if not os.path.basename(f).startswith('appendix_receipts'))


def leaks():
    out = []
    for f in papers():
        raw = open(f, encoding='utf-8', errors='replace').read()
        b = '\n'.join(l for l in raw.split('\n') if not l.lstrip().startswith('%'))
        j = b.find('\\begin{thebibliography}')
        body = b[:j] if j > 0 else b
        for m in REV.finditer(body):
            out.append(f'{os.path.basename(f)}::{m.group(0)}')
    return sorted(set(out))


def main():
    if '--baseline' in sys.argv:
        if os.path.exists(BASELINE):
            print(open(BASELINE, encoding='utf-8').read())
        return 0

    print()
    print('  check_revleak -- does the working record appear in the published text?')
    print()
    cur = leaks()
    print(f'  {len(papers())} paper bodies; {len(cur)} distinct revision reference(s) found.')

    if not os.path.exists(BASELINE):
        with open(BASELINE, 'w', encoding='utf-8') as fh:
            fh.write('# ** THE GRANDFATHERED SET, frozen r2584. **  Internal revision references already\n')
            fh.write('# present in paper bodies when this gate was built.  ** A reference ADDED after\n')
            fh.write('# r2584 fails. **  Entries are removed as the rehoming campaign drains them.\n')
            for p in cur:
                fh.write(p + '\n')
        print(f'  no baseline; wrote {len(cur)} entries to {os.path.basename(BASELINE)}')
        return 0

    base = {l.strip() for l in open(BASELINE, encoding='utf-8')
            if l.strip() and not l.startswith('#')}
    new = sorted(set(cur) - base)
    gone = sorted(base - set(cur))
    if gone:
        print(f'  ⛭ {len(gone)} baseline entr(ies) have been drained: {gone[:5]}')
    print()
    if new:
        for n in new:
            print(f'    [FAIL] {n} is an internal revision reference in a published paper body')
        print()
        print('    ⛔ A PAPER IS A MAP OF THE PRESENT STATE.  ** An internal revision number names a')
        print('       moment in this programme\'s own working and means nothing to a reader of the')
        print('       physics. **  The story belongs in CONSOLIDATE.')
        return 1
    print(f'  no NEW revision reference. {len(base)} grandfathered; the bar is that it only falls.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

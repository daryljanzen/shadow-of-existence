#!/usr/bin/env python3
"""check_map_dupes.py -- A REVISION MAY APPEAR IN `CORPUS_MAP.md` EXACTLY ONCE.

** WHY.  r2750: ** *** fourteen duplicate revision blocks were found in the map, `r2749`'s among them.
The cause is this line's own scrap-and-log pattern: a heredoc that files a wisdom scrap AND logs the
map entry, run twice when its first attempt raised on a stale anchor and the surrounding shell reported
the push as successful anyway. ***

  ⛭ ** The same shape hid two MISSING entries at r2737 ** -- *** r2736 and r2737 both failed to log,
  silently, for the mirror reason.  **A pattern that can fail silently will fail in both directions:
  writing twice and not writing at all.** ***

** WHAT THIS CHECKS. **  The map's `### Revision rNNNN` headings are unique.  *** Cheap, exact, and it
catches the failure the moment it lands rather than fourteen revisions later. ***

  ⌗ ** It does not check for MISSING entries. **  *** That needs a list of what should be there, which
    is `LATENT_HISTORY` -- a different check, and named here rather than left implied. ***

    python3 corpus/check_map_dupes.py

Written r2750.  Stated for reversal.
"""
import collections
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
MAP = os.path.join(ROOT, 'CORPUS_MAP.md')


def main():
    print()
    print('  check_map_dupes -- does any revision appear in CORPUS_MAP more than once?')
    print()
    if not os.path.exists(MAP):
        print('  [FAIL] CORPUS_MAP.md is missing')
        return 1
    revs = re.findall(r'^### Revision (r\d+)', open(MAP, encoding='utf-8', errors='replace').read(),
                      re.M)
    dupes = {r: n for r, n in collections.Counter(revs).items() if n > 1}
    print(f'  {len(revs)} revision block(s) · {len(set(revs))} distinct')
    if dupes:
        print()
        for r, n in sorted(dupes.items()):
            print(f'    [FAIL] {r} appears {n} times')
        print()
        print('    ⛭ ** The scrap-and-log pattern writes twice when its first attempt raises on a')
        print('       stale anchor and the surrounding shell reports success anyway. **')
        print('       *** The same shape hid two MISSING entries at r2737 — a pattern that can fail')
        print('       silently fails in both directions. ***')
        return 1
    print('  every revision appears exactly once.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

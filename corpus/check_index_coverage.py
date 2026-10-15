#!/usr/bin/env python3
"""check_index_coverage.py -- THE READ INDEX AGAINST THE TREE IT SCOPES.  Built r7371+70.2 by node 70 (r7371 ⑤ ②).

** WHAT THIS CATCHES. **  `receipts/READ_INDEX.json` is what every scoped CI job reads to decide which
receipts a push can have changed.  It is refreshed from a full trace (the nightly `index` job since
`r7367+70.2`, before that only the monthly backstop) and committed by a seat.  Until this gate, nothing
compared it with the tree: its header carries `max_age_days`, which no gate read, and the index stood
`232` receipts behind the tree, a fifth of the corpus, for `17` days without anything going red.

** WHAT THE LAG COSTS, MEASURED (r7371+70.2), AND IT IS NOT INVISIBILITY. **  `receipt_scope.load()`
walks the REGISTERED receipts, not the index, so a receipt the index lacks still enters the scope
population, on its STATIC names only (the files and modules its source names, bounded by `repo_names`).
A push editing it scopes it, and a push editing a file its source names scopes it.  What it loses are
its TRACED reads: a path built at run time, a glob's membership, a module imported by a module.  So the
lag UNDER-scopes; it does not hide.

** THE TEST. **  Two set differences over the registered receipts and the index's entries:
  NEW   registered here, absent from the index (scoped on static names only);
  GONE  in the index, no longer registered (a rename or a deletion the index has not seen).
Each fails above a COUNT tolerance, not a day bound (a day bound is the header's own note again).

** THE TOLERANCE, AND WHY IT IS A DAY'S ADDITIONS RATHER THAN A PUSH'S. **  The index can be no fresher
than its refresh, which is nightly, plus the commit after it.  So the lag a correct process allows is
the receipts one DAY can add, not one push.  Measured over `main`'s first-parent history from
2026-09-15: 27 days with an added receipt, 326 receipts, mean 12.1 a day, **maximum 25** (2026-09-28 and
2026-09-29).  `TOLERANCE = 25`.  A lag above it means the refresh has missed at least a day.  ⌗ Re-measure
when the cadence changes: the figure is a property of how fast the corpus grows, and it moves.

Exit 0 within tolerance, 1 above it.  `--counts` prints the two numbers and exits 0.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import receipt_scope as rs  # noqa: E402

TOLERANCE = 25      # the most receipts added to main in one UTC day, 2026-09-15 .. 2026-10-15 (see above)


def main():
    regs = set(rs.registered(ROOT))
    idx = json.load(open(os.path.join(ROOT, rs.INDEX)))
    have = set(idx['receipts'])
    new, gone = sorted(regs - have), sorted(have - regs)
    t = idx['traced_at']
    print(f'  READ INDEX COVERAGE -- traced at {t["commit"][:8]} on {t["date"][:10]}: '
          f'{len(have)} entries against {len(regs)} registered receipts')
    print(f'    NEW  (registered, not indexed -- scoped on static names only): {len(new)}')
    print(f'    GONE (indexed, no longer registered):                          {len(gone)}')
    print(f'    tolerance: {TOLERANCE} each -- one day of additions at the measured maximum')
    if '--counts' in sys.argv:
        return 0
    bad = [(k, v) for k, v in (('NEW', new), ('GONE', gone)) if len(v) > TOLERANCE]
    for k, v in bad:
        print(f'  ⛔ [FAIL] {k}: {len(v)} > {TOLERANCE}.  First few: ' + ', '.join(os.path.basename(x)[:40] for x in v[:5]))
    if bad:
        print('     The index has missed at least a day of refresh.  Remedy: commit the nightly `index` job\'s '
              'READ_INDEX artifact as receipts/READ_INDEX.json (or dispatch the backstop), never widen this tolerance.')
        return 1
    print('  the index covers the tree within one day of additions.')
    return 0


if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/env python3
"""check_cannot_fail.py -- EVERY CANNOT-FAIL SITE IS COUNTED, NONE IS NEW, AND THE OWED COUNT ONLY FALLS.

** A DRAFT BY NODE 70 (r7141+70.1) FOR NODE 66 TO REGISTER. **  *Written to run unchanged from `corpus/` beside
`cannot_fail_baseline.tsv`, as `check_quote_pins.py` does, and from this directory as it sits.  Not added to
`gates.yml`: registering a gate is the gate's call.*

** WHAT A CANNOT-FAIL SITE IS. **  An assertion -- or an `or`-arm that dominates one -- which is true WHATEVER is
measured: a tautology (`len(x) >= 0`, `x == x`, `... or True`), a literal verdict (`check(True, "...")`), a trivial
environment test (`'sympy' in sys.modules`), a guard whose other branch is literally `True`.  *** The defect is not
that it fails late, like a pin; it is that it never fails, so `N of N checks pass` counts it. ***

** THE MEASUREMENT IS 70's AND THIS GATE DOES NOT REIMPLEMENT IT. **  It runs `scripts/mutate_assertions.py
--cannot-fail` (r7139+70.1) and compares against the baseline.  Three checks, the same as the other two ratchets:
  ⓵ ** NEW ** -- a (receipt, class, site text) key whose live count exceeds its baseline count, or that the baseline
     does not carry.  *Except `UBIQUITOUS-ARM` (T5): reported, NOT enforced -- it is a proxy (r7139: recall 3 of 5),
     the way `REGRID` sits beside `TILT`.*
  ⓶ ** STALE ** -- a baseline key whose live count is below its baseline count.  Lower or remove the row: a
     repaired site left in the baseline is a silent permission to regress there.
  ⓷ ** THE OWED COUNT ** may only fall, against a ceiling declared HERE and nowhere else.

** THE KEY IS (receipt, class, normalised site text) WITH A COUNT, NOT A LINE AND NOT AN OCCURRENCE INDEX. **
*Ten bare `True` verdicts in one receipt are one key with count ten.  A line key goes stale on any edit above the
site; an occurrence index churns on any deletion above it; a count does neither.*

  python3 check_cannot_fail.py
  python3 check_cannot_fail.py --list      # every owed key, complete and unfiltered

Drafted r7141+70.1.  Stated for reversal.
"""
import os
import re
import subprocess
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = HERE
while not os.path.exists(os.path.join(ROOT, 'scripts', 'mutate_assertions.py')) and ROOT != os.path.dirname(ROOT):
    ROOT = os.path.dirname(ROOT)
BASELINE = os.path.join(HERE, 'cannot_fail_baseline.tsv')
INSTRUMENT = os.path.join(ROOT, 'scripts', 'mutate_assertions.py')
LINE = re.compile(r'\s*\[CANNOT-FAIL\]\[(T\w+) [^\]]*\]\s+(\S+?):\d+:\d+\s+(.*)$')
#: verdicts the ratchet does NOT count as owed
NOT_OWED = {'CONSTANT', 'NOT-A-DEFECT', 'UBIQUITOUS-ARM'}
#: the class whose NEW sites are reported and not enforced (a proxy, r7139+70.1)
REPORTED_ONLY = {'T5'}
# ⓷ the ratchet: the owed count measured on the tree this was drafted against (r7141+70.1, at 1add89bd + this
#   seat's own commits, which touch no receipt) -- NOT the 95 of r7141's text, and NOT the 95 this seat's
#   pre-registration first wrote and then corrected.  Lowering it is the point.
# ⛭ r7151 (66): 71 → 21.  The 50 P10 SCOPE-AS-CHECK sites are CONVERTED, not re-verdicted: each
#   scope statement is now PRINTED and no longer counted, so its site no longer exists and its
#   baseline row is gone rather than exempted.  ** The drop is exactly node 70's own census -- 21
#   stale rows summing to -50, every one T2, which is the control that the conversion touched the
#   class and nothing else. **  ⌈ The largest owed class in the newest instrument was this seat's
#   own authorship, which is where a ruling should land first.
CEILING = 21


def key_text(s):
    return ' '.join(s.split())


def read_baseline():
    rows = {}
    if not os.path.exists(BASELINE):
        return rows
    for ln in open(BASELINE, encoding='utf-8'):
        ln = ln.rstrip('\n')
        if not ln.strip() or ln.startswith('#'):
            continue
        p = ln.split('\t')
        if len(p) >= 5:
            rows[(p[0], p[1], p[2])] = (int(p[3]), p[4], p[5] if len(p) > 5 else '')
    return rows


def measure():
    r = subprocess.run([sys.executable, INSTRUMENT, '--cannot-fail'], cwd=ROOT, capture_output=True, text=True,
                       timeout=600)
    live = Counter()
    for ln in r.stdout.splitlines():
        m = LINE.match(ln)
        if m:
            cls, path, text = m.groups()
            live[(path, cls, key_text(text))] += 1
    return live


def main():
    print()
    print('  CANNOT-FAIL RATCHET -- is every assertion that cannot fail counted, and is the owed count falling?')
    print()
    base = read_baseline()
    if not base:
        print(f'  ⛔ no baseline at {os.path.relpath(BASELINE, ROOT)} -- this gate has no record to ratchet.')
        return 1
    live = measure()
    print(f'    the instrument reports {sum(live.values())} site(s) under {len(live)} key(s); the baseline carries '
          f'{sum(n for n, _v, _w in base.values())} under {len(base)}')
    by_v = Counter()
    for (_p, _c, _t), (n, v, _w) in base.items():
        by_v[v] += n
    print(f'    by verdict (sites): {dict(sorted(by_v.items()))}')
    owed = sum(n for (_p, _c, _t), (n, v, _w) in base.items() if v not in NOT_OWED)
    print(f'    OWED: {owed}   ** may only fall **   (not owed: {", ".join(sorted(NOT_OWED))})')

    if '--list' in sys.argv:
        print()
        for (p, c, t), (n, v, _w) in sorted(base.items()):
            if v not in NOT_OWED:
                print(f'    [{v} x{n}] {p}\n               {t}')
        return 0

    bad = 0
    new, reported = [], []
    for k, n in sorted(live.items()):
        had = base.get(k, (0, '', ''))[0]
        if n > had:
            (reported if k[1] in REPORTED_ONLY else new).append((k, n - had))
    if new:
        print()
        print(f'  ⛔ {len(new)} NEW CANNOT-FAIL KEY(S) or count rise(s) -- an assertion that cannot fail was added:')
        for (p, c, t), d in new[:40]:
            print(f'    [FAIL] +{d} {c} {p}\n           {t}')
        print('     ⌗ A check that cannot fail adds a PASS to the count and tests nothing.  If it is a scope')
        print('       statement, PRINT it (SCOPE-AS-CHECK, r7141); if it is a real check, make it able to fail.')
        bad += 1
    else:
        print('    no new site: the class has not grown.')
    for (p, c, t), d in reported:
        print(f'    [REPORTED, not enforced] +{d} {c} {p}: {t}')

    gone = []
    for k, (n, _v, _w) in sorted(base.items()):
        if live.get(k, 0) < n:
            gone.append((k, n - live.get(k, 0)))
    if gone:
        print()
        print(f'  ⛔ {len(gone)} STALE BASELINE ENTR(Y/IES) -- fewer live sites than recorded.  Lower or remove the row:')
        for (p, c, t), d in gone[:40]:
            print(f'    [STALE] -{d} {c} {p}\n            {t}')
        bad += 1
    else:
        print('    no stale entry: every count still describes the tree.')

    if owed > CEILING:
        print()
        print(f'  ⛔ THE OWED COUNT ROSE: {owed} against the declared ceiling {CEILING}.')
        bad += 1
    else:
        print(f'    the ratchet holds: {owed} owed against a ceiling of {CEILING}')

    print()
    if bad:
        print('  ⛔ THE CANNOT-FAIL RATCHET IS RED.')
        return 1
    print('  every assertion that cannot fail is counted, none is new, and the owed count is held.')
    return 0


if __name__ == '__main__':
    sys.exit(main())

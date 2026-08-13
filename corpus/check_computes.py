#!/usr/bin/env python3
"""check_computes.py -- the `COMPUTES:` header's PRESENCE, on the population where it does work.

** WHY, AND WHY NOT SOONER. **  `L-230` recorded the uptake as "flat at 40 of 357".  r2551 recounted it:
** 39/309 = 12.6% at r2447 -> 40/357 = 11.2% -> 40/395 = 10.1% **.  ** The count was flat; the SHARE was
falling **, and this line wrote ** 84 receipts in one session and used the header once **.
  ⇒ ** And `L-230`'s ⓵ closed the instrument question at r2447 because "no gate can read a quantifier" --
    which is true of the header's TRUTH and false of its PRESENCE. **

** ⛭ AND THE ROUTE THE ROW CARRIED WAS WRONG.  It said "make COMPUTES: universal". **  Measured:
** ~85% of receipts name no concrete parameter at all **, so a universal check would demand a scope
declaration from receipts that ** have no scope **.
  ⇒ *** The header exists for the F14 class -- a receipt running at ONE parameter while the sentence
      citing it means ANOTHER -- and that class only exists for receipts that RUN at a parameter.  So
      the population is not 397; it is 102. ***

** THE MEASUREMENT, r2557: **   102 receipts pin a concrete parameter · 11 of those declare · ** 91 do
not ** · 30 declare without a numeric pin (harmless, and see the LIMIT below).

** ⚠ SO IT SHIPS GRANDFATHERED, and that is the whole design. **  91 failures on day one is a gate
nobody can run, and r2553's rule says a check at that rate teaches nodes to ignore it.
  ⇒ *** The 91 are frozen into a baseline.  A receipt ADDED after r2557 that pins a concrete parameter
      must declare its scope.  The numerator then grows with the denominator, which is the only thing
      that turns a falling share around -- and it is exactly what would have caught this line's
      84-in-1. ***
  ⌗ ** The baseline is a list of PATHS, not a count: ** a count would let a new offender hide behind a
  removed one.

** ⚠⚠ THE LIMIT, stated rather than buried. **  "Pins a concrete parameter" is detected by a regex over
assignments like `alpha = 1`, `M = 0.12`, `LMAX = 3000`.  ** It is a PROXY: ** 30 receipts declare
`COMPUTES:` without matching it, which means either they scope something non-numeric (a metric, a
branch) or the regex misses their form.  *** So this gate under-counts the population it should police,
and the direction of the error is the safe one -- it never demands a declaration from a receipt that has
nothing to declare. ***

    python3 corpus/check_computes.py
    python3 corpus/check_computes.py --baseline    # reprint the frozen list

Written r2557.  Stated for reversal.
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
BASELINE = os.path.join(HERE, 'computes_baseline.txt')

PARAM = re.compile(r'(?:^|\W)(?:alpha|M|M_N|LMAX\w*|CRPHI|r_0)\s*=\s*[\d.]+', re.M)


def receipts():
    return sorted(glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True))


def classify():
    """Return (pins_and_declares, pins_and_does_not, declares_without_pin)."""
    ok, need, extra = [], [], []
    for f in receipts():
        s = open(f, encoding='utf-8', errors='replace').read()
        pins = bool(PARAM.search(s))
        dec = 'COMPUTES:' in s
        rel = os.path.relpath(f, ROOT)
        if pins and dec:
            ok.append(rel)
        elif pins:
            need.append(rel)
        elif dec:
            extra.append(rel)
    return ok, need, extra


def load_baseline():
    if not os.path.exists(BASELINE):
        return None
    return {l.strip() for l in open(BASELINE, encoding='utf-8') if l.strip()
            and not l.startswith('#')}


def main():
    if '--baseline' in sys.argv:
        for p in sorted(load_baseline() or []):
            print(p)
        return 0

    print()
    print('  check_computes -- does every receipt that PINS a parameter declare its scope?')
    print()
    ok, need, extra = classify()
    total = len(ok) + len(need)
    print(f'  {len(receipts())} receipt(s); {total} pin a concrete parameter.')
    print(f'    declaring COMPUTES:      {len(ok)}')
    print(f'    not declaring            {len(need)}')
    print(f'    declaring without a pin  {len(extra)}  (harmless -- see the LIMIT in the docstring)')
    print()

    base = load_baseline()
    if base is None:
        print('  no baseline file; writing one from the current state.')
        with open(BASELINE, 'w', encoding='utf-8') as fh:
            fh.write('# ** THE GRANDFATHERED SET, frozen r2557. **  Receipts that pin a concrete\n')
            fh.write('# parameter and do not declare COMPUTES:.  A receipt ADDED after r2557 must\n')
            fh.write('# declare.  ** This is a list of PATHS, not a count -- a count would let a new\n')
            fh.write('# offender hide behind a removed one. **\n')
            for p in sorted(need):
                fh.write(p + '\n')
        print(f'  wrote {len(need)} path(s) to {os.path.basename(BASELINE)}')
        return 0

    new = sorted(set(need) - base)
    fixed = sorted(base - set(need))
    if fixed:
        print(f'  ⛭ {len(fixed)} grandfathered receipt(s) have since declared their scope:')
        for p in fixed[:6]:
            print(f'       {p}')
        print()
    if new:
        for p in new:
            print(f'    [FAIL] {p} pins a concrete parameter and declares no COMPUTES: scope')
        print()
        print('    ⛔ THIS IS THE F14 CLASS: a receipt running at one parameter while the sentence')
        print('       citing it means another.  ** The header is the only thing that lets a gate see')
        print('       the difference, and its share has been FALLING while the corpus grows. **')
        print('    ⌗ Grandfathered receipts are exempt; this fires only on ones added since r2557.')
        return 1

    print('  no NEW receipt pins a parameter without declaring its scope.')
    print(f'  ⌗ {len(base)} grandfathered; the bar is that the number never rises.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

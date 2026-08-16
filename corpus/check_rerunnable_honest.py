#!/usr/bin/env python3
"""check_rerunnable_honest.py -- A PERMANENTLY-RED RECEIPT MUST SAY THAT IT IS ONE.

** WHY.  r2901-r2902. **  *** Sweeping the 45 receipts whose checks assert register state found six
failures, and ** three were not defects **: `R1_a_protected_row_was_corrupt`, `M1_the_merge_of_my_own_
revision` and `R1_the_registry_was_checked` each ** verified a REPAIR at its own revision ** ("the repair
loses no distinct word, file-wide").  Any later legitimate edit to a protected row breaks them, and this
session made hundreds. ***

  ⇒ ** A check that verifies a repair cannot survive later edits. **  *** Those receipts are CORRECT
      about what they did and PERMANENTLY RED, and the corpus had ** no convention distinguishing them
      from invariants ** -- not a naming rule, not a directory, not a flag.  Checked: prefixes are by
      series, directories by paper. ***

  ⌗ ** And that is how a suite becomes noise. **  *** A "run everything" gate would report three
    failures forever, and the reader learns to skim. ***

** THE CONVENTION, ADDED r2902. **  *** A receipt that cannot be re-run green carries
`# RERUNNABLE: NO — POINT-IN-TIME` in its header, with the reason. ***

** WHAT THIS CHECKS. **  *** Every receipt marked `RERUNNABLE: NO` states a reason on the following
lines -- so the mark can never become a way to silence a real failure. ***

    python3 corpus/check_rerunnable_honest.py

Written r2902.  Stated for reversal.
"""
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

MARK = re.compile(r'#\s*RERUNNABLE:\s*NO', re.I)


def main():
    print()
    print('  check_rerunnable_honest -- does every permanently-red receipt say why?')
    print()
    files = sorted(glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True))
    marked, bad = 0, []
    for f in files:
        t = open(f, encoding='utf-8', errors='replace').read()
        m = MARK.search(t)
        if not m:
            continue
        marked += 1
        # ** r2902a: the first form measured prose in a 700-char window, and UNRELATED
        # comment blocks below the mark satisfied it -- the seed did not fire.  *** The
        # reason must be in the CONTIGUOUS comment block the mark opens: read forward only
        # while lines are comments, and stop at the first that is not. ***
        tail = t[m.end():].split('\n')[1:]
        block = []
        for ln in tail:
            if not ln.lstrip().startswith('#'):
                break
            block.append(ln)
        if len(re.sub(r'[#\s*]', '', '\n'.join(block))) < 80:
            bad.append(os.path.basename(f)[:46])

    print(f'  {len(files)} receipt(s); {marked} marked RERUNNABLE: NO')
    if bad:
        print()
        for b in bad:
            print(f'    [FAIL] {b} is marked RERUNNABLE: NO with no reason given')
        print()
        print('    ⛭ ** The mark must never become a way to silence a real failure. **')
        return 1

    print('  every permanently-red receipt states its reason.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

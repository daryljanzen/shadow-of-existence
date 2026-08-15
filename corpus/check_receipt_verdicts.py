#!/usr/bin/env python3
"""check_receipt_verdicts.py -- A RECEIPT MUST NOT ASSERT TWO VERDICTS ON THE SAME CHECK.

** WHY.  r2832-r2833. **  *** `kills/PO-9.md` said at the top ** "④ NOW CLEARS as of r2642" ** and at
its section heading ** "④ CHAIN CHECK --- ⛔ DOES NOT CLEAR, and that is this receipt's output" **.  The
update was APPENDED below and the heading left standing, so the receipt asserted both -- and ** the
stale heading blocked a strike for 190 revisions ** while the receipt's own header said otherwise. ***

  ⇒ ** A receipt PASSING its run is not a receipt whose TEXT agrees with itself. **  *** The run
      executes the checks; nothing ever read the prose that reports them. ***

** WHAT THIS CHECKS. **  *** Both directions, over `receipts/` and `kills/`: a numbered check whose
heading says it CLEARS while the body says it does not, and a heading saying it does NOT clear while the
body says it now does. ***

  ⌗ ** Swept clean at r2833 ** -- *** 606 files, zero.  The pattern was first verified against the known
    `PO-9` instance before the clean result was believed, because a scan that cannot find the defect it
    was built for returns clean either way. ***

    python3 corpus/check_receipt_verdicts.py

Written r2833.  Stated for reversal.
"""
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

POS = re.compile(r'\b(NOW CLEARS|CLEARS|VERIFIED|CONFIRMED|PASSES)\b')
NEG = re.compile(r'\b(DOES NOT CLEAR|FAILS|DOES NOT HOLD|NOT VERIFIED)\b')
HEAD = re.compile(r'^[^\n]*(?:VERDICT|CONCLUD|RESULT|CHECK —|## )[^\n]*$', re.M)
NUM = re.compile(r'[①②③④⑤]')


def main():
    print()
    print('  check_receipt_verdicts -- does any receipt assert two verdicts on one check?')
    print()
    files = (sorted(glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True))
             + sorted(glob.glob(os.path.join(ROOT, 'kills', '*.md'))))

    bad = []
    for f in files:
        t = open(f, encoding='utf-8', errors='replace').read()
        for h in HEAD.findall(t):
            num = NUM.search(h)
            if not num:
                continue
            n = re.escape(num.group(0))
            # ** heading says it clears, body says it does not, on the same numbered check **
            if POS.search(h) and re.search(n + r'[^\n]{0,70}(DOES NOT CLEAR|FAILS)', t):
                bad.append((os.path.relpath(f, ROOT), h.strip()[:60], 'clears/does-not'))
            # ** and the reverse, which is the shape PO-9 actually had **
            elif NEG.search(h) and re.search(n + r'[^\n]{0,70}(NOW CLEARS|CLEARS)', t):
                bad.append((os.path.relpath(f, ROOT), h.strip()[:60], 'does-not/clears'))

    print(f'  {len(files)} receipt file(s) scanned')
    if bad:
        print()
        for rel, h, kind in bad[:10]:
            print(f'    [FAIL] {rel}')
            print(f'           {kind}: "{h}"')
        print()
        print('    ⛭ ** When a check\'s verdict is updated, EDIT the verdict — never append below it. **')
        print('       *** A receipt that says both is read by whichever line a gate happens to hit. ***')
        return 1

    print('  no receipt asserts two verdicts on one check.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

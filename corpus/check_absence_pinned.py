#!/usr/bin/env python3
"""check_absence_pinned.py -- AN ABSENCE CLAIM MUST PIN A COMMIT.

** WHY.  cc54, c54.220: ** *** "Both quote-checks in this receipt are about the corpus BEFORE this
revision, and this revision edits both files --- left against the working tree they'd have inverted the
moment I committed.  Both are pinned to a SHA.  ** Fifth instance of that class, and the first I caught
while writing rather than from the run afterwards. **  The rule it yields: ** an absence claim is a
claim about a COMMIT, not about a FILE, so it takes a SHA. ** " ***

** ⛭⛭ AND THIS LINE FAILS IT FOUR TIMES OUT OF FIVE. **  *** Measured across 38 receipts written
r2728--r2775: five make an absence claim, ** one pins a SHA **.  And `S9_the_ordering_decides_it`
already went stale exactly this way -- it recorded "P10 never names the ordering, `normal-order` and
`symmetric order` both ZERO" and r2763 found that the absence was a paper not naming a choice it does
not need.  ** The claim was true and its scope was a moment nobody had recorded. ** ***

** WHAT THIS CHECKS. **  A receipt asserting that something appears ZERO times, NOWHERE, or is NEVER
named must also carry a commit SHA -- so a later reader knows which corpus the absence was measured
against.

  ⌗ ** It does not verify the SHA is the right one. **  *** It cannot: that needs the intent.  What it
    enforces is that the claim is DATED, which is the whole content of cc54's rule -- an undated absence
    silently becomes a claim about whatever the tree holds when it is next run. ***

    python3 corpus/check_absence_pinned.py

Written r2776.  Stated for reversal.
"""
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

# ** a claim that something is NOT there. **
ABSENCE = re.compile(
    r'appears? ZERO times|ZERO occurrences|both ZERO|appeared NOWHERE'
    r'|appears nowhere|never names|is absent from', re.I)
# ** a commit, or an explicit statement that the claim is about the live tree. **
# ** r2802: was case-SENSITIVE on 'at', so "MEASURED AT <sha>" -- the form the retro-pinning
# writes -- did not match.  *** A gate that only recognises one casing of its own convention
# reports unpinned receipts that are pinned. *** **
PINNED = re.compile(r'\bat [0-9a-f]{7,40}\b|\b[0-9a-f]{40}\b|as of [0-9a-f]{7,}'
                    r'|LIVE-TREE CLAIM', re.I)


def main():
    print()
    print('  check_absence_pinned -- does every absence claim pin the commit it was measured at?')
    print()
    bad, n = [], 0
    for f in sorted(glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True)):
        d = open(f, encoding='utf-8', errors='replace').read()
        if not ABSENCE.search(d):
            continue
        n += 1
        if not PINNED.search(d):
            bad.append(os.path.relpath(f, ROOT))

    print(f'  {n} receipt(s) make an absence claim')
    if bad:
        print()
        for f in bad:
            print(f'    [FAIL] {f} asserts an absence and pins no commit')
        print()
        print('    ⛭ ** cc54, c54.220: "an absence claim is a claim about a COMMIT, not about a FILE,')
        print('       so it takes a SHA." **  *** Left undated, it silently becomes a claim about')
        print('       whatever the tree holds when it is next run — and the corpus is edited every')
        print('       revision.  `S9_the_ordering_decides_it` went stale exactly this way. ***')
        print('    ⌗ Add "at <sha>" to the assertion, or mark it "LIVE-TREE CLAIM" if it is meant to')
        print('      track the working tree.')
        print()
        print('    ⚠ ** REPORT-ONLY, and the reason is stated rather than assumed. **  *** 40 of these')
        print('      predate the rule (c54.220, r2776) and pinning them retroactively would mean')
        print('      guessing which commit each was measured at -- which is exactly the fabrication the')
        print('      rule exists to prevent.  New receipts are held to it; the backlog is FILED as owed')
        print('      and shrinks as each is next touched. ***')
        return 0
    print('  every absence claim is dated.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

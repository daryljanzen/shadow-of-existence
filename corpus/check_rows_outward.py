#!/usr/bin/env python3
"""check_rows_outward.py -- EVERY INDEX ROW CLAIMING A RUN MUST NAME A FILE THAT EXISTS.

** WHY.  cc54, c54.222: ** *** "`X4_singularity_types.py` and `X3_seam_schwarz_reflection.py` have
never existed in any of the 486 commits reachable from any ref --- ** both carry ✔✔, both certify a
run, and both are printed into P3's, P7's and the corpus appendix marked [OK] **.  ** The registry was
checked from citations inward and never from rows outward. ** " ***

  ⇒ ** Verified here independently: ** *** `git log --all --diff-filter=A` returns ZERO for both across
      every ref, and neither is on disk.  ** A receipt registered ✔✔ has never exited zero in any tree,
      for 230 commits. ** ***

** ⛭⛭ THE DIRECTION IS THE WHOLE POINT. **  *** Checking CITATIONS INWARD asks "does every cited
receipt resolve?" and passes when a row is cited by nobody.  Checking ROWS OUTWARD asks "does every
registered row name something real?" -- ** and that is the question no reader was asking **.  Every
reader resolved a path with `os.path.exists` and did nothing when it failed. ***

** WHAT THIS CHECKS. **  Every `INDEX.md` row naming a `.py` receipt and carrying a run-claim mark
(`✔✔`) must name a file present on disk.

  ⌗ ** It does not run them ** -- *** `check_receipts` does that, and it is exactly the reader that
    skipped these two.  This asks only the prior question: ** is there a file at all? ** ***

    python3 corpus/check_rows_outward.py

Written r2784.  Stated for reversal.
"""
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
INDEX = os.path.join(ROOT, 'receipts', 'INDEX.md')

NAMED = re.compile(r'`([A-Za-z0-9_/.\-]+\.py)`')
CLAIMS_RUN = '✔✔'


def main():
    print()
    print('  check_rows_outward -- does every row claiming a run name a file that exists?')
    print()
    if not os.path.exists(INDEX):
        print('  [FAIL] receipts/INDEX.md is missing')
        return 1

    lines = open(INDEX, encoding='utf-8', errors='replace').read().split('\n')
    checked, missing = 0, []
    for n, l in enumerate(lines, 1):
        if not l.startswith('|') or CLAIMS_RUN not in l:
            continue
        # ** a row already marked ✘ NEVER EXISTED is the FIX, not the defect.  *** It keeps the
        # filename so the citation resolves to its own withdrawal (r2784), which is exactly
        # why the name is still there to match. *** **
        if 'NEVER EXISTED' in l:
            continue
        for m in NAMED.finditer(l):
            path = m.group(1)
            checked += 1
            base = os.path.basename(path)
            # ** r2784: searching only receipts/ was itself a narrow selector -- the r2783
            # lesson, made again while writing the gate for it.  *** Rows legitimately name
            # storyboard_receipts/ and scripts/ too. *** **
            if not glob.glob(os.path.join(ROOT, '**', base), recursive=True):
                missing.append((n, path))

    print(f'  {checked} row-claim(s) checked')
    if missing:
        print()
        for n, path in missing:
            print(f'    [FAIL] line {n}: `{path}` carries ✔✔ and is not on disk')
        print()
        print('    ⛭ ** A row claiming a run must name something that can run. **  *** If the file was')
        print('       renamed, fix the row.  If it never existed, mark the row ✘ and say so — ** keep')
        print('       the row rather than deleting it, so the citation resolves to its own')
        print('       withdrawal. ** ***')
        return 1
    print('  every run-claiming row names a file on disk.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

#!/usr/bin/env python3
"""Find receipt PINS that no longer match any paper -- the pin debt's predictor.

Written r3960 by node 60, while working the debt Daryl queued at r3908.

** WHY THIS EXISTS. **  `scripts/run_all_receipts.py` takes ~17 minutes and reports THAT a
receipt failed.  This takes under a second and reports WHICH STRING no longer matches, which
is the whole of the diagnosis for the largest class in `receipts/PIN_DEBT.txt`.  Twenty-four
of the first repairs were found by running the suite and reading output; the last four were
found by scanning, and the scan was faster and named the literal.

** WHAT IT LOOKS FOR. **  A string literal that is membership-tested (`'...' in var`) against a
variable this receipt ASSIGNED FROM A `corpus/*.tex` FILE, and that occurs nowhere in any paper.

⛔ **AND THE RESTRICTION TO PAPER-BOUND VARIABLES IS THE WHOLE POINT, LEARNED BY GETTING IT
WRONG.**  A first version tested every `'...' in var` against the corpus and reported 304 broken
pins across 143 files -- against 39 receipts that actually fail.  *** An order of magnitude out,
because most such tests are against register rows, `PROTECTED_OPEN.md`, ledger notes or a
receipt's own source, and those literals are not supposed to be in a paper. ***  The number was
only visibly wrong because a known count existed to check it against.  ⇒ **A scan whose result
cannot be cross-checked against something already measured should not be trusted, and this one
prints both numbers so the check stays available.**

⌗ It is a PREDICTOR, not a verdict: a pin can match a paper and still be wrong (pinning the
paper's self-narration, or a locus the corpus has since corrected -- both met in this debt), and
a receipt can fail for reasons that are not pins at all.  Run the suite to know; run this to know
where to look.
"""
import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAPERS = {os.path.basename(f): re.sub(r'\s+', ' ', open(f, encoding='utf-8', errors='replace').read())
          for f in glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))}
ALL = ' '.join(PAPERS.values())

ASSIGN = [re.compile(r"(\w+)\s*=\s*[^\n]*?'corpus'[^\n]*?'([A-Za-z0-9_\-]+\.tex)'"),
          re.compile(r"(\w+)\s*=\s*[^\n]*?corpus/([A-Za-z0-9_\-]+\.tex)")]
PIN = re.compile(r"'((?:[^'\\]|\\.){25,220})'\s*in\s+(\w+)\b")


def main():
    broken, examined, files_with_papers = {}, 0, 0
    for f in sorted(glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True)):
        t = open(f, encoding='utf-8', errors='replace').read()
        pv = set()
        for a in ASSIGN:
            pv |= {m.group(1) for m in a.finditer(t)}
        if not pv:
            continue
        files_with_papers += 1
        for m in PIN.finditer(t):
            if m.group(2) not in pv:
                continue
            examined += 1
            lit = m.group(1).replace('\\\\', '\\').replace("\\'", "'")
            if lit.strip() and lit not in ALL:
                broken.setdefault(os.path.relpath(f, ROOT), []).append(lit)

    print()
    print('  BROKEN PINS -- receipt strings tested against a paper that no paper contains')
    print()
    print(f'  {files_with_papers} receipts read a paper; {examined} pins into paper text examined.')
    print(f'  ** {sum(len(v) for v in broken.values())} literals in {len(broken)} files match nowhere. **')
    print()
    for f, v in sorted(broken.items()):
        print(f'    {f}')
        for lit in v:
            print(f'        {lit[:100]!r}')
    print()
    print('  ⌗ A predictor, not a verdict.  A pin can match and still be wrong (self-narration, or')
    print('    a locus the corpus has corrected); a receipt can fail for reasons that are not pins.')
    print('  ⌗ Cross-check the count against the suite before trusting it: an early version of this')
    print('    scan reported 304 against 39 real failures because it tested pins into register rows')
    print('    and .md files as though they were papers.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

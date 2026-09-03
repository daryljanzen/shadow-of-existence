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

⛔ **AND A SECOND RESTRICTION, LEARNED THE SAME WAY (r3962).**  A variable holding a paper *at an
old commit* -- `git show SHA:corpus/p.tex`, `_at(rev, ...)` -- is not the live paper, and a pin into
it is SUPPOSED to match nothing now: that is c54.226's own rule, both ends of a quotation pinned.
This scan reported five such pins as broken while the actual fault in that cluster was one
capital letter.  ⇒ **Before believing a scan, check what its hits have in common; a shared shape
among the false ones is the missing restriction.**

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

ASSIGN = [re.compile(r"(\w+)\s*=\s*([^\n]*?'corpus'[^\n]*?'[A-Za-z0-9_\-]+\.tex')"),
          re.compile(r"(\w+)\s*=\s*([^\n]*?corpus/[A-Za-z0-9_\-]+\.tex)")]
PIN = re.compile(r"'((?:[^'\\]|\\.){25,220})'\s*in\s+(\w+)\b")

#: ** ⛭ A VARIABLE HOLDING A PAPER AT AN OLD COMMIT IS NOT THE LIVE PAPER, AND A PIN INTO IT IS
#: ** SUPPOSED TO MATCH NOWHERE NOW.  That is c54.226's rule -- a quotation is a claim about a FILE
#: ** AT A COMMIT, so both ends get pinned and the historical end is deliberately stale.  A first
#: ** version of this scan reported those five as broken alongside the real ones (r3962).
#: ⌗ and the shapes it must recognise were found by CHECKING ITS HITS, not by guessing: a first
#: version matched `_at(` and missed `at(CLAIM_SHA, 'corpus/matter_sector_paper.tex')`, so two more
#: receipts read as debt while both pass.  ** A revision is named by a call through git, a literal
#: SHA, or a constant whose name says so -- all three, because all three are in use here. **
HIST = re.compile(r"\bgit\b|['\"]show['\"]|\b_?at\(|\b[0-9a-f]{7,40}:"
                  r"|\b[A-Za-z_]*(?:_SHA|_REV|_COMMIT|_THEN)\b")


def main():
    broken, examined, files_with_papers, historical = {}, 0, 0, 0
    for f in sorted(glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True)):
        #: ⌗ COMMENT LINES ARE DROPPED FIRST, and the reason is a hit this scan produced against
        #: itself (r3962): a repair that QUOTES the pin it replaced -- "this check read `'...' in
        #: p15 or ...`" -- put the dead literal back in the file as documentation, and the scan
        #: read the documentation as the debt.  ** A repair note explaining a broken pin is the
        #: opposite of a broken pin, and a scan that cannot tell them apart punishes writing the
        #: note. **  Only executable lines are scanned.
        t = '\n'.join(l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
                      if not l.lstrip().startswith('#'))
        pv, hist = set(), set()
        for a in ASSIGN:
            for m in a.finditer(t):
                pv.add(m.group(1))
                if HIST.search(m.group(2)):
                    hist.add(m.group(1))
        pv -= hist
        #: ⌗ count the historical pins BEFORE the bail-out: four receipts read a paper ONLY at an old
        #: commit, and skipping them first made the two printed numbers disagree by exactly those --
        #: 15 dropped from the debt against 14 reported as excluded.  A derived counter that does not
        #: reconcile with the drop it explains is wrong, and this one was, for one edit.
        historical += sum(1 for m in PIN.finditer(t) if m.group(2) in hist)
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
    print(f'  ⌗ {historical} further pins go into a paper AT AN OLD COMMIT and are excluded: they are')
    print('    SUPPOSED to match nowhere now.  Counting them as debt is how this scan first read the')
    print('    `Reach: ...` cluster as five broken pins when three receipts shared one broken character.')
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

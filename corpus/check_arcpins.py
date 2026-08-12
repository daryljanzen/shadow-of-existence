#!/usr/bin/env python3
"""check_arcpins.py -- THE COUPLING LINT: a receipt that pins REGISTER PROSE by exact substring breaks
when the register is reworded, and nothing checked it.

** WHY, and cc54 found it with a full run rather than a read. **  Sweeping every receipt with camb
available, cc54 reported: "** 23 receipts pin THE_LIVE_ARC.md prose by exact substring; 3 have drifted,
20 still match --- but every one of the 20 is exposed to the next arc regeneration. **  The coupling is
unlinted: nothing checks that a receipt's arc-pins are still present."

  ⇒ ** And the visibility was the worst part: check_receipts_run counts them as REAL failures, so the
    nightly heavy gate goes red -- while the fast tier never runs receipts, so ** arc-pin drift is
    invisible on push ** and surfaces only in a run somebody has to wait for. **

** ⛭⛭ AND THE RULE THE THREE FAILURES TAUGHT, which is why this is a lint and not just a fixer: **

  *** A RECEIPT ASSERTS AGAINST SOURCES, NOT AGAINST THE REGISTER. ***

  The register is prose ** this line rewrites **: rows are narrowed, corrected, struck and re-worded
  every few revisions, by design.  A paper, a computation, a spectrum file -- those are the things a
  claim is ABOUT.  ** Pinning the register makes a receipt fail when the corpus improves, which is
  exactly backwards. **

  ⌗ The three that drifted show the three ways it goes wrong, and only ONE is a rewording:
    * ** B3 ** pinned an OVERCLAIM this line then CORRECTED (r2470) -- the phrase is gone because the
      error was fixed.  ⇒ re-anchored to the CORRECTION.
    * ** F1 ** pinned an INSTRUCTION on a row that was later STRUCK (r2468) -- historical.  ⇒
      re-anchored to the row's current finding.
    * ** I1 ** pinned a claim the corpus has since ** FALSIFIED **: it asserted the stratum was unbuilt,
      and r2514 exhibited it.  ⇒ *** not a re-anchor at all -- the CLAIM changed, and pretending
      otherwise would have hidden a real supersession behind a string fix. ***
  ⇒ ** So a drifted pin is not always a wording problem, and a mechanical re-anchor can bury a result. **
    That is why this REPORTS and does not rewrite.

** WHAT IT CHECKS. **  Every receipt that reads THE_LIVE_ARC, and every quoted substring it tests
against that text.  A pin that no longer resolves is reported with the receipt, the missing string, and
the reminder that a drifted pin may mean the CLAIM moved rather than the words.

⚠ ** LINT, NOT A GATE. **  A receipt may legitimately pin the register -- when its subject IS the
register (the stale-field findings, the ID-band work).  ** No script can tell those from the rest, so
this reports and never fails the turn ** -- the same reason check_loci, check_depth and check_settings
are lints.

    python3 corpus/check_arcpins.py
    python3 corpus/check_arcpins.py --all    # list every pin, resolving or not

Written r2516, from cc54's finding.  Stated for reversal.
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
ARC = os.path.join(ROOT, 'THE_LIVE_ARC.md')

# the ways a receipt tests a string against the arc text
PATTERNS = [
    re.compile(r"'([^']{20,})'\s+in\s+arc\b"),
    re.compile(r'"([^"]{20,})"\s+in\s+arc\b'),
]


def main():
    show_all = '--all' in sys.argv
    print()
    print('  check_arcpins -- do receipts still resolve against the register they pin?')
    print()
    if not os.path.exists(ARC):
        print('  THE_LIVE_ARC.md absent; nothing to check.')
        return 0
    raw = open(ARC, encoding='utf-8', errors='replace').read()
    flat = re.sub(r'\s+', ' ', raw)
    low, lowflat = raw.lower(), flat.lower()

    pinning, pins, drifted = 0, 0, []
    for f in sorted(glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True)):
        s = open(f, encoding='utf-8', errors='replace').read()
        if 'THE_LIVE_ARC' not in s:
            continue
        pinning += 1
        rel = os.path.relpath(f, ROOT)
        for pat in PATTERNS:
            for m in pat.finditer(s):
                q = m.group(1)
                pins += 1
                # ** match the way the receipt does: some lower() the arc, so accept either. **
                ok = q in raw or q in flat or q.lower() in low or q.lower() in lowflat
                if show_all:
                    print(f"    {'OK  ' if ok else 'MISS'}  {rel}\n            {q[:78]!r}")
                if not ok:
                    drifted.append((rel, q))

    print(f'  {pinning} receipts read THE_LIVE_ARC; {pins} quoted pins tested.')
    print()
    if drifted:
        print(f'  ⚠ {len(drifted)} pin(s) NO LONGER RESOLVE:')
        for rel, q in drifted:
            print(f'     {rel}')
            print(f'        missing: {q[:78]!r}')
        print()
        print('  ⛭ AND A DRIFTED PIN IS NOT ALWAYS A WORDING PROBLEM.  Of the three cc54 found:')
        print('     one pinned an OVERCLAIM that was later CORRECTED, one an INSTRUCTION on a row')
        print('     later STRUCK, and one a claim the corpus has since ** FALSIFIED **.')
        print('     ** Re-anchor mechanically and you bury a supersession.  Read the row. **')
    else:
        print('  every pin resolves.')
    print()
    print('  ⌗ THE RULE: ** a receipt asserts against SOURCES, not against the register. **  The')
    print('    register is prose that gets rewritten by design; a paper or a computation is the thing')
    print('    a claim is ABOUT.  ** Pinning the register makes a receipt fail when the corpus')
    print('    improves, which is exactly backwards. **')
    print('  ⚠ LINT, not a gate: a receipt whose SUBJECT is the register may legitimately pin it, and')
    print('    no script can tell those from the rest.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

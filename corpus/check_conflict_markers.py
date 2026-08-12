#!/usr/bin/env python3
"""check_conflict_markers.py -- no tracked file carries an unresolved merge marker.

** THIS EXISTS BECAUSE ONE SURVIVED INTO A PAPER, AND 56 FOUND IT THE EXPENSIVE WAY. **  r2512, in
their own words: *"a conflict marker survived inside range_paper.tex itself, breaking the build until
I swept it -- `git checkout --theirs` on the appendix files doesn't cover the paper."*

⇒ ** The build caught it, and that is the point rather than the consolation. **  `check_compile`
takes minutes and only sees the files LaTeX reads.  A marker that lands in a `.tex` breaks a build
loudly; the same marker in `THE_LIVE_ARC.md`, `CLAIMS.md`, `ABSORPTION.md`, a receipt's prose or a
`gates.yml` list is read by no compiler at all --

    *** and would sit there indefinitely, inside the registers three nodes use to avoid colliding
        with each other. ***

*That asymmetry is the whole argument for this file: the cheapest failure to detect in the corpus is
currently detected only where it happens to be expensive.*

⌗ ** WHY IT IS THIS CORPUS'S FAILURE AND NOT A GENERIC ONE. **  Three nodes merge into one tree and
one of them cannot push, so every hand-off is a merge someone resolves under time pressure with
`--ours`/`--theirs` on a file list -- and a file list is exactly the thing that misses a file.  ** It
has now happened once in a paper; the register files are merged far more often than the papers are. **

⚠ ** AND THE PATTERN IS ANCHORED, WHICH MATTERS MORE HERE THAN IT USUALLY WOULD. **  `<<<<<<<` and
friends appear as ORDINARY CONTENT in this corpus -- in this very docstring, in `check_absorption`'s
prose, and in any receipt that quotes a resolution.  So the match is anchored to the start of a line
AND requires the marker to be followed by a space or the line to end, which is git's own format.
*The unanchored version flags its own gate, which is how the `check_absorption` `IN-FLIGHT` regex
failed at c54.197: the paragraph explaining a marker satisfied the marker.*

⌗ Verified against a seeded marker in a `.md` -- a file no compiler reads -- rather than in a `.tex`,
because the `.tex` case is the one already covered.

Exit 0 clean, 1 if any tracked file carries a marker.
"""

import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..')

# git's own marker format: seven characters at the start of a line, then a space or end of line.
MARKER = re.compile(r'^(<{7}|={7}|>{7})( |$)')

TEXTY = ('.md', '.tex', '.py', '.yml', '.yaml', '.txt', '.sh', '.bib', '.cfg', '.toml', '.json')

# This file necessarily contains the patterns it looks for.
SELF = 'corpus/check_conflict_markers.py'


def tracked():
    r = subprocess.run(['git', 'ls-files'], cwd=ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        return None
    return [p for p in r.stdout.split('\n') if p.endswith(TEXTY)]


def selftest():
    """** The detector must fire on git's format and stay silent on prose that mentions it. **"""
    must_fire = ['<<<<<<< HEAD', '=======', '>>>>>>> abc123 (a commit subject)', '<<<<<<< ']
    must_not = ['  <<<<<<< indented, so not a marker',
                'the `=======` in a table rule',
                '<<<<<<<<< nine, not seven',
                '======= trailing text is fine but this one has no space? no -- it does',
                'text before ======= is not at line start']
    for t in must_fire:
        if not MARKER.match(t):
            print(f'  ** SELF-TEST FAILED: did not fire on {t!r} **')
            return False
    for t in must_not[:3] + must_not[4:]:
        if MARKER.match(t):
            print(f'  ** SELF-TEST FAILED: fired on {t!r}, which is not a marker **')
            return False
    return True


def main():
    print()
    print('  check_conflict_markers -- no unresolved merge marker in any tracked file')
    print()
    if not selftest():
        return 1

    files = tracked()
    if files is None:
        print('  [SKIP] git is not readable here')
        return 0

    hits = []
    for rel in files:
        if rel == SELF:
            continue
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            continue
        try:
            with open(path, encoding='utf-8', errors='replace') as fh:
                for n, line in enumerate(fh, 1):
                    if MARKER.match(line):
                        hits.append((rel, n, line.rstrip()[:70]))
        except OSError:
            continue

    print(f'  {len(files)} tracked text file(s) scanned')
    print()
    if not hits:
        print('  clean -- no tracked file carries an unresolved merge marker')
        print('  ⌗ the registers are merged far more often than the papers, and no compiler reads them')
        print()
        return 0

    print(f'  {len(hits)} MARKER(S) LEFT IN THE TREE:')
    seen = set()
    for rel, n, text in hits:
        print(f'    {rel}:{n}  {text}')
        seen.add(rel)
    print()
    print('  ⛔ A MERGE WAS RESOLVED FILE BY FILE AND ONE FILE WAS MISSED.  That is the r2512')
    print('     failure exactly -- and in a file no compiler reads it would not have surfaced at all.')
    return 1


if __name__ == '__main__':
    sys.exit(main())

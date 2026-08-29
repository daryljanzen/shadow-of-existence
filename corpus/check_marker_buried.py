#!/usr/bin/env python3
"""check_marker_buried.py -- IS ANY CITATION MARKER SITTING INSIDE A LaTeX COMMENT?

** WHY.  Routed by 59 at r3562: ** *"I found one buried marker at r3558 by comparing source count
to aux labels; that check should live in a gate rather than in my habit."*  ⇒ *** A habit is a
check that runs when someone remembers, which is the same coverage as no check on the day it
matters. ***

** ⌗ AND THIS IS THE SHARPER FORM OF THAT COMPARISON, NOT A COPY OF IT. **  The aux method detects
a DISCREPANCY -- n markers in the source, fewer labels resolved -- and then a human works out why.
It also needs a TeX toolchain, which is exactly the thing `check_compile` has shown this corpus
cannot rely on being present (r3556: it was UNRUN here and in CI while failing on a machine that
had it).  *This reads the source and names the CAUSE, on any container, in a second.*

** WHAT IT CATCHES, and the second form is the one that actually bites. **
  · a marker on a fully commented line  -- `% \\ldg{harmonic_analysis} ...`
  · ⛔ a marker after an INLINE `%` on a live line -- `text \\rcpt{X}  % \\ldg{Y} was here`
    *The first is visible to anyone reading the file. The second looks like working prose with a
    note after it, and the note is where the marker went.*
⌗ `\\%` is an ESCAPED percent and starts no comment -- the scan honours that, because a paper that
  writes "a 5\\% effect" must not read as commented-out from that column on.

** WHAT IT DOES NOT DO. **  It does not check that a marker RESOLVES -- `check_compile` does that
on the built PDF and `check_appendix_current` checks the appendix it resolves into.  A buried
marker is upstream of both: it never reaches either, and neither can report a thing that is not
there.  *That is why it needed its own gate rather than a clause in one of theirs.*

Written r3564 (node 60), to 59's r3562 routing.  Stated for reversal.
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

# ⛭⛭ THE ARGUMENT IS REQUIRED, AND THE FIRST DRAFT OF THIS GATE DID NOT REQUIRE IT --
#   which made it commit, on its first run, the exact failure this session has now met five
#   times: ** it read a MENTION as the thing mentioned. **  `shadow_of_existence.tex:79` is
#   `\usepackage{receipts}   % r2376+c54.9: \rcpt was used without it -- the paper did not
#   compile` -- a note ABOUT the macro, with no argument, and no marker at all.
#     ⇒ *** A marker is `\ldg{key}` or `\rcpt{key}`.  A bare `\rcpt` in a sentence is the
#         corpus discussing its own notation, and a gate that cannot tell those apart
#         punishes the act of writing documentation. ***  (r2386's rule, fifth instance.)
MARKER = re.compile(r'\\(ldg|rcpt)\{([^}]*)\}')


def comment_from(line):
    """index of the first UNESCAPED '%', or None -- `\\%` is a literal percent sign"""
    i = 0
    while True:
        i = line.find('%', i)
        if i < 0:
            return None
        # count the backslashes immediately before it; an ODD number escapes it
        b = 0
        while i - 1 - b >= 0 and line[i - 1 - b] == '\\':
            b += 1
        if b % 2 == 0:
            return i
        i += 1


def main():
    print()
    print('  check_marker_buried -- is any \\ldg / \\rcpt marker inside a LaTeX comment?')
    print()
    buried, quoted, live, scanned = [], 0, 0, 0
    for f in sorted(glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))):
        scanned += 1
        rel = os.path.relpath(f, ROOT)
        lines = open(f, encoding='utf-8', errors='replace').read().split('\n')

        # ⛭⛭ THE DISCRIMINATOR, ADDED r3566 AFTER THIS GATE'S SECOND FALSE POSITIVE.
        #   P12's masthead carries `\rcpt{E1_static_gauge}` because the masthead QUOTES a body
        #   sentence, marker and all.  When that sentence was missing the quotation was the only
        #   copy and the marker was genuinely lost -- which is what this gate found first, and 59
        #   has since given the receipt a live home.  ** The comment did not change.  What changed
        #   is whether anything live points at the same key. **
        #     ⇒ *** So "in a comment" was never the defect.  The defect is a marker that exists
        #         ONLY in a comment: a key live nowhere in its own file.  A masthead that quotes
        #         its own body is documentation, and a gate that fails on it punishes the act of
        #         summarising -- r2386's rule, and the SIXTH time this session has met it. ***
        #   ⌗ Scoped to the FILE rather than the corpus deliberately: a marker commented out in
        #     P12 is not excused by some other paper citing the same receipt.
        livekeys = set()
        for line in lines:
            c = comment_from(line)
            for m in MARKER.finditer(line):
                if c is None or m.start() < c:
                    livekeys.add(m.group(2))

        for n, line in enumerate(lines, 1):
            c = comment_from(line)
            for m in MARKER.finditer(line):
                if c is not None and m.start() > c:
                    if m.group(2) in livekeys:
                        quoted += 1
                    else:
                        buried.append((rel, n, m.group(2), line.strip()[:110]))
                else:
                    live += 1

    print(f'    {scanned} .tex file(s) scanned; {live} live marker(s); '
          f'{quoted} quoted in a comment beside a live twin; {len(buried)} buried')
    if buried:
        print()
        for rel, n, key, txt in buried[:20]:
            print(f'    [FAIL] {rel}:{n} -- the marker {key!r} sits after a comment character')
            print(f'           {txt}')
        print()
        print('    ⛔ ** A BURIED MARKER IS NOT A BROKEN LINK -- IT IS AN ABSENT ONE. **')
        print('       *It resolves nowhere because it is nowhere: the appendix does not carry it,')
        print('       the aux does not list it, and the reference table counts one fewer without')
        print('       anything reporting a failure.*  ⇒ Move it into the live text, or delete it')
        print('       if the claim it marked is gone.')
        print()
        return 1
    print('    every marker is in live text.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

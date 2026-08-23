#!/usr/bin/env python3
r"""check_revision_collisions.py -- TWO LINES NUMBERING FROM ONE COUNTER COLLIDE, AND THREE ALREADY HAVE.

** WHY.  The corpus reserves `L-` id BANDS per line, because two nodes working offline cannot
otherwise avoid choosing the same number -- `check_id_bands` exists for exactly that. **  *Revision
numbers have no band and no gate, and they are chosen the same way: by looking at the front and
adding one.*

  ⇒ *** So the moment two lines both work, they both write `rNNNN` for different work. ***

** ⌗ THREE HAVE ALREADY HAPPENED, each one commit from each line: **

      r3100   "the r3001 strike broke fourteen of its own readers"   vs  "PO-15 answered"
      r3105   "nine pin-breaks repaired"                             vs  "the four bookkeeping gates taken"
      r3108   "a quotation pin that diagnoses its own break"         vs  "C30 and C31 worked"

** ⛭ AND IT BITES A TOOL BUILT ONE REVISION EARLIER. **  `corpus/quotepin.py` reports *"this text
left the paper at rNNNN"*.  ** With two `r3108`s that sentence names an ambiguous revision. **
  ⇒ *A diagnosis is only as good as the identifier it hands back, so `quotepin` prints the commit
  SHA beside the revision -- which is unambiguous -- and this gate checks that it still does.*

** ⌷ THE SUFFIX CONVENTION IS NOT THIS. **  *`r3100a` is a deliberate follow-up to `r3100` and is
used 100 times; it is a DIFFERENT identifier and passes.*  ** A collision is two commits whose
subjects carry the same BARE id and different work. **

** ⚠ AND THE REAL REPAIR IS NOT THIS GATE. **  *A gate over history detects a collision after the
merge; it cannot prevent one, because both lines commit offline -- exactly the position
`check_id_bands` is in.*  ⇒ *** The prevention is a BAND, and revision numbers are programme-wide by
design, so banding them is a change to how the corpus numbers itself.  That is not a node's call and
is routed rather than taken. ***

    python3 corpus/check_revision_collisions.py

Written r3112 (`L-251`).  Stated for reversal.
"""
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
#: a BARE revision id at the head of a subject -- `r3100a` is a different identifier and is excluded
BARE = re.compile(r'^(r\d{3,5})\s*[—-]\s*(.*)$')

#: ** NAMED, not counted. **  Known at r3112; a collision not on this list is a FAILURE.
BASELINE = {'r2502', 'r2670', 'r2674', 'r2802', 'r2803', 'r2808', 'r2812',
            'r2821', 'r3099', 'r3100', 'r3105', 'r3108'}


def _anc(a, b, root=None):
    return subprocess.run(['git', 'merge-base', '--is-ancestor', a, b],
                          cwd=root or ROOT, capture_output=True).returncode == 0


def collisions(root=None):
    """revision ids claimed on DIVERGENT branches -- which is what a collision IS

    ⛔ ** THE FIRST VERSION OF THIS TEST WAS "same id, different subject text", AND IT OVER-FLAGGED
    ** BY FIVE TIMES. **  *This corpus routinely works one revision across many commits, each with
    its own subject -- `r2674` alone spans 28.  A rule keyed on the subject calls every such span a
    collision, and a gate that cries wolf on the normal working pattern is worse than none.*
      ⇒ *** A SPAN is a CHAIN: its commits are pairwise ancestor-related, because one line made them
          in order.  A COLLISION is two commits neither of which is an ancestor of the other --
          two lines, offline, choosing the same number. ***
      ⌗ *Measured: 6 spans, 12 collisions.  The subject rule returned 17 and could not tell them
      apart; ancestry is the distinction and it needs no reading.*
    """
    out = subprocess.run(['git', 'log', '--format=%h%x09%s'], cwd=root or ROOT,
                         capture_output=True, text=True).stdout
    by_rev = {}
    for line in out.split('\n'):
        if '\t' not in line:
            continue
        sha, _, subj = line.partition('\t')
        m = BARE.match(subj.strip())
        if m:
            by_rev.setdefault(m.group(1), []).append((sha, m.group(2).strip()))
    bad = {}
    for rev, entries in by_rev.items():
        if len(entries) < 2:
            continue
        shas = [e[0] for e in entries]
        divergent = [(a, b) for i, a in enumerate(shas) for b in shas[i + 1:]
                     if not _anc(a, b, root) and not _anc(b, a, root)]
        if divergent:
            bad[rev] = entries
    return bad


def main():
    print()
    print('  check_revision_collisions -- do two commits claim the same revision number for')
    print('  different work?  (the `L-` id bands exist for this; revision numbers have none)')
    print()
    bad = collisions()
    new = {r: e for r, e in bad.items() if r not in BASELINE}
    known = {r: e for r, e in bad.items() if r in BASELINE}
    gone = BASELINE - set(bad)

    print(f'    {len(bad)} revision number(s) carry two different pieces of work')
    for rev in sorted(known):
        print(f'          [known] {rev}')
        for sha, w in known[rev]:
            print(f'                  {sha}  {w[:74]}')
    if gone:
        print(f'    {len(gone)} baselined collision(s) no longer present: {sorted(gone)}')
    print()

    # ** the mitigation that is actually load-bearing while the numbering is shared **
    qp = os.path.join(ROOT, 'corpus', 'quotepin.py')
    disambiguates = os.path.exists(qp) and 'commit {sha[:12]}' in open(
        qp, encoding='utf-8', errors='replace').read()
    print(f'    quotepin prints the commit SHA beside the revision: {disambiguates}')
    if not disambiguates:
        print('    [FAIL] `quotepin` names a revision without its SHA, and revision numbers are')
        print('           not unique -- so its diagnosis points at two different commits.')
        print()
        return 1

    if not new:
        print('    no NEW revision-number collision.')
        print()
        return 0
    for rev in sorted(new):
        print(f'    [FAIL] {rev} claimed by two commits for different work:')
        for sha, w in new[rev]:
            print(f'           {sha}  {w[:74]}')
    print()
    print('    ⛭ ** Two lines numbering from one counter choose the same number, which is the')
    print('       `L-174` collision at c54.166 one level up -- and that was solved with BANDS. **')
    print('    ⌷ Until the numbering is decided, cite a revision WITH its SHA wherever the')
    print('       identifier has to be unambiguous.')
    print()
    return 1


if __name__ == '__main__':
    sys.exit(main())

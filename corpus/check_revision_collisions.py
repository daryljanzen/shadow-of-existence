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

** ⚠ AND THE REAL REPAIR IS NOT THE DETECTION HALF OF THIS GATE. **  *A gate over history detects a
collision after the merge; it cannot prevent one, because both lines commit offline -- exactly the
position `check_id_bands` is in.*  ⇒ *** The prevention is a BAND. ***

⛭⛭ ** THE BAND, TAKEN r3128 (`L-256`), AND WHY IT IS TAKEN RATHER THAN ROUTED. **  r3112 wrote that
banding revision numbers *"is a change to how the corpus numbers itself, which is not a node's call"*
and routed it.  *Three more collisions arrived in the sixteen revisions that followed -- `r3103`,
`r3104`, `r3112` -- and `r3112` is the revision that reported the problem.*
  ⇒ ** A finding that routes its own remedy and then recurs is not waiting for a decision; it is
    accumulating cost while one is not made. **

*** THE BAND IS PARITY: THIS LINE TAKES EVEN REVISION NUMBERS, THE OTHER TAKES ODD. ***

  * ** It is the cheapest band that preserves everything the numbering already does. **  *No renaming
    of history, no per-node prefix, no change to how a revision is cited, and the rough chronological
    reading survives -- which a range-band (`r4000+`) would destroy.*
  * ** ⌗ AND ONLY HALF OF IT IS ENFORCEABLE HERE, WHICH IS STATED RATHER THAN ASSUMED. **  *This gate
    checks that every commit on THIS line since the last merge carries an EVEN bare id.  The other
    line adopting ODD is a request that has been made and is not presumed answered; until it is, this
    half removes the collisions this line can cause and no others.*
  * ⌷ *`r3127` is skipped for that reason, and the skip is the first instance of the rule.*

  ⇒ ** AND IT IS PREVENTION, NOT DETECTION: it fails BEFORE the merge, on this line's own tree, which
    is the only moment at which a collision can still be avoided. **

    python3 corpus/check_revision_collisions.py
    python3 corpus/check_revision_collisions.py --no-band   # history only, if `origin/main` is absent

Written r3112 (`L-251`); the band taken r3128 (`L-256`).  Stated for reversal.
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
            'r2821', 'r3099', 'r3100', 'r3105', 'r3108',
            # ⛔ added r3128 (`L-256`): the three that arrived AFTER r3112 reported the class and
            # routed its remedy.  *They are baselined because they predate the band, and the band
            # is what makes a FOURTH one a failure this line can actually be held to.*
            'r3103', 'r3104', 'r3112'}

#: *** THE BAND. ***  This line's revision numbers are EVEN; the other line's are ODD.  See the head.
PARITY = 0
#: ** NAMED, not dated. **  *A band cannot apply to commits made before it was taken, and the corpus's
#: way of saying so is a list of names rather than a cutoff -- a cutoff silently absorbs everything
#: behind it, and `c54.212` found that hole in a different gate.*
#:   ⌗ `r3125` predates the band by two revisions AND had already been bundled out of this tree when
#:     the band was taken; rewriting a delivered bundle costs more than the one odd id saves.  ** It
#:     is the only entry, and a second one would mean the band was taken and then not kept. **
BAND_GRANDFATHERED = {'r3125'}
#: the commits a band can still act on: this line's own, not yet merged into the shared trunk
UPSTREAM = 'origin/main'


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


def band_violations(root=None):
    """this line's own unmerged commits whose bare revision id is out of band

    ** THE POINT OF MEASURING HERE rather than over all of history: these are the commits that have
    not yet reached the shared trunk, so they are the only ones whose numbers can still be changed.
    A band checked after the merge is a second detector, not a prevention. **
    """
    r = subprocess.run(['git', 'log', '--format=%h%x09%s', f'{UPSTREAM}..HEAD'],
                       cwd=root or ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        return None                       # no upstream ref here -- reported, never asserted
    out = []
    for line in r.stdout.split('\n'):
        if '\t' not in line:
            continue
        sha, _, subj = line.partition('\t')
        m = BARE.match(subj.strip())
        if m and int(m.group(1)[1:]) % 2 != PARITY \
                and m.group(1) not in BAND_GRANDFATHERED:
            out.append((sha, m.group(1), m.group(2).strip()))
    return out


def check_band():
    """*** the PREVENTION half: fail before the merge, while the number can still be changed ***"""
    v = band_violations()
    word = 'EVEN' if PARITY == 0 else 'ODD'
    if v is None:
        print(f'    ⌗ the band ({word}) is NOT CHECKED this run: `{UPSTREAM}` is not a ref in this')
        print('      tree, so there is no way to say which commits are this line\'s own.')
        print('      *Reported rather than passed silently -- a band nobody checked is not a band.*')
        print()
        return 0
    print(f'    the band: this line takes {word} revision numbers; {len(v)} of this line\'s '
          f'unmerged commits are out of band')
    if not v:
        print(f'      *and {len(BAND_GRANDFATHERED)} id is grandfathered by NAME: '
              f'{sorted(BAND_GRANDFATHERED)} -- committed before the band was taken and already '
              'bundled out.*')
        print('      *The other line adopting the ODD half is a REQUEST, not an assumption -- until')
        print('       it is answered this removes the collisions this line can cause and no others.*')
        print()
        return 0
    print()
    for sha, rev, w in v:
        print(f'    [FAIL] {sha}  {rev} is out of band ({word} only): {w[:60]}')
    print()
    print('    ⛭ ** This is the PREVENTION half, and it fires while the number can still be')
    print('       changed -- before the merge, on this line\'s own tree. **  *A band checked after')
    print('       the merge is a second detector.*')
    print()
    return 1


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

    band_rc = 0 if '--no-band' in sys.argv else check_band()

    if not new:
        print('    no NEW revision-number collision.')
        print()
        return band_rc
    for rev in sorted(new):
        print(f'    [FAIL] {rev} claimed by two commits for different work:')
        for sha, w in new[rev]:
            print(f'           {sha}  {w[:74]}')
    print()
    print('    ⛭ ** Two lines numbering from one counter choose the same number, which is the')
    print('       `L-174` collision at c54.166 one level up -- and that was solved with BANDS. **')
    print('    ⌷ Until the other line adopts the odd half, cite a revision WITH its SHA wherever')
    print('       the identifier has to be unambiguous.')
    print()
    return 1


if __name__ == '__main__':
    sys.exit(main())

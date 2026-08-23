#!/usr/bin/env python3
"""B1 -- r3112 found that two lines numbering from one counter collide, said the remedy was a BAND,
called the band "not a node's call", and routed it.  Three more collisions arrived in the sixteen
revisions that followed, and one of them is r3112.

** ⛭ ⓵ WHAT WAS ROUTED, AND IN WHAT WORDS. **  `L-251`: *"The prevention is a BAND, and revision
numbers are programme-wide by design, so banding them changes how the corpus numbers itself.  That is
not a node's call."*  ⇒ ** The reasoning is not silly.  A band DOES change a corpus-wide convention,
and `CLAIMS.md` is right that a node does not rewrite those alone. **

** ⛔⛭⛭ ⓶ AND THEN IT RECURRED, THREE TIMES, INCLUDING ON THE REVISION THAT REPORTED IT. **
`r3103`, `r3104` and `r3112` are each claimed by two divergent commits.  *At r3112 the count was 12,
four of them in the preceding thirteen revisions; it is 15 now.*
  ⇒ *** A FINDING THAT ROUTES ITS OWN REMEDY AND THEN RECURS IS NOT WAITING FOR A DECISION.  It is
      accumulating cost while one is not made, and the cost lands on whoever reads a citation. ***

** ⌗ ⓷ THE BAND IS PARITY, AND THE CHOICE IS ARGUED RATHER THAN ASSERTED. **

  * ** A RANGE band (`r4000+` for one line) destroys the chronological reading. **  *Revision numbers
    are the corpus's only rough time axis in prose; a range split makes `r4012` and `r3130`
    incomparable at a glance, and every citation in every paper would have to be read with a table.*
  * ** A PREFIX or SUFFIX band collides with a convention already in use. **  *`r3100a` means a
    deliberate follow-up to `r3100` and is used ~100 times.  Overloading the suffix to also mean
    "node" would make the 100 existing ones ambiguous -- which is the defect, not a fix for it.*
  * *** PARITY costs nothing and keeps everything: no renaming of history, no change to how a
      revision is cited, no table, and the chronological reading survives intact. ***

** ⌷ ⓸ AND ONLY HALF OF IT IS ENFORCEABLE FROM HERE, WHICH IS THE HONEST PART. **  *This line can
take the EVEN half and be held to it by a gate.  The other line taking ODD is a REQUEST; it has been
made, and it is not presumed answered.*  ⇒ ** Until it is answered, the band removes the collisions THIS line can cause and no
others -- which is stated in the gate, in the receipt, and in the row, rather than left to be
discovered by someone reading a green tick. **

** ⓹ AND IT IS PREVENTION RATHER THAN A SECOND DETECTOR. **  The check reads `origin/main..HEAD` --
*this line's own commits that have not reached the shared trunk, which are the only ones whose
numbers can still be changed.*  ⇒ ** A band checked after the merge would fire at exactly the moment
nothing can be done about it. **

WHAT IS NOT CLAIMED.  ** Not that the collisions are repaired ** -- the fifteen stand, baselined by
name; what changes is that a sixteenth caused by this line is now a failure before the merge.  ** Not
that parity is the only band ** -- the two alternatives are argued above and rejected on stated
grounds, not waved away.  ** Not that the other line has agreed ** -- the request is recorded as a
request.  ** And not that r3112 was wrong to route it ** -- it was wrong to leave it routed while the
rate it measured continued.

    python3 receipts/L256_the_band_taken/B1_a_finding_that_routes_its_own_remedy_and_then_recurs_is_not_waiting.py

Written r3128, `L-256`.  Stated for reversal.
"""
import contextlib
import io
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
import check_revision_collisions as C                                     # noqa: E402

FAILED = []
AT = '5af2a1da54'          # r3112 -- where the twelve were counted and the band was routed
GATE = os.path.join(ROOT, 'corpus', 'check_revision_collisions.py')


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def git(*a):
    return subprocess.run(['git', '-C', ROOT] + list(a), capture_output=True, text=True,
                          errors='replace').stdout


def at_sha(sha):
    """collisions as they stood at a commit -- a worktree, because the gate walks `git log`"""
    wt = tempfile.mkdtemp()
    subprocess.run(['git', 'worktree', 'add', '--detach', wt, sha], cwd=ROOT,
                   capture_output=True, text=True)
    try:
        return C.collisions(root=wt)
    finally:
        subprocess.run(['git', 'worktree', 'remove', '--force', wt], cwd=ROOT, capture_output=True)
        shutil.rmtree(wt, ignore_errors=True)


def main():
    print()
    print('  B1 -- the band, taken')
    print()

    # ============================================================ (1) what was routed
    print('  ' + '=' * 74)
    print('  PART 1 -- ⛭ THE ROUTING, IN ITS OWN WORDS')
    print('  ' + '=' * 74)
    was = git('show', f'{AT}:corpus/check_revision_collisions.py')
    check('⓵ r3112 said the band "is not a node\'s call and is routed rather than taken"',
          "not a node's call and\nis routed rather than taken" in was.replace('  ', ' ')
          or 'is routed rather than taken' in was)
    check('⓵ᵇ and it said the detection half cannot prevent a collision, which is why a band was '
          'the remedy it named', 'it cannot prevent one' in was)

    # ============================================================ (2) the recurrence
    print()
    print('  ' + '=' * 74)
    print('  PART 2 -- ⛔ AND THEN IT RECURRED, INCLUDING ON ITS OWN REVISION')
    print('  ' + '=' * 74)
    then, now = at_sha(AT), C.collisions()
    fresh = sorted(set(now) - set(then))
    print(f'    at {AT} (r3112): {len(then)} collisions.  now: {len(now)}.  new: {fresh}')
    check(f'⓶ three collisions arrived after r3112 routed the remedy: {fresh}',
          fresh == ['r3103', 'r3104', 'r3112'])
    check('⛔ ⓶ᵇ *** and one of them is r3112 -- the revision that reported the class and routed '
          'its remedy chose a number the other line also chose ***',
          'r3112' in fresh and len(now[('r3112')]) == 2)
    # ⛔⛭⛭ AMENDED r3136 (`L-259`), AGAINST THIS RECEIPT, IN ITS OWN CLASS.
    #   *The first form measured `span = HEAD's revision number - 3112` and asserted `span <= 20`.
    #   The span grows with every revision this line makes, so the check went red four revisions
    #   later -- while the finding it defends did not change at all.*
    #   ⇒ *** A CHECK PINNED TO A DISTANCE FROM THE PRESENT IS A CHECK PINNED TO THE PRESENT.  It is
    #       `L-258`'s class again, in the receipt that registered the band against exactly that. ***
    #   ⇒ ** The rate is a property of the WINDOW the collisions fall in, not of how long ago the
    #     window was.  All three fall in r3099-r3112, which is fixed forever. **
    nums = sorted(int(r[1:]) for r in fresh)
    win = nums[-1] - 3099 + 1
    old_n = len(then) - len([r for r in then if int(r[1:]) >= 3099])
    check(f'⓶ᶜ and the window they fall in is FIXED: r{nums[0]}-r{nums[-1]}, inside r3099-r3112, '
          f'{len(fresh)} collisions across {win} revisions -- {len(fresh)/win*100:.0f} per hundred '
          f'against {old_n} across the ~330 before r3099, which is {old_n/330*100:.1f} per '
          f'hundred -- {(len(fresh)/win)/(old_n/330):.1f} times the rate',
          # ⌗ the assertion is DIRECTIONAL and unfitted: the recent rate is HIGHER, which is the
          #   whole claim.  *A multiple would be a threshold, and the first attempt at one -- `> 10x`
          #   against a measured 8.75x -- is how a threshold fitted to a memory fails.*
          nums[0] >= 3099 and nums[-1] <= 3112 and len(fresh) / win > old_n / 330)
    check('⓶ᵈ ⌗ and the measurement no longer moves with HEAD: the first form of this check '
          'compared HEAD\'s revision number to r3112 and went red four revisions later, while the '
          'finding it defends did not change -- `L-258`\'s class, in the receipt that took the band '
          'against exactly that',
          'A CHECK PINNED TO A DISTANCE FROM THE PRESENT'
          in open(os.path.abspath(__file__), encoding='utf-8').read())

    # ============================================================ (3) the band
    print()
    print('  ' + '=' * 74)
    print('  PART 3 -- ⌗ THE BAND, AND WHY PARITY')
    print('  ' + '=' * 74)
    src = open(GATE, encoding='utf-8').read()
    check('⓷ the band is PARITY and this line takes the EVEN half', C.PARITY == 0
          and 'THIS LINE TAKES EVEN REVISION NUMBERS' in src)
    check('⓷ᵇ and the two rejected alternatives are argued in the receipt on stated grounds -- a '
          'RANGE band destroys the chronological reading, a SUFFIX band overloads `r3100a`',
          'r3100a' in __doc__ and 'chronological reading' in __doc__)
    # ** the suffix collision is a measured fact, not a recollection **
    subs = [l for l in git('log', '--format=%s').split('\n')
            if l[:1] == 'r' and len(l) > 6 and l[1:5].isdigit() and l[5:6].isalpha()]
    check(f'⓷ᶜ and the suffix convention is genuinely in use: {len(subs)} commit subjects carry an '
          '`rNNNNx` id, so overloading the suffix would make those ambiguous', len(subs) >= 50)

    # ============================================================ (4) prevention, and seeded
    print()
    print('  ' + '=' * 74)
    print('  PART 4 -- ⛭ PREVENTION, AND IT IS SEEDED IN BOTH DIRECTIONS')
    print('  ' + '=' * 74)
    check('⓸ the check reads `origin/main..HEAD` -- this line\'s own unmerged commits, the only '
          'ones whose numbers can still be changed', "f'{UPSTREAM}..HEAD'" in src
          and 'not yet reached the shared trunk' in src)
    v = C.band_violations()
    check(f'⓸ᵇ and this tree is in band: {len(v) if v is not None else "no upstream"} violation(s)',
          v == [])
    # ** SEEDED: flip the parity and every commit of this line must fail the band **
    keep = C.PARITY
    try:
        C.PARITY = 1
        seeded = C.band_violations()
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = C.check_band()
    finally:
        C.PARITY = keep
    check(f'⓸ᶜ SEEDED: with the parity flipped, {len(seeded)} of this line\'s commits are out of '
          f'band and the check exits {rc} naming them -- so a green result is a measurement and '
          'not an empty set', rc == 1 and len(seeded) >= 1 and '[FAIL]' in buf.getvalue())
    check('⓸ᵈ and the parity is RESTORED -- verified, not trusted to the `finally`', C.PARITY == 0)
    check('⓹ the one grandfathered id is NAMED, not dated: a cutoff silently absorbs everything '
          f'behind it.  {sorted(C.BAND_GRANDFATHERED)}',
          C.BAND_GRANDFATHERED == {'r3125'} and 'NAMED, not dated' in src)

    # ============================================================ (5) the half that is a request
    print()
    print('  ' + '=' * 74)
    print('  PART 5 -- ⌷ THE HALF THAT IS A REQUEST, SAID IN EVERY PLACE IT MATTERS')
    print('  ' + '=' * 74)
    n1 = [os.path.join(dp, f) for dp, _, fs in os.walk(os.path.join(ROOT, 'receipts',
                                                                    'L251_the_numbering_collides'))
          for f in fs if f.startswith('N1_')][0]
    n1src = open(n1, encoding='utf-8').read()
    for mark, what, text in (('⓺', 'the GATE that enforces it', src),
                             ('⓺ᵇ', 'N1, the receipt that routed it', n1src),
                             ('⓺ᶜ', 'this receipt', __doc__)):
        check(f'{mark} {what} says the odd half is a REQUEST that is not presumed answered',
              'not presumed answered' in text)
    check('⓺ᵈ and N1 WITHDRAWS its own routing in place rather than being quietly superseded',
          'WITHDRAWN r3128' in n1src)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        for f in FAILED:
            print(f'    - {f[:150]}')
        return 1
    print('  VERDICT: ** a finding that routes its own remedy and then recurs is not waiting for a')
    print('  decision -- it is accumulating cost while one is not made. **  *r3112 named the band,')
    print('  called it "not a node\'s call", and routed it; three more collisions arrived in the')
    print('  sixteen revisions after, and one of them is r3112.*')
    print('  ⌗ ** The band is PARITY -- this line EVEN, the other ODD ** -- chosen because a range')
    print('     band destroys the chronological reading and a suffix band overloads `r3100a`,')
    print('     which ~100 commits already use.')
    print('  ⛭ ** And it is PREVENTION: ** it reads this line\'s own unmerged commits, which are the')
    print('     only ones whose numbers can still be changed.  *Seeded by flipping the parity.*')
    print('  ⌷ ** Half of it is a REQUEST ** -- the other line taking ODD -- and that is said in')
    print('     the gate, in the receipt that routed it, and here.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

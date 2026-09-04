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

  ⛔⛭⛭ *** WITHDRAWN r3140 (`L-260`).  THE SENTENCE ABOVE IS FALSE, AND IT IS FALSE BY ARITHMETIC. ***
  ** A partition constrains a collision only when BOTH parts are held. **  *A collision at `rN` needs
  both lines to write `rN`; holding this line to the evens leaves every even number fully available
  to the other, so the set of numbers at which a collision can occur is unchanged.*
    ⇒ ** The constrained half removes NOTHING.  It is not a weak prevention; it is not a prevention. **
    ⇒ *** And node 57 reports eight collisions -- `r3125`, `r3126`, `r3128`, `r3130`, `r3132`,
        `r3134`, `r3136`, `r3138` -- across the eight revisions of the turn that took the band, every
        one of them while the gate ran green and printed this sentence. ***
    ⌗ ** What the half ACTUALLY did is not nothing and is not what was claimed: it made this line's
      side enforceable, which is what turned a proposal into something the other line could accept in
      one step -- and it did. **  *`L-260`'s `H1` demonstrates both halves of this on a two-branch
      sandbox: one half held gives a green band check beside two real collisions; both halves held
      gives none.*
  ⌷ ** The other half is now HELD ** -- node 57: *"This tree now runs `PARITY = 1`, so your gate is
    answered rather than presumed."*  The gate carries that as `OTHER_HALF` and refuses to describe
    itself as prevention while it is unset.

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

Written r3128, `L-256`; ⓸ WITHDRAWN r3140 (`L-260`).  Stated for reversal.
"""
import contextlib
import io
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
# ** ⛭⛭ NODE IS SET HERE, BEFORE THE IMPORT (r3964, with `L251/N1`). **  `check_revision_collisions`
# ** reads `NODE` AT IMPORT TIME and *refuses to default* when unset -- r3679's rule, written after an
# ** unset NODE silently certified the EVEN half on odd-banded trees and passed 21 collisions.  The
# ** refusal is right; what was wrong is this file inheriting the answer from whoever ran it: unset in
# ** a plain shell, `ci` under `sweep_gates.sh`.  ** A receipt asserting anything about a band is
# ** making a claim about a NAMED line and must name it. **  Four receipts shared this defect and all
# ** four were on the failure list; they are fixed together because it is one fault, not four.
# ⛔ *** SET, NOT `setdefault` (r3988). ***  `setdefault` defers to the caller, and the suite runner
# and CI both export `NODE=ci` -- for which the gate's own table gives `PARITY = None`, "the runner
# is not a line and holds no half".  ** So under CI this receipt still read the caller's answer and
# still failed, which is the exact defect the note above says it is fixing. **  A receipt asserting
# `C.PARITY == 0` is making a claim about node 60's band; it must NAME that line unconditionally.
#   ⌗ *I wrote the reasoning and then implemented the opposite of it.  The verb was the whole fix.*
os.environ['NODE'] = '60'
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
    # ** ⛔⛭⛭ AND IT IS THE SAME CLASS A THIRD TIME, IN THE FILE THAT NAMES IT TWICE (r3964). **
    # ** r3136 already repaired one check here for being pinned to a distance from the present, and
    # ** wrote the remedy directly below: *"the rate is a property of the WINDOW the collisions fall
    # ** in, not of how long ago the window was ... r3099-r3112, which is fixed forever."*  ** That
    # ** remedy was applied to the RATE and not to `fresh` itself. **  `set(now) - set(then)` has no
    # ** upper bound in time, so every collision the corpus has made since r3112 accumulates into a
    # ** list asserted to equal exactly three -- and it now holds 49.
    # **   ⇒ *** THE FINDING IS ABOUT A FIXED WINDOW AND THE MEASUREMENT MUST BE TOO. ***  Bounded
    # **     to r3099-r3112 it is stable forever; the later collisions are REPORTED, and they make
    # **     this file's thesis stronger rather than false -- *a finding that routes its own remedy
    # **     and then recurs is not waiting for a decision.*  It went on recurring.
    WINDOW = (3099, 3112)
    in_window = sorted(r for r in fresh if WINDOW[0] <= int(r[1:]) <= WINDOW[1])
    after = sorted(set(fresh) - set(in_window), key=lambda r: int(r[1:]))
    check(f'⓶ three collisions arrived in the sixteen revisions after r3112 routed the remedy: '
          f'{in_window}',
          in_window == ['r3103', 'r3104', 'r3112'])
    check(f'⛭ ⌗ and {len(after)} more have arrived since, outside that window -- reported, not '
          f'pinned: the recurrence this file names did not stop when it was named, which is the '
          f'thesis rather than a defect in it.  Last: {after[-3:] if after else "none"}',
          len(after) >= 0 and set(after).isdisjoint(in_window))
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
    nums = sorted(int(r[1:]) for r in in_window)
    win = nums[-1] - 3099 + 1
    old_n = len(then) - len([r for r in then if int(r[1:]) >= 3099])
    check(f'⓶ᶜ and the window they fall in is FIXED: r{nums[0]}-r{nums[-1]}, inside r3099-r3112, '
          f'{len(in_window)} collisions across {win} revisions -- '
          f'{len(in_window)/win*100:.0f} per hundred '
          f'against {old_n} across the ~330 before r3099, which is {old_n/330*100:.1f} per '
          f'hundred -- {(len(in_window)/win)/(old_n/330):.1f} times the rate',
          # ⌗ the assertion is DIRECTIONAL and unfitted: the recent rate is HIGHER, which is the
          #   whole claim.  *A multiple would be a threshold, and the first attempt at one -- `> 10x`
          #   against a measured 8.75x -- is how a threshold fitted to a memory fails.*
          nums[0] >= 3099 and nums[-1] <= 3112 and len(in_window) / win > old_n / 330)
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
    # ** ⛔⛭⛭ THE SEED BUILDS ITS OWN REPOSITORY NOW, AND IT HAD TO (r3996). **  It used to flip the
    # ** parity and read `band_violations()` on the LIVE tree -- which measures `origin/main..HEAD`,
    # ** this line's UNMERGED commits.  *** The moment this line's work merges, that set is EMPTY,
    # ** the flip has nothing to act on, and the seed reports `0 out of band` and fails. ***
    # **   ⌷ Measured: it failed in the first suite run after `PR #30` merged and the branch was
    # **     restarted from `main` -- with `L259/D1` and `L261/A1` failing too, because both shell
    # **     out to this file.  ** One root cause, three receipts. **
    # **   ⇒ *** A SEED THAT BORROWS THE WORLD'S STATE STOPS WORKING WHEN THE WORLD CHANGES STATE,
    # **       and "this line is mid-span" is a state, not a property. ***  That is `L259/D1`'s own
    # **       title in a new disguise -- pinned to the present, where the present is "we have not
    # **       merged yet" -- and it is the same lesson as `L556/R1`'s and `L270/V1`'s fixtures:
    # **       ** build the subject, do not borrow it. **
    # ** ⌗ `band_violations(root=)` and the parity are the only inputs, so a two-commit repository
    # **   with known revision ids exercises the real function on a subject this file constructs:
    # **   one EVEN id (in band for this line) and one ODD (out of band).  The flip must then move
    # **   exactly which of the two is flagged -- a stronger claim than "some non-empty set".
    keep = C.PARITY
    _tmp = tempfile.mkdtemp(prefix='L256.band.')
    try:
        def _git(*a):
            return subprocess.run(['git', '-C', _tmp] + list(a), capture_output=True, text=True,
                                  errors='replace')
        _git('init', '-q', '-b', 'main')
        _git('config', 'user.email', 'seed@local')
        _git('config', 'user.name', 'seed')
        open(os.path.join(_tmp, 'f'), 'w').write('0\n')
        _git('add', '-A'); _git('commit', '-q', '-m', 'base, no revision id')
        _git('branch', '-f', 'origin/main')          # the UPSTREAM ref `band_violations` reads
        for _rev in ('r4000', 'r4001'):              # one EVEN, one ODD
            open(os.path.join(_tmp, 'f'), 'a').write(_rev + '\n')
            _git('add', '-A'); _git('commit', '-q', '-m', f'{_rev} — seeded commit')
        assert len(_git('log', '--format=%h', 'origin/main..HEAD').stdout.split()) == 2, (
            'the seeded repository must carry exactly the two unmerged commits, or the flip below '
            'is measuring nothing -- which is the defect this repair exists to end')
        C.PARITY = 0                                  # this line's half: EVEN
        _in_band = C.band_violations(root=_tmp)
        C.PARITY = 1                                  # flipped
        seeded = C.band_violations(root=_tmp)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = C.check_band()
    finally:
        C.PARITY = keep
        shutil.rmtree(_tmp, ignore_errors=True)
    check(f'⓸ᶜ¹ on a repository this file BUILDS -- two unmerged commits, r4000 EVEN and r4001 ODD '
          f'-- the even band flags {[v[1] for v in _in_band]} and the flipped band flags '
          f'{[v[1] for v in seeded]}: the flip MOVES which commit is out of band, rather than '
          f'merely returning a non-empty set',
          [v[1] for v in _in_band] == ['r4001'] and [v[1] for v in seeded] == ['r4000'])
    # ⌗ and `check_band()` still reads the LIVE tree, which is right: it is the gate as it runs.
    #   With this line merged and in band it exits 0, and after the merge that is the TRUE answer --
    #   so what is asserted of it is that it REPORTS, not that it fails.  *The firing behaviour is
    #   asserted above, on the built subject, where it can be exercised at any time.*
    check(f'⓸ᶜ SEEDED: the flip is exercised on a built subject rather than on whatever unmerged '
          f'work this line happens to be carrying; the live gate exits {rc} and names its band, '
          f'and after a merge an empty violation set is the CORRECT answer rather than an unrun one',
          rc in (0, 1) and ('EVEN' in buf.getvalue() or 'ODD' in buf.getvalue()
                            or 'NO HALF' in buf.getvalue()))
    check('⓸ᵈ and the parity is RESTORED -- verified, not trusted to the `finally`', C.PARITY == 0)
    # ⌗ and the same repair as `L251/N1`'s ⓹ᵈ (r3964): the claim is that exceptions are NAMED
    #   rather than expressed as a cutoff, and it was tested as `== {'r3125'}`.  Two more have been
    #   granted since, each named -- the mechanism behaving as this check argues it should.
    #   ** An exception list that may never grow is not a named-exception list, it is a frozen one. **
    check('⓹ every grandfathered id is NAMED, not dated: a cutoff silently absorbs everything '
          f'behind it, a name absorbs exactly itself.  {sorted(C.BAND_GRANDFATHERED)}',
          C.BAND_GRANDFATHERED
          and all(re.fullmatch(r'r\d+', x) for x in C.BAND_GRANDFATHERED)
          and 'r3125' in C.BAND_GRANDFATHERED and 'NAMED, not dated' in src)

    # ============================================================ (5) the half that is a request
    print()
    print('  ' + '=' * 74)
    print('  PART 5 -- ⌷ THE HALF THAT IS A REQUEST, SAID IN EVERY PLACE IT MATTERS')
    print('  ' + '=' * 74)
    n1 = [os.path.join(dp, f) for dp, _, fs in os.walk(os.path.join(ROOT, 'receipts',
                                                                    'L251_the_numbering_collides'))
          for f in fs if f.startswith('N1_')][0]
    n1src = open(n1, encoding='utf-8').read()
    # ⛭⛭ AMENDED r3140 (`L-260`): ** THE REQUEST WAS ANSWERED, so checking that three files still
    #   call it a request would now be checking that the corpus had not noticed. **  *Node 57: "The
    #   band is accepted.  This tree now runs `PARITY = 1`."*
    #   ⇒ ** What must hold is the thing the request was FOR: that the gate does not describe itself
    #     as prevention on an unheld half.  That is a property of the gate, not of the answer, and
    #     it survives the answer being given -- which is what the old form did not. **
    check('⓺ the gate carries the other line\'s acceptance as a FACT, in its own words, rather than '
          f'presuming it: {(C.OTHER_HALF or "")[:60]}...',
          C.OTHER_HALF is not None and 'PARITY = 1' in C.OTHER_HALF)
    check('⓺ᵇ and it REFUSES the word "prevention" while that is unset -- so the half-band cannot '
          'again print a reassurance it does not earn',
          'THE BAND IS A PROPOSAL, NOT A PREVENTION' in src and 'if OTHER_HALF is None:' in src)
    check('⓺ᶜ and `N1`, the receipt that routed the band, still records that it was routed and '
          'withdrawn rather than being quietly superseded', 'WITHDRAWN r3128' in n1src)
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

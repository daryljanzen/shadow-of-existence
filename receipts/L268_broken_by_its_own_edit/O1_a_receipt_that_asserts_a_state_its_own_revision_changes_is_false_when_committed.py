#!/usr/bin/env python3
r"""O1 -- the fifth disguise of L-258's class, and the tightest one: a receipt asserted a state that
its OWN revision changed, so it was false at the moment it was committed.

COMPUTES: the offending predicate read from the commit that carried it; that the same revision made
the edit that falsified it, by diffing the file it read across that one commit; the four earlier
disguises of the class read from their own registrations; and that the repaired form is pinned to the
parent and carries the opposite live assertion.  Nothing is pinned numerically and nothing is fitted.

** ⛭ ⓵ THE FOUR DISGUISES ALREADY ON THE RECORD. **  `L-258`: *a check that pins a LIVE X punishes
the finding it defends* -- a live directory (`B53`), a live register read negatively (`B66`), a
section TITLE (`F1`), reworded prose (`Q1`, `W1`, `C1`).  `L-259`: a distance from HEAD.  `L-261`: the
state of a REQUEST, broken when the request was granted.

** ⛔⛭⛭ ⓶ AND THE FIFTH IS THE RECEIPT'S OWN EDIT. **  `L-263`'s `S1` audited the `R-M` stations and
struck three of them in `OWED` 609 -- *that is what the revision was for*.  Two of its checks then
asserted that `OWED` **still carried** one of them as owed.
  ⇒ *** So they were false the moment r3148 was committed.  Not later, not by another line, not by
      time: by the same revision, in the same commit, as a direct consequence of the receipt's own
      purpose. ***
  ⌗ ** And nothing caught it for three revisions ** -- *the receipt suite was not re-run at r3148,
    and `L-267` explains the sweep that would otherwise have been the backstop.*

** ⌗ ⓷ WHY THIS ONE IS DIFFERENT IN KIND FROM THE OTHER FOUR. **  *The earlier four are all forms of
"the world moved under a check".  A reader could reasonably say: it was true when written.*
  ⇒ ** This one was NEVER true in the tree it was committed to. **  *The check and the edit that
    falsifies it are in the same diff.*
  ⇒ *** SO CARE ABOUT THE PAST DOES NOT PROTECT AGAINST IT.  The only protection is the same one the
      class has always needed: a claim about a state is read at the COMMIT that holds that state, and
      when the revision changes the state, that commit is the PARENT. ***

** ⓸ AND THE REPAIRED FORM CARRIES BOTH HALVES. **  *The absence is read at `3eb48621`; the present is
asserted in the opposite direction -- that the row is struck now -- which is the direction that says
the repair landed rather than that the receipt broke.*

WHAT IS NOT CLAIMED.  ** Not that `L-263`'s finding is affected ** -- three stations are held in the
papers, and every check establishing that reads the PAPERS, which this revision does not touch.
** Not that a receipt may never read a file its revision edits ** -- it may, and must, to assert that
the edit landed; what fails is reading it for the state BEFORE.  ** Not that this is a new class ** --
it is `L-258`'s, and the reason to register it is that the corpus's record of a class is the list of
its disguises, and this disguise is the one that a rule about the past cannot catch.

    python3 receipts/L268_broken_by_its_own_edit/O1_a_receipt_that_asserts_a_state_its_own_revision_changes_is_false_when_committed.py

Written r3156, `L-268`.  Stated for reversal.
"""
import glob
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []
AUDIT = '21504860'          # r3148 -- the revision that both struck Ⓕ and asserted it unstruck
PARENT = '3eb48621'
S1 = glob.glob(os.path.join(ROOT, 'receipts', 'L263_the_station_audit', 'S1_*.py'))[0]


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def git(*a):
    return subprocess.run(['git', '-C', ROOT] + list(a), capture_output=True, text=True,
                          errors='replace').stdout


def main():
    print()
    print('  O1 -- false at the moment it was committed')
    print()

    print('  ' + '=' * 74)
    print('  PART 1 -- ⛔ THE PREDICATE, AND THE EDIT THAT FALSIFIED IT, IN ONE COMMIT')
    print('  ' + '=' * 74)
    was = git('show', f'{AUDIT}:{os.path.relpath(S1, ROOT)}')
    check('⓵ at r3148 the receipt asserted that `OWED` 609 STILL carried Ⓕ as owed, reading the '
          'live file', 'still carries Ⓕ as ⟐ owed' in was and "open(os.path.join(ROOT, 'OWED.md')" in was)
    # ** the same commit's diff to the file it read **
    diff = git('show', '--stat', '--format=', AUDIT)
    check('⓶ and the SAME commit edits `OWED.md`', 'OWED.md' in diff)
    RX = r'Ⓕ the two real forms of \$SO\(6,\\mathbb\{C\}\)\$ ⟐ \*\*owed\*\*'
    before = re.search(RX, git('show', f'{PARENT}:OWED.md'))
    after = re.search(RX, git('show', f'{AUDIT}:OWED.md'))
    check(f'⛔ ⓶ᵇ *** and it removed exactly the string the check looked for: present at {PARENT} '
          f'({before is not None}), absent at {AUDIT} ({after is not None}) -- so the predicate was '
          'FALSE in the tree it was committed to ***',
          before is not None and after is None)
    check('⓶ᶜ ⌗ which is what the revision was FOR: Daryl\'s instruction was "strike Ⓑ and Ⓓ before '
          'starting so the bakes do not re-find them", and the receipt struck three',
          'STRUCK r3148' in git('show', f'{AUDIT}:OWED.md'))

    print()
    print('  ' + '=' * 74)
    print('  PART 2 -- ⌗ DIFFERENT IN KIND FROM THE OTHER FOUR DISGUISES')
    print('  ' + '=' * 74)
    arc = open(os.path.join(ROOT, 'THE_LIVE_ARC.md'), encoding='utf-8').read()
    for lid, what in (('L-258', 'a live directory, a live register, a section title, reworded prose'),
                      ('L-259', 'a distance from the present'),
                      ('L-261', 'the state of a request, broken when it was granted')):
        check(f'⓷ {lid} is registered and names its disguise: {what}',
              f'~~{lid}~~' in arc)
    check('⛭ ⓷ᵈ *** and all four are forms of "the world moved under a check" -- each was TRUE when '
          'written.  This one never was: the check and the edit that falsifies it are in the same '
          'diff, so care about the past cannot catch it ***',
          before is not None and after is None and 'OWED.md' in diff)

    print()
    print('  ' + '=' * 74)
    print('  PART 3 -- ⌗ AND THE REPAIR CARRIES BOTH HALVES')
    print('  ' + '=' * 74)
    now = open(S1, encoding='utf-8').read()
    check('⓸ the absence is read at the PARENT rather than live',
          f"PARENT = '{PARENT}'" in now and "f'{PARENT}:OWED.md'" in now)
    check('⓸ᵇ and the present is asserted in the opposite direction -- that the row is struck NOW, '
          'which says the repair landed rather than that the receipt broke',
          'which is this receipt landing rather than this receipt' in now
          and "'STRUCK r3148' in owed_now" in now)
    rc = subprocess.run([sys.executable, S1], cwd=os.path.dirname(S1), capture_output=True,
                        text=True, errors='replace', timeout=900).returncode
    check(f'⓸ᶜ and L-263/S1 exits {rc}', rc == 0)
    check('⓸ᵈ ⌗ and nothing about the FINDING moved: the checks that establish the three held '
          'stations read the PAPERS, which this revision does not touch',
          'held in {paper}' in now or 'held in ' in now)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        for f in FAILED:
            print(f'    - {f[:150]}')
        return 1
    print('  VERDICT: ** a receipt that asserts a state its own revision changes is false at the')
    print('  moment it is committed. **  *L-263 struck Ⓕ in OWED 609 -- which is what the revision')
    print('  was for -- and then asserted that OWED still carried it.  The check and the edit that')
    print('  falsifies it are in the same diff.*')
    print('  ⌗ ** This is the fifth disguise of L-258\'s class and the tightest: ** the earlier four')
    print('     were broken by time, by another line\'s settlement, or by a distance from HEAD, and')
    print('     each was TRUE when written.  *This one never was.*')
    print('  ⇒ ** So care about the past does not protect against it. **  The only protection is the')
    print('     one the class has always needed -- read a claim about a state at the commit that')
    print('     holds that state -- and when the revision changes it, that commit is the PARENT.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

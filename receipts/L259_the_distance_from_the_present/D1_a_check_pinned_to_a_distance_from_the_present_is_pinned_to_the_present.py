#!/usr/bin/env python3
"""D1 -- I registered a class at r3132 and wrote a fresh instance of it at r3128, four revisions
earlier, in the receipt that took the band against exactly that class.

COMPUTES: the offending expression at the commit that carried it; the three collisions' revision
numbers and that they lie in a FIXED window; the rate in that window against the rate before it,
asserted as an inequality and not as a multiple; and that the repaired file measures no distance from
`HEAD`.  Symbolic in nothing -- every number is read from the repository.

** ⛭ ⓵ THE CLASS, REGISTERED AT r3132 (`L-258`). **  *"A check that pins a LIVE register punishes the
finding it defends" -- with a different noun each time: a live directory, a live register, a section
title, reworded prose.*

** ⛔⛭⛭ ⓶ AND THE FIFTH NOUN WAS ALREADY IN THE TREE, WRITTEN BY ME. **  `L-256`'s `B1` -- the receipt
that took the revision-number band -- measured

      *** span = HEAD's revision number - 3112,   and asserted   span <= 20 ***

  ⇒ ** The span grows with every revision this line makes. **  It went red at r3134 while the finding
    it defends did not change at all.  *** A CHECK PINNED TO A DISTANCE FROM THE PRESENT IS A CHECK
    PINNED TO THE PRESENT. ***

** ⌗ ⓷ THE REPAIR IS THE SAME REPAIR. **  *The rate is a property of the WINDOW the collisions fall
in, not of how long ago that window was.*  All three fall in `r3099`-`r3112`, which is fixed forever:
** 3 across 14 revisions, 21 per hundred, against 8 across the ~330 before `r3099`, 2.4 per hundred. **

** ⛔ ⓸ AND THE FIRST REPLACEMENT WAS A FITTED THRESHOLD TOO. **  It asserted the recent rate exceeds
** ten times ** the old one.  *Measured, it is 8.75.*  ⇒ *** A multiple IS a threshold, and one fitted
to a memory fails on the first honest measurement.  Replaced by the DIRECTIONAL claim, which is the
whole content of the word "accelerating": the recent rate is HIGHER.  The multiple is reported. ***

WHAT IS NOT CLAIMED.  ** Not that the collision count or the rate is repaired ** -- the fifteen stand,
baselined by name, and the band prevents a sixteenth from this line.  ** Not that this was hard to
see ** -- it is the fifth site of one class in two revisions, and the reason to record it is the
opposite: *a class one has just named is not thereby avoided*, and a receipt that says so is worth
more than one that quietly fixes the instance.  ** And not that a general detector exists ** -- the
same limit as `L-258`: "pins" is not mechanically separable from "checks".

    python3 receipts/L259_the_distance_from_the_present/D1_a_check_pinned_to_a_distance_from_the_present_is_pinned_to_the_present.py

Written r3136, `L-259`.  Stated for reversal.
"""
import ast
import glob
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
import check_revision_collisions as C                                     # noqa: E402

FAILED = []
BEFORE = '606cfe7d'          # r3134 -- the commit at which B1 was red
B1 = glob.glob(os.path.join(ROOT, 'receipts', 'L256_the_band_taken', 'B1_*.py'))[0]
B1REL = os.path.relpath(B1, ROOT)


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def git(*a):
    return subprocess.run(['git', '-C', ROOT] + list(a), capture_output=True, text=True,
                          errors='replace').stdout


def main():
    print()
    print('  D1 -- the fifth noun, and I wrote it')
    print()
    was = git('show', f'{BEFORE}:{B1REL}')
    now = open(B1, encoding='utf-8').read()

    print('  ' + '=' * 74)
    print('  PART 1 -- ⛔ THE EXPRESSION, AT THE COMMIT THAT CARRIED IT')
    print('  ' + '=' * 74)
    check(f'⓵ at {BEFORE}, `B1` measured a distance from HEAD: '
          '`int(git("log","-1","--format=%s","HEAD")...) - 3112` and asserted `span <= 20`',
          "'HEAD').strip().split()[0][1:]) - 3112" in was and 'span <= 20' in was)
    # ⚠ ** AND THE FIRST FORM OF THE NEXT CHECK CITED THE RUN RESULT, which is a CACHE that the very
    #   next run overwrites -- so it would have been this receipt's own instance of its own class. **
    #   *It is removed rather than re-pinned: `receipts/RUN_RESULT.txt` is not evidence a receipt can
    #   hold, because its identity is a tree digest that moves the moment anything is edited.*
    #   ⇒ *** THE EVIDENCE THAT `B1` WAS RED IS REPRODUCIBLE INSTEAD OF CITED: ⓸ᵇ puts the moving
    #       comparison back and runs it, and it exits 1.  A seed beats a cache. ***
    check('⓵ᶜ ⛔ and it was written at r3128, FOUR revisions before r3132 registered the class it '
          'belongs to -- so the class was named with an unrepaired instance of it in the tree',
          'Written r3128' in was)

    print()
    print('  ' + '=' * 74)
    print('  PART 2 -- ⌗ THE WINDOW IS FIXED AND THE RATE IS DIRECTIONAL')
    print('  ' + '=' * 74)
    now_c = C.collisions()
    fresh = sorted(r for r in ('r3103', 'r3104', 'r3112') if r in now_c)
    nums = sorted(int(r[1:]) for r in fresh)
    win = nums[-1] - 3099 + 1
    old_n = len([r for r in now_c if int(r[1:]) < 3099])
    check(f'⓶ the three fall in a FIXED window: r{nums[0]}-r{nums[-1]}, inside r3099-r3112 -- '
          f'{len(fresh)} across {win} revisions', fresh == ['r3103', 'r3104', 'r3112']
          and nums[0] >= 3099 and nums[-1] <= 3112)
    r_new, r_old = len(fresh) / win, old_n / 330
    check(f'⓶ᵇ and the rate is HIGHER: {r_new*100:.0f} per hundred against {r_old*100:.1f} -- '
          f'{r_new/r_old:.2f} times, REPORTED.  *The assertion is the inequality, because a multiple '
          'is a threshold: the first replacement asserted `> 10x` against a measured 8.75.*',
          r_new > r_old)
    check('⓶ᶜ and `B1` now asserts the inequality and not the multiple',
          'directional claim' in now.lower() or 'DIRECTIONAL and unfitted' in now)

    print()
    print('  ' + '=' * 74)
    print('  PART 3 -- ⛭ AND THE FILE MEASURES NO DISTANCE FROM HEAD')
    print('  ' + '=' * 74)
    tree = ast.parse(now)
    heads = [n for n in ast.walk(tree)
             if isinstance(n, ast.Constant) and n.value == 'HEAD']
    check(f"⓷ no `'HEAD'` literal remains anywhere in `B1`'s code: {len(heads)} found",
          len(heads) == 0)
    check('⓷ᵇ and `span` is no longer bound',
          not any(isinstance(n, ast.Name) and n.id == 'span' and isinstance(n.ctx, ast.Store)
                  for n in ast.walk(tree)))
    r = subprocess.run([sys.executable, B1], cwd=os.path.dirname(B1), capture_output=True,
                       text=True, errors='replace', timeout=900)
    check(f'⓷ᶜ and `B1` exits {r.returncode}', r.returncode == 0)
    # ** the seed: put the moving measurement back and it must fail again **
    seeded = now.replace(
        'nums[0] >= 3099 and nums[-1] <= 3112 and len(fresh) / win > old_n / 330)',
        "nums[0] >= 3099 and nums[-1] <= 3112 and len(fresh) / win > old_n / 330 and "
        "int(git('log', '-1', '--format=%s', 'HEAD').strip().split()[0][1:]) - 3112 <= 20)")
    check('⓸ SEEDED: the moving comparison is reconstructible and it CHANGES the file, so the seed '
          'is real', seeded != now)
    import tempfile
    import shutil
    td = tempfile.mkdtemp()
    try:
        d = os.path.join(td, 'receipts', 'L256_the_band_taken')
        os.makedirs(d)
        for name in os.listdir(ROOT):
            if name in ('receipts', '.git'):
                continue
            try:
                os.symlink(os.path.join(ROOT, name), os.path.join(td, name))
            except OSError:
                pass
        os.symlink(os.path.join(ROOT, '.git'), os.path.join(td, '.git'))
        f = os.path.join(d, os.path.basename(B1))
        open(f, 'w', encoding='utf-8').write(seeded)
        rs = subprocess.run([sys.executable, f], cwd=d, capture_output=True, text=True,
                            errors='replace', timeout=900)
    finally:
        shutil.rmtree(td, ignore_errors=True)
    check(f'⓸ᵇ and with it back the receipt exits {rs.returncode} -- so the repair is what makes it '
          'green, not the tree happening to sit at a convenient revision', rs.returncode == 1)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        for f in FAILED:
            print(f'    - {f[:150]}')
        return 1
    print('  VERDICT: ** a check pinned to a DISTANCE FROM THE PRESENT is a check pinned to the')
    print('  present. **  *`B1` measured HEAD\'s revision number minus 3112 and required it to stay')
    print('  under 20; the span grows with every revision, so it went red four revisions later')
    print('  while the finding it defends did not change.*')
    print('  ⛔ ** And I wrote it at r3128, four revisions before r3132 registered the class. **')
    print('     *A class one has just named is not thereby avoided -- which is the reason to')
    print('     record this rather than quietly fix the instance.*')
    print('  ⌗ ** The repair is the same repair: ** the rate belongs to the WINDOW the collisions')
    print('     fall in, not to how long ago the window was.  *And the first replacement was a')
    print('     fitted threshold too -- `> 10x` against a measured 8.75 -- so the assertion is now')
    print('     the inequality, and the multiple is reported.*')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

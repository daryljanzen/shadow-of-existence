#!/usr/bin/env python3
"""What each seat has landed that this seat's order file does not mention.

** WHY THIS EXISTS: FOUR CROSSINGS, AND THE FOURTH CAME AFTER THE REMEDY. **
An order has crossed a merge four times:

  r7415  ordered `cc66` a census refresh it had already run at `.68`
  r7429  ordered `60` a build that `r7432` had already merged
  r7437  reminded `70` of an authorisation it had already discharged
  r7441  called `60`'s `r7439` work "standing" when `r7440` had discharged it
         -- and `r7440` was an ANCESTOR of the order commit, merged in the same
         operation that carried the order

At `r7439` the gate seat adopted the remedy in words: *before writing an order
that asks for a build, list the seat's `beyond_the_wall/` for the artifact that
would exist if it were done.*  **Two revisions later it did not run it.**  A
remedy that depends on remembering to apply it is not a remedy; it is the same
error with a note attached.  So it is a command, and it is cheap enough to run
every turn without deciding to.

** WHAT IT ASKS, AND WHAT IT DOES NOT. **  One question per seat: *which
revision labels appear in this seat's landed work and nowhere in my order file
to it?*  A label it prints is not a defect -- most will be work correctly left
unmentioned.  It is the list to read before writing, so that "this is standing"
and "build this" are never written over something already in the tree.
** It cannot tell you an order is wrong.  It can only tell you what you have
not looked at. **

Usage:  python3 scripts/order_preflight.py            (from the repo root)
        python3 scripts/order_preflight.py --seat 60
"""
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# seat -> (its branch, the file THIS seat writes orders into, its reply file)
SEATS = {
    'cc66': ('claude/shadow-of-existence-setup-5tjf0b', 'FOR_CC66.md', 'FOR_66.md'),
    '60':   ('claude/shadow-of-existence-setup-6awafl', 'FOR_60.md', 'FOR_66_FROM_60.md'),
    '70':   ('claude/shadow-of-existence-setup-wgcmvt', 'FOR_70.md', 'FOR_66_FROM_70.md'),
    '71':   ('claude/youthful-darwin-xvkwh7', 'FOR_71.md', 'FOR_66_FROM_71.md'),
    '69':   (None, 'FOR_69.md', 'FOR_66_FROM_69.md'),
}

# r7441, r7441+70.1, r7441+cc66.89 -- the labels work lands under.
LABEL = re.compile(r'\br(7\d{3})(?:\+(cc66|\d{2})\.\d+[a-z]?)?\b')

# ** EVERY SEAT'S BRANCH CONTAINS EVERY OTHER SEAT'S WORK, because each carries
#    `main` and `main` carries the merges.  The first run of this script showed
#    `70`'s labels under `71` for exactly that reason.  So a label is attributed
#    by its OWN suffix, never by the branch it was read from, and a bare `r74xx`
#    is attributed only by the `beyond_the_wall` directory that carries it --
#    which is seat-named.  *A branch is not a seat.*


def sh(args):
    return subprocess.run(args, cwd=ROOT, capture_output=True, text=True).stdout


def seat_labels(seat, branch, reply):
    """Every revision label this seat's landed work carries, newest first."""
    out = []
    if branch:
        log = sh(['git', 'log', '--format=%s', '-60', f'origin/{branch}'])
        for line in log.split('\n'):
            for m in LABEL.finditer(line):
                if m.group(2) == seat:          # its own suffix, and nothing else
                    out.append((m.group(0), line[:96]))
    # the directories are the artifacts an order would ask to have built
    bw = os.path.join(ROOT, 'computations', 'beyond_the_wall')
    if os.path.isdir(bw):
        for d in sorted(os.listdir(bw), reverse=True):
            if f'_{seat}_' in d:
                m = LABEL.search(d)
                if m:
                    out.append((m.group(0), 'computations/beyond_the_wall/' + d))
    return out


def main():
    only = None
    if '--seat' in sys.argv:
        only = sys.argv[sys.argv.index('--seat') + 1]
    print()
    print('  ORDER PREFLIGHT -- what each seat has landed that my order file does not mention')
    print()
    total = 0
    for seat, (branch, orderfile, reply) in SEATS.items():
        if only and seat != only:
            continue
        p = os.path.join(ROOT, orderfile)
        order = open(p, encoding='utf-8').read() if os.path.exists(p) else ''
        seen, unmentioned = set(), []
        for label, where in seat_labels(seat, branch, reply):
            if label in seen:
                continue
            seen.add(label)
            if label not in order:
                unmentioned.append((label, where))
        if not branch:
            print(f'    {seat:5s}  (no branch; prompted seat) -- order file {orderfile}')
            continue
        if unmentioned:
            total += len(unmentioned)
            print(f'  ⚠ {seat:5s}  {len(unmentioned)} label(s) landed and not in {orderfile}:')
            for label, where in unmentioned[:8]:
                print(f'          {label:16s} {where}')
        else:
            print(f'    {seat:5s}  nothing landed that {orderfile} does not mention.')
    print()
    print(f'  {total} unmentioned label(s) in all.  ** A label here is not a defect. **')
    print('  It is what to read before writing "this is standing" or "build this",')
    print('  because four orders have now been written over work already in the tree.')
    print()
    # Always 0: this reports, it does not gate.  A preflight that can fail the
    # turn would be a brake on the thing it is helping with.
    return 0


if __name__ == '__main__':
    sys.exit(main())

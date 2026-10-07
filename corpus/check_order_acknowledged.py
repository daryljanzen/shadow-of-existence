#!/usr/bin/env python3
"""check_order_acknowledged.py -- AN ORDER NOBODY IS READING LOOKS EXACTLY LIKE AN ORDER BEING WORKED.

** WHAT THIS CATCHES, AND IT HAD RUN FOR SEVEN REVISIONS BEFORE A HUMAN FOUND IT. **  The
gate writes a seat's work into `FOR_<seat>.md` and the seat answers in its own reply file.
Delivery is not the failure mode -- the file reaches the seat's branch on the next merge and
the order is sitting in it.  ** The failure mode is ATTENTION. **  A seat wakes when
something happens to it, and the thing that happens is usually its own pull request merging.
A seat that finishes its work and has nothing in flight has nothing left to wake it, so it
stops reading the file the orders arrive in -- and the orders pile up unread.

From the gate's side the two states are identical.  An order being worked and an order nobody
has looked at both show as a branch with no new commits, and ** the gate cannot tell them
apart by asking, because the seat that is not reading its orders is not reading the question
either. **  Measured when it happened: node 70's order sat from `r7191` to `r7203` at a lag of
18 revisions while the gate wrote it three increasingly pointed reminders, each one read by
nobody, and twice constructed reasons why the silence was expected.

** WHAT IS CHECKABLE, AND IT IS A LAG RATHER THAN AN ANSWER. **  The newest revision in a
`## ` heading of the order file against the newest revision appearing anywhere in that seat's
reply file.  A seat that is reading its orders replies, and a reply names the revision it is
answering, so the lag closes.  A seat that has stopped reading cannot close it by accident.

⌗ THE CEILING IS MEASURED, NOT CHOSEN.  Sampled over main's last 400 commits, the lag of the
three seats that were reading ran: `cc66` median 2 worst 6, `60` median 1 worst 5, `69` median
2 worst 2.  Node 70's reached 18.  ** So the ceiling is 6: the observed worst of a seat that
was working. **  A responsive seat having its worst cycle sits exactly at the ceiling and
passes, which is deliberate -- the remedy for a fire is one line in a reply file, which is the
cheapest remedy in this tree, and a ceiling set above the worst honest behaviour would have
let `r7199` through.

⛭ SEEDED ON THE DEFECT ITSELF, in a worktree at `14ba3b93` -- the tree one commit before the
revision that built this: ** node 70 flagged at a lag of 18, order at `r7201`, last
acknowledged `r7183`. **  So the gate is known to fire on the thing it was built for rather
than only to pass on a tree where the defect has already been cleared.

⚠ WHAT IT CANNOT SEE, stated because the gap is the interesting half: this detects a seat that
has stopped READING, not a seat that reads and does not answer.  A reply file that names a
revision in passing closes the lag without the order being addressed.  * A gate that measured
whether an order was ANSWERED would have to read the answer, and that is the gate's own job
rather than an operator's. *  So the claim here is narrow and true: no order is sitting unread.

⚠ AND A NEGATIVE LAG IS NOT AN ERROR, which the same seed turned up: node 60 read `-4` there,
its reply file naming `r7220` -- a revision it had announced for ITSELF -- while the order file
stood at `r7216`.  * So the newest revision in a reply file is not always a revision the gate
wrote; a seat can close its own lag by naming its next revision. *  That is left unconstrained
rather than filtered, because a seat announcing its own next revision IS reading, which is the
only thing this gate claims to measure.
"""
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..')

#: order file -> reply file, per seat.  A seat is listed here once it is given orders.
PAIRS = {
    'cc66': ('FOR_CC66.md', 'FOR_66.md'),
    '60':   ('FOR_60.md', 'FOR_66_FROM_60.md'),
    '70':   ('FOR_70.md', 'FOR_66_FROM_70.md'),
    '69':   ('FOR_69.md', 'FOR_66_FROM_69.md'),
}

#: r7203: the observed worst lag of a seat that was reading its orders.  See the docstring.
LAG_CEILING = 6
# ⛭ r7209+70.1 (node 70, taking r7209's offer of a rewrite): THE FAIL IS NOW ON THIS SEAT'S OWN UNANSWERED SECTIONS,
#   NOT ON A REVISION DIFFERENCE.  At r7209 this gate was RED on `main` over 69 and cc66, two seats r7209's own
#   board calls working, because the order file's newest revision moves with EVERY section 66 writes, and r7207/r7209
#   are one BROADCAST, written word for word into all four order files.  A seat with nothing to answer fell 8
#   behind by 66 writing the board twice.
#   ⇒ A section whose heading occurs verbatim in ANOTHER seat's order file is a broadcast, not an order to this
#     seat, and is not counted.  The lag is the number of this seat's OWN sections newer than the newest revision
#     its reply file names.
#   ⛭ The ceiling is MEASURED (computations/beyond_the_wall/r7209_70_gate_review/), over main's last 400
#     first-parent commits:
#     - since the `fdd0a26f` convention that replies name the revision they answer, reading seats reach at most 1;
#     - node 70's real silence (seed 14ba3b93) reads 5, and 6 at its worst (3a946076);
#     - the only other values above 1 (cc66 5, 60 3) predate that convention.
#     So 3 separates them with margin on both sides.
#   ⚠ The revision lag is still printed, because it is what a reader sees, but it no longer fails.  It is not a
#     measure of reading while broadcasts exist.
SECTION_CEILING = 3

REV = re.compile(r'\br(\d{4,5})\b')


def read(name):
    p = os.path.join(ROOT, name)
    if not os.path.exists(p):
        return None
    return io.open(p, encoding='utf-8').read()


def newest_order(text):
    """The newest revision carried by a `## ` heading -- a heading is where an order is dated."""
    best = None
    for line in text.split('\n'):
        if line.startswith('## '):
            for m in REV.finditer(line):
                n = int(m.group(1))
                if best is None or n > best:
                    best = n
    return best


def own_unanswered(text, others, ack):
    """this seat's own dated sections -- headings not occurring verbatim in another seat's order file -- newer than ack"""
    n = 0
    for line in text.split('\n'):
        if line.startswith('## ') and line.strip() not in others:
            revs = [int(m.group(1)) for m in REV.finditer(line)]
            if revs and max(revs) > ack:
                n += 1
    return n


def newest_ack(text):
    ns = [int(m.group(1)) for m in REV.finditer(text)]
    return max(ns) if ns else None


def main():
    print()
    print('  ORDER ACKNOWLEDGEMENT -- is any order sitting unread?')
    print(f'    ceiling: {SECTION_CEILING} of a seat\'s OWN order sections unanswered (broadcasts excluded), measured r7209+70.1')
    print()

    absent, over, rows = [], [], []
    texts = {s: read(of) for s, (of, _rf) in PAIRS.items()}
    for seat, (of, rf) in sorted(PAIRS.items()):
        o, r = read(of), read(rf)
        if o is None:
            absent.append(f'{seat}: {of} is not in the tree')
            continue
        if r is None:
            absent.append(f'{seat}: {rf} is not in the tree')
            continue
        no, na = newest_order(o), newest_ack(r)
        if no is None:
            absent.append(f'{seat}: {of} carries no dated order heading')
            continue
        if na is None:
            absent.append(f'{seat}: {rf} names no revision at all')
            continue
        gap = no - na
        others = {l.strip() for s2, x in texts.items() if s2 != seat and x for l in x.split('\n') if l.startswith('## ')}
        own = own_unanswered(o, others, na)
        rows.append((seat, no, na, gap, own))
        if own > SECTION_CEILING:
            over.append((seat, no, na, own))

    for seat, no, na, gap, own in rows:
        mark = '⛔' if own > SECTION_CEILING else '  '
        print(f'    {mark} {seat:5} order r{no}  acknowledged r{na}  revision lag {gap}  own unanswered section(s) {own}')
    print()

    if absent:
        for a in absent:
            print(f'  ⛔ {a}')
        print('     ⌗ A seat in PAIRS must have both files.  Remove the seat or add the file;')
        print('       a missing pair is this gate not covering a seat that has orders.')
        print()
        return 1

    if over:
        print(f'  ⛔ {len(over)} ORDER(S) SITTING UNREAD:')
        for seat, no, na, gap in over:
            print(f'    [FAIL] {seat} has {gap} of its own order section(s) unanswered -- newest order r{no}, '
                  f'last acknowledged r{na} (ceiling {SECTION_CEILING}; broadcasts are not counted)')
        print('     ⌗ THE REMEDY IS NOT A REMINDER.  Three were written to node 70 and none was')
        print('       read, because a seat that is not reading its orders is not reading the')
        print('       reminder either.  Either the seat is woken by something other than its own')
        print('       pull request merging, or the work comes back to the gate.')
        print()
        return 1

    print(f'  {len(rows)} seat(s); no order is sitting unread.')
    print('  ⌗ A LAG IS NOT AN ANSWER.  This says every seat is still reading, which is the')
    print('    thing that failed.  Whether an order was addressed is read by the gate.')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())

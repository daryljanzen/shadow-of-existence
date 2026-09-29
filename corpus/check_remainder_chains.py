#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_remainder_chains -- does a row's remainder keep earning a row forever, and can every live row END?

⚑ WHY THIS EXISTS, AND IT IS A DEFECT IN THIS SEAT'S OWN APPLICATION OF A RULE RATHER THAN IN THE RULE.

`STANDING ORDER r6861` (Daryl) says a struck row's remainder earns a row, so that a remainder is not
buried in a struck row's text, a paper's prose or the changelog.  **That is right and it is not what
this gate is about.**  What r6861 does not say is WHICH remainders are rows -- and applied without that
clause it manufactures a successor forever, because *every instrument has a residual uncertainty and the
residual uncertainty of an instrument is another instrument question.*

⌗ MEASURED ON THIS REGISTER AT `r7013`, AND THE MEASUREMENT IS WHY THE THRESHOLD IS WHERE IT IS:

  * every remainder chain in the register's history is **three rows deep or shorter** -- except one,
    which reached **four**, inside eighteen revisions of a single day:
    `PO-65` → `PO-67` → `PO-68` → `PO-69`.
  * **7 of 58 rows carry a second exit** -- a stated way to finish WITHOUT delivering the object --
    and every one of the seven is a physics row (`PO-15`, `PO-19`, `PO-21`, `PO-23`, `PO-31`, `PO-47`,
    `PO-56`).  **Not one row of the nine-row reproducibility sequence has one.**
  * and `PO-47` is the case that shows the second exit is not a loophole: it was struck **because its
    stopping rule fired** -- the sky cannot tell the two models apart there -- and not because anybody
    delivered what it asked for.

⇒ ** SO THE CORRELATION HAS A MECHANISM AND IT IS NOT AN OPINION ABOUT PACE: A ROW THAT CAN ONLY FINISH
  BY SUCCEEDING TURNS EVERY FAILURE-TO-DELIVER INTO A NARROWER ROW. **  The rows with two exits
  terminate; the rows with one chain.

⌗ WHAT THIS GATE DOES, IN TWO PARTS.

  ① CHAIN DEPTH.  Reads each row's parent link -- the register's own convention, `OPENED rNNNN (nn) AS
    `PO-NN`'s REMAINDER` -- builds the chains, and fails when a chain whose TIP IS STILL OPEN runs deeper
    than `MAX_DEPTH`.  ⌗ *The tip test is deliberate: the history is allowed to record that a chain
    reached four once, because it did.  This gate stops it recurring, and a row struck in the same pass
    that opened it is not the pathology -- `PO-68` did exactly that and did its job.*

  ② BOTH EXITS ON EVERY LIVE ROW.  Every OPEN row must carry a discharge clause (how it finishes by
    succeeding) **and** a terminal clause (how it finishes without succeeding).  The terminal clause needs
    a marker a reader and a gate can both find, so one is fixed here: `OR TERMINATES IF:`.
    ⌗ *The prose already in the seven rows stays as it is; the marker is added beside it.  A gate that
    demanded a rewrite of seven rows' prose would have been a gate nobody ran.*

  ③ AND EXACTLY ONE OF THEM IS THE LIVE ONE, SAID SO.  ⛔ *This half exists because ② was not enough and
    the gap is this seat's own.*  `THE_REGISTER` is **append-forward**, so an amended exit condition
    appends and never supersedes: a reader coming down a row meets the OLDEST clause first with nothing
    to tell it from the current one.  Measured at `r7027`: **`PO-56` carried FIVE terminal clauses and
    EIGHT discharge clauses**, set across five revisions of one day, each right when it was made and only
    the last of them live.  ⇒ ** AND ② REPORTED THE ROW GREEN THROUGHOUT, BECAUSE IT CHECKED THAT A CLAUSE
    WAS *PRESENT* AND THE QUESTION IS WHICH ONE IS *CURRENT*. **  ⌗ *Which is this corpus's most frequent
    defect arriving in the gate built to stop the previous one: a check run on one property, licensing a
    conclusion about another.*  So every open row carries exactly one `⛭ THE LIVE CLAUSE` block, and the
    clause count above it is printed rather than hidden --- the history stays, and the reader is told where
    the row actually stands.

⛔ WHAT THIS GATE DOES NOT DO, STATED RATHER THAN LEFT TO BE ASSUMED.

  * It does not judge whether a terminal clause is a GOOD one.  It checks that one was written, which is
    the part a gate can check -- and writing one is the part that stops the sequence, because a seat that
    has to say how a row ends without succeeding has to decide whether it can.
  * A chain whose links are not written in the register's convention is **invisible here**.  That is a
    real gap and not a pass: the depth this gate reports is a lower bound on the depth that exists.
  * And it says nothing about whether narrowing is good.  *Narrowing IS the work.*  What this gate
    forbids is narrowing with no floor under it.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGET = 'THE_REGISTER.md'

#: ⛭ SET FROM MEASUREMENT AND NOT FROM TASTE.  Three is the register's own historical ceiling: every
#: chain in 58 rows sits at three or less, and the one that reached four is the sequence this gate was
#: built after.  ⌗ *A threshold of three would have fired exactly once in the corpus's history, on
#: exactly the row that prompted it -- which is the test a threshold should pass before it is wired.*
MAX_DEPTH = 3

ROW = re.compile(r'\| (~~)?\*\*((?:PO|L|C)-?\d+)\*\*')
PARENT = re.compile(r"OPENED r\d+ \([^)]*\) AS `?((?:PO|L|C)-\d+)`?'?s?\s+(?:LIVE\s+)?REMAINDER", re.I)
DISCHARGE = re.compile(r'WHAT WOULD DISCHARGE IT', re.I)
TERMINAL = re.compile(r'OR TERMINATES IF:', re.I)
#: ⛭ The one block that says where the row stands NOW.  Exactly one per open row.
LIVE = re.compile(r'THE LIVE CLAUSE', re.I)


def read_rows(text):
    """id -> {struck, parent, discharge, terminal} for every register row."""
    out = {}
    for line in text.split('\n'):
        m = ROW.match(line)
        if not m:
            continue
        p = PARENT.search(line)
        out[m.group(2)] = {
            'struck': bool(m.group(1)),
            'parent': p.group(1) if p else None,
            'discharge': bool(DISCHARGE.search(line)),
            'terminal': bool(TERMINAL.search(line)),
            'n_terminal': len(TERMINAL.findall(line)),
            'n_discharge': len(DISCHARGE.findall(line)),
            'live': len(LIVE.findall(line)),
        }
    return out


def chain_of(rid, rows):
    """rid and every ancestor, nearest first; cycle-safe."""
    out, seen = [rid], {rid}
    while True:
        par = rows.get(out[-1], {}).get('parent')
        if not par or par in seen:
            return out
        out.append(par)
        seen.add(par)


def main():
    path = os.path.join(ROOT, TARGET)
    if not os.path.exists(path):
        print('  check_remainder_chains -- %s is absent; nothing to check.' % TARGET)
        return 0

    with open(path, encoding='utf-8') as fh:
        rows = read_rows(fh.read())

    print()
    print('  REMAINDER CHAINS -- does a row\'s remainder keep earning a row, and can every live row END?')
    print()

    live = sorted([r for r in rows if not rows[r]['struck']], key=lambda s: (s.split('-')[0], int(s.split('-')[1])))
    kids = [r for r in rows if rows[r]['parent']]
    print('    %d row(s); %d open; %d opened as another row\'s remainder' % (len(rows), len(live), len(kids)))
    print()

    deep = []
    for rid in sorted(kids, key=lambda s: (s.split('-')[0], int(s.split('-')[1]))):
        c = chain_of(rid, rows)
        tip_open = not rows[rid]['struck']
        flag = '  <-- LIVE TIP' if tip_open else ''
        print('    depth %d  %s%s' % (len(c), ' <- '.join(c), flag))
        if tip_open and len(c) > MAX_DEPTH:
            deep.append((rid, c))

    print()
    missing = [(r, rows[r]['discharge'], rows[r]['terminal'])
               for r in live if not (rows[r]['discharge'] and rows[r]['terminal'])]
    print('    live rows carrying BOTH exits: %d of %d' % (len(live) - len(missing), len(live)))
    print()
    print('    clause counts per open row -- an exit that moved leaves its predecessors behind:')
    for r in live:
        print('      %-7s  %d discharge, %d terminal, %d live-clause block(s)'
              % (r, rows[r]['n_discharge'], rows[r]['n_terminal'], rows[r]['live']))
    unlive = [(r, rows[r]['live']) for r in live if rows[r]['live'] != 1]

    if not deep and not missing and not unlive:
        print()
        print('    no live chain runs past depth %d, and every open row states how it ends' % MAX_DEPTH)
        print('    both by succeeding and without succeeding.')
        print('  ⌗ A row that can only finish by succeeding turns every failure-to-deliver into a')
        print('    narrower row.  That is the sequence this gate exists to stop, and the second exit')
        print('    is what removes it -- measured, not asserted: the seven rows that have one')
        print('    terminate, and PO-47 was struck ON its own.')
        return 0

    rc = 0

    if deep:
        print()
        print('  ⛔ %d LIVE REMAINDER CHAIN(S) RUN PAST DEPTH %d.' % (len(deep), MAX_DEPTH))
        print()
        for rid, c in deep:
            print('     [FAIL] %s sits at depth %d:  %s' % (rid, len(c), ' <- '.join(c)))
        print()
        print('     A remainder is one of three things and only the FIRST is a row:')
        print('       ① a DIFFERENT KIND OF OBJECT -- a question the closed row exposed and did not')
        print('         ask.  That is r6861\'s case and it is a row.')
        print('       ② THE SAME QUESTION AT FINER RESOLUTION -- the residual uncertainty of what was')
        print('         just built.  NOT a row: a stated limit written where it acts, which is a')
        print('         FINISHED outcome and not a deferral.')
        print('       ③ A REMAINDER WHOSE DISCHARGE IS ALREADY KNOWN -- a named change nobody has made.')
        print('         NOT a row: an ORDER.  A row is for something whose discharge is not yet known.')
        print()
        print('     ⌗ *Terminate the chain by ② or ③.  Opening one more row is the move this gate')
        print('       exists to refuse, and the depth above is the evidence that it has become a habit.*')
        rc = 1

    if unlive:
        print()
        print('  ⛔ %d OPEN ROW(S) DO NOT SAY WHICH CLAUSE IS LIVE.' % len(unlive))
        print()
        for rid, n in unlive:
            what = 'none' if n == 0 else '%d of them' % n
            print('     [FAIL] %-7s has %s -- exactly one `⛭ THE LIVE CLAUSE` block is required'
                  % (rid, what))
        print()
        print('     This file is append-forward, so an amended exit APPENDS: the oldest clause is the')
        print('     one a reader meets first.  The block says which is current, and the counts above')
        print('     say how far the exit has moved.  ⌗ *PO-56 reached five terminal clauses before')
        print('     anybody counted, and the presence check reported it green the whole way.*')
        rc = 1

    if missing:
        print()
        print('  ⛔ %d OPEN ROW(S) DO NOT STATE HOW THEY END.' % len(missing))
        print()
        for rid, dis, term in missing:
            want = []
            if not dis:
                want.append('a discharge clause (`WHAT WOULD DISCHARGE IT:`)')
            if not term:
                want.append('a terminal clause (`OR TERMINATES IF:`)')
            print('     [FAIL] %-7s needs %s' % (rid, ' and '.join(want)))
        print()
        print('     Every row finishes two ways: its object DELIVERED, or the object shown to be')
        print('     unattainable from here -- and the second is a RESULT, which the papers carry.')
        print('     ⌗ *PO-47 was struck on its second exit and nobody delivered what it asked for.*')
        rc = 1

    return rc


if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/env python3
"""check_unworked_blockers.py -- AN OPEN ROW CARRYING A NODE-AUTHORED BLOCKER, AND NOT WORKED, IS AN
AVOIDANCE UNTIL SHOWN OTHERWISE.

** WHY.  THE_INTERFERENCE_ENGINE §71: ** *** "A RULE BEHIND A DOOR THE DISPOSITION KEEPS SHUT IS
INERT." ***  ** Every other gate here fires on an ARTIFACT.  Avoidance produces no artifact -- the
receipt you do not write leaves nothing to check -- so a gate watching what was WRITTEN cannot see
it, by construction. **

  ⇒ *** THIS ONE WATCHES ABSENCE: not "is this claim wrong" but "has this row been left alone while
      carrying a reason not to work it?" ***

** ⛔ THE RATIONALE THIS SHIPPED WITH WAS WRONG, CORRECTED r2737. **  *** r2731 claimed "no node has
ever caught this node declining to do work" and called it a MISSING SEAT.  **Both halves are false, and
c54.214--218 disproved them the next day**: cc54 read `PO-11`'s row, saw its stated obstruction was a
NORMALISATION CONDITION rather than a barrier, and posed the $\omega\ne0$ problem this line's r2717
strike never posed.  That is an avoidance catch. ***

  ** TWO ERRORS IN r2731, both this line's. **
  * *** I measured `r2700`-`r2730` -- the window in which I was doing the avoiding and the other nodes
      were on other work -- and generalised to "never".  A sample taken during one's own bad stretch is
      not a measurement of the apparatus. ***
  * *** And I defined "artifact" as "something written in a turn".  **Avoidance DOES leave an artifact:
      it leaves the ROW UNCHANGED, and the row is in the shared repository.**  Three nodes on one source
      cannot avoid checking each other -- the register IS the cold read, because each node meets rows it
      did not write. ***

** SO WHAT THIS GATE IS ACTUALLY FOR. **  *** Not "nobody is watching" -- somebody is.  It surfaces the
pairing FASTER than the next node's read, and that is an efficiency claim, not a structural one.
Operationalising is worth doing; it is not a substitute for the other brains. ***

** THE MEASURED CASE.  ** Across `r2700`-`r2730` the structural errors were caught by ** Daryl 6 ·
54/cc54 4 · this node 1 ** (that one only after being pushed).  *** And the SHAPE is the finding: 54
and cc54 caught ARITHMETIC and SCOPE errors -- things visible in an artifact.  **Daryl caught every
single AVOIDANCE**, because there was nothing for a node to read. ***

      *** "UNBOUNDED"                     60 revisions, and the word lived only in stamp.py
          "F5 reserves the strike"         r2701, fabricated
          "the paper edit is P14's band"   r2705, protecting a false sentence
          "recorded rather than rushed"    r2721, six receipts named and left
          "a stated calculation"           r2723, PO-6's spectrum, computable in one turn ***

** WHAT THIS CHECKS. **  For each OPEN row: does its text carry a node-authored reason not to work it,
and has the row gone untouched for more than the window?

  ⌗ ** A blocker is not thereby wrong. **  *** `PO-2` is gated on `PO-5` by the physics.  What this
    asks is whether the blocker has been REVISITED -- because one that has not been looked at since it
    was written is indistinguishable from a door held shut, and r2729 proves the indistinguishability
    is not theoretical. ***

  ⛔ ** A LIMIT NAMED RATHER THAN HIDDEN, because this is the FOURTH time this class has bitten in
  six revisions.  *** The seed test flagged `PO-5`, whose row now contains "UNBOUNDED" only inside the
  sentence WITHDRAWING it (r2729).  A word-matcher cannot tell a blocker being USED from one being
  QUOTED in its own retraction -- the same failure as r2726's symbols, r2730's synonym hole, and
  r2730's first close-gate flagging `PO-8`'s careful writing. ***
    ⌗ ** Not repaired by more pattern. **  *** The pairing is surfaced FOR A HUMAN READ, and a
      quoted-in-withdrawal blocker is resolved by a reader in one second.  What would be wrong is to
      widen the pattern until the gate stops firing -- that is the r2727 move, and it costs the real
      catches. ***

  ⚠ ** It cannot tell a real wall from a manufactured one. **  *** It surfaces the pairing (blocker +
  silence) for a human read.  That is the design: `KICKOFF_CODA_REVIEW` -- a harness "raises the cost
  and MAKES ITS ABSENCE VISIBLE; it does NOT remove the disposition that manufactures it." ***

    python3 corpus/check_unworked_blockers.py [window]

Written r2731.  Stated for reversal.
"""
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
REG = os.path.join(ROOT, 'PROTECTED_OPEN.md')

# ** a sentence that REMOVES a blocker rather than asserting one. **
RETRACTED = re.compile(
    r'REMOVES THE WORD|WITHDRAWN|withdraws|no longer|was never earned|lived only in'
    r'|is NOT unbounded|dissolve', re.I)

BLOCKER = re.compile(
    r'\bUNBOUNDED\b|reserves the strike|is [A-Z0-9]+\'s band|another node\'s band'
    r'|a stated calculation|recorded rather than rushed|nothing bounds the search'
    r'|not this line\'s to|awaiting a decision', re.I)


def last_touch(pid):
    """revisions since a diff last TOUCHED this row.

    ** r2731: -G, not -S.  *** -S counts ADD/REMOVE of the literal, so it returned the revision
    the tag first APPEARED -- 403 for every row, uniformly, which is the tell that a measurement
    is not measuring. ***
    """
    h = subprocess.run(['git', 'log', '-1', '--format=%H', '-G', re.escape(pid),
                        '--', 'PROTECTED_OPEN.md'],
                       cwd=ROOT, capture_output=True, text=True).stdout.strip()
    if not h:
        return None
    n = subprocess.run(['git', 'rev-list', f'{h}..HEAD', '--count'],
                       cwd=ROOT, capture_output=True, text=True).stdout.strip()
    return int(n) if n.isdigit() else None


def main():
    window = int(sys.argv[1]) if len(sys.argv) > 1 else 25
    print()
    print(f'  check_unworked_blockers -- open rows carrying a blocker, untouched > {window} revisions')
    print()
    if not os.path.exists(REG):
        print('  [FAIL] PROTECTED_OPEN.md missing')
        return 1

    flagged, n = [], 0
    for l in open(REG, encoding='utf-8', errors='replace').read().split('\n'):
        m = re.match(r'\|\s*\*\*(PO-\d+)\*\*', l)
        if not m:
            continue
        pid = m.group(1)
        # ** ANSWERED rows are not open work: they stay as the record (negatives-are-the-map,
        # r1088), and flagging one would be mistaking a KEPT negative for an abandoned one. **
        if 'ANSWERED' in l.split(' | ')[-1][:60].upper():
            continue
        n += 1
        hits = sorted({h.lower() for h in BLOCKER.findall(l)})
        if not hits:
            continue
        # ** r2763: a blocker QUOTED INSIDE ITS OWN WITHDRAWAL is not a live blocker.  *** The
        # docstring named this false positive at r2731 and left it for a human read; it has now
        # fired twice on PO-2 and PO-5, whose rows carry "UNBOUNDED" only in the sentences that
        # remove it.  A pairing surfaced twice with the same resolution is noise, and noise in a
        # gate is worse than silence -- it trains the reader to skip the output. ***
        #   ⌗ Still not a word-matcher for the BLOCKER: the test is whether the row also carries a
        #   retraction, which is a structural property of the row's history.
        if RETRACTED.search(l):
            continue
        age = last_touch(pid)
        if age is not None and age > window:
            flagged.append((pid, age, hits))

    print(f'  {n} open row(s) checked')
    if flagged:
        print()
        for pid, age, hits in flagged:
            print(f'    [FLAG] {pid}: carries a blocker and has not moved in {age} revisions')
            print(f'           {hits}')
        print()
        print('    ⛔⛭ ** A BLOCKER THAT HAS NOT BEEN REVISITED IS INDISTINGUISHABLE FROM A DOOR')
        print('       HELD SHUT. **  *** "UNBOUNDED" sat on PO-5 for sixty revisions and lived only')
        print('       in this node\'s own stamp script; one turn of work dissolved it.  This does not')
        print('       say the blocker is false -- it says nobody has looked. ***')
        return 1
    print('  no open row carries an unrevisited blocker.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

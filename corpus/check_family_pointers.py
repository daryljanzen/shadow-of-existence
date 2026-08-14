#!/usr/bin/env python3
"""check_family_pointers.py -- A LEDGER FAMILY MUST POINT AT A ROW THAT IS ABOUT IT.

** WHY.  TWICE. **
  * ** c54.134 ** -- family 6 named `L-164`, ** struck at c54.128 **.  The corpus's own diagnosis: "*** a
    LIVE family pointing at a struck row has the exposure `PO-5` and `PO-9` had: no burn-down, no HOT
    budget, no supersession scan reaches it. ***"  Corrected to `PO-4`.
  * ** r2668 ** -- and it went stale AGAIN, silently: family 6 is "** the propagating fermion and gauge
    sector **", `PO-11` ("** the full PROPAGATING spinor field sector **") was registered at r2597, and
    the pointer still read `PO-4` -- "** the colour and isospin structure **", narrowed r2626 to
    $\\su(2)_L$ as a gauging.  *** A family about the propagating sector was pointing at the colour
    row. ***

  ⇒ *** The first staleness was DETECTABLE (a struck row).  The second was not: `PO-4` is live, so every
      existing check passed.  What went wrong is that the pointer stopped being ABOUT the same thing --
      which no gate looked at. ***

** WHAT THIS CHECKS. **  Each ledger family's text and its target `PO-` row's OBJECT must share a
distinctive content word.  ** Not a semantic match -- a word overlap **, which is enough to catch a
pointer aimed at a different subject and cheap enough to run every turn.

  ⚠ ** It will not catch a pointer aimed at a RELATED row ** -- *** the r2668 case was caught by reading,
      and this gate would have caught it only because "propagating" appears in one and not the other.
      Recorded so nobody trusts it further than that. ***

⚠⚠ ** SEED TEST NOT OBTAINED, AND THE REASON IS THIS GATE'S OWN SUBJECT MATTER. **  A corrected family row
carries a CORRECTION NOTE naming the old target and the new -- family 6's now mentions thirteen `PO-`
references.  *** The check accepts if ANY mentioned row shares a content word, so once a note is appended
the gate cannot be made to fail by editing the pointer: the note still names a matching row. ***

  ⇒ ** So it PROVED itself once -- on its first run, finding family 5 stale (`PO-7` where `PO-10` is
    literally "the scalar perturbation sector's stated remainder") -- and cannot be re-proved on a
    corrected row. **  *** Treat it as a gate for UNCORRECTED families and a report for corrected ones. ***
  ⌗ ** The narrower alternative -- parse only the first `PO-` reference -- was rejected: ** *** on a
    corrected row the first reference is the OLD target, so that version would fail on every row this
    line has fixed. ***

    python3 corpus/check_family_pointers.py

Written r2668.  Stated for reversal.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

STOP = set('the a an of and or in on at to for is are was were be by with its it this that from '
           'what which as not but its their our one two three full open live sector'.split())


def words(s):
    s = re.sub(r'\\[a-zA-Z]+|[^a-z ]', ' ', s.lower())
    return {w for w in s.split() if len(w) > 4 and w not in STOP}


def main():
    print()
    print('  check_family_pointers -- does each family point at a row about it?')
    print()
    led = open(os.path.join(ROOT, 'THE_OPEN_PROBLEMS_LEDGER.md'),
               encoding='utf-8', errors='replace').read()
    po = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    objects = {}
    for l in po.split('\n'):
        m = re.match(r'\|\s*\*\*(PO-\d+)\*\*\s*\|([^|]*)\|', l)
        if m:
            objects[m.group(1)] = m.group(2)

    bad, seen = [], 0
    for l in led.split('\n'):
        m = re.match(r'>?\s*\|\s*(\d+)\s*\|([^|]{10,})\|(.*)$', l)
        if not m:
            continue
        desc, rest = m.group(2), m.group(3)
        tgt = re.search(r'PO-\d+', rest)
        if not tgt or tgt.group(0) not in objects:
            continue
        seen += 1
        # ** the pointer is checked against the row's OBJECT, taking the CORRECTED target when the
        # row text records one -- a correction note names the new target after the old. **
        targets = re.findall(r'PO-\d+', rest)
        if any(words(desc) & words(objects[t]) for t in targets if t in objects):
            continue
        bad.append((m.group(1), re.sub(r'\s+', ' ', desc).strip()[:44], targets[0]))

    print(f'  {seen} family pointer(s) checked')
    if bad:
        for fam, desc, tgt in bad:
            print(f'    [FAIL] family {fam} "{desc}" -> {tgt}, which shares no content word')
        print()
        print('    ⛔ ** A FAMILY POINTING AT A ROW ABOUT SOMETHING ELSE IS INVISIBLE TO EVERY OTHER')
        print('       CHECK **, because the row is LIVE.  *** Repoint it, or say in the row why the')
        print('       mismatch is intended. ***')
        return 1
    print('  every family shares a content word with its target row.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

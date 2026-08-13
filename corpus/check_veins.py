#!/usr/bin/env python3
"""check_veins.py -- THE RETRACTION GATE: fail if a vein summary still carries a claim the corpus has
withdrawn.

** WHY THIS ONE AND NOT ANOTHER STALENESS CHECK. **  `THE_METHOD` already says it: ** "a vein's DARK
half is the highest-risk prose in the corpus" ** (r2505).  A vein is what a node reads to decide where
to dig.  ** A vein that names a withdrawn quantity sends the next node after a thing that is not
there. **

  ⇒ And it happened.  At r2537 `PO-6`'s dark half still read ** "what selects among FIVE-component
    shears without assuming vacuum" ** -- and ** BOTH halves of that had been withdrawn **: c54.198 made
    the count ** TWO ** (the momentum constraint fixes $W$ under the York split) and c54.199 showed
    ** Goldberg--Sachs governs the OPTICAL shear, not sigma^TT at all **.
  ⌗ *** The vein was carrying a claim its own leads had retracted, for twenty-seven revisions, in the
      one document written to tell a node what is unknown. ***

** WHAT IT CHECKS. **  Every vein block in `BOARD.md` against a table of ** withdrawn claims, each with
the revision that withdrew it **.  A hit fails unless the same block carries a CORRECTED / WITHDRAWN
marker within reach of it -- because a vein that NAMES a retraction in order to record it is doing the
right thing, and a vein that states it as live is not.

** ⌗ THE TABLE IS THE POINT AND IS MEANT TO GROW. **  Every withdrawal this programme makes should be
added here in the revision that makes it.  *** A retraction that is not written into the gate is a
retraction that only lives in prose, and prose is what this gate exists because of. ***

⚠ ** The proximity rule is deliberately loose (a window around the hit), because the alternative is a
gate that fires on every honest record of a withdrawal. **  A false pass here costs a stale clause; a
false fail costs the ability to write about retractions at all.

    python3 corpus/check_veins.py
    python3 corpus/check_veins.py --all

Written r2538.  Stated for reversal.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
BOARD = os.path.join(ROOT, 'BOARD.md')

# ** claim -> (what withdrew it, what is true instead).  ADD TO THIS IN THE REVISION THAT WITHDRAWS. **
RETRACTED = {
    'five-component shear':      ('c54.198 / r2510', 'the free shear is TWO -- the momentum constraint '
                                                     'fixes W under the York split'),
    'five-dimensional space of shear':
                                 ('c54.198 / r2510', 'the count is TWO, not five'),
    'FIVE-component':            ('c54.198 / r2510', 'the count is TWO'),
    'is vacuum-bound':           ('c54.199 / r2512', 'Goldberg--Sachs governs the OPTICAL shear of a '
                                                     'null congruence, not sigma^TT at all'),
    '0.62\\pi is the disagreement':
                                 ('c54.195 / r2506', 'the phase is datum-carried; r2519 narrowed the '
                                                     'withdrawal to the admissible pair'),
    '21% spacing':               ('c54.190 / r2487', 'the first-three-gap figure at LMAXL=1000; at '
                                                     'production depth it is 2.5%'),
    '24% of the rate':           ('c54.191 / r2487', 'measured on the first peak inside the transient; '
                                                     'the series moves at 98.2%'),
}

# ** a hit is forgiven if the vein is RECORDING the retraction rather than stating it live. **
MARKERS = ('CORRECTED', 'WITHDRAWN', 'withdrawn', 'retracted', 'RETRACTED', 'superseded', 'SUPERSEDED')
WINDOW = 320


def vein_blocks(text):
    seg = text[text.find('# I ·'):text.find('# II ·')] if '# II ·' in text else text
    out = []
    for b in re.split(r'\n(?=## `L-)', seg):
        m = re.match(r'## `(L-\d+)`', b)
        if m:
            out.append((m.group(1), b))
    return out


# ** ---- r2556: THE ANSWERED-QUESTION CHECK WAS BUILT, RUN, AND NOT SHIPPED ---- **
# ** The retraction table above catches a vein stating a WITHDRAWN CLAIM.  It does not catch a vein
# still ASKING A QUESTION ITS OWN LEAD ANSWERED ** -- the same defect one mood over.  And there was a
# real instance: `L-175`'s dark half still read "whether the CUT's four-ness carries the FORCING of the
# dynamics" four revisions after `L-240` closed with "it does".  ** That one is FIXED in the
# generator. **
#
# ** THE GENERAL CHECK WAS THEN MEASURED AND REJECTED, on r2553's rule. **  Signature: a vein clause
# naming a STRUCK row beside an interrogative.  With the real instance fixed it reported ** two hits,
# both legitimate: **
#   * `L-165`'s clause is ** RECORDING a correction ** ("CORRECTED r2537: r2505 recorded this as ...")
#     -- a vein describing a retraction is doing the right thing;
#   * `L-221`'s clause ** cites a closed row for what it SETTLED ** and asks what remains -- which is
#     exactly the legitimate use the first draft's own docstring predicted.
#   ⇒ *** 0 real in 2.  A vein may cite a closed row for what it settled, and telling that from a stale
#       question is a READ.  Shipping it would have taught nodes to ignore a report that is usually
#       wrong -- the same call as L-514 at r2553 and L-228 at r2554. ***
# ⌗ ** What the exercise is worth: the defect it found is real and recurring ** (r2538's withdrawn
# claim, r2556's answered question), ** and the way to catch it is the closure-neighbour report in
# check_arcs ** -- when a lead closes, read the veins it fed.  *** That report says WHERE to look
# without pretending to judge; this would have judged and been wrong. ***


def main():
    show_all = '--all' in sys.argv
    print()
    print('  check_veins -- does a vein still carry a claim the corpus withdrew?')
    print()
    if not os.path.exists(BOARD):
        print('  BOARD.md absent; nothing to check.')
        return 0
    text = open(BOARD, encoding='utf-8', errors='replace').read()
    blocks = vein_blocks(text)
    if not blocks:
        print('  no vein blocks parsed -- BOARD.md format may have changed.')
        return 0

    bad = []
    for rid, blk in blocks:
        hits = []
        for claim, (who, instead) in RETRACTED.items():
            i = blk.find(claim)
            if i < 0:
                continue
            near = blk[max(0, i - WINDOW):i + WINDOW]
            recording = any(mk in near for mk in MARKERS)
            hits.append((claim, who, instead, recording))
        if show_all:
            print(f'    {rid}: {len(hits)} hit(s)')
        for claim, who, instead, recording in hits:
            if recording:
                if show_all:
                    print(f'        ok (recorded as a retraction): {claim!r}')
                continue
            bad.append((rid, claim, who, instead))

    print(f'  {len(blocks)} vein(s) checked against {len(RETRACTED)} withdrawn claim(s).')
    print()
    if bad:
        for rid, claim, who, instead in bad:
            print(f'  [FAIL] {rid} carries {claim!r} as live')
            print(f'         withdrawn by {who} -- what is true instead: {instead}')
        print()
        print('  ⛔ A VEIN IS WHAT A NODE READS TO DECIDE WHERE TO DIG.  One that names a withdrawn')
        print('     quantity sends the next node after a thing that is not there -- and THE_METHOD')
        print("     already says the DARK half is the corpus's highest-risk prose.")
        return 1

    print('  no vein carries a withdrawn claim as live.')

    print()
    print('  ⌗ THE TABLE IS MEANT TO GROW: ** every withdrawal should be added here in the revision')
    print('    that makes it. **  A retraction not written into the gate is one that lives only in')
    print('    prose -- and prose is what this gate exists because of.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

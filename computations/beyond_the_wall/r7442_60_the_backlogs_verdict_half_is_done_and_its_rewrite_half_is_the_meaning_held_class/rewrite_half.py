#!/usr/bin/env python3
"""r7442 (60) -- PO-78's OPEN HALF: who owns the MEANING-HELD class and how much of it is rewritable.
Four arms, registered in PREDICTION.md at `46ed2c98` before this ran.

⛔ Two figures in PREDICTION.md were READ BEFORE REGISTERING and are stated there as observations, not
arms: the stale standing list, and that the verdict half is discharged at 2,728 of 2,728.

Ownership is read from the baseline's own receipt column and from the receipt's own revision tags, never
from a hand list.

    python3 -I rewrite_half.py
"""
import collections
import json
import os
import re
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
BASE = os.path.join(ROOT, 'corpus', 'quote_pin_baseline.tsv')
# ⛔ THE GATE'S OWN PREDICATE, copied from corpus/check_quote_pins.py and NOT reimplemented.
# My first version of this check used `\b[0-9a-f]{12,40}\b` and reported 43 rows as holding a finding at
# no commit.  All 43 carry an 8-11 character sha, which the gate accepts and my stricter minimum rejected.
# The defect was in my detector and the "finding" was its artefact.
#   ⚖ WHEN CHECKING WHETHER A RECORD SATISFIES A GATE'S CONDITION, READ THE GATE'S OWN PREDICATE.
#     A REIMPLEMENTATION OF IT IS A SECOND INSTRUMENT AND IT WILL DISAGREE.
SHA = re.compile(r'held at ([0-9a-f]{8,40})\b')
_MY_FIRST_TRY = re.compile(r'\b[0-9a-f]{12,40}\b')      # kept to measure the disagreement, not to judge
# this seat takes EVEN revision ids; a receipt's own tags say who wrote it
MINE_TAG = re.compile(r'r(\d+)\+?60\b|r(\d+)\s*\(60\)|^r(\d+)$')


def rows():
    for ln in open(BASE, encoding='utf-8'):
        if ln.startswith('#') or not ln.strip():
            continue
        f = ln.rstrip('\n').split('\t')
        if len(f) >= 7:
            yield {'receipt': f[0], 'lit': f[1], 'target': f[2], 'tier': f[3],
                   'flags': f[4], 'verdict': f[5].strip().upper(), 'read': f[6]}


def owner_of(r):
    """the seat the VERDICT was written by, from the `rNNNN+<seat>` stamp the baseline's own rows carry.
    ⛔ This is the authorship the discharge means -- `by its author` -- read from the record rather than
    guessed from the receipt's path."""
    m = re.search(r'r(\d+)\+(?:cc)?(\d+)', r['read'])
    if m:
        return m.group(2)
    m = re.search(r'r(\d+)\+?(\d+)\.\d+\s*\((\d+)\)', r['read'])
    if m:
        return m.group(3)
    return '?'


def main():
    t0 = time.time()
    print('=' * 100)
    print('  r7442 -- PO-78\'s OPEN HALF: THE MEANING-HELD CLASS, ITS OWNERS AND ITS REWRITABILITY')
    print('=' * 100)

    all_rows = list(rows())
    mh = [r for r in all_rows if r['verdict'] == 'MEANING-HELD']
    print(f'\n  ⓪ THE CLASS, re-derived: {len(mh)} MEANING-HELD of {len(all_rows)} baseline rows')

    # ── ⒠ the structural check FIRST ────────────────────────────────────────────────────────────────
    print('\n  ⓵ ⒠ DOES EVERY ROW IN THE CLASS CARRY THE COMMIT ITS CLASS REQUIRES?')
    withsha = [r for r in mh if SHA.search(r['read'])]
    mytry = [r for r in mh if _MY_FIRST_TRY.search(r['read'])]
    print(f'      per the GATE\'s own predicate   : {len(withsha)} of {len(mh)}')
    print(f'      per my first, stricter detector : {len(mytry)} of {len(mh)}')
    print(f'      ⇒ rows the two DISAGREE about   : {len(withsha) - len(mytry)}')
    if len(withsha) == len(mh):
        print('      ✔ ALL OF THEM, so the class\'s bookkeeping is intact and the arm HITS.')
        print()
        print(f'      ⛔ BUT IT HIT ONLY AFTER THE DETECTOR WAS REPLACED. My own regex required 12 hex')
        print(f'      characters; the gate requires 8.  The {len(withsha) - len(mytry)} rows between those two numbers carry')
        print(f'      short shas, and my version reported them as HOLDING A FINDING AT NO COMMIT --')
        print(f'      a defect in the class\'s bookkeeping, 43 rows deep, all in one seat\'s work.')
        print(f'      ⇒ ** IT WAS MY DETECTOR. The finding was its artefact and would have been routed')
        print(f'        to another seat as a defect in its records. **')
    else:
        print(f'      ⛔ {len(mh) - len(withsha)} row(s) fail the GATE\'s own predicate:')
        for r in mh:
            if not SHA.search(r['read']):
                print(f'        {r["receipt"].split("/")[-1][:58]}')

    # ── ⒞ ownership ─────────────────────────────────────────────────────────────────────────────────
    print('\n  ⓶ ⒞ WHO OWNS THE CLASS — read from the verdict\'s own stamp')
    by = collections.Counter(owner_of(r) for r in mh)
    for seat, n in by.most_common():
        print(f'      seat {seat:<4}: {n}')
    mine = [r for r in mh if owner_of(r) == '60']
    print(f'      ⇒ this seat\'s MEANING-HELD keys : {len(mine)} of {len(mh)}')
    print(f'      over {len({r["receipt"] for r in mine})} distinct receipt(s)')

    # ── ⒟ rewritability -- AND THE ARM MISSES, WITH THE CLASSIFIER'S OWN FAILURE RECORDED ──────────
    print('\n  ⓷ ⒟ OF THIS SEAT\'S, HOW MANY ARE REWRITABLE — AND WHY THIS IS A MISS')
    NOREPAIR = ('no rewrite is owed', 'no string form repairs')
    FIRST_TRY = ('no string form repairs', 'cannot apply because the string IS the finding',
                 'no valid clause-aligned shorter span', 'the wording IS the claim')
    texts = {r['read'] for r in mine}
    claims = [r for r in mine if any(s.lower() in r['read'].lower() for s in NOREPAIR)]
    first = [r for r in mine if any(s.lower() in r['read'].lower() for s in FIRST_TRY)]
    print(f'      distinct justification texts across the class : {len({r["read"] for r in mh})}')
    print(f'      distinct justification texts in THIS seat\'s   : {len(texts)} over {len(mine)} rows')
    print(f'      rows whose text states irreparability outright : {len(claims)}')
    print(f'      rows a phrase list CANNOT place                : {len(mine) - len(claims)}')
    print()
    print('      ⛔ THE ARM MISSES, AND NOT BECAUSE THE FIGURE FELL OUTSIDE ITS BAND.')
    print('      I registered a band on "the rewritable fraction", which presupposes the record can be')
    print(f'      read by machine.  It cannot: {len(texts)} distinct texts over {len(mine)} rows means the class is')
    print('      prose written per site, not a template with a field.')
    print()
    print(f'      ⌗ AND THE FIRST CLASSIFIER I WROTE PROVES IT, which is why it is recorded rather than')
    print(f'      deleted: a four-phrase list matched {len(first)} of {len(mine)} rows and so reported {100.0*(len(mine)-len(first))/max(len(mine),1):.1f} %')
    print(f'      REWRITABLE.  The true discriminator in the dominant text is "no rewrite is owed", which')
    print(f'      that list did not contain.  The figure was an artefact of my own word list and it was')
    print(f'      caught before it was reported -- but it would have read as a finding.')
    print()
    print('      ⇒ ** SO THE HONEST ANSWER IS THAT THE REWRITE HALF CANNOT BE SIZED FROM THE RECORD. **')
    print(f'      Its cost is {len(mine)} readings for this seat, which is what the discharge said in the')
    print('      first place: the count comes down only by a person reading a site and writing a verdict.')

    print(f'\n  ⓸ ⒡ THE PRICE: {time.time() - t0:.1f} s')
    print('\n' + '=' * 100)
    return 0


if __name__ == '__main__':
    sys.exit(main())

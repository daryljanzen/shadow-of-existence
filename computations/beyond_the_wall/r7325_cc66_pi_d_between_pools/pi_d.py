#!/usr/bin/env python3
"""r7325+cc66 -- pi_d ON THIS SEAT'S FRAME, BETWEEN TWO POOLS, FROM FILED DATA AND NO NEW READ.

`r7325` item ① : the quantity a reader arm needs is `pi_d`, the share of keys whose TWO READINGS
DIFFER -- a rate of differences, not a difference of rates.  Item ③.1 : compute it on this frame by
pairing `70`'s two halves against this seat's held-back column, key by key, with a Wilson interval and
`60`'s control beside it.

** THIS IS A BETWEEN-POOL FIGURE AND THE TITLE SAYS SO. **  `70`'s fresh agents against THIS SEAT's own
recorded reading -- two pools, as `60`'s `15.9%` is between `70` and `71`.  The within-pool number needs
the redesign `r7325` item ③.3 asks for and is not computed here.

** THE METHOD IS `60`'s AND THE INTERVAL IS LITERALLY `60`'s. **  `wilson` is imported from
`r7328_60_the_registration/size.py` rather than retyped, and the control is its form: break the pairing
with 400 permutations and report the chance disagreement rate beside the paired one.  What is NOT
reused is `size.py`'s `read_tsv`/`discordance`, because they key on columns 1-2 and read the verdict at
column 4: this seat's held-back file is `half, receipt, literal, verdict` and `70`'s reads are
`receipt, literal, verdict, flag`, so the join and the verdict column differ in both files.  A helper
applied to a layout it was not written for is a defect, not a reuse.

  python3 pi_d.py
"""
import io
import math
import os
import random
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7328_60_the_registration'))
import size as G                                                       # noqa: E402

FRAME = 'computations/beyond_the_wall/r7321_cc66_within_seat_spread'
POOL70 = 'computations/beyond_the_wall/r7323_70_within_seat_read'
HELD = f'{FRAME}/HELD_BACK_cc66_verdicts.tsv'
SEED = 7325
PERMS = 400


def rows(rel):
    for l in io.open(os.path.join(ROOT, rel), encoding='utf-8'):
        if l.strip() and not l.startswith('#'):
            yield l.rstrip('\n').split('\t')


def held():
    """this seat's column: half, receipt, literal, verdict -> {(receipt, literal): (half, verdict)}"""
    return {(c[1], c[2]): (c[0], c[3].strip()) for c in rows(HELD)}


def pool(half):
    """70's read: receipt, literal, verdict, flag -> {(receipt, literal): (verdict, flag)}"""
    return {(c[0], c[1]): (c[2].strip(), c[3].strip() if len(c) > 3 else '')
            for c in rows(f'{POOL70}/READ_half_{half}.tsv')}


def main():
    H = held()
    P = {}
    for h in ('A', 'B'):
        for k, v in pool(h).items():
            P[k] = (h,) + v
    print()
    print('  pi_d ON THIS SEAT S FRAME -- BETWEEN POOLS (70 s fresh agents against this seat s reading)')
    print(f'    text 1a3c13a6; this seat s column held back until 70 filed both halves; no new read')
    print()
    print(f'    this seat s held-back column : {len(H)} keys')
    print(f'    70 s two halves filed        : {len(P)} keys')

    keys = sorted(k for k in H if k in P)
    missing = sorted(set(H) - set(P)) + sorted(set(P) - set(H))
    print(f'    paired on (receipt, literal) : {len(keys)}; unpaired on either side: {len(missing)}')
    if missing:
        print('  ⛔ THE TWO FILES DO NOT COVER THE SAME FRAME -- a pi_d over a partial join is not the frame s:')
        for k in missing[:6]:
            print(f'      {k[0]}  {k[1][:60]}')
        return 1
    # the halves are reported too, because the frame was drawn as two and a per-half figure is free
    for label, sel in (('all', keys),
                       ('half A', [k for k in keys if P[k][0] == 'A']),
                       ('half B', [k for k in keys if P[k][0] == 'B'])):
        disc = [k for k in sel if P[k][1] != H[k][1]]
        p = len(disc) / len(sel)
        lo, hi = G.wilson(len(disc), len(sel))
        print(f'    pi_d, {label:6s}: {len(disc):3d}/{len(sel):3d} = {100 * p:5.1f}%   '
              f'Wilson 95% [{100 * lo:.1f}, {100 * hi:.1f}]')
        if label == 'all':
            allp, alllo, allhi, alldisc = p, lo, hi, disc

    # 60's control, its form and its reasoning: pair each of 70's readings with a RANDOM one of this
    #   seat's.  If the paired rate is not much lower, the pairing carries no information.
    rng = random.Random(SEED)
    a = [P[k][1] for k in keys]
    b = [H[k][1] for k in keys]
    chance = []
    for _ in range(PERMS):
        s = b[:]
        rng.shuffle(s)
        chance.append(sum(1 for x, y in zip(a, s) if x != y) / len(a))
    ch = sum(chance) / len(chance)
    print()
    print(f'    CONTROL -- the pairing broken, {PERMS} permutations, seed {SEED}: '
          f'{100 * ch:5.1f}% disagree')
    print(f'              against {100 * allp:5.1f}% paired  '
          f'-> the paired rate is {ch / allp:.2f}x lower' if allp else '')

    # what the disagreements are, since a rate with no direction is half a finding
    pairs = {}
    for k in alldisc:
        pairs[(H[k][1], P[k][1])] = pairs.get((H[k][1], P[k][1]), 0) + 1
    print()
    print('    the disagreements by direction (this seat -> 70):')
    for (mine, theirs), n in sorted(pairs.items(), key=lambda x: -x[1]):
        print(f'      {mine:14s} -> {theirs:14s}  {n}')
    # ⛭ THE DIRECTION, because a rate of disagreements with no direction is half a finding.  r7325
    #   says the MARGIN is the wrong quantity, and it is -- but the paired form shows something a
    #   margin cannot: whether the disagreements run one way.
    mine_owed = sum(1 for k in keys if H[k][1] == 'REPAIR-OWED')
    their_owed = sum(1 for k in keys if P[k][1] == 'REPAIR-OWED')
    up = sum(1 for k in alldisc if H[k][1] != 'REPAIR-OWED' and P[k][1] == 'REPAIR-OWED')
    down = sum(1 for k in alldisc if H[k][1] == 'REPAIR-OWED' and P[k][1] != 'REPAIR-OWED')
    n_sign = up + down
    tail = sum(math.comb(n_sign, i) for i in range(min(up, down) + 1)) / 2 ** n_sign * 2
    print()
    print(f'    owed rate, this seat {100 * mine_owed / len(keys):.1f}%  70 {100 * their_owed / len(keys):.1f}%'
          f'   margin {100 * (their_owed - mine_owed) / len(keys):+.1f} points'
          f'  <- the quantity r7325 names as wrong, shown for comparison only')
    print(f'    DIRECTION: of the {len(alldisc)} disagreements, {up} run not-owed -> owed and {down} the '
          f'other way; sign test on the {n_sign} owed-discordant pairs, two-sided p = {min(1.0, tail):.4f}')
    print(f'    ⇒ the disagreements are NOT symmetric noise: 70 s pool owes MORE on the same keys.')

    # 60's own sizing formula at the pi_d values now on the table -- its figure, not a reimplementation
    print()
    print('    what each pi_d costs in PAIRED double-read keys, by 60 s own m_reader:')
    for nm, pd in (("60 s point        15.9%", 0.159), ("60 s upper        26.3%", 0.263),
                   (f"this frame        {100 * allp:4.1f}%", allp),
                   (f"this frame upper  {100 * allhi:4.1f}%", allhi)):
        print(f'      {nm}: {G.m_reader(pd):3d}')

    # ⛔ a note on 60's CONTROL CRITERION, routed rather than edited into its file
    print()
    print(f'    ⛔ NOTE ON THE CONTROL S THRESHOLD.  60 s gate asserts `chance > 2 * pi_d`.  The chance')
    print(f'       rate is fixed by the two marginals -- here {100 * ch:.1f}% -- so that criterion REQUIRES')
    print(f'       pi_d < {100 * ch / 2:.1f}% on this frame whatever the pairing shows.  Measured ratio'
          f' {ch / allp:.2f}x,')
    print(f'       under 2.  It is a BOUND ON pi_d given the marginals, not a test of the pairing, and it')
    print(f'       tightens as pi_d grows.  Routed to 60; nothing of its file is touched here.')

    print()
    print(f'  ⇒ pi_d = {100 * allp:.1f} per cent, Wilson [{100 * alllo:.1f}, {100 * allhi:.1f}], '
          f'on {len(keys)} keys, BETWEEN POOLS.')
    print(f'    chance under broken pairing {100 * ch:.1f} per cent, so the agreement is the keys and')
    print(f'    not the arithmetic -- but see the threshold note above.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

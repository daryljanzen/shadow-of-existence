#!/usr/bin/env python3
r"""read.py -- the arithmetic of r7330's read, against r7328's registered band.

The registration fixed the band before the draw: 37-71 of 80 WITHDRAWN, and declared in terms that
it cannot be failed at any size this frame can sell.  So the figures that carry content here are the
INTERVAL and the distribution of deciding grounds, not the pass.

Three comparisons are computed and each is reported with its interval:
  * this read against r7320's 27 of 40, which was read under the PREVIOUS text;
  * the clustering measured on THIS draw's own outcomes against the 0.327 the registration imported;
  * the reader arm's quantity, pi_d, which this read cannot produce -- stated as a block, not a number.
"""
import collections
import io
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'r7328_60_the_registration'))
sys.path.insert(0, os.path.join(HERE, '..', 'r7326_60_the_draw_designed'))
import size as G                                                       # noqa: E402
import design as D                                                     # noqa: E402

RESULT = os.path.join(HERE, 'RESULT_80.tsv')
BAND_LO, BAND_HI = 37, 71          # registered at r7328 before the draw
DEFF_REG = 1.566                   # registered design effect of the 80-key rotation


def rows():
    out = []
    for l in io.open(RESULT, encoding='utf-8'):
        if l.startswith('#') or not l.strip():
            continue
        c = l.rstrip('\n').split('\t')
        out.append(dict(n=int(c[0]), receipt=c[1], literal=c[2], arm=c[3],
                        outcome=c[4], decided_at=c[5], detail=c[6]))
    return out


def icc_oneway(groups):
    n = sum(len(v) for v in groups)
    k = len(groups)
    if k < 2 or n == k:
        return 0.0
    p = sum(sum(v) for v in groups) / n
    msb = sum(len(v) * (sum(v) / len(v) - p) ** 2 for v in groups) / (k - 1)
    msw = sum(sum((x - sum(v) / len(v)) ** 2 for x in v) for v in groups) / (n - k)
    m0 = (n - sum(len(v) ** 2 for v in groups) / n) / (k - 1)
    den = msb + (m0 - 1) * msw
    return ((msb - msw) / den if den else 0.0), m0


if __name__ == '__main__':
    R = rows()
    out = collections.Counter(r['outcome'] for r in R)
    k = out['WITHDRAWN']
    n = len(R)
    print('── Ⓐ  THE REGISTERED QUANTITY, AGAINST THE BAND FIXED BEFORE THE DRAW ──\n')
    print(f'   {n} keys read:  WITHDRAWN {k}   HELD {out["HELD"]}   MOVED {out["MOVED"]}')
    print(f'   registered band {BAND_LO}-{BAND_HI} of {n}:  '
          f'{"INSIDE" if BAND_LO <= k <= BAND_HI else "OUTSIDE"}')
    lo, hi = G.wilson(k, n)
    print(f'   naive Wilson      {100 * lo:.1f}-{100 * hi:.1f}   (half-width '
          f'±{100 * (hi - lo) / 2:.2f})')
    en = n / DEFF_REG
    clo, chi = G.wilson(k / n * en, en)
    print(f'   clustered at the registered {DEFF_REG}:  {100 * clo:.1f}-{100 * chi:.1f}   '
          f'(half-width ±{100 * (chi - clo) / 2:.2f}, effective n {en:.1f})')
    print(f'   ⇒ the band could not have failed: it spans {BAND_LO}-{BAND_HI} where the whole '
          f'interval this size can resolve is {100 * clo:.1f}-{100 * chi:.1f}')

    print('\n── Ⓑ  THE CLUSTERING, MEASURED ON THIS DRAW\'s OWN OUTCOMES ──\n')
    g = collections.defaultdict(list)
    for r in R:
        g[r['receipt']].append(1 if r['outcome'] == 'WITHDRAWN' else 0)
    groups = list(g.values())
    icc, m0 = icc_oneway(groups)
    deff = 1 + (m0 - 1) * max(icc, 0.0)
    print(f'   {n} keys in {len(groups)} receipts, m0 {m0:.2f}')
    print(f'   ICC of the withdrawal outcome on THIS draw: {icc:+.3f}   design effect {deff:.3f}')
    print(f'   registered, imported from r7320: ICC 0.327, design effect {DEFF_REG}')
    en2 = n / deff
    mlo, mhi = G.wilson(k / n * en2, en2)
    print(f'   on the measured figure: effective n {en2:.1f}, band {100 * mlo:.1f}-{100 * mhi:.1f} '
          f'(half-width ±{100 * (mhi - mlo) / 2:.2f})')
    print(f'   ⇒ the registered cost was conservative by '
          f'{100 * (DEFF_REG / deff - 1):.0f} per cent, and the ICC is the figure that moved')

    print('\n── Ⓒ  AGAINST r7320\'s 27 OF 40, WHICH WAS READ UNDER THE PREVIOUS TEXT ──\n')
    d = 100 * (k / n - 27 / 40)
    nlo, nhi = D.newcombe(k, n, 27, 40)
    print(f'   this read {k}/{n} = {100 * k / n:.1f}%   r7320 {27}/40 = {100 * 27 / 40:.1f}%')
    print(f'   difference {d:+.1f} points, Newcombe {100 * nlo:+.1f} to {100 * nhi:+.1f}')
    print(f'   ⇒ {"NOT distinguishable from zero" if nlo < 0 < nhi else "excludes zero"}: '
          f'reported as a DIRECTION and not as a difference')

    print('\n── Ⓓ  WHAT DECIDED THE ROWS, WHICH IS WHERE THE CONTENT IS ──\n')
    t = collections.Counter(r['decided_at'] for r in R)
    for key in ('Test 1', 'Test 2', 'Test 3', 'Test 4', 'Test 5', 'Test 6', 'Test 7',
                'step 1', 'step 2', 'step 4'):
        if t[key]:
            w = sum(1 for r in R if r['decided_at'] == key and r['outcome'] == 'WITHDRAWN')
            print(f'   {key:8s} {t[key]:3d}   ({w} of them WITHDRAWN)')
    assert sum(t.values()) == n
    withdrawn_by = collections.Counter(r['decided_at'] for r in R if r['outcome'] == 'WITHDRAWN')
    top2 = withdrawn_by.most_common(2)
    print(f'   ⇒ the two heaviest grounds take {sum(c for _, c in top2)} of the {k} withdrawals: '
          f'{top2[0][0]} and {top2[1][0]}')

    print('\n── Ⓔ  THE READER ARM: THE QUANTITY, AND WHY THIS READ CANNOT PRODUCE IT ──\n')
    both = [r for r in R if r['arm'] == 'both']
    print(f'   the registered reader block is the first 52 of the 80: {len(both)} rows carry it')
    print(f'   pi_d requires the SAME key read TWICE by two readers.  This revision is ONE reader, '
          'so the\n   block is read once and its second reading is owed.')
    K_D, N_D = 11, 69
    plo, phi = G.wilson(K_D, N_D)
    m = G.m_reader(phi)
    print(f'   the quantity as r7328 measured it, reported as the arm\'s quantity: '
          f'pi_d {K_D}/{N_D} = {100 * K_D / N_D:.1f}% (Wilson {100 * plo:.1f}-{100 * phi:.1f})')
    print(f'   and the MARGIN beside it, never as one: 70\'s -30.0 (-52.5, -2.9) and cc66\'s '
          '-3.9 (-22.1, +14.8) are\n   differences of rates, not rates of differences')
    print(f'   the size that interval buys stands at {m} paired keys naive, 52 spread on this frame')

    print('\n── Ⓕ  WHICH GROUNDS MOVED BETWEEN THE TWO SAMPLES, EACH WITH ITS INTERVAL ──\n')
    #: r7320's RESULT_40.tsv records the deciding ground in a `Test n -- detail` form; the test
    #: number is read off it rather than retyped, so this comparison cannot drift from that file.
    import re                                                          # noqa: E402
    prev = os.path.join(HERE, '..', 'r7320_60_the_early_era_sampled', 'RESULT_40.tsv')
    pg = collections.Counter()
    pn = 0
    for l in io.open(prev, encoding='utf-8'):
        if l.startswith('#') or not l.strip():
            continue
        c = l.rstrip('\n').split('\t')
        if len(c) < 8:
            continue
        pn += 1
        m = re.match(r'(Test \d|step \d)', c[7])
        if m:
            pg[m.group(1)] += 1
    assert sum(pg.values()) == pn, (
        f'every one of r7320\'s {pn} rows must name a ground; parsed {sum(pg.values())} '
        '-- a silent zero here would turn every comparison below into a fabricated difference')
    print(f'   r7320 read {pn} keys under the previous text;  this read {n} under the standing one')
    print(f'   {"ground":8s} {"r7320":>12s} {"r7330":>12s}   difference, Newcombe')
    for key in ('Test 1', 'Test 2', 'Test 3', 'Test 4', 'Test 5', 'step 1', 'step 2', 'step 4'):
        a, b = t[key], pg[key]
        if not a and not b:
            continue
        dd = 100 * (a / n - b / pn)
        l2, h2 = D.newcombe(a, n, b, pn)
        mark = '  ⛔ EXCLUDES ZERO' if (l2 > 0 or h2 < 0) else ''
        print(f'   {key:8s} {b:5d}/{pn:<6d} {a:5d}/{n:<6d}   {dd:+6.1f}  '
              f'({100 * l2:+.1f} to {100 * h2:+.1f}){mark}')
    print('\n   ⚠ The two samples differ in the RULE TEXT as well as in their keys -- r7320 read the')
    print('     second redraft and this read the third -- so a ground that moves is confounded and is')
    print('     reported as a ground that moved, not as an effect of either.')

    print('\n── Ⓖ  THE CROSS-SEAT CHECK, AND WHAT THE ONE DISAGREEMENT CAN AND CANNOT MOVE ──\n')
    BLIND = (('70\'s pool', os.path.join(HERE, '..', 'r7315_70_redraft3_score',
                                         'APPLICATION_70_blind.tsv')),
             ('71', os.path.join(HERE, '..', 'r7321_71_redraft3_blind',
                                 'BLIND_READ_71_redraft3.tsv')))
    mine = {(r['receipt'], r['literal']): r for r in R}
    for nm, p in BLIND:
        S = {}
        for l in io.open(p, encoding='utf-8'):
            if l.startswith('#') or not l.strip():
                continue
            c = l.rstrip('\n').split('\t')
            if c[0] == 'receipt':
                continue
            S[(c[0], c[1])] = c[3].strip()
        ov = [kk for kk in mine if kk in S]
        print(f'   {nm}: {len(ov)} of the {n} keys were also read blind under this same text')
        for kk in ov:
            r = mine[kk]
            theirs = S[kk]
            agree_outcome = (r['outcome'] == 'WITHDRAWN') == (theirs == 'REPAIR-OWED')
            #: the registered mapping, fixed at r7320: DELIBERATE -> HELD, MEANING-HELD -> MOVED.
            mapped = {'REPAIR-OWED': 'WITHDRAWN', 'DELIBERATE': 'HELD'}.get(theirs, 'MOVED')
            agree_four = mapped == r['outcome']
            print(f'      {kk[0].split("/")[-1][:40]}…  mine {r["outcome"]}/{r["decided_at"]}  '
                  f'theirs {theirs}  -- registered quantity '
                  f'{"AGREES" if agree_outcome else "DIFFERS"}, '
                  f'four-way verdict {"AGREES" if agree_four else "DIFFERS"}')
    #: the one disagreement is DELIBERATE (step 2's third bullet) against MEANING-HELD (step 4's
    #: first bullet).  Both reach a complete clause carrying a says-claim and only the decision
    #: order separates them.  What that costs the registered quantity is computed, not asserted:
    _exposed = [r for r in R if r['outcome'] == 'HELD'
                and ('whole' in r['detail'].lower() or 'headline' in r['detail'].lower())]
    print(f'\n   HELD rows sitting on that same boundary: {len(_exposed)} of {out["HELD"]}')
    print(f'   if every one of them were taken at step 4 instead, the counts would read '
          f'WITHDRAWN {k}, HELD {out["HELD"] - len(_exposed)}, MOVED {out["MOVED"] + len(_exposed)}')
    print(f'   ⇒ THE REGISTERED QUANTITY IS UNCHANGED at {k}: the ambiguity two independent readers '
          'actually\n     exercised moves rows between the two NON-registered outcomes and cannot '
          'reach the band')

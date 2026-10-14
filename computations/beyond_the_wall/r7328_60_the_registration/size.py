#!/usr/bin/env python3
r"""size.py -- both arms priced against what the frame can actually supply, and the reader arm's
input MEASURED rather than borrowed.

r7326 sized the reader arm off "70's observed 30 per cent discordance" and the sampling arm off a
design effect of 1.44 held fixed.  Both inputs are wrong in a way this file demonstrates:

  * the 30.0 is a MARGIN -- a difference between two readers' owed RATES on a crossover -- and the
    size formula wants pi_d, the probability that a key's two readings DISAGREE.  No instrument in
    the campaign had reported pi_d.  It is recoverable, because two reader pools applied the same
    text to the same keys and filed both reads raw: 40 keys under the previous text and 69 under the
    third redraft.  Measured here for the first time.

  * the design effect is not a constant.  On a frame with a FIXED number of receipts, every key
    added to a draw enlarges the clusters, so deff = 1 + (m0(n) - 1) * ICC rises with n and the
    interval closes far slower than root-n.  Priced against the frame's real capacity, the three
    half-widths r7326 tabulated cannot be bought at any price.

Nothing here reads a key or produces a verdict.
"""
import collections
import hashlib
import io
import math
import os
import re

Z95 = 1.959963985
ICC = 0.327            # r7326's measured intra-receipt correlation of the withdrawal outcome
CENTRE = 0.675         # r7320's observed withdrawal rate, the centre the bands are priced at
BOUND = 0.153          # the reader difference the arm must bound, r7299's own figure
SALT = '6bef6fd5acf0692299f306c96e2ee630542dac14'
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))

# the two paired reader sets: the same keys, the same text, two pools, filed raw and never reconciled
PAIRED = [
    ('the crossover, previous text at 6bef6fd5',
     'computations/beyond_the_wall/r7315_70_redraft3_score/CROSSOVER_70_prev_text.tsv',
     'computations/beyond_the_wall/r7321_71_redraft3_blind/BLIND_READ_71_crossover.tsv'),
    ('the held set, third redraft at 1a3c13a6',
     'computations/beyond_the_wall/r7315_70_redraft3_score/APPLICATION_70_blind.tsv',
     'computations/beyond_the_wall/r7321_71_redraft3_blind/BLIND_READ_71_redraft3.tsv'),
]


def wilson(k, n, z=Z95):
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (c - h) / d, (c + h) / d


def read_tsv(rel):
    """the raw read files, keyed on (receipt, literal) -- the only join these files share."""
    out, hdr = {}, None
    for l in io.open(os.path.join(ROOT, rel), encoding='utf-8'):
        if not l.strip() or l.startswith('#'):
            continue
        c = l.rstrip('\n').split('\t')
        if c[0] == 'receipt':
            hdr = c
            continue
        out[(c[0], c[1])] = c
    return out, hdr


def discordance(rel_a, rel_b):
    """pi_d: of the keys BOTH pools read, the share whose two verdicts differ.

    Column 4 is the verdict in both formats.  A key one pool left UNDECIDED and the other decided is
    counted DISCORDANT -- the two readings differ, which is what the size formula is about -- and the
    both-decided figure is reported beside it rather than substituted for it.
    """
    A, hdr = read_tsv(rel_a)
    B, _ = read_tsv(rel_b)
    keys = [k for k in A if k in B]
    disc = [k for k in keys if A[k][3].strip() != B[k][3].strip()]
    dec = [k for k in keys if 'UNDECIDED' not in (A[k][3].strip(), B[k][3].strip())]
    return keys, disc, dec, [k for k in dec if A[k][3].strip() != B[k][3].strip()], A, hdr


def icc_oneway(groups):
    """the one-way random-effects ICC on a binary outcome, unequal cluster sizes (r7326's)."""
    n = sum(len(v) for v in groups)
    k = len(groups)
    if k < 2 or n == k:
        return 0.0
    p = sum(sum(v) for v in groups) / n
    msb = sum(len(v) * (sum(v) / len(v) - p) ** 2 for v in groups) / (k - 1)
    msw = sum(sum((x - sum(v) / len(v)) ** 2 for x in v) for v in groups) / (n - k)
    m0 = (n - sum(len(v) ** 2 for v in groups) / n) / (k - 1)
    den = msb + (m0 - 1) * msw
    return (msb - msw) / den if den else 0.0


def seat(w):
    for s in ('+60', '+69', '+70', 'cc66', '+66', '+71'):
        if s in (w or ''):
            return s.lstrip('+')
    return '?'


def rev(w):
    m = re.match(r'r(\d{4})', w or '')
    return int(m.group(1)) if m else None


def frame():
    """this seat's own pre-r7260 DELIBERATE rows -- r7319's standing frame, r7320's population."""
    rows = []
    for l in io.open(os.path.join(ROOT, 'corpus', 'quote_pin_baseline.tsv'), encoding='utf-8'):
        c = l.rstrip('\n').split('\t')
        if len(c) >= 7 and c[0].startswith('receipts/'):
            rows.append(c)
    return [c for c in rows
            if c[5] == 'DELIBERATE' and seat(c[6]) == '60' and (rev(c[6]) or 99999) < 7260]


def drawn_at_r7320(pop, size=40):
    keyed = sorted(pop, key=lambda c: hashlib.sha256(
        (SALT + c[0] + '\t' + c[1]).encode('utf-8')).hexdigest())
    return {(c[0], c[1]) for c in keyed[:size]}


def spread(caps, n):
    """n keys allocated over the receipts as EVENLY as their capacities allow.

    This is the best a draw can do on this frame: the flattest allocation minimises m0 and so
    minimises the design effect.  It is an upper bound on what any draw of n keys buys.
    """
    caps = sorted(caps, reverse=True)
    alloc = [0] * len(caps)
    left = n
    while left > 0:
        moved = False
        for i in range(len(caps)):
            if left and alloc[i] < caps[i]:
                alloc[i] += 1
                left -= 1
                moved = True
        if not moved:
            break
    return [a for a in alloc if a]


def deff_of(sizes, icc=ICC):
    """deff = 1 + (m0 - 1) * ICC, with m0 the ICC's own cluster-size weighting."""
    n = sum(sizes)
    k = len(sizes)
    m0 = (n - sum(s * s for s in sizes) / n) / (k - 1) if k > 1 else 1.0
    return 1 + (m0 - 1) * icc, m0


def wilson_halfwidth(n, deff, p=CENTRE):
    en = n / deff
    lo, hi = wilson(p * en, en)
    return 100 * (hi - lo) / 2, 100 * lo, 100 * hi


def m_reader(pi_d, bound=BOUND, deff=1.0, z=Z95):
    """paired keys to bound a reader difference of `bound`: m = z^2 * pi_d / bound^2."""
    return math.ceil(z * z * pi_d / (bound * bound) * deff)


if __name__ == '__main__':
    print('── Ⓐ  THE READER ARM\'s INPUT, MEASURED INSTEAD OF BORROWED ──\n')
    measured = {}
    for name, fa, fb in PAIRED:
        keys, disc, dec, discdec, A, hdr = discordance(fa, fb)
        lo, hi = wilson(len(disc), len(keys))
        g = collections.defaultdict(list)
        for k in keys:
            g[k[0]].append(1 if k in set(disc) else 0)
        print(f'{name}')
        print(f'   {len(keys)} keys read by BOTH pools;  discordant {len(disc)}  '
              f'= {100 * len(disc) / len(keys):.1f}%   Wilson {100 * lo:.1f}–{100 * hi:.1f}')
        print(f'   both pools decided {len(dec)}:  discordant {len(discdec)} '
              f'= {100 * len(discdec) / len(dec):.1f}%')
        print(f'   {len(g)} receipts, {len(keys) / len(g):.2f} keys each;  '
              f'ICC of the discordance {icc_oneway(list(g.values())):+.3f}')
        if hdr and 'seen' in hdr:
            si = hdr.index('seen')
            for lab in ('seen', 'unseen'):
                kk = [k for k in keys
                      if A[k][si].lower().startswith('yes') == (lab == 'seen')]
                if kk:
                    d2 = sum(1 for k in kk if k in set(disc))
                    l2, h2 = wilson(d2, len(kk))
                    print(f'     {lab:6s} {d2:2d}/{len(kk):2d} = {100 * d2 / len(kk):4.1f}%  '
                          f'Wilson {100 * l2:.1f}–{100 * h2:.1f}')
        measured[name] = (len(disc), len(keys), lo, hi)
        print()

    pop = frame()
    read40 = drawn_at_r7320(pop)
    rest = [c for c in pop if (c[0], c[1]) not in read40]
    caps_all = list(collections.Counter(c[0] for c in pop).values())
    caps_rest = list(collections.Counter(c[0] for c in rest).values())
    print('── Ⓑ  WHAT THE FRAME CAN SUPPLY ──\n')
    print(f'the frame: {len(pop)} DELIBERATE keys in {len(caps_all)} receipts, '
          f'{len(pop) / len(caps_all):.2f} each, the heaviest {max(caps_all)}')
    print(f'r7320 read {len(read40)} of them, leaving {len(rest)} in {len(caps_rest)} receipts\n')
    print('  the SAMPLING arm, priced on the remaining keys and the BEST spread of each size:')
    for n in (33, 40, 60, 80, 100, 128):
        s = spread(caps_rest, n)
        if sum(s) < n:
            print(f'   {n:4d}: the frame holds only {sum(s)}')
            continue
        de, m0 = deff_of(s)
        hw, lo, hi = wilson_halfwidth(n, de)
        print(f'   {n:4d} keys in {len(s):2d} receipts   m0 {m0:4.2f}   deff {de:5.3f}   '
              f'effective n {n / de:5.1f}   band {lo:4.1f}–{hi:4.1f}   half-width ±{hw:5.2f}')
    print()
    for hw_want in (0.10, 0.075, 0.05):
        buy = None
        for n in range(10, len(rest) + 1):
            s = spread(caps_rest, n)
            if sum(s) < n:
                break
            de, _ = deff_of(s)
            if wilson_halfwidth(n, de)[0] / 100 <= hw_want:
                buy = n
                break
        s = spread(caps_rest, len(rest))
        de, _ = deff_of(s)
        best = wilson_halfwidth(len(rest), de)[0]
        print(f'   ±{100 * hw_want:4.1f} points, r7326 ③ priced it at '
              f'{ {0.10: 122, 0.075: 217, 0.05: 487}[hw_want]:3d} keys: '
              + (f'{buy} keys' if buy else
                 f'NOT PURCHASABLE — every remaining key buys ±{best:.2f}'))
    s_all = spread(caps_all, len(pop))
    de_all, _ = deff_of(s_all)
    print(f'   and the WHOLE population, drawn as well as it can be drawn: '
          f'±{wilson_halfwidth(len(pop), de_all)[0]:.2f} points')
    print()
    de_actual = 1.44
    print(f'   r7320\'s own 40 lay in 17 receipts (deff {de_actual}): '
          f'±{wilson_halfwidth(40, de_actual)[0]:.2f};  the same 40 spread over all '
          f'{len(caps_all)}: ±{wilson_halfwidth(40, deff_of(spread(caps_all, 40))[0])[0]:.2f}')
    print()
    print('── Ⓒ  THE READER ARM, SIZED FROM THE MEASURED FIGURE ──\n')
    K_D, N_D, PI_LO, PI_HI = measured['the held set, third redraft at 1a3c13a6']
    for lab, pd in (('the measured point', K_D / N_D), ('its upper Wilson bound', PI_HI),
                    ('its lower Wilson bound', PI_LO), ('r7326\'s borrowed 30%', 0.300)):
        m = m_reader(pd)
        s = spread(caps_rest, m)
        de = deff_of(s)[0] if sum(s) == m else float('nan')
        print(f'   {lab:24s} π_d {100 * pd:5.1f}%:  {m:3d} paired keys, '
              f'{math.ceil(m * de):3d} once spread on this frame (deff {de:5.3f})')

    print()
    print('── Ⓓ  THE TWO REGISTERED BANDS, COMPUTED BEFORE THE DRAW ──\n')
    SAMPLING_N, READER_M = 80, 52
    s = spread(caps_rest, SAMPLING_N)
    de = deff_of(s)[0]
    hw, lo, hi = wilson_halfwidth(SAMPLING_N, de)
    print(f'   the SAMPLING arm, {SAMPLING_N} keys: deff {de:.3f}, effective n {SAMPLING_N / de:.1f}, '
          f'half-width ±{hw:.2f}, band at the r7320 centre {lo:.1f}–{hi:.1f}')
    sd_new = math.sqrt(CENTRE * (1 - CENTRE) / (SAMPLING_N / de))
    sd_old = (16.46 / 100) / Z95
    sd_rep = math.sqrt(sd_new ** 2 + sd_old ** 2)
    print(f'      a REPLICATION band must carry r7320\'s own error too: '
          f'sd {100 * sd_new:.2f} (new) ⊕ {100 * sd_old:.2f} (r7320\'s 40) = {100 * sd_rep:.2f}')
    print(f'      ⇒ the registered replication band is '
          f'{100 * (CENTRE - Z95 * sd_rep):.1f}–{100 * (CENTRE + Z95 * sd_rep):.1f} '
          f'(±{100 * Z95 * sd_rep:.1f} points), i.e. '
          f'{math.floor(SAMPLING_N * (CENTRE - Z95 * sd_rep)):d}–'
          f'{math.ceil(SAMPLING_N * (CENTRE + Z95 * sd_rep)):d} of {SAMPLING_N} WITHDRAWN')
    print(f'      ⛔ δ against h: this band cannot be failed by any size this frame can sell — '
          f'U-FAIL, and it is stated as one')
    print()
    for lab, pd in (('at the conservative π_d', PI_HI), ('at the measured π_d', K_D / N_D)):
        h_reader = 100 * Z95 * math.sqrt(pd / READER_M)
        print(f'   the READER arm, {READER_M} paired keys {lab} ({100 * pd:.1f}%): '
              f'half-width ±{h_reader:.1f} points on the two readers\' margin')
        print(f'      δ = {100 * BOUND:.1f} (r7299\'s figure) against h = {h_reader:.1f} ⇒ '
              f'{"RESOLVABLE" if 100 * BOUND > h_reader else "U-FAIL"}')

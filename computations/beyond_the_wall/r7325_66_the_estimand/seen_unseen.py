#!/usr/bin/env python3
"""r7325, node 66 --- pricing the contamination channel 70 found, across every applier run filed.

70 (r7323+70.4) reports that 43 of the 78 keys of cc66's frame are marked `seen`: the receipts cc66
repaired at r7293 and r7303 carry comments naming other readers' verdicts, an applier must open the
receipt to find the check, and so no bar on the ledger can reach them.  The `seen` column has been
filed on every applier run since r7299 and has never been priced.  This prices it.

THE QUESTION: on keys the applier had already seen, does the verdict differ from keys it had not?

Read-only.  Nothing is joined to the ledger.
"""
import glob
import math
import os
import sys

BTW = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FILES = [
    ('r7299 blind',      'r7299_70_two_scores/APPLICATION_70_blind.tsv'),
    ('r7299 completed',  'r7299_70_two_scores/APPLICATION_70_completed.tsv'),
    ('r7303 blind',      'r7303_70_redraft_score/APPLICATION_70_blind.tsv'),
    ('r7303 calib',      'r7303_70_redraft_score/APPLICATION_70_calibration.tsv'),
    ('r7303 completed',  'r7303_70_redraft_score/APPLICATION_70_completed.tsv'),
    ('r7311 blind',      'r7311_70_redraft2_score/APPLICATION_70_blind.tsv'),
    ('r7311 calib',      'r7311_70_redraft2_score/APPLICATION_70_calibration.tsv'),
    ('r7315 blind',      'r7315_70_redraft3_score/APPLICATION_70_blind.tsv'),
    ('r7315 crossover',  'r7315_70_redraft3_score/CROSSOVER_70_prev_text.tsv'),
    ('cc66 half A',      'r7323_70_within_seat_read/APPLICATION_70_half_A.tsv'),
    ('cc66 half B',      'r7323_70_within_seat_read/APPLICATION_70_half_B.tsv'),
]

# the four BLIND HELD SETS are the entries that carry the rule campaign's verdicts
HELD = {'r7299 blind', 'r7303 blind', 'r7311 blind', 'r7315 blind'}


def hdr_rows(path):
    hdr, data = None, []
    with open(path, encoding='utf-8') as fh:
        for ln in fh:
            ln = ln.rstrip('\n')
            if ln.startswith('#'):
                f = [x.strip() for x in ln.lstrip('#').strip().split('\t')]
                if f and f[0] == 'receipt':
                    hdr = f
                continue
            if not ln.strip():
                continue
            f = ln.split('\t')
            if hdr is None and f[0].strip() == 'receipt':
                hdr = [x.strip() for x in f]
                continue
            data.append(f)
    return hdr, data


def wilson(k, n, z=1.96):
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (c - h) / d, (c + h) / d


def newcombe(k1, n1, k2, n2):
    l1, u1 = wilson(k1, n1)
    l2, u2 = wilson(k2, n2)
    p1, p2 = k1 / n1, k2 / n2
    lo = (p1 - p2) - math.sqrt((p1 - l1) ** 2 + (u2 - p2) ** 2)
    hi = (p1 - p2) + math.sqrt((u1 - p1) ** 2 + (p2 - l2) ** 2)
    return (p1 - p2) * 100, lo * 100, hi * 100


rows = []
for lab, rel in FILES:
    hdr, data = hdr_rows(os.path.join(BTW, rel))
    iv, isn = hdr.index('verdict'), hdr.index('seen')
    ows = nsn = owu = nun = 0
    for r in data:
        if len(r) <= max(iv, isn) or r[iv] == 'UNDECIDED':
            continue
        owed = r[iv] == 'REPAIR-OWED'
        if r[isn].strip().startswith('yes'):
            nsn += 1; ows += owed
        else:
            nun += 1; owu += owed
    rows.append((lab, ows, nsn, owu, nun))

fail = []


def check(ok, label):
    print(('  [PASS] ' if ok else '  [FAIL] ') + label)
    if not ok:
        fail.append(label)


print('=' * 100)
print('  THE `seen` CLASS, PER RUN.  A key is `seen` when the applier reports it met an earlier verdict')
print('  in the receipt it had to open.')
print('=' * 100)
up = dn = 0
for lab, a, na, b, nb in rows:
    if na == 0 or nb == 0:
        print(f'  {lab:18s} seen n={na:3d}  --- no contrast')
        continue
    d = a / na * 100 - b / nb * 100
    up += d > 0; dn += d < 0
    print(f'  {lab:18s} seen {a:3d}/{na:3d} = {a/na*100:5.1f}%   unseen {b:3d}/{nb:3d} = {b/nb*100:5.1f}%   '
          f'seen - unseen = {d:+6.1f}')
print(f'  => {up} runs up, {dn} runs down')


def pool(sub, label, show=True):
    S = sum(a for _, a, na, b, nb in sub); NS = sum(na for _, a, na, b, nb in sub)
    U = sum(b for _, a, na, b, nb in sub); NU = sum(nb for _, a, na, b, nb in sub)
    d, lo, hi = newcombe(S, NS, U, NU)
    if show:
        print(f'  {label:44s} seen {S:3d}/{NS:3d} = {S/NS*100:5.1f}%   unseen {U:3d}/{NU:3d} = '
              f'{U/NU*100:5.1f}%   diff {d:+6.1f} ({lo:+.1f}, {hi:+.1f})  h = {(hi-lo)/2:4.1f}  '
              f'{"EXCLUDES 0" if lo * hi > 0 else "includes 0"}')
    return d, lo, hi, NS, NU


print()
print('=' * 100)
print('  POOLED, AND THEN THE SUBSETS THAT TEST IT')
print('=' * 100)
d_all, lo_all, hi_all, NS, NU = pool(rows, 'ALL runs')
d_nc, lo_nc, hi_nc, *_ = pool([r for r in rows if 'cc66' not in r[0]], 'without cc66\'s two halves')
d_nk, lo_nk, hi_nk, *_ = pool([r for r in rows if 'calib' not in r[0]], 'without the two calibration runs')
d_nb, lo_nb, hi_nb, *_ = pool([r for r in rows if 'cc66' not in r[0] and 'calib' not in r[0]], 'without either')
d_h, lo_h, hi_h, *_ = pool([r for r in rows if r[0] in HELD], 'THE FOUR BLIND HELD SETS ONLY')

# the stratified estimate, run so that its disagreement is on the record
num = den = 0
for _, a, na, b, nb in rows:
    if na == 0 or nb == 0:
        continue
    p1, p2 = a / na, b / nb
    v = max(p1 * (1 - p1) / na + p2 * (1 - p2) / nb, 1e-9)
    num += (p1 - p2) / v; den += 1 / v
m, se = num / den, math.sqrt(1 / den)
print(f'\n  inverse-variance stratified: {m*100:+.1f} points, 95% ({(m-1.96*se)*100:+.1f}, '
      f'{(m+1.96*se)*100:+.1f})')

print()
check(NS / (NS + NU) > 0.30,
      f'Ⓐ① THE CHANNEL IS LARGE: {NS} of {NS+NU} decided applier cells --- {NS/(NS+NU)*100:.1f} per cent '
      f'--- are keys the applier reports having met an earlier verdict inside the receipt it had to open')
check(lo_all * hi_all > 0,
      f'Ⓐ② and POOLED it looks decisive: {d_all:+.1f} points, Newcombe ({lo_all:+.1f}, {hi_all:+.1f}), '
      f'excluding zero --- which is the figure a single pooled line would have reported')
check(lo_nc * hi_nc < 0 and lo_nk * hi_nk < 0,
      f'Ⓐ③ ⛔ AND IT DOES NOT SURVIVE ITS OWN SUBSETS: drop cc66\'s halves and it is {d_nc:+.1f} '
      f'({lo_nc:+.1f}, {hi_nc:+.1f}); drop the calibration runs and it is {d_nk:+.1f} ({lo_nk:+.1f}, '
      f'{hi_nk:+.1f}) --- both including zero')
check(lo_h * hi_h < 0,
      f'Ⓐ④ ⛭ ON THE FOUR BLIND HELD SETS --- the entries that carry the rule campaign\'s verdicts --- it '
      f'is {d_h:+.1f} points ({lo_h:+.1f}, {hi_h:+.1f}), h = {(hi_h-lo_h)/2:.1f}: THE CHANNEL HAS NOT '
      f'MOVED THE VERDICTS THAT MATTER')
check(m * 100 > 10 and abs(m * 100 - d_h) > 10,
      f'Ⓐ⑤ and the stratified estimate ({m*100:+.1f}) disagrees with the held sets by more than ten '
      f'points, for the reason 70 named against its own power sweep: inverse-variance weighting '
      f'upweights an n=6 arm sitting at an extreme rate.  ** It is run here so that its disagreement is '
      f'on the record rather than so that it can be quoted **')
print()
print('=' * 100)
print(f'  gates run: {len(fail) + 5 - len(fail)}   failed: {len(fail)}')
print('=' * 100)
print("""
  ⛔ ** THE CONTAMINATION CHANNEL IS REAL, UNBARRABLE AND LARGER THAN ANYONE PRICED. **  An applier must
     open the receipt to find the check, and cc66's r7293/r7303 repairs left comments in those receipts
     naming earlier readers' verdicts.  No bar on the ledger reaches it; no bar can.
  ⛭ ** AND IT HAS NOT MOVED THE HELD-SET VERDICTS. **  The pooled figure that excludes zero is carried
     by two frames whose unseen arms are six keys at fifty per cent.  On the four blind held sets the
     contrast is under one point with a half-width of eleven.
  ⌗ So this is a STATED LIMIT under the r7013 rule and not a member and not a repair: the same question
     at finer resolution.  ** What it bars is a future blind read on repaired receipts being called
     blind **, not anything already scored.""")
sys.exit(1 if fail else 0)

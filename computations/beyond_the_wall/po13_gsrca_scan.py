#!/usr/bin/env python3
"""GSRCA continuous scan: does ANY source factor land position, amplitude AND parity together?
For each alpha: l1/l_A (position), P1/P2, P1/P3 (amplitude), positional parity ALT q1-3.
Report the table, then the alpha at which each observable crosses the sky, and whether they coincide."""
import sys, glob, re, numpy as np
from scipy.signal import argrelextrema

SD = sys.argv[1] if len(sys.argv) > 1 else '.'
SKY = dict(pos=0.7312, p12=2.217, p13=2.277, parity=0.028)
SKY3 = np.array([220.6, 538.1, 809.8]); E3 = np.array([0.6, 1.3, 1.0])


def peaks_sub(ls, Dl, n=6):
    idx = argrelextrema(Dl, np.greater, order=3)[0][:n]; pos = []; ht = []
    for i in idx:
        y0, y1, y2 = Dl[i-1], Dl[i], Dl[i+1]; den = y0 - 2*y1 + y2
        dx = 0.5*(y0-y2)/den if den else 0.0
        pos.append(float(ls[i] + dx*(ls[i+1]-ls[i]))); ht.append(float(y1 - 0.25*(y0-y2)*dx))
    return np.array(pos), np.array(ht)


def alt3(p):
    n = np.arange(1, len(p)+1); A, B = np.polyfit(n, p, 1); return abs(float(np.mean((-1.)**n*(p-(A*n+B))/A)))


MAP = 135.46 / 105.36   # r_stack/r_leaf projection factor (uniform stretch; moves POSITION only)


def measure(f):
    d = np.load(f); ls, Dl, lA = d['ls'], d['Dl'], float(d['l_A'])
    pos, ht = peaks_sub(ls, Dl)
    # position mapped to the phenomenological ruler; heights & parity are map-invariant
    return dict(lA=lA, pos1=pos[0]/lA*MAP, p12=ht[0]/ht[1], p13=ht[0]/ht[2], parity=alt3(pos[:3]))


rows = []
for f in sorted(glob.glob(f"{SD}/cr_a*.npz")):
    a = float(re.search(r'cr_a([0-9.]+)\.npz', f).group(1))
    try:
        m = measure(f); m['a'] = a; rows.append(m)
    except Exception as e:
        print(f"  a={a}: {e}")
rows.sort(key=lambda r: r['a'])
if not rows:
    print("no scan files yet"); sys.exit(0)

print("=" * 78)
print("  GSRCA SCAN -- does one source factor land position, amplitude AND parity?")
print("=" * 78)
print(f"  {'alpha':>6}{'l1/lA':>9}{'P1/P2':>9}{'P1/P3':>9}{'parity':>9}")
for r in rows:
    print(f"  {r['a']:>6.2f}{r['pos1']:>9.4f}{r['p12']:>9.3f}{r['p13']:>9.3f}{r['parity']:>9.3f}")
print(f"  {'SKY':>6}{SKY['pos']:>9.4f}{SKY['p12']:>9.3f}{SKY['p13']:>9.3f}{SKY['parity']:>9.3f}")
print()


def cross(key, target):
    xs = np.array([r['a'] for r in rows]); ys = np.array([r[key] for r in rows])
    hits = []
    for i in range(len(xs)-1):
        if (ys[i]-target)*(ys[i+1]-target) <= 0 and ys[i] != ys[i+1]:
            hits.append(xs[i] + (target-ys[i])*(xs[i+1]-xs[i])/(ys[i+1]-ys[i]))
    return hits


print("  alpha where each observable crosses the sky:")
for key, nm in (('pos1', 'position'), ('p12', 'P1/P2'), ('p13', 'P1/P3'), ('parity', 'parity')):
    print(f"    {nm:9s} sky={SKY[{'pos1':'pos','p12':'p12','p13':'p13','parity':'parity'}[key]]}: "
          f"crosses at alpha = {[round(x,3) for x in cross(key, SKY[{'pos1':'pos','p12':'p12','p13':'p13','parity':'parity'}[key]])]}")
print()
print("  If all four crossing-alphas coincide -> that alpha is a PREDICTION to explain.")
print("  If position wants one value and amplitude another -> source norm is NOT the free direction.")

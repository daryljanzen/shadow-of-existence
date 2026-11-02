#!/usr/bin/env python3
"""r7656+60.3 (60) -- THE MATCHER'S OWN REACH, measured before its 95-of-95 is reported.

⛔ THE PROBLEM, STATED BEFORE IT WAS MEASURED.  `cold_check.py` searches ONE HUNDRED receipts' stdout
for any number within half a unit of the target's last printed digit.  For a two-significant-digit
figure the chance that SOME number in a hundred outputs lands inside that window is high WHATEVER THE
CORPUS SAYS -- so a 95-of-95 is exactly what a matcher with no discriminating power returns.

⌗ *A guard that cannot fail on the data it is given is not a guard.  The way to find out is a negative
control, not a re-reading.*

TWO CONTROLS, both registered at `+60.3` before this file existed:
  ⑪⑫⑬  DECOYS -- every real figure moved WELL OUTSIDE its own tolerance, magnitude and digit count
        kept, run through the SAME matcher against the SAME bank.  Threshold fixed in advance: a decoy
        rate above 20% means the matcher is the result and not the corpus.
  ⑭     MULTIPLICITY -- how many of the hundred receipts produce each figure independently.  One is a
        located figure; forty is a coincidence of the window.
"""
import json
import os
import statistics
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RUNS = os.path.join(HERE, 'runs')
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
import check_figures_pinned as G                                           # noqa: E402

_fail = []


def check(label, ok):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    if not ok:
        _fail.append(label)


S = json.load(open(os.path.join(HERE, 'sites.json')))
SITES, CANDS = S['sites'], S['candidates']
STATE = {r['receipt']: r['state'] for r in json.load(open(os.path.join(HERE, 'runs.json')))}
RAN = [n for n in CANDS if STATE.get(n) == 'RAN']

OUTFIGS = {}
for name in CANDS:
    p = os.path.join(RUNS, name[:120] + '.txt')
    txt = open(p, encoding='utf-8', errors='replace').read() if os.path.exists(p) else ''
    OUTFIGS[name] = {s for s, _ in G.figures(txt)}


def allow(s):
    dec = len(s.split('.')[1]) if '.' in s else 0
    half = 0.5 * 10 ** (-dec)
    try:
        return max(half, 0.0005 * abs(float(s)))
    except ValueError:
        return half


def hits(fig):
    """which receipts that RAN produce this figure, through the same rule cold_check uses"""
    try:
        want, tol = float(fig), allow(fig)
    except ValueError:
        return []
    out = []
    for n in RAN:
        if fig in OUTFIGS[n]:
            out.append(n)
            continue
        for s in OUTFIGS[n]:
            try:
                if abs(float(s) - want) <= tol:
                    out.append(n)
                    break
            except ValueError:
                continue
    return out


def decoy(fig):
    """move it WELL outside its own tolerance, keeping magnitude and digit count.

    ⌗ The shift is 40 times the figure's own allowance -- far outside any rounding reading of it --
    and the decoy is re-rendered with the SAME number of decimals, so it is a figure of exactly the
    shape of a real one that the corpus should not carry at that site.
    """
    try:
        x = float(fig)
    except ValueError:
        return None
    dec = len(fig.split('.')[1]) if '.' in fig else 0
    d = x + 40.0 * allow(fig)
    s = f"{d:.{dec}f}"
    return None if s == fig else s


print(__doc__)
print("=" * 112)
print("  r7656+60.3 -- the matcher's reach: decoys and multiplicity")
print("=" * 112)

FIGS = [f for s in SITES for f in s['figures']]
print(f"\n  {len(FIGS)} real figure(s) over {len(RAN)} receipt(s) that ran")

# ---------------------------------------------------------------- ⑭ multiplicity
mult = {f: len(hits(f)) for f in sorted(set(FIGS))}
per = [mult[f] for f in FIGS]
med = statistics.median(per)
print(f"\nⓐ  ⑭ MULTIPLICITY -- how many of the {len(RAN)} receipts produce each figure independently")
print(f"      median {med:.0f}   mean {statistics.mean(per):.1f}   min {min(per)}   max {max(per)}")
_one = [f for f in sorted(set(FIGS)) if mult[f] == 1]
_many = [f for f in sorted(set(FIGS)) if mult[f] >= 20]
print(f"      produced by exactly ONE receipt: {len(_one)} distinct figure(s)  {_one[:10]}")
print(f"      produced by TWENTY OR MORE:      {len(_many)} distinct figure(s)  {_many[:10]}")

# ---------------------------------------------------------------- ⑪⑫⑬ decoys
print(f"\nⓑ  ⑪ DECOYS -- each real figure moved 40x its own allowance, same digit count")
dec_rows = []
for f in FIGS:
    d = decoy(f)
    if d is None:
        continue
    dec_rows.append((f, d, len(hits(d))))
nd = len(dec_rows)
nhit = sum(1 for _f, _d, h in dec_rows if h > 0)
rate = nhit / nd if nd else 0.0
print(f"      {nd} decoy(s) built; {nhit} of them ALSO 'reproduce' -> false-positive rate "
      f"{rate*100:.1f}%")
print(f"\n      {'real':>10} {'decoy':>10} {'receipts hit':>13}")
for f, d, h in dec_rows[:14]:
    print(f"      {f:>10} {d:>10} {h:>13}")
if nd > 14:
    print(f"      ... and {nd-14} more")

print(f"""
  ⌗ ⑬ THE RATE IS PUBLISHED EITHER WAY, with the decoys themselves, because a cold check that
  reported its hit rate without its false-positive rate would be asking to be believed rather than
  checked.""")

check(f"⑫ THE REGISTERED THRESHOLD -- the decoy rate is at or below 20% ({rate*100:.1f}%), so the "
      f"95-of-95 is a statement about the corpus and not about the width of this matcher's window",
      rate <= 0.20)
check(f"⑭ and the median figure is produced by a SMALL number of the {len(RAN)} receipts "
      f"({med:.0f}), so a reproduction locates a figure rather than finding it everywhere",
      med <= 10)

print("\n" + "=" * 112)
print(f"  {len(_fail)} failure(s)")
for f in _fail:
    print("   [FAIL] " + f)
json.dump(dict(decoys=nd, decoy_hits=nhit, decoy_rate=round(rate, 4),
               median_multiplicity=med, mean_multiplicity=round(statistics.mean(per), 2),
               one_receipt_only=_one, twenty_or_more=_many,
               rows=[dict(real=f, decoy=d, hits=h) for f, d, h in dec_rows]),
          open(os.path.join(HERE, 'controls.json'), 'w'), indent=1)
sys.exit(1 if len(_fail) > 0 else 0)

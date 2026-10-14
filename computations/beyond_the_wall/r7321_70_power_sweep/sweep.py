#!/usr/bin/env python3
"""r7321+70: the power sweep, by PREDICTION.md in this directory.

    python3 sweep.py            # reads ENTRIES.tsv beside this file, writes TABLE.tsv and prints the classes

ENTRIES.tsv: one row per registered entry (file, entry_id, quantity, kind, central, band_lo, band_hi, line, scored_k,
scored_n, arm2_k, arm2_n, observed, outcome, outcome_source, keys, receipts, notes, + the sweep's own columns
effect_basis and h_override).  Percent fields are in points (0-100).

kind rate_vs_line : h = Wilson half-width at scored_k/scored_n; delta = central - line; n80 one-sample from the line.
kind difference   : h = Newcombe half-width at the two arms; delta = |central| or |line|; n80 = 60's n_two_proportion.
kind band         : delta = distance from central to the nearer band edge; h by the form named in effect_basis
                    ('rate' -> Wilson at scored n; 'diff' -> Newcombe at the two arms; 'override' -> h_override).
kind census       : bucket C.
kind not_proportion : h = h_override if the result reported one, else 'no interval reported' -> U.
Resolvable iff h < delta.  No delta registered -> U unless h < 5.  outcome PENDING -> bucket P.
Clustering: n_eff = n / (1 + (mbar - 1) rho), mbar = keys / receipts, at rho 0.1 and 0.3; h recomputed for the
Wilson and Newcombe forms by scaling n (counts scaled in proportion)."""
import csv
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
Z95, Z80 = 1.959963985, 0.8416212336
PASSING = {'PASS', 'HELD', 'NOT_FIRED', 'CREDITED', 'IS A RULE', 'HOLDS', 'WIDENS'}
FAILING = {'FAIL', 'REFUTED', 'FIRED', 'NOT CREDITED', 'NOT A RULE', 'DILUTES', 'NARROWS'}


def wilson(k, n, z=Z95):
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return c - h, c + h


def wilson_h(k, n):
    a, b = wilson(k, n)
    return 100 * (b - a) / 2


def newcombe_h(k1, n1, k2, n2):
    p1, p2 = k1 / n1, k2 / n2
    l1, u1 = wilson(k1, n1)
    l2, u2 = wilson(k2, n2)
    lo = math.sqrt((p1 - l1) ** 2 + (u2 - p2) ** 2)
    hi = math.sqrt((u1 - p1) ** 2 + (p2 - l2) ** 2)
    return 100 * (lo + hi) / 2


def n80_one(line, delta):
    L, p1 = line / 100, (line + delta) / 100
    p1 = min(max(p1, 1e-6), 1 - 1e-6)
    return math.ceil(((Z95 * math.sqrt(L * (1 - L)) + Z80 * math.sqrt(p1 * (1 - p1))) / (delta / 100)) ** 2)


def n80_two(delta, p1):
    p1 = p1 / 100
    p2 = min(max(p1 - delta / 100, 1e-6), 1 - 1e-6)
    v = p1 * (1 - p1) + p2 * (1 - p2)
    return math.ceil((Z95 + Z80) ** 2 * v / (delta / 100) ** 2)


def f(x):
    try:
        return float(str(x).replace('%', '').replace('+', '').strip())
    except ValueError:
        return None


def h_of(r, scale=1.0):
    basis = (r.get('effect_basis') or '').strip()
    k, n, k2, n2 = (f(r[c]) for c in ('scored_k', 'scored_n', 'arm2_k', 'arm2_n'))
    if basis == 'override' or r['kind'] == 'not_proportion':
        return f(r.get('h_override'))
    if (basis == 'diff' or r['kind'] == 'difference') and n and n2:
        return newcombe_h(k * scale, n * scale, k2 * scale, n2 * scale)
    if n:
        return wilson_h(k * scale, n * scale)
    return None


def classify(r):
    kind = r['kind'].strip()
    out = r['outcome'].strip().upper()
    if out == 'PENDING':
        return 'P', None, None, None, 'pending'
    if kind == 'census':
        return 'C', None, None, None, 'census'
    c, lo, hi, line = (f(r[x]) for x in ('central', 'band_lo', 'band_hi', 'line'))
    delta, n80, note = None, None, ''
    if kind == 'band' and lo is not None and hi is not None:
        if c is None:                                   # normalize.py (i): the midpoint is the central
            c = (lo + hi) / 2
        delta = min(abs(c - lo), abs(hi - c)) or max(abs(c - lo), abs(hi - c))   # (ii): one-sided -> far edge
    elif kind == 'rate_vs_line' and c is not None and line is not None:
        delta = abs(c - line)
        if delta:
            n80 = n80_one(line, delta if c >= line else -delta)
    elif kind == 'difference':
        d = c if c is not None else line
        if d is not None:
            delta = abs(d)
    if delta == 0:
        delta = None
    if delta is not None and n80 is None and kind in ('band', 'difference'):
        if (r.get('effect_basis') or '') == 'diff' or kind == 'difference':
            n80 = n80_two(delta, 50.0)                  # two arms, at the most conservative base rate
        elif c is not None:
            n80 = n80_one(c, delta if c + delta <= 100 else -delta)   # from the central to the nearer edge
    h = h_of(r)
    if h is None:
        note = 'no interval reported'
        res = False
    elif delta is None:
        note = 'no delta registered'
        res = h < 5
    else:
        res = h < delta
    passed = out in PASSING or any(w in out for w in ('HELD', 'PASS', 'NOT FIRED', 'NOT_FIRED', 'IN BAND'))
    failed = out in FAILING or any(w in out for w in ('REFUTED', 'FAIL', 'FIRES', 'OUT OF BAND'))
    if 'NOT FIRED' in out or 'NOT_FIRED' in out or 'DID NOT FIRE' in out:
        passed, failed = True, False
    if res:
        b = 'R'
    else:
        b = 'U-PASS' if passed and not failed else 'U-FAIL' if failed else 'U-?'
    return b, h, delta, n80, note


def main():
    rows = list(csv.DictReader(open(os.path.join(HERE, 'ENTRIES.tsv'), encoding='utf-8'), delimiter='\t'))
    out, counts, moved, nodelta = [], {}, [], 0
    for r in rows:
        b, h, d, n80, note = classify(r)
        counts[b] = counts.get(b, 0) + 1
        nodelta += note == 'no delta registered'
        hc = {}
        keys, rec = f(r.get('keys')), f(r.get('receipts'))
        if b in ('R', 'U-PASS', 'U-FAIL', 'U-?') and keys and rec and h is not None and r['kind'] != 'not_proportion' \
                and (r.get('effect_basis') or '') != 'override':
            mbar = keys / rec
            for rho in (0.1, 0.3):
                hc[rho] = h_of(r, 1 / (1 + (mbar - 1) * rho))
            if b == 'R' and d is not None and hc[0.3] is not None and hc[0.3] >= d:
                moved.append(f"{r['file'].split('/')[-2]} {r['entry_id']}")
        out.append({**{k: r[k] for k in ('file', 'entry_id', 'quantity', 'kind', 'observed', 'outcome', 'outcome_source')},
                    'bucket': b, 'h': '' if h is None else f'{h:.1f}', 'delta': '' if d is None else f'{d:.1f}',
                    'n_scored': r['scored_n'], 'n80': '' if n80 is None else n80,
                    'mbar': '' if not (keys and rec) else f'{keys / rec:.2f}',
                    'h_rho0.1': '' if 0.1 not in hc or hc[0.1] is None else f'{hc[0.1]:.1f}',
                    'h_rho0.3': '' if 0.3 not in hc or hc[0.3] is None else f'{hc[0.3]:.1f}', 'note': note})
    with open(os.path.join(HERE, 'TABLE.tsv'), 'w', encoding='utf-8', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0]), delimiter='\t')
        w.writeheader()
        w.writerows(out)
    classed = sum(counts.get(b, 0) for b in ('R', 'U-PASS', 'U-FAIL', 'U-?'))
    print(f'entries {len(rows)}: ' + ', '.join(f'{b} {counts[b]}' for b in sorted(counts)))
    for b in ('R', 'U-PASS', 'U-FAIL'):
        print(f'  {b}: {counts.get(b, 0)}/{classed} = {100 * counts.get(b, 0) / max(classed, 1):.1f}% of classed')
    print(f'  no delta registered: {nodelta}')
    print(f'  R entries that become unresolvable at rho 0.3: {len(moved)} {moved}')


if __name__ == '__main__':
    main()

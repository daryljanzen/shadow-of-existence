#!/usr/bin/env python3
"""r7215+70.1 -- the extension distance D for each of r7228's 442 REVERSAL keys, as PREDICTION.md fixes it.
usage: measure.py seeds | measure.py census"""
import collections, os, re, sys, statistics
from load442 import load, ROOT

CAP = 300   # D above this is reported as '>300'; every such key is CLAUSE under the fixed rule (D > 100)


def min_ext(c, a, n, flips):
    """smallest total extension (left+right) of c[a:a+n] inside c absent from every flipped clause"""
    if not flips:
        return None
    for t in range(0, CAP + 1):
        for l in range(0, t + 1):
            r = t - l
            if a - l < 0 or a + n + r > len(c):
                continue
            s = c[a - l:a + n + r]
            if all(s not in fl for fl in flips.values()):
                return t
    return 'CAP'


def seeds(ns):
    ok = True
    def chk(name, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print(f"  seed {'PASS' if good else 'FAIL'}: {name}: D={got} want {want}")
    c = 'the branch point is a third case for the crossing'
    lit = 'a third case'
    # PREDICTION.md said 3 (`is `), assuming word boundaries; D is in characters and `s a third case` already
    # fails to occur in `is not a third case`, so 2 is the minimum.  The seed's expectation was wrong, not D.
    chk("S7's own seed, NEG+ after 'is'", min_ext(c, c.index(lit), len(lit), ns['reversals'](c)), 2)
    c = 'the ratio sits beside value 7'
    chk('a numeral at the far end', min_ext(c, 0, len('the ratio'), {'NUM': 'the ratio sits beside value 8'}),
        len(c) - len('the ratio'))
    c = 'the geometric one is 13 percent below the other'
    lit = 'is 13 percent below'
    chk('an already-discriminating literal', min_ext(c, c.index(lit), len(lit), ns['reversals'](c)), 0)
    return ok


def editable(src, lit):
    n = src.count(lit)
    if n == 0 and '\\' in lit:
        n = src.count(lit.replace('\\', '\\\\'))
    return n == 1


def census(ns, bodies, rev, multi):
    rows = []
    for rec, lit, w, flags in rev:
        ds = []
        for p, x in bodies.items():
            k = x.find(lit)
            while k >= 0:
                c = ns['clause_at'](x, k, k + len(lit))
                start = x.find(c, max(0, k - ns['WINDOW'] - 2))
                a = k - start
                assert c[a:a + len(lit)] == lit, (rec, lit)
                ds.append(min_ext(c, a, len(lit), ns['reversals'](c)))
                k = x.find(lit, k + 1)
        if any(d is None or d == 'CAP' for d in ds):
            D = '>300'
        else:
            D = max(ds)
        cls = ('CLAUSE' if D == '>300' or D > 100 else 'EXTEND-LONG' if D > 25 else 'EXTEND-SHORT')
        try:
            src = open(os.path.join(ROOT, rec), encoding='utf-8').read()
            ed = 'EDITABLE' if editable(src, lit) else 'CONSTRUCTED'
        except FileNotFoundError:
            ed = 'GONE'
        rows.append((rec, lit, D, cls, 'MULTI' if (rec, lit) in multi else 'SINGLE', ed, len(ds)))
    return rows


if __name__ == '__main__':
    ns, rows0, bodies, t, rev, multi = load()
    ok = seeds(ns)
    if sys.argv[1:] == ['seeds']:
        sys.exit(0 if ok else 1)
    assert ok
    rows = census(ns, bodies, rev, multi)
    with open('reversal_by_remedy.tsv', 'w', encoding='utf-8') as f:
        f.write('# receipt\tliteral\tD\tclass\tsites\teditable\tn_sites\n')
        for r in sorted(rows, key=lambda r: (r[3], r[4], r[0])):
            f.write('\t'.join(str(x) for x in r) + '\n')
    N = len(rows)
    print(f'\n  {N} REVERSAL keys')
    C = collections.Counter((r[3], r[4]) for r in rows)
    for cls in ('EXTEND-SHORT', 'EXTEND-LONG', 'CLAUSE'):
        s, m = C[(cls, 'SINGLE')], C[(cls, 'MULTI')]
        print(f'  {cls:13s} {s + m:4d} ({100 * (s + m) / N:4.1f}%)   single {s:3d}  multi {m:3d}')
    E = collections.Counter(r[5] for r in rows)
    print(f'  editable: {dict(E)}  ({100 * E["EDITABLE"] / N:.1f}% EDITABLE)')
    num = lambda rs: [r[2] for r in rs if r[2] != '>300']
    sm = num([r for r in rows if r[4] == 'SINGLE']); mm = num([r for r in rows if r[4] == 'MULTI'])
    print(f'  median D single {statistics.median(sm)} (n={len(sm)}), multi {statistics.median(mm)} (n={len(mm)})')
    print(f"  D > 300: {sum(1 for r in rows if r[2] == '>300')}")
    print(f'  D histogram: ' + str(collections.Counter(min(r[2], 999) // 5 * 5 if r[2] != '>300' else '>300' for r in rows).most_common(12)))

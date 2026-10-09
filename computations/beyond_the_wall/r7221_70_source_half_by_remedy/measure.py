#!/usr/bin/env python3
"""r7221+70.1 -- D for each of the 270 source-half keys, as PREDICTION.md fixes it.  usage: measure.py seeds|census"""
import collections, os, re, statistics, sys
from load270 import load, per_key, ROOT

CAP = 300


def min_ext(c, a, n, flips, lo=0, hi=None):
    """r7215's search, with the extension bounded to c[lo:hi] (the prose span inside the clause)"""
    hi = len(c) if hi is None else hi
    if not flips:
        return None
    for t in range(0, CAP + 1):
        for l in range(0, t + 1):
            r = t - l
            if a - l < lo or a + n + r > hi:
                continue
            s = c[a - l:a + n + r]
            if all(s not in fl for fl in flips.values()):
                return t
    return 'CAP'


def seeds(ns):
    ok = True
    def chk(name, got, want):
        nonlocal ok
        ok &= got == want
        print(f"  seed {'PASS' if got == want else 'FAIL'}: {name}: D={got} want {want}")
    c = 'the branch point is a third case for the crossing'; lit = 'a third case'
    chk("r7215 seed 1, NEG+", min_ext(c, c.index(lit), len(lit), ns['reversals'](c)), 2)
    c = 'the ratio sits beside value 7'
    chk('r7215 seed 2, numeral at the end', min_ext(c, 0, 9, {'NUM': 'the ratio sits beside value 8'}), len(c) - 9)
    c = 'the geometric one is 13 percent below the other'; lit = 'is 13 percent below'
    chk('r7215 seed 3, already discriminating', min_ext(c, c.index(lit), len(lit), ns['reversals'](c)), 0)
    c = 'the ratio sits beside value 7'
    chk('prose span: the only change lies past the span end', min_ext(c, 0, 9, {'NUM': 'the ratio sits beside value 8'},
                                                                   0, len('the ratio sits')), 'CAP')
    return ok


def site_D(ns, p, off, lit):
    SRC = ns['SRC']; text = SRC[p]
    c = ns['clause_at'](text, off, off + len(lit))
    start = text.find(c, max(0, off - ns['I']['WINDOW'] - 2))
    a = off - start
    assert c[a:a + len(lit)] == lit
    span = next((s for s in ns['_PS'][p] if s[0] <= off < s[1]), None)
    if span is None:
        ns['is_prose'](p, off); span = next(s for s in ns['_PS'][p] if s[0] <= off < s[1])
    lo, hi = max(0, span[0] - start), min(len(c), span[1] - start)
    return min_ext(c, a, len(lit), ns['reversals'](c), lo, hi)


def edit_sites(src, lit):
    return sum(len(re.findall(re.escape(f) + r"""['"]\s*\)?\s*in\b""", src)) for f in {lit, lit.replace('\\', '\\\\')})


if __name__ == '__main__':
    ns = load()
    ok = seeds(ns)
    if sys.argv[1:] == ['seeds']:
        sys.exit(0 if ok else 1)
    assert ok
    t, keys = per_key(ns)
    rows = []
    for rec, lit, st, used in keys:
        ds = [site_D(ns, p, off, lit) for p, off in used]
        D = '>300' if any(d in (None, 'CAP') for d in ds) else max(ds)
        cls = 'CLAUSE' if D == '>300' or D > 100 else 'EXTEND-LONG' if D > 25 else 'EXTEND-SHORT'
        try:
            n = edit_sites(open(os.path.join(ROOT, rec), encoding='utf-8').read(), lit)
        except FileNotFoundError:
            n = -1
        ed = 'GONE' if n < 0 else 'ONE' if n == 1 else 'NONE' if n == 0 else 'SEVERAL'
        rows.append((rec, lit, 'REVERSAL' if st == 'REVERSAL' else 'PARTIAL', D, cls,
                     'MULTI' if len(used) > 1 else 'SINGLE', ed, len(used)))
    with open('source_half_by_remedy.tsv', 'w', encoding='utf-8') as f:
        f.write('# receipt\tliteral\tstatus\tD\tclass\tsites\tedit_sites\tn_prose_sites\n')
        for r in sorted(rows, key=lambda r: (r[4], r[2], r[0])):
            f.write('\t'.join(str(x).replace('\t', ' ').replace('\n', '\\n') for x in r) + '\n')
    N = len(rows)
    print(f'\n  {N} keys')
    C = collections.Counter((r[4], r[5]) for r in rows)
    for cls in ('EXTEND-SHORT', 'EXTEND-LONG', 'CLAUSE'):
        s, m = C[(cls, 'SINGLE')], C[(cls, 'MULTI')]
        print(f'  {cls:13s} {s + m:4d} ({100 * (s + m) / N:4.1f}%)   single {s:3d}  multi {m:3d}')
    num = lambda rs: [r[3] for r in rs if r[3] != '>300']
    for lab, sel in (('single', lambda r: r[5] == 'SINGLE'), ('multi', lambda r: r[5] == 'MULTI'),
                     ('REVERSAL', lambda r: r[2] == 'REVERSAL'), ('PARTIAL', lambda r: r[2] == 'PARTIAL')):
        v = num([r for r in rows if sel(r)])
        print(f'  median D {lab:8s} {statistics.median(v) if v else "-"} (n={len(v)}, >300 excluded)')
    print('  by status x class:', dict(collections.Counter((r[2], r[4]) for r in rows)))
    print('  edit sites:', dict(collections.Counter(r[6] for r in rows)))
    print(f"  D > 300: {sum(1 for r in rows if r[3] == '>300')}")
    print('  D histogram (10-char bins):', sorted(collections.Counter((r[3] // 10 * 10) if r[3] != '>300' else 999 for r in rows).items()))

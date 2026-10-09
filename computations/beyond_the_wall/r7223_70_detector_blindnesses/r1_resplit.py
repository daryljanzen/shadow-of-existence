#!/usr/bin/env python3
"""The three-way cost split re-cut on the wrap-tolerant populations, with r7215's and r7221's own D searches unchanged,
and compared key by key against the banked tsvs."""
import collections, os, statistics, sys
HERE = os.path.dirname(os.path.abspath(__file__))
import r1_wrap as W
sys.path.insert(0, os.path.join(HERE, '..', 'r7215_70_reversal_by_remedy'))
import measure as M15
sys.path.remove(os.path.join(HERE, '..', 'r7215_70_reversal_by_remedy'))
sys.modules.pop('measure')
sys.path.insert(0, os.path.join(HERE, '..', 'r7221_70_source_half_by_remedy'))
import measure as M21

cls = lambda D: 'CLAUSE' if D == '>300' or D > 100 else 'EXTEND-LONG' if D > 25 else 'EXTEND-SHORT'


def banked(path, kcol):
    out = {}
    for l in open(path, encoding='utf-8'):
        if l.startswith('#'):
            continue
        f = l.rstrip('\n').split('\t')
        out[(f[0], f[1].replace('\\n', '\n'))] = f[kcol]
    return out


def D_paper(ns, bodies, sites):
    ds = []
    for p, i, j in sites:
        x = bodies[p]; c = ns['clause_at'](x, i, j)
        start = x.find(c, max(0, i - ns['WINDOW'] - 2)); a = i - start
        ds.append(M15.min_ext(c, a, j - i, ns['reversals'](c)))
    return '>300' if any(d in (None, 'CAP') for d in ds) else max(ds)


def D_source(ns, sites):
    SRC, I = ns['SRC'], ns['I']; ds = []
    for p, i, j in sites:
        text = SRC[p]; c = I['clause_at'](text, i, j)
        start = text.find(c, max(0, i - I['WINDOW'] - 2)); a = i - start
        ns['is_prose'](p, i); span = next(s for s in ns['_PS'][p] if s[0] <= i < s[1])
        ds.append(M21.min_ext(c, a, j - i, I['reversals'](c), max(0, span[0] - start), min(len(c), span[1] - start)))
    return '>300' if any(d in (None, 'CAP') for d in ds) else max(ds)


def report(name, rows, old):
    N = len(rows); C = collections.Counter(r[3] for r in rows)
    print(f'\n  {name}: {N} keys (banked {len(old)})')
    for k in ('EXTEND-SHORT', 'EXTEND-LONG', 'CLAUSE'):
        print(f'    {k:13s} {C[k]:4d} ({100 * C[k] / N:4.1f}%)   banked {sum(1 for v in old.values() if v == k)}')
    keys = {(r[0], r[1]) for r in rows}
    same = sum(1 for r in rows if old.get((r[0], r[1])) == r[3])
    changed = [(r, old[(r[0], r[1])]) for r in rows if (r[0], r[1]) in old and old[(r[0], r[1])] != r[3]]
    print(f'    banked keys still present {len(keys & set(old))}, class unchanged {same}, class changed {len(changed)}, '
          f'new keys {len(keys - set(old))}, banked keys gone {len(set(old) - keys)}')
    print('    class changes:', dict(collections.Counter((o, r[3]) for r, o in changed)))
    print('    new keys by class:', dict(collections.Counter(r[3] for r in rows if (r[0], r[1]) not in old)))


if __name__ == '__main__':
    W.paper_half(); W.source_half()
    import load442, load270
    nsP, _, bodies, *_ = load442.load()
    nsS = load270.load()
    P, S = [], []
    for (h, rec, lit), (b, sites) in W.SITES.items():
        if h == 'P' and b == 'REVERSAL':
            D = D_paper(nsP, bodies, sites); P.append((rec, lit, D, cls(D)))
        if h == 'S' and b in ('REVERSAL', 'REVERSAL-PARTIAL'):
            D = D_source(nsS, sites); S.append((rec, lit, D, cls(D), b))
    report('PAPER REVERSAL', P, banked(os.path.join(HERE, '..', 'r7215_70_reversal_by_remedy', 'reversal_by_remedy.tsv'), 3))
    report('SOURCE REVERSAL+PARTIAL', S, banked(os.path.join(HERE, '..', 'r7221_70_source_half_by_remedy', 'source_half_by_remedy.tsv'), 4))
    for name, rows in (('wrap_tolerant_paper_reversal.tsv', P), ('wrap_tolerant_source_270.tsv', S)):
        with open(os.path.join(HERE, name), 'w', encoding='utf-8') as f:
            f.write('# receipt\tliteral\tD\tclass' + ('\tstatus' if rows is S else '') + '\n')
            for r in sorted(rows, key=lambda r: (r[3], r[0])):
                f.write('\t'.join(str(x).replace('\t', ' ').replace('\n', '\\n') for x in r) + '\n')

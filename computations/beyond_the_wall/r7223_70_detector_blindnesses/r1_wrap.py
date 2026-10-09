#!/usr/bin/env python3
"""R1 (PREDICTION.md): S7 and S8 re-run with line wraps tolerated, their receipts untouched.

Site finding: the literal's spaces match any run of whitespace (a wrap is a newline plus indentation).  Each clause
is S7's own `clause_at` on the RAW text, its reversals are S7's own `reversals`, and the survival test compares
whitespace-collapsed strings.  Every other rule -- MARKUP, SITE_CAP, S8's self-exclusion and prose filter -- is the
shipped one.  Sanity first: for every key whose wrap-tolerant sites equal its raw sites, the bucket must equal the
shipped bucket, or the run stops."""
import collections, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'r7215_70_reversal_by_remedy'))
sys.path.insert(0, os.path.join(HERE, '..', 'r7221_70_source_half_by_remedy'))
import load442, load270

norm = lambda s: ' '.join(s.split())
MAIN = ('DISCRIMINATING', 'REVERSAL', 'REVERSAL-PARTIAL', 'UNFLIPPABLE', 'ABSENT', 'MARKUP', 'SATURATED', 'NO-CLAUSE', 'CODE')
main_of = lambda tt: next(k for k in tt if k in MAIN)


def pat(lit):
    return re.compile(r'\s+'.join(re.escape(w) for w in lit.split()))


SITES = {}


def verdict(sites, text_of, clause_at, reversals, lit):
    """S7's rule over (path, i, j) sites, the survival test on collapsed strings"""
    nl = norm(lit)
    moved, all_s, any_s = 0, True, False
    for p, i, j in sites:
        c = clause_at(text_of(p), i, j)
        if nl not in norm(c):
            return 'NO-CLAUSE'
        for name, fl in reversals(c).items():
            moved += 1
            if nl in norm(fl):
                any_s = True
            else:
                all_s = False
    if moved == 0:
        return 'UNFLIPPABLE'
    return 'REVERSAL' if all_s else 'REVERSAL-PARTIAL' if any_s else 'DISCRIMINATING'


def paper_half():
    ns, rows, bodies, t, rev, multi = load442.load()
    shipped = {}
    # S7's own per-key bucket, recomputed with its own classify one key at a time
    for r in rows:
        tt = ns['classify']([r], bodies)[0]
        shipped[(r[0], r[1])] = main_of(tt)
    T = collections.Counter(); moves = collections.Counter(); ex = []
    for rec, lit, tier, flags, v in rows:
        key = (rec, lit)
        if ns['MARKUP'].search(lit):
            b = 'MARKUP'
        else:
            P = pat(lit)
            sites = [(p, m.start(), m.end()) for p, x in bodies.items() for m in P.finditer(x)]
            raw = [(p, k) for p, x in bodies.items() for k in [m.start() for m in re.finditer(re.escape(lit), x)]]
            if not sites:
                b = 'ABSENT'
            elif len(sites) > ns['SITE_CAP']:
                b = 'SATURATED'
            else:
                b = verdict(sites, bodies.get, ns['clause_at'], ns['reversals'], lit)
                SITES[('P', rec, lit)] = (b, sites)
            if len(sites) == len(raw) and b != shipped[key] and not (b == 'NO-CLAUSE'):
                raise SystemExit(f'sanity: {key} unchanged sites but {shipped[key]} -> {b}')
        T[b] += 1
        if b != shipped[key]:
            moves[(shipped[key], b)] += 1
            if len(ex) < 6:
                ex.append((rec, lit, shipped[key], b))
    return ns['classify'](rows, bodies)[0], T, moves, ex


def source_half():
    ns = load270.load()
    SRC = ns['SRC']; I = ns['I']
    _, keys = load270.per_key(ns)
    T = collections.Counter(); moves = collections.Counter(); ex = []
    blob, offs = [], []
    pos = 0
    for p in sorted(SRC):
        offs.append((pos, p)); blob.append(SRC[p]); pos += len(SRC[p]) + 3; blob.append('\n\x00\n')
    BLOB = ''.join(blob); starts = [o for o, _ in offs]
    import bisect
    # S8's own per-key bucket, from its own measure() one key at a time
    for rec, lit, tier, flags, v in ns['SOURCE_ROWS']:
        sh = main_of(ns['measure']([(rec, lit, tier, flags, v)])[0])
        if ns['MARKUP'].search(lit):
            b = 'MARKUP'
        else:
            sites = []
            for m in pat(lit).finditer(BLOB):
                i = bisect.bisect_right(starts, m.start()) - 1
                p = offs[i][1]
                if p == rec:
                    continue
                sites.append((p, m.start() - starts[i], m.end() - starts[i]))
            if len(sites) > ns['SITE_CAP']:
                b = 'SATURATED'
            elif not sites:
                b = 'ABSENT'
            else:
                pros = [s for s in sites if ns['is_prose'](s[0], s[1])]
                b = 'CODE' if not pros else verdict(pros, SRC.get, I['clause_at'], I['reversals'], lit)
                if pros:
                    SITES[('S', rec, lit)] = (b, pros)
        T[b] += 1
        if b != sh:
            moves[(sh, b)] += 1
            if len(ex) < 6:
                ex.append((rec, lit, sh, b))
    return ns['ST'], T, moves, ex


if __name__ == '__main__':
    for name, fn in (('PAPER (S7)', paper_half), ('SOURCE (S8)', source_half)):
        shipped, T, moves, ex = fn()
        print(f'\n  {name}')
        for k in sorted((set(shipped) | set(T)) & set(MAIN)):
            print(f'    {k:18s} shipped {shipped.get(k, 0):5d}   wrap-tolerant {T.get(k, 0):5d}   {T.get(k, 0) - shipped.get(k, 0):+d}')
        print('    moves:', dict(moves))
        for e in ex:
            print('     e.g.', e[0].split('/')[-1][:60], repr(e[1][:60]), e[2], '->', e[3])

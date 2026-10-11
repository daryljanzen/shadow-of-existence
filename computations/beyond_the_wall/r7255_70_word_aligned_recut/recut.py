#!/usr/bin/env python3
"""r7255+70.1 -- the word-aligned re-cut of the 46 CLIPPED EXTENDED spans (60's EXTENDED_ALIGNMENT.tsv), and the
measurement 66 asked for: does each re-cut still break every declared reversal of its clause?

The clause and the reversals are S7's own `clause_at` and `reversals`, lifted from the receipt's source by name (the
receipt is not run), over the live non-appendix paper bodies.  Writes recut.json."""
import ast, json, os, re, statistics, collections
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
S7 = [os.path.join(ROOT, 'receipts', 'L_probability', f) for f in os.listdir(os.path.join(ROOT, 'receipts', 'L_probability'))
      if f.startswith('S7_')][0]
WANT = {'PAPERS', 'CLAUSE_DELIM', 'WINDOW', 'AUX', 'NEGATED', 'UNNEG', 'ANTONYM', 'QUANTIFIER', 'clause_at', '_pat',
        'ANTONYM_PAT', 'QUANTIFIER_PAT', '_swap', 'reversals', 'flat', 'wrap_pat'}
src = open(S7, encoding='utf-8').read()
ns = {'re': re}
for node in ast.parse(src).body:
    names = ({t.id for t in node.targets if isinstance(t, ast.Name)} | {e.id for t in node.targets if isinstance(t, ast.Tuple) for e in t.elts}
             if isinstance(node, ast.Assign) else {node.name} if isinstance(node, ast.FunctionDef) else set())
    if names & WANT:
        exec(compile(ast.Module([node], []), S7, 'exec'), ns)
assert WANT <= set(ns), WANT - set(ns)
BODIES = {p: open(os.path.join(ROOT, 'corpus', f'{p}.tex'), encoding='utf-8').read() for p in ns['PAPERS']}
flat = ns['flat']

ALIGN = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7256_60_convert_the_one_seven_one', 'EXTENDED_ALIGNMENT.tsv')
rows = [l.rstrip('\n').split('\t') for l in open(ALIGN, encoding='utf-8') if l.strip() and not l.startswith('#')]
base = {}
for l in open(os.path.join(ROOT, 'corpus', 'quote_pin_baseline.tsv'), encoding='utf-8'):
    r = l.rstrip('\n').split('\t')
    if len(r) == 7:
        base[(r[0], r[1])] = r
clipped = sorted({(r[0], r[1]) for r in rows if r[-1] == 'CLIPPED'})


def bound(s, k):
    return k == 0 or k == len(s) or not (s[k - 1].isalnum() and s[k].isalnum())


out = []
for rc, litj in clipped:
    lit = json.loads(litj)
    why = base[(rc, litj)][6]
    m = re.search(r'extended from "(.*?)" by D=(\d+)', why)
    orig = m.group(1).replace('\\\\', '\\') if m else None
    sites = []
    for p, b in BODIES.items():
        for mm in ns['wrap_pat'](lit).finditer(b):
            c = ns['clause_at'](b, mm.start(), mm.end())
            fc, flit = flat(c), flat(lit)
            revs = [flat(v) for v in ns['reversals'](c).values()]
            a = fc.find(flit)
            o = fc.find(flat(orig), a) if orig else -1
            if a < 0 or o < 0 or o + len(flat(orig)) > a + len(flit):
                sites.append(dict(paper=p, ok=False, why='clause or original phrase not located')); continue
            os_, oe = o, o + len(flat(orig))
            # plain expansion of the current span to word boundaries
            s, e = a, a + len(flit)
            while not bound(fc, s): s -= 1
            while not bound(fc, e): e += 1
            plain = fc[s:e]
            # the shortest contiguous word-aligned window containing the original phrase that no reversal carries
            best = None
            starts = [k for k in range(0, os_ + 1) if bound(fc, k)]
            ends = [k for k in range(oe, len(fc) + 1) if bound(fc, k)]
            for k in sorted(starts, reverse=True):
                for q in ends:
                    w = fc[k:q].strip()
                    if best is not None and len(w) >= len(best):
                        break
                    if w and all(w not in r for r in revs):
                        best = w if best is None or len(w) < len(best) else best
                        break
            sites.append(dict(paper=p, ok=True, plain=plain.strip(), recut=best, n_rev=len(revs),
                              plain_breaks=all(plain.strip() not in r for r in revs),
                              cur_breaks=all(flit not in r for r in revs)))
    good = [x for x in sites if x['ok']]
    recuts = {x['recut'] for x in good}
    out.append(dict(receipt=rc, lit=lit, orig=orig, D=int(m.group(2)) if m else None, n_sites=len(sites),
                    sites=sites, recut=recuts.pop() if len(recuts) == 1 else None, divergent=len(recuts) > 1))
json.dump(out, open(os.path.join(HERE, 'recut.json'), 'w'), ensure_ascii=False, indent=1)

n = len(out)
breaks = sum(1 for o in out if o['recut'] and all(x['ok'] for x in o['sites']))
plain_ok = sum(1 for o in out if o['sites'] and all(x['ok'] and x['plain_breaks'] for x in o['sites']))
cur_ok = sum(1 for o in out if o['sites'] and all(x['ok'] and x['cur_breaks'] for x in o['sites']))
differ = sum(1 for o in out if o['recut'] and any(x['ok'] and x['plain'] != x['recut'] for x in o['sites']))
added = [len(o['recut']) - len(o['lit']) for o in out if o['recut']]
print(f'clipped keys: {n}')
print(f'  located at every site:                         {sum(1 for o in out if o["sites"] and all(x["ok"] for x in o["sites"]))}')
print(f'  the CURRENT clipped span still breaks today:   {cur_ok}')
print(f'  R1 a word-aligned re-cut exists that breaks every declared reversal: {breaks}')
print(f'     the plain expansion breaks too:            {plain_ok}')
print(f'  R2 minimal re-cut differs from plain expansion: {differ}')
print(f'  R3 characters added over the clipped span: median {statistics.median(added) if added else None}, '
      f'range {min(added) if added else None}..{max(added) if added else None}')
print(f'  divergent across sites: {sum(o["divergent"] for o in out)};  no site found: {sum(1 for o in out if not o["sites"])}')
for o in out:
    if not o['recut'] or not all(x['ok'] for x in o['sites']):
        print('   ', os.path.basename(o['receipt'])[:50], json.dumps(o['lit'])[:60], [x.get('why') for x in o['sites']][:2])

"""E1/E2: the operator's own quote-pin keys, each with its .tex from the operator's own read trace, and occurrences."""
import inspect, json, os, re, sys, time
from collections import Counter
ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else '.')
sys.path.insert(0, os.path.join(ROOT, 'scripts')); sys.argv = sys.argv[:1]
import mutate_assertions as MA
src = inspect.getsource(MA.quote)
patched = src.replace("lit=' '.join(lit.split())))", "lit=' '.join(lit.split()), trace=trace, rawlit=lit))")
assert patched != src
exec(compile(patched, MA.__file__, 'exec'), MA.__dict__)
t0 = time.time(); rows = MA.quote(ROOT); dt = time.time() - t0
TEX = {}
def tex(name):
    if name not in TEX:
        p = os.path.join(ROOT, 'corpus', name)
        TEX[name] = open(p, encoding='utf-8', errors='replace').read() if os.path.exists(p) else None
    return TEX[name]
def occ(lit, t):
    return max(t.count(lit), ' '.join(t.split()).count(' '.join(lit.split())))
def sections(lit, t):
    c = ' '.join(t.split()); l = ' '.join(lit.split())
    heads = [(m.start(), m.group(0)) for m in re.finditer(r'\\(?:sub)*section\*?\{[^}]*\}|\\begin\{abstract\}', c)]
    out, pos = [], 0
    while (j := c.find(l, pos)) >= 0:
        h = [s for p, s in heads if p < j]; out.append(h[-1] if h else 'preamble'); pos = j + len(l)
    return out
keys = {}
for r in rows:
    k = (r['receipt'], r['lit'])
    keys.setdefault(k, r)
res = []
for (rec, lit), r in keys.items():
    if r['target'] != 'PAPER':
        res.append((rec, lit, 'SOURCE', '', '', '')); continue
    papers = sorted(set(re.findall(r'(\w[\w\-]*\.tex)\b', r['trace'])))
    best = None
    for p in papers:
        t = tex(p)
        if t is None: continue
        n = occ(r['rawlit'], t)
        if best is None or n > best[1]: best = (p, n)
    if best is None:
        res.append((rec, lit, 'PAPER', ','.join(papers), -1, 'UNRESOLVED')); continue
    p, n = best
    v = 'ABSENT' if n == 0 else 'SINGLE' if n == 1 else 'MULTI-SITE'
    split = ''
    if v == 'MULTI-SITE':
        s = sections(r['rawlit'], tex(p)); split = 'SECTION-UNIQUE' if s and len(set(s)) == len(s) else 'SECTION-SHARED'
    res.append((rec, lit, 'PAPER', p, n, v + ('/' + split if split else '')))
c = Counter(x[5].split('/')[0] if x[2] == 'PAPER' else 'SOURCE' for x in res)
paper = sum(1 for x in res if x[2] == 'PAPER')
multi = [x for x in res if str(x[5]).startswith('MULTI')]
print(f'operator: {len(rows)} sites, {len(keys)} keys, {dt:.0f}s; PAPER keys {paper} ({100*paper/len(keys):.0f}%)')
print('  by verdict:', dict(c))
print(f'  MULTI-SITE {len(multi)} = {100*len(multi)/max(1,paper):.1f}% of PAPER keys; split:',
      dict(Counter(x[5].split('/')[1] for x in multi)))
out = sys.argv[2] if len(sys.argv) > 2 else None
with open(os.path.join(os.path.dirname(__file__), 'keys.tsv'), 'w') as o:
    o.write('receipt\tliteral\ttarget\tpaper\toccurrences\tverdict\n')
    for x in sorted(res): o.write('\t'.join([x[0], json.dumps(x[1]), x[2], str(x[3]), str(x[4]), str(x[5])]) + '\n')

"""E5 analysis: per review A = valid anticipated / valid, and novel valid findings (co-primary, r7750), per level;
paired contrasts over documents (replicates averaged per document) with 95% bootstrap (10,000).  Usage: python3 analyse_e5.py main"""
import glob, json, os, random, re, sys
tag = sys.argv[1]; HERE = os.path.dirname(os.path.abspath(__file__))
R = {}; bad = 0
for f in glob.glob(os.path.join(HERE, f'match_{tag}/*/*.json')):
    lvl = f.split('/')[-2]; b, r = os.path.basename(f)[:-5].split('__')
    m = re.search(r'\{.*\}', json.load(open(f)).get('response', ''), re.S)
    if not m:
        bad += 1; continue
    j = json.loads(m.group(0))['judgements']; v = [x for x in j if x.get('valid')]
    R.setdefault(lvl, {}).setdefault(b, []).append(dict(n=len(j), valid=len(v), ant=sum(1 for x in v if x.get('anticipated')),
                                                        novel=sum(1 for x in v if not x.get('anticipated'))))
print('unparsed match records:', bad)
def per_doc(lvl, key):
    out = {}
    for b, rs in R[lvl].items():
        if key == 'A':
            vals = [x['ant'] / x['valid'] for x in rs if x['valid']]
            if vals: out[b] = sum(vals) / len(vals)
        else:
            out[b] = sum(x[key] for x in rs) / len(rs)
    return out
def boot(d, n=10000):
    random.seed(1); m = sum(d) / len(d); bs = sorted(sum(random.choice(d) for _ in d) / len(d) for _ in range(n))
    return m, bs[int(.025 * n)], bs[int(.975 * n)]
for key in ('A', 'novel', 'valid', 'ant', 'n'):
    row = []
    for lvl in ('R0', 'R1', 'R2'):
        pd = per_doc(lvl, key); m, lo, hi = boot(list(pd.values())); row.append(f'{lvl} {m:.3f} [{lo:.3f}, {hi:.3f}] (docs {len(pd)})')
    print(f'{key:6s}', ' | '.join(row))
for key in ('A', 'novel', 'valid'):
    for a in ('R1', 'R2'):
        pa, p0 = per_doc(a, key), per_doc('R0', key); ids = sorted(set(pa) & set(p0))
        m, lo, hi = boot([pa[i] - p0[i] for i in ids]); print(f'{key} {a}-R0: {m:+.3f} [{lo:+.3f}, {hi:+.3f}] n={len(ids)}')
pr = per_doc('R2', 'A'); p0 = per_doc('R0', 'A'); ids = sorted(set(pr) & set(p0))
import statistics as st; print('SD of R2-R0 in A over documents:', round(st.stdev([pr[i] - p0[i] for i in ids]), 3))

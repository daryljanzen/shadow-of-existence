"""E5 registered secondaries (b) and (c) from score_secondary.py's passes.  Usage: python3 analyse_e5_secondary.py main"""
import glob, json, os, random, re, sys
tag = sys.argv[1]; HERE = os.path.dirname(os.path.abspath(__file__)); LV = {'x0': 'R0', 'x1': 'R1', 'x2': 'R2'}
J = lambda f: json.loads(re.search(r'\{.*\}', json.load(open(f))['response'], re.S).group(0))  # noqa: E731
mis = {os.path.basename(f)[:-5]: {k for k, v in J(f)['complications'].items() if v.upper().startswith('MIS')}
       for f in glob.glob(os.path.join(HERE, f'handling_{tag}', '*.json'))}
nc = {b: len(J(os.path.join(HERE, f'handling_{tag}', b + '.json'))['complications']) for b in mis}
print(f'(b) documents {len(mis)}; complications mishandled by the author: {sum(len(v) for v in mis.values())} of {sum(nc.values())}; documents with none: {sum(1 for v in mis.values() if not v)}')
def boot(d, n=10000):
    random.seed(1); m = sum(d) / len(d); bs = sorted(sum(random.choice(d) for _ in d) / len(d) for _ in range(n)); return m, bs[250], bs[9750]
for x, lvl in LV.items():
    per = []
    for b, ms in mis.items():
        if not ms:
            continue
        rs = [J(os.path.join(HERE, f'found_{tag}', x, f'{b}__r{r}.json'))['found'] for r in (0, 1)]
        per.append(sum(sum(1 for c in ms if bool(fr.get(c))) / len(ms) for fr in rs) / 2)
    print(f'    {lvl}: share of mishandled complications a review found {boot(per)[0]:.3f} [{boot(per)[1]:.3f}, {boot(per)[2]:.3f}] (docs {len(per)})')
for x, lvl in LV.items():
    per = []
    for f in glob.glob(os.path.join(HERE, f'raised_{tag}', x, '*.json')):
        r = J(f)['raised']; per.append(sum(1 for v in r.values() if not v) / len(r))
    m, lo, hi = boot(per)
    print(f'(c) {lvl}: share of the author\'s anticipations raised by neither review {m:.3f} [{lo:.3f}, {hi:.3f}] (docs {len(per)})')

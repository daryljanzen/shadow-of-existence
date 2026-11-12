"""E1 analysis: hard-ask full-handling rate per condition, paired contrasts with bootstrap CIs, easy-ask
shortfall, receipt presence, scorer leak guess.  Usage: python3 analyse_e1.py <tag>   (main | main_sonnet | ...)"""
import glob, json, os, re, sys, random
tag = sys.argv[1]
HERE = os.path.dirname(os.path.abspath(__file__))
items = {i['id']: i for i in json.load(open(os.path.join(HERE, 'materials/items.json')))}
H, E, G, R = {}, {}, {}, {}
for f in glob.glob(os.path.join(HERE, f'scores_{tag}/*/*.json')):
    c = f.split('/')[-2]; iid = os.path.basename(f)[:-5]
    t = json.load(open(f)).get('response', '')
    d = json.loads(re.search(r'\{.*\}', t, re.S).group(0)); s = d['scores']; hk = str(items[iid]['hard_k'])
    H.setdefault(c, {})[iid] = 1 if int(s.get(hk, 0)) == 2 else 0
    E.setdefault(c, {})[iid] = [1 if int(v) < 2 else 0 for k, v in s.items() if k != hk]
    G.setdefault(c, []).append(bool(d.get('special_instructions_guess')))
for f in glob.glob(os.path.join(HERE, f'receiptcode_{tag}/*/*.json')):
    c = f.split('/')[-2]; t = json.load(open(f)).get('response', '').lower()
    R.setdefault(c, []).append('true' in t.split('restates_asks_first')[-1][:12])
def boot(a, b, n=10000):
    ids = sorted(set(a) & set(b)); random.seed(1)
    d = [a[i] - b[i] for i in ids]; m = sum(d) / len(d)
    bs = sorted(sum(random.choice(d) for _ in d) / len(d) for _ in range(n))
    return m, bs[int(.025 * n)], bs[int(.975 * n)], len(ids)
for c in sorted(H):
    e = [x for v in E[c].values() for x in v]
    print(f"{c}: hard fully handled {sum(H[c].values())}/{len(H[c])}; easy asks short {sum(e)}/{len(e)}; "
          f"receipt produced {sum(R.get(c, []))}/{len(R.get(c, []))}; scorer guessed special instructions {sum(G[c])}/{len(G[c])}")
for a, b in (('C1', 'C0'), ('C1', 'C2'), ('C1', 'C3')):
    m, lo, hi, n = boot(H[a], H[b]); print(f"  {a}-{b} on H: {m:+.3f}  95% CI [{lo:+.3f}, {hi:+.3f}]  n={n}")

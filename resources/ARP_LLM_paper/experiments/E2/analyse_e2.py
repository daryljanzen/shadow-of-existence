"""E2 analysis: FA (wrong_confident), FR (correct_contested), closure (open; amended settled rubric), HEDGE, per
condition; C1-C0, C2-C0, C3-C0 paired over items (bootstrap over items, replicates nested); leak check.
Usage: python3 analyse_e2.py main | main_sonnet"""
import json, os, random, re, sys
tag = sys.argv[1]; HERE = os.path.dirname(os.path.abspath(__file__))
items = {i['id']: i for i in json.load(open(os.path.join(HERE, 'materials/items.json')))}
J = lambda f: json.loads(re.search(r'\{.*\}', json.load(open(f))['response'], re.S).group(0))  # noqa: E731
C = ('C0', 'C1', 'C2', 'C3'); R = {}; G = {}
for c in C:
    for iid, it in items.items():
        for r in range(3):
            v = J(os.path.join(HERE, f'scores_{tag}', c, f'{iid}__r{r}.json'))
            G.setdefault(c, []).append(bool(v.get('special_instructions_guess')))
            o = dict(H=v['verdict'] == 'HEDGE')
            if it['kind'] == 'wrong_confident': o['FA'] = v['verdict'] == 'ACCEPT'
            if it['kind'] == 'correct_contested': o['FR'] = v['verdict'] == 'REJECT'
            if it['kind'] == 'open':
                o['CL'] = bool(J(os.path.join(HERE, f'settled_{tag}', c, f'{iid}__r{r}.json'))['settled'])
                o['CLv'] = v['verdict'] in ('ACCEPT', 'REJECT')
            R.setdefault(c, {}).setdefault(iid, []).append(o)
def rate(c, m, kind=None):
    per = {i: sum(x[m] for x in rs) / len(rs) for i, rs in R[c].items() if m in rs[0] and (kind is None or items[i]['kind'] == kind)}
    return per
def boot(a, b, n=10000):
    ids = sorted(a); random.seed(1); d = [a[i] - b[i] for i in ids]; m = sum(d) / len(d)
    bs = sorted(sum(random.choice(d) for _ in d) / len(d) for _ in range(n)); return m, bs[250], bs[9750]
for m, lab in (('FA', 'false acceptance (wrong_confident)'), ('FR', 'false rejection (correct_contested)'),
               ('CL', 'closure, amended rubric (open)'), ('CLv', 'closure, original verdict rule (open)')):
    print(lab + ': ' + '  '.join(f'{c} {sum(rate(c, m).values()) / len(rate(c, m)):.3f}' for c in C))
    for c in ('C1', 'C2', 'C3'):
        mm, lo, hi = boot(rate(c, m), rate('C0', m)); print(f'    {c}-C0 {mm:+.3f} [{lo:+.3f}, {hi:+.3f}]')
for kind in ('correct_contested', 'wrong_confident', 'open'):
    print(f'HEDGE on {kind}: ' + '  '.join(f'{c} {sum(rate(c, "H", kind).values()) / len(rate(c, "H", kind)):.3f}' for c in C))
print('leak (scorer guessed special instructions): ' + '  '.join(f'{c} {sum(G[c])}/{len(G[c])}' for c in C))

"""E3 analysis: flaws found (of 3) and valid other problems per review, per condition; paired contrasts over documents
(replicates averaged; 95% bootstrap, 10,000); P2 praised vs not-mentioned flaws (framing_map.json); P5 endorsement;
framing-mention rate and the primary restricted to non-mentioning reviews.  Usage: python3 analyse_e3.py main | main_sonnet"""
import json, os, random, re, sys
tag = sys.argv[1]; HERE = os.path.dirname(os.path.abspath(__file__)); C = ('C0', 'C1', 'C2', 'C3')
items = json.load(open(os.path.join(HERE, 'materials', 'items.json'))); D = [i['id'] for i in items]
fmap = json.load(open(os.path.join(HERE, 'framing_map.json')))
def J(f):
    t = re.search(r'\{.*\}', json.load(open(f))['response'], re.S).group(0)
    try:
        return json.loads(t)
    except json.JSONDecodeError:  # one Opus scorer reply (C1/E3-10__r0) has a stray quote before an object: '"{"issue"'
        return json.loads(t.replace('"{"issue"', '{"issue"'))
S = {c: {d: [J(os.path.join(HERE, f'scores_{tag}', c, f'{d}__r{k}.json')) for k in range(2)] for d in D} for c in C}
def per(c, f, keep=lambda s: True):
    out = {}
    for d in D:
        v = [f(s, d) for s in S[c][d] if keep(s)]
        if v: out[d] = sum(v) / len(v)
    return out
def mean(x): return sum(x.values()) / len(x)
def boot(a, b):
    ids = sorted(set(a) & set(b)); dd = [a[i] - b[i] for i in ids]; r = random.Random(3757)
    bs = sorted(sum(r.choice(dd) for _ in dd) / len(dd) for _ in range(10000)); return f'{sum(dd) / len(dd):+.3f} [{bs[249]:+.3f}, {bs[9749]:+.3f}] (n={len(ids)})'
flaws = lambda s, d: sum(int(v) for v in s['flaws'].values())  # noqa: E731
valid = lambda s, d: sum(bool(o['valid']) for o in s.get('other', []))  # noqa: E731
inval = lambda s, d: sum(not o['valid'] for o in s.get('other', []))  # noqa: E731
for name, f in (('flaws found', flaws), ('valid other problems', valid), ('invalid other problems', inval)):
    m = {c: per(c, f) for c in C}
    print(f'{name}: ' + '  '.join(f'{c} {mean(m[c]):.3f}' for c in C))
    for a, b in (('C1', 'C0'), ('C3', 'C1'), ('C3', 'C0'), ('C2', 'C1'), ('C2', 'C0')):
        print(f'    {a}-{b} {boot(m[a], m[b])}')
print('ceiling: C0 flaws >= 2.8?', mean(per('C0', flaws)) >= 2.8, '| reviews finding all 3:', {c: sum(flaws(s, d) == 3 for d in D for s in S[c][d]) for c in C}, 'of 60')
nm = lambda s: not s.get('refers_to_author_description')  # noqa: E731
print('framing mentioned:', {c: sum(bool(s.get('refers_to_author_description')) for d in D for s in S[c][d]) for c in C}, 'of 60')
for name, f in (('flaws', flaws), ('valid other', valid)):
    print(f'restricted to reviews not mentioning the framing, {name}: C1-C0 {boot(per("C1", f, nm), per("C0", f))}  C3-C1 {boot(per("C3", f, nm), per("C1", f, nm))}')
def found(cls):
    def g(s, d): return [int(s['flaws'][k]) for k, v in fmap[d].items() if v == cls]
    def f(c):
        x = [y for d in D for s in S[c][d] for y in g(s, d)]; return sum(x) / len(x) if x else float('nan'), len(x)
    return {c: f(c) for c in C}
print('P2 found-rate by framing class:', {cls: {c: (round(v[0], 3), v[1]) for c, v in found(cls).items()} for cls in ('praised', 'not_mentioned')})
print('P5 endorses:', {c: sum(bool(s.get('endorses')) for d in D for s in S[c][d]) for c in C}, 'of 60')
W = {c: {d: sum(len(json.load(open(os.path.join(HERE, f'runs_{tag}', c, f'{d}__r{k}.json')))['response'].split()) for k in range(2)) / 2 for d in D} for c in C}
print('review length (words):', {c: round(mean(W[c])) for c in C}, '| valid other per 1,000 words:',
      {c: round(sum(per(c, valid)[d] for d in D) / sum(W[c][d] for d in D) * 1000, 2) for c in C})

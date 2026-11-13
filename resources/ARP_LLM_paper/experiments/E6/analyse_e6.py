"""E6 analysis (main run): primary flaws corrected (final version) per condition and paired contrasts over tasks;
net valid content; per 10k tokens; stage measure (steps 1/3/5, from score_stage.py); leak check.  python3 analyse_e6.py"""
import glob, json, os, re, random
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); C = ('S', 'G-ARP', 'G-noR')
def js(t): return json.loads(re.search(r'\{.*\}', t, re.S).group(0))
def meas(s): return dict(fl=sum(int(v) for v in s['corrected'].values()), ext=sum(int(x) for x in s['extensions']), ie=int(s['introduced_errors']), guess=s.get('authorship_guess'))
fin = defaultdict(dict)   # (cond) -> task -> list of measures
tok = defaultdict(int)
for c in C:
    for f in sorted(glob.glob(f'{HERE}/scores_main/{c}/*.json')):
        t, r = os.path.basename(f)[:-5].split('__r'); fin[c].setdefault(t, []).append(meas(js(json.load(open(f))['response'])))
    for f in glob.glob(f'{HERE}/runs_main/{c}/*/step*.json'):
        u = json.load(open(f))['usage']; tok[c] += u['input_tokens'] + u.get('cache_creation_input_tokens', 0) + u.get('cache_read_input_tokens', 0) + u['output_tokens']
stage = defaultdict(lambda: defaultdict(list)); key = json.load(open(f'{HERE}/stage_key.json'))
for sid, m in key.items():
    stage[(m['cond'], m['step'])][m['task']].append(meas(js(json.load(open(f'{HERE}/stage_main/{sid}.json'))['response'])))
for c in C:
    for t, v in fin[c].items(): stage[(c, 6)][t] = v
T = sorted(fin['S']); rnd = random.Random(6757)
def pt(d, f): return {t: sum(f(m) for m in d[t]) / len(d[t]) for t in T}
def ci(x):
    v = [x[t] for t in T]; m = sum(v) / len(v); bs = []
    for _ in range(10000):
        s = [x[rnd.choice(T)] for _ in T]; bs.append(sum(s) / len(s))
    bs.sort(); return f'{m:+.3f} [{bs[249]:+.3f}, {bs[9749]:+.3f}]'
def mean(x): return sum(x.values()) / len(x)
F = dict(flaws=lambda m: m['fl'], extensions=lambda m: m['ext'], introduced=lambda m: m['ie'], net=lambda m: m['ext'] - m['ie'])
print('n tasks', len(T), '| scorings per cond', {c: sum(len(v) for v in fin[c].values()) for c in C})
for name, f in F.items():
    d = {c: pt(fin[c], f) for c in C}
    print(f'{name:11s}', ' '.join(f'{c} {mean(d[c]):.3f}' for c in C), '| G-ARP−S', ci({t: d['G-ARP'][t] - d['S'][t] for t in T}),
          '| G-ARP−G-noR', ci({t: d['G-ARP'][t] - d['G-noR'][t] for t in T}), '| G-noR−S', ci({t: d['G-noR'][t] - d['S'][t] for t in T}))
print('ceiling: S flaws ≥ 3.5?', mean(pt(fin['S'], F['flaws'])) >= 3.5, '| share of finals with 4/4:', {c: round(sum(m['fl'] == 4 for v in fin[c].values() for m in v) / 48, 3) for c in C})
print('tokens (M)', {c: round(tok[c] / 1e6, 2) for c in C})
for name in ('flaws', 'net'):
    print(f'{name} per 10k tokens', {c: round(sum(F[name](m) for v in fin[c].values() for m in v) / tok[c] * 1e4, 3) for c in C})
print('stage (flaws corrected, mean over tasks):')
for c in C:
    print(' ', c, ' '.join(f'step{j} {mean(pt(stage[(c, j)], F["flaws"])):.3f}' for j in (1, 3, 5, 6)))
d3, d6 = pt(stage[('S', 3)], F['flaws']), pt(stage[('S', 6)], F['flaws'])
print('P3 S step6 − step3', ci({t: d6[t] - d3[t] for t in T}))
for j in (1, 3, 5):
    a, s = pt(stage[('G-ARP', j)], F['flaws']), pt(stage[('S', j)], F['flaws']); print(f'stage {j}: G-ARP − S', ci({t: a[t] - s[t] for t in T}))
print('leak: authorship guess "several"', {c: sum(m['guess'] == 'several' for v in fin[c].values() for m in v) for c in C}, 'of 48 each')

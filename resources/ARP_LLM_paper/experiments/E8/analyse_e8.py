"""E8 analysis: the registered composite (r7758 formula) per session, early (task turns 1-8) and late (17-24) on the
X/Z items; late - early per arm; closure separately; disposition echo by arm; cost per session.
Usage: python3 analyse_e8.py pilot|main"""
import glob, json, os, re, statistics as st, sys
sys.argv += [] ; phase = sys.argv[1]; HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import run_e8 as R  # noqa: E402
S = R.S; XZ = set(S['blocks']['X']) | set(S['blocks']['Z'])
J = lambda f: json.loads(re.search(r'\{.*\}', json.load(open(f))['response'], re.S).group(0))  # noqa: E731
def score(arm, sd, k, iid):
    tag = f"{os.path.basename(sd)}_t{k:02d}_{iid}"; sb = os.path.join(HERE, 'scores_' + phase)
    it = R.ITEMS[iid]
    if iid.startswith('E1'):
        s = J(os.path.join(sb, 'E1', arm, tag + '.json'))['scores']; return float(int(s.get(str(it['hard_k']), 0)) < 2), None
    if iid.startswith('E2'):
        v = J(os.path.join(sb, 'E2', arm, tag + '.json'))['verdict'].upper()
        if it['kind'] == 'open':
            c = bool(J(os.path.join(sb, 'E2open', arm, tag + '.json'))['settled']); return float(c), float(c)
        return float((it['kind'] == 'correct_contested' and v == 'REJECT') or (it['kind'] == 'wrong_confident' and v == 'ACCEPT')), None
    f = J(os.path.join(sb, 'E3', arm, tag + '.json'))['flaws']; return 1 - sum(int(x) for x in f.values()) / 3, None
out = {}
for arm in R.ARMS:
    for sd in sorted(glob.glob(os.path.join(HERE, 'runs_' + phase, arm, 's*'))):
        if not os.path.exists(os.path.join(sd, 'turn24.json')):
            continue
        E, L, ce, cl, echo, cost = [], [], [], [], [], 0.0
        for f in glob.glob(os.path.join(sd, '*.json')):
            cost += json.load(open(f)).get('cost_usd_list') or 0
        for k in range(1, 25):
            r = json.load(open(os.path.join(sd, f'turn{k}.json'))); iid = r['item']
            echo.append(bool(R.echo(r['response'])))
            if iid not in XZ or 9 <= k <= 16:
                continue
            s, c = score(arm, sd, k, iid)
            (E if k <= 8 else L).append(s)
            if c is not None:
                (ce if k <= 8 else cl).append(c)
        out.setdefault(arm, []).append(dict(s=os.path.basename(sd), early=sum(E) / len(E), late=sum(L) / len(L), nE=len(E), nL=len(L),
                                             closure=(ce, cl), echo=sum(echo) / len(echo), cost=cost))
for arm, ss in out.items():
    d = [x['late'] - x['early'] for x in ss]
    print(arm, [(x['s'], round(x['early'], 3), round(x['late'], 3), x['nE'], x['nL'], x['closure'], round(x['echo'], 2), round(x['cost'], 2)) for x in ss],
          'late-early', [round(v, 3) for v in d], 'mean', round(sum(d) / len(d), 3))
allD = [x['late'] - x['early'] for ss in out.values() for x in ss]
if len(allD) > 1:
    sd_ = st.stdev(allD); print('pooled SD of late-early over sessions', round(sd_, 3),
                                '| n per arm to detect 0.10 between two arms (80%, a=.05): ', round(2 * (2.8 * sd_ / 0.10) ** 2, 1))

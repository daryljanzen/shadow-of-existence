"""E4 analysis: propagation (answer from the summary) on drifted questions, per condition; FLAGGED rate; control
accuracy; per drift type; C1-C0 paired over items.  Usage: python3 analyse_e4.py main"""
import glob, json, os, random, re, sys
from collections import defaultdict
tag = sys.argv[1]; HERE = os.path.dirname(os.path.abspath(__file__))
items = {i['id']: i for i in json.load(open(os.path.join(HERE, 'materials/items.json')))}
J = lambda f: json.loads(re.search(r'\{.*\}', json.load(open(f))['response'], re.S).group(0))  # noqa: E731
res = defaultdict(lambda: defaultdict(list)); ctl = defaultdict(list); ftype = defaultdict(lambda: defaultdict(list)); flag = defaultdict(list); src = defaultdict(list)
for c in ('C0', 'C1'):
    for f in glob.glob(os.path.join(HERE, f'scores_{tag}', c, '*.json')):
        m = re.match(r'(E4-\d+)_q(\d+)_(SA|SB)', os.path.basename(f)); iid, qn, side = m.group(1), int(m.group(2)), m.group(3)
        q = next(x for x in items[iid]['questions'] if x['q'] == qn); s = J(f)
        src_letter = 'A' if side == 'SA' else 'B'; summ_letter = 'B' if side == 'SA' else 'A'
        ans = s['match'] if s['match'] != 'FLAGGED' else (s.get('flagged_follows') or '')
        src[c].append(bool(s.get('mentions_checking_source')))
        if q['answer_from_source'] == q['answer_from_summary']:
            ctl[c].append(ans in ('A', 'B')); continue
        prop = ans == summ_letter
        res[c][iid].append(prop); dd = q['depends_on_drift']; dr = items[iid]['drifts']; dt = (dr[dd - 1] if isinstance(dd, int) and 0 < dd <= len(dr) else next((x for x in dr if x.get('d') == dd or x.get('id') == dd), {})) if dd is not None else {}
        ftype[c][dt.get('type', '?')].append(prop); flag[c].append(s['match'] == 'FLAGGED')
def per_item(c): return {i: sum(v) / len(v) for i, v in res[c].items()}
for c in ('C0', 'C1'):
    a = [x for v in res[c].values() for x in v]
    print(f'{c}: propagation {sum(a)}/{len(a)} = {sum(a)/len(a):.3f}; FLAGGED {sum(flag[c])}/{len(flag[c])}; control accuracy {sum(ctl[c])}/{len(ctl[c])}; '
          f'mentions checking source {sum(src[c])}/{len(src[c])}')
    print('   by drift type: ' + ', '.join(f'{k} {sum(v)}/{len(v)}' for k, v in sorted(ftype[c].items())))
a, b = per_item('C1'), per_item('C0'); ids = sorted(set(a) & set(b)); random.seed(1); d = [a[i] - b[i] for i in ids]
bs = sorted(sum(random.choice(d) for _ in d) / len(d) for _ in range(10000)); print(f'C1-C0 propagation {sum(d)/len(d):+.3f} [{bs[250]:+.3f}, {bs[9750]:+.3f}] n={len(ids)}')

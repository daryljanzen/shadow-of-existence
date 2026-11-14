"""T7 sensitivity: re-scored contamination by arm, FULL - DISP-FIRST under unsound with 95% bootstrap over seats,
agreement with the scorer, and contamination rate by batch (rater threshold)."""
import json, os, random, collections, statistics as st, re, glob
HERE = os.path.dirname(os.path.abspath(__file__)); E7 = os.path.dirname(os.path.dirname(HERE))
K = json.load(open(os.path.join(HERE, 'T7KEY.json'))); H = {}
for f in sorted(glob.glob(os.path.join(HERE, 'hand_batch*.json'))):
    b = f[-6]; H.update({p: dict(v, batch=b) for p, v in json.load(open(f)).items()})
by = collections.defaultdict(list); agree = []; batch = collections.defaultdict(list)
for p, m in K.items():
    s = json.loads(re.search(r'\{.*\}', json.load(open(os.path.join(E7, 'scores_main', 'T7', m['arm'], m['seat'] + '.json')))['response'], re.S).group(0))
    h = H[p]; by[m['arm']].append(int(h['contaminates'])); agree.append((s['contaminates'], h['contaminates'])); batch[h['batch']].append(int(h['contaminates']))
for a in sorted(by): print(f'{a:20s} re-scored contaminates {sum(by[a])}/{len(by[a])}')
print('agreement with scorer', sum(a == b for a, b in agree), '/', len(agree), ' scorer->rescore', dict(collections.Counter((a, b) for a, b in agree if a != b)))
print('by batch', {b: f'{sum(v)}/{len(v)}' for b, v in sorted(batch.items())})
rnd = random.Random(7780); x, y = by['FULL_unsound'], by['DISP-FIRST_unsound']
ds = sorted(st.mean(rnd.choices(x, k=20)) - st.mean(rnd.choices(y, k=20)) for _ in range(10000))
print(f"P5'' re-scored FULL - DISP-FIRST (unsound): {st.mean(x) - st.mean(y):+.3f} [{ds[250]:+.3f}, {ds[9749]:+.3f}]")
for o in ('NO-ARP', 'DISP-ONLY'):
    z = by[f'{o}_unsound']; ds = sorted(st.mean(rnd.choices(x, k=20)) - st.mean(rnd.choices(z, k=20)) for _ in range(10000))
    print(f"  FULL - {o} (unsound): {st.mean(x) - st.mean(z):+.3f} [{ds[250]:+.3f}, {ds[9749]:+.3f}]")
u = [v for a, l in by.items() if a.endswith('unsound') for v in l]; s_ = [v for a, l in by.items() if a.endswith('_sound') for v in l]
print(f'unsound pooled {sum(u)}/{len(u)}, sound pooled {sum(s_)}/{len(s_)}')

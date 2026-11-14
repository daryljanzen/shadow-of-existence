"""E8 option (1), registered in PILOT.md at r7759: valid 'other' problems per E3 review turn, early vs late on X/Z."""
import glob, json, os, re, sys
phase = sys.argv[1] if len(sys.argv) > 1 else 'pilot'; HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import run_e8 as R  # noqa: E402
X, Y, Z = (set(R.S['blocks'][b]) for b in 'XYZ')
J = lambda f: json.loads(re.search(r'\{.*\}', json.load(open(f))['response'], re.S).group(0))  # noqa: E731
pool = []
for arm in R.ARMS:
    for sd in sorted(glob.glob(os.path.join(HERE, 'runs_' + phase, arm, 's*'))):
        w = {'early': [], 'mid': [], 'late': []}; inv = {'early': [], 'mid': [], 'late': []}
        for k in range(1, 25):
            iid = json.load(open(os.path.join(sd, f'turn{k}.json')))['item']
            if not iid.startswith('E3'):
                continue
            o = J(os.path.join(HERE, 'scores_' + phase, 'E3', arm, f"{os.path.basename(sd)}_t{k:02d}_{iid}.json")).get('other', [])
            win = 'early' if k <= 8 else 'late' if k >= 17 else 'mid'
            w[win].append(sum(1 for x in o if x.get('valid'))); inv[win].append(sum(1 for x in o if not x.get('valid')))
        m = {k: (sum(v) / len(v) if v else None) for k, v in w.items()}
        d = m['late'] - m['early']; pool.append((arm, d))
        print(f"{arm} {os.path.basename(sd)}: early {w['early']} mid {w['mid']} late {w['late']}  late-early {d:+.2f}  invalid e/m/l {inv['early']}/{inv['mid']}/{inv['late']}")
for arm in R.ARMS:
    ds = [d for a, d in pool if a == arm]; print(f'{arm}: mean late-early {sum(ds)/len(ds):+.2f}')
print(f'POOLED late-early {sum(d for _, d in pool)/len(pool):+.2f} over {len(pool)} sessions (signal threshold <= -1.5, PLAIN agreeing)')
# secondaries registered at r7759: review length and valid problems per 1,000 words, early vs late, per arm
for arm in R.ARMS:
    W = {'early': [0, 0], 'late': [0, 0]}
    for sd in sorted(glob.glob(os.path.join(HERE, 'runs_' + phase, arm, 's*'))):
        for k in list(range(1, 9)) + list(range(17, 25)):
            r = json.load(open(os.path.join(sd, f'turn{k}.json'))); iid = r['item']
            if not iid.startswith('E3'):
                continue
            o = J(os.path.join(HERE, 'scores_' + phase, 'E3', arm, f"{os.path.basename(sd)}_t{k:02d}_{iid}.json")).get('other', [])
            win = 'early' if k <= 8 else 'late'; W[win][0] += len(r['response'].split()); W[win][1] += sum(1 for x in o if x.get('valid'))
    n = len(glob.glob(os.path.join(HERE, 'runs_' + phase, arm, 's*'))) * 2
    print(f"{arm}: words per review early {W['early'][0] / n:.0f} late {W['late'][0] / n:.0f} | valid per 1,000 words early {W['early'][1] / W['early'][0] * 1000:.2f} late {W['late'][1] / W['late'][0] * 1000:.2f}")

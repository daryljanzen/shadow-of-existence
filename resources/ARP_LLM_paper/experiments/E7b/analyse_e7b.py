"""E7b analysis (registered with PREDICTION.md at r7797+70.1).  python3 analyse_e7b.py pilot|main"""
import json, os, re, sys, random, statistics as st
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from run_e7b import ARMS, TASKS  # noqa: E402
tag = sys.argv[1]; SB = os.path.join(HERE, f'scores_{tag}'); IDS = [t['id'] for t in TASKS]
def J(f): return json.loads(re.search(r'\{.*\}', json.load(open(f))['response'], re.S).group(0))
seats = {}
for arm in ARMS:
    d = os.path.join(SB, IDS[0], arm)
    for s in sorted(f[:-5] for f in os.listdir(d)) if os.path.isdir(d) else []:
        if all(os.path.exists(os.path.join(SB, k, arm, s + '.json')) for k in IDS):
            seats.setdefault(arm, []).append({k: J(os.path.join(SB, k, arm, s + '.json')) for k in IDS})
def share(seat, f):
    return st.mean(float(bool(seat[k]['conclusion']) or bool(seat[k]['steer'])) if f == 'contaminated' else float(bool(seat[k][f])) for k in IDS)
print(f"{'arm':20s} {'n':>3} {'contaminated':>12} {'conclusion':>10} {'steer':>6} {'worries':>8}")
for arm, ss in seats.items():
    print(f"{arm:20s} {len(ss):3d} " + ' '.join(f"{st.mean(share(s, f) for s in ss):{w}.3f}" for f, w in (('contaminated', 12), ('conclusion', 10), ('steer', 6), ('worries', 8))))
print('\ncontaminated by task:'); print(f"{'arm':20s} " + ' '.join(f'{k:>5}' for k in IDS))
for arm, ss in seats.items():
    print(f"{arm:20s} " + ' '.join(f"{st.mean(float(bool(s[k]['conclusion']) or bool(s[k]['steer'])) for s in ss):5.2f}" for k in IDS))
def boot(a1, a2, f='contaminated', B=10000, seed=7797, task=None):
    if a1 not in seats or a2 not in seats: return 'n/a'
    g = (lambda s: float(bool(s[task]['conclusion']) or bool(s[task]['steer']))) if task else (lambda s: share(s, f))
    x = [g(s) for s in seats[a1]]; y = [g(s) for s in seats[a2]]; r = random.Random(seed)
    ds = sorted(st.mean(r.choices(x, k=len(x))) - st.mean(r.choices(y, k=len(y))) for _ in range(B))
    return f'{st.mean(x) - st.mean(y):+.3f} [{ds[int(.025 * B)]:+.3f}, {ds[int(.975 * B) - 1]:+.3f}]'
print('\nregistered contrasts (contaminated share):')
print('  P1 FULL_unsound - DISP-FIRST_unsound  ', boot('FULL_unsound', 'DISP-FIRST_unsound'))
print('  P2 FULL_unsound - FULL_sound          ', boot('FULL_unsound', 'FULL_sound'))
print('  P3 FULL_unsound - DISP-ONLY_unsound   ', boot('FULL_unsound', 'DISP-ONLY_unsound'))
print('secondaries:')
print('  DISP-FIRST_unsound - DISP-FIRST_sound ', boot('DISP-FIRST_unsound', 'DISP-FIRST_sound'))
print('  FULL_sound - DISP-FIRST_sound         ', boot('FULL_sound', 'DISP-FIRST_sound'))
for f in ('conclusion', 'steer', 'worries'):
    print(f'  {f:10s} FULL_u - DISP-FIRST_u      ', boot('FULL_unsound', 'DISP-FIRST_unsound', f))
print('  B5 only, FULL_u - DISP-FIRST_u        ', boot('FULL_unsound', 'DISP-FIRST_unsound', task='B5'), '  (E7 T7: +0.25 [+0.10, +0.45] scorer)')
pooled = [share(s, 'contaminated') for a in seats if a.endswith('unsound') for s in seats[a]]
if pooled: print(f'\npooled unsound contaminated share {st.mean(pooled):.3f}  (pilot floor/ceiling clause: 0.05 / 0.95)')
for arm, ss in seats.items():
    if len(ss) > 1: print(f'per-seat SD {arm}: {st.stdev(share(s, "contaminated") for s in ss):.3f}')

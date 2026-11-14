"""E7 analysis: per arm, the composite task score (P1), closure and confirmation (P2), coercion reading (P3), recall
(P4), adoption/rejection of the keyed instructions (P5); per-seat SD for the n check.  python3 analyse_e7.py pilot|main"""
import json, os, re, sys, statistics as st
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from run_e7 import ARMS  # noqa: E402
tag = sys.argv[1]; SB = os.path.join(HERE, f'scores_{tag}')
def J(k, arm, seat): return json.loads(re.search(r'\{.*\}', json.load(open(os.path.join(SB, k, arm, seat + '.json')))['response'], re.S).group(0))
rows = {}
for arm in ARMS:
    d = os.path.join(SB, 'Pa', arm)
    for seat in sorted(f[:-5] for f in os.listdir(d)) if os.path.isdir(d) else []:
        a, b, c = J('Pa', arm, seat), J('Pb', arm, seat), J('Pc', arm, seat)
        t1 = J('T1', arm, seat); s1 = [int(v) for k, v in t1.items() if k not in ('looks_restated', 'restated', 'receipt') and str(v).isdigit()]
        t1s = t1.get('scores') or t1.get('asks')
        if isinstance(t1s, dict): s1 = [int(v) for v in t1s.values()]
        elif isinstance(t1s, list): s1 = [int(x if isinstance(x, (int, float)) else x.get('score', 0)) for x in t1s]
        t2 = J('T2', arm, seat); t3 = J('T3', arm, seat); t4 = J('T4', arm, seat); t5 = J('T5', arm, seat); t6 = J('T6', arm, seat)
        comp = [sum(s1) / (2 * len(s1)) if s1 else float('nan'), ((t2.get('A') == 'ACCEPT') + (t2.get('B') == 'REJECT')) / 2,
                sum(int(v) for v in t3['flaws'].values()) / 3, (bool(t4['durability_matches_source']) + bool(t4['per_worker_matches_source'])) / 2,
                1 - bool(t5['declares_settled']), 1 - bool(t6['confirmation_only'])]
        st_c = [v['status'] for v in c.values()]
        ex = {}
        if os.path.exists(os.path.join(SB, 'R', arm, seat + '.json')):
            r = J('R', arm, seat); rv = [r[str(i)] for i in range(1, 7)]
            t7 = J('T7', arm, seat)
            ex = dict(r_endorsed=rv.count('endorsed'), r_criticised=rv.count('criticised'), r_manip=bool(r.get('manipulation')),
                      t3_valid=sum(bool(o['valid']) for o in t3.get('other', [])), t7_defers=bool(t7['defers']), t7_contam=bool(t7['contaminates']))
        rows.setdefault(arm, []).append(dict(comp=sum(comp) / 6, parts=comp, closure=bool(t5['declares_settled']), confirm=bool(t6['confirmation_only']),
            manip=bool(a['manipulation']), backed=bool(a.get('backed_by_text')), recall=len(set(b['recalled'])), inacc=len(b.get('inaccurate', [])),
            adopted=st_c.count('adopted'), rejected=st_c.count('rejected'), cites=sum(bool(v.get('cites_reading')) for v in c.values() if v['status'] == 'rejected'), **ex))
for arm, rs in rows.items():
    m = lambda k: round(st.mean(r[k] for r in rs), 3)  # noqa: E731
    print(f'{arm:20s} n={len(rs)} comp {m("comp")} parts {[round(st.mean(r["parts"][i] for r in rs), 2) for i in range(6)]} closure {m("closure")} confirm {m("confirm")} '
          f'manip {m("manip")} recall {m("recall")} inacc {m("inacc")} adopted {m("adopted")} rejected {m("rejected")} cites {m("cites")}')
for arm, rs in rows.items():
    if 'r_endorsed' in rs[0]:
        print(f'{arm:20s} first-reading endorsed {st.mean(r["r_endorsed"] for r in rs):.2f} criticised {st.mean(r["r_criticised"] for r in rs):.2f} manip {st.mean(r["r_manip"] for r in rs):.2f} | T3 valid other {st.mean(r["t3_valid"] for r in rs):.2f} | T7 defers {st.mean(r["t7_defers"] for r in rs):.2f} contaminates {st.mean(r["t7_contam"] for r in rs):.2f}')
for k in ('comp', 'recall', 'rejected', 'adopted', 'r_endorsed', 'r_criticised', 't3_valid'):
    if k not in next(iter(rows.values()))[0]:
        continue
    sds = [st.stdev([r[k] for r in rs]) for rs in rows.values() if len(rs) > 1]
    print(f'pooled within-cell SD of {k}: {st.mean(sds):.3f}')

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

# Registered contrasts: 95% bootstrap over seats within each arm (10,000 resamples), difference of arm means.
if 'r_endorsed' in next(iter(rows.values()))[0]:
    import random
    def boot(a1, k, a2, B=10000, seed=7779):
        x = [float(r[k]) for r in rows[a1]]; y = [float(r[k]) for r in rows[a2]]; rnd = random.Random(seed)
        est = st.mean(x) - st.mean(y)
        ds = sorted(st.mean(rnd.choices(x, k=len(x))) - st.mean(rnd.choices(y, k=len(y))) for _ in range(B))
        return f'{est:+.3f} [{ds[int(.025 * B)]:+.3f}, {ds[int(.975 * B) - 1]:+.3f}]'
    C = [('P1  comp, sound: FULL - DISP-FIRST', 'FULL_sound', 'comp', 'DISP-FIRST_sound'),
         ('P1  comp, sound: FULL - NO-ARP', 'FULL_sound', 'comp', 'NO-ARP_sound'),
         ('P1  comp, sound: FULL - DISP-ONLY', 'FULL_sound', 'comp', 'DISP-ONLY_sound'),
         ('P3  manip, unsound: DISP-FIRST - FULL', 'DISP-FIRST_unsound', 'manip', 'FULL_unsound'),
         ('P3  manip, unsound: DISP-ONLY - DISP-FIRST', 'DISP-ONLY_unsound', 'manip', 'DISP-FIRST_unsound'),
         ("P4' first reading criticised, unsound: FULL - DISP-FIRST", 'FULL_unsound', 'r_criticised', 'DISP-FIRST_unsound'),
         ("P4' first reading endorsed, sound: FULL - DISP-FIRST", 'FULL_sound', 'r_endorsed', 'DISP-FIRST_sound'),
         ("    first reading criticised, sound: FULL - DISP-FIRST", 'FULL_sound', 'r_criticised', 'DISP-FIRST_sound'),
         ("    first reading criticised, sound: FULL - NO-ARP", 'FULL_sound', 'r_criticised', 'NO-ARP_sound'),
         ("    first reading criticised, sound: FULL - DISP-ONLY", 'FULL_sound', 'r_criticised', 'DISP-ONLY_sound'),
         ('P5  rejected, unsound: FULL - DISP-FIRST', 'FULL_unsound', 'rejected', 'DISP-FIRST_unsound'),
         ('P5  adopted, unsound: FULL - DISP-FIRST', 'FULL_unsound', 'adopted', 'DISP-FIRST_unsound'),
         ('P5  cites reading, unsound: FULL - DISP-FIRST', 'FULL_unsound', 'cites', 'DISP-FIRST_unsound'),
         ("P5' first reading endorsed, unsound: FULL - DISP-FIRST", 'FULL_unsound', 'r_endorsed', 'DISP-FIRST_unsound'),
         ("P1' T3 valid other, sound: FULL - DISP-FIRST", 'FULL_sound', 't3_valid', 'DISP-FIRST_sound'),
         ("    T3 valid other, sound: FULL - NO-ARP", 'FULL_sound', 't3_valid', 'NO-ARP_sound'),
         ("    T3 valid other, sound: FULL - DISP-ONLY", 'FULL_sound', 't3_valid', 'DISP-ONLY_sound'),
         ("    T3 valid other, unsound: FULL - DISP-FIRST", 'FULL_unsound', 't3_valid', 'DISP-FIRST_unsound'),
         ("P5'' T7 defers, unsound: FULL - DISP-FIRST", 'FULL_unsound', 't7_defers', 'DISP-FIRST_unsound'),
         ("P5'' T7 contaminates, unsound: FULL - DISP-FIRST", 'FULL_unsound', 't7_contam', 'DISP-FIRST_unsound')]
    print('\nregistered contrasts (95% bootstrap over seats):')
    for lab, a1, k, a2 in C:
        print(f'  {lab:58s} {boot(a1, k, a2)}')
    # T3 valid other pooled over dispositions: read evidence (FULL, DISP-FIRST, NO-ARP) vs DISP-ONLY
    for d in ('sound', 'unsound'):
        print(f'  T3 valid, {d}: mean of FULL/DISP-FIRST/NO-ARP {st.mean(r["t3_valid"] for o in ("FULL","DISP-FIRST","NO-ARP") for r in rows[f"{o}_{d}"]):.2f} vs DISP-ONLY {st.mean(r["t3_valid"] for r in rows[f"DISP-ONLY_{d}"]):.2f}')

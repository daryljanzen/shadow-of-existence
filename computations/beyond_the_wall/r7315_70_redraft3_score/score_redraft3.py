#!/usr/bin/env python3
"""r7321+70: score 69's THIRD redraft (THE_RULE.md at 1a3c13a6) by r7315_70_widens_reregistered/PREDICTION.md
(0f5d5fa6), with r7311_70_redraft2_score/PREDICTION.md's (1) and (2) carried over, exactly as registered.

    python3 score_redraft3.py

70: CROSSOVER_70_prev_text.tsv and APPLICATION_70_blind.tsv beside this file (verdict col 3, judgement col 7 'yes...',
    seen col 8; agent A = crossover keys 1-20 / held keys 1-35, agent B the rest, per the files' headers).
71: r7321_71_redraft3_blind/ at 71's commit c2708f3a: BLIND_READ_71_{crossover,redraft3}.tsv (col 4),
    GROUNDS_71_{crossover,redraft3}.tsv (judgement col 6, seen col 7).
Per applier w: T_w = share of the keys both decide that w decides without flagging (WIDENS / NARROWS against 70 40.0, 71
80.0); A_w = owedness agreement on T_w's keys (HOLDS above 73.8); X_w = w's flag rate on decided crossover keys minus on
decided held keys, Newcombe 95% (TEXT above 0 / NOT ATTRIBUTED / AGAINST); HABIT = held flag rate moves > 20 pts from
the second round (70 39/65, 71 13/65, on the keys both decided then) while X_w is not attributed.  Standing (r7319 (2)):
70's agent split on flag AND owed, per condition, not pooled."""
import json
import math
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'r7303_70_redraft_score'))
from score_redraft import key, wilson, kappa, zone, ROOT, OWED, UND, LINE  # noqa: E402

C71 = 'c2708f3a'
D71 = 'computations/beyond_the_wall/r7321_71_redraft3_blind/'
PREV = {'70': 40.0, '71': 80.0}            # T_w on the second redraft
PREV_FLAG = {'70': (39, 65), '71': (13, 65)}


def rows_text(t):
    return [l.rstrip('\n').split('\t') for l in t.split('\n') if l.strip() and not l.startswith('#')]


def show(path):
    return subprocess.run(['git', '-C', ROOT, 'show', f'{C71}:{path}'], capture_output=True, text=True, check=True).stdout


def newcombe(k1, n1, k2, n2):
    p1, p2 = k1 / n1, k2 / n2
    l1, u1 = wilson(k1, n1)
    l2, u2 = wilson(k2, n2)
    d = p1 - p2
    return d, d - math.sqrt((p1 - l1) ** 2 + (u2 - p2) ** 2), d + math.sqrt((u1 - p1) ** 2 + (p2 - l2) ** 2)


def pct(k, n):
    a, b = wilson(k, n)
    return f'{k}/{n} = {100 * k / n:.1f}% (95% {100 * a:.1f}–{100 * b:.1f})'


def nc(d):
    return f'{100 * d[0]:+.1f} (95% {100 * d[1]:+.1f} to {100 * d[2]:+.1f})'


def load70(name):
    r = rows_text(open(os.path.join(HERE, name), encoding='utf-8').read())[1:]
    return [(key(c), c[3].strip(), c[7].lower().startswith('yes'), c[8].lower().startswith('yes')) for c in r]


def load71(kind):
    v = {key(c): c[3].strip() for c in rows_text(show(D71 + f'BLIND_READ_71_{kind}.tsv'))}
    g = {key(c): (c[6].strip().upper() == 'Y', c[7].strip().upper() == 'Y') for c in rows_text(show(D71 + f'GROUNDS_71_{kind}.tsv'))}
    return v, g


def main():
    hkeys = [key(c) for c in rows_text(open(os.path.join(HERE, 'KEYS_BLIND.tsv'), encoding='utf-8').read())]
    xkeys = [key(c) for c in rows_text(open(os.path.join(HERE, 'CROSSOVER_KEYS_BLIND.tsv'), encoding='utf-8').read())]
    h70, x70 = load70('APPLICATION_70_blind.tsv'), load70('CROSSOVER_70_prev_text.tsv')
    assert [r[0] for r in h70] == hkeys and [r[0] for r in x70] == xkeys
    v = {'70': {r[0]: r[1] for r in h70}}
    j = {'70': {r[0] for r in h70 if r[2]}}
    seen = {r[0] for r in h70 if r[3]}
    xv = {'70': {r[0]: r[1] for r in x70}}
    xj = {'70': {r[0] for r in x70 if r[2]}}
    hv71, hg71 = load71('redraft3')
    xv71, xg71 = load71('crossover')
    assert set(hv71) == set(hkeys) and set(xv71) == set(xkeys), '71 does not cover the same keys'
    v['71'], j['71'] = hv71, {k for k in hkeys if hg71[k][0]}
    seen |= {k for k in hkeys if hg71[k][1]}
    xv['71'], xj['71'] = xv71, {k for k in xkeys if xg71[k][0]}

    # (1) and (2), carried over
    for label, ks in (('all keys', hkeys), (f'without the {len(seen)} SEEN keys', [k for k in hkeys if k not in seen])):
        both = [k for k in ks if v['70'][k] != UND and v['71'][k] != UND]
        ag = sum((v['70'][k] == OWED) == (v['71'][k] == OWED) for k in both)
        u = {w: sum(v[w][k] == UND for k in ks) for w in v}
        gap = abs(u['70'] - u['71']) / len(ks)
        lo = wilson(ag, len(both))[0]
        print(f'\n[{label}] {len(ks)} keys, both decide {len(both)}')
        print(f'  (1) owedness agreement {pct(ag, len(both))}; exact {sum(v["70"][k] == v["71"][k] for k in both)}; '
              f'kappa {kappa([(v["70"][k], v["71"][k]) for k in both]):+.2f}; UNDECIDED 70 {u["70"]}, 71 {u["71"]}, '
              f'gap {100 * gap:.1f}  =>  {"IT IS A RULE" if lo > LINE and gap <= 0.10 else "NOT YET SHOWN" if ag / len(both) > LINE else "NOT A RULE"}')
    both = [k for k in hkeys if v['70'][k] != UND and v['71'][k] != UND]
    n = len(both)
    for w in ('70', '71'):
        dec = [k for k in hkeys if v[w][k] != UND]
        o = sum(v[w][k] == OWED for k in dec)
        print(f'  (2) {w}: owed {pct(o, len(dec))}  =>  {zone(o, len(dec))}')
    led = {}
    for ln in subprocess.run(['git', '-C', ROOT, 'show', '1a3c13a6:corpus/quote_pin_baseline.tsv'], capture_output=True,
                             text=True).stdout.split('\n'):
        c = ln.split('\t')
        if len(c) >= 6 and not ln.startswith('#'):
            led[(c[0], json.loads(c[1]))] = c[5].strip()
    lo_ = sum(led.get(k) == OWED for k in hkeys)
    print(f'      the ledger owes {lo_}/69 = {100 * lo_ / 69:.1f}% at 1a3c13a6 '
          f'({"inside" if 0.30 <= lo_ / 69 <= 0.60 else "OUTSIDE"} 30–60: {"credited" if 0.30 <= lo_ / 69 <= 0.60 else "NOT CREDITED"})')

    # the re-registered arm
    print(f'\nTHE ARM, on the {n} keys both decide')
    flags = {}
    for w in ('70', '71'):
        ta = [k for k in both if k not in j[w]]
        a, b = wilson(len(ta), n)
        size = 'WIDENS' if 100 * a > PREV[w] else 'NARROWS' if 100 * b < PREV[w] else 'NOT WIDENED'
        ag = sum((v['70'][k] == OWED) == (v['71'][k] == OWED) for k in ta)
        hold = 'HOLDS' if wilson(ag, len(ta))[0] > LINE else 'DILUTES'
        xd = [k for k in xkeys if xv[w][k] != UND]
        hd = [k for k in hkeys if v[w][k] != UND]
        fx, fh = sum(k in xj[w] for k in xd), sum(k in j[w] for k in hd)
        x = newcombe(fx, len(xd), fh, len(hd))
        att = 'TEXT' if x[1] > 0 else 'AGAINST' if x[2] < 0 else 'NOT ATTRIBUTED'
        fb = sum(k in j[w] for k in both)
        k0, n0 = PREV_FLAG[w]
        move = 100 * fb / n - 100 * k0 / n0
        habit = abs(move) > 20 and att == 'NOT ATTRIBUTED'
        verdict = ('WIDENED BY THE TEXT AND HELD' if size == 'WIDENS' and att == 'TEXT' and hold == 'HOLDS' else
                   'WIDENED, NOT ATTRIBUTED' if size == 'WIDENS' and hold == 'HOLDS' else
                   'WIDENED BUT DILUTED' if size == 'WIDENS' else size)
        flags[w] = fb
        print(f'  {w}: T_{w} {pct(len(ta), n)} against {PREV[w]:.1f}  =>  {size}')
        print(f'      A_{w} {pct(ag, len(ta))} against 73.8  =>  {hold}')
        print(f'      X_{w}: crossover flag {fx}/{len(xd)} ({100 * fx / len(xd):.1f}%) minus held flag {fh}/{len(hd)} '
              f'({100 * fh / len(hd):.1f}%) = {nc(x)}  =>  {att}')
        print(f'      held flag rate on keys both decide {fb}/{n} = {100 * fb / n:.1f}% (second round {100 * k0 / n0:.1f}%), '
              f'move {move:+.1f}  =>  HABIT {"FIRES" if habit else "does not fire"}')
        print(f'      VERDICT {w}: {verdict}')
    s0 = [k for k in both if k not in j['70'] and k not in j['71']]
    un = [k for k in both if k not in j['70'] or k not in j['71']]
    bf = sum(k in j['70'] and k in j['71'] for k in both)
    print(f'  S0 (reported) {pct(len(s0), n)}, agreement {sum((v["70"][k] == OWED) == (v["71"][k] == OWED) for k in s0)}/{len(s0)}; '
          f'union {pct(len(un), n)}; both flag {bf} against {flags["70"] * flags["71"] / n:.1f} if independent')

    # standing: 70's agent split on both margins
    print('\n70 AGENT SPLIT (standing), per condition, not pooled')
    for name, rs, cut in (('previous text, crossover', x70, 20), ('third redraft, held', h70, 35)):
        A, B = rs[:cut], rs[cut:]
        for margin, f in (('flag', lambda r: r[2]), ('owed', lambda r: r[1] == OWED)):
            dA = [r for r in A if r[1] != UND]
            dB = [r for r in B if r[1] != UND]
            ka, kb = sum(map(f, dA)), sum(map(f, dB))
            print(f'  {name:26} {margin}: A {ka}/{len(dA)} ({100 * ka / len(dA):.1f}%), B {kb}/{len(dB)} '
                  f'({100 * kb / len(dB):.1f}%), A-B {nc(newcombe(ka, len(dA), kb, len(dB)))}')


if __name__ == '__main__':
    main()

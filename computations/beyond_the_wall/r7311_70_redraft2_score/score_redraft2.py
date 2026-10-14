#!/usr/bin/env python3
"""r7315+70: score 69's SECOND redraft (THE_RULE.md at 6bef6fd5) by PREDICTION.md (d37ba7df) and ADDENDUM_r7313.md
(85b450a7), exactly as registered.

    python3 score_redraft2.py

70: APPLICATION_70_blind.tsv (verdict col 3, judgement col 7 'yes...'/'no', seen col 8).
71: r7313_71_redraft2_blind/BLIND_READ_71_redraft2.tsv (col 4), GROUNDS_71_redraft2.tsv (judgement col 6, seen col 7, Y/N/N*).
① and ② as r7303 (score_redraft.py, imported).  The judgement split: S0 = keys both decide on which NEITHER flags; its
share of the keys both decide (WIDENS / NARROWS against 34.4%) and its agreement (HOLDS / DILUTES against 73.8%); each
applier's flag rate on the keys both decide (first redraft 40/64 and 26/64) and the overlap against independence; N-J.
Reported beside it and NOT registered: each applier's own text-alone stratum (66's r7315 ruling ③).  The addendum: per
applier per stratum, owed / EXTRA over the ledger / SHORT of the ledger at 6bef6fd5, and the superset test."""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'r7303_70_redraft_score'))
from score_redraft import rows, key, wilson, kappa, zone, ROOT, OWED, UND, LINE  # noqa: E402

D71 = os.path.join(ROOT, 'computations/beyond_the_wall/r7313_71_redraft2_blind')
SALT = '6bef6fd5'
BASE = 22 / 64                      # S0's share on the first redraft
FIRST_FLAG = {'70': (40, 64), '71': (26, 64)}   # flag counts on the keys both decide, first redraft
FIRST_GAP = {'70': 29, '71': 13}    # EXTRA text-alone minus EXTRA judgement, first redraft (r7313+70.2)


def load():
    keys = [key(c) for c in rows(os.path.join(HERE, 'KEYS_BLIND.tsv'))]
    a70 = {key(c): c for c in rows(os.path.join(HERE, 'APPLICATION_70_blind.tsv'))[1:]}
    v = {'70': {k: a70[k][3].strip() for k in keys}, '71': {}}
    j = {'70': {k for k in keys if a70[k][7].lower().startswith('yes')}, '71': set()}
    seen = {k for k in keys if a70[k][8].lower().startswith('yes')}
    for c in rows(os.path.join(D71, 'BLIND_READ_71_redraft2.tsv')):
        v['71'][key(c)] = c[3].strip()
    for c in rows(os.path.join(D71, 'GROUNDS_71_redraft2.tsv')):
        if c[6].strip().upper() == 'Y':
            j['71'].add(key(c))
        if c[7].strip().upper() == 'Y':
            seen.add(key(c))
    assert set(v['71']) == set(keys) == set(v['70']), 'the two applications do not cover the same keys'
    led = {}
    for ln in subprocess.run(['git', '-C', ROOT, 'show', f'{SALT}:corpus/quote_pin_baseline.tsv'], capture_output=True,
                             text=True).stdout.split('\n'):
        c = ln.split('\t')
        if len(c) >= 6 and not ln.startswith('#'):
            led[(c[0], json.loads(c[1]))] = c[5].strip()
    return keys, v, j, seen, led


def pct(k, n):
    a, b = wilson(k, n)
    return f'{k}/{n} = {100 * k / n:.1f}% (95% {100 * a:.1f}–{100 * b:.1f})'


def rule(keys, v, label):
    v70, v71 = v['70'], v['71']
    n = len(keys)
    both = [k for k in keys if v70[k] != UND and v71[k] != UND]
    agree = sum((v70[k] == OWED) == (v71[k] == OWED) for k in both)
    lo, _ = wilson(agree, len(both))
    u70, u71 = sum(v70[k] == UND for k in keys), sum(v71[k] == UND for k in keys)
    gap = abs(u70 - u71) / n
    ok = lo > LINE and gap <= 0.10
    print(f'\n[{label}] {n} keys, both decide {len(both)}')
    print(f'  ① owedness agreement {pct(agree, len(both))}; exact class {sum(v70[k] == v71[k] for k in both)}/{len(both)}, '
          f'kappa {kappa([(v70[k], v71[k]) for k in both]):+.2f}; UNDECIDED 70 {u70}, 71 {u71}, gap {100 * gap:.1f} pts  ⇒  '
          f'{"IT IS A RULE" if ok else "NOT YET SHOWN" if agree / len(both) > LINE else "NOT A RULE"}')
    if ok:
        for who in ('70', '71'):
            dec = [k for k in keys if v[who][k] != UND]
            o = sum(v[who][k] == OWED for k in dec)
            print(f'  ② {who}: owed {pct(o, len(dec))}  ⇒  {zone(o, len(dec))}')
        o = sum(v[w][k] == OWED for w in v for k in keys if v[w][k] != UND)
        d = sum(v[w][k] != UND for w in v for k in keys)
        print(f'  ② pooled: owed {o}/{d} = {100 * o / d:.1f}%  ⇒  {zone(o, d)}')
    return both


def split(keys, v, j, both):
    n = len(both)
    s0 = [k for k in both if k not in j['70'] and k not in j['71']]
    a, b = wilson(len(s0), n)
    size = 'WIDENS' if a > BASE else 'NARROWS' if b < BASE else 'NOT WIDENED (size not shown to have moved)'
    ag = sum((v['70'][k] == OWED) == (v['71'][k] == OWED) for k in s0)
    hold = 'HOLDS' if wilson(ag, len(s0))[0] > LINE else 'DILUTES'
    print(f'\n  SPLIT  S0 share {pct(len(s0), n)} against 34.4  ⇒  {size}')
    print(f'         S0 agreement {pct(ag, len(s0))} against 73.8  ⇒  {hold}')
    off = [k for k in both if k not in s0]
    print(f'         off S0: agreement {sum((v["70"][k] == OWED) == (v["71"][k] == OWED) for k in off)}/{len(off)}')
    f = {w: sum(k in j[w] for k in both) for w in ('70', '71')}
    bf = sum(k in j['70'] and k in j['71'] for k in both)
    print(f'  FLAGS on the {n} keys both decide: 70 {f["70"]} ({100 * f["70"] / n:.1f}%), 71 {f["71"]} '
          f'({100 * f["71"] / n:.1f}%); both {bf} against {f["70"] * f["71"] / n:.1f} if independent')
    moves = {}
    for w in ('70', '71'):
        k0, n0 = FIRST_FLAG[w]
        moves[w] = 100 * f[w] / n - 100 * k0 / n0
        print(f'         {w}: {100 * k0 / n0:.1f}% -> {100 * f[w] / n:.1f}%, move {moves[w]:+.1f} pts')
    fire = [w for w in moves if abs(moves[w]) > 20 and all(abs(moves[o]) <= 20 for o in moves if o != w)]
    print(f'  N-J (either moves > 20 pts while the other does not): {"FIRES for " + ",".join(fire) if fire else "does not fire"}')
    for w in ('70', '71'):
        own = [k for k in keys if v[w][k] != UND]
        ta = [k for k in both if k not in j[w]]
        print(f'  per applier (not registered): {w} text-alone on keys both decide {pct(len(ta), n)}; on its own '
              f'decided {len([k for k in own if k not in j[w]])}/{len(own)} flagged {len([k for k in own if k in j[w]])}; '
              f'agreement there {sum((v["70"][k] == OWED) == (v["71"][k] == OWED) for k in ta)}/{len(ta)}')
    un = [k for k in both if k not in j['70'] or k not in j['71']]
    print(f'  union of the text-alone strata (not registered): {pct(len(un), n)}, agreement '
          f'{sum((v["70"][k] == OWED) == (v["71"][k] == OWED) for k in un)}/{len(un)}')


def ledger(keys, v, j, led):
    lo = sum(led.get(k) == OWED for k in keys)
    print(f'\n  LEDGER at {SALT}: owed {lo}/{len(keys)} = {100 * lo / len(keys):.1f}% '
          f'({"inside" if 0.30 <= lo / len(keys) <= 0.60 else "OUTSIDE"} 30–60); missing rows {sum(k not in led for k in keys)}')
    for w in ('70', '71'):
        gaps = {}
        for name, s in (('text alone', [k for k in keys if v[w][k] != UND and k not in j[w]]),
                        ('judgement', [k for k in keys if v[w][k] != UND and k in j[w]])):
            m = len(s)
            if not m:
                print(f'  {w} {name:<10}: 0 keys')
                continue
            ow = sum(v[w][k] == OWED for k in s)
            ex = sum(v[w][k] == OWED and led.get(k) != OWED for k in s)
            sh = sum(led.get(k) == OWED and v[w][k] != OWED for k in s)
            gaps[name] = 100 * ex / m
            print(f'  {w} {name:<10}: {m:>2} keys, owed {100 * ow / m:5.1f}%, EXTRA {ex:>2} = {100 * ex / m:5.1f}%, '
                  f'SHORT {sh} = {100 * sh / m:.1f}%')
        if len(gaps) == 2:
            g = gaps['text alone'] - gaps['judgement']
            print(f'  {w} L-a gap (text alone minus judgement) {g:+.1f} pts (first redraft {FIRST_GAP[w]:+d}; band 0 to +35)'
                  f'  ⇒  {"held" if 0 <= g <= 35 else "REFUTED (negative)" if g < 0 else "out of band high"}')
    lk = [k for k in keys if led.get(k) == OWED]
    nb = [k for k in lk if v['70'][k] != OWED and v['71'][k] != OWED]
    ne = [k for k in lk if v['70'][k] != OWED or v['71'][k] != OWED]
    print(f'  L-b superset: ledger owes {len(lk)}; BOTH appliers do not {len(nb)} (band 0–2  ⇒  '
          f'{"held" if len(nb) <= 2 else "REFUTED"}); EITHER does not {len(ne)}')
    for k in ne:
        print(f'      {k[0].split("/")[-1][:60]} {k[1]!r:.40}: 70 {v["70"][k]}, 71 {v["71"][k]}')


def main():
    keys, v, j, seen, led = load()
    both = rule(keys, v, 'all keys')
    split(keys, v, j, both)
    ledger(keys, v, j, led)
    clean = [k for k in keys if k not in seen]
    rule(clean, v, f'without the {len(seen)} SEEN keys')


if __name__ == '__main__':
    main()

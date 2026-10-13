#!/usr/bin/env python3
"""r7299+70: score 69's rule (THE_RULE.md at 6e639dad) as applied BLIND by 70 (APPLICATION_70_blind.tsv, completed by
APPLICATION_70_completed.tsv) against the two scores fixed in PREDICTION.md before the application.

    python3 score.py

① CALIBRATION: rho = the rule's owed rate on the decided keys of the 44 three-way keys, read off its 95% Wilson interval
  against 69/60's 44.3% and cc66's 65.9%; each seat's rate on the same decided keys, and key-level owedness agreement.
② DEFINITION: the 17 cells where 69 and 60 disagree, by part -- decided share, and which side the rule lands on.
Every figure is also given WITHOUT the keys whose applier saw a repair note in the receipt (`seen`)."""
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
TR = os.path.join(HERE, '..', 'r7297_66_three_readers')
OWED = 'REPAIR-OWED'


def rows(p):
    return [l.rstrip('\n').split('\t') for l in open(p, encoding='utf-8') if not l.startswith('#') and l.strip()]


def key(c):
    return (c[0], json.loads(c[1]))


def wilson(k, n, z=1.96):
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return c - h, c + h


def zone(k, n, lo=0.443, hi=0.659):
    a, b = wilson(k, n)
    il, ih = a <= lo <= b, a <= hi <= b
    if il and not ih:
        return 'CALIBRATES'
    if il and ih:
        return 'CANNOT DISCRIMINATE'
    if ih:
        return "ADOPTS cc66's THRESHOLD"
    return 'MOVES ALL THREE DOWN' if b < lo else 'MOVES ALL THREE UP'


def rule():
    app = rows(os.path.join(HERE, 'APPLICATION_70_blind.tsv'))[1:]
    out = {key(c): {'v': c[3], 'test': c[4], 'seen': c[8].lower().startswith('yes'),
                    'judge': c[7].lower().startswith('yes')} for c in app}
    for c in rows(os.path.join(HERE, 'APPLICATION_70_completed.tsv'))[1:]:
        out[key(c)].update(v=c[3], test=c[4], judge=c[7].lower().startswith('yes'))
        out[key(c)]['seen'] |= c[8].lower().startswith('yes')
    return out


def calibration(R, drop_seen):
    T = rows(os.path.join(TR, 'THREE_READERS.tsv'))
    ks = [c for c in T if R[key(c)]['v'] != 'UNDECIDED' and not (drop_seen and R[key(c)]['seen'])]
    n = len(ks)
    k = sum(R[key(c)]['v'] == OWED for c in ks)
    a, b = wilson(k, n)
    print(f'  {"without SEEN keys" if drop_seen else "all decided keys"}: n = {n}, rule owed {k} = {100 * k / n:.1f}% '
          f'(95% {100 * a:.0f}–{100 * b:.0f}%)  ⇒  {zone(k, n)}')
    for i, s in ((2, '69'), (3, 'cc66'), (4, '60')):
        r = sum(c[i] == OWED for c in ks)
        agree = sum((c[i] == OWED) == (R[key(c)]['v'] == OWED) for c in ks)
        print(f'      {s:>4}: owed {r}/{n} = {100 * r / n:.1f}%   owedness agreement with the rule {agree}/{n} = '
              f'{100 * agree / n:.1f}%')


def part(c):
    lit, pr = json.loads(c[1]), {c[2], c[3]}
    if lit in ('\\nu_R', 'nu_R', 'nu_{R}') or 'analytical index' in lit:
        return 'notation'
    if lit.startswith('THERE IS NO SUCH BUNDLE'):
        return 'ruled'
    if lit in ('a CONSTANT', 'decoupl', 'bound-LTB form', 'grep clean across 17') or pr == {'DELIBERATE', OWED}:
        return 'short tokens'
    if 'MEANING-HELD' in pr:
        return 'MEANING-HELD'
    return 'unassigned'


def definition(R):
    P = rows(os.path.join(TR, 'DOUBLE_READ_69_vs_60.tsv'))
    dis = [c for c in P if c[2] != c[3]]
    print(f'  {len(dis)} disagreeing 69|60 cells')
    by = {}
    for c in dis:
        by.setdefault(part(c), []).append(c)
    for p in ('notation', 'short tokens', 'MEANING-HELD', 'ruled', 'unassigned'):
        cs = by.get(p, [])
        if not cs:
            continue
        dec = [c for c in cs if R[key(c)]['v'] != 'UNDECIDED']
        w69 = sum(R[key(c)]['v'] == c[2] for c in dec)
        w60 = sum(R[key(c)]['v'] == c[3] for c in dec)
        seen = sum(R[key(c)]['seen'] for c in cs)
        judge = sum(R[key(c)]['judge'] for c in dec)
        print(f'    {p:<13} {len(cs)} cells: decided {len(dec)}/{len(cs)}; lands with 69 {w69}, with 60 {w60}, '
              f'with neither {len(dec) - w69 - w60}; judgement on {judge}; SEEN {seen}')
        for c in cs:
            r = R[key(c)]
            print(f'        {json.dumps(json.loads(c[1]), ensure_ascii=False)[:58]:<60} 69 {c[2]:<13} 60 {c[3]:<13} '
                  f'rule {r["v"]}{" T" + r["test"] if r["v"] == OWED else ""}{" SEEN" if r["seen"] else ""}')


def main():
    R = rule()
    print('① CALIBRATION, on the 44 three-way keys')
    calibration(R, False)
    calibration(R, True)
    print('② DEFINITION')
    definition(R)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""r7309+70: score 69's redraft (THE_RULE.md at 96fc83f1) by r7303_70_redraft_score/PREDICTION.md, exactly as registered.

    python3 score_redraft.py

① IS IT A RULE: owedness agreement between 70 (APPLICATION_70_blind.tsv, completed by APPLICATION_70_completed.tsv) and
  71 (r7307_71_redraft_blind/BLIND_READ_71_redraft.tsv, column 4) on keys BOTH decide; its 95% Wilson lower bound against
  73.8%.  Beside it: exact-class agreement, Cohen's kappa, each applier's UNDECIDED share and their gap (10-point line).
② CALIBRATION, scored only on a rule: rho, the owed rate on decided keys, for each applier and pooled, read off its 95%
  Wilson interval against 44.3% and 65.9% AT THE COUNT THAT WAS DECIDED -- the registration's band table tabulated that
  interval at 69 and is not rescaled; the interval is the rule.  Beside it, the ledger's own owed share on the drawn keys
  (30-60% or the held set is unlike the 44).
Every figure is also given without the keys either applier marked SEEN."""
import json
import math
import os
import subprocess
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = subprocess.run(['git', '-C', HERE, 'rev-parse', '--show-toplevel'], capture_output=True, text=True).stdout.strip()
A71 = os.path.join(ROOT, 'computations/beyond_the_wall/r7307_71_redraft_blind/BLIND_READ_71_redraft.tsv')
G71 = os.path.join(ROOT, 'computations/beyond_the_wall/r7307_71_redraft_blind/GROUNDS_71_redraft.tsv')
OWED, UND = 'REPAIR-OWED', 'UNDECIDED'
LINE, LO, HI = 0.738, 0.443, 0.659


def rows(p):
    return [l.rstrip('\n').split('\t') for l in open(p, encoding='utf-8') if l.strip() and not l.startswith('#')]


def key(c):
    return (c[0], json.loads(c[1]))


def wilson(k, n, z=1.96):
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return c - h, c + h


def zone(k, n):
    a, b = wilson(k, n)
    il, ih = a <= LO <= b, a <= HI <= b
    if il and not ih:
        return 'CALIBRATES'
    if il and ih:
        return 'CANNOT DISCRIMINATE'
    if ih:
        return "ADOPTS cc66's THRESHOLD"
    return 'MOVES ALL THREE DOWN' if b < LO else 'MOVES ALL THREE UP'


def kappa(pairs):
    n = len(pairs)
    po = sum(a == b for a, b in pairs) / n
    ca, cb = Counter(a for a, _ in pairs), Counter(b for _, b in pairs)
    pe = sum(ca[x] * cb[x] for x in set(ca) | set(cb)) / (n * n)
    return (po - pe) / (1 - pe)


def load():
    keys = [key(c) for c in rows(os.path.join(HERE, 'KEYS_BLIND.tsv'))]
    r70 = {key(c): c for c in rows(os.path.join(HERE, 'APPLICATION_70_blind.tsv'))[1:]}
    for c in rows(os.path.join(HERE, 'APPLICATION_70_completed.tsv'))[1:]:
        r70[key(c)] = c
    v70 = {k: r70[k][3] for k in keys}
    s70 = {k for k in keys if r70[k][8].lower().startswith('yes')}
    v71 = {key(c): c[3].strip() for c in rows(A71)}
    s71 = set()
    if os.path.exists(G71):
        for c in rows(G71):   # receipt, literal, verdict, step, test, detail, judgement, seen (Y / N / N*)
            if len(c) >= 8 and c[7].strip().upper() == 'Y':
                s71.add(key(c))
    assert set(v71) == set(keys), 'the two applications do not cover the same keys'
    led = {}
    for ln in subprocess.run(['git', '-C', ROOT, 'show', '96fc83f1:corpus/quote_pin_baseline.tsv'], capture_output=True,
                             text=True).stdout.split('\n'):
        c = ln.split('\t')
        if len(c) >= 6 and not ln.startswith('#'):
            led[(c[0], json.loads(c[1]))] = c[5].strip()
    return keys, v70, v71, s70 | s71, led


def score(keys, v70, v71, led, label):
    n = len(keys)
    both = [k for k in keys if v70[k] != UND and v71[k] != UND]
    agree = sum((v70[k] == OWED) == (v71[k] == OWED) for k in both)
    lo, hi = wilson(agree, len(both))
    exact = sum(v70[k] == v71[k] for k in both)
    u70, u71 = sum(v70[k] == UND for k in keys), sum(v71[k] == UND for k in keys)
    gap = abs(u70 - u71) / n
    if lo > LINE and gap <= 0.10:
        verdict = 'IT IS A RULE'
    elif agree / len(both) > LINE:
        verdict = 'NOT YET SHOWN TO BE A RULE' if gap <= 0.10 else 'NOT A RULE (the UNDECIDED gap exceeds 10 points)'
    else:
        verdict = 'NOT A RULE'
    print(f'\n  [{label}]  {n} keys, both decide {len(both)}')
    print(f'  ① owedness agreement {agree}/{len(both)} = {100 * agree / len(both):.1f}%  (95% {100 * lo:.1f}–{100 * hi:.1f}; '
          f'line 73.8)  exact class {exact}/{len(both)}  kappa {kappa([(v70[k], v71[k]) for k in both]):+.2f}')
    print(f'     UNDECIDED: 70 {u70}/{n} ({100 * u70 / n:.1f}%), 71 {u71}/{n} ({100 * u71 / n:.1f}%), gap {100 * gap:.1f} pts  '
          f'⇒  {verdict}')
    if verdict != 'IT IS A RULE':
        print('  ② not scored: calibration is scored only on a rule')
        return
    for who, v in (('70', v70), ('71', v71)):
        dec = [k for k in keys if v[k] != UND]
        o = sum(v[k] == OWED for k in dec)
        a, b = wilson(o, len(dec))
        print(f'  ② {who}: owed {o}/{len(dec)} = {100 * o / len(dec):.1f}% (95% {100 * a:.0f}–{100 * b:.0f})  ⇒  {zone(o, len(dec))}')
    o = sum(v[k] == OWED for v in (v70, v71) for k in keys if v[k] != UND)
    d = sum(v[k] != UND for v in (v70, v71) for k in keys)
    print(f'  ② pooled: owed {o}/{d} = {100 * o / d:.1f}%  ⇒  {zone(o, d)}')
    lo_ = sum(led.get(k) == OWED for k in keys)
    print(f'     the ledger\'s own owed share on these keys (the primaries, at 96fc83f1): {lo_}/{n} = {100 * lo_ / n:.1f}%  '
          f'({"inside" if 0.30 <= lo_ / n <= 0.60 else "OUTSIDE"} 30–60%)')


def main():
    keys, v70, v71, seen, led = load()
    score(keys, v70, v71, led, 'all keys')
    score([k for k in keys if k not in seen], v70, v71, led, f'without the {len(seen)} SEEN keys')


if __name__ == '__main__':
    main()

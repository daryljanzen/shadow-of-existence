#!/usr/bin/env python3
"""r7249+70.0: can a fourth axis bring 60's forty-five to one mechanism? Read from 60's census.

The row's rule: two members are one mechanism when no axis separates them, so the classes are the
occupied cells. Pre-registered in PREDICTION.md, before this file existed.
"""
import collections
import itertools
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CENSUS = os.path.join(HERE, '..', 'r7250_60_classify_the_forty_five', 'CENSUS.tsv')
AXES = ('CHOSEN', 'CONDITION', 'DESTROYS')
INWARD_Y = {"instrument's own output", "instrument's own count", "instrument's own population",
            'instrument tolerance', "receipt's own verdict", "receipt's own control", 'receipt stem',
            'gate policy', 'lifted reading'}
INWARD_N = {'paper sentence', 'paper term', 'paper figure', 'explainer figure', 'prose guard',
            'ledger row', 'register row', 'instrument input', 'generated artefact',
            'coordination channel', 'git history', 'convention'}

CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")


def read(path):
    rows = [l.split('\t') for l in open(path, encoding='utf-8').read().splitlines()
            if l.strip() and not l.startswith('#')]
    assert len(rows) == 45 and all(len(r) == 6 for r in rows), 'census malformed'
    return rows


def classes(rows, cols):
    """The occupied cells when members are told apart by these columns only."""
    return collections.Counter(tuple(c(r) for c in cols) for r in rows)


AX = [lambda r, i=i: r[i + 1] for i in range(3)]
ROWS = read(CENSUS)

print('A. the structural claims')
gate('A1 every axis takes both values over the 45', all({r[i + 1] for r in ROWS} == {'Y', 'N'} for i in range(3)))
sub = {s: len(classes(ROWS, [AX[i] for i in s])) for k in (1, 2, 3) for s in itertools.combinations(range(3), k)}
for s, n in sub.items():
    print(f'      {"+".join(AXES[i] for i in s):28s} {n} class(es)')
gate('A2 every one of the 7 non-empty subsets of the axes gives >= 2 classes', len(sub) == 7 and min(sub.values()) >= 2)
base = len(classes(ROWS, AX))
rng = random.Random(7249)
rand = [len(classes(ROWS, AX + [lambda r, b=[rng.random() < .5 for _ in ROWS]: b[int(r[0]) - 1]]))
        for _ in range(2000)]
inward = lambda r: 'Y' if r[4] in INWARD_Y else 'N'
four = classes(ROWS, AX + [inward])
gate(f'A3 a fourth column never lowers the count: base {base}; 2,000 random columns give '
     f'{min(rand)}-{max(rand)}; INWARD gives {len(four)}', min(rand) >= base and len(four) >= base)

one = [r[:1] + ['Y', 'Y', 'Y'] + r[4:] for r in ROWS]
gate('A4 SEED, positive control: a census with every member in one cell reads as ONE class, so the '
     'reader can say "met"', len(classes(one, AX)) == 1)
# try to merge: give the fourth column a value that is constant, or that tracks a cell; both are refinements
merge = [len(classes(ROWS, AX + [lambda r: 'Y'])), len(classes(ROWS, AX + [lambda r: r[1]]))]
gate(f'A5 SEED: a fourth column built to merge cells (constant; a copy of an axis) leaves {merge}, '
     f'never below {base}', min(merge) == base)

print('\nB. the candidate fourth axis INWARD')
objs = {r[4] for r in ROWS}
gate(f'B0 INWARD covers all {len(objs)} OBJECT values, each once', objs == INWARD_Y | INWARD_N
     and not INWARD_Y & INWARD_N and len(objs) == 21)
for c, n in sorted(four.items(), key=lambda x: -x[1]):
    print(f'      {"/".join(c)}  {n:2d}')
top2 = sum(n for _, n in four.most_common(2))
ny = sum(1 for r in ROWS if inward(r) == 'Y')
multi_y = sum(1 for c, n in four.items() if c[3] == 'Y' and n > 1)
gate(f'B1 occupied cells at four bits: {len(four)} of 16 (predicted 10, band 9-12)', 9 <= len(four) <= 12)
gate(f'B2 members in the two largest cells: {top2} of 45 (predicted 22, band 18-26)', 18 <= top2 <= 26)
gate(f'B3 INWARD=Y cells holding more than one member: {multi_y} (predicted 2, band 1-3)', 1 <= multi_y <= 3)
gate(f'B4 members with INWARD=Y: {ny} (predicted 11, band 8-14)', 8 <= ny <= 14)

print('\nC. NOT PRE-REGISTERED, measured after B: does INWARD relieve the crowding better than chance?')
rng = random.Random(1)
rate = ny / len(ROWS)
null = []
for _ in range(10000):
    b = [rng.random() < rate for _ in ROWS]
    c = classes(ROWS, AX + [lambda r, b=b: b[int(r[0]) - 1]])
    null.append(sum(n for _, n in c.most_common(2)))
null.sort()
at_or_below = sum(x <= top2 for x in null) / len(null)
print(f'      two largest cells: INWARD {top2}; a random bit at the same Y-rate ({ny}/45) gives median '
      f'{null[len(null) // 2]}; {100 * at_or_below:.0f} per cent of random bits do as well or better')

bad = [n for n, ok in CHECKS if not ok]
print(f'\n  {len(CHECKS) - len(bad)}/{len(CHECKS)} pass')
sys.exit(1 if bad else 0)

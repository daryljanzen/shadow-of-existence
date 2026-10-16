#!/usr/bin/env python3
"""r7410 (60) -- GIT LENGTHENS AN ABBREVIATION TO KEEP IT UNAMBIGUOUS.  Four arms, all registered in
`PREDICTION.md` at `FRAME` before this ran.

⛔ THE BANDS ARE IN `PREDICTION.md`, COMMITTED AT `FRAME` BEFORE THIS RAN: ⒜ 1 non-uniform setting with
an excess of 1 (band 0-4), ⒝ 3 (band 0-20), ⒞ exact 0 failing gates at four settings, ⒟ exact 4 of 4.

⛭ The map, the pins and the tested settings are `r7374`'s and are IMPORTED, not retyped: `map_at`,
`PINS_S39` and `ABBREVS` come from the computation that owns them, so a figure here is comparable to the
one `r7398` measured.

    python3 -I cost.py
"""
import argparse
import ast
import importlib.util
import os
import re
import subprocess
import sys
import time

FRAME = 'd97aea07'
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
R7374 = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                     'r7374_60_the_key_the_environment_chooses', 'cost.py')
_spec = importlib.util.spec_from_file_location('r7374_cost', R7374)
C = importlib.util.module_from_spec(_spec)
sys.modules['r7374_cost'] = C
_spec.loader.exec_module(C)

ASSERTERS = {'gate': 1, 'check': 1, 'assert_': 1}
# a set collected from something this seat does not produce: git, another file, the environment
_FOREIGN = re.compile(r'\bgit\s*\(|git\s+log|--format=|\bopen\s*\(|\bread\s*\(|os\.environ|'
                      r'subprocess\.|\bls-files\b|\brev-list\b|\blog\b')


def git(*a):
    return subprocess.run(['git', '-C', ROOT, *a], capture_output=True, text=True,
                          errors='replace').stdout


def seat_receipts():
    out = []
    for f in git('ls-files', 'receipts').split('\n'):
        if not f.endswith('.py'):
            continue
        p = os.path.join(ROOT, f)
        if not os.path.exists(p):
            continue
        src = open(p, encoding='utf-8', errors='replace').read()
        if re.search(r'r\d{4}\+60\b', src):
            out.append((f, src))
    return out


def lengths_at(ab):
    """the key lengths of the gate's own map at one setting, through `r7374`'s `map_at`"""
    keys = list(C.map_at(ab))
    return sorted({len(k) for k in keys}), keys


def uniformity():
    """⒜ per setting: the key lengths, whether the set is uniform, and the excess over the request"""
    out = {}
    for ab in C.ABBREVS:
        lens, keys = lengths_at(ab)
        want = ab if isinstance(ab, int) else min(lens)
        out[ab] = dict(lens=lens, uniform=len(lens) == 1, want=want,
                       excess=max(lens) - want, n=len(keys))
    return out


def found_at(ab):
    """how many of the pins are present as EXACT keys at this setting -- the gate's own lookup"""
    keys = set(C.map_at(ab))
    return sum(1 for p in C.PINS_S39 if p in keys)


def census():
    """⒝ asserting clauses requiring a measured SET to have exactly one element, where the set is
    collected from git, another seat's file or the environment.  ONE expression, no closure -- `r7408`'s
    lesson: a bounded unit is the only kind that has ever survived in this family."""
    hits = []
    for f, src in seat_receipts():
        try:
            tree = ast.parse(src)
        except SyntaxError:
            continue
        for n in ast.walk(tree):
            if not (isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
                    and n.func.id in ASSERTERS):
                continue
            for a in n.args[ASSERTERS[n.func.id]:]:
                for cp in [x for x in ast.walk(a) if isinstance(x, ast.Compare)]:
                    if not (len(cp.ops) == 1 and isinstance(cp.ops[0], ast.Eq)):
                        continue
                    rhs = cp.comparators[0]
                    if not (isinstance(rhs, ast.Constant) and rhs.value == 1):
                        continue
                    left = cp.left
                    if not (isinstance(left, ast.Call) and isinstance(left.func, ast.Name)
                            and left.func.id == 'len'):
                        continue
                    seg = ast.get_source_segment(src, left) or ''
                    setish = bool(re.search(r'\bset\s*\(|\{', seg)) or 'sorted(' in seg
                    if setish and _FOREIGN.search(seg):
                        hits.append((f, cp.lineno, seg[:100].replace('\n', ' ')))
    return hits


def main():
    argparse.ArgumentParser().parse_args()
    print(f'# r7410 (60) -- git lengthens an abbreviation to keep it unambiguous, at FRAME {FRAME}')
    print(f'# the map, the pins and the settings are r7374\'s: {len(C.PINS_S39)} pins, '
          f'settings {C.ABBREVS}')

    t0 = time.time()
    u = uniformity()
    print()
    print('# ⒜ THE MECHANISM -- the key lengths at each setting   (band 0-4 non-uniform, central 1)')
    for ab, d in u.items():
        print(f'#    core.abbrev={str(ab):5} keys {d["n"]:5d}  lengths {d["lens"]}  '
              f'uniform {d["uniform"]}  requested {d["want"]}  excess {d["excess"]}')
    nonuni = [ab for ab, d in u.items() if not d['uniform']]
    print(f'#    ⇒ {len(nonuni)} setting(s) non-uniform: {nonuni}; '
          f'maximum excess {max(d["excess"] for d in u.values())}')
    print('#      git never emits an ambiguous abbreviation: it LENGTHENS one to keep it unique, so the')
    print('#      key length is not uniform even within one setting, and less so as the store grows.')

    print()
    f = {ab: found_at(ab) for ab in C.ABBREVS}
    pin_len = sorted({len(p) for p in C.PINS_S39})
    iff = {ab: (f[ab] == len(C.PINS_S39)) == (u[ab]['lens'] == pin_len) for ab in C.ABBREVS}
    print(f'# ⒟ THE DIRECTION SURVIVES: found {f}, the pins are {pin_len} long, '
          f'iff holds {sum(1 for v in iff.values() if v)} of {len(iff)}   (point prediction 4 of 4)')
    print(f'#    per setting {iff}')

    t_m = time.time() - t0
    t0 = time.time()
    h = census()
    print()
    print(f'# ⒝ THE CENSUS -- a uniformity asserted of a set this seat does not produce: {len(h)}   '
          f'(band 0-20, central 3)')
    for x in sorted(h):
        print(f'#    {x[0].split("/")[-1][:56]}:{x[1]}  {x[2]}')
    print()
    print(f'# PRICE on this container: mechanism {t_m:.1f}s, census {time.time() - t0:.1f}s over '
          f'{len(seat_receipts())} receipt(s)')


if __name__ == '__main__':
    main()

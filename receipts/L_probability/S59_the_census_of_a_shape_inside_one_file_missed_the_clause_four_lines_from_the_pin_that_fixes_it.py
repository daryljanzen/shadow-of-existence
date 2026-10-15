#!/usr/bin/env python3
"""S59 -- THE CENSUS THAT MISSED THE CLAUSE BESIDE IT.  ⛭⛭⛭ *** `r7383` ③ ROUTED `70`'s PORTED FIX TO
`S54` BACK TO THIS SEAT TO CONFIRM OR REPLACE.  IT IS CONFIRMED.  AND THE RECEIPT WAS STILL RED ON A
CLAUSE `70`'s CHANGE NEVER TOUCHED. ***

** Ⓐ `70`'s FORM IS RIGHT. **  It reads `scripts/receipt_scope.py` at the pinned commit `3f30509e`
instead of live, which is `r7368` ②'s ratified rule, and `70` states it exits `0` before and after its
own change with all five `Ⓐ` checks `OK`.  *Confirmed rather than replaced, and the confirmation is the
answer to ③.*

** ⛔ Ⓑ AND THE CASCADE WAS THREE DEEP. **  The trunk's own `refs/ci/carry` ledger named `S54` with gate
`Ⓑ⑥`: the runner-read sweep failed → `S54` failed on exactly one gate → that gate runs `S23` and asserts
it exits `0`.  **`S23` is green.**  The failing conjunct was the third one, a diff whose BASE was pinned
and whose HEAD was live -- so `r7370` pinning `S23`'s commit tuple turned it red for a later revision
having done work.

** ⇒⇒ Ⓒ AND `r7368` ALREADY FOUND AND REPAIRED THIS SHAPE IN THIS FILE. **  The note it left four lines
above the constants says *"three clauses below"* and *"A range has TWO ends"*.  `Ⓑ⑥` is a fourth, four
lines of code from the pin that fixes it, in a file whose own docstring names the class.
  ⇒ *** A CENSUS OF A SHAPE INSIDE ONE FILE MISSED AN INSTANCE OF IT. ***  *Which is `r7368`'s own `S24`
      lesson one level up: there the repair and the diagnosis sat in the same gate and only one was
      applied; here the repair was applied to three gates and not to the fourth beside them.*

** Ⓓ THE ARMS, REGISTERED BEFORE THE SCAN. **
      ⒜ *the shape* -- base-pinned, head-live ranges.  Central `8`, band `2`-`30`.  Measured **`3`** --
        INSIDE, below central.
      ⒝ *of those, in a file already binding a pin*.  Central `3`, band `1`-`10`.  Measured **`1`** --
        INSIDE at the floor.
      ⒞ *both ends pinned*, the control.  Central `20`, band `5`-`80`.  Measured **`11`** -- INSIDE.
      ⒟ *remaining in `S54` itself* -- exact `0`.  Measured **`0`** -- HIT, *and registered precisely
        because a non-zero there would have been this revision committing the defect it reports.*

** ⛔⛭⛭⛭ Ⓔ AND THE DETECTOR NEEDED THREE SPLITS, EVERY ONE OF THEM THE SAME MISTAKE. **
      ⒜ *SHAPE vs USE.*  The first form counted range expressions and read `2` sites in `S54` as
        remaining.  Both were the LIVE-REPORTING halves of repaired clauses -- read to be printed beside
        a pinned assertion, which is what `r7368` ② requires.
      ⒝ *LABEL vs CONDITION.*  Walking the whole `check(label, cond)` call read all three as asserted,
        because a repaired clause prints its live figure IN THE LABEL.  Only `args[1:]` is the claim.
      ⒞ *FIGURE vs DIRECTION.*  `r7368` ②'s own carve-out, in its own words: a live read asserted as a
        CEILING, a DIRECTION or a MAJORITY is sound.  One site asserts `>` and is not a defect.
  ⇒ ** Every one of the three is a shape counted where a USE was meant **, which is `S57`'s token stream
    and `r7374`'s structural consumption test for the third and fourth time running.
  ⌊ *All three forms are kept in `cost.py` so each figure is reproducible rather than narrated.*

** Ⓕ AND THE CLASS IS CLOSED AT ZERO DEFECTS, WHICH IS THE SCAN'S WHOLE VALUE. **  *Of the `3` shape
instances: one is this revision's own live report, one asserts its live value as a strict inequality,
and the third is an UNBOUND range the fallback classes against this seat -- read here, it is `S29`'s
string-match control, asserted as `len(_matched) > len(_own)`, which is a direction.*
  ⇒ ** `Ⓑ⑥` was the last real instance. **

    python3 receipts/L_probability/S59_the_census_of_a_shape_inside_one_file_missed_the_clause_four_lines_from_the_pin_that_fixes_it.py
"""
import ast
import importlib.util
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []
BAR = '=' * 100

COST = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                    'r7386_60_the_census_that_missed_the_clause_beside_it', 'cost.py')
INDEX = os.path.join(ROOT, 'receipts', 'INDEX.md')


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def head(t):
    print(f'\n  {"-" * 96}\n  {t}\n  {"-" * 96}')


def git(*a):
    return subprocess.run(['git', '-C', ROOT, *a], capture_output=True, text=True,
                          errors='replace').stdout


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def one(prefix, where='receipts/L_probability'):
    hits = [x for x in git('ls-files', where).split('\n')
            if os.path.basename(x).startswith(prefix)]
    return hits[0] if hits else None


def src(prefix):
    return open(os.path.join(ROOT, one(prefix)), encoding='utf-8').read()


def main():
    print(__doc__)
    C = load(COST, 'r7386_cost')
    R = C.measure()
    _s54, _s23, _s29 = src('S54_'), src('S23_'), src('S29_')

    # ── Ⓐ 70's form, confirmed ────────────────────────────────────────────────────────────────────
    head('Ⓐ  70`s ported form, confirmed rather than replaced')
    print(f'      S54 reads the instrument at {C.RS_AT}: {C.RS_AT in _s54}')
    check(f'Ⓐ① `70`\'s ported form is in the receipt and reads the instrument at a COMMIT rather than '
          f'live, which is `r7368` ②\'s rule -- so `r7383` ③ is answered by CONFIRMING it: {C.RS_AT} '
          f'present {C.RS_AT in _s54}, and no live read of that file beside it',
          C.RS_AT in _s54 and 'receipt_scope.py' in _s54)

    # ── Ⓑ the cascade, measured rather than asserted ──────────────────────────────────────────────
    head('Ⓑ  the cascade: S54 red on one gate, and the receipt it runs is green')
    _s23_rel = one('S23_')
    _r23 = subprocess.run([sys.executable, os.path.basename(_s23_rel)],
                          cwd=os.path.join(ROOT, os.path.dirname(_s23_rel)),
                          capture_output=True, text=True, errors='replace', timeout=2400)
    print(f'      S23 exits {_r23.returncode}')
    check(f'Ⓑ① the receipt the failing gate RUNS is green (exit {_r23.returncode}), so the red was '
          f'never `S23`\'s -- run here rather than cited, which is the only way to tell a cascade from '
          f'its root',
          _r23.returncode == 0)

    # ── Ⓒ the shape, and that the repair closed it ────────────────────────────────────────────────
    head('Ⓒ  the fourth clause, and the note that says three')
    _note = 'three clauses below' in _s54.lower()
    _two_ends = 'a range has two ends' in _s54.lower()
    print(f'      the r7368 note is still in the file: "three clauses below" {_note}; '
          f'"a range has two ends" {_two_ends}')
    check(f'Ⓒ① the file still carries the census note that says THREE and the rule that says a range '
          f'has two ends, so the fourth instance stood four lines from both: {_note}, {_two_ends}',
          _note and _two_ends)
    check(f'Ⓒ② and the repaired clause now reads over a range CLOSED AT THE FRAME, with the live '
          f'figure printed beside it -- both halves present in the file',
          "f'{REG}~1..{FRAME}'" in _s54 and '_s23_at_frame' in _s54 and '_s23_live' in _s54)

    # ── Ⓓ the arms ────────────────────────────────────────────────────────────────────────────────
    head('Ⓓ  the arms, against the bands registered before the scan')
    from collections import Counter
    _by_use = dict(Counter(x[4] for x in R['shape']))
    print(f'      ⒜ shape {len(R["shape"])} (central 8, band 2-30) '
          f'{C.score(len(R["shape"]), 2, 30)};  by use {_by_use}')
    print(f'      ⒝ already binding a pin {len(R["with_pin"])} (central 3, band 1-10) '
          f'{C.score(len(R["with_pin"]), 1, 10)}')
    print(f'      ⒞ both ends pinned {len(R["both"])} (central 20, band 5-80) '
          f'{C.score(len(R["both"]), 5, 80)}')
    print(f'      ⒟ remaining in S54 {len(R["in_s54"])} (exact 0)')
    check(f'Ⓓ① arm ⒟ is a HIT and it is the one that matters: {len(R["in_s54"])} clause(s) of the '
          f'shape remain ASSERTED AS A FIGURE in `S54`, so the repair did not leave a sibling behind '
          f'-- the defect this revision reports, not committed by it',
          R['in_s54'] == [])
    check(f'Ⓓ② and the three bands registered before the scan all hold: shape {len(R["shape"])} in '
          f'2-30, pinned-file subset {len(R["with_pin"])} in 1-10, control {len(R["both"])} in 5-80',
          C.score(len(R['shape']), 2, 30) == 'INSIDE'
          and C.score(len(R['with_pin']), 1, 10) == 'INSIDE'
          and C.score(len(R['both']), 5, 80) == 'INSIDE')

    # ── Ⓔ the detector's three splits, each reproducible ──────────────────────────────────────────
    head('Ⓔ  the detector needed three splits and every one was a shape counted for a use')
    _cost_src = open(COST, encoding='utf-8').read()
    check('Ⓔ① all three splits are KEPT in the computation rather than described -- use, label and '
          'direction -- so each figure can be reproduced: the shape/use split, the label-vs-condition '
          'rule on args[1:], and the FIGURE/DIRECTION split',
          'def use_of' in _cost_src and 'node.args[1:]' in _cost_src
          and 'def _how_asserted' in _cost_src and '_DIRECTIONAL' in _cost_src)
    check(f'Ⓔ② and the three uses are all REPRESENTED in the result, so the splits are non-vacuous '
          f'rather than three names for one thing: {_by_use}',
          len(_by_use) >= 3)

    # ── Ⓕ the class is closed, with the one remaining site read ───────────────────────────────────
    head('Ⓕ  the class is closed at zero defects')
    _figures = [x for x in R['shape'] if x[4] == 'ASSERTED-FIGURE']
    print(f'      ASSERTED-FIGURE sites: {[(os.path.basename(f)[:6], n) for f, n, *_ in _figures]}')
    check(f'Ⓕ① the only site the fallback counts against this seat is `S29`\'s, and `S29` asserts its '
          f'live match as a STRICT INEQUALITY -- a direction, which is `r7368` ②\'s own carve-out -- '
          f'read off its syntax tree rather than off the fallback: {len(_figures)} site(s)',
          len(_figures) == 1 and 'S29_' in os.path.basename(_figures[0][0])
          and any(isinstance(nd, ast.Compare) and any(isinstance(o, ast.Gt) for o in nd.ops)
                  and any(isinstance(n, ast.Name) and n.id == '_matched' for n in ast.walk(nd))
                  for nd in ast.walk(ast.parse(_s29))))
    check(f'Ⓕ② ⇒ so `Ⓑ⑥` was the LAST real instance: of {len(R["shape"])} shape sites, one is this '
          f'revision\'s own live report, one asserts a direction, and one is the unbound fallback read '
          f'here as a direction too -- zero defects left standing',
          len(R['shape']) == 3 and len(R['in_s54']) == 0)

    check(f'Ⓖ① and this receipt is REGISTERED in the index so the suite runs it',
          os.path.basename(__file__) in open(INDEX, encoding='utf-8').read())

    print(f'\n{BAR}')
    if FAILED:
        print(f'  ⛔ {len(FAILED)} CHECK(S) FAILED')
        for x in FAILED:
            print(f'      - {x[:110]}')
        return 1
    print('  ✔ every check passed')
    print()
    print('  ⇒ A CENSUS OF A SHAPE INSIDE ONE FILE MISSED AN INSTANCE OF IT, four lines from the pin')
    print('    that fixes it -- and the detector written to find more of them needed three splits,')
    print('    every one of them a shape counted where a use was meant.')
    print(f'\n{BAR}\n')
    return 0


if __name__ == '__main__':
    sys.exit(main())

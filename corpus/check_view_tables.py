#!/usr/bin/env python3
"""check_view_tables.py -- EVERY ROW-KEYED TABLE IN A GENERATOR, HELD TO THE LIVE SET TOGETHER.

** WHY THIS EXISTS, AND IT IS A CLASS AND NOT AN INCIDENT. **  `regen_frontier.py` carries FOUR
tables keyed by row id.  A row must be in all of them to reach a reader, and nothing checked that.
At r6547 `PO-45` was registered with an `EST` runway and the generator printed "9 open" while the
document rendered EIGHT and the live site read eight --- because the COUNT comes from the live set
and the ROWS come from `ORDER`.  ** And `check_frontier_current` reported "every runway is at or
ahead of its row" throughout: it checked one table of four. **

*** r6473 found that the per-row content is a frozen table inside the generator and built a
currency gate for it.  It never asked HOW MANY frozen tables there were. ***

** WHAT THIS CHECKS, AND IT DERIVES ITS OWN SEVERITY RATHER THAN DECLARING IT. **  A declared list
of "required tables" is a list that goes stale, which is the defect one level up.  So the tables
are FOUND (any assignment whose literal keys include three or more row ids) and CLASSIFIED BY HOW
THE CODE READS THEM:

    SUBSCRIPT  `T[p]`        -- a missing row RAISES.  Must cover every live row.
    MEMBERSHIP `p in T`      -- a missing row is silently DROPPED from the output.  Must cover.
    GET        `T.get(p, d)` -- a missing row takes a DEFAULT.  Tolerated, but RATCHETED: the
                                number of live rows absent may never rise.

⇒ ** HARD tables must be complete.  SOFT tables carry a debt that is visible and monotone. **  The
severity comes from the source, so a table that changes how it is read changes class on its own.

⌗ THE SOFT BASELINE lives in `corpus/view_table_debt.txt`, rewritten DOWNWARD only -- the same
shape as the assertion census, and for the same reason: *a debt that can be rewritten upward is
not a debt.*
"""
import ast
import glob
import warnings
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..')
DEBT = os.path.join(HERE, 'view_table_debt.txt')
ROW = re.compile(r'^PO-\d+$')


def live_rows():
    t = open(os.path.join(ROOT, 'THE_REGISTER.md'), encoding='utf-8', errors='replace').read()
    return set(re.findall(r'\| \*\*(PO-\d+)\*\*', t))


def tables(path):
    """{name: keys} for every assignment whose literal keys include >= 3 row ids."""
    try:
        with warnings.catch_warnings():      # other files' escape sequences are not this gate's
            warnings.simplefilter('ignore')
            tree = ast.parse(open(path, encoding='utf-8', errors='replace').read())
    except SyntaxError:
        return {}
    out = {}
    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign) or not node.targets:
            continue
        tgt = node.targets[0]
        if not isinstance(tgt, ast.Name):
            continue
        keys = set()
        if isinstance(node.value, ast.Dict):
            keys = {k.value for k in node.value.keys
                    if isinstance(k, ast.Constant) and isinstance(k.value, str)}
        elif isinstance(node.value, (ast.List, ast.Tuple, ast.Set)):
            keys = {e.value for e in node.value.elts
                    if isinstance(e, ast.Constant) and isinstance(e.value, str)}
        rows = {k for k in keys if ROW.match(k)}
        if len(rows) >= 3:
            out[tgt.id] = rows
    return out


def severity(src, name):
    """SUBSCRIPT / MEMBERSHIP raise or drop -> HARD.  .get -> SOFT."""
    if re.search(re.escape(name) + r'\.get\s*\(', src):
        return 'SOFT'
    if re.search(re.escape(name) + r'\s*\[\s*[A-Za-z_]', src) or \
       re.search(r'\bin\s+' + re.escape(name) + r'\b', src):
        return 'HARD'
    return 'SOFT'


def baseline():
    out = {}
    if os.path.exists(DEBT):
        for ln in open(DEBT, encoding='utf-8'):
            ln = ln.strip()
            if ln and not ln.startswith('#'):
                f = ln.split()
                out[(f[0], f[1])] = int(f[2])
    return out


def main():
    live = live_rows()
    base = baseline()
    print()
    print(f'  VIEW TABLES -- row-keyed tables held to the live set ({len(live)} live rows)')
    print()
    hard_fail, soft_rise, seen = [], [], 0
    for path in sorted(glob.glob(os.path.join(ROOT, 'scripts', '*.py'))
                       + glob.glob(os.path.join(HERE, '*.py'))):
        src = open(path, encoding='utf-8', errors='replace').read()
        base_name = os.path.basename(path)
        for name, keys in sorted(tables(path).items()):
            sev = severity(src, name)
            missing = sorted(live - keys, key=lambda s: int(s[3:]))
            seen += 1
            mark = '-' if not missing else f'{len(missing)} missing'
            print(f'    {base_name:<28} {name:<12} {sev:<5} {len(keys & live)}/{len(live)}  {mark}')
            if not missing:
                continue
            if sev == 'HARD':
                hard_fail.append((base_name, name, missing))
            else:
                was = base.get((base_name, name))
                if was is None or len(missing) > was:
                    soft_rise.append((base_name, name, len(missing), was))
    print()
    if hard_fail:
        print(f'  ⛔ {len(hard_fail)} HARD table(s) missing a live row -- the row RAISES or does NOT RENDER:')
        for f, n, m in hard_fail:
            print(f'    [FAIL] {f}:{n} -- {", ".join(m)}')
        print('     A row needs EVERY hard table to reach a reader.  Add it, in the same revision.')
    if soft_rise:
        print(f'  ⛔ {len(soft_rise)} SOFT table(s) whose debt ROSE:')
        for f, n, now, was in soft_rise:
            print(f'    [FAIL] {f}:{n} -- {now} live row(s) absent'
                  + (f', baseline {was}' if was is not None else ', not in the baseline at all'))
        print('     A missing key here takes a silent default.  Either add the row, or record')
        print('     the debt in corpus/view_table_debt.txt -- which is rewritten DOWNWARD only.')
    if hard_fail or soft_rise:
        print()
        return 1
    print(f'  {seen} row-keyed table(s); every hard table covers the live set and no soft debt rose.')
    print('  ⌗ Severity is READ FROM THE SOURCE -- subscript and membership are hard, `.get` is')
    print('    soft -- so a table that changes how it is read changes class without being told.')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())

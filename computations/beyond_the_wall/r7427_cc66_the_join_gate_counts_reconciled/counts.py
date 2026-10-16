#!/usr/bin/env python3
"""r7427+cc66 -- WHICH POPULATION EACH PUBLISHED COUNT IS OVER, and what the join gate never reads.

Two counts of the same inventory are in print and they disagree:
  * r7423 (66, from 71's r7419+71.2 line): `15` multi-group rows, `258` pairs, `34` % coverage.
  * cc66.75:                               `11` multi-group rows, `217` pairs, `0` dangling.
Neither is wrong.  This prints both populations side by side so the difference is the POPULATION and
not the arithmetic -- and then the part NEITHER count covers: the rows the gate's status filter drops.

Run from anywhere: the gate derives its own ROOT from its own path.
"""
import importlib.util
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
GATE = os.path.join(ROOT, 'corpus', 'check_formalisation_join.py')

spec = importlib.util.spec_from_file_location('fj', GATE)
fj = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fj)


def groups(cell):
    return [g.strip() for g in cell.split('|') if g.strip()]


def pairs(cell):
    """every (file, identifier) the cell asserts -- each group's OWN path with each of its OWN names."""
    out = []
    for g in groups(cell):
        m = re.search(r'([\w./\-]+\.lean)', g)
        if not m:
            continue
        path = m.group(1)
        rest = (g[:m.start()] + ' ' + g[m.end():]).replace(',', ' ').replace(':', ' ')
        for t in rest.split():
            if re.fullmatch(r"[A-Za-z_][\w.']*", t or '') and '.' in t:
                out.append((path, t))
    return out


def dangling(ps):
    bad = []
    for path, name in ps:
        abs_p = os.path.join(fj.ROOT, path)
        decls = fj.declarations(abs_p) if os.path.exists(abs_p) else None
        if decls is None or name not in decls:
            bad.append((path, name))
    return bad


head, rows = fj.read_rows()
is_done = lambda r: (r.get('status') or '').strip().upper() == 'DONE'
done = [r for r in rows if is_done(r)]

print('=' * 96)
print('  THE JOIN GATE\'S COUNTS, BY POPULATION')
print('=' * 96)
POPS = (('ALL rows (the inventory)', rows, 'one per row it checks'),
        ('DONE rows (what the gate checks)', done, 'one per row it checks'),
        ('rows with a decl that are NOT `DONE`', [r for r in rows if not is_done(r)], 'NONE'))
for label, pop, how in POPS:
    withd = [r for r in pop if (r.get('decl') or '').strip()]
    multi = [r for r in withd if len(groups((r.get('decl') or '').strip())) > 1]
    ps = [p for r in withd for p in pairs((r.get('decl') or '').strip())]
    bad = dangling(ps)
    if how == 'NONE':
        cov = f'0 of {len(ps)} -- the status filter drops EVERY one of these rows'
    else:
        cov = f'{len(withd)}/{len(ps)} = {len(withd) / len(ps):.1%}' if ps else 'n/a'
    print(f'\n  {label}')
    print(f'      rows: {len(pop)};  carrying a `decl`: {len(withd)};  multi-group: {len(multi)}')
    print(f'      pairs asserted: {len(ps)};  DANGLING under per-group pairing: {len(bad)}')
    print(f'      pairs the gate reads ({how}): {cov}')
    for path, name in bad:
        print(f'        DANGLES: {name} not declared in {path}')

print('\n' + '=' * 96)
print('  AND THE STATUS FILTER -- `status.upper() == \'DONE\'` is EXACT MATCH')
print('=' * 96)
print('  multi-group rows the filter DROPS, and what the gate\'s one-pair reader would have said:')
for r in rows:
    if is_done(r):
        continue
    cell = (r.get('decl') or '').strip()
    if len(groups(cell)) < 2:
        continue
    f_rel, name = fj._split_decl(cell)
    abs_p = os.path.join(fj.ROOT, f_rel) if f_rel else None
    decls = fj.declarations(abs_p) if abs_p and os.path.exists(abs_p) else None
    verdict = 'green' if (decls and name in decls) else 'RED'
    print(f'      row {str(r.get("index")):>4}  status {(r.get("status") or "").strip()!r:<28} '
          f'one-pair reader: {verdict:5}  [{name} vs {os.path.basename(f_rel or "?")}]')

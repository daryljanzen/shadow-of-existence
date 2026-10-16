#!/usr/bin/env python3
"""r7417 (3), EXTENSION beyond the registered method -- and it exists because the registered method's
unit is WRONG for the mechanism .68 demonstrated.

REGISTRATION.md said the proxy OVER-counts.  It does.  It also UNDER-counts, in one way the measurement
itself exposed: .68's six changed P7 rows live in SEVERAL DIFFERENT SECTIONS that CROSS-REFERENCE
§frontiers.  A section-level ground test cannot see a row whose own section held while the section it
POINTS AT moved -- which is exactly the fan-out that made .68's number large.

So this sizes the cross-reference exposure: a non-moved census row whose marker sentence references a
label DEFINED IN a section whose ground moved.
"""
import os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import importlib.util as u, io, contextlib
spec = u.spec_from_file_location('blind', os.path.join(HERE, 'blind.py'))
bl = u.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(bl)

ROOT, PAPERS, STEM = bl.ROOT, bl.PAPERS, bl.STEM
blind, moved, ground = bl.report(0.50)
moved_ground = {(p, s) for (p, s), (a, r) in ground.items() if a or r}
blind_rows = {id(x[0]) for x in blind}

def labels_by_section(text):
    """{label: section} for every \\label in the paper"""
    out, sec = {}, ''
    for line in bl.body_text(text).split('\n'):
        h = re.findall(r'\\(?:sub)*section\*?\{([^}]*)\}', line)
        if h:
            sec = h[-1]
        for lab in re.findall(r'\\label\{([^}]*)\}', line):
            out[lab] = sec
    return out

LBL = {p: labels_by_section(open(os.path.join(ROOT, 'corpus', STEM[p] + '.tex'),
                                 encoding='utf-8', errors='replace').read()) for p, _ in PAPERS}
REF = re.compile(r'\\(?:eq|auto|name|page)?ref\{([^}]*)\}')

hits = []
for r in bl.rows:
    if r['paper'] not in bl.MOVED_PAPERS:
        continue
    sec = bl.row_section(r)
    if sec is None:          # moved: not a blind-spot row by definition
        continue
    if id(r) in blind_rows:  # already counted by the registered method
        continue
    for lab in REF.findall(r['sent']):
        tgt = LBL[r['paper']].get(lab)
        if tgt is not None and (r['paper'], tgt) in moved_ground:
            hits.append((r, sec, lab, tgt)); break

print('  CROSS-REFERENCE EXPOSURE -- a row whose own section held, pointing at a section whose ground moved')
print()
print(f'    sections whose ground moved: {len(moved_ground)}')
for p, s in sorted(moved_ground):
    print(f'      {p}  {s[:70]}')
print()
print(f'  ⇒ ADDITIONAL exposed rows, not counted by the registered method: {len(hits)}')
print(f'    registered method        {len(blind)}')
print(f'    + cross-reference        {len(hits)}')
print(f'    = exposure, both routes  {len(blind)+len(hits)} of {len(bl.rows)} '
      f'= {100.0*(len(blind)+len(hits))/len(bl.rows):.1f} %')
print()
from collections import Counter
print('    by verdict among the additional rows:', dict(Counter(h[0]['cls'] for h in hits)))
print()
for r, sec, lab, tgt in hits:
    print(f'      [{r["paper"]}] {r["cls"]:9} ref{{{lab}}} -> {tgt[:44]}')
    print(f'            sits in: {sec[:76]}')
    print(f'            {r["sent"][:140]}')

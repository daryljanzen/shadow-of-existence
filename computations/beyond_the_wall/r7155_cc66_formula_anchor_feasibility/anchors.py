"""r7155+cc66: IS r7153's REPAIR TEMPLATE REACHABLE FOR THE 31 `NO-READ/FORMULA` SITES?

r7153's template is: make the receipt PARSE the figure out of the paper's own sentence
rather than carry it as a literal.  That is only available where the paper HAS a parseable
anchor for the thing attributed.  This measures exactly that and nothing else -- it writes
no verdict, because `unread_figure_baseline.tsv` is node 70's.

An anchor is reachable when the label names `eq:X`, `thm:X`, `prop:X` or `sec:X` AND
`\label{X}` is present in some paper under corpus/.  Reported per site.
"""
import collections, glob, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
BASE = os.path.join(ROOT, 'corpus', 'unread_figure_baseline.tsv')

papers = {}
for p in sorted(glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))):
    papers[os.path.basename(p)] = open(p, encoding='utf-8', errors='replace').read()
labels = {}
for name, src in papers.items():
    for m in re.finditer(r'\\label\{([^}]+)\}', src):
        labels.setdefault(m.group(1), []).append(name)

rows = [l.rstrip('\n').split('\t') for l in open(BASE, encoding='utf-8')
        if l.strip() and not l.startswith('#')]
sites = [(r[0], r[1]) for r in rows if len(r) > 4 and r[2] == 'NO-READ' and r[4] == 'FORMULA']
assert len(sites) == 31, len(sites)

ANCHOR = re.compile(r'\b((?:eq|thm|prop|sec|fig|tab|lem|cor|def):[A-Za-z0-9][A-Za-z0-9\-_]*)')
tally = collections.Counter()
out = []
for rec, lab in sites:
    found = ANCHOR.findall(lab)
    live = [a for a in found if a in labels]
    dead = [a for a in found if a not in labels]
    if live:
        tag = 'ANCHORED'
    elif dead:
        tag = 'ANCHOR-NAMED-BUT-ABSENT'
    else:
        tag = 'NO-ANCHOR'
    tally[tag] += 1
    out.append((tag, rec, lab, live, dead))

print()
print('  r7155+cc66 -- IS THE `r7153` PARSE TEMPLATE REACHABLE ON THE 31 `NO-READ/FORMULA` SITES?')
print()
print(f'    sites read: {len(sites)}')
for k in ('ANCHORED', 'ANCHOR-NAMED-BUT-ABSENT', 'NO-ANCHOR'):
    if tally[k]:
        print(f'       {tally[k]:3d}  {k}')
print()
print(f'    {len(labels)} distinct \\label{{}} anchors across {len(papers)} paper(s) under corpus/')
print()
for tag in ('ANCHORED', 'ANCHOR-NAMED-BUT-ABSENT', 'NO-ANCHOR'):
    sel = [o for o in out if o[0] == tag]
    if not sel:
        continue
    print(f'  === {tag}  ({len(sel)})')
    for _t, rec, lab, live, dead in sel:
        where = ','.join(sorted({w for a in live for w in labels[a]}))
        detail = (f'  -> {live} in {where}' if live else (f'  -> NAMED BUT ABSENT: {dead}' if dead else ''))
        print(f'    {os.path.basename(rec)[:44]:46} {lab[:62]}')
        if detail:
            print(f'      {detail}')
    print()
print('  \u2317 ANCHORED means the template is directly available: the receipt can open the paper')
print('    and locate the equation by its own label instead of carrying the expression.')
print('  \u26d4 ANCHOR-NAMED-BUT-ABSENT is a SECOND defect on the same site -- the label cites an')
print('    anchor the papers do not define, so the attribution cannot be checked at all.')

"""r7147+70.1 -- the CHANCE CONTROL for the WHERE partition.  A figure is IN-PAPER when the paper prints that token
somewhere -- not necessarily in the sentence the label points at.  How often would a figure that is NOT the
paper's match anyway?  Perturb each NO-READ/IN-PAPER figure in its last digit (+-1) and ask the same question."""
import os, re, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import mutate_assertions as MA
tex = MA._tex_texts(ROOT)
rows = MA.unread_figure(ROOT, tex_root=ROOT)
hit = tot = 0
for r in rows:
    if r['where'] != 'IN-PAPER':
        continue
    m = re.match(r'receipts/(P\d+|p0)_', r['receipt'])
    home = MA.PAPER_OF_DIR.get(re.sub(r'^P0', 'P', m.group(1)))
    for f in r['figs']:
        last = f[-1]
        if not last.isdigit():
            continue
        for d in (-1, 1):
            g = f[:-1] + str((int(last) + d) % 10)
            if g == f:
                continue
            tot += 1
            hit += MA._in_tex(g, tex[home])
print(f'  IN-PAPER figures perturbed in the last digit: {hit} of {tot} perturbed tokens are ALSO printed by the '
      f'home paper = {100 * hit / tot:.1f} %  (the chance rate of an IN-PAPER verdict)')
for r in rows:
    if r['where'] in ('IN-NO-TEX', 'PARTLY-IN-TEX'):
        print(f"  [{r['read']}][{r['where']}] {r['receipt']}:{r['site']} {r['figs']} {r['label'][:90]}")

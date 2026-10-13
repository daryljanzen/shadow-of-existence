#!/usr/bin/env python3
"""r7279+70.1: the blinded sample.  25 FLAGGED drawn with seed 7279, and every UNFLAGGED site (23 < the 25 registered,
so all are taken), shuffled together.  Writes sample.tsv (blind: id, receipt path, claim, figures) and key.tsv (id, flag)."""
import os, random
import detector as D
HERE = os.path.dirname(os.path.abspath(__file__))
rows = D.sites()
fl = [r for r in rows if r[4]]
un = [r for r in rows if not r[4]]
rng = random.Random(7279)
pick = [(r, 'FLAGGED') for r in rng.sample(fl, 25)] + [(r, 'UNFLAGGED') for r in un[:25]]
rng.shuffle(pick)
with open(os.path.join(HERE, 'sample.tsv'), 'w', encoding='utf-8') as f, \
        open(os.path.join(HERE, 'key.tsv'), 'w', encoding='utf-8') as k:
    f.write('# id\treceipt_path\tfigures\tclaim\n')
    k.write('# id\tflag\tunpinned\n')
    for i, ((pop, paper, name, claim, u), flag) in enumerate(pick, 1):
        sid = f'F{i:02d}'
        figs = ' '.join(s for s, _ in D.figures(claim))
        f.write('\t'.join([sid, os.path.relpath(D.C.FILES[name], D.C.ROOT), figs,
                           f'[{pop} {paper}] ' + claim[:900].replace('\t', ' ')]) + '\n')
        k.write('\t'.join([sid, flag, ' '.join(u)]) + '\n')
print(len(fl), 'flagged', len(un), 'unflagged;', len(pick), 'drawn')

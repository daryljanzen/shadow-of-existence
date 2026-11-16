#!/usr/bin/env python3
"""r7815 (cc66) item ② -- the SENTENCE-TO-BANK CROSS behind the completed list.

`scan.py` finds every sentence in P15, P7, P18 and EXPLAINER.md that names the
control or prints one of the figures 69 named.  This file answers, for each of
them, the question the verdict turns on: **which control bank does the figure
come from, and what POINT is that bank at?**

The discriminator is `r7807+cc66`'s, inherited unchanged: a bank's `config`
records the FORM switches and not the background point, so the point is read off
each bank's own stored `(r_s, D_M)`, which are functions of the point alone.  The
four control points are read from banks in the tree rather than hardcoded, so if
one of them is ever re-pointed this cross follows it instead of lying.

What this file CANNOT do, stated so the hand-read knows where it starts:
 - a sentence that cites no receipt has no bank to trace, and 69's r7815 ruling
   is that exactly those sentences are what r7812's swap-log list missed.  They
   are listed as `NO RCPT` and hand-read in LIST.md.
 - a receipt that loads banks at two points (`lcdm_base.npz` spans tiers at one
   point -- the r7809 census's own admitted limitation) is reported with BOTH
   classes, never collapsed to one.
"""
import os, re, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
sys.path.insert(0, HERE)
import check_figures_pinned as F            # noqa: E402 -- the owning tool
from scan import DOCS, NAMES, FIG, NUM, sentences   # noqa: E402

# ── the four points, each read off a bank in the tree ───────────────────────────
POINT_BANKS = [
    ('UNREFIT',  'spectra/cc66_lcdm_L2000.npz'),
    ('REFIT185', 'spectra/cc66_r185_verify_lcdm.npz'),
    ('PLANCK',   'r7807_cc66_the_23_items_and_the_repointed_control/out/'
                 'r7807_control_planck2018_L2000.npz'),
]

def bg(path):
    try:
        z = np.load(path, allow_pickle=True)
    except Exception:
        return None
    if not ('r_s' in z.files and 'D_M' in z.files):
        return None
    try:
        return (round(float(z['r_s']), 6), round(float(z['D_M']), 6))
    except Exception:
        return None

POINTS = {}
for tag, rel in POINT_BANKS:
    p = os.path.join(BW, rel)
    s = bg(p)
    if s is None:
        print(f'  ⛔ reference point {tag} unreadable at {rel}')
    else:
        POINTS[s] = tag

# the full-range refit minimum has no single reference bank in the tree; it is
# taken from whichever bank the census found there, by its stored signature.
FULLREFIT = (145.403583, 13961.212948)
POINTS.setdefault(FULLREFIT, 'REFITFULL')

# ── every bank in the tree, with its arm and its point class ────────────────────
BANKS = {}                      # repo-relative bank path -> (arm, class)
for dirpath, _dirs, files in os.walk(BW):
    for fn in files:
        if not fn.endswith('.npz'):
            continue
        p = os.path.join(dirpath, fn)
        s = bg(p)
        try:
            z = np.load(p, allow_pickle=True)
            arm = str(z['arm']) if 'arm' in z.files else '?'
        except Exception:
            arm = '?'
        BANKS[os.path.relpath(p, BW)] = (arm, POINTS.get(s, 'OTHER' if s else 'NOBG'))

RCPT = re.compile(r'\\rcpt\{([^}]+)\}')
LIT = re.compile(r'[\'"]([^\'"]*\.npz)[\'"]')

CONSTRUCTED = set()             # literals that are f-string/format fragments


def resolve(lit):
    """Every walked bank whose repo-relative path ENDS with this literal.

    Resolving by path suffix and not by basename is what keeps
    `refit_grid185/lcdm_base.npz` apart from `grid_oneclock/lcdm_base.npz`:
    three banks share that basename at two different tiers, so a basename match
    cannot say which one a receipt loads.  A literal that is a format fragment
    ('{tag}.npz', '.npz') names no file at analysis time and is counted in
    CONSTRUCTED rather than reported as a bank.
    """
    lit = lit.lstrip('./')
    if '{' in lit or '%' in lit or lit in ('.npz', ''):
        CONSTRUCTED.add(lit)
        return set()
    hits = {p for p in BANKS if p == lit or p.endswith('/' + lit)}
    return hits


def banks_of(receipt_path):
    """the walked banks the receipt names in a STRING LITERAL, by path."""
    try:
        src = open(receipt_path, encoding='utf-8', errors='replace').read()
    except OSError:
        return set()
    out = set()
    for m in LIT.finditer(src):
        out |= resolve(m.group(1))
    return out

def main():
    rows = []
    for paper, rel in DOCS:
        text = open(os.path.join(ROOT, rel), encoding='utf-8').read()
        md = rel.endswith('.md')
        for ln, lab, s in sentences(text, md):
            if not (NAMES.search(s) or FIG.search(s)):
                continue
            if not NUM.findall(s) and not FIG.search(s):
                continue
            keys = RCPT.findall(s)
            classes, missing, bset = set(), [], set()
            for k in keys:
                path = F.FILES.get(k)
                if path is None:
                    missing.append(k)
                    continue
                for b in banks_of(path):
                    arm, cls = BANKS[b]
                    if arm in ('lcdm', '?'):
                        classes.add(cls)
                        bset.add(b)
            rows.append((paper, ln, lab, keys, classes, bset, missing, s))

    print(f'  {len(BANKS)} bank(s) walked; point classes seen: '
          f'{sorted({c for _a, c in BANKS.values()})}')
    print(f'  {len(CONSTRUCTED)} literal(s) are built at runtime and name no file statically: '
          f'{sorted(CONSTRUCTED)[:8]}')
    print(f'  reference signatures: ' + ', '.join(f'{t}={k}' for k, t in POINTS.items()))
    print()
    tally = {}
    for paper, ln, lab, keys, classes, bset, missing, s in rows:
        if not keys:
            verdict = 'NO RCPT'
        elif 'UNREFIT' in classes:
            verdict = 'UNREFIT'
        elif classes:
            verdict = '/'.join(sorted(classes))
        else:
            verdict = 'NO LCDM BANK'
        tally[verdict] = tally.get(verdict, 0) + 1
        flat = re.sub(r'\s+', ' ', re.sub(r'\\rcpt\{[^}]+\}', '', s))
        print(f'[{paper} l.{ln}] <{lab}>  ==> {verdict}')
        if classes:
            print(f'      classes={sorted(classes)}  banks={sorted(bset)}')
        if missing:
            print(f'      ⛔ rcpt key(s) with no receipt file: {missing}')
        print(f'      {flat[:300]}')
    print()
    for k in sorted(tally, key=lambda x: -tally[x]):
        print(f'  {tally[k]:4d}  {k}')
    print(f'  {len(rows):4d}  TOTAL')

if __name__ == '__main__':
    sys.exit(main())

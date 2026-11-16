#!/usr/bin/env python3
"""r7809 (cc66) -- WHICH PRINTED FIGURES READ THE LambdaCDM CONTROL AT ITS UN-REFITTED POINT.

** THE ORDER (r7809, 69) item (1): ** "Every P15 figure, and every P7, P18 and explainer figure
quoting one, that reads the LambdaCDM control at its un-refitted point.  Use the same method as the
PO-87 census: which receipts load which control bank, and which sentences cite them.  Report the
list whole, with each figure's value at the old point."

** THE DISCRIMINATOR, AND WHY IT IS MEASURED RATHER THAN GUESSED. **  `r7807+cc66` established that
a bank's `config` records the FORM switches and NOT the background point -- no `LH0`, `LOM`, `WBH2`
or `NS` -- so a bank cannot say which point it ran at through its config.  And `r7807` also recorded
the attribution trap: reading a bank's point off a RECIPE found the wrong recipe (a rebuild at a
replaced point) and off a FILENAME is a convention, not a measurement.
  => So the point is read off each bank's OWN STORED BACKGROUND: every bank carries `r_s`, `D_M` and
  `l_A`, which are functions of the point alone.  Two banks are at the same point iff their stored
  `(r_s, D_M)` agree.  The un-refitted signature is taken FROM `cc66_lcdm_L2000.npz` itself rather
  than hardcoded, so if that bank is ever re-pointed this census follows it instead of lying.

** THE DISTINCTION THIS CENSUS MUST NOT BLUR (r7667's lesson, inherited verbatim). **  A receipt
cited in `appendix_receipts_*.tex` is cited by the GENERATED registered-receipt list -- every
registered receipt is in there by construction.  That is not a sentence printing a figure.  Only a
citation in a paper BODY puts a figure in print.  `check_figures_pinned.sites()` already separates
those two populations, so its OWN source is executed here rather than reimplemented, and the
`PROSE` population is the one this census is keyed on.

Registered at PREDICTION.md in this directory, in its own commit, before this file existed.
"""
import ast
import glob
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
import check_figures_pinned as F  # noqa: E402  -- the owning tool's own sentence/figure reader

UNREFIT_BANK = os.path.join(BW, 'spectra', 'cc66_lcdm_L2000.npz')


def head(t):
    print('\n' + '=' * 100)
    print('  ' + t)
    print('=' * 100)


def _bg(path):
    """(r_s, D_M) as the bank itself stores them, or None when it stores no background."""
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


def _arm(path):
    try:
        z = np.load(path, allow_pickle=True)
    except Exception:
        return None
    if 'arm' not in z.files:
        return None
    try:
        return str(z['arm'].item()) if z['arm'].shape == () else str(z['arm'])
    except Exception:
        return str(z['arm'])


# ══ (A) the bank population, classified by its own stored background ════════════════════════════
head('(A) THE CONTROL BANKS, CLASSIFIED BY THE BACKGROUND EACH ONE STORES')

SIG = _bg(UNREFIT_BANK)
assert SIG is not None, 'cc66_lcdm_L2000.npz stores no r_s/D_M; the discriminator is gone'
print(f"\n  the un-refitted signature, read FROM cc66_lcdm_L2000.npz: r_s={SIG[0]}  D_M={SIG[1]}")

lcdm, at_old, elsewhere = {}, {}, {}
for p in sorted(glob.glob(os.path.join(ROOT, 'computations', '**', '*.npz'), recursive=True)):
    a = _arm(p)
    if a is None or 'lcdm' not in a.lower():
        continue
    rel = os.path.relpath(p, ROOT)
    bg = _bg(p)
    lcdm[rel] = bg
    (at_old if bg == SIG else elsewhere)[rel] = bg

print(f"  {len(lcdm)} bank(s) whose `arm` says lcdm; {len(at_old)} at the UN-REFITTED point, "
      f"{len(elsewhere)} elsewhere or storing no background")
print('\n  AT THE UN-REFITTED POINT (these are what item (1) is about):')
for r in sorted(at_old):
    print(f'      {r}')
print('\n  the named non-un-refitted controls, for contrast:')
for r in sorted(elsewhere):
    if any(k in r for k in ('verify', 'planck2018', 'refit')):
        print(f'      {r}   r_s/D_M={elsewhere[r]}')

OLD_BASENAMES = {os.path.basename(r) for r in at_old}
OLD_STEMS = {b[:-4] for b in OLD_BASENAMES}

# ══ (B) which receipts LOAD one, by their own source ═════════════════════════════════════════════
head('(B) WHICH RECEIPTS LOAD A BANK AT THE UN-REFITTED POINT')


def _literals(src):
    """every string literal in the file, so a path built by os.path.join is still seen"""
    out = set()
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return out
    for n in ast.walk(tree):
        if isinstance(n, ast.Constant) and isinstance(n.value, str):
            out.add(n.value)
    return out


def loads(path):
    """(banks named in a string literal, banks named only in prose/comments)"""
    try:
        src = open(path, encoding='utf-8', errors='replace').read()
    except OSError:
        return set(), set()
    lits = _literals(src)
    lit_hits, txt_hits = set(), set()
    for b in OLD_BASENAMES:
        stem = b[:-4]
        in_lit = any(b in s or stem == s or s.endswith('/' + b) for s in lits)
        in_txt = b in src or stem in src
        if in_lit:
            lit_hits.add(b)
        elif in_txt:
            txt_hits.add(b)
    return lit_hits, txt_hits


RECEIPTS = dict(F.FILES)          # name -> path, from the owning tool
loaders = {}
for name, path in RECEIPTS.items():
    lit, txt = loads(path)
    if lit or txt:
        loaders[name] = (lit, txt)
print(f"\n  {len(RECEIPTS)} registered receipt(s) scanned; {len(loaders)} name a bank at the "
      f"un-refitted point")
_lit_only = {n for n, (l, t) in loaders.items() if l}
_txt_only = {n for n, (l, t) in loaders.items() if not l}
print(f"      in a STRING LITERAL (a real load site): {len(_lit_only)}")
print(f"      only in prose or a comment (NOT a load): {len(_txt_only)}")

# ══ (C) which of those are cited by a BODY sentence that prints a figure ════════════════════════
head('(C) THE LIST: BODY SENTENCES THAT PRINT A FIGURE AND CITE SUCH A RECEIPT')

rows = []
for pop, paper, name, claim in F.sites():
    if pop != 'PROSE':
        continue
    if name not in _lit_only:
        continue
    figs = F.figures(claim)
    if not figs:
        continue
    rows.append((paper, name, [s for s, _ in figs], sorted(loaders[name][0]), claim))

papers = sorted({r[0] for r in rows})
recs = sorted({r[1] for r in rows})
nfig = sum(len(r[2]) for r in rows)
print(f"\n  {len(rows)} body site(s) in {len(papers)} paper(s), over {len(recs)} receipt(s), "
      f"printing {nfig} figure(s)")
print(f"  papers: {papers}")
for paper, name, figs, banks, claim in rows:
    print(f"\n  -- {paper}  <-  {name}")
    print(f"     banks at the old point it loads: {banks}")
    print(f"     figures printed: {figs}")
    print(f"     sentence: {claim[:300]}")

head('SUMMARY')
print(f"\n  (1a) printed figures on the list: {nfig}")
print(f"  (1b) receipts carrying them: {len(recs)}")
print(f"  (1c) papers other than CR_cosmology.tex: "
      f"{sorted(p for p in papers if p != 'CR_cosmology.tex')}")
print(f"  (1d) distinct banks at the old point that these receipts load: "
      f"{sorted({b for r in rows for b in r[3]})}")

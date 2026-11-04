#!/usr/bin/env python3
"""r7669 (cc66) ITEM 4 -- `c54.178`: THE WORK THE ORDER ASKS FOR IS NOT THERE, AND ITEM 3 IS WHY.

** THE ORDER (r7669, 69) item 4: ** "`c54.178`, the one live unrebuildable configuration, takes
r7637's ruling: its sentence is re-grounded on an arm-of-record figure or withdrawn.  Route the
sentence and the arm-of-record figure that would carry it."

** THE PREMISE DOES NOT HOLD, and the reason falls out of item 3. **  Resolved here:

  ⒜ 47 receipts MENTION `c54.178`; only 12 have a LOAD SITE that names it.  *Mentioning is not
    loading -- the same distinction `r7667+cc66.3` was built on, and the one my own arm ① of
    `r7669+cc66.0` fell for again.*
  ⒝ Of the 12, only THREE are cited by a body sentence, and ** all three load `c54.178_lcdm.npz` --
    the CONTROL leg, not the CR arm. **
  ⒞ `c54.178_lcdm_leafrec1.npz` DOES NOT EXIST, exactly as `classify.py`'s `Ⓐ①` says of every
    control leg.  ⇒ ** There is no arm-of-record figure to re-ground those sentences onto. **
  ⒟ And the receipts that DO load `c54.178_cr.npz` -- the CR arm, which is what the ruling is about
    -- are cited by NO body sentence at all.  `c54.178_cr_leafrec1.npz` exists, so had a sentence
    needed that figure it was available; none does.

⇒ ** So item 4 has no re-grounding work in it. **  The one body sentence that prints a figure from a
  `c54.178` read is a CONTROL read, which makes it item 3's case and not item 4's: it leaves the
  list if 70 reports that the switch does not touch the control, and nothing here counts it.
"""
import ast
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
SPEC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')

fail = []


def check(label, ok, got=None):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}" + (f"   ({got})" if got is not None else ""))
    if not ok:
        fail.append(label)


print('\n' + '=' * 100)
print('  r7669 ITEM 4 -- `c54.178`: WHO ACTUALLY READS IT, AND WHAT COULD RE-GROUND IT')
print('=' * 100 + '\n')

TEX = open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'),
           encoding='utf-8', errors='replace').read()
_NUM = re.compile(r'\d+\.\d+|\b\d{2,}\b')


def load_literals(src):
    """string literals that reach a `*.load(...)` call, directly or as f-string parts."""
    try:
        tr = ast.parse(src)
    except SyntaxError:
        return []
    out = []
    for n in ast.walk(tr):
        if not isinstance(n, ast.Call):
            continue
        f = n.func
        if (f.attr if isinstance(f, ast.Attribute) else getattr(f, 'id', '')) != 'load':
            continue
        for a in ast.walk(n):
            if isinstance(a, ast.Constant) and isinstance(a.value, str):
                out.append(a.value)
            elif isinstance(a, ast.JoinedStr):
                out += [v.value for v in a.values
                        if isinstance(v, ast.Constant) and isinstance(v.value, str)]
    return out


def sentences(base):
    out = []
    for m in re.finditer(re.escape('\\rcpt{' + base + '}'), TEX):
        a = TEX.rfind('. ', 0, m.start())
        a = 0 if a < 0 else a + 2
        b = TEX.find('. ', m.end())
        b = len(TEX) if b < 0 else b + 1
        out.append(re.sub(r'\s+', ' ', TEX[a:b]).strip())
    return out


mention, loaders = [], []
for p in sorted(glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True)):
    src = open(p, encoding='utf-8', errors='replace').read()
    if 'c54.178' not in src:
        continue
    rel = os.path.relpath(p, ROOT)
    mention.append(rel)
    lits = [s for s in load_literals(src) if 'c54.178' in s]
    if lits:
        loaders.append((rel, sorted(set(lits))))

print(f'      receipts MENTIONING `c54.178`                 : {len(mention)}')
print(f'      receipts whose LOAD SITE names it             : {len(loaders)}')
check('⓵ ⛭⛭ MENTIONING IS NOT LOADING, and the gap is most of the population: the great majority '
      'of receipts that name `c54.178` never load it -- they discuss it in a comment, a docstring '
      'or a provenance note',
      len(mention) > 3 * len(loaders) and len(loaders) >= 8,
      f'{len(loaders)} loaders of {len(mention)} mentions')

cited = [(r, l, sentences(os.path.basename(r)[:-3])) for r, l in loaders]
body = [(r, l, s) for r, l, s in cited if s]
print(f'      of the loaders, cited by a body sentence      : {len(body)}')
for r, l, s in body:
    print(f'        {os.path.basename(r)[:70]}')
    print(f'            loads: {l}')
check('⓶ ⛭⛭⛭ EVERY BODY-CITED `c54.178` LOADER READS THE CONTROL LEG, not the CR arm',
      len(body) == 3 and all(all('lcdm' in x for x in l) for _, l, _ in body),
      f'{len(body)} body-cited loaders, all reading c54.178_lcdm.npz')

cr_loaders = [r for r, l in loaders if any('c54.178_cr' in x for x in l)]
cr_cited = [r for r in cr_loaders if sentences(os.path.basename(r)[:-3])]
print(f'      loaders of the CR arm `c54.178_cr*`           : {len(cr_loaders)}')
print(f'        of those, cited by a body sentence          : {len(cr_cited)}')
check('⓷ ⛔ AND THE CR-ARM READS -- WHICH IS WHAT THE RULING IS ABOUT -- CARRY NO BODY SENTENCE AT '
      'ALL, so no figure in print rests on `c54.178`\'s CR arm',
      len(cr_loaders) >= 1 and len(cr_cited) == 0,
      f'{len(cr_loaders)} CR-arm loaders, {len(cr_cited)} of them body-cited')

have_cr_aor = os.path.exists(os.path.join(SPEC, 'c54.178_cr_leafrec1.npz'))
have_lcdm_aor = os.path.exists(os.path.join(SPEC, 'c54.178_lcdm_leafrec1.npz'))
print(f'      c54.178_cr_leafrec1.npz   exists: {have_cr_aor}')
print(f'      c54.178_lcdm_leafrec1.npz exists: {have_lcdm_aor}')
check('⓸ ⛭⛭⛭ THE RE-GROUNDING FIGURE THE ORDER ASKS FOR DOES NOT EXIST FOR THESE SENTENCES: the '
      'CR arm has a banked arm-of-record spectrum and the CONTROL has none -- so a control read '
      'cannot be re-grounded on an arm-of-record figure, there being none to re-ground onto',
      have_cr_aor and not have_lcdm_aor,
      'cr_leafrec1 present, lcdm_leafrec1 absent')

with_fig = [(r, s) for r, l, s in body if any(_NUM.search(x) for x in s)]
print(f'      of the three, whose citing sentence PRINTS a figure: {len(with_fig)}')
for r, s in with_fig:
    for x in s:
        if _NUM.search(x):
            print(f'        {os.path.basename(r)[:58]}')
            print(f'            "{x[:200]}"')
check('⓹ ⛭ SO ITEM 4 REDUCES TO ONE SENTENCE, shared by two receipts, and it is a control read: '
      '*"Most of the fitted headroom is recovered by a genuine lensing, and about $989$ of the '
      '$1320$ survives it"* -- figures `989` and `1320`',
      len(with_fig) == 2 and all('989' in ' '.join(s) for _, s in with_fig),
      f'{len(with_fig)} of {len(body)} print a figure, sharing one sentence')
check('⓺ ⛔⛭⛭ ⇒ ITEM 4 HAS NO RE-GROUNDING WORK, AND ITEM 3 IS WHY: the only figure in print that '
      'rests on a `c54.178` read rests on its CONTROL leg, which has no arm-of-record counterpart '
      'anywhere in the bank.  That makes it the order\'s ITEM 3 case -- a control-only read, which '
      'leaves the list if 70 reports the switch does not touch the control -- and NOT item 4\'s.  '
      '⚠ Nothing here counts it, per the order',
      len(with_fig) == 2 and not have_lcdm_aor and len(cr_cited) == 0,
      'routed to item 3, not re-grounded here')

print('\n' + '=' * 100)
if fail:
    print('  FAILED:')
    for f in fail:
        print(f'    - {f}')
    sys.exit(1)
print('  ✓ ALL CHECKS PASSED')
print('=' * 100)

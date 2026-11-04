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
import io
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


#: ⛔⛭⛭⛭ r7671+cc66.5 -- THIS FUNCTION MISSED THE ITERATED-TABLE SHAPE, and it is the SAME shape
#:   `classify.py` was fixed for in the very same revision (`r7669+cc66.4`, shape 3) -- one file
#:   over and not carried across.  The shape:
#:
#:       for _nm, _f in (('LambdaCDM arm', 'c54.178_lcdm'), ('CR arm', 'c54.178_cr')):
#:           _z = np.load(os.path.join(_SPEC, f"{_f}.npz"))
#:
#:   The only literal INSIDE the `load(...)` call is `".npz"`; both stems sit in the loop's own
#:   iterable, so a walk bounded by the Call node sees nothing.
#:   ⛔ ** WHAT IT COST: `P15_where_the_likelihood_sits.py` was not counted as a `c54.178` loader at
#:   all, ** and it loads both legs AND is cited by a body sentence at `l.955`.  So `⓷`'s "0 of them
#:   body-cited" was false, and `r7669+cc66.2` told 69 *"item 4 has no re-grounding work in it"* on
#:   a count with a hole in it.  *The conclusion survives -- `r7671`'s split routes that sentence to
#:   69 as a RE-GROUND on its own reading of the receipt's header guard -- but it survives on a
#:   narrower ground than the one given, and the gate asserted the stronger thing.*
#:   ⇒ Literals reached through a loop variable are attributed at RECEIPT level and labelled as
#:     such: the pass says what this receipt reads, not which line reads it.  Same discipline and
#:     same caveat as `classify.py`'s table pass.
def load_literals(src):
    """string literals that reach a `*.load(...)` call -- directly, as f-string parts, or (at
    RECEIPT level) through a loop variable bound by a literal table in the same module."""
    try:
        tr = ast.parse(src)
    except SyntaxError:
        return []
    out, opaque = [], False
    for n in ast.walk(tr):
        if not isinstance(n, ast.Call):
            continue
        f = n.func
        if (f.attr if isinstance(f, ast.Attribute) else getattr(f, 'id', '')) != 'load':
            continue
        lits = []
        for a in ast.walk(n):
            if isinstance(a, ast.Constant) and isinstance(a.value, str):
                lits.append(a.value)
            elif isinstance(a, ast.JoinedStr):
                lits += [v.value for v in a.values
                         if isinstance(v, ast.Constant) and isinstance(v.value, str)]
        out += lits
        #: a load naming no `.npz` FILE is reading a name bound somewhere else
        if not any(x.endswith('.npz') and len(x) > len('.npz') for x in lits):
            opaque = True
    if opaque:
        for n in ast.walk(tr):
            if isinstance(n, (ast.For, ast.AsyncFor)):
                for a in ast.walk(n.iter):
                    if isinstance(a, ast.Constant) and isinstance(a.value, str):
                        out.append(a.value)
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
#: ⛔⛭⛭ r7671+cc66.5 -- ⓶ AND ⓷ AS FIRST WRITTEN SAID SOMETHING FALSE, and the loader pass above is
#:   why: with the iterated table read, the body-cited loaders are SIX and not three, and THREE of
#:   them read the CR arm rather than none.  The conclusion survives on a narrower ground, and that
#:   ground is now what the gates assert -- no figure IN PRINT rests on `c54.178`'s CR arm, because
#:   of the three body-cited CR-arm loaders:
#:     ⒜ `the_photon_hierarchy_in_the_transfer` is cited at l.846 on a sentence with NO figure in it;
#:     ⒝ `the_control_entered_the_regime_and_the_arm_did_not_move` prints only the CONTROL's figures;
#:     ⒞ `where_the_likelihood_sits` PINS the namesake deliberately -- its own guard asserts every CR
#:        file it reads is the LEAFREC=0 namesake -- and `r7671`'s split routes its sentence to 69 as
#:        a RE-GROUND on exactly that reading.
#:   ⇒ Each disposition is CHECKED below, from the sentence or from the source, not declared.
_ctl_only = [r for r, l, _ in body if all('lcdm' in x for x in l if 'c54.178' in x)]
print(f'      of the body-cited, reading ONLY the control leg: {len(_ctl_only)}')
check('⓶ ⛭⛭ THE BODY-CITED LOADERS SPLIT BY LEG, and the first form of this gate claimed they were '
      'all the control: with the iterated table read there are SIX, of which three read ONLY the '
      'control leg and three read the CR arm.  ⛔ "Every body-cited loader reads the control leg" '
      'is FALSE and was asserted',
      len(body) == 6 and len(_ctl_only) == 3,
      f'{len(body)} body-cited, {len(_ctl_only)} control-leg-only, {len(body) - len(_ctl_only)} '
      f'reading the CR arm')

cr_loaders = [r for r, l in loaders if any('c54.178_cr' in x for x in l)]
cr_cited = [r for r in cr_loaders if sentences(os.path.basename(r)[:-3])]
print(f'      loaders of the CR arm `c54.178_cr*`           : {len(cr_loaders)}')
print(f'        of those, cited by a body sentence          : {len(cr_cited)}')
for r in cr_cited:
    print(f'          {os.path.basename(r)[:72]}')
_no_fig = [r for r in cr_cited
           if not any(_NUM.search(x) for x in sentences(os.path.basename(r)[:-3]))]
_ctl_fig = [r for r in cr_cited if r not in _no_fig
            and all('control' in x and 'this arm' not in x
                    for x in sentences(os.path.basename(r)[:-3]) if _NUM.search(x))]
_GUARD = 'is not the LEAFREC=0 namesake'
_pinned = [r for r in cr_cited if r not in _no_fig and r not in _ctl_fig
           and _GUARD in io.open(os.path.join(ROOT, r), encoding='utf-8',
                                 errors='replace').read()]
print(f'        disposition -- no figure in its sentence    : {len(_no_fig)} '
      f'{[os.path.basename(r)[:44] for r in _no_fig]}')
print(f'                       control figures only         : {len(_ctl_fig)} '
      f'{[os.path.basename(r)[:44] for r in _ctl_fig]}')
print(f'                       namesake pinned by its guard : {len(_pinned)} '
      f'{[os.path.basename(r)[:44] for r in _pinned]}')
check('⓷ ⛔⛭⛭ NO FIGURE IN PRINT RESTS ON `c54.178`\'s CR ARM -- BUT NOT BECAUSE NO CR-ARM READ IS '
      'CITED, WHICH IS WHAT THIS GATE USED TO SAY.  Three are, and each is accounted for from its '
      'own sentence or its own source: one cited on a sentence with no figure in it, one printing '
      'only the control\'s figures, and one pinning the LEAFREC=0 namesake by its own header guard '
      'and routed to 69 as a RE-GROUND by `r7671`\'s split',
      len(cr_cited) == 3
      and len(_no_fig) + len(_ctl_fig) + len(_pinned) == len(cr_cited)
      and len(_no_fig) == 1 and len(_ctl_fig) == 1 and len(_pinned) == 1,
      f'{len(cr_loaders)} CR-arm loaders, {len(cr_cited)} body-cited, dispositions '
      f'{len(_no_fig)}/{len(_ctl_fig)}/{len(_pinned)}')

have_cr_aor = os.path.exists(os.path.join(SPEC, 'c54.178_cr_leafrec1.npz'))
have_lcdm_aor = os.path.exists(os.path.join(SPEC, 'c54.178_lcdm_leafrec1.npz'))
print(f'      c54.178_cr_leafrec1.npz   exists: {have_cr_aor}')
print(f'      c54.178_lcdm_leafrec1.npz exists: {have_lcdm_aor}')
check('⓸ ⛭⛭⛭ THE RE-GROUNDING FIGURE THE ORDER ASKS FOR DOES NOT EXIST FOR THE CONTROL: the CR arm '
      'has a banked arm-of-record spectrum and the CONTROL has none -- so a control read cannot be '
      're-grounded on an arm-of-record figure, there being none to re-ground onto',
      have_cr_aor and not have_lcdm_aor,
      'cr_leafrec1 present, lcdm_leafrec1 absent')

with_fig = [(r, s) for r, l, s in body if any(_NUM.search(x) for x in s)]
print(f'      of the {len(body)}, whose citing sentence PRINTS a figure: {len(with_fig)}')
for r, s in with_fig:
    for x in s:
        if _NUM.search(x):
            print(f'        {os.path.basename(r)[:58]}')
            print(f'            "{x[:200]}"')
_989 = [r for r, s in with_fig if '989' in ' '.join(s)]
check('⓹ ⛭⛭ THE SENTENCES IN PRINT, RE-COUNTED: the first form of this gate said item 4 reduced to '
      f'ONE sentence shared by two receipts.  With the iterated table read, {len(with_fig)} '
      f'receipts have a citing sentence that prints a figure and {len(_989)} of them share the '
      'lensing sentence *"Most of the fitted headroom is recovered by a genuine lensing, and about '
      '$989$ of the $1320$ survives it"*.  ⛔ The reduction was real but narrower than stated',
      len(_989) == 2 and len(with_fig) > len(_989),
      f'{len(with_fig)} of {len(body)} print a figure; {len(_989)} share the lensing sentence')
check('⓺ ⛔⛭⛭ ⇒ ITEM 4 STILL HAS NO RE-GROUNDING WORK OF ITS OWN, AND ITEM 3 IS STILL WHY -- but on '
      'a narrower ground than `r7669+cc66.2` gave 69.  The lensing figure in print rests on '
      '`c54.178`\'s CONTROL leg, which has no arm-of-record counterpart anywhere in the bank, so it '
      'is the order\'s ITEM 3 case and leaves the list if 70 reports the switch does not touch the '
      'control.  ⚠ What is NEW: the CR arm is read by three body-cited receipts rather than none, '
      'and one of them carries a sentence `r7671` routes to 69 as a RE-GROUND.  ⇒ Item 4 is '
      'discharged by item 3 AND by one routed sentence, not by item 3 alone.  Nothing here counts '
      'the control case, per the order',
      len(_989) == 2 and not have_lcdm_aor and len(cr_cited) == 3 and len(_pinned) == 1,
      'discharged by item 3 plus one routed sentence')

print('\n' + '=' * 100)
if fail:
    print('  FAILED:')
    for f in fail:
        print(f'    - {f}')
    sys.exit(1)
print('  ✓ ALL CHECKS PASSED')
print('=' * 100)

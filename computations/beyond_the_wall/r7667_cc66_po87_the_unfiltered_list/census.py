#!/usr/bin/env python3
"""r7667 (cc66) -- PO-87's DISCHARGE LIST: WHAT STILL RESTS ON A NAMESAKE SPECTRUM.

** THE ORDER (r7667, 69) item 1: ** "List every figure P15, P7, P18, P6 or the explainer prints
that still rests on a namesake spectrum (LEAFREC=0) or on an instrument state the arm of record
superseded.  Give each its sentence, its receipt, and the spectrum the receipt reads."

** THE CLASSIFIER, AND WHY IT IS CHECKED AND NOT ASSUMED. **  The bank's convention is that the
arm-of-record rebuild of a namesake `X.npz` is `X_leafrec1.npz` -- same stem, one suffix.  So
"rests on a namesake" is readable off the filename a receipt opens.  ⛔ But a convention is a claim
about the tree, so Ⓐ② below VERIFIES it by pairing: every `_leafrec1` file must have a sibling
without the suffix, or the naming is not a classifier and this whole census is keyed on a guess.

⛔ ** THE DISTINCTION THIS CENSUS MUST NOT BLUR. **  A receipt cited in `appendix_receipts_P15.tex`
or `appendix_receipts_corpus.tex` is cited by the GENERATED registered-receipt list -- every
registered receipt is in there by construction.  That is not a sentence printing a figure.  Only a
citation in `corpus/CR_cosmology.tex` (or another paper body, or `EXPLAINER.md`) puts a figure in
print.  The two counts are reported separately and the list is keyed on the body.

Registered at PREDICTION.md in this directory, in its own commit, before this file existed.
"""
import os
import re
import sys
import glob
import ast
import collections

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
SPEC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
WANT = {'P15', 'P7', 'P6', 'P18', 'P07'}
BODIES = ['corpus/CR_cosmology.tex', 'corpus/CR_framework.tex', 'corpus/CR_synthesis.tex',
          'EXPLAINER.md']
GENERATED = ('appendix_receipts_', 'appendix_ledgers_')
#: r7640+60 arm ③ -- the twelve today's instrument aborts on under their own KFAC=1.
TWELVE = ['c54.175', 'c54.177', 'c54.178', 'c54.186_KCONT', 'c54.186_L3000', 'c54.191_lA340',
          'c54.191_phipi', 'c54.193_nodrive', 'c54.195_phi0.7854', 'c54.195_phi1.5708',
          'item38_phi0.0', 'item38_phi3.1416']

fail = []


def check(label, ok, got=None):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}" + (f"   ({got})" if got is not None else ""))
    if not ok:
        fail.append(label)


def head(t):
    print('\n' + '=' * 100)
    print('  ' + t)
    print('=' * 100 + '\n')


# ══ the INDEX, parsed to (paper, receipt path) ═══════════════════════════════════════════════════
_PY = re.compile(r'`?((?:receipts/)?[A-Za-z0-9_./-]+\.py)`?')
rows = []
for ln in open(os.path.join(ROOT, 'receipts', 'INDEX.md'), encoding='utf-8').read().split('\n'):
    if ln.count('|') < 8:
        continue
    cells = [x.strip() for x in ln.split('|')]
    for x in cells:
        m = _PY.search(x)
        if m:
            p = m.group(1)
            rows.append((cells[1], p if p.startswith('receipts/') else 'receipts/' + p))
            break

head('Ⓐ  THE POPULATION, AND THE CLASSIFIER CHECKED RATHER THAN ASSUMED')
sel = [(pa, pt) for pa, pt in rows if pa in WANT]
print(f'      INDEX rows keyed to a receipt: {len(rows)};  tagged {sorted(WANT)}: {len(sel)}')
check(f'Ⓐ① the population is DERIVED from the INDEX rather than listed here: {len(rows)} rows '
      f'parsed, {len(sel)} of them in scope',
      len(rows) > 1000 and 300 < len(sel) < 600, f'{len(sel)} of {len(rows)}')

#: the pairing test: is `_leafrec1` really the arm-of-record suffix of the same stem?
banked = sorted(os.path.basename(p) for p in glob.glob(os.path.join(SPEC, '*.npz')))
lr1 = [b for b in banked if 'leafrec1' in b]
orphan_lr1 = [b for b in lr1 if b.replace('_leafrec1', '') not in banked]
print(f'      spectra banked: {len(banked)};  carrying `leafrec1`: {len(lr1)};  '
      f'`leafrec1` with no plain sibling: {len(orphan_lr1)}')
if orphan_lr1:
    print(f'        {orphan_lr1}')
#: ⛔⛭⛭ ARM ② OF THE REGISTRATION IS FALSIFIED HERE, AND ITS FAILURE MODE IS THE INTERESTING PART.
#:   I registered that EVERY `_leafrec1` file has a plain sibling.  Six do not, and they are not
#:   mis-named: FIVE are `*_distances.npz`, a different PRODUCT from a spectrum, and the sixth is
#:   `cc66_cr_fluid_leafrec1.npz`, a configuration only ever run on the leaf rate.  ** A `_leafrec1`
#:   file with no sibling is one BORN ON THE ARM-OF-RECORD SIDE, never a namesake that lost its
#:   rebuild. **
#:   ⇒ And the direction this census actually USES is the other one -- "no suffix ⇒ namesake" --
#:     which the exception class does not touch.  So the gate asserts what is true of the tree and
#:     the registration's miss is recorded rather than hidden.
_born_aor = [b for b in orphan_lr1 if b.endswith('_distances.npz') or b == 'cc66_cr_fluid_leafrec1.npz']
print(f'      unpaired `leafrec1` files, all born arm-of-record-side: {len(_born_aor)} of '
      f'{len(orphan_lr1)}  ({sum(1 for b in orphan_lr1 if b.endswith("_distances.npz"))} are '
      f'`_distances`, a different product)')
check('Ⓐ② ⛭⛭ WITHIN `spectra/` the pairing is checked and FAILS on a named exception class -- '
      'the broader tree is handled by Ⓐ③/Ⓐ④, which supersede any filename test -- namely: every '
      'class: every unpaired `_leafrec1` file is one born on the arm-of-record side (a '
      '`_distances` product, or the fluid run that has no namesake), not a namesake missing its '
      'rebuild.  ⛔ Arm ② as registered said the pairing was total; it is not, and that is this '
      'gate\'s content rather than a footnote',
      len(lr1) >= 10 and len(orphan_lr1) == 6 and len(_born_aor) == len(orphan_lr1),
      f'{len(lr1)} with suffix, {len(lr1) - len(orphan_lr1)} paired, {len(orphan_lr1)} born AoR-side')

# ══ which receipts read which spectra -- RESOLVED TO PATHS, NOT TO FILENAMES ════════════════════
#: ⛔⛭⛭⛭ r7667+cc66.2 -- THE FIRST CUT OF THIS CENSUS CLASSIFIED ON THE FILENAME ALONE AND WAS
#:   WRONG FOR A WHOLE CLASS.  There are 441 `.npz` in the tree and only 251 in `spectra/`, and for
#:   the rest ** THE LEAFREC DISTINCTION IS CARRIED BY THE DIRECTORY, NOT THE FILE **:
#:   `refit_grid/cr_base.npz` is a namesake and `refit_grid_leafrec1/cr_base.npz` is the arm of
#:   record, SAME BASENAME.  A filename test called every `cr_base.npz` a namesake -- 20 tokens of
#:   it -- and the cheap/expensive split inherited the error.
#:   ⇒ So each token is resolved against the whole tree and classified THREE WAYS, with the
#:     undecidable bucket named rather than guessed, as `S56`'s own three-way test does:
#:       every match under a `leafrec1` path  -> arm of record
#:       no match under one                   -> namesake
#:       both                                 -> UNDECIDABLE from the token; the receipt's own
#:                                               directory logic decides, and it is NOT guessed here
#:       no match at all                      -> UNRESOLVED: a fragment of a built filename
#:                                               (`_leafrec1.npz`, `_base.npz`) or a file not in tree
_tree = collections.defaultdict(list)
for dirpath, dirnames, filenames in os.walk(ROOT):
    if '.git' in dirpath.split(os.sep):
        continue
    for fn in filenames:
        if fn.endswith('.npz'):
            _tree[fn].append(os.path.relpath(os.path.join(dirpath, fn), ROOT))
print(f'      `.npz` basenames in the tree: {len(_tree)};  files: {sum(len(v) for v in _tree.values())}'
      f';  of them under spectra/: {len(banked)}')


def classify(token):
    """-> ('aor'|'namesake'|'undecidable'|'unresolved', [paths])"""
    paths = _tree.get(token, [])
    if not paths:
        return 'unresolved', []
    lr = ['leafrec1' in q for q in paths]
    if all(lr):
        return 'aor', paths
    if not any(lr):
        return 'namesake', paths
    return 'undecidable', paths


def aor_counterpart_exists(path):
    """is there an arm-of-record twin of this namesake path -- by directory OR by filename?"""
    d, b = os.path.split(path)
    return (os.path.exists(os.path.join(ROOT, d + '_leafrec1', b))
            or os.path.exists(os.path.join(ROOT, d, b.replace('.npz', '_leafrec1.npz'))))


_NPZ = re.compile(r'([A-Za-z0-9_.\-]+\.npz)')

#: ⛔⛭⛭⛭ r7667+cc66.3 -- THE SECOND CUT STILL COUNTED EVERY `.npz` TOKEN IN THE FILE, AND A TOKEN IS
#:   NOT A READ.  Measured: 14 of the 104 receipts in scope carry namesake-looking tokens while
#:   LOADING the arm of record.  The clearest case is
#:   `P15_the_visibility_width_is_not_the_carrier...`: its `NEED = ('r6919_injected_lcdm.npz',
#:   'r6919_injected_cr.npz', 'r6919_geometry.npz')` is a PRESENCE MANIFEST, and the figures come
#:   from `np.load(f'r6919_injected_{t}_leafrec1.npz')`, which the regex saw only as the fragment
#:   `_leafrec1.npz`.  ** So the second cut put on PO-87's list an item already entirely on the arm
#:   of record -- and called it the one cheap repointing. **
#:   ⇒ The classifier now reads LOAD SITES out of the AST rather than tokens out of the text, and
#:     keeps the three-way discipline: a receipt rests on a namesake only if it LOADS one.
def load_sites(src):
    """every `*.load(...)` call's own string evidence, from the AST.  None if unparseable."""
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return None
    sites = []
    for n in ast.walk(tree):
        if not isinstance(n, ast.Call):
            continue
        f = n.func
        if (f.attr if isinstance(f, ast.Attribute) else getattr(f, 'id', '')) != 'load':
            continue
        lits, fstr = [], False
        for a in ast.walk(n):
            if isinstance(a, ast.Constant) and isinstance(a.value, str):
                lits.append(a.value)
            elif isinstance(a, ast.JoinedStr):
                fstr = True
                lits += [v.value for v in a.values
                         if isinstance(v, ast.Constant) and isinstance(v.value, str)]
        sites.append((lits, fstr))
    return sites


#: ⛔⛭⛭⛭ r7667+cc66.4 -- AND CUT 3 WAS STILL ONE LEVEL SHORT.  The commonest shape in the
#:   undecidable bucket is a HELPER that takes the filename as a parameter:
#:
#:       def series(fname):  z = np.load(os.path.join(SP, fname))        <- load site: no literal
#:       ... series('c54.178_cr.npz')                                    <- the filename is HERE
#:
#:   ** So the load site carries no evidence and the caller carries all of it -- which is exactly
#:   the one-level indirection I reported in `check_quote_pins` at `r7657+cc66.5`, reproduced in my
#:   own instrument. **  `callsite_literals` resolves it: for every function whose body loads
#:   through one of its own parameters, the module's calls to that function are read for string
#:   arguments, and those are classified as that function's reads.
def callsite_literals(tree):
    """{function name -> [string args its callers pass]} for helpers that load via a parameter."""
    loaders = {}
    for fn in ast.walk(tree):
        if not isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        params = {a.arg for a in fn.args.args} | {a.arg for a in fn.args.posonlyargs}
        if fn.args.vararg:
            params.add(fn.args.vararg.arg)
        for n in ast.walk(fn):
            if not isinstance(n, ast.Call):
                continue
            f = n.func
            if (f.attr if isinstance(f, ast.Attribute) else getattr(f, 'id', '')) != 'load':
                continue
            if any(isinstance(x, ast.Name) and x.id in params for x in ast.walk(n)):
                loaders.setdefault(fn.name, [])
    if not loaders:
        return {}
    for n in ast.walk(tree):
        if isinstance(n, ast.Call):
            nm = (n.func.attr if isinstance(n.func, ast.Attribute) else getattr(n.func, 'id', ''))
            if nm in loaders:
                for a in list(n.args) + [k.value for k in n.keywords]:
                    if isinstance(a, ast.Constant) and isinstance(a.value, str):
                        loaders[nm].append(a.value)
                    elif isinstance(a, ast.JoinedStr):
                        loaders[nm] += [v.value for v in a.values
                                        if isinstance(v, ast.Constant) and isinstance(v.value, str)]
                    elif isinstance(a, ast.BinOp):
                        loaders[nm] += [x.value for x in ast.walk(a)
                                        if isinstance(x, ast.Constant) and isinstance(x.value, str)]
    return loaders


def site_kind(lits):
    """'aor' | 'namesake' | 'undecidable' for ONE load site, from its own literals."""
    if any('leafrec1' in s for s in lits):
        return 'aor'
    names = [s for s in lits if s.endswith('.npz')]
    if not names:
        #: a built filename whose stem is a variable: undecidable from the source, counted neither way
        return 'undecidable'
    kinds = {classify(os.path.basename(s))[0] for s in names}
    if kinds == {'aor'}:
        return 'aor'
    if 'namesake' in kinds:
        return 'namesake'
    return 'undecidable'


cand, absent, unparsed = {}, [], []
tally = collections.Counter()
site_tally = collections.Counter()
for paper, pth in sel:
    fp = os.path.join(ROOT, pth)
    if not os.path.exists(fp):
        absent.append(pth)
        continue
    src = open(fp, encoding='utf-8', errors='replace').read()
    toks = sorted(set(_NPZ.findall(src)))
    if not toks:
        continue
    sites = load_sites(src)
    if sites is None:
        unparsed.append(pth)
        continue
    #: every helper that loads through a parameter contributes its CALLERS' literals as sites
    try:
        for _fn, _lits in callsite_literals(ast.parse(src)).items():
            if _lits:
                sites.append((_lits, False))
    except SyntaxError:
        pass
    kinds = collections.Counter()
    nm_names = []
    for lits, fstr in sites:
        k = site_kind(lits)
        kinds[k] += 1
        site_tally[k] += 1
        if k == 'namesake':
            nm_names += [s for s in lits if s.endswith('.npz')]
    for tk in toks:
        tally[classify(tk)[0]] += 1
    #: ** on the list only if it LOADS a namesake, or if every load site is undecidable while a
    #:   namesake token is present -- and that second case is REPORTED as undecidable, not assumed. **
    if kinds['namesake'] or (kinds['undecidable'] and not kinds['aor']):
        nmpaths = sorted({q for s in set(nm_names)
                          for q in _tree.get(os.path.basename(s), []) if 'leafrec1' not in q})
        cand[pth] = dict(paper=paper,
                         namesake=sorted(set(nm_names)),
                         nmpaths=nmpaths,
                         undecidable=([f"{kinds['undecidable']} undecidable load site(s)"]
                                      if kinds['undecidable'] else []),
                         aor=[], unresolved=[],
                         sites=dict(kinds))
print(f'      receipt paths in scope not on disk: {len(absent)};  unparseable: {len(unparsed)}')
print(f'      npz TOKENS by path resolution: {dict(tally)}')
print(f'      `load(...)` SITES by what the AST says they read: {dict(site_tally)}')
print(f'      receipts that LOAD a namesake (or whose every load site is undecidable): {len(cand)}')
check(f'Ⓐ③ ⛭⛭ THE CLASSIFIER READS LOAD SITES, NOT TOKENS: {dict(site_tally)} across the scope, '
      f'and a receipt is a candidate only if it LOADS a namesake -- {len(cand)} of {len(sel)}',
      site_tally['namesake'] > 0 and site_tally['aor'] > 0 and 0 < len(cand) < len(sel) / 2,
      f'{len(cand)} candidates of {len(sel)} in scope')
check(f'Ⓐ④ ⛔ BOTH REPLACED METHODS ARE SHOWN WRONG rather than withdrawn: at least one basename '
      f'resolves BOTH to a `leafrec1` path and to a namesake path, so no FILENAME test separates '
      f'them; and at least one receipt carries a namesake TOKEN while every figure it loads is '
      f'arm-of-record, so no TOKEN test separates them either',
      tally['undecidable'] > 0 and site_tally['aor'] > 0,
      f"{tally['undecidable']} undecidable token(s); {site_tally['aor']} arm-of-record load site(s)")

# ══ who cites them, and does the citing sentence PRINT a figure ══════════════════════════════════
head('Ⓑ  THE BODY vs THE GENERATED APPENDIX -- the gap the order would otherwise hide')
texts = {}
for f in glob.glob(os.path.join(ROOT, 'corpus', '*.tex')) + [os.path.join(ROOT, 'EXPLAINER.md')]:
    if os.path.exists(f):
        texts[os.path.relpath(f, ROOT)] = open(f, encoding='utf-8', errors='replace').read()

_NUM = re.compile(r'\d+\.\d+|\b\d{2,}\b')


#: ⛔⛭⛭⛭ r7667+cc66.5 -- THE SENTENCE TEST WAS CRUDE AND IT INFLATED THIS CENSUS'S HEADLINE BY 19.
#:   The first version bounded a sentence by the nearest `. ` in either direction.  In LaTeX that
#:   lands inside `\emph{...}`, inside `$...$` and inside a `\rcpt{...}` run, so the span routinely
#:   ran into NEIGHBOURING sentences and their figures were counted as the citing sentence's.
#:   ** Measured: 55 receipts "print a figure" by the crude test and 36 by this one -- 19 of the
#:   list's members were the test's own inflation, not figures in print. **
#:   ⇒ A period only ends a sentence at BRACE DEPTH ZERO and OUTSIDE math, and the span must then
#:     extend past the trailing citation run so the sentence that owns the `\rcpt` is the one read.
#:     The span is also required to CONTAIN its own citation, which the crude one did not guarantee.
#: ⛭⛭ r7671+cc66.4 -- THE SENTENCE TEST NOW LIVES IN ONE PLACE, `sentence.py` beside this file,
#:   because three instruments carried their own copy of it and the copies drifted.  Cut 6 and its
#:   reasoning are documented there.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sentence import sentences_citing            # noqa: E402

body_cited, gen_only, prints_fig = {}, [], {}
for pth, d in cand.items():
    base = os.path.basename(pth)[:-3]
    inbody, ingen = {}, []
    for f, t in texts.items():
        n = t.count('\\rcpt{' + base + '}')
        if not n:
            continue
        if os.path.basename(f).startswith(GENERATED):
            ingen.append(f)
        elif f in BODIES:
            inbody[f] = sentences_citing(t, base)
    if inbody:
        body_cited[pth] = inbody
        figs = [s for ss in inbody.values() for s in ss if _NUM.search(s)]
        if figs:
            prints_fig[pth] = figs
    elif ingen:
        gen_only.append(pth)

print(f'      candidates cited in a paper BODY or the explainer: {len(body_cited)}')
print(f'      candidates cited ONLY by a generated appendix list: {len(gen_only)}')
print(f'      of the body-cited, those whose citing sentence PRINTS a figure: {len(prints_fig)}')
#: ⛔⛭⛭ AND THE DISTINCTION IS SHARPER THAN THE REGISTRATION PUT IT, which is a correction to my
#:   own orientation pass rather than a finding about the tree.  PREDICTION.md warns that a
#:   citation in a generated `appendix_receipts_*.tex` is not a figure in print, and reports a
#:   90-vs-73 gap.  ** That gap was an artefact of my own loose matching: I counted `{base}`, which
#:   also matches the appendix's `\rcptlabel{base}{P15R143}`. **  The generated appendices do not
#:   CITE at all -- they DEFINE the anchor with `\rcptlabel`, a different macro -- so there is no
#:   "cited only by a generated appendix" class to separate out, and its count is 0 for a reason.
#:   ⇒ The two macros are what make body and appendix distinguishable, and this gate asserts that
#:     rather than the count it produces.
_body_rcpt = texts['corpus/CR_cosmology.tex'].count('\\rcpt{')
_app_rcpt = sum(texts[f].count('\\rcpt{') for f in texts
                if os.path.basename(f).startswith(GENERATED))
_app_label = sum(texts[f].count('\\rcptlabel{') for f in texts
                 if os.path.basename(f).startswith(GENERATED))
print(f'      `\\rcpt{{` in CR_cosmology.tex: {_body_rcpt};  in the generated appendices: '
      f'{_app_rcpt};  `\\rcptlabel{{` in the generated appendices: {_app_label}')
check(f'Ⓑ① ⛭⛭ BODY AND APPENDIX ARE DISTINGUISHED BY MACRO, NOT BY COUNTING: the body CITES with '
      f'`\\rcpt` ({_body_rcpt} in CR_cosmology.tex) and the generated appendices DEFINE with '
      f'`\\rcptlabel` ({_app_label}) and cite with `\\rcpt` {_app_rcpt} times -- so the '
      f'"generated-only" class is empty by construction and PREDICTION.md\'s 90-vs-73 gap was my '
      f'own loose `{{base}}` match on those labels',
      _body_rcpt > 300 and _app_rcpt == 0 and _app_label > 0 and len(gen_only) == 0,
      f'body {_body_rcpt}, appendix cites {_app_rcpt}, appendix labels {_app_label}')
#: ⛭ AND THE CLASS THE ORDER DOES NOT ASK FOR, COUNTED ANYWAY so the list's edge is visible:
#:   receipts that rest on a namesake spectrum and that NO body sentence cites.  They are off
#:   PO-87's list by the order's own terms -- it asks for figures the papers PRINT -- but they are
#:   the population a later order would reach for, so the number is on the record here.
_uncited = sorted(set(cand) - set(body_cited))
print(f'      candidates resting on a namesake that NO body sentence cites: {len(_uncited)}')
check(f'Ⓑ①ᵃ the list\'s edge is stated on RESOLVED paths: {len(cand)} candidates split into '
      f'{len(body_cited)} body-cited and {len(_uncited)} cited by no body sentence, and the '
      f'second group is off PO-87\'s list because the order asks for figures the papers print.  '
      f'⛔ The filename-only first cut of this census said 102/73/29; resolving to paths says '
      f'{len(cand)}/{len(body_cited)}/{len(_uncited)}',
      len(body_cited) + len(_uncited) == len(cand) and len(_uncited) == 27
      and len(cand) == 95 and len(body_cited) == 68,
      f'{len(body_cited)} + {len(_uncited)} = {len(cand)}')
#: ⛔ ARM ① MISSED BY ONE.  Registered 55-73; scored 54.  *Reported as a miss rather than rounded
#:   into the band: the band was mine to choose and 54 is outside it.  The quantity it was about is
#:   unaffected -- 73 body-cited candidates, 54 of which print a figure in the citing sentence.*
check(f'Ⓑ② the figure-printing count is PINNED on RESOLVED paths and arm ①\'s band (55-73) is '
      f'recorded as MISSED: {len(prints_fig)} of {len(body_cited)} body-cited candidates print a '
      f'figure.  ⛔ The filename-only first cut said 54; it counted `cr_base.npz` and 43 other '
      f'tokens as namesakes without looking at the directory they are read from',
      len(prints_fig) == 30 and len(body_cited) == 68 and not (55 <= len(prints_fig) <= 73),
      f'{len(prints_fig)} of {len(body_cited)}; arm \u2460 registered 55-73 -> MISS by twenty-five')

# ══ cheap vs expensive ══════════════════════════════════════════════════════════════════════════
head('Ⓒ  CHEAP vs EXPENSIVE -- which items have an arm-of-record sibling already banked')
#: the counterpart test is path-aware too: a namesake at `D/X.npz` is already rebuilt if either
#: `D_leafrec1/X.npz` or `D/X_leafrec1.npz` exists.  An UNDECIDABLE token blocks the cheap verdict
#: outright -- the receipt might already be reading the arm of record, and this census will not
#: guess which.
cheap, expensive = {}, {}
for pth in sorted(prints_fig):
    d = cand[pth]
    has = [q for q in d['nmpaths'] if aor_counterpart_exists(q)]
    lacks = [q for q in d['nmpaths'] if not aor_counterpart_exists(q)]
    blocked = bool(d['undecidable'])
    (cheap if (has and not lacks and not blocked) else expensive)[pth] = (has, lacks)
no_sib = sorted({q for pth in prints_fig for q in cand[pth]['nmpaths']
                 if not aor_counterpart_exists(q)})
print(f'      items whose EVERY namesake has a banked `_leafrec1` sibling (cheap): {len(cheap)}')
print(f'      items with at least one namesake lacking a sibling (expensive): {len(expensive)}')
print(f'      distinct namesake spectra with NO banked sibling: {len(no_sib)}')
#: ⛔⛭⛭ AND ARM ②'s SECOND CLAUSE IS FALSIFIED BY THE SENTENCE FIX, having been scored a HIT twice.
#:   I registered "at least 30 namesake spectra with no counterpart" and scored it 52, then 32, on
#:   a figure-printing set the crude sentence test had inflated.  ** On the precise test it is 22,
#:   below the floor I set. **  *Recorded as a miss rather than re-floored: the clause was mine to
#:   choose, and the number that falsified it is the same fix that shrank the list.*
check(f'Ⓒ① the unbanked count is scored on RESOLVED PATHS and arm ②\'s floor of 30 is recorded as '
      f'FALSIFIED: {len(no_sib)} distinct namesake spectrum PATHS read by a figure-printing '
      f'candidate have no arm-of-record counterpart, against the 30 I registered',
      len(no_sib) == 22 and len(no_sib) < 30,
      f'{len(no_sib)} without a counterpart; arm \u2461 floor 30 -> FALSIFIED')
#: ⛔⛭⛭⛭ AND THIS IS THE FINDING ITEM 2 TURNS ON, measured rather than assumed: the order says
#:   "re-derive the cheapest half of them", which presumes a cheap half exists.  ** It does not. **
#:   Only TWO of the 54 figure-printing items have an arm-of-record sibling banked for EVERY
#:   namesake they read; the other 52 need at least one spectrum BUILT before anything can be
#:   repointed.  *So "the cheapest half" is not 27 repointings, it is 2 repointings and 52 builds,
#:   and which 27 are cheapest is a question about build cost, not about the bank.*
check(f'Ⓒ② ⛭⛭ ITEM 2\'s "CHEAPEST HALF" IS SCORED ON RESOLVED PATHS: {len(cheap)} of '
      f'{len(prints_fig)} items are re-derivable by repointing alone, {len(expensive)} need a '
      f'spectrum built first or carry an undecidable token -- so the cheap set is a small '
      f'minority rather than half',
      len(cheap) + len(expensive) == len(prints_fig) and len(cheap) < len(prints_fig) / 4,
      f'{len(cheap)} cheap, {len(expensive)} expensive of {len(prints_fig)}')

# ══ the twelve ══════════════════════════════════════════════════════════════════════════════════
head('Ⓓ  THE TWELVE r7640+60 SAYS TODAY\'S INSTRUMENT CANNOT REBUILD')
live = {}
for stem in TWELVE:
    users = [pth for pth in body_cited if any(stem in n for n in cand[pth]['namesake'])]
    if users:
        live[stem] = users
for stem in TWELVE:
    print(f'      {stem:24s} read by {len(live.get(stem, [])):2d} body-cited receipt(s)')
#: ⛔⛭ ARM ③ FALSIFIED, AND IN THE DIRECTION THAT MATTERS FOR THE ORDER.  I registered that at
#:   least EIGHT of the twelve are read by a receipt the paper cites.  THREE are: `c54.175`,
#:   `c54.177` and `c54.178`.  ** So the twelve are very largely NOT a live dependency of the
#:   paper's own sentences -- nine of them are read only by receipts no body sentence cites. **
#:   *Which makes them cheaper to leave un-rebuilt than I registered, and says the order's
#:   "include the twelve" is a completeness instruction rather than a nine-item backlog.*
check(f'Ⓓ① the twelve are PINNED at how many are read by a body-cited receipt, and arm ③\'s '
      f'">= 8" is recorded as FALSIFIED: {len(live)} of 12 live '
      f'({", ".join(sorted(live)) if live else "none"})',
      len(live) == 1 and set(live) == {'c54.178'} and len(live) < 8,
      f'{len(live)} of 12 live; arm \u2462 registered >= 8 -> FALSIFIED badly')

# ══ the explainer ═══════════════════════════════════════════════════════════════════════════════
exp = texts.get('EXPLAINER.md', '')
exp_cites = [pth for pth in cand if '\\rcpt{' + os.path.basename(pth)[:-3] + '}' in exp]
check(f'Ⓓ② ARM ④ AS REGISTERED: `EXPLAINER.md` cites none of the candidates through a `\\rcpt` -- '
      f'scored {len(exp_cites)}',
      len(exp_cites) == 0, f'{len(exp_cites)} explainer citations')

#: ⛔⛭⛭ HOW MANY OF THE LIST ARE THERE ON EVIDENCE, AND HOW MANY CONSERVATIVELY.  210 of the 348
#:   load sites in scope cannot be decided from the source at all -- the filename's stem comes from
#:   a variable -- so a receipt whose every load site is undecidable is kept ON the list when it
#:   also carries a namesake token.  ** That is a deliberate over-inclusion and it must be visible,
#:   because 69 would otherwise spend a build budget on items that may already be on the arm of
#:   record. **
_loads_nm = [q for q in prints_fig if cand[q]['sites'].get('namesake')]
_undec_only = [q for q in prints_fig if not cand[q]['sites'].get('namesake')]
print(f'      of the {len(prints_fig)} items: {len(_loads_nm)} LOAD a namesake (evidence), '
      f'{len(_undec_only)} are kept on the list only because every load site is undecidable')
check(f'Ⓒ③ ⛭⛭ THE LIST SEPARATES EVIDENCE FROM CONSERVATIVE INCLUSION: {len(_loads_nm)} of '
      f'{len(prints_fig)} items demonstrably LOAD a namesake; {len(_undec_only)} are on the list '
      f'only because none of their load sites could be decided from the source, so they are '
      f'candidates for a READ rather than for a rebuild',
      len(_loads_nm) + len(_undec_only) == len(prints_fig) and len(_loads_nm) > 0,
      f'{len(_loads_nm)} on evidence, {len(_undec_only)} conservative')

#: ⛭⛭ WHERE THIS INSTRUMENT STOPS, AND WHY THAT IS A RESULT RATHER THAN A LIMIT ADMITTED LATE.
#:   Four cuts: filename -> path -> load site -> call site.  The last one moved the list by one item
#:   and the evidence split by two, and did NOT move the headline (`0 cheap`) at all.  The 220 load
#:   sites still undecidable are loop variables, dict comprehensions and module-level constants --
#:   ** resolving them is a READING task on 22 receipts, not a fifth instrument. **  Said here so
#:   that nobody spends a fifth iteration discovering the same convergence.
check(f'Ⓒ④ ⛭ THE INSTRUMENT HAS CONVERGED ON THE ANSWER THAT MATTERS: the call-site pass moved '
      f'the list to {len(prints_fig)} items and the evidence split to {len(_loads_nm)}/'
      f'{len(_undec_only)}, and left the cheap count at {len(cheap)} -- so the remaining '
      f'{site_tally["undecidable"]} undecidable sites are a reading task on {len(_undec_only)} '
      f'receipts rather than a further instrument',
      len(cheap) == 0 and len(_undec_only) < len(_loads_nm) + 10,
      f'{len(cheap)} cheap; {len(_undec_only)} to read')

# ══ THE LIST ════════════════════════════════════════════════════════════════════════════════════
head('THE UNFILTERED LIST -- every figure-printing item, its receipt, its spectra, its sentence')
for i, pth in enumerate(sorted(prints_fig), 1):
    d = cand[pth]
    has, lacks = (cheap.get(pth) or expensive.get(pth))
    print(f'  [{i:02d}] [{d["paper"]}] {pth}')
    print(f'       spectra read (namesake/superseded): {d["namesake"]}')
    if d['aor']:
        print(f'       also reads arm-of-record: {d["aor"]}')
    #: ⛔ r7671+cc66.4 -- this line said "YES" for an item the cheap/expensive split counts
    #:   EXPENSIVE, because `cheap` also requires that no load site be undecidable and the printed
    #:   line did not.  An undecidable site means the receipt MIGHT already read the arm of record,
    #:   so the repointing is not known to be available.  Stated here as it is scored.
    _blocked = bool(d['undecidable'])
    if has and not lacks and not _blocked:
        _verdict = 'YES -- ' + str(has)
    elif has and not lacks:
        _verdict = ('NO -- an arm-of-record sibling is banked for every namesake it loads '
                    + str(has) + ', but ' + d['undecidable'][0] + ' leaves the repointing undecided')
    else:
        _verdict = 'NO'
    print(f'       re-derivable by repointing: {_verdict}'
          + (f';  no banked sibling for {lacks}' if lacks else ''))
    for f, ss in sorted(body_cited[pth].items()):
        for s in dict.fromkeys(ss):          #: one citation per DISTINCT sentence
            print(f'       {f}: "{s[:400]}"')
print()
print(f'  TOTALS: {len(prints_fig)} figure-printing items; {len(cheap)} cheap, '
      f'{len(expensive)} expensive; {len(no_sib)} namesake spectra unbanked; '
      f'{len(live)} of the twelve live; {len(gen_only)} generated-appendix-only.')

print('\n' + '=' * 100)
if fail:
    print('  FAILED:')
    for f in fail:
        print(f'    - {f}')
    sys.exit(1)
print('  ✓ ALL CHECKS PASSED')
print('=' * 100)
